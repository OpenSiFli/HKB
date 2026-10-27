---
title: 
type: dev_board_sch
aliases: 
tags: ["开发板","原理图","PCB","BOM","GPIO分配表","图纸提取"]
sources: [[对应raw原理图/PCB/BOM/GPIO双链]]
board_model: [] # 开发板型号
hardware_version: [] # 硬件版本
created: {{当前日期}}
updated: {{当前日期}}
---

## 摘要
本页为开发板图纸（原理图为主，辅以 PCB/BOM/GPIO 分配表）的结构化提取结果，是填写板卡实体 11 项参数的事实依据。所有数据标注原理图页码/坐标/图号，禁止编造。

## 一、图纸清单
- 原理图：[[对应raw原理图路径]]（图号/页数）
- PCB：[[对应raw PCB路径]]
- BOM：[[对应raw BOM路径]]
- GPIO 分配表：[[对应raw GPIO路径]]

## 二、关键电路提取（依据原理图 EDA 矢量文本/坐标）
- 电源树（BUCK/LDO/各电源域/去耦）位号/参数/网络：
- 复位电路（POR/BOR/nRST 外接）位号/参数：
- 时钟/晶振（48M 主晶振 + 32.768k RTC + 负载电容）位号/参数：
- 外置存储（QSPI/SPI/SDRAM/eMMC 接口与电平/去耦，MPI/SDMMC 互斥）：
- BOOT 配置（strapping 电阻/跳线/电平）：
- 下载调试接口（SWD/UART 引脚、测试点、上拉）：
- 去耦/滤波/ESD 防护：

## 三、引脚与 GPIO 分配（依据 GPIO 分配表 / 原理图）
| 功能 | 引脚 | 网络 | 备注 |
|---|---|---|---|
| ... | ... | ... | ... |

## 四、物料清单要点（依据 BOM）
- 关键器件（MCU/电源芯片/晶振/存储器/连接器的型号与供应商），关联 AVL：`raw/mcu/vendor/device_spec/`

## 五、关联页面
- 开发板实体：[[wiki/dev_board/all/board_entity/对应板卡页面]]
- 来源页：[[wiki/dev_board/all/sources/...]]
- 平台/芯片：[[wiki/mcu/all/chip_entity/...]]

## 六、待核实问题
无 / 图纸模糊、缺少量化指标处统一标记「待人工核实」，禁止编造。
