# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# Parser
from genie.libs.parser.nxos.show_virtual_service import (
    ShowVirtualServiceGlobal,
    ShowVirtualServiceList,
    ShowVirtualServiceCore,
    ShowVirtualServiceDetail,
    ShowGuestshell,
    ShowVirtualServiceUtilization,
)


# ===========================================
# Unit test for "show virtual-service global"
# ===========================================
class test_show_virtual_service_global(unittest.TestCase):
    """Unit test for "show virtual-service global"."""

    empty_output = {'execute.return_value': """

    """}

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

    def test_show_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowVirtualServiceGlobal(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

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


# =======================================================
# Unit test for "show virtual-service core [name <name>]"
# =======================================================
class test_show_virtual_service_core(unittest.TestCase):
    """Unit test for "show virtual-service core [name <name>]."""

    empty_output = {'execute.return_value': """

    Virtual-Service  Process-name  PID       Date(Year-Month-Day Time)
    ---------------  ------------  --------  -------------------------
    """}

    golden_output_1 = {'execute.return_value': """

    Virtual-Service  Process-name  PID       Date(Year-Month-Day Time)
    ---------------  ------------  --------  -------------------------
    guestshell+      sleep         266       2019-05-30 19:53:28
    """}

    golden_parsed_output_1 = {
        'cores': {
            1: {
                'virtual_service': 'guestshell+',
                'process_name': 'sleep',
                'pid': 266,
                'date': '2019-05-30 19:53:28',
            },
        }
    }

    def test_show_virtual_service_core_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowVirtualServiceCore(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

        obj = ShowVirtualServiceCore(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(name="guestshell+")

    def test_show_virtual_service_core(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowVirtualServiceCore(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

        obj = ShowVirtualServiceCore(device=self.device)
        parsed_output = obj.parse(name="guestshell+")
        self.assertEqual(parsed_output, self.golden_parsed_output_1)



# ===========================================
# Unit test for "show virtual-service detail"
# ===========================================
class test_show_virtual_service_detail(unittest.TestCase):
    """Unit test for "show virtual-service detail"."""

    empty_output = {'execute.return_value': """

    """}

    golden_output_1 = {'execute.return_value': """
Virtual service lxc_9 detail
  State                 : Not Installed
  Package information
    Name                : None
    Path                : Not Available
    Application
      Name              : None
      Installed version : None
      Description       : None
    Signing
      Key type          : Unsigned
      Method            : None
    Licensing
      Name              : None
      Version           : None
  Resource reservation
    Disk                : 0 MB
    Memory              : 0 MB
    CPU                 : 0% system CPU
"""}

    golden_parsed_output_1 = {
        'service': {
            'lxc_9': {
                'state': 'not installed',
                'package_information': {
                    'name': 'None',
                    'path': 'Not Available',
                    'application': {
                        'name': 'None',
                        'version': 'None',
                        'description': 'None',
                    },
                    'signing': {
                        'key_type': 'Unsigned',
                        'method': 'None',
                    },
                    'licensing': {
                        'name': 'None',
                        'version': 'None',
                    },
                },
                'resource_reservation': {
                    'disk_mb': 0,
                    'memory_mb': 0,
                    'cpu_percent': 0,
                },
            },
        },
    }

    golden_output_2 = {'execute.return_value': """
Virtual service lxc_8 detail
  State                 : Installed
  Package information
    Name                : c7ulxc_kstack.ova
    Path                : bootflash:/c7ulxc_kstack.ova
    Application
      Name              : Centos7Kstack
      Installed version : 1.0; (devtest)
      Description       : centos distro (kstack)
    Signing
      Key type          : Cisco development key
      Method            : SHA-1
    Licensing
      Name              : None
      Version           : None
  Resource reservation
    Disk                : 126 MB
    Memory              : 0 MB
    CPU                 : 0% system CPU

  Attached devices
    Type              Name        Alias
    ---------------------------------------------
    Disk              _rootfs
    Disk              /var/sysmgr/tmp
    Serial/shell
    Serial/aux
    Serial/Syslog                 serial2
    Serial/Trace                  serial3
"""}

    golden_parsed_output_2 = {
        'service': {
            'lxc_8': {
                'state': 'installed',
                'package_information': {
                    'name': 'c7ulxc_kstack.ova',
                    'path': 'bootflash:/c7ulxc_kstack.ova',
                    'application': {
                        'name': 'Centos7Kstack',
                        'version': '1.0; (devtest)',
                        'description': 'centos distro (kstack)',
                    },
                    'signing': {
                        'key_type': 'Cisco development key',
                        'method': 'SHA-1',
                    },
                    'licensing': {
                        'name': 'None',
                        'version': 'None',
                    },
                },
                'resource_reservation': {
                    'disk_mb': 126,
                    'memory_mb': 0,
                    'cpu_percent': 0,
                },
                'attached_devices': {
                    1: {
                        'type': 'Disk',
                        'name': '_rootfs',
                    },
                    2: {
                        'type': 'Disk',
                        'name': '/var/sysmgr/tmp',
                    },
                    3: {
                        'type': 'Serial/shell',
                    },
                    4: {
                        'type': 'Serial/aux',
                    },
                    5: {
                        'type': 'Serial/Syslog',
                        'alias': 'serial2',
                    },
                    6: {
                        'type': 'Serial/Trace',
                        'alias': 'serial3',
                    },
                },
            },
        },
    }

    golden_output_3 = {'execute.return_value': """
Virtual service watchdog_lxc detail
  State                 : Activated
  Package information
    Name                : ft_mv_no_onep.ova
    Path                : bootflash:/ft_mv_no_onep.ova
    Application
      Name              : TestingApp
      Installed version : 45.67.A.01
      Description       : Testing Application Suite
    Signing
      Key type          : Cisco development key
      Method            : SHA-1
    Licensing
      Name              : None
      Version           : None
  Resource reservation
    Disk                : 87 MB
    Memory              : 256 MB
    CPU                 : 1% system CPU

  Attached devices
    Type              Name        Alias
    ---------------------------------------------
    Disk              _rootfs
    Disk              /mnt/data_disk
    Disk              /var/sysmgr/tmp
    Disk              /mnt/config_disk
    Serial/shell
    Serial/aux
    Serial/Syslog                 serial2
    Serial/Trace                  serial3
    Watchdog
"""}

    golden_parsed_output_3 = {
        'service': {
            'watchdog_lxc': {
                'state': 'activated',
                'package_information': {
                    'name': 'ft_mv_no_onep.ova',
                    'path': 'bootflash:/ft_mv_no_onep.ova',
                    'application': {
                        'name': 'TestingApp',
                        'version': '45.67.A.01',
                        'description': 'Testing Application Suite',
                    },
                    'signing': {
                        'key_type': 'Cisco development key',
                        'method': 'SHA-1'
                    },
                    'licensing': {
                        'name': 'None',
                        'version': 'None',
                    },
                },
                'resource_reservation': {
                    'disk_mb': 87,
                    'memory_mb': 256,
                    'cpu_percent': 1,
                },
                'attached_devices': {
                    1: {
                        'type': 'Disk',
                        'name': '_rootfs',
                    },
                    2: {
                        'type': 'Disk',
                        'name': '/mnt/data_disk',
                    },
                    3: {
                        'type': 'Disk',
                        'name': '/var/sysmgr/tmp',
                    },
                    4: {
                        'type': 'Disk',
                        'name': '/mnt/config_disk',
                    },
                    5: {
                        'type': 'Serial/shell',
                    },
                    6: {
                        'type': 'Serial/aux',
                    },
                    7: {
                        'type': 'Serial/Syslog',
                        'alias': 'serial2',
                    },
                    8: {
                        'type': 'Serial/Trace',
                        'alias': 'serial3',
                    },
                    9: {
                        'type': 'Watchdog',
                    },
                },
            }
        }
    }

    def test_show_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowVirtualServiceDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowVirtualServiceDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

    def test_show_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        obj = ShowVirtualServiceDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

    def test_show_3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_3)
        obj = ShowVirtualServiceDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_3)


# ===============================
# Unit test for "show guestshell"
# ===============================
class test_show_guestshell(unittest.TestCase):
    """Unit test for "show guestshell"."""

    empty_output = {'execute.return_value': """

    """}

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

    golden_parsed_output_1 = {
        'state': 'activated',
        'package_information': {
            'name': 'guestshell.ova',
            'path': '/isanboot/bin/guestshell.ova',
            'application': {
                'name': 'GuestShell',
                'version': '2.4(0.0)',
                'description': 'Cisco Systems Guest Shell',
            },
            'signing': {
                'key_type': 'Cisco release key',
                'method': 'SHA-1'
            },
            'licensing': {
                'name': 'None',
                'version': 'None',
            },
        },
        'resource_reservation': {
            'disk_mb': 1000,
            'memory_mb': 500,
            'cpu_percent': 1,
        },
        'attached_devices': {
            1: {
                'type': 'Disk',
                'name': '_rootfs',
            },
            2: {
                'type': 'Disk',
                'name': '/cisco/cor',
            },
            3: {
                'type': 'Serial/shell',
            },
            4: {
                'type': 'Serial/aux',
            },
            5: {
                'type': 'Serial/Syslog',
                'alias': 'serial2',
            },
            6: {
                'type': 'Serial/Trace',
                'alias': 'serial3',
            },
        }
    }

    def test_show_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowGuestshell(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowGuestshell(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)


# ============================================================
# Unit test for "show virtual-service utilization name <name>"
# ============================================================
class test_show_virtual_service_utilization(unittest.TestCase):
    """Unit test for "show virtual-service utilization name <name>"."""

    empty_output = {'execute.return_value': """
    """}

    golden_output_1 = {'execute.return_value': """
	Virtual-Service Utilization:

	CPU Utilization:
	  Requested Application Utilization:  1 %
	  Actual Application Utilization:  0 % (30 second average)
	  CPU State: R : Running

	Memory Utilization:
	  Memory Allocation: 262144 KB
	  Memory Used:       13400 KB

	Storage Utilization:
	  Name: _rootfs, Alias:
	    Capacity(1K blocks):  243823      Used(1K blocks): 161690
	    Available(1K blocks): 77537       Usage: 68 %

	  Name: /cisco/core, Alias:
	    Capacity(1K blocks):  2097152     Used(1K blocks): 62216
	    Available(1K blocks): 2034936     Usage: 3  %
    """}

    golden_parsed_output_1 = {
        'cpu': {
            'requested_percent': 1,
            'actual_percent': 0,
            'state_abbrev': "R",
            'state': "Running",
        },
        'memory': {
            'allocation_kb': 262144,
            'used_kb': 13400,
        },
        'storage': {
            "_rootfs": {
                'capacity_kb': 243823,
                'used_kb': 161690,
                'available_kb': 77537,
                'used_percent': 68,
            },
            "/cisco/core": {
                'capacity_kb': 2097152,
                'used_kb': 62216,
                'available_kb': 2034936,
                'used_percent': 3,
            },
        },
    }

    def test_show_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowVirtualServiceUtilization(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(name="guestshell+")

    def test_show_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowVirtualServiceUtilization(device=self.device)
        parsed_output = obj.parse(name="guestshell+")
        self.assertEqual(parsed_output, self.golden_parsed_output_1)


if __name__ == "__main__":
    unittest.main()
