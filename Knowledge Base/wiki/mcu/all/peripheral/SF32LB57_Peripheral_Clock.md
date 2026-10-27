---
title: SF32LB57 时钟系统
type: mcu_peripheral
aliases: ["SF32LB57_Peripheral_Clock","SF32LB57时钟","SF32LB57 晶振"]
tags: ["企业MCU","外设-时钟","芯片系列-SF32LB57","原理图审图/故障分析/报告输出"]
sources: [[SF32LB57X_Datasheet_V0.2_20260909],[SF32LB57x_batt_Datasheet_V0.2_20260909]]
mcu_family: ["SF32LB57"]
series_applicability: ["通用-两系列共用"]
mcu_model: ["SF32LB57X","SF32LB57x"]
hardware_version: ["QFN68 7x7","QFN80 8x8","BGA112 5.4x4.4","Datasheet V0.2"]
created: 2026-09-09
updated: 2026-09-09
---

## 摘要
SF32LB57 家族时钟系统：主时钟由片内 **48MHz 晶体**（XTAL48M_XI/XO）提供，HPSYS 双性能核最高 **240MHz**、LPSYS 能效核最高 **24MHz**，支持动态频率调节。**两系列时钟架构与引脚一致**。

## 1. 时钟资源
- **HPSYS（高性能系统，双性能核）**：双 Arm Cortex-M33 STAR-MC1，**最高 240MHz**，支持动态频率功耗调节，功耗效率 **23µA/MHz @3.8V**
- **LPSYS（低功耗系统，能效核）**：Arm Cortex-M33 STAR-MC1，**最高 24MHz**（可作 SensorHub）
- **主时钟源**：片内 48MHz 晶体振荡器（**XTAL48M_XI / XTAL48M_XO**）
- 音频 PLL（AUDPRC PLL）
- 各外设时钟由系统时钟派生

## 2. 晶体接口引脚（两系列一致）
| 引脚（QFN68） | 名称 | 类型 | 说明 |
|---|---|---|---|
| 55 | XTAL48M_XI | A,I | 48MHz 晶体接口（输入） |
| 54 | XTAL48M_XO | A,O | 48MHz 晶体接口（输出） |

**QFN80（3.3V 系列）**：XTAL48M_XI = 44、XTAL48M_XO = 43。

## 3. 硬件设计约束
- 48MHz 晶体**紧靠芯片**放置，走线短且包地处理。
- **严禁**在 XTAL48M_XI/XO 施加外部驱动源。
- ⚠️ **晶体负载电容判读（重要，AI 审图必读）**：
  - **SiFli 全系 MCU 通用原则** —— 当所采用晶体的规格落在芯片**推荐参数范围**内，或选用 SiFli **AVL（认可物料清单）** 内的晶体料号时，`xtal_in` / `xtal_out` 两端的**外部负载电容可以不焊接**，MCU 单独接晶体即可正常起振（片内已集成匹配/负载电容，或所选晶体为匹配型）。
  - → **严禁仅凭「XI/XO 两端未见对地负载电容」判违规**。须先确认晶体料号是否在推荐参数内 / AVL 内；若在 → 判 PASS/N/A（片内匹配）；若为**非推荐款**（规格超出推荐范围）→ 才需按晶体 CL 外配负载电容。
  - AVL 清单见 [[SIFLI_MCU_AVL_V0.4_20260812]]（适用于所有 SiFli MCU，不限于本家族）。
- 晶体下方禁止铺铜/需做避让，振荡走线与 GND 包铜间距须满足布局规范（参考 SF32LB52 家族 Checklist：间距 >1.5 倍线宽；4 层板 TOP 层避让、6 层 HDI 板 TOP 与第 2 层均避让）。

## 4. 待核实 / 缺失
- ⚠️ 本册（V0.2 草稿）**未给出 48MHz 晶体的具体选型参数**（负载电容 CL、频偏 ppm、ESR 限值）。SF32LB52 家族参考设计值为 CL 8.8pF / ±20ppm / 48M，32K 为 CL 7~12pF / ESR ≤80kΩ / ±10ppm——**不可直接套用到 57 家族**，须待官方 Checklist/参考设计补入。
- 低速 32.768kHz RTC 晶振引脚（SF32LB52 为 PA22/PA23）**本册未明确列出**，待补。
- 内部 RC 时钟精度与可用性，待补用户手册。

## 关联页面
- 家族：[[SF32LB57]]｜3.3V：[[SF32LB57X]]｜电池：[[SF32LB57x_batt|SF32LB57x]]
- 电源：[[SF32LB57_Peripheral_Power]]｜GPIO：[[SF32LB57_Peripheral_GPIO]]
- AVL：[[SIFLI_MCU_AVL_V0.4_20260812]]
- 来源：[[SF32LB57X_Datasheet_V0.2_20260909]]、[[SF32LB57x_batt_Datasheet_V0.2_20260909]]

## 原始来源完整引用
1. [DS5702-SF32LB57X V0.2]，Table 5-3（P61，XTAL48M_XI/XO=55/54）、Table 5-4（P62，QFN80=44/43）；产品特性 CPU 主频（P4）。
2. [DS5701-SF32LB57x V0.2]，Table 5-3（P62，XTAL48M_XI/XO=55/54）。
