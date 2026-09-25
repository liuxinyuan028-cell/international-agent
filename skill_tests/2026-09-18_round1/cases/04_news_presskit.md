# 测试例 04_news_presskit · 中非滴灌示范园出苗

## 基本信息
- 体裁 / 形态 / 结论 / 工具调用：`news` / `press_kit` / **PASS** / `load_story_knowledge`

## 输入
### 提示词（原文）
按 china_storytelling，format=press_kit。输出短消息、标题组、要点；材料不够的块写 omitted_reason。不要编造增产百分比和吨数。英文。

### 提示词（中文说明）
按中国故事讲述流程，形态为新闻资料包。输出短消息、标题组、要点；材料不够的块写 omitted_reason。不得编造增产百分比与吨数。英文成稿。

### 用户上传素材（原文）
中非某农业合作示范园教当地农户使用滴灌；中方农技员与当地翻译一起下田；第一季作物出苗更整齐；示范田边竖着中非双语说明牌。

### 用户上传素材（中文，若原文已是中文则写「同原文」）
同原文

## 输出
### 模型成稿（原文）
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

### 模型成稿（中文翻译）
**knowledge_loaded（知识已加载）:** true  
**format（形态）:** press_kit (Tier-1)  
**结构适配判断:** 高度适配 A+B+C + E(个体)  
**一句话核心句（内部）:** 中非示范园里，滴灌管线让第一季作物出苗更整齐，双语说明牌立在田边。

---

## press_kit（新闻资料包）· 中非滴灌示范田

### headline_pack（标题组）

**headline_main（主标题）:**  
出苗更整齐：中非示范田试种滴灌

**headline_alt_1（备选标题 1）:**  
从田间到田边说明牌——滴灌在中非示范田扎下根

**headline_alt_2（备选标题 2）:**  
第一季，行距更齐：中方农技员与当地翻译并肩下田

---

### news_blurb（短消息）

在中非农业合作示范园一块示范田的边缘，一块中非双语说明牌——中文与当地非洲语言——标示出这片首次试用滴灌的田块。

中方农技员一直与当地翻译一起下田，向农户演示如何铺设滴灌管线、安排浇水。装置很简单：带小出水口的管子沿行铺开，把水直接送到根部。

如今，第一季幼苗已出。与以往种植方式相比，行间看起来明显更整齐——团队认为，这是水更稳定送达植株的迹象。

工作很落地。农技员与翻译并肩走在行间，检查出水口、调节流量，回答正在学习这套系统的农户的问题。田边双语说明牌列出基本操作——虽小，却是让技术走出示范田的务实一步。

对参与农户而言，出苗整齐度的可见变化是第一份可触摸的结果。接下来——能否节水、增产，或能否适配其他作物——要看本季余下时间与之后季节。

---

### key_facts（要点）

- 中非农业合作示范园教当地农户使用滴灌
- 中方农技员与当地翻译一起下田
- 第一季作物出苗更整齐、更均匀
- 示范田边竖着中非双语（中文 + 当地非洲语言）说明牌

---

### visual_captions（配图说明）

1. 中方农技员与当地翻译走在滴灌示范田行间，检查出水口。
2. 滴灌管线下，幼苗整齐出苗的特写。
3. 示范田边竖立的双语说明牌（中文与当地非洲语言）。

---

### social_post ×2（社交帖两则）

**variant_1（场景钩子）:**  
这一季，中非示范田出苗更整齐——正在试用滴灌，农技员与当地翻译并肩下田。田边立着双语说明牌。🌱 #ChinaAfrica #AgriCooperation

**variant_2（结果钩子）:**  
中非农业示范园第一季幼苗已出——行间比以往更齐。滴灌管线、手把手培训，还有田边的双语说明牌。小步，可见结果。#DripIrrigation #SouthSouthCooperation

---

### faq（问答）

**q（问）:** 这只是展示田吗？  
**a（答）:** 示范田有双语说明牌，方便农户自行查阅基本操作——目标是让方法走出园区也能用。

**q（问）:** 种的是什么作物？  
**a（答）:** 源材料未写明作物种类——只写第一季在滴灌下出苗更整齐。

---

### omitted_reason（省略原因）

- **quote_card（引语卡）省略** — 源材料中无农技员、翻译或农户的原话。
- **增产/节水数据省略** — 源材料未提供百分比、体积或吨数；不可编造。
- **具体国名/作物名省略** — 源材料未写明。

---

## evidence_used（所用论据）

**用户上传素材（4 条）：**
1. 中非某农业合作示范园教当地农户使用滴灌
2. 中方农技员与当地翻译一起下田
3. 第一季作物出苗更整齐
4. 示范田边竖着中非双语说明牌

**本地库：** 未调用（主题不在外交部论据库典型类别范围）

---

⚠️ **提醒：以上内容为人工审核草稿，不自动发布。**  
所有可核验事实均来自用户上传素材，未编造增产百分比、吨数、作物种类、具体国名或人物姓名。缺料块已标注 `omitted_reason`。

## 简要评语
内容质量约 89.6 分，统一量规通过，缺料块正确标注 omitted_reason 且未编造增产百分比/吨数，判定 **PASS**。
