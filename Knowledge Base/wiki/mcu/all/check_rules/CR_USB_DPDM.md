---
title: CR-USB差分对DP/DM
type: mcu_check_rule
aliases: ["CR_USB_DPDM","USB DP/DM审图规则"]
tags: ["企业MCU","AI审图规则","原理图审图","风险等级-严重"]
sources: [[SF32LB52X_Datasheet_V0.2.6]]
mcu_family: ["SF32LB52"]
series_applicability: ["通用-两系列共用"]
mcu_model: ["SF32LB52X家族"]
hardware_version: ["QFN68L"]
risk_level: 严重
created: 2026-08-10
updated: 2026-08-10
---

## 摘要
校验 SF32LB52X USB2.0 FS 差分数据线 DP/DM（PA35=#USB11_DP / PA36=#USB11_DM）的片内 PHY 使用、差分阻抗与等长，禁止外接独立收发器。

## 核心硬件内容（背景）
SF32LB52X 集成 USB2.0 FS PHY，DP/DM 直接由 GPIO 复用（PA35/PA36，Sel#=2）引出，无需外置收发器。详见 [[SF32LB52_Peripheral_USB]]。

## 专项业务内容 —— 原理图 AI 审图规则（必填）
1. **判定条件**：解析到 SF32LB52X 的 USB DP(PA35)/DM(PA36) 网络时，检查是否按 USB FS 差分规范布线、是否误接外部 USB 收发器、VBUS 检测与上下拉是否齐备。
2. **违规现象描述**：DP/DM 未做 90Ω 差分阻抗控制/未等长；在 DP/DM 上外接独立 USB 收发器或错误电平转换；缺 VBUS 检测与 FS 上拉（D+ 1.5kΩ）。
3. **风险影响说明**：阻抗/等长失控 → 眼图劣化、通信丢包/失败；外接收发器与片内 PHY 冲突（严重）。
4. **标准化整改方案**：DP/DM 按 90Ω±10% 差分阻抗、做等长并包地；移除任何外部收发器；补齐 VBUS 检测与 FS 上拉（按参考设计）；确认 PA35/PA36 复用 Sel#=2。
5. **知识库溯源依据**：[[SF32LB52_Peripheral_USB]]；Datasheet §3.5.8（P20）、Table 5-2（P55）。

## 关联页面
- USB：[[SF32LB52_Peripheral_USB]]｜GPIO：[[SF32LB52_Peripheral_GPIO]]｜电源：[[SF32LB52_Peripheral_Power]]
- 同类规则：[[CR_AbsMaxRatings]]

## 原始来源完整引用
1. [DS5202-SF32LB52X-Datasheet V0p2p6.pdf]，Raw：raw/mcu/all_chip/datasheets/，§3.5.8（P20）、Table 5-2（P55）

## 待核实问题
- VBUS 检测与 FS 上拉实现方式待补参考设计。
