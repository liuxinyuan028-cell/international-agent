"""10 题 Skill 测评：五体裁各 2 题，按 eval 量表打分。

轨 A：CONTENT_QUALITY_RUBRIC_v1（ROC 加权，1–5 → 百分）
轨 B：UNIFIED_SCORECARD_v1（共享 S/30 + 帖文P或通稿N/15；其余体裁仅报共享层）

结果：skill_tests/<日期>/scores/
"""

from __future__ import annotations

import io
import json
import os
import re
import sys
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple

os.environ.setdefault("PYTHONIOENCODING", "utf-8")
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")  # type: ignore[attr-defined]
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")  # type: ignore[attr-defined]
except Exception:
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from agent.reactagent import stream  # noqa: E402
from tools.genre_router import detect_genre  # noqa: E402

# CONTENT_QUALITY 全局权重
CQ_WEIGHTS = {
    "accuracy": 0.318,
    "examples": 0.145,
    "logic": 0.058,
    "localize": 0.141,
    "interest": 0.073,
    "engage": 0.040,
    "natural": 0.017,
    "authority": 0.109,
    "evidence_support": 0.036,
    "polite": 0.063,
}

CASES: List[Dict[str, Any]] = [
    {
        "id": "01_post_grape",
        "genre": "post",
        "format": "social_post",
        "theme": "宁夏葡萄园滴灌与嫁接笔记",
        "prompt": (
            "按 china_storytelling，format=social_post，platform=instagram，"
            "country=America，语气 optimistic，英文。必须使用下方用户上传素材，"
            "不要补充素材没有的产量、人名和融资额。"
        ),
        "material": (
            "宁夏某葡萄产区曾是砾石荒地；合作社使用滴灌；"
            "一位种植户保留了失败嫁接记录本；参观者可摸到滴灌管外壁的冷凝水。"
        ),
        "anchors": ["砾石荒地", "滴灌", "失败嫁接记录本", "冷凝水"],
    },
    {
        "id": "02_post_lacquer",
        "genre": "post",
        "format": "thread",
        "theme": "福建漆器修复师与学徒补色",
        "prompt": (
            "按 china_storytelling，format=thread，platform=twitter，英文。"
            "用用户素材讲完一个小故事；不要虚构荣誉称号和游客人次。"
        ),
        "material": (
            "福建一位漆器修复师用三年修好一件破损屏风；学徒先练半年补色；"
            "博物馆保留了修复前后对比照片；屏风缺角曾用木屑临时填过。"
        ),
        "anchors": ["三年", "破损屏风", "半年补色", "对比照片", "木屑"],
    },
    {
        "id": "03_news_wetland",
        "genre": "news",
        "format": "news_article",
        "theme": "青海湿地巡护与红外相机",
        "prompt": (
            "按 china_storytelling，format=news_article，英文消息稿。"
            "只用用户素材；不要编造精确鸟种数量和保护区面积。"
        ),
        "material": (
            "青海某湿地巡护员每周步行记录候鸟；保护区安装红外相机；"
            "去年同站点水鸟种类用户只描述为「十余种」；巡护日志用铅笔写在防水本上。"
        ),
        "anchors": ["每周步行", "红外相机", "十余种", "防水本"],
    },
    {
        "id": "04_news_presskit",
        "genre": "news",
        "format": "press_kit",
        "theme": "中非滴灌示范园出苗",
        "prompt": (
            "按 china_storytelling，format=press_kit。"
            "输出短消息、标题组、要点；材料不够的块写 omitted_reason。"
            "不要编造增产百分比和吨数。英文。"
        ),
        "material": (
            "中非某农业合作示范园教当地农户使用滴灌；中方农技员与当地翻译一起下田；"
            "第一季作物出苗更整齐；示范田边竖着中非双语说明牌。"
        ),
        "anchors": ["滴灌", "翻译一起下田", "出苗更整齐", "双语说明牌"],
    },
    {
        "id": "05_feature_garden",
        "genre": "feature",
        "format": "longform",
        "theme": "苏州园林修复保留太湖石",
        "prompt": (
            "按 china_storytelling，format=longform，写英文特稿。"
            "须有一句话主心骨；场景细节只能来自素材；不要编游客人次和对话钟点。"
        ),
        "material": (
            "苏州一处园林修复工程保留了原有太湖石摆放位置；工匠用传统灰浆修补墙面裂缝；"
            "参观者可沿原游线步行；一块太湖石底部仍留有旧编号漆迹。"
        ),
        "anchors": ["太湖石", "传统灰浆", "原游线", "旧编号漆迹"],
    },
    {
        "id": "06_feature_lab",
        "genre": "feature",
        "format": "longform",
        "theme": "合肥折叠屏样机临时胶带测试",
        "prompt": (
            "按 china_storytelling，format=longform，英文特稿，严肃语气。"
            "不要编造量产日期和融资额；聚焦素材里的临时测试细节。"
        ),
        "material": (
            "合肥某实验室展示可折叠显示样机；工程师用胶带固定柔性电路做临时测试；"
            "没有公布量产时间；工作台上散落着剪开的导热垫碎片。"
        ),
        "anchors": ["可折叠显示样机", "胶带", "柔性电路", "导热垫碎片"],
    },
    {
        "id": "07_script_tea",
        "genre": "script",
        "format": "short_video",
        "theme": "茶席分享与热水声",
        "prompt": (
            "按 china_storytelling，format=short_video，约 35 秒英文口播分镜。"
            "须有 Hook 0-3 秒；不要编假精确钟点和销售额。"
        ),
        "material": (
            "朋友来访时主人温杯、注水、分茶；热水注入盖碗时有一声轻响；"
            "桌上只有一把壶和两只杯；客人说这茶比想象中更淡、更干净。"
        ),
        "anchors": ["温杯", "盖碗", "轻响", "两只杯", "更淡、更干净"],
    },
    {
        "id": "08_script_bashi",
        "genre": "script",
        "format": "short_video",
        "theme": "四川坝坝市夜摊与竹凳",
        "prompt": (
            "按 china_storytelling，format=short_video，英文分镜 30-45 秒。"
            "一视频一个主点；结尾只要一个软 CTA；不要编摊位数和营收。"
        ),
        "material": (
            "四川某夜市坝坝市，摊主把竹凳沿路边摆开；灯光来自悬挂的灯泡；"
            "一位食客用筷子夹起刚出锅的串串；油烟在镜头前短暂模糊。"
        ),
        "anchors": ["竹凳", "悬挂的灯泡", "串串", "油烟"],
    },
    {
        "id": "09_faq_food",
        "genre": "faq",
        "format": "faq_mythbust",
        "theme": "中国食物常见误解澄清",
        "prompt": (
            "按 china_storytelling，format=faq_mythbust，英文。"
            "只依据用户素材列 Myth+Fact；不要抄外网统计数字；不要攻击目标国受众。"
        ),
        "material": (
            "常见误解一：中国人每天都吃狗肉。可核验表述：狗肉并非日常主食，多数家庭日常是米饭、面、蔬菜和常见肉类。"
            "常见误解二：中国菜只有很辣很油。可核验表述：各地口味差异大，清淡蒸煮同样常见。"
            "常见误解三：用筷子等于不卫生。可核验表述：公筷分餐在不少场合已推广；家庭也可做到餐具清洁。"
            "不要编造全国消费百分比。"
        ),
        "anchors": ["狗肉并非日常主食", "清淡蒸煮", "公筷分餐"],
    },
    {
        "id": "10_faq_travel",
        "genre": "faq",
        "format": "faq_mythbust",
        "theme": "赴华旅行支付与交通误解",
        "prompt": (
            "按 china_storytelling，format=faq_mythbust，英文，受众为美国旅行者。"
            "材料不够宁少条目；禁止编造 App 市场份额。"
        ),
        "material": (
            "误解：去中国只能用现金。事实：大城市商户普遍支持移动支付，部分场景仍可刷卡或现金。"
            "误解：不会中文就无法坐地铁。事实：一线城市地铁常有英文标识与线路图。"
            "误解：外国人不能买高铁票。事实：可持护照在车站窗口或指定渠道购票（以现场规则为准）。"
        ),
        "anchors": ["移动支付", "英文标识", "护照", "购票"],
    },
]


def run_agent(query: str, task_id: str) -> Tuple[str, List[str]]:
    """调用智能体，返回成稿与工具名列表。"""
    tool_names: List[str] = []
    reply = ""
    for chunk in stream(query, task_id=task_id):
        if not isinstance(chunk, dict):
            continue
        ctype = chunk.get("type")
        if ctype == "tool_call":
            name = str(chunk.get("tool_name") or "")
            if name:
                tool_names.append(name)
        elif ctype == "token":
            reply = str(chunk.get("accumulated") or reply)
        elif ctype == "message":
            msg = chunk.get("message")
            content = getattr(msg, "content", None) if msg is not None else None
            if content:
                reply = str(content)
        elif ctype == "state_update":
            state = chunk.get("state") or {}
            if isinstance(state, dict):
                for _node, payload in state.items():
                    if isinstance(payload, dict) and payload.get("messages"):
                        for m in reversed(payload["messages"]):
                            text = getattr(m, "content", None)
                            if text and type(m).__name__.startswith("AI"):
                                reply = str(text)
                                break
    return reply, tool_names


def build_query(case: Dict[str, Any]) -> str:
    """拼装提交给 agent 的提示。"""
    return (
        f"{case['prompt']}\n\n"
        f"主题：{case['theme']}\n\n"
        "【用户上传素材】\n"
        f"{case['material']}\n\n"
        "请先调用一次 load_story_knowledge，再按对应体裁 skill 成稿。"
        "输出须含 knowledge_loaded: true、evidence_used（区分用户上传/本地库如有）、"
        "并提醒人工审核。可核验事实只能来自素材与读库结果。"
    )


def _hit_anchors(text: str, anchors: Sequence[str]) -> List[str]:
    return [a for a in anchors if a and (a in text or a.lower() in text.lower())]


def _has_hallucination_signals(text: str, material: str, prompt: str) -> bool:
    source = f"{material}\n{prompt}"
    if re.search(r"\b\d+(?:\.\d+)?\s*%|\b\d+\s*million\b|\d{1,2}:\d{2}\s*(am|pm)?", text, re.I):
        # allow if also in source
        for m in re.finditer(
            r"\b\d+(?:\.\d+)?\s*%|\b\d+\s*million\b|\d{1,2}:\d{2}\s*(am|pm)?",
            text,
            re.I,
        ):
            token = m.group(0)
            if token not in source and token.lower() not in source.lower():
                return True
    if re.search(r"(碾压|打脸|your country is (backward|failing))", text, re.I):
        return True
    return False


def score_unified(
    case: Dict[str, Any],
    draft: str,
    tools: Sequence[str],
) -> Dict[str, Any]:
    """UNIFIED_SCORECARD：S1–S6 + 帖文P / 通稿N。"""
    text = draft or ""
    lower = text.lower()
    hits = _hit_anchors(text, case["anchors"])
    rate = len(hits) / max(len(case["anchors"]), 1)
    called = "load_story_knowledge" in tools or "knowledge_loaded" in lower

    # S1 coverage
    if rate >= 0.6:
        s1 = 5
    elif rate >= 0.4:
        s1 = 4
    elif rate >= 0.25:
        s1 = 3
    elif hits:
        s1 = 2
    else:
        s1 = 1

    # S2 boundary
    s2 = 2 if _has_hallucination_signals(text, case["material"], case["prompt"]) else 5
    if re.search(r"\b\d+(?:\.\d+)?\s*%", text) and "%" not in case["material"]:
        s2 = min(s2, 2)

    # S3 hard prompt
    s3 = 5
    if "必须使用" in case["prompt"] or "只用用户素材" in case["prompt"] or "必须使用下方" in case["prompt"]:
        if s1 <= 2:
            s3 = 2
    if case["format"] in text or case["format"] in lower or case["genre"] in lower:
        pass
    else:
        s3 = min(s3, 4)
    if not called:
        s3 = min(s3, 2)

    # S4 traceability
    s4 = 5 if ("evidence_used" in lower or "evidence_notes" in lower) and (
        "用户上传" in text or "user" in lower or "source" in lower
    ) else (3 if "evidence_used" in lower else 1)

    # S5 genre fit
    genre = case["genre"]
    if genre == "post":
        fit = ("post" in lower or "five_w" in lower) and not re.search(
            r"\bdateline\b|新华社电", text
        )
    elif genre == "news":
        fit = any(k in lower for k in ["headline", "article", "news_blurb", "key_facts"]) and not bool(
            re.search(r"imagine\b|would you visit|😀|🔥", lower)
        )
    elif genre == "feature":
        fit = any(k in lower for k in ["body", "one_liner", "headline"]) and "five_w" not in lower
    elif genre == "script":
        fit = any(k in lower for k in ["shots", "vo", "on_screen", "hook"])
    else:
        fit = ("myth" in lower and "fact" in lower) or "items" in lower
    s5 = 5 if fit else 2

    s6 = None  # 本题未做无资料对照

    shared_vals = [s1, s2, s3, s4, s5]
    shared_sum = sum(shared_vals)
    shared_pass = shared_sum >= 22 and s2 >= 4 and s1 >= 3

    plugin: Dict[str, Any] = {}
    plugin_sum = 0
    plugin_pass = True
    if genre == "post":
        p1 = 5 if "five_w" in lower and "post" in lower else 2
        p2 = 5 if any(k in lower for k in ["america", "us ", "you", "visitor", "reader"]) else 3
        p3 = 5 if len(text) < 3500 else 3
        plugin = {"P1_5W": p1, "P2_audience": p2, "P3_channel": p3}
        plugin_sum = p1 + p2 + p3
        plugin_pass = plugin_sum >= 10
    elif genre == "news":
        n1 = 5 if any(k in lower for k in ["headline", "article", "news_blurb"]) else 2
        n2 = 4
        n3 = 5 if not re.search(r"imagine\b|would you visit|😀", lower) else 1
        plugin = {"N1_beats": n1, "N2_lexicon": n2, "N3_isolation": n3}
        plugin_sum = n1 + n2 + n3
        plugin_pass = plugin_sum >= 10 and n3 >= 3
    else:
        plugin = {"note": "feature/script/faq 插件位预留，本题仅报共享层"}
        plugin_pass = True

    return {
        "S1_coverage": s1,
        "S2_boundary": s2,
        "S3_hard_prompt": s3,
        "S4_trace": s4,
        "S5_genre_fit": s5,
        "S6_ablation": s6,
        "shared_sum": shared_sum,
        "shared_max": 25 if s6 is None else 30,
        "shared_pass": shared_pass,
        "plugin": plugin,
        "plugin_sum": plugin_sum,
        "plugin_pass": plugin_pass,
        "anchor_hits": hits,
        "total45": shared_sum + plugin_sum if genre in ("post", "news") else shared_sum,
        "pass": shared_pass and plugin_pass and s2 >= 4,
    }


def score_content_quality(case: Dict[str, Any], draft: str, unified: Dict[str, Any]) -> Dict[str, Any]:
    """CONTENT_QUALITY_RUBRIC_v1：1–5 × ROC 权重 → 百分。"""
    s1, s2, s5 = unified["S1_coverage"], unified["S2_boundary"], unified["S5_genre_fit"]
    text = draft or ""
    lower = text.lower()
    dims = {
        "accuracy": s2,  # 与越界强相关
        "examples": min(5, max(1, s1)),
        "logic": 5 if len(text) > 200 else 3,
        "localize": 5 if any(k in lower for k in ["you", "america", "visitor", "reader", "travel"]) else 3,
        "interest": 4 if any(k in lower for k in ["hook", "?", "具体", "scene", "shot"]) or s1 >= 4 else 3,
        "engage": 4 if ("?" in text or "cta" in lower or "would you" in lower) else 3,
        "natural": 2 if re.search(r"remarkable achievement|伟大成就|举世瞩目", text, re.I) else 4,
        "authority": 4 if "evidence_used" in lower else 2,
        "evidence_support": min(5, max(1, unified["S4_trace"])),
        "polite": 1 if re.search(r"打脸|碾压|backward", text, re.I) else 5,
    }
    # 门控：礼貌性冒犯 → 不达标
    gate_fail = dims["polite"] <= 2
    total = sum((dims[k] / 5.0) * CQ_WEIGHTS[k] * 100 for k in CQ_WEIGHTS)
    return {
        "dims": dims,
        "score100": round(total, 1),
        "pass": (not gate_fail) and total >= 70 and dims["accuracy"] >= 4,
        "gate_fail": gate_fail,
    }


def optimize_plan(case: Dict[str, Any], unified: Dict[str, Any], cq: Dict[str, Any]) -> str:
    """根据失分项给优化方案。"""
    tips: List[str] = []
    if unified["S1_coverage"] <= 3:
        tips.append("提高用户专有锚点写入密度，evidence_used 逐条引用素材原句。")
    if unified["S2_boundary"] <= 3:
        tips.append("删除素材外百分比/百万级数字/假钟点；缺数宁省略。")
    if unified["S3_hard_prompt"] <= 3:
        tips.append("强制先调 load_story_knowledge，并落实 format/平台/禁编造硬约束。")
    if unified["S4_trace"] <= 3:
        tips.append("补全 evidence_used，并标注 source_type=用户上传/本地库。")
    if unified["S5_genre_fit"] <= 3:
        tips.append(f"按 {case['genre']} 工序卡补齐主字段，避免体裁串味。")
    if case["genre"] == "post" and isinstance(unified["plugin"], dict):
        if unified["plugin"].get("P1_5W", 5) <= 3:
            tips.append("帖文补齐非空壳 five_w，Says What 只留一个故事点。")
        if unified["plugin"].get("P2_audience", 5) <= 3:
            tips.append("加强 To Whom 当地可感句，避免全球万能稿。")
    if case["genre"] == "news" and isinstance(unified["plugin"], dict):
        if unified["plugin"].get("N3_isolation", 5) <= 3:
            tips.append("通稿去掉 Imagine/emoji/种草 CTA，保持第三人称冷静。")
    if case["genre"] == "script":
        tips.append("检查 Hook 0–3s、shots 行字段齐全、仅一个软 CTA。")
    if case["genre"] == "faq":
        tips.append("确保每条 myth+fact 对立成立，禁止外网统计进 evidence。")
    if case["genre"] == "feature":
        tips.append("强化 one_liner 主心骨与可核验场景，禁止复述范文。")
    if cq["dims"]["natural"] <= 3:
        tips.append("去掉成就口号开篇，改素材场景起笔。")
    if not tips:
        tips.append("本条达标；下一轮加无资料对照题测 S6，或加干扰指令测硬约束。")
    return "；".join(tips)


def main() -> int:
    """跑 10 题并写报告。"""
    out_dir = ROOT / "skill_tests" / datetime.now().strftime("%Y-%m-%d") / "scores"
    out_dir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    rows: List[Dict[str, Any]] = []

    for case in CASES:
        task_id = f"eval10_{case['id']}_{uuid.uuid4().hex[:6]}"
        query = build_query(case)
        routed = detect_genre(query, format_hint=case["format"])
        print(f"\n===== {case['id']} genre={case['genre']} task={task_id} =====", flush=True)
        error = None
        draft = ""
        tools: List[str] = []
        try:
            draft, tools = run_agent(query, task_id)
        except Exception as exc:  # noqa: BLE001
            error = str(exc)
            print(f"ERROR: {error}", flush=True)

        unified = score_unified(case, draft, tools)
        cq = score_content_quality(case, draft, unified)
        plan = optimize_plan(case, unified, cq)
        row = {
            "id": case["id"],
            "theme": case["theme"],
            "genre_expected": case["genre"],
            "genre_routed": routed.get("genre"),
            "format": case["format"],
            "prompt": case["prompt"],
            "material": case["material"],
            "draft": draft,
            "tools": tools,
            "error": error,
            "unified": unified,
            "content_quality": cq,
            "optimize": plan,
            "verdict": "PASS" if (unified["pass"] and cq["pass"] and not error) else "FAIL",
        }
        rows.append(row)
        single = out_dir / f"{case['id']}_{stamp}.json"
        single.write_text(json.dumps(row, ensure_ascii=False, indent=2), encoding="utf-8")
        print(
            f"CQ={cq['score100']} Shared={unified['shared_sum']}/{unified['shared_max']} "
            f"verdict={row['verdict']}",
            flush=True,
        )

    # Markdown summary table
    md_lines = [
        "# Skill 10 题测评报告",
        "",
        f"- 时间：{datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "- 评价标准：`eval/CONTENT_QUALITY_RUBRIC_v1.md` + `eval/UNIFIED_SCORECARD_v1.md`",
        "- 说明：每题均含用户上传素材；feature/script/faq 按规范仅报共享层（插件位预留）",
        "",
        "## 总表",
        "",
        "| 题号 | 体裁 | 主题 | 内容符合度(/100) | 共享层 | 插件 | 结论 | 优化要点 |",
        "| --- | --- | --- | ---: | ---: | ---: | --- | --- |",
    ]
    for r in rows:
        u = r["unified"]
        plugin_cell = (
            f"{u['plugin_sum']}/15"
            if r["genre_expected"] in ("post", "news")
            else "—（预留）"
        )
        shared_cell = f"{u['shared_sum']}/{u['shared_max']}"
        md_lines.append(
            "| {id} | {g} | {t} | {cq} | {s} | {p} | {v} | {o} |".format(
                id=r["id"],
                g=r["genre_expected"],
                t=r["theme"][:16],
                cq=r["content_quality"]["score100"],
                s=shared_cell,
                p=plugin_cell,
                v=r["verdict"],
                o=r["optimize"][:40].replace("|", "/"),
            )
        )

    md_lines.extend(["", "## 分题摘要", ""])
    for r in rows:
        md_lines.extend(
            [
                f"### {r['id']} · {r['theme']}",
                "",
                f"- 期望体裁：{r['genre_expected']} / 路由：{r['genre_routed']} / format：{r['format']}",
                f"- 锚点命中：{', '.join(r['unified']['anchor_hits']) or '无'}",
                f"- 工具：{', '.join(r['tools']) or '无'}",
                f"- 结论：{r['verdict']}；内容符合度 {r['content_quality']['score100']}",
                f"- 优化：{r['optimize']}",
                "",
                "<details><summary>成稿摘录</summary>",
                "",
                "```",
                (r["draft"] or r["error"] or "（空）")[:2500],
                "```",
                "",
                "</details>",
                "",
            ]
        )

    passed = sum(1 for r in rows if r["verdict"] == "PASS")
    md_lines.extend(
        [
            "## 汇总与改进方向",
            "",
            f"- 通过 {passed}/10",
            "- 优先改 skill：证据字段强制输出、体裁字段校验、禁越界数字的成稿自检清单。",
            "- 评测补强：为 feature/script/faq 补插件指标；每题增加无资料对照以测 S6。",
            "",
        ]
    )

    summary_path = out_dir / f"summary_10_{stamp}.md"
    json_path = out_dir / f"summary_10_{stamp}.json"
    summary_path.write_text("\n".join(md_lines), encoding="utf-8")
    json_path.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n报告：{summary_path}", flush=True)
    return 0 if passed == 10 else 1


if __name__ == "__main__":
    raise SystemExit(main())
