---
title: CR-SF32LB57绝对最大额定值与IO约束
type: mcu_check_rule
aliases: ["CR_SF32LB57_AbsMaxRatings","SF32LB57绝对最大额定值审图规则"]
tags: ["企业MCU","AI审图规则","原理图审图","风险等级-严重"]
sources: [[SF32LB57X_Datasheet_V0.2_20260909],[SF32LB57x_batt_Datasheet_V0.2_20260909],[SF32LB57_Peripheral_Power]]
mcu_family: ["SF32LB57"]
series_applicability: ["系列相关-按引脚归属"]
mcu_model: ["SF32LB57X","SF32LB57x"]
hardware_version: ["QFN68 7x7","QFN80 8x8","BGA112 5.4x4.4","Datasheet V0.2"]
risk_level: 严重
created: 2026-09-09
updated: 2026-09-09
---

## 摘要
校验 SF32LB57 家族各电源引脚**不得超过绝对最大额定值**，以及 Buck / 内部 LDO 输出脚、参考电压脚的正确处理。超限将造成芯片永久损伤。

## 核心硬件内容（背景）
**绝对最大值（Table 4-2，两册一致）**
| Symbol | Description | Max | Unit |
|---|---|---|---|
| VBUS | VBUS power input | **5.5** | V |
| VBAT | VBAT power output | **4.7** | V |
| VCC | System power input | **4.7** | V |
| PVDD | System power input | **3.63** | V |
| TStorage | Storage temperature | ‑40 ~ +125 | °C |

**推荐工作条件（Table 4-1）**
| Symbol | Min | Typ | Max |
|---|---|---|---|
| VBUS | 4.5 | 5 | 5.5 |
| VBAT | 3.0 | — | 4.7 |
| VCC | 3.0* | — | 4.7 |
| PVDD | 2.97 | — | 3.63 |
| Tamb | ‑40 | — | +85 |
> * 开机电压 3.5V ±10%

**引脚归属（关键）**
- **PVDD(19) 属 3.3V 系列**；**VBUS(21)/VBAT(20)/VCC(24) 属电池系列**。审图须**只对实际存在的引脚**施加对应限值 —— 详见 [[CR_SF32LB57_PowerSeries]]。

**ESD / 可靠性（Table 4-4）**：HBM ±4000V（JS-001-2017）、CDM ±1000V（JS-002-2018）、Latch-up I-Test ±200mA / OVT +1.5×VddMAX（JESD78E）、MSL3（回流 260+0°C 20s ×3）。

## 专项业务内容 —— 原理图 AI 审图规则（必填）
1. **判定条件**：PDF 解析到 SF32LB57 家族芯片的任一电源网络（PVDD / VBUS / VBAT / VCC / AVDD33 / AVDD33_AUD / AVDD_BRF / VDDIOA / VDDIOSB）时触发。

2. **违规现象描述**：
   - **PVDD / AVDD33 / AVDD33_AUD / AVDD_BRF 电压 > 3.63V**；
   - 电池系列 **VBUS > 5.5V**、**VBAT / VCC > 4.7V**；
   - 工作环境温度超出 ‑40 ~ +85 °C 或存储超出 ‑40 ~ +125 °C；
   - **Buck 被旁路**（BUCK_LX(18) 未接电感、BUCK_FB(17) 未接电容到地）；
   - **内部 LDO 输出脚被外部供电**：VDD_VOUT1(16)、VDD_VOUT2(15)、VDD_RET(13)、VDD_RTC(12)、VDD18_VOUT(23)、以及电池系列 VDD33_VOUT1(22)/VDD33_VOUT2(14)、VSYS(19)；
   - **GPADC_VREF(68) / AUD_VREF(39) 被外部供电**（应仅接电容到地）；
   - **电池系列 VDD33_VOUT1/2 负载 > 150mA**；
   - **EPAD(69) 未接 GND**。

3. **风险影响说明**：过压 → 器件永久损伤/ latch-up/起火；内部 LDO 反灌 → 电源冲突损坏；Buck 旁路 → 系统不上电（严重，部分场景致命）。

4. **标准化整改方案**：
   - 3.3V 系列所有 3.3V 域电源（PVDD/AVDD33/AVDD33_AUD/AVDD_BRF/VDDIOA）须由 ≤3.63V 稳压源供电，推荐 3.3V；
   - 电池系列 VBUS 加 OVP 保护（≤5.5V），VBAT/VCC 不超过 4.7V（芯片过充保护阈值 4.78V，见 [[SF32LB57x_batt]] §6）；
   - Buck 电感按参考设计选型，BUCK_FB 接电容到地，**不得旁路**；
   - 所有内部电源输出脚仅接去耦电容到地，**禁止外部供电**；
   - GPADC_VREF / AUD_VREF 仅接电容到地；
   - VDD33_VOUT1/2 各带载 ≤150mA；
   - EPAD 可靠接地（散热兼电气地）。

5. **知识库溯源依据**：[[SF32LB57_Peripheral_Power]]；[[SF32LB57X]] §3–§5；[[SF32LB57x_batt]] §4–§6；DS5702 Table 4-1/4-2/4-3（P39）、Table 4-4（P40）、Table 5-3（P61）；DS5701 同表（P40–41、P62）。

## 关联页面
- 家族：[[SF32LB57]]｜3.3V：[[SF32LB57X]]｜电池：[[SF32LB57x_batt|SF32LB57x]]
- 双系列引脚匹配：[[CR_SF32LB57_PowerSeries]]｜电源外设：[[SF32LB57_Peripheral_Power]]
- 来源：[[SF32LB57X_Datasheet_V0.2_20260909]]、[[SF32LB57x_batt_Datasheet_V0.2_20260909]]
- 方法学参照：[[CR_AbsMaxRatings]]（52 家族）

## 原始来源完整引用
1. [DS5702-SF32LB57X V0.2]，Raw：`raw/mcu/all_chip/datasheets/DS5702-SF32LB57X-芯片技术规格书-V0p2-20260909.pdf`，Table 4-1（P39 运行条件）、Table 4-2（P39 绝对最大值）、Table 4-3（P39 I/O @3.3V）、Table 4-4（P40 可靠性）、Table 4-20（P48 充电模块）。
2. [DS5701-SF32LB57x V0.2]，Raw：`raw/mcu/all_chip/datasheets/DS5701-SF32LB57x-芯片技术规格书-V0p2-20260909.pdf`，同表（P40–41、P49）。

## 待核实问题
- **Table 4-1/4-2 在两册中完全相同且同时含 VBUS/VBAT/VCC 与 PVDD**，但 3.3V 系列引脚表无 VBUS/VBAT/VCC。审图时**必须先判定系列，再只对该系列实际存在的引脚施加限值**。
- 规格书为 V0.2 草稿，限值可能变更；量产前须复核。
- **功耗参数（Table 4-5/4-6）全部 TBD**，本规则暂不含电流/热预算校验，待补。
