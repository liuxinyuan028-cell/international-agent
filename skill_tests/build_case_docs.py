"""从 summary JSON 生成 skill_tests 用例文档（输入/输出 + 中文翻译）。"""

from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

GENRE_ZH = {
    "post": "帖文",
    "news": "通稿",
    "feature": "特稿",
    "script": "短视频脚本",
    "faq": "误解澄清 FAQ",
}

FORMAT_ZH = {
    "social_post": "社交单帖",
    "thread": "长帖串",
    "news_article": "新闻稿",
    "press_kit": "对外素材包",
    "longform": "长文特稿",
    "short_video": "短视频分镜",
    "faq_mythbust": "误解澄清清单",
}


def _load_dotenv() -> None:
    env = ROOT / ".env"
    if not env.exists():
        return
    for line in env.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


def translate_to_zh(text: str) -> str:
    """把成稿中的英文叙述译成中文；保留 Markdown 与字段名。"""
    if not text or not text.strip():
        return "（无输出）"

    _load_dotenv()
    api_key = os.environ.get("QWEN_APIKEY") or os.environ.get("DASHSCOPE_APIKEY")
    if not api_key:
        return "（未配置 API Key，未能自动翻译。请对照上方英文原文。）"

    try:
        from openai import OpenAI

        base = os.environ.get("QWEN_BASE_URL") or "https://dashscope.aliyuncs.com/compatible-mode/v1"
        model = os.environ.get("QWEN_MODEL") or "qwen3.6-flash"
        client = OpenAI(api_key=api_key, base_url=base)
        chunks: list[str] = []
        step = 2200
        parts = [text[i : i + step] for i in range(0, len(text), step)] or [text]
        for idx, part in enumerate(parts, start=1):
            print(f"    translate chunk {idx}/{len(parts)}", flush=True)
            prompt = (
                "请将下列讲好中国故事的成稿译成通顺中文。\n"
                "要求：\n"
                "1. 保留 Markdown 标题、表格、列表结构；\n"
                "2. 机读字段名（如 post、headline、shots、vo）保留英文，可在旁加中文括号；\n"
                "3. 正文、旁白、标题、导语等英文叙述必须译成中文；\n"
                "4. 不增删事实，不加评论。\n\n"
                f"【第 {idx}/{len(parts)} 段】\n{part}"
            )
            resp = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.2,
                timeout=120,
            )
            chunks.append((resp.choices[0].message.content or "").strip())
        return "\n\n".join(chunks)
    except Exception as exc:  # noqa: BLE001
        return f"（自动翻译失败：{exc}）\n\n请对照上方英文原文。"


def render_case(row: dict, translation: str) -> str:
    """生成单题 Markdown。"""
    gid = row["id"]
    genre = row["genre_expected"]
    fmt = row["format"]
    lines = [
        f"# {gid} · {row['theme']}",
        "",
        f"- 体裁：{GENRE_ZH.get(genre, genre)}（`{genre}`）",
        f"- 成品形态：{FORMAT_ZH.get(fmt, fmt)}（`{fmt}`）",
        f"- 路由识别：`{row.get('genre_routed')}`",
        f"- 工具调用：{', '.join(row.get('tools') or []) or '无'}",
        "",
        "## 一、输入",
        "",
        "### 1. 提示词（原文）",
        "",
        row.get("prompt") or "（空）",
        "",
        "### 2. 提示词（中文说明）",
        "",
        _prompt_zh(row),
        "",
        "### 3. 用户上传素材（原文）",
        "",
        row.get("material") or "（空）",
        "",
        "### 4. 用户上传素材（中文）",
        "",
        "素材原文即为中文，内容同上。",
        "",
        "## 二、输出",
        "",
        "### 1. Agent 成稿（原文）",
        "",
        "```text",
        (row.get("draft") or row.get("error") or "（空）").rstrip(),
        "```",
        "",
        "### 2. Agent 成稿（中文翻译）",
        "",
        translation.strip(),
        "",
        "---",
        "",
        "> 说明：本文件是测试样例，不属于 `eval/` 评价体系规范。",
        "",
    ]
    return "\n".join(lines)


def _prompt_zh(row: dict) -> str:
    """提示词中文复述。"""
    genre = GENRE_ZH.get(row["genre_expected"], row["genre_expected"])
    fmt = FORMAT_ZH.get(row["format"], row["format"])
    return (
        f"按中国故事成稿 skill，体裁走「{genre}」，成品形态为「{fmt}」。"
        f"主题：{row['theme']}。"
        "必须使用用户上传素材；不要补充素材没有的数字、人名等可核验细节；"
        "先调用一次加载故事知识库，再成稿；输出标明已读库，并提醒人工审核。"
    )


def main() -> int:
    only = {a for a in sys.argv[1:] if not a.startswith("-")}
    src = ROOT / "skill_tests" / "2026-09-18" / "scores" / "summary_10_20260918_210007.json"
    if not src.exists():
        src = ROOT / "eval" / "reports" / "summary_10_20260918_210007.json"
    rows = json.loads(src.read_text(encoding="utf-8"))
    if only:
        rows = [r for r in rows if r["id"] in only]
    out_dir = ROOT / "skill_tests" / "2026-09-18" / "cases"
    out_dir.mkdir(parents=True, exist_ok=True)

    index_rows = json.loads(
        (ROOT / "skill_tests" / "2026-09-18" / "scores" / "summary_10_20260918_210007.json").read_text(
            encoding="utf-8"
        )
    )
    index = [
        "# 2026-09-18 Skill 测试样例索引",
        "",
        "本目录只放**测试输入/输出样例**，评价体系规范仍在 `eval/`。",
        "",
        "| 文件 | 体裁 | 主题 |",
        "|------|------|------|",
    ]
    for row in index_rows:
        index.append(
            f"| [{row['id']}.md]({row['id']}.md) | {GENRE_ZH.get(row['genre_expected'], row['genre_expected'])} | {row['theme']} |"
        )
    index.append("")

    for row in rows:
        print(f"translating {row['id']} ...", flush=True)
        zh = translate_to_zh(row.get("draft") or "")
        md = render_case(row, zh)
        path = out_dir / f"{row['id']}.md"
        path.write_text(md, encoding="utf-8")
        print(f"  wrote {path.name} ({len(zh)} chars zh)", flush=True)

    (out_dir / "README.md").write_text("\n".join(index), encoding="utf-8")
    print("done", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
