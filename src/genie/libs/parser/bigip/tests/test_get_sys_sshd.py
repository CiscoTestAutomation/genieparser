# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_sshd
from genie.libs.parser.bigip.get_sys_sshd import SysSshd

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/sshd'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:sshd:sshdstate",
            "selfLink": "https://localhost/mgmt/tm/sys/sshd?ver=14.1.2.1",
            "allow": ["ALL"],
            "banner": "enabled",
            "bannerText": " __omit_place_holder__345005cc4fdfd5af832f1cc9559086e384b26499",
            "fipsCipherVersion": 0,
            "inactivityTimeout": 0,
            "logLevel": "info",
            "login": "enabled",
            "port": 22,
        }


class test_get_sys_sshd(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "allow": ["ALL"],
        "banner": "enabled",
        "bannerText": " __omit_place_holder__345005cc4fdfd5af832f1cc9559086e384b26499",
        "fipsCipherVersion": 0,
        "inactivityTimeout": 0,
        "kind": "tm:sys:sshd:sshdstate",
        "logLevel": "info",
        "login": "enabled",
        "port": 22,
        "selfLink": "https://localhost/mgmt/tm/sys/sshd?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysSshd(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysSshd(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
