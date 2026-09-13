"""Replacement contracts for the Hardhat Ledger skill consolidation."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import unittest


REPOSITORY = Path(__file__).resolve().parents[1]
SKILLS = REPOSITORY / ".claude" / "skills"
SOURCE_COMMIT = "eb3b8a6ba47dfcdc05cea434f2f6a7dba82f96ef"
TRANSFERRED_SKILL_HASHES = {
    "coal-lsl-levy": "c0330c9ec817435c731872452e5984040c89b16a5ad432193b0135ba1a322c23",
    "contract-cost-tracking": "c385d832d1bfc00bd4e4eed12c2b86740047049f50cfcf11325a5adbdc0e1690",
    "contracting-exports": "bcfec0dd235e2940eb2f0a5c447f097bc2257d85cc723c1151b4c1885aef929e",
    "contractor-super-tpar": "47ba8863485798b80cc25d1fe7485c58918b853032bc81e1f4128cce39e1eece",
    "fuel-tax-credits": "a2721d3afc420b17a4a13503b046870564f1f8e6bc0700ed144376ace2ae99be",
    "payroll-tax-contractors": "1e6e58397fb139c4c3d7320f3c3cf38e86f632517921e1942447a70189bc9108",
    "plant-and-equipment-costing": "7718b8226306e3ec6c546758a2839ee04c6ea964e550fdf83586e4081cac80af",
    "progress-claim-preparation": "9d4b7bbf3789cab8c4e3e3686b7194eb6a7ec9f7604191151c4d5593917233e4",
    "retention-schedule": "84e23a7a268391cb352c3d1f36d7bb5628690b6aa390a0492cfc81106832373c",
    "wip-over-under-billing": "c1aa5c432c41a5ac79ab384ce5ab7e472a555b6825faa01536e6e01aae8270b1",
}

# Destination-owned changes are recorded separately from the original transfer.
AMENDED_SKILL_HASHES = {
    "coal-lsl-levy": "d77c86459d3bff0761b079fcaea84e73673ecea8f027fa5c018fcfe3dca08bc3",
    "contract-cost-tracking": "b68116aa00a401d8934fe50490ea4361f7e4e176d717e1695e6486873be4493a",
    "contracting-exports": "a84b6a267206fa7e03d3cd55d4367965cca438dd5236ff2f3ad02037f856238b",
    "contractor-super-tpar": "0cd72dc506d3b53a335ed27316e81e075ad40e68ea17ee74d712682ab4d1e8e2",
    "fuel-tax-credits": "06d08d8b4d980557abc4c4f04321edd52f7c749710d99d0add5488a2b319ecdc",
    "payroll-tax-contractors": "f635b19f6a857fc2f72a63866462117245543f75f0ed3cfa615f3cd7d1e1ebf2",
    "plant-and-equipment-costing": "4893bbed2aab75f01a4ffe21491a9b65985b35c335d21bf6069c81fdc7679f78",
    "progress-claim-preparation": "e809b5ba58abaea107c38b02ef734524cf95d293b562a6e7125fa033b5d95392",
    "retention-schedule": "356d4bf0689d480bd467a87ab7256ac071ca5e1c4f128c79c77757a0d9245c52",
    "wip-over-under-billing": "47d284ce45e07a062f2d1f5e4d62c5b7f6351e0281a18790c9022797bde44efa",
}


class HardhatConsolidationTests(unittest.TestCase):
    def test_skill_bytes_match_the_transfer_or_documented_amendment(self) -> None:
        record = (REPOSITORY / "docs" / "HARDHAT-CONSOLIDATION.md").read_text(
            encoding="utf-8"
        )
        for name, expected_hash in TRANSFERRED_SKILL_HASHES.items():
            with self.subTest(skill=name):
                self.assertIn(expected_hash, record)
                expected_hash = AMENDED_SKILL_HASHES.get(name, expected_hash)
                self.assertIn(expected_hash, record)
                content = (SKILLS / name / "SKILL.md").read_bytes()
                canonical = content.replace(b"\r\n", b"\n")
                self.assertNotIn(b"\r", canonical)
                self.assertEqual(hashlib.sha256(canonical).hexdigest(), expected_hash)

    def test_marketplace_exposes_the_complete_fifty_skill_inventory(self) -> None:
        marketplace = json.loads(
            (REPOSITORY / ".claude-plugin" / "marketplace.json").read_text(
                encoding="utf-8"
            )
        )
        declared = {
            Path(item).name for item in marketplace["plugins"][0]["skills"]
        }
        discovered = {
            path.parent.name for path in SKILLS.glob("*/SKILL.md")
        }
        self.assertEqual(declared, discovered)
        self.assertEqual(len(discovered), 50)
        self.assertLessEqual(set(TRANSFERRED_SKILL_HASHES), discovered)

    def test_transition_record_preserves_replace_then_remove_order(self) -> None:
        record = (REPOSITORY / "docs" / "HARDHAT-CONSOLIDATION.md").read_text(
            encoding="utf-8"
        )
        self.assertIn(SOURCE_COMMIT, record)
        self.assertIn("uninstall", record.lower())
        self.assertIn("before installing", record.lower())
        self.assertIn("rollback", record.lower())
        self.assertIn("v0.1.5", record)
        self.assertNotIn("install both", record.lower())


if __name__ == "__main__":
    unittest.main()
