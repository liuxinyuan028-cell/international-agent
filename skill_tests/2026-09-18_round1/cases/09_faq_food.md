# 测试例 09_faq_food · 中国食物常见误解澄清

## 基本信息
- 体裁 / 形态 / 结论 / 工具调用：`faq` / `faq_mythbust` / **FAIL** / `load_story_knowledge`

## 输入
### 提示词（原文）
按 china_storytelling，format=faq_mythbust，英文。只依据用户素材列 Myth+Fact；不要抄外网统计数字；不要攻击目标国受众。

### 提示词（中文说明）
按中国故事讲述流程，形态为英文 FAQ 破除误解。只依据用户素材列 Myth+Fact；不得抄外网统计数字；不得攻击目标国受众。

### 用户上传素材（原文）
常见误解一：中国人每天都吃狗肉。可核验表述：狗肉并非日常主食，多数家庭日常是米饭、面、蔬菜和常见肉类。常见误解二：中国菜只有很辣很油。可核验表述：各地口味差异大，清淡蒸煮同样常见。常见误解三：用筷子等于不卫生。可核验表述：公筷分餐在不少场合已推广；家庭也可做到餐具清洁。不要编造全国消费百分比。

### 用户上传素材（中文，若原文已是中文则写「同原文」）
同原文

## 输出
### 模型成稿（原文）
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

### 模型成稿（中文翻译）
**knowledge_loaded（知识已加载）:** true  
**format（形态）:** faq_mythbust (Tier-2)  
**genre（体裁）:** faq · genre_status（体裁状态）: methods_in

---

## title（标题）
**旅行者仍在重复的中国食物误解**

## audience（受众）
初次接触中国饮食的英语读者——旅行论坛、美食博客、日常闲聊。

## intro（导语）
有些食物说法比菜单传播得更快。下面是三条常见误解，以及素材实际支撑的内容——不编造统计，也不做文化对立框架。

## items（条目）

```json
[
  {
    "myth（误解）": "中国人每天都吃狗肉。",
    "fact（事实）": "狗肉并非日常主食。多数家庭日常吃米饭、面、蔬菜，以及猪肉、鸡肉、鱼等常见肉类。",
    "verdict（判定）": "false（不成立）",
    "bridge（桥接）": "中国人的日常餐食，更接近家常的米饭蔬菜桌，而不是标题暗示的那样。",
    "not_claiming（不声称）": "这并不否认某些地区在某些时期存在狗肉消费；对多数家庭而言，它不是日常食物。",
    "evidence_refs（论据引用）": ["user_materials#myth-dog-meat"]
  },
  {
    "myth（误解）": "中国菜只有很辣很油。",
    "fact（事实）": "各地口味差异很大。清淡烹调——蒸、煮、焯——在许多地方同样常见。",
    "verdict（判定）": "overstated（夸大）",
    "bridge（桥接）": "如果你只尝过一种地方风味，你只读了菜单的一章。",
    "not_claiming（不声称）": "这并不否认川菜、湘菜等地方菜可以很辣、很油重。",
    "evidence_refs（论据引用）": ["user_materials#myth-spicy-oily"]
  },
  {
    "myth（误解）": "用筷子等于不卫生。",
    "fact（事实）": "公筷与分餐在不少用餐场合已推广；家庭也可通过常规卫生习惯保持餐具清洁。",
    "verdict（判定）": "false（不成立）",
    "bridge（桥接）": "卫生关乎做法，不关乎餐具本身——中国共桌习惯也在变化。",
    "not_claiming（不声称）": "这并不声称每一张桌子都遵循同一标准；它指出的是实践方向。",
    "evidence_refs（论据引用）": ["user_materials#myth-chopsticks-hygiene"]
  }
]
```

## closing（收束）
可分享的要点是桌上的多样性——日常米饭与蔬菜、地方口味差异、以及演变中的用餐习惯——而不是辩论胜利。

---

**evidence_used（所用论据）:**
- 全部三组 myth/fact 仅来自 **user_materials**（本会话用户上传内容）。
- 未调用本地论据库（`retrieve_evidence`）——主题与可用类别（治理、强迫劳动等）不匹配。
- 未引入外部统计、百分比或调查数字。

**modules_used（所用模块）:** A（现状起点 — intro 框定）+ B（行动展示 — 实际做法）+ C（意义连接 — 收束到可分享点）

**Checklist self-check（自检）:**
- ✅ 未编造百分比、人名或统计
- ✅ 未攻击目标国受众
- ✅ 所有可核验主张可回溯至用户素材
- ✅ 遵守 soft-fiction ban（无虚构细节）

⚠️ **发布前请人工审核。** 本稿为编辑审核草稿，非自动发布内容。

## 简要评语
内容质量虽约 81.4 分且内容门未失败，但统一量规 S1 覆盖仅 1 分、`anchor_hits` 为空，专有锚点写入不足，统一量规未通过，判定 **FAIL**。
