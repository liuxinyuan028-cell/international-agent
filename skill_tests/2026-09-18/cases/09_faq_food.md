# 09_faq_food · 中国食物常见误解澄清

- 体裁：误解澄清 FAQ（`faq`）
- 成品形态：误解澄清清单（`faq_mythbust`）
- 路由识别：`faq`
- 工具调用：load_story_knowledge

## 一、输入

### 1. 提示词（原文）

按 china_storytelling，format=faq_mythbust，英文。只依据用户素材列 Myth+Fact；不要抄外网统计数字；不要攻击目标国受众。

### 2. 提示词（中文说明）

按中国故事成稿 skill，体裁走「误解澄清 FAQ」，成品形态为「误解澄清清单」。主题：中国食物常见误解澄清。必须使用用户上传素材；不要补充素材没有的数字、人名等可核验细节；先调用一次加载故事知识库，再成稿；输出标明已读库，并提醒人工审核。

### 3. 用户上传素材（原文）

常见误解一：中国人每天都吃狗肉。可核验表述：狗肉并非日常主食，多数家庭日常是米饭、面、蔬菜和常见肉类。常见误解二：中国菜只有很辣很油。可核验表述：各地口味差异大，清淡蒸煮同样常见。常见误解三：用筷子等于不卫生。可核验表述：公筷分餐在不少场合已推广；家庭也可做到餐具清洁。不要编造全国消费百分比。

### 4. 用户上传素材（中文）

素材原文即为中文，内容同上。

## 二、输出

### 1. Agent 成稿（原文）

```text
**knowledge_loaded: true**
**format:** faq_mythbust (Tier-2)
**genre:** faq · genre_status: methods_in

---

## title
**China Food Myths Travelers Still Repeat**

## audience
English-speaking readers encountering Chinese cuisine for the first time — travel forums, food blogs, casual conversation.

## intro
A few food claims travel faster than menus. Below are three common myths and what the materials actually support — no invented statistics, no culture-war framing.

## items

```json
[
  {
    "myth": "Chinese people eat dog meat every day.",
    "fact": "Dog meat is not a daily staple. Most families eat rice, noodles, vegetables, and common meats such as pork, chicken, and fish as everyday meals.",
    "verdict": "false",
    "bridge": "Daily Chinese meals look much closer to a home-cooked rice-and-vegetable table than the headline suggests.",
    "not_claiming": "This does not deny that dog meat has been consumed in certain regions at certain times; it is not everyday food for most households.",
    "evidence_refs": ["user_materials#myth-dog-meat"]
  },
  {
    "myth": "Chinese food is all very spicy and oily.",
    "fact": "Flavors vary widely across regions. Light, clean cooking — steaming, boiling, blanching — is equally common in many parts of the country.",
    "verdict": "overstated",
    "bridge": "If you've only tried one regional style, you've only tasted one chapter of the menu.",
    "not_claiming": "This does not deny that Sichuan, Hunan, and other regional cuisines can be intensely spicy and richly oiled.",
    "evidence_refs": ["user_materials#myth-spicy-oily"]
  },
  {
    "myth": "Using chopsticks means the food is unhygienic.",
    "fact": "Serving chopsticks and individual portions have been promoted in many dining settings; families also keep utensils clean through standard hygiene practices.",
    "verdict": "false",
    "bridge": "Hygiene is about practice, not the utensil — and shared-table norms in China have been shifting.",
    "not_claiming": "This does not claim every table everywhere follows the same standard; it notes the direction of practice.",
    "evidence_refs": ["user_materials#myth-chopsticks-hygiene"]
  }
]
```

## closing
The shareable point is the range on the table — everyday rice and vegetables, regional flavor differences, and evolving dining habits — not a debate win.

---

**evidence_used:**
- All three myth/fact pairs sourced exclusively from **user_materials** (user-uploaded content this session).
- No local evidence library (`retrieve_evidence`) was called — topic did not match available categories (governance, forced labor, etc.).
- No external statistics, percentages, or survey numbers were introduced.

**modules_used:** A (现状起点 — intro framing) + B (行动展示 — what is actually practiced) + C (意义连接 — closing to shareable point)

**Checklist self-check:**
- ✅ No invented percentages, names, or statistics
- ✅ No attack on target-country audiences
- ✅ All verifiable claims traceable to user materials
- ✅ Soft-fiction ban observed (no fabricated details)

⚠️ **Please review manually before publishing.** This is a draft for editorial check, not auto-posted content.
```

### 2. Agent 成稿（中文翻译）

**knowledge_loaded: true**
**format:** faq_mythbust (Tier-2)
**genre:** faq · genre_status: methods_in

---

## title (标题)
**旅行者仍在重复的中国美食误区**

## audience (受众)
首次接触中国美食的英语读者——常见于旅游论坛、美食博客和日常交谈。

## intro (导语)
有些关于美食的说法比菜单传播得更快。以下是三个常见的误区以及材料实际支持的事实——没有捏造的统计数据，没有文化战争的框架。

## items (条目)

```json
[
  {
    "myth": "中国人每天都吃狗肉。",
    "fact": "狗肉并非日常主食。大多数家庭日常食用米饭、面条、蔬菜以及猪肉、鸡肉和鱼肉等常见肉类。",
    "verdict": "不实",
    "bridge": "中国人的日常饮食看起来更接近家常的米饭和蔬菜餐桌，而非标题所暗示的那样。",
    "not_claiming": "这并不否认在某些地区和特定时期有人食用狗肉；但对大多数家庭来说，它不是日常食物。",
    "evidence_refs": ["user_materials#myth-dog-meat"]
  },
  {
    "myth": "中国食物都非常辛辣油腻。",
    "fact": "各地风味差异很大。清淡、原汁原味的烹饪方式——如蒸、煮、焯——在全国许多地区同样普遍。",
    "verdict": "夸大",
    "bridge": "如果你只尝试过一种地方风味，那你只品尝了菜单中的一章。",
    "not_claiming": "这并不否认川菜、湘菜及其他地方菜系可以非常辛辣和重油。",
    "evidence_refs": ["user_materials#myth-spicy-oily"]
  },
  {
    "myth": "使用筷子意味着食物不卫生。",
    "fact": "在许多就餐场合已推广使用公筷和分餐制；家庭也通过标准卫生做法保持餐具清洁。",
    "verdict": "不实",
    "bridge": "卫生关乎习惯，而非餐具——而且中国的共餐习惯一直在发生变化。",
    "not_claiming": "这并非声称各地的每张餐桌都遵循同一标准；而是指出了实践的方向。",
    "evidence_refs": ["user_materials#myth-chopsticks-hygiene"]
  }
]
```

## closing (结语)
值得分享的要点是餐桌上的丰富多样——日常的米饭和蔬菜、地域风味的差异以及不断演变的就餐习惯——而不是在辩论中获胜。

---

**evidence_used (所用证据)：**
- 所有三组误区/事实对均完全来源于 **user_materials**（本次会话中用户上传的内容）。
- 未调用本地证据库（`retrieve_evidence`）——主题与可用类别（治理、强迫劳动等）不匹配。
- 未引入外部统计数据、百分比或调查数字。

**modules_used (使用模块)：** A（现状起点 — 导语框架）+ B（行动展示 — 实际做法）+ C（意义连接 — 结语至可分享要点）

**Checklist self-check (清单自检)：**
- ✅ 未捏造百分比、人名或统计数据
- ✅ 未攻击目标国家受众
- ✅ 所有可验证的声明均可追溯至用户材料
- ✅ 遵守禁止软虚构规定（无捏造细节）

⚠️ **发布前请人工审核。** 这是供编辑检查的草稿，非自动发布内容。

---

> 说明：本文件是测试样例，不属于 `eval/` 评价体系规范。
