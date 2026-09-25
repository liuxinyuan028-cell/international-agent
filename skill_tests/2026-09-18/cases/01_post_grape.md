# 01_post_grape · 宁夏葡萄园滴灌与嫁接笔记

- 体裁：帖文（`post`）
- 成品形态：社交单帖（`social_post`）
- 路由识别：`post`
- 工具调用：load_story_knowledge

## 一、输入

### 1. 提示词（原文）

按 china_storytelling，format=social_post，platform=instagram，country=America，语气 optimistic，英文。必须使用下方用户上传素材，不要补充素材没有的产量、人名和融资额。

### 2. 提示词（中文说明）

按中国故事成稿 skill，体裁走「帖文」，成品形态为「社交单帖」。主题：宁夏葡萄园滴灌与嫁接笔记。必须使用用户上传素材；不要补充素材没有的数字、人名等可核验细节；先调用一次加载故事知识库，再成稿；输出标明已读库，并提醒人工审核。

### 3. 用户上传素材（原文）

宁夏某葡萄产区曾是砾石荒地；合作社使用滴灌；一位种植户保留了失败嫁接记录本；参观者可摸到滴灌管外壁的冷凝水。

### 4. 用户上传素材（中文）

素材原文即为中文，内容同上。

## 二、输出

### 1. Agent 成稿（原文）

```text
**knowledge_loaded: true**
**format:** social_post (Tier-1)
**platform:** instagram
**country:** America
**tone:** optimistic
**结构适配判断:** 高度适配 A+B+C + D(蜕变) + E(个体)
**一句话核心句（内部）:** 砾石荒地上，滴灌管线的冷凝水和一本写满失败的本子，记录着葡萄园如何从无到有。

---

**post:**

> Touch the outside of a drip-irrigation pipe in this Ningxia vineyard — your fingers come away wet. Condensation. That small detail tells a bigger story.
>
> This land was once gravel wasteland. Nothing grew. Today, a local cooperative runs drip lines through the rows, and one grower keeps a notebook full of failed grafts — every attempt, every lesson, written down.
>
> No one started with answers. They started with soil, water, and willingness to fail on paper.
>
> Swipe to see what patience looks like in a vineyard. 🍇

**hashtags:** ["ChinaStories", "Ningxia", "VineyardLife", "DryLandFarming", "GrowFromFailure"]

---

**evidence_used:**
| 来源 | 内容 |
|------|------|
| 用户素材 | 宁夏某葡萄产区曾是砾石荒地 |
| 用户素材 | 合作社使用滴灌 |
| 用户素材 | 一位种植户保留了失败嫁接记录本 |
| 用户素材 | 参观者可摸到滴灌管外壁的冷凝水 |

**knowledge_loaded:** true
**modules_used:** A(起点：砾石荒地) + B(行动：滴灌/记录本) + C(延伸：耐心与试错) + D(蜕变：荒地→葡萄园) + E(个体：种植户的本子)

⚠️ **仅供人工审核草稿，不自动发布。** 未编造产量、人名、融资额；所有可核验细节均来自用户素材。
```

### 2. Agent 成稿（中文翻译）

【第 1/1 段】
**knowledge_loaded:** true
**format:** social_post (Tier-1)
**platform:** instagram
**country:** America
**tone:** optimistic
**结构适配判断:** 高度适配 A+B+C + D(蜕变) + E(个体)
**一句话核心句（内部）:** 砾石荒地上，滴灌管线的冷凝水和一本写满失败的本子，记录着葡萄园如何从无到有。

---

**post (帖子):**

> 触摸宁夏这片葡萄园里滴灌管的外壁——你的手指会沾上水迹。那是冷凝水。这个微小的细节诉说着一个更宏大的故事。
>
> 这片土地曾是砾石荒地，寸草不生。如今，当地合作社在葡萄藤行间铺设了滴灌管线，而一位种植户则保留着一本写满嫁接失败记录的本子——每一次尝试、每一堂教训，都记录在案。
>
> 一开始，没有人知道答案。他们从土壤、水源，以及愿意将失败记录在纸上的决心起步。
>
> 滑动查看葡萄园里耐心的模样。🍇

**hashtags (标签):** ["中国故事", "宁夏", "葡萄园生活", "旱地农业", "从失败中成长"]

---

**evidence_used (使用素材):**
| 来源 | 内容 |
|------|------|
| 用户素材 | 宁夏某葡萄产区曾是砾石荒地 |
| 用户素材 | 合作社使用滴灌 |
| 用户素材 | 一位种植户保留了失败嫁接记录本 |
| 用户素材 | 参观者可摸到滴灌管外壁的冷凝水 |

**knowledge_loaded:** true
**modules_used:** A(起点：砾石荒地) + B(行动：滴灌/记录本) + C(延伸：耐心与试错) + D(蜕变：荒地→葡萄园) + E(个体：种植户的本子)

⚠️ **仅供人工审核草稿，不自动发布。** 未编造产量、人名、融资额；所有可核验细节均来自用户素材。

---

> 说明：本文件是测试样例，不属于 `eval/` 评价体系规范。
