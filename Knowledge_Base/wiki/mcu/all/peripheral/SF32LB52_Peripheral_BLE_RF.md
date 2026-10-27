---
title: SF32LB52 外设-BLE/RF
type: mcu_periph
aliases: ["SF32LB52X BLE","SF32LB52X Wireless","SF32LB52X RF"]
tags: ["企业MCU","外设模块-BLE/RF","芯片系列-SF32LB52","原理图审图/故障分析/报告输出"]
sources: [[SF32LB52x_Datasheet_V0.2.6],[SF32LB52X_UserManual_V0.8.8],[SF32LB52X_Datasheet_V2.5.5]]
mcu_family: ["SF32LB52"]
mcu_model: ["SF32LB52X家族"]
hardware_version: ["QFN68L"]
series_applicability: ["通用-两系列共用"]
created: 2026-08-10
updated: 2026-08-11
---

## 摘要

> **适用系列**：本外设为 SF32LB52X（电池供电）与 SF32LB52x（3.3V 供电）两系列**共用**；两系列外设逻辑一致，差异仅在电源架构与电源专用引脚（见 [[SF32LB52_Peripheral_Power]]、[[SF32LB52_Peripheral_GPIO]]）。
SF32LB52X 集成双模 BT5.3（BLE/BR/EDR）收发器，片上已集成 Balun 与天线匹配网络，**无需片外匹配**；无线接口为 BRF_ANT（引脚 53）。本页整理 RF 电源、天线接口与谐波抑制相关电路约束。

## 核心硬件内容
### 1. 工作机制
- 双模 BT5.3：支持 1M/2M PHY、BR、EDR2/EDR3；BLE 灵敏度 ‑100dBm(1Mbps)；最大 Tx 19dBm(BR/BLE)/13dBm(EDR)。
- 片内集成 AGC、RSSI、自动频偏校正；集成 Balun 与天线匹配网络。

### 2. 标准电路要求
- **RF 电源 AVDD_BRF（引脚 52）**：2.97~3.63V，须独立滤波去耦（RF 敏感）。
- **天线接口 BRF_ANT（引脚 53，A,I/O）**：直接接天线（含必要 ESD/匹配）；片上已集成 Balun 与匹配，通常无需片外匹配网络。
- 二次/三次谐波抑制：在 +19dBm 发射功率下，二次谐波 ‑50dBm、三次 ‑40dBm（带外部 π 型匹配网络时）。

### 3. 约束禁忌
- BRF_ANT 禁止额外串入不匹配的无源网络导致失配/反射超标。
- RF 输入（VLNA）绝对最大 0dBm，避免强干扰注入。
- AVDD_BRF 必须与数字电源隔离滤波，否则灵敏度劣化。

### 4. 规范依据
- Datasheet §3.1 Dual-mode Bluetooth 5.3（P12）、§4.3 Bluetooth RF（P32–P35）、Table 4-8~4-16 RF 特性、Table 5-3（BRF_ANT 53 / AVDD_BRF 52，P47）

## 用户手册 V0.8.8 补充（蓝牙共存接口）
来源：[[SF32LB52X_UserManual_V0.8.8]] §16（P364–P368）。

- 蓝牙支持 v5.3（兼容 4.2/4.1/4.0）；BLE 最大 Tx 19dBm；BR 19dBm、EDR2/3 13dBm。
- **共存接口 4 线**：BT_ACTIVE、BT_PRIORITY、BT_COLLISION（输出）+ WLAN_ACTIVE（输入），可兼容单/2/3/4 线方案，支持外部或内部仲裁。
- **天线共用**：蓝牙与 WIFI 可共用天线，经射频开关切换，由 BT_ACTIVE/BT_PRIORITY 控制或 WIFI 经 WLAN_ACTIVE 屏蔽低优先级收发。
- 最大连接数：单 BLE 场景锂电版(523/525/527)最大 4 条、常规版(52A/52B/52D)最大 8 条；单经典 BT 场景锂电版 2 条、常规版 7 条。
- IO 映射：共存信号可映射到任意 PA（输出仅高有效，HPSYS 可 deepsleep 不可 standby/hibernate），或限定 PA00~PA03（极性可配，可 deepsleep/standby 不可 hibernate）。映射需先设 PA_TIM(FSEL=5) 再在 HPSYS_CFG 指定。

> 天线匹配/π 网络具体值仍待核实。

## V2.5.5 版本补充（DS5201-SF32LB52x-EN V2.5.5）
来源：[[SF32LB52x_Datasheet_V2.5.5]]。
- 本外设 RF 特性（BLE/经典蓝牙灵敏度、Tx 功率、谐波抑制、片上 Balun、共存接口 4 线）在 V2.5.5 中**无新增/变更**，与 V0.2.6 / UM V0.8.8 一致；已将本规格书登记为来源引用。
- 跨版本命名体系差异、VBAT 范围等事项见 [[SF32LB52x_batt|SF32LB52x]] 待核实 #2 与 [[SF32LB52x_Datasheet_V2.5.5]]。

## 关联页面
- 芯片实体：[[SF32LB52x_batt|SF32LB52x]]
- 电源：[[SF32LB52_Peripheral_Power]]
- 校验规则：[[CR_BLE_RF_Antenna]]、[[CR_AbsMaxRatings]]、[[CR_PowerDomains]]

## 原始来源完整引用
1. [DS5202-SF32LB52X-Datasheet V0p2p6.pdf]，Raw：raw/mcu/all_chip/datasheets/，§3.1（P12）、§4.3（P32–P35）、Table 5-3（P47）

## 待核实问题
- BRF_ANT 推荐天线匹配/π 网络具体值（谐波达标前提下）待补参考设计。
