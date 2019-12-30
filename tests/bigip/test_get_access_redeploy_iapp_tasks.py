# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_access_redeploy_iapp_tasks
from genie.libs.parser.bigip.get_access_redeploy_iapp_tasks import (
    AccessRedeployiapptasks,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/access/redeploy-iapp-tasks'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "items": [],
            "generation": 0,
            "kind": "tm:access:redeploy-iapp-tasks:iappbesteffortredeploytaskcollectionstate",
            "lastUpdateMicros": 0,
            "selfLink": "https://localhost/mgmt/tm/access/redeploy-iapp-tasks",
        }


class test_get_access_redeploy_iapp_tasks(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "generation": 0,
        "items": [],
        "kind": "tm:access:redeploy-iapp-tasks:iappbesteffortredeploytaskcollectionstate",
        "lastUpdateMicros": 0,
        "selfLink": "https://localhost/mgmt/tm/access/redeploy-iapp-tasks",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = AccessRedeployiapptasks(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = AccessRedeployiapptasks(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
