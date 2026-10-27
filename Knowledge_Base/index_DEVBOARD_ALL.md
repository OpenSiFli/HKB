---
title: index_DEVBOARD_ALL
type: index
aliases: ["开发板硬件知识库导航","开发板全局索引"]
tags: ["开发板","全局导航","索引"]
created: 2026-08-12
updated: 2026-08-12
---

# 企业开发板（Dev Board）硬件知识库 —— 全局导航索引

> 开发板与企业全系列 MCU 硬件知识库**平级**，是独立的一大类。本库以**原理图（Schematic）为主要入库依据**，提取开发板 11 项核心参数（平台 / 芯片 / 模组 / 上芯方式 / 存储配置 / 供电方式 / 外设 / 调试接口 / 适用场景 / 使用指南文档 / 图纸），并与 MCU 知识库双向双链。
> 所有页面均以 Obsidian 双链互相关联。

---

## 一、Schema 规则层（运维入口）
- [[log_DEVBOARD_ALL]] —— 变更日志（仅追加）
- 本页 —— 全局导航索引
- 入库指令：`cmd/新增开发板入库指令.md`（首次建板）、`cmd/更新开发板入库指令.md`（迭代新版）
- 原始资料区：`raw/dev_board/`（README 说明命名与目录约定）

### 入库流程快捷入口
- 新增开发板：将原理图等资料放入 `raw/dev_board/schematics/`（PCB/BOM/GPIO/指南对应子目录）→ 按 `cmd/新增开发板入库指令.md` 执行：EDA 原理图提取 → 建 sources 来源页 → 建 board_entity 实体页（11 参数）→ 建 schematics 图纸提取页 → 更新本导航与 log → 双链校验。

---

## 二、按板型 / 平台检索
- 板卡实体库：`wiki/dev_board/all/board_entity/`
  - 每一款开发板独立页面，收录 11 项核心参数与图纸引用。
- 来源摘要库：`wiki/dev_board/all/sources/`
- 图纸提取库：`wiki/dev_board/all/schematics/`（原理图/PCB/BOM/GPIO 结构化提取）

### 已入库开发板（待首次建板后在此登记）
- （暂无，待执行 `cmd/新增开发板入库指令.md` 后填充）

---

## 三、与 MCU 知识库的关系
- 开发板的「平台 / 芯片 / 模组」通过双链指向 `wiki/mcu/all/chip_entity/` 对应 MCU 页面；
- 外设约束、校验规则（原理图审图）复用 `wiki/mcu/all/peripheral/`、`wiki/mcu/all/check_rules/`；
- 开发板侧**不修改** MCU 侧任何文件，仅作单向引用。
