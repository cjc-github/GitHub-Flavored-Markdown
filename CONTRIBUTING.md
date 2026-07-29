# 贡献指南

感谢你帮助完善这份GitHub Flavored Markdown参考文档。

## 修改范围

- 修正无法渲染、描述不准确或已经失效的示例。
- 补充GFM、GitHub平台功能、HTML或LaTeX相关说明时，明确标注所属层次。
- 新增图片、音频或视频时，优先使用仓库内相对路径，并控制资源体积。
- 不要把特定编辑器扩展描述为GFM标准语法。

## 本地检查

仓库根目录下运行：

```powershell
python material/parser_entities.py --check
python scripts/check_local_links.py
python -m unittest discover -s tests -v
npx --yes markdownlint-cli2@0.18.1 README.md CONTRIBUTING.md "docs/*.md" "material/*.md"
```

如果修改了`material/entities.json`，重新生成实体文档：

```powershell
python material/parser_entities.py
```

## 提交建议

- 一个Pull Request尽量只处理一个主题。
- 在说明中列出修改章节和验证方式。
- 内容性修改应附上权威来源，优先使用GFM规范、CommonMark规范或GitHub官方文档。
- 提交前确认没有生成临时文件、缓存目录或无关格式化改动。

## 版本规则

项目采用`YYYY.MM.PATCH`格式的日期版本号，当前版本记录在`VERSION`。影响内容分类或目录结构的修改应同步更新`CHANGELOG.md`。
