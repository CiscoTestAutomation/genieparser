# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_snmp
from genie.libs.parser.bigip.get_sys_snmp import SysSnmp

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/snmp'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:snmp:snmpstate",
            "selfLink": "https://localhost/mgmt/tm/sys/snmp?ver=14.1.2.1",
            "agentAddresses": ["tcp6:161", "udp6:161"],
            "agentTrap": "enabled",
            "allowedAddresses": ["127.0.0.0/8"],
            "authTrap": "disabled",
            "bigipTraps": "enabled",
            "loadMax1": 12,
            "loadMax15": 12,
            "loadMax5": 12,
            "snmpv1": "enable",
            "snmpv2c": "enable",
            "sysContact": "Customer Name <admin@customer.com>",
            "sysLocation": "Network Closet 1",
            "sysServices": 78,
            "trapCommunity": "public",
            "trapSource": "none",
            "communitiesReference": {
                "link": "https://localhost/mgmt/tm/sys/snmp/communities?ver=14.1.2.1",
                "isSubcollection": True,
            },
            "diskMonitors": [
                {
                    "name": "/Common/root",
                    "minspace": 2000,
                    "minspaceType": "size",
                    "path": "/",
                },
                {
                    "name": "/Common/var",
                    "minspace": 10000,
                    "minspaceType": "size",
                    "path": "/var",
                },
            ],
            "processMonitors": [
                {
                    "name": "/Common/bigd",
                    "maxProcesses": "infinity",
                    "minProcesses": 1,
                    "process": "bigd",
                },
                {
                    "name": "/Common/chmand",
                    "maxProcesses": "1",
                    "minProcesses": 1,
                    "process": "chmand",
                },
                {
                    "name": "/Common/httpd",
                    "maxProcesses": "infinity",
                    "minProcesses": 1,
                    "process": "httpd",
                },
                {
                    "name": "/Common/mcpd",
                    "maxProcesses": "1",
                    "minProcesses": 1,
                    "process": "mcpd",
                },
                {
                    "name": "/Common/sod",
                    "maxProcesses": "1",
                    "minProcesses": 1,
                    "process": "sod",
                },
                {
                    "name": "/Common/tmm",
                    "maxProcesses": "infinity",
                    "minProcesses": 1,
                    "process": "tmm",
                },
            ],
            "trapsReference": {
                "link": "https://localhost/mgmt/tm/sys/snmp/traps?ver=14.1.2.1",
                "isSubcollection": True,
            },
            "usersReference": {
                "link": "https://localhost/mgmt/tm/sys/snmp/users?ver=14.1.2.1",
                "isSubcollection": True,
            },
        }


class test_get_sys_snmp(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "agentAddresses": ["tcp6:161", "udp6:161"],
        "agentTrap": "enabled",
        "allowedAddresses": ["127.0.0.0/8"],
        "authTrap": "disabled",
        "bigipTraps": "enabled",
        "communitiesReference": {
            "isSubcollection": True,
            "link": "https://localhost/mgmt/tm/sys/snmp/communities?ver=14.1.2.1",
        },
        "diskMonitors": [
            {
                "minspace": 2000,
                "minspaceType": "size",
                "name": "/Common/root",
                "path": "/",
            },
            {
                "minspace": 10000,
                "minspaceType": "size",
                "name": "/Common/var",
                "path": "/var",
            },
        ],
        "kind": "tm:sys:snmp:snmpstate",
        "loadMax1": 12,
        "loadMax15": 12,
        "loadMax5": 12,
        "processMonitors": [
            {
                "maxProcesses": "infinity",
                "minProcesses": 1,
                "name": "/Common/bigd",
                "process": "bigd",
            },
            {
                "maxProcesses": "1",
                "minProcesses": 1,
                "name": "/Common/chmand",
                "process": "chmand",
            },
            {
                "maxProcesses": "infinity",
                "minProcesses": 1,
                "name": "/Common/httpd",
                "process": "httpd",
            },
            {
                "maxProcesses": "1",
                "minProcesses": 1,
                "name": "/Common/mcpd",
                "process": "mcpd",
            },
            {
                "maxProcesses": "1",
                "minProcesses": 1,
                "name": "/Common/sod",
                "process": "sod",
            },
            {
                "maxProcesses": "infinity",
                "minProcesses": 1,
                "name": "/Common/tmm",
                "process": "tmm",
            },
        ],
        "selfLink": "https://localhost/mgmt/tm/sys/snmp?ver=14.1.2.1",
        "snmpv1": "enable",
        "snmpv2c": "enable",
        "sysContact": "Customer Name <admin@customer.com>",
        "sysLocation": "Network Closet 1",
        "sysServices": 78,
        "trapCommunity": "public",
        "trapSource": "none",
        "trapsReference": {
            "isSubcollection": True,
            "link": "https://localhost/mgmt/tm/sys/snmp/traps?ver=14.1.2.1",
        },
        "usersReference": {
            "isSubcollection": True,
            "link": "https://localhost/mgmt/tm/sys/snmp/users?ver=14.1.2.1",
        },
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysSnmp(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysSnmp(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
