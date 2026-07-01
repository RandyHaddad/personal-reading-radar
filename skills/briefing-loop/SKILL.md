---
name: briefing-loop
description: Set up and run a harness-agnostic briefing loop that learns a user's reading taste over time, builds recurring digests from articles, feeds, newsletters, papers, X posts, videos, podcasts, or existing digests, verifies links/dates/recency, maintains transparent memory, and delivers to the user's chosen surfaces such as chat, email, Slack, PDF/EPUB, or Kindle. Use when the user wants a daily/weekly reading digest, a learned recommendation loop, source watchlist, Kindle send workflow, catch-up tracker, or feedback-driven reading system.
---

# Briefing Loop

## Overview

Create and operate a briefing loop. The loop learns from normal interaction, keeps its memory in inspectable files, verifies sources and recency, and delivers the digest where the user actually reads.

This skill is harness-agnostic. Use the host environment's available tools for search, browsing, email, Slack, scheduled tasks, cron, file creation, or secret storage. Do not assume a specific agent product.

## Operating Model

Keep these responsibilities separate:

- `setup`: establish delivery surface, cadence, memory home, and taste-seeding method.
- `discovery`: gather candidates from links, feeds, search, newsletters, X posts, videos, podcasts, papers, or existing digests.
- `digestion`: explain what is worth understanding, with links, dates, recency, and a reading experience that fits the user.
- `learning`: update transparent memory from interactions, feedback, reads, saves, sends, and ignores.
- `delivery`: send or render the digest through the user's chosen surface.

Codex/chat/workspace may be the control surface, but it is not always the reading surface. Honor the user's chosen delivery target.

## First Setup

Read [setup-flow.md](references/setup-flow.md) when creating or changing a loop.

Default setup sequence:

1. Ask where the user wants to receive/read the digest.
2. Ask how the user likes to digest material: terse bullets, visual cards, images, HTML explainer, quiz, PDF/EPUB, audio-style brief, or another format.
3. Ask cadence and timezone only if scheduling is requested or implied.
4. Ask the easiest way to learn taste: pasted links, feed/browser/newsletter inspection, existing digest comparison, or a few specific questions.
5. Create the memory home with `scripts/init_loop_state.py` when file access is available.
6. Run a small calibration sweep before relying on automation.

Frame setup lightly: the loop improves from ongoing interaction, so the first questions only reduce obvious mistakes.

## Memory

Read [state-and-learning.md](references/state-and-learning.md) before writing or updating memory.

Use transparent, user-editable state files. Keep raw feedback separate from durable preferences. Keep `surfaced`, `read`, and `delivered` separate:

- `surfaced`: shown in a digest.
- `read`: user explicitly read or used it.
- `delivered`: sent to a target such as email, Slack, Kindle, PDF, EPUB, or saved list.

Do not treat a surfaced item as read. Do not repeat surfaced or delivered items unless there is a clear reason.

## Digest Workflow

Read [digest-quality.md](references/digest-quality.md) before producing a digest.
Read [reading-experience.md](references/reading-experience.md) when choosing or changing the digest format.

For every candidate:

- verify the URL or source identity;
- verify publication date, upload date, issue date, or say `date unclear`;
- assign recency: `new`, `recent`, `older/canonical`, `catch-up`, or `date unclear`;
- explain why old items are still included;
- avoid hallucinated titles, dates, authors, or source claims.

During cold start, keep sweeps small and honest. Do not claim to know the user's taste yet. Include occasional adjacent or outlier candidates when they could reveal new taste, but label why they are exploratory.

## Delivery

Read [delivery-integrations.md](references/delivery-integrations.md) before setting up or using email, Slack, Kindle, PDF/EPUB, or other delivery.

Delivery rules:

- Inspect connected MCPs/connectors, browser/computer-use capabilities, local config, and existing user context before asking the user to set up anything new.
- Detect available integrations when possible and show status plainly: connected, not connected, unavailable, or unknown.
- Ask for sign-in, credentials, or app setup only when the harness cannot do it.
- Store secrets only in the host's secret manager/keychain, never in loop memory.
- Send a small test artifact before depending on a delivery route.
- Treat `sent` as transport status, not proof that the destination accepted or rendered the item.
- Do not send to Kindle unless the user approves the item or explicitly configures auto-send.

## Feedback Loop

Learn from natural interaction. Short reactions such as "more like this", "too old", "already read", "send this", or "not useful" are helpful, but do not make the user use a formal labeling system.

After meaningful feedback:

1. Append the raw reaction to `feedback.jsonl`.
2. Promote durable taste/style/source/delivery rules to the right memory file.
3. Update `surfaced`, `read`, `delivered`, or tracker state as appropriate.
4. Tell the user what changed, briefly.

## System vs Preference Boundary

Treat these as system fixes:

- wrong delivery surface;
- missing source/date/recency verification;
- state semantics are unclear;
- memory files conflict or duplicate ownership;
- automation or cron behavior violates setup choices;
- agreed trackers or catch-up lanes are ignored.

Treat these as preference learning:

- item was interesting or boring;
- source should be more or less prominent;
- style was too long, too shallow, too technical, or too broad;
- item was too old, already read, or worth sending.

System fixes update the skill/workflow. Preference learning updates loop memory.
