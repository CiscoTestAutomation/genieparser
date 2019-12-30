# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_shared_sysbackup
from genie.libs.parser.bigip.get_shared_sysbackup import SharedSysBackup

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/shared/sys/backup'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "lastRestoreDateTime": "1969-12-31T16:00:00.000-0800",
            "items": [],
            "generation": 0,
            "lastUpdateMicros": 0,
            "kind": "tm:shared:sys:backup:ucsbackuptaskcollectionstate",
            "selfLink": "https://localhost/mgmt/tm/shared/sys/backup",
        }


class test_get_shared_sysbackup(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "generation": 0,
        "items": [],
        "kind": "tm:shared:sys:backup:ucsbackuptaskcollectionstate",
        "lastRestoreDateTime": "1969-12-31T16:00:00.000-0800",
        "lastUpdateMicros": 0,
        "selfLink": "https://localhost/mgmt/tm/shared/sys/backup",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SharedSysBackup(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SharedSysBackup(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
