# Python
import re
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Parser
from genie.libs.parser.iosxr.show_platform import (ShowRedundancy,
                                                   ShowPlatformVm,
                                                   ShowPlatform,
                                                   ShowSdrDetail,
                                                   ShowInstallActiveSummary,
                                                   ShowInventory,
                                                   ShowRedundancySummary,
                                                   AdminShowDiagChassis,
                                                   ShowVersion,
                                                   Dir,
                                                   ShowInstallInactiveSummary,
                                                   ShowInstallCommitSummary,
                                                   ShowProcessesMemory,
                                                   ShowProcessesMemoryDetail)

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# ==============================
#  Unit test for 'show version'       
# ==============================

class TestShowVersion(unittest.TestCase):
    
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

class TestShowSdrDetail(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'sdr_id': {
            0: {
                'dsdrsc_node': '0/RSP0/CPU0',
                'dsdrsc_partner_node': '0/RSP1/CPU0',
                'mac_address': 'a80c.0dff.0b76',
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
                mac addr             : a80c.0dff.0b76



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
                'mac_address': '025e.eaff.fb57',
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
                mac addr             : 025e.eaff.fb57



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

class TestShowPlatform(unittest.TestCase):
    
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
                    'state': 'IOS XR RUN'}},
            'oc': {
                '0/PT0': {
                    'name': 'A9K-DC-PEM',
                    'full_slot': '0/PT0',
                    'state': 'OPERATIONAL',
                    'config_state': 'NSHUT'
                }}}}

    golden_output5 = {'execute.return_value': '''
        Node            Type                      State            Config State
        -----------------------------------------------------------------------------
        0/RSP0/CPU0     A9K-RSP440-TR(Active)     IOS XR RUN       PWR,NSHUT,MON
        0/RSP1/CPU0     A9K-RSP440-TR(Standby)    IOS XR RUN       PWR,NSHUT,MON
        0/0/0           A9K-MPA-20X1GE            OK               PWR,NSHUT,MON
        0/0/1           A9K-MQA-20X2GE            OK               PWR,NSHUT,MON
        0/0/2           A9K-MRA-20X3GE            OK               PWR,NSHUT,MON
        0/0/CPU0        A9K-MOD80-SE              IOS XR RUN       PWR,NSHUT,MON
        0/PT0           A9K-DC-PEM                OPERATIONAL      NSHUT
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

class TestShowPlatformVm(unittest.TestCase):
    
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

class TestShowInstallActiveSummary(unittest.TestCase):
    
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

class TestShowInventory(unittest.TestCase):
    
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

    golden_output3 = {'execute.return_value': '''

        Diag Information For : 
        0 Rack 0-IDPROM Info
            Product ID      : NCS-5501
            VID             : V01
            Serial Number   : FOC23158XXX
            CLEI Code       : INM1J10ARA
            Part Number     : 73-101057-02
            Part Revision   : D0
            H/W Version     : 1.0
        Top Assembly Block:
            Serial Number   : FOC231XXXHW
            Part Number     : 68-6098-01
            Part Revision   : F0
            Mfg Deviation   : 0
            H/W Version     : 1.0
            Mfg Bits        : 1
    '''
    }

    golden_parsed_output3 = {
        'clei': 'INM1J10ARA',
        'hw_version': '1.0',
        'part_number': '73-101057-02',
        'part_revision': 'D0',
        'pid': 'NCS-5501',
        'rack_num': 0,
        'sn': 'FOC23158XXX',
        'top_assembly_block': {
            'hw_version': '1.0',
            'mfg_bits': '1',
            'mfg_deviation': '0',
            'part_number': '68-6098-01',
            'part_revision': 'F0',
            'serial_number': 'FOC231XXXHW'
        },
        'vid': 'V01'
    }

    golden_output4 = {'execute.return_value': '''
        Rack 0-IDPROM Info
            PID                      : ASR-9901
            Version Identifier       : V01
            Top Assy. Part Number    : 00-0000-00
            Chassis Serial Number    : FOC2202PFWL
            CLEI Code                : INM4710ARA
    '''
    }

    golden_parsed_output4 = {
        'rack_num': 0,
        'pid': 'ASR-9901',
        'vid': 'V01',
        'top_assembly_block': {
            'part_number': '00-0000-00'
        },
        'sn': 'FOC2202PFWL',
        'clei': 'INM4710ARA'
    }

    golden_output5 = {'execute.return_value': '''
        RP/0/RP0/CPU0:ios#admin show diag chassis
        Tue Sep 22 23:23:54.013 UTC
        
        Diag Information For : 0
        
        Rack 0-Chassis IDPROM Info
            Controller Family        : 0009
            Controller Type          : 09d2
            PID                      : NCS1004
            Version Identifier       : V01
            UDI Description          : Network Convergence System 1004 4 line card slots
            CLEI Code                : WOMS400GRA
            Top Assy. Part Number    : 800-47655-01
            Top Assy. Revision       : A0
            PCB Serial Number        : CAT2311B0AK
        RP/0/RP0/CPU0:ios#
    '''
    }
    golden_parsed_output5 = {
        'clei': 'WOMS400GRA',
        'controller_family': '0009',
        'controller_type': '09d2',
        'desc': 'Network Convergence System 1004 4 line card slots',
        'pid': 'NCS1004',
        'rack_num': 0,
        'sn': 'CAT2311B0AK',
        'top_assembly_block': {
            'part_number': '800-47655-01',
            'revision': 'A0',
        },
        'vid': 'V01',
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

    def test_admin_show_diag_chassis_golden3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        obj = AdminShowDiagChassis(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output3)

    def test_admin_show_diag_chassis_golden4(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output4)
        obj = AdminShowDiagChassis(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output4)

    def test_admin_show_diag_chassis_golden5(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output5)
        obj = AdminShowDiagChassis(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output5)

# ========================================
#  Unit test for 'show redundancy summary'       
# ========================================

class TestShowRedundancySummary(unittest.TestCase):
    
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

class TestShowRedundancy(unittest.TestCase):
    
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

class TestDir(unittest.TestCase):
    
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

    golden_parsed_output2 =  {
        'dir': {
            'dir_name': 'disk0a:/usr',
            'files': {
                'start': {
                    'date': 'Thu Jan 15 15:29:26 2015',
                    'index': '9867',
                    'permission': '-rwx',
                    'size': '8909'
                }
            },
           'total_bytes': '2562719744 bytes',
           'total_free_bytes': '1918621184 bytes'
        }
    }


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

    golden_output4 = {'execute.return_value': '''
        dir disk0:/prod2_vxlan_config
        Mon May 18 21:31:29.857 PDT

        Directory of disk0:

        10541310    -rwx  6142        Mon May 18 19:16:01 2020  prod2_vxlan_config

        12810436608 bytes total (12134223872 bytes free)
    '''
    }

    golden_parsed_output4 = {
        'dir': {
            'dir_name': 'disk0:',
            'files': {
                'prod2_vxlan_config': {
                    'date': 'Mon May 18 19:16:01 2020',
                    'index': '10541310',
                    'permission': '-rwx',
                    'size': '6142'
                }
            },
            'total_bytes': '12810436608 bytes',
            'total_free_bytes': '12134223872 bytes'
        }
    }

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

    def test_dir_golden4(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output4)
        dir_obj4 = Dir(device=self.device)
        parsed_output4 = dir_obj4.parse()
        self.assertEqual(parsed_output4,self.golden_parsed_output4)

    def test_dir_empty(self):
        self.device = Mock(**self.empty_output)
        dir_obj = Dir(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = dir_obj.parse()


# ==============================================
#  Unit test for 'show install inactive summary'
# ==============================================

class TestShowInstallInactiveSummary(unittest.TestCase):

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

class TestShowInstallCommitSummary(unittest.TestCase):
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


class TestShowProcessesMemory(unittest.TestCase):
    
    maxDiff = None
    dev = Device(name='ASR9K')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'jid': {1: {'index': {1: {'data': 344,
                           'dynamic': 0,
                           'jid': 1,
                           'process': 'init',
                           'stack': 136,
                           'text': 296}}},
         51: {'index': {1: {'data': 1027776,
                            'dynamic': 5668,
                            'jid': 51,
                            'process': 'processmgr',
                            'stack': 136,
                            'text': 1372}}},
         53: {'index': {1: {'data': 342500,
                            'dynamic': 7095,
                            'jid': 53,
                            'process': 'dsr',
                            'stack': 136,
                            'text': 32}}},
         111: {'index': {1: {'data': 531876,
                             'dynamic': 514,
                             'jid': 111,
                             'process': 'devc-conaux-aux',
                             'stack': 136,
                             'text': 8}}},
         112: {'index': {1: {'data': 861144,
                             'dynamic': 957,
                             'jid': 112,
                             'process': 'qsm',
                             'stack': 136,
                             'text': 144}}},
         113: {'index': {1: {'data': 400776,
                             'dynamic': 671,
                             'jid': 113,
                             'process': 'spp',
                             'stack': 136,
                             'text': 328}}},
         114: {'index': {1: {'data': 531912,
                             'dynamic': 545,
                             'jid': 114,
                             'process': 'devc-conaux-con',
                             'stack': 136,
                             'text': 8}}},
         115: {'index': {1: {'data': 662452,
                             'dynamic': 366,
                             'jid': 115,
                             'process': 'syslogd_helper',
                             'stack': 136,
                             'text': 52}}},
         118: {'index': {1: {'data': 200748,
                             'dynamic': 426,
                             'jid': 118,
                             'process': 'shmwin_svr',
                             'stack': 136,
                             'text': 56}}},
         119: {'index': {1: {'data': 397880,
                             'dynamic': 828,
                             'jid': 119,
                             'process': 'syslog_dev',
                             'stack': 136,
                             'text': 12}}},
         121: {'index': {1: {'data': 470008,
                             'dynamic': 6347,
                             'jid': 121,
                             'process': 'calv_alarm_mgr',
                             'stack': 136,
                             'text': 504}}},
         122: {'index': {1: {'data': 1003480,
                             'dynamic': 2838,
                             'jid': 122,
                             'process': 'udp',
                             'stack': 136,
                             'text': 180}}},
         123: {'index': {1: {'data': 529852,
                             'dynamic': 389,
                             'jid': 123,
                             'process': 'enf_broker',
                             'stack': 136,
                             'text': 40}}},
         124: {'index': {1: {'data': 200120,
                             'dynamic': 351,
                             'jid': 124,
                             'process': 'procfs_server',
                             'stack': 168,
                             'text': 20}}},
         125: {'index': {1: {'data': 333592,
                             'dynamic': 1506,
                             'jid': 125,
                             'process': 'pifibm_server_rp',
                             'stack': 136,
                             'text': 312}}},
         126: {'index': {1: {'data': 399332,
                             'dynamic': 305,
                             'jid': 126,
                             'process': 'ltrace_sync',
                             'stack': 136,
                             'text': 28}}},
         127: {'index': {1: {'data': 797548,
                             'dynamic': 2573,
                             'jid': 127,
                             'process': 'ifindex_server',
                             'stack': 136,
                             'text': 96}}},
         128: {'index': {1: {'data': 532612,
                             'dynamic': 3543,
                             'jid': 128,
                             'process': 'eem_ed_test',
                             'stack': 136,
                             'text': 44}}},
         130: {'index': {1: {'data': 200120,
                             'dynamic': 257,
                             'jid': 130,
                             'process': 'igmp_policy_reg_agent',
                             'stack': 136,
                             'text': 8}}},
         132: {'index': {1: {'data': 200628,
                             'dynamic': 280,
                             'jid': 132,
                             'process': 'show_mediang_edm',
                             'stack': 136,
                             'text': 20}}},
         134: {'index': {1: {'data': 466168,
                             'dynamic': 580,
                             'jid': 134,
                             'process': 'ipv4_acl_act_agent',
                             'stack': 136,
                             'text': 28}}},
         136: {'index': {1: {'data': 997196,
                             'dynamic': 5618,
                             'jid': 136,
                             'process': 'resmon',
                             'stack': 136,
                             'text': 188}}},
         137: {'index': {1: {'data': 534184,
                             'dynamic': 2816,
                             'jid': 137,
                             'process': 'bundlemgr_local',
                             'stack': 136,
                             'text': 612}}},
         138: {'index': {1: {'data': 200652,
                             'dynamic': 284,
                             'jid': 138,
                             'process': 'chkpt_proxy',
                             'stack': 136,
                             'text': 16}}},
         139: {'index': {1: {'data': 200120,
                             'dynamic': 257,
                             'jid': 139,
                             'process': 'lisp_xr_policy_reg_agent',
                             'stack': 136,
                             'text': 8}}},
         141: {'index': {1: {'data': 200648,
                             'dynamic': 246,
                             'jid': 141,
                             'process': 'linux_nto_misc_showd',
                             'stack': 136,
                             'text': 20}}},
         143: {'index': {1: {'data': 200644,
                             'dynamic': 247,
                             'jid': 143,
                             'process': 'procfind',
                             'stack': 136,
                             'text': 20}}},
         146: {'index': {1: {'data': 200240,
                             'dynamic': 275,
                             'jid': 146,
                             'process': 'bgp_policy_reg_agent',
                             'stack': 136,
                             'text': 28}}},
         147: {'index': {1: {'data': 201332,
                             'dynamic': 418,
                             'jid': 147,
                             'process': 'type6_server',
                             'stack': 136,
                             'text': 68}}},
         149: {'index': {1: {'data': 663524,
                             'dynamic': 1297,
                             'jid': 149,
                             'process': 'clns',
                             'stack': 136,
                             'text': 188}}},
         152: {'index': {1: {'data': 532616,
                             'dynamic': 3541,
                             'jid': 152,
                             'process': 'eem_ed_none',
                             'stack': 136,
                             'text': 52}}},
         154: {'index': {1: {'data': 729896,
                             'dynamic': 1046,
                             'jid': 154,
                             'process': 'ipv4_acl_mgr',
                             'stack': 136,
                             'text': 140}}},
         155: {'index': {1: {'data': 200120,
                             'dynamic': 261,
                             'jid': 155,
                             'process': 'ospf_policy_reg_agent',
                             'stack': 136,
                             'text': 12}}},
         157: {'index': {1: {'data': 200908,
                             'dynamic': 626,
                             'jid': 157,
                             'process': 'ssh_key_server',
                             'stack': 136,
                             'text': 44}}},
         158: {'index': {1: {'data': 200628,
                             'dynamic': 285,
                             'jid': 158,
                             'process': 'heap_summary_edm',
                             'stack': 136,
                             'text': 20}}},
         161: {'index': {1: {'data': 200640,
                             'dynamic': 297,
                             'jid': 161,
                             'process': 'cmp_edm',
                             'stack': 136,
                             'text': 16}}},
         162: {'index': {1: {'data': 267456,
                             'dynamic': 693,
                             'jid': 162,
                             'process': 'ip_aps',
                             'stack': 136,
                             'text': 52}}},
         166: {'index': {1: {'data': 935480,
                             'dynamic': 8194,
                             'jid': 166,
                             'process': 'mpls_lsd',
                             'stack': 136,
                             'text': 1108}}},
         167: {'index': {1: {'data': 730776,
                             'dynamic': 3649,
                             'jid': 167,
                             'process': 'ipv6_ma',
                             'stack': 136,
                             'text': 540}}},
         168: {'index': {1: {'data': 266788,
                             'dynamic': 589,
                             'jid': 168,
                             'process': 'nd_partner',
                             'stack': 136,
                             'text': 36}}},
         169: {'index': {1: {'data': 735000,
                             'dynamic': 6057,
                             'jid': 169,
                             'process': 'ipsub_ma',
                             'stack': 136,
                             'text': 680}}},
         171: {'index': {1: {'data': 266432,
                             'dynamic': 530,
                             'jid': 171,
                             'process': 'shelf_mgr_proxy',
                             'stack': 136,
                             'text': 16}}},
         172: {'index': {1: {'data': 200604,
                             'dynamic': 253,
                             'jid': 172,
                             'process': 'early_fast_discard_verifier',
                             'stack': 136,
                             'text': 16}}},
         174: {'index': {1: {'data': 200096,
                             'dynamic': 256,
                             'jid': 174,
                             'process': 'bundlemgr_checker',
                             'stack': 136,
                             'text': 56}}},
         175: {'index': {1: {'data': 200120,
                             'dynamic': 248,
                             'jid': 175,
                             'process': 'syslog_infra_hm',
                             'stack': 136,
                             'text': 12}}},
         177: {'index': {1: {'data': 200112,
                             'dynamic': 241,
                             'jid': 177,
                             'process': 'meminfo_svr',
                             'stack': 136,
                             'text': 8}}},
         178: {'index': {1: {'data': 468272,
                             'dynamic': 2630,
                             'jid': 178,
                             'process': 'accounting_ma',
                             'stack': 136,
                             'text': 264}}},
         180: {'index': {1: {'data': 1651090,
                             'dynamic': 242,
                             'jid': 180,
                             'process': 'aipc_cleaner',
                             'stack': 136,
                             'text': 8}}},
         181: {'index': {1: {'data': 201280,
                             'dynamic': 329,
                             'jid': 181,
                             'process': 'nsr_ping_reply',
                             'stack': 136,
                             'text': 16}}},
         182: {'index': {1: {'data': 334236,
                             'dynamic': 843,
                             'jid': 182,
                             'process': 'spio_ma',
                             'stack': 136,
                             'text': 4}}},
         183: {'index': {1: {'data': 266788,
                             'dynamic': 607,
                             'jid': 183,
                             'process': 'statsd_server',
                             'stack': 136,
                             'text': 40}}},
         184: {'index': {1: {'data': 407016,
                             'dynamic': 8579,
                             'jid': 184,
                             'process': 'subdb_svr',
                             'stack': 136,
                             'text': 368}}},
         186: {'index': {1: {'data': 932992,
                             'dynamic': 3072,
                             'jid': 186,
                             'process': 'smartlicserver',
                             'stack': 136,
                             'text': 16}}},
         187: {'index': {1: {'data': 200120,
                             'dynamic': 259,
                             'jid': 187,
                             'process': 'rip_policy_reg_agent',
                             'stack': 136,
                             'text': 8}}},
         188: {'index': {1: {'data': 533704,
                             'dynamic': 3710,
                             'jid': 188,
                             'process': 'eem_ed_nd',
                             'stack': 136,
                             'text': 60}}},
         189: {'index': {1: {'data': 401488,
                             'dynamic': 3499,
                             'jid': 189,
                             'process': 'ifmgr',
                             'stack': 136,
                             'text': 4}}},
         190: {'index': {1: {'data': 1001552,
                             'dynamic': 3082,
                             'jid': 190,
                             'process': 'rdsfs_svr',
                             'stack': 136,
                             'text': 196}}},
         191: {'index': {1: {'data': 398300,
                             'dynamic': 632,
                             'jid': 191,
                             'process': 'hostname_sync',
                             'stack': 136,
                             'text': 12}}},
         192: {'index': {1: {'data': 466168,
                             'dynamic': 570,
                             'jid': 192,
                             'process': 'l2vpn_policy_reg_agent',
                             'stack': 136,
                             'text': 20}}},
         193: {'index': {1: {'data': 665096,
                             'dynamic': 1405,
                             'jid': 193,
                             'process': 'ntpd',
                             'stack': 136,
                             'text': 344}}},
         194: {'index': {1: {'data': 794692,
                             'dynamic': 2629,
                             'jid': 194,
                             'process': 'nrssvr',
                             'stack': 136,
                             'text': 180}}},
         195: {'index': {1: {'data': 531776,
                             'dynamic': 748,
                             'jid': 195,
                             'process': 'ipv4_io',
                             'stack': 136,
                             'text': 256}}},
         196: {'index': {1: {'data': 200624,
                             'dynamic': 274,
                             'jid': 196,
                             'process': 'domain_sync',
                             'stack': 136,
                             'text': 16}}},
         197: {'index': {1: {'data': 1015252,
                             'dynamic': 21870,
                             'jid': 197,
                             'process': 'parser_server',
                             'stack': 136,
                             'text': 304}}},
         198: {'index': {1: {'data': 532612,
                             'dynamic': 3540,
                             'jid': 198,
                             'process': 'eem_ed_config',
                             'stack': 136,
                             'text': 56}}},
         199: {'index': {1: {'data': 200648,
                             'dynamic': 282,
                             'jid': 199,
                             'process': 'cerrno_server',
                             'stack': 136,
                             'text': 48}}},
         200: {'index': {1: {'data': 531264,
                             'dynamic': 1810,
                             'jid': 200,
                             'process': 'ipv4_arm',
                             'stack': 136,
                             'text': 344}}},
         201: {'index': {1: {'data': 268968,
                             'dynamic': 1619,
                             'jid': 201,
                             'process': 'session_mon',
                             'stack': 136,
                             'text': 68}}},
         202: {'index': {1: {'data': 864208,
                             'dynamic': 3472,
                             'jid': 202,
                             'process': 'netio',
                             'stack': 136,
                             'text': 292}}},
         204: {'index': {1: {'data': 268932,
                             'dynamic': 2122,
                             'jid': 204,
                             'process': 'ether_caps_partner',
                             'stack': 136,
                             'text': 152}}},
         205: {'index': {1: {'data': 201168,
                             'dynamic': 254,
                             'jid': 205,
                             'process': 'sunstone_stats_svr',
                             'stack': 136,
                             'text': 28}}},
         206: {'index': {1: {'data': 794684,
                             'dynamic': 2967,
                             'jid': 206,
                             'process': 'sysdb_shared_nc',
                             'stack': 136,
                             'text': 4}}},
         207: {'index': {1: {'data': 601736,
                             'dynamic': 2823,
                             'jid': 207,
                             'process': 'yang_server',
                             'stack': 136,
                             'text': 268}}},
         208: {'index': {1: {'data': 200096,
                             'dynamic': 251,
                             'jid': 208,
                             'process': 'ipodwdm',
                             'stack': 136,
                             'text': 16}}},
         209: {'index': {1: {'data': 200656,
                             'dynamic': 253,
                             'jid': 209,
                             'process': 'crypto_edm',
                             'stack': 136,
                             'text': 24}}},
         210: {'index': {1: {'data': 878632,
                             'dynamic': 13237,
                             'jid': 210,
                             'process': 'nvgen_server',
                             'stack': 136,
                             'text': 244}}},
         211: {'index': {1: {'data': 334080,
                             'dynamic': 2169,
                             'jid': 211,
                             'process': 'pfilter_ma',
                             'stack': 136,
                             'text': 228}}},
         213: {'index': {1: {'data': 531840,
                             'dynamic': 1073,
                             'jid': 213,
                             'process': 'kim',
                             'stack': 136,
                             'text': 428}}},
         216: {'index': {1: {'data': 267224,
                             'dynamic': 451,
                             'jid': 216,
                             'process': 'showd_lc',
                             'stack': 136,
                             'text': 64}}},
         217: {'index': {1: {'data': 406432,
                             'dynamic': 4666,
                             'jid': 217,
                             'process': 'pppoe_ma',
                             'stack': 136,
                             'text': 520}}},
         218: {'index': {1: {'data': 664484,
                             'dynamic': 2602,
                             'jid': 218,
                             'process': 'l2rib',
                             'stack': 136,
                             'text': 484}}},
         220: {'index': {1: {'data': 598812,
                             'dynamic': 3443,
                             'jid': 220,
                             'process': 'eem_ed_syslog',
                             'stack': 136,
                             'text': 60}}},
         221: {'index': {1: {'data': 267264,
                             'dynamic': 290,
                             'jid': 221,
                             'process': 'lpts_fm',
                             'stack': 136,
                             'text': 52}}},
         222: {'index': {1: {'data': 205484,
                             'dynamic': 5126,
                             'jid': 222,
                             'process': 'mpa_fm_svr',
                             'stack': 136,
                             'text': 12}}},
         243: {'index': {1: {'data': 267576,
                             'dynamic': 990,
                             'jid': 243,
                             'process': 'spio_ea',
                             'stack': 136,
                             'text': 8}}},
         244: {'index': {1: {'data': 200632,
                             'dynamic': 247,
                             'jid': 244,
                             'process': 'mempool_edm',
                             'stack': 136,
                             'text': 8}}},
         245: {'index': {1: {'data': 532624,
                             'dynamic': 3541,
                             'jid': 245,
                             'process': 'eem_ed_counter',
                             'stack': 136,
                             'text': 48}}},
         247: {'index': {1: {'data': 1010268,
                             'dynamic': 1923,
                             'jid': 247,
                             'process': 'cfgmgr-rp',
                             'stack': 136,
                             'text': 344}}},
         248: {'index': {1: {'data': 465260,
                             'dynamic': 1243,
                             'jid': 248,
                             'process': 'alarm-logger',
                             'stack': 136,
                             'text': 104}}},
         249: {'index': {1: {'data': 797376,
                             'dynamic': 1527,
                             'jid': 249,
                             'process': 'locald_DLRSC',
                             'stack': 136,
                             'text': 604}}},
         250: {'index': {1: {'data': 265800,
                             'dynamic': 438,
                             'jid': 250,
                             'process': 'lcp_mgr',
                             'stack': 136,
                             'text': 12}}},
         251: {'index': {1: {'data': 265840,
                             'dynamic': 712,
                             'jid': 251,
                             'process': 'tamfs',
                             'stack': 136,
                             'text': 32}}},
         252: {'index': {1: {'data': 531384,
                             'dynamic': 7041,
                             'jid': 252,
                             'process': 'sysdb_svr_local',
                             'stack': 136,
                             'text': 4}}},
         253: {'index': {1: {'data': 200672,
                             'dynamic': 256,
                             'jid': 253,
                             'process': 'tty_show_users_edm',
                             'stack': 136,
                             'text': 32}}},
         254: {'index': {1: {'data': 534032,
                             'dynamic': 4463,
                             'jid': 254,
                             'process': 'eem_ed_generic',
                             'stack': 136,
                             'text': 96}}},
         255: {'index': {1: {'data': 201200,
                             'dynamic': 409,
                             'jid': 255,
                             'process': 'ipv6_acl_cfg_agent',
                             'stack': 136,
                             'text': 32}}},
         256: {'index': {1: {'data': 334104,
                             'dynamic': 756,
                             'jid': 256,
                             'process': 'mpls_vpn_mib',
                             'stack': 136,
                             'text': 156}}},
         257: {'index': {1: {'data': 267888,
                             'dynamic': 339,
                             'jid': 257,
                             'process': 'bundlemgr_adj',
                             'stack': 136,
                             'text': 156}}},
         258: {'index': {1: {'data': 1651090,
                             'dynamic': 244,
                             'jid': 258,
                             'process': 'file_paltx',
                             'stack': 136,
                             'text': 16}}},
         259: {'index': {1: {'data': 1000600,
                             'dynamic': 6088,
                             'jid': 259,
                             'process': 'ipv6_nd',
                             'stack': 136,
                             'text': 1016}}},
         260: {'index': {1: {'data': 533044,
                             'dynamic': 1793,
                             'jid': 260,
                             'process': 'sdr_instagt',
                             'stack': 136,
                             'text': 260}}},
         261: {'index': {1: {'data': 334860,
                             'dynamic': 806,
                             'jid': 261,
                             'process': 'ipsec_pp',
                             'stack': 136,
                             'text': 220}}},
         266: {'index': {1: {'data': 266344,
                             'dynamic': 717,
                             'jid': 266,
                             'process': 'pm_server',
                             'stack': 136,
                             'text': 92}}},
         267: {'index': {1: {'data': 598760,
                             'dynamic': 2768,
                             'jid': 267,
                             'process': 'object_tracking',
                             'stack': 136,
                             'text': 204}}},
         268: {'index': {1: {'data': 200700,
                             'dynamic': 417,
                             'jid': 268,
                             'process': 'wdsysmon_fd_edm',
                             'stack': 136,
                             'text': 20}}},
         269: {'index': {1: {'data': 664752,
                             'dynamic': 2513,
                             'jid': 269,
                             'process': 'eth_mgmt',
                             'stack': 136,
                             'text': 60}}},
         270: {'index': {1: {'data': 200064,
                             'dynamic': 257,
                             'jid': 270,
                             'process': 'gcp_fib_verifier',
                             'stack': 136,
                             'text': 20}}},
         271: {'index': {1: {'data': 400624,
                             'dynamic': 2348,
                             'jid': 271,
                             'process': 'rsi_agent',
                             'stack': 136,
                             'text': 580}}},
         272: {'index': {1: {'data': 794692,
                             'dynamic': 1425,
                             'jid': 272,
                             'process': 'nrssvr_global',
                             'stack': 136,
                             'text': 180}}},
         273: {'index': {1: {'data': 494124,
                             'dynamic': 19690,
                             'jid': 273,
                             'process': 'invmgr_proxy',
                             'stack': 136,
                             'text': 112}}},
         275: {'index': {1: {'data': 199552,
                             'dynamic': 264,
                             'jid': 275,
                             'process': 'nsr_fo',
                             'stack': 136,
                             'text': 12}}},
         276: {'index': {1: {'data': 202328,
                             'dynamic': 436,
                             'jid': 276,
                             'process': 'mpls_fwd_show_proxy',
                             'stack': 136,
                             'text': 204}}},
         277: {'index': {1: {'data': 267112,
                             'dynamic': 688,
                             'jid': 277,
                             'process': 'tam_sync',
                             'stack': 136,
                             'text': 44}}},
         278: {'index': {1: {'data': 200120,
                             'dynamic': 259,
                             'jid': 278,
                             'process': 'mldp_policy_reg_agent',
                             'stack': 136,
                             'text': 8}}},
         290: {'index': {1: {'data': 200640,
                             'dynamic': 262,
                             'jid': 290,
                             'process': 'sh_proc_mem_edm',
                             'stack': 136,
                             'text': 20}}},
         291: {'index': {1: {'data': 794684,
                             'dynamic': 3678,
                             'jid': 291,
                             'process': 'sysdb_shared_sc',
                             'stack': 136,
                             'text': 4}}},
         293: {'index': {1: {'data': 200120,
                             'dynamic': 259,
                             'jid': 293,
                             'process': 'pim6_policy_reg_agent',
                             'stack': 136,
                             'text': 8}}},
         294: {'index': {1: {'data': 267932,
                             'dynamic': 1495,
                             'jid': 294,
                             'process': 'issumgr',
                             'stack': 136,
                             'text': 560}}},
         295: {'index': {1: {'data': 266744,
                             'dynamic': 296,
                             'jid': 295,
                             'process': 'vlan_ea',
                             'stack': 136,
                             'text': 220}}},
         296: {'index': {1: {'data': 796404,
                             'dynamic': 1902,
                             'jid': 296,
                             'process': 'correlatord',
                             'stack': 136,
                             'text': 292}}},
         297: {'index': {1: {'data': 201304,
                             'dynamic': 367,
                             'jid': 297,
                             'process': 'imaedm_server',
                             'stack': 136,
                             'text': 56}}},
         298: {'index': {1: {'data': 200224,
                             'dynamic': 246,
                             'jid': 298,
                             'process': 'ztp_cfg',
                             'stack': 136,
                             'text': 12}}},
         299: {'index': {1: {'data': 268000,
                             'dynamic': 459,
                             'jid': 299,
                             'process': 'ipv6_ea',
                             'stack': 136,
                             'text': 92}}},
         301: {'index': {1: {'data': 200644,
                             'dynamic': 250,
                             'jid': 301,
                             'process': 'sysmgr_show_proc_all_edm',
                             'stack': 136,
                             'text': 88}}},
         303: {'index': {1: {'data': 399360,
                             'dynamic': 882,
                             'jid': 303,
                             'process': 'tftp_fs',
                             'stack': 136,
                             'text': 68}}},
         304: {'index': {1: {'data': 202220,
                             'dynamic': 306,
                             'jid': 304,
                             'process': 'ncd',
                             'stack': 136,
                             'text': 32}}},
         305: {'index': {1: {'data': 1001716,
                             'dynamic': 9508,
                             'jid': 305,
                             'process': 'gsp',
                             'stack': 136,
                             'text': 1096}}},
         306: {'index': {1: {'data': 794684,
                             'dynamic': 1792,
                             'jid': 306,
                             'process': 'sysdb_svr_admin',
                             'stack': 136,
                             'text': 4}}},
         308: {'index': {1: {'data': 333172,
                             'dynamic': 538,
                             'jid': 308,
                             'process': 'devc-vty',
                             'stack': 136,
                             'text': 8}}},
         309: {'index': {1: {'data': 1012628,
                             'dynamic': 9404,
                             'jid': 309,
                             'process': 'tcp',
                             'stack': 136,
                             'text': 488}}},
         310: {'index': {1: {'data': 333572,
                             'dynamic': 2092,
                             'jid': 310,
                             'process': 'daps',
                             'stack': 136,
                             'text': 512}}},
         312: {'index': {1: {'data': 200620,
                             'dynamic': 283,
                             'jid': 312,
                             'process': 'ipv6_assembler',
                             'stack': 136,
                             'text': 36}}},
         313: {'index': {1: {'data': 199844,
                             'dynamic': 551,
                             'jid': 313,
                             'process': 'ssh_key_client',
                             'stack': 136,
                             'text': 48}}},
         314: {'index': {1: {'data': 332076,
                             'dynamic': 371,
                             'jid': 314,
                             'process': 'timezone_config',
                             'stack': 136,
                             'text': 28}}},
         316: {'index': {1: {'data': 531560,
                             'dynamic': 2016,
                             'jid': 316,
                             'process': 'bcdls',
                             'stack': 136,
                             'text': 112}}},
         317: {'index': {1: {'data': 531560,
                             'dynamic': 2015,
                             'jid': 317,
                             'process': 'bcdls',
                             'stack': 136,
                             'text': 112}}},
         318: {'index': {1: {'data': 532344,
                             'dynamic': 2874,
                             'jid': 318,
                             'process': 'bcdls',
                             'stack': 136,
                             'text': 112}}},
         319: {'index': {1: {'data': 532344,
                             'dynamic': 2874,
                             'jid': 319,
                             'process': 'bcdls',
                             'stack': 136,
                             'text': 112}}},
         320: {'index': {1: {'data': 531556,
                             'dynamic': 2013,
                             'jid': 320,
                             'process': 'bcdls',
                             'stack': 136,
                             'text': 112}}},
         326: {'index': {1: {'data': 398256,
                             'dynamic': 348,
                             'jid': 326,
                             'process': 'sld',
                             'stack': 136,
                             'text': 116}}},
         327: {'index': {1: {'data': 997196,
                             'dynamic': 3950,
                             'jid': 327,
                             'process': 'eem_policy_dir',
                             'stack': 136,
                             'text': 268}}},
         329: {'index': {1: {'data': 267464,
                             'dynamic': 434,
                             'jid': 329,
                             'process': 'mpls_io_ea',
                             'stack': 136,
                             'text': 108}}},
         332: {'index': {1: {'data': 332748,
                             'dynamic': 276,
                             'jid': 332,
                             'process': 'redstatsd',
                             'stack': 136,
                             'text': 20}}},
         333: {'index': {1: {'data': 799488,
                             'dynamic': 4511,
                             'jid': 333,
                             'process': 'rsi_master',
                             'stack': 136,
                             'text': 404}}},
         334: {'index': {1: {'data': 333648,
                             'dynamic': 351,
                             'jid': 334,
                             'process': 'sconbkup',
                             'stack': 136,
                             'text': 12}}},
         336: {'index': {1: {'data': 199440,
                             'dynamic': 204,
                             'jid': 336,
                             'process': 'pam_manager',
                             'stack': 136,
                             'text': 12}}},
         337: {'index': {1: {'data': 600644,
                             'dynamic': 3858,
                             'jid': 337,
                             'process': 'nve_mgr',
                             'stack': 136,
                             'text': 204}}},
         339: {'index': {1: {'data': 266800,
                             'dynamic': 679,
                             'jid': 339,
                             'process': 'rmf_svr',
                             'stack': 136,
                             'text': 140}}},
         341: {'index': {1: {'data': 465864,
                             'dynamic': 1145,
                             'jid': 341,
                             'process': 'ipv6_io',
                             'stack': 136,
                             'text': 160}}},
         342: {'index': {1: {'data': 864468,
                             'dynamic': 1011,
                             'jid': 342,
                             'process': 'syslogd',
                             'stack': 136,
                             'text': 224}}},
         343: {'index': {1: {'data': 663932,
                             'dynamic': 1013,
                             'jid': 343,
                             'process': 'ipv6_acl_daemon',
                             'stack': 136,
                             'text': 212}}},
         344: {'index': {1: {'data': 996048,
                             'dynamic': 2352,
                             'jid': 344,
                             'process': 'plat_sl_client',
                             'stack': 136,
                             'text': 108}}},
         346: {'index': {1: {'data': 598152,
                             'dynamic': 778,
                             'jid': 346,
                             'process': 'cinetd',
                             'stack': 136,
                             'text': 136}}},
         347: {'index': {1: {'data': 200648,
                             'dynamic': 261,
                             'jid': 347,
                             'process': 'debug_d',
                             'stack': 136,
                             'text': 24}}},
         349: {'index': {1: {'data': 200612,
                             'dynamic': 284,
                             'jid': 349,
                             'process': 'debug_d_admin',
                             'stack': 136,
                             'text': 20}}},
         350: {'index': {1: {'data': 399188,
                             'dynamic': 1344,
                             'jid': 350,
                             'process': 'vm-monitor',
                             'stack': 136,
                             'text': 72}}},
         352: {'index': {1: {'data': 465844,
                             'dynamic': 1524,
                             'jid': 352,
                             'process': 'lpts_pa',
                             'stack': 136,
                             'text': 308}}},
         353: {'index': {1: {'data': 1002896,
                             'dynamic': 5160,
                             'jid': 353,
                             'process': 'call_home',
                             'stack': 136,
                             'text': 728}}},
         355: {'index': {1: {'data': 994116,
                             'dynamic': 7056,
                             'jid': 355,
                             'process': 'eem_server',
                             'stack': 136,
                             'text': 292}}},
         356: {'index': {1: {'data': 200720,
                             'dynamic': 396,
                             'jid': 356,
                             'process': 'tcl_secure_mode',
                             'stack': 136,
                             'text': 8}}},
         357: {'index': {1: {'data': 202040,
                             'dynamic': 486,
                             'jid': 357,
                             'process': 'tamsvcs_tamm',
                             'stack': 136,
                             'text': 36}}},
         359: {'index': {1: {'data': 531256,
                             'dynamic': 1788,
                             'jid': 359,
                             'process': 'ipv6_arm',
                             'stack': 136,
                             'text': 328}}},
         360: {'index': {1: {'data': 201196,
                             'dynamic': 363,
                             'jid': 360,
                             'process': 'fwd_driver_partner',
                             'stack': 136,
                             'text': 88}}},
         361: {'index': {1: {'data': 533872,
                             'dynamic': 2637,
                             'jid': 361,
                             'process': 'ipv6_mfwd_partner',
                             'stack': 136,
                             'text': 836}}},
         362: {'index': {1: {'data': 932680,
                             'dynamic': 3880,
                             'jid': 362,
                             'process': 'arp',
                             'stack': 136,
                             'text': 728}}},
         363: {'index': {1: {'data': 202024,
                             'dynamic': 522,
                             'jid': 363,
                             'process': 'cepki',
                             'stack': 136,
                             'text': 96}}},
         364: {'index': {1: {'data': 1001736,
                             'dynamic': 4343,
                             'jid': 364,
                             'process': 'fib_mgr',
                             'stack': 136,
                             'text': 3580}}},
         365: {'index': {1: {'data': 269016,
                             'dynamic': 2344,
                             'jid': 365,
                             'process': 'pim_ma',
                             'stack': 136,
                             'text': 56}}},
         368: {'index': {1: {'data': 1002148,
                             'dynamic': 3111,
                             'jid': 368,
                             'process': 'raw_ip',
                             'stack': 136,
                             'text': 124}}},
         369: {'index': {1: {'data': 464272,
                             'dynamic': 625,
                             'jid': 369,
                             'process': 'ltrace_server',
                             'stack': 136,
                             'text': 40}}},
         371: {'index': {1: {'data': 200572,
                             'dynamic': 279,
                             'jid': 371,
                             'process': 'netio_debug_partner',
                             'stack': 136,
                             'text': 24}}},
         372: {'index': {1: {'data': 200120,
                             'dynamic': 259,
                             'jid': 372,
                             'process': 'pim_policy_reg_agent',
                             'stack': 136,
                             'text': 8}}},
         373: {'index': {1: {'data': 333240,
                             'dynamic': 1249,
                             'jid': 373,
                             'process': 'policymgr_rp',
                             'stack': 136,
                             'text': 592}}},
         375: {'index': {1: {'data': 200624,
                             'dynamic': 290,
                             'jid': 375,
                             'process': 'loopback_caps_partner',
                             'stack': 136,
                             'text': 32}}},
         376: {'index': {1: {'data': 467420,
                             'dynamic': 3815,
                             'jid': 376,
                             'process': 'eem_ed_sysmgr',
                             'stack': 136,
                             'text': 76}}},
         377: {'index': {1: {'data': 333636,
                             'dynamic': 843,
                             'jid': 377,
                             'process': 'mpls_io',
                             'stack': 136,
                             'text': 140}}},
         378: {'index': {1: {'data': 200120,
                             'dynamic': 258,
                             'jid': 378,
                             'process': 'ospfv3_policy_reg_agent',
                             'stack': 136,
                             'text': 8}}},
         380: {'index': {1: {'data': 333604,
                             'dynamic': 520,
                             'jid': 380,
                             'process': 'fhrp_output',
                             'stack': 136,
                             'text': 124}}},
         381: {'index': {1: {'data': 533872,
                             'dynamic': 2891,
                             'jid': 381,
                             'process': 'ipv4_mfwd_partner',
                             'stack': 136,
                             'text': 828}}},
         382: {'index': {1: {'data': 465388,
                             'dynamic': 538,
                             'jid': 382,
                             'process': 'packet',
                             'stack': 136,
                             'text': 132}}},
         383: {'index': {1: {'data': 333284,
                             'dynamic': 359,
                             'jid': 383,
                             'process': 'dumper',
                             'stack': 136,
                             'text': 40}}},
         384: {'index': {1: {'data': 200636,
                             'dynamic': 244,
                             'jid': 384,
                             'process': 'showd_server',
                             'stack': 136,
                             'text': 12}}},
         385: {'index': {1: {'data': 603424,
                             'dynamic': 3673,
                             'jid': 385,
                             'process': 'ipsec_mp',
                             'stack': 136,
                             'text': 592}}},
         388: {'index': {1: {'data': 729160,
                             'dynamic': 836,
                             'jid': 388,
                             'process': 'bcdl_agent',
                             'stack': 136,
                             'text': 176}}},
         389: {'index': {1: {'data': 729880,
                             'dynamic': 1066,
                             'jid': 389,
                             'process': 'bcdl_agent',
                             'stack': 136,
                             'text': 176}}},
         390: {'index': {1: {'data': 663828,
                             'dynamic': 1384,
                             'jid': 390,
                             'process': 'bcdl_agent',
                             'stack': 136,
                             'text': 176}}},
         391: {'index': {1: {'data': 795416,
                             'dynamic': 1063,
                             'jid': 391,
                             'process': 'bcdl_agent',
                             'stack': 136,
                             'text': 176}}},
         401: {'index': {1: {'data': 466148,
                             'dynamic': 579,
                             'jid': 401,
                             'process': 'es_acl_act_agent',
                             'stack': 136,
                             'text': 20}}},
         402: {'index': {1: {'data': 597352,
                             'dynamic': 1456,
                             'jid': 402,
                             'process': 'vi_config_replicator',
                             'stack': 136,
                             'text': 40}}},
         403: {'index': {1: {'data': 532624,
                             'dynamic': 3546,
                             'jid': 403,
                             'process': 'eem_ed_timer',
                             'stack': 136,
                             'text': 64}}},
         405: {'index': {1: {'data': 664196,
                             'dynamic': 2730,
                             'jid': 405,
                             'process': 'pm_collector',
                             'stack': 136,
                             'text': 732}}},
         406: {'index': {1: {'data': 868076,
                             'dynamic': 5739,
                             'jid': 406,
                             'process': 'ppp_ma',
                             'stack': 136,
                             'text': 1268}}},
         407: {'index': {1: {'data': 794684,
                             'dynamic': 1753,
                             'jid': 407,
                             'process': 'sysdb_shared_data_nc',
                             'stack': 136,
                             'text': 4}}},
         408: {'index': {1: {'data': 415316,
                             'dynamic': 16797,
                             'jid': 408,
                             'process': 'statsd_manager_l',
                             'stack': 136,
                             'text': 4}}},
         409: {'index': {1: {'data': 946780,
                             'dynamic': 16438,
                             'jid': 409,
                             'process': 'iedged',
                             'stack': 136,
                             'text': 1824}}},
         411: {'index': {1: {'data': 542460,
                             'dynamic': 17658,
                             'jid': 411,
                             'process': 'sysdb_mc',
                             'stack': 136,
                             'text': 388}}},
         412: {'index': {1: {'data': 1003624,
                             'dynamic': 5783,
                             'jid': 412,
                             'process': 'l2fib_mgr',
                             'stack': 136,
                             'text': 1808}}},
         413: {'index': {1: {'data': 401532,
                             'dynamic': 2851,
                             'jid': 413,
                             'process': 'aib',
                             'stack': 136,
                             'text': 256}}},
         414: {'index': {1: {'data': 266776,
                             'dynamic': 440,
                             'jid': 414,
                             'process': 'rmf_cli_edm',
                             'stack': 136,
                             'text': 32}}},
         415: {'index': {1: {'data': 399116,
                             'dynamic': 895,
                             'jid': 415,
                             'process': 'ether_sock',
                             'stack': 136,
                             'text': 28}}},
         416: {'index': {1: {'data': 200980,
                             'dynamic': 275,
                             'jid': 416,
                             'process': 'shconf-edm',
                             'stack': 136,
                             'text': 32}}},
         417: {'index': {1: {'data': 532108,
                             'dynamic': 3623,
                             'jid': 417,
                             'process': 'eem_ed_stats',
                             'stack': 136,
                             'text': 60}}},
         418: {'index': {1: {'data': 532288,
                             'dynamic': 2306,
                             'jid': 418,
                             'process': 'ipv4_ma',
                             'stack': 136,
                             'text': 540}}},
         419: {'index': {1: {'data': 689020,
                             'dynamic': 15522,
                             'jid': 419,
                             'process': 'sdr_invmgr',
                             'stack': 136,
                             'text': 144}}},
         420: {'index': {1: {'data': 466456,
                             'dynamic': 1661,
                             'jid': 420,
                             'process': 'http_client',
                             'stack': 136,
                             'text': 96}}},
         421: {'index': {1: {'data': 201152,
                             'dynamic': 285,
                             'jid': 421,
                             'process': 'pak_capture_partner',
                             'stack': 136,
                             'text': 16}}},
         422: {'index': {1: {'data': 200016,
                             'dynamic': 267,
                             'jid': 422,
                             'process': 'bag_schema_svr',
                             'stack': 136,
                             'text': 36}}},
         424: {'index': {1: {'data': 604932,
                             'dynamic': 8135,
                             'jid': 424,
                             'process': 'issudir',
                             'stack': 136,
                             'text': 212}}},
         425: {'index': {1: {'data': 466796,
                             'dynamic': 1138,
                             'jid': 425,
                             'process': 'l2snoop',
                             'stack': 136,
                             'text': 104}}},
         426: {'index': {1: {'data': 331808,
                             'dynamic': 444,
                             'jid': 426,
                             'process': 'ssm_process',
                             'stack': 136,
                             'text': 56}}},
         427: {'index': {1: {'data': 200120,
                             'dynamic': 245,
                             'jid': 427,
                             'process': 'media_server',
                             'stack': 136,
                             'text': 16}}},
         428: {'index': {1: {'data': 267340,
                             'dynamic': 432,
                             'jid': 428,
                             'process': 'ip_app',
                             'stack': 136,
                             'text': 48}}},
         429: {'index': {1: {'data': 269032,
                             'dynamic': 2344,
                             'jid': 429,
                             'process': 'pim6_ma',
                             'stack': 136,
                             'text': 56}}},
         431: {'index': {1: {'data': 200416,
                             'dynamic': 390,
                             'jid': 431,
                             'process': 'local_sock',
                             'stack': 136,
                             'text': 16}}},
         432: {'index': {1: {'data': 265704,
                             'dynamic': 269,
                             'jid': 432,
                             'process': 'crypto_monitor',
                             'stack': 136,
                             'text': 68}}},
         433: {'index': {1: {'data': 597624,
                             'dynamic': 1860,
                             'jid': 433,
                             'process': 'ema_server_sdr',
                             'stack': 136,
                             'text': 112}}},
         434: {'index': {1: {'data': 200120,
                             'dynamic': 259,
                             'jid': 434,
                             'process': 'isis_policy_reg_agent',
                             'stack': 136,
                             'text': 8}}},
         435: {'index': {1: {'data': 200120,
                             'dynamic': 261,
                             'jid': 435,
                             'process': 'eigrp_policy_reg_agent',
                             'stack': 136,
                             'text': 12}}},
         437: {'index': {1: {'data': 794096,
                             'dynamic': 776,
                             'jid': 437,
                             'process': 'cdm_rs',
                             'stack': 136,
                             'text': 80}}},
         1003: {'index': {1: {'data': 798196,
                              'dynamic': 3368,
                              'jid': 1003,
                              'process': 'eigrp',
                              'stack': 136,
                              'text': 936}}},
         1011: {'index': {1: {'data': 1006776,
                              'dynamic': 8929,
                              'jid': 1011,
                              'process': 'isis',
                              'stack': 136,
                              'text': 4888}}},
         1012: {'index': {1: {'data': 1006776,
                              'dynamic': 8925,
                              'jid': 1012,
                              'process': 'isis',
                              'stack': 136,
                              'text': 4888}}},
         1027: {'index': {1: {'data': 1012376,
                              'dynamic': 14258,
                              'jid': 1027,
                              'process': 'ospf',
                              'stack': 136,
                              'text': 2880}}},
         1046: {'index': {1: {'data': 804288,
                              'dynamic': 8673,
                              'jid': 1046,
                              'process': 'ospfv3',
                              'stack': 136,
                              'text': 1552}}},
         1066: {'index': {1: {'data': 333188,
                              'dynamic': 1084,
                              'jid': 1066,
                              'process': 'autorp_candidate_rp',
                              'stack': 136,
                              'text': 52}}},
         1067: {'index': {1: {'data': 532012,
                              'dynamic': 1892,
                              'jid': 1067,
                              'process': 'autorp_map_agent',
                              'stack': 136,
                              'text': 84}}},
         1071: {'index': {1: {'data': 998992,
                              'dynamic': 5498,
                              'jid': 1071,
                              'process': 'msdp',
                              'stack': 136,
                              'text': 484}}},
         1074: {'index': {1: {'data': 599436,
                              'dynamic': 1782,
                              'jid': 1074,
                              'process': 'rip',
                              'stack': 136,
                              'text': 296}}},
         1078: {'index': {1: {'data': 1045796,
                              'dynamic': 40267,
                              'jid': 1078,
                              'process': 'bgp',
                              'stack': 136,
                              'text': 2408}}},
         1093: {'index': {1: {'data': 668844,
                              'dynamic': 3577,
                              'jid': 1093,
                              'process': 'bpm',
                              'stack': 136,
                              'text': 716}}},
         1101: {'index': {1: {'data': 266776,
                              'dynamic': 602,
                              'jid': 1101,
                              'process': 'cdp_mgr',
                              'stack': 136,
                              'text': 24}}},
         1113: {'index': {1: {'data': 200096,
                              'dynamic': 251,
                              'jid': 1113,
                              'process': 'eigrp_uv',
                              'stack': 136,
                              'text': 48}}},
         1114: {'index': {1: {'data': 1084008,
                              'dynamic': 45594,
                              'jid': 1114,
                              'process': 'emsd',
                              'stack': 136,
                              'text': 10636}}},
         1128: {'index': {1: {'data': 200156,
                              'dynamic': 284,
                              'jid': 1128,
                              'process': 'isis_uv',
                              'stack': 136,
                              'text': 84}}},
         1130: {'index': {1: {'data': 599144,
                              'dynamic': 2131,
                              'jid': 1130,
                              'process': 'lldp_agent',
                              'stack': 136,
                              'text': 412}}},
         1135: {'index': {1: {'data': 1052648,
                              'dynamic': 24083,
                              'jid': 1135,
                              'process': 'netconf',
                              'stack': 136,
                              'text': 772}}},
         1136: {'index': {1: {'data': 600036,
                              'dynamic': 795,
                              'jid': 1136,
                              'process': 'netconf_agent_tty',
                              'stack': 136,
                              'text': 20}}},
         1139: {'index': {1: {'data': 200092,
                              'dynamic': 259,
                              'jid': 1139,
                              'process': 'ospf_uv',
                              'stack': 136,
                              'text': 48}}},
         1140: {'index': {1: {'data': 200092,
                              'dynamic': 258,
                              'jid': 1140,
                              'process': 'ospfv3_uv',
                              'stack': 136,
                              'text': 32}}},
         1147: {'index': {1: {'data': 808524,
                              'dynamic': 5098,
                              'jid': 1147,
                              'process': 'sdr_mgbl_proxy',
                              'stack': 136,
                              'text': 464}}},
         1221: {'index': {1: {'data': 200848,
                              'dynamic': 503,
                              'jid': 1221,
                              'process': 'ssh_conf_verifier',
                              'stack': 136,
                              'text': 32}}},
         1233: {'index': {1: {'data': 399212,
                              'dynamic': 1681,
                              'jid': 1233,
                              'process': 'mpls_static',
                              'stack': 136,
                              'text': 252}}},
         1234: {'index': {1: {'data': 464512,
                              'dynamic': 856,
                              'jid': 1234,
                              'process': 'lldp_mgr',
                              'stack': 136,
                              'text': 100}}},
         1235: {'index': {1: {'data': 665416,
                              'dynamic': 1339,
                              'jid': 1235,
                              'process': 'intf_mgbl',
                              'stack': 136,
                              'text': 212}}},
         1236: {'index': {1: {'data': 546924,
                              'dynamic': 17047,
                              'jid': 1236,
                              'process': 'statsd_manager_g',
                              'stack': 136,
                              'text': 4}}},
         1237: {'index': {1: {'data': 201996,
                              'dynamic': 1331,
                              'jid': 1237,
                              'process': 'ipv4_mfwd_ma',
                              'stack': 136,
                              'text': 144}}},
         1238: {'index': {1: {'data': 1015244,
                              'dynamic': 22504,
                              'jid': 1238,
                              'process': 'ipv4_rib',
                              'stack': 136,
                              'text': 1008}}},
         1239: {'index': {1: {'data': 201364,
                              'dynamic': 341,
                              'jid': 1239,
                              'process': 'ipv6_mfwd_ma',
                              'stack': 136,
                              'text': 136}}},
         1240: {'index': {1: {'data': 951448,
                              'dynamic': 26381,
                              'jid': 1240,
                              'process': 'ipv6_rib',
                              'stack': 136,
                              'text': 1160}}},
         1241: {'index': {1: {'data': 873952,
                              'dynamic': 11135,
                              'jid': 1241,
                              'process': 'mrib',
                              'stack': 136,
                              'text': 1536}}},
         1242: {'index': {1: {'data': 873732,
                              'dynamic': 11043,
                              'jid': 1242,
                              'process': 'mrib6',
                              'stack': 136,
                              'text': 1516}}},
         1243: {'index': {1: {'data': 800236,
                              'dynamic': 3444,
                              'jid': 1243,
                              'process': 'policy_repository',
                              'stack': 136,
                              'text': 472}}},
         1244: {'index': {1: {'data': 399440,
                              'dynamic': 892,
                              'jid': 1244,
                              'process': 'ipv4_mpa',
                              'stack': 136,
                              'text': 160}}},
         1245: {'index': {1: {'data': 399444,
                              'dynamic': 891,
                              'jid': 1245,
                              'process': 'ipv6_mpa',
                              'stack': 136,
                              'text': 160}}},
         1246: {'index': {1: {'data': 200664,
                              'dynamic': 261,
                              'jid': 1246,
                              'process': 'eth_gl_cfg',
                              'stack': 136,
                              'text': 20}}},
         1247: {'index': {1: {'data': 941936,
                              'dynamic': 13246,
                              'jid': 1247,
                              'process': 'igmp',
                              'stack': 144,
                              'text': 980}}},
         1248: {'index': {1: {'data': 267440,
                              'dynamic': 677,
                              'jid': 1248,
                              'process': 'ipv4_connected',
                              'stack': 136,
                              'text': 4}}},
         1249: {'index': {1: {'data': 267424,
                              'dynamic': 677,
                              'jid': 1249,
                              'process': 'ipv4_local',
                              'stack': 136,
                              'text': 4}}},
         1250: {'index': {1: {'data': 267436,
                              'dynamic': 680,
                              'jid': 1250,
                              'process': 'ipv6_connected',
                              'stack': 136,
                              'text': 4}}},
         1251: {'index': {1: {'data': 267420,
                              'dynamic': 681,
                              'jid': 1251,
                              'process': 'ipv6_local',
                              'stack': 136,
                              'text': 4}}},
         1252: {'index': {1: {'data': 940472,
                              'dynamic': 12973,
                              'jid': 1252,
                              'process': 'mld',
                              'stack': 136,
                              'text': 928}}},
         1253: {'index': {1: {'data': 1018740,
                              'dynamic': 22744,
                              'jid': 1253,
                              'process': 'pim',
                              'stack': 136,
                              'text': 4424}}},
         1254: {'index': {1: {'data': 1017788,
                              'dynamic': 22444,
                              'jid': 1254,
                              'process': 'pim6',
                              'stack': 136,
                              'text': 4544}}},
         1255: {'index': {1: {'data': 799148,
                              'dynamic': 4916,
                              'jid': 1255,
                              'process': 'bundlemgr_distrib',
                              'stack': 136,
                              'text': 2588}}},
         1256: {'index': {1: {'data': 999524,
                              'dynamic': 7871,
                              'jid': 1256,
                              'process': 'bfd',
                              'stack': 136,
                              'text': 1512}}},
         1257: {'index': {1: {'data': 268092,
                              'dynamic': 1903,
                              'jid': 1257,
                              'process': 'bgp_epe',
                              'stack': 136,
                              'text': 60}}},
         1258: {'index': {1: {'data': 268016,
                              'dynamic': 493,
                              'jid': 1258,
                              'process': 'domain_services',
                              'stack': 136,
                              'text': 136}}},
         1259: {'index': {1: {'data': 201184,
                              'dynamic': 272,
                              'jid': 1259,
                              'process': 'ethernet_stats_controller_edm',
                              'stack': 136,
                              'text': 32}}},
         1260: {'index': {1: {'data': 399868,
                              'dynamic': 874,
                              'jid': 1260,
                              'process': 'ftp_fs',
                              'stack': 136,
                              'text': 64}}},
         1261: {'index': {1: {'data': 206536,
                              'dynamic': 2468,
                              'jid': 1261,
                              'process': 'python_process_manager',
                              'stack': 136,
                              'text': 12}}},
         1262: {'index': {1: {'data': 200360,
                              'dynamic': 421,
                              'jid': 1262,
                              'process': 'tty_verifyd',
                              'stack': 136,
                              'text': 8}}},
         1263: {'index': {1: {'data': 265924,
                              'dynamic': 399,
                              'jid': 1263,
                              'process': 'ipv4_rump',
                              'stack': 136,
                              'text': 60}}},
         1264: {'index': {1: {'data': 265908,
                              'dynamic': 394,
                              'jid': 1264,
                              'process': 'ipv6_rump',
                              'stack': 136,
                              'text': 108}}},
         1265: {'index': {1: {'data': 729900,
                              'dynamic': 1030,
                              'jid': 1265,
                              'process': 'es_acl_mgr',
                              'stack': 136,
                              'text': 56}}},
         1266: {'index': {1: {'data': 530424,
                              'dynamic': 723,
                              'jid': 1266,
                              'process': 'rt_check_mgr',
                              'stack': 136,
                              'text': 104}}},
         1267: {'index': {1: {'data': 336304,
                              'dynamic': 2594,
                              'jid': 1267,
                              'process': 'pbr_ma',
                              'stack': 136,
                              'text': 184}}},
         1268: {'index': {1: {'data': 466552,
                              'dynamic': 2107,
                              'jid': 1268,
                              'process': 'qos_ma',
                              'stack': 136,
                              'text': 876}}},
         1269: {'index': {1: {'data': 334576,
                              'dynamic': 975,
                              'jid': 1269,
                              'process': 'vservice_mgr',
                              'stack': 136,
                              'text': 60}}},
         1270: {'index': {1: {'data': 1000676,
                              'dynamic': 5355,
                              'jid': 1270,
                              'process': 'mpls_ldp',
                              'stack': 136,
                              'text': 2952}}},
         1271: {'index': {1: {'data': 1002132,
                              'dynamic': 6985,
                              'jid': 1271,
                              'process': 'xtc_agent',
                              'stack': 136,
                              'text': 1948}}},
         1272: {'index': {1: {'data': 1017288,
                              'dynamic': 14858,
                              'jid': 1272,
                              'process': 'l2vpn_mgr',
                              'stack': 136,
                              'text': 5608}}},
         1273: {'index': {1: {'data': 424,
                              'dynamic': 0,
                              'jid': 1273,
                              'process': 'bash',
                              'stack': 136,
                              'text': 1016}}},
         1274: {'index': {1: {'data': 202200,
                              'dynamic': 1543,
                              'jid': 1274,
                              'process': 'cmpp',
                              'stack': 136,
                              'text': 60}}},
         1275: {'index': {1: {'data': 334624,
                              'dynamic': 1555,
                              'jid': 1275,
                              'process': 'l2tp_mgr',
                              'stack': 136,
                              'text': 960}}},
         1276: {'index': {1: {'data': 223128,
                              'dynamic': 16781,
                              'jid': 1276,
                              'process': 'schema_server',
                              'stack': 136,
                              'text': 80}}},
         1277: {'index': {1: {'data': 670692,
                              'dynamic': 6660,
                              'jid': 1277,
                              'process': 'sdr_instmgr',
                              'stack': 136,
                              'text': 1444}}},
         1278: {'index': {1: {'data': 1004336,
                              'dynamic': 436,
                              'jid': 1278,
                              'process': 'snmppingd',
                              'stack': 136,
                              'text': 24}}},
         1279: {'index': {1: {'data': 200120,
                              'dynamic': 263,
                              'jid': 1279,
                              'process': 'ssh_backup_server',
                              'stack': 136,
                              'text': 100}}},
         1280: {'index': {1: {'data': 398960,
                              'dynamic': 835,
                              'jid': 1280,
                              'process': 'ssh_server',
                              'stack': 136,
                              'text': 228}}},
         1281: {'index': {1: {'data': 399312,
                              'dynamic': 1028,
                              'jid': 1281,
                              'process': 'tc_server',
                              'stack': 136,
                              'text': 240}}},
         1282: {'index': {1: {'data': 200636,
                              'dynamic': 281,
                              'jid': 1282,
                              'process': 'wanphy_proc',
                              'stack': 136,
                              'text': 12}}},
         67280: {'index': {1: {'data': 204,
                               'dynamic': 0,
                               'jid': 67280,
                               'process': 'bash',
                               'stack': 136,
                               'text': 1016}}},
         67321: {'index': {1: {'data': 132,
                               'dynamic': 0,
                               'jid': 67321,
                               'process': 'sh',
                               'stack': 136,
                               'text': 1016}}},
         67322: {'index': {1: {'data': 204,
                               'dynamic': 0,
                               'jid': 67322,
                               'process': 'bash',
                               'stack': 136,
                               'text': 1016}}},
         67338: {'index': {1: {'data': 40,
                               'dynamic': 0,
                               'jid': 67338,
                               'process': 'cgroup_oom',
                               'stack': 136,
                               'text': 8}}},
         67493: {'index': {1: {'data': 176,
                               'dynamic': 0,
                               'jid': 67493,
                               'process': 'bash',
                               'stack': 136,
                               'text': 1016}}},
         67499: {'index': {1: {'data': 624,
                               'dynamic': 0,
                               'jid': 67499,
                               'process': 'bash',
                               'stack': 136,
                               'text': 1016}}},
         67513: {'index': {1: {'data': 256,
                               'dynamic': 0,
                               'jid': 67513,
                               'process': 'inotifywait',
                               'stack': 136,
                               'text': 24}}},
         67514: {'index': {1: {'data': 636,
                               'dynamic': 0,
                               'jid': 67514,
                               'process': 'bash',
                               'stack': 136,
                               'text': 1016}}},
         67563: {'index': {1: {'data': 8408,
                               'dynamic': 0,
                               'jid': 67563,
                               'process': 'dbus-daemon',
                               'stack': 136,
                               'text': 408}}},
         67582: {'index': {1: {'data': 440,
                               'dynamic': 0,
                               'jid': 67582,
                               'process': 'sshd',
                               'stack': 136,
                               'text': 704}}},
         67592: {'index': {1: {'data': 200,
                               'dynamic': 0,
                               'jid': 67592,
                               'process': 'rpcbind',
                               'stack': 136,
                               'text': 44}}},
         67686: {'index': {1: {'data': 244,
                               'dynamic': 0,
                               'jid': 67686,
                               'process': 'rngd',
                               'stack': 136,
                               'text': 20}}},
         67692: {'index': {1: {'data': 176,
                               'dynamic': 0,
                               'jid': 67692,
                               'process': 'syslogd',
                               'stack': 136,
                               'text': 44}}},
         67695: {'index': {1: {'data': 3912,
                               'dynamic': 0,
                               'jid': 67695,
                               'process': 'klogd',
                               'stack': 136,
                               'text': 28}}},
         67715: {'index': {1: {'data': 176,
                               'dynamic': 0,
                               'jid': 67715,
                               'process': 'xinetd',
                               'stack': 136,
                               'text': 156}}},
         67758: {'index': {1: {'data': 748,
                               'dynamic': 0,
                               'jid': 67758,
                               'process': 'crond',
                               'stack': 524,
                               'text': 56}}},
         68857: {'index': {1: {'data': 672,
                               'dynamic': 0,
                               'jid': 68857,
                               'process': 'bash',
                               'stack': 136,
                               'text': 1016}}},
         68876: {'index': {1: {'data': 744,
                               'dynamic': 0,
                               'jid': 68876,
                               'process': 'bash',
                               'stack': 136,
                               'text': 1016}}},
         68881: {'index': {1: {'data': 82976,
                               'dynamic': 0,
                               'jid': 68881,
                               'process': 'dev_inotify_hdlr',
                               'stack': 136,
                               'text': 12}}},
         68882: {'index': {1: {'data': 82976,
                               'dynamic': 0,
                               'jid': 68882,
                               'process': 'dev_inotify_hdlr',
                               'stack': 136,
                               'text': 12}}},
         68909: {'index': {1: {'data': 88312,
                               'dynamic': 0,
                               'jid': 68909,
                               'process': 'ds',
                               'stack': 136,
                               'text': 56}}},
         69594: {'index': {1: {'data': 199480,
                               'dynamic': 173,
                               'jid': 69594,
                               'process': 'tty_exec_launcher',
                               'stack': 136,
                               'text': 16}}},
         70487: {'index': {1: {'data': 200108,
                               'dynamic': 312,
                               'jid': 70487,
                               'process': 'tams_proc',
                               'stack': 136,
                               'text': 440}}},
         70709: {'index': {1: {'data': 200200,
                               'dynamic': 342,
                               'jid': 70709,
                               'process': 'tamd_proc',
                               'stack': 136,
                               'text': 32}}},
         73424: {'index': {1: {'data': 200808,
                               'dynamic': 0,
                               'jid': 73424,
                               'process': 'attestation_agent',
                               'stack': 136,
                               'text': 108}}},
         75962: {'index': {1: {'data': 206656,
                               'dynamic': 0,
                               'jid': 75962,
                               'process': 'pyztp2',
                               'stack': 136,
                               'text': 8}}},
         76021: {'index': {1: {'data': 1536,
                               'dynamic': 0,
                               'jid': 76021,
                               'process': 'bash',
                               'stack': 136,
                               'text': 1016}}},
         76022: {'index': {1: {'data': 1784,
                               'dynamic': 0,
                               'jid': 76022,
                               'process': 'bash',
                               'stack': 136,
                               'text': 1016}}},
         76639: {'index': {1: {'data': 16480,
                               'dynamic': 0,
                               'jid': 76639,
                               'process': 'perl',
                               'stack': 136,
                               'text': 8}}},
         76665: {'index': {1: {'data': 487380,
                               'dynamic': 0,
                               'jid': 76665,
                               'process': 'pam_cli_agent',
                               'stack': 136,
                               'text': 1948}}},
         76768: {'index': {1: {'data': 24868,
                               'dynamic': 0,
                               'jid': 76768,
                               'process': 'perl',
                               'stack': 136,
                               'text': 8}}},
         76784: {'index': {1: {'data': 17356,
                               'dynamic': 0,
                               'jid': 76784,
                               'process': 'perl',
                               'stack': 136,
                               'text': 8}}},
         76802: {'index': {1: {'data': 16280,
                               'dynamic': 0,
                               'jid': 76802,
                               'process': 'perl',
                               'stack': 136,
                               'text': 8}}},
         77304: {'index': {1: {'data': 598100,
                               'dynamic': 703,
                               'jid': 77304,
                               'process': 'exec',
                               'stack': 136,
                               'text': 76}}},
         80488: {'index': {1: {'data': 172,
                               'dynamic': 0,
                               'jid': 80488,
                               'process': 'sleep',
                               'stack': 136,
                               'text': 32}}},
         80649: {'index': {1: {'data': 172,
                               'dynamic': 0,
                               'jid': 80649,
                               'process': 'sleep',
                               'stack': 136,
                               'text': 32}}},
         80788: {'index': {1: {'data': 1484,
                               'dynamic': 2,
                               'jid': 80788,
                               'process': 'sleep',
                               'stack': 136,
                               'text': 32}}},
         80791: {'index': {1: {'data': 420,
                               'dynamic': 0,
                               'jid': 80791,
                               'process': 'sh',
                               'stack': 136,
                               'text': 1016}}},
         80792: {'index': {1: {'data': 133912,
                               'dynamic': 194,
                               'jid': 80792,
                               'process': 'sh_proc_mem_cli',
                               'stack': 136,
                               'text': 12}}},
         80796: {'index': {1: {'data': 484,
                               'dynamic': 0,
                               'jid': 80796,
                               'process': 'sh',
                               'stack': 136,
                               'text': 1016}}},
         80797: {'index': {1: {'data': 133916,
                               'dynamic': 204,
                               'jid': 80797,
                               'process': 'sh_proc_memory',
                               'stack': 136,
                               'text': 12
                               }
                            }
                        }
                    }
                }

    # show processes memory
    golden_output = {
        'execute.return_value':
        '''\

            JID      Text(KB)   Data(KB)  Stack(KB) Dynamic(KB) Process
        ------ ---------- ---------- ---------- ----------- ------------------------------
        1114        10636    1084008        136       45594 emsd
        1078         2408    1045796        136       40267 bgp
        1240         1160     951448        136       26381 ipv6_rib
        1135          772    1052648        136       24083 netconf
        1253         4424    1018740        136       22744 pim
        1238         1008    1015244        136       22504 ipv4_rib
        1254         4544    1017788        136       22444 pim6
        197           304    1015252        136       21870 parser_server
        273           112     494124        136       19690 invmgr_proxy
        411           388     542460        136       17658 sysdb_mc
        1236            4     546924        136       17047 statsd_manager_g
        408             4     415316        136       16797 statsd_manager_l
        1276           80     223128        136       16781 schema_server
        409          1824     946780        136       16438 iedged
        419           144     689020        136       15522 sdr_invmgr
        1272         5608    1017288        136       14858 l2vpn_mgr
        1027         2880    1012376        136       14258 ospf
        1247          980     941936        144       13246 igmp
        210           244     878632        136       13237 nvgen_server
        1252          928     940472        136       12973 mld
        1241         1536     873952        136       11135 mrib
        1242         1516     873732        136       11043 mrib6
        305          1096    1001716        136        9508 gsp
        309           488    1012628        136        9404 tcp
        1011         4888    1006776        136        8929 isis
        1012         4888    1006776        136        8925 isis
        1046         1552     804288        136        8673 ospfv3
        184           368     407016        136        8579 subdb_svr
        166          1108     935480        136        8194 mpls_lsd
        424           212     604932        136        8135 issudir
        1256         1512     999524        136        7871 bfd
        53             32     342500        136        7095 dsr
        355           292     994116        136        7056 eem_server
        252             4     531384        136        7041 sysdb_svr_local
        1271         1948    1002132        136        6985 xtc_agent
        1277         1444     670692        136        6660 sdr_instmgr
        121           504     470008        136        6347 calv_alarm_mgr
        259          1016    1000600        136        6088 ipv6_nd
        169           680     735000        136        6057 ipsub_ma
        412          1808    1003624        136        5783 l2fib_mgr
        406          1268     868076        136        5739 ppp_ma
        51           1372    1027776        136        5668 processmgr
        136           188     997196        136        5618 resmon
        1071          484     998992        136        5498 msdp
        1270         2952    1000676        136        5355 mpls_ldp
        353           728    1002896        136        5160 call_home
        222            12     205484        136        5126 mpa_fm_svr
        1147          464     808524        136        5098 sdr_mgbl_proxy
        1255         2588     799148        136        4916 bundlemgr_distrib
        217           520     406432        136        4666 pppoe_ma
        333           404     799488        136        4511 rsi_master
        254            96     534032        136        4463 eem_ed_generic
        364          3580    1001736        136        4343 fib_mgr
        327           268     997196        136        3950 eem_policy_dir
        362           728     932680        136        3880 arp
        337           204     600644        136        3858 nve_mgr
        376            76     467420        136        3815 eem_ed_sysmgr
        188            60     533704        136        3710 eem_ed_nd
        291             4     794684        136        3678 sysdb_shared_sc
        385           592     603424        136        3673 ipsec_mp
        167           540     730776        136        3649 ipv6_ma
        417            60     532108        136        3623 eem_ed_stats
        1093          716     668844        136        3577 bpm
        403            64     532624        136        3546 eem_ed_timer
        128            44     532612        136        3543 eem_ed_test
        245            48     532624        136        3541 eem_ed_counter
        152            52     532616        136        3541 eem_ed_none
        198            56     532612        136        3540 eem_ed_config
        189             4     401488        136        3499 ifmgr
        202           292     864208        136        3472 netio
        1243          472     800236        136        3444 policy_repository
        220            60     598812        136        3443 eem_ed_syslog
        1003          936     798196        136        3368 eigrp
        368           124    1002148        136        3111 raw_ip
        190           196    1001552        136        3082 rdsfs_svr
        186            16     932992        136        3072 smartlicserver
        206             4     794684        136        2967 sysdb_shared_nc
        381           828     533872        136        2891 ipv4_mfwd_partner
        319           112     532344        136        2874 bcdls
        318           112     532344        136        2874 bcdls
        413           256     401532        136        2851 aib
        122           180    1003480        136        2838 udp
        207           268     601736        136        2823 yang_server
        137           612     534184        136        2816 bundlemgr_local
        267           204     598760        136        2768 object_tracking
        405           732     664196        136        2730 pm_collector
        361           836     533872        136        2637 ipv6_mfwd_partner
        178           264     468272        136        2630 accounting_ma
        194           180     794692        136        2629 nrssvr
        218           484     664484        136        2602 l2rib
        1267          184     336304        136        2594 pbr_ma
        127            96     797548        136        2573 ifindex_server
        269            60     664752        136        2513 eth_mgmt
        1261           12     206536        136        2468 python_process_manager
        344           108     996048        136        2352 plat_sl_client
        271           580     400624        136        2348 rsi_agent
        429            56     269032        136        2344 pim6_ma
        365            56     269016        136        2344 pim_ma
        418           540     532288        136        2306 ipv4_ma
        211           228     334080        136        2169 pfilter_ma
        1130          412     599144        136        2131 lldp_agent
        204           152     268932        136        2122 ether_caps_partner
        1268          876     466552        136        2107 qos_ma
        310           512     333572        136        2092 daps
        316           112     531560        136        2016 bcdls
        317           112     531560        136        2015 bcdls
        320           112     531556        136        2013 bcdls
        247           344    1010268        136        1923 cfgmgr-rp
        1257           60     268092        136        1903 bgp_epe
        296           292     796404        136        1902 correlatord
        1067           84     532012        136        1892 autorp_map_agent
        433           112     597624        136        1860 ema_server_sdr
        200           344     531264        136        1810 ipv4_arm
        260           260     533044        136        1793 sdr_instagt
        306             4     794684        136        1792 sysdb_svr_admin
        359           328     531256        136        1788 ipv6_arm
        1074          296     599436        136        1782 rip
        407             4     794684        136        1753 sysdb_shared_data_nc
        1233          252     399212        136        1681 mpls_static
        420            96     466456        136        1661 http_client
        201            68     268968        136        1619 session_mon
        1275          960     334624        136        1555 l2tp_mgr
        1274           60     202200        136        1543 cmpp
        249           604     797376        136        1527 locald_DLRSC
        352           308     465844        136        1524 lpts_pa
        125           312     333592        136        1506 pifibm_server_rp
        294           560     267932        136        1495 issumgr
        402            40     597352        136        1456 vi_config_replicator
        272           180     794692        136        1425 nrssvr_global
        193           344     665096        136        1405 ntpd
        390           176     663828        136        1384 bcdl_agent
        350            72     399188        136        1344 vm-monitor
        1235          212     665416        136        1339 intf_mgbl
        1237          144     201996        136        1331 ipv4_mfwd_ma
        149           188     663524        136        1297 clns
        373           592     333240        136        1249 policymgr_rp
        248           104     465260        136        1243 alarm-logger
        341           160     465864        136        1145 ipv6_io
        425           104     466796        136        1138 l2snoop
        1066           52     333188        136        1084 autorp_candidate_rp
        213           428     531840        136        1073 kim
        389           176     729880        136        1066 bcdl_agent
        391           176     795416        136        1063 bcdl_agent
        154           140     729896        136        1046 ipv4_acl_mgr
        1265           56     729900        136        1030 es_acl_mgr
        1281          240     399312        136        1028 tc_server
        343           212     663932        136        1013 ipv6_acl_daemon
        342           224     864468        136        1011 syslogd
        243             8     267576        136         990 spio_ea
        1269           60     334576        136         975 vservice_mgr
        112           144     861144        136         957 qsm
        415            28     399116        136         895 ether_sock
        1244          160     399440        136         892 ipv4_mpa
        1245          160     399444        136         891 ipv6_mpa
        303            68     399360        136         882 tftp_fs
        1260           64     399868        136         874 ftp_fs
        1234          100     464512        136         856 lldp_mgr
        377           140     333636        136         843 mpls_io
        182             4     334236        136         843 spio_ma
        388           176     729160        136         836 bcdl_agent
        1280          228     398960        136         835 ssh_server
        119            12     397880        136         828 syslog_dev
        261           220     334860        136         806 ipsec_pp
        1136           20     600036        136         795 netconf_agent_tty
        346           136     598152        136         778 cinetd
        437            80     794096        136         776 cdm_rs
        256           156     334104        136         756 mpls_vpn_mib
        195           256     531776        136         748 ipv4_io
        1266          104     530424        136         723 rt_check_mgr
        266            92     266344        136         717 pm_server
        251            32     265840        136         712 tamfs
        77304          76     598100        136         703 exec
        162            52     267456        136         693 ip_aps
        277            44     267112        136         688 tam_sync
        1251            4     267420        136         681 ipv6_local
        1250            4     267436        136         680 ipv6_connected
        339           140     266800        136         679 rmf_svr
        1249            4     267424        136         677 ipv4_local
        1248            4     267440        136         677 ipv4_connected
        113           328     400776        136         671 spp
        191            12     398300        136         632 hostname_sync
        157            44     200908        136         626 ssh_key_server
        369            40     464272        136         625 ltrace_server
        183            40     266788        136         607 statsd_server
        1101           24     266776        136         602 cdp_mgr
        168            36     266788        136         589 nd_partner
        134            28     466168        136         580 ipv4_acl_act_agent
        401            20     466148        136         579 es_acl_act_agent
        192            20     466168        136         570 l2vpn_policy_reg_agent
        313            48     199844        136         551 ssh_key_client
        114             8     531912        136         545 devc-conaux-con
        382           132     465388        136         538 packet
        308             8     333172        136         538 devc-vty
        171            16     266432        136         530 shelf_mgr_proxy
        363            96     202024        136         522 cepki
        380           124     333604        136         520 fhrp_output
        111             8     531876        136         514 devc-conaux-aux
        1221           32     200848        136         503 ssh_conf_verifier
        1258          136     268016        136         493 domain_services
        357            36     202040        136         486 tamsvcs_tamm
        299            92     268000        136         459 ipv6_ea
        216            64     267224        136         451 showd_lc
        426            56     331808        136         444 ssm_process
        414            32     266776        136         440 rmf_cli_edm
        250            12     265800        136         438 lcp_mgr
        1278           24    1004336        136         436 snmppingd
        276           204     202328        136         436 mpls_fwd_show_proxy
        329           108     267464        136         434 mpls_io_ea
        428            48     267340        136         432 ip_app
        118            56     200748        136         426 shmwin_svr
        1262            8     200360        136         421 tty_verifyd
        147            68     201332        136         418 type6_server
        268            20     200700        136         417 wdsysmon_fd_edm
        255            32     201200        136         409 ipv6_acl_cfg_agent
        1263           60     265924        136         399 ipv4_rump
        356             8     200720        136         396 tcl_secure_mode
        1264          108     265908        136         394 ipv6_rump
        431            16     200416        136         390 local_sock
        123            40     529852        136         389 enf_broker
        314            28     332076        136         371 timezone_config
        297            56     201304        136         367 imaedm_server
        115            52     662452        136         366 syslogd_helper
        360            88     201196        136         363 fwd_driver_partner
        383            40     333284        136         359 dumper
        334            12     333648        136         351 sconbkup
        124            20     200120        168         351 procfs_server
        326           116     398256        136         348 sld
        70709          32     200200        136         342 tamd_proc
        1239          136     201364        136         341 ipv6_mfwd_ma
        257           156     267888        136         339 bundlemgr_adj
        181            16     201280        136         329 nsr_ping_reply
        70487         440     200108        136         312 tams_proc
        304            32     202220        136         306 ncd
        126            28     399332        136         305 ltrace_sync
        161            16     200640        136         297 cmp_edm
        295           220     266744        136         296 vlan_ea
        375            32     200624        136         290 loopback_caps_partner
        221            52     267264        136         290 lpts_fm
        421            16     201152        136         285 pak_capture_partner
        158            20     200628        136         285 heap_summary_edm
        1128           84     200156        136         284 isis_uv
        349            20     200612        136         284 debug_d_admin
        138            16     200652        136         284 chkpt_proxy
        312            36     200620        136         283 ipv6_assembler
        199            48     200648        136         282 cerrno_server
        1282           12     200636        136         281 wanphy_proc
        132            20     200628        136         280 show_mediang_edm
        371            24     200572        136         279 netio_debug_partner
        332            20     332748        136         276 redstatsd
        416            32     200980        136         275 shconf-edm
        146            28     200240        136         275 bgp_policy_reg_agent
        196            16     200624        136         274 domain_sync
        1259           32     201184        136         272 ethernet_stats_controller_edm
        432            68     265704        136         269 crypto_monitor
        422            36     200016        136         267 bag_schema_svr
        275            12     199552        136         264 nsr_fo
        1279          100     200120        136         263 ssh_backup_server
        290            20     200640        136         262 sh_proc_mem_edm
        1246           20     200664        136         261 eth_gl_cfg
        435            12     200120        136         261 eigrp_policy_reg_agent
        347            24     200648        136         261 debug_d
        155            12     200120        136         261 ospf_policy_reg_agent
        1139           48     200092        136         259 ospf_uv
        434             8     200120        136         259 isis_policy_reg_agent
        372             8     200120        136         259 pim_policy_reg_agent
        293             8     200120        136         259 pim6_policy_reg_agent
        278             8     200120        136         259 mldp_policy_reg_agent
        187             8     200120        136         259 rip_policy_reg_agent
        1140           32     200092        136         258 ospfv3_uv
        378             8     200120        136         258 ospfv3_policy_reg_agent
        270            20     200064        136         257 gcp_fib_verifier
        139             8     200120        136         257 lisp_xr_policy_reg_agent
        130             8     200120        136         257 igmp_policy_reg_agent
        253            32     200672        136         256 tty_show_users_edm
        174            56     200096        136         256 bundlemgr_checker
        205            28     201168        136         254 sunstone_stats_svr
        209            24     200656        136         253 crypto_edm
        172            16     200604        136         253 early_fast_discard_verifier
        1113           48     200096        136         251 eigrp_uv
        208            16     200096        136         251 ipodwdm
        301            88     200644        136         250 sysmgr_show_proc_all_edm
        175            12     200120        136         248 syslog_infra_hm
        244             8     200632        136         247 mempool_edm
        143            20     200644        136         247 procfind
        298            12     200224        136         246 ztp_cfg
        141            20     200648        136         246 linux_nto_misc_showd
        427            16     200120        136         245 media_server
        384            12     200636        136         244 showd_server
        258            16     1651090        136         244 file_paltx
        180             8     1651090        136         242 aipc_cleaner
        177             8     200112        136         241 meminfo_svr
        80797          12     133916        136         204 sh_proc_memory
        336            12     199440        136         204 pam_manager
        80792          12     133912        136         194 sh_proc_mem_cli
        69594          16     199480        136         173 tty_exec_launcher
        80788          32       1484        136           2 sleep
        80796        1016        484        136           0 sh
        80791        1016        420        136           0 sh
        80649          32        172        136           0 sleep
        80488          32        172        136           0 sleep
        76802           8      16280        136           0 perl
        76784           8      17356        136           0 perl
        76768           8      24868        136           0 perl
        76665        1948     487380        136           0 pam_cli_agent
        76639           8      16480        136           0 perl
        76022        1016       1784        136           0 bash
        76021        1016       1536        136           0 bash
        75962           8     206656        136           0 pyztp2
        73424         108     200808        136           0 attestation_agent
        68909          56      88312        136           0 ds
        68882          12      82976        136           0 dev_inotify_hdlr
        68881          12      82976        136           0 dev_inotify_hdlr
        68876        1016        744        136           0 bash
        68857        1016        672        136           0 bash
        67758          56        748        524           0 crond
        67715         156        176        136           0 xinetd
        67695          28       3912        136           0 klogd
        67692          44        176        136           0 syslogd
        67686          20        244        136           0 rngd
        67592          44        200        136           0 rpcbind
        67582         704        440        136           0 sshd
        67563         408       8408        136           0 dbus-daemon
        67514        1016        636        136           0 bash
        67513          24        256        136           0 inotifywait
        67499        1016        624        136           0 bash
        67493        1016        176        136           0 bash
        67338           8         40        136           0 cgroup_oom
        67322        1016        204        136           0 bash
        67321        1016        132        136           0 sh
        67280        1016        204        136           0 bash
        1273         1016        424        136           0 bash
        1             296        344        136           0 init
            '''
    }

    def test_empty(self):
        self.dev = Mock(**self.empty_output)
        obj = ShowProcessesMemory(device=self.dev)
        with self.assertRaises(SchemaEmptyParserError):
            parsered_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output)
        obj = ShowProcessesMemory(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

class TestShowProcessesMemoryDetail(unittest.TestCase):
    
    maxDiff = None
    dev = Device(name='ASR9K')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'jid': {240: {'index': {1: {'data': '195M',
                              'dyn_limit': 'unlimited',
                              'dynamic': '275K',
                              'jid': 240,
                              'phy_tot': '6M',
                              'process': 'bgp_policy_reg_agent',
                              'shm_tot': '5M',
                              'stack': '136K',
                              'text': '28K'}}},
          1078: {'index': {1: {'data': '1021M',
                               'dyn_limit': '14894M',
                               'dynamic': '39M',
                               'jid': 1078,
                               'phy_tot': '62M',
                               'process': 'bgp',
                               'shm_tot': '23M',
                               'stack': '136K',
                               'text': '2M'}}},
          1257: {'index': {1: {'data': '261M',
                               'dyn_limit': 'unlimited',
                               'dynamic': '1M',
                               'jid': 1257,
                               'phy_tot': '9M',
                               'process': 'bgp_epe',
                               'shm_tot': '6M',
                               'stack': '136K',
                               'text': '60K'}}}}}

    # show processes memory detail
    golden_output = {
        'execute.return_value':
        '''\
Tue Sep 29 08:11:12.207 UTC
JID         Text       Data       Stack      Dynamic    Dyn-Limit  Shm-Tot    Phy-Tot               Process
1078           2M      1021M       136K        39M     14894M        23M        62M bgp                           
1257          60K       261M       136K         1M  unlimited         6M         9M bgp_epe                       
240           28K       195M       136K       275K  unlimited         5M         6M bgp_policy_reg_agent 
        '''
    }

    def test_empty(self):
        self.dev = Mock(**self.empty_output)
        obj = ShowProcessesMemoryDetail(device=self.dev)
        with self.assertRaises(SchemaEmptyParserError):
            parsered_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output)
        obj = ShowProcessesMemoryDetail(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

if __name__ == '__main__':
    unittest.main()
