# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_net_interface
from genie.libs.parser.bigip.get_net_interface import NetInterface

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/net/interface'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:net:interface:interfacecollectionstate",
            "selfLink": "https://localhost/mgmt/tm/net/interface?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:net:interface:interfacestate",
                    "name": "1.1",
                    "fullPath": "1.1",
                    "generation": 2163,
                    "selfLink": "https://localhost/mgmt/tm/net/interface/1.1?ver=14.1.2.1",
                    "bundle": "not-supported",
                    "bundleSpeed": "not-supported",
                    "enabled": True,
                    "flowControl": "tx-rx",
                    "forceGigabitFiber": "disabled",
                    "forwardErrorCorrection": "not-supported",
                    "ifIndex": 48,
                    "lldpAdmin": "txonly",
                    "lldpTlvmap": 130943,
                    "macAddress": "00:0c:29:35:0d:c7",
                    "mediaActive": "10000T-FD",
                    "mediaFixed": "10000T-FD",
                    "mediaMax": "auto",
                    "mediaSfp": "auto",
                    "mtu": 1500,
                    "portFwdMode": "l3",
                    "preferPort": "sfp",
                    "qinqEthertype": "0x8100",
                    "sflow": {"pollInterval": 0, "pollIntervalGlobal": "yes"},
                    "stp": "enabled",
                    "stpAutoEdgePort": "enabled",
                    "stpEdgePort": "true",
                    "stpLinkType": "auto",
                },
                {
                    "kind": "tm:net:interface:interfacestate",
                    "name": "1.2",
                    "fullPath": "1.2",
                    "generation": 2162,
                    "selfLink": "https://localhost/mgmt/tm/net/interface/1.2?ver=14.1.2.1",
                    "bundle": "not-supported",
                    "bundleSpeed": "not-supported",
                    "enabled": True,
                    "flowControl": "tx-rx",
                    "forceGigabitFiber": "disabled",
                    "forwardErrorCorrection": "not-supported",
                    "ifIndex": 64,
                    "lldpAdmin": "txonly",
                    "lldpTlvmap": 130943,
                    "macAddress": "00:0c:29:35:0d:d1",
                    "mediaActive": "10000T-FD",
                    "mediaFixed": "10000T-FD",
                    "mediaMax": "auto",
                    "mediaSfp": "auto",
                    "mtu": 1500,
                    "portFwdMode": "l3",
                    "preferPort": "sfp",
                    "qinqEthertype": "0x8100",
                    "sflow": {"pollInterval": 0, "pollIntervalGlobal": "yes"},
                    "stp": "enabled",
                    "stpAutoEdgePort": "enabled",
                    "stpEdgePort": "true",
                    "stpLinkType": "auto",
                },
                {
                    "kind": "tm:net:interface:interfacestate",
                    "name": "1.3",
                    "fullPath": "1.3",
                    "generation": 2157,
                    "selfLink": "https://localhost/mgmt/tm/net/interface/1.3?ver=14.1.2.1",
                    "bundle": "not-supported",
                    "bundleSpeed": "not-supported",
                    "enabled": True,
                    "flowControl": "tx-rx",
                    "forceGigabitFiber": "disabled",
                    "forwardErrorCorrection": "not-supported",
                    "ifIndex": 80,
                    "lldpAdmin": "txonly",
                    "lldpTlvmap": 130943,
                    "macAddress": "00:0c:29:35:0d:db",
                    "mediaActive": "10000T-FD",
                    "mediaFixed": "10000T-FD",
                    "mediaMax": "auto",
                    "mediaSfp": "auto",
                    "mtu": 1500,
                    "portFwdMode": "l3",
                    "preferPort": "sfp",
                    "qinqEthertype": "0x8100",
                    "sflow": {"pollInterval": 0, "pollIntervalGlobal": "yes"},
                    "stp": "enabled",
                    "stpAutoEdgePort": "enabled",
                    "stpEdgePort": "true",
                    "stpLinkType": "auto",
                },
                {
                    "kind": "tm:net:interface:interfacestate",
                    "name": "mgmt",
                    "fullPath": "mgmt",
                    "generation": 2082,
                    "selfLink": "https://localhost/mgmt/tm/net/interface/mgmt?ver=14.1.2.1",
                    "bundle": "not-supported",
                    "bundleSpeed": "not-supported",
                    "enabled": True,
                    "flowControl": "tx-rx",
                    "forceGigabitFiber": "disabled",
                    "forwardErrorCorrection": "not-supported",
                    "ifIndex": 32,
                    "lldpAdmin": "txonly",
                    "lldpTlvmap": 130943,
                    "macAddress": "00:0c:29:35:0d:bd",
                    "mediaActive": "100TX-FD",
                    "mediaFixed": "auto",
                    "mediaSfp": "auto",
                    "mtu": 1500,
                    "portFwdMode": "l3",
                    "preferPort": "sfp",
                    "qinqEthertype": "0x8100",
                    "sflow": {"pollInterval": 0, "pollIntervalGlobal": "yes"},
                    "stp": "enabled",
                    "stpAutoEdgePort": "enabled",
                    "stpEdgePort": "true",
                    "stpLinkType": "auto",
                },
            ],
        }


class test_get_net_interface(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "bundle": "not-supported",
                "bundleSpeed": "not-supported",
                "enabled": True,
                "flowControl": "tx-rx",
                "forceGigabitFiber": "disabled",
                "forwardErrorCorrection": "not-supported",
                "fullPath": "1.1",
                "generation": 2163,
                "ifIndex": 48,
                "kind": "tm:net:interface:interfacestate",
                "lldpAdmin": "txonly",
                "lldpTlvmap": 130943,
                "macAddress": "00:0c:29:35:0d:c7",
                "mediaActive": "10000T-FD",
                "mediaFixed": "10000T-FD",
                "mediaMax": "auto",
                "mediaSfp": "auto",
                "mtu": 1500,
                "name": "1.1",
                "portFwdMode": "l3",
                "preferPort": "sfp",
                "qinqEthertype": "0x8100",
                "selfLink": "https://localhost/mgmt/tm/net/interface/1.1?ver=14.1.2.1",
                "sflow": {"pollInterval": 0, "pollIntervalGlobal": "yes"},
                "stp": "enabled",
                "stpAutoEdgePort": "enabled",
                "stpEdgePort": "true",
                "stpLinkType": "auto",
            },
            {
                "bundle": "not-supported",
                "bundleSpeed": "not-supported",
                "enabled": True,
                "flowControl": "tx-rx",
                "forceGigabitFiber": "disabled",
                "forwardErrorCorrection": "not-supported",
                "fullPath": "1.2",
                "generation": 2162,
                "ifIndex": 64,
                "kind": "tm:net:interface:interfacestate",
                "lldpAdmin": "txonly",
                "lldpTlvmap": 130943,
                "macAddress": "00:0c:29:35:0d:d1",
                "mediaActive": "10000T-FD",
                "mediaFixed": "10000T-FD",
                "mediaMax": "auto",
                "mediaSfp": "auto",
                "mtu": 1500,
                "name": "1.2",
                "portFwdMode": "l3",
                "preferPort": "sfp",
                "qinqEthertype": "0x8100",
                "selfLink": "https://localhost/mgmt/tm/net/interface/1.2?ver=14.1.2.1",
                "sflow": {"pollInterval": 0, "pollIntervalGlobal": "yes"},
                "stp": "enabled",
                "stpAutoEdgePort": "enabled",
                "stpEdgePort": "true",
                "stpLinkType": "auto",
            },
            {
                "bundle": "not-supported",
                "bundleSpeed": "not-supported",
                "enabled": True,
                "flowControl": "tx-rx",
                "forceGigabitFiber": "disabled",
                "forwardErrorCorrection": "not-supported",
                "fullPath": "1.3",
                "generation": 2157,
                "ifIndex": 80,
                "kind": "tm:net:interface:interfacestate",
                "lldpAdmin": "txonly",
                "lldpTlvmap": 130943,
                "macAddress": "00:0c:29:35:0d:db",
                "mediaActive": "10000T-FD",
                "mediaFixed": "10000T-FD",
                "mediaMax": "auto",
                "mediaSfp": "auto",
                "mtu": 1500,
                "name": "1.3",
                "portFwdMode": "l3",
                "preferPort": "sfp",
                "qinqEthertype": "0x8100",
                "selfLink": "https://localhost/mgmt/tm/net/interface/1.3?ver=14.1.2.1",
                "sflow": {"pollInterval": 0, "pollIntervalGlobal": "yes"},
                "stp": "enabled",
                "stpAutoEdgePort": "enabled",
                "stpEdgePort": "true",
                "stpLinkType": "auto",
            },
            {
                "bundle": "not-supported",
                "bundleSpeed": "not-supported",
                "enabled": True,
                "flowControl": "tx-rx",
                "forceGigabitFiber": "disabled",
                "forwardErrorCorrection": "not-supported",
                "fullPath": "mgmt",
                "generation": 2082,
                "ifIndex": 32,
                "kind": "tm:net:interface:interfacestate",
                "lldpAdmin": "txonly",
                "lldpTlvmap": 130943,
                "macAddress": "00:0c:29:35:0d:bd",
                "mediaActive": "100TX-FD",
                "mediaFixed": "auto",
                "mediaSfp": "auto",
                "mtu": 1500,
                "name": "mgmt",
                "portFwdMode": "l3",
                "preferPort": "sfp",
                "qinqEthertype": "0x8100",
                "selfLink": "https://localhost/mgmt/tm/net/interface/mgmt?ver=14.1.2.1",
                "sflow": {"pollInterval": 0, "pollIntervalGlobal": "yes"},
                "stp": "enabled",
                "stpAutoEdgePort": "enabled",
                "stpEdgePort": "true",
                "stpLinkType": "auto",
            },
        ],
        "kind": "tm:net:interface:interfacecollectionstate",
        "selfLink": "https://localhost/mgmt/tm/net/interface?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = NetInterface(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = NetInterface(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
