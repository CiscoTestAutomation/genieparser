#!/bin/env python
import unittest

from unittest.mock import Mock
from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                             SchemaMissingKeyError
from genie.libs.parser.iosxe.c9500.show_platform import ShowVersion,\
                                                        ShowRedundancy,\
                                                        ShowInventory,\
                                                        ShowPlatform


class TestShowVersion(unittest.TestCase):

    dev1 = Device(name='empty')
    dev_c9500 = Device(name='c9500')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output_c9500 = {
        "version": {
            "version_short": "2019-10-31_17.49_makale",
            "os": "IOS-XE",
            "code_name": "Amsterdam",
            "platform": "Catalyst L3 Switch",
            "image_id": "CAT9K_IOSXE",
            "version": "17.2.20191101:003833",
            "compiled_date": "Thu 31-Oct-19 17:43",
            "compiled_by": "makale",
            "rom": "IOS-XE ROMMON",
            "bootldr_version": "System Bootstrap, Version 17.1.1[FC2], RELEASE SOFTWARE (P)",
            "hostname": "SF2",
            "uptime": "1 day, 18 hours, 48 minutes",
            "returned_to_rom_by": "Reload Command",
            "system_image": "bootflash:/ecr.bin",
            "last_reload_reason": "Reload Command",
            "license_level": "AIR DNA Advantage",
            "next_reload_license_level": "AIR DNA Advantage",
            "smart_licensing_status": "UNREGISTERED/EVAL EXPIRED",
            "chassis": "C9500-32QC",
            "processor_type": "X86",
            "main_mem": "1863083",
            "processor_board_id": "CAT2242L6CG",
            'uptime_this_cp': '1 day, 18 hours, 49 minutes',
            "number_of_intfs": {
                "virtual_ethernet_interfaces": "44",
                "forty_gigabit_ethernet_interfaces": "32",
                "hundred_gigabit_ethernet_interfaces": "16"
            },
            "mem_size": {
                "non_volatile_memory": "32768",
                "physical_memory": "16002848"
            },
            "disks": {
                "bootflash:": {
                    "disk_size": "11161600"
                },
                "crashinfo:": {
                    "disk_size": "1638400"
                }
            },
            "mac_address": "70:b3:17:60:05:00",
            "mb_assembly_num": "47A7",
            "mb_sn": "CAT2242L6CG",
            "model_rev_num": "V02",
            "mb_rev_num": "4",
            "model_num": "C9500-32QC",
            "system_sn": "CAT2242L6CG",
            "curr_config_register": "0x102"
        }
    }

    golden_output_c9500 = {'execute.return_value': '''\
        show version

        Cisco IOS XE Software, Version 2019-10-31_17.49_makale

        Cisco IOS Software [Amsterdam], Catalyst L3 Switch Software (CAT9K_IOSXE), Experimental Version 17.2.20191101:003833 [HEAD-/nobackup/makale/puntject2/polaris 106]

        Copyright (c) 1986-2019 by Cisco Systems, Inc.

        Compiled Thu 31-Oct-19 17:43 by makale





        Cisco IOS-XE software, Copyright (c) 2005-2019 by cisco Systems, Inc.

        All rights reserved.  Certain components of Cisco IOS-XE software are

        licensed under the GNU General Public License ("GPL") Version 2.0.  The

        software code licensed under GPL Version 2.0 is free software that comes

        with ABSOLUTELY NO WARRANTY.  You can redistribute and/or modify such

        GPL code under the terms of GPL Version 2.0.  For more details, see the

        documentation or "License Notice" file accompanying the IOS-XE software,

        or the applicable URL provided on the flyer accompanying the IOS-XE

        software.





        ROM: IOS-XE ROMMON

        BOOTLDR: System Bootstrap, Version 17.1.1[FC2], RELEASE SOFTWARE (P)



        SF2 uptime is 1 day, 18 hours, 48 minutes

        Uptime for this control processor is 1 day, 18 hours, 49 minutes

        System returned to ROM by Reload Command

        System image file is "bootflash:/ecr.bin"

        Last reload reason: Reload Command







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





        Technology Package License Information: 



        ------------------------------------------------------------------------------

        Technology-package                                     Technology-package

        Current                        Type                       Next reboot  

        ------------------------------------------------------------------------------

        network-advantage       Smart License                    network-advantage   

        dna-advantage           Subscription Smart License       dna-advantage                 

        AIR License Level: AIR DNA Advantage

        Next reload AIR license Level: AIR DNA Advantage





        Smart Licensing Status: UNREGISTERED/EVAL EXPIRED



        cisco C9500-32QC (X86) processor with 1863083K/6147K bytes of memory.

        Processor board ID CAT2242L6CG

        44 Virtual Ethernet interfaces

        32 Forty Gigabit Ethernet interfaces

        16 Hundred Gigabit Ethernet interfaces

        32768K bytes of non-volatile configuration memory.

        16002848K bytes of physical memory.

        11161600K bytes of Bootflash at bootflash:.

        1638400K bytes of Crash Files at crashinfo:.



        Base Ethernet MAC Address          : 70:b3:17:60:05:00

        Motherboard Assembly Number        : 47A7

        Motherboard Serial Number          : CAT2242L6CG

        Model Revision Number              : V02

        Motherboard Revision Number        : 4

        Model Number                       : C9500-32QC          

        System Serial Number               : CAT2242L6CG



        Configuration register is 0x102
    '''}


    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        version_obj = ShowVersion(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsered_output = version_obj.parse()

    def test_golden_c9500(self):
        self.maxDiff = None
        self.dev_c9500 = Mock(**self.golden_output_c9500)
        version_obj = ShowVersion(device=self.dev_c9500)
        parsed_output = version_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_c9500)


class TestShowRedundancy(unittest.TestCase):
    dev1 = Device(name='empty')
    dev_c9500 = Device(name='c9500')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output_c9500 = {
        "red_sys_info": {
            "available_system_uptime": "1 day, 18 hours, 48 minutes",
            "switchovers_system_experienced": "0",
            "standby_failures": "0",
            "last_switchover_reason": "none",
            "hw_mode": "Simplex",
            "conf_red_mode": "Non-redundant",
            "oper_red_mode": "Non-redundant",
            "maint_mode": "Disabled",
            "communications": "Down",
            "communications_reason": "Failure"
        },
        "slot": {
            "slot 1": {
                "curr_sw_state": "ACTIVE",
                "uptime_in_curr_state": "1 day, 18 hours, 48 minutes",
                "image_ver": "Cisco IOS Software [Amsterdam], Catalyst L3 Switch Software (CAT9K_IOSXE), Experimental Version 17.2.20191101:003833 [HEAD-/nobackup/makale/puntject2/polaris 106]",
                "compiled_by": "makale",
                "compiled_date": "Thu 31-Oct-19 17:43",
                "boot": "bootflash:/ecr.bin;",
                "config_register": "0x102",
            }
        }
    }

    golden_output_c9500 = {'execute.return_value': '''\
        show redundancy

        Redundant System Information :

        ------------------------------

               Available system uptime = 1 day, 18 hours, 48 minutes

        Switchovers system experienced = 0

                      Standby failures = 0

                Last switchover reason = none



                         Hardware Mode = Simplex

            Configured Redundancy Mode = Non-redundant

             Operating Redundancy Mode = Non-redundant

                      Maintenance Mode = Disabled

                        Communications = Down      Reason: Failure



        Current Processor Information :

        -------------------------------

                       Active Location = slot 1

                Current Software state = ACTIVE

               Uptime in current state = 1 day, 18 hours, 48 minutes

                         Image Version = Cisco IOS Software [Amsterdam], Catalyst L3 Switch Software (CAT9K_IOSXE), Experimental Version 17.2.20191101:003833 [HEAD-/nobackup/makale/puntject2/polaris 106]

        Copyright (c) 1986-2019 by Cisco Systems, Inc.

        Compiled Thu 31-Oct-19 17:43 by makale

                                  BOOT = bootflash:/ecr.bin;

                Configuration register = 0x102



        Peer (slot: 1) information is not available because it is in 'DISABLED' state
    '''}


    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        redundancy_obj = ShowRedundancy(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = redundancy_obj.parse()

    def test_golden_c9500(self):
        self.maxDiff = None
        self.dev_c9500 = Mock(**self.golden_output_c9500)
        redundancy_obj = ShowRedundancy(device=self.dev_c9500)
        parsed_output = redundancy_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_c9500)


# ====================
# Unit test for:
#   * 'show inventory'
# ====================
class TestShowInventory(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output_c9500 = {
        "index": {
            1: {
                "name": "Chassis",
                "descr": "Cisco Catalyst 9500 Series Chassis",
                "pid": "C9500-32QC",
                "vid": "V01",
                "sn": "CAT2242L6CG"
            },
            2: {
                "name": "Power Supply Module 0",
                "descr": "Cisco Catalyst 9500 Series 650W AC Power Supply",
                "pid": "C9K-PWR-650WAC-R",
                "vid": "V01",
                "sn": "ART2216F3XV"
            },
            3: {
                "name": "Fan Tray 0",
                "descr": "Cisco Catalyst 9500 Series Fan Tray",
                "pid": "C9K-T1-FANTRAY"
            },
            4: {
                "name": "Fan Tray 1",
                "descr": "Cisco Catalyst 9500 Series Fan Tray",
                "pid": "C9K-T1-FANTRAY"
            },
            5: {
                "name": "Slot 1 Supervisor",
                "descr": "Cisco Catalyst 9500 Series Router",
                "pid": "C9500-32QC",
                "vid": "V01",
                "sn": "CAT2242L6CG"
            },
            6: {
                "name": "FortyGigabitEthernet1/0/4",
                "descr": "QSFP 40GE CU3M",
                "pid": "QSFP-H40G-CU3M",
                "vid": "V03",
                "sn": "TED2122K3A4-B"
            },
            7: {
                "name": "FortyGigabitEthernet1/0/8",
                "descr": "QSFP 40GE AOC3M",
                "pid": "QSFP-H40G-AOC3M",
                "vid": "V02",
                "sn": "FIW231301C6-B"
            },
            8: {
                "name": "FortyGigabitEthernet1/0/14",
                "descr": "QSFP 40GE AOC3M",
                "pid": "QSFP-H40G-AOC3M",
                "vid": "V02",
                "sn": "FIW231301BQ-B"
            },
            9: {
                "name": "FortyGigabitEthernet1/0/16",
                "descr": "QSFP 40GE AOC3M",
                "pid": "QSFP-H40G-AOC3M",
                "vid": "V02",
                "sn": "FIW2311023W-A"
            },
            10: {
                "name": "FortyGigabitEthernet1/0/20",
                "descr": "QSFP 40GE AOC3M",
                "pid": "QSFP-H40G-AOC3M",
                "vid": "V02",
                "sn": "FIW231301CF-B"
            },
            11: {
                "name": "HundredGigE1/0/33",
                "descr": "QSFP 100GE SR",
                "pid": "QSFP-100G-SR4-S",
                "vid": "V03",
                "sn": "INL23092488"
            },
            12: {
                "name": "HundredGigE1/0/35",
                "descr": "QSFP 100GE SR",
                "pid": "QSFP-100G-SR4-S",
                "vid": "V03",
                "sn": "AVF2243S0ZT"
            },
            13: {
                "name": "HundredGigE1/0/37",
                "descr": "QSFP 100GE SR",
                "pid": "QSFP-100G-SR4-S",
                "vid": "V03",
                "sn": "INL23092508"
            },
            14: {
                "name": "HundredGigE1/0/38",
                "descr": "QSFP 100GE AOC3M",
                "pid": "QSFP-100G-AOC3M",
                "vid": "V02",
                "sn": "FIW231000BV-A"
            },
            15: {
                "name": "HundredGigE1/0/41",
                "descr": "QSFP 100GE AOC1M",
                "pid": "QSFP-100G-AOC1M",
                "vid": "V03",
                "sn": "INL23100481-B"
            },
            16: {
                "name": "HundredGigE1/0/43",
                "descr": "QSFP 100GE CU2M",
                "pid": "QSFP-100G-CU2M",
                "sn": "APF23030058-B"
            },
            17: {
                "name": "HundredGigE1/0/44",
                "descr": "QSFP 100GE AOC3M",
                "pid": "QSFP-100G-AOC3M",
                "vid": "V02",
                "sn": "FIW23080391-B"
            },
            18: {
                "name": "HundredGigE1/0/45",
                "descr": "QSFP 100GE CU5M",
                "pid": "QSFP-100G-CU5M",
                "sn": "LCC2229G2JT-A"
            },
            19: {
                "name": "HundredGigE1/0/46",
                "descr": "QSFP 100GE AOC3M",
                "pid": "QSFP-100G-AOC3M",
                "vid": "V02",
                "sn": "FIW230802M4-B"
            },
            20: {
                "name": "HundredGigE1/0/47",
                "descr": "QSFP 100GE CU2M",
                "pid": "QSFP-100G-CU2M",
                "sn": "LCC2250H9M1-B"
            },
            21: {
                "name": "HundredGigE1/0/48",
                "descr": "QSFP 100GE SR",
                "pid": "QSFP-100G-SR4-S",
                "vid": "V03",
                "sn": "AVF2243S10A"
            }
        }
    }

    golden_output_c9500 = {'execute.return_value': '''
        show inventory

        NAME: "Chassis", DESCR: "Cisco Catalyst 9500 Series Chassis"

        PID: C9500-32QC        , VID: V01  , SN: CAT2242L6CG



        NAME: "Power Supply Module 0", DESCR: "Cisco Catalyst 9500 Series 650W AC Power Supply"

        PID: C9K-PWR-650WAC-R  , VID: V01  , SN: ART2216F3XV



        NAME: "Fan Tray 0", DESCR: "Cisco Catalyst 9500 Series Fan Tray"

        PID: C9K-T1-FANTRAY    , VID:      , SN:            



        NAME: "Fan Tray 1", DESCR: "Cisco Catalyst 9500 Series Fan Tray"

        PID: C9K-T1-FANTRAY    , VID:      , SN:            



        NAME: "Slot 1 Supervisor", DESCR: "Cisco Catalyst 9500 Series Router"

        PID: C9500-32QC        , VID: V01  , SN: CAT2242L6CG



        NAME: "FortyGigabitEthernet1/0/4", DESCR: "QSFP 40GE CU3M"

        PID: QSFP-H40G-CU3M      , VID: V03  , SN: TED2122K3A4-B   



        NAME: "FortyGigabitEthernet1/0/8", DESCR: "QSFP 40GE AOC3M"

        PID: QSFP-H40G-AOC3M     , VID: V02  , SN: FIW231301C6-B   



        NAME: "FortyGigabitEthernet1/0/14", DESCR: "QSFP 40GE AOC3M"

        PID: QSFP-H40G-AOC3M     , VID: V02  , SN: FIW231301BQ-B   



        NAME: "FortyGigabitEthernet1/0/16", DESCR: "QSFP 40GE AOC3M"

        PID: QSFP-H40G-AOC3M     , VID: V02  , SN: FIW2311023W-A   



        NAME: "FortyGigabitEthernet1/0/20", DESCR: "QSFP 40GE AOC3M"

        PID: QSFP-H40G-AOC3M     , VID: V02  , SN: FIW231301CF-B   



        NAME: "HundredGigE1/0/33", DESCR: "QSFP 100GE SR"

        PID: QSFP-100G-SR4-S     , VID: V03  , SN: INL23092488     



        NAME: "HundredGigE1/0/35", DESCR: "QSFP 100GE SR"

        PID: QSFP-100G-SR4-S     , VID: V03  , SN: AVF2243S0ZT     



        NAME: "HundredGigE1/0/37", DESCR: "QSFP 100GE SR"

        PID: QSFP-100G-SR4-S     , VID: V03  , SN: INL23092508     



        NAME: "HundredGigE1/0/38", DESCR: "QSFP 100GE AOC3M"

        PID: QSFP-100G-AOC3M     , VID: V02  , SN: FIW231000BV-A   



        NAME: "HundredGigE1/0/41", DESCR: "QSFP 100GE AOC1M"

        PID: QSFP-100G-AOC1M     , VID: V03  , SN: INL23100481-B   



        NAME: "HundredGigE1/0/43", DESCR: "QSFP 100GE CU2M"

        PID: QSFP-100G-CU2M      , VID:      , SN: APF23030058-B   



        NAME: "HundredGigE1/0/44", DESCR: "QSFP 100GE AOC3M"

        PID: QSFP-100G-AOC3M     , VID: V02  , SN: FIW23080391-B   



        NAME: "HundredGigE1/0/45", DESCR: "QSFP 100GE CU5M"

        PID: QSFP-100G-CU5M      , VID:      , SN: LCC2229G2JT-A   



        NAME: "HundredGigE1/0/46", DESCR: "QSFP 100GE AOC3M"

        PID: QSFP-100G-AOC3M     , VID: V02  , SN: FIW230802M4-B   



        NAME: "HundredGigE1/0/47", DESCR: "QSFP 100GE CU2M"

        PID: QSFP-100G-CU2M      , VID:      , SN: LCC2250H9M1-B   



        NAME: "HundredGigE1/0/48", DESCR: "QSFP 100GE SR"

        PID: QSFP-100G-SR4-S     , VID: V03  , SN: AVF2243S10A   
    '''}


    def test_show_inventory_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        inventory_obj = ShowInventory(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = inventory_obj.parse()

    def test_show_inventory_golden_c9500(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_c9500)
        inventory_obj = ShowInventory(device=self.device)
        parsed_output = inventory_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_c9500)


class TestShowPlatform(unittest.TestCase):
    dev1 = Device(name='empty')
    dev_c9500 = Device(name='c9500')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output_c9500 = {
        "chassis": "C9500-32QC",
        "slot": {
            "1": {
                "name": "C9500-32QC",
                "state": "ok",
                "insert_time": "1d18h",
                "slot": "1",
                "cpld_ver": "19061022",
                "fw_ver": "17.1.1[FC2]",
                "subslot": {
                    "0": {
                        "name": "C9500-32QC",
                        "state": "ok",
                        "insert_time": "1d18h",
                        "subslot": "0"
                    }
                }
            },
            "R0": {
                "name": "C9500-32QC",
                "state": "ok, active",
                "insert_time": "1d18h",
                "slot": "R0"
            },
            "P0": {
                "name": "C9K-PWR-650WAC-R",
                "state": "ok",
                "insert_time": "1d18h",
                "slot": "P0"
            },
            "P2": {
                "name": "C9K-T1-FANTRAY",
                "state": "ok",
                "insert_time": "1d18h",
                "slot": "P2"
            },
            "P3": {
                "name": "C9K-T1-FANTRAY",
                "state": "ok",
                "insert_time": "1d18h",
                "slot": "P3",
            }
        }
    }

    golden_output_c9500 = {'execute.return_value': '''\
        show platform

        Chassis type: C9500-32QC          



        Slot      Type                State                 Insert time (ago) 

        --------- ------------------- --------------------- ----------------- 

        1         C9500-32QC          ok                    1d18h         

         1/0      C9500-32QC          ok                    1d18h         

        R0        C9500-32QC          ok, active            1d18h         

        P0        C9K-PWR-650WAC-R    ok                    1d18h         

        P2        C9K-T1-FANTRAY      ok                    1d18h         

        P3        C9K-T1-FANTRAY      ok                    1d18h         



        Slot      CPLD Version        Firmware Version                        

        --------- ------------------- --------------------------------------- 

        1         19061022            17.1.1[FC2]                         

    '''}


    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        platform_obj = ShowPlatform(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = platform_obj.parse()

    def test_golden_c9500(self):
        self.maxDiff = None
        self.dev_c9500 = Mock(**self.golden_output_c9500)
        platform_obj = ShowPlatform(device=self.dev_c9500)
        parsed_output = platform_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_c9500)


if __name__ == '__main__':
    unittest.main()