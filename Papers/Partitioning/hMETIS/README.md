# hMETIS：多层超图划分

## 原论文

**Multilevel Hypergraph Partitioning: Applications in VLSI Domain**  
George Karypis, Rajat Aggarwal, Vipin Kumar, Shashi Shekhar.  
IEEE Transactions on Very Large Scale Integration (VLSI) Systems, 7(1), 69–79, March 1999.

[原论文 PDF](Paper.pdf) · [Notion 学习条目](https://app.notion.com/p/3e7106e3498e81f295a2e00dafebbf6a)

在均衡约束下最小化被切超边，采用粗化、最粗层初始划分、反粗化与细化的多层框架。重点学习 EC/HEC/MHEC、FM/FM-EE/HER 和受限粗化。

## 六份学习笔记

建议按 01–06 顺序阅读；PDF 保留原始内容。

| 顺序 | 学习笔记 | 页数 |
|---|---|---|
| 01 | [hMETIS论文总览](01_hMETIS论文总览.pdf) | 10 |
| 02 | [粗化算法与初始划分](02_粗化算法与初始划分.pdf) | 14 |
| 03 | [反粗化与细化](03_反粗化与细化.pdf) | 9 |
| 04 | [受限粗化与多阶段细化](04_受限粗化与多阶段细化.pdf) | 10 |
| 05 | [实验结果与论文结论](05_实验结果与论文结论.pdf) | 9 |
| 06 | [全景复盘与复现路线](06_全景复盘与复现路线.pdf) | 10 |

## 延伸阅读

- [FPGA 多资源划分](../FPGA-Multi-Resource-Partitioning/README.md)：从单一均衡约束扩展到异构资源约束。
- [返回仓库首页](../../../README.md)
