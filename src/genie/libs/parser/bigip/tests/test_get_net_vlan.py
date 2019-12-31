# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_net_vlan
from genie.libs.parser.bigip.get_net_vlan import NetVlan

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/net/vlan'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:net:vlan:vlancollectionstate",
            "selfLink": "https://localhost/mgmt/tm/net/vlan?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:net:vlan:vlanstate",
                    "name": "External",
                    "partition": "Common",
                    "fullPath": "/Common/External",
                    "generation": 1383,
                    "selfLink": "https://localhost/mgmt/tm/net/vlan/~Common~External?ver=14.1.2.1",
                    "autoLasthop": "default",
                    "cmpHash": "default",
                    "dagRoundRobin": "disabled",
                    "dagTunnel": "outer",
                    "failsafe": "disabled",
                    "failsafeAction": "failover-restart-tm",
                    "failsafeTimeout": 90,
                    "fwdMode": "l3",
                    "hardwareSyncookie": "disabled",
                    "ifIndex": 144,
                    "learning": "enable-forward",
                    "mtu": 1500,
                    "sflow": {
                        "pollInterval": 0,
                        "pollIntervalGlobal": "yes",
                        "samplingRate": 0,
                        "samplingRateGlobal": "yes",
                    },
                    "sourceChecking": "disabled",
                    "synFloodRateLimit": 1000,
                    "syncacheThreshold": 6000,
                    "tag": 4094,
                    "interfacesReference": {
                        "link": "https://localhost/mgmt/tm/net/vlan/~Common~External/interfaces?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                },
                {
                    "kind": "tm:net:vlan:vlanstate",
                    "name": "HA",
                    "partition": "Common",
                    "fullPath": "/Common/HA",
                    "generation": 994,
                    "selfLink": "https://localhost/mgmt/tm/net/vlan/~Common~HA?ver=14.1.2.1",
                    "autoLasthop": "default",
                    "cmpHash": "default",
                    "dagRoundRobin": "disabled",
                    "dagTunnel": "outer",
                    "failsafe": "disabled",
                    "failsafeAction": "failover-restart-tm",
                    "failsafeTimeout": 90,
                    "fwdMode": "l3",
                    "hardwareSyncookie": "disabled",
                    "ifIndex": 192,
                    "learning": "enable-forward",
                    "mtu": 1500,
                    "sflow": {
                        "pollInterval": 0,
                        "pollIntervalGlobal": "yes",
                        "samplingRate": 0,
                        "samplingRateGlobal": "yes",
                    },
                    "sourceChecking": "disabled",
                    "synFloodRateLimit": 1000,
                    "syncacheThreshold": 6000,
                    "tag": 4093,
                    "interfacesReference": {
                        "link": "https://localhost/mgmt/tm/net/vlan/~Common~HA/interfaces?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                },
                {
                    "kind": "tm:net:vlan:vlanstate",
                    "name": "Internal",
                    "partition": "Common",
                    "fullPath": "/Common/Internal",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/net/vlan/~Common~Internal?ver=14.1.2.1",
                    "autoLasthop": "default",
                    "cmpHash": "default",
                    "dagRoundRobin": "disabled",
                    "dagTunnel": "outer",
                    "failsafe": "disabled",
                    "failsafeAction": "failover-restart-tm",
                    "failsafeTimeout": 90,
                    "fwdMode": "l3",
                    "hardwareSyncookie": "disabled",
                    "ifIndex": 160,
                    "learning": "enable-forward",
                    "mtu": 1500,
                    "sflow": {
                        "pollInterval": 0,
                        "pollIntervalGlobal": "yes",
                        "samplingRate": 0,
                        "samplingRateGlobal": "yes",
                    },
                    "sourceChecking": "disabled",
                    "synFloodRateLimit": 1000,
                    "syncacheThreshold": 6000,
                    "tag": 11,
                    "interfacesReference": {
                        "link": "https://localhost/mgmt/tm/net/vlan/~Common~Internal/interfaces?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                },
                {
                    "kind": "tm:net:vlan:vlanstate",
                    "name": "Services",
                    "partition": "Common",
                    "fullPath": "/Common/Services",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/net/vlan/~Common~Services?ver=14.1.2.1",
                    "autoLasthop": "default",
                    "cmpHash": "default",
                    "dagRoundRobin": "disabled",
                    "dagTunnel": "outer",
                    "failsafe": "disabled",
                    "failsafeAction": "failover-restart-tm",
                    "failsafeTimeout": 90,
                    "fwdMode": "l3",
                    "hardwareSyncookie": "disabled",
                    "ifIndex": 176,
                    "learning": "enable-forward",
                    "mtu": 1500,
                    "sflow": {
                        "pollInterval": 0,
                        "pollIntervalGlobal": "yes",
                        "samplingRate": 0,
                        "samplingRateGlobal": "yes",
                    },
                    "sourceChecking": "disabled",
                    "synFloodRateLimit": 1000,
                    "syncacheThreshold": 6000,
                    "tag": 12,
                    "interfacesReference": {
                        "link": "https://localhost/mgmt/tm/net/vlan/~Common~Services/interfaces?ver=14.1.2.1",
                        "isSubcollection": True,
                    },
                },
            ],
        }


class test_get_net_vlan(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "autoLasthop": "default",
                "cmpHash": "default",
                "dagRoundRobin": "disabled",
                "dagTunnel": "outer",
                "failsafe": "disabled",
                "failsafeAction": "failover-restart-tm",
                "failsafeTimeout": 90,
                "fullPath": "/Common/External",
                "fwdMode": "l3",
                "generation": 1383,
                "hardwareSyncookie": "disabled",
                "ifIndex": 144,
                "interfacesReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/net/vlan/~Common~External/interfaces?ver=14.1.2.1",
                },
                "kind": "tm:net:vlan:vlanstate",
                "learning": "enable-forward",
                "mtu": 1500,
                "name": "External",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/net/vlan/~Common~External?ver=14.1.2.1",
                "sflow": {
                    "pollInterval": 0,
                    "pollIntervalGlobal": "yes",
                    "samplingRate": 0,
                    "samplingRateGlobal": "yes",
                },
                "sourceChecking": "disabled",
                "synFloodRateLimit": 1000,
                "syncacheThreshold": 6000,
                "tag": 4094,
            },
            {
                "autoLasthop": "default",
                "cmpHash": "default",
                "dagRoundRobin": "disabled",
                "dagTunnel": "outer",
                "failsafe": "disabled",
                "failsafeAction": "failover-restart-tm",
                "failsafeTimeout": 90,
                "fullPath": "/Common/HA",
                "fwdMode": "l3",
                "generation": 994,
                "hardwareSyncookie": "disabled",
                "ifIndex": 192,
                "interfacesReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/net/vlan/~Common~HA/interfaces?ver=14.1.2.1",
                },
                "kind": "tm:net:vlan:vlanstate",
                "learning": "enable-forward",
                "mtu": 1500,
                "name": "HA",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/net/vlan/~Common~HA?ver=14.1.2.1",
                "sflow": {
                    "pollInterval": 0,
                    "pollIntervalGlobal": "yes",
                    "samplingRate": 0,
                    "samplingRateGlobal": "yes",
                },
                "sourceChecking": "disabled",
                "synFloodRateLimit": 1000,
                "syncacheThreshold": 6000,
                "tag": 4093,
            },
            {
                "autoLasthop": "default",
                "cmpHash": "default",
                "dagRoundRobin": "disabled",
                "dagTunnel": "outer",
                "failsafe": "disabled",
                "failsafeAction": "failover-restart-tm",
                "failsafeTimeout": 90,
                "fullPath": "/Common/Internal",
                "fwdMode": "l3",
                "generation": 1,
                "hardwareSyncookie": "disabled",
                "ifIndex": 160,
                "interfacesReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/net/vlan/~Common~Internal/interfaces?ver=14.1.2.1",
                },
                "kind": "tm:net:vlan:vlanstate",
                "learning": "enable-forward",
                "mtu": 1500,
                "name": "Internal",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/net/vlan/~Common~Internal?ver=14.1.2.1",
                "sflow": {
                    "pollInterval": 0,
                    "pollIntervalGlobal": "yes",
                    "samplingRate": 0,
                    "samplingRateGlobal": "yes",
                },
                "sourceChecking": "disabled",
                "synFloodRateLimit": 1000,
                "syncacheThreshold": 6000,
                "tag": 11,
            },
            {
                "autoLasthop": "default",
                "cmpHash": "default",
                "dagRoundRobin": "disabled",
                "dagTunnel": "outer",
                "failsafe": "disabled",
                "failsafeAction": "failover-restart-tm",
                "failsafeTimeout": 90,
                "fullPath": "/Common/Services",
                "fwdMode": "l3",
                "generation": 1,
                "hardwareSyncookie": "disabled",
                "ifIndex": 176,
                "interfacesReference": {
                    "isSubcollection": True,
                    "link": "https://localhost/mgmt/tm/net/vlan/~Common~Services/interfaces?ver=14.1.2.1",
                },
                "kind": "tm:net:vlan:vlanstate",
                "learning": "enable-forward",
                "mtu": 1500,
                "name": "Services",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/net/vlan/~Common~Services?ver=14.1.2.1",
                "sflow": {
                    "pollInterval": 0,
                    "pollIntervalGlobal": "yes",
                    "samplingRate": 0,
                    "samplingRateGlobal": "yes",
                },
                "sourceChecking": "disabled",
                "synFloodRateLimit": 1000,
                "syncacheThreshold": 6000,
                "tag": 12,
            },
        ],
        "kind": "tm:net:vlan:vlancollectionstate",
        "selfLink": "https://localhost/mgmt/tm/net/vlan?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = NetVlan(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = NetVlan(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
