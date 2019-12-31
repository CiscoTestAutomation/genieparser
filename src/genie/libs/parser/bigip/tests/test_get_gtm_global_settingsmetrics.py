# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_gtm_global_settingsmetrics
from genie.libs.parser.bigip.get_gtm_global_settingsmetrics import (
    GtmGlobalsettingsMetrics,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/gtm/global-settings/metrics'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:gtm:global-settings:metrics:metricsstate",
            "selfLink": "https://localhost/mgmt/tm/gtm/global-settings/metrics?ver=14.1.2.1",
            "defaultProbeLimit": 12,
            "hopsPacketLength": 64,
            "hopsSampleCount": 3,
            "hopsTimeout": 3,
            "hopsTtl": 604800,
            "inactiveLdnsTtl": 2419200,
            "inactivePathsTtl": 604800,
            "ldnsUpdateInterval": 20,
            "maxSynchronousMonitorRequests": 20,
            "metricsCaching": 3600,
            "metricsCollectionProtocols": ["icmp"],
            "pathTtl": 2400,
            "pathsRetry": 120,
        }


class test_get_gtm_global_settingsmetrics(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "defaultProbeLimit": 12,
        "hopsPacketLength": 64,
        "hopsSampleCount": 3,
        "hopsTimeout": 3,
        "hopsTtl": 604800,
        "inactiveLdnsTtl": 2419200,
        "inactivePathsTtl": 604800,
        "kind": "tm:gtm:global-settings:metrics:metricsstate",
        "ldnsUpdateInterval": 20,
        "maxSynchronousMonitorRequests": 20,
        "metricsCaching": 3600,
        "metricsCollectionProtocols": ["icmp"],
        "pathTtl": 2400,
        "pathsRetry": 120,
        "selfLink": "https://localhost/mgmt/tm/gtm/global-settings/metrics?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = GtmGlobalsettingsMetrics(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = GtmGlobalsettingsMetrics(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
