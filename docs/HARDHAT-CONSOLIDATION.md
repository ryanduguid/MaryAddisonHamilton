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

Later still on 9 September 2026, the same client-data boundary was carried
across the other nine transferred skills, which had kept the earlier wording.
Monthly Close Controls is gaining a guard that refuses any output path beneath
a checkout marker outright, so a skill that asked only for output kept out of
version control could send an agent to a path the command then rejects. That
behaviour is proposed in
[accounting-review-pipeline PR 134](https://github.com/ryanduguid/accounting-review-pipeline/pull/134),
read on 9 September 2026, and is in no released version of `close-control` yet.
Re-check the release actually installed before relying on it. The table records
their amended canonical SHA-256 values.

| Skill | Amended SHA-256 |
| --- | --- |
| `coal-lsl-levy` | `6b49ab510a171517a7385e4bf019fba4e57fcf162ebe4edaaf0da3b261721a12` |
| `contract-cost-tracking` | `b68116aa00a401d8934fe50490ea4361f7e4e176d717e1695e6486873be4493a` |
| `contractor-super-tpar` | `8cc6dfaf4181c6b1be86fc269b39415fb0db58639e12c58d6300fd723a2e1b0c` |
| `fuel-tax-credits` | `ef2641203848f74e4cb882eba811d97cc62255431ff7b059715a2b55f6e5ab3e` |
| `payroll-tax-contractors` | `e3ac75e4813a530aa8e3c89840309f84ca531dbc035e582512bcb6ff3fcd3124` |
| `plant-and-equipment-costing` | `4893bbed2aab75f01a4ffe21491a9b65985b35c335d21bf6069c81fdc7679f78` |
| `progress-claim-preparation` | `e809b5ba58abaea107c38b02ef734524cf95d293b562a6e7125fa033b5d95392` |
| `retention-schedule` | `356d4bf0689d480bd467a87ab7256ac071ca5e1c4f128c79c77757a0d9245c52` |
| `wip-over-under-billing` | `554f05d8c6f8b3d7fb2704e192b04ef5dca9ee7d039d424a4bb56596334355a6` |

Their transfer hashes above remain the historical source record.

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

## Spelling amendment, 11 September 2026

Original prose now uses Australian English `lodgement`. Official source titles,
original transfer hashes and earlier amendment records remain intact. This changes
spelling only. Source-review dates, refusal rules and human authority stay as recorded.

| Skill | Amended canonical SHA-256 |
|---|---|
| `coal-lsl-levy` | `a189220a63ce47fa6d251f2aba82f4c64ccfedc1cbe6f20687620dc8495d3cec` |
| `contractor-super-tpar` | `0cd72dc506d3b53a335ed27316e81e075ad40e68ea17ee74d712682ab4d1e8e2` |
| `fuel-tax-credits` | `06d08d8b4d980557abc4c4f04321edd52f7c749710d99d0add5488a2b319ecdc` |
| `payroll-tax-contractors` | `f635b19f6a857fc2f72a63866462117245543f75f0ed3cfa615f3cd7d1e1ebf2` |
