# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_global_settingstraffic_control
from genie.libs.parser.bigip.get_ltm_global_settingstraffic_control import (
    LtmGlobalsettingsTrafficcontrol,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/global-settings/traffic-control'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:global-settings:traffic-control:traffic-controlstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/global-settings/traffic-control?ver=14.1.2.1",
            "acceptIpOptions": "disabled",
            "acceptIpSourceRoute": "disabled",
            "allowIpSourceRoute": "disabled",
            "continueMatching": "disabled",
            "maxIcmpRate": 100,
            "maxRejectRate": 250,
            "maxRejectRateTimeout": 30,
            "minPathMtu": 296,
            "pathMtuDiscovery": "enabled",
            "portFindLinear": 16,
            "portFindRandom": 16,
            "portFindThresholdTimeout": 30,
            "portFindThresholdTrigger": 8,
            "portFindThresholdWarning": "enabled",
            "rejectUnmatched": "enabled",
        }


class test_get_ltm_global_settingstraffic_control(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "acceptIpOptions": "disabled",
        "acceptIpSourceRoute": "disabled",
        "allowIpSourceRoute": "disabled",
        "continueMatching": "disabled",
        "kind": "tm:ltm:global-settings:traffic-control:traffic-controlstate",
        "maxIcmpRate": 100,
        "maxRejectRate": 250,
        "maxRejectRateTimeout": 30,
        "minPathMtu": 296,
        "pathMtuDiscovery": "enabled",
        "portFindLinear": 16,
        "portFindRandom": 16,
        "portFindThresholdTimeout": 30,
        "portFindThresholdTrigger": 8,
        "portFindThresholdWarning": "enabled",
        "rejectUnmatched": "enabled",
        "selfLink": "https://localhost/mgmt/tm/ltm/global-settings/traffic-control?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmGlobalsettingsTrafficcontrol(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmGlobalsettingsTrafficcontrol(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
