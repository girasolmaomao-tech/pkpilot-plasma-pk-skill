import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class PublicDistributionTests(unittest.TestCase):
    def test_backend_source_is_not_present(self):
        forbidden = [
            path
            for path in ROOT.rglob("*.py")
            if path.relative_to(ROOT).parts[0] not in {"scripts", "tests"}
        ]
        self.assertEqual(forbidden, [])
        self.assertFalse((ROOT / "src").exists())
        self.assertFalse((ROOT / "plugins").exists())
        self.assertFalse((ROOT / "scripts" / "src").exists())

    def test_checksum_is_pinned_in_installer(self):
        checksum_line = (ROOT / "checksums.txt").read_text(encoding="utf-8").strip()
        checksum = checksum_line.split()[0]
        self.assertRegex(checksum, r"^[0-9a-f]{64}$")
        installer = (ROOT / "scripts" / "install_pkpilot.sh").read_text(encoding="utf-8")
        self.assertIn(checksum, installer)

    def test_skill_has_no_todo_placeholders(self):
        text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIsNone(re.search(r"\[TODO:", text))

    def test_public_assets_contain_no_study_demo(self):
        self.assertEqual(
            sorted(path.name for path in (ROOT / "assets").iterdir()),
            ["pk_input_template.xlsx"],
        )


if __name__ == "__main__":
    unittest.main()
