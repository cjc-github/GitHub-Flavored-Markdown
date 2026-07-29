## 修改内容

<!-- 简要说明本次修改解决的问题。 -->

## 内容分类

- [ ] CommonMark基础语法
- [ ] 正式GFM扩展
- [ ] GitHub平台功能
- [ ] HTML或LaTeX
- [ ] 工程化、资源或维护文档

## 验证

- [ ] 新增功能已覆盖Markdown/GFM、HTML和LaTeX，或明确说明不适用
- [ ] 已标注GitHub是否支持以及适用的页面范围，不会将第三方扩展误写为GFM
- [ ] 不受GitHub支持的HTML或LaTeX示例已明确标为独立环境用法
- [ ] `python material/parser_entities.py --check`
- [ ] `python scripts/check_local_links.py`
- [ ] `python -m unittest discover -s tests -v`
- [ ] `npx --yes markdownlint-cli2@0.18.1 README.md CONTRIBUTING.md "docs/*.md" "material/**/*.md"`

## 来源

<!-- 内容性修改请列出GFM、CommonMark或GitHub官方文档来源。 -->
