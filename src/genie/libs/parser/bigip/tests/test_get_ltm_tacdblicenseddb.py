# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_tacdblicenseddb
from genie.libs.parser.bigip.get_ltm_tacdblicenseddb import LtmTacdbLicenseddb

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/tacdb/licenseddb'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:tacdb:licenseddb:licenseddbcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/tacdb/licenseddb?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:tacdb:licenseddb:licenseddbstate",
                    "name": "licensed-tacdb",
                    "partition": "Common",
                    "fullPath": "/Common/licensed-tacdb",
                    "generation": 0,
                    "selfLink": "https://localhost/mgmt/tm/ltm/tacdb/licenseddb/~Common~licensed-tacdb?ver=14.1.2.1",
                    "lastSyncDatetime": "1970-01-01T00:00:00Z",
                    "pollInterval": "0",
                    "progressStatus": "not-loaded",
                }
            ],
        }


class test_get_ltm_tacdblicenseddb(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "fullPath": "/Common/licensed-tacdb",
                "generation": 0,
                "kind": "tm:ltm:tacdb:licenseddb:licenseddbstate",
                "lastSyncDatetime": "1970-01-01T00:00:00Z",
                "name": "licensed-tacdb",
                "partition": "Common",
                "pollInterval": "0",
                "progressStatus": "not-loaded",
                "selfLink": "https://localhost/mgmt/tm/ltm/tacdb/licenseddb/~Common~licensed-tacdb?ver=14.1.2.1",
            }
        ],
        "kind": "tm:ltm:tacdb:licenseddb:licenseddbcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/tacdb/licenseddb?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmTacdbLicenseddb(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmTacdbLicenseddb(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
