# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_net_ipsectraffic_selector
from genie.libs.parser.bigip.get_net_ipsectraffic_selector import (
    NetIpsecTrafficselector,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/net/ipsec/traffic-selector'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:net:ipsec:traffic-selector:traffic-selectorcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/net/ipsec/traffic-selector?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:net:ipsec:traffic-selector:traffic-selectorstate",
                    "name": "default-traffic-selector-interface",
                    "partition": "Common",
                    "fullPath": "/Common/default-traffic-selector-interface",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/net/ipsec/traffic-selector/~Common~default-traffic-selector-interface?ver=14.1.2.1",
                    "action": "protect",
                    "destinationAddress": "::/0",
                    "destinationPort": 0,
                    "direction": "both",
                    "ipProtocol": 255,
                    "ipsecPolicy": "/Common/default-ipsec-policy-interface",
                    "ipsecPolicyReference": {
                        "link": "https://localhost/mgmt/tm/net/ipsec/ipsec-policy/~Common~default-ipsec-policy-interface?ver=14.1.2.1"
                    },
                    "order": 0,
                    "sourceAddress": "::/0",
                    "sourcePort": 0,
                }
            ],
        }


class test_get_net_ipsectraffic_selector(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "action": "protect",
                "destinationAddress": "::/0",
                "destinationPort": 0,
                "direction": "both",
                "fullPath": "/Common/default-traffic-selector-interface",
                "generation": 1,
                "ipProtocol": 255,
                "ipsecPolicy": "/Common/default-ipsec-policy-interface",
                "ipsecPolicyReference": {
                    "link": "https://localhost/mgmt/tm/net/ipsec/ipsec-policy/~Common~default-ipsec-policy-interface?ver=14.1.2.1"
                },
                "kind": "tm:net:ipsec:traffic-selector:traffic-selectorstate",
                "name": "default-traffic-selector-interface",
                "order": 0,
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/net/ipsec/traffic-selector/~Common~default-traffic-selector-interface?ver=14.1.2.1",
                "sourceAddress": "::/0",
                "sourcePort": 0,
            }
        ],
        "kind": "tm:net:ipsec:traffic-selector:traffic-selectorcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/net/ipsec/traffic-selector?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = NetIpsecTrafficselector(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = NetIpsecTrafficselector(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
