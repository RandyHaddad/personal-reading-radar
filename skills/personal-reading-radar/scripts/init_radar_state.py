#!/usr/bin/env python3
"""Initialize transparent state files for a personal reading radar."""

from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path


def write_if_missing(path: Path, content: str) -> bool:
    if path.exists():
        return False
    path.write_text(content, encoding="utf-8")
    return True


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", required=True, help="Directory for radar memory files")
    parser.add_argument("--name", default="Personal Reading Radar")
    args = parser.parse_args()

    root = Path(args.path).expanduser().resolve()
    root.mkdir(parents=True, exist_ok=True)
    (root / "trackers").mkdir(exist_ok=True)

    today = datetime.now().strftime("%Y-%m-%d")

    created = []
    files = {
        "profile.md": f"""# {args.name} Profile

Updated: {today}

## Goal

Maintain a personal reading radar that learns from interaction and delivers reading candidates where the user wants to read them.

## Delivery

- Primary surface: unknown
- Mirrors/extensions: none configured

## Cadence

- Schedule: manual until configured
- Timezone: unknown

## Current Taste

Cold start. Learn from links, feeds, existing digests, and reactions.

## Style

Keep summaries concise, concrete, and useful for deciding what to read.
""",
        "sources.md": f"""# {args.name} Sources

Updated: {today}

## Seed Sources

None yet.

## Search Queries

None yet.

## Exclusions

None yet.
""",
        "feedback.jsonl": "",
        "surfaced.jsonl": "",
        "read.jsonl": "",
        "delivered.jsonl": "",
    }

    for filename, content in files.items():
        if write_if_missing(root / filename, content):
            created.append(filename)

    print(f"Radar state: {root}")
    if created:
        print("Created:")
        for filename in created:
            print(f"- {filename}")
        print("- trackers/")
    else:
        print("No files created; state already existed.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
