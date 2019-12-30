# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_net_self
from genie.libs.parser.bigip.get_net_self import NetSelf

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/net/self'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:net:self:selfcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/net/self?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:net:self:selfstate",
                    "name": "Services-SelfIP",
                    "partition": "Common",
                    "fullPath": "/Common/Services-SelfIP",
                    "generation": 1015,
                    "selfLink": "https://localhost/mgmt/tm/net/self/~Common~Services-SelfIP?ver=14.1.2.1",
                    "address": "172.16.2.233/24",
                    "addressSource": "from-user",
                    "floating": "disabled",
                    "inheritedTrafficGroup": "false",
                    "trafficGroup": "/Common/traffic-group-local-only",
                    "trafficGroupReference": {
                        "link": "https://localhost/mgmt/tm/cm/traffic-group/~Common~traffic-group-local-only?ver=14.1.2.1"
                    },
                    "unit": 0,
                    "vlan": "/Common/Services",
                    "vlanReference": {
                        "link": "https://localhost/mgmt/tm/net/vlan/~Common~Services?ver=14.1.2.1"
                    },
                    "allowService": ["default"],
                },
                {
                    "kind": "tm:net:self:selfstate",
                    "name": "Internal-SelfIP",
                    "partition": "Common",
                    "fullPath": "/Common/Internal-SelfIP",
                    "generation": 1014,
                    "selfLink": "https://localhost/mgmt/tm/net/self/~Common~Internal-SelfIP?ver=14.1.2.1",
                    "address": "172.16.1.233/24",
                    "addressSource": "from-user",
                    "floating": "disabled",
                    "inheritedTrafficGroup": "false",
                    "trafficGroup": "/Common/traffic-group-local-only",
                    "trafficGroupReference": {
                        "link": "https://localhost/mgmt/tm/cm/traffic-group/~Common~traffic-group-local-only?ver=14.1.2.1"
                    },
                    "unit": 0,
                    "vlan": "/Common/Internal",
                    "vlanReference": {
                        "link": "https://localhost/mgmt/tm/net/vlan/~Common~Internal?ver=14.1.2.1"
                    },
                    "allowService": ["default"],
                },
                {
                    "kind": "tm:net:self:selfstate",
                    "name": "External-SelfIP",
                    "partition": "Common",
                    "fullPath": "/Common/External-SelfIP",
                    "generation": 1013,
                    "selfLink": "https://localhost/mgmt/tm/net/self/~Common~External-SelfIP?ver=14.1.2.1",
                    "address": "192.168.40.233/24",
                    "addressSource": "from-user",
                    "floating": "disabled",
                    "inheritedTrafficGroup": "false",
                    "trafficGroup": "/Common/traffic-group-local-only",
                    "trafficGroupReference": {
                        "link": "https://localhost/mgmt/tm/cm/traffic-group/~Common~traffic-group-local-only?ver=14.1.2.1"
                    },
                    "unit": 0,
                    "vlan": "/Common/External",
                    "vlanReference": {
                        "link": "https://localhost/mgmt/tm/net/vlan/~Common~External?ver=14.1.2.1"
                    },
                    "allowService": ["default"],
                },
            ],
        }


class test_get_net_self(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "address": "172.16.2.233/24",
                "addressSource": "from-user",
                "allowService": ["default"],
                "floating": "disabled",
                "fullPath": "/Common/Services-SelfIP",
                "generation": 1015,
                "inheritedTrafficGroup": "false",
                "kind": "tm:net:self:selfstate",
                "name": "Services-SelfIP",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/net/self/~Common~Services-SelfIP?ver=14.1.2.1",
                "trafficGroup": "/Common/traffic-group-local-only",
                "trafficGroupReference": {
                    "link": "https://localhost/mgmt/tm/cm/traffic-group/~Common~traffic-group-local-only?ver=14.1.2.1"
                },
                "unit": 0,
                "vlan": "/Common/Services",
                "vlanReference": {
                    "link": "https://localhost/mgmt/tm/net/vlan/~Common~Services?ver=14.1.2.1"
                },
            },
            {
                "address": "172.16.1.233/24",
                "addressSource": "from-user",
                "allowService": ["default"],
                "floating": "disabled",
                "fullPath": "/Common/Internal-SelfIP",
                "generation": 1014,
                "inheritedTrafficGroup": "false",
                "kind": "tm:net:self:selfstate",
                "name": "Internal-SelfIP",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/net/self/~Common~Internal-SelfIP?ver=14.1.2.1",
                "trafficGroup": "/Common/traffic-group-local-only",
                "trafficGroupReference": {
                    "link": "https://localhost/mgmt/tm/cm/traffic-group/~Common~traffic-group-local-only?ver=14.1.2.1"
                },
                "unit": 0,
                "vlan": "/Common/Internal",
                "vlanReference": {
                    "link": "https://localhost/mgmt/tm/net/vlan/~Common~Internal?ver=14.1.2.1"
                },
            },
            {
                "address": "192.168.40.233/24",
                "addressSource": "from-user",
                "allowService": ["default"],
                "floating": "disabled",
                "fullPath": "/Common/External-SelfIP",
                "generation": 1013,
                "inheritedTrafficGroup": "false",
                "kind": "tm:net:self:selfstate",
                "name": "External-SelfIP",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/net/self/~Common~External-SelfIP?ver=14.1.2.1",
                "trafficGroup": "/Common/traffic-group-local-only",
                "trafficGroupReference": {
                    "link": "https://localhost/mgmt/tm/cm/traffic-group/~Common~traffic-group-local-only?ver=14.1.2.1"
                },
                "unit": 0,
                "vlan": "/Common/External",
                "vlanReference": {
                    "link": "https://localhost/mgmt/tm/net/vlan/~Common~External?ver=14.1.2.1"
                },
            },
        ],
        "kind": "tm:net:self:selfcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/net/self?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = NetSelf(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = NetSelf(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
