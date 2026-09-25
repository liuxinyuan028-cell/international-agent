# 07_script_tea · 茶席分享与热水声

- 体裁：短视频脚本（`script`）
- 成品形态：短视频分镜（`short_video`）
- 路由识别：`script`
- 工具调用：load_story_knowledge

## 一、输入

### 1. 提示词（原文）

按 china_storytelling，format=short_video，约 35 秒英文口播分镜。须有 Hook 0-3 秒；不要编假精确钟点和销售额。

### 2. 提示词（中文说明）

按中国故事成稿 skill，体裁走「短视频脚本」，成品形态为「短视频分镜」。主题：茶席分享与热水声。必须使用用户上传素材；不要补充素材没有的数字、人名等可核验细节；先调用一次加载故事知识库，再成稿；输出标明已读库，并提醒人工审核。

### 3. 用户上传素材（原文）

朋友来访时主人温杯、注水、分茶；热水注入盖碗时有一声轻响；桌上只有一把壶和两只杯；客人说这茶比想象中更淡、更干净。

### 4. 用户上传素材（中文）

素材原文即为中文，内容同上。

## 二、输出

### 1. Agent 成稿（原文）

```text
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
```

### 2. Agent 成稿（中文翻译）

【第 1/1 段】
---

## 短视频脚本 · short_video (短视频)（Tier-1）

**knowledge_loaded (知识已加载):** true  
**format (格式):** short_video (短视频)  
**genre (体裁):** script (脚本)（体裁完善度：methods_in）  
**结构适配判断:** 高度适配 A+B+C + E（个体）+ H（隐喻）  
**一句话核心句（内部）:** 一壶两杯，热水入碗那一声轻响，和一杯比想象中更淡更干净的茶——分享不需要更多。

---

**title (标题):** 两杯之间的声音

**duration_sec (时长_秒):** 35

**shots (镜头):**

| t (时间) | shot (镜头) | vo (旁白) | on_screen (屏幕文字) | broll / sfx (空镜头 / 音效) |
|---|------|----|-----------|-------------|
| 0-3 | 特写：热水注入盖碗 | *（无旁白——仅有声音）* | 倾听 | **sfx (音效):** 轻柔的注水声，陶瓷共鸣声 |
| 3-10 | 全景：桌上一壶两杯 | “朋友顺道来访。没有繁文缛节，只有一壶两杯。” | 一壶。两杯。 | **broll (空镜头):** 热气升腾，房间静谧 |
| 10-18 | 手部特写：温杯 → 注水 → 分茶 | “先温杯。然后注水。然后我们分享。” | 温 · 注 · 享 | **sfx (音效):** 茶杯与杯托轻碰的清脆声 |
| 18-28 | 客人端起茶杯，品饮，停顿 | “他们说：‘这茶比想象中更淡。……更干净。’” | 更淡。更净。 | **broll (空镜头):** 客人放下茶杯的手部动作 |
| 28-35 | 主人微笑，向镜头微微点头 | “就这么简单。没有表演——只有茶，和它发出的声音。” | 该你了 | **sfx (音效):** 伴随室内环境音渐弱 |

---

**caption (文案):**  
一壶。两杯。热水入碗的轻响——和一口比想象中更淡、更干净的茶。我们就是这样分享茶。

**hashtags (标签):**  
`#ChinaStories (中国故事)` `#TeaTime (品茶时光)` `#SlowMoments (慢享时光)`

---

### evidence_used (使用证据)

| 来源 | 内容 |
|------|------|
| **用户上传素材** | 朋友来访；主人温杯、注水、分茶；热水注入盖碗时有一声轻响；桌上一把壶、两只杯；客人说“这茶比想象中更淡、更干净” |
| **本地论据库** | 未调用（生活场景类，非争议议题） |

---

### 自检清单
- ✅ 已调用 `load_story_knowledge`（仅一次），gate=ready_to_generate
- ✅ 已写一句话核心句，完成结构适配判断（高度适配 A+B+C+E+H）
- ✅ 未虚构人名/茶种/地名/精确钟点/销售额；缺料已省略
- ✅ 正文体现画面感构建（镜头语言）与抽象阶梯（具体动作→分享意义）
- ✅ 开头具体（声音特写），无成就口号开篇
- ✅ 输出字段符合 short_video (短视频) 规范

---

> ⚠️ **本稿仅供人工审核，不自动发布。** 如需调整时长、增删分镜或补充视觉素材说明，请告知。

---

> 说明：本文件是测试样例，不属于 `eval/` 评价体系规范。
