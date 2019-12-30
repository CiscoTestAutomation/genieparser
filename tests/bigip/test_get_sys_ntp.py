# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_ntp
from genie.libs.parser.bigip.get_sys_ntp import SysNtp

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/ntp'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:ntp:ntpstate",
            "selfLink": "https://localhost/mgmt/tm/sys/ntp?ver=14.1.2.1",
            "servers": ["172.27.1.1", "172.27.1.2"],
            "timezone": "America/Los_Angeles",
            "restrictReference": {
                "link": "https://localhost/mgmt/tm/sys/ntp/restrict?ver=14.1.2.1",
                "isSubcollection": True,
            },
        }


class test_get_sys_ntp(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "kind": "tm:sys:ntp:ntpstate",
        "restrictReference": {
            "isSubcollection": True,
            "link": "https://localhost/mgmt/tm/sys/ntp/restrict?ver=14.1.2.1",
        },
        "selfLink": "https://localhost/mgmt/tm/sys/ntp?ver=14.1.2.1",
        "servers": ["172.27.1.1", "172.27.1.2"],
        "timezone": "America/Los_Angeles",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysNtp(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysNtp(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
