# Setup Flow

Use the lightest setup that can produce a useful first sweep.

## Setup Prompt

Say this in substance, not necessarily verbatim:

```text
I can set up a personal reading radar. It improves from our interactions: what you open, reject, save, send, ask about, or ignore. First I only need the delivery surface, how you like to digest things, cadence, and the easiest way to learn your taste.
```

## Step 1: Delivery Surface

Ask where the user wants to read or receive the digest.

Common targets:

- chat/workspace thread;
- email;
- Slack or Discord;
- Kindle;
- PDF or EPUB file;
- local markdown;
- Notion, Drive, Docs, or another connected store.

Detect available integrations when possible. Use plain status:

```text
Delivery options I can see:
- Email: connected
- Slack: not connected, can help set up
- Kindle: not configured
- Local PDF/EPUB: available
```

If the harness cannot inspect integrations, say so and ask the user to choose from available routes.

## Step 2: Reading Experience

Ask how the user likes to read or digest material. Treat this as a preference that will evolve, not a fixed template.

Offer examples:

- terse text with bullets;
- article cards with images;
- HTML explainer or interactive page;
- quiz/game format for retention;
- visual map, timeline, or comparison table;
- PDF/EPUB optimized for longer reading;
- audio-style briefing script;
- mixed mode depending on the item.

If visual tools are available, suggest useful options:

- include article images or thumbnails with attribution when available and appropriate;
- generate explanatory images or diagrams when they would clarify the idea;
- create a small HTML artifact for interactive summaries, quizzes, timelines, or flashcards.

Do not overfit the user to the first answer. Save the preference and keep learning from what they actually open, ask about, save, or reject.

## Step 3: Cadence

Ask cadence only after delivery is known.

Useful defaults:

- daily morning in local timezone;
- weekdays only;
- weekly;
- manual until the user likes the shape.

If the harness supports scheduled tasks, configure them after the first acceptable run. If not, prepare a cron/system scheduler instruction or a manual command path.

## Step 4: Taste Seeding

Do not ask "what do you want to read about?" as the main cold-start question. That is often too hard.

Offer concrete ways to seed taste:

- paste links the user liked;
- inspect browser tabs, feeds, bookmarks, newsletters, or X timeline if the user grants access;
- compare against existing digests the user reads;
- answer a few gap-filling questions.

Ask specific questions only to fill gaps:

- "Should I include older canonical material, or only recent items?"
- "Are X posts/videos/podcasts eligible, or only articles?"
- "Do you want catch-up lanes for specific archives or authors?"
- "What should never appear?"

## Step 5: Memory Home

Create a transparent memory directory. Prefer a user-visible path such as:

```text
~/.reading-radar/<radar-name>/
```

If the harness has a project-local convention, use that and tell the user.

Run:

```bash
python3 scripts/init_radar_state.py --path <memory-path> --name "<radar name>"
```

## Step 6: Calibration

Early runs are calibration. Keep them small, show uncertainty, and learn from normal interaction. Do not imply the user must label everything.

Good feedback invitations:

```text
Tell me what you actually read, saved, sent, or disliked. Short reactions are enough.
```

Bad feedback invitations:

```text
Please label every item with one of these categories.
```
