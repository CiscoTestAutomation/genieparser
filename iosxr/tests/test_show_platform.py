# Python
import re
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Parser
from parser.iosxr.show_platform import ShowVersion, ShowSdrDetail,\
                                ShowPlatform, ShowPlatformVm,\
                                ShowInstallActiveSummary, ShowInventory,\
                                ShowRedundancySummary, AdminShowDiagChassis,\
                                ShowRedundancy

# Metaparser
from metaparser.util.exceptions import SchemaEmptyParserError

# ==============================
#  Unit test for 'show version'       
# ==============================

class test_show_version(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'chassis_detail': 'ASR 9006 4 Line Card Slot Chassis with V2 AC PEM',
        'config_register': '0x1922',
        'image': 'disk0:asr9k-os-mbi-6.1.4.10I/0x100305/mbiasr9k-rsp3.vm',
        'main_mem': 'cisco ASR9K Series (Intel 686 F6M14S4) processor with 6291456K '
                    'bytes of memory.',
        'operating_system': 'IOSXR',
        'processor': 'Intel 686 F6M14S4',
        'processor_memory_bytes': '6291456K',
        'device_family': 'ASR9K',
        'rp_config_register': '0x1922',
        'software_version': '6.1.4.10I',
        'uptime': '5 hours, 14 minutes'}

    golden_output1 = {'execute.return_value': '''
        Cisco IOS XR Software, Version 6.1.4.10I[Default]
        Copyright (c) 2017 by Cisco Systems, Inc.

        ROM: System Bootstrap, Version 0.75(c) 1994-2012 by Cisco Systems,  Inc.

        PE1 uptime is 5 hours, 14 minutes
        System image file is "disk0:asr9k-os-mbi-6.1.4.10I/0x100305/mbiasr9k-rsp3.vm"

        cisco ASR9K Series (Intel 686 F6M14S4) processor with 6291456K bytes of memory.
        Intel 686 F6M14S4 processor at 2134MHz, Revision 2.174
        ASR 9006 4 Line Card Slot Chassis with V2 AC PEM

        2 FastEthernet
        4 Management Ethernet
        20 GigabitEthernet
        503k bytes of non-volatile configuration memory.
        6271M bytes of hard disk.
        12510192k bytes of disk0: (Sector size 512 bytes).
        12510192k bytes of disk1: (Sector size 512 bytes).

        Configuration register on node 0/RSP0/CPU0 is 0x1922
        Boot device on node 0/RSP0/CPU0 is disk0:
        Package active on node 0/RSP0/CPU0:
        '''}

    golden_parsed_output2 = {
        'chassis_detail': 'IOS XRv Chassis',
        'config_register': '0x1',
        'image': 'bootflash:disk0/xrvr-os-mbi-6.2.1.23I/mbixrvr-rp.vm',
        'main_mem': 'cisco IOS XRv Series (Pentium Celeron Stepping 3) processor '
                    'with 4193911K bytes of memory.',
        'operating_system': 'IOSXR',
        'processor': 'Pentium Celeron Stepping 3',
        'processor_memory_bytes': '4193911K',
        'device_family': 'IOS XRv',
        'rp_config_register': '0x1',
        'software_version': '6.2.1.23I',
        'uptime': '5 days, 25 minutes'}

    golden_output2 = {'execute.return_value': '''
        Cisco IOS XR Software, Version 6.2.1.23I[Default]
        Copyright (c) 2016 by Cisco Systems, Inc.

        ROM: GRUB, Version 1.99(0), DEV RELEASE

        iosxrvuut uptime is 5 days, 25 minutes
        System image file is "bootflash:disk0/xrvr-os-mbi-6.2.1.23I/mbixrvr-rp.vm"

        cisco IOS XRv Series (Pentium Celeron Stepping 3) processor with 4193911K bytes of memory.
        Pentium Celeron Stepping 3 processor at 2931MHz, Revision 2.174
        IOS XRv Chassis

        1 Management Ethernet
        7 GigabitEthernet
        97070k bytes of non-volatile configuration memory.
        866M bytes of hard disk.
        2321392k bytes of disk0: (Sector size 512 bytes).

        Configuration register on node 0/0/CPU0 is 0x1
        Boot device on node 0/0/CPU0 is disk0:
        Package active on node 0/0/CPU0:
        '''}

    golden_parsed_output3 = {
        'operating_system': 'IOSXR',
        'device_family': 'IOS-XRv 9000',
        'software_version': '6.3.1.15I',
        'uptime': '1 week, 1 day, 5 hours, 47 minutes'}

    golden_output3 = {'execute.return_value': '''
        Cisco IOS XR Software, Version 6.3.1.15I
        Copyright (c) 2013-2017 by Cisco Systems, Inc.

        Build Information:
         Built By     : nkhai
         Built On     : Tue Apr 18 04:03:44 PDT 2017
         Build Host   : iox-ucs-012
         Workspace    : /auto/iox-ucs-012-san1/nightly_xr-dev/170418A_xrv9k/ws
         Version      : 6.3.1.15I
         Location     : /opt/cisco/XR/packages/

        cisco IOS-XRv 9000 () processor 
        System uptime is 1 week, 1 day, 5 hours, 47 minutes
        '''}

    def test_show_version_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        show_version_obj1 = ShowVersion(device=self.device)
        parsed_output1 = show_version_obj1.parse()
        self.assertEqual(parsed_output1,self.golden_parsed_output1)

    def test_show_version_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        show_version_obj2 = ShowVersion(device=self.device)
        parsed_output2 = show_version_obj2.parse()
        self.assertEqual(parsed_output2,self.golden_parsed_output2)

    def test_show_version_golden3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        show_version_obj3 = ShowVersion(device=self.device)
        parsed_output3 = show_version_obj3.parse()
        self.assertEqual(parsed_output3,self.golden_parsed_output3)

    def test_show_version_empty(self):
        self.device = Mock(**self.empty_output)
        show_version_obj = ShowVersion(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = show_version_obj.parse()


# ================================
#  Unit test for 'show sdr detail'       
# ================================

class test_show_sdr_detail(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'sdr_id': {
            0: {
                'dsdrsc_node': '0/RSP0/CPU0',
                'dsdrsc_partner_node': '0/RSP1/CPU0',
                'mac_address': 'a80c.0d5f.ab17',
                'membership': {
                    '0/0/CPU0': {
                        'node_status': 'IOS XR RUN',
                        'partner_name': 'NONE',
                        'red_state': 'Not-known',
                        'type': 'LC'},
                    '0/RSP0/CPU0': {
                        'node_status': 'IOS XR RUN',
                        'partner_name': '0/RSP1/CPU0',
                        'red_state': 'Primary',
                        'type': 'RP'},
                    '0/RSP1/CPU0': {
                        'node_status': 'IOS XR RUN',
                        'partner_name': '0/RSP0/CPU0',
                        'red_state': 'Backup',
                        'type': 'RP'}},
                'primary_node1': '0/RSP0/CPU0',
                'primary_node2': '0/RSP1/CPU0',
                'sdr_name': 'Owner'}}}

    golden_output1 = {'execute.return_value': '''
        SDR Information:
        __________________________________________________
                SDR_id               : 0
                SDR_name             : Owner
                dSDRsc node          : 0/RSP0/CPU0
                dSDRsc partner node  : 0/RSP1/CPU0
                primary node1        : 0/RSP0/CPU0
                primary node2        : 0/RSP1/CPU0
                mac addr             : a80c.0d5f.ab17



        SDR Inventory
        --------------

        Type       NodeName    NodeState         RedState   PartnerName
        ---------------------------------------------------------------
        RP         0/RSP0/CPU0 IOS XR RUN        Primary    0/RSP1/CPU0 
        RP         0/RSP1/CPU0 IOS XR RUN        Backup     0/RSP0/CPU0 
        LC         0/0/CPU0    IOS XR RUN        Not-known  NONE    
        '''}

    golden_parsed_output2 = {
        'sdr_id': {
            0: {
                'dsdrsc_node': '0/0/CPU0',
                'dsdrsc_partner_node': 'NONE',
                'mac_address': '025e.ea57.a400',
                'membership': {
                    '0/0/CPU0': {
                        'node_status': 'IOS XR RUN',
                        'partner_name': 'NONE',
                        'red_state': 'Primary',
                        'type': 'RP'}},
                'primary_node1': '0/0/CPU0',
                'primary_node2': 'NONE',
                'sdr_name': 'Owner'}}}

    golden_output2 = {'execute.return_value': '''
            SDR Information:
        __________________________________________________
                SDR_id               : 0
                SDR_name             : Owner
                dSDRsc node          : 0/0/CPU0
                dSDRsc partner node  : NONE
                primary node1        : 0/0/CPU0
                primary node2        : NONE
                mac addr             : 025e.ea57.a400



        SDR Inventory
        --------------

        Type       NodeName    NodeState         RedState   PartnerName
        ---------------------------------------------------------------
        RP         0/0/CPU0    IOS XR RUN        Primary    NONE
        '''}

    golden_parsed_output3 = {
        'sdr_id': {
            2: {
                'membership': {
                    '0/0/CPU0': {
                        'node_status': 'OPERATIONAL',
                        'partner_name': 'N/A',
                        'red_state': 'None',
                        'type': 'R-IOSXRV9000-LC-C'},
                    '0/RP0/CPU0': {
                        'node_status': 'IOS XR RUN',
                        'partner_name': 'NONE',
                        'red_state': 'ACTIVE',
                        'type': 'RP'}},
                'primary_node1': '0x1000',
                'primary_node2': '0xffffffff',
                'sdr_name': 'default-sdr'}}}


    golden_output3 = {'execute.return_value': '''
        SDR information
        ---------------
        SDR ID             : 2
        SDR name           : default-sdr
        SDR lead (Primary) : 0x1000
        SDR lead (Backup)  : 0xffffffff

        Type                  NodeName       NodeState      RedState       PartnerName
        --------------------------------------------------------------------------------
        R-IOSXRV9000-LC-C     0/0/CPU0       OPERATIONAL                   N/A           
        RP                    0/RP0/CPU0     IOS XR RUN     ACTIVE         NONE          
        LC                    0/0/CPU0       IOS XR RUN     N/A            N/A           
        R-IOSXRV9000-RP-C     0/RP0/CPU0     OPERATIONAL                   N/A
        '''}

    def test_show_sdr_detail_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        show_sdr_obj1 = ShowSdrDetail(device=self.device)
        parsed_output1 = show_sdr_obj1.parse()
        self.assertEqual(parsed_output1,self.golden_parsed_output1)

    def test_show_sdr_detail_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        show_sdr_obj2 = ShowSdrDetail(device=self.device)
        parsed_output2 = show_sdr_obj2.parse()
        self.assertEqual(parsed_output2,self.golden_parsed_output2)

    def test_show_sdr_detail_golden3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        show_sdr_obj3 = ShowSdrDetail(device=self.device)
        parsed_output3 = show_sdr_obj3.parse()
        self.assertEqual(parsed_output3,self.golden_parsed_output3)

    def test_show_sdr_detail_empty(self):
        self.device = Mock(**self.empty_output)
        show_sdr_obj = ShowSdrDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = show_sdr_obj.parse()

# ==============================
#  Unit test for 'show platform'       
# ==============================

class test_show_platform(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'slot': {
            'lc': {
                '0/0': {
                    'config_state': 'PWR,NSHUT,MON',
                    'name': 'A9K-MOD80-SE',
                    'state': 'IOS XR RUN',
                    'subslot': {
                        '0': {
                            'config_state': 'PWR,NSHUT,MON',
                            'name': 'A9K-MPA-20X1GE',
                            'redundancy_state': 'None',
                            'state': 'OK'}}}},
            'rp': {
                '0/RSP0': {
                    'config_state': 'PWR,NSHUT,MON',
                    'name': 'A9K-RSP440-TR',
                    'redundancy_state': 'Active',
                    'state': 'IOS XR RUN'},
                '0/RSP1': {
                    'config_state': 'PWR,NSHUT,MON',
                    'name': 'A9K-RSP440-TR',
                    'redundancy_state': 'Standby',
                    'state': 'IOS XR RUN'}}}}

    golden_output1 = {'execute.return_value': '''
        Node            Type                      State            Config State
        -----------------------------------------------------------------------------
        0/RSP0/CPU0     A9K-RSP440-TR(Active)     IOS XR RUN       PWR,NSHUT,MON
        0/RSP1/CPU0     A9K-RSP440-TR(Standby)    IOS XR RUN       PWR,NSHUT,MON
        0/0/CPU0        A9K-MOD80-SE              IOS XR RUN       PWR,NSHUT,MON
        0/0/0           A9K-MPA-20X1GE            OK               PWR,NSHUT,MON
        '''}

    golden_parsed_output2 = {
        'slot': {
            'lc': {
                '0/0': {
                    'config_state': 'NSHUT',
                    'name': 'R-IOSXRV9000-LC-C',
                    'state': 'IOS XR RUN'}},
            'rp': {
                '0/RP0': {
                    'config_state': 'NSHUT',
                    'name': 'R-IOSXRV9000-RP-C',
                    'redundancy_state': 'Active',
                    'state': 'IOS XR RUN'}}}}

    golden_output2 = {'execute.return_value': '''
        Node              Type                       State             Config state
        --------------------------------------------------------------------------------
        0/0/CPU0          R-IOSXRV9000-LC-C          IOS XR RUN        NSHUT
        0/RP0/CPU0        R-IOSXRV9000-RP-C(Active)  IOS XR RUN        NSHUT
        
        '''}

    golden_parsed_output3 = {
        'slot': {
            'rp': {
                '0/0': {
                    'config_state': 'PWR,NSHUT,MON',
                    'name': 'RP',
                    'plim': 'N/A',
                    'redundancy_state': 'Active',
                    'state': 'IOS XR RUN'}}}}

    golden_output3 = {'execute.return_value': '''
        Node            Type            PLIM            State           Config State
        -----------------------------------------------------------------------------
        0/0/CPU0        RP(Active)      N/A             IOS XR RUN      PWR,NSHUT,MON
        '''}

    golden_parsed_output4 = {
        'slot': {
            'lc': {
                '0/0': {
                    'config_state': 'PWR,NSHUT,MON',
                    'name': 'A9K-MOD80-SE',
                    'state': 'IOS XR RUN',
                    'subslot': {
                        '0': {
                            'config_state': 'PWR,NSHUT,MON',
                            'name': 'A9K-MPA-20X1GE',
                            'redundancy_state': 'None',
                            'state': 'OK'},
                        '1': {
                            'config_state': 'PWR,NSHUT,MON',
                            'name': 'A9K-MQA-20X2GE',
                            'redundancy_state': 'None',
                            'state': 'OK'},
                        '2': {
                            'config_state': 'PWR,NSHUT,MON',
                            'name': 'A9K-MRA-20X3GE',
                            'redundancy_state': 'None',
                            'state': 'OK'}}}},
            'rp': {
                '0/RSP0': {
                    'config_state': 'PWR,NSHUT,MON',
                    'name': 'A9K-RSP440-TR',
                    'redundancy_state': 'Active',
                    'state': 'IOS XR RUN'},
                '0/RSP1': {
                    'config_state': 'PWR,NSHUT,MON',
                    'name': 'A9K-RSP440-TR',
                    'redundancy_state': 'Standby',
                    'state': 'IOS XR RUN'}}}}

    golden_output4 = {'execute.return_value': '''
        Node            Type                      State            Config State
        -----------------------------------------------------------------------------
        0/RSP0/CPU0     A9K-RSP440-TR(Active)     IOS XR RUN       PWR,NSHUT,MON
        0/RSP1/CPU0     A9K-RSP440-TR(Standby)    IOS XR RUN       PWR,NSHUT,MON
        0/0/CPU0        A9K-MOD80-SE              IOS XR RUN       PWR,NSHUT,MON
        0/0/0           A9K-MPA-20X1GE            OK               PWR,NSHUT,MON
        0/0/1           A9K-MQA-20X2GE            OK               PWR,NSHUT,MON
        0/0/2           A9K-MRA-20X3GE            OK               PWR,NSHUT,MON
        '''}

    golden_parsed_output5 = {
        'slot': {
            'lc': {
                '0/0': {
                    'config_state': 'PWR,NSHUT,MON',
                    'name': 'A9K-MPA-20X1GE',
                    'state': 'OK',
                    'subslot': {
                        '0': {
                            'config_state': 'PWR,NSHUT,MON',
                            'name': 'A9K-MPA-20X1GE',
                            'redundancy_state': 'None',
                            'state': 'OK'},
                        '1': {
                            'config_state': 'PWR,NSHUT,MON',
                            'name': 'A9K-MQA-20X2GE',
                            'redundancy_state': 'None',
                            'state': 'OK'},
                        '2': {
                            'config_state': 'PWR,NSHUT,MON',
                            'name': 'A9K-MRA-20X3GE',
                            'redundancy_state': 'None',
                            'state': 'OK'}}}},
            'rp': {
                '0/RSP0': {
                    'config_state': 'PWR,NSHUT,MON',
                    'name': 'A9K-RSP440-TR',
                    'redundancy_state': 'Active',
                    'state': 'IOS XR RUN'},
                 '0/RSP1': {
                    'config_state': 'PWR,NSHUT,MON',
                    'name': 'A9K-RSP440-TR',
                    'redundancy_state': 'Standby',
                    'state': 'IOS XR RUN'}}}}

    golden_output5 = {'execute.return_value': '''
        Node            Type                      State            Config State
        -----------------------------------------------------------------------------
        0/RSP0/CPU0     A9K-RSP440-TR(Active)     IOS XR RUN       PWR,NSHUT,MON
        0/RSP1/CPU0     A9K-RSP440-TR(Standby)    IOS XR RUN       PWR,NSHUT,MON
        0/0/0           A9K-MPA-20X1GE            OK               PWR,NSHUT,MON
        0/0/1           A9K-MQA-20X2GE            OK               PWR,NSHUT,MON
        0/0/2           A9K-MRA-20X3GE            OK               PWR,NSHUT,MON
        0/0/CPU0        A9K-MOD80-SE              IOS XR RUN       PWR,NSHUT,MON
        '''}

    def test_show_platform_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        show_platform_obj1 = ShowPlatform(device=self.device)
        parsed_output1 = show_platform_obj1.parse()
        self.assertEqual(parsed_output1,self.golden_parsed_output1)
    
    def test_show_platform_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        show_platform_obj2 = ShowPlatform(device=self.device)
        parsed_output2 = show_platform_obj2.parse()
        self.assertEqual(parsed_output2,self.golden_parsed_output2)
    
    def test_show_platform_golden3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        show_platform_obj3 = ShowPlatform(device=self.device)
        parsed_output3 = show_platform_obj3.parse()
        self.assertEqual(parsed_output3,self.golden_parsed_output3)

    def test_show_platform_golden4(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output4)
        show_platform_obj4 = ShowPlatform(device=self.device)
        parsed_output4 = show_platform_obj4.parse()
        self.assertEqual(parsed_output4,self.golden_parsed_output4)

    def test_show_platform_golden5(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output5)
        show_platform_obj5 = ShowPlatform(device=self.device)
        parsed_output5 = show_platform_obj5.parse()
        import pdb ;  pdb.set_trace()
        self.assertEqual(parsed_output5,self.golden_parsed_output5)

    def test_show_platform_empty(self):
        self.device = Mock(**self.empty_output)
        show_platform_obj = ShowPlatform(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = show_platform_obj.parse()

# =================================
#  Unit test for 'show platform vm'       
# =================================

class test_show_platform_vm(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'node': {
            '0/0/CPU0': {
                'ip_address': '192.0.0.6',
                'partner_name': 'NONE',
                'sw_status': 'FINAL Band',
                'type': 'LC (ACTIVE)'},
            '0/RP0/CPU0': {
                'ip_address': '192.0.0.4',
                'partner_name': 'NONE',
                'sw_status': 'FINAL Band',
                'type': 'RP (ACTIVE)'}}}


    golden_output1 = {'execute.return_value': '''
        Node name       Node type       Partner name    SW status       IP address
        --------------- --------------- --------------- --------------- ---------------
        0/RP0/CPU0      RP (ACTIVE)     NONE            FINAL Band      192.0.0.4
        0/0/CPU0        LC (ACTIVE)     NONE            FINAL Band      192.0.0.6
        '''}

    def test_show_platform_vm_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        show_platform_vm_obj1 = ShowPlatformVm(device=self.device)
        parsed_output1 = show_platform_vm_obj1.parse()
        self.assertEqual(parsed_output1,self.golden_parsed_output1)

    def test_show_platform_vm_empty(self):
        self.device = Mock(**self.empty_output)
        show_platform_vm_obj = ShowPlatformVm(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = show_platform_vm_obj.parse()

# ============================================
#  Unit test for 'show install active summary'       
# ============================================

class test_show_install_active_summary(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'active_packages': ['disk0:asr9k-mini-px-6.1.21.15I',
                            'disk0:asr9k-mpls-px-6.1.21.15I',
                            'disk0:asr9k-mcast-px-6.1.21.15I',
                            'disk0:asr9k-mgbl-px-6.1.21.15I'],
        'sdr': 'Owner'}

    golden_output1 = {'execute.return_value': '''
        Default Profile:
          SDRs:
            Owner
        Active Packages:
            disk0:asr9k-mini-px-6.1.21.15I
            disk0:asr9k-mpls-px-6.1.21.15I
            disk0:asr9k-mcast-px-6.1.21.15I
            disk0:asr9k-mgbl-px-6.1.21.15I
        '''}

    golden_parsed_output2 = {
        'active_packages': ['xrv9k-xr-6.2.2.14I version=6.2.2.14I [Boot image]'],
        'num_active_packages': 1}

    golden_output2 = {'execute.return_value': '''
        Active Packages: 1
            xrv9k-xr-6.2.2.14I version=6.2.2.14I [Boot image]
        '''}

    def test_show_install_active_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        install_active_obj1 = ShowInstallActiveSummary(device=self.device)
        parsed_output1 = install_active_obj1.parse()
        self.assertEqual(parsed_output1,self.golden_parsed_output1)

    def test_show_install_active_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        install_active_obj2 = ShowInstallActiveSummary(device=self.device)
        parsed_output2 = install_active_obj2.parse()
        self.assertEqual(parsed_output2,self.golden_parsed_output2)

    def test_show_install_active_empty(self):
        self.device = Mock(**self.empty_output)
        install_active_obj = ShowInstallActiveSummary(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = install_active_obj.parse()

# ===============================
#  Unit test for 'show inventory'
# ===============================

class test_show_inventory(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'module_name': {
            'module 0/RSP0/CPU0': {
                'descr': 'ASR9K Route Switch '
                         'Processor with 440G/slot '
                         'Fabric and 6GB',
                'pid': 'A9K-RSP440-TR',
                'sn': 'FOC1808NEND',
                'vid': 'V05'},
            'module 0/RSP1/CPU0': {
                'descr': 'ASR9K Route Switch '
                         'Processor with 440G/slot '
                         'Fabric and 6GB',
                'pid': 'A9K-MPA-20X1GE',
                'sn': 'FOC1811N49J',
                'vid': 'V02'},
            'module mau 0/0/0/0': {
                'descr': 'Unknown or Unsupported '
                         'CPAK Module',
                'pid': 'GLC-T',
                'sn': '00000MTC160107LP',
                'vid': 'N/A'},
            'module mau 0/0/0/1': {
                'descr': 'Unknown or Unsupported '
                         'CPAK Module',
                'pid': 'GLC-T',
                'sn': '00000MTC17150731',
                'vid': 'N/A'}}}

    golden_output1 = {'execute.return_value': '''
        NAME: "module 0/RSP0/CPU0", DESCR: "ASR9K Route Switch Processor with 440G/slot Fabric and 6GB"
        PID: A9K-RSP440-TR, VID: V05, SN: FOC1808NEND

        NAME: "module 0/RSP1/CPU0", DESCR: "ASR9K Route Switch Processor with 440G/slot Fabric and 6GB"
        PID: A9K-RSP440-TR, VID: V05, SN: FOC1808NEP5

        NAME: "module 0/0/CPU0", DESCR: "80G Modular Linecard, Service Edge Optimized"
        PID: A9K-MOD80-SE, VID: V06, SN: FOC1821NEET

        NAME: "module 0/0/0", DESCR: "ASR 9000 20-port 1GE Modular Port Adapter"
        PID: A9K-MPA-20X1GE, VID: V02, SN: FOC1811N49J

        NAME: "module mau 0/0/0/0", DESCR: "Unknown or Unsupported CPAK Module"
        PID: GLC-T               , VID: N/A, SN: 00000MTC160107LP

        NAME: "module mau 0/0/0/1", DESCR: "Unknown or Unsupported CPAK Module"
        PID: GLC-T               , VID: N/A, SN: 00000MTC17150731
        '''}

    golden_parsed_output2 = {
        'module_name': {
            '0/0': {
                'descr': 'Cisco XRv9K Centralized Line Card',
                'pid': 'R-IOSXRV9000-LC-C',
                'sn': 'AB7FB950B88',
                'vid': 'V01'},
        '0/0/0': {
            'descr': 'N/A',
            'pid': 'SFP-1G-NIC-X',
            'sn': 'N/A',
            'vid': 'N/A'},
        '0/0/1': {
            'descr': 'N/A',
            'pid': 'SFP-1G-NIC-X',
            'sn': 'N/A',
            'vid': 'N/A'},
        '0/0/2': {
            'descr': 'N/A',
            'pid': 'SFP-1G-NIC-X',
            'sn': 'N/A',
            'vid': 'N/A'},
        '0/RP0': {
            'descr': 'Cisco XRv9K Centralized Route '
                     'Processor',
            'pid': 'R-IOSXRV9000-RP-C',
            'sn': 'DEB3B4DE58E',
            'vid': 'V01'},
        'Rack 0': {
            'descr': 'Cisco XRv9K Centralized Virtual '
                     'Router',
            'pid': 'R-IOSXRV9000-CC',
            'sn': 'E289E87566C',
            'vid': 'V01'}}}

    golden_output2 = {'execute.return_value': '''
        NAME: "0/0", DESCR: "Cisco XRv9K Centralized Line Card"
        PID: R-IOSXRV9000-LC-C , VID: V01, SN: AB7FB950B88

        NAME: "0/0/0", DESCR: "N/A"
        PID: SFP-1G-NIC-X      , VID: N/A, SN: N/A

        NAME: "0/0/1", DESCR: "N/A"
        PID: SFP-1G-NIC-X      , VID: N/A, SN: N/A

        NAME: "0/0/2", DESCR: "N/A"
        PID: SFP-1G-NIC-X      , VID: N/A, SN: N/A

        NAME: "0/RP0", DESCR: "Cisco XRv9K Centralized Route Processor"
        PID: R-IOSXRV9000-RP-C , VID: V01, SN: DEB3B4DE58E

        NAME: "Rack 0", DESCR: "Cisco XRv9K Centralized Virtual Router"
        PID: R-IOSXRV9000-CC   , VID: V01, SN: E289E87566C
        '''}

    def test_show_inventory_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        invetory_obj1 = ShowInventory(device=self.device)
        parsed_output1 = invetory_obj1.parse()
        self.assertEqual(parsed_output1,self.golden_parsed_output1)

    def test_show_inventory_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        invetory_obj2 = ShowInventory(device=self.device)
        parsed_output2 = invetory_obj2.parse()
        self.assertEqual(parsed_output2,self.golden_parsed_output2)

    def test_show_inventory_empty(self):
        self.device = Mock(**self.empty_output)
        invetory_obj = ShowInventory(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = invetory_obj.parse()

# =======================================
#  Unit test for admin show diag chassis'       
# =======================================

class test_admin_show_diag_chassis(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'chassis_feature': 'V2 AC PEM',
        'clei': 'IPMUP00BRB',
        'desc': 'ASR 9006 4 Line Card Slot Chassis with V2 AC PEM',
        'device_family': 'ASR',
        'device_series': 9006,
        'num_line_cards': 4,
        'pid': 'ASR-9006-AC-V2',
        'rack_num': 0,
        'sn': 'FOX1810G8LR',
        'top_assy_num': '68-4235-02',
        'vid': 'V02'}

    golden_output1 = {'execute.return_value': '''
        Rack 0 - ASR 9006 4 Line Card Slot Chassis with V2 AC PEM
          RACK NUM: 0
          S/N:   FOX1810G8LR
          PID:   ASR-9006-AC-V2
          VID:   V02
          Desc:  ASR 9006 4 Line Card Slot Chassis with V2 AC PEM
          CLEI:  IPMUP00BRB
          Top Assy. Number:   68-4235-02
        '''}

    def test_admin_show_diag_chassis_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        diag_chassis_obj1 = AdminShowDiagChassis(device=self.device)
        parsed_output1 = diag_chassis_obj1.parse()
        self.assertEqual(parsed_output1,self.golden_parsed_output1)

    def test_show_inventory_empty(self):
        self.device = Mock(**self.empty_output)
        diag_chassis_obj = AdminShowDiagChassis(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = diag_chassis_obj.parse()

# ========================================
#  Unit test for 'show redundancy summary'       
# ========================================

class test_show_redundancy_summary(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'node': {
            '0/RSP0/CPU0(A)': {
                'node_detail': 'Node Not Ready, NSR: Not '
                               'Configured',
                'standby_node': '0/RSP1/CPU0(S)',
                'type': 'active'},
            '0/RSP0/CPU0(P)': {
                'backup_node': '0/RSP1/CPU0(B)',
                'node_detail': 'Proc Group Not Ready, NSR: '
                               'Ready',
                'standby_node': '0/RSP1/CPU0(B)',
                'type': 'primary'}}}

    golden_output1 = {'execute.return_value': '''
        Active/Primary   Standby/Backup
        --------------   --------------
        0/RSP0/CPU0(A)   0/RSP1/CPU0(S) (Node Not Ready, NSR: Not Configured)
        0/RSP0/CPU0(P)   0/RSP1/CPU0(B) (Proc Group Not Ready, NSR: Ready)
        0/RSP0/CPU0(P)           N/A    (Proc Group Not Ready)
        '''}

    golden_parsed_output2 = {
        'node': {
            '0/RP0/CPU0': {
                'standby_node': 'N/A',
                'type': 'active'}}}


    golden_output2 = {'execute.return_value': '''
        Active Node    Standby Node
        -----------    ------------
         0/RP0/CPU0             N/A
        '''}

    def test_show_redundancy_summary_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        show_redundancy_summary_obj1 = ShowRedundancySummary(device=self.device)
        parsed_output1 = show_redundancy_summary_obj1.parse()
        self.assertEqual(parsed_output1,self.golden_parsed_output1)

    def test_show_redundancy_summary_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        show_redundancy_summary_obj2 = ShowRedundancySummary(device=self.device)
        parsed_output2 = show_redundancy_summary_obj2.parse()
        self.assertEqual(parsed_output2,self.golden_parsed_output2)

    def test_show_platform_vm_empty(self):
        self.device = Mock(**self.empty_output)
        show_redundancy_summary_obj = ShowRedundancySummary(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = show_redundancy_summary_obj.parse()

# ================================
#  Unit test for 'show redundancy'       
# ================================

class test_show_redundancy(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'node': {
            '0/RSP0/CPU0': {
                'group': {
                    'central-services': {
                        'backup': 'N/A',
                        'primary': '0/RSP0/CPU0',
                        'status': 'Not '
                                  'Ready'},
                    'dlrsc': {
                        'backup': 'N/A',
                        'primary': '0/RSP0/CPU0',
                        'status': 'Not Ready'},
                    'dsc': {
                        'backup': 'N/A',
                        'primary': '0/RSP0/CPU0',
                        'status': 'Not Ready'},
                    'mcast-routing': {
                        'backup': 'N/A',
                        'primary': '0/RSP0/CPU0',
                        'status': 'Not '
                                  'Ready'},
                    'netmgmt': {
                        'backup': 'N/A',
                        'primary': '0/RSP0/CPU0',
                        'status': 'Not Ready'},
                    'v4-routing': {
                        'backup': 'N/A',
                        'primary': '0/RSP0/CPU0',
                        'status': 'Not Ready'},
                    'v6-routing': {
                        'backup': 'N/A',
                        'primary': '0/RSP0/CPU0',
                        'status': 'Not Ready'}},
                'last_reload_timestamp': 'Thu Apr 27 02:14:12 '
                                         '2017',
                'last_switchover_timepstamp': 'Thu Apr 27 '
                                              '03:29:57 2017',
                'node_uptime': '8 minutes ago',
                'node_uptime_timestamp': 'Thu Apr 27 03:22:37 '
                                         '2017',
                'primary_rmf_state': 'not ready',
                'primary_rmf_state_reason': 'Backup is not '
                                            'Present',
                'reload_cause': 'Initiating switch-over',
                'role': 'ACTIVE',
                'time_since_last_reload': '1 hour, 16 minutes ago',
                'time_since_last_switchover': '1 minute ago',
                'valid_partner': ''}}}

    golden_output1 = {'execute.return_value': '''
        Redundancy information for node 0/RSP0/CPU0:
        ==========================================
        Node 0/RSP0/CPU0 is in ACTIVE role
        Node 0/RSP0/CPU0 has no valid partner

        Group            Primary         Backup          Status         
        ---------        ---------       ---------       ---------      
        v6-routing       0/RSP0/CPU0     N/A             Not Ready      
        v6-routing       0/RSP0/CPU0     N/A             Not NSR-Ready  
        mcast-routing    0/RSP0/CPU0     N/A             Not Ready      
        mcast-routing    0/RSP0/CPU0     N/A             Not NSR-Ready  
        netmgmt          0/RSP0/CPU0     N/A             Not Ready      
        v4-routing       0/RSP0/CPU0     N/A             Not Ready      
        v4-routing       0/RSP0/CPU0     N/A             Not NSR-Ready  
        central-services 0/RSP0/CPU0     N/A             Not Ready      
        central-services 0/RSP0/CPU0     N/A             Not NSR-Ready  
        dsc              0/RSP0/CPU0     N/A             Not Ready      
        dlrsc            0/RSP0/CPU0     N/A             Not Ready      

        Process Group Details
        ---------------------

        Current primary rmf state:
            NSR not ready since Backup is not Present

        Reload and boot info
        ----------------------
        A9K-RSP440-TR reloaded Thu Apr 27 02:14:12 2017: 1 hour, 16 minutes ago
        Active node booted Thu Apr 27 03:22:37 2017: 8 minutes ago
        Last switch-over Thu Apr 27 03:29:57 2017: 1 minute ago
        Active node reload  Cause: Initiating switch-over.
        '''}

    def test_show_redundancy_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        show_redundancy_obj1 = ShowRedundancy(device=self.device)
        parsed_output1 = show_redundancy_obj1.parse()
        self.assertEqual(parsed_output1,self.golden_parsed_output1)


    def test_show_platform_vm_empty(self):
        self.device = Mock(**self.empty_output)
        show_redundancy_obj = ShowRedundancy(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = show_redundancy_obj.parse()

if __name__ == '__main__':
    unittest.main()

# vim: ft=python et sw=4