import re
import sys
from pathlib import Path
from typing import Dict, Iterable, List, Set, Tuple
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)\n]+)\)")
REFERENCE_DEFINITION = re.compile(r"^\s{0,3}\[(?!\^)[^\]]+\]:\s*(\S+)")
HTML_LINK = re.compile(r"\b(?:href|src)=[\"']([^\"']+)[\"']", re.IGNORECASE)
HTML_ANCHOR = re.compile(r"\b(?:id|name)=[\"']([^\"']+)[\"']", re.IGNORECASE)
INLINE_CODE = re.compile(r"(`+).*?\1")
HTML_TAG = re.compile(r"<[^>]+>")
ATX_HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")
EXTERNAL_PREFIXES = ("http://", "https://", "mailto:", "data:", "tel:")


Failure = Tuple[int, str, str]


def markdown_files(root: Path = ROOT) -> Iterable[Path]:
    yield from sorted(root.rglob("*.md"))


def content_without_fences(text: str) -> Iterable[Tuple[int, str]]:
    fence = None

    for line_number, line in enumerate(text.splitlines(), start=1):
        stripped = line.lstrip()
        match = re.match(r"(`{3,}|~{3,})", stripped)
        if match:
            marker = match.group(1)
            if fence is None:
                fence = marker[0]
            elif marker[0] == fence:
                fence = None
            continue
        if fence is None:
            yield line_number, line


def github_slug(text: str) -> str:
    text = HTML_TAG.sub("", text)
    text = text.replace("`", "").replace("*", "").replace("_", "")
    text = text.strip().lower()
    text = re.sub(r"[^\w\- ]", "", text, flags=re.UNICODE)
    return re.sub(r"\s+", "-", text)


def document_anchors(path: Path) -> Set[str]:
    anchors = set()
    occurrences: Dict[str, int] = {}
    text = path.read_text(encoding="utf-8")

    for _, line in content_without_fences(text):
        heading = ATX_HEADING.match(line)
        if heading:
            base = github_slug(heading.group(2))
            duplicate_index = occurrences.get(base, 0)
            anchor = base if duplicate_index == 0 else f"{base}-{duplicate_index}"
            occurrences[base] = duplicate_index + 1
            anchors.add(anchor)
        anchors.update(unquote(anchor) for anchor in HTML_ANCHOR.findall(line))

    return anchors


def split_target(raw_target: str) -> Tuple[str, str]:
    target = raw_target.strip()
    if target.startswith("<") and ">" in target:
        target = target[1 : target.index(">")]
    else:
        target = target.split(maxsplit=1)[0]
    path, separator, fragment = target.partition("#")
    return unquote(path), unquote(fragment) if separator else ""


def is_external_target(target: str) -> bool:
    return target.startswith(EXTERNAL_PREFIXES)


def check_target(
    source_path: Path,
    line_number: int,
    raw_target: str,
    anchor_cache: Dict[Path, Set[str]],
) -> List[Failure]:
    target_path, fragment = split_target(raw_target)
    if is_external_target(target_path):
        return []

    resolved = source_path if not target_path else (source_path.parent / target_path).resolve()
    if not resolved.exists():
        return [(line_number, raw_target, "本地目标不存在")]

    if fragment and resolved.suffix.lower() == ".md":
        anchors = anchor_cache.setdefault(resolved, document_anchors(resolved))
        if fragment.lower() not in anchors:
            return [(line_number, raw_target, "标题锚点不存在")]

    return []


def check_file(path: Path, anchor_cache: Dict[Path, Set[str]] = None) -> List[Failure]:
    failures = []
    text = path.read_text(encoding="utf-8")
    anchor_cache = anchor_cache if anchor_cache is not None else {}

    for line_number, line in content_without_fences(text):
        line_without_code = INLINE_CODE.sub("", line)
        targets = MARKDOWN_LINK.findall(line_without_code)
        targets.extend(HTML_LINK.findall(line_without_code))
        reference = REFERENCE_DEFINITION.match(line_without_code)
        if reference:
            targets.append(reference.group(1))

        for raw_target in targets:
            failures.extend(check_target(path, line_number, raw_target, anchor_cache))

    return failures


def main() -> int:
    failures = []
    anchor_cache: Dict[Path, Set[str]] = {}

    for path in markdown_files():
        for line_number, target, reason in check_file(path, anchor_cache):
            failures.append((path.relative_to(ROOT), line_number, target, reason))

    if failures:
        for path, line_number, target, reason in failures:
            print(f"{path}:{line_number}: {reason}：{target}")
        return 1

    print("所有Markdown本地链接、资源路径和标题锚点均有效。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
