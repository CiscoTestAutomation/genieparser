# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_monitorwmi
from genie.libs.parser.bigip.get_ltm_monitorwmi import LtmMonitorWmi

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/monitor/wmi'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:monitor:wmi:wmicollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/monitor/wmi?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:monitor:wmi:wmistate",
                    "name": "wmi",
                    "partition": "Common",
                    "fullPath": "/Common/wmi",
                    "generation": 0,
                    "selfLink": "https://localhost/mgmt/tm/ltm/monitor/wmi/~Common~wmi?ver=14.1.2.1",
                    "agent": "Mozilla/4.0 (compatible: MSIE 5.0; Windows NT)",
                    "tmCommand": "GetCPUInfo, GetDiskInfo, GetOSInfo",
                    "destination": "*:80",
                    "interval": 5,
                    "method": "POST",
                    "metrics": "LoadPercentage, DiskUsage, PhysicalMemoryUsage:1.5, VirtualMemoryUsage:2.0",
                    "post": "RespFormat=HTML",
                    "timeUntilUp": 0,
                    "timeout": 16,
                    "url": "/scripts/F5Isapi.dll",
                }
            ],
        }


class test_get_ltm_monitorwmi(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "agent": "Mozilla/4.0 (compatible: MSIE 5.0; Windows NT)",
                "destination": "*:80",
                "fullPath": "/Common/wmi",
                "generation": 0,
                "interval": 5,
                "kind": "tm:ltm:monitor:wmi:wmistate",
                "method": "POST",
                "metrics": "LoadPercentage, DiskUsage, PhysicalMemoryUsage:1.5, "
                "VirtualMemoryUsage:2.0",
                "name": "wmi",
                "partition": "Common",
                "post": "RespFormat=HTML",
                "selfLink": "https://localhost/mgmt/tm/ltm/monitor/wmi/~Common~wmi?ver=14.1.2.1",
                "timeUntilUp": 0,
                "timeout": 16,
                "tmCommand": "GetCPUInfo, GetDiskInfo, GetOSInfo",
                "url": "/scripts/F5Isapi.dll",
            }
        ],
        "kind": "tm:ltm:monitor:wmi:wmicollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/monitor/wmi?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmMonitorWmi(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmMonitorWmi(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
