# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_global_settingsgeneral
from genie.libs.parser.bigip.get_ltm_global_settingsgeneral import (
    LtmGlobalsettingsGeneral,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/global-settings/general'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:global-settings:general:generalstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/global-settings/general?ver=14.1.2.1",
            "gratuitousArpRate": 0,
            "l2CacheTimeout": 300,
            "maintenanceMode": "disabled",
            "mgmtAutoLastHop": "enabled",
            "shareSingleMac": "vmw-compat",
            "snatPacketForward": "disabled",
        }


class test_get_ltm_global_settingsgeneral(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "gratuitousArpRate": 0,
        "kind": "tm:ltm:global-settings:general:generalstate",
        "l2CacheTimeout": 300,
        "maintenanceMode": "disabled",
        "mgmtAutoLastHop": "enabled",
        "selfLink": "https://localhost/mgmt/tm/ltm/global-settings/general?ver=14.1.2.1",
        "shareSingleMac": "vmw-compat",
        "snatPacketForward": "disabled",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmGlobalsettingsGeneral(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmGlobalsettingsGeneral(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
