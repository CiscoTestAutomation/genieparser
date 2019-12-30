# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_monitorreal_server
from genie.libs.parser.bigip.get_ltm_monitorreal_server import (
    LtmMonitorRealserver,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/monitor/real-server'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:monitor:real-server:real-servercollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/monitor/real-server?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:monitor:real-server:real-serverstate",
                    "name": "real_server",
                    "partition": "Common",
                    "fullPath": "/Common/real_server",
                    "generation": 0,
                    "selfLink": "https://localhost/mgmt/tm/ltm/monitor/real-server/~Common~real_server?ver=14.1.2.1",
                    "agent": "Mozilla/4.0 (compatible: MSIE 5.0; Windows NT)",
                    "tmCommand": "GetServerStats",
                    "interval": 5,
                    "method": "GET",
                    "metrics": "ServerBandwidth:1.5, CPUPercentUsage, MemoryUsage, TotalClientCount",
                    "timeUntilUp": 0,
                    "timeout": 16,
                }
            ],
        }


class test_get_ltm_monitorreal_server(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "agent": "Mozilla/4.0 (compatible: MSIE 5.0; Windows NT)",
                "fullPath": "/Common/real_server",
                "generation": 0,
                "interval": 5,
                "kind": "tm:ltm:monitor:real-server:real-serverstate",
                "method": "GET",
                "metrics": "ServerBandwidth:1.5, CPUPercentUsage, MemoryUsage, "
                "TotalClientCount",
                "name": "real_server",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/monitor/real-server/~Common~real_server?ver=14.1.2.1",
                "timeUntilUp": 0,
                "timeout": 16,
                "tmCommand": "GetServerStats",
            }
        ],
        "kind": "tm:ltm:monitor:real-server:real-servercollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/monitor/real-server?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmMonitorRealserver(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmMonitorRealserver(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
