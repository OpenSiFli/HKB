---
title: SF32LB57 显示与图形（ePicasso 3.0 / LCD / DCMI / eZip）
type: mcu_peripheral
aliases: ["SF32LB57_Peripheral_Display","SF32LB57显示","SF32LB57 LCD","SF32LB57 GPU","SF32LB57 ePicasso"]
tags: ["企业MCU","外设-显示/图形","芯片系列-SF32LB57","原理图审图/故障分析/报告输出"]
sources: [[SF32LB57X_Datasheet_V0.2_20260909],[SF32LB57x_batt_Datasheet_V0.2_20260909]]
mcu_family: ["SF32LB57"]
series_applicability: ["通用-两系列共用"]
mcu_model: ["SF32LB57X","SF32LB57x"]
hardware_version: ["QFN68 7x7","QFN80 8x8","BGA112 5.4x4.4","Datasheet V0.2"]
created: 2026-09-09
updated: 2026-09-09
---

## 摘要
SF32LB57 集成 **2D/2.5D ePicasso 3.0 图形引擎**、**eZip 3.0 通用压缩解码器**、**LCD 控制器**与 **DCMI 摄像头控制器**，可**不依赖 CPU 自主实现最高 60fps 全屏刷新**，支持低功耗息屏常显。**两系列一致**。

## 1. 图形引擎 ePicasso 3.0（§2.1）
- 硬件加速：**旋转、缩放、投影变换、镜像**
- 最大解析度：**2048 × 2048**
- 色彩格式：**RGB888、RGB565、aRGB8888、aRGB8565**，以及 L8/4、G8/4/2、A8/4/2、YUV
- 支持**多图层叠加**、多种 **alpha 混叠**方式
- 图层类型：普通图层 / 功能图层 / 投射图层

## 2. eZip 3.0 通用压缩解码器（§2.3）
- 无损：**eZip** 格式、**eZip-A** 动画
- 有损：**JPEG** 图片、**MJPEG** 动画
- 可与 **ePicasso 3.0 联动，无需中间缓存**

## 3. LCD 控制器（§2.2）
支持显示接口：
- **MIPI-DBI（8080）**
- **SPI / Dual-SPI / Quad-SPI**
- **MIPI-DPI（RGB / DPI）**
- **JDI**（反射屏）
- **8/16b-EPD**（电子纸）
- 最高 **60fps** 全屏刷新，不依赖 CPU；支持低功耗息屏常显

## 4. DCMI 摄像头控制器
- 支持 **DVP** 接口
- 支持 **SPI / Dual-SPI / Quad-SPI** 摄像头接口

## 5. 硬件设计约束
- LCD 并行总线（8080 / RGB）走线尽量等长、短，远离射频与 Buck 开关节点（BUCK_LX）；必要时包地。
- **Quad-SPI 显示屏**时钟较高，注意阻抗与串扰。
- EPD（电子纸）需额外高压驱动电路，按屏厂规格设计。
- 显示电源与背光驱动须独立评估，避免与 MCU 内部 LDO（150mA 限制）超载冲突。
- 摄像头 DCMI 数据线与 PCLK 须做阻抗/时序控制。
- FPC 排线（LCD）是常见 EMI 源，须按官方 Checklist 做屏蔽与接地处理（SF32LB52 家族有 `CR_RefDesign_LCD_FPC_EMI` 规则可参照，57 家族待补）。

## 关联页面
- 家族：[[SF32LB57]]｜3.3V：[[SF32LB57X]]｜电池：[[SF32LB57x_batt|SF32LB57x]]
- GPIO/复用：[[SF32LB57_Peripheral_GPIO]]、[[SF32LB57_Pinmux]]
- 存储：[[SF32LB57_Peripheral_Memory]]｜DMA/总线：见规格书 §1.3.1
- 来源：[[SF32LB57X_Datasheet_V0.2_20260909]]、[[SF32LB57x_batt_Datasheet_V0.2_20260909]]

## 原始来源完整引用
1. [DS5702-SF32LB57X V0.2]，§2.1 ePicasso（P10）、§2.2 LCD 控制器与显示接口（P10–11）、§2.3 eZip（P11）；产品特性图形段（P4）。
2. [DS5701-SF32LB57x V0.2]，同上（P10–11 / P4）。

## 待核实问题
1. LCD / DCMI 各接口对应的 GPIO 复用引脚，待补 Pinmux。
2. 显示接口速率上限、刷新率与分辨率的对应关系，待补用户手册。
3. 低功耗息屏常显（AOD）的硬件/电源要求未给出。
