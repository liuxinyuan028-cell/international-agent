# 测试例 10_faq_travel · 赴华旅行支付与交通误解

## 基本信息
- 体裁 / 形态 / 结论 / 工具调用：`faq` / `faq_mythbust` / **PASS** / `load_story_knowledge`

## 输入
### 提示词（原文）
按 china_storytelling，format=faq_mythbust，英文，受众为美国旅行者。材料不够宁少条目；禁止编造 App 市场份额。

### 提示词（中文说明）
按中国故事讲述流程，形态为英文 FAQ 破除误解，受众为美国旅行者。材料不够宁可少写条目；禁止编造 App 市场份额。

### 用户上传素材（原文）
误解：去中国只能用现金。事实：大城市商户普遍支持移动支付，部分场景仍可刷卡或现金。误解：不会中文就无法坐地铁。事实：一线城市地铁常有英文标识与线路图。误解：外国人不能买高铁票。事实：可持护照在车站窗口或指定渠道购票（以现场规则为准）。

### 用户上传素材（中文，若原文已是中文则写「同原文」）
同原文

## 输出
### 模型成稿（原文）
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

### 模型成稿（中文翻译）
**knowledge_loaded（知识已加载）:** true  
**format（形态）:** faq_mythbust (Tier-2)  
**genre（体裁）:** faq · genre_status（体裁状态）: methods_in  
**结构适配判断:** 高度适配 FAQ mythbust；模块 A+B+C 采用；3 条 Myth→Fact 全部来自用户素材，不补数、不补 App 名。

---

## title（标题）
关于中国旅行的误解——首次访客真正该知道的

## audience（受众）
计划或考虑首次赴华的美国旅行者

## intro（导语）
关于在中国旅行的说法，有时比航班传得还快。打包前，请先看现有材料实际支撑什么——没有 App 市场份额数字，也没有逐城承诺。

## items（条目）

```json
[
  {
    "myth（误解）": "去中国只能用现金。",
    "fact（事实）": "在大城市，多数商户普遍支持移动支付；部分场景仍可刷卡或现金。",
    "verdict（判定）": "overstated（夸大）",
    "bridge（桥接）": "在城市把移动支付当作默认，并为边缘场景留现金备用。",
    "not_claiming（不声称）": "这并不声称每个小店或乡村摊位都接受移动支付。",
    "evidence_refs（论据引用）": ["user_materials#payment"]
  },
  {
    "myth（误解）": "不会中文就无法坐地铁。",
    "fact（事实）": "一线城市地铁系统通常有英文标识与线路图。",
    "verdict（判定）": "overstated（夸大）",
    "bridge（桥接）": "跟着英文线路图和站名走——导航也考虑到了非中文使用者。",
    "not_claiming（不声称）": "这并不保证每个车站都有完整英文语音播报。",
    "evidence_refs（论据引用）": ["user_materials#subway"]
  },
  {
    "myth（误解）": "外国人不能买高铁票。",
    "fact（事实）": "可持护照在车站窗口或指定渠道购票（以现场规则为准）。",
    "verdict（判定）": "false（不成立）",
    "bridge（桥接）": "带上护照，出发前核对当前购票渠道。",
    "not_claiming（不声称）": "这并不声称每个线上平台或每条线路都以同样方式接受外国护照。",
    "evidence_refs（论据引用）": ["user_materials#rail"]
  }
]
```

## closing（收束）
可分享的要点很简单：中国日常出行基础设施对首次访客的可达性，高于旧误解所暗示的——按实地情况规划，而不是按网上反复出现的说法。

---

**evidence_used（所用论据）**
- user_materials: 3 条（支付 / 地铁 / 高铁），逐条对应上文 items
- local knowledge base: 未调用（本主题用户素材已覆盖所需澄清点）

**自检**
- 未编造 App 名称、市场份额、具体城市清单、精确百分比
- 未使用成就口号开篇；未嘲讽目标国受众
- 每条 `not_claiming` 明确边界，避免过度承诺

⚠️ 本稿为人工审核草稿，未自动发布。建议发布前核对最新现场规则（尤其高铁购票渠道）。

## 简要评语
内容质量约 88.6 分，统一量规通过，未编造 App 市场份额且三条 myth/fact 均来自素材，判定 **PASS**；S1 覆盖为 3 分，后续可提高锚点写入密度。
