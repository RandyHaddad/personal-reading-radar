# Briefing Loop

Daily digest that:

- can send specific readings to your Kindle;
- sets up an initial profile from links you send;
- continuously learns preferences from what you read, save, reject, send, or ask about;
- uses Spotify-style explore/exploit: mostly things that fit, sometimes outliers to learn your taste;
- adds articles, newsletters, papers, YouTube, X posts, podcasts, and existing digests to the mix;
- verifies sources, authors, dates, and recency;
- delivers the digest where you actually read: chat, email, Slack, PDF/EPUB, files, or another available surface;
- keeps profile and history files inspectable.

## Install

### Claude Code

Run these one at a time inside Claude Code:

```text
/plugin marketplace add https://github.com/RandyHaddad/briefing-loop.git
```

```text
/plugin install briefing-loop@briefing-loop
```

```text
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
