# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_virtual_address
from genie.libs.parser.bigip.get_ltm_virtual_address import LtmVirtualaddress

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/virtual-address'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:virtual-address:virtual-addresscollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/virtual-address?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:virtual-address:virtual-addressstate",
                    "name": "1.1.1.2",
                    "partition": "Common",
                    "fullPath": "/Common/1.1.1.2",
                    "generation": 1342,
                    "selfLink": "https://localhost/mgmt/tm/ltm/virtual-address/~Common~1.1.1.2?ver=14.1.2.1",
                    "address": "1.1.1.2",
                    "arp": "enabled",
                    "autoDelete": "true",
                    "connectionLimit": 0,
                    "enabled": "yes",
                    "floating": "enabled",
                    "icmpEcho": "enabled",
                    "inheritedTrafficGroup": "false",
                    "mask": "255.255.255.255",
                    "routeAdvertisement": "disabled",
                    "serverScope": "any",
                    "spanning": "disabled",
                    "trafficGroup": "/Common/traffic-group-1",
                    "trafficGroupReference": {
                        "link": "https://localhost/mgmt/tm/cm/traffic-group/~Common~traffic-group-1?ver=14.1.2.1"
                    },
                    "unit": 1,
                },
                {
                    "kind": "tm:ltm:virtual-address:virtual-addressstate",
                    "name": "10.1.1.3",
                    "partition": "Common",
                    "fullPath": "/Common/10.1.1.3",
                    "generation": 1580,
                    "selfLink": "https://localhost/mgmt/tm/ltm/virtual-address/~Common~10.1.1.3?ver=14.1.2.1",
                    "address": "10.1.1.3",
                    "arp": "enabled",
                    "autoDelete": "true",
                    "connectionLimit": 0,
                    "enabled": "yes",
                    "floating": "enabled",
                    "icmpEcho": "enabled",
                    "inheritedTrafficGroup": "false",
                    "mask": "255.255.255.255",
                    "routeAdvertisement": "disabled",
                    "serverScope": "any",
                    "spanning": "disabled",
                    "trafficGroup": "/Common/traffic-group-1",
                    "trafficGroupReference": {
                        "link": "https://localhost/mgmt/tm/cm/traffic-group/~Common~traffic-group-1?ver=14.1.2.1"
                    },
                    "unit": 1,
                },
                {
                    "kind": "tm:ltm:virtual-address:virtual-addressstate",
                    "name": "10.1.1.7",
                    "partition": "Common",
                    "fullPath": "/Common/10.1.1.7",
                    "generation": 1458,
                    "selfLink": "https://localhost/mgmt/tm/ltm/virtual-address/~Common~10.1.1.7?ver=14.1.2.1",
                    "address": "10.1.1.7",
                    "arp": "enabled",
                    "autoDelete": "true",
                    "connectionLimit": 0,
                    "enabled": "yes",
                    "floating": "enabled",
                    "icmpEcho": "enabled",
                    "inheritedTrafficGroup": "false",
                    "mask": "255.255.255.255",
                    "routeAdvertisement": "disabled",
                    "serverScope": "any",
                    "spanning": "disabled",
                    "trafficGroup": "/Common/traffic-group-1",
                    "trafficGroupReference": {
                        "link": "https://localhost/mgmt/tm/cm/traffic-group/~Common~traffic-group-1?ver=14.1.2.1"
                    },
                    "unit": 1,
                },
                {
                    "kind": "tm:ltm:virtual-address:virtual-addressstate",
                    "name": "10.10.34.250",
                    "partition": "Common",
                    "fullPath": "/Common/10.10.34.250",
                    "generation": 1446,
                    "selfLink": "https://localhost/mgmt/tm/ltm/virtual-address/~Common~10.10.34.250?ver=14.1.2.1",
                    "address": "10.10.34.250",
                    "arp": "enabled",
                    "autoDelete": "true",
                    "connectionLimit": 0,
                    "enabled": "yes",
                    "floating": "enabled",
                    "icmpEcho": "enabled",
                    "inheritedTrafficGroup": "false",
                    "mask": "255.255.255.255",
                    "routeAdvertisement": "disabled",
                    "serverScope": "any",
                    "spanning": "disabled",
                    "trafficGroup": "/Common/traffic-group-1",
                    "trafficGroupReference": {
                        "link": "https://localhost/mgmt/tm/cm/traffic-group/~Common~traffic-group-1?ver=14.1.2.1"
                    },
                    "unit": 1,
                },
                {
                    "kind": "tm:ltm:virtual-address:virtual-addressstate",
                    "name": "101.11.11.139",
                    "partition": "Common",
                    "fullPath": "/Common/101.11.11.139",
                    "generation": 1440,
                    "selfLink": "https://localhost/mgmt/tm/ltm/virtual-address/~Common~101.11.11.139?ver=14.1.2.1",
                    "address": "101.11.11.139",
                    "arp": "enabled",
                    "autoDelete": "true",
                    "connectionLimit": 0,
                    "enabled": "yes",
                    "floating": "enabled",
                    "icmpEcho": "enabled",
                    "inheritedTrafficGroup": "false",
                    "mask": "255.255.255.255",
                    "routeAdvertisement": "disabled",
                    "serverScope": "any",
                    "spanning": "disabled",
                    "trafficGroup": "/Common/traffic-group-1",
                    "trafficGroupReference": {
                        "link": "https://localhost/mgmt/tm/cm/traffic-group/~Common~traffic-group-1?ver=14.1.2.1"
                    },
                    "unit": 1,
                },
                {
                    "kind": "tm:ltm:virtual-address:virtual-addressstate",
                    "name": "172.16.100.141",
                    "partition": "Common",
                    "fullPath": "/Common/172.16.100.141",
                    "generation": 1413,
                    "selfLink": "https://localhost/mgmt/tm/ltm/virtual-address/~Common~172.16.100.141?ver=14.1.2.1",
                    "address": "172.16.100.141",
                    "arp": "enabled",
                    "autoDelete": "true",
                    "connectionLimit": 0,
                    "enabled": "yes",
                    "floating": "enabled",
                    "icmpEcho": "enabled",
                    "inheritedTrafficGroup": "false",
                    "mask": "255.255.255.255",
                    "routeAdvertisement": "disabled",
                    "serverScope": "any",
                    "spanning": "disabled",
                    "trafficGroup": "/Common/traffic-group-1",
                    "trafficGroupReference": {
                        "link": "https://localhost/mgmt/tm/cm/traffic-group/~Common~traffic-group-1?ver=14.1.2.1"
                    },
                    "unit": 1,
                },
                {
                    "kind": "tm:ltm:virtual-address:virtual-addressstate",
                    "name": "172.16.220.141",
                    "partition": "Common",
                    "fullPath": "/Common/172.16.220.141",
                    "generation": 1412,
                    "selfLink": "https://localhost/mgmt/tm/ltm/virtual-address/~Common~172.16.220.141?ver=14.1.2.1",
                    "address": "172.16.220.141",
                    "arp": "enabled",
                    "autoDelete": "true",
                    "connectionLimit": 0,
                    "enabled": "yes",
                    "floating": "enabled",
                    "icmpEcho": "enabled",
                    "inheritedTrafficGroup": "false",
                    "mask": "255.255.255.255",
                    "routeAdvertisement": "disabled",
                    "serverScope": "any",
                    "spanning": "disabled",
                    "trafficGroup": "/Common/traffic-group-1",
                    "trafficGroupReference": {
                        "link": "https://localhost/mgmt/tm/cm/traffic-group/~Common~traffic-group-1?ver=14.1.2.1"
                    },
                    "unit": 1,
                },
            ],
        }


class test_get_ltm_virtual_address(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "address": "1.1.1.2",
                "arp": "enabled",
                "autoDelete": "true",
                "connectionLimit": 0,
                "enabled": "yes",
                "floating": "enabled",
                "fullPath": "/Common/1.1.1.2",
                "generation": 1342,
                "icmpEcho": "enabled",
                "inheritedTrafficGroup": "false",
                "kind": "tm:ltm:virtual-address:virtual-addressstate",
                "mask": "255.255.255.255",
                "name": "1.1.1.2",
                "partition": "Common",
                "routeAdvertisement": "disabled",
                "selfLink": "https://localhost/mgmt/tm/ltm/virtual-address/~Common~1.1.1.2?ver=14.1.2.1",
                "serverScope": "any",
                "spanning": "disabled",
                "trafficGroup": "/Common/traffic-group-1",
                "trafficGroupReference": {
                    "link": "https://localhost/mgmt/tm/cm/traffic-group/~Common~traffic-group-1?ver=14.1.2.1"
                },
                "unit": 1,
            },
            {
                "address": "10.1.1.3",
                "arp": "enabled",
                "autoDelete": "true",
                "connectionLimit": 0,
                "enabled": "yes",
                "floating": "enabled",
                "fullPath": "/Common/10.1.1.3",
                "generation": 1580,
                "icmpEcho": "enabled",
                "inheritedTrafficGroup": "false",
                "kind": "tm:ltm:virtual-address:virtual-addressstate",
                "mask": "255.255.255.255",
                "name": "10.1.1.3",
                "partition": "Common",
                "routeAdvertisement": "disabled",
                "selfLink": "https://localhost/mgmt/tm/ltm/virtual-address/~Common~10.1.1.3?ver=14.1.2.1",
                "serverScope": "any",
                "spanning": "disabled",
                "trafficGroup": "/Common/traffic-group-1",
                "trafficGroupReference": {
                    "link": "https://localhost/mgmt/tm/cm/traffic-group/~Common~traffic-group-1?ver=14.1.2.1"
                },
                "unit": 1,
            },
            {
                "address": "10.1.1.7",
                "arp": "enabled",
                "autoDelete": "true",
                "connectionLimit": 0,
                "enabled": "yes",
                "floating": "enabled",
                "fullPath": "/Common/10.1.1.7",
                "generation": 1458,
                "icmpEcho": "enabled",
                "inheritedTrafficGroup": "false",
                "kind": "tm:ltm:virtual-address:virtual-addressstate",
                "mask": "255.255.255.255",
                "name": "10.1.1.7",
                "partition": "Common",
                "routeAdvertisement": "disabled",
                "selfLink": "https://localhost/mgmt/tm/ltm/virtual-address/~Common~10.1.1.7?ver=14.1.2.1",
                "serverScope": "any",
                "spanning": "disabled",
                "trafficGroup": "/Common/traffic-group-1",
                "trafficGroupReference": {
                    "link": "https://localhost/mgmt/tm/cm/traffic-group/~Common~traffic-group-1?ver=14.1.2.1"
                },
                "unit": 1,
            },
            {
                "address": "10.10.34.250",
                "arp": "enabled",
                "autoDelete": "true",
                "connectionLimit": 0,
                "enabled": "yes",
                "floating": "enabled",
                "fullPath": "/Common/10.10.34.250",
                "generation": 1446,
                "icmpEcho": "enabled",
                "inheritedTrafficGroup": "false",
                "kind": "tm:ltm:virtual-address:virtual-addressstate",
                "mask": "255.255.255.255",
                "name": "10.10.34.250",
                "partition": "Common",
                "routeAdvertisement": "disabled",
                "selfLink": "https://localhost/mgmt/tm/ltm/virtual-address/~Common~10.10.34.250?ver=14.1.2.1",
                "serverScope": "any",
                "spanning": "disabled",
                "trafficGroup": "/Common/traffic-group-1",
                "trafficGroupReference": {
                    "link": "https://localhost/mgmt/tm/cm/traffic-group/~Common~traffic-group-1?ver=14.1.2.1"
                },
                "unit": 1,
            },
            {
                "address": "101.11.11.139",
                "arp": "enabled",
                "autoDelete": "true",
                "connectionLimit": 0,
                "enabled": "yes",
                "floating": "enabled",
                "fullPath": "/Common/101.11.11.139",
                "generation": 1440,
                "icmpEcho": "enabled",
                "inheritedTrafficGroup": "false",
                "kind": "tm:ltm:virtual-address:virtual-addressstate",
                "mask": "255.255.255.255",
                "name": "101.11.11.139",
                "partition": "Common",
                "routeAdvertisement": "disabled",
                "selfLink": "https://localhost/mgmt/tm/ltm/virtual-address/~Common~101.11.11.139?ver=14.1.2.1",
                "serverScope": "any",
                "spanning": "disabled",
                "trafficGroup": "/Common/traffic-group-1",
                "trafficGroupReference": {
                    "link": "https://localhost/mgmt/tm/cm/traffic-group/~Common~traffic-group-1?ver=14.1.2.1"
                },
                "unit": 1,
            },
            {
                "address": "172.16.100.141",
                "arp": "enabled",
                "autoDelete": "true",
                "connectionLimit": 0,
                "enabled": "yes",
                "floating": "enabled",
                "fullPath": "/Common/172.16.100.141",
                "generation": 1413,
                "icmpEcho": "enabled",
                "inheritedTrafficGroup": "false",
                "kind": "tm:ltm:virtual-address:virtual-addressstate",
                "mask": "255.255.255.255",
                "name": "172.16.100.141",
                "partition": "Common",
                "routeAdvertisement": "disabled",
                "selfLink": "https://localhost/mgmt/tm/ltm/virtual-address/~Common~172.16.100.141?ver=14.1.2.1",
                "serverScope": "any",
                "spanning": "disabled",
                "trafficGroup": "/Common/traffic-group-1",
                "trafficGroupReference": {
                    "link": "https://localhost/mgmt/tm/cm/traffic-group/~Common~traffic-group-1?ver=14.1.2.1"
                },
                "unit": 1,
            },
            {
                "address": "172.16.220.141",
                "arp": "enabled",
                "autoDelete": "true",
                "connectionLimit": 0,
                "enabled": "yes",
                "floating": "enabled",
                "fullPath": "/Common/172.16.220.141",
                "generation": 1412,
                "icmpEcho": "enabled",
                "inheritedTrafficGroup": "false",
                "kind": "tm:ltm:virtual-address:virtual-addressstate",
                "mask": "255.255.255.255",
                "name": "172.16.220.141",
                "partition": "Common",
                "routeAdvertisement": "disabled",
                "selfLink": "https://localhost/mgmt/tm/ltm/virtual-address/~Common~172.16.220.141?ver=14.1.2.1",
                "serverScope": "any",
                "spanning": "disabled",
                "trafficGroup": "/Common/traffic-group-1",
                "trafficGroupReference": {
                    "link": "https://localhost/mgmt/tm/cm/traffic-group/~Common~traffic-group-1?ver=14.1.2.1"
                },
                "unit": 1,
            },
        ],
        "kind": "tm:ltm:virtual-address:virtual-addresscollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/virtual-address?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmVirtualaddress(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmVirtualaddress(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
