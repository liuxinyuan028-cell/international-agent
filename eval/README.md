# Skill 评测文件说明（只放评价标准）

**本目录只保留量规与空白模板，不存放测试成稿与运行结果。**

测试成果（输入、输出、中文翻译、打分表）统一放在：

→ [`../skill_tests/`](../skill_tests/)

例如本轮：[`../skill_tests/2026-09-18_round1/`](../skill_tests/2026-09-18_round1/)

---

**上传规则（必须遵守）**：只上传用户明确要求公开的**最终结果**；讨论稿、推演过程、对话纪要、本机训练脚本/输出一律不推送。

## 当前可公开（评价标准）

| 文件 | 用途 |
|------|------|
| `CONTENT_QUALITY_RUBRIC_v1.md` | 成稿符合度定稿表（含权重） |
| `LIT_DIMENSION_BANK.md` | 文献维度库 |
| `UNIFIED_SCORECARD_v1.md` | 工程打分卡（Shared + 体裁插件） |
| `MATERIALS_FLEX_PROMPT_COMPLIANCE_RUBRIC.md` | 用料/提示遵从细则 |

## 空白模板

| 文件 | 用途 |
|------|------|
| `skill_eval_template.csv` | 测试题空白表 |
| `skill_changelog_template.csv` | 改动记录空白表 |
| `skill_eval_summary_template.csv` | 汇总空白表 |

跑批脚本在 `skill_tests/run_skill_eval_10.py`，结果写入 `skill_tests/`，**不要**写入本目录。
