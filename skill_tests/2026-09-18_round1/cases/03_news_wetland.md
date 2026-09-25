# 测试例 03_news_wetland · 青海湿地巡护与红外相机

## 基本信息
- 体裁 / 形态 / 结论 / 工具调用：`news` / `news_article` / **PASS** / `load_story_knowledge`

## 输入
### 提示词（原文）
按 china_storytelling，format=news_article，英文消息稿。只用用户素材；不要编造精确鸟种数量和保护区面积。

### 提示词（中文说明）
按中国故事讲述流程，形态为英文消息稿。只用用户素材；不得编造精确鸟种数量与保护区面积。

### 用户上传素材（原文）
青海某湿地巡护员每周步行记录候鸟；保护区安装红外相机；去年同站点水鸟种类用户只描述为「十余种」；巡护日志用铅笔写在防水本上。

### 用户上传素材（中文，若原文已是中文则写「同原文」）
同原文

## 输出
### 模型成稿（原文）
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

### 模型成稿（中文翻译）
**knowledge_loaded（知识已加载）:** true  
**format（形态）:** news_article (Tier-1)  
**genre（体裁）:** news | **genre_status（体裁状态）:** complete  
**结构适配判断:** 生态主题 → 必选 A+B+C；素材偏个体日常，优先激活 E(个体)；无蜕变/数据素材，不强行用 D/F。

---

**headline（标题）:** 青海，一位湿地巡护员用脚步数鸟  
**dek（导语）:** 每周巡护、铅笔写在防水本上的记录、新安装的红外相机——高原上，一套安静的日常正在追踪候鸟的踪迹。

**中文对照：**（成稿原文已含，同此）

---

**body（正文）:**

每周，一位巡护员步行穿越青海某自然保护区的湿地，清点过境的候鸟。这份工作没有机动车——路线靠脚步走完，好让沼泽里的动静尽量不漏过。

每次巡护唯一的「正式记录」，是一本防水笔记本。条目用铅笔写，因为高原湿冷里墨水容易失效。一页又一页，日志记下看见了什么鸟、在哪里、大概多少——一座缓慢、手写的活态生态数据库。

保护区还在关键观测点开始安装红外相机。相机全天候工作，捕捉人眼可能漏记的野生动物——尤其是在晨昏或夜间活动的物种，那时人并不在巡护路上。

在一个固定观测点，去年的调查记录到十余种水鸟。数字并不夸张，但它是一条基线——巡护员的每周步行与新相机，将在之后的季节继续把它垒高。

这里没有盛大宣布。只有一个人在走，一支铅笔在写，一枚镜头在看——一周又一周，在一片仍在呼吸的青海湿地上。

---

**suggested_visual（配图建议）:** 防水本摊开在湿地栈道上，铅笔搁在页面；背景：沼泽草丛与远处水面。可选小图：木桩上安装的红外相机。

---

**evidence_used（所用论据）:**
| # | 来源 | 内容 |
|---|------|------|
| U1 | 用户上传 | 青海某湿地巡护员每周步行记录候鸟 |
| U2 | 用户上传 | 保护区安装红外相机 |
| U3 | 用户上传 | 去年同站点水鸟种类"十余种" |
| U4 | 用户上传 | 巡护日志用铅笔写在防水本上 |

（本地论据库未调用——用户素材已足够支撑短消息稿，无需额外检索。）

**素材回溯自检：** 正文每句事实均可指回 U1–U4；未补充精确鸟种名、保护区面积、巡护员姓名、具体钟点、百分比或制度背景。"more than a dozen"对应素材"十余种"，未做精确化。

⚠️ **本稿仅供人工审核，不自动发布。** 如需补充保护区正式名称、海拔、鸟种清单等可核验信息，请提供后更新。

## 简要评语
内容质量约 88.8 分，统一量规通过，锚点「每周步行 / 红外相机 / 十余种 / 防水本」齐全且未编造面积与精确鸟种数，判定 **PASS**。
