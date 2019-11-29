#!/bin/env python
import unittest

from unittest.mock import Mock
from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                       SchemaMissingKeyError
from genie.libs.parser.iosxe.show_platform import ShowVersion,\
                                                  Dir,\
                                                  ShowRedundancy,\
                                                  ShowRedundancyStates,\
                                                  ShowInventory,\
                                                  ShowPlatform, ShowBoot, \
                                                  ShowSwitchDetail, \
                                                  ShowSwitch, \
                                                  ShowModule, \
                                                  ShowPlatformSoftwareStatusControl, \
                                                  ShowPlatformSoftwareSlotActiveMonitorMem, \
                                                  ShowProcessesCpuSorted, \
                                                  ShowProcessesCpuPlatform, \
                                                  ShowEnvironment, \
                                                  ShowProcessesCpu, \
                                                  ShowVersionRp, \
                                                  ShowPlatformHardware, \
                                                  ShowPlatformHardwarePlim, \
                                                  ShowPlatformHardwareQfpBqsOpmMapping, \
                                                  ShowPlatformHardwareQfpBqsIpmMapping, \
                                                  ShowPlatformHardwareSerdes, \
                                                  ShowPlatformHardwareSerdesInternal, \
                                                  ShowPlatformPower, \
                                                  ShowPlatformHardwareQfpBqsStatisticsChannelAll, \
                                                  ShowPlatformHardwareQfpInterfaceIfnameStatistics, \
                                                  ShowPlatformHardwareQfpStatisticsDrop, \
                                                  ShowProcessesCpuHistory, \
                                                  ShowProcessesMemory


class TestShowVersion(unittest.TestCase):

    dev1 = Device(name='empty')
    dev2 = Device(name='semi_empty')
    dev_asr1k = Device(name='asr1k')
    dev_c3850 = Device(name='c3850')
    dev_isr4k = Device(name='isr4k')
    dev_asr901 = Device(name='asr901')
    dev_asr1002 = Device(name='asr1002')
    dev_c4k = Device(name='c4507')
    empty_output = {'execute.return_value': ''}
    semi_empty_output = {'execute.return_value': '''\
        Cisco IOS-XE software, Copyright (c) 2005-2017 by cisco Systems, Inc.
    '''}

    golden_parsed_output_c3850 = {
        'version': {
            'version_short': '16.4',
            'platform': 'Catalyst L3 Switch',
            'version': '16.4.20170410:165034',
            'returned_to_rom_at': '17:05:27 UTC Mon Apr 10 2017',
            'returned_to_rom_by': 'reload',
            'compiled_by': 'mcpre',
            'compiled_date': 'Mon 10-Apr-17 13:02',
            'image_id': 'CAT3K_CAA-UNIVERSALK9-M',
            'rom': 'IOS-XE ROMMON',
            'bootldr': 'CAT3K_CAA Boot Loader (CAT3K_CAA-HBOOT-M) Version 4.318, engineering software (D)',
            'hostname': 'R1',
            'image_type': 'developer image',
            'uptime': '1 hour, 24 minutes',
            'uptime_this_cp': '1 hour, 27 minutes',
            'system_restarted_at': '17:23:53 UTC Mon Apr 10 2017',
            'system_image': 'tftp://10.1.6.241//auto/tftp-ssr/Edison/cat3k_caa-universalk9.BLD_V164_THROTTLE_LATEST_20170410_174845.SSA.bin',
            'last_reload_reason': 'Admin reload CLI',
            'license_type': 'Permanent',
            'license_level': 'ipservicesk9',
            'next_reload_license_level': 'ipservicesk9',
            'chassis': 'WS-C3850-24P',
            'processor_type': 'MIPS',
            'chassis_sn': 'FCW1932D0LB',
            'rtr_type': 'Edison',
            'os': 'IOS-XE',
            'curr_config_register': '0x102',
            'main_mem': '862498',
            'number_of_intfs': {
                'Virtual Ethernet': '13',
                'Gigabit Ethernet': '140',
                'Ten Gigabit Ethernet': '20',
            },
            'mem_size': {
                'non-volatile configuration': '2048',
                'physical': '4194304',
            },
            'disks': {
                'crashinfo:.': {
                    'disk_size': '262143',
                    'type_of_disk': 'Crash Files',
                },
                'crashinfo-2:.': {
                    'disk_size': '250456',
                    'type_of_disk': 'Crash Files',
                },
                'crashinfo-3:.': {
                    'disk_size': '250456',
                    'type_of_disk': 'Crash Files',
                },
                'crashinfo-4:.': {
                    'disk_size': '250456',
                    'type_of_disk': 'Crash Files',
                },
                'crashinfo-5:.': {
                    'disk_size': '250456',
                    'type_of_disk': 'Crash Files',
                },
                'flash:.': {
                    'disk_size': '1586119',
                    'type_of_disk': 'Flash',
                },
                'flash-2:.': {
                    'disk_size': '1609272',
                    'type_of_disk': 'Flash',
                },
                'flash-3:.': {
                    'disk_size': '1609272',
                    'type_of_disk': 'Flash',
                },
                'flash-4:.': {
                    'disk_size': '1609272',
                    'type_of_disk': 'Flash',
                },
                'flash-5:.': {
                    'disk_size': '1609272',
                    'type_of_disk': 'Flash',
                },
                'webui:.': {
                    'disk_size': '0',
                    'type_of_disk': '',
                },
            },
            'switch_num': {
                '1': {
                    'uptime': '1 hour, 27 minutes',
                    'mac_address': '38:20:56:72:7d:80',
                    'mb_assembly_num': '73-15805-04',
                    'mb_sn': 'FOC19315RWV',
                    'model_rev_num': 'U0',
                    'mb_rev_num': 'A0',
                    'model_num': 'WS-C3850-24P',
                    'system_sn': 'FCW1932D0LB',
                    'mode': 'BUNDLE',
                    'model': 'WS-C3850-24P',
                    'sw_image': 'CAT3K_CAA-UNIVERSALK9',
                    'ports': '32',
                    'sw_ver': '16.4.2',
                    'active': True,
                },
                '2': {
                    'uptime': '1 hour, 27 minutes',
                    'mac_address': '38:20:56:29:7b:00',
                    'mb_assembly_num': '73-15805-04',
                    'mb_sn': 'FOC19315SCE',
                    'model_rev_num': 'U0',
                    'mb_rev_num': 'A0',
                    'model_num': 'WS-C3850-24P',
                    'system_sn': 'FOC1932X0K1',
                    'mode': 'BUNDLE',
                    'model': 'WS-C3850-24P',
                    'sw_image': 'CAT3K_CAA-UNIVERSALK9',
                    'ports': '32',
                    'sw_ver': '16.4.2',
                    'active': False
                },
                '3': {
                    'uptime': '1 hour, 27 minutes',
                    'mac_address': '38:20:56:72:a8:00',
                    'mb_assembly_num': '73-15805-04',
                    'mb_sn': 'FOC193182KD',
                    'model_rev_num': 'U0',
                    'mb_rev_num': 'A0',
                    'model_num': 'WS-C3850-24P',
                    'system_sn': 'FCW1932C0MA',
                    'mode': 'BUNDLE',
                    'model': 'WS-C3850-24P',
                    'sw_image': 'CAT3K_CAA-UNIVERSALK9',
                    'ports': '32',
                    'sw_ver': '16.4.2',
                    'active': False
                },
                '4': {
                    'uptime': '1 hour, 27 minutes',
                    'mac_address': '38:20:56:29:97:00',
                    'mb_assembly_num': '73-15805-04',
                    'mb_sn': 'FOC193182KG',
                    'model_rev_num': 'U0',
                    'mb_rev_num': 'A0',
                    'model_num': 'WS-C3850-24P',
                    'system_sn': 'FCW1932D0L0',
                    'mode': 'BUNDLE',
                    'model': 'WS-C3850-24P',
                    'sw_image': 'CAT3K_CAA-UNIVERSALK9',
                    'ports': '32',
                    'sw_ver': '16.4.2',
                    'active': False
                },
                '5': {
                    'uptime': '1 hour, 27 minutes',
                    'mac_address': '38:20:56:29:49:00',
                    'mb_assembly_num': '73-15805-04',
                    'mb_sn': 'FOC193182KB',
                    'model_rev_num': 'U0',
                    'mb_rev_num': 'A0',
                    'model_num': 'WS-C3850-24P',
                    'system_sn': 'FOC1932X0F9',
                    'mode': 'BUNDLE',
                    'model': 'WS-C3850-24P',
                    'sw_image': 'CAT3K_CAA-UNIVERSALK9',
                    'ports': '32',
                    'sw_ver': '16.4.2',
                    'active': False,
                },
            }
        }
    }

    golden_output_c3850 = {'execute.return_value': '''\
        Cisco IOS Software [Everest], Catalyst L3 Switch Software (CAT3K_CAA-UNIVERSALK9-M), Experimental Version 16.4.20170410:165034 [v164_throttle-BLD-BLD_V164_THROTTLE_LATEST_20170410_174845 105]
        Copyright (c) 1986-2017 by Cisco Systems, Inc.
        Compiled Mon 10-Apr-17 13:02 by mcpre


        Cisco IOS-XE software, Copyright (c) 2005-2017 by cisco Systems, Inc.
        All rights reserved.  Certain components of Cisco IOS-XE software are
        licensed under the GNU General Public License ("GPL") Version 2.0.  The
        software code licensed under GPL Version 2.0 is free software that comes
        with ABSOLUTELY NO WARRANTY.  You can redistribute and/or modify such
        GPL code under the terms of GPL Version 2.0.  For more details, see the
        documentation or "License Notice" file accompanying the IOS-XE software,
        or the applicable URL provided on the flyer accompanying the IOS-XE
        software.


        ROM: IOS-XE ROMMON
        BOOTLDR: CAT3K_CAA Boot Loader (CAT3K_CAA-HBOOT-M) Version 4.318, engineering software (D)

        R1 uptime is 1 hour, 24 minutes
        Uptime for this control processor is 1 hour, 27 minutes
        System returned to ROM by reload at 17:05:27 UTC Mon Apr 10 2017
        System restarted at 17:23:53 UTC Mon Apr 10 2017
        System image file is "tftp://10.1.6.241//auto/tftp-ssr/Edison/cat3k_caa-universalk9.BLD_V164_THROTTLE_LATEST_20170410_174845.SSA.bin"
        Last reload reason: Admin reload CLI



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

        -----------------------------------------------------------------
        Technology-package                   Technology-package
        Current             Type             Next reboot  
        ------------------------------------------------------------------
        ipservicesk9        Permanent        ipservicesk9

        cisco WS-C3850-24P (MIPS) processor (revision U0) with 862498K/6147K bytes of memory.
        Processor board ID FCW1932D0LB
        13 Virtual Ethernet interfaces
        140 Gigabit Ethernet interfaces
        20 Ten Gigabit Ethernet interfaces
        2048K bytes of non-volatile configuration memory.
        4194304K bytes of physical memory.
        262143K bytes of Crash Files at crashinfo:.
        250456K bytes of Crash Files at crashinfo-2:.
        250456K bytes of Crash Files at crashinfo-3:.
        250456K bytes of Crash Files at crashinfo-4:.
        250456K bytes of Crash Files at crashinfo-5:.
        1586119K bytes of Flash at flash:.
        1609272K bytes of Flash at flash-2:.
        1609272K bytes of Flash at flash-3:.
        1609272K bytes of Flash at flash-4:.
        1609272K bytes of Flash at flash-5:.
        0K bytes of  at webui:.

        Base Ethernet MAC Address          : 38:20:56:72:7d:80
        Motherboard Assembly Number        : 73-15805-04
        Motherboard Serial Number          : FOC19315RWV
        Model Revision Number              : U0
        Motherboard Revision Number        : A0
        Model Number                       : WS-C3850-24P
        System Serial Number               : FCW1932D0LB


        Switch Ports Model              SW Version        SW Image              Mode   
        ------ ----- -----              ----------        ----------            ----   
        *    1 32    WS-C3850-24P       16.4.2            CAT3K_CAA-UNIVERSALK9 BUNDLE 
             2 32    WS-C3850-24P       16.4.2            CAT3K_CAA-UNIVERSALK9 BUNDLE 
             3 32    WS-C3850-24P       16.4.2            CAT3K_CAA-UNIVERSALK9 BUNDLE 
             4 32    WS-C3850-24P       16.4.2            CAT3K_CAA-UNIVERSALK9 BUNDLE 
             5 32    WS-C3850-24P       16.4.2            CAT3K_CAA-UNIVERSALK9 BUNDLE 


        Switch 02
        ---------
        Switch uptime                      : 1 hour, 27 minutes 

        Base Ethernet MAC Address          : 38:20:56:29:7b:00
        Motherboard Assembly Number        : 73-15805-04
        Motherboard Serial Number          : FOC19315SCE
        Model Revision Number              : U0
        Motherboard Revision Number        : A0
        Model Number                       : WS-C3850-24P
        System Serial Number               : FOC1932X0K1

        Switch 03
        ---------
        Switch uptime                      : 1 hour, 27 minutes 

        Base Ethernet MAC Address          : 38:20:56:72:a8:00
        Motherboard Assembly Number        : 73-15805-04
        Motherboard Serial Number          : FOC193182KD
        Model Revision Number              : U0
        Motherboard Revision Number        : A0
        Model Number                       : WS-C3850-24P
        System Serial Number               : FCW1932C0MA

        Switch 04
        ---------
        Switch uptime                      : 1 hour, 27 minutes 

        Base Ethernet MAC Address          : 38:20:56:29:97:00
        Motherboard Assembly Number        : 73-15805-04
        Motherboard Serial Number          : FOC193182KG
        Model Revision Number              : U0
        Motherboard Revision Number        : A0
        Model Number                       : WS-C3850-24P
        System Serial Number               : FCW1932D0L0

        Switch 05
        ---------
        Switch uptime                      : 1 hour, 27 minutes 

        Base Ethernet MAC Address          : 38:20:56:29:49:00
        Motherboard Assembly Number        : 73-15805-04
        Motherboard Serial Number          : FOC193182KB
        Model Revision Number              : U0
        Motherboard Revision Number        : A0
        Model Number                       : WS-C3850-24P
        System Serial Number               : FOC1932X0F9

        Configuration register is 0x102
'''}

    golden_parsed_output_asr1k = {
        'version': {
            'version_short': '16.3',
            'platform': 'ASR1000',
            'compiled_by': 'mcpre',
            'compiled_date': 'Mon 10-Apr-17 04:35',
            'returned_to_rom_at': '02:14:51 PDT Mon Apr 10 2017',
            'returned_to_rom_by': 'reload',
            'version': '16.3.20170410:103306',
            'image_id': 'X86_64_LINUX_IOSD-UNIVERSALK9-M',
            'rom': 'IOS-XE ROMMON',
            'hostname': 'PE1',
            'uptime': '32 minutes',
            'image_type': 'developer image',
            'uptime_this_cp': '34 minutes',
            'system_restarted_at': '09:08:57 PDT Mon Apr 10 2017',
            'system_image': 'harddisk:test-image-PE1-13113029',
            'last_reload_reason': 'Reload Command',
            'license_type': 'RightToUse',
            'license_level': 'advipservices',
            'next_reload_license_level': 'advipservices',
            'chassis': 'ASR1006',
            'processor_type': 'RP2',
            'chassis_sn': 'FOX1444GPXU',
            'rtr_type': 'ASR1K',
            'os': 'IOS-XE',
            'curr_config_register': '0x2000',
            'next_config_register': '0x2002',
            'main_mem': '4138965',
            'number_of_intfs': {
                'Gigabit Ethernet': '5',
            },
            'mem_size': {
                'non-volatile configuration': '32768',
                'physical': '8388608',
            },
            'disks': {
                'bootflash:.': {
                    'disk_size': '1925119',
                    'type_of_disk': 'eUSB flash',
                },
                'harddisk:.': {
                    'disk_size': '78085207',
                    'type_of_disk': 'SATA hard disk',
                },
                'webui:.': {
                    'disk_size': '0',
                    'type_of_disk': '',
                },
            }
        }
    }

    golden_output_asr1k = {'execute.return_value': '''\
        Cisco IOS XE Software, Version BLD_V163_MR_THROTTLE_LATEST_20170410_093453_V16_3_3_24
        Cisco IOS Software [Denali], ASR1000 Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Experimental Version 16.3.20170410:103306 [v163_mr_throttle-BLD-BLD_V163_MR_THROTTLE_LATEST_20170410_093453 118]
        Copyright (c) 1986-2017 by Cisco Systems, Inc.
        Compiled Mon 10-Apr-17 04:35 by mcpre


        Cisco IOS-XE software, Copyright (c) 2005-2017 by cisco Systems, Inc.
        All rights reserved.  Certain components of Cisco IOS-XE software are
        licensed under the GNU General Public License ("GPL") Version 2.0.  The
        software code licensed under GPL Version 2.0 is free software that comes
        with ABSOLUTELY NO WARRANTY.  You can redistribute and/or modify such
        GPL code under the terms of GPL Version 2.0.  For more details, see the
        documentation or "License Notice" file accompanying the IOS-XE software,
        or the applicable URL provided on the flyer accompanying the IOS-XE
        software.


        ROM: IOS-XE ROMMON

        PE1 uptime is 32 minutes
        Uptime for this control processor is 34 minutes
        System returned to ROM by reload at 02:14:51 PDT Mon Apr 10 2017
        System restarted at 09:08:57 PDT Mon Apr 10 2017
        System image file is "harddisk:test-image-PE1-13113029"
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

        License Type: RightToUse
        License Level: advipservices
        Next reload license Level: advipservices

        cisco ASR1006 (RP2) processor (revision RP2) with 4138965K/6147K bytes of memory.
        Processor board ID FOX1444GPXU
        5 Gigabit Ethernet interfaces
        32768K bytes of non-volatile configuration memory.
        8388608K bytes of physical memory.
        1925119K bytes of eUSB flash at bootflash:.
        78085207K bytes of SATA hard disk at harddisk:.
        0K bytes of  at webui:.

        Configuration register is 0x2000 (will be 0x2002 at next reload)
'''}

    golden_parsed_output_isr4k = {
        'version': {
            'chassis': 'ISR4451-X/K9',
            'chassis_sn': 'FGL273610NK',
            'compiled_by': 'mcpre',
            'compiled_date': 'Mon 10-Dec-18 13:10',
            'returned_to_rom_at': '07:15:43 UTC Fri Feb 1 2019',
            'returned_to_rom_by': 'Reload Command',
            'curr_config_register': '0x2102',
            'license_package': {
                'appxk9': {
                    'license_level': 'appxk9',
                    'license_type': 'RightToUse',
                    'next_reload_license_level': 'appxk9'
                },
                'ipbase': {
                    'license_level': 'ipbasek9',
                    'license_type': 'Permanent',
                    'next_reload_license_level': 'ipbasek9'
                },
                'securityk9': {
                    'license_level': 'securityk9',
                    'license_type': 'RightToUse',
                    'next_reload_license_level': 'securityk9'
                },
                'uck9': {
                    'license_level': 'None',
                    'license_type': 'None',
                    'next_reload_license_level': 'None'
                }
            },
            'module': {
                'esg': {
                    'AdvUCSuiteK9': {
                        'suite_current': 'None',
                        'suite_next_reboot': 'None',
                        'type': 'None'
                    },
                    'FoundationSuiteK9': {
                        'suite_current': 'None',
                        'suite_next_reboot': 'None',
                        'type': 'None'
                    },
                    'appxk9': {},
                    'cme-srst': {},
                    'cube': {},
                    'securityk9': {},
                    'uck9': {}
                }
            },
            'disks': {
                'bootflash:.': {
                    'disk_size': '7341807',
                    'type_of_disk': 'flash memory'
                },
                'webui:.': {
                    'disk_size': '0',
                    'type_of_disk': 'WebUI ODM Files'
                }
            },
            'hostname': 'isr4k',
            'image_id': 'X86_64_LINUX_IOSD-UNIVERSALK9-M',
            'image_type': 'production image',
            'last_reload_reason': 'Reload Command',
            'main_mem': '1795979',
            'mem_size': {
                'non-volatile configuration': '32768',
                'physical': '4194304'
            },
            'number_of_intfs': {
                'Gigabit Ethernet': '4',
                'Virtual Ethernet': '1'
            },
            'os': 'IOS-XE',
            'platform': 'ISR',
            'processor_type': '2RU',
            'rom': 'IOS-XE ROMMON',
            'rtr_type': 'ISR4451-X/K9',
            'system_image': 'bootflash:isr4400-universalk10.115.6.5.SPA.bin',
            'system_restarted_at': '07:19:15 UTC Fri Feb 1 2019',
            'uptime': '2 days, 3 hours, 18 minutes',
            'uptime_this_cp': '2 days, 3 hours, 19 minutes',
            'version': '16.6.5',
            'version_short': '16.6'
        }
    }

    golden_output_isr4k = {'execute.return_value': '''\
        Cisco IOS XE Software, Version 16.06.05
        Cisco IOS Software [Everest], ISR Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 16.6.5, RELEASE SOFTWARE (fc3)
        Technical Support: http://www.cisco.com/techsupport
        Copyright (c) 1986-2018 by Cisco Systems, Inc.
        Compiled Mon 10-Dec-18 13:10 by mcpre


        Cisco IOS-XE software, Copyright (c) 2005-2018 by cisco Systems, Inc.
        All rights reserved.  Certain components of Cisco IOS-XE software are
        licensed under the GNU General Public License ("GPL") Version 2.0.  The
        software code licensed under GPL Version 2.0 is free software that comes
        with ABSOLUTELY NO WARRANTY.  You can redistribute and/or modify such
        GPL code under the terms of GPL Version 2.0.  For more details, see the
        documentation or "License Notice" file accompanying the IOS-XE software,
        or the applicable URL provided on the flyer accompanying the IOS-XE
        software.


        ROM: IOS-XE ROMMON

        isr4k uptime is 2 days, 3 hours, 18 minutes
        Uptime for this control processor is 2 days, 3 hours, 19 minutes
        System returned to ROM by Reload Command at 07:15:43 UTC Fri Feb 1 2019
        System restarted at 07:19:15 UTC Fri Feb 1 2019
        System image file is "bootflash:isr4400-universalk10.115.6.5.SPA.bin"
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



        Suite License Information for Module:'esg'

        --------------------------------------------------------------------------------
        Suite                 Suite Current         Type           Suite Next reboot
        --------------------------------------------------------------------------------
        FoundationSuiteK9     None                  None           None
        securityk9
        appxk9

        AdvUCSuiteK9          None                  None           None
        uck9
        cme-srst
        cube


        Technology Package License Information:

        -----------------------------------------------------------------
        Technology    Technology-package           Technology-package
                      Current       Type           Next reboot
        ------------------------------------------------------------------
        appxk9           appxk9           RightToUse       appxk9
        uck9             None             None             None
        securityk9       securityk9       RightToUse       securityk9
        ipbase           ipbasek9         Permanent        ipbasek9

        cisco ISR4451-X/K9 (2RU) processor with 1795979K/6147K bytes of memory.
        Processor board ID FGL273610NK
        1 Virtual Ethernet interface
        4 Gigabit Ethernet interfaces
        32768K bytes of non-volatile configuration memory.
        4194304K bytes of physical memory.
        7341807K bytes of flash memory at bootflash:.
        0K bytes of WebUI ODM Files at webui:.

        Configuration register is 0x2102
''' }

    golden_parsed_output_asr901 = {
        'version': {
            'chassis': 'A901-6CZ-FT-D',
            'chassis_sn': 'CAT1733U070',
            'compiled_by': 'prod_rel_team',
            'compiled_date': 'Mon 19-Mar-18 16:39',
            'returned_to_rom_at': '15:57:52 CDT Mon Sep 24 2018',
            'returned_to_rom_by': 'reload',
            'last_reload_type': 'Normal Reload',
            'processor_board_flash': '98304K',
            'curr_config_register': '0x2102',
            'hostname': 'LAB-ASR901T',
            'image_id': 'ASR901-UNIVERSALK9-M',
            'image_type': 'production image',
            'last_reload_reason': 'Reload Command',
            'license_level': 'AdvancedMetroIPAccess',
            'license_type': 'Smart License',
            'main_mem': '393216',
            'mem_size': {
                'non-volatile configuration': '256'
            },
            'next_reload_license_level': 'AdvancedMetroIPAccess',
            'number_of_intfs': {
                'Gigabit Ethernet': '12',
                'Ten Gigabit Ethernet': '2',
                'External Alarm': '1',
                'FastEthernet': '1',
                'terminal': '1',
                'Channelized T1': '8'
            },
            'processor': {
                'speed': '800MHz',
                'core': 'E500v2',
                'cpu_type': 'P2020',
                'l2_cache': '512KB'
            },
            'os': 'IOS',
            'platform': '901',
            'processor_type': 'P2020',
            'rom': 'System Bootstrap, Version 15.6(2r)SP4, RELEASE SOFTWARE '
                '(fc1)',
            'rtr_type': 'A901-6CZ-FT-D',
            'system_image': 'flash:asr901-universalk9-mz.156-2.SP4.bin',
            'system_restarted_at': '15:59:27 CDT Mon Sep 24 2018',
            'uptime': '26 weeks, 21 hours, 26 minutes',
            'version': '15.6(2)SP4',
            'version_short': '15.6'
        }
    }
    
    golden_output_asr901 = {'execute.return_value': '''
        show version
        Cisco IOS Software, 901 Software (ASR901-UNIVERSALK9-M), Version 15.6(2)SP4, RELEASE SOFTWARE (fc3)
        Technical Support: http://www.cisco.com/techsupport
        Copyright (c) 1986-2018 by Cisco Systems, Inc.
        Compiled Mon 19-Mar-18 16:39 by prod_rel_team

        ROM: System Bootstrap, Version 15.6(2r)SP4, RELEASE SOFTWARE (fc1)

        LAB-ASR901T uptime is 26 weeks, 21 hours, 26 minutes
        System returned to ROM by reload at 15:57:52 CDT Mon Sep 24 2018
        System restarted at 15:59:27 CDT Mon Sep 24 2018
        System image file is "flash:asr901-universalk9-mz.156-2.SP4.bin"
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

        License Level: AdvancedMetroIPAccess
        License Type: Smart License
        Next reload license Level: AdvancedMetroIPAccess

        Cisco A901-6CZ-FT-D (P2020) processor (revision 1.0) with 393216K/131072K bytes of memory.
        Processor board ID CAT1733U070
        P2020 CPU at 800MHz, E500v2 core, 512KB L2 Cache
        1 External Alarm interface
        1 FastEthernet interface
        12 Gigabit Ethernet interfaces
        2 Ten Gigabit Ethernet interfaces
        1 terminal line
        8 Channelized T1 ports
        256K bytes of non-volatile configuration memory.
        98304K bytes of processor board System flash (Read/Write)

        Configuration register is 0x2102
        '''}

    golden_output_c4507 = {'execute.return_value': '''
        Cisco IOS Software, IOS-XE Software, Catalyst 4500 L3 Switch Software (cat4500e-UNIVERSALK9-M), Version 03.03.02.SG RELEASE SOFTWARE (fc1)
        Technical Support: http://www.cisco.com/techsupport
        Copyright (c) 1986-2012 by Cisco Systems, Inc.
        Compiled Tue 23-Oct-12 23:51 by prod_rel_team

        ROM: 15.0(1r)SG5
        switchname uptime is 6 years, 2 weeks, 13 hours, 31 minutes
        Uptime for this control processor is 6 years, 2 weeks, 13 hours, 33 minutes
        System returned to ROM by reload
        System restarted at 09:57:20 GMT Tue Oct 15 2013
        Running default software
        Jawa Revision 7, Snowtrooper Revision 0x0.0x1C

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


        License Information for 'WS-X45-SUP7-E'
            License Level: entservices   Type: Permanent
            Next reboot license Level: entservices

        cisco WS-C4507R+E (MPC8572) processor (revision 10) with 2097152K/20480K bytes of memory.
        Processor board ID FXS1729E2TD
        MPC8572 CPU at 1.5GHz, Supervisor 7
        Last reset from Reload
        9 Virtual Ethernet interfaces
        240 Gigabit Ethernet interfaces
        4 Ten Gigabit Ethernet interfaces
        511K bytes of non-volatile configuration memory.

        Configuration register is 0x2101 (will be 0x2102 at next reload)

    '''}

    golden_parsed_output_c4507 = {
        'version': {
            'chassis': 'WS-C4507R+E',
            'chassis_sn': 'FXS1729E2TD',
            'compiled_by': 'prod_rel_team',
            'compiled_date': 'Tue 23-Oct-12 23:51',
            'curr_config_register': '0x2101',
            'hostname': 'switchname',
            'image_id': 'cat4500e-UNIVERSALK9-M',
            'image_type': 'production image',
            'jawa_revision': '7',
            'last_reload_reason': 'Reload',
            'license_level': 'entservices',
            'license_type': 'Permanent',
            'main_mem': '2097152',
            'mem_size': {
                'non-volatile configuration': '511'
            },
            'next_config_register': '0x2102',
            'next_reload_license_level': 'entservices',
            'number_of_intfs': {
                'Gigabit Ethernet': '240',
                'Ten Gigabit Ethernet': '4',
                'Virtual Ethernet': '9'
            },
            'os': 'IOS-XE',
            'platform': 'Catalyst 4500 L3 Switch',
            'processor': {
                'cpu_type': 'MPC8572',
                'speed': '1.5GHz',
                'supervisor': '7'
            },
            'processor_type': 'MPC8572',
            'returned_to_rom_by': 'reload',
            'rom': '15.0(1r)SG5',
            'rtr_type': 'WS-C4507R+E',
            'running_default_software': True,
            'snowtrooper_revision': '0x0.0x1C',
            'system_restarted_at': '09:57:20 GMT Tue Oct 15 2013',
            'uptime': '6 years, 2 weeks, 13 hours, 31 minutes',
            'uptime_this_cp': '6 years, 2 weeks, 13 hours, 33 minutes',
            'version': '03.03.02.SG',
            'version_short': '03.03'
        }
    }

    golden_output_1 = {'execute.return_value': '''
        Cisco IOS Software, IOS-XE Software, Catalyst 4500 L3 Switch  Software (cat4500e-UNIVERSALK9-M), Version 03.04.06.SG RELEASE SOFTWARE (fc1)
        Technical Support: http://www.cisco.com/techsupport
        Copyright (c) 1986-2015 by Cisco Systems, Inc.
        Compiled Mon 04-May-15 02:44 by prod_rel_team
        
        
        
        Cisco IOS-XE software, Copyright (c) 2005-2010, 2012 by cisco Systems, Inc.
        All rights reserved.  Certain components of Cisco IOS-XE software are
        licensed under the GNU General Public License ("GPL") Version 2.0.  The
        software code licensed under GPL Version 2.0 is free software that comes
        with ABSOLUTELY NO WARRANTY.  You can redistribute and/or modify such
        GPL code under the terms of GPL Version 2.0.  For more details, see the
        documentation or "License Notice" file accompanying the IOS-XE software,
        or the applicable URL provided on the flyer accompanying the IOS-XE
        software.
        
        
        
        ROM: 15.0(1r)SG10
        sample_4510r_e uptime is 2 years, 11 weeks, 3 days, 3 hours, 3 minutes
        Uptime for this control processor is 2 years, 11 weeks, 1 day, 22 hours, 18 minutes
        System returned to ROM by SSO Switchover
        System restarted at 19:11:28 GMT Tue Aug 22 2017
        System image file is "bootflash:cat4500e-universalk9.SPA.03.04.06.SG.151-2.SG6.bin"
        Jawa Revision 7, Snowtrooper Revision 0x0.0x1C
        
        Last reload reason: power-on
        
        
        
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
        
        
        License Information for 'WS-X45-SUP7-E'
            License Level: entservices   Type: Permanent
            Next reboot license Level: entservices
        
        cisco WS-C4510R+E (MPC8572) processor (revision 11) with 2097152K/20480K bytes of memory.
        Processor board ID JAD213101PP
        MPC8572 CPU at 1.5GHz, Supervisor 7
        Last reset from PowerUp
        8 Virtual Ethernet interfaces
        384 Gigabit Ethernet interfaces
        8 Ten Gigabit Ethernet interfaces
        511K bytes of non-volatile configuration memory.
        
        Configuration register is 0x2102
        
    '''}

    golden_parsed_output_1 = {
        'version': {
            'version_short': '03.04',
            'platform': 'Catalyst 4500 L3 Switch',
            'version': '03.04.06.SG',
            'image_id': 'cat4500e-UNIVERSALK9-M',
            'os': 'IOS-XE',
            'image_type': 'production image',
            'compiled_date': 'Mon 04-May-15 02:44',
            'compiled_by': 'prod_rel_team',
            'rom': '15.0(1r)SG10',
            'hostname': 'sample_4510r_e',
            'uptime': '2 years, 11 weeks, 3 days, 3 hours, 3 minutes',
            'uptime_this_cp': '2 years, 11 weeks, 1 day, 22 hours, 18 minutes',
            'returned_to_rom_by': 'SSO Switchover',
            'system_restarted_at': '19:11:28 GMT Tue Aug 22 2017',
            'system_image': 'bootflash:cat4500e-universalk9.SPA.03.04.06.SG.151-2.SG6.bin',
            'jawa_revision': '7',
            'snowtrooper_revision': '0x0.0x1C',
            'last_reload_reason': 'PowerUp',
            'license_type': 'Permanent',
            'license_level': 'entservices',
            'next_reload_license_level': 'entservices',
            'chassis': 'WS-C4510R+E',
            'main_mem': '2097152',
            'processor_type': 'MPC8572',
            'rtr_type': 'WS-C4510R+E',
            'chassis_sn': 'JAD213101PP',
            'processor': {
                'cpu_type': 'MPC8572',
                'speed': '1.5GHz',
                'supervisor': '7'
            },
            'number_of_intfs': {
                'Virtual Ethernet': '8',
                'Gigabit Ethernet': '384',
                'Ten Gigabit Ethernet': '8'
            },
            'mem_size': {
                'non-volatile configuration': '511'
            },
            'curr_config_register': '0x2102'
        }
    }

    
    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        version_obj = ShowVersion(device=self.dev1)
        with self.assertRaises(AttributeError):
            parsered_output = version_obj.parse()

    def test_semi_empty(self):
        self.dev2 = Mock(**self.semi_empty_output)
        version_obj = ShowVersion(device=self.dev2)
        with self.assertRaises(KeyError):
            parsed_output = version_obj.parse()

    def test_golden_asr1k(self):
        self.maxDiff = None
        self.dev_asr1k = Mock(**self.golden_output_asr1k)
        version_obj = ShowVersion(device=self.dev_asr1k)
        parsed_output = version_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_asr1k)

    def test_golden_c3850(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_c3850)
        version_obj = ShowVersion(device=self.dev_c3850)
        parsed_output = version_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_c3850)

    def test_golden_isr4k(self):
        self.maxDiff = None
        self.dev_isr4k = Mock(**self.golden_output_isr4k)
        version_obj = ShowVersion(device=self.dev_isr4k)
        parsed_output = version_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_isr4k)

    def test_golden_asr901(self):
        self.maxDiff = None
        self.dev_asr901 = Mock(**self.golden_output_asr901)
        version_obj = ShowVersion(device=self.dev_asr901)
        parsed_output = version_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_asr901)

    def test_golden_c4507(self):
        self.maxDiff = None
        self.dev_c4k = Mock(**self.golden_output_c4507)
        obj = ShowVersion(device=self.dev_c4k)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_c4507)

    def test_golden_1(self):
        self.maxDiff = None
        self.dev_1 = Mock(**self.golden_output_1)
        obj = ShowVersion(device=self.dev_1)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

class TestDir(unittest.TestCase):
    dev1 = Device(name='empty')
    dev2 = Device(name='semi_empty')
    dev_asr1k = Device(name='asr1k')
    dev_c3850 = Device(name='c3850')
    empty_output = {'execute.return_value': ''}
    semi_empty_output = {'execute.return_value': '''\
Directory of flash:/
'''}

    golden_parsed_output_c3850 = {
                                    'dir': {
                                        'dir': 'flash:/',
                                        'flash:/': {
                                            'files': {
                                                'bootloader_evt_handle.log': {
                                                    'index': '30530',
                                                    'permissions': '-rw-',
                                                    'size': '16872',
                                                    'last_modified_date': 'Apr 10 2017 17:20:51 +00:00',
                                                },
                                                'core': {
                                                    'index': '30531',
                                                    'permissions': 'drwx',
                                                    'size': '4096',
                                                    'last_modified_date': 'Apr 10 2017 00:17:34 +00:00',
                                                },
                                                '.prst_sync': {
                                                    'index': '30532',
                                                    'permissions': 'drwx',
                                                    'size': '4096',
                                                    'last_modified_date': 'Apr 10 2017 14:35:35 +00:00',
                                                },
                                                '.rollback_timer': {
                                                    'index': '30534',
                                                    'permissions': 'drwx',
                                                    'size': '4096',
                                                    'last_modified_date': 'Jan 15 2017 20:53:32 +00:00',
                                                },
                                                'dc_profile_dir': {
                                                    'index': '30535',
                                                    'permissions': 'drwx',
                                                    'size': '4096',
                                                    'last_modified_date': 'Apr 10 2017 17:21:10 +00:00',
                                                },
                                                'gs_script': {
                                                    'index': '30537',
                                                    'permissions': 'drwx',
                                                    'size': '4096',
                                                    'last_modified_date': 'Jan 15 2017 20:53:40 +00:00',
                                                },
                                                'memleak.tcl': {
                                                    'index': '30540',
                                                    'permissions': '-rw-',
                                                    'size': '65301',
                                                    'last_modified_date': 'Apr 10 2017 17:21:27 +00:00',
                                                },
                                                'boothelper.log': {
                                                    'index': '30542',
                                                    'permissions': '-rw-',
                                                    'size': '66',
                                                    'last_modified_date': 'Apr 10 2017 17:21:28 +00:00',
                                                },
                                                '.installer': {
                                                    'index': '30541',
                                                    'permissions': 'drwx',
                                                    'size': '4096',
                                                    'last_modified_date': 'Jan 15 2017 20:54:21 +00:00',
                                                },
                                                'nvram_config': {
                                                    'index': '30539',
                                                    'permissions': '-rw-',
                                                    'size': '2097152',
                                                    'last_modified_date': 'Apr 10 2017 17:25:37 +00:00',
                                                },
                                                'tools': {
                                                    'index': '68689',
                                                    'permissions': 'drwx',
                                                    'size': '4096',
                                                    'last_modified_date': 'Mar 18 2017 20:39:57 +00:00',
                                                },
                                                'mscfips_post_test.dbg': {
                                                    'index': '30544',
                                                    'permissions': '-rw-',
                                                    'size': '17500',
                                                    'last_modified_date': 'Apr 10 2017 17:23:01 +00:00',
                                                },
                                                'vlan.dat': {
                                                    'index': '30548',
                                                    'permissions': '-rw-',
                                                    'size': '3436',
                                                    'last_modified_date': 'Apr 10 2017 11:52:23 +00:00',
                                                },
                                                'mscfips_post_test.output': {
                                                    'index': '30545',
                                                    'permissions': '-rw-',
                                                    'size': '6856',
                                                    'last_modified_date': 'Apr 10 2017 17:23:01 +00:00',
                                                },
                                                'pnp-tech-time': {
                                                    'index': '30546',
                                                    'permissions': '-rw-',
                                                    'size': '35',
                                                    'last_modified_date': 'Apr 10 2017 17:25:57 +00:00',
                                                },
                                                'ISSUCleanGolden': {
                                                    'index': '30550',
                                                    'permissions': '-rw-',
                                                    'size': '630812001',
                                                    'last_modified_date': 'Jan 16 2017 11:05:56 +00:00',
                                                },
                                                'pnp-tech-discovery-summary': {
                                                    'index': '30547',
                                                    'permissions': '-rw-',
                                                    'size': '21107',
                                                    'last_modified_date': 'Apr 10 2017 17:26:38 +00:00',
                                                },
                                                'onep': {
                                                    'index': '30552',
                                                    'permissions': 'drwx',
                                                    'size': '4096',
                                                    'last_modified_date': 'Jan 17 2017 10:21:50 +00:00',
                                                },
                                            },
                                            'bytes_total': '1598627840',
                                            'bytes_free': '880939008',
                                        },
                                    }
                                }

    golden_output_c3850 = {'execute.return_value': '''\
Directory of flash:/

30530  -rw-            16872  Apr 10 2017 17:20:51 +00:00  bootloader_evt_handle.log
30531  drwx             4096  Apr 10 2017 00:17:34 +00:00  core
30532  drwx             4096  Apr 10 2017 14:35:35 +00:00  .prst_sync
30534  drwx             4096  Jan 15 2017 20:53:32 +00:00  .rollback_timer
30535  drwx             4096  Apr 10 2017 17:21:10 +00:00  dc_profile_dir
30537  drwx             4096  Jan 15 2017 20:53:40 +00:00  gs_script
30540  -rw-            65301  Apr 10 2017 17:21:27 +00:00  memleak.tcl
30542  -rw-               66  Apr 10 2017 17:21:28 +00:00  boothelper.log
30541  drwx             4096  Jan 15 2017 20:54:21 +00:00  .installer
30539  -rw-          2097152  Apr 10 2017 17:25:37 +00:00  nvram_config
68689  drwx             4096  Mar 18 2017 20:39:57 +00:00  tools
30544  -rw-            17500  Apr 10 2017 17:23:01 +00:00  mscfips_post_test.dbg
30548  -rw-             3436  Apr 10 2017 11:52:23 +00:00  vlan.dat
30545  -rw-             6856  Apr 10 2017 17:23:01 +00:00  mscfips_post_test.output
30546  -rw-               35  Apr 10 2017 17:25:57 +00:00  pnp-tech-time
30550  -rw-        630812001  Jan 16 2017 11:05:56 +00:00  ISSUCleanGolden
30547  -rw-            21107  Apr 10 2017 17:26:38 +00:00  pnp-tech-discovery-summary
30552  drwx             4096  Jan 17 2017 10:21:50 +00:00  onep

1598627840 bytes total (880939008 bytes free)
'''}

    golden_parsed_output_asr1k = {
                                    'dir': {
                                        'dir': 'bootflash:/',
                                        'bootflash:/': {
                                            'bytes_free': '1036210176',
                                            'bytes_total': '1940303872',
                                            'files': {
                                                'lost+found': {
                                                    'index': '11',
                                                    'permissions': 'drwx',
                                                    'size': '16384',
                                                    'last_modified_date': 'Nov 25 2016 19:32:53 -07:00',
                                                },
                                                'ds_stats.txt': {
                                                    'index': '12',
                                                    'permissions': '-rw-',
                                                    'size': '0',
                                                    'last_modified_date': 'Dec 13 2016 11:36:36 -07:00',
                                                },
                                                '.prst_sync': {
                                                    'index': '104417',
                                                    'permissions': 'drwx',
                                                    'size': '4096',
                                                    'last_modified_date': 'Apr 10 2017 09:09:11 -07:00',
                                                },
                                                '.rollback_timer': {
                                                    'index': '80321',
                                                    'permissions': 'drwx',
                                                    'size': '4096',
                                                    'last_modified_date': 'Nov 25 2016 19:40:38 -07:00',
                                                },
                                                '.installer': {
                                                    'index': '64257',
                                                    'permissions': 'drwx',
                                                    'size': '4096',
                                                    'last_modified_date': 'Nov 25 2016 19:41:02 -07:00',
                                                },
                                                'virtual-instance-stby-sync': {
                                                    'index': '48193',
                                                    'permissions': 'drwx',
                                                    'size': '4096',
                                                    'last_modified_date': 'Nov 25 2016 19:41:14 -07:00',
                                                },
                                                'onep': {
                                                    'index': '8033',
                                                    'permissions': 'drwx',
                                                    'size': '4096',
                                                    'last_modified_date': 'Nov 25 2016 18:42:07 -07:00',
                                                },
                                                'pnp-tech-time': {
                                                    'index': '13',
                                                    'permissions': '-rw-',
                                                    'size': '35',
                                                    'last_modified_date': 'Apr 10 2017 09:11:45 -07:00',
                                                },
                                                'pnp-tech-discovery-summary': {
                                                    'index': '14',
                                                    'permissions': '-rw-',
                                                    'size': '19957',
                                                    'last_modified_date': 'Apr 10 2017 09:13:55 -07:00',
                                                },
                                                'aaa1': {
                                                    'index': '15',
                                                    'permissions': '-rw-',
                                                    'size': '24970',
                                                    'last_modified_date': 'Dec 13 2016 12:07:18 -07:00',
                                                },
                                                'crashinfo_RP_00_00_20170203-155749-PDT': {
                                                    'index': '16',
                                                    'permissions': '-rw-',
                                                    'size': '177449',
                                                    'last_modified_date': 'Feb 3 2017 15:57:50 -07:00',
                                                },
                                                'crashinfo_RP_00_00_20170206-122158-PDT': {
                                                    'index': '17',
                                                    'permissions': '-rw-',
                                                    'size': '168196',
                                                    'last_modified_date': 'Feb 6 2017 12:21:59 -07:00',
                                                },
                                                'crashinfo_RP_00_00_20170206-172530-PDT': {
                                                    'index': '18',
                                                    'permissions': '-rw-',
                                                    'size': '163081',
                                                    'last_modified_date': 'Feb 6 2017 17:25:31 -07:00',
                                                },
                                                'crashinfo_RP_00_00_20170207-133017-PDT': {
                                                    'index': '19',
                                                    'permissions': '-rw-',
                                                    'size': '160713',
                                                    'last_modified_date': 'Feb 7 2017 13:30:18 -07:00',
                                                },
                                                'crashinfo_RP_00_00_20170208-180855-PDT': {
                                                    'index': '20',
                                                    'permissions': '-rw-',
                                                    'size': '177276',
                                                    'last_modified_date': 'Feb 8 2017 18:08:56 -07:00',
                                                },
                                                'crashinfo_RP_00_00_20170210-120312-PDT': {
                                                    'index': '21',
                                                    'permissions': '-rw-',
                                                    'size': '160725',
                                                    'last_modified_date': 'Feb 10 2017 12:03:13 -07:00',
                                                },
                                                'crashinfo_RP_00_00_20170210-163201-PDT': {
                                                    'index': '22',
                                                    'permissions': '-rw-',
                                                    'size': '163143',
                                                    'last_modified_date': 'Feb 10 2017 16:32:02 -07:00',
                                                },
                                                'crashinfo_RP_00_00_20170213-112420-PDT': {
                                                    'index': '23',
                                                    'permissions': '-rw-',
                                                    'size': '168245',
                                                    'last_modified_date': 'Feb 13 2017 11:24:21 -07:00',
                                                },
                                                'testimage': {
                                                    'index': '24',
                                                    'permissions': '-rw-',
                                                    'size': '794609595',
                                                    'last_modified_date': 'Feb 17 2017 11:50:21 -07:00',
                                                },
                                                'crashinfo_RP_00_00_20170307-043013-PDT': {
                                                    'index': '25',
                                                    'permissions': '-rw-',
                                                    'size': '167767',
                                                    'last_modified_date': 'Mar 7 2017 04:30:14 -07:00',
                                                },
                                                'crashinfo_RP_00_00_20170307-165741-PDT': {
                                                    'index': '28',
                                                    'permissions': '-rw-',
                                                    'size': '163152',
                                                    'last_modified_date': 'Mar 7 2017 16:57:42 -07:00',
                                                },
                                                'kak1': {
                                                    'index': '37',
                                                    'permissions': '-rw-',
                                                    'size': '25189',
                                                    'last_modified_date': 'Dec 14 2016 09:15:37 -07:00',
                                                },
                                            }
                                        }
                                    }
                                }

    golden_output_asr1k = {'execute.return_value': '''\
Directory of bootflash:/

   11  drwx            16384  Nov 25 2016 19:32:53 -07:00  lost+found
   12  -rw-                0  Dec 13 2016 11:36:36 -07:00  ds_stats.txt
104417  drwx             4096  Apr 10 2017 09:09:11 -07:00  .prst_sync
80321  drwx             4096  Nov 25 2016 19:40:38 -07:00  .rollback_timer
64257  drwx             4096  Nov 25 2016 19:41:02 -07:00  .installer
48193  drwx             4096  Nov 25 2016 19:41:14 -07:00  virtual-instance-stby-sync
 8033  drwx             4096  Nov 25 2016 18:42:07 -07:00  onep
   13  -rw-               35  Apr 10 2017 09:11:45 -07:00  pnp-tech-time
   14  -rw-            19957  Apr 10 2017 09:13:55 -07:00  pnp-tech-discovery-summary
   15  -rw-            24970  Dec 13 2016 12:07:18 -07:00  aaa1
   16  -rw-           177449   Feb 3 2017 15:57:50 -07:00  crashinfo_RP_00_00_20170203-155749-PDT
   17  -rw-           168196   Feb 6 2017 12:21:59 -07:00  crashinfo_RP_00_00_20170206-122158-PDT
   18  -rw-           163081   Feb 6 2017 17:25:31 -07:00  crashinfo_RP_00_00_20170206-172530-PDT
   19  -rw-           160713   Feb 7 2017 13:30:18 -07:00  crashinfo_RP_00_00_20170207-133017-PDT
   20  -rw-           177276   Feb 8 2017 18:08:56 -07:00  crashinfo_RP_00_00_20170208-180855-PDT
   21  -rw-           160725  Feb 10 2017 12:03:13 -07:00  crashinfo_RP_00_00_20170210-120312-PDT
   22  -rw-           163143  Feb 10 2017 16:32:02 -07:00  crashinfo_RP_00_00_20170210-163201-PDT
   23  -rw-           168245  Feb 13 2017 11:24:21 -07:00  crashinfo_RP_00_00_20170213-112420-PDT
   24  -rw-        794609595  Feb 17 2017 11:50:21 -07:00  testimage
   25  -rw-           167767   Mar 7 2017 04:30:14 -07:00  crashinfo_RP_00_00_20170307-043013-PDT
   28  -rw-           163152   Mar 7 2017 16:57:42 -07:00  crashinfo_RP_00_00_20170307-165741-PDT
   37  -rw-            25189  Dec 14 2016 09:15:37 -07:00  kak1

1940303872 bytes total (1036210176 bytes free)
'''}

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        dir_obj = Dir(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = dir_obj.parse()

    def test_semi_empty(self):
        self.dev2 = Mock(**self.semi_empty_output)
        dir_obj = Dir(device=self.dev2)
        # with self.assertRaises(SchemaMissingKeyError):
        with self.assertRaises(Exception):
            parsed_output = dir_obj.parse()

    def test_golden_c3850(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_c3850)
        dir_obj = Dir(device=self.dev_c3850)
        parsed_output = dir_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_c3850)

    def test_golden_asr1k(self):
        self.maxDiff = None
        self.dev_asr1k = Mock(**self.golden_output_asr1k)
        dir_obj = Dir(device=self.dev_asr1k)
        parsed_output = dir_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_asr1k)

    def test_golden_asr1k_with_arg(self):
        self.maxDiff = None
        self.dev_asr1k = Mock(**self.golden_output_asr1k)
        dir_obj = Dir(device=self.dev_asr1k)
        parsed_output = dir_obj.parse(directory='bootflash:/')
        self.assertEqual(parsed_output, self.golden_parsed_output_asr1k)


class TestShowRedundancy(unittest.TestCase):
    dev1 = Device(name='empty')
    dev2 = Device(name='semi_empty')
    dev_asr1k = Device(name='asr1k')
    dev_c3850 = Device(name='c3850')
    dev_asr1002 = Device(name='asr1002')
    empty_output = {'execute.return_value': ''}
    semi_empty_output = {'execute.return_value': '''\
Redundant System Information :
------------------------------
       Available system uptime = 1 hour, 32 minutes
Switchovers system experienced = 0
'''}

    golden_parsed_output_c3850 = {
                                    'red_sys_info': {
                                        'available_system_uptime': '1 hour, 32 minutes',
                                        'switchovers_system_experienced': '0',
                                        'standby_failures': '0',
                                        'last_switchover_reason': 'none',
                                        'hw_mode': 'Simplex',
                                        'conf_red_mode': 'sso',
                                        'oper_red_mode': 'Non-redundant',
                                        'maint_mode': 'Disabled',
                                        'communications': 'Down',
                                        'communications_reason': 'Failure',
                                    },
                                    'slot': {
                                        'slot 1': {
                                            'curr_sw_state': 'ACTIVE',
                                            'uptime_in_curr_state': '1 hour, 31 minutes',
                                            'image_ver': 'Cisco IOS Software [Everest], Catalyst L3 Switch Software (CAT3K_CAA-UNIVERSALK9-M), Experimental Version 16.4.20170410:165034 [v164_throttle-BLD-BLD_V164_THROTTLE_LATEST_20170410_174845 105]',
                                            'boot': 'tftp://10.1.6.241//auto/tftp-ssr/Edison/cat3k_caa-universalk9.BLD_V164_THROTTLE_LATEST_20170410_174845.SSA.bin',
                                            'config_register': '0x102',
                                        }
                                    }
                                }

    golden_output_c3850 = {'execute.return_value': '''\
Redundant System Information :
------------------------------
       Available system uptime = 1 hour, 32 minutes
Switchovers system experienced = 0
              Standby failures = 0
        Last switchover reason = none

                 Hardware Mode = Simplex
    Configured Redundancy Mode = sso
     Operating Redundancy Mode = Non-redundant
              Maintenance Mode = Disabled
                Communications = Down      Reason: Failure

Current Processor Information :
-------------------------------
               Active Location = slot 1
        Current Software state = ACTIVE
       Uptime in current state = 1 hour, 31 minutes
                 Image Version = Cisco IOS Software [Everest], Catalyst L3 Switch Software (CAT3K_CAA-UNIVERSALK9-M), Experimental Version 16.4.20170410:165034 [v164_throttle-BLD-BLD_V164_THROTTLE_LATEST_20170410_174845 105]
Copyright (c) 1986-2017 by Cisco Systems, Inc.
Compiled Mon 10-Apr-17 13:02 by mcpre
                          BOOT = tftp://10.1.6.241//auto/tftp-ssr/Edison/cat3k_caa-universalk9.BLD_V164_THROTTLE_LATEST_20170410_174845.SSA.bin
        Configuration register = 0x102

Peer (slot: 0) information is not available because it is in 'DISABLED' state
'''}

    golden_parsed_output_asr1k = {
                                    'red_sys_info': {
                                        'available_system_uptime': '15 hours, 4 minutes',
                                        'switchovers_system_experienced': '0',
                                        'standby_failures': '0',
                                        'last_switchover_reason': 'none',
                                        'hw_mode': 'Duplex',
                                        'conf_red_mode': 'sso',
                                        'oper_red_mode': 'sso',
                                        'maint_mode': 'Disabled',
                                        'communications': 'Up',
                                        },
                                    'slot': {
                                        'slot 6': {
                                            'curr_sw_state': 'ACTIVE',
                                            'uptime_in_curr_state': '15 hours, 4 minutes',
                                            'image_ver': 'Cisco IOS Software [Everest], ASR1000 Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Experimental Version 16.4.20170425:070036 [v164_throttle-BLD-BLD_V164_THROTTLE_LATEST_20170425_075354 141]',
                                            'boot': 'harddisk:test-image-PE1-13116843,12;',
                                            'config_register': '0x2102',
                                        },
                                        'slot 7': {
                                            'curr_sw_state': 'STANDBY HOT',
                                            'uptime_in_curr_state': '15 hours, 1 minute',
                                            'image_ver': 'Cisco IOS Software [Everest], ASR1000 Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Experimental Version 16.4.20170425:070036 [v164_throttle-BLD-BLD_V164_THROTTLE_LATEST_20170425_075354 141]',
                                            'boot': 'harddisk:test-image-PE1-13116843,12;',
                                            'config_register': '0x2102',
                                        },
                                    }
                                }

    golden_output_asr1k = {'execute.return_value': '''\
Redundant System Information :
------------------------------
       Available system uptime = 15 hours, 4 minutes
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
       Uptime in current state = 15 hours, 4 minutes
                 Image Version = Cisco IOS Software [Everest], ASR1000 Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Experimental Version 16.4.20170425:070036 [v164_throttle-BLD-BLD_V164_THROTTLE_LATEST_20170425_075354 141]
Copyright (c) 1986-2017 by Cisco Systems, Inc.
Compiled Tue 25-Apr-17 06:17 by mcpre
                          BOOT = harddisk:test-image-PE1-13116843,12;
                   CONFIG_FILE = 
        Configuration register = 0x2102

Peer Processor Information :
----------------------------
              Standby Location = slot 7
        Current Software state = STANDBY HOT 
       Uptime in current state = 15 hours, 1 minute
                 Image Version = Cisco IOS Software [Everest], ASR1000 Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Experimental Version 16.4.20170425:070036 [v164_throttle-BLD-BLD_V164_THROTTLE_LATEST_20170425_075354 141]
Copyright (c) 1986-2017 by Cisco Systems, Inc.
Compiled Tue 25-Apr-17 06:17 by mcpre
                          BOOT = harddisk:test-image-PE1-13116843,12;
                   CONFIG_FILE = 
        Configuration register = 0x2102
'''}

    golden_parsed_output_asr1002 = {
        'red_sys_info': {
            'available_system_uptime': '11 weeks, 2 days, 3 hours, 0 minutes',
            'communications': 'Down',
            'communications_reason': 'Failure',
            'conf_red_mode': 'Non-redundant',
            'hw_mode': 'Simplex',
            'last_switchover_reason': 'none',
            'maint_mode': 'Disabled',
            'oper_red_mode': 'Non-redundant',
            'standby_failures': '0',
            'switchovers_system_experienced': '0'
        },
        'slot': {
            'slot 6': {
                'boot': 'bootflash:asr1002x-universalk10.144.1.1.S.154-3.S9-ext.SPA.bin,1;bootflash:,1;',
                'config_register': '0x1000',
                'curr_sw_state': 'ACTIVE',
                'image_ver': 'Cisco IOS Software, ASR1000 Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 15.4(3)S9, RELEASE SOFTWARE (fc2)',
                'uptime_in_curr_state': '11 weeks, 2 days, 2 hours, 59 minutes'
            }
        }
    }

    golden_output_asr1002 = {'execute.return_value': '''\
    +++ router: executing command 'show redundancy' +++
    show redundancy
    Redundant System Information :
    ------------------------------
           Available system uptime = 11 weeks, 2 days, 3 hours, 0 minutes
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
                   Active Location = slot 6
            Current Software state = ACTIVE
           Uptime in current state = 11 weeks, 2 days, 2 hours, 59 minutes
                     Image Version = Cisco IOS Software, ASR1000 Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 15.4(3)S9, RELEASE SOFTWARE (fc2)
    Technical Support: http://www.cisco.com/techsupport
    Copyright (c) 1986-2018 by Cisco Systems, Inc.
    Compiled Mon 26-Feb-18 10:00 by mcpre
                              BOOT = bootflash:asr1002x-universalk10.144.1.1.S.154-3.S9-ext.SPA.bin,1;bootflash:,1;
            Configuration register = 0x1000

    Peer (slot: 7) information is not available because it is in 'DISABLED' state
'''}



    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        redundancy_obj = ShowRedundancy(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = redundancy_obj.parse()

    def test_semi_empty(self):
        self.dev2 = Mock(**self.semi_empty_output)
        redundancy_obj = ShowRedundancy(device=self.dev2)
        # with self.assertRaises(SchemaMissingKeyError):
        with self.assertRaises(Exception):
            parsed_output = redundancy_obj.parse()

    def test_golden_c3850(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_c3850)
        redundancy_obj = ShowRedundancy(device=self.dev_c3850)
        parsed_output = redundancy_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_c3850)

    def test_golden_asr1k(self):
        self.maxDiff = None
        self.dev_asr1k = Mock(**self.golden_output_asr1k)
        redundancy_obj = ShowRedundancy(device=self.dev_asr1k)
        parsed_output = redundancy_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_asr1k)

    def test_golden_asr1002(self):
        self.maxDiff = None
        self.dev_asr1002 = Mock(**self.golden_output_asr1002)
        redundancy_obj = ShowRedundancy(device=self.dev_asr1002)
        parsed_output = redundancy_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_asr1002)


class TestShowRedundancy2(unittest.TestCase):
    dev = Device(name='aDevice')
    
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        "my_state": "13 -ACTIVE",
        "peer_state": "1  -DISABLED",
        "mode": "Simplex",
        "unit": "Primary",
        "unit_id": 48,
        "redundancy_mode_operational": "Non-redundant",
        "redundancy_mode_configured": "Non-redundant",
        "redundancy_state": "Non Redundant",
        "maintenance_mode": "Disabled",
        "manual_swact": "disabled",
        "manual_swact_reason": "system is simplex (no peer unit)",
        "communications": "Down",
        "communications_reason": "Simplex mode",
        "client_count": 111,
        "client_notification_tmr_msec": 30000,
        "rf_debug_mask": "0x0"
    }

    golden_output1 = {'execute.return_value': '''
    PE1#show redundancy states 
    Load for five secs: 2%/0%; one minute: 1%; five minutes: 1%
    Time source is NTP, 05:47:45.686 EST Thu Jun 6 2019
           my state = 13 -ACTIVE 
         peer state = 1  -DISABLED 
               Mode = Simplex
               Unit = Primary
            Unit ID = 48

    Redundancy Mode (Operational) = Non-redundant
    Redundancy Mode (Configured)  = Non-redundant
    Redundancy State              = Non Redundant
         Maintenance Mode = Disabled
        Manual Swact = disabled (system is simplex (no peer unit))
     Communications = Down      Reason: Simplex mode

       client count = 111
     client_notification_TMR = 30000 milliseconds
               RF debug mask = 0x0   

    PE1#
    '''}

    golden_parsed_output2 = {
        "my_state": "13 -ACTIVE",
        "peer_state": "8  -STANDBY HOT",
        "mode": "Duplex",
        "unit": "Primary",
        "unit_id": 48,
        "redundancy_mode_operational": "sso",
        "redundancy_mode_configured": "sso",
        "redundancy_state": "sso",
        "maintenance_mode": "Disabled",
        "manual_swact": "enabled",
        "communications": "Up",
        "client_count": 76,
        "client_notification_tmr_msec": 30000,
        "rf_debug_mask": "0x0"
    }

    golden_output2 = {'execute.return_value': '''
    asr104#show redundancy states 
           my state = 13 -ACTIVE 
         peer state = 8  -STANDBY HOT 
               Mode = Duplex
               Unit = Primary
            Unit ID = 48

    Redundancy Mode (Operational) = sso
    Redundancy Mode (Configured)  = sso
    Redundancy State              = sso
         Maintenance Mode = Disabled
        Manual Swact = enabled
     Communications = Up

       client count = 76
     client_notification_TMR = 30000 milliseconds
               RF debug mask = 0x0   

    asr104#
    '''}


    golden_output3 = {'execute.return_value': '''
    show redundancy states
    my state = 13 -ACTIVE 
    peer state = 1  -DISABLED 
    Mode = Simplex
    Unit = Primary
    Unit ID = 48
    Redundancy Mode (Operational) = Non-redundant
    Redundancy Mode (Configured)  = sso
    Redundancy State              = Non Redundant
    Manual Swact = disabled (system is simplex (no peer unit))
    Communications = Down      Reason: Simplex mode
    client count = 84
    client_notification_TMR = 30000 milliseconds
    RF debug mask = 0x0   
    '''}

    golden_parsed_output3 = {
        'my_state': '13 -ACTIVE',
        'peer_state': '1  -DISABLED',
        'mode': 'Simplex',
        'unit': 'Primary',
        'unit_id': 48,
        'redundancy_mode_operational': 'Non-redundant',
        'redundancy_mode_configured': 'sso',
        'redundancy_state': 'Non Redundant',
        'manual_swact': 'disabled',
        'manual_swact_reason': 'system is simplex (no peer unit)',
        'communications': 'Down',
        'communications_reason': 'Simplex mode',
        'client_count': 84,
        'client_notification_tmr_msec': 30000,
        'rf_debug_mask': '0x0',
    }

    def test_empty(self):
        self.dev = Mock(**self.empty_output)
        redundancy_obj = ShowRedundancyStates(device=self.dev)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = redundancy_obj.parse()

    def test_golden1(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output1)
        redundancy_obj = ShowRedundancyStates(device=self.dev)
        parsed_output = redundancy_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_golden2(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output2)
        redundancy_obj = ShowRedundancyStates(device=self.dev)
        parsed_output = redundancy_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_golden3(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output3)
        redundancy_obj = ShowRedundancyStates(device=self.dev)
        parsed_output = redundancy_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output3)


# ====================
# Unit test for:
#   * 'show inventory'
# ====================
class TestShowInventory(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output_c3850 = {
        'main': 
            {'swstack': True,
            },
        'slot': 
            {'1': 
                {'rp': 
                    {'WS-C3850-24P-E': 
                        {'name': 'Switch 1',
                        'descr': 'WS-C3850-24P-E',
                        'pid': 'WS-C3850-24P-E',
                        'vid': 'V01',
                        'sn': 'FCW1932D0LB',
                        'subslot': 
                            {'1': 
                                {'STACK-T1-50CM': 
                                    {'name': 'StackPort1/1',
                                    'descr': 'StackPort1/1',
                                    'pid': 'STACK-T1-50CM',
                                    'vid': 'V01',
                                    'sn': 'LCC1921G11G',
                                    },
                                },
                            '2': 
                                {'STACK-T1-50CM': 
                                    {'name': 'StackPort1/2',
                                    'descr': 'StackPort1/2',
                                    'pid': 'STACK-T1-50CM',
                                    'vid': 'V01',
                                    'sn': 'LCC1921G250',
                                    },
                                },
                            },
                        },
                    },
                'other': 
                    {'C3KX-PWR-715WAC': 
                        {'name': 'Switch 1 - Power Supply A',
                        'descr': 'Switch 1 - Power Supply A',
                        'pid': 'C3KX-PWR-715WAC',
                        'vid': 'V01',
                        'sn': 'LIT14291MTJ',
                        },
                    },
                },
            '2': 
                {'rp': 
                    {'WS-C3850-24P-E': 
                        {'name': 'Switch 2',
                        'descr': 'WS-C3850-24P-E',
                        'pid': 'WS-C3850-24P-E',
                        'vid': 'V04',
                        'sn': 'FOC1932X0K1',
                        'subslot': 
                            {'1': 
                                {'STACK-T1-50CM': 
                                    {'name': 'StackPort2/1',
                                    'descr': 'StackPort2/1',
                                    'pid': 'STACK-T1-50CM',
                                    'vid': 'V01',
                                    'sn': 'MOC1932A0BU',
                                    },
                                },
                            '2': 
                                {'STACK-T1-50CM': 
                                    {'name': 'StackPort2/2',
                                    'descr': 'StackPort2/2',
                                    'pid': 'STACK-T1-50CM',
                                    'vid': 'V01',
                                    'sn': 'LCC1921G10J',
                                    },
                                },
                            },
                        },
                    },
                'other': 
                    {'C3KX-PWR-715WAC': 
                        {'name': 'Switch 2 - Power Supply A',
                        'descr': 'Switch 2 - Power Supply A',
                        'pid': 'C3KX-PWR-715WAC',
                        'vid': 'V01',
                        'sn': 'LIT15090DUL',
                        },
                    },
                },
            '3': 
                {'rp': 
                    {'WS-C3850-24P-E': 
                        {'name': 'Switch 3',
                        'descr': 'WS-C3850-24P-E',
                        'pid': 'WS-C3850-24P-E',
                        'vid': 'V04',
                        'sn': 'FCW1932C0MA',
                        'subslot': 
                            {'1': 
                                {'STACK-T1-50CM': 
                                    {'name': 'StackPort3/1',
                                    'descr': 'StackPort3/1',
                                    'pid': 'STACK-T1-50CM',
                                    'vid': 'V01',
                                    'sn': 'LCC1921G10J',
                                    },
                                },
                            '2': 
                                {'STACK-T1-50CM': 
                                    {'name': 'StackPort3/2',
                                    'descr': 'StackPort3/2',
                                    'pid': 'STACK-T1-50CM',
                                    'vid': 'V01',
                                    'sn': 'LCC1921G106',
                                    },
                                },
                            },
                        },
                    },
                'other': 
                    {'PWR-C1-715WAC': 
                        {'name': 'Switch 3 - Power Supply A',
                        'descr': 'Switch 3 - Power Supply A',
                        'pid': 'PWR-C1-715WAC',
                        'vid': 'V01',
                        'sn': 'LIT19220MG1',
                        },
                    },
                },
            '4': 
                {'rp': 
                    {'WS-C3850-24P-E': 
                        {'name': 'Switch 4',
                        'descr': 'WS-C3850-24P-E',
                        'pid': 'WS-C3850-24P-E',
                        'vid': 'V04',
                        'sn': 'FCW1932D0L0',
                        'subslot': 
                            {'1': 
                                {'STACK-T1-50CM': 
                                    {'name': 'StackPort4/1',
                                    'descr': 'StackPort4/1',
                                    'pid': 'STACK-T1-50CM',
                                    'vid': 'V01',
                                    'sn': 'LCC1921G250',
                                    },
                                },
                            '2': 
                                {'STACK-T1-50CM': 
                                    {'name': 'StackPort4/2',
                                    'descr': 'StackPort4/2',
                                    'pid': 'STACK-T1-50CM',
                                    'vid': 'V01',
                                    'sn': 'MOC1932A0BU',
                                    },
                                },
                            },
                        },
                    },
                'other': 
                    {'C3KX-PWR-715WAC': 
                        {'name': 'Switch 4 - Power Supply A',
                        'descr': '',
                        'pid': 'C3KX-PWR-715WAC',
                        'vid': 'V01',
                        'sn': 'LIT15140DEP',
                        },
                    },
                },
            '5': 
                {'rp': 
                    {'WS-C3850-24P-E': 
                        {'name': 'Switch 5',
                        'descr': 'WS-C3850-24P-E',
                        'pid': 'WS-C3850-24P-E',
                        'vid': 'V04',
                        'sn': 'FOC1932X0F9',
                        'subslot': 
                            {'1': 
                                {'STACK-T1-50CM': 
                                    {'name': 'StackPort5/1',
                                    'descr': 'StackPort5/1',
                                    'pid': 'STACK-T1-50CM',
                                    'vid': 'V01',
                                    'sn': 'LCC1921G106',
                                    },
                                },
                            '2': 
                                {'STACK-T1-50CM': 
                                    {'name': 'StackPort5/2',
                                    'descr': 'StackPort5/2',
                                    'pid': 'STACK-T1-50CM',
                                    'vid': 'V01',
                                    'sn': 'LCC1921G11G',
                                    },
                                },
                            },
                        },
                    },
                'other': 
                    {'PWR-C1-715WAC': 
                        {'name': 'Switch 5 - Power Supply A',
                        'descr': 'Switch 5 - Power Supply A',
                        'pid': 'PWR-C1-715WAC',
                        'vid': 'V01',
                        'sn': 'LIT17130ZDU',
                        },
                    },
                },
            },
        }

    golden_output_c3850 = {'execute.return_value': '''
        NAME: "c38xx Stack", DESCR: "c38xx Stack"
        PID: WS-C3850-24P-E    , VID: V01  , SN: FCW1932D0LB

        NAME: "Switch 1", DESCR: "WS-C3850-24P-E"
        PID: WS-C3850-24P-E    , VID: V01  , SN: FCW1932D0LB

        NAME: "StackPort1/1", DESCR: "StackPort1/1"
        PID: STACK-T1-50CM     , VID: V01  , SN: LCC1921G11G

        NAME: "StackPort1/2", DESCR: "StackPort1/2"
        PID: STACK-T1-50CM     , VID: V01  , SN: LCC1921G250

        NAME: "Switch 1 - Power Supply A", DESCR: "Switch 1 - Power Supply A"
        PID: C3KX-PWR-715WAC   , VID: V01  , SN: LIT14291MTJ

        NAME: "Switch 2", DESCR: "WS-C3850-24P-E"
        PID: WS-C3850-24P-E    , VID: V04  , SN: FOC1932X0K1

        NAME: "StackPort2/1", DESCR: "StackPort2/1"
        PID: STACK-T1-50CM     , VID: V01  , SN: MOC1932A0BU

        NAME: "StackPort2/2", DESCR: "StackPort2/2"
        PID: STACK-T1-50CM     , VID: V01  , SN: LCC1921G10J

        NAME: "Switch 2 - Power Supply A", DESCR: "Switch 2 - Power Supply A"
        PID: C3KX-PWR-715WAC   , VID: V01  , SN: LIT15090DUL

        NAME: "Switch 3", DESCR: "WS-C3850-24P-E"
        PID: WS-C3850-24P-E    , VID: V04  , SN: FCW1932C0MA

        NAME: "StackPort3/1", DESCR: "StackPort3/1"
        PID: STACK-T1-50CM     , VID: V01  , SN: LCC1921G10J

        NAME: "StackPort3/2", DESCR: "StackPort3/2"
        PID: STACK-T1-50CM     , VID: V01  , SN: LCC1921G106

        NAME: "Switch 3 - Power Supply A", DESCR: "Switch 3 - Power Supply A"
        PID: PWR-C1-715WAC     , VID: V01  , SN: LIT19220MG1

        NAME: "Switch 4", DESCR: "WS-C3850-24P-E"
        PID: WS-C3850-24P-E    , VID: V04  , SN: FCW1932D0L0

        NAME: "StackPort4/1", DESCR: "StackPort4/1"
        PID: STACK-T1-50CM     , VID: V01  , SN: LCC1921G250

        NAME: "StackPort4/2", DESCR: "StackPort4/2"
        PID: STACK-T1-50CM     , VID: V01  , SN: MOC1932A0BU

        NAME: "Switch 4 - Power Supply A", DESCR: ""
        PID: C3KX-PWR-715WAC   , VID: V01  , SN: LIT15140DEP

        NAME: "Switch 5", DESCR: "WS-C3850-24P-E"
        PID: WS-C3850-24P-E    , VID: V04  , SN: FOC1932X0F9

        NAME: "StackPort5/1", DESCR: "StackPort5/1"
        PID: STACK-T1-50CM     , VID: V01  , SN: LCC1921G106

        NAME: "StackPort5/2", DESCR: "StackPort5/2"
        PID: STACK-T1-50CM     , VID: V01  , SN: LCC1921G11G

        NAME: "Switch 5 - Power Supply A", DESCR: "Switch 5 - Power Supply A"
        PID: PWR-C1-715WAC     , VID: V01  , SN: LIT17130ZDU
        '''}

    golden_parsed_output_asr1k = {
        'main': {
            'chassis': {
                'ASR1006': {
                    'descr': 'Cisco ASR1006 Chassis',
                    'name': 'Chassis',
                    'pid': 'ASR1006',
                    'sn': 'FOX1204G6WN',
                    'vid': 'V01'
                }
            }
        },
        'slot': {
            '0': {
                'lc': {
                    'ASR1000-SIP40': {
                        'descr': 'Cisco ASR1000 SPA Interface Processor 40',
                        'name': 'module 0',
                        'pid': 'ASR1000-SIP40',
                        'sn': 'JAE200609WP',
                        'subslot': {
                            '0': {
                                'SPA-5X1GE-V2': {
                                    'descr': '5-port Gigabit Ethernet Shared Port Adapter',
                                    'name': 'SPA subslot 0/0',
                                    'pid': 'SPA-5X1GE-V2',
                                    'sn': 'JAE151203T2',
                                    'vid': 'V02'
                                }
                            },
                            '0 transceiver 0': {
                                'SP7041-E': {
                                    'descr': 'GE T',
                                    'name': 'subslot 0/0 transceiver 0',
                                    'pid': 'SP7041-E',
                                    'sn': 'MTC164204VE',
                                    'vid': 'E'
                                }
                            },
                            '0 transceiver 1': {
                                'SP7041-E': {
                                    'descr': 'GE T',
                                    'name': 'subslot 0/0 transceiver 1',
                                    'pid': 'SP7041-E',
                                    'sn': 'MTC164204F0',
                                    'vid': 'E'
                                }
                            },
                            '0 transceiver 2': {
                                'SP7041-E': {
                                    'descr': 'GE T',
                                    'name': 'subslot 0/0 transceiver 2',
                                    'pid': 'SP7041-E',
                                    'sn': 'MTC164206U2',
                                    'vid': 'E'
                                }
                            },
                            '0 transceiver 3': {
                                'SP7041-E': {
                                    'descr': 'GE T',
                                    'name': 'subslot 0/0 transceiver 3',
                                    'pid': 'SP7041-E',
                                    'sn': 'MTC1644033S',
                                    'vid': 'E'
                                }
                            }
                        },
                        'vid': 'V02'
                    }
                }
            },
            'F0': {
                'other': {
                    'ASR1000-ESP20': {
                        'descr': 'Cisco ASR1000 Embedded Services Processor, 20Gbps',
                        'name': 'module F0',
                        'pid': 'ASR1000-ESP20',
                        'sn': 'JAE1239W7G6',
                        'vid': 'V01'
                    }
                }
            },
            'P0': {
                'other': {
                    'ASR1006-PWR-AC': {
                        'descr': 'Cisco ASR1006 AC Power Supply',
                        'name': 'Power Supply Module 0',
                        'pid': 'ASR1006-PWR-AC',
                        'sn': 'ART1210Q049',
                        'vid': 'V01'
                    }
                }
            },
            'P1': {
                'other': {
                    'ASR1006-PWR-AC': {
                        'descr': 'Cisco ASR1006 AC Power Supply',
                        'name': 'Power Supply Module 1',
                        'pid': 'ASR1006-PWR-AC',
                        'sn': 'ART1210Q04C',
                        'vid': 'V01'
                    }
                }
            },
            'R0': {
                'rp': {
                    'ASR1000-RP2': {
                        'descr': 'Cisco ASR1000 Route Processor 2',
                        'name': 'module R0',
                        'pid': 'ASR1000-RP2',
                        'sn': 'JAE153408NJ',
                        'vid': 'V02'
                    }
                }
            },
            'R1': {
                'rp': {
                    'ASR1000-RP2': {
                        'descr': 'Cisco ASR1000 Route Processor 2',
                        'name': 'module R1',
                        'pid': 'ASR1000-RP2',
                        'sn': 'JAE1703094H',
                        'vid': 'V03'
                    }
                }
            }
        }
    }

    golden_output_asr1k = {'execute.return_value': '''
        NAME: "Chassis", DESCR: "Cisco ASR1006 Chassis"
        PID: ASR1006           , VID: V01  , SN: FOX1204G6WN

        NAME: "module 0", DESCR: "Cisco ASR1000 SPA Interface Processor 40"
        PID: ASR1000-SIP40     , VID: V02  , SN: JAE200609WP

        NAME: "SPA subslot 0/0", DESCR: "5-port Gigabit Ethernet Shared Port Adapter"
        PID: SPA-5X1GE-V2      , VID: V02  , SN: JAE151203T2

        NAME: "subslot 0/0 transceiver 0", DESCR: "GE T"
        PID: SP7041-E          , VID: E    , SN: MTC164204VE     

        NAME: "subslot 0/0 transceiver 1", DESCR: "GE T"
        PID: SP7041-E          , VID: E    , SN: MTC164204F0     

        NAME: "subslot 0/0 transceiver 2", DESCR: "GE T"
        PID: SP7041-E          , VID: E    , SN: MTC164206U2     

        NAME: "subslot 0/0 transceiver 3", DESCR: "GE T"
        PID: SP7041-E          , VID: E    , SN: MTC1644033S     

        NAME: "module R0", DESCR: "Cisco ASR1000 Route Processor 2"
        PID: ASR1000-RP2       , VID: V02  , SN: JAE153408NJ

        NAME: "module R1", DESCR: "Cisco ASR1000 Route Processor 2"
        PID: ASR1000-RP2       , VID: V03  , SN: JAE1703094H

        NAME: "module F0", DESCR: "Cisco ASR1000 Embedded Services Processor, 20Gbps"
        PID: ASR1000-ESP20     , VID: V01  , SN: JAE1239W7G6

        NAME: "Power Supply Module 0", DESCR: "Cisco ASR1006 AC Power Supply"
        PID: ASR1006-PWR-AC    , VID: V01  , SN: ART1210Q049

        NAME: "Power Supply Module 1", DESCR: "Cisco ASR1006 AC Power Supply"
        PID: ASR1006-PWR-AC    , VID: V01  , SN: ART1210Q04C
        '''}

    golden_parsed_output_isr4k = {
        'main': 
            {'chassis': 
                {'ISR4331/K9': 
                    {'sn': 'FDO2201A0SR',
                    'pid': 'ISR4331/K9',
                    'descr': 'Cisco ISR4331 Chassis',
                    'name': 'Chassis',
                    'vid': 'V04',
                    },
                },
            },
        'slot': 
            {'0': 
                {'lc': 
                    {'ISR4331-3x1GE': 
                        {'descr': 'Front Panel 3 ports Gigabitethernet Module',
                        'name': 'NIM subslot 0/0',
                        'pid': 'ISR4331-3x1GE',
                        'sn': '',
                        'subslot': 
                            {'0 transceiver 2': 
                                {'SFP-GE-T': 
                                    {'descr': 'GE T',
                                    'name': 'subslot 0/0 transceiver 2',
                                    'pid': 'SFP-GE-T',
                                    'sn': 'MTC2139029X',
                                    'vid': 'V02'}}},
                        'vid': 'V01'},
                    'ISR4331/K9': 
                        {'descr': 'Cisco ISR4331 Built-In NIM controller',
                        'name': 'module 0',
                        'pid': 'ISR4331/K9',
                        'sn': '',
                        'subslot': 
                            {'1': 
                                {'NIM-ES2-4': 
                                    {'descr': 'NIM-ES2-4',
                                    'name': 'NIM subslot 0/1',
                                    'pid': 'NIM-ES2-4',
                                    'sn': 'FOC21486SRL',
                                    'vid': 'V01'}},
                            '2': 
                                {'NIM-ES2-8': 
                                    {'descr': 'NIM-ES2-8',
                                    'name': 'NIM subslot 0/2',
                                    'pid': 'NIM-ES2-8',
                                    'sn': 'FOC22384AXC',
                                    'vid': 'V01'}}},
                        'vid': ''}}},
            '1': 
                {'lc': 
                    {'ISR4331/K9': 
                        {'sn': '',
                        'pid': 'ISR4331/K9',
                        'descr': 'Cisco ISR4331 Built-In SM controller',
                        'name': 'module 1',
                        'vid': '',
                        },
                    },
                },
            'F0': 
                {'lc': 
                    {'ISR4331/K9': 
                        {'sn': '',
                        'pid': 'ISR4331/K9',
                        'descr': 'Cisco ISR4331 Forwarding Processor',
                        'name': 'module F0',
                        'vid': '',
                        },
                    },
                },
            'P0': 
                {'other': 
                    {'PWR-4330-AC': 
                        {'sn': 'PST2150N1E2',
                        'pid': 'PWR-4330-AC',
                        'descr': '250W AC Power Supply for Cisco ISR 4330',
                        'name': 'Power Supply Module 0',
                        'vid': 'V02',
                        },
                    },
                },
            'Fan_Tray': {
                'other': {
                    'ACS-4330-FANASSY': {
                        'descr': 'Cisco ISR4330 Fan Assembly',
                        'name': 'Fan Tray',
                        'pid': 'ACS-4330-FANASSY',
                        'sn': '',
                        'vid': '',
                    }
                }
            },
            'R0': 
                {'rp': 
                    {'ISR4331/K9': 
                        {'sn': 'FDO21520TGH',
                        'pid': 'ISR4331/K9',
                        'descr': 'Cisco ISR4331 Route Processor',
                        'name': 'module R0',
                        'vid': 'V04',
                        },
                    },
                },
            },
        }

    golden_output_isr4k = {'execute.return_value': '''
        show inventory

        +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        INFO: Please use "show license UDI" to get serial number for licensing.
        +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        NAME: "Chassis", DESCR: "Cisco ISR4331 Chassis"
        PID: ISR4331/K9        , VID: V04  , SN: FDO2201A0SR

        NAME: "Power Supply Module 0", DESCR: "250W AC Power Supply for Cisco ISR 4330"
        PID: PWR-4330-AC       , VID: V02  , SN: PST2150N1E2

        NAME: "Fan Tray", DESCR: "Cisco ISR4330 Fan Assembly"
        PID: ACS-4330-FANASSY  , VID:      , SN:            

        NAME: "module 0", DESCR: "Cisco ISR4331 Built-In NIM controller"
        PID: ISR4331/K9        , VID:      , SN:            

        NAME: "NIM subslot 0/1", DESCR: "NIM-ES2-4"
        PID: NIM-ES2-4         , VID: V01  , SN: FOC21486SRL

        NAME: "NIM subslot 0/2", DESCR: "NIM-ES2-8"
        PID: NIM-ES2-8         , VID: V01  , SN: FOC22384AXC

        NAME: "NIM subslot 0/0", DESCR: "Front Panel 3 ports Gigabitethernet Module"
        PID: ISR4331-3x1GE     , VID: V01  , SN:            

        NAME: "subslot 0/0 transceiver 2", DESCR: "GE T"
        PID: SFP-GE-T            , VID: V02  , SN: MTC2139029X     

        NAME: "module 1", DESCR: "Cisco ISR4331 Built-In SM controller"
        PID: ISR4331/K9        , VID:      , SN:            

        NAME: "module R0", DESCR: "Cisco ISR4331 Route Processor"
        PID: ISR4331/K9        , VID: V04  , SN: FDO21520TGH

        NAME: "module F0", DESCR: "Cisco ISR4331 Forwarding Processor"
        PID: ISR4331/K9        , VID:      , SN:            
        '''}

    golden_parsed_output_asr901 = {
        'main': 
            {'chassis': 
                {'ASR-920-24SZ-IM': 
                    {'descr': 'Cisco ASR920 Series - 24GE and 4-10GE- Modular PSU and IM',
                    'name': 'Chassis',
                    'pid': 'ASR-920-24SZ-IM',
                    'sn': 'CAT1902V19M',
                    'vid': 'V01'}}},
        'slot': 
            {'0': 
                {'rp': 
                    {'ASR-920-24SZ-IM': 
                        {'descr': 'Cisco ASR920 Series - 24GE and 4-10GE- Modular PSU and IM',
                        'name': 'Chassis',
                        'pid': 'ASR-920-24SZ-IM',
                        'sn': 'CAT1902V19M',
                        'subslot': 
                            {'0 transceiver 26': 
                                {'SFP-10G-LR': 
                                    {'descr': 'SFP+ 10GBASE-LR',
                                    'name': 'subslot 0/0 transceiver 26',
                                    'pid': 'SFP-10G-LR',
                                    'sn': 'CD180456291',
                                    'vid': 'CSCO'}},
                            '0 transceiver 27': 
                                {'SFP-10G-LR': 
                                    {'descr': 'SFP+ 10GBASE-LR',
                                    'name': 'subslot 0/0 transceiver 27',
                                    'pid': 'SFP-10G-LR',
                                    'sn': 'CD180456292',
                                    'vid': 'CSCO'}},
                            '1': 
                                {'A900-IMA3G-IMSG': 
                                    {'descr': 'ASR 900 Combo 4 port DS3 12 DS1 and 4 OCx',
                                    'name': 'IM subslot 0/1',
                                    'pid': 'A900-IMA3G-IMSG',
                                    'sn': 'FOC2204PAP1',
                                    'vid': 'V01'}},
                            '1 transceiver 16': 
                                {'ONS-SI-622-I1': 
                                    {'descr': 'Dual-Rate OC3/12 IR-1',
                                    'name': 'subslot 0/1 transceiver 16',
                                    'pid': 'ONS-SI-622-I1',
                                    'sn': 'ECL133706C3',
                                    'vid': 'A'}}},
                        'vid': 'V01'}}},
            'Fan_Tray': {
                'other': {
                    'ASR-920-FAN-M': {
                        'descr': 'ASR 920 Fan tray',
                        'name': 'Fan Tray',
                        'pid': 'ASR-920-FAN-M',
                        'sn': 'CAT1903V028',
                        'vid': 'V01'}}},
            'P0': 
                {'other': 
                    {'ASR-920-PWR-D': 
                        {'descr': 'ASR 920 250W DC Power Supply',
                        'name': 'Power Supply Module 0',
                        'pid': 'ASR-920-PWR-D',
                        'sn': 'ART1832F11X',
                        'vid': 'V01'}}}}}

    golden_output_asr901 = {'execute.return_value': '''
        Router#show inventory
        NAME: "Chassis", DESCR: "Cisco ASR920 Series - 24GE and 4-10GE- Modular PSU and IM"
        PID: ASR-920-24SZ-IM   , VID: V01  , SN: CAT1902V19M

        NAME: "subslot 0/0 transceiver 26", DESCR: "SFP+ 10GBASE-LR"
        PID: SFP-10G-LR          , VID: CSCO , SN: CD180456291     

        NAME: "subslot 0/0 transceiver 27", DESCR: "SFP+ 10GBASE-LR"
        PID: SFP-10G-LR          , VID: CSCO , SN: CD180456292     

        NAME: "IM subslot 0/1", DESCR: "ASR 900 Combo 4 port DS3 12 DS1 and 4 OCx"
        PID: A900-IMA3G-IMSG   , VID: V01  , SN: FOC2204PAP1

        NAME: "subslot 0/1 transceiver 16", DESCR: "Dual-Rate OC3/12 IR-1"
        PID: ONS-SI-622-I1       , VID: A    , SN: ECL133706C3     

        NAME: "Power Supply Module 0", DESCR: "ASR 920 250W DC Power Supply"
        PID: ASR-920-PWR-D     , VID: V01  , SN: ART1832F11X

        NAME: "Fan Tray", DESCR: "ASR 920 Fan tray"
        PID: ASR-920-FAN-M     , VID: V01  , SN: CAT1903V028
        '''}


    golden_parsed_output_asr1002 = {
        'main': {
            'chassis': {
                'ASR1002-X': {
                    'descr': 'Cisco ASR1002-X Chassis',
                    'name': 'Chassis',
                    'pid': 'ASR1002-X',
                    'sn': 'FOX1111P1M1',
                    'vid': 'V07'
                }
            }
        },
        'slot': {
            '0': {
                'lc': {
                    'ASR1002-X': {
                        'descr': 'Cisco ASR1002-X SPA Interface Processor',
                        'name': 'module 0',
                        'pid': 'ASR1002-X',
                        'sn': '',
                        'subslot': {
                            '0': {
                                '6XGE-BUILT-IN': {
                                    'descr': '6-port Built-in GE SPA',
                                    'name': 'SPA subslot 0/0',
                                    'pid': '6XGE-BUILT-IN',
                                    'sn': '',
                                    'vid': ''
                                }
                            },
                            '0 transceiver 0': {
                                'GLC-SX-MMD': {
                                    'descr': 'GE SX',
                                    'name': 'subslot 0/0 transceiver 0',
                                    'pid': 'GLC-SX-MMD',
                                    'sn': 'AGJ3333R1GC',
                                    'vid': '001'
                                }
                            },
                            '0 transceiver 1': {
                                'GLC-SX-MMD': {
                                    'descr': 'GE SX',
                                    'name': 'subslot 0/0 transceiver 1',
                                    'pid': 'GLC-SX-MMD',
                                    'sn': 'AGJ1111R1G1',
                                    'vid': '001'
                                }
                            },
                            '0 transceiver 2': {
                                'GLC-SX-MMD': {
                                    'descr': 'GE SX',
                                    'name': 'subslot 0/0 transceiver 2',
                                    'pid': 'GLC-SX-MMD',
                                    'sn': 'AGJ9999R1FL',
                                    'vid': '001'
                                }
                            },
                            '0 transceiver 3': {
                                'GLC-SX-MMD': {
                                    'descr': 'GE SX',
                                    'name': 'subslot 0/0 transceiver 3',
                                    'pid': 'GLC-SX-MMD',
                                    'sn': 'AGJ5555RAFM',
                                    'vid': '001'
                                }
                            }
                        },
                        'vid': ''
                    }
                }
            },
            'F0': {
                'lc': {
                    'ASR1002-X': {
                        'descr': 'Cisco ASR1002-X Embedded Services Processor',
                        'name': 'module F0',
                        'pid': 'ASR1002-X',
                        'sn': '',
                        'vid': ''
                    }
                }
            },
            'P0': {
                'other': {
                    'ASR1002-PWR-AC': {
                        'descr': 'Cisco ASR1002 AC Power Supply',
                        'name': 'Power Supply Module 0',
                        'pid': 'ASR1002-PWR-AC',
                        'sn': 'ABC111111EJ',
                        'vid': 'V04'
                    }
                }
            },
            'P1': {
                'other': {
                    'ASR1002-PWR-AC': {
                        'descr': 'Cisco ASR1002 AC Power Supply',
                        'name': 'Power Supply Module 1',
                        'pid': 'ASR1002-PWR-AC',
                        'sn': 'DCB222222EK',
                        'vid': 'V04'
                    }
                }
            },
            'R0': {
                'rp': {
                    'ASR1002-X': {
                        'descr': 'Cisco ASR1002-X Route Processor',
                        'name': 'module R0',
                        'pid': 'ASR1002-X',
                        'sn': 'JAD333333AQ',
                        'vid': 'V07'
                    }
                }
            }
        }
    }

    golden_output_asr1002 = {'execute.return_value': '''
        router#
        ++ router: executing command 'show inventory' +++
        how inventory
        NAME: "Chassis", DESCR: "Cisco ASR1002-X Chassis"
        PID: ASR1002-X         , VID: V07, SN: FOX1111P1M1

        NAME: "Power Supply Module 0", DESCR: "Cisco ASR1002 AC Power Supply"
        PID: ASR1002-PWR-AC    , VID: V04, SN: ABC111111EJ

        NAME: "Power Supply Module 1", DESCR: "Cisco ASR1002 AC Power Supply"
        PID: ASR1002-PWR-AC    , VID: V04, SN: DCB222222EK

        NAME: "module 0", DESCR: "Cisco ASR1002-X SPA Interface Processor"
        PID: ASR1002-X         , VID:    , SN:            

        NAME: "SPA subslot 0/0", DESCR: "6-port Built-in GE SPA"
        PID: 6XGE-BUILT-IN     , VID:    , SN:            

        NAME: "subslot 0/0 transceiver 0", DESCR: "GE SX"
        PID: GLC-SX-MMD          , VID: 001 , SN: AGJ3333R1GC     

        NAME: "subslot 0/0 transceiver 1", DESCR: "GE SX"
        PID: GLC-SX-MMD          , VID: 001 , SN: AGJ1111R1G1     

        NAME: "subslot 0/0 transceiver 2", DESCR: "GE SX"
        PID: GLC-SX-MMD          , VID: 001 , SN: AGJ9999R1FL     

        NAME: "subslot 0/0 transceiver 3", DESCR: "GE SX"
        PID: GLC-SX-MMD          , VID: 001 , SN: AGJ5555RAFM     

        NAME: "module R0", DESCR: "Cisco ASR1002-X Route Processor"
        PID: ASR1002-X         , VID: V07, SN: JAD333333AQ

        NAME: "module F0", DESCR: "Cisco ASR1002-X Embedded Services Processor"
        PID: ASR1002-X         , VID:    , SN:         
        '''}

    golden_parsed_output = {
        'main': {
            'chassis': {
                'ASR1002-HX': {
                    'name': 'Chassis',
                    'descr': 'Cisco ASR1002-HX Chassis',
                    'pid': 'ASR1002-HX',
                    'vid': 'V01',
                    'sn': 'FXS2049Q1P2',
                },
            },
        },
        'slot': {
            'P0': {
                'other': {
                    'ASR1000X-AC-750W': {
                        'name': 'Power Supply Module 0',
                        'descr': 'Cisco 750 Watt AC power supply',
                        'pid': 'ASR1000X-AC-750W',
                        'vid': 'V01',
                        'sn': 'POG20517XAE',
                    },
                },
            },
            'P1': {
                'other': {
                    'ASR1000X-AC-750W': {
                        'name': 'Power Supply Module 1',
                        'descr': 'Cisco 750 Watt AC power supply',
                        'pid': 'ASR1000X-AC-750W',
                        'vid': 'V01',
                        'sn': 'POG20517X06',
                    },
                },
            },
            'Fan_Tray': {
                'other': {
                    'ASR1002HX-FAN': {
                        'descr': 'Cisco ASR1002-HX Fan Tray',
                        'name': 'Fan Tray',
                        'pid': 'ASR1002HX-FAN',
                        'sn': '',
                        'vid': ''
                    }
                }
            },
            '0': {
                'lc': {
                    'ASR1002-HX': {
                        'name': 'module 0',
                        'descr': 'Cisco ASR1002-HX Modular Interface Processor',
                        'pid': 'ASR1002-HX',
                        'vid': '',
                        'sn': '',
                        'subslot': {
                            '0': {
                                'BUILT-IN-EPA-8x1G': {
                                    'name': 'SPA subslot 0/0',
                                    'descr': '8-port Built-in Gigabit Ethernet Port Adapter',
                                    'pid': 'BUILT-IN-EPA-8x1G',
                                    'vid': 'N/A',
                                    'sn': 'JAE12345678',
                                },
                            },
                            '0 transceiver 0': {
                                'F24-CI-SFP-GE-T': {
                                    'name': 'subslot 0/0 transceiver 0',
                                    'descr': 'GE T',
                                    'pid': 'F24-CI-SFP-GE-T',
                                    'vid': '1.0',
                                    'sn': '1165124049',
                                },
                            },
                            '0 transceiver 1': {
                                'F24-CI-SFP-GE-T': {
                                    'name': 'subslot 0/0 transceiver 1',
                                    'descr': 'GE T',
                                    'pid': 'F24-CI-SFP-GE-T',
                                    'vid': '1.0',
                                    'sn': '1165124050',
                                },
                            },
                            '0 transceiver 2': {
                                '': {
                                    'descr': 'GE LX',
                                    'name': 'subslot 0/0 transceiver 2',
                                    'pid': '',
                                    'sn': '1162722191',
                                    'vid': '1.0'
                                }
                            },
                            '0 transceiver 3': {
                                'F24-CI-SFP-GE-T': {
                                    'name': 'subslot 0/0 transceiver 3',
                                    'descr': 'GE T',
                                    'pid': 'F24-CI-SFP-GE-T',
                                    'vid': '1.0',
                                    'sn': '1165124052',
                                },
                            },
                            '1': {
                                'BUILT-IN-EPA-8x10G': {
                                    'name': 'SPA subslot 0/1',
                                    'descr': '8-port Built-in 10-Gigabit Ethernet Port Adapter',
                                    'pid': 'BUILT-IN-EPA-8x10G',
                                    'vid': 'N/A',
                                    'sn': 'JAE87654321',
                                },
                            },
                            '1 transceiver 0': {
                                'SFP-10G-LR': {
                                    'name': 'subslot 0/1 transceiver 0',
                                    'descr': 'SFP+ 10GBASE-LR',
                                    'pid': 'SFP-10G-LR',
                                    'vid': 'V02',
                                    'sn': '3162917828',
                                },
                            },
                            '1 transceiver 1': {
                                'SFP-10G-LR': {
                                    'name': 'subslot 0/1 transceiver 1',
                                    'descr': 'SFP+ 10GBASE-LR',
                                    'pid': 'SFP-10G-LR',
                                    'vid': 'V02',
                                    'sn': '3170330174',
                                },
                            },
                            '1 transceiver 2': {
                                'SFP-10G-LR': {
                                    'name': 'subslot 0/1 transceiver 2',
                                    'descr': 'SFP+ 10GBASE-LR',
                                    'pid': 'SFP-10G-LR',
                                    'vid': 'V02',
                                    'sn': '3170330172',
                                },
                            },
                        },
                    },
                },
            },
            'R0': {
                'rp': {
                    'ASR1002-HX': {
                        'name': 'module R0',
                        'descr': 'Cisco ASR1002-HX Route Processor',
                        'pid': 'ASR1002-HX',
                        'vid': 'V01',
                        'sn': 'JAE21050044',
                    },
                },
            },
            'F0': {
                'lc': {
                    'ASR1002-HX': {
                        'name': 'module F0',
                        'descr': 'Cisco ASR1002-HX Embedded Services Processor',
                        'pid': 'ASR1002-HX',
                        'vid': '',
                        'sn': '',
                    },
                },
            },
        },
    }
    golden_output = {'execute.return_value': '''
        show inventory
        NAME: "Chassis", DESCR: "Cisco ASR1002-HX Chassis"
        PID: ASR1002-HX        , VID: V01  , SN: FXS2049Q1P2

        NAME: "Power Supply Module 0", DESCR: "Cisco 750 Watt AC power supply"
        PID: ASR1000X-AC-750W  , VID: V01  , SN: POG20517XAE

        NAME: "Power Supply Module 1", DESCR: "Cisco 750 Watt AC power supply"
        PID: ASR1000X-AC-750W  , VID: V01  , SN: POG20517X06

        NAME: "Fan Tray", DESCR: "Cisco ASR1002-HX Fan Tray"
        PID: ASR1002HX-FAN     , VID:      , SN:

        NAME: "module 0", DESCR: "Cisco ASR1002-HX Modular Interface Processor"
        PID: ASR1002-HX        , VID:      , SN:

        NAME: "SPA subslot 0/0", DESCR: "8-port Built-in Gigabit Ethernet Port Adapter"
        PID: BUILT-IN-EPA-8x1G , VID: N/A  , SN: JAE12345678

        NAME: "subslot 0/0 transceiver 0", DESCR: "GE T"
        PID: F24-CI-SFP-GE-T   , VID: 1.0  , SN: 1165124049

        NAME: "subslot 0/0 transceiver 1", DESCR: "GE T"
        PID: F24-CI-SFP-GE-T   , VID: 1.0  , SN: 1165124050

        NAME: "subslot 0/0 transceiver 2", DESCR: "GE LX"
        PID: , VID: 1.0  , SN: 1162722191

        NAME: "subslot 0/0 transceiver 3", DESCR: "GE T"
        PID: F24-CI-SFP-GE-T   , VID: 1.0  , SN: 1165124052

        NAME: "SPA subslot 0/1", DESCR: "8-port Built-in 10-Gigabit Ethernet Port Adapter"
        PID: BUILT-IN-EPA-8x10G, VID: N/A  , SN: JAE87654321

        NAME: "subslot 0/1 transceiver 0", DESCR: "SFP+ 10GBASE-LR"
        PID: SFP-10G-LR          , VID: V02  , SN: 3162917828

        NAME: "subslot 0/1 transceiver 1", DESCR: "SFP+ 10GBASE-LR"
        PID: SFP-10G-LR          , VID: V02  , SN: 3170330174

        NAME: "subslot 0/1 transceiver 2", DESCR: "SFP+ 10GBASE-LR"
        PID: SFP-10G-LR          , VID: V02  , SN: 3170330172

        NAME: "module R0", DESCR: "Cisco ASR1002-HX Route Processor"
        PID: ASR1002-HX        , VID: V01  , SN: JAE21050044

        NAME: "module F0", DESCR: "Cisco ASR1002-HX Embedded Services Processor"
        PID: ASR1002-HX        , VID:      , SN:
    '''}

    def test_show_inventory_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        inventory_obj = ShowInventory(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = inventory_obj.parse()
    
    def test_show_inventory_golden_asr1k(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_asr1k)
        inventory_obj = ShowInventory(device=self.device)
        parsed_output = inventory_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_asr1k)

    def test_show_inventory_golden_isr4k(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_isr4k)
        inventory_obj = ShowInventory(device=self.device)
        parsed_output = inventory_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_isr4k)

    def test_show_inventory_golden_c3850(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_c3850)
        inventory_obj = ShowInventory(device=self.device)
        parsed_output = inventory_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_c3850)

    def test_show_inventory_golden_asr901(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_asr901)
        inventory_obj = ShowInventory(device=self.device)
        parsed_output = inventory_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_asr901)

    def test_show_inventory_golden_asr1002(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_asr1002)
        inventory_obj = ShowInventory(device=self.device)
        parsed_output = inventory_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_asr1002)

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        inventory_obj = ShowInventory(device=self.device)
        parsed_output = inventory_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


class TestShowPlatform(unittest.TestCase):
    dev1 = Device(name='empty')
    dev2 = Device(name='semi_empty')
    dev_asr1k = Device(name='asr1k')
    dev_c3850 = Device(name='c3850')
    empty_output = {'execute.return_value': ''}
    semi_empty_output = {'execute.return_value': '''/
Switch#   Role        Priority      State 
-------------------------------------------
*1       Active          3          Ready  
'''}

    golden_parsed_output_c8300 = {
        "slot": {
            "0": {
                "other": {
                    "C8300-1N1S-4G2X": {
                        "slot": "0",
                        "name": "C8300-1N1S-4G2X",
                        "state": "ok",
                        "insert_time": "1w5d",
                        "subslot": {
                            "0": {
                                "4x1G-2xSFP+": {
                                    "subslot": "0",
                                    "name": "4x1G-2xSFP+",
                                    "state": "ok",
                                    "insert_time": "1w5d"
                                }
                            },
                            "1": {
                                "NIMX-M-1TE-SFP": {
                                    "subslot": "1",
                                    "name": "NIMX-M-1TE-SFP",
                                    "state": "ok",
                                    "insert_time": "1w5d"
                                }
                            }
                        },
                        "cpld_ver": "19041222",
                        "fw_ver": "20190618"
                    }
                }
            },
            "1": {
                "other": {
                    "C8300-1N1S-4G2X": {
                        "slot": "1",
                        "name": "C8300-1N1S-4G2X",
                        "state": "ok",
                        "insert_time": "1w5d",
                        "cpld_ver": "19041222",
                        "fw_ver": "20190618"
                    }
                }
            },
            "R0": {
                "other": {
                    "C8300-1N1S-4G2X": {
                        "slot": "R0",
                        "name": "C8300-1N1S-4G2X",
                        "state": "ok, active",
                        "insert_time": "1w5d",
                        "cpld_ver": "19041222",
                        "fw_ver": "20190618"
                    }
                }
            },
            "F0": {
                "other": {
                    "C8300-1N1S-4G2X": {
                        "slot": "F0",
                        "name": "C8300-1N1S-4G2X",
                        "state": "ok, active",
                        "insert_time": "1w5d",
                        "cpld_ver": "19041222",
                        "fw_ver": "20190618"
                    }
                }
            },
            "P0": {
                "other": {
                    "PWR-4430-AC": {
                        "slot": "P0",
                        "name": "PWR-4430-AC",
                        "state": "ok",
                        "insert_time": "1w5d"
                    }
                }
            },
            "P1": {
                "other": {
                    "Unknown": {
                        "slot": "P1",
                        "name": "Unknown",
                        "state": "empty",
                        "insert_time": "never"
                    }
                }
            },
            "P2": {
                "other": {
                    "ACS-4450-FANASSY": {
                        "slot": "P2",
                        "name": "ACS-4450-FANASSY",
                        "state": "ok",
                        "insert_time": "1w5d"
                    }
                }
            }
        }
    }

    golden_output_c8300 = {'execute.return_value': '''\
        Radium-Ultima#sh platform
        Chassis type: C8300-1N1S-4G2X
         
        Slot      Type                State                 Insert time (ago)
        --------- ------------------- --------------------- -----------------
        0         C8300-1N1S-4G2X     ok                    1w5d         
         0/0      4x1G-2xSFP+         ok                    1w5d         
         0/1      NIMX-M-1TE-SFP      ok                    1w5d         
        1         C8300-1N1S-4G2X     ok                    1w5d         
        R0        C8300-1N1S-4G2X     ok, active            1w5d         
        F0        C8300-1N1S-4G2X     ok, active            1w5d         
        P0        PWR-4430-AC         ok                    1w5d         
        P1        Unknown             empty                 never        
        P2        ACS-4450-FANASSY    ok                    1w5d         
         
        Slot      CPLD Version        Firmware Version                       
        --------- ------------------- ---------------------------------------
        0         19041222            20190618                           
        1         19041222            20190618                           
        R0        19041222            20190618                           
        F0        19041222            20190618      
    '''}

    golden_parsed_output_c3850 = {
                                    'main': {
                                        'switch_mac_address': '0057.d21b.cc00',
                                        'mac_persistency_wait_time': 'indefinite',
                                        'swstack': True,
                                    },
                                    'slot': {
                                        '1': {
                                            'rp': {
                                                'WS-C3850-24P-E': {
                                                    'hw_ver': 'V07',
                                                    'mac_address': '0057.d21b.cc00',
                                                    'name': 'WS-C3850-24P-E',
                                                    'ports': '32',
                                                    'swstack_priority': '3',
                                                    'swstack_role': 'Active',
                                                    'slot': '1',
                                                    'sn': 'FCW1947C0HH',
                                                    'state': 'Ready',
                                                    'sw_ver': '16.6.1',
                                                }
                                            }
                                        },
                                        '2': {
                                            'rp': {
                                                'WS-C3850-24P-E': {
                                                    'hw_ver': 'V06',
                                                    'mac_address': '3820.565b.8e80',
                                                    'name': 'WS-C3850-24P-E',
                                                    'ports': '32',
                                                    'swstack_priority': '1',
                                                    'swstack_role': 'Member',
                                                    'slot': '2',
                                                    'sn': 'FCW1932D0TF',
                                                    'state': 'Ready',
                                                    'sw_ver': '16.6.1',
                                                }
                                            }
                                        },
                                        '3': {
                                            'rp': {
                                                'WS-C3850-24P-E': {
                                                    'hw_ver': 'V06',
                                                    'mac_address': '3820.5629.8e00',
                                                    'name': 'WS-C3850-24P-E',
                                                    'ports': '32',
                                                    'swstack_priority': '1',
                                                    'swstack_role': 'Member',
                                                    'slot': '3',
                                                    'sn': 'FCW1932D0L8',
                                                    'state': 'Ready',
                                                    'sw_ver': '16.6.1',
                                                }
                                            }
                                        },
                                        '4': {
                                            'rp': {
                                                'WS-C3850-24P-E': {
                                                    'hw_ver': 'V06',
                                                    'mac_address': '3820.5629.da80',
                                                    'name': 'WS-C3850-24P-E',
                                                    'ports': '32',
                                                    'swstack_priority': '1',
                                                    'swstack_role': 'Member',
                                                    'slot': '4',
                                                    'sn': 'FCW1932C0VB',
                                                    'state': 'Ready',
                                                    'sw_ver': '16.6.1',
                                                }
                                            }
                                        },
                                        '5': {
                                            'rp': {
                                                'WS-C3850-24P-E': {
                                                    'hw_ver': 'V06',
                                                    'mac_address': '3820.5629.7a00',
                                                    'name': 'WS-C3850-24P-E',
                                                    'ports': '32',
                                                    'swstack_priority': '1',
                                                    'swstack_role': 'Standby',
                                                    'slot': '5',
                                                    'sn': 'FCW1932C0M9',
                                                    'state': 'Ready',
                                                    'sw_ver': '16.6.1',
                                                }
                                            }
                                        },
                                    }
                                }

    golden_output_c3850 = {'execute.return_value': '''\
Switch  Ports    Model                Serial No.   MAC address     Hw Ver.       Sw Ver. 
------  -----   ---------             -----------  --------------  -------       --------
 1       32     WS-C3850-24P-E        FCW1947C0HH  0057.d21b.cc00  V07           16.6.1        
 2       32     WS-C3850-24P-E        FCW1932D0TF  3820.565b.8e80  V06           16.6.1        
 3       32     WS-C3850-24P-E        FCW1932D0L8  3820.5629.8e00  V06           16.6.1        
 4       32     WS-C3850-24P-E        FCW1932C0VB  3820.5629.da80  V06           16.6.1        
 5       32     WS-C3850-24P-E        FCW1932C0M9  3820.5629.7a00  V06           16.6.1        
Switch/Stack Mac Address : 0057.d21b.cc00 - Local Mac Address
Mac persistency wait time: Indefinite
                                   Current
Switch#   Role        Priority      State 
-------------------------------------------
*1       Active          3          Ready               
 2       Member          1          Ready               
 3       Member          1          Ready               
 4       Member          1          Ready               
 5       Standby         1          Ready   
'''}

    golden_parsed_output_asr1k = {
                                    'main': {
                                        'chassis': 'ASR1006',
                                    },
                                    'slot': {
                                        '0': {
                                            'lc': {
                                                'ASR1000-SIP40': {
                                                    'slot': '0',
                                                    'name': 'ASR1000-SIP40',
                                                    'state': 'ok',
                                                    'insert_time': '00:33:53',
                                                    'cpld_ver': '00200800',
                                                    'fw_ver': '16.2(1r)',
                                                    'subslot': {
                                                        '0': {
                                                            'SPA-1XCHSTM1/OC3': {
                                                                'subslot': '0',
                                                                'name': 'SPA-1XCHSTM1/OC3',
                                                                'state': 'ok',
                                                                'insert_time': '2d00h',
                                                            }
                                                        },
                                                        '1': {
                                                            'SPA-2XT3/E3': {
                                                                'subslot': '1',
                                                                'name': 'SPA-2XT3/E3',
                                                                'state': 'ok',
                                                                'insert_time': '2d00h',
                                                            }
                                                        },
                                                        '2': {
                                                            'SPA-1XOC48POS/RPR': {
                                                                'subslot': '2',
                                                                'name': 'SPA-1XOC48POS/RPR',
                                                                'state': 'ok',
                                                                'insert_time': '2d00h',
                                                            }
                                                        },
                                                        '3': {
                                                            'SPA-5X1GE-V2': {
                                                                'subslot': '3',
                                                                'name': 'SPA-5X1GE-V2',
                                                                'state': 'ok',
                                                                'insert_time': '2d00h',
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        },
                                        '1': {
                                            'lc': {
                                                'ASR1000-2T+20X1GE': {
                                                    'slot': '1',
                                                    'name': 'ASR1000-2T+20X1GE',
                                                    'state': 'ok',
                                                    'insert_time': '2d00h',
                                                    'cpld_ver': '14011701',
                                                    'fw_ver': '16.3(2r)',
                                                    'subslot': {
                                                        '0': {
                                                            'BUILT-IN-2T+20X1GE': {
                                                                'subslot': '0',
                                                                'name': 'BUILT-IN-2T+20X1GE',
                                                                'state': 'ok',
                                                                'insert_time': '2d00h',
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        },
                                        '2': {
                                            'lc': {
                                                'ASR1000-6TGE': {
                                                    'slot': '2',
                                                    'name': 'ASR1000-6TGE',
                                                    'state': 'ok',
                                                    'insert_time': '2d00h',
                                                    'cpld_ver': '14011701',
                                                    'fw_ver': '16.3(2r)',
                                                    'subslot': {
                                                        '0': {
                                                            'BUILT-IN-6TGE': {
                                                                'subslot': '0',
                                                                'name': 'BUILT-IN-6TGE',
                                                                'state': 'ok',
                                                                'insert_time': '2d00h',
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        },
                                        'R0': {
                                            'rp': {
                                                'ASR1000-RP2': {
                                                    'slot': 'R0',
                                                    'name': 'ASR1000-RP2',
                                                    'state': 'ok, active',
                                                    'insert_time': '00:33:53',
                                                    'cpld_ver': '10021901',
                                                    'fw_ver': '16.2(1r)',
                                                }
                                            }
                                        },
                                        'R1': {
                                            'rp': {
                                                'ASR1000-RP2': {
                                                    'slot': 'R1',
                                                    'name': 'ASR1000-RP2',
                                                    'state': 'ok, standby',
                                                    'insert_time': '00:33:53',
                                                    'cpld_ver': '14111801',
                                                    'fw_ver': '16.2(1r)',
                                                }
                                            }
                                        },
                                        'F0': {
                                            'other': {
                                                'ASR1000-ESP20': {
                                                    'slot': 'F0',
                                                    'name': 'ASR1000-ESP20',
                                                    'state': 'ok, active',
                                                    'insert_time': '00:33:53',
                                                    'cpld_ver': '08041102',
                                                    'fw_ver': '16.2(1r)',
                                                }
                                            }
                                        },
                                        'P0': {
                                            'other': {
                                                'ASR1006-PWR-AC': {
                                                    'slot': 'P0',
                                                    'name': 'ASR1006-PWR-AC',
                                                    'state': 'ok',
                                                    'insert_time': '00:33:18',
                                                }
                                            }
                                        },
                                        'P1': {
                                            'other': {
                                                'ASR1006-PWR-AC': {
                                                    'slot': 'P1',
                                                    'name': 'ASR1006-PWR-AC',
                                                    'state': 'ps, fail',
                                                    'insert_time': '00:33:17',
                                                }
                                            }
                                        },
                                        '4': {
                                            'other': {
                                                '': {
                                                    'slot': '4',
                                                    'name': '',
                                                    'state': 'unknown',
                                                    'insert_time': '2d00h',
                                                    'cpld_ver': 'N/A',
                                                    'fw_ver': 'N/A',
                                                }
                                            }
                                        },
                                    }
                                }

    golden_output_asr1k = {'execute.return_value': '''\
        Chassis type: ASR1006             

        Slot      Type                State                 Insert time (ago) 
        --------- ------------------- --------------------- ----------------- 
        0         ASR1000-SIP40       ok                    00:33:53      
         0/0      SPA-1XCHSTM1/OC3    ok                    2d00h         
         0/1      SPA-2XT3/E3         ok                    2d00h         
         0/2      SPA-1XOC48POS/RPR   ok                    2d00h         
         0/3      SPA-5X1GE-V2        ok                    2d00h        
        1         ASR1000-2T+20X1GE   ok                    2d00h         
         1/0      BUILT-IN-2T+20X1GE  ok                    2d00h         
        2         ASR1000-6TGE        ok                    2d00h         
         2/0      BUILT-IN-6TGE       ok                    2d00h         
        4                             unknown               2d00h         
        R0        ASR1000-RP2         ok, active            00:33:53      
        R1        ASR1000-RP2         ok, standby           00:33:53      
        F0        ASR1000-ESP20       ok, active            00:33:53      
        P0        ASR1006-PWR-AC      ok                    00:33:18      
        P1        ASR1006-PWR-AC      ps, fail              00:33:17      

        Slot      CPLD Version        Firmware Version                        
        --------- ------------------- --------------------------------------- 
        0         00200800            16.2(1r)                            
        1         14011701            16.3(2r)                            
        2         14011701            16.3(2r)                            
        4         N/A                 N/A      
        R0        10021901            16.2(1r)                            
        R1        14111801            16.2(1r)                            
        F0        08041102            16.2(1r)        
        '''}

    golden_parsed_output = {
        'slot': {
            '1': {
                'lc': {
                    'ISR4331/K9': {
                        'insert_time': '3w5d',
                        'slot': '1',
                        'cpld_ver': '17100927',
                        'fw_ver': '16.7(3r)',
                        'name': 'ISR4331/K9',
                        'state': 'ok',
                        },
                    },
                },
            'F0': {
                'other': {
                    'ISR4331/K9': {
                        'insert_time': '3w5d',
                        'slot': 'F0',
                        'cpld_ver': '17100927',
                        'fw_ver': '16.7(3r)',
                        'name': 'ISR4331/K9',
                        'state': 'ok, active',
                        },
                    },
                },
            'P0': {
                'other': {
                    'PWR-4330-AC': {
                        'state': 'ok',
                        'slot': 'P0',
                        'name': 'PWR-4330-AC',
                        'insert_time': '3w5d',
                        },
                    },
                },
            'P2': {
                'other': {
                    'ACS-4330-FANASSY': {
                        'state': 'ok',
                        'slot': 'P2',
                        'name': 'ACS-4330-FANASSY',
                        'insert_time': '3w5d',
                        },
                    },
                },
            '0': {
                'lc': {
                    'ISR4331/K9': {
                        'insert_time': '3w5d',
                        'subslot': {
                            '1': {
                                'NIM-ES2-4': {
                                    'state': 'ok',
                                    'subslot': '1',
                                    'name': 'NIM-ES2-4',
                                    'insert_time': '3w5d',
                                    },
                                },
                            '0': {
                                'ISR4331-3x1GE': {
                                    'state': 'ok',
                                    'subslot': '0',
                                    'name': 'ISR4331-3x1GE',
                                    'insert_time': '3w5d',
                                    },
                                },
                            '2': {
                                'NIM-ES2-8': {
                                    'state': 'ok',
                                    'subslot': '2',
                                    'name': 'NIM-ES2-8',
                                    'insert_time': '3w5d',
                                    },
                                },
                            },
                        'cpld_ver': '17100927',
                        'fw_ver': '16.7(3r)',
                        'name': 'ISR4331/K9',
                        'state': 'ok',
                        'slot': '0',
                        },
                    },
                },
            'R0': {
                'rp': {
                    'ISR4331/K9': {
                        'insert_time': '3w5d',
                        'slot': 'R0',
                        'cpld_ver': '17100927',
                        'fw_ver': '16.7(3r)',
                        'name': 'ISR4331/K9',
                        'state': 'ok, active',
                        },
                    },
                },
            },
        }

    golden_output = {'execute.return_value': '''\
        show platform
        Chassis type: ISR4331/K9

        Slot      Type                State                 Insert time (ago) 
        --------- ------------------- --------------------- ----------------- 
        0         ISR4331/K9          ok                    3w5d          
         0/0      ISR4331-3x1GE       ok                    3w5d          
         0/1      NIM-ES2-4           ok                    3w5d          
         0/2      NIM-ES2-8           ok                    3w5d          
        1         ISR4331/K9          ok                    3w5d          
        R0        ISR4331/K9          ok, active            3w5d          
        F0        ISR4331/K9          ok, active            3w5d          
        P0        PWR-4330-AC         ok                    3w5d          
        P2        ACS-4330-FANASSY    ok                    3w5d          

        Slot      CPLD Version        Firmware Version                        
        --------- ------------------- --------------------------------------- 
        0         17100927            16.7(3r)                            
        1         17100927            16.7(3r)                            
        R0        17100927            16.7(3r)                            
        F0        17100927            16.7(3r)                            

        c4331a#      
    '''}

    golden_parsed_output_2 = {
        'main': {
            'chassis': 'ASR1002'
        },
        'slot': {
            '0': {
                'lc': {
                    'ASR1002-SIP10': {
                        'cpld_ver': '07123456',
                        'fw_ver': '16.1(5r)S',
                        'insert_time': '2y30w',
                        'name': 'ASR1002-SIP10',
                        'slot': '0',
                        'state': 'ok',
                        'subslot': {
                            '0': {
                                'SPA-2X1GE-V2': {
                                    'insert_time': '2y30w',
                                    'name': 'SPA-2X1GE-V2',
                                    'state': 'ok',
                                    'subslot': '0'
                                }
                            },
                            '1': {
                                '4XGE-BUILT-IN': {
                                    'insert_time': '2y30w',
                                    'name': '4XGE-BUILT-IN',
                                    'state': 'ok',
                                    'subslot': '1'
                                }
                            }
                        }
                    }
                }
            },
            'F0': {
                'other': {
                    'ASR1000-ESP10': {
                        'cpld_ver': '09123456',
                        'fw_ver': '16.1(5r)S',
                        'insert_time': '2y30w',
                        'name': 'ASR1000-ESP10',
                        'slot': 'F0',
                        'state': 'ok, active'
                    }
                }
            },
            'P0': {
                'other': {
                    'ASR1002-PWR-AC': {
                        'insert_time': '2y30w',
                        'name': 'ASR1002-PWR-AC',
                        'slot': 'P0',
                        'state': 'ok, active'
                    }
                }
            },
            'P1': {
                'other': {
                    'ASR1002-PWR-AC': {
                        'insert_time': '2y30w',
                        'name': 'ASR1002-PWR-AC',
                        'slot': 'P1',
                        'state': 'ok'
                    }
                }
            },
            'R0': {
                'rp': {
                    'ASR1002-RP1': {
                        'cpld_ver': '08123456',
                        'fw_ver': '16.1(5r)S',
                        'insert_time': '2y30w',
                        'name': 'ASR1002-RP1',
                        'slot': 'R0',
                        'state': 'ok, active'
                    }
                }
            }
        }
    }

    golden_output_2 = {'execute.return_value': '''\
        Chassis type: ASR1002            
         
        Slot      Type                State                 Insert time (ago)
        --------- ------------------- --------------------- -----------------
        0         ASR1002-SIP10       ok                    2y30w        
         0/0      SPA-2X1GE-V2        ok                    2y30w        
         0/1      4XGE-BUILT-IN       ok                    2y30w        
        R0        ASR1002-RP1         ok, active            2y30w        
        F0        ASR1000-ESP10       ok, active            2y30w        
        P0        ASR1002-PWR-AC      ok, active            2y30w        
        P1        ASR1002-PWR-AC      ok                    2y30w        
         
        Slot      CPLD Version        Firmware Version                        
        --------- ------------------- ---------------------------------------
        0         07123456            16.1(5r)S                          
        R0        08123456            16.1(5r)S                          
        F0        09123456            16.1(5r)S    
    '''}

    golden_parsed_output_3 = {
        'slot': {
            '0': {
                'lc': {
                    'ASR1002-X': {
                        'cpld_ver': '11112222',
                        'fw_ver': '16.7(2r)',
                        'insert_time': '22w5d',
                        'name': 'ASR1002-X',
                        'slot': '0',
                        'state': 'ok',
                        'subslot': {
                            '0': {
                                '6XGE-BUILT-IN': {
                                    'insert_time': '22w5d',
                                    'name': '6XGE-BUILT-IN',
                                    'state': 'ok',
                                    'subslot': '0'
                                }
                            }
                        }
                    }
                }
            },
            'F0': {
                'other': {
                    'ASR1002-X': {
                        'cpld_ver': '11112222',
                        'fw_ver': '16.7(2r)',
                        'insert_time': '22w5d',
                        'name': 'ASR1002-X',
                        'slot': 'F0',
                        'state': 'ok, active'
                    }
                }
            },
            'P0': {
                'other': {
                    'ASR1002-PWR-AC': {
                        'insert_time': '22w5d',
                        'name': 'ASR1002-PWR-AC',
                        'slot': 'P0',
                        'state': 'ok'
                    }
                }
            },
            'P1': {
                'other': {
                    'ASR1002-PWR-AC': {
                        'insert_time': '22w5d',
                        'name': 'ASR1002-PWR-AC',
                        'slot': 'P1',
                        'state': 'ok'
                    }
                }
            },
            'R0': {
                'rp': {
                    'ASR1002-X': {
                        'cpld_ver': '11112222',
                        'fw_ver': '16.7(2r)',
                        'insert_time': '22w5d',
                        'name': 'ASR1002-X',
                        'slot': 'R0',
                        'state': 'ok, active'
                    }
                }
            }
        }        
    }

    golden_output_3 = {'execute.return_value': '''\
        Chassis type: ASR1002-X          
         
        Slot      Type                State                 Insert time (ago)
        --------- ------------------- --------------------- -----------------
        0         ASR1002-X           ok                    22w5d        
         0/0      6XGE-BUILT-IN       ok                    22w5d        
        R0        ASR1002-X           ok, active            22w5d        
        F0        ASR1002-X           ok, active            22w5d        
        P0        ASR1002-PWR-AC      ok                    22w5d        
        P1        ASR1002-PWR-AC      ok                    22w5d        
         
        Slot      CPLD Version        Firmware Version                        
        --------- ------------------- ---------------------------------------
        0         11112222            16.7(2r)                            
        R0        11112222            16.7(2r)                            
        F0        11112222            16.7(2r)            
    '''}

    golden_parsed_output_c9500 = {
        "slot": {
            "1": {
                "lc": {
                    "C9500-32QC": {
                        "slot": "1",
                        "name": "C9500-32QC",
                        "state": "ok",
                        "insert_time": "1d18h",
                        "subslot": {
                            "0": {
                                "C9500-32QC": {
                                    "subslot": "0",
                                    "name": "C9500-32QC",
                                    "state": "ok",
                                    "insert_time": "1d18h"
                                }
                            }
                        }
                    }
                }
            },
            "R0": {
                "rp": {
                    "C9500-32QC": {
                        "slot": "R0",
                        "name": "C9500-32QC",
                        "state": "ok, active",
                        "insert_time": "1d18h"
                    }
                }
            },
            "P0": {
                "other": {
                    "C9K-PWR-650WAC-R": {
                        "slot": "P0",
                        "name": "C9K-PWR-650WAC-R",
                        "state": "ok",
                        "insert_time": "1d18h"
                    }
                }
            },
            "P2": {
                "other": {
                    "C9K-T1-FANTRAY": {
                        "slot": "P2",
                        "name": "C9K-T1-FANTRAY",
                        "state": "ok",
                        "insert_time": "1d18h"
                    }
                }
            },
            "P3": {
                "other": {
                    "C9K-T1-FANTRAY": {
                        "slot": "P3",
                        "name": "C9K-T1-FANTRAY",
                        "state": "ok",
                        "insert_time": "1d18h"
                    }
                }
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

    def test_semi_empty(self):
        self.dev2 = Mock(**self.semi_empty_output)
        platform_obj = ShowPlatform(device=self.dev2)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = platform_obj.parse()       

    def test_golden_c8300(self):
        self.maxDiff = None
        self.dev_c8300 = Mock(**self.golden_output_c8300)
        platform_obj = ShowPlatform(device=self.dev_c8300)
        parsed_output = platform_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_c8300)

    def test_golden_c3850(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_c3850)
        platform_obj = ShowPlatform(device=self.dev_c3850)
        parsed_output = platform_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_c3850)

    def test_golden_asr1k(self):
        self.maxDiff = None
        self.dev_asr1k = Mock(**self.golden_output_asr1k)
        platform_obj = ShowPlatform(device=self.dev_asr1k)
        parsed_output = platform_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_asr1k)

    def test_golden(self):
        self.maxDiff = None
        self.dev_asr1k = Mock(**self.golden_output)
        platform_obj = ShowPlatform(device=self.dev_asr1k)
        parsed_output = platform_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_2(self):
        self.maxDiff = None
        self.dev_asr1002 = Mock(**self.golden_output_2)
        platform_obj = ShowPlatform(device=self.dev_asr1002)
        parsed_output_2 = platform_obj.parse()
        self.assertEqual(parsed_output_2,self.golden_parsed_output_2)

    def test_golden_3(self):
        self.maxDiff = None
        self.dev_asr1002 = Mock(**self.golden_output_3)
        platform_obj = ShowPlatform(device=self.dev_asr1002)
        parsed_output_3 = platform_obj.parse()
        self.assertEqual(parsed_output_3,self.golden_parsed_output_3)

    def test_golden_c9500(self):
        self.maxDiff = None
        self.dev_c9500 = Mock(**self.golden_output_c9500)
        platform_obj = ShowPlatform(device=self.dev_c9500)
        parsed_output = platform_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_c9500)


class TestShowBoot(unittest.TestCase):
    dev1 = Device(name='empty')
    dev_asr1k = Device(name='asr1k')
    dev_c3850 = Device(name='c3850')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output_c3850 = {
        "ipxe_timeout": 0,
         "enable_break": True,
         "current_boot_variable": "flash:cat3k_caa-universalk9.BLD_POLARIS_DEV_LATEST_20150907_031219.bin;flash:cat3k_caa-universalk9.BLD_POLARIS_DEV_LATEST_20150828_174328.SSA.bin;flash:ISSUCleanGolden",
         "next_reload_boot_variable": "flash:ISSUCleanGolden",
         "manual_boot": True,
         "boot_mode": "device"
    }

    golden_output_c3850 = {'execute.return_value': '''\
        ---------------------------
        Switch 5
        ---------------------------
        Current Boot Variables:
        BOOT variable = flash:cat3k_caa-universalk9.BLD_POLARIS_DEV_LATEST_20150907_031219.bin;flash:cat3k_caa-universalk9.BLD_POLARIS_DEV_LATEST_20150828_174328.SSA.bin;flash:ISSUCleanGolden;

        Boot Variables on next reload:
        BOOT variable = flash:ISSUCleanGolden;
        Manual Boot = yes
        Enable Break = yes
        Boot Mode = DEVICE
        iPXE Timeout = 0
    '''
    }

    golden_parsed_output_asr1k = {
        "standby": {
            "boot_variable": "bootflash:/asr1000rpx.bin,12",
            "configuration_register": "0x2002"
        },
        "active": {
            "boot_variable": "bootflash:/asr1000rpx.bin,12",
            "configuration_register": "0x2002"
        }
    }

    golden_output_asr1k = {'execute.return_value': '''\
        BOOT variable = bootflash:/asr1000rpx.bin,12;
        CONFIG_FILE variable = 
        BOOTLDR variable does not exist
        Configuration register is 0x2002

        Standby BOOT variable = bootflash:/asr1000rpx.bin,12;
        Standby CONFIG_FILE variable = 
        Standby BOOTLDR variable does not exist
        Standby Configuration register is 0x2002
    '''
    }

    golden_output_2900 = {'execute.return_value': '''
        SW-GENIE#sho boot
        BOOT path-list      : flash:/c2960x-universalk9-mz.152-4.E8.bin
        Config file         : flash:/config.text
        Private Config file : flash:/private-config.text
        Enable Break        : yes
        Manual Boot         : no
        Allow Dev Key         : yes
        HELPER path-list    : 
        Auto upgrade        : yes
        Auto upgrade path   : 
        Boot optimization   : disabled
        NVRAM/Config file
            buffer size:   524288
        Timeout for Config
                Download:    0 seconds
        Config Download 
            via DHCP:       disabled (next boot: disabled)
        -------------------
        Switch 2
        -------------------
        BOOT path-list      : flash:/c2960x-universalk9-mz.152-4.E8.bin
        Config file         : flash:/config.text
        Private Config file : flash:/private-config.text
        Enable Break        : yes
        Manual Boot         : no
        Allow Dev Key         : yes
        HELPER path-list    : 
        Auto upgrade        : no
        Auto upgrade path   : 
        -------------------
        Switch 3
        -------------------
        BOOT path-list      : flash:/c2960x-universalk9-mz.152-4.E8.bin
        Config file         : flash:/config.text
        Private Config file : flash:/private-config.text
        Enable Break        : yes
        Manual Boot         : no
        Allow Dev Key         : yes
        HELPER path-list    : 
        Auto upgrade        : no
        Auto upgrade path   : 
        SW-GENIE# 
    '''}

    golden_parsed_output_2900 = {
        'allow_dev_key': True,
        'auto_upgrade': True,
        'boot_optimization': False,
        'boot_path_list': 'flash:/c2960x-universalk9-mz.152-4.E8.bin',
        'config_download_via_dhcp': False,
        'config_file': 'flash:/config.text',
        'enable_break': True,
        'manual_boot': False,
        'next_boot': False,
        'nvram_buffer_size': 524288,
        'private_config_file': 'flash:/private-config.text',
        'switches': {
            2: {
                'allow_dev_key': True,
                'auto_upgrade': False,
                'boot_path_list': 'flash:/c2960x-universalk9-mz.152-4.E8.bin',
                'config_file': 'flash:/config.text',
                'enable_break': True,
                'manual_boot': False,
                'private_config_file': 'flash:/private-config.text'
            },
            3: {'allow_dev_key': True,
                'auto_upgrade': False,
                'boot_path_list': 'flash:/c2960x-universalk9-mz.152-4.E8.bin',
                'config_file': 'flash:/config.text',
                'enable_break': True,
                'manual_boot': False,
                'private_config_file': 'flash:/private-config.text'
            }
        },
        'timeout_config_download': '0 seconds'
    }
    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        platform_obj = ShowBoot(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = platform_obj.parse()    

    def test_golden_c3850(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_c3850)
        platform_obj = ShowBoot(device=self.dev_c3850)
        parsed_output = platform_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_c3850)

    def test_golden_asr1k(self):
        self.maxDiff = None
        self.dev_asr1k = Mock(**self.golden_output_asr1k)
        platform_obj = ShowBoot(device=self.dev_asr1k)
        parsed_output = platform_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_asr1k)
    
    def test_golden_2900(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_2900)
        obj = ShowBoot(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_2900)


class TestShowSwitchDetail(unittest.TestCase):
    dev1 = Device(name='empty')
    dev_c3850 = Device(name='c3850')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output_c3850 = {
        "switch": {
            "stack": {
               "1": {
                    "role": "active",
                    "hw_ver": "V04",
                    "ports": {
                         "1": {
                              "stack_port_status": "ok",
                              "neighbors_num": 3
                         },
                         "2": {
                              "stack_port_status": "ok",
                              "neighbors_num": 2
                         }
                    },
                    "state": "ready",
                    "priority": "3",
                    "mac_address": "689c.e2d9.df00"
               },
               "3": {
                    "role": "member",
                    "hw_ver": "V05",
                    "ports": {
                         "1": {
                              "stack_port_status": "ok",
                              "neighbors_num": 2
                         },
                         "2": {
                              "stack_port_status": "ok",
                              "neighbors_num": 1
                         }
                    },
                    "state": "ready",
                    "priority": "1",
                    "mac_address": "c800.84ff.4800"
               },
               "2": {
                    "role": "standby",
                    "hw_ver": "V05",
                    "ports": {
                         "1": {
                              "stack_port_status": "ok",
                              "neighbors_num": 1
                         },
                         "2": {
                              "stack_port_status": "ok",
                              "neighbors_num": 3
                         }
                    },
                    "state": "ready",
                    "priority": "2",
                    "mac_address": "c800.84ff.7e00"
               }
            },
            "mac_address": "689c.e2d9.df00",
            "mac_persistency_wait_time": "indefinite"
        }
    }

    golden_output_c3850 = {'execute.return_value': '''\
        show switch detail
        Switch/Stack Mac Address : 689c.e2d9.df00 - Local Mac Address
        Mac persistency wait time: Indefinite
                                                     H/W   Current
        Switch#   Role    Mac Address     Priority Version  State 
        -------------------------------------------------------------------------------------
        *1       Active   689c.e2d9.df00     3      V04     Ready                
         2       Standby  c800.84ff.7e00     2      V05     Ready                
         3       Member   c800.84ff.4800     1      V05     Ready                



                 Stack Port Status             Neighbors     
        Switch#  Port 1     Port 2           Port 1   Port 2 
        --------------------------------------------------------
          1         OK         OK               3        2 
          2         OK         OK               1        3 
          3         OK         OK               2        1 
    '''
    }

    golden_parsed_output1 = {
        "switch": {
            "mac_address": "00d6.fe70.3c80",
            "mac_persistency_wait_time": "indefinite",
            "stack": {
                "1": {
                    "role": "active",
                    "state": "ready",
                    "mac_address": "00d6.fe70.3c80",
                    "priority": "1",
                    "hw_ver": "V02",
                    "ports": {
                        "1": {
                            "stack_port_status": "down",
                            "neighbors_num": "None"
                        },
                        "2": {
                            "stack_port_status": "down",
                            "neighbors_num": "None"
                        }
                    }
                }
            }
        }
    }
    golden_output1 = {'execute.return_value': '''\
        show switch detail
        Switch/Stack Mac Address : 00d6.fe70.3c80 - Local Mac Address
        Mac persistency wait time: Indefinite
                                                    H/W   Current
        Switch#   Role    Mac Address     Priority Version  State
        ------------------------------------------------------------
        *1       Active   00d6.fe70.3c80     1      V02     Ready

                Stack Port Status             Neighbors
        Switch#  Port 1     Port 2           Port 1   Port 2
        --------------------------------------------------------
        1       DOWN       DOWN             None     None
    '''}

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
        self.assertEqual(parsed_output,self.golden_parsed_output_c3850)

    def test_golden1(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output1)
        platform_obj = ShowSwitchDetail(device=self.dev_c3850)
        parsed_output = platform_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output1)

class TestShowSwitch(unittest.TestCase):
    dev1 = Device(name='empty')
    dev_c3850 = Device(name='c3850')
    empty_output = {'execute.return_value': '      '}

    golden_parsed_output_c3850 = {
        "switch": {
            "stack": {
               "1": {
                    "role": "active",
                    "hw_ver": "V04",
                    "state": "ready",
                    "priority": "3",
                    "mac_address": "689c.e2d9.df00"
               },
               "3": {
                    "role": "member",
                    "hw_ver": "V05",
                    "state": "ready",
                    "priority": "1",
                    "mac_address": "c800.84ff.4800"
               },
               "2": {
                    "role": "standby",
                    "hw_ver": "V05",
                    "state": "ready",
                    "priority": "2",
                    "mac_address": "c800.84ff.7e00"
               }
            },
            "mac_address": "689c.e2d9.df00",
            "mac_persistency_wait_time": "indefinite"
        }
    }

    golden_output_c3850 = {'execute.return_value': '''\
        Switch/Stack Mac Address : 689c.e2d9.df00 - Local Mac Address
        Mac persistency wait time: Indefinite
                                                     H/W   Current
        Switch#   Role    Mac Address     Priority Version  State 
        -------------------------------------------------------------------------------------
        *1       Active   689c.e2d9.df00     3      V04     Ready                
         2       Standby  c800.84ff.7e00     2      V05     Ready                
         3       Member   c800.84ff.4800     1      V05     Ready 
    '''
    }

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
        self.assertEqual(parsed_output,self.golden_parsed_output_c3850)


class TestShowModule(unittest.TestCase):
    dev1 = Device(name='empty')
    dev_c3850 = Device(name='c3850')
    empty_output = {'execute.return_value': '      '}

    golden_parsed_output_c3850 = {
        "switch": {
            "2": {
               "serial_number": "fcw1909c0n2",
               "mac_address": "c800.84ff.7e00",
               "sw_ver": "16.9.1",
               "model": "ws-c3850-24p-e",
               "hw_ver": "v05",
               "port": "32"
            },
            "1": {
               "serial_number": "foc1902x062",
               "mac_address": "689c.e2d9.df00",
               "sw_ver": "16.9.1",
               "model": "ws-c3850-48p-e",
               "hw_ver": "v04",
               "port": "56"
            },
            "3": {
               "serial_number": "fcw1909d0jc",
               "mac_address": "c800.84ff.4800",
               "sw_ver": "16.9.1",
               "model": "ws-c3850-24p-e",
               "hw_ver": "v05",
               "port": "32"
            }
        }
    }

    golden_output_c3850 = {'execute.return_value': '''\
        Switch  Ports    Model                Serial No.   MAC address     Hw Ver.       Sw Ver. 
        ------  -----   ---------             -----------  --------------  -------       --------
         1       56     WS-C3850-48P-E        FOC1902X062  689c.e2d9.df00  V04           16.9.1        
         2       32     WS-C3850-24P-E        FCW1909C0N2  c800.84ff.7e00  V05           16.9.1        
         3       32     WS-C3850-24P-E        FCW1909D0JC  c800.84ff.4800  V05           16.9.1
    '''
    }

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
        self.assertEqual(parsed_output,self.golden_parsed_output_c3850)


class TestShowPlatformSoftwareStatusControlProcessorBrief(unittest.TestCase):

    dev = Device(name='c3850')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        "slot": {
            "4-rp0": {
               "memory": {
                    "used_percentage": 40,
                    "committed": 1950012,
                    "free": 2411376,
                    "total": 4010000,
                    "committed_percentage": 49,
                    "status": "healthy",
                    "used": 1598624,
                    "free_percentage": 60
               },
               "cpu": {
                    "0": {
                         "waiting": 0.09,
                         "system": 3.29,
                         "nice_process": 0.0,
                         "irq": 0.0,
                         "sirq": 0.0,
                         "idle": 93.7,
                         "user": 2.89
                    },
                    "3": {
                         "waiting": 0.0,
                         "system": 4.2,
                         "nice_process": 0.0,
                         "irq": 0.0,
                         "sirq": 0.0,
                         "idle": 92.0,
                         "user": 3.8
                    },
                    "1": {
                         "waiting": 0.0,
                         "system": 3.4,
                         "nice_process": 0.0,
                         "irq": 0.0,
                         "sirq": 0.0,
                         "idle": 94.7,
                         "user": 1.9
                    },
                    "2": {
                         "waiting": 0.0,
                         "system": 3.8,
                         "nice_process": 0.0,
                         "irq": 0.0,
                         "sirq": 0.0,
                         "idle": 93.3,
                         "user": 2.9
                    }
               },
               "load_average": {
                    "1_min": 0.08,
                    "status": "healthy",
                    "15_min": 0.27,
                    "5_min": 0.24
               }
            },
            "1-rp0": {
               "memory": {
                    "used_percentage": 64,
                    "committed": 3536536,
                    "free": 1456916,
                    "total": 4010000,
                    "committed_percentage": 88,
                    "status": "healthy",
                    "used": 2553084,
                    "free_percentage": 36
               },
               "cpu": {
                    "0": {
                         "waiting": 0.0,
                         "system": 2.09,
                         "nice_process": 0.0,
                         "irq": 0.0,
                         "sirq": 0.19,
                         "idle": 93.8,
                         "user": 3.89
                    },
                    "3": {
                         "waiting": 0.1,
                         "system": 1.4,
                         "nice_process": 0.0,
                         "irq": 0.0,
                         "sirq": 0.0,
                         "idle": 93.8,
                         "user": 4.7
                    },
                    "1": {
                         "waiting": 0.0,
                         "system": 1.0,
                         "nice_process": 0.0,
                         "irq": 0.0,
                         "sirq": 0.1,
                         "idle": 93.2,
                         "user": 5.7
                    },
                    "2": {
                         "waiting": 0.0,
                         "system": 0.89,
                         "nice_process": 0.0,
                         "irq": 0.0,
                         "sirq": 0.09,
                         "idle": 94.1,
                         "user": 4.89
                    }
               },
               "load_average": {
                    "1_min": 0.26,
                    "status": "healthy",
                    "15_min": 0.33,
                    "5_min": 0.35
               }
            },
            "3-rp0": {
               "memory": {
                    "used_percentage": 40,
                    "committed": 1940852,
                    "free": 2418208,
                    "total": 4010000,
                    "committed_percentage": 48,
                    "status": "healthy",
                    "used": 1591792,
                    "free_percentage": 60
               },
               "cpu": {
                    "0": {
                         "waiting": 0.0,
                         "system": 3.5,
                         "nice_process": 0.0,
                         "irq": 0.0,
                         "sirq": 0.0,
                         "idle": 94.6,
                         "user": 1.9
                    },
                    "3": {
                         "waiting": 0.0,
                         "system": 2.6,
                         "nice_process": 0.0,
                         "irq": 0.0,
                         "sirq": 0.0,
                         "idle": 95.49,
                         "user": 1.9
                    },
                    "1": {
                         "waiting": 0.0,
                         "system": 3.4,
                         "nice_process": 0.0,
                         "irq": 0.0,
                         "sirq": 0.0,
                         "idle": 93.2,
                         "user": 3.4
                    },
                    "2": {
                         "waiting": 0.0,
                         "system": 2.7,
                         "nice_process": 0.0,
                         "irq": 0.0,
                         "sirq": 0.0,
                         "idle": 94.0,
                         "user": 3.3
                    }
               },
               "load_average": {
                    "1_min": 0.07,
                    "status": "healthy",
                    "15_min": 0.12,
                    "5_min": 0.09
               }
            },
            "2-rp0": {
               "memory": {
                    "used_percentage": 61,
                    "committed": 3433136,
                    "free": 1560928,
                    "total": 4010000,
                    "committed_percentage": 86,
                    "status": "healthy",
                    "used": 2449072,
                    "free_percentage": 39
               },
               "cpu": {
                    "0": {
                         "waiting": 0.0,
                         "system": 1.7,
                         "nice_process": 0.0,
                         "irq": 0.0,
                         "sirq": 0.0,
                         "idle": 94.99,
                         "user": 3.3
                    },
                    "3": {
                         "waiting": 0.0,
                         "system": 1.2,
                         "nice_process": 0.0,
                         "irq": 0.0,
                         "sirq": 0.0,
                         "idle": 96.89,
                         "user": 1.9
                    },
                    "1": {
                         "waiting": 0.0,
                         "system": 1.3,
                         "nice_process": 0.0,
                         "irq": 0.0,
                         "sirq": 0.0,
                         "idle": 95.39,
                         "user": 3.3
                    },
                    "2": {
                         "waiting": 0.0,
                         "system": 1.7,
                         "nice_process": 0.0,
                         "irq": 0.0,
                         "sirq": 0.0,
                         "idle": 94.6,
                         "user": 3.7
                    }
               },
               "load_average": {
                    "1_min": 0.17,
                    "status": "healthy",
                    "15_min": 0.23,
                    "5_min": 0.24
               }
            },
            "5-rp0": {
               "memory": {
                    "used_percentage": 40,
                    "committed": 1948956,
                    "free": 2410820,
                    "total": 4010000,
                    "committed_percentage": 49,
                    "status": "healthy",
                    "used": 1599180,
                    "free_percentage": 60
               },
               "cpu": {
                    "0": {
                         "waiting": 0.0,
                         "system": 0.8,
                         "nice_process": 0.0,
                         "irq": 0.0,
                         "sirq": 0.0,
                         "idle": 97.39,
                         "user": 1.8
                    },
                    "3": {
                         "waiting": 0.0,
                         "system": 0.79,
                         "nice_process": 0.0,
                         "irq": 0.0,
                         "sirq": 0.0,
                         "idle": 97.1,
                         "user": 2.09
                    },
                    "1": {
                         "waiting": 0.0,
                         "system": 0.5,
                         "nice_process": 0.0,
                         "irq": 0.0,
                         "sirq": 0.0,
                         "idle": 98.1,
                         "user": 1.4
                    },
                    "2": {
                         "waiting": 0.0,
                         "system": 1.3,
                         "nice_process": 0.0,
                         "irq": 0.0,
                         "sirq": 0.0,
                         "idle": 96.8,
                         "user": 1.9
                    }
               },
               "load_average": {
                    "1_min": 0.15,
                    "status": "healthy",
                    "15_min": 0.14,
                    "5_min": 0.15
               }
            }
        }
    }

    golden_output = {'execute.return_value': '''\
        Load Average
         Slot  Status  1-Min  5-Min 15-Min
        1-RP0 Healthy   0.26   0.35   0.33
        2-RP0 Healthy   0.17   0.24   0.23
        3-RP0 Healthy   0.07   0.09   0.12
        4-RP0 Healthy   0.08   0.24   0.27
        5-RP0 Healthy   0.15   0.15   0.14

        Memory (kB)
         Slot  Status    Total     Used (Pct)     Free (Pct) Committed (Pct)
        1-RP0 Healthy  4010000  2553084 (64%)  1456916 (36%)   3536536 (88%)
        2-RP0 Healthy  4010000  2449072 (61%)  1560928 (39%)   3433136 (86%)
        3-RP0 Healthy  4010000  1591792 (40%)  2418208 (60%)   1940852 (48%)
        4-RP0 Healthy  4010000  1598624 (40%)  2411376 (60%)   1950012 (49%)
        5-RP0 Healthy  4010000  1599180 (40%)  2410820 (60%)   1948956 (49%)

        CPU Utilization
         Slot  CPU   User System   Nice   Idle    IRQ   SIRQ IOwait
        1-RP0    0   3.89   2.09   0.00  93.80   0.00   0.19   0.00
                 1   5.70   1.00   0.00  93.20   0.00   0.10   0.00
                 2   4.89   0.89   0.00  94.10   0.00   0.09   0.00
                 3   4.70   1.40   0.00  93.80   0.00   0.00   0.10
        2-RP0    0   3.30   1.70   0.00  94.99   0.00   0.00   0.00
                 1   3.30   1.30   0.00  95.39   0.00   0.00   0.00
                 2   3.70   1.70   0.00  94.60   0.00   0.00   0.00
                 3   1.90   1.20   0.00  96.89   0.00   0.00   0.00
        3-RP0    0   1.90   3.50   0.00  94.60   0.00   0.00   0.00
                 1   3.40   3.40   0.00  93.20   0.00   0.00   0.00
                 2   3.30   2.70   0.00  94.00   0.00   0.00   0.00
                 3   1.90   2.60   0.00  95.49   0.00   0.00   0.00
        4-RP0    0   2.89   3.29   0.00  93.70   0.00   0.00   0.09
                 1   1.90   3.40   0.00  94.70   0.00   0.00   0.00
                 2   2.90   3.80   0.00  93.30   0.00   0.00   0.00
                 3   3.80   4.20   0.00  92.00   0.00   0.00   0.00
        5-RP0    0   1.80   0.80   0.00  97.39   0.00   0.00   0.00
                 1   1.40   0.50   0.00  98.10   0.00   0.00   0.00
                 2   1.90   1.30   0.00  96.80   0.00   0.00   0.00
                 3   2.09   0.79   0.00  97.10   0.00   0.00   0.00'''
    }

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


class TestShowPlatformSoftwareSlotActiveMonitorMemSwap(unittest.TestCase):

    dev = Device(name='c3850')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        "swap": {
            "used": 0,
            "total": 0,
            "available_memory": 1779488,
            "free": 0
        },
        "memory": {
            "used": 1530208,
            "total": 4010000,
            "buff_cache": 2466212,
            "free": 13580
        }
    }

    golden_output = {'execute.return_value': '''\
        show platform software process slot switch active R0 monitor | inc Mem :|Swap:    
        KiB Mem :  4010000 total,    13580 free,  1530208 used,  2466212 buff/cache
        KiB Swap:        0 total,        0 free,        0 used.  1779488 avail Mem 
    '''
    }

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


class TestShowProcessesCpuSortedCPU(unittest.TestCase):

    dev = Device(name='c3850')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        "five_sec_cpu_total": 7,
        "five_min_cpu": 6,
        "one_min_cpu": 6,
        "five_sec_cpu_interrupts": 1
    }

    golden_output = {'execute.return_value': '''\
        show processes cpu sorted 5min | inc CPU
        CPU utilization for five seconds: 7%/1%; one minute: 6%; five minutes: 6%
    '''
    }

    golden_parsed_output_1 = {
        "five_min_cpu": 6,
        "five_sec_cpu_interrupts": 1,
        "one_min_cpu": 6,
        "nonzero_cpu_processes": [
          "PLFM-MGR IPC pro",
          "Spanning Tree"
        ],
        "zero_cpu_processes": [
          "IPC Seat TX Cont"
        ],
        "five_sec_cpu_total": 5,
        "sort": {
            1: {
               "five_min_cpu": 0.54,
               "invoked": 6437005,
               "usecs": 1236,
               "one_min_cpu": 0.53,
               "tty": 0,
               "process": "PLFM-MGR IPC pro",
               "five_sec_cpu": 0.31,
               "runtime": 7962054,
               "pid": 152
            },
            2: {
               "five_min_cpu": 0.31,
               "invoked": 14602032,
               "usecs": 336,
               "one_min_cpu": 0.31,
               "tty": 0,
               "process": "Spanning Tree",
               "five_sec_cpu": 0.23,
               "runtime": 4915791,
               "pid": 242
            },
            3: {
               "five_min_cpu": 0.0,
               "invoked": 1,
               "usecs": 0,
               "one_min_cpu": 0.0,
               "tty": 0,
               "process": "IPC Seat TX Cont",
               "five_sec_cpu": 0.0,
               "runtime": 0,
               "pid": 32
            }
        }
    }

    golden_output_1 = {'execute.return_value': '''
        CPU utilization for five seconds: 5%/1%; one minute: 6%; five minutes: 6%
         PID Runtime(ms)     Invoked      uSecs   5Sec   1Min   5Min TTY Process          
         152     7962054     6437005       1236  0.31%  0.53%  0.54%   0 PLFM-MGR IPC pro 
         242     4915791    14602032        336  0.23%  0.31%  0.31%   0 Spanning Tree    
          32           0           1          0  0.00%  0.00%  0.00%   0 IPC Seat TX Cont
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

class TestShowProcessesCpuPlatform(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': '      '}

    golden_parsed_output = {'cpu_utilization': {'core': {'Core 0': {'core_cpu_util_five_min': '18%',
                                         'core_cpu_util_five_secs': '2%',
                                         'core_cpu_util_one_min': '8%'},
                              'Core 1': {'core_cpu_util_five_min': '23%',
                                         'core_cpu_util_five_secs': '0%',
                                         'core_cpu_util_one_min': '3%'}},
                     'cpu_util_five_min': '22%',
                     'cpu_util_five_secs': '2%',
                     'cpu_util_one_min': '5%'},
 'pid': {'1': {'five_min': '0%',
               'five_sec': '0%',
               'name': 'init',
               'one_min': '0%',
               'ppid': 0,
               'size': 1863680,
               'status': 'S'},
         '10': {'five_min': '0%',
                'five_sec': '0%',
                'name': 'sirq-tasklet/0',
                'one_min': '0%',
                'ppid': 2,
                'size': 0,
                'status': 'S'},
         '11': {'five_min': '0%',
                'five_sec': '0%',
                'name': 'sirq-sched/0',
                'one_min': '0%',
                'ppid': 2,
                'size': 0,
                'status': 'S'},
         '11125': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'sleep',
                   'one_min': '0%',
                   'ppid': 14891,
                   'size': 1929216,
                   'status': 'S'},
         '12': {'five_min': '0%',
                'five_sec': '0%',
                'name': 'sirq-hrtimer/0',
                'one_min': '0%',
                'ppid': 2,
                'size': 0,
                'status': 'S'},
         '1225': {'five_min': '0%',
                  'five_sec': '0%',
                  'name': 'scsi_eh_0',
                  'one_min': '0%',
                  'ppid': 2,
                  'size': 0,
                  'status': 'S'},
         '1227': {'five_min': '0%',
                  'five_sec': '0%',
                  'name': 'scsi_eh_1',
                  'one_min': '0%',
                  'ppid': 2,
                  'size': 0,
                  'status': 'S'},
         '1229': {'five_min': '0%',
                  'five_sec': '0%',
                  'name': 'scsi_eh_2',
                  'one_min': '0%',
                  'ppid': 2,
                  'size': 0,
                  'status': 'S'},
         '1231': {'five_min': '0%',
                  'five_sec': '0%',
                  'name': 'scsi_eh_3',
                  'one_min': '0%',
                  'ppid': 2,
                  'size': 0,
                  'status': 'S'},
         '12579': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'udevd',
                   'one_min': '0%',
                   'ppid': 1,
                   'size': 1773568,
                   'status': 'S'},
         '1268': {'five_min': '0%',
                  'five_sec': '0%',
                  'name': 'kstriped',
                  'one_min': '0%',
                  'ppid': 2,
                  'size': 0,
                  'status': 'S'},
         '1269': {'five_min': '0%',
                  'five_sec': '0%',
                  'name': 'pman.sh',
                  'one_min': '0%',
                  'ppid': 27708,
                  'size': 4407296,
                  'status': 'S'},
         '1271': {'five_min': '0%',
                  'five_sec': '0%',
                  'name': 'ksnapd',
                  'one_min': '0%',
                  'ppid': 2,
                  'size': 0,
                  'status': 'S'},
         '13': {'five_min': '0%',
                'five_sec': '0%',
                'name': 'sirq-rcu/0',
                'one_min': '0%',
                'ppid': 2,
                'size': 0,
                'status': 'S'},
         '1301': {'five_min': '0%',
                  'five_sec': '0%',
                  'name': 'usbhid_resumer',
                  'one_min': '0%',
                  'ppid': 2,
                  'size': 0,
                  'status': 'S'},
         '1316': {'five_min': '0%',
                  'five_sec': '0%',
                  'name': 'deferwq',
                  'one_min': '0%',
                  'ppid': 2,
                  'size': 0,
                  'status': 'S'},
         '1319': {'five_min': '0%',
                  'five_sec': '0%',
                  'name': 'scsi_eh_4',
                  'one_min': '0%',
                  'ppid': 2,
                  'size': 0,
                  'status': 'S'},
         '1320': {'five_min': '0%',
                  'five_sec': '0%',
                  'name': 'usb-storage',
                  'one_min': '0%',
                  'ppid': 2,
                  'size': 0,
                  'status': 'S'},
         '1325': {'five_min': '0%',
                  'five_sec': '0%',
                  'name': 'scsi_eh_5',
                  'one_min': '0%',
                  'ppid': 2,
                  'size': 0,
                  'status': 'S'},
         '1326': {'five_min': '0%',
                  'five_sec': '0%',
                  'name': 'usb-storage',
                  'one_min': '0%',
                  'ppid': 2,
                  'size': 0,
                  'status': 'S'},
         '14': {'five_min': '0%',
                'five_sec': '0%',
                'name': 'stopper/0',
                'one_min': '0%',
                'ppid': 2,
                'size': 0,
                'status': 'S'},
         '14891': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'auxport.sh',
                   'one_min': '0%',
                   'ppid': 1,
                   'size': 2818048,
                   'status': 'S'},
         '14898': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'reflector.sh',
                   'one_min': '0%',
                   'ppid': 1,
                   'size': 4722688,
                   'status': 'S'},
         '14905': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'droputil.sh',
                   'one_min': '0%',
                   'ppid': 1,
                   'size': 4706304,
                   'status': 'S'},
         '15': {'five_min': '0%',
                'five_sec': '0%',
                'name': 'watchdog/0',
                'one_min': '0%',
                'ppid': 2,
                'size': 0,
                'status': 'S'},
         '15034': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'automount',
                   'one_min': '0%',
                   'ppid': 1,
                   'size': 24010752,
                   'status': 'S'},
         '15087': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'xinetd',
                   'one_min': '0%',
                   'ppid': 1,
                   'size': 2187264,
                   'status': 'S'},
         '15089': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'xinetd',
                   'one_min': '0%',
                   'ppid': 1,
                   'size': 2187264,
                   'status': 'S'},
         '15121': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'lockd',
                   'one_min': '0%',
                   'ppid': 2,
                   'size': 0,
                   'status': 'S'},
         '15126': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'nfsd',
                   'one_min': '0%',
                   'ppid': 2,
                   'size': 0,
                   'status': 'S'},
         '15127': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'nfsd',
                   'one_min': '0%',
                   'ppid': 2,
                   'size': 0,
                   'status': 'S'},
         '15128': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'nfsd',
                   'one_min': '0%',
                   'ppid': 2,
                   'size': 0,
                   'status': 'S'},
         '15129': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'nfsd',
                   'one_min': '0%',
                   'ppid': 2,
                   'size': 0,
                   'status': 'S'},
         '15130': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'nfsd',
                   'one_min': '0%',
                   'ppid': 2,
                   'size': 0,
                   'status': 'S'},
         '15131': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'nfsd',
                   'one_min': '0%',
                   'ppid': 2,
                   'size': 0,
                   'status': 'S'},
         '15132': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'nfsd',
                   'one_min': '0%',
                   'ppid': 2,
                   'size': 0,
                   'status': 'S'},
         '15133': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'nfsd',
                   'one_min': '0%',
                   'ppid': 2,
                   'size': 0,
                   'status': 'S'},
         '15135': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'rpc.mountd',
                   'one_min': '0%',
                   'ppid': 1,
                   'size': 1789952,
                   'status': 'S'},
         '152': {'five_min': '0%',
                 'five_sec': '0%',
                 'name': 'sync_supers',
                 'one_min': '0%',
                 'ppid': 2,
                 'size': 0,
                 'status': 'S'},
         '15337': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'lsmpi-refill',
                   'one_min': '0%',
                   'ppid': 2,
                   'size': 0,
                   'status': 'S'},
         '15338': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'lsmpi-xmit',
                   'one_min': '0%',
                   'ppid': 2,
                   'size': 0,
                   'status': 'S'},
         '15339': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'lsmpi-rx',
                   'one_min': '0%',
                   'ppid': 2,
                   'size': 0,
                   'status': 'S'},
         '154': {'five_min': '0%',
                 'five_sec': '0%',
                 'name': 'bdi-default',
                 'one_min': '0%',
                 'ppid': 2,
                 'size': 0,
                 'status': 'S'},
         '155': {'five_min': '0%',
                 'five_sec': '0%',
                 'name': 'kblockd/0',
                 'one_min': '0%',
                 'ppid': 2,
                 'size': 0,
                 'status': 'S'},
         '156': {'five_min': '0%',
                 'five_sec': '0%',
                 'name': 'kblockd/1',
                 'one_min': '0%',
                 'ppid': 2,
                 'size': 0,
                 'status': 'S'},
         '157': {'five_min': '0%',
                 'five_sec': '0%',
                 'name': 'kacpid',
                 'one_min': '0%',
                 'ppid': 2,
                 'size': 0,
                 'status': 'S'},
         '15791': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'ddr_err_monitor',
                   'one_min': '0%',
                   'ppid': 2,
                   'size': 0,
                   'status': 'S'},
         '158': {'five_min': '0%',
                 'five_sec': '0%',
                 'name': 'kacpi_notify',
                 'one_min': '0%',
                 'ppid': 2,
                 'size': 0,
                 'status': 'S'},
         '15806': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'mtdblockd',
                   'one_min': '0%',
                   'ppid': 2,
                   'size': 0,
                   'status': 'S'},
         '15828': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'scansta',
                   'one_min': '0%',
                   'ppid': 2,
                   'size': 0,
                   'status': 'S'},
         '159': {'five_min': '0%',
                 'five_sec': '0%',
                 'name': 'kacpi_hotplug',
                 'one_min': '0%',
                 'ppid': 2,
                 'size': 0,
                 'status': 'S'},
         '16': {'five_min': '0%',
                'five_sec': '0%',
                'name': 'desched/0',
                'one_min': '0%',
                'ppid': 2,
                'size': 0,
                'status': 'S'},
         '1630': {'five_min': '0%',
                  'five_sec': '0%',
                  'name': 'pcscd',
                  'one_min': '0%',
                  'ppid': 31695,
                  'size': 10375168,
                  'status': 'S'},
         '1689': {'five_min': '0%',
                  'five_sec': '0%',
                  'name': 'rotee',
                  'one_min': '0%',
                  'ppid': 1,
                  'size': 4927488,
                  'status': 'S'},
         '17': {'five_min': '0%',
                'five_sec': '0%',
                'name': 'migration/1',
                'one_min': '0%',
                'ppid': 2,
                'size': 0,
                'status': 'S'},
         '1706': {'five_min': '0%',
                  'five_sec': '0%',
                  'name': 'rotee',
                  'one_min': '0%',
                  'ppid': 1,
                  'size': 4927488,
                  'status': 'S'},
         '1750': {'five_min': '0%',
                  'five_sec': '0%',
                  'name': 'pman.sh',
                  'one_min': '0%',
                  'ppid': 27708,
                  'size': 4431872,
                  'status': 'S'},
         '17957': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'rotee',
                   'one_min': '0%',
                   'ppid': 1,
                   'size': 4927488,
                   'status': 'S'},
         '1796': {'five_min': '0%',
                  'five_sec': '0%',
                  'name': 'rotee',
                  'one_min': '0%',
                  'ppid': 1,
                  'size': 4927488,
                  'status': 'S'},
         '18': {'five_min': '0%',
                'five_sec': '0%',
                'name': 'stopper/1',
                'one_min': '0%',
                'ppid': 2,
                'size': 0,
                'status': 'S'},
         '18040': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'rotee',
                   'one_min': '0%',
                   'ppid': 1,
                   'size': 4927488,
                   'status': 'S'},
         '18056': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'inotifywait',
                   'one_min': '0%',
                   'ppid': 14898,
                   'size': 1761280,
                   'status': 'S'},
         '18100': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'inotifywait',
                   'one_min': '0%',
                   'ppid': 14905,
                   'size': 1761280,
                   'status': 'S'},
         '19': {'five_min': '0%',
                'five_sec': '0%',
                'name': 'sirq-high/1',
                'one_min': '0%',
                'ppid': 2,
                'size': 0,
                'status': 'S'},
         '1900': {'five_min': '0%',
                  'five_sec': '0%',
                  'name': 'plogd',
                  'one_min': '0%',
                  'ppid': 32339,
                  'size': 20828160,
                  'status': 'S'},
         '2': {'five_min': '0%',
               'five_sec': '0%',
               'name': 'kthreadd',
               'one_min': '0%',
               'ppid': 0,
               'size': 0,
               'status': 'S'},
         '20': {'five_min': '0%',
                'five_sec': '0%',
                'name': 'sirq-timer/1',
                'one_min': '0%',
                'ppid': 2,
                'size': 0,
                'status': 'S'},
         '21': {'five_min': '0%',
                'five_sec': '0%',
                'name': 'sirq-net-tx/1',
                'one_min': '0%',
                'ppid': 2,
                'size': 0,
                'status': 'S'},
         '2160': {'five_min': '0%',
                  'five_sec': '0%',
                  'name': 'rotee',
                  'one_min': '0%',
                  'ppid': 1,
                  'size': 4927488,
                  'status': 'S'},
         '21718': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'mcp_chvrf.sh',
                   'one_min': '0%',
                   'ppid': 1,
                   'size': 2560000,
                   'status': 'S'},
         '21719': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'mcp_chvrf.sh',
                   'one_min': '0%',
                   'ppid': 1,
                   'size': 2560000,
                   'status': 'S'},
         '21721': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'sntp',
                   'one_min': '0%',
                   'ppid': 1,
                   'size': 1867776,
                   'status': 'S'},
         '21722': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'rollback_timer.',
                   'one_min': '0%',
                   'ppid': 1,
                   'size': 3059712,
                   'status': 'S'},
         '21726': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'xinetd',
                   'one_min': '0%',
                   'ppid': 21718,
                   'size': 2187264,
                   'status': 'S'},
         '21727': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'oom.sh',
                   'one_min': '0%',
                   'ppid': 1,
                   'size': 3026944,
                   'status': 'S'},
         '21729': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'xinetd',
                   'one_min': '0%',
                   'ppid': 21719,
                   'size': 2187264,
                   'status': 'S'},
         '21734': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'iptbl.sh',
                   'one_min': '0%',
                   'ppid': 1,
                   'size': 3710976,
                   'status': 'S'},
         '21737': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'libvirtd.sh',
                   'one_min': '0%',
                   'ppid': 1,
                   'size': 2551808,
                   'status': 'S'},
         '21742': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'libvirtd',
                   'one_min': '0%',
                   'ppid': 21737,
                   'size': 22347776,
                   'status': 'S'},
         '22': {'five_min': '0%',
                'five_sec': '0%',
                'name': 'sirq-net-rx/1',
                'one_min': '0%',
                'ppid': 2,
                'size': 0,
                'status': 'S'},
         '22012': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'rotee',
                   'one_min': '0%',
                   'ppid': 1,
                   'size': 4927488,
                   'status': 'S'},
         '22049': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'inotifywait',
                   'one_min': '0%',
                   'ppid': 21734,
                   'size': 1757184,
                   'status': 'S'},
         '22052': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'rotee',
                   'one_min': '0%',
                   'ppid': 1,
                   'size': 4927488,
                   'status': 'S'},
         '22054': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'rotee',
                   'one_min': '0%',
                   'ppid': 1,
                   'size': 4927488,
                   'status': 'S'},
         '22086': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'inotifywait',
                   'one_min': '0%',
                   'ppid': 21722,
                   'size': 1757184,
                   'status': 'S'},
         '22097': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'sleep',
                   'one_min': '0%',
                   'ppid': 21727,
                   'size': 1929216,
                   'status': 'S'},
         '23': {'five_min': '0%',
                'five_sec': '0%',
                'name': 'sirq-block/1',
                'one_min': '0%',
                'ppid': 2,
                'size': 0,
                'status': 'S'},
         '23402': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'chasync.sh',
                   'one_min': '0%',
                   'ppid': 1,
                   'size': 4034560,
                   'status': 'S'},
         '23672': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'rotee',
                   'one_min': '0%',
                   'ppid': 1,
                   'size': 4927488,
                   'status': 'S'},
         '23740': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'inotifywait',
                   'one_min': '0%',
                   'ppid': 23402,
                   'size': 1761280,
                   'status': 'S'},
         '24': {'five_min': '0%',
                'five_sec': '0%',
                'name': 'sirq-block-iopo',
                'one_min': '0%',
                'ppid': 2,
                'size': 0,
                'status': 'S'},
         '25': {'five_min': '0%',
                'five_sec': '0%',
                'name': 'sirq-tasklet/1',
                'one_min': '0%',
                'ppid': 2,
                'size': 0,
                'status': 'S'},
         '26': {'five_min': '0%',
                'five_sec': '0%',
                'name': 'sirq-sched/1',
                'one_min': '0%',
                'ppid': 2,
                'size': 0,
                'status': 'S'},
         '2648': {'five_min': '0%',
                  'five_sec': '0%',
                  'name': 'rpciod/0',
                  'one_min': '0%',
                  'ppid': 2,
                  'size': 0,
                  'status': 'S'},
         '2649': {'five_min': '0%',
                  'five_sec': '0%',
                  'name': 'rpciod/1',
                  'one_min': '0%',
                  'ppid': 2,
                  'size': 0,
                  'status': 'S'},
         '2655': {'five_min': '0%',
                  'five_sec': '0%',
                  'name': 'nfsiod',
                  'one_min': '0%',
                  'ppid': 2,
                  'size': 0,
                  'status': 'S'},
         '27': {'five_min': '0%',
                'five_sec': '0%',
                'name': 'sirq-hrtimer/1',
                'one_min': '0%',
                'ppid': 2,
                'size': 0,
                'status': 'S'},
         '275': {'five_min': '0%',
                 'five_sec': '0%',
                 'name': 'ata/0',
                 'one_min': '0%',
                 'ppid': 2,
                 'size': 0,
                 'status': 'S'},
         '27578': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'klogd',
                   'one_min': '0%',
                   'ppid': 1,
                   'size': 1654784,
                   'status': 'S'},
         '276': {'five_min': '0%',
                 'five_sec': '0%',
                 'name': 'ata/1',
                 'one_min': '0%',
                 'ppid': 2,
                 'size': 0,
                 'status': 'S'},
         '277': {'five_min': '0%',
                 'five_sec': '0%',
                 'name': 'ata_aux',
                 'one_min': '0%',
                 'ppid': 2,
                 'size': 0,
                 'status': 'S'},
         '27708': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'pvp.sh',
                   'one_min': '0%',
                   'ppid': 1,
                   'size': 4521984,
                   'status': 'S'},
         '27791': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'rotee',
                   'one_min': '0%',
                   'ppid': 1,
                   'size': 4927488,
                   'status': 'S'},
         '2794': {'five_min': '4%',
                  'five_sec': '0%',
                  'name': 'smand',
                  'one_min': '4%',
                  'ppid': 1269,
                  'size': 154185728,
                  'status': 'S'},
         '28': {'five_min': '0%',
                'five_sec': '0%',
                'name': 'sirq-rcu/1',
                'one_min': '0%',
                'ppid': 2,
                'size': 0,
                'status': 'S'},
         '28080': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'inotifywait',
                   'one_min': '0%',
                   'ppid': 27708,
                   'size': 1761280,
                   'status': 'S'},
         '281': {'five_min': '0%',
                 'five_sec': '0%',
                 'name': 'khubd',
                 'one_min': '0%',
                 'ppid': 2,
                 'size': 0,
                 'status': 'S'},
         '28156': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'pman.sh',
                   'one_min': '0%',
                   'ppid': 27708,
                   'size': 4427776,
                   'status': 'S'},
         '28264': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'pman.sh',
                   'one_min': '0%',
                   'ppid': 27708,
                   'size': 4407296,
                   'status': 'S'},
         '2833': {'five_min': '0%',
                  'five_sec': '0%',
                  'name': 'psd',
                  'one_min': '0%',
                  'ppid': 824,
                  'size': 20340736,
                  'status': 'S'},
         '28362': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'rotee',
                   'one_min': '0%',
                   'ppid': 1,
                   'size': 4927488,
                   'status': 'S'},
         '284': {'five_min': '0%',
                 'five_sec': '0%',
                 'name': 'kseriod',
                 'one_min': '0%',
                 'ppid': 2,
                 'size': 0,
                 'status': 'S'},
         '28464': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'pman.sh',
                   'one_min': '0%',
                   'ppid': 27708,
                   'size': 4407296,
                   'status': 'S'},
         '28562': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'rotee',
                   'one_min': '0%',
                   'ppid': 1,
                   'size': 4927488,
                   'status': 'S'},
         '28801': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'rotee',
                   'one_min': '0%',
                   'ppid': 1,
                   'size': 4927488,
                   'status': 'S'},
         '28831': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'pman.sh',
                   'one_min': '0%',
                   'ppid': 27708,
                   'size': 4407296,
                   'status': 'S'},
         '2896': {'five_min': '0%',
                  'five_sec': '0%',
                  'name': 'flush-8:16',
                  'one_min': '0%',
                  'ppid': 2,
                  'size': 0,
                  'status': 'S'},
         '28996': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'btrace_rotate.s',
                   'one_min': '0%',
                   'ppid': 28156,
                   'size': 4009984,
                   'status': 'S'},
         '29': {'five_min': '0%',
                'five_sec': '0%',
                'name': 'watchdog/1',
                'one_min': '0%',
                'ppid': 2,
                'size': 0,
                'status': 'S'},
         '29041': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'cmand',
                   'one_min': '0%',
                   'ppid': 28264,
                   'size': 39702528,
                   'status': 'S'},
         '29140': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'rotee',
                   'one_min': '0%',
                   'ppid': 1,
                   'size': 4927488,
                   'status': 'S'},
         '2931': {'five_min': '0%',
                  'five_sec': '0%',
                  'name': 'flush-8:0',
                  'one_min': '0%',
                  'ppid': 2,
                  'size': 0,
                  'status': 'S'},
         '29439': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'rotee',
                   'one_min': '0%',
                   'ppid': 1,
                   'size': 4927488,
                   'status': 'S'},
         '29452': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'pman.sh',
                   'one_min': '0%',
                   'ppid': 27708,
                   'size': 4407296,
                   'status': 'S'},
         '29495': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'emd',
                   'one_min': '0%',
                   'ppid': 28464,
                   'size': 27250688,
                   'status': 'S'},
         '29699': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'pman.sh',
                   'one_min': '0%',
                   'ppid': 27708,
                   'size': 4407296,
                   'status': 'S'},
         '29704': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'rotee',
                   'one_min': '0%',
                   'ppid': 1,
                   'size': 4927488,
                   'status': 'S'},
         '29787': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'fman_rp',
                   'one_min': '0%',
                   'ppid': 28831,
                   'size': 4294967295,
                   'status': 'S'},
         '29949': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'rotee',
                   'one_min': '0%',
                   'ppid': 1,
                   'size': 4927488,
                   'status': 'S'},
         '3': {'five_min': '0%',
               'five_sec': '0%',
               'name': 'migration/0',
               'one_min': '0%',
               'ppid': 2,
               'size': 0,
               'status': 'S'},
         '30': {'five_min': '0%',
                'five_sec': '0%',
                'name': 'desched/1',
                'one_min': '0%',
                'ppid': 2,
                'size': 0,
                'status': 'S'},
         '30526': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'imand',
                   'one_min': '0%',
                   'ppid': 29699,
                   'size': 52994048,
                   'status': 'S'},
         '30643': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'pman.sh',
                   'one_min': '0%',
                   'ppid': 27708,
                   'size': 4407296,
                   'status': 'S'},
         '3074': {'five_min': '0%',
                  'five_sec': '0%',
                  'name': 'portmap',
                  'one_min': '0%',
                  'ppid': 1,
                  'size': 1810432,
                  'status': 'S'},
         '3076': {'five_min': '0%',
                  'five_sec': '0%',
                  'name': 'portmap',
                  'one_min': '0%',
                  'ppid': 1,
                  'size': 1810432,
                  'status': 'S'},
         '30914': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'hman',
                   'one_min': '0%',
                   'ppid': 29452,
                   'size': 43081728,
                   'status': 'R'},
         '30953': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'rotee',
                   'one_min': '0%',
                   'ppid': 1,
                   'size': 4927488,
                   'status': 'S'},
         '31': {'five_min': '0%',
                'five_sec': '0%',
                'name': 'events/0',
                'one_min': '0%',
                'ppid': 2,
                'size': 0,
                'status': 'S'},
         '31695': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'pman.sh',
                   'one_min': '0%',
                   'ppid': 27708,
                   'size': 4407296,
                   'status': 'S'},
         '31700': {'five_min': '32%',
                   'five_sec': '1%',
                   'name': 'linux_iosd-imag',
                   'one_min': '5%',
                   'ppid': 30643,
                   'size': 4294967295,
                   'status': 'S'},
         '3180': {'five_min': '0%',
                  'five_sec': '0%',
                  'name': 'loop1',
                  'one_min': '0%',
                  'ppid': 2,
                  'size': 0,
                  'status': 'S'},
         '32': {'five_min': '0%',
                'five_sec': '0%',
                'name': 'events/1',
                'one_min': '0%',
                'ppid': 2,
                'size': 0,
                'status': 'S'},
         '32105': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'pman.sh',
                   'one_min': '0%',
                   'ppid': 27708,
                   'size': 4431872,
                   'status': 'S'},
         '3221': {'five_min': '0%',
                  'five_sec': '0%',
                  'name': 'loop2',
                  'one_min': '0%',
                  'ppid': 2,
                  'size': 0,
                  'status': 'S'},
         '32309': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'rotee',
                   'one_min': '0%',
                   'ppid': 1,
                   'size': 4927488,
                   'status': 'S'},
         '32339': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'pman.sh',
                   'one_min': '0%',
                   'ppid': 27708,
                   'size': 4407296,
                   'status': 'S'},
         '32609': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'rotee',
                   'one_min': '0%',
                   'ppid': 1,
                   'size': 4927488,
                   'status': 'S'},
         '3270': {'five_min': '0%',
                  'five_sec': '0%',
                  'name': 'loop3',
                  'one_min': '0%',
                  'ppid': 2,
                  'size': 0,
                  'status': 'S'},
         '32706': {'five_min': '0%',
                   'five_sec': '0%',
                   'name': 'rotee',
                   'one_min': '0%',
                   'ppid': 1,
                   'size': 4927488,
                   'status': 'S'},
         '33': {'five_min': '0%',
                'five_sec': '0%',
                'name': 'cpuset',
                'one_min': '0%',
                'ppid': 2,
                'size': 0,
                'status': 'S'},
         '3314': {'five_min': '0%',
                  'five_sec': '0%',
                  'name': 'loop4',
                  'one_min': '0%',
                  'ppid': 2,
                  'size': 0,
                  'status': 'S'},
         '337': {'five_min': '0%',
                 'five_sec': '0%',
                 'name': 'khungtaskd',
                 'one_min': '0%',
                 'ppid': 2,
                 'size': 0,
                 'status': 'S'},
         '338': {'five_min': '0%',
                 'five_sec': '0%',
                 'name': 'kswapd0',
                 'one_min': '0%',
                 'ppid': 2,
                 'size': 0,
                 'status': 'S'},
         '3381': {'five_min': '0%',
                  'five_sec': '0%',
                  'name': 'pman.sh',
                  'one_min': '0%',
                  'ppid': 27708,
                  'size': 4407296,
                  'status': 'S'},
         '34': {'five_min': '0%',
                'five_sec': '0%',
                'name': 'khelper',
                'one_min': '0%',
                'ppid': 2,
                'size': 0,
                'status': 'S'},
         '3421': {'five_min': '0%',
                  'five_sec': '0%',
                  'name': 'sort_files_by_i',
                  'one_min': '0%',
                  'ppid': 1750,
                  'size': 4227072,
                  'status': 'S'},
         '3466': {'five_min': '0%',
                  'five_sec': '0%',
                  'name': 'loop5',
                  'one_min': '0%',
                  'ppid': 2,
                  'size': 0,
                  'status': 'S'},
         '3508': {'five_min': '0%',
                  'five_sec': '0%',
                  'name': 'loop6',
                  'one_min': '0%',
                  'ppid': 2,
                  'size': 0,
                  'status': 'S'},
         '3547': {'five_min': '0%',
                  'five_sec': '0%',
                  'name': 'loop7',
                  'one_min': '0%',
                  'ppid': 2,
                  'size': 0,
                  'status': 'S'},
         '3641': {'five_min': '0%',
                  'five_sec': '0%',
                  'name': 'loop8',
                  'one_min': '0%',
                  'ppid': 2,
                  'size': 0,
                  'status': 'S'},
         '37': {'five_min': '0%',
                'five_sec': '0%',
                'name': 'netns',
                'one_min': '0%',
                'ppid': 2,
                'size': 0,
                'status': 'S'},
         '3742': {'five_min': '0%',
                  'five_sec': '0%',
                  'name': 'flush-8:32',
                  'one_min': '0%',
                  'ppid': 2,
                  'size': 0,
                  'status': 'S'},
         '392': {'five_min': '0%',
                 'five_sec': '0%',
                 'name': 'aio/0',
                 'one_min': '0%',
                 'ppid': 2,
                 'size': 0,
                 'status': 'S'},
         '393': {'five_min': '0%',
                 'five_sec': '0%',
                 'name': 'aio/1',
                 'one_min': '0%',
                 'ppid': 2,
                 'size': 0,
                 'status': 'S'},
         '3990': {'five_min': '0%',
                  'five_sec': '0%',
                  'name': 'loop9',
                  'one_min': '0%',
                  'ppid': 2,
                  'size': 0,
                  'status': 'S'},
         '4': {'five_min': '0%',
               'five_sec': '0%',
               'name': 'sirq-high/0',
               'one_min': '0%',
               'ppid': 2,
               'size': 0,
               'status': 'S'},
         '40': {'five_min': '0%',
                'five_sec': '0%',
                'name': 'async/mgr',
                'one_min': '0%',
                'ppid': 2,
                'size': 0,
                'status': 'S'},
         '4084': {'five_min': '0%',
                  'five_sec': '0%',
                  'name': 'loop10',
                  'one_min': '0%',
                  'ppid': 2,
                  'size': 0,
                  'status': 'S'},
         '410': {'five_min': '0%',
                 'five_sec': '0%',
                 'name': 'crypto/0',
                 'one_min': '0%',
                 'ppid': 2,
                 'size': 0,
                 'status': 'S'},
         '411': {'five_min': '0%',
                 'five_sec': '0%',
                 'name': 'crypto/1',
                 'one_min': '0%',
                 'ppid': 2,
                 'size': 0,
                 'status': 'S'},
         '4217': {'five_min': '0%',
                  'five_sec': '0%',
                  'name': 'rotee',
                  'one_min': '0%',
                  'ppid': 1,
                  'size': 4927488,
                  'status': 'S'},
         '4758': {'five_min': '0%',
                  'five_sec': '0%',
                  'name': 'vman',
                  'one_min': '0%',
                  'ppid': 3381,
                  'size': 186593280,
                  'status': 'S'},
         '5': {'five_min': '0%',
               'five_sec': '0%',
               'name': 'sirq-timer/0',
               'one_min': '0%',
               'ppid': 2,
               'size': 0,
               'status': 'S'},
         '550': {'five_min': '0%',
                 'five_sec': '0%',
                 'name': 'periodic.sh',
                 'one_min': '0%',
                 'ppid': 32105,
                 'size': 5353472,
                 'status': 'S'},
         '6': {'five_min': '0%',
               'five_sec': '0%',
               'name': 'sirq-net-tx/0',
               'one_min': '0%',
               'ppid': 2,
               'size': 0,
               'status': 'S'},
         '7': {'five_min': '0%',
               'five_sec': '0%',
               'name': 'sirq-net-rx/0',
               'one_min': '0%',
               'ppid': 2,
               'size': 0,
               'status': 'S'},
         '8': {'five_min': '0%',
               'five_sec': '0%',
               'name': 'sirq-block/0',
               'one_min': '0%',
               'ppid': 2,
               'size': 0,
               'status': 'S'},
         '824': {'five_min': '0%',
                 'five_sec': '0%',
                 'name': 'pman.sh',
                 'one_min': '0%',
                 'ppid': 27708,
                 'size': 4407296,
                 'status': 'S'},
         '8330': {'five_min': '0%',
                  'five_sec': '0%',
                  'name': 'sleep',
                  'one_min': '0%',
                  'ppid': 550,
                  'size': 1929216,
                  'status': 'S'},
         '8496': {'five_min': '0%',
                  'five_sec': '0%',
                  'name': 'sleep',
                  'one_min': '0%',
                  'ppid': 3421,
                  'size': 1929216,
                  'status': 'S'},
         '8643': {'five_min': '0%',
                  'five_sec': '0%',
                  'name': 'inotifywait',
                  'one_min': '0%',
                  'ppid': 28996,
                  'size': 1757184,
                  'status': 'S'},
         '9': {'five_min': '0%',
               'five_sec': '0%',
               'name': 'sirq-block-iopo',
               'one_min': '0%',
               'ppid': 2,
               'size': 0,
               'status': 'S'}}}

    golden_output = {'execute.return_value': '''\
        Router#show processes cpu platform 
        Load for five secs: 1%/0%; one minute: 9%; five minutes: 19%
        Time source is NTP, 17:48:03.994 EST Wed Oct 19 2016
        CPU utilization for five seconds:  2%, one minute:  5%, five minutes: 22%
        Core 0: CPU utilization for five seconds:  2%, one minute:  8%, five minutes: 18%
        Core 1: CPU utilization for five seconds:  0%, one minute:  3%, five minutes: 23%
           Pid    PPid    5Sec    1Min    5Min  Status        Size  Name                  
        --------------------------------------------------------------------------------
             1       0      0%      0%      0%  S          1863680  init                  
             2       0      0%      0%      0%  S                0  kthreadd              
             3       2      0%      0%      0%  S                0  migration/0           
             4       2      0%      0%      0%  S                0  sirq-high/0           
             5       2      0%      0%      0%  S                0  sirq-timer/0          
             6       2      0%      0%      0%  S                0  sirq-net-tx/0         
             7       2      0%      0%      0%  S                0  sirq-net-rx/0         
             8       2      0%      0%      0%  S                0  sirq-block/0          
             9       2      0%      0%      0%  S                0  sirq-block-iopo       
            10       2      0%      0%      0%  S                0  sirq-tasklet/0        
            11       2      0%      0%      0%  S                0  sirq-sched/0          
            12       2      0%      0%      0%  S                0  sirq-hrtimer/0        
            13       2      0%      0%      0%  S                0  sirq-rcu/0            
            14       2      0%      0%      0%  S                0  stopper/0             
            15       2      0%      0%      0%  S                0  watchdog/0            
            16       2      0%      0%      0%  S                0  desched/0             
            17       2      0%      0%      0%  S                0  migration/1           
            18       2      0%      0%      0%  S                0  stopper/1             
            19       2      0%      0%      0%  S                0  sirq-high/1           
            20       2      0%      0%      0%  S                0  sirq-timer/1          
            21       2      0%      0%      0%  S                0  sirq-net-tx/1         
            22       2      0%      0%      0%  S                0  sirq-net-rx/1         
            23       2      0%      0%      0%  S                0  sirq-block/1          
            24       2      0%      0%      0%  S                0  sirq-block-iopo       
            25       2      0%      0%      0%  S                0  sirq-tasklet/1        
            26       2      0%      0%      0%  S                0  sirq-sched/1          
            27       2      0%      0%      0%  S                0  sirq-hrtimer/1        
            28       2      0%      0%      0%  S                0  sirq-rcu/1            
            29       2      0%      0%      0%  S                0  watchdog/1            
            30       2      0%      0%      0%  S                0  desched/1             
            31       2      0%      0%      0%  S                0  events/0              
            32       2      0%      0%      0%  S                0  events/1              
            33       2      0%      0%      0%  S                0  cpuset                
            34       2      0%      0%      0%  S                0  khelper               
            37       2      0%      0%      0%  S                0  netns                 
            40       2      0%      0%      0%  S                0  async/mgr             
           152       2      0%      0%      0%  S                0  sync_supers           
           154       2      0%      0%      0%  S                0  bdi-default           
           155       2      0%      0%      0%  S                0  kblockd/0             
           156       2      0%      0%      0%  S                0  kblockd/1             
           157       2      0%      0%      0%  S                0  kacpid                
           158       2      0%      0%      0%  S                0  kacpi_notify          
           159       2      0%      0%      0%  S                0  kacpi_hotplug         
           275       2      0%      0%      0%  S                0  ata/0                 
           276       2      0%      0%      0%  S                0  ata/1                 
           277       2      0%      0%      0%  S                0  ata_aux               
           281       2      0%      0%      0%  S                0  khubd                 
           284       2      0%      0%      0%  S                0  kseriod               
           337       2      0%      0%      0%  S                0  khungtaskd            
           338       2      0%      0%      0%  S                0  kswapd0               
           392       2      0%      0%      0%  S                0  aio/0                 
           393       2      0%      0%      0%  S                0  aio/1                 
           410       2      0%      0%      0%  S                0  crypto/0              
           411       2      0%      0%      0%  S                0  crypto/1              
           550   32105      0%      0%      0%  S          5353472  periodic.sh           
           824   27708      0%      0%      0%  S          4407296  pman.sh               
          1225       2      0%      0%      0%  S                0  scsi_eh_0             
          1227       2      0%      0%      0%  S                0  scsi_eh_1             
          1229       2      0%      0%      0%  S                0  scsi_eh_2             
          1231       2      0%      0%      0%  S                0  scsi_eh_3             
          1268       2      0%      0%      0%  S                0  kstriped              
          1269   27708      0%      0%      0%  S          4407296  pman.sh               
          1271       2      0%      0%      0%  S                0  ksnapd                
          1301       2      0%      0%      0%  S                0  usbhid_resumer        
          1316       2      0%      0%      0%  S                0  deferwq               
          1319       2      0%      0%      0%  S                0  scsi_eh_4             
          1320       2      0%      0%      0%  S                0  usb-storage           
          1325       2      0%      0%      0%  S                0  scsi_eh_5             
          1326       2      0%      0%      0%  S                0  usb-storage           
          1630   31695      0%      0%      0%  S         10375168  pcscd                 
          1689       1      0%      0%      0%  S          4927488  rotee                 
          1706       1      0%      0%      0%  S          4927488  rotee                 
          1750   27708      0%      0%      0%  S          4431872  pman.sh               
          1796       1      0%      0%      0%  S          4927488  rotee                 
          1900   32339      0%      0%      0%  S         20828160  plogd                 
          2160       1      0%      0%      0%  S          4927488  rotee                 
          2648       2      0%      0%      0%  S                0  rpciod/0              
          2649       2      0%      0%      0%  S                0  rpciod/1              
          2655       2      0%      0%      0%  S                0  nfsiod                
          2794    1269      0%      4%      4%  S        154185728  smand                 
          2833     824      0%      0%      0%  S         20340736  psd                   
          2896       2      0%      0%      0%  S                0  flush-8:16            
          2931       2      0%      0%      0%  S                0  flush-8:0             
          3074       1      0%      0%      0%  S          1810432  portmap               
          3076       1      0%      0%      0%  S          1810432  portmap               
          3180       2      0%      0%      0%  S                0  loop1                 
          3221       2      0%      0%      0%  S                0  loop2                 
          3270       2      0%      0%      0%  S                0  loop3                 
          3314       2      0%      0%      0%  S                0  loop4                 
          3381   27708      0%      0%      0%  S          4407296  pman.sh               
          3421    1750      0%      0%      0%  S          4227072  sort_files_by_i       
          3466       2      0%      0%      0%  S                0  loop5                 
          3508       2      0%      0%      0%  S                0  loop6                 
          3547       2      0%      0%      0%  S                0  loop7                 
          3641       2      0%      0%      0%  S                0  loop8                 
          3742       2      0%      0%      0%  S                0  flush-8:32            
          3990       2      0%      0%      0%  S                0  loop9                 
          4084       2      0%      0%      0%  S                0  loop10                
          4217       1      0%      0%      0%  S          4927488  rotee                 
          4758    3381      0%      0%      0%  S        186593280  vman                  
          8330     550      0%      0%      0%  S          1929216  sleep                 
          8496    3421      0%      0%      0%  S          1929216  sleep                 
          8643   28996      0%      0%      0%  S          1757184  inotifywait           
         11125   14891      0%      0%      0%  S          1929216  sleep                 
         12579       1      0%      0%      0%  S          1773568  udevd                 
         14891       1      0%      0%      0%  S          2818048  auxport.sh            
         14898       1      0%      0%      0%  S          4722688  reflector.sh          
         14905       1      0%      0%      0%  S          4706304  droputil.sh           
         15034       1      0%      0%      0%  S         24010752  automount             
         15087       1      0%      0%      0%  S          2187264  xinetd                
         15089       1      0%      0%      0%  S          2187264  xinetd                
         15121       2      0%      0%      0%  S                0  lockd                 
         15126       2      0%      0%      0%  S                0  nfsd                  
         15127       2      0%      0%      0%  S                0  nfsd                  
         15128       2      0%      0%      0%  S                0  nfsd                  
         15129       2      0%      0%      0%  S                0  nfsd                  
         15130       2      0%      0%      0%  S                0  nfsd                  
         15131       2      0%      0%      0%  S                0  nfsd                  
         15132       2      0%      0%      0%  S                0  nfsd                  
         15133       2      0%      0%      0%  S                0  nfsd                  
         15135       1      0%      0%      0%  S          1789952  rpc.mountd            
         15337       2      0%      0%      0%  S                0  lsmpi-refill          
         15338       2      0%      0%      0%  S                0  lsmpi-xmit            
         15339       2      0%      0%      0%  S                0  lsmpi-rx              
         15791       2      0%      0%      0%  S                0  ddr_err_monitor       
         15806       2      0%      0%      0%  S                0  mtdblockd             
         15828       2      0%      0%      0%  S                0  scansta               
         17957       1      0%      0%      0%  S          4927488  rotee                 
         18040       1      0%      0%      0%  S          4927488  rotee                 
         18056   14898      0%      0%      0%  S          1761280  inotifywait           
         18100   14905      0%      0%      0%  S          1761280  inotifywait           
         21718       1      0%      0%      0%  S          2560000  mcp_chvrf.sh          
         21719       1      0%      0%      0%  S          2560000  mcp_chvrf.sh          
         21721       1      0%      0%      0%  S          1867776  sntp                  
         21722       1      0%      0%      0%  S          3059712  rollback_timer.       
         21726   21718      0%      0%      0%  S          2187264  xinetd                
         21727       1      0%      0%      0%  S          3026944  oom.sh                
         21729   21719      0%      0%      0%  S          2187264  xinetd                
         21734       1      0%      0%      0%  S          3710976  iptbl.sh              
         21737       1      0%      0%      0%  S          2551808  libvirtd.sh           
         21742   21737      0%      0%      0%  S         22347776  libvirtd              
         22012       1      0%      0%      0%  S          4927488  rotee                 
         22049   21734      0%      0%      0%  S          1757184  inotifywait           
         22052       1      0%      0%      0%  S          4927488  rotee                 
         22054       1      0%      0%      0%  S          4927488  rotee                 
         22086   21722      0%      0%      0%  S          1757184  inotifywait           
         22097   21727      0%      0%      0%  S          1929216  sleep                 
         23402       1      0%      0%      0%  S          4034560  chasync.sh            
         23672       1      0%      0%      0%  S          4927488  rotee                 
         23740   23402      0%      0%      0%  S          1761280  inotifywait           
         27578       1      0%      0%      0%  S          1654784  klogd                 
         27708       1      0%      0%      0%  S          4521984  pvp.sh                
         27791       1      0%      0%      0%  S          4927488  rotee                 
         28080   27708      0%      0%      0%  S          1761280  inotifywait           
         28156   27708      0%      0%      0%  S          4427776  pman.sh               
         28264   27708      0%      0%      0%  S          4407296  pman.sh               
         28362       1      0%      0%      0%  S          4927488  rotee                 
         28464   27708      0%      0%      0%  S          4407296  pman.sh               
         28562       1      0%      0%      0%  S          4927488  rotee                 
         28801       1      0%      0%      0%  S          4927488  rotee                 
         28831   27708      0%      0%      0%  S          4407296  pman.sh               
         28996   28156      0%      0%      0%  S          4009984  btrace_rotate.s       
         29041   28264      0%      0%      0%  S         39702528  cmand                 
         29140       1      0%      0%      0%  S          4927488  rotee                 
         29439       1      0%      0%      0%  S          4927488  rotee                 
         29452   27708      0%      0%      0%  S          4407296  pman.sh               
         29495   28464      0%      0%      0%  S         27250688  emd                   
         29699   27708      0%      0%      0%  S          4407296  pman.sh               
         29704       1      0%      0%      0%  S          4927488  rotee                 
         29787   28831      0%      0%      0%  S       4294967295  fman_rp               
         29949       1      0%      0%      0%  S          4927488  rotee                 
         30526   29699      0%      0%      0%  S         52994048  imand                 
         30643   27708      0%      0%      0%  S          4407296  pman.sh               
         30914   29452      0%      0%      0%  R         43081728  hman                  
         30953       1      0%      0%      0%  S          4927488  rotee                 
         31695   27708      0%      0%      0%  S          4407296  pman.sh               
         31700   30643      1%      5%     32%  S       4294967295  linux_iosd-imag       
         32105   27708      0%      0%      0%  S          4431872  pman.sh               
         32309       1      0%      0%      0%  S          4927488  rotee                 
         32339   27708      0%      0%      0%  S          4407296  pman.sh               
         32609       1      0%      0%      0%  S          4927488  rotee                 
         32706       1      0%      0%      0%  S          4927488  rotee 
    '''
    }

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        cpu_platform_obj = ShowProcessesCpuPlatform(device=self.device)
        parsed_output = cpu_platform_obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        cpu_platform_obj = ShowProcessesCpuPlatform(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = cpu_platform_obj.parse()


class TestShowEnv(unittest.TestCase):

    dev = Device(name='c3850')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {'critical_larams': 0,
 'major_alarms': 0,
 'minor_alarms': 0,
 'slot': {'0': {'sensor': {'Temp: Asic1': {'reading': '50 Celsius',
                                           'state': 'Normal'},
                           'Temp: Center': {'reading': '37 Celsius',
                                            'state': 'Normal'},
                           'Temp: Left': {'reading': '30 Celsius',
                                          'state': 'Normal'},
                           'Temp: Right': {'reading': '35 Celsius',
                                           'state': 'Normal'},
                           'V1: 12v': {'reading': '11894 mV',
                                       'state': 'Normal'},
                           'V1: GP1': {'reading': '749 mV',
                                       'state': 'Normal'},
                           'V1: GP2': {'reading': '898 mV',
                                       'state': 'Normal'},
                           'V1: VDD': {'reading': '3295 mV',
                                       'state': 'Normal'},
                           'V1: VMA': {'reading': '1098 mV',
                                       'state': 'Normal'},
                           'V1: VMB': {'reading': '1196 mV',
                                       'state': 'Normal'},
                           'V1: VMC': {'reading': '1494 mV',
                                       'state': 'Normal'},
                           'V1: VMD': {'reading': '1796 mV',
                                       'state': 'Normal'},
                           'V1: VME': {'reading': '2490 mV',
                                       'state': 'Normal'},
                           'V1: VMF': {'reading': '3286 mV',
                                       'state': 'Normal'},
                           'V2: 12v': {'reading': '11865 mV',
                                       'state': 'Normal'},
                           'V2: GP2': {'reading': '747 mV',
                                       'state': 'Normal'},
                           'V2: VDD': {'reading': '3295 mV',
                                       'state': 'Normal'},
                           'V2: VMB': {'reading': '996 mV',
                                       'state': 'Normal'},
                           'V2: VME': {'reading': '747 mV',
                                       'state': 'Normal'},
                           'V2: VMF': {'reading': '747 mV',
                                       'state': 'Normal'}}},
          '1': {'sensor': {'Temp: Asic1': {'reading': '38 Celsius',
                                           'state': 'Normal'},
                           'Temp: Center': {'reading': '29 Celsius',
                                            'state': 'Normal'},
                           'Temp: Left': {'reading': '26 Celsius',
                                          'state': 'Normal'},
                           'Temp: Right': {'reading': '29 Celsius',
                                           'state': 'Normal'},
                           'V1: 12v': {'reading': '11879 mV',
                                       'state': 'Normal'},
                           'V1: GP1': {'reading': '747 mV',
                                       'state': 'Normal'},
                           'V1: GP2': {'reading': '891 mV',
                                       'state': 'Normal'},
                           'V1: VDD': {'reading': '3291 mV',
                                       'state': 'Normal'},
                           'V1: VMA': {'reading': '1098 mV',
                                       'state': 'Normal'},
                           'V1: VMB': {'reading': '1196 mV',
                                       'state': 'Normal'},
                           'V1: VMC': {'reading': '1494 mV',
                                       'state': 'Normal'},
                           'V1: VMD': {'reading': '1791 mV',
                                       'state': 'Normal'},
                           'V1: VME': {'reading': '2490 mV',
                                       'state': 'Normal'},
                           'V1: VMF': {'reading': '3286 mV',
                                       'state': 'Normal'},
                           'V2: 12v': {'reading': '11865 mV',
                                       'state': 'Normal'},
                           'V2: GP2': {'reading': '749 mV',
                                       'state': 'Normal'},
                           'V2: VDD': {'reading': '3295 mV',
                                       'state': 'Normal'},
                           'V2: VMB': {'reading': '996 mV',
                                       'state': 'Normal'},
                           'V2: VME': {'reading': '747 mV',
                                       'state': 'Normal'},
                           'V2: VMF': {'reading': '747 mV',
                                       'state': 'Normal'}}},
          'F0': {'sensor': {'Temp: CPP Rear': {'reading': '40 Celsius',
                                               'state': 'Normal'},
                            'Temp: HKP Die': {'reading': '47 Celsius',
                                              'state': 'Normal'},
                            'Temp: Inlet': {'reading': '30 Celsius',
                                            'state': 'Normal'},
                            'Temp: Left Ext': {'reading': '42 Celsius',
                                               'state': 'Normal'},
                            'Temp: MCH Die': {'reading': '53 Celsius',
                                              'state': 'Normal'},
                            'Temp: Olv Die': {'reading': '38 Celsius',
                                              'state': 'Normal'},
                            'Temp: Pop Die': {'reading': '43 Celsius',
                                              'state': 'Normal'},
                            'Temp: Rght Ext': {'reading': '37 Celsius',
                                               'state': 'Normal'},
                            'V1: 12v': {'reading': '11821 mV',
                                        'state': 'Normal'},
                            'V1: GP1': {'reading': '908 mV',
                                        'state': 'Normal'},
                            'V1: GP2': {'reading': '771 mV',
                                        'state': 'Normal'},
                            'V1: VDD': {'reading': '3295 mV',
                                        'state': 'Normal'},
                            'V1: VMA': {'reading': '1796 mV',
                                        'state': 'Normal'},
                            'V1: VMB': {'reading': '1196 mV',
                                        'state': 'Normal'},
                            'V1: VMC': {'reading': '996 mV',
                                        'state': 'Normal'},
                            'V1: VMD': {'reading': '1044 mV',
                                        'state': 'Normal'},
                            'V1: VME': {'reading': '1020 mV',
                                        'state': 'Normal'},
                            'V1: VMF': {'reading': '1098 mV',
                                        'state': 'Normal'},
                            'V2: 12v': {'reading': '11748 mV',
                                        'state': 'Normal'},
                            'V2: GP1': {'reading': '771 mV',
                                        'state': 'Normal'},
                            'V2: GP2': {'reading': '1096 mV',
                                        'state': 'Normal'},
                            'V2: VDD': {'reading': '3295 mV',
                                        'state': 'Normal'},
                            'V2: VMA': {'reading': '3291 mV',
                                        'state': 'Normal'},
                            'V2: VMB': {'reading': '2495 mV',
                                        'state': 'Normal'},
                            'V2: VMC': {'reading': '1499 mV',
                                        'state': 'Normal'},
                            'V2: VMD': {'reading': '1196 mV',
                                        'state': 'Normal'},
                            'V2: VME': {'reading': '1103 mV',
                                        'state': 'Normal'},
                            'V2: VMF': {'reading': '1000 mV',
                                        'state': 'Normal'},
                            'V3: 12v': {'reading': '11850 mV',
                                        'state': 'Normal'},
                            'V3: VDD': {'reading': '3300 mV',
                                        'state': 'Normal'},
                            'V3: VMA': {'reading': '3291 mV',
                                        'state': 'Normal'},
                            'V3: VMB': {'reading': '2495 mV',
                                        'state': 'Normal'},
                            'V3: VMC': {'reading': '1499 mV',
                                        'state': 'Normal'},
                            'V3: VMD': {'reading': '1000 mV',
                                        'state': 'Normal'}}},
          'F1': {'sensor': {'Temp: CPP Rear': {'reading': '46 Celsius',
                                               'state': 'Normal'},
                            'Temp: HKP Die': {'reading': '52 Celsius',
                                              'state': 'Normal'},
                            'Temp: Inlet': {'reading': '31 Celsius',
                                            'state': 'Normal'},
                            'Temp: Left Ext': {'reading': '43 Celsius',
                                               'state': 'Normal'},
                            'Temp: MCH Die': {'reading': '54 Celsius',
                                              'state': 'Normal'},
                            'Temp: Olv Die': {'reading': '41 Celsius',
                                              'state': 'Normal'},
                            'Temp: Pop Die': {'reading': '48 Celsius',
                                              'state': 'Normal'},
                            'Temp: Rght Ext': {'reading': '37 Celsius',
                                               'state': 'Normal'},
                            'V1: 12v': {'reading': '11821 mV',
                                        'state': 'Normal'},
                            'V1: GP1': {'reading': '903 mV',
                                        'state': 'Normal'},
                            'V1: GP2': {'reading': '769 mV',
                                        'state': 'Normal'},
                            'V1: VDD': {'reading': '3295 mV',
                                        'state': 'Normal'},
                            'V1: VMA': {'reading': '1796 mV',
                                        'state': 'Normal'},
                            'V1: VMB': {'reading': '1196 mV',
                                        'state': 'Normal'},
                            'V1: VMC': {'reading': '996 mV',
                                        'state': 'Normal'},
                            'V1: VMD': {'reading': '1049 mV',
                                        'state': 'Normal'},
                            'V1: VME': {'reading': '1035 mV',
                                        'state': 'Normal'},
                            'V1: VMF': {'reading': '1098 mV',
                                        'state': 'Normal'},
                            'V2: 12v': {'reading': '11762 mV',
                                        'state': 'Normal'},
                            'V2: GP1': {'reading': '771 mV',
                                        'state': 'Normal'},
                            'V2: GP2': {'reading': '1088 mV',
                                        'state': 'Normal'},
                            'V2: VDD': {'reading': '3295 mV',
                                        'state': 'Normal'},
                            'V2: VMA': {'reading': '3291 mV',
                                        'state': 'Normal'},
                            'V2: VMB': {'reading': '2495 mV',
                                        'state': 'Normal'},
                            'V2: VMC': {'reading': '1499 mV',
                                        'state': 'Normal'},
                            'V2: VMD': {'reading': '1196 mV',
                                        'state': 'Normal'},
                            'V2: VME': {'reading': '1098 mV',
                                        'state': 'Normal'},
                            'V2: VMF': {'reading': '996 mV',
                                        'state': 'Normal'},
                            'V3: 12v': {'reading': '11806 mV',
                                        'state': 'Normal'},
                            'V3: VDD': {'reading': '3295 mV',
                                        'state': 'Normal'},
                            'V3: VMA': {'reading': '3286 mV',
                                        'state': 'Normal'},
                            'V3: VMB': {'reading': '2495 mV',
                                        'state': 'Normal'},
                            'V3: VMC': {'reading': '1494 mV',
                                        'state': 'Normal'},
                            'V3: VMD': {'reading': '996 mV',
                                        'state': 'Normal'}}},
          'P0': {'sensor': {'Iin': {'reading': '1 A', 'state': 'Normal'},
                            'Iout': {'reading': '15 A', 'state': 'Normal'},
                            'Temp1': {'reading': '26 Celsius',
                                      'state': 'Normal'},
                            'Temp2': {'reading': '31 Celsius',
                                      'state': 'Normal'},
                            'Temp3': {'reading': '26 Celsius',
                                      'state': 'Normal'},
                            'Vin': {'reading': '101 V AC',
                                    'state': 'Normal'},
                            'Vout': {'reading': '12 V AC',
                                     'state': 'Normal'}}},
          'P1': {'sensor': {'Iin': {'reading': '2 A', 'state': 'Normal'},
                            'Iout': {'reading': '16 A', 'state': 'Normal'},
                            'Temp1': {'reading': '26 Celsius',
                                      'state': 'Normal'},
                            'Temp2': {'reading': '33 Celsius',
                                      'state': 'Normal'},
                            'Temp3': {'reading': '26 Celsius',
                                      'state': 'Normal'},
                            'Vin': {'reading': '101 V AC',
                                    'state': 'Normal'},
                            'Vout': {'reading': '12 V AC',
                                     'state': 'Normal'}}},
          'P2': {'sensor': {'Iin': {'reading': '1 A', 'state': 'Normal'},
                            'Iout': {'reading': '13 A', 'state': 'Normal'},
                            'Temp1': {'reading': '26 Celsius',
                                      'state': 'Normal'},
                            'Temp2': {'reading': '31 Celsius',
                                      'state': 'Normal'},
                            'Temp3': {'reading': '26 Celsius',
                                      'state': 'Normal'},
                            'Vin': {'reading': '101 V AC',
                                    'state': 'Normal'},
                            'Vout': {'reading': '12 V AC',
                                     'state': 'Normal'}}},
          'P3': {'sensor': {'Iin': {'reading': '1 A', 'state': 'Normal'},
                            'Iout': {'reading': '13 A', 'state': 'Normal'},
                            'Temp1': {'reading': '26 Celsius',
                                      'state': 'Normal'},
                            'Temp2': {'reading': '31 Celsius',
                                      'state': 'Normal'},
                            'Temp3': {'reading': '26 Celsius',
                                      'state': 'Normal'},
                            'Vin': {'reading': '100 V AC',
                                    'state': 'Normal'},
                            'Vout': {'reading': '12 V AC',
                                     'state': 'Normal'}}},
          'P6': {'sensor': {'Temp1': {'reading': '38 Celsius',
                                      'state': 'Normal'},
                            'Temp: FC PWM1': {'reading': '26 Celsius',
                                              'state': 'Fan Speed 60%'}}},
          'P7': {'sensor': {'Temp1': {'reading': '37 Celsius',
                                      'state': 'Normal'},
                            'Temp: FC PWM1': {'reading': '26 Celsius',
                                              'state': 'Fan Speed 60%'}}},
          'R0': {'sensor': {'Temp: C2D C0': {'reading': '35 Celsius',
                                             'state': 'Normal'},
                            'Temp: C2D C1': {'reading': '37 Celsius',
                                             'state': 'Normal'},
                            'Temp: CPU AIR': {'reading': '32 Celsius',
                                              'state': 'Normal'},
                            'Temp: Inlet': {'reading': '26 Celsius',
                                            'state': 'Normal'},
                            'Temp: MCH AIR': {'reading': '40 Celsius',
                                              'state': 'Normal'},
                            'Temp: MCH DIE': {'reading': '54 Celsius',
                                              'state': 'Normal'},
                            'Temp: Outlet': {'reading': '30 Celsius',
                                             'state': 'Normal'},
                            'Temp: SCBY AIR': {'reading': '45 Celsius',
                                               'state': 'Normal'},
                            'V1: 12v': {'reading': '11835 mV',
                                        'state': 'Normal'},
                            'V1: GP1': {'reading': '910 mV',
                                        'state': 'Normal'},
                            'V1: GP2': {'reading': '1198 mV',
                                        'state': 'Normal'},
                            'V1: VDD': {'reading': '3295 mV',
                                        'state': 'Normal'},
                            'V1: VMA': {'reading': '1201 mV',
                                        'state': 'Normal'},
                            'V1: VMB': {'reading': '2495 mV',
                                        'state': 'Normal'},
                            'V1: VMC': {'reading': '3291 mV',
                                        'state': 'Normal'},
                            'V1: VMD': {'reading': '2495 mV',
                                        'state': 'Normal'},
                            'V1: VME': {'reading': '1796 mV',
                                        'state': 'Normal'},
                            'V1: VMF': {'reading': '1528 mV',
                                        'state': 'Normal'},
                            'V2: 12v': {'reading': '11850 mV',
                                        'state': 'Normal'},
                            'V2: GP1': {'reading': '2497 mV',
                                        'state': 'Normal'},
                            'V2: GP2': {'reading': '1196 mV',
                                        'state': 'Normal'},
                            'V2: VDD': {'reading': '3300 mV',
                                        'state': 'Normal'},
                            'V2: VMA': {'reading': '1049 mV',
                                        'state': 'Normal'},
                            'V2: VMB': {'reading': '1098 mV',
                                        'state': 'Normal'},
                            'V2: VMD': {'reading': '996 mV',
                                        'state': 'Normal'},
                            'V2: VME': {'reading': '1098 mV',
                                        'state': 'Normal'},
                            'V2: VMF': {'reading': '996 mV',
                                        'state': 'Normal'}}},
          'R1': {'sensor': {'Temp: C2D C0': {'reading': '36 Celsius',
                                             'state': 'Normal'},
                            'Temp: C2D C1': {'reading': '33 Celsius',
                                             'state': 'Normal'},
                            'Temp: CPU AIR': {'reading': '32 Celsius',
                                              'state': 'Normal'},
                            'Temp: Inlet': {'reading': '25 Celsius',
                                            'state': 'Normal'},
                            'Temp: MCH AIR': {'reading': '39 Celsius',
                                              'state': 'Normal'},
                            'Temp: MCH DIE': {'reading': '53 Celsius',
                                              'state': 'Normal'},
                            'Temp: Outlet': {'reading': '30 Celsius',
                                             'state': 'Normal'},
                            'Temp: SCBY AIR': {'reading': '40 Celsius',
                                               'state': 'Normal'},
                            'V1: 12v': {'reading': '11835 mV',
                                        'state': 'Normal'},
                            'V1: GP1': {'reading': '910 mV',
                                        'state': 'Normal'},
                            'V1: GP2': {'reading': '1198 mV',
                                        'state': 'Normal'},
                            'V1: VDD': {'reading': '3305 mV',
                                        'state': 'Normal'},
                            'V1: VMA': {'reading': '1201 mV',
                                        'state': 'Normal'},
                            'V1: VMB': {'reading': '2495 mV',
                                        'state': 'Normal'},
                            'V1: VMC': {'reading': '3291 mV',
                                        'state': 'Normal'},
                            'V1: VMD': {'reading': '2495 mV',
                                        'state': 'Normal'},
                            'V1: VME': {'reading': '1796 mV',
                                        'state': 'Normal'},
                            'V1: VMF': {'reading': '1528 mV',
                                        'state': 'Normal'},
                            'V2: 12v': {'reading': '11821 mV',
                                        'state': 'Normal'},
                            'V2: GP1': {'reading': '2497 mV',
                                        'state': 'Normal'},
                            'V2: GP2': {'reading': '1196 mV',
                                        'state': 'Normal'},
                            'V2: VDD': {'reading': '3305 mV',
                                        'state': 'Normal'},
                            'V2: VMA': {'reading': '1044 mV',
                                        'state': 'Normal'},
                            'V2: VMB': {'reading': '1098 mV',
                                        'state': 'Normal'},
                            'V2: VMD': {'reading': '991 mV',
                                        'state': 'Normal'},
                            'V2: VME': {'reading': '1098 mV',
                                        'state': 'Normal'},
                            'V2: VMF': {'reading': '1000 mV',
                                        'state': 'Normal'}}},
          'Slot': {'sensor': {'Sensor': {'reading': 'State       Reading',
                                         'state': 'Current'}}}}}

    golden_output = {'execute.return_value': '''\
        Router#show environment
        Load for five secs: 4%/0%; one minute: 8%; five minutes: 6%
        Time source is NTP, 17:41:24.716 EST Wed Oct 19 2016


        Number of Critical alarms:  0
        Number of Major alarms:     0
        Number of Minor alarms:     0

        Slot    Sensor       Current State       Reading
        ----    ------       -------------       -------
         F0    V1: VMA          Normal           1796 mV
         F0    V1: VMB          Normal           1196 mV
         F0    V1: VMC          Normal           996 mV
         F0    V1: VMD          Normal           1044 mV
         F0    V1: VME          Normal           1020 mV
         F0    V1: VMF          Normal           1098 mV
         F0    V1: 12v          Normal           11821 mV
         F0    V1: VDD          Normal           3295 mV
         F0    V1: GP1          Normal           908 mV
         F0    V1: GP2          Normal           771 mV
         F0    V2: VMA          Normal           3291 mV
         F0    V2: VMB          Normal           2495 mV
         F0    V2: VMC          Normal           1499 mV
         F0    V2: VMD          Normal           1196 mV
         F0    V2: VME          Normal           1103 mV
         F0    V2: VMF          Normal           1000 mV
         F0    V2: 12v          Normal           11748 mV
         F0    V2: VDD          Normal           3295 mV
         F0    V2: GP1          Normal           771 mV
         F0    V2: GP2          Normal           1096 mV
         F0    Temp: Inlet      Normal           30 Celsius
         F0    Temp: Pop Die    Normal           43 Celsius
         F0    Temp: Left Ext   Normal           42 Celsius
         F0    Temp: HKP Die    Normal           47 Celsius
         F0    Temp: CPP Rear   Normal           40 Celsius
         F0    Temp: Olv Die    Normal           38 Celsius
         F0    Temp: Rght Ext   Normal           37 Celsius
         F0    Temp: MCH Die    Normal           53 Celsius
         F0    V3: VMA          Normal           3291 mV
         F0    V3: VMB          Normal           2495 mV
         F0    V3: VMC          Normal           1499 mV
         F0    V3: VMD          Normal           1000 mV
         F0    V3: 12v          Normal           11850 mV
         F0    V3: VDD          Normal           3300 mV
         P0    Vin              Normal           101 V AC
         P0    Iin              Normal           1 A
         P0    Vout             Normal           12 V AC
         P0    Iout             Normal           15 A
         P0    Temp1            Normal           26 Celsius
         P0    Temp2            Normal           31 Celsius
         P0    Temp3            Normal           26 Celsius
         P1    Vin              Normal           101 V AC
         P1    Iin              Normal           2 A
         P1    Vout             Normal           12 V AC
         P1    Iout             Normal           16 A
         P1    Temp1            Normal           26 Celsius
         P1    Temp2            Normal           33 Celsius
         P1    Temp3            Normal           26 Celsius
         P6    Temp1            Normal           38 Celsius
         P6    Temp: FC PWM1    Fan Speed 60%    26 Celsius
         P7    Temp1            Normal           37 Celsius
         P7    Temp: FC PWM1    Fan Speed 60%    26 Celsius
         R0    V1: VMA          Normal           1201 mV
         R0    V1: VMB          Normal           2495 mV
         R0    V1: VMC          Normal           3291 mV
         R0    V1: VMD          Normal           2495 mV
         R0    V1: VME          Normal           1796 mV
         R0    V1: VMF          Normal           1528 mV
         R0    V1: 12v          Normal           11835 mV
         R0    V1: VDD          Normal           3295 mV
         R0    V1: GP1          Normal           910 mV
         R0    V1: GP2          Normal           1198 mV
         R0    V2: VMA          Normal           1049 mV
         R0    V2: VMB          Normal           1098 mV
         R0    V2: VMD          Normal           996 mV
         R0    V2: VME          Normal           1098 mV
         R0    V2: VMF          Normal           996 mV
         R0    V2: 12v          Normal           11850 mV
         R0    V2: VDD          Normal           3300 mV
         R0    V2: GP1          Normal           2497 mV
         R0    V2: GP2          Normal           1196 mV
         R0    Temp: Outlet     Normal           30 Celsius
         R0    Temp: CPU AIR    Normal           32 Celsius
         R0    Temp: Inlet      Normal           26 Celsius
         R0    Temp: SCBY AIR   Normal           45 Celsius
         R0    Temp: MCH DIE    Normal           54 Celsius
         R0    Temp: MCH AIR    Normal           40 Celsius
         R0    Temp: C2D C0     Normal           35 Celsius
         R0    Temp: C2D C1     Normal           37 Celsius
         R1    V1: VMA          Normal           1201 mV
         R1    V1: VMB          Normal           2495 mV
         R1    V1: VMC          Normal           3291 mV
         R1    V1: VMD          Normal           2495 mV
         R1    V1: VME          Normal           1796 mV
         R1    V1: VMF          Normal           1528 mV
         R1    V1: 12v          Normal           11835 mV
         R1    V1: VDD          Normal           3305 mV
         R1    V1: GP1          Normal           910 mV
         R1    V1: GP2          Normal           1198 mV
         R1    V2: VMA          Normal           1044 mV
         R1    V2: VMB          Normal           1098 mV
         R1    V2: VMD          Normal           991 mV
         R1    V2: VME          Normal           1098 mV
         R1    V2: VMF          Normal           1000 mV
         R1    V2: 12v          Normal           11821 mV
         R1    V2: VDD          Normal           3305 mV
         R1    V2: GP1          Normal           2497 mV
         R1    V2: GP2          Normal           1196 mV
         R1    Temp: Outlet     Normal           30 Celsius
         R1    Temp: CPU AIR    Normal           32 Celsius
         R1    Temp: Inlet      Normal           25 Celsius
         R1    Temp: SCBY AIR   Normal           40 Celsius
         R1    Temp: MCH DIE    Normal           53 Celsius
         R1    Temp: MCH AIR    Normal           39 Celsius
         R1    Temp: C2D C0     Normal           36 Celsius
         R1    Temp: C2D C1     Normal           33 Celsius
         0     V1: VMA          Normal           1098 mV
         0     V1: VMB          Normal           1196 mV
         0     V1: VMC          Normal           1494 mV
         0     V1: VMD          Normal           1796 mV
         0     V1: VME          Normal           2490 mV
         0     V1: VMF          Normal           3286 mV
         0     V1: 12v          Normal           11894 mV
         0     V1: VDD          Normal           3295 mV
         0     V1: GP1          Normal           749 mV
         0     V1: GP2          Normal           898 mV
         0     V2: VMB          Normal           996 mV
         0     V2: VME          Normal           747 mV
         0     V2: VMF          Normal           747 mV
         0     V2: 12v          Normal           11865 mV
         0     V2: VDD          Normal           3295 mV
         0     V2: GP2          Normal           747 mV
         0     Temp: Left       Normal           30 Celsius
         0     Temp: Center     Normal           37 Celsius
         0     Temp: Asic1      Normal           50 Celsius
         0     Temp: Right      Normal           35 Celsius
         F1    V1: VMA          Normal           1796 mV
         F1    V1: VMB          Normal           1196 mV
         F1    V1: VMC          Normal           996 mV
         F1    V1: VMD          Normal           1049 mV
         F1    V1: VME          Normal           1035 mV
         F1    V1: VMF          Normal           1098 mV
         F1    V1: 12v          Normal           11821 mV
         F1    V1: VDD          Normal           3295 mV
         F1    V1: GP1          Normal           903 mV
         F1    V1: GP2          Normal           769 mV
         F1    V2: VMA          Normal           3291 mV
         F1    V2: VMB          Normal           2495 mV
         F1    V2: VMC          Normal           1499 mV
         F1    V2: VMD          Normal           1196 mV
         F1    V2: VME          Normal           1098 mV
         F1    V2: VMF          Normal           996 mV
         F1    V2: 12v          Normal           11762 mV
         F1    V2: VDD          Normal           3295 mV
         F1    V2: GP1          Normal           771 mV
         F1    V2: GP2          Normal           1088 mV
         F1    Temp: Inlet      Normal           31 Celsius
         F1    Temp: Pop Die    Normal           48 Celsius
         F1    Temp: Left Ext   Normal           43 Celsius
         F1    Temp: HKP Die    Normal           52 Celsius
         F1    Temp: CPP Rear   Normal           46 Celsius
         F1    Temp: Olv Die    Normal           41 Celsius
         F1    Temp: Rght Ext   Normal           37 Celsius
         F1    Temp: MCH Die    Normal           54 Celsius
         F1    V3: VMA          Normal           3286 mV
         F1    V3: VMB          Normal           2495 mV
         F1    V3: VMC          Normal           1494 mV
         F1    V3: VMD          Normal           996 mV
         F1    V3: 12v          Normal           11806 mV
         F1    V3: VDD          Normal           3295 mV
         1     V1: VMA          Normal           1098 mV
         1     V1: VMB          Normal           1196 mV
         1     V1: VMC          Normal           1494 mV
         1     V1: VMD          Normal           1791 mV
         1     V1: VME          Normal           2490 mV
         1     V1: VMF          Normal           3286 mV
         1     V1: 12v          Normal           11879 mV
         1     V1: VDD          Normal           3291 mV
         1     V1: GP1          Normal           747 mV
         1     V1: GP2          Normal           891 mV
         1     V2: VMB          Normal           996 mV
         1     V2: VME          Normal           747 mV
         1     V2: VMF          Normal           747 mV
         1     V2: 12v          Normal           11865 mV
         1     V2: VDD          Normal           3295 mV
         1     V2: GP2          Normal           749 mV
         1     Temp: Left       Normal           26 Celsius
         1     Temp: Center     Normal           29 Celsius
         1     Temp: Asic1      Normal           38 Celsius
         1     Temp: Right      Normal           29 Celsius
         P2    Vin              Normal           101 V AC
         P2    Iin              Normal           1 A
         P2    Vout             Normal           12 V AC
         P2    Iout             Normal           13 A
         P2    Temp1            Normal           26 Celsius
         P2    Temp2            Normal           31 Celsius
         P2    Temp3            Normal           26 Celsius
         P3    Vin              Normal           100 V AC
         P3    Iin              Normal           1 A
         P3    Vout             Normal           12 V AC
         P3    Iout             Normal           13 A
         P3    Temp1            Normal           26 Celsius
         P3    Temp2            Normal           31 Celsius
         P3    Temp3            Normal           26 Celsius
    '''
    }

    golden_parsed_output2 = {
        "slot": {
            "P6": {
                "sensor": {
                    "Temp: FC PWM1": {
                        "state": "Fan Speed 45%",
                        "reading": "25 Celsius"
                    }
                }
            },
            "P7": {
                "sensor": {
                    "Temp: FC PWM1": {
                        "state": "Fan Speed 45%",
                        "reading": "25 Celsius"
                    }
                }
            }
        }
    }

    golden_output2 = {'execute.return_value': '''
        show environment | include Fan Speed
        P6    Temp: FC PWM1    Fan Speed 45%    25 Celsius
        P7    Temp: FC PWM1    Fan Speed 45%    25 Celsius
    '''}

    
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

    def test_golden2(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output2)
        obj = ShowEnvironment(device=self.dev)
        parsed_output = obj.parse(include='Fan Speed')
        self.assertEqual(parsed_output, self.golden_parsed_output2)

class TestShowProcessesCpu(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {'five_min_cpu': 3,
 'five_sec_cpu_interrupts': 0,
 'five_sec_cpu_total': 1,
 'nonzero_cpu_processes': ['Check heaps',
                           'IOSD ipc task',
                           'IOSXE-RP Punt Se',
                           'Per-Second Jobs',
                           'VRRS Main thread',
                           'IP ARP Retry Age',
                           'BGP Scanner',
                           'MMA DB TIMER',
                           'MFI LFD Stats Pr',
                           'BGP Router',
                           'Virtual Exec'],
 'one_min_cpu': 2,
 'sort': {1: {'five_min_cpu': 0.0,
              'five_sec_cpu': 0.0,
              'invoked': 1016,
              'one_min_cpu': 0.0,
              'pid': 1,
              'process': 'Chunk Manager',
              'runtime': 15,
              'tty': 0,
              'usecs': 14},
          2: {'five_min_cpu': 0.0,
              'five_sec_cpu': 0.0,
              'invoked': 6576,
              'one_min_cpu': 0.0,
              'pid': 2,
              'process': 'Load Meter',
              'runtime': 1883,
              'tty': 0,
              'usecs': 286},
          3: {'five_min_cpu': 0.0,
              'five_sec_cpu': 0.0,
              'invoked': 2,
              'one_min_cpu': 0.0,
              'pid': 3,
              'process': 'SpanTree Helper',
              'runtime': 2,
              'tty': 0,
              'usecs': 1000},
          4: {'five_min_cpu': 0.0,
              'five_sec_cpu': 0.0,
              'invoked': 120,
              'one_min_cpu': 0.0,
              'pid': 4,
              'process': 'Retransmission o',
              'runtime': 2,
              'tty': 0,
              'usecs': 16},
          5: {'five_min_cpu': 0.0,
              'five_sec_cpu': 0.0,
              'invoked': 4,
              'one_min_cpu': 0.0,
              'pid': 5,
              'process': 'IPC ISSU Dispatc',
              'runtime': 1,
              'tty': 0,
              'usecs': 250},
          6: {'five_min_cpu': 0.0,
              'five_sec_cpu': 0.0,
              'invoked': 210,
              'one_min_cpu': 0.0,
              'pid': 6,
              'process': 'RF Slave Main Th',
              'runtime': 48,
              'tty': 0,
              'usecs': 228},
          7: {'five_min_cpu': 0.0,
              'five_sec_cpu': 0.0,
              'invoked': 1,
              'one_min_cpu': 0.0,
              'pid': 7,
              'process': 'EDDRI_MAIN',
              'runtime': 0,
              'tty': 0,
              'usecs': 0},
          8: {'five_min_cpu': 0.0,
              'five_sec_cpu': 0.0,
              'invoked': 34,
              'one_min_cpu': 0.0,
              'pid': 8,
              'process': 'RO Notify Timers',
              'runtime': 0,
              'tty': 0,
              'usecs': 0},
          9: {'five_min_cpu': 0.46,
              'five_sec_cpu': 0.0,
              'invoked': 11390,
              'one_min_cpu': 0.59,
              'pid': 9,
              'process': 'Check heaps',
              'runtime': 192629,
              'tty': 0,
              'usecs': 16912},
          10: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 556,
               'one_min_cpu': 0.0,
               'pid': 10,
               'process': 'Pool Manager',
               'runtime': 60,
               'tty': 0,
               'usecs': 107},
          11: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 4,
               'one_min_cpu': 0.0,
               'pid': 11,
               'process': 'DiscardQ Backgro',
               'runtime': 21,
               'tty': 0,
               'usecs': 5250},
          12: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 2,
               'one_min_cpu': 0.0,
               'pid': 12,
               'process': 'Timers',
               'runtime': 0,
               'tty': 0,
               'usecs': 0},
          13: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 6865,
               'one_min_cpu': 0.0,
               'pid': 13,
               'process': 'WATCH_AFS',
               'runtime': 8,
               'tty': 0,
               'usecs': 1},
          14: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 1,
               'one_min_cpu': 0.0,
               'pid': 14,
               'process': 'MEMLEAK PROCESS',
               'runtime': 0,
               'tty': 0,
               'usecs': 0},
          15: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 50568,
               'one_min_cpu': 0.0,
               'pid': 15,
               'process': 'ARP Input',
               'runtime': 2538,
               'tty': 0,
               'usecs': 50},
          16: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 34824,
               'one_min_cpu': 0.0,
               'pid': 16,
               'process': 'ARP Background',
               'runtime': 413,
               'tty': 0,
               'usecs': 11},
          17: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 2,
               'one_min_cpu': 0.0,
               'pid': 17,
               'process': 'ATM Idle Timer',
               'runtime': 0,
               'tty': 0,
               'usecs': 0},
          18: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 1,
               'one_min_cpu': 0.0,
               'pid': 18,
               'process': 'ATM ASYNC PROC',
               'runtime': 0,
               'tty': 0,
               'usecs': 0},
          19: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 1,
               'one_min_cpu': 0.0,
               'pid': 19,
               'process': 'AAA_SERVER_DEADT',
               'runtime': 0,
               'tty': 0,
               'usecs': 0},
          20: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 1,
               'one_min_cpu': 0.0,
               'pid': 20,
               'process': 'Policy Manager',
               'runtime': 0,
               'tty': 0,
               'usecs': 0},
          21: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 2,
               'one_min_cpu': 0.0,
               'pid': 21,
               'process': 'DDR Timers',
               'runtime': 0,
               'tty': 0,
               'usecs': 0},
          22: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 54,
               'one_min_cpu': 0.0,
               'pid': 22,
               'process': 'Entity MIB API',
               'runtime': 65,
               'tty': 0,
               'usecs': 1203},
          23: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 254,
               'one_min_cpu': 0.0,
               'pid': 23,
               'process': 'PrstVbl',
               'runtime': 148,
               'tty': 0,
               'usecs': 582},
          24: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 1,
               'one_min_cpu': 0.0,
               'pid': 24,
               'process': 'RMI RM Notify Wa',
               'runtime': 0,
               'tty': 0,
               'usecs': 0},
          25: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 16446,
               'one_min_cpu': 0.0,
               'pid': 25,
               'process': 'IOSXE heartbeat',
               'runtime': 150,
               'tty': 0,
               'usecs': 9},
          26: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 2,
               'one_min_cpu': 0.0,
               'pid': 26,
               'process': 'ATM AutoVC Perio',
               'runtime': 0,
               'tty': 0,
               'usecs': 0},
          27: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 2,
               'one_min_cpu': 0.0,
               'pid': 27,
               'process': 'ATM VC Auto Crea',
               'runtime': 0,
               'tty': 0,
               'usecs': 0},
          28: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 73,
               'one_min_cpu': 0.0,
               'pid': 28,
               'process': 'IPC Apps Task',
               'runtime': 3,
               'tty': 0,
               'usecs': 41},
          29: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 11,
               'one_min_cpu': 0.0,
               'pid': 29,
               'process': 'ifIndex Receive',
               'runtime': 0,
               'tty': 0,
               'usecs': 0},
          30: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 6580,
               'one_min_cpu': 0.0,
               'pid': 30,
               'process': 'IPC Event Notifi',
               'runtime': 36,
               'tty': 0,
               'usecs': 5},
          31: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 32091,
               'one_min_cpu': 0.0,
               'pid': 31,
               'process': 'IPC Mcast Pendin',
               'runtime': 161,
               'tty': 0,
               'usecs': 5},
          32: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 1,
               'one_min_cpu': 0.0,
               'pid': 32,
               'process': 'ASR1000 appsess',
               'runtime': 0,
               'tty': 0,
               'usecs': 0},
          33: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 549,
               'one_min_cpu': 0.0,
               'pid': 33,
               'process': 'IPC Dynamic Cach',
               'runtime': 12,
               'tty': 0,
               'usecs': 21},
          34: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 6678,
               'one_min_cpu': 0.0,
               'pid': 34,
               'process': 'IPC Service NonC',
               'runtime': 593,
               'tty': 0,
               'usecs': 88},
          35: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 1,
               'one_min_cpu': 0.0,
               'pid': 35,
               'process': 'IPC Zone Manager',
               'runtime': 0,
               'tty': 0,
               'usecs': 0},
          36: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 32091,
               'one_min_cpu': 0.0,
               'pid': 36,
               'process': 'IPC Periodic Tim',
               'runtime': 239,
               'tty': 0,
               'usecs': 7},
          37: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 32090,
               'one_min_cpu': 0.0,
               'pid': 37,
               'process': 'IPC Deferred Por',
               'runtime': 176,
               'tty': 0,
               'usecs': 5},
          38: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 1,
               'one_min_cpu': 0.0,
               'pid': 38,
               'process': 'IPC Process leve',
               'runtime': 0,
               'tty': 0,
               'usecs': 0},
          39: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 15214,
               'one_min_cpu': 0.0,
               'pid': 39,
               'process': 'IPC Seat Manager',
               'runtime': 464,
               'tty': 0,
               'usecs': 30},
          40: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 1881,
               'one_min_cpu': 0.0,
               'pid': 40,
               'process': 'IPC Check Queue',
               'runtime': 10,
               'tty': 0,
               'usecs': 5},
          41: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 556,
               'one_min_cpu': 0.0,
               'pid': 41,
               'process': 'IPC Seat RX Cont',
               'runtime': 20,
               'tty': 0,
               'usecs': 35},
          42: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 1,
               'one_min_cpu': 0.0,
               'pid': 42,
               'process': 'IPC Seat TX Cont',
               'runtime': 0,
               'tty': 0,
               'usecs': 0},
          43: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 3291,
               'one_min_cpu': 0.0,
               'pid': 43,
               'process': 'IPC Keep Alive M',
               'runtime': 100,
               'tty': 0,
               'usecs': 30},
          44: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 6580,
               'one_min_cpu': 0.0,
               'pid': 44,
               'process': 'IPC Loadometer',
               'runtime': 687,
               'tty': 0,
               'usecs': 104},
          45: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 1,
               'one_min_cpu': 0.0,
               'pid': 45,
               'process': 'IPC Session Deta',
               'runtime': 0,
               'tty': 0,
               'usecs': 0},
          46: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 1,
               'one_min_cpu': 0.0,
               'pid': 46,
               'process': 'SENSOR-MGR event',
               'runtime': 0,
               'tty': 0,
               'usecs': 0},
          47: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 3292,
               'one_min_cpu': 0.0,
               'pid': 47,
               'process': 'Compute SRP rate',
               'runtime': 17,
               'tty': 0,
               'usecs': 5},
          48: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 1,
               'one_min_cpu': 0.0,
               'pid': 48,
               'process': 'CEF MIB API',
               'runtime': 0,
               'tty': 0,
               'usecs': 0},
          49: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 2,
               'one_min_cpu': 0.0,
               'pid': 49,
               'process': 'Serial Backgroun',
               'runtime': 0,
               'tty': 0,
               'usecs': 0},
          50: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 32875,
               'one_min_cpu': 0.0,
               'pid': 50,
               'process': 'GraphIt',
               'runtime': 267,
               'tty': 0,
               'usecs': 8},
          51: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 2,
               'one_min_cpu': 0.0,
               'pid': 51,
               'process': 'Dialer event',
               'runtime': 1,
               'tty': 0,
               'usecs': 500},
          52: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 1,
               'one_min_cpu': 0.0,
               'pid': 52,
               'process': 'IOSXE signals IO',
               'runtime': 0,
               'tty': 0,
               'usecs': 0},
          53: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 2,
               'one_min_cpu': 0.0,
               'pid': 53,
               'process': 'SMART',
               'runtime': 0,
               'tty': 0,
               'usecs': 0},
          54: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 17,
               'one_min_cpu': 0.0,
               'pid': 54,
               'process': 'client_entity_se',
               'runtime': 1,
               'tty': 0,
               'usecs': 58},
          55: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 1,
               'one_min_cpu': 0.0,
               'pid': 55,
               'process': 'RF SCTPthread',
               'runtime': 0,
               'tty': 0,
               'usecs': 0},
          56: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 1,
               'one_min_cpu': 0.0,
               'pid': 56,
               'process': 'CHKPT RG SCTPthr',
               'runtime': 0,
               'tty': 0,
               'usecs': 0},
          57: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 4,
               'one_min_cpu': 0.0,
               'pid': 58,
               'process': 'Critical Bkgnd',
               'runtime': 3,
               'tty': 0,
               'usecs': 750},
          58: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 51594,
               'one_min_cpu': 0.0,
               'pid': 59,
               'process': 'Net Background',
               'runtime': 1949,
               'tty': 0,
               'usecs': 37},
          59: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 3,
               'one_min_cpu': 0.0,
               'pid': 60,
               'process': 'IDB Work',
               'runtime': 0,
               'tty': 0,
               'usecs': 0},
          60: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 728,
               'one_min_cpu': 0.0,
               'pid': 61,
               'process': 'Logger',
               'runtime': 11,
               'tty': 0,
               'usecs': 15},
          61: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 32836,
               'one_min_cpu': 0.0,
               'pid': 62,
               'process': 'TTY Background',
               'runtime': 385,
               'tty': 0,
               'usecs': 11},
          62: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 1,
               'one_min_cpu': 0.0,
               'pid': 63,
               'process': 'BACK CHECK',
               'runtime': 0,
               'tty': 0,
               'usecs': 0},
          63: {'five_min_cpu': 0.05,
               'five_sec_cpu': 0.07,
               'invoked': 282755,
               'one_min_cpu': 0.04,
               'pid': 64,
               'process': 'IOSD ipc task',
               'runtime': 17768,
               'tty': 0,
               'usecs': 62},
          64: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 79222,
               'one_min_cpu': 0.0,
               'pid': 65,
               'process': 'IOSD chasfs task',
               'runtime': 1119,
               'tty': 0,
               'usecs': 14},
          65: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 4712,
               'one_min_cpu': 0.0,
               'pid': 66,
               'process': 'REDUNDANCY FSM',
               'runtime': 41,
               'tty': 0,
               'usecs': 8},
          66: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 9,
               'one_min_cpu': 0.0,
               'pid': 67,
               'process': 'SBC IPC Hold Que',
               'runtime': 0,
               'tty': 0,
               'usecs': 0},
          67: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 1,
               'one_min_cpu': 0.0,
               'pid': 68,
               'process': 'Punt FP Stats Du',
               'runtime': 0,
               'tty': 0,
               'usecs': 0},
          68: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 16390,
               'one_min_cpu': 0.0,
               'pid': 69,
               'process': 'PuntInject Keepa',
               'runtime': 912,
               'tty': 0,
               'usecs': 55},
          69: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 260,
               'one_min_cpu': 0.0,
               'pid': 70,
               'process': 'IF-MGR control p',
               'runtime': 340,
               'tty': 0,
               'usecs': 1307},
          70: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 34,
               'one_min_cpu': 0.0,
               'pid': 71,
               'process': 'IF-MGR event pro',
               'runtime': 2,
               'tty': 0,
               'usecs': 58},
          71: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 290,
               'one_min_cpu': 0.0,
               'pid': 72,
               'process': 'cpf_msg_holdq_pr',
               'runtime': 48,
               'tty': 0,
               'usecs': 165},
          72: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 6715,
               'one_min_cpu': 0.0,
               'pid': 73,
               'process': 'cpf_msg_rcvq_pro',
               'runtime': 176,
               'tty': 0,
               'usecs': 26},
          73: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 13566,
               'one_min_cpu': 0.0,
               'pid': 74,
               'process': 'cpf_process_tpQ',
               'runtime': 17155,
               'tty': 0,
               'usecs': 1264},
          74: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 2,
               'one_min_cpu': 0.0,
               'pid': 75,
               'process': 'Network-rf Notif',
               'runtime': 1,
               'tty': 0,
               'usecs': 500},
          75: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 32866,
               'one_min_cpu': 0.0,
               'pid': 76,
               'process': 'Environmental Mo',
               'runtime': 1034,
               'tty': 0,
               'usecs': 31},
          76: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 32866,
               'one_min_cpu': 0.0,
               'pid': 77,
               'process': 'RP HA Periodic',
               'runtime': 206,
               'tty': 0,
               'usecs': 6},
          77: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 1,
               'one_min_cpu': 0.0,
               'pid': 78,
               'process': 'CONSOLE helper p',
               'runtime': 0,
               'tty': 0,
               'usecs': 0},
          78: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 355,
               'one_min_cpu': 0.0,
               'pid': 79,
               'process': 'CEF RRP RF waite',
               'runtime': 5,
               'tty': 0,
               'usecs': 14},
          79: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 3,
               'one_min_cpu': 0.0,
               'pid': 80,
               'process': 'CWAN APS HA Proc',
               'runtime': 0,
               'tty': 0,
               'usecs': 0},
          80: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 42450,
               'one_min_cpu': 0.0,
               'pid': 81,
               'process': 'REDUNDANCY peer',
               'runtime': 1041,
               'tty': 0,
               'usecs': 24},
          81: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 328370,
               'one_min_cpu': 0.0,
               'pid': 82,
               'process': '100ms check',
               'runtime': 2062,
               'tty': 0,
               'usecs': 6},
          82: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 554,
               'one_min_cpu': 0.0,
               'pid': 83,
               'process': 'RF CWAN HA Proce',
               'runtime': 11,
               'tty': 0,
               'usecs': 19},
          83: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 9,
               'one_min_cpu': 0.0,
               'pid': 84,
               'process': 'CWAN IF EVENT HA',
               'runtime': 1,
               'tty': 0,
               'usecs': 111},
          84: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 5,
               'one_min_cpu': 0.0,
               'pid': 85,
               'process': 'ANCP HA',
               'runtime': 1,
               'tty': 0,
               'usecs': 200},
          85: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 18,
               'one_min_cpu': 0.0,
               'pid': 86,
               'process': 'ANCP HA IPC flow',
               'runtime': 0,
               'tty': 0,
               'usecs': 0},
          86: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 1,
               'one_min_cpu': 0.0,
               'pid': 87,
               'process': 'QoS HA ID RETAIN',
               'runtime': 0,
               'tty': 0,
               'usecs': 0},
          87: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 1,
               'one_min_cpu': 0.0,
               'pid': 88,
               'process': 'CHKPT Test clien',
               'runtime': 0,
               'tty': 0,
               'usecs': 0},
          88: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 1,
               'one_min_cpu': 0.0,
               'pid': 89,
               'process': 'CHKPT Test clien',
               'runtime': 0,
               'tty': 0,
               'usecs': 0},
          89: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 1,
               'one_min_cpu': 0.0,
               'pid': 90,
               'process': 'CHKPT Test clien',
               'runtime': 0,
               'tty': 0,
               'usecs': 0},
          90: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 1,
               'one_min_cpu': 0.0,
               'pid': 91,
               'process': 'CHKPT Test clien',
               'runtime': 0,
               'tty': 0,
               'usecs': 0},
          91: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 1,
               'one_min_cpu': 0.0,
               'pid': 92,
               'process': 'CHKPT Test clien',
               'runtime': 0,
               'tty': 0,
               'usecs': 0},
          92: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 1,
               'one_min_cpu': 0.0,
               'pid': 93,
               'process': 'CHKPT Test clien',
               'runtime': 0,
               'tty': 0,
               'usecs': 0},
          93: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 1,
               'one_min_cpu': 0.0,
               'pid': 94,
               'process': 'CHKPT Test clien',
               'runtime': 0,
               'tty': 0,
               'usecs': 0},
          94: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 1,
               'one_min_cpu': 0.0,
               'pid': 95,
               'process': 'CHKPT Test clien',
               'runtime': 0,
               'tty': 0,
               'usecs': 0},
          95: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 1,
               'one_min_cpu': 0.0,
               'pid': 96,
               'process': 'CHKPT Test clien',
               'runtime': 0,
               'tty': 0,
               'usecs': 0},
          96: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 1,
               'one_min_cpu': 0.0,
               'pid': 97,
               'process': 'CHKPT Test clien',
               'runtime': 0,
               'tty': 0,
               'usecs': 0},
          97: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 1,
               'one_min_cpu': 0.0,
               'pid': 98,
               'process': 'CHKPT Test clien',
               'runtime': 0,
               'tty': 0,
               'usecs': 0},
          98: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 7,
               'one_min_cpu': 0.0,
               'pid': 99,
               'process': 'DHCPC HA',
               'runtime': 1,
               'tty': 0,
               'usecs': 142},
          99: {'five_min_cpu': 0.0,
               'five_sec_cpu': 0.0,
               'invoked': 7,
               'one_min_cpu': 0.0,
               'pid': 100,
               'process': 'DHCPD HA',
               'runtime': 1,
               'tty': 0,
               'usecs': 142},
          100: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 8,
                'one_min_cpu': 0.0,
                'pid': 101,
                'process': 'DHCPv6 Relay HA',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          101: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 8,
                'one_min_cpu': 0.0,
                'pid': 102,
                'process': 'DHCPv6 Server HA',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          102: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 5,
                'one_min_cpu': 0.0,
                'pid': 103,
                'process': 'Metadata HA',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          103: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 18,
                'one_min_cpu': 0.0,
                'pid': 104,
                'process': 'FMD HA IPC flow',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          104: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 3,
                'one_min_cpu': 0.0,
                'pid': 105,
                'process': 'SISF HA Process',
                'runtime': 1,
                'tty': 0,
                'usecs': 333},
          105: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 174,
                'one_min_cpu': 0.0,
                'pid': 106,
                'process': 'ARP HA',
                'runtime': 15,
                'tty': 0,
                'usecs': 86},
          106: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 107,
                'process': 'XDR RRP RF waite',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          107: {'five_min_cpu': 0.02,
                'five_sec_cpu': 0.0,
                'invoked': 407444,
                'one_min_cpu': 0.03,
                'pid': 108,
                'process': 'IOSXE-RP Punt Se',
                'runtime': 13441,
                'tty': 0,
                'usecs': 32},
          108: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 109,
                'process': 'IOSXE-RP Punt IP',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          109: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 4,
                'one_min_cpu': 0.0,
                'pid': 110,
                'process': 'IOSXE-RP SPA TSM',
                'runtime': 1,
                'tty': 0,
                'usecs': 250},
          110: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 8256,
                'one_min_cpu': 0.0,
                'pid': 111,
                'process': 'RF Master Main T',
                'runtime': 78,
                'tty': 0,
                'usecs': 9},
          111: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 8220,
                'one_min_cpu': 0.0,
                'pid': 112,
                'process': 'RF Master Status',
                'runtime': 488,
                'tty': 0,
                'usecs': 59},
          112: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 7528,
                'one_min_cpu': 0.0,
                'pid': 113,
                'process': 'Net Input',
                'runtime': 92,
                'tty': 0,
                'usecs': 12},
          113: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 5,
                'one_min_cpu': 0.0,
                'pid': 114,
                'process': 'OTV Event Dispat',
                'runtime': 1,
                'tty': 0,
                'usecs': 200},
          114: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 3290,
                'one_min_cpu': 0.0,
                'pid': 115,
                'process': 'Compute load avg',
                'runtime': 161,
                'tty': 0,
                'usecs': 48},
          115: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1097,
                'one_min_cpu': 0.0,
                'pid': 116,
                'process': 'Per-minute Jobs',
                'runtime': 3720,
                'tty': 0,
                'usecs': 3391},
          116: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.07,
                'invoked': 32944,
                'one_min_cpu': 0.01,
                'pid': 117,
                'process': 'Per-Second Jobs',
                'runtime': 4496,
                'tty': 0,
                'usecs': 136},
          117: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 32847,
                'one_min_cpu': 0.0,
                'pid': 118,
                'process': 'mLDP Process',
                'runtime': 247,
                'tty': 0,
                'usecs': 7},
          118: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 46,
                'one_min_cpu': 0.0,
                'pid': 119,
                'process': 'Transport Port A',
                'runtime': 1,
                'tty': 0,
                'usecs': 21},
          119: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 310,
                'one_min_cpu': 0.0,
                'pid': 120,
                'process': 'EEM ED ND',
                'runtime': 3,
                'tty': 0,
                'usecs': 9},
          120: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 121,
                'process': 'IOSXE-RP FastPat',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          121: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 122,
                'process': 'Src Fltr backgro',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          122: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 123,
                'process': 'DSX3MIB ll handl',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          123: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 32087,
                'one_min_cpu': 0.0,
                'pid': 124,
                'process': 'fanrp_l2fib',
                'runtime': 223,
                'tty': 0,
                'usecs': 6},
          124: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 125,
                'process': 'POS APS Event Pr',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          125: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 3,
                'one_min_cpu': 0.0,
                'pid': 126,
                'process': 'netclk_process',
                'runtime': 5,
                'tty': 0,
                'usecs': 1666},
          126: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 3,
                'one_min_cpu': 0.0,
                'pid': 127,
                'process': 'netclk_ha_proces',
                'runtime': 1,
                'tty': 0,
                'usecs': 333},
          127: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 7,
                'one_min_cpu': 0.0,
                'pid': 128,
                'process': 'FPD Management P',
                'runtime': 4,
                'tty': 0,
                'usecs': 571},
          128: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 129,
                'process': 'FPD Action Proce',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          129: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 130,
                'process': 'BFD HW EVENT',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          130: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 131,
                'process': 'BFD IPV6 ADDR CH',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          131: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 132,
                'process': 'FEC_Link_event_h',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          132: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 255002,
                'one_min_cpu': 0.0,
                'pid': 133,
                'process': 'MCP RP autovc pr',
                'runtime': 1395,
                'tty': 0,
                'usecs': 5},
          133: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 134,
                'process': 'VMI Background',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          134: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 6563,
                'one_min_cpu': 0.0,
                'pid': 135,
                'process': 'MGMTE stats Proc',
                'runtime': 259,
                'tty': 0,
                'usecs': 39},
          135: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 44788,
                'one_min_cpu': 0.0,
                'pid': 136,
                'process': 'Ether-SPA backgr',
                'runtime': 386,
                'tty': 0,
                'usecs': 8},
          136: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 32863,
                'one_min_cpu': 0.0,
                'pid': 137,
                'process': 'CWAN CHOCX PROCE',
                'runtime': 207,
                'tty': 0,
                'usecs': 6},
          137: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 138,
                'process': 'CE3 Mailbox',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          138: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 139,
                'process': 'CT3 Mailbox',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          139: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 140,
                'process': 'HAL Mailbox',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          140: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 141,
                'process': 'MIP Mailbox',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          141: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1198,
                'one_min_cpu': 0.0,
                'pid': 142,
                'process': 'CWAN OIR Handler',
                'runtime': 1001,
                'tty': 0,
                'usecs': 835},
          142: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 143,
                'process': 'TP CUTOVER EVENT',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          143: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 144,
                'process': 'ASR1K ESMC Proce',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          144: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 145,
                'process': 'ASR1000-RP SPA A',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          145: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 146,
                'process': 'RTTYS Process',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          146: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 130,
                'one_min_cpu': 0.0,
                'pid': 147,
                'process': 'AAA Server',
                'runtime': 1,
                'tty': 0,
                'usecs': 7},
          147: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 148,
                'process': 'AAA ACCT Proc',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          148: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 149,
                'process': 'ACCT Periodic Pr',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          149: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 32863,
                'one_min_cpu': 0.0,
                'pid': 150,
                'process': 'cdp init process',
                'runtime': 140,
                'tty': 0,
                'usecs': 4},
          150: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 565,
                'one_min_cpu': 0.0,
                'pid': 151,
                'process': 'Call Home Timer',
                'runtime': 6,
                'tty': 0,
                'usecs': 10},
          151: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 152,
                'process': 'CEF switching ba',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          152: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 153,
                'process': 'ADJ NSF process',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          153: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 154,
                'process': 'AAA Dictionary R',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          154: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 32863,
                'one_min_cpu': 0.0,
                'pid': 155,
                'process': 'FHRP Main thread',
                'runtime': 504,
                'tty': 0,
                'usecs': 15},
          155: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 156,
                'process': 'TRACK Main threa',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          156: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 157,
                'process': 'TRACK Client thr',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          157: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 158,
                'process': 'VRRP Main thread',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          158: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.07,
                'invoked': 510138,
                'one_min_cpu': 0.0,
                'pid': 159,
                'process': 'VRRS Main thread',
                'runtime': 4663,
                'tty': 0,
                'usecs': 9},
          159: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 160,
                'process': 'ATM OAM Input',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          160: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 161,
                'process': 'ATM OAM TIMER',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          161: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 162,
                'process': 'HQF TARGET DYNAM',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          162: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 247,
                'one_min_cpu': 0.0,
                'pid': 163,
                'process': 'IP ARP Adjacency',
                'runtime': 45,
                'tty': 0,
                'usecs': 182},
          163: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.07,
                'invoked': 1006869,
                'one_min_cpu': 0.01,
                'pid': 164,
                'process': 'IP ARP Retry Age',
                'runtime': 5672,
                'tty': 0,
                'usecs': 5},
          164: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 549,
                'one_min_cpu': 0.0,
                'pid': 165,
                'process': 'IP Input',
                'runtime': 2,
                'tty': 0,
                'usecs': 3},
          165: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 166,
                'process': 'ICMP event handl',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          166: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 32863,
                'one_min_cpu': 0.0,
                'pid': 167,
                'process': 'mDNS',
                'runtime': 283,
                'tty': 0,
                'usecs': 8},
          167: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 3,
                'one_min_cpu': 0.0,
                'pid': 168,
                'process': 'PIM register asy',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          168: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 169,
                'process': 'IPv6 ping proces',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          169: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 32063,
                'one_min_cpu': 0.0,
                'pid': 170,
                'process': 'BGP Scheduler',
                'runtime': 589,
                'tty': 0,
                'usecs': 18},
          170: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 116,
                'one_min_cpu': 0.0,
                'pid': 171,
                'process': 'MOP Protocols',
                'runtime': 11,
                'tty': 0,
                'usecs': 94},
          171: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 172,
                'process': 'PPP SIP',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          172: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 173,
                'process': 'PPP Bind',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          173: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 174,
                'process': 'PPP IP Route',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          174: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 175,
                'process': 'LSP Verification',
                'runtime': 1,
                'tty': 0,
                'usecs': 1000},
          175: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 176,
                'process': 'RIB LM VALIDATE',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          176: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 346,
                'one_min_cpu': 0.0,
                'pid': 177,
                'process': 'SSM connection m',
                'runtime': 170,
                'tty': 0,
                'usecs': 491},
          177: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 549,
                'one_min_cpu': 0.0,
                'pid': 178,
                'process': 'SSS Manager',
                'runtime': 2,
                'tty': 0,
                'usecs': 3},
          178: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 179,
                'process': 'SSS Policy Manag',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          179: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 180,
                'process': 'SSS Feature Mana',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          180: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 128492,
                'one_min_cpu': 0.0,
                'pid': 181,
                'process': 'SSS Feature Time',
                'runtime': 932,
                'tty': 0,
                'usecs': 7},
          181: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 182,
                'process': 'Spanning Tree',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          182: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 183,
                'process': 'VRRS',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          183: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 184,
                'process': 'Ethernet LMI',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          184: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 185,
                'process': 'Ethernet OAM Pro',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          185: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 186,
                'process': 'Ethernet CFM',
                'runtime': 1,
                'tty': 0,
                'usecs': 500},
          186: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 5561,
                'one_min_cpu': 0.0,
                'pid': 187,
                'process': 'mcp callhome per',
                'runtime': 357,
                'tty': 0,
                'usecs': 64},
          187: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 188,
                'process': 'PPCP RP Stats Ba',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          188: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 110,
                'one_min_cpu': 0.0,
                'pid': 189,
                'process': 'Appnav auto disc',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          189: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 190,
                'process': 'L2FIB Timer Disp',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          190: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 71,
                'one_min_cpu': 0.0,
                'pid': 191,
                'process': 'MLRIB L2 Msg Thr',
                'runtime': 10,
                'tty': 0,
                'usecs': 140},
          191: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 192,
                'process': 'Spanning Tree St',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          192: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 193,
                'process': 'IGMP Route Msg H',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          193: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 36,
                'one_min_cpu': 0.0,
                'pid': 194,
                'process': 'IGMP Route Rx Pr',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          194: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 3,
                'one_min_cpu': 0.0,
                'pid': 195,
                'process': 'RABAPOL HA',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          195: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 18,
                'one_min_cpu': 0.0,
                'pid': 196,
                'process': 'RABAPOL HA IPC f',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          196: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 9,
                'one_min_cpu': 0.0,
                'pid': 197,
                'process': 'TEMPLATE HA',
                'runtime': 1,
                'tty': 0,
                'usecs': 111},
          197: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 4,
                'one_min_cpu': 0.0,
                'pid': 198,
                'process': 'DVLAN HA',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          198: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 90,
                'one_min_cpu': 0.0,
                'pid': 199,
                'process': 'CCM',
                'runtime': 13,
                'tty': 0,
                'usecs': 144},
          199: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 18,
                'one_min_cpu': 0.0,
                'pid': 200,
                'process': 'CCM IPC flow con',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          200: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 201,
                'process': 'RG Faults Timer',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          201: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 202,
                'process': 'RG VP',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          202: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 203,
                'process': 'RG AR',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          203: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 204,
                'process': 'RG Protocol Time',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          204: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 205,
                'process': 'RG Transport Tim',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          205: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 206,
                'process': 'HDLC HA',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          206: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 207,
                'process': 'SBC initializer',
                'runtime': 1,
                'tty': 0,
                'usecs': 1000},
          207: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 3,
                'one_min_cpu': 0.0,
                'pid': 208,
                'process': 'SVM HA',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          208: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 32876,
                'one_min_cpu': 0.0,
                'pid': 209,
                'process': 'UDLD',
                'runtime': 423,
                'tty': 0,
                'usecs': 12},
          209: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 210,
                'process': 'AC Switch',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          210: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 211,
                'process': 'IEDGE ACCT TIMER',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          211: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 212,
                'process': 'ISG CMD HANDLER',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          212: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 213,
                'process': 'IMA PROC',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          213: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 8033,
                'one_min_cpu': 0.0,
                'pid': 214,
                'process': 'IP Lite session',
                'runtime': 35,
                'tty': 0,
                'usecs': 4},
          214: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 215,
                'process': 'IP PORTBUNDLE',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          215: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 216,
                'process': 'SSS Mobility mes',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          216: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 8026,
                'one_min_cpu': 0.0,
                'pid': 217,
                'process': 'IP Static Sessio',
                'runtime': 35,
                'tty': 0,
                'usecs': 4},
          217: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 218,
                'process': 'DVLAN Config Pro',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          218: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 219,
                'process': 'IPAM/ODAP Events',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          219: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1006869,
                'one_min_cpu': 0.0,
                'pid': 220,
                'process': 'IPAM Manager',
                'runtime': 6054,
                'tty': 0,
                'usecs': 6},
          220: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 221,
                'process': 'IPAM Events',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          221: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 222,
                'process': 'OCE punted Pkts',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          222: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 223,
                'process': 'O-UNI Client Msg',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          223: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 224,
                'process': 'LSP Tunnel FRR',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          224: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 5,
                'one_min_cpu': 0.0,
                'pid': 225,
                'process': 'MPLS Auto-Tunnel',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          225: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 226,
                'process': 'st_pw_oam',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          226: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 227,
                'process': 'AAA EPD HANDLER',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          227: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 228,
                'process': 'PM EPD API',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          228: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 229,
                'process': 'DM Proc',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          229: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 230,
                'process': 'RADIUS Proxy',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          230: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 231,
                'process': 'SSS PM SHIM QOS',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          231: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 232,
                'process': 'LONG TO SHORT NA',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          232: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 233,
                'process': 'Timer handler fo',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          233: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 234,
                'process': 'Prepaid response',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          234: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 235,
                'process': 'Timed Policy act',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          235: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 236,
                'process': 'AAA response han',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          236: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 237,
                'process': 'AAA System Acct',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          237: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 238,
                'process': 'VPWS Thread',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          238: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 239,
                'process': 'IP Traceroute',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          239: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 240,
                'process': 'Tunnel',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          240: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 241,
                'process': 'ATIP_UDP_TSK',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          241: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 242,
                'process': 'XDR background p',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          242: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 18357,
                'one_min_cpu': 0.0,
                'pid': 243,
                'process': 'XDR mcast',
                'runtime': 19944,
                'tty': 0,
                'usecs': 1086},
          243: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 3,
                'one_min_cpu': 0.0,
                'pid': 244,
                'process': 'XDR RP Ping Back',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          244: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 211,
                'one_min_cpu': 0.0,
                'pid': 245,
                'process': 'XDR receive',
                'runtime': 46,
                'tty': 0,
                'usecs': 218},
          245: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 4,
                'one_min_cpu': 0.0,
                'pid': 246,
                'process': 'IPC LC Message H',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          246: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 247,
                'process': 'XDR RP Test Back',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          247: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 549,
                'one_min_cpu': 0.0,
                'pid': 248,
                'process': 'FRR Background P',
                'runtime': 2,
                'tty': 0,
                'usecs': 3},
          248: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 3521,
                'one_min_cpu': 0.0,
                'pid': 249,
                'process': 'CEF background p',
                'runtime': 26621,
                'tty': 0,
                'usecs': 7560},
          249: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 250,
                'process': 'fib_fib_bfd_sb e',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          250: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 251,
                'process': 'IP IRDP',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          251: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 7,
                'one_min_cpu': 0.0,
                'pid': 252,
                'process': 'SNMP Timers',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          252: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 5,
                'one_min_cpu': 0.0,
                'pid': 253,
                'process': 'LSD HA Proc',
                'runtime': 1,
                'tty': 0,
                'usecs': 200},
          253: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 148,
                'one_min_cpu': 0.0,
                'pid': 254,
                'process': 'CEF RP Backgroun',
                'runtime': 14,
                'tty': 0,
                'usecs': 94},
          254: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 255,
                'process': 'Routing Topology',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          255: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 7171,
                'one_min_cpu': 0.0,
                'pid': 256,
                'process': 'IP RIB Update',
                'runtime': 337307,
                'tty': 0,
                'usecs': 47037},
          256: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 915,
                'one_min_cpu': 0.0,
                'pid': 257,
                'process': 'IP Background',
                'runtime': 1371,
                'tty': 0,
                'usecs': 1498},
          257: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 837,
                'one_min_cpu': 0.0,
                'pid': 258,
                'process': 'IP Connected Rou',
                'runtime': 229,
                'tty': 0,
                'usecs': 273},
          258: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 259,
                'process': 'PPP Compress Inp',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          259: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 260,
                'process': 'PPP Compress Res',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          260: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 261,
                'process': 'Tunnel FIB',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          261: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 68,
                'one_min_cpu': 0.0,
                'pid': 263,
                'process': 'ADJ background',
                'runtime': 9,
                'tty': 0,
                'usecs': 132},
          262: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 523,
                'one_min_cpu': 0.0,
                'pid': 264,
                'process': 'Collection proce',
                'runtime': 12855,
                'tty': 0,
                'usecs': 24579},
          263: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 3,
                'one_min_cpu': 0.0,
                'pid': 265,
                'process': 'ADJ resolve proc',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          264: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 62,
                'one_min_cpu': 0.0,
                'pid': 266,
                'process': 'Socket Timers',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          265: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 75126,
                'one_min_cpu': 0.0,
                'pid': 267,
                'process': 'TCP Timer',
                'runtime': 3096,
                'tty': 0,
                'usecs': 41},
          266: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 49,
                'one_min_cpu': 0.0,
                'pid': 268,
                'process': 'TCP Protocols',
                'runtime': 5,
                'tty': 0,
                'usecs': 102},
          267: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 269,
                'process': 'COPS',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          268: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1097,
                'one_min_cpu': 0.0,
                'pid': 270,
                'process': 'NGCP SCHEDULER P',
                'runtime': 12,
                'tty': 0,
                'usecs': 10},
          269: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 32840,
                'one_min_cpu': 0.0,
                'pid': 271,
                'process': 'STILE PERIODIC T',
                'runtime': 178,
                'tty': 0,
                'usecs': 5},
          270: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 549,
                'one_min_cpu': 0.0,
                'pid': 272,
                'process': 'UV AUTO CUSTOM P',
                'runtime': 4,
                'tty': 0,
                'usecs': 7},
          271: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 273,
                'process': 'Dialer Forwarder',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          272: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 3,
                'one_min_cpu': 0.0,
                'pid': 274,
                'process': 'Service Routing',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          273: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 196,
                'one_min_cpu': 0.0,
                'pid': 275,
                'process': 'SR CapMan Proces',
                'runtime': 32,
                'tty': 0,
                'usecs': 163},
          274: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 151,
                'one_min_cpu': 0.0,
                'pid': 276,
                'process': 'Flow Exporter Ti',
                'runtime': 2,
                'tty': 0,
                'usecs': 13},
          275: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 277,
                'process': 'Flow Exporter Pa',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          276: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 110,
                'one_min_cpu': 0.0,
                'pid': 278,
                'process': 'HTTP CORE',
                'runtime': 1,
                'tty': 0,
                'usecs': 9},
          277: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 279,
                'process': 'SBC Msg Ack Time',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          278: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 111,
                'one_min_cpu': 0.0,
                'pid': 280,
                'process': 'MFIB Master back',
                'runtime': 1,
                'tty': 0,
                'usecs': 9},
          279: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 51,
                'one_min_cpu': 0.0,
                'pid': 281,
                'process': 'VFI Mgr',
                'runtime': 21,
                'tty': 0,
                'usecs': 411},
          280: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 330,
                'one_min_cpu': 0.0,
                'pid': 282,
                'process': 'MVPN Mgr Process',
                'runtime': 56,
                'tty': 0,
                'usecs': 169},
          281: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 283,
                'process': 'Multicast Offloa',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          282: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 284,
                'process': 'RARP Input',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          283: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 128,
                'one_min_cpu': 0.0,
                'pid': 285,
                'process': 'static',
                'runtime': 12,
                'tty': 0,
                'usecs': 93},
          284: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 286,
                'process': 'App Route Proces',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          285: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 287,
                'process': 'IPv6 RIB Cleanup',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          286: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 3,
                'one_min_cpu': 0.0,
                'pid': 288,
                'process': 'IPv6 RIB Event H',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          287: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 289,
                'process': 'IPv6 Static Hand',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          288: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 290,
                'process': 'DHCPv6 LQ client',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          289: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 12,
                'one_min_cpu': 0.0,
                'pid': 291,
                'process': 'AToM manager',
                'runtime': 68,
                'tty': 0,
                'usecs': 5666},
          290: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 292,
                'process': 'PPP NBF',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          291: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 32559,
                'one_min_cpu': 0.0,
                'pid': 293,
                'process': 'PfR BR Learn',
                'runtime': 209,
                'tty': 0,
                'usecs': 6},
          292: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 294,
                'process': 'PAD InCall',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          293: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 3289,
                'one_min_cpu': 0.0,
                'pid': 297,
                'process': 'QoS stats proces',
                'runtime': 82,
                'tty': 0,
                'usecs': 24},
          294: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 298,
                'process': 'RBSCP Background',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          295: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 299,
                'process': 'SCTP Main Proces',
                'runtime': 2,
                'tty': 0,
                'usecs': 1000},
          296: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 300,
                'process': 'VPDN call manage',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          297: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 15,
                'one_min_cpu': 0.0,
                'pid': 301,
                'process': 'XC RIB MGR',
                'runtime': 95,
                'tty': 0,
                'usecs': 6333},
          298: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 302,
                'process': 'AToM LDP manager',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          299: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 303,
                'process': 'EFP Errd',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          300: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 304,
                'process': 'Ether EFP Proces',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          301: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 305,
                'process': 'Ether Infra RP',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          302: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 18,
                'one_min_cpu': 0.0,
                'pid': 306,
                'process': 'CFM HA IPC messa',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          303: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 307,
                'process': 'Ethernet PM Proc',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          304: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 308,
                'process': 'Ethernet PM Soft',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          305: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 9857,
                'one_min_cpu': 0.0,
                'pid': 309,
                'process': 'Ethernet PM Moni',
                'runtime': 83,
                'tty': 0,
                'usecs': 8},
          306: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 310,
                'process': 'Ethernet Datapla',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          307: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 18,
                'one_min_cpu': 0.0,
                'pid': 311,
                'process': 'ELB HA IPC flow',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          308: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 42,
                'one_min_cpu': 0.0,
                'pid': 312,
                'process': 'IGMPSN L2MCM',
                'runtime': 31,
                'tty': 0,
                'usecs': 738},
          309: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 313,
                'process': 'IGMPSN MRD',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          310: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 314,
                'process': 'IGMPSN',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          311: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 131016,
                'one_min_cpu': 0.0,
                'pid': 315,
                'process': 'TCP HA PROC',
                'runtime': 4917,
                'tty': 0,
                'usecs': 37},
          312: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 5076,
                'one_min_cpu': 0.0,
                'pid': 316,
                'process': 'BGP HA SSO',
                'runtime': 49197,
                'tty': 0,
                'usecs': 9692},
          313: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 5,
                'one_min_cpu': 0.0,
                'pid': 317,
                'process': 'RSVP SYNC',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          314: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 318,
                'process': 'RETRY_REPOPULATE',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          315: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 4,
                'one_min_cpu': 0.0,
                'pid': 319,
                'process': 'XDR FOF process',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          316: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 320,
                'process': 'BD Route Msg Hol',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          317: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 321,
                'process': 'BD Route Rx Proc',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          318: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 3,
                'one_min_cpu': 0.0,
                'pid': 322,
                'process': 'BD MACSEC HA',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          319: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 323,
                'process': 'BD MACSEC HA CHK',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          320: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 128,
                'one_min_cpu': 0.0,
                'pid': 324,
                'process': 'L2FIB Event Disp',
                'runtime': 121,
                'tty': 0,
                'usecs': 945},
          321: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 18,
                'one_min_cpu': 0.0,
                'pid': 325,
                'process': 'STP HA IPC flow',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          322: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 326,
                'process': 'IGMPQR',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          323: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 4,
                'one_min_cpu': 0.0,
                'pid': 327,
                'process': 'AAA HA',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          324: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 328,
                'process': 'AAA HA cleanup',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          325: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 329,
                'process': 'ac_atm_state_eve',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          326: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 330,
                'process': 'ac_atm_mraps_hsp',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          327: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 331,
                'process': 'AC HA Bulk Sync',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          328: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 332,
                'process': 'ATM HA',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          329: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 18,
                'one_min_cpu': 0.0,
                'pid': 333,
                'process': 'ATM HA IPC flow',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          330: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 334,
                'process': 'ATM HA AC',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          331: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 335,
                'process': 'BFD HA',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          332: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 336,
                'process': 'FR HA',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          333: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 10,
                'one_min_cpu': 0.0,
                'pid': 337,
                'process': 'GLBP HA',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          334: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 10,
                'one_min_cpu': 0.0,
                'pid': 338,
                'process': 'HSRP HA',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          335: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 64077,
                'one_min_cpu': 0.0,
                'pid': 339,
                'process': 'Inspect process',
                'runtime': 397,
                'tty': 0,
                'usecs': 6},
          336: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 76816,
                'one_min_cpu': 0.0,
                'pid': 340,
                'process': 'BGP I/O',
                'runtime': 5548,
                'tty': 0,
                'usecs': 72},
          337: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 8026,
                'one_min_cpu': 0.0,
                'pid': 341,
                'process': 'IP SIP Process',
                'runtime': 69,
                'tty': 0,
                'usecs': 8},
          338: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 342,
                'process': 'MRIB RP Proxy',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          339: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 343,
                'process': 'IPv6 ACL RP Proc',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          340: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 18,
                'one_min_cpu': 0.0,
                'pid': 344,
                'process': 'Netsync IPC flow',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          341: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 345,
                'process': 'PPPoE VRRS EVT M',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          342: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 346,
                'process': 'RG If-Mgr Timer',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          343: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 347,
                'process': 'RG Media Timer',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          344: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 13,
                'one_min_cpu': 0.0,
                'pid': 348,
                'process': 'MCPRP RG Timer',
                'runtime': 1,
                'tty': 0,
                'usecs': 76},
          345: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 349,
                'process': 'URL filter proc',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          346: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 5,
                'one_min_cpu': 0.0,
                'pid': 350,
                'process': 'VFI HA Bulk Sync',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          347: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 3,
                'one_min_cpu': 0.0,
                'pid': 351,
                'process': 'XC RIB HA Bulk S',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          348: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 4,
                'one_min_cpu': 0.0,
                'pid': 352,
                'process': 'XC BGP SIG RIB H',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          349: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 353,
                'process': 'VPDN CCM Backgro',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          350: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 10,
                'one_min_cpu': 0.0,
                'pid': 354,
                'process': 'VRRP HA',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          351: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 18,
                'one_min_cpu': 0.0,
                'pid': 355,
                'process': 'VTEMPLATE IPC fl',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          352: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 187,
                'one_min_cpu': 0.0,
                'pid': 356,
                'process': 'CEM PROC',
                'runtime': 1,
                'tty': 0,
                'usecs': 5},
          353: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 357,
                'process': 'CEM HA',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          354: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 358,
                'process': 'CEM HA AC',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          355: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 359,
                'process': 'L2X Switching Ev',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          356: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 360,
                'process': 'Probe Input',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          357: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 361,
                'process': 'IP Inband Sessio',
                'runtime': 1,
                'tty': 0,
                'usecs': 500},
          358: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 362,
                'process': 'DHCP SIP',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          359: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 8223,
                'one_min_cpu': 0.0,
                'pid': 363,
                'process': 'FRR Manager',
                'runtime': 77,
                'tty': 0,
                'usecs': 9},
          360: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 364,
                'process': 'MFI Comm RP Proc',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          361: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 365,
                'process': 'Path set broker',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          362: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 366,
                'process': 'LFD Label Block',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          363: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 5273,
                'one_min_cpu': 0.0,
                'pid': 367,
                'process': 'LDP HA',
                'runtime': 439,
                'tty': 0,
                'usecs': 83},
          364: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 3,
                'one_min_cpu': 0.0,
                'pid': 368,
                'process': 'MPLS VPN HA Clie',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          365: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 7,
                'one_min_cpu': 0.0,
                'pid': 369,
                'process': 'TSPTUN HA',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          366: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 370,
                'process': 'RSVP HA Services',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          367: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 371,
                'process': 'TE NSR OOS DB Pr',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          368: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 17,
                'one_min_cpu': 0.0,
                'pid': 372,
                'process': 'MPLS TP HA',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          369: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 5,
                'one_min_cpu': 0.0,
                'pid': 373,
                'process': 'AToM HA Bulk Syn',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          370: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 17,
                'one_min_cpu': 0.0,
                'pid': 374,
                'process': 'AToM MGR HA IPC',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          371: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 375,
                'process': 'LFDp Input Proc',
                'runtime': 2,
                'tty': 0,
                'usecs': 1000},
          372: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 376,
                'process': 'AAA Cached Serve',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          373: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 6,
                'one_min_cpu': 0.0,
                'pid': 377,
                'process': 'ENABLE AAA',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          374: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 378,
                'process': 'EM Background Pr',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          375: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 3,
                'one_min_cpu': 0.0,
                'pid': 379,
                'process': 'LDAP process',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          376: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 380,
                'process': 'Opaque Database',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          377: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 381,
                'process': 'Key chain liveke',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          378: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 382,
                'process': 'LINE AAA',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          379: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 17,
                'one_min_cpu': 0.0,
                'pid': 383,
                'process': 'LOCAL AAA',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          380: {'five_min_cpu': 0.64,
                'five_sec_cpu': 0.0,
                'invoked': 6202,
                'one_min_cpu': 0.44,
                'pid': 384,
                'process': 'BGP Scanner',
                'runtime': 278040,
                'tty': 0,
                'usecs': 44830},
          381: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 472,
                'one_min_cpu': 0.0,
                'pid': 385,
                'process': 'TPLUS',
                'runtime': 20,
                'tty': 0,
                'usecs': 42},
          382: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 319,
                'one_min_cpu': 0.0,
                'pid': 386,
                'process': 'DynCmd Package P',
                'runtime': 6,
                'tty': 0,
                'usecs': 18},
          383: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 510125,
                'one_min_cpu': 0.01,
                'pid': 387,
                'process': 'MMA DB TIMER',
                'runtime': 4924,
                'tty': 0,
                'usecs': 9},
          384: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 388,
                'process': 'FLEX DSPRM MAIN',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          385: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 389,
                'process': 'VSP_MGR',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          386: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 390,
                'process': 'STUN_APP',
                'runtime': 1,
                'tty': 0,
                'usecs': 500},
          387: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 391,
                'process': 'STUN_TEST',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          388: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 392,
                'process': 'Manet Infra Back',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          389: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 393,
                'process': 'IDMGR CORE',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          390: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 18101,
                'one_min_cpu': 0.0,
                'pid': 394,
                'process': 'MPLS Auto Mesh P',
                'runtime': 188,
                'tty': 0,
                'usecs': 10},
          391: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 32875,
                'one_min_cpu': 0.0,
                'pid': 395,
                'process': 'RSCMSM VOLUME MO',
                'runtime': 678,
                'tty': 0,
                'usecs': 20},
          392: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 396,
                'process': 'CCSIP_EVENT_TRAC',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          393: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 397,
                'process': 'Sip MPA',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          394: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 398,
                'process': 'QOS_MODULE_MAIN',
                'runtime': 1,
                'tty': 0,
                'usecs': 1000},
          395: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 399,
                'process': 'IP TRUST Registe',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          396: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 400,
                'process': 'VoIP AAA',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          397: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 18,
                'one_min_cpu': 0.0,
                'pid': 401,
                'process': 'COND_DEBUG HA IP',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          398: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 23,
                'one_min_cpu': 0.0,
                'pid': 402,
                'process': 'PIM HA',
                'runtime': 2,
                'tty': 0,
                'usecs': 86},
          399: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 403,
                'process': 'MMON PROCESS',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          400: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 404,
                'process': 'QOS PERUSER',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          401: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 405,
                'process': 'RPMS_PROC_MAIN',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          402: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 406,
                'process': 'http client proc',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          403: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 65763,
                'one_min_cpu': 0.0,
                'pid': 407,
                'process': 'OSPF-65109 Router',
                'runtime': 914,
                'tty': 0,
                'usecs': 13},
          404: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 408,
                'process': 'SEGMENT ROUTING',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          405: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 44,
                'one_min_cpu': 0.0,
                'pid': 409,
                'process': 'AAA SEND STOP EV',
                'runtime': 1,
                'tty': 0,
                'usecs': 22},
          406: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 410,
                'process': 'Test AAA Client',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          407: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 411,
                'process': 'dcm_cli_engine',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          408: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 3,
                'one_min_cpu': 0.0,
                'pid': 412,
                'process': 'dcm_cli_provider',
                'runtime': 1,
                'tty': 0,
                'usecs': 333},
          409: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 5,
                'one_min_cpu': 0.0,
                'pid': 413,
                'process': 'DCM Core Thread',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          410: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 580,
                'one_min_cpu': 0.0,
                'pid': 414,
                'process': 'EEM ED Syslog',
                'runtime': 14,
                'tty': 0,
                'usecs': 24},
          411: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 4,
                'one_min_cpu': 0.0,
                'pid': 415,
                'process': 'EEM ED Generic',
                'runtime': 1,
                'tty': 0,
                'usecs': 250},
          412: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 4,
                'one_min_cpu': 0.0,
                'pid': 416,
                'process': 'EEM ED Track',
                'runtime': 1,
                'tty': 0,
                'usecs': 250},
          413: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 4,
                'one_min_cpu': 0.0,
                'pid': 417,
                'process': 'EEM ED Routing',
                'runtime': 1,
                'tty': 0,
                'usecs': 250},
          414: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 4,
                'one_min_cpu': 0.0,
                'pid': 418,
                'process': 'EEM ED Resource',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          415: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 419,
                'process': 'Syslog Traps',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          416: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 420,
                'process': 'Policy HA Timer',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          417: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 421,
                'process': 'BGP Consistency',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          418: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 422,
                'process': 'ICRM',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          419: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 423,
                'process': 'Online Diag EEM',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          420: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 10469,
                'one_min_cpu': 0.0,
                'pid': 424,
                'process': 'SPA ENTITY Proce',
                'runtime': 1362,
                'tty': 0,
                'usecs': 130},
          421: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 425,
                'process': 'SONET Traps',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          422: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 426,
                'process': 'ISG MIB jobs Man',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          423: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 427,
                'process': 'SBC RF config sy',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          424: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 6,
                'one_min_cpu': 0.0,
                'pid': 428,
                'process': 'DCM snmp dp Thre',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          425: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 3,
                'one_min_cpu': 0.0,
                'pid': 429,
                'process': 'snmp dcm ma shim',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          426: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 3291,
                'one_min_cpu': 0.0,
                'pid': 430,
                'process': 'Bulkstat-Client',
                'runtime': 50,
                'tty': 0,
                'usecs': 15},
          427: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 3,
                'one_min_cpu': 0.0,
                'pid': 431,
                'process': 'dcm_expression_p',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          428: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 510,
                'one_min_cpu': 0.0,
                'pid': 432,
                'process': 'EEM Server',
                'runtime': 12,
                'tty': 0,
                'usecs': 23},
          429: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 33,
                'one_min_cpu': 0.0,
                'pid': 433,
                'process': 'Call Home proces',
                'runtime': 3,
                'tty': 0,
                'usecs': 90},
          430: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 434,
                'process': 'Call Home DS',
                'runtime': 1,
                'tty': 0,
                'usecs': 1000},
          431: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 435,
                'process': 'Call Home DSfile',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          432: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 3,
                'one_min_cpu': 0.0,
                'pid': 436,
                'process': 'EEM Policy Direc',
                'runtime': 1,
                'tty': 0,
                'usecs': 333},
          433: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 6580,
                'one_min_cpu': 0.0,
                'pid': 437,
                'process': 'LSD Main Proc',
                'runtime': 70,
                'tty': 0,
                'usecs': 10},
          434: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 4,
                'one_min_cpu': 0.0,
                'pid': 438,
                'process': 'EEM ED CLI',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          435: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 4,
                'one_min_cpu': 0.0,
                'pid': 439,
                'process': 'EEM ED Counter',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          436: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 4,
                'one_min_cpu': 0.0,
                'pid': 440,
                'process': 'EEM ED Interface',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          437: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 4,
                'one_min_cpu': 0.0,
                'pid': 441,
                'process': 'EEM ED IOSWD',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          438: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 4,
                'one_min_cpu': 0.0,
                'pid': 442,
                'process': 'EEM ED None',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          439: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 4,
                'one_min_cpu': 0.0,
                'pid': 443,
                'process': 'EEM ED OIR',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          440: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 16,
                'one_min_cpu': 0.0,
                'pid': 444,
                'process': 'EEM ED RF',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          441: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 32933,
                'one_min_cpu': 0.0,
                'pid': 445,
                'process': 'EEM ED SNMP',
                'runtime': 1455,
                'tty': 0,
                'usecs': 44},
          442: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 4,
                'one_min_cpu': 0.0,
                'pid': 446,
                'process': 'EEM ED SNMP Obje',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          443: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 4,
                'one_min_cpu': 0.0,
                'pid': 447,
                'process': 'EEM ED SNMP Noti',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          444: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 555,
                'one_min_cpu': 0.0,
                'pid': 448,
                'process': 'EEM ED Timer',
                'runtime': 11,
                'tty': 0,
                'usecs': 19},
          445: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 4,
                'one_min_cpu': 0.0,
                'pid': 449,
                'process': 'EEM ED Ipsla',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          446: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 4,
                'one_min_cpu': 0.0,
                'pid': 450,
                'process': 'EEM ED Test',
                'runtime': 1,
                'tty': 0,
                'usecs': 250},
          447: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 4,
                'one_min_cpu': 0.0,
                'pid': 451,
                'process': 'EEM ED Config',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          448: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 4,
                'one_min_cpu': 0.0,
                'pid': 452,
                'process': 'EEM ED Env',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          449: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 4,
                'one_min_cpu': 0.0,
                'pid': 453,
                'process': 'EEM ED DS',
                'runtime': 1,
                'tty': 0,
                'usecs': 250},
          450: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 4,
                'one_min_cpu': 0.0,
                'pid': 454,
                'process': 'EEM ED CRASH',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          451: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 4,
                'one_min_cpu': 0.0,
                'pid': 455,
                'process': 'EM ED GOLD',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          452: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 417,
                'one_min_cpu': 0.0,
                'pid': 456,
                'process': 'Syslog',
                'runtime': 73,
                'tty': 0,
                'usecs': 175},
          453: {'five_min_cpu': 0.05,
                'five_sec_cpu': 0.07,
                'invoked': 3284,
                'one_min_cpu': 0.06,
                'pid': 457,
                'process': 'MFI LFD Stats Pr',
                'runtime': 21526,
                'tty': 0,
                'usecs': 6554},
          454: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 458,
                'process': 'IP SLAs Ethernet',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          455: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 6579,
                'one_min_cpu': 0.0,
                'pid': 459,
                'process': 'VDC process',
                'runtime': 58,
                'tty': 0,
                'usecs': 8},
          456: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 460,
                'process': 'udp_transport Se',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          457: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 3290,
                'one_min_cpu': 0.0,
                'pid': 461,
                'process': 'qos_mon_periodic',
                'runtime': 55,
                'tty': 0,
                'usecs': 16},
          458: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 462,
                'process': 'ISSU Utility Pro',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          459: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 463,
                'process': 'IOSXE-RP Virtual',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          460: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 464,
                'process': 'Online Diag CNS',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          461: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 465,
                'process': 'Online Diag CNS',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          462: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 9,
                'one_min_cpu': 0.0,
                'pid': 466,
                'process': 'MPLS IFMIB Proce',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          463: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 467,
                'process': 'IPC ISSU Version',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          464: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 468,
                'process': 'IPC ISSU Version',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          465: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 469,
                'process': 'IPC ISSU Version',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          466: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 470,
                'process': 'IPC ISSU Version',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          467: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 471,
                'process': 'IPC ISSU Version',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          468: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 472,
                'process': 'IPC ISSU Version',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          469: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 473,
                'process': 'IPC ISSU Version',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          470: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 474,
                'process': 'IPC ISSU Version',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          471: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 475,
                'process': 'IPC ISSU Version',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          472: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 476,
                'process': 'IPC ISSU Version',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          473: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 477,
                'process': 'IPC ISSU Version',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          474: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 478,
                'process': 'IPC ISSU Version',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          475: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 479,
                'process': 'IPC ISSU Version',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          476: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 480,
                'process': 'IPC ISSU Version',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          477: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 481,
                'process': 'MPLS TE OAM Clie',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          478: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 482,
                'process': 'IPC ISSU Version',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          479: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 483,
                'process': 'IPC ISSU Version',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          480: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 484,
                'process': 'IPC ISSU Version',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          481: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 485,
                'process': 'IPC ISSU Version',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          482: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 486,
                'process': 'IPC ISSU Version',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          483: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 487,
                'process': 'IPC ISSU Version',
                'runtime': 1,
                'tty': 0,
                'usecs': 1000},
          484: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 488,
                'process': 'IPC ISSU Version',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          485: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 489,
                'process': 'IPC ISSU Version',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          486: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 490,
                'process': 'IPC ISSU Version',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          487: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 491,
                'process': 'IPC ISSU Version',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          488: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 492,
                'process': 'IPC ISSU Version',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          489: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 493,
                'process': 'IPC ISSU Version',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          490: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 494,
                'process': 'IPC ISSU Version',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          491: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 495,
                'process': 'IPC ISSU Version',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          492: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 496,
                'process': 'IPC ISSU Version',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          493: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 13140,
                'one_min_cpu': 0.0,
                'pid': 497,
                'process': 'DiagCard1/-1',
                'runtime': 829,
                'tty': 0,
                'usecs': 63},
          494: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 498,
                'process': 'IPC ISSU Version',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          495: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 499,
                'process': 'IPC ISSU Version',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          496: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 500,
                'process': 'IPC ISSU Version',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          497: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 501,
                'process': 'IPC ISSU Version',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          498: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 502,
                'process': 'IPC ISSU Version',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          499: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 503,
                'process': 'IPC ISSU Version',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          500: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 504,
                'process': 'IPC ISSU Version',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          501: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 505,
                'process': 'IPC ISSU Version',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          502: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 506,
                'process': 'IPC ISSU Version',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          503: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 507,
                'process': 'IPC ISSU Version',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          504: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 508,
                'process': 'IPC ISSU Version',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          505: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 509,
                'process': 'IPC ISSU Version',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          506: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 510,
                'process': 'IPC ISSU Version',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          507: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 511,
                'process': 'IPC ISSU Version',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          508: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 512,
                'process': 'IPC ISSU Version',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          509: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 13143,
                'one_min_cpu': 0.0,
                'pid': 513,
                'process': 'DiagCard2/-1',
                'runtime': 252,
                'tty': 0,
                'usecs': 19},
          510: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 514,
                'process': 'IPC ISSU Version',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          511: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 515,
                'process': 'IPC ISSU Version',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          512: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 516,
                'process': 'IPC ISSU Version',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          513: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 517,
                'process': 'IPC ISSU Version',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          514: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 518,
                'process': 'IPC ISSU Version',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          515: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 519,
                'process': 'IPC ISSU Version',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          516: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 520,
                'process': 'IPC ISSU Version',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          517: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 521,
                'process': 'IPC ISSU Version',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          518: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 522,
                'process': 'IPC ISSU Version',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          519: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 523,
                'process': 'IPC ISSU Version',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          520: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 524,
                'process': 'IPC ISSU Version',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          521: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 525,
                'process': 'IPC ISSU Version',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          522: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 526,
                'process': 'IPC ISSU Version',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          523: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 527,
                'process': 'IPC ISSU Version',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          524: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 528,
                'process': 'IPC ISSU Version',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          525: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 5,
                'one_min_cpu': 0.0,
                'pid': 529,
                'process': 'CWAN OIR IPC Rea',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          526: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2008,
                'one_min_cpu': 0.0,
                'pid': 530,
                'process': 'mdns Timer Proce',
                'runtime': 261,
                'tty': 0,
                'usecs': 129},
          527: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 65670,
                'one_min_cpu': 0.0,
                'pid': 531,
                'process': 'SBC main process',
                'runtime': 977,
                'tty': 0,
                'usecs': 14},
          528: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 532,
                'process': 'MRIB Process',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          529: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 560,
                'one_min_cpu': 0.0,
                'pid': 533,
                'process': 'EEM Helper Threa',
                'runtime': 8,
                'tty': 0,
                'usecs': 14},
          530: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 6209,
                'one_min_cpu': 0.0,
                'pid': 534,
                'process': 'MFI LFD Timer Pr',
                'runtime': 39,
                'tty': 0,
                'usecs': 6},
          531: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 4702,
                'one_min_cpu': 0.0,
                'pid': 535,
                'process': 'LCON Main',
                'runtime': 354,
                'tty': 0,
                'usecs': 75},
          532: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 4,
                'one_min_cpu': 0.0,
                'pid': 536,
                'process': 'MFI LFD Main Pro',
                'runtime': 1,
                'tty': 0,
                'usecs': 250},
          533: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 6,
                'one_min_cpu': 0.0,
                'pid': 537,
                'process': 'Inter Chassis Pr',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          534: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 3,
                'one_min_cpu': 0.0,
                'pid': 538,
                'process': 'DiagCard3/-1',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          535: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 3,
                'one_min_cpu': 0.0,
                'pid': 539,
                'process': 'DiagCard4/-1',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          536: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 549,
                'one_min_cpu': 0.0,
                'pid': 540,
                'process': 'LDP Background',
                'runtime': 266,
                'tty': 0,
                'usecs': 484},
          537: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 254919,
                'one_min_cpu': 0.0,
                'pid': 541,
                'process': 'MCP RP EFP proce',
                'runtime': 1468,
                'tty': 0,
                'usecs': 5},
          538: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 207,
                'one_min_cpu': 0.0,
                'pid': 542,
                'process': 'BGP Event',
                'runtime': 9701,
                'tty': 0,
                'usecs': 46864},
          539: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2902,
                'one_min_cpu': 0.0,
                'pid': 543,
                'process': 'LDP Main',
                'runtime': 149,
                'tty': 0,
                'usecs': 51},
          540: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 15020,
                'one_min_cpu': 0.0,
                'pid': 544,
                'process': 'LDP Hello',
                'runtime': 854,
                'tty': 0,
                'usecs': 56},
          541: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1320,
                'one_min_cpu': 0.0,
                'pid': 545,
                'process': 'BGP Task',
                'runtime': 13752,
                'tty': 0,
                'usecs': 10418},
          542: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 546,
                'process': 'BGP BMP Server',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          543: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 93,
                'one_min_cpu': 0.0,
                'pid': 547,
                'process': 'TCP Listener',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          544: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 551,
                'one_min_cpu': 0.0,
                'pid': 548,
                'process': 'IPRM',
                'runtime': 2,
                'tty': 0,
                'usecs': 3},
          545: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 673,
                'one_min_cpu': 0.0,
                'pid': 549,
                'process': 'IP SNMP',
                'runtime': 36,
                'tty': 0,
                'usecs': 53},
          546: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 550,
                'process': 'PDU DISPATCHER',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          547: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 4,
                'one_min_cpu': 0.0,
                'pid': 551,
                'process': 'SNMP ENGINE',
                'runtime': 1,
                'tty': 0,
                'usecs': 250},
          548: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 552,
                'process': 'IP SNMPV6',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          549: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 553,
                'process': 'SNMP ConfCopyPro',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          550: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 387,
                'one_min_cpu': 0.0,
                'pid': 554,
                'process': 'SNMP Traps',
                'runtime': 416,
                'tty': 0,
                'usecs': 1074},
          551: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 33806,
                'one_min_cpu': 0.0,
                'pid': 555,
                'process': 'NTP',
                'runtime': 851,
                'tty': 0,
                'usecs': 25},
          552: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 556,
                'process': 'EM Action CNS',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          553: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 557,
                'process': 'DiagCard5/-1',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          554: {'five_min_cpu': 0.73,
                'five_sec_cpu': 0.55,
                'invoked': 78644,
                'one_min_cpu': 0.72,
                'pid': 558,
                'process': 'BGP Router',
                'runtime': 307942,
                'tty': 0,
                'usecs': 3915},
          555: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 10680,
                'one_min_cpu': 0.0,
                'pid': 559,
                'process': 'OSPF-65109 Hello',
                'runtime': 311,
                'tty': 0,
                'usecs': 29},
          556: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 560,
                'process': 'BGP VA',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          557: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 561,
                'process': 'IFCOM Msg Hdlr',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          558: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 562,
                'process': 'IFCOM Msg Hdlr',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          559: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 563,
                'process': 'IFCOM Msg Hdlr',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          560: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 564,
                'process': 'IFCOM Msg Hdlr',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          561: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 565,
                'process': 'Network Synchron',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          562: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 127232,
                'one_min_cpu': 0.0,
                'pid': 566,
                'process': 'CCM Subscriber P',
                'runtime': 862,
                'tty': 0,
                'usecs': 6},
          563: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 4,
                'one_min_cpu': 0.0,
                'pid': 567,
                'process': 'Process to do EH',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          564: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 11,
                'one_min_cpu': 0.0,
                'pid': 568,
                'process': 'RFS server proce',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          565: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 569,
                'process': 'IP MPLS Service',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          566: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 1,
                'one_min_cpu': 0.0,
                'pid': 570,
                'process': 'HA-IDB-SYNC',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          567: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 2,
                'one_min_cpu': 0.0,
                'pid': 571,
                'process': 'VTEMPLATE Backgr',
                'runtime': 0,
                'tty': 0,
                'usecs': 0},
          568: {'five_min_cpu': 0.75,
                'five_sec_cpu': 0.0,
                'invoked': 9517,
                'one_min_cpu': 0.28,
                'pid': 573,
                'process': 'Virtual Exec',
                'runtime': 4487,
                'tty': 2,
                'usecs': 471},
          569: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 15,
                'one_min_cpu': 0.0,
                'pid': 574,
                'process': 'L2FIB HA Flow Th',
                'runtime': 4,
                'tty': 0,
                'usecs': 266},
          570: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 75795,
                'one_min_cpu': 0.0,
                'pid': 575,
                'process': 'Virtual Exec',
                'runtime': 66557,
                'tty': 3,
                'usecs': 878},
          571: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 19063,
                'one_min_cpu': 0.0,
                'pid': 576,
                'process': 'Virtual Exec',
                'runtime': 13105,
                'tty': 4,
                'usecs': 687},
          572: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 797,
                'one_min_cpu': 0.0,
                'pid': 577,
                'process': 'Virtual Exec',
                'runtime': 4208,
                'tty': 5,
                'usecs': 5279},
          573: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 542,
                'one_min_cpu': 0.0,
                'pid': 578,
                'process': 'Virtual Exec',
                'runtime': 71,
                'tty': 6,
                'usecs': 130},
          574: {'five_min_cpu': 0.0,
                'five_sec_cpu': 0.0,
                'invoked': 448,
                'one_min_cpu': 0.0,
                'pid': 606,
                'process': 'LCON Addr',
                'runtime': 17,
                'tty': 0,
                'usecs': 37}},
'zero_cpu_processes': ['Chunk Manager',
                        'Load Meter',
                        'SpanTree Helper',
                        'Retransmission o',
                        'IPC ISSU Dispatc',
                        'RF Slave Main Th',
                        'EDDRI_MAIN',
                        'RO Notify Timers',
                        'Pool Manager',
                        'DiscardQ Backgro',
                        'Timers',
                        'WATCH_AFS',
                        'MEMLEAK PROCESS',
                        'ARP Input',
                        'ARP Background',
                        'ATM Idle Timer',
                        'ATM ASYNC PROC',
                        'AAA_SERVER_DEADT',
                        'Policy Manager',
                        'DDR Timers',
                        'Entity MIB API',
                        'PrstVbl',
                        'RMI RM Notify Wa',
                        'IOSXE heartbeat',
                        'ATM AutoVC Perio',
                        'ATM VC Auto Crea',
                        'IPC Apps Task',
                        'ifIndex Receive',
                        'IPC Event Notifi',
                        'IPC Mcast Pendin',
                        'ASR1000 appsess',
                        'IPC Dynamic Cach',
                        'IPC Service NonC',
                        'IPC Zone Manager',
                        'IPC Periodic Tim',
                        'IPC Deferred Por',
                        'IPC Process leve',
                        'IPC Seat Manager',
                        'IPC Check Queue',
                        'IPC Seat RX Cont',
                        'IPC Seat TX Cont',
                        'IPC Keep Alive M',
                        'IPC Loadometer',
                        'IPC Session Deta',
                        'SENSOR-MGR event',
                        'Compute SRP rate',
                        'CEF MIB API',
                        'Serial Backgroun',
                        'GraphIt',
                        'Dialer event',
                        'IOSXE signals IO',
                        'SMART',
                        'client_entity_se',
                        'RF SCTPthread',
                        'CHKPT RG SCTPthr',
                        'Critical Bkgnd',
                        'Net Background',
                        'IDB Work',
                        'Logger',
                        'TTY Background',
                        'BACK CHECK',
                        'IOSD chasfs task',
                        'REDUNDANCY FSM',
                        'SBC IPC Hold Que',
                        'Punt FP Stats Du',
                        'PuntInject Keepa',
                        'IF-MGR control p',
                        'IF-MGR event pro',
                        'cpf_msg_holdq_pr',
                        'cpf_msg_rcvq_pro',
                        'cpf_process_tpQ',
                        'Network-rf Notif',
                        'Environmental Mo',
                        'RP HA Periodic',
                        'CONSOLE helper p',
                        'CEF RRP RF waite',
                        'CWAN APS HA Proc',
                        'REDUNDANCY peer',
                        '100ms check',
                        'RF CWAN HA Proce',
                        'CWAN IF EVENT HA',
                        'ANCP HA',
                        'ANCP HA IPC flow',
                        'QoS HA ID RETAIN',
                        'CHKPT Test clien',
                        'CHKPT Test clien',
                        'CHKPT Test clien',
                        'CHKPT Test clien',
                        'CHKPT Test clien',
                        'CHKPT Test clien',
                        'CHKPT Test clien',
                        'CHKPT Test clien',
                        'CHKPT Test clien',
                        'CHKPT Test clien',
                        'CHKPT Test clien',
                        'DHCPC HA',
                        'DHCPD HA',
                        'DHCPv6 Relay HA',
                        'DHCPv6 Server HA',
                        'Metadata HA',
                        'FMD HA IPC flow',
                        'SISF HA Process',
                        'ARP HA',
                        'XDR RRP RF waite',
                        'IOSXE-RP Punt IP',
                        'IOSXE-RP SPA TSM',
                        'RF Master Main T',
                        'RF Master Status',
                        'Net Input',
                        'OTV Event Dispat',
                        'Compute load avg',
                        'Per-minute Jobs',
                        'mLDP Process',
                        'Transport Port A',
                        'EEM ED ND',
                        'IOSXE-RP FastPat',
                        'Src Fltr backgro',
                        'DSX3MIB ll handl',
                        'fanrp_l2fib',
                        'POS APS Event Pr',
                        'netclk_process',
                        'netclk_ha_proces',
                        'FPD Management P',
                        'FPD Action Proce',
                        'BFD HW EVENT',
                        'BFD IPV6 ADDR CH',
                        'FEC_Link_event_h',
                        'MCP RP autovc pr',
                        'VMI Background',
                        'MGMTE stats Proc',
                        'Ether-SPA backgr',
                        'CWAN CHOCX PROCE',
                        'CE3 Mailbox',
                        'CT3 Mailbox',
                        'HAL Mailbox',
                        'MIP Mailbox',
                        'CWAN OIR Handler',
                        'TP CUTOVER EVENT',
                        'ASR1K ESMC Proce',
                        'ASR1000-RP SPA A',
                        'RTTYS Process',
                        'AAA Server',
                        'AAA ACCT Proc',
                        'ACCT Periodic Pr',
                        'cdp init process',
                        'Call Home Timer',
                        'CEF switching ba',
                        'ADJ NSF process',
                        'AAA Dictionary R',
                        'FHRP Main thread',
                        'TRACK Main threa',
                        'TRACK Client thr',
                        'VRRP Main thread',
                        'ATM OAM Input',
                        'ATM OAM TIMER',
                        'HQF TARGET DYNAM',
                        'IP ARP Adjacency',
                        'IP Input',
                        'ICMP event handl',
                        'mDNS',
                        'PIM register asy',
                        'IPv6 ping proces',
                        'BGP Scheduler',
                        'MOP Protocols',
                        'PPP SIP',
                        'PPP Bind',
                        'PPP IP Route',
                        'LSP Verification',
                        'RIB LM VALIDATE',
                        'SSM connection m',
                        'SSS Manager',
                        'SSS Policy Manag',
                        'SSS Feature Mana',
                        'SSS Feature Time',
                        'Spanning Tree',
                        'VRRS',
                        'Ethernet LMI',
                        'Ethernet OAM Pro',
                        'Ethernet CFM',
                        'mcp callhome per',
                        'PPCP RP Stats Ba',
                        'Appnav auto disc',
                        'L2FIB Timer Disp',
                        'MLRIB L2 Msg Thr',
                        'Spanning Tree St',
                        'IGMP Route Msg H',
                        'IGMP Route Rx Pr',
                        'RABAPOL HA',
                        'RABAPOL HA IPC f',
                        'TEMPLATE HA',
                        'DVLAN HA',
                        'CCM',
                        'CCM IPC flow con',
                        'RG Faults Timer',
                        'RG VP',
                        'RG AR',
                        'RG Protocol Time',
                        'RG Transport Tim',
                        'HDLC HA',
                        'SBC initializer',
                        'SVM HA',
                        'UDLD',
                        'AC Switch',
                        'IEDGE ACCT TIMER',
                        'ISG CMD HANDLER',
                        'IMA PROC',
                        'IP Lite session',
                        'IP PORTBUNDLE',
                        'SSS Mobility mes',
                        'IP Static Sessio',
                        'DVLAN Config Pro',
                        'IPAM/ODAP Events',
                        'IPAM Manager',
                        'IPAM Events',
                        'OCE punted Pkts',
                        'O-UNI Client Msg',
                        'LSP Tunnel FRR',
                        'MPLS Auto-Tunnel',
                        'st_pw_oam',
                        'AAA EPD HANDLER',
                        'PM EPD API',
                        'DM Proc',
                        'RADIUS Proxy',
                        'SSS PM SHIM QOS',
                        'LONG TO SHORT NA',
                        'Timer handler fo',
                        'Prepaid response',
                        'Timed Policy act',
                        'AAA response han',
                        'AAA System Acct',
                        'VPWS Thread',
                        'IP Traceroute',
                        'Tunnel',
                        'ATIP_UDP_TSK',
                        'XDR background p',
                        'XDR mcast',
                        'XDR RP Ping Back',
                        'XDR receive',
                        'IPC LC Message H',
                        'XDR RP Test Back',
                        'FRR Background P',
                        'CEF background p',
                        'fib_fib_bfd_sb e',
                        'IP IRDP',
                        'SNMP Timers',
                        'LSD HA Proc',
                        'CEF RP Backgroun',
                        'Routing Topology',
                        'IP RIB Update',
                        'IP Background',
                        'IP Connected Rou',
                        'PPP Compress Inp',
                        'PPP Compress Res',
                        'Tunnel FIB',
                        'ADJ background',
                        'Collection proce',
                        'ADJ resolve proc',
                        'Socket Timers',
                        'TCP Timer',
                        'TCP Protocols',
                        'COPS',
                        'NGCP SCHEDULER P',
                        'STILE PERIODIC T',
                        'UV AUTO CUSTOM P',
                        'Dialer Forwarder',
                        'Service Routing',
                        'SR CapMan Proces',
                        'Flow Exporter Ti',
                        'Flow Exporter Pa',
                        'HTTP CORE',
                        'SBC Msg Ack Time',
                        'MFIB Master back',
                        'VFI Mgr',
                        'MVPN Mgr Process',
                        'Multicast Offloa',
                        'RARP Input',
                        'static',
                        'App Route Proces',
                        'IPv6 RIB Cleanup',
                        'IPv6 RIB Event H',
                        'IPv6 Static Hand',
                        'DHCPv6 LQ client',
                        'AToM manager',
                        'PPP NBF',
                        'PfR BR Learn',
                        'PAD InCall',
                        'QoS stats proces',
                        'RBSCP Background',
                        'SCTP Main Proces',
                        'VPDN call manage',
                        'XC RIB MGR',
                        'AToM LDP manager',
                        'EFP Errd',
                        'Ether EFP Proces',
                        'Ether Infra RP',
                        'CFM HA IPC messa',
                        'Ethernet PM Proc',
                        'Ethernet PM Soft',
                        'Ethernet PM Moni',
                        'Ethernet Datapla',
                        'ELB HA IPC flow',
                        'IGMPSN L2MCM',
                        'IGMPSN MRD',
                        'IGMPSN',
                        'TCP HA PROC',
                        'BGP HA SSO',
                        'RSVP SYNC',
                        'RETRY_REPOPULATE',
                        'XDR FOF process',
                        'BD Route Msg Hol',
                        'BD Route Rx Proc',
                        'BD MACSEC HA',
                        'BD MACSEC HA CHK',
                        'L2FIB Event Disp',
                        'STP HA IPC flow',
                        'IGMPQR',
                        'AAA HA',
                        'AAA HA cleanup',
                        'ac_atm_state_eve',
                        'ac_atm_mraps_hsp',
                        'AC HA Bulk Sync',
                        'ATM HA',
                        'ATM HA IPC flow',
                        'ATM HA AC',
                        'BFD HA',
                        'FR HA',
                        'GLBP HA',
                        'HSRP HA',
                        'Inspect process',
                        'BGP I/O',
                        'IP SIP Process',
                        'MRIB RP Proxy',
                        'IPv6 ACL RP Proc',
                        'Netsync IPC flow',
                        'PPPoE VRRS EVT M',
                        'RG If-Mgr Timer',
                        'RG Media Timer',
                        'MCPRP RG Timer',
                        'URL filter proc',
                        'VFI HA Bulk Sync',
                        'XC RIB HA Bulk S',
                        'XC BGP SIG RIB H',
                        'VPDN CCM Backgro',
                        'VRRP HA',
                        'VTEMPLATE IPC fl',
                        'CEM PROC',
                        'CEM HA',
                        'CEM HA AC',
                        'L2X Switching Ev',
                        'Probe Input',
                        'IP Inband Sessio',
                        'DHCP SIP',
                        'FRR Manager',
                        'MFI Comm RP Proc',
                        'Path set broker',
                        'LFD Label Block',
                        'LDP HA',
                        'MPLS VPN HA Clie',
                        'TSPTUN HA',
                        'RSVP HA Services',
                        'TE NSR OOS DB Pr',
                        'MPLS TP HA',
                        'AToM HA Bulk Syn',
                        'AToM MGR HA IPC',
                        'LFDp Input Proc',
                        'AAA Cached Serve',
                        'ENABLE AAA',
                        'EM Background Pr',
                        'LDAP process',
                        'Opaque Database',
                        'Key chain liveke',
                        'LINE AAA',
                        'LOCAL AAA',
                        'TPLUS',
                        'DynCmd Package P',
                        'FLEX DSPRM MAIN',
                        'VSP_MGR',
                        'STUN_APP',
                        'STUN_TEST',
                        'Manet Infra Back',
                        'IDMGR CORE',
                        'MPLS Auto Mesh P',
                        'RSCMSM VOLUME MO',
                        'CCSIP_EVENT_TRAC',
                        'Sip MPA',
                        'QOS_MODULE_MAIN',
                        'IP TRUST Registe',
                        'VoIP AAA',
                        'COND_DEBUG HA IP',
                        'PIM HA',
                        'MMON PROCESS',
                        'QOS PERUSER',
                        'RPMS_PROC_MAIN',
                        'http client proc',
                        'OSPF-65109 Router',
                        'SEGMENT ROUTING',
                        'AAA SEND STOP EV',
                        'Test AAA Client',
                        'dcm_cli_engine',
                        'dcm_cli_provider',
                        'DCM Core Thread',
                        'EEM ED Syslog',
                        'EEM ED Generic',
                        'EEM ED Track',
                        'EEM ED Routing',
                        'EEM ED Resource',
                        'Syslog Traps',
                        'Policy HA Timer',
                        'BGP Consistency',
                        'ICRM',
                        'Online Diag EEM',
                        'SPA ENTITY Proce',
                        'SONET Traps',
                        'ISG MIB jobs Man',
                        'SBC RF config sy',
                        'DCM snmp dp Thre',
                        'snmp dcm ma shim',
                        'Bulkstat-Client',
                        'dcm_expression_p',
                        'EEM Server',
                        'Call Home proces',
                        'Call Home DS',
                        'Call Home DSfile',
                        'EEM Policy Direc',
                        'LSD Main Proc',
                        'EEM ED CLI',
                        'EEM ED Counter',
                        'EEM ED Interface',
                        'EEM ED IOSWD',
                        'EEM ED None',
                        'EEM ED OIR',
                        'EEM ED RF',
                        'EEM ED SNMP',
                        'EEM ED SNMP Obje',
                        'EEM ED SNMP Noti',
                        'EEM ED Timer',
                        'EEM ED Ipsla',
                        'EEM ED Test',
                        'EEM ED Config',
                        'EEM ED Env',
                        'EEM ED DS',
                        'EEM ED CRASH',
                        'EM ED GOLD',
                        'Syslog',
                        'IP SLAs Ethernet',
                        'VDC process',
                        'udp_transport Se',
                        'qos_mon_periodic',
                        'ISSU Utility Pro',
                        'IOSXE-RP Virtual',
                        'Online Diag CNS',
                        'Online Diag CNS',
                        'MPLS IFMIB Proce',
                        'IPC ISSU Version',
                        'IPC ISSU Version',
                        'IPC ISSU Version',
                        'IPC ISSU Version',
                        'IPC ISSU Version',
                        'IPC ISSU Version',
                        'IPC ISSU Version',
                        'IPC ISSU Version',
                        'IPC ISSU Version',
                        'IPC ISSU Version',
                        'IPC ISSU Version',
                        'IPC ISSU Version',
                        'IPC ISSU Version',
                        'IPC ISSU Version',
                        'MPLS TE OAM Clie',
                        'IPC ISSU Version',
                        'IPC ISSU Version',
                        'IPC ISSU Version',
                        'IPC ISSU Version',
                        'IPC ISSU Version',
                        'IPC ISSU Version',
                        'IPC ISSU Version',
                        'IPC ISSU Version',
                        'IPC ISSU Version',
                        'IPC ISSU Version',
                        'IPC ISSU Version',
                        'IPC ISSU Version',
                        'IPC ISSU Version',
                        'IPC ISSU Version',
                        'IPC ISSU Version',
                        'DiagCard1/-1',
                        'IPC ISSU Version',
                        'IPC ISSU Version',
                        'IPC ISSU Version',
                        'IPC ISSU Version',
                        'IPC ISSU Version',
                        'IPC ISSU Version',
                        'IPC ISSU Version',
                        'IPC ISSU Version',
                        'IPC ISSU Version',
                        'IPC ISSU Version',
                        'IPC ISSU Version',
                        'IPC ISSU Version',
                        'IPC ISSU Version',
                        'IPC ISSU Version',
                        'IPC ISSU Version',
                        'DiagCard2/-1',
                        'IPC ISSU Version',
                        'IPC ISSU Version',
                        'IPC ISSU Version',
                        'IPC ISSU Version',
                        'IPC ISSU Version',
                        'IPC ISSU Version',
                        'IPC ISSU Version',
                        'IPC ISSU Version',
                        'IPC ISSU Version',
                        'IPC ISSU Version',
                        'IPC ISSU Version',
                        'IPC ISSU Version',
                        'IPC ISSU Version',
                        'IPC ISSU Version',
                        'IPC ISSU Version',
                        'CWAN OIR IPC Rea',
                        'mdns Timer Proce',
                        'SBC main process',
                        'MRIB Process',
                        'EEM Helper Threa',
                        'MFI LFD Timer Pr',
                        'LCON Main',
                        'MFI LFD Main Pro',
                        'Inter Chassis Pr',
                        'DiagCard3/-1',
                        'DiagCard4/-1',
                        'LDP Background',
                        'MCP RP EFP proce',
                        'BGP Event',
                        'LDP Main',
                        'LDP Hello',
                        'BGP Task',
                        'BGP BMP Server',
                        'TCP Listener',
                        'IPRM',
                        'IP SNMP',
                        'PDU DISPATCHER',
                        'SNMP ENGINE',
                        'IP SNMPV6',
                        'SNMP ConfCopyPro',
                        'SNMP Traps',
                        'NTP',
                        'EM Action CNS',
                        'DiagCard5/-1',
                        'OSPF-65109 Hello',
                        'BGP VA',
                        'IFCOM Msg Hdlr',
                        'IFCOM Msg Hdlr',
                        'IFCOM Msg Hdlr',
                        'IFCOM Msg Hdlr',
                        'Network Synchron',
                        'CCM Subscriber P',
                        'Process to do EH',
                        'RFS server proce',
                        'IP MPLS Service',
                        'HA-IDB-SYNC',
                        'VTEMPLATE Backgr',
                        'L2FIB HA Flow Th',
                        'Virtual Exec',
                        'Virtual Exec',
                        'Virtual Exec',
                        'Virtual Exec',
                        'LCON Addr']}

    golden_output = {'execute.return_value': '''\
        Router#show process cpu
        Load for five secs: 1%/0%; one minute: 2%; five minutes: 3%
        Time source is NTP, 19:10:39.512 EST Mon Oct 17 2016

        CPU utilization for five seconds: 1%/0%; one minute: 2%; five minutes: 3%
         PID Runtime(ms)     Invoked      uSecs   5Sec   1Min   5Min TTY Process 
           1          15        1016         14  0.00%  0.00%  0.00%   0 Chunk Manager    
           2        1883        6576        286  0.00%  0.00%  0.00%   0 Load Meter       
           3           2           2       1000  0.00%  0.00%  0.00%   0 SpanTree Helper  
           4           2         120         16  0.00%  0.00%  0.00%   0 Retransmission o 
           5           1           4        250  0.00%  0.00%  0.00%   0 IPC ISSU Dispatc 
           6          48         210        228  0.00%  0.00%  0.00%   0 RF Slave Main Th 
           7           0           1          0  0.00%  0.00%  0.00%   0 EDDRI_MAIN       
           8           0          34          0  0.00%  0.00%  0.00%   0 RO Notify Timers 
           9      192629       11390      16912  0.00%  0.59%  0.46%   0 Check heaps      
          10          60         556        107  0.00%  0.00%  0.00%   0 Pool Manager     
          11          21           4       5250  0.00%  0.00%  0.00%   0 DiscardQ Backgro 
          12           0           2          0  0.00%  0.00%  0.00%   0 Timers           
          13           8        6865          1  0.00%  0.00%  0.00%   0 WATCH_AFS        
          14           0           1          0  0.00%  0.00%  0.00%   0 MEMLEAK PROCESS  
          15        2538       50568         50  0.00%  0.00%  0.00%   0 ARP Input        
          16         413       34824         11  0.00%  0.00%  0.00%   0 ARP Background   
          17           0           2          0  0.00%  0.00%  0.00%   0 ATM Idle Timer   
          18           0           1          0  0.00%  0.00%  0.00%   0 ATM ASYNC PROC   
          19           0           1          0  0.00%  0.00%  0.00%   0 AAA_SERVER_DEADT 
          20           0           1          0  0.00%  0.00%  0.00%   0 Policy Manager   
          21           0           2          0  0.00%  0.00%  0.00%   0 DDR Timers       
          22          65          54       1203  0.00%  0.00%  0.00%   0 Entity MIB API   
          23         148         254        582  0.00%  0.00%  0.00%   0 PrstVbl          
          24           0           1          0  0.00%  0.00%  0.00%   0 RMI RM Notify Wa 
          25         150       16446          9  0.00%  0.00%  0.00%   0 IOSXE heartbeat  
          26           0           2          0  0.00%  0.00%  0.00%   0 ATM AutoVC Perio 
          27           0           2          0  0.00%  0.00%  0.00%   0 ATM VC Auto Crea 
          28           3          73         41  0.00%  0.00%  0.00%   0 IPC Apps Task    
          29           0          11          0  0.00%  0.00%  0.00%   0 ifIndex Receive  
          30          36        6580          5  0.00%  0.00%  0.00%   0 IPC Event Notifi 
          31         161       32091          5  0.00%  0.00%  0.00%   0 IPC Mcast Pendin 
          32           0           1          0  0.00%  0.00%  0.00%   0 ASR1000 appsess  
          33          12         549         21  0.00%  0.00%  0.00%   0 IPC Dynamic Cach 
          34         593        6678         88  0.00%  0.00%  0.00%   0 IPC Service NonC 
          35           0           1          0  0.00%  0.00%  0.00%   0 IPC Zone Manager 
          36         239       32091          7  0.00%  0.00%  0.00%   0 IPC Periodic Tim 
          37         176       32090          5  0.00%  0.00%  0.00%   0 IPC Deferred Por 
          38           0           1          0  0.00%  0.00%  0.00%   0 IPC Process leve 
          39         464       15214         30  0.00%  0.00%  0.00%   0 IPC Seat Manager 
          40          10        1881          5  0.00%  0.00%  0.00%   0 IPC Check Queue  
          41          20         556         35  0.00%  0.00%  0.00%   0 IPC Seat RX Cont 
          42           0           1          0  0.00%  0.00%  0.00%   0 IPC Seat TX Cont 
          43         100        3291         30  0.00%  0.00%  0.00%   0 IPC Keep Alive M 
          44         687        6580        104  0.00%  0.00%  0.00%   0 IPC Loadometer   
          45           0           1          0  0.00%  0.00%  0.00%   0 IPC Session Deta 
          46           0           1          0  0.00%  0.00%  0.00%   0 SENSOR-MGR event 
          47          17        3292          5  0.00%  0.00%  0.00%   0 Compute SRP rate 
          48           0           1          0  0.00%  0.00%  0.00%   0 CEF MIB API      
          49           0           2          0  0.00%  0.00%  0.00%   0 Serial Backgroun 
          50         267       32875          8  0.00%  0.00%  0.00%   0 GraphIt          
          51           1           2        500  0.00%  0.00%  0.00%   0 Dialer event     
          52           0           1          0  0.00%  0.00%  0.00%   0 IOSXE signals IO 
          53           0           2          0  0.00%  0.00%  0.00%   0 SMART            
          54           1          17         58  0.00%  0.00%  0.00%   0 client_entity_se 
          55           0           1          0  0.00%  0.00%  0.00%   0 RF SCTPthread    
          56           0           1          0  0.00%  0.00%  0.00%   0 CHKPT RG SCTPthr 
          57           0           1          0  0.00%  0.00%  0.00%   0 SERIAL A'detect  
          58           3           4        750  0.00%  0.00%  0.00%   0 Critical Bkgnd   
          59        1949       51594         37  0.00%  0.00%  0.00%   0 Net Background   
          60           0           3          0  0.00%  0.00%  0.00%   0 IDB Work         
          61          11         728         15  0.00%  0.00%  0.00%   0 Logger           
          62         385       32836         11  0.00%  0.00%  0.00%   0 TTY Background   
          63           0           1          0  0.00%  0.00%  0.00%   0 BACK CHECK       
          64       17768      282755         62  0.07%  0.04%  0.05%   0 IOSD ipc task    
          65        1119       79222         14  0.00%  0.00%  0.00%   0 IOSD chasfs task 
          66          41        4712          8  0.00%  0.00%  0.00%   0 REDUNDANCY FSM   
          67           0           9          0  0.00%  0.00%  0.00%   0 SBC IPC Hold Que 
          68           0           1          0  0.00%  0.00%  0.00%   0 Punt FP Stats Du 
          69         912       16390         55  0.00%  0.00%  0.00%   0 PuntInject Keepa 
          70         340         260       1307  0.00%  0.00%  0.00%   0 IF-MGR control p 
          71           2          34         58  0.00%  0.00%  0.00%   0 IF-MGR event pro 
          72          48         290        165  0.00%  0.00%  0.00%   0 cpf_msg_holdq_pr 
          73         176        6715         26  0.00%  0.00%  0.00%   0 cpf_msg_rcvq_pro 
          74       17155       13566       1264  0.00%  0.00%  0.00%   0 cpf_process_tpQ  
          75           1           2        500  0.00%  0.00%  0.00%   0 Network-rf Notif 
          76        1034       32866         31  0.00%  0.00%  0.00%   0 Environmental Mo 
          77         206       32866          6  0.00%  0.00%  0.00%   0 RP HA Periodic   
          78           0           1          0  0.00%  0.00%  0.00%   0 CONSOLE helper p 
          79           5         355         14  0.00%  0.00%  0.00%   0 CEF RRP RF waite 
          80           0           3          0  0.00%  0.00%  0.00%   0 CWAN APS HA Proc 
          81        1041       42450         24  0.00%  0.00%  0.00%   0 REDUNDANCY peer  
          82        2062      328370          6  0.00%  0.00%  0.00%   0 100ms check      
          83          11         554         19  0.00%  0.00%  0.00%   0 RF CWAN HA Proce 
          84           1           9        111  0.00%  0.00%  0.00%   0 CWAN IF EVENT HA 
          85           1           5        200  0.00%  0.00%  0.00%   0 ANCP HA          
          86           0          18          0  0.00%  0.00%  0.00%   0 ANCP HA IPC flow 
          87           0           1          0  0.00%  0.00%  0.00%   0 QoS HA ID RETAIN 
          88           0           1          0  0.00%  0.00%  0.00%   0 CHKPT Test clien 
          89           0           1          0  0.00%  0.00%  0.00%   0 CHKPT Test clien 
          90           0           1          0  0.00%  0.00%  0.00%   0 CHKPT Test clien 
          91           0           1          0  0.00%  0.00%  0.00%   0 CHKPT Test clien 
          92           0           1          0  0.00%  0.00%  0.00%   0 CHKPT Test clien 
          93           0           1          0  0.00%  0.00%  0.00%   0 CHKPT Test clien 
          94           0           1          0  0.00%  0.00%  0.00%   0 CHKPT Test clien 
          95           0           1          0  0.00%  0.00%  0.00%   0 CHKPT Test clien 
          96           0           1          0  0.00%  0.00%  0.00%   0 CHKPT Test clien 
          97           0           1          0  0.00%  0.00%  0.00%   0 CHKPT Test clien 
          98           0           1          0  0.00%  0.00%  0.00%   0 CHKPT Test clien 
          99           1           7        142  0.00%  0.00%  0.00%   0 DHCPC HA         
         100           1           7        142  0.00%  0.00%  0.00%   0 DHCPD HA         
         101           0           8          0  0.00%  0.00%  0.00%   0 DHCPv6 Relay HA  
         102           0           8          0  0.00%  0.00%  0.00%   0 DHCPv6 Server HA 
         103           0           5          0  0.00%  0.00%  0.00%   0 Metadata HA      
         104           0          18          0  0.00%  0.00%  0.00%   0 FMD HA IPC flow  
         105           1           3        333  0.00%  0.00%  0.00%   0 SISF HA Process  
         106          15         174         86  0.00%  0.00%  0.00%   0 ARP HA           
         107           0           1          0  0.00%  0.00%  0.00%   0 XDR RRP RF waite 
         108       13441      407444         32  0.00%  0.03%  0.02%   0 IOSXE-RP Punt Se 
         109           0           1          0  0.00%  0.00%  0.00%   0 IOSXE-RP Punt IP 
         110           1           4        250  0.00%  0.00%  0.00%   0 IOSXE-RP SPA TSM 
         111          78        8256          9  0.00%  0.00%  0.00%   0 RF Master Main T 
         112         488        8220         59  0.00%  0.00%  0.00%   0 RF Master Status 
         113          92        7528         12  0.00%  0.00%  0.00%   0 Net Input        
         114           1           5        200  0.00%  0.00%  0.00%   0 OTV Event Dispat 
         115         161        3290         48  0.00%  0.00%  0.00%   0 Compute load avg 
         116        3720        1097       3391  0.00%  0.00%  0.00%   0 Per-minute Jobs  
         117        4496       32944        136  0.07%  0.01%  0.00%   0 Per-Second Jobs  
         118         247       32847          7  0.00%  0.00%  0.00%   0 mLDP Process     
         119           1          46         21  0.00%  0.00%  0.00%   0 Transport Port A 
         120           3         310          9  0.00%  0.00%  0.00%   0 EEM ED ND        
         121           0           1          0  0.00%  0.00%  0.00%   0 IOSXE-RP FastPat 
         122           0           1          0  0.00%  0.00%  0.00%   0 Src Fltr backgro 
         123           0           1          0  0.00%  0.00%  0.00%   0 DSX3MIB ll handl 
         124         223       32087          6  0.00%  0.00%  0.00%   0 fanrp_l2fib      
         125           0           1          0  0.00%  0.00%  0.00%   0 POS APS Event Pr 
         126           5           3       1666  0.00%  0.00%  0.00%   0 netclk_process   
         127           1           3        333  0.00%  0.00%  0.00%   0 netclk_ha_proces 
         128           4           7        571  0.00%  0.00%  0.00%   0 FPD Management P 
         129           0           1          0  0.00%  0.00%  0.00%   0 FPD Action Proce 
         130           0           1          0  0.00%  0.00%  0.00%   0 BFD HW EVENT     
         131           0           1          0  0.00%  0.00%  0.00%   0 BFD IPV6 ADDR CH 
         132           0           2          0  0.00%  0.00%  0.00%   0 FEC_Link_event_h 
         133        1395      255002          5  0.00%  0.00%  0.00%   0 MCP RP autovc pr 
         134           0           2          0  0.00%  0.00%  0.00%   0 VMI Background   
         135         259        6563         39  0.00%  0.00%  0.00%   0 MGMTE stats Proc 
         136         386       44788          8  0.00%  0.00%  0.00%   0 Ether-SPA backgr 
         137         207       32863          6  0.00%  0.00%  0.00%   0 CWAN CHOCX PROCE 
         138           0           1          0  0.00%  0.00%  0.00%   0 CE3 Mailbox      
         139           0           1          0  0.00%  0.00%  0.00%   0 CT3 Mailbox      
         140           0           1          0  0.00%  0.00%  0.00%   0 HAL Mailbox      
         141           0           2          0  0.00%  0.00%  0.00%   0 MIP Mailbox      
         142        1001        1198        835  0.00%  0.00%  0.00%   0 CWAN OIR Handler 
         143           0           1          0  0.00%  0.00%  0.00%   0 TP CUTOVER EVENT 
         144           0           1          0  0.00%  0.00%  0.00%   0 ASR1K ESMC Proce 
         145           0           1          0  0.00%  0.00%  0.00%   0 ASR1000-RP SPA A 
         146           0           1          0  0.00%  0.00%  0.00%   0 RTTYS Process    
         147           1         130          7  0.00%  0.00%  0.00%   0 AAA Server       
         148           0           1          0  0.00%  0.00%  0.00%   0 AAA ACCT Proc    
         149           0           1          0  0.00%  0.00%  0.00%   0 ACCT Periodic Pr 
         150         140       32863          4  0.00%  0.00%  0.00%   0 cdp init process 
         151           6         565         10  0.00%  0.00%  0.00%   0 Call Home Timer  
         152           0           2          0  0.00%  0.00%  0.00%   0 CEF switching ba 
         153           0           1          0  0.00%  0.00%  0.00%   0 ADJ NSF process  
         154           0           2          0  0.00%  0.00%  0.00%   0 AAA Dictionary R 
         155         504       32863         15  0.00%  0.00%  0.00%   0 FHRP Main thread 
         156           0           1          0  0.00%  0.00%  0.00%   0 TRACK Main threa 
         157           0           1          0  0.00%  0.00%  0.00%   0 TRACK Client thr 
         158           0           1          0  0.00%  0.00%  0.00%   0 VRRP Main thread 
         159        4663      510138          9  0.07%  0.00%  0.00%   0 VRRS Main thread 
         160           0           2          0  0.00%  0.00%  0.00%   0 ATM OAM Input    
         161           0           2          0  0.00%  0.00%  0.00%   0 ATM OAM TIMER    
         162           0           1          0  0.00%  0.00%  0.00%   0 HQF TARGET DYNAM 
         163          45         247        182  0.00%  0.00%  0.00%   0 IP ARP Adjacency 
         164        5672     1006869          5  0.07%  0.01%  0.00%   0 IP ARP Retry Age 
         165           2         549          3  0.00%  0.00%  0.00%   0 IP Input         
         166           0           1          0  0.00%  0.00%  0.00%   0 ICMP event handl 
         167         283       32863          8  0.00%  0.00%  0.00%   0 mDNS             
         168           0           3          0  0.00%  0.00%  0.00%   0 PIM register asy 
         169           0           1          0  0.00%  0.00%  0.00%   0 IPv6 ping proces 
         170         589       32063         18  0.00%  0.00%  0.00%   0 BGP Scheduler    
         171          11         116         94  0.00%  0.00%  0.00%   0 MOP Protocols    
         172           0           2          0  0.00%  0.00%  0.00%   0 PPP SIP          
         173           0           2          0  0.00%  0.00%  0.00%   0 PPP Bind         
         174           0           2          0  0.00%  0.00%  0.00%   0 PPP IP Route     
         175           1           1       1000  0.00%  0.00%  0.00%   0 LSP Verification 
         176           0           2          0  0.00%  0.00%  0.00%   0 RIB LM VALIDATE  
         177         170         346        491  0.00%  0.00%  0.00%   0 SSM connection m 
         178           2         549          3  0.00%  0.00%  0.00%   0 SSS Manager      
         179           0           1          0  0.00%  0.00%  0.00%   0 SSS Policy Manag 
         180           0           1          0  0.00%  0.00%  0.00%   0 SSS Feature Mana 
         181         932      128492          7  0.00%  0.00%  0.00%   0 SSS Feature Time 
         182           0           2          0  0.00%  0.00%  0.00%   0 Spanning Tree    
         183           0           1          0  0.00%  0.00%  0.00%   0 VRRS             
         184           0           2          0  0.00%  0.00%  0.00%   0 Ethernet LMI     
         185           0           2          0  0.00%  0.00%  0.00%   0 Ethernet OAM Pro 
         186           1           2        500  0.00%  0.00%  0.00%   0 Ethernet CFM     
         187         357        5561         64  0.00%  0.00%  0.00%   0 mcp callhome per 
         188           0           1          0  0.00%  0.00%  0.00%   0 PPCP RP Stats Ba 
         189           0         110          0  0.00%  0.00%  0.00%   0 Appnav auto disc 
         190           0           1          0  0.00%  0.00%  0.00%   0 L2FIB Timer Disp 
         191          10          71        140  0.00%  0.00%  0.00%   0 MLRIB L2 Msg Thr 
         192           0           1          0  0.00%  0.00%  0.00%   0 Spanning Tree St 
         193           0           2          0  0.00%  0.00%  0.00%   0 IGMP Route Msg H 
         194           0          36          0  0.00%  0.00%  0.00%   0 IGMP Route Rx Pr 
         195           0           3          0  0.00%  0.00%  0.00%   0 RABAPOL HA       
         196           0          18          0  0.00%  0.00%  0.00%   0 RABAPOL HA IPC f 
         197           1           9        111  0.00%  0.00%  0.00%   0 TEMPLATE HA      
         198           0           4          0  0.00%  0.00%  0.00%   0 DVLAN HA         
         199          13          90        144  0.00%  0.00%  0.00%   0 CCM              
         200           0          18          0  0.00%  0.00%  0.00%   0 CCM IPC flow con 
         201           0           2          0  0.00%  0.00%  0.00%   0 RG Faults Timer  
         202           0           1          0  0.00%  0.00%  0.00%   0 RG VP            
         203           0           2          0  0.00%  0.00%  0.00%   0 RG AR            
         204           0           2          0  0.00%  0.00%  0.00%   0 RG Protocol Time 
         205           0           2          0  0.00%  0.00%  0.00%   0 RG Transport Tim 
         206           0           2          0  0.00%  0.00%  0.00%   0 HDLC HA          
         207           1           1       1000  0.00%  0.00%  0.00%   0 SBC initializer  
         208           0           3          0  0.00%  0.00%  0.00%   0 SVM HA           
         209         423       32876         12  0.00%  0.00%  0.00%   0 UDLD             
         210           0           1          0  0.00%  0.00%  0.00%   0 AC Switch        
         211           0           1          0  0.00%  0.00%  0.00%   0 IEDGE ACCT TIMER 
         212           0           1          0  0.00%  0.00%  0.00%   0 ISG CMD HANDLER  
         213           0           1          0  0.00%  0.00%  0.00%   0 IMA PROC         
         214          35        8033          4  0.00%  0.00%  0.00%   0 IP Lite session  
         215           0           2          0  0.00%  0.00%  0.00%   0 IP PORTBUNDLE    
         216           0           2          0  0.00%  0.00%  0.00%   0 SSS Mobility mes 
         217          35        8026          4  0.00%  0.00%  0.00%   0 IP Static Sessio 
         218           0           2          0  0.00%  0.00%  0.00%   0 DVLAN Config Pro 
         219           0           2          0  0.00%  0.00%  0.00%   0 IPAM/ODAP Events 
         220        6054     1006869          6  0.00%  0.00%  0.00%   0 IPAM Manager     
         221           0           2          0  0.00%  0.00%  0.00%   0 IPAM Events      
         222           0           2          0  0.00%  0.00%  0.00%   0 OCE punted Pkts  
         223           0           1          0  0.00%  0.00%  0.00%   0 O-UNI Client Msg 
         224           0           1          0  0.00%  0.00%  0.00%   0 LSP Tunnel FRR   
         225           0           5          0  0.00%  0.00%  0.00%   0 MPLS Auto-Tunnel 
         226           0           1          0  0.00%  0.00%  0.00%   0 st_pw_oam        
         227           0           1          0  0.00%  0.00%  0.00%   0 AAA EPD HANDLER  
         228           0           1          0  0.00%  0.00%  0.00%   0 PM EPD API       
         229           0           1          0  0.00%  0.00%  0.00%   0 DM Proc          
         230           0           1          0  0.00%  0.00%  0.00%   0 RADIUS Proxy     
         231           0           1          0  0.00%  0.00%  0.00%   0 SSS PM SHIM QOS  
         232           0           1          0  0.00%  0.00%  0.00%   0 LONG TO SHORT NA 
         233           0           1          0  0.00%  0.00%  0.00%   0 Timer handler fo 
         234           0           1          0  0.00%  0.00%  0.00%   0 Prepaid response 
         235           0           1          0  0.00%  0.00%  0.00%   0 Timed Policy act 
         236           0           1          0  0.00%  0.00%  0.00%   0 AAA response han 
         237           0           1          0  0.00%  0.00%  0.00%   0 AAA System Acct  
         238           0           2          0  0.00%  0.00%  0.00%   0 VPWS Thread      
         239           0           1          0  0.00%  0.00%  0.00%   0 IP Traceroute    
         240           0           2          0  0.00%  0.00%  0.00%   0 Tunnel           
         241           0           2          0  0.00%  0.00%  0.00%   0 ATIP_UDP_TSK     
         242           0           1          0  0.00%  0.00%  0.00%   0 XDR background p 
         243       19944       18357       1086  0.00%  0.00%  0.00%   0 XDR mcast        
         244           0           3          0  0.00%  0.00%  0.00%   0 XDR RP Ping Back 
         245          46         211        218  0.00%  0.00%  0.00%   0 XDR receive      
         246           0           4          0  0.00%  0.00%  0.00%   0 IPC LC Message H 
         247           0           1          0  0.00%  0.00%  0.00%   0 XDR RP Test Back 
         248           2         549          3  0.00%  0.00%  0.00%   0 FRR Background P 
         249       26621        3521       7560  0.00%  0.00%  0.00%   0 CEF background p 
         250           0           1          0  0.00%  0.00%  0.00%   0 fib_fib_bfd_sb e 
         251           0           1          0  0.00%  0.00%  0.00%   0 IP IRDP          
         252           0           7          0  0.00%  0.00%  0.00%   0 SNMP Timers      
         253           1           5        200  0.00%  0.00%  0.00%   0 LSD HA Proc      
         254          14         148         94  0.00%  0.00%  0.00%   0 CEF RP Backgroun 
         255           0           2          0  0.00%  0.00%  0.00%   0 Routing Topology 
         256      337307        7171      47037  0.00%  0.00%  0.00%   0 IP RIB Update    
         257        1371         915       1498  0.00%  0.00%  0.00%   0 IP Background    
         258         229         837        273  0.00%  0.00%  0.00%   0 IP Connected Rou 
         259           0           2          0  0.00%  0.00%  0.00%   0 PPP Compress Inp 
         260           0           2          0  0.00%  0.00%  0.00%   0 PPP Compress Res 
         261           0           1          0  0.00%  0.00%  0.00%   0 Tunnel FIB       
         262         185       16351         11  0.00%  0.00%  0.00%   0 CEF: IPv4 proces 
         263           9          68        132  0.00%  0.00%  0.00%   0 ADJ background   
         264       12855         523      24579  0.00%  0.00%  0.00%   0 Collection proce 
         265           0           3          0  0.00%  0.00%  0.00%   0 ADJ resolve proc 
         266           0          62          0  0.00%  0.00%  0.00%   0 Socket Timers    
         267        3096       75126         41  0.00%  0.00%  0.00%   0 TCP Timer        
         268           5          49        102  0.00%  0.00%  0.00%   0 TCP Protocols    
         269           0           1          0  0.00%  0.00%  0.00%   0 COPS             
         270          12        1097         10  0.00%  0.00%  0.00%   0 NGCP SCHEDULER P 
         271         178       32840          5  0.00%  0.00%  0.00%   0 STILE PERIODIC T 
         272           4         549          7  0.00%  0.00%  0.00%   0 UV AUTO CUSTOM P 
         273           0           2          0  0.00%  0.00%  0.00%   0 Dialer Forwarder 
         274           0           3          0  0.00%  0.00%  0.00%   0 Service Routing  
         275          32         196        163  0.00%  0.00%  0.00%   0 SR CapMan Proces 
         276           2         151         13  0.00%  0.00%  0.00%   0 Flow Exporter Ti 
         277           0           2          0  0.00%  0.00%  0.00%   0 Flow Exporter Pa 
         278           1         110          9  0.00%  0.00%  0.00%   0 HTTP CORE        
         279           0           1          0  0.00%  0.00%  0.00%   0 SBC Msg Ack Time 
         280           1         111          9  0.00%  0.00%  0.00%   0 MFIB Master back 
         281          21          51        411  0.00%  0.00%  0.00%   0 VFI Mgr          
         282          56         330        169  0.00%  0.00%  0.00%   0 MVPN Mgr Process 
         283           0           2          0  0.00%  0.00%  0.00%   0 Multicast Offloa 
         284           0           1          0  0.00%  0.00%  0.00%   0 RARP Input       
         285          12         128         93  0.00%  0.00%  0.00%   0 static           
         286           0           2          0  0.00%  0.00%  0.00%   0 App Route Proces 
         287           0           1          0  0.00%  0.00%  0.00%   0 IPv6 RIB Cleanup 
         288           0           3          0  0.00%  0.00%  0.00%   0 IPv6 RIB Event H 
         289           0           1          0  0.00%  0.00%  0.00%   0 IPv6 Static Hand 
         290           0           2          0  0.00%  0.00%  0.00%   0 DHCPv6 LQ client 
         291          68          12       5666  0.00%  0.00%  0.00%   0 AToM manager     
         292           0           2          0  0.00%  0.00%  0.00%   0 PPP NBF          
         293         209       32559          6  0.00%  0.00%  0.00%   0 PfR BR Learn     
         294           0           1          0  0.00%  0.00%  0.00%   0 PAD InCall       
         295           0           2          0  0.00%  0.00%  0.00%   0 X.25 Background  
         296           0           1          0  0.00%  0.00%  0.00%   0 X.25 Encaps Mana 
         297          82        3289         24  0.00%  0.00%  0.00%   0 QoS stats proces 
         298           0           2          0  0.00%  0.00%  0.00%   0 RBSCP Background 
         299           2           2       1000  0.00%  0.00%  0.00%   0 SCTP Main Proces 
         300           0           1          0  0.00%  0.00%  0.00%   0 VPDN call manage 
         301          95          15       6333  0.00%  0.00%  0.00%   0 XC RIB MGR       
         302           0           2          0  0.00%  0.00%  0.00%   0 AToM LDP manager 
         303           0           2          0  0.00%  0.00%  0.00%   0 EFP Errd         
         304           0           2          0  0.00%  0.00%  0.00%   0 Ether EFP Proces 
         305           0           2          0  0.00%  0.00%  0.00%   0 Ether Infra RP   
         306           0          18          0  0.00%  0.00%  0.00%   0 CFM HA IPC messa 
         307           0           1          0  0.00%  0.00%  0.00%   0 Ethernet PM Proc 
         308           0           2          0  0.00%  0.00%  0.00%   0 Ethernet PM Soft 
         309          83        9857          8  0.00%  0.00%  0.00%   0 Ethernet PM Moni 
         310           0           1          0  0.00%  0.00%  0.00%   0 Ethernet Datapla 
         311           0          18          0  0.00%  0.00%  0.00%   0 ELB HA IPC flow  
         312          31          42        738  0.00%  0.00%  0.00%   0 IGMPSN L2MCM     
         313           0           1          0  0.00%  0.00%  0.00%   0 IGMPSN MRD       
         314           0           1          0  0.00%  0.00%  0.00%   0 IGMPSN           
         315        4917      131016         37  0.00%  0.00%  0.00%   0 TCP HA PROC      
         316       49197        5076       9692  0.00%  0.00%  0.00%   0 BGP HA SSO       
         317           0           5          0  0.00%  0.00%  0.00%   0 RSVP SYNC        
         318           0           1          0  0.00%  0.00%  0.00%   0 RETRY_REPOPULATE 
         319           0           4          0  0.00%  0.00%  0.00%   0 XDR FOF process  
         320           0           2          0  0.00%  0.00%  0.00%   0 BD Route Msg Hol 
         321           0           1          0  0.00%  0.00%  0.00%   0 BD Route Rx Proc 
         322           0           3          0  0.00%  0.00%  0.00%   0 BD MACSEC HA     
         323           0           2          0  0.00%  0.00%  0.00%   0 BD MACSEC HA CHK 
         324         121         128        945  0.00%  0.00%  0.00%   0 L2FIB Event Disp 
         325           0          18          0  0.00%  0.00%  0.00%   0 STP HA IPC flow  
         326           0           1          0  0.00%  0.00%  0.00%   0 IGMPQR           
         327           0           4          0  0.00%  0.00%  0.00%   0 AAA HA           
         328           0           1          0  0.00%  0.00%  0.00%   0 AAA HA cleanup   
         329           0           1          0  0.00%  0.00%  0.00%   0 ac_atm_state_eve 
         330           0           1          0  0.00%  0.00%  0.00%   0 ac_atm_mraps_hsp 
         331           0           1          0  0.00%  0.00%  0.00%   0 AC HA Bulk Sync  
         332           0           2          0  0.00%  0.00%  0.00%   0 ATM HA           
         333           0          18          0  0.00%  0.00%  0.00%   0 ATM HA IPC flow  
         334           0           1          0  0.00%  0.00%  0.00%   0 ATM HA AC        
         335           0           2          0  0.00%  0.00%  0.00%   0 BFD HA           
         336           0           2          0  0.00%  0.00%  0.00%   0 FR HA            
         337           0          10          0  0.00%  0.00%  0.00%   0 GLBP HA          
         338           0          10          0  0.00%  0.00%  0.00%   0 HSRP HA          
         339         397       64077          6  0.00%  0.00%  0.00%   0 Inspect process  
         340        5548       76816         72  0.00%  0.00%  0.00%   0 BGP I/O          
         341          69        8026          8  0.00%  0.00%  0.00%   0 IP SIP Process   
         342           0           1          0  0.00%  0.00%  0.00%   0 MRIB RP Proxy    
         343           0           2          0  0.00%  0.00%  0.00%   0 IPv6 ACL RP Proc 
         344           0          18          0  0.00%  0.00%  0.00%   0 Netsync IPC flow 
         345           0           2          0  0.00%  0.00%  0.00%   0 PPPoE VRRS EVT M 
         346           0           1          0  0.00%  0.00%  0.00%   0 RG If-Mgr Timer  
         347           0           2          0  0.00%  0.00%  0.00%   0 RG Media Timer   
         348           1          13         76  0.00%  0.00%  0.00%   0 MCPRP RG Timer   
         349           0           2          0  0.00%  0.00%  0.00%   0 URL filter proc  
         350           0           5          0  0.00%  0.00%  0.00%   0 VFI HA Bulk Sync 
         351           0           3          0  0.00%  0.00%  0.00%   0 XC RIB HA Bulk S 
         352           0           4          0  0.00%  0.00%  0.00%   0 XC BGP SIG RIB H 
         353           0           1          0  0.00%  0.00%  0.00%   0 VPDN CCM Backgro 
         354           0          10          0  0.00%  0.00%  0.00%   0 VRRP HA          
         355           0          18          0  0.00%  0.00%  0.00%   0 VTEMPLATE IPC fl 
         356           1         187          5  0.00%  0.00%  0.00%   0 CEM PROC         
         357           0           2          0  0.00%  0.00%  0.00%   0 CEM HA           
         358           0           1          0  0.00%  0.00%  0.00%   0 CEM HA AC        
         359           0           2          0  0.00%  0.00%  0.00%   0 L2X Switching Ev 
         360           0           1          0  0.00%  0.00%  0.00%   0 Probe Input      
         361           1           2        500  0.00%  0.00%  0.00%   0 IP Inband Sessio 
         362           0           1          0  0.00%  0.00%  0.00%   0 DHCP SIP         
         363          77        8223          9  0.00%  0.00%  0.00%   0 FRR Manager      
         364           0           1          0  0.00%  0.00%  0.00%   0 MFI Comm RP Proc 
         365           0           1          0  0.00%  0.00%  0.00%   0 Path set broker  
         366           0           1          0  0.00%  0.00%  0.00%   0 LFD Label Block  
         367         439        5273         83  0.00%  0.00%  0.00%   0 LDP HA           
         368           0           3          0  0.00%  0.00%  0.00%   0 MPLS VPN HA Clie 
         369           0           7          0  0.00%  0.00%  0.00%   0 TSPTUN HA        
         370           0           2          0  0.00%  0.00%  0.00%   0 RSVP HA Services 
         371           0           2          0  0.00%  0.00%  0.00%   0 TE NSR OOS DB Pr 
         372           0          17          0  0.00%  0.00%  0.00%   0 MPLS TP HA       
         373           0           5          0  0.00%  0.00%  0.00%   0 AToM HA Bulk Syn 
         374           0          17          0  0.00%  0.00%  0.00%   0 AToM MGR HA IPC  
         375           2           2       1000  0.00%  0.00%  0.00%   0 LFDp Input Proc  
         376           0           2          0  0.00%  0.00%  0.00%   0 AAA Cached Serve 
         377           0           6          0  0.00%  0.00%  0.00%   0 ENABLE AAA       
         378           0           1          0  0.00%  0.00%  0.00%   0 EM Background Pr 
         379           0           3          0  0.00%  0.00%  0.00%   0 LDAP process     
         380           0           1          0  0.00%  0.00%  0.00%   0 Opaque Database  
         381           0           1          0  0.00%  0.00%  0.00%   0 Key chain liveke 
         382           0           2          0  0.00%  0.00%  0.00%   0 LINE AAA         
         383           0          17          0  0.00%  0.00%  0.00%   0 LOCAL AAA        
         384      278040        6202      44830  0.00%  0.44%  0.64%   0 BGP Scanner      
         385          20         472         42  0.00%  0.00%  0.00%   0 TPLUS            
         386           6         319         18  0.00%  0.00%  0.00%   0 DynCmd Package P 
         387        4924      510125          9  0.00%  0.01%  0.00%   0 MMA DB TIMER     
         388           0           2          0  0.00%  0.00%  0.00%   0 FLEX DSPRM MAIN  
         389           0           2          0  0.00%  0.00%  0.00%   0 VSP_MGR          
         390           1           2        500  0.00%  0.00%  0.00%   0 STUN_APP         
         391           0           1          0  0.00%  0.00%  0.00%   0 STUN_TEST        
         392           0           2          0  0.00%  0.00%  0.00%   0 Manet Infra Back 
         393           0           1          0  0.00%  0.00%  0.00%   0 IDMGR CORE       
         394         188       18101         10  0.00%  0.00%  0.00%   0 MPLS Auto Mesh P 
         395         678       32875         20  0.00%  0.00%  0.00%   0 RSCMSM VOLUME MO 
         396           0           1          0  0.00%  0.00%  0.00%   0 CCSIP_EVENT_TRAC 
         397           0           2          0  0.00%  0.00%  0.00%   0 Sip MPA          
         398           1           1       1000  0.00%  0.00%  0.00%   0 QOS_MODULE_MAIN  
         399           0           1          0  0.00%  0.00%  0.00%   0 IP TRUST Registe 
         400           0           1          0  0.00%  0.00%  0.00%   0 VoIP AAA         
         401           0          18          0  0.00%  0.00%  0.00%   0 COND_DEBUG HA IP 
         402           2          23         86  0.00%  0.00%  0.00%   0 PIM HA           
         403           0           2          0  0.00%  0.00%  0.00%   0 MMON PROCESS     
         404           0           1          0  0.00%  0.00%  0.00%   0 QOS PERUSER      
         405           0           1          0  0.00%  0.00%  0.00%   0 RPMS_PROC_MAIN   
         406           0           1          0  0.00%  0.00%  0.00%   0 http client proc 
         407         914       65763         13  0.00%  0.00%  0.00%   0 OSPF-65109 Router 
         408           0           2          0  0.00%  0.00%  0.00%   0 SEGMENT ROUTING  
         409           1          44         22  0.00%  0.00%  0.00%   0 AAA SEND STOP EV 
         410           0           1          0  0.00%  0.00%  0.00%   0 Test AAA Client  
         411           0           1          0  0.00%  0.00%  0.00%   0 dcm_cli_engine   
         412           1           3        333  0.00%  0.00%  0.00%   0 dcm_cli_provider 
         413           0           5          0  0.00%  0.00%  0.00%   0 DCM Core Thread  
         414          14         580         24  0.00%  0.00%  0.00%   0 EEM ED Syslog    
         415           1           4        250  0.00%  0.00%  0.00%   0 EEM ED Generic   
         416           1           4        250  0.00%  0.00%  0.00%   0 EEM ED Track     
         417           1           4        250  0.00%  0.00%  0.00%   0 EEM ED Routing   
         418           0           4          0  0.00%  0.00%  0.00%   0 EEM ED Resource  
         419           0           1          0  0.00%  0.00%  0.00%   0 Syslog Traps     
         420           0           1          0  0.00%  0.00%  0.00%   0 Policy HA Timer  
         421           0           1          0  0.00%  0.00%  0.00%   0 BGP Consistency  
         422           0           2          0  0.00%  0.00%  0.00%   0 ICRM             
         423           0           1          0  0.00%  0.00%  0.00%   0 Online Diag EEM  
         424        1362       10469        130  0.00%  0.00%  0.00%   0 SPA ENTITY Proce 
         425           0           1          0  0.00%  0.00%  0.00%   0 SONET Traps      
         426           0           2          0  0.00%  0.00%  0.00%   0 ISG MIB jobs Man 
         427           0           2          0  0.00%  0.00%  0.00%   0 SBC RF config sy 
         428           0           6          0  0.00%  0.00%  0.00%   0 DCM snmp dp Thre 
         429           0           3          0  0.00%  0.00%  0.00%   0 snmp dcm ma shim 
         430          50        3291         15  0.00%  0.00%  0.00%   0 Bulkstat-Client  
         431           0           3          0  0.00%  0.00%  0.00%   0 dcm_expression_p 
         432          12         510         23  0.00%  0.00%  0.00%   0 EEM Server       
         433           3          33         90  0.00%  0.00%  0.00%   0 Call Home proces 
         434           1           1       1000  0.00%  0.00%  0.00%   0 Call Home DS     
         435           0           1          0  0.00%  0.00%  0.00%   0 Call Home DSfile 
         436           1           3        333  0.00%  0.00%  0.00%   0 EEM Policy Direc 
         437          70        6580         10  0.00%  0.00%  0.00%   0 LSD Main Proc    
         438           0           4          0  0.00%  0.00%  0.00%   0 EEM ED CLI       
         439           0           4          0  0.00%  0.00%  0.00%   0 EEM ED Counter   
         440           0           4          0  0.00%  0.00%  0.00%   0 EEM ED Interface 
         441           0           4          0  0.00%  0.00%  0.00%   0 EEM ED IOSWD     
         442           0           4          0  0.00%  0.00%  0.00%   0 EEM ED None      
         443           0           4          0  0.00%  0.00%  0.00%   0 EEM ED OIR       
         444           0          16          0  0.00%  0.00%  0.00%   0 EEM ED RF        
         445        1455       32933         44  0.00%  0.00%  0.00%   0 EEM ED SNMP      
         446           0           4          0  0.00%  0.00%  0.00%   0 EEM ED SNMP Obje 
         447           0           4          0  0.00%  0.00%  0.00%   0 EEM ED SNMP Noti 
         448          11         555         19  0.00%  0.00%  0.00%   0 EEM ED Timer     
         449           0           4          0  0.00%  0.00%  0.00%   0 EEM ED Ipsla     
         450           1           4        250  0.00%  0.00%  0.00%   0 EEM ED Test      
         451           0           4          0  0.00%  0.00%  0.00%   0 EEM ED Config    
         452           0           4          0  0.00%  0.00%  0.00%   0 EEM ED Env       
         453           1           4        250  0.00%  0.00%  0.00%   0 EEM ED DS        
         454           0           4          0  0.00%  0.00%  0.00%   0 EEM ED CRASH     
         455           0           4          0  0.00%  0.00%  0.00%   0 EM ED GOLD       
         456          73         417        175  0.00%  0.00%  0.00%   0 Syslog           
         457       21526        3284       6554  0.07%  0.06%  0.05%   0 MFI LFD Stats Pr 
         458           0           1          0  0.00%  0.00%  0.00%   0 IP SLAs Ethernet 
         459          58        6579          8  0.00%  0.00%  0.00%   0 VDC process      
         460           0           1          0  0.00%  0.00%  0.00%   0 udp_transport Se 
         461          55        3290         16  0.00%  0.00%  0.00%   0 qos_mon_periodic 
         462           0           1          0  0.00%  0.00%  0.00%   0 ISSU Utility Pro 
         463           0           1          0  0.00%  0.00%  0.00%   0 IOSXE-RP Virtual 
         464           0           1          0  0.00%  0.00%  0.00%   0 Online Diag CNS  
         465           0           1          0  0.00%  0.00%  0.00%   0 Online Diag CNS  
         466           0           9          0  0.00%  0.00%  0.00%   0 MPLS IFMIB Proce 
         467           0           1          0  0.00%  0.00%  0.00%   0 IPC ISSU Version 
         468           0           1          0  0.00%  0.00%  0.00%   0 IPC ISSU Version 
         469           0           1          0  0.00%  0.00%  0.00%   0 IPC ISSU Version 
         470           0           1          0  0.00%  0.00%  0.00%   0 IPC ISSU Version 
         471           0           1          0  0.00%  0.00%  0.00%   0 IPC ISSU Version 
         472           0           1          0  0.00%  0.00%  0.00%   0 IPC ISSU Version 
         473           0           1          0  0.00%  0.00%  0.00%   0 IPC ISSU Version 
         474           0           1          0  0.00%  0.00%  0.00%   0 IPC ISSU Version 
         475           0           1          0  0.00%  0.00%  0.00%   0 IPC ISSU Version 
         476           0           1          0  0.00%  0.00%  0.00%   0 IPC ISSU Version 
         477           0           1          0  0.00%  0.00%  0.00%   0 IPC ISSU Version 
         478           0           1          0  0.00%  0.00%  0.00%   0 IPC ISSU Version 
         479           0           1          0  0.00%  0.00%  0.00%   0 IPC ISSU Version 
         480           0           1          0  0.00%  0.00%  0.00%   0 IPC ISSU Version 
         481           0           1          0  0.00%  0.00%  0.00%   0 MPLS TE OAM Clie 
         482           0           1          0  0.00%  0.00%  0.00%   0 IPC ISSU Version 
         483           0           1          0  0.00%  0.00%  0.00%   0 IPC ISSU Version 
         484           0           1          0  0.00%  0.00%  0.00%   0 IPC ISSU Version 
         485           0           1          0  0.00%  0.00%  0.00%   0 IPC ISSU Version 
         486           0           1          0  0.00%  0.00%  0.00%   0 IPC ISSU Version 
         487           1           1       1000  0.00%  0.00%  0.00%   0 IPC ISSU Version 
         488           0           1          0  0.00%  0.00%  0.00%   0 IPC ISSU Version 
         489           0           1          0  0.00%  0.00%  0.00%   0 IPC ISSU Version 
         490           0           1          0  0.00%  0.00%  0.00%   0 IPC ISSU Version 
         491           0           1          0  0.00%  0.00%  0.00%   0 IPC ISSU Version 
         492           0           1          0  0.00%  0.00%  0.00%   0 IPC ISSU Version 
         493           0           1          0  0.00%  0.00%  0.00%   0 IPC ISSU Version 
         494           0           1          0  0.00%  0.00%  0.00%   0 IPC ISSU Version 
         495           0           1          0  0.00%  0.00%  0.00%   0 IPC ISSU Version 
         496           0           1          0  0.00%  0.00%  0.00%   0 IPC ISSU Version 
         497         829       13140         63  0.00%  0.00%  0.00%   0 DiagCard1/-1     
         498           0           1          0  0.00%  0.00%  0.00%   0 IPC ISSU Version 
         499           0           1          0  0.00%  0.00%  0.00%   0 IPC ISSU Version 
         500           0           1          0  0.00%  0.00%  0.00%   0 IPC ISSU Version 
         501           0           1          0  0.00%  0.00%  0.00%   0 IPC ISSU Version 
         502           0           1          0  0.00%  0.00%  0.00%   0 IPC ISSU Version 
         503           0           1          0  0.00%  0.00%  0.00%   0 IPC ISSU Version 
         504           0           1          0  0.00%  0.00%  0.00%   0 IPC ISSU Version 
         505           0           1          0  0.00%  0.00%  0.00%   0 IPC ISSU Version 
         506           0           1          0  0.00%  0.00%  0.00%   0 IPC ISSU Version 
         507           0           1          0  0.00%  0.00%  0.00%   0 IPC ISSU Version 
         508           0           1          0  0.00%  0.00%  0.00%   0 IPC ISSU Version 
         509           0           1          0  0.00%  0.00%  0.00%   0 IPC ISSU Version 
         510           0           1          0  0.00%  0.00%  0.00%   0 IPC ISSU Version 
         511           0           1          0  0.00%  0.00%  0.00%   0 IPC ISSU Version 
         512           0           1          0  0.00%  0.00%  0.00%   0 IPC ISSU Version 
         513         252       13143         19  0.00%  0.00%  0.00%   0 DiagCard2/-1     
         514           0           1          0  0.00%  0.00%  0.00%   0 IPC ISSU Version 
         515           0           1          0  0.00%  0.00%  0.00%   0 IPC ISSU Version 
         516           0           1          0  0.00%  0.00%  0.00%   0 IPC ISSU Version 
         517           0           1          0  0.00%  0.00%  0.00%   0 IPC ISSU Version 
         518           0           1          0  0.00%  0.00%  0.00%   0 IPC ISSU Version 
         519           0           1          0  0.00%  0.00%  0.00%   0 IPC ISSU Version 
         520           0           1          0  0.00%  0.00%  0.00%   0 IPC ISSU Version 
         521           0           1          0  0.00%  0.00%  0.00%   0 IPC ISSU Version 
         522           0           1          0  0.00%  0.00%  0.00%   0 IPC ISSU Version 
         523           0           1          0  0.00%  0.00%  0.00%   0 IPC ISSU Version 
         524           0           1          0  0.00%  0.00%  0.00%   0 IPC ISSU Version 
         525           0           1          0  0.00%  0.00%  0.00%   0 IPC ISSU Version 
         526           0           1          0  0.00%  0.00%  0.00%   0 IPC ISSU Version 
         527           0           1          0  0.00%  0.00%  0.00%   0 IPC ISSU Version 
         528           0           1          0  0.00%  0.00%  0.00%   0 IPC ISSU Version 
         529           0           5          0  0.00%  0.00%  0.00%   0 CWAN OIR IPC Rea 
         530         261        2008        129  0.00%  0.00%  0.00%   0 mdns Timer Proce 
         531         977       65670         14  0.00%  0.00%  0.00%   0 SBC main process 
         532           0           2          0  0.00%  0.00%  0.00%   0 MRIB Process     
         533           8         560         14  0.00%  0.00%  0.00%   0 EEM Helper Threa 
         534          39        6209          6  0.00%  0.00%  0.00%   0 MFI LFD Timer Pr 
         535         354        4702         75  0.00%  0.00%  0.00%   0 LCON Main        
         536           1           4        250  0.00%  0.00%  0.00%   0 MFI LFD Main Pro 
         537           0           6          0  0.00%  0.00%  0.00%   0 Inter Chassis Pr 
         538           0           3          0  0.00%  0.00%  0.00%   0 DiagCard3/-1     
         539           0           3          0  0.00%  0.00%  0.00%   0 DiagCard4/-1     
         540         266         549        484  0.00%  0.00%  0.00%   0 LDP Background   
         541        1468      254919          5  0.00%  0.00%  0.00%   0 MCP RP EFP proce 
         542        9701         207      46864  0.00%  0.00%  0.00%   0 BGP Event        
         543         149        2902         51  0.00%  0.00%  0.00%   0 LDP Main         
         544         854       15020         56  0.00%  0.00%  0.00%   0 LDP Hello        
         545       13752        1320      10418  0.00%  0.00%  0.00%   0 BGP Task         
         546           0           1          0  0.00%  0.00%  0.00%   0 BGP BMP Server   
         547           0          93          0  0.00%  0.00%  0.00%   0 TCP Listener     
         548           2         551          3  0.00%  0.00%  0.00%   0 IPRM             
         549          36         673         53  0.00%  0.00%  0.00%   0 IP SNMP          
         550           0           1          0  0.00%  0.00%  0.00%   0 PDU DISPATCHER   
         551           1           4        250  0.00%  0.00%  0.00%   0 SNMP ENGINE      
         552           0           2          0  0.00%  0.00%  0.00%   0 IP SNMPV6        
         553           0           1          0  0.00%  0.00%  0.00%   0 SNMP ConfCopyPro 
         554         416         387       1074  0.00%  0.00%  0.00%   0 SNMP Traps       
         555         851       33806         25  0.00%  0.00%  0.00%   0 NTP              
         556           0           1          0  0.00%  0.00%  0.00%   0 EM Action CNS    
         557           0           2          0  0.00%  0.00%  0.00%   0 DiagCard5/-1     
         558      307942       78644       3915  0.55%  0.72%  0.73%   0 BGP Router       
         559         311       10680         29  0.00%  0.00%  0.00%   0 OSPF-65109 Hello  
         560           0           1          0  0.00%  0.00%  0.00%   0 BGP VA           
         561           0           1          0  0.00%  0.00%  0.00%   0 IFCOM Msg Hdlr   
         562           0           1          0  0.00%  0.00%  0.00%   0 IFCOM Msg Hdlr   
         563           0           1          0  0.00%  0.00%  0.00%   0 IFCOM Msg Hdlr   
         564           0           1          0  0.00%  0.00%  0.00%   0 IFCOM Msg Hdlr   
         565           0           1          0  0.00%  0.00%  0.00%   0 Network Synchron 
         566         862      127232          6  0.00%  0.00%  0.00%   0 CCM Subscriber P 
         567           0           4          0  0.00%  0.00%  0.00%   0 Process to do EH 
         568           0          11          0  0.00%  0.00%  0.00%   0 RFS server proce 
         569           0           2          0  0.00%  0.00%  0.00%   0 IP MPLS Service  
         570           0           1          0  0.00%  0.00%  0.00%   0 HA-IDB-SYNC      
         571           0           2          0  0.00%  0.00%  0.00%   0 VTEMPLATE Backgr 
         573        4487        9517        471  0.00%  0.28%  0.75%   2 Virtual Exec     
         574           4          15        266  0.00%  0.00%  0.00%   0 L2FIB HA Flow Th 
         575       66557       75795        878  0.00%  0.00%  0.00%   3 Virtual Exec     
         576       13105       19063        687  0.00%  0.00%  0.00%   4 Virtual Exec     
         577        4208         797       5279  0.00%  0.00%  0.00%   5 Virtual Exec     
         578          71         542        130  0.00%  0.00%  0.00%   6 Virtual Exec     
         606          17         448         37  0.00%  0.00%  0.00%   0 LCON Addr       

        This command only shows processes inside the IOS daemon.
        Please use 'show processes cpu platform'
        to show processes from the underlying operating system.
    '''
    }

    golden_parsed_output_1 = {'sort': {1: {'five_min_cpu': 0.0,
              'five_sec_cpu': 0.0,
              'invoked': 1,
              'one_min_cpu': 0.0,
              'pid': 100,
              'process': 'cpf_process_tpQ',
              'runtime': 0,
              'tty': 0,
              'usecs': 0},
          2: {'five_min_cpu': 0.0,
              'five_sec_cpu': 0.0,
              'invoked': 1,
              'one_min_cpu': 0.0,
              'pid': 189,
              'process': 'ADJ NSF process',
              'runtime': 0,
              'tty': 0,
              'usecs': 0},
          3: {'five_min_cpu': 0.0,
              'five_sec_cpu': 0.0,
              'invoked': 365006,
              'one_min_cpu': 0.0,
              'pid': 244,
              'process': 'cdp init process',
              'runtime': 2930,
              'tty': 0,
              'usecs': 8},
          4: {'five_min_cpu': 0.0,
              'five_sec_cpu': 0.0,
              'invoked': 2,
              'one_min_cpu': 0.0,
              'pid': 309,
              'process': 'XDR FOF process',
              'runtime': 0,
              'tty': 0,
              'usecs': 0},
          5: {'five_min_cpu': 0.0,
              'five_sec_cpu': 0.0,
              'invoked': 712805,
              'one_min_cpu': 0.0,
              'pid': 355,
              'process': 'Inspect process',
              'runtime': 9385,
              'tty': 0,
              'usecs': 13},
          6: {'five_min_cpu': 0.0,
              'five_sec_cpu': 0.0,
              'invoked': 3,
              'one_min_cpu': 0.0,
              'pid': 429,
              'process': 'LDAP process',
              'runtime': 0,
              'tty': 0,
              'usecs': 0},
          7: {'five_min_cpu': 0.0,
              'five_sec_cpu': 0.0,
              'invoked': 73010,
              'one_min_cpu': 0.0,
              'pid': 547,
              'process': 'VDC process',
              'runtime': 592,
              'tty': 0,
              'usecs': 8},
          8: {'five_min_cpu': 0.0,
              'five_sec_cpu': 0.0,
              'invoked': 730005,
              'one_min_cpu': 0.0,
              'pid': 615,
              'process': 'SBC main process',
              'runtime': 19084,
              'tty': 0,
              'usecs': 26}},
 'zero_cpu_processes': ['cpf_process_tpQ',
                        'ADJ NSF process',
                        'cdp init process',
                        'XDR FOF process',
                        'Inspect process',
                        'LDAP process',
                        'VDC process',
                        'SBC main process']}

    golden_output_1 = {'execute.return_value': '''
        PE1#show processes cpu | include process
         100           0           1          0  0.00%  0.00%  0.00%   0 cpf_process_tpQ  
         189           0           1          0  0.00%  0.00%  0.00%   0 ADJ NSF process  
         244        2930      365006          8  0.00%  0.00%  0.00%   0 cdp init process 
         309           0           2          0  0.00%  0.00%  0.00%   0 XDR FOF process  
         355        9385      712805         13  0.00%  0.00%  0.00%   0 Inspect process  
         429           0           3          0  0.00%  0.00%  0.00%   0 LDAP process     
         547         592       73010          8  0.00%  0.00%  0.00%   0 VDC process      
         615       19084      730005         26  0.00%  0.00%  0.00%   0 SBC main process
    '''}

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowProcessesCpu(device=self.device)
        parsed_output = obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)

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


class TestShowVersionRp(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output_active = {
        'rp': {
            'active': {
                'slot': {
                    'ESP0': {
                        'package': {
                            'espx86base': {
                                'built_by': 'mcpre',
                                'built_time': '2016-10-04_12.28',
                                'file': 'asr1000rp2-espx86base.03.16.04a.S.155-3.S4a-ext.pkg',
                                'file_sha1_checksum': 'e9401142366cf5c9fdeb2e570eae233d1a211803',
                                'status': 'active',
                                'version': '03.16.04a.S.155-3.S4a-ext',
                            }
                        }
                    },
                    'ESP1': {
                        'package': {
                            'espx86base': {'built_by': 'mcpre',
                                                                'built_time': '2016-10-04_12.28',
                                                                'file': 'asr1000rp2-espx86base.03.16.04a.S.155-3.S4a-ext.pkg',
                                                                'file_sha1_checksum': 'e9401142366cf5c9fdeb2e570eae233d1a211803',
                                                                'status': 'active',
                                                                'version': '03.16.04a.S.155-3.S4a-ext'}}},
                            'RP0': {'package': {'Provisioning File': {'built_by': 'n/a',
                                                                      'built_time': 'n/a',
                                                                      'file': 'packages.conf',
                                                                      'file_sha1_checksum': 'e9cc713ad9eacbdc1ac59d598a99cd1755351d44',
                                                                      'status': 'active',
                                                                      'version': 'n/a'},
                                                'rpbase': {'built_by': 'mcpre',
                                                           'built_time': '2016-10-04_12.28',
                                                           'file': 'asr1000rp2-rpbase.03.16.04a.S.155-3.S4a-ext.pkg',
                                                           'file_sha1_checksum': '79e234871520fd480dc1128058160b4e2acee9f7',
                                                           'status': 'n/a',
                                                           'version': '03.16.04a.S.155-3.S4a-ext'}}},
                            'RP0/0': {'package': {'rpaccess': {'built_by': 'mcpre',
                                                               'built_time': '2016-10-04_12.28',
                                                               'file': 'asr1000rp2-rpaccess.03.16.04a.S.155-3.S4a-ext.pkg',
                                                               'file_sha1_checksum': '7ae3f198743db3011eaeb9311d0b26bdf0e41f09',
                                                               'status': 'n/a',
                                                               'version': '03.16.04a.S.155-3.S4a-ext'},
                                                  'rpcontrol': {'built_by': 'mcpre',
                                                                'built_time': '2016-10-04_12.31',
                                                                'file': 'asr1000rp2-rpios-adventerprise.03.16.04a.S.155-3.S4a-ext.pkg',
                                                                'file_sha1_checksum': 'ead482a384b287a9a518d6514a495546cdbf7e85',
                                                                'status': 'n/a',
                                                                'version': '03.16.04a.S.155-3.S4a-ext'}}},
                            'RP1': {'package': {'rpbase': {'built_by': 'mcpre',
                                                           'built_time': '2016-10-04_12.28',
                                                           'file': 'asr1000rp2-rpbase.03.16.04a.S.155-3.S4a-ext.pkg',
                                                           'file_sha1_checksum': '79e234871520fd480dc1128058160b4e2acee9f7',
                                                           'status': 'active',
                                                           'version': '03.16.04a.S.155-3.S4a-ext'}}},
                            'RP1/0': {'package': {'rpaccess': {'built_by': 'mcpre',
                                                               'built_time': '2016-10-04_12.28',
                                                               'file': 'asr1000rp2-rpaccess.03.16.04a.S.155-3.S4a-ext.pkg',
                                                               'file_sha1_checksum': '7ae3f198743db3011eaeb9311d0b26bdf0e41f09',
                                                               'status': 'active',
                                                               'version': '03.16.04a.S.155-3.S4a-ext'},
                                                  'rpcontrol': {'built_by': 'mcpre',
                                                                'built_time': '2016-10-04_12.31',
                                                                'file': 'asr1000rp2-rpios-adventerprise.03.16.04a.S.155-3.S4a-ext.pkg',
                                                                'file_sha1_checksum': 'ead482a384b287a9a518d6514a495546cdbf7e85',
                                                                'status': 'active',
                                                                'version': '03.16.04a.S.155-3.S4a-ext'}}},
                            'SIP0': {'package': {'sipbase': {'built_by': 'mcpre',
                                                             'built_time': '2016-10-04_09.39',
                                                             'file': 'asr1000rp2-sipbase.03.16.04a.S.155-3.S4a-ext.pkg',
                                                             'file_sha1_checksum': '39f3451d1e4d84297ba6c696c450c2d8fed22fb7',
                                                             'status': 'active',
                                                             'version': '03.16.04a.S.155-3.S4a-ext'}}},
                            'SIP0/0': {'package': {'sipspa': {'built_by': 'mcpre',
                                                              'built_time': '2016-10-04_09.39',
                                                              'file': 'asr1000rp2-sipspa.03.16.04a.S.155-3.S4a-ext.pkg',
                                                              'file_sha1_checksum': 'bcd8cb438dd1829f31e361bd35287c392e641490',
                                                              'status': 'active',
                                                              'version': '03.16.04a.S.155-3.S4a-ext'}}},
                            'SIP0/1': {'package': {'sipspa': {'built_by': 'mcpre',
                                                              'built_time': '2016-10-04_09.39',
                                                              'file': 'asr1000rp2-sipspa.03.16.04a.S.155-3.S4a-ext.pkg',
                                                              'file_sha1_checksum': 'bcd8cb438dd1829f31e361bd35287c392e641490',
                                                              'status': 'active',
                                                              'version': '03.16.04a.S.155-3.S4a-ext'}}},
                            'SIP0/2': {'package': {'sipspa': {'built_by': 'mcpre',
                                                              'built_time': '2016-10-04_09.39',
                                                              'file': 'asr1000rp2-sipspa.03.16.04a.S.155-3.S4a-ext.pkg',
                                                              'file_sha1_checksum': 'bcd8cb438dd1829f31e361bd35287c392e641490',
                                                              'status': 'active',
                                                              'version': '03.16.04a.S.155-3.S4a-ext'}}},
                            'SIP0/3': {'package': {'sipspa': {'built_by': 'mcpre',
                                                              'built_time': '2016-10-04_09.39',
                                                              'file': 'asr1000rp2-sipspa.03.16.04a.S.155-3.S4a-ext.pkg',
                                                              'file_sha1_checksum': 'bcd8cb438dd1829f31e361bd35287c392e641490',
                                                              'status': 'active',
                                                              'version': '03.16.04a.S.155-3.S4a-ext'}}},
                            'SIP1': {'package': {'sipbase': {'built_by': 'mcpre',
                                                             'built_time': '2016-10-04_09.39',
                                                             'file': 'asr1000rp2-sipbase.03.16.04a.S.155-3.S4a-ext.pkg',
                                                             'file_sha1_checksum': '39f3451d1e4d84297ba6c696c450c2d8fed22fb7',
                                                             'status': 'active',
                                                             'version': '03.16.04a.S.155-3.S4a-ext'}}},
                            'SIP1/0': {'package': {'sipspa': {'built_by': 'mcpre',
                                                              'built_time': '2016-10-04_09.39',
                                                              'file': 'asr1000rp2-sipspa.03.16.04a.S.155-3.S4a-ext.pkg',
                                                              'file_sha1_checksum': 'bcd8cb438dd1829f31e361bd35287c392e641490',
                                                              'status': 'active',
                                                              'version': '03.16.04a.S.155-3.S4a-ext'}}},
                            'SIP1/1': {'package': {'sipspa': {'built_by': 'mcpre',
                                                              'built_time': '2016-10-04_09.39',
                                                              'file': 'asr1000rp2-sipspa.03.16.04a.S.155-3.S4a-ext.pkg',
                                                              'file_sha1_checksum': 'bcd8cb438dd1829f31e361bd35287c392e641490',
                                                              'status': 'active',
                                                              'version': '03.16.04a.S.155-3.S4a-ext'}}}}}}}

    golden_output_active = {'execute.return_value': '''\
        Router#show version RP active running
        Load for five secs: 1%/0%; one minute: 28%; five minutes: 44%
        Time source is NTP, 18:31:35.860 EST Mon Oct 24 2016
        Package: Provisioning File, version: n/a, status: active
          File: consolidated:packages.conf, on: RP0
          Built: n/a, by: n/a
          File SHA1 checksum: e9cc713ad9eacbdc1ac59d598a99cd1755351d44

        Package: rpbase, version: 03.16.04a.S.155-3.S4a-ext, status: n/a
          File: consolidated:asr1000rp2-rpbase.03.16.04a.S.155-3.S4a-ext.pkg, on: RP0
          Built: 2016-10-04_12.28, by: mcpre
          File SHA1 checksum: 79e234871520fd480dc1128058160b4e2acee9f7

        Package: rpcontrol, version: 03.16.04a.S.155-3.S4a-ext, status: n/a
          File: consolidated:asr1000rp2-rpcontrol.03.16.04a.S.155-3.S4a-ext.pkg, on: RP0/0
          Built: 2016-10-04_12.28, by: mcpre
          File SHA1 checksum: 16c8c12376cc94bdd9442fe64c429bdb034cd224

        Package: rpios-adventerprise, version: 03.16.04a.S.155-3.S4a-ext, status: n/a
          File: consolidated:asr1000rp2-rpios-adventerprise.03.16.04a.S.155-3.S4a-ext.pkg, on: RP0/0
          Built: 2016-10-04_12.31, by: mcpre
          File SHA1 checksum: ead482a384b287a9a518d6514a495546cdbf7e85

        Package: rpaccess, version: 03.16.04a.S.155-3.S4a-ext, status: n/a
          File: consolidated:asr1000rp2-rpaccess.03.16.04a.S.155-3.S4a-ext.pkg, on: RP0/0
          Built: 2016-10-04_12.28, by: mcpre
          File SHA1 checksum: 7ae3f198743db3011eaeb9311d0b26bdf0e41f09

        Package: rpbase, version: 03.16.04a.S.155-3.S4a-ext, status: active
          File: consolidated:asr1000rp2-rpbase.03.16.04a.S.155-3.S4a-ext.pkg, on: RP1
          Built: 2016-10-04_12.28, by: mcpre
          File SHA1 checksum: 79e234871520fd480dc1128058160b4e2acee9f7

        Package: rpcontrol, version: 03.16.04a.S.155-3.S4a-ext, status: active
          File: consolidated:asr1000rp2-rpcontrol.03.16.04a.S.155-3.S4a-ext.pkg, on: RP1/0
          Built: 2016-10-04_12.28, by: mcpre
          File SHA1 checksum: 16c8c12376cc94bdd9442fe64c429bdb034cd224

        Package: rpios-adventerprise, version: 03.16.04a.S.155-3.S4a-ext, status: active
          File: consolidated:asr1000rp2-rpios-adventerprise.03.16.04a.S.155-3.S4a-ext.pkg, on: RP1/0
          Built: 2016-10-04_12.31, by: mcpre
          File SHA1 checksum: ead482a384b287a9a518d6514a495546cdbf7e85

        Package: rpaccess, version: 03.16.04a.S.155-3.S4a-ext, status: active
          File: consolidated:asr1000rp2-rpaccess.03.16.04a.S.155-3.S4a-ext.pkg, on: RP1/0
          Built: 2016-10-04_12.28, by: mcpre
          File SHA1 checksum: 7ae3f198743db3011eaeb9311d0b26bdf0e41f09

        Package: espx86base, version: 03.16.04a.S.155-3.S4a-ext, status: active
          File: consolidated:asr1000rp2-espx86base.03.16.04a.S.155-3.S4a-ext.pkg, on: ESP0
          Built: 2016-10-04_12.28, by: mcpre
          File SHA1 checksum: e9401142366cf5c9fdeb2e570eae233d1a211803

        Package: espx86base, version: 03.16.04a.S.155-3.S4a-ext, status: active
          File: consolidated:asr1000rp2-espx86base.03.16.04a.S.155-3.S4a-ext.pkg, on: ESP1
          Built: 2016-10-04_12.28, by: mcpre
          File SHA1 checksum: e9401142366cf5c9fdeb2e570eae233d1a211803

        Package: sipbase, version: 03.16.04a.S.155-3.S4a-ext, status: active
          File: consolidated:asr1000rp2-sipbase.03.16.04a.S.155-3.S4a-ext.pkg, on: SIP0
          Built: 2016-10-04_09.39, by: mcpre
          File SHA1 checksum: 39f3451d1e4d84297ba6c696c450c2d8fed22fb7

        Package: sipspa, version: 03.16.04a.S.155-3.S4a-ext, status: active
          File: consolidated:asr1000rp2-sipspa.03.16.04a.S.155-3.S4a-ext.pkg, on: SIP0/0
          Built: 2016-10-04_09.39, by: mcpre
          File SHA1 checksum: bcd8cb438dd1829f31e361bd35287c392e641490

        Package: sipspa, version: 03.16.04a.S.155-3.S4a-ext, status: active
          File: consolidated:asr1000rp2-sipspa.03.16.04a.S.155-3.S4a-ext.pkg, on: SIP0/1
          Built: 2016-10-04_09.39, by: mcpre
          File SHA1 checksum: bcd8cb438dd1829f31e361bd35287c392e641490

        Package: sipspa, version: 03.16.04a.S.155-3.S4a-ext, status: active
          File: consolidated:asr1000rp2-sipspa.03.16.04a.S.155-3.S4a-ext.pkg, on: SIP0/2
          Built: 2016-10-04_09.39, by: mcpre
          File SHA1 checksum: bcd8cb438dd1829f31e361bd35287c392e641490

        Package: sipspa, version: 03.16.04a.S.155-3.S4a-ext, status: active
          File: consolidated:asr1000rp2-sipspa.03.16.04a.S.155-3.S4a-ext.pkg, on: SIP0/3
          Built: 2016-10-04_09.39, by: mcpre
          File SHA1 checksum: bcd8cb438dd1829f31e361bd35287c392e641490

        Package: sipbase, version: 03.16.04a.S.155-3.S4a-ext, status: active
          File: consolidated:asr1000rp2-sipbase.03.16.04a.S.155-3.S4a-ext.pkg, on: SIP1
          Built: 2016-10-04_09.39, by: mcpre
          File SHA1 checksum: 39f3451d1e4d84297ba6c696c450c2d8fed22fb7

        Package: sipspa, version: 03.16.04a.S.155-3.S4a-ext, status: active
          File: consolidated:asr1000rp2-sipspa.03.16.04a.S.155-3.S4a-ext.pkg, on: SIP1/0
          Built: 2016-10-04_09.39, by: mcpre
          File SHA1 checksum: bcd8cb438dd1829f31e361bd35287c392e641490

        Package: sipspa, version: 03.16.04a.S.155-3.S4a-ext, status: active
          File: consolidated:asr1000rp2-sipspa.03.16.04a.S.155-3.S4a-ext.pkg, on: SIP1/1
          Built: 2016-10-04_09.39, by: mcpre
          File SHA1 checksum: bcd8cb438dd1829f31e361bd35287c392e641490
    '''
    }

    golden_parsed_output_standby = {
        'rp': {
            'standby': {
                'slot': {
                    'ESP0': {
                        'package': {
                            'espbase': {
                                'built_by': 'mcpre',
                                'built_time': '2016-06-10_03.48',
                                'file': 'asr1000rp2-espbase.03.16.03.S.155-3.S3-ext.pkg',
                                'file_sha1_checksum': '4699d60fdb5fad4cc56927917309de4a4027e4e5',
                                'status': 'n/a',
                                'version': '03.16.03.S.155-3.S3-ext',
                            },
                            'espx86base': {
                                'built_by': 'mcpre',
                                'built_time': '2016-06-10_04.41',
                                'file': 'asr1000rp2-espx86base.03.16.03.S.155-3.S3-ext.pkg',
                                'file_sha1_checksum': '1d7393ac1fc1569797e62b8ce3bf5b3354ba3572',
                                'status': 'n/a',
                                'version': '03.16.03.S.155-3.S3-ext',
                            }
                        }
                    },
                    'ESP1': {
                        'package': {'espbase': {'built_by': 'mcpre',
                                                              'built_time': '2016-06-10_03.48',
                                                              'file': 'asr1000rp2-espbase.03.16.03.S.155-3.S3-ext.pkg',
                                                              'file_sha1_checksum': '4699d60fdb5fad4cc56927917309de4a4027e4e5',
                                                              'status': 'n/a',
                                                              'version': '03.16.03.S.155-3.S3-ext'},
                                                  'espx86base': {'built_by': 'mcpre',
                                                                 'built_time': '2016-06-10_04.41',
                                                                 'file': 'asr1000rp2-espx86base.03.16.03.S.155-3.S3-ext.pkg',
                                                                 'file_sha1_checksum': '1d7393ac1fc1569797e62b8ce3bf5b3354ba3572',
                                                                 'status': 'n/a',
                                                                 'version': '03.16.03.S.155-3.S3-ext'}}},
                             'RP0': {'package': {'Provisioning File': {'built_by': 'n/a',
                                                                       'built_time': 'n/a',
                                                                       'file': 'packages.conf',
                                                                       'file_sha1_checksum': '7055efa3e5674ba91b149dd669ff26bf6c375648',
                                                                       'status': 'active',
                                                                       'version': 'n/a'},
                                                 'rpbase': {'built_by': 'mcpre',
                                                            'built_time': '2016-06-10_04.41',
                                                            'file': 'asr1000rp2-rpbase.03.16.03.S.155-3.S3-ext.pkg',
                                                            'file_sha1_checksum': '8539d83af5a332779fe9424d7cb08061258c1af9',
                                                            'status': 'active',
                                                            'version': '03.16.03.S.155-3.S3-ext'}}},
                             'RP0/0': {'package': {'rpaccess': {'built_by': 'mcpre',
                                                                'built_time': '2016-06-10_04.41',
                                                                'file': 'asr1000rp2-rpaccess.03.16.03.S.155-3.S3-ext.pkg',
                                                                'file_sha1_checksum': '32547e24130869ad9985aca9370a0d7214d256e9',
                                                                'status': 'active',
                                                                'version': '03.16.03.S.155-3.S3-ext'},
                                                   'rpcontrol': {'built_by': 'mcpre',
                                                                 'built_time': '2016-06-10_04.43',
                                                                 'file': 'asr1000rp2-rpios-adventerprise.03.16.03.S.155-3.S3-ext.pkg',
                                                                 'file_sha1_checksum': '095f51f1d35ab539f6b26773c9413a41f918ad42',
                                                                 'status': 'active',
                                                                 'version': '03.16.03.S.155-3.S3-ext'}}},
                             'RP1': {'package': {'rpbase': {'built_by': 'mcpre',
                                                            'built_time': '2016-06-10_04.41',
                                                            'file': 'asr1000rp2-rpbase.03.16.03.S.155-3.S3-ext.pkg',
                                                            'file_sha1_checksum': '8539d83af5a332779fe9424d7cb08061258c1af9',
                                                            'status': 'n/a',
                                                            'version': '03.16.03.S.155-3.S3-ext'}}},
                             'RP1/0': {'package': {'rpaccess': {'built_by': 'mcpre',
                                                                'built_time': '2016-06-10_04.41',
                                                                'file': 'asr1000rp2-rpaccess.03.16.03.S.155-3.S3-ext.pkg',
                                                                'file_sha1_checksum': '32547e24130869ad9985aca9370a0d7214d256e9',
                                                                'status': 'n/a',
                                                                'version': '03.16.03.S.155-3.S3-ext'},
                                                   'rpcontrol': {'built_by': 'mcpre',
                                                                 'built_time': '2016-06-10_04.43',
                                                                 'file': 'asr1000rp2-rpios-adventerprise.03.16.03.S.155-3.S3-ext.pkg',
                                                                 'file_sha1_checksum': '095f51f1d35ab539f6b26773c9413a41f918ad42',
                                                                 'status': 'n/a',
                                                                 'version': '03.16.03.S.155-3.S3-ext'}}},
                             'SIP0': {'package': {'elcbase': {'built_by': 'mcpre',
                                                              'built_time': '2016-06-10_03.48',
                                                              'file': 'asr1000rp2-elcbase.03.16.03.S.155-3.S3-ext.pkg',
                                                              'file_sha1_checksum': 'e4573bf9a752b31a0c2d713990ad13e11b9b3387',
                                                              'status': 'n/a',
                                                              'version': '03.16.03.S.155-3.S3-ext'},
                                                  'sipbase': {'built_by': 'mcpre',
                                                              'built_time': '2016-06-10_03.48',
                                                              'file': 'asr1000rp2-sipbase.03.16.03.S.155-3.S3-ext.pkg',
                                                              'file_sha1_checksum': 'db8fb38d845c23b0e0f74b05f1a86aadcaa34972',
                                                              'status': 'n/a',
                                                              'version': '03.16.03.S.155-3.S3-ext'}}},
                             'SIP0/0': {'package': {'elcspa': {'built_by': 'mcpre',
                                                               'built_time': '2016-06-10_03.48',
                                                               'file': 'asr1000rp2-elcspa.03.16.03.S.155-3.S3-ext.pkg',
                                                               'file_sha1_checksum': 'a912595d72b5be9890810042ec2a529d5d9a18b7',
                                                               'status': 'n/a',
                                                               'version': '03.16.03.S.155-3.S3-ext'},
                                                    'sipspa': {'built_by': 'mcpre',
                                                               'built_time': '2016-06-10_03.48',
                                                               'file': 'asr1000rp2-sipspa.03.16.03.S.155-3.S3-ext.pkg',
                                                               'file_sha1_checksum': 'bab5367d34c07e1522c102a95b4bfa3b099a3e0e',
                                                               'status': 'n/a',
                                                               'version': '03.16.03.S.155-3.S3-ext'}}},
                             'SIP0/1': {'package': {'elcspa': {'built_by': 'mcpre',
                                                               'built_time': '2016-06-10_03.48',
                                                               'file': 'asr1000rp2-elcspa.03.16.03.S.155-3.S3-ext.pkg',
                                                               'file_sha1_checksum': 'a912595d72b5be9890810042ec2a529d5d9a18b7',
                                                               'status': 'n/a',
                                                               'version': '03.16.03.S.155-3.S3-ext'},
                                                    'sipspa': {'built_by': 'mcpre',
                                                               'built_time': '2016-06-10_03.48',
                                                               'file': 'asr1000rp2-sipspa.03.16.03.S.155-3.S3-ext.pkg',
                                                               'file_sha1_checksum': 'bab5367d34c07e1522c102a95b4bfa3b099a3e0e',
                                                               'status': 'n/a',
                                                               'version': '03.16.03.S.155-3.S3-ext'}}},
                             'SIP0/2': {'package': {'elcspa': {'built_by': 'mcpre',
                                                               'built_time': '2016-06-10_03.48',
                                                               'file': 'asr1000rp2-elcspa.03.16.03.S.155-3.S3-ext.pkg',
                                                               'file_sha1_checksum': 'a912595d72b5be9890810042ec2a529d5d9a18b7',
                                                               'status': 'n/a',
                                                               'version': '03.16.03.S.155-3.S3-ext'},
                                                    'sipspa': {'built_by': 'mcpre',
                                                               'built_time': '2016-06-10_03.48',
                                                               'file': 'asr1000rp2-sipspa.03.16.03.S.155-3.S3-ext.pkg',
                                                               'file_sha1_checksum': 'bab5367d34c07e1522c102a95b4bfa3b099a3e0e',
                                                               'status': 'n/a',
                                                               'version': '03.16.03.S.155-3.S3-ext'}}},
                             'SIP0/3': {'package': {'elcspa': {'built_by': 'mcpre',
                                                               'built_time': '2016-06-10_03.48',
                                                               'file': 'asr1000rp2-elcspa.03.16.03.S.155-3.S3-ext.pkg',
                                                               'file_sha1_checksum': 'a912595d72b5be9890810042ec2a529d5d9a18b7',
                                                               'status': 'n/a',
                                                               'version': '03.16.03.S.155-3.S3-ext'},
                                                    'sipspa': {'built_by': 'mcpre',
                                                               'built_time': '2016-06-10_03.48',
                                                               'file': 'asr1000rp2-sipspa.03.16.03.S.155-3.S3-ext.pkg',
                                                               'file_sha1_checksum': 'bab5367d34c07e1522c102a95b4bfa3b099a3e0e',
                                                               'status': 'n/a',
                                                               'version': '03.16.03.S.155-3.S3-ext'}}},
                             'SIP1': {'package': {'elcbase': {'built_by': 'mcpre',
                                                              'built_time': '2016-06-10_03.48',
                                                              'file': 'asr1000rp2-elcbase.03.16.03.S.155-3.S3-ext.pkg',
                                                              'file_sha1_checksum': 'e4573bf9a752b31a0c2d713990ad13e11b9b3387',
                                                              'status': 'n/a',
                                                              'version': '03.16.03.S.155-3.S3-ext'},
                                                  'sipbase': {'built_by': 'mcpre',
                                                              'built_time': '2016-06-10_03.48',
                                                              'file': 'asr1000rp2-sipbase.03.16.03.S.155-3.S3-ext.pkg',
                                                              'file_sha1_checksum': 'db8fb38d845c23b0e0f74b05f1a86aadcaa34972',
                                                              'status': 'n/a',
                                                              'version': '03.16.03.S.155-3.S3-ext'}}},
                             'SIP1/0': {'package': {'elcspa': {'built_by': 'mcpre',
                                                               'built_time': '2016-06-10_03.48',
                                                               'file': 'asr1000rp2-elcspa.03.16.03.S.155-3.S3-ext.pkg',
                                                               'file_sha1_checksum': 'a912595d72b5be9890810042ec2a529d5d9a18b7',
                                                               'status': 'n/a',
                                                               'version': '03.16.03.S.155-3.S3-ext'},
                                                    'sipspa': {'built_by': 'mcpre',
                                                               'built_time': '2016-06-10_03.48',
                                                               'file': 'asr1000rp2-sipspa.03.16.03.S.155-3.S3-ext.pkg',
                                                               'file_sha1_checksum': 'bab5367d34c07e1522c102a95b4bfa3b099a3e0e',
                                                               'status': 'n/a',
                                                               'version': '03.16.03.S.155-3.S3-ext'}}},
                             'SIP1/1': {'package': {'elcspa': {'built_by': 'mcpre',
                                                               'built_time': '2016-06-10_03.48',
                                                               'file': 'asr1000rp2-elcspa.03.16.03.S.155-3.S3-ext.pkg',
                                                               'file_sha1_checksum': 'a912595d72b5be9890810042ec2a529d5d9a18b7',
                                                               'status': 'n/a',
                                                               'version': '03.16.03.S.155-3.S3-ext'},
                                                    'sipspa': {'built_by': 'mcpre',
                                                               'built_time': '2016-06-10_03.48',
                                                               'file': 'asr1000rp2-sipspa.03.16.03.S.155-3.S3-ext.pkg',
                                                               'file_sha1_checksum': 'bab5367d34c07e1522c102a95b4bfa3b099a3e0e',
                                                               'status': 'n/a',
                                                               'version': '03.16.03.S.155-3.S3-ext'}}}}}}}

    golden_output_standby = {'execute.return_value': '''\
        Router#show version RP standby running
        Load for five secs: 22%/0%; one minute: 18%; five minutes: 45%
        Time source is NTP, 18:37:42.222 EST Mon Oct 24 2016
        Package: Provisioning File, version: n/a, status: active
          File: consolidated:packages.conf, on: RP0
          Built: n/a, by: n/a
          File SHA1 checksum: 7055efa3e5674ba91b149dd669ff26bf6c375648

        Package: rpbase, version: 03.16.03.S.155-3.S3-ext, status: active
          File: consolidated:asr1000rp2-rpbase.03.16.03.S.155-3.S3-ext.pkg, on: RP0
          Built: 2016-06-10_04.41, by: mcpre
          File SHA1 checksum: 8539d83af5a332779fe9424d7cb08061258c1af9

        Package: rpcontrol, version: 03.16.03.S.155-3.S3-ext, status: active
          File: consolidated:asr1000rp2-rpcontrol.03.16.03.S.155-3.S3-ext.pkg, on: RP0/0
          Built: 2016-06-10_04.41, by: mcpre
          File SHA1 checksum: 4c6e5a1b052aadb2665ddb6f869e823970f9d4ee

        Package: rpios-adventerprise, version: 03.16.03.S.155-3.S3-ext, status: active
          File: consolidated:asr1000rp2-rpios-adventerprise.03.16.03.S.155-3.S3-ext.pkg, on: RP0/0
          Built: 2016-06-10_04.43, by: mcpre
          File SHA1 checksum: 095f51f1d35ab539f6b26773c9413a41f918ad42

        Package: rpaccess, version: 03.16.03.S.155-3.S3-ext, status: active
          File: consolidated:asr1000rp2-rpaccess.03.16.03.S.155-3.S3-ext.pkg, on: RP0/0
          Built: 2016-06-10_04.41, by: mcpre
          File SHA1 checksum: 32547e24130869ad9985aca9370a0d7214d256e9

        Package: rpbase, version: 03.16.03.S.155-3.S3-ext, status: n/a
          File: consolidated:asr1000rp2-rpbase.03.16.03.S.155-3.S3-ext.pkg, on: RP1
          Built: 2016-06-10_04.41, by: mcpre
          File SHA1 checksum: 8539d83af5a332779fe9424d7cb08061258c1af9

        Package: rpcontrol, version: 03.16.03.S.155-3.S3-ext, status: n/a
          File: consolidated:asr1000rp2-rpcontrol.03.16.03.S.155-3.S3-ext.pkg, on: RP1/0
          Built: 2016-06-10_04.41, by: mcpre
          File SHA1 checksum: 4c6e5a1b052aadb2665ddb6f869e823970f9d4ee

        Package: rpios-adventerprise, version: 03.16.03.S.155-3.S3-ext, status: n/a
          File: consolidated:asr1000rp2-rpios-adventerprise.03.16.03.S.155-3.S3-ext.pkg, on: RP1/0
          Built: 2016-06-10_04.43, by: mcpre
          File SHA1 checksum: 095f51f1d35ab539f6b26773c9413a41f918ad42

        Package: rpaccess, version: 03.16.03.S.155-3.S3-ext, status: n/a
          File: consolidated:asr1000rp2-rpaccess.03.16.03.S.155-3.S3-ext.pkg, on: RP1/0
          Built: 2016-06-10_04.41, by: mcpre
          File SHA1 checksum: 32547e24130869ad9985aca9370a0d7214d256e9

        Package: espbase, version: 03.16.03.S.155-3.S3-ext, status: n/a
          File: consolidated:asr1000rp2-espbase.03.16.03.S.155-3.S3-ext.pkg, on: ESP0
          Built: 2016-06-10_03.48, by: mcpre
          File SHA1 checksum: 4699d60fdb5fad4cc56927917309de4a4027e4e5

        Package: espx86base, version: 03.16.03.S.155-3.S3-ext, status: n/a
          File: consolidated:asr1000rp2-espx86base.03.16.03.S.155-3.S3-ext.pkg, on: ESP0
          Built: 2016-06-10_04.41, by: mcpre
          File SHA1 checksum: 1d7393ac1fc1569797e62b8ce3bf5b3354ba3572

        Package: espbase, version: 03.16.03.S.155-3.S3-ext, status: n/a
          File: consolidated:asr1000rp2-espbase.03.16.03.S.155-3.S3-ext.pkg, on: ESP1
          Built: 2016-06-10_03.48, by: mcpre
          File SHA1 checksum: 4699d60fdb5fad4cc56927917309de4a4027e4e5

        Package: espx86base, version: 03.16.03.S.155-3.S3-ext, status: n/a
          File: consolidated:asr1000rp2-espx86base.03.16.03.S.155-3.S3-ext.pkg, on: ESP1
          Built: 2016-06-10_04.41, by: mcpre
          File SHA1 checksum: 1d7393ac1fc1569797e62b8ce3bf5b3354ba3572

        Package: sipbase, version: 03.16.03.S.155-3.S3-ext, status: n/a
          File: consolidated:asr1000rp2-sipbase.03.16.03.S.155-3.S3-ext.pkg, on: SIP0
          Built: 2016-06-10_03.48, by: mcpre
          File SHA1 checksum: db8fb38d845c23b0e0f74b05f1a86aadcaa34972

        Package: elcbase, version: 03.16.03.S.155-3.S3-ext, status: n/a
          File: consolidated:asr1000rp2-elcbase.03.16.03.S.155-3.S3-ext.pkg, on: SIP0
          Built: 2016-06-10_03.48, by: mcpre
          File SHA1 checksum: e4573bf9a752b31a0c2d713990ad13e11b9b3387

        Package: sipspa, version: 03.16.03.S.155-3.S3-ext, status: n/a
          File: consolidated:asr1000rp2-sipspa.03.16.03.S.155-3.S3-ext.pkg, on: SIP0/0
          Built: 2016-06-10_03.48, by: mcpre
          File SHA1 checksum: bab5367d34c07e1522c102a95b4bfa3b099a3e0e

        Package: elcspa, version: 03.16.03.S.155-3.S3-ext, status: n/a
          File: consolidated:asr1000rp2-elcspa.03.16.03.S.155-3.S3-ext.pkg, on: SIP0/0
          Built: 2016-06-10_03.48, by: mcpre
          File SHA1 checksum: a912595d72b5be9890810042ec2a529d5d9a18b7

        Package: sipspa, version: 03.16.03.S.155-3.S3-ext, status: n/a
          File: consolidated:asr1000rp2-sipspa.03.16.03.S.155-3.S3-ext.pkg, on: SIP0/1
          Built: 2016-06-10_03.48, by: mcpre
          File SHA1 checksum: bab5367d34c07e1522c102a95b4bfa3b099a3e0e

        Package: elcspa, version: 03.16.03.S.155-3.S3-ext, status: n/a
          File: consolidated:asr1000rp2-elcspa.03.16.03.S.155-3.S3-ext.pkg, on: SIP0/1
          Built: 2016-06-10_03.48, by: mcpre
          File SHA1 checksum: a912595d72b5be9890810042ec2a529d5d9a18b7

        Package: sipspa, version: 03.16.03.S.155-3.S3-ext, status: n/a
          File: consolidated:asr1000rp2-sipspa.03.16.03.S.155-3.S3-ext.pkg, on: SIP0/2
          Built: 2016-06-10_03.48, by: mcpre
          File SHA1 checksum: bab5367d34c07e1522c102a95b4bfa3b099a3e0e

        Package: elcspa, version: 03.16.03.S.155-3.S3-ext, status: n/a
          File: consolidated:asr1000rp2-elcspa.03.16.03.S.155-3.S3-ext.pkg, on: SIP0/2
          Built: 2016-06-10_03.48, by: mcpre
          File SHA1 checksum: a912595d72b5be9890810042ec2a529d5d9a18b7

        Package: sipspa, version: 03.16.03.S.155-3.S3-ext, status: n/a
          File: consolidated:asr1000rp2-sipspa.03.16.03.S.155-3.S3-ext.pkg, on: SIP0/3
          Built: 2016-06-10_03.48, by: mcpre
          File SHA1 checksum: bab5367d34c07e1522c102a95b4bfa3b099a3e0e

        Package: elcspa, version: 03.16.03.S.155-3.S3-ext, status: n/a
          File: consolidated:asr1000rp2-elcspa.03.16.03.S.155-3.S3-ext.pkg, on: SIP0/3
          Built: 2016-06-10_03.48, by: mcpre
          File SHA1 checksum: a912595d72b5be9890810042ec2a529d5d9a18b7

        Package: sipbase, version: 03.16.03.S.155-3.S3-ext, status: n/a
          File: consolidated:asr1000rp2-sipbase.03.16.03.S.155-3.S3-ext.pkg, on: SIP1
          Built: 2016-06-10_03.48, by: mcpre
          File SHA1 checksum: db8fb38d845c23b0e0f74b05f1a86aadcaa34972

        Package: elcbase, version: 03.16.03.S.155-3.S3-ext, status: n/a
          File: consolidated:asr1000rp2-elcbase.03.16.03.S.155-3.S3-ext.pkg, on: SIP1
          Built: 2016-06-10_03.48, by: mcpre
          File SHA1 checksum: e4573bf9a752b31a0c2d713990ad13e11b9b3387

        Package: sipspa, version: 03.16.03.S.155-3.S3-ext, status: n/a
          File: consolidated:asr1000rp2-sipspa.03.16.03.S.155-3.S3-ext.pkg, on: SIP1/0
          Built: 2016-06-10_03.48, by: mcpre
          File SHA1 checksum: bab5367d34c07e1522c102a95b4bfa3b099a3e0e

        Package: elcspa, version: 03.16.03.S.155-3.S3-ext, status: n/a
          File: consolidated:asr1000rp2-elcspa.03.16.03.S.155-3.S3-ext.pkg, on: SIP1/0
          Built: 2016-06-10_03.48, by: mcpre
          File SHA1 checksum: a912595d72b5be9890810042ec2a529d5d9a18b7

        Package: sipspa, version: 03.16.03.S.155-3.S3-ext, status: n/a
          File: consolidated:asr1000rp2-sipspa.03.16.03.S.155-3.S3-ext.pkg, on: SIP1/1
          Built: 2016-06-10_03.48, by: mcpre
          File SHA1 checksum: bab5367d34c07e1522c102a95b4bfa3b099a3e0e

        Package: elcspa, version: 03.16.03.S.155-3.S3-ext, status: n/a
          File: consolidated:asr1000rp2-elcspa.03.16.03.S.155-3.S3-ext.pkg, on: SIP1/1
          Built: 2016-06-10_03.48, by: mcpre
          File SHA1 checksum: a912595d72b5be9890810042ec2a529d5d9a18b7
    '''
    }

    golden_output_standby_offline = {'execute.return_value': '''\
        Router#show version RP standby running
        Load for five secs: 1%/0%; one minute: 24%; five minutes: 43%
        Time source is NTP, 18:31:45.991 EST Mon Oct 24 2016
        The standby Route-Processor is currently offline
    '''
    }

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


class TestShowPlatformHardware(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output_active = {
        'BG4001.1020892': {
            'if_h': 4256},
        'BG4002.1020893': {'if_h': 4257},
        'BG4006.1020894': {'if_h': 4258},
        'BG4010.1020895': {'if_h': 4259},
        'BG4033.10207fd': {'if_h': 4107},
        'BG4044.10207fe': {'if_h': 4108},
        'BG4045.10207ff': {'if_h': 4109},
        'BG4048.10207e1': {'if_h': 4079},
        'BG4111.1020807': {'if_h': 4117},
        'BG4117.1020808': {'if_h': 4118},
        'BG4118.1020809': {'if_h': 4119},
        'CPP_Null': {'if_h': 5},
        'GigabitEthernet0/0/0': {
            'if_h': 7,
            'index': {
                '0': {
                    'name': 'GigabitEthernet0/0/0',
                    'queue_id': '0x8d',
                    'software_control_info': {
                        'cache_queue_id': '0x0000008d',
                        'debug_name': 'GigabitEthernet0/0/0',
                        'defer_obj_refcnt': 0,
                        'max': 0,
                        'max_dflt': 0,
                        'max_qos': 0,
                        'min': 105000000,
                        'min_dflt': 0,
                        'min_qos': 0,
                        'orig_max': 0,
                        'orig_min': 0,
                        'parent_sid': '0x268',
                        'plevel': 0,
                        'port_uidb': 245753,
                        'priority': 65535,
                        'qlimit_bytes': 3281312,
                        'share': 1,
                        'sw_flags': '0x08000011',
                        'sw_state': '0x00000c01',
                        'wred': '0x88b16932',
                    },
                    'statistics': {
                        'lic_throughput_oversub_drops_bytes': 0,
                        'lic_throughput_oversub_drops_packets': 0,
                        'queue_depth_bytes': 0,
                        'tail_drops_bytes': 0,
                        'tail_drops_packets': 0,
                        'total_enqs_bytes': 103120085,
                        'total_enqs_packets': 518314,
                    }
                }
            }
        },
        'GigabitEthernet0/0/1': {'if_h': 8,
                          'index': {'0': {'name': 'GigabitEthernet0/0/1',
                                          'queue_id': '0x8e',
                                          'software_control_info': {'cache_queue_id': '0x0000008e',
                                                                    'debug_name': 'GigabitEthernet0/0/1',
                                                                    'defer_obj_refcnt': 0,
                                                                    'max': 0,
                                                                    'max_dflt': 0,
                                                                    'max_qos': 0,
                                                                    'min': 105000000,
                                                                    'min_dflt': 0,
                                                                    'min_qos': 0,
                                                                    'orig_max': 0,
                                                                    'orig_min': 0,
                                                                    'parent_sid': '0x269',
                                                                    'plevel': 0,
                                                                    'port_uidb': 245752,
                                                                    'priority': 65535,
                                                                    'qlimit_bytes': 3281312,
                                                                    'share': 1,
                                                                    'sw_flags': '0x08000011',
                                                                    'sw_state': '0x00000c01',
                                                                    'wred': '0x88b16942'},
                                          'statistics': {'lic_throughput_oversub_drops_bytes': 0,
                                                         'lic_throughput_oversub_drops_packets': 0,
                                                         'queue_depth_bytes': 0,
                                                         'tail_drops_bytes': 0,
                                                         'tail_drops_packets': 0,
                                                         'total_enqs_bytes': 649104074,
                                                         'total_enqs_packets': 7688841}}}},
 'GigabitEthernet0/0/1.11': {'if_h': 37},
 'GigabitEthernet0/0/1.12': {'if_h': 38},
 'GigabitEthernet0/0/1.13': {'if_h': 39},
 'GigabitEthernet0/0/1.14': {'if_h': 40},
 'GigabitEthernet0/0/1.15': {'if_h': 41},
 'GigabitEthernet0/0/1.16': {'if_h': 42},
 'GigabitEthernet0/0/1.17': {'if_h': 43},
 'GigabitEthernet0/0/1.1795': {'if_h': 1821},
 'GigabitEthernet0/0/1.1796': {'if_h': 1822},
 'GigabitEthernet0/0/1.1797': {'if_h': 1823},
 'GigabitEthernet0/0/1.18': {'if_h': 44},
 'GigabitEthernet0/0/1.19': {'if_h': 45},
 'GigabitEthernet0/0/1.2': {'if_h': 35},
 'GigabitEthernet0/0/1.20': {'if_h': 46},
 'GigabitEthernet0/0/1.21': {'if_h': 47},
 'GigabitEthernet0/0/1.22': {'if_h': 48},
 'GigabitEthernet0/0/1.23': {'if_h': 49},
 'GigabitEthernet0/0/1.24': {'if_h': 50},
 'GigabitEthernet0/0/1.25': {'if_h': 51},
 'GigabitEthernet0/0/1.26': {'if_h': 52},
 'GigabitEthernet0/0/1.27': {'if_h': 53},
 'GigabitEthernet0/0/1.28': {'if_h': 54},
 'GigabitEthernet0/0/1.29': {'if_h': 55},
 'GigabitEthernet0/0/1.30': {'if_h': 56},
 'GigabitEthernet0/0/1.31': {'if_h': 57},
 'GigabitEthernet0/0/1.32': {'if_h': 58},
 'GigabitEthernet0/0/1.33': {'if_h': 59},
 'GigabitEthernet0/0/1.34': {'if_h': 60},
 'GigabitEthernet0/0/1.35': {'if_h': 61},
 'GigabitEthernet0/0/1.36': {'if_h': 62},
 'GigabitEthernet0/0/1.37': {'if_h': 63},
 'GigabitEthernet0/0/1.38': {'if_h': 64},
 'GigabitEthernet0/0/1.400': {'if_h': 426},
 'GigabitEthernet0/0/1.401': {'if_h': 427},
 'GigabitEthernet0/0/1.402': {'if_h': 428},
 'GigabitEthernet0/0/1.403': {'if_h': 429},
 'GigabitEthernet0/0/1.404': {'if_h': 430},
 'GigabitEthernet0/0/1.405': {'if_h': 431},
 'GigabitEthernet0/0/1.406': {'if_h': 432},
 'GigabitEthernet0/0/1.407': {'if_h': 433},
 'GigabitEthernet0/0/1.408': {'if_h': 434},
 'GigabitEthernet0/0/1.409': {'if_h': 435},
 'GigabitEthernet0/0/1.410': {'if_h': 436},
 'GigabitEthernet0/0/1.411': {'if_h': 437},
 'GigabitEthernet0/0/1.412': {'if_h': 438},
 'GigabitEthernet0/0/1.413': {'if_h': 439},
 'GigabitEthernet0/0/1.414': {'if_h': 440},
 'GigabitEthernet0/0/1.415': {'if_h': 441},
 'GigabitEthernet0/0/1.416': {'if_h': 442},
 'GigabitEthernet0/0/1.417': {'if_h': 443},
 'GigabitEthernet0/0/1.418': {'if_h': 444},
 'GigabitEthernet0/0/1.419': {'if_h': 445},
 'GigabitEthernet0/0/1.420': {'if_h': 446},
 'GigabitEthernet0/0/1.421': {'if_h': 447},
 'GigabitEthernet0/0/1.422': {'if_h': 448},
 'GigabitEthernet0/0/1.423': {'if_h': 449},
 'GigabitEthernet0/0/1.424': {'if_h': 450},
 'GigabitEthernet0/0/1.425': {'if_h': 451},
 'GigabitEthernet0/0/1.426': {'if_h': 452},
 'GigabitEthernet0/0/1.427': {'if_h': 453},
 'GigabitEthernet0/0/1.428': {'if_h': 454},
 'GigabitEthernet0/0/1.429': {'if_h': 455},
 'GigabitEthernet0/0/1.430': {'if_h': 456},
 'GigabitEthernet0/0/1.431': {'if_h': 457},
 'GigabitEthernet0/0/1.432': {'if_h': 458},
 'GigabitEthernet0/0/1.433': {'if_h': 459},
 'GigabitEthernet0/0/1.434': {'if_h': 460},
 'GigabitEthernet0/0/1.57': {'if_h': 83},
 'GigabitEthernet0/0/1.58': {'if_h': 84},
 'GigabitEthernet0/0/1.59': {'if_h': 85},
 'GigabitEthernet0/0/1.60': {'if_h': 86},
 'GigabitEthernet0/0/1.61': {'if_h': 87},
 'GigabitEthernet0/0/1.62': {'if_h': 88},
 'GigabitEthernet0/0/1.63': {'if_h': 89},
 'GigabitEthernet0/0/1.720': {'if_h': 746},
 'GigabitEthernet0/0/1.721': {'if_h': 747},
 'GigabitEthernet0/0/1.722': {'if_h': 748},
 'GigabitEthernet0/0/1.723': {'if_h': 749},
 'GigabitEthernet0/0/1.724': {'if_h': 750},
 'GigabitEthernet0/0/1.725': {'if_h': 751},
 'GigabitEthernet0/0/1.726': {'if_h': 752},
 'GigabitEthernet0/0/1.727': {'if_h': 753},
 'GigabitEthernet0/0/1.728': {'if_h': 754},
 'GigabitEthernet0/0/1.729': {'if_h': 755},
 'GigabitEthernet0/0/1.730': {'if_h': 756},
 'GigabitEthernet0/0/1.731': {'if_h': 757},
 'GigabitEthernet0/0/1.732': {'if_h': 758},
 'GigabitEthernet0/0/1.733': {'if_h': 759},
 'GigabitEthernet0/0/1.734': {'if_h': 760},
 'GigabitEthernet0/0/1.735': {'if_h': 761},
 'GigabitEthernet0/0/1.736': {'if_h': 762},
 'GigabitEthernet0/0/1.737': {'if_h': 763},
 'GigabitEthernet0/0/1.738': {'if_h': 764},
 'GigabitEthernet0/0/1.EFP2054': {'if_h': 36},
 'GigabitEthernet0/0/2': {'if_h': 9,
                          'index': {'0': {'name': 'GigabitEthernet0/0/2',
                                          'queue_id': '0x8f',
                                          'software_control_info': {'cache_queue_id': '0x0000008f',
                                                                    'debug_name': 'GigabitEthernet0/0/2',
                                                                    'defer_obj_refcnt': 0,
                                                                    'max': 0,
                                                                    'max_dflt': 0,
                                                                    'max_qos': 0,
                                                                    'min': 105000000,
                                                                    'min_dflt': 0,
                                                                    'min_qos': 0,
                                                                    'orig_max': 0,
                                                                    'orig_min': 0,
                                                                    'parent_sid': '0x26a',
                                                                    'plevel': 0,
                                                                    'port_uidb': 245751,
                                                                    'priority': 65535,
                                                                    'qlimit_bytes': 3281312,
                                                                    'share': 1,
                                                                    'sw_flags': '0x08000011',
                                                                    'sw_state': '0x00000c01',
                                                                    'wred': '0x88b16952'},
                                          'statistics': {'lic_throughput_oversub_drops_bytes': 0,
                                                         'lic_throughput_oversub_drops_packets': 0,
                                                         'queue_depth_bytes': 0,
                                                         'tail_drops_bytes': 0,
                                                         'tail_drops_packets': 0,
                                                         'total_enqs_bytes': 779830,
                                                         'total_enqs_packets': 10261}}}},
 'GigabitEthernet0/0/3': {'if_h': 10,
                          'index': {'0': {'name': 'GigabitEthernet0/0/3',
                                          'queue_id': '0x90',
                                          'software_control_info': {'cache_queue_id': '0x00000090',
                                                                    'debug_name': 'GigabitEthernet0/0/3',
                                                                    'defer_obj_refcnt': 0,
                                                                    'max': 0,
                                                                    'max_dflt': 0,
                                                                    'max_qos': 0,
                                                                    'min': 105000000,
                                                                    'min_dflt': 0,
                                                                    'min_qos': 0,
                                                                    'orig_max': 0,
                                                                    'orig_min': 0,
                                                                    'parent_sid': '0x26b',
                                                                    'plevel': 0,
                                                                    'port_uidb': 245750,
                                                                    'priority': 65535,
                                                                    'qlimit_bytes': 3281312,
                                                                    'share': 1,
                                                                    'sw_flags': '0x08000011',
                                                                    'sw_state': '0x00000c01',
                                                                    'wred': '0x88b16962'},
                                          'statistics': {'lic_throughput_oversub_drops_bytes': 0,
                                                         'lic_throughput_oversub_drops_packets': 0,
                                                         'queue_depth_bytes': 0,
                                                         'tail_drops_bytes': 0,
                                                         'tail_drops_packets': 0,
                                                         'total_enqs_bytes': 5698,
                                                         'total_enqs_packets': 74}}}},
 'GigabitEthernet0/0/3.EFP2051': {'if_h': 2077},
 'GigabitEthernet0/0/3.EFP2052': {'if_h': 2078},
 'GigabitEthernet0/0/3.EFP2053': {'if_h': 2079},
 'GigabitEthernet0/0/3.EFP2054': {'if_h': 2080},
 'GigabitEthernet0/0/3.EFP2055': {'if_h': 2081},
 'GigabitEthernet0/0/3.EFP2174': {'if_h': 2200},
 'GigabitEthernet0/0/3.EFP2175': {'if_h': 2201},
 'GigabitEthernet0/0/3.EFP2176': {'if_h': 2202},
 'GigabitEthernet0/0/3.EFP2177': {'if_h': 2203},
 'GigabitEthernet0/0/3.EFP2178': {'if_h': 2204},
 'GigabitEthernet0/0/3.EFP2179': {'if_h': 2205},
 'GigabitEthernet0/0/4': {'if_h': 11,
                          'index': {'0': {'name': 'GigabitEthernet0/0/4',
                                          'queue_id': '0x91',
                                          'software_control_info': {'cache_queue_id': '0x00000091',
                                                                    'debug_name': 'GigabitEthernet0/0/4',
                                                                    'defer_obj_refcnt': 0,
                                                                    'max': 0,
                                                                    'max_dflt': 0,
                                                                    'max_qos': 0,
                                                                    'min': 105000000,
                                                                    'min_dflt': 0,
                                                                    'min_qos': 0,
                                                                    'orig_max': 0,
                                                                    'orig_min': 0,
                                                                    'parent_sid': '0x26c',
                                                                    'plevel': 0,
                                                                    'port_uidb': 245749,
                                                                    'priority': 65535,
                                                                    'qlimit_bytes': 3281312,
                                                                    'share': 1,
                                                                    'sw_flags': '0x08000011',
                                                                    'sw_state': '0x00000c01',
                                                                    'wred': '0x88b16972'},
                                          'statistics': {'lic_throughput_oversub_drops_bytes': 0,
                                                         'lic_throughput_oversub_drops_packets': 0,
                                                         'queue_depth_bytes': 0,
                                                         'tail_drops_bytes': 0,
                                                         'tail_drops_packets': 0,
                                                         'total_enqs_bytes': 2754752998,
                                                         'total_enqs_packets': 2765893}}}},
 'GigabitEthernet0/0/5': {'if_h': 12,
                          'index': {'0': {'name': 'GigabitEthernet0/0/5',
                                          'queue_id': '0x92',
                                          'software_control_info': {'cache_queue_id': '0x00000092',
                                                                    'debug_name': 'GigabitEthernet0/0/5',
                                                                    'defer_obj_refcnt': 0,
                                                                    'max': 0,
                                                                    'max_dflt': 0,
                                                                    'max_qos': 0,
                                                                    'min': 105000000,
                                                                    'min_dflt': 0,
                                                                    'min_qos': 0,
                                                                    'orig_max': 0,
                                                                    'orig_min': 0,
                                                                    'parent_sid': '0x26d',
                                                                    'plevel': 0,
                                                                    'port_uidb': 245748,
                                                                    'priority': 65535,
                                                                    'qlimit_bytes': 3281312,
                                                                    'share': 1,
                                                                    'sw_flags': '0x08000011',
                                                                    'sw_state': '0x00000c01',
                                                                    'wred': '0x88b16982'},
                                          'statistics': {'lic_throughput_oversub_drops_bytes': 0,
                                                         'lic_throughput_oversub_drops_packets': 0,
                                                         'queue_depth_bytes': 0,
                                                         'tail_drops_bytes': 0,
                                                         'tail_drops_packets': 0,
                                                         'total_enqs_bytes': 2754752998,
                                                         'total_enqs_packets': 2765893}}}},
 'GigabitEthernet0/0/6': {'if_h': 13,
                          'index': {'0': {'name': 'GigabitEthernet0/0/6',
                                          'queue_id': '0x93',
                                          'software_control_info': {'cache_queue_id': '0x00000093',
                                                                    'debug_name': 'GigabitEthernet0/0/6',
                                                                    'defer_obj_refcnt': 0,
                                                                    'max': 0,
                                                                    'max_dflt': 0,
                                                                    'max_qos': 0,
                                                                    'min': 105000000,
                                                                    'min_dflt': 0,
                                                                    'min_qos': 0,
                                                                    'orig_max': 0,
                                                                    'orig_min': 0,
                                                                    'parent_sid': '0x26e',
                                                                    'plevel': 0,
                                                                    'port_uidb': 245747,
                                                                    'priority': 65535,
                                                                    'qlimit_bytes': 3281312,
                                                                    'share': 1,
                                                                    'sw_flags': '0x08000011',
                                                                    'sw_state': '0x00000c01',
                                                                    'wred': '0x88b16992'},
                                          'statistics': {'lic_throughput_oversub_drops_bytes': 0,
                                                         'lic_throughput_oversub_drops_packets': 0,
                                                         'queue_depth_bytes': 0,
                                                         'tail_drops_bytes': 0,
                                                         'tail_drops_packets': 0,
                                                         'total_enqs_bytes': 5998,
                                                         'total_enqs_packets': 79}}}},
 'GigabitEthernet0/0/7': {'if_h': 14,
                          'index': {'0': {'name': 'GigabitEthernet0/0/7',
                                          'queue_id': '0x94',
                                          'software_control_info': {'cache_queue_id': '0x00000094',
                                                                    'debug_name': 'GigabitEthernet0/0/7',
                                                                    'defer_obj_refcnt': 0,
                                                                    'max': 0,
                                                                    'max_dflt': 0,
                                                                    'max_qos': 0,
                                                                    'min': 105000000,
                                                                    'min_dflt': 0,
                                                                    'min_qos': 0,
                                                                    'orig_max': 0,
                                                                    'orig_min': 0,
                                                                    'parent_sid': '0x270',
                                                                    'plevel': 0,
                                                                    'port_uidb': 245746,
                                                                    'priority': 65535,
                                                                    'qlimit_bytes': 3281312,
                                                                    'share': 1,
                                                                    'sw_flags': '0x08000011',
                                                                    'sw_state': '0x00000c01',
                                                                    'wred': '0x88b169a2'},
                                          'statistics': {'lic_throughput_oversub_drops_bytes': 0,
                                                         'lic_throughput_oversub_drops_packets': 0,
                                                         'queue_depth_bytes': 0,
                                                         'tail_drops_bytes': 0,
                                                         'tail_drops_packets': 0,
                                                         'total_enqs_bytes': 0,
                                                         'total_enqs_packets': 0}}}},
 'GigabitEthernet0/1/0': {'if_h': 15,
                          'index': {'0': {'name': 'GigabitEthernet0/1/0',
                                          'queue_id': '0x95',
                                          'software_control_info': {'cache_queue_id': '0x00000095',
                                                                    'debug_name': 'GigabitEthernet0/1/0',
                                                                    'defer_obj_refcnt': 0,
                                                                    'max': 0,
                                                                    'max_dflt': 0,
                                                                    'max_qos': 0,
                                                                    'min': 105000000,
                                                                    'min_dflt': 0,
                                                                    'min_qos': 0,
                                                                    'orig_max': 0,
                                                                    'orig_min': 0,
                                                                    'parent_sid': '0x271',
                                                                    'plevel': 0,
                                                                    'port_uidb': 245745,
                                                                    'priority': 65535,
                                                                    'qlimit_bytes': 3281312,
                                                                    'share': 1,
                                                                    'sw_flags': '0x08000011',
                                                                    'sw_state': '0x00000c01',
                                                                    'wred': '0x88b169b2'},
                                          'statistics': {'lic_throughput_oversub_drops_bytes': 0,
                                                         'lic_throughput_oversub_drops_packets': 0,
                                                         'queue_depth_bytes': 0,
                                                         'tail_drops_bytes': 0,
                                                         'tail_drops_packets': 0,
                                                         'total_enqs_bytes': 0,
                                                         'total_enqs_packets': 0}}}},
 'GigabitEthernet0/1/1': {'if_h': 16,
                          'index': {'0': {'name': 'GigabitEthernet0/1/1',
                                          'queue_id': '0x96',
                                          'software_control_info': {'cache_queue_id': '0x00000096',
                                                                    'debug_name': 'GigabitEthernet0/1/1',
                                                                    'defer_obj_refcnt': 0,
                                                                    'max': 0,
                                                                    'max_dflt': 0,
                                                                    'max_qos': 0,
                                                                    'min': 105000000,
                                                                    'min_dflt': 0,
                                                                    'min_qos': 0,
                                                                    'orig_max': 0,
                                                                    'orig_min': 0,
                                                                    'parent_sid': '0x272',
                                                                    'plevel': 0,
                                                                    'port_uidb': 245744,
                                                                    'priority': 65535,
                                                                    'qlimit_bytes': 3281312,
                                                                    'share': 1,
                                                                    'sw_flags': '0x08000011',
                                                                    'sw_state': '0x00000c01',
                                                                    'wred': '0x88b169c2'},
                                          'statistics': {'lic_throughput_oversub_drops_bytes': 0,
                                                         'lic_throughput_oversub_drops_packets': 0,
                                                         'queue_depth_bytes': 0,
                                                         'tail_drops_bytes': 0,
                                                         'tail_drops_packets': 0,
                                                         'total_enqs_bytes': 0,
                                                         'total_enqs_packets': 0}}}},
 'GigabitEthernet0/1/2': {'if_h': 17,
                          'index': {'0': {'name': 'GigabitEthernet0/1/2',
                                          'queue_id': '0x97',
                                          'software_control_info': {'cache_queue_id': '0x00000097',
                                                                    'debug_name': 'GigabitEthernet0/1/2',
                                                                    'defer_obj_refcnt': 0,
                                                                    'max': 0,
                                                                    'max_dflt': 0,
                                                                    'max_qos': 0,
                                                                    'min': 105000000,
                                                                    'min_dflt': 0,
                                                                    'min_qos': 0,
                                                                    'orig_max': 0,
                                                                    'orig_min': 0,
                                                                    'parent_sid': '0x273',
                                                                    'plevel': 0,
                                                                    'port_uidb': 245743,
                                                                    'priority': 65535,
                                                                    'qlimit_bytes': 3281312,
                                                                    'share': 1,
                                                                    'sw_flags': '0x08000011',
                                                                    'sw_state': '0x00000c01',
                                                                    'wred': '0x88b169d2'},
                                          'statistics': {'lic_throughput_oversub_drops_bytes': 0,
                                                         'lic_throughput_oversub_drops_packets': 0,
                                                         'queue_depth_bytes': 0,
                                                         'tail_drops_bytes': 0,
                                                         'tail_drops_packets': 0,
                                                         'total_enqs_bytes': 0,
                                                         'total_enqs_packets': 0}}}},
 'GigabitEthernet0/1/3': {'if_h': 18,
                          'index': {'0': {'name': 'GigabitEthernet0/1/3',
                                          'queue_id': '0x98',
                                          'software_control_info': {'cache_queue_id': '0x00000098',
                                                                    'debug_name': 'GigabitEthernet0/1/3',
                                                                    'defer_obj_refcnt': 0,
                                                                    'max': 0,
                                                                    'max_dflt': 0,
                                                                    'max_qos': 0,
                                                                    'min': 105000000,
                                                                    'min_dflt': 0,
                                                                    'min_qos': 0,
                                                                    'orig_max': 0,
                                                                    'orig_min': 0,
                                                                    'parent_sid': '0x274',
                                                                    'plevel': 0,
                                                                    'port_uidb': 245742,
                                                                    'priority': 65535,
                                                                    'qlimit_bytes': 3281312,
                                                                    'share': 1,
                                                                    'sw_flags': '0x08000011',
                                                                    'sw_state': '0x00000c01',
                                                                    'wred': '0x88b169e2'},
                                          'statistics': {'lic_throughput_oversub_drops_bytes': 0,
                                                         'lic_throughput_oversub_drops_packets': 0,
                                                         'queue_depth_bytes': 0,
                                                         'tail_drops_bytes': 0,
                                                         'tail_drops_packets': 0,
                                                         'total_enqs_bytes': 0,
                                                         'total_enqs_packets': 0}}}},
 'GigabitEthernet0/1/4': {'if_h': 19,
                          'index': {'0': {'name': 'GigabitEthernet0/1/4',
                                          'queue_id': '0x99',
                                          'software_control_info': {'cache_queue_id': '0x00000099',
                                                                    'debug_name': 'GigabitEthernet0/1/4',
                                                                    'defer_obj_refcnt': 0,
                                                                    'max': 0,
                                                                    'max_dflt': 0,
                                                                    'max_qos': 0,
                                                                    'min': 105000000,
                                                                    'min_dflt': 0,
                                                                    'min_qos': 0,
                                                                    'orig_max': 0,
                                                                    'orig_min': 0,
                                                                    'parent_sid': '0x275',
                                                                    'plevel': 0,
                                                                    'port_uidb': 245741,
                                                                    'priority': 65535,
                                                                    'qlimit_bytes': 3281312,
                                                                    'share': 1,
                                                                    'sw_flags': '0x08000011',
                                                                    'sw_state': '0x00000c01',
                                                                    'wred': '0x88b169f2'},
                                          'statistics': {'lic_throughput_oversub_drops_bytes': 0,
                                                         'lic_throughput_oversub_drops_packets': 0,
                                                         'queue_depth_bytes': 0,
                                                         'tail_drops_bytes': 0,
                                                         'tail_drops_packets': 0,
                                                         'total_enqs_bytes': 0,
                                                         'total_enqs_packets': 0}}}},
 'GigabitEthernet0/1/5': {'if_h': 20,
                          'index': {'0': {'name': 'GigabitEthernet0/1/5',
                                          'queue_id': '0x9a',
                                          'software_control_info': {'cache_queue_id': '0x0000009a',
                                                                    'debug_name': 'GigabitEthernet0/1/5',
                                                                    'defer_obj_refcnt': 0,
                                                                    'max': 0,
                                                                    'max_dflt': 0,
                                                                    'max_qos': 0,
                                                                    'min': 105000000,
                                                                    'min_dflt': 0,
                                                                    'min_qos': 0,
                                                                    'orig_max': 0,
                                                                    'orig_min': 0,
                                                                    'parent_sid': '0x276',
                                                                    'plevel': 0,
                                                                    'port_uidb': 245740,
                                                                    'priority': 65535,
                                                                    'qlimit_bytes': 3281312,
                                                                    'share': 1,
                                                                    'sw_flags': '0x08000011',
                                                                    'sw_state': '0x00000c01',
                                                                    'wred': '0x88b16a02'},
                                          'statistics': {'lic_throughput_oversub_drops_bytes': 0,
                                                         'lic_throughput_oversub_drops_packets': 0,
                                                         'queue_depth_bytes': 0,
                                                         'tail_drops_bytes': 0,
                                                         'tail_drops_packets': 0,
                                                         'total_enqs_bytes': 0,
                                                         'total_enqs_packets': 0}}}},
 'GigabitEthernet0/1/6': {'if_h': 21,
                          'index': {'0': {'name': 'GigabitEthernet0/1/6',
                                          'queue_id': '0x9b',
                                          'software_control_info': {'cache_queue_id': '0x0000009b',
                                                                    'debug_name': 'GigabitEthernet0/1/6',
                                                                    'defer_obj_refcnt': 0,
                                                                    'max': 0,
                                                                    'max_dflt': 0,
                                                                    'max_qos': 0,
                                                                    'min': 105000000,
                                                                    'min_dflt': 0,
                                                                    'min_qos': 0,
                                                                    'orig_max': 0,
                                                                    'orig_min': 0,
                                                                    'parent_sid': '0x278',
                                                                    'plevel': 0,
                                                                    'port_uidb': 245739,
                                                                    'priority': 65535,
                                                                    'qlimit_bytes': 3281312,
                                                                    'share': 1,
                                                                    'sw_flags': '0x08000011',
                                                                    'sw_state': '0x00000c01',
                                                                    'wred': '0x88b16a12'},
                                          'statistics': {'lic_throughput_oversub_drops_bytes': 0,
                                                         'lic_throughput_oversub_drops_packets': 0,
                                                         'queue_depth_bytes': 0,
                                                         'tail_drops_bytes': 0,
                                                         'tail_drops_packets': 0,
                                                         'total_enqs_bytes': 0,
                                                         'total_enqs_packets': 0}}}},
 'GigabitEthernet0/1/7': {'if_h': 22,
                          'index': {'0': {'name': 'GigabitEthernet0/1/7',
                                          'queue_id': '0x9c',
                                          'software_control_info': {'cache_queue_id': '0x0000009c',
                                                                    'debug_name': 'GigabitEthernet0/1/7',
                                                                    'defer_obj_refcnt': 0,
                                                                    'max': 0,
                                                                    'max_dflt': 0,
                                                                    'max_qos': 0,
                                                                    'min': 105000000,
                                                                    'min_dflt': 0,
                                                                    'min_qos': 0,
                                                                    'orig_max': 0,
                                                                    'orig_min': 0,
                                                                    'parent_sid': '0x279',
                                                                    'plevel': 0,
                                                                    'port_uidb': 245738,
                                                                    'priority': 65535,
                                                                    'qlimit_bytes': 3281312,
                                                                    'share': 1,
                                                                    'sw_flags': '0x08000011',
                                                                    'sw_state': '0x00000c01',
                                                                    'wred': '0x88b16a22'},
                                          'statistics': {'lic_throughput_oversub_drops_bytes': 0,
                                                         'lic_throughput_oversub_drops_packets': 0,
                                                         'queue_depth_bytes': 0,
                                                         'tail_drops_bytes': 0,
                                                         'tail_drops_packets': 0,
                                                         'total_enqs_bytes': 0,
                                                         'total_enqs_packets': 0}}}},
 'GigabitEthernet1/0/0': {'if_h': 25,
                          'index': {'0': {'name': 'GigabitEthernet1/0/0',
                                          'queue_id': '0x9f',
                                          'software_control_info': {'cache_queue_id': '0x0000009f',
                                                                    'debug_name': 'GigabitEthernet1/0/0',
                                                                    'defer_obj_refcnt': 0,
                                                                    'max': 0,
                                                                    'max_dflt': 0,
                                                                    'max_qos': 0,
                                                                    'min': 105000000,
                                                                    'min_dflt': 0,
                                                                    'min_qos': 0,
                                                                    'orig_max': 0,
                                                                    'orig_min': 0,
                                                                    'parent_sid': '0x27c',
                                                                    'plevel': 0,
                                                                    'port_uidb': 245735,
                                                                    'priority': 65535,
                                                                    'qlimit_bytes': 3281312,
                                                                    'share': 1,
                                                                    'sw_flags': '0x08000011',
                                                                    'sw_state': '0x00000c01',
                                                                    'wred': '0x88b16a52'},
                                          'statistics': {'lic_throughput_oversub_drops_bytes': 0,
                                                         'lic_throughput_oversub_drops_packets': 0,
                                                         'queue_depth_bytes': 0,
                                                         'tail_drops_bytes': 0,
                                                         'tail_drops_packets': 0,
                                                         'total_enqs_bytes': 0,
                                                         'total_enqs_packets': 0}}}},
 'GigabitEthernet1/0/1': {'if_h': 26,
                          'index': {'0': {'name': 'GigabitEthernet1/0/1',
                                          'queue_id': '0xa0',
                                          'software_control_info': {'cache_queue_id': '0x000000a0',
                                                                    'debug_name': 'GigabitEthernet1/0/1',
                                                                    'defer_obj_refcnt': 0,
                                                                    'max': 0,
                                                                    'max_dflt': 0,
                                                                    'max_qos': 0,
                                                                    'min': 105000000,
                                                                    'min_dflt': 0,
                                                                    'min_qos': 0,
                                                                    'orig_max': 0,
                                                                    'orig_min': 0,
                                                                    'parent_sid': '0x27d',
                                                                    'plevel': 0,
                                                                    'port_uidb': 245734,
                                                                    'priority': 65535,
                                                                    'qlimit_bytes': 3281312,
                                                                    'share': 1,
                                                                    'sw_flags': '0x08000011',
                                                                    'sw_state': '0x00000c01',
                                                                    'wred': '0x88b16a62'},
                                          'statistics': {'lic_throughput_oversub_drops_bytes': 0,
                                                         'lic_throughput_oversub_drops_packets': 0,
                                                         'queue_depth_bytes': 0,
                                                         'tail_drops_bytes': 0,
                                                         'tail_drops_packets': 0,
                                                         'total_enqs_bytes': 0,
                                                         'total_enqs_packets': 0}}}},
 'GigabitEthernet1/0/2': {'if_h': 27,
                          'index': {'0': {'name': 'GigabitEthernet1/0/2',
                                          'queue_id': '0xa1',
                                          'software_control_info': {'cache_queue_id': '0x000000a1',
                                                                    'debug_name': 'GigabitEthernet1/0/2',
                                                                    'defer_obj_refcnt': 0,
                                                                    'max': 0,
                                                                    'max_dflt': 0,
                                                                    'max_qos': 0,
                                                                    'min': 105000000,
                                                                    'min_dflt': 0,
                                                                    'min_qos': 0,
                                                                    'orig_max': 0,
                                                                    'orig_min': 0,
                                                                    'parent_sid': '0x27e',
                                                                    'plevel': 0,
                                                                    'port_uidb': 245733,
                                                                    'priority': 65535,
                                                                    'qlimit_bytes': 3281312,
                                                                    'share': 1,
                                                                    'sw_flags': '0x08000011',
                                                                    'sw_state': '0x00000c01',
                                                                    'wred': '0x88b16a72'},
                                          'statistics': {'lic_throughput_oversub_drops_bytes': 0,
                                                         'lic_throughput_oversub_drops_packets': 0,
                                                         'queue_depth_bytes': 0,
                                                         'tail_drops_bytes': 0,
                                                         'tail_drops_packets': 0,
                                                         'total_enqs_bytes': 0,
                                                         'total_enqs_packets': 0}}}},
 'GigabitEthernet1/0/3': {'if_h': 28,
                          'index': {'0': {'name': 'GigabitEthernet1/0/3',
                                          'queue_id': '0xa2',
                                          'software_control_info': {'cache_queue_id': '0x000000a2',
                                                                    'debug_name': 'GigabitEthernet1/0/3',
                                                                    'defer_obj_refcnt': 0,
                                                                    'max': 0,
                                                                    'max_dflt': 0,
                                                                    'max_qos': 0,
                                                                    'min': 105000000,
                                                                    'min_dflt': 0,
                                                                    'min_qos': 0,
                                                                    'orig_max': 0,
                                                                    'orig_min': 0,
                                                                    'parent_sid': '0x280',
                                                                    'plevel': 0,
                                                                    'port_uidb': 245732,
                                                                    'priority': 65535,
                                                                    'qlimit_bytes': 3281312,
                                                                    'share': 1,
                                                                    'sw_flags': '0x08000011',
                                                                    'sw_state': '0x00000c01',
                                                                    'wred': '0x88b16a82'},
                                          'statistics': {'lic_throughput_oversub_drops_bytes': 0,
                                                         'lic_throughput_oversub_drops_packets': 0,
                                                         'queue_depth_bytes': 0,
                                                         'tail_drops_bytes': 0,
                                                         'tail_drops_packets': 0,
                                                         'total_enqs_bytes': 0,
                                                         'total_enqs_packets': 0}}}},
 'GigabitEthernet1/0/4': {'if_h': 29,
                          'index': {'0': {'name': 'GigabitEthernet1/0/4',
                                          'queue_id': '0xa3',
                                          'software_control_info': {'cache_queue_id': '0x000000a3',
                                                                    'debug_name': 'GigabitEthernet1/0/4',
                                                                    'defer_obj_refcnt': 0,
                                                                    'max': 0,
                                                                    'max_dflt': 0,
                                                                    'max_qos': 0,
                                                                    'min': 105000000,
                                                                    'min_dflt': 0,
                                                                    'min_qos': 0,
                                                                    'orig_max': 0,
                                                                    'orig_min': 0,
                                                                    'parent_sid': '0x281',
                                                                    'plevel': 0,
                                                                    'port_uidb': 245731,
                                                                    'priority': 65535,
                                                                    'qlimit_bytes': 3281312,
                                                                    'share': 1,
                                                                    'sw_flags': '0x08000011',
                                                                    'sw_state': '0x00000c01',
                                                                    'wred': '0x88b16a92'},
                                          'statistics': {'lic_throughput_oversub_drops_bytes': 0,
                                                         'lic_throughput_oversub_drops_packets': 0,
                                                         'queue_depth_bytes': 0,
                                                         'tail_drops_bytes': 0,
                                                         'tail_drops_packets': 0,
                                                         'total_enqs_bytes': 0,
                                                         'total_enqs_packets': 0}}}},
 'GigabitEthernet1/0/5': {'if_h': 30,
                          'index': {'0': {'name': 'GigabitEthernet1/0/5',
                                          'queue_id': '0xa4',
                                          'software_control_info': {'cache_queue_id': '0x000000a4',
                                                                    'debug_name': 'GigabitEthernet1/0/5',
                                                                    'defer_obj_refcnt': 0,
                                                                    'max': 0,
                                                                    'max_dflt': 0,
                                                                    'max_qos': 0,
                                                                    'min': 105000000,
                                                                    'min_dflt': 0,
                                                                    'min_qos': 0,
                                                                    'orig_max': 0,
                                                                    'orig_min': 0,
                                                                    'parent_sid': '0x282',
                                                                    'plevel': 0,
                                                                    'port_uidb': 245730,
                                                                    'priority': 65535,
                                                                    'qlimit_bytes': 3281312,
                                                                    'share': 1,
                                                                    'sw_flags': '0x08000011',
                                                                    'sw_state': '0x00000c01',
                                                                    'wred': '0x88b16aa2'},
                                          'statistics': {'lic_throughput_oversub_drops_bytes': 0,
                                                         'lic_throughput_oversub_drops_packets': 0,
                                                         'queue_depth_bytes': 0,
                                                         'tail_drops_bytes': 0,
                                                         'tail_drops_packets': 0,
                                                         'total_enqs_bytes': 0,
                                                         'total_enqs_packets': 0}}}},
 'GigabitEthernet1/0/6': {'if_h': 31,
                          'index': {'0': {'name': 'GigabitEthernet1/0/6',
                                          'queue_id': '0xa5',
                                          'software_control_info': {'cache_queue_id': '0x000000a5',
                                                                    'debug_name': 'GigabitEthernet1/0/6',
                                                                    'defer_obj_refcnt': 0,
                                                                    'max': 0,
                                                                    'max_dflt': 0,
                                                                    'max_qos': 0,
                                                                    'min': 105000000,
                                                                    'min_dflt': 0,
                                                                    'min_qos': 0,
                                                                    'orig_max': 0,
                                                                    'orig_min': 0,
                                                                    'parent_sid': '0x283',
                                                                    'plevel': 0,
                                                                    'port_uidb': 245729,
                                                                    'priority': 65535,
                                                                    'qlimit_bytes': 3281312,
                                                                    'share': 1,
                                                                    'sw_flags': '0x08000011',
                                                                    'sw_state': '0x00000c01',
                                                                    'wred': '0x88b16ab2'},
                                          'statistics': {'lic_throughput_oversub_drops_bytes': 0,
                                                         'lic_throughput_oversub_drops_packets': 0,
                                                         'queue_depth_bytes': 0,
                                                         'tail_drops_bytes': 0,
                                                         'tail_drops_packets': 0,
                                                         'total_enqs_bytes': 0,
                                                         'total_enqs_packets': 0}}}},
 'GigabitEthernet1/0/7': {'if_h': 32,
                          'index': {'0': {'name': 'GigabitEthernet1/0/7',
                                          'queue_id': '0xa6',
                                          'software_control_info': {'cache_queue_id': '0x000000a6',
                                                                    'debug_name': 'GigabitEthernet1/0/7',
                                                                    'defer_obj_refcnt': 0,
                                                                    'max': 0,
                                                                    'max_dflt': 0,
                                                                    'max_qos': 0,
                                                                    'min': 105000000,
                                                                    'min_dflt': 0,
                                                                    'min_qos': 0,
                                                                    'orig_max': 0,
                                                                    'orig_min': 0,
                                                                    'parent_sid': '0x284',
                                                                    'plevel': 0,
                                                                    'port_uidb': 245728,
                                                                    'priority': 65535,
                                                                    'qlimit_bytes': 3281312,
                                                                    'share': 1,
                                                                    'sw_flags': '0x08000011',
                                                                    'sw_state': '0x00000c01',
                                                                    'wred': '0x88b16ac2'},
                                          'statistics': {'lic_throughput_oversub_drops_bytes': 0,
                                                         'lic_throughput_oversub_drops_packets': 0,
                                                         'queue_depth_bytes': 0,
                                                         'tail_drops_bytes': 0,
                                                         'tail_drops_packets': 0,
                                                         'total_enqs_bytes': 0,
                                                         'total_enqs_packets': 0}}}},
 'Loopback0': {'if_h': 33},
 'Loopback2': {'if_h': 34},
 'Null0': {'if_h': 6},
 'TenGigabitEthernet0/2/0': {'if_h': 23,
                             'index': {'0': {'name': 'TenGigabitEthernet0/2/0',
                                             'queue_id': '0x9d',
                                             'software_control_info': {'cache_queue_id': '0x0000009d',
                                                                       'debug_name': 'TenGigabitEthernet0/2/0',
                                                                       'defer_obj_refcnt': 0,
                                                                       'max': 0,
                                                                       'max_dflt': 0,
                                                                       'max_qos': 0,
                                                                       'min': 1050000000,
                                                                       'min_dflt': 0,
                                                                       'min_qos': 0,
                                                                       'orig_max': 0,
                                                                       'orig_min': 0,
                                                                       'parent_sid': '0x27a',
                                                                       'plevel': 0,
                                                                       'port_uidb': 245737,
                                                                       'priority': 65535,
                                                                       'qlimit_bytes': 32812544,
                                                                       'share': 1,
                                                                       'sw_flags': '0x08000011',
                                                                       'sw_state': '0x00000c01',
                                                                       'wred': '0x88b16a32'},
                                             'statistics': {'lic_throughput_oversub_drops_bytes': 0,
                                                            'lic_throughput_oversub_drops_packets': 0,
                                                            'queue_depth_bytes': 0,
                                                            'tail_drops_bytes': 0,
                                                            'tail_drops_packets': 0,
                                                            'total_enqs_bytes': 0,
                                                            'total_enqs_packets': 0}}}},
 'TenGigabitEthernet0/3/0': {'if_h': 24,
                             'index': {'0': {'name': 'TenGigabitEthernet0/3/0',
                                             'queue_id': '0x9e',
                                             'software_control_info': {'cache_queue_id': '0x0000009e',
                                                                       'debug_name': 'TenGigabitEthernet0/3/0',
                                                                       'defer_obj_refcnt': 0,
                                                                       'max': 0,
                                                                       'max_dflt': 0,
                                                                       'max_qos': 0,
                                                                       'min': 1050000000,
                                                                       'min_dflt': 0,
                                                                       'min_qos': 0,
                                                                       'orig_max': 0,
                                                                       'orig_min': 0,
                                                                       'parent_sid': '0x27b',
                                                                       'plevel': 0,
                                                                       'port_uidb': 245736,
                                                                       'priority': 65535,
                                                                       'qlimit_bytes': 32812544,
                                                                       'share': 1,
                                                                       'sw_flags': '0x08000011',
                                                                       'sw_state': '0x00000c01',
                                                                       'wred': '0x88b16a42'},
                                             'statistics': {'lic_throughput_oversub_drops_bytes': 0,
                                                            'lic_throughput_oversub_drops_packets': 0,
                                                            'queue_depth_bytes': 0,
                                                            'tail_drops_bytes': 0,
                                                            'tail_drops_packets': 0,
                                                            'total_enqs_bytes': 0,
                                                            'total_enqs_packets': 0}}}},
 'VPLS-2320.1020896': {'if_h': 4260},
 'VPLS-2321.1020897': {'if_h': 4261},
 'VPLS-2322.1020898': {'if_h': 4262},
 'VPLS-2816.102080a': {'if_h': 4120},
 'VPLS-2817.102080b': {'if_h': 4121},
 'VPLS-2818.102080c': {'if_h': 4122},
 'VPLS-2819.102080d': {'if_h': 4123},
 'VPLS-2820.102080e': {'if_h': 4124},
 'VPLS-2944.10207e2': {'if_h': 4080},
 'VPLS-2945.10207e3': {'if_h': 4081},
 'VPLS-2946.10207e4': {'if_h': 4082},
 'VPLS-2974.10207fb': {'if_h': 4105},
 'VPLS-2975.10207fc': {'if_h': 4106},
 'VPLS-3049.1020890': {'if_h': 4254},
 'VPLS-3050.1020891': {'if_h': 4255},
 'VPLS_maint.1020a6b': {'if_h': 4729},
 'internal0/0/crypto:0': {'if_h': 4,
                          'index': {'0': {'name': 'i2l_if_4_cpp_0_prio0',
                                          'queue_id': '0x8b',
                                          'software_control_info': {'cache_queue_id': '0x0000008b',
                                                                    'debug_name': 'i2l_if_4_cpp_0_prio0',
                                                                    'defer_obj_refcnt': 0,
                                                                    'max': 0,
                                                                    'max_dflt': 0,
                                                                    'max_qos': 0,
                                                                    'min': 0,
                                                                    'min_dflt': 0,
                                                                    'min_qos': 0,
                                                                    'orig_max': 0,
                                                                    'orig_min': 0,
                                                                    'parent_sid': '0x265',
                                                                    'plevel': 0,
                                                                    'port_uidb': 245756,
                                                                    'priority': 65535,
                                                                    'qlimit_bytes': 80000064,
                                                                    'share': 1,
                                                                    'sw_flags': '0x08001001',
                                                                    'sw_state': '0x00000c01',
                                                                    'wred': '0x88b168f1'},
                                          'statistics': {'lic_throughput_oversub_drops_bytes': 0,
                                                         'lic_throughput_oversub_drops_packets': 0,
                                                         'queue_depth_bytes': 0,
                                                         'tail_drops_bytes': 0,
                                                         'tail_drops_packets': 0,
                                                         'total_enqs_bytes': 0,
                                                         'total_enqs_packets': 0}},
                                    '1': {'name': 'i2l_if_4_cpp_0_prio1',
                                          'queue_id': '0x8c',
                                          'software_control_info': {'cache_queue_id': '0x0000008c',
                                                                    'debug_name': 'i2l_if_4_cpp_0_prio1',
                                                                    'defer_obj_refcnt': 0,
                                                                    'max': 0,
                                                                    'max_dflt': 0,
                                                                    'max_qos': 0,
                                                                    'min': 0,
                                                                    'min_dflt': 0,
                                                                    'min_qos': 0,
                                                                    'orig_max': 0,
                                                                    'orig_min': 0,
                                                                    'parent_sid': '0x266',
                                                                    'plevel': 1,
                                                                    'port_uidb': 245756,
                                                                    'priority': 0,
                                                                    'qlimit_bytes': 80000064,
                                                                    'share': 0,
                                                                    'sw_flags': '0x18001001',
                                                                    'sw_state': '0x00000c01',
                                                                    'wred': '0x88b16901'},
                                          'statistics': {'lic_throughput_oversub_drops_bytes': 0,
                                                         'lic_throughput_oversub_drops_packets': 0,
                                                         'queue_depth_bytes': 0,
                                                         'tail_drops_bytes': 0,
                                                         'tail_drops_packets': 0,
                                                         'total_enqs_bytes': 0,
                                                         'total_enqs_packets': 0}}}},
 'internal0/0/recycle:0': {'if_h': 1},
 'internal0/0/rp:0': {'if_h': 2,
                      'index': {'0': {'name': 'i2l_if_2_cpp_0_prio0',
                                      'queue_id': '0x87',
                                      'software_control_info': {'cache_queue_id': '0x00000087',
                                                                'debug_name': 'i2l_if_2_cpp_0_prio0',
                                                                'defer_obj_refcnt': 0,
                                                                'max': 0,
                                                                'max_dflt': 0,
                                                                'max_qos': 0,
                                                                'min': 0,
                                                                'min_dflt': 0,
                                                                'min_qos': 0,
                                                                'orig_max': 0,
                                                                'orig_min': 0,
                                                                'parent_sid': '0x263',
                                                                'plevel': 0,
                                                                'port_uidb': 245758,
                                                                'priority': 65535,
                                                                'qlimit_bytes': 3125056,
                                                                'share': 1,
                                                                'sw_flags': '0x08000001',
                                                                'sw_state': '0x00000c01',
                                                                'wred': '0x88b16872'},
                                      'statistics': {'lic_throughput_oversub_drops_bytes': 0,
                                                     'lic_throughput_oversub_drops_packets': 0,
                                                     'queue_depth_bytes': 0,
                                                     'tail_drops_bytes': 0,
                                                     'tail_drops_packets': 0,
                                                     'total_enqs_bytes': 294475395,
                                                     'total_enqs_packets': 4297477}},
                                '1': {'name': 'i2l_if_2_cpp_0_prio1',
                                      'queue_id': '0x88',
                                      'software_control_info': {'cache_queue_id': '0x00000088',
                                                                'debug_name': 'i2l_if_2_cpp_0_prio1',
                                                                'defer_obj_refcnt': 0,
                                                                'max': 0,
                                                                'max_dflt': 0,
                                                                'max_qos': 0,
                                                                'min': 0,
                                                                'min_dflt': 0,
                                                                'min_qos': 0,
                                                                'orig_max': 0,
                                                                'orig_min': 0,
                                                                'parent_sid': '0x263',
                                                                'plevel': 1,
                                                                'port_uidb': 245758,
                                                                'priority': 0,
                                                                'qlimit_bytes': 3125056,
                                                                'share': 0,
                                                                'sw_flags': '0x18000001',
                                                                'sw_state': '0x00000c01',
                                                                'wred': '0x88b16882'},
                                      'statistics': {'lic_throughput_oversub_drops_bytes': 0,
                                                     'lic_throughput_oversub_drops_packets': 0,
                                                     'queue_depth_bytes': 0,
                                                     'tail_drops_bytes': 0,
                                                     'tail_drops_packets': 0,
                                                     'total_enqs_bytes': 203225236,
                                                     'total_enqs_packets': 1201820}}}},
 'internal0/0/rp:1': {'if_h': 3,
                      'index': {'0': {'name': 'i2l_if_3_cpp_0_prio0',
                                      'queue_id': '0x89',
                                      'software_control_info': {'cache_queue_id': '0x00000089',
                                                                'debug_name': 'i2l_if_3_cpp_0_prio0',
                                                                'defer_obj_refcnt': 0,
                                                                'max': 0,
                                                                'max_dflt': 0,
                                                                'max_qos': 0,
                                                                'min': 0,
                                                                'min_dflt': 0,
                                                                'min_qos': 0,
                                                                'orig_max': 0,
                                                                'orig_min': 0,
                                                                'parent_sid': '0x264',
                                                                'plevel': 0,
                                                                'port_uidb': 245757,
                                                                'priority': 65535,
                                                                'qlimit_bytes': 3125056,
                                                                'share': 1,
                                                                'sw_flags': '0x08000001',
                                                                'sw_state': '0x00000c01',
                                                                'wred': '0x88b168b2'},
                                      'statistics': {'lic_throughput_oversub_drops_bytes': 0,
                                                     'lic_throughput_oversub_drops_packets': 0,
                                                     'queue_depth_bytes': 0,
                                                     'tail_drops_bytes': 0,
                                                     'tail_drops_packets': 0,
                                                     'total_enqs_bytes': 46447411,
                                                     'total_enqs_packets': 670805}},
                                '1': {'name': 'i2l_if_3_cpp_0_prio1',
                                      'queue_id': '0x8a',
                                      'software_control_info': {'cache_queue_id': '0x0000008a',
                                                                'debug_name': 'i2l_if_3_cpp_0_prio1',
                                                                'defer_obj_refcnt': 0,
                                                                'max': 0,
                                                                'max_dflt': 0,
                                                                'max_qos': 0,
                                                                'min': 0,
                                                                'min_dflt': 0,
                                                                'min_qos': 0,
                                                                'orig_max': 0,
                                                                'orig_min': 0,
                                                                'parent_sid': '0x264',
                                                                'plevel': 1,
                                                                'port_uidb': 245757,
                                                                'priority': 0,
                                                                'qlimit_bytes': 3125056,
                                                                'share': 0,
                                                                'sw_flags': '0x18000001',
                                                                'sw_state': '0x00000c01',
                                                                'wred': '0x88b168c2'},
                                      'statistics': {'lic_throughput_oversub_drops_bytes': 0,
                                                     'lic_throughput_oversub_drops_packets': 0,
                                                     'queue_depth_bytes': 0,
                                                     'tail_drops_bytes': 0,
                                                     'tail_drops_packets': 0,
                                                     'total_enqs_bytes': 269658370,
                                                     'total_enqs_packets': 1424992}}}}}

    golden_output_active = {'execute.return_value': '''\
        Router#    show platform hardware qfp active infrastructure bqs queue output default all
        Load for five secs: 2%/1%; one minute: 9%; five minutes: 8%
        Time source is NTP, 07:47:13.438 EST Thu Sep 8 2016

        Interface: internal0/0/recycle:0 QFP: 0.0 if_h: 1 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: internal0/0/rp:0 QFP: 0.0 if_h: 2 Num Queues/Schedules: 2
          Queue specifics:
            Index 0 (Queue ID:0x87, Name: i2l_if_2_cpp_0_prio0)
            Software Control Info:
              (cache) queue id: 0x00000087, wred: 0x88b16872, qlimit (bytes): 3125056
              parent_sid: 0x263, debug_name: i2l_if_2_cpp_0_prio0
              sw_flags: 0x08000001, sw_state: 0x00000c01, port_uidb: 245758
              orig_min  : 0                   ,      min: 0                   
              min_qos   : 0                   , min_dflt: 0                   
              orig_max  : 0                   ,      max: 0                   
              max_qos   : 0                   , max_dflt: 0                   
              share     : 1
              plevel    : 0, priority: 65535
              defer_obj_refcnt: 0
            Statistics:
              tail drops  (bytes): 0                   ,          (packets): 0                   
              total enqs  (bytes): 294475395           ,          (packets): 4297477             
              queue_depth (bytes): 0                   
              licensed throughput oversubscription drops:
                          (bytes): 0                   ,          (packets): 0                   
          Queue specifics:
            Index 1 (Queue ID:0x88, Name: i2l_if_2_cpp_0_prio1)
            Software Control Info:
              (cache) queue id: 0x00000088, wred: 0x88b16882, qlimit (bytes): 3125056
              parent_sid: 0x263, debug_name: i2l_if_2_cpp_0_prio1
              sw_flags: 0x18000001, sw_state: 0x00000c01, port_uidb: 245758
              orig_min  : 0                   ,      min: 0                   
              min_qos   : 0                   , min_dflt: 0                   
              orig_max  : 0                   ,      max: 0                   
              max_qos   : 0                   , max_dflt: 0                   
              share     : 0
              plevel    : 1, priority: 0
              defer_obj_refcnt: 0
            Statistics:
              tail drops  (bytes): 0                   ,          (packets): 0                   
              total enqs  (bytes): 203225236           ,          (packets): 1201820             
              queue_depth (bytes): 0                   
              licensed throughput oversubscription drops:
                          (bytes): 0                   ,          (packets): 0                   

        Interface: internal0/0/rp:1 QFP: 0.0 if_h: 3 Num Queues/Schedules: 2
          Queue specifics:
            Index 0 (Queue ID:0x89, Name: i2l_if_3_cpp_0_prio0)
            Software Control Info:
              (cache) queue id: 0x00000089, wred: 0x88b168b2, qlimit (bytes): 3125056
              parent_sid: 0x264, debug_name: i2l_if_3_cpp_0_prio0
              sw_flags: 0x08000001, sw_state: 0x00000c01, port_uidb: 245757
              orig_min  : 0                   ,      min: 0                   
              min_qos   : 0                   , min_dflt: 0                   
              orig_max  : 0                   ,      max: 0                   
              max_qos   : 0                   , max_dflt: 0                   
              share     : 1
              plevel    : 0, priority: 65535
              defer_obj_refcnt: 0
            Statistics:
              tail drops  (bytes): 0                   ,          (packets): 0                   
              total enqs  (bytes): 46447411            ,          (packets): 670805              
              queue_depth (bytes): 0                   
              licensed throughput oversubscription drops:
                          (bytes): 0                   ,          (packets): 0                   
          Queue specifics:
            Index 1 (Queue ID:0x8a, Name: i2l_if_3_cpp_0_prio1)
            Software Control Info:
              (cache) queue id: 0x0000008a, wred: 0x88b168c2, qlimit (bytes): 3125056
              parent_sid: 0x264, debug_name: i2l_if_3_cpp_0_prio1
              sw_flags: 0x18000001, sw_state: 0x00000c01, port_uidb: 245757
              orig_min  : 0                   ,      min: 0                   
              min_qos   : 0                   , min_dflt: 0                   
              orig_max  : 0                   ,      max: 0                   
              max_qos   : 0                   , max_dflt: 0                   
              share     : 0
              plevel    : 1, priority: 0
              defer_obj_refcnt: 0
            Statistics:
              tail drops  (bytes): 0                   ,          (packets): 0                   
              total enqs  (bytes): 269658370           ,          (packets): 1424992             
              queue_depth (bytes): 0                   
              licensed throughput oversubscription drops:
                          (bytes): 0                   ,          (packets): 0                   

        Interface: internal0/0/crypto:0 QFP: 0.0 if_h: 4 Num Queues/Schedules: 2
          Queue specifics:
            Index 0 (Queue ID:0x8b, Name: i2l_if_4_cpp_0_prio0)
            Software Control Info:
              (cache) queue id: 0x0000008b, wred: 0x88b168f1, qlimit (bytes): 80000064
              parent_sid: 0x265, debug_name: i2l_if_4_cpp_0_prio0
              sw_flags: 0x08001001, sw_state: 0x00000c01, port_uidb: 245756
              orig_min  : 0                   ,      min: 0                   
              min_qos   : 0                   , min_dflt: 0                   
              orig_max  : 0                   ,      max: 0                   
              max_qos   : 0                   , max_dflt: 0                   
              share     : 1
              plevel    : 0, priority: 65535
              defer_obj_refcnt: 0
            Statistics:
              tail drops  (bytes): 0                   ,          (packets): 0                   
              total enqs  (bytes): 0                   ,          (packets): 0                   
              queue_depth (bytes): 0                   
              licensed throughput oversubscription drops:
                          (bytes): 0                   ,          (packets): 0                   
          Queue specifics:
            Index 1 (Queue ID:0x8c, Name: i2l_if_4_cpp_0_prio1)
            Software Control Info:
              (cache) queue id: 0x0000008c, wred: 0x88b16901, qlimit (bytes): 80000064
              parent_sid: 0x266, debug_name: i2l_if_4_cpp_0_prio1
              sw_flags: 0x18001001, sw_state: 0x00000c01, port_uidb: 245756
              orig_min  : 0                   ,      min: 0                   
              min_qos   : 0                   , min_dflt: 0                   
              orig_max  : 0                   ,      max: 0                   
              max_qos   : 0                   , max_dflt: 0                   
              share     : 0
              plevel    : 1, priority: 0
              defer_obj_refcnt: 0
            Statistics:
              tail drops  (bytes): 0                   ,          (packets): 0                   
              total enqs  (bytes): 0                   ,          (packets): 0                   
              queue_depth (bytes): 0                   
              licensed throughput oversubscription drops:
                          (bytes): 0                   ,          (packets): 0                   

        Interface: CPP_Null QFP: 0.0 if_h: 5 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: Null0 QFP: 0.0 if_h: 6 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/0 QFP: 0.0 if_h: 7 Num Queues/Schedules: 1
          Queue specifics:
            Index 0 (Queue ID:0x8d, Name: GigabitEthernet0/0/0)
            Software Control Info:
              (cache) queue id: 0x0000008d, wred: 0x88b16932, qlimit (bytes): 3281312
              parent_sid: 0x268, debug_name: GigabitEthernet0/0/0
              sw_flags: 0x08000011, sw_state: 0x00000c01, port_uidb: 245753
              orig_min  : 0                   ,      min: 105000000           
              min_qos   : 0                   , min_dflt: 0                   
              orig_max  : 0                   ,      max: 0                   
              max_qos   : 0                   , max_dflt: 0                   
              share     : 1
              plevel    : 0, priority: 65535
              defer_obj_refcnt: 0
            Statistics:
              tail drops  (bytes): 0                   ,          (packets): 0                   
              total enqs  (bytes): 103120085           ,          (packets): 518314              
              queue_depth (bytes): 0                   
              licensed throughput oversubscription drops:
                          (bytes): 0                   ,          (packets): 0                   

        Interface: GigabitEthernet0/0/1 QFP: 0.0 if_h: 8 Num Queues/Schedules: 1
          Queue specifics:
            Index 0 (Queue ID:0x8e, Name: GigabitEthernet0/0/1)
            Software Control Info:
              (cache) queue id: 0x0000008e, wred: 0x88b16942, qlimit (bytes): 3281312
              parent_sid: 0x269, debug_name: GigabitEthernet0/0/1
              sw_flags: 0x08000011, sw_state: 0x00000c01, port_uidb: 245752
              orig_min  : 0                   ,      min: 105000000           
              min_qos   : 0                   , min_dflt: 0                   
              orig_max  : 0                   ,      max: 0                   
              max_qos   : 0                   , max_dflt: 0                   
              share     : 1
              plevel    : 0, priority: 65535
              defer_obj_refcnt: 0
            Statistics:
              tail drops  (bytes): 0                   ,          (packets): 0                   
              total enqs  (bytes): 649104074           ,          (packets): 7688841             
              queue_depth (bytes): 0                   
              licensed throughput oversubscription drops:
                          (bytes): 0                   ,          (packets): 0                   

        Interface: GigabitEthernet0/0/2 QFP: 0.0 if_h: 9 Num Queues/Schedules: 1
          Queue specifics:
            Index 0 (Queue ID:0x8f, Name: GigabitEthernet0/0/2)
            Software Control Info:
              (cache) queue id: 0x0000008f, wred: 0x88b16952, qlimit (bytes): 3281312
              parent_sid: 0x26a, debug_name: GigabitEthernet0/0/2
              sw_flags: 0x08000011, sw_state: 0x00000c01, port_uidb: 245751
              orig_min  : 0                   ,      min: 105000000           
              min_qos   : 0                   , min_dflt: 0                   
              orig_max  : 0                   ,      max: 0                   
              max_qos   : 0                   , max_dflt: 0                   
              share     : 1
              plevel    : 0, priority: 65535
              defer_obj_refcnt: 0
            Statistics:
              tail drops  (bytes): 0                   ,          (packets): 0                   
              total enqs  (bytes): 779830              ,          (packets): 10261               
              queue_depth (bytes): 0                   
              licensed throughput oversubscription drops:
                          (bytes): 0                   ,          (packets): 0                   

        Interface: GigabitEthernet0/0/3 QFP: 0.0 if_h: 10 Num Queues/Schedules: 1
          Queue specifics:
            Index 0 (Queue ID:0x90, Name: GigabitEthernet0/0/3)
            Software Control Info:
              (cache) queue id: 0x00000090, wred: 0x88b16962, qlimit (bytes): 3281312
              parent_sid: 0x26b, debug_name: GigabitEthernet0/0/3
              sw_flags: 0x08000011, sw_state: 0x00000c01, port_uidb: 245750
              orig_min  : 0                   ,      min: 105000000           
              min_qos   : 0                   , min_dflt: 0                   
              orig_max  : 0                   ,      max: 0                   
              max_qos   : 0                   , max_dflt: 0                   
              share     : 1
              plevel    : 0, priority: 65535
              defer_obj_refcnt: 0
            Statistics:
              tail drops  (bytes): 0                   ,          (packets): 0                   
              total enqs  (bytes): 5698                ,          (packets): 74                  
              queue_depth (bytes): 0                   
              licensed throughput oversubscription drops:
                          (bytes): 0                   ,          (packets): 0                   

        Interface: GigabitEthernet0/0/4 QFP: 0.0 if_h: 11 Num Queues/Schedules: 1
          Queue specifics:
            Index 0 (Queue ID:0x91, Name: GigabitEthernet0/0/4)
            Software Control Info:
              (cache) queue id: 0x00000091, wred: 0x88b16972, qlimit (bytes): 3281312
              parent_sid: 0x26c, debug_name: GigabitEthernet0/0/4
              sw_flags: 0x08000011, sw_state: 0x00000c01, port_uidb: 245749
              orig_min  : 0                   ,      min: 105000000           
              min_qos   : 0                   , min_dflt: 0                   
              orig_max  : 0                   ,      max: 0                   
              max_qos   : 0                   , max_dflt: 0                   
              share     : 1
              plevel    : 0, priority: 65535
              defer_obj_refcnt: 0
            Statistics:
              tail drops  (bytes): 0                   ,          (packets): 0                   
              total enqs  (bytes): 2754752998          ,          (packets): 2765893             
              queue_depth (bytes): 0                   
              licensed throughput oversubscription drops:
                          (bytes): 0                   ,          (packets): 0                   

        Interface: GigabitEthernet0/0/5 QFP: 0.0 if_h: 12 Num Queues/Schedules: 1
          Queue specifics:
            Index 0 (Queue ID:0x92, Name: GigabitEthernet0/0/5)
            Software Control Info:
              (cache) queue id: 0x00000092, wred: 0x88b16982, qlimit (bytes): 3281312
              parent_sid: 0x26d, debug_name: GigabitEthernet0/0/5
              sw_flags: 0x08000011, sw_state: 0x00000c01, port_uidb: 245748
              orig_min  : 0                   ,      min: 105000000           
              min_qos   : 0                   , min_dflt: 0                   
              orig_max  : 0                   ,      max: 0                   
              max_qos   : 0                   , max_dflt: 0                   
              share     : 1
              plevel    : 0, priority: 65535
              defer_obj_refcnt: 0
            Statistics:
              tail drops  (bytes): 0                   ,          (packets): 0                   
              total enqs  (bytes): 2754752998          ,          (packets): 2765893             
              queue_depth (bytes): 0                   
              licensed throughput oversubscription drops:
                          (bytes): 0                   ,          (packets): 0                   

        Interface: GigabitEthernet0/0/6 QFP: 0.0 if_h: 13 Num Queues/Schedules: 1
          Queue specifics:
            Index 0 (Queue ID:0x93, Name: GigabitEthernet0/0/6)
            Software Control Info:
              (cache) queue id: 0x00000093, wred: 0x88b16992, qlimit (bytes): 3281312
              parent_sid: 0x26e, debug_name: GigabitEthernet0/0/6
              sw_flags: 0x08000011, sw_state: 0x00000c01, port_uidb: 245747
              orig_min  : 0                   ,      min: 105000000           
              min_qos   : 0                   , min_dflt: 0                   
              orig_max  : 0                   ,      max: 0                   
              max_qos   : 0                   , max_dflt: 0                   
              share     : 1
              plevel    : 0, priority: 65535
              defer_obj_refcnt: 0
            Statistics:
              tail drops  (bytes): 0                   ,          (packets): 0                   
              total enqs  (bytes): 5998                ,          (packets): 79                  
              queue_depth (bytes): 0                   
              licensed throughput oversubscription drops:
                          (bytes): 0                   ,          (packets): 0                   

        Interface: GigabitEthernet0/0/7 QFP: 0.0 if_h: 14 Num Queues/Schedules: 1
          Queue specifics:
            Index 0 (Queue ID:0x94, Name: GigabitEthernet0/0/7)
            Software Control Info:
              (cache) queue id: 0x00000094, wred: 0x88b169a2, qlimit (bytes): 3281312
              parent_sid: 0x270, debug_name: GigabitEthernet0/0/7
              sw_flags: 0x08000011, sw_state: 0x00000c01, port_uidb: 245746
              orig_min  : 0                   ,      min: 105000000           
              min_qos   : 0                   , min_dflt: 0                   
              orig_max  : 0                   ,      max: 0                   
              max_qos   : 0                   , max_dflt: 0                   
              share     : 1
              plevel    : 0, priority: 65535
              defer_obj_refcnt: 0
            Statistics:
              tail drops  (bytes): 0                   ,          (packets): 0                   
              total enqs  (bytes): 0                   ,          (packets): 0                   
              queue_depth (bytes): 0                   
              licensed throughput oversubscription drops:
                          (bytes): 0                   ,          (packets): 0                   

        Interface: GigabitEthernet0/1/0 QFP: 0.0 if_h: 15 Num Queues/Schedules: 1
          Queue specifics:
            Index 0 (Queue ID:0x95, Name: GigabitEthernet0/1/0)
            Software Control Info:
              (cache) queue id: 0x00000095, wred: 0x88b169b2, qlimit (bytes): 3281312
              parent_sid: 0x271, debug_name: GigabitEthernet0/1/0
              sw_flags: 0x08000011, sw_state: 0x00000c01, port_uidb: 245745
              orig_min  : 0                   ,      min: 105000000           
              min_qos   : 0                   , min_dflt: 0                   
              orig_max  : 0                   ,      max: 0                   
              max_qos   : 0                   , max_dflt: 0                   
              share     : 1
              plevel    : 0, priority: 65535
              defer_obj_refcnt: 0
            Statistics:
              tail drops  (bytes): 0                   ,          (packets): 0                   
              total enqs  (bytes): 0                   ,          (packets): 0                   
              queue_depth (bytes): 0                   
              licensed throughput oversubscription drops:
                          (bytes): 0                   ,          (packets): 0                   

        Interface: GigabitEthernet0/1/1 QFP: 0.0 if_h: 16 Num Queues/Schedules: 1
          Queue specifics:
            Index 0 (Queue ID:0x96, Name: GigabitEthernet0/1/1)
            Software Control Info:
              (cache) queue id: 0x00000096, wred: 0x88b169c2, qlimit (bytes): 3281312
              parent_sid: 0x272, debug_name: GigabitEthernet0/1/1
              sw_flags: 0x08000011, sw_state: 0x00000c01, port_uidb: 245744
              orig_min  : 0                   ,      min: 105000000           
              min_qos   : 0                   , min_dflt: 0                   
              orig_max  : 0                   ,      max: 0                   
              max_qos   : 0                   , max_dflt: 0                   
              share     : 1
              plevel    : 0, priority: 65535
              defer_obj_refcnt: 0
            Statistics:
              tail drops  (bytes): 0                   ,          (packets): 0                   
              total enqs  (bytes): 0                   ,          (packets): 0                   
              queue_depth (bytes): 0                   
              licensed throughput oversubscription drops:
                          (bytes): 0                   ,          (packets): 0                   

        Interface: GigabitEthernet0/1/2 QFP: 0.0 if_h: 17 Num Queues/Schedules: 1
          Queue specifics:
            Index 0 (Queue ID:0x97, Name: GigabitEthernet0/1/2)
            Software Control Info:
              (cache) queue id: 0x00000097, wred: 0x88b169d2, qlimit (bytes): 3281312
              parent_sid: 0x273, debug_name: GigabitEthernet0/1/2
              sw_flags: 0x08000011, sw_state: 0x00000c01, port_uidb: 245743
              orig_min  : 0                   ,      min: 105000000           
              min_qos   : 0                   , min_dflt: 0                   
              orig_max  : 0                   ,      max: 0                   
              max_qos   : 0                   , max_dflt: 0                   
              share     : 1
              plevel    : 0, priority: 65535
              defer_obj_refcnt: 0
            Statistics:
              tail drops  (bytes): 0                   ,          (packets): 0                   
              total enqs  (bytes): 0                   ,          (packets): 0                   
              queue_depth (bytes): 0                   
              licensed throughput oversubscription drops:
                          (bytes): 0                   ,          (packets): 0                   

        Interface: GigabitEthernet0/1/3 QFP: 0.0 if_h: 18 Num Queues/Schedules: 1
          Queue specifics:
            Index 0 (Queue ID:0x98, Name: GigabitEthernet0/1/3)
            Software Control Info:
              (cache) queue id: 0x00000098, wred: 0x88b169e2, qlimit (bytes): 3281312
              parent_sid: 0x274, debug_name: GigabitEthernet0/1/3
              sw_flags: 0x08000011, sw_state: 0x00000c01, port_uidb: 245742
              orig_min  : 0                   ,      min: 105000000           
              min_qos   : 0                   , min_dflt: 0                   
              orig_max  : 0                   ,      max: 0                   
              max_qos   : 0                   , max_dflt: 0                   
              share     : 1
              plevel    : 0, priority: 65535
              defer_obj_refcnt: 0
            Statistics:
              tail drops  (bytes): 0                   ,          (packets): 0                   
              total enqs  (bytes): 0                   ,          (packets): 0                   
              queue_depth (bytes): 0                   
              licensed throughput oversubscription drops:
                          (bytes): 0                   ,          (packets): 0                   

        Interface: GigabitEthernet0/1/4 QFP: 0.0 if_h: 19 Num Queues/Schedules: 1
          Queue specifics:
            Index 0 (Queue ID:0x99, Name: GigabitEthernet0/1/4)
            Software Control Info:
              (cache) queue id: 0x00000099, wred: 0x88b169f2, qlimit (bytes): 3281312
              parent_sid: 0x275, debug_name: GigabitEthernet0/1/4
              sw_flags: 0x08000011, sw_state: 0x00000c01, port_uidb: 245741
              orig_min  : 0                   ,      min: 105000000           
              min_qos   : 0                   , min_dflt: 0                   
              orig_max  : 0                   ,      max: 0                   
              max_qos   : 0                   , max_dflt: 0                   
              share     : 1
              plevel    : 0, priority: 65535
              defer_obj_refcnt: 0
            Statistics:
              tail drops  (bytes): 0                   ,          (packets): 0                   
              total enqs  (bytes): 0                   ,          (packets): 0                   
              queue_depth (bytes): 0                   
              licensed throughput oversubscription drops:
                          (bytes): 0                   ,          (packets): 0                   

        Interface: GigabitEthernet0/1/5 QFP: 0.0 if_h: 20 Num Queues/Schedules: 1
          Queue specifics:
            Index 0 (Queue ID:0x9a, Name: GigabitEthernet0/1/5)
            Software Control Info:
              (cache) queue id: 0x0000009a, wred: 0x88b16a02, qlimit (bytes): 3281312
              parent_sid: 0x276, debug_name: GigabitEthernet0/1/5
              sw_flags: 0x08000011, sw_state: 0x00000c01, port_uidb: 245740
              orig_min  : 0                   ,      min: 105000000           
              min_qos   : 0                   , min_dflt: 0                   
              orig_max  : 0                   ,      max: 0                   
              max_qos   : 0                   , max_dflt: 0                   
              share     : 1
              plevel    : 0, priority: 65535
              defer_obj_refcnt: 0
            Statistics:
              tail drops  (bytes): 0                   ,          (packets): 0                   
              total enqs  (bytes): 0                   ,          (packets): 0                   
              queue_depth (bytes): 0                   
              licensed throughput oversubscription drops:
                          (bytes): 0                   ,          (packets): 0                   

        Interface: GigabitEthernet0/1/6 QFP: 0.0 if_h: 21 Num Queues/Schedules: 1
          Queue specifics:
            Index 0 (Queue ID:0x9b, Name: GigabitEthernet0/1/6)
            Software Control Info:
              (cache) queue id: 0x0000009b, wred: 0x88b16a12, qlimit (bytes): 3281312
              parent_sid: 0x278, debug_name: GigabitEthernet0/1/6
              sw_flags: 0x08000011, sw_state: 0x00000c01, port_uidb: 245739
              orig_min  : 0                   ,      min: 105000000           
              min_qos   : 0                   , min_dflt: 0                   
              orig_max  : 0                   ,      max: 0                   
              max_qos   : 0                   , max_dflt: 0                   
              share     : 1
              plevel    : 0, priority: 65535
              defer_obj_refcnt: 0
            Statistics:
              tail drops  (bytes): 0                   ,          (packets): 0                   
              total enqs  (bytes): 0                   ,          (packets): 0                   
              queue_depth (bytes): 0                   
              licensed throughput oversubscription drops:
                          (bytes): 0                   ,          (packets): 0        

        Interface: GigabitEthernet0/1/7 QFP: 0.0 if_h: 22 Num Queues/Schedules: 1
          Queue specifics:
            Index 0 (Queue ID:0x9c, Name: GigabitEthernet0/1/7)
            Software Control Info:
              (cache) queue id: 0x0000009c, wred: 0x88b16a22, qlimit (bytes): 3281312
              parent_sid: 0x279, debug_name: GigabitEthernet0/1/7
              sw_flags: 0x08000011, sw_state: 0x00000c01, port_uidb: 245738
              orig_min  : 0                   ,      min: 105000000           
              min_qos   : 0                   , min_dflt: 0                   
              orig_max  : 0                   ,      max: 0                   
              max_qos   : 0                   , max_dflt: 0                   
              share     : 1
              plevel    : 0, priority: 65535
              defer_obj_refcnt: 0
            Statistics:
              tail drops  (bytes): 0                   ,          (packets): 0                   
              total enqs  (bytes): 0                   ,          (packets): 0                   
              queue_depth (bytes): 0                   
              licensed throughput oversubscription drops:
                          (bytes): 0                   ,          (packets): 0                   

        Interface: TenGigabitEthernet0/2/0 QFP: 0.0 if_h: 23 Num Queues/Schedules: 1
          Queue specifics:
            Index 0 (Queue ID:0x9d, Name: TenGigabitEthernet0/2/0)
            Software Control Info:
              (cache) queue id: 0x0000009d, wred: 0x88b16a32, qlimit (bytes): 32812544
              parent_sid: 0x27a, debug_name: TenGigabitEthernet0/2/0
              sw_flags: 0x08000011, sw_state: 0x00000c01, port_uidb: 245737
              orig_min  : 0                   ,      min: 1050000000          
              min_qos   : 0                   , min_dflt: 0                   
              orig_max  : 0                   ,      max: 0                   
              max_qos   : 0                   , max_dflt: 0                   
              share     : 1
              plevel    : 0, priority: 65535
              defer_obj_refcnt: 0
            Statistics:
              tail drops  (bytes): 0                   ,          (packets): 0                   
              total enqs  (bytes): 0                   ,          (packets): 0                   
              queue_depth (bytes): 0                   
              licensed throughput oversubscription drops:
                          (bytes): 0                   ,          (packets): 0                   

        Interface: TenGigabitEthernet0/3/0 QFP: 0.0 if_h: 24 Num Queues/Schedules: 1
          Queue specifics:
            Index 0 (Queue ID:0x9e, Name: TenGigabitEthernet0/3/0)
            Software Control Info:
              (cache) queue id: 0x0000009e, wred: 0x88b16a42, qlimit (bytes): 32812544
              parent_sid: 0x27b, debug_name: TenGigabitEthernet0/3/0
              sw_flags: 0x08000011, sw_state: 0x00000c01, port_uidb: 245736
              orig_min  : 0                   ,      min: 1050000000          
              min_qos   : 0                   , min_dflt: 0                   
              orig_max  : 0                   ,      max: 0                   
              max_qos   : 0                   , max_dflt: 0                   
              share     : 1
              plevel    : 0, priority: 65535
              defer_obj_refcnt: 0
            Statistics:
              tail drops  (bytes): 0                   ,          (packets): 0                   
              total enqs  (bytes): 0                   ,          (packets): 0                   
              queue_depth (bytes): 0                   
              licensed throughput oversubscription drops:
                          (bytes): 0                   ,          (packets): 0                   

        Interface: GigabitEthernet1/0/0 QFP: 0.0 if_h: 25 Num Queues/Schedules: 1
          Queue specifics:
            Index 0 (Queue ID:0x9f, Name: GigabitEthernet1/0/0)
            Software Control Info:
              (cache) queue id: 0x0000009f, wred: 0x88b16a52, qlimit (bytes): 3281312
              parent_sid: 0x27c, debug_name: GigabitEthernet1/0/0
              sw_flags: 0x08000011, sw_state: 0x00000c01, port_uidb: 245735
              orig_min  : 0                   ,      min: 105000000           
              min_qos   : 0                   , min_dflt: 0                   
              orig_max  : 0                   ,      max: 0                   
              max_qos   : 0                   , max_dflt: 0                   
              share     : 1
              plevel    : 0, priority: 65535
              defer_obj_refcnt: 0
            Statistics:
              tail drops  (bytes): 0                   ,          (packets): 0                   
              total enqs  (bytes): 0                   ,          (packets): 0                   
              queue_depth (bytes): 0                   
              licensed throughput oversubscription drops:
                          (bytes): 0                   ,          (packets): 0                   

        Interface: GigabitEthernet1/0/1 QFP: 0.0 if_h: 26 Num Queues/Schedules: 1
          Queue specifics:
            Index 0 (Queue ID:0xa0, Name: GigabitEthernet1/0/1)
            Software Control Info:
              (cache) queue id: 0x000000a0, wred: 0x88b16a62, qlimit (bytes): 3281312
              parent_sid: 0x27d, debug_name: GigabitEthernet1/0/1
              sw_flags: 0x08000011, sw_state: 0x00000c01, port_uidb: 245734
              orig_min  : 0                   ,      min: 105000000           
              min_qos   : 0                   , min_dflt: 0                   
              orig_max  : 0                   ,      max: 0                   
              max_qos   : 0                   , max_dflt: 0                   
              share     : 1
              plevel    : 0, priority: 65535
              defer_obj_refcnt: 0
            Statistics:
              tail drops  (bytes): 0                   ,          (packets): 0                   
              total enqs  (bytes): 0                   ,          (packets): 0                   
              queue_depth (bytes): 0                   
              licensed throughput oversubscription drops:
                          (bytes): 0                   ,          (packets): 0                   

        Interface: GigabitEthernet1/0/2 QFP: 0.0 if_h: 27 Num Queues/Schedules: 1
          Queue specifics:
            Index 0 (Queue ID:0xa1, Name: GigabitEthernet1/0/2)
            Software Control Info:
              (cache) queue id: 0x000000a1, wred: 0x88b16a72, qlimit (bytes): 3281312
              parent_sid: 0x27e, debug_name: GigabitEthernet1/0/2
              sw_flags: 0x08000011, sw_state: 0x00000c01, port_uidb: 245733
              orig_min  : 0                   ,      min: 105000000           
              min_qos   : 0                   , min_dflt: 0                   
              orig_max  : 0                   ,      max: 0                   
              max_qos   : 0                   , max_dflt: 0                   
              share     : 1
              plevel    : 0, priority: 65535
              defer_obj_refcnt: 0
            Statistics:
              tail drops  (bytes): 0                   ,          (packets): 0                   
              total enqs  (bytes): 0                   ,          (packets): 0                   
              queue_depth (bytes): 0                   
              licensed throughput oversubscription drops:
                          (bytes): 0                   ,          (packets): 0                   

        Interface: GigabitEthernet1/0/3 QFP: 0.0 if_h: 28 Num Queues/Schedules: 1
          Queue specifics:
            Index 0 (Queue ID:0xa2, Name: GigabitEthernet1/0/3)
            Software Control Info:
              (cache) queue id: 0x000000a2, wred: 0x88b16a82, qlimit (bytes): 3281312
              parent_sid: 0x280, debug_name: GigabitEthernet1/0/3
              sw_flags: 0x08000011, sw_state: 0x00000c01, port_uidb: 245732
              orig_min  : 0                   ,      min: 105000000           
              min_qos   : 0                   , min_dflt: 0                   
              orig_max  : 0                   ,      max: 0                   
              max_qos   : 0                   , max_dflt: 0                   
              share     : 1
              plevel    : 0, priority: 65535
              defer_obj_refcnt: 0
            Statistics:
              tail drops  (bytes): 0                   ,          (packets): 0                   
              total enqs  (bytes): 0                   ,          (packets): 0                   
              queue_depth (bytes): 0                   
              licensed throughput oversubscription drops:
                          (bytes): 0                   ,          (packets): 0                   

        Interface: GigabitEthernet1/0/4 QFP: 0.0 if_h: 29 Num Queues/Schedules: 1
          Queue specifics:
            Index 0 (Queue ID:0xa3, Name: GigabitEthernet1/0/4)
            Software Control Info:
              (cache) queue id: 0x000000a3, wred: 0x88b16a92, qlimit (bytes): 3281312
              parent_sid: 0x281, debug_name: GigabitEthernet1/0/4
              sw_flags: 0x08000011, sw_state: 0x00000c01, port_uidb: 245731
              orig_min  : 0                   ,      min: 105000000           
              min_qos   : 0                   , min_dflt: 0                   
              orig_max  : 0                   ,      max: 0                   
              max_qos   : 0                   , max_dflt: 0                   
              share     : 1
              plevel    : 0, priority: 65535
              defer_obj_refcnt: 0
            Statistics:
              tail drops  (bytes): 0                   ,          (packets): 0                   
              total enqs  (bytes): 0                   ,          (packets): 0                   
              queue_depth (bytes): 0                   
              licensed throughput oversubscription drops:
                          (bytes): 0                   ,          (packets): 0                   

        Interface: GigabitEthernet1/0/5 QFP: 0.0 if_h: 30 Num Queues/Schedules: 1
          Queue specifics:
            Index 0 (Queue ID:0xa4, Name: GigabitEthernet1/0/5)
            Software Control Info:
              (cache) queue id: 0x000000a4, wred: 0x88b16aa2, qlimit (bytes): 3281312
              parent_sid: 0x282, debug_name: GigabitEthernet1/0/5
              sw_flags: 0x08000011, sw_state: 0x00000c01, port_uidb: 245730
              orig_min  : 0                   ,      min: 105000000           
              min_qos   : 0                   , min_dflt: 0                   
              orig_max  : 0                   ,      max: 0                   
              max_qos   : 0                   , max_dflt: 0                   
              share     : 1
              plevel    : 0, priority: 65535
              defer_obj_refcnt: 0
            Statistics:
              tail drops  (bytes): 0                   ,          (packets): 0                   
              total enqs  (bytes): 0                   ,          (packets): 0                   
              queue_depth (bytes): 0                   
              licensed throughput oversubscription drops:
                          (bytes): 0                   ,          (packets): 0                   

        Interface: GigabitEthernet1/0/6 QFP: 0.0 if_h: 31 Num Queues/Schedules: 1
          Queue specifics:
            Index 0 (Queue ID:0xa5, Name: GigabitEthernet1/0/6)
            Software Control Info:
              (cache) queue id: 0x000000a5, wred: 0x88b16ab2, qlimit (bytes): 3281312
              parent_sid: 0x283, debug_name: GigabitEthernet1/0/6
              sw_flags: 0x08000011, sw_state: 0x00000c01, port_uidb: 245729
              orig_min  : 0                   ,      min: 105000000           
              min_qos   : 0                   , min_dflt: 0                   
              orig_max  : 0                   ,      max: 0                   
              max_qos   : 0                   , max_dflt: 0                   
              share     : 1
              plevel    : 0, priority: 65535
              defer_obj_refcnt: 0
            Statistics:
              tail drops  (bytes): 0                   ,          (packets): 0                   
              total enqs  (bytes): 0                   ,          (packets): 0                   
              queue_depth (bytes): 0                   
              licensed throughput oversubscription drops:
                          (bytes): 0                   ,          (packets): 0                   

        Interface: GigabitEthernet1/0/7 QFP: 0.0 if_h: 32 Num Queues/Schedules: 1
          Queue specifics:
            Index 0 (Queue ID:0xa6, Name: GigabitEthernet1/0/7)
            Software Control Info:
              (cache) queue id: 0x000000a6, wred: 0x88b16ac2, qlimit (bytes): 3281312
              parent_sid: 0x284, debug_name: GigabitEthernet1/0/7
              sw_flags: 0x08000011, sw_state: 0x00000c01, port_uidb: 245728
              orig_min  : 0                   ,      min: 105000000           
              min_qos   : 0                   , min_dflt: 0                   
              orig_max  : 0                   ,      max: 0                   
              max_qos   : 0                   , max_dflt: 0                   
              share     : 1
              plevel    : 0, priority: 65535
              defer_obj_refcnt: 0
            Statistics:
              tail drops  (bytes): 0                   ,          (packets): 0                   
              total enqs  (bytes): 0                   ,          (packets): 0                   
              queue_depth (bytes): 0                   
              licensed throughput oversubscription drops:
                          (bytes): 0                   ,          (packets): 0                   

        Interface: Loopback0 QFP: 0.0 if_h: 33 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: Loopback2 QFP: 0.0 if_h: 34 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.2 QFP: 0.0 if_h: 35 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.EFP2054 QFP: 0.0 if_h: 36 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.11 QFP: 0.0 if_h: 37 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.12 QFP: 0.0 if_h: 38 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.13 QFP: 0.0 if_h: 39 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.14 QFP: 0.0 if_h: 40 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.15 QFP: 0.0 if_h: 41 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.16 QFP: 0.0 if_h: 42 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.17 QFP: 0.0 if_h: 43 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.18 QFP: 0.0 if_h: 44 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.19 QFP: 0.0 if_h: 45 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.20 QFP: 0.0 if_h: 46 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.21 QFP: 0.0 if_h: 47 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.22 QFP: 0.0 if_h: 48 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.23 QFP: 0.0 if_h: 49 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.24 QFP: 0.0 if_h: 50 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.25 QFP: 0.0 if_h: 51 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.26 QFP: 0.0 if_h: 52 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.27 QFP: 0.0 if_h: 53 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.28 QFP: 0.0 if_h: 54 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.29 QFP: 0.0 if_h: 55 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.30 QFP: 0.0 if_h: 56 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.31 QFP: 0.0 if_h: 57 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.32 QFP: 0.0 if_h: 58 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.33 QFP: 0.0 if_h: 59 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.34 QFP: 0.0 if_h: 60 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.35 QFP: 0.0 if_h: 61 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.36 QFP: 0.0 if_h: 62 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.37 QFP: 0.0 if_h: 63 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.38 QFP: 0.0 if_h: 64 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.57 QFP: 0.0 if_h: 83 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.58 QFP: 0.0 if_h: 84 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.59 QFP: 0.0 if_h: 85 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.60 QFP: 0.0 if_h: 86 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.61 QFP: 0.0 if_h: 87 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.62 QFP: 0.0 if_h: 88 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.63 QFP: 0.0 if_h: 89 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.400 QFP: 0.0 if_h: 426 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.401 QFP: 0.0 if_h: 427 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.402 QFP: 0.0 if_h: 428 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.403 QFP: 0.0 if_h: 429 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.404 QFP: 0.0 if_h: 430 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.405 QFP: 0.0 if_h: 431 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.406 QFP: 0.0 if_h: 432 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.407 QFP: 0.0 if_h: 433 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.408 QFP: 0.0 if_h: 434 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.409 QFP: 0.0 if_h: 435 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.410 QFP: 0.0 if_h: 436 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.411 QFP: 0.0 if_h: 437 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.412 QFP: 0.0 if_h: 438 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.413 QFP: 0.0 if_h: 439 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.414 QFP: 0.0 if_h: 440 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.415 QFP: 0.0 if_h: 441 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.416 QFP: 0.0 if_h: 442 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.417 QFP: 0.0 if_h: 443 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.418 QFP: 0.0 if_h: 444 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.419 QFP: 0.0 if_h: 445 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.420 QFP: 0.0 if_h: 446 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.421 QFP: 0.0 if_h: 447 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.422 QFP: 0.0 if_h: 448 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.423 QFP: 0.0 if_h: 449 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.424 QFP: 0.0 if_h: 450 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.425 QFP: 0.0 if_h: 451 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.426 QFP: 0.0 if_h: 452 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.427 QFP: 0.0 if_h: 453 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.428 QFP: 0.0 if_h: 454 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.429 QFP: 0.0 if_h: 455 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.430 QFP: 0.0 if_h: 456 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.431 QFP: 0.0 if_h: 457 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.432 QFP: 0.0 if_h: 458 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.433 QFP: 0.0 if_h: 459 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.434 QFP: 0.0 if_h: 460 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.720 QFP: 0.0 if_h: 746 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.721 QFP: 0.0 if_h: 747 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.722 QFP: 0.0 if_h: 748 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.723 QFP: 0.0 if_h: 749 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.724 QFP: 0.0 if_h: 750 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.725 QFP: 0.0 if_h: 751 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.726 QFP: 0.0 if_h: 752 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.727 QFP: 0.0 if_h: 753 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.728 QFP: 0.0 if_h: 754 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.729 QFP: 0.0 if_h: 755 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.730 QFP: 0.0 if_h: 756 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.731 QFP: 0.0 if_h: 757 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.732 QFP: 0.0 if_h: 758 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.733 QFP: 0.0 if_h: 759 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.734 QFP: 0.0 if_h: 760 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.735 QFP: 0.0 if_h: 761 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.736 QFP: 0.0 if_h: 762 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.737 QFP: 0.0 if_h: 763 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.738 QFP: 0.0 if_h: 764 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.1795 QFP: 0.0 if_h: 1821 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.1796 QFP: 0.0 if_h: 1822 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/1.1797 QFP: 0.0 if_h: 1823 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/3.EFP2051 QFP: 0.0 if_h: 2077 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/3.EFP2052 QFP: 0.0 if_h: 2078 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/3.EFP2053 QFP: 0.0 if_h: 2079 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/3.EFP2054 QFP: 0.0 if_h: 2080 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/3.EFP2055 QFP: 0.0 if_h: 2081 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/3.EFP2174 QFP: 0.0 if_h: 2200 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/3.EFP2175 QFP: 0.0 if_h: 2201 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/3.EFP2176 QFP: 0.0 if_h: 2202 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/3.EFP2177 QFP: 0.0 if_h: 2203 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/3.EFP2178 QFP: 0.0 if_h: 2204 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: GigabitEthernet0/0/3.EFP2179 QFP: 0.0 if_h: 2205 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: BG4048.10207e1 QFP: 0.0 if_h: 4079 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: VPLS-2944.10207e2 QFP: 0.0 if_h: 4080 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: VPLS-2945.10207e3 QFP: 0.0 if_h: 4081 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: VPLS-2946.10207e4 QFP: 0.0 if_h: 4082 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: VPLS-2974.10207fb QFP: 0.0 if_h: 4105 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: VPLS-2975.10207fc QFP: 0.0 if_h: 4106 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: BG4033.10207fd QFP: 0.0 if_h: 4107 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: BG4044.10207fe QFP: 0.0 if_h: 4108 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: BG4045.10207ff QFP: 0.0 if_h: 4109 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: BG4111.1020807 QFP: 0.0 if_h: 4117 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: BG4117.1020808 QFP: 0.0 if_h: 4118 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: BG4118.1020809 QFP: 0.0 if_h: 4119 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: VPLS-2816.102080a QFP: 0.0 if_h: 4120 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: VPLS-2817.102080b QFP: 0.0 if_h: 4121 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: VPLS-2818.102080c QFP: 0.0 if_h: 4122 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: VPLS-2819.102080d QFP: 0.0 if_h: 4123 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: VPLS-2820.102080e QFP: 0.0 if_h: 4124 Num Queues/Schedules: 0
          No Queue/Schedule Info
        Interface: VPLS-3049.1020890 QFP: 0.0 if_h: 4254 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: VPLS-3050.1020891 QFP: 0.0 if_h: 4255 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: BG4001.1020892 QFP: 0.0 if_h: 4256 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: BG4002.1020893 QFP: 0.0 if_h: 4257 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: BG4006.1020894 QFP: 0.0 if_h: 4258 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: BG4010.1020895 QFP: 0.0 if_h: 4259 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: VPLS-2320.1020896 QFP: 0.0 if_h: 4260 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: VPLS-2321.1020897 QFP: 0.0 if_h: 4261 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: VPLS-2322.1020898 QFP: 0.0 if_h: 4262 Num Queues/Schedules: 0
          No Queue/Schedule Info

        Interface: VPLS_maint.1020a6b QFP: 0.0 if_h: 4729 Num Queues/Schedules: 0
          No Queue/Schedule Info
    '''
    }

    golden_parsed_output_interface = {
        "GigabitEthernet4": {
            "if_h": 9,
            "index": {
                "0": {
                    "queue_id": "0x70",
                    "name": "GigabitEthernet4",
                    "software_control_info": {
                        "cache_queue_id": "0x00000070",
                        "wred": "0xe73cfde0",
                        "qlimit_pkts": 418,
                        "parent_sid": "0x8d",
                        "debug_name": "GigabitEthernet4",
                        "sw_flags": "0x08000011",
                        "sw_state": "0x00000c01",
                        "port_uidb": 65527,
                        "orig_min": 0,
                        "min": 105000000,
                        "min_qos": 0,
                        "min_dflt": 0,
                        "orig_max": 0,
                        "max": 0,
                        "max_qos": 0,
                        "max_dflt": 0,
                        "share": 1,
                        "plevel": 0,
                        "priority": 65535,
                        "defer_obj_refcnt": 0
                    },
                    "statistics": {
                        "tail_drops_bytes": 0,
                        "tail_drops_packets": 0,
                        "total_enqs_bytes": 108648448,
                        "total_enqs_packets": 1697632,
                        "queue_depth_pkts": 0,
                        "lic_throughput_oversub_drops_bytes": 0,
                        "lic_throughput_oversub_drops_packets": 0
                    }
                }
            }
        }
    }
    
    golden_output_interface = {'execute.return_value': '''
        Interface: GigabitEthernet4 QFP: 0.0 if_h: 9 Num Queues/Schedules: 1
          Queue specifics:
            Index 0 (Queue ID:0x70, Name: GigabitEthernet4)
            PARQ Software Control Info:
              (cache) queue id: 0x00000070, wred: 0xe73cfde0, qlimit (pkts ): 418
              parent_sid: 0x8d, debug_name: GigabitEthernet4
              sw_flags: 0x08000011, sw_state: 0x00000c01, port_uidb: 65527
              orig_min  : 0                   ,      min: 105000000           
              min_qos   : 0                   , min_dflt: 0                   
              orig_max  : 0                   ,      max: 0                   
              max_qos   : 0                   , max_dflt: 0                   
              share     : 1
              plevel    : 0, priority: 65535
              defer_obj_refcnt: 0
            Statistics:
              tail drops  (bytes): 0                   ,          (packets): 0                   
              total enqs  (bytes): 108648448           ,          (packets): 1697632             
              queue_depth (pkts ): 0                   
              licensed throughput oversubscription drops:
                          (bytes): 0                   ,          (packets): 0     
    '''}

    golden_parsed_output = {
        'TenGigabitEthernet0/0/0': {
            'if_h': 7,
            'index': {
                '0': {
                    'queue_id': '0xcc8',
                    'name': 'TenGigabitEthernet0/0/0',
                    'software_control_info': {
                        'cache_queue_id': '0x00000cc8',
                        'wred': '0x5218622c',
                        'qlimit_bytes': 65625002,
                        'parent_sid': '0x28194',
                        'debug_name': 'TenGigabitEthernet0/0/0',
                        'sw_flags': '0x08000011',
                        'sw_state': '0x00000801',
                        'port_uidb': 262137,
                        'orig_min': 0,
                        'min': 1050000000,
                        'min_qos': 0,
                        'min_dflt': 0,
                        'orig_max': 0,
                        'max': 0,
                        'max_qos': 0,
                        'max_dflt': 0,
                        'share': 1,
                        'plevel': 0,
                        'priority': 65535,
                        'defer_obj_refcnt': 0,
                        'cp_ppe_addr': '0x00000000',
                    },
                    'statistics': {
                        'tail_drops_bytes': 0,
                        'tail_drops_packets': 0,
                        'total_enqs_bytes': 19215977960,
                        'total_enqs_packets': 82176494,
                        'queue_depth_bytes': 0,
                        'lic_throughput_oversub_drops_bytes': 0,
                        'lic_throughput_oversub_drops_packets': 0,
                    },
                },
            },
        },
    }
    golden_output = {'execute.return_value': '''
        show platform hardware qfp active infrastructure bqs queue output default interface TenGigabitEthernet0/0/0
        Load for five secs: 91%/1%; one minute: 83%; five minutes: 65%
        Time source is NTP, 18:30:46.284 EST Wed Oct 16 2019
        
        Interface: TenGigabitEthernet0/0/0 QFP: 0.0 if_h: 7 Num Queues/Schedules: 1
        Queue specifics:
            Index 0 (Queue ID:0xcc8, Name: TenGigabitEthernet0/0/0)
            Software Control Info:
            (cache) queue id: 0x00000cc8, wred: 0x5218622c, qlimit (bytes): 65625002
            parent_sid: 0x28194, debug_name: TenGigabitEthernet0/0/0
            sw_flags: 0x08000011, sw_state: 0x00000801, port_uidb: 262137
            orig_min  : 0                   ,      min: 1050000000         
            min_qos   : 0                   , min_dflt: 0                  
            orig_max  : 0                   ,      max: 0                  
            max_qos   : 0                   , max_dflt: 0                  
            share     : 1
            plevel    : 0, priority: 65535
            defer_obj_refcnt: 0, cp_ppe_addr: 0x00000000
            Statistics:
            tail drops  (bytes): 0                   ,          (packets): 0                  
            total enqs  (bytes): 19215977960         ,          (packets): 82176494           
            queue_depth (bytes): 0                  
            licensed throughput oversubscription drops:
                        (bytes): 0                   ,          (packets): 0    
    '''}

    def test_golden_active(self):
        self.device = Mock(**self.golden_output_active)
        obj = ShowPlatformHardware(device=self.device)
        parsed_output = obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output, self.golden_parsed_output_active)

    def test_golden_interface(self):
        self.device = Mock(**self.golden_output_interface)
        obj = ShowPlatformHardware(device=self.device)
        parsed_output = obj.parse(interface='GigabitEthernet4')
        self.maxDiff = None
        self.assertEqual(parsed_output, self.golden_parsed_output_interface)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowPlatformHardware(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowPlatformHardware(device=self.device)
        parsed_output = obj.parse(interface='TenGigabitEthernet0/0/0')
        self.assertEqual(parsed_output, self.golden_parsed_output)


class TestShowPlatformHardwarePlim(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output_port = {
        'port': {
            '0/0/0': {
                'received': {
                    'high_priority': {
                        'dropped_bytes': 0,
                        'dropped_pkts': 0,
                        'errored_bytes': 0,
                        'errored_pkts': 0,
                        'bytes': 327940189,
                        'pkts': 316215},
                    'low_priority': {
                        'dropped_bytes': 0,
                        'dropped_pkts': 0,
                        'errored_bytes': 0,
                        'errored_pkts': 0,
                        'bytes': 27789,
                        'pkts': 369}
                },
                'transmitted': {
                    'high_priority': {
                        'dropped_bytes': 0,
                        'dropped_pkts': 0,
                        'bytes': 0,
                        'pkts': 0},
                    'low_priority': {
                        'dropped_bytes': 0,
                        'dropped_pkts': 0,
                        'bytes': 250735325722,
                        'pkts': 1265574622}
                }
            }
        }
    }

    golden_output_port = {'execute.return_value': '''\
        Router#show platform hardware port 0/0/0 plim statistics
        Interface 0/0/0
          RX Low Priority
            RX Pkts      369         Bytes 27789      
            RX Drop Pkts 0           Bytes 0          
            RX Err  Pkts 0           Bytes 0          
          TX Low Priority
            TX Pkts      1265574622  Bytes 250735325722
            TX Drop Pkts 0           Bytes 0          
          RX High Priority
            RX Pkts      316215      Bytes 327940189  
            RX Drop Pkts 0           Bytes 0          
            RX Err  Pkts 0           Bytes 0          
          TX High Priority
            TX Pkts      0           Bytes 0          
            TX Drop Pkts 0           Bytes 0   
    '''
    }

    golden_parsed_output_slot = {
        'slot': {
            '0': {
                'subslot': {
                    '0': {
                        'name': 'SPA-8X1GE-V2',
                        'received': {
                            'bytes': 6378454260,
                            'ipc_bytes': 0,
                            'ipc_pkts': 0,
                            'pkts': 13543013},
                        'status': 'Online',
                        'transmitted': {
                            'bytes': 6258449952,
                            'ipc_bytes': 0,
                            'ipc_pkts': 0,
                            'pkts': 13689497}
                    },
                    '1': {
                        'name': 'SPA-8X1GE-V2',
                        'received': {
                            'bytes': 0,
                            'ipc_bytes': 0,
                            'ipc_pkts': 0,
                            'pkts': 0},
                        'status': 'Online',
                        'transmitted': {
                            'bytes': 0,
                            'ipc_bytes': 0,
                            'ipc_pkts': 0,
                            'pkts': 0}
                    },
                    '2': {
                        'name': 'SPA-1XTENGE-XFP-V2',
                        'received': {
                            'bytes': 0,
                            'ipc_bytes': 0,
                            'ipc_pkts': 0,
                            'pkts': 0},
                        'status': 'Online',
                        'transmitted': {
                            'bytes': 0,
                            'ipc_bytes': 0,
                            'ipc_pkts': 0,
                            'pkts': 0}
                    },
                    '3': {
                        'name': 'SPA-1XTENGE-XFP-V2',
                        'received': {
                            'bytes': 0,
                            'ipc_bytes': 0,
                            'ipc_pkts': 0,
                            'pkts': 0},
                        'status': 'Online',
                        'transmitted': {
                            'bytes': 0,
                            'ipc_bytes': 0,
                            'ipc_pkts': 0,
                            'pkts': 0,
                        }
                    }
                }
            }
        }
    }

    golden_output_slot = {'execute.return_value': '''\
        Router#show platform hardware slot 0 plim statistics 
        0/0, SPA-8X1GE-V2, Online
          RX Pkts 13543013    Bytes 6378454260 
          TX Pkts 13689497    Bytes 6258449952 
          RX IPC Pkts 0           Bytes 0          
          TX IPC Pkts 0           Bytes 0          

        0/1, SPA-8X1GE-V2, Online
          RX Pkts 0           Bytes 0          
          TX Pkts 0           Bytes 0          
          RX IPC Pkts 0           Bytes 0          
          TX IPC Pkts 0           Bytes 0          

        0/2, SPA-1XTENGE-XFP-V2, Online
          RX Pkts 0           Bytes 0          
          TX Pkts 0           Bytes 0          
          RX IPC Pkts 0           Bytes 0          
          TX IPC Pkts 0           Bytes 0          

        0/3, SPA-1XTENGE-XFP-V2, Online
          RX Pkts 0           Bytes 0          
          TX Pkts 0           Bytes 0          
          RX IPC Pkts 0           Bytes 0          
          TX IPC Pkts 0           Bytes 0
    '''
    }

    golden_parsed_output_subslot = {
        'slot': {
            '0': {
                'subslot': {
                    '1': {
                        'name': 'SPA-8X1GE-V2',
                        'received': {
                            'bytes': 0,
                            'ipc_bytes': 0,
                            'ipc_pkts': 0,
                            'pkts': 0},
                        'status': 'Online',
                        'transmitted': {
                            'bytes': 0,
                            'ipc_bytes': 0,
                            'ipc_pkts': 0,
                            'pkts': 0,
                        }
                    }
                }
            }
        }
    }

    golden_output_subslot = {'execute.return_value': '''\
        Router#show platform hardware subslot 0/1 plim statistics
        0/1, SPA-8X1GE-V2, Online
          RX Pkts 0           Bytes 0          
          TX Pkts 0           Bytes 0          
          RX IPC Pkts 0           Bytes 0          
          TX IPC Pkts 0           Bytes 0 
    '''
    }

    golden_parsed_output_slot_internal = {
        'slot': {
            '0': {
                'subslot': {
                    '0': {
                        'name': 'SPA-8X1GE-V2',
                        'received': {
                            'ipc_err': 0,
                            'spi4_interrupt_counters': {
                                'burst_error': 0,
                                'control_word_error': 0,
                                'dip4_error': 0,
                                'disabled': 0,
                                'eop_abort': 0,
                                'loss_of_sync': 0,
                                'out_of_frame': 0,
                                'packet_gap_error': 0,
                                'sequence_error': 0,
                            }
                        },
                        'status': 'Online',
                        'transmitted': {
                            'ipc_err': 0,
                            'spi4_interrupt_counters': {
                                'dip2_error': 0,
                                'fifo_over_flow': 0,
                                'frame_error': 0,
                                'out_of_frame': 0,
                            }
                        }
                    },
                    '1': {
                        'name': 'SPA-8X1GE-V2',
                        'received': {
                            'ipc_err': 0,
                            'spi4_interrupt_counters': {
                                'burst_error': 0,
                                'control_word_error': 0,
                                'dip4_error': 0,
                                'disabled': 0,
                                'eop_abort': 0,
                                'loss_of_sync': 0,
                                'out_of_frame': 0,
                                'packet_gap_error': 0,
                                'sequence_error': 0}
                            },
                        'status': 'Online',
                        'transmitted': {
                            'ipc_err': 0,
                            'spi4_interrupt_counters': {
                                'dip2_error': 0,
                                'fifo_over_flow': 0,
                                'frame_error': 0,
                                'out_of_frame': 0,
                            }
                        }
                    },
                    '2': {
                        'name': 'SPA-1XTENGE-XFP-V2',
                        'received': {
                            'ipc_err': 0,
                            'spi4_interrupt_counters': {
                                'burst_error': 0,
                                'control_word_error': 0,
                                'dip4_error': 0,
                                'disabled': 0,
                                'eop_abort': 0,
                                'loss_of_sync': 0,
                                'out_of_frame': 0,
                                'packet_gap_error': 0,
                                'sequence_error': 0,
                            }
                        },
                        'status': 'Online',
                        'transmitted': {
                            'ipc_err': 0,
                            'spi4_interrupt_counters': {
                                'dip2_error': 0,
                                'fifo_over_flow': 0,
                                'frame_error': 0,
                                'out_of_frame': 0,
                            }
                        }
                    },
                    '3': {
                        'name': 'SPA-1XTENGE-XFP-V2',
                        'received': {
                            'ipc_err': 0,
                            'spi4_interrupt_counters': {
                                'burst_error': 0,
                                'control_word_error': 0,
                                'dip4_error': 0,
                                'disabled': 0,
                                'eop_abort': 0,
                                'loss_of_sync': 0,
                                'out_of_frame': 0,
                                'packet_gap_error': 0,
                                'sequence_error': 0,
                            }
                        },
                        'status': 'Online',
                        'transmitted': {
                            'ipc_err': 0,
                            'spi4_interrupt_counters': {
                                'dip2_error': 0,
                                'fifo_over_flow': 0,
                                'frame_error': 0,
                                'out_of_frame': 0,
                            }
                        }
                    }
                }
            }
        }
    }

    golden_output_slot_internal = {'execute.return_value': '''\
        Router#show platform hardware slot 0 plim statistics internal 
        0/0, SPA-8X1GE-V2, Online
          RX IPC Err 0          
          TX IPC Err 0          
          RX Spi4 Interrupt Counters
            Out Of Frame 0          
            Dip4 Error 0          
            Disabled 0          
            Loss Of Sync 0          
            Sequence Error 0          
            Burst Error 0          
            EOP Abort 0          
            Packet Gap Error 0          
            Control Word Error 0          
          TX Spi4 Interrupt Counters
            Out Of Frame 0          
            Frame Error 0          
            FIFO Over Flow 0          
            Dip2 Error 0          

        0/1, SPA-8X1GE-V2, Online
          RX IPC Err 0          
          TX IPC Err 0          
          RX Spi4 Interrupt Counters
            Out Of Frame 0          
            Dip4 Error 0          
            Disabled 0          
            Loss Of Sync 0          
            Sequence Error 0          
            Burst Error 0          
            EOP Abort 0          
            Packet Gap Error 0          
            Control Word Error 0          
          TX Spi4 Interrupt Counters
            Out Of Frame 0          
            Frame Error 0          
            FIFO Over Flow 0          
            Dip2 Error 0          

        0/2, SPA-1XTENGE-XFP-V2, Online
          RX IPC Err 0          
          TX IPC Err 0          
          RX Spi4 Interrupt Counters
            Out Of Frame 0          
            Dip4 Error 0          
            Disabled 0          
            Loss Of Sync 0          
            Sequence Error 0          
            Burst Error 0          
            EOP Abort 0          
            Packet Gap Error 0          
            Control Word Error 0          
          TX Spi4 Interrupt Counters
            Out Of Frame 0          
            Frame Error 0          
            FIFO Over Flow 0          
            Dip2 Error 0          

        0/3, SPA-1XTENGE-XFP-V2, Online
          RX IPC Err 0          
          TX IPC Err 0          
          RX Spi4 Interrupt Counters
            Out Of Frame 0          
            Dip4 Error 0          
            Disabled 0          
            Loss Of Sync 0          
            Sequence Error 0          
            Burst Error 0          
            EOP Abort 0          
            Packet Gap Error 0          
            Control Word Error 0          
          TX Spi4 Interrupt Counters
            Out Of Frame 0          
            Frame Error 0          
            FIFO Over Flow 0          
            Dip2 Error 0    
    '''
    }

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
        self.assertEqual(parsed_output, self.golden_parsed_output_slot_internal)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowPlatformHardwarePlim(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(port='0/0/0')

class TestShowPlatformHardwareQfpBqsOpmMapping(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output_active_opm = {
        'channel': {
            '0': {
                'drain_mode': False,
                'interface': 'SPI0',
                'logical_channel': 0,
                'name': 'CC0 Low',
            },
            '1': {
                'drain_mode': False,
                'interface': 'SPI0',
                'logical_channel': 1,
                'name': 'CC0 Hi',
            },
            '10': {
                'drain_mode': False,
                'interface': 'SPI0',
                'logical_channel': 10,
                'name': 'CC2B Low',
            },
            '11': {
                'drain_mode': False,
                'interface': 'SPI0',
                'logical_channel': 11,
                'name': 'CC2B Hi',
            },
            '12': {
                'drain_mode': False,
                'interface': 'SPI0',
                'logical_channel': 12,
                'name': 'CC3 Low',
            },
            '13': {
                'drain_mode': False,
                'interface': 'SPI0',
                'logical_channel': 13,
                'name': 'CC3 Hi',
            },
            '14': {
                'drain_mode': False,
                'interface': 'SPI0',
                'logical_channel': 14,
                'name': 'CC3B Low',
            },
            '15': {
                'drain_mode': False,
                'interface': 'SPI0',
                'logical_channel': 15,
                'name': 'CC3B Hi',
            },
            '16': {
                'drain_mode': False,
                'interface': 'SPI0',
                'logical_channel': 16,
                'name': 'CC4 Low',
            },
            '17': {
                'drain_mode': False,
                'interface': 'SPI0',
                'logical_channel': 17,
                'name': 'CC4 Hi',
            },
            '18': {
                'drain_mode': False,
                'interface': 'SPI0',
                'logical_channel': 18,
                'name': 'CC5 Low',
            },
            '19': {
                'drain_mode': False,
                'interface': 'SPI0',
                'logical_channel': 19,
                'name': 'CC5 Hi',
            },
            '2': {
                'drain_mode': False,
                'interface': 'SPI0',
                'logical_channel': 2,
                'name': 'CC0B Low',
            },
            '20': {
                'drain_mode': False,
                'interface': 'SPI0',
                'logical_channel': 20,
                'name': 'RP0 Low',
            },
            '21': {
                'drain_mode': False,
                'interface': 'SPI0',
                'logical_channel': 21,
                'name': 'RP0 Hi',
            },
            '22': {
                'drain_mode': False,
                'interface': 'SPI0',
                'logical_channel': 22,
                'name': 'RP1 Low',
            },
            '23': {
                'drain_mode': False,
                'interface': 'SPI0',
                'logical_channel': 23,
                'name': 'RP1 Hi',
            },
            '24': {
                'drain_mode': False,
                'interface': 'SPI0',
                'logical_channel': 24,
                'name': 'Peer-FP Low',
            },
            '25': {
                'drain_mode': False,
                'interface': 'SPI0',
                'logical_channel': 25,
                'name': 'Peer-FP Hi',
            },
            '26': {
                'drain_mode': False,
                'interface': 'SPI0',
                'logical_channel': 26,
                'name': 'Nitrox Low',
            },
            '27': {
                'drain_mode': False,
                'interface': 'SPI0',
                'logical_channel': 27,
                'name': 'Nitrox Hi',
            },
            '28': {
                'drain_mode': False,
                'interface': 'HT',
                'logical_channel': 0,
                'name': 'HT Pkt Low',
            },
             '29': {
                'drain_mode': False,
                'interface': 'HT',
                'logical_channel': 1,
                'name': 'HT Pkt Hi',
            },
            '3': {
                'drain_mode': False,
                'interface': 'SPI0',
                'logical_channel': 3,
                'name': 'CC0B Hi',
            },
            '30': {
                'drain_mode': False,
                'interface': 'HT',
                'logical_channel': 2,
                'name': 'HT IPC Low',
            },
            '31': {
                'drain_mode': False,
                'interface': 'HT',
                'logical_channel': 3,
                'name': 'HT IPC Hi',
            },
            '32': {
                'name': 'unmapped',
            },
            '33': {
                'name': 'unmapped',
            },
            '34': {
                'name': 'unmapped',
            },
            '35': {
                'name': 'unmapped',
            },
            '36': {
                'name': 'unmapped',
            },
            '37': {
                'name': 'unmapped',
            },
            '38': {
                'drain_mode': False,
                'interface': 'GPM',
                'logical_channel': 7,
                'name': 'HighNormal',
            },
            '39': {
                'drain_mode': False,
                'interface': 'GPM',
                'logical_channel': 6,
                'name': 'HighPriority',
            },
            '4': {
                'drain_mode': False,
                'interface': 'SPI0',
                'logical_channel': 4,
                'name': 'CC1 Low',
            },
            '40': {
                'drain_mode': False,
                'interface': 'GPM',
                'logical_channel': 11,
                'name': 'LowNormal',
            },
            '41': {
                'drain_mode': False,
                'interface': 'GPM',
                'logical_channel': 10,
                'name': 'LowPriority',
            },
            '42': {
                'drain_mode': False,
                'interface': 'GPM',
                'logical_channel': 12,
                'name': 'InternalTrafficHiChannel',
            },
            '43': {
                'drain_mode': False,
                'interface': 'GPM',
                'logical_channel': 13,
                'name': 'InternalTrafficLoChannel',
            },
            '44': {
                'drain_mode': False,
                'interface': 'GPM',
                'logical_channel': 14,
                'name': 'AttnTrafficHiChannel',
            },
            '45': {
                'drain_mode': False,
                'interface': 'GPM',
                'logical_channel': 15,
                'name': 'MetaPktTrafficChannel',
            },
            '46': {
                'name': 'unmapped',
            },
            '47': {
                'name': 'unmapped',
            },
            '48': {
                'name': 'unmapped',
            },
            '49': {
                'name': 'unmapped',
            },
            '5': {
                'drain_mode': False,
                'interface': 'SPI0',
                'logical_channel': 5,
                'name': 'CC1 Hi',
            },
            '50': {
                'name': 'unmapped',
            },
            '51': {
                'name': 'unmapped',
            },
            '52': {
                'name': 'unmapped',
            },
            '53': {
                'name': 'unmapped',
            },
            '54': {
                'name': 'unmapped',
            },
            '55': {
                'drain_mode': True,
                'interface': 'GPM',
                'logical_channel': 0,
                'name': 'Drain Low',
            },
            '6': {
                'drain_mode': False,
                'interface': 'SPI0',
                'logical_channel': 6,
                'name': 'CC1B Low',
            },
            '7': {
                'drain_mode': False,
                'interface': 'SPI0',
                'logical_channel': 7,
                'name': 'CC1B Hi',
            },
            '8': {
                'drain_mode': False,
                'interface': 'SPI0',
                'logical_channel': 8,
                'name': 'CC2 Low',
            },
            '9': {
                'drain_mode': False,
                'interface': 'SPI0',
                'logical_channel': 9,
                'name': 'CC2 Hi',
            },
        },
    }

    golden_output_active_opm = {'execute.return_value': '''\ 
        Router#show platform hardware qfp active bqs 0 opm mapping 
        Load for five secs: 5%/3%; one minute: 7%; five minutes: 8%
        Time source is NTP, 07:43:32.664 EST Thu Sep 8 2016

        BQS OPM Channel Mapping

        Chan     Name                          Interface      LogicalChannel

         0       CC0 Low                       SPI0            0             
         1       CC0 Hi                        SPI0            1             
         2       CC0B Low                      SPI0            2             
         3       CC0B Hi                       SPI0            3             
         4       CC1 Low                       SPI0            4             
         5       CC1 Hi                        SPI0            5             
         6       CC1B Low                      SPI0            6             
         7       CC1B Hi                       SPI0            7             
         8       CC2 Low                       SPI0            8             
         9       CC2 Hi                        SPI0            9             
        10       CC2B Low                      SPI0           10             
        11       CC2B Hi                       SPI0           11             
        12       CC3 Low                       SPI0           12             
        13       CC3 Hi                        SPI0           13             
        14       CC3B Low                      SPI0           14             
        15       CC3B Hi                       SPI0           15             
        16       CC4 Low                       SPI0           16             
        17       CC4 Hi                        SPI0           17             
        18       CC5 Low                       SPI0           18             
        19       CC5 Hi                        SPI0           19             
        20       RP0 Low                       SPI0           20             
        21       RP0 Hi                        SPI0           21             
        22       RP1 Low                       SPI0           22             
        23       RP1 Hi                        SPI0           23             
        24       Peer-FP Low                   SPI0           24             
        25       Peer-FP Hi                    SPI0           25             
        26       Nitrox Low                    SPI0           26             
        27       Nitrox Hi                     SPI0           27             
        28       HT Pkt Low                    HT              0             
        29       HT Pkt Hi                     HT              1             
        30       HT IPC Low                    HT              2             
        31       HT IPC Hi                     HT              3             
        32       Unmapped                      
        33       Unmapped                      
        34       Unmapped                      
        35       Unmapped                      
        36       Unmapped                      
        37       Unmapped                      
        38       HighNormal                    GPM             7             
        39       HighPriority                  GPM             6             
        40       LowNormal                     GPM            11             
        41       LowPriority                   GPM            10             
        42       InternalTrafficHiChannel      GPM            12             
        43       InternalTrafficLoChannel      GPM            13             
        44       AttnTrafficHiChannel          GPM            14             
        45       MetaPktTrafficChannel         GPM            15             
        46       Unmapped                      
        47       Unmapped                      
        48       Unmapped                      
        49       Unmapped                      
        50       Unmapped                      
        51       Unmapped                      
        52       Unmapped                      
        53       Unmapped                      
        54       Unmapped                      
        55*      Drain Low                     GPM             0             
         * - indicates the drain mode bit is set for this channel
    '''
    }

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

class TestShowPlatformHardwareQfpBqsIpmMapping(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output_active_ipm = {
        'channel': {
            '1': {
                'cfifo': 1,
                'interface': 'SPI0',
                'name': 'CC3 Low',
                'port': 0,
            },
            '10': {
                'cfifo': 0,
                'interface': 'SPI0',
                'name': 'RP1 Hi',
                'port': 9,
            },
            '11': {
                'cfifo': 1,
                'interface': 'SPI0',
                'name': 'RP0 Low',
                'port': 10,
            },
            '12': {
                'cfifo': 0,
                'interface': 'SPI0',
                'name': 'RP0 Hi',
                'port': 11,
            },
            '13': {
                'cfifo': 3,
                'interface': 'SPI0',
                'name': 'Peer-FP Low',
                'port': 12,
            },
            '14': {
                'cfifo': 2,
                'interface': 'SPI0',
                'name': 'Peer-FP Hi',
                'port': 13,
            },
            '15': {
                'cfifo': 1,
                'interface': 'SPI0',
                'name': 'Nitrox Low',
                'port': 14,
            },
            '16': {
                'cfifo': 0,
                'interface': 'SPI0',
                'name': 'Nitrox Hi',
                'port': 15,
            },
            '17': {
                'cfifo': 1,
                'interface': 'HT',
                'name': 'HT Pkt Low',
                'port': 0,
            },
            '18': {
                'cfifo': 0,
                'interface': 'HT',
                'name': 'HT Pkt Hi',
                'port': 1,
            },
            '19': {
                'cfifo': 3,
                'interface': 'HT',
                'name': 'HT IPC Low',
                'port': 2,
            },
            '2': {
                'cfifo': 0,
                'interface': 'SPI0',
                'name': 'CC3 Hi',
                'port': 1,
            },
            '20': {
                'cfifo': 2,
                'interface': 'HT',
                'name': 'HT IPC Hi',
                'port': 3,
            },
            '21': {
                'cfifo': 1,
                'interface': 'SPI0',
                'name': 'CC4 Low',
                'port': 16,
            },
            '22': {
                'cfifo': 0,
                'interface': 'SPI0',
                'name': 'CC4 Hi',
                'port': 17,
            },
            '23': {
                'cfifo': 1,
                'interface': 'SPI0',
                'name': 'CC5 Low',
                'port': 18,
            },
            '24': {
                'cfifo': 0,
                'interface': 'SPI0',
                'name': 'CC5 Hi',
                'port': 19,
            },
            '3': {
                'cfifo': 1,
                'interface': 'SPI0',
                'name': 'CC2 Low',
                'port': 2,
            },
            '4': {
                'cfifo': 0,
                'interface': 'SPI0',
                'name': 'CC2 Hi',
                'port': 3,
            },
            '5': {
                'cfifo': 1,
                'interface': 'SPI0',
                'name': 'CC1 Low',
                'port': 4,
            },
            '6': {
                'cfifo': 0,
                'interface': 'SPI0',
                'name': 'CC1 Hi',
                'port': 5,
            },
            '7': {
                'cfifo': 1,
                'interface': 'SPI0',
                'name': 'CC0 Low',
                'port': 6,
            },
            '8': {
                'cfifo': 0,
                'interface': 'SPI0',
                'name': 'CC0 Hi',
                'port': 7,
            },
            '9': {
                'cfifo': 1,
                'interface': 'SPI0',
                'name': 'RP1 Low',
                'port': 8,
            },
        },
    }

    golden_output_active_ipm = {'execute.return_value': '''\
        Router#show platform hardware qfp active bqs 0 ipm mapping 
        Load for five secs: 29%/1%; one minute: 8%; five minutes: 9%
        Time source is NTP, 07:42:52.908 EST Thu Sep 8 2016

        BQS IPM Channel Mapping

        Chan   Name                Interface      Port     CFIFO

         1     CC3 Low             SPI0           0        1     
         2     CC3 Hi              SPI0           1        0     
         3     CC2 Low             SPI0           2        1     
         4     CC2 Hi              SPI0           3        0     
         5     CC1 Low             SPI0           4        1     
         6     CC1 Hi              SPI0           5        0     
         7     CC0 Low             SPI0           6        1     
         8     CC0 Hi              SPI0           7        0     
         9     RP1 Low             SPI0           8        1     
        10     RP1 Hi              SPI0           9        0     
        11     RP0 Low             SPI0          10        1     
        12     RP0 Hi              SPI0          11        0     
        13     Peer-FP Low         SPI0          12        3     
        14     Peer-FP Hi          SPI0          13        2     
        15     Nitrox Low          SPI0          14        1     
        16     Nitrox Hi           SPI0          15        0     
        17     HT Pkt Low          HT             0        1     
        18     HT Pkt Hi           HT             1        0     
        19     HT IPC Low          HT             2        3     
        20     HT IPC Hi           HT             3        2     
        21     CC4 Low             SPI0          16        1     
        22     CC4 Hi              SPI0          17        0     
        23     CC5 Low             SPI0          18        1     
        24     CC5 Hi              SPI0          19        0   
    '''
    }

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

class TestShowPlatformHardwareSerdesStatistics(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output_serdes = {
        'link': {
            '0-Link A': {
                'from': {
                    'bytes': {
                        'bad': 0,
                        'dropped': 0,
                        'high': 53361379,
                        'looped': 0,
                        'low': 199330758,
                    },
                    'flow_ctrl_count': 3680,
                    'pkts': {
                        'bad': 0,
                        'dropped': 0,
                        'errored': 0,
                        'high': 63052,
                        'looped': 0,
                        'low': 2703601,
                    },
                    'qstat_count': 331199,
                },
                'to': {
                    'pkts': {
                        'high': 0,
                        'low': 2787636,
                    }
                }
            },
            '0-Link B': {
                'from': {
                    'bytes': {
                        'bad': 0,
                        'dropped': 0,
                        'high': 0,
                        'looped': 0,
                        'low': 0,
                    },
                    'flow_ctrl_count': 3680,
                    'pkts': {
                        'bad': 0,
                        'dropped': 0,
                        'errored': 0,
                        'high': 0,
                        'looped': 0,
                        'low': 0,
                    },
                    'qstat_count': 331199,
                },
                'to': {
                    'pkts': {
                        'high': 0,
                        'low': 0,
                    }
                }
            },
            '1-Link A': {
                'from': {
                    'bytes': {
                        'bad': 0,
                        'dropped': 0,
                        'high': 0,
                        'looped': 0,
                        'low': 0,
                    },
                    'flow_ctrl_count': 3680,
                    'pkts': {
                        'bad': 0,
                        'dropped': 0,
                        'errored': 0,
                        'high': 0,
                        'looped': 0,
                        'low': 0,
                    },
                    'qstat_count': 294400,
                },
                'to': {
                    'pkts': {
                        'high': 0,
                        'low': 0,
                    }
                }
            },
            '1-Link B': {
                'from': {
                    'bytes': {
                        'bad': 0,
                        'dropped': 0,
                        'high': 0,
                        'looped': 0,
                        'low': 0,
                    },
                    'flow_ctrl_count': 3680,
                    'pkts': {
                        'bad': 0,
                        'dropped': 0,
                        'errored': 0,
                        'high': 0,
                        'looped': 0,
                        'low': 0,
                    },
                    'qstat_count': 0,
                },
                'to': {
                    'pkts': {
                        'high': 0,
                        'low': 0,
                    }
                }
            },
            'F1-Link A': {
                'from': {
                    'bytes': {
                        'bad': 0,
                        'dropped': 0,
                        'high': 0,
                        'looped': 0,
                        'low': 18648,
                    },
                    'flow_ctrl_count': 3680,
                    'pkts': {
                        'bad': 0,
                        'dropped': 0,
                        'errored': 0,
                        'high': 0,
                        'looped': 0,
                        'low': 518,
                    },
                    'qstat_count': 0,
                },
                'to': {
                    'pkts': {
                        'high': 0,
                        'low': 518,
                    }
                }
            },
            'R0-Link A': {
                'from': {
                    'bytes': {
                        'bad': 0,
                        'dropped': 0,
                        'high': 1614284,
                        'looped': 0,
                        'low': 298734735,
                    },
                    'flow_ctrl_count': 3700,
                    'pkts': {
                        'bad': 0,
                        'dropped': 0,
                        'errored': 0,
                        'high': 19461,
                        'looped': 0,
                        'low': 2777099,
                    },
                    'qstat_count': 0,
                },
                'to': {
                    'pkts': {
                        'high': 1018101,
                        'low': 1719353,
                    }
                }
            },
            'R1-Link A': {
                'from': {
                    'bytes': {
                        'bad': 0,
                        'dropped': 0,
                        'high': 0,
                        'looped': 0,
                        'low': 0,
                    },
                    'flow_ctrl_count': 3501,
                    'pkts': {
                        'bad': 0,
                        'dropped': 0,
                        'errored': 0,
                        'high': 0,
                        'looped': 0,
                        'low': 0,
                    },
                    'qstat_count': 0,
                },
                'to': {
                    'pkts': {
                        'high': 0,
                        'low': 0,
                    }
                }
            }
        }
    }

    golden_output_serdes = {'execute.return_value': '''\
        Router#show platform hardware slot F0 serdes statistics 
        Load for five secs: 22%/1%; one minute: 8%; five minutes: 9%
        Time source is NTP, 07:42:08.304 EST Thu Sep 8 2016
        From Slot R1-Link A
          Pkts  High: 0          Low: 0          Bad: 0          Dropped: 0         
          Bytes High: 0          Low: 0          Bad: 0          Dropped: 0         
          Pkts  Looped: 0          Error: 0         
          Bytes Looped 0         
          Qstat count: 0          Flow ctrl count: 3501      
        To Slot R1-Link A
          Pkts  High: 0          Low: 0         

        From Slot R0-Link A
          Pkts  High: 19461      Low: 2777099    Bad: 0          Dropped: 0         
          Bytes High: 1614284    Low: 298734735  Bad: 0          Dropped: 0         
          Pkts  Looped: 0          Error: 0         
          Bytes Looped 0         
          Qstat count: 0          Flow ctrl count: 3700      
        To Slot R0-Link A
          Pkts  High: 1018101    Low: 1719353   

        From Slot F1-Link A
          Pkts  High: 0          Low: 518        Bad: 0          Dropped: 0         
          Bytes High: 0          Low: 18648      Bad: 0          Dropped: 0         
          Pkts  Looped: 0          Error: 0         
          Bytes Looped 0         
          Qstat count: 0          Flow ctrl count: 3680      
        To Slot F1-Link A
          Pkts  High: 0          Low: 518       

        From Slot 1-Link A
          Pkts  High: 0          Low: 0          Bad: 0          Dropped: 0         
          Bytes High: 0          Low: 0          Bad: 0          Dropped: 0         
          Pkts  Looped: 0          Error: 0         
          Bytes Looped 0         
          Qstat count: 294400     Flow ctrl count: 3680      
        To Slot 1-Link A
          Pkts  High: 0          Low: 0         

        From Slot 0-Link A
          Pkts  High: 63052      Low: 2703601    Bad: 0          Dropped: 0         
          Bytes High: 53361379   Low: 199330758  Bad: 0          Dropped: 0         
          Pkts  Looped: 0          Error: 0         
          Bytes Looped 0         
          Qstat count: 331199     Flow ctrl count: 3680      
        To Slot 0-Link A
          Pkts  High: 0          Low: 2787636   

        From Slot 0-Link B
          Pkts  High: 0          Low: 0          Bad: 0          Dropped: 0         
          Bytes High: 0          Low: 0          Bad: 0          Dropped: 0         
          Pkts  Looped: 0          Error: 0         
          Bytes Looped 0         
          Qstat count: 331199     Flow ctrl count: 3680      
        To Slot 0-Link B
          Pkts  High: 0          Low: 0         

        From Slot 1-Link B
          Pkts  High: 0          Low: 0          Bad: 0          Dropped: 0         
          Bytes High: 0          Low: 0          Bad: 0          Dropped: 0         
          Pkts  Looped: 0          Error: 0         
          Bytes Looped 0         
          Qstat count: 0          Flow ctrl count: 3680      
        To Slot 1-Link B
          Pkts  High: 0          Low: 0         
    '''
    }

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

class TestShowPlatformHardwareSerdesStatisticsInternal(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output_serdes_internal = {
        'link': {
            'Encryption Processor': {
                'errors': {
                    'rx_parity': 0,
                    'rx_process': 0,
                    'rx_schedule': 0,
                    'rx_statistics': 0,
                    'tx_process': 0,
                    'tx_schedule': 0,
                    'tx_statistics': 0,
                },
                'from': {
                    'bytes': {
                        'dropped': 0,
                        'errored': 0,
                        'total': 0},
                    'pkts': {
                        'dropped': 0,
                        'errored': 0,
                        'total': 0,
                    },
                },
                'local_rx_in_sync': True,
                'local_tx_in_sync': True,
                'remote_rx_in_sync': True,
                'remote_tx_in_sync': True,
                'to': {
                    'bytes': {
                        'dropped': 0,
                        'total': 0,
                    },
                    'pkts': {
                        'dropped': 0,
                        'total': 0,
                    },
                },
            },
            'Network-Processor-0': {
                'from': {
                    'bytes': {
                        'total': 7397920802,
                    },
                    'pkts': {
                        'total': 21259012,
                    },
                },
                'local_rx_in_sync': True,
                'local_tx_in_sync': True,
                'to': {
                    'bytes': {
                        'total': 7343838083,
                    },
                    'pkts': {
                        'total': 21763844,
                    },
                },
            },
        },
        'serdes_exception_counts': {
            'c2w': {},
            'cfg': {},
            'cilink': {
                'link': {
                    '0': {
                        'chicoEvent': 5,
                        'msgEccError': 5,
                        'msgTypeError': 5,
                    },
                    '1': {
                        'chicoEvent': 1,
                        'msgEccError': 1,
                        'msgTypeError': 1,
                    },
                    '2': {
                        'chicoEvent': 3,
                        'msgEccError': 3,
                        'msgTypeError': 3,
                    },
                },
            },
            'edh-hi': {},
            'edh-lo': {},
            'edm': {},
            'eqs/fc': {},
            'idh-hi': {},
            'idh-lo': {},
            'idh-shared': {},
            'ilak': {},
            'isch': {},
            'pcie': {},
            'slb': {},
            'spi link': {},
        },
    }

    golden_output_serdes_internal = {'execute.return_value': '''\
        Router#show platform hardware slot F0 serdes statistics internal 
        Load for five secs: 5%/1%; one minute: 8%; five minutes: 9%
        Time source is NTP, 07:42:13.752 EST Thu Sep 8 2016
        Warning: Clear option may not clear all the counters

        Network-Processor-0 Link:
          Local TX in sync, Local RX in sync
          From Network-Processor     Packets:    21259012  Bytes:  7397920802
          To Network-Processor       Packets:    21763844  Bytes:  7343838083

        Encryption Processor Link:
          Local TX in sync, Local RX in sync
          Remote TX in sync, Remote RX in sync
          To Encryption Processor   Packets:           0  Bytes:           0
            Drops                   Packets:           0  Bytes:           0
          From Encryption Processor Packets:           0  Bytes:           0
            Drops                   Packets:           0  Bytes:           0
            Errors                  Packets:           0  Bytes:           0
          Errors:
            RX/TX process: 0/0, RX/TX schedule: 0/0
            RX/TX statistics: 0/0, RX parity: 0

        Serdes Exception Counts:
          spi link:
          cilink:
            link 0: msgTypeError: 5
            link 0: msgEccError: 5
            link 0: chicoEvent: 5
            link 1: msgTypeError: 1
            link 1: msgEccError: 1
            link 1: chicoEvent: 1
            link 2: msgTypeError: 3
            link 2: msgEccError: 3
            link 2: chicoEvent: 3
          ilak:
          slb:
          edm:
          isch:
          cfg:
          c2w:
          pcie:
          eqs/fc:
          idh-hi:
          idh-lo:
          idh-shared:
          edh-hi:
          edh-lo:
    '''
    }

    def test_golden(self):
        self.device = Mock(**self.golden_output_serdes_internal)
        obj = ShowPlatformHardwareSerdesInternal(device=self.device)
        parsed_output = obj.parse(slot='0')
        self.maxDiff = None
        self.assertEqual(parsed_output, self.golden_parsed_output_serdes_internal)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowPlatformHardwareSerdesInternal(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(slot='0')


class TestShowPlatformPower(unittest.TestCase):
    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'allocation_status': 'Sufficient',
        'chassis': 'ASR1006-X',
        'excess_capacity_percent': 72,
        'excess_power': 3201,
        'fan_alc': 250,
        'fru_alc': 949,
        'load_capacity_percent': 15,
        'power_capacity': 4400,
        'redundancy_mode': 'nplus1',
        'redundant_alc': 0,
        'slot': {'0': {'allocation': 64.0, 'state': 'ok', 'type': 'ASR1000-SIP40'},
              '0/0': {'allocation': 14.0,
                      'state': 'inserted',
                      'type': 'SPA-8X1GE-V2'},
              '0/1': {'allocation': 14.0,
                      'state': 'inserted',
                      'type': 'SPA-8X1GE-V2'},
              '0/2': {'allocation': 17.4,
                      'state': 'inserted',
                      'type': 'SPA-1X10GE-L-V2'},
              '0/3': {'allocation': 17.4,
                      'state': 'inserted',
                      'type': 'SPA-1X10GE-L-V2'},
              '1': {'allocation': 64.0, 'state': 'ok', 'type': 'ASR1000-SIP40'},
              '1/0': {'allocation': 14.0,
                      'state': 'inserted',
                      'type': 'SPA-8X1GE-V2'},
              'F0': {'allocation': 267.0,
                     'state': 'ok, active',
                     'type': 'ASR1000-ESP40'},
              'F1': {'allocation': 267.0,
                     'state': 'ok, standby',
                     'type': 'ASR1000-ESP40'},
              'P0': {'capacity': 1100,
                     'load': 132,
                     'state': 'ok',
                     'type': 'ASR1000X-AC-1100W'},
              'P1': {'capacity': 1100,
                     'load': 204,
                     'state': 'ok',
                     'type': 'ASR1000X-AC-1100W'},
              'P2': {'capacity': 1100,
                     'load': 180,
                     'state': 'ok',
                     'type': 'ASR1000X-AC-1100W'},
              'P3': {'capacity': 1100,
                     'load': 180,
                     'state': 'ok',
                     'type': 'ASR1000X-AC-1100W'},
              'P6': {'allocation': 125.0, 'state': 'ok', 'type': 'ASR1000X-FAN'},
              'P7': {'allocation': 125.0, 'state': 'ok', 'type': 'ASR1000X-FAN'},
              'R0': {'allocation': 105.0,
                     'state': 'ok, active',
                     'type': 'ASR1000-RP2'},
              'R1': {'allocation': 105.0,
                     'state': 'ok, standby',
                     'type': 'ASR1000-RP2'}},
        'total_capacity': 4400,
        'total_load': 696
    }
    
    golden_output = {'execute.return_value': '''\
        Chassis type: ASR1006-X           

        Slot      Type                State                 Allocation(W) 
        --------- ------------------- --------------------- ------------- 
        0         ASR1000-SIP40       ok                    64
         0/0      SPA-8X1GE-V2        inserted              14
         0/1      SPA-8X1GE-V2        inserted              14
         0/2      SPA-1X10GE-L-V2     inserted              17.40
         0/3      SPA-1X10GE-L-V2     inserted              17.40
        1         ASR1000-SIP40       ok                    64
         1/0      SPA-8X1GE-V2        inserted              14
        R0        ASR1000-RP2         ok, active            105
        R1        ASR1000-RP2         ok, standby           105
        F0        ASR1000-ESP40       ok, active            267
        F1        ASR1000-ESP40       ok, standby           267
        P6        ASR1000X-FAN        ok                    125        
        P7        ASR1000X-FAN        ok                    125        

        Slot      Type                State                 Capacity (W) Load (W)     
        --------- ------------------- --------------------- ------------ ------------ 
        P0        ASR1000X-AC-1100W   ok                    1100         132          
        P1        ASR1000X-AC-1100W   ok                    1100         204          
        P2        ASR1000X-AC-1100W   ok                    1100         180          
        P3        ASR1000X-AC-1100W   ok                    1100         180          

        Total load: 696 W, total capacity: 4400 W. Load / Capacity is 15%

        Power capacity:       4400 W
        Redundant allocation: 0 W
        Fan allocation:       250 W
        FRU allocation:       949 W
        --------------------------------------------
        Excess Power in Reserve:   3201 W
        Excess / (Capacity - Redundant) is 72%

        Power Redundancy Mode: nplus1

        Power Allocation Status: Sufficient
    '''}


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
        self.assertEqual(parsed_output,self.golden_parsed_output)


class TestShowPlatformHardwareQfpBqsStatisticsChannelAll(unittest.TestCase):

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output_active_ipm = {
        'channel': {
             1: {'badbytes': '0000000000',
                 'badpkts': '0000000000',
                 'goodbytes': '0000000000',
                 'goodpkts': '0000000000'},
             2: {'badbytes': '0000000000',
                 'badpkts': '0000000000',
                 'goodbytes': '0000000000',
                 'goodpkts': '0000000000'},
             3: {'badbytes': '0000000000',
                 'badpkts': '0000000000',
                 'goodbytes': '0000000000',
                 'goodpkts': '0000000000'},
             4: {'badbytes': '0000000000',
                 'badpkts': '0000000000',
                 'goodbytes': '0000000000',
                 'goodpkts': '0000000000'},
             5: {'badbytes': '0000000000',
                 'badpkts': '0000000000',
                 'goodbytes': '0000000000',
                 'goodpkts': '0000000000'},
             6: {'badbytes': '0000000000',
                 'badpkts': '0000000000',
                 'goodbytes': '0000000000',
                 'goodpkts': '0000000000'},
             7: {'badbytes': '0000000000',
                 'badpkts': '0000000000',
                 'goodbytes': '016a5004b0',
                 'goodpkts': '0000c40f64'},
             8: {'badbytes': '0000000000',
                 'badpkts': '0000000000',
                 'goodbytes': '00153685bd',
                 'goodpkts': '00000afbe9'},
             9: {'badbytes': '0000000000',
                 'badpkts': '0000000000',
                 'goodbytes': '0012139723',
                 'goodpkts': '0000288e4f'},
             10: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'goodbytes': '00000b2184',
                  'goodpkts': '000000223f'},
             11: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'goodbytes': '0023f74c7a',
                  'goodpkts': '000053ff08'},
             12: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'goodbytes': '0000305734',
                  'goodpkts': '0000009533'},
             13: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'goodbytes': '0000010ce4',
                  'goodpkts': '0000000749'},
             14: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'goodbytes': '0000000000',
                  'goodpkts': '0000000000'},
             15: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'goodbytes': '0000000000',
                  'goodpkts': '0000000000'},
             16: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'goodbytes': '0000000000',
                  'goodpkts': '0000000000'},
             17: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'goodbytes': '0000000000',
                  'goodpkts': '0000000000'},
             18: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'goodbytes': '0000000000',
                  'goodpkts': '0000000000'},
             19: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'goodbytes': '000aba8f64',
                  'goodpkts': '00000d968e'},
             20: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'goodbytes': '0000000000',
                  'goodpkts': '0000000000'},
             21: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'goodbytes': '0000000000',
                  'goodpkts': '0000000000'},
             22: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'goodbytes': '0000000000',
                  'goodpkts': '0000000000'},
             23: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'goodbytes': '0000000000',
                  'goodpkts': '0000000000'},
             24: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'goodbytes': '0000000000',
                  'goodpkts': '0000000000'}}}
    
    golden_parsed_output_active_opm = {
        'channel': {
             0: {'badbytes': '0000000000',
                 'badpkts': '0000000000',
                 'comment': 'OPM Channels',
                 'goodbytes': '01787bc9e1',
                 'goodpkts': '0000d18caf'},
             1: {'badbytes': '0000000000',
                 'badpkts': '0000000000',
                 'comment': 'OPM Channels',
                 'goodbytes': '0000000000',
                 'goodpkts': '0000000000'},
             2: {'badbytes': '0000000000',
                 'badpkts': '0000000000',
                 'comment': 'OPM Channels',
                 'goodbytes': '0000000000',
                 'goodpkts': '0000000000'},
             3: {'badbytes': '0000000000',
                 'badpkts': '0000000000',
                 'comment': 'OPM Channels',
                 'goodbytes': '0000000000',
                 'goodpkts': '0000000000'},
             4: {'badbytes': '0000000000',
                 'badpkts': '0000000000',
                 'comment': 'OPM Channels',
                 'goodbytes': '0000000000',
                 'goodpkts': '0000000000'},
             5: {'badbytes': '0000000000',
                 'badpkts': '0000000000',
                 'comment': 'OPM Channels',
                 'goodbytes': '0000000000',
                 'goodpkts': '0000000000'},
             6: {'badbytes': '0000000000',
                 'badpkts': '0000000000',
                 'comment': 'OPM Channels',
                 'goodbytes': '0000000000',
                 'goodpkts': '0000000000'},
             7: {'badbytes': '0000000000',
                 'badpkts': '0000000000',
                 'comment': 'OPM Channels',
                 'goodbytes': '0000000000',
                 'goodpkts': '0000000000'},
             8: {'badbytes': '0000000000',
                 'badpkts': '0000000000',
                 'comment': 'OPM Channels',
                 'goodbytes': '0000000000',
                 'goodpkts': '0000000000'},
             9: {'badbytes': '0000000000',
                 'badpkts': '0000000000',
                 'comment': 'OPM Channels',
                 'goodbytes': '0000000000',
                 'goodpkts': '0000000000'},
             10: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'comment': 'OPM Channels',
                  'goodbytes': '0000000000',
                  'goodpkts': '0000000000'},
             11: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'comment': 'OPM Channels',
                  'goodbytes': '0000000000',
                  'goodpkts': '0000000000'},
             12: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'comment': 'OPM Channels',
                  'goodbytes': '0000000000',
                  'goodpkts': '0000000000'},
             13: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'comment': 'OPM Channels',
                  'goodbytes': '0000000000',
                  'goodpkts': '0000000000'},
             14: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'comment': 'OPM Channels',
                  'goodbytes': '0000000000',
                  'goodpkts': '0000000000'},
             15: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'comment': 'OPM Channels',
                  'goodbytes': '0000000000',
                  'goodpkts': '0000000000'},
             16: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'comment': 'OPM Channels',
                  'goodbytes': '0000000000',
                  'goodpkts': '0000000000'},
             17: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'comment': 'OPM Channels',
                  'goodbytes': '0000000000',
                  'goodpkts': '0000000000'},
             18: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'comment': 'OPM Channels',
                  'goodbytes': '0000000000',
                  'goodpkts': '0000000000'},
             19: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'comment': 'OPM Channels',
                  'goodbytes': '0000000000',
                  'goodpkts': '0000000000'},
             20: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'comment': 'OPM Channels',
                  'goodbytes': '001ab1e8ad',
                  'goodpkts': '0000416122'},
             21: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'comment': 'OPM Channels',
                  'goodbytes': '000eac93b2',
                  'goodpkts': '000012481d'},
             22: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'comment': 'OPM Channels',
                  'goodbytes': '0004353727',
                  'goodpkts': '00000a3c55'},
             23: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'comment': 'OPM Channels',
                  'goodbytes': '00131e7f90',
                  'goodpkts': '000015b68d'},
             24: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'comment': 'OPM Channels',
                  'goodbytes': '00000b6ce8',
                  'goodpkts': '0000000749'},
             25: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'comment': 'OPM Channels',
                  'goodbytes': '0000000000',
                  'goodpkts': '0000000000'},
             26: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'comment': 'OPM Channels',
                  'goodbytes': '0000000000',
                  'goodpkts': '0000000000'},
             27: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'comment': 'OPM Channels',
                  'goodbytes': '0000000000',
                  'goodpkts': '0000000000'},
             28: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'comment': 'OPM Channels',
                  'goodbytes': '0000000000',
                  'goodpkts': '0000000000'},
             29: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'comment': 'OPM Channels',
                  'goodbytes': '0000000000',
                  'goodpkts': '0000000000'},
             30: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'comment': 'OPM Channels',
                  'goodbytes': '0016872998',
                  'goodpkts': '00000e35a9'},
             31: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'comment': 'OPM Channels',
                  'goodbytes': '0000000000',
                  'goodpkts': '0000000000'},
             32: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'comment': 'OPM Channels',
                  'goodbytes': '0000000000',
                  'goodpkts': '0000000000'},
             33: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'comment': 'OPM Channels',
                  'goodbytes': '0000000000',
                  'goodpkts': '0000000000'},
             34: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'comment': 'OPM Channels',
                  'goodbytes': '0000000000',
                  'goodpkts': '0000000000'},
             35: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'comment': 'OPM Channels',
                  'goodbytes': '0000000000',
                  'goodpkts': '0000000000'},
             36: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'comment': 'OPM Channels',
                  'goodbytes': '0000000000',
                  'goodpkts': '0000000000'},
             37: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'comment': 'OPM Channels',
                  'goodbytes': '0000000000',
                  'goodpkts': '0000000000'},
             38: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'comment': 'OPM Channels',
                  'goodbytes': '00018a62d0',
                  'goodpkts': '0000007f33'},
             39: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'comment': 'OPM Channels',
                  'goodbytes': '00000f3110',
                  'goodpkts': '0000000fd2'},
             40: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'comment': 'OPM Channels',
                  'goodbytes': '0000000000',
                  'goodpkts': '0000000000'},
             41: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'comment': 'OPM Channels',
                  'goodbytes': '0000000000',
                  'goodpkts': '0000000000'},
             42: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'comment': 'OPM Channels',
                  'goodbytes': '0000000300',
                  'goodpkts': '0000000010'},
             43: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'comment': 'OPM Channels',
                  'goodbytes': '0830f8d074',
                  'goodpkts': '002f8bbd4a'},
             44: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'comment': 'OPM Channels',
                  'goodbytes': '002f7036c0',
                  'goodpkts': '0001b1b8d0'},
             45: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'comment': 'OPM Channels',
                  'goodbytes': '0000000000',
                  'goodpkts': '0000000000'},
             46: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'comment': 'OPM Channels',
                  'goodbytes': '0000000000',
                  'goodpkts': '0000000000'},
             47: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'comment': 'OPM Channels',
                  'goodbytes': '0000000000',
                  'goodpkts': '0000000000'},
             48: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'comment': 'OPM Channels',
                  'goodbytes': '0000000000',
                  'goodpkts': '0000000000'},
             49: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'comment': 'OPM Channels',
                  'goodbytes': '0000000000',
                  'goodpkts': '0000000000'},
             50: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'comment': 'OPM Channels',
                  'goodbytes': '0000000000',
                  'goodpkts': '0000000000'},
             51: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'comment': 'OPM Channels',
                  'goodbytes': '0000000000',
                  'goodpkts': '0000000000'},
             52: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'comment': 'OPM Channels',
                  'goodbytes': '0000000000',
                  'goodpkts': '0000000000'},
             53: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'comment': 'OPM Channels',
                  'goodbytes': '0000000000',
                  'goodpkts': '0000000000'},
             54: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'comment': 'OPM Channels',
                  'goodbytes': '0000000000',
                  'goodpkts': '0000000000'},
             55: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'comment': 'OPM Channels',
                  'goodbytes': '0000000000',
                  'goodpkts': '0000000000'},
             56: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'comment': 'Metapacket/Recycle Pools 0-3',
                  'goodbytes': '0000000620',
                  'goodpkts': '000000001c'},
             57: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'comment': 'Metapacket/Recycle Pools 0-3',
                  'goodbytes': '0000000000',
                  'goodpkts': '0000000000'},
             58: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'comment': 'Metapacket/Recycle Pools 0-3',
                  'goodbytes': '0000000000',
                  'goodpkts': '0000000000'},
             59: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'comment': 'Metapacket/Recycle Pools 0-3',
                  'goodbytes': '0000000000',
                  'goodpkts': '0000000000'},
             60: {'badbytes': '0000000000',
                  'badpkts': '0000000000',
                  'comment': 'Reassembled Packets Sent to QED',
                  'goodbytes': '0000000000',
                  'goodpkts': '0000000000'}}}


    golden_output_active_ipm = {'execute.return_value': '''\
        Router#show platform hardware qfp active bqs 0 ipm statistics channel all
        Load for five secs: 25%/2%; one minute: 9%; five minutes: 9%
        Time source is NTP, 07:43:10.431 EST Thu Sep 8 2016

        BQS IPM Channel Statistics

        Chan   GoodPkts  GoodBytes    BadPkts   BadBytes

         1 - 0000000000 0000000000 0000000000 0000000000
         2 - 0000000000 0000000000 0000000000 0000000000
         3 - 0000000000 0000000000 0000000000 0000000000
         4 - 0000000000 0000000000 0000000000 0000000000
         5 - 0000000000 0000000000 0000000000 0000000000
         6 - 0000000000 0000000000 0000000000 0000000000
         7 - 0000c40f64 016a5004b0 0000000000 0000000000
         8 - 00000afbe9 00153685bd 0000000000 0000000000
         9 - 0000288e4f 0012139723 0000000000 0000000000
        10 - 000000223f 00000b2184 0000000000 0000000000
        11 - 000053ff08 0023f74c7a 0000000000 0000000000
        12 - 0000009533 0000305734 0000000000 0000000000
        13 - 0000000749 0000010ce4 0000000000 0000000000
        14 - 0000000000 0000000000 0000000000 0000000000
        15 - 0000000000 0000000000 0000000000 0000000000
        16 - 0000000000 0000000000 0000000000 0000000000
        17 - 0000000000 0000000000 0000000000 0000000000
        18 - 0000000000 0000000000 0000000000 0000000000
        19 - 00000d968e 000aba8f64 0000000000 0000000000
        20 - 0000000000 0000000000 0000000000 0000000000
        21 - 0000000000 0000000000 0000000000 0000000000
        22 - 0000000000 0000000000 0000000000 0000000000
        23 - 0000000000 0000000000 0000000000 0000000000
        24 - 0000000000 0000000000 0000000000 0000000000
    '''}

    golden_output_active_opm = {'execute.return_value': '''\
        Router#show platform hardware qfp active bqs 0 opm statistics channel all
        Load for five secs: 6%/0%; one minute: 9%; five minutes: 9%
        Time source is NTP, 07:45:18.968 EST Thu Sep 8 2016

        BQS OPM Channel Statistics

        Chan   GoodPkts  GoodBytes    BadPkts   BadBytes

         0 - 0000d18caf 01787bc9e1 0000000000 0000000000
         1 - 0000000000 0000000000 0000000000 0000000000
         2 - 0000000000 0000000000 0000000000 0000000000
         3 - 0000000000 0000000000 0000000000 0000000000
         4 - 0000000000 0000000000 0000000000 0000000000
         5 - 0000000000 0000000000 0000000000 0000000000
         6 - 0000000000 0000000000 0000000000 0000000000
         7 - 0000000000 0000000000 0000000000 0000000000
         8 - 0000000000 0000000000 0000000000 0000000000
         9 - 0000000000 0000000000 0000000000 0000000000
        10 - 0000000000 0000000000 0000000000 0000000000
        11 - 0000000000 0000000000 0000000000 0000000000
        12 - 0000000000 0000000000 0000000000 0000000000
        13 - 0000000000 0000000000 0000000000 0000000000
        14 - 0000000000 0000000000 0000000000 0000000000
        15 - 0000000000 0000000000 0000000000 0000000000
        16 - 0000000000 0000000000 0000000000 0000000000
        17 - 0000000000 0000000000 0000000000 0000000000
        18 - 0000000000 0000000000 0000000000 0000000000
        19 - 0000000000 0000000000 0000000000 0000000000
        20 - 0000416122 001ab1e8ad 0000000000 0000000000
        21 - 000012481d 000eac93b2 0000000000 0000000000
        22 - 00000a3c55 0004353727 0000000000 0000000000
        23 - 000015b68d 00131e7f90 0000000000 0000000000
        24 - 0000000749 00000b6ce8 0000000000 0000000000
        25 - 0000000000 0000000000 0000000000 0000000000
        26 - 0000000000 0000000000 0000000000 0000000000
        27 - 0000000000 0000000000 0000000000 0000000000
        28 - 0000000000 0000000000 0000000000 0000000000
        29 - 0000000000 0000000000 0000000000 0000000000
        30 - 00000e35a9 0016872998 0000000000 0000000000
        31 - 0000000000 0000000000 0000000000 0000000000
        32 - 0000000000 0000000000 0000000000 0000000000
        33 - 0000000000 0000000000 0000000000 0000000000
        34 - 0000000000 0000000000 0000000000 0000000000
        35 - 0000000000 0000000000 0000000000 0000000000
        36 - 0000000000 0000000000 0000000000 0000000000
        37 - 0000000000 0000000000 0000000000 0000000000
        38 - 0000007f33 00018a62d0 0000000000 0000000000
        39 - 0000000fd2 00000f3110 0000000000 0000000000
        40 - 0000000000 0000000000 0000000000 0000000000
        41 - 0000000000 0000000000 0000000000 0000000000
        42 - 0000000010 0000000300 0000000000 0000000000
        43 - 002f8bbd4a 0830f8d074 0000000000 0000000000
        44 - 0001b1b8d0 002f7036c0 0000000000 0000000000
        45 - 0000000000 0000000000 0000000000 0000000000
        46 - 0000000000 0000000000 0000000000 0000000000
        47 - 0000000000 0000000000 0000000000 0000000000
        48 - 0000000000 0000000000 0000000000 0000000000
        49 - 0000000000 0000000000 0000000000 0000000000
        50 - 0000000000 0000000000 0000000000 0000000000
        51 - 0000000000 0000000000 0000000000 0000000000
        52 - 0000000000 0000000000 0000000000 0000000000
        53 - 0000000000 0000000000 0000000000 0000000000
        54 - 0000000000 0000000000 0000000000 0000000000
        55 - 0000000000 0000000000 0000000000 0000000000
        56 - 000000001c 0000000620 0000000000 0000000000
        57 - 0000000000 0000000000 0000000000 0000000000
        58 - 0000000000 0000000000 0000000000 0000000000
        59 - 0000000000 0000000000 0000000000 0000000000
        60 - 0000000000 0000000000 0000000000 0000000000
         0-55: OPM Channels
        56-59: Metapacket/Recycle Pools 0-3
           60: Reassembled Packets Sent to QED
    '''}


    def test_empty(self):
        self.device = Mock(**self.empty_output)
        platform_obj = ShowPlatformHardwareQfpBqsStatisticsChannelAll(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = platform_obj.parse(status='active', slot='0', iotype='ipm')    

    def test_golden_active_ipm(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_active_ipm)
        platform_obj = ShowPlatformHardwareQfpBqsStatisticsChannelAll(device=self.device)
        parsed_output = platform_obj.parse(status='active', slot='0', iotype='ipm')
        self.assertEqual(parsed_output,self.golden_parsed_output_active_ipm)

    def test_golden_active_opm(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_active_opm)
        platform_obj = ShowPlatformHardwareQfpBqsStatisticsChannelAll(device=self.device)
        parsed_output = platform_obj.parse(status='active', slot='0', iotype='opm')
        self.assertEqual(parsed_output,self.golden_parsed_output_active_opm)

class ShowPlatformHardwareQfpInterface(unittest.TestCase):

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {
        'qfp': {
            'active': {
                'interface': {
                    'GigabitEthernet0/0/0': {
                        'egress_drop_stats': {},
                        'ingress_drop_stats': {},
                        'platform_handle': 7,
                        'receive_stats': {
                            'FragIpv4': {
                                'octets': 0,
                                'packets': 0,
                            },
                            'FragIpv6': {
                                'octets': 0,
                                'packets': 0,
                            },
                            'Ipv4': {
                                'octets': 306,
                                'packets': 4,
                            },
                            'Ipv6': {
                                'octets': 0,
                                'packets': 0,
                            },
                            'McastIpv4': {
                                'octets': 0,
                                'packets': 0,
                            },
                            'McastIpv6': {
                                'octets': 0,
                                'packets': 0,
                            },
                            'Other': {
                                'octets': 0,
                                'packets': 0,
                            },
                            'ReassIpv4': {
                                'octets': 0,
                                'packets': 0,
                            },
                            'ReassIpv6': {
                                'octets': 0,
                                'packets': 0,
                            },
                            'Tag': {
                                'octets': 0,
                                'packets': 0,
                            },
                        },
                        'transmit_stats': {
                            'FragmentedIpv4': {
                                'octets': 0,
                                'packets': 0,
                            },
                            'FragmentedIpv6': {
                                'octets': 0,
                                'packets': 0,
                            },
                            'FragmentsIpv4': {
                                'octets': 0,
                                'packets': 0,
                            },
                            'FragmentsIpv6': {
                                'octets': 0,
                                'packets': 0,
                            },
                            'Ipv4': {
                                'octets': 246,
                                'packets': 3,
                            },
                            'Ipv6': {
                                'octets': 0,
                                'packets': 0,
                            },
                            'McastIpv4': {
                                'octets': 0,
                                'packets': 0,
                            },
                            'McastIpv6': {
                                'octets': 0,
                                'packets': 0,
                            },
                            'Other': {
                                'octets': 0,
                                'packets': 0,
                            },
                            'Tag': {
                                'octets': 77,
                                'packets': 1,
                            },
                        },
                    },
                }
            }
        },
    }

    golden_output = {'execute.return_value': '''\
        Router#show platform hardware qfp active interface if-name gigabitEthernet 0/0/0 statistics
        Load for five secs: 2%/0%; one minute: 8%; five minutes: 8%
        Time source is NTP, 07:55:23.913 EST Thu Sep 8 2016
        Platform Handle 7
        ----------------------------------------------------------------
        Receive Stats                             Packets        Octets
        ----------------------------------------------------------------
          Ipv4                                       4             306
          Ipv6                                       0               0
          Tag                                        0               0
          McastIpv4                                  0               0
          McastIpv6                                  0               0
          FragIpv4                                   0               0
          FragIpv6                                   0               0
          ReassIpv4                                  0               0
          ReassIpv6                                  0               0
          Other                                      0               0

        ----------------------------------------------------------------
        Transmit Stats                            Packets        Octets
        ----------------------------------------------------------------
          Ipv4                                       3             246
          Ipv6                                       0               0
          Tag                                        1              77
          McastIpv4                                  0               0
          McastIpv6                                  0               0
          FragmentsIpv4                              0               0
          FragmentsIpv6                              0               0
          FragmentedIpv4                             0               0
          FragmentedIpv6                             0               0
          Other                                      0               0

        ----------------------------------------------------------------
        Input Drop Stats                          Packets        Octets
        ----------------------------------------------------------------
          Ingress Drop stats are not enabled on this interface

        ----------------------------------------------------------------
        Output Drop Stats                         Packets        Octets
        ----------------------------------------------------------------
          The Egress Drop stats are not enabled on this interface
    '''}


    def test_empty(self):
        self.device = Mock(**self.empty_output)
        platform_obj = ShowPlatformHardwareQfpInterfaceIfnameStatistics(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = platform_obj.parse(status='active', interface='gigabitEthernet 0/0/0')  

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        platform_obj = ShowPlatformHardwareQfpInterfaceIfnameStatistics(device=self.device)
        parsed_output = platform_obj.parse(status='active', interface='gigabitEthernet 0/0/0')
        self.assertEqual(parsed_output,self.golden_parsed_output)


class TestShowPlatformHardwareQfpStatisticsDrop(unittest.TestCase):

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output_active = {
      "global_drop_stats": {
        "Ipv4NoAdj": {
          "octets": 296,
          "packets": 7
        },
        "Ipv4NoRoute": {
          "octets": 7964,
          "packets": 181
        },
        "PuntPerCausePolicerDrops": {
          "octets": 184230,
          "packets": 2003
        },
        "UidbNotCfgd": {
          "octets": 29312827,
          "packets": 466391
        },
        "UnconfiguredIpv4Fia": {
          "octets": 360,
          "packets": 6
        }
      }
    }

    golden_output_active = {'execute.return_value': '''\
        Router#show platform hardware qfp active statistics drop | exclude _0_
        Load for five secs: 2%/1%; one minute: 9%; five minutes: 8%
        Time source is NTP, 07:47:11.317 EST Thu Sep 8 2016
        -------------------------------------------------------------------------
        Global Drop Stats                         Packets                  Octets  
        -------------------------------------------------------------------------
        Ipv4NoAdj                                       7                     296  
        Ipv4NoRoute                                   181                    7964  
        PuntPerCausePolicerDrops                     2003                  184230  
        UidbNotCfgd                                466391                29312827  
        UnconfiguredIpv4Fia                             6                     360  
    '''}


    def test_empty(self):
        self.device = Mock(**self.empty_output)
        platform_obj = ShowPlatformHardwareQfpStatisticsDrop(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = platform_obj.parse(status='active')    

    def test_golden_active(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_active)
        platform_obj = ShowPlatformHardwareQfpStatisticsDrop(device=self.device)
        parsed_output = platform_obj.parse(status='active')
        self.assertEqual(parsed_output,self.golden_parsed_output_active)


class TestShowProcessesCpuHistory(unittest.TestCase):
    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
         '60m': {1: {'average': 10, 'maximum': 51},
                 2: {'average': 20, 'maximum': 69},
                 3: {'average': 10, 'maximum': 56},
                 4: {'average': 10, 'maximum': 15},
                 5: {'average': 20, 'maximum': 75},
                 6: {'average': 10, 'maximum': 21},
                 7: {'average': 30, 'maximum': 99},
                 8: {'average': 50, 'maximum': 98},
                 9: {'average': 80, 'maximum': 99},
                 10: {'average': 20, 'maximum': 98},
                 11: {'average': 80, 'maximum': 98},
                 12: {'average': 20, 'maximum': 99},
                 13: {'average': 30, 'maximum': 98},
                 14: {'average': 0, 'maximum': 9},
                 15: {'average': 0, 'maximum': 11},
                 16: {'average': 0, 'maximum': 18},
                 17: {'average': 40, 'maximum': 98},
                 18: {'average': 0, 'maximum': 14},
                 19: {'average': 10, 'maximum': 94},
                 20: {'average': 10, 'maximum': 50},
                 21: {'average': 0, 'maximum': 10},
                 22: {'average': 0, 'maximum': 10},
                 23: {'average': 0, 'maximum': 11},
                 24: {'average': 0, 'maximum': 16},
                 25: {'average': 0, 'maximum': 10},
                 26: {'average': 0, 'maximum': 10},
                 27: {'average': 10, 'maximum': 77},
                 28: {'average': 0, 'maximum': 10},
                 29: {'average': 0, 'maximum': 10},
                 30: {'average': 0, 'maximum': 11},
                 31: {'average': 0, 'maximum': 7},
                 32: {'average': 0, 'maximum': 10},
                 33: {'average': 0, 'maximum': 14},
                 34: {'average': 0, 'maximum': 10},
                 35: {'average': 0, 'maximum': 10},
                 36: {'average': 0, 'maximum': 10},
                 37: {'average': 0, 'maximum': 10},
                 38: {'average': 10, 'maximum': 48},
                 39: {'average': 10, 'maximum': 67},
                 40: {'average': 0, 'maximum': 10},
                 41: {'average': 0, 'maximum': 7},
                 42: {'average': 0, 'maximum': 15},
                 43: {'average': 0, 'maximum': 15},
                 44: {'average': 0, 'maximum': 10},
                 45: {'average': 0, 'maximum': 10},
                 46: {'average': 0, 'maximum': 10},
                 47: {'average': 0, 'maximum': 10},
                 48: {'average': 0, 'maximum': 10},
                 49: {'average': 0, 'maximum': 10},
                 50: {'average': 0, 'maximum': 10},
                 51: {'average': 0, 'maximum': 10},
                 52: {'average': 0, 'maximum': 11},
                 53: {'average': 0, 'maximum': 10},
                 54: {'average': 0, 'maximum': 10},
                 55: {'average': 0, 'maximum': 10},
                 56: {'average': 0, 'maximum': 11},
                 57: {'average': 0, 'maximum': 10},
                 58: {'average': 0, 'maximum': 14},
                 59: {'average': 0, 'maximum': 14},
                 60: {'average': 0, 'maximum': 12}},
         '60s': {1: {'average': 0, 'maximum': 7},
                 2: {'average': 0, 'maximum': 7},
                 3: {'average': 0, 'maximum': 7},
                 4: {'average': 0, 'maximum': 7},
                 5: {'average': 0, 'maximum': 7},
                 6: {'average': 0, 'maximum': 5},
                 7: {'average': 0, 'maximum': 5},
                 8: {'average': 0, 'maximum': 5},
                 9: {'average': 0, 'maximum': 5},
                 10: {'average': 0, 'maximum': 5},
                 11: {'average': 0, 'maximum': 89},
                 12: {'average': 0, 'maximum': 89},
                 13: {'average': 0, 'maximum': 89},
                 14: {'average': 0, 'maximum': 89},
                 15: {'average': 0, 'maximum': 89},
                 16: {'average': 0, 'maximum': 66},
                 17: {'average': 0, 'maximum': 66},
                 18: {'average': 0, 'maximum': 66},
                 19: {'average': 0, 'maximum': 66},
                 20: {'average': 0, 'maximum': 66},
                 21: {'average': 0, 'maximum': 14},
                 22: {'average': 0, 'maximum': 14},
                 23: {'average': 0, 'maximum': 14},
                 24: {'average': 0, 'maximum': 14},
                 25: {'average': 0, 'maximum': 14},
                 26: {'average': 0, 'maximum': 6},
                 27: {'average': 0, 'maximum': 6},
                 28: {'average': 0, 'maximum': 6},
                 29: {'average': 0, 'maximum': 6},
                 30: {'average': 0, 'maximum': 6},
                 31: {'average': 0, 'maximum': 3},
                 32: {'average': 0, 'maximum': 3},
                 33: {'average': 0, 'maximum': 3},
                 34: {'average': 0, 'maximum': 3},
                 35: {'average': 0, 'maximum': 3},
                 36: {'average': 0, 'maximum': 5},
                 37: {'average': 0, 'maximum': 5},
                 38: {'average': 0, 'maximum': 5},
                 39: {'average': 0, 'maximum': 5},
                 40: {'average': 0, 'maximum': 5},
                 41: {'average': 0, 'maximum': 4},
                 42: {'average': 0, 'maximum': 4},
                 43: {'average': 0, 'maximum': 4},
                 44: {'average': 0, 'maximum': 4},
                 45: {'average': 0, 'maximum': 4},
                 46: {'average': 0, 'maximum': 16},
                 47: {'average': 0, 'maximum': 16},
                 48: {'average': 0, 'maximum': 16},
                 49: {'average': 0, 'maximum': 16},
                 50: {'average': 0, 'maximum': 16},
                 51: {'average': 0, 'maximum': 7},
                 52: {'average': 0, 'maximum': 7},
                 53: {'average': 0, 'maximum': 7},
                 54: {'average': 0, 'maximum': 7},
                 55: {'average': 0, 'maximum': 7},
                 56: {'average': 0, 'maximum': 7},
                 57: {'average': 0, 'maximum': 7},
                 58: {'average': 0, 'maximum': 7},
                 59: {'average': 0, 'maximum': 7},
                 60: {'average': 0, 'maximum': 7}},
         '72h': {1: {'average': 0, 'maximum': 73},
                 2: {'average': 0, 'maximum': 15},
                 3: {'average': 0, 'maximum': 82},
                 4: {'average': 0, 'maximum': 15},
                 5: {'average': 0, 'maximum': 15},
                 6: {'average': 0, 'maximum': 16},
                 7: {'average': 0, 'maximum': 14},
                 8: {'average': 0, 'maximum': 19},
                 9: {'average': 0, 'maximum': 14},
                 10: {'average': 0, 'maximum': 15},
                 11: {'average': 0, 'maximum': 15},
                 12: {'average': 0, 'maximum': 15},
                 13: {'average': 0, 'maximum': 15},
                 14: {'average': 0, 'maximum': 15},
                 15: {'average': 0, 'maximum': 15},
                 16: {'average': 0, 'maximum': 15},
                 17: {'average': 0, 'maximum': 15},
                 18: {'average': 0, 'maximum': 15},
                 19: {'average': 0, 'maximum': 15},
                 20: {'average': 0, 'maximum': 83},
                 21: {'average': 0, 'maximum': 78},
                 22: {'average': 0, 'maximum': 82},
                 23: {'average': 0, 'maximum': 77},
                 24: {'average': 0, 'maximum': 19},
                 25: {'average': 0, 'maximum': 66},
                 26: {'average': 0, 'maximum': 14},
                 27: {'average': 0, 'maximum': 77},
                 28: {'average': 10, 'maximum': 99},
                 29: {'average': 10, 'maximum': 100},
                 30: {'average': 0, 'maximum': 0},
                 31: {'average': 0, 'maximum': 0},
                 32: {'average': 0, 'maximum': 0},
                 33: {'average': 0, 'maximum': 0},
                 34: {'average': 0, 'maximum': 0},
                 35: {'average': 0, 'maximum': 0},
                 36: {'average': 0, 'maximum': 0},
                 37: {'average': 0, 'maximum': 0},
                 38: {'average': 0, 'maximum': 0},
                 39: {'average': 0, 'maximum': 0},
                 40: {'average': 0, 'maximum': 0},
                 41: {'average': 0, 'maximum': 0},
                 42: {'average': 0, 'maximum': 0},
                 43: {'average': 0, 'maximum': 0},
                 44: {'average': 0, 'maximum': 0},
                 45: {'average': 0, 'maximum': 0},
                 46: {'average': 0, 'maximum': 0},
                 47: {'average': 0, 'maximum': 0},
                 48: {'average': 0, 'maximum': 0},
                 49: {'average': 0, 'maximum': 0},
                 50: {'average': 0, 'maximum': 0},
                 51: {'average': 0, 'maximum': 0},
                 52: {'average': 0, 'maximum': 0},
                 53: {'average': 0, 'maximum': 0},
                 54: {'average': 0, 'maximum': 0},
                 55: {'average': 0, 'maximum': 0},
                 56: {'average': 0, 'maximum': 0},
                 57: {'average': 0, 'maximum': 0},
                 58: {'average': 0, 'maximum': 0},
                 59: {'average': 0, 'maximum': 0},
                 60: {'average': 0, 'maximum': 0},
                 61: {'average': 0, 'maximum': 0},
                 62: {'average': 0, 'maximum': 0},
                 63: {'average': 0, 'maximum': 0},
                 64: {'average': 0, 'maximum': 0},
                 65: {'average': 0, 'maximum': 0},
                 66: {'average': 0, 'maximum': 0},
                 67: {'average': 0, 'maximum': 0},
                 68: {'average': 0, 'maximum': 0},
                 69: {'average': 0, 'maximum': 0},
                 70: {'average': 0, 'maximum': 0},
                 71: {'average': 0, 'maximum': 0},
                 72: {'average': 0, 'maximum': 0}
            }
        }
    
    golden_output = {'execute.return_value': '''\
Router#show processes cpu history 
Load for five secs: 9%/1%; one minute: 18%; five minutes: 19%
Time source is NTP, 15:54:30.599 EST Tue Oct 18 2016                                       
                                                                  
                888886666611111                    11111          
      777775555599999666664444466666333335555544444666667777777777
  100                                                           
   90           *****                                           
   80           *****                                           
   70           **********                                      
   60           **********                                      
   50           **********                                      
   40           **********                                      
   30           **********                                      
   20           **********                         *****        
   10 ******************************     *****     *************
     0....5....1....1....2....2....3....3....4....4....5....5....6
               0    5    0    5    0    5    0    5    0    5    0
               CPU% per second (last 60 seconds)
                                         
                                                                  
      5651729999999 1191951111117111 111111461 1111111111111111111
      196551989889891884400016007001704000087075500000000100010442
  100       *******   *                                         
   90       *******   * *                                       
   80     * **#*#**   * *       *                               
   70  *  * **#*#**   * *       *           *                   
   60  ** * **#*#**   * *       *           *                   
   50 *** * *##*#**   * **      *          **                   
   40 *** * *##*#**   # **      *          **                   
   30 *** * ###*#*#   # **      *          **                   
   20 *#**#*#######  *# **   *  *          **  **               
   10 #############***#*##******#**********##*******************
     0....5....1....1....2....2....3....3....4....4....5....5....6
               0    5    0    5    0    5    0    5    0    5    0
               CPU% per minute (last 60 minutes)
              * = maximum CPU%   # = average CPU%
                                                     
                                  1                                           
      71811111111111111118787161790                                           
      35255649455555555553827964790                                           
  100                            **                                         
   90                            **                                         
   80   *                ****   ***                                         
   70 * *                **** * ***                                         
   60 * *                **** * ***                                         
   50 * *                **** * ***                                         
   40 * *                **** * ***                                         
   30 * *                **** * ***                                         
   20 ****** * **************** ***                                         
   10 ***************************##                                         
     0....5....1....1....2....2....3....3....4....4....5....5....6....6....7..
               0    5    0    5    0    5    0    5    0    5    0    5    0  
                   CPU% per hour (last 72 hours)
                  * = maximum CPU%   # = average CPU%
    '''}


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
        self.assertEqual(parsed_output,self.golden_parsed_output)


class TestShowProcessMemory(unittest.TestCase):
    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'lsmi_io_pool': {
            'free': 832,
            'total': 6295128,
            'used': 6294296,
        },
        'pid': {
            0: {
                'index': {
                    1: {
                        'allocated': 678985440,
                        'freed': 347855496,
                        'getbufs': 428,
                        'holding': 304892096,
                        'pid': 0,
                        'process': '*Init*',
                        'retbufs': 2134314,
                        'tty': 0,
                    },
                    2: {
                        'allocated': 800,
                        'freed': 4965889216,
                        'getbufs': 17,
                        'holding': 800,
                        'pid': 0,
                        'process': '*Sched*',
                        'retbufs': 17,
                        'tty': 0,
                    },
                    3: {
                        'allocated': 2675774192,
                        'freed': 2559881512,
                        'getbufs': 2111,
                        'holding': 43465512,
                        'pid': 0,
                        'process': '*Dead*',
                        'retbufs': 351,
                        'tty': 0,
                    },
                    4: {
                        'allocated': 0,
                        'freed': 0,
                        'getbufs': 0,
                        'holding': 4070880,
                        'pid': 0,
                        'process': '*MallocLite*',
                        'retbufs': 0,
                        'tty': 0,
                    },
                },
            },
            1: {
                'index': {
                    1: {
                        'allocated': 3415536,
                        'freed': 879912,
                        'getbufs': 0,
                        'holding': 2565568,
                        'pid': 1,
                        'process': 'Chunk Manager',
                        'retbufs': 0,
                        'tty': 0,
                    },
                },
            },
        },
        'processor_pool': {
            'free': 9662451880,
            'total': 10147887840,
            'used': 485435960,
        },
        'reserve_p_pool': {
            'free': 102316,
            'total': 102404,
            'used': 88,
        },
    }

    golden_output = {'execute.return_value': '''\
        Load for five secs: 1%/0%; one minute: 1%; five minutes: 0%
        Time source is NTP, 21:28:35.662 JST Mon May 11 2020

        Processor Pool Total: 10147887840 Used:  485435960 Free: 9662451880
        reserve P Pool Total:     102404 Used:         88 Free:     102316
        lsmpi_io Pool Total:    6295128 Used:    6294296 Free:        832

        PID TTY  Allocated      Freed    Holding    Getbufs    Retbufs Process
        0   0  678985440  347855496  304892096        428    2134314 *Init*
        0   0        800 4965889216        800         17         17 *Sched*
        0   0 2675774192 2559881512   43465512       2111        351 *Dead*
        0   0          0          0    4070880          0          0 *MallocLite*
        1   0    3415536     879912    2565568          0          0 Chunk Manager
    '''}

    golden_parsed_output2 = {
        'processor_pool': {
            'total': 10147887840,
            'used': 487331816,
            'free': 9660556024,
        },
        'reserve_p_pool': {
            'total': 102404,
            'used': 88,
            'free': 102316,
        },
        'lsmi_io_pool': {
            'total': 6295128,
            'used': 6294296,
            'free': 832,
        }
    }

    golden_output2 = {'execute.return_value': '''\
        Processor Pool Total: 10147887840 Used:  487331816 Free: 9660556024
        reserve P Pool Total:     102404 Used:         88 Free:     102316
        lsmpi_io Pool Total:    6295128 Used:    6294296 Free:        832
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        platform_obj = ShowProcessesMemory(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = platform_obj.parse()    

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        platform_obj = ShowProcessesMemory(device=self.device)
        parsed_output = platform_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)
    
    def test_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        platform_obj = ShowProcessesMemory(device=self.device)
        parsed_output = platform_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output2)

if __name__ == '__main__':
    unittest.main()
