# Delivery Integrations

Delivery is user-chosen. The agent controls setup and memory, but the readable artifact should land where the user actually reads.

## General Integration Pattern

For each delivery target:

1. Inspect the harness first: connected MCPs/connectors, available tools, browser state, local config, existing context, and known user delivery habits.
2. Detect whether the integration is connected or available.
3. State status plainly: connected, not connected, unavailable, or unknown.
4. Use the lowest-friction setup path the harness can actually operate: connector, MCP, API, SMTP, browser automation, computer use, local file, or manual fallback.
5. Do as much setup and verification as possible without involving the user.
6. Ask the user only for sign-in, approval, credentials, account setup, or destination details the agent cannot obtain.
7. Store secrets only in a secret manager/keychain, never in radar memory.
8. Send a small test artifact before relying on the route.
9. Distinguish transport success from delivery success. A connector, SMTP server, or API may report `sent` before the destination accepts or renders the artifact.
10. When possible, check for bounce/error replies, delivery receipts, destination-side status, or first-delivery user confirmation before marking the route reliable.
11. Record successful deliveries in `delivered.jsonl`.

Prefer native connected tools when they exist. If the user already handles email through Gmail, Outlook, Slack, Discord, or another connected surface, adapt to that route instead of forcing a new one.

If a browser or computer-control tool is available and the integration needs a one-time setting, use it to navigate setup pages, inspect current settings, and fill non-secret fields. Keep the user in the loop for authentication, sensitive approvals, and irreversible actions.

## Email

Use a connected email tool when available. Otherwise use SMTP only if the user provides or approves a sender account.

For SMTP:

- store app passwords or tokens in the host secret manager/keychain;
- never write secrets to profile, source, feedback, or logs;
- send a short test message;
- do not treat SMTP/API `sent` as final delivery when the destination can later reject the attachment;
- record sender address and non-secret delivery preferences in memory.

## Slack, Discord, And Chat Tools

If a connector is available, offer it as a delivery target. If not connected, say it can be set up if the harness supports that connector.

Use channels/DMs only after the user chooses the destination.

## PDF And EPUB

Use local files when external delivery is not configured or when the user wants a portable artifact.

For EPUB:

- include valid language metadata such as `en-US` when the target expects it;
- keep formatting simple;
- test rendering or delivery before relying on it.

## Kindle

Kindle delivery is optional and should usually be approval-based.

Fast setup:

1. Ask the user to open or sign in to Amazon's Send to Kindle / device preferences if browser automation cannot do it.
2. Find the user's Send-to-Kindle email address for the target device/app.
3. Confirm or add the sender email to Amazon's approved personal document email list.
4. Configure a sender route: connected email tool or SMTP with secret stored in keychain/secret manager.
5. Send a small test file.
6. Check for Amazon rejection emails or ask the user to confirm the first item landed; SMTP `sent` only proves the email left the sender.
7. If EPUB fails with an internal or metadata error, retry with valid `en-US` metadata or a simpler PDF.
8. Record Kindle target addresses and non-secret setup facts in memory.

Rules:

- Do not auto-send to Kindle unless the user explicitly configures that policy.
- By default, send only specific items the user approves.
- Record successful Kindle sends in `delivered.jsonl`.

## Scheduling

If the harness supports native scheduled tasks, use that. Otherwise prepare a cron/system scheduler command that runs the radar workflow.

Keep the schedule separate from taste memory. If a schedule prompt duplicates workflow instructions, shorten it and point back to the skill/state files.
