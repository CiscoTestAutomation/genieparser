# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_net_ike_evt_stat
from genie.libs.parser.bigip.get_net_ike_evt_stat import NetIkeevtstat

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/net/ike-evt-stat'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:net:ike-evt-stat:ike-evt-statstats",
            "selfLink": "https://localhost/mgmt/tm/net/ike-evt-stat?ver=14.1.2.1",
            "entries": {
                "https://localhost/mgmt/tm/net/ike-evt-stat/0": {
                    "nestedStats": {
                        "entries": {
                            "activeTunnels": {"value": 0},
                            "authFailures": {"value": 0},
                            "authSuccess": {"value": 0},
                            "childRekeyLInit": {"value": 0},
                            "childRekeyRInit": {"value": 0},
                            "decryptFailures": {"value": 0},
                            "hashFailures": {"value": 0},
                            "ikeRekeyLInit": {"value": 0},
                            "ikeRekeyRInit": {"value": 0},
                            "inSaNegotiation": {"value": 0},
                            "invalidSpi": {"value": 0},
                            "lInitFailSa": {"value": 0},
                            "lInitSa": {"value": 0},
                            "negotiatedTunnels": {"value": 0},
                            "outSaNegotiation": {"value": 0},
                            "proposalMismatch": {"value": 0},
                            "rInitFailSa": {"value": 0},
                            "rInitSa": {"value": 0},
                            "v2Negotiations": {"value": 0},
                            "v2NegotiationsFail": {"value": 0},
                        }
                    }
                }
            },
        }


class test_get_net_ike_evt_stat(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "entries": {
            "https://localhost/mgmt/tm/net/ike-evt-stat/0": {
                "nestedStats": {
                    "entries": {
                        "activeTunnels": {"value": 0},
                        "authFailures": {"value": 0},
                        "authSuccess": {"value": 0},
                        "childRekeyLInit": {"value": 0},
                        "childRekeyRInit": {"value": 0},
                        "decryptFailures": {"value": 0},
                        "hashFailures": {"value": 0},
                        "ikeRekeyLInit": {"value": 0},
                        "ikeRekeyRInit": {"value": 0},
                        "inSaNegotiation": {"value": 0},
                        "invalidSpi": {"value": 0},
                        "lInitFailSa": {"value": 0},
                        "lInitSa": {"value": 0},
                        "negotiatedTunnels": {"value": 0},
                        "outSaNegotiation": {"value": 0},
                        "proposalMismatch": {"value": 0},
                        "rInitFailSa": {"value": 0},
                        "rInitSa": {"value": 0},
                        "v2Negotiations": {"value": 0},
                        "v2NegotiationsFail": {"value": 0},
                    }
                }
            }
        },
        "kind": "tm:net:ike-evt-stat:ike-evt-statstats",
        "selfLink": "https://localhost/mgmt/tm/net/ike-evt-stat?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = NetIkeevtstat(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = NetIkeevtstat(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
