# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_monitortcp_half_open
from genie.libs.parser.bigip.get_ltm_monitortcp_half_open import (
    LtmMonitorTcphalfopen,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/monitor/tcp-half-open'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:monitor:tcp-half-open:tcp-half-opencollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/monitor/tcp-half-open?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:monitor:tcp-half-open:tcp-half-openstate",
                    "name": "tcp_half_open",
                    "partition": "Common",
                    "fullPath": "/Common/tcp_half_open",
                    "generation": 0,
                    "selfLink": "https://localhost/mgmt/tm/ltm/monitor/tcp-half-open/~Common~tcp_half_open?ver=14.1.2.1",
                    "destination": "*:*",
                    "interval": 5,
                    "manualResume": "disabled",
                    "timeUntilUp": 0,
                    "timeout": 16,
                    "transparent": "disabled",
                    "upInterval": 0,
                }
            ],
        }


class test_get_ltm_monitortcp_half_open(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "destination": "*:*",
                "fullPath": "/Common/tcp_half_open",
                "generation": 0,
                "interval": 5,
                "kind": "tm:ltm:monitor:tcp-half-open:tcp-half-openstate",
                "manualResume": "disabled",
                "name": "tcp_half_open",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/monitor/tcp-half-open/~Common~tcp_half_open?ver=14.1.2.1",
                "timeUntilUp": 0,
                "timeout": 16,
                "transparent": "disabled",
                "upInterval": 0,
            }
        ],
        "kind": "tm:ltm:monitor:tcp-half-open:tcp-half-opencollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/monitor/tcp-half-open?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmMonitorTcphalfopen(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmMonitorTcphalfopen(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
