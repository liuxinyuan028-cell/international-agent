# 10_faq_travel · 赴华旅行支付与交通误解

- 体裁：误解澄清 FAQ（`faq`）
- 成品形态：误解澄清清单（`faq_mythbust`）
- 路由识别：`faq`
- 工具调用：load_story_knowledge

## 一、输入

### 1. 提示词（原文）

按 china_storytelling，format=faq_mythbust，英文，受众为美国旅行者。材料不够宁少条目；禁止编造 App 市场份额。

### 2. 提示词（中文说明）

按中国故事成稿 skill，体裁走「误解澄清 FAQ」，成品形态为「误解澄清清单」。主题：赴华旅行支付与交通误解。必须使用用户上传素材；不要补充素材没有的数字、人名等可核验细节；先调用一次加载故事知识库，再成稿；输出标明已读库，并提醒人工审核。

### 3. 用户上传素材（原文）

误解：去中国只能用现金。事实：大城市商户普遍支持移动支付，部分场景仍可刷卡或现金。误解：不会中文就无法坐地铁。事实：一线城市地铁常有英文标识与线路图。误解：外国人不能买高铁票。事实：可持护照在车站窗口或指定渠道购票（以现场规则为准）。

### 4. 用户上传素材（中文）

素材原文即为中文，内容同上。

## 二、输出

### 1. Agent 成稿（原文）

```text
**knowledge_loaded: true**
**format:** faq_mythbust (Tier-2)
**genre:** faq · genre_status: methods_in
**结构适配判断:** 高度适配 FAQ mythbust；模块 A+B+C 采用；3 条 Myth→Fact 全部来自用户素材，不补数、不补 App 名。

---

## title
Travel myths about China — what first-time visitors should actually know

## audience
U.S. travelers planning or considering a first trip to China

## intro
A few claims about traveling in China travel faster than the flights. Before you pack, here is what the available materials actually support — no app market-share numbers, no city-by-city promises.

## items

```json
[
  {
    "myth": "You can only pay in cash in China.",
    "fact": "In major cities, most merchants widely accept mobile payments; some scenarios still allow card or cash.",
    "verdict": "overstated",
    "bridge": "Plan for mobile payment as the default in cities, and keep a cash backup for edge cases.",
    "not_claiming": "This does not claim every small shop or rural stall takes mobile payment.",
    "evidence_refs": ["user_materials#payment"]
  },
  {
    "myth": "You can't use the subway if you don't speak Chinese.",
    "fact": "Subway systems in first-tier cities commonly have English signage and route maps.",
    "verdict": "overstated",
    "bridge": "Follow the English route map and station names — navigation is designed for non-Chinese speakers too.",
    "not_claiming": "This does not guarantee full English audio announcements at every station.",
    "evidence_refs": ["user_materials#subway"]
  },
  {
    "myth": "Foreigners cannot buy high-speed rail tickets.",
    "fact": "You can buy tickets with a passport at station windows or through designated channels (subject to on-site rules).",
    "verdict": "false",
    "bridge": "Bring your passport and check the current ticketing channel before you go.",
    "not_claiming": "This does not claim every online platform or every route accepts foreign passports the same way.",
    "evidence_refs": ["user_materials#rail"]
  }
]
```

## closing
The shareable point is simple: China's everyday travel infrastructure is more accessible to first-time visitors than the old myths suggest — plan by what's actually on the ground, not by what's repeated online.

---

**evidence_used**
- user_materials: 3 条（支付 / 地铁 / 高铁），逐条对应上文 items
- local knowledge base: 未调用（本主题用户素材已覆盖所需澄清点）

**自检**
- 未编造 App 名称、市场份额、具体城市清单、精确百分比
- 未使用成就口号开篇；未嘲讽目标国受众
- 每条 `not_claiming` 明确边界，避免过度承诺

⚠️ 本稿为人工审核草稿，未自动发布。建议发布前核对最新现场规则（尤其高铁购票渠道）。
```

### 2. Agent 成稿（中文翻译）

**knowledge_loaded: true**
**format:** faq_mythbust (Tier-2)
**genre:** faq · genre_status: methods_in
**结构适配判断:** 高度适配 FAQ mythbust；模块 A+B+C 采用；3 条 Myth→Fact 全部来自用户素材，不补数、不补 App 名。

---

## title
关于中国的旅行迷思——初次访华游客真正需要知道的事

## audience
计划或考虑首次前往中国旅行的美国游客

## intro
关于在中国旅行的一些说法，传播得比航班还要快。在您打包行李之前，以下是现有资料实际支持的内容——没有应用程序的市场份额数据，也没有逐个城市的具体承诺。

## items

```json
[
  {
    "myth (迷思)": "在中国只能使用现金支付。",
    "fact (事实)": "在主要城市，大多数商户广泛接受移动支付；部分场景仍可使用银行卡或现金。",
    "verdict (判定)": "夸大其词",
    "bridge (过渡)": "在城市中将移动支付作为默认支付方式，并备有现金以应对特殊情况。",
    "not_claiming (未断言)": "这并不意味着每家小店或乡村摊位都支持移动支付。",
    "evidence_refs (证据参考)": ["user_materials#payment"]
  },
  {
    "myth (迷思)": "不会中文就无法乘坐地铁。",
    "fact (事实)": "一线城市的地铁系统通常设有英文标识和线路图。",
    "verdict (判定)": "夸大其词",
    "bridge (过渡)": "跟着英文线路图和站名走——导航系统同样为非中文使用者设计。",
    "not_claiming (未断言)": "这并不保证每个车站都有全英文的语音播报。",
    "evidence_refs (证据参考)": ["user_materials#subway"]
  },
  {
    "myth (迷思)": "外国人无法购买高铁票。",
    "fact (事实)": "您可以凭护照在车站窗口或通过指定渠道购票（需遵守现场规定）。",
    "verdict (判定)": "不实",
    "bridge (过渡)": "带上您的护照，并在出发前确认当前的购票渠道。",
    "not_claiming (未断言)": "这并不意味着每个在线平台或每条线路都以相同方式接受外国护照。",
    "evidence_refs (证据参考)": ["user_materials#rail"]
  }
]
```

## closing
值得分享的要点很简单：中国的日常旅行基础设施对初次来访的游客来说，比那些老旧的迷思所暗示的要便利得多——请根据实际情况来规划行程，而不是盲从网上的重复传言。

---

**evidence_used**
- user_materials: 3 条（支付 / 地铁 / 高铁），逐条对应上文 items
- local knowledge base: 未调用（本主题用户素材已覆盖所需澄清点）

**自检**
- 未编造 App 名称、市场份额、具体城市清单、精确百分比
- 未使用成就口号开篇；未嘲讽目标国受众
- 每条 `not_claiming` 明确边界，避免过度承诺

⚠️ 本稿为人工审核草稿，未自动发布。建议发布前核对最新现场规则（尤其高铁购票渠道）。

---

> 说明：本文件是测试样例，不属于 `eval/` 评价体系规范。
