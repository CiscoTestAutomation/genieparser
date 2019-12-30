# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_net_stp_globals
from genie.libs.parser.bigip.get_net_stp_globals import NetStpglobals

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/net/stp-globals'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:net:stp-globals:stp-globalsstate",
            "selfLink": "https://localhost/mgmt/tm/net/stp-globals?ver=14.1.2.1",
            "configRevision": 0,
            "fwdDelay": 15,
            "helloTime": 2,
            "maxAge": 20,
            "maxHops": 20,
            "mode": "passthru",
            "transmitHold": 6,
        }


class test_get_net_stp_globals(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "configRevision": 0,
        "fwdDelay": 15,
        "helloTime": 2,
        "kind": "tm:net:stp-globals:stp-globalsstate",
        "maxAge": 20,
        "maxHops": 20,
        "mode": "passthru",
        "selfLink": "https://localhost/mgmt/tm/net/stp-globals?ver=14.1.2.1",
        "transmitHold": 6,
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = NetStpglobals(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = NetStpglobals(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
