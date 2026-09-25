# 通稿工序卡（体裁：通稿 news）

**何时用**：新闻通稿 / Across China（中国各地通讯）/ 短消息 / `press_kit`（对外素材包）/ newsletter（邮件简报）。  
**不用**：社交帖、特稿南周长弧、短视频分镜、GenZ（Z 世代）种草。  
**细则**：`china-story-news-reference.md`。铁律：`intl-comm.md`（国际传播）+ evidence（证据规则）。

## 步骤

1. 按材料厚度选：短消息 vs 通讯（宁短勿编）
2. 骨架顺序（可合并）：地点反差 → 场景 → 具名人物（有证据才写）→ 时间转折 → 机制 → 权威句 → 数据 → 模式点到收束
3. 第三人称、冷静；无 emoji（表情）/ Imagine（想象式开场）/ Would you visit（你会去吗式 CTA）/ 5W 帖文腔
4. 每句事实映射 evidence（证据）；离题库条目不写进正文
5. 即使用户要求 IG（Instagram）/ GenZ（Z 世代种草）→ **仍出通稿**

## 输出字段

| format（成品形态） | 主字段（括号内为中文） |
|--------------------|------------------------|
| `news_article` 新闻稿 | `headline`（标题）/ `dek`（副题或导语摘要）/ `article`（正文）；可选 `pull_quote`（提引句）/ `suggested_visual`（建议配图） |
| `newsletter_brief` 邮件简报 | `subject_line`（邮件主题）/ `preview_text`（预览句）/ `body`（正文）/ `cta`（行动号召，通稿式） |
| `press_kit` 对外素材包 | `news_blurb`（短消息）/ `headline_pack`（标题组）/ `key_facts`（要点）+ 可选块；缺块写 `omitted_reason`（省略原因） |

篇幅参考：英 450–900 词通讯或更短消息；用户 `max_words`（字数上限）优先。

## 红线

- 禁帖文式 CTA（行动号召）/ emoji（表情）；禁口号墙收束  
- 无证据不写姓名职务数据对话  
- 不为凑长而编机制  
