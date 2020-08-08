import unittest
from unittest.mock import Mock

from genie.metaparser.util.exceptions import SchemaEmptyParserError
from genie.libs.parser.iosxe.show_stackwise_virtual import ShowStackwiseVirtual


# ======================================
# Unit test for 'show stackwise-virtual'
# ======================================
class test_show_stackwise_virtual(unittest.TestCase):
    """Unit test for 'show stackwise-virtual'"""

    maxDiff = None
    empty_output = {"execute.return_value": ""}
    golden_parsed_output1 = {
        "domain": 100,
        "enabled": True,
        "switches": {
            1: {
               "stackwise_virtual_link": {
                 1: {
                    "ports": ["HundredGigE1/0/3", "HundredGigE1/0/4"],
                 },
               },
            },
            2: {
               "stackwise_virtual_link": {
                 1: {
                   "ports": ["HundredGigE2/0/3", "HundredGigE2/0/4"],
                 },
               },
            },
        },
    }

    golden_output1 = {
        "execute.return_value": "Stackwise Virtual Configuration:\n"
        "--------------------------------\n"
        "Stackwise Virtual : Enabled\n"
        "Domain Number : 100\n"
        "\n"
        "Switch  Stackwise Virtual Link  Ports\n"
        "------  ----------------------  ------\n"
        "1       1                       HundredGigE1/0/3\n"
        "                                HundredGigE1/0/4\n"
        "2       1                       HundredGigE2/0/3\n"
        "                                HundredGigE2/0/4\n"
    }

    def test_show_stackwise_virtual_full(self):
        self.device = Mock(**self.golden_output1)
        obj = ShowStackwiseVirtual(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_stackwise_virtual_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowStackwiseVirtual(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


if __name__ == "__main__":
    unittest.main()
