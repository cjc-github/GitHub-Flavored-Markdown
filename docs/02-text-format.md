# 二、文本格式

[返回文档首页](../README.md)


> **显示效果说明**：以下示例中的 `>` 块引用仅为排版用途，实际使用时不需要添加 `>`。

## 2.1 换行

### 2.1.1 Markdown语法实现方式

> **支持层级**：CommonMark（普通换行、新段落）/ GFM（硬换行、反斜杠换行）

Markdown 段落没有特殊的格式，直接编写文字就好。

Markdown 中常见的换行与分段方式如下：

1. **普通换行（隐式）**：在编辑器中直接按 Enter 换行，渲染行为取决于具体平台。
2. **硬换行（显式）**：在行尾添加两个空格后再换行，GFM 支持这种写法。
3. **新段落**：在两段之间添加一个空行，GFM 和 CommonMark 均支持。

> **提示**：两个空格在视觉上不易察觉，下面的示例使用 `··`（两个点）来表示两个空格的位置。实际编写时，请将 `··` 替换为空格。

<br/>

案例：

```markdown
# 方法一：硬换行（行尾两个空格）
段落1··
段落2

# 方法二：普通换行
段落1
段落2

# 方法三：新段落
段落1

段落2
```

<br/>

显示效果如下：

> 方法一：硬换行（行尾添加两个空格 `··`）
>
> 段落1<br>
> 段落2
>
> 方法二：普通换行
>
> 段落1<br>
> 段落2
>
> 方法三：新段落
>
> 段落1
>
> 段落2
>
> 方法四：反斜杠换行
>
> 段落1\
> 段落2

<br/>

### 2.1.2 HTML标签实现方式

HTML 的换行标签可以写成 `<br>`、`<br/>` 或 `<br />`。这些写法在说明文字中必须用反引号包裹，否则 GitHub 会把它们解析为真正的 HTML 标签。`</br>` 不是有效写法，不应使用。

案例：

```markdown
# 方法：标签换行，使用HTML的换行标签<br>、<br/>或<br />。
段落1 <br/> 段落2
```
<br/>

显示效果如下：

> 方法三：标签换行，使用HTML的换行标签`<br>`、`<br/>`或`<br />`。
>
> 段落1 <br/> 段落2


### 2.1.3 LaTeX实现方式

完整LaTeX文档可以使用`\\`、`\newline`和`\par`控制换行与分段。

```latex
第一行\\
第二行\newline
第三行

\par 新的段落
```

`\\`和`\newline`用于强制换行，空行或`\par`用于开始新段落。GitHub中的LaTeX仅用于数学表达式，不能替代Markdown正文换行。


## 2.2 字体格式

字体格式

### 2.2.1 Markdown语法实现方式

**粗体语法：** 使用两个星号 `**` 或两个下划线 `__` 包围文字：

案例：

```markdown
这是**粗体文字**使用星号
这是 __粗体文字__ 使用下划线
```

显示效果如下：

> 这是**粗体文字**使用星号
>
> 这是 __粗体文字__ 使用下划线

<br/>

**斜体语法：** 使用一个星号 `*` 或一个下划线 `_` 包围文字：

案例：

```markdown
这是*斜体文字*使用星号
这是 _斜体文字_ 使用下划线
```

显示效果如下：

> 这是*斜体文字*使用星号
>
> 这是 _斜体文字_ 使用下划线

<br/>

**粗斜体组合：** 使用三个星号 `***` 或三个下划线 `___` 包围文字：

案例：

```markdown
这是*斜体文本*使用星号
这是 _斜体文本_ 使用下划线

这是**粗体文本**使用星号
这是 __粗体文本__ 使用下划线

这是***粗斜体文本***使用星号
这是 ___粗斜体文本___ 使用下划线
```

<br/>

显示效果如下：

> 这是*斜体文本*使用星号
>
> 这是 _斜体文本_ 使用下划线
>
> 这是**粗体文本**使用星号
>
> 这是 __粗体文本__ 使用下划线
>
> 这是***粗斜体文本***使用星号
>
> 这是 ___粗斜体文本___ 使用下划线

强调标记会根据标记两侧的字符判断是否可以打开或关闭。下划线通常不能在单词内部创建强调，而星号更适合包围连续文本；标记还可以嵌套，但必须成对出现。

```markdown
*普通斜体*，**普通粗体**，***粗斜体***
文本中的 a_b_c 通常不会形成下划线强调
文本中的 a*b*c 可以按星号边界解析
**粗体中的*斜体***
```

<br/>


**注意事项**

原始Markdown规范支持 `__粗体__` 语法，但CommonMark（现代标准）中，`__粗体__` 的解析规则比 `**粗体**` 更严格。

根据CommonMark规范，`__粗体__` 语法需要满足:

1. 不能紧邻其他字母/数字（即需要被非单词字符包围）；

2. 单词边界规则：下划线需要被空格、标点、行首/行尾等包围；

<br/>

案例：

```markdown
文本__粗体__文本（无效规则）
文本 __粗体__ 文本（有效规则，前后为空格）
__粗体__。（有效规则，前为行首，后为标点）
1__粗体__2（无效规则）
a__粗体__b（无效规则）
```

<br/>

显示效果如下：

> 文本__粗体__文本（无效规则）
>
> 文本 __粗体__ 文本（有效规则）
>
> __粗体__。（有效规则）
>
> 1__粗体__2（无效规则）
>
> a__粗体__b（无效规则）

<br/>

因此，在设置字体的粗体、斜体时**推荐**使用星号语法。如果使用下划线时，可以在下划线前后加上空格，标点，行首/行尾等。

<br/>

### 2.2.2 HTML标签实现方式

HTML也可以实现上述效果，`<b>`标签和`<strong>`标签效果相同，都是粗体，`<i>`标签和`<em>`标签效果相同，都是斜体。

案例：

```markdown
这是<b>粗体文本</b>
这是<strong>粗体文本</strong>
这是<i>斜体文本</i>
这是<em>斜体文本</em>
这是<b><i>粗斜体文本</i></b>
```

显示效果如下：

> 这是<b>粗体文本</b>
>
> 这是<strong>粗体文本</strong>
>
> 这是<i>斜体文本</i>
>
> 这是<em>斜体文本</em>
>
> 这是<b><i>粗斜体文本</i></b>

<br/>

### 2.2.3 LaTeX实现方式

LaTeX提供了粗体、斜体、强调和等宽字体命令。

```latex
\textbf{粗体文本}
\textit{斜体文本}
\emph{强调文本}
\textbf{\textit{粗斜体文本}}
\texttt{等宽文本}
```

在GitHub数学公式中可以使用`\mathbf{}`、`\mathit{}`和`\mathtt{}`设置数学字符样式，但它们不等同于完整LaTeX正文排版。


## 2.3 删除线

### 2.3.1 Markdown语法实现方式

**删除线语法：** 使用两个波浪号 **~~** 包围文字：

删除线不是CommonMark基础语法，而是正式GFM扩展。

案例：

```markdown
这是~~删除线~~使用波浪号
```

显示效果如下：

> 这是~~删除线~~使用波浪号

<br/>

### 2.3.2 HTML标签实现方式

HTML中有多种标签可以实现删除效果：

| 标签 | 语义 | 建议 |
| --- | --- | --- |
| `<del>` | 表示内容被删除 | GFM 推荐使用 |
| `<s>` | 表示内容不再准确或不再适用 | 语义有区别 |

> **注意**：`~~文本~~` 是 GFM 推荐语法；`<del>` 和 `<s>` 在 GitHub 中渲染效果可能相同，但语义不同。

案例：

```markdown
这是<del>被删除的内容</del>
这是<s>不再适用的内容</s>
```

显示效果如下：

> 这是<del>被删除的内容</del>
>
> 这是<s>不再适用的内容</s>

<br/>

### 2.3.3 LaTeX实现方式

完整LaTeX文档可以使用`ulem`宏包的`\sout{}`命令删除普通文本。

```latex
\usepackage[normalem]{ulem}

这是\sout{删除线文本}。
```

数学表达式常使用`cancel`宏包：

```latex
\usepackage{cancel}

$\cancel{x + 1}$
```

GitHub数学公式支持范围不是完整LaTeX环境，不能加载任意宏包；普通文本删除线应优先使用GFM的`~~文本~~`。

## 2.4 下划线和上划线

### 2.4.1 Markdown语法实现方式

CommonMark和正式GFM都没有定义普通文本的下划线或上划线语法。

### 2.4.2 HTML标签实现方式

HTML可以使用`<u>`表示无语义下划线，使用`<ins>`表示插入的内容。GitHub会对原始HTML进行过滤，跨平台文档更推荐使用`<ins>`并实际预览。

<br/>

案例：

```markdown
# 方法一
这是 <u>下划线</u> 使用`<u>`标签
# 方法二
这是 <ins>下划线</ins> 使用`<ins>`标签

注意：这些写法属于HTML，不属于GFM语法。
```
<br/>

显示效果如下：

> 这是 <u>下划线</u> 使用`<u>`标签
>
> 这是 <ins>下划线</ins> 使用`<ins>`标签
>
> 这是 $\underline{下划线}$ 使用`$\underline{下划线}$`LaTeX公式实现

<br/>

### 2.4.3 LaTeX实现方式

LaTeX公式使用 `$\underline{}` 和 `$\overline{}` 实现下划线和上划线的渲染。

案例：

```markdown
# 方法一
这是 $\underline{下划线}$ 使用`$\underline{下划线}$`LaTeX公式实现

这是 $\overline{上划线}$ 使用`$\overline{上划线}$`LaTeX公式实现
```
<br/>

显示效果如下：

> 这是 $\underline{下划线}$ 使用`$\underline{下划线}$`LaTeX公式实现
>
> 这是 $\overline{上划线}$ 使用`$\overline{上划线}$`LaTeX公式实现

<br/>

注意事项：

1. 在使用 `LaTeX` 的 `\underline{}` 和 `\overline{}` 命令来显示下划线和上划线时，可能会出现划线不完整的显示异常；

2. GitHub数学渲染仅支持部分LaTeX数学命令，不能加载`mathtools`等任意宏包；

<br/>

案例：

```markdown
$\underline{\underline{双下划线文本}}$
$\underline{\underline{\underline{三下划线文本}}}$
$\underbrace{这是大括号下划线}$
$\underleftarrow{这是左箭头下划线}$
$\underrightarrow{这是左箭头下划线}$
$\underleftrightarrow{这是左右箭头下划线}$
$\underline{\text{这是大括号下划线}}$
$$\underline{\text{这是下划线公式}}$$
```

<br/>

显示效果如下：

> $\underline{\underline{双下划线文本}}$
>
> $\underline{\underline{\underline{三下划线文本}}}$
>
> $\underbrace{这是大括号下划线}$
>
> $\underleftarrow{这是左箭头下划线}$
>
> $\underrightarrow{这是左箭头下划线}$
>
> $\underleftrightarrow{这是左右箭头下划线}$
>
> $\underline{\text{这是大括号下划线}}$
>
> $$\underline{\text{这是下划线公式}}$$

## 2.5 上下标

### 2.5.1 Markdown语法实现方式

CommonMark和正式GFM没有定义`^上标^`或`~下标~`语法，下面的写法仅在Typora等部分编辑器中有效。

案例：

```markdown
这是^上标^显示

这是~下标~显示

总结：
部分Markdown编辑器（如Typora）支持
```
<br/>

显示效果如下：

> 这是^上标^显示
>
> 这是~下标~显示


<br/>

### 2.5.2 HTML标签实现方式

HTML中使用`<sup>`标签来实现上标、使用`<sub>`标签来实现下标。

案例：

```markdown
这是<sup>上标</sup>显示

这是<sub>下标</sub>显示
```
<br/>

显示效果如下：


> 这是<sup>上标</sup>显示
>
> 这是<sub>下标</sub>显示

<br/>


### 2.5.3 LaTeX实现方式


LaTeX中使用`^{text}`命令来实现上标显示，使用`_{text}`命令来实现下标显示

案例：

```markdown
$这是^{上标}显示$

$这是_{下标}显示$
```
<br/>

显示效果如下：

> $这是^{上标}显示$
>
> $这是_{下标}显示$

<br/>


## 2.6 分割线

### 2.6.1 Markdown语法实现方式


**分割线：** 在单独一行上使用三个或多个星号（`***`）、破折号（`---`）或下划线（`___`）。分隔字符之间可以有空格，整行最多允许缩进三个空格，但不能混用不同字符。

案例：

```markdown
---
***
___
  - - -
*** ***
```

显示效果如下：

> ---
>
> ***
>
> ___
>  - - -
> *** ***

如果分隔线写在段落、列表或标题语境中，解析结果可能受到前后内容影响。例如，`---`紧跟在一段文字后面可能被解析为Setext二级标题，而不是分割线；要明确表示分割线，建议前后各保留一个空行。


### 2.6.2 HTML标签实现方式

HTML中使用 `<hr>` 标签来实现分割线，hr全程为（Horizontal Rule，水平分割线）

案例：

```markdown
段落A
<hr>
段落B
```

显示效果如下：

> 段落A
> <hr>
> 段落B

### 2.6.3 LaTeX实现方式

LaTeX中使用`\rule`命令来绘制分割线

`\rule`命令的格式如下：

```text
\rule[lift]{width}{height}
lift‌（可选）：指定矩形基线相对于当前文本基线的垂直偏移量。正值向上抬升，负值向下降低。默认为 0pt。
‌width‌：矩形的宽度。
‌height‌：矩形的高度。
```

案例：

```markdown

段落A

$\rule{33cm}{0.5pt}$

段落B
```
<br/>

显示效果如下：

> 段落A
>
> $\rule{33cm}{0.5pt}$
>
> 段落B


<br/>


## 2.7 脚注

脚注：脚注是对文本的补充说明

### 2.7.1 Markdown语法实现方式

CommonMark和正式GFM规范都没有定义脚注语法，但GitHub平台、Typora和部分编辑器支持相似的脚注扩展，核心是「脚注标记 + 脚注内容」的组合。

在GitHub支持脚注的页面中，脚注定义的位置通常不影响最终显示位置，GitHub会将脚注内容集中到页面末尾。脚注支持范围可能因仓库Markdown文件、Issue、Pull Request、Discussion、评论和Wiki而不同，应以目标页面的实际渲染结果为准；不要把脚注语法当作CommonMark或正式GFM语法。

<br/>

案例：

```markdown
这是一个脚注[^note]。

[^note]: 这是带标签的脚注内容。
    脚注内容可以有多行，需要缩进。
    这是脚注的第二行。
```

<br/>

显示效果如下：

> 这是一个脚注[^note]。
>
> [^note]: 这是带标签的脚注内容。
>    脚注内容可以有多行，需要缩进。
>    这是脚注的第二行。

<br/>

### 2.7.2 HTML标签实现方式

HTML可以通过`<sup>`和锚点链接`<a>`手动实现脚注，分为正文标记和脚注内容两部分。这是HTML实现方式，不属于正式GFM脚注语法。


```markdown
<p>地铁车厢里的大风主要来自隧道活塞效应<sup id="ref1"><a href="#fn1">1</a></sup>，其次是空调通风系统<sup id="ref2"><a href="#fn2">2</a></sup>。</p>

<div id="footnotes">
  <h3>脚注</h3>
  <ol>
    <li id="fn1">
      活塞效应指列车在隧道中高速行驶时，像活塞一样挤压空气形成的强气流，是车厢大风的核心来源。
      <a href="#ref1">↩</a> <!-- 返回正文锚点 -->
    </li>
    <li id="fn2">
      空调系统会持续向车厢送入新风，形成稳定的背景风，风感相对柔和。
      <a href="#ref2">↩</a>
    </li>
  </ol>
</div>
```

显示效果如下：

> <p>地铁车厢里的大风主要来自隧道活塞效应<sup id="ref1"><a href="#fn1">1</a></sup>，其次是空调通风系统<sup id="ref2"><a href="#fn2">2</a></sup>。</p>
>
> <div id="footnotes">
>  <h3>脚注</h3>
>  <ol>
>   <li id="fn1">
>    活塞效应指列车在隧道中高速行驶时，像活塞一样挤压空气形成的强气流，是车厢大风的核心来源。
> ​      <a href="#ref1">↩</a> <!-- 返回正文锚点 -->
>   </li>
>   <li id="fn2">
>    空调系统会持续向车厢送入新风，形成稳定的背景风，风感相对柔和。
> ​      <a href="#ref2">↩</a>
>   </li>
>  </ol>
> </div>

<br/>

### 2.7.3 LaTeX实现方式

完整LaTeX文档提供原生的`\footnote{}`命令，编译后会自动编号并将脚注放在页面底部。GitHub数学公式不会执行正文脚注命令。

案例：

```latex
地铁车厢里的大风主要来自隧道活塞效应\footnote{活塞效应是车厢大风的核心来源。}，其次是空调通风系统\footnote{空调系统会形成稳定的背景风。}。
```

<br/>

## 2.8 高亮

> **支持层级**：不属于 CommonMark 或 GFM，是部分第三方编辑器的扩展语法。GitHub 不会将 `==文本==` 渲染为高亮。

CommonMark 和正式 GFM 都没有定义普通文本高亮语法。围栏代码块的语法高亮由渲染平台根据语言标识符提供，与此处的文本高亮不同。

### 2.8.1 Markdown语法实现方式

部分编辑器（如 Typora）支持 `==文本==` 扩展语法，但该语法不属于 GFM，在 GitHub 中不会渲染为高亮。

案例：

```markdown
这是==高亮文本==  # 部分编辑器支持，GitHub 不支持
```

显示效果如下：

> 这是==高亮文本==  # GitHub 不会高亮显示

显示效果如下：

> 这是==高亮文本==
<br/>


### 2.8.2 HTML标签实现方式

HTML中使用`<mark>`标签来实现高亮。

案例：

```markdown
这是<mark>高亮文本</mark>
```

显示效果如下：

> 这是<mark>高亮文本</mark>

<br/>


### 2.8.3 LaTeX实现方式

完整LaTeX文档可以使用`soul`宏包的`\hl{}`命令高亮普通文本。

案例：

```latex
\usepackage{soul}

这是\hl{高亮文本}。
```

GitHub数学公式不能加载`soul`宏包，因此该示例不适用于GitHub正文。

<br/>

## 2.9 行内代码标记

行内代码是指在文本中嵌入简短的代码片段，通常用于展示函数、变量、命令等内容。

### 2.9.1 Markdown语法实现方式

Markdown使用用单个反引号 ` 包裹代码来实现行内代码

案例：

```markdown
这是`行内代码标记`
```

显示效果如下：

> 这是`行内代码标记`

<br/>

### 2.9.2 HTML标签实现方式

HTML中使用 `<code>` 标签包裹代码来实现行内代码

案例：

```markdown
<code>行内代码标记</code>
```

显示效果如下：

> 这是<code>行内代码标记</code>

<br/>

### 2.9.3 LaTeX实现方式

LaTeX可以使用`\texttt{}`或`\verb`显示行内代码。

```latex
调用\texttt{print()}函数。

运行命令\verb|git status|查看状态。
```

`\verb`适合包含大量特殊字符的短代码，但不能直接出现在某些命令参数中。

<br/>

## 2.10 块引用

### 2.10.1 Markdown语法实现方式

Markdown语法：每行开头加 >（多层嵌套可叠加 >>）

块引用可以跨越多行和多个段落。段落中的普通续行有时可以省略 `>`，这种写法称为惰性续行；为了避免不同渲染器产生差异，建议每一行都保留引用标记。

案例：

```markdown
下面是块引用
> 块引用内容
>> 二级块引用内容
```

显示效果如下：

> 下面是块引用
>
> > 块引用内容
> >
> > > 二级块引用内容

<br/>

多段落和惰性续行示例：

```markdown
> 第一段的第一行
第一段的第二行
>
> 第二段内容
```

显示效果如下：

> > 第一段的第一行
> 第一段的第二行
> >
> > 第二段内容

普通续行通常会按同一段落显示为连续文本；如果需要页面中明确换行，应在第一行末尾添加两个空格或使用反斜杠。



注意：

1. 块引用支持嵌套使用，为了更好地凸显出显示效果，本文档中的所有显示效果均在块引用中展示。
2. Alerts不支持在块引用显示。

#### GitHub平台的Alerts

GitHub提供了基于块引用的Alerts扩展，用于高亮提示、警告和重要信息。Alerts属于GitHub平台功能，不属于正式GFM规范，并且部分Markdown编辑器（如Typora）不支持。

案例：

```markdown
> [!NOTE]
> Highlights information that users should take into account, even when skimming.
>
> 突出显示用户应该考虑的信息，即使在略读时也是如此。

> [!TIP]
> Optional information to help a user be more successful.
>
> 可选信息，帮助用户更成功。

> [!IMPORTANT]
> Crucial information necessary for users to succeed.
>
> 用户成功所需的关键信息。

> [!WARNING]
> Critical content demanding immediate user attention due to potential risks.
>
> 由于潜在风险需要用户立即关注的关键内容。

> [!CAUTION]
> Negative potential consequences of an action.
>
> 一个动作的负面潜在后果。
```

<br/>

显示效果如下：

> [!NOTE]
> Highlights information that users should take into account, even when skimming.
>
> 突出显示用户应该考虑的信息，即使在略读时也是如此。

> [!TIP]
> Optional information to help a user be more successful.
>
> 可选信息，帮助用户更成功。

> [!IMPORTANT]
> Crucial information necessary for users to succeed.
>
> 用户成功所需的关键信息。

> [!WARNING]
> Critical content demanding immediate user attention due to potential risks.
>
> 由于潜在风险需要用户立即关注的关键内容。

> [!CAUTION]
> Negative potential consequences of an action.
>
> 一个动作的负面潜在后果。

<br/>

### 2.10.2 HTML标签实现方式

HTML使用 `<blockquote>` 标签包裹内容（可嵌套）来实现块引用

案例：

```markdown
<blockquote>
  地铁活塞效应：列车在隧道中高速行驶时，像活塞一样挤压空气形成强气流。
  <blockquote>补充：隧道越窄，活塞效应越显著。</blockquote>
</blockquote>
```

显示效果如下：

> <blockquote>
>   地铁活塞效应：列车在隧道中高速行驶时，像活塞一样挤压空气形成强气流。
>   <blockquote>补充：隧道越窄，活塞效应越显著。</blockquote>
> </blockquote>

<br/>

### 2.10.3 LaTeX实现方式

完整LaTeX文档使用`quote`或`quotation`环境实现块引用。它们是正文环境，不能放在数学公式分隔符`$$...$$`内部。

案例：

```latex
% 基础引用
\begin{quote}
地铁活塞效应：列车在隧道中高速行驶时，像活塞一样挤压空气形成强气流。
\end{quote}

% 嵌套引用
\begin{quotation}
核心结论：活塞效应是车厢大风的主要来源。
\begin{quote}补充：风速可达列车速度的0.6~0.8倍。\end{quote}
\end{quotation}
```

GitHub数学公式不会渲染这些正文环境。

<br/>

## 2.11 代码块


### 2.11.1 Markdown语法实现方式

代码块使用围栏式语法显示。围栏可以由三个或更多连续的反引号（`` ` ``）或波浪线（`~`）组成。开始围栏和结束围栏必须使用相同的字符；结束围栏的长度不能短于开始围栏，且结束围栏后不能再添加语言标识符。

开始围栏最多可以缩进三个空格。开始围栏后可以添加可选的 info string，通常将其第一个单词作为语言标识符，以便GitHub为代码块启用语法着色。语言标识符只影响显示方式，不会改变代码内容或执行代码。

围栏代码块中的内容不会继续解析Markdown语法，直到遇到有效的结束围栏。代码块内容中的反引号、波浪线、标题、链接和HTML标签都会按代码原样显示。

注意：如果代码内容中包含三个反引号，可以改用波浪线围栏，或使用长度更长的反引号围栏。

案例：

`````markdown
# 普通代码块
```
这是代码块
```

# 指定c语言的语言标识符
```c
printf("hello world!");
printf("hello world!");
```

# 波浪线围栏
~~~python
print("hello world!")
~~~

# 更长的反引号围栏可以包裹代码中的三个反引号
````
代码中的 ``` 不会结束这个代码块。
````

# 代码内容不会解析Markdown
```
# 这不是标题
[这不是链接](https://example.com)
<span>这不是HTML标签</span>
```
`````

显示效果如下：

> 普通代码块
> ```text
> 这是代码块
> ```
>
> 指定c语言的语言标识符
> ```c
> printf("hello world!");
> printf("hello world!");
> ```
>
> 波浪线围栏和反引号围栏的作用相同：
> ~~~python
> print("hello world!")
> ~~~
>
> 代码内容不会解析Markdown语法，而是原样显示：
> ```text
> # 这不是标题
> [这不是链接](https://example.com)
> <span>这不是HTML标签</span>
> ```

<br/>


#### 差异显示-diff语法

差异显示是代码审查中的重要功能，使用 `diff` 语言标识符。

具体实现如8.2节。

### 2.11.2 HTML标签实现方式

HTML使用`<pre>+<code>` 标签组合实现代码块渲染

案例：

````markdown
<pre><code>def calc_pressure(rho, v):
 return 0.5 * rho * v**2
</code></pre>
````

显示效果如下：

> <pre><code>def calc_pressure(rho, v):
>  return 0.5 * rho * v**2
> </code></pre>

<br/>

### 2.11.3 LaTeX实现方式

LaTeX使用`verbatim`环境显示保留空格和特殊字符的代码块。

```latex
\begin{verbatim}
def hello():
    print("Hello, world!")
\end{verbatim}
```

需要语法高亮时可以使用`listings`或`minted`宏包。GitHub代码块应使用Markdown围栏语法。

## 2.12 字体颜色

### 2.12.1 Markdown语法实现方式

Markdown不支持对字体颜色修改

<br/>

### 2.12.2 HTML标签实现方式


HTML中存在多种样式来显示字体颜色：

1. 使用HTML中`<font>`标签, GFM不支持
2. 使用HTML中的`<span>`标签, GFM不支持
3. 使用HTML中的`<div>`标签, GFM不支持

<br/>

> **颜色支持**
>
> - 颜色名：例如 `red`
> - RGB 颜色：例如 `rgb(255, 0, 0)`
> - 十六进制颜色值：例如 `#FF0000`

<br/>

> **仅适用于独立 HTML 页面**：GitHub 会过滤 `style`、`color` 等属性，不应依赖自定义颜色。

案例：

```markdown
这是<font color="red">红色</font>

这是<span style="color:rgb(255, 0, 0)">红色</span>

<div style="color: red;">
  这是一个字体为红色的块，可以包含多行文本。
</div>
```

<br/>

显示效果如下：

> 这是<font color="red">红色</font>
>
> 这是<span style="color:rgb(255, 0, 0)">红色</span>
>
> <div style="color: red;">
>   这是一个字体为红色的块，可以包含多行文本。
> </div>

<br/>

### 2.12.3 LaTeX实现方式

LaTeX支持使用`color`或`textcolor`命令来实现文本颜色

案例：

```markdown
这是 $\color{#FF0000}{\mathtt{红色}}$

这是 $\textcolor{red}{\mathtt{红色}}$
```

显示效果如下：

> 这是 $\color{#FF0000}{\mathtt{红色}}$
>
> 这是 $\textcolor{red}{\mathtt{红色}}$

<br/>

## 2.13 背景颜色


### 2.13.1 Markdown语法实现方式

Markdown语法不支持为字体提供背景颜色，但是部分Markdown编辑器（如Typora）支持的扩展高亮语法 `==文本==`, GFM不支持

案例：

```markdown
这是 ==背景为红色==
```

<br/>

显示效果如下：

> 这是 ==背景为红色==

<br/>

### 2.13.2 HTML标签实现方式

HTML中存在多种样式来显示字体背景颜色：

1. 使用HTML中`<font>`标签, GFM不支持
2. 使用HTML中的`<span>`标签, GFM不支持
3. 使用HTML中的`<div>`标签, GFM不支持
4. 使用HTML中的`<mark>`标签，GFM不支持修改颜色

<br/>

案例：

```markdown
这是 <font style="background: red"> 背景为红色</font>

这是 <span style="background-color: red"> 背景为红色</span>

<div style="background: red;">
  这是一个有背景色的块，可以包含多行文本。
</div>

这是<mark>背景默认为黄色</mark>

这是<mark style="background-color: #ff4444; color: #ffffff;">背景为红色</mark>

```

<br/>

显示效果如下：

> 这是 <font style="background: red"> 背景为红色</font>
>
> 这是 <span style="background-color: red"> 背景为红色</span>
>
> <div style="background: red;">
>   这是一个有背景色的块，可以包含多行文本。
> </div>
>
> 这是<mark>背景默认为黄色</mark>
>
> 这是<mark style="background-color: #ff4444; color: #ffffff;">背景为红色</mark>


注意：独立HTML页面可以通过CSS修改颜色，但GitHub会过滤`style`等属性。GitHub文档中不应依赖自定义前景色或背景色。

### 2.13.3 LaTeX实现方式

完整LaTeX文档可以使用`xcolor`宏包的`\colorbox`或`\fcolorbox`设置文本背景。

```latex
\usepackage{xcolor}

这是\colorbox{yellow}{黄色背景}。

这是\fcolorbox{red}{yellow}{红色边框和黄色背景}。
```

GitHub不允许在Markdown中加载`xcolor`宏包，因此该方式主要适用于独立LaTeX文档。


<br/>
