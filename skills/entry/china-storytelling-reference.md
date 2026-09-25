# 入口附录（默认不整篇注入）

主工序卡：`china-storytelling.md`。本文件仅在需要对照长表时查阅。

## Tier（形态分层）

| Tier-1 常用形态（默认可选） | Tier-2 进阶形态（用户明确才用） |
|-----------------------------|-------------------------------|
| `social_post` 单帖、`thread` 长帖串、`news_article` 新闻稿、`visual_story` 图文轮播、`short_video` 短视频脚本、`press_kit` 对外素材包 | `explainer` 概念解释帖、`quote_card` 引语卡、`reel_hook` 短视频钩子方案、`caption_only` 仅配文、`longform` 长文、`headline_pack` 标题组、`newsletter_brief` 邮件简报、`youtube_script` 油管脚本、`podcast_script` 播客脚本、`faq_mythbust` 误解澄清、`talking_points` 发言要点、`bilingual_pair` 中英对照 |

字段与样例：`knowledge/content_formats.md` / `format_examples.md`（工具返回摘录）。默认英文海外向。

## 体裁 ↔ 成品形态 format

| 用户说法 / format | 体裁 genre | 主字段 |
|-------------------|------------|--------|
| `social_post` 单帖 / `thread` 长帖串 / `visual_story` 图文 / `caption_only` 仅配文 / 帖文 | 帖文 post | `five_w`（5W）+ `post`/`hashtags`（正文/话题标签） |
| `news_article` 新闻稿 / `press_kit` 素材包 / `newsletter_brief` 简报 / 通稿 | 通稿 news | `headline`/`dek`/`article`（标题/副题/正文） |
| `longform` 长文 / 特稿 / 深度 | 特稿 feature | `body`/`one_liner`/`five_dimensions`（正文/主心骨/五维度） |
| `short_video` 短视频 / `reel_hook` 钩子 / 口播分镜 | 脚本 script | `shots[]`（分镜列表） |
| `faq_mythbust` 误解澄清 / FAQ / 辟谣 | 澄清 faq | `items[]`：myth（误解）+ fact（事实） |

## 结构适配（读 framework 叙事框架后用）

| 主题 | 必选 | 优先扩展 |
|------|------|----------|
| 科技 | A+B+C | D 蜕变, F 数据 |
| 文化 | A+B+C | E 人物, D 蜕变 |
| 生态 | A+B+C | D 蜕变, F 数据 |
| 社会 | A+B+C | E 人物, D 蜕变 |
| 国际合作-项目 | A+B+C | F 数据, E 人物 |
| 国际合作-理念 | A+B+C | H 隐喻 |

先有素材再定结构；不为凑模块而虚构。

## 软虚构禁令

用户未提供则不写：精确钟点/秒数、未给姓名职务、未给年限/百分比/大额数字、未给制度旁支。  
允许：同义改写已给事实；模糊时段；缺料追问或 `omitted_reason`（省略原因）。

## 生成前检查（可选默念）

- 已认 genre（体裁）并读对应体裁工序卡  
- 已调一次 `load_story_knowledge`（加载故事知识库）  
- 无空壳核心、无虚构、缺料已处理  
- 未串味；有用户资料时区分 `source_type`（来源类型）  
- 无口号开篇、无空赞美、不抬杠他国  
