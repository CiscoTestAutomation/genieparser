# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_gtm_monitorhttps
from genie.libs.parser.bigip.get_gtm_monitorhttps import GtmMonitorHttps

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/gtm/monitor/https'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:gtm:monitor:https:httpscollectionstate",
            "selfLink": "https://localhost/mgmt/tm/gtm/monitor/https?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:gtm:monitor:https:httpsstate",
                    "name": "https",
                    "partition": "Common",
                    "fullPath": "/Common/https",
                    "generation": 0,
                    "selfLink": "https://localhost/mgmt/tm/gtm/monitor/https/~Common~https?ver=14.1.2.1",
                    "cipherlist": "DEFAULT:!EXPORT",
                    "compatibility": "enabled",
                    "destination": "*:*",
                    "ignoreDownResponse": "disabled",
                    "interval": 30,
                    "probeTimeout": 5,
                    "reverse": "disabled",
                    "send": "GET /",
                    "timeout": 120,
                    "transparent": "disabled",
                },
                {
                    "kind": "tm:gtm:monitor:https:httpsstate",
                    "name": "https_head_f5",
                    "partition": "Common",
                    "fullPath": "/Common/https_head_f5",
                    "generation": 0,
                    "selfLink": "https://localhost/mgmt/tm/gtm/monitor/https/~Common~https_head_f5?ver=14.1.2.1",
                    "cipherlist": "DEFAULT:!EXPORT",
                    "compatibility": "enabled",
                    "defaultsFrom": "/Common/https",
                    "destination": "*:*",
                    "ignoreDownResponse": "disabled",
                    "interval": 30,
                    "probeTimeout": 5,
                    "recv": "Server\\:",
                    "reverse": "disabled",
                    "send": "HEAD / HTTP/1.0\\r\\n\\r\\n",
                    "timeout": 120,
                    "transparent": "disabled",
                },
            ],
        }


class test_get_gtm_monitorhttps(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "cipherlist": "DEFAULT:!EXPORT",
                "compatibility": "enabled",
                "destination": "*:*",
                "fullPath": "/Common/https",
                "generation": 0,
                "ignoreDownResponse": "disabled",
                "interval": 30,
                "kind": "tm:gtm:monitor:https:httpsstate",
                "name": "https",
                "partition": "Common",
                "probeTimeout": 5,
                "reverse": "disabled",
                "selfLink": "https://localhost/mgmt/tm/gtm/monitor/https/~Common~https?ver=14.1.2.1",
                "send": "GET /",
                "timeout": 120,
                "transparent": "disabled",
            },
            {
                "cipherlist": "DEFAULT:!EXPORT",
                "compatibility": "enabled",
                "defaultsFrom": "/Common/https",
                "destination": "*:*",
                "fullPath": "/Common/https_head_f5",
                "generation": 0,
                "ignoreDownResponse": "disabled",
                "interval": 30,
                "kind": "tm:gtm:monitor:https:httpsstate",
                "name": "https_head_f5",
                "partition": "Common",
                "probeTimeout": 5,
                "recv": "Server\\:",
                "reverse": "disabled",
                "selfLink": "https://localhost/mgmt/tm/gtm/monitor/https/~Common~https_head_f5?ver=14.1.2.1",
                "send": "HEAD / HTTP/1.0\\r\\n\\r\\n",
                "timeout": 120,
                "transparent": "disabled",
            },
        ],
        "kind": "tm:gtm:monitor:https:httpscollectionstate",
        "selfLink": "https://localhost/mgmt/tm/gtm/monitor/https?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = GtmMonitorHttps(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = GtmMonitorHttps(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
