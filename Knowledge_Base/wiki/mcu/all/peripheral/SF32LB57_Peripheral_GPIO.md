---
title: SF32LB57 GPIO 与 IO 特性
type: mcu_peripheral
aliases: ["SF32LB57_Peripheral_GPIO","SF32LB57 GPIO","SF32LB57 IO特性"]
tags: ["企业MCU","外设-GPIO","芯片系列-SF32LB57","原理图审图/故障分析/报告输出"]
sources: [[SF32LB57X_Datasheet_V0.2_20260909],[SF32LB57x_batt_Datasheet_V0.2_20260909]]
mcu_family: ["SF32LB57"]
series_applicability: ["通用-两系列共用"]
mcu_model: ["SF32LB57X","SF32LB57x"]
hardware_version: ["QFN68 7x7","QFN80 8x8","BGA112 5.4x4.4","Datasheet V0.2"]
created: 2026-09-09
updated: 2026-09-09
---

## 摘要
SF32LB57 家族 GPIO 与 IO 电气特性。**两系列 IO 电气特性完全相同**，差异仅在：3.3V 系列有独立 **VDDIOA** 外部引脚供 GPIO 域；电池系列**无独立 VDDIOA 引脚**（IO 域由内部供给），且 **pin24 被 VCC 占用**故 GPIO 数比 3.3V 系列少 1 个。

## 1. GPIO 资源
- 大核域 GPIO：**PA**（Pinmux 见 [[SF32LB57_Pinmux]]；完整复用矩阵见规格书 Table 5-2，P52/54（3.3V）、P53/55（电池））
- 总数：**58 GPIO + 6 GPO MPI IO**（家族特性）
- 按封装（3.3V 系列）：**QFN68 = 47 GPIO**；**QFN80 = 58 GPIO**；**BGA112 = 最多 58 GPIO + 6 GPO MPI IO**
- 电池系列**订购信息（Table 6-1）仅列 QFN68 料号**，其 GPIO 数比 3.3V QFN68 少 1（pin24 被 VCC 占用，待原厂确认确切值）；DS5701 已详述 QFN80/BGA112 管脚但料号缺失（规格书【严重】缺陷）
- **FreeIO GPIO**：支持灵活配置

## 2. IO 电气特性（Table 4-3 @3.3V，两系列一致）
| 参数 | 符号 | 条件 | Min | Typ | Max | 单位 |
|---|---|---|---|---|---|---|
| 管脚电容 | CIN | | 2.5 | 3 | 3.5 | pF |
| 高电平输入电压 | VIH | | 0.7×VDD | | VDD | V |
| 低电平输入电压 | VIL | | VSS | | 0.3×VDD | V |
| 高电平输入电流 | IIH | | | 10 | 40 | nA |
| 低电平输入电流 | IIL | | | 10 | 40 | nA |
| 高电平输出电压 | VOH | 高阻负载 | 0.8×VDD | | VDD | V |
| 低电平输出电压 | VOL | 高阻负载 | VSS | | 0.2×VDD | V |
| 高电平驱动电流 | IOH | VOH=0.8×VDD，最大驱动强度 | 12 | 30 | 38 | mA |
| 低电平驱动电流 | IOL | VOH=0.2×VDD，最大驱动强度 | 12 | 30 | 38 | mA |
| 内部上拉电阻 | RPU | Vpad=0.8×VDD | 7 | 10 | 20 | kΩ |
| 内部下拉电阻 | RPD | Vpad=0.2×VDD | 7 | 10 | 20 | kΩ |
| 复位释放电压 | VIH_nRST | | 0.7×VDD | | VDD | V |
| 复位电压 | VIL_nRST | | VSS | | 0.3×VDD | V |

**驱动能力档位（Table 4-21）**
| DS1 | DS0 | 驱动能力 |
|---|---|---|
| 0 | 0 | 2 mA |
| 0 | 1 | 4 mA |
| 1 | 0 | 8 mA |
| 1 | 1 | 12 mA |

> 注：Table 4-3 的 12/30/38mA 为**最大驱动强度**下的实测（VOH=0.8×VDD 测试条件）；Table 4-21 为可配置四档。二者为同一驱动电路在不同配置/测试条件下的结果（与 SF32LB52 家族结论一致）。

## 3. 双系列 GPIO 差异
| 项目 | 3.3V 系列 SF32LB57X | 电池系列 SF32LB57x |
|---|---|---|
| GPIO 电源 | **VDDIOA(21)** 外部独立供电 | **无独立 VDDIOA 引脚**，IO 域由内部供给 |
| pin24 | GPIO（非专用脚） | **VCC**（系统电源输入，接电池）→ 少 1 个 GPIO |
| QFN68 GPIO 数 | 47 | 46（推算，待确认） |

## 4. 硬件设计约束
- 使能输入的数字 IO **不得悬空**，须配置确定电平（避免低功耗漏电升高）。
- IO 电平域须与对端器件匹配；3.3V 系列由 VDDIOA 决定，电池系列由内部电源决定。
- 驱动强度按负载选择（默认/2/4/8/12mA），大电流负载注意总功耗与压降。
- 内部上下拉典型 10kΩ（7~20kΩ），精密/低功耗场合优先外部电阻。
- **pin22（3.3V QFN68）为 NC，必须悬空**，不可作 GPIO。
- **PA34 电源键（PWRKEY）**：默认带 PWRKEY 硬件功能（长按高电平触发复位）；需当普通 GPIO 时，将 **PMUC WER.PWRKEY 置 0** 关闭该功能后无高电平时长限制（见 [[DR_PA34_PowerKey_GPIO]]）。

## 关联页面
- 家族：[[SF32LB57]]｜3.3V：[[SF32LB57X]]｜电池：[[SF32LB57x_batt|SF32LB57x]]
- 电源：[[SF32LB57_Peripheral_Power]]｜复用矩阵：[[SF32LB57_Pinmux]]
- PA34 电源键作 GPIO：[[DR_PA34_PowerKey_GPIO]]
- 来源：[[SF32LB57X_Datasheet_V0.2_20260909]]、[[SF32LB57x_batt_Datasheet_V0.2_20260909]]

## 原始来源完整引用
1. [DS5702-SF32LB57X V0.2]，Table 4-3（P39）、Table 4-21（P48）、Table 5-2（P52/54）、Table 5-3（P61）。
2. [DS5701-SF32LB57x V0.2]，Table 4-3（P40）、Table 4-21（P49）、Table 5-2（P53/55）、Table 5-3（P62）。

## 待核实问题
1. 完整 PA 复用矩阵（Table 5-2）为多页表格，本次未逐行转录，详见 [[SF32LB57_Pinmux]]（导入后）与规格书原表。
2. 电池系列 GPIO 确切数量待确认。
3. 默认上电状态（PU/PD/高阻）逐引脚表未在规格书文本中完整给出，待补用户手册/参考设计。
