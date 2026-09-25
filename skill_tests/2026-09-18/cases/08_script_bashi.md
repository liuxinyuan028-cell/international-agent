# 08_script_bashi · 四川坝坝市夜摊与竹凳

- 体裁：短视频脚本（`script`）
- 成品形态：短视频分镜（`short_video`）
- 路由识别：`script`
- 工具调用：load_story_knowledge

## 一、输入

### 1. 提示词（原文）

按 china_storytelling，format=short_video，英文分镜 30-45 秒。一视频一个主点；结尾只要一个软 CTA；不要编摊位数和营收。

### 2. 提示词（中文说明）

按中国故事成稿 skill，体裁走「短视频脚本」，成品形态为「短视频分镜」。主题：四川坝坝市夜摊与竹凳。必须使用用户上传素材；不要补充素材没有的数字、人名等可核验细节；先调用一次加载故事知识库，再成稿；输出标明已读库，并提醒人工审核。

### 3. 用户上传素材（原文）

四川某夜市坝坝市，摊主把竹凳沿路边摆开；灯光来自悬挂的灯泡；一位食客用筷子夹起刚出锅的串串；油烟在镜头前短暂模糊。

### 4. 用户上传素材（中文）

素材原文即为中文，内容同上。

## 二、输出

### 1. Agent 成稿（原文）

```text
---

## short_video · 四川坝坝市夜摊与竹凳

**knowledge_loaded:** true  
**format:** short_video (Tier-1)  
**duration:** 35 秒  
**结构适配判断:** 高度适配 A（场景起点）+ B（行动展示：摊主摆设）+ C（意义延伸：日常烟火）+ E-2（画面感构建）  
**一句话核心句（内部）:** 竹凳、灯泡、串串——四川夜市的烟火气，是最真实的中国日常。

---

**title:** Bamboo stools under bare bulbs  
（标题：裸灯泡下的竹凳）

**duration_sec:** 35

**shots:**

| t | shot | vo | on_screen | broll / sfx |
|---|------|----|-----------|-------------|
| 0-3 | Close-up: oil smoke drifts across lens, then clears | — | — | sfx: sizzle |
| 3-10 | Low angle: bamboo stools lined along curb | "No reservations. No velvet rope." | BAMBOO STOOLS | — |
| 10-18 | Mid: hanging bulbs sway; warm light on faces | "Just a string of bulbs and a street that smells like chili oil." | BABA SHI · SICHUAN | sfx: distant chatter |
| 18-26 | CU: chopsticks lift skewer from pot; steam rises | "One skewer at a time — that's how the night moves here." | — | — |
| 26-32 | Wide: row of stools, people eating, elbows out | "This is what a Sichuan evening looks like when no one's performing." | — | — |
| 32-35 | Static: empty stool, light on it | "Pull up a stool. Tell us what your street food night looks like." | YOUR TURN | sfx: fade out |

---

**caption:**  
Bamboo stools. Bare bulbs. Skewers straight from the pot.  
This is a Sichuan *bàba* night market — no stage, just supper.  
（竹凳、裸灯泡、刚出锅的串串。这就是四川坝坝夜市——没有舞台，只有晚饭。）

**hashtags:** ["ChinaStories", "Sichuan", "StreetFood", "NightMarket"]

---

### evidence_used

| 来源 | 内容 |
|------|------|
| **用户上传素材** | 四川某夜市坝坝市；摊主把竹凳沿路边摆开；灯光来自悬挂的灯泡；一位食客用筷子夹起刚出锅的串串；油烟在镜头前短暂模糊 |
| **本地库** | 未调用（主题为日常场景，无需论据支撑） |

**未编造内容：** 摊位数、营收数字、人名、精确钟点、具体地名（除"四川"外）。

---

⚠️ **本稿为人工审核草稿，不自动发布。** 请核实画面素材与旁白节奏是否匹配实际拍摄条件。
```

### 2. Agent 成稿（中文翻译）

【第 1/1 段】
---

## short_video (短视频) · 四川坝坝市夜摊与竹凳

**knowledge_loaded (知识加载):** true  
**format (格式):** short_video (Tier-1)  
**duration (时长):** 35 秒  
**结构适配判断:** 高度适配 A（场景起点）+ B（行动展示：摊主摆设）+ C（意义延伸：日常烟火）+ E-2（画面感构建）  
**一句话核心句（内部）:** 竹凳、灯泡、串串——四川夜市的烟火气，是最真实的中国日常。

---

**title (标题):** 裸灯泡下的竹凳  

**duration_sec (时长_秒):** 35

**shots (镜头):**

| t (时间) | shot (镜头画面) | vo (旁白) | on_screen (屏幕文字) | broll / sfx (空镜头/音效) |
|---|------|----|-----------|-------------|
| 0-3 | 特写：油烟飘过镜头，随后散去 | — | — | 音效：滋滋声 |
| 3-10 | 低角度：竹凳沿路沿排开 | “无需预约，没有VIP隔离绳。” | 竹凳 | — |
| 10-18 | 中景：悬挂的灯泡摇晃；暖光打在脸上 | “只有一串灯泡，和一条弥漫着辣椒油香气的街道。” | 坝坝市 · 四川 | 音效：远处的喧闹声 |
| 18-26 | 特写：筷子从锅里夹起串串；热气升腾 | “一串接一串——这里的夜晚就是这样度过的。” | — | — |
| 26-32 | 全景：一排竹凳，人们大快朵颐，毫不拘束 | “当无人刻意表演时，四川的夜晚就是这般模样。” | — | — |
| 32-35 | 固定镜头：空着的竹凳，灯光打在上面 | “拉把凳子坐下。告诉我们，你的街头美食之夜是什么样的。” | 轮到你了 | 音效：渐弱 |

---

**caption (文案):**  
竹凳、裸灯泡、刚出锅的串串。  
这就是四川坝坝夜市——没有舞台，只有晚饭。  

**hashtags (标签):** ["ChinaStories", "Sichuan", "StreetFood", "NightMarket"]

---

### evidence_used (素材来源)

| 来源 | 内容 |
|------|------|
| **用户上传素材** | 四川某夜市坝坝市；摊主把竹凳沿路边摆开；灯光来自悬挂的灯泡；一位食客用筷子夹起刚出锅的串串；油烟在镜头前短暂模糊 |
| **本地库** | 未调用（主题为日常场景，无需论据支撑） |

**未编造内容：** 摊位数、营收数字、人名、精确钟点、具体地名（除"四川"外）。

---

⚠️ **本稿为人工审核草稿，不自动发布。** 请核实画面素材与旁白节奏是否匹配实际拍摄条件。

---

> 说明：本文件是测试样例，不属于 `eval/` 评价体系规范。
