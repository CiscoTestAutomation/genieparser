# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_filessl_csr
from genie.libs.parser.bigip.get_sys_filessl_csr import SysFileSslcsr

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/file/ssl-csr'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:file:ssl-csr:ssl-csrcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/sys/file/ssl-csr?ver=14.1.2.1",
            "items": [],
        }


class test_get_sys_filessl_csr(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [],
        "kind": "tm:sys:file:ssl-csr:ssl-csrcollectionstate",
        "selfLink": "https://localhost/mgmt/tm/sys/file/ssl-csr?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysFileSslcsr(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysFileSslcsr(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
