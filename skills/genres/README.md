# 体裁工序卡目录（生成链路中的体裁环节）

> 来源合并：国际传播定稿体裁工序卡 + zip 包里的 `content_formats`（内容形态表）  
> + 《南方周末写作课》→ **仅** `feature`（特稿/深度）；**不**用于帖文/通稿。

主文件是短工序卡；长语料/细则在 `*-reference.md`（参考附录）与 `docs/corpus/`（语料），默认不整篇注入。

工序卡是生成过程中的**体裁插件**：共享立场与证据硬约束（`skills/shared/intl-comm.md` + `skills/shared/evidence-user-materials.md`），按用户提示词里的**文本类型**切换不同细节框架。

一体裁一文件夹：`post/` 帖文 · `news/` 通稿 · `feature/` 特稿 · `script/` 脚本 · `faq/` 澄清。每夹内有主工序卡 + `*-reference.md`。

## 一、体裁一览（Agent 必读）

| 体裁 ID | 中文 | Skill 文件 | 状态 | 细节框架（禁止串味） | 主要输出字段 |
|---------|------|------------|------|----------------------|--------------|
| `post` | 帖文 | `post/china-story-post.md` | **已完善** | 5W + 钩子场景骨架 | `five_w`（5W）+ `post`/`hashtags`/`ops_tips`（正文/话题标签/运营提示） |
| `news` | 通稿 | `news/china-story-news.md` | **已完善** | 通稿八步骨架 | `headline`/`dek`/`article`（标题/副题/正文） |
| `feature` | 特稿 | `feature/china-story-feature.md` | **可用** | 南周特稿方法（细则在 reference） | `body`/`one_liner`/`five_dimensions`（正文/主心骨/五维度） |
| `script` | 脚本 | `script/china-story-script.md` | **methods_in**（方法已入库） | Hook-Body-CTA（钩子-主体-行动号召）分镜 | `shots[]`（分镜列表） |
| `faq` | 澄清 | `faq/china-story-faq-mythbust.md` | **methods_in** | Myth→Fact（误解→事实） | `items[]`（条目列表） |

参考附录：各子目录 `*-reference.md`；帖文语料 `docs/corpus/post/`；脚本语料 `docs/corpus/script/`  
共享铁律：`skills/shared/intl-comm.md` + `skills/shared/evidence-user-materials.md`  
字段：`knowledge/content_formats.md`；路由：`tools/genre_router.py`（体裁路由器）；门禁：`load_story_knowledge`（加载故事知识库）

## 二、提示词 → 体裁路由（关键词优先，先匹配先得）

规则顺序：**特稿 feature → 通稿 news → 脚本 script → 澄清 faq → 帖文 post**；都未命中 → 默认 **帖文 `post`**。

| 用户提示词出现… | 路由到 | 说明 |
|-----------------|--------|------|
| 深度报道 / 专题稿 / 特稿 / 长篇深度 / feature / longform（长文）/ in-depth | 特稿 `feature` | 《南方周末写作课》方法；勿用贴文 5W 硬套 |
| 新闻稿 / 新闻通稿 / 通稿 / 消息稿 / 通讯 / 新华体 / press release（新闻稿）/ news wire / Across China（中国各地通讯） | 通稿 `news` | 已完善；与帖文工序卡 **互斥** |
| 短视频脚本 / 视频脚本 / 口播 / 分镜 / reels script / tiktok script / video script / short_video | 脚本 `script` | methods_in；完整分镜 + 钩子规范 |
| 误解澄清 / 辟谣 / FAQ（常见问答）/ mythbust（拆解误解）/ misconception / myth vs fact | 澄清 `faq` | 主动 误解→事实 清单 |
| 帖文 / 发帖 / 社交媒体 / Instagram / Twitter / 微博 / hashtag（话题标签）/ social post / thread（长帖串）/ 长帖 | 帖文 `post` | 已完善；含单帖与长帖串 |
| 未写体裁 | 帖文 `post` | 默认贴文 |

### 成品形态 ID → 本仓库体裁（对照表）

| 成品形态 format ID | 中文 | 本仓库体裁 | 处理 |
|--------------------|------|------------|------|
| `social_post` / `thread` / `caption_only` | 单帖 / 长帖串 / 仅配文 | 帖文 `post` | 已覆盖；长帖串写在帖文工序卡 |
| `visual_story` | 图文轮播 | 帖文 `post`（变体） | 按图文页输出 |
| `news_article` / `newsletter_brief` / `press_kit` | 新闻稿 / 邮件简报 / 对外素材包 | 通稿 `news` | 素材包在通稿工序卡；未齐材料写 `omitted_reason`（省略原因） |
| `longform` | 长文 | 特稿 `feature` | 南周特稿方法 + 字段 |
| `short_video` / `reel_hook` / `youtube_script` | 短视频 / 钩子方案 / 油管脚本 | 脚本 `script` | methods_in；油管长片仍降级/标清 |
| `faq_mythbust` | 误解澄清清单 | 澄清 `faq` | 见澄清工序卡 |
| Tier-2 其余（如 `explainer` 概念解释帖） | — | 暂不单开 | 用户明确要求时再扩展；默认勿猜 |

## 三、所有体裁共享的硬约束（先于体裁细节）

1. **事实边界**：可核验事实/数字/专名/职务/金额/营收/到访人次等 **只能** 来自 `evidence_used`（已用证据 = 用户上传 ∪ 本地库）；禁止常识偷补。
2. **用户资料优先**：有上传时双源合并；无证据则停或只写可核验角度。
3. **立场**：讲好中国故事；不抬杠、不以贬损他国衬托；成稿供人工审核。
4. **体裁隔离**：通稿禁止 GenZ（Z 世代种草）/ emoji（表情）/ Imagine（想象式开场）/ Would you visit（你会去吗）；帖文禁止写成电头长通讯。
5. **完善度**：脚本 / 特稿 / 澄清 方法已入库时可标 `genre_status: methods_in`（方法已入库、评测未齐）。特稿禁止复述南周范文；澄清禁止照搬外部网页数字当证据；脚本禁止假精确时点与无镜头注的空口播。

## 四、生成链路中的位置

```text
用户提示词
  → genre_router.detect_genre()     # 识别体裁
  → 注入国际传播铁律 + 对应体裁工序卡（+ 有资料时用户资料论据工序卡）
  → load_story_knowledge（加载故事知识库）
  → 检索/门控 evidence_used（已用证据）
  → 按体裁字段生成成稿
  → 人工审核
```

## 五、提示词 / 工具对应

| 体裁 | 工具 + 工序卡 | 说明 |
|------|---------------|------|
| 帖文 post | `load_story_knowledge` + 帖文工序卡 | 5W 成稿 |
| 通稿 news | `load_story_knowledge` + 通稿工序卡 | 通稿成稿 |
| 特稿 / 脚本 / 澄清 | `load_story_knowledge` + 对应工序卡 | 以工序卡正文约束 |

## 版本

- v0.5-genres-merge · 2026-09-14 · 合并 zip 体裁字段与路由对照；明确四类体裁完善度
- v0.6-nfzm-feature · 2026-09-14 · 《南方周末写作课》并入特稿；帖文/通稿仍禁用南周长模板
- v0.6.1-repo · 2026-09-14 · 本仓库适配：门禁工具为 `load_story_knowledge`
- v0.7-faq · 2026-09-15 · 新增澄清 faq（faq_mythbust）；依据爬取澄清帖蒸馏；评测待补
- v0.7.1-faq · 2026-09-15 · 全文复核语料清单写入 reference；工序卡升 v0.2
- v0.8-post-corpus · 2026-09-18 · 帖文工序卡爬取社媒/旅行/短视频文案加固；语料落盘 docs/corpus/post
- v0.9-script-methods · 2026-09-18 · 脚本升 methods_in；方法论+转写分镜落盘 docs/corpus/script
- v1.2 · 2026-09-18 · 体裁按子目录分册；入口 entry/；共用规则 shared/
- v1.3 · 2026-09-18 · 主工序卡英文术语补中文释义
