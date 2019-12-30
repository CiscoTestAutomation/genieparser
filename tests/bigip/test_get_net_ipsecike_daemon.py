# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_net_ipsecike_daemon
from genie.libs.parser.bigip.get_net_ipsecike_daemon import NetIpsecIkedaemon

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/net/ipsec/ike-daemon'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:net:ipsec:ike-daemon:ike-daemoncollectionstate",
            "selfLink": "https://localhost/mgmt/tm/net/ipsec/ike-daemon?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:net:ipsec:ike-daemon:ike-daemonstate",
                    "name": "ikedaemon",
                    "partition": "Common",
                    "fullPath": "/Common/ikedaemon",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/net/ipsec/ike-daemon/~Common~ikedaemon?ver=14.1.2.1",
                    "isakmpNattPort": 4500,
                    "isakmpPort": 500,
                    "logLevel": "info",
                    "logPublisher": "/Common/default-ipsec-log-publisher",
                    "logPublisherReference": {
                        "link": "https://localhost/mgmt/tm/sys/log-config/publisher/~Common~default-ipsec-log-publisher?ver=14.1.2.1"
                    },
                    "nattKeepAlive": 0,
                }
            ],
        }


class test_get_net_ipsecike_daemon(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "fullPath": "/Common/ikedaemon",
                "generation": 1,
                "isakmpNattPort": 4500,
                "isakmpPort": 500,
                "kind": "tm:net:ipsec:ike-daemon:ike-daemonstate",
                "logLevel": "info",
                "logPublisher": "/Common/default-ipsec-log-publisher",
                "logPublisherReference": {
                    "link": "https://localhost/mgmt/tm/sys/log-config/publisher/~Common~default-ipsec-log-publisher?ver=14.1.2.1"
                },
                "name": "ikedaemon",
                "nattKeepAlive": 0,
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/net/ipsec/ike-daemon/~Common~ikedaemon?ver=14.1.2.1",
            }
        ],
        "kind": "tm:net:ipsec:ike-daemon:ike-daemoncollectionstate",
        "selfLink": "https://localhost/mgmt/tm/net/ipsec/ike-daemon?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = NetIpsecIkedaemon(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = NetIpsecIkedaemon(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
