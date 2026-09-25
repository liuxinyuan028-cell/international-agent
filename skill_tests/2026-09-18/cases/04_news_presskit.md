# 04_news_presskit · 中非滴灌示范园出苗

- 体裁：通稿（`news`）
- 成品形态：对外素材包（`press_kit`）
- 路由识别：`news`
- 工具调用：load_story_knowledge

## 一、输入

### 1. 提示词（原文）

按 china_storytelling，format=press_kit。输出短消息、标题组、要点；材料不够的块写 omitted_reason。不要编造增产百分比和吨数。英文。

### 2. 提示词（中文说明）

按中国故事成稿 skill，体裁走「通稿」，成品形态为「对外素材包」。主题：中非滴灌示范园出苗。必须使用用户上传素材；不要补充素材没有的数字、人名等可核验细节；先调用一次加载故事知识库，再成稿；输出标明已读库，并提醒人工审核。

### 3. 用户上传素材（原文）

中非某农业合作示范园教当地农户使用滴灌；中方农技员与当地翻译一起下田；第一季作物出苗更整齐；示范田边竖着中非双语说明牌。

### 4. 用户上传素材（中文）

素材原文即为中文，内容同上。

## 二、输出

### 1. Agent 成稿（原文）

```text
**knowledge_loaded: true**
**format:** press_kit (Tier-1)
**结构适配判断:** 高度适配 A+B+C + E(个体)
**一句话核心句（内部）:** 中非示范园里，滴灌管线让第一季作物出苗更整齐，双语说明牌立在田边。

---

## press_kit · China-Africa Drip Irrigation Demo Plot

### headline_pack

**headline_main:**  
Seedlings Rise in Neater Rows: A China-Africa Demo Plot Tests Drip Irrigation

**headline_alt_1:**  
From Field to Fieldside Sign — Drip Irrigation Takes Root in a China-Africa Demo Plot

**headline_alt_2:**  
First Season, Neater Rows: Chinese Agronomists and Local Translators Work Side by Side

---

### news_blurb

At the edge of a demonstration field in a China-Africa agricultural cooperation park, a bilingual sign — in Chinese and a local African language — marks the plot where drip irrigation is being tried for the first time.

Chinese agronomists have been going into the field together with local translators, showing farmers how to lay drip lines and schedule watering. The setup is simple: pipes with small emitters run along the rows, delivering water directly to the roots.

Now, the first season's seedlings have come up. Compared with earlier planting methods, the rows look noticeably more even — a sign, the team says, that the water is reaching the plants more consistently.

The work is hands-on. Agronomists and translators walk the rows together, checking emitters, adjusting flow, answering questions from farmers who are learning the system. The bilingual sign at the field's edge lists basic instructions — a small but practical step toward making the technology accessible beyond the demo plot.

For the farmers involved, the visible difference in seedling uniformity is the first tangible result. What comes next — whether the method saves water, improves yields, or can be adapted to other crops — will depend on the rest of this season and the ones after.

---

### key_facts

- China-Africa agricultural cooperation demo park teaching local farmers drip irrigation
- Chinese agronomists working in the field together with local translators
- First season's seedlings emerged in neater, more uniform rows
- Bilingual (Chinese + local African language) instruction sign placed at the edge of the demo field

---

### visual_captions

1. Chinese agronomist and local translator walking through a drip-irrigated demo plot, checking emitters along the rows.
2. Close-up of seedlings emerging in even rows from drip lines.
3. Bilingual instruction sign (Chinese and local African language) standing at the edge of the demonstration field.

---

### social_post ×2

**variant_1 (scene hook):**  
Neater rows this season at a China-Africa demo plot — drip irrigation is being tried, with agronomists and local translators working side by side in the field. A bilingual sign marks the edge of the plot. 🌱 #ChinaAfrica #AgriCooperation

**variant_2 (result hook):**  
First seedlings are up at a China-Africa agricultural demo park — and the rows look more even than before. Drip lines, hands-on training, and a bilingual sign at the field's edge. Small steps, visible results. #DripIrrigation #SouthSouthCooperation

---

### faq

**q:** Is this just a showcase plot?  
**a:** The demo field has a bilingual instruction sign so farmers can reference the basics on their own — the aim is to make the method usable beyond the park.

**q:** What crop is being grown?  
**a:** The source materials do not specify the crop type — only that first-season seedlings emerged in neater rows under drip irrigation.

---

### omitted_reason

- **quote_card omitted** — no verbatim quote from agronomists, translators, or farmers in source materials.
- **yield/water-saving data omitted** — no percentage, volume, or tonnage provided in source materials; cannot fabricate.
- **specific country / crop name omitted** — not specified in source materials.

---

## evidence_used

**用户上传素材（4 条）：**
1. 中非某农业合作示范园教当地农户使用滴灌
2. 中方农技员与当地翻译一起下田
3. 第一季作物出苗更整齐
4. 示范田边竖着中非双语说明牌

**本地库：** 未调用（主题不在外交部论据库典型类别范围）

---

⚠️ **提醒：以上内容为人工审核草稿，不自动发布。**  
所有可核验事实均来自用户上传素材，未编造增产百分比、吨数、作物种类、具体国名或人物姓名。缺料块已标注 `omitted_reason`。
```

### 2. Agent 成稿（中文翻译）

**knowledge_loaded: true**
**format:** press_kit (Tier-1)
**结构适配判断:** 高度适配 A+B+C + E(个体)
**一句话核心句（内部）:** 中非示范园里，滴灌管线让第一季作物出苗更整齐，双语说明牌立在田边。

---

## press_kit · 中非滴灌示范田

### headline_pack

**headline_main:**  
幼苗破土，行列更齐：中非示范田试水滴灌技术

**headline_alt_1:**  
从田间到田边标牌——滴灌技术在中非示范田落地生根

**headline_alt_2:**  
首季播种，行列更齐：中国农艺师与当地翻译并肩劳作

---

### news_blurb

在中非农业合作示范园的一块试验田边，立着一块中文和当地非洲语言的双语说明牌，标记着这里正是首次试水滴灌技术的地块。

中国农艺师与当地翻译一同深入田间，向农户演示如何铺设滴灌带和安排灌溉。这套系统很简单：带有小型滴头的管道沿作物行列铺设，将水直接输送到作物根部。

如今，第一季的幼苗已经破土而出。与以往的种植方式相比，现在的苗垄看起来明显更加整齐——团队表示，这说明水分供应更加均匀稳定。

这项工作注重实操。农艺师和翻译并肩走在田垄间，检查滴头、调节流量，并解答正在学习该系统的农户提出的问题。田边的双语说明牌上列出了基本操作指南——这是让这项技术走出示范田、惠及更多农户的一小步，却十分务实。

对于参与的农户而言，幼苗整齐度肉眼可见的变化是第一个切实可见的成果。接下来的成效——这种方法能否节水、增产，或能否推广到其他作物——将取决于本季余下时间以及未来几个种植季的表现。

---

### key_facts

- 中非农业合作示范园向当地农户传授滴灌技术
- 中国农艺师与当地翻译共同在田间作业
- 第一季幼苗出苗更齐，苗垄更加均匀
- 示范田边竖立双语（中文+当地非洲语言）操作说明牌

---

### visual_captions

1. 中国农艺师与当地翻译穿行于滴灌示范田中，沿田垄检查滴头。
2. 特写：幼苗从滴灌带旁破土而出，行列整齐。
3. 示范田边竖立着双语（中文和当地非洲语言）操作说明牌。

---

### social_post ×2

**variant_1 (scene hook):**  
中非示范田本季苗垄更齐——滴灌技术正在试水，农艺师与当地翻译并肩在田间劳作。田边立着一块双语说明牌。🌱 #中非合作 #农业合作

**variant_2 (result hook):**  
中非农业示范园首批幼苗破土而出——苗垄比以往更加整齐。滴灌带、实操培训，还有田边的双语说明牌。小步迈进，成效可见。#滴灌技术 #南南合作

---

### faq

**q:** 这仅仅是一块展示田吗？  
**a:** 示范田边设有双语操作说明牌，以便农户……

可自行查阅基础知识——目的是让该方法在园区之外也能推广应用。

**q:** 种植的是什么作物？  
**a:** 素材未指明作物种类——仅说明在滴灌条件下，首季作物出苗更为整齐。

---

### omitted_reason（省略原因）

- **quote_card（引语卡片）省略**——素材中无农艺师、译员或农户的原话引用。
- **yield/water-saving data（增产/节水数据）省略**——素材未提供百分比、水量或吨数，不得编造。
- **specific country / crop name（具体国家/作物名称）省略**——素材未作具体说明。

---

## evidence_used（所用证据）

**用户上传素材（4 条）：**
1. 中非某农业合作示范园教当地农户使用滴灌
2. 中方农技员与当地翻译一起下田
3. 第一季作物出苗更整齐
4. 示范田边竖着中非双语说明牌

**本地库：** 未调用（主题不在外交部论据库典型类别范围）

---

⚠️ **提醒：以上内容为人工审核草稿，不自动发布。**  
所有可核验事实均来自用户上传素材，未编造增产百分比、吨数、作物种类、具体国名或人物姓名。缺料块已标注 `omitted_reason`。

---

> 说明：本文件是测试样例，不属于 `eval/` 评价体系规范。
