# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_net_dag_globals
from genie.libs.parser.bigip.get_net_dag_globals import NetDagglobals

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/net/dag-globals'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:net:dag-globals:dag-globalsstate",
            "selfLink": "https://localhost/mgmt/tm/net/dag-globals?ver=14.1.2.1",
            "dagIpv6PrefixLen": 128,
            "icmpHash": "icmp",
            "roundRobinMode": "global",
        }


class test_get_net_dag_globals(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "dagIpv6PrefixLen": 128,
        "icmpHash": "icmp",
        "kind": "tm:net:dag-globals:dag-globalsstate",
        "roundRobinMode": "global",
        "selfLink": "https://localhost/mgmt/tm/net/dag-globals?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = NetDagglobals(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = NetDagglobals(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
