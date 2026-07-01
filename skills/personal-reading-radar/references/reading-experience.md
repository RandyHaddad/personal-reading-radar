# Reading Experience

The radar should learn not only what the user likes to read, but how the user likes to digest it.

## Principle

Choose the format that helps the user understand, decide, remember, or act. Keep the format open-ended and tool-aware.

Examples:

- terse bullets for fast scanning;
- longer narrative briefs for context;
- visual cards for phone reading;
- image-rich digests with source images;
- generated diagrams for abstract ideas;
- HTML explainers, timelines, or interactive maps;
- quiz games or flashcards for retention;
- comparison tables for products, papers, companies, or policies;
- PDF/EPUB for long reading;
- audio-style scripts for listening;
- "send only approved items" bundles for Kindle or read-later apps.

## Visual Assets

Use visuals when they add signal.

Useful sources:

- images embedded in the source article;
- Open Graph or social preview images;
- figures from papers, reports, or slides;
- screenshots of relevant pages when permitted by the harness;
- generated explanatory images or diagrams when no source image exists.

Generated images are available only in harnesses that support image generation, such as Codex with an image-generation tool. If unavailable, use source images, diagrams, screenshots, or text-first explanations instead.

Rules:

- keep the original link and attribution near source images;
- do not imply generated images came from the article;
- avoid decorative images that do not help the user inspect or remember the item;
- preserve dates, source links, and recency labels even in visual formats.

## Interactive Formats

If the harness can create local HTML or rich artifacts, consider:

- one-page interactive digest;
- collapsible item cards;
- timeline by recency;
- topic map;
- "quiz me later" flashcards;
- paper figure walkthrough;
- compare-and-rank board;
- reading queue with buttons or commands for save/send/read.

Interactive output should still be inspectable and portable. If the artifact is external, leave a concise text summary and link/path in the control thread.

## Media-Specific Digestion

For X posts:

- capture the core claim or pattern;
- include the post URL;
- say whether it is a thread, article-style post, or single take;
- avoid over-weighting viral takes without substance.

For videos or podcasts:

- include title, source/channel, publish date, and duration when available;
- summarize the useful segments or timestamps when possible;
- mark if the digest is based on transcript, notes, description, or full watch/listen.

For papers:

- include venue/preprint status when available;
- identify the central claim, method, evidence, and limitation;
- include figures only when they help comprehension.

## Learning The Format

Treat format feedback as durable preference when repeated or explicit.

Examples:

- "I like Digest this bullets."
- "Make these more visual."
- "Quiz me on the important ones."
- "Send full PDFs, but keep chat short."
- "Use article images."
- "No generated images unless they explain something."

Record raw reactions in `feedback.jsonl` and promote durable format rules to `profile.md`.
