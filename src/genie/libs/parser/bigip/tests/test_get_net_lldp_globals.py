# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_net_lldp_globals
from genie.libs.parser.bigip.get_net_lldp_globals import NetLldpglobals

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/net/lldp-globals'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:net:lldp-globals:lldp-globalsstate",
            "selfLink": "https://localhost/mgmt/tm/net/lldp-globals?ver=14.1.2.1",
            "disabled": True,
            "maxNeighborsPerPort": 10,
            "reinitDelay": 2,
            "txDelay": 2,
            "txHold": 4,
            "txInterval": 30,
        }


class test_get_net_lldp_globals(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "disabled": True,
        "kind": "tm:net:lldp-globals:lldp-globalsstate",
        "maxNeighborsPerPort": 10,
        "reinitDelay": 2,
        "selfLink": "https://localhost/mgmt/tm/net/lldp-globals?ver=14.1.2.1",
        "txDelay": 2,
        "txHold": 4,
        "txInterval": 30,
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = NetLldpglobals(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = NetLldpglobals(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
