# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_global_settingsconnection
from genie.libs.parser.bigip.get_ltm_global_settingsconnection import (
    LtmGlobalsettingsConnection,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/global-settings/connection'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:global-settings:connection:connectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/global-settings/connection?ver=14.1.2.1",
            "adaptiveReaperHiwater": 95,
            "adaptiveReaperLowater": 85,
            "autoLastHop": "enabled",
            "defaultVsSynChallengeThreshold": "infinite",
            "globalFlowEvictionPolicy": "/Common/default-eviction-policy",
            "globalFlowEvictionPolicyReference": {
                "link": "https://localhost/mgmt/tm/ltm/eviction-policy/~Common~default-eviction-policy?ver=14.1.2.1"
            },
            "globalSynChallengeThreshold": "64000",
            "syncookiesThreshold": 16384,
            "vlanKeyedConn": "enabled",
            "vlanSynCookie": "enabled",
        }


class test_get_ltm_global_settingsconnection(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "adaptiveReaperHiwater": 95,
        "adaptiveReaperLowater": 85,
        "autoLastHop": "enabled",
        "defaultVsSynChallengeThreshold": "infinite",
        "globalFlowEvictionPolicy": "/Common/default-eviction-policy",
        "globalFlowEvictionPolicyReference": {
            "link": "https://localhost/mgmt/tm/ltm/eviction-policy/~Common~default-eviction-policy?ver=14.1.2.1"
        },
        "globalSynChallengeThreshold": "64000",
        "kind": "tm:ltm:global-settings:connection:connectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/global-settings/connection?ver=14.1.2.1",
        "syncookiesThreshold": 16384,
        "vlanKeyedConn": "enabled",
        "vlanSynCookie": "enabled",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmGlobalsettingsConnection(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmGlobalsettingsConnection(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
