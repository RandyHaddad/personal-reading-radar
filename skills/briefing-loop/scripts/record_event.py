#!/usr/bin/env python3
"""Append a JSONL event to a briefing loop state file."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


ALLOWED_FILES = {
    "feedback": "feedback.jsonl",
    "surfaced": "surfaced.jsonl",
    "read": "read.jsonl",
    "delivered": "delivered.jsonl",
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", required=True, help="Briefing loop memory directory")
    parser.add_argument("--kind", required=True, choices=sorted(ALLOWED_FILES))
    parser.add_argument("--item", required=True)
    parser.add_argument("--url", default="")
    parser.add_argument("--notes", default="")
    parser.add_argument("--extra-json", default="{}", help="Additional JSON object fields")
    args = parser.parse_args()

    root = Path(args.path).expanduser().resolve()
    target = root / ALLOWED_FILES[args.kind]
    if not target.exists():
        raise SystemExit(f"Missing state file: {target}")

    try:
        extra = json.loads(args.extra_json)
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid --extra-json: {exc}") from exc
    if not isinstance(extra, dict):
        raise SystemExit("--extra-json must be a JSON object")

    event = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "kind": args.kind,
        "item": args.item,
    }
    if args.url:
        event["url"] = args.url
    if args.notes:
        event["notes"] = args.notes
    event.update(extra)

    with target.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(event, ensure_ascii=True, sort_keys=True) + "\n")

    print(f"Recorded {args.kind} event in {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
