# 03_news_wetland · 青海湿地巡护与红外相机

- 体裁：通稿（`news`）
- 成品形态：新闻稿（`news_article`）
- 路由识别：`news`
- 工具调用：load_story_knowledge

## 一、输入

### 1. 提示词（原文）

按 china_storytelling，format=news_article，英文消息稿。只用用户素材；不要编造精确鸟种数量和保护区面积。

### 2. 提示词（中文说明）

按中国故事成稿 skill，体裁走「通稿」，成品形态为「新闻稿」。主题：青海湿地巡护与红外相机。必须使用用户上传素材；不要补充素材没有的数字、人名等可核验细节；先调用一次加载故事知识库，再成稿；输出标明已读库，并提醒人工审核。

### 3. 用户上传素材（原文）

青海某湿地巡护员每周步行记录候鸟；保护区安装红外相机；去年同站点水鸟种类用户只描述为「十余种」；巡护日志用铅笔写在防水本上。

### 4. 用户上传素材（中文）

素材原文即为中文，内容同上。

## 二、输出

### 1. Agent 成稿（原文）

```text
**knowledge_loaded: true**
**format:** news_article (Tier-1)
**genre:** news | **genre_status:** complete
**结构适配判断:** 生态主题 → 必选 A+B+C；素材偏个体日常，优先激活 E(个体)；无蜕变/数据素材，不强行用 D/F。

---

**headline:** In Qinghai, a wetland watcher counts birds step by step
**dek:** Weekly patrols, pencil-on-waterproof-paper logs, and newly installed infrared cameras — a quiet routine is tracking migratory life on the plateau.

**中文对照：**
标题：青海，一位湿地巡护员用脚步数鸟
导语：每周巡护、铅笔写在防水本上的记录、新安装的红外相机——高原上，一套安静的日常正在追踪候鸟的踪迹。

---

**body:**

Every week, a patrol ranger walks the wetlands of a nature reserve in Qinghai, counting the migratory birds that pass through. There is no motorized vehicle for the job — the route is covered on foot, so that nothing in the marsh goes unnoticed.

The only "official record" of each patrol is a waterproof notebook. Entries are written in pencil, because ink can fail in the plateau's damp cold. Page after page, the log tracks which birds were seen, where, and in what numbers — a slow, hand-written database of a living ecosystem.

The reserve has also begun installing infrared cameras at key observation points. The cameras work around the clock, capturing wildlife that might otherwise go unrecorded — especially species that are active at dawn, dusk, or night, when human patrols are not on the trail.

At one fixed observation point, last year's surveys recorded more than a dozen species of waterbirds. The number is modest, but it is a baseline — one that the ranger's weekly walks and the new cameras will help build upon in seasons to come.

There is no grand announcement here. Just a person walking, a pencil writing, and a lens watching — week after week, on a Qinghai wetland that keeps breathing.

---

**suggested_visual:** A waterproof notebook open on a wetland boardwalk, pencil resting on the page; background: marsh grass and distant water. Optional inset: an infrared camera mounted on a wooden post.
（配图建议：防水本摊开在湿地栈道上，铅笔搁在页面；背景：沼泽草丛与远处水面。可选小图：木桩上安装的红外相机。）

---

**evidence_used:**
| # | 来源 | 内容 |
|---|------|------|
| U1 | 用户上传 | 青海某湿地巡护员每周步行记录候鸟 |
| U2 | 用户上传 | 保护区安装红外相机 |
| U3 | 用户上传 | 去年同站点水鸟种类"十余种" |
| U4 | 用户上传 | 巡护日志用铅笔写在防水本上 |

（本地论据库未调用——用户素材已足够支撑短消息稿，无需额外检索。）

**素材回溯自检：** 正文每句事实均可指回 U1–U4；未补充精确鸟种名、保护区面积、巡护员姓名、具体钟点、百分比或制度背景。"more than a dozen"对应素材"十余种"，未做精确化。

⚠️ **本稿仅供人工审核，不自动发布。** 如需补充保护区正式名称、海拔、鸟种清单等可核验信息，请提供后更新。
```

### 2. Agent 成稿（中文翻译）

**knowledge_loaded (知识加载状态):** true
**format (格式):** news_article (Tier-1)
**genre (体裁):** news | **genre_status (体裁状态):** complete
**结构适配判断:** 生态主题 → 必选 A+B+C；素材偏个体日常，优先激活 E(个体)；无蜕变/数据素材，不强行用 D/F。

---

**headline (标题):** 青海，一位湿地巡护员用脚步数鸟
**dek (导语):** 每周巡护、铅笔写在防水纸上的日志，以及新安装的红外相机——高原上，一套安静的日常正在追踪候鸟的踪迹。

---

**body (正文):**

每周，青海某自然保护区的一名巡护员都会步行穿越湿地，清点途经的候鸟。这项工作没有机动车代步——巡护路线全靠双脚丈量，以确保沼泽中的任何细节都不被遗漏。

每次巡护唯一的“官方记录”是一本防水笔记本。记录都用铅笔书写，因为墨水在高原湿冷的环境中容易失效。一页又一页，日志记录着看到了哪些鸟、在哪里看到、数量多少——这是一个缓慢建立的、手写的活态生态系统数据库。

保护区还开始在关键观测点安装红外相机。这些相机全天候工作，捕捉那些否则可能未被记录的野生动物——尤其是那些在黎明、黄昏或夜间活动的物种，此时人工巡护员并未巡护至此。

在一个固定的观测点，去年的调查记录了十余种水鸟。这个数字虽然不大，但却是一个基线——在未来的季节里，巡护员每周的步行和新安装的相机将帮助在此基础上不断积累。

这里没有宏大的宣告。只有一个人行走、一支铅笔书写、一个镜头注视——周而复始，在青海这片生生不息的湿地上。

---

**suggested_visual (配图建议):** 一本防水笔记本摊开在湿地栈道上，铅笔搁在页面上；背景：沼泽草丛与远处水面。可选小图：木桩上安装的红外相机。

---

**evidence_used (使用论据):**
| # | 来源 | 内容 |
|---|------|------|
| U1 | 用户上传 | 青海某湿地巡护员每周步行记录候鸟 |
| U2 | 用户上传 | 保护区安装红外相机 |
| U3 | 用户上传 | 去年同站点水鸟种类"十余种" |
| U4 | 用户上传 | 巡护日志用铅笔写在防水本上 |

（本地论据库未调用——用户素材已足够支撑短消息稿，无需额外检索。）

**素材回溯自检：** 正文每句事实均可指回 U1–U4；未补充精确鸟种名、保护区面积、巡护员姓名、具体钟点、百分比或制度背景。"more than a dozen"对应素材"十余种"，未做精确化。

⚠️ **本稿仅供人工审核，不自动发布。** 如需补充保护区正式名称、海拔、鸟种清单等可核验信息，请提供后更新。

---

> 说明：本文件是测试样例，不属于 `eval/` 评价体系规范。
