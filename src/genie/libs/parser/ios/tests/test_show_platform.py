#!/bin/env python
import unittest
from unittest.mock import Mock
from pyats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
    SchemaMissingKeyError
from genie.libs.parser.ios.show_platform import ShowVersion, \
    Dir, \
    ShowRedundancy, \
    ShowInventory, \
    ShowBootvar, \
    ShowProcessesCpuSorted, \
    ShowProcessesCpu, \
    ShowVersionRp, \
    ShowPlatform, \
    ShowPlatformPower, \
    ShowProcessesCpuHistory, \
    ShowProcessesCpuPlatform, \
    ShowPlatformSoftwareStatusControl, \
    ShowPlatformSoftwareSlotActiveMonitorMem, \
    ShowPlatformHardware, \
    ShowPlatformHardwarePlim, \
    ShowPlatformHardwareQfpBqsOpmMapping, \
    ShowPlatformHardwareQfpBqsIpmMapping, \
    ShowPlatformHardwareSerdes, \
    ShowPlatformHardwareSerdesInternal, \
    ShowPlatformHardwareQfpBqsStatisticsChannelAll, \
    ShowPlatformHardwareQfpInterfaceIfnameStatistics, \
    ShowPlatformHardwareQfpStatisticsDrop, \
    ShowEnvironment, \
    ShowModule, \
    ShowSwitch, ShowSwitchDetail

from genie.libs.parser.iosxe.tests.test_show_platform import TestShowPlatform as test_show_platform_iosxe, \
    TestShowPlatformPower as test_show_platform_power_iosxe, \
    TestShowVersionRp as test_show_version_rp_iosxe, \
    TestShowProcessesCpu as test_show_processes_cpu_iosxe, \
    TestShowProcessesCpuHistory as test_show_processes_cpu_history_iosxe, \
    TestShowProcessesCpuPlatform as test_show_processes_cpu_platform_iosxe, \
    TestShowPlatformSoftwareStatusControlProcessorBrief as test_show_platform_software_status_control_processor_brief_iosxe, \
    TestShowPlatformSoftwareSlotActiveMonitorMemSwap as test_show_platform_software_slot_active_monitor_Mem_iosxe, \
    TestShowPlatformHardware as test_show_platform_hardware_iosxe, \
    TestShowPlatformHardwarePlim as test_show_platform_hardware_plim_iosxe, \
    TestShowPlatformHardwareQfpBqsOpmMapping as test_show_platform_hardware_qfp_bqs_opm_mapping_iosxe, \
    TestShowPlatformHardwareQfpBqsIpmMapping as test_show_platform_hardware_qfp_bqs_ipm_mapping_iosxe, \
    TestShowPlatformHardwareSerdesStatistics as test_show_platform_hardware_serdes_statistics_iosxe, \
    TestShowPlatformHardwareSerdesStatisticsInternal as test_show_platform_hardware_serdes_statistics_internal_iosxe, \
    ShowPlatformHardwareQfpBqsStatisticsChannelAll as show_platform_hardware_qfp_bqs_statistics_channel_all_iosxe, \
    ShowPlatformHardwareQfpInterface as show_platform_hardware_qfp_interface_iosxe, \
    TestShowPlatformHardwareQfpStatisticsDrop as test_show_platform_hardware_qfp_statistics_drop_iosxe, \
    TestShowEnv as test_show_env_iosxe, \
    TestShowModule as test_show_module_iosxe, \
    TestShowSwitch as test_show_switch_iosxe, \
    TestShowSwitchDetail as test_show_switch_detail_iosxe


class TestShowVersion(unittest.TestCase):
    dev1 = Device(name='empty')
    dev_iosv = Device(name='iosv')
    empty_output = {'execute.return_value': ''}
    semi_empty_output = {'execute.return_value': '''\
        ROM: Bootstrap program is IOSv
    '''}

    golden_parsed_output_iosv = {
        "version": {
            "last_reload_reason": "Unknown reason",
            "hostname": "N95_1",
            "os": "IOS",
            "version_short": "15.6",
            "number_of_intfs": {
                "Gigabit Ethernet": "6"
            },
            "version": "15.6(3)M2",
            "rtr_type": "IOSv",
            "chassis_sn": "9K66Z7TOKAACDEQA24N7S",
            "chassis": "IOSv",
            "image_id": "VIOS-ADVENTERPRISEK9-M",
            'compiled_by': 'prod_rel_team',
            'compiled_date': 'Wed 29-Mar-17 14:05',
            "processor_type": "revision 1.0",
            "platform": "IOSv",
            "image_type": "production image",
            'processor_board_flash': '10080K',
            'returned_to_rom_by': 'reload',
            "main_mem": "435457",
            "mem_size": {
                "non-volatile configuration": "256"
            },
            "system_image": "flash0:/vios-adventerprisek9-m",
            "curr_config_register": "0x0",
            "rom": "Bootstrap program is IOSv",
            "uptime": "1 day, 16 hours, 42 minutes"
        }
    }

    golden_output_iosv = {'execute.return_value': '''\
        Cisco IOS Software, IOSv Software (VIOS-ADVENTERPRISEK9-M), Version 15.6(3)M2, RELEASE SOFTWARE (fc2)
        Technical Support: http://www.cisco.com/techsupport
        Copyright (c) 1986-2017 by Cisco Systems, Inc.
        Compiled Wed 29-Mar-17 14:05 by prod_rel_team


        ROM: Bootstrap program is IOSv

        N95_1 uptime is 1 day, 16 hours, 42 minutes
        System returned to ROM by reload
        System image file is "flash0:/vios-adventerprisek9-m"
        Last reload reason: Unknown reason



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

        Cisco IOSv (revision 1.0) with  with 435457K/87040K bytes of memory.
        Processor board ID 9K66Z7TOKAACDEQA24N7S
        6 Gigabit Ethernet interfaces
        DRAM configuration is 72 bits wide with parity disabled.
        256K bytes of non-volatile configuration memory.
        2097152K bytes of ATA System CompactFlash 0 (Read/Write)
        0K bytes of ATA CompactFlash 1 (Read/Write)
        0K bytes of ATA CompactFlash 2 (Read/Write)
        10080K bytes of ATA CompactFlash 3 (Read/Write)

        Configuration register is 0x0'''}

    golden_parsed_output_ios = {
        'version': {'bootldr': 'C3750E Boot Loader (C3750X-HBOOT-M) Version '
                               '15.2(3r)E, RELEASE SOFTWARE (fc1)',
                    'chassis': 'WS-C3750X-24P',
                    'chassis_sn': 'FDO2028F1WK',
                    'curr_config_register': '0xF',
                    'compiled_by': 'prod_rel_team',
                    'compiled_date': 'Wed 26-Jun-13 09:56',
                    'hostname': 'R5',
                    'image_id': 'C3750E-UNIVERSALK9-M',
                    'image_type': 'production image',
                    'last_reload_reason': 'power-on',
                    'license_level': 'ipservices',
                    'license_type': 'Permanent',
                    'main_mem': '262144',
                    'mem_size': {'flash-simulated non-volatile configuration': '512'},
                    'next_reload_license_level': 'ipservices',
                    'number_of_intfs': {'Gigabit Ethernet': '28',
                                        'Ten Gigabit Ethernet': '2',
                                        'Virtual Ethernet': '2',
                                        'Gigabit Ethernet': '28',
                                        'FastEthernet': '1'
                                        },
                    'os': 'IOS',
                    'platform': 'C3750E',
                    'processor_type': 'PowerPC405',
                    'returned_to_rom_by': 'power-on',
                    'rom': 'Bootstrap program is C3750E boot loader',
                    'rtr_type': 'WS-C3750X-24P',
                    'system_image': 'flash:c3750e-universalk9-mz',
                    'system_restarted_at': '12:22:21 PDT Mon Sep 10 2018',
                    'uptime': '9 weeks, 4 days, 2 hours, 3 minutes',
                    'version': '12.2(55)SE8',
                    'version_short': '12.2',
                    'image': {
                        'data_base': '0x02800000',
                        'text_base': '0x00003000',
                        },
                    'switch_num': {
                        '1': {
                            'ports': '30',
                            'model': 'WS-C3750X-24P',
                            'sw_ver': '12.2(55)SE8',
                            'sw_image': 'C3750E-UNIVERSALK9-M',
                            'active': True,
                            'mac_address': '84:3D:C6:FF:F1:B8',
                            'mb_assembly_num': '73-15476-04',
                            'mb_sn': 'FDO202907UH',
                            'model_rev_num': 'W0',
                            'mb_rev_num': 'B0',
                            'model_num': 'WS-C3750X-24P-L',
                            'db_assembly_num': '800-32727-03',
                            'db_sn': 'FDO202823P8',
                            'system_sn': 'FDO2028F1WK',
                            'top_assembly_part_num': '800-38990-01',
                            'top_assembly_rev_num': 'F0',
                            'version_id': 'V07',
                            'clei_code_num': 'CMMPP00DRB',
                            'hb_rev_num': '0x05'
                        }
                    }
        }
    }

    golden_output_ios = {'execute.return_value': '''\
        Cisco IOS Software, C3750E Software (C3750E-UNIVERSALK9-M), Version 12.2(55)SE8, RELEASE SOFTWARE (fc2)
        Technical Support: http://www.cisco.com/techsupport
        Copyright (c) 1986-2013 by Cisco Systems, Inc.
        Compiled Wed 26-Jun-13 09:56 by prod_rel_team
        Image text-base: 0x00003000, data-base: 0x02800000

        ROM: Bootstrap program is C3750E boot loader
        BOOTLDR: C3750E Boot Loader (C3750X-HBOOT-M) Version 15.2(3r)E, RELEASE SOFTWARE (fc1)

        R5 uptime is 9 weeks, 4 days, 2 hours, 3 minutes
        System returned to ROM by power-on
        System restarted at 12:22:21 PDT Mon Sep 10 2018
        System image file is "flash:c3750e-universalk9-mz"


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

        License Level: ipservices
        License Type: Permanent
        Next reload license Level: ipservices

        cisco WS-C3750X-24P (PowerPC405) processor (revision W0) with 262144K bytes of memory.
        Processor board ID FDO2028F1WK
        Last reset from power-on
        2 Virtual Ethernet interfaces
        1 FastEthernet interface
        28 Gigabit Ethernet interfaces
        2 Ten Gigabit Ethernet interfaces
        The password-recovery mechanism is enabled.

        512K bytes of flash-simulated non-volatile configuration memory.
        Base ethernet MAC Address       : 84:3D:C6:FF:F1:B8
        Motherboard assembly number     : 73-15476-04
        Motherboard serial number       : FDO202907UH
        Model revision number           : W0
        Motherboard revision number     : B0
        Model number                    : WS-C3750X-24P-L
        Daughterboard assembly number   : 800-32727-03
        Daughterboard serial number     : FDO202823P8
        System serial number            : FDO2028F1WK
        Top Assembly Part Number        : 800-38990-01
        Top Assembly Revision Number    : F0
        Version ID                      : V07
        CLEI Code Number                : CMMPP00DRB
        Hardware Board Revision Number  : 0x05


        Switch Ports Model              SW Version            SW Image                 
        ------ ----- -----              ----------            ----------               
        *    1 30    WS-C3750X-24P      12.2(55)SE8           C3750E-UNIVERSALK9-M     


        Configuration register is 0xF

    '''}

    golden_parsed_output_ios_cat6k = {
        "version": {
            "os": "IOS",
            "version_short": "12.2",
            "platform": "s72033_rp",
            "version": "12.2(18)SXF7",
            "image_id": "s72033_rp-ADVENTERPRISEK9_WAN-M",
            'compiled_by': 'kellythw',
            'compiled_date': 'Thu 23-Nov-06 06:26',
            "image_type": "production image",
            "rom": "System Bootstrap, Version 12.2(17r)S4, RELEASE SOFTWARE (fc1)",
            "bootldr": "s72033_rp Software (s72033_rp-ADVENTERPRISEK9_WAN-M), Version 12.2(18)SXF7, RELEASE SOFTWARE (fc1)",
            "hostname": "cat6k_tb1",
            "uptime": "10 weeks, 5 days, 5 hours, 16 minutes",
            "system_image": "disk0:s72033-adventerprisek9_wan-mz.122-18.SXF7",
            "chassis": "WS-C6503-E",
            "main_mem": "983008",
            "processor_type": "R7000",
            'sp_by': 'power on',
            'returned_to_rom_at': '21:57:23 UTC Sat Aug 28 2010',
            'returned_to_rom_by': 'power cycle',
            "rtr_type": "WS-C6503-E",
            "chassis_sn": "FXS1821Q2H9",
            "last_reload_reason": "s/w reset",
            'processor_board_flash': '65536K',
            "number_of_intfs": {
                "Gigabit Ethernet/IEEE 802.3": "50",
                'Virtual Ethernet/IEEE 802.3': '1'
            },
            "mem_size": {"non-volatile configuration": "1917", "packet buffer": "8192"},
            "curr_config_register": "0x2102",
            'image': {
                'data_base': '0x42D98000',
                'text_base': '0x40101040',
            },
        }
    }

    golden_output_ios_cat6k = {'execute.return_value': '''
        show version
        Cisco Internetwork Operating System Software
        IOS (tm) s72033_rp Software (s72033_rp-ADVENTERPRISEK9_WAN-M), Version 12.2(18)SXF7, RELEASE SOFTWARE (fc1)
        Technical Support: http://www.cisco.com/techsupport
        Copyright (c) 1986-2006 by cisco Systems, Inc.
        Compiled Thu 23-Nov-06 06:26 by kellythw
        Image text-base: 0x40101040, data-base: 0x42D98000

        ROM: System Bootstrap, Version 12.2(17r)S4, RELEASE SOFTWARE (fc1)
        BOOTLDR: s72033_rp Software (s72033_rp-ADVENTERPRISEK9_WAN-M), Version 12.2(18)SXF7, RELEASE SOFTWARE (fc1)

        cat6k_tb1 uptime is 10 weeks, 5 days, 5 hours, 16 minutes
        Time since cat6k_tb1 switched to active is 10 weeks, 5 days, 5 hours, 15 minutes
        System returned to ROM by  power cycle at 21:57:23 UTC Sat Aug 28 2010 (SP by power on)
        System image file is "disk0:s72033-adventerprisek9_wan-mz.122-18.SXF7"


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

        cisco WS-C6503-E (R7000) processor (revision 1.4) with 983008K/65536K bytes of memory.
        Processor board ID FXS1821Q2H9
        SR71000 CPU at 600Mhz, Implementation 0x504, Rev 1.2, 512KB L2 Cache
        Last reset from s/w reset
        SuperLAT software (copyright 1990 by Meridian Technology Corp).
        X.25 software, Version 3.0.0.
        Bridging software.
        TN3270 Emulation software.
        1 Virtual Ethernet/IEEE 802.3 interface
        50 Gigabit Ethernet/IEEE 802.3 interfaces
        1917K bytes of non-volatile configuration memory.
        8192K bytes of packet buffer memory.

        65536K bytes of Flash internal SIMM (Sector size 512K).
        Configuration register is 0x2102
    '''}

    golden_output_ios_1 = {'execute.return_value': '''\
    Cisco IOS Software, C3750E Software (C3750E-UNIVERSALK9-M), Version 15.2(2)E8, RELEASE SOFTWARE (fc1)
    Technical Support: http://www.cisco.com/techsupport
    Copyright (c) 1986-2018 by Cisco Systems, Inc.
    Compiled Mon 22-Jan-18 04:07 by prod_rel_team

    ROM: Bootstrap program is C3750E boot loader
    BOOTLDR: C3750E Boot Loader (C3750X-HBOOT-M) Version 12.2(58r)SE, RELEASE SOFTWARE (fc1)

    sample_switch uptime is 8 weeks, 3 days, 10 hours, 27 minutes
    System returned to ROM by power-on
    System restarted at 05:06:40 GMT Tue Sep 10 2019
    System image file is "flash:c3750e-universalk9-mz.152-2.E8.bin"
    Last reload reason: Reload command



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

    License Level: ipservices
    License Type: Permanent
    Next reload license Level: ipservices

    cisco WS-C3750X-24S (PowerPC405) processor (revision A0) with 524288K bytes of memory.
    Processor board ID FDO1633Q14S
    Last reset from power-on
    14 Virtual Ethernet interfaces
    1 FastEthernet interface
    28 Gigabit Ethernet interfaces
    2 Ten Gigabit Ethernet interfaces
    The password-recovery mechanism is enabled.

    512K bytes of flash-simulated non-volatile configuration memory.
    Base ethernet MAC Address       : AC:F2:C5:FF:55:E7
    Motherboard assembly number     : 73-13061-04
    Motherboard serial number       : FDO1633Q14M
    Model revision number           : A0
    Motherboard revision number     : A0
    Model number                    : WS-C3750X-24S-E
    Daughterboard assembly number   : 800-32727-03
    Daughterboard serial number     : FDO172217ED
    System serial number            : FDO1633Q14S
    Top Assembly Part Number        : 800-33746-04
    Top Assembly Revision Number    : B0
    Version ID                      : V03
    CLEI Code Number                : CMMFF00ARC
    Hardware Board Revision Number  : 0x04


    Switch Ports Model                     SW Version            SW Image
    ------ ----- -----                     ----------            ----------
    *    1 30    WS-C3750X-24S             15.2(2)E8             C3750E-UNIVERSALK9-M


    Configuration register is 0xF

    '''}

    golden_parsed_output_ios_1 = {
        'version': {'version_short': '15.2',
                    'platform': 'C3750E',
                    'version': '15.2(2)E8',
                    'image_id': 'C3750E-UNIVERSALK9-M',
                    'os': 'IOS',
                    'image_type': 'production image',
                    'compiled_date': 'Mon 22-Jan-18 04:07',
                    'compiled_by': 'prod_rel_team',
                    'rom': 'Bootstrap program is C3750E boot loader',
                    'bootldr': 'C3750E Boot Loader (C3750X-HBOOT-M) Version 12.2(58r)SE, RELEASE SOFTWARE (fc1)',
                    'hostname': 'sample_switch',
                    'uptime': '8 weeks, 3 days, 10 hours, 27 minutes',
                    'returned_to_rom_by': 'power-on',
                    'system_restarted_at': '05:06:40 GMT Tue Sep 10 2019',
                    'system_image': 'flash:c3750e-universalk9-mz.152-2.E8.bin',
                    'last_reload_reason': 'power-on',
                    'license_level': 'ipservices',
                    'license_type': 'Permanent',
                    'next_reload_license_level': 'ipservices',
                    'chassis': 'WS-C3750X-24S',
                    'main_mem': '524288',
                    'processor_type': 'PowerPC405',
                    'rtr_type': 'WS-C3750X-24S',
                    'chassis_sn': 'FDO1633Q14S',
                    'number_of_intfs': {
                        'Virtual Ethernet': '14',
                        'FastEthernet': '1',
                        'Gigabit Ethernet': '28',
                        'Ten Gigabit Ethernet': '2'
                    },
                    'mem_size': {
                        'flash-simulated non-volatile configuration': '512'
                    },
                    'curr_config_register': '0xF'
                    }
    }

    device_output = {'execute.return_value': '''
    best-c3945-IOS3#show version
    Cisco IOS Software, C3900 Software (C3900-UNIVERSALK9-M), Version 15.0(1)M7, RELEASE SOFTWARE (fc2)
    Technical Support: http://www.cisco.com/techsupport
    Copyright (c) 1986-2011 by Cisco Systems, Inc.
    Compiled Fri 05-Aug-11 00:32 by prod_rel_team
    
    ROM: System Bootstrap, Version 15.0(1r)M13, RELEASE SOFTWARE (fc1)
    
    best-c3945-IOS3 uptime is 1 hour, 20 minutes
    System returned to ROM by reload at 10:26:47 EST Mon Dec 9 2019
    System restarted at 10:27:57 EST Mon Dec 9 2019
    System image file is "flash0:c3900-universalk9-mz.SPA.150-1.M7.bin"
    Last reload type: Normal Reload
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
              
    Cisco CISCO3945-CHASSIS (revision 1.1) with C3900-SPE150/K9 with 2027520K/69632K bytes of memory.
    Processor board ID FGL161010K8
    2 FastEthernet interfaces
    3 Gigabit Ethernet interfaces
    1 Virtual Private Network (VPN) Module
    DRAM configuration is 72 bits wide with parity enabled.
    255K bytes of non-volatile configuration memory.
    2000880K bytes of ATA System CompactFlash 0 (Read/Write)
              
              
    License Info:
              
    License UDI:
              
    -------------------------------------------------
    Device#   PID                   SN
    -------------------------------------------------
    *0        C3900-SPE150/K9       FOC16050QP6     
              
              
              
    Technology Package License Information for Module:'c3900' 
              
    -----------------------------------------------------------------
    Technology    Technology-package           Technology-package
                  Current       Type           Next reboot  
    ------------------------------------------------------------------
    ipbase        ipbasek9      Permanent      ipbasek9
    security      securityk9    Permanent      securityk9
    uc            None          None           None
    data          datak9        Permanent      datak9
              
    Configuration register is 0x2102
    '''}

    parsed_output = {
        'version': {
            'chassis': 'CISCO3945-CHASSIS',
            'chassis_sn': 'FGL161010K8',
            'compiled_by': 'prod_rel_team',
            'compiled_date': 'Fri 05-Aug-11 00:32',
            'curr_config_register': '0x2102',
            'hostname': 'best-c3945-IOS3',
            'image_id': 'C3900-UNIVERSALK9-M',
            'image_type': 'production image',
            'last_reload_reason': 'Reload Command',
            'last_reload_type': 'Normal Reload',
            'license_udi': {
                'device_num': {
                    '*0': {
                        'pid': 'C3900-SPE150/K9',
                        'sn': 'FOC16050QP6'
                    }
                }
            },
            'license_package': {
                'data': {
                    'license_level': 'datak9',
                    'license_type': 'Permanent',
                    'next_reload_license_level': 'datak9',
                },
                'ipbase': {
                    'license_level': 'ipbasek9',
                    'license_type': 'Permanent',
                    'next_reload_license_level': 'ipbasek9',
                },
                'security': {
                    'license_level': 'securityk9',
                    'license_type': 'Permanent',
                    'next_reload_license_level': 'securityk9',
                },
                'uc': {
                    'license_level': 'None',
                    'license_type': 'None',
                    'next_reload_license_level': 'None',
                },
            },
            'main_mem': '2027520',
            'mem_size': {
                'non-volatile configuration': '255',
            },
            'number_of_intfs': {
                'FastEthernet': '2',
                'Gigabit Ethernet': '3',
            },
            'os': 'IOS',
            'platform': 'C3900',
            'processor_board_flash': '2000880K',
            'processor_type': 'C3900-SPE150/K9',
            'returned_to_rom_at': '10:26:47 EST Mon Dec 9 2019',
            'returned_to_rom_by': 'reload',
            'rom': 'System Bootstrap, Version 15.0(1r)M13, RELEASE SOFTWARE (fc1)',
            'rtr_type': 'CISCO3945-CHASSIS',
            'system_image': 'flash0:c3900-universalk9-mz.SPA.150-1.M7.bin',
            'system_restarted_at': '10:27:57 EST Mon Dec 9 2019',
            'uptime': '1 hour, 20 minutes',
            'version': '15.0(1)M7',
            'version_short': '15.0',
        },
    }

    golden_output_ios_2 = {'execute.return_value': '''
    show version
    Cisco Internetwork Operating System Software 
    IOS (tm) Catalyst 4000 L3 Switch Software (cat4000-I9S-M), Version 12.2(18)EW5, RELEASE SOFTWARE (fc1)
    Technical Support: http://www.cisco.com/techsupport
    Copyright (c) 1986-2005 by cisco Systems, Inc.
    Compiled Wed 07-Sep-05 11:16 by someone
    Image text-base: 0x00000000, data-base: 0x010BF898
    
    ROM: 12.2(20r)EW1
    Dagobah Revision 95, Swamp Revision 6
    
    GENIE123123 uptime is 1 years, 2 weeks, 3 days, 4 hours, 5 minutes
    System returned to ROM by RPR Switchover
    System restarted at 13:54:51 CET Sun Apr 15 2007
    System image file is "bootflash:cat4000-i9s-mz.122-18.EW5.bin"
    
    cisco WS-C4507R (MPC8245) processor (revision 8) with 524288K bytes of memory.
    Processor board ID FOX093206HY
    Last reset from Reload
    2 Virtual Ethernet/IEEE 802.3  interface(s)
    244 Gigabit Ethernet/IEEE 802.3 interface(s)
    511K bytes of non-volatile configuration memory.
    
    Configuration register is 0x2102
    
    GENIE123123#
    '''}

    golden_parsed_output_ios_2 = {
        'version': {
            'chassis': 'WS-C4507R',
            'chassis_sn': 'FOX093206HY',
            'compiled_by': 'someone',
            'compiled_date': 'Wed 07-Sep-05 11:16',
            'curr_config_register': '0x2102',
            'hostname': 'GENIE123123',
            'image': {
                'data_base': '0x010BF898',
                'text_base': '0x00000000',
            },
            'image_id': 'cat4000-I9S-M',
            'image_type': 'production image',
            'interfaces': {
                'gigabit_ethernet': 244,
                'virtual_ethernet': 2,
            },
            'last_reload_reason': 'Reload',
            'main_mem': '524288',
            'mem_size': {
                'non-volatile configuration': '511',
            },
            'os': 'IOS',
            'platform': 'Catalyst 4000 L3 Switch',
            'processor_type': 'MPC8245',
            'returned_to_rom_by': 'RPR Switchover',
            'revision': {
                'Dagobah': 95,
                'Swamp': 6,
            },
            'rom': '12.2(20r)EW1',
            'rtr_type': 'WS-C4507R',
            'system_image': 'bootflash:cat4000-i9s-mz.122-18.EW5.bin',
            'system_restarted_at': '13:54:51 CET Sun Apr 15 2007',
            'uptime': '1 years, 2 weeks, 3 days, 4 hours, 5 minutes',
            'version': '12.2(18)EW5',
            'version_short': '12.2',
        },
    }

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        version_obj = ShowVersion(device=self.dev1)
        with self.assertRaises(AttributeError):
            parsered_output = version_obj.parse()

    def test_semi_empty(self):
        self.dev1 = Mock(**self.semi_empty_output)
        version_obj = ShowVersion(device=self.dev1)
        with self.assertRaises(KeyError):
            parsed_output = version_obj.parse()

    def test_golden_iosv(self):
        self.maxDiff = None
        self.dev_iosv = Mock(**self.golden_output_iosv)
        version_obj = ShowVersion(device=self.dev_iosv)
        parsed_output = version_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_iosv)

    def test_golden_ios(self):
        self.maxDiff = None
        self.dev_iosv = Mock(**self.golden_output_ios)
        version_obj = ShowVersion(device=self.dev_iosv)
        parsed_output = version_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_ios)

    def test_golden_ios_cat6k(self):
        self.maxDiff = None
        self.dev_iosv = Mock(**self.golden_output_ios_cat6k)
        version_obj = ShowVersion(device=self.dev_iosv)
        parsed_output = version_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_ios_cat6k)

    def test_golden_ios_1(self):
        self.maxDiff = None
        self.dev_iosv = Mock(**self.golden_output_ios_1)
        version_obj = ShowVersion(device=self.dev_iosv)
        parsed_output = version_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_ios_1)

    def test_golden_ios_2(self):
        self.maxDiff = None
        self.dev_iosv = Mock(**self.device_output)
        version_obj = ShowVersion(device=self.dev_iosv)
        parsed_output = version_obj.parse()
        self.assertEqual(parsed_output, self.parsed_output)

    def test_golden_ios_3(self):
        self.maxDiff = None
        self.dev_iosv = Mock(**self.golden_output_ios_2)
        version_obj = ShowVersion(device=self.dev_iosv)
        parsed_output = version_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_ios_2)


class test_dir(unittest.TestCase):
    dev1 = Device(name='empty')
    dev_iosv = Device(name='iosv')
    empty_output = {'execute.return_value': ''}
    semi_empty_output = {'execute.return_value': '''\
        Directory of flash:/
    '''}

    golden_parsed_output_iosv = {
        "dir": {
            "flash0:/": {
                "files": {
                    "e1000_bia.txt": {
                        "last_modified_date": "Oct 17 2018 18:57:18 +00:00",
                        "index": "269",
                        "size": "119",
                        "permissions": "-rw-"
                    },
                    "config": {
                        "last_modified_date": "Oct 14 2013 00:00:00 +00:00",
                        "index": "264",
                        "size": "0",
                        "permissions": "drw-"
                    },
                    "nvram": {
                        "last_modified_date": "Oct 17 2018 18:57:10 +00:00",
                        "index": "268",
                        "size": "524288",
                        "permissions": "-rw-"
                    },
                    "boot": {
                        "last_modified_date": "Jan 30 2013 00:00:00 +00:00",
                        "index": "1",
                        "size": "0",
                        "permissions": "drw-"
                    },
                    "vios-adventerprisek9-m": {
                        "last_modified_date": "Mar 29 2017 00:00:00 +00:00",
                        "index": "267",
                        "size": "147988420",
                        "permissions": "-rw-"
                    }
                },
                "bytes_total": "2142715904",
                "bytes_free": "1989595136"
            },
            "dir": "flash0:/"
        }
    }

    golden_output_iosv = {'execute.return_value': '''\
        Directory of flash0:/

            1  drw-           0  Jan 30 2013 00:00:00 +00:00  boot
          264  drw-           0  Oct 14 2013 00:00:00 +00:00  config
          267  -rw-   147988420  Mar 29 2017 00:00:00 +00:00  vios-adventerprisek9-m
          268  -rw-      524288  Oct 17 2018 18:57:10 +00:00  nvram
          269  -rw-         119  Oct 17 2018 18:57:18 +00:00  e1000_bia.txt

        2142715904 bytes total (1989595136 bytes free)
    '''}

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        dir_obj = Dir(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsered_output = dir_obj.parse()

    def test_semi_empty(self):
        self.dev1 = Mock(**self.semi_empty_output)
        dir_obj = Dir(device=self.dev1)
        with self.assertRaises(SchemaMissingKeyError):
            parsed_output = dir_obj.parse()

    def test_golden_iosv(self):
        self.maxDiff = None
        self.dev_iosv = Mock(**self.golden_output_iosv)
        dir_obj = Dir(device=self.dev_iosv)
        parsed_output = dir_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_iosv)


class test_show_redundancy(unittest.TestCase):
    dev1 = Device(name='empty')
    dev_iosv = Device(name='iosv')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output_iosv = {
        "red_sys_info": {
            "last_switchover_reason": "unsupported",
            "maint_mode": "Disabled",
            "switchovers_system_experienced": "0",
            "available_system_uptime": "0 minutes",
            "communications": "Down",
            "hw_mode": "Simplex",
            "communications_reason": "Failure",
            "standby_failures": "0"
        },
        "slot": {
            "slot 0": {
                "image_ver": "Cisco IOS Software, IOSv Software (VIOS-ADVENTERPRISEK9-M), Version 15.6(3)M2, RELEASE SOFTWARE (fc2)",
                "uptime_in_curr_state": "1 day, 16 hours, 42 minutes",
                "config_register": "0x0",
                "curr_sw_state": "ACTIVE"
            }
        }
    }

    golden_output_iosv = {'execute.return_value': '''\
        Redundant System Information :
        ------------------------------
               Available system uptime = 0 minutes
        Switchovers system experienced = 0
                      Standby failures = 0
                Last switchover reason = unsupported

                         Hardware Mode = Simplex
                      Maintenance Mode = Disabled
                        Communications = Down      Reason: Failure

        Current Processor Information :
        -------------------------------
                       Active Location = slot 0
                Current Software state = ACTIVE
               Uptime in current state = 1 day, 16 hours, 42 minutes
                         Image Version = Cisco IOS Software, IOSv Software (VIOS-ADVENTERPRISEK9-M), Version 15.6(3)M2, RELEASE SOFTWARE (fc2)
        Technical Support: http://www.cisco.com/techsupport
        Copyright (c) 1986-2017 by Cisco Systems, Inc.
        Compiled Wed 29-Mar-17 14:05 by prod_rel_team
                Configuration register = 0x0

        Peer (slot: 0) information is not available because it is in 'DISABLED' state
    '''}

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        redundancy_obj = ShowRedundancy(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = redundancy_obj.parse()

    def test_golden_iosv(self):
        self.maxDiff = None
        self.dev_iosv = Mock(**self.golden_output_iosv)
        redundancy_obj = ShowRedundancy(device=self.dev_iosv)
        parsed_output = redundancy_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_iosv)


class TestShowInventory(unittest.TestCase):
    dev1 = Device(name='empty')
    dev_iosv = Device(name='iosv')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output_iosv = {
        'main': {
            'chassis': {
                'IOSv': {
                    'descr': 'IOSv chassis, Hw Serial#: 9K66Z7TOKAACDEQA24N7S, Hw Revision: 1.0',
                    'name': 'IOSv',
                    'pid': 'IOSv',
                    'sn': '9K66Z7TOKAACDEQA24N7S',
                    'vid': '1.0',
                },
            },
        },
    }

    golden_output_iosv = {'execute.return_value': '''\
        NAME: "IOSv", DESCR: "IOSv chassis, Hw Serial#: 9K66Z7TOKAACDEQA24N7S, Hw Revision: 1.0"
        PID: IOSv              , VID: 1.0, SN: 9K66Z7TOKAACDEQA24N7S
    '''}

    golden_parsed_output_2 = {
        "main": {
            "chassis": {
                "WS-C6504-E": {
                    "name": "WS-C6504-E",
                    "descr": "Cisco Systems Cisco 6500 4-slot Chassis System",
                    "pid": "WS-C6504-E",
                    "vid": "V01",
                    "sn": "FXS1712Q1R8",
                }
            }
        },
        "slot": {
            "CLK-7600 1": {
                "other": {
                    "CLK-7600 1": {
                        "name": "CLK-7600 1",
                        "descr": "OSR-7600 Clock FRU 1",
                        "pid": "CLK-7600",
                        "vid": "",
                        "sn": "FXS170802GL",
                    }
                }
            },
            "CLK-7600 2": {
                "other": {
                    "CLK-7600 2": {
                        "name": "CLK-7600 2",
                        "descr": "OSR-7600 Clock FRU 2",
                        "pid": "CLK-7600",
                        "vid": "",
                        "sn": "FXS170802GL",
                    }
                }
            },
            "FAN-MOD-4HS 1": {
                "other": {
                    "FAN-MOD-4HS 1": {
                        "name": "FAN-MOD-4HS 1",
                        "descr": "High Speed Fan Module for CISCO7604 1",
                        "pid": "FAN-MOD-4HS",
                        "vid": "V01",
                        "sn": "DCH170900PF",
                    }
                }
            },
            "PS 1 PWR-2700-AC/4": {
                "other": {
                    "PS 1 PWR-2700-AC/4": {
                        "name": "PS 1 PWR-2700-AC/4",
                        "descr": "2700W AC power supply for CISCO7604 1",
                        "pid": "PWR-2700-AC/4",
                        "vid": "V03",
                        "sn": "APS1707008Y",
                    }
                }
            },
            "PS 2 PWR-2700-AC/4": {
                "other": {
                    "PS 2 PWR-2700-AC/4": {
                        "name": "PS 2 PWR-2700-AC/4",
                        "descr": "2700W AC power supply for CISCO7604 2",
                        "pid": "PWR-2700-AC/4",
                        "vid": "V03",
                        "sn": "APS17070093",
                    }
                }
            },
            "1": {
                "rp": {
                    "VS-SUP2T-10G": {
                        "name": "1",
                        "descr": "VS-SUP2T-10G 5 ports Supervisor Engine 2T 10GE w/ CTS Rev. 1.5",
                        "pid": "VS-SUP2T-10G",
                        "vid": "V05",
                        "sn": "SAL17152N0F",
                        "subslot": {
                            "0": {
                                "VS-F6K-MSFC5": {
                                    "descr": "VS-F6K-MSFC5 CPU Daughterboard Rev. 2.0",
                                    "name": "msfc sub-module of 1",
                                    "pid": "VS-F6K-MSFC5",
                                    "sn": "SAL17142D06",
                                    "vid": "",
                                },
                                "VS-F6K-PFC4": {
                                    "descr": "VS-F6K-PFC4 Policy Feature Card 4 Rev. 2.0",
                                    "name": "VS-F6K-PFC4 Policy Feature Card 4 EARL sub-module of 1",
                                    "pid": "VS-F6K-PFC4",
                                    "sn": "SAL17163901",
                                    "vid": "V03",
                                },
                            },
                            "4": {
                                "X2-10GB-SR": {
                                    "descr": "X2 Transceiver 10Gbase-SR Te1/4",
                                    "name": "Transceiver Te1/4",
                                    "pid": "X2-10GB-SR",
                                    "sn": "ONT170202T1",
                                    "vid": "V06 ",
                                }
                            },
                            "5": {
                                "X2-10GB-SR": {
                                    "descr": "X2 Transceiver 10Gbase-SR Te1/5",
                                    "name": "Transceiver Te1/5",
                                    "pid": "X2-10GB-SR",
                                    "sn": "ONT1702033D",
                                    "vid": "V06 ",
                                }
                            },
                        },
                    }
                }
            },
            "2": {
                "lc": {
                    "WS-X6816-10GE": {
                        "name": "2",
                        "descr": "WS-X6816-10GE CEF720 16 port 10GE Rev. 2.0",
                        "pid": "WS-X6816-10GE",
                        "vid": "V02",
                        "sn": "SAL17152QB3",
                        "subslot": {
                            "0": {
                                "WS-F6K-DFC4-E": {
                                    "descr": "WS-F6K-DFC4-E Distributed Forwarding Card 4 Rev. 1.2",
                                    "name": "WS-F6K-DFC4-E Distributed Forwarding Card 4 EARL sub-module of 2",
                                    "pid": "WS-F6K-DFC4-E",
                                    "sn": "SAL171846RF",
                                    "vid": "V02",
                                }
                            },
                            "1": {
                                "X2-10GB-SR": {
                                    "descr": "X2 Transceiver 10Gbase-SR Te2/1",
                                    "name": "Transceiver Te2/1",
                                    "pid": "X2-10GB-SR",
                                    "sn": "ONT17020338",
                                    "vid": "V06 ",
                                }
                            },
                            "2": {
                                "X2-10GB-SR": {
                                    "descr": "X2 Transceiver 10Gbase-SR Te2/2",
                                    "name": "Transceiver Te2/2",
                                    "pid": "X2-10GB-SR",
                                    "sn": "ONT1702020H",
                                    "vid": "V06 ",
                                }
                            },
                            "3": {
                                "X2-10GB-SR": {
                                    "descr": "X2 Transceiver 10Gbase-SR Te2/3",
                                    "name": "Transceiver Te2/3",
                                    "pid": "X2-10GB-SR",
                                    "sn": "ONT170202UU",
                                    "vid": "V06 ",
                                }
                            },
                            "4": {
                                "X2-10GB-SR": {
                                    "descr": "X2 Transceiver 10Gbase-SR Te2/4",
                                    "name": "Transceiver Te2/4",
                                    "pid": "X2-10GB-SR",
                                    "sn": "ONT170202T5",
                                    "vid": "V06 ",
                                }
                            },
                            "5": {
                                "X2-10GB-SR": {
                                    "descr": "X2 Transceiver 10Gbase-SR Te2/5",
                                    "name": "Transceiver Te2/5",
                                    "pid": "X2-10GB-SR",
                                    "sn": "AGA1515XZE2",
                                    "vid": "V05 ",
                                }
                            },
                            "6": {
                                "X2-10GB-SR": {
                                    "descr": "X2 Transceiver 10Gbase-SR Te2/6",
                                    "name": "Transceiver Te2/6",
                                    "pid": "X2-10GB-SR",
                                    "sn": "FNS153920YJ",
                                    "vid": "V06 ",
                                }
                            },
                            "16": {
                                "X2-10GB-SR": {
                                    "descr": "X2 Transceiver 10Gbase-SR Te2/16",
                                    "name": "Transceiver Te2/16",
                                    "pid": "X2-10GB-SR",
                                    "sn": "ONT170201TT",
                                    "vid": "V06 ",
                                }
                            },
                        },
                    }
                }
            },
            "3": {
                "lc": {
                    "WS-X6824-SFP": {
                        "name": "3",
                        "descr": "WS-X6824-SFP CEF720 24 port 1000mb SFP Rev. 1.0",
                        "pid": "WS-X6824-SFP",
                        "vid": "V01",
                        "sn": "SAL17152EG9",
                        "subslot": {
                            "0": {
                                "WS-F6K-DFC4-A": {
                                    "descr": "WS-F6K-DFC4-A Distributed Forwarding Card 4 Rev. 1.0",
                                    "name": "WS-F6K-DFC4-A Distributed Forwarding Card 4 EARL sub-module of 3",
                                    "pid": "WS-F6K-DFC4-A",
                                    "sn": "SAL171848KL",
                                    "vid": "V04",
                                }
                            }
                        },
                    }
                }
            },
            "4": {
                "lc": {
                    "WS-X6748-GE-TX": {
                        "name": "4",
                        "descr": "WS-X6748-GE-TX CEF720 48 port 10/100/1000mb Ethernet Rev. 3.4",
                        "pid": "WS-X6748-GE-TX",
                        "vid": "V04",
                        "sn": "SAL14017TWF",
                        "subslot": {
                            "0": {
                                "WS-F6700-CFC": {
                                    "descr": "WS-F6700-CFC Centralized Forwarding Card Rev. 4.1",
                                    "name": "WS-F6700-CFC Centralized Forwarding Card EARL sub-module of 4",
                                    "pid": "WS-F6700-CFC",
                                    "sn": "SAL13516QS8",
                                    "vid": "V06",
                                }
                            }
                        },
                    }
                }
            },
        },
    }

    golden_output_2 = {'execute.return_value': '''
        NAME: "WS-C6504-E", DESCR: "Cisco Systems Cisco 6500 4-slot Chassis System"
        PID: WS-C6504-E        ,                     VID: V01, SN: FXS1712Q1R8

        NAME: "CLK-7600 1", DESCR: "OSR-7600 Clock FRU 1"
        PID: CLK-7600          ,                     VID:    , SN: FXS170802GL

        NAME: "CLK-7600 2", DESCR: "OSR-7600 Clock FRU 2"
        PID: CLK-7600          ,                     VID:    , SN: FXS170802GL

        NAME: "1", DESCR: "VS-SUP2T-10G 5 ports Supervisor Engine 2T 10GE w/ CTS Rev. 1.5"
        PID: VS-SUP2T-10G      ,                     VID: V05, SN: SAL17152N0F

        NAME: "msfc sub-module of 1", DESCR: "VS-F6K-MSFC5 CPU Daughterboard Rev. 2.0"
        PID: VS-F6K-MSFC5      ,                     VID:    , SN: SAL17142D06

        NAME: "VS-F6K-PFC4 Policy Feature Card 4 EARL sub-module of 1", DESCR: "VS-F6K-PFC4 Policy Feature Card 4 Rev. 2.0"
        PID: VS-F6K-PFC4       ,                     VID: V03, SN: SAL17163901

        NAME: "Transceiver Te1/4", DESCR: "X2 Transceiver 10Gbase-SR Te1/4"
        PID: X2-10GB-SR        ,                     VID: V06 , SN: ONT170202T1

        NAME: "Transceiver Te1/5", DESCR: "X2 Transceiver 10Gbase-SR Te1/5"
        PID: X2-10GB-SR        ,                     VID: V06 , SN: ONT1702033D

        NAME: "2", DESCR: "WS-X6816-10GE CEF720 16 port 10GE Rev. 2.0"
        PID: WS-X6816-10GE     ,                     VID: V02, SN: SAL17152QB3

        NAME: "WS-F6K-DFC4-E Distributed Forwarding Card 4 EARL sub-module of 2", DESCR: "WS-F6K-DFC4-E Distributed Forwarding Card 4 Rev. 1.2"
        PID: WS-F6K-DFC4-E     ,                     VID: V02, SN: SAL171846RF

        NAME: "Transceiver Te2/1", DESCR: "X2 Transceiver 10Gbase-SR Te2/1"
        PID: X2-10GB-SR        ,                     VID: V06 , SN: ONT17020338

        NAME: "Transceiver Te2/2", DESCR: "X2 Transceiver 10Gbase-SR Te2/2"
        PID: X2-10GB-SR        ,                     VID: V06 , SN: ONT1702020H

        NAME: "Transceiver Te2/3", DESCR: "X2 Transceiver 10Gbase-SR Te2/3"
        PID: X2-10GB-SR        ,                     VID: V06 , SN: ONT170202UU

        NAME: "Transceiver Te2/4", DESCR: "X2 Transceiver 10Gbase-SR Te2/4"
        PID: X2-10GB-SR        ,                     VID: V06 , SN: ONT170202T5

        NAME: "Transceiver Te2/5", DESCR: "X2 Transceiver 10Gbase-SR Te2/5"
        PID: X2-10GB-SR        ,                     VID: V05 , SN: AGA1515XZE2

        NAME: "Transceiver Te2/6", DESCR: "X2 Transceiver 10Gbase-SR Te2/6"
        PID: X2-10GB-SR        ,                     VID: V06 , SN: FNS153920YJ

        NAME: "Transceiver Te2/16", DESCR: "X2 Transceiver 10Gbase-SR Te2/16"
        PID: X2-10GB-SR        ,                     VID: V06 , SN: ONT170201TT

        NAME: "3", DESCR: "WS-X6824-SFP CEF720 24 port 1000mb SFP Rev. 1.0"
        PID: WS-X6824-SFP      ,                     VID: V01, SN: SAL17152EG9

        NAME: "WS-F6K-DFC4-A Distributed Forwarding Card 4 EARL sub-module of 3", DESCR: "WS-F6K-DFC4-A Distributed Forwarding Card 4 Rev. 1.0"
        PID: WS-F6K-DFC4-A     ,                     VID: V04, SN: SAL171848KL

        NAME: "4", DESCR: "WS-X6748-GE-TX CEF720 48 port 10/100/1000mb Ethernet Rev. 3.4"
        PID: WS-X6748-GE-TX    ,                     VID: V04, SN: SAL14017TWF

        NAME: "WS-F6700-CFC Centralized Forwarding Card EARL sub-module of 4", DESCR: "WS-F6700-CFC Centralized Forwarding Card Rev. 4.1"
        PID: WS-F6700-CFC      ,                     VID: V06, SN: SAL13516QS8

        NAME: "FAN-MOD-4HS 1", DESCR: "High Speed Fan Module for CISCO7604 1"
        PID: FAN-MOD-4HS       ,                     VID: V01, SN: DCH170900PF

        NAME: "PS 1 PWR-2700-AC/4", DESCR: "2700W AC power supply for CISCO7604 1"
        PID: PWR-2700-AC/4     ,                     VID: V03, SN: APS1707008Y

        NAME: "PS 2 PWR-2700-AC/4", DESCR: "2700W AC power supply for CISCO7604 2"
        PID: PWR-2700-AC/4     ,                     VID: V03, SN: APS17070093
    '''}

    golden_parsed_output_3 = {
        "main": {
            "chassis": {
                "WS-C6503-E": {
                    "name": "WS-C6503-E",
                    "descr": "Cisco Systems Catalyst 6500 3-slot Chassis System",
                    "pid": "WS-C6503-E",
                    "vid": "V03",
                    "sn": "FXS1821Q2H9",
                }
            }
        },
        "slot": {
            "CLK-7600 1": {
                "other": {
                    "CLK-7600 1": {
                        "name": "CLK-7600 1",
                        "descr": "OSR-7600 Clock FRU 1",
                        "pid": "CLK-7600",
                        "vid": "",
                        "sn": "FXS181101V4",
                    }
                }
            },
            "CLK-7600 2": {
                "other": {
                    "CLK-7600 2": {
                        "name": "CLK-7600 2",
                        "descr": "OSR-7600 Clock FRU 2",
                        "pid": "CLK-7600",
                        "vid": "",
                        "sn": "FXS181101V4",
                    }
                }
            },
            "1": {
                "rp": {
                    "WS-SUP720-3BXL": {
                        "name": "1",
                        "descr": "WS-SUP720-3BXL 2 ports Supervisor Engine 720 Rev. 5.6",
                        "pid": "WS-SUP720-3BXL",
                        "vid": "V05",
                        "sn": "SAL11434P2C",
                        "subslot": {
                            "0": {
                                "WS-SUP720": {
                                    "descr": "WS-SUP720 MSFC3 Daughterboard Rev. 3.1",
                                    "name": "msfc sub-module of 1",
                                    "pid": "WS-SUP720",
                                    "sn": "SAL11434N9G",
                                    "vid": "",
                                },
                                "WS-F6K-PFC3BXL": {
                                    "descr": "WS-F6K-PFC3BXL Policy Feature Card 3 Rev. 1.8",
                                    "name": "switching engine sub-module of 1",
                                    "pid": "WS-F6K-PFC3BXL",
                                    "sn": "SAL11434LYG",
                                    "vid": "V01",
                                },
                            }
                        },
                    }
                }
            },
            "2": {
                "lc": {
                    "WS-X6748-GE-TX": {
                        "name": "2",
                        "descr": "WS-X6748-GE-TX CEF720 48 port 10/100/1000mb Ethernet Rev. 2.6",
                        "pid": "WS-X6748-GE-TX",
                        "vid": "V02",
                        "sn": "SAL1128UPQ9",
                        "subslot": {
                            "0": {
                                "WS-F6700-DFC3CXL": {
                                    "descr": "WS-F6700-DFC3CXL Distributed Forwarding Card 3 Rev. 1.1",
                                    "name": "switching engine sub-module of 2",
                                    "pid": "WS-F6700-DFC3CXL",
                                    "sn": "SAL1214LAG5",
                                    "vid": "V01",
                                }
                            }
                        },
                    }
                }
            },
            "WS-C6503-E-FAN 1": {
                "other": {
                    "WS-C6503-E-FAN 1": {
                        "name": "WS-C6503-E-FAN 1",
                        "descr": "Enhanced 3-slot Fan Tray 1",
                        "pid": "WS-C6503-E-FAN",
                        "vid": "V02",
                        "sn": "DCH183500KW",
                    }
                }
            },
            "PS 1 PWR-1400-AC": {
                "other": {
                    "PS 1 PWR-1400-AC": {
                        "name": "PS 1 PWR-1400-AC",
                        "descr": "AC power supply, 1400 watt 1",
                        "pid": "PWR-1400-AC",
                        "vid": "V01",
                        "sn": "ABC0830J127",
                    }
                }
            },
        },
    }

    golden_output_3 = {'execute.return_value': '''
        # show inventory
        NAME: "WS-C6503-E", DESCR: "Cisco Systems Catalyst 6500 3-slot Chassis System"
        PID: WS-C6503-E        , VID: V03, SN: FXS1821Q2H9

        NAME: "CLK-7600 1", DESCR: "OSR-7600 Clock FRU 1"
        PID: CLK-7600          , VID:    , SN: FXS181101V4

        NAME: "CLK-7600 2", DESCR: "OSR-7600 Clock FRU 2"
        PID: CLK-7600          , VID:    , SN: FXS181101V4

        NAME: "1", DESCR: "WS-SUP720-3BXL 2 ports Supervisor Engine 720 Rev. 5.6"
        PID: WS-SUP720-3BXL    , VID: V05, SN: SAL11434P2C

        NAME: "msfc sub-module of 1", DESCR: "WS-SUP720 MSFC3 Daughterboard Rev. 3.1"
        PID: WS-SUP720         , VID:    , SN: SAL11434N9G

        NAME: "switching engine sub-module of 1", DESCR: "WS-F6K-PFC3BXL Policy Feature Card 3 Rev. 1.8"
        PID: WS-F6K-PFC3BXL    , VID: V01, SN: SAL11434LYG

        NAME: "2", DESCR: "WS-X6748-GE-TX CEF720 48 port 10/100/1000mb Ethernet Rev. 2.6"
        PID: WS-X6748-GE-TX    , VID: V02, SN: SAL1128UPQ9

        NAME: "switching engine sub-module of 2", DESCR: "WS-F6700-DFC3CXL Distributed Forwarding Card 3 Rev. 1.1"
        PID: WS-F6700-DFC3CXL  , VID: V01, SN: SAL1214LAG5

        NAME: "WS-C6503-E-FAN 1", DESCR: "Enhanced 3-slot Fan Tray 1"
        PID: WS-C6503-E-FAN    , VID: V02, SN: DCH183500KW

        NAME: "PS 1 PWR-1400-AC", DESCR: "AC power supply, 1400 watt 1"
        PID: PWR-1400-AC       , VID: V01, SN: ABC0830J127
    '''}

    golden_output_4 = {'execute.return_value': '''
    NAME: "1", DESCR: "WS-C8888X-88"
    PID: WS-C0123X-45T-S   , VID: V00  , SN: FDO123R12W
    
    NAME: "Switch 1 - Power Supply 1", DESCR: "ABC Power Supply"
    PID: C3KX-PWR-350WAC   , VID: V01D , SN: DTN1504L0E9
    
    NAME: "TenGigabitEthernet1/1/1", DESCR: "SFP-10GBase-SR"
    PID: SFP-10G-SR          , VID: V03  , SN: SPC1519005V

    NAME: "2", DESCR: "WS-C3210X-48"
    PID: WS-C3210X-48T-S   , VID: V02  , SN: FD5678Z90P
    
    NAME: "Switch 2 - Power Supply 1", DESCR: "BCA Power Supply"
    PID: C3KX-PWR-007CBA   , VID: V01L , SN: LTP13579L3R
    
    
    NAME: "TenGigabitEthernet2/1/1", DESCR: "SFP-10GBase-LR"
    PID: SFP-10G-LR          , VID: V02  , SN: ONT182746GZ
    
    NAME: "1", DESCR: "WS-C1010XR-48FPS-I"
    PID: WS-C1010XR-48FPS-I, VID: V05  , SN: FD2043B0K3
    
    NAME: "Switch 1 - Power Supply 1", DESCR: "LLL Power Supply"
    PID: PWR-C2-2929WAC    , VID: V02L , SN: LIT03728KKK
    
    NAME: "Switch 1 - FlexStackPlus Module", DESCR: "Stacking Module"
    PID: C1010X-STACK      , VID: V02  , SN: FD232323XXZ
    
    NAME: "GigabitEthernet1/0/49", DESCR: "1000BaseSX SFP"
    PID: GLC-SX-MMD          , VID: V01  , SN: ACW102938VS  
    '''}

    golden_parsed_output_4 = {
        'slot': {
            '1': {
                'rp': {
                    'WS-C0123X-45T-S': {
                        'descr': 'WS-C8888X-88',
                        'name': '1',
                        'pid': 'WS-C0123X-45T-S',
                        'sn': 'FDO123R12W',
                        'subslot': {
                            '1': {
                                'C3KX-PWR-350WAC': {
                                    'descr': 'ABC Power Supply',
                                    'name': 'Switch 1 - Power Supply 1',
                                    'pid': 'C3KX-PWR-350WAC',
                                    'sn': 'DTN1504L0E9',
                                    'vid': 'V01D ',
                                },
                            },
                            '1/1/1': {
                                'SFP-10G-SR': {
                                    'descr': 'SFP-10GBase-SR',
                                    'name': 'TenGigabitEthernet1/1/1',
                                    'pid': 'SFP-10G-SR',
                                    'sn': 'SPC1519005V',
                                    'vid': 'V03  ',
                                },
                            },
                        },
                        'vid': 'V00  ',
                    },
                    'WS-C1010XR-48FPS-I': {
                        'descr': 'WS-C1010XR-48FPS-I',
                        'name': '1',
                        'pid': 'WS-C1010XR-48FPS-I',
                        'sn': 'FD2043B0K3',
                        'subslot': {
                            '1': {
                                'C1010X-STACK': {
                                    'descr': 'Stacking Module',
                                    'name': 'Switch 1 - FlexStackPlus Module',
                                    'pid': 'C1010X-STACK',
                                    'sn': 'FD232323XXZ',
                                    'vid': 'V02  ',
                                },
                                'PWR-C2-2929WAC': {
                                    'descr': 'LLL Power Supply',
                                    'name': 'Switch 1 - Power Supply 1',
                                    'pid': 'PWR-C2-2929WAC',
                                    'sn': 'LIT03728KKK',
                                    'vid': 'V02L ',
                                },
                            },
                            '1/0/49': {
                                'GLC-SX-MMD': {
                                    'descr': '1000BaseSX SFP',
                                    'name': 'GigabitEthernet1/0/49',
                                    'pid': 'GLC-SX-MMD',
                                    'sn': 'ACW102938VS',
                                    'vid': 'V01  ',
                                },
                            },
                        },
                        'vid': 'V05  ',
                    },
                },
            },
            '2': {
                'rp': {
                    'WS-C3210X-48T-S': {
                        'descr': 'WS-C3210X-48',
                        'name': '2',
                        'pid': 'WS-C3210X-48T-S',
                        'sn': 'FD5678Z90P',
                        'subslot': {
                            '2': {
                                'C3KX-PWR-007CBA': {
                                    'descr': 'BCA Power Supply',
                                    'name': 'Switch 2 - Power Supply 1',
                                    'pid': 'C3KX-PWR-007CBA',
                                    'sn': 'LTP13579L3R',
                                    'vid': 'V01L ',
                                },
                            },
                            '2/1/1': {
                                'SFP-10G-LR': {
                                    'descr': 'SFP-10GBase-LR',
                                    'name': 'TenGigabitEthernet2/1/1',
                                    'pid': 'SFP-10G-LR',
                                    'sn': 'ONT182746GZ',
                                    'vid': 'V02  ',
                                },
                            },
                        },
                        'vid': 'V02  ',
                    },
                },
            },
        },
    }

    golden_output_5 = {'execute.return_value': '''
    best-c3945-IOS3#show inventory
    NAME: "CISCO3945-CHASSIS", DESCR: "CISCO3945-CHASSIS"
    PID: CISCO3945-CHASSIS , VID: V05 , SN: FGL161010K8
    
    NAME: "Cisco Services Performance Engine 150 for Cisco 3900 ISR on Slot 0", DESCR: "Cisco Services Performance Engine 150 for Cisco 3900 ISR"
    PID: C3900-SPE150/K9   , VID: V05 , SN: FOC16050QP6
    
    NAME: "Two-Port Fast Ethernet High Speed WAN Interface Card on Slot 0 SubSlot 3", DESCR: "Two-Port Fast Ethernet High Speed WAN Interface Card"
    PID: HWIC-2FE          , VID: V02 , SN: FOC16062824
    
    NAME: "C3900 AC Power Supply 1", DESCR: "C3900 AC Power Supply 1"
    PID: PWR-3900-AC       , VID: V03 , SN: QCS1604P0BT
    '''}
    golden_parsed_output_5 = {
        'main': {
            'chassis': {
                'CISCO3945-CHASSIS': {
                    'descr': 'CISCO3945-CHASSIS',
                    'name': 'CISCO3945-CHASSIS',
                    'pid': 'CISCO3945-CHASSIS',
                    'sn': 'FGL161010K8',
                    'vid': 'V05 ',
                },
            },
        },
        'slot': {
            '0': {
                'rp': {
                    'C3900-SPE150/K9': {
                        'descr': 'Cisco Services Performance Engine 150 for Cisco 3900 ISR',
                        'name': 'Cisco Services Performance Engine 150 for Cisco 3900 ISR on Slot 0',
                        'pid': 'C3900-SPE150/K9',
                        'sn': 'FOC16050QP6',
                        'subslot': {
                            '3': {
                                'HWIC-2FE': {
                                    'descr': 'Two-Port Fast Ethernet High Speed WAN Interface Card',
                                    'name': 'Two-Port Fast Ethernet High Speed WAN Interface Card on Slot 0 SubSlot 3',
                                    'pid': 'HWIC-2FE',
                                    'sn': 'FOC16062824',
                                    'vid': 'V02 ',
                                },
                            },
                        },
                        'vid': 'V05 ',
                    },
                },
            },
            'C3900 AC Power Supply 1': {
                'other': {
                    'C3900 AC Power Supply 1': {
                        'descr': 'C3900 AC Power Supply 1',
                        'name': 'C3900 AC Power Supply 1',
                        'pid': 'PWR-3900-AC',
                        'sn': 'QCS1604P0BT',
                        'vid': 'V03 ',
                    },
                },
            },
        },
    }

    golden_output_6 = {'execute.return_value': '''
    NAME: "1", DESCR: "SM-ES2-16-P"
    PID: SM-ES2-16-P       , VID:      , SN: FOC09876NP3
    '''}
    golden_parsed_output_6 = {
        'slot': {
            '1': {
                'lc': {
                    'SM-ES2-16-P': {
                        'descr': 'SM-ES2-16-P',
                        'name': '1',
                        'pid': 'SM-ES2-16-P',
                        'sn': 'FOC09876NP3',
                        'vid': '',
                    },
                },
            },
        },
    }

    golden_output_7 = {'execute.return_value': '''
    NAME: "2821 chassis", DESCR: "2821 chassis"
    PID: CISCO2821         , VID: V07 , SN: FTX1234AMWT
    
    NAME: "VWIC2-2MFT-T1/E1 - 2-Port RJ-48 Multiflex Trunk - T1/E1 on Slot 0 SubSlot 0", DESCR: "VWIC2-2MFT-T1/E1 - 2-Port RJ-48 Multiflex Trunk - T1/E1"
    PID: VWIC2-2MFT-T1/E1  , VID: V01 , SN: FOC98675U0D
    
    NAME: "VWIC2-2MFT-T1/E1 - 2-Port RJ-48 Multiflex Trunk - T1/E1 on Slot 0 SubSlot 1", DESCR: "VWIC2-2MFT-T1/E1 - 2-Port RJ-48 Multiflex Trunk - T1/E1"
    PID: VWIC2-2MFT-T1/E1  , VID: V01 , SN: FOC98675W3E
    
    NAME: "Virtual Private Network (VPN) Module on Slot 0", DESCR: "Encryption AIM Element"
    PID: AIM-VPN/SSL-2     , VID: V01, SN: FOC2837465E
    '''}

    golden_parsed_output_7 = {
        'main': {
            'chassis': {
                'CISCO2821': {
                    'descr': '2821 chassis',
                    'name': '2821 chassis',
                    'pid': 'CISCO2821',
                    'sn': 'FTX1234AMWT',
                    'vid': 'V07 ',
                },
            },
        },
        'slot': {
            '0': {
                'other': {
                    'AIM-VPN/SSL-2': {
                        'descr': 'Encryption AIM Element',
                        'name': 'Virtual Private Network (VPN) Module on Slot 0',
                        'pid': 'AIM-VPN/SSL-2',
                        'sn': 'FOC2837465E',
                        'vid': 'V01',
                        'subslot': {
                            '0': {
                                'VWIC2-2MFT-T1/E1': {
                                    'descr': 'VWIC2-2MFT-T1/E1 - 2-Port RJ-48 Multiflex Trunk - T1/E1',
                                    'name': 'VWIC2-2MFT-T1/E1 - 2-Port RJ-48 Multiflex Trunk - T1/E1 on Slot 0 SubSlot 0',
                                    'pid': 'VWIC2-2MFT-T1/E1',
                                    'sn': 'FOC98675U0D',
                                    'vid': 'V01 ',
                                },
                            },
                            '1': {
                                'VWIC2-2MFT-T1/E1': {
                                    'descr': 'VWIC2-2MFT-T1/E1 - 2-Port RJ-48 Multiflex Trunk - T1/E1',
                                    'name': 'VWIC2-2MFT-T1/E1 - 2-Port RJ-48 Multiflex Trunk - T1/E1 on Slot 0 SubSlot 1',
                                    'pid': 'VWIC2-2MFT-T1/E1',
                                    'sn': 'FOC98675W3E',
                                    'vid': 'V01 ',
                                },
                            },
                        },
                    },
                },
            },
        },
    }

    golden_output_8 = {'execute.return_value': '''
    NAME: "3825 chassis", DESCR: "3825 chassis"
    PID: CISCO3825         , VID: V05 , SN: FTX7908A3RQ
    
    NAME: "VWIC2-2MFT-T1/E1 - 2-Port RJ-48 Multiflex Trunk - T1/E1 on Slot 0 SubSlot 0", DESCR: "VWIC2-2MFT-T1/E1 - 2-Port RJ-48 Multiflex Trunk - T1/E1"
    PID: VWIC2-2MFT-T1/E1  , VID: V01 , SN: FOC65428K9F
    
    NAME: "Wan Interface Card BRI U (2091, 3086) on Slot 0 SubSlot 1", DESCR: "Wan Interface Card BRI U (2091, 3086)"
    PID: WIC-1B-U-V2       , VID: V01, SN: 10293847   
    
    NAME: "PVDMII DSP SIMM with four DSPs on Slot 0 SubSlot 4", DESCR: "PVDMII DSP SIMM with four DSPs"
    PID: PVDM2-64          , VID: V01 , SN: FOC63358WSI
    
    NAME: "High Density Voice Module - 8FXS/DID on Slot 1", DESCR: "High Density Voice Module - 8FXS/DID"
    PID: EVM-HD-8FXS/DID   , VID: V04 , SN: FOC65798TG8
    
    NAME: "Six port FXO voice interface daughtercard on Slot 1 SubSlot 1", DESCR: "Six port FXO voice interface daughtercard"
    PID: EM-HDA-6FXO       , VID: V03 , SN: FOC85389QXB
    '''}

    golden_parsed_output_8 = {
        'main': {
            'chassis': {
                'CISCO3825': {
                    'descr': '3825 chassis',
                    'name': '3825 chassis',
                    'pid': 'CISCO3825',
                    'sn': 'FTX7908A3RQ',
                    'vid': 'V05 ',
                },
            },
        },
        'slot': {
            '0': {
                'rp': {
                    'CISCO3825': {
                        'subslot': {
                            '0': {
                                'VWIC2-2MFT-T1/E1': {
                                    'descr': 'VWIC2-2MFT-T1/E1 - 2-Port RJ-48 Multiflex Trunk - T1/E1',
                                    'name': 'VWIC2-2MFT-T1/E1 - 2-Port RJ-48 Multiflex Trunk - T1/E1 on Slot 0 SubSlot 0',
                                    'pid': 'VWIC2-2MFT-T1/E1',
                                    'sn': 'FOC65428K9F',
                                    'vid': 'V01 ',
                                },
                            },
                            '1': {
                                'WIC-1B-U-V2': {
                                    'descr': 'Wan Interface Card BRI U (2091, 3086)',
                                    'name': 'Wan Interface Card BRI U (2091, 3086) on Slot 0 SubSlot 1',
                                    'pid': 'WIC-1B-U-V2',
                                    'sn': '10293847',
                                    'vid': 'V01',
                                },
                            },
                            '4': {
                                'PVDM2-64': {
                                    'descr': 'PVDMII DSP SIMM with four DSPs',
                                    'name': 'PVDMII DSP SIMM with four DSPs on Slot 0 SubSlot 4',
                                    'pid': 'PVDM2-64',
                                    'sn': 'FOC63358WSI',
                                    'vid': 'V01 ',
                                },
                            },
                        },
                    },
                },
            },
            '1': {
                'other': {
                    'EVM-HD-8FXS/DID': {
                        'descr': 'High Density Voice Module - 8FXS/DID',
                        'name': 'High Density Voice Module - 8FXS/DID on Slot 1',
                        'pid': 'EVM-HD-8FXS/DID',
                        'sn': 'FOC65798TG8',
                        'subslot': {
                            '1': {
                                'EM-HDA-6FXO': {
                                    'descr': 'Six port FXO voice interface daughtercard',
                                    'name': 'Six port FXO voice interface daughtercard on Slot 1 SubSlot 1',
                                    'pid': 'EM-HDA-6FXO',
                                    'sn': 'FOC85389QXB',
                                    'vid': 'V03 ',
                                },
                            },
                        },
                        'vid': 'V04 ',
                    },
                },
            },
        },
    }

    golden_output_9 = {'execute.return_value': '''
    NAME: "3845 chassis", DESCR: "3845 chassis"
    PID: CISCO3845         , VID: V05 , SN: FTX6666ARJ9
    
    NAME: "c3845 Motherboard with Gigabit Ethernet on Slot 0", DESCR: "c3845 Motherboard with Gigabit Ethernet"
    PID: CISCO3845-MB      , VID: V09 , SN: FOC729346GQ
    
    NAME: "Virtual Private Network (VPN) Module on Slot 0", DESCR: "Encryption AIM Element"
    PID: AIM-VPN/SSL-3     , VID: V01, SN: FOC758693YO
    
    NAME: "Clear/Subrate T3/E3 WAN on Slot 1", DESCR: "Clear/Subrate T3/E3 WAN"
    PID: NM-1T3/E3=        , VID: V01 , SN: FOC28476ADM
    
    NAME: "16 Port 10BaseT/100BaseTX EtherSwitch on Slot 2", DESCR: "16 Port 10BaseT/100BaseTX EtherSwitch"
    PID: NM-16ESW          , VID: V01 , SN: FOC135464KO
    
    NAME: "Gigabit(1000BaseT) module for EtherSwitch NM on Slot 2 SubSlot 0", DESCR: "Gigabit(1000BaseT) module for EtherSwitch NM"
    PID: GE-DCARD-ESW      , VID: V01 , SN: FOC91864MNN
    '''}

    golden_parsed_output_9 = {
        'main': {
            'chassis': {
                'CISCO3845': {
                    'descr': '3845 chassis',
                    'name': '3845 chassis',
                    'pid': 'CISCO3845',
                    'sn': 'FTX6666ARJ9',
                    'vid': 'V05 ',
                },
            },
        },
        'slot': {
            '0': {
                'lc': {
                    'CISCO3845-MB': {
                        'descr': 'c3845 Motherboard with Gigabit Ethernet',
                        'name': 'c3845 Motherboard with Gigabit Ethernet on Slot 0',
                        'pid': 'CISCO3845-MB',
                        'sn': 'FOC729346GQ',
                        'vid': 'V09 ',
                    },
                },
                'other': {
                    'AIM-VPN/SSL-3': {
                        'descr': 'Encryption AIM Element',
                        'name': 'Virtual Private Network (VPN) Module on Slot 0',
                        'pid': 'AIM-VPN/SSL-3',
                        'sn': 'FOC758693YO',
                        'vid': 'V01',
                    },

                },
            },
            '1': {
                'lc': {
                    'NM-1T3/E3=': {
                        'descr': 'Clear/Subrate T3/E3 WAN',
                        'name': 'Clear/Subrate T3/E3 WAN on Slot 1',
                        'pid': 'NM-1T3/E3=',
                        'sn': 'FOC28476ADM',
                        'vid': 'V01 ',
                    },
                },
            },
            '16': {
                'lc': {
                    'NM-16ESW': {
                        'descr': '16 Port 10BaseT/100BaseTX EtherSwitch',
                        'name': '16 Port 10BaseT/100BaseTX EtherSwitch on Slot 2',
                        'pid': 'NM-16ESW',
                        'sn': 'FOC135464KO',
                        'subslot': {
                            '0': {
                                'GE-DCARD-ESW': {
                                    'descr': 'Gigabit(1000BaseT) module for EtherSwitch NM',
                                    'name': 'Gigabit(1000BaseT) module for EtherSwitch NM on Slot 2 SubSlot 0',
                                    'pid': 'GE-DCARD-ESW',
                                    'sn': 'FOC91864MNN',
                                    'vid': 'V01 ',
                                },
                            },
                        },
                        'vid': 'V01 ',
                    },
                },
            },
        },
    }

    golden_output_10 = {'execute.return_value': '''
        show inventory
        NAME: "Switch System", DESCR: "Cisco Systems, Inc. WS-C4948 1 slot switch "
        PID:                   , VID:      , SN: FOX1638GU8L

        NAME: "Linecard(slot 1)", DESCR: "10/100/1000BaseT (RJ45), 1000BaseX (SFP) Supervisor with 48 10/100/1000BASE-T ports and 4 1000BASE-"
        PID: WS-C4948          , VID: V12  , SN: FOX1638GU8L

        NAME: "GigabitEthernet1/45", DESCR: "1000BaseSX"
        PID: Unspecified       , VID:      , SN: AGM1637LJE4

        NAME: "GigabitEthernet1/47", DESCR: "1000BaseSX"
        PID: GLC-SX-MM         , VID: V03  , SN: VB12150046 

        NAME: "Power Supply 1", DESCR: "Power Supply ( AC 300W )"
        PID: PWR-C49-300AC     , VID:      , SN: PAC15240NRN

        NAME: "Power Supply 2", DESCR: "Power Supply ( AC 300W )"
        PID: PWR-C49-300AC     , VID:      , SN: PAC15240S5T
    '''}

    golden_parsed_output_10 = {
        'main': {
            'chassis': {
                '': {
                    'descr': 'Cisco Systems, Inc. WS-C4948 1 slot switch ',
                    'name': 'Switch System',
                    'pid': '',
                    'sn': 'FOX1638GU8L',
                    'vid': '',
                },
            },
        },
        'slot': {
            '1': {
                'rp': {
                    'WS-C4948': {
                        'descr': '10/100/1000BaseT (RJ45), 1000BaseX (SFP) Supervisor with 48 10/100/1000BASE-T ports and 4 1000BASE-',
                        'name': 'Linecard(slot 1)',
                        'pid': 'WS-C4948',
                        'sn': 'FOX1638GU8L',
                        'subslot': {
                            '1/45': {
                                'Unspecified': {
                                    'descr': '1000BaseSX',
                                    'name': 'GigabitEthernet1/45',
                                    'pid': 'Unspecified',
                                    'sn': 'AGM1637LJE4',
                                    'vid': '',
                                },
                            },
                            '1/47': {
                                'GLC-SX-MM': {
                                    'descr': '1000BaseSX',
                                    'name': 'GigabitEthernet1/47',
                                    'pid': 'GLC-SX-MM',
                                    'sn': 'VB12150046',
                                    'vid': 'V03  ',
                                },
                            },
                        },
                        'vid': 'V12  ',
                    },
                },
            },
            'Power Supply 1': {
                'other': {
                    'Power Supply 1': {
                        'descr': 'Power Supply ( AC 300W )',
                        'name': 'Power Supply 1',
                        'pid': 'PWR-C49-300AC',
                        'sn': 'PAC15240NRN',
                        'vid': '',
                    },
                },
            },
            'Power Supply 2': {
                'other': {
                    'Power Supply 2': {
                        'descr': 'Power Supply ( AC 300W )',
                        'name': 'Power Supply 2',
                        'pid': 'PWR-C49-300AC',
                        'sn': 'PAC15240S5T',
                        'vid': '',
                    },
                },
            },
        },
    }

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        inventory_obj = ShowInventory(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = inventory_obj.parse()

    def test_golden_iosv(self):
        self.maxDiff = None
        self.dev_iosv = Mock(**self.golden_output_iosv)
        inventory_obj = ShowInventory(device=self.dev_iosv)
        parsed_output = inventory_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_iosv)

    def test_golden_output_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        obj = ShowInventory(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

    def test_golden_output_3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_3)
        obj = ShowInventory(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_3)

    def test_golden_output_4(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_4)
        obj = ShowInventory(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_4)

    def test_golden_output_5(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_5)
        obj = ShowInventory(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_5)

    def test_golden_output_6(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_6)
        obj = ShowInventory(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_6)

    def test_golden_output_7(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_7)
        obj = ShowInventory(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_7)

    def test_golden_output_8(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_8)
        obj = ShowInventory(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_8)

    def test_golden_output_9(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_9)
        obj = ShowInventory(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_9)
    
    def test_golden_output_10(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_10)
        obj = ShowInventory(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_10)


class test_show_bootvar(unittest.TestCase):
    dev = Device(name='ios')
    dev_iosv = Device(name='iosv')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output_iosv = {
        "active": {
            "boot_variable": "disk0:s72033-adventerprisek9-mz.122-33.SRE0a-ssr-nxos-76k-1,12;",
            "configuration_register": "0x2012"
        },
        "next_reload_boot_variable": "disk0:s72033-adventerprisek9-mz.122-33.SRE0a-ssr-nxos-76k-1,12;"
    }

    golden_output_iosv = {'execute.return_value': '''\
        BOOT variable = disk0:s72033-adventerprisek9-mz.122-33.SRE0a-ssr-nxos-76k-1,12;
        CONFIG_FILE variable = 
        BOOTLDR variable = 
        Configuration register is 0x2012

        Standby not ready to show bootvar

    '''}

    def test_empty(self):
        self.dev = Mock(**self.empty_output)
        platform_obj = ShowBootvar(device=self.dev)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = platform_obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev_iosv = Mock(**self.golden_output_iosv)
        platform_obj = ShowBootvar(device=self.dev_iosv)
        parsed_output = platform_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_iosv)


class test_show_processes_cpu_sorted_CPU(unittest.TestCase):
    dev = Device(name='c3850')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        "five_sec_cpu_total": 13,
        "five_min_cpu": 15,
        "one_min_cpu": 23,
        "five_sec_cpu_interrupts": 0
    }

    golden_output = {'execute.return_value': '''\
        show processes cpu sorted 5min | inc CPU
        CPU utilization for five seconds: 13%/0%; one minute: 23%; five minutes: 15%
    '''}

    golden_parsed_output_1 = {
        "sort": {
            1: {
                "invoked": 3321960,
                "usecs": 109,
                "tty": 0,
                "one_min_cpu": 0.54,
                "process": "PIM Process",
                "five_min_cpu": 0.48,
                "runtime": 362874,
                "pid": 368,
                "five_sec_cpu": 1.03
            },
            2: {
                "invoked": 1466728,
                "usecs": 2442,
                "tty": 0,
                "one_min_cpu": 0.87,
                "process": "IOSv e1000",
                "five_min_cpu": 2.77,
                "runtime": 3582279,
                "pid": 84,
                "five_sec_cpu": 0.55
            },
            3: {
                "invoked": 116196,
                "usecs": 976,
                "tty": 0,
                "one_min_cpu": 0.07,
                "process": "OSPF-1 Hello",
                "five_min_cpu": 0.07,
                "runtime": 113457,
                "pid": 412,
                "five_sec_cpu": 0.15
            }
        },
        "five_sec_cpu_total": 4,
        "five_min_cpu": 9,
        "one_min_cpu": 4,
        "nonzero_cpu_processes": [
            "PIM Process",
            "IOSv e1000",
            "OSPF-1 Hello"
        ],
        "five_sec_cpu_interrupts": 0
    }

    golden_output_1 = {'execute.return_value': '''
        CPU utilization for five seconds: 4%/0%; one minute: 4%; five minutes: 9%
         PID Runtime(ms)     Invoked      uSecs   5Sec   1Min   5Min TTY Process 
         368      362874     3321960        109  1.03%  0.54%  0.48%   0 PIM Process      
          84     3582279     1466728       2442  0.55%  0.87%  2.77%   0 IOSv e1000   
          412      113457      116196        976  0.15%  0.07%  0.07%   0 OSPF-1 Hello
    '''}

    def test_empty(self):
        self.dev = Mock(**self.empty_output)
        obj = ShowProcessesCpuSorted(device=self.dev)
        with self.assertRaises(SchemaEmptyParserError):
            parsered_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output)
        obj = ShowProcessesCpuSorted(device=self.dev)
        parsed_output = obj.parse(key_word='CPU', sort_time='5min')
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_1(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output_1)
        obj = ShowProcessesCpuSorted(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)


class test_show_processes_cpu(test_show_processes_cpu_iosxe):

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowProcessesCpu(device=self.device)
        parsed_output = obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowProcessesCpu(device=self.device)
        parsed_output = obj.parse(key_word='process')
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowProcessesCpu(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


class test_show_version_rp(test_show_version_rp_iosxe):

    def test_golden_active(self):
        self.device = Mock(**self.golden_output_active)
        obj = ShowVersionRp(device=self.device)
        parsed_output = obj.parse(rp='active', status='running')
        self.maxDiff = None
        self.assertEqual(parsed_output, self.golden_parsed_output_active)

    def test_golden_standby(self):
        self.device = Mock(**self.golden_output_standby)
        obj = ShowVersionRp(device=self.device)
        parsed_output = obj.parse(rp='standby', status='running')
        self.maxDiff = None
        self.assertEqual(parsed_output, self.golden_parsed_output_standby)

    def test_golden_standby_offline(self):
        self.device = Mock(**self.golden_output_standby_offline)
        obj = ShowVersionRp(device=self.device)
        self.maxDiff = None
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(rp='standby', status='running')

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowVersionRp(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


class test_show_platform(test_show_platform_iosxe):

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        platform_obj = ShowPlatform(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = platform_obj.parse()

    def test_semi_empty(self):
        self.dev2 = Mock(**self.semi_empty_output)
        platform_obj = ShowPlatform(device=self.dev2)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = platform_obj.parse()

    def test_golden_c3850(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_c3850)
        platform_obj = ShowPlatform(device=self.dev_c3850)
        parsed_output = platform_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_c3850)

    def test_golden_asr1k(self):
        self.maxDiff = None
        self.dev_asr1k = Mock(**self.golden_output_asr1k)
        platform_obj = ShowPlatform(device=self.dev_asr1k)
        parsed_output = platform_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_asr1k)


class test_show_platform_power(test_show_platform_power_iosxe):

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        platform_obj = ShowPlatformPower(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = platform_obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        platform_obj = ShowPlatformPower(device=self.device)
        parsed_output = platform_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


class test_show_processes_cpu_history(test_show_processes_cpu_history_iosxe):

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        platform_obj = ShowProcessesCpuHistory(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = platform_obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        platform_obj = ShowProcessesCpuHistory(device=self.device)
        parsed_output = platform_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


class test_show_processes_cpu_platform(test_show_processes_cpu_platform_iosxe):

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        cpu_platform_obj = ShowProcessesCpuPlatform(device=self.device)
        parsed_output = cpu_platform_obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        cpu_platform_obj = ShowProcessesCpuPlatform(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = cpu_platform_obj.parse()


class test_show_platform_software_status_control_processor_brief(
    test_show_platform_software_status_control_processor_brief_iosxe):

    def test_empty(self):
        self.dev = Mock(**self.empty_output)
        obj = ShowPlatformSoftwareStatusControl(device=self.dev)
        with self.assertRaises(SchemaEmptyParserError):
            parsered_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output)
        obj = ShowPlatformSoftwareStatusControl(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


class test_show_platform_software_slot_active_monitor_Mem(test_show_platform_software_slot_active_monitor_Mem_iosxe):

    def test_empty(self):
        self.dev = Mock(**self.empty_output)
        obj = ShowPlatformSoftwareSlotActiveMonitorMem(device=self.dev)
        with self.assertRaises(SchemaEmptyParserError):
            parsered_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output)
        obj = ShowPlatformSoftwareSlotActiveMonitorMem(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


class test_show_platform_hardware(test_show_platform_hardware_iosxe):

    def test_golden_active(self):
        self.device = Mock(**self.golden_output_active)
        obj = ShowPlatformHardware(device=self.device)
        parsed_output = obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output, self.golden_parsed_output_active)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowPlatformHardware(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


class test_show_platform_hardware_plim(test_show_platform_hardware_plim_iosxe):

    def test_golden_port(self):
        self.device = Mock(**self.golden_output_port)
        obj = ShowPlatformHardwarePlim(device=self.device)
        parsed_output = obj.parse(port='0/0/0')
        self.maxDiff = None
        self.assertEqual(parsed_output, self.golden_parsed_output_port)

    def test_golden_slot(self):
        self.device = Mock(**self.golden_output_slot)
        obj = ShowPlatformHardwarePlim(device=self.device)
        parsed_output = obj.parse(slot='0')
        self.maxDiff = None
        self.assertEqual(parsed_output, self.golden_parsed_output_slot)

    def test_golden_subslot(self):
        self.device = Mock(**self.golden_output_subslot)
        obj = ShowPlatformHardwarePlim(device=self.device)
        parsed_output = obj.parse(subslot='0/1')
        self.maxDiff = None
        self.assertEqual(parsed_output, self.golden_parsed_output_subslot)

    def test_golden_slot_internal(self):
        self.device = Mock(**self.golden_output_slot_internal)
        obj = ShowPlatformHardwarePlim(device=self.device)
        parsed_output = obj.parse(slot='0', internal=True)
        self.maxDiff = None
        self.assertEqual(
            parsed_output, self.golden_parsed_output_slot_internal)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowPlatformHardwarePlim(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(port='0/0/0')


class test_show_platform_hardware_qfp_bqs_opm_mapping(test_show_platform_hardware_qfp_bqs_opm_mapping_iosxe):

    def test_golden_active_opm(self):
        self.device = Mock(**self.golden_output_active_opm)
        obj = ShowPlatformHardwareQfpBqsOpmMapping(device=self.device)
        parsed_output = obj.parse(status='active', slot='0')
        self.maxDiff = None
        self.assertEqual(parsed_output, self.golden_parsed_output_active_opm)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowPlatformHardwareQfpBqsOpmMapping(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(status='active', slot='0')


class test_show_platform_hardware_qfp_bqs_ipm_mapping(test_show_platform_hardware_qfp_bqs_ipm_mapping_iosxe):

    def test_golden_active_ipm(self):
        self.device = Mock(**self.golden_output_active_ipm)
        obj = ShowPlatformHardwareQfpBqsIpmMapping(device=self.device)
        parsed_output = obj.parse(status='active', slot='0')
        self.maxDiff = None
        self.assertEqual(parsed_output, self.golden_parsed_output_active_ipm)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowPlatformHardwareQfpBqsIpmMapping(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(status='active', slot='0')


class test_show_platform_hardware_serdes_statistics(test_show_platform_hardware_serdes_statistics_iosxe):

    def test_golden_serdes(self):
        self.device = Mock(**self.golden_output_serdes)
        obj = ShowPlatformHardwareSerdes(device=self.device)
        parsed_output = obj.parse(slot='0')
        self.maxDiff = None
        self.assertEqual(parsed_output, self.golden_parsed_output_serdes)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowPlatformHardwareSerdes(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(slot='0')


class test_show_platform_hardware_serdes_statistics_internal(
    test_show_platform_hardware_serdes_statistics_internal_iosxe):

    def test_golden(self):
        self.device = Mock(**self.golden_output_serdes_internal)
        obj = ShowPlatformHardwareSerdesInternal(device=self.device)
        parsed_output = obj.parse(slot='0')
        self.maxDiff = None
        self.assertEqual(
            parsed_output, self.golden_parsed_output_serdes_internal)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowPlatformHardwareSerdesInternal(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(slot='0')


class show_platform_hardware_qfp_bqs_statistics_channel_all(
    show_platform_hardware_qfp_bqs_statistics_channel_all_iosxe):

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        platform_obj = ShowPlatformHardwareQfpBqsStatisticsChannelAll(
            device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = platform_obj.parse(
                status='active', slot='0', iotype='ipm')

    def test_golden_active_ipm(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_active_ipm)
        platform_obj = ShowPlatformHardwareQfpBqsStatisticsChannelAll(
            device=self.device)
        parsed_output = platform_obj.parse(
            status='active', slot='0', iotype='ipm')
        self.assertEqual(parsed_output, self.golden_parsed_output_active_ipm)

    def test_golden_active_opm(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_active_opm)
        platform_obj = ShowPlatformHardwareQfpBqsStatisticsChannelAll(
            device=self.device)
        parsed_output = platform_obj.parse(
            status='active', slot='0', iotype='opm')
        self.assertEqual(parsed_output, self.golden_parsed_output_active_opm)


class show_platform_hardware_qfp_interface(show_platform_hardware_qfp_interface_iosxe):

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        platform_obj = ShowPlatformHardwareQfpInterfaceIfnameStatistics(
            device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = platform_obj.parse(
                status='active', interface='gigabitEthernet 0/0/0')

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        platform_obj = ShowPlatformHardwareQfpInterfaceIfnameStatistics(
            device=self.device)
        parsed_output = platform_obj.parse(
            status='active', interface='gigabitEthernet 0/0/0')
        self.assertEqual(parsed_output, self.golden_parsed_output)


class test_show_platform_hardware_qfp_statistics_drop(test_show_platform_hardware_qfp_statistics_drop_iosxe):

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        platform_obj = ShowPlatformHardwareQfpStatisticsDrop(
            device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = platform_obj.parse(status='active')

    def test_golden_active(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_active)
        platform_obj = ShowPlatformHardwareQfpStatisticsDrop(
            device=self.device)
        parsed_output = platform_obj.parse(status='active')
        self.assertEqual(parsed_output, self.golden_parsed_output_active)


class test_show_env(test_show_env_iosxe):

    def test_empty(self):
        self.dev = Mock(**self.empty_output)
        obj = ShowEnvironment(device=self.dev)
        with self.assertRaises(SchemaEmptyParserError):
            parsered_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output)
        obj = ShowEnvironment(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


class test_show_module(test_show_module_iosxe):

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        platform_obj = ShowModule(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = platform_obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_c3850)
        platform_obj = ShowModule(device=self.dev_c3850)
        parsed_output = platform_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_c3850)


class test_show_switch(test_show_switch_iosxe):

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        platform_obj = ShowSwitch(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = platform_obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_c3850)
        platform_obj = ShowSwitch(device=self.dev_c3850)
        parsed_output = platform_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_c3850)


class test_show_switch_detail(test_show_switch_detail_iosxe):

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        platform_obj = ShowSwitchDetail(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = platform_obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_c3850)
        platform_obj = ShowSwitchDetail(device=self.dev_c3850)
        parsed_output = platform_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_c3850)


if __name__ == '__main__':
    unittest.main()
