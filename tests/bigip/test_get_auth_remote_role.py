# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_auth_remote_role
from genie.libs.parser.bigip.get_auth_remote_role import AuthRemoterole

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/auth/remote-role'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:auth:remote-role:remote-rolestate",
            "selfLink": "https://localhost/mgmt/tm/auth/remote-role?ver=14.1.2.1",
            "roleInfoReference": {
                "link": "https://localhost/mgmt/tm/auth/remote-role/role-info?ver=14.1.2.1",
                "isSubcollection": True,
            },
        }


class test_get_auth_remote_role(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "kind": "tm:auth:remote-role:remote-rolestate",
        "roleInfoReference": {
            "isSubcollection": True,
            "link": "https://localhost/mgmt/tm/auth/remote-role/role-info?ver=14.1.2.1",
        },
        "selfLink": "https://localhost/mgmt/tm/auth/remote-role?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = AuthRemoterole(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = AuthRemoterole(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
