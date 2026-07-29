# 七、数学公式

[返回文档首页](../README.md)

Markdown和正式GFM规范本身没有定义数学公式。GitHub平台使用美元符号分隔数学内容，并解析其中受支持的LaTeX数学命令。

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

GitHub数学渲染不提供完整LaTeX文档的公式编号和交叉引用能力。`\tag{}`、`\label{}`和`\hfill`的表现可能受限；`&&`和`\hspace{}`只能用于视觉对齐，不能建立真正的编号引用关系。

案例：

```markdown
公式1: `\tag{}` 会乱码

$$E = mc^2  \tag{1} $$

公式2: `\tag{}` 会乱码

$$
\begin{align}
f'(x) = 2ax + b \tag{2} \\
\end{align}
$$

公式3: `\label{}` 在GitHub上不显示

$$
\begin{align}
y5=x5+z5 \label{Za}\\
y6=x6+z6 \notag \\
y7=x7+z7 \label{Zb}
\end{align}
$$

公式4: `&&` 来间隔公式，GitHub支持; `\hfill`在GitHub不支持

$$
\begin{align*}
f(x) &= ax^2 + bx + c && \text{（二次函数）} \\
f'(x) &= 2ax + b \hfill && \text{（一阶导数）} \\
f''(x) &= 2a && \text{（二阶导数）}
\end{align*}
$$

公式5: `\hspace{}`来间隔2个文本，GitHub支持，但不推荐

$$
\begin{align*}
f(x) &= ax^2 + bx + c \hspace{5cm} \text{（二次函数）} \\
f'(x) &= 2ax + b \hspace{5cm} \text{（一阶导数）} \\
f''(x) &= 2a \hspace{5cm} \text{（二阶导数）}
\end{align*}
$$
```

显示效果如下：

> 公式1: `\tag{}` 会乱码
>
> $$E = mc^2  \tag{1} $$
>
> 公式2: `\tag{}` 会乱码
>
> $$
> \begin{align}
> f'(x) = 2ax + b \tag{2} \\
> \end{align}
> $$
>
> 公式3: `\label{}` 在GitHub上不显示
>
> $$
> \begin{align}
> y5=x5+z5 \label{Za}\\
> y6=x6+z6 \notag \\
> y7=x7+z7 \label{Zb}
> \end{align}
> $$
>
> 公式4: `&&` 来间隔公式，GitHub支持; `\hfill`在GitHub不支持
>
> $$
> \begin{align*}
> f(x) &= ax^2 + bx + c && \text{（二次函数）} \\
> f'(x) &= 2ax + b \hfill && \text{（一阶导数）} \\
> f''(x) &= 2a && \text{（二阶导数）}
> \end{align*}
> $$
>
> 公式5: `\hspace{}`来间隔2个文本，GitHub支持，但不推荐
>
> $$
> \begin{align*}
> f(x) &= ax^2 + bx + c \hspace{5cm} \text{（二次函数）} \\
> f'(x) &= 2ax + b \hspace{5cm} \text{（一阶导数）} \\
> f''(x) &= 2a \hspace{5cm} \text{（二阶导数）}
> \end{align*}
> $$

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
