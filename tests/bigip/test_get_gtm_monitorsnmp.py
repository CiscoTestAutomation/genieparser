# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_gtm_monitorsnmp
from genie.libs.parser.bigip.get_gtm_monitorsnmp import GtmMonitorSnmp

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/gtm/monitor/snmp'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:gtm:monitor:snmp:snmpcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/gtm/monitor/snmp?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:gtm:monitor:snmp:snmpstate",
                    "name": "snmp_gtm",
                    "partition": "Common",
                    "fullPath": "/Common/snmp_gtm",
                    "generation": 0,
                    "selfLink": "https://localhost/mgmt/tm/gtm/monitor/snmp/~Common~snmp_gtm?ver=14.1.2.1",
                    "community": "public",
                    "destination": "*:*",
                    "ignoreDownResponse": "disabled",
                    "interval": 90,
                    "port": 161,
                    "probeAttempts": 3,
                    "probeInterval": 1,
                    "probeTimeout": 5,
                    "timeout": 180,
                    "version": "v1",
                }
            ],
        }


class test_get_gtm_monitorsnmp(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "community": "public",
                "destination": "*:*",
                "fullPath": "/Common/snmp_gtm",
                "generation": 0,
                "ignoreDownResponse": "disabled",
                "interval": 90,
                "kind": "tm:gtm:monitor:snmp:snmpstate",
                "name": "snmp_gtm",
                "partition": "Common",
                "port": 161,
                "probeAttempts": 3,
                "probeInterval": 1,
                "probeTimeout": 5,
                "selfLink": "https://localhost/mgmt/tm/gtm/monitor/snmp/~Common~snmp_gtm?ver=14.1.2.1",
                "timeout": 180,
                "version": "v1",
            }
        ],
        "kind": "tm:gtm:monitor:snmp:snmpcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/gtm/monitor/snmp?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = GtmMonitorSnmp(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = GtmMonitorSnmp(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
