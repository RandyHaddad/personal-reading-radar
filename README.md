# Personal Reading Radar

A harness-agnostic Agent Skill for a learned reading digest.

It helps an agent learn what a user likes to read, verify sources/dates/recency, avoid repeats, and deliver digests to the user's chosen surfaces: chat, email, Slack, PDF/EPUB, Kindle, or another available integration.

## Install

### Claude Code

```text
/plugin marketplace add RandyHaddad/personal-reading-radar
/plugin install personal-reading-radar@personal-reading-radar
/reload-plugins
```

Then run:

```text
/personal-reading-radar:personal-reading-radar
```

### Codex

Use this repo as a Codex plugin. The plugin manifest is at:

```text
.codex-plugin/plugin.json
```

### Other Agents

Install the folder at `skills/personal-reading-radar` anywhere your Agent Skills-compatible harness reads skills from.

## Use

Ask your agent:

```text
Use personal-reading-radar to set up my reading digest.
```

The skill keeps user-specific state outside the skill package. Do not commit personal profiles, delivery addresses, credentials, or digest logs.

## License

MIT
