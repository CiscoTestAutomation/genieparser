# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_cli_version
from genie.libs.parser.bigip.get_cli_version import CliVersion

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/cli/version'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:cli:version:versionstats",
            "selfLink": "https://localhost/mgmt/tm/cli/version?ver=14.1.2.1",
            "entries": {
                "https://localhost/mgmt/tm/cli/version/0": {
                    "nestedStats": {
                        "entries": {
                            "active": {"description": "14.1.2.1"},
                            "latest": {"description": "14.1.2.1"},
                            "supported": {
                                "description": "{ 11.5.0 11.5.1 11.5.2 11.5.3 11.5.4 11.5.5 11.6.0 11.6.1 11.6.2 11.6.3 12.0.0 12.1.0 12.1.1 12.1.2 12.1.3 12.1.3.1 13.0.0 13.0.1 13.1.0 13.1.1 14.0.0 14.1.0 14.1.1 14.1.2 14.1.2.1 }"
                            },
                        }
                    }
                }
            },
        }


class test_get_cli_version(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "entries": {
            "https://localhost/mgmt/tm/cli/version/0": {
                "nestedStats": {
                    "entries": {
                        "active": {"description": "14.1.2.1"},
                        "latest": {"description": "14.1.2.1"},
                        "supported": {
                            "description": "{ "
                            "11.5.0 "
                            "11.5.1 "
                            "11.5.2 "
                            "11.5.3 "
                            "11.5.4 "
                            "11.5.5 "
                            "11.6.0 "
                            "11.6.1 "
                            "11.6.2 "
                            "11.6.3 "
                            "12.0.0 "
                            "12.1.0 "
                            "12.1.1 "
                            "12.1.2 "
                            "12.1.3 "
                            "12.1.3.1 "
                            "13.0.0 "
                            "13.0.1 "
                            "13.1.0 "
                            "13.1.1 "
                            "14.0.0 "
                            "14.1.0 "
                            "14.1.1 "
                            "14.1.2 "
                            "14.1.2.1 "
                            "}"
                        },
                    }
                }
            }
        },
        "kind": "tm:cli:version:versionstats",
        "selfLink": "https://localhost/mgmt/tm/cli/version?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = CliVersion(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = CliVersion(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
