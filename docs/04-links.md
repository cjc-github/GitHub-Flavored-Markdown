# 四、链接

[返回文档首页](../README.md)

## 4.1 网址链接

### 4.1.1 Markdown与GFM实现方式

CommonMark 使用 `[链接文本](URL "title")` 创建链接，`title` 为可选的悬停提示。

```markdown
[百度一下](https://www.baidu.com "悬停显示：百度一下")
```

显示效果如下：

> [百度一下](https://www.baidu.com "悬停显示：百度一下")

正式 GFM 还支持扩展自动链接，可以识别部分裸 URL、`www` 网址和 Email 地址。

```markdown
<https://www.baidu.com>

https://www.baidu.com

contact@example.com
```

### 4.1.2 HTML实现方式

HTML使用`<a>`标签，`href`指定地址，`title`提供可选提示。

```html
<a href="https://www.baidu.com" title="悬停显示：百度一下">百度一下</a>
```

GitHub会过滤不安全的URL协议和事件属性，不应使用`javascript:`或`onclick`等写法。

### 4.1.3 LaTeX实现方式

完整LaTeX文档可以通过`hyperref`宏包使用`\href`和`\url`。

```latex
\usepackage{hyperref}

\href{https://www.baidu.com}{百度一下}

\url{https://www.baidu.com}
```

GitHub数学公式渲染器不会加载`hyperref`，在GitHub文档正文中应使用Markdown链接。

> **路径与大小写敏感提示**：
> - `./file.md`、`../README.md` 和 `/README.md` 路径含义不同
> - GitHub 和 Linux 对文件名大小写敏感
> - Windows 本地环境可能对大小写不敏感，导致跨平台问题时需注意

<br/>

## 4.2 文件链接

### 4.2.1 Markdown与GFM实现方式

文件链接与普通网址链接语法相同，可以使用相对路径指向仓库内文件。

```markdown
[下载示例音频](../material/test.mp3 "test.mp3")
```

显示效果如下：

> [下载示例音频](../material/test.mp3 "test.mp3")

相对路径会相对于当前Markdown文件解析，因此移动文档后需要同步调整路径。

### 4.2.2 HTML实现方式

HTML同样使用`<a>`标签。独立网页可以添加`download`属性，但GitHub可能过滤或忽略该属性。

```html
<a href="../material/test.mp3">下载示例音频</a>
```

### 4.2.3 LaTeX实现方式

使用`hyperref`宏包可以链接同目录文件。是否允许直接打开本地文件取决于PDF阅读器的安全策略。

```latex
\usepackage{hyperref}

\href{run:./manual.pdf}{打开使用手册}
```

发布PDF时应确保被链接文件与PDF一起分发，并尽量使用相对路径。

## 4.3 图片与图片链接

### 4.3.1 Markdown与GFM实现方式

Markdown使用`![替代文本](图片URL "title")`插入图片。

```markdown
![百度示例图片](../README.assets/baidu.gif "悬停显示：百度一下")
```

显示效果如下：

> ![百度示例图片](../README.assets/baidu.gif "悬停显示：百度一下")

使用普通链接包裹图片语法，可以创建可点击图片。

```markdown
[![百度示例图片](../README.assets/baidu.gif)](https://www.baidu.com)
```

显示效果如下：

> [![百度示例图片](../README.assets/baidu.gif)](https://www.baidu.com)

### 4.3.2 HTML实现方式

HTML使用`<img>`插入图片，使用`<a>`包裹图片创建链接。

```html
<a href="https://www.baidu.com">
  <img src="../README.assets/baidu.gif" alt="百度示例图片" width="120">
</a>
```

GitHub会过滤部分样式属性，推荐使用`width`、`height`和有意义的`alt`文本完成基础展示。

### 4.3.3 LaTeX实现方式

完整LaTeX文档使用`graphicx`宏包插入图片；配合`hyperref`可以创建可点击图片。

```latex
\usepackage{graphicx}
\usepackage{hyperref}

\includegraphics[width=0.3\textwidth]{baidu.gif}

\href{https://www.baidu.com}{%
  \includegraphics[width=0.3\textwidth]{baidu.gif}%
}
```

实际支持的图片格式取决于LaTeX编译引擎；GIF动画通常只能作为静态帧处理。

## 4.4 标题和文档内跳转

### 4.4.1 Markdown与GitHub实现方式

GitHub会根据标题文本生成锚点，可以通过`[链接文本](#标题锚点)`进行页内跳转。

```markdown
[跳转到网址链接](#41-网址链接)

[返回文档目录](../README.md#文档目录)
```

显示效果如下：

> [跳转到网址链接](#41-网址链接)
>
> [返回文档目录](../README.md#文档目录)

修改标题可能改变自动锚点。需要被长期引用的章节应避免频繁重命名。

### 4.4.2 HTML实现方式

HTML可以通过`id`属性定义稳定锚点。

```html
<a href="#installation">跳转到安装章节</a>

<h2 id="installation">安装</h2>
```

### 4.4.3 LaTeX实现方式

LaTeX使用`\label`定义目标，使用`\ref`、`\pageref`或`\hyperref`进行引用。

```latex
\usepackage{hyperref}

\section{安装}\label{sec:installation}

详见第\ref{sec:installation}节。

\hyperref[sec:installation]{跳转到安装章节}
```

交叉引用通常需要至少编译两次才能得到正确编号。
