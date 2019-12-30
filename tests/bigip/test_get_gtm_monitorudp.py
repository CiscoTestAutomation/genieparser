# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_gtm_monitorudp
from genie.libs.parser.bigip.get_gtm_monitorudp import GtmMonitorUdp

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/gtm/monitor/udp'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:gtm:monitor:udp:udpcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/gtm/monitor/udp?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:gtm:monitor:udp:udpstate",
                    "name": "udp",
                    "partition": "Common",
                    "fullPath": "/Common/udp",
                    "generation": 0,
                    "selfLink": "https://localhost/mgmt/tm/gtm/monitor/udp/~Common~udp?ver=14.1.2.1",
                    "debug": "no",
                    "destination": "*:*",
                    "ignoreDownResponse": "disabled",
                    "interval": 30,
                    "probeAttempts": 3,
                    "probeInterval": 1,
                    "probeTimeout": 5,
                    "reverse": "disabled",
                    "send": "default send string",
                    "timeout": 120,
                    "transparent": "disabled",
                }
            ],
        }


class test_get_gtm_monitorudp(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "debug": "no",
                "destination": "*:*",
                "fullPath": "/Common/udp",
                "generation": 0,
                "ignoreDownResponse": "disabled",
                "interval": 30,
                "kind": "tm:gtm:monitor:udp:udpstate",
                "name": "udp",
                "partition": "Common",
                "probeAttempts": 3,
                "probeInterval": 1,
                "probeTimeout": 5,
                "reverse": "disabled",
                "selfLink": "https://localhost/mgmt/tm/gtm/monitor/udp/~Common~udp?ver=14.1.2.1",
                "send": "default send string",
                "timeout": 120,
                "transparent": "disabled",
            }
        ],
        "kind": "tm:gtm:monitor:udp:udpcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/gtm/monitor/udp?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = GtmMonitorUdp(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = GtmMonitorUdp(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
