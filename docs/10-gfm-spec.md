# 十、GFM规范补充

[返回文档首页](../README.md)

## 10.1 正式GFM扩展范围

GFM以CommonMark为基础，并定义了以下扩展：

1. 删除线（Strikethrough）
2. 表格（Tables）
3. 任务列表项（Task list items）
4. 扩展自动链接（Autolinks extension）
5. 禁止的原始HTML标签（Disallowed raw HTML）

GitHub上的Alerts、脚注、数学公式、Mermaid图表、GeoJSON、TopoJSON和STL属于GitHub平台能力，不应与正式GFM扩展混为一谈。

## 10.2 反斜杠转义

在具有Markdown语义的ASCII标点符号前添加反斜杠，可以让该符号按普通文本显示。

```markdown
\*不会变成强调文本\*
\# 不会变成标题
\[不会变成链接文本\](https://example.com)
```

显示效果如下：

> \*不会变成强调文本\*
>
> \# 不会变成标题
>
> \[不会变成链接文本\](https://example.com)

代码跨度和代码块中的反斜杠不会继续触发Markdown转义规则。

## 10.3 缩进代码块

连续内容缩进四个空格可以形成缩进代码块。与围栏式代码块相比，它不能直接指定语言标识符，因此通常推荐使用三个反引号。

```markdown
    const message = "hello";
    console.log(message);
```

缩进代码块不能中断正在解析的段落，通常需要在前面保留一个空行。

## 10.4 引用式链接

引用式链接将链接文本和目标地址分开定义，适合在同一篇文档中复用地址。

```markdown
这是一个[GitHub链接][github]，这里再次使用[同一个地址][github]。

[github]: https://github.com "GitHub"
```

引用标识符不区分大小写，连续空白会按规范折叠。未被引用的链接定义不会直接显示在最终文档中。

引用式图片使用相同机制：

```markdown
![图片说明][logo]

[logo]: ./README.assets/image-20251221121446147.png "示例图片"
```

## 10.5 原始HTML与安全过滤

Markdown允许混合部分原始HTML，但GitHub会对最终HTML进行安全过滤。能够写入Markdown源码，不代表所有标签、属性或URL协议都会保留。

使用原始HTML时应遵循以下原则：

- 优先使用Markdown原生语法。
- 不依赖`onclick`等事件属性或JavaScript协议。
- 不假设`style`、CSS类或任意嵌入内容一定会保留。
- 对需要跨平台显示的内容，在目标平台进行实际预览。

## 10.6 禁止的原始HTML标签

正式GFM会对以下标签名称进行特殊处理，使其不能作为可执行或可嵌入的原始HTML直接生效：

```text
title textarea style xmp iframe noembed noframes script plaintext
```

例如下面的内容会作为文本处理，而不是执行脚本：

```markdown
<script>alert("不会执行")</script>
```

除了GFM规范中的禁止标签，GitHub平台还会执行额外的HTML清理，因此应避免依赖未经官方文档确认的HTML行为。
