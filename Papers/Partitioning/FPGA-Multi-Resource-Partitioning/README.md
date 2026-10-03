# FPGA 多资源划分

## 原论文

**Multi-Resource Aware Partitioning Algorithms for FPGAs with Heterogeneous Resources**  
Navaratnasothie Selvakkumaran, Abhishek Ranjan, Salil Raje, George Karypis.

[原论文 PDF（6 页）](Paper.pdf) · [Notion 条目](https://app.notion.com/p/3e7106e3498e8113bcd8c1248578139a)

当前 PDF 未明确列出出版年份和会议，待核实后补充。

## 研究问题与方法

异构 FPGA 的划分需要同时平衡不同资源，防止某个分区的特定资源超出容量。论文讨论直接生成多资源均衡划分的 native 方法，以及修正单约束划分的 enforcement 方法，并结合多约束 V-cycle 改进解的质量。

## 阅读顺序

先学习 [hMETIS 及六份笔记](../hMETIS/README.md)，再阅读本文的问题定义、多资源算法及实验对比。目前此目录只有原论文，尚无独立学习笔记。

[返回仓库首页](../../../README.md)
