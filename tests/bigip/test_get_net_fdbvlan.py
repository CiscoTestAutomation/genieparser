# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_net_fdbvlan
from genie.libs.parser.bigip.get_net_fdbvlan import NetFdbVlan

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/net/fdb/vlan'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:net:fdb:vlan:vlancollectionstate",
            "selfLink": "https://localhost/mgmt/tm/net/fdb/vlan?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:net:fdb:vlan:vlanstate",
                    "name": "External",
                    "partition": "Common",
                    "fullPath": "/Common/External",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/net/fdb/vlan/~Common~External?ver=14.1.2.1",
                },
                {
                    "kind": "tm:net:fdb:vlan:vlanstate",
                    "name": "HA",
                    "partition": "Common",
                    "fullPath": "/Common/HA",
                    "generation": 994,
                    "selfLink": "https://localhost/mgmt/tm/net/fdb/vlan/~Common~HA?ver=14.1.2.1",
                },
                {
                    "kind": "tm:net:fdb:vlan:vlanstate",
                    "name": "Internal",
                    "partition": "Common",
                    "fullPath": "/Common/Internal",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/net/fdb/vlan/~Common~Internal?ver=14.1.2.1",
                },
                {
                    "kind": "tm:net:fdb:vlan:vlanstate",
                    "name": "Services",
                    "partition": "Common",
                    "fullPath": "/Common/Services",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/net/fdb/vlan/~Common~Services?ver=14.1.2.1",
                },
            ],
        }


class test_get_net_fdbvlan(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "fullPath": "/Common/External",
                "generation": 1,
                "kind": "tm:net:fdb:vlan:vlanstate",
                "name": "External",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/net/fdb/vlan/~Common~External?ver=14.1.2.1",
            },
            {
                "fullPath": "/Common/HA",
                "generation": 994,
                "kind": "tm:net:fdb:vlan:vlanstate",
                "name": "HA",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/net/fdb/vlan/~Common~HA?ver=14.1.2.1",
            },
            {
                "fullPath": "/Common/Internal",
                "generation": 1,
                "kind": "tm:net:fdb:vlan:vlanstate",
                "name": "Internal",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/net/fdb/vlan/~Common~Internal?ver=14.1.2.1",
            },
            {
                "fullPath": "/Common/Services",
                "generation": 1,
                "kind": "tm:net:fdb:vlan:vlanstate",
                "name": "Services",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/net/fdb/vlan/~Common~Services?ver=14.1.2.1",
            },
        ],
        "kind": "tm:net:fdb:vlan:vlancollectionstate",
        "selfLink": "https://localhost/mgmt/tm/net/fdb/vlan?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = NetFdbVlan(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = NetFdbVlan(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
