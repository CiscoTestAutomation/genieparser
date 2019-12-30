# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_monitorsnmp_dca_base
from genie.libs.parser.bigip.get_ltm_monitorsnmp_dca_base import (
    LtmMonitorSnmpdcabase,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/monitor/snmp-dca-base'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:monitor:snmp-dca-base:snmp-dca-basecollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/monitor/snmp-dca-base?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:monitor:snmp-dca-base:snmp-dca-basestate",
                    "name": "snmp_dca_base",
                    "partition": "Common",
                    "fullPath": "/Common/snmp_dca_base",
                    "generation": 0,
                    "selfLink": "https://localhost/mgmt/tm/ltm/monitor/snmp-dca-base/~Common~snmp_dca_base?ver=14.1.2.1",
                    "community": "public",
                    "interval": 10,
                    "timeUntilUp": 0,
                    "timeout": 30,
                    "version": "v1",
                }
            ],
        }


class test_get_ltm_monitorsnmp_dca_base(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "community": "public",
                "fullPath": "/Common/snmp_dca_base",
                "generation": 0,
                "interval": 10,
                "kind": "tm:ltm:monitor:snmp-dca-base:snmp-dca-basestate",
                "name": "snmp_dca_base",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/monitor/snmp-dca-base/~Common~snmp_dca_base?ver=14.1.2.1",
                "timeUntilUp": 0,
                "timeout": 30,
                "version": "v1",
            }
        ],
        "kind": "tm:ltm:monitor:snmp-dca-base:snmp-dca-basecollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/monitor/snmp-dca-base?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmMonitorSnmpdcabase(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmMonitorSnmpdcabase(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
