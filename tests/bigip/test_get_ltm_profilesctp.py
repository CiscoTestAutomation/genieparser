# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_profilesctp
from genie.libs.parser.bigip.get_ltm_profilesctp import LtmProfileSctp

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/profile/sctp'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:profile:sctp:sctpcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/profile/sctp?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:profile:sctp:sctpstate",
                    "name": "sctp",
                    "partition": "Common",
                    "fullPath": "/Common/sctp",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/profile/sctp/~Common~sctp?ver=14.1.2.1",
                    "appService": "none",
                    "clientSideMultihoming": "disabled",
                    "cookieExpiration": 60,
                    "defaultsFrom": "none",
                    "description": "none",
                    "heartbeatInterval": 30,
                    "heartbeatMaxBurst": 1,
                    "idleTimeout": 300,
                    "inStreams": 2,
                    "initMaxRetries": 8,
                    "ipTos": "0",
                    "linkQos": "0",
                    "maxBurst": 4,
                    "maxCommunicationPaths": 16,
                    "maxPathRetransmitLimit": 5,
                    "outStreams": 2,
                    "proxyBufferHigh": 16384,
                    "proxyBufferLow": 4096,
                    "receiveChunks": 256,
                    "receiveOrdered": "enabled",
                    "receiveWindowSize": 65535,
                    "resetOnTimeout": "enabled",
                    "rtoInitial": 3000,
                    "rtoMax": 60000,
                    "rtoMin": 1000,
                    "sackTimeout": 200,
                    "secret": "$M$jx$0+ART/wNjLBxkv97jRtGNA==",
                    "sendBufferSize": 65536,
                    "sendMaxRetries": 10,
                    "sendPartial": "disabled",
                    "serverSideMultihoming": "disabled",
                    "tcpShutdown": "disabled",
                    "transmitChunks": 256,
                }
            ],
        }


class test_get_ltm_profilesctp(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "appService": "none",
                "clientSideMultihoming": "disabled",
                "cookieExpiration": 60,
                "defaultsFrom": "none",
                "description": "none",
                "fullPath": "/Common/sctp",
                "generation": 1,
                "heartbeatInterval": 30,
                "heartbeatMaxBurst": 1,
                "idleTimeout": 300,
                "inStreams": 2,
                "initMaxRetries": 8,
                "ipTos": "0",
                "kind": "tm:ltm:profile:sctp:sctpstate",
                "linkQos": "0",
                "maxBurst": 4,
                "maxCommunicationPaths": 16,
                "maxPathRetransmitLimit": 5,
                "name": "sctp",
                "outStreams": 2,
                "partition": "Common",
                "proxyBufferHigh": 16384,
                "proxyBufferLow": 4096,
                "receiveChunks": 256,
                "receiveOrdered": "enabled",
                "receiveWindowSize": 65535,
                "resetOnTimeout": "enabled",
                "rtoInitial": 3000,
                "rtoMax": 60000,
                "rtoMin": 1000,
                "sackTimeout": 200,
                "secret": "$M$jx$0+ART/wNjLBxkv97jRtGNA==",
                "selfLink": "https://localhost/mgmt/tm/ltm/profile/sctp/~Common~sctp?ver=14.1.2.1",
                "sendBufferSize": 65536,
                "sendMaxRetries": 10,
                "sendPartial": "disabled",
                "serverSideMultihoming": "disabled",
                "tcpShutdown": "disabled",
                "transmitChunks": 256,
            }
        ],
        "kind": "tm:ltm:profile:sctp:sctpcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/profile/sctp?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmProfileSctp(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmProfileSctp(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
