# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_gtm_persist
from genie.libs.parser.bigip.get_gtm_persist import GtmPersist

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/gtm/persist'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:gtm:persist:persiststats",
            "selfLink": "https://localhost/mgmt/tm/gtm/persist?ver=14.1.2.1",
            "apiRawValues": {
                "apiAnonymous": "Total persistence records returned: 0\n"
            },
        }


class test_get_gtm_persist(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "apiRawValues": {
            "apiAnonymous": "Total persistence records returned: 0\n"
        },
        "kind": "tm:gtm:persist:persiststats",
        "selfLink": "https://localhost/mgmt/tm/gtm/persist?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = GtmPersist(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = GtmPersist(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
