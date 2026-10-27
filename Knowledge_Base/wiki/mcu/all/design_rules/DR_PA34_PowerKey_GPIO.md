---
title: DR-PA34电源键引脚作普通GPIO使用规范(SF32LB52/57)
type: mcu_design_rule
aliases: ["DR_PA34_PowerKey_GPIO","PA34作GPIO","PWRKEY关闭","PA34电源键复用"]
tags: ["企业MCU","通用设计规范","GPIO/电源键","原理图审图/故障分析/报告输出"]
sources: [[SF32LB52X_UserManual_V0.8.8],[SF32LB57X_Datasheet_V0.2_20260909],[SF32LB57x_batt_Datasheet_V0.2_20260909]]
mcu_family: ["SF32LB52","SF32LB57"]
series_applicability: ["通用-两系列共用"]
mcu_model: ["SF32LB52X家族","SF32LB57X家族"]
hardware_version: ["QFN68L/V0.8.8","QFN68/QFN80/BGA112 V0.2"]
risk_level: 一般
created: 2026-10-27
updated: 2026-10-27
---

## 摘要
说明 SF32LB52 / SF32LB57 两家族 **PA34（电源键 / PWRKEY 引脚）在需要当作普通 GPIO 使用时的处理路径**：
- 52 系列 **不可关闭** PWRKEY 功能，只能把长按复位阈值配到最大并约束高电平保持时长；
- 57 系列可经 **PMUC WER.PWRKEY = 0** **彻底关闭** PWRKEY 功能后自由作 GPIO。

## 核心硬件内容
### 1. PA34 默认硬件功能
- PA34 在 52 / 57 两家族均为 **电源键（PWRKEY）引脚**，复用名 `(PWR_KEY)` / `PWRKEY`。
- 长按（持续）高电平会触发芯片复位（除 RTC / IWDT 外模块复位）；同时 PA34 亦复用为 GPIO_A34 / GPADC_CH6 / WKUP_PIN。

### 2. SF32LB52 系列：PWRKEY 不可关闭，靠 PWRKEY_CNT 规避
- **无法关闭 PWRKEY 功能**（纯硬件行为，无禁用位）。
- 可通过 **PWRKEY_CNT 寄存器**配置长按复位阈值；**写入最大值**时，需约 **100 多秒**持续高电平才会触发芯片复位（默认阈值约 10s）。
- 使用约束（复用为 GPIO 时）：
  - PA34 默认（常态）为 **低电平**；
  - **高电平保持时间不要超过 50s** 即保险不会触发复位（远低于 ~100s 阈值，留足余量）。
- 设计要点：外部电路须保证 PA34 常态被可靠下拉到地，仅在需要时短暂拉高；若外部驱动可能长期拉高，须软件配合确保脉冲 < 50s。

### 3. SF32LB57 系列：PWRKEY 可关闭（PMUC WER.PWRKEY = 0）
- PA34 的 PWRKEY（电源键）功能 **可以关闭**：在 **PMUC 的 WER 寄存器**中有 **PWRKEY 字段**，将该字段 **置 0** 即关闭芯片复位 / 开关机功能。
- 关闭后 PA34 **可完全当作普通 GPIO 使用，无任何高电平保持时长限制**。
- 设计要点：固件初始化阶段将 `WER.PWRKEY` 置 0 即可释放该引脚；如需保留开机键功能则保持默认。

### 4. 两家族差异速查
| 项目 | SF32LB52 | SF32LB57 |
|---|---|---|
| PWRKEY 能否关闭 | 否 | 是（PMUC WER.PWRKEY = 0） |
| 规避 / 释放方式 | PWRKEY_CNT 设最大值（~100+s 阈值） | 关闭功能后无限制 |
| GPIO 高电平约束 | 保持 < 50s 保险 | 无限制 |
| 常态电平 | 低电平（可靠下拉） | 关闭功能后按 GPIO 配置 |
| 复用名 | `(PWR_KEY)` | PWRKEY（纯硬件功能，关闭前长按高仍触发复位） |

## 约束禁忌
- 52 系列：PA34 严禁永久上拉到高（无按键即持续高），否则即便配了最大 PWRKEY_CNT 仍会在 ~100s 后复位；常态必须可靠下拉。
- 57 系列：未将 `WER.PWRKEY` 置 0 前，PA34 长按高电平仍会触发复位；当作 GPIO 前务必先关闭 PWRKEY 功能。

## 规范依据
- [[SF32LB52X_UserManual_V0.8.8]] §2.2（P20–P22，PWRKEY 复位源、PWRKEY_CNT 配置）
- [[SF32LB57X_Datasheet_V0.2_20260909]] / [[SF32LB57x_batt_Datasheet_V0.2_20260909]]（PMUC WER 寄存器，PWRKEY 字段）
- 设计经验（2026-10-27）：52 PWRKEY_CNT 最大值约 100+s、常态低 / < 50s；57 PMUC WER.PWRKEY = 0 关闭

## 关联页面
- 复位设计：[[DR_Reset_Design]]｜PWRKEY 审图规则：[[CR_Reset_PWRKEY]]
- 52 GPIO：[[SF32LB52_Peripheral_GPIO]]｜57 GPIO：[[SF32LB57_Peripheral_GPIO]]
- 52 复用：[[SF32LB52_Pinmux]]｜57 复用：[[SF32LB57_Pinmux]]

## 原始来源完整引用
1. [UM5201‐SF32LB52x‐CN.pdf]，Raw：raw/mcu/all_chip/datasheets/UM5201‐SF32LB52x‐CN.pdf，§2.2（P20–P22，PWRKEY 复位源、PWRKEY_CNT）
2. [DS5702-SF32LB57X V0.2] / [DS5701-SF32LB57x V0.2]，PMUC WER 寄存器（PWRKEY 字段），见 [[SF32LB57X_Datasheet_V0.2_20260909]] / [[SF32LB57x_batt_Datasheet_V0.2_20260909]]

## 待核实问题
- 52 的 PWRKEY_CNT 寄存器最大值对应的精确秒数（用户估 ~100+s，待用户手册寄存器定义确认）。
- 57 的 PMUC WER.PWRKEY 字段位号、关闭后 PA34 默认电平（待用户手册确认）。
