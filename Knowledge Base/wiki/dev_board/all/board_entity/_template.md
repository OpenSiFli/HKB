---
title: 
type: dev_board
aliases: 
tags: ["开发板","板卡系列-XX","型号-XX","板卡实体","原理图审图/故障分析/报告输出"]
sources: [[对应raw原理图/指南双链]]
board_model: [] # 开发板型号
hardware_version: [] # 硬件版本
platform_family: [] # 平台：使用的MCU系列，如 SF32LB52X
chip_model: [] # 芯片具体型号
module_model: [] # 模组具体型号
mounting_type: [] # 上芯方式：芯片直贴 / 模组
storage_config: [] # 存储配置
power_supply: [] # 供电方式
peripherals: [] # 外设
debug_interface: [] # 调试接口
use_cases: [] # 适用场景
guide_doc: [[使用指南文档raw双链]]
drawings: [[图纸raw双链: 原理图/PCB/BOM/GPIO分配表]]
created: {{当前日期}}
updated: {{当前日期}}
---

## 摘要
一句话概括本开发板定位：平台 + 芯片/模组 + 上芯方式 + 核心资源，标注业务场景。

## 一、平台（使用的 MCU 系列）
- 平台系列：[[wiki/mcu/all/chip_entity/对应MCU系列页面]]
- 说明：本开发板基于哪一 MCU 系列设计，决定可复用的外设规范与校验规则。

## 二、芯片（具体型号）
- 芯片型号：[[wiki/mcu/all/chip_entity/具体芯片页面]]
- 关键参数（封装/主频/存储，摘自芯片实体页，不在此重复展开，以双链引用为准）。

## 三、模组（具体型号）
- 模组型号：（如采用模组方式则填写；芯片直贴方式填「无 / 不适用」）
- 模组关键参数与接口约束。

## 四、上芯方式
- 方式：芯片直贴 / 模组
- 说明：板载是裸芯片还是模组；影响最小系统、散热、调试接口形态。

## 五、存储配置
- 板载 Flash / RAM：
- 扩展存储接口：QSPI NOR / SPI NAND / SDRAM / eMMC / TF 卡 等（对应引脚与电源/去耦，详见图纸提取页）。

## 六、供电方式
- 输入电压范围：
- 板载电源树：BUCK/LDO、各电源域、去耦（详见图纸提取页与 MCU 电源规范）。
- 上电/掉电时序要点。

## 七、外设
- 板载外设与扩展接口：GPIO/UART/SPI/I2C/CAN/USB/ADC/PWM/音频/无线 等。
- 每项外设详细电路与约束见 [[wiki/mcu/all/peripheral/对应外设页面]]（开发板仅作参考演示，量产以企业硬件设计指南为准）。

## 八、调试接口
- 调试方式：SWD / UART 等，引脚、测试点、上拉（详见图纸提取页与 [[wiki/mcu/all/design_rules/DR_Debug_Interface]]）。

## 九、适用场景
- 评估 / 研发调试 / 量产参考 / 教学 等场景描述。

## 十、使用指南文档
- 指南文档：[[对应raw指南路径]]（如适用）。
- 定位：实物配套实操文档，优先级低于企业硬件设计指南、芯片 datasheet/用户手册。

## 十一、图纸（原理图 / PCB / BOM / GPIO 分配表）
- 原理图：[[对应raw原理图路径]] → 提取页 [[wiki/dev_board/all/schematics/对应图纸页]]
- PCB：[[对应raw PCB路径]]
- BOM：[[对应raw BOM路径]]
- GPIO 分配表：[[对应raw GPIO路径]]
- 图纸提取要点见「图纸提取页」，含电源树/复位/时钟/BOOT/调试/存储/外设的关键位号、参数、网络。

## 关联页面
- 来源摘要：[[wiki/dev_board/all/sources/...]]
- 图纸提取：[[wiki/dev_board/all/schematics/...]]
- 平台/芯片：[[wiki/mcu/all/chip_entity/...]]
- 外设规范：[[wiki/mcu/all/peripheral/...]]
- 校验规则（审图复用）：[[wiki/mcu/all/check_rules/...]]

## 原始来源完整引用
1. [开发板原理图]，Raw 存储路径：raw/dev_board/schematics/...，图号：xxx

## 待核实问题
无 / 待确认型号、参数冲突、测试补充需求
