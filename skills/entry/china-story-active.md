# 主动内容路由

用户要**选题 / 发帖 / 标签 / 账号运营**等主动内容时用。

## 步骤

1. 主题不清 → 先问清或列方向（不编事实）
2. `detect_genre`（识别体裁）→ 读对应 `genres/<体裁>/`（默认 **帖文 post**）
3. 成稿前 **一次** `load_story_knowledge`（加载故事知识库）
4. 有粘贴资料 → `skills/shared/evidence-user-materials.md`（用户资料双源论据）
5. 展示：论据要点（区分来源）+ 成稿字段 + `genre`（体裁）/（如需）`genre_status`（完善度）
6. 提醒人工审核后再发

## 分流速查

| 用户说法含… | 体裁 genre | 打开 |
|-------------|------------|------|
| 帖文 / Instagram（图片社交）/ thread（长帖串）… | 帖文 post | `genres/post/china-story-post.md` |
| 通稿 / 新闻稿 / 新华体… | 通稿 news | `genres/news/china-story-news.md` |
| 特稿 / 深度 / longform（长文）… | 特稿 feature | `genres/feature/china-story-feature.md` |
| 短视频脚本 / 口播 / 分镜… | 脚本 script | `genres/script/china-story-script.md` |
| 误解澄清 / 辟谣 / FAQ（常见问答）… | 澄清 faq | `genres/faq/china-story-faq-mythbust.md` |
| 未写 | 帖文 post | 同上 |

总表：`genres/README.md`。也可指定成品形态，如 `format=social_post`（单帖）等。

## 默认（用户未指定）

| 项 | 默认值 | 中文 |
|----|--------|------|
| platform | instagram | 平台：图片社交 |
| identity | online_influencer | 身份：网络博主 |
| tone | optimistic | 语气：乐观正面 |
| country | America | 目标国：美国 |
| language | English | 语言：英文 |
| genre | post | 体裁：帖文 |

## 红线

- 必须先调工具；`evidence_used`（已用证据）空/报错 → 如实说明，不假装成功
- 禁止串味；禁止工具结果外编数字/职务/假钟点
- 遵守 `skills/shared/intl-comm.md`（国际传播铁律）+ 当前体裁工序卡
