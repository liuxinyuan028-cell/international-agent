---
name: china-storytelling
description: |
  讲好中国故事成稿入口。先识别体裁再读对应体裁工序卡；
  生成前必须调用一次 load_story_knowledge（加载故事知识库）。默认帖文 post。
  Skill 不更新知识库。细则见 skills/entry/china-storytelling-reference.md。
knowledge_dependencies:
  - knowledge/storytelling_framework.txt
  - knowledge/writing_methodology.txt
  - knowledge/content_formats.md
  - knowledge/format_examples.md
  - skills/genres/README.md
  - skills/shared/evidence-user-materials.md
---

# 中国故事成稿（入口）

共用铁律：`skills/shared/intl-comm.md`。主动路由：`china-story-active.md`。长表：`china-storytelling-reference.md`（勿整篇注入）。

## 何时用

用户要主动生成中国故事内容（帖文 / 通稿 / 特稿 / 短视频脚本 / 误解澄清 FAQ 等）。

## 步骤（必须按序）

1. **认体裁**（用 `detect_genre` 识别体裁 / 关键词表）；未写 → 默认 **帖文 `post`**。
2. **定成品形态 format**（如 `social_post` 单帖 / `news_article` 新闻稿 / `short_video` 短视频脚本）；用户说形态没想好 → 先列 **Tier-1 常用形态** 再问，确认后写。
3. **读库一次** `load_story_knowledge`（加载故事知识库，参数含 format 与 topic_hint 主题提示）；仅当 `gate=ready_to_generate`（门禁=可以成稿）才写。
4. **只读一本**对应体裁工序卡（禁止串味）：
   - 帖文 `post` → `genres/post/china-story-post.md`
   - 通稿 `news` → `genres/news/china-story-news.md`
   - 特稿 `feature` → `genres/feature/china-story-feature.md`
   - 短视频脚本 `script` → `genres/script/china-story-script.md`（状态：`methods_in` 方法已入库、评测未齐）
   - 误解澄清 `faq` → `genres/faq/china-story-faq-mythbust.md`（状态同上）
5. 有用户粘贴资料 → 遵守 `skills/shared/evidence-user-materials.md`（用户资料双源论据）。
6. 按该体裁字段输出；附上 `genre`（体裁）/（如需）`genre_status`（体裁完善度）/ `knowledge_loaded: true`（已读库）；提醒人工审核。

## 体裁 → 主输出（速查）

| 体裁 genre | 主字段（括号内为中文） |
|------------|------------------------|
| 帖文 post | `five_w`（5W 要素）+ `post`（帖文正文）/ `hashtags`（话题标签） |
| 通稿 news | `headline`（标题）/ `dek`（副题或导语摘要）/ `article`（正文） |
| 特稿 feature | `body`（正文）/ `one_liner`（一句话主心骨）/ `five_dimensions`（五维度） |
| 脚本 script | `shots[]`（分镜列表） |
| 澄清 faq | `items[]`（条目列表：误解 myth + 事实 fact） |

## 红线

- 未读库不成稿；同轮不重复调 `load_story_knowledge`（加载故事知识库）
- 通稿禁 emoji（表情符号）/ 硬 CTA（强硬行动号召）；帖文禁电头长通讯；FAQ 禁无误解对立硬凑；脚本禁假精确钟点
- 材料没有的数字/姓名/职务/精确秒数 → 不写
- 不抬杠目标国受众；Skill 不改知识库

## 优先级

真实性 > 用户素材 > 知识库 > 体裁写法 > 文采
