# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_auth_login_failures
from genie.libs.parser.bigip.get_auth_login_failures import AuthLoginfailures

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/auth/login-failures'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:auth:login-failures:login-failurescollectionstats",
            "selfLink": "https://localhost/mgmt/tm/auth/login-failures?ver=14.1.2.1",
            "entries": {
                "https://localhost/mgmt/tm/auth/login-failures/admin": {
                    "nestedStats": {
                        "kind": "tm:auth:login-failures:login-failuresstats",
                        "selfLink": "https://localhost/mgmt/tm/auth/login-failures/admin?ver=14.1.2.1",
                        "entries": {
                            "failTime": {"description": "None"},
                            "lockedOut": {"description": "no"},
                            "loginAttempts": {"value": 0},
                            "tty": {"description": " "},
                            "username": {"description": "admin"},
                        },
                    }
                },
                "https://localhost/mgmt/tm/auth/login-failures/f5hubblelcdadmin": {
                    "nestedStats": {
                        "kind": "tm:auth:login-failures:login-failuresstats",
                        "selfLink": "https://localhost/mgmt/tm/auth/login-failures/f5hubblelcdadmin?ver=14.1.2.1",
                        "entries": {
                            "failTime": {"description": "None"},
                            "lockedOut": {"description": "no"},
                            "loginAttempts": {"value": 0},
                            "tty": {"description": " "},
                            "username": {"description": "f5hubblelcdadmin"},
                        },
                    }
                },
                "https://localhost/mgmt/tm/auth/login-failures/root": {
                    "nestedStats": {
                        "kind": "tm:auth:login-failures:login-failuresstats",
                        "selfLink": "https://localhost/mgmt/tm/auth/login-failures/root?ver=14.1.2.1",
                        "entries": {
                            "failTime": {"description": "None"},
                            "lockedOut": {"description": "no"},
                            "loginAttempts": {"value": 0},
                            "tty": {"description": " "},
                            "username": {"description": "root"},
                        },
                    }
                },
            },
        }


class test_get_auth_login_failures(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "entries": {
            "https://localhost/mgmt/tm/auth/login-failures/admin": {
                "nestedStats": {
                    "entries": {
                        "failTime": {"description": "None"},
                        "lockedOut": {"description": "no"},
                        "loginAttempts": {"value": 0},
                        "tty": {"description": " "},
                        "username": {"description": "admin"},
                    },
                    "kind": "tm:auth:login-failures:login-failuresstats",
                    "selfLink": "https://localhost/mgmt/tm/auth/login-failures/admin?ver=14.1.2.1",
                }
            },
            "https://localhost/mgmt/tm/auth/login-failures/f5hubblelcdadmin": {
                "nestedStats": {
                    "entries": {
                        "failTime": {"description": "None"},
                        "lockedOut": {"description": "no"},
                        "loginAttempts": {"value": 0},
                        "tty": {"description": " "},
                        "username": {"description": "f5hubblelcdadmin"},
                    },
                    "kind": "tm:auth:login-failures:login-failuresstats",
                    "selfLink": "https://localhost/mgmt/tm/auth/login-failures/f5hubblelcdadmin?ver=14.1.2.1",
                }
            },
            "https://localhost/mgmt/tm/auth/login-failures/root": {
                "nestedStats": {
                    "entries": {
                        "failTime": {"description": "None"},
                        "lockedOut": {"description": "no"},
                        "loginAttempts": {"value": 0},
                        "tty": {"description": " "},
                        "username": {"description": "root"},
                    },
                    "kind": "tm:auth:login-failures:login-failuresstats",
                    "selfLink": "https://localhost/mgmt/tm/auth/login-failures/root?ver=14.1.2.1",
                }
            },
        },
        "kind": "tm:auth:login-failures:login-failurescollectionstats",
        "selfLink": "https://localhost/mgmt/tm/auth/login-failures?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = AuthLoginfailures(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = AuthLoginfailures(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
