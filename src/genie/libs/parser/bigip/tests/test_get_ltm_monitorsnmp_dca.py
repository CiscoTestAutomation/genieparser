# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_monitorsnmp_dca
from genie.libs.parser.bigip.get_ltm_monitorsnmp_dca import LtmMonitorSnmpdca

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/monitor/snmp-dca'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:monitor:snmp-dca:snmp-dcacollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/monitor/snmp-dca?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:monitor:snmp-dca:snmp-dcastate",
                    "name": "snmp_dca",
                    "partition": "Common",
                    "fullPath": "/Common/snmp_dca",
                    "generation": 0,
                    "selfLink": "https://localhost/mgmt/tm/ltm/monitor/snmp-dca/~Common~snmp_dca?ver=14.1.2.1",
                    "agentType": "UCD",
                    "community": "public",
                    "cpuCoefficient": "1.5",
                    "cpuThreshold": "80",
                    "diskCoefficient": "2.0",
                    "diskThreshold": "90",
                    "interval": 10,
                    "memoryCoefficient": "1.0",
                    "memoryThreshold": "70",
                    "timeUntilUp": 0,
                    "timeout": 30,
                    "version": "v1",
                }
            ],
        }


class test_get_ltm_monitorsnmp_dca(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "agentType": "UCD",
                "community": "public",
                "cpuCoefficient": "1.5",
                "cpuThreshold": "80",
                "diskCoefficient": "2.0",
                "diskThreshold": "90",
                "fullPath": "/Common/snmp_dca",
                "generation": 0,
                "interval": 10,
                "kind": "tm:ltm:monitor:snmp-dca:snmp-dcastate",
                "memoryCoefficient": "1.0",
                "memoryThreshold": "70",
                "name": "snmp_dca",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/monitor/snmp-dca/~Common~snmp_dca?ver=14.1.2.1",
                "timeUntilUp": 0,
                "timeout": 30,
                "version": "v1",
            }
        ],
        "kind": "tm:ltm:monitor:snmp-dca:snmp-dcacollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/monitor/snmp-dca?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmMonitorSnmpdca(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmMonitorSnmpdca(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
