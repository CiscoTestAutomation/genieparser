# Python
import re
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Parser
from genie.libs.parser.iosxr.show_platform import ShowRedundancy, ShowPlatformVm,\
                                ShowPlatform, ShowSdrDetail,\
                                ShowInstallActiveSummary, ShowInventory,\
                                ShowRedundancySummary, AdminShowDiagChassis,\
                                ShowVersion, Dir, ShowInstallInactiveSummary,\
                                ShowInstallCommitSummary

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

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
        'device_family': 'ASR9K Series',
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
        'device_family': 'IOS XRv Series',
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

    device_output = {'execute.return_value': '''
        Mon Oct 14 17:44:22.298 EDT
        
        Cisco IOS XR Software, Version 6.4.2[Default]
        Copyright (c) 2019 by Cisco Systems, Inc.
        
        ROM: System Bootstrap, Version 2.12(20170128:070504) [CRS ROMMON],  
        
        
        tcore3-rohan uptime is 4 days, 5 hours, 46 minutes
        System image file is "disk0:hfr-os-mbi-6.4.2.CSCvm85739-1.0.0/0x100008/mbihfr-rp-x86e.vm"
        
        cisco CRS-16/S-B (Intel 686 F6M14S4) processor with 12582912K bytes of memory.
        Intel 686 F6M14S4 processor at 2127Mhz, Revision 2.174
        CRS 16 Slots Line Card Chassis for CRS-16/S-B
        
        2 Management Ethernet
        54 TenGigE
        59 DWDM controller(s)
        54 WANPHY controller(s)
        5 HundredGigE
        5 GigabitEthernet
        4 SONET/SDH
        4 Packet over SONET/SDH
        1019k bytes of non-volatile configuration memory.
        16726M bytes of hard disk.
        11881456k bytes of disk0: (Sector size 512 bytes).
        11881456k bytes of disk1: (Sector size 512 bytes).
        
        Boot device on node 0/0/CPU0 is lcdisk0:
        Package active on node 0/0/CPU0:
        iosxr-mpls-6.4.2.CSCvr26601, V 1.0.0[SMU], Cisco Systems, at disk0:iosxr-mpls-6.4.2.CSCvr26601-1.0.0
            Built on Fri Oct  4 05:07:32 EDT 2019
            By iox-lnx-smu2 in /san2/EFR/smu_r64x_6_4_2/workspace for pie
        
        hfr-px-6.4.2.CSCvr26601, V 1.0.0[SMU], Cisco Systems, at disk0:hfr-px-6.4.2.CSCvr26601-1.0.0
            Built on Fri Oct  4 05:07:38 EDT 2019
            By iox-lnx-smu2 in /san2/EFR/smu_r64x_6_4_2/workspace for pie
    '''}

    device_parsed_output = {
        'chassis_detail': 'CRS 16 Slots Line Card Chassis for CRS-16/S-B',
        'device_family': 'CRS-16/S-B',
        'image': 'disk0:hfr-os-mbi-6.4.2.CSCvm85739-1.0.0/0x100008/mbihfr-rp-x86e.vm',
        'main_mem': 'cisco CRS-16/S-B (Intel 686 F6M14S4) processor with 12582912K bytes of memory.',
        'operating_system': 'IOSXR',
        'processor': 'Intel 686 F6M14S4',
        'processor_memory_bytes': '12582912K',
        'software_version': '6.4.2',
        'uptime': '4 days, 5 hours, 46 minutes',
    }

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

    def test(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output)
        show_version_obj = ShowVersion(device=self.device)
        parsed_output = show_version_obj.parse()
        self.assertEqual(parsed_output,self.device_parsed_output)


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
                    'full_slot': '0/0/CPU0',
                    'subslot': {
                        '0': {
                            'config_state': 'PWR,NSHUT,MON',
                            'name': 'A9K-MPA-20X1GE',
                            'redundancy_state': 'None',
                            'state': 'OK'}}}},
            'rp': {
                '0/RSP0': {
                    'full_slot': '0/RSP0/CPU0',
                    'config_state': 'PWR,NSHUT,MON',
                    'name': 'A9K-RSP440-TR',
                    'redundancy_state': 'Active',
                    'state': 'IOS XR RUN'},
                '0/RSP1': {
                    'full_slot': '0/RSP1/CPU0',
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
                    'full_slot': '0/0/CPU0',
                    'name': 'R-IOSXRV9000-LC-C',
                    'state': 'IOS XR RUN'}},
            'rp': {
                '0/RP0': {
                    'config_state': 'NSHUT',
                    'full_slot': '0/RP0/CPU0',
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
                    'full_slot': '0/0/CPU0',
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
                    'full_slot': '0/0/CPU0',
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
                    'full_slot': '0/RSP0/CPU0',
                    'name': 'A9K-RSP440-TR',
                    'redundancy_state': 'Active',
                    'state': 'IOS XR RUN'},
                '0/RSP1': {
                    'config_state': 'PWR,NSHUT,MON',
                    'name': 'A9K-RSP440-TR',
                    'full_slot': '0/RSP1/CPU0',
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
                    'full_slot': '0/0/0',
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
                    'full_slot': '0/RSP0/CPU0',
                    'name': 'A9K-RSP440-TR',
                    'redundancy_state': 'Active',
                    'state': 'IOS XR RUN'},
                 '0/RSP1': {
                    'config_state': 'PWR,NSHUT,MON',
                    'full_slot': '0/RSP1/CPU0',
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

    golden_output_2 = {'execute.return_value': '''\
        RP/0/RSP0/CPU0:ios#show platform vm
        Sat Sep  7 18:34:53.949 UTC
        Node name       Node type       Partner name    SW status       IP address
        --------------- --------------- --------------- --------------- ---------------
        0/RSP0/CPU0     RP (ACTIVE)     0/RSP1/CPU0     FINAL Band      192.0.0.4
        0/RSP1/CPU0     RP (STANDBY)    0/RSP0/CPU0     FINAL Band      192.168.166.4
    '''
    }

    golden_parsed_output_2 = {
        'node': {
            '0/RSP0/CPU0': {
                'ip_address': '192.0.0.4',
                'partner_name': '0/RSP1/CPU0',
                'sw_status': 'FINAL Band',
                'type': 'RP (ACTIVE)'
            },
            '0/RSP1/CPU0': {
                'ip_address': '192.168.166.4',
                'partner_name': '0/RSP0/CPU0',
                'sw_status': 'FINAL Band',
                'type': 'RP (STANDBY)'
            }
        }
    }

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

    def test_show_platform_vm_golden_thaing(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        obj = ShowPlatformVm(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

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
    maxDiff = None
    golden_parsed_output1 = {
        "module_name": {
          "module 0/RSP0/CPU0": {
               "pid": "A9K-RSP440-TR",
               "descr": "ASR9K Route Switch Processor with 440G/slot Fabric and 6GB",
               "sn": "FOC1808NEND",
               "vid": "V05"
          },
          "module 0/RSP1/CPU0": {
               "pid": "A9K-RSP440-TR",
               "descr": "ASR9K Route Switch Processor with 440G/slot Fabric and 6GB",
               "sn": "FOC1808NEP5",
               "vid": "V05"
          },
          "module mau 0/0/0/1": {
               "pid": "GLC-T",
               "descr": "Unknown or Unsupported CPAK Module",
               "sn": "00000MTC17150731",
               "vid": "N/A"
          },
          "module 0/0/CPU0": {
               "pid": "A9K-MOD80-SE",
               "descr": "80G Modular Linecard, Service Edge Optimized",
               "sn": "FOC1821NEET",
               "vid": "V06"
          },
          "module 0/0/0": {
               "pid": "A9K-MPA-20X1GE",
               "descr": "ASR 9000 20-port 1GE Modular Port Adapter",
               "sn": "FOC1811N49J",
               "vid": "V02"
          },
          "module mau 0/0/0/0": {
               "pid": "GLC-T",
               "descr": "Unknown or Unsupported CPAK Module",
               "sn": "00000MTC160107LP",
               "vid": "N/A"
          }
     }}

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

    golden_output3 = {'execute.return_value': '''
        show inventory

        Mon Oct 14 17:55:59.530 EDT
        NAME: "module 0/RSP0/CPU0", DESCR: "ASR9K Route Switch Processor with 880G/slot Fabric and 32GB"
        PID: A9K-RSP880-SE, VID: V02, SN: FOC2027NFV5

        NAME: "module 0/RSP1/CPU0", DESCR: "ASR9K Route Switch Processor with 880G/slot Fabric and 32GB"
        PID: A9K-RSP880-SE, VID: V02, SN: FOC2027NFVR

        NAME: "module 0/0/CPU0", DESCR: "80G Modular Linecard, Service Edge Optimized"
        PID: A9K-MOD80-SE, VID: V08, SN: FOC1941N335

        NAME: "module 0/0/0", DESCR: "ASR 9000 20-port 1GE Modular Port Adapter"
        PID: A9K-MPA-20X1GE, VID: V03, SN: FOC1946N2X9

        NAME: "GigabitEthernet0/0/0/1", DESCR: "Non-Cisco Methode Elec. SFP 1G Pluggable Optics Module"
        PID: SP7041-M1-JN, VID: -, SN: 9420172         

        NAME: "GigabitEthernet0/0/0/2", DESCR: "Non-Cisco E.C.I.NETWORKS SFP 1G Pluggable Optics Module"
        PID: EN-SFP1G-LX-CO, VID: 1.0, SN: ECI50L257       

        NAME: "module mau 0/0/0/4", DESCR: "GE T"
        PID: N/A, VID: N/A, SN: MTC17180BJ4     

        NAME: "GigabitEthernet0/0/0/8", DESCR: "Non-Cisco E.C.I.NETWORKS SFP 1G Pluggable Optics Module"
        PID: EN-SFP-GE-T, VID: 1.0, SN: ECI80T012       

        NAME: "GigabitEthernet0/0/0/19", DESCR: "Non-Cisco E.C.I.NETWORKS SFP 1G Pluggable Optics Module"
        PID: EN-SFP1G-LX-CO, VID: 1.0, SN: ECI50L003       

        NAME: "module 0/0/1", DESCR: "ASR 9000 4-port 10GE Modular Port Adapter"
        PID: A9K-MPA-4X10GE, VID: V05, SN: FOC1935NCBZ

        NAME: "module mau 0/0/1/1", DESCR: "Multirate 10GBASE-LR and OC-192/STM-64 SR-1 XFP, SMF"
        PID: XFP-10GLR-OC192SR   , VID: V04 , SN: SPC191402P5     

        NAME: "TenGigE0/0/1/2", DESCR: "Non-Cisco ECINETWORKS XFP 10G Pluggable Optics Module"
        PID: EN-XFP10G-LR-CO, VID: N, SN: B31160520008    

        NAME: "TenGigE0/0/1/3", DESCR: "Non-Cisco XFP 10G Pluggable Optics Module"
        PID: N/A, VID: N/A, SN: 

        NAME: "module 0/1/CPU0", DESCR: "80G Modular Linecard, Service Edge Optimized"
        PID: A9K-MOD80-SE, VID: V11, SN: FOC2242P17S

        NAME: "module 0/1/0", DESCR: "ASR 9000 20-port 1GE Modular Port Adapter"
        PID: A9K-MPA-20X1GE, VID: V06, SN: FOC2244NCSA

        NAME: "module mau 0/1/0/2", DESCR: "1000BASE-SX SFP transceiver module, MMF, 850nm, DOM"
        PID: GLC-SX-MMD          , VID: V01 , SN: AGJ1821REPB     

        NAME: "GigabitEthernet0/1/0/12", DESCR: "Non-Cisco E.C.I.NETWORKS SFP 1G Pluggable Optics Module"
        PID: EN-SFP1G-LX-CO, VID: 1.0, SN: ECI50L252       

        NAME: "module 0/2/CPU0", DESCR: "Cisco ASR 9000 Series SPA Interface Processor-700"
        PID: A9K-SIP-700, VID: V02, SN: FOC1748N0B7

        NAME: "module 0/2/0", DESCR: "3-port OC3c SFP Optics ATM Shared Port Adapter"
        PID: SPA-3XOC3-ATM-V2, VID: V03, SN: JP614240083

        NAME: "module mau 0/2/0/2", DESCR: "OC3 SR-1/STM1 MM"
        PID: SFP-OC3-MM          , VID: V01 , SN: OCP10310921     

        NAME: "module 0/4/CPU0", DESCR: "24X10G/1G  Service Edge Optimized LC"
        PID: A9K-24X10GE-1G-SE, VID: V01, SN: FOC2237N3Y0

        NAME: "module mau GigabitEthernet0/4/CPU0/0", DESCR: "Unknown or Unsupported SFP Module"
        PID: GLC-T              , VID: V04, SN: MTC191108UW     

        NAME: "module mau GigabitEthernet0/4/CPU0/1", DESCR: "Unknown pluggable optics"
        PID: N/A, VID: N/A, SN: FNS13441EZE     

        NAME: "GigabitEthernet0/4/0/5", DESCR: "Non-Cisco E.C.I.NETWORKS SFP 1G Pluggable Optics Module"
        PID: EN-SFP1G-LX-CO, VID: 1., SN: ECI50L009       

        NAME: "GigabitEthernet0/4/0/6", DESCR: "Non-Cisco E.C.I.NETWORKS SFP 1G Pluggable Optics Module"
        PID: EN-SFP1G-SX-CO, VID: 1., SN: ECI32M012       

        NAME: "TenGigE0/4/0/12", DESCR: "Non-Cisco LambdaGain SFP+ 10G Pluggable Optics Module"
        PID: L04D-10GE-ER, VID: N/A, SN: FXLG021112310001

        NAME: "TenGigE0/4/0/13", DESCR: "Non-Cisco E.C.I.NETWORKS SFP+ 10G Pluggable Optics Module"
        PID: EN-SFP10G-LR-CO, VID: 1., SN: ECIXPL037       

        NAME: "module mau TenGigE0/4/CPU0/14", DESCR: "10GBASE-SR SFP+ Module for MMF"
        PID: SFP-10G-SR         , VID: V03 , SN: JUR184402WK     

        NAME: "module mau TenGigE0/4/CPU0/16", DESCR: "10GBASE-LR SFP+ Module for SMF"
        PID: SFP-10G-LR         , VID: V02 , SN: FNS16201FK4     

        NAME: "TenGigE0/4/0/20", DESCR: "Non-Cisco FINISAR CORP. SFP+ 10G Pluggable Optics Module"
        PID: FTLX1471D3BNL-J1, VID: A, SN: APG0MX8         

        NAME: "module mau TenGigE0/4/CPU0/21", DESCR: "10GBASE-LR SFP+ Module for SMF"
        PID: SFP-10G-LR         , VID: V02 , SN: ONT174402HM     

        NAME: "TenGigE0/4/0/22", DESCR: "Non-Cisco SumitomoElectric SFP+ 10G Pluggable Optics Module"
        PID: SPP5200LR-J6-M, VID: A, SN: 163627A01776    

        NAME: "TenGigE0/4/0/23", DESCR: "Non-Cisco E.C.I.NETWORKS SFP+ 10G Pluggable Optics Module"
        PID: EN-SFP10G-LR-CO, VID: 1., SN: ECIXPL233       

    '''}

    golden_parsed_output3 = {
        'module_name': {
            'module 0/RSP0/CPU0': {
                'descr': 'ASR9K Route Switch Processor with 880G/slot Fabric and 32GB',
                'pid': 'A9K-RSP880-SE',
                'vid': 'V02',
                'sn': 'FOC2027NFV5',
            },
            'module 0/RSP1/CPU0': {
                'descr': 'ASR9K Route Switch Processor with 880G/slot Fabric and 32GB',
                'pid': 'A9K-RSP880-SE',
                'vid': 'V02',
                'sn': 'FOC2027NFVR',
            },
            'module 0/0/CPU0': {
                'descr': '80G Modular Linecard, Service Edge Optimized',
                'pid': 'A9K-MOD80-SE',
                'vid': 'V08',
                'sn': 'FOC1941N335',
            },
            'module 0/0/0': {
                'descr': 'ASR 9000 20-port 1GE Modular Port Adapter',
                'pid': 'A9K-MPA-20X1GE',
                'vid': 'V03',
                'sn': 'FOC1946N2X9',
            },
            'GigabitEthernet0/0/0/1': {
                'descr': 'Non-Cisco Methode Elec. SFP 1G Pluggable Optics Module',
                'pid': 'SP7041-M1-JN',
                'vid': '-',
                'sn': '9420172',
            },
            'GigabitEthernet0/0/0/2': {
                'descr': 'Non-Cisco E.C.I.NETWORKS SFP 1G Pluggable Optics Module',
                'pid': 'EN-SFP1G-LX-CO',
                'vid': '1.0',
                'sn': 'ECI50L257',
            },
            'module mau 0/0/0/4': {
                'descr': 'GE T',
                'pid': 'N/A',
                'vid': 'N/A',
                'sn': 'MTC17180BJ4',
            },
            'GigabitEthernet0/0/0/8': {
                'descr': 'Non-Cisco E.C.I.NETWORKS SFP 1G Pluggable Optics Module',
                'pid': 'EN-SFP-GE-T',
                'vid': '1.0',
                'sn': 'ECI80T012',
            },
            'GigabitEthernet0/0/0/19': {
                'descr': 'Non-Cisco E.C.I.NETWORKS SFP 1G Pluggable Optics Module',
                'pid': 'EN-SFP1G-LX-CO',
                'vid': '1.0',
                'sn': 'ECI50L003',
            },
            'module 0/0/1': {
                'descr': 'ASR 9000 4-port 10GE Modular Port Adapter',
                'pid': 'A9K-MPA-4X10GE',
                'vid': 'V05',
                'sn': 'FOC1935NCBZ',
            },
            'module mau 0/0/1/1': {
                'descr': 'Multirate 10GBASE-LR and OC-192/STM-64 SR-1 XFP, SMF',
                'pid': 'XFP-10GLR-OC192SR',
                'vid': 'V04',
                'sn': 'SPC191402P5',
            },
            'TenGigE0/0/1/2': {
                'descr': 'Non-Cisco ECINETWORKS XFP 10G Pluggable Optics Module',
                'pid': 'EN-XFP10G-LR-CO',
                'vid': 'N',
                'sn': 'B31160520008',
            },
            'TenGigE0/0/1/3': {
                'descr': 'Non-Cisco XFP 10G Pluggable Optics Module',
                'pid': 'N/A',
                'vid': 'N/A',
                'sn': '',
            },
            'module 0/1/CPU0': {
                'descr': '80G Modular Linecard, Service Edge Optimized',
                'pid': 'A9K-MOD80-SE',
                'vid': 'V11',
                'sn': 'FOC2242P17S',
            },
            'module 0/1/0': {
                'descr': 'ASR 9000 20-port 1GE Modular Port Adapter',
                'pid': 'A9K-MPA-20X1GE',
                'vid': 'V06',
                'sn': 'FOC2244NCSA',
            },
            'module mau 0/1/0/2': {
                'descr': '1000BASE-SX SFP transceiver module, MMF, 850nm, DOM',
                'pid': 'GLC-SX-MMD',
                'vid': 'V01',
                'sn': 'AGJ1821REPB',
            },
            'GigabitEthernet0/1/0/12': {
                'descr': 'Non-Cisco E.C.I.NETWORKS SFP 1G Pluggable Optics Module',
                'pid': 'EN-SFP1G-LX-CO',
                'vid': '1.0',
                'sn': 'ECI50L252',
            },
            'module 0/2/CPU0': {
                'descr': 'Cisco ASR 9000 Series SPA Interface Processor-700',
                'pid': 'A9K-SIP-700',
                'vid': 'V02',
                'sn': 'FOC1748N0B7',
            },
            'module 0/2/0': {
                'descr': '3-port OC3c SFP Optics ATM Shared Port Adapter',
                'pid': 'SPA-3XOC3-ATM-V2',
                'vid': 'V03',
                'sn': 'JP614240083',
            },
            'module mau 0/2/0/2': {
                'descr': 'OC3 SR-1/STM1 MM',
                'pid': 'SFP-OC3-MM',
                'vid': 'V01',
                'sn': 'OCP10310921',
            },
            'module 0/4/CPU0': {
                'descr': '24X10G/1G  Service Edge Optimized LC',
                'pid': 'A9K-24X10GE-1G-SE',
                'vid': 'V01',
                'sn': 'FOC2237N3Y0',
            },
            'module mau GigabitEthernet0/4/CPU0/0': {
                'descr': 'Unknown or Unsupported SFP Module',
                'pid': 'GLC-T',
                'vid': 'V04',
                'sn': 'MTC191108UW',
            },
            'module mau GigabitEthernet0/4/CPU0/1': {
                'descr': 'Unknown pluggable optics',
                'pid': 'N/A',
                'vid': 'N/A',
                'sn': 'FNS13441EZE',
            },
            'GigabitEthernet0/4/0/5': {
                'descr': 'Non-Cisco E.C.I.NETWORKS SFP 1G Pluggable Optics Module',
                'pid': 'EN-SFP1G-LX-CO',
                'vid': '1.',
                'sn': 'ECI50L009',
            },
            'GigabitEthernet0/4/0/6': {
                'descr': 'Non-Cisco E.C.I.NETWORKS SFP 1G Pluggable Optics Module',
                'pid': 'EN-SFP1G-SX-CO',
                'vid': '1.',
                'sn': 'ECI32M012',
            },
            'TenGigE0/4/0/12': {
                'descr': 'Non-Cisco LambdaGain SFP+ 10G Pluggable Optics Module',
                'pid': 'L04D-10GE-ER',
                'vid': 'N/A',
                'sn': 'FXLG021112310001',
            },
            'TenGigE0/4/0/13': {
                'descr': 'Non-Cisco E.C.I.NETWORKS SFP+ 10G Pluggable Optics Module',
                'pid': 'EN-SFP10G-LR-CO',
                'vid': '1.',
                'sn': 'ECIXPL037',
            },
            'module mau TenGigE0/4/CPU0/14': {
                'descr': '10GBASE-SR SFP+ Module for MMF',
                'pid': 'SFP-10G-SR',
                'vid': 'V03',
                'sn': 'JUR184402WK',
            },
            'module mau TenGigE0/4/CPU0/16': {
                'descr': '10GBASE-LR SFP+ Module for SMF',
                'pid': 'SFP-10G-LR',
                'vid': 'V02',
                'sn': 'FNS16201FK4',
            },
            'TenGigE0/4/0/20': {
                'descr': 'Non-Cisco FINISAR CORP. SFP+ 10G Pluggable Optics Module',
                'pid': 'FTLX1471D3BNL-J1',
                'vid': 'A',
                'sn': 'APG0MX8',
            },
            'module mau TenGigE0/4/CPU0/21': {
                'descr': '10GBASE-LR SFP+ Module for SMF',
                'pid': 'SFP-10G-LR',
                'vid': 'V02',
                'sn': 'ONT174402HM',
            },
            'TenGigE0/4/0/22': {
                'descr': 'Non-Cisco SumitomoElectric SFP+ 10G Pluggable Optics Module',
                'pid': 'SPP5200LR-J6-M',
                'vid': 'A',
                'sn': '163627A01776',
            },
            'TenGigE0/4/0/23': {
                'descr': 'Non-Cisco E.C.I.NETWORKS SFP+ 10G Pluggable Optics Module',
                'pid': 'EN-SFP10G-LR-CO',
                'vid': '1.',
                'sn': 'ECIXPL233',
            },
        },
    }

    def test_show_inventory_golden1(self):
        self.device = Mock(**self.golden_output1)
        invetory_obj1 = ShowInventory(device=self.device)
        parsed_output1 = invetory_obj1.parse()
        self.assertEqual(parsed_output1,self.golden_parsed_output1)

    def test_show_inventory_golden2(self):
        self.device = Mock(**self.golden_output2)
        invetory_obj2 = ShowInventory(device=self.device)
        parsed_output2 = invetory_obj2.parse()
        self.assertEqual(parsed_output2,self.golden_parsed_output2)
    
    def test_show_inventory_golden3(self):
        self.device = Mock(**self.golden_output3)
        invetory_obj2 = ShowInventory(device=self.device)
        parsed_output2 = invetory_obj2.parse()
        self.assertEqual(parsed_output2,self.golden_parsed_output3)

    def test_show_inventory_empty(self):
        self.device = Mock(**self.empty_output)
        invetory_obj = ShowInventory(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = invetory_obj.parse()

# =======================================
#  Unit test for admin show diag chassis'       
# =======================================

class TestAdminShowDiagChassis(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'chassis_feature': 'V2 AC PEM',
        'clei': 'IPMUP00BRB',
        'desc': 'ASR 9006 4 Line Card Slot Chassis with V2 AC PEM',
        'device_family': 'ASR',
        'device_series': '9006',
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
    
    golden_parsed_output2 = {
        'rack_num': 0,
        'desc': ' Cisco CRS Series 16 Slots Line Card Chassis',
        'device_family': 'Cisco',
        'device_series': 'CRS Series',
        'num_line_cards': 16,
        'main': {
            'board_type': '500060',
            'part': '800-25021-05 rev B0',
            'dev': '079239',
            'serial_number': 'SAD0925050J',
        },
        'pca': '73-7648-08 rev B0',
        'pid': 'CRS-MSC',
        'vid': 'V02',
        'clei': 'IPUCAC1BAA',
        'eci': '132502',
    }

    golden_output2 = {'execute.return_value': '''
        admin show diag chassis

        Mon Oct 14 17:45:40.649 EDT

        Rack 0 - Cisco CRS Series 16 Slots Line Card Chassis
        MAIN:  board type 500060
                800-25021-05 rev B0
                dev 079239
                S/N SAD0925050J
        PCA:   73-7648-08 rev B0
        PID:   CRS-MSC
        VID:   V02
        CLEI:  IPUCAC1BAA
        ECI:   132502
        RACK NUM: 0
        '''}

    device_output = {'execute.return_value': '''
        admin show diag chassis

        Mon Oct 21 10:54:18.093 EDT

        Rack 0 - CRS 16 Slots Line Card Chassis for CRS-16/S-B
          MAIN:  board type 0001ee
                 800-35128-03 rev B1
                 dev N/A
                 S/N FXS1752Q3AU
          PCA:   73-13062-02 rev A0
          PID:   CRS-16-LCC-B
          VID:   V03
          CLEI:  IPMS110DRC
          ECI:   465887
          RACK NUM: 0
        '''}

    device_parsed_output = {
        'clei': 'IPMS110DRC',
        'desc': ' CRS 16 Slots Line Card Chassis for CRS-16/S-B',
        'device_series': 'CRS',
        'eci': '465887',
        'main': {
            'board_type': '0001ee',
            'dev': 'N/A',
            'part': '800-35128-03 rev B1',
            'serial_number': 'FXS1752Q3AU',
        },
        'num_line_cards': 16,
        'pca': '73-13062-02 rev A0',
        'pid': 'CRS-16-LCC-B',
        'rack_num': 0,
        'vid': 'V03',
        'chassis_feature': 'CRS-16/S-B'
    }

    def test_show_inventory_empty(self):
        self.device = Mock(**self.empty_output)
        diag_chassis_obj = AdminShowDiagChassis(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = diag_chassis_obj.parse()

    def test_admin_show_diag_chassis_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        diag_chassis_obj1 = AdminShowDiagChassis(device=self.device)
        parsed_output1 = diag_chassis_obj1.parse()
        self.assertEqual(parsed_output1,self.golden_parsed_output1)
    
    def test_admin_show_diag_chassis_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        diag_chassis_obj1 = AdminShowDiagChassis(device=self.device)
        parsed_output1 = diag_chassis_obj1.parse()
        self.assertEqual(parsed_output1,self.golden_parsed_output2)

    def test_3(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output)
        diag_chassis_obj1 = AdminShowDiagChassis(device=self.device)
        parsed_output = diag_chassis_obj1.parse()
        self.assertEqual(parsed_output, self.device_parsed_output)

# ========================================
#  Unit test for 'show redundancy summary'       
# ========================================

class test_show_redundancy_summary(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        "redundancy_communication": True,
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

    golden_parsed_output1 = {'node': {
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
            'node_uptime': '8 minutes',
            'node_uptime_in_seconds': 480,
            'node_uptime_timestamp': 'Thu Apr 27 03:22:37 '
                                     '2017',
            'primary_rmf_state': 'not ready',
            'primary_rmf_state_reason': 'Backup is not '
                                        'Present',
            'reload_cause': 'Initiating switch-over',
            'role': 'ACTIVE',
            'time_since_last_reload': '1 hour, 16 minutes ago',
            'time_since_last_switchover': '1 minute ago',
            'valid_partner': 'no'}}}


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


# ====================
#  Unit test for 'dir'       
# ====================

class test_dir(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'dir': {
            'total_free_bytes': '939092 kbytes',
            'files':
                {'pnet_cfg.log':
                    {'permission': '-rw-r--r--', 'date': 'May 10 2017', 'index': '14', 'size': '10429'},
                 'status_file':
                    {'permission': '-rw-r--r--', 'date': 'May 10 13:15', 'index': '18', 'size': '2458'},
                 'nvgen_traces':
                    {'permission': 'drwxr-xr-x', 'date': 'May 10 14:02', 'index': '16353', 'size': '4096'},
                 'clihistory':
                    {'permission': 'drwx------', 'date': 'May 10 2017', 'index': '8177', 'size': '4096'},
                 'core':
                    {'permission': 'drwxr-xr-x', 'date': 'May 10 2017', 'index': '12', 'size': '4096'},
                 'cvac.log':
                    {'permission': '-rw-r--r--', 'date': 'May 10 2017', 'index': '20', 'size': '773'},
                 'kim':
                    {'permission': 'drwxr-xr-x', 'date': 'May 10 2017', 'index': '8178', 'size': '4096'},
                 'config -> /misc/config':
                    {'permission': 'lrwxrwxrwx', 'date': 'May 10 2017', 'index': '15', 'size': '12'},
                 'ztp':
                    {'permission': 'drwxr-xr-x', 'date': 'May 10 13:41', 'index': '8179', 'size': '4096'},
                 'lost+found':
                    {'permission': 'drwx------', 'date': 'May 10 2017', 'index': '11', 'size': '16384'},
                 'envoke_log':
                    {'permission': '-rw-r--r--', 'date': 'May 10 2017', 'index': '13', 'size': '1438'}},
            'total_bytes': '1012660 kbytes',
            'dir_name': '/misc/scratch'}}

    golden_output1 = {'execute.return_value': '''
        Directory of /misc/scratch
           15 lrwxrwxrwx 1    12 May 10  2017 config -> /misc/config
           20 -rw-r--r-- 1   773 May 10  2017 cvac.log
        16353 drwxr-xr-x 2  4096 May 10 14:02 nvgen_traces
         8179 drwxr-xr-x 9  4096 May 10 13:41 ztp
         8177 drwx------ 2  4096 May 10  2017 clihistory
           11 drwx------ 2 16384 May 10  2017 lost+found
           14 -rw-r--r-- 1 10429 May 10  2017 pnet_cfg.log
           18 -rw-r--r-- 1  2458 May 10 13:15 status_file
           12 drwxr-xr-x 2  4096 May 10  2017 core
           13 -rw-r--r-- 1  1438 May 10  2017 envoke_log
         8178 drwxr-xr-x 2  4096 May 10  2017 kim

        1012660 kbytes total (939092 kbytes free)
        '''}

    golden_parsed_output2 = {
        'dir': {
            'dir_name': 'disk0a:/usr',
            'total_bytes': '2562719744 bytes',
            'total_free_bytes': '1918621184 bytes'}}

    golden_output2 = {'execute.return_value': '''
        Directory of disk0a:/usr

        9867        -rwx  8909        Thu Jan 15 15:29:26 2015  start

        2562719744 bytes total (1918621184 bytes free)
        '''}

    golden_parsed_output3 = {
        'dir':
            {'dir_name': '/misc/scratch',
             'total_bytes': '1012660 kbytes',
             'total_free_bytes': '938440 kbytes',
             'files':
                {'fake_config.tcl':
                    {'date': 'Mar 22 08:47', 'index': '39', 'permission': '-rwxr--r--', 'size': '0'},
                 'cvac':
                    {'date': 'Mar 7 14:29', 'index': '16353', 'permission': 'drwxrwxrwx', 'size': '4096'},
                 'nvgen_traces':
                    {'date': 'Mar 7 07:22', 'index': '16354', 'permission': 'drwxr-xr-x', 'size': '4096'},
                 'ztp':
                    {'date': 'Mar 7 07:01', 'index': '8179', 'permission': 'drwxr-xr-x', 'size': '4096'},
                 'lost+found':
                    {'date': 'Mar 7 14:26', 'index': '11', 'permission': 'drwx------', 'size': '16384'},
                 'config -> /misc/config':
                    {'date': 'Mar 7 14:26', 'index': '15', 'permission': 'lrwxrwxrwx', 'size': '12'},
                 'clihistory':
                    {'date': 'Mar 7 14:27', 'index': '8177', 'permission': 'drwx---r-x', 'size': '4096'},
                 'core':
                    {'date': 'Mar 7 14:26', 'index': '12', 'permission': 'drwxr-xr-x', 'size': '4096'},
                 'cvac.log':
                    {'date': 'Mar 7 06:29', 'index': '32', 'permission': '-rw-rw-rw-', 'size': '824'},
                 'status_file':
                    {'date': 'Mar 12 14:35', 'index': '41', 'permission': '-rw-r--r--', 'size': '1985'},
                 'kim':
                    {'date': 'Mar 7 14:27', 'index': '8178', 'permission': 'drwxr-xr-x', 'size': '4096'},
                 'oor_aware_process':
                    {'date': 'Mar 7 06:34', 'index': '16', 'permission': '-rw-r--r--', 'size': '98'},
                 'fake_config_2.tcl':
                    {'date': 'Mar 22 08:58', 'index': '43', 'permission': '-rwxr--r--', 'size': '0'},
                 '.python-history':
                    {'date': 'Mar 20 11:08', 'index': '42', 'permission': '-rw-------', 'size': '0'},
                 'pnet_cfg.log':
                    {'date': 'Mar 7 14:26', 'index': '14', 'permission': '-rw-r--r--', 'size': '10429'},
                 'envoke_log':
                    {'date': 'Mar 7 14:26', 'index': '13', 'permission': '-rw-r--r--', 'size': '1438'}}}}

    golden_output3 = {'execute.return_value': '''
        Directory of /misc/scratch
           32 -rw-rw-rw- 1   824 Mar  7 06:29 cvac.log
           43 -rwxr--r-- 1     0 Mar 22 08:58 fake_config_2.tcl
           41 -rw-r--r-- 1  1985 Mar 12 14:35 status_file
           13 -rw-r--r-- 1  1438 Mar  7 14:26 envoke_log
           16 -rw-r--r-- 1    98 Mar  7 06:34 oor_aware_process
         8178 drwxr-xr-x 2  4096 Mar  7 14:27 kim
         8177 drwx---r-x 2  4096 Mar  7 14:27 clihistory
           15 lrwxrwxrwx 1    12 Mar  7 14:26 config -> /misc/config
           39 -rwxr--r-- 1     0 Mar 22 08:47 fake_config.tcl
           12 drwxr-xr-x 2  4096 Mar  7 14:26 core
           14 -rw-r--r-- 1 10429 Mar  7 14:26 pnet_cfg.log
           11 drwx------ 2 16384 Mar  7 14:26 lost+found
         8179 drwxr-xr-x 8  4096 Mar  7 07:01 ztp
           42 -rw------- 1     0 Mar 20 11:08 .python-history
        16354 drwxr-xr-x 2  4096 Mar  7 07:22 nvgen_traces
        16353 drwxrwxrwx 3  4096 Mar  7 14:29 cvac

        1012660 kbytes total (938440 kbytes free)
        '''}

    def test_dir_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        dir_obj1 = Dir(device=self.device)
        parsed_output1 = dir_obj1.parse()
        self.assertEqual(parsed_output1,self.golden_parsed_output1)

    def test_dir_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        dir_obj2 = Dir(device=self.device)
        parsed_output2 = dir_obj2.parse()
        self.assertEqual(parsed_output2,self.golden_parsed_output2)

    def test_dir_golden2_with_arg(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        dir_obj2 = Dir(device=self.device)
        parsed_output2 = dir_obj2.parse(directory='disk0a:/usr')
        self.assertEqual(parsed_output2,self.golden_parsed_output2)

    def test_dir_golden3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        dir_obj3 = Dir(device=self.device)
        parsed_output3 = dir_obj3.parse()
        self.assertEqual(parsed_output3,self.golden_parsed_output3)

    def test_dir_empty(self):
        self.device = Mock(**self.empty_output)
        dir_obj = Dir(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = dir_obj.parse()


# ==============================================
#  Unit test for 'show install inactive summary'
# ==============================================

class test_show_install_inactive_summary(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'sdr': ['Owner'],
        'inactive_packages': ['disk0:asr9k-diags-3.7.2']}

    golden_output1 = {'execute.return_value': '''
        Default Profile:
            SDRs:
            Owner
            Inactive Packages:
                disk0:asr9k-diags-3.7.2
    '''}

    golden_parsed_output2 = {
        'sdr': ['Owner'],
        'inactive_packages': ['disk0:c12k-diags-3.7.2',
                              "Install operation 30 'install remove disk0:hfr-diags-3.7.2 test' started by",
                              "user 'lab' at 23:40:22 UTC Sat Apr 15 2009.",
                              "Warning:  No changes will occur due to 'test' option being specified. The",
                              'Warning:  following is the predicted output for this install command.',
                              'Info:     This operation will remove the following package:',
                              'Info:         disk0:c12k-diags-3.7.2',
                              'Info:     After this install remove the following install rollback points will',
                              'Info:     no longer be reachable, as the required packages will not be present:',
                              'Info:         4, 9, 10, 14, 15, 17, 18',
                              'Proceed with removing these packages? [confirm] y',
                              'The install operation will continue asynchronously.',
                              'Install operation 30 completed successfully at 23.',
                              '-3.7.2.07I.CSCsr09575-1.0.0 pause sw-change',
                              "Install operation 12 '(admin) install deactivate",
                              "disk0:comp-c12k-3.7.2.07I.CSCsr09575-1.0.0 pause sw-change'",
                              "started by user 'admin' via CLI at 09:06:26 BST Mon Jul 07 2009.",
                              'Info: This operation will reload the following nodes in parallel:',
                              'The install operation will continue asynchronously.',
                              'Info: Install Method: Parallel Reload',
                              'Info: Install operation 12 is pausing before the config lock is applied for',
                              'Info:    the software change as requested by the user.',
                              'Info: No further install operations will be allowed until the operation is resumed.',
                              'Info: Please continue the operation using one of the following steps:',
                              "Info: - run the command '(admin) install operation 12 complete'.",
                              "Info: - run the command '(admin) install operation 12 attach synchronous' and then",
                              'Info:      answer the query.']}

    golden_output2 = {'execute.return_value': '''
        RP/0/0/CPU0:router(admin)#show install inactive summary
        RP/0/0/CPU0:router(admin)# install activate
          disk0:c12k-mini-px-4.3.99
                
        
        RP/0/0/CPU0:router(admin)# install verify packages
        
        RP/0/0/CPU0:router(admin)# exit
                
        Default Profile:
          SDRs:
          Owner
          Inactive Packages:
            disk0:c12k-diags-3.7.2
        
        RP/0/0/CPU0:router(admin)#install remove disk0:c12k-diags-3.7.2 test
        
        Install operation 30 'install remove disk0:hfr-diags-3.7.2 test' started by
        user 'lab' at 23:40:22 UTC Sat Apr 15 2009.
        Warning:  No changes will occur due to 'test' option being specified. The
        Warning:  following is the predicted output for this install command.
        Info:     This operation will remove the following package:
        Info:         disk0:c12k-diags-3.7.2
        Info:     After this install remove the following install rollback points will
        Info:     no longer be reachable, as the required packages will not be present:
        Info:         4, 9, 10, 14, 15, 17, 18
        Proceed with removing these packages? [confirm] y
        
        The install operation will continue asynchronously.
        Install operation 30 completed successfully at 23.
        
        RP/0/0/CPU0:router(admin)#install deactivate disk0:comp-c12k
        -3.7.2.07I.CSCsr09575-1.0.0 pause sw-change
        
        Install operation 12 '(admin) install deactivate
          disk0:comp-c12k-3.7.2.07I.CSCsr09575-1.0.0 pause sw-change'
          started by user 'admin' via CLI at 09:06:26 BST Mon Jul 07 2009.
        Info: This operation will reload the following nodes in parallel:
        Info: 0/0/CPU0 (RP) (SDR: Owner)
        Info: 0/1/CPU0 (LC(E3-GE-4)) (SDR: Owner)
        Info: 0/5/CPU0 (LC(E3-OC3-POS-4)) (SDR: Owner)
        Proceed with this install operation (y/n)? [y]
        The install operation will continue asynchronously.
        Info: Install Method: Parallel Reload
        Info: Install operation 12 is pausing before the config lock is applied for
        Info:    the software change as requested by the user.
        Info: No further install operations will be allowed until the operation is resumed.
        Info: Please continue the operation using one of the following steps:
        Info: - run the command '(admin) install operation 12 complete'.
        Info: - run the command '(admin) install operation 12 attach synchronous' and then
        Info:      answer the query.
    '''}

    def test_show_install_inactive_summary_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowInstallInactiveSummary(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_install_inactive_summary_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowInstallInactiveSummary(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_install_inactive_summary_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowInstallInactiveSummary(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


# ==============================================
#  Unit test for 'show install commit summary'
# ==============================================

class test_show_install_commit_summary(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'sdr': ['Owner',
                'Owner'],
        'committed_packages': ['disk0:asr9k-services-infra-5.3.3',
                               'disk0:asr9k-9000v-nV-px-5.3.3',
                               'disk0:asr9k-k9sec-px-5.3.3',
                               'disk0:asr9k-mpls-px-5.3.3',
                               'disk0:asr9k-li-px-5.3.3',
                               'disk0:asr9k-optic-px-5.3.3',
                               'disk0:asr9k-bng-px-5.3.3',
                               'disk0:asr9k-mcast-px-5.3.3',
                               'disk0:asr9k-doc-px-5.3.3',
                               'disk0:asr9k-mgbl-px-5.3.3',
                               'disk0:asr9k-services-px-5.3.3',
                               'disk0:asr9k-fpd-px-5.3.3',
                               'disk0:asr9k-mini-px-5.3.3',
                               'disk0:asr9k-video-px-5.3.3',
                               'disk0:asr9k-asr901-nV-px-5.3.',
                               'Default Profile:',
                               'Admin Resources',
                               'disk0:hfr-asr9000v-nV-px-5.3.3',
                               'disk0:hfr-diags-px-5.3.3',
                               'disk0:hfr-doc-px-5.3.3',
                               'disk0:hfr-fpd-px-5.3.3',
                               'disk0:hfr-k9sec-px-5.3.3',
                               'disk0:hfr-li-px-5.3.3',
                               'disk0:hfr-mcast-px-5.3.3',
                               'disk0:hfr-mgbl-px-5.3.3',
                               'disk0:hfr-mini-px-5.3.3',
                               'disk0:hfr-mpls-px-5.3.3',
                               'disk0:hfr-services-px-5.3.3',
                               'disk0:hfr-video-px-5.3.3',
                               'disk0:hfr-px-5.3.3.CSCuy08977-1.0.0',
                               'disk0:hfr-px-5.3.3.CSCuz68269-1.0.0',
                               'disk0:hfr-px-5.3.3.CSCuz75928-1.0.0',
                               'disk0:hfr-px-5.3.3.CSCva10822-1.0.0',
                               'disk0:hfr-px-5.3.3.CSCva10837-1.0.0',
                               'disk0:hfr-px-5.3.3.CSCva10886-1.0.0',
                               'disk0:hfr-px-5.3.3.CSCva10910-1.0.0',
                               'disk0:hfr-px-5.3.3.CSCva10928-1.0.0',
                               'disk0:hfr-px-5.3.3.CSCva10941-1.0.0',
                               'disk0:hfr-px-5.3.3.CSCva11056-1.0.0']}

    golden_output1 = {'execute.return_value': '''
        RP/0/RSP0/CPU0:router# show install commit summary
            SDRs:
                Owner
            Committed Packages:
                disk0:asr9k-services-infra-5.3.3
                disk0:asr9k-9000v-nV-px-5.3.3
                disk0:asr9k-k9sec-px-5.3.3
                disk0:asr9k-mpls-px-5.3.3
                disk0:asr9k-li-px-5.3.3
                disk0:asr9k-optic-px-5.3.3
                disk0:asr9k-bng-px-5.3.3
                disk0:asr9k-mcast-px-5.3.3
                disk0:asr9k-doc-px-5.3.3
                disk0:asr9k-mgbl-px-5.3.3
                disk0:asr9k-services-px-5.3.3
                disk0:asr9k-fpd-px-5.3.3
                disk0:asr9k-mini-px-5.3.3
                disk0:asr9k-video-px-5.3.3
                disk0:asr9k-asr901-nV-px-5.3.

        Default Profile:
        Admin Resources
            SDRs:
                Owner
            Committed Packages:
                disk0:hfr-asr9000v-nV-px-5.3.3
                disk0:hfr-diags-px-5.3.3
                disk0:hfr-doc-px-5.3.3
                disk0:hfr-fpd-px-5.3.3
                disk0:hfr-k9sec-px-5.3.3
                disk0:hfr-li-px-5.3.3
                disk0:hfr-mcast-px-5.3.3
                disk0:hfr-mgbl-px-5.3.3
                disk0:hfr-mini-px-5.3.3
                disk0:hfr-mpls-px-5.3.3
                disk0:hfr-services-px-5.3.3
                disk0:hfr-video-px-5.3.3
                disk0:hfr-px-5.3.3.CSCuy08977-1.0.0
                disk0:hfr-px-5.3.3.CSCuz68269-1.0.0
                disk0:hfr-px-5.3.3.CSCuz75928-1.0.0
                disk0:hfr-px-5.3.3.CSCva10822-1.0.0
                disk0:hfr-px-5.3.3.CSCva10837-1.0.0
                disk0:hfr-px-5.3.3.CSCva10886-1.0.0
                disk0:hfr-px-5.3.3.CSCva10910-1.0.0
                disk0:hfr-px-5.3.3.CSCva10928-1.0.0
                disk0:hfr-px-5.3.3.CSCva10941-1.0.0
                disk0:hfr-px-5.3.3.CSCva11056-1.0.0
    '''}

    golden_parsed_output2 = {
        'sdr': ['Owner'],
        'active_packages': ['disk0:asr9k-services-infra-6.0.2',
                            'disk0:asr9k-9000v-nV-px-6.0.2',
                            'disk0:asr9k-li-px-6.0.2',
                            'disk0:asr9k-ncs500x-nV-px-6.0.2',
                            'disk0:asr9k-bng-px-6.0.2',
                            'disk0:asr9k-mcast-px-6.0.2',
                            'disk0:asr9k-optic-px-6.0.2',
                            'disk0:asr9k-doc-px-6.0.2',
                            'disk0:asr9k-mgbl-px-6.0.2',
                            'disk0:asr9k-fpd-px-6.0.2',
                            'disk0:asr9k-mini-px-6.0.2',
                            'disk0:asr9k-services-px-6.0.2',
                            'disk0:asr9k-infra-test-px-6.0.2',
                            'disk0:asr9k-video-px-6.0.2',
                            'disk0:asr9k-mpls-px-6.0.2',
                            'disk0:asr9k-k9sec-px-6.0.2']}

    golden_output2 = {'execute.return_value': '''
        RP/0/RSP0/CPU0:router# show install commit summary
        Default Profile:
            SDRs:
                Owner
            Active Packages:
                disk0:asr9k-services-infra-6.0.2
                disk0:asr9k-9000v-nV-px-6.0.2
                disk0:asr9k-li-px-6.0.2
                disk0:asr9k-ncs500x-nV-px-6.0.2
                disk0:asr9k-bng-px-6.0.2
                disk0:asr9k-mcast-px-6.0.2
                disk0:asr9k-optic-px-6.0.2
                disk0:asr9k-doc-px-6.0.2
                disk0:asr9k-mgbl-px-6.0.2
                disk0:asr9k-fpd-px-6.0.2
                disk0:asr9k-mini-px-6.0.2
                disk0:asr9k-services-px-6.0.2
                disk0:asr9k-infra-test-px-6.0.2
                disk0:asr9k-video-px-6.0.2
                disk0:asr9k-mpls-px-6.0.2
                disk0:asr9k-k9sec-px-6.0.2
    '''}

    def test_show_install_commit_summary_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowInstallCommitSummary(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_install_commit_summary_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowInstallCommitSummary(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_install_commit_summary_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowInstallCommitSummary(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


if __name__ == '__main__':
    unittest.main()
