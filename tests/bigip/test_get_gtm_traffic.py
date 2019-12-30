# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_gtm_traffic
from genie.libs.parser.bigip.get_gtm_traffic import GtmTraffic

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/gtm/traffic'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:gtm:traffic:trafficstats",
            "selfLink": "https://localhost/mgmt/tm/gtm/traffic?ver=14.1.2.1",
            "entries": {
                "https://localhost/mgmt/tm/gtm/traffic/0": {
                    "nestedStats": {
                        "entries": {
                            "aRequests": {"value": 0},
                            "aaaaRequests": {"value": 0},
                            "cnameRequests": {"value": 0},
                            "ldnses": {"value": 0},
                            "mxRequests": {"value": 0},
                            "naptrRequests": {"value": 0},
                            "paths": {"value": 0},
                            "srvRequests": {"value": 0},
                        }
                    }
                }
            },
        }


class test_get_gtm_traffic(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "entries": {
            "https://localhost/mgmt/tm/gtm/traffic/0": {
                "nestedStats": {
                    "entries": {
                        "aRequests": {"value": 0},
                        "aaaaRequests": {"value": 0},
                        "cnameRequests": {"value": 0},
                        "ldnses": {"value": 0},
                        "mxRequests": {"value": 0},
                        "naptrRequests": {"value": 0},
                        "paths": {"value": 0},
                        "srvRequests": {"value": 0},
                    }
                }
            }
        },
        "kind": "tm:gtm:traffic:trafficstats",
        "selfLink": "https://localhost/mgmt/tm/gtm/traffic?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = GtmTraffic(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = GtmTraffic(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
