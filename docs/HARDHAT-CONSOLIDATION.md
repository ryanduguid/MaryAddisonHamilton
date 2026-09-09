# Hardhat Ledger consolidation

This pack became the owner of the ten contracting skills transferred from
`ryanduguid/hardhat-ledger`. The integration source is immutable commit
`eb3b8a6ba47dfcdc05cea434f2f6a7dba82f96ef`. At transfer, every `SKILL.md`
matched that commit after canonical LF normalisation. The table preserves
that original inventory. Later destination-owned amendments are recorded
separately below; the other definitions still match their transferred bytes.

The `v0.2.0` destination release was published and verified on 2 September
2026, and `ryanduguid/hardhat-ledger` was archived on 3 September 2026. That
archive stays readable, so its last compatible release, tags and rollback link
remain available; no forwarding implementation was layered on it.

## Exact transferred inventory

| Skill | Source Git blob | Canonical SHA-256 |
|---|---|---|
| `coal-lsl-levy` | `2ad5d31656301cf18a4dafc863066c259cef00b1` | `c0330c9ec817435c731872452e5984040c89b16a5ad432193b0135ba1a322c23` |
| `contract-cost-tracking` | `cc8b1d2c98224c66eba6a5a8b7fd071f6165fdf9` | `c385d832d1bfc00bd4e4eed12c2b86740047049f50cfcf11325a5adbdc0e1690` |
| `contracting-exports` | `6ef0ebdeadb046710accd8c3956c7cfe60704230` | `bcfec0dd235e2940eb2f0a5c447f097bc2257d85cc723c1151b4c1885aef929e` |
| `contractor-super-tpar` | `1f2be7647fa2f4f37920c869d87e10761c2d8377` | `47ba8863485798b80cc25d1fe7485c58918b853032bc81e1f4128cce39e1eece` |
| `fuel-tax-credits` | `ef5b3121ca1cbbbc68ee300280e4a032c23b481c` | `a2721d3afc420b17a4a13503b046870564f1f8e6bc0700ed144376ace2ae99be` |
| `payroll-tax-contractors` | `408ab33363c73aa81720990307fd53c0174caacd` | `1e6e58397fb139c4c3d7320f3c3cf38e86f632517921e1942447a70189bc9108` |
| `plant-and-equipment-costing` | `4f796dcdd8fe3ea0cf128aea88c1968fd0a622d6` | `7718b8226306e3ec6c546758a2839ee04c6ea964e550fdf83586e4081cac80af` |
| `progress-claim-preparation` | `cf475ace966fb28416dde1608462ebd0f589ef5b` | `9d4b7bbf3789cab8c4e3e3686b7194eb6a7ec9f7604191151c4d5593917233e4` |
| `retention-schedule` | `063fe6910f4ed4165730658df6c5991a4061588c` | `84e23a7a268391cb352c3d1f36d7bb5628690b6aa390a0492cfc81106832373c` |
| `wip-over-under-billing` | `41ac43dca0b7489b42647d2203654822a191606a` | `c1aa5c432c41a5ac79ab384ce5ab7e472a555b6825faa01536e6e01aae8270b1` |

The reviewed legal and tax source record is retained in
[`source-review-2026-08-15.md`](source-review-2026-08-15.md). Its conclusions
remain bounded by the copied skills' use-time source checks and human-review
gates.

## Destination-owned amendments

On 9 September 2026, `contracting-exports` gained explicit manifest timestamp,
filter, total and rounding-bridge requirements, including re-export after a
filter change and pending authorised review. This responds to the recorded
`export-manifest-rounding` failure; fresh model verification is pending.
Its canonical SHA-256 after that amendment was
`07caf7a2e2aacc371ec6693e56fbd3e3b7679381b72abeb4a6de5f4e671adf6f`.

Later on 9 September 2026, its client-data boundary stopped accepting ignore
coverage as the safeguard for where exports and generated output may be
written, and now requires a location outside every version-control checkout.
The skill already forbade a repository fallback in its portable safety
boundary, so the earlier wording contradicted the same file two sections
above it. Its amended canonical SHA-256 is
`d39b1a6479b6f73d373b51841555e8ef276135b9879594a2064c0a69cdbec3f4`.
The transfer hash above remains the historical source record.

## Migration order

Existing Hardhat users must uninstall or disable
`subcontractor-accounting-skills@ryanduguid-contracting` before installing
`australian-accounting-skills@ryanduguid`. The ten names are stable
compatibility identifiers, so never enable both packs at once.

## Rollback

If destination discovery, validation or behaviour regresses, uninstall the
destination pack and reinstall Hardhat Ledger
[`v0.1.5`](https://github.com/ryanduguid/hardhat-ledger/releases/tag/v0.1.5).
The archived repository is read-only, so that release and its tags stay
available. Do not rename skills, rewrite tags or keep two active owners as a
workaround.
