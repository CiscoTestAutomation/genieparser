# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_message_routingrouter
from genie.libs.parser.bigip.get_ltm_message_routingrouter import (
    LtmMessageroutingRouter,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/message-routing/mqtt/profile/router'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:message-routing:mqtt:profile:router:routercollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/message-routing/mqtt/profile/router?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:message-routing:mqtt:profile:router:routerstate",
                    "name": "mqttrouter",
                    "partition": "Common",
                    "fullPath": "/Common/mqttrouter",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/message-routing/mqtt/profile/router/~Common~mqttrouter?ver=14.1.2.1",
                    "inheritedTrafficGroup": "true",
                    "maxPayloadPendingBytes": 32768,
                    "maxPendingBytes": 32768,
                    "maxPendingMessages": 64,
                    "maxRetries": 1,
                    "trafficGroup": "/Common/traffic-group-1",
                    "trafficGroupReference": {
                        "link": "https://localhost/mgmt/tm/cm/traffic-group/~Common~traffic-group-1?ver=14.1.2.1"
                    },
                    "useLocalConnection": "enabled",
                }
            ],
        }


class test_get_ltm_message_routingrouter(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "fullPath": "/Common/mqttrouter",
                "generation": 1,
                "inheritedTrafficGroup": "true",
                "kind": "tm:ltm:message-routing:mqtt:profile:router:routerstate",
                "maxPayloadPendingBytes": 32768,
                "maxPendingBytes": 32768,
                "maxPendingMessages": 64,
                "maxRetries": 1,
                "name": "mqttrouter",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/message-routing/mqtt/profile/router/~Common~mqttrouter?ver=14.1.2.1",
                "trafficGroup": "/Common/traffic-group-1",
                "trafficGroupReference": {
                    "link": "https://localhost/mgmt/tm/cm/traffic-group/~Common~traffic-group-1?ver=14.1.2.1"
                },
                "useLocalConnection": "enabled",
            }
        ],
        "kind": "tm:ltm:message-routing:mqtt:profile:router:routercollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/message-routing/mqtt/profile/router?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmMessageroutingRouter(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmMessageroutingRouter(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
