# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_gtm_monitorsnmp_link
from genie.libs.parser.bigip.get_gtm_monitorsnmp_link import GtmMonitorSnmplink

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/gtm/monitor/snmp-link'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:gtm:monitor:snmp-link:snmp-linkcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/gtm/monitor/snmp-link?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:gtm:monitor:snmp-link:snmp-linkstate",
                    "name": "snmp_link",
                    "partition": "Common",
                    "fullPath": "/Common/snmp_link",
                    "generation": 0,
                    "selfLink": "https://localhost/mgmt/tm/gtm/monitor/snmp-link/~Common~snmp_link?ver=14.1.2.1",
                    "community": "public",
                    "destination": "*",
                    "ignoreDownResponse": "disabled",
                    "interval": 10,
                    "port": 161,
                    "probeAttempts": 3,
                    "probeInterval": 1,
                    "probeTimeout": 5,
                    "timeout": 30,
                    "version": "v1",
                }
            ],
        }


class test_get_gtm_monitorsnmp_link(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "community": "public",
                "destination": "*",
                "fullPath": "/Common/snmp_link",
                "generation": 0,
                "ignoreDownResponse": "disabled",
                "interval": 10,
                "kind": "tm:gtm:monitor:snmp-link:snmp-linkstate",
                "name": "snmp_link",
                "partition": "Common",
                "port": 161,
                "probeAttempts": 3,
                "probeInterval": 1,
                "probeTimeout": 5,
                "selfLink": "https://localhost/mgmt/tm/gtm/monitor/snmp-link/~Common~snmp_link?ver=14.1.2.1",
                "timeout": 30,
                "version": "v1",
            }
        ],
        "kind": "tm:gtm:monitor:snmp-link:snmp-linkcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/gtm/monitor/snmp-link?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = GtmMonitorSnmplink(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = GtmMonitorSnmplink(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
