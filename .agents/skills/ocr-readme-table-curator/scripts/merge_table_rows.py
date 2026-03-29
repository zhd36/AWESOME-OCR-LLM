from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


def normalize_text(value: str) -> str:
    return "".join(re.findall(r"[a-z0-9]+", value.lower()))


def load_decisions(path: Path) -> list[dict[str, Any]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(payload, list):
        return payload
    if not isinstance(payload, dict) or "insertions" not in payload:
        raise ValueError("decisions JSON must be a list or an object with an 'insertions' key")
    insertions = payload["insertions"]
    if not isinstance(insertions, list):
        raise ValueError("'insertions' must be a list")
    return insertions


def find_heading(lines: list[str], target: str) -> int:
    target_norm = normalize_text(target)
    for index, line in enumerate(lines):
        stripped = line.strip()
        if not stripped.startswith("#"):
            continue
        if target_norm and target_norm in normalize_text(stripped):
            return index
    raise ValueError(f"Could not find heading for target: {target}")


def find_table_bounds(lines: list[str], heading_index: int) -> tuple[int, int, int, int]:
    next_heading = len(lines)
    for index in range(heading_index + 1, len(lines)):
        if lines[index].strip().startswith("#"):
            next_heading = index
            break

    table_header = None
    for index in range(heading_index + 1, next_heading):
        if lines[index].startswith("|"):
            table_header = index
            break

    if table_header is None:
        raise ValueError(f"Could not find table after heading line {heading_index + 1}")

    separator = table_header + 1
    if separator >= len(lines) or not lines[separator].startswith("|"):
        raise ValueError(f"Malformed table near line {table_header + 1}")

    body_start = separator + 1
    table_end = body_start
    while table_end < next_heading and lines[table_end].startswith("|"):
        table_end += 1

    return table_header, separator, body_start, table_end


def existing_row_matches(existing_row: str, tokens: list[str]) -> bool:
    existing_norm = normalize_text(existing_row)
    return any(token and token in existing_norm for token in tokens)


def dedupe_tokens(insertion: dict[str, Any]) -> list[str]:
    dedupe = insertion.get("dedupe_keys", {})
    if not isinstance(dedupe, dict):
        dedupe = {}
    paper_id = str(dedupe.get("paper_id", "")).strip()
    if paper_id:
        return [normalize_text(paper_id)]
    values = [
        str(dedupe.get("name", "")).strip(),
        str(dedupe.get("title", "")).strip(),
    ]
    return [normalize_text(value) for value in values if value]


def group_insertions(insertions: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = {}
    for insertion in insertions:
        target = insertion.get("target") or insertion.get("section")
        row = insertion.get("row")
        if not isinstance(target, str) or not target.strip():
            raise ValueError("Each insertion needs a non-empty 'target' field")
        if not isinstance(row, str) or not row.strip().startswith("|") or not row.strip().endswith("|"):
            raise ValueError(f"Insertion for target '{target}' must provide a complete Markdown table row")
        grouped.setdefault(target.strip(), []).append(insertion)
    return grouped


def sort_key(insertion: dict[str, Any]) -> tuple[str, str]:
    return (
        str(insertion.get("date_iso", "")),
        str(insertion.get("row", "")),
    )


def merge_rows(readme_path: Path, decisions_path: Path, dry_run: bool) -> dict[str, Any]:
    lines = readme_path.read_text(encoding="utf-8").splitlines()
    grouped = group_insertions(load_decisions(decisions_path))

    inserted: list[dict[str, str]] = []
    skipped: list[dict[str, str]] = []

    for target, items in grouped.items():
        heading_index = find_heading(lines, target)
        _, _, body_start, table_end = find_table_bounds(lines, heading_index)
        existing_rows = lines[body_start:table_end]

        rows_to_insert: list[str] = []
        for insertion in sorted(items, key=sort_key, reverse=True):
            tokens = dedupe_tokens(insertion)
            if any(existing_row_matches(row, tokens) for row in existing_rows):
                skipped.append(
                    {
                        "target": target,
                        "reason": "duplicate",
                        "row": insertion["row"],
                    }
                )
                continue
            row = insertion["row"].rstrip()
            rows_to_insert.append(row)
            existing_rows.insert(0, row)
            inserted.append({"target": target, "row": row})

        if rows_to_insert:
            lines[body_start:body_start] = rows_to_insert

    if not dry_run:
        readme_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    return {
        "readme_path": str(readme_path),
        "decisions_path": str(decisions_path),
        "inserted_count": len(inserted),
        "skipped_count": len(skipped),
        "inserted": inserted,
        "skipped": skipped,
        "dry_run": dry_run,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Merge curated Markdown table rows into README.md.")
    parser.add_argument("--readme", required=True, help="Path to README.md.")
    parser.add_argument("--decisions", required=True, help="Path to the decisions JSON file.")
    parser.add_argument("--dry-run", action="store_true", help="Compute the merge result without writing README.md.")
    args = parser.parse_args()

    summary = merge_rows(Path(args.readme), Path(args.decisions), args.dry_run)
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
