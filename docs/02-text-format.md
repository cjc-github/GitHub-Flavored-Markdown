# 二、文本格式

[返回文档首页](../README.md)

## 2.1 换行

### 2.1.1 Markdown语法实现方式

Markdown 段落没有特殊的格式，直接编写文字就好。

换行存在以下方法：

1. 硬换行：在行尾添加两个以上空格再换行，GFM支持
2. 软换行：在段落间添加一个空行，推荐
3. 反斜杠换行：在行尾添加反斜杠再换行，GFM支持

<br/>

案例：

```markdown
# 方法一：行尾添加两个空格
段落1  # 这里添加2个空格
段落2

# 方法二：软换行
段落1 # 换行

段落2

# 方法三，反斜杠换行
段落1\
段落2
```

<br/>

显示效果如下：

> 方法一：硬换行
>
> 段落1  # 这里添加2个空格
> 段落2
>
> 方法二：软换行
>
> 段落1 # 换行
>
> 段落2
>
> 方法三，反斜杠换行
>
> 段落1\
> 段落2

<br/>

### 2.1.2 HTML标签实现方式

标签换行：使用HTML的换行标签<br>，<br/> 或 <br />

案例：

```markdown
# 方法：标签换行，使用HTML的换行标签<br>，<br/>, </br>或<br />。
段落1 <br/> 段落2
```
<br/>

显示效果如下：

> 方法三：标签换行，使用HTML的换行标签`<br>`，`<br/>`, `</br>` 或 `<br />`。
>
> 段落1 </br> 段落2


### 2.1.3 LaTeX公式实现方式

暂无


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

### 2.2.3 LaTeX公式实现方式

暂无


## 2.3 删除线

### 2.3.1 Markdown语法实现方式

**删除线语法：** 使用两个波浪号 **~~** 包围文字：

案例：

```markdown
这是~~删除线~~使用波浪号
```

显示效果如下：

> 这是~~删除线~~使用波浪号

<br/>

### 2.3.2 HTML标签实现方式

**删除线语法：** 使用`<del>`标签包围文字：

案例：

```markdown
这是<del>删除线</del>使用波浪号
```

显示效果如下：

> 这是<del>删除线</del>使用波浪号

<br/>

### 2.3.3 LaTeX公式实现方式

暂无

## 2.4 下划线和上划线

### 2.4.1 Markdown语法实现方式

Markdown语法不支持下划线和上划线显示

### 2.4.2 HTML标签实现方式

**下划线语法：** Markdown自身没有实现下划线，但支持HTML的`<u>`标签来实现。

然而，传统的Markdown下划线语法`<u>`标签在GitHub的Markdown文件中不生效，应该使用`<ins>`标签或者LaTeX公式实现。

<br/>

案例：

```markdown
# 方法一
这是 <u>下划线</u> 使用`<u>`标签
# 方法二
这是 <ins>下划线</ins> 使用`<ins>`标签

注意：GFM只支持方法二来显示下划线
```
<br/>

显示效果如下：

> 这是 <u>下划线</u> 使用`<u>`标签
>
> 这是 <ins>下划线</ins> 使用`<ins>`标签
>
> 这是 $\underline{下划线}$ 使用`$\underline{下划线}$`LaTeX公式实现

<br/>

### 2.4.3 LaTeX公式实现方式

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

2. 在 GitHub Flavored Markdown (GFM) 中使用 `LaTeX` 时，某些需要额外 `LaTeX` 包的划线命令无法正常渲染，例如 `\underbracket{}` 命令需要mathtools包, 但是GFM不支持；

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


### 2.5.3 LaTeX公式实现方式


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


**分割线：** 在单独一行上使用三个或多个星号（`***`）、破折号（`---`）或下划线（`___`），并且不能包含其他内容。

案例：

```markdown
---
***
___
```

显示效果如下：

> ---
> 
> ***
> 
> ___


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

### 2.6.3 LaTeX公式实现方式

LaTeX中使用`\rule`命令来绘制分割线

`\rule`命令的格式如下：

```
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

Markdown 没有官方统一的脚注标准，但绝大多数主流编辑器 / 平台（如 Typora、GitHub、VS Code）都支持 GFM (GitHub Flavored Markdown) 风格的脚注语法，核心是「脚注标记 + 脚注内容」的组合。GFM支持这种渲染。

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

HTML 主要通过 `<sup>`（上标）+ 锚点链接 `<a>` 实现脚注，分「正文标记」和「脚注内容」两部分。GFM支持这种渲染。


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

### 2.7.3 LaTeX公式实现方式

LaTeX 提供原生的 `\footnote{}` 命令，用法最简单，编译后会自动编号并将脚注放在当前页面底部。但是GFM不支持渲染。

案例：

```markdown
地铁车厢里的大风主要来自隧道活塞效应$\footnote{活塞效应指列车在隧道中高速行驶时，像活塞一样挤压空气形成的强气流，是车厢大风的核心来源。}$，其次是空调通风系统$\footnote{空调系统会持续向车厢送入新风，形成稳定的背景风，风感相对柔和。}$。
```

显示效果如下：

> 地铁车厢里的大风主要来自隧道活塞效应$\footnote{活塞效应指列车在隧道中高速行驶时，像活塞一样挤压空气形成的强气流，是车厢大风的核心来源。}$，其次是空调通风系统$\footnote{空调系统会持续向车厢送入新风，形成稳定的背景风，风感相对柔和。}$。

<br/>

## 2.8 高亮

Markdown 本身没有官方的「文本高亮」语法，但不同平台（如 GitHub、Typora、Obsidian）有通用的扩展语法；代码块高亮则是 GFM（GitHub Flavored Markdown）的核心特性。

## 2.8.1 Markdown语法实现方式

主流平台通用的是 ==高亮文本== 语法

案例：

```markdown
# 方法一：扩展, GFM不支持，但Typora等Markdown编辑器支持
这是==高亮文本==
```

显示效果如下：

> 这是==高亮文本==
<br/>


## 2.8.2 HTML标签实现方式

HTML中使用`<mark>`标签来实现高亮。

案例：

```markdown
这是<mark>高亮文本</mark>
```

显示效果如下：

> 这是<mark>高亮文本</mark>

<br/>


## 2.8.3 LaTeX公式实现方式

LaTeX中的文本高亮依赖 `soul` 宏包（\hl{}）, 但GFM不支持。

案例：

```markdown
这是$\hl{高亮文本}$
```

显示效果如下：

> 这是$\hl{高亮文本}$

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

### 2.9.3 LaTeX公式实现方式

LaTeX中存在`\texttt{}`，`\verb{}`命令来区别其他文本，但无法达到上述效果的行内代码标记渲染。

<br/>

## 2.10 块引用

### 2.10.1 Markdown语法实现方式

Markdown语法：每行开头加 >（多层嵌套可叠加 >>）

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

### 2.10.3 LaTeX公式实现方式

LaTeX使用`quote`，`quotation`来实现块引用，但GFM不支持。

案例：

```markdown
% 基础引用
$$\begin{quote}
地铁活塞效应：列车在隧道中高速行驶时，像活塞一样挤压空气形成强气流。
\end{quote}$$

% 嵌套引用
$$\begin{quotation}
核心结论：活塞效应是车厢大风的主要来源。
\begin{quote}补充：风速可达列车速度的0.6~0.8倍。\end{quote}
\end{quotation}$$
```


显示效果如下：

> % 基础引用
> $$\begin{quote}
> 地铁活塞效应：列车在隧道中高速行驶时，像活塞一样挤压空气形成强气流。
> \end{quote}$$
>
> % 嵌套引用
> $$\begin{quotation}
> 核心结论：活塞效应是车厢大风的主要来源。
> \begin{quote}补充：风速可达列车速度的0.6~0.8倍。\end{quote}
> \end{quotation}$$

<br/>

## 2.11 代码块


### 2.11.1 Markdown语法实现方式

代码块使用三个反引号（即```）来显示。这种的代码块方式被称为围栏式代码块，在这种围栏式代码块中，可以指定一个可选的语言标识符，在指定后，可以为代码块启动语法着色功能。

注意：在代码块中想显示代码块符号的话，可以使用四个反引号（即````）来包裹。

案例：

````markdown
# 普通代码块
```
这是代码块
```

# 指定c语言的语言标识符
```c
printf("hello world!");
printf("hello world!");
```
````

显示效果如下：

> 普通代码块
> ```
> 这是代码块
> ```
>
> 指定c语言的语言标识符
> ```c
> printf("hello world!");
> printf("hello world!");
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

### 2.11.3 LaTeX公式实现方式

LaTeX中存在`verbatim`来实现代码块，但GFM不支持。

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

注意：颜色支持

```markdown
颜色名: 例如red
rgb颜色: 例如rgb(255, 0, 0)
十六进制颜色值: #FF0000
```

<br/>

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

### 2.12.3 LaTeX公式实现方式

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


注意：在HTML中支持对mark进行背景和字体颜色进行修改，但是GFM似乎采用默认的样式，无法进行配置。


<br/>
