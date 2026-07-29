# 四、链接

[返回文档首页](../README.md)

## 4.1 网址链接

### 4.1.1 Markdown语法实现方式

格式:

```markdown
[链接文本](URL "title")
```

方括号中的内容是链接文本，圆括号中依次填写目标地址和可选的标题。

- 链接文本用于描述目标内容，不建议省略

- title表示鼠标悬停在链接时的提示文本，使用引号包裹

案例：

```markdown
这是一个URL链接: [百度一下](https://www.baidu.com "悬停显示: 百度一下")
```

显示效果如下：

> 这是一个URL链接: [百度一下](https://www.baidu.com "悬停显示: 百度一下")

<br/>

#### 网址链接扩展

如果想直接展示URL，可以把链接文本写成URL，也可以使用自动链接语法。

案例：

```markdown
这是一个URL链接: [https://www.baidu.com](https://www.baidu.com "悬停显示: 百度一下")
```

显示效果如下：

> 这是一个URL链接: [https://www.baidu.com](https://www.baidu.com "悬停显示: 百度一下")

<br/>

**省略方法：**

使用尖括号可以很方便地把URL或Email地址变成可点击的链接。GFM还可以自动识别常见的裸URL和`www`开头的网址。

案例：

```markdown
这是一个URL链接: <https://www.baidu.com>
```

显示效果如下：

> 这是一个URL链接: <https://www.baidu.com>

注意：这种方式适用于URL网址，Email地址等场景

<br/>

### 4.1.2 HTML标签实现方式

HTML可以使用`<a>`标签创建链接，`href`属性指定目标地址，`title`属性提供可选提示文本。

案例：

```html
<a href="https://www.baidu.com" title="悬停显示：百度一下">百度一下</a>
```

注意：GitHub会过滤不安全的HTML属性和协议，不应依赖脚本事件或内联JavaScript。

### 4.1.3 LaTeX公式实现方式

LaTeX数学公式用于表达数学内容，不提供通用的网页链接语法。在GitHub文档中需要链接时，应使用Markdown链接或`<a>`标签。


## 4.2 文件链接

格式:

```markdown
[alt](URL title)
```

alt和title即对应HTML中的alt和title属性（都可省略）

- alt表示文件链接显示失败时的替换文本
- title表示鼠标悬停在文件链接时的显示文本（注意这里要加引号）

案例：

```markdown
这是一个文件链接: [百度一下](../README.assets/baidu.gif "悬停显示: 百度一下")
```

显示效果如下：

> 这是一个文件链接: [百度一下](../README.assets/baidu.gif "悬停显示: 百度一下")

<br/>

## 4.3 图片链接/插入图片

格式:

```markdown
![alt](URL title)
```

alt和title即对应HTML中的alt和title属性（都可省略）

- alt表示图片显示失败时的替换文本

- title表示鼠标悬停在图片时的显示文本（注意这里要加引号）

案例：

```markdown
这是一个文件链接: ![百度一下](../README.assets/baidu.gif "悬停显示: 百度一下")
```

显示效果如下：

> 这是一个文件链接: ![百度一下](../README.assets/baidu.gif "悬停显示: 百度一下")

<br/>

### 4.3.1 给图片加链接

格式:

```markdown
[![alt](图片URL title)](链接URL)
```

alt和title即对应HTML中的alt和title属性（都可省略）

- alt表示图片显示失败时的替换文本
- title表示鼠标悬停在图片时的显示文本（注意这里要加引号）

案例：

```markdown
这是一个文件链接: [![百度一下](../README.assets/baidu.gif "悬停显示: 百度一下")](https://www.baidu.com)
```

显示效果如下：

> 这是一个文件链接: [![百度一下](../README.assets/baidu.gif "悬停显示: 百度一下")](https://www.baidu.com)

## 4.4 标题链接

格式:

```markdown
[alt](URL title)
```

alt和title即对应HTML中的alt和title属性（都可省略）

- alt表示标题链接显示失败时的替换文本
- title表示鼠标悬停在标题链接时的显示文本（注意这里要加引号）

案例：

```markdown
标题链接: [4.1 网址链接](#41-网址链接 "跳转到4.1节")

回到目录: [↑ 回到目录](../README.md#文档目录)
```

显示效果如下：

> 标题链接: [4.1 网址链接](#41-网址链接 "跳转到4.1节")
> 
> 回到目录: [↑ 回到目录](../README.md#文档目录)

<br/>
