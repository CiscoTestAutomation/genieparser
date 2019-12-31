# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_profilerequest_log
from genie.libs.parser.bigip.get_ltm_profilerequest_log import (
    LtmProfileRequestlog,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/profile/request-log'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:profile:request-log:request-logcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/profile/request-log?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:profile:request-log:request-logstate",
                    "name": "request-log",
                    "partition": "Common",
                    "fullPath": "/Common/request-log",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/profile/request-log/~Common~request-log?ver=14.1.2.1",
                    "appService": "none",
                    "defaultsFrom": "none",
                    "description": "none",
                    "logRequestLoggingErrors": "no",
                    "logResponseByDefault": "yes",
                    "logResponseLoggingErrors": "disabled",
                    "proxyCloseOnError": "no",
                    "proxyRespondOnLoggingError": "no",
                    "proxyResponse": "none",
                    "requestLogErrorPool": "none",
                    "requestLogErrorProtocol": "mds-udp",
                    "requestLogErrorTemplate": "none",
                    "requestLogPool": "none",
                    "requestLogProtocol": "mds-udp",
                    "requestLogTemplate": "none",
                    "requestLogging": "disabled",
                    "responseLogErrorPool": "none",
                    "responseLogErrorProtocol": "mds-udp",
                    "responseLogErrorTemplate": "none",
                    "responseLogPool": "none",
                    "responseLogProtocol": "mds-udp",
                    "responseLogTemplate": "none",
                    "responseLogging": "disabled",
                }
            ],
        }


class test_get_ltm_profilerequest_log(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "appService": "none",
                "defaultsFrom": "none",
                "description": "none",
                "fullPath": "/Common/request-log",
                "generation": 1,
                "kind": "tm:ltm:profile:request-log:request-logstate",
                "logRequestLoggingErrors": "no",
                "logResponseByDefault": "yes",
                "logResponseLoggingErrors": "disabled",
                "name": "request-log",
                "partition": "Common",
                "proxyCloseOnError": "no",
                "proxyRespondOnLoggingError": "no",
                "proxyResponse": "none",
                "requestLogErrorPool": "none",
                "requestLogErrorProtocol": "mds-udp",
                "requestLogErrorTemplate": "none",
                "requestLogPool": "none",
                "requestLogProtocol": "mds-udp",
                "requestLogTemplate": "none",
                "requestLogging": "disabled",
                "responseLogErrorPool": "none",
                "responseLogErrorProtocol": "mds-udp",
                "responseLogErrorTemplate": "none",
                "responseLogPool": "none",
                "responseLogProtocol": "mds-udp",
                "responseLogTemplate": "none",
                "responseLogging": "disabled",
                "selfLink": "https://localhost/mgmt/tm/ltm/profile/request-log/~Common~request-log?ver=14.1.2.1",
            }
        ],
        "kind": "tm:ltm:profile:request-log:request-logcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/profile/request-log?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmProfileRequestlog(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmProfileRequestlog(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
