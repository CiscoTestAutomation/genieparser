# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_gtm_monitorbigip_link
from genie.libs.parser.bigip.get_gtm_monitorbigip_link import (
    GtmMonitorBigiplink,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/gtm/monitor/bigip-link'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:gtm:monitor:bigip-link:bigip-linkcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/gtm/monitor/bigip-link?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:gtm:monitor:bigip-link:bigip-linkstate",
                    "name": "bigip_link",
                    "partition": "Common",
                    "fullPath": "/Common/bigip_link",
                    "generation": 0,
                    "selfLink": "https://localhost/mgmt/tm/gtm/monitor/bigip-link/~Common~bigip_link?ver=14.1.2.1",
                    "destination": "*",
                    "ignoreDownResponse": "disabled",
                    "interval": 10,
                    "timeout": 30,
                }
            ],
        }


class test_get_gtm_monitorbigip_link(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "destination": "*",
                "fullPath": "/Common/bigip_link",
                "generation": 0,
                "ignoreDownResponse": "disabled",
                "interval": 10,
                "kind": "tm:gtm:monitor:bigip-link:bigip-linkstate",
                "name": "bigip_link",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/gtm/monitor/bigip-link/~Common~bigip_link?ver=14.1.2.1",
                "timeout": 30,
            }
        ],
        "kind": "tm:gtm:monitor:bigip-link:bigip-linkcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/gtm/monitor/bigip-link?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = GtmMonitorBigiplink(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = GtmMonitorBigiplink(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
