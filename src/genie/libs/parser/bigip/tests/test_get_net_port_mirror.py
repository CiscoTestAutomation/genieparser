# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_net_port_mirror
from genie.libs.parser.bigip.get_net_port_mirror import NetPortmirror

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/net/port-mirror'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:net:port-mirror:port-mirrorcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/net/port-mirror?ver=14.1.2.1",
            "items": [],
        }


class test_get_net_port_mirror(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [],
        "kind": "tm:net:port-mirror:port-mirrorcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/net/port-mirror?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = NetPortmirror(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = NetPortmirror(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
