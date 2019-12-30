# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_diagsihealth_request
from genie.libs.parser.bigip.get_sys_diagsihealth_request import (
    SysDiagsIhealthrequest,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/diags/ihealth-request'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:diags:ihealth-request:ihealth-requeststate",
            "selfLink": "https://localhost/mgmt/tm/sys/diags/ihealth-request?ver=14.1.2.1",
            "error": "none",
            "ihealthFinishTime": 0,
            "ihealthStartTime": 0,
            "progress": 0,
            "qkProgress": 0,
            "qkviewDate": 0,
            "qkviewSize": 0,
            "status": "none",
            "tcpdumpDate": 0,
            "tcpdumpSize": 0,
            "type": "none",
        }


class test_get_sys_diagsihealth_request(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "error": "none",
        "ihealthFinishTime": 0,
        "ihealthStartTime": 0,
        "kind": "tm:sys:diags:ihealth-request:ihealth-requeststate",
        "progress": 0,
        "qkProgress": 0,
        "qkviewDate": 0,
        "qkviewSize": 0,
        "selfLink": "https://localhost/mgmt/tm/sys/diags/ihealth-request?ver=14.1.2.1",
        "status": "none",
        "tcpdumpDate": 0,
        "tcpdumpSize": 0,
        "type": "none",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysDiagsIhealthrequest(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysDiagsIhealthrequest(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
