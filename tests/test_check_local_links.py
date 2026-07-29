import tempfile
import unittest
from pathlib import Path

from scripts.check_local_links import (
    check_file,
    document_anchors,
    github_slug,
    normalize_reference_label,
    split_target,
)


class LinkCheckerTests(unittest.TestCase):
    def test_github_slug_removes_formatting_and_punctuation(self):
        self.assertEqual("github平台的alerts", github_slug("GitHub平台的`Alerts`！"))

    def test_document_anchors_number_duplicate_headings(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "README.md"
            path.write_text("# 标题\n\n## 标题\n", encoding="utf-8")
            self.assertEqual({"标题", "标题-1"}, document_anchors(path))

    def test_split_target_preserves_fragment(self):
        self.assertEqual(("docs/guide.md", "安装"), split_target("docs/guide.md#安装"))

    def test_reference_labels_ignore_case_and_repeated_spaces(self):
        self.assertEqual("my label", normalize_reference_label(" My   Label "))

    def test_check_file_reports_missing_anchor_and_file(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            target = root / "target.md"
            target.write_text("# 存在的标题\n", encoding="utf-8")
            source = root / "README.md"
            source.write_text(
                "[正确](target.md#存在的标题)\n"
                "[错误锚点](target.md#不存在)\n"
                "[错误文件](missing.md)\n",
                encoding="utf-8",
            )

            failures = check_file(source)
            self.assertEqual(2, len(failures))
            self.assertEqual("标题锚点不存在", failures[0][2])
            self.assertEqual("本地目标不存在", failures[1][2])

    def test_check_file_reports_undefined_reference_link(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "README.md"
            source.write_text(
                "[已定义][guide]\n"
                "[折叠引用][]\n"
                "[guide]: https://example.com\n",
                encoding="utf-8",
            )

            failures = check_file(source)
            self.assertEqual([(2, "折叠引用", "引用式链接未定义")], failures)

    def test_check_file_reports_invalid_local_target(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "README.md"
            source.write_text("[错误路径](bad<name.md)\n", encoding="utf-8")

            failures = check_file(source)
            self.assertEqual("本地目标格式无效", failures[0][2])


if __name__ == "__main__":
    unittest.main()
