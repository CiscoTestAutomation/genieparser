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
                                       ShowEnvironmentAll, ShowModule, \
                                       ShowPlatformSoftwareStatusControl, \
                                       ShowPlatformSoftwareSlotActiveMonitorMem, \
                                       ShowProcessesCpuSorted



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


class test_show_environment_all(unittest.TestCase):
    dev1 = Device(name='empty')
    dev_c3850 = Device(name='c3850')
    empty_output = {'execute.return_value': '      '}

    golden_parsed_output_c3850 = {
        "switch": {
            "3": {
               "system_temperature_state": "ok",
               "hotspot_temperature": {
                    "yellow_threshold": "105",
                    "red_threshold": "125",
                    "state": "green",
                    "value": "43"
               },
               "power_supply": {
                    "2": {
                         "state": "not present",
                         "status": "not present"
                    },
                    "1": {
                         "pid": "PWR-C1-715WAC",
                         "serial_number": "DCB1844G1WW",
                         "watts": "715",
                         "system_power": "good",
                         "state": "ok",
                         "poe_power": "good",
                         "status": "ok"
                    }
               },
               "inlet_temperature": {
                    "yellow_threshold": "46",
                    "red_threshold": "56",
                    "state": "green",
                    "value": "33"
               },
               "fan": {
                    "3": {
                         "state": "ok"
                    },
                    "2": {
                         "state": "ok"
                    },
                    "1": {
                         "state": "ok"
                    }
               }
            },
            "2": {
               "system_temperature_state": "ok",
               "hotspot_temperature": {
                    "yellow_threshold": "105",
                    "red_threshold": "125",
                    "state": "green",
                    "value": "43"
               },
               "power_supply": {
                    "2": {
                         "state": "not present",
                         "status": "not present"
                    },
                    "1": {
                         "pid": "PWR-C1-715WAC",
                         "serial_number": "DCB1844G1X0",
                         "watts": "715",
                         "system_power": "good",
                         "state": "ok",
                         "poe_power": "good",
                         "status": "ok"
                    }
               },
               "inlet_temperature": {
                    "yellow_threshold": "46",
                    "red_threshold": "56",
                    "state": "green",
                    "value": "33"
               },
               "fan": {
                    "3": {
                         "state": "ok"
                    },
                    "2": {
                         "state": "ok"
                    },
                    "1": {
                         "state": "ok"
                    }
               }
            },
            "1": {
               "system_temperature_state": "ok",
               "hotspot_temperature": {
                    "yellow_threshold": "105",
                    "red_threshold": "125",
                    "state": "green",
                    "value": "45"
               },
               "power_supply": {
                    "2": {
                         "state": "not present",
                         "status": "not present"
                    },
                    "1": {
                         "pid": "PWR-C1-715WAC",
                         "serial_number": "DCB1844G1ZY",
                         "watts": "715",
                         "system_power": "good",
                         "state": "ok",
                         "poe_power": "good",
                         "status": "ok"
                    }
               },
               "inlet_temperature": {
                    "yellow_threshold": "46",
                    "red_threshold": "56",
                    "state": "green",
                    "value": "34"
               },
               "fan": {
                    "3": {
                         "state": "ok"
                    },
                    "2": {
                         "state": "ok"
                    },
                    "1": {
                         "state": "ok"
                    }
               }
            }
        }
    }

    golden_output_c3850 = {'execute.return_value': '''\
        Switch 1 FAN 1 is OK
        Switch 1 FAN 2 is OK
        Switch 1 FAN 3 is OK
        FAN PS-1 is OK
        FAN PS-2 is NOT PRESENT
        Switch 2 FAN 1 is OK
        Switch 2 FAN 2 is OK
        Switch 2 FAN 3 is OK
        FAN PS-1 is OK
        FAN PS-2 is NOT PRESENT
        Switch 3 FAN 1 is OK
        Switch 3 FAN 2 is OK
        Switch 3 FAN 3 is OK
        FAN PS-1 is OK
        FAN PS-2 is NOT PRESENT
        Switch 1: SYSTEM TEMPERATURE is OK
        Inlet Temperature Value: 34 Degree Celsius
        Temperature State: GREEN
        Yellow Threshold : 46 Degree Celsius
        Red Threshold    : 56 Degree Celsius

        Hotspot Temperature Value: 45 Degree Celsius
        Temperature State: GREEN
        Yellow Threshold : 105 Degree Celsius
        Red Threshold    : 125 Degree Celsius
        Switch 2: SYSTEM TEMPERATURE is OK
        Inlet Temperature Value: 33 Degree Celsius
        Temperature State: GREEN
        Yellow Threshold : 46 Degree Celsius
        Red Threshold    : 56 Degree Celsius

        Hotspot Temperature Value: 43 Degree Celsius
        Temperature State: GREEN
        Yellow Threshold : 105 Degree Celsius
        Red Threshold    : 125 Degree Celsius
        Switch 3: SYSTEM TEMPERATURE is OK
        Inlet Temperature Value: 33 Degree Celsius
        Temperature State: GREEN
        Yellow Threshold : 46 Degree Celsius
        Red Threshold    : 56 Degree Celsius

        Hotspot Temperature Value: 43 Degree Celsius
        Temperature State: GREEN
        Yellow Threshold : 105 Degree Celsius
        Red Threshold    : 125 Degree Celsius
        SW  PID                 Serial#     Status           Sys Pwr  PoE Pwr  Watts
        --  ------------------  ----------  ---------------  -------  -------  -----
        1A  PWR-C1-715WAC       DCB1844G1ZY  OK              Good     Good     715 
        1B  Not Present
        2A  PWR-C1-715WAC       DCB1844G1X0  OK              Good     Good     715 
        2B  Not Present
        3A  PWR-C1-715WAC       DCB1844G1WW  OK              Good     Good     715 
        3B  Not Present
    '''
    }

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        platform_obj = ShowEnvironmentAll(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = platform_obj.parse()    

    def test_golden(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_c3850)
        platform_obj = ShowEnvironmentAll(device=self.dev_c3850)
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


if __name__ == '__main__':
    unittest.main()

