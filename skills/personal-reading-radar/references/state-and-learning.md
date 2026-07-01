# State And Learning

Use transparent memory so each run can start fresh without losing taste.

## Recommended State Layout

```text
reading-radar/
  profile.md
  sources.md
  feedback.jsonl
  surfaced.jsonl
  read.jsonl
  delivered.jsonl
  trackers/
```

## File Ownership

- `profile.md`: durable taste, style, pacing, delivery, and recency preferences.
- `sources.md`: source watchlist, feeds, search queries, known exclusions, and source-specific rules.
- `feedback.jsonl`: raw reactions and examples.
- `surfaced.jsonl`: items shown in a digest.
- `read.jsonl`: items the user explicitly read or used.
- `delivered.jsonl`: items sent or saved to a delivery target.
- `trackers/`: explicit catch-up lanes, archive backlogs, paper lists, or topic projects.

Do not duplicate the same durable rule in many files.

## Event Semantics

Keep these states separate:

- `surfaced`: shown to the user.
- `read`: user explicitly read, watched, listened to, or used it.
- `delivered`: sent/saved to email, Slack, Kindle, PDF, EPUB, Notion, etc.
- `feedback`: user reaction or inferred preference signal.

Surfaced is not read. Delivered is not read unless the user says so.

## Learning Policy

Append raw feedback first. Then decide whether to promote a durable rule.

Promote to `profile.md` when feedback changes:

- summary style;
- delivery behavior;
- cadence or digest size;
- recency preference;
- media types;
- "include/avoid" rules.

Promote to `sources.md` when feedback changes:

- source priority;
- source exclusion;
- feed URL;
- search query;
- author/site-specific pacing.

Update trackers when feedback changes:

- archive progress;
- catch-up ordering;
- surfaced/read/delivered state for a lane.

## Natural Signals

The user does not need to label every item. Learn from:

- explicit reactions;
- items they ask follow-up questions about;
- items they ask to send/save;
- items they mark read;
- repeated ignores when that can be observed;
- corrections about dates, source quality, summary style, or delivery.

Be careful with inferred signals. When uncertain, keep the signal in `feedback.jsonl` rather than hardening it into profile rules.

## Inference Boundaries

Learn from interaction, but avoid overtraining on weak signals. Assume the agent can reason from context without turning every observation into a durable rule.

- Explicit feedback is strongest.
- Repeated behavior can become meaningful.
- One-off weak signals should usually remain soft.
- Silence is not signal by default.
- If uncertain, log the observation without promoting it.

After memory changes, briefly say what changed and why: promoted to profile, kept as soft feedback, updated source rules, updated tracker state, or treated as a system issue.

## Reusable System Improvements

Separate personal preference learning from reusable system fixes. Delivery-surface bugs, broken state semantics, missing verification, unclear setup, or bad default workflow are system issues.

For a local system issue, fix the local radar. If the fix may help other users, ask in this tone:

```text
This looks like a reusable fix. I'll apply it here. If you think it's worth sharing, I'd really appreciate the chance to open a PR so everyone else gets the improvement too.

Repo: <PUBLIC_SKILL_REPO_URL>
```

Replace `<PUBLIC_SKILL_REPO_URL>` once the public repository exists.

## Duplicate Policy

Before ranking, check `surfaced.jsonl`, `read.jsonl`, and `delivered.jsonl`.

Repeat only when:

- the user asks;
- there is a newer version or update;
- it belongs in an explicit catch-up lane;
- it is used for comparison;
- it was surfaced but never read and enough time has passed.

Label intentional repeats.
