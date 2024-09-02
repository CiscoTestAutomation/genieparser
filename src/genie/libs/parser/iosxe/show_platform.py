''' show_platform.py
IOSXE parsers for the following show commands:

    * 'show bootvar'
    * 'show version'
    * 'dir'
    * 'show redundancy'
    * 'show inventory'
    * 'show platform'
    * 'show boot'
    * 'show switch detail'
    * 'show switch'
    * 'show environment all'
    * 'show module'
    * 'show platform resources'
    * 'show platform sudi certificate sign nonce {sig}'
    * 'show environment status'
    * 'show platform sudi pki'
    * 'show platform packet-trace statistics'
    * 'show platform packet-trace summary'
    * 'show platform packet-trace all'
    * 'show version running'
    * 'show platform nat translations active statistics'
    * 'show platform nat translations active'
    * 'show call admission statistics'
    * 'show call admission statistics detailed'
    * 'show file systems'
    * 'show redundancy config-sync failures mcl'
    * 'show platform authentication sbinfo interface {interface}'
    * 'show platform usb status'
    * 'show xfsu status'
    * 'show graceful-reload'
    * 'show file information {file}'
    * 'show file descriptors detail'
    * 'show diagnostics status'
    * 'test platform software database get-n all ios_oper/platform_component'
    * 'test platform software database get-n all ios_oper/transceiver'
    '''

# Python
import re
import logging
from collections import OrderedDict
from sys import int_info
import xml.etree.ElementTree as ET
from xml.dom import minidom

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional, Use, And
from genie.libs.parser.utils.common import Common
from genie.parsergen import oper_fill_tabular
# genie.parsergen
try:
    import genie.parsergen
except (ImportError, OSError):
    pass

# pyATS
from pyats.utils.exceptions import SchemaTypeError

log = logging.getLogger(__name__)

class ShowBootvarSchema(MetaParser):
    """Schema for show bootvar"""

    schema = {
        Optional('current_boot_variable'): str,
        Optional('next_reload_boot_variable'): str,
        Optional('config_file'): str,
        Optional('bootldr'): str,
        Optional('active'): {
            Optional('configuration_register'): str,
            Optional("next_reload_configuration_register"): str,
            Optional('boot_variable'): str,
            Optional('manual_boot'): bool,
        },
        Optional('standby'): {
            Optional('configuration_register'): str,
            Optional("next_reload_configuration_register"): str,
            Optional('boot_variable'): str,
            Optional('standby_manual_boot'): bool,
        },
    }


class ShowBootvar(ShowBootvarSchema):
    """Parser for show bootvar"""

    cli_command = 'show bootvar'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        boot_dict = {}
        boot_variable = None

        # BOOT variable = bootflash:/asr1000rpx.bin,12;
        # BOOT variable = flash:cat3k_caa-universalk9.BLD_POLARIS_DEV_LATEST_20150907_031219.bin;flash:cat3k_caa-universalk9.BLD_POLARIS_DEV_LATEST_20150828_174328.SSA.bin;flash:ISSUCleanGolden;
        # BOOT variable = tftp:/auto/tftp-best/genie_images/genie_clean/asr1000-genie-image 255.255.255.255,12;
        # BOOT variable = tftp:/auto/tftp-best/genie_images/genie_clean/asr1000-genie-image 255.255.255.255,12;harddisk:/asr1000-genie-image_asr-MIB-1,12;
        p1 = re.compile(r'^BOOT +variable +=( *(?P<var>.+);?)?$')

        # Standby BOOT variable = bootflash:/asr1000rpx.bin,12;
        p2 = re.compile(r'^Standby +BOOT +variable +=( *(?P<var>\S+);)?$')

        # Configuration register is 0x2002
        # Configuration register is 0x2 (will be 0x2102 at next reload)
        # Configuration Register is 0x102
        p3 = re.compile(r'Configuration +[R|r]egister +is +(?P<var1>(\S+))'
                        r'(?: +\(will +be +(?P<var2>(\S+)) +at +next +reload\))?$')

        # Standby Configuration register is 0x2002
        # Standby Configuration register is 0x1  (will be 0x2102 at next reload)
        p4 = re.compile(r'^Standby +Configuration +register +is +(?P<var>\w+)'
                        r'(?: +\(will +be +(?P<var2>\S+) +at +next +reload\))?$')

        # CONFIG_FILE variable =
        p5 = re.compile(r'^CONFIG_FILE +variable += +(?P<var>\S+)$')

        # BOOTLDR variable =
        p6 = re.compile(r'^BOOTLDR +variable += +(?P<var>\S+)$')

        # BOOTLDR variable does not exist
        # not parsing

        # Standby not ready to show bootvar
        # not parsing
        # MANUAL_BOOT variable = no
        p7 = re.compile(r'(^MANUAL_BOOT\s*variable)\s*=\s*(?P<manual_boot>\w+)$')

        # Standby MANUAL_BOOT variable = no
        p8 = re.compile(r'(^Standby\s*MANUAL_BOOT\s*variable)\s*=\s*(?P<standby_manual_boot>\w+)$')

        for line in out.splitlines():
            line = line.strip()
            # BOOT variable = disk0:s72033-adventerprisek9-mz.122-33.SRE0a-ssr-nxos-76k-1,12;
            m = p1.match(line)
            if m:
                boot = m.groupdict()['var']
                if boot:
                    boot_dict['next_reload_boot_variable'] = boot
                    boot_dict.setdefault('active', {})['boot_variable'] = boot
                continue

            # Standby BOOT variable = bootflash:/asr1000rpx.bin,12;
            m = p2.match(line)
            if m:
                boot = m.groupdict()['var']
                if boot:
                    boot_dict.setdefault('standby', {})['boot_variable'] = boot
                continue

            # Configuration register is 0x2002
            m = p3.match(line)
            if m:
                boot_dict.setdefault('active', {})['configuration_register'] = m.groupdict()['var1']
                if m.groupdict()['var2']:
                    boot_dict.setdefault('active', {})['next_reload_configuration_register'] = m.groupdict()['var2']
                continue

            # Standby Configuration register is 0x2002
            m = p4.match(line)
            if m:
                boot_dict.setdefault('standby', {})['configuration_register'] = m.groupdict()['var']
                if m.groupdict()['var2']:
                    boot_dict.setdefault('standby', {})['next_reload_configuration_register'] = m.groupdict()['var2']
                continue

            # CONFIG_FILE variable =
            m = p5.match(line)
            if m:
                if m.groupdict()['var']:
                    boot_dict.update({'config_file': m.groupdict()['var']})
                continue

            # BOOTLDR variable =
            m = p6.match(line)
            if m:
                if m.groupdict()['var']:
                    boot_dict.setdefault('standby', {})['bootldr'] = m.groupdict()['var']
                continue

            # MANUAL_BOOT variable = no
            m = p7.match(line)
            if m:
                if m.groupdict()['manual_boot'].lower() == 'yes':
                    boot_dict.setdefault('active', {})['manual_boot'] = True
                else:
                    boot_dict.setdefault('active', {})['manual_boot'] = False
                continue

            # Standby MANUAL_BOOT variable = yes
            m = p8.match(line)
            if m:
                if m.groupdict()['standby_manual_boot'].lower() == 'yes':
                    boot_dict.setdefault(
                        'standby', {})['standby_manual_boot'] = True
                else:
                    boot_dict.setdefault(
                        'standby', {})['standby_manual_boot'] = False
                continue

        return boot_dict


class ShowVersionSchema(MetaParser):
    """Schema for show version"""
    schema = {
        'version': {
            Optional('xe_version'): str,
            'version_short': str,
            'platform': str,
            'version': str,
            Optional('label'): str,
            Optional('build_label'): str,
            'image_id': str,
            'rom': str,
            'image_type': str,
            Optional('installation_mode'): str,
            Optional('bootldr'): str,
            'hostname': str,
            'uptime': str,
            Optional('uptime_this_cp'): str,
            Optional('jawa_revision'): str,
            Optional('snowtrooper_revision'): str,
            Optional('running_default_software'): bool,
            Optional('processor_board_flash'): str,
            Optional('last_reload_type'): str,
            Optional('returned_to_rom_by'):  str,
            Optional('returned_to_rom_at'): str,
            Optional('compiled_date'): str,
            Optional('location'): str,
            Optional('copyright_years'): str,
            Optional('sp_by'): str,
            Optional('compiled_by'): str,
            Optional('system_restarted_at'): str,
            Optional('system_image'): str,
            Optional('last_reload_reason'): str,
            Optional('license_type'): str,
            Optional('license_level'): str,
            Optional('next_reload_license_level'): str,
            Optional('air_license_level'): str,
            Optional('next_reload_air_license_level'): str,
            Optional('chassis'): str,
            Optional('processor_type'): str,
            Optional('chassis_sn'): str,
            Optional('rtr_type'): str,
            Optional('router_operating_mode'): str,
            'os': str,
            Optional('curr_config_register'): str,
            Optional('license_udi'): {
                Optional('device_num'): {
                    Any(): {
                        'pid': str,
                        'sn': str,
                    }
                },
            },
            Optional('next_config_register'): str,
            Optional('main_mem'): str,
            Optional('number_of_intfs'): {
                Any(): str,
            },
            Optional('mem_size'): {
                Any(): str,
            },
            Optional('disks'): {
                Any(): {
                    Optional('disk_size'): str,
                    Optional('type_of_disk'): str,
                }
            },
            Optional('switch_num'): {
                Any(): {
                    Optional('uptime'): str,
                    Optional('mac_address'): str,
                    Optional('mb_assembly_num'): str,
                    Optional('power_supply_part_nr'): str,
                    Optional('mb_sn'): str,
                    Optional('power_supply_sn'): str,
                    Optional('model_rev_num'): str,
                    Optional('mb_rev_num'): str,
                    Optional('model_num'): str,
                    Optional('db_assembly_num'): str,
                    Optional('db_sn'): str,
                    Optional('system_sn'): str,
                    Optional('top_assembly_part_num'): str,
                    Optional('top_assembly_rev_num'): str,
                    Optional('system_fpga_version'): str,
                    Optional('version_id'): str,
                    Optional('clei_code_num'): str,
                    Optional('db_rev_num'): str,
                    Optional('hb_rev_num'): str,
                    Optional('mode'): str,
                    Optional('model'): str,
                    Optional('sw_image'): str,
                    Optional('ports'): str,
                    Optional('sw_ver'): str,
                    Optional('active'): bool,
                }
            },
            Optional('processor'): {
                Optional('cpu_type'): str,
                Optional('speed'): str,
                Optional('core'): str,
                Optional('l2_cache'): str,
                Optional('supervisor'): str,
            },
            Optional('license_package'): {
                Any(): {
                    'license_level': str,
                    'license_type': str,
                    'next_reload_license_level': str,
                },
            },
            Optional('module'): {
                Any(): {
                    Any(): {
                        Optional('suite'): str,
                        Optional('suite_current'): str,
                        Optional('type'): str,
                        Optional('suite_next_reboot'): str,
                    },
                },
            },
            Optional('image'): {
                'text_base': str,
                'data_base': str,
            },
            Optional('interfaces'): {
                Optional('virtual_ethernet'): int,
                Optional('fastethernet'): int,
                Optional('gigabit_ethernet'): int,
            },
            Optional('revision'): {
                Any(): int,
            }
        }
    }


class ShowVersion(ShowVersionSchema):
    """Parser for show version
    parser class - implements detail parsing mechanisms for cli output.
    """
    # *************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).

    cli_command = 'show version'
    exclude = ['system_restarted_at', 'uptime_this_cp', 'uptime']

    def cli(self, output=None):
        """parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: exe
        cuting, transforming, returning
        """
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        version_dict = {}
        active_dict = {}
        rtr_type = ''
        suite_flag = False
        license_flag = False

        # Cisco IOS XE Software, Version BLD_POLARIS_DEV_LATEST_20200702_122021_V17_4_0_67_2
        p0 = re.compile(
            r'^Cisco +([\S\s]+) +Software, +Version +(?P<xe_version>.*)$')

        # version
        # Cisco IOS Software [Everest], ISR Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 16.6.5, RELEASE SOFTWARE (fc3)
        # Cisco IOS Software, IOS-XE Software, Catalyst 4500 L3 Switch Software (cat4500e-UNIVERSALK9-M), Version 03.03.02.SG RELEASE SOFTWARE (fc1)
        p1 = re.compile(r'^[Cc]isco +IOS +[Ss]oftware\, +(?P<os>([\S]+)) +Software\, '
                        r'+(?P<platform>.+) Software +\((?P<image_id>.+)\).+[Vv]ersion '
                        r'+(?P<version>\S+) +.*$')

        # IOS (tm) Catalyst 4000 L3 Switch Software (cat4000-I9S-M), Version 12.2(18)EW5, RELEASE SOFTWARE (fc1)
        # IOS (tm) s72033_rp Software (s72033_rp-ADVENTERPRISEK9_WAN-M), Version 12.2(18)SXF7, RELEASE SOFTWARE (fc1)
        # IOS (tm) C2600 Software (C2600-I-M), Version 12.2(2)XA1, EARLY DEPLOYMENT RELEASE SOFTWARE (fc1)
        p1_1 = re.compile(r'^(?P<os>[A-Z]+) +\(.*\) +(?P<platform>.+) +Software'
                          r' +\((?P<image_id>.+)\).+( +Experimental)? +[Vv]ersion'
                          r' +(?P<version>\S+), +(EARLY DEPLOYMENT )?RELEASE SOFTWARE .*$')

        # 16.6.5
        p2 = re.compile(r'^(?P<ver_short>\d+\.\d+).*')

        # Cisco IOS Software [Fuji], ASR1000 Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 16.7.1prd4, RELEASE SOFTWARE (fc1)
        # Cisco IOS Software [Fuji], Catalyst L3 Switch Software (CAT3K_CAA-UNIVERSALK9-M), Experimental Version 16.8.20170924:182909 [polaris_dev-/nobackup/mcpre/BLD-BLD_POLARIS_DEV_LATEST_20170924_191550 132]
        # Cisco IOS Software, 901 Software (ASR901-UNIVERSALK9-M), Version 15.6(2)SP4, RELEASE SOFTWARE (fc3)
        # Cisco IOS Software [Amsterdam], Catalyst L3 Switch Software (CAT9K_IOSXE), Experimental Version 17.4.20200702:124009 [S2C-build-polaris_dev-116872-/nobackup/mcpre/BLD-BLD_POLARIS_DEV_LATEST_20200702_122021 243]
        # Cisco IOS Software [Denali], ASR1000 Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Experimental Version 16.3.20170410:103306 [v163_mr_throttle-BLD-BLD_V163_MR_THROTTLE_LATEST_20170410_093453 118]
        # Cisco IOS Software [IOSXE], Virtual XE Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Experimental Version 17.15.20240326:010319 [BLD_POLARIS_DEV_LATEST_20240326_003112:/nobackup/mcpre/s2c-build-ws 101]
        p3 = re.compile(r'^[Cc]isco +(?P<os>[A-Z]+) +[Ss]oftware\s*\[?(?P<location>\w*)?\]?\, '
                        r'+(?P<platform>.+) +Software +\((?P<image_id>.+)\).+( '
                        r'+Experimental)? +[Vv]ersion '
                        r'+(?P<version>[\w.:()]+) *,? *'
                        r'(?P<label>(\[.*?(?P<build_label>BLD_\w+)([-:]\S+)? \d+\])|.*)$')

        # Copyright (c) 1986-2016 by Cisco Systems, Inc.
        p4 = re.compile(r'^Copyright +\(c\) +(?P<copyright_years>\d+-\d+).*$')

        # Technical Support: http://www.cisco.com/techsupport
        p5 = re.compile(r'^Technical +Support: +http\:\/\/www'
                        r'\.cisco\.com\/techsupport')

        # rom
        # ROM: IOS-XE ROMMONBOOTLDR: System Bootstrap, Version 17.6.1r[FC2], DEVELOPMENT SOFTWARE
        p6 = re.compile(r'^ROM\: +(?P<rom>.+?)(?:BOOTLDR\: +(?P<bootldr>.+))?$')

        # ROM: Bootstrap program is IOSv
        p7 = re.compile(r'^Bootstrap +program +is +(?P<os>.+)$')

        # bootldr
        p8 = re.compile(r'^BOOTLDR\: +(?P<bootldr>.+)$')

        # hostname & uptime
        p9 = re.compile(r'^(?P<hostname>.+) +uptime +is +(?P<uptime>.+)$')

        # uptime_this_cp
        p10 = re.compile(r'^[Uu]ptime +for +this +control +processor '
                         r'+is +(?P<uptime_this_cp>.+)$')

        # system_restarted_at
        p11 = re.compile(r'^[Ss]ystem +restarted +at '
                         r'+(?P<system_restarted_at>.+)$')

        # system_image
        # System image file is "tftp://10.1.6.241//auto/genie-ftp/Edison/cat3k_caa-universalk9.BLD__20170410_174845.SSA.bin"
        # System image file is "harddisk:test-image-PE1-13113029"
        p12 = re.compile(r'^[Ss]ystem +image +file +is '
                         r'+\"(?P<system_image>.+)\"')

        # last_reload_reason
        p13 = re.compile(r'^[Ll]ast +reload +reason\: '
                         r'+(?P<last_reload_reason>.+)$')

        # last_reload_reason
        # Last reset from power-on
        p14 = re.compile(r'^[Ll]ast +reset +from +(?P<last_reload_reason>.+)$')

        # license_type
        p15 = re.compile(r'^[Ll]icense +[Tt]ype\: +(?P<license_type>.+)$')

        # license_level
        p16 = re.compile(r'^\s*[Ll]icense +[Ll]evel\: +(?P<license_level>.+)$')

        # entservices   Type: Permanent
        p16_1 = re.compile(r'(?P<license_level>\S+) +Type\: +(?P<license_type>.+)$')

        # AIR License Level: AIR DNA Advantage
        p16_2 = re.compile(r'^\s*AIR [Ll]icense +[Ll]evel\: +(?P<air_license_level>.+)$')

        ## Technology Package License Information:
        ## Technology-package                                     Technology-package
        # Current                        Type                       Next reboot
        p16_3 = re.compile(r'^Current  +Type  +Next reboot')

        # network-advantage     Smart License                    network-advantage
        # dna-advantage         Subscription Smart License       dna-advantage
        p16_4 = re.compile(r'^(?P<license_package>[\w-]+)(?:\s{2,})(?P<package_license_type>(\w+ )+)(?:\s{2,})(?P<next_reload_license_level>\S+)\s*$')

        # next_reload_license_level
        p17 = re.compile(r'^[Nn]ext +(reload|reboot) +license +Level\: '
                         r'+(?P<next_reload_license_level>.+)$')

        # Next reload AIR license Level: AIR DNA Advantage
        p17_1 = re.compile(r'^[Nn]ext +(reload|reboot) +AIR license +Level\: '
                           r'+(?P<next_reload_air_license_level>.+)$')

        # chassis, processor_type, main_mem and rtr_type
        # cisco WS-C3650-24PD (MIPS) processor (revision H0) with 829481K/6147K bytes of memory.
        # cisco CSR1000V (VXE) processor (revision VXE) with 1987991K/3075K bytes of memory.
        # cisco C1111-4P (1RU) processor with 1453955K/6147K bytes of memory.
        # Cisco IOSv (revision 1.0) with  with 435457K/87040K bytes of memory.
        # cisco WS-C3750X-24P (PowerPC405) processor (revision W0) with 262144K bytes of memory.
        # cisco ISR4451-X/K9 (2RU) processor with 1795979K/6147K bytes of memory.
        # cisco WS-C4507R+E (MPC8572) processor (revision 10) with 2097152K/20480K bytes of memory.
        # Cisco CISCO1941/K9 (revision 1.0) with 491520K/32768K bytes of memory.
        p18 = re.compile(r'^(C|c)isco +(?P<chassis>[a-zA-Z0-9\-\/\+]+) '
                         r'+\((?P<processor_type>[^)]*)\) +(.*?)with '
                         r'+(?P<main_mem>[0-9]+)[kK](\/[0-9]+[kK])?')

        # Cisco CISCO3945-CHASSIS (revision 1.0) with C3900-SPE150/K9 with 1835264K/261888K bytes of memory.
        p18_2 = re.compile(r'^(C|c)isco +(?P<chassis>[a-zA-Z0-9\-\/\+]+) +.* '
                           r'+with +(?P<processor_type>.+) +with +(?P<main_mem>[0-9]+)[kK](\/[0-9]+[kK])?')

        # Allen-Bradley 1783-CMS10DP (ARM) processor (revision V00) with 634958K/6147K bytes of memory.
        p18_3 = re.compile(r'^(A|a)llen-Bradley +(?P<chassis>[a-zA-Z0-9\-\/\+]+) '
                         r'+\((?P<processor_type>[^)]*)\) +(.*?)with '
                         r'+(?P<main_mem>[0-9]+)[kK](\/[0-9]+[kK])?')

        # chassis_sn
        p19 = re.compile(r'^[pP]rocessor +board +ID '
                         r'+(?P<chassis_sn>[a-zA-Z0-9]+)')

        # number_of_intfs
        p20 = re.compile(r'^(?P<number_of_ports>\d+) +(?P<interface>.+) '
                         r'+(interface(?:s)?|line|port(?:s)?)$')

        # mem_size
        p21 = re.compile(r'^(?P<mem_size>\d+)K +bytes +of '
                         r'+(?P<memories>.+) +[Mm]emory\.')

        # disks, disk_size and type_of_disk
        p22 = re.compile(r'^(?P<disk_size>\d+)K bytes of '
                         r'(?P<type_of_disk>.*) at (?P<disks>.+)$')

        # os
        # Cisco IOS Software,
        p23 = re.compile(r'^[Cc]isco +(?P<os>[a-zA-Z\-]+) '
                         r'+[Ss]oftware\,')

        # curr_config_register
        p24 = re.compile(r'^[Cc]onfiguration +register +is '
                         r'+(?P<curr_config_register>[a-zA-Z0-9]+)')

        # next_config_register
        p25 = re.compile(r'^[Cc]onfiguration +register +is +[a-zA-Z0-9]+ '
                         r'+\(will be (?P<next_config_register>[a-zA-Z0-9]+) '
                         r'at next reload\)')

        # switch_number
        p26 = re.compile(r'^[Ss]witch +0(?P<switch_number>\d+)$')

        # uptime
        p27 = re.compile(r'^[Ss]witch +[Uu]ptime +\: +(?P<uptime>.+)$')

        # mac_address
        p28 = re.compile(r'^[Bb]ase +[Ee]thernet +MAC +[Aa]ddress '
                         r'+\: +(?P<mac_address>.+)$')

        # mb_assembly_num
        p29 = re.compile(r'^[Mm]otherboard +[Aa]ssembly +[Nn]umber +\: '
                         r'+(?P<mb_assembly_num>.+)$')

        # mb_sn
        p30 = re.compile(r'^[Mm]otherboard +[Ss]erial +[Nn]umber +\: '
                         r'+(?P<mb_sn>.+)$')

        # model_rev_num
        p31 = re.compile(r'^[Mm]odel +[Rr]evision +[Nn]umber +\: '
                         r'+(?P<model_rev_num>.+)$')

        # mb_rev_num
        p32 = re.compile(r'^[Mm]otherboard +[Rr]evision +[Nn]umber +\: '
                         r'+(?P<mb_rev_num>.+)$')

        # model_num
        p33 = re.compile(r'^[Mm]odel +[Nn]umber +\: +(?P<model_num>.+)$')

        # system_sn
        p34 = re.compile(r'^[Ss]ystem +[Ss]erial +[Nn]umber +\: +(?P<system_sn>.+)$')

        # Compiled Mon 10-Apr-17 04:35 by mcpre
        # Compiled Mon 19-Mar-18 16:39 by prod_rel_team
        p36 = re.compile(r'^Compiled +(?P<compiled_date>[\S\s]+) +by '
                         r'+(?P<compiled_by>\w+)$')

        # System returned to ROM by reload at 15:57:52 CDT Mon Sep 24 2018
        # System returned to ROM by Reload Command at 07:15:43 UTC Fri Feb 1 2019
        # System returned to ROM by reload
        # System returned to ROM by power cycle at 23:31:24 PDT Thu Sep 27 2007 (SP by power on)
        # System returned to ROM by power-on
        p37 = re.compile(r'^System +returned +to +ROM +by '
                         r'+(?P<returned_to_rom_by>[\w\s\-]+)(?: +at '
                         r'+(?P<returned_to_rom_at>[\w\s\:]+))?(?: +\(SP +by '
                         r'+(?P<sp_by>[\S\s\-]+)\))?$')

        # Last reload type: Normal Reload
        p38 = re.compile(
            r'^Last +reload +type\: +(?P<last_reload_type>[\S ]+)$')

        # P2020 CPU at 800MHz, E500v2 core, 512KB L2 Cache
        p39 = re.compile(r'^(?P<cpu_name>\S+) +(CPU|cpu|Cpu) +at '
                         r'+(?P<speed>\S+)\,(( +(?P<core>\S+) +core\, '
                         r'+(?P<l2_cache>\S+) +L2 +[Cc]ache)|( +Supervisor '
                         r'+(?P<supervisor>\S+)))$')

        # 98304K bytes of processor board System flash (Read/Write)
        p40 = re.compile(r'^(?P<processor_board_flash>\S+) +bytes .+$')

        # Running default software
        p41 = re.compile(r'^Running +(?P<running_default_software>\S+) +software$')

        # Jawa Revision 7, Snowtrooper Revision 0x0.0x1C
        p42 = re.compile(r'^Jawa +Revision +(?P<jawa_revision>\S+)\, '
                         r'+Snowtrooper +Revision +(?P<snowtrooper_rev>\S+)$')

        # ipbase           ipbasek9         Smart License    ipbasek9
        # securityk9       securityk9       RightToUse       securityk9
        p43 = re.compile(r'^(?P<technology>\w[\w\-]+)(?: {2,}'
                         r'(?P<license_level>\w+) {2,}(?P<license_type>\w+(?: '
                         r'+\w+)?) {2,}(?P<next_boot>\w+))?$')

        # Suite                 Suite Current         Type           Suite Next reboot
        # Technology    Technology-package           Technology-package
        p44 = re.compile(r'^(?P<aname>Suite|Technology) +((Suite +Current)|'
                         r'(Technology\-package))')

        # Suite License Information for Module:'esg'
        p45 = re.compile(r'^[Ss]uite +[Ll]icense +[Ii]nformation +for '
                         r'+[Mm]odule\:\'(?P<module>\S+)\'$')

        # License UDI:
        p46_0 = re.compile(r'^License UDI:$')

        #     *0        C3900-SPE150/K9       FOC16050QP6
        p46 = re.compile(r'^(?P<device_num>[*\d]+) +(?P<pid>[\S]+) +(?P<sn>[A-Z\d]+)$')

        # Image text-base: 0x40101040, data-base: 0x42D98000
        p47 = re.compile(r'^Image text-base: +(?P<text_base>\S+), '
                         r'data-base: +(?P<data_base>\S+)$')

        # 1 Virtual Ethernet/IEEE 802.3 interface(s)
        # 50 Gigabit Ethernet/IEEE 802.3 interface(s)
        p48 = re.compile(r'^(?P<interface>\d+) +(?P<ethernet_type>Virtual Ethernet|Gigabit Ethernet|FastEthernet)'
                         r'/IEEE 802\.3 +interface\(s\)$')

        # Dagobah Revision 95, Swamp Revision 6
        p50 = re.compile(r'^(?P<group1>\S+)\s+Revision\s+(?P<group1_int>\d+),'
                         r'\s+(?P<group2>\S+)\s+Revision\s+(?P<group2_int>\d+)$')

        # power_supply_part_nr
        # Power supply part number: 444-8888-00
        p51 = re.compile(r'^[Pp]ower\s+[Ss]upply\s+[Pp]art\s+[Nn]umber\s+\:\s+(?P<power_supply_part_nr>.+)$')

        # power_supply_sn
        # Power supply serial number: CCC4466B6LL
        p52 = re.compile(r'^[Pp]ower\s+[Ss]upply\s+[Ss]erial\s+[Nn]umber\s+\:\s+(?P<power_supply_sn>.+)$')

        # Daughterboard assembly number   : 73-11111-00
        # db_assembly_num
        p53 = re.compile(r'^[Dd]aughterboard\s+[Aa]ssembly\s+[Nn]umber\s+\:\s+(?P<db_assembly_num>.+)$')

        # Daughterboard serial number     : FOC87654CWW
        # db_sn
        p54 = re.compile(r'^[Dd]aughterboard\s+[Ss]erial\s+[Nn]umber\s+\:\s+(?P<db_sn>.+)$')

        # top_assembly_part_num
        # Top Assembly Part Number        : 800-55555-11
        p55 = re.compile(r'^[Tt]op\s+[Aa]ssembly\s+[Pp]art\s+[Nn]umber\s+\:\s+(?P<top_assembly_part_num>.+)$')

        # top_assembly_rev_num
        # Top Assembly Revision Number    : C0
        p56 = re.compile(r'^[Tt]op\s+[Aa]ssembly\s+[Rr]evision\s+[Nn]umber\s+\:\s+(?P<top_assembly_rev_num>.+)$')

        # version_id
        # Version ID                      : V02
        p57 = re.compile(r'^[Vv]ersion\s+ID\s+\:\s+(?P<version_id>.+)$')

        # clei_code_num
        # CLEI Code Number                : AAALJ00ERT
        p58 = re.compile(r'^CLEI\s+[Cc]ode\s+[Nn]umber\s+\:\s+(?P<clei_code_num>.+)$')

        # Daughterboard revision number   : A0
        # db_rev_num
        p59 = re.compile(r'^[Dd]aughterboard\s+[Rr]evision\s+[Nn]umber\s+\:\s+(?P<db_rev_num>.+)$')

        # Hardware Board Revision Number  : 0x12
        # hb_rev_num
        p60 = re.compile(r'^[Hh]ardware\s+[Bb]oard\s+[Rr]evision\s+[Nn]umber\s+\:\s+(?P<hb_rev_num>.+)$')

        # Router operating mode: Controller-Managed
        p61 = re.compile(r'^Router operating mode: (?P<router_operating_mode>.+)$')

        # Installation mode is BUNDLE
        p62 = re.compile(r'^Installation\s+mode\s+is\s+(?P<installation_mode>.+)$')

        #System FPGA version                : 0.2.11
        p63 = re.compile('^System FPGA version\s+:\s+(?P<system_fpga_version>(\d+\.?)+)')

        for line in out.splitlines():
            line = line.strip()

            # Cisco IOS XE Software, Version BLD_POLARIS_DEV_LATEST_20200702_122021_V17_4_0_67_2
            m = p0.match(line)
            if m:
                if 'version' not in version_dict:
                    version_dict['version'] = {}
                xe_version = m.groupdict()['xe_version']
                version_dict['version']['xe_version'] = xe_version
                continue

            # version
            # Cisco IOS Software [Everest], ISR Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 16.6.5, RELEASE SOFTWARE (fc3)
            # Cisco IOS Software, IOS-XE Software, Catalyst 4500 L3 Switch Software (cat4500e-UNIVERSALK9-M), Version 03.03.02.SG RELEASE SOFTWARE (fc1)
            # IOS (tm) Catalyst 4000 L3 Switch Software (cat4000-I9S-M), Version 12.2(18)EW5, RELEASE SOFTWARE (fc1)
            # IOS (tm) s72033_rp Software (s72033_rp-ADVENTERPRISEK9_WAN-M), Version 12.2(18)SXF7, RELEASE SOFTWARE (fc1)
            # IOS (tm) C2600 Software (C2600-I-M), Version 12.2(2)XA1, EARLY DEPLOYMENT RELEASE SOFTWARE (fc1)
            m = p1.match(line) or p1_1.match(line)
            if m:
                version = m.groupdict()['version']
                # 16.6.5
                m2 = p2.match(version)
                if m2:
                    if 'version' not in version_dict:
                        version_dict['version'] = {}
                    version_dict['version']['version_short'] = \
                        m2.groupdict()['ver_short']
                    version_dict['version']['platform'] = \
                        m.groupdict()['platform'].strip()
                    version_dict['version']['version'] = \
                        m.groupdict()['version']
                    version_dict['version']['image_id'] = \
                        m.groupdict()['image_id']
                    version_dict['version']['os'] = m.groupdict()['os']
                    continue

            # Cisco IOS Software [Fuji], ASR1000 Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 16.7.1prd4, RELEASE SOFTWARE (fc1)
            # Cisco IOS Software [Fuji], Catalyst L3 Switch Software (CAT3K_CAA-UNIVERSALK9-M), Experimental Version 16.8.20170924:182909 [polaris_dev-/nobackup/mcpre/BLD-BLD_POLARIS_DEV_LATEST_20170924_191550 132]
            # Cisco IOS Software, 901 Software (ASR901-UNIVERSALK9-M), Version 15.6(2)SP4, RELEASE SOFTWARE (fc3)
            # Cisco IOS Software [Amsterdam], Catalyst L3 Switch Software (CAT9K_IOSXE), Experimental Version 17.4.20200702:124009 [S2C-build-polaris_dev-116872-/nobackup/mcpre/BLD-BLD_POLARIS_DEV_LATEST_20200702_122021 243]
            # Cisco IOS Software [Denali], ASR1000 Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Experimental Version 16.3.20170410:103306 [v163_mr_throttle-BLD-BLD_V163_MR_THROTTLE_LATEST_20170410_093453 118]
            m = p3.match(line)
            if m:
                version = m.groupdict()['version']
                # 16.6.5

                m2 = p2.match(version)

                if m2:
                    if 'version' not in version_dict:
                        version_dict['version'] = {}
                    version_dict['version']['version_short'] = \
                        m2.groupdict()['ver_short']
                    version_dict['version']['platform'] = \
                        m.groupdict()['platform']
                    version_dict['version']['version'] = \
                        m.groupdict()['version']
                    version_dict['version']['image_id'] = \
                        m.groupdict()['image_id']
                    if m.groupdict()['label']:
                        version_dict['version']['label'] = \
                            m.groupdict()['label']
                    if m.groupdict()['build_label']:
                        version_dict['version']['build_label'] = \
                            m.groupdict()['build_label']
                    if m.groupdict()['os']:
                        version_dict['version']['os'] = m.groupdict()['os']
                    if m.groupdict()['location']:
                        version_dict['version']['location'] = m.groupdict()['location']
                    continue

            # Copyright (c) 1986-2016 by Cisco Systems, Inc.
            m = p4.match(line)
            if m:
                version_dict.setdefault('version', {}).setdefault('image_type', 'developer image')
                version_dict.setdefault('version', {}).setdefault('copyright_years', m.groupdict()['copyright_years'])
                continue

            # Technical Support: http://www.cisco.com/techsupport
            m = p5.match(line)
            if m:
                version_dict.setdefault('version', {}).setdefault('image_type', 'production image')
                continue

            # rom
            m = p6.match(line)
            if m:
                rom = m.groupdict()['rom']
                version_dict['version']['rom'] = rom
                bootldr = m.groupdict()['bootldr']
                if bootldr:
                    version_dict['version']['bootldr'] = bootldr

                # ROM: Bootstrap program is IOSv
                m = p7.match(rom)
                if m:
                    if 'os' not in version_dict['version']:
                        version_dict['version']['os'] = \
                            m.groupdict()['os']
                continue

            # bootldr
            m = p8.match(line)
            if m:
                version_dict['version']['bootldr'] = \
                    m.groupdict()['bootldr']
                continue

            # hostname & uptime
            m = p9.match(line)
            if m:
                version_dict['version']['hostname'] = \
                    m.groupdict()['hostname']
                version_dict['version']['uptime'] = \
                    m.groupdict()['uptime']
                continue

            # uptime_this_cp
            m = p10.match(line)
            if m:
                version_dict['version']['uptime_this_cp'] = \
                    m.groupdict()['uptime_this_cp']
                uptime_this_cp = m.groupdict()['uptime_this_cp']
                continue

            # system_restarted_at
            m = p11.match(line)
            if m:
                version_dict['version']['system_restarted_at'] = \
                    m.groupdict()['system_restarted_at']
                continue

            # system_image
            # System image file is "tftp://10.1.6.241//auto/tftp-ssr/Edison/cat3k_caa-universalk9.BLD_V164_THROTTLE_LATEST_20170410_174845.SSA.bin"
            # System image file is "harddisk:test-image-PE1-13113029"
            m = p12.match(line)
            if m:
                version_dict['version']['system_image'] = \
                    m.groupdict()['system_image']
                continue

            # last_reload_reason
            m = p13.match(line)
            if m:
                version_dict['version']['last_reload_reason'] = \
                    m.groupdict()['last_reload_reason']
                continue

            # last_reload_reason
            # Last reset from power-on
            m = p14.match(line)
            if m:
                version_dict['version']['last_reload_reason'] = \
                    m.groupdict()['last_reload_reason']
                continue

            # license_type
            m = p15.match(line)
            if m:
                version_dict['version']['license_type'] = \
                    m.groupdict()['license_type']
                continue

            # license_level
            # License Level: entservices   Type: Permanent
            # License Level: AdvancedMetroIPAccess
            m = p16.match(line)
            if m:
                group = m.groupdict()
                if 'Type:' in group['license_level']:
                    lic_type = group['license_level'].strip()
                    m_1 = p16_1.match(lic_type)
                    if m_1:
                        lic_group = m_1.groupdict()
                        version_dict['version']['license_type'] = lic_group['license_type']
                        version_dict['version']['license_level'] = lic_group['license_level']
                else:
                    version_dict['version']['license_level'] = group['license_level']
                continue

            # AIR License Level: AIR DNA Advantage
            m = p16_2.match(line)
            if m:
                version_dict['version']['air_license_level'] = m.groupdict()['air_license_level']
                continue

            # Current                        Type                       Next reboot
            m = p16_3.match(line)
            if m:
                version_dict['version'].setdefault('license_package', {})
                continue

            # network-advantage     Smart License                    network-advantage
            # dna-advantage         Subscription Smart License       dna-advantage
            m = p16_4.match(line)
            if m:
                group = m.groupdict()
                license_package = group['license_package']
                version_dict['version'].setdefault('license_package', {})
                version_dict['version']['license_package'][license_package] = {
                    'license_level': license_package,
                    'license_type': group['package_license_type'].strip(),
                    'next_reload_license_level': group['next_reload_license_level']
                }
                continue

            # next_reload_license_level
            # Next reboot license Level: entservices
            # Next reload license Level: advipservices
            m = p17.match(line)
            if m:
                version_dict['version']['next_reload_license_level'] = \
                    m.groupdict()['next_reload_license_level']
                continue

            # Next reload AIR license Level: AIR DNA Advantage
            m = p17_1.match(line)
            if m:
                version_dict['version']['next_reload_air_license_level'] = \
                    m.groupdict()['next_reload_air_license_level']

            # chassis, processor_type, main_mem and rtr_type
            # cisco WS-C3650-24PD (MIPS) processor (revision H0) with 829481K/6147K bytes of memory.
            # cisco CSR1000V (VXE) processor (revision VXE) with 1987991K/3075K bytes of memory.
            # cisco C1111-4P (1RU) processor with 1453955K/6147K bytes of memory.
            # Cisco IOSv (revision 1.0) with  with 435457K/87040K bytes of memory.
            # cisco WS-C3750X-24P (PowerPC405) processor (revision W0) with 262144K bytes of memory.
            # cisco ISR4451-X/K9 (2RU) processor with 1795979K/6147K bytes of memory.
            m = p18.match(line)

            # Cisco CISCO3945-CHASSIS (revision 1.0) with C3900-SPE150/K9 with 1835264K/261888K bytes of memory.
            m2 = p18_2.match(line)

            m3 = p18_3.match(line)

            if m or m2 or m3:
                if m:
                    group = m.groupdict()
                elif m2:
                    group = m2.groupdict()
                elif m3:
                    group = m3.groupdict()

                version_dict['version']['chassis'] = group['chassis']
                version_dict['version']['main_mem'] = group['main_mem']
                version_dict['version']['processor_type'] = group['processor_type']

                if 'C3850' in version_dict['version']['chassis'] or \
                   'C3650' in version_dict['version']['chassis']:
                    version_dict['version']['rtr_type'] = rtr_type = 'Edison'
                elif 'ASR1' in version_dict['version']['chassis']:
                    version_dict['version']['rtr_type'] = rtr_type = 'ASR1K'
                elif 'CSR1000V' in version_dict['version']['chassis']:
                    version_dict['version']['rtr_type'] = rtr_type = 'CSR1000V'
                elif 'C11' in version_dict['version']['chassis']:
                    version_dict['version']['rtr_type'] = rtr_type = 'ISR'
                else:
                    version_dict['version']['rtr_type'] = rtr_type = version_dict['version']['chassis']
                continue

            # Router operating mode: Controller-Managed
            m = p61.match(line)
            if m:
                version_dict['version']['router_operating_mode'] = m.groupdict()['router_operating_mode']
                continue

            # Installation mode is BUNDLE
            m = p62.match(line)
            if m:
                version_dict['version']['installation_mode'] = m.groupdict()['installation_mode']
                continue

            # chassis_sn
            m = p19.match(line)
            if m:
                version_dict['version']['chassis_sn'] \
                    = m.groupdict()['chassis_sn']
                continue

            # number_of_intfs
            # 1 External Alarm interface
            # 1 FastEthernet interface
            # 12 Gigabit Ethernet interfaces
            # 2 Ten Gigabit Ethernet interfaces
            # 1 terminal line
            # 8 Channelized T1 ports
            m = p20.match(line)
            if m:
                interface = m.groupdict()['interface']
                if 'number_of_intfs' not in version_dict['version']:
                    version_dict['version']['number_of_intfs'] = {}
                version_dict['version']['number_of_intfs'][interface] = \
                    m.groupdict()['number_of_ports']
                continue

            # mem_size
            m = p21.match(line)
            if m:
                memories = m.groupdict()['memories']
                if 'mem_size' not in version_dict['version']:
                    version_dict['version']['mem_size'] = {}
                version_dict['version']['mem_size'][memories] = \
                    m.groupdict()['mem_size']
                continue

            # disks, disk_size and type_of_disk
            m = p22.match(line)
            if m:
                disks = m.groupdict()['disks']
                if 'disks' not in version_dict['version']:
                    version_dict['version']['disks'] = {}
                if disks not in version_dict['version']['disks']:
                    version_dict['version']['disks'][disks] = {}
                version_dict['version']['disks'][disks]['disk_size'] = \
                    m.groupdict()['disk_size']
                version_dict['version']['disks'][disks]['type_of_disk'] = \
                    m.groupdict()['type_of_disk']
                continue

            # os
            m = p23.match(line)
            if m:
                version_dict['version']['os'] = m.groupdict()['os']

                continue

            # curr_config_register
            m = p24.match(line)
            if m:
                version_dict['version']['curr_config_register'] \
                    = m.groupdict()['curr_config_register']

            # next_config_register
            m = p25.match(line)
            if m:
                version_dict['version']['next_config_register'] \
                    = m.groupdict()['next_config_register']
                continue

            # switch_number
            m = p26.match(line)
            if m:
                switch_number = m.groupdict()['switch_number']

                if 'switch_num' not in version_dict['version']:
                    version_dict['version']['switch_num'] = {}
                if switch_number not in version_dict['version']['switch_num']:
                    version_dict['version']['switch_num'][switch_number] = {}

                continue

            # uptime
            m = p27.match(line)
            if m:
                if 'switch_num' not in version_dict['version']:
                    continue
                version_dict['version']['switch_num'][switch_number]['uptime'] = m.groupdict()['uptime']
                continue

            # mac_address
            m = p28.match(line)
            if m:
                if 'switch_num' not in version_dict['version']:
                    active_dict.setdefault('mac_address', m.groupdict()['mac_address'])
                    continue
                version_dict['version']['switch_num'][switch_number]['mac_address'] = m.groupdict()['mac_address']
                continue

            # mb_assembly_num
            m = p29.match(line)
            if m:
                if 'switch_num' not in version_dict['version']:
                    active_dict.setdefault('mb_assembly_num', m.groupdict()['mb_assembly_num'])
                    continue
                version_dict['version']['switch_num'][switch_number]['mb_assembly_num'] = m.groupdict()['mb_assembly_num']
                continue

            # mb_sn
            m = p30.match(line)
            if m:
                if 'switch_num' not in version_dict['version']:
                    active_dict.setdefault('mb_sn', m.groupdict()['mb_sn'])
                    continue
                version_dict['version']['switch_num'][switch_number]['mb_sn'] = m.groupdict()['mb_sn']
                continue

            # model_rev_num
            m = p31.match(line)
            if m:
                if 'switch_num' not in version_dict['version']:
                    active_dict.setdefault('model_rev_num', m.groupdict()['model_rev_num'])
                    continue
                version_dict['version']['switch_num'][switch_number]['model_rev_num'] = m.groupdict()['model_rev_num']
                continue

            # mb_rev_num
            m = p32.match(line)
            if m:
                if 'switch_num' not in version_dict['version']:
                    active_dict.setdefault('mb_rev_num', m.groupdict()['mb_rev_num'])
                    continue
                version_dict['version']['switch_num'][switch_number]['mb_rev_num'] = m.groupdict()['mb_rev_num']
                continue

            # model_num
            m = p33.match(line)
            if m:
                if 'switch_num' not in version_dict['version']:
                    active_dict.setdefault('model_num', m.groupdict()['model_num'])
                    continue
                version_dict['version']['switch_num'][switch_number]['model_num'] = m.groupdict()['model_num']
                continue

            # system_sn
            m = p34.match(line)
            if m:
                if 'switch_num' not in version_dict['version']:
                    active_dict.setdefault('system_sn', m.groupdict()['system_sn'])
                    continue
                version_dict['version']['switch_num'][switch_number]['system_sn'] = m.groupdict()['system_sn']
                continue

            # power_supply_part_nr
            m = p51.match(line)
            if m:
                if 'switch_num' not in version_dict['version']:
                    active_dict.setdefault('power_supply_part_nr', m.groupdict()['power_supply_part_nr'])
                    continue
                version_dict['version']['switch_num'][switch_number]['power_supply_part_nr'] = m.groupdict()['power_supply_part_nr']
                continue

            # power_supply_sn
            m = p52.match(line)
            if m:
                if 'switch_num' not in version_dict['version']:
                    active_dict.setdefault('power_supply_sn', m.groupdict()['power_supply_sn'])
                    continue
                version_dict['version']['switch_num'][switch_number]['power_supply_sn'] = m.groupdict()['power_supply_sn']
                continue

            # db_assembly_num
            m = p53.match(line)
            if m:
                if 'switch_num' not in version_dict['version']:
                    active_dict.setdefault('db_assembly_num', m.groupdict()['db_assembly_num'])
                    continue
                version_dict['version']['switch_num'][switch_number]['db_assembly_num'] = m.groupdict()['db_assembly_num']
                continue

            # db_sn
            m = p54.match(line)
            if m:
                if 'switch_num' not in version_dict['version']:
                    active_dict.setdefault('db_sn', m.groupdict()['db_sn'])
                    continue
                version_dict['version']['switch_num'][switch_number]['db_sn'] = m.groupdict()['db_sn']
                continue

            # top_assembly_part_num
            m = p55.match(line)
            if m:
                if 'switch_num' not in version_dict['version']:
                    active_dict.setdefault('top_assembly_part_num', m.groupdict()['top_assembly_part_num'])
                    continue
                version_dict['version']['switch_num'][switch_number]['top_assembly_part_num'] = m.groupdict()['top_assembly_part_num']
                continue

            # top_assembly_rev_num
            m = p56.match(line)
            if m:
                if 'switch_num' not in version_dict['version']:
                    active_dict.setdefault('top_assembly_rev_num', m.groupdict()['top_assembly_rev_num'])
                    continue
                version_dict['version']['switch_num'][switch_number]['top_assembly_rev_num'] = m.groupdict()['top_assembly_rev_num']
                continue

            # version_id
            m = p57.match(line)
            if m:
                if 'switch_num' not in version_dict['version']:
                    active_dict.setdefault('version_id', m.groupdict()['version_id'])
                    continue
                version_dict['version']['switch_num'][switch_number]['version_id'] = m.groupdict()['version_id']
                continue

            # clei_code_num
            m = p58.match(line)
            if m:
                if 'switch_num' not in version_dict['version']:
                    active_dict.setdefault('clei_code_num', m.groupdict()['clei_code_num'])
                    continue
                version_dict['version']['switch_num'][switch_number]['clei_code_num'] = m.groupdict()['clei_code_num']
                continue

            # db_rev_num
            m = p59.match(line)
            if m:
                if 'switch_num' not in version_dict['version']:
                    active_dict.setdefault('db_rev_num', m.groupdict()['db_rev_num'])
                    continue
                version_dict['version']['switch_num'][switch_number]['db_rev_num'] = m.groupdict()['db_rev_num']
                continue

            # hb_rev_num
            m = p60.match(line)
            if m:
                if 'switch_num' not in version_dict['version']:
                    active_dict.setdefault('hb_rev_num', m.groupdict()['hb_rev_num'])
                    continue
                version_dict['version']['switch_num'][switch_number]['hb_rev_num'] = m.groupdict()['hb_rev_num']
                continue

            # Compiled Mon 10-Apr-17 04:35 by mcpre
            # Compiled Mon 19-Mar-18 16:39 by prod_rel_team
            m36 = p36.match(line)
            if m36:
                group = m36.groupdict()
                version_dict['version']['compiled_date'] = group['compiled_date']
                version_dict['version']['compiled_by'] = group['compiled_by']

                continue

            # System returned to ROM by reload at 15:57:52 CDT Mon Sep 24 2018
            # System returned to ROM by Reload Command at 07:15:43 UTC Fri Feb 1 2019
            # System returned to ROM by reload
            # System returned to ROM by power cycle at 23:31:24 PDT Thu Sep 27 2007 (SP by power on)
            # System returned to ROM by power-on
            m37 = p37.match(line)
            if m37:
                group = m37.groupdict()

                if group['returned_to_rom_at']:
                    version_dict['version']['returned_to_rom_by'] = group['returned_to_rom_by']
                    version_dict['version']['returned_to_rom_at'] = group['returned_to_rom_at']
                else:
                    version_dict['version']['returned_to_rom_by'] = group['returned_to_rom_by']

                if group['sp_by']:
                    version_dict['version']['sp_by'] = group['sp_by']

                continue

            # Last reload type: Normal Reload
            m38 = p38.match(line)
            if m38:
                version_dict['version']['last_reload_type'] = m38.groupdict()['last_reload_type']

                continue

            # P2020 CPU at 800MHz, E500v2 core, 512KB L2 Cache
            # MPC8572 CPU at 1.5GHz, Supervisor 7
            m39 = p39.match(line)
            if m39:
                group = m39.groupdict()
                cpu_dict = version_dict['version'].setdefault('processor', {})
                if group['supervisor']:
                    cpu_dict['cpu_type'] = group['cpu_name']
                    cpu_dict['speed'] = group['speed']
                    cpu_dict['supervisor'] = group['supervisor']
                else:
                    cpu_dict['cpu_type'] = group['cpu_name']
                    cpu_dict['speed'] = group['speed']
                    cpu_dict['core'] = group['core']
                    cpu_dict['l2_cache'] = group['l2_cache']

                continue

            # 98304K bytes of processor board System flash (Read/Write)
            m40 = p40.match(line)
            if m40:
                flash_dict = version_dict['version']
                in_kb = m40.groupdict()['processor_board_flash']
                flash_dict['processor_board_flash'] = in_kb

                continue

            # Running default software
            m41 = p41.match(line)
            if m41:
                version_dict['version']['running_default_software'] = True

                continue

            # Jawa Revision 7, Snowtrooper Revision 0x0.0x1C
            m42 = p42.match(line)
            if m42:
                version_dict['version']['jawa_revision'] = m42.groupdict()['jawa_revision']
                version_dict['version']['snowtrooper_revision'] = m42.groupdict()['snowtrooper_rev']

                continue

            # ipbase           ipbasek9         Smart License    ipbasek9
            # securityk9       securityk9       RightToUse       securityk9
            m43 = p43.match(line)
            if m43:
                group = m43.groupdict()

                if license_flag:
                    lic_initial_dict = version_dict['version'].setdefault('license_package', {})
                    license_dict = lic_initial_dict.setdefault(group['technology'], {})

                    if group['license_type']:
                        license_dict.update({'license_type': group['license_type']})

                    if group['license_level']:
                        license_dict.update({'license_level': group['license_level']})

                    if group['next_boot']:
                        license_dict.update({'next_reload_license_level': group['next_boot']})

                if suite_flag:
                    suite_lic_dict = suite_dict.setdefault(group['technology'], {})

                    if group['license_level']:
                        suite_lic_dict.update({'suite_current': group['license_level']})

                    if group['license_type']:
                        suite_lic_dict.update({'type': group['license_type'].strip()})

                    if group['next_boot']:
                        suite_lic_dict.update({'suite_next_reboot': group['next_boot']})

                continue

            # Suite                 Suite Current         Type           Suite Next reboot
            # Technology    Technology-package           Technology-package
            m44 = p44.match(line)
            if m44:
                if 'Suite' in m44.groupdict()['aname']:
                    suite_flag = True

                if 'Technology' in m44.groupdict()['aname']:
                    license_flag = True
                    suite_flag = False

                continue

            # Suite License Information for Module:'esg'
            m45 = p45.match(line)
            if m45:
                module_dict = version_dict['version'].setdefault('module', {})
                suite_dict = module_dict.setdefault(m45.groupdict()['module'], {})

                continue

            # License UDI:
            m46_0 = p46_0.match(line)
            if m46_0:
                if 'license_udi' not in version_dict:
                    license_udi_dict = version_dict['version'].setdefault('license_udi', {})
                continue

            # *0        C3900-SPE150/K9       FOC16050QP6
            m46 = p46.match(line)
            if m46:
                group = m46.groupdict()
                license_udi_sub = license_udi_dict.setdefault('device_num', {}).\
                    setdefault(group['device_num'], {})
                license_udi_sub['pid'] = group['pid']
                license_udi_sub['sn'] = group['sn']
                continue

            # Image text-base: 0x40101040, data-base: 0x42D98000
            m = p47.match(line)
            if m:
                version_dict['version']['image'] = {}
                version_dict['version']['image']['text_base'] = m.groupdict()['text_base']
                version_dict['version']['image']['data_base'] = m.groupdict()['data_base']
                continue

            # 1 Virtual Ethernet/IEEE 802.3 interface(s)
            # 50 Gigabit Ethernet/IEEE 802.3 interface(s)
            m = p48.match(line)
            if m:
                group = m.groupdict()
                ethernet_type = '_'.join(group['ethernet_type'].lower().split())

                if 'interfaces' not in version_dict['version']:
                    version_dict['version']['interfaces'] = {}
                version_dict['version']['interfaces'][ethernet_type] = \
                    int(group['interface'])
                continue

            # Dagobah Revision 95, Swamp Revision 6
            m = p50.match(line)
            if m:
                groupdict = m.groupdict()
                version_dict['version']['revision'] = {}
                version_dict['version']['revision'][groupdict['group1']] = int(groupdict['group1_int'])
                version_dict['version']['revision'][groupdict['group2']] = int(groupdict['group2_int'])
                continue

            m = p63.match(line)
            if m:
                if 'switch_num' not in version_dict['version']:
                    active_dict.setdefault('system_fpga_version', m.groupdict()['system_fpga_version'])
                    continue
                version_dict['version']['switch_num'][switch_number]['system_fpga_version'] = m.groupdict()['system_fpga_version']
                continue

        # table2 for C3850
        tmp2 = genie.parsergen.oper_fill_tabular(right_justified=True,
                                                 header_fields=["Switch",
                                                                "Ports",
                                                                "Model             ",
                                                                'SW Version       ',
                                                                "SW Image              ",
                                                                "Mode   "],
                                                 label_fields=["switch_num",
                                                               "ports",
                                                               "model",
                                                               "sw_ver",
                                                               'sw_image',
                                                               'mode'],
                                                 index=[0, ],
                                                 table_terminal_pattern=r"(^\n|^\s*$)",
                                                 device_output=out,
                                                 device_os='iosxe')

        if not tmp2.entries:
            # table2 for IOS
            tmp2 = genie.parsergen.oper_fill_tabular(right_justified=True,
                                                     header_fields=["Switch",
                                                                    "Ports",
                                                                    "Model             ",
                                                                    'SW Version       ',
                                                                    "SW Image              "],
                                                     label_fields=["switch_num",
                                                                   "ports",
                                                                   "model",
                                                                   "sw_ver",
                                                                   'sw_image'],
                                                     index=[0, ],
                                                     table_terminal_pattern=r"(^\n|^\s*$)",
                                                     device_output=out,
                                                     device_os='ios')

        if tmp2.entries:
            res2 = tmp2
            for key in res2.entries.keys():
                if 'switch_num' not in version_dict['version']:
                    version_dict['version']['switch_num'] = {}
                if '*' in key:
                    p = re.compile(r'\**\ *(?P<new_key>\d)')
                    m = p.match(key)
                    switch_no = m.groupdict()['new_key']
                    if m:
                        if switch_no not in version_dict['version']['switch_num']:
                            version_dict['version']['switch_num'][switch_no] = {}
                        for k, v in res2.entries[key].items():
                            if 'switch_num' != k:
                                version_dict['version']['switch_num'][switch_no][k] = v

                        if 'uptime_this_cp' in locals():
                            version_dict['version']['switch_num'][switch_no]['uptime'] = uptime_this_cp

                        version_dict['version']['switch_num'][switch_no]['active'] = True
                        version_dict['version']['switch_num'][switch_no].\
                            update(active_dict) if active_dict else None
                else:
                    for k, v in res2.entries[key].items():
                        if key not in version_dict['version']['switch_num']:
                            version_dict['version']['switch_num'][key] = {}
                        if 'switch_num' != k:
                            version_dict['version']['switch_num'][key][k] = v
                    version_dict['version']['switch_num'][key]['active'] = False

        elif active_dict:
            # Insert active switch into first free switch number
            used_switch_nums = version_dict.get('version', {}).get('switch_num', {}).keys()
            used_switch_nums = [int(x) for x in used_switch_nums]

            for num in range(1, len(used_switch_nums) + 2):
                if num not in used_switch_nums:
                    active_switch = version_dict.setdefault('version', {}).\
                        setdefault('switch_num', {}).setdefault(str(num), {})
                    active_switch.update(active_dict)
                    break

        # Backward compatibility for license_level and license_type
        if len(version_dict['version'].get('license_package', '')) == 1:
            k = list(version_dict['version']['license_package'].keys())[0]
            lic_info = version_dict['version']['license_package'][k]
            version_dict['version'].setdefault('license_level', lic_info.get('license_level'))
            version_dict['version'].setdefault('license_type', lic_info.get('license_type'))
            version_dict['version'].setdefault('next_reload_license_level', lic_info.get('next_reload_license_level'))

        return version_dict


class DirSchema(MetaParser):
    """Schema for dir"""
    schema = {
        'dir': {
            'dir': str,
            Any(): {
                Optional('files'): {
                    Any(): {
                        Optional('index'): str,
                        Optional('permissions'): str,
                        'size': str,
                        Optional('last_modified_date'): str
                    }
                },
                Optional('bytes_total'): str,
                Optional('bytes_free'): str
            }
        }
    }


class Dir(DirSchema):
    """Parser for dir
    parser class - implements detail parsing mechanisms for cli output.
    """
    # *************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).
    cli_command = ['dir', 'dir {directory}']
    exclude = ['last_modified_date', 'bytes_free', 'files']

    def cli(self, directory='', output=None):
        """parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: exe
        cuting, transforming, returning
        """
        if output is None:
            if directory:
                out = self.device.execute(
                    self.cli_command[1].format(directory=directory))
            else:
                out = self.device.execute(self.cli_command[0])
        else:
            out = output

        dir_dict = {}
        for line in out.splitlines():
            line = line.rstrip()

            # dir
            p1 = re.compile(
                r'^\s*[Dd]irectory +of +(?P<dir>.+)$')
            m = p1.match(line)
            if m:
                dir1 = m.groupdict()['dir']
                if 'dir' not in dir_dict:
                    dir_dict['dir'] = {}
                if dir1 not in dir_dict['dir']:
                    dir_dict['dir'][dir1] = {}
                    dir_dict['dir']['dir'] = dir1
                continue

            # filename, index, permissions, size and last_modified_date
            p2 = re.compile(
                r'\s*(?P<index>\d+) +(?P<permissions>\S+) +(?P<size>\d+) +(?P<last_modified_date>\S+ +\d+ +\d+ +\d+\:\d+\:\d+ +\S+) +(?P<filename>.+)$')
            m = p2.match(line)
            if m:
                filename = m.groupdict()['filename']
                if 'files' not in dir_dict['dir'][dir1]:
                    dir_dict['dir'][dir1]['files'] = {}
                if filename not in dir_dict['dir'][dir1]['files']:
                    dir_dict['dir'][dir1]['files'][filename] = {}
                dir_dict['dir'][dir1]['files'][filename]['index'] = m.groupdict()['index']
                dir_dict['dir'][dir1]['files'][filename]['permissions'] = m.groupdict()['permissions']
                dir_dict['dir'][dir1]['files'][filename]['size'] = m.groupdict()['size']
                dir_dict['dir'][dir1]['files'][filename]['last_modified_date'] = m.groupdict()['last_modified_date']
                continue

            # bytes_total and bytes_free
            p3 = re.compile(r'\s*(?P<bytes_total>\d+) +bytes +total +\((?P<bytes_free>\d+) +bytes +free\)')
            m = p3.match(line)
            if m:
                dir_dict['dir'][dir1]['bytes_total'] = m.groupdict()['bytes_total']
                dir_dict['dir'][dir1]['bytes_free'] = m.groupdict()['bytes_free']
                continue

        return dir_dict


class ShowRedundancySchema(MetaParser):
    """Schema for show redundancy """
    schema = {
        'red_sys_info': {
            'available_system_uptime': str,
            'switchovers_system_experienced': str,
            'standby_failures': str,
            'last_switchover_reason': str,
            'hw_mode': str,
            'conf_red_mode': str,
            'oper_red_mode': str,
            'maint_mode': str,
            'communications': str,
            Optional('communications_reason'): str,
        },
        'slot': {
            Any(): {
                'curr_sw_state': str,
                'uptime_in_curr_state': str,
                'image_ver': str,
                Optional('boot'): str,
                Optional('config_file'): str,
                Optional('bootldr'): str,
                Optional('config_register'): str,
            }
        }
    }


class ShowRedundancy(ShowRedundancySchema):
    """Parser for show redundancy
    parser class - implements detail parsing mechanisms for cli output.
    """
    # *************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).

    cli_command = 'show redundancy'
    exclude = ['available_system_uptime', 'uptime_in_curr_state']

    def cli(self, output=None):
        """parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: exe
        cuting, transforming, returning
        """
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        redundancy_dict = {}
        for line in out.splitlines():
            line = line.rstrip()

            # available_system_uptime
            p1 = re.compile(r'\s*[Aa]vailable +[Ss]ystem +[Uu]ptime +\= +(?P<available_system_uptime>.+)$')
            m = p1.match(line)
            if m:
                redundancy_dict.setdefault('red_sys_info', {})
                redundancy_dict['red_sys_info']['available_system_uptime'] = \
                    m.groupdict()['available_system_uptime']
                continue

            # switchovers_system_experienced
            p2 = re.compile(r'\s*[Ss]witchovers +system +experienced +\= +(?P<switchovers_system_experienced>\d+)$')
            m = p2.match(line)
            if m:
                redundancy_dict['red_sys_info']['switchovers_system_experienced'] = \
                    m.groupdict()['switchovers_system_experienced']
                continue

            # standby_failures
            p3 = re.compile(r'\s*[Ss]tandby +failures +\= +(?P<standby_failures>\d+)$')
            m = p3.match(line)
            if m:
                redundancy_dict['red_sys_info']['standby_failures'] = \
                    m.groupdict()['standby_failures']
                continue

            # last_switchover_reason
            p4 = re.compile(r'^\s*[Ll]ast +[Ss]witchover +[Rr]eason +\= +(?P<last_switchover_reason>.+)$')
            m = p4.match(line)
            if m:
                redundancy_dict['red_sys_info']['last_switchover_reason'] = \
                    m.groupdict()['last_switchover_reason']
                continue

            # hw_mode
            p5 = re.compile(r'\s*[Hh]ardware +[Mm]ode +\= +(?P<hw_mode>\S+)$')
            m = p5.match(line)
            if m:
                redundancy_dict['red_sys_info']['hw_mode'] = \
                    m.groupdict()['hw_mode']
                continue

            # conf_red_mode
            p6 = re.compile(r'\s*[Cc]onfigured +[Rr]edundancy +[Mm]ode +\= +(?P<conf_red_mode>[\s\S]+)$')
            m = p6.match(line)
            if m:
                redundancy_dict['red_sys_info']['conf_red_mode'] = \
                    m.groupdict()['conf_red_mode']
                continue

            # oper_red_mode
            p7 = re.compile(r'\s*[Oo]perating +[Rr]edundancy +[Mm]ode +\= +(?P<oper_red_mode>.+)$')
            m = p7.match(line)
            if m:
                redundancy_dict['red_sys_info']['oper_red_mode'] = \
                    m.groupdict()['oper_red_mode']
                continue

            # maint_mode
            p7 = re.compile(r'\s*[Mm]aintenance +[Mm]ode +\= +(?P<maint_mode>\S+)$')
            m = p7.match(line)
            if m:
                redundancy_dict['red_sys_info']['maint_mode'] = \
                    m.groupdict()['maint_mode']
                continue

            # communications
            p8 = re.compile(r'^\s*[Cc]ommunications +\= +(?P<communications>\S+)$')
            m = p8.match(line)
            if m:
                redundancy_dict['red_sys_info']['communications'] = \
                    m.groupdict()['communications']

            # communications_reason
            p8 = re.compile(r'^\s*[Cc]ommunications +\= +(?P<communications>\S+)\s+[Rr]eason\: +(?P<communications_reason>.+)$')
            m = p8.match(line)
            if m:
                redundancy_dict['red_sys_info']['communications'] = \
                    m.groupdict()['communications']
                redundancy_dict['red_sys_info']['communications_reason'] = \
                    m.groupdict()['communications_reason']
                continue

            # slot number
            p9 = re.compile(r'^\s*\S+ +[Ll]ocation +\= +(?P<slot>.+)$')
            m = p9.match(line)
            if m:
                slot = m.groupdict()['slot']
                if 'slot' not in redundancy_dict:
                    redundancy_dict['slot'] = {}
                if slot not in redundancy_dict['slot']:
                    redundancy_dict['slot'][slot] = {}
                continue

            # curr_sw_state
            p10 = re.compile(r'^\s*[Cc]urrent +[Ss]oftware +[Ss]tate +\= +(?P<curr_sw_state>.+)$')
            m = p10.match(line)
            if m:
                if 'slot' in redundancy_dict:
                    redundancy_dict['slot'][slot]['curr_sw_state'] = \
                        m.groupdict()['curr_sw_state']
                continue

            # uptime_in_curr_state
            p11 = re.compile(r'^\s*[Uu]ptime +[Ii]n +[Cc]urrent +[Ss]tate +\= +(?P<uptime_in_curr_state>.+)$')
            m = p11.match(line)
            if m:
                if 'slot' in redundancy_dict:
                    redundancy_dict['slot'][slot]['uptime_in_curr_state'] = \
                        m.groupdict()['uptime_in_curr_state']
                continue

            # image_ver
            p12 = re.compile(r'^\s*[Ii]mage +[Vv]ersion +\= +(?P<image_ver>.+)$')
            m = p12.match(line)
            if m:
                if 'slot' in redundancy_dict:
                    redundancy_dict['slot'][slot]['image_ver'] = \
                        m.groupdict()['image_ver']
                continue

            # boot
            p13 = re.compile(r'^\s*BOOT +\= +(?P<boot>.+)$')
            m = p13.match(line)
            if m:
                if 'slot' in redundancy_dict:
                    redundancy_dict['slot'][slot]['boot'] = \
                        m.groupdict()['boot']
                continue

            # config_file
            p14 = re.compile(r'\s*CONFIG_FILE +\= +(?P<config_file>.?)$')
            m = p14.match(line)
            if m:
                if 'slot' in redundancy_dict:
                    redundancy_dict['slot'][slot]['config_file'] = \
                        m.groupdict()['config_file']
                continue

            # bootldr
            p15 = re.compile(r'\s*BOOTLDR +\= +(?P<bootldr>.?)$')
            m = p15.match(line)
            if m:
                if 'slot' in redundancy_dict:
                    redundancy_dict['slot'][slot]['bootldr'] = \
                        m.groupdict()['bootldr']
                continue

            # config_register
            p16 = re.compile(r'^\s*[Cc]onfiguration +[Rr]egister = (?P<config_register>.+)$')
            m = p16.match(line)
            if m:
                if 'slot' in redundancy_dict:
                    redundancy_dict['slot'][slot]['config_register'] = \
                        m.groupdict()['config_register']
                continue

        return redundancy_dict


class ShowRedundancyStatesSchema(MetaParser):
    """Schema for show redundancy states """
    schema = {
        'my_state': str,
        'peer_state': str,
        'mode': str,
        Optional('unit'): str,
        'unit_id': int,
        'redundancy_mode_operational': str,
        'redundancy_mode_configured': str,
        'redundancy_state': str,
        Optional('maintenance_mode'): str,
        'manual_swact': str,
        Optional('manual_swact_reason'): str,
        'communications': str,
        Optional('communications_reason'): str,
        'client_count': int,
        'client_notification_tmr_msec': int,
        'rf_debug_mask': str,
    }


class ShowRedundancyStates(ShowRedundancyStatesSchema):
    """ Parser for show redundancy states """

    cli_command = 'show redundancy states'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial variables
        ret_dict = {}

        # my state = 13 -ACTIVE
        p1 = re.compile(r'^my +state += +(?P<my_state>[\s\S]+)$')

        # peer state = 8  -STANDBY HOT
        p2 = re.compile(r'^peer +state += +(?P<peer_state>[\s\S]+)$')

        # Mode = Duplex
        p3 = re.compile(r'^Mode += +(?P<mode>[\w]+)$')

        # Unit = Primary
        p4 = re.compile(r'^Unit += +(?P<unit>[\w]+)$')

        # Unit ID = 48
        p5 = re.compile(r'^Unit +ID += +(?P<unit_id>[\d]+)$')

        # Redundancy Mode (Operational) = sso
        p6 = re.compile(r'^Redundancy +Mode +\(Operational\) += +'
                        '(?P<redundancy_mode_operational>[\s\S]+)$')

        # Redundancy Mode (Configured)  = sso
        p7 = re.compile(r'^Redundancy +Mode +\(Configured\) += +'
                        '(?P<redundancy_mode_configured>[\s\S]+)$')

        # Redundancy State              = sso
        p8 = re.compile(r'^Redundancy +State += +(?P<redundancy_state>[\s\S]+)$')

        # Maintenance Mode = Disabled
        p9 = re.compile(r'^Maintenance +Mode += +(?P<maintenance_mode>[\w]+)$')

        # Manual Swact = enabled
        # Manual Swact = disabled (system is simplex (no peer unit))
        p10 = re.compile(r'^Manual +Swact += +(?P<manual_swact>[\w]+)'
                         '( +\((?P<manual_swact_reason>.*)\))?$')

        # Communications = Up
        # Communications = Down      Reason: Simplex mode
        p11 = re.compile(r'^Communications += +(?P<communications>[\w]+)'
                         '( +Reason: +(?P<communications_reason>[\s\S]+))?$')

        # client count = 76
        p12 = re.compile(r'^client +count += +(?P<client_count>[\d]+)$')

        # client_notification_TMR = 30000 milliseconds
        p13 = re.compile(r'^client_notification_TMR += +'
                         '(?P<client_notification_tmr_msec>[\d]+) +milliseconds$')

        # RF debug mask = 0x0
        p14 = re.compile(r'^RF +debug +mask += +(?P<rf_debug_mask>[\w]+)$')

        for line in out.splitlines():
            line = line.strip()
            if not line:
                continue

            # my state = 13 -ACTIVE
            m = p1.match(line)
            if m:
                ret_dict['my_state'] = m.groupdict()['my_state']
                continue

            # peer state = 1  -DISABLED
            m = p2.match(line)
            if m:
                ret_dict['peer_state'] = m.groupdict()['peer_state']
                continue

            # Mode = Simplex
            m = p3.match(line)
            if m:
                ret_dict['mode'] = m.groupdict()['mode']
                continue

            # Unit = Primary
            m = p4.match(line)
            if m:
                ret_dict['unit'] = m.groupdict()['unit']
                continue

            # Unit ID = 48
            m = p5.match(line)
            if m:
                ret_dict['unit_id'] = int(m.groupdict()['unit_id'])
                continue

            # Redundancy Mode (Operational) = Non-redundant
            m = p6.match(line)
            if m:
                ret_dict['redundancy_mode_operational'] = \
                    m.groupdict()['redundancy_mode_operational']
                continue

            # Redundancy Mode (Configured)  = Non-redundant
            m = p7.match(line)
            if m:
                ret_dict['redundancy_mode_configured'] = \
                    m.groupdict()['redundancy_mode_configured']
                continue

            # Redundancy State              = sso
            m = p8.match(line)
            if m:
                ret_dict['redundancy_state'] = m.groupdict()[
                    'redundancy_state']
                continue

            # Maintenance Mode = Disabled
            m = p9.match(line)
            if m:
                ret_dict['maintenance_mode'] = m.groupdict()[
                    'maintenance_mode']
                continue

            # Manual Swact = enabled
            m = p10.match(line)
            if m:
                ret_dict['manual_swact'] = m.groupdict()['manual_swact']
                reason = m.groupdict()['manual_swact_reason']
                if reason:
                    ret_dict['manual_swact_reason'] = reason
                continue

            # Communications = Up
            m = p11.match(line)
            if m:
                ret_dict['communications'] = m.groupdict()['communications']
                reason = m.groupdict()['communications_reason']
                if reason:
                    ret_dict['communications_reason'] = reason
                continue

            # client count = 76
            m = p12.match(line)
            if m:
                ret_dict['client_count'] = int(m.groupdict()['client_count'])
                continue

            # client_notification_TMR = 30000 milliseconds
            m = p13.match(line)
            if m:
                ret_dict['client_notification_tmr_msec'] = int(
                    m.groupdict()['client_notification_tmr_msec'])
                continue

            # RF debug mask = 0x0
            m = p14.match(line)
            if m:
                ret_dict['rf_debug_mask'] = m.groupdict()['rf_debug_mask']
                continue

        return ret_dict


# =====================
# Schema for:
#   * 'show inventory'
# =====================
class ShowInventorySchema(MetaParser):

    ''' Schema for:
        * 'show inventory'
    '''

    schema = {
        Optional('main'):
            {Optional('swstack'): bool,
             Optional(Any()):
                {Any():
                    {Optional('name'): str,
                     Optional('descr'): str,
                     Optional('pid'): str,
                     Optional('vid'): str,
                     Optional('sn'): str,
                     },
                 },
             },
        Optional('slot'):
            {Any():
                {Optional('rp'):
                    {Any():
                        {Optional('name'): str,
                         Optional('descr'): str,
                         Optional('pid'): str,
                         Optional('vid'): str,
                         Optional('sn'): str,
                         Optional('swstack_power'): str,
                         Optional('swstack_power_sn'): str,
                         Optional('subslot'):
                            {Any():
                                {Any():
                                    {Optional('name'): str,
                                     Optional('descr'): str,
                                     Optional('pid'): str,
                                     Optional('vid'): str,
                                     Optional('sn'): str,
                                     },
                                 },
                             },
                         },
                     },
                 Optional('lc'):
                    {Any():
                        {Optional('name'): str,
                         Optional('descr'): str,
                         Optional('pid'): str,
                         Optional('vid'): str,
                         Optional('sn'): str,
                         Optional('swstack_power'): str,
                         Optional('swstack_power_sn'): str,
                         Optional('subslot'):
                            {Any():
                                {Any():
                                    {Optional('name'): str,
                                     Optional('descr'): str,
                                     Optional('pid'): str,
                                     Optional('vid'): str,
                                     Optional('sn'): str,
                                     },
                                 },
                             },
                         },
                     },
                 Optional('other'):
                    {Any():
                        {Optional('name'): str,
                         Optional('descr'): str,
                         Optional('pid'): str,
                         Optional('vid'): str,
                         Optional('sn'): str,
                         Optional('swstack_power'): str,
                         Optional('swstack_power_sn'): str,
                         Optional('subslot'):
                            {Any():
                                {Any():
                                    {Optional('name'): str,
                                     Optional('descr'): str,
                                     Optional('pid'): str,
                                     Optional('vid'): str,
                                     Optional('sn'): str,
                                     },
                                 },
                             },
                         },
                     },
                 },
             },
    }


# ====================
# Parser for:
#   * 'show inventory'
# ====================
class ShowInventory(ShowInventorySchema):

    ''' Parser for:
        * 'show inventory'
    '''

    cli_command = ['show inventory']

    def cli(self, output=None):

        if output is None:
            # Build command
            cmd = self.cli_command[0]
            # Execute command
            out = self.device.execute(cmd)
        else:
            out = output

        # Init vars
        ret_dict = {}
        name = descr = slot = subslot = pid = ''
        asr900_rp = False

        # NAME: "Switch 1", DESCR: "WS-C3850-24P-E"
        # NAME: "StackPort5/2", DESCR: "StackPort5/2"
        # NAME: "Switch 5 - Power Supply A", DESCR: "Switch 5 - Power Supply A"
        # NAME: "subslot 0/0 transceiver 2", DESCR: "GE T"
        # NAME: "NIM subslot 0/0", DESCR: "Front Panel 3 ports Gigabitethernet Module"
        # NAME: "Modem 0 on Cellular0/2/0", DESCR: "Sierra Wireless EM7455/EM7430"
        # NAME: "1", DESCR: "WS-C3560CX-12PC-S"
        p1 = re.compile(r'^NAME: +\"(?P<name>.*)\",'
                        r' +DESCR: +\"(?P<descr>.*)\"$')

        # Switch 1
        # module 0
        p1_1 = re.compile(r'^(Switch|[Mm]odule) +(?P<slot>(\S+))')

        # Power Supply Module 0
        # Power Supply Module 1
        p1_2 = re.compile(r'Power Supply Module')

        # SPA subslot 0/0
        # IM subslot 0/1
        # NIM subslot 0/0
        p1_3 = re.compile(r'^(SPA|IM|NIM|PVDM) +subslot +(?P<slot>(\d+))/(?P<subslot>(\d+))')

        # subslot 0/0 transceiver 0
        p1_4 = re.compile(r'^subslot +(?P<slot>(\d+))\/(?P<subslot>(.*))')

        # StackPort1/1
        p1_5 = re.compile(r'^StackPort(?P<slot>(\d+))/(?P<subslot>(\d+))$')

        # Fan Tray
        p1_6 = re.compile(r'^Fan +Tray|\d+$')

        # Modem 0 on Cellular0/2/0
        p1_7 = re.compile(r'^Modem +(?P<modem>\S+) +on +Cellular(?P<slot>\d+)\/(?P<subslot>.*)$')

        # Slot 2 Linecard
        # Slot 3 Supervisor
        p1_8 = re.compile(r'^Slot \d Linecard|Slot \d Supervisor|Slot \d Router$')
        p1_8 = re.compile(r'^Slot \d Linecard|Slot \d Supervisor|Slot \d Router$')

        # PID: ASR-920-24SZ-IM   , VID: V01  , SN: CAT1902V19M
        # PID: SFP-10G-LR        , VID: CSCO , SN: CD180456291
        # PID: A900-IMA3G-IMSG   , VID: V01  , SN: FOC2204PAP1
        # PID: SFP-GE-T          , VID: V02  , SN: MTC2139029X
        # PID: ISR4331-3x1GE     , VID: V01  , SN:
        # PID: ISR4331/K9        , VID:      , SN: FDO21520TGH
        # PID: ISR4331/K9        , VID:      , SN:
        # PID: , VID: 1.0  , SN: 1162722191
        # PID: WS-C3560CX-12PC-S , VID: V03  , SN: FOC2419L9KY
        p2 = re.compile(r'^PID: +(?P<pid>[\S\s]+)? *, +VID:(?: +(?P<vid>(\S+)))? *,'
                        r' +SN:(?: +(?P<sn>(\S+)))?$')
        for line in out.splitlines():
            line = line.strip()

            # NAME: "Switch 1", DESCR: "WS-C3850-24P-E"
            # NAME: "StackPort5/2", DESCR: "StackPort5/2"
            # NAME: "Switch 5 - Power Supply A", DESCR: "Switch 5 - Power Supply A"
            # NAME: "subslot 0/0 transceiver 2", DESCR: "GE T"
            # NAME: "NIM subslot 0/0", DESCR: "Front Panel 3 ports Gigabitethernet Module"
            # NAME: "Modem 0 on Cellular0/2/0", DESCR: "Sierra Wireless EM7455/EM7430"
            # NAME: "1", DESCR: "WS-C3560CX-12PC-S"
            m = p1.match(line)

            if m:
                group = m.groupdict()
                name = group['name'].strip()
                descr = group['descr'].strip()

                # ------------------------------------------------------------------
                # Define slot_dict
                # ------------------------------------------------------------------

                # Switch 1
                # module 0
                m1_1 = p1_1.match(name)
                if m1_1:
                    slot = m1_1.groupdict()['slot']
                    # Creat slot_dict
                    slot_dict = ret_dict.setdefault('slot', {}).setdefault(slot, {})

                # Power Supply Module 0
                m1_2 = p1_2.match(name)
                if m1_2:
                    slot = name.replace('Power Supply Module ', 'P')
                    # Creat slot_dict
                    slot_dict = ret_dict.setdefault('slot', {}).setdefault(slot, {})

                # ------------------------------------------------------------------
                # Define subslot
                # ------------------------------------------------------------------

                # SPA subslot 0/0
                # IM subslot 0/1
                # NIM subslot 0/0
                # subslot 0/0 transceiver 0
                # StackPort1/1
                # Modem 0 on Cellular0/2/0
                m = p1_3.match(name) or p1_4.match(name) or p1_5.match(name) or p1_7.match(name)
                if m:
                    group = m.groupdict()
                    slot = group['slot']
                    subslot = group['subslot']
                    # Creat slot_dict
                    slot_dict = ret_dict.setdefault('slot', {}).setdefault(slot, {})

                # Fan Tray
                m1_6 = p1_6.match(name)
                if m1_6:
                    slot = name.replace(' ', '_')
                    # Create slot_dict
                    slot_dict = ret_dict.setdefault('slot', {}).setdefault(slot, {})

                # Slot 2 Linecard
                # Slot 3 Supervisor
                m1_8 = p1_8.match(name)
                if m1_8:
                    slot = name.replace(' ', '_')
                    # Create slot_dict
                    slot_dict = ret_dict.setdefault('slot', {}).setdefault(slot, {})

                # go to next line
                continue

            # PID: ASR-920-24SZ-IM   , VID: V01  , SN: CAT1902V19M
            # PID: SFP-10G-LR        , VID: CSCO , SN: CD180456291
            # PID: A900-IMA3G-IMSG   , VID: V01  , SN: FOC2204PAP1
            # PID: SFP-GE-T          , VID: V02  , SN: MTC2139029X
            # PID: ISR4331-3x1GE     , VID: V01  , SN:
            # PID: ISR4331/K9        , VID:      , SN: FDO21520TGH
            # PID: ISR4331/K9        , VID:      , SN:
            # PID: EM7455/EM7430     , VID: 1.0  , SN: 355813070074072
            # PID: WS-C3560CX-12PC-S , VID: V03  , SN: FOC2419L9KY
            m = p2.match(line)
            if m:
                group = m.groupdict()
                if group.get('pid'):
                    pid = group['pid'].strip(' ')
                else:
                    pid = ''
                vid = group['vid'] or ''
                sn = group['sn'] or ''

                # NAME: "Chassis", DESCR: "Cisco ASR1006 Chassis"
                if 'Chassis' in name:
                    main_dict = ret_dict.setdefault('main', {}).\
                        setdefault('chassis', {}).\
                        setdefault(pid, {})
                    main_dict['name'] = name
                    main_dict['descr'] = descr
                    main_dict['pid'] = pid
                    main_dict['vid'] = vid
                    main_dict['sn'] = sn

                if ('IE' in pid) or ('17' in pid):
                    if ('Supervisor' in name):
                        main_dict = ret_dict.setdefault('main', {}).\
                            setdefault('supervisor', {}).\
                            setdefault(pid, {})
                        main_dict['name'] = name
                        main_dict['descr'] = descr
                        main_dict['pid'] = pid
                        main_dict['vid'] = vid
                        main_dict['sn'] = sn

                if "Expansion Module" in name:
                    main_dict = ret_dict.setdefault('main', {}).\
                        setdefault('expansion_module', {}).\
                        setdefault(pid, {})
                    main_dict['name'] = name
                    main_dict['descr'] = descr
                    main_dict['pid'] = pid
                    main_dict['vid'] = vid
                    main_dict['sn'] = sn


                if 'cpu' in name or 'usb' in name:
                    main_dict = ret_dict.setdefault('main', {}).\
                        setdefault(name, {}).\
                        setdefault(pid, {})
                    main_dict['name'] = name
                    main_dict['descr'] = descr
                    main_dict['pid'] = pid
                    main_dict['vid'] = vid
                    main_dict['sn'] = sn

                main_names = [
                    'Switch1',
                    'Switch2',
                    'GigabitEthernet',
                    'TwoGigabitEthernet',
                    'TenGigabitEthernet',
                    'HundredGigE',
                    'FourHundredGigE',
                    'FiftyGigE'
                ]

                for interface in main_names:
                    if interface in name:
                        main_dict = ret_dict.setdefault('main', {}).\
                            setdefault(name, {}).\
                            setdefault(pid, {})
                        main_dict['name'] = name
                        main_dict['descr'] = descr
                        main_dict['pid'] = pid
                        main_dict['vid'] = vid
                        main_dict['sn'] = sn

                # PID: STACK-T1-50CM     , VID: V01  , SN: LCC1921G250
                if 'STACK' in pid:
                    main_dict = ret_dict.setdefault('main', {})
                    main_dict['swstack'] = True

                if ('ASR-9') in pid and ('PWR' not in pid) and ('FAN' not in pid):
                    rp_dict = ret_dict.setdefault('slot', {}).\
                        setdefault('0', {}).\
                        setdefault('rp', {}).\
                        setdefault(pid, {})
                    rp_dict['name'] = name
                    rp_dict['descr'] = descr
                    rp_dict['pid'] = pid
                    rp_dict['vid'] = vid
                    rp_dict['sn'] = sn
                    asr900_rp = True

                # Ensure name, slot have been previously parsed
                if not name or not slot:
                    continue

                # PID: ASR1000-RP2       , VID: V02  , SN: JAE153408NJ
                # PID: ASR1000-RP2       , VID: V03  , SN: JAE1703094H
                # PID: WS-C3850-24P-E    , VID: V01  , SN: FCW1932D0LB
                if ('RP' in pid) or ('WS-C' in pid) or ('R' in name):
                    rp_dict = slot_dict.setdefault('rp', {}).\
                        setdefault(pid, {})
                    rp_dict['name'] = name
                    rp_dict['descr'] = descr
                    rp_dict['pid'] = pid
                    rp_dict['vid'] = vid
                    rp_dict['sn'] = sn

                # PID: ASR1000-SIP40     , VID: V02  , SN: JAE200609WP
                # PID: ISR4331/K9        , VID:      , SN: FDO21520TGH
                # PID: ASR1002-X         , VID: V07, SN: FOX1111P1M1
                # PID: ASR1002-HX        , VID:      , SN:
                elif (('SIP' in pid)  or ('-X' in pid) or \
                     ('-HX' in pid) or ('-LC' in pid) or ('module' in name and not ('module F' in name))) and \
                     ('subslot' not in name):

                    lc_dict = slot_dict.setdefault('lc', {}).\
                        setdefault(pid, {})
                    lc_dict['name'] = name
                    lc_dict['descr'] = descr
                    lc_dict['pid'] = pid
                    lc_dict['vid'] = vid
                    lc_dict['sn'] = sn

                # PID: SP7041-E          , VID: E    , SN: MTC164204VE
                # PID: SFP-GE-T          , VID: V02  , SN: MTC2139029X
                # PID: EM7455/EM7430     , VID: 1.0  , SN: 355813070074072
                elif subslot:
                    if ('STACK' in pid):
                        try:
                            rp_dict
                        except NameError:
                            stack_dict = slot_dict.setdefault('other', {}).\
                                setdefault(pid, {})
                            subslot_dict = stack_dict.setdefault('subslot', {}).\
                                setdefault(subslot, {}).\
                                setdefault(pid, {})
                        else:
                            subslot_dict = rp_dict.setdefault('subslot', {}).\
                                setdefault(subslot, {}).\
                                setdefault(pid, {})

                    elif asr900_rp:
                        subslot_dict = rp_dict.setdefault('subslot', {}).\
                            setdefault(subslot, {}).\
                            setdefault(pid, {})
                    else:
                        if 'lc' not in slot_dict:
                            lc_dict = slot_dict.setdefault('lc', {}). \
                                setdefault(pid, {})
                        subslot_dict = lc_dict.setdefault('subslot', {}).\
                            setdefault(subslot, {}).\
                            setdefault(pid, {})
                    subslot_dict['name'] = name
                    subslot_dict['descr'] = descr
                    subslot_dict['pid'] = pid
                    subslot_dict['vid'] = vid
                    subslot_dict['sn'] = sn

                # PID: ASR1006-PWR-AC    , VID: V01  , SN: ART1210Q049
                # PID: ASR1006-PWR-AC    , VID: V01  , SN: ART1210Q04C
                # PID: ASR-920-FAN-M     , VID: V01  , SN: CAT1903V028
                else:
                    other_dict = slot_dict.setdefault('other', {}).\
                        setdefault(pid, {})
                    other_dict['name'] = name
                    other_dict['descr'] = descr
                    other_dict['pid'] = pid
                    other_dict['vid'] = vid
                    other_dict['sn'] = sn

                # Reset to avoid overwrite
                name = descr = slot = subslot = ''
                continue

        return ret_dict


class ShowPlatformSchema(MetaParser):
    """Schema for show platform"""
    schema = {
        Optional('main'): {
            Optional('switch_mac_address'): str,
            Optional('mac_persistency_wait_time'): str,
            Optional('chassis'): str,
            Optional('swstack'): bool
        },
        'slot': {
            Any(): {
                Optional('rp'): {
                    Any(): {
                        Optional('sn'): str,
                        Optional('state'): str,
                        Optional('num_of_ports'): str,
                        Optional('mac_address'): str,
                        Optional('hw_ver'): str,
                        Optional('sw_ver'): str,
                        Optional('swstack_role'): str,
                        Optional('swstack_priority'): str,
                        Optional('ports'): str,
                        Optional('role'): str,
                        Optional('name'): str,
                        Optional('slot'): str,
                        Optional('priority'): str,
                        Optional('insert_time'): str,
                        Optional('fw_ver'): str,
                        Optional('cpld_ver'): str,
                    }
                },
                Optional('lc'): {
                    Any(): {
                        Optional('cpld_ver'): str,
                        Optional('fw_ver'): str,
                        Optional('insert_time'): str,
                        Optional('name'): str,
                        Optional('slot'): str,
                        Optional('state'): str,
                        Optional('subslot'): {
                            Any(): {
                                Any(): {
                                    Optional('insert_time'): str,
                                    Optional('name'): str,
                                    Optional('state'): str,
                                    Optional('subslot'): str,
                                }
                            }
                        }
                    }
                },
                Optional('other'): {
                    Any(): {
                        Optional('cpld_ver'): str,
                        Optional('fw_ver'): str,
                        Optional('insert_time'): str,
                        Optional('name'): str,
                        Optional('slot'): str,
                        Optional('state'): str,
                        Optional('subslot'): {
                            Any(): {
                                Any(): {
                                    Optional('insert_time'): str,
                                    Optional('name'): str,
                                    Optional('state'): str,
                                    Optional('subslot'): str,
                                }
                            }
                        }
                    }
                }
            }
        }
    }


class ShowPlatform(ShowPlatformSchema):
    """Parser for show platform
    parser class - implements detail parsing mechanisms for cli output.
    """
    # *************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).

    cli_command = 'show platform'
    exclude = ['insert_time']

    def cli(self, output=None):
        """parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: exe
        cuting, transforming, returning
        """
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        platform_dict = {}
        sub_dict = {}

        # ----------      C3850    -------------

        # Switch/Stack Mac Address : 0057.d2ff.e71b - Local Mac Address
        p1 = re.compile(r'^[Ss]witch\/[Ss]tack +[Mm]ac +[Aa]ddress +\: +'
                        r'(?P<switch_mac_address>[\w\.]+) *(?P<local>[\w\s\-]+)?$')

        # Mac persistency wait time: Indefinite
        p2 = re.compile(r'^[Mm]ac +persistency +wait +time\: +(?P<mac_persistency_wait_time>[\w\.\:]+)$')

        # Switch  Ports    Model                Serial No.   MAC address     Hw Ver.       Sw Ver.
        # ------  -----   ---------             -----------  --------------  -------       --------
        #  1       32     WS-C3850-24P-E        FCW1947C0HH  0057.d2ff.e71b  V07           16.6.1
        #  1       32     C9200-24P             JAD2310213C  dc8c.37ff.ad21  V01           17.05.01
        #  1       32     C9200-24P             JAD2310213C  dc8c.37ff.ad21  V01           2021-03-03_18.
        p3 = re.compile(r'^(?P<switch>\d+) +(?P<ports>\d+) +'
                        r'(?P<model>[\w\-]+) +(?P<serial_no>\w+) +'
                        r'(?P<mac_address>[\w\.\:]+) +'
                        r'(?P<hw_ver>\w+) +(?P<sw_ver>[\s\S]+)$')

        #                                     Current
        # Switch#   Role        Priority      State
        # -------------------------------------------
        # *1       Active          3          Ready
        p4 = re.compile(r'^\*?(?P<switch>\d+) +(?P<role>\w+) +'
                        r'(?P<priority>\d+) +(?P<state>[\w\s]+)$')

        # ----------      ASR1K    -------------
        # Chassis type: ASR1006
        # Chassis type: ASR-903
        p5 = re.compile(r'^[Cc]hassis +type: +(?P<chassis>\S+)$')

        # Slot      Type                State                 Insert time (ago)
        # --------- ------------------- --------------------- -----------------
        # 0         ASR1000-SIP40       ok                    00:33:53
        # 0/0       SPA-1XCHSTM1/OC3    ok                    2d00h
        # F0                            ok, active            00:09:23
        # P1        Unknown             N/A                   never
        # 1/0       SM-X-E2-20UXF       admin down            00:00:03
        # F0        C8500-20X6C         init, active          00:01:37
        p6 = re.compile(r'^(?P<slot>[\w]+)(\/)?(?P<subslot>\d+)?\s*(?P<name>[\w\-_+\/]+)?\s*'\
                        r'(?P<state>(ok|unknown|admin down|ok, active|N\/A|ok, standby|init, active'\
                        r'|ps, fail|empty|incompatible|inserted|fail|disabled|booting|init, standby))\s*'\
                        r'(?P<insert_time>[\w\.\:]+)$')

        # 4                             unknown               2d00h
        p6_1 = re.compile(r'^(?P<slot>\w+) +(?P<state>\w+(\, \w+)?) +(?P<insert_time>[\w\.\:]+)$')

        # Slot      CPLD Version        Firmware Version
        # --------- ------------------- ---------------------------------------
        # 0         00200800            16.2(1r)
        p7 = re.compile(r'^(?P<slot>\w+) +(?P<cpld_version>\d+|N\/A) +(?P<fireware_ver>[\w\.\(\)\/]+)$')

        for line in out.splitlines():
            line = line.strip()

            # Switch/Stack Mac Address : 0057.d2ff.e71b - Local Mac Address
            m = p1.match(line)
            if m:
                if 'main' not in platform_dict:
                    platform_dict['main'] = {}
                platform_dict['main']['switch_mac_address'] = m.groupdict()['switch_mac_address']
                platform_dict['main']['swstack'] = True
                continue

            # Mac persistency wait time: Indefinite
            m = p2.match(line)
            if m:
                if 'main' not in platform_dict:
                    platform_dict['main'] = {}
                platform_dict['main']['mac_persistency_wait_time'] = m.groupdict()['mac_persistency_wait_time'].lower()
                continue

            # Switch  Ports    Model                Serial No.   MAC address     Hw Ver.       Sw Ver.
            # ------  -----   ---------             -----------  --------------  -------       --------
            #  1       32     WS-C3850-24P-E        FCW1947C0HH  0057.d2ff.e71b  V07           16.6.1
            #  1       32     C9200-24P             JAD2310213C  dc8c.37ff.ad21  V01           17.05.01
            #  1       32     C9200-24P             JAD2310213C  dc8c.37ff.ad21  V01           2021-03-03_18.
            m = p3.match(line)
            if m:
                slot = m.groupdict()['switch']
                model = m.groupdict()['model']
                if 'slot' not in platform_dict:
                    platform_dict['slot'] = {}
                if slot not in platform_dict['slot']:
                    platform_dict['slot'][slot] = {}

                if ('WS-C' in model or 'C9500' in model or 'C9300' in model or 'C9200' in model or
                   'IE-32' in model or 'IE-33' in model or 'IE-34' in model or 'IE-93' in model or
                   'IE-31' in model or '1783' in model or 'C9350' in model):
                    lc_type = 'rp'
                else:
                    lc_type = 'other'

                if lc_type not in platform_dict['slot'][slot]:
                    platform_dict['slot'][slot][lc_type] = {}
                if model not in platform_dict['slot'][slot][lc_type]:
                    platform_dict['slot'][slot][lc_type][model] = {}
                platform_dict['slot'][slot][lc_type][model]['hw_ver'] = m.groupdict()['hw_ver']
                platform_dict['slot'][slot][lc_type][model]['mac_address'] = m.groupdict()['mac_address']
                platform_dict['slot'][slot][lc_type][model]['name'] = model
                platform_dict['slot'][slot][lc_type][model]['ports'] = m.groupdict()['ports']
                platform_dict['slot'][slot][lc_type][model]['slot'] = slot
                platform_dict['slot'][slot][lc_type][model]['sn'] = m.groupdict()['serial_no']
                platform_dict['slot'][slot][lc_type][model]['sw_ver'] = m.groupdict()['sw_ver']
                continue

            #                                     Current
            # Switch#   Role        Priority      State
            # -------------------------------------------
            # *1       Active          3          Ready
            m = p4.match(line)
            if m:
                slot = m.groupdict()['switch']
                if 'slot' not in platform_dict:
                    continue
                if slot not in platform_dict['slot']:
                    continue

                for key, value in platform_dict['slot'][slot].items():
                    for key, last in value.items():
                        last['swstack_priority'] = m.groupdict()['priority']
                        last['swstack_role'] = m.groupdict()['role']
                        last['state'] = m.groupdict()['state']
                continue

            # Chassis type: ASR1006
            # Chassis type: ASR-903
            m = p5.match(line)
            if m:
                if 'main' not in platform_dict:
                    platform_dict['main'] = {}
                platform_dict['main']['chassis'] = m.groupdict()['chassis']
                continue

            # Slot      Type                State                 Insert time (ago)
            # --------- ------------------- --------------------- -----------------
            # 0         ASR1000-SIP40       ok                    00:33:53
            #  0/0      SPA-1XCHSTM1/OC3    ok                    2d00h
            # 0         C8200-1N-4T         ok                    00:32:26
            m = p6.match(line)
            if m:
                slot = m.groupdict()['slot']
                subslot = m.groupdict()['subslot']
                name = m.groupdict()['name']
                if name:

                    # subslot
                    if subslot:
                        try:
                            # no-slot-type output:
                            # Slot      Type                State                 Insert time (ago)

                            # --------- ------------------- --------------------- -----------------

                            # 0/2      A900-IMA8Z          ok                    1w4d

                            if 'slot' not in platform_dict:
                                platform_dict['slot'] = {}
                            if slot not in platform_dict['slot']:
                                platform_dict['slot'][slot] = {}
                            # if slot not in platform_dict['slot']:
                            #     continue

                            slot_items = platform_dict['slot'][slot].items()

                            # for no-slot-type output
                            if not slot_items:
                                if re.match(r'^ASR\d+-(\d+T\S+|SIP\d+|X)|ISR|C9|C82|C83', name):
                                    if 'R' in slot:
                                        lc_type = 'rp'
                                    elif re.match(r'^\d+', slot):
                                        lc_type = 'lc'
                                    else:
                                        lc_type = 'other'
                                elif re.match(r'^ASR\d+-RP\d+', name):
                                    lc_type = 'rp'
                                elif re.match(r'^CSR\d+V', name):
                                    if 'R' in slot:
                                        lc_type = 'rp'
                                    else:
                                        lc_type = 'other'
                                else:
                                    lc_type = 'other'

                                if lc_type not in platform_dict['slot'][slot]:
                                    platform_dict['slot'][slot][lc_type] = {}

                                if name not in platform_dict['slot'][slot][lc_type]:
                                    platform_dict['slot'][slot][lc_type][name] = {}
                                sub_dict = platform_dict['slot'][slot][lc_type][name]
                                sub_dict['slot'] = slot

                            # Add subslot
                            for key, value in slot_items:
                                for key, last in value.items():
                                    if 'subslot' not in last:
                                        last['subslot'] = {}
                                    if subslot not in last['subslot']:
                                        last['subslot'][subslot] = {}
                                    if name not in last['subslot'][subslot]:
                                        last['subslot'][subslot][name] = {}
                                    sub_dict = last['subslot'][subslot][name]
                            sub_dict['subslot'] = subslot

                        # KeyError: 'slot'
                        except Exception:
                            continue
                    else:
                        if 'slot' not in platform_dict:
                            platform_dict['slot'] = {}
                        if slot not in platform_dict['slot']:
                            platform_dict['slot'][slot] = {}
                        if re.match(r'^ASR\d+-(\d+T\S+|SIP\d+|X)|ISR|C9|C82|C83', name):
                            if 'R' in slot:
                                lc_type = 'rp'
                            elif re.match(r'^\d+', slot):
                                lc_type = 'lc'
                            else:
                                lc_type = 'other'
                        elif re.match(r'^ASR\d+-RP\d+', name):
                            lc_type = 'rp'
                        elif re.match(r'^CSR\d+V', name):
                            if 'R' in slot:
                                lc_type = 'rp'
                            else:
                                lc_type = 'other'
                        else:
                            lc_type = 'other'

                        if lc_type not in platform_dict['slot'][slot]:
                            platform_dict['slot'][slot][lc_type] = {}

                        if name not in platform_dict['slot'][slot][lc_type]:
                            platform_dict['slot'][slot][lc_type][name] = {}
                        sub_dict = platform_dict['slot'][slot][lc_type][name]
                        sub_dict['slot'] = slot

                    sub_dict['name'] = name
                    sub_dict['state'] = m.groupdict()['state'].strip()
                    sub_dict['insert_time'] = m.groupdict()['insert_time']
                    continue

            # Slot      CPLD Version        Firmware Version
            # --------- ------------------- ---------------------------------------
            # 0         00200800            16.2(1r)
            m = p7.match(line)
            if m:
                fw_ver = m.groupdict()['fireware_ver']
                cpld_ver = m.groupdict()['cpld_version']
                slot = m.groupdict()['slot']

                if 'slot' not in platform_dict:
                    continue
                if slot not in platform_dict['slot']:
                    continue

                for key, value in platform_dict['slot'][slot].items():
                    for key, last in value.items():
                        last['cpld_ver'] = m.groupdict()['cpld_version']
                        last['fw_ver'] = m.groupdict()['fireware_ver']
                continue

            # 4                             unknown               2d00h
            m = p6_1.match(line)
            if m:
                slot = m.groupdict()['slot']
                if 'slot' not in platform_dict:
                    platform_dict['slot'] = {}
                if slot not in platform_dict['slot']:
                    platform_dict['slot'][slot] = {}

                if 'other' not in platform_dict['slot'][slot]:
                    platform_dict['slot'][slot]['other'] = {}
                    platform_dict['slot'][slot]['other'][''] = {}
                platform_dict['slot'][slot]['other']['']['slot'] = slot
                platform_dict['slot'][slot]['other']['']['name'] = ''
                platform_dict['slot'][slot]['other']['']['state'] = m.groupdict()['state']
                platform_dict['slot'][slot]['other']['']['insert_time'] = m.groupdict()['insert_time']
                continue

        return platform_dict


class ShowBootSchema(MetaParser):
    """Schema for show boot"""

    schema = {
        Optional('current_boot_variable'): str,
        Optional('next_reload_boot_variable'): str,
        Optional('manual_boot'): bool,
        Optional('enable_break'): bool,
        Optional('boot_mode'): str,
        Optional('ipxe_timeout'): int,
        Optional('active'): {
            Optional('configuration_register'): str,
            Optional('boot_variable'): str,
            Optional('manual_boot'): bool,
        },
        Optional('standby'): {
            Optional('configuration_register'): str,
            Optional('boot_variable'): str,
            Optional('manual_boot'): bool,
        },
        Optional('boot_path_list'): str,
        Optional('config_file'): str,
        Optional('private_config_file'): str,
        Optional('enable_break'): bool,
        Optional('manual_boot'): bool,
        Optional('helper_path_list'): str,
        Optional('auto_upgrade'): bool,
        Optional('auto_upgrade_path'): str,
        Optional('boot_optimization'): bool,
        Optional('nvram_buffer_size'): int,
        Optional('timeout_config_download'): str,
        Optional('config_download_via_dhcp'): bool,
        Optional('next_boot'): bool,
        Optional('allow_dev_key'): bool,
        Optional('switches'): {
            Any(): {
                'boot_path_list': str,
                'config_file': str,
                'private_config_file': str,
                'enable_break': bool,
                'manual_boot': bool,
                Optional('helper_path_list'): str,
                'auto_upgrade': bool,
                Optional('auto_upgrade_path'): str,
                Optional('boot_optimization'): bool,
                Optional('nvram_buffer_size'): int,
                Optional('timeout_config_download'): str,
                Optional('config_download_via_dhcp'): bool,
                Optional('next_boot'): bool,
                Optional('allow_dev_key'): bool,
            },
        },
    }


class ShowBoot(ShowBootSchema):
    """Parser for show boot"""
    SW_MAPPING = {
        'BOOT path-list ': 'boot_path_list',
        'Config file': 'config_file',
        'Private Config file': 'private_config_file',
        'Enable Break': 'enable_break',
        'Manual Boot': 'manual_boot',
        'Allow Dev Key': 'allow_dev_key',
        'HELPER path-list': 'helper_path_list',
        'Auto upgrade': 'auto_upgrade',
        'Auto upgrade path': 'auto_upgrade_path',
        'Boot optimization': 'boot_optimization',
        'NVRAM/Config file buffer size': 'nvram_buffer_size',
        'Timeout for Config Download': 'timeout_config_download',
        'Config Download via DHCP': 'config_download_via_dhcp'
    }
    TRUE_FALSE = {
        'disable': False,
        'disabled': False,
        'no': False,
        'enable': True,
        'enabled': True,
        'yes': True
    }

    cli_command = 'show boot'

    def cli(self, output=None):

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        boot_dict = {}
        boot_variable = None
        switch_number = 0

        # Current Boot Variables:
        p1 = re.compile(r'Current +Boot +Variables:$')

        # Boot Variables on next reload:
        p1_2 = re.compile(r'Boot +Variables +on +next +reload:$')

        # BOOT variable = bootflash:/asr1000rpx.bin,12;
        # BOOT variable = flash:cat3k_caa-universalk9.BLD_POLARIS_DEV_LATEST_20150907_031219.bin;
        #                 flash:cat3k_caa-universalk9.BLD_POLARIS_DEV_LATEST_20150828_174328.SSA.bin;flash:ISSUCleanGolden;
        # BOOT variable = tftp://10.1.144.25//auto/tftptest-blr/latest//cat9k_iosxe.BLD_V173_THROTTLE_LATEST_20200427_012602.SSA.bin
        # BOOT variable = tftp://10.1.144.25//auto/tftptest-blr/latest//cat9k_iosxe.BLD_V173_THROTTLE_LATEST_20200428_021754.SSA.bin;bootflash:/cat9k_iosxe.BLD_POLARIS_DEV_LATEST_20200429_051305.SSA_starfleet-1.bin;
        p1_1 = re.compile(r'^BOOT +variable +=( *(?P<var>\S+);?)?$')

        # Standby BOOT variable = bootflash:/asr1000rpx.bin,12;
        p2 = re.compile(r'^Standby +BOOT +variable +=( *(?P<var>\S+);)?$')

        # Configuration register is 0x2002
        # Configuration Register is 0x102
        p3 = re.compile(r'^Configuration +[r|R]egister +is +(?P<var>\w+)$')

        # Standby Configuration register is 0x2002
        p4 = re.compile(r'^Standby +Configuration +register'
                        ' +is +(?P<var>\w+)$')

        # Manual Boot = yes
        p5 = re.compile(r'^Manual +Boot += +(?P<var>\w+)$')

        # MANUAL_BOOT variable = no
        p5_1 = re.compile(r'(^MANUAL_BOOT +variable) += +(?P<var>\w+)$')

        # Standby MANUAL_BOOT variable = no
        p5_2 = re.compile(r'(^Standby +MANUAL_BOOT +variable) += +(?P<var>\w+)$')

        # Enable Break = yes
        p6 = re.compile(r'^Enable +Break += +(?P<var>\w+)$')

        # Boot Mode = DEVICE
        p7 = re.compile(r'^Boot +Mode += +(?P<var>\S+)$')

        # iPXE Timeout = 0
        p8 = re.compile(r'^iPXE +Timeout +=? +(?P<var>\w+)$')

        # BOOT path-list{      : flash:/c2960x-universalk9-mz.152-4.E8.bin
        # HELPER path-list    :
        p9 = re.compile(r'^(?P<key>BOOT|HELPER) +path\-list +\:(?: '
                        r'+(?P<value>[\w\:\/\-\.]+)?)$')

        # Config file         : flash:/config.text
        # Private Config file : flash:/private-config.text
        # Enable Break        : yes
        # Manual Boot         : no
        # Allow Dev Key         : yes
        # Auto upgrade        : no
        # Auto upgrade path   :
        p10 = re.compile(r'^(?P<key>[\w\s]+) +\: +(?P<value>[\w\:\/\-\.]+)$')

        # buffer size:   524288
        p11 = re.compile(r'buffer +size\: +(?P<value>\d+)$')

        # Download:    0 seconds
        p12 = re.compile(r'Download\: +(?P<value>\d+ +\w+)$')

        # via DHCP:       disabled (next boot: disabled)
        p13 = re.compile(r'via +DHCP\: +(?P<value>\w+) +\(next +boot\: '
                            r'+(?P<next_boot>\w+)\)$')

        # Switch 2
        # switch 3
        p14 = re.compile(r'^[Ss]witch +(?P<switch_number>\d+)$')

        # BOOT path-list      :
        p15 = re.compile(r'^(?P<key>BOOT) +path\-list +\:$')

        for line in out.splitlines():
            line = line.strip()

            # Current Boot Variables:
            m1 = p1.match(line)
            if m1:
                boot_variable = 'current'
                continue

            # Boot Variables on next reload:
            m1_2 = p1_2.match(line)
            if m1_2:
                boot_variable = 'next'
                continue

            # BOOT variable = bootflash:/asr1000rpx.bin,12;
            # BOOT variable = flash:cat3k_caa-universalk9.BLD_POLARIS_DEV_LATEST_20150907_031219.bin;
            #                 flash:cat3k_caa-universalk9.BLD_POLARIS_DEV_LATEST_20150828_174328.SSA.bin;flash:ISSUCleanGolden;
            # BOOT variable = tftp://10.1.144.25//auto/tftptest-blr/latest//cat9k_iosxe.BLD_V173_THROTTLE_LATEST_20200427_012602.SSA.bin
            # BOOT variable = tftp://10.1.144.25//auto/tftptest-blr/latest//cat9k_iosxe.BLD_V173_THROTTLE_LATEST_20200428_021754.SSA.bin;bootflash:/cat9k_iosxe.BLD_POLARIS_DEV_LATEST_20200429_051305.SSA_starfleet-1.bin;
            m1_1 = p1_1.match(line)
            if m1_1:
                boot = m1_1.groupdict()['var']
                if boot:
                    if boot_variable == 'current':
                        boot_dict['current_boot_variable'] = boot
                    elif boot_variable == 'next':
                        boot_dict['next_reload_boot_variable'] = boot
                    else:
                        if 'active' not in boot_dict:
                            boot_dict['active'] = {}
                        boot_dict['active']['boot_variable'] = boot
                continue

            # Standby BOOT variable = bootflash:/asr1000rpx.bin,12;
            m2 = p2.match(line)
            if m2:
                if m2.groupdict()['var']:
                    if 'standby' not in boot_dict:
                        boot_dict['standby'] = {}
                        boot_dict['standby']['boot_variable'] = m2.groupdict()['var']
                continue

            # Configuration register is 0x2002
            # Configuration Register is 0x102
            m3 = p3.match(line)
            if m3:
                if 'active' not in boot_dict:
                    boot_dict['active'] = {}
                boot_dict['active']['configuration_register'] = m3.groupdict()['var']
                continue

            # Standby Configuration register is 0x2002
            m4 = p4.match(line)
            if m4:
                if 'standby' not in boot_dict:
                    boot_dict['standby'] = {}
                boot_dict['standby']['configuration_register'] = m4.groupdict()['var']
                continue

            # Manual Boot = yes
            m5 = p5.match(line)
            if m5:
                boot_dict['manual_boot'] = True if \
                    m5.groupdict()['var'].lower() == 'yes' else\
                    False
                continue

            # MANUAL_BOOT variable = no
            m5_1 = p5_1.match(line)
            if m5_1:
                if 'active' not in boot_dict:
                    boot_dict['active'] = {}
                boot_dict['active']['manual_boot'] = True if \
                    m5_1.groupdict()['var'].lower() == 'yes' else\
                    False
                continue

            # Standby MANUAL_BOOT variable = no
            m5_2 = p5_2.match(line)
            if m5_2:
                if 'standby' not in boot_dict:
                    boot_dict['standby'] = {}
                boot_dict['standby']['manual_boot'] = True if \
                    m5_2.groupdict()['var'].lower() == 'yes' else\
                    False
                continue

            # Enable Break = yes
            m6 = p6.match(line)
            if m6:
                boot_dict['enable_break'] = True if \
                    m6.groupdict()['var'].lower() == 'yes' else\
                    False
                continue

            # Boot Mode = DEVICE
            m7 = p7.match(line)
            if m7:
                boot_dict['boot_mode'] = m7.groupdict()['var'].lower()
                continue

            # iPXE Timeout = 0
            m8 = p8.match(line)
            if m8:
                boot_dict['ipxe_timeout'] = int(m8.groupdict()['var'])
                continue

            # BOOT path-list      : flash:/c2960x-universalk9-mz.152-4.E8.bin
            # HELPER path-list    :
            m9 = p9.match(line)
            if m9:
                group = m9.groupdict()
                if 'BOOT' in group['key']:
                    sw_dict = boot_dict
                    if switch_number >= 2:
                        switches_dict = sw_dict.setdefault('switches', {})
                        index_dict = switches_dict.setdefault(
                            switch_number, {})
                        index_dict.update({'boot_path_list': m9.groupdict()['value']})
                    else:
                        index_dict = sw_dict
                        index_dict.update({'boot_path_list': m9.groupdict()['value']})

                elif 'HELPER' in group['key']:
                    index_dict.update({'helper_path_list': m9.groupdict()['value']})

                continue

            # Config file         : flash:/config.text
            # Private Config file : flash:/private-config.text
            # Enable Break        : yes
            # Manual Boot         : no
            # Allow Dev Key         : yes
            # Auto upgrade        : no
            # Auto upgrade path   :
            m10 = p10.match(line)
            if m10:
                group = m10.groupdict()

                key = self.SW_MAPPING.get(group['key'].strip())
                true_false = self.TRUE_FALSE.get(group['value'])

                if isinstance(true_false, bool):
                    index_dict[key] = true_false
                else:
                    index_dict[key] = group['value']

                continue

            # buffer size:   524288
            m11 = p11.match(line)
            if m11:
                index_dict.update({'nvram_buffer_size': int(m11.groupdict()['value'])})

                continue

            # Download:    0 seconds
            m12 = p12.match(line)
            if m12:
                index_dict.update({'timeout_config_download': m12.groupdict()['value']})

                continue

            # via DHCP:       disabled (next boot: disabled)
            m13 = p13.match(line)
            if m13:
                group = m13.groupdict()
                value = self.TRUE_FALSE.get(group['value'])
                next_boot = self.TRUE_FALSE.get(group['next_boot'])
                index_dict.update({'config_download_via_dhcp': value})
                index_dict.update({'next_boot': next_boot})

                continue

            # Switch 2
            # switch 3
            m14 = p14.match(line)
            if m14:
                switch_number = int(m14.groupdict()['switch_number'])

                continue

            # BOOT path-list      :
            m15 = p15.match(line)
            if m15:
                sw_dict = boot_dict
                index_dict = sw_dict

                continue

        return boot_dict


class ShowSwitchDetailSchema(MetaParser):
    """Schema for show switch detail"""
    schema = {
        'switch': {
            'mac_address': str,
            Optional('mac_persistency_wait_time'): str,
            'stack': {
                Any(): {
                    'role': str,
                    'mac_address': str,
                    'priority': str,
                    Optional('hw_ver'): str,
                    'state': str,
                    'ports': {
                        Any(): {
                            'stack_port_status': str,
                            'neighbors_num': Or(int, str)
                        },
                    }
                },
            }
        }
    }


class ShowSwitchDetail(ShowSwitchDetailSchema):
    """Parser for show switch detail."""

    cli_command = 'show switch detail'
    STACK_PORT_RANGE = ('1', '2')

    def cli(self, output=None):

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # return empty when no output
        if not out:
            return ret_dict

        # initial regexp pattern

        # Switch/Stack Mac Address : 0057.d2ff.e71b - Local Mac Address
        p1 = re.compile(r'^[Ss]witch\/[Ss]tack +[Mm]ac +[Aa]ddress +\: +'
                        '(?P<switch_mac_address>[\w\.]+) *(?P<local>[\w\s\-]+)?$')

        # Mac persistency wait time: Indefinite
        p2 = re.compile(r'^[Mm]ac +persistency +wait +time\: +'
                        '(?P<mac_persistency_wait_time>[\w\.\:]+)$')

        #                                              H/W   Current
        # Switch#   Role    Mac Address     Priority Version  State
        # -----------------------------------------------------------
        # *1       Active   689c.e2ff.b9d9     3      V04     Ready
        #  2       Standby  689c.e2ff.b9d9     14             Ready
        #  3       Member   bbcc.fcff.7b00     15     0       V-Mismatch
        p3_0 = re.compile(r'^Switch#\s+Role\s+Mac\sAddress\s+Priority\s+Version\s+State$')

        p3_1 = re.compile(r'^\*?(?P<switch>\d+) +(?P<role>\w+) +'
                           '(?P<mac_address>[\w\.]+) +'
                           '(?P<priority>\d+) +'
                           '(?P<hw_ver>\w+)? +'
                           '(?P<state>[\w\s-]+)$')

        #          Stack Port Status             Neighbors
        # Switch#  Port 1     Port 2           Port 1   Port 2
        #   1         OK         OK               3        2
        #   1       DOWN       DOWN             None     None
        p4_0 = re.compile(r'^Switch#\s+Port\s1\s+Port\s2\s+Port\s1\s+Port\s2$')

        p4_1 = re.compile(r'^(?P<switch>\d+) +(?P<status1>\w+) +'
                           '(?P<status2>\w+) +'
                           '(?P<nbr_num_1>\w+) +'
                           '(?P<nbr_num_2>\w+)$')

        active_table = 0

        for line in out.splitlines():
            line = line.strip()

            # Switch/Stack Mac Address : 0057.d2ff.e71b - Local Mac Address
            m = p1.match(line)
            if m:
                ret_dict['mac_address'] = m.groupdict()['switch_mac_address']
                continue

            # Mac persistency wait time: Indefinite
            m = p2.match(line)
            if m:
                ret_dict['mac_persistency_wait_time'] = m.groupdict()['mac_persistency_wait_time'].lower()
                continue

            # In order to know which regex (p3_1 or p4_1) should be used, we use p3_0 and p4_0 to determine which table
            # is currently parsed.
            m = p3_0.match(line)
            if m:
                active_table = 1
                continue

            m = p4_0.match(line)
            if m:
                active_table = 2
                continue

            #                                              H/W   Current
            # Switch#   Role    Mac Address     Priority Version  State
            # -----------------------------------------------------------
            # *1       Active   689c.e2ff.b9d9     3      V04     Ready
            #  2       Standby  689c.e2ff.b9d9     14             Ready
            m = p3_1.match(line)
            if m and active_table == 1:
                group = m.groupdict()
                stack = group['switch']
                match_dict = {k: v.lower()for k, v in group.items() if k in ['role', 'state']}
                match_dict.update({k: v for k, v in group.items() if k in ['priority', 'mac_address', 'hw_ver'] and v})
                ret_dict.setdefault('stack', {}).setdefault(stack, {}).update(match_dict)
                continue

            #          Stack Port Status             Neighbors
            # Switch#  Port 1     Port 2           Port 1   Port 2
            # --------------------------------------------------------
            #   1         OK         OK               3        2
            #   1       DOWN       DOWN             None     None
            m = p4_1.match(line)
            if m and active_table == 2:
                group = m.groupdict()
                stack = group['switch']
                stack_ports = ret_dict.setdefault('stack', {}).setdefault(stack, {}).setdefault('ports', {})
                for port in self.STACK_PORT_RANGE:
                    port_dict = stack_ports.setdefault(port, {})
                    port_dict['stack_port_status'] = group['status{}'.format(port)].lower()
                    nbr_num = group['nbr_num_{}'.format(port)]
                    port_dict['neighbors_num'] = int(nbr_num) if nbr_num.isdigit() else nbr_num
                continue

        return {'switch': ret_dict} if ret_dict else {}



class ShowSwitchSchema(MetaParser):
    """Schema for show switch"""
    schema = {
        'switch': {
            'mac_address': str,
            Optional('mac_persistency_wait_time'): str,
            'stack': {
                Any(): {
                    'role': str,
                    'mac_address': str,
                    'priority': str,
                    Optional('hw_ver'): str,
                    'state': str
                },
            }
        }
    }


class ShowSwitch(ShowSwitchSchema, ShowSwitchDetail):
    """Parser for show switch."""
    cli_command = 'show switch'


# ===================================================
# Schema for
#   * 'show env all'
#   * 'show env fan'
#   * 'show env power'
#   * 'show env power all'
#   * 'show env rps
#   * 'show env stack'
#   * 'show env temperature'
#   * 'show env temperature status'
#   * 'show environment all'
# ===================================================
class ShowEnvironmentSchema(MetaParser):
    """Schema for show environment all"""
    schema = {
        'switch': {
            Any(): {
                Optional('fan'): {
                    Any(): {
                        Optional('speed'): int,
                        Optional('direction'): str,
                        Optional('state'): str
                    }
                },
                Optional('power_supply'): {
                    Any(): {
                        Optional('state'): str,
                        Optional('pid'): str,
                        Optional('serial_number'): str,
                        Optional('status'): str,
                        Optional('system_power'): str,
                        Optional('poe_power'): str,
                        Optional('watts'): str,
                        Optional('temperature'): str,
                        Optional('power_source'): str,
                        Optional('type'): str,
                        Optional('mode'): str
                    }
                },
                Optional('sensors_details'): {
                    Any(): {
                        Optional('location'): str,
                        Optional('state'): str,
                        Optional('reading'): int,
                        Optional('unit'): str,
                        Optional('range'): str
                    }
                },
                Optional('system_temperature_state'): str,
                Optional('inlet_temperature'): {
                    'value': Or(int,str),
                    'state': str,
                    'yellow_threshold': str,
                    'red_threshold': str
                },
                Optional('hotspot_temperature'): {
                    'value': str,
                    'state': str,
                    'yellow_threshold': str,
                    'red_threshold': str
                },
                Optional('asic_temperature'): {
                    'value': str,
                    'state': str,
                    'yellow_threshold': str,
                    'red_threshold': str
                },
                Optional('outlet_temperature'): {
                    'value': str,
                    'state': str,
                    'yellow_threshold': str,
                    'red_threshold': str
                },
                Optional('system_temperature'): {
                    'value': str,
                    'state': str,
                    'yellow_threshold': str,
                    'red_threshold': str
                },
                Optional('redundant_power_system'): {
                    str: {
                        'status': str,
                        Optional('serial_num'): str,
                        Optional('port_num'): str,
                    }
                }
            }
        }

    }


# ===================================================
# Superparser for
#   * 'show env all'
#   * 'show env fan'
#   * 'show env power'
#   * 'show env power all'
#   * 'show env rps
#   * 'show env stack'
#   * 'show env temperature'
#   * 'show env temperature status'
#   * 'show environment all'
# ===================================================
class ShowEnvironmentSuperParser(ShowEnvironmentSchema):
    """Parser for show environment all"""
    PS_MAPPING = {'A': '1', 'B': '2'}

    def cli(self, output):

        # initial return dictionary
        ret_dict = {}

        # SWITCH: 1
        p0 = re.compile(r'^SWITCH: +(?P<switch>\d+)$')

        # Switch 1 FAN 1 is OK
        p1 = re.compile(r'^Switch\s+(?P<switch>\d+)\s+FAN\s+(?P<fan>\d+)\s+is\s+(?P<state>\S+)$')

        # Switch 1 FAN 1 direction is Front to Back
        p1_1 = re.compile(r'^Switch\s+(?P<switch>\d+)\s+FAN +(?P<fan>\d+)\s+direction\s+is\s+(?P<direction>[\w\s]+)$')

        # Switch   FAN   Speed   State
        # ---------------------------------------------------
        # 1     1 35840     OK
        p1_2 = re.compile(r'^(?P<switch>\d+)\s+(?P<fan>\d+)\s+(?P<speed>\d+)\s+(?P<state>\w+)$')

        # Switch     FAN     Speed   State   Airflow direction
        # ---------------------------------------------------
        # 2           1       5600    OK     Front to Back
        p1_3 = re.compile(r'^(?P<switch>\d+)\s+(?P<fan>\d+)\s+(?P<speed>\d+)\s+(?P<state>\w+)\s+(?P<direction>[\w\s]+)$')

        # FAN PS-1 is NOT PRESENT
        # FAN PS-2 is OK
        p2 = re.compile(r'^FAN\s+PS\-(?P<ps>\d+)\s+is\s+(?P<state>[\w\s]+)$')

        # Switch 1: SYSTEM TEMPERATURE is OK
        # SYSTEM TEMPERATURE is OK
        p3 = re.compile(r'^(Switch\s+(?P<switch>\d+):\s+)?SYSTEM\s+TEMPERATURE\s+is\s+(?P<state>[\w\s]+)$')

        # Inlet Temperature Value: 34 Degree Celsius
        # Hotspot Temperature Value: 45 Degree Celsius
        # ASIC Temperature Value: 36 Degree Celsius
        # System Temperature Value: 41 Degree Celsius
        # Temperature Value: 28 Degree Celsius
        p4 = re.compile(r'^((?P<type>\w+)\s+)?Temperature\s+Value:\s+(?P<temperature>\d+)\s+Degree\s+Celsius$')

        # System Temperature State: GREEN
        # Temperature State: GREEN
        p5 = re.compile(r'^(System\s+)?Temperature\s+State:\s+(?P<state>\w+)$')


        # Yellow Threshold : 66 Degree Celsius
        # Red Threshold    : 76 Degree Celsius
        p6 = re.compile(r'^(?P<color>\w+)\s+Threshold\s*:\s+(?P<temperature>\d+)\s+Degree\s+Celsius$')

        # POWER SUPPLY 1A TEMPERATURE: OK
        # POWER SUPPLY 1B TEMPERATURE: Not Present
        p7 = re.compile(r'^POWER\s+SUPPLY\s+(?P<switch>\d+)(?P<power_supply>A|B)\s+'
                        r'TEMPERATURE:\s+(?P<temperature>[\w\s]+)$')

        # 1A  PWR-C1-715WAC       DCB1844G1ZY  OK              Good     Good     715
        # 1A  PWR-C2-1025WAC      DCB1636C003  OK              Good     Good     250/775
        # 1B  Not Present
        p8 = re.compile(r'^(?P<sw>\d+)(?P<ps>\w+)\s*'
                        r'((?P<pid>[\w\-]+)\s+'
                        r'(?P<serial_number>\w+)\s+)?'
                        r'(?P<status>(\w+|Not\sPresent|No\s+Input\s+Power))\s*'
                        r'((?P<system_power>\w+)\s+'
                        r'(?P<poe_power>[\w\/]+)\s+'
                        r'(?P<watts>[\w\/]+))?$')

        # 1   Not Present     <>
        p9 = re.compile(r'^(?P<switch>\d+)\s+(?P<status>\w+|Not\s+Present)\s+'
                         r'(?P<rps_name>\w+|<>)(\s+(?P<rps_serial_num>\w+)\s+'
                         r'(?P<rps_port_num>\w+))?$')

        #Gi1/1/1        Type3          60(w)     Available
        p10 = re.compile(r'^(?P<power_source>[\w./]+)\s+(?P<type>\w+)\s+(?P<watts>\S+)\(w\)\s+(?P<mode>\S+)')

        #A.C. Input     Auxilliary     150(w)    Available
        p11 = re.compile(r'^(?P<power_source>A.C. Input|\S+)\s+(?P<type>\w+)\s+(?P<watts>\S+)\(w\)\s+(?P<mode>\S+)')

        #Built-In                      310(w)
        p12 = re.compile(r'^(?P<power_source>A.C. Input|\S+)\s+(?P<watts>\S+)\(w\)')

        # Switch   FAN     Speed   State   Airflow direction
        # ---------------------------------------------------
        #     1       1     5160      OK     Front to Back
        p13 = re.compile(r'^\s*(?P<switch>\d+)\s+(?P<fan>\d+)\s+(?P<speed>\d+)\s+(?P<state>\w+)\s+(?P<direction>\S+\s+\S+\s+\S+)$')

        #Sensor          Location        State               Reading       Range(min-max)
        # PS1 Vout        1               GOOD               12000 mV          na
        # PS1 Curout      1               GOOD               25000 mA          na
        # PS1 Powout      1               GOOD              300000 mW          na
        # PS1 Hotspot     1               GOOD                  24 Celsius     na
        # PS1 Fan Status  1               GOOD               43008 rpm         na
        p14 = re.compile(r"^\s*(?P<sensor>PS\d+\s+\S+(?:\s+\S+)?)\s+(?P<location>\d+)\s+(?P<state>\S+)\s+(?P<reading>\d+)\s+(?P<unit>\S+)\s+\S+")

        # SYSTEM INLET    1               GREEN                 23 Celsius   0 - 56
        # SYSTEM OUTLET   1               GREEN                 28 Celsius   0 - 125
        # SYSTEM HOTSPOT  1               GREEN                 38 Celsius   0 - 125
        p15 = re.compile(r"^\s*(?P<sensor>SYSTEM+\s+\S+(?:\s+\S+)?)\s+(?P<location>\d+)\s+(?P<state>\S+)\s+(?P<reading>\d+)\s+(?P<unit>\S+)\s+(?P<range>\d+\s*-\s*\d+)$")
        # set default value for switch
        switch = 1

        for line in output.splitlines():
            line = line.strip()

            # SWITCH: 1
            m = p0.match(line)
            if m:
                switch = m.groupdict()['switch']
                root_dict = ret_dict.setdefault('switch', {}).setdefault(switch, {})
                continue

            # Switch 1 FAN 1 is OK
            m = p1.match(line)
            if m:
                group = m.groupdict()
                switch = group['switch']
                fan = group['fan']
                root_dict = ret_dict.setdefault('switch', {}).setdefault(switch, {})
                root_dict.setdefault('fan', {}).setdefault(fan, {}).setdefault('state', group['state'].lower())
                continue

            # Switch 1 FAN 1 direction is Front to Back
            m = p1_1.match(line)
            if m:
                group = m.groupdict()
                switch = group['switch']
                fan = group['fan']
                fan_dict = ret_dict.setdefault('switch', {}).setdefault(switch, {})\
                                   .setdefault('fan', {}).setdefault(fan, {})
                fan_dict.update({'direction': group['direction'].lower()})
                continue

            # Switch   FAN   Speed   State
            # ---------------------------------------------------
            # 1     1 35840     OK
            m = p1_2.match(line)
            if m:
                group = m.groupdict()
                switch = group['switch']
                fan = group['fan']
                root_dict = ret_dict.setdefault('switch', {}).setdefault(switch, {})
                root_dict.setdefault('fan', {}).setdefault(fan, {}).setdefault('state', group['state'].lower())
                continue

            # Switch     FAN     Speed   State   Airflow direction
            # ---------------------------------------------------
            # 2           1       5600    OK     Front to Back
            m = p1_3.match(line)
            if m:
                group = m.groupdict()
                switch = group['switch']
                fan = group['fan']
                root_dict = ret_dict.setdefault('switch', {}).setdefault(switch, {})
                fan_dict = root_dict.setdefault('fan', {}).setdefault(fan, {})
                fan_dict['state'] = group['state'].lower()
                fan_dict['speed'] = int(group['speed'])
                fan_dict['direction'] = group['direction'].lower()
                continue

            # FAN PS-1 is OK
            # FAN PS-1 is NOT PRESENT
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ps = group['ps']
                power_supply_dict = root_dict.setdefault('power_supply', {}).setdefault(ps, {})
                power_supply_dict.setdefault('state', group['state'].lower())
                continue

            # Switch 1: SYSTEM TEMPERATURE is OK
            # SYSTEM TEMPERATURE is OK
            m = p3.match(line)
            if m:
                group = m.groupdict()
                if group['switch']:
                    switch = group['switch']
                root_dict = ret_dict.setdefault('switch', {}).setdefault(switch, {})
                root_dict['system_temperature_state'] = group['state'].lower()
                continue

            # Inlet Temperature Value: 34 Degree Celsius
            # Hotspot Temperature Value: 45 Degree Celsius
            # ASIC Temperature Value: 36 Degree Celsius
            # System Temperature Value: 41 Degree Celsius
            # Temperature Value: 28 Degree Celsius
            m = p4.match(line)
            if m:
                group = m.groupdict()
                if group['type']:
                    temp_type = group['type'].lower() + '_temperature'
                else:
                    temp_type = 'system_temperature'
                root_dict = ret_dict.setdefault('switch', {}).setdefault(str(switch), {})
                temp_dict = root_dict.setdefault(temp_type, {})
                temp_dict['value'] = group['temperature']
                continue

            # Temperature State: GREEN
            m = p5.match(line)
            if m:
                try:
                    temp_dict['state'] = m.groupdict()['state'].lower()
                except UnboundLocalError:
                    root_dict = ret_dict.setdefault('switch', {}).setdefault(str(switch), {})
                    temp_dict = root_dict.setdefault("system_temperature", {})
                    temp_dict['state'] = m.groupdict()['state'].lower()
                continue

            # Yellow Threshold : 46 Degree Celsius
            # Red Threshold    : 56 Degree Celsius
            m = p6.match(line)
            if m:
                group = m.groupdict()
                color_type = group['color'].lower() + '_threshold'
                temp_dict[color_type] = group['temperature']
                continue

            # POWER SUPPLY 1A TEMPERATURE: OK
            # POWER SUPPLY 1B TEMPERATURE: Not Present
            m = p7.match(line)
            if m:
                switch = m.groupdict()['switch']
                power_supply = self.PS_MAPPING[m.groupdict()['power_supply']]
                root_dict = ret_dict.setdefault('switch', {}).setdefault(switch, {})
                power_supply_dict = root_dict.setdefault('power_supply', {}).setdefault(power_supply, {})
                power_supply_dict.setdefault('temperature', m.groupdict()['temperature'].lower())
                continue


            # SW  PID                 Serial#     Status           Sys Pwr  PoE Pwr  Watts
            # --  ------------------  ----------  ---------------  -------  -------  -----
            # 1A  PWR-C1-715WAC       DCB1844G1ZY  OK              Good     Good     715
            # 1A  PWR-C2-1025WAC      DCB1636C003  OK              Good     Good     250/775
            # 1B  Not Present
            m = p8.match(line)
            if m:
                group = m.groupdict()
                switch = group.pop('sw')
                ps = self.PS_MAPPING[group.pop('ps')]
                root_dict = ret_dict.setdefault('switch', {}).setdefault(switch, {})
                power_supply_dict = root_dict.setdefault('power_supply', {}).setdefault(ps, {})
                power_supply_dict.update({k: v for k, v in group.items() if k in ['pid', 'serial_number', 'watts'] and v})
                power_supply_dict.update({k: v.lower() for k, v in group.items()
                     if k in ['status', 'system_power', 'poe_power'] and v})
                continue

            # SW  Status          RPS Name          RPS Serial#  RPS Port#
            # --  -------------   ----------------  -----------  ---------
            # 1   Not Present     <>
            m = p9.match(line)
            if m:
                group = m.groupdict()
                switch = group['switch']
                rps_name = group['rps_name']
                root_dict = ret_dict.setdefault('switch', {}).setdefault(switch, {})
                redundant_power_system_dict = root_dict.setdefault('redundant_power_system', {}).setdefault(rps_name, {})
                redundant_power_system_dict['status'] = group['status'].lower()
                if group['rps_serial_num']:
                    redundant_power_system_dict['rps_serial_num'] = group['rps_serial_num']
                if group['rps_port_num']:
                    redundant_power_system_dict['rps_port_num'] = group['rps_port_num']
                continue

            #Gi1/1/1        Type3          60(w)     Available
            m = p10.match(line)

            if m:
                group = m.groupdict()
                intf = Common.convert_intf_name(group.pop('power_source'))
                root_dict = ret_dict.setdefault('switch', {}).setdefault(switch, {})
                power_supply_dict = root_dict.setdefault('power_supply', {}).setdefault(intf, {})
                power_supply_dict["power_source"] =  intf
                power_supply_dict.update({k: v for k, v in group.items()})
                continue

            #A.C. Input     Auxilliary     150(w)    Available
            m = p11.match(line)
            if m:
                group = m.groupdict()
                root_dict = ret_dict.setdefault('switch', {}).setdefault(switch, {})
                power_supply_dict = root_dict.setdefault('power_supply', {}).setdefault(group['power_source'], {})
                power_supply_dict.update({k: v for k, v in group.items()})
                continue

            #Built-In                      310(w)
            m = p12.match(line)
            if m:
                group = m.groupdict()
                root_dict = ret_dict.setdefault('switch', {}).setdefault(switch, {})
                power_supply_dict = root_dict.setdefault('power_supply', {}).setdefault(group['power_source'], {})
                power_supply_dict.update({k: v for k, v in group.items()})
                continue

            # Switch   FAN     Speed   State   Airflow direction
            # ---------------------------------------------------
            # 1       1     5160      OK     Front to Back
            m = p13.match(line)
            if m:
                group = m.groupdict()
                switch = group['switch']
                fan = group['fan']
                fan_dict = ret_dict.setdefault('switch', {}).setdefault(switch, {})\
                    .setdefault('fan', {}).setdefault(fan, {})
                fan_dict.update({
                    'speed': int(group['speed']),
                    'state': group['state'].lower(),
                    'direction': group['direction'].lower(),
                })
                continue

            #Sensor          Location        State               Reading       Range(min-max)
            # PS1 Vout        1               GOOD               12000 mV          na
            # PS1 Curout      1               GOOD               25000 mA          na
            # PS1 Powout      1               GOOD              300000 mW          na
            # PS1 Hotspot     1               GOOD                  24 Celsius     na
            # PS1 Fan Status  1               GOOD               43008 rpm         na
            m = p14.match(line)
            if m:
                group = m.groupdict()
                location = group['location']
                sensors = group['sensor']
                sensor_dict = ret_dict.setdefault('switch', {}).setdefault(location, {})\
                    .setdefault('sensors_details', {}).setdefault(sensors, {})
                sensor_dict.update({
                    'location': group['location'],
                    'state': group['state'],
                    'reading': int(group['reading']),
                    'unit': group['unit']
                })

                continue

            # SYSTEM INLET    1               GREEN                 23 Celsius   0 - 56
            # SYSTEM OUTLET   1               GREEN                 28 Celsius   0 - 125
            # SYSTEM HOTSPOT  1               GREEN                 38 Celsius   0 - 125
            m = p15.match(line)
            if m:
                group = m.groupdict()
                location = group['location']
                sensors = group['sensor']
                sensor_dict = ret_dict.setdefault('switch', {}).setdefault(location, {})\
                    .setdefault('sensors_details', {}).setdefault(sensors, {})
                sensor_dict.update({
                    'location': group['location'],
                    'state': group['state'],
                    'reading': int(group['reading']),
                    'unit': group['unit'],
                    'range': group['range']
                })

                continue

        return ret_dict


# ===================================================
# Parser for 'show environment all'
# ===================================================
class ShowEnvironmentAll(ShowEnvironmentSuperParser):
    """Parser for show environment all'
    """

    cli_command = 'show environment all'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        return super().cli(output=output)


# ===================================================
# Parser for 'show env all'
# ===================================================
class ShowEnvAll(ShowEnvironmentSuperParser):
    """Parser for show env all'
    """

    cli_command = 'show env all'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        return super().cli(output=output)

# ===================================================
# Parser for 'show env fan'
# ===================================================
class ShowEnvFan(ShowEnvironmentSuperParser):
    """Parser for show env fan"""

    cli_command = 'show env fan'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        return super().cli(output=out)


# ===================================================
# Parser for 'show env power'
# ===================================================
class ShowEnvPower(ShowEnvironmentSuperParser):
    """Parser for show env power"""

    cli_command = 'show env power'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        return super().cli(output=out)


# ===================================================
# Parser for 'show env power all'
# ===================================================
class ShowEnvPowerAll(ShowEnvironmentSuperParser):
    """Parser for show env power all"""

    cli_command = 'show env power all'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        return super().cli(output=output)


# ===================================================
# Parser for 'show env rps'
# ===================================================
class ShowEnvRPS(ShowEnvironmentSuperParser):
    """Parser for show env rps"""

    cli_command = 'show env rps'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        return super().cli(output=out)


# ===================================================
# Parser for 'show env stack'
# ===================================================
class ShowEnvStack(ShowEnvironmentSuperParser):
    """Parser for show env stack"""

    cli_command = 'show env stack'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        return super().cli(output=out)


# ===================================================
# Parser for 'show env temperature'
# ===================================================
class ShowEnvTemperature(ShowEnvironmentSuperParser):
    """Parser for show env temperature"""

    cli_command = 'show env temperature'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        return super().cli(output=out)


# ===================================================
# Parser for 'show env temperature status'
# ===================================================
class ShowEnvTemperatureStatus(ShowEnvironmentSuperParser):
    """Parser for show env temperature status"""

    cli_command = 'show env temperature status'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        return super().cli(output=output)


class ShowModuleSchema(MetaParser):
    """Schema for show module"""
    schema = {
        Optional('switch'): {
            Any(): {
                'port': str,
                'model': str,
                'serial_number': str,
                'mac_address': str,
                'hw_ver': str,
                'sw_ver': str
            },
        },
        Optional('module'):{
            int:{
                'ports':int,
                'card_type':str,
                'model':str,
                Optional('serial'):str,
                'mac_address':str,
                'hw':str,
                'fw':str,
                'sw':str,
                'status':str,
                Optional('redundancy_role'):str,
                Optional('operating_redundancy_mode'):str,
                Optional('configured_redundancy_mode'):str,
            },
        },
        Optional('number_of_mac_address'):int,
        Optional('chassis_mac_address_lower_range'):str,
        Optional('chassis_mac_address_upper_range'):str,
        Optional('switches'):{
            int:{
                Optional('module'):{
                    int:{
                        'ports':int,
                        'card_type':str,
                        'model':str,
                        'serial':str,
                        'mac_address':str,
                        'hw':str,
                        'fw':str,
                        'sw':str,
                        'status':str,
                        Optional('redundancy_role'):str,
                        Optional('operating_redundancy_mode'):str,
                        Optional('configured_redundancy_mode'):str
                    },
                },
            },
        },
        Optional('chassis'): {
            int:{
                'number_of_mac_address':int,
                'chassis_mac_address_lower_range':str,
                'chassis_mac_address_upper_range':str,
            },
        },
    }


class ShowModule(ShowModuleSchema):
    """Parser for show module"""

    cli_command = 'show module'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # initial return dictionary
        ret_dict = {}
        switch_flag = False

        # initial regexp pattern
        p1 = re.compile(r'^(?P<switch>\d+) *'
                        '(?P<port>\w+) +'
                        '(?P<model>[\w\-]+) +'
                        '(?P<serial_number>\w+) +'
                        '(?P<mac_address>[\w\.]+) +'
                        '(?P<hw_ver>\w+) +'
                        '(?P<sw_ver>[\w\.]+)$')

        # Chassis Type: C9500X-28C8D

        # Mod Ports Card Type                                   Model          Serial No.
        # ---+-----+--------------------------------------+--------------+--------------
        # 1   38   Cisco Catalyst 9500X-28C8D Switch           C9500X-28C8D     FDO25030SLN

        p2=re.compile(r'^(?P<mod>\d+) +(?P<ports>\d+) +(?P<card_type>[\w\/()\-\+]+(?: [\w\/()\-\+]+)*) +(?P<model>\S+)(\s+)?(?P<serial>\S+)?$')

        # Mod MAC addresses                    Hw   Fw           Sw                 Status
        # ---+--------------------------------+----+------------+------------------+--------
        # 1   F87A.4125.1400 to F87A.4125.147D 0.2  17.7.0.41     BLD_POLARIS_DEV_LA ok

        p3=re.compile(r'^(?P<mod>\d+) +(?P<mac_address>([\w\.]+ +to +[\w\.]+)|unknown) +(?P<hw>\S+) +(?P<fw>\S+) +(?P<sw>\S+) +(?P<status>\S+)$')

        # Mod Redundancy Role     Operating Redundancy Mode Configured Redundancy Mode
        # ---+-------------------+-------------------------+---------------------------
        # 1   Active              non-redundant             Non-redundant

        p4=re.compile(r'^(?P<mod>\d+) *(?P<redundancy_role>\S+) *(?P<operating_redundancy_mode>\S+) *(?P<configured_redundancy_mode>\S+)$')

        # Chassis MAC address range: 512 addresses from f87a.4125.1400 to f87a.4125.15ff
        p5=re.compile(r'^Chassis MAC address range: (?P<number_of_mac_address>\d+) addresses from (?P<chassis_mac_address_lower_range>.*) to (?P<chassis_mac_address_upper_range>.*)$')

        # Switch Number 1
        p6 = re.compile(r'^Switch\s+Number\s+(?P<switch_number>\d+)$')

        # Chassis 1 MAC address range: 512 addresses from 40b5.c1ff.ee00 to 40b5.c1ff.efff
        p7=re.compile(r'^Chassis\s*(?P<chassis>\d+)\s*MAC address range: (?P<number_of_mac_address>\d+) addresses from (?P<chassis_mac_address_lower_range>.*) to (?P<chassis_mac_address_upper_range>.*)$')


        for line in output.splitlines():
            line = line.strip()

            # Switch  Ports    Model                Serial No.   MAC address     Hw Ver.       Sw Ver.
            # ------  -----   ---------             -----------  --------------  -------       --------
            #  1       56     WS-C3850-48P-E        FOC1902X062  689c.e2ff.b9d9  V04           16.9.1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                switch = group.pop('switch')
                switch_dict = ret_dict.setdefault('switch', {}).setdefault(switch, {})
                switch_dict.update({k: v.lower() for k, v in group.items()})
                continue

            # Switch Number 1
            m = p6.match(line)
            if m:
                group = m.groupdict()
                s_dict = ret_dict.setdefault('switches', {}).setdefault(int(group['switch_number']), {})
                switch_flag=True


            # Chassis Type: C9500X-28C8D

            # Mod Ports Card Type                                   Model          Serial No.
            # ---+-----+--------------------------------------+--------------+--------------
            # 1   38   Cisco Catalyst 9500X-28C8D Switch           C9500X-28C8D     FDO25030SLN
            m = p2.match(line)
            if m:
                group = m.groupdict()
                switch = group.pop('mod')
                if switch_flag:
                    switch_dict = s_dict.setdefault('module', {}).setdefault(int(switch), {})
                else:
                    switch_dict = ret_dict.setdefault('module', {}).setdefault(int(switch), {})
                if not group.get('serial'):
                    group.pop('serial')
                switch_dict.update({k: v.strip() for k, v in group.items()})
                switch_dict['ports']=int(group['ports'])
                continue

            # Mod MAC addresses                    Hw   Fw           Sw                 Status
            # ---+--------------------------------+----+------------+------------------+--------
            # 1   F87A.4125.1400 to F87A.4125.147D 0.2  17.7.0.41     BLD_POLARIS_DEV_LA ok

            m=p3.match(line)
            if m:
                group = m.groupdict()
                switch = group.pop('mod')
                if switch_flag:
                    switch_dict = s_dict.setdefault('module', {}).setdefault(int(switch), {})
                else:
                    switch_dict = ret_dict.setdefault('module', {}).setdefault(int(switch), {})
                switch_dict.update({k: v.strip() for k, v in group.items()})
                continue

            # Mod Redundancy Role     Operating Redundancy Mode Configured Redundancy Mode
            # ---+-------------------+-------------------------+---------------------------
            # 1   Active              non-redundant             Non-redundant
            m=p4.match(line)
            if m:
                group = m.groupdict()
                switch = group.pop('mod')
                if switch_flag:
                    switch_dict = s_dict.setdefault('module', {}).setdefault(int(switch), {})
                else:
                    switch_dict = ret_dict.setdefault('module', {}).setdefault(int(switch), {})
                switch_dict.update({k: v.lower().strip() for k, v in group.items()})
                continue

            #Chassis MAC address range: 512 addresses from f87a.4125.1400 to f87a.4125.15ff
            m=p5.match(line)
            if m:
                group=m.groupdict()
                ret_dict.update({k: v.lower().strip() for k, v in group.items()})
                ret_dict['number_of_mac_address'] = int(group['number_of_mac_address'])
                continue

            # Chassis MAC address range: 512 addresses from f87a.4125.1400 to f87a.4125.15ff
            m=p7.match(line)
            if m:
                group=m.groupdict()
                if switch_flag:
                    chassis_dict = ret_dict.setdefault('chassis', {}).setdefault(int(group['chassis']), {})
                    chassis_dict['number_of_mac_address'] = int(group['number_of_mac_address'])
                    chassis_dict['chassis_mac_address_lower_range'] = group['chassis_mac_address_lower_range']
                    chassis_dict['chassis_mac_address_upper_range'] = group['chassis_mac_address_upper_range']

                continue

        return ret_dict


class ShowProcessesCpuSortedSchema(MetaParser):
    """Schema for show processes cpu sorted
                  show processes cpu sorted <1min|5min|5sec>
                  show processes cpu sorted | include <WORD>
                  show processes cpu sorted | exclude <WORD>
                  show processes cpu sorted <1min|5min|5sec> | include <WORD>
                  show processes cpu sorted <1min|5min|5sec> | exclude <WORD>"""

    schema = {
        Optional('core'): {
            Any(): {
                Optional('five_sec_cpu_interrupts'): int,
                Optional('five_sec_cpu_total'): int,
                Optional('one_min_cpu'): int,
                Optional('five_min_cpu'): int,
                Optional('zero_cpu_processes'): list,
                Optional('nonzero_cpu_processes'): list,
                Optional('sort'):{
                    Any(): {
                        'runtime': int,
                        'invoked': int,
                        'usecs': int,
                        'five_sec_cpu': float,
                        'one_min_cpu': float,
                        'five_min_cpu': float,
                        'tty': int,
                        'pid': int,
                        'process': str
                    },
                },
            },
        },
        Optional('five_sec_cpu_interrupts'): int,
        Optional('five_sec_cpu_total'): int,
        Optional('one_min_cpu'): int,
        Optional('five_min_cpu'): int,
        Optional('zero_cpu_processes'): list,
        Optional('nonzero_cpu_processes'): list,
        Optional('sort'): {
            Any(): {
                'runtime': int,
                'invoked': int,
                'usecs': int,
                'five_sec_cpu': float,
                'one_min_cpu': float,
                'five_min_cpu': float,
                'tty': int,
                'pid': int,
                'process': str
            }
        }
    }


class ShowProcessesCpuSorted(ShowProcessesCpuSortedSchema):
    """Parser for show processes cpu sorted
                  show processes cpu sorted {sort_time}
                  show processes cpu sorted | include {key_word}
                  show processes cpu sorted | exclude {exclude}
                  show processes cpu sorted {sort_time} | include {key_word}
                  show processes cpu sorted {sort_time} | exclude {exclude}"""

    cli_command = [
        'show processes cpu sorted',
        'show processes cpu sorted {sort_time}',
        'show processes cpu sorted | include {key_word}',
        'show processes cpu sorted | exclude {exclude}',
        'show processes cpu sorted {sort_time} | include {key_word}',
        'show processes cpu sorted {sort_time} | exclude {exclude}'
    ]

    exclude = ['five_min_cpu', 'five_sec_cpu_total', 'nonzero_cpu_processes', 'zero_cpu_processes',
               'five_sec_cpu', 'invoked', 'one_min_cpu', 'runtime', 'usecs', 'pid', 'process', ]

    def cli(self, sort_time='', key_word='', exclude='', cmd='', output=None):

        assert sort_time in ['1min', '5min', '5sec', ''], "Not one from 1min 5min 5sec"
        if output is None:
            if not cmd:
                if sort_time and key_word:
                    cmd = self.cli_command[4].format(sort_time=sort_time, key_word=key_word)
                elif sort_time and exclude:
                    cmd = self.cli_command[5].format(sort_time=sort_time, exclude=exclude)
                elif exclude:
                    cmd = self.cli_command[3].format(exclude=exclude)
                elif key_word:
                    cmd = self.cli_command[2].format(key_word=key_word)
                elif sort_time:
                    cmd = self.cli_command[1].format(sort_time=sort_time)
                else:
                    cmd = self.cli_command[0]

            out = self.device.execute(cmd)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}
        zero_cpu_processes = []
        nonzero_cpu_processes = []
        index = 0

        # initial regexp pattern
        #Core 0 : CPU utilization for five seconds: 5%/1%; one minute: 6%; five minutes: 6%
        p1 = re.compile(r'^(Core\s+(?P<core>[\w\s]+): +)?CPU +utilization +for +five +seconds: '
                        r'+(?P<five_sec_cpu_total>\d+)\%(\/(?P<five_sec_cpu_interrupts>\d+)\%)?; +one +minute: '
                        r'+(?P<one_min_cpu>\d+)\%; +five +minutes: +(?P<five_min_cpu>\d+)\%$')

        #PID    Runtime(ms) Invoked  uSecs  5Sec     1Min     5Min     TTY   Process
        # 5782   2045595     13521147 208    4.52     6.10     5.85     0     iosd
        # 22     1520051     62763660 24     0.02     0.02     0.02     0     sirq-net-rx/1
        p2 = re.compile(r'^(?P<pid>\d+) +(?P<runtime>\d+) +(?P<invoked>\d+) +(?P<usecs>\d+) +(?P<five_sec_cpu>[\d\.]+)(\%)? +'
                        r'(?P<one_min_cpu>[\d\.]+)(\%)? +(?P<five_min_cpu>[\d\.]+)(\%)? +(?P<tty>\d+) +(?P<process>.+)$')

        for line in out.splitlines():
            line = line.strip()

            # CPU utilization for five seconds: 5%/1%; one minute: 6%; five minutes: 6%
            #Core 0 : CPU utilization for five seconds: 5%/1%; one minute: 6%; five minutes: 6%
            m = p1.match(line)
            if m:
                group = m.groupdict()
                if group['core'] is None:
                    ret_dict.update({k:int(v) for k, v in m.groupdict().items() if k != 'core'})
                else:
                    cpu_dict = ret_dict.setdefault('core', {}).setdefault(group['core'], {})
                    cpu_dict.update({k:int(v) for k, v in m.groupdict().items() if v is not None and k != 'core'})

                continue

            # PID Runtime(ms)     Invoked      uSecs   5Sec   1Min   5Min TTY Process
            # 539     6061647    89951558         67  0.31%  0.36%  0.38%   0 HSRP Common

            # PID    Runtime(ms) Invoked  uSecs  5Sec     1Min     5Min     TTY   Process
            # 5782   2045595     13521147 208    4.52     6.10     5.85     0     iosd
            # 22     1520051     62763660 24     0.02     0.02     0.02     0     sirq-net-rx/1
            m = p2.match(line)
            if m:
                group = m.groupdict()
                index += 1
                sort_dict = ret_dict.setdefault('sort', {}).setdefault(index, {})
                sort_dict['process'] = group['process']
                sort_dict.update({k: int(v) for k, v in group.items()
                                  if k in ['runtime', 'invoked', 'usecs', 'tty', 'pid']})
                sort_dict.update({k: float(v) for k, v in group.items()
                                  if k in ['five_sec_cpu', 'one_min_cpu', 'five_min_cpu']})
                if float(group['five_sec_cpu']) or \
                   float(group['one_min_cpu']) or \
                   float(group['five_min_cpu']):
                    nonzero_cpu_processes.append(group['process'])
                else:
                    zero_cpu_processes.append(group['process'])
                continue

        ret_dict.setdefault('zero_cpu_processes',
                            zero_cpu_processes) if zero_cpu_processes else None
        ret_dict.setdefault('nonzero_cpu_processes',
                            nonzero_cpu_processes) if nonzero_cpu_processes else None
        return ret_dict


class ShowProcessesCpuPlatformSchema(MetaParser):
    """Schema for show processes cpu platform"""
    schema = {
        'cpu_utilization': {
            'cpu_util_five_secs': str,
            'cpu_util_one_min': str,
            'cpu_util_five_min': str,
            Optional('core'): {
                Any(): {
                    'core_cpu_util_five_secs': str,
                    'core_cpu_util_one_min': str,
                    'core_cpu_util_five_min': str,
                },
            }
        },
        'pid': {
            Any(): {
                'ppid': int,
                'five_sec': str,
                'one_min': str,
                'five_min': str,
                'status': str,
                'size': int,
                'name': str,
            },
        }
    }


class ShowProcessesCpuPlatform(ShowProcessesCpuPlatformSchema):
    """Parser for show processes cpu platform"""

    cli_command = 'show processes cpu platform'
    exclude = ['five_min_cpu', 'nonzero_cpu_processes', 'zero_cpu_processes', 'invoked',
               'runtime', 'usecs', 'five_sec_cpu', 'one_min_cpu']

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern

        # CPU utilization for five seconds: 43%, one minute: 44%, five minutes: 44%
        p1 = re.compile(r'^CPU +utilization +for +five +seconds: +(?P<cpu_util_five_secs>[\d\%]+),'
                        ' +one +minute: +(?P<cpu_util_one_min>[\d\%]+),'
                        ' +five +minutes: +(?P<cpu_util_five_min>[\d\%]+)$')

        # Core 0: CPU utilization for five seconds:  6%, one minute: 11%, five minutes: 11%
        p2 = re.compile(r'^(?P<core>[\w\s]+): +CPU +utilization +for'
                        ' +five +seconds: +(?P<core_cpu_util_five_secs>\d+\%+),'
                        ' +one +minute: +(?P<core_cpu_util_one_min>[\d+\%]+),'
                        ' +five +minutes: +(?P<core_cpu_util_five_min>[\d+\%]+)$')

        # 21188   21176    599%    600%    599%  R           478632  ucode_pkt_PPE0
        p3 = re.compile(r'^(?P<pid>\d+) +(?P<ppid>\d+)'
                        ' +(?P<five_sec>[\d\%]+) +(?P<one_min>[\d\%]+)'
                        ' +(?P<five_min>[\d\%]+) +(?P<status>[\w]+)'
                        ' +(?P<size>\d+) +(?P<name>.*)$')

        for line in out.splitlines():
            line = line.strip()

            # CPU utilization for five seconds:  2%, one minute:  5%, five minutes: 22%
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('cpu_utilization', {})
                ret_dict['cpu_utilization'].update({k: str(v) for k, v in group.items()})
                continue

            # Core 0: CPU utilization for five seconds:  2%, one minute:  8%, five minutes: 18%
            m = p2.match(line)
            if m:
                group = m.groupdict()
                core = group.pop('core')
                if 'cpu_utilization' not in ret_dict:
                    ret_dict.setdefault('cpu_utilization', {})
                ret_dict['cpu_utilization'].setdefault('core', {}).setdefault(core, {})
                ret_dict['cpu_utilization']['core'][core].update({k: str(v) for k, v in group.items()})
                continue

            #    Pid    PPid    5Sec    1Min    5Min  Status        Size  Name
            # --------------------------------------------------------------------------------
            #      1       0      0%      0%      0%  S          1863680  init
            #      2       0      0%      0%      0%  S                0  kthreadd
            #      3       2      0%      0%      0%  S                0  migration/0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                pid = group['pid']
                ret_dict.setdefault('pid', {}).setdefault(pid, {})
                ret_dict['pid'][pid]['ppid'] = int(group['ppid'])
                ret_dict['pid'][pid]['five_sec'] = group['five_sec']
                ret_dict['pid'][pid]['one_min'] = group['one_min']
                ret_dict['pid'][pid]['five_min'] = group['five_min']
                ret_dict['pid'][pid]['status'] = group['status']
                ret_dict['pid'][pid]['size'] = int(group['size'])
                ret_dict['pid'][pid]['name'] = group['name']
                continue

        return ret_dict


class ShowEnvironmentSchema(MetaParser):
    """Schema for show environment
                  show environment | include {include} """

    schema = {
        Optional('critical_larams'): int,
        Optional('major_alarms'): int,
        Optional('minor_alarms'): int,
        'slot': {
            Any(): {
                'sensor': {
                    Any(): {
                        'state': str,
                        'reading': str,
                        Optional('threshold'): {
                            Optional('minor'): int,
                            Optional('major'): int,
                            Optional('critical'): int,
                            Optional('shutdown'): int,
                            'celsius' : bool
                        },
                    },
                }
            },
        }
    }


class ShowEnvironment(ShowEnvironmentSchema):
    """Parser for show environment
                  show environment | include {include} """

    cli_command = ['show environment', 'show environment | include {include}']

    def cli(self, include='', output=None):
        if output is None:
            if include:
                cmd = self.cli_command[1].format(include=include)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # Number of Critical alarms:  0
        p1 = re.compile(r'^Number +of +Critical +alarms: +(?P<critic_larams>\d+)$')

        # Number of Major alarms:     0
        p2 = re.compile(r'^Number +of +Major +alarms: +(?P<maj_alarms>\d+)$')

        # Number of Minor alarms:     0
        p3 = re.compile(r'^Number +of +Minor +alarms: +(?P<min_alarms>\d+)$')

        # Slot    Sensor       Current State       Reading          Threshold(Minor,Major,Critical,Shutdown)
        # ----    ------       -------------       -------          ---------------------------------------
        #  F0    Temp: Pop Die    Normal           43 Celsius
        #  P6    Temp: FC PWM1    Fan Speed 60%    26 Celsius
        #  P0    Iin              Normal           1 A
        #  P0    Vin              Normal           101 V AC
        #  R0    Temp: SCBY AIR   Normal           45 Celsius
        #  R0    3570DB2 _0: VO   Normal          1201 mV
        #  R1    V2: VMD          Normal           991 mV
        #  R0          3570MB2_0: VOU  Normal          1000 mV            na
        #  R0          Temp: Outlet_A  Normal          34   Celsius       (55 ,60 ,65 ,75 )(Celsius)
        #  R0          Temp: UADP_0_4  Normal          45   Celsius       (105,110,120,124)(Celsius)

        #R0 Temp: Inlet Critical 47 Celsius (na ,na ,47 ,na )(Celsius)
        #R0 Temp: Internal Normal 47 Celsius (na ,na ,na ,na )(Celsius)
        p4 = re.compile(r'^(?P<slot>\S+) +(?P<sensor_name>.+?)\s+(?P<state>Normal|Critical|Warning|Fan +Speed +\d+%)\s+(?P<reading>\d+\s*\S+\s*?\S*?)(\s*?(?P<threshold>na|\([\d|na,\s]+\)(\(Celsius\))?))?$')

        for line in out.splitlines():
            line = line.strip()
            # Number of Critical alarms:  0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['critical_larams'] = int(group['critic_larams'])
                continue

            # Number of Major alarms:     0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict['major_alarms'] = int(group['maj_alarms'])
                continue

            # Number of Minor alarms:     0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict['minor_alarms'] = int(group['min_alarms'])
                continue

            # Slot    Sensor       Current State       Reading          Threshold(Minor,Major,Critical,Shutdown)
            # ----    ------       -------------       -------          ---------------------------------------
            #  F0    Temp: Pop Die    Normal           43 Celsius
            #  P6    Temp: FC PWM1    Fan Speed 60%    26 Celsius
            #  P0    Iin              Normal           1 A
            #  P0    Vin              Normal           101 V AC
            #  R0    Temp: SCBY AIR   Normal           45 Celsius
            #  R0    3570DB2 _0: VO   Normal          1201 mV
            #  R1    V2: VMD          Normal           991 mV
            #  R0          3570MB2_0: VOU  Normal          1000 mV            na
            #  R0          Temp: Outlet_A  Normal          34   Celsius       (55 ,60 ,65 ,75 )(Celsius)
            #  R0          Temp: UADP_0_4  Normal          45   Celsius       (105,110,120,124)(Celsius)
            m = p4.match(line)
            if m:
                group = m.groupdict()
                sensor_name = group.pop('sensor_name')
                slot = group.pop('slot')

                threshold = group.pop('threshold') if group.get('threshold') else None
                if not threshold:
                    del group['threshold']

                fin_dict = ret_dict.setdefault('slot', {}).setdefault(slot, {}).\
                    setdefault('sensor', {}).setdefault(sensor_name, {})
                fin_dict.update({k: str(v) for k, v in group.items()})

                if threshold and threshold != 'na':

                    threshold_dict = fin_dict.setdefault('threshold', {})

                    if threshold.endswith('(Celsius)'):
                        threshold_dict['celsius'] = True
                        threshold = threshold[:-9]

                    threshold_names = ['minor', 'major','critical', 'shutdown']
                    for threshold_name, threshold_value in zip(threshold_names, threshold.strip('()').split(',')):
                        if 'na' not in threshold_value:
                            threshold_dict[threshold_name] = int(threshold_value.strip())


        return ret_dict



class ShowProcessesCpu(ShowProcessesCpuSorted):
    """Parser for show processes cpu
                  show processes cpu | include <WORD>"""

    cli_command = 'show processes cpu'

    def cli(self, key_word='', output=None):
        return(super().cli(key_word=key_word, output=output))


class ShowVersionRpSchema(MetaParser):
    """Schema for show version RP active [running|provisioned|installed]
                  show version RP standby [running|provisioned|installed]"""

    schema = {
        'rp': {
            Optional('active'): {
                'slot': {
                    Any(): {
                        'package': {
                            Any(): {
                                'version': str,
                                'status': str,
                                'file': str,
                                'built_time': str,
                                'built_by': str,
                                'file_sha1_checksum': str,
                            },
                        }
                    },
                }
            },
            Optional('standby'): {
                'slot': {
                    Any(): {
                        'package': {
                            Any(): {
                                'version': str,
                                'status': str,
                                'file': str,
                                'built_time': str,
                                'built_by': str,
                                'file_sha1_checksum': str,
                            },
                        }
                    },
                }
            }
        }
    }


class ShowVersionRp(ShowVersionRpSchema):
    """Parser for show version RP active [running|provisioned|installed]
                  show version RP standby [running|provisioned|installed]"""

    cli_command = ['show version RP {rp} {status}']
    exclude = ['total_enqs_bytes', 'total_enqs_packets']

    def cli(self, rp='active', status='running', output=None):

        if output is None:
            cmd = self.cli_command[0].format(rp=rp, status=status)
            out = self.device.execute(cmd)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}
        package_name = ''
        rp_slot = ''
        built_time = ''

        # Package: rpbase, version: 03.16.04a.S.155-3.S4a-ext, status: active
        # Package: Provisioning File, version: n/a, status: active
        p1 = re.compile(r'^Package: +(?P<package_name>[\w\d\s]+),'
                        ' +version: +(?P<version>[\w\d\.\-\/]+),'
                        ' +status: +(?P<status>[\w\/]+)$')

        #   File: consolidated:asr1000rp2-rpbase.03.16.04a.S.155-3.S4a-ext.pkg, on: RP0
        p2 = re.compile(r'^File: +consolidated:(?P<file>[\w\d\-\.]+),'
                        ' +on: +(?P<rp_slot>[\w\d\/]+)$')

        # Built: 2016-10-04_12.28, by: mcpre
        # Built: n/a, by: n/a
        p3 = re.compile(r'^Built: +(?P<built_time>[\w\d\:\.\_\/\-]+),'
                        ' +by: +(?P<built_by>[\w\d\/]+)$')

        #   File SHA1 checksum: 79e234871520fd480dc1128058160b4e2acee9f7
        p4 = re.compile(r'^File +SHA1 +checksum:'
                        ' +(?P<file_sha1_checksum>[\w\d]+)$')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                package_name = group['package_name']
                version = group['version']
                status = group['status']
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                file = group['file']
                rp_slot = group['rp_slot']

                # Safer, return empty dictionary instead of an error
                if not package_name:
                    return ret_dict
                elif 'rp' not in ret_dict:
                    ret_dict.setdefault('rp', {})

                if rp not in ret_dict['rp']:
                    ret_dict['rp'].setdefault(rp, {})
                if 'slot' not in ret_dict['rp'][rp]:
                    ret_dict['rp'][rp].setdefault('slot', {})
                if rp_slot not in ret_dict['rp'][rp]['slot']:
                    ret_dict['rp'][rp]['slot'].setdefault(rp_slot, {})
                if 'package' not in ret_dict['rp'][rp]['slot'][rp_slot]:
                    ret_dict['rp'][rp]['slot'][rp_slot].setdefault('package', {})

                ret_dict['rp'][rp]['slot'][rp_slot]['package'].setdefault(package_name, {})
                ret_dict['rp'][rp]['slot'][rp_slot]['package'][package_name]['version'] = version
                ret_dict['rp'][rp]['slot'][rp_slot]['package'][package_name]['status'] = status
                ret_dict['rp'][rp]['slot'][rp_slot]['package'][package_name]['file'] = file
                continue

            m = p3.match(line)
            if m:
                # Safer, return empty dictionary instead of an error
                if not package_name or not rp_slot:
                    return ret_dict

                group = m.groupdict()
                built_time = group['built_time']

                ret_dict['rp'][rp]['slot'][rp_slot]['package'][package_name]['built_time'] = built_time
                ret_dict['rp'][rp]['slot'][rp_slot]['package'][package_name]['built_by'] = group['built_by']
                continue

            m = p4.match(line)
            if m:
                # Safer, return empty dictionary instead of an error
                if not package_name or not rp_slot:
                    return ret_dict
                group = m.groupdict()
                ret_dict['rp'][rp]['slot'][rp_slot]['package'][package_name]['file_sha1_checksum'] = group['file_sha1_checksum']
                continue

        return ret_dict


class ShowPlatformPowerSchema(MetaParser):
    """Schema for show platform power"""
    schema = {
        'chassis': str,
        'total_load': int,
        'total_capacity': int,
        'load_capacity_percent': int,
        'power_capacity': int,
        'redundant_alc': int,
        'fan_alc': int,
        'fru_alc': int,
        'excess_power': int,
        'excess_capacity_percent': int,
        'redundancy_mode': str,
        'allocation_status': str,
        'slot': {
            Any(): {
                'type': str,
                'state': str,
                Optional('allocation'): float,
                Optional('capacity'): int,
                Optional('load'): int,
            },
        }
    }


class ShowPlatformPower(ShowPlatformPowerSchema):
    """Parser for show platform power"""
    cli_command = 'show platform power'

    def cli(self, output=None):

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # Chassis type: ASR1006-X
        p1 = re.compile(r'^\s*Chassis +type\: +(?P<chassis>[\w\-]+)')

        # Power Redundancy Mode: nplus1
        p2 = re.compile(r'^\s*Power +Redundancy +Mode\: +(?P<redundancy_mode>[\w]+)')

        # Power Allocation Status: Sufficient
        p3 = re.compile(r'^\s*Power +Allocation +Status\: +(?P<allocation_status>[\w]+)')

        # Slot      Type                State                 Allocation(W)
        # 0         ASR1000-SIP40       ok                    64
        #  0/0      SPA-8X1GE-V2        inserted              14
        #  0/1      SPA-1X10GE-L-V2     inserted              17.40
        p4 = re.compile(r'^\s*(?P<slot>[\w\/]+) +(?P<type>[\w-]+) '
                        '+(?P<state>\w+(?:\, \w+)?) +(?P<allocation>[\d.]+)$')

        # Slot      Type                State                 Capacity (W) Load (W)
        # P0        ASR1000X-AC-1100W   ok                    1100         132
        p5 = re.compile(r'^\s*(?P<slot>[\w\/]+) +(?P<type>[\w\-]+) '
                        '+(?P<state>\w+(?:\, \w+)?) +(?P<capacity>[\d.]+) +(?P<load>[\d.]+)')

        # Total load: 696 W, total capacity: 4400 W. Load / Capacity is 15%
        p6 = re.compile(r'^\s*Total +load\: +(?P<total_load>\d+) +W\, +total +capacity\: +(?P<total_capacity>\d+) +W\.'
                        ' +Load +\/ +Capacity +is +(?P<load_capacity_percent>\d+)\%$')

        # Power capacity:       4400 W
        p7 = re.compile(r'^\s*Power +capacity\: +(?P<power_capacity>\d+) +W$')

        # Redundant allocation: 0 W
        p8 = re.compile(r'^\s*Redundant +allocation\: +(?P<redundant_alc>\d+) +W$')

        # Fan allocation:       250 W
        p9 = re.compile(r'^\s*Fan +allocation\: +(?P<fan_alc>\d+) +W$')

        # FRU allocation:       949 W
        p10 = re.compile(r'^\s*FRU +allocation\: +(?P<fru_alc>\d+) +W$')

        # Excess Power in Reserve:   3201 W
        p11 = re.compile(r'^\s*Excess +Power +in +Reserve\: +(?P<excess_power>\d+) +W$')

        # Excess / (Capacity - Redundant) is 72%
        p12 = re.compile(r'^\s*Excess +\/ +\(Capacity - Redundant\) +is +(?P<excess_capacity_percent>\d+)\%$')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                ret_dict['chassis'] = m.groupdict()['chassis']
                continue

            m = p2.match(line)
            if m:
                ret_dict['redundancy_mode'] = m.groupdict()['redundancy_mode']
                continue

            m = p3.match(line)
            if m:
                ret_dict['allocation_status'] = m.groupdict()['allocation_status']

            m = p4.match(line)
            if m:
                slot = m.groupdict()['slot']
                t = m.groupdict()['type']
                state = m.groupdict()['state']
                allocation = float(m.groupdict()['allocation'])
                slot_dict = ret_dict.setdefault('slot', {}).setdefault(slot, {})
                slot_dict.update({"type": t})
                slot_dict.update({"state": state})
                slot_dict.update({"allocation": allocation})
                continue

            m = p5.match(line)
            if m:
                slot = m.groupdict()['slot']
                t = m.groupdict()['type']
                state = m.groupdict()['state']
                capacity = int(m.groupdict()['capacity'])
                load = int(m.groupdict()['load'])
                slot_dict = ret_dict.setdefault('slot', {}).setdefault(slot, {})
                slot_dict.update({"type": t})
                slot_dict.update({"state": state})
                slot_dict.update({"capacity": capacity})
                slot_dict.update({"load": load})
                continue

            m = p6.match(line)
            if m:
                ret_dict['total_load'] = int(m.groupdict()['total_load'])
                ret_dict['total_capacity'] = int(m.groupdict()['total_capacity'])
                ret_dict['load_capacity_percent'] = int(m.groupdict()['load_capacity_percent'])
                continue

            m = p7.match(line)
            if m:
                ret_dict['power_capacity'] = int(m.groupdict()['power_capacity'])
                continue

            m = p8.match(line)
            if m:
                ret_dict['redundant_alc'] = int(m.groupdict()['redundant_alc'])
                continue

            m = p9.match(line)
            if m:
                ret_dict['fan_alc'] = int(m.groupdict()['fan_alc'])
                continue

            m = p10.match(line)
            if m:
                ret_dict['fru_alc'] = int(m.groupdict()['fru_alc'])
                continue

            m = p11.match(line)
            if m:
                ret_dict['excess_power'] = int(m.groupdict()['excess_power'])
                continue

            m = p12.match(line)
            if m:
                ret_dict['excess_capacity_percent'] = int(m.groupdict()['excess_capacity_percent'])
                continue

        return ret_dict


class ShowProcessesCpuHistorySchema(MetaParser):
    """Schema for show processes cpu history"""

    schema = {
        '60s': {
            Any(): {
                'maximum': int,
                Optional('average'): int,
            },
        },
        '60m': {
            Any(): {
                'maximum': int,
                Optional('average'): int,
            },
        },
        '72h': {
            Any(): {
                'maximum': int,
                Optional('average'): int,
            },
        },
    }


class ShowProcessesCpuHistory(ShowProcessesCpuHistorySchema):
    """Parser for show processes cpu history"""

    cli_command = 'show processes cpu history'
    exclude = ['maximum', 'average']

    def cli(self, output=None):

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        #           888886666611111                    11111
        # 7777755555996510966664444466666333335555544444666667777777777
        p1 = re.compile(r'^ *\d+( +\d+)* *$')

        #          0    5    0    5    0    5    0    5    0    5    0
        p2 = re.compile(r'^ *0( +5 +0){5,6} *$')

        # 80     * **#*#**   * *       *
        # 70  *  * **#*#**   * *       *           *
        p3 = re.compile(r'^ *(?P<num>[\d]+)(?P<line>.*#.*$)')

        # CPU% per second (last 60 seconds)
        p4 = re.compile(r'^ *CPU%.*$')

        # initialize max list & average list & return dictionary
        max_list = []
        average_list = []
        ret_dict = {}

        for line in out.splitlines():
            strip_line = line[6:]
            m = p1.match(strip_line)
            if m:
                max_list.append(strip_line)
                continue

            m1 = p3.match(line)
            m2 = p4.match(line)
            if m1 or m2:
                average_list.append(line)
                continue

        # parser max value
        tmp = [''] * 72
        count = 0
        for line in max_list:
            m = p2.match(line)
            if not m:
                for i, v in enumerate(line):
                    if v == ' ':
                        pass
                    else:
                        tmp[i] += v
            else:
                if count == 0:
                    sub_dict = ret_dict.setdefault('60s', {})
                    for i in range(60):
                        sub_dict.setdefault(i + 1, {}).update({'maximum': int(tmp[i]) if tmp[i] != '' else 0})

                elif count == 1:
                    sub_dict = ret_dict.setdefault('60m', {})
                    for i in range(60):
                        sub_dict.setdefault(i + 1, {}).update({'maximum': int(tmp[i]) if tmp[i] != '' else 0})

                else:
                    sub_dict = ret_dict.setdefault('72h', {})
                    for i in range(72):
                        sub_dict.setdefault(i + 1, {}).update({'maximum': int(tmp[i]) if tmp[i] != '' else 0})
                tmp = [''] * 72
                count += 1

        # parser average value
        count = 0
        for line in average_list:
            m = p3.match(line)
            if count == 0:
                sub_dict = ret_dict.setdefault('60s', {})
            elif count == 1:
                sub_dict = ret_dict.setdefault('60m', {})
            else:
                sub_dict = ret_dict.setdefault('72h', {})

            if m:
                num = int(m.groupdict()['num'])
                line = m.groupdict()['line']
                for i, char in enumerate(line):
                    if char == '#':
                        t = sub_dict.setdefault(i, {})
                        if 'average' not in t:
                            t.update({'average': num})

            else:
                for value in sub_dict.values():
                    if 'average' not in value:
                        value.update({'average': 0})

                count += 1

        return ret_dict


class ShowProcessesMemorySchema(MetaParser):
    schema = {
        Optional('processor_pool'): {
            'total': int,
            'used': int,
            'free': int,
        },
        Optional('reserve_p_pool'): {
            'total': int,
            'used': int,
            'free': int,
        },
        Optional('lsmi_io_pool'): {
            'total': int,
            'used': int,
            'free': int,
        },
        Optional('pid'): {
            Any(): {
                'index': {
                    Any(): {
                        'pid': int,
                        'tty': int,
                        'allocated': int,
                        'freed': int,
                        'holding': int,
                        'getbufs': int,
                        'retbufs': int,
                        'process': str,
                    }
                }
            }
        }
    }


class ShowProcessesMemory(ShowProcessesMemorySchema):
    cli_command = [
        'show processes memory',
        'show processes memory | include {include}',
        'show processes memory | exclude {exclude}',
        'show processes memory | section {section}'
    ]

    def cli(self, include=None, exclude=None, section=None, output=None):

        ret_dict = {}
        pid_index = {}

        if not output:
            if include:
                cmd = self.cli_command[1].format(include=include)
            elif exclude:
                cmd = self.cli_command[2].format(exclude=exclude)
            elif section:
                cmd = self.cli_command[3].format(section=section)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        # Processor Pool Total: 10147887840 Used:  485435960 Free: 9662451880
        p1 = re.compile(r'^Processor +Pool +Total: +(?P<total>\d+) +'
                        r'Used: +(?P<used>\d+) +Free: +(?P<free>\d+)$')

        # reserve P Pool Total:     102404 Used:         88 Free:     102316
        p2 = re.compile(r'^reserve +P +Pool +Total: +(?P<total>\d+) +'
                        r'Used: +(?P<used>\d+) +Free: +(?P<free>\d+)$')

        # lsmpi_io Pool Total:    6295128 Used:    6294296 Free:        832
        p3 = re.compile(r'^lsmpi_io +Pool +Total: +(?P<total>\d+) +'
                        r'Used: +(?P<used>\d+) +Free: +(?P<free>\d+)$')

        # 0   0  678985440  347855496  304892096        428    2134314 *Init*
        # 1   0    3415536     879912    2565568          0          0 Chunk Manager
        p4 = re.compile(r'^(?P<pid>\d+) +(?P<tty>\d+) +(?P<allocated>\d+) +'
                        r'(?P<freed>\d+) +(?P<holding>\d+) +(?P<getbufs>\d+) +'
                        r'(?P<retbufs>\d+) +(?P<process>[\S ]+)$')

        for line in out.splitlines():
            line = line.strip()

            # Processor Pool Total: 10147887840 Used:  485435960 Free: 9662451880
            m = p1.match(line)
            if m:
                group = m.groupdict()
                processor_pool_dict = ret_dict.setdefault('processor_pool', {})
                processor_pool_dict.update({k: int(v) for k, v in group.items() if v is not None})
                continue

            # reserve P Pool Total:     102404 Used:         88 Free:     102316
            m = p2.match(line)
            if m:
                group = m.groupdict()
                processor_pool_dict = ret_dict.setdefault('reserve_p_pool', {})
                processor_pool_dict.update({k: int(v) for k, v in group.items() if v is not None})
                continue

            # lsmpi_io Pool Total:    6295128 Used:    6294296 Free:        832
            m = p3.match(line)
            if m:
                group = m.groupdict()
                processor_pool_dict = ret_dict.setdefault('lsmi_io_pool', {})
                processor_pool_dict.update({k: int(v) for k, v in group.items() if v is not None})
                continue

            # 0   0  678985440  347855496  304892096        428    2134314 *Init*
            # 1   0    3415536     879912    2565568          0          0 Chunk Manager
            m = p4.match(line)
            if m:
                group = m.groupdict()
                pid = int(group['pid'])
                index = pid_index.get(pid, 0) + 1
                pid_dict = ret_dict.setdefault('pid', {}). \
                    setdefault(pid, {}). \
                    setdefault('index', {}). \
                    setdefault(index, {})
                pid_index.update({pid: index})
                pid_dict.update({k: int(v) if v.isdigit() else v for k, v in group.items() if v is not None})
                continue

        return ret_dict

class ShowProcessesMemorySortedSchema(MetaParser):
    schema = {
        'processor_pool': {
            'total': int,
            'used': int,
            'free': int,
        },
        'reserve_p_pool': {
            'total': int,
            'used': int,
            'free': int,
        },
        'lsmi_io_pool': {
            'total': int,
            'used': int,
            'free': int,
        },
        'per_process_memory': {
            Any(): {
                'pid': int,
                'tty': int,
                'allocated': int,
                'freed': int,
                'holding': int,
                'getbufs': int,
                'retbufs': int,
            }
        }
    }


class ShowProcessesMemorySorted(ShowProcessesMemorySortedSchema):
    cli_command = 'show processes memory sorted'

    def cli(self, include=None, sorted=None, output=None):

        ret_dict = {}
        pid_index = {}

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        if out:
            per_process_memory_dict = ret_dict.setdefault('per_process_memory', OrderedDict())

        # Processor Pool Total: 10147887840 Used:  485435960 Free: 9662451880
        p1 = re.compile(r'^Processor +Pool +Total: +(?P<total>\d+) +'
                        r'Used: +(?P<used>\d+) +Free: +(?P<free>\d+)$')

        # reserve P Pool Total:     102404 Used:         88 Free:     102316
        p2 = re.compile(r'^reserve +P +Pool +Total: +(?P<total>\d+) +'
                        r'Used: +(?P<used>\d+) +Free: +(?P<free>\d+)$')

        # lsmpi_io Pool Total:    6295128 Used:    6294296 Free:        832
        p3 = re.compile(r'^lsmpi_io +Pool +Total: +(?P<total>\d+) +'
                        r'Used: +(?P<used>\d+) +Free: +(?P<free>\d+)$')

        # 0   0  678985440  347855496  304892096        428    2134314 *Init*
        # 1   0    3415536     879912    2565568          0          0 Chunk Manager
        p4 = re.compile(r'^(?P<pid>\d+) +(?P<tty>\d+) +(?P<allocated>\d+) +'
                        r'(?P<freed>\d+) +(?P<holding>\d+) +(?P<getbufs>\d+) +'
                        r'(?P<retbufs>\d+) +(?P<process>[\S ]+)$')

        for line in out.splitlines():
            line = line.strip()
            # Processor Pool Total: 10147887840 Used:  485435960 Free: 9662451880
            m = p1.match(line)
            if m:
                group = m.groupdict()
                processor_pool_dict = ret_dict.setdefault('processor_pool', {})
                processor_pool_dict.update({k: int(v) for k, v in group.items() if v is not None})
                continue

            # reserve P Pool Total:     102404 Used:         88 Free:     102316
            m = p2.match(line)
            if m:
                group = m.groupdict()
                processor_pool_dict = ret_dict.setdefault('reserve_p_pool', {})
                processor_pool_dict.update({k: int(v) for k, v in group.items() if v is not None})
                continue

            # lsmpi_io Pool Total:    6295128 Used:    6294296 Free:        832
            m = p3.match(line)
            if m:
                group = m.groupdict()
                processor_pool_dict = ret_dict.setdefault('lsmi_io_pool', {})
                processor_pool_dict.update({k: int(v) for k, v in group.items() if v is not None})
                continue

            # 0   0  678985440  347855496  304892096        428    2134314 *Init*
            # 1   0    3415536     879912    2565568          0          0 Chunk Manager
            m = p4.match(line)
            if m:
                group = m.groupdict()
                process_name = str(group['process'])
                one_process_dict = per_process_memory_dict.setdefault(process_name, {})
                one_process_dict['pid'] = int(group['pid'])
                one_process_dict['tty'] = int(group['tty'])
                one_process_dict['allocated'] = int(group['allocated'])
                one_process_dict['freed'] = int(group['freed'])
                one_process_dict['holding'] = int(group['holding'])
                one_process_dict['getbufs'] = int(group['getbufs'])
                one_process_dict['retbufs'] = int(group['retbufs'])
                continue

        return ret_dict

class ShowPlatformIntegritySchema(MetaParser):
    schema = {
        'platform': str,
        'boot': {
            Any(): {
                'version': str,
                'hash': str,
            },
            'loader': {
                'version': str,
                'hash': str,
            },
        },
        'os_version': str,
        'os_hashes': {
            Any(): str,
        },
        Optional('signature_version'): int,
        Optional('signature'): str,
    }

class ShowPlatformIntegrity(ShowPlatformIntegritySchema):
    # cli_command = 'show platform integrity'
    cli_command = [
        'show platform integrity',
        'show platform integrity sign nonce {nonce}',
        'show platform integrity {signature}'
    ]

    def cli(self, signature=None, nonce=None, output=None):
        if not output:
            if nonce:
                output = self.device.execute(self.cli_command[1].format(nonce=nonce))
            elif signature:
                output = self.device.execute(self.cli_command[2].format(signature=signature))
            else:
                output = self.device.execute(self.cli_command[0])

        ret_dict = {}

        # Platform: C9300-24U
        p1 = re.compile(r'^Platform: +(?P<platform>\S+)$')
        # Boot 0 Version: F01144R16.216e68ad62019-02-13
        p2 = re.compile(r'^Boot +(?P<boot>\d+) +Version: +(?P<version>\S+)$')
        # Boot 0 Hash: 523DD459C650AF0F5AB5396060605E412C1BE99AF51F4FA88AD26049612921FF
        p3 = re.compile(r'^Boot +(?P<boot>\d+) +Hash: +(?P<hash>\S+)$')
        # Boot Loader Version: System Bootstrap, Version 16.10.1r[FC2], DEVELOPMENT SOFTWARE
        p4 = re.compile(r'^Boot +Loader +Version: +(?P<boot_loader_version>[\S ]+)$')
        # Boot Loader Hash: 523DD459C650AF0F5AB5396060605E412C1BE99AF51F4FA88AD26049612921FF
        p5 = re.compile(r'^Boot +Loader +Hash: *(?P<hash>\S+)$')
        # 51CE6FB9AE606330810EBFFE99D71D56640FD48F780EDE0C19FB5A75E31EF2192A58A196D18B244ADF67D18BF6B3AA6A16229C66DCC03D8A900753760B252C57
        p6 = re.compile(r'^(?P<hash>\S+)$')
        # OS Version: 2019-07-11_16.25_mzafar
        p7 = re.compile(r'^OS +Version: +(?P<os_version>\S+)$')
        # OS Hashes:
        p8 = re.compile(r'^OS +Hashes:$')
        # PCR0: BB33E3FE338B82635B1BD3F1401CF442ACC9BB12A405A424FBE0A5776569884E
        p9 = re.compile(r'^(?P<hash_key>\S+): +(?P<hash_val>\S+)$')
        # cat9k_iosxe.2019-07-11_16.25_mzafar.SSA.bin:
        p10 = re.compile(r'^(?P<os_hash>\S+):$')
        # Signature version: 1
        p11 = re.compile(r'^Signature version: +(?P<signature_version>\S+)$')
        # Signature:
        p12 = re.compile(r'^Signature:$')

        for line in output.splitlines():
            line = line.strip()

            # Platform: C9300-24U
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'platform': group['platform']})
                continue

            # Boot 0 Version: F01144R16.216e68ad62019-02-13
            m = p2.match(line)
            if m:
                group = m.groupdict()
                boot = int(group['boot'])
                version = group['version']
                boot_dict = ret_dict.setdefault('boot', {}). \
                    setdefault(boot, {})
                boot_dict.update({'version': version})
                continue

            # Boot 0 Hash: 523DD459C650AF0F5AB5396060605E412C1BE99AF51F4FA88AD26049612921FF
            m = p3.match(line)
            if m:
                group = m.groupdict()
                boot = int(group['boot'])
                hash_val = group['hash']
                boot_dict = ret_dict.setdefault('boot', {}). \
                    setdefault(boot, {})
                boot_dict.update({'hash': hash_val})
                continue

            # Boot Loader Version: System Bootstrap, Version 16.10.1r[FC2], DEVELOPMENT SOFTWARE
            m = p4.match(line)
            if m:
                group = m.groupdict()
                boot_loader_dict = ret_dict.setdefault('boot', {}). \
                    setdefault('loader', {})
                boot_loader_version = group['boot_loader_version']
                boot_loader_dict.update({'version': boot_loader_version})
                continue

            # Boot Loader Hash: 523DD459C650AF0F5AB5396060605E412C1BE99AF51F4FA88AD26049612921FF
            m = p5.match(line)
            if m:
                group = m.groupdict()
                hash_val = group['hash']
                hash_type = 'boot_loader'
                boot_loader_dict = ret_dict.setdefault('boot', {}). \
                    setdefault('loader', {})
                boot_loader_hash = ret_dict.get('boot_loader_hash', '')
                boot_loader_hash = '{}{}'.format(boot_loader_hash, hash_val)
                boot_loader_dict.update({'hash': boot_loader_hash})
                continue

            # OS Version: 2019-07-11_16.25_mzafar
            m = p7.match(line)
            if m:
                group = m.groupdict()
                os_version = group['os_version']
                ret_dict.update({'os_version': os_version})
                continue

            # OS Hashes:
            m = p8.match(line)
            if m:
                hash_type = 'os_hashes'
                continue

            # Signature:
            m = p12.match(line)
            if m:
                hash_type = 'signature'
                continue

            # PCR0: BB33E3FE338B82635B1BD3F1401CF442ACC9BB12A405A424FBE0A5776569884E
            m = p9.match(line)
            if m:
                group = m.groupdict()
                hash_type = 'os_hashes'
                group = m.groupdict()
                os_hash = group['hash_key']
                hash_val = group['hash_val']
                os_hash_dict = ret_dict.setdefault('os_hashes', {})
                os_hash_dict.update({os_hash: hash_val})
                continue

            # cat9k_iosxe.2019-07-11_16.25_mzafar.SSA.bin:
            m = p10.match(line)
            if m:
                hash_type = 'os_hashes'
                group = m.groupdict()
                os_hash = group['os_hash']
                os_hash_dict = ret_dict.setdefault('os_hashes', {})
                os_hash_dict.update({os_hash: ''})
                continue

            # Signature version: 1
            m = p11.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'signature_version': int(group['signature_version'])})
                continue

            # 51CE6FB9AE606330810EBFFE99D71D56640FD48F780EDE0C19FB5A75E31EF2192A58A196D18B244ADF67D18BF6B3AA6A16229C66DCC03D8A900753760B252C57
            m = p6.match(line)
            if m:
                group = m.groupdict()
                hash_val = group['hash']
                if hash_type == 'boot_loader':
                    boot_loader_hash = boot_loader_dict.get('boot_loader_hash', '')
                    boot_loader_hash = '{}{}'.format(boot_loader_hash, hash_val)
                    boot_loader_dict.update({'hash': boot_loader_hash})
                elif hash_type == 'os_hash':
                    os_hash_val = os_hash_dict.get(os_hash, '')
                    os_hash_val = '{}{}'.format(os_hash_val, hash_val)
                    os_hash_dict.update({'os_hash': os_hash_val})
                elif hash_type == 'signature':
                    ret_dict.update({'signature': hash_val})
                continue

        return ret_dict

    def yang(self, nonce=None, output=None):
        if not output:
            # xpath is the same regardless of if nonce is passed or not
            output = self.device.get(filter=('xpath', '/boot-integrity-oper-data')).data_xml

        log.info(minidom.parseString(output).toprettyxml())

        root = ET.fromstring(output)
        boot_integrity_oper_data = Common.retrieve_xml_child(root=root, key='boot-integrity-oper-data')
        boot_integrity = Common.retrieve_xml_child(root=boot_integrity_oper_data, key='boot-integrity')
        ret_dict = {}
        boot_index = 0
        name = None
        for child in boot_integrity:
            if child.tag.endswith('platform'):
                ret_dict.update({'platform': child.text})
            elif child.tag.endswith('os-version'):
                ret_dict.update({'os_version': child.text})
            elif child.tag.endswith('boot-ver'):
                boot_dict = ret_dict.setdefault('boot', {}). \
                    setdefault(boot_index, {})
                boot_dict.update({'version': child.text})
                boot_index+=1
            elif child.tag.endswith('boot-hash'):
                boot_dict.update({'hash': child.text})
            elif child.tag.endswith('boot-loader-hash'):
                boot_loader_dict = ret_dict.setdefault('boot', {}). \
                    setdefault('loader', {})
                boot_loader_dict.update({'hash': child.text})
            elif child.tag.endswith('boot-loader-ver'):
                boot_loader_dict = ret_dict.setdefault('boot', {}). \
                    setdefault('loader', {})
                boot_loader_dict.update({'version': child.text})
            elif child.tag.endswith('package-signature') or child.tag.endswith('package-integrity'):
                for sub_child in child:
                    os_hashes = ret_dict.setdefault('os_hashes', {})
                    if sub_child.tag.endswith('name'):
                        name = sub_child.text
                    elif name and sub_child.tag.endswith('hash'):
                        os_hashes.update({name: sub_child.text})
                        name = None
            elif child.tag.endswith('pcr-register'):
                for sub_child in child:
                    os_hashes = ret_dict.setdefault('os_hashes', {})
                    if sub_child.tag.endswith('index'):
                        name = 'PCR{}'.format(sub_child.text)
                    elif name and sub_child.tag.endswith('pcr-content'):
                        os_hashes.update({name: sub_child.text})
                        name = None
            elif child.tag.endswith('sig-version'):
                ret_dict.update({'signature_version': int(child.text)})
            elif child.tag.endswith('signature'):
                ret_dict.update({'signature': child.text})
        return ret_dict


class ShowPlatformTcamUtilizationSchema(MetaParser):
    """Schema for show platform hardware fed sw active fwd-asic resource tcam utilization """
    schema = {
        'asic': {
            Any(): {
                'table': {
                    Any(): {
                        'subtype': {
                            Any(): {
                                'dir': {
                                    Any(): {
                                        'max': str,
                                        'used': str,
                                        'used_percent': str,
                                        'v4': str,
                                        'v6': str,
                                        'mpls': str,
                                        'other': str,
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }


class ShowPlatformTcamUtilization(ShowPlatformTcamUtilizationSchema):
    """Parser for show platform hardware fed sw active fwd-asic resource tcam utilization """

    cli_command = ['show platform hardware fed {switch} {mode} fwd-asic resource tcam utilization',
                   'show platform hardware fed active fwd-asic resource tcam utilization',
                   'show platform hardware fed switch {mode} fwd-asic resource tcam utilization']

    def cli(self, output=None, switch='', mode=None):
        if output is None:
            if switch and mode:
                cmd = self.cli_command[0].format(switch=switch, mode=mode)
            elif mode:
                cmd = self.cli_command[2].format(mode=mode)
            else:
                cmd = self.cli_command[1]
            output = self.device.execute(cmd)

        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern
        # CAM Utilization for ASIC  [0]
        p1 = re.compile(r'CAM +Utilization +for +ASIC  +\[+(?P<asic>(\d+))\]$')

        #CTS Cell Matrix/VPN
        #Label                  EM           O       16384        0    0.00%        0        0        0        0
        #CTS Cell Matrix/VPN
        #Label                  TCAM         O        1024        1    0.10%        0        0        0        1
        # Mac Address Table      EM           I       16384       44    0.27%        0        0        0       44
        # Mac Address Table      TCAM         I        1024       21    2.05%        0        0        0       21
        p2 = re.compile(r'(?P<table>.*(\S+)) +(?P<subtype>\S+) +(?P<dir>\S+) +(?P<max>\d+) +(?P<used>\d+) +(?P<used_percent>\S+\%) +(?P<v4>\d+) +(?P<v6>\d+) +(?P<mpls>\d+) +(?P<other>\d+)$')


        for line in output.splitlines():
            line = line.strip()

            # CAM Utilization for ASIC  [0]
            m = p1.match(line)
            if m:
                group = m.groupdict()
                asic = group['asic']
                asic_dict = ret_dict.setdefault('asic', {}).setdefault(asic, {})
                continue

            #CTS Cell Matrix/VPN
            #Label                  EM           O       16384        0    0.00%        0        0        0        0
            #CTS Cell Matrix/VPN
            #Label                  TCAM         O        1024        1    0.10%        0        0        0        1
            # Mac Address Table      EM           I       16384       44    0.27%        0        0        0       44
            # Mac Address Table      TCAM         I        1024       21    2.05%        0        0        0       21
            m = p2.match(line)
            if m:
                group = m.groupdict()
                table_ = group.pop('table')
                if table_ == 'Label':
                    table_ = 'CTS Cell Matrix/VPN Label'
                subtype_ = group.pop('subtype')
                dir_ = group.pop('dir')
                dir_dict = asic_dict.setdefault('table', {}). \
                            setdefault(table_, {}). \
                            setdefault('subtype', {}). \
                            setdefault(subtype_, {}). \
                            setdefault('dir', {}). \
                            setdefault(dir_, {})
                dir_dict.update({k: v for k, v in group.items()})
                continue

        return ret_dict

# =======================================================================
# Schema for 'show platform resources'
# =======================================================================
class ShowPlatformResourcesSchema(MetaParser):
    schema = {
        Optional('rp'): {
            Any():  {

            'state': str,
            'role': str,
            'control_processer': {
                'usage_perc': float,
                'max_perc': int,
                'warning_perc': int,
                'critical_perc': int,
                'state': str,
                'dram': {
                    'usage_mb': int,
                    'usage_perc': int,
                    'max_mb': int,
                    'warning_perc': int,
                    'critical_perc': int,
                    'state': str
                },
                Optional('bootflash'): {
                'usage_mb': int,
                'usage_perc': int,
                'max_mb': int,
                'warning_perc': int,
                'critical_perc': int,
                'state': str
                },
                Optional('harddisk'): {
                'usage_mb': int,
                'usage_perc': int,
                'max_mb': int,
                'warning_perc': int,
                'critical_perc': int,
                'state': str
                }
            }
            }
        },
        Optional('esp'): {
            Any(): {
                'state': str,
                'role': str,
                Optional('control_processer'): {
                    'usage_perc': float,
                    'max_perc': int,
                    'warning_perc': int,
                    'critical_perc': int,
                    'state': str,
                    'dram': {
                        'usage_mb': int,
                        'usage_perc': int,
                        'max_mb': int,
                        'warning_perc': int,
                        'critical_perc': int,
                        'state': str
                    }
                },
                'qfp': {
                    'state': str,
                    Optional('tcam'): {
                        'usage_cells': int,
                        'usage_perc': int,
                        'max_cells': int,
                        'warning_perc': int,
                        'critical_perc': int,
                        'state': 'H'
                    },
                    'dram': {
                        'usage_kb': int,
                        'usage_perc': int,
                        'max_kb': int,
                        'warning_perc': int,
                        'critical_perc': int,
                        'state': str
                    },
                    'iram': {
                        'usage_kb': int,
                        'usage_perc': int,
                        'max_kb': int,
                        'warning_perc': int,
                        'critical_perc': int,
                        'state': str
                    },
                    'cpu_utilization': {
                        'usage_perc': float,
                        'max_perc': int,
                        'warning_perc': int,
                        'state': str
                    },
                    Optional(Any()): {
                        'usage_kb': int,
                        'usage_perc': int,
                        'max_kb': int,
                        'warning_perc': int,
                        'critical_perc': int,
                        'state': str
                    }
                }
            }
        },
        Optional('sip'): {
            Any(): {
                'state': str,
                'control_processer': {
                    'usage_perc': float,
                    'max_perc': int,
                    'warning_perc': int,
                    'critical_perc': int,
                    'state': str,
                    'dram': {
                        'usage_mb': int,
                        'usage_perc': int,
                        'max_mb': int,
                        'warning_perc': int,
                        'critical_perc': int,
                        'state': str
                    }
                }
            }
        },
        Optional('control_processer'): {
                'usage_perc': float,
                'max_perc': int,
                'warning_perc': int,
                'critical_perc': int,
                'state': str,
                'dram': {
                    'usage_mb': int,
                    'usage_perc': int,
                    'max_mb': int,
                    'warning_perc': int,
                    'critical_perc': int,
                    'state': str
                },
                Optional('tmpfs'):{
                    'usage_mb': int,
                    'usage_perc': int,
                    'max_mb': int,
                    'warning_perc': int,
                    'critical_perc': int,
                    'state': str
                }
        }
    }

# =======================================================================
# Parser for 'show platform resources'
# =======================================================================
class ShowPlatformResources(ShowPlatformResourcesSchema):

    cli_command = ['show platform resources']


    def cli(self, output=None):

        # if the user does not provide output to the parser
        # we need to get it from the device
        if not output:
            output = self.device.execute(self.cli_command[0])


        #RP0 (ok, active)                                                                               H
        #RP1 (ok, standby)                                                                               H
        #ESP0(ok, active)                                                                               H
        #ESP1(ok, standby)                                                                               H
        p1 = re.compile(r'^(?P<type>RP|ESP)(?P<key>[0-9]) ?\((?P<status>\S+)\, +(?P<role>\S+)\) +(?P<state>\S)$')

        #SIP0                                                                                           H
        p2 = re.compile(r'^SIP(?P<key>[0-9]) +(?P<state>\S)$')

        # Control Processor       0.51%                 100%            80%             90%             H
        p3 = re.compile(r'^Control Processor +(?P<usage>(\d*\.?\d+))\S+ +(?P<max>\d+)\S+ +(?P<warning>\d+)\S+ +(?P<critical>\d+)\S+ +(?P<state>\S)$')

        #QFP                                                                                           H
        p4 = re.compile(r'^QFP +(?P<state>\S)$')

        #CPU Utilization        0.00%                 100%            90%             95%             H
        p5 = re.compile(r'^(?P<resource>[\S\s]+\S) +(?P<usage>(\d*\.?\d+))\S+ +(?P<max>\d+)\S+ +(?P<warning>\d+)\S+ +(?P<critical>\d+)\S+ +(?P<state>\S)$')

        # TCAM                   16cells(0%)           1048576cells    65%             85%             H
        # DRAM                   238906KB(5%)          4194304KB       85%             95%             H
        # IRAM                   13014KB(9%)           131072KB        85%             95%             H
        p6 = re.compile(r'^(?P<resource>[\s\S]+\S) +(?P<use_val>(\d*\.?\d+))(?P<type>\S+)\((?P<val>\d+)\%\) +(?P<max>\d+)(?P<max_type>\S+) +(?P<warning>\d+)\S+ +(?P<critical>\d+)\S+ +(?P<state>\S)$')


        ret_dict = {}
        feature_dict = ret_dict
        for line in output.splitlines():
            line = line.strip()

            #RP1 (ok, standby)                                                                               H
            #ESP0 (ok, active)                                                                               H
            m = p1.match(line)

            if m:
                groups = m.groupdict()
                type_ = groups['type'].lower()

                feature_dict = ret_dict.setdefault(type_, {}).setdefault(groups['key'], {})

                feature_dict.update(({'state': (groups['state'])}))
                feature_dict.update(({'role': (groups['role'])}))

                last_dict_ptr1 = feature_dict
                continue

            #SIP0                                                                                           H
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                feature_dict = ret_dict.setdefault('sip', {}).setdefault(groups['key'], {})
                feature_dict.update(({'state': (groups['state'])}))
                last_dict_ptr1 = feature_dict
                continue

            # Control Processor       0.51%                 100%            80%             90%             H
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                feature_dict = feature_dict.setdefault('control_processer', {})
                feature_dict.update({'usage_perc': float(groups['usage'])})
                feature_dict.update({'max_perc': int(groups['max'])})
                feature_dict.update({'warning_perc': int(groups['warning'])})
                feature_dict.update({'critical_perc': int(groups['critical'])})
                feature_dict.update({'state': (groups['state'])})
                last_dict_ptr = feature_dict
                continue

            #QFP                                                                                           H
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                feature_dict = last_dict_ptr1
                feature_dict = feature_dict.setdefault('qfp', {})
                feature_dict.update({'state': (groups['state'])})
                last_dict_ptr = feature_dict
                continue

            #CPU Utilization        0.00%                 100%            90%             95%             H
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                feature_dict = last_dict_ptr
                res1 = groups['resource'].replace(' ','_').replace('(','').replace(')','').lower()
                feature_dict = feature_dict.setdefault(res1,{})
                feature_dict.update({'usage_' + groups['type'].lower(): int(groups['use_val'])})
                feature_dict.update({'usage_perc': int(groups['val'])})
                feature_dict.update({'max_' + groups['max_type'].lower(): int(groups['max'])})
                feature_dict.update({'warning_perc': int(groups['warning'])})
                feature_dict.update({'critical_perc': int(groups['critical'])})
                feature_dict.update({'state': (groups['state'])})
                continue

            #TCAM                   16cells(0%)           1048576cells    65%             85%             H
            # DRAM                   238906KB(5%)          4194304KB       85%             95%             H
            # IRAM                   13014KB(9%)           131072KB        85%             95%             H
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                feature_dict = last_dict_ptr
                res1 = groups['resource'].replace(' ','_').replace('(','').replace(')','').lower()
                feature_dict = feature_dict.setdefault(res1,{})
                feature_dict.update({'usage_perc': float(groups['usage'])})
                feature_dict.update({'max_perc': int(groups['max'])})
                feature_dict.update({'warning_perc': int(groups['warning'])})
                feature_dict.update({'state': (groups['state'])})
                continue

        return(ret_dict)


class ShowPlatformSudiCertificateNonceSchema(MetaParser):
    """Schema for show platform sudi certificate sign nonce 123"""

    schema = {
        'certificates':{
            int: str,
        },
        Optional('signature'):str,
        Optional('signature_version'):int,
    }


class ShowPlatformSudiCertificateNonce(ShowPlatformSudiCertificateNonceSchema):
    """Parser for show platform  sudi  certificate sign nonce 123"""

    cli_command = ['show platform sudi certificate sign nonce {signature}','show platform sudi certificate']

    def cli(self,signature='', output=None):
        if output is None:
            # Build the command
            if signature:
                output = self.device.execute(self.cli_command[0].format(signature=signature))
            else:
                output = self.device.execute(self.cli_command[1])

        certificate_num=0
        certficate=""
        sig_check =False
        ret_dict = {}

        # -----BEGIN CERTIFICATE-----
        p1=re.compile('^\-+BEGIN CERTIFICATE\-+$')

        # -----END CERTIFICATE-----
        p2=re.compile('^\-+END CERTIFICATE\-+$')

        # Signature version: 1
        p3=re.compile('^Signature version:\s+(?P<signature>\d+)$')

        # Signature:
        p4=re.compile('^Signature:$')

        # A59DA741EA66C2AFC006E1766B3B11493A79E67408388C40160C2729F88281E9
        p5=re.compile('^(?P<signatur>[A-Z\d]+)$')

        # o4IBBDCCAQAwDgYDVR0PAQH/BAQDAgXgMAwGA1UdEwEB/wQCMAAwHwYDVR0jBBgw
        p6 =re.compile('([a-zA-Z0-9/+=]+)')

        for line in output.splitlines():
            line=line.strip()

            # -----BEGIN CERTIFICATE-----
            m=p1.match(line)
            if m:
                begin_certf=True
                certificate_num = certificate_num + 1
                continue

            # -----END CERTIFICATE-----
            m=p2.match(line)
            if m:
                root_dict=ret_dict.setdefault('certificates',{})
                #certificate_list.append(certficate)
                root_dict[certificate_num] = certficate
                certficate = ''
                continue

            # Signature version: 1
            m=p3.match(line)
            if m:
                group=m.groupdict()
                ret_dict.setdefault('signature_version',int(group['signature']))
                continue

            # Signature:
            m=p4.match(line)
            if m:
                sig_check=True
                continue

            # 7E873A87E287B685E823F7BC66CF13D43EC238D40DA7CBEA06F6926C04C8C5AFC21BA4C
            m=p5.match(line)
            if m and sig_check:
                group=m.groupdict()
                ret_dict.setdefault('signature', group['signatur'])
                continue

            # o4IBBDCCAQAwDgYDVR0PAQH/BAQDAgXgMAwGA1UdEwEB/wQCMAAwHwYDVR0jBBgw
            m=p6.match(line)
            if m:
                certficate = certficate + m.group()
                continue
        return ret_dict


class ShowEnvironmentStatusSchema(MetaParser):
    """
    Schema for show environment status
    """
    schema = {
        Optional('power_supply'): {
            Any(): {
                'model_num': str,
                'type': str,
                'capacity': str,
                'status': str,
                'fan_states' :{
                    int: str,
                },
            },
        },
        Optional('fan_tray'): {
            Any(): {
                'status': str,
                'fan_states' :{
                    int: str,
                },
            },
        },
        Optional('switch'): {
            Any(): {
                Optional('power_supply'): {
                    Any(): {
                        'model_num': str,
                        'type': str,
                        'capacity': str,
                        'status': str,
                        'fan_states' :{
                            int: str,
                        },
                    },
                },
                Optional('fan_tray'): {
                    Any(): {
                        'status': str,
                        'fan_states' :{
                            int: str,
                        },
                    },
                },
            },
        },
    }


class ShowEnvironmentStatus(ShowEnvironmentStatusSchema):
    """ Parser for show environment status"""

    cli_command = 'show environment status'

    def cli(self,output=None):
        if output is None:
            # excute command to get output
            output = self.device.execute(self.cli_command)

        # initial variables
        ret_dict  = switch_id_dict = {}

        # Switch:1
        p1 = re.compile(r'^Switch:(?P<switch>\S+)$')

        # PS1     C9K-PWR-1500WAC-R     ac    n.a.      standby    good  good
        # PS0     C9K-PWR-650WAC-R      AC    650 W     ok         good  N/A
        p2 = re.compile(r'^(?P<power_supply>\S+) +'
                        r'(?P<model_num>\S+) +'
                        r'(?P<type>\S+) +'
                        r'(?P<capacity>\S+) +W?\s*'
                        r'(?P<status>\S+) +'
                        r'(?P<fan_state0>\S+) +'
                        r'(?P<fan_state1>\S+)$')

        # FM6     active      good  good
        p3= re.compile('^(?P<fan_tray>\w+\d+)\s+(?P<status>\w+)\s+(?P<fan_state0>\w+)\s+(?P<fan_state1>\w+)$')

        # FM0     ok          good  good  good  good
        p4= re.compile(r'^(?P<fan_tray>\w+\d+) +'
                        r'(?P<status>\w+) +'
                        r'(?P<fan_state0>\S+) +'
                        r'(?P<fan_state1>\S+) +'
                        r'(?P<fan_state2>\S+) +'
                        r'(?P<fan_state3>\S+)$')

        for line in output.splitlines():
            line = line.strip()

            #Switch:1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                switch = group['switch']
                switch_dict = ret_dict.setdefault('switch',{})
                switch_id_dict = switch_dict.setdefault(switch,{})
                continue

            # PS1     C9K-PWR-1500WAC-R     ac    n.a.      standby    good  good
            m=p2.match(line)
            if m:
                group= m.groupdict()
                root_dict=switch_id_dict.setdefault('power_supply',{}).setdefault(group['power_supply'],{})
                root_dict.setdefault('model_num',group['model_num'])
                root_dict.setdefault('type',group['type'])
                root_dict.setdefault('capacity',group['capacity'])
                root_dict.setdefault('status',group['status'])
                root_dict1=root_dict.setdefault('fan_states',{})
                root_dict1.setdefault(0,group['fan_state0'])
                root_dict1.setdefault(1,group['fan_state1'])
                continue

            # FM6     active      good  good
            m=p3.match(line)
            if m:
                group=m.groupdict()
                root_dict = switch_id_dict.setdefault('fan_tray', {}).setdefault(group['fan_tray'],{})
                root_dict.setdefault('status',group['status'])
                root_dict1=root_dict.setdefault('fan_states',{})
                root_dict1.setdefault(0,group['fan_state0'])
                root_dict1.setdefault(1,group['fan_state1'])
                continue

            # FM0     ok          good  good  good  good
            m=p4.match(line)
            if m:
                group=m.groupdict()
                root_dict = switch_id_dict.setdefault('fan_tray', {}).setdefault(group['fan_tray'],{})
                root_dict.setdefault('status',group['status'])
                root_dict1=root_dict.setdefault('fan_states',{})
                root_dict1.setdefault(0,group['fan_state0'])
                root_dict1.setdefault(1,group['fan_state1'])
                root_dict1.setdefault(2,group['fan_state2'])
                root_dict1.setdefault(3,group['fan_state3'])

        return ret_dict


# =====================================
# Schema for:
#  * 'show platform sudi pki'
# =====================================
class ShowPlatformSudiPkiSchema(MetaParser):
    """Schema for show platform sudi pki."""

    schema = {
        Optional('Cisco Manufacturing CA III certificate') : str,
        Optional('Cisco Manufacturing CA') : str,
        Optional('Cisco Manufacturing CA III') : str,
        Optional('Cisco Manufacturing CA SHA2') : str,

    }

# =====================================
# Parser for:
#  * 'show platform sudi pki'
# =====================================
class ShowPlatformSudiPki(ShowPlatformSudiPkiSchema):
    """Parser for show platform sudi pki"""

    cli_command = 'show platform sudi pki'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        #'Cisco Manufacturing CA III' certificate : Enabled
        #    SUDI Issuer-CN                      Validation status
        #    -----------------------------------------------------
        #    Cisco Manufacturing CA              Valid
        #    Cisco Manufacturing CA III          Valid
        #    Cisco Manufacturing CA SHA2         Valid

        ret_dict = {}

        p1=re.compile('((Cisco.+|\'Cisco.+:)\s+(?P<Valid>(((Enabled\s\(.*\))|Enabled)|((Disabled\s\(.*\))|Disabled)|Valid|Not Supported|Invalid|Init Failure)))')

        for line in output.splitlines():
            line1=[]
            line=line.strip()
            if ":" in line:
                line1.insert(0,'Cisco Manufacturing CA III certificate')
            else:
                line1 = line.split('  ')

            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict[line1[0]] = group['Valid']
                continue

        return ret_dict


# =============================================================================================================================
# Schema for 'show platform hardware fed switch active fwd-asic resource tcam table pbr record 0 format 0 | begin {nat_region}'
# =============================================================================================================================
class ShowPlatformTcamPbrSchema(MetaParser):
    """Schema for show platform hardware fed switch active fwd-asic resource tcam table pbr record 0 format 0 | begin {nat_region}"""

    schema = {
                 Optional(Any()):{
                     Optional('index'):{
                         Any():{
                             Optional('mask'):{
                                 Any(): str,
                             },
                             Optional('key'):{
                                 Any(): str,
                             },
                             Optional('ad'): str,
                         }
                     }
                 }
             }

# ============================================================================================================================
#  Parser for show platform hardware fed switch active fwd-asic resource tcam table pbr record 0 format 0 | begin {nat_region}
# ============================================================================================================================
class ShowPlatformTcamPbr(ShowPlatformTcamPbrSchema):
    """
    show platform hardware fed switch active fwd-asic resource tcam table pbr record 0 format 0 | begin {nat_region}
    """

    cli_command = ['show platform hardware fed {switch} active fwd-asic resource tcam table pbr record 0 format 0 | begin {nat_region}',
                   'show platform hardware fed active fwd-asic resource tcam table pbr record 0 format 0 | begin {nat_region}',
                   'show platform hardware fed switch {switch_type} fwd-asic resource tcam table pbr record 0 format 0 | begin {nat_region}']

    def cli(self, nat_region, switch="", switch_type="", output=None):

        if output is None:
            if switch:
                cmd = self.cli_command[0].format(switch=switch,nat_region=nat_region)
            else:
                if switch_type:
                    cmd = self.cli_command[2].format(nat_region=nat_region, switch_type=switch_type)
                else:
                    cmd = self.cli_command[1].format(nat_region=nat_region)

            output = self.device.execute(cmd)

        # initial variables
        ret_dict = {}

        # Printing entries for region NAT_1 (387) type 6 asic 0
        p00 = re.compile(r'^Printing entries for region\s(?P<nat_r>\w+)\s\(\d+\)\stype\s\d+\sasic\s\d$')

        #TAQ-1 Index-352 (A:0,C:0) Valid StartF-1 StartA-1 SkipF-0 SkipA-0
        p0 = re.compile(r'^TAQ-\d+\sIndex-(?P<index>\d+)\s\([A-Z]\:\d,[A-Z]\:\d\)\sValid\sStart[A-Z]-\d\sStart[A-Z]-\d\sSkip[A-Z]-\d\sSkip[A-Z]-\d$')

        # Mask1 00ffff00:00000000:00000000:00000000:00000000:00000000:00000000:00000000
        p1 = re.compile(r'^Mask(?P<mask_name>\d+) +(?P<mask_id>\S+)$')

        # Key1  00800400:00000000:00000000:00000000:00000000:00000000:00000000:00000000
        p2 = re.compile(r'^Key(?P<key_name>\d+) +(?P<key_id>\S+)$')

        # AD 10082000:00000001
        p3 = re.compile(r'^AD +(?P<ad>[\da-f:]+)$')

        for line in output.splitlines():
            line = line.strip()

            # Printing entries for region NAT_1 (387) type 6 asic 0
            m = p00.match(line)
            if m:
                group = m.groupdict()
                nat_r = group['nat_r']
                nat_dict = ret_dict.setdefault(nat_r, {})
                continue

            #TAQ-1 Index-352 (A:0,C:0) Valid StartF-1 StartA-1 SkipF-0 SkipA-0
            m = p0.match(line)
            if m:
                group = m.groupdict()
                index = group['index']
                index_dict = nat_dict.setdefault('index', {}).setdefault(index,{})
                mask_dict = index_dict.setdefault('mask',{})
                key_dict = index_dict.setdefault('key',{})

            # Mask1 3300f000:0f030000:00000000:00000000:00000000:00000000:00000000:ffffffff
            m = p1.match(line)
            if m:
                group = m.groupdict()
                mask_name = group['mask_name']
                mask_dict[mask_name] = group['mask_id']

            # Key1  11009000:01020000:00000000:00000000:00000000:00000000:00000000:c0000002
            m = p2.match(line)
            if m:
                group = m.groupdict()
                key_name = group['key_name']
                key_dict[key_name] = group['key_id']

            # AD 10087000:000000b6:00000000
            m = p3.match(line)
            if m:
                group = m.groupdict()
                index_dict['ad'] = group['ad']

        return ret_dict

# =============================================================
# Schema for 'show platform nat translations active statistics'
# =============================================================
class ShowPlatformNatTranslationsStatisticsSchema(MetaParser):
    """Schema for show platform nat translations active statistics"""

    schema = {
                  'nat_type': str,
                  'netflow_type': str,
                  'flow_record': str,
                  'dynamic_nat_entries': str,
                  'static_nat_entries': str,
                  'total_nat_entries': str,
                  'total_hw_resource_tcam': str
             }

# ============================================================
#  Parser for show platform nat translations active statistics
# ============================================================
class ShowPlatformNatTranslationsStatistics(ShowPlatformNatTranslationsStatisticsSchema):
    """
    show platform nat translations active statistics
    """

    cli_command = 'show platform nat translations active statistics'

    def cli(self, output=None):

        if output is None:

           output = self.device.execute(self.cli_command)

        # initial variables
        ret_dict = {}

        # NAT Type                : Static
        p0 = re.compile(r'^NAT Type +: +(?P<nat_type>-+|Static|Dynamic)$')

        # Netflow Type            : NA
        p1 = re.compile(r'^Netflow Type +: +(?P<netflow_type>\S+)$')

        # Flow Record             : Disabled
        p2 = re.compile(r'^Flow Record  +: +(?P<flow_record>-+|Disabled|Enabled)$')

        # Dynamic NAT entries     : 0 entries
        p3 = re.compile(r'^Dynamic NAT entries  +: +(?P<dynamic_nat_entries>\d+ entries)$')

        # Static NAT entries      : 0 entries
        p4 = re.compile(r'^Static NAT entries +: +(?P<static_nat_entries>\d+ entries)$')

        # Total NAT entries       : 0 entries
        p5 = re.compile(r'^Total NAT entries +: +(?P<total_nat_entries>\d+ entries)$')

        # Total HW Resource (TCAM): 26 of 27648 /0 .09% utilization
        p6 = re.compile(r'^Total HW Resource \(TCAM\)+: +(?P<total_hw_resource_tcam>\d+ of \d+ /\d+ \.\d+% utilization)$')

        for line in output.splitlines():
            line = line.strip()

            # NAT Type                : Static
            m = p0.match(line)
            if m:
                group = m.groupdict()
                ret_dict["nat_type"] = group["nat_type"]

            # Netflow Type            : NA
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict["netflow_type"] = group["netflow_type"]

            # Flow Record             : Disabled
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict["flow_record"] = group["flow_record"]

            # Dynamic NAT entries     : 0 entries
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict["dynamic_nat_entries"] = group["dynamic_nat_entries"]

            # Static NAT entries      : 0 entries
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ret_dict["static_nat_entries"] = group["static_nat_entries"]

            # Total NAT entries       : 0 entries
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ret_dict["total_nat_entries"] = group["total_nat_entries"]

            # Total HW Resource (TCAM): 26 of 27648 /0 .09% utilization
            m = p6.match(line)
            if m:
                group = m.groupdict()
                ret_dict["total_hw_resource_tcam"] = group["total_hw_resource_tcam"]

        return ret_dict

# ==================================================
# Schema for 'show platform nat translations active'
# ==================================================
class ShowPlatformNatTranslationsSchema(MetaParser):
    """Schema for show platform nat translations active"""

    schema = {
                 'index':{
                     Any():{
                         'protocol': str,
                         'inside_global': str,
                         'inside_local': str,
                         'outside_local': str,
                         'outside_global': str
                     }
                  }
             }

# =================================================
#  Parser for show platform nat translations active
# =================================================
class ShowPlatformNatTranslations(ShowPlatformNatTranslationsSchema):
    """
    show platform nat translations active
    """

    cli_command = 'show platform nat translations active'

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)

        # initial variables
        ret_dict = {}
        index_dict = {}
        index = 1

        # Pro Inside global Inside local Outside local Outside global
        # TCP 135.0.0.2:0   192.0.0.2:0  193.0.0.2:0   193.0.0.2:0
        p1 = re.compile(r'^(?P<protocol>-+|UDP|TCP) +'
                        r'(?P<inside_global>[\d.]+:+\d+) +'
                        r'(?P<inside_local>[\d.]+:+\d+) +'
                        r'(?P<outside_local>[\d.]+:+\d+) +'
                        r'(?P<outside_global>[\d.]+:+\d+)$')

        for line in output.splitlines():
            line = line.strip()

            # Pro Inside global Inside local Outside local Outside global
            # TCP 135.0.0.2:0   192.0.0.2:0  193.0.0.2:0   193.0.0.2:0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                index_dict = ret_dict.setdefault('index', {}).setdefault(index,{})
                index_dict['protocol'] = group['protocol']
                index_dict['inside_global'] = group['inside_global']
                index_dict['inside_local'] = group['inside_local']
                index_dict['outside_local'] = group['outside_local']
                index_dict['outside_global'] = group['outside_global']
                index += 1

        return ret_dict


# ==========================================================================================================
# Schema for 'show platform hardware fed switch active fwd-asic resource tcam table acl | begin {INPUT_NAT}'
# ==========================================================================================================
class ShowPlatformTcamAclSchema(MetaParser):
    """Schema for show platform hardware fed switch active fwd-asic resource tcam table acl | begin {INPUT_NAT}"""

    schema = {
                 'index':{
                     Any():{
                         'labels': {
                             Any(): {
                                 'vcu_results': int,
                                 'l3len': int,
                                 'l3pro': int,
                                 'l3tos': int,
                                 'srcaddr': int,
                                 'dstaddr': int,
                                 'mtrid': int,
                                 'vrfid': int,
                                 'sh': int,
                                 'mvid': int,
                                 'l3err': int
                              },
                         },
                        'nat_result_rm': int,
                        'nat_static_rule': int,
                        'nat_dynamic_rule': int
                        }
                   }
             }

# =========================================================================================================
#  Parser for show platform hardware fed switch active fwd-asic resource tcam table acl | begin {INPUT_NAT}
# =========================================================================================================
class ShowPlatformTcamAcl(ShowPlatformTcamAclSchema):
    """
    show platform hardware fed switch active fwd-asic resource tcam table acl | begin {INPUT_NAT}
    """

    cli_command = 'show platform hardware fed switch active fwd-asic resource tcam table acl | begin {INPUT_NAT}'

    def cli(self, INPUT_NAT, output=None):

        cmd = self.cli_command.format(INPUT_NAT=INPUT_NAT)

        if output is None:
            output = self.device.execute(cmd)

        # initial variables
        ret_dict = {}

        # Index-1152
        p0 = re.compile(r'Index-+(?P<index>\d+)$')

        # Labels vcuResults l3Len l3Pro l3Tos SrcAddr  DstAddr  mtrid vrfid  SH Mvid  l3Err
        # M:  00000000   0000  00    00  00000000 00000000  00   0000   0000 000   00
        # V:  00000000   0000  00    00  00000000 00000000  00   0000   0000 000   00
        p1 = re.compile(r'^(?P<labels>\S+) +'
                        r'(?P<vcu_results>\d+) +'
                        r'(?P<l3len>\d+) +'
                        r'(?P<l3pro>\d+) +'
                        r'(?P<l3tos>\d+) +'
                        r'(?P<srcaddr>\d+) +'
                        r'(?P<dstaddr>\d+) +'
                        r'(?P<mtrid>\d+) +'
                        r'(?P<vrfid>\d+) +'
                        r'(?P<sh>\d+) +'
                        r'(?P<mvid>\d+) +'
                        r'(?P<l3err>\d+)$')

        # natResultRm    natStaticRule     natDynamicRule
        # 1                1                  0
        p2 = re.compile(r'^(?P<nat_result_rm>\d+) +(?P<nat_static_rule>\d+) +(?P<nat_dynamic_rule>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            # Index-1152
            m = p0.match(line)
            if m:
                group = m.groupdict()
                index = group['index']
                index_dict = ret_dict.setdefault('index', {}).setdefault(index, {})

            # Labels vcuResults l3Len l3Pro l3Tos SrcAddr  DstAddr  mtrid vrfid  SH Mvid  l3Err
            # M:  00000000   0000  00    00  00000000 00000000  00   0000   0000 000   00
            # V:  00000000   0000  00    00  00000000 00000000  00   0000   0000 000   00
            m = p1.match(line)
            if m:
                group = m.groupdict()
                labels = group['labels']
                label_dict = index_dict.setdefault('labels', {}).setdefault(labels, {})
                label_dict['vcu_results'] = int(group['vcu_results'])
                label_dict['l3len'] = int(group['l3len'])
                label_dict['l3pro'] = int(group['l3pro'])
                label_dict['l3tos'] = int(group['l3tos'])
                label_dict['srcaddr'] = int(group['srcaddr'])
                label_dict['dstaddr'] = int(group['dstaddr'])
                label_dict['mtrid'] = int(group['mtrid'])
                label_dict['vrfid'] = int(group['vrfid'])
                label_dict['sh'] = int(group['sh'])
                label_dict['mvid'] = int(group['mvid'])
                label_dict['l3err'] = int(group['l3err'])

            # natResultRm    natStaticRule     natDynamicRule
            # 1                1                  0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                index_dict ['nat_result_rm'] = int(group['nat_result_rm'])
                index_dict ['nat_static_rule'] = int(group['nat_static_rule'])
                index_dict ['nat_dynamic_rule'] = int(group['nat_dynamic_rule'])

        return ret_dict

class ShowVersionRunningSchema(MetaParser):
    """show version running."""

    schema = {
       'version_running': {
           Any(): {
               'package': str,
               'version': str,
               'status': str,
               'role': str,
               'file': str,
               'on': str,
               'built': str,
               'by': str,
               'file_sha_checksum': str
           }
       }
    }


class ShowVersionRunning(ShowVersionRunningSchema):
    """show version running"""

    cli_command = ["show version running"]

    def cli(self, output=None):
        if output is None:
            # get output from device
            output = self.device.execute(self.cli_command[0])

        # initial return dictionary
        ret_dict = {}
        index = 0

        # initial regexp pattern
        # Package: Provisioning File, version: n/a, status: active
        p1 = re.compile(r'^Package: +(?P<package>[\w+\s+\w]+)+, +version: (?P<version>\S+)+, status: (?P<status>\S+)$')

        # Role: provisioning file
        p2 = re.compile(r'^Role: +(?P<role>[\w+\s+\w]+)$')

        # File: bootflash:cat9k-rpbase.BLD_POLARIS_DEV_LATEST_20211115_013205.SSA.pkg, on: RP0
        p3 = re.compile(r'^File: +(?P<file>\S+)+, on: (?P<on>\S+)$')

        # Built: 2021-11-14_18.31, by: mcpre
        p4 = re.compile(r'^Built: +(?P<built>\S+)+, by: (?P<by>\S+)$')

        # File SHA1 checksum: 69c0fe122c9f0885021f874875caeba46a2c6d07
        p5 = re.compile(r'^File SHA1 checksum: +(?P<file_sha_checksum>\S+)$')

        for line in output.splitlines():
            line = line.strip()

            # Last configuration file parsed
            m = p1.match(line)
            if m:
                group = m.groupdict()
                index += 1
                ver = ret_dict.setdefault('version_running', {}).setdefault(index, {})
                ver.update({'package': group['package']})
                ver.update({'version': group['version']})
                ver.update({'status': group['status']})
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                ver.update({'role': group['role']})
                continue

            m = p3.match(line)
            if m:
                group = m.groupdict()
                ver.update({'file': group['file']})
                ver.update({'on': group['on']})
                continue

            m = p4.match(line)
            if m:
                group = m.groupdict()
                ver.update({'built': group['built']})
                ver.update({'by': group['by']})
                continue

            m = p5.match(line)
            if m:
                group = m.groupdict()
                ver.update({'file_sha_checksum': group['file_sha_checksum']})
                continue

        return ret_dict

# ==========================================
# Schema for
#   'show call admission statistics'
#   'show call admission statistics detailed'
# ===========================================

class ShowCallAdmissionStatisticsSchema(MetaParser):
    """
    Schema for
        * 'show call admission statistics'
        * 'show call admission statistics detailed'
    """

    schema = {
        'cac_status': str,
        'cac_state': str,
        'calls_rejected': int,
        'cac_duration': int,
        'calls_accepted': int,
        Optional('total_call_session_charges'): int,
        Optional('call_limit'): int,
        Optional('current_actual_cpu'): int,
        Optional('cpu_limit'): int,
        Optional('fsol_packet_drop'): int,
        Optional('cac_events'): {
            Optional("reject_reason"): {
                Optional('cpu_limit'): {
                    Optional('times_of_activation'): int,
                    Optional('duration_of_activation'): int,
                    Optional('rejected_calls'): int
                },
                Optional('session_charges'): {
                    Optional('times_of_activation'): int,
                    Optional('duration_of_activation'): int,
                    Optional('rejected_calls'): int
                },
                Optional('low_platform_resources'): {
                    Optional('times_of_activation'): int,
                    Optional('duration_of_activation'): int,
                    Optional('rejected_calls'): int
                },
                Optional('session_limit'): {
                    Optional('times_of_activation'): int,
                    Optional('duration_of_activation'): int,
                    Optional('rejected_calls'): int
                }
            }
        }
    }

class ShowCallAdmissionStatistics(ShowCallAdmissionStatisticsSchema):
    """
    Parser for
        * 'show call admission statistics'
        * 'show call admission statistics detailed'
    """
    cli_command = ['show call admission statistics']

    def cli(self, output=None):
        cmd = self.cli_command[0]

        if output is None:
            output = self.device.execute(self.cli_command[0])

        res_dict = {}
        # CAC New Model (SRSM) is ACTIVE
        p1 = re.compile(r'^CAC New Model \(SRSM\) is (?P<state>\w+)$')

        # CAC statistics duration:  2(seconds)
        p2 = re.compile(r'^CAC statistics duration:  (?P<duration>\d+)'
                        r'\(seconds\)$')

        # Total calls rejected 0, accepted 0
        p3 = re.compile(r'^Total calls rejected (?P<rejected>\d+), '
                        r'accepted (?P<accepted>\d+)$')

        # Current hardware CAC status is: Not Dropping
        p4 = re.compile(r'^Current hardware CAC status is: '
                        r'(?P<status>\w+\s?\w+)$')

        # Total call Session charges: 0, limit 350
        p5 = re.compile(r'^Total call Session charges: (?P<total_call_session_charges>'
                        r'\d+), limit (?P<call_limit>\d+)$')

        # CPU utilization: Five Sec Average CPU Load, Current actual CPU: 3%, Limit: 80%
        p6 = re.compile(r'^CPU utilization: Five Sec Average CPU Load, Current actual '
                        r'CPU: (?P<current_actual_cpu>\d+)%, Limit: (?P<cpu_limit>\d+)%$')

        # CPU-limit:              3354                116                  33541234
        p7 = re.compile(r'^CPU-limit:\s+(?P<times_of_activation>\d+)\s+'
                        r'(?P<duration_of_activation>\d+)\s+(?P<rejected_calls>\d+)$')

        # SessionCharges:          27                  0                    27
        p8 = re.compile(r'^SessionCharges:\s+(?P<times_of_activation>\d+)\s+'
                        r'(?P<duration_of_activation>\d+)\s+(?P<rejected_calls>\d+)$')

        # LowPlatformResource:     0                   0                     0
        p9 = re.compile(r'^LowPlatformResource:\s+(?P<times_of_activation>\d+)\s+'
                        r'(?P<duration_of_activation>\d+)\s+(?P<rejected_calls>\d+)$')

        # Session Limit:         9876543               0                     0
        p10 = re.compile(r'^Session Limit:\s+(?P<times_of_activation>\d+)\s+'
                         r'(?P<duration_of_activation>\d+)\s+(?P<rejected_calls>\d+)$')

        # Total dropped FSOL packets at data plane: 0
        p11 = re.compile(r'^Total dropped FSOL packets at data plane: (?P<fsol_drop>\d+)$')
        for line in output.splitlines():
            line = line.strip()

            # CAC New Model (SRSM) is ACTIVE
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                res_dict['cac_state'] = groups['state']
                continue

            # CAC statistics duration:  2(seconds)
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                res_dict['cac_duration'] = int(groups['duration'])
                continue

            # Total calls rejected 0, accepted 0
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                res_dict['calls_rejected'] = int(groups['rejected'])
                res_dict['calls_accepted'] = int(groups['accepted'])
                continue

            # Total calls rejected 0, accepted 0
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                res_dict['cac_status'] = groups['status']
                continue

            # Total call Session charges: 0, limit 350
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                res_dict['total_call_session_charges'] = int(groups['total_call_session_charges'])
                res_dict['call_limit'] = int(groups['call_limit'])
                continue

            # CPU utilization: Five Sec Average CPU Load, Current actual CPU: 3%, Limit: 80%
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                res_dict['current_actual_cpu'] = int(groups['current_actual_cpu'])
                res_dict['cpu_limit'] = int(groups['cpu_limit'])
                continue

            # CPU-limit:         3354            116                3354
            m = p7.match(line)
            if m:
                res_dict.setdefault('cac_events', {})
                res_dict['cac_events'].setdefault('reject_reason', {})
                res_dict['cac_events']['reject_reason'].setdefault('cpu_limit', {})
                groups = m.groupdict()
                res_dict['cac_events']['reject_reason']['cpu_limit'] \
                    ['times_of_activation'] = int(groups['times_of_activation'])
                res_dict['cac_events']['reject_reason']['cpu_limit'] \
                    ['duration_of_activation'] = int(groups['duration_of_activation'])
                res_dict['cac_events']['reject_reason']['cpu_limit'] \
                    ['rejected_calls'] = int(groups['rejected_calls'])

            # SessionCharges:                  27                     0                          27
            m = p8.match(line)
            if m:
                res_dict.setdefault('cac_events', {})
                res_dict['cac_events'].setdefault('reject_reason', {})
                res_dict['cac_events']['reject_reason'].setdefault('session_charges', {})
                groups = m.groupdict()
                res_dict['cac_events']['reject_reason']['session_charges'] \
                    ['times_of_activation'] = int(groups['times_of_activation'])
                res_dict['cac_events']['reject_reason']['session_charges'] \
                    ['duration_of_activation'] = int(groups['duration_of_activation'])
                res_dict['cac_events']['reject_reason']['session_charges'] \
                    ['rejected_calls'] = int(groups['rejected_calls'])

            # LowPlatformResource:             0                      0                          0
            m = p9.match(line)
            if m:
                res_dict.setdefault('cac_events', {})
                res_dict['cac_events'].setdefault('reject_reason', {})
                res_dict['cac_events']['reject_reason'].setdefault('low_platform_resources', {})
                groups = m.groupdict()
                res_dict['cac_events']['reject_reason']['low_platform_resources'] \
                    ['times_of_activation'] = int(groups['times_of_activation'])
                res_dict['cac_events']['reject_reason']['low_platform_resources'] \
                    ['duration_of_activation'] = int(groups['duration_of_activation'])
                res_dict['cac_events']['reject_reason']['low_platform_resources'] \
                    ['rejected_calls'] = int(groups['rejected_calls'])

            # Session Limit:                   0                      0                          0
            m = p10.match(line)
            if m:
                res_dict.setdefault('cac_events', {})
                res_dict['cac_events'].setdefault('reject_reason', {})
                res_dict['cac_events']['reject_reason'].setdefault('session_limit', {})
                groups = m.groupdict()
                res_dict['cac_events']['reject_reason']['session_limit'] \
                    ['times_of_activation'] = int(groups['times_of_activation'])
                res_dict['cac_events']['reject_reason']['session_limit'] \
                    ['duration_of_activation'] = int(groups['duration_of_activation'])
                res_dict['cac_events']['reject_reason']['session_limit'] \
                    ['rejected_calls'] = int(groups['rejected_calls'])

            # Total dropped FSOL packets at data plane: 0
            m = p11.match(line)
            if m:
                groups = m.groupdict()
                res_dict['fsol_packet_drop'] = int(groups['fsol_drop'])

        return res_dict

class ShowCallAdmissionStatisticsDetailed(ShowCallAdmissionStatistics):
    ''' Parser for:
           * show call admission statistics detailed
    '''
    cli_command = ['show call admission statistics detailed']

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command[0])

        return super().cli(output=output)

# ====================================================
#  Schema for :
#  * 'show rep topology segment {no}'
# ====================================================

class ShowRepTopologySegmentSchema(MetaParser):
    """Schema for show rep topology segment {no}"""
    schema = {
        'interfaces' : {
            Any() : {
                'port' : str,
                'bridge' : str,
                'edge' : str,
                'role' : str
            },
        }
    }

# ====================================================
#  Parser for :
#  * 'show rep topology segment {no}'
# ====================================================

class ShowRepTopologySegment(ShowRepTopologySegmentSchema):

    """Parser for show rep topology segment {no}"""

    cli_command = 'show rep topology segment {no}'

    def cli(self, no, output=None):

        if output is None:
            output = self.device.execute(self.cli_command.format(no=no))

        ret_dict = {}

        # fr1                              Tw2/0/3    Pri* Alt
        # fr1                              Gi1/0/3    Sec* Open
        p1 = re.compile(r'(?P<bridge>\S+)\s+(?P<interface>[a-z|A-Z]+\d+\/\d+\/\d+)\s+(?P<edge>\S+)\s+(?P<role>\S+)')

        for line in output.splitlines():

            line = line.strip()

            # fr1                              Tw2/0/3    Pri* Alt
            # fr1                              Gi1/0/3    Sec* Open
            m = p1.match(line)
            if m:
                group = m.groupdict()
                intf = Common.convert_intf_name(group.pop('interface'))

                intf_dict = ret_dict.setdefault('interfaces', {}).setdefault(intf, {})

                intf_dict['port'] = intf
                intf_dict.update({k: v for k, v in group.items()})

                continue

        return ret_dict

# ==================================================
# Parser for 'show platfrm packet-trace'
# ==================================================
class ShowPlatformPktTraceStatsSchema(MetaParser):
    """schema for show packet-trace statistics"""
    schema = {
        'packets_summary': {
            Optional('matched'): int,
            'traced': int
        },
        'packets_recieved': {
            'ingress': int,
            'inject': int
        },
        'packets_processed': {
            'forward': int,
            'punt': int,
            'drop': int,
            'consume': int
        }
    }

class ShowPlatformPacketStats(ShowPlatformPktTraceStatsSchema):
    """
    parser for show platform packet-trace statistics
    """
    cli_command = ['show platform packet-trace statistics']

    def cli(self, output=None):
        if output is None:
            cmd = self.cli_command[0]
            output = self.device.execute(cmd)

        ret_dict = {}

        # Packets Summary
        #   Matched  1
        p1 = re.compile(r'\s+Matched\s+(?P<count>\d+)')
        # Packets Traced: 5
        #    or (different version)
        #   Traced   11
        p2 = re.compile(r'.*Traced:?\s+(?P<count>\d+)')

        # Packets Received
        #   Ingress  12
        #   Inject   13
        p3 = re.compile(r'^\s+(?P<pkt_type>(Ingress|Inject))\s+(?P<count>\d+)$')

        # Packets Processed
        #   Forward  14
        #   Punt     15
        #   Drop     16
        #   Consume  17
        p4 = re.compile(r'^\s+(?P<pkt_type>(Forward|Punt|Drop|Consume))\s+(?P<count>\d+)$')

        for line in output.splitlines():

            # Packets Summary
            #   Matched  1
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                ret_dict.setdefault('packets_summary', {})['matched'] = int(groups['count'])
                continue
            # Packets Traced: 5
            #    or (different version)
            #   Traced   11
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                ret_dict.setdefault('packets_summary', {})['traced'] = int(groups['count'])
                continue

            # Packets Received
            #   Ingress  12
            #   Inject   13
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                key = groups['pkt_type'].lower()
                ret_dict.setdefault('packets_recieved', {})[key] = int(groups['count'])
                continue

            # Packets Processed
            #   Forward  14
            #   Punt     15
            #   Drop     16
            #   Consume  17
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                key = groups['pkt_type'].lower()
                ret_dict.setdefault('packets_processed', {})[key] = int(groups['count'])
                continue

        return ret_dict


class ShowPlatformPktTraceSummarySchema(MetaParser):
    """schema for show platform packet-trace summary"""

    schema = {
        'packets': {
            int: {
                'input_intf': str,
                'output_intf': str,
                'state': str,
                Optional('reason'): {
                    'code': int,
                    'text': str
                }
            }
        }
    }


class ShowPlatformPacketSumm(ShowPlatformPktTraceSummarySchema):
    """
    parser for show platform packet-trace statistics
    """
    cli_command = ['show platform packet-trace summary']

    def cli(self, output=None):
        if output is None:
            cmd = self.cli_command[0]
            output = self.device.execute(cmd)

        ret_dict = {}

        # Pkt   Input            Output           State  Reason
        # 0     Gi0/0/1          Gi0/0/0          FWD     97  (Packets to LFTS)
        p = re.compile(r'\s*(?P<pkt>\d+)\s+(?P<input>\S+)\s+(?P<output>\S+)'
                       r'\s+(?P<state>\S+)(\s+(?P<reason_code>\d+)\s+(?P<reason_str>.*$))?')

        for line in output.splitlines():
            m = p.match(line)
            if m:
                groups = m.groupdict()
                pkt_num = int(groups['pkt'])
                ret_dict.setdefault('packets', {}).update({
                    pkt_num: {
                        'input_intf': groups['input'],
                        'output_intf': groups['output'],
                        'state': groups['state']
                    }
                })

                # add the reason code if matched
                reason_code = groups['reason_code'] or None
                if reason_code is not None:
                    reason_code = int(reason_code)
                    ret_dict['packets'][pkt_num].update({
                        'reason': {
                            'code': reason_code,
                            'text': groups['reason_str']
                        },
                    })
        return ret_dict


class ShowPlatformPacketTracePacketSchema(MetaParser):
    """schema for show platform packet-trace packet all|packet_num"""

    schema = {
        'packets': {
            int: {
                'cbug_id': int,
                'summary': {
                    'input': str,
                    'output': str,
                    'state': str,
                    'start_timestamp_ns': int,
                    'stop_timestamp_ns': int,
                    'start_timestamp': str,
                    'stop_timestamp': str,
                },
                'path_trace': {
                    Optional('ipv4_input'): {
                        'input': str,
                        'output': str,
                        'source': str,
                        'destination': str,
                        'protocol': str,
                        Optional('src_port'): str,
                        Optional('dst_port'): str
                    },
                    Optional('ipv4_output'): {
                        'input': str,
                        'output': str,
                        'source': str,
                        'destination': str,
                        'protocol': str,
                        Optional('src_port'): str,
                        Optional('dst_port'): str
                    },
                    Optional('icmpv4_input'): {
                        'input': str,
                        'output': str,
                        'type': str,
                        'code': str
                    },
                    Optional('icmpv4_output'): {
                        'input': str,
                        'output': str,
                        'type': str,
                        'code': str
                    },
                    Optional('cft'): {
                        'api': str,
                        'packet_capabilities': str,
                        'input_vrf_idx': str,
                        'calling_feature': str,
                        'direction': str,
                        'triplet_vrf_idx': str,
                        'triplet_network_start': str,
                        'triplet_triplet_flags': str,
                        'triplet_counter': str,
                        'cft_bucket_number': str,
                        'cft_l3_payload_size': str,
                        'cft_pkt_ind_flags': str,
                        'cft_pkt_ind_valid': str,
                        'tuple_src_ip': str,
                        'tuple_dst_ip': str,
                        'tuple_src_port': str,
                        'tuple_dst_port': str,
                        'tuple_vrfid': str,
                        'tuple_l4_protocol': str,
                        'tuple_l3_protocol': str,
                        'pkt_sb_state': str,
                        'pkt_sb_num_flows': str,
                        'pkt_sb_tuple_epoch': str,
                        'returned_cft_error': str,
                        'returned_fid': str
                    },
                    Optional('nbar'): {
                        'packet_number_in_flow': str,
                        'classification_state': str,
                        'classification_name': str,
                        'classification_id': str,
                        'classification_source': str,
                        'number_of_matched_sub_classifications': str,
                        'number_of_extracted_fields': str,
                        'is_pa_split_packet': str,
                        'tph_mqc_bitmask_value': str
                    },
                    Optional('qos'): {
                        'direction': str,
                        'action': str,
                        'fields': str
                    },
                    Optional('ipsec'): {
                        'action': str,
                        'sa_handle': str,
                        'spi': str,
                        'peer_addr': str,
                        'local_addr': str
                    },
                    Optional('nat'): {
                        'direction': str,
                        'from': str,
                        'action': str,
                        'fwd_point': str,
                        'vrf': str,
                        'table_id': str,
                        'protocol': str,
                        'src_addr': str,
                        'dest_addr': str,
                        'src_port': str,
                        'dst_port': str
                    }

                },
                Optional('iosd_flow'): {
                    Optional('infra'): {
                        'pkt_direction': str,
                        'packet_rcvd_from': str
                    },
                    Optional('ip'): {
                        'pkt_direction': str,
                        'packet_enqueued_in': str,
                        'source': str,
                        'destination': str,
                        'interface': str
                    },
                    Optional('tcp'): {
                        'pkt_direction': str,
                        'tcp0': str
                    },
                    Optional('udp'):  {
                        'pkt_direction': str,
                        'src': str,
                        'dst': str,
                        'length': str
                    }
                }
            }
        }
    }

class ShowPlatformPacketTracePacket(ShowPlatformPacketTracePacketSchema):
    """
    parser for `show platform packet-trace packet all|packet_id`
    """
    cli_command = ['show platform packet-trace packet all',
                   'show platform packet-trace packet {packet_id}']

    FIRST_CAP_REGEX = re.compile('(.)([A-Z][a-z]+)')
    ALL_CAP_REGEX = re.compile('([a-z0-9])([A-Z])')
    SLUGIFY_P = re.compile(r'[^a-z0-9]+')

    def _field_name_normalize(self, name):
        """
        convert field name to snake_case (.e.g CamleCase to snake_case) and remove unwanted special chars.
        :param name: str
        :return:str
        """
        # convert to snake_case
        string_one = self.FIRST_CAP_REGEX.sub(r'\1_\2', name)
        name = self.ALL_CAP_REGEX.sub(r'\1_\2', string_one).lower()
        # slugify
        name = re.sub(self.SLUGIFY_P, '_', name)
        name = re.sub(r'_{2,}', '_', name).strip('_')
        return name

    def cli(self, output=None, packet_id=None):
        if output is None:
            if packet_id is None:
                cmd = self.cli_command[0]
            else:
                cmd = self.cli_command[0].format(packet_id=packet_id)
            output = self.device.execute(cmd)

        # Packet: 0           CBUG ID: 104
        p_packet_start = re.compile(r'Packet:\s+(?P<packet_id>\d+)\s+CBUG\s+ID:\s(?P<cbug_id>\d+)')
        # Summary
        p_summary_start = re.compile(r'Summary$')
        #  Timestamp
        #   Start   : 19591546248064016 ns (07/27/2021 09:34:28.261898 UTC)
        #   Stop    : 19591546248087028 ns (07/27/2021 09:34:28.261921 UTC)
        p_timestamp = re.compile(
            r'\s+(?P<field>(Start)|(Stop))\s+:\s(?P<time_ns>\d+)\s+ns\s+'
            r'\((?P<date_str>\d+/\d+/\d+\s+\d+:\d+:\d+\.\d+)\s+\w+\)')
        #   Feature: IPV4(Output)
        p_feature_start = re.compile(r'\s+Feature:\s(?P<feature_name>[\w\\()]+)')
        # Path Trace
        p_path_trace_start = re.compile(r'Path\s+Trace$')
        # IOSd Path Flow: Packet: 1    CBUG ID: 105
        p_iosd_flow_start = re.compile(r'IOSd\sPath\sFlow:\sPacket:')

        p_from_plane = re.compile(r'\s+Packet\s+Rcvd\s+From\s+(?P<from_plane>\w+)')
        p_layer = re.compile(r'\s+Packet\s+Enqueued\s+in\s+(?P<layer>.*)')

        ret_dict = {}

        for line in output.splitlines():
            # start a with new packet
            # Packet: 0           CBUG ID: 104
            m = p_packet_start.match(line)
            if m:
                groups = m.groupdict()
                packet_id = int(groups['packet_id'])
                packet_dict = ret_dict.setdefault('packets', {}).setdefault(packet_id, {})
                packet_dict['cbug_id'] = int(groups['cbug_id'])
                continue

            # Summary
            m = p_summary_start.match(line)
            if m:
                current_dict = packet_dict.setdefault('summary', {})
                continue

            # Path Trace
            m = p_path_trace_start.match(line)
            if m:
                current_features_key = 'path_trace'
                continue
            # IOSd Path Flow: Packet: 1    CBUG ID: 105
            m = p_iosd_flow_start.match(line)
            if m:
                current_features_key = 'iosd_flow'
                continue

            #   Feature: IPV4(Output)
            m = p_feature_start.match(line)
            if m:
                groups = m.groupdict()
                current_feature = self._field_name_normalize(groups['feature_name'])
                current_dict = packet_dict.setdefault(current_features_key, {}).setdefault(current_feature, {})
                continue

            #  Timestamp
            #   Start   : 19591546248064016 ns (07/27/2021 09:34:28.261898 UTC)
            #   Stop    : 19591546248087028 ns (07/27/2021 09:34:28.261921 UTC)
            m = p_timestamp.match(line)
            if m:
                groups = m.groupdict()
                current_dict.update({
                    groups['field'].lower() + '_timestamp_ns': int(groups['time_ns']),
                    groups['field'].lower() + '_timestamp': groups['date_str']
                })
                continue

            #     Packet Rcvd From DATAPLANE
            m = p_from_plane.match(line)
            if m:
                groups = m.groupdict()
                current_dict['packet_rcvd_from'] = groups['from_plane']
                continue

            #     Packet Enqueued in IP layer
            m = p_layer.match(line)
            if m:
                groups = m.groupdict()
                current_dict['packet_enqueued_in'] = groups['layer']
                continue

            # from here on we match all lines by splitting by :
            #
            # current_dict is set to summary or the respective feature based on earlier
            # matches

            # Summary
            #   Input     : GigabitEthernet1
            #   Output    : internal0/0/rp:0
            #   State     : PUNT 11  (For-us data)

            # Path Trace
            #     Input       : GigabitEthernet1
            #     <snippt>
            #     Protocol    : 6 (TCP)
            #       SrcPort   : 43520
            #       DstPort   : 22
            #     API                   : cft_handle_pkt
            #     packet capabilities   : 0x000000af
            #     <snip>
            #     triplet.triplet_flags : 0x00000000
            #     triplet.counter       : 0

            line = line.split(':', maxsplit=1)
            if len(line) == 2:
                current_dict[self._field_name_normalize(line[0])] = line[1].strip()
                continue

        return ret_dict

class ShowSystemMtuSchema(MetaParser):
    """
    Schema for show system mtu
    """
    schema = {
            'mtu_in_bytes': int
                }

class ShowSystemMtu(ShowSystemMtuSchema):
    """ Parser for show system mtu"""

    cli_command = 'show system mtu'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # initial variables
        ret_dict = {}

        # Global Ethernet MTU is 1500 bytes
        p1 = re.compile(r'^Global\s+Ethernet\s+MTU\s+is\s+(?P<mtu_in_bytes>\d+)\s+bytes\.$')


        for line in output.splitlines():
            line = line.strip()

            # Global Ethernet MTU is 1500 bytes
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['mtu_in_bytes'] =int(group['mtu_in_bytes'])
                continue
        return ret_dict

# ======================================================================================
# Parser for 'show processes cpu platform sorted'
# ======================================================================================

class ShowProcessesCpuPlatformSorted(ShowProcessesCpuPlatform):
    """Parser for show processes cpu platform sorted"""

    cli_command = 'show processes cpu platform sorted'

    def cli(self, output=None):
        return(super().cli(output=output))


class ShowFileSystemsSchema(MetaParser):
    """
    Schema for show file systems
    """
    schema = {
        'file_systems': {
                Any(): {
                    'total_size': int,
                    'free_size': int,
                    'type': str,
                    'flags': str,
                    'prefixes': str,
                }
        },
    }


class ShowFileSystems(ShowFileSystemsSchema):
    """
    Parser for show file systems
    """

    cli_command = 'show file systems'

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)
        # initialze return dictionary
        ret_dict = {}
        index = 0
        #*  11353194496    7130390528      disk     rw   flash-3:
        p0 = re.compile(r'^\*\s*(?P<total_size>\d+)\s*(?P<free_size>\d+)\s*(?P<type>\w+)\s*(?P<flags>\w+)\s*(?P<prefixes>[\S\s]+)$')
        #8162746368    8019398656      disk     ro   webui:
        p1 = re.compile(r'^(?P<total_size>\d+)\s*(?P<free_size>\d+)\s*(?P<type>\S*)\s*(?P<flags>\S*)\s*(?P<prefixes>[\S\s]+)$')

        for line in output.splitlines():
            line = line.strip()
            #*  11353194496    7130390528      disk     rw   flash-3:
            if p0.match(line):
                m = p0.match(line)
            else:
            #8162746368    8019398656      disk     ro   webui:
                m = p1.match(line)

            if m:
                group = m.groupdict()
                index += 1
                file_systems_dict = ret_dict.setdefault('file_systems', {}).setdefault(index, {})
                file_systems_dict.update({'total_size': int(group['total_size'])})
                file_systems_dict.update({'free_size': int(group['free_size'])})
                file_systems_dict.update({'type': group['type']})
                file_systems_dict.update({'flags': group['flags']})
                file_systems_dict.update({'prefixes': group['prefixes']})

        return ret_dict

# ======================================================
# Parser for 'show redundancy config-sync failures mcl '
# ======================================================

class ShowRedundancyConfigSyncFailuresMclSchema(MetaParser):
    """Schema for show redundancy config-sync failures mcl"""

    schema = {
        'err_list': list,
    }

class ShowRedundancyConfigSyncFailuresMcl(ShowRedundancyConfigSyncFailuresMclSchema):
    """Parser for show redundancy config-sync failures mcl"""

    cli_command = 'show redundancy config-sync failures mcl'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # The list is Empty
        p1 = re.compile(r"^The\s+list\s+is\s+Empty$")

        # 00:06:31: Config Sync: Starting lines from MCL file:
        p2 = re.compile(r"^\S+\s+Config Sync: Starting lines from MCL file:$")

        ret_dict = {}
        err_flag = False

        for line in output.splitlines():
            line = line.strip()

            # The list is Empty
            match_obj = p1.match(line)
            if match_obj:
                ret_dict.setdefault("err_list", [])
                break

            # 00:06:31: Config Sync: Starting lines from MCL file:
            match_obj = p2.match(line)
            if match_obj:
                err_flag = True
                ret_dict.setdefault('err_list', []).append(line)
                continue

            # Append all the config-sync failures
            if err_flag:
                ret_dict["err_list"].append(line)
                continue

        return ret_dict


# =========================================================================
# Parser for 'show platform authentication sbinfo interface {interface} '
# =========================================================================

class ShowPlatformAuthenticationSbinfoInterfaceSchema(MetaParser):
    """Schema for show platform authentication sbinfo interface {interface}"""

    schema = {
        'sb_info': {
            'sb_access_vlan': int,
            'sb_voice_vlan': int,
            'conf_access_vlan': int,
            'conf_voice_vlan': int,
            'oper_access_vlan': int,
            'oper_voice_vlan': int,
            'def_host_access': int,
            'auth_in_vp': bool,
            'client_count': int,
            'vlan_count': int,
            'port_ctrl_enable': bool,
            'cdp_bypass_enable': bool,
            'port_mode': str,
            'ctrl_dir': str,
        },
        'mac': {
            Any(): {
                'int': str,
                'mac': str,
                'domain': str,
                'vlan': int,
                'clent_handle': str,
                'port_open': str,
                'flags': str,
            },
        },
        'int_vlan': {
            Any(): {
                'int': str,
                'vlan': int,
                'domain': str,
                'user_count': int,
                'fwd_count': int,
                'client_count': int,
                'vp_state': int,
                'flags': str,
            },
        },
    }

# =====================================================================
# Parser for 'show platform authentication sbinfo interface {interface} '
# ======================================================================
class ShowPlatformAuthenticationSbinfoInterface(ShowPlatformAuthenticationSbinfoInterfaceSchema):
    """Parser for show platform authentication sbinfo interface {interface}"""

    cli_command = 'show platform authentication sbinfo interface {interface}'

    def cli(self, interface, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(interface=interface))

        # SB Access Vlan: 1
        p1 = re.compile(r"^\s+SB\s+Access\s+Vlan:\s+(?P<sb_access_vlan>\d+)$")
        # SB Voice Vlan: 100
        p1_1 = re.compile(r"^\s+SB\s+Voice\s+Vlan:\s+(?P<sb_voice_vlan>\d+)$")
        # Conf Access Vlan: 1
        p1_2 = re.compile(r"^\s+Conf\s+Access\s+Vlan:\s+(?P<conf_access_vlan>\d+)$")
        # Conf Voice Vlan: 100
        p1_3 = re.compile(r"^\s+Conf\s+Voice\s+Vlan:\s+(?P<conf_voice_vlan>\d+)$")
        # Oper Access Vlan: 1
        p1_4 = re.compile(r"^\s+Oper\s+Access\s+Vlan:\s+(?P<oper_access_vlan>\d+)$")
        # Oper Voice Vlan: 100
        p1_5 = re.compile(r"^\s+Oper\s+Voice\s+Vlan:\s+(?P<oper_voice_vlan>\d+)$")
        # Default Host Access: 1
        p1_6 = re.compile(r"^\s+Default\s+Host\s+Access:\s+(?P<def_host_access>\d+)$")
        # Auth In VP: True
        p1_7 = re.compile(r"^\s+Auth\s+In\s+VP:\s+(?P<auth_in_vp>\w+)$")
        # Client Count : 1
        p1_8 = re.compile(r"^\s+Client\s+Count\s+:\s+(?P<client_count>\d+)$")
        # Vlan Count : 2
        p1_9 = re.compile(r"^\s+Vlan\s+Count\s+:\s+(?P<vlan_count>\d+)$")
        # Port-Control Auto Enabled : TRUE
        p1_10 = re.compile(r"^Port-Control\s+Auto\s+Enabled\s+:\s+(?P<port_ctrl_enable>\w+)$")
        # CDP Bypass Enabled : FALSE
        p1_11 = re.compile(r"^\s+CDP\s+Bypass\s+Enabled\s+:\s+(?P<cdp_bypass_enable>\w+)$")
        # Port Mode : CLOSED
        p1_12 = re.compile(r"^\s+Port\s+Mode\s+:\s+(?P<port_mode>\w+)$")
        # Control Direction : BOTH
        p1_13 = re.compile(r"^\s+Control\s+Direction\s+:\s+(?P<ctrl_dir>\w+)$")
        # Gi1/0/24  001b.0c18.918d    VOICE    100  0x94000008  0x0002  None
        p2 = re.compile(r"^\s+(?P<int>\S+)\s+(?P<mac>\S+)\s+(?P<domain>\w+)\s+(?P<vlan>\d+)\s+(?P<clent_handle>\S+)\s+(?P<port_open>\S+)\s+(?P<flags>\w+)$")
        # Gi1/0/24  1       DATA    1     0     0       2     None
        p3 = re.compile(r"^\s+(?P<int>\S+)\s+(?P<vlan>\d+)\s+(?P<domain>\w+)\s+(?P<user_count>\d+)\s+(?P<fwd_count>\d+)\s+(?P<client_count>\d+)\s+(?P<vp_state>\S+\s+)\s+(?P<flags>\w+)$")

        ret_dict = {}

        for line in output.splitlines():

            # SB Access Vlan: 1
            m = p1.match(line)
            if m:
                dict_val = m.groupdict()
                if 'sb_info' not in ret_dict:
                    sb_info = ret_dict.setdefault('sb_info', {})
                sb_info['sb_access_vlan'] = int(dict_val['sb_access_vlan'])
                continue

            # SB Voice Vlan: 100
            m = p1_1.match(line)
            if m:
                dict_val = m.groupdict()
                if 'sb_info' not in ret_dict:
                    sb_info = ret_dict.setdefault('sb_info', {})
                sb_info['sb_voice_vlan'] = int(dict_val['sb_voice_vlan'])
                continue

            # Conf Access Vlan: 1
            m = p1_2.match(line)
            if m:
                dict_val = m.groupdict()
                if 'sb_info' not in ret_dict:
                    sb_info = ret_dict.setdefault('sb_info', {})
                sb_info['conf_access_vlan'] = int(dict_val['conf_access_vlan'])
                continue

            # Conf Voice Vlan: 100
            m = p1_3.match(line)
            if m:
                dict_val = m.groupdict()
                if 'sb_info' not in ret_dict:
                    sb_info = ret_dict.setdefault('sb_info', {})
                sb_info['conf_voice_vlan'] = int(dict_val['conf_voice_vlan'])
                continue

            # Oper Access Vlan: 1
            m = p1_4.match(line)
            if m:
                dict_val = m.groupdict()
                if 'sb_info' not in ret_dict:
                    sb_info = ret_dict.setdefault('sb_info', {})
                sb_info['oper_access_vlan'] = int(dict_val['oper_access_vlan'])
                continue

            # Oper Voice Vlan: 100
            m = p1_5.match(line)
            if m:
                dict_val = m.groupdict()
                if 'sb_info' not in ret_dict:
                    sb_info = ret_dict.setdefault('sb_info', {})
                sb_info['oper_voice_vlan'] = int(dict_val['oper_voice_vlan'])
                continue

            # Default Host Access: 1
            m = p1_6.match(line)
            if m:
                dict_val = m.groupdict()
                if 'sb_info' not in ret_dict:
                    sb_info = ret_dict.setdefault('sb_info', {})
                sb_info['def_host_access'] = int(dict_val['def_host_access'])
                continue

            # Auth In VP: True
            m = p1_7.match(line)
            if m:
                dict_val = m.groupdict()
                if 'sb_info' not in ret_dict:
                    sb_info = ret_dict.setdefault('sb_info', {})
                sb_info['auth_in_vp'] = bool(dict_val['auth_in_vp'])
                continue

            # Client Count : 1
            m = p1_8.match(line)
            if m:
                dict_val = m.groupdict()
                if 'sb_info' not in ret_dict:
                    sb_info = ret_dict.setdefault('sb_info', {})
                sb_info['client_count'] = int(dict_val['client_count'])
                continue

            # Vlan Count : 2
            m = p1_9.match(line)
            if m:
                dict_val = m.groupdict()
                if 'sb_info' not in ret_dict:
                    sb_info = ret_dict.setdefault('sb_info', {})
                sb_info['vlan_count'] = int(dict_val['vlan_count'])
                continue

            # Port-Control Auto Enabled : TRUE
            m = p1_10.match(line)
            if m:
                dict_val = m.groupdict()
                if 'sb_info' not in ret_dict:
                    sb_info = ret_dict.setdefault('sb_info', {})
                sb_info['port_ctrl_enable'] = bool(dict_val['port_ctrl_enable'])
                continue

            # CDP Bypass Enabled : FALSE
            m = p1_11.match(line)
            if m:
                dict_val = m.groupdict()
                if 'sb_info' not in ret_dict:
                    sb_info = ret_dict.setdefault('sb_info', {})
                sb_info['cdp_bypass_enable'] = bool(dict_val['cdp_bypass_enable'])
                continue

            # Port Mode : CLOSED
            m = p1_12.match(line)
            if m:
                dict_val = m.groupdict()
                if 'sb_info' not in ret_dict:
                    sb_info = ret_dict.setdefault('sb_info', {})
                sb_info['port_mode'] = dict_val['port_mode']
                continue

            # Control Direction : BOTH
            m = p1_13.match(line)
            if m:
                dict_val = m.groupdict()
                if 'sb_info' not in ret_dict:
                    sb_info = ret_dict.setdefault('sb_info', {})
                sb_info['ctrl_dir'] = dict_val['ctrl_dir']
                continue

            # Gi1/0/24  001b.0c18.918d    VOICE    100  0x94000008  0x0002  None
            m = p2.match(line)
            if m:
                dict_val = m.groupdict()
                int_var = dict_val['int']
                if 'mac' not in ret_dict:
                    mac = ret_dict.setdefault('mac', {})
                if int_var not in ret_dict['mac']:
                    int_dict = ret_dict['mac'].setdefault(int_var, {})
                int_dict['int'] = dict_val['int']
                int_dict['mac'] = dict_val['mac']
                int_dict['domain'] = dict_val['domain']
                int_dict['vlan'] = int(dict_val['vlan'])
                int_dict['clent_handle'] = dict_val['clent_handle']
                int_dict['port_open'] = dict_val['port_open']
                int_dict['flags'] = dict_val['flags']
                continue

            # Gi1/0/24  1       DATA    1     0     0       2     None
            m = p3.match(line)
            if m:
                dict_val = m.groupdict()
                vlan_var = dict_val['vlan']
                if 'int_vlan' not in ret_dict:
                    int_vlan = ret_dict.setdefault('int_vlan', {})
                if vlan_var not in ret_dict['int_vlan']:
                    vlan_dict = ret_dict['int_vlan'].setdefault(vlan_var, {})
                vlan_dict['int'] = dict_val['int']
                vlan_dict['vlan'] = int(dict_val['vlan'])
                vlan_dict['domain'] = dict_val['domain']
                vlan_dict['user_count'] = int(dict_val['user_count'])
                vlan_dict['fwd_count'] = int(dict_val['fwd_count'])
                vlan_dict['client_count'] = int(dict_val['client_count'])
                vlan_dict['vp_state'] = int(dict_val['vp_state'])
                vlan_dict['flags'] = dict_val['flags']
                continue


        return ret_dict


# ======================================================
# Schema for 'show platform host-access-table {interface} '
# ======================================================

class ShowPlatformHostAccessTableIntfSchema(MetaParser):
    """Schema for show platform host-access-table <intf>"""

    schema = {
        'host_access': {
            Any(): {
                'src_address': str,
                'vlan_id': int,
                'access_mode': str,
                'feature': str,
                'type': str,
            },
            'current_feature': str,
            'default': str,
        },
    }

class ShowPlatformHostAccessTableIntf(ShowPlatformHostAccessTableIntfSchema):
    """Parser for show platform host-access-table <intf>"""

    cli_command = 'show platform host-access-table {intf}'

    def cli(self, intf=None, output=None):
        if output is None:
            cmd = self.cli_command.format(intf=intf)
            output = self.device.execute(cmd)

        # 001b.0c18.918d       100         permit         dot1x        dynamic
        p1 = re.compile(r"^(?P<src_address>\S+)\s+(?P<vlan_id>\d+)\s+(?P<access_mode>\w+)\s+(?P<feature>\S+)\s+(?P<type>\w+)$")
        # Current feature:  dot1x
        p1_1 = re.compile(r"^Current\s+feature:\s+(?P<current_feature>\S+)$")
        # Default            ask
        p1_2 = re.compile(r"^Default\s+(?P<default>\w+)$")

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # 001b.0c18.918d       100         permit         dot1x        dynamic
            m = p1.match(line)
            if m:
                dict_val = m.groupdict()
                vlan_id_var = dict_val['vlan_id']
                if 'host_access' not in ret_dict:
                    host_access = ret_dict.setdefault('host_access', {})
                if vlan_id_var not in ret_dict['host_access']:
                    vlan_id_dict = ret_dict['host_access'].setdefault(vlan_id_var, {})
                vlan_id_dict['src_address'] = dict_val['src_address']
                vlan_id_dict['vlan_id'] = int(dict_val['vlan_id'])
                vlan_id_dict['access_mode'] = dict_val['access_mode']
                vlan_id_dict['feature'] = dict_val['feature']
                vlan_id_dict['type'] = dict_val['type']
                continue

            # Current feature:  dot1x
            m = p1_1.match(line)
            if m:
                dict_val = m.groupdict()
                if 'host_access' not in ret_dict:
                    host_access = ret_dict.setdefault('host_access', {})
                host_access['current_feature'] = dict_val['current_feature']
                continue

            # Default            ask
            m = p1_2.match(line)
            if m:
                dict_val = m.groupdict()
                if 'host_access' not in ret_dict:
                    host_access = ret_dict.setdefault('host_access', {})
                host_access['default'] = dict_val['default']
                continue


        return ret_dict


# ======================================================
# Schema for 'show platform pm port-data <int> '
# ======================================================

class ShowPlatformPmPortDataIntSchema(MetaParser):
    """Schema for show platform pm port-data <int>"""

    schema = {
        Optional('pm_port_data'): {
            Any(): {
                Optional('field'): str,
                Optional('admin_field'): str,
                Optional('oper_field'): str,
            },

        },
        Optional('pm_port_info'): {
            Optional('forwarding_vlans'): int,
            Optional('current_pruned_vlans'): str,
            Optional('previous_pruned_vlans'): str,
            Optional('sw_linkneg_state'): str,
            Optional('no_link_down_events'): int,
            Optional('time_stamp_last_link_flapped'): str,
            Optional('last_link_down_duration_secs'): int,
            Optional('last_link_up_duration_secs'): int,
        },
    }

# ======================================================
# Parser for 'show platform pm port-data <int> '
# ======================================================
class ShowPlatformPmPortDataInt(ShowPlatformPmPortDataIntSchema):
    """Parser for show platform pm port-data <int>"""

    cli_command = 'show platform pm port-data {interface}'

    def cli(self, interface=None, output=None):
        if output is None:
            cmd = self.cli_command.format(interface=interface)
            output = self.device.execute(cmd)

        #   Access Mode               Multi-Static         Multi-Static
        p1 = re.compile(r"^\s+(?P<field>(\w+|\w+\s+\w+|\w+\s+\w+\s+\w+)?)\s+(?P<admin_field>(\S+|\s+)?)\s+(?P<oper_field>(\S+|s+)?)$")

        #   Forwarding Vlans : 100
        p2 = re.compile(r"^\s+Forwarding\s+Vlans\s+:\s+(?P<forwarding_vlans>\d+)$")
        #   Current Pruned Vlans : none
        p2_1 = re.compile(r"^\s+Current\s+Pruned\s+Vlans\s+:\s+(?P<current_pruned_vlans>\w+)$")
        #   Previous Pruned Vlans : none
        p2_2 = re.compile(r"^\s+Previous\s+Pruned\s+Vlans\s+:\s+(?P<previous_pruned_vlans>\w+)$")
        #   Sw LinkNeg State : LinkStateUp
        p2_3 = re.compile(r"^\s+Sw\s+LinkNeg\s+State\s+:\s+(?P<sw_linkneg_state>\w+)$")
        #   No.of LinkDownEvents :    3
        p2_4 = re.compile(r"^\s+No\.of\s+LinkDownEvents\s+:\s+(?P<no_link_down_events>\d+)\s+$")
        #   Time Stamp Last Link Flapped(U) : Sep 13 20:14:35.714
        p2_5 = re.compile(r"^\s+Time\s+Stamp\s+Last\s+Link\s+Flapped\(U\)\s+:\s+(?P<time_stamp_last_link_flapped>\S+\s+\S+\s+\S+)$")
        #   LastLinkDownDuration(sec) 2
        p2_6 = re.compile(r"^\s+LastLinkDownDuration\(sec\)\s+(?P<last_link_down_duration_secs>\d+)\s+$")
        #   LastLinkUpDuration(sec):  1355054
        p2_7 = re.compile(r"^\s+LastLinkUpDuration\(sec\):\s+(?P<last_link_up_duration_secs>\d+)\s+$")

        ret_dict = {}

        for line in output.splitlines():

            #   Access Mode               Multi-Static         Multi-Static
            m = p1.match(line)
            if m:
                dict_val = m.groupdict()
                field_var = dict_val['field']
                if 'pm_port_data' not in ret_dict:
                    pm_port_data = ret_dict.setdefault('pm_port_data', {})
                if field_var not in ret_dict['pm_port_data']:
                    field_dict = ret_dict['pm_port_data'].setdefault(field_var, {})
                field_dict['field'] = dict_val['field']
                field_dict['admin_field'] = dict_val['admin_field']
                field_dict['oper_field'] = dict_val['oper_field']
                continue


            #   Forwarding Vlans : 100
            m = p2.match(line)
            if m:
                dict_val = m.groupdict()
                if 'pm_port_info' not in ret_dict:
                    pm_port_info = ret_dict.setdefault('pm_port_info', {})
                pm_port_info['forwarding_vlans'] = int(dict_val['forwarding_vlans'])
                continue

            #   Current Pruned Vlans : none
            m = p2_1.match(line)
            if m:
                dict_val = m.groupdict()
                if 'pm_port_info' not in ret_dict:
                    pm_port_info = ret_dict.setdefault('pm_port_info', {})
                pm_port_info['current_pruned_vlans'] = dict_val['current_pruned_vlans']
                continue

            #   Previous Pruned Vlans : none
            m = p2_2.match(line)
            if m:
                dict_val = m.groupdict()
                if 'pm_port_info' not in ret_dict:
                    pm_port_info = ret_dict.setdefault('pm_port_info', {})
                pm_port_info['previous_pruned_vlans'] = dict_val['previous_pruned_vlans']
                continue

            #   Sw LinkNeg State : LinkStateUp
            m = p2_3.match(line)
            if m:
                dict_val = m.groupdict()
                if 'pm_port_info' not in ret_dict:
                    pm_port_info = ret_dict.setdefault('pm_port_info', {})
                pm_port_info['sw_linkneg_state'] = dict_val['sw_linkneg_state']
                continue

            #   No.of LinkDownEvents :    3
            m = p2_4.match(line)
            if m:
                dict_val = m.groupdict()
                if 'pm_port_info' not in ret_dict:
                    pm_port_info = ret_dict.setdefault('pm_port_info', {})
                pm_port_info['no_link_down_events'] = int(dict_val['no_link_down_events'])
                continue

            #   Time Stamp Last Link Flapped(U) : Sep 13 20:14:35.714
            m = p2_5.match(line)
            if m:
                dict_val = m.groupdict()
                if 'pm_port_info' not in ret_dict:
                    pm_port_info = ret_dict.setdefault('pm_port_info', {})
                pm_port_info['time_stamp_last_link_flapped'] = dict_val['time_stamp_last_link_flapped']
                continue

            #   LastLinkDownDuration(sec) 2

            m = p2_6.match(line)
            if m:
                dict_val = m.groupdict()
                if 'pm_port_info' not in ret_dict:
                    pm_port_info = ret_dict.setdefault('pm_port_info', {})
                pm_port_info['last_link_down_duration_secs'] = int(dict_val['last_link_down_duration_secs'])
                continue

            #   LastLinkUpDuration(sec):  1355054
            m = p2_7.match(line)
            if m:
                dict_val = m.groupdict()
                if 'pm_port_info' not in ret_dict:
                    pm_port_info = ret_dict.setdefault('pm_port_info', {})
                pm_port_info['last_link_up_duration_secs'] = int(dict_val['last_link_up_duration_secs'])
                continue


        return ret_dict


class ShowPlatformRewriteUtilizationSchema(MetaParser):
    """Schema for show platform hardware fed active fwd-asic resource rewrite utilization """
    schema = {
        'asic': {
            Any(): {
                'rewritedata': {
                    Any(): {
                        'allocated': int,
                        'free': int,
                          }
                   }
            }
        }
    }


class ShowPlatformRewriteUtilization(ShowPlatformRewriteUtilizationSchema):
    """Parser for show platform hardware fed sw active fwd-asic resource rewrite utilization """

    cli_command = ['show platform hardware fed {switch} active fwd-asic resource rewrite utilization','show platform hardware fed active fwd-asic resource rewrite utilization']

    def cli(self, output=None, switch=''):
        if output is None:
            if switch:
                cmd = self.cli_command[0].format(switch=switch)
            else:
                cmd = self.cli_command[1]
            output = self.device.execute(cmd)

        # initial return dictionary
        ret_dict = {}
        # initial regexp pattern
        # Resource Info for ASIC Instance: 0
        p1 = re.compile(r'Resource +Info +for +ASIC +Instance: +(?P<asic>(\d+))$')

        #Rewrite Data                        Allocated     Free
        #-------------------------------------------------------
        #PHF_EGRESS_destMacAddress             75001       23303
        #UDP_ENCAP_SRC_PORT                        0         256
        p2 = re.compile(r'(?P<rewritedata>\S+) +(?P<allocated>\S+) +(?P<free>\S+)$')
        for line in output.splitlines():
            line = line.strip()

            # Resource Info for ASIC Instance: 0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                asic = group['asic']
                asic_dict = ret_dict.setdefault('asic', {}).setdefault(asic, {})
                continue

            #PHF_EGRESS_destMacAddress             75001       23303
            #UDP_ENCAP_SRC_PORT                        0         256

            m = p2.match(line)
            if m:
                groups = m.groupdict()
                rewritedata = (groups['rewritedata'])
                allocated = int(groups['allocated'])
                free = int(groups['free'])
                rewrite_table_dict = asic_dict.setdefault('rewritedata', {}).setdefault(rewritedata, {})

                rewrite_table_dict.update({
                    'allocated': allocated,
                    'free': free,
                })
                continue
        return ret_dict

class ShowPlatformMatmMacTableSchema(MetaParser):
    """Schema for show platform hardware fed switch active matm macTable"""
    schema = {
        'mac_address': {
            Any(): {
                'head': {
                    'vlan': int
                },
                'key': {
                    'vlan': int,
                    'mac': str,
                    'l3_if': int,
                    'gpn': int,
                    'epoch': int,
                    'static': int,
                    'flood_en': int,
                    'vlan_lead_wless_flood_en': int,
                    'client_home_asic': int,
                    'learning_peerid': int,
                    'learning_peerid_valid': int
                },
                'mask': {
                    'vlan': int,
                    'mac': str,
                    'l3_if': int,
                    'gpn': int,
                    'epoch': int,
                    'static': int,
                    'flood_en': int,
                    'vlan_lead_wless_flood_en': int,
                    'client_home_asic': int,
                    'learning_peerid': int,
                    'learning_peerid_valid': int
                },
                'src_ad': {
                    'need_to_learn': int,
                    'lrn_v': int,
                    'catchall': int,
                    'static_mac': int,
                    'chain_ptr_v': int,
                    'chain_ptr': int,
                    'static_entry_v': int,
                    'auth_state': int,
                    'auth_mode': int,
                    'traf_mode': int,
                    'is_src_ce': int
                },
                'dst_ad': {
                    'si': str,
                    'bridge': int,
                    'replicate': int,
                    'blk_fwd_o': int,
                    'v4_mac': int,
                    'v6_mac': int,
                    'catchall': int,
                    'ign_src_lrn': int,
                    'port_mask_o': int,
                    'afd_cli_f': int,
                    'afd_lbl': int,
                    'priority': int,
                    'dest_mod_idx':int,
                    'destined_to_us': int,
                    'pv_trunk': int
                }
            }
        },
        'total_mac_address': int
    }


class ShowPlatformMatmMacTable(ShowPlatformMatmMacTableSchema):
    """Parser for show platform hardware fed switch active matm macTable"""

    cli_command = 'show platform hardware fed switch active matm macTable'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # HEAD: MAC address 0012.7fae.9662 in VLAN 1
        p1 = re.compile(r'^HEAD:\s+MAC\s+address\s+(?P<mac_address>[\d\.a-f]+)\s+in\s+VLAN\s+(?P<vlan>\d+)$')

        # KEY: vlan 4, mac 0x127fae9662, l3_if 0, gpn 24, epoch 0, static 0, flood_en 0, vlan_lead_wless_flood_en 0,
        # client_home_asic 0, learning_peerid 0, learning_peerid_valid 0
        p2 = re.compile(r'^(?P<key_mask>(KEY|MASK)):\s+vlan\s+(?P<vlan>\d+),\s+mac\s+(?P<mac>\S+),\s+l3_if\s+(?P<l3_if>\d+),\s+gpn\s+(?P<gpn>\d+),'
        r'\s+epoch\s+(?P<epoch>\d+),\s+static\s+(?P<static>\d+),\s+flood_en\s+(?P<flood_en>\d+),\s+vlan_lead_wless_flood_en'
        r'\s+(?P<vlan_lead_wless_flood_en>\d+),\s+client_home_asic\s+(?P<client_home_asic>\d+),*\s+learning_peerid\s+(?P<learning_peerid>\d+),'
        r'\s+learning_peerid_valid\s+(?P<learning_peerid_valid>\d+)$')

        # SRC_AD: need_to_learn 0, lrn_v 0, catchall 0, static_mac 0, chain_ptr_v 0, chain_ptr 0, static_entry_v 0,
        # auth_state 0, auth_mode 0, traf_mode 0, is_src_ce 0
        p3 = re.compile(r'^SRC_AD:\s+need_to_learn\s+(?P<need_to_learn>\d+),\s+lrn_v\s+(?P<lrn_v>\d+),\s+catchall\s+(?P<catchall>\d+),'
        r'\s+static_mac\s+(?P<static_mac>\d+),\s+chain_ptr_v\s+(?P<chain_ptr_v>\d+),\s+chain_ptr\s+(?P<chain_ptr>\d+),\s+static_entry_v'
        r'\s+(?P<static_entry_v>\d+),\s+auth_state\s+(?P<auth_state>\d+),\s+auth_mode\s+(?P<auth_mode>\d+),\s+traf_mode\s+(?P<traf_mode>\d+),'
        r'\s+is_src_ce\s+(?P<is_src_ce>\d+)$')

        # DST_AD: si 0xb1, bridge 0, replicate 0, blk_fwd_o 0, v4_mac 0, v6_mac 0, catchall 0, ign_src_lrn 0, port_mask_o 0,
        # afd_cli_f 0, afd_lbl 0, priority 3, dest_mod_idx 0, destined_to_us 0, pv_trunk 0
        p4 = re.compile(r'^DST_AD:\s+si\s+(?P<si>\S+),\s+bridge\s+(?P<bridge>\d+),\s+replicate\s+(?P<replicate>\d+),\s+blk_fwd_o\s+(?P<blk_fwd_o>\d+),'
        r'\s+v4_mac\s+(?P<v4_mac>\d+),\s+v6_mac\s+(?P<v6_mac>\d+),\s+catchall\s+(?P<catchall>\d+),\s+ign_src_lrn\s+(?P<ign_src_lrn>\d+),\s+port_mask_o'
        r'\s+(?P<port_mask_o>\d+),\s+afd_cli_f\s+(?P<afd_cli_f>\d+),\s+afd_lbl\s+(?P<afd_lbl>\d+),\s+priority\s+(?P<priority>\d+),\s+'
        r'dest_mod_idx\s+(?P<dest_mod_idx>\d+),\s+destined_to_us\s+(?P<destined_to_us>\d+),\s+pv_trunk\s+(?P<pv_trunk>\d+)$')

        # Total Mac number of addresses:: 6
        p5 = re.compile(r'^Total\s+Mac\s+number\s+of\s+addresses::\s+(?P<total_mac_address>\d+)$')

        ret_dict = dict()

        for line in output.splitlines():
            line = line.strip()

            # HEAD: MAC address 0012.7fae.9662 in VLAN 1
            m = p1.match(line)
            if m:
                mac_dict = ret_dict.setdefault('mac_address', {}).setdefault(m.groupdict()['mac_address'], {})
                mac_dict.setdefault('head', {}).setdefault('vlan', int(m.groupdict()['vlan']))
                continue

            # KEY: vlan 4, mac 0x127fae9662, l3_if 0, gpn 24, epoch 0, static 0, flood_en 0, vlan_lead_wless_flood_en 0,
            # client_home_asic 0, learning_peerid 0, learning_peerid_valid 0
            m = p2.match(line)
            if m:
                grp_dict = m.groupdict()
                tmp_dict = mac_dict.setdefault('key' if grp_dict['key_mask'] == 'KEY' else 'mask', {})
                tmp_dict['vlan'] = int(grp_dict['vlan'])
                tmp_dict['mac'] = grp_dict['mac']
                tmp_dict['l3_if'] = int(grp_dict['l3_if'])
                tmp_dict['gpn'] = int(grp_dict['gpn'])
                tmp_dict['epoch'] = int(grp_dict['epoch'])
                tmp_dict['static'] = int(grp_dict['static'])
                tmp_dict['flood_en'] = int(grp_dict['flood_en'])
                tmp_dict['vlan_lead_wless_flood_en'] = int(grp_dict['vlan_lead_wless_flood_en'])
                tmp_dict['client_home_asic'] = int(grp_dict['client_home_asic'])
                tmp_dict['learning_peerid'] = int(grp_dict['learning_peerid'])
                tmp_dict['learning_peerid_valid'] = int(grp_dict['learning_peerid_valid'])
                continue

            # SRC_AD: need_to_learn 0, lrn_v 0, catchall 0, static_mac 0, chain_ptr_v 0, chain_ptr 0, static_entry_v 0,
            # auth_state 0, auth_mode 0, traf_mode 0, is_src_ce 0
            m = p3.match(line)
            if m:
                grp_dict = m.groupdict()
                src_dict = mac_dict.setdefault('src_ad', {})
                src_dict['need_to_learn'] = int(grp_dict['need_to_learn'])
                src_dict['lrn_v'] = int(grp_dict['lrn_v'])
                src_dict['catchall'] = int(grp_dict['catchall'])
                src_dict['static_mac'] = int(grp_dict['static_mac'])
                src_dict['chain_ptr_v'] = int(grp_dict['chain_ptr_v'])
                src_dict['chain_ptr'] = int(grp_dict['chain_ptr'])
                src_dict['static_entry_v'] = int(grp_dict['static_entry_v'])
                src_dict['auth_state'] = int(grp_dict['auth_state'])
                src_dict['auth_mode'] = int(grp_dict['auth_mode'])
                src_dict['traf_mode'] = int(grp_dict['traf_mode'])
                src_dict['is_src_ce'] = int(grp_dict['is_src_ce'])
                continue

            # DST_AD: si 0xb1, bridge 0, replicate 0, blk_fwd_o 0, v4_mac 0, v6_mac 0, catchall 0, ign_src_lrn 0, port_mask_o 0,
            # afd_cli_f 0, afd_lbl 0, priority 3, dest_mod_idx 0, destined_to_us 0, pv_trunk 0
            m = p4.match(line)
            if m:
                grp_dict = m.groupdict()
                dst_dict = mac_dict.setdefault('dst_ad', {})
                dst_dict['si'] = grp_dict['si']
                dst_dict['bridge'] = int(grp_dict['bridge'])
                dst_dict['replicate'] = int(grp_dict['replicate'])
                dst_dict['blk_fwd_o'] = int(grp_dict['blk_fwd_o'])
                dst_dict['v4_mac'] = int(grp_dict['v4_mac'])
                dst_dict['v6_mac'] = int(grp_dict['v6_mac'])
                dst_dict['catchall'] = int(grp_dict['catchall'])
                dst_dict['ign_src_lrn'] = int(grp_dict['ign_src_lrn'])
                dst_dict['port_mask_o'] = int(grp_dict['port_mask_o'])
                dst_dict['afd_cli_f'] = int(grp_dict['afd_cli_f'])
                dst_dict['afd_lbl'] = int(grp_dict['afd_lbl'])
                dst_dict['priority'] = int(grp_dict['priority'])
                dst_dict['dest_mod_idx'] = int(grp_dict['dest_mod_idx'])
                dst_dict['destined_to_us'] = int(grp_dict['destined_to_us'])
                dst_dict['pv_trunk'] = int(grp_dict['pv_trunk'])
                continue

            # Total Mac number of addresses:: 6
            m = p5.match(line)
            if m:
                ret_dict['total_mac_address'] = int(m.groupdict()['total_mac_address'])
                continue

        return ret_dict

class ShowSwitchStackRingSpeedSchema(MetaParser):
    """Schema for show switch stack-ring speed"""

    schema = {
        'speed': str,
        'configuration': str,
        'protocol': str
    }


class ShowSwitchStackRingSpeed(ShowSwitchStackRingSpeedSchema):
    """Parser for show switch stack-ring speed"""

    cli_command = 'show switch stack-ring speed'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Stack Ring Speed        : 240G
        p1 = re.compile(r'^Stack\s+Ring\s+Speed\s+:\s+(?P<speed>\w+)$')

        # Stack Ring Configuration: Half
        p2 = re.compile(r'^Stack\s+Ring\s+Configuration:\s+(?P<configuration>\w+)$')

        # Stack Ring Protocol     : StackWise
        p3 = re.compile(r'^Stack\s+Ring\s+Protocol\s+:\s+(?P<protocol>\w+)$')

        ret_dict = dict()

        for line in output.splitlines():
            line = line.strip()

            match = p1.match(line)
            if match:
                ret_dict.update(match.groupdict())
                continue

            match = p2.match(line)
            if match:
                ret_dict.update(match.groupdict())
                continue

            match = p3.match(line)
            if match:
                ret_dict.update(match.groupdict())
                continue

        return ret_dict

class ShowPlatformUsbStatusSchema(MetaParser):
    '''Schema for show platform usb status'''
    schema = {
        'status': str
    }


class ShowPlatformUsbStatus(ShowPlatformUsbStatusSchema):
    '''Parser for show platform usb status'''

    cli_command = 'show platform usb status'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # USB enabled
        p1 = re.compile(r'^USB\s+(?P<status>\S+)$')

        ret_dict = dict()

        for line in output.splitlines():
            line = line.strip()

            # USB enabled
            m = p1.match(line)
            if m:
                ret_dict.update(m.groupdict())
                continue

        return ret_dict


# Parser for 'show platform pm interface-numbers '
# ======================================================

class ShowPlatformPmInterfaceNumbersSchema(MetaParser):
    """Schema for show platform pm interface-numbers"""
    schema = {
        'interfaces': {
            Any(): {
                'interface': str,
                'iif_id': int,
                'gid': int,
                'slot': int,
                'unit': int,
                'slun': int,
                'hwidb_ptr': str,
                'status': str,
                'status2': str,
                'state': str,
                'snmp_if_index': int,
            },
        },
    }

class ShowPlatformPmInterfaceNumbers(ShowPlatformPmInterfaceNumbersSchema):
    """Parser for show platform pm interface-numbers"""

    cli_command = 'show platform pm interface-numbers'
    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Gi1/0/1       9  1    1    1    1    0x7F2C5B930F40 0x10040    0x20001B   0x4        9

        p1 = re.compile(r"^(?P<interface>\S+)\s+(?P<iif_id>\d+)\s+(?P<gid>\d+)\s+(?P<slot>\d+)\s+(?P<unit>\d+)\s+(?P<slun>\d+)\s+(?P<hwidb_ptr>\S+)\s+(?P<status>\S+)\s+(?P<status2>\S+)\s+(?P<state>\S+)\s+(?P<snmp_if_index>\d+)$")
        ret_dict = {}
        for line in output.splitlines():
            line = line.strip()
            # Gi1/0/1       9  1    1    1    1    0x7F2C5B930F40 0x10040    0x20001B   0x4        9
            m = p1.match(line)
            if m:
                dict_val = m.groupdict()
                interface_var = dict_val['interface']
                if 'interfaces' not in ret_dict:
                    interfaces = ret_dict.setdefault('interfaces', {})
                if interface_var not in ret_dict['interfaces']:
                    interface_dict = ret_dict['interfaces'].setdefault(interface_var, {})
                interface_dict['interface'] = dict_val['interface']
                interface_dict['iif_id'] = int(dict_val['iif_id'])
                interface_dict['gid'] = int(dict_val['gid'])
                interface_dict['slot'] = int(dict_val['slot'])
                interface_dict['unit'] = int(dict_val['unit'])
                interface_dict['slun'] = int(dict_val['slun'])
                interface_dict['hwidb_ptr'] = dict_val['hwidb_ptr']
                interface_dict['status'] = dict_val['status']
                interface_dict['status2'] = dict_val['status2']
                interface_dict['state'] = dict_val['state']
                interface_dict['snmp_if_index'] = int(dict_val['snmp_if_index'])
                continue

        return ret_dict


# ====================
# Schema for:
#  * 'show processes <pid>'
# ====================
class ShowProcessesPidSchema(MetaParser):
    ''' Schema for "show processes <pid>" '''

    schema = {
        'pid': int,
        'process_name': str,
        'tty': int,
        'memory_usage': {
            'holding': int,
            'maximum': int,
            'allocated': int,
            'freed': int,
            'getbufs': int,
            'retbufs': int,
            'stack': str,
        },
        'cpu_usage': {
            'pc': str,
            'invoked': int,
            'giveups': int,
            'u_sec': int,
            '5sec_percent': float,
            '1min_percent': float,
            '5min_percent': float,
            'average': float,
            'age': int,
            'runtime': int,
            'state': str,
            'priority': str,
        }
    }

# ====================
# Parser for:
#  * 'show processes <pid>'
# ====================
class ShowProcessesPid(ShowProcessesPidSchema):
    ''' Parser for "show processes <processid>" '''

    # Process ID 3 [Network Synchronization Selection Control Process], TTY 0
    # Memory usage [in bytes]
    #   Holding: 41960, Maximum: 0, Allocated: 0, Freed: 0
    #   Getbufs: 0, Retbufs: 0, Stack: 34240/36000
    # CPU usage
    #   PC: 64448F4868F5, Invoked: 1, Giveups: 0, uSec: 0
    #   5Sec: 0.00%, 1Min: 0.00%, 5Min: 0.00%, Average: 0.00%
    #   Age: 511941589 msec, Runtime: 0 msec
    #   State: Waiting for Event, Priority: Critical

    cli_command = 'show processes {processid}'

    # Define a function to run the cli_command
    def cli(self, processid=None, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(processid=processid))

        parsed_dict = {}

        # Define RegExes for each possible kind of line

        # Process ID 3 [Network Synchronization Selection Control Process], TTY 0
        p1 = re.compile(r'^Process +ID +(?P<pid>(\S+)) +\[ *(?P<process_name>([ a-zA-Z0-9]+)) *\], TTY +(?P<tty>(\S+))$')

        #   Holding: 41960, Maximum: 0, Allocated: 0, Freed: 0
        p2 = re.compile(r'^Holding: +(?P<holding>(\d+)), +Maximum: +(?P<maximum>(\d+)), +Allocated: +(?P<allocated>(\d+)), +Freed: +(?P<freed>(\d+))$')

        #   Getbufs: 0, Retbufs: 0, Stack: 34240/36000
        p3 = re.compile(r'^Getbufs: +(?P<getbufs>(\d+)), +Retbufs: +(?P<retbufs>(\d+)), Stack: +(?P<stack>(\S+))$')

        #   PC: 64448F4868F5, Invoked: 1, Giveups: 0, uSec: 0
        p4 = re.compile(r'^PC: +(?P<pc>(\S+)), +Invoked: +(?P<invoked>(\d+)), Giveups: +(?P<giveups>(\d+)), uSec: (?P<u_sec>(\d+))$')

        #   5Sec: 0.00%, 1Min: 0.00%, 5Min: 0.00%, Average: 0.00%
        p5 = re.compile(r'^5Sec: +(?P<five_sec_percent>(\S+))%, +1Min: +(?P<one_min_percent>(\S+))%, +5Min: +(?P<five_min_percent>(\S+))%, +Average: +(?P<average>(\S+))%$')

        #   Age: 511941589 msec, Runtime: 0 msec
        p6 = re.compile(r'^Age: +(?P<age>(\S+)) msec, +Runtime: +(?P<runtime>(\d+)) msec$')

        #   State: Waiting for Event, Priority: Critical
        p7 = re.compile(r'^State: +(?P<state>([ a-zA-Z0-9]+)), +Priority: +(?P<priority>(\S+))$')


        # Iterate over output lines to check which pattern is matched

        for line in output.splitlines():
            line = line.strip()

            # Try matching pattern 1
            # Process ID 3 [Network Synchronization Selection Control Process], TTY 0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                parsed_dict.setdefault('pid',int(group["pid"]))
                parsed_dict.setdefault('process_name',group["process_name"])
                parsed_dict.setdefault('tty',int(group["tty"]))
                continue


            # Try matching pattern 2
            #   Holding: 41960, Maximum: 0, Allocated: 0, Freed: 0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                memory_usage_dict = parsed_dict.setdefault('memory_usage',{})
                memory_usage_dict.update({
                    'holding': int(group["holding"]),
                    'maximum':int(group["maximum"]),
                    'allocated':int(group["allocated"]),
                    'freed':int(group["freed"])
                })
                continue

            # Try matching pattern 3
            #   Getbufs: 0, Retbufs: 0, Stack: 34240/36000
            m = p3.match(line)
            if m:
                group = m.groupdict()
                memory_usage_dict = parsed_dict.setdefault('memory_usage',{})
                memory_usage_dict.update({
                    'getbufs':int(group["getbufs"]),
                    'retbufs':int(group["retbufs"]),
                    'stack':group["stack"]
                })
                continue

            # Try matching pattern 4
            #   PC: 64448F4868F5, Invoked: 1, Giveups: 0, uSec: 0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                cpu_usage_dict = parsed_dict.setdefault("cpu_usage",{})
                cpu_usage_dict.update({
                    'pc':group["pc"],
                    'invoked':int(group["invoked"]),
                    'giveups':int(group["giveups"]),
                    'u_sec':int(group["u_sec"])
                })
                continue

            # Try matching pattern 5
            #   5Sec: 0.00%, 1Min: 0.00%, 5Min: 0.00%, Average: 0.00%
            m = p5.match(line)
            if m:
                group = m.groupdict()
                cpu_usage_dict = parsed_dict.setdefault("cpu_usage",{})
                cpu_usage_dict.update({
                    '5sec_percent':float(group["five_sec_percent"]),
                    '1min_percent':float(group["one_min_percent"]),
                    '5min_percent':float(group["five_min_percent"]),
                    'average':float(group["average"])
                })
                continue

            # Try matching pattern 6
            #   Age: 511941589 msec, Runtime: 0 msec
            m = p6.match(line)
            if m:
                group = m.groupdict()
                cpu_usage_dict = parsed_dict.setdefault("cpu_usage",{})
                cpu_usage_dict.update({
                    'age': int(group["age"]),
                    'runtime': int(group["runtime"])
                })
                continue

            # Try matching pattern 7
            #   State: Waiting for Event, Priority: Critical
            m = p7.match(line)
            if m:
                group = m.groupdict()
                cpu_usage_dict = parsed_dict.setdefault("cpu_usage",{})
                cpu_usage_dict.update({
                    'state': group["state"],
                    'priority': group["priority"]
                })
                continue



        return parsed_dict

# ==========================================================================================
# Parser Schema for 'show xfsu eligibility'
# ==========================================================================================

class ShowXfsuEligibilitySchema(MetaParser):
    """
    Schema for
        * 'show xfsu eligibility'
    """

    schema = {
        'reload_fast_supported': str,
        'reload_fast_platform_stauts': str,
        'stack_configuration': str,
        'eligibility_check': {
            Any(): {
                'status': str
            },
            'spanning_tree':{
                'status': str,
                Optional(Any()): str
            }
        }
    }

# ==========================================================================================
# Parser for 'show xfsu eligibility
# ==========================================================================================

class ShowXfsuEligibility(ShowXfsuEligibilitySchema):
    """
    Parser for
        * 'show xfsu eligibility'
    """
    cli_command = 'show xfsu eligibility'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        #Reload fast supported: Yes
        p1 = re.compile(r'^Reload fast supported: (?P<reload_fast_supported>\w+)$')
        #Reload Fast PLATFORM Status: Not started yet
        p2 = re.compile(r'^Reload Fast PLATFORM Status: (?P<platform_status>[\w\s]+)$')
        #Stack Configuration: Yes
        p3 = re.compile(r'^Stack Configuration: (?P<stack_configuration>\w+)$')
        #Eligibility Check         Status
        #=================         ======
        #Autoboot Enabled          Yes
        #Install Mode              Yes
        #Network Advantage License Yes
        #Full ring stack           Yes
        #Check macsec eligibility  Eligible
        p4 = re.compile(r'^(?P<eligibility_check>[\w+ ]+) +(?P<status>Yes|No|Eligible|Ineligible)$')
        #Spanning Tree             Ineligible:Root Switch with forwarding link:VLAN0069
        p5 = re.compile(r'^Spanning Tree\s+(?P<spanning_tree>\w+):(?P<status>[\w ]+):(?P<forwarding_link>\S+)$')
        ret_dict = {}
        for line in output.splitlines():
            line = line.strip()
            #Reload fast supported: Yes
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['reload_fast_supported'] = group['reload_fast_supported']
                continue

            #Reload Fast PLATFORM Status: Not started yet
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict['reload_fast_platform_stauts'] = group['platform_status']
                continue
            #Stack Configuration: Yes
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict['stack_configuration'] = group['stack_configuration']
                continue
            #Eligibility Check         Status
            #=================         ======
            #Autoboot Enabled          Yes
            #Install Mode              Yes
            #Network Advantage License Yes
            #Full ring stack           Yes
            #Check macsec eligibility  Eligible
            m = p4.match(line)
            if m:
                group = m.groupdict()
                root_dict = ret_dict.setdefault('eligibility_check',{})
                if group['eligibility_check'] != 'Eligibility Check':
                    if group['status'] != 'Status':
                        check_dict = root_dict.setdefault(group['eligibility_check'].lower().strip().replace(" ","_"),{})
                        check_dict['status'] = group['status']
                continue
            #Spanning Tree             Ineligible:Root Switch with forwarding link:VLAN0069
            m = p5.match(line)
            if m:
                group = m.groupdict()
                root_dict = ret_dict.setdefault('eligibility_check',{})
                spanning_dict = root_dict.setdefault('spanning_tree',{})
                spanning_dict['status'] = group['spanning_tree']
                spanning_dict[group['status'].lower().strip().replace(" ","_")] = group['forwarding_link']
                continue
        return ret_dict



# ==========================================================================================
# Parser Schema for 'show switch stack-ports detail'
# ==========================================================================================

class ShowSwitchStackPortsDetailSchema(MetaParser):
    """
    Schema for
        * 'show switch stack-ports detail'
    """
    schema = {
        'stackports': {
            Any(): {
                'switch_port_id': str,
                'status': str,
                'loopback': str,
                'cable_length': str,
                'neighbor': str,
                'link_ok': str,
                'sync_ok': str,
                'link_active': str,
                'changes_to_link_ok': int,
                'five_minute_input_rate': str,
                'five_minute_output_rate': str,
                'input_bytes': int,
                'output_bytes': int,
                'crc_errors': {
                    'data_crc': int,
                    'ringword_crc': int,
                    'inv_ringword': int,
                    'pcs_codeword': int,
                }
            }
        }
    }

# ==========================================================================================
# Parser for 'show switch stack-ports detail'
# ==========================================================================================

class ShowSwitchStackPortsDetail(ShowSwitchStackPortsDetailSchema):
    """
    Parser for
        * 'show switch stack-ports detail'
    """
    cli_command = 'show switch stack-ports detail'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # initializing dictionary
        ret_dict = {}

        # 1/1 is DOWN Loopback No
        p1 = re.compile(r'^(?P<switch_port_id>\S+) is (?P<status>\S+) Loopback (?P<loopback>\S+)$')

        # Cable Length 50cm     Neighbor NONE
        p2 = re.compile(r'^Cable Length (?P<cable_length>\S+)\s+Neighbor (?P<neighbor>\S+)$')

        # Link Ok Yes Sync Ok Yes Link Active No
        p3 = re.compile(r'^Link Ok (?P<link_ok>\S+) Sync Ok (?P<sync_ok>\S+) Link Active (?P<link_active>\S+)$')

        # Changes to LinkOK 0
        p4 = re.compile(r'^Changes to LinkOK (?P<changes_to_link_ok>\d+)$')

        # Five minute input rate  0 bytes/sec
        p5 = re.compile(r'^Five minute input rate\s+(?P<five_minute_input_rate>[\S\s]+)$')

        # Five minute output rate 0 bytes/sec
        p6 = re.compile(r'^Five minute output rate\s+(?P<five_minute_output_rate>[\S\s]+)$')

        # 0 bytes input
        p7 = re.compile(r'^(?P<input_bytes>\d+) bytes input$')

        # 0 bytes output
        p8 = re.compile(r'^(?P<output_bytes>\d+) bytes output$')

        # Data CRC 0
        p9 = re.compile(r'^Data CRC\s+(?P<data_crc>\d+)$')

        # Ringword CRC 0
        p10 = re.compile(r'^Ringword CRC\s+(?P<ringword_crc>\d+)$')

        # InvRingWord  0
        p11 = re.compile(r'^InvRingWord\s+(?P<inv_ringword>\d+)$')

        # PcsCodeWord 0
        p12 = re.compile(r'^PcsCodeWord\s+(?P<pcs_codeword>\d+)$')

        for line in output.splitlines():
            line = line.strip()
            # 1/1 is DOWN Loopback No
            m = p1.match(line)
            if m:
                group = m.groupdict()
                port_dict = ret_dict.setdefault('stackports',{}).setdefault(group['switch_port_id'],{})
                port_dict['switch_port_id'] = group['switch_port_id']
                port_dict['status'] = group['status']
                port_dict['loopback'] = group['loopback']
                continue

            # Cable Length 50cm     Neighbor NONE
            m = p2.match(line)
            if m:
                group = m.groupdict()
                port_dict['cable_length'] = group['cable_length']
                port_dict['neighbor'] = group['neighbor']
                continue

            # Link Ok Yes Sync Ok Yes Link Active No
            m = p3.match(line)
            if m:
                group = m.groupdict()
                port_dict['link_ok'] = group['link_ok']
                port_dict['sync_ok'] = group['sync_ok']
                port_dict['link_active'] = group['link_active']
                continue

            # Changes to LinkOK 0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                port_dict['changes_to_link_ok'] = int(group['changes_to_link_ok'])
                continue

            # Five minute input rate  0 bytes/sec
            m = p5.match(line)
            if m:
                group = m.groupdict()
                port_dict['five_minute_input_rate'] = group['five_minute_input_rate']
                continue

            # Five minute output rate 0 bytes/sec
            m = p6.match(line)
            if m:
                group = m.groupdict()
                port_dict['five_minute_output_rate'] = group['five_minute_output_rate']
                continue

            # 0 bytes input
            m = p7.match(line)
            if m:
                group = m.groupdict()
                port_dict['input_bytes'] = int(group['input_bytes'])
                continue

            # 0 bytes output
            m = p8.match(line)
            if m:
                group = m.groupdict()
                port_dict['output_bytes'] = int(group['output_bytes'])
                continue

            # Data CRC 0
            m = p9.match(line)
            if m:
                group = m.groupdict()
                error_dict = port_dict.setdefault('crc_errors',{})
                error_dict['data_crc'] = int(group['data_crc'])
                continue

            # Ringword CRC 0
            m = p10.match(line)
            if m:
                group = m.groupdict()
                error_dict['ringword_crc'] = int(group['ringword_crc'])
                continue

            # InvRingWord  0
            m = p11.match(line)
            if m:
                group = m.groupdict()
                error_dict['inv_ringword'] = int(group['inv_ringword'])
                continue

            # PcsCodeWord 0
            m = p12.match(line)
            if m:
                group = m.groupdict()
                error_dict['pcs_codeword'] = int(group['pcs_codeword'])
                continue

        return ret_dict


class ShowXfsuStatusSchema(MetaParser):
    """
        Schema for show xfsu status
    """
    schema = {
        Optional('reload_fast_platform_status'): str,
        'graceful_reload_infra_status': str,
        'uptime_before_fast_reload': int,
        'client': {
            Any(): {
                'id': str,
                'status': str
            }
        }
    }


class ShowXfsuStatus(ShowXfsuStatusSchema):
    """
        Parser for show xfsu status
    """
    cli_command = 'show xfsu status'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        # Reload Fast PLATFORM Status: Not started yet
        p1 = re.compile(r'^Reload Fast PLATFORM Status: (?P<reload_fast_platform_status>.+)$')

        # Graceful Reload Infra Status: Started in stacking mode, not running
        p2 = re.compile(r'^Graceful Reload Infra Status: (?P<graceful_reload_infra_status>.+)$')

        # Minimum required system uptime before fast reload can be supported is 5 seconds
        p3 = re.compile(r'^Minimum required system uptime before fast reload can be supported is (?P<uptime_before_fast_reload>\d+) seconds$')
        # Client OSPFV3                          : (0x10203004) Status: GR stack none: Up
        # Client OSPF                            : (0x10203003) Status: GR stack none: Up
        # Client IS-IS                           : (0x10203002) Status: GR stack none: Up
        # Client GR_CLIENT_FIB                   : (0x10203001) Status: GR stack none: Up
        # Client GR_CLIENT_RIB                   : (0x10203000) Status: GR stack none: Up
        p4 = re.compile(r'^Client (?P<client>\S+)\s+: \((?P<id>\S+)\) Status: (?P<status>.+)$')

        ret_dict = {}
        for line in output.splitlines():
            line = line.strip()

            # Reload Fast PLATFORM Status: Not started yet
            m = p1.match(line)
            if m:
                ret_dict['reload_fast_platform_status'] = m.groupdict()['reload_fast_platform_status']
                continue
            # Graceful Reload Infra Status: Started in stacking mode, not running
            m = p2.match(line)
            if m:
                ret_dict['graceful_reload_infra_status'] = m.groupdict()['graceful_reload_infra_status']
                continue

            # Minimum required system uptime before fast reload can be supported is 5 seconds
            m = p3.match(line)
            if m:
                ret_dict['uptime_before_fast_reload'] = int(m.groupdict()['uptime_before_fast_reload'])
                continue

            # Client OSPFV3                          : (0x10203004) Status: GR stack none: Up
            # Client OSPF                            : (0x10203003) Status: GR stack none: Up
            # Client IS-IS                           : (0x10203002) Status: GR stack none: Up
            # Client GR_CLIENT_FIB                   : (0x10203001) Status: GR stack none: Up
            # Client GR_CLIENT_RIB                   : (0x10203000) Status: GR stack none: Up
            m = p4.match(line)
            if m:
                output_dict = m.groupdict()
                client_dict = ret_dict.setdefault('client', {}).setdefault(output_dict['client'].lower().replace('-', '_'), {})
                client_dict['id'] = output_dict['id']
                client_dict['status'] = output_dict['status']
                continue
        return ret_dict


class ShowGracefulReload(ShowXfsuStatus):
    """
        Parser for show graceful-reload
    """

    cli_command = 'show graceful-reload'

    def cli(self, output=None):
        return super().cli(output=output)

class ShowFileSysSchema(MetaParser):
    """
        Schema for show {filesystem} filesys
    """
    schema = {
        'filesystem': str,
        'filesystem_path': str,
        'filesystem_type': str,
        'mounted': str
    }


class ShowFileSys(ShowFileSysSchema):
    """
        Parser for show {filesystem} filesys
    """

    cli_command = 'show {filesystem} filesys'

    def cli(self, filesystem, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Filesystem: usbflash0
        # Filesystem Path: /mnt/usb0
        # Filesystem Type: vfat
        # Mounted: Read/Write
        p1 = re.compile(r'^(?P<key>Filesystem|Filesystem Path|Filesystem Type|Mounted):\s+(?P<value>.+)$')

        ret_dict = {}
        for line in output.splitlines():
            line = line.strip()

            # Filesystem: usbflash0
            # Filesystem Path: /mnt/usb0
            # Filesystem Type: vfat
            # Mounted: Read/Write
            m = p1.match(line)
            if m:
                ret_dict[m.groupdict()['key'].lower().replace(' ', '_')] = m.groupdict()['value']
                continue

        return ret_dict

class ShowFileInformationSchema(MetaParser):
    """
    Schema for show file information {file}
    """
    schema = {
            Any(): {
                    'file_type': str,
            },
    }


class ShowFileInformation(ShowFileInformationSchema):
    """
    Parser for show file Information {file}
    """

    cli_command = 'show file information {file}'

    def cli(self, file, output=None):

        if output is None:
            cli_cmd = self.cli_command.format(file=file)
            output = self.device.execute(cli_cmd)

        # initialze return dictionary
        ret_dict = {}
        #type is IOSXE_PACKAGE []
        p1 = re.compile(r'^type\s+is\s+(?P<file_type>\S+).*$')

        for line in output.splitlines():
            line = line.strip()
            m = p1.match(line)
            if m:
                group = m.groupdict()
                file_system_dict = ret_dict.setdefault('file_system', {})
                file_system_dict.update({'file_type': group['file_type']})

        return ret_dict


class ShowFileDescriptorsDetailSchema(MetaParser):
    """
    Schema for show file descriptors detail
    """
    schema = {
        'File descriptors': {
            int: {
                    'position_id': str,
                    'open_id': str,
                    'pid': str,
                    'path': str,
                    'file_system': str,
                    'file_name': str
            },
        },
    }


class ShowFileDescriptorsDetail(ShowFileDescriptorsDetailSchema):
    """Parser for show file descriptors detail"""

    cli_command = 'show file descriptors detail'

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        # 0         0  0000  699  revrcsf:-
        p1 = re.compile(r'^(?P<file_id>\d+) +(?P<position_id>\d+) +(?P<open_id>\d+) +(?P<pid>\d+) +(?P<path>\w+\:\-)$')

        # Filename: usb0:GD_run_config Fd: 4
        p2 = re.compile(r'^Filename\: +(?P<file_system>\w+)\:(\/)?(?P<file_name>\w+(\.)?(\w+)?).*$')

        for line in output.splitlines():
            line = line.strip()

            # 0         0  0000  699  revrcsf:-
            m = p1.match(line)
            if m:
                group = m.groupdict()
                file_desc = ret_dict.setdefault('File descriptors', {})
                file_dict = file_desc.setdefault(int(group['file_id']), {})
                file_dict.update({
                    'position_id': group['position_id'],
                    'open_id': group['open_id'],
                    'pid': group['pid'],
                    'path': group['path']
                })

            # Filename: usb0:GD_run_config Fd: 4
            m = p2.match(line)
            if m:
                group = m.groupdict()
                file_dict['file_system'] = group['file_system']
                file_dict['file_name'] = group['file_name']

        return ret_dict


# ======================================================
# Parser for 'show time-range {time_range_name}'
# ======================================================

class ShowTimeRangeSchema(MetaParser):
    """Schema for show time-range {time_range_name}"""

    schema = {
        'time_range_entry': str,
        'status': str,
        'periodicity': str,
        'start_time': str,
        'end_time': str,
        Optional('used_in'): str,
    }

class ShowTimeRange(ShowTimeRangeSchema):
    """Parser for show time-range {time_range_name}"""

    cli_command = 'show time-range {time_range_name}'

    def cli(self, time_range_name, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(time_range_name=time_range_name))

        # time-range entry: time1 (active)
        p1 = re.compile(r"^time-range\s+entry:\s+(?P<time_range_entry>\S+)\s+\((?P<status>\w+)\)$")
        #    periodic daily 22:40 to 22:41
        p2 = re.compile(r"^\s+periodic\s+(?P<periodicity>\w+)\s+(?P<start_time>\S+)\s+to\s+(?P<end_time>\S+)$")
        #    used in: IPv6 ACL entry
        p3 = re.compile(r"^\s+used\s+in:\s+(?P<used_in>\S+\s+\S+\s+\S+)$")

        ret_dict = {}

        for line in output.splitlines():

            # time-range entry: time1 (active)
            m = p1.match(line)
            if m:
                dict_val = m.groupdict()
                ret_dict['time_range_entry'] = dict_val['time_range_entry']
                ret_dict['status'] = dict_val['status']
                continue

            #    periodic daily 22:40 to 22:41
            m = p2.match(line)
            if m:
                dict_val = m.groupdict()
                ret_dict['periodicity'] = dict_val['periodicity']
                ret_dict['start_time'] = dict_val['start_time']
                ret_dict['end_time'] = dict_val['end_time']
                continue

            #    used in: IPv6 ACL entry
            m = p3.match(line)
            if m:
                dict_val = m.groupdict()
                ret_dict['used_in'] = dict_val['used_in']
                continue

        return ret_dict

# ============================================================================
# Schema for 'show platform pm etherchannel {ec_channel_group_id} group-mask '
# ============================================================================
class ShowPlatformPmEtherchannelGroupMaskSchema(MetaParser):
    """Schema for show platform pm etherchannel {ec_channel_group_id} group-mask"""

    schema = {
        'etherchannel': {
            Any(): {
                'ec_channel_group_id': int,
                'ec_channel_group_mac': str,
                'active_ports': int,
                Optional('interface'): {
                    Any(): {
                        'if_id': str,
                        'ec_index': int
                    }
                }
            }
        }
    }

# ============================================================================
# Parser for 'show platform pm etherchannel {ec_channel_group_id} group-mask '
# ============================================================================
class ShowPlatformPmEtherchannelGroupMask(ShowPlatformPmEtherchannelGroupMaskSchema):
    """Parser for show platform pm etherchannel {ec_channel_group_id} group-mask"""

    cli_command = 'show platform pm etherchannel {ec_channel_group_id} group-mask'

    def cli(self, ec_channel_group_id="", output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(ec_channel_group_id=ec_channel_group_id))

        # EC Channel-Group               : 10
        p1 = re.compile(r"^EC Channel-Group\s+: (?P<ec_channel_group_id>\S+)$")

        # EC Channel-Group Mac           : 0077.8d99.410e
        p2 = re.compile(r"^EC Channel-Group Mac\s+: (?P<ec_channel_group_mac>\S+)$")

        # # Of Active Ports              : 2
        p3 = re.compile(r"^# Of Active Ports\s+: (?P<of_active_ports>\S+)$")

        # If Name                                  If Id                  EC Index
        p4 = re.compile(r"^(?P<interface_name>\S+) +(?P<interface_id>[\w\s]+)\s+(?P<ec_index>[\d]+)$")

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # EC Channel-Group               : 10
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ether_dict = ret_dict.setdefault('etherchannel',{}).setdefault(int(group['ec_channel_group_id']),{})
                ether_dict['ec_channel_group_id'] = int(group['ec_channel_group_id'])
                continue

            # EC Channel-Group Mac           : 0077.8d99.410e
            m = p2.match(line)
            if m:
                dict_val = m.groupdict()
                ether_dict['ec_channel_group_mac'] = dict_val['ec_channel_group_mac']
                continue

            # # Of Active Ports              : 2
            m = p3.match(line)
            if m:
                dict_val = m.groupdict()
                ether_dict['active_ports'] = int(dict_val['of_active_ports'])
                continue

            # If Name                                  If Id                  EC Index
            m = p4.match(line)
            if m:
                name = m.groupdict()
                key_chain_dict = ether_dict.setdefault('interface', {}).setdefault(Common.convert_intf_name(name['interface_name']), {})
                key_chain_dict['if_id'] = name['interface_id']
                key_chain_dict['ec_index'] = int(name['ec_index'])
                continue

        return ret_dict

class TestPlatformSoftwareDatabaseSchema(MetaParser):
    """Schema for test platform software database get-n all ios_oper/platform_component
                  test platform software database get-n all ios_oper/transceiver"""

    schema = {
        'table_record_index': {
            str: {
                str: Or(str, int),
            },
        },
    }

class TestPlatformSoftwareDatabase(TestPlatformSoftwareDatabaseSchema):
    """Parser for test platform software database get-n all ios_oper/platform_component
                  test platform software database get-n all ios_oper/transceiver"""

    cli_command = 'test platform software database get-n all ios_oper/{component}'

    def cli(self, component, output=None):
        if output is None:
            # execute command to get output
            output = self.device.execute(self.cli_command.format(component=component))

        # Initialize the ret_dict
        ret_dict = {}

        # Table Record Index 0 = {
        p1 = re.compile(r"^Table\s+Record\s+Index\s+(?P<index>\d+)\s+=\s+{$")

        # [0] cname = Fan1/1
        p2 = re.compile(r"^\s*\[(?P<index>\d+)\]\s+(?P<key>\S+)\s+=\s+(?P<value>.*)$")

        # Initialize variables to hold temporary values
        index = None
        table_record = {}

        # Iterate over each line of the output
        for line in output.splitlines():
            line = line.strip()

            # Table Record Index 0 = {
            m = p1.match(line)
            if m:
                index = m.group("index")
                table_record[index] = {}
                continue

            # [0] cname = Fan1/1
            m = p2.match(line)
            if m and index is not None:
                key = m.group("key")
                value_str = m.group("value")

                # Try to convert value to int if possible
                try:
                    value = int(value_str)
                except ValueError:
                    # If conversion to int fails, keep the value as string
                    value = value_str

                # Remove prefixes and extract the last part of the key if it contains '.'
                key_parts = key.split('.')
                key = key_parts[-1]

                # Update table_record with the value
                table_record[index][key] = value
                continue

        # Populate the parsed output
        if table_record:
            ret_dict["table_record_index"] = table_record

        return ret_dict

