---
title: CR-BLE天线接口与匹配
type: mcu_check_rule
aliases: ["CR_BLE_RF_Antenna","BRF_ANT审图规则"]
tags: ["企业MCU","AI审图规则","原理图审图","风险等级-优化建议"]
sources: [[SF32LB52X_Datasheet_V0.2.6]]
mcu_family: ["SF32LB52"]
series_applicability: ["通用-两系列共用"]
mcu_model: ["SF32LB52X家族"]
hardware_version: ["QFN68L"]
risk_level: 优化建议
created: 2026-08-10
updated: 2026-08-10
---

## 摘要
校验 SF32LB52X 无线接口 BRF_ANT（引脚 53）的天线连接与匹配网络，利用其片上已集成 Balun/匹配的特性，必要时补 π 型网络以满足谐波指标。

## 核心硬件内容（背景）
SF32LB52X 集成双模 BT5.3，片上已集成 Balun 与天线匹配网络，**通常无需片外匹配**；BRF_ANT(53) 直接接天线。在 +19dBm 发射下，二次谐波 ‑50dBm、三次 ‑40dBm（带外部 π 型匹配时）。详见 [[SF32LB52_Peripheral_BLE_RF]]。

## 专项业务内容 —— 原理图 AI 审图规则（必填）
1. **判定条件**：解析到 SF32LB52X BRF_ANT(53) 网络时，检查是否接天线/匹配网络，是否串入不匹配无源网络，以及 AVDD_BRF(52) 是否独立滤波。
2. **违规现象描述**：BRF_ANT 误串入额外 Balun/不匹配网络导致失配；天线端无 ESD 保护；AVDD_BRF 未独立低噪滤波。
3. **风险影响说明**：失配 → 反射/发射功率下降/谐波超标；射频性能劣化（优化建议级，认证可能不通过）。
4. **标准化整改方案**：BRF_ANT 直接接天线；如谐波/回波不达标再加外部 π 型匹配（按参考设计取值）；AVDD_BRF 独立去耦；天线端加 ESD 器件。
5. **知识库溯源依据**：[[SF32LB52_Peripheral_BLE_RF]]；Datasheet §3.1（P12）、§4.3 RF 特性（P32–P35）、Table 5-3（P47）。

## 关联页面
- BLE/RF：[[SF32LB52_Peripheral_BLE_RF]]｜电源：[[SF32LB52_Peripheral_Power]]
- 同类规则：[[CR_PowerDomains]]、[[CR_AbsMaxRatings]]

## 原始来源完整引用
1. [DS5202-SF32LB52X-Datasheet V0p2p6.pdf]，Raw：raw/mcu/all_chip/datasheets/，§3.1（P12）、§4.3（P32–P35）、Table 5-3（P47）

## 待核实问题
- BRF_ANT 推荐 π 型匹配具体值待补参考设计。
