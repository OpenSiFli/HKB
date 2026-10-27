---
title: CR-参考设计-电池系列内置电源树
type: mcu_check_rule
aliases: ["CR_RefDesign_Batt_PowerTree","电池电源树审图规则"]
tags: ["企业MCU","AI审图规则","原理图审图","风险等级-严重"]
sources: [[SF32LB52x_batt_Reference_Schematic],[SF32LB52x_batt],[SF32LB52_Peripheral_Power]]
mcu_family: ["SF32LB52"]
series_applicability: ["SF32LB52x(电池)"]
mcu_model: ["SF32LB52x家族"]
hardware_version: ["QFN68L"]
risk_level: 严重
created: 2026-08-13
updated: 2026-08-13
---

## 摘要
依据 SF32LB52x（电池系列）官方参考设计，校验 **内置电源树分配**是否符合黄金样板：VSYS_3V3 仅供 MCU 内部；VDD33_VOUT1 最大 150mA（Flash+Sensor）、VDD33_VOUT2 最大 150mA（马达）；三者外挂电容之和 <9.6µF；AVDD_BRF←VSYS_3V3、AVDD33_AUD←VDD33_VOUT1；VBAT&VCC 短接且去耦靠近芯片；VDD18_VOUT 走线 <10pF 包地。

## 核心硬件内容（背景）
- **VSYS_3V3**：仅能供 MCU 内部使用，**禁止给外设**。
- **VDD33_VOUT1**：最大电流 **150mA**，推荐给外部 Flash 和 Sensor 供电。
- **VDD33_VOUT2**：最大电流 **150mA**，可单独给马达供电。
- **VSYS_3V3 + VDD33_VOUT1 + VDD33_VOUT2 外挂电容之和 < 9.6µF**。
- **AVDD_BRF 由 VSYS_3V3 供电**；**AVDD33_AUD 由 VDD33_VOUT1 供电**。
- **VBAT 与 VCC 接在一起**使用（待机=deepsleep，关机=Hibernate），去耦电容靠近芯片。
- **VDD18_VOUT（pin23，内部 LDO 输出）**：走线**寄生电容 <10pF、立体包地处理**；SF32LB520 须焊接 R0106，SF32LB523/5/7 按型号处理。
- 船运/关机（Hibernate）：仅 VSYS_3V3 有输出，其他 VBAT 下游器件电源默认关闭。

## 专项业务内容 —— 原理图 AI 审图规则（必填）
1. **判定条件**：PDF 解析到电池系列 VSYS_3V3 / VDD33_VOUT1 / VDD33_VOUT2 / VDD18_VOUT / AVDD_BRF / AVDD33_AUD / VBAT / VCC 网络分配时触发。
2. **违规现象描述**：
   - 外设挂到 **VSYS_3V3**（仅内部用）；
   - VDD33_VOUT1 / VDD33_VOUT2 负载 >150mA（超载跌落）；
   - 三者外挂电容之和 **>9.6µF**；
   - AVDD_BRF / AVDD33_AUD 供电源接错；
   - VBAT 与 VCC 未短接或去耦远离芯片；VDD18_VOUT 走线寄生电容 >10pF 或未包地。
3. **风险影响说明**：电源树错配 → UVLO/电源崩溃、模拟射频性能劣化、待机漏电（严重）。
4. **标准化整改方案**：按树分配负载（VOUT1→Flash+Sensor、VOUT2→马达、VSYS_3V3→仅内部）；控制总电容 <9.6µF；AVDD_BRF←VSYS_3V3、AVDD33_AUD←VOUT1；VBAT&VCC 短接靠近去耦；VDD18_VOUT 走线 <10pF 包地。
5. **知识库溯源依据**：[[SF32LB52x_batt]]；[[SF32LB52_Peripheral_Power]]；[[SF32LB52x_batt_Reference_Schematic]]。

## 关联页面
- 芯片实体：[[SF32LB52x_batt]]｜电源：[[SF32LB52_Peripheral_Power]]｜OVP/充电器：[[CR_RefDesign_Batt_OVP_Charger]]｜多电源域：[[CR_PowerDomains]]

## 原始来源完整引用
1. [SF32LB52x_batt-Reference-SCH-V1.0.0_20251015.pdf]，Raw：raw/mcu/ref_design/SF32LB52x_batt/，设计注释（电源树电流/电容限制、AVDD 供电源、VDD18_VOUT 走线要求）

## 待核实问题
- 无（参数来自参考设计黄金样板）。
