# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_dns
from genie.libs.parser.bigip.get_sys_dns import SysDns

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/dns'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:dns:dnsstate",
            "selfLink": "https://localhost/mgmt/tm/sys/dns?ver=14.1.2.1",
            "description": "configured-by-dhcp",
            "nameServers": ["8.8.8.8", "4.4.4.4", "200.200.2.2"],
            "numberOfDots": 0,
            "search": ["local", "localhost"],
        }


class test_get_sys_dns(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "description": "configured-by-dhcp",
        "kind": "tm:sys:dns:dnsstate",
        "nameServers": ["8.8.8.8", "4.4.4.4", "200.200.2.2"],
        "numberOfDots": 0,
        "search": ["local", "localhost"],
        "selfLink": "https://localhost/mgmt/tm/sys/dns?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysDns(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysDns(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
