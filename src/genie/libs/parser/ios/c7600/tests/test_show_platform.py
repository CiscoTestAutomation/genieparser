import unittest
import genie.gre
from unittest.mock import Mock
from pyats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                             SchemaMissingKeyError

# c7600 show_platform
from genie.libs.parser.ios.c7600.show_platform import (ShowVersion, 
                                                       Dir,
                                                       ShowRedundancy,
                                                       ShowInventory,
                                                       ShowModule)

class TestShowVersion(unittest.TestCase):
    device_empty = Device(name='empty')
    device_c7600 = Device(name='c7600')

    empty_output = {'execute.return_value': ''}
    output_c7600 = {'execute.return_value': '''
           Cisco IOS Software, s72033_rp Software (s72033_rp-ADVENTERPRISEK9_DBG-M), Version 15.4(0.10)S, EARLY DEPLOYMENT ENGINEERING WEEKLY BUILD, synced to  BLD_DARLING_122S_040709_1301
           Technical Support: http://www.cisco.com/techsupport
           Copyright (c) 1986-2013 by Cisco Systems, Inc.
           Compiled Wed 26-Jun-13 02:21 by alnguyen

           ROM: System Bootstrap, Version 12.2(17r)SX7, RELEASE SOFTWARE (fc1)
           BOOTLDR: Cisco IOS Software, s72033_rp Software (s72033_rp-ADVENTERPRISEK9_DBG-M), Version 15.4(0.10)S, EARLY DEPLOYMENT ENGINEERING WEEKLY BUILD, synced to  BLD_DARLING_122S_040709_1301

           ipcore-ssr-uut2 uptime is 22 weeks, 6 days, 2 hours, 1 minute
           Uptime for this control processor is 22 weeks, 6 days, 1 hour, 57 minutes
           System returned to ROM by  power cycle at 03:04:03 PDT Thu May 18 2017 (SP by power on)
           System image file is "disk0:s72033-adventerprisek9_dbg-mz.154-0.10.S-ipcore-ssr-uut2"
           Last reload type: Normal Reload
           Last reload reason: abort at PC 0x433A11BC



           This product contains cryptographic features and is subject to United
           States and local country laws governing import, export, transfer and
           use. Delivery of Cisco cryptographic products does not imply
           third-party authority to import, export, distribute or use encryption.
           Importers, exporters, distributors and users are responsible for
           compliance with U.S. and local country laws. By using this product you
           agree to comply with applicable laws and regulations. If you are unable
           to comply with U.S. and local laws, return this product immediately.

           A summary of U.S. laws governing Cisco cryptographic products may be found at:
           http://www.cisco.com/wwl/export/crypto/tool/stqrg.html

           If you require further assistance please contact us by sending email to
           export@cisco.com.

           cisco CISCO7606 (R7000) processor (revision 1.0) with 983008K/65536K bytes of memory.
           Processor board ID FOX11140RN8
           SR71000 CPU at 600MHz, Implementation 1284, Rev 1.2, 512KB L2 Cache
           Last reset from s/w reset
           1 Enhanced FlexWAN controller (4 Serial).
           1 Virtual Ethernet interface
           52 Gigabit Ethernet interfaces
           4 Serial interfaces
           1917K bytes of non-volatile configuration memory.
           8192K bytes of packet buffer memory.

           65536K bytes of Flash internal SIMM (Sector size 512K).
           Configuration register is 0x2

           '''}

    parsed_output_c7600 = {
        'version': {
            'bootldr_version': 'Cisco IOS Software, s72033_rp Software (s72033_rp-ADVENTERPRISEK9_DBG-M), Version 15.4(0.10)S, EARLY DEPLOYMENT ENGINEERING WEEKLY BUILD, synced to  BLD_DARLING_122S_040709_1301',
            'chassis': 'CISCO7606',
            'compiled_by': 'alnguyen',
            'compiled_date': 'Wed 26-Jun-13 02:21',
            'control_processor_uptime': '22 weeks, 6 days, 1 hour, 57 minutes',
            'controller': {
                'counts': 1,
                'serial': 4,
                'type': 'Enhanced FlexWAN',
            },
            'cpu': {
                'implementation': '1284',
                'l2_cache': '512KB',
                'name': 'SR71000',
                'rev': '1.2',
                'speed': '600MHz',
            },
            'curr_config_register': '0x2',
            'hostname': 'ipcore-ssr-uut2',
            'image_id': 's72033_rp-ADVENTERPRISEK9_DBG-M',
            'interfaces': {
                'gigabit_ethernet': 52,
                'serial': 4,
                'virtual_ethernet': 1,
            },
            'last_reload': {
                'reason': 'abort at PC 0x433A11BC',
                'type': 'Normal Reload',
            },
            'last_reset': 's/w',
            'main_mem': '983008',
            'memory': {
                'flash_internal_SIMM': 65536,
                'non_volatile_conf': 1917,
                'packet_buffer': 8192,
            },
            'os': 'IOS',
            'platform': 's72033_rp',
            'processor_board_id': 'FOX11140RN8',
            'processor_type': 'R7000',
            'returned_to_rom_by': 'power cycle at 03:04:03 PDT Thu May 18 2017 (SP by power on)',
            'rom': 'System Bootstrap, Version 12.2(17r)SX7, RELEASE SOFTWARE',
            'rom_version': '(fc1)',
            'system_image': 'disk0:s72033-adventerprisek9_dbg-mz.154-0.10.S-ipcore-ssr-uut2',
            'uptime': '22 weeks, 6 days, 2 hours, 1 minute',
            'version': '15.4(0.10)S',
        },
    }

    def test_empty(self):
        self.device_empty = Mock(**self.empty_output)
        obj = ShowVersion(device=self.device_empty)
        with self.assertRaises(SchemaEmptyParserError):
            empty_parsed_output = obj.parse()

    def test_c7600(self):
        self.maxDiff = None
        self.device_c7600 = Mock(**self.output_c7600)
        obj = ShowVersion(device=self.device_c7600)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.parsed_output_c7600)


class TestDir(unittest.TestCase):
    empty_output = {'execute.return_value': ''}
    output_c7600 = {'execute.return_value': '''
            Directory of disk0:/

            2  -rw-         373   May 9 2013 10:00:08 -07:00  default_config
            3  -rw-         421   May 9 2013 10:00:20 -07:00  golden_config
            4  -rw-   188183700   May 9 2013 10:11:56 -07:00  ISSUCleanGolden
            5  -rw-   210179540  Oct 18 2018 07:22:24 -07:00  s72033-adventerprisek9_dbg-mz.154-0.10.S-ipcore-ssr-uut2

        1024589824 bytes total (626180096 bytes free)
    '''}
    parsed_output = {
        'dir': {
            'dir': 'disk0:/',
            'disk0:/': {
                'bytes_free': '626180096',
                'bytes_total': '1024589824',
                'files': {
                    'ISSUCleanGolden': {
                        'index': '4',
                        'last_modified_date': 'May 9 2013 10:11:56 -07:00',
                        'permissions': '-rw-',
                        'size': '188183700',
                    },
                    'default_config': {
                        'index': '2',
                        'last_modified_date': 'May 9 2013 10:00:08 -07:00',
                        'permissions': '-rw-',
                        'size': '373',
                    },
                    'golden_config': {
                        'index': '3',
                        'last_modified_date': 'May 9 2013 10:00:20 -07:00',
                        'permissions': '-rw-',
                        'size': '421',
                    },
                    's72033-adventerprisek9_dbg-mz.154-0.10.S-ipcore-ssr-uut2': {
                        'index': '5',
                        'last_modified_date': 'Oct 18 2018 07:22:24 -07:00',
                        'permissions': '-rw-',
                        'size': '210179540',
                    },
                },
            },
        },
    }

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        version_obj = Dir(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            empty_parsed_output = version_obj.parse()

    def test_c7600(self):
        self.maxDiff = None
        self.device = Mock(**self.output_c7600)
        obj = Dir(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.parsed_output)

class TestShowRedundancy(unittest.TestCase):

    dev1 = Device(name='empty')
    dev_iosv = Device(name='c7600')
    empty_output = {'execute.return_value': ''}
    output_c7600 = {'execute.return_value': '''
                Redundant System Information :
        ------------------------------
            Available system uptime = 24 weeks, 6 days, 23 hours, 14 minutes
        Switchovers system experienced = 0
                    Standby failures = 0
                Last switchover reason = none

                        Hardware Mode = Duplex
            Configured Redundancy Mode = sso
            Operating Redundancy Mode = sso
                    Maintenance Mode = Disabled
                        Communications = Up

        Current Processor Information :
        -------------------------------
                    Active Location = slot 6
                Current Software state = ACTIVE
            Uptime in current state = 24 weeks, 6 days, 23 hours, 13 minutes
                        Image Version = Cisco IOS Software, s72033_rp Software (s72033_rp-ADVENTERPRISEK9_DBG-M), Version 15.4(0.10)S, EARLY DEPLOYMENT ENGINEERING WEEKLY BUILD, synced to  BLD_DARLING_122S_040709_1301
        Technical Support: http://www.cisco.com/techsupport
        Copyright (c) 1986-2013 by Cisco Systems, Inc.
        Compiled Wed 26-Jun-13 02:21 by alnguyen
                                BOOT = disk0:s72033-adventerprisek9_dbg-mz.154-0.10.S-ipcore-ssr-uut2,12;
                        CONFIG_FILE =
                            BOOTLDR =
                Configuration register = 0x2

        Peer Processor Information :
        ----------------------------
                    Standby Location = slot 5
                Current Software state = STANDBY HOT
            Uptime in current state = 4 weeks, 1 day, 22 hours, 47 minutes
                        Image Version = Cisco IOS Software, s72033_rp Software (s72033_rp-ADVENTERPRISEK9_DBG-M), Version 15.4(0.10)S, EARLY DEPLOYMENT ENGINEERING WEEKLY BUILD, synced to  BLD_DARLING_122S_040709_1301
        Technical Support: http://www.cisco.com/techsupport
        Copyright (c) 1986-2013 by Cisco Systems, Inc.
        Compiled Wed 26-Jun-13 02:21 by alnguyen
                                BOOT = disk0:s72033-adventerprisek9_dbg-mz.154-0.10.S-ipcore-ssr-uut2,12;
                        CONFIG_FILE =
                            BOOTLDR =
                Configuration register = 0x2
        
    '''}

    parsed_output = {
        'red_sys_info': {
            'available_system_uptime': '24 weeks, 6 days, 23 hours, 14 minutes',
            'communications': 'Up',
            'conf_red_mode': 'sso',
            'hw_mode': 'Duplex',
            'last_switchover_reason': 'none',
            'maint_mode': 'Disabled',
            'oper_red_mode': 'sso',
            'standby_failures': '0',
            'switchovers_system_experienced': '0',
        },
        'slot': {
            'slot 5': {
                'boot': 'disk0:s72033-adventerprisek9_dbg-mz.154-0.10.S-ipcore-ssr-uut2,12;',
                'compiled_by': 'alnguyen',
                'compiled_date': 'Wed 26-Jun-13 02:21',
                'config_register': '0x2',
                'curr_sw_state': 'STANDBY HOT',
                'image_ver': 'Cisco IOS Software, s72033_rp Software (s72033_rp-ADVENTERPRISEK9_DBG-M), Version 15.4(0.10)S, EARLY DEPLOYMENT ENGINEERING WEEKLY BUILD, synced to  BLD_DARLING_122S_040709_1301',
                'uptime_in_curr_state': '4 weeks, 1 day, 22 hours, 47 minutes',
            },
            'slot 6': {
                'boot': 'disk0:s72033-adventerprisek9_dbg-mz.154-0.10.S-ipcore-ssr-uut2,12;',
                'compiled_by': 'alnguyen',
                'compiled_date': 'Wed 26-Jun-13 02:21',
                'config_register': '0x2',
                'curr_sw_state': 'ACTIVE',
                'image_ver': 'Cisco IOS Software, s72033_rp Software (s72033_rp-ADVENTERPRISEK9_DBG-M), Version 15.4(0.10)S, EARLY DEPLOYMENT ENGINEERING WEEKLY BUILD, synced to  BLD_DARLING_122S_040709_1301',
                'uptime_in_curr_state': '24 weeks, 6 days, 23 hours, 13 minutes',
            },
        },
    }

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        version_obj = ShowRedundancy(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            empty_parsed_output = version_obj.parse()
    
    def test_c7600(self):
        self.maxDiff = None
        self.device = Mock(**self.output_c7600)
        obj = ShowRedundancy(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.parsed_output)

class TestShowInventory(unittest.TestCase):

    dev1 = Device(name='empty')
    dev_iosv = Device(name='c7600')
    empty_output = {'execute.return_value': ''}
    output_c7600 = {'execute.return_value': '''
        NAME: "CISCO7606", DESCR: "Cisco Systems Cisco 7600 6-slot Chassis System"
        PID: CISCO7606         , VID:    , SN: FOX11140RN8

        NAME: "CLK-7600 1", DESCR: "OSR-7600 Clock FRU 1"
        PID: CLK-7600          , VID:    , SN: NWG1112014W

        NAME: "CLK-7600 2", DESCR: "OSR-7600 Clock FRU 2"
        PID: CLK-7600          , VID:    , SN: NWG1112014W

        NAME: "module 1", DESCR: "WS-X6748-GE-TX CEF720 48 port 10/100/1000mb Ethernet Rev. 2.7"
        PID: WS-X6748-GE-TX    , VID: V02, SN: SAL1209HMW3

        NAME: "switching engine sub-module of 1", DESCR: "WS-F6700-CFC Centralized Forwarding Card Rev. 4.0"
        PID: WS-F6700-CFC      , VID: V05, SN: SAL1207G5V1

        NAME: "module 2", DESCR: "2 port adapter Enhanced FlexWAN Rev. 2.1"
        PID: WS-X6582-2PA      , VID: V06, SN: JAE0939LYNQ

        NAME: "module 2/1", DESCR: "Serial Port Adapter"
        PID: PA-4T+            , VID:    , SN: 32861325

        NAME: "module 5", DESCR: "WS-SUP720-3BXL 2 ports Supervisor Engine 720 Rev. 4.1"
        PID: WS-SUP720-3BXL    , VID: V11, SN: SAD09020BF8

        NAME: "msfc sub-module of 5", DESCR: "WS-SUP720 MSFC3 Daughterboard Rev. 2.2"
        PID: WS-SUP720         , VID:    , SN: SAD090105M6

        NAME: "switching engine sub-module of 5", DESCR: "WS-F6K-PFC3BXL Policy Feature Card 3 Rev. 1.4"
        PID: WS-F6K-PFC3BXL    , VID:    , SN: SAD090301K6

        NAME: "module 6", DESCR: "WS-SUP720-3BXL 2 ports Supervisor Engine 720 Rev. 5.12"
        PID: WS-SUP720-3BXL    , VID: V11, SN: SAL15129MRC

        NAME: "msfc sub-module of 6", DESCR: "WS-SUP720 MSFC3 Daughterboard Rev. 5.1"
        PID: WS-SUP720         , VID:    , SN: SAL15045PYS

        NAME: "switching engine sub-module of 6", DESCR: "WS-F6K-PFC3BXL Policy Feature Card 3 Rev. 1.11"
        PID: WS-F6K-PFC3BXL    , VID: V02, SN: SAL15129KW4

        NAME: "PS 1 PWR-1900-AC/6", DESCR: "AC_6 power supply, 1900 watt 1"
        PID: PWR-1900-AC/6     , VID: V02, SN: DCA1104401B

        NAME: "PS 2 PWR-1900-AC/6", DESCR: "AC_6 power supply, 1900 watt 2"
        PID: PWR-1900-AC/6     , VID: V02, SN: DCA11044011

    '''}

    parsed_output = {
        'index': {
            1: {
                'descr': 'Cisco Systems Cisco 7600 6-slot Chassis System',
                'name': 'CISCO7606',
                'pid': 'CISCO7606',
                'sn': 'FOX11140RN8',
            },
            2: {
                'descr': 'OSR-7600 Clock FRU 1',
                'name': 'CLK-7600 1',
                'pid': 'CLK-7600',
                'sn': 'NWG1112014W',
            },
            3: {
                'descr': 'OSR-7600 Clock FRU 2',
                'name': 'CLK-7600 2',
                'pid': 'CLK-7600',
                'sn': 'NWG1112014W',
            },
            4: {
                'descr': 'WS-X6748-GE-TX CEF720 48 port 10/100/1000mb Ethernet Rev. 2.7',
                'name': 'module 1',
                'pid': 'WS-X6748-GE-TX',
                'sn': 'SAL1209HMW3',
                'vid': 'V02',
            },
            5: {
                'descr': 'WS-F6700-CFC Centralized Forwarding Card Rev. 4.0',
                'name': 'switching engine sub-module of 1',
                'pid': 'WS-F6700-CFC',
                'sn': 'SAL1207G5V1',
                'vid': 'V05',
            },
            6: {
                'descr': '2 port adapter Enhanced FlexWAN Rev. 2.1',
                'name': 'module 2',
                'pid': 'WS-X6582-2PA',
                'sn': 'JAE0939LYNQ',
                'vid': 'V06',
            },
            7: {
                'descr': 'Serial Port Adapter',
                'name': 'module 2/1',
                'pid': 'PA-4T+',
                'sn': '32861325',
            },
            8: {
                'descr': 'WS-SUP720-3BXL 2 ports Supervisor Engine 720 Rev. 4.1',
                'name': 'module 5',
                'pid': 'WS-SUP720-3BXL',
                'sn': 'SAD09020BF8',
                'vid': 'V11',
            },
            9: {
                'descr': 'WS-SUP720 MSFC3 Daughterboard Rev. 2.2',
                'name': 'msfc sub-module of 5',
                'pid': 'WS-SUP720',
                'sn': 'SAD090105M6',
            },
            10: {
                'descr': 'WS-F6K-PFC3BXL Policy Feature Card 3 Rev. 1.4',
                'name': 'switching engine sub-module of 5',
                'pid': 'WS-F6K-PFC3BXL',
                'sn': 'SAD090301K6',
            },
            11: {
                'descr': 'WS-SUP720-3BXL 2 ports Supervisor Engine 720 Rev. 5.12',
                'name': 'module 6',
                'pid': 'WS-SUP720-3BXL',
                'sn': 'SAL15129MRC',
                'vid': 'V11',
            },
            12: {
                'descr': 'WS-SUP720 MSFC3 Daughterboard Rev. 5.1',
                'name': 'msfc sub-module of 6',
                'pid': 'WS-SUP720',
                'sn': 'SAL15045PYS',
            },
            13: {
                'descr': 'WS-F6K-PFC3BXL Policy Feature Card 3 Rev. 1.11',
                'name': 'switching engine sub-module of 6',
                'pid': 'WS-F6K-PFC3BXL',
                'sn': 'SAL15129KW4',
                'vid': 'V02',
            },
            14: {
                'descr': 'AC_6 power supply, 1900 watt 1',
                'name': 'PS 1 PWR-1900-AC/6',
                'pid': 'PWR-1900-AC/6',
                'sn': 'DCA1104401B',
                'vid': 'V02',
            },
            15: {
                'descr': 'AC_6 power supply, 1900 watt 2',
                'name': 'PS 2 PWR-1900-AC/6',
                'pid': 'PWR-1900-AC/6',
                'sn': 'DCA11044011',
                'vid': 'V02',
            },
        },
    }

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        version_obj = ShowInventory(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            empty_parsed_output = version_obj.parse()
    
    def test_c7600(self):
        self.maxDiff = None
        self.device = Mock(**self.output_c7600)
        obj = ShowInventory(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.parsed_output)

class TestShowModule(unittest.TestCase):
    dev1 = Device(name='empty')
    dev_iosv = Device(name='c7600')
    empty_output = {'execute.return_value': ''}
    output_c7600 = {'execute.return_value': '''
        Mod Ports Card Type                              Model              Serial No.
        --- ----- -------------------------------------- ------------------ -----------
        1   48  CEF720 48 port 10/100/1000mb Ethernet  WS-X6748-GE-TX     SAL1209HMW3
        2    0  2 port adapter Enhanced FlexWAN        WS-X6582-2PA       JAE0939LYNQ
        5    2  Supervisor Engine 720 (Hot)            WS-SUP720-3BXL     SAD09020BF8
        6    2  Supervisor Engine 720 (Active)         WS-SUP720-3BXL     SAL15129MRC

        Mod MAC addresses                       Hw   Fw            Sw           Status
        --- ---------------------------------- ----- ------------- ------------ -------
        1  001e.4aff.ee89 to 001e.4aff.eeb8  2.7   12.2(14r)S    15.4(0.10)   Ok
        2  0015.2bff.e884 to 0015.2bff.e8c3  2.1   15.4(0.10)S   15.4(0.10)S  Ok
        5  0011.21ff.441a to 0011.21ff.441d  4.1   8.1(3         15.4(0.10)   Ok
        6  0022.55ff.039b to 0022.55ff.039e  5.12  8.5(4         15.4(0.10)   Ok

        Mod  Sub-Module                  Model              Serial       Hw     Status
        ---- --------------------------- ------------------ ----------- ------- -------
        1  Centralized Forwarding Card WS-F6700-CFC       SAL1207G5V1  4.0    Ok
        5  Policy Feature Card 3       WS-F6K-PFC3BXL     SAD090301K6  1.4    Ok
        5  MSFC3 Daughterboard         WS-SUP720          SAD090105M6  2.2    Ok
        6  Policy Feature Card 3       WS-F6K-PFC3BXL     SAL15129KW4  1.11   Ok
        6  MSFC3 Daughterboard         WS-SUP720          SAL15045PYS  5.1    Ok

        Mod  Online Diag Status
        ---- -------------------
        1  Pass
        2  Pass
        5  Pass
        6  Pass
    '''}

    parsed_output = {
        'slot': {
            '1': {
                'lc': {
                    'card_type': 'CEF720 48 port 10/100/1000mb Ethernet',
                    'fw_ver': '12.2(14r)S',
                    'hw_ver': '2.7',
                    'mac_address_from': '001e.4aff.ee89',
                    'mac_address_to': '001e.4aff.eeb8',
                    'model': 'WS-X6748-GE-TX',
                    'online_diag_status': 'Pass',
                    'ports': 48,
                    'serial_number': 'SAL1209HMW3',
                    'status': 'Ok',
                    'subslot': {
                        'WS-F6700-CFC': {
                            'hw_ver': '4.0',
                            'model': 'WS-F6700-CFC',
                            'serial_number': 'SAL1207G5V1',
                            'status': 'Ok',
                        },
                    },
                    'sw_ver': '15.4(0.10)',
                },
            },
            '2': {
                'lc': {
                    'card_type': '2 port adapter Enhanced FlexWAN',
                    'fw_ver': '15.4(0.10)S',
                    'hw_ver': '2.1',
                    'mac_address_from': '0015.2bff.e884',
                    'mac_address_to': '0015.2bff.e8c3',
                    'model': 'WS-X6582-2PA',
                    'online_diag_status': 'Pass',
                    'ports': 0,
                    'serial_number': 'JAE0939LYNQ',
                    'status': 'Ok',
                    'sw_ver': '15.4(0.10)S',
                },
            },
            '5': {
                'rp': {
                    'card_type': 'Supervisor Engine 720 (Hot)',
                    'fw_ver': '8.1(3',
                    'hw_ver': '4.1',
                    'mac_address_from': '0011.21ff.441a',
                    'mac_address_to': '0011.21ff.441d',
                    'model': 'WS-SUP720-3BXL',
                    'online_diag_status': 'Pass',
                    'ports': 2,
                    'serial_number': 'SAD09020BF8',
                    'status': 'Ok',
                    'subslot': {
                        'WS-F6K-PFC3BXL': {
                            'hw_ver': '1.4',
                            'model': 'WS-F6K-PFC3BXL',
                            'serial_number': 'SAD090301K6',
                            'status': 'Ok',
                        },
                        'WS-SUP720': {
                            'hw_ver': '2.2',
                            'model': 'WS-SUP720',
                            'serial_number': 'SAD090105M6',
                            'status': 'Ok',
                        },
                    },
                    'sw_ver': '15.4(0.10)',
                },
            },
            '6': {
                'rp': {
                    'card_type': 'Supervisor Engine 720 (Active)',
                    'fw_ver': '8.5(4',
                    'hw_ver': '5.12',
                    'mac_address_from': '0022.55ff.039b',
                    'mac_address_to': '0022.55ff.039e',
                    'model': 'WS-SUP720-3BXL',
                    'online_diag_status': 'Pass',
                    'ports': 2,
                    'serial_number': 'SAL15129MRC',
                    'status': 'Ok',
                    'subslot': {
                        'WS-F6K-PFC3BXL': {
                            'hw_ver': '1.11',
                            'model': 'WS-F6K-PFC3BXL',
                            'serial_number': 'SAL15129KW4',
                            'status': 'Ok',
                        },
                        'WS-SUP720': {
                            'hw_ver': '5.1',
                            'model': 'WS-SUP720',
                            'serial_number': 'SAL15045PYS',
                            'status': 'Ok',
                        },
                    },
                    'sw_ver': '15.4(0.10)',
                },
            },
        },
    }

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        version_obj = ShowModule(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            empty_parsed_output = version_obj.parse()
    
    def test_c7600(self):
        self.maxDiff = None
        self.device = Mock(**self.output_c7600)
        obj = ShowModule(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.parsed_output)

if __name__ == '__main__':
    unittest.main()