import unittest

from material.parser_entities import build_outputs, escape_table_cell, group_name


class EntityGeneratorTests(unittest.TestCase):
    def test_group_name_uses_first_letter_without_ampersand(self):
        self.assertEqual("A", group_name("&AElig;"))

    def test_escape_table_cell_handles_pipes_and_newlines(self):
        self.assertEqual("a\\|b<br>c", escape_table_cell("a|b\nc"))

    def test_build_outputs_creates_index_and_group_pages(self):
        outputs = build_outputs(
            {
                "&AElig;": {"codepoints": [198], "characters": "Æ"},
                "&beta;": {"codepoints": [946], "characters": "β"},
            }
        )

        self.assertEqual({"../entities.md", "A.md", "B.md"}, set(outputs))
        self.assertIn("[A](entities/A.md)", outputs["../entities.md"])
        self.assertIn("`U+00C6`", outputs["A.md"])


if __name__ == "__main__":
    unittest.main()
