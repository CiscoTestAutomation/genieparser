# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_auth_remote_user
from genie.libs.parser.bigip.get_auth_remote_user import AuthRemoteuser

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/auth/remote-user'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:auth:remote-user:remote-userstate",
            "selfLink": "https://localhost/mgmt/tm/auth/remote-user?ver=14.1.2.1",
            "defaultPartition": "all",
            "defaultPartitionReference": {
                "link": "https://localhost/mgmt/tm/auth/partition/all?ver=14.1.2.1"
            },
            "defaultRole": "no-access",
            "remoteConsoleAccess": "disabled",
        }


class test_get_auth_remote_user(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "defaultPartition": "all",
        "defaultPartitionReference": {
            "link": "https://localhost/mgmt/tm/auth/partition/all?ver=14.1.2.1"
        },
        "defaultRole": "no-access",
        "kind": "tm:auth:remote-user:remote-userstate",
        "remoteConsoleAccess": "disabled",
        "selfLink": "https://localhost/mgmt/tm/auth/remote-user?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = AuthRemoteuser(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = AuthRemoteuser(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
