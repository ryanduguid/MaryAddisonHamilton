## Install

Pick the smallest path that matches what you need:

| Need | Install | What you get |
| --- | --- | --- |
| Claude Code, with updates from this repo | Plugin install | Skills at the installed repository revision as `australian-accounting-skills:*` |
| Codex | Codex plugin | The same revision's skills via `.codex-plugin/plugin.json` |
| Any agent that reads `SKILL.md` | `npx skills` | Portable skill files only. No extra runtime. |

### Claude Code plugin

This repo is also a Claude Code plugin marketplace. It packages the inventory
present at the repository revision it installs under the stable namespace:

```
/plugin marketplace add ryanduguid/australian-accounting-skills
/plugin install australian-accounting-skills@ryanduguid
```

The skills then register as `australian-accounting-skills:bas-preparation` and so on.

The `australian-accounting-skills` plug-in ID, namespace and install target are stable compatibility identifiers.

If the Hardhat Ledger plugin is installed, uninstall or disable
`subcontractor-accounting-skills@ryanduguid-contracting` before installing
`australian-accounting-skills@ryanduguid`. The ten transferred skill names are
intentionally unchanged, so never enable both packs at once. See
[`docs/HARDHAT-CONSOLIDATION.md`](../docs/HARDHAT-CONSOLIDATION.md) for the exact
source inventory and rollback route.

### Codex plugin

```
codex plugin marketplace add ryanduguid/australian-accounting-skills
codex plugin add australian-accounting-skills@ryanduguid
```

### Any agent, via the skills CLI

One command, using the [`skills` CLI](https://github.com/vercel-labs/skills). It reads the
`.claude/skills/` layout this repo uses, so no extra manifest is needed:

```bash
npx skills add ryanduguid/australian-accounting-skills
```

That installs into the current project (`./.claude/skills/`). Add `-g` to install into
`~/.claude/skills` instead, `-a claude-code` to target one agent, and `-l` to list the skills
without installing anything.

### By hand

Copy the skills you want into your project or user skills directory:

```bash
git clone https://github.com/ryanduguid/australian-accounting-skills australian-accounting-skills
mkdir -p ~/.claude/skills
cp -r australian-accounting-skills/.claude/skills/* ~/.claude/skills/
```

PowerShell:

```powershell
git clone https://github.com/ryanduguid/australian-accounting-skills australian-accounting-skills
New-Item -ItemType Directory -Force "$HOME/.claude/skills"
Copy-Item -Recurse australian-accounting-skills/.claude/skills/* "$HOME/.claude/skills/"
```

Or copy individual skill folders into `<project>/.claude/skills/`. The skills cross-reference each other (`bas-preparation`, `stp-finalisation`, `workpaper-tie-out`, `fbt-annual-workflow` and `xero-exports` are shared dependencies), so installing the full set works best. For a firm repository, adapt [`templates/firm-CLAUDE.md.example`](../templates/firm-CLAUDE.md.example) to its actual policy; this repository's [`CLAUDE.md`](../CLAUDE.md) is contributor guidance, not a substitute for firm controls.

### Versioning

The tagged `v0.2.0` release contains and tests all 19 skills as a set. The
earlier `v0.1.5` release contained the original nine practice skills. Installing
a subset by hand can break skills that call their siblings:

- `bas-preparation`, `month-end-close` and `year-end-workpapers` depend on `xero-exports`
- `fbt-annual-workflow` and `stp-finalisation` depend on each other (RFBA hand-off)
- `year-end-workpapers` depends on `bas-preparation`, `stp-finalisation` and `workpaper-tie-out`
- the contracting workflows use `contracting-exports` as their shared export
  reference, and the costing, claim, retention and WIP skills cross-reference
  each other

Every command under [Install](#install) resolves the default branch, which may
be ahead of the latest tag. To take the tagged 19-skill pack exactly as
released and verified, install from the tag instead:

```bash
git clone --branch v0.2.0 --depth 1 https://github.com/ryanduguid/australian-accounting-skills australian-accounting-skills
mkdir -p ~/.claude/skills
cp -r australian-accounting-skills/.claude/skills/* ~/.claude/skills/
```

Install the full tagged pack so the expanded set stays consistent. The
nine-skill `v0.1.5` pack remains available from its tag for anyone who cites
it.
