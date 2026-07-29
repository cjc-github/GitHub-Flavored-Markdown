import argparse
import json
from pathlib import Path
from typing import Any, Dict


BASE_DIR = Path(__file__).resolve().parent
DEFAULT_INPUT = BASE_DIR / "entities.json"
DEFAULT_OUTPUT = BASE_DIR / "entities.md"


def render_entities(data: Dict[str, Dict[str, Any]]) -> str:
    lines = ["", "# entities.json文件内容整理", ""]

    for entity, metadata in data.items():
        rendered_metadata = dict(metadata)
        rendered_metadata["code"] = f"`{entity}`"
        lines.extend((f"{entity}: {rendered_metadata}", ""))

    return "\n".join(lines) + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="将HTML实体JSON整理为Markdown文档。")
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT, help="输入JSON文件路径")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT, help="输出Markdown文件路径")
    parser.add_argument("--check", action="store_true", help="检查输出文件是否为最新版本")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    input_path = args.input.resolve()
    output_path = args.output.resolve()

    with input_path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, dict):
        raise ValueError("实体JSON的顶层结构必须是对象。")

    rendered = render_entities(data)

    if args.check:
        if not output_path.exists() or output_path.read_text(encoding="utf-8") != rendered:
            print(f"需要重新生成：{output_path}")
            return 1
        print(f"已是最新版本：{output_path}")
        return 0

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(rendered, encoding="utf-8")
    print(f"已生成：{output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
