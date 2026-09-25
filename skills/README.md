# Skills 目录

主 Skill = 短工序卡（何时用 / 步骤 / 输出 / 红线）。  
长依据放 `*-reference.md`（参考附录）或 `docs/corpus/`（语料目录），**默认不整篇注入**。

```text
skills/
├── README.md                 ← 本说明
├── entry/                    ← 成稿入口（先认体裁，再读库）
│   ├── china-storytelling.md
│   ├── china-storytelling-reference.md
│   └── china-story-active.md
├── shared/                   ← 所有体裁共用的铁律
│   ├── intl-comm.md
│   └── evidence-user-materials.md
└── genres/                   ← 一体裁一文件夹
    ├── README.md             ← 路由表 + 成品形态对照
    ├── post/                 ← 帖文
    ├── news/                 ← 通稿
    ├── feature/              ← 特稿
    ├── script/               ← 短视频脚本
    └── faq/                  ← 误解澄清
```

## entry/ 入口

| 文件 | skill_id（技能编号） | 内容 |
|------|----------------------|------|
| `china-storytelling.md` | `china_storytelling` | 成稿总入口：认体裁 → 定成品形态 → 读库一次 → 只开一本体裁工序卡 |
| `china-storytelling-reference.md` | — | 入口长表附录（常用/进阶形态、结构适配等） |
| `china-story-active.md` | `china_story_active` | 主动选题时的路由短卡 |

## shared/ 共用规则

| 文件 | skill_id | 内容 |
|------|----------|------|
| `intl-comm.md` | `intl_comm` | 团队铁律：证据绑定、语气、少抬杠、人工审核 |
| `evidence-user-materials.md` | `evidence_user_materials` | 用户上传 ∪ 本地库双源论据；禁止常识偷补 |

## genres/ 体裁分册

每个子文件夹里通常有：**主工序卡** + **reference（参考附录）**。

| 子文件夹 | 主文件 | 附录 | 状态 | 写什么 |
|----------|--------|------|------|--------|
| `post/` 帖文 | `china-story-post.md` | `china-story-post-reference.md` | 已完善 | 海外社交帖 / 长帖串 / 图文配文；5W |
| `news/` 通稿 | `china-story-news.md` | `china-story-news-reference.md` | 已完善 | 通稿 / 消息 / 对外素材包 |
| `feature/` 特稿 | `china-story-feature.md` | `china-story-feature-reference.md` | methods_in（方法已入库） | 特稿 / 深度 / 长文 |
| `script/` 脚本 | `china-story-script.md` | `china-story-script-reference.md` | methods_in | 短视频分镜；语料在 `docs/corpus/script/` |
| `faq/` 澄清 | `china-story-faq-mythbust.md` | `china-story-faq-mythbust-reference.md` | methods_in | 误解→事实澄清清单 |

总路由表：`genres/README.md`  
代码路由：`tools/genre_router.py`（体裁路由器）  
读库门禁：`tools/load_story_knowledge.py`（加载故事知识库）  
注册路径：`config/skills.yaml`

**默认体裁：** 帖文 post  

**Tier-1 常用成品形态：**  
`social_post`（单帖）/ `thread`（长帖串）/ `news_article`（新闻稿）/ `visual_story`（图文轮播）/ `short_video`（短视频脚本）/ `press_kit`（对外素材包）
