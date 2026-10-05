import unittest
from pathlib import Path

from pyats.topology import Device

from genie.libs.parser.iosxe.rv1.show_platform import ShowInventory


class TestShowInventoryRev1MemberInventory(unittest.TestCase):

    def test_preserves_member_qualified_records(self):
        output = (
            Path(__file__).parent
            / "ShowInventory"
            / "cli"
            / "equal"
            / "golden_output_7_output.txt"
        ).read_text()
        parsed = ShowInventory(
            device=Device(name="svl", os="iosxe")
        ).cli(output=output)

        self.assertEqual(set(parsed["member"]), {"1", "2"})
        self.assertEqual(
            parsed["member"]["1"]["inventory"]
            ["Switch 1 Slot 1 Supervisor"]["pid"],
            "C9500X-28C8D",
        )
        self.assertEqual(
            parsed["member"]["2"]["inventory"]
            ["Switch 2 Chassis"]["sn"],
            "FDO25130VEC",
        )


if __name__ == "__main__":
    unittest.main()
