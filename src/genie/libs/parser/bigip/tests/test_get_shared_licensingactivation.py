# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_shared_licensingactivation
from genie.libs.parser.bigip.get_shared_licensingactivation import (
    SharedLicensingActivation,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/shared/licensing/activation'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "status": "LICENSING_NO_DATA",
            "generation": 0,
            "lastUpdateMicros": 0,
            "kind": "tm:shared:licensing:activation:activatelicenseresponse",
            "selfLink": "https://localhost/mgmt/tm/shared/licensing/activation",
        }


class test_get_shared_licensingactivation(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "generation": 0,
        "kind": "tm:shared:licensing:activation:activatelicenseresponse",
        "lastUpdateMicros": 0,
        "selfLink": "https://localhost/mgmt/tm/shared/licensing/activation",
        "status": "LICENSING_NO_DATA",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SharedLicensingActivation(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SharedLicensingActivation(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
