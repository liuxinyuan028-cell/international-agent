# 短视频脚本工序卡（体裁：脚本 script）

**何时用**：`short_video`（完整短视频脚本）/ `reel_hook`（只要前几秒钩子）/ 口播分镜。  
**不用**：特稿、通稿、IG（Instagram）长 caption（配文）冒充分镜、FAQ（常见问答）清单。  
**细则**：`china-story-script-reference.md` + `docs/corpus/script/`。  
**状态**：`methods_in`（方法已入库、评测未齐；标在输出里）。铁律：`intl-comm.md`（国际传播）+ evidence（证据规则）。

## 步骤

1. 确认 format（成品形态）：完整脚本 or 只要前 3 秒钩子；平台；时长
2. `reel_hook`（钩子方案）→ 只出 ≥3 个 0–3 秒方案，停
3. 先写 ≥3 钩子再选 1；禁「大家好 / Today I'm going to…（今天我要讲…）」
4. 填分镜：Hook 钩子(0–3 秒) → Body 主体(一视频一点，每句 VO 旁白都有 shot 镜头) → Payoff 收束 + **一个**软 CTA（轻行动号召，如提问邀约，非硬推销）
5. 目标约 28–45 秒（材料厚可 45–60）；约 21 秒前有第一「奖赏」画面
6. 无声也能看懂（字幕关键词）；事实 ∈ evidence（必须落在证据内）；无假精确钟点

## 分镜行字段

| 字段 | 中文 |
|------|------|
| `t` | 时间段 |
| `shot` | 镜头（景别+主体，禁「好看点」） |
| `vo` | VO 旁白/口播 |
| `on_screen` | 画面上字幕/关键词 |
| `broll` | B-roll 空镜/补充画面 |
| `sfx?` | 可选音效 |

整稿：`title`（标题）· `duration_sec`（时长秒）· `shots[]`（分镜列表）· `caption`（配文）· `hashtags?`（可选话题标签）· `genre: script`（体裁：脚本）· `genre_status: methods_in`（方法已入库）

## 红线

- 一视频一个主点；CTA（行动号召）不抬杠他国  
- 不写成帖文 5W 或通稿电头  
- 无 evidence（证据）不写数字/姓名/假地址对话  
