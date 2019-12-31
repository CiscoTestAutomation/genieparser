# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_net_cosglobal_settings
from genie.libs.parser.bigip.get_net_cosglobal_settings import (
    NetCosGlobalsettings,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/net/cos/global-settings'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:net:cos:global-settings:global-settingsstate",
            "selfLink": "https://localhost/mgmt/tm/net/cos/global-settings?ver=14.1.2.1",
            "featureDisabled": True,
            "precedence": "8021p-only",
        }


class test_get_net_cosglobal_settings(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "featureDisabled": True,
        "kind": "tm:net:cos:global-settings:global-settingsstate",
        "precedence": "8021p-only",
        "selfLink": "https://localhost/mgmt/tm/net/cos/global-settings?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = NetCosGlobalsettings(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = NetCosGlobalsettings(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
