# ePlace：静电场密度模型与解析布局

**ePlace: Electrostatics-Based Placement Using Fast Fourier Transform and Nesterov’s Method**  
Jingwei Lu et al. · ACM TODAES · 2015

将布局密度建模为静电系统，通过泊松方程与 FFT 谱方法计算密度力，并结合平滑线长、Nesterov 优化和步长预测完成解析全局布局。

## 完整学习笔记

[完整七天合订本（70 页）](ePlace_完整七天学习笔记.pdf) · [Notion 学习条目](https://app.notion.com/p/3a7106e3498e814d9ef2e356f3e95b1e)

中文 LaTeX 学术讲义，包含教学图解、公式推导和实验解读。建议按第 1—7 天顺序阅读；合订本带目录与书签。

2026-10-06 更新：完整笔记扩展至 70 页；第 35 页加入正、零、负散度示意图和密度偏差说明。当前阅读请优先使用完整合订本，下面的分天文件保留为早期归档。

## 分天笔记（早期归档）

| 天数 | 主题 | 页数 |
|---|---|---|
| 第 1 天 | [布局问题与静电模型直觉](ePlace_Day01_学习笔记.pdf) | 8 |
| 第 2 天 | [HPWL、WA 与 LSE 平滑线长](ePlace_Day02_学习笔记.pdf) | 8 |
| 第 3 天 | [eDensity：面积电荷与密度力](ePlace_Day03_学习笔记.pdf) | 5 |
| 第 4 天 | [泊松方程与边界条件](ePlace_Day04_学习笔记.pdf) | 5 |
| 第 5 天 | [FFT 与谱方法求场](ePlace_Day05_学习笔记.pdf) | 5 |
| 第 6 天 | [Nesterov、步长预测与预条件](ePlace_Day06_学习笔记.pdf) | 5 |
| 第 7 天 | [完整算法、参数调度与实验证据](ePlace_Day07_学习笔记.pdf) | 6 |

[返回仓库首页](../../../README.md)
