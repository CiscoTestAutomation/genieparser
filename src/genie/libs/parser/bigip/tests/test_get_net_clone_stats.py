# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_net_clone_stats
from genie.libs.parser.bigip.get_net_clone_stats import NetClonestats

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/net/clone-stats'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:net:clone-stats:clone-statsstats",
            "selfLink": "https://localhost/mgmt/tm/net/clone-stats?ver=14.1.2.1",
            "entries": {
                "https://localhost/mgmt/tm/net/clone-stats/0": {
                    "nestedStats": {
                        "entries": {
                            "freeErr": {"value": 0},
                            "freeOk": {"value": 0},
                            "nhopErr": {"value": 0},
                            "nhopOk": {"value": 0},
                            "pktErr": {"value": 0},
                            "pktOk": {"value": 0},
                            "pmbrErr": {"value": 0},
                            "pmbrOk": {"value": 0},
                            "rslctMacErr": {"value": 0},
                            "rslctMacOk": {"value": 0},
                        }
                    }
                }
            },
        }


class test_get_net_clone_stats(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "entries": {
            "https://localhost/mgmt/tm/net/clone-stats/0": {
                "nestedStats": {
                    "entries": {
                        "freeErr": {"value": 0},
                        "freeOk": {"value": 0},
                        "nhopErr": {"value": 0},
                        "nhopOk": {"value": 0},
                        "pktErr": {"value": 0},
                        "pktOk": {"value": 0},
                        "pmbrErr": {"value": 0},
                        "pmbrOk": {"value": 0},
                        "rslctMacErr": {"value": 0},
                        "rslctMacOk": {"value": 0},
                    }
                }
            }
        },
        "kind": "tm:net:clone-stats:clone-statsstats",
        "selfLink": "https://localhost/mgmt/tm/net/clone-stats?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = NetClonestats(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = NetClonestats(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
