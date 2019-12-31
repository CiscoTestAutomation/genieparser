# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_message_routingsession
from genie.libs.parser.bigip.get_ltm_message_routingsession import (
    LtmMessageroutingSession,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/message-routing/mqtt/profile/session'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:message-routing:mqtt:profile:session:sessioncollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/message-routing/mqtt/profile/session?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:message-routing:mqtt:profile:session:sessionstate",
                    "name": "mqttsession",
                    "partition": "Common",
                    "fullPath": "/Common/mqttsession",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/message-routing/mqtt/profile/session/~Common~mqttsession?ver=14.1.2.1",
                    "clientWillHandlingMode": "send-local-copy",
                    "keepaliveInt": 60,
                    "peeredSessionMode": "disabled",
                    "serverWillHandlingMode": "copy-from-client",
                }
            ],
        }


class test_get_ltm_message_routingsession(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "clientWillHandlingMode": "send-local-copy",
                "fullPath": "/Common/mqttsession",
                "generation": 1,
                "keepaliveInt": 60,
                "kind": "tm:ltm:message-routing:mqtt:profile:session:sessionstate",
                "name": "mqttsession",
                "partition": "Common",
                "peeredSessionMode": "disabled",
                "selfLink": "https://localhost/mgmt/tm/ltm/message-routing/mqtt/profile/session/~Common~mqttsession?ver=14.1.2.1",
                "serverWillHandlingMode": "copy-from-client",
            }
        ],
        "kind": "tm:ltm:message-routing:mqtt:profile:session:sessioncollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/message-routing/mqtt/profile/session?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmMessageroutingSession(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmMessageroutingSession(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
