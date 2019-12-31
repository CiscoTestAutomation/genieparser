# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_profilesip
from genie.libs.parser.bigip.get_ltm_profilesip import LtmProfileSip

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/profile/sip'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:profile:sip:sipcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/profile/sip?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:profile:sip:sipstate",
                    "name": "sip",
                    "partition": "Common",
                    "fullPath": "/Common/sip",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/profile/sip/~Common~sip?ver=14.1.2.1",
                    "algEnable": "disabled",
                    "appService": "none",
                    "community": "none",
                    "defaultsFrom": "none",
                    "description": "none",
                    "dialogAware": "disabled",
                    "dialogEstablishmentTimeout": 10,
                    "enableSipFirewall": "no",
                    "insertRecordRouteHeader": "disabled",
                    "insertViaHeader": "disabled",
                    "logProfile": "none",
                    "logPublisher": "none",
                    "maxMediaSessions": 6,
                    "maxRegistrations": 100,
                    "maxSessionsPerRegistration": 50,
                    "maxSize": 65535,
                    "registrationTimeout": 3600,
                    "rtpProxyStyle": "symmetric",
                    "secureViaHeader": "disabled",
                    "security": "disabled",
                    "sipSessionTimeout": 300,
                    "terminateOnBye": "enabled",
                    "userViaHeader": "none",
                }
            ],
        }


class test_get_ltm_profilesip(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "algEnable": "disabled",
                "appService": "none",
                "community": "none",
                "defaultsFrom": "none",
                "description": "none",
                "dialogAware": "disabled",
                "dialogEstablishmentTimeout": 10,
                "enableSipFirewall": "no",
                "fullPath": "/Common/sip",
                "generation": 1,
                "insertRecordRouteHeader": "disabled",
                "insertViaHeader": "disabled",
                "kind": "tm:ltm:profile:sip:sipstate",
                "logProfile": "none",
                "logPublisher": "none",
                "maxMediaSessions": 6,
                "maxRegistrations": 100,
                "maxSessionsPerRegistration": 50,
                "maxSize": 65535,
                "name": "sip",
                "partition": "Common",
                "registrationTimeout": 3600,
                "rtpProxyStyle": "symmetric",
                "secureViaHeader": "disabled",
                "security": "disabled",
                "selfLink": "https://localhost/mgmt/tm/ltm/profile/sip/~Common~sip?ver=14.1.2.1",
                "sipSessionTimeout": 300,
                "terminateOnBye": "enabled",
                "userViaHeader": "none",
            }
        ],
        "kind": "tm:ltm:profile:sip:sipcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/profile/sip?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmProfileSip(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmProfileSip(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
