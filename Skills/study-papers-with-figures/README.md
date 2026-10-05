# 论文精读与图解笔记

可复用的中文论文学习 skill，适用于研究论文，尤其 FPGA/ASIC EDA 与优化算法。

## 使用方式

在已安装该技能的 ChatGPT/Codex 中上传论文，然后请求：

> 使用 study-papers-with-figures 带领我学习这篇论文，从第一天开始，循序讲解，尽量覆盖原图和子图，并整理成学术风格的中文 LaTeX PDF。

也支持“继续下一天”“完成剩余学习”“补充原图与读图说明”等请求。学习天数根据论文内容决定，不固定七天。

[ChatGPT 技能页面](https://chatgpt.com/skills?skill_id=6ac37a35b5e481919ab864878dc98fbb)

此目录为完整技能源码归档。GitHub 中的文件不会自动安装到其他账户或客户端；需要按对应环境的技能安装方式导入整个目录，保留相对路径。

## 文件

| 文件 | 用途 |
|---|---|
| [SKILL.md](SKILL.md) | 触发条件与完整工作流程 |
| [agents/openai.yaml](agents/openai.yaml) | 技能名称与调用提示 |
| [assets/academic-notes.tex](assets/academic-notes.tex) | 中文学术风格 LaTeX 模板 |
| [references/figures.md](references/figures.md) | 原图、子图覆盖与裁切规则 |
| [references/teaching-and-layout.md](references/teaching-and-layout.md) | 循序教学、证据与排版要求 |
| [scripts/paper_figures.py](scripts/paper_figures.py) | 图注候选清点、PDF/PNG 原图裁切 |

## 原图处理工具

脚本需要 Python 与 PyMuPDF。PDF 编译需要 XeLaTeX、模板使用的 LaTeX 包和可用的中文字体；缺字体时在论文项目中提供 paper-fonts.tex。

```bash
python3 scripts/paper_figures.py inventory paper.pdf --out inventory.json
python3 scripts/paper_figures.py crop paper.pdf --page 7 --rect 108 99 528 300 --out figures/fig01.pdf
```

裁切参数仅为格式示例，必须按当前论文实际页面确认。图注清点结果只是候选，必须视觉核对全部原图和子图后，才能声明全部覆盖。

技能将原文内容、教学推导和数值例子分开；每幅原图保留图号、出处和中文读图说明。同步到 Notion/GitHub 需有用户授权及可用连接。
