#!/bin/env python
import re
import unittest
from unittest.mock import Mock

from pyats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError

from genie.libs.parser.nxos.show_platform import (
    ShowBoot, ShowInventory, ShowInstallActive, ShowSystemRedundancyStatus,
    ShowRedundancyStatus, ShowVersion, ShowModule, Dir, ShowVdcDetail,
    ShowVdcCurrent, ShowVdcMembershipStatus, ShowProcessesCpu,
    ShowProcessesMemory, ShowCores)
ats_mock = Mock()


class test_show_version(unittest.TestCase):
    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    device2 = Device(name='cDevice')
    empty_output = {'execute.return_value': '', 'os': 'nxos'}
    semi_empty_output = {'execute.return_value': 'Cisco Nexus Operating System (NX-OS) Software', 'os': 'nxos'}
    golden_parsed_output = {'platform':
                              {'name': 'Nexus',
                               'reason': 'Reset Requested by CLI command reload',
                               'system_version': '6.2(6)',
                               'os': 'NX-OS',
                               'hardware':
                                {'bootflash': '2007040 kB',
                                 'cpu': 'Intel(R) Xeon(R) CPU',
                                 'chassis': 'Nexus7000 C7009',
                                 'rp': 'Supervisor Module-2',
                                 'device_name': 'PE1',
                                 'memory': '32938744 kB',
                                 'model': 'Nexus7000 C7009',
                                 'processor_board_id': 'JAF1708AAKL',
                                 'slot0': '7989768 kB',
                                 'slots': '9'},
                              'kernel_uptime':
                                {'days': 0,
                                 'hours': 0,
                                 'minutes': 53,
                                 'seconds': 5},
                              'software':
                                {'bios_version': '2.12.0',
                                 'bios_compile_time': '05/29/2013',
                                 'kickstart_version': '8.1(1) [build 8.1(0.129)] [gdb]',
                                 'kickstart_compile_time': '4/30/2017 23:00:00 [04/15/2017 ''04:34:05]',
                                 'kickstart_image_file': 'slot0:///n7000-s2-kickstart.10.81.0.129.gbin',
                                 'system_version': '8.1(1) [build 8.1(0.129)] [gdb]',
                                 'system_compile_time': '4/30/2017 23:00:00 [04/15/2017 ''06:43:41]',
                                 'system_image_file': 'slot0:///n7000-s2-dk10.34.1.0.129.gbin'}
                              }
                            }

    golden_parsed_output2 = {'platform':
                              {'reason': 'Unknown',
                               'os': 'NX-OS',
                               'name': 'Nexus',
                               'hardware':
                                {'bootflash': '3509454 kB',
                                 'chassis': 'NX-OSv',
                                 'rp': 'None',
                                 'slots': 'None',
                                 'cpu': 'Intel(R) Xeon(R) CPU E5-2699 v3 @ 2.30GHz',
                                 'device_name': 'N95_2',
                                 'memory': '10214428 kB',
                                 'model': 'NX-OSv',
                                 'processor_board_id': '9YH2MQQB30N'},
                              'kernel_uptime':
                                {'days': 0,
                                 'hours': 18,
                                 'minutes': 29,
                                 'seconds': 37},
                              'software':
                                {'system_version': '7.0(3)I5(2) [build 7.0(3)I5(1.145)]',
                                 'system_compile_time': '1/4/2017 20:00:00 [01/04/2017 21:47:15]',
                                 'system_image_file': 'bootflash:///ISSUCleanGolden.system.gbin'}
                              }
                            }

    golden_output = {'execute.return_value': '''

Cisco Nexus Operating System (NX-OS) Software
TAC support: http://www.cisco.com/tac
Documents: http://www.cisco.com/en/US/products/ps9372/tsd_products_support_series_home.html
Copyright (c) 2002-2017, Cisco Systems, Inc. All rights reserved.
The copyrights to certain works contained in this software are
owned by other third parties and used and distributed under
license. Certain components of this software are licensed under
the GNU General Public License (GPL) version 2.0 or the GNU
Lesser General Public License (LGPL) Version 2.1. A copy of each
such license is available at
http://www.opensource.org/licenses/gpl-2.0.php and
http://www.opensource.org/licenses/lgpl-2.1.php

Software
  BIOS:      version 2.12.0
  kickstart: version 8.1(1) [build 8.1(0.129)] [gdb]
  system:    version 8.1(1) [build 8.1(0.129)] [gdb]
  BIOS compile time:       05/29/2013
  kickstart image file is: slot0:///n7000-s2-kickstart.10.81.0.129.gbin
  kickstart compile time:  4/30/2017 23:00:00 [04/15/2017 04:34:05]
  system image file is:    slot0:///n7000-s2-dk10.34.1.0.129.gbin
  system compile time:     4/30/2017 23:00:00 [04/15/2017 06:43:41]


Hardware
  cisco Nexus7000 C7009 (9 Slot) Chassis ("Supervisor Module-2")
  Intel(R) Xeon(R) CPU         with 32938744 kB of memory.
  Processor Board ID JAF1708AAKL

  Device name: PE1
  bootflash:    2007040 kB
  slot0:        7989768 kB (expansion flash)

Kernel uptime is 0 day(s), 0 hour(s), 53 minute(s), 5 second(s)

Last reset at 885982 usecs after  Wed Apr 19 10:23:31 2017

  Reason: Reset Requested by CLI command reload
  System version: 6.2(6)
  Service:

plugin
  Core Plugin, Ethernet Plugin

Active Package(s)

''', 'os': 'nxos'}

    golden_output2 = {'execute.return_value': '''

Cisco Nexus Operating System (NX-OS) Software
TAC support: http://www.cisco.com/tac
Documents: http://www.cisco.com/en/US/products/ps9372/tsd_products_support_series_home.html
Copyright (c) 2002-2017, Cisco Systems, Inc. All rights reserved.
The copyrights to certain works contained herein are owned by
other third parties and are used and distributed under license.
Some parts of this software are covered under the GNU Public
License. A copy of the license is available at
http://www.gnu.org/licenses/gpl.html.

NX-OSv9K is a demo version of the Nexus Operating System

Software
  BIOS: version
  NXOS: version 7.0(3)I5(2) [build 7.0(3)I5(1.145)]
  BIOS compile time:
  NXOS image file is: bootflash:///ISSUCleanGolden.system.gbin
  NXOS compile time:  1/4/2017 20:00:00 [01/04/2017 21:47:15]


Hardware
  cisco NX-OSv Chassis
  Intel(R) Xeon(R) CPU E5-2699 v3 @ 2.30GHz with 10214428 kB of memory.
  Processor Board ID 9YH2MQQB30N

  Device name: N95_2
  bootflash:    3509454 kB
Kernel uptime is 0 day(s), 18 hour(s), 29 minute(s), 37 second(s)

Last reset
  Reason: Unknown
  System version:
  Service:

plugin
  Core Plugin, Ethernet Plugin

Active Package(s):

''', 'os': 'nxos'}

    golden_output3 = {'execute.return_value': '''

        Cisco Nexus Operating System (NX-OS) Software
        TAC support: http://www.cisco.com/tac
        Documents: http://www.cisco.com/en/US/products/ps9372/tsd_products_support_series_home.html
        Copyright (c) 2002-2018, Cisco Systems, Inc. All rights reserved.
        The copyrights to certain works contained herein are owned by
        other third parties and are used and distributed under license.
        Some parts of this software are covered under the GNU Public
        License. A copy of the license is available at
        http://www.gnu.org/licenses/gpl.html.

        Software
          BIOS:      version 3.6.0
          Power Sequencer Firmware:
                     Module 1: v7.0
                     Module 1: v1.0
                     Module 3: v1.0
          Microcontroller Firmware:        version v10.1.0.2
          QSFP Microcontroller Firmware:
                     Module 3: v0.0.0.0
          CXP Microcontroller Firmware:
                     Module not detected
          kickstart: version 7.3(3)N1(1)
          system:    version 7.3(3)N1(1)
          BIOS compile time:       05/09/2012
          kickstart image file is: bootflash:///n5000-uk9-kickstart.7.3.3.N1.1.bin
          kickstart compile time:  4/27/2018 9:00:00 [04/27/2018 17:18:59]
          system image file is:    bootflash:///n5000-uk10.1.3.3.N1.1.bin
          system compile time:     4/27/2018 9:00:00 [04/27/2018 21:24:41]


        Hardware
          cisco Nexus 5596 Chassis ("O2 48X10GE/Modular Supervisor")
          Intel(R) Xeon(R) CPU         with 8253792 kB of memory.
          Processor Board ID FOC171850PP

          Device name: sample_5k
          bootflash:    2007040 kB

        Kernel uptime is 289 day(s), 16 hour(s), 36 minute(s), 32 second(s)

        Last reset at 463212 usecs after  Thu Jan 24 05:58:41 2019

          Reason: Disruptive upgrade
          System version: 7.0(8)N1(1)
          Service:

        plugin
          Core Plugin, Ethernet Plugin, Fc Plugin

        Active Package(s)

        '''}

    golden_parsed_output3 = {'platform': {
                               'os': 'NX-OS',
                               'name': 'Nexus',
                               'reason': 'Disruptive upgrade',
                               'hardware':
                                {'model': 'Nexus 5596',
                                 'chassis': 'Nexus 5596',
                                 'rp': 'O2 48X10GE/Modular Supervisor',
                                 'slots': 'None',
                                 'cpu': 'Intel(R) Xeon(R) CPU',
                                 'device_name': 'sample_5k',
                                 'memory': '8253792 kB',
                                 'bootflash': '2007040 kB',
                                 'processor_board_id': 'FOC171850PP'},
                              'kernel_uptime':
                                {'days': 289,
                                 'hours': 16,
                                 'minutes': 36,
                                 'seconds': 32},
                              'software':
                                {'bios_version': '3.6.0',
                                 'kickstart_version': '7.3(3)N1(1)',
                                 'system_version': '7.3(3)N1(1)',
                                 'bios_compile_time': '05/09/2012',
                                 'kickstart_image_file': 'bootflash:///n5000-uk9-kickstart.7.3.3.N1.1.bin',
                                 'kickstart_compile_time': '4/27/2018 9:00:00 [04/27/2018 17:18:59]',
                                 'system_image_file': 'bootflash:///n5000-uk10.1.3.3.N1.1.bin',
                                 'system_compile_time': '4/27/2018 9:00:00 [04/27/2018 21:24:41]'}
                              }
                            }

    golden_output4 = {'execute.return_value': '''

        Cisco Nexus Operating System (NX-OS) Software
        TAC support: http://www.cisco.com/tac
        Documents: http://www.cisco.com/en/US/products/ps9372/tsd_products_support_series_home.html
        Copyright (c) 2002-2017, Cisco Systems, Inc. All rights reserved.
        The copyrights to certain works contained herein are owned by
        other third parties and are used and distributed under license.
        Some parts of this software are covered under the GNU Public
        License. A copy of the license is available at
        http://www.gnu.org/licenses/gpl.html.

        Software
          BIOS:      version 1.4.0
          loader:    version N/A
          kickstart: version 6.0(2)U6(10)
          system:    version 6.0(2)U6(10)
          Power Sequencer Firmware:
                     Module 1: version v4.4
          BIOS compile time:       12/09/2013
          kickstart image file is: bootflash:///n3000-uk9-kickstart.6.0.2.U6.10.bin
          kickstart compile time:  3/30/2017 9:00:00 [03/30/2017 19:37:34]
          system image file is:    bootflash:///n3000-uk10.225.0.2.U6.10.bin
          system compile time:     3/30/2017 9:00:00 [03/30/2017 20:04:06]


        Hardware
          cisco Nexus 3048 Chassis ("48x1GE + 4x10G Supervisor")
          Intel(R) Celeron(R) CPU        P4505  @ 1.87GHz with 3665288 kB of memory.
          Processor Board ID FOC19243WQN

          Device name: n3k
          bootflash:    2007040 kB

        Kernel uptime is 796 day(s), 15 hour(s), 58 minute(s), 29 second(s)

        Last reset at 2131 usecs after  Thu Jan 18 21:17:51 2018

          Reason: Disruptive upgrade
          System version: 6.0(2)U6(5b)
          Service:

        plugin
          Core Plugin, Ethernet Plugin


        '''}

    golden_parsed_output4 = {'platform': {
                               'os': 'NX-OS',
                               'name': 'Nexus',
                               'reason': 'Disruptive upgrade',
                               'hardware':
                                {'model': 'Nexus 3048',
                                 'chassis': 'Nexus 3048',
                                 'rp': '48x1GE + 4x10G Supervisor',
                                 'slots': 'None',
                                 'cpu': 'Intel(R) Celeron(R) CPU        P4505  @ 1.87GHz',
                                 'device_name': 'n3k',
                                 'memory': '3665288 kB',
                                 'bootflash': '2007040 kB',
                                 'processor_board_id': 'FOC19243WQN'},
                              'kernel_uptime':
                                {'days': 796,
                                 'hours': 15,
                                 'minutes': 58,
                                 'seconds': 29},
                              'software':
                                {'bios_version': '1.4.0',
                                 'kickstart_version': '6.0(2)U6(10)',
                                 'system_version': '6.0(2)U6(10)',
                                 'bios_compile_time': '12/09/2013',
                                 'kickstart_image_file': 'bootflash:///n3000-uk9-kickstart.6.0.2.U6.10.bin',
                                 'kickstart_compile_time': '3/30/2017 9:00:00 [03/30/2017 19:37:34]',
                                 'system_image_file': 'bootflash:///n3000-uk10.225.0.2.U6.10.bin',
                                 'system_compile_time': '3/30/2017 9:00:00 [03/30/2017 20:04:06]'}
                              }
                            }

    ats_mock.tcl.eval.return_value = 'nxos'

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        version_obj = ShowVersion(device=self.device)
        parsed_output = version_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        version_obj = ShowVersion(device=self.device)
        parsed_output = version_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output2)

    def test_golden3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        version_obj = ShowVersion(device=self.device)
        parsed_output = version_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output3)

    def test_golden4(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output4)
        version_obj = ShowVersion(device=self.device)
        parsed_output = version_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output4)

    def test_empty(self):
        self.device2 = Mock(**self.empty_output)
        version_obj = ShowVersion(device=self.device2)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = version_obj.parse()


class test_show_inventory(unittest.TestCase):
    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {'name':
                                {'Chassis':
                                    {'description': 'Nexus7000 C7009 (9 Slot) Chassis ',
                                     'pid': 'N7K-C7009',
                                     'slot': 'None',
                                     'vid': 'V01',
                                     'serial_number': 'JAF1704ARQG'},
                                 'Slot 1':
                                    {'description': 'Supervisor Module-2',
                                     'pid': 'N7K-SUP2',
                                     'slot': '1',
                                     'vid': 'V01',
                                     'serial_number': 'JAF1708AGTH'},
                                 'Slot 2':
                                    {'description': 'Supervisor Module-2',
                                     'pid': 'N7K-SUP2',
                                     'slot': '2',
                                     'vid': 'V01',
                                     'serial_number': 'JAF1708AGQH'},
                                 'Slot 3':
                                    {'description': '1/10 Gbps Ethernet Module',
                                     'pid': 'N7K-F248XP-25E',
                                     'slot': '3',
                                     'vid': 'V01',
                                     'serial_number': 'JAF1717AAND'},
                                 'Slot 4':
                                    {'description': '10/40 Gbps Ethernet Module',
                                     'pid': 'N7K-F312FQ-25',
                                     'slot': '4',
                                     'vid': 'V01',
                                     'serial_number': 'JAE18120FLU'},
                                 'Slot 33':
                                    {'description': 'Nexus7000 C7009 (9 Slot) Chassis Power Supply',
                                     'pid': 'N7K-AC-6.0KW',
                                     'slot': '33',
                                     'vid': 'V03',
                                     'serial_number': 'DTM171300QB'},
                                 'Slot 35':
                                    {'description': 'Nexus7000 C7009 (9 Slot) Chassis Fan Module',
                                     'pid': 'N7K-C7009-FAN',
                                     'slot': '35',
                                     'vid': 'V01',
                                     'serial_number': 'JAF1702AEBE'}
                                }
                            }

    golden_output = {'execute.return_value': '''

        NAME: "Chassis",  DESCR: "Nexus7000 C7009 (9 Slot) Chassis "
        PID: N7K-C7009           ,  VID: V01 ,  SN: JAF1704ARQG

        NAME: "Slot 1",  DESCR: "Supervisor Module-2"
        PID: N7K-SUP2            ,  VID: V01 ,  SN: JAF1708AGTH

        NAME: "Slot 2",  DESCR: "Supervisor Module-2"
        PID: N7K-SUP2            ,  VID: V01 ,  SN: JAF1708AGQH

        NAME: "Slot 3",  DESCR: "1/10 Gbps Ethernet Module"
        PID: N7K-F248XP-25E      ,  VID: V01 ,  SN: JAF1717AAND

        NAME: "Slot 4",  DESCR: "10/40 Gbps Ethernet Module"
        PID: N7K-F312FQ-25       ,  VID: V01 ,  SN: JAE18120FLU

        NAME: "Slot 33",  DESCR: "Nexus7000 C7009 (9 Slot) Chassis Power Supply"
        PID: N7K-AC-6.0KW        ,  VID: V03 ,  SN: DTM171300QB

        NAME: "Slot 35",  DESCR: "Nexus7000 C7009 (9 Slot) Chassis Fan Module"
        PID: N7K-C7009-FAN       ,  VID: V01 ,  SN: JAF1702AEBE

    '''}

    golden_parsed_output1 = {
        'name': {
            'Slot 38': {
                'description': 'Nexus7700 C7706 (6 Slot) Chassis Fan Module',
                'slot': '38',
                'pid': 'N77-C7706-FAN',
                'vid': 'V01',
                'serial_number': 'DCH212300ZQ',
            },
            'Slot 39': {
                'description': 'Nexus7700 C7706 (6 Slot) Chassis Fan Module',
                'slot': '39',
                'pid': 'N77-C7706-FAN',
                'vid': 'V01',
                'serial_number': 'DCH212300ZR',
            },
            'FEX 106 CHASSIS': {
                'description': 'N2K-C2248TP-E-1GE  CHASSIS',
                'slot': 'None',
                'pid': 'N2K-C2248TP-E-1GE',
                'vid': 'V03',
                'serial_number': 'FOX2129PR28',
            },
            'FEX 106 Module 1': {
                'description': 'Fabric Extender Module: 48x1GE, 4x10GE Supervisor',
                'slot': 'None',
                'pid': 'N2K-C2248TP-E-1GE',
                'vid': 'V03',
                'serial_number': 'FOC21306SY6',
            },
            'FEX 106 Fan 1': {
                'description': 'Fabric Extender Fan module',
                'slot': 'None',
                'pid': 'N2K-C2248-FAN',
                'vid': 'N/A',
                'serial_number': 'N/A',
            },
            'FEX 106 Power Supply 1': {
                'description': 'Fabric Extender AC power supply',
                'slot': 'None',
                'pid': 'N2200-PAC-400W',
                'vid': 'V06',
                'serial_number': 'DCA21265683',
            },
            'FEX 106 Power Supply 2': {
                'description': 'Fabric Extender AC power supply',
                'slot': 'None',
                'pid': 'N2200-PAC-400W',
                'vid': 'V06',
                'serial_number': 'DCA21265681',
            },
            'FEX 108 CHASSIS': {
                'description': 'N2K-C2248TP-E-1GE  CHASSIS',
                'slot': 'None',
                'pid': 'N2K-C2248TP-E-1GE',
                'vid': 'V03',
                'serial_number': 'FOX2131P982',
            },
            'FEX 108 Module 1': {
                'description': 'Fabric Extender Module: 48x1GE, 4x10GE Supervisor',
                'slot': 'None',
                'pid': 'N2K-C2248TP-E-1GE',
                'vid': 'V03',
                'serial_number': 'FOC21306TAS',
            },
            'FEX 108 Fan 1': {
                'description': 'Fabric Extender Fan module',
                'slot': 'None',
                'pid': 'N2K-C2248-FAN',
                'vid': 'N/A',
                'serial_number': 'N/A',
            },
        },
    }
    golden_output1 = {'execute.return_value': '''
        show inventory
        NAME: "Slot 38",  DESCR: "Nexus7700 C7706 (6 Slot) Chassis Fan Module"
        PID: N77-C7706-FAN       ,  VID: V01 ,  SN: DCH212300ZQ

        NAME: "Slot 39",  DESCR: "Nexus7700 C7706 (6 Slot) Chassis Fan Module"
        PID: N77-C7706-FAN       ,  VID: V01 ,  SN: DCH212300ZR

        NAME: "FEX 106 CHASSIS",  DESCR: "N2K-C2248TP-E-1GE  CHASSIS"
        PID: N2K-C2248TP-E-1GE   ,  VID: V03 ,  SN: FOX2129PR28

        NAME: "FEX 106 Module 1",  DESCR: "Fabric Extender Module: 48x1GE, 4x10GE Supervisor"
        PID: N2K-C2248TP-E-1GE   ,  VID: V03 ,  SN: FOC21306SY6

        NAME: "FEX 106 Fan 1",  DESCR: "Fabric Extender Fan module"
        PID: N2K-C2248-FAN       ,  VID: N/A ,  SN: N/A

        NAME: "FEX 106 Power Supply 1",  DESCR: "Fabric Extender AC power supply"
        PID: N2200-PAC-400W      ,  VID: V06 ,  SN: DCA21265683

        NAME: "FEX 106 Power Supply 2",  DESCR: "Fabric Extender AC power supply"
        PID: N2200-PAC-400W      ,  VID: V06 ,  SN: DCA21265681

        NAME: "FEX 108 CHASSIS",  DESCR: "N2K-C2248TP-E-1GE  CHASSIS"
        PID: N2K-C2248TP-E-1GE   ,  VID: V03 ,  SN: FOX2131P982

        NAME: "FEX 108 Module 1",  DESCR: "Fabric Extender Module: 48x1GE, 4x10GE Supervisor"
        PID: N2K-C2248TP-E-1GE   ,  VID: V03 ,  SN: FOC21306TAS

        NAME: "FEX 108 Fan 1",  DESCR: "Fabric Extender Fan module"
        PID: N2K-C2248-FAN       ,  VID: N/A ,  SN: N/A
    '''}

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        inventory_obj = ShowInventory(device=self.device)
        parsed_output = inventory_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        inventory_obj = ShowInventory(device=self.device)
        parsed_output = inventory_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        inventory_obj = ShowInventory(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = inventory_obj.parse()

class test_show_install_active(unittest.TestCase):
    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {'boot_images':
                              {'kickstart_image': 'slot0:/n7000-s2-kickstart.8.3.0.CV.0.658.gbin',
                               'system_image': 'slot0:/n7000-s2-dk10.34.3.0.CV.0.658.gbin'},
                            'active_packages':
                              {'active_package_module_0':
                                {'active_package_name': 'n7700-s2-dk10.1.2.0.D1.1.CSCuo7721.bin'},
                               'active_package_module_3':
                                {'active_package_name': 'n7700-s2-dk10.1.2.0.D1.1.CSCuo7721.bin'}
                              }
                            }

    golden_output = {'execute.return_value': '''

    Boot Images:
            Kickstart Image: slot0:/n7000-s2-kickstart.8.3.0.CV.0.658.gbin
            System Image: slot0:/n7000-s2-dk10.34.3.0.CV.0.658.gbin

    Active Packages:

            n7700-s2-dk10.1.2.0.D1.1.CSCuo7721.bin

    Active Packages on Module #3:

            n7700-s2-dk10.1.2.0.D1.1.CSCuo7721.bin

    Active Packages on Module #4:


    Active Packages on Module #6:


    Active Packages on Module #7:


    Active Packages on Module #8:

'''}

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        active_obj = ShowInstallActive(device=self.device)
        parsed_output = active_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        active_obj = ShowInstallActive(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = active_obj.parse()

class test_show_system_redundancy_status(unittest.TestCase):
    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {'redundancy_mode':
                            {'administrative': 'HA',
                             'operational': 'HA'},
                            'supervisor_1':
                              {'redundancy_state': 'Active',
                               'supervisor_state': 'Active',
                               'internal_state':'Active with HA standby'},
                            'supervisor_2':
                              {'redundancy_state': 'Standby',
                               'supervisor_state': 'HA standby',
                               'internal_state':'HA standby'},
                          }

    golden_output = {'execute.return_value': '''

    Redundancy mode
    ---------------
          administrative:   HA
             operational:   HA

    This supervisor (sup-1)
    -----------------------
        Redundancy state:   Active
        Supervisor state:   Active
          Internal state:   Active with HA standby

    Other supervisor (sup-2)
    ------------------------
        Redundancy state:   Standby
        Supervisor state:   HA standby
          Internal state:   HA standby

'''}

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        redundancy_obj = ShowSystemRedundancyStatus(device=self.device)
        parsed_output = redundancy_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        redundancy_obj = ShowSystemRedundancyStatus(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = redundancy_obj.parse()

class test_show_redundancy_status(unittest.TestCase):
    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {'redundancy_mode':
                              {'administrative': 'HA',
                               'operational': 'HA'},
                            'supervisor_1':
                              {'redundancy_state': 'Active',
                               'supervisor_state': 'Active',
                               'internal_state':'Active with HA standby'},
                            'supervisor_2':
                              {'redundancy_state': 'Standby',
                               'supervisor_state': 'HA standby',
                               'internal_state':'HA standby'},
                            'system_start_time': 'Fri Apr 21 01:53:24 2017',
                            'system_uptime': '0 days, 7 hours, 57 minutes, 30 seconds',
                            'kernel_uptime': '0 days, 8 hours, 0 minutes, 56 seconds',
                            'active_supervisor_time': '0 days, 7 hours, 57 minutes, 30 seconds'}

    golden_output = {'execute.return_value': '''

    Redundancy mode
    ---------------
          administrative:   HA
             operational:   HA

    This supervisor (sup-1)
    -----------------------
        Redundancy state:   Active
        Supervisor state:   Active
          Internal state:   Active with HA standby

    Other supervisor (sup-2)
    ------------------------
        Redundancy state:   Standby

        Supervisor state:   HA standby
          Internal state:   HA standby

    System start time:          Fri Apr 21 01:53:24 2017

    System uptime:              0 days, 7 hours, 57 minutes, 30 seconds
    Kernel uptime:              0 days, 8 hours, 0 minutes, 56 seconds
    Active supervisor uptime:   0 days, 7 hours, 57 minutes, 30 seconds

'''}

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        redundancy_obj = ShowRedundancyStatus(device=self.device)
        parsed_output = redundancy_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        redundancy_obj = ShowRedundancyStatus(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = redundancy_obj.parse()

class test_show_boot(unittest.TestCase):
    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {'current_boot_variable':
                                {'sup_number':
                                    {'sup-1':
                                        {'kickstart_variable': 'slot0:/n7000-s2-kickstart.8.3.0.CV.0.658.gbin',
                                         'system_variable': 'slot0:/n7000-s2-dk10.34.3.0.CV.0.658.gbin',
                                         'boot_poap':'Disabled'},
                                     'sup-2':
                                        {'kickstart_variable': 'slot0:/n7000-s2-kickstart.8.3.0.CV.0.658.gbin',
                                         'system_variable': 'slot0:/n7000-s2-dk10.34.3.0.CV.0.658.gbin',
                                         'boot_poap':'Disabled'}
                                    }
                                },
                            'next_reload_boot_variable':
                                {'sup_number':
                                    {'sup-1':
                                        {'kickstart_variable': 'slot0:/n7000-s2-kickstart.8.3.0.CV.0.658.gbin',
                                         'system_variable': 'slot0:/n7000-s2-dk10.34.3.0.CV.0.658.gbin',
                                         'boot_poap':'Disabled'},
                                     'sup-2':
                                        {'kickstart_variable': 'slot0:/n7000-s2-kickstart.8.3.0.CV.0.658.gbin',
                                         'system_variable': 'slot0:/n7000-s2-dk10.34.3.0.CV.0.658.gbin',
                                         'boot_poap':'Disabled'}
                                    }
                                }
                            }

    golden_output = {'execute.return_value': '''

    Current Boot Variables:

    sup-1
    kickstart variable = slot0:/n7000-s2-kickstart.8.3.0.CV.0.658.gbin
    system variable = slot0:/n7000-s2-dk10.34.3.0.CV.0.658.gbin
    Boot POAP Disabled
    sup-2
    kickstart variable = slot0:/n7000-s2-kickstart.8.3.0.CV.0.658.gbin
    system variable = slot0:/n7000-s2-dk10.34.3.0.CV.0.658.gbin
    Boot POAP Disabled
    No module boot variable set

    Boot Variables on next reload:

    sup-1
    kickstart variable = slot0:/n7000-s2-kickstart.8.3.0.CV.0.658.gbin
    system variable = slot0:/n7000-s2-dk10.34.3.0.CV.0.658.gbin
    Boot POAP Disabled
    sup-2
    kickstart variable = slot0:/n7000-s2-kickstart.8.3.0.CV.0.658.gbin
    system variable = slot0:/n7000-s2-dk10.34.3.0.CV.0.658.gbin
    Boot POAP Disabled
    No module boot variable set

'''}

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        boot_obj = ShowBoot(device=self.device)
        parsed_output = boot_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        boot_obj = ShowBoot(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = boot_obj.parse()

class test_show_boot_without_sup(unittest.TestCase):
    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    device2 = Device(name='cDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {'current_boot_variable':
                                          {'kickstart_variable': 'bootflash:/n6000-uk9-kickstart.7.3.2.N1.0.420.bin',
                                           'system_variable': 'bootflash:/n6000-uk10.1.3.2.N1.0.420.bin',
                                           'boot_poap':'Disabled'},
                                        'next_reload_boot_variable':
                                          {'kickstart_variable': 'bootflash:/n6000-uk9-kickstart.7.3.2.N1.0.420.bin',
                                           'system_variable': 'bootflash:/n6000-uk10.1.3.2.N1.0.420.bin',
                                           'boot_poap':'Disabled'}
                                      }

    golden_output = {'execute.return_value': '''

    Current Boot Variables:


    kickstart variable = bootflash:/n6000-uk9-kickstart.7.3.2.N1.0.420.bin
    system variable = bootflash:/n6000-uk10.1.3.2.N1.0.420.bin
    Boot POAP Disabled

    Boot Variables on next reload:


    kickstart variable = bootflash:/n6000-uk9-kickstart.7.3.2.N1.0.420.bin
    system variable = bootflash:/n6000-uk10.1.3.2.N1.0.420.bin
    Boot POAP Disabled

'''}

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        boot_obj = ShowBoot(device=self.device)
        parsed_output = boot_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        boot_obj = ShowBoot(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = boot_obj.parse()

class test_show_module(unittest.TestCase):
    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {'slot':
                                {'rp':
                                  {'1':
                                    {'Supervisor Module-2':
                                      {'ports': '0',
                                       'model': 'N7K-SUP2',
                                       'status': 'active',
                                       'software': '8.3(0)CV(0.658)',
                                       'hardware': '1.0',
                                       'mac_address': '84-78-ac-ff-d3-dc to 84-78-ac-ff-d3-ee',
                                       'serial_number': 'JAF1708AGTH',
                                       'online_diag_status': 'Pass'}
                                    },
                                  '2':
                                    {'Supervisor Module-2':
                                      {'ports': '0',
                                       'model': 'N7K-SUP2',
                                       'status': 'ha-standby',
                                       'software': '8.3(0)CV(0.658)',
                                       'hardware': '1.0',
                                       'mac_address': '84-78-ac-ff-c8-0f to 84-78-ac-ff-c8-21',
                                       'serial_number': 'JAF1708AGQH',
                                       'online_diag_status': 'Pass'}
                                    }
                                  },
                                'lc':
                                  {'3':
                                    {'1/10 Gbps Ethernet Module':
                                      {'ports': '48',
                                       'model': 'N7K-F248XP-25E',
                                       'status': 'ok',
                                       'software': '8.3(0)CV(0.658)',
                                       'hardware': '1.0',
                                       'mac_address': '84-78-ac-ff-f5-48 to 84-78-ac-ff-f5-7b',
                                       'serial_number': 'JAF1717AAND',
                                       'online_diag_status': 'Pass'}
                                    },
                                  '4':
                                    {'10/40 Gbps Ethernet Module':
                                      {'ports': '12',
                                       'model': 'N7K-F312FQ-25',
                                       'status': 'ok',
                                       'software': '8.3(0)CV(0.658)',
                                       'hardware': '1.0',
                                       'mac_address': '54-4a-00-ff-c6-ed to 54-4a-00-ff-c6-29',
                                       'serial_number': 'JAE18120FLU',
                                       'online_diag_status': 'Pass'}
                                    },
                                  '6':
                                    {'10 Gbps Ethernet XL Module':
                                      {'ports': '32',
                                       'model': 'N7K-M132XP-12L',
                                       'status': 'ok',
                                       'software': '8.3(0)CV(0.658)',
                                       'hardware': '2.0',
                                       'mac_address': 'bc-16-65-ff-04-b8 to bc-16-65-ff-04-db',
                                       'serial_number': 'JAF1719AHMB',
                                       'online_diag_status': 'Pass'}
                                    },
                                  '7':
                                    {'10 Gbps Ethernet Module':
                                      {'ports': '24',
                                       'model': 'N7K-M224XP-23L',
                                       'status': 'ok',
                                       'software': '8.3(0)CV(0.658)',
                                       'hardware': '1.0',
                                       'mac_address': 'd8-67-d9-ff-9f-d6 to d8-67-d9-ff-9f-f1',
                                       'serial_number': 'JAF1641APPF',
                                       'online_diag_status': 'Pass'}
                                    },
                                  '8':
                                    {'10/100/1000 Mbps Ethernet XL Module':
                                      {'ports': '48',
                                       'model': 'N7K-M148GT-11L',
                                       'status': 'ok',
                                       'software': '8.3(0)CV(0.658)',
                                       'hardware': '2.1',
                                       'mac_address': 'bc-16-65-ff-f2-0b to bc-16-65-ff-f3-3d',
                                       'serial_number': 'JAF1717BEAT',
                                       'online_diag_status': 'Pass'}
                                    }
                                  }
                                },
                            'xbar':
                              {'1':
                                  {'ports': '0',
                                   'module_type': 'Fabric Module 2',
                                   'model': 'N7K-C7009-FAB-2',
                                   'status': 'ok',
                                   'software': 'NA',
                                   'hardware': '3.1',
                                   'mac_address': 'NA',
                                   'serial_number': 'JAF1705AEEF'},
                              '2':
                                  {'ports': '0',
                                   'module_type': 'Fabric Module 2',
                                   'model': 'N7K-C7009-FAB-2',
                                   'status': 'ok',
                                   'software': 'NA',
                                   'hardware': '3.1',
                                   'mac_address': 'NA',
                                   'serial_number': 'JAF1705BFBM'},
                              '3':
                                  {'ports': '0',
                                   'module_type': 'Fabric Module 2',
                                   'model': 'N7K-C7009-FAB-2',
                                   'status': 'ok',
                                   'software': 'NA',
                                   'hardware': '3.1',
                                   'mac_address': 'NA',
                                   'serial_number': 'JAF1705AELK'},
                              '4':
                                  {'ports': '0',
                                   'module_type': 'Fabric Module 2',
                                   'model': 'N7K-C7009-FAB-2',
                                   'status': 'ok',
                                   'software': 'NA',
                                   'hardware': '3.1',
                                   'mac_address': 'NA',
                                   'serial_number': 'JAF1705BFCF'},
                              '5':
                                  {'ports': '0',
                                   'module_type': 'Fabric Module 2',
                                   'model': 'N7K-C7009-FAB-2',
                                   'status': 'ok',
                                   'software': 'NA',
                                   'hardware': '3.1',
                                   'mac_address': 'NA',
                                   'serial_number': 'JAF1704APQH'}
                              }
                          }

    golden_output = {'execute.return_value': '''

    Mod  Ports  Module-Type                         Model              Status
    ---  -----  ----------------------------------- ------------------ ----------
    1    0      Supervisor Module-2                 N7K-SUP2           active *
    2    0      Supervisor Module-2                 N7K-SUP2           ha-standby
    3    48     1/10 Gbps Ethernet Module           N7K-F248XP-25E     ok
    4    12     10/40 Gbps Ethernet Module          N7K-F312FQ-25      ok
    6    32     10 Gbps Ethernet XL Module          N7K-M132XP-12L     ok
    7    24     10 Gbps Ethernet Module             N7K-M224XP-23L     ok
    8    48     10/100/1000 Mbps Ethernet XL Module N7K-M148GT-11L     ok

    Mod  Sw               Hw
    ---  ---------------  ------
    1    8.3(0)CV(0.658)  1.0
    2    8.3(0)CV(0.658)  1.0
    3    8.3(0)CV(0.658)  1.0
    4    8.3(0)CV(0.658)  1.0
    6    8.3(0)CV(0.658)  2.0
    7    8.3(0)CV(0.658)  1.0
    8    8.3(0)CV(0.658)  2.1



    Mod  MAC-Address(es)                         Serial-Num
    ---  --------------------------------------  ----------
    1    84-78-ac-ff-d3-dc to 84-78-ac-ff-d3-ee  JAF1708AGTH
    2    84-78-ac-ff-c8-0f to 84-78-ac-ff-c8-21  JAF1708AGQH
    3    84-78-ac-ff-f5-48 to 84-78-ac-ff-f5-7b  JAF1717AAND
    4    54-4a-00-ff-c6-ed to 54-4a-00-ff-c6-29  JAE18120FLU
    6    bc-16-65-ff-04-b8 to bc-16-65-ff-04-db  JAF1719AHMB
    7    d8-67-d9-ff-9f-d6 to d8-67-d9-ff-9f-f1  JAF1641APPF
    8    bc-16-65-ff-f2-0b to bc-16-65-ff-f3-3d  JAF1717BEAT

    Mod  Online Diag Status
    ---  ------------------
    1    Pass
    2    Pass
    3    Pass
    4    Pass
    6    Pass
    7    Pass
    8    Pass

    Xbar Ports  Module-Type                         Model              Status
    ---  -----  ----------------------------------- ------------------ ----------
    1    0      Fabric Module 2                     N7K-C7009-FAB-2    ok
    2    0      Fabric Module 2                     N7K-C7009-FAB-2    ok
    3    0      Fabric Module 2                     N7K-C7009-FAB-2    ok
    4    0      Fabric Module 2                     N7K-C7009-FAB-2    ok
    5    0      Fabric Module 2                     N7K-C7009-FAB-2    ok

    Xbar Sw               Hw
    ---  ---------------  ------
    1    NA               3.1
    2    NA               3.1
    3    NA               3.1
    4    NA               3.1
    5    NA               3.1



    Xbar MAC-Address(es)                         Serial-Num
    ---  --------------------------------------  ----------
    1    NA                                      JAF1705AEEF
    2    NA                                      JAF1705BFBM
    3    NA                                      JAF1705AELK
    4    NA                                      JAF1705BFCF
    5    NA                                      JAF1704APQH

    * this terminal session


'''}

    output = {'execute.return_value': '''
        Mod Ports             Module-Type                       Model          Status
        --- ----- ------------------------------------- --------------------- ---------
        1    52   48x1/10G SFP+ 4x40G Ethernet Module   N9K-X9564PX           ok
        22   0    Fabric Module                         N9K-C9504-FM          ok
        24   0    Fabric Module                         N9K-C9504-FM          ok
        26   0    Fabric Module                         N9K-C9504-FM          ok
        27   0    Supervisor Module                     N9K-SUP-A             ha-standby
        28   0    Supervisor Module                     N9K-SUP-A             active *
        29   0    System Controller                     N9K-SC-A              active
        30   0    System Controller                     N9K-SC-A              standby

        Mod  Sw                Hw     Slot
        ---  ----------------  ------ ----
        1    7.0(3)I5(0.125)   1.3    LC1
        22   7.0(3)I5(0.125)   1.1    FM2
        24   7.0(3)I5(0.125)   1.1    FM4
        26   7.0(3)I5(0.125)   1.1    FM6
        27   7.0(3)I5(0.125)   1.4    SUP1
        28   7.0(3)I5(0.125)   1.4    SUP2
        29   7.0(3)I5(0.125)   1.4    SC1
        30   7.0(3)I5(0.125)   1.4    SC2


        Mod  MAC-Address(es)                         Serial-Num
        ---  --------------------------------------  ----------
        1    88-1d-fc-ff-68-71 to 88-1d-fc-ff-69-b3  SAL18422J9D
        22   NA                                      SAL18401T5J
        24   NA                                      SAL18401T2L
        26   NA                                      SAL18401T5S
        27   e4-c7-22-ff-bf-ca to e4-c7-22-ff-bf-db  SAL18422LG1
        28   e4-c7-22-ff-af-64 to e4-c7-22-ff-af-75  SAL18412064
        29   NA                                      SAL18422HKT
        30   NA                                      SAL18422HKA

        Mod  Online Diag Status
        ---  ------------------
        1    Pass
        22   Pass
        24   Pass
        26   Pass
        27   Pass
        28   Pass
        29   Pass
        30   Pass
        '''
    }

    parsed_output_1 = {
        "slot": {
            "rp": {
                 "28": {
                      "Supervisor Module": {
                           "online_diag_status": "Pass",
                           "ports": "0",
                           "model": "N9K-SUP-A",
                           "software": "7.0(3)I5(0.125)",
                           "serial_number": "SAL18412064",
                           "hardware": "1.4",
                           "status": "active",
                           "slot/world_wide_name": "SUP2",
                           "mac_address": "e4-c7-22-ff-af-64 to e4-c7-22-ff-af-75"
                      }
                 },
                 "27": {
                      "Supervisor Module": {
                           "online_diag_status": "Pass",
                           "ports": "0",
                           "model": "N9K-SUP-A",
                           "software": "7.0(3)I5(0.125)",
                           "serial_number": "SAL18422LG1",
                           "hardware": "1.4",
                           "status": "ha-standby",
                           "slot/world_wide_name": "SUP1",
                           "mac_address": "e4-c7-22-ff-bf-ca to e4-c7-22-ff-bf-db"
                      }
                 }
            },
            "lc": {
                 "1": {
                      "48x1/10G SFP+ 4x40G Ethernet Module": {
                           "online_diag_status": "Pass",
                           "ports": "52",
                           "model": "N9K-X9564PX",
                           "software": "7.0(3)I5(0.125)",
                           "serial_number": "SAL18422J9D",
                           "hardware": "1.3",
                           "status": "ok",
                           "slot/world_wide_name": "LC1",
                           "mac_address": "88-1d-fc-ff-68-71 to 88-1d-fc-ff-69-b3"
                      }
                 },
                 "26": {
                      "Fabric Module": {
                           "online_diag_status": "Pass",
                           "ports": "0",
                           "model": "N9K-C9504-FM",
                           "software": "7.0(3)I5(0.125)",
                           "serial_number": "SAL18401T5S",
                           "hardware": "1.1",
                           "status": "ok",
                           "slot/world_wide_name": "FM6",
                           "mac_address": "NA"
                      }
                 },
                 "30": {
                      "System Controller": {
                           "online_diag_status": "Pass",
                           "ports": "0",
                           "model": "N9K-SC-A",
                           "software": "7.0(3)I5(0.125)",
                           "serial_number": "SAL18422HKA",
                           "hardware": "1.4",
                           "status": "standby",
                           "slot/world_wide_name": "SC2",
                           "mac_address": "NA"
                      }
                 },
                 "29": {
                      "System Controller": {
                           "online_diag_status": "Pass",
                           "ports": "0",
                           "model": "N9K-SC-A",
                           "software": "7.0(3)I5(0.125)",
                           "serial_number": "SAL18422HKT",
                           "hardware": "1.4",
                           "status": "active",
                           "slot/world_wide_name": "SC1",
                           "mac_address": "NA"
                      }
                 },
                 "24": {
                      "Fabric Module": {
                           "online_diag_status": "Pass",
                           "ports": "0",
                           "model": "N9K-C9504-FM",
                           "software": "7.0(3)I5(0.125)",
                           "serial_number": "SAL18401T2L",
                           "hardware": "1.1",
                           "status": "ok",
                           "slot/world_wide_name": "FM4",
                           "mac_address": "NA"
                      }
                 },
                 "22": {
                      "Fabric Module": {
                           "online_diag_status": "Pass",
                           "ports": "0",
                           "model": "N9K-C9504-FM",
                           "software": "7.0(3)I5(0.125)",
                           "serial_number": "SAL18401T5J",
                           "hardware": "1.1",
                           "status": "ok",
                           "slot/world_wide_name": "FM2",
                           "mac_address": "NA"
                      }
                 }
            }
       }
    }

    golden_output_2 = {'execute.return_value': '''
        Mod Ports             Module-Type                      Model           Status
        --- ----- ------------------------------------- --------------------- ---------
        1    16   16x400G Ethernet Module               N9K-X9716D-GX         ok
        2    36   36x40/100G Ethernet Module            N9K-X9736C-FX         ok
        5    36   36x40G Ethernet Module                                      pwr-denied
        6    52   48x10/25G + 4x40/100G Ethernet Module N9K-X97160YC-EX       ok
        7    52   48x10G + 4x40/100G Ethernet Module                          pwr-denied
        22   0    8-slot (100G) Fabric Module           N9K-C9508-FM-E2       ok
        24   0    8-slot (100G) Fabric Module           N9K-C9508-FM-E2       ok
        26   0    8-slot (100G) Fabric Module           N9K-C9508-FM-E2       ok
        27   0    Supervisor Module                     N9K-SUP-A+            active *
        29   0    System Controller                     N9K-SC-A              active
        30   0    System Controller                     N9K-SC-A              standby

        Mod  Sw                       Hw    Slot
        ---  ----------------------- ------ ----
        1    10.1(0.233)              3.1    LC1
        2    10.1(0.233)              1.1    LC2
        6    10.1(0.233)              2.3    LC6
        22   10.1(0.233)              1.1    FM2
        24   10.1(0.233)              1.1    FM4
        26   10.1(0.233)              1.1    FM6
        27   10.1(0.233)              1.1    SUP1
        29   10.1(0.233)              2.0    SC1
        30   10.1(0.233)              2.0    SC2


        Mod  MAC-Address(es)                         Serial-Num
        ---  --------------------------------------  ----------
        1    bc-4a-56-aa-50-b0 to bc-4a-56-aa-51-33  FOC24322RBW
        2    90-77-ee-34-f8-7c to 90-77-ee-34-f9-0f  FOC24294DJ8
        6    24-16-9d-d0-c9-38 to 24-16-9d-d0-c9-7b  FOC24021CNU
        22   NA                                      FOC24381TPG
        24   NA                                      FOC24381TX1
        26   NA                                      FOC24381TUV
        27   54-88-de-ae-5a-80 to 54-88-de-ae-5a-91  FOC24362EGB
        29   NA                                      FOC24362EU0
        30   NA                                      FOC2435407P

        Mod  Online Diag Status
        ---  ------------------
        1    Pass
        2    Pass
        6    Pass
        22   Pass
        24   Pass
        26   Pass
        27   Pass
        29   Pass
        30   Pass
        '''
    }

    golden_parsed_output_2 = {
        'slot': {
            'lc': {
                '1': {
                    '16x400G Ethernet Module': {
                        'hardware': '3.1',
                        'mac_address': 'bc-4a-56-aa-50-b0 '
                        'to '
                        'bc-4a-56-aa-51-33',
                        'model': 'N9K-X9716D-GX',
                        'online_diag_status': 'Pass',
                        'ports': '16',
                        'serial_number': 'FOC24322RBW',
                        'slot/world_wide_name': 'LC1',
                        'software': '10.1(0.233)',
                        'status': 'ok'
                    }
                },
                '2': {
                    '36x40/100G Ethernet Module': {
                        'hardware': '1.1',
                        'mac_address': '90-77-ee-34-f8-7c '
                        'to '
                        '90-77-ee-34-f9-0f',
                        'model': 'N9K-X9736C-FX',
                        'online_diag_status': 'Pass',
                        'ports': '36',
                        'serial_number': 'FOC24294DJ8',
                        'slot/world_wide_name': 'LC2',
                        'software': '10.1(0.233)',
                        'status': 'ok'
                    }
                },
                '22': {
                    '8-slot (100G) Fabric Module': {
                        'hardware': '1.1',
                        'mac_address': 'NA',
                        'model': 'N9K-C9508-FM-E2',
                        'online_diag_status': 'Pass',
                        'ports': '0',
                        'serial_number': 'FOC24381TPG',
                        'slot/world_wide_name': 'FM2',
                        'software': '10.1(0.233)',
                        'status': 'ok'
                    }
                },
                '24': {
                    '8-slot (100G) Fabric Module': {
                        'hardware': '1.1',
                        'mac_address': 'NA',
                        'model': 'N9K-C9508-FM-E2',
                        'online_diag_status': 'Pass',
                        'ports': '0',
                        'serial_number': 'FOC24381TX1',
                        'slot/world_wide_name': 'FM4',
                        'software': '10.1(0.233)',
                        'status': 'ok'
                    }
                },
                '26': {
                    '8-slot (100G) Fabric Module': {
                        'hardware': '1.1',
                        'mac_address': 'NA',
                        'model': 'N9K-C9508-FM-E2',
                        'online_diag_status': 'Pass',
                        'ports': '0',
                        'serial_number': 'FOC24381TUV',
                        'slot/world_wide_name': 'FM6',
                        'software': '10.1(0.233)',
                        'status': 'ok'
                    }
                },
                '29': {
                    'System Controller': {
                        'hardware': '2.0',
                        'mac_address': 'NA',
                        'model': 'N9K-SC-A',
                        'online_diag_status': 'Pass',
                        'ports': '0',
                        'serial_number': 'FOC24362EU0',
                        'slot/world_wide_name': 'SC1',
                        'software': '10.1(0.233)',
                        'status': 'active'
                    }
                },
                '30': {
                    'System Controller': {
                        'hardware': '2.0',
                        'mac_address': 'NA',
                        'model': 'N9K-SC-A',
                        'online_diag_status': 'Pass',
                        'ports': '0',
                        'serial_number': 'FOC2435407P',
                        'slot/world_wide_name': 'SC2',
                        'software': '10.1(0.233)',
                        'status': 'standby'
                    }
                },
                '5': {
                    '36x40G Ethernet': {
                        'model': 'Module',
                        'ports': '36',
                        'status': 'pwr-denied'
                    }
                },
                '6': {
                    '48x10/25G + 4x40/100G Ethernet Module': {
                        'hardware': '2.3',
                        'mac_address': '24-16-9d-d0-c9-38 '
                        'to '
                        '24-16-9d-d0-c9-7b',
                        'model': 'N9K-X97160YC-EX',
                        'online_diag_status': 'Pass',
                        'ports': '52',
                        'serial_number': 'FOC24021CNU',
                        'slot/world_wide_name': 'LC6',
                        'software': '10.1(0.233)',
                        'status': 'ok'
                    }
                },
                '7': {
                    '48x10G + 4x40/100G Ethernet': {
                        'model': 'Module',
                        'ports': '52',
                        'status': 'pwr-denied'
                    }
                }
            },
            'rp': {
                '27': {
                    'Supervisor Module': {
                        'hardware': '1.1',
                        'mac_address': '54-88-de-ae-5a-80 '
                        'to '
                        '54-88-de-ae-5a-91',
                        'model': 'N9K-SUP-A+',
                        'online_diag_status': 'Pass',
                        'ports': '0',
                        'serial_number': 'FOC24362EGB',
                        'slot/world_wide_name': 'SUP1',
                        'software': '10.1(0.233)',
                        'status': 'active'
                    }
                }
            }
        }
    }

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        module_obj = ShowModule(device=self.device)
        parsed_output = module_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_1(self):
        self.maxDiff = None
        self.device = Mock(**self.output)
        module_obj = ShowModule(device=self.device)
        parsed_output = module_obj.parse()
        self.assertEqual(parsed_output,self.parsed_output_1)

    def test_golden_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        module_obj = ShowModule(device=self.device)
        parsed_output = module_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        module_obj = ShowModule(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = module_obj.parse()

class test_dir(unittest.TestCase):
    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {'files':
                                {'.patch/':
                                    {'size': '4096', 'date': 'Apr 20 2017', 'time': '10:23:05'},
                                 '20170202_074746_poap_7537_init.log':
                                    {'size': '1398', 'date': 'Feb 02 2017', 'time': '00:48:18'},
                                 'ethpm_act_logs.log':
                                    {'size': '251599', 'date': 'Mar 15 2017', 'time': '10:35:50'},
                                 'ethpm_im_tech.log':
                                    {'size': '1171318', 'date': 'Mar 15 2017', 'time': '10:35:55'},
                                 'ethpm_mts_details.log':
                                    {'size': '3837', 'date': 'Mar 15 2017', 'time': '10:35:50'},
                                 'ethpm_syslogs.log':
                                    {'size': '81257', 'date': 'Mar 15 2017', 'time': '10:35:50'},
                                 'ethpm_tech.log':
                                    {'size': '3930383', 'date': 'Mar 15 2017', 'time': '10:35:55'},
                                 'fault-management-logs/':
                                    {'size': '24576', 'date': 'Apr 21 2017', 'time': '04:18:28'},
                                 'lost+found/':
                                    {'size': '4096', 'date': 'Nov 23 2016', 'time': '08:25:40'},
                                 'n7000-s2-debug-sh.10.81.0.125.gbin':
                                    {'size': '4073830', 'date': 'Apr 20 2017', 'time': '10:19:08'},
                                 'virtual-instance-stby-sync/':
                                    {'size': '4096', 'date': 'Apr 20 2017', 'time': '10:28:55'}
                                },
                            'dir': 'bootflash:',
                            'disk_used_space': '108449792',
                            'disk_free_space': '1674481664',
                            'disk_total_space': '1782931456'
                          }

    golden_output = {'execute.return_value': '''

       4096    Apr 20 10:23:05 2017  .patch/
       1398    Feb 02 00:48:18 2017  20170202_074746_poap_7537_init.log
     251599    Mar 15 10:35:50 2017  ethpm_act_logs.log
    1171318    Mar 15 10:35:55 2017  ethpm_im_tech.log
       3837    Mar 15 10:35:50 2017  ethpm_mts_details.log
      81257    Mar 15 10:35:50 2017  ethpm_syslogs.log
    3930383    Mar 15 10:35:55 2017  ethpm_tech.log
      24576    Apr 21 04:18:28 2017  fault-management-logs/
       4096    Nov 23 08:25:40 2016  lost+found/
    4073830    Apr 20 10:19:08 2017  n7000-s2-debug-sh.10.81.0.125.gbin
       4096    Apr 20 10:28:55 2017  virtual-instance-stby-sync/

Usage for bootflash://
  108449792 bytes used
 1674481664 bytes free
 1782931456 bytes total

'''}

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        dir_obj = Dir(device=self.device)
        parsed_output = dir_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_with_arg(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        dir_obj = Dir(device=self.device)
        parsed_output = dir_obj.parse(directory='bootflash:/')
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        dir_obj = Dir(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = dir_obj.parse()

class test_show_vdc_detail(unittest.TestCase):
    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {'vdc':
                            {'1':
                              {'name': 'PE1',
                               'state': 'active',
                               'mac_address': '84:78:ac:ff:e0:1c',
                               'ha_policy': 'RELOAD',
                               'dual_sup_ha_policy': 'SWITCHOVER',
                               'boot_order': '1',
                               'cpu_share': '5',
                               'cpu_share_percentage': '33%',
                               'create_time': 'Fri Apr 28 03:36:26 2017',
                               'reload_count': '0',
                               'uptime': '0 day(s), 10 hour(s), 35 minute(s), 47 second(s)',
                               'restart_count': '1',
                               'restart_time': 'Fri Apr 28 03:36:26 2017',
                               'type': 'Ethernet',
                               'supported_linecards': 'f3'},
                            '2':
                              {'name': 'PE2',
                               'state': 'active',
                               'mac_address': '84:78:ac:ff:e0:1d',
                               'ha_policy': 'RESTART',
                               'dual_sup_ha_policy': 'SWITCHOVER',
                               'boot_order': '1',
                               'cpu_share': '5',
                               'cpu_share_percentage': '33%',
                               'create_time': 'Fri Apr 28 03:48:01 2017',
                               'reload_count': '0',
                               'uptime': '0 day(s), 10 hour(s), 25 minute(s), 2 second(s)',
                               'restart_count': '1',
                               'restart_time': 'Fri Apr 28 03:48:01 2017',
                               'type': 'Ethernet',
                               'supported_linecards': 'f3'},
                            '3':
                              {'name': 'CORE',
                               'state': 'active',
                               'mac_address': '84:78:ac:ff:e0:1e',
                               'ha_policy': 'RESTART',
                               'dual_sup_ha_policy': 'SWITCHOVER',
                               'boot_order': '1',
                               'cpu_share': '5',
                               'cpu_share_percentage': '33%',
                               'create_time': 'Fri Apr 28 03:49:33 2017',
                               'reload_count': '0',
                               'uptime': '0 day(s), 10 hour(s), 23 minute(s), 39 second(s)',
                               'restart_count': '1',
                               'restart_time': 'Fri Apr 28 03:49:33 2017',
                               'type': 'Ethernet',
                               'supported_linecards': 'f3'}
                            }
                        }

    golden_output = {'execute.return_value': '''

    Switchwide mode is m1 f1 m1xl f2 m2xl f2e f3 m3

    vdc id: 1
    vdc name: PE1
    vdc state: active
    vdc mac address: 84:78:ac:ff:e0:1c
    vdc ha policy: RELOAD
    vdc dual-sup ha policy: SWITCHOVER
    vdc boot Order: 1
    CPU Share: 5
    CPU Share Percentage: 33%
    vdc create time: Fri Apr 28 03:36:26 2017
    vdc reload count: 0
    vdc uptime: 0 day(s), 10 hour(s), 35 minute(s), 47 second(s)
    vdc restart count: 1
    vdc restart time: Fri Apr 28 03:36:26 2017
    vdc type: Ethernet
    vdc supported linecards: f3

    vdc id: 2
    vdc name: PE2
    vdc state: active
    vdc mac address: 84:78:ac:ff:e0:1d
    vdc ha policy: RESTART
    vdc dual-sup ha policy: SWITCHOVER
    vdc boot Order: 1
    CPU Share: 5
    CPU Share Percentage: 33%
    vdc create time: Fri Apr 28 03:48:01 2017
    vdc reload count: 0
    vdc uptime: 0 day(s), 10 hour(s), 25 minute(s), 2 second(s)
    vdc restart count: 1
    vdc restart time: Fri Apr 28 03:48:01 2017
    vdc type: Ethernet
    vdc supported linecards: f3

    vdc id: 3
    vdc name: CORE
    vdc state: active
    vdc mac address: 84:78:ac:ff:e0:1e
    vdc ha policy: RESTART
    vdc dual-sup ha policy: SWITCHOVER
    vdc boot Order: 1
    CPU Share: 5
    CPU Share Percentage: 33%
    vdc create time: Fri Apr 28 03:49:33 2017
    vdc reload count: 0
    vdc uptime: 0 day(s), 10 hour(s), 23 minute(s), 39 second(s)
    vdc restart count: 1
    vdc restart time: Fri Apr 28 03:49:33 2017
    vdc type: Ethernet
    vdc supported linecards: f3

'''}

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        vdc_detail_obj = ShowVdcDetail(device=self.device)
        parsed_output = vdc_detail_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        vdc_detail_obj = ShowVdcDetail(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = vdc_detail_obj.parse()

class test_show_vdc_current(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'current_vdc':
            {'id': '1',
            'name': 'PE1',
            },
        }

    golden_output = {'execute.return_value': '''
        Current vdc is 1 - PE1
        '''}

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        vdc_current_obj = ShowVdcCurrent(device=self.device)
        parsed_output = vdc_current_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        vdc_current_obj = ShowVdcCurrent(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = vdc_current_obj.parse()

class test_show_vdc_membership_status(unittest.TestCase):
    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {'virtual_device':
                                {'0':
                                    {'membership':
                                        {'Unallocated':
                                            {'Eth3/1':
                                              {'vd_ms_status': 'OK',
                                               'vd_ms_type': 'Ethernet'},
                                             'Eth3/2':
                                              {'vd_ms_status': 'OK',
                                               'vd_ms_type': 'Ethernet'}
                                            }
                                        }
                                    },
                                '1':
                                    {'membership':
                                        {'PE1':
                                            {'Eth4/5':
                                              {'vd_ms_status': 'OK',
                                               'vd_ms_type': 'Ethernet'},
                                             'Eth4/6':
                                              {'vd_ms_status': 'OK',
                                               'vd_ms_type': 'Ethernet'}
                                            }
                                        }
                                    },
                                '2':
                                    {'membership':
                                        {'PE2':
                                            {'Eth4/3':
                                              {'vd_ms_status': 'OK',
                                               'vd_ms_type': 'Ethernet'},
                                             'Eth4/4':
                                              {'vd_ms_status': 'OK',
                                               'vd_ms_type': 'Ethernet'}
                                            }
                                        }
                                    },
                                '3':
                                    {'membership':
                                        {'CORE':
                                            {'Eth4/1':
                                              {'vd_ms_status': 'OK',
                                               'vd_ms_type': 'Ethernet'},
                                             'Eth4/2(b)':
                                              {'vd_ms_status': 'OK',
                                               'vd_ms_type': 'Ethernet'}
                                            }
                                        }
                                    }
                                }
                            }

    golden_output = {'execute.return_value': '''

    Flags : b - breakout port
    ---------------------------------

    vdc_id: 0 vdc_name: Unallocated interfaces:
    Port        Status
    ----        ----------
    Eth3/1      OK
    Eth3/2      OK

    vdc_id: 1 vdc_name: PE1 interfaces:
    Port        Status
    ----        ----------
    Eth4/5      OK
    Eth4/6      OK

    vdc_id: 2 vdc_name: PE2 interfaces:
    Port        Status
    ----        ----------
    Eth4/3      OK
    Eth4/4      OK

    vdc_id: 3 vdc_name: CORE interfaces:
    Port        Status
    ----        ----------
    Eth4/1      OK
    Eth4/2(b)   OK

'''}

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        vdc_membership_status_obj = ShowVdcMembershipStatus(device=self.device)
        parsed_output = vdc_membership_status_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        vdc_membership_status_obj = ShowVdcMembershipStatus(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = vdc_membership_status_obj.parse()


class TestShowProcessesCpu(unittest.TestCase):

    dev = Device(name='N9Kv')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'five_min_cpu': 21,
        'five_sec_cpu_interrupts': 5,
        'five_sec_cpu_total': 19,
        'idle_percent': 78.35,
        'index': {
            1: {
                'invoked': 162103,
                'one_sec': 0.0,
                'pid': 1,
                'process': 'init',
                'runtime_ms': 24380,
                'usecs': 0
            },
            2: {
                'invoked': 28,
                'one_sec': 0.0,
                'pid': 417,
                'process': 'bootflash_sync.',
                'runtime_ms': 0,
                'usecs': 0
            },
            3: {
                'invoked': 10,
                'one_sec': 0.0,
                'pid': 447,
                'process': 'inotifywait',
                'runtime_ms': 0,
                'usecs': 0
            }
        },
        'kernel_percent': 20.34,
        'one_min_cpu': 19,
        'user_percent': 1.29
    }

    golden_output = {
        'execute.return_value':
        '''\

    PID    Runtime(ms)  Invoked   uSecs  1Sec    Process
    -----  -----------  --------  -----  ------  -----------
        1        24380    162103      0   0.00%  init
      417            0        28      0   0.00%  bootflash_sync.
      447            0        10      0   0.00%  inotifywait

    CPU util  :    1.29% user,   20.34% kernel,   78.35% idle

    CPU utilization for five seconds: 19%/5%; one minute: 19%; five minutes: 21%
     Please note that only processes from the requested vdc are shown above
    '''
    }

    def test_empty(self):
        self.dev = Mock(**self.empty_output)
        obj = ShowProcessesCpu(device=self.dev)
        with self.assertRaises(SchemaEmptyParserError):
            parsered_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output)
        obj = ShowProcessesCpu(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


class TestShowProcessesMemory(unittest.TestCase):

    dev = Device(name='N9Kv')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'all_mem_alloc': 4646350848,
        'pid': {
            1: {
                'index': {
                    1: {
                        'mem_alloc': 188416,
                        'mem_limit': 0,
                        'mem_used': 4308992,
                        'pid': 1,
                        'process': 'init',
                        'stack_base_ptr': 'ffffffff/ffffffff'
                    }
                }
            },
            417: {
                'index': {
                    1: {
                        'mem_alloc': 200704,
                        'mem_limit': 0,
                        'mem_used': 3588096,
                        'pid': 417,
                        'process': 'bootflash_sync.',
                        'stack_base_ptr': 'ffe65dd0/ffe64518'
                    }
                }
            },
            447: {
                'index': {
                    1: {
                        'mem_alloc': 393216,
                        'mem_limit': 0,
                        'mem_used': 6639616,
                        'pid': 447,
                        'process': 'inotifywait',
                        'stack_base_ptr': 'ffffffff/ffffffff'
                    }
                }
            }
        }
    }

    # show processes memory
    golden_output = {
        'execute.return_value':
        '''\

    PID    MemAlloc  MemLimit    MemUsed     StackBase/Ptr      Process
    -----  --------  ----------  ----------  -----------------  ----------------
        1    188416  0           4308992     ffffffff/ffffffff  init
      417    200704  0           3588096     ffe65dd0/ffe64518  bootflash_sync.
      447    393216  0           6639616     ffffffff/ffffffff  inotifywait

    All processes: MemAlloc = 4646350848
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


class TestShowCores(unittest.TestCase):

    dev = Device(name='N9Kv')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        "date": {
            "2020-08-17 18:00:56": {
                "pid": {
                    8083: {
                        "instance": 1,
                        "module": 27,
                        "process_name": "bgp",
                        "vdc": 1
                    }
                }
            },
            "2020-08-17 18:04:03": {
                "pid": {
                    8083: {
                        "instance": 2,
                        "module": 27,
                        "process_name": "bgp",
                        "vdc": 1
                    }
                }
            }
        }
    }

    # show cores
    golden_output = {
        'execute.return_value':
        '''\
        VDC  Module  Instance  Process-name     PID       Date(Year-Month-Day Time)
        ---  ------  --------  ---------------  --------  -------------------------
        1    27      1         bgp              8083      2020-08-17 18:00:56
        1    27      2         bgp              8083      2020-08-17 18:04:03
        '''
    }

    def test_empty(self):
        self.dev = Mock(**self.empty_output)
        obj = ShowCores(device=self.dev)
        with self.assertRaises(SchemaEmptyParserError):
            parsered_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output)
        obj = ShowCores(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

if __name__ == '__main__':
    unittest.main()
