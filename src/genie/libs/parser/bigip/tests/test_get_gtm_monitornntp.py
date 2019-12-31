# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_gtm_monitornntp
from genie.libs.parser.bigip.get_gtm_monitornntp import GtmMonitorNntp

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/gtm/monitor/nntp'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:gtm:monitor:nntp:nntpcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/gtm/monitor/nntp?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:gtm:monitor:nntp:nntpstate",
                    "name": "nntp",
                    "partition": "Common",
                    "fullPath": "/Common/nntp",
                    "generation": 0,
                    "selfLink": "https://localhost/mgmt/tm/gtm/monitor/nntp/~Common~nntp?ver=14.1.2.1",
                    "debug": "no",
                    "destination": "*:*",
                    "ignoreDownResponse": "disabled",
                    "interval": 30,
                    "probeTimeout": 5,
                    "timeout": 120,
                }
            ],
        }


class test_get_gtm_monitornntp(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "debug": "no",
                "destination": "*:*",
                "fullPath": "/Common/nntp",
                "generation": 0,
                "ignoreDownResponse": "disabled",
                "interval": 30,
                "kind": "tm:gtm:monitor:nntp:nntpstate",
                "name": "nntp",
                "partition": "Common",
                "probeTimeout": 5,
                "selfLink": "https://localhost/mgmt/tm/gtm/monitor/nntp/~Common~nntp?ver=14.1.2.1",
                "timeout": 120,
            }
        ],
        "kind": "tm:gtm:monitor:nntp:nntpcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/gtm/monitor/nntp?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = GtmMonitorNntp(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = GtmMonitorNntp(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
