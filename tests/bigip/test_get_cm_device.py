# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_cm_device
from genie.libs.parser.bigip.get_cm_device import CmDevice

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/cm/device'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:cm:device:devicecollectionstate",
            "selfLink": "https://localhost/mgmt/tm/cm/device?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:cm:device:devicestate",
                    "name": "bigip01.lab.local",
                    "partition": "Common",
                    "fullPath": "/Common/bigip01.lab.local",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/cm/device/~Common~bigip01.lab.local?ver=14.1.2.1",
                    "activeModules": [
                        "BIG-IP, VE, LAB|GSMORBH-FRIQHYL|Rate Shaping|External Interface and Network HSM, VE|BIG-IP VE, Multicast Routing|Routing Bundle, VE|ASM, VE|SSL, VE|DNS VE Lab  (10K QPS)|Max Compression, VE|Advanced Protocols, VE|SSL Orchestrator, VE|Advanced Web Application Firewall, VE Lab|APM, Lab, VE|AFM, VE (LAB ONLY - NO ROUTING)|DNSSEC|VE, Carrier Grade NAT (AFM ONLY)|PSM, VE"
                    ],
                    "alternateIp": "none",
                    "baseMac": "00:0c:29:35:0d:bd",
                    "build": "0.0.4",
                    "cert": "/Common/dtdi.crt",
                    "certReference": {
                        "link": "https://localhost/mgmt/tm/cm/cert/~Common~dtdi.crt?ver=14.1.2.1"
                    },
                    "chassisId": "564d4d7e-c668-e9dc-2bf3c9350dbd",
                    "chassisType": "individual",
                    "configsyncIp": "none",
                    "edition": "Point Release 1",
                    "failoverState": "active",
                    "haCapacity": 0,
                    "hostname": "bigip01.lab.local",
                    "key": "/Common/dtdi.key",
                    "keyReference": {
                        "link": "https://localhost/mgmt/tm/cm/key/~Common~dtdi.key?ver=14.1.2.1"
                    },
                    "managementIp": "192.168.189.233",
                    "marketingName": "BIG-IP Virtual Edition",
                    "mgmtUnicastMode": "both",
                    "mirrorIp": "any6",
                    "mirrorSecondaryIp": "any6",
                    "multicastIp": "any6",
                    "multicastPort": 0,
                    "optionalModules": [
                        "Anti-Bot Mobile, VE 25 Mbps",
                        "App Mode (TMSH Only, No Root/Bash)",
                        "FIPS 140-2 Level 1, BIG-IP VE-200M",
                        "IP Intelligence, 1Yr, VE-200M/VE-25M",
                        "IP Intelligence, 3Yr, VE-200M/VE-25M",
                        "ONAP",
                        "Threat Campaigns, 1Yr, VE-200M/VE-25M",
                        "URL Filtering, VE-25M-1G, 500 Sessions, 1Yr",
                        "URL Filtering, VE-25M-1G, 500 Sessions, 3Yr",
                    ],
                    "platformId": "Z100",
                    "product": "BIG-IP",
                    "selfDevice": "true",
                    "timeZone": "America/Los_Angeles",
                    "version": "14.1.2.1",
                }
            ],
        }


class test_get_cm_device(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "activeModules": [
                    "BIG-IP, VE, LAB|GSMORBH-FRIQHYL|Rate "
                    "Shaping|External Interface and Network HSM, "
                    "VE|BIG-IP VE, Multicast Routing|Routing Bundle, "
                    "VE|ASM, VE|SSL, VE|DNS VE Lab  (10K QPS)|Max "
                    "Compression, VE|Advanced Protocols, VE|SSL "
                    "Orchestrator, VE|Advanced Web Application "
                    "Firewall, VE Lab|APM, Lab, VE|AFM, VE (LAB ONLY "
                    "- NO ROUTING)|DNSSEC|VE, Carrier Grade NAT (AFM "
                    "ONLY)|PSM, VE"
                ],
                "alternateIp": "none",
                "baseMac": "00:0c:29:35:0d:bd",
                "build": "0.0.4",
                "cert": "/Common/dtdi.crt",
                "certReference": {
                    "link": "https://localhost/mgmt/tm/cm/cert/~Common~dtdi.crt?ver=14.1.2.1"
                },
                "chassisId": "564d4d7e-c668-e9dc-2bf3c9350dbd",
                "chassisType": "individual",
                "configsyncIp": "none",
                "edition": "Point Release 1",
                "failoverState": "active",
                "fullPath": "/Common/bigip01.lab.local",
                "generation": 1,
                "haCapacity": 0,
                "hostname": "bigip01.lab.local",
                "key": "/Common/dtdi.key",
                "keyReference": {
                    "link": "https://localhost/mgmt/tm/cm/key/~Common~dtdi.key?ver=14.1.2.1"
                },
                "kind": "tm:cm:device:devicestate",
                "managementIp": "192.168.189.233",
                "marketingName": "BIG-IP Virtual Edition",
                "mgmtUnicastMode": "both",
                "mirrorIp": "any6",
                "mirrorSecondaryIp": "any6",
                "multicastIp": "any6",
                "multicastPort": 0,
                "name": "bigip01.lab.local",
                "optionalModules": [
                    "Anti-Bot Mobile, VE 25 Mbps",
                    "App Mode (TMSH Only, No Root/Bash)",
                    "FIPS 140-2 Level 1, BIG-IP VE-200M",
                    "IP Intelligence, 1Yr, VE-200M/VE-25M",
                    "IP Intelligence, 3Yr, VE-200M/VE-25M",
                    "ONAP",
                    "Threat Campaigns, 1Yr, VE-200M/VE-25M",
                    "URL Filtering, VE-25M-1G, 500 Sessions, 1Yr",
                    "URL Filtering, VE-25M-1G, 500 Sessions, 3Yr",
                ],
                "partition": "Common",
                "platformId": "Z100",
                "product": "BIG-IP",
                "selfDevice": "true",
                "selfLink": "https://localhost/mgmt/tm/cm/device/~Common~bigip01.lab.local?ver=14.1.2.1",
                "timeZone": "America/Los_Angeles",
                "version": "14.1.2.1",
            }
        ],
        "kind": "tm:cm:device:devicecollectionstate",
        "selfLink": "https://localhost/mgmt/tm/cm/device?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = CmDevice(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = CmDevice(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
