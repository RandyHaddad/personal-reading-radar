# Briefing Loop

A harness-agnostic Agent Skill for a learned reading digest.

It helps an agent learn what a user likes to read, verify sources/dates/recency, avoid repeats, and deliver digests to the user's chosen surfaces: chat, email, Slack, PDF/EPUB, Kindle, or another available integration.

## Install

### Claude Code

```text
/plugin marketplace add RandyHaddad/briefing-loop
/plugin install briefing-loop@briefing-loop
/reload-plugins
```

Then run:

```text
/briefing-loop:briefing-loop
```

### Codex

Use this repo as a Codex plugin. The plugin manifest is at:

```text
.codex-plugin/plugin.json
```

### Other Agents

Install the folder at `skills/briefing-loop` anywhere your Agent Skills-compatible harness reads skills from.

## Use

Ask your agent:

```text
Use briefing-loop to set up my reading digest.
```

The skill keeps user-specific state outside the skill package. Do not commit personal profiles, delivery addresses, credentials, or digest logs.

## License

MIT
