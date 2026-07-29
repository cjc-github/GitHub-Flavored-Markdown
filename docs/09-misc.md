# 九、杂项

[返回文档首页](../README.md)

## 9.1 GitHub Markdown暂不支持的功能

+ 目前GitHub Markdown暂时不支持css语法，如字体颜色、字体等
+ 目前GitHub Markdown不支持文本块行号显示
+ 目前GitHub Markdown不支持代码块自动换行、行号显示
+ 目前GitHub Markdown不支持嵌入音频组件显示
+ 目前github Markdown不支持对公式进行编号

<br/>


## 9.2 支持情况与实现方法总结

本文汇总了常见排版功能在原生 Markdown、GFM、HTML、LaTeX 以及 Markdown 编辑器中的支持情况与实现方法。不同渲染器的实现可能存在差异，实际使用时应以目标平台的渲染结果为准。



| 序号 | **功能点**         | **Markdown标准语法**                                         | HTML标签                                                     | LaTeX公式（不考虑导入外部包）                            | GitHub Flavored Markdown (GFM)语法                      | **Markdown编辑器**（以Typora为例）                      |
| ---- | ------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | -------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| 1    | 标题               | 1、`=`为1级标题，`-`为2级标题；<br /> 2、`#`到`#######`代表1-6级标题； | 1、使用`<h1>到<h6>`标签代表1-6级标题；                       | 1、使用`\section{}`, `\part{}`, `\chapter{}`命令；       | • 支持Markdown<br />• 支持HTML<br />• 不支持LaTeX公式   | • 支持Markdown<br />• 支持HTML<br />• 不支持LaTeX公式   |
| 2    | 换行               | 1、行尾2个空格+回车；<br/>2、 行尾+空行；<br/>3、行尾反斜杠+回车； | 1、使用`<br/>`标签；                                         | 1、使用`\newline{}`命令；                                | • 支持Markdown<br />• 支持HTML<br />• 不支持LaTeX公式   | • 支持Markdown<br />• 支持HTML<br />• 不支持LaTeX公式   |
| 3    | 字体格式-粗体      | 1、使用两个星号`**`包围；<br />2、使用两个下划线`__`包围；   | 1、使用`<b>`标签；<br />2、使用`<strong>`标签；              | 1、使用`\textbf{}`命令；                                 | • 支持Markdown<br />• 支持HTML<br />• 支持LaTeX公式     | • 支持Markdown<br />• 支持HTML<br />• 支持LaTeX公式     |
| 4    | 字体格式-斜体      | 1、使用一个星号`*`包围；<br />2、使用一个下划线`_`包围；     | 1、使用`<i>`标签；<br />2、使用`<em>`标签；                  | 1、使用`\textit{}`命令；                                 | • 支持Markdown<br />• 支持HTML<br />• 支持LaTeX公式     | • 支持Markdown<br />• 支持HTML<br />• 支持LaTeX公式     |
| 5    | 删除线             | 1、使用两个波浪号`~~`包围；<br />2、使用一个波浪号`~`包围（非常规，但GFM支持）； | 1、使用`<del>`标签；<br />2、使用`<s>`标签；                 | 1、使用`\cancel{}`命令；                                 | • 支持Markdown<br />• 支持HTML<br />• 支持LaTeX公式     | • 支持Markdown<br />• 支持HTML<br />• 支持LaTeX公式     |
| 6    | 下划线             | 不支持                                                       | 1、使用`<u>`标签；<br />2、使用`<ins>`标签;                  | 1、使用`\underline{}`命令；                              | • 不支持Markdown<br />• 支持HTML<br />• 支持LaTeX公式   | • 不支持Markdown<br />• 支持HTML<br />• 支持LaTeX公式   |
| 7    | 上划线             | 不支持                                                       | 不支持                                                       | 1、使用`\overline{}`命令；                               | • 不支持Markdown<br />• 不支持HTML<br />• 支持LaTeX公式 | • 不支持Markdown<br />• 不支持HTML<br />• 支持LaTeX公式 |
| 8    | 下标               | 不支持                                                       | 1、使用`<sub>`标签；                                         | 1、使用`^{}`命令；                                       | • 不支持Markdown<br />• 支持HTML<br />• 支持LaTeX公式   | • 不支持Markdown<br />• 支持HTML<br />• 支持LaTeX公式   |
| 9    | 上标               | 不支持                                                       | 1、使用`<sup>`标签；                                         | 1、使用`_{}`命令；                                       | • 不支持Markdown<br />• 支持HTML<br />• 支持LaTeX公式   | • 不支持Markdown<br />• 支持HTML<br />• 支持LaTeX公式   |
| 10   | 分割线             | 1、单行使用三个或多个星号`*`；<br />2、单行使用三个或多个破折号`-`；<br />3、单行使用三个或多个下划线号`_`；<br /> | 1、使用`<hr>`标签；                                          |                                                          | 支持Markdown、HTML                                      |                                                         |
| 11   | 脚注               | 1、使用`[^脚注标识]`；                                       |                                                              |                                                          | 支持Markdown、HTML                                      |                                                         |
| 12   | 高亮               | 不支持                                                       | 1、使用`<mark>`标签；                                        |                                                          | 支持Markdown、HTML                                      |                                                         |
| 13   | 行内代码标记       | 1、使用一个反引号`` `来包围；                                | 1、使用`<code>`标签；                                        |                                                          | 支持Markdown、HTML                                      |                                                         |
| 14   | 块引用             | 1、使用`>`符号                                               | 1、使用`<blockquote>`标签；                                  |                                                          | 支持Markdown、HTML                                      |                                                         |
| 15   | 代码块             | 1、使用三个反引号`````` ```来包围；                          | 1、使用`<code>`标签；                                        |                                                          | 支持Markdown、HTML                                      |                                                         |
| 16   | 字体颜色           | 不支持                                                       | 1、使用`<font>`标签的`color`属性；<br />2、使用`<span>`标签的`color`属性;<br />3、使用`<div>`标签的`color`属性； | 1、使用`\color{}`命令；<br />2、使用`\textcolor{}`命令； | 支持Markdown、HTML                                      |                                                         |
| 17   | 背景颜色           | 不支持                                                       | 1、使用`<font>`标签的`color`属性；<br />2、使用`<span>`标签的`color`属性;<br />3、使用`<div>`标签的`color`属性；<br />4、使用`<mark>`标签 |                                                          | 支持Markdown、HTML                                      |                                                         |
| 18   | 无序列表           | 1、使用星号(`*`)加空格；<br />2、使用加号(`+`)加空格；<br />3、使用减号(`-`)加空格； | 1、使用`<ul>`标签；                                          |                                                          | 支持Markdown、HTML                                      |                                                         |
| 19   | 有序列表           | 1、使用数字加.号；<br />                                     | 1、使用`<ol>`标签；                                          |                                                          | 支持Markdown、HTML                                      |                                                         |
| 20   | 任务列表           | 1、使用`- [ ] `表示未选用；<br />2、使用`- [x] `表示已选用； | 1、使用`<ul>`和`<input>`标签组合使用；                       |                                                          | 支持Markdown、HTML                                      |                                                         |
| 21   | 链接-网址/文件链接 | 1、使用`[链接文本](URL "title")`语法；                      | 1、使用`<a href="URL">`标签；                                |                                                          | 支持Markdown、HTML                                      |                                                         |
| 22   | 链接-图片链接      | 1、使用`![alt](URL title)`语法                               | 1、使用`<a href="URL">`包裹`<img>`标签；                     |                                                          | 支持Markdown、HTML                                      |                                                         |
| 23   | 链接-标题链接      | 1、使用`[链接文本](#标题锚点)`语法；                         | 1、使用`<a href="#标题锚点">`标签；                          |                                                          | 支持Markdown、HTML                                      |                                                         |
| 24   | 图片               | 1、使用`![alt](URL title)`语法；                             | 1、使用`<img>`标签；                                         |                                                          | 支持Markdown、HTML                                      |                                                         |
| 25   | 表格               | 1、使用 `\|` 分割单元格，使用 `-` 分割表头和其他行；         | 1、使用`<table>`标签；                                       |                                                          | 支持Markdown、HTML                                      |                                                         |
| 26   | 数学公式           | 1.行内公式：单个美元符号 `$` 包围；<br />2.块级公式：两个美元符号 `$$` 包围； |                                                              |                                                          | 支持Markdown、HTML                                      |                                                         |
| 27   | 折叠               | 不支持                                                       | 1、使用`<details>`和`<summary>`标签；                         |                                                          | 支持Markdown、HTML                                      |                                                         |
| 28   | 视频               | 只支持`user-attachments`附件，但可以渲染成视频组件           | 1、使用`<video>`标签；                                       |                                                          | 支持Markdown、HTML                                      |                                                         |
| 29   | 音频               | 支持`user-attachments`附件，但不可以渲染成音频组件           | 1、使用`<audio>`标签；                                       |                                                          | 支持Markdown、HTML                                      |                                                         |

<br/>

