# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_auth_user
from genie.libs.parser.bigip.get_auth_user import AuthUser

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/auth/user'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:auth:user:usercollectionstate",
            "selfLink": "https://localhost/mgmt/tm/auth/user?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:auth:user:userstate",
                    "name": "admin",
                    "fullPath": "admin",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/auth/user/admin?ver=14.1.2.1",
                    "description": "Admin User",
                    "encryptedPassword": "$6$B3tava7B$dqnf1qofV3VG0eKhxvl2qENKMrBFYGWZqancenABXkRyVmR8hpqJpz8SlVcs/VeqKh3ww0dM3N7r371v4cFrs1",
                    "partitionAccess": [
                        {
                            "name": "all-partitions",
                            "role": "admin",
                            "nameReference": {
                                "link": "https://localhost/mgmt/tm/auth/partition/all-partitions?ver=14.1.2.1"
                            },
                        }
                    ],
                }
            ],
        }


class test_get_auth_user(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "description": "Admin User",
                "encryptedPassword": "$6$B3tava7B$dqnf1qofV3VG0eKhxvl2qENKMrBFYGWZqancenABXkRyVmR8hpqJpz8SlVcs/VeqKh3ww0dM3N7r371v4cFrs1",
                "fullPath": "admin",
                "generation": 1,
                "kind": "tm:auth:user:userstate",
                "name": "admin",
                "partitionAccess": [
                    {
                        "name": "all-partitions",
                        "nameReference": {
                            "link": "https://localhost/mgmt/tm/auth/partition/all-partitions?ver=14.1.2.1"
                        },
                        "role": "admin",
                    }
                ],
                "selfLink": "https://localhost/mgmt/tm/auth/user/admin?ver=14.1.2.1",
            }
        ],
        "kind": "tm:auth:user:usercollectionstate",
        "selfLink": "https://localhost/mgmt/tm/auth/user?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = AuthUser(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = AuthUser(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
