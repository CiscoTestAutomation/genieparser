# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_net_fdbtunnel
from genie.libs.parser.bigip.get_net_fdbtunnel import NetFdbTunnel

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/net/fdb/tunnel'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:net:fdb:tunnel:tunnelcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/net/fdb/tunnel?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:net:fdb:tunnel:tunnelstate",
                    "name": "http-tunnel",
                    "partition": "Common",
                    "fullPath": "/Common/http-tunnel",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/net/fdb/tunnel/~Common~http-tunnel?ver=14.1.2.1",
                    "recordsReference": {
                        "link": "https://localhost/mgmt/tm/net/fdb/tunnel/~Common~http-tunnel/records?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                },
                {
                    "kind": "tm:net:fdb:tunnel:tunnelstate",
                    "name": "socks-tunnel",
                    "partition": "Common",
                    "fullPath": "/Common/socks-tunnel",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/net/fdb/tunnel/~Common~socks-tunnel?ver=14.1.2.1",
                    "recordsReference": {
                        "link": "https://localhost/mgmt/tm/net/fdb/tunnel/~Common~socks-tunnel/records?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                },
            ],
        }


class test_get_net_fdbtunnel(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "fullPath": "/Common/http-tunnel",
                "generation": 1,
                "kind": "tm:net:fdb:tunnel:tunnelstate",
                "name": "http-tunnel",
                "partition": "Common",
                "recordsReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/net/fdb/tunnel/~Common~http-tunnel/records?ver=14.1.2.1",
                },
                "selfLink": "https://localhost/mgmt/tm/net/fdb/tunnel/~Common~http-tunnel?ver=14.1.2.1",
            },
            {
                "fullPath": "/Common/socks-tunnel",
                "generation": 1,
                "kind": "tm:net:fdb:tunnel:tunnelstate",
                "name": "socks-tunnel",
                "partition": "Common",
                "recordsReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/net/fdb/tunnel/~Common~socks-tunnel/records?ver=14.1.2.1",
                },
                "selfLink": "https://localhost/mgmt/tm/net/fdb/tunnel/~Common~socks-tunnel?ver=14.1.2.1",
            },
        ],
        "kind": "tm:net:fdb:tunnel:tunnelcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/net/fdb/tunnel?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = NetFdbTunnel(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = NetFdbTunnel(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
