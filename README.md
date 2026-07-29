# GitHub Flavored Markdown 中文参考

本项目整理CommonMark基础语法、正式GFM扩展、GitHub平台写作功能，以及常见HTML和LaTeX实现差异。

> 当前文档版本：`2026.07.0`

## 内容边界

1. **CommonMark基础语法**：Markdown通用语法基础。
2. **正式GFM扩展**：删除线、表格、任务列表项、扩展自动链接和禁止的原始HTML。
3. **GitHub平台功能**：Alerts、脚注、数学公式、Mermaid、GeoJSON、TopoJSON和STL等。
4. **HTML与LaTeX**：仅用于对比实现方式，不代表GitHub支持任意标签、属性或命令。

## 文档目录

- [一、标题与目录](docs/01-headings.md)
- [二、文本格式](docs/02-text-format.md)
- [三、列表](docs/03-lists.md)
- [四、链接](docs/04-links.md)
- [五、图片与图表](docs/05-images.md)
- [六、表格](docs/06-tables.md)
- [七、数学公式](docs/07-math.md)
- [八、GitHub常见组件](docs/08-github-features.md)
- [九、支持情况与杂项](docs/09-misc.md)
- [十、GFM规范补充](docs/10-gfm-spec.md)
- [Emoji参考](material/emoji.md)
- [HTML实体参考](material/entities.md)

## 官方资源

- [GitHub Flavored Markdown规范](https://github.github.com/gfm/)
- [CommonMark规范](https://commonmark.org/)
- [GitHub写作与格式化文档](https://docs.github.com/get-started/writing-on-github)

## 本地验证

```powershell
python material/parser_entities.py --check
python scripts/check_local_links.py
python -m unittest discover -s tests -v
npx --yes markdownlint-cli2@0.18.1 README.md CONTRIBUTING.md "docs/*.md" "material/*.md"
```

## 参与维护

提交修改前请阅读[贡献指南](CONTRIBUTING.md)。项目协作约定和维护信息见：

- [行为准则](CODE_OF_CONDUCT.md)
- [安全策略](SECURITY.md)
- [支持说明](SUPPORT.md)
- [更新日志](CHANGELOG.md)
- [当前版本](VERSION)

本项目采用MIT许可证，详见[LICENSE](LICENSE)。
