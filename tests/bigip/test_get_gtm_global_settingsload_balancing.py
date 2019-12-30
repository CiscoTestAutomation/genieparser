# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_gtm_global_settingsload_balancing
from genie.libs.parser.bigip.get_gtm_global_settingsload_balancing import (
    GtmGlobalsettingsLoadbalancing,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/gtm/global-settings/load-balancing'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:gtm:global-settings:load-balancing:load-balancingstate",
            "selfLink": "https://localhost/mgmt/tm/gtm/global-settings/load-balancing?ver=14.1.2.1",
            "failureRcode": "noerror",
            "failureRcodeResponse": "disabled",
            "failureRcodeTtl": 0,
            "ignorePathTtl": "no",
            "qosFactorBps": 1000000,
            "qosFactorHitRatio": 10000,
            "qosFactorHops": 25,
            "qosFactorLinkCapacity": 1,
            "qosFactorPacketRate": 10000,
            "qosFactorRtt": 10000,
            "qosFactorTopology": 10,
            "qosFactorVsCapacity": 1,
            "qosFactorVsScore": 1,
            "respectFallbackDependency": "no",
            "topologyAllowZeroScores": "yes",
            "topologyLongestMatch": "yes",
            "topologyPreferEdns0ClientSubnet": "disabled",
            "verifyVsAvailability": "yes",
        }


class test_get_gtm_global_settingsload_balancing(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "failureRcode": "noerror",
        "failureRcodeResponse": "disabled",
        "failureRcodeTtl": 0,
        "ignorePathTtl": "no",
        "kind": "tm:gtm:global-settings:load-balancing:load-balancingstate",
        "qosFactorBps": 1000000,
        "qosFactorHitRatio": 10000,
        "qosFactorHops": 25,
        "qosFactorLinkCapacity": 1,
        "qosFactorPacketRate": 10000,
        "qosFactorRtt": 10000,
        "qosFactorTopology": 10,
        "qosFactorVsCapacity": 1,
        "qosFactorVsScore": 1,
        "respectFallbackDependency": "no",
        "selfLink": "https://localhost/mgmt/tm/gtm/global-settings/load-balancing?ver=14.1.2.1",
        "topologyAllowZeroScores": "yes",
        "topologyLongestMatch": "yes",
        "topologyPreferEdns0ClientSubnet": "disabled",
        "verifyVsAvailability": "yes",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = GtmGlobalsettingsLoadbalancing(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = GtmGlobalsettingsLoadbalancing(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
