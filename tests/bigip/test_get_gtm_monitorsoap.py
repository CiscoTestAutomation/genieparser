# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_gtm_monitorsoap
from genie.libs.parser.bigip.get_gtm_monitorsoap import GtmMonitorSoap

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/gtm/monitor/soap'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:gtm:monitor:soap:soapcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/gtm/monitor/soap?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:gtm:monitor:soap:soapstate",
                    "name": "soap",
                    "partition": "Common",
                    "fullPath": "/Common/soap",
                    "generation": 0,
                    "selfLink": "https://localhost/mgmt/tm/gtm/monitor/soap/~Common~soap?ver=14.1.2.1",
                    "debug": "no",
                    "destination": "*:*",
                    "expectFault": "no",
                    "ignoreDownResponse": "disabled",
                    "interval": 30,
                    "probeTimeout": 5,
                    "protocol": "http",
                    "timeout": 120,
                }
            ],
        }


class test_get_gtm_monitorsoap(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "debug": "no",
                "destination": "*:*",
                "expectFault": "no",
                "fullPath": "/Common/soap",
                "generation": 0,
                "ignoreDownResponse": "disabled",
                "interval": 30,
                "kind": "tm:gtm:monitor:soap:soapstate",
                "name": "soap",
                "partition": "Common",
                "probeTimeout": 5,
                "protocol": "http",
                "selfLink": "https://localhost/mgmt/tm/gtm/monitor/soap/~Common~soap?ver=14.1.2.1",
                "timeout": 120,
            }
        ],
        "kind": "tm:gtm:monitor:soap:soapcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/gtm/monitor/soap?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = GtmMonitorSoap(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = GtmMonitorSoap(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
