import argparse
import json
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, Mapping


BASE_DIR = Path(__file__).resolve().parent
DEFAULT_INPUT = BASE_DIR / "entities.json"
DEFAULT_OUTPUT = BASE_DIR / "entities.md"
DEFAULT_DIRECTORY = BASE_DIR / "entities"


def group_name(entity: str) -> str:
    name = entity.lstrip("&")
    return name[:1].upper()


def escape_table_cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", "<br>")


def codepoints_text(codepoints: Any) -> str:
    return " ".join(f"U+{int(codepoint):04X}" for codepoint in codepoints)


def render_group(group: str, entities: Mapping[str, Mapping[str, Any]]) -> str:
    lines = [
        f"# HTML实体：{group}",
        "",
        "[返回实体索引](../entities.md)",
        "",
        "| 实体写法 | 显示字符 | Unicode码点 |",
        "| --- | --- | --- |",
    ]

    for entity, metadata in entities.items():
        character = escape_table_cell(str(metadata.get("characters", "")))
        codepoints = codepoints_text(metadata.get("codepoints", []))
        lines.append(f"| `{entity}` | {character} | `{codepoints}` |")

    return "\n".join(lines) + "\n"


def render_index(groups: Mapping[str, Mapping[str, Any]]) -> str:
    lines = [
        "# HTML实体参考",
        "",
        "本目录根据实体名称的首字母分页生成，数据来源为`entities.json`。",
        "",
        "| 分组 | 实体数量 |",
        "| --- | ---: |",
    ]

    for group, entities in groups.items():
        lines.append(f"| [{group}](entities/{group}.md) | {len(entities)} |")

    lines.extend(
        (
            "",
            "修改`entities.json`后运行以下命令重新生成：",
            "",
            "```powershell",
            "python material/parser_entities.py",
            "```",
        )
    )
    return "\n".join(lines) + "\n"


def build_outputs(data: Mapping[str, Mapping[str, Any]]) -> Dict[str, str]:
    grouped = defaultdict(dict)
    for entity, metadata in data.items():
        grouped[group_name(entity)][entity] = metadata

    groups = {group: grouped[group] for group in sorted(grouped)}
    outputs = {"../entities.md": render_index(groups)}
    outputs.update({f"{group}.md": render_group(group, entities) for group, entities in groups.items()})
    return outputs


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="将HTML实体JSON整理为分页Markdown文档。")
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT, help="输入JSON文件路径")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT, help="索引Markdown文件路径")
    parser.add_argument("--directory", type=Path, default=DEFAULT_DIRECTORY, help="分页输出目录")
    parser.add_argument("--check", action="store_true", help="检查全部生成文件是否为最新版本")
    return parser.parse_args()


def expected_files(args: argparse.Namespace, data: Mapping[str, Mapping[str, Any]]) -> Dict[Path, str]:
    outputs = build_outputs(data)
    files = {args.output.resolve(): outputs.pop("../entities.md")}
    files.update({(args.directory / name).resolve(): content for name, content in outputs.items()})
    return files


def main() -> int:
    args = parse_args()
    with args.input.resolve().open("r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, dict):
        raise ValueError("实体JSON的顶层结构必须是对象。")

    files = expected_files(args, data)
    expected_page_paths = {path for path in files if path.parent == args.directory.resolve()}
    existing_page_paths = set(args.directory.resolve().glob("*.md")) if args.directory.exists() else set()

    if args.check:
        outdated = [
            path
            for path, content in files.items()
            if not path.exists() or path.read_text(encoding="utf-8") != content
        ]
        stale = sorted(existing_page_paths - expected_page_paths)
        if outdated or stale:
            for path in outdated:
                print(f"需要重新生成：{path}")
            for path in stale:
                print(f"需要删除过期分页：{path}")
            return 1
        print(f"实体索引和{len(expected_page_paths)}个分页均为最新版本。")
        return 0

    args.directory.resolve().mkdir(parents=True, exist_ok=True)
    for path in existing_page_paths - expected_page_paths:
        path.unlink()
    for path, content in files.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    print(f"已生成实体索引和{len(expected_page_paths)}个分页。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
