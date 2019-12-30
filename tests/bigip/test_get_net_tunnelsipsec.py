# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_net_tunnelsipsec
from genie.libs.parser.bigip.get_net_tunnelsipsec import NetTunnelsIpsec

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/net/tunnels/ipsec'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:net:tunnels:ipsec:ipseccollectionstate",
            "selfLink": "https://localhost/mgmt/tm/net/tunnels/ipsec?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:net:tunnels:ipsec:ipsecstate",
                    "name": "ipsec",
                    "partition": "Common",
                    "fullPath": "/Common/ipsec",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/net/tunnels/ipsec/~Common~ipsec?ver=14.1.2.1",
                    "trafficSelector": "/Common/default-traffic-selector-interface",
                    "trafficSelectorReference": {
                        "link": "https://localhost/mgmt/tm/net/ipsec/traffic-selector/~Common~default-traffic-selector-interface?ver=14.1.2.1"
                    },
                }
            ],
        }


class test_get_net_tunnelsipsec(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "fullPath": "/Common/ipsec",
                "generation": 1,
                "kind": "tm:net:tunnels:ipsec:ipsecstate",
                "name": "ipsec",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/net/tunnels/ipsec/~Common~ipsec?ver=14.1.2.1",
                "trafficSelector": "/Common/default-traffic-selector-interface",
                "trafficSelectorReference": {
                    "link": "https://localhost/mgmt/tm/net/ipsec/traffic-selector/~Common~default-traffic-selector-interface?ver=14.1.2.1"
                },
            }
        ],
        "kind": "tm:net:tunnels:ipsec:ipseccollectionstate",
        "selfLink": "https://localhost/mgmt/tm/net/tunnels/ipsec?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = NetTunnelsIpsec(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = NetTunnelsIpsec(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
