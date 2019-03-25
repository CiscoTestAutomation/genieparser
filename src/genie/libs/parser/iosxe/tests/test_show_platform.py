#!/bin/env python
import unittest
from unittest.mock import Mock
from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                       SchemaMissingKeyError
from genie.libs.parser.iosxe.show_platform import ShowVersion,\
                                                  Dir,\
                                                  ShowRedundancy,\
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
                                                  ShowProcessesCpu


class test_show_version(unittest.TestCase):

    dev1 = Device(name='empty')
    dev2 = Device(name='semi_empty')
    dev_asr1k = Device(name='asr1k')
    dev_c3850 = Device(name='c3850')
    dev_isr4k = Device(name='isr4k')
    empty_output = {'execute.return_value': ''}
    semi_empty_output = {'execute.return_value': '''\
        Cisco IOS-XE software, Copyright (c) 2005-2017 by cisco Systems, Inc.
    '''}

    golden_parsed_output_c3850 = {
        'version': {
            'version_short': '16.4',
            'platform': 'Catalyst L3 Switch',
            'version': '16.4.20170410:165034',
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
            'curr_config_register': '0x2102',
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
                'Gigabit Ethernet': '4'
            },
            'os': 'IOS-XE',
            'platform': 'ISR',
            'processor_type': '2RU',
            'rom': 'IOS-XE ROMMON',
            'rtr_type': 'ISR4451-X/K9',
            'system_image': 'bootflash:isr4400-universalk9.16.06.05.SPA.bin',
            'system_restarted_at': '07:19:15 UTC Fri Feb 1 2019',
            'uptime': '2 days, 3 hours, 18 minutes',
            'uptime_this_cp': '2 days, 3 hours, 19 minutes',
            'version': '16.6.5,',
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
        System image file is "bootflash:isr4400-universalk9.16.06.05.SPA.bin"
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

class test_dir(unittest.TestCase):
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


class test_show_redundancy(unittest.TestCase):
    dev1 = Device(name='empty')
    dev2 = Device(name='semi_empty')
    dev_asr1k = Device(name='asr1k')
    dev_c3850 = Device(name='c3850')
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


class test_show_inventory(unittest.TestCase):
    dev1 = Device(name='empty')
    dev2 = Device(name='semi_empty')
    dev_asr1k = Device(name='asr1k')
    dev_c3850 = Device(name='c3850')
    empty_output = {'execute.return_value': ''}
    semi_empty_output = {'execute.return_value': '''/
        NAME: "c38xx Stack", DESCR: "c38xx Stack"
        PID: WS-C3850-24P-E    , VID: V01  , SN: FCW1932D0LB

        NAME: "Switch 1", DESCR: "WS-C3850-24P-E"
        PID: WS-C3850-24P-E    , VID: V01  ,
    '''}

    golden_parsed_output_c3850 = {
                                    'main': {
                                        'swstack': True,
                                    },
                                    'slot': {
                                        '1': {
                                            'rp': {
                                                'WS-C3850-24P-E': {
                                                    'name': 'Switch 1',
                                                    'descr': 'WS-C3850-24P-E',
                                                    'pid': 'WS-C3850-24P-E',
                                                    'vid': 'V01',
                                                    'sn': 'FCW1932D0LB',
                                                    'subslot': {
                                                        '1': {
                                                            'STACK-T1-50CM': {
                                                                'name': 'StackPort1/1',
                                                                'descr': 'StackPort1/1',
                                                                'pid': 'STACK-T1-50CM',
                                                                'vid': 'V01',
                                                                'sn': 'LCC1921G11G',
                                                            }
                                                        },
                                                        '2': {
                                                            'STACK-T1-50CM': {
                                                                'name': 'StackPort1/2',
                                                                'descr': 'StackPort1/2',
                                                                'pid': 'STACK-T1-50CM',
                                                                'vid': 'V01',
                                                                'sn': 'LCC1921G250',
                                                            }
                                                        },
                                                    }
                                                }
                                            },
                                            'other': {
                                                'C3KX-PWR-715WAC': {
                                                    'name': 'Switch 1 - Power Supply A',
                                                    'descr': 'Switch 1 - Power Supply A',
                                                    'pid': 'C3KX-PWR-715WAC',
                                                    'vid': 'V01',
                                                    'sn': 'LIT14291MTJ',
                                                }
                                            },
                                        },
                                        '2': {
                                            'rp': {
                                                'WS-C3850-24P-E': {
                                                    'name': 'Switch 2',
                                                    'descr': 'WS-C3850-24P-E',
                                                    'pid': 'WS-C3850-24P-E',
                                                    'vid': 'V04',
                                                    'sn': 'FOC1932X0K1',
                                                    'subslot': {
                                                        '1': {
                                                            'STACK-T1-50CM': {
                                                                'name': 'StackPort2/1',
                                                                'descr': 'StackPort2/1',
                                                                'pid': 'STACK-T1-50CM',
                                                                'vid': 'V01',
                                                                'sn': 'MOC1932A0BU',
                                                            }
                                                        },
                                                        '2': {
                                                            'STACK-T1-50CM': {
                                                                'name': 'StackPort2/2',
                                                                'descr': 'StackPort2/2',
                                                                'pid': 'STACK-T1-50CM',
                                                                'vid': 'V01',
                                                                'sn': 'LCC1921G10J',
                                                            }
                                                        },
                                                    }
                                                }
                                            },
                                            'other': {
                                                'C3KX-PWR-715WAC': {
                                                    'name': 'Switch 2 - Power Supply A',
                                                    'descr': 'Switch 2 - Power Supply A',
                                                    'pid': 'C3KX-PWR-715WAC',
                                                    'vid': 'V01',
                                                    'sn': 'LIT15090DUL',
                                                }
                                            },
                                        },
                                        '3': {
                                            'rp': {
                                                'WS-C3850-24P-E': {
                                                    'name': 'Switch 3',
                                                    'descr': 'WS-C3850-24P-E',
                                                    'pid': 'WS-C3850-24P-E',
                                                    'vid': 'V04',
                                                    'sn': 'FCW1932C0MA',
                                                    'subslot': {
                                                        '1': {
                                                            'STACK-T1-50CM': {
                                                                'name': 'StackPort3/1',
                                                                'descr': 'StackPort3/1',
                                                                'pid': 'STACK-T1-50CM',
                                                                'vid': 'V01',
                                                                'sn': 'LCC1921G10J',
                                                            }
                                                        },
                                                        '2': {
                                                            'STACK-T1-50CM': {
                                                                'name': 'StackPort3/2',
                                                                'descr': 'StackPort3/2',
                                                                'pid': 'STACK-T1-50CM',
                                                                'vid': 'V01',
                                                                'sn': 'LCC1921G106',
                                                            }
                                                        },
                                                    }
                                                }
                                            },
                                            'other': {
                                                'PWR-C1-715WAC': {
                                                    'name': 'Switch 3 - Power Supply A',
                                                    'descr': 'Switch 3 - Power Supply A',
                                                    'pid': 'PWR-C1-715WAC',
                                                    'vid': 'V01',
                                                    'sn': 'LIT19220MG1',
                                                }
                                            },
                                        },
                                        '4': {
                                            'rp': {
                                                'WS-C3850-24P-E': {
                                                    'name': 'Switch 4',
                                                    'descr': 'WS-C3850-24P-E',
                                                    'pid': 'WS-C3850-24P-E',
                                                    'vid': 'V04',
                                                    'sn': 'FCW1932D0L0',
                                                    'subslot': {
                                                        '1': {
                                                            'STACK-T1-50CM': {
                                                                'name': 'StackPort4/1',
                                                                'descr': 'StackPort4/1',
                                                                'pid': 'STACK-T1-50CM',
                                                                'vid': 'V01',
                                                                'sn': 'LCC1921G250',
                                                            }
                                                        },
                                                        '2': {
                                                            'STACK-T1-50CM': {
                                                                'name': 'StackPort4/2',
                                                                'descr': 'StackPort4/2',
                                                                'pid': 'STACK-T1-50CM',
                                                                'vid': 'V01',
                                                                'sn': 'MOC1932A0BU',
                                                            }
                                                        },
                                                    }
                                                }
                                            },
                                            'other': {
                                                'C3KX-PWR-715WAC': {
                                                    'name': 'Switch 4 - Power Supply A',
                                                    'descr': '',
                                                    'pid': 'C3KX-PWR-715WAC',
                                                    'vid': 'V01',
                                                    'sn': 'LIT15140DEP',
                                                }
                                            },
                                        },
                                        '5': {
                                            'rp': {
                                                'WS-C3850-24P-E': {
                                                    'name': 'Switch 5',
                                                    'descr': 'WS-C3850-24P-E',
                                                    'pid': 'WS-C3850-24P-E',
                                                    'vid': 'V04',
                                                    'sn': 'FOC1932X0F9',
                                                    'subslot': {
                                                        '1': {
                                                            'STACK-T1-50CM': {
                                                                'name': 'StackPort5/1',
                                                                'descr': 'StackPort5/1',
                                                                'pid': 'STACK-T1-50CM',
                                                                'vid': 'V01',
                                                                'sn': 'LCC1921G106',
                                                            }
                                                        },
                                                        '2': {
                                                            'STACK-T1-50CM': {
                                                                'name': 'StackPort5/2',
                                                                'descr': 'StackPort5/2',
                                                                'pid': 'STACK-T1-50CM',
                                                                'vid': 'V01',
                                                                'sn': 'LCC1921G11G',
                                                            }
                                                        },
                                                    }
                                                }
                                            },
                                            'other': {
                                                'PWR-C1-715WAC': {
                                                    'name': 'Switch 5 - Power Supply A',
                                                    'descr': 'Switch 5 - Power Supply A',
                                                    'pid': 'PWR-C1-715WAC',
                                                    'vid': 'V01',
                                                    'sn': 'LIT17130ZDU',
                                                }
                                            },
                                        },
                                    }
                                }

    golden_output_c3850 = {'execute.return_value': '''\
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
                                                'name': 'Chassis',
                                                'descr': 'Cisco ASR1006 Chassis',
                                                'pid': 'ASR1006',
                                                'vid': 'V01',
                                                'sn': 'FOX1204G6WN',
                                            }
                                        }
                                    },
                                    'slot': {
                                        '0': {
                                            'lc': {
                                                'ASR1000-SIP40': {
                                                    'name': 'module 0',
                                                    'descr': 'Cisco ASR1000 SPA Interface Processor 40',
                                                    'pid': 'ASR1000-SIP40',
                                                    'vid': 'V02',
                                                    'sn': 'JAE200609WP',
                                                    'subslot': {
                                                        '0': {
                                                            'SPA-5X1GE-V2': {
                                                                'name': 'SPA subslot 0/0',
                                                                'descr': '5-port Gigabit Ethernet Shared Port Adapter',
                                                                'pid': 'SPA-5X1GE-V2',
                                                                'vid': 'V02',
                                                                'sn': 'JAE151203T2',
                                                            }
                                                        },
                                                        '0 transceiver 0': {
                                                            'SP7041-E': {
                                                                'name': 'subslot 0/0 transceiver 0',
                                                                'descr': 'GE T',
                                                                'pid': 'SP7041-E',
                                                                'vid': 'E',
                                                                'sn': 'MTC164204VE',
                                                            }    
                                                        },
                                                        '0 transceiver 1': {
                                                            'SP7041-E': {
                                                                'name': 'subslot 0/0 transceiver 1',
                                                                'descr': 'GE T',
                                                                'pid': 'SP7041-E',
                                                                'vid': 'E',
                                                                'sn': 'MTC164204F0',
                                                            }    
                                                        },
                                                        '0 transceiver 2': {
                                                            'SP7041-E': {
                                                                'name': 'subslot 0/0 transceiver 2',
                                                                'descr': 'GE T',
                                                                'pid': 'SP7041-E',
                                                                'vid': 'E',
                                                                'sn': 'MTC164206U2',
                                                            }    
                                                        },
                                                        '0 transceiver 3': {
                                                            'SP7041-E': {
                                                                'name': 'subslot 0/0 transceiver 3',
                                                                'descr': 'GE T',
                                                                'pid': 'SP7041-E',
                                                                'vid': 'E',
                                                                'sn': 'MTC1644033S',
                                                            }    
                                                        },
                                                    }
                                                }
                                            }
                                        },
                                        'R0': {
                                            'rp': {
                                                'ASR1000-RP2': {
                                                    'name': 'module R0',
                                                    'descr': 'Cisco ASR1000 Route Processor 2',
                                                    'pid': 'ASR1000-RP2',
                                                    'vid': 'V02',
                                                    'sn': 'JAE153408NJ',
                                                }
                                            }
                                        },
                                        'R1': {
                                            'rp': {
                                                'ASR1000-RP2': {
                                                    'name': 'module R1',
                                                    'descr': 'Cisco ASR1000 Route Processor 2',
                                                    'pid': 'ASR1000-RP2',
                                                    'vid': 'V03',
                                                    'sn': 'JAE1703094H',
                                                }
                                            }
                                        },
                                        'F0': {
                                            'other': {
                                                'ASR1000-ESP20': {
                                                    'name': 'module F0',
                                                    'descr': 'Cisco ASR1000 Embedded Services Processor, 20Gbps',
                                                    'pid': 'ASR1000-ESP20',
                                                    'vid': 'V01',
                                                    'sn': 'JAE1239W7G6',
                                                }
                                            }
                                        },
                                        'P0': {
                                            'other': {
                                                'ASR1006-PWR-AC': {
                                                    'name': 'Power Supply Module 0',
                                                    'descr': 'Cisco ASR1006 AC Power Supply',
                                                    'pid': 'ASR1006-PWR-AC',
                                                    'vid': 'V01',
                                                    'sn': 'ART1210Q049',
                                                }
                                            }
                                        },
                                        'P1': {
                                            'other': {
                                                'ASR1006-PWR-AC': {
                                                    'name': 'Power Supply Module 1',
                                                    'descr': 'Cisco ASR1006 AC Power Supply',
                                                    'pid': 'ASR1006-PWR-AC',
                                                    'vid': 'V01',
                                                    'sn': 'ART1210Q04C',
                                                }
                                            }
                                        }
                                    }
                                }

    golden_output_asr1k = {'execute.return_value': '''\
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

    golden_parsed_output = {
        'slot': {
            'F0': {
                'lc': {
                    'ISR4331/K9': {
                        'sn': '',
                        'pid': 'ISR4331/K9',
                        'descr': 'Cisco ISR4331 Forwarding Processor',
                        'name': 'module F0',
                        'vid': '',
                        },
                    },
                },
            '1': {
                'lc': {
                    'ISR4331/K9': {
                        'sn': '',
                        'pid': 'ISR4331/K9',
                        'descr': 'Cisco ISR4331 Built-In SM controller',
                        'name': 'module 1',
                        'vid': '',
                        },
                    },
                },
            '0': {
                'lc': {
                    'ISR4331/K9': {
                        'descr': 'Cisco ISR4331 Built-In NIM controller',
                        'name': 'module 0',
                        'subslot': {
                            '0 transceiver 2': {
                                'SFP-GE-T': {
                                    'sn': 'MTC2139029X',
                                    'pid': 'SFP-GE-T',
                                    'descr': 'GE T',
                                    'name': 'subslot 0/0 transceiver 2',
                                    'vid': 'V02',
                                    },
                                },
                            },
                        'sn': '',
                        'pid': 'ISR4331/K9',
                        'vid': '',
                        },
                    },
                },
            'P0': {
                'other': {
                    'PWR-4330-AC': {
                        'sn': 'PST2150N1E2',
                        'pid': 'PWR-4330-AC',
                        'descr': '250W AC Power Supply for Cisco ISR 4330',
                        'name': 'Power Supply Module 0',
                        'vid': 'V02',
                        },
                    },
                },
            'R0': {
                'lc': {
                    'ISR4331/K9': {
                        'sn': 'FDO21520TGH',
                        'pid': 'ISR4331/K9',
                        'descr': 'Cisco ISR4331 Route Processor',
                        'name': 'module R0',
                        'vid': 'V04',
                        },
                    },
                },
            },
        'main': {
            'chassis': {
                'ISR4331/K9': {
                    'sn': 'FDO2201A0SR',
                    'pid': 'ISR4331/K9',
                    'descr': 'Cisco ISR4331 Chassis',
                    'name': 'Chassis',
                    'vid': 'V04',
                    },
                },
            },
        }

    golden_output = {'execute.return_value': '''\
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

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        inventory_obj = ShowInventory(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = inventory_obj.parse()

    # All parameters are Optional. So, no need to test semi empty output.
    # def test_semi_empty(self):
    #     self.dev2 = Mock(**self.semi_empty_output)
    #     inventory_obj = ShowInventory(device=self.dev2)
    #     with self.assertRaises(SchemaMissingKeyError):
    #         parsed_output = inventory_obj.parse()   

    def test_golden(self):
        self.maxDiff = None
        self.dev_asr1k = Mock(**self.golden_output)
        inventory_obj = ShowInventory(device=self.dev_asr1k)
        parsed_output = inventory_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_c3850(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_c3850)
        inventory_obj = ShowInventory(device=self.dev_c3850)
        parsed_output = inventory_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_c3850)

    def test_golden_asr1k(self):
        self.maxDiff = None
        self.dev_asr1k = Mock(**self.golden_output_asr1k)
        inventory_obj = ShowInventory(device=self.dev_asr1k)
        parsed_output = inventory_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_asr1k)

class test_show_platform(unittest.TestCase):
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

    golden_parsed_output_c3850 = {
                                    'main': {
                                        'switch_mac_address': '0057.d21b.cc00',
                                        'mac_persistency_wait_time': 'indefinite',
                                    },
                                    'slot': {
                                        '1': {
                                            'rp': {
                                                'WS-C3850-24P-E': {
                                                    'hw_ver': 'V07',
                                                    'mac_address': '0057.d21b.cc00',
                                                    'name': 'WS-C3850-24P-E',
                                                    'ports': '32',
                                                    'priority': '3',
                                                    'role': 'Active',
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
                                                    'priority': '1',
                                                    'role': 'Member',
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
                                                    'priority': '1',
                                                    'role': 'Member',
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
                                                    'priority': '1',
                                                    'role': 'Member',
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
                                                    'priority': '1',
                                                    'role': 'Standby',
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
                'lc': {
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
                'lc': {
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


class test_show_boot(unittest.TestCase):
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


class test_show_switch_detail(unittest.TestCase):
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

class test_show_switch(unittest.TestCase):
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


class test_show_module(unittest.TestCase):
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


class test_show_platform_software_status_control_processor_brief(unittest.TestCase):

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


class test_show_platform_software_slot_active_monitor_Mem_Swap(unittest.TestCase):

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


class test_show_processes_cpu_sorted_CPU(unittest.TestCase):

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

class test_show_processes_cpu_platform(unittest.TestCase):
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
        Time source is NTP, 17:48:03.994 JST Wed Oct 19 2016
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


class test_show_env(unittest.TestCase):

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
        Time source is NTP, 17:41:24.716 JST Wed Oct 19 2016


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

class test_show_processes_cpu(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {}

    golden_output = {'execute.return_value': '''\
        Router#show process cpu
        Load for five secs: 1%/0%; one minute: 2%; five minutes: 3%
        Time source is NTP, 19:10:39.512 JST Mon Oct 17 2016

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
         407         914       65763         13  0.00%  0.00%  0.00%   0 OSPF-9996 Router 
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
         559         311       10680         29  0.00%  0.00%  0.00%   0 OSPF-9996 Hello  
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

    def test_golden(self):
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


if __name__ == '__main__':
    unittest.main()

