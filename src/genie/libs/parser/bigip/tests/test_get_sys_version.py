# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_version
from genie.libs.parser.bigip.get_sys_version import SysVersion

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/version'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:version:versionstats",
            "selfLink": "https://localhost/mgmt/tm/sys/version?ver=14.1.2.1",
            "entries": {
                "https://localhost/mgmt/tm/sys/version/0": {
                    "nestedStats": {
                        "entries": {
                            "Build": {"description": "0.0.4"},
                            "Date": {
                                "description": "Tue Sep 17 15:44:32 PDT 2019"
                            },
                            "Edition": {"description": "Point Release 1"},
                            "Product": {"description": "BIG-IP"},
                            "Title": {"description": "Main Package"},
                            "Version": {"description": "14.1.2.1"},
                        }
                    }
                }
            },
        }


class test_get_sys_version(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "entries": {
            "https://localhost/mgmt/tm/sys/version/0": {
                "nestedStats": {
                    "entries": {
                        "Build": {"description": "0.0.4"},
                        "Date": {
                            "description": "Tue "
                            "Sep "
                            "17 "
                            "15:44:32 "
                            "PDT "
                            "2019"
                        },
                        "Edition": {"description": "Point " "Release " "1"},
                        "Product": {"description": "BIG-IP"},
                        "Title": {"description": "Main " "Package"},
                        "Version": {"description": "14.1.2.1"},
                    }
                }
            }
        },
        "kind": "tm:sys:version:versionstats",
        "selfLink": "https://localhost/mgmt/tm/sys/version?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysVersion(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysVersion(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
