# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_profiletcp_analytics
from genie.libs.parser.bigip.get_ltm_profiletcp_analytics import (
    LtmProfileTcpanalytics,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/profile/tcp-analytics'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:profile:tcp-analytics:tcp-analyticscollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/profile/tcp-analytics?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:profile:tcp-analytics:tcp-analyticsstate",
                    "name": "tcp-analytics",
                    "partition": "Common",
                    "fullPath": "/Common/tcp-analytics",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/profile/tcp-analytics/~Common~tcp-analytics?ver=14.1.2.1",
                    "appService": "none",
                    "collectCity": "disabled",
                    "collectContinent": "enabled",
                    "collectCountry": "enabled",
                    "collectNexthop": "disabled",
                    "collectPostCode": "disabled",
                    "collectRegion": "disabled",
                    "collectRemoteHostIp": "disabled",
                    "collectRemoteHostSubnet": "enabled",
                    "collectedByClientSide": "enabled",
                    "collectedByServerSide": "disabled",
                    "collectedStatsExternalLogging": "disabled",
                    "collectedStatsInternalLogging": "enabled",
                    "defaultsFrom": "none",
                    "description": "none",
                    "externalLoggingPublisher": "none",
                }
            ],
        }


class test_get_ltm_profiletcp_analytics(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "appService": "none",
                "collectCity": "disabled",
                "collectContinent": "enabled",
                "collectCountry": "enabled",
                "collectNexthop": "disabled",
                "collectPostCode": "disabled",
                "collectRegion": "disabled",
                "collectRemoteHostIp": "disabled",
                "collectRemoteHostSubnet": "enabled",
                "collectedByClientSide": "enabled",
                "collectedByServerSide": "disabled",
                "collectedStatsExternalLogging": "disabled",
                "collectedStatsInternalLogging": "enabled",
                "defaultsFrom": "none",
                "description": "none",
                "externalLoggingPublisher": "none",
                "fullPath": "/Common/tcp-analytics",
                "generation": 1,
                "kind": "tm:ltm:profile:tcp-analytics:tcp-analyticsstate",
                "name": "tcp-analytics",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/profile/tcp-analytics/~Common~tcp-analytics?ver=14.1.2.1",
            }
        ],
        "kind": "tm:ltm:profile:tcp-analytics:tcp-analyticscollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/profile/tcp-analytics?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmProfileTcpanalytics(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmProfileTcpanalytics(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
