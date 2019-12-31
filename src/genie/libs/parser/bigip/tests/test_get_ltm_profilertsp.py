# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_profilertsp
from genie.libs.parser.bigip.get_ltm_profilertsp import LtmProfileRtsp

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/profile/rtsp'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:profile:rtsp:rtspcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/profile/rtsp?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:profile:rtsp:rtspstate",
                    "name": "rtsp",
                    "partition": "Common",
                    "fullPath": "/Common/rtsp",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/profile/rtsp/~Common~rtsp?ver=14.1.2.1",
                    "appService": "none",
                    "checkSource": "enabled",
                    "defaultsFrom": "none",
                    "description": "none",
                    "idleTimeout": "300",
                    "logProfile": "none",
                    "logPublisher": "none",
                    "maxHeaderSize": 4096,
                    "maxQueuedData": 32768,
                    "multicastRedirect": "disabled",
                    "proxy": "none",
                    "proxyHeader": "none",
                    "realHttpPersistence": "enabled",
                    "rtcpPort": 0,
                    "rtpPort": 0,
                    "sessionReconnect": "disabled",
                    "unicastRedirect": "disabled",
                }
            ],
        }


class test_get_ltm_profilertsp(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "appService": "none",
                "checkSource": "enabled",
                "defaultsFrom": "none",
                "description": "none",
                "fullPath": "/Common/rtsp",
                "generation": 1,
                "idleTimeout": "300",
                "kind": "tm:ltm:profile:rtsp:rtspstate",
                "logProfile": "none",
                "logPublisher": "none",
                "maxHeaderSize": 4096,
                "maxQueuedData": 32768,
                "multicastRedirect": "disabled",
                "name": "rtsp",
                "partition": "Common",
                "proxy": "none",
                "proxyHeader": "none",
                "realHttpPersistence": "enabled",
                "rtcpPort": 0,
                "rtpPort": 0,
                "selfLink": "https://localhost/mgmt/tm/ltm/profile/rtsp/~Common~rtsp?ver=14.1.2.1",
                "sessionReconnect": "disabled",
                "unicastRedirect": "disabled",
            }
        ],
        "kind": "tm:ltm:profile:rtsp:rtspcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/profile/rtsp?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmProfileRtsp(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmProfileRtsp(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
