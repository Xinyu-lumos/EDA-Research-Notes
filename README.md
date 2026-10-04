# EDA Research Notes

Systematic study notes for FPGA/EDA research, including placement, timing-driven placement, packing/legalization, detailed placement, routability/congestion, macro placement, timing/STA, clocking/CDC, and optimization methods.

## Papers

### Partitioning｜划分

| 论文 | 原文 | 学习笔记 |
|---|---|---|
| [hMETIS — Multilevel Hypergraph Partitioning (TVLSI 1999)](Papers/Partitioning/hMETIS/README.md) | [PDF](Papers/Partitioning/hMETIS/Paper.pdf) | 01–06，共六份 |
| [FPGA Multi-Resource Partitioning](Papers/Partitioning/FPGA-Multi-Resource-Partitioning/README.md) | [PDF](Papers/Partitioning/FPGA-Multi-Resource-Partitioning/Paper.pdf) | 待补充 |

### Macro Placement｜宏布局

- [AMF-Placer (ICCAD 2021)](Papers/Macro-Placement/AMF-Placer_ICCAD2021/README.md)
- [Routability-Driven Macro Placement Engine (TCAD 2025)](Papers/Macro-Placement/FPGA-Routability-Driven-Macro-Placement/README.md) — [原文 PDF](Papers/Macro-Placement/FPGA-Routability-Driven-Macro-Placement/Paper.pdf)，作者接受稿。

## Projects｜项目与代码

- [PACT 项目学习笔记](Projects/PACT/README.md) — Day1–Day7，共 7 份 HTML 笔记，覆盖工具后端、证据与决策、优化技能、候选搜索、算子改写和提交验证。

## 归档约定

每篇论文采用 `Papers/<Topic>/<Paper>/` 目录，包含 `README.md`、原文 `Paper.pdf` 和已有的编号学习笔记。主题目录使用英文，README 提供中文导航。PDF 保留原始内容，论文元信息以原文为依据。

> PDF notes are generated from LaTeX and archived in GitHub for versioned study/review. Original papers retain their respective copyright notices.
