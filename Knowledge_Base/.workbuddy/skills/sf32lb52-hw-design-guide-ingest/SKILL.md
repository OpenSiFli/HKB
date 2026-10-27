---
name: sf32lb52-hw-design-guide-ingest
agent_created: true
description: 在 D:\obsidian\硬件知识库 中导入或修复 SiFli SF32LB52 家族官方硬件设计指南（SiFli Wiki）。处理 3.3V 系列（SF32LB52X）与电池系列（SF32LB52x）的目录分类、NTFS 大小写冲突、HTML/PDF 备份、markdown Wiki 生成与双链更新。
---

# SF32LB52 家族硬件设计指南入库技能

## 触发场景
- 用户要从 SiFli Wiki 导入 SF32LB52 家族硬件设计指南；
- 用户反馈硬件设计指南只有一份、元数据错误、X/x 系列被覆盖；
- 需要把旧的 `hw_application` 分类/目录迁移为 `hardware_design_guide`。

## 核心事实与命名约定
1. **分类/目录名**：统一用 **`hardware_design_guide`**（数据库 `doc_type` 同样为 `hardware_design_guide`）。旧名 `hw_application` 已弃用。
2. **NTFS 大小写陷阱**：同目录下 `SF32LB52X_*` 与 `SF32LB52x_*` 会被 Windows 视为同一文件。必须通过后缀区分：
   - 3.3V 系列：纯名 **`SF32LB52X_Hardware_Design_Guide.md`**
   - 电池系列：必须加后缀 **`SF32LB52x_batt_Hardware_Design_Guide.md`**，引用用 `[[SF32LB52x_batt_Hardware_Design_Guide|SF32LB52x 硬件设计指南]]`
3. **源文件备份位置**：`raw/mcu/all_chip/hw_design/`
   - 3.3V 源 HTML：`SF32LB52X_3V3_HW_Application.html`
   - 电池源 HTML：`SF32LB52x_batt_HW_Application.html`
   - 1:1 PDF 与图片已去重后存于同目录 `images/`。
4. **图片引用格式**：`![[raw/mcu/all_chip/hw_design/images/<basename>]]`。

## 执行流程
1. **确认源文件已存在**：`raw/mcu/all_chip/hw_design/` 下应有对应 HTML、PDF、`images/`（如缺失，先用 URL-to-PDF 技能下载并生成 1:1 PDF + HTML 备份）。
2. **创建目标目录**：`wiki/mcu/all/hardware_design_guide/`。
3. **生成 markdown**：
   - 使用脚本 `C:\Users\Jingming\.workbuddy\tmp\convert_hw_html_to_md.py`：
     ```bash
     python convert_hw_html_to_md.py \
       raw/mcu/all_chip/hw_design/SF32LB52X_3V3_HW_Application.html \
       wiki/mcu/all/hardware_design_guide/SF32LB52X_Hardware_Design_Guide.md \
       --title "SF32LB52X 硬件设计指南（3.3V 供电）" \
       --source_url "https://wiki.sifli.com/hardware/SF32LB52B-E-G-J-HW-Application.html" \
       --series "3.3V供电系列" --model "SF32LB52X" \
       --raw_html "SF32LB52X_3V3_HW_Application.html"
     ```
   - 电池页同样生成或从旧页迁移，必须确保文件名带 `_batt` 后缀。
4. **手工修正（必须）**：
   - 检查 3.3V 页是否含电池专属内容（如充电、VBAT）并删除；
   - 检查电池页是否把原 3.3V 页中 `PA21` 相关描述修正为「电池系列无 PA21」；
   - 确保电池页内所有指向 3.3V 指南的链接为 `[[SF32LB52X_Hardware_Design_Guide]]`。
5. **删除旧目录**：迁移完成后删除 `wiki/mcu/all/hw_application/`（避免 Obsidian 出现重复/冲突条目）。
6. **更新双链**：
   - `index_MCU_ALL.md`：硬件设计指南入口改为 `hardware_design_guide` 与新的两个文件名。
   - `chip_entity/SF32LB52X.md`：3.3V 指南链接改为 `[[SF32LB52X_Hardware_Design_Guide]]`。
   - `chip_entity/SF32LB52x_batt.md`：电池指南链接改为 `[[SF32LB52x_batt_Hardware_Design_Guide]]`。
7. **追加日志**：在 `log_MCU_ALL.md` 追加变更记录；在 `.workbuddy/memory/YYYY-MM-DD.md` 追加工作日志。
8. **自检**：
   - 两页 frontmatter `doc_type` 均为 `hardware_design_guide`；
   - 目录下恰好两个文件，无 `hw_application` 残留；
   - 全库无 `[[SF32LB52X_HW_Application]]` / `[[SF32LB52x_HW_Application]]` 旧链接（`log_MCU_ALL.md` 历史记录除外）；
   - 所有 `![[raw/mcu/all_chip/hw_design/images/...]]` 引用对应的 png 文件存在。

## 依赖
- Python 3 + BeautifulSoup4 + lxml（已装在默认 venv）。
- 脚本路径：`C:\Users\Jingming\.workbuddy\tmp\convert_hw_html_to_md.py`。
