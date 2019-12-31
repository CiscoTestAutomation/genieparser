# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_tacdb
from genie.libs.parser.bigip.get_ltm_tacdb import LtmTacdb

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/tacdb'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:tacdb:tacdbcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/tacdb?ver=14.1.2.1",
            "items": [
                {
                    "reference": {
                        "link": "https://localhost/mgmt/tm/ltm/tacdb/customdb?ver=14.1.2.1"
                    }
                },
                {
                    "reference": {
                        "link": "https://localhost/mgmt/tm/ltm/tacdb/customdb-file?ver=14.1.2.1"
                    }
                },
            ],
        }


class test_get_ltm_tacdb(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "reference": {
                    "link": "https://localhost/mgmt/tm/ltm/tacdb/customdb?ver=14.1.2.1"
                }
            },
            {
                "reference": {
                    "link": "https://localhost/mgmt/tm/ltm/tacdb/customdb-file?ver=14.1.2.1"
                }
            },
        ],
        "kind": "tm:ltm:tacdb:tacdbcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/tacdb?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmTacdb(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmTacdb(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
