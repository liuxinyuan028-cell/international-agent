# 测试例 07_script_tea · 茶席分享与热水声

## 基本信息
- 体裁 / 形态 / 结论 / 工具调用：`script` / `short_video` / **PASS** / `load_story_knowledge`

## 输入
### 提示词（原文）
按 china_storytelling，format=short_video，约 35 秒英文口播分镜。须有 Hook 0-3 秒；不要编假精确钟点和销售额。

### 提示词（中文说明）
按中国故事讲述流程，形态为约 35 秒英文口播分镜短视频。须有 0–3 秒 Hook；不得编造假精确钟点与销售额。

### 用户上传素材（原文）
朋友来访时主人温杯、注水、分茶；热水注入盖碗时有一声轻响；桌上只有一把壶和两只杯；客人说这茶比想象中更淡、更干净。

### 用户上传素材（中文，若原文已是中文则写「同原文」）
同原文

## 输出
### 模型成稿（原文）
---

## 短视频脚本 · short_video（Tier-1）

**knowledge_loaded:** true  
**format:** short_video  
**genre:** script（体裁完善度：methods_in）  
**结构适配判断:** 高度适配 A+B+C + E（个体）+ H（隐喻）  
**一句话核心句（内部）:** 一壶两杯，热水入碗那一声轻响，和一杯比想象中更淡更干净的茶——分享不需要更多。

---

**title:** The sound between two cups  
（标题：两杯之间的声音）

**duration_sec:** 35

**shots:**

| t | shot | vo | on_screen | broll / sfx |
|---|------|----|-----------|-------------|
| 0-3 | CU: hot water hitting gaiwan | *(no VO — only the sound)* | LISTEN | **sfx:** light pour, ceramic resonance |
| 3-10 | Wide: table with one pot, two cups | "A friend dropped by. No ceremony, just one pot, two cups." | ONE POT. TWO CUPS. | **broll:** steam rising, quiet room |
| 10-18 | Hands: warming cup → pouring → dividing tea | "Warm the cup first. Then the water goes in. Then we share." | WARM · POUR · SHARE | **sfx:** gentle clink of cup on saucer |
| 18-28 | Guest lifts cup, sips, pauses | "They said: 'This is lighter than I expected. … Cleaner.'" | LIGHTER. CLEANER. | **broll:** guest's hand setting cup down |
| 28-35 | Host smiles, slight nod to camera | "That's the whole thing. No performance — just tea, and the sound it makes." | YOUR TURN | **sfx:** fade out with ambient room tone |

---

**caption:**  
One pot. Two cups. The sound of hot water hitting the bowl — and a sip that turned out lighter, cleaner than expected. That's how we share tea.  
（一壶。两杯。热水入碗的声音——和一口比想象中更淡、更干净的茶。我们就是这样分享茶。）

**hashtags:**  
`#ChinaStories` `#TeaTime` `#SlowMoments`

---

### evidence_used

| 来源 | 内容 |
|------|------|
| **用户上传素材** | 朋友来访；主人温杯、注水、分茶；热水注入盖碗时有一声轻响；桌上一把壶、两只杯；客人说"这茶比想象中更淡、更干净" |
| **本地论据库** | 未调用（生活场景类，非争议议题） |

---

### 自检清单
- ✅ 已调用 `load_story_knowledge`（仅一次），gate=ready_to_generate
- ✅ 已写一句话核心句，完成结构适配判断（高度适配 A+B+C+E+H）
- ✅ 未虚构人名/茶种/地名/精确钟点/销售额；缺料已省略
- ✅ 正文体现画面感构建（镜头语言）与抽象阶梯（具体动作→分享意义）
- ✅ 开头具体（声音特写），无成就口号开篇
- ✅ 输出字段符合 short_video 规范

---

> ⚠️ **本稿仅供人工审核，不自动发布。** 如需调整时长、增删分镜或补充视觉素材说明，请告知。

### 模型成稿（中文翻译）
---

## 短视频脚本 · short_video（Tier-1）

**knowledge_loaded（知识已加载）:** true  
**format（形态）:** short_video  
**genre（体裁）:** script（体裁完善度：methods_in）  
**结构适配判断:** 高度适配 A+B+C + E（个体）+ H（隐喻）  
**一句话核心句（内部）:** 一壶两杯，热水入碗那一声轻响，和一杯比想象中更淡更干净的茶——分享不需要更多。

---

**title（标题）:** 两杯之间的声音  

**duration_sec（时长秒）:** 35

**shots（分镜）:**

| t（时间） | shot（镜头） | vo（口播） | on_screen（屏显） | broll / sfx（空镜/音效） |
|---|------|----|-----------|-------------|
| 0-3 | 特写：热水注入盖碗 | *（无口播——只留声音）* | LISTEN（听） | **sfx:** 轻柔注水、瓷响 |
| 3-10 | 全景：桌上只有一壶两杯 | 「朋友来了。没有仪式，就是一壶、两杯。」 | ONE POT. TWO CUPS.（一壶。两杯。） | **broll:** 蒸汽升起、安静房间 |
| 10-18 | 手部：温杯 → 注水 → 分茶 | 「先温杯。然后水进去。然后我们分享。」 | WARM · POUR · SHARE（温 · 注 · 分） | **sfx:** 杯轻碰托碟 |
| 18-28 | 客人端杯、品一口、停顿 | 「他们说：『比我想象的更淡。……更干净。』」 | LIGHTER. CLEANER.（更淡。更干净。） | **broll:** 客人放下杯子的手 |
| 28-35 | 主人微笑，微微对镜头点头 | 「就是这些。没有表演——只有茶，和它发出的声音。」 | YOUR TURN（轮到你） | **sfx:** 环境音淡出 |

---

**caption（字幕/说明）:**  
一壶。两杯。热水入碗的声音——和一口比想象中更淡、更干净的茶。我们就是这样分享茶。

**hashtags（话题标签）:**  
`#ChinaStories` `#TeaTime` `#SlowMoments`

---

### evidence_used（所用论据）

| 来源 | 内容 |
|------|------|
| **用户上传素材** | 朋友来访；主人温杯、注水、分茶；热水注入盖碗时有一声轻响；桌上一把壶、两只杯；客人说「这茶比想象中更淡、更干净」 |
| **本地论据库** | 未调用（生活场景类，非争议议题） |

---

### 自检清单
- ✅ 已调用 `load_story_knowledge`（仅一次），gate=ready_to_generate
- ✅ 已写一句话核心句，完成结构适配判断（高度适配 A+B+C+E+H）
- ✅ 未虚构人名/茶种/地名/精确钟点/销售额；缺料已省略
- ✅ 正文体现画面感构建（镜头语言）与抽象阶梯（具体动作→分享意义）
- ✅ 开头具体（声音特写），无成就口号开篇
- ✅ 输出字段符合 short_video 规范

---

> ⚠️ **本稿仅供人工审核，不自动发布。** 如需调整时长、增删分镜或补充视觉素材说明，请告知。

## 简要评语
内容质量约 94.4 分，统一量规通过，Hook 0–3s 与 shots 字段齐全且未编造钟点/销售额，判定 **PASS**。
