#!/bin/env python
import re
import unittest
from unittest.mock import Mock

from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError

from genie.libs.parser.nxos.show_platform import  ShowBoot,\
                                         ShowInventory,\
                                         ShowInstallActive,\
                                         ShowSystemRedundancyStatus,\
                                         ShowRedundancyStatus,\
                                         ShowVersion,\
                                         ShowModule,\
                                         Dir, \
                                         ShowVdcDetail, \
                                         ShowVdcCurrent, \
                                         ShowVdcMembershipStatus
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
                                 'cpu': None,
                                 'chassis': 'Supervisor Module-2',
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
                                 'chassis': 'None',
                                 'slots': 'None',
                                 'cpu': 'E5-2699 v3 @ 2.30GHz',
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

    golden_output3 = {'execute.return_value' : '''
      Cisco Nexus Operating System (NX-OS) Software
      TAC support: http://www.cisco.com/tac
      Documents: http://www.cisco.com/en/US/products/ps9372/tsd_products_support_series_home.html
      Copyright (c) 2002-2013, Cisco Systems, Inc. All rights reserved.
      The copyrights to certain works contained in this software are
      owned by other third parties and used and distributed under
      license. Certain components of this software are licensed under
      the GNU General Public License (GPL) version 2.0 or the GNU
      Lesser General Public License (LGPL) Version 2.1. A copy of each
      such license is available at
      http://www.opensource.org/licenses/gpl-2.0.php and
      http://www.opensource.org/licenses/lgpl-2.1.php

      Software
        BIOS:      version 3.22.0
        kickstart: version 5.2(9)
        system:    version 5.2(9)
        BIOS compile time:       02/20/10
        kickstart image file is: bootflash:///n7000-s1-kickstart.5.2.9.bin
        kickstart compile time:  12/25/2020 12:00:00 [04/04/2013 09:33:19]
        system image file is:    bootflash:///n7000-s1-dk9.5.2.9.bin
        system compile time:     2/22/2013 9:00:00 [04/04/2013 10:41:37]


      Hardware
        cisco Nexus7000 C7010 (10 Slot) Chassis ("Supervisor module-1X")
        Intel(R) Xeon(R) CPU         with 4115656 kB of memory.
        Processor Board ID JAF1111AKJP 

        Device name: Nexus7000
        bootflash:    2029608 kB
        slot0:        2075246 kB (expansion flash)

      Kernel uptime is 404 day(s), 22 hour(s), 35 minute(s), 19 second(s)

      Last reset at 991934 usecs after  Tue Mar  6 13:32:43 2018

        Reason: Reset triggered due to Switchover Request by User
        System version: 5.2(5)
        Service: SAP(93): Swover due to install

      plugin
        Core Plugin, Ethernet Plugin


      CMP (Module 5) ok
       CMP Software
        CMP BIOS version:        02.01.05
        CMP Image version:       5.0(2) [build 5.0(0.66)]
        CMP BIOS compile time:   7/13/2008 19:44:27
        CMP Image compile time:  5/25/2010 13:00:00

      CMP (Module 6) ok
       CMP Software
        CMP BIOS version:        02.01.05
        CMP Image version:       5.2(4) [build 5.0(0.66)]
        CMP BIOS compile time:   7/13/2008 19:44:27
        CMP Image compile time:  1/28/2012 23:00:00

    '''}
    golden_parsed_output3 = {
      'platform': {
          'name': 'Nexus',
          'os': 'NX-OS',
          'software': {
              'bios_version': '3.22.0',
              'kickstart_version': '5.2(9)',
              'system_version': '5.2(9)',
              'bios_compile_time': '02/20/10',
              'kickstart_image_file': 'bootflash:///n7000-s1-kickstart.5.2.9.bin',
              'kickstart_compile_time': '12/25/2020 12:00:00 [04/04/2013 09:33:19]',
              'system_image_file': 'bootflash:///n7000-s1-dk9.5.2.9.bin',
              'system_compile_time': '2/22/2013 9:00:00 [04/04/2013 10:41:37]',
              },
          'hardware': {
              'model': 'Nexus7000 C7010',
              'slots': '10',
              'chassis': 'Supervisor module-1X',
              'cpu': None,
              'memory': '4115656 kB',
              'processor_board_id': 'JAF1111AKJP',
              'device_name': 'Nexus7000',
              'bootflash': '2029608 kB',
              'slot0': '2075246 kB',
              },
          'kernel_uptime': {
              'days': 404,
              'hours': 22,
              'minutes': 35,
              'seconds': 19,
              },
          'reason': 'Reset triggered due to Switchover Request by User',
          'system_version': '5.2(5)',
          },
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

    golden_output_2 = {'execute.return_value': '''
    NAME: "Chassis",  DESCR: "Nexus7000 C7010 (10 Slot) Chassis "    
    PID: N7K-C7010           ,  VID: V01 ,  SN: TBM11111111          

    NAME: "Slot 1",  DESCR: "10 Gbps Ethernet Module"               
    PID: N7K-M132XP-12       ,  VID: V06 ,  SN: JAF1111ATMS          

    NAME: "Slot 2",  DESCR: "10 Gbps Ethernet Module"               
    PID: N7K-M132XP-12       ,  VID: V06 ,  SN: JAF1111BGRG          

    NAME: "Slot 3",  DESCR: "1/10 Gbps Ethernet Module"             
    PID: N7K-F132XP-15       ,  VID: V02 ,  SN: JAF1111BCSA          

    NAME: "Slot 4",  DESCR: "1/10 Gbps Ethernet Module"             
    PID: N7K-F132XP-15       ,  VID: V02 ,  SN: JAF1111BDTA          

    NAME: "Slot 5",  DESCR: "Supervisor module-1X"                  
    PID: N7K-SUP1            ,  VID: V14 ,  SN: JAF1111AKJP          

    NAME: "Slot 6",  DESCR: "Supervisor module-1X"                  
    PID: N7K-SUP1            ,  VID: V09 ,  SN: JAF1111EESP          

    NAME: "Slot 7",  DESCR: "1/10 Gbps Ethernet Module"             
    PID: N7K-F132XP-15       ,  VID: V04 ,  SN: JAF1111BJPH          

    NAME: "Slot 8",  DESCR: "10/100/1000 Mbps Ethernet Module"      
    PID: N7K-M148GT-11       ,  VID: V07 ,  SN: JAF1111ALEQ          

    NAME: "Slot 9",  DESCR: "10/100/1000 Mbps Ethernet Module"      
    PID: N7K-M148GT-11       ,  VID: V07 ,  SN: JAF1111ALFN          

    NAME: "Slot 10",  DESCR: "10/100/1000 Mbps Ethernet Module"      
    PID: N7K-M148GT-11       ,  VID: V07 ,  SN: JAF1111ALEP          

    NAME: "Slot 11",  DESCR: "Fabric card module"                    
    PID: N7K-C7010-FAB-1     ,  VID: V02 ,  SN: JAF1111BFKT          

    NAME: "Slot 12",  DESCR: "Fabric card module"                    
    PID: N7K-C7010-FAB-1     ,  VID: V02 ,  SN: JAF1111ALPC          

    NAME: "Slot 13",  DESCR: "Fabric card module"                    
    PID: N7K-C7010-FAB-1     ,  VID: V02 ,  SN: JAF1111BFLA          

    NAME: "Slot 14",  DESCR: "Fabric card module"                    
    PID: N7K-C7010-FAB-1     ,  VID: V02 ,  SN: JAF1111BFNA          

    NAME: "Slot 15",  DESCR: "Fabric card module"                    
    PID: N7K-C7010-FAB-1     ,  VID: V02 ,  SN: JAF1111BFNF          

    NAME: "Slot 33",  DESCR: "Nexus7000 C7010 (10 Slot) Chassis Power Supply"
    PID: N7K-AC-6.0KW        ,  VID: V01 ,  SN: DTM11111111          

    NAME: "Slot 34",  DESCR: "Nexus7000 C7010 (10 Slot) Chassis Power Supply"
    PID: N7K-AC-6.0KW        ,  VID: V01 ,  SN: DTM11111111          

    NAME: "Slot 35",  DESCR: "Nexus7000 C7010 (10 Slot) Chassis Power Supply"
    PID: N7K-AC-6.0KW        ,  VID: V01 ,  SN: DTM111111Z1          

    NAME: "Slot 36",  DESCR: "Nexus7000 C7010 (10 Slot) Chassis Fan Module"
    PID: N7K-C7010-FAN-S     ,  VID: V01 ,  SN: FOX1111XAA1          

    NAME: "Slot 37",  DESCR: "Nexus7000 C7010 (10 Slot) Chassis Fan Module"
    PID: N7K-C7010-FAN-S     ,  VID: V01 ,  SN: FOX1111XAC1          

    NAME: "Slot 38",  DESCR: "Nexus7000 C7010 (10 Slot) Chassis Fan Module"
    PID: N7K-C7010-FAN-F     ,  VID: V02 ,  SN: FOX1111XA11          

    NAME: "Slot 39",  DESCR: "Nexus7000 C7010 (10 Slot) Chassis Fan Module"
    PID: N7K-C7010-FAN-F     ,  VID: V02 ,  SN: FOX1111XA1F          
    '''}
    
    golden_parsed_output_2 = {
      'name': {
          'Chassis': {
              'description': 'Nexus7000 C7010 (10 Slot) Chassis ',
              'slot': 'None',
              'pid': 'N7K-C7010',
              'vid': 'V01',
              'serial_number': 'TBM11111111',
              },
          'Slot 1': {
              'description': '10 Gbps Ethernet Module',
              'slot': '1',
              'pid': 'N7K-M132XP-12',
              'vid': 'V06',
              'serial_number': 'JAF1111ATMS',
              },
          'Slot 2': {
              'description': '10 Gbps Ethernet Module',
              'slot': '2',
              'pid': 'N7K-M132XP-12',
              'vid': 'V06',
              'serial_number': 'JAF1111BGRG',
              },
          'Slot 3': {
              'description': '1/10 Gbps Ethernet Module',
              'slot': '3',
              'pid': 'N7K-F132XP-15',
              'vid': 'V02',
              'serial_number': 'JAF1111BCSA',
              },
          'Slot 4': {
              'description': '1/10 Gbps Ethernet Module',
              'slot': '4',
              'pid': 'N7K-F132XP-15',
              'vid': 'V02',
              'serial_number': 'JAF1111BDTA',
              },
          'Slot 5': {
              'description': 'Supervisor module-1X',
              'slot': '5',
              'pid': 'N7K-SUP1',
              'vid': 'V14',
              'serial_number': 'JAF1111AKJP',
              },
          'Slot 6': {
              'description': 'Supervisor module-1X',
              'slot': '6',
              'pid': 'N7K-SUP1',
              'vid': 'V09',
              'serial_number': 'JAF1111EESP',
              },
          'Slot 7': {
              'description': '1/10 Gbps Ethernet Module',
              'slot': '7',
              'pid': 'N7K-F132XP-15',
              'vid': 'V04',
              'serial_number': 'JAF1111BJPH',
              },
          'Slot 8': {
              'description': '10/100/1000 Mbps Ethernet Module',
              'slot': '8',
              'pid': 'N7K-M148GT-11',
              'vid': 'V07',
              'serial_number': 'JAF1111ALEQ',
              },
          'Slot 9': {
              'description': '10/100/1000 Mbps Ethernet Module',
              'slot': '9',
              'pid': 'N7K-M148GT-11',
              'vid': 'V07',
              'serial_number': 'JAF1111ALFN',
              },
          'Slot 10': {
              'description': '10/100/1000 Mbps Ethernet Module',
              'slot': '10',
              'pid': 'N7K-M148GT-11',
              'vid': 'V07',
              'serial_number': 'JAF1111ALEP',
              },
          'Slot 11': {
              'description': 'Fabric card module',
              'slot': '11',
              'pid': 'N7K-C7010-FAB-1',
              'vid': 'V02',
              'serial_number': 'JAF1111BFKT',
              },
          'Slot 12': {
              'description': 'Fabric card module',
              'slot': '12',
              'pid': 'N7K-C7010-FAB-1',
              'vid': 'V02',
              'serial_number': 'JAF1111ALPC',
              },
          'Slot 13': {
              'description': 'Fabric card module',
              'slot': '13',
              'pid': 'N7K-C7010-FAB-1',
              'vid': 'V02',
              'serial_number': 'JAF1111BFLA',
              },
          'Slot 14': {
              'description': 'Fabric card module',
              'slot': '14',
              'pid': 'N7K-C7010-FAB-1',
              'vid': 'V02',
              'serial_number': 'JAF1111BFNA',
              },
          'Slot 15': {
              'description': 'Fabric card module',
              'slot': '15',
              'pid': 'N7K-C7010-FAB-1',
              'vid': 'V02',
              'serial_number': 'JAF1111BFNF',
              },
          'Slot 33': {
              'description': 'Nexus7000 C7010 (10 Slot) Chassis Power Supply',
              'slot': '33',
              'pid': 'N7K-AC-6.0KW',
              'vid': 'V01',
              'serial_number': 'DTM11111111',
              },
          'Slot 34': {
              'description': 'Nexus7000 C7010 (10 Slot) Chassis Power Supply',
              'slot': '34',
              'pid': 'N7K-AC-6.0KW',
              'vid': 'V01',
              'serial_number': 'DTM11111111',
              },
          'Slot 35': {
              'description': 'Nexus7000 C7010 (10 Slot) Chassis Power Supply',
              'slot': '35',
              'pid': 'N7K-AC-6.0KW',
              'vid': 'V01',
              'serial_number': 'DTM111111Z1',
              },
          'Slot 36': {
              'description': 'Nexus7000 C7010 (10 Slot) Chassis Fan Module',
              'slot': '36',
              'pid': 'N7K-C7010-FAN-S',
              'vid': 'V01',
              'serial_number': 'FOX1111XAA1',
              },
          'Slot 37': {
              'description': 'Nexus7000 C7010 (10 Slot) Chassis Fan Module',
              'slot': '37',
              'pid': 'N7K-C7010-FAN-S',
              'vid': 'V01',
              'serial_number': 'FOX1111XAC1',
              },
          'Slot 38': {
              'description': 'Nexus7000 C7010 (10 Slot) Chassis Fan Module',
              'slot': '38',
              'pid': 'N7K-C7010-FAN-F',
              'vid': 'V02',
              'serial_number': 'FOX1111XA21',
              },
          'Slot 39': {
              'description': 'Nexus7000 C7010 (10 Slot) Chassis Fan Module',
              'slot': '39',
              'pid': 'N7K-C7010-FAN-F',
              'vid': 'V02',
              'serial_number': 'FOX1111XA1F',
              },
          },
      }

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        inventory_obj = ShowInventory(device=self.device)
        parsed_output = inventory_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        inventory_obj = ShowInventory(device=self.device)
        parsed_output = inventory_obj.parse()
        from genie.libs.parser.utils.common import format_output

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

    golden_output2 = {'execute.return_value' : '''
      Redundancy mode
      ---------------
            administrative:   HA
               operational:   HA

      This supervisor (sup-5)
      -----------------------
          Redundancy state:   Active
          Supervisor state:   Active
            Internal state:   Active with HA standby

      Other supervisor (sup-6)
      ------------------------
          Redundancy state:   Standby

          Supervisor state:   HA standby
            Internal state:   HA standby

      System start time:          Thu Mar  9 21:05:36 2017

      System uptime:              766 days, 15 hours, 53 minutes, 6 seconds
      Kernel uptime:              404 days, 22 hours, 35 minutes, 19 seconds
      Active supervisor uptime:   404 days, 20 hours, 40 minutes, 0 seconds
    '''}

    golden_parsed_output2 = {
      'redundancy_mode': {
          'administrative': 'HA',
          'operational': 'HA',
          },
      'supervisor_5': {
          'redundancy_state': 'Active',
          'supervisor_state': 'Active',
          'internal_state': 'Active with HA standby',
          },
      'supervisor_6': {
          'redundancy_state': 'Standby',
          'supervisor_state': 'HA standby',
          'internal_state': 'HA standby',
          },
      'system_start_time': 'Thu Mar  9 21:05:36 2017',
      'system_uptime': '766 days, 15 hours, 53 minutes, 6 seconds',
      'kernel_uptime': '404 days, 22 hours, 35 minutes, 19 seconds',
      'active_supervisor_time': '404 days, 20 hours, 40 minutes, 0 seconds',
      }

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        redundancy_obj = ShowRedundancyStatus(device=self.device)
        parsed_output = redundancy_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        redundancy_obj = ShowRedundancyStatus(device=self.device)
        parsed_output = redundancy_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output2)

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

    golden_output2 = {'execute.return_value': '''
      Current Boot Variables:

      sup-1
      kickstart variable = bootflash:/n7000-s1-kickstart.5.2.9.bin
      system variable = bootflash:/n7000-s1-dk9.5.2.9.bin
      sup-2
      kickstart variable = bootflash:/n7000-s1-kickstart.5.2.9.bin
      system variable = bootflash:/n7000-s1-dk9.5.2.9.bin
      No module boot variable set

      Boot Variables on next reload:

      sup-1
      kickstart variable = bootflash:/n7000-s1-kickstart.5.2.9.bin
      system variable = bootflash:/n7000-s1-dk9.5.2.9.bin
      sup-2
      kickstart variable = bootflash:/n7000-s1-kickstart.5.2.9.bin
      system variable = bootflash:/
    '''}

    golden_parsed_output2 = {
      'current_boot_variable': {
          'sup_number': {
              'sup-1': {
                  'kickstart_variable': 'bootflash:/n7000-s1-kickstart.5.2.9.bin',
                  'system_variable': 'bootflash:/n7000-s1-dk9.5.2.9.bin',
                  },
              'sup-2': {
                  'kickstart_variable': 'bootflash:/n7000-s1-kickstart.5.2.9.bin',
                  'system_variable': 'bootflash:/n7000-s1-dk9.5.2.9.bin',
                  },
              },
          },
      'next_reload_boot_variable': {
          'sup_number': {
              'sup-1': {
                  'kickstart_variable': 'bootflash:/n7000-s1-kickstart.5.2.9.bin',
                  'system_variable': 'bootflash:/n7000-s1-dk9.5.2.9.bin',
                  },
              'sup-2': {
                  'kickstart_variable': 'bootflash:/n7000-s1-kickstart.5.2.9.bin',
                  'system_variable': 'bootflash:/',
                  },
              },
          },
      }
    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        boot_obj = ShowBoot(device=self.device)
        parsed_output = boot_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        boot_obj = ShowBoot(device=self.device)
        parsed_output = boot_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output2)

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
                                       'mac_address': '84-78-ac-0f-c4-cd to 84-78-ac-0f-c4-df',
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
                                       'mac_address': '84-78-ac-0f-b9-00 to 84-78-ac-0f-b9-12',
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
                                       'mac_address': '84-78-ac-18-dd-30 to 84-78-ac-18-dd-63',
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
                                       'mac_address': '54-4a-00-ad-19-40 to 54-4a-00-ad-19-7b',
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
                                       'mac_address': 'bc-16-65-54-af-64 to bc-16-65-54-af-87',
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
                                       'mac_address': 'd8-67-d9-0e-91-c8 to d8-67-d9-0e-91-e3',
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
                                       'mac_address': 'bc-16-65-3a-b8-d0 to bc-16-65-3a-b9-03',
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
    1    84-78-ac-0f-c4-cd to 84-78-ac-0f-c4-df  JAF1708AGTH
    2    84-78-ac-0f-b9-00 to 84-78-ac-0f-b9-12  JAF1708AGQH
    3    84-78-ac-18-dd-30 to 84-78-ac-18-dd-63  JAF1717AAND
    4    54-4a-00-ad-19-40 to 54-4a-00-ad-19-7b  JAE18120FLU
    6    bc-16-65-54-af-64 to bc-16-65-54-af-87  JAF1719AHMB
    7    d8-67-d9-0e-91-c8 to d8-67-d9-0e-91-e3  JAF1641APPF
    8    bc-16-65-3a-b8-d0 to bc-16-65-3a-b9-03  JAF1717BEAT

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
        1    88-1d-fc-84-e3-ec to 88-1d-fc-84-e4-2f  SAL18422J9D
        22   NA                                      SAL18401T5J
        24   NA                                      SAL18401T2L
        26   NA                                      SAL18401T5S
        27   e4-c7-22-be-01-0c to e4-c7-22-be-01-1d  SAL18422LG1
        28   e4-c7-22-bd-f1-a6 to e4-c7-22-bd-f1-b7  SAL18412064
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
                           "mac_address": "e4-c7-22-bd-f1-a6 to e4-c7-22-bd-f1-b7"
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
                           "mac_address": "e4-c7-22-be-01-0c to e4-c7-22-be-01-1d"
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
                           "mac_address": "88-1d-fc-84-e3-ec to 88-1d-fc-84-e4-2f"
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
      Mod  Ports  Module-Type                         Model              Status
      ---  -----  ----------------------------------- ------------------ ----------
      1    32     10 Gbps Ethernet Module             N7K-M132XP-12      ok
      2    32     10 Gbps Ethernet Module             N7K-M132XP-12      ok
      3    32     1/10 Gbps Ethernet Module           N7K-F132XP-15      ok
      4    32     1/10 Gbps Ethernet Module           N7K-F132XP-15      ok
      5    0      Supervisor module-1X                N7K-SUP1           active *
      6    0      Supervisor module-1X                N7K-SUP1           ha-standby
      7    32     1/10 Gbps Ethernet Module           N7K-F132XP-15      ok
      8    48     10/100/1000 Mbps Ethernet Module    N7K-M148GT-11      ok
      9    48     10/100/1000 Mbps Ethernet Module    N7K-M148GT-11      ok
      10   48     10/100/1000 Mbps Ethernet Module    N7K-M148GT-11      ok

      Mod  Sw              Hw
      ---  --------------  ------
      1    5.2(9)          1.6     
      2    5.2(9)          1.6     
      3    5.2(9)          1.1     
      4    5.2(9)          1.2     
      5    5.2(9)          2.4     
      6    5.2(9)          1.6     
      7    5.2(9)          1.1     
      8    5.2(9)          1.5     
      9    5.2(9)          1.5     
      10   5.2(9)          1.5     


      Mod  MAC-Address(es)                         Serial-Num
      ---  --------------------------------------  ----------
      1    00-24-f7-1a-7b-a8 to 00-24-f7-1a-7b-cc  JAF1246ATMS
      2    00-25-84-eb-59-04 to 00-25-84-eb-59-28  JAF1242BGRG
      3    40-55-39-e6-73-5c to 40-55-39-e6-73-a0  JAF1515BCSA
      4    30-e4-db-ef-95-f8 to 30-e4-db-ef-96-3c  JAF1527BDTA
      5    00-24-98-6f-82-e0 to 00-24-98-6f-82-e8  JAF1308AKJP
      6    a8-b1-d4-57-36-88 to a8-b1-d4-57-36-90  JAF1423EESP
      7    24-e9-b3-56-ab-fc to 24-e9-b3-56-ac-40  JAF1751BJPH
      8    00-25-84-e7-0a-20 to 00-25-84-e7-0a-54  JAF1323ALEQ
      9    00-25-84-eb-66-c4 to 00-25-84-eb-66-f8  JAF1323ALFN
      10   00-26-0b-3c-89-38 to 00-26-0b-3c-89-6c  JAF1323ALEP

      Mod  Online Diag Status
      ---  ------------------
      1    Fail
      2    Pass
      3    Pass
      4    Pass
      5    Pass
      6    Pass
      7    Pass
      8    Pass
      9    Pass
      10   Pass

      Xbar Ports  Module-Type                         Model              Status
      ---  -----  ----------------------------------- ------------------ ----------
      1    0      Fabric Module 1                     N7K-C7010-FAB-1    ok
      2    0      Fabric Module 1                     N7K-C7010-FAB-1    ok
      3    0      Fabric Module 1                     N7K-C7010-FAB-1    ok
      4    0      Fabric Module 1                     N7K-C7010-FAB-1    ok
      5    0      Fabric Module 1                     N7K-C7010-FAB-1    ok

      Xbar Sw              Hw
      ---  --------------  ------
      1    NA              1.0     
      2    NA              1.0     
      3    NA              1.0     
      4    NA              1.0     
      5    NA              1.0     


      Xbar MAC-Address(es)                         Serial-Num
      ---  --------------------------------------  ----------
      1    NA                                      JAF1321BFKT
      2    NA                                      JAF1320ALPC
      3    NA                                      JAF1321BFLA
      4    NA                                      JAF1321BFNA
      5    NA                                      JAF1321BFNF

    '''}

    golden_parsed_output_2 = {
      'slot': {
          'lc': {
              '1': {
                  '10 Gbps Ethernet Module': {
                      'ports': '32',
                      'model': 'N7K-M132XP-12',
                      'status': 'ok',
                      'software': '5.2(9)',
                      'hardware': '1.6',
                      'mac_address': '00-24-f7-1a-7b-a8 to 00-24-f7-1a-7b-cc',
                      'serial_number': 'JAF1246ATMS',
                      'online_diag_status': 'Fail',
                      },
                  },
              '2': {
                  '10 Gbps Ethernet Module': {
                      'ports': '32',
                      'model': 'N7K-M132XP-12',
                      'status': 'ok',
                      'software': '5.2(9)',
                      'hardware': '1.6',
                      'mac_address': '00-25-84-eb-59-04 to 00-25-84-eb-59-28',
                      'serial_number': 'JAF1242BGRG',
                      'online_diag_status': 'Pass',
                      },
                  },
              '3': {
                  '1/10 Gbps Ethernet Module': {
                      'ports': '32',
                      'model': 'N7K-F132XP-15',
                      'status': 'ok',
                      'software': '5.2(9)',
                      'hardware': '1.1',
                      'mac_address': '40-55-39-e6-73-5c to 40-55-39-e6-73-a0',
                      'serial_number': 'JAF1515BCSA',
                      'online_diag_status': 'Pass',
                      },
                  },
              '4': {
                  '1/10 Gbps Ethernet Module': {
                      'ports': '32',
                      'model': 'N7K-F132XP-15',
                      'status': 'ok',
                      'software': '5.2(9)',
                      'hardware': '1.2',
                      'mac_address': '30-e4-db-ef-95-f8 to 30-e4-db-ef-96-3c',
                      'serial_number': 'JAF1527BDTA',
                      'online_diag_status': 'Pass',
                      },
                  },
              '7': {
                  '1/10 Gbps Ethernet Module': {
                      'ports': '32',
                      'model': 'N7K-F132XP-15',
                      'status': 'ok',
                      'software': '5.2(9)',
                      'hardware': '1.1',
                      'mac_address': '24-e9-b3-56-ab-fc to 24-e9-b3-56-ac-40',
                      'serial_number': 'JAF1751BJPH',
                      'online_diag_status': 'Pass',
                      },
                  },
              '8': {
                  '10/100/1000 Mbps Ethernet Module': {
                      'ports': '48',
                      'model': 'N7K-M148GT-11',
                      'status': 'ok',
                      'software': '5.2(9)',
                      'hardware': '1.5',
                      'mac_address': '00-25-84-e7-0a-20 to 00-25-84-e7-0a-54',
                      'serial_number': 'JAF1323ALEQ',
                      'online_diag_status': 'Pass',
                      },
                  },
              '9': {
                  '10/100/1000 Mbps Ethernet Module': {
                      'ports': '48',
                      'model': 'N7K-M148GT-11',
                      'status': 'ok',
                      'software': '5.2(9)',
                      'hardware': '1.5',
                      'mac_address': '00-25-84-eb-66-c4 to 00-25-84-eb-66-f8',
                      'serial_number': 'JAF1323ALFN',
                      'online_diag_status': 'Pass',
                      },
                  },
              '10': {
                  '10/100/1000 Mbps Ethernet Module': {
                      'ports': '48',
                      'model': 'N7K-M148GT-11',
                      'status': 'ok',
                      'software': '5.2(9)',
                      'hardware': '1.5',
                      'mac_address': '00-26-0b-3c-89-38 to 00-26-0b-3c-89-6c',
                      'serial_number': 'JAF1323ALEP',
                      'online_diag_status': 'Pass',
                      },
                  },
              },
          'rp': {
              '5': {
                  'Supervisor module-1X': {
                      'ports': '0',
                      'model': 'N7K-SUP1',
                      'status': 'active',
                      'software': '5.2(9)',
                      'hardware': '2.4',
                      'mac_address': '00-24-98-6f-82-e0 to 00-24-98-6f-82-e8',
                      'serial_number': 'JAF1308AKJP',
                      'online_diag_status': 'Pass',
                      },
                  },
              '6': {
                  'Supervisor module-1X': {
                      'ports': '0',
                      'model': 'N7K-SUP1',
                      'status': 'ha-standby',
                      'software': '5.2(9)',
                      'hardware': '1.6',
                      'mac_address': 'a8-b1-d4-57-36-88 to a8-b1-d4-57-36-90',
                      'serial_number': 'JAF1423EESP',
                      'online_diag_status': 'Pass',
                      },
                  },
              },
          },
      'xbar': {
          '1': {
              'ports': '0',
              'module_type': 'Fabric Module 1',
              'model': 'N7K-C7010-FAB-1',
              'status': 'ok',
              'software': 'NA',
              'hardware': '1.0',
              'mac_address': 'NA',
              'serial_number': 'JAF1321BFKT',
              },
          '2': {
              'ports': '0',
              'module_type': 'Fabric Module 1',
              'model': 'N7K-C7010-FAB-1',
              'status': 'ok',
              'software': 'NA',
              'hardware': '1.0',
              'mac_address': 'NA',
              'serial_number': 'JAF1320ALPC',
              },
          '3': {
              'ports': '0',
              'module_type': 'Fabric Module 1',
              'model': 'N7K-C7010-FAB-1',
              'status': 'ok',
              'software': 'NA',
              'hardware': '1.0',
              'mac_address': 'NA',
              'serial_number': 'JAF1321BFLA',
              },
          '4': {
              'ports': '0',
              'module_type': 'Fabric Module 1',
              'model': 'N7K-C7010-FAB-1',
              'status': 'ok',
              'software': 'NA',
              'hardware': '1.0',
              'mac_address': 'NA',
              'serial_number': 'JAF1321BFNA',
              },
          '5': {
              'ports': '0',
              'module_type': 'Fabric Module 1',
              'model': 'N7K-C7010-FAB-1',
              'status': 'ok',
              'software': 'NA',
              'hardware': '1.0',
              'mac_address': 'NA',
              'serial_number': 'JAF1321BFNF',
              },
          },
      }

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
        self.assertEqual(parsed_output,self.golden_parsed_output_2)

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        module_obj = ShowModule(device=self.device)
        parsed_output = module_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

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
                               'mac_address': '84:78:ac:5a:86:c1',
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
                               'mac_address': '84:78:ac:5a:86:c2',
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
                               'mac_address': '84:78:ac:5a:86:c3',
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
    vdc mac address: 84:78:ac:5a:86:c1
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
    vdc mac address: 84:78:ac:5a:86:c2
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
    vdc mac address: 84:78:ac:5a:86:c3
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

    golden_output_2 = {'execute.return_value':
    '''
    vdc id: 1
    vdc name: VACRS01001001E
    vdc state: active
    vdc mac address: 00:24:f7:16:33:41
    vdc ha policy: RELOAD
    vdc dual-sup ha policy: SWITCHOVER
    vdc boot Order: 1
    vdc create time: Thu Mar  9 21:05:39 2017
    vdc reload count: 0
    vdc restart count: 0
    vdc type: Ethernet
    vdc supported linecards: m1 f1 m1xl 

    vdc id: 2
    vdc name: otv
    vdc state: active
    vdc mac address: 00:24:f7:16:33:42
    vdc ha policy: RESTART
    vdc dual-sup ha policy: SWITCHOVER
    vdc boot Order: 1
    vdc create time: Thu Mar  9 21:10:17 2017
    vdc reload count: 0
    vdc restart count: 0
    vdc type: Ethernet
    vdc supported linecards: m1 f1 m1xl 
  '''}

    golden_parsed_output_2 = {
      'vdc': {
          '1': {
              'name': 'VACRS01001001E',
              'state': 'active',
              'mac_address': '00:24:f7:16:33:41',
              'ha_policy': 'RELOAD',
              'dual_sup_ha_policy': 'SWITCHOVER',
              'boot_order': '1',
              'create_time': 'Thu Mar  9 21:05:39 2017',
              'reload_count': '0',
              'restart_count': '0',
              'type': 'Ethernet',
              'supported_linecards': 'm1 f1 m1xl',
              },
          '2': {
              'name': 'otv',
              'state': 'active',
              'mac_address': '00:24:f7:16:33:42',
              'ha_policy': 'RESTART',
              'dual_sup_ha_policy': 'SWITCHOVER',
              'boot_order': '1',
              'create_time': 'Thu Mar  9 21:10:17 2017',
              'reload_count': '0',
              'restart_count': '0',
              'type': 'Ethernet',
              'supported_linecards': 'm1 f1 m1xl',
              },
          },
      }

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        vdc_detail_obj = ShowVdcDetail(device=self.device)
        parsed_output = vdc_detail_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        vdc_detail_obj = ShowVdcDetail(device=self.device)
        parsed_output = vdc_detail_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_2)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        vdc_detail_obj = ShowVdcDetail(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = vdc_detail_obj.parse()

class test_show_vdc_current(unittest.TestCase):
    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {'current_vdc':
                            {'id': '1',
                             'name': 'PE1'}
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
        self.device1 = Mock(**self.empty_output)
        vdc_current_obj = ShowVdcCurrent(device=self.device1)
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

    golden_output_2 = {'execute.return_value': '''
      dc_id: 0 vdc_name: Unallocated interfaces:
      Port        Status      
      ----        ----------  

      vdc_id: 2 vdc_name: otv interfaces:
      Port        Status      
      ----        ----------  
      Eth2/17     OK
      Eth2/19     OK
      Eth2/21     OK
      Eth2/23     OK
    '''}

    golden_parsed_output_2 = {
      'virtual_device': {
          '2': {
              'membership': {
                  'otv': {
                      'Eth2/17': {
                          'vd_ms_status': 'OK',
                          'vd_ms_type': 'Ethernet',
                          },
                      'Eth2/19': {
                          'vd_ms_status': 'OK',
                          'vd_ms_type': 'Ethernet',
                          },
                      'Eth2/21': {
                          'vd_ms_status': 'OK',
                          'vd_ms_type': 'Ethernet',
                          },
                      'Eth2/23': {
                          'vd_ms_status': 'OK',
                          'vd_ms_type': 'Ethernet',
                          },
                      },
                  },
              },
          },
      }

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        vdc_membership_status_obj = ShowVdcMembershipStatus(device=self.device)
        parsed_output = vdc_membership_status_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        vdc_membership_status_obj = ShowVdcMembershipStatus(device=self.device)
        parsed_output = vdc_membership_status_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_2)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        vdc_membership_status_obj = ShowVdcMembershipStatus(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = vdc_membership_status_obj.parse()

if __name__ == '__main__':
    unittest.main()
