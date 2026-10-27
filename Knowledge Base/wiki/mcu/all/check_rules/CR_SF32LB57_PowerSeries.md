---
title: CR-SF32LB57双系列电源引脚匹配
type: mcu_check_rule
aliases: ["CR_SF32LB57_PowerSeries","SF32LB57双系列电源审图规则"]
tags: ["企业MCU","AI审图规则","原理图审图","风险等级-致命"]
sources: [[SF32LB57X_Datasheet_V0.2_20260909],[SF32LB57x_batt_Datasheet_V0.2_20260909],[SF32LB57_Peripheral_Power]]
mcu_family: ["SF32LB57"]
series_applicability: ["系列相关-两系列对照"]
mcu_model: ["SF32LB57X","SF32LB57x"]
hardware_version: ["QFN68 7x7","QFN80 8x8","BGA112 5.4x4.4","Datasheet V0.2"]
risk_level: 致命
created: 2026-09-09
updated: 2026-09-09
---

## 摘要
SF32LB57 家族**两系列（3.3V / 电池）的电源专用引脚定义完全不同但封装兼容（同 QFN68）**。本规则校验原理图所选芯片系列与其电源引脚连接是否匹配，防止"电池系列电路套在 3.3V 料号上"或反之——此类错误将直接导致芯片不工作或永久损坏。

## 核心硬件内容（背景）
**QFN68 同封装下，两系列 pin 14/19/20/21/22/24 定义完全不同**：

| 引脚 | 3.3V 系列 SF32LB57X | 电池系列 SF32LB57x |
|---|---|---|
| 14 | AVDD33（模拟电源**输入**，接 3.3V） | VDD33_VOUT2（3.3V LDO2 **输出**，150mA） |
| 19 | PVDD（PMU 电源**输入**，接 3.3V） | VSYS（电源**输出** 3.0V，外挂电容到地） |
| 20 | VBATS（电池电压**检测输入**） | VBAT（电源**输出**，接电池） |
| 21 | VDDIOA（GPIO 电源**输入**） | VBUS（充电模块电源**输入**） |
| 22 | NC（**必须悬空**） | VDD33_VOUT1（3.3V LDO1 **输出**，150mA） |
| 24 | GPIO（非专用脚） | VCC（系统电源**输入**，接电池） |
| 52 | AVDD_BRF（接 **3.3V**） | AVDD_BRF（接 **VSYS**） |

**系列判定（权威）**：以芯片命名大小写判定——**大写 X = 3.3V 系列（DS5702）**，**小写 x = 电池系列（DS5701）**。文档标题大小写与芯片命名一致。

## 专项业务内容 —— 原理图 AI 审图规则（必填）
1. **判定条件**：PDF 原理图解析到 SF32LB57 家族芯片（型号含 `SF32LB57`）的电源网络（PVDD / VDDIOA / VBATS / VBUS / VBAT / VSYS / VCC / VDD33_VOUT1 / VDD33_VOUT2 / AVDD33 / AVDD_BRF）时触发。**必须先从 BOM 或位号确定芯片料号所属系列**，再逐脚核对。

2. **违规现象描述**：
   - 3.3V 料号（SF32LB57X）却按电池系列接线（如 pin21 接 VBUS、pin24 接电池、pin19 当输出用）；
   - 电池料号（SF32LB57x）却按 3.3V 系列接线（如 pin19 接 3.3V 电源、pin21 外接 GPIO 电源、pin22 悬空而丢失 VDD33_VOUT1）；
   - 电池系列 **AVDD_BRF(52) 接到 3.3V**（应为 VSYS）；
   - 3.3V 系列 **pin22(NC) 被连接**（应悬空）；
   - 电源输出脚（VDD33_VOUT1/2、VSYS、VDD_VOUT1/2、VDD_RET、VDD_RTC、VDD18_VOUT）被**外部供电**；
   - **VDD33_VOUT1/2 负载超过 150mA**；
   - **GPADC_VREF(68) / AUD_VREF(39) 被外部供电**（应仅接电容到地）。

3. **风险影响说明**：电源引脚错配 → 芯片不上电、内部 LDO 反灌、电池反充或短路 → **永久损坏 / 起火风险**（致命）。

4. **标准化整改方案**：
   - 先确认料号与系列（见 [[SF32LB57]] §订购信息 / 两份规格书 Table 6-1）；
   - 按 [[SF32LB57_Peripheral_Power]] §1 对照表逐脚核对并修正；
   - 电池系列：VCC(24) 与 VBAT(20) 接电池，VBUS(21) 接充电输入，VSYS(19) 外挂电容到地，AVDD_BRF(52) 接 VSYS；
   - 3.3V 系列：PVDD(19) 接 3.3V，VDDIOA(21) 供 GPIO，AVDD33(14)/AVDD33_AUD(38)/AVDD_BRF(52) 接 3.3V，pin22 悬空。

5. **知识库溯源依据**：[[SF32LB57_Peripheral_Power]]；[[SF32LB57X]] §2；[[SF32LB57x_batt]] §2；DS5702 Table 5-3（P61）；DS5701 Table 5-3（P62）。

## 关联页面
- 家族：[[SF32LB57]]｜3.3V：[[SF32LB57X]]｜电池：[[SF32LB57x_batt|SF32LB57x]]
- 电源外设：[[SF32LB57_Peripheral_Power]]｜绝对最大额定值：[[CR_SF32LB57_AbsMaxRatings]]
- 来源：[[SF32LB57X_Datasheet_V0.2_20260909]]、[[SF32LB57x_batt_Datasheet_V0.2_20260909]]
- 方法学参照（52 家族）：[[CR_PowerDomains]]

## 原始来源完整引用
1. [DS5702-SF32LB57X V0.2]，Raw：`raw/mcu/all_chip/datasheets/DS5702-SF32LB57X-芯片技术规格书-V0p2-20260909.pdf`，Table 5-3（P61，QFN68 3.3V 专用管脚）、Table 5-4（P62，QFN80）、Table 6-1（P83）。
2. [DS5701-SF32LB57x V0.2]，Raw：`raw/mcu/all_chip/datasheets/DS5701-SF32LB57x-芯片技术规格书-V0p2-20260909.pdf`，Table 5-3（P62，QFN68 电池专用管脚）、Table 6-1（P84）。

## 待核实问题
- 两份规格书均为 **V0.2 草稿**，引脚定义可能变更，量产前须复核。
- 两册 Table 4-1/4-2 电气表均含 VBUS/VBAT/VCC 与 PVDD 参数、Table 4-20 充电模块特性——**这是芯片裸 die 同时支持电池供电与常规 3.3V 供电两种模式的完整能力描述，非错误**（规格书多处明确，见一致性核查报告）。QFN68 3.3V 封装（DS5702 Table 5-3）未将 VBUS/VBAT/VCC 引出到封装引脚（pin19/21/22 = PVDD/VDDIOA/NC），故 3.3V QFN68 版本按引脚表布线、无需连接充电电路；**原理图布线以引脚表（封装管脚定义）为准**。
- 3.3V 系列对外 3.3V 输出（150mA×2）的对应引脚号待确认。
