---
title: SF32LB57 蓝牙射频（BT/BLE 6.3）
type: mcu_peripheral
aliases: ["SF32LB57_Peripheral_BLE_RF","SF32LB57 BLE","SF32LB57 射频","SF32LB57 BT"]
tags: ["企业MCU","外设-无线/射频","芯片系列-SF32LB57","原理图审图/故障分析/报告输出"]
sources: [[SF32LB57X_Datasheet_V0.2_20260909],[SF32LB57x_batt_Datasheet_V0.2_20260909]]
mcu_family: ["SF32LB57"]
series_applicability: ["通用-两系列共用"]
mcu_model: ["SF32LB57X","SF32LB57x"]
hardware_version: ["QFN68 7x7","QFN80 8x8","BGA112 5.4x4.4","Datasheet V0.2"]
created: 2026-09-09
updated: 2026-09-09
---

## 摘要
SF32LB57 集成**双模蓝牙 6.3** 收发机（支持 BLE Audio、LE LR）。**两系列射频前端一致**，但**射频电源 AVDD_BRF 的供电源不同**：3.3V 系列接 3.3V，电池系列接 VSYS。

## 1. 主要特性
- 双模蓝牙 **6.3**，支持 **BLE Audio**、**LE LR**
- 灵敏度：**‑100 dBm（BLE / 1Mbps）**、**‑107.5 dBm（BLE / 125Kbps，S8）**、‑96 dBm（BR）、‑95 dBm（EDR2）
- 最大发射功率：**17 dBm（BR / BLE）**、**13 dBm（EDR2/3）**
- 接收机峰值功耗（BR）：**2.0 mA @3.8V**
- 频率范围：2402 ~ 2480 MHz

## 2. 射频引脚（两系列一致，QFN68）
| 引脚 | 名称 | 类型 | 说明 |
|---|---|---|---|
| 53 | BRF_ANT | A,I/O | 天线接口（片上集成 Balun） |
| 52 | AVDD_BRF | PWR | 射频电源输入 —— **3.3V 系列接 3.3V；电池系列接 VSYS** |

**QFN80（3.3V 系列）**：BRF_ANT = 42、AVDD_BRF = 41。

> ⚠️ QFN80 表（Table 5-4）中 AVDD_BRF 描述残留「电池供电时和 VSYS 接一起；常规 3.3V 供电时接 3.3V 电源」——为共用模板痕迹；**3.3V 系列常规供电时应接 3.3V**。

## 3. 关键射频指标
**BLE 发射（Table 4-7，1Mbps）**：最大发射功率 17 dBm；功率控制范围 ‑20 dBm；Δf1avg 225/250/275 kHz；Δf2max 185/205 kHz；Δf2avg/Δf1avg 0.8/0.85；ICFT ±150 kHz（typ 20）；Drift rate ±20 kHz/50µs；Drift ±50 kHz；二次谐波 ‑50 dBm；三次谐波 ‑40 dBm（* 基于外部 π 型匹配网络）。
**BLE 发射（Table 4-8，2Mbps）**：最大 17 dBm；Δf1avg 450/500/550 kHz；Δf2max 370/420 kHz。
**BLE 接收（Table 4-9~4-12）**：
| 模式 | 灵敏度（dirty TX off） | 灵敏度（dirty TX on） | 最大接收 |
|---|---|---|---|
| 1 Mbps | ‑100 dBm | ‑99 dBm | 0 dBm |
| 2 Mbps | ‑97 dBm | ‑96 dBm | 0 dBm |
| S2 | ‑104 dBm | ‑103.5 dBm | 0 dBm |
| S8 | ‑107.5 dBm | ‑107 dBm | 0 dBm |
**经典蓝牙**：BR 发射最大 17 dBm（Table 4-13）；EDR 发射最大 **13 dBm**（Table 4-14）；BR 接收灵敏度 ‑96 dBm（Table 4-15）；π/4-DQPSK 接收 ‑95 dBm（Table 4-16）；8DPSK 接收 ‑88.5 dBm（Table 4-17）。

## 4. 硬件设计约束
- **BRF_ANT(53)**：片上集成 Balun 与天线匹配，**通常无需片外匹配网络**；但规格书射频指标均基于**外部 π 型匹配网络**测得（表注 *），量产设计应按官方参考设计保留 π 型匹配位。
- **AVDD_BRF(52) 供电源按系列区分**：3.3V 系列接 3.3V；**电池系列必须接 VSYS**（接 3.3V 与电池架构不符）。
- 天线走线须做 50Ω 阻抗控制，远离 BUCK_LX、晶体、高速数字线；天线下方及各层做净空处理。
- ⚠️ **BT/BLE 功耗（Table 4-6）全部为 TBD**，无法核算无线功耗预算，量产前须向原厂确认。

## 关联页面
- 家族：[[SF32LB57]]｜3.3V：[[SF32LB57X]]｜电池：[[SF32LB57x_batt|SF32LB57x]]
- 电源：[[SF32LB57_Peripheral_Power]]｜时钟：[[SF32LB57_Peripheral_Clock]]
- 来源：[[SF32LB57X_Datasheet_V0.2_20260909]]、[[SF32LB57x_batt_Datasheet_V0.2_20260909]]

## 原始来源完整引用
1. [DS5702-SF32LB57X V0.2]，产品特性无线段（P4）、Table 4-6（P41）、Table 4-7~4-12（P41–44）、Table 4-13~4-17（P45–47）、Table 5-3（P61）、Table 5-4（P62）。
2. [DS5701-SF32LB57x V0.2]，同上（P4 / P42–48 / P62）。

## 待核实问题
1. **BT/BLE 功耗全部 TBD**（Table 4-6）。
2. 天线匹配网络的具体元件值与布局（官方参考设计）本册未给出，待补。
3. RF 输出功率与温度的降额关系未给出。
