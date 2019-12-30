# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_management_ovsdb
from genie.libs.parser.bigip.get_sys_management_ovsdb import SysManagementovsdb

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/management-ovsdb'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:management-ovsdb:management-ovsdbstate",
            "selfLink": "https://localhost/mgmt/tm/sys/management-ovsdb?ver=14.1.2.1",
            "bfdDisabled": True,
            "disabled": True,
            "floodingType": "replicator",
            "logLevel": "info",
            "logicalRoutingType": "none",
            "port": 6640,
            "tunnelLocalAddress": "any6",
            "tunnelMaintenanceMode": "active",
        }


class test_get_sys_management_ovsdb(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "bfdDisabled": True,
        "disabled": True,
        "floodingType": "replicator",
        "kind": "tm:sys:management-ovsdb:management-ovsdbstate",
        "logLevel": "info",
        "logicalRoutingType": "none",
        "port": 6640,
        "selfLink": "https://localhost/mgmt/tm/sys/management-ovsdb?ver=14.1.2.1",
        "tunnelLocalAddress": "any6",
        "tunnelMaintenanceMode": "active",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysManagementovsdb(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysManagementovsdb(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
