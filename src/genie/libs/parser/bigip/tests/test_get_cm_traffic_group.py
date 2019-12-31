# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_cm_traffic_group
from genie.libs.parser.bigip.get_cm_traffic_group import CmTrafficgroup

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/cm/traffic-group'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:cm:traffic-group:traffic-groupcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/cm/traffic-group?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:cm:traffic-group:traffic-groupstate",
                    "name": "traffic-group-1",
                    "partition": "Common",
                    "fullPath": "/Common/traffic-group-1",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/cm/traffic-group/~Common~traffic-group-1?ver=14.1.2.1",
                    "autoFailbackEnabled": "false",
                    "autoFailbackTime": 60,
                    "failoverMethod": "ha-order",
                    "haLoadFactor": 1,
                    "isFloating": "true",
                    "mac": "none",
                    "monitor": {},
                    "unitId": 1,
                },
                {
                    "kind": "tm:cm:traffic-group:traffic-groupstate",
                    "name": "traffic-group-local-only",
                    "partition": "Common",
                    "fullPath": "/Common/traffic-group-local-only",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/cm/traffic-group/~Common~traffic-group-local-only?ver=14.1.2.1",
                    "autoFailbackEnabled": "false",
                    "autoFailbackTime": 60,
                    "failoverMethod": "ha-order",
                    "haLoadFactor": 1,
                    "isFloating": "false",
                    "mac": "none",
                    "monitor": {},
                    "unitId": 0,
                },
            ],
        }


class test_get_cm_traffic_group(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "autoFailbackEnabled": "false",
                "autoFailbackTime": 60,
                "failoverMethod": "ha-order",
                "fullPath": "/Common/traffic-group-1",
                "generation": 1,
                "haLoadFactor": 1,
                "isFloating": "true",
                "kind": "tm:cm:traffic-group:traffic-groupstate",
                "mac": "none",
                "monitor": {},
                "name": "traffic-group-1",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/cm/traffic-group/~Common~traffic-group-1?ver=14.1.2.1",
                "unitId": 1,
            },
            {
                "autoFailbackEnabled": "false",
                "autoFailbackTime": 60,
                "failoverMethod": "ha-order",
                "fullPath": "/Common/traffic-group-local-only",
                "generation": 1,
                "haLoadFactor": 1,
                "isFloating": "false",
                "kind": "tm:cm:traffic-group:traffic-groupstate",
                "mac": "none",
                "monitor": {},
                "name": "traffic-group-local-only",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/cm/traffic-group/~Common~traffic-group-local-only?ver=14.1.2.1",
                "unitId": 0,
            },
        ],
        "kind": "tm:cm:traffic-group:traffic-groupcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/cm/traffic-group?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = CmTrafficgroup(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = CmTrafficgroup(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
