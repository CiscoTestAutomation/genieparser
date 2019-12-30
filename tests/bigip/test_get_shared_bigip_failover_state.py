# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_shared_bigip_failover_state
from genie.libs.parser.bigip.get_shared_bigip_failover_state import (
    SharedBigipfailoverstate,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/shared/bigip-failover-state'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "isEnabled": True,
            "pollCyclePeriodMillis": 3600000,
            "nextPollTime": "2019-12-30T09:25:10.285-0800",
            "failoverState": "active",
            "generation": 0,
            "lastUpdateMicros": 0,
        }


class test_get_shared_bigip_failover_state(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "failoverState": "active",
        "generation": 0,
        "isEnabled": True,
        "lastUpdateMicros": 0,
        "nextPollTime": "2019-12-30T09:25:10.285-0800",
        "pollCyclePeriodMillis": 3600000,
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SharedBigipfailoverstate(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SharedBigipfailoverstate(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
