import unittest
from unittest.mock import Mock
from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError

# c7600 show_platform
from genie.libs.parser.ios.c7600.show_platform import ShowVersion

# cat6k tests/test_show_platform
from genie.libs.parser.ios.cat6k.tests.test_show_platform import TestShowVersion as TestShowVersion_cat6k


# telnet 172.27.115.176 6034
class TestShowVersion(TestShowVersion_cat6k):

    def test_empty(self):
        self.maxDiff = None
        self.dev1 = Mock(**self.empty_output)
        obj = ShowVersion(device=self.dev1)
        with self.assertRaises(AttributeError):
            parsered_output = obj.parse()

    def test_c7600(self):
        self.maxDiff = None
        self.device = Mock(**self.output_c7600)
        obj = ShowVersion(device=self.device)
        parsed_output = obj.parse()
        import pprint
        pprint.pprint(parsed_output)
        import pdb
        pdb.set_trace()

        self.assertEqual(parsed_output, self.golden_parsed_output)

#
# class TestDir(unittest.TestCase):
#
#     dev1 = Device(name='empty')
#     dev_iosv = Device(name='c7600')
#     empty_output = {'execute.return_value': ''}
#     device_output = {'execute.return_value': '''
#     Directory of disk0:/
#
#     2  -rw-         373   May 9 2013 10:00:08 -07:00  default_config
#     3  -rw-         421   May 9 2013 10:00:20 -07:00  golden_config
#     4  -rw-   188183700   May 9 2013 10:11:56 -07:00  ISSUCleanGolden
#     5  -rw-   210179540  Oct 18 2018 07:22:24 -07:00  s72033-adventerprisek9_dbg-mz.154-0.10.S-ipcore-ssr-uut2
#
# 1024589824 bytes total (626180096 bytes free)
#     '''}
#
#     def test_empty(self):
#         self.dev1 = Mock(**self.empty_output)
#         version_obj = Dir(device=self.dev1)
#         with self.assertRaises(AttributeError):
#             parsered_output = version_obj.parse()
#
#
# class TestShowRedundancy(unittest.TestCase):
#
#     dev1 = Device(name='empty')
#     dev_iosv = Device(name='c7600')
#     empty_output = {'execute.return_value': ''}
#     device_output = {'execute.return_value': '''
#     Directory of disk0:/
#
#         2  -rw-         373   May 9 2013 10:00:08 -07:00  default_config
#         3  -rw-         421   May 9 2013 10:00:20 -07:00  golden_config
#         4  -rw-   188183700   May 9 2013 10:11:56 -07:00  ISSUCleanGolden
#         5  -rw-   210179540  Oct 18 2018 07:22:24 -07:00  s72033-adventerprisek9_dbg-mz.154-0.10.S-ipcore-ssr-uut2
#
#     1024589824 bytes total (626180096 bytes free)
#     ipcore-ssr-uut2#show redundancy
#     Redundant System Information :
#     ------------------------------
#            Available system uptime = 22 weeks, 6 days, 4 hours, 58 minutes
#     Switchovers system experienced = 0
#                   Standby failures = 0
#             Last switchover reason = none
#
#                      Hardware Mode = Duplex
#         Configured Redundancy Mode = sso
#          Operating Redundancy Mode = sso
#                   Maintenance Mode = Disabled
#                     Communications = Up
#
#     Current Processor Information :
#     -------------------------------
#                    Active Location = slot 6
#             Current Software state = ACTIVE
#            Uptime in current state = 22 weeks, 6 days, 4 hours, 57 minutes
#                      Image Version = Cisco IOS Software, s72033_rp Software (s72033_rp-ADVENTERPRISEK9_DBG-M), Version 15.4(0.10)S, EARLY DEPLOYMENT ENGINEERING WEEKLY BUILD, synced to  BLD_DARLING_122S_040709_1301
#     Technical Support: http://www.cisco.com/techsupport
#     Copyright (c) 1986-2013 by Cisco Systems, Inc.
#     Compiled Wed 26-Jun-13 02:21 by alnguyen
#                               BOOT = disk0:s72033-adventerprisek9_dbg-mz.154-0.10.S-ipcore-ssr-uut2,12;
#                        CONFIG_FILE =
#                            BOOTLDR =
#             Configuration register = 0x2
#
#     Peer Processor Information :
#     ----------------------------
#                   Standby Location = slot 5
#             Current Software state = STANDBY HOT
#            Uptime in current state = 2 weeks, 1 day, 4 hours, 31 minutes
#                      Image Version = Cisco IOS Software, s72033_rp Software (s72033_rp-ADVENTERPRISEK9_DBG-M), Version 15.4(0.10)S, EARLY DEPLOYMENT ENGINEERING WEEKLY BUILD, synced to  BLD_DARLING_122S_040709_1301
#     Technical Support: http://www.cisco.com/techsupport
#     Copyright (c) 1986-2013 by Cisco Systems, Inc.
#     Compiled Wed 26-Jun-13 02:21 by alnguyen
#                               BOOT = disk0:s72033-adventerprisek9_dbg-mz.154-0.10.S-ipcore-ssr-uut2,12;
#                        CONFIG_FILE =
#                            BOOTLDR =
#             Configuration register = 0x2
#
#     '''}
#
#     def test_empty(self):
#         self.dev1 = Mock(**self.empty_output)
#         version_obj = ShowRedundancy(device=self.dev1)
#         with self.assertRaises(AttributeError):
#             parsered_output = version_obj.parse()
#
# class TestShowInventory(unittest.TestCase):
#
#     dev1 = Device(name='empty')
#     dev_iosv = Device(name='c7600')
#     empty_output = {'execute.return_value': ''}
#     device_output = {'execute.return_value': '''
#     NAME: "CISCO7606", DESCR: "Cisco Systems Cisco 7600 6-slot Chassis System"
#     PID: CISCO7606         , VID:    , SN: FOX11140RN8
#
#     NAME: "CLK-7600 1", DESCR: "OSR-7600 Clock FRU 1"
#     PID: CLK-7600          , VID:    , SN: NWG1112014W
#
#     NAME: "CLK-7600 2", DESCR: "OSR-7600 Clock FRU 2"
#     PID: CLK-7600          , VID:    , SN: NWG1112014W
#
#     NAME: "module 1", DESCR: "WS-X6748-GE-TX CEF720 48 port 10/100/1000mb Ethernet Rev. 2.7"
#     PID: WS-X6748-GE-TX    , VID: V02, SN: SAL1209HMW3
#
#     NAME: "switching engine sub-module of 1", DESCR: "WS-F6700-CFC Centralized Forwarding Card Rev. 4.0"
#     PID: WS-F6700-CFC      , VID: V05, SN: SAL1207G5V1
#
#     NAME: "module 2", DESCR: "2 port adapter Enhanced FlexWAN Rev. 2.1"
#     PID: WS-X6582-2PA      , VID: V06, SN: JAE0939LYNQ
#
#     NAME: "module 2/1", DESCR: "Serial Port Adapter"
#     PID: PA-4T+            , VID:    , SN: 32861325
#
#     NAME: "module 5", DESCR: "WS-SUP720-3BXL 2 ports Supervisor Engine 720 Rev. 4.1"
#     PID: WS-SUP720-3BXL    , VID: V11, SN: SAD09020BF8
#
#     NAME: "msfc sub-module of 5", DESCR: "WS-SUP720 MSFC3 Daughterboard Rev. 2.2"
#     PID: WS-SUP720         , VID:    , SN: SAD090105M6
#
#     NAME: "switching engine sub-module of 5", DESCR: "WS-F6K-PFC3BXL Policy Feature Card 3 Rev. 1.4"
#     PID: WS-F6K-PFC3BXL    , VID:    , SN: SAD090301K6
#
#     NAME: "module 6", DESCR: "WS-SUP720-3BXL 2 ports Supervisor Engine 720 Rev. 5.12"
#     PID: WS-SUP720-3BXL    , VID: V11, SN: SAL15129MRC
#
#     NAME: "msfc sub-module of 6", DESCR: "WS-SUP720 MSFC3 Daughterboard Rev. 5.1"
#     PID: WS-SUP720         , VID:    , SN: SAL15045PYS
#
#     NAME: "switching engine sub-module of 6", DESCR: "WS-F6K-PFC3BXL Policy Feature Card 3 Rev. 1.11"
#     PID: WS-F6K-PFC3BXL    , VID: V02, SN: SAL15129KW4
#
#     NAME: "PS 1 PWR-1900-AC/6", DESCR: "AC_6 power supply, 1900 watt 1"
#     PID: PWR-1900-AC/6     , VID: V02, SN: DCA1104401B
#
#     NAME: "PS 2 PWR-1900-AC/6", DESCR: "AC_6 power supply, 1900 watt 2"
#     PID: PWR-1900-AC/6     , VID: V02, SN: DCA11044011
#
#     '''}
#
#     def test_empty(self):
#         self.dev1 = Mock(**self.empty_output)
#         version_obj = ShowInventory(device=self.dev1)
#         with self.assertRaises(AttributeError):
#             parsered_output = version_obj.parse()
#
# class TestShowModule(unittest.TestCase):
#     dev1 = Device(name='empty')
#     dev_iosv = Device(name='c7600')
#     empty_output = {'execute.return_value': ''}
#     device_output = {'execute.return_value': '''
#     Mod Ports Card Type                              Model              Serial No.
#     --- ----- -------------------------------------- ------------------ -----------
#       1   48  CEF720 48 port 10/100/1000mb Ethernet  WS-X6748-GE-TX     SAL1209HMW3
#       2    0  2 port adapter Enhanced FlexWAN        WS-X6582-2PA       JAE0939LYNQ
#       5    2  Supervisor Engine 720 (Hot)            WS-SUP720-3BXL     SAD09020BF8
#       6    2  Supervisor Engine 720 (Active)         WS-SUP720-3BXL     SAL15129MRC
#
#     Mod MAC addresses                       Hw   Fw            Sw           Status
#     --- ---------------------------------- ----- ------------- ------------ -------
#       1  001e.4a79.7510 to 001e.4a79.753f  2.7   12.2(14r)S    15.4(0.10)   Ok
#       2  0015.2bc3.25c0 to 0015.2bc3.25ff  2.1   15.4(0.10)S   15.4(0.10)S  Ok
#       5  0011.21b5.8e64 to 0011.21b5.8e67  4.1   8.1(3         15.4(0.10)   Ok
#       6  0022.559e.64fc to 0022.559e.64ff  5.12  8.5(4         15.4(0.10)   Ok
#
#     Mod  Sub-Module                  Model              Serial       Hw     Status
#     ---- --------------------------- ------------------ ----------- ------- -------
#       1  Centralized Forwarding Card WS-F6700-CFC       SAL1207G5V1  4.0    Ok
#       5  Policy Feature Card 3       WS-F6K-PFC3BXL     SAD090301K6  1.4    Ok
#       5  MSFC3 Daughterboard         WS-SUP720          SAD090105M6  2.2    Ok
#       6  Policy Feature Card 3       WS-F6K-PFC3BXL     SAL15129KW4  1.11   Ok
#       6  MSFC3 Daughterboard         WS-SUP720          SAL15045PYS  5.1    Ok
#
#     Mod  Online Diag Status
#     ---- -------------------
#       1  Pass
#       2  Pass
#       5  Pass
#       6  Pass
#     '''}
#
#     def test_empty(self):
#         self.dev1 = Mock(**self.empty_output)
#         version_obj = ShowModule(device=self.dev1)
#         with self.assertRaises(AttributeError):
#             parsered_output = version_obj.parse()


if __name__ == '__main__':
    unittest.main()