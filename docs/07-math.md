# 七、数学公式

[返回文档首页](../README.md)

Markdown和正式GFM规范本身没有定义数学公式。GitHub平台使用MathJax渲染受支持的LaTeX数学命令，可用于仓库Markdown文件、Issue、Pull Request、Discussion和Wiki。该能力不是完整LaTeX编译环境。

## 7.1 行内公式

行内公式使用单个美元符号 `$` 包围，公式会嵌入到文本中

案例：

```markdown
文本中的变量 $x = 5$ 和函数 $f(x) = x^2 + 2x + 1$。
```

显示效果如下：

文本中的变量 $x = 5$ 和函数 $f(x) = x^2 + 2x + 1$。

<br/>

## 7.2 块级公式

块级公式使用双美元符号 `$$` 包围，公式会独立成行并居中显示

案例：

```markdown
$$E = mc^2$$

$$\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}$$
```

显示效果如下：

$$E = mc^2$$

$$\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}$$

<br/>

## 7.3 多行公式

使用 align 环境创建多行对齐公式

案例：

```markdown
$$
  \begin{align}
  f(x) &= ax^2 + bx + c \\
  f'(x)  &= 2ax + b \\
  f''(x)  &= 2a
  \end{align}
$$

$$
\begin{equation}
E = mc^2
\end{equation}
$$
```

显示效果如下：

> align
>
> $$
> \begin{align}
>   f(x) &= ax^2 + bx + c \\
>   f'(x)  &= 2ax + b \\
>   f''(x)  &= 2a
>   \end{align}
> $$
>
> equation
>
> $$
> \begin{equation}
> E = mc^2
> \end{equation}
> $$

<br/>

## 7.4 公式编号

GitHub数学渲染不提供完整LaTeX文档那样稳定的自动编号、`\label`和`\ref`交叉引用流程。即使某个MathJax命令当前能够显示，也不应把它等同于完整LaTeX环境中的编号系统。

面向GitHub的文档可以使用普通文本手工编号，并通过Markdown标题链接建立稳定引用：

```markdown
### 公式 1

$$
E = mc^2 \qquad (1)
$$

[参见公式 1](#公式-1)
```

显示效果如下：

### 公式 1

$$
E = mc^2 \qquad (1)
$$

[参见公式 1](#公式-1)

<br/>

## 7.5 不同载体的实现方式

| 载体 | 实现方式 | 适用范围 |
| --- | --- | --- |
| Markdown/CommonMark | 无原生数学语法 | 需要依赖目标渲染器扩展。 |
| 正式GFM | 无数学扩展 | 数学公式不是正式GFM的一部分。 |
| GitHub平台 | `$...$`、`$$...$$`和受支持的LaTeX数学命令 | 适合行内和块级数学表达式。 |
| HTML | MathML，或由KaTeX/MathJax等库生成HTML | GitHub不会执行任意JavaScript库。 |
| 完整LaTeX | `equation`、`align`、`gather`等环境 | 支持编号、标签、引用和宏包。 |

HTML MathML示例：

```html
<math xmlns="http://www.w3.org/1998/Math/MathML">
  <msup>
    <mi>x</mi>
    <mn>2</mn>
  </msup>
</math>
```

完整LaTeX交叉引用示例：

```latex
\begin{equation}\label{eq:energy}
E = mc^2
\end{equation}

公式\ref{eq:energy}给出了质能关系。
```
