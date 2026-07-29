# 贡献指南

感谢你帮助完善这份GitHub Flavored Markdown参考文档。

## 修改范围

- 修正无法渲染、描述不准确或已经失效的示例。
- 补充GFM、GitHub平台功能、HTML或LaTeX相关说明时，明确标注所属层次。
- 新增图片、音频或视频时，优先使用仓库内相对路径，并控制资源体积。
- 不要把特定编辑器扩展描述为GFM标准语法。
- 新增功能章节时，尽量同时说明Markdown/CommonMark、正式GFM或GitHub平台、HTML和LaTeX实现。
- 某种载体没有等价语法时，应明确写为“无原生实现”或“不适用”，并给出最接近的替代方案，不要保留“暂无”占位。
- 对GitHub不能渲染的源码示例，必须在示例之前明确标注“GitHub不支持”，不能用“显示效果如下”暗示其会生效。
- GitHub平台功能应注明适用位置，例如仓库Markdown文件、Issue、Pull Request、Discussion或评论；不确定时使用保守表述并链接官方文档。
- HTML示例应区分“独立HTML页面可用”和“GitHub Markdown会过滤”，LaTeX示例应区分“完整LaTeX文档”和“GitHub数学公式”。

## 本地检查

仓库根目录下运行：

```powershell
python material/parser_entities.py --check
python scripts/check_local_links.py
python -m unittest discover -s tests -v
npx --yes markdownlint-cli2@0.18.1 README.md CONTRIBUTING.md "docs/*.md" "material/**/*.md"
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
