# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_gtm_monitorwmi
from genie.libs.parser.bigip.get_gtm_monitorwmi import GtmMonitorWmi

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/gtm/monitor/wmi'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:gtm:monitor:wmi:wmicollectionstate",
            "selfLink": "https://localhost/mgmt/tm/gtm/monitor/wmi?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:gtm:monitor:wmi:wmistate",
                    "name": "wmi",
                    "partition": "Common",
                    "fullPath": "/Common/wmi",
                    "generation": 0,
                    "selfLink": "https://localhost/mgmt/tm/gtm/monitor/wmi/~Common~wmi?ver=14.1.2.1",
                    "agent": "Mozilla/4.0 (compatible: MSIE 5.0; Windows NT)",
                    "tmCommand": "GetCPUInfo, GetDiskInfo, GetOSInfo",
                    "destination": "*:80",
                    "ignoreDownResponse": "disabled",
                    "interval": 30,
                    "method": "POST",
                    "metrics": "LoadPercentage, DiskUsage, PhysicalMemoryUsage:1.5, VirtualMemoryUsage:2.0",
                    "post": "RespFormat=HTML",
                    "probeTimeout": 5,
                    "timeout": 120,
                    "url": "/scripts/F5Isapi.dll",
                }
            ],
        }


class test_get_gtm_monitorwmi(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "agent": "Mozilla/4.0 (compatible: MSIE 5.0; Windows NT)",
                "destination": "*:80",
                "fullPath": "/Common/wmi",
                "generation": 0,
                "ignoreDownResponse": "disabled",
                "interval": 30,
                "kind": "tm:gtm:monitor:wmi:wmistate",
                "method": "POST",
                "metrics": "LoadPercentage, DiskUsage, PhysicalMemoryUsage:1.5, "
                "VirtualMemoryUsage:2.0",
                "name": "wmi",
                "partition": "Common",
                "post": "RespFormat=HTML",
                "probeTimeout": 5,
                "selfLink": "https://localhost/mgmt/tm/gtm/monitor/wmi/~Common~wmi?ver=14.1.2.1",
                "timeout": 120,
                "tmCommand": "GetCPUInfo, GetDiskInfo, GetOSInfo",
                "url": "/scripts/F5Isapi.dll",
            }
        ],
        "kind": "tm:gtm:monitor:wmi:wmicollectionstate",
        "selfLink": "https://localhost/mgmt/tm/gtm/monitor/wmi?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = GtmMonitorWmi(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = GtmMonitorWmi(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
