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

- [一、标题与目录](docs/01-headings.md)
	- [1.1 标题](docs/01-headings.md#11-标题)
		- [1.1.1 Markdown语法实现方式](docs/01-headings.md#111-markdown语法实现方式)
		- [1.1.2 HTML标签实现方式](docs/01-headings.md#112-html标签实现方式)
		- [1.1.3 LaTeX实现方式](docs/01-headings.md#113-latex实现方式)
	- [1.2 目录生成](docs/01-headings.md#12-目录生成)
		- [1.2.1 Markdown语法实现方式](docs/01-headings.md#121-markdown语法实现方式)
		- [1.2.2 HTML标签实现方式](docs/01-headings.md#122-html标签实现方式)
		- [1.2.3 LaTeX实现方式](docs/01-headings.md#123-latex实现方式)
- [二、文本格式](docs/02-text-format.md)
	- [2.1 换行](docs/02-text-format.md#21-换行)
		- [2.1.1 Markdown语法实现方式](docs/02-text-format.md#211-markdown语法实现方式)
		- [2.1.2 HTML标签实现方式](docs/02-text-format.md#212-html标签实现方式)
		- [2.1.3 LaTeX实现方式](docs/02-text-format.md#213-latex实现方式)
	- [2.2 字体格式](docs/02-text-format.md#22-字体格式)
		- [2.2.1 Markdown语法实现方式](docs/02-text-format.md#221-markdown语法实现方式)
		- [2.2.2 HTML标签实现方式](docs/02-text-format.md#222-html标签实现方式)
		- [2.2.3 LaTeX实现方式](docs/02-text-format.md#223-latex实现方式)
	- [2.3 删除线](docs/02-text-format.md#23-删除线)
		- [2.3.1 Markdown语法实现方式](docs/02-text-format.md#231-markdown语法实现方式)
		- [2.3.2 HTML标签实现方式](docs/02-text-format.md#232-html标签实现方式)
		- [2.3.3 LaTeX实现方式](docs/02-text-format.md#233-latex实现方式)
	- [2.4 下划线和上划线](docs/02-text-format.md#24-下划线和上划线)
		- [2.4.1 Markdown语法实现方式](docs/02-text-format.md#241-markdown语法实现方式)
		- [2.4.2 HTML标签实现方式](docs/02-text-format.md#242-html标签实现方式)
		- [2.4.3 LaTeX实现方式](docs/02-text-format.md#243-latex实现方式)
	- [2.5 上下标](docs/02-text-format.md#25-上下标)
		- [2.5.1 Markdown语法实现方式](docs/02-text-format.md#251-markdown语法实现方式)
		- [2.5.2 HTML标签实现方式](docs/02-text-format.md#252-html标签实现方式)
		- [2.5.3 LaTeX实现方式](docs/02-text-format.md#253-latex实现方式)
	- [2.6 分割线](docs/02-text-format.md#26-分割线)
		- [2.6.1 Markdown语法实现方式](docs/02-text-format.md#261-markdown语法实现方式)
		- [2.6.2 HTML标签实现方式](docs/02-text-format.md#262-html标签实现方式)
		- [2.6.3 LaTeX实现方式](docs/02-text-format.md#263-latex实现方式)
	- [2.7 脚注](docs/02-text-format.md#27-脚注)
		- [2.7.1 Markdown语法实现方式](docs/02-text-format.md#271-markdown语法实现方式)
		- [2.7.2 HTML标签实现方式](docs/02-text-format.md#272-html标签实现方式)
		- [2.7.3 LaTeX实现方式](docs/02-text-format.md#273-latex实现方式)
	- [2.8 高亮](docs/02-text-format.md#28-高亮)
		- [2.8.1 Markdown语法实现方式](docs/02-text-format.md#281-markdown语法实现方式)
		- [2.8.2 HTML标签实现方式](docs/02-text-format.md#282-html标签实现方式)
		- [2.8.3 LaTeX实现方式](docs/02-text-format.md#283-latex实现方式)
	- [2.9 行内代码标记](docs/02-text-format.md#29-行内代码标记)
		- [2.9.1 Markdown语法实现方式](docs/02-text-format.md#291-markdown语法实现方式)
		- [2.9.2 HTML标签实现方式](docs/02-text-format.md#292-html标签实现方式)
		- [2.9.3 LaTeX实现方式](docs/02-text-format.md#293-latex实现方式)
	- [2.10 块引用](docs/02-text-format.md#210-块引用)
		- [2.10.1 Markdown语法实现方式](docs/02-text-format.md#2101-markdown语法实现方式)
		- [2.10.2 HTML标签实现方式](docs/02-text-format.md#2102-html标签实现方式)
		- [2.10.3 LaTeX实现方式](docs/02-text-format.md#2103-latex实现方式)
	- [2.11 代码块](docs/02-text-format.md#211-代码块)
		- [2.11.1 Markdown语法实现方式](docs/02-text-format.md#2111-markdown语法实现方式)
		- [2.11.2 HTML标签实现方式](docs/02-text-format.md#2112-html标签实现方式)
		- [2.11.3 LaTeX实现方式](docs/02-text-format.md#2113-latex实现方式)
	- [2.12 字体颜色](docs/02-text-format.md#212-字体颜色)
		- [2.12.1 Markdown语法实现方式](docs/02-text-format.md#2121-markdown语法实现方式)
		- [2.12.2 HTML标签实现方式](docs/02-text-format.md#2122-html标签实现方式)
		- [2.12.3 LaTeX实现方式](docs/02-text-format.md#2123-latex实现方式)
	- [2.13 背景颜色](docs/02-text-format.md#213-背景颜色)
		- [2.13.1 Markdown语法实现方式](docs/02-text-format.md#2131-markdown语法实现方式)
		- [2.13.2 HTML标签实现方式](docs/02-text-format.md#2132-html标签实现方式)
		- [2.13.3 LaTeX实现方式](docs/02-text-format.md#2133-latex实现方式)
- [三、列表](docs/03-lists.md)
	- [3.1 无序列表](docs/03-lists.md#31-无序列表)
		- [3.1.1 Markdown语法实现方式](docs/03-lists.md#311-markdown语法实现方式)
		- [3.1.2 HTML标签实现方式](docs/03-lists.md#312-html标签实现方式)
		- [3.1.3 LaTeX实现方式](docs/03-lists.md#313-latex实现方式)
	- [3.2 有序列表](docs/03-lists.md#32-有序列表)
		- [3.2.1 Markdown语法实现方式](docs/03-lists.md#321-markdown语法实现方式)
		- [3.2.2 HTML标签实现方式](docs/03-lists.md#322-html标签实现方式)
		- [3.2.3 LaTeX实现方式](docs/03-lists.md#323-latex实现方式)
	- [3.3 任务列表](docs/03-lists.md#33-任务列表)
		- [3.3.1 Markdown语法实现方式](docs/03-lists.md#331-markdown语法实现方式)
		- [3.3.2 HTML标签实现方式](docs/03-lists.md#332-html标签实现方式)
		- [3.3.3 LaTeX实现方式](docs/03-lists.md#333-latex实现方式)
- [四、链接](docs/04-links.md)
	- [4.1 网址链接](docs/04-links.md#41-网址链接)
		- [4.1.1 Markdown与GFM实现方式](docs/04-links.md#411-markdown与gfm实现方式)
		- [4.1.2 HTML实现方式](docs/04-links.md#412-html实现方式)
		- [4.1.3 LaTeX实现方式](docs/04-links.md#413-latex实现方式)
	- [4.2 文件链接](docs/04-links.md#42-文件链接)
		- [4.2.1 Markdown与GFM实现方式](docs/04-links.md#421-markdown与gfm实现方式)
		- [4.2.2 HTML实现方式](docs/04-links.md#422-html实现方式)
		- [4.2.3 LaTeX实现方式](docs/04-links.md#423-latex实现方式)
	- [4.3 图片与图片链接](docs/04-links.md#43-图片与图片链接)
		- [4.3.1 Markdown与GFM实现方式](docs/04-links.md#431-markdown与gfm实现方式)
		- [4.3.2 HTML实现方式](docs/04-links.md#432-html实现方式)
		- [4.3.3 LaTeX实现方式](docs/04-links.md#433-latex实现方式)
	- [4.4 标题和文档内跳转](docs/04-links.md#44-标题和文档内跳转)
		- [4.4.1 Markdown与GitHub实现方式](docs/04-links.md#441-markdown与github实现方式)
		- [4.4.2 HTML实现方式](docs/04-links.md#442-html实现方式)
		- [4.4.3 LaTeX实现方式](docs/04-links.md#443-latex实现方式)
- [五、图片与图表](docs/05-images.md)
	- [5.1 插入静态图片](docs/05-images.md#51-插入静态图片)
		- [5.1.1 图片链接](docs/05-images.md#511-图片链接)
		- [5.1.2 HTML标签](docs/05-images.md#512-html标签)
		- [5.1.3 LaTeX实现方式](docs/05-images.md#513-latex实现方式)
	- [5.2 插入动态图片](docs/05-images.md#52-插入动态图片)
		- [5.2.1 流程图](docs/05-images.md#521-流程图)
		- [5.2.2 时序图](docs/05-images.md#522-时序图)
		- [5.2.3 甘特图](docs/05-images.md#523-甘特图)
		- [5.2.4 饼图](docs/05-images.md#524-饼图)
		- [5.2.5 类图](docs/05-images.md#525-类图)
		- [5.2.6 状态图](docs/05-images.md#526-状态图)
		- [5.2.7 flow流程图](docs/05-images.md#527-flow流程图)
		- [5.2.8 GeoJSON地图](docs/05-images.md#528-geojson地图)
		- [5.2.9 TopoJSON地图](docs/05-images.md#529-topojson地图)
		- [5.2.10 ASCII STL三维模型](docs/05-images.md#5210-ascii-stl三维模型)
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
		- [公式 1](docs/07-math.md#公式-1)
	- [7.5 不同载体的实现方式](docs/07-math.md#75-不同载体的实现方式)
- [八、GitHub常见组件](docs/08-github-features.md)
	- [8.1 表情和符号](docs/08-github-features.md#81-表情和符号)
		- [8.1.1 emoji表情](docs/08-github-features.md#811-emoji表情)
		- [8.1.2 HTML字符](docs/08-github-features.md#812-html字符)
		- [8.1.3 特殊符号](docs/08-github-features.md#813-特殊符号)
	- [8.2 diff代码块](docs/08-github-features.md#82-diff代码块)
	- [8.3 徽章](docs/08-github-features.md#83-徽章)
		- [8.3.1 构建与集成状态](docs/08-github-features.md#831-构建与集成状态)
		- [8.3.2 测试覆盖率与质量](docs/08-github-features.md#832-测试覆盖率与质量)
		- [8.3.3 版本与发布信息](docs/08-github-features.md#833-版本与发布信息)
		- [8.3.4 GitHub仓库数据](docs/08-github-features.md#834-github仓库数据)
		- [8.3.5 兼容性信息](docs/08-github-features.md#835-兼容性信息)
		- [8.3.6 文档与聊天渠道](docs/08-github-features.md#836-文档与聊天渠道)
		- [8.3.7 其他用途](docs/08-github-features.md#837-其他用途)
	- [8.4 GitHub数据图](docs/08-github-features.md#84-github数据图)
		- [8.4.1 star历史图](docs/08-github-features.md#841-star历史图)
		- [8.4.2 contribution贡献图](docs/08-github-features.md#842-contribution贡献图)
	- [8.5 折叠](docs/08-github-features.md#85-折叠)
	- [8.6 视频](docs/08-github-features.md#86-视频)
		- [8.6.1 GitHub上传视频](docs/08-github-features.md#861-github上传视频)
		- [8.6.2 HTML的视频标签](docs/08-github-features.md#862-html的视频标签)
	- [8.7 音频](docs/08-github-features.md#87-音频)
		- [8.7.1 GitHub上传音频](docs/08-github-features.md#871-github上传音频)
		- [8.7.2 HTML的音频标签](docs/08-github-features.md#872-html的音频标签)
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
