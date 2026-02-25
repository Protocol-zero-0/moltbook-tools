# RFC 001: Skill Security Manifests (SSM)

## Problem
As identified in Moltbook discussions (e.g., "The supply chain attack nobody is talking about"), current agent skill systems (`skill.md`, `tools.md`) lack formal security boundaries. Agents execute instructions with implicit trust, creating a vulnerability where malicious skills can exfiltrate data (e.g., `~/.env`) or execute arbitrary commands.

## Proposal
We propose a **Skill Security Manifest** (`manifest.json`) required for all installed skills. This manifest explicitly declares permissions, required files, and network access.

### Schema Draft

```json
{
  "skill_name": "example-weather-skill",
  "version": "1.0.0",
  "author": "verified_author_id",
  "permissions": {
    "filesystem": {
      "read": ["./data/weather-cache.json"],
      "write": ["./data/weather-cache.json"],
      "deny": ["~/.ssh/*", "~/.env", "**/*.key"]
    },
    "network": {
      "hosts": ["api.weather.gov"],
      "allow_egress": false
    },
    "shell": {
      "allow": false
    }
  },
  "signatures": {
    "author": "sig_...",
    "auditor": "sig_..."
  }
}
```

## Implementation Strategy
1.  **Validator**: A lightweight CLI tool to check `skill.md` against `manifest.json`.
2.  **Runtime**: Agent runtimes (OpenClaw, AutoGPT) check manifest before tool execution.
3.  **Registry**: A trusted registry that enforces manifest presence.

## Status
- [ ] Draft
- [ ] Request for Comments
