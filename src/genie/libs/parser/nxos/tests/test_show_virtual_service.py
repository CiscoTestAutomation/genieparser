# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# Parser
from genie.libs.parser.nxos.show_virtual_service import (
    ShowVirtualServiceGlobal,
    ShowVirtualServiceList,
    ShowVirtualServiceDetail,
    ShowGuestshell,
)

# ===========================================
# Unit test for "show virtual-service global"
# ===========================================
class test_show_virtual_service_global(unittest.TestCase):
    """Unit test for "show virtual-service global"."""

    golden_parsed_output = {
        'version': '1.10',
        'virtual_services': {
            'installed': 1,
            'activated': 1,
        },
        'machine_types': {
            'supported': ['LXC'],
            'disabled': ['KVM'],
        },
        'resource_limits': {
            'cpus_per_service': 1,
            'cpu': {
                'quota': 20,
                'committed': 1,
                'available': 19,
            },
            'memory': {
                'quota': 3840,
                'committed': 500,
                'available': 3340,
            },
            'bootflash': {
                'quota': 8192,
                'committed': 1000,
                'available': 7192,
            },
        },
    }

    golden_output = {'execute.return_value': """

        Virtual Service Global State and Virtualization Limits:

        Infrastructure version : 1.10
        Total virtual services installed : 1
        Total virtual services activated : 1

        Machine types supported   : LXC
        Machine types disabled    : KVM

        Maximum VCPUs per virtual service : 1

        Resource virtualization limits:
        Name                        Quota    Committed    Available
        -----------------------------------------------------------------------
        system CPU (%)                 20            1           19
        memory (MB)                  3840          500         3340
        bootflash (MB)               8192         1000         7192

    """}

    def test_show_virtual_service_global(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowVirtualServiceGlobal(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


# =========================================
# Unit test for "show virtual-service list"
# =========================================
class test_show_virtual_service_list(unittest.TestCase):
    """Unit test for "show virtual-service list"."""

    empty_output = {'execute.return_value': """


        Virtual Service List:


        """}

    golden_parsed_output = {
        'service': {
            "guestshell+": {
                'status': "activated",
                'package': "guestshell.ova",
            },
            "lxc4": {
                'status': "not installed",
            },
            "sc_sanity_03": {
                'status': "installed",
                'package': "ft_mv_no_onep.ova",
            },
            "lxc_upgrade": {
                'status': "activate failed",
                'package': "c63lxc_no_onep.ova",
            },
        },
    }

    golden_output = {'execute.return_value': """
        Virtual Service List:

        Name                    Status             Package Name
        ----------------------------------------------------------------------
        guestshell+             Activated          guestshell.ova
        lxc4                    Not Installed      Not Available
        sc_sanity_03            Installed          ft_mv_no_onep.ova
        lxc_upgrade             Activate Failed    c63lxc_no_onep.ova
        """}

    def test_show_virtual_service_list_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowVirtualServiceList(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_virtual_service_list(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowVirtualServiceList(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


# ===========================================
# Unit test for "show virtual-service detail"
# ===========================================
class test_show_virtual_service_detail(unittest.TestCase):
    """Unit test for "show virtual-service detail"."""

    empty_output = {'execute.return_value': """

    """}

    golden_parsed_output_1 = {
        'service': {
            'guestshell+': {
                'state': 'activated',
                'info': {
                    'package_location': '/isanboot/bin/guestshell.ova',
                    'version': '2.4(0.0)',
                    'description': 'Cisco Systems Guest Shell',
                    'signing_key_type': 'Cisco release key',
                },
                'resource_reservation': {
                    'disk_mb': 1000,
                    'memory_mb': 500,
                    'cpu_percent': 1,
                }
            }
        }
    }

    golden_output_1 = {'execute.return_value': """
        Virtual service guestshell+ detail
          State                 : Activated
          Package information
            Name                : guestshell.ova
            Path                : /isanboot/bin/guestshell.ova
            Application
              Name              : GuestShell
              Installed version : 2.4(0.0)
              Description       : Cisco Systems Guest Shell
            Signing
              Key type          : Cisco release key
              Method            : SHA-1
            Licensing
              Name              : None
              Version           : None
          Resource reservation
            Disk                : 1000 MB
            Memory              : 500 MB
            CPU                 : 1% system CPU

          Attached devices
            Type              Name        Alias
            ---------------------------------------------
            Disk              _rootfs
            Disk              /cisco/cor
            Serial/shell
            Serial/aux
            Serial/Syslog                 serial2
            Serial/Trace                  serial3
    """}

    my_test_class = ShowVirtualServiceDetail

    def test_show_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = self.my_test_class(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = self.my_test_class(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)


# ===============================
# Unit test for "show guestshell"
# ===============================
class test_show_guestshell(test_show_virtual_service_detail):
    """Unit test for "show guestshell"."""

    golden_parsed_output_1 = {
        'state': 'activated',
        'info': {
            'package_location': '/isanboot/bin/guestshell.ova',
            'version': '2.4(0.0)',
            'description': 'Cisco Systems Guest Shell',
            'signing_key_type': 'Cisco release key',
        },
        'resource_reservation': {
            'disk_mb': 1000,
            'memory_mb': 500,
            'cpu_percent': 1,
        }
    }

    my_test_class = ShowGuestshell


if __name__ == "__main__":
    unittest.main()
