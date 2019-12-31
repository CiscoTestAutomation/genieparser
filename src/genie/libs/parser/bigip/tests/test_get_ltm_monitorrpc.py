# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_monitorrpc
from genie.libs.parser.bigip.get_ltm_monitorrpc import LtmMonitorRpc

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/monitor/rpc'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:monitor:rpc:rpccollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/monitor/rpc?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:monitor:rpc:rpcstate",
                    "name": "rpc",
                    "partition": "Common",
                    "fullPath": "/Common/rpc",
                    "generation": 0,
                    "selfLink": "https://localhost/mgmt/tm/ltm/monitor/rpc/~Common~rpc?ver=14.1.2.1",
                    "debug": "no",
                    "destination": "*:*",
                    "interval": 10,
                    "manualResume": "disabled",
                    "mode": "tcp",
                    "timeUntilUp": 0,
                    "timeout": 31,
                    "upInterval": 0,
                }
            ],
        }


class test_get_ltm_monitorrpc(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "debug": "no",
                "destination": "*:*",
                "fullPath": "/Common/rpc",
                "generation": 0,
                "interval": 10,
                "kind": "tm:ltm:monitor:rpc:rpcstate",
                "manualResume": "disabled",
                "mode": "tcp",
                "name": "rpc",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/monitor/rpc/~Common~rpc?ver=14.1.2.1",
                "timeUntilUp": 0,
                "timeout": 31,
                "upInterval": 0,
            }
        ],
        "kind": "tm:ltm:monitor:rpc:rpccollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/monitor/rpc?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmMonitorRpc(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmMonitorRpc(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
