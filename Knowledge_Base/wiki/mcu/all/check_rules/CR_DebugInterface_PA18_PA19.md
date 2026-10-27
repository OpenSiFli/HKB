---
title: CR-调试接口引脚(PA18/PA19)保留
type: mcu_check_rule
aliases: ["CR_DebugInterface_PA18_PA19","调试接口审图规则"]
tags: ["企业MCU","AI审图规则","原理图审图","风险等级-优化建议"]
sources: [[SF32LB52X_UserManual_V0.8.8],[SF32LB52X]]
mcu_family: ["SF32LB52"]
series_applicability: ["通用-两系列共用"]
mcu_model: ["SF32LB52X家族"]
hardware_version: ["QFN68L","V0.8.8"]
risk_level: 优化建议
created: 2026-08-11
updated: 2026-08-11
---

## 摘要
校验 SF32LB52X 调试接口引脚 PA18(SWDIO, 默认 PU)/PA19(SWCLK, 默认 No Pull) 在原理图中被合理保留，避免量产/低功耗下调试不可连。

## 核心硬件内容（背景）
调试器默认经 PA18/PA19（SWDIO/SWCLK）连接；另提供 UART 调试经 USART1（RX=PA18、TX=PA19，上电默认 1M/8N1）。PA18 上电默认上拉、PA19 默认无上下拉。低功耗下若 IO 功能被改、USART1/DMAC1 复位、或进入 deepsleep/standby/hibernate，调试会断开/失效。详见 [[DR_Debug_Interface]]、[[FC_DebugInterface_Failure]]、[[SF32LB52_Peripheral_USB]]。

## 专项业务内容 —— 原理图 AI 审图规则（必填）
1. **判定条件**：PDF 原理图解析到 PA18/PA19 被复用为普通 GPIO/外设功能，或连接会拉低/拉高影响调试的电路时，核对调试可访问性。
2. **违规现象描述**：① PA18/PA19 被强上拉/强下拉或接固定电平，导致 SWD/UART 调试无法工作；② 量产把 PA18/PA19 仅作普通 IO 又无测试点，返修无法调试；③ 调试接口无 TVS/ESD 保护（产线插拔风险）。
3. **风险影响说明**：调试不可连 → 产测/返修困难；ESD 损伤 IO（优化建议）。
4. **标准化整改方案**：保留 PA18/PA19 测试点或串阻；避免外部固定电平冲突默认态；调试走线加 ESD 防护；低功耗设计保证唤醒后可重连调试。
5. **知识库溯源依据**：[[SF32LB52X_UserManual_V0.8.8]] P57（4.2.6 调试器行为）、P362（15.8/15.9 调试接口与失效）；[[SF32LB52x_batt|SF32LB52x]] §10 调试接口。

## 关联页面
- 芯片实体：[[SF32LB52x_batt|SF32LB52x]]｜USB/调试：[[SF32LB52_Peripheral_USB]]｜设计规范：[[DR_Debug_Interface]]｜故障案例：[[FC_DebugInterface_Failure]]

## 原始来源完整引用
1. [UM5201‐SF32LB52x‐CN.pdf]，Raw：raw/mcu/all_chip/datasheets/UM5201‐SF32LB52x‐CN.pdf，P57、P362

## 待核实问题
- 无（本规则依据明确）。
