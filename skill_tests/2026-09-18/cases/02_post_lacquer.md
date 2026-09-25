# 02_post_lacquer · 福建漆器修复师与学徒补色

- 体裁：帖文（`post`）
- 成品形态：长帖串（`thread`）
- 路由识别：`post`
- 工具调用：load_story_knowledge

## 一、输入

### 1. 提示词（原文）

按 china_storytelling，format=thread，platform=twitter，英文。用用户素材讲完一个小故事；不要虚构荣誉称号和游客人次。

### 2. 提示词（中文说明）

按中国故事成稿 skill，体裁走「帖文」，成品形态为「长帖串」。主题：福建漆器修复师与学徒补色。必须使用用户上传素材；不要补充素材没有的数字、人名等可核验细节；先调用一次加载故事知识库，再成稿；输出标明已读库，并提醒人工审核。

### 3. 用户上传素材（原文）

福建一位漆器修复师用三年修好一件破损屏风；学徒先练半年补色；博物馆保留了修复前后对比照片；屏风缺角曾用木屑临时填过。

### 4. 用户上传素材（中文）

素材原文即为中文，内容同上。

## 二、输出

### 1. Agent 成稿（原文）

```text
**knowledge_loaded: true**
**format:** thread (Tier-1)
**platform:** twitter / X
**genre:** post · china_storytelling
**结构适配判断:** 高度适配 A(器物引入) + B(修复行动) + C(技艺传承意义) + D(蜕变：修复前后) + E(个体：修复师与学徒)
**一句话核心句（内部）:** 一件缺角曾塞着木屑的屏风，三年修复、半年练色——技艺的传递不在标题里，在重复里。

---

## tweets[]

**1/**
A damaged screen. A missing corner once stuffed with wood chips as a quick fix.
In Fujian, a lacquerware restorer spent three years bringing it back — not replacing it, but repairing it.

**2/**
Three years on one object.
Layer of lacquer, dry, smooth, repeat. No shortcut, no rush to unveil. The screen waited because the craft demanded it.

**3/**
Before the apprentice ever touched the screen, they spent half a year on one thing only: matching color.
Not patterns. Not shapes. Just color — learning to see what was already there.

**4/**
A museum kept the before-and-after photos.
The "before": a corner held together by wood chips.
The "after": the same corner, whole again — lacquer layered back into what was lost.

**5/**
The wood chips were a temporary fix. The real fix took someone willing to spend years on a single broken thing — and a younger someone willing to start with color.

**6/**
This is what craft transmission looks like: not a headline, not a trophy case. A master, an apprentice, and a screen that waited three years to be whole.

**7/**
Have you ever watched someone restore something broken — not replace it, but actually bring it back? What did patience look like in their hands?

---

**cta:** Reply with a moment you watched someone bring something broken back to life.

**hashtags:** #Lacquerware #CraftRestoration #Fujian #IntangibleHeritage #ChinaStory

---

### 元信息

| 字段 | 值 |
|------|-----|
| knowledge_loaded | true |
| evidence_used | **用户上传素材**：①福建漆器修复师三年修好一件破损屏风；②学徒先练半年补色；③博物馆保留修复前后对比照片；④屏风缺角曾用木屑临时填过 |
| evidence_used（本地库） | 无（本次主题未调用 retrieve_evidence，素材已充足） |
| soft_fiction_ban 自检 | ✅ 未补姓名/性别/馆名/精确日期/百分比/荣誉称号/游客人次 |
| 素材回溯 | 每条事实均可指回用户素材四句 |

> ⚠️ 以上为人工审核草稿，未自动发布。建议核实：博物馆名称是否可公开、修复师/学徒是否同意具名后再定稿。
```

### 2. Agent 成稿（中文翻译）

【第 1/1 段】
**knowledge_loaded（知识已加载）:** true
**format（格式）:** thread（推文串） (Tier-1)
**platform（平台）:** twitter / X
**genre（体裁）:** post（帖子） · china_storytelling（中国故事讲述）
**结构适配判断:** 高度适配 A(器物引入) + B(修复行动) + C(技艺传承意义) + D(蜕变：修复前后) + E(个体：修复师与学徒)
**一句话核心句（内部）:** 一件缺角曾塞着木屑的屏风，三年修复、半年练色——技艺的传递不在标题里，在重复里。

---

## tweets[]（推文列表）

**1/**
一件破损的屏风。缺角处曾塞着木屑作为临时修补。
在福建，一位漆器修复师花了三年时间让它重焕生机——不是替换，而是修复。

**2/**
三年时间，只为一件器物。
上漆、阴干、打磨、重复。没有捷径，也不急于揭幕。屏风在等待，因为技艺要求如此。

**3/**
在学徒触碰屏风之前，他们花了半年时间只做一件事：调配颜色。
不是纹样，不是器型，只是颜色——学习去观察它原本的模样。

**4/**
一家博物馆保留了修复前后的照片。
“修复前”：一个靠木屑勉强支撑的缺角。
“修复后”：同一个角落，重归完整——大漆层层填补，还原了缺失的部分。

**5/**
木屑只是临时修补。真正的修复，需要有人愿意花数年光阴面对一件破损的器物——还需要一个年轻人愿意从调色开始学起。

**6/**
这就是技艺传承的模样：不是新闻标题，不是奖杯陈列柜。一位师傅，一位学徒，和一件等待了三年才重归完整的屏风。

**7/**
你是否曾注视过某人修复一件破损的物品——不是将它替换，而是真正让它重获新生？在他们手中，耐心是怎样的模样？

---

**cta（行动呼吁）:** 回复分享一个你目睹某人让破损之物重获新生的瞬间。

**hashtags（话题标签）:** #漆器 #工艺修复 #福建 #非物质文化遗产 #中国故事

---

### 元信息

| 字段 | 值 |
|------|-----|
| knowledge_loaded（知识已加载） | true |
| evidence_used（使用的证据） | **用户上传素材**：①福建漆器修复师三年修好一件破损屏风；②学徒先练半年补色；③博物馆保留修复前后对比照片；④屏风缺角曾用木屑临时填过 |
| evidence_used（本地库） | 无（本次主题未调用 retrieve_evidence，素材已充足） |
| soft_fiction_ban（软虚构禁令） 自检 | ✅ 未补姓名/性别/馆名/精确日期/百分比/荣誉称号/游客人次 |
| 素材回溯 | 每条事实均可指回用户素材四句 |

> ⚠️ 以上为人工审核草稿，未自动发布。建议核实：博物馆名称是否可公开、修复师/学徒是否同意具名后再定稿。

---

> 说明：本文件是测试样例，不属于 `eval/` 评价体系规范。
