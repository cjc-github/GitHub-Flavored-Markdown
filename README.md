# GitHub Flavored Markdown 中文参考

本项目整理CommonMark基础语法、正式GFM扩展、GitHub平台写作功能，以及常见HTML和LaTeX实现差异。

> 当前文档版本：`2026.07.0`

## 内容边界

1. **CommonMark基础语法**：Markdown通用语法基础。
2. **正式GFM扩展**：删除线、表格、任务列表项、扩展自动链接和禁止的原始HTML。
3. **GitHub平台功能**：Alerts、脚注、数学公式、Mermaid、GeoJSON、TopoJSON和STL等。
4. **HTML与LaTeX**：仅用于对比实现方式，不代表GitHub支持任意标签、属性或命令。

## 示例编写约定

各功能尽量给出Markdown/GFM、HTML和LaTeX实现。某种载体没有等价能力时，文档会明确标记“无原生实现”或“不适用”，并提供最接近的静态替代方案。

本仓库以GitHub网页端的实际渲染结果为主要目标。示例中的代码按以下范围理解：

- **GitHub可直接渲染**：可以用于GitHub支持的Markdown页面，但仍可能存在页面类型或安全过滤限制。
- **仅独立HTML可用**：浏览器打开独立HTML页面时有效，不代表粘贴到GitHub Markdown后仍会保留。
- **仅完整LaTeX可用**：需要LaTeX编译器和相关宏包；GitHub只支持数学公式中的部分LaTeX命令。
- **第三方扩展**：依赖特定编辑器、插件或渲染器，在GitHub上通常只显示源码或普通文本。

详细支持矩阵和判断方法见[支持情况与杂项](docs/09-misc.md)。

## 文档目录

> **目录说明**：为降低维护成本，目录仅保留一级和二级章节。详细三级目录请查看各文档页面。

- [一、标题与目录](docs/01-headings.md)
	- [1.1 标题](docs/01-headings.md#11-标题)
	- [1.2 目录生成](docs/01-headings.md#12-目录生成)
- [二、文本格式](docs/02-text-format.md)
	- [2.1 换行](docs/02-text-format.md#21-换行)
	- [2.2 字体格式](docs/02-text-format.md#22-字体格式)
	- [2.3 删除线](docs/02-text-format.md#23-删除线)
	- [2.4 下划线和上划线](docs/02-text-format.md#24-下划线和上划线)
	- [2.5 上下标](docs/02-text-format.md#25-上下标)
	- [2.6 分割线](docs/02-text-format.md#26-分割线)
	- [2.7 脚注](docs/02-text-format.md#27-脚注)
	- [2.8 高亮](docs/02-text-format.md#28-高亮)
	- [2.9 行内代码标记](docs/02-text-format.md#29-行内代码标记)
	- [2.10 块引用](docs/02-text-format.md#210-块引用)
	- [2.11 代码块](docs/02-text-format.md#211-代码块)
	- [2.12 字体颜色](docs/02-text-format.md#212-字体颜色)
	- [2.13 背景颜色](docs/02-text-format.md#213-背景颜色)
- [三、列表](docs/03-lists.md)
	- [3.1 无序列表](docs/03-lists.md#31-无序列表)
	- [3.2 有序列表](docs/03-lists.md#32-有序列表)
	- [3.3 任务列表](docs/03-lists.md#33-任务列表)
- [四、链接](docs/04-links.md)
	- [4.1 网址链接](docs/04-links.md#41-网址链接)
	- [4.2 文件链接](docs/04-links.md#42-文件链接)
	- [4.3 图片与图片链接](docs/04-links.md#43-图片与图片链接)
	- [4.4 标题和文档内跳转](docs/04-links.md#44-标题和文档内跳转)
- [五、图片与图表](docs/05-images.md)
	- [5.1 插入静态图片](docs/05-images.md#51-插入静态图片)
	- [5.2 插入图表和可视化内容](docs/05-images.md#52-插入图表和可视化内容)
	- [5.3 特殊图片](docs/05-images.md#53-特殊图片)
- [六、表格](docs/06-tables.md)
	- [6.1 Markdown与GFM实现方式](docs/06-tables.md#61-markdown与gfm实现方式)
	- [6.2 HTML实现方式](docs/06-tables.md#62-html实现方式)
	- [6.3 LaTeX实现方式](docs/06-tables.md#63-latex实现方式)
- [七、数学公式](docs/07-math.md)
	- [7.1 行内公式](docs/07-math.md#71-行内公式)
	- [7.2 块级公式](docs/07-math.md#72-块级公式)
	- [7.3 多行公式](docs/07-math.md#73-多行公式)
	- [7.4 公式编号](docs/07-math.md#74-公式编号)
	- [7.5 不同载体的实现方式](docs/07-math.md#75-不同载体的实现方式)
- [八、GitHub常见组件](docs/08-github-features.md)
	- [8.1 表情和符号](docs/08-github-features.md#81-表情和符号)
	- [8.2 diff代码块](docs/08-github-features.md#82-diff代码块)
	- [8.3 徽章](docs/08-github-features.md#83-徽章)
	- [8.4 GitHub数据图](docs/08-github-features.md#84-github数据图)
	- [8.5 折叠](docs/08-github-features.md#85-折叠)
	- [8.6 视频](docs/08-github-features.md#86-视频)
	- [8.7 音频](docs/08-github-features.md#87-音频)
	- [8.8 GitHub自动引用与提及](docs/08-github-features.md#88-github-自动引用与提及)
- [九、支持情况与杂项](docs/09-misc.md)
	- [9.1 GitHub平台的常见限制](docs/09-misc.md#91-github平台的常见限制)
	- [9.2 功能归属与支持矩阵](docs/09-misc.md#92-功能归属与支持矩阵)
	- [9.3 判断一项语法属于哪一层](docs/09-misc.md#93-判断一项语法属于哪一层)
- [十、GFM规范补充](docs/10-gfm-spec.md)
	- [10.1 正式GFM扩展范围](docs/10-gfm-spec.md#101-正式gfm扩展范围)
	- [10.2 反斜杠转义](docs/10-gfm-spec.md#102-反斜杠转义)
	- [10.3 缩进代码块](docs/10-gfm-spec.md#103-缩进代码块)
	- [10.4 引用式链接](docs/10-gfm-spec.md#104-引用式链接)
	- [10.5 原始HTML与安全过滤](docs/10-gfm-spec.md#105-原始html与安全过滤)
	- [10.6 禁止的原始HTML标签](docs/10-gfm-spec.md#106-禁止的原始html标签)
- [Emoji参考](material/emoji.md)
- [HTML实体参考](material/entities.md)

## 官方资源

- [GitHub Flavored Markdown规范](https://github.github.com/gfm/)：https://github.github.com/gfm/
- [CommonMark规范](https://commonmark.org/)：https://commonmark.org/
- [GitHub写作与格式化文档](https://docs.github.com/get-started/writing-on-github)：https://docs.github.com/get-started/writing-on-github

## 本地验证

```powershell
python material/parser_entities.py --check
python scripts/check_local_links.py
python -m unittest discover -s tests -v
npx --yes markdownlint-cli2@0.18.1 README.md CONTRIBUTING.md "docs/*.md" "material/**/*.md"
```

## 参与维护

提交修改前请阅读[贡献指南](CONTRIBUTING.md)。项目协作约定和维护信息见：

- [行为准则](CODE_OF_CONDUCT.md)
- [安全策略](SECURITY.md)
- [支持说明](SUPPORT.md)
- [更新日志](CHANGELOG.md)
- [当前版本](VERSION)

本项目采用MIT许可证，详见[LICENSE](LICENSE)。
