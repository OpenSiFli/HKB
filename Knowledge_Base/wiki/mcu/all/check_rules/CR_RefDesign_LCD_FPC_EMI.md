---
title: CR-参考设计-LCD FPC排线EMI
type: mcu_check_rule
aliases: ["CR_RefDesign_LCD_FPC_EMI","LCD排线EMI审图规则"]
tags: ["企业MCU","AI审图规则","原理图审图","风险等级-优化建议"]
sources: [[SF32LB52X_3V3_Reference_Schematic],[SF32LB52x_batt_Reference_Schematic],[SF32LB52_Peripheral_Power]]
mcu_family: ["SF32LB52"]
series_applicability: ["通用-两系列共用"]
mcu_model: ["SF32LB52X家族","SF32LB52x家族"]
hardware_version: ["QFN68L"]
risk_level: 优化建议
created: 2026-08-13
updated: 2026-08-13
---

## 摘要
依据 SF32LB52 官方参考设计，校验 **LCD FPC 排线及相关高速/时钟信号的 EMI 布线**是否符合黄金样板，避免排线辐射影响射频天线与蓝牙性能。

## 核心硬件内容（背景）
参考设计明确：LCD 信号无法完全屏蔽，排线延伸到屏上是**最主要的 EMI 源**。故要求：
- 结构上排线尽量短，且**远离射频天线**（考虑对天线的辐射影响）；
- 芯片到排线接插件之间的走线**走 PCB 内层、上下都用地包起来**；
- 时钟和数据线上**预留 RC 位置**滤除高阶谐波；
- Flash 芯片放**屏蔽罩内部**，信号线中间预留 RC 器件，走线尽量短优先走内层；
- LCD 电源须用**低 Iq LDO** 供电。

## 专项业务内容 —— 原理图 AI 审图规则（必填）
1. **判定条件**：PDF 解析到 LCD 接口（PA00–PA09 QSPI/8080/JDI、BTB-FPC 接插件）及外部 Flash 布线时触发。
2. **违规现象描述**：LCD FPC 排线过长或紧邻射频天线；芯片到接插件走线未走内层/未包地；时钟/数据线未预留 RC 滤波；Flash 未入屏蔽罩；LCD 电源未用低 Iq LDO。
3. **风险影响说明**：EMI 辐射 → 射频/蓝牙性能劣化、EMC 测试不通过（优化建议）。
4. **标准化整改方案**：按参考设计布线——短排线、远天线、内层包地、时钟/数据线预留 RC、Flash 入屏蔽罩、LCD 用低 Iq LDO。
5. **知识库溯源依据**：[[SF32LB52_Peripheral_Power]]（EMI/EMC 配套）；参考设计两页（LCD FPC 与 Flash EMI 注释）。

## 关联页面
- 电源/EMI：[[SF32LB52_Peripheral_Power]]｜BLE 天线：[[CR_BLE_RF_Antenna]]｜参考设计：[[SF32LB52X_3V3_Reference_Schematic]]

## 原始来源完整引用
1. [SF32LB52X_3V3-Reference-SCH-V1.0.0_20251015.pdf] / [SF32LB52x_batt-Reference-SCH-V1.0.0_20251015.pdf]，Raw：raw/mcu/ref_design/，设计注释（LCD FPC 排线 EMI、Flash 屏蔽罩与 RC）

## 待核实问题
- 无（参数来自参考设计黄金样板）。
