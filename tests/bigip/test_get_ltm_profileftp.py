# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_profileftp
from genie.libs.parser.bigip.get_ltm_profileftp import LtmProfileFtp

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/profile/ftp'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:profile:ftp:ftpcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/profile/ftp?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:profile:ftp:ftpstate",
                    "name": "ftp",
                    "partition": "Common",
                    "fullPath": "/Common/ftp",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/profile/ftp/~Common~ftp?ver=14.1.2.1",
                    "allowActiveMode": "enabled",
                    "allowFtps": "disabled",
                    "appService": "none",
                    "defaultsFrom": "none",
                    "description": "none",
                    "enforceTlsSessionReuse": "disabled",
                    "ftpsMode": "disallow",
                    "inheritParentProfile": "disabled",
                    "inheritVlanList": "disabled",
                    "logProfile": "none",
                    "logPublisher": "none",
                    "port": 20,
                    "security": "disabled",
                    "translateExtended": "enabled",
                }
            ],
        }


class test_get_ltm_profileftp(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "allowActiveMode": "enabled",
                "allowFtps": "disabled",
                "appService": "none",
                "defaultsFrom": "none",
                "description": "none",
                "enforceTlsSessionReuse": "disabled",
                "ftpsMode": "disallow",
                "fullPath": "/Common/ftp",
                "generation": 1,
                "inheritParentProfile": "disabled",
                "inheritVlanList": "disabled",
                "kind": "tm:ltm:profile:ftp:ftpstate",
                "logProfile": "none",
                "logPublisher": "none",
                "name": "ftp",
                "partition": "Common",
                "port": 20,
                "security": "disabled",
                "selfLink": "https://localhost/mgmt/tm/ltm/profile/ftp/~Common~ftp?ver=14.1.2.1",
                "translateExtended": "enabled",
            }
        ],
        "kind": "tm:ltm:profile:ftp:ftpcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/profile/ftp?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmProfileFtp(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmProfileFtp(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
