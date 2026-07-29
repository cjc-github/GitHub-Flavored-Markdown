# 六、表格

[返回文档首页](../README.md)

## 6.1 Markdown与GFM实现方式

表格不是CommonMark基础语法，而是正式GFM扩展。使用`|`分隔单元格，使用连字符分隔表头与数据行。

语法规则：

1. 表头和数据行之间必须存在分隔行。
2. 每个分隔单元至少需要三个连字符。
3. 两端竖线可以省略，但保留后更容易阅读。
4. `:---`表示左对齐，`---:`表示右对齐，`:---:`表示居中。

```markdown
| 项目 | 状态 | 进度 |
| :--- | :---: | ---: |
| 文档 | 进行中 | 80% |
| 测试 | 已完成 | 100% |
```

显示效果如下：

> | 项目 | 状态 | 进度 |
> | :--- | :---: | ---: |
> | 文档 | 进行中 | 80% |
> | 测试 | 已完成 | 100% |

GFM表格不支持跨行或跨列合并，复杂布局需要使用HTML或图片。

## 6.2 HTML实现方式

HTML使用`<table>`、`<thead>`、`<tbody>`、`<tr>`、`<th>`和`<td>`创建表格，并可以通过`rowspan`、`colspan`合并单元格。

```html
<table>
  <thead>
    <tr>
      <th rowspan="2">功能模块</th>
      <th colspan="2">开发进度</th>
    </tr>
    <tr>
      <th>前端</th>
      <th>后端</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>用户管理</td>
      <td>100%</td>
      <td>90%</td>
    </tr>
  </tbody>
</table>
```

GitHub会过滤自定义CSS，因此不应依赖`style`实现复杂表格样式。

## 6.3 LaTeX实现方式

LaTeX使用`tabular`环境创建表格，`l`、`c`、`r`分别表示左对齐、居中和右对齐。

```latex
\begin{tabular}{lcr}
\hline
项目 & 状态 & 进度 \\
\hline
文档 & 进行中 & 80\% \\
测试 & 已完成 & 100\% \\
\hline
\end{tabular}
```

复杂表格可以使用`booktabs`、`longtable`和`multirow`等宏包。GitHub数学公式不适合渲染完整`tabular`环境。
