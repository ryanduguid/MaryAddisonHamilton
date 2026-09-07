# v0.2.1

Changes since the last published release, `v0.2.0`. The inventory is the same
nineteen skills.

- `xero-exports` replaces its inferred parsing rules with conventions and
  header rows verified against Xero's own report exports. The skill's Parsing
  conventions and Observed column headers sections are the record: they name
  the export set (the Excel exports of 41 Demo Company (AU) reports plus the
  Overall Budget and Statement Lines CSV exports), carry the 5 September 2026
  check date beside each fact relied on, and say to re-verify when Xero
  changes a report layout.
- The validation pack gains a results schema and evaluation guide, and the
  first recorded validation run: 17 cards, 17 pass, `claude-opus-5` at
  `6e08f2a`, one fresh session per card with only that card and the skills it
  names loaded.
- The README leads with the synthetic BAS tie-out, AGENTS.md merges its
  duplicated repository summary and hand-off check lists, and the sibling
  tools point at their monorepo homes.
- `verify.yml` runs ruff and mypy in a lint job before the verification checks,
  which now run on Python 3.10, 3.12 and 3.13, and `pre-commit` runs the same
  ruff version on staged files. Every workflow carries a concurrency group and
  a job timeout, and text files normalise to LF.
- The release and verify workflows call the shared release-policy workflows at
  a commit reachable from that repository's `main` (`99a6314`) after the
  5 September history rewrite left the earlier pins dangling. The shared
  skill-verification canary reports on that pin.

# v0.2.0

Changes since the last published release, `v0.1.5`:

- The destination plugin is `australian-accounting-skills@ryanduguid`. Its
  nineteen skills include the ten incoming Hardhat Ledger skills:
  `coal-lsl-levy`, `contract-cost-tracking`, `contracting-exports`,
  `contractor-super-tpar`, `fuel-tax-credits`, `payroll-tax-contractors`,
  `plant-and-equipment-costing`, `progress-claim-preparation`,
  `retention-schedule` and `wip-over-under-billing`.
- Claude and Codex plugin discovery resolve the canonical `.claude/skills/`
  owner. `skills@1.5.22 add . --list` must discover the same nineteen skills.
- After a published and publicly verified destination release passes its gates,
  uninstall or disable `subcontractor-accounting-skills@ryanduguid-contracting`
  before installing `australian-accounting-skills@ryanduguid`. Never enable both
  packs at once because the ten transferred skill names collide.
- To roll back, uninstall the destination pack and reinstall Hardhat Ledger
  `v0.1.5`. Keep its release and tags intact.

# v0.1.5

Changes since the last published release, `v0.1.4`:

- The documented Claude Code install works again: the marketplace entry sets `strict: true`, resolving the conflicting-manifests error that made the plugin fail to load with zero skills registered.
- The project identity is Australian Accounting Skills everywhere a reader meets it: README and contributor-guide headings, the disclaimer's lead sentence, the banner and the release runbook.
- Every skill's Boundaries section closes with an inline not-advice line that survives copying a single skill folder out of the repository, except `stp-finalisation`, which shipped with a repository-relative `DISCLAIMER.md` link only. Its inline line landed after this release.
- bas-preparation's `sources.json` records provenance for the W3/W4 label facts and the $1,000 capital-purchases concession its text hedges.
- Repository topics are reconciled between docs/DISCOVERY.md, the publish script (which now sets the list wholesale) and the live About; Dependabot covers the pinned pip test dependency.
- The release runbook records that v0.1.1 to v0.1.4 predate the August 2026 history rewrite, so `gh release verify` fails permanently for them; this release restores end-to-end verification.

# v0.1.4

Changes since the last published release, `v0.1.3`:

- publish the W1 large-withholder mapping (#35) and Payday Super allowable-period / s 18C control (#36) that landed on `main` after `v0.1.3`, so the tagged zip matches git `main`;
- require an `UNKNOWN` / no-SGC missing-facts branch on the SG validation cards when first-contribution or s 18C facts are absent, and forbid a late classification from a seven-business-day count alone;
- name the sibling CLIs `payday-super-check` and `export-tb` / `xero-trial-balance-export` from the skills pack, without moving SGC calculation into the agent; and
- point year-end payroll/SG ageing at the Payday Super timing control in `stp-finalisation`, and add the ATO employer Payday Super URL beside the existing software-developer source.

Recovery note: `v0.1.2` is a protected annotated tag at `efc8c5b8f0b6bd1dee65eccba953cb1b60a4aaa4`, but it has no GitHub release. Its release run failed safely at the asset-inventory gate because that gate expected `SHA256SUMS` before creating it. Upload, attestation, draft creation and publication did not start. The tag will not be moved, deleted or reused.
