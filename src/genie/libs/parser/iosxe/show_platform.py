''' show_platform.py

IOSXE parsers for the following show commands:

    * 'show bootvar'
    * 'show version'
    * 'dir'
    * 'show redundancy'
    * 'show inventory'
    * 'show platform'
    * 'show platform hardware qfp active feature appqoe stats all'
    * 'show boot'
    * 'show switch detail'
    * 'show switch'
    * 'show environment all'
    * 'show platform software fed switch {switch_type} mpls rlist'
    * 'show platform hardware fed switch active fwd-asic resource tcam utilization'
    * 'show module'
    * 'show platform hardware qfp active datapath utilization summary'
    * 'show platform resources'
    * 'show platform software fed switch active mpls rlist | sect RLIST id:'
    * 'show platform hardware qfp active tcam resource-manager usage'
    * 'show platform software yang-management process'
    * 'show platform software yang-management process monitor'
    * 'show platform software yang-management process state'
    * 'show platform software fed active fnf et-analytics-flows'
    * 'show platform software fed switch active mpls forwarding label {label} detail'
    * 'show platform software fed active mpls forwarding label {label} detail'
    * 'show platform software fed active inject packet-capture detailed'
    * 'show platform hardware throughput crypto'
    * 'show platform software dpidb index'
    * 'show platform software fed switch active ifm mappings lpn'
    * 'show platform software fed switch active ifm mappings lpn | include {interface}'
    * 'show platform software fed switch active ptp domain'
    * 'show platform software fed switch active ptp interface {interface}'
    * 'show platform software fed active acl usage'
    * 'show platform software fed active acl usage | include {aclName}'
    * 'show platform sudi certificate sign nonce {sig}'
    * 'show environment status'
    * 'show platform hardware fed switch active fwd-asic drops exceptions'
    * 'show platform software fed {switchvirtualstate} mpls lspa all | c {mode}'
    * 'show platform software fed {switchvirtualstate} mpls lspa all'
    * 'show platform software dns-umbrella statistics'
'''

# Python
import re
import logging
from collections import OrderedDict
import xml.etree.ElementTree as ET
from xml.dom import minidom

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional, Use
from genie.libs.parser.utils.common import Common
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
        },
        Optional('standby'): {
            Optional('configuration_register'): str,
            Optional("next_reload_configuration_register"): str,
            Optional('boot_variable'): str,
        },
    }


class ShowBootvar(ShowBootvarSchema):
    """Parser for show boot"""

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
        p1 = re.compile(r'^BOOT +variable +=( *(?P<var>\S+);?)?$')

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
                'gigabit_ethernet': int,
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
        p1_1 = re.compile(r'^(?P<os>[A-Z]+) +\(.*\) +(?P<platform>.+) +Software'
                          r' +\((?P<image_id>.+)\).+( +Experimental)? +[Vv]ersion'
                          r' +(?P<version>\S+), +RELEASE SOFTWARE .*$')

        # 16.6.5
        p2 = re.compile(r'^(?P<ver_short>\d+\.\d+).*')

        # Cisco IOS Software [Fuji], ASR1000 Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 16.7.1prd4, RELEASE SOFTWARE (fc1)
        # Cisco IOS Software [Fuji], Catalyst L3 Switch Software (CAT3K_CAA-UNIVERSALK9-M), Experimental Version 16.8.20170924:182909 [polaris_dev-/nobackup/mcpre/BLD-BLD_POLARIS_DEV_LATEST_20170924_191550 132]
        # Cisco IOS Software, 901 Software (ASR901-UNIVERSALK9-M), Version 15.6(2)SP4, RELEASE SOFTWARE (fc3)
        # Cisco IOS Software [Amsterdam], Catalyst L3 Switch Software (CAT9K_IOSXE), Experimental Version 17.4.20200702:124009 [S2C-build-polaris_dev-116872-/nobackup/mcpre/BLD-BLD_POLARIS_DEV_LATEST_20200702_122021 243]
        # Cisco IOS Software [Denali], ASR1000 Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Experimental Version 16.3.20170410:103306 [v163_mr_throttle-BLD-BLD_V163_MR_THROTTLE_LATEST_20170410_093453 118]
        p3 = re.compile(r'^[Cc]isco +(?P<os>[A-Z]+) +[Ss]oftware(.+)?\, '
                        r'+(?P<platform>.+) +Software +\((?P<image_id>.+)\).+( '
                        r'+Experimental)? +[Vv]ersion '
                        r'+(?P<version>[a-zA-Z0-9\.\:\(\)]+) *,? *'
                        r'(?P<label>(\[.+?(?P<build_label>BLD_[0-9a-zA-Z_]+)(-\S+)? \d+\])|.*)$')

        # Copyright (c) 1986-2016 by Cisco Systems, Inc.
        p4 = re.compile(r'^Copyright +(.*)$')

        # Technical Support: http://www.cisco.com/techsupport
        p5 = re.compile(r'^Technical +Support: +http\:\/\/www'
                        r'\.cisco\.com\/techsupport')

        # rom
        p6 = re.compile(r'^ROM\: +(?P<rom>.+)$')

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
        p16_1 = re.compile(r'(?P<license_level>\S+) +Type\: +(?P<license_type>\S+)$')

        # AIR License Level: AIR DNA Advantage
        p16_2 = re.compile(r'^\s*AIR [Ll]icense +[Ll]evel\: +(?P<air_license_level>.+)$')

        ## Technology Package License Information:
        ## Technology-package                                     Technology-package
        # Current                        Type                       Next reboot
        p16_3 = re.compile(r'^Current  +Type  +Next reboot')

        # network-advantage   	Smart License                 	 network-advantage
        # dna-advantage       	Subscription Smart License    	 dna-advantage
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
                    continue

            # Copyright (c) 1986-2016 by Cisco Systems, Inc.
            m = p4.match(line)
            if m:
                version_dict.setdefault('version', {}).setdefault('image_type', 'developer image')
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
                    group = m_1.groupdict()
                    version_dict['version']['license_type'] = group['license_type']
                    version_dict['version']['license_level'] = group['license_level']
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

            # network-advantage   	Smart License                 	 network-advantage
            # dna-advantage       	Subscription Smart License    	 dna-advantage
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

            if m or m2:
                if m:
                    group = m.groupdict()
                elif m2:
                    group = m2.groupdict()

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
        'unit': str,
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
        p1_8 = re.compile(r'^Slot \d Linecard|Slot \d Supervisor$')        

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

                if 'Switch1' in name or 'Switch2' in name or 'TenGigabitEthernet' in name:
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
                        'state': str,
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
        #  0/0      SPA-1XCHSTM1/OC3    ok                    2d00h
        # F0                            ok, active            00:09:23
        # P1        Unknown             N/A                   never
        p6 = re.compile(r'^(?P<slot>[a-zA-Z0-9]+)(\/(?P<subslot>\d+))?( +(?P<name>[a-zA-Z0-9\-\_/+]+))? +(?P<state>(?!\d+|unknown)\w+(\, \w+)?(/\w+)?) +(?P<insert_time>[\w\.\:]+)$')

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
                if ('WS-C' in model) or ('C9500' in model) or ('C9300' in model) or ('C9200' in model):
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
                                if re.match(r'^ASR\d+-(\d+T\S+|SIP\d+|X)', name) or ('ISR' in name) or ('C9' in name) or ('C82' in name):
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
                        if re.match(r'^ASR\d+-(\d+T\S+|SIP\d+|X)', name) or ('ISR' in name) or ('C9' in name) or ('C82' in name):
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
        },
        Optional('standby'): {
            Optional('configuration_register'): str,
            Optional('boot_variable'): str,
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

        # Enable Break = yes
        p6 = re.compile(r'^Enable +Break += +(?P<var>\w+)$')

        # Boot Mode = DEVICE
        p7 = re.compile(r'^Boot +Mode += +(?P<var>\w+)$')

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
                    'hw_ver': str,
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
                        'state': str,
                        Optional('direction'): str,
                    },
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
            },
        },
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
        p1 = re.compile(r'^Switch\s+(?P<switch>\d+)\s+FAN\s+(?P<fan>\d+)\s+is\s+(?P<state>[\w\s]+)$')

        # Switch 1 FAN 1 direction is Front to Back
        p1_1 = re.compile(r'^Switch\s+(?P<switch>\d+)\s+FAN +(?P<fan>\d+)\s'
                          r'+direction\s+is\s+(?P<direction>[\w\s]+)$')

        p1_2 = re.compile(r'^(?P<switch>\d+)\s+(?P<fan>\d+)\s+\d+\s+(?P<state>.*)')

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

            m = p1_2.match(line)
            if m:
                group = m.groupdict()
                switch = group['switch']
                fan = group['fan']
                root_dict = ret_dict.setdefault('switch', {}).setdefault(switch, {})
                root_dict.setdefault('fan', {}).setdefault(fan, {}).setdefault('state', group['state'].lower())
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
                'serial':str,
                'mac_address':str,
                'hw':str,
                'fw':str,
                'sw':str,
                'status':str,
                'redundancy_role':str,
                'operating_redundancy_mode':str,
                'configured_redundancy_mode':str,
            },
        },
        Optional('number_of_mac_address'):int,
        Optional('chassis_mac_address_lower_range'):str,
        Optional('chassis_mac_address_upper_range'):str,
    }


class ShowModule(ShowModuleSchema):
    """Parser for show module"""

    cli_command = 'show module'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

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

        p2=re.compile(r'^(?P<mod>\d+) *(?P<ports>\d+) +(?P<card_type>.*) +(?P<model>\S+) +(?P<serial>\S+)$')

        # Mod MAC addresses                    Hw   Fw           Sw                 Status
        # ---+--------------------------------+----+------------+------------------+--------
        # 1   F87A.4125.1400 to F87A.4125.147D 0.2  17.7.0.41     BLD_POLARIS_DEV_LA ok

        p3=re.compile(r'^\d+\s+(?P<mac_address>[\w\.]+) .*(?P<hw>\d+.?\d+?) +(?P<fw>\S+) +(?P<sw>\S+) +(?P<status>\S+)$')

        # Mod Redundancy Role     Operating Redundancy Mode Configured Redundancy Mode
        # ---+-------------------+-------------------------+---------------------------
        # 1   Active              non-redundant             Non-redundant

        p4=re.compile(r'^\d+ *(?P<redundancy_role>\S+) *(?P<operating_redundancy_mode>\S+) *(?P<configured_redundancy_mode>\S+)$')

        #Chassis MAC address range: 512 addresses from f87a.4125.1400 to f87a.4125.15ff
        p5=re.compile(r'^Chassis MAC address range: (?P<number_of_mac_address>\d+) addresses from (?P<chassis_mac_address_lower_range>.*) to (?P<chassis_mac_address_upper_range>.*)$')

        for line in out.splitlines():
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

            # Chassis Type: C9500X-28C8D

            # Mod Ports Card Type                                   Model          Serial No.
            # ---+-----+--------------------------------------+--------------+--------------
            # 1   38   Cisco Catalyst 9500X-28C8D Switch           C9500X-28C8D     FDO25030SLN
            m = p2.match(line)
            if m:
                group = m.groupdict()
                switch = group.pop('mod')
                switch_dict = ret_dict.setdefault('module', {}).setdefault(int(switch), {})
                switch_dict.update({k: v.strip() for k, v in group.items()})
                switch_dict['ports']=int(group['ports'])
                continue

            # Mod MAC addresses                    Hw   Fw           Sw                 Status
            # ---+--------------------------------+----+------------+------------------+--------
            # 1   F87A.4125.1400 to F87A.4125.147D 0.2  17.7.0.41     BLD_POLARIS_DEV_LA ok

            m=p3.match(line)
            if m:
                group = m.groupdict()
                switch_dict.update({k: v.strip() for k, v in group.items()})
                continue

            # Mod Redundancy Role     Operating Redundancy Mode Configured Redundancy Mode
            # ---+-------------------+-------------------------+---------------------------
            # 1   Active              non-redundant             Non-redundant
            m=p4.match(line)
            if m:
                group = m.groupdict()
                switch_dict.update({k: v.lower().strip() for k, v in group.items()})
                continue

            #Chassis MAC address range: 512 addresses from f87a.4125.1400 to f87a.4125.15ff
            m=p5.match(line)
            if m:
                group=m.groupdict()
                ret_dict.update({k: v.lower().strip() for k, v in group.items()})
                ret_dict['number_of_mac_address'] = int(group['number_of_mac_address'])
                continue

        return ret_dict


class ShowPlatformSoftwareSlotActiveMonitorMemSchema(MetaParser):
    """Schema for show platform software process slot switch active R0 monitor | inc Mem :|Swap:"""
    schema = {
        'memory': {
            'total': int,
            'free': int,
            'used': int,
            'buff_cache': int
        },
        'swap': {
            'total': int,
            'free': int,
            'used': int,
            'available_memory': int
        }
    }


class ShowPlatformSoftwareSlotActiveMonitorMem(ShowPlatformSoftwareSlotActiveMonitorMemSchema):
    """Parser for show platform software process slot switch active R0 monitor | inc Mem :|Swap:"""

    cli_command = 'show platform software process slot switch active R0 monitor | inc Mem :|Swap:'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern
        p1 = re.compile(r'^KiB +Mem *: +(?P<total>\d+) *total, +'
                        '(?P<free>\d+) *free, +(?P<used>\d+) *used, +'
                        '(?P<buff_cache>\d+) *buff\/cache$')

        p2 = re.compile(r'^KiB +Swap *: +(?P<total>\d+) *total, +'
                        '(?P<free>\d+) *free, +(?P<used>\d+) *used. +'
                        '(?P<available_memory>\d+) *avail +Mem$')

        for line in out.splitlines():
            line = line.strip()

            # KiB Mem :  4010000 total,    16756 free,  1531160 used,  2462084 buff/cache
            m = p1.match(line)
            if m:
                group = m.groupdict()
                name_dict = ret_dict.setdefault('memory', {})
                name_dict.update({k: int(v) for k, v in group.items()})
                continue

            # KiB Swap:        0 total,        0 free,        0 used.  1778776 avail Mem
            m = p2.match(line)
            if m:
                group = m.groupdict()
                name_dict = ret_dict.setdefault('swap', {})
                name_dict.update({k: int(v) for k, v in group.items()})
                continue
        return ret_dict


class ShowPlatformSoftwareStatusControlSchema(MetaParser):
    """Schema for show platform software status control-processor brief"""
    schema = {
        'slot': {
            Any(): {
                'load_average': {
                    'status': str,
                    '1_min': float,
                    '5_min': float,
                    '15_min': float,
                },
                'memory': {
                    'status': str,
                    'total': int,
                    'used': int,
                    'used_percentage': int,
                    'free': int,
                    'free_percentage': int,
                    'committed': int,
                    'committed_percentage': int,
                },
                'cpu': {
                    Any(): {
                        'user': float,
                        'system': float,
                        'nice_process': float,
                        'idle': float,
                        'irq': float,
                        'sirq': float,
                        'waiting': float
                    }
                }
            }
        }
    }


class ShowPlatformSoftwareStatusControl(ShowPlatformSoftwareStatusControlSchema):
    """Parser for show platform software status control-processor brief"""

    cli_command = 'show platform software status control-processor brief'
    exclude = ['idle', 'system', 'user', '1_min', '5_min',
               '15_min', 'free', 'used', 'sirq', 'waiting', 'committed']

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern
        p1 = re.compile(r'^(?P<slot>\S+) +(?P<status>\w+) +'
                        '(?P<min1>[\d\.]+) +(?P<min5>[\d\.]+) +(?P<min15>[\d\.]+)$')

        p2 = re.compile(r'^(?P<slot>\S+) +(?P<status>\w+) +'
                        '(?P<total>\d+) +(?P<used>\d+) +\((?P<used_percentage>[\d\s]+)\%\) +'
                        '(?P<free>\d+) +\((?P<free_percentage>[\d\s]+)\%\) +'
                        '(?P<committed>\d+) +\((?P<committed_percentage>[\d\s]+)\%\)$')

        p3 = re.compile(r'^((?P<slot>\S+) +)?(?P<cpu>\d+) +(?P<user>[\d\.]+) +(?P<system>[\d\.]+) +(?P<nice_process>[\d\.]+) +(?P<idle>[\d\.]+) +(?P<irq>[\d\.]+) +(?P<sirq>[\d\.]+) +(?P<waiting>[\d\.]+)$')

        for line in out.splitlines():
            line = line.strip()

            # Slot  Status  1-Min  5-Min 15-Min
            # 1-RP0 Healthy   0.26   0.35   0.33
            m = p1.match(line)
            if m:
                group = m.groupdict()
                slot = group.pop('slot').lower()
                load_dict = ret_dict.setdefault('slot', {}).setdefault(slot, {}).setdefault('load_average', {})
                load_dict['status'] = group['status'].lower()
                load_dict['1_min'] = float(group['min1'])
                load_dict['5_min'] = float(group['min5'])
                load_dict['15_min'] = float(group['min15'])
                continue

            # Slot  Status    Total     Used (Pct)     Free (Pct) Committed (Pct)
            # 1-RP0 Healthy  4010000  2553084 (64%)  1456916 (36%)   3536536 (88%)
            m = p2.match(line)
            if m:
                group = m.groupdict()
                slot = group.pop('slot').lower()
                mem_dict = ret_dict.setdefault('slot', {}).setdefault(slot, {}).setdefault('memory', {})
                mem_dict['status'] = group.pop('status').lower()
                mem_dict.update({k: int(v) for k, v in group.items()})
                continue

            #  Slot  CPU   User System   Nice   Idle    IRQ   SIRQ IOwait
            # 1-RP0    0   3.89   2.09   0.00  93.80   0.00   0.19   0.00
            #          1   5.70   1.00   0.00  93.20   0.00   0.10   0.00
            m = p3.match(line)
            if m:
                group = m.groupdict()
                if group['slot']:
                    slot = group.pop('slot').lower()
                else:
                    group.pop('slot')
                cpu = group.pop('cpu')
                cpu_dict = ret_dict.setdefault('slot', {}).setdefault(slot, {}).\
                    setdefault('cpu', {}).setdefault(cpu, {})
                cpu_dict.update({k: float(v) for k, v in group.items()})
                continue
        return ret_dict


class ShowProcessesCpuSortedSchema(MetaParser):
    """Schema for show processes cpu sorted
                  show processes cpu sorted <1min|5min|5sec>
                  show processes cpu sorted | include <WORD>
                  show processes cpu sorted <1min|5min|5sec> | include <WORD>"""
    schema = {
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
                  show processes cpu sorted <1min|5min|5sec>
                  show processes cpu sorted | include <WORD>
                  show processes cpu sorted <1min|5min|5sec> | include <WORD>"""

    cli_command = 'show processes cpu sorted'
    exclude = ['five_min_cpu', 'five_sec_cpu_total', 'nonzero_cpu_processes', 'zero_cpu_processes',
               'five_sec_cpu', 'invoked', 'one_min_cpu', 'runtime', 'usecs', 'pid', 'process', ]

    def cli(self, sort_time='', key_word='', output=None):

        assert sort_time in ['1min', '5min', '5sec', ''], "Not one from 1min 5min 5sec"
        if output is None:
            if sort_time:
                self.cli_command += ' ' + sort_time
            if key_word:
                self.cli_command += ' | include ' + key_word

            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}
        zero_cpu_processes = []
        nonzero_cpu_processes = []
        index = 0

        # initial regexp pattern
        p1 = re.compile(r'^CPU +utilization +for +five +seconds: +'
                        '(?P<five_sec_cpu_total>\d+)\%\/(?P<five_sec_cpu_interrupts>\d+)\%;'
                        ' +one +minute: +(?P<one_min_cpu>\d+)\%;'
                        ' +five +minutes: +(?P<five_min_cpu>\d+)\%$')

        p2 = re.compile(r'^(?P<pid>\d+) +(?P<runtime>\d+) +(?P<invoked>\d+) +(?P<usecs>\d+) +'
                        '(?P<five_sec_cpu>[\d\.]+)\% +(?P<one_min_cpu>[\d\.]+)\% +'
                        '(?P<five_min_cpu>[\d\.]+)\% +(?P<tty>\d+) +'
                        '(?P<process>[\w\-\/\s]+)$')

        for line in out.splitlines():
            line = line.strip()

            # CPU utilization for five seconds: 5%/1%; one minute: 6%; five minutes: 6%
            m = p1.match(line)
            if m:
                ret_dict.update({k: int(v) for k, v in m.groupdict().items()})
                continue

            # PID Runtime(ms)     Invoked      uSecs   5Sec   1Min   5Min TTY Process
            # 539     6061647    89951558         67  0.31%  0.36%  0.38%   0 HSRP Common
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
        p1 = re.compile(r'^CPU +utilization +for +five +seconds: +(?P<cpu_util_five_secs>[\d\%]+),'
                        ' +one +minute: +(?P<cpu_util_one_min>[\d\%]+),'
                        ' +five +minutes: +(?P<cpu_util_five_min>[\d\%]+)$')

        p2 = re.compile(r'^(?P<core>[\w\s]+): +CPU +utilization +for'
                        ' +five +seconds: +(?P<core_cpu_util_five_secs>\d\%+),'
                        ' +one +minute: +(?P<core_cpu_util_one_min>[\d\%]+),'
                        ' +five +minutes: +(?P<core_cpu_util_five_min>[\d\%]+)$')

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

        p1 = re.compile(r'^Number +of +Critical +alarms: +(?P<critic_larams>\d+)$')

        p2 = re.compile(r'^Number +of +Major +alarms: +(?P<maj_alarms>\d+)$')

        p3 = re.compile(r'^Number +of +Minor +alarms: +(?P<min_alarms>\d+)$')

        p4 = re.compile(r'(?P<slot>\S+) +(?P<sensor_name>\S+|\w+\: +\S+(:? +\S+)?) +'
                        r'(?P<state>Normal|Fan +Speed +\S+) +(?P<reading>\d+ +\S+'
                        r'(:? +AC)?)(:? +\S+)?$')

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

            # Slot    Sensor       Current State       Reading
            # ----    ------       -------------       -------
            #  F0    Temp: Pop Die    Normal           43 Celsius
            #  P6    Temp: FC PWM1    Fan Speed 60%    26 Celsius
            #  P0    Iin              Normal           1 A
            #  P0    Vin              Normal           101 V AC
            m = p4.match(line)
            if m:
                group = m.groupdict()
                sensor_name = group.pop('sensor_name')
                slot = group.pop('slot')
                fin_dict = ret_dict.setdefault('slot', {}).setdefault(slot, {}).\
                    setdefault('sensor', {}).setdefault(sensor_name, {})
                fin_dict.update({k: str(v) for k, v in group.items()})
                continue

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


class ShowPlatformHardwareSchema(MetaParser):
    """Schema for show platform hardware qfp active infrastructure bqs queue output default all
        show platform hardware qfp active infrastructure bqs queue output default interface {interface}"""

    schema = {
        Any(): {
            'if_h': int,
            Optional('index'): {
                Any(): {
                    'queue_id': str,
                    'name': str,
                    'software_control_info': {
                        'cache_queue_id': str,
                        'wred': str,
                        Optional('qlimit_bytes'): int,
                        Optional('qlimit_pkts'): int,
                        'parent_sid': str,
                        'debug_name': str,
                        'sw_flags': str,
                        'sw_state': str,
                        'port_uidb': int,
                        'orig_min': int,
                        'min': int,
                        'min_qos': int,
                        'min_dflt': int,
                        'orig_max': int,
                        'max': int,
                        'max_qos': int,
                        'max_dflt': int,
                        'share': int,
                        'plevel': int,
                        'priority': int,
                        Optional('defer_obj_refcnt'): int,
                        Optional('cp_ppe_addr'): str,
                    },
                    'statistics': {
                        'tail_drops_bytes': int,
                        'tail_drops_packets': int,
                        'total_enqs_bytes': int,
                        'total_enqs_packets': int,
                        Optional('queue_depth_bytes'): int,
                        Optional('queue_depth_pkts'): int,
                        Optional('lic_throughput_oversub_drops_bytes'): int,
                        Optional('lic_throughput_oversub_drops_packets'): int,
                    }
                },
            }
        },
    }


class ShowPlatformHardware(ShowPlatformHardwareSchema):
    """Parser for show platform hardware qfp active infrastructure bqs queue output default all
        show platform hardware qfp active infrastructure bqs queue output default interface {interface}"""

    cli_command = ['show platform hardware qfp active infrastructure bqs queue output default all',
                   'show platform hardware qfp active infrastructure bqs queue output default interface {interface}']

    def cli(self, interface='', output=None):

        if output is None:
            if interface:
                cmd = self.cli_command[1].format(interface=interface)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # Interface: GigabitEthernet1/0/7 QFP: 0.0 if_h: 32 Num Queues/Schedules: 1
        # Interface: Loopback2 QFP: 0.0 if_h: 34 Num Queues/Schedules: 0
        # Interface: GigabitEthernet0/0/1.2 QFP: 0.0 if_h: 35 Num Queues/Schedules: 0
        # Interface: GigabitEthernet0/0/1.EFP2054 QFP: 0.0 if_h: 36 Num Queues/Schedules: 0
        # Interface: BG4048.10207e1 QFP: 0.0 if_h: 4079 Num Queues/Schedules: 0
        # Interface: VPLS-2944.10207e2 QFP: 0.0 if_h: 4080 Num Queues/Schedules:
        # Interface: internal0/0/recycle:0 QFP: 0.0 if_h: 1 Num Queues/Schedules: 0
        p1 = re.compile(r'^Interface: +(?P<intf_name>[\w\d\/\.\-\:]+)'
                        ' +QFP: +(?P<qfp>[\d\.]+)'
                        ' +if_h: +(?P<if_h>\d+)'
                        ' +Num Queues/Schedules: +(?P<num_queues>\d+)$')

        #     Index 0 (Queue ID:0xa6, Name: GigabitEthernet1/0/7)
        p2 = re.compile(r'^Index +(?P<index>\d+)'
                        ' +\(Queue +ID:(?P<queue_id>[\w\d]+),'
                        ' +Name: +(?P<interf_name>[\w\d\/\.\-\:]+)\)$')

        #       Software Control Info:
        #  PARQ Software Control Info:
        p3_1 = re.compile(r'^(PARQ +)?Software Control Info:$')

        #  (cache) queue id: 0x000000a6, wred: 0x88b16ac2, qlimit (bytes): 3281312
        #  (cache) queue id: 0x00000070, wred: 0xe73cfde0, qlimit (pkts ): 418
        p3_2 = re.compile(r'^\(cache\) +queue +id: +(?P<cache_queue_id>[\w\d]+),'
                          ' +wred: +(?P<wred>[\w\d]+),'
                          ' +qlimit +\((?P<type>bytes|pkts +)\): +(?P<qlimit>\d+)$')

        #       parent_sid: 0x284, debug_name: GigabitEthernet1/0/7
        p4 = re.compile(r'^parent_sid: +(?P<parent_sid>[\w\d]+),'
                        ' debug_name: +(?P<debug_name>[\w\d\/\.\-\:]+)$')

        #       sw_flags: 0x08000011, sw_state: 0x00000c01, port_uidb: 245728
        p5 = re.compile(r'^sw_flags: +(?P<sw_flags>[\w\d]+),'
                        ' +sw_state: +(?P<sw_state>[\w\d]+),'
                        ' +port_uidb: +(?P<port_uidb>\d+)$')

        #       orig_min  : 0                   ,      min: 105000000
        p6 = re.compile(r'^orig_min +: +(?P<orig_min>\d+) +,'
                        ' +min: +(?P<min>\d+)$')

        #       min_qos   : 0                   , min_dflt: 0
        p7 = re.compile(r'^min_qos +: +(?P<min_qos>\d+) +,'
                        ' +min_dflt: +(?P<min_dflt>\d+)$')

        #       orig_max  : 0                   ,      max: 0
        p8 = re.compile(r'^orig_max +: +(?P<orig_max>\d+) +,'
                        ' +max: +(?P<max>\d+)$')

        #       max_qos   : 0                   , max_dflt: 0
        p9 = re.compile(r'^max_qos +: +(?P<max_qos>\d+) +,'
                        ' +max_dflt: +(?P<max_dflt>\d+)$')

        #       share     : 1
        p10 = re.compile(r'^share +: +(?P<share>\d+)$')

        #       plevel    : 0, priority: 65535
        p11 = re.compile(r'^plevel +: +(?P<plevel>\d+),'
                         ' +priority: +(?P<priority>\d+)$')

        #       defer_obj_refcnt: 0
        #   defer_obj_refcnt: 0, cp_ppe_addr: 0x00000000
        p12 = re.compile(r'^defer_obj_refcnt: +(?P<defer_obj_refcnt>\d+)'
                         r'(, +cp_ppe_addr: +(?P<cp_ppe_addr>\w+))?$')

        #     Statistics:
        p13_1 = re.compile(r'^Statistics:$')

        #       tail drops  (bytes): 0                   ,          (packets): 0
        p13_2 = re.compile(r'^tail +drops +\(bytes\): +(?P<tail_drops_bytes>\d+) +,'
                           ' +\(packets\): +(?P<tail_drops_packets>\d+)$')

        #       total enqs  (bytes): 0                   ,          (packets): 0
        p14 = re.compile(r'^total +enqs +\(bytes\): +(?P<total_enqs_bytes>\d+) +,'
                         ' +\(packets\): +(?P<total_enqs_packets>\d+)$')

        #       queue_depth (bytes): 0
        #       queue_depth (pkts ): 0
        p15 = re.compile(r'^queue_depth +\((?P<type>bytes|pkts +)\): +(?P<queue_depth>\d+)$')

        #       licensed throughput oversubscription drops:
        #                   (bytes): 0                   ,          (packets): 0
        p16 = re.compile(r'^\(bytes\): +(?P<lic_throughput_oversub_drops_bytes>\d+) +,'
                         ' +\(packets\): +(?P<lic_throughput_oversub_drops_packets>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                interface = group['intf_name']
                ret_dict.setdefault(interface, {})
                ret_dict[interface]['if_h'] = int(group['if_h'])
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                index = group['index']
                if 'index' not in ret_dict[interface]:
                    ret_dict[interface].setdefault('index', {})
                ret_dict[interface]['index'].setdefault(index, {})
                ret_dict[interface]['index'][index]['queue_id'] = \
                    group['queue_id']
                ret_dict[interface]['index'][index]['name'] = \
                    group['interf_name']
                continue

            m = p3_1.match(line)
            if m:
                ret_dict[interface]['index'][index].setdefault('software_control_info', {})
                continue

            m = p3_2.match(line)
            if m:
                group = m.groupdict()
                ret_dict[interface]['index'][index]['software_control_info']['cache_queue_id'] = group['cache_queue_id']
                ret_dict[interface]['index'][index]['software_control_info']['wred'] = group['wred']
                if group['type'].strip() == 'bytes':
                    ret_dict[interface]['index'][index]['software_control_info']['qlimit_bytes'] = int(group['qlimit'])
                else:
                    ret_dict[interface]['index'][index]['software_control_info']['qlimit_pkts'] = int(group['qlimit'])
                continue

            m = p4.match(line)
            if m:
                group = m.groupdict()
                ret_dict[interface]['index'][index]['software_control_info'].\
                    update({k: v for k, v in group.items()})
                continue

            m = p5.match(line)
            if m:
                group = m.groupdict()
                ret_dict[interface]['index'][index]['software_control_info']['sw_flags'] = group['sw_flags']
                ret_dict[interface]['index'][index]['software_control_info']['sw_state'] = group['sw_state']
                ret_dict[interface]['index'][index]['software_control_info']['port_uidb'] = int(group['port_uidb'])
                continue

            m = p6.match(line)
            if m:
                group = m.groupdict()
                ret_dict[interface]['index'][index]['software_control_info'].\
                    update({k: int(v) for k, v in group.items()})
                continue

            m = p7.match(line)
            if m:
                group = m.groupdict()
                ret_dict[interface]['index'][index]['software_control_info'].\
                    update({k: int(v) for k, v in group.items()})
                continue

            m = p8.match(line)
            if m:
                group = m.groupdict()
                ret_dict[interface]['index'][index]['software_control_info'].\
                    update({k: int(v) for k, v in group.items()})
                continue

            m = p9.match(line)
            if m:
                group = m.groupdict()
                ret_dict[interface]['index'][index]['software_control_info'].\
                    update({k: int(v) for k, v in group.items()})
                continue

            m = p10.match(line)
            if m:
                group = m.groupdict()
                ret_dict[interface]['index'][index]['software_control_info']['share'] = int(group['share'])
                continue

            m = p11.match(line)
            if m:
                group = m.groupdict()
                ret_dict[interface]['index'][index]['software_control_info'].\
                    update({k: int(v) for k, v in group.items()})
                continue

            m = p12.match(line)
            if m:
                group = m.groupdict()
                ret_dict[interface]['index'][index]['software_control_info']['defer_obj_refcnt'] = int(group['defer_obj_refcnt'])

                if group['cp_ppe_addr']:
                    ret_dict[interface]['index'][index]['software_control_info']['cp_ppe_addr'] = group['cp_ppe_addr']
                continue

            m = p13_1.match(line)
            if m:
                ret_dict[interface]['index'][index].setdefault('statistics', {})
                continue

            m = p13_2.match(line)
            if m:
                group = m.groupdict()
                ret_dict[interface]['index'][index]['statistics'].update({k: int(v) for k, v in group.items()})
                continue

            m = p14.match(line)
            if m:
                group = m.groupdict()
                ret_dict[interface]['index'][index]['statistics'].update({k: int(v) for k, v in group.items()})
                continue

            m = p15.match(line)
            if m:
                group = m.groupdict()
                if group['type'].strip() == 'bytes':
                    ret_dict[interface]['index'][index]['statistics']['queue_depth_bytes'] = int(group['queue_depth'])
                else:
                    ret_dict[interface]['index'][index]['statistics']['queue_depth_pkts'] = int(group['queue_depth'])
                continue

            m = p16.match(line)
            if m:
                group = m.groupdict()
                ret_dict[interface]['index'][index]['statistics'].update({k: int(v) for k, v in group.items()})
                continue

        return ret_dict


class ShowPlatformHardwarePlimSchema(MetaParser):
    """Schema for show platform hardware port <x/x/x> plim statistics
                  show platform hardware slot <x> plim statistics
                  show platform hardware slot <x> plim statistics internal
                  show platform hardware subslot <x/x> plim statistics"""

    schema = {
        Optional('port'): {
            Any(): {
                'received': {
                    'low_priority': {
                        'pkts': int,
                        'dropped_pkts': int,
                        'errored_pkts': int,
                        'bytes': int,
                        'dropped_bytes': int,
                        'errored_bytes': int,
                    },
                    'high_priority': {
                        'pkts': int,
                        'dropped_pkts': int,
                        'errored_pkts': int,
                        'bytes': int,
                        'dropped_bytes': int,
                        'errored_bytes': int,
                    }
                },
                'transmitted': {
                    'low_priority': {
                        'pkts': int,
                        'dropped_pkts': int,
                        'bytes': int,
                        'dropped_bytes': int,
                    },
                    'high_priority': {
                        'pkts': int,
                        'dropped_pkts': int,
                        'bytes': int,
                        'dropped_bytes': int,
                    }
                },
            },
        },
        Optional('slot'): {
            Any(): {
                'subslot': {
                    Any(): {
                        'name': str,
                        'status': str,
                        'received': {
                            Optional('pkts'): int,
                            Optional('ipc_pkts'): int,
                            Optional('bytes'): int,
                            Optional('ipc_bytes'): int,
                            Optional('ipc_err'): int,
                            Optional('spi4_interrupt_counters'): {
                                'out_of_frame': int,
                                'dip4_error': int,
                                'disabled': int,
                                'loss_of_sync': int,
                                'sequence_error': int,
                                'burst_error': int,
                                'eop_abort': int,
                                'packet_gap_error': int,
                                'control_word_error': int,
                            }
                        },
                        'transmitted': {
                            Optional('pkts'): int,
                            Optional('ipc_pkts'): int,
                            Optional('bytes'): int,
                            Optional('ipc_bytes'): int,
                            Optional('ipc_err'): int,
                            Optional('spi4_interrupt_counters'): {
                                'out_of_frame': int,
                                'frame_error': int,
                                'fifo_over_flow': int,
                                'dip2_error': int,
                            }
                        }
                    },
                }
            },
        }
    }


class ShowPlatformHardwarePlim(ShowPlatformHardwarePlimSchema):
    """Parser for show platform hardware port <x/x/x> plim statistics
                  show platform hardware slot <x> plim statistics
                  show platform hardware slot <x> plim statistics internal
                  show platform hardware subslot <x/x> plim statistics"""

    cli_command = ['show platform hardware port {port} plim statistics',
                   'show platform hardware slot {slot} plim statistics',
                   'show platform hardware slot {slot} plim statistics internal',
                   'show platform hardware subslot {subslot} plim statistics']

    def cli(self, port=None, slot=None, subslot=None, internal=False, output=None):

        if output is None:
            if port:
                cmd = self.cli_command[0].format(port=port)
            elif slot:
                if internal:
                    cmd = self.cli_command[2].format(slot=slot)
                else:
                    cmd = self.cli_command[1].format(slot=slot)
            elif subslot:
                cmd = self.cli_command[3].format(subslot=subslot)
            out = self.device.execute(cmd)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # Interface 0/0/0
        p1 = re.compile(r'^Interface +(?P<port>[\d\/]+)$')

        #   RX Low Priority
        #   RX High Priority
        p2 = re.compile(r'^RX +(?P<direction>\w+) +Priority$')

        #     RX Pkts      369         Bytes 27789
        p3 = re.compile(r'^RX +Pkts +(?P<rx_total_pkts>\d+) +Bytes +(?P<rx_total_bytes>\d+)$')

        #     RX Drop Pkts 0           Bytes 0
        p4 = re.compile(r'^RX +Drop +Pkts +(?P<rx_dropped_pkts>\d+) +Bytes +(?P<rx_dropped_bytes>\d+)$')

        #     RX Err  Pkts 0           Bytes 0
        p5 = re.compile(r'^RX +Err +Pkts +(?P<rx_errored_pkts>\d+) +Bytes +(?P<rx_errored_bytes>\d+)$')

        #   TX Low Priority
        #   TX High Priority
        p6 = re.compile(r'^TX +(?P<direction>\w+) +Priority$')

        #     TX Pkts      1265574622  Bytes 250735325722
        p7 = re.compile(r'^TX +Pkts +(?P<tx_total_pkts>\d+) +Bytes +(?P<tx_total_bytes>\d+)$')

        #     TX Drop Pkts 0           Bytes 0
        p8 = re.compile(r'^TX +Drop +Pkts +(?P<tx_dropped_pkts>\d+) +Bytes +(?P<tx_dropped_bytes>\d+)$')

        # 0/3, SPA-1XTENGE-XFP-V2, Online
        p9 = re.compile(r'^(?P<slot>\d+)/(?P<subslot>\d+),'
                        ' +(?P<name>[\w\d\-]+),'
                        ' +(?P<status>\w+)$')

        #   RX IPC Pkts 0           Bytes 0
        p10 = re.compile(r'^RX +IPC +Pkts +(?P<rx_ipc_pkts>\d+) +Bytes +(?P<rx_ipc_bytes>\d+)$')

        #   TX IPC Pkts 0           Bytes 0
        p11 = re.compile(r'^TX +IPC +Pkts +(?P<tx_ipc_pkts>\d+) +Bytes +(?P<tx_ipc_bytes>\d+)$')

        #   RX IPC Err 0
        p12 = re.compile(r'^RX +IPC +Err +(?P<rx_ipc_err>\d+)$')

        #   TX IPC Err 0
        p13 = re.compile(r'^TX +IPC +Err +(?P<tx_ipc_err>\d+)$')

        #   RX Spi4 Interrupt Counters
        #   TX Spi4 Interrupt Counters
        p14 = re.compile(r'^(?P<tx_rx>\w+) +Spi4 +Interrupt +Counters$')

        #     Out Of Frame 0
        p15 = re.compile(r'^Out +Of +Frame +(?P<out_of_frame>\d+)$')

        #     Dip4 Error 0
        p16 = re.compile(r'^Dip4 +Error +(?P<rx_dip4_error>\d+)$')

        #     Disabled 0
        p17 = re.compile(r'^Disabled +(?P<rx_disbaled>\d+)$')

        #     Loss Of Sync 0
        p18 = re.compile(r'^Loss +Of +Sync +(?P<rx_loss_of_sync>\d+)$')

        #     Sequence Error 0
        p19 = re.compile(r'^Sequence +Error +(?P<rx_sequence_error>\d+)$')

        #     Burst Error 0
        p20 = re.compile(r'^Burst +Error +(?P<rx_burst_error>\d+)$')

        #     EOP Abort 0
        p21 = re.compile(r'^EOP +Abort +(?P<rx_eop_abort>\d+)$')

        #     Packet Gap Error 0
        p22 = re.compile(r'^Packet +Gap +Error +(?P<rx_packet_gap_error>\d+)$')

        #     Control Word Error 0
        p23 = re.compile(r'^Control +Word +Error +(?P<rx_control_word_error>\d+)$')

        #     Frame Error 0
        p24 = re.compile(r'^Frame +Error +(?P<tx_frame_error>\d+)$')

        #     FIFO Over Flow 0
        p25 = re.compile(r'^FIFO +Over +Flow +(?P<tx_fifo_over_flow>\d+)$')

        #     Dip2 Error 0
        p26 = re.compile(r'^Dip2 +Error +(?P<tx_dip2_error>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                port = group['port']
                ret_dict.setdefault('port', {}).setdefault(port, {})
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                direction = group['direction']
                if 'received' not in ret_dict['port'][port]:
                    ret_dict['port'][port].setdefault('received', {})
                if direction == 'Low':
                    low_high = 'low_priority'
                else:
                    low_high = 'high_priority'
                ret_dict['port'][port]['received'].setdefault(low_high, {})
                continue

            m = p3.match(line)
            if m:
                group = m.groupdict()
                if 'port' in ret_dict:
                    ret_dict['port'][port]['received'][low_high]['pkts'] = int(group['rx_total_pkts'])
                    ret_dict['port'][port]['received'][low_high]['bytes'] = int(group['rx_total_bytes'])
                else:
                    if 'received' not in ret_dict['slot'][slot]['subslot'][subslot]:
                        ret_dict['slot'][slot]['subslot'][subslot].\
                            setdefault('received', {})
                    ret_dict['slot'][slot]['subslot'][subslot]['received']['pkts'] = int(group['rx_total_pkts'])
                    ret_dict['slot'][slot]['subslot'][subslot]['received']['bytes'] = int(group['rx_total_bytes'])
                continue

            m = p4.match(line)
            if m:
                group = m.groupdict()
                ret_dict['port'][port]['received'][low_high]['dropped_pkts'] = int(group['rx_dropped_pkts'])
                ret_dict['port'][port]['received'][low_high]['dropped_bytes'] = int(group['rx_dropped_bytes'])
                continue

            m = p5.match(line)
            if m:
                group = m.groupdict()
                ret_dict['port'][port]['received'][low_high]['errored_pkts'] = int(group['rx_errored_pkts'])
                ret_dict['port'][port]['received'][low_high]['errored_bytes'] = int(group['rx_errored_bytes'])
                continue

            m = p6.match(line)
            if m:
                group = m.groupdict()
                direction = group['direction']
                if 'transmitted' not in ret_dict['port'][port]:
                    ret_dict['port'][port].setdefault('transmitted', {})
                if direction == 'Low':
                    low_high = 'low_priority'
                else:
                    low_high = 'high_priority'
                ret_dict['port'][port]['transmitted'].setdefault(low_high, {})
                continue

            m = p7.match(line)
            if m:
                group = m.groupdict()
                if 'port' in ret_dict:
                    ret_dict['port'][port]['transmitted'][low_high]['pkts'] = int(group['tx_total_pkts'])
                    ret_dict['port'][port]['transmitted'][low_high]['bytes'] = int(group['tx_total_bytes'])
                else:
                    if 'transmitted' not in ret_dict['slot'][slot]['subslot'][subslot]:
                        ret_dict['slot'][slot]['subslot'][subslot].setdefault('transmitted', {})
                    ret_dict['slot'][slot]['subslot'][subslot]['transmitted']['pkts'] = int(group['tx_total_pkts'])
                    ret_dict['slot'][slot]['subslot'][subslot]['transmitted']['bytes'] = int(group['tx_total_bytes'])
                continue

            m = p8.match(line)
            if m:
                group = m.groupdict()
                ret_dict['port'][port]['transmitted'][low_high]['dropped_pkts'] = int(group['tx_dropped_pkts'])
                ret_dict['port'][port]['transmitted'][low_high]['dropped_bytes'] = int(group['tx_dropped_bytes'])
                continue

            m = p9.match(line)
            if m:
                group = m.groupdict()
                slot = group['slot']
                subslot = group['subslot']
                ret_dict.setdefault('slot', {}).setdefault(slot, {})
                if 'subslot' not in ret_dict['slot'][slot]:
                    ret_dict['slot'][slot].setdefault('subslot', {})
                ret_dict['slot'][slot]['subslot'].setdefault(subslot, {})
                ret_dict['slot'][slot]['subslot'][subslot]['name'] = \
                    group['name']
                ret_dict['slot'][slot]['subslot'][subslot]['status'] = \
                    group['status']
                continue

            m = p10.match(line)
            if m:
                group = m.groupdict()
                if 'received' not in ret_dict['slot'][slot]['subslot'][subslot]:
                    ret_dict['slot'][slot]['subslot'][subslot].setdefault('received', {})
                ret_dict['slot'][slot]['subslot'][subslot]['received']['ipc_pkts'] = int(group['rx_ipc_pkts'])
                ret_dict['slot'][slot]['subslot'][subslot]['received']['ipc_bytes'] = int(group['rx_ipc_bytes'])
                continue

            m = p11.match(line)
            if m:
                group = m.groupdict()
                if 'transmitted' not in ret_dict['slot'][slot]['subslot'][subslot]:
                    ret_dict['slot'][slot]['subslot'][subslot].setdefault('transmitted', {})
                ret_dict['slot'][slot]['subslot'][subslot]['transmitted']['ipc_pkts'] = int(group['tx_ipc_pkts'])
                ret_dict['slot'][slot]['subslot'][subslot]['transmitted']['ipc_bytes'] = int(group['tx_ipc_bytes'])
                continue

            m = p12.match(line)
            if m:
                group = m.groupdict()
                ret_dict['slot'][slot]['subslot'][subslot].setdefault('received', {})
                ret_dict['slot'][slot]['subslot'][subslot]['received']['ipc_err'] = int(group['rx_ipc_err'])
                continue

            m = p13.match(line)
            if m:
                group = m.groupdict()
                ret_dict['slot'][slot]['subslot'][subslot].setdefault('transmitted', {})
                ret_dict['slot'][slot]['subslot'][subslot]['transmitted']['ipc_err'] = int(group['tx_ipc_err'])
                continue

            m = p14.match(line)
            if m:
                group = m.groupdict()
                tx_rx_direction = group['tx_rx']
                if tx_rx_direction == 'RX':
                    new_direction = 'received'
                else:
                    new_direction = 'transmitted'
                ret_dict['slot'][slot]['subslot'][subslot][new_direction].\
                    setdefault('spi4_interrupt_counters', {})
                continue

            m = p15.match(line)
            if m:
                group = m.groupdict()
                ret_dict['slot'][slot]['subslot'][subslot][new_direction]['spi4_interrupt_counters']['out_of_frame'] = int(group['out_of_frame'])
                continue

            m = p16.match(line)
            if m:
                group = m.groupdict()
                ret_dict['slot'][slot]['subslot'][subslot][new_direction]['spi4_interrupt_counters']['dip4_error'] = int(group['rx_dip4_error'])
                continue

            m = p17.match(line)
            if m:
                group = m.groupdict()
                ret_dict['slot'][slot]['subslot'][subslot][new_direction]['spi4_interrupt_counters']['disabled'] = int(group['rx_disbaled'])
                continue

            m = p18.match(line)
            if m:
                group = m.groupdict()
                ret_dict['slot'][slot]['subslot'][subslot][new_direction]['spi4_interrupt_counters']['loss_of_sync'] = int(group['rx_loss_of_sync'])
                continue

            m = p19.match(line)
            if m:
                group = m.groupdict()
                ret_dict['slot'][slot]['subslot'][subslot][new_direction]['spi4_interrupt_counters']['sequence_error'] = int(group['rx_sequence_error'])
                continue

            m = p20.match(line)
            if m:
                group = m.groupdict()
                ret_dict['slot'][slot]['subslot'][subslot][new_direction]['spi4_interrupt_counters']['burst_error'] = int(group['rx_burst_error'])
                continue

            m = p21.match(line)
            if m:
                group = m.groupdict()
                ret_dict['slot'][slot]['subslot'][subslot][new_direction]['spi4_interrupt_counters']['eop_abort'] = int(group['rx_eop_abort'])
                continue

            m = p22.match(line)
            if m:
                group = m.groupdict()
                ret_dict['slot'][slot]['subslot'][subslot][new_direction]['spi4_interrupt_counters']['packet_gap_error'] = int(group['rx_packet_gap_error'])
                continue

            m = p23.match(line)
            if m:
                group = m.groupdict()
                ret_dict['slot'][slot]['subslot'][subslot][new_direction]['spi4_interrupt_counters']['control_word_error'] = int(group['rx_control_word_error'])
                continue

            m = p24.match(line)
            if m:
                group = m.groupdict()
                ret_dict['slot'][slot]['subslot'][subslot][new_direction]['spi4_interrupt_counters']['frame_error'] = int(group['tx_frame_error'])
                continue

            m = p25.match(line)
            if m:
                group = m.groupdict()
                ret_dict['slot'][slot]['subslot'][subslot][new_direction]['spi4_interrupt_counters']['fifo_over_flow'] = int(group['tx_fifo_over_flow'])
                continue

            m = p26.match(line)
            if m:
                group = m.groupdict()
                ret_dict['slot'][slot]['subslot'][subslot][new_direction]['spi4_interrupt_counters']['dip2_error'] = int(group['tx_dip2_error'])
                continue

        return ret_dict


class ShowPlatformHardwareQfpBqsMappingSchema(MetaParser):
    """Schema for show platform hardware qfp active bqs <x> ipm mapping
                  show platform hardware qfp standby bqs <x> ipm mapping
                  show platform hardware qfp active bqs <x> opm mapping
                  show platform hardware qfp standby bqs <x> opm mapping"""

    schema = {
        'channel': {
            Any(): {
                Optional('interface'): str,
                'name': str,
                Optional('logical_channel'): int,
                Optional('drain_mode'): bool,
                Optional('port'): int,
                Optional('cfifo'): int,
            },
        }
    }


class ShowPlatformHardwareQfpBqsOpmMapping(ShowPlatformHardwareQfpBqsMappingSchema):
    """Parser for show platform hardware qfp active bqs <x> opm mapping
                  show platform hardware qfp standby bqs <x> opm mapping"""

    cli_command = 'show platform hardware qfp {status} bqs {slot} opm mapping'

    def cli(self, status, slot, output=None):

        if output is None:
            cmd = self.cli_command.format(status=status, slot=slot)
            out = self.device.execute(cmd)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # Chan     Name                          Interface      LogicalChannel
        #  0       CC0 Low                       SPI0            0
        # 24       Peer-FP Low                   SPI0           24
        # 26       Nitrox Low                    SPI0           26
        # 28       HT Pkt Low                    HT              0
        # 38       HighNormal                    GPM             7
        # 55*      Drain Low                     GPM             0
        # * - indicates the drain mode bit is set for this channel
        p1 = re.compile(r'^(?P<number>\d+)(?P<drained>\*)? +(?P<name>[\w\-\s]+)'
                        ' +(?P<interface>[\w\d]+) +(?P<logical_channel>\d+)$')

        # 32       Unmapped
        p2 = re.compile(r'^(?P<unmapped_number>\d+) +Unmapped$')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                interface = group['interface']
                number = group['number']
                if group['drained']:
                    drained = True
                else:
                    drained = False
                if 'channel' not in ret_dict:
                    final_dict = ret_dict.setdefault('channel', {})
                final_dict = ret_dict['channel'].setdefault(number, {})
                final_dict.update({'interface': group['interface'].strip()})
                final_dict.update({'name': group['name'].strip()})
                final_dict.update({'logical_channel': int(group['logical_channel'])})
                final_dict.update({'drain_mode': drained})
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                unmapped_number = group['unmapped_number']
                if 'channel' not in ret_dict:
                    ret_dict.setdefault('channel', {})
                ret_dict['channel'].setdefault(unmapped_number, {})
                ret_dict['channel'][unmapped_number].update({'name': 'unmapped'})
                continue

        return ret_dict


class ShowPlatformHardwareQfpBqsIpmMapping(ShowPlatformHardwareQfpBqsMappingSchema):
    """Parser for show platform hardware qfp active bqs <x> ipm mapping
                  show platform hardware qfp standby bqs <x> ipm mapping"""

    cli_command = 'show platform hardware qfp {status} bqs {slot} ipm mapping'

    def cli(self, status, slot, output=None):

        if output is None:
            cmd = self.cli_command.format(status=status, slot=slot)
            out = self.device.execute(cmd)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # Chan   Name                Interface      Port     CFIFO
        #  1     CC3 Low             SPI0           0        1
        # 13     Peer-FP Low         SPI0          12        3
        # 15     Nitrox Low          SPI0          14        1
        # 17     HT Pkt Low          HT             0        1
        # 21     CC4 Low             SPI0          16        1
        p1 = re.compile(r'^(?P<number>\d+) +(?P<name>[\w\-\s]+)'
                        ' +(?P<interface>[\w\d]+) +(?P<port>\d+)'
                        ' +(?P<cfifo>\d+)$')

        # 32       Unmapped
        p2 = re.compile(r'^(?P<unmapped_number>\d+) +Unmapped$')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                number = group['number']
                final_dict = ret_dict.setdefault(
                    'channel', {}).setdefault(number, {})
                final_dict.update({'interface': group['interface'].strip()})
                final_dict.update({'name': group['name'].strip()})
                final_dict.update({'port': int(group['port'])})
                final_dict.update({'cfifo': int(group['cfifo'])})
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                unmapped_number = group['unmapped_number']
                if 'channel' not in ret_dict:
                    ret_dict.setdefault('channel', {})
                ret_dict['channel'].setdefault(unmapped_number, {})
                ret_dict['channel'][unmapped_number].update({'name': 'unmapped'})
                continue

        return ret_dict


class ShowPlatformHardwareSerdesSchema(MetaParser):
    """Schema for show platform hardware slot <x> serdes statistics
                  show platform hardware slot <x> serdes statistics internal"""

    schema = {
        'link': {
            Any(): {
                Optional('from'): {
                    'pkts': {
                        Optional('total'): int,
                        Optional('high'): int,
                        Optional('low'): int,
                        Optional('dropped'): int,
                        Optional('errored'): int,
                        Optional('looped'): int,
                        Optional('bad'): int,
                    },
                    'bytes': {
                        Optional('total'): int,
                        Optional('high'): int,
                        Optional('low'): int,
                        Optional('dropped'): int,
                        Optional('errored'): int,
                        Optional('looped'): int,
                        Optional('bad'): int,
                    },
                    Optional('qstat_count'): int,
                    Optional('flow_ctrl_count'): int,
                },
                Optional('to'): {
                    'pkts': {
                        Optional('total'): int,
                        Optional('high'): int,
                        Optional('low'): int,
                        Optional('dropped'): int,
                        Optional('errored'): int,
                    },
                    Optional('bytes'): {
                        Optional('total'): int,
                        Optional('high'): int,
                        Optional('low'): int,
                        Optional('dropped'): int,
                        Optional('errored'): int,
                    }
                },
                Optional('local_tx_in_sync'): bool,
                Optional('local_rx_in_sync'): bool,
                Optional('remote_tx_in_sync'): bool,
                Optional('remote_rx_in_sync'): bool,
                Optional('errors'): {
                    'rx_process': int,
                    'rx_schedule': int,
                    'rx_statistics': int,
                    'rx_parity': int,
                    'tx_process': int,
                    'tx_schedule': int,
                    'tx_statistics': int,
                },
            },
        },
        Optional('serdes_exception_counts'): {
            Any(): {
                Optional('link'): {
                    Any(): {
                        'msgTypeError': int,
                        'msgEccError': int,
                        'chicoEvent': int,
                    },
                }
            },
        }
    }


class ShowPlatformHardwareSerdes(ShowPlatformHardwareSerdesSchema):
    """Parser for show platform hardware slot <x> serdes statistics"""

    cli_command = 'show platform hardware slot {slot} serdes statistics'

    def cli(self, slot, output=None):

        if output is None:
            cmd = self.cli_command.format(slot=slot)
            out = self.device.execute(cmd)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # From Slot 1-Link B
        p1 = re.compile(r'^From +Slot +(?P<link>[\w\d\-\s]+)$')

        #   Pkts  High: 0          Low: 0          Bad: 0          Dropped: 0
        p2 = re.compile(r'^Pkts +High: +(?P<high>\d+) +Low: +(?P<low>\d+)( +Bad: +(?P<bad>\d+) +Dropped: +(?P<dropped>\d+))?$')

        #   Bytes High: 0          Low: 0          Bad: 0          Dropped: 0
        p3 = re.compile(r'^Bytes +High: +(?P<high>\d+) +Low: +(?P<low>\d+) +Bad: +(?P<bad>\d+) +Dropped: +(?P<dropped>\d+)$')

        #   Pkts  Looped: 0          Error: 0
        p4 = re.compile(r'^Pkts +Looped: +(?P<looped>\d+) +Error: +(?P<errored>\d+)$')

        #   Bytes Looped 0
        p5 = re.compile(r'^Bytes +Looped +(?P<looped>\d+)$')

        #   Qstat count: 0          Flow ctrl count: 3501
        p6 = re.compile(r'^Qstat +count: +(?P<qstat_count>\d+) +Flow +ctrl +count: +(?P<flow_ctrl_count>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                slot = group['link']
                from_dict = ret_dict.setdefault('link', {}).setdefault(slot, {}).setdefault('from', {})
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                if not group['bad']:
                    to_dict = ret_dict['link'][slot].setdefault('to', {}).setdefault('pkts', {})
                    to_dict.update({k: int(v) for k, v in group.items() if v})
                    continue

                pkts_dict = ret_dict['link'][slot]['from'].setdefault('pkts', {})
                pkts_dict.update({k: int(v) for k, v in group.items()})
                continue

            m = p3.match(line)
            if m:
                group = m.groupdict()
                bytes_dict = ret_dict['link'][slot]['from'].setdefault('bytes', {})
                bytes_dict.update({k: int(v) for k, v in group.items()})
                continue

            m = p4.match(line)
            if m:
                group = m.groupdict()
                pkts_dict.update({k: int(v) for k, v in group.items()})
                continue

            m = p5.match(line)
            if m:
                group = m.groupdict()
                bytes_dict.update({k: int(v) for k, v in group.items()})
                continue

            m = p6.match(line)
            if m:
                group = m.groupdict()
                from_dict.update({k: int(v) for k, v in group.items()})
                continue

        return ret_dict


class ShowPlatformHardwareSerdesInternal(ShowPlatformHardwareSerdesSchema):
    """Parser for show platform hardware slot <x> serdes statistics internal"""

    cli_command = 'show platform hardware slot {slot} serdes statistics internal'

    def cli(self, slot, output=None):

        if output is None:
            cmd = self.cli_command.format(slot=slot)
            out = self.device.execute(cmd)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # Network-Processor-0 Link:
        # RP/ESP Link:
        p1 = re.compile(r'^(?P<link>[\w\d\-\s/]+) +Link:$')

        #   Local TX in sync, Local RX in sync
        p2 = re.compile(r'^Local +TX +in +sync, +Local +RX +in +sync$')

        #   Remote TX in sync, Remote RX in sync
        p3 = re.compile(r'^Remote +TX +in +sync, +Remote +RX +in +sync$')

        #   To Network-Processor       Packets:    21763844  Bytes:  7343838083
        #   To Encryption Processor   Packets:           0  Bytes:           0
        #   To RP/ESP Packets: 1150522 Bytes: 166031138
        p4 = re.compile(r'^To +(?P<link_name_1>[\w\-\d\s/]+) +Packets: +(?P<to_packets>\d+) +Bytes: +(?P<to_bytes>\d+)$')

        #   From Network-Processor     Packets:    21259012  Bytes:  7397920802
        #   From RP/ESP Packets: 4364008 Bytes: 697982854
        p5 = re.compile(r'^From +(?P<link_name_2>[\w\-\d\s/]+) +Packets: +(?P<from_packets>\d+) +Bytes: +(?P<from_bytes>\d+)$')

        #     Drops                   Packets:           0  Bytes:           0
        p6 = re.compile(r'^Drops +Packets: +(?P<dropped_packets>\d+) +Bytes: +(?P<dropped_bytes>\d+)$')

        #     Errors                  Packets:           0  Bytes:           0
        p7 = re.compile(r'^Errors +Packets: +(?P<errored_packets>\d+) +Bytes: +(?P<errored_bytes>\d+)$')

        #     Errors:
        p8 = re.compile(r'^Errors:$')

        #     RX/TX process: 0/0, RX/TX schedule: 0/0
        p9 = re.compile(r'^RX/TX +process: +(?P<rx_process>\d+)/(?P<tx_process>\d+), +RX/TX +schedule: +(?P<rx_schedule>\d+)/(?P<tx_schedule>\d+)$')

        #     RX/TX statistics: 0/0, RX parity: 0
        p10 = re.compile(r'^RX/TX +statistics: +(?P<rx_statistics>\d+)/(?P<tx_statistics>\d+), +RX +parity: +(?P<rx_parity>\d+)$')

        # Serdes Exception Counts:
        p11 = re.compile(r'^Serdes +Exception +Counts:$')

        #   eqs/fc:
        #   idh-hi:
        #   spi link:
        p12 = re.compile(r'^(?P<link>[\w\d\-\s\/]+):$')

        #     link 0: msgTypeError: 5
        #     link 0: msgEccError: 5
        #     link 0: chicoEvent: 5
        #     link 1: msgTypeError: 1
        #     link 1: msgEccError: 1
        #     link 1: chicoEvent: 1
        #     link 2: msgTypeError: 3
        #     link 2: msgEccError: 3
        #     link 2: chicoEvent: 3
        p13 = re.compile(r'^link +(?P<link_number>\d+): +(?P<error_event>\w+): +(?P<count>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                link = group['link']
                new_dict = ret_dict.setdefault('link', {}).setdefault(link, {})
                continue

            m = p2.match(line)
            if m:
                new_dict['local_tx_in_sync'] = True
                new_dict['local_rx_in_sync'] = True
                continue

            m = p3.match(line)
            if m:
                new_dict['remote_tx_in_sync'] = True
                new_dict['remote_rx_in_sync'] = True
                continue

            m = p4.match(line)
            if m:
                group = m.groupdict()
                to_not_from = True
                new_dict.setdefault('to', {}).setdefault('pkts', {})
                new_dict['to'].setdefault('bytes', {})
                new_dict['to']['pkts']['total'] = int(group['to_packets'])
                new_dict['to']['bytes']['total'] = int(group['to_bytes'])
                continue

            m = p5.match(line)
            if m:
                group = m.groupdict()
                to_not_from = False
                new_dict.setdefault('from', {}).setdefault('pkts', {})
                new_dict['from'].setdefault('bytes', {})
                new_dict['from']['pkts']['total'] = int(group['from_packets'])
                new_dict['from']['bytes']['total'] = int(group['from_bytes'])
                continue

            m = p6.match(line)
            if m:
                group = m.groupdict()
                if to_not_from:
                    new_dict['to']['pkts']['dropped'] = int(group['dropped_packets'])
                    new_dict['to']['bytes']['dropped'] = int(group['dropped_bytes'])
                else:
                    new_dict['from']['pkts']['dropped'] = int(group['dropped_packets'])
                    new_dict['from']['bytes']['dropped'] = int(group['dropped_bytes'])
                continue

            m = p7.match(line)
            if m:
                group = m.groupdict()
                if to_not_from:
                    new_dict['to']['pkts']['errored'] = int(group['errored_packets'])
                    new_dict['to']['bytes']['errored'] = int(group['errored_bytes'])
                else:
                    new_dict['from']['pkts']['errored'] = int(group['errored_packets'])
                    new_dict['from']['bytes']['errored'] = int(group['errored_bytes'])
                continue

            m = p8.match(line)
            if m:
                continue

            m = p9.match(line)
            if m:
                group = m.groupdict()
                new_dict.setdefault('errors', {})
                new_dict['errors'].update({k: int(v)
                                           for k, v in group.items()})
                continue

            m = p10.match(line)
            if m:
                group = m.groupdict()
                if 'errors' in ret_dict['link'][link]:
                    new_dict['errors'].update(
                        {k: int(v) for k, v in group.items()})
                continue

            m = p11.match(line)
            if m:
                serdes_exception_counts = True
                ret_dict.setdefault('serdes_exception_counts', {})
                continue

            m = p12.match(line)
            if m:
                group = m.groupdict()
                link = group['link']
                ret_dict['serdes_exception_counts'].setdefault(link, {})
                continue

            m = p13.match(line)
            if m:
                group = m.groupdict()
                link_number = group['link_number']
                error_event = group['error_event']
                ret_dict['serdes_exception_counts'][link].setdefault('link', {}).setdefault(link_number, {})
                ret_dict['serdes_exception_counts'][link]['link'][link_number][error_event] = int(group['count'])
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


class ShowPlatformHardwareQfpBqsStatisticsChannelAllSchema(MetaParser):
    """Schema for show platform hardware qfp active bqs <x> ipm statistics channel all
                  show platform hardware qfp standby bqs <x> ipm statistics channel all
                  show platform hardware qfp active bqs <x> opm statistics channel all
                  show platform hardware qfp standby bqs <x> opm statistics channel all"""

    schema = {
        'channel': {
            Any(): {
                'goodpkts': str,
                'goodbytes': str,
                'badpkts': str,
                'badbytes': str,
                Optional('comment'): str,
            },
        }
    }


class ShowPlatformHardwareQfpBqsStatisticsChannelAll(ShowPlatformHardwareQfpBqsStatisticsChannelAllSchema):
    """Parser for show platform hardware qfp active bqs <x> ipm statistics channel all
                  show platform hardware qfp standby bqs <x> ipm statistics channel all
                  show platform hardware qfp active bqs <x> opm statistics channel all
                  show platform hardware qfp standby bqs <x> opm statistics channel all"""

    cli_command = 'show platform hardware qfp {status} bqs {slot} {iotype} statistics channel all'

    def cli(self, status='active', slot='0', iotype='ipm', output=None):

        if output is None:
            cmd = self.cli_command.format(
                status=status, slot=slot, iotype=iotype)
            out = self.device.execute(cmd)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # Chan   GoodPkts  GoodBytes    BadPkts   BadBytes
        # 1 - 0000000000 0000000000 0000000000 0000000000
        # 2 - 0000c40f64 016a5004b0 0000000000 0000000000
        p1 = re.compile(r'^(?P<channel>\d+) +- +(?P<goodpkts>\w+) +(?P<goodbytes>\w+) +(?P<badpkts>\w+) +(?P<badbytes>\w+)$')

        #  0-55: OPM Channels
        # 56-59: Metapacket/Recycle Pools 0-3
        #    60: Reassembled Packets Sent to QED
        p2 = re.compile(r'^(?P<channel>\d+)-?(?P<end_channel>\d+)?: +(?P<comment>.+)$')

        for line in out.splitlines():
            line = line.strip()
            m = p1.match(line)
            if m:
                group = m.groupdict()
                channel = int(group.pop('channel'))
                chan_dict = ret_dict.setdefault('channel', {}).setdefault(channel, {})
                chan_dict.update({k: v for k, v in group.items()})
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                channel = int(group['channel'])
                comment = group['comment']
                if group['end_channel']:
                    end_channel = int(group['end_channel'])
                    for i in range(channel, end_channel + 1):
                        ret_dict['channel'][i].update({'comment': comment})
                else:
                    ret_dict['channel'][channel].update({'comment': comment})

                continue

        return ret_dict


class ShowPlatformHardwareQfpBqsMappingSchema(MetaParser):
    """Schema for show platform hardware qfp active bqs <x> ipm mapping
                  show platform hardware qfp standby bqs <x> ipm mapping
                  show platform hardware qfp active bqs <x> opm mapping
                  show platform hardware qfp standby bqs <x> opm mapping"""

    schema = {
        'channel': {
            Any(): {
                Optional('interface'): str,
                'name': str,
                Optional('logical_channel'): int,
                Optional('drain_mode'): bool,
                Optional('port'): int,
                Optional('cfifo'): int,
            },
        }
    }


class ShowPlatformHardwareQfpBqsOpmMapping(ShowPlatformHardwareQfpBqsMappingSchema):
    """Parser for show platform hardware qfp active bqs <x> opm mapping
                  show platform hardware qfp standby bqs <x> opm mapping"""

    cli_command = 'show platform hardware qfp {status} bqs {slot} opm mapping'

    def cli(self, status, slot, output=None):

        if output is None:
            cmd = self.cli_command.format(status=status, slot=slot)
            out = self.device.execute(cmd)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # Chan     Name                          Interface      LogicalChannel
        #  0       CC0 Low                       SPI0            0
        # 24       Peer-FP Low                   SPI0           24
        # 26       Nitrox Low                    SPI0           26
        # 28       HT Pkt Low                    HT              0
        # 38       HighNormal                    GPM             7
        # 55*      Drain Low                     GPM             0
        # * - indicates the drain mode bit is set for this channel
        p1 = re.compile(r'^(?P<number>\d+)(?P<drained>\*)? +(?P<name>[\w\-\s]+)'
                        ' +(?P<interface>[\w\d]+) +(?P<logical_channel>\d+)$')

        # 32       Unmapped
        p2 = re.compile(r'^(?P<unmapped_number>\d+) +Unmapped$')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                interface = group['interface']
                number = group['number']
                if group['drained']:
                    drained = True
                else:
                    drained = False
                if 'channel' not in ret_dict:
                    final_dict = ret_dict.setdefault('channel', {})
                final_dict = ret_dict['channel'].setdefault(number, {})
                final_dict.update({'interface': group['interface'].strip()})
                final_dict.update({'name': group['name'].strip()})
                final_dict.update({'logical_channel': int(group['logical_channel'])})
                final_dict.update({'drain_mode': drained})
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                unmapped_number = group['unmapped_number']
                if 'channel' not in ret_dict:
                    ret_dict.setdefault('channel', {})
                ret_dict['channel'].setdefault(unmapped_number, {})
                ret_dict['channel'][unmapped_number].update({'name': 'unmapped'})
                continue

        return ret_dict


class ShowPlatformHardwareQfpBqsIpmMapping(ShowPlatformHardwareQfpBqsMappingSchema):
    """Parser for show platform hardware qfp active bqs <x> ipm mapping
                  show platform hardware qfp standby bqs <x> ipm mapping"""

    cli_command = 'show platform hardware qfp {status} bqs {slot} ipm mapping'

    def cli(self, status, slot, output=None):

        if output is None:
            cmd = self.cli_command.format(status=status, slot=slot)
            out = self.device.execute(cmd)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # Chan   Name                Interface      Port     CFIFO
        #  1     CC3 Low             SPI0           0        1
        # 13     Peer-FP Low         SPI0          12        3
        # 15     Nitrox Low          SPI0          14        1
        # 17     HT Pkt Low          HT             0        1
        # 21     CC4 Low             SPI0          16        1
        p1 = re.compile(r'^(?P<number>\d+) +(?P<name>[\w\-\s]+)'
                        ' +(?P<interface>[\w\d]+) +(?P<port>\d+)'
                        ' +(?P<cfifo>\d+)$')

        # 32       Unmapped
        p2 = re.compile(r'^(?P<unmapped_number>\d+) +Unmapped$')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                number = group['number']
                final_dict = ret_dict.setdefault('channel', {}).setdefault(number, {})
                final_dict.update({'interface': group['interface'].strip()})
                final_dict.update({'name': group['name'].strip()})
                final_dict.update({'port': int(group['port'])})
                final_dict.update({'cfifo': int(group['cfifo'])})
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                unmapped_number = group['unmapped_number']
                if 'channel' not in ret_dict:
                    ret_dict.setdefault('channel', {})
                ret_dict['channel'].setdefault(unmapped_number, {})
                ret_dict['channel'][unmapped_number].update({'name': 'unmapped'})
                continue

        return ret_dict


class ShowPlatformHardwareQfpInterfaceIfnameStatisticsSchema(MetaParser):
    """Schema for show platform hardware qfp active interface if-name <interface> statistics
                  show platform hardware qfp standby interface if-name <interface> statistics"""

    schema = {
        'qfp': {
            'active': {
                'interface': {
                    Any(): {
                        Optional('platform_handle'): int,
                        'receive_stats': {
                            Any(): {
                                'packets': int,
                                'octets': int,
                            },
                        },
                        'transmit_stats': {
                            Any(): {
                                'packets': int,
                                'octets': int,
                            },
                        },
                        'ingress_drop_stats': {
                            Optional(Any()): {
                                'packets': int,
                                'octets': int,
                            },
                        },
                        'egress_drop_stats': {
                            Optional(Any()): {
                                'packets': int,
                                'octets': int,
                            },
                        }
                    },
                }
            }
        }
    }


class ShowPlatformHardwareQfpInterfaceIfnameStatistics(ShowPlatformHardwareQfpInterfaceIfnameStatisticsSchema):
    """Parser for show platform hardware qfp active interface if-name <interface> statistics
                  show platform hardware qfp standby interface if-name <interface> statistics"""

    cli_command = 'show platform hardware qfp {status} interface if-name {interface} statistics'

    def cli(self, status, interface, output=None):

        if output is None:
            cmd = self.cli_command.format(status=status, interface=interface)
            out = self.device.execute(cmd)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}
        current_stats = None
        final_dict = {}

        # Platform Handle 7
        p1 = re.compile(r'^Platform +Handle +(?P<platform_handle>\d+)$')

        # Receive Stats                             Packets        Octets
        # Transmit Stats                            Packets        Octets
        # Input Drop Stats                          Packets        Octets
        # Output Drop Stats                         Packets        Octets
        p2 = re.compile(r'^(?P<transmit_receive>[\w\s]+) +Stats +Packets +Octets$')

        #   FragmentedIpv6                             0               0
        #   Other
        p3 = re.compile(r'^(?P<stats>[\w\d]+) +(?P<packets>[\w\d]+) +(?P<octets>[\w\d]+)$')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                converted_interface = Common.convert_intf_name(interface)
                final_dict = ret_dict.setdefault('qfp', {}).setdefault(
                    'active', {}).setdefault('interface', {}).setdefault(converted_interface, {})
                final_dict['platform_handle'] = int(group['platform_handle'])
                continue

            m = p2.match(line)
            if m:
                if not final_dict:
                    converted_interface = Common.convert_intf_name(interface)
                    final_dict = ret_dict.setdefault('qfp', {}).setdefault(
                        'active', {}).setdefault('interface', {}).setdefault(converted_interface, {})

                group = m.groupdict()
                status = group['transmit_receive']
                if 'Receive' in status:
                    current_stats = 'receive_stats'
                elif 'Transmit' in status:
                    current_stats = 'transmit_stats'
                elif 'Input Drop' in status:
                    current_stats = 'ingress_drop_stats'
                else:
                    current_stats = 'egress_drop_stats'

                final_dict.setdefault(current_stats, {})
                continue

            m = p3.match(line)
            if m:
                group = m.groupdict()
                stats = group['stats']
                final_dict[current_stats].setdefault(stats, {})
                final_dict[current_stats][stats]['packets'] = int(group['packets'])
                final_dict[current_stats][stats]['octets'] = int(group['octets'])
                continue

        return ret_dict


class ShowPlatformHardwareQfpStatisticsDropSchema(MetaParser):
    """Schema for show platform hardware qfp active statistics drop
                  show platform hardware qfp standby statistics drop"""

    schema = {
        'global_drop_stats': {
            Any(): {
                'packets': int,
                'octets': int,
            },
        }
    }


class ShowPlatformHardwareQfpStatisticsDrop(ShowPlatformHardwareQfpStatisticsDropSchema):
    """Parser for show platform hardware qfp active statistics drop
                  show platform hardware qfp standby statistics drop"""

    cli_command = 'show platform hardware qfp {status} statistics drop | exclude _0_'

    def cli(self, status='active', output=None):

        if output is None:
            cmd = self.cli_command.format(status=status)
            out = self.device.execute(cmd)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # Global Drop Stats                         Packets                  Octets
        # -------------------------------------------------------------------------
        # Ipv4NoAdj                                       7                     296
        # Ipv4NoRoute                                   181                    7964
        p1 = re.compile(r'^(?P<global_drop_stats>\w+) +(?P<packets>\d+) +(?P<octets>\d+)$')

        for line in out.splitlines():
            line = line.strip()
            m = p1.match(line)
            if m:
                group = m.groupdict()
                global_drop_stats = group.pop('global_drop_stats')
                stats_dict = ret_dict.setdefault('global_drop_stats', {}).setdefault(global_drop_stats, {})
                stats_dict.update({k: int(v) for k, v in group.items()})
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
        'processor_pool': {
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
        'show processes memory | include {include}'
    ]

    def cli(self, include=None, output=None):

        ret_dict = {}
        pid_index = {}

        if not output:
            if include:
                cmd = self.cli_command[1].format(include=include)
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


class ShowPlatformSoftwareMemoryCallsiteSchema(MetaParser):
    """ Schema for show platform software memory <process> switch active <R0> alloc callsite brief """
    schema = {
        'tracekey': str,
        'callsites': {
            Any(): {
                'thread': int,
                'diff_byte': int,
                'diff_call': int
            }
        }
    }


class ShowPlatformSoftwareMemoryCallsite(ShowPlatformSoftwareMemoryCallsiteSchema):
    """ Parser for show platform software memory <process> switch active <R0> alloc callsite brief """

    cli_command = 'show platform software memory {process} switch active {slot} alloc callsite brief'

    def cli(self, process, slot, output=None):

        if output is None:
            out = self.device.execute(self.cli_command.format(process=process, slot=slot))
        else:
            out = output

        # Init vars
        parsed_dict = {}
        if out:
            callsite_dict = parsed_dict.setdefault('callsites', {})

        # The current tracekey is   : 1#2315ece11e07bc883d89421df58e37b6
        p1 = re.compile(r'The +current +tracekey +is\s*: +(?P<tracekey>[#\d\w]*)')

        # callsite      thread    diff_byte               diff_call
        # ----------------------------------------------------------
        # 1617611779    31884     57424                   2
        p2 = re.compile(r'(?P<callsite>(\d+))\s+(?P<thread>(\d+))\s+(?P<diffbyte>(\d+))\s+(?P<diffcall>(\d+))')

        for line in out.splitlines():
            line = line.strip()

            # The current tracekey is   : 1#2315ece11e07bc883d89421df58e37b6
            m = p1.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['tracekey'] = str(group['tracekey'])
                continue

            # callsite      thread    diff_byte               diff_call
            # ----------------------------------------------------------
            # 1617611779    31884     57424                   2
            m = p2.match(line)
            if m:
                group = m.groupdict()
                callsite = group['callsite']
                one_callsite_dict = callsite_dict.setdefault(callsite, {})
                one_callsite_dict['thread'] = int(group['thread'])
                one_callsite_dict['diff_byte'] = int(group['diffbyte'])
                one_callsite_dict['diff_call'] = int(group['diffcall'])
                continue

        return parsed_dict


class ShowPlatformSoftwareMemoryBacktraceSchema(MetaParser):
    """ Schema for show platform software memory <process> switch active <R0> alloc backtrace """
    schema = {
        'backtraces': {
            Any():
                {'allocs': int,
                 'frees': int,
                 'call_diff': int,
                 'callsite': str,
                 'thread_id': int}
        }

    }

class ShowPlatformSoftwareMemoryBacktrace(ShowPlatformSoftwareMemoryBacktraceSchema):
    """ Parser for show platform software memory <process> switch active <R0> alloc backtrace """

    cli_command = 'show platform software memory {process} switch active {slot} alloc backtrace'

    def cli(self, process, slot, output=None):
        if output is None:
            out = self.device.execute(
                self.cli_command.format(process=process, slot=slot))
        else:
            out = output

        # Init vars
        parsed_dict = {}
        if out:
            backtraces_dict = parsed_dict.setdefault('backtraces', {})

        # backtrace: 1#2315ece11e07bc883d89421df58e37b6   maroon:7F740DEDC000+61F6 tdllib:7F7474D05000+B2B46 ui:7F74770E4000+4639A ui:7F74770E4000+4718C cdlcore:7F7466A6B000+37C95 cdlcore:7F7466A6B000+37957 uipeer:7F747A7A8000+24F2A evutil:7F747864E000+7966 evutil:7F747864E000+7745
        p1 = re.compile(r'backtrace: (?P<backtrace>[\w#\d\s:+]+)$')

        #   callsite: 2150603778, thread_id: 31884
        p2 = re.compile(r'callsite: +(?P<callsite>\d+), +thread_id: +(?P<thread_id>\d+)')

        #   allocs: 1, frees: 0, call_diff: 1
        p3 = re.compile(r'allocs: +(?P<allocs>(\d+)), +frees: +(?P<frees>(\d+)), +call_diff: +(?P<call_diff>(\d+))')

        for line in out.splitlines():
            line = line.strip()

            # backtrace: 1#2315ece11e07bc883d89421df58e37b6   maroon:7F740DEDC000+61F6 tdllib:7F7474D05000+B2B46 ui:7F74770E4000+4639A ui:7F74770E4000+4718C cdlcore:7F7466A6B000+37C95 cdlcore:7F7466A6B000+37957 uipeer:7F747A7A8000+24F2A evutil:7F747864E000+7966 evutil:7F747864E000+7745
            m = p1.match(line)
            if m:
                group = m.groupdict()
                backtrace = str(group['backtrace'])
                one_backtrace_dict = backtraces_dict.setdefault(backtrace, {})
                continue

            #   callsite: 2150603778, thread_id: 31884
            m = p2.match(line)
            if m:
                group = m.groupdict()
                one_backtrace_dict['callsite'] = group['callsite']
                one_backtrace_dict['thread_id'] = int(group['thread_id'])
                continue

            #   allocs: 1, frees: 0, call_diff: 1
            m = p3.match(line)
            if m:
                group = m.groupdict()
                one_backtrace_dict['allocs'] = int(group['allocs'])
                one_backtrace_dict['frees'] = int(group['frees'])
                one_backtrace_dict['call_diff'] = int(group['call_diff'])
                continue

        return parsed_dict

# class RmSoftwareMemoryChassisActiveBacktrace(ShowPlatformSoftwareMemoryBacktrace):
#     """ Parser for rm platform software memory <process> chassis active <R0> alloc backtrace """

#     cli_command = 'rm software memory {process} chassis active {slot} alloc backtrace'

#     def cli(self, process, slot, output=None):
#         if output is None:
#             out = self.device.execute(
#                 self.cli_command.format(process=process, slot=slot))
#         else:
#             out = output

#         return super().cli(process=process, slot=slot, output=out)

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


# =======================================================================
# Parser for 'show platform hardware qfp active feature appqoe stats all,
# show platform hardware qfp active feature appqoe stats service-node status up'
# =======================================================================
class ShowPlatformHardwareQfpActiveFeatureAppqoeSchema(MetaParser):
    schema = {
        'feature': {
            Any(): {
                'global': {
                    'ip_non_tcp_pkts': int,
                    'not_enabled': int,
                    'cft_handle_pkt': int,
                    'sdvt_divert_req_fail': int,
                    Optional('syn_policer_rate'): int,
                    Optional('sn_data_pkts_processed'): int,
                    Optional('appqoe_srv_chain_non_tcp_bypass'): int,
                    Optional('appqoe_srv_chain_frag_bypass'): int,
                    Optional('appqoe_cvla_alloc_failure'): int,
                    Optional('appqoe_srv_chain_sn_unhealthy_bypass'): int,
                    Optional('appqoe_srv_chain_tcp_mid_flow_bypass'): int,
                    Optional('appqoe_lb_without_dre') : int,
                    Optional('appqoe_alloc_empty_ht_entry'): int,
                    Optional('appqoe_bulk_upd_mem_bm_no_sng'): int,
                    Optional('appqoe_srv_chain_transit_dre_bypass'): int,
                    Optional('appqoe_sn_data_pkts_processed'): int,
                    Optional('appqoe_svc_on_appqoe_vpn_drop') : int,
                    'sdvt_global_stats': {
                        Optional('appnav_registration'): int,
                        Optional('control_decaps_could_not_find_flow_from_tuple'): int,
                        Optional('control_decaps_couldnt_find_sdvt_cft_fo'): int,
                        Optional('sdvt_decaps_couldnt_find_cft_instance_handle'): int,
                        Optional('exceeded_sdvt_syn_policer_limit'): int,
                        Optional('within_sdvt_syn_policer_limit'): int
                    }
                },
                Optional('sng'):{
                    Any():{
                        'sn_index': {
                            Any(): {
                                Optional('ip'): str,
                                Optional('oce_id'): int,
                                Optional('del'): int,
                                Optional('key'): str,
                                Optional('id'): int,
                                Optional('ver'): int,
                                Optional('status'): int,
                                Optional('type'): int,
                                Optional('sng'): int,
                                Optional('appnav_stats'): {
                                    Optional('to_sn'): {
                                        'packets': int,
                                        'bytes': int
                                    },
                                    Optional('from_sn'): {
                                        'packets': int,
                                        'bytes': int
                                    }
                                },
                                'sdvt_count_stats': {
                                    Optional('active_connections'): int,
                                    Optional('decaps'): int,
                                    Optional('encaps'): int,
                                    Optional('packets_unmarked_in_ingress'): int,
                                    Optional('expired_connections'): int,
                                    Optional('idle_timed_out_persistent_connections'): int,
                                    Optional('decap_messages'): {
                                        'processed_control_messages': int,
                                        'delete_requests_recieved': int,
                                        'deleted_protocol_decision': int,
                                        Optional('connections_passed_through_as_intermediate_node'): int,
                                        Optional('connections_dreopt_service_is_cleared'): int
                                    }
                                },
                                'sdvt_packet_stats': {
                                    Optional('divert'): {
                                        'packets': int,
                                        'bytes': int
                                    },
                                    Optional('reinject'): {
                                        'packets': int,
                                        'bytes': int
                                    }
                                },
                                Optional('sdvt_drop_cause_stats'): dict, # This is here because not enough info in output shared
                                Optional('sdvt_errors_stats'): dict, # This is here because not enough info in output shared
                            }
                        }
                    }
                },
                'sn_index': {
                    Any(): {
                        Optional('ip'): str,
                        Optional('oce_id'): int,
                        Optional('del'): int,
                        Optional('key'): str,
                        Optional('id'): int,
                        Optional('ver'): int,
                        Optional('status'): int,
                        Optional('type'): int,
                        Optional('sng'): int,
                        Optional('appnav_stats'): {
                            Optional('to_sn'): {
                                'packets': int,
                                'bytes': int
                            },
                            Optional('from_sn'): {
                                'packets': int,
                                'bytes': int
                            }
                        },
                        'sdvt_count_stats': {
                            Optional('active_connections'): int,
                            Optional('decaps'): int,
                            Optional('encaps'): int,
                            Optional('packets_unmarked_in_ingress'): int,
                            Optional('expired_connections'): int,
                            Optional('idle_timed_out_persistent_connections'): int,
                            Optional('non_syn_divert_requests') : int,
                            Optional('decap_messages'): {
                                'processed_control_messages': int,
                                'delete_requests_recieved': int,
                                'deleted_protocol_decision': int,
                                Optional('connections_passed_through_as_intermediate_node'): int,
                                Optional('connections_dreopt_service_is_cleared'): int
                            }
                        },
                        'sdvt_packet_stats': {
                            Optional('divert'): {
                                'packets': int,
                                'bytes': int
                            },
                            Optional('reinject'): {
                                'packets': int,
                                'bytes': int
                            }
                        },
                        Optional('sdvt_drop_cause_stats'): dict, # This is here because not enough info in output shared
                        Optional('sdvt_errors_stats'): dict, # This is here because not enough info in output shared
                    }
                }
            }
        }
    }

class ShowPlatformHardwareQfpActiveFeatureAppqoe(ShowPlatformHardwareQfpActiveFeatureAppqoeSchema):

    cli_command = ['show platform hardware qfp active feature appqoe stats', 'show platform hardware qfp active feature appqoe stats sng {sng} all']

    def cli(self, sng='', output=None):

        # if the user does not provide output to the parser
        # we need to get it from the device
        if not output:
            if sng:
                output = self.device.execute(self.cli_command[1].format(sng=sng))
            else:
                output = self.device.execute(self.cli_command[0])

        # APPQOE Feature Statistics:
        p1 = re.compile(r'^(?P<feature>\w+) +Feature +Statistics:$')

        # Global:
        p2 = re.compile(r'^Global:$')

        # SDVT Global stats:
        p3 = re.compile(r'^SDVT +Global +stats:$')

        # SN Index [0 (Green)]
        # SN Index [Default]
        p4 = re.compile(r'^SN +Index +\[(?P<index>[\s\S]+)\]$')

        # SNG: 3
        p4_1 = re.compile(r'^SNG: +(?P<sng_index>[\d]+)')

        # SDVT Count stats:
        # SDVT Packet stats:
        # SDVT Drop Cause stats:
        # SDVT Errors stats:
        p5 = re.compile(r'^(?P<sdvt_stats_type>SDVT +[\s\S]+ +stats):$')

        # decaps: Processed control messages from SN: 14200
        # decaps: delete requests received total: 14200
        # decaps: delete - protocol decision: 14200
        p6 = re.compile(r'^decaps: +(?P<decap_type>[\s\S]+): +(?P<value>\d+)$')

        # Divert packets/bytes: 743013/43313261
        # Reinject packets/bytes: 679010/503129551
        p7 = re.compile(r'^(?P<type>Divert|Reinject) +packets\/bytes: +(?P<packets>\d+)\/(?P<bytes>\d+)$')

        # ip-non-tcp-pkts: 0
        # not-enabled: 0
        # cft_handle_pkt:  0
        # sdvt_divert_req_fail:  0
        # syn_policer_rate: 800
        p8 = re.compile(r'^(?P<key>[\s\S]+): +(?P<value>\d+)$')

        # SN Index [0 (Green)], IP: 10.136.1.250, oce_id: 1243618816
        p9 = re.compile(r'^SN +Index +\[(?P<index>[\s\S]+)\], +IP: +(?P<ip>[\s\S]+), +oce_id: +(?P<oce_id>[\s\S]+)$')

        # SNG: 3 SN Index [0 (Green)], IP: 10.136.1.250, oce_id: 1243618816
        p9_1 = re.compile(r'^SNG: +(?P<sng_index>[\d]+) +SN +Index +\[(?P<index>[\s\S]+)\], +IP: +(?P<ip>[\s\S]+), +oce_id: +(?P<oce_id>[\s\S]+)$')

        # del 0, key 0x0301, id 1, ver 1, status 1, type 3, sng 0
        p10 = re.compile(r'^del +(?P<del>[\s\S]+), key +(?P<key>[\s\S]+), id +(?P<id>[\s\S]+), ver +(?P<ver>[\s\S]+), status +(?P<status>[\s\S]+), type +(?P<type>[\s\S]+), sng +(?P<sng>[\s\S]+)$')

        # APPNAV STATS: toSN 2662751642/2206742552009, fromSN 2715505607/2260448392656
        p11 = re.compile(r'^APPNAV STATS: +(?P<to_sn>[\S]+) +(?P<tosn_packets>[\d]+)\/(?P<tosn_bytes>\d+), +(?P<from_sn>[\S]+) +(?P<frmsn_packets>[\d]+)\/(?P<frmsn_bytes>\d+)$')

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # APPQOE Feature Statistics:
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                feature_name = groups['feature'].lower()
                feature_dict = ret_dict.setdefault('feature', {}).setdefault(feature_name, {})

                last_dict_ptr = feature_dict
                continue

            # Global:
            m = p2.match(line)
            if m:
                global_dict = feature_dict.setdefault('global', {})

                last_dict_ptr = global_dict
                continue

            # SDVT Global stats:
            m = p3.match(line)
            if m:
                sdvt_global_dict = global_dict.setdefault('sdvt_global_stats', {})

                last_dict_ptr = sdvt_global_dict
                continue

            # SN Index [0 (Green)]
            # SN Index [Default]
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                index_dict = feature_dict.setdefault('sn_index', {}).setdefault(groups['index'], {})

                last_dict_ptr = index_dict
                continue

            # SN Index [0 (Green)], IP: 10.136.1.250, oce_id: 1243618816
            m = p9.match(line)
            if m:
                groups = m.groupdict()
                index_dict = feature_dict.setdefault('sn_index', {}).setdefault(groups['index'], {})
                index_dict.update({'ip': groups['ip']})
                index_dict.update({'oce_id': int(groups['oce_id'])})
                last_dict_ptr = index_dict
                continue

            # SNG: 3 SN Index [0 (Green)], IP: 10.136.1.250, oce_id: 1243618816
            m = p9_1.match(line)
            if m:
                groups = m.groupdict()
                index_dict = feature_dict.setdefault('sng', {}).setdefault(groups['sng_index'], {}).setdefault('sn_index', {}).setdefault(groups['index'], {})
                index_dict.update({'ip': groups['ip']})
                index_dict.update({'oce_id': int(groups['oce_id'])})
                last_dict_ptr = index_dict
                continue

            # del 0, key 0x0301, id 1, ver 1, status 1, type 3, sng 0
            m = p10.match(line)
            if m:
                groups = m.groupdict()
                index_dict.update({'del': int(groups['del'])})
                index_dict.update({'key': groups['key']})
                index_dict.update({'id': int(groups['id'])})
                index_dict.update({'ver': int(groups['ver'])})
                index_dict.update({'status': int(groups['status'])})
                index_dict.update({'type': int(groups['type'])})
                index_dict.update({'sng': int(groups['sng'])})

                last_dict_ptr = index_dict
                continue

            # APPNAV STATS: toSN 2662751642/2206742552009, fromSN 2715505607/2260448392656
            m = p11.match(line)
            if m:
                groups = m.groupdict()
                appnav_stats_dict = index_dict.setdefault('appnav_stats', {})
                to_sn_dict = appnav_stats_dict.setdefault('to_sn', {})
                to_sn_dict.update({
                    'packets': int(groups['tosn_packets']),
                    'bytes': int(groups['tosn_bytes'])
                    })
                from_sn_dict = appnav_stats_dict.setdefault('from_sn', {})
                from_sn_dict.update({
                    'packets': int(groups['frmsn_packets']),
                    'bytes': int(groups['frmsn_bytes'])
                    })

                last_dict_ptr = index_dict
                continue

            # SDVT Count stats
            # SDVT Packet stats
            # SDVT Drop Cause stats
            # SDVT Errors stats
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                sdvt_stats_type = groups['sdvt_stats_type'].replace(' ', '_').lower()
                sdvt_stats_type_dict = index_dict.setdefault(sdvt_stats_type, {})

                last_dict_ptr = sdvt_stats_type_dict
                continue

            # decaps: Processed control messages from SN: 14200
            # decaps: delete requests received total: 14200
            # decaps: delete - protocol decision: 14200
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                decap_messages_dict = sdvt_stats_type_dict.setdefault('decap_messages', {})

                if 'control messages' in groups['decap_type']:
                    decap_messages_dict.update({'processed_control_messages': int(groups['value'])})

                elif 'delete requests' in groups['decap_type']:
                    decap_messages_dict.update({'delete_requests_recieved': int(groups['value'])})

                elif 'protocol decision' in groups['decap_type']:
                    decap_messages_dict.update({'deleted_protocol_decision': int(groups['value'])})

                last_dict_ptr = decap_messages_dict
                continue

            # Divert packets/bytes: 743013/43313261
            # Reinject packets/bytes: 679010/503129551
            m = p7.match(line)
            if m:
                groups = m.groupdict()

                if 'Divert' in groups['type']:
                    divert_reinject_dict = sdvt_stats_type_dict.setdefault('divert', {})
                elif 'Reinject' in groups['type']:
                    divert_reinject_dict = sdvt_stats_type_dict.setdefault('reinject', {})

                divert_reinject_dict.update({
                    'packets': int(groups['packets']),
                    'bytes': int(groups['bytes'])
                })

                last_dict_ptr = divert_reinject_dict
                continue

            # ip-non-tcp-pkts: 0
            # not-enabled: 0
            # cft_handle_pkt:  0
            # sdvt_divert_req_fail:  0
            # syn_policer_rate: 800
            m = p8.match(line)
            if m:
                groups = m.groupdict()
                key = groups['key'].replace('-', '_').replace(' ', '_').replace(':', '').lower()
                last_dict_ptr.update({key: int(groups['value'])})
                continue

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

    cli_command = 'show platform hardware fed switch active fwd-asic resource tcam utilization'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

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


        for line in out.splitlines():
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

class ShowPlatformHardwareQfpActiveDatapathUtilSumSchema(MetaParser):

    schema = {
        'cpp': {
            Any(): {
                Any(): {
                    'pps': {
                        '5_secs': int,
                        '1_min': int,
                        '5_min': int,
                        '60_min': int
                    },
                    'bps': {
                        '5_secs': int,
                        '1_min': int,
                        '5_min': int,
                        '60_min': int
                    }
                },
                'processing': {
                    'load_pct': {
                    	'5_secs': int,
                    	'1_min': int,
                    	'5_min': int,
                    	'60_min': int
                    }
                },
                Optional('crypto_io'): {
                    'crypto_load_pct': {
                    	'5_secs': int,
                    	'1_min': int,
                    	'5_min': int,
                    	'60_min': int
                    },
                    'rx_load_pct': {
                    	'5_secs': int,
                    	'1_min': int,
                    	'5_min': int,
                    	'60_min': int
                    },
                    'tx_load_pct': {
                    	'5_secs': int,
                    	'1_min': int,
                    	'5_min': int,
                    	'60_min': int
                    },
                    'idle_pct': {
                    	'5_secs': int,
                    	'1_min': int,
                    	'5_min': int,
                    	'60_min': int
                    }
                }
            }
        }
    }


class ShowPlatformHardwareQfpActiveDatapathUtilSum(ShowPlatformHardwareQfpActiveDatapathUtilSumSchema):

    cli_command = ['show platform hardware qfp active datapath utilization summary']

    def cli(self, output=None):

        # if the user does not provide output to the parser
        # we need to get it from the device
        if not output:
            output = self.device.execute(self.cli_command[0])

        #CPP 0:                     5 secs        1 min        5 min       60 min
        p1 = re.compile(r'^CPP (?P<cpp_num>\d)\: +(\d\s\S+) +(\d\s\S+) +(\d\s\S+) +(\d+\s\S+)$')
        #Crypto/IO
        p2 = re.compile(r'^Crypto/IO$')
        #Input:     Total (pps)            2            2            1            0
        p3 = re.compile(r'^(?P<dir>\w+)\: +\S+ \((?P<type>\S+)\) +(?P<value_5s>\d+) +(?P<value_1m>\d+) +(?P<value_5m>\d+) +(?P<value_60m>\d+)$')
        #(bps)         2928         1856         1056           88
        #Idle (pct)           43           35           35           75
        p4 = re.compile(r'^(Idle )?\((?P<type>bps|pct)\) +(?P<value_5s>\d+) +(?P<value_1m>\d+) +(?P<value_5m>\d+) +(?P<value_60m>\d+)$')

        ret_dict = {}
        for line in output.splitlines():
            line = line.strip()
            #   CPP 0:                     5 secs        1 min        5 min       60 min
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                cpp_number = groups['cpp_num'].lower()
                feature_dict = ret_dict.setdefault('cpp', {}).setdefault(cpp_number, {})
                last_dict_ptr = feature_dict
                continue

            #Crypto/IO
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                feature_dict = feature_dict.setdefault('crypto_io', {})
                last_dict_ptr = feature_dict
                continue

            #Input:     Total (pps)            2            2            1            0
            #Processing: Load (pct)            0            0            0            0
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                if groups['dir'].strip() in ['Crypto','RX','TX','Idle']:
                    key = "{a}_load_{b}".format(a=groups['dir'].strip().lower(), b=groups['type'].strip().lower())
                    dir_dict = feature_dict.setdefault(key, {})
                    dir_dict.update({'5_secs': int(groups['value_5s'])})
                    dir_dict.update({'1_min': int(groups['value_1m'])})
                    dir_dict.update({'5_min': int(groups['value_5m'])})
                    dir_dict.update({'60_min': int(groups['value_60m'])})
                    last_dict_ptr = dir_dict
                    continue
                else:
                    dir_dict = feature_dict.setdefault(groups['dir'].lower(), {})
                    if 'pct' in groups['type']:
                        key = 'load_' + groups['type']
                    else:
                        key = groups['type']
                    type_dict = dir_dict.setdefault(key, {})
                    type_dict.update({'5_secs': int(groups['value_5s'])})
                    type_dict.update({'1_min': int(groups['value_1m'])})
                    type_dict.update({'5_min': int(groups['value_5m'])})
                    type_dict.update({'60_min': int(groups['value_60m'])})
                    last_dict_ptr = type_dict
                    continue

            #(bps)         2928         1856         1056           88
            #Idle (pct)           43           35           35           75
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                if 'pct' in groups['type']:
                    key = "idle_{t}".format(t=groups['type'])
                    type_dict = feature_dict.setdefault(key, {})
                    type_dict.update({'5_secs': int(groups['value_5s'])})
                    type_dict.update({'1_min': int(groups['value_1m'])})
                    type_dict.update({'5_min': int(groups['value_5m'])})
                    type_dict.update({'60_min': int(groups['value_60m'])})
                    last_dict_ptr = type_dict
                else:
                    type_dict = dir_dict.setdefault(groups['type'], {})
                    type_dict.update({'5_secs': int(groups['value_5s'])})
                    type_dict.update({'1_min': int(groups['value_1m'])})
                    type_dict.update({'5_min': int(groups['value_5m'])})
                    type_dict.update({'60_min': int(groups['value_60m'])})
                    last_dict_ptr = type_dict
                    continue

        return ret_dict

# =======================================================================
# Schema for 'show platform hardware qfp active tcam resource-manager usage'
# =======================================================================
class ShowPlatformHardwareQfpActiveTcamResourceManagerUsageSchema(MetaParser):
     schema = {
                'qfp_tcam_usage_information': {
                    Any(): {
                        'name': str,
                        'number_of_cells_per_entry': int,
                        Optional('current_80_bit_entries_used'): int,
                        Optional('current_160_bits_entries_used'): int,
                        Optional('current_320_bits_entries_used'): int,
                        'current_used_cell_entries': int,
                        'current_free_cell_entries': int
                        },
                    'total_tcam_cell_usage_information': {
                        'name': str,
                        'total_number_of_regions': int,
                        'total_tcam_used_cell_entries': int,
                        'total_tcam_free_cell_entries': int,
                        'threshold_status': str
                        }
                    }
                }

# =======================================================================
# Parser for 'show platform hardware qfp active tcam resource-manager usage'
# =======================================================================
class ShowPlatformHardwareQfpActiveTcamResourceManagerUsage(ShowPlatformHardwareQfpActiveTcamResourceManagerUsageSchema):

    cli_command = ['show platform hardware qfp active tcam resource-manager usage']


    def cli(self, output=None):

        # if the user does not provide output to the parser
        # we need to get it from the device
        if not output:
            output = self.device.execute(self.cli_command[0])

        #QFP TCAM Usage Information
        p1 = re.compile(r'^(?P<key>QFP TCAM Usage Information)$')

        #80 Bit Region Information
        #Total TCAM Cell Usage Information
        p2 = re.compile(r'^(?P<num>\d+|Total TCAM)(?P<region>[\s\S]+)$')

        # Name                                : Leaf Region #1
        # Number of cells per entry           : 2
        # Current 160 bits entries used       : 19
        # Current used cell entries           : 38
        # Current free cell entries           : 4058
        p3 = re.compile(r'^(?P<key>[\s\S]+)\:(?P<value>[\s\S]+\S)$')


        ret_dict = {}
        for line in output.splitlines():
            line = line.strip()

            #QFP TCAM Usage Information
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                key1 = groups['key'].replace(' ','_').lower()
                feature_dict = ret_dict.setdefault(key1, {})
                continue

            #80 Bit Region Information
            #Total TCAM Cell Usage Information
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                reg = groups['region'].strip().replace(' ','_').lower()
                reg_name = groups['num'].replace(' ','_').lower() +'_'+reg
                region_hash = feature_dict.setdefault(reg_name, {})
                continue

            # Name                                : Leaf Region #1
            # Number of cells per entry           : 2
            # Current 160 bits entries used       : 19
            # Current used cell entries           : 38
            # Current free cell entries           : 4058
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                name = groups['key'].strip().replace(' ','_').lower()
                val = groups['value'].strip()
                if name not in ['threshold_status', 'name']:
                    val = int(groups['value'])

                region_hash.update({name : val})
                continue


        return ret_dict

# =======================================================================
# Schema for 'show platform resources'
# =======================================================================
class ShowPlatformResourcesSchema(MetaParser):
    schema = {
        'rp': {
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
                    'tcam': {
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
                    Optional('pkt_buf_mem_0'): {
                        'usage_kb': int,
                        'usage_perc': int,
                        'max_kb': int,
                        'warning_perc': int,
                        'critical_perc': int,
                        'state': str
                    },
                    Optional('pkt_buf_mem_1'): {
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


class ShowPlatformSoftwareYangManagementProcessSchema(MetaParser):
    '''schema for
        * show platform software yang-management process
    '''

    schema = {
        str: str
    }

class ShowPlatformSoftwareYangManagementProcess(ShowPlatformSoftwareYangManagementProcessSchema):
    '''parser for
        * show platform software yang-management process
    '''

    cli_command = "show platform software yang-management process"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # confd            : Running
        # pubd             : Running
        # gnmib            : Not Running
        p1 = re.compile(r'^(?P<key>\S+) *: +(?P<data>(Running|Not +Running))$')

        ret_dict = dict()

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({
                    group['key']: group['data']
                })
                continue

        return ret_dict


class ShowPlatformSoftwareYangManagementProcessMonitorSchema(MetaParser):
    '''schema for
        * show platform software yang-management process monitor
    '''

    schema = {
        'pid': {
            int: {
                'command': str,
                'state': str,
                'vsz': int,
                'rss': int,
                'cpu': float,
                'mem': float,
                'elapsed': str,
            }
        }
    }

class ShowPlatformSoftwareYangManagementProcessMonitor(ShowPlatformSoftwareYangManagementProcessMonitorSchema):
    '''parser for
        * show platform software yang-management process monitor
    '''

    cli_command = "show platform software yang-management process monitor"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # dmiauthd          551 S 376940 49600  0.0  0.6    21:44:33
        # ncsshd           1503 S 301344 17592  0.0  0.2    21:44:32
        p1 = re.compile(r'^(?P<command>\S+) +(?P<pid>\d+) +(?P<s>\S+) +(?P<vsz>\d+) +'
                        r'(?P<rss>\d+) +(?P<cpu>\S+) +(?P<mem>\S+) +(?P<elapsed>\S+)$')

        ret_dict = dict()

        for line in out.splitlines():
            line = line.strip()

            # dmiauthd          551 S 376940 49600  0.0  0.6    21:44:33
            # ncsshd           1503 S 301344 17592  0.0  0.2    21:44:32
            m = p1.match(line)
            if m:
                group = m.groupdict()
                commands = ret_dict.setdefault('pid', {})
                command = commands.setdefault(int(group['pid']), {})
                command.update({
                    'command': group['command'],
                    'state': group['s'],
                    'vsz': int(group['vsz']),
                    'rss': int(group['rss']),
                    'cpu': float(group['cpu']),
                    'mem': float(group['mem']),
                    'elapsed': group['elapsed'],
                })
                continue

        return ret_dict


class ShowPlatformSoftwareYangManagementProcessStateSchema(MetaParser):
    '''schema for
        * show platform software yang-management process state
    '''

    schema = {
        'confd-status': str,
        'processes': {
            str: {
                'status': str,
                'state': str,
                },
            }
        }

class ShowPlatformSoftwareYangManagementProcessState(ShowPlatformSoftwareYangManagementProcessStateSchema):
    '''parser for
        * show platform software yang-management process state
    '''

    cli_command = "show platform software yang-management process state"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Confd Status: Started
        # Confd Status: Not Running
        p1 = re.compile(r'^Confd +Status: +(?P<status>.+)$')

        # pubd                 Running             Active
        # gnmib                Not Running         Not Applicable
        # ndbmand              Not Running         Down
        # pubd                 Running             Reset
        p2 = re.compile(r'^(?P<process>\S+) +(?P<status>(Running|Not +Running)) +'
                        r'(?P<state>(Active|Not +Active|Not +Applicable|Down|Reset))$')

        ret_dict = dict()

        for line in out.splitlines():
            line = line.strip()

            # Confd Status: Started
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['confd-status'] = group['status']
                continue

            # pubd                 Running             Active
            # gnmib                Not Running         Not Applicable
            # ndbmand              Not Running         Down
            m = p2.match(line)
            if m:
                group = m.groupdict()
                commands = ret_dict.setdefault('processes', {})
                command = commands.setdefault(group['process'], {})
                command.update({
                    'status': group['status'],
                    'state': group['state'],
                })
                continue

        return ret_dict

class ShowPlatformSoftwareMemoryRpActiveSchema(MetaParser):
    """ Schema for
        * show platform software memory mdt-pubd RP active
    """
    schema = {
        'module': {
            Any(): {
                'allocated': int,
                'requested': int,
                'overhead': int,
                Optional('allocations'): int,
                Optional('failed'): int,
                Optional('frees'): int,
            }
        }
    }

class ShowPlatformSoftwareMemoryRpActive(ShowPlatformSoftwareMemoryRpActiveSchema):
    """ Parser for
        * show platform software memory mdt-pubd RP active
    """

    cli_command = 'show platform software memory {process} RP active'

    def cli(self, process, output=None):

        if output is None:
            out = self.device.execute(self.cli_command.format(process=process))
        else:
            out = output

        ret_dict = {}

        # Module: process
        p1 = re.compile(r'Module: +(?P<module>[\S\s]+)$')

        # allocated: 16695, requested: 16647, overhead: 48
        p2 = re.compile(r'allocated: +(?P<allocated>\d+), +requested: +'
            r'(?P<requested>\d+), +overhead: +(?P<overhead>\d+)$')

        # Allocations: 3, failed: 0, frees: 0
        p3 = re.compile(r'Allocations: +(?P<allocations>\d+), +failed: +'
            r'(?P<failed>\d+), +frees: +(?P<frees>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            # Module: process
            m = p1.match(line)
            if m:
                group = m.groupdict()
                module = group.get('module')
                module_dict = ret_dict.setdefault('module', {}). \
                    setdefault(module, {})
                continue

            # allocated: 16695, requested: 16647, overhead: 48
            m = p2.match(line)
            if m:
                group = m.groupdict()
                module_dict.update({k:int(v) for k, v in group.items() if v is not None})
                continue

            # Allocations: 3, failed: 0, frees: 0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                module_dict.update({k:int(v) for k, v in group.items() if v is not None})
                continue

        return ret_dict

class ShowPlatformSoftwareMemorySwitchActive(ShowPlatformSoftwareMemoryRpActive):
    """ Parser for
        * show platform software memory mdt-pubd switch active <R0>
    """

    cli_command = 'show platform software memory {process} switch active {slot}'

    def cli(self, process, slot, output=None):

        if output is None:
            out = self.device.execute(self.cli_command.format(
                process=process,
                slot=slot))
        else:
            out = output

        return super().cli(process=process, output=out)

class ShowPlatformSoftwareMemoryChassisActive(ShowPlatformSoftwareMemoryRpActive):
    """ Parser for
        * show platform software memory mdt-pubd chassis active <R0>
    """

    cli_command = 'show platform software memory {process} chassis active {slot}'

    def cli(self, process, slot, output=None):

        if output is None:
            out = self.device.execute(self.cli_command.format(
                process=process,
                slot=slot))
        else:
            out = output

        return super().cli(process=process, output=out)

class ShowPlatformSoftwareMemoryRpActiveBriefSchema(MetaParser):
    """ Schema for
        * show platform software memory mdt-pubd RP active brief
    """
    schema = {
        'module': {
            Any(): {
                'allocated': int,
                'requested': int,
                'allocs': int,
                'frees': int,
            }
        }
    }

class ShowPlatformSoftwareMemoryRpActiveBrief(ShowPlatformSoftwareMemoryRpActiveBriefSchema):
    """ Parser for
        * show platform software memory mdt-pubd RP active brief
    """

    cli_command = 'show platform software memory {process} RP active brief'

    def cli(self, process, output=None):

        if output is None:
            out = self.device.execute(self.cli_command.format(process=process))
        else:
            out = output

        ret_dict = {}

        # Summary                 420136        364136        3706          206
        p1 = re.compile(r'^(?P<module>\S+) +(?P<allocated>\d+) +'
            r'(?P<requested>\d+) +(?P<allocs>\d+) +(?P<frees>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            # Summary                 420136        364136        3706          206
            m = p1.match(line)
            if m:
                group = m.groupdict()
                module = group.pop('module')
                module_dict = ret_dict.setdefault('module', {}). \
                    setdefault(module, {})
                module_dict.update({k:int(v) for k, v in group.items() if v is not None})
                continue

        return ret_dict

class ShowPlatformSoftwareMemorySwitchActiveBrief(ShowPlatformSoftwareMemoryRpActiveBrief):
    """ Parser for
        * show platform software memory mdt-pubd switch active R0 brief
    """

    cli_command = 'show platform software memory {process} switch active {slot} brief'

    def cli(self, process, slot, output=None):

        if output is None:
            out = self.device.execute(self.cli_command.format(
                process=process,
                slot=slot))
        else:
            out = output

        return super().cli(process=process, output=out)

class ShowPlatformSoftwareMemoryChassisActiveBrief(ShowPlatformSoftwareMemoryRpActiveBrief):
    """ Parser for
        * show platform software memory mdt-pubd chassis active R0 brief
    """

    cli_command = 'show platform software memory {process} chassis active {slot} brief'

    def cli(self, process, slot, output=None):

        if output is None:
            out = self.device.execute(self.cli_command.format(
                process=process,
                slot=slot))
        else:
            out = output

        return super().cli(process=process, output=out)

class ShowPlatformSoftwareMemoryRpActiveAllocCallsiteSchema(MetaParser):
    """ Schema for
        * show platform software memory mdt-pubd RP active alloc callsite
    """
    schema = {
        'callsite': {
            Any(): {
                'thread_id': int,
                'allocs': int,
                'frees': int,
                'alloc_bytes': int,
                'free_bytes': int,
                'call_diff': int,
                'byte_diff': int
            }
        }
    }

class ShowPlatformSoftwareMemoryRpActiveAllocCallsite(ShowPlatformSoftwareMemoryRpActiveAllocCallsiteSchema):
    """ Parser for
        * show platform software memory mdt-pubd RP active alloc callsite
    """

    cli_command = 'show platform software memory {process} RP active alloc callsite'

    def cli(self, process, output=None):

        if output is None:
            out = self.device.execute(self.cli_command.format(process=process))
        else:
            out = output

        ret_dict = {}

        # callsite: 1355696130, thread_id: 24813
        p1 = re.compile(r'^callsite: +(?P<callsite>\d+), +thread_id: +(?P<thread_id>\d+)$')

        # allocs: 138151, frees: 138141, alloc_bytes: 15466123, free_bytes: 15464846, call_diff: 10, byte_diff: 1277
        p2 = re.compile(r'^allocs: +(?P<allocs>\d+), +frees: +(?P<frees>\d+), +'
            r'alloc_bytes: +(?P<alloc_bytes>\d+), +free_bytes: +(?P<free_bytes>\d+), +'
            r'call_diff: +(?P<call_diff>\d+), +byte_diff: +(?P<byte_diff>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            # callsite: 1355696130, thread_id: 24813
            m = p1.match(line)
            if m:
                group = m.groupdict()
                callsite = group.get('callsite')
                thread_id = group.get('thread_id')
                thread_dict = ret_dict.setdefault('callsite', {}). \
                    setdefault(callsite, {})
                thread_dict.update({'thread_id': int(thread_id)})
                continue

            # allocs: 138151, frees: 138141, alloc_bytes: 15466123, free_bytes: 15464846, call_diff: 10, byte_diff: 1277
            m = p2.match(line)
            if m:
                group = m.groupdict()
                thread_dict.update({k:int(v) for k, v in group.items() if v is not None})
                continue

        return ret_dict

class ShowPlatformSoftwareMemorySwitchActiveAllocCallsite(ShowPlatformSoftwareMemoryRpActiveAllocCallsite):
    """ Parser for
        * show platform software memory mdt-pubd switch active <R0> alloc callsite
    """

    cli_command = 'show platform software memory {process} switch active {slot} alloc callsite'

    def cli(self, process, slot, output=None):

        if output is None:
            out = self.device.execute(self.cli_command.format(
                process=process,
                slot=slot))
        else:
            out = output

        return super().cli(process=process, output=out)

class ShowPlatformSoftwareMemoryRpActiveAllocCallsiteBriefSchema(MetaParser):
    """ Schema for
        * show platform software memory mdt-pubd RP active alloc callsite
    """
    schema = {
        'tracekey': str,
        'callsite': {
            Any(): {
                'thread_id': int,
                'diff_byte': int,
                'diff_call': int,
            }
        }
    }

class ShowPlatformSoftwareMemoryRpActiveAllocCallsiteBrief(ShowPlatformSoftwareMemoryRpActiveAllocCallsiteBriefSchema):
    """ Parser for
        * show platform software memory mdt-pubd RP active alloc callsite brief
    """

    cli_command = 'show platform software memory {process} RP active alloc callsite brief'

    def cli(self, process, output=None):

        if output is None:
            out = self.device.execute(self.cli_command.format(process=process))
        else:
            out = output

        ret_dict = {}

        # callsite: 1355696130, thread_id: 24813
        p1 = re.compile(r'^The +current +tracekey +is +: +(?P<tracekey>\S+)$')

        # allocs: 138151, frees: 138141, alloc_bytes: 15466123, free_bytes: 15464846, call_diff: 10, byte_diff: 1277
        p2 = re.compile(r'^(?P<callsite>\d+) +(?P<thread_id>\d+) +(?P<diff_byte>\d+) +(?P<diff_call>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'tracekey': group['tracekey']})
                continue

            # callsite: 1355696130, thread_id: 24813
            m = p2.match(line)
            if m:
                group = m.groupdict()
                callsite = group.pop('callsite')
                thread_id = group.pop('thread_id')
                thread_dict = ret_dict.setdefault('callsite', {}). \
                    setdefault(callsite, {})
                thread_dict.update({'thread_id': int(thread_id)})
                thread_dict.update({k:int(v) for k, v in group.items() if v is not None})
                continue

        return ret_dict

class ShowPlatformSoftwareMemoryRpActiveAllocTypeSchema(MetaParser):
    """ Schema for
        * show platform software memory mdt-pubd RP active alloc type component
    """
    schema = {
        Optional('module'): {
            Any(): {
                'allocated': int,
                'requested': int,
                'overhead': int,
                'allocations': int,
                'null_allocations': int,
                'frees': int,
            }
        },
        Optional('type'): {
            Any(): {
                'allocated': int,
                'requested': int,
                'overhead': int,
                'allocations': int,
                'null_allocations': int,
                'frees': int,
            }
        },
    }

class ShowPlatformSoftwareMemoryRpActiveAllocType(ShowPlatformSoftwareMemoryRpActiveAllocTypeSchema):
    """ Parser for
        * show platform software memory mdt-pubd RP active alloc type component
        * show platform software memory mdt-pubd RP active alloc type data
    """

    cli_command = 'show platform software memory {process} RP active alloc type {alloc_type}'

    def cli(self, process, alloc_type, output=None):

        if output is None:
            out = self.device.execute(self.cli_command.format(
                process=process,
                alloc_type=alloc_type))
        else:
            out = output

        ret_dict = {}

        # Module: process
        p1 = re.compile(r'Module: +(?P<module>[\S\s]+)$')

        # Type: process
        p1_1 = re.compile(r'Type: +(?P<type>[\S\s]+)$')

        # allocated: 16695, requested: 16647, overhead: 48
        p2 = re.compile(r'Allocated: +(?P<allocated>\d+), +'
            r'Requested: +(?P<requested>\d+), +Overhead: +(?P<overhead>\d+)$')

        # Allocations: 3, failed: 0, frees: 0
        p3 = re.compile(r'Allocations: +(?P<allocations>\d+), +Null +Allocations: +'
            r'(?P<null_allocations>\d+), +Frees: +(?P<frees>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            # Module: process
            m = p1.match(line)
            if m:
                group = m.groupdict()
                module = group.get('module')
                module_dict = ret_dict.setdefault('module', {}). \
                    setdefault(module, {})
                continue

            # type: process
            m = p1_1.match(line)
            if m:
                group = m.groupdict()
                module = group.get('type')
                module_dict = ret_dict.setdefault('type', {}). \
                    setdefault(module, {})
                continue

            # allocated: 16695, requested: 16647, overhead: 48
            m = p2.match(line)
            if m:
                group = m.groupdict()
                module_dict.update({k:int(v) for k, v in group.items() if v is not None})
                continue

            # Allocations: 3, failed: 0, frees: 0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                module_dict.update({k:int(v) for k, v in group.items() if v is not None})
                continue

        return ret_dict

class ShowPlatformSoftwareMemorySwitchActiveAllocType(ShowPlatformSoftwareMemoryRpActiveAllocType):
    """ Parser for
        * show platform software memory mdt-pubd switch active <R0> alloc type component
    """

    cli_command = 'show platform software memory {process} switch active {slot} alloc type {alloc_type}'

    def cli(self, process, slot, alloc_type, output=None):

        if output is None:
            out = self.device.execute(self.cli_command.format(
                process=process,
                slot=slot,
                alloc_type=alloc_type))
        else:
            out = output

        return super().cli(process=process, output=out, alloc_type=alloc_type)

class ShowPlatformSoftwareMemoryRpActiveAllocTypeBriefSchema(MetaParser):
    """ Schema for
        * show platform software memory mdt-pubd RP active alloc type component brief
    """
    schema = {
        'type': {
            Any(): {
                'allocated': int,
                'requested': int,
                'allocations': int,
                'frees': int,
            }
        }
    }

class ShowPlatformSoftwareMemoryRpActiveAllocTypeBrief(ShowPlatformSoftwareMemoryRpActiveAllocTypeBriefSchema):
    """ Parser for
        * show platform software memory mdt-pubd RP active alloc type component brief
    """

    cli_command = 'show platform software memory {process} RP active alloc type {alloc_type} brief'

    def cli(self, process, alloc_type, output=None):

        if output is None:
            out = self.device.execute(self.cli_command.format(
                process=process,
                alloc_type=alloc_type))
        else:
            out = output

        ret_dict = {}

        # Summary                 4989412       4501988       150851        142147
        p1 = re.compile(r'(?P<type>\S+) +(?P<allocated>\d+) +'
            r'(?P<requested>\d+) +(?P<allocations>\d+) +(?P<frees>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            # Summary                 4989412       4501988       150851        142147
            m = p1.match(line)
            if m:
                group = m.groupdict()
                module = group.pop('type')
                module_dict = ret_dict.setdefault('type', {}). \
                    setdefault(module, {})
                module_dict.update({k:int(v) for k, v in group.items() if v is not None})
                continue

        return ret_dict

class ShowPlatformSoftwareMemorySwitchActiveAllocTypeBrief(ShowPlatformSoftwareMemoryRpActiveAllocTypeBrief):
    """ Parser for
        * show platform software memory mdt-pubd switch active <R0> alloc type component brief
    """

    cli_command = 'show platform software memory {process} switch active {slot} alloc type {alloc_type} brief'

    def cli(self, process, slot, alloc_type, output=None):

        if output is None:
            out = self.device.execute(self.cli_command.format(
                process=process,
                slot=slot,
                alloc_type=alloc_type))
        else:
            out = output

        return super().cli(process=process, alloc_type=alloc_type, output=out)


class ShowPlatformSoftwareIomdMacsecInterfaceBriefSchema(MetaParser):
    """ Schema for
        * show platform software iomd 1/0 macsec interface {interface} brief
    """
    schema = {
        Optional('tx-sc'): {
            Any(): {
                'sub-interface': str,
                'sc-idx': str,
                'pre-cur-an': str,
                'sci': str,
                'sa-vp-rule-idx': str,
                'cipher': str
            }
        },
        Optional('rx-sc'): {
            Any(): {
                'sub-interface': str,
                'sc-idx': str,
                'pre-cur-an': str,
                'sci': str,
                'sa-vp-rule-idx': str,
                'cipher': str
            }
        }
    }


class ShowPlatformSoftwareIomdMacsecInterfaceBrief(ShowPlatformSoftwareIomdMacsecInterfaceBriefSchema):
    """ Parser for
        * show platform software iomd 1/0 macsec interface {interface} brief
    """

    cli_command = 'show platform software iomd 1/0 macsec interface {interface} brief'

    def cli(self, interface, output=None):

        if output is None:
            out = self.device.execute(self.cli_command.format(
                interface=interface))
        else:
            out = output

        ret_dict = {}
        #Tx SC
        p1 = re.compile(r'(.*)Tx SC')

        #Rx SC
        p2 = re.compile(r'(.*)Rx SC')

        #3/11  |   0    |     3/0    | f87a41252702008b | 50331759/ 2/ 1  |     GCM_AES_128 |
        p3 = re.compile(r'(?P<if>\d+\/\d+) +\|'
                        ' +(?P<sc_idx>\d+) +\|'
                        ' +(?P<pre_cur_an>\d+\/\d+) +\|'
                        ' +(?P<sci>\S+) +\|'
                        ' +(?P<idx>\d+\/ \d+\/ \d+) +\|'
                        ' +(?P<cipher>\S+) +\|'
                        )

        sess_tx=0
        sess_rx=0
        for line in out.splitlines():
            line = line.strip()
            m1 = p1.match(line)
            if m1:
                sc = 'tx'
                tx_sc = ret_dict.setdefault('tx-sc', {})
            m2 = p2.match(line)
            if m2:
                sc = 'rx'
                rx_sc = ret_dict.setdefault('rx-sc', {})
            m3 = p3.match(line)
            if m3:
                group = m3.groupdict()
                if sc == 'tx':
                    sess_tx+=1
                    sc_tx_dict = tx_sc.setdefault(sess_tx, {})
                    sc_tx_dict['sub-interface'] = group['if']
                    sc_tx_dict['sc-idx'] = group['sc_idx']
                    sc_tx_dict['pre-cur-an'] = group['pre_cur_an']
                    sc_tx_dict['sci'] = group['sci']
                    sc_tx_dict['sa-vp-rule-idx'] = group['idx']
                    sc_tx_dict['cipher'] = group['cipher']
                elif sc == 'rx':
                    sess_rx+=1
                    sc_rx_dict = rx_sc.setdefault(sess_rx, {})
                    sc_rx_dict['sub-interface'] = group['if']
                    sc_rx_dict['sc-idx'] = group['sc_idx']
                    sc_rx_dict['pre-cur-an'] = group['pre_cur_an']
                    sc_rx_dict['sci'] = group['sci']
                    sc_rx_dict['sa-vp-rule-idx'] = group['idx']
                    sc_rx_dict['cipher'] = group['cipher']
        return ret_dict


class ShowPlatformSoftwareIomdMacsecInterfaceDetailSchema(MetaParser):
    """ Schema for
        * show platform software iomd 1/0 macsec interface {interface} detail
    """
    schema = {
        Optional('subport-11-tx'): {
                'bypass': str,
                'cipher': str,
                'conf-offset': str,
                'cur-an': str,
                'delay-protection': str,
                'encrypt': str,
                'end-station': str,
                'hashkey-len': str,
                'key-len': str,
                'next-pn': str,
                'prev-an': str,
                'rule-index': str,
                'sa-index': str,
                'scb': str,
                'sci': str,
                'vlan': str,
                'vport-index': str
        },
        Optional('subport-12-tx'): {
                'bypass': str,
                'cipher': str,
                'conf-offset': str,
                'cur-an': str,
                'delay-protection': str,
                'encrypt': str,
                'end-station': str,
                'hashkey-len': str,
                'key-len': str,
                'next-pn': str,
                'prev-an': str,
                'rule-index': str,
                'sa-index': str,
                'scb': str,
                'sci': str,
                'vlan': str,
                'vport-index': str
        },
        Optional('subport-11-rx'): {
                   'bypass': str,
                   'cipher': str,
                   'conf-offset': str,
                   'cur-an': str,
                   'decrypt-frames': str,
                   'hashkey-len': str,
                   'key-len': str,
                   'next-pn': str,
                   'prev-an': str,
                   'replay-protect': str,
                   'replay-window-size': str,
                   'rule-index': str,
                   'sa-index': str,
                   'sci': str,
                   'validate-frames': str,
                   'vport-index': str
       },
        Optional('subport-12-rx'): {
                   'bypass': str,
                   'cipher': str,
                   'conf-offset': str,
                   'cur-an': str,
                   'decrypt-frames': str,
                   'hashkey-len': str,
                   'key-len': str,
                   'next-pn': str,
                   'prev-an': str,
                   'replay-protect': str,
                   'replay-window-size': str,
                   'rule-index': str,
                   'sa-index': str,
                   'sci': str,
                   'validate-frames': str,
                   'vport-index': str
       }}



class ShowPlatformSoftwareIomdMacsecInterfaceDetail(ShowPlatformSoftwareIomdMacsecInterfaceDetailSchema):
    """ Parser for
        * show platform software iomd 1/0 macsec interface {interface} detail
    """

    cli_command = 'show platform software iomd 1/0 macsec interface {interface} detail'

    def cli(self, interface, output=None):

        if output is None:
            out = self.device.execute(self.cli_command.format(
                interface=interface))
        else:
            out = output

        ret_dict = {}

        #Port:3, Subport:11, Tx SC index:0
        p1 = re.compile(r'Port\:\d+\, Subport\:(.*)\, Tx SC index')

        #Port:3, Subport:11, Rx SC index:0
        p2 = re.compile(r'Port\:\d+\, Subport\:(.*)\, Rx SC index')

        #Prev AN: 3, Cur AN: 0
        p3 = re.compile(r'Prev AN\: (?P<prev_an>\d+)\, +'
                        'Cur AN\: (?P<cur_an>\d+)')

        #SA index: 50331759, vport index: 2, rule index: 1
        p4 = re.compile(r'SA index\: (?P<sa_index>\d+)\, +'
                        'vport index\: (?P<vport_index>\d+)\, +'
                        'rule index\: (?P<rule_index>\d+)')

        #key_len: 16
        p5 = re.compile(r'^key_len\: (?P<key_len>\d+)$')

        #hashkey_len: 16
        p6 = re.compile(r'^hashkey_len\: (?P<hashkey_len>\d+)$')

        #bypass: 0
        p7 = re.compile(r'^bypass\: (?P<bypass>\d+)$')

        #nextPn: 1
        p8 = re.compile(r'^nextPn\: (?P<nextPn>\d+)$')

        #conf_offset: 0
        p9 = re.compile(r'^conf_offset\: (?P<conf_offset>\d+)$')

        #encrypt: 1
        p10 = re.compile(r'^encrypt\: (?P<encrypt>\d+)$')

        #vlan: 1
        p11 = re.compile(r'^vlan\: (?P<vlan>\d+)$')

        #end_station: 0
        p12 = re.compile(r'^end_station\: (?P<end_station>\d+)$')

        #scb: 0
        p13 = re.compile(r'^scb\: (?P<scb>\d+)$')

        #cipher: GCM_AES_128
        p14 = re.compile(r'^cipher\: (?P<cipher>\S+)$')

        #Delay protection: 0
        p15 = re.compile(r'^Delay protection\: (?P<delay_protection>\d+)$')

        #replay_protect: 1
        p16 = re.compile(r'^replay_protect\: (?P<replay_protect>\d+)$')

        #replay_window_size: 0
        p17 = re.compile(r'^replay_window_size\: (?P<replay_window_size>\d+)$')

        #decrypt_frames: 1
        p18 = re.compile(r'^decrypt_frames\: (?P<decrypt_frames>\d+)$')

        #validate_frames: 1
        p19 = re.compile(r'^validate_frames\: (?P<validate_frames>\d+)$')

        #sci:ecce1346f902008c
        p20 = re.compile(r'^sci\:(?P<sci>\S+)$')

        for line in out.splitlines():
            line = line.strip()
            m1 = p1.match(line)
            if m1:
                sc = 'tx'
                subport_tx = m1.group(1)
                subport_tx_dict = ret_dict.setdefault('subport-{}-tx'.format(subport_tx), {})
            m2 = p2.match(line)
            if m2:
                sc = 'rx'
                subport_rx = m2.group(1)
                subport_rx_dict = ret_dict.setdefault('subport-{}-rx'.format(subport_rx), {})
            m3 = p3.match(line)
            if m3:
                group = m3.groupdict()
                if sc == 'tx':
                    subport_tx_dict['prev-an'] = group['prev_an']
                    subport_tx_dict['cur-an'] = group['cur_an']
                elif sc == 'rx':
                    subport_rx_dict['prev-an'] = group['prev_an']
                    subport_rx_dict['cur-an'] = group['cur_an']
            m4 = p4.match(line)
            if m4:
                group = m4.groupdict()
                if sc == 'tx':
                    subport_tx_dict['sa-index'] = group['sa_index']
                    subport_tx_dict['vport-index'] = group['vport_index']
                    subport_tx_dict['rule-index'] = group['rule_index']
                elif sc == 'rx':
                    subport_rx_dict['sa-index'] = group['sa_index']
                    subport_rx_dict['vport-index'] = group['vport_index']
                    subport_rx_dict['rule-index'] = group['rule_index']
            m5 = p5.match(line)
            if m5:
                group = m5.groupdict()
                if sc == 'tx':
                    subport_tx_dict['key-len'] = group['key_len']
                elif sc == 'rx':
                    subport_rx_dict['key-len'] = group['key_len']
            m6 = p6.match(line)
            if m6:
                group = m6.groupdict()
                if sc == 'tx':
                    subport_tx_dict['hashkey-len'] = group['hashkey_len']
                elif sc == 'rx':
                    subport_rx_dict['hashkey-len'] = group['hashkey_len']
            m7 = p7.match(line)
            if m7:
                group = m7.groupdict()
                if sc == 'tx':
                    subport_tx_dict['bypass'] = group['bypass']
                elif sc == 'rx':
                    subport_rx_dict['bypass'] = group['bypass']
            m8 = p8.match(line)
            if m8:
                group = m8.groupdict()
                if sc == 'tx':
                    subport_tx_dict['next-pn'] = group['nextPn']
                elif sc == 'rx':
                    subport_rx_dict['next-pn'] = group['nextPn']
            m9 = p9.match(line)
            if m9:
                group = m9.groupdict()
                if sc == 'tx':
                   subport_tx_dict['conf-offset'] = group['conf_offset']
                elif sc == 'rx':
                   subport_rx_dict['conf-offset'] = group['conf_offset']
            m10 = p10.match(line)
            if m10:
                group = m10.groupdict()
                if sc == 'tx':
                    subport_tx_dict['encrypt'] = group['encrypt']
                elif sc == 'rx':
                    subport_rx_dict['encrypt'] = group['encrypt']
            m11 = p11.match(line)
            if m11:
                group = m11.groupdict()
                if sc == 'tx':
                    subport_tx_dict['vlan'] = group['vlan']
                elif sc == 'rx':
                    subport_rx_dict['vlan'] = group['vlan']
            m12 = p12.match(line)
            if m12:
                group = m12.groupdict()
                if sc == 'tx':
                    subport_tx_dict['end-station'] = group['end_station']
                elif sc == 'rx':
                    subport_rx_dict['end-station'] = group['end_station']
            m13 = p13.match(line)
            if m13:
                group = m13.groupdict()
                if sc == 'tx':
                    subport_tx_dict['scb'] = group['scb']
                elif sc == 'rx':
                    subport_rx_dict['scb'] = group['scb']
            m14 = p14.match(line)
            if m14:
                group = m14.groupdict()
                if sc == 'tx':
                    subport_tx_dict['cipher'] = group['cipher']
                elif sc == 'rx':
                    subport_rx_dict['cipher'] = group['cipher']
            m15 = p15.match(line)
            if m15:
                group = m15.groupdict()
                if sc == 'tx':
                    subport_tx_dict['delay-protection'] = group['delay_protection']
                elif sc == 'rx':
                    subport_rx_dict['delay-protection'] = group['delay_protection']
            m16 = p16.match(line)
            if m16:
                group = m16.groupdict()
                if sc == 'tx':
                    subport_tx_dict['replay-protect'] = group['replay_protect']
                elif sc == 'rx':
                    subport_rx_dict['replay-protect'] = group['replay_protect']
            m17 = p17.match(line)
            if m17:
                group = m17.groupdict()
                if sc == 'tx':
                    subport_tx_dict['replay-window-size'] = group['replay_window_size']
                elif sc == 'rx':
                    subport_rx_dict['replay-window-size'] = group['replay_window_size']
            m18 = p18.match(line)
            if m18:
                group = m18.groupdict()
                if sc == 'tx':
                     subport_tx_dict['decrypt-frames'] = group['decrypt_frames']
                elif sc == 'rx':
                     subport_rx_dict['decrypt-frames'] = group['decrypt_frames']
            m19 = p19.match(line)
            if m19:
                group = m19.groupdict()
                if sc == 'tx':
                    subport_tx_dict['validate-frames'] = group['validate_frames']
                elif sc == 'rx':
                    subport_rx_dict['validate-frames'] = group['validate_frames']
            m20 = p20.match(line)
            if m20:
                group = m20.groupdict()
                if sc == 'tx':
                    subport_tx_dict['sci'] = group['sci']
                elif sc == 'rx':
                    subport_rx_dict['sci'] = group['sci']

        return ret_dict


class ShowPlatformSoftwareFedactiveFnfEtAnalyticsFlowsSchema(MetaParser):
    """ Schema for
        * show platform software fed active fnf et-analytics-flows
    """
    schema = {
            'current-eta-records': int,
            'excess-packets-received': int,
            'excess-syn-received': int,
            'total-eta-fnf': int,
            'total-eta-idp': int,
            'total-eta-records': int,
            'total-eta-splt': int,
            'total-packets-out-of-order': int,
            'total-packets-received': int,
            'total-packets-retransmitted': int
            }


class ShowPlatformSoftwareFedactiveFnfEtAnalyticsFlows(ShowPlatformSoftwareFedactiveFnfEtAnalyticsFlowsSchema):
    """ Parser for
        * show platform software fed active fnf et-analytics-flows
    """

    cli_command = 'show platform software fed active fnf et-analytics-flows'

    def cli(self, output=None):

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        #Total packets received     : 80
        p1 = re.compile(r'Total +packets +received +: +(?P<total_pkts>\d+)')

        #Excess packets received    : 60
        p2 = re.compile(r'Excess +packets +received +: +(?P<excess_pkts>\d+)')

        #Excess syn received        : 0
        p3 = re.compile(r'Excess +syn +received +: +(?P<excess_syn>\d+)')

        #Total eta records added    : 4
        p4 = re.compile(r'Total +eta +records +added +: +(?P<tot_eta>\d+)')

        #Current eta records        : 0
        p5 = re.compile(r'Current +eta +records +: +(?P<cur_eta>\d+)')

        #Total eta splt exported    : 2
        p6 = re.compile(r'Total +eta +splt +exported +: +(?P<eta_splt>\d+)')

        #Total eta IDP exported     : 2
        p7 = re.compile(r'Total +eta +IDP +exported +: +(?P<eta_idp>\d+)')

        #Total eta-fnf records      : 2
        p8 = re.compile(r'Total +eta\-fnf +records +: +(?P<eta_fnf>\d+)')

        #Total retransmitted pkts   : 0
        p9 = re.compile(r'Total +retransmitted +pkts +: +(?P<retr_pkts>\d+)')

        #Total out of order pkts    : 0
        p10 = re.compile(r'Total +out +of +order +pkts +: +(?P<order_pkts>\d+)')


        for line in out.splitlines():
            line = line.strip()

            #Total packets received     : 80
            m1 = p1.match(line)
            if m1:
                group = m1.groupdict()
                ret_dict["total-packets-received"] = int(group["total_pkts"])

            #Excess packets received    : 60
            m2 = p2.match(line)
            if m2:
                group = m2.groupdict()
                ret_dict["excess-packets-received"] = int(group["excess_pkts"])

            #Excess syn received        : 0
            m3 = p3.match(line)
            if m3:
                group = m3.groupdict()
                ret_dict["excess-syn-received"] = int(group["excess_syn"])

            #Total eta records added    : 4
            m4 = p4.match(line)
            if m4:
                group = m4.groupdict()
                ret_dict["total-eta-records"] = int(group["tot_eta"])

            #Current eta records        : 0
            m5 = p5.match(line)
            if m5:
                group = m5.groupdict()
                ret_dict["current-eta-records"] = int(group["cur_eta"])

            #Total eta splt exported    : 2
            m6 = p6.match(line)
            if m6:
                group = m6.groupdict()
                ret_dict["total-eta-splt"] = int(group["eta_splt"])

            #Total eta IDP exported     : 2
            m7 = p7.match(line)
            if m7:
                group = m7.groupdict()
                ret_dict["total-eta-idp"] = int(group["eta_idp"])

            #Total eta-fnf records      : 2
            m8 = p8.match(line)
            if m8:
                group = m8.groupdict()
                ret_dict["total-eta-fnf"] = int(group["eta_fnf"])

            #Total retransmitted pkts   : 0
            m9 = p9.match(line)
            if m9:
                group = m9.groupdict()
                ret_dict["total-packets-retransmitted"] = int(group["retr_pkts"])

            #Total out of order pkts    : 0
            m10 = p10.match(line)
            if m10:
                group = m10.groupdict()
                ret_dict["total-packets-out-of-order"] = int(group["order_pkts"])
        return ret_dict

# =============================================
# Schema for 'show platform software fed switch active mpls forwarding label <label> detail'
# Schema for 'show platform software fed active mpls forwarding label <label> detail'
# =============================================
class ShowPlatformSoftwareFedSchema(MetaParser):
    """ Schema for:
        *show platform software fed {switch} active mpls forwarding label {label} detail
        *show platform software fed active mpls forwarding label {label} detail
    """
    schema = {
        'lentry_label':{
            Any():{
                'nobj': list,
                'lentry_hdl': str,
                'modify_cnt': int,
                'backwalk_cnt': int,
                'lspa_handle': str,
                'aal':{
                    'id': int,
                    'lbl': int,
                    'eos0':{
                        'adj_hdl': str,
                        'hw_hdl': str,
                        },
                    'eos1':{
                        'adj_hdl': str,
                        'hw_hdl': str,
                    },
                    'deagg_vrf_id': int,
                    'lspa_handle': str,
                    },
                Optional('eos'):{
                    'objid': int,
                    'local_label': int,
                    'flags': str,
                    'pdflags': str,
                    'nobj0': list,
                    'nobj1': list,
                    'modify': int,
                    'bwalk': int,
                },
                Optional('label'):{
                    Any():{
                        'link_type': str,
                        'local_label': int,
                        'outlabel': str,
                        'flags': {
                            Any(): list,
                        },
                        'pdflags': {
                            Any(): list,
                        },
                        'adj_handle': str,
                        'unsupported_recursion': int,
                        'olbl_changed': int,
                        'local_adj': int,
                        'modify_cnt': int,
                        'bwalk_cnt': int,
                        'subwalk_cnt': int,
                        'collapsed_oce': int,
                        Optional('label_aal'):{
                            Any():{
                                'lbl': int,
                                'smac': str,
                                'dmac': str,
                                'sub_type': int,
                                'link_type': int,
                                'adj_flags': str,
                                'label_type': int,
                                'rewrite_type': str,
                                'vlan_id': int,
                                'vrf_id': int,
                                'ri': str,
                                'ri_id': str,
                                'phdl': str,
                                'ref_cnt':int,
                                'si': str,
                                'si_id': str,
                                'di_id': str,
                                },
                            },
                        },
                    },
                Optional('adj'):{
                    Any():{
                        'link_type': str,
                        'ifnum': str,
                        'adj': str,
                        'si': str,
                        Optional('IPv4'): str,
                        },
                    },
                Optional('objid'):{
                    Any():{
                        'SPECIAL': str,
                    },
                },

                Optional('lb'):{
                    Any():{
                        'ecr_map_objid': int,
                        'link_type': str,
                        'num_choices': int,
                        'flags': str,
                        'mpls_ecr': int,
                        'local_label': int,
                        'path_inhw': int,
                        'ecrh': str,
                        'old_ecrh': str,
                        'modify_cnt': int,
                        'bwalk_cnt': int,
                        'subwalk_cnt': int,
                        'finish_cnt': int,
                        Optional('bwalk'):{
                            'req': int,
                            'in_prog': int,
                            'nested': int,
                            },
                        Optional('aal'):{
                            'ecr_id': int,
                            'af': int,
                            'ecr_type': str,
                            'ref': int,
                            'ecrh': str,
                            'hwhdl': str,
                        }
                    },
                },
                Optional('sw_enh_ecr_scale'):{
                    Any():{
                        'llabel': int,
                        'eos': int,
                        'adjs': int,
                        'mixed_adj': str,
                        'reprogram_hw': str,
                        'ecrhdl': str,
                        'ecr_hwhdl': str,
                        'mod_cnt': int,
                        'prev_npath': int,
                        'pmismatch': int,
                        'pordermatch': int,
                        Optional('ecr_adj'):{
                            Any():{
                                Optional('is_mpls_adj'): int,
                                Optional('l3adj_flags'): str,
                                Optional('recirc_adj_id'): int,
                                'sih': str,
                                'di_id': int,
                                'rih': str,
                                Optional('adj_lentry'): str,
                            },
                        },
                    },
                },

            }
        }
    }

# ================================================================
# Parser for:
#   * 'show platform software fed '
# ================================================================
class ShowPlatformSoftwareFed(ShowPlatformSoftwareFedSchema):
    ''' Parser for:
        ' show platform software fed {switch} active mpls forwarding label {label} detail'
        ' show platform software fed active mpls forwarding label {label} detail '
    '''

    cli_command = ['show platform software fed active mpls forwarding label {label} detail',
                   'show platform software fed {switch} active mpls forwarding label {label} detail']
    def cli(self, label='',switch='',output=None):
        ''' cli for:
         ' show platform software fed {switch} active mpls forwarding label {label} detail '
         ' show platform software fed active mpls forwarding label {label} detail '
        '''
        if output is None:
            # Build command
            if not switch:
                cmd = self.cli_command[0].format(label=label)
            else:
                cmd = self.cli_command[1].format(switch=switch, label=label)
            # Execute command
            out = self.device.execute(cmd)
        else:
            out = output


        #LENTRY:label:22 nobj:(EOS, 142) lentry_hdl:0xde00000a
        p1 = re.compile(r'^LENTRY:label:+(?P<label>\d+)\s+nobj:\(+'
                        r'(?P<nobj>[\w\, ]+)+\)\s+lentry_hdl:+(?P<lentry_hdl>\S+)$')

        #modify_cnt:1 backwalk_cnt:2
        p2 = re.compile(r'^modify_cnt:+(?P<modify_cnt>\d+)\s+'
                        r'backwalk_cnt:+(?P<backwalk_cnt>\d+)$')

        #lspa_handle:0
        p3 = re.compile(r'^lspa_handle:+(?P<lspa_handle>\w+)$')

        #AAL: id:3724541962 lbl:22
        p4 = re.compile(r'^AAL:\s+id:+(?P<id>\d+)\s+lbl:+(?P<lbl>\d+)$')

        #eos0:[adj_hdl:0x83000039, hw_hdl:0x7f02737c6628]
        p5 = re.compile(r'^eos0:\[+adj_hdl:+(?P<adj_hdl>\w+)+,\s+hw_hdl:+(?P<hw_hdl>\w+)+\]+$')

        #eos1:[adj_hdl:0x3d000038, hw_hdl:0x7f02737c6478]
        p6 = re.compile(r'^eos1:\[+adj_hdl:+(?P<adj_hdl>\w+)+,\s+hw_hdl:+'
                        r'(?P<hw_hdl>\w+)+\]+$')

        #deagg_vrf_id = 0 lspa_handle:0
        p7 = re.compile(r'^deagg_vrf_id\s+=\s+(?P<deagg_vrf_id>\d+)+\s+lspa_handle:+'
                        r'(?P<lspa_handle>\w+)+$')

        #EOS:objid:142 local_label:0 flags:0:() pdflags:0
        p8 = re.compile(r'^EOS:+objid:+(?P<objid>\d+)\s+local_label:+'
                        r'(?P<local_label>\d+)\s+flags:+\S:+'
                        r'(?P<flags>[\S\s]+)\s+pdflags:+'
                        r'(?P<pdflags>\S+)$')

        #nobj0:(LABEL, 143), nobj1:(LABEL, 141) modify:1 bwalk:0
        p9 = re.compile(r'^nobj0:\(+(?P<nobj0>[\w\,\s]+)+\)+\,\s+nobj1:\(+'
                        r'(?P<nobj1>[\w\,\s]+)+\)\s+modify:+(?P<modify>\d+)\s+bwalk:+(?P<bwalk>\d+)$')

        #LABEL:objid:143 link_type:MPLS local_label:22 outlabel:(3, 0)
        p10 = re.compile(r'LABEL:+objid:+(?P<objid>\d+)\s+link_type:+'
                         r'(?P<link_type>\w+)\s+local_label:+'
                         r'(?P<local_label>\d+)\s+outlabel:+(?P<outlabel>[\S\s]+)$')

        #flags:0x18:(POP,PHP,) pdflags:0:(INSTALL_HW_OK,) adj_handle:0x83000039
        p11 = re.compile(r'flags:+(?P<flagid>\w+)+:\(+(?P<flagstr>\S+)+\,+\)+\s+pdflags:+'
                         r'(?P<pdflagid>\w+)+:\(+(?P<pdflagstr>\S+)+\,+\)+\s+adj_handle:+(?P<adj_handle>\w+)$')

        #unsupported recursion:0 olbl_changed 0 local_adj:0 modify_cnt:0
        p12 = re.compile(r'^unsupported\s+recursion:+(?P<unsupported_recursion>\d+)\s+olbl_changed\s+'
                         r'(?P<olbl_changed>\d+)\s+local_adj:+'
                         r'(?P<local_adj>\d+)\s+modify_cnt:+(?P<modify_cnt>\d+)$')

        #bwalk_cnt:0 subwalk_cnt:0 collapsed_oce:0
        p13 = re.compile(r'^bwalk_cnt:+(?P<bwalk_cnt>\d+)\s+subwalk_cnt:+'
                         r'(?P<subwalk_cnt>\d+)\s+collapsed_oce:+(?P<collapsed_oce>\d+)$')

        #AAL: id:2197815353 lbl:0 smac:00a7.42d6.c41f dmac:0027.90bf.2ee7
        p14 = re.compile(r'^AAL:\s+id:+(?P<id>\d+)\s+lbl:+(?P<lbl>\d+)\s+smac:+'
                         r'(?P<smac>\S+)\s+dmac:+(?P<dmac>\S+)$')

        #sub_type:0 link_type:2 adj_flags:0 label_type:1 rewrite_type:POP2MPLS(138)
        p15 = re.compile(r'^sub_type:+(?P<sub_type>\d+)\s+link_type:+'
                         r'(?P<link_type>\d+)\s+adj_flags:+(?P<adj_flags>\w+)\s+label_type:+'
                         r'(?P<label_type>\d+)\s+rewrite_type:+(?P<rewrite_type>\S+)$')

        #vlan_id:0 vrf_id:0 ri:0x7f02737cc1e8, ri_id:0x3e phdl:0xab000447, ref_cnt:1
        p16 = re.compile(r'^vlan_id:+(?P<vlan_id>\d+)\s+vrf_id:+(?P<vrf_id>\d+)\s+ri:+'
                         r'(?P<ri>\w+)+,\s+ri_id:+(?P<ri_id>\w+)\s+phdl:+'
                         r'(?P<phdl>\w+)+,\s+ref_cnt:+(?P<ref_cnt>\d+)$')

        #si:0x7f02737cc6b8, si_id:0x4027, di_id:0x526d
        p17 = re.compile(r'^si:+(?P<si>\w+)+,\s+si_id:+(?P<si_id>\w+)+,\s+di_id:+(?P<di_id>\w+)$')

        #ADJ:objid:139 {link_type:MPLS ifnum:0x36, adj:0x5c000037, si: 0x7f02737a2348  }
        p18 = re.compile(r'ADJ:objid:+(?P<objid>\d+) +{link_type:(?P<link_type>\w+) +ifnum:(?P<ifnum>\w+), +adj:(?P<adj>\w+), +si: +(?P<si>\w+) +}$')

        #ADJ:objid:137 {link_type:IP ifnum:0x36, adj:0x63000036, si: 0x7f02737a2348  IPv4:     172.16.25.2 }
        p19 = re.compile(r'ADJ:objid:+(?P<objid>\d+) +{link_type:(?P<link_type>\w+) +ifnum:(?P<ifnum>\w+), +adj:(?P<adj>\w+), +si: +(?P<si>\w+) +IPv4: +(?P<IPv4>[\d\.]+) +}$')

        #LENTRY:label:75 not found...
        p20 = re.compile(r'^LENTRY:label:+(?P<label>\d+)\snot +found\S+$')

        #AAL: Handle not found:0
        p21 = re.compile(r'^AAL:\s+Handle\ not\ found:\S$')

        #LB:obj_id:38 ecr_map_objid:0 link_type:IP num_choices:2 Flags:0
        p22 = re.compile(r'LB:+obj_id:+(?P<obj_id>\d+)\s+ecr_map_objid:+'
                         r'(?P<ecr_map_objid>\d+)\s+link_type:+'
                         r'(?P<link_type>\w+)\s+num_choices:+'
                         r'(?P<num_choices>\d+)\s+Flags:+(?P<flags>\w+)$')

        #mpls_ecr:1 local_label:24 path_inhw:2 ecrh:0xf9000002 old_ecrh:0
        p23 = re.compile(r'mpls_ecr:+(?P<mpls_ecr>\d+)\s+local_label:+'
                         r'(?P<local_label>\d+)\s+path_inhw:+'
                         r'(?P<path_inhw>\d+)\s+ecrh:+'
                         r'(?P<ecrh>\w+)\s+old_ecrh:+(?P<old_ecrh>\w+)$')

        #modify_cnt:0 bwalk_cnt:0 subwalk_cnt:0 finish_cnt:0
        p24 = re.compile(r'modify_cnt:+(?P<modify_cnt>\d+)\s+bwalk_cnt:+'
                         r'(?P<bwalk_cnt>\d+)\s+subwalk_cnt:+'
                         r'(?P<subwalk_cnt>\d+)\s+finish_cnt:+'+
                         r'(?P<finish_cnt>\d+)$')

        #bwalk:[req:0 in_prog:0 nested:0]
        p25 = re.compile(r'bwalk:\[+req:+(?P<req>\d+)\s+in_prog:+'
                         r'(?P<in_prog>\d+)\s+nested:+(?P<nested>\d+)+\]+$')

        #AAL: ecr:id:4177526786 af:0 ecr_type:0 ref:3 ecrh:0x7f02737e49f8(28:2)
        p26 = re.compile(r'AAL:\s+ecr:id:+(?P<ecr_id>\d+)\s+af:(?P<af>\d+)\s+ecr_type:+'
                         r'(?P<ecr_type>\w+)\s+ref:+(?P<ref>\d+)\s+ecrh:+(?P<ecrh>\S+)+$')

        #hwhdl:1937656312 ::0x7f02737e11c8,0x7f02737e2728,0x7f02737e11c8,0x7f02737e2728
        p27 = re.compile(r'hwhdl+(?P<hwhdl>[\S\s]+)$')

        #Sw Enh ECR scale: objid:38 llabel:24 eos:1 #adjs:2 mixed_adj:0
        p28 = re.compile(r'Sw +Enh +ECR +scale:\s+objid:+(?P<objid>\d+)\s+llabel:+'
                         r'(?P<llabel>\d+)\s+eos:+(?P<eos>\d+)\s+\#adjs:+'
                         r'(?P<adjs>\d+)\s+mixed_adj:+(?P<mixed_adj>\w+)$')

        #reprogram_hw:0 ecrhdl:0xf9000002 ecr_hwhdl:0x7f02737e49f8
        p29 = re.compile(r'reprogram_hw:+(?P<reprogram_hw>\w+)\s+ecrhdl:+'
                         r'(?P<ecrhdl>\w+)\s+ecr_hwhdl:+(?P<ecr_hwhdl>\w+)$')

        # mod_cnt:0 prev_npath:0 pmismatch:0 pordermatch:0
        p30 = re.compile(r'mod_cnt:+(?P<mod_cnt>\d+)\s+prev_npath:+'
                         r'(?P<prev_npath>\d+)\s+pmismatch:+(?P<pmismatch>\d+)\s+pordermatch:+'
                         r'(?P<pordermatch>\d+)$')

        #ecr_adj: id:1644167265 is_mpls_adj:1 l3adj_flags:0x100000
        p31 = re.compile(r'(?P<ecr_adj>\S+):\s+id:+(?P<id>\d+)\s+is_mpls_adj:+'
                         r'(?P<is_mpls_adj>\d+)\s+l3adj_flags:+(?P<l3adj_flags>\w+)$')

        # recirc_adj_id:3120562239
        p32 = re.compile(r'recirc_adj_id:+(?P<recirc_adj_id>\d+)$')

        # sih:0x7f02737e11c8(182) di_id:20499 rih:0x7f02737e0bf8(74)
        p33 = re.compile(r'sih:+(?P<sih>\S+)\s+di_id:(?P<di_id>\d+)\s+rih:+(?P<rih>\S+)$')

        # adj_lentry [eos0:0x7f02734123b8 eos1:0x7f02737ec5e8]
        p34 = re.compile(r'adj_lentry\s+(?P<adj_lentry>[\S\s]+)$')

        #ecr_prefix_adj: id:2483028067 (ref:1)
        p35 = re.compile(r'(?P<ecr_prefix_adj>\S+):\s+id:+(?P<id>\d+)\s+\S+$')

        #objid:ADJ SPECIAL:0
        p36 = re.compile(r'objid:+(?P<objid>\S+)\s+SPECIAL:+(?P<SPECIAL>\w+)$')

        # Init vars
        ret_dict = {}
        for line in out.splitlines():
            line = line.strip()
            eos_dict = {}

            #LENTRY:label:22 nobj:(EOS, 142) lentry_hdl:0xde00000a
            m = p1.match(line)
            if m:
                group = m.groupdict()
                label_id = int(group['label'])
                lentry_dict = ret_dict.setdefault('lentry_label', {}).setdefault(label_id, {})
                lentry_dict['nobj'] = list(str(group['nobj']).split(','))
                lentry_dict['lentry_hdl'] = group['lentry_hdl']
                continue

            #modify_cnt:1 backwalk_cnt:2
            m = p2.match(line)
            if m:
                group = m.groupdict()
                lentry_dict['modify_cnt'] = int(group['modify_cnt'])
                lentry_dict['backwalk_cnt'] = int(group['backwalk_cnt'])
                continue

            #lspa_handle:0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                lentry_dict['lspa_handle'] = str(group['lspa_handle'])
                continue

            #AAL: id:3724541962 lbl:22
            m = p4.match(line)
            if m:
                group = m.groupdict()
                aal_dict = ret_dict['lentry_label'][label_id].setdefault('aal', {})
                aal_dict['id'] = int(group['id'])
                aal_dict['lbl'] = int(group['lbl'])
                continue

            #eos0:[adj_hdl:0x83000039, hw_hdl:0x7f02737c6628]
            m = p5.match(line)
            if m:
                group = m.groupdict()
                eos0_dict = ret_dict['lentry_label'][label_id]['aal'].setdefault('eos0', {})
                eos0_dict['adj_hdl'] = str(group['adj_hdl'])
                eos0_dict['hw_hdl'] = str(group['hw_hdl'])
                continue

            #eos1:[adj_hdl:0x3d000038, hw_hdl:0x7f02737c6478]
            m = p6.match(line)
            if m:
                group = m.groupdict()
                eos1_dict = ret_dict['lentry_label'][label_id]['aal'].setdefault('eos1', {})
                eos1_dict['adj_hdl'] = str(group['adj_hdl'])
                eos1_dict['hw_hdl'] = str(group['hw_hdl'])
                continue

            #deagg_vrf_id = 0 lspa_handle:0
            m = p7.match(line)
            if m:
                group = m.groupdict()
                aal_dict['deagg_vrf_id'] = int(group['deagg_vrf_id'])
                aal_dict['lspa_handle'] = str(group['lspa_handle'])
                continue

            #EOS:objid:142 local_label:0 flags:0:() pdflags:0
            m = p8.match(line)
            if m:
                group = m.groupdict()
                eos_dict = ret_dict['lentry_label'][label_id].setdefault('eos', {})
                eos_dict['objid'] = int(group['objid'])
                eos_dict['local_label'] = int(group['local_label'])
                eos_dict['flags'] = str(group['flags'])
                eos_dict['pdflags'] = str(group['pdflags'])
                continue

            #nobj0:(LABEL, 143), nobj1:(LABEL, 141) modify:1 bwalk:0
            m = p9.match(line)
            if m:
                group = m.groupdict()
                ret_dict['lentry_label'][label_id]['eos']['nobj0'] = list(str(group['nobj0']).split(', '))
                ret_dict['lentry_label'][label_id]['eos']['nobj1'] = list(str(group['nobj1']).split(', '))
                ret_dict['lentry_label'][label_id]['eos']['modify']=int(group['modify'])
                ret_dict['lentry_label'][label_id]['eos']['bwalk'] = int(group['bwalk'])
                continue

            #LABEL:objid:143 link_type:MPLS local_label:22 outlabel:(3, 0)
            m = p10.match(line)
            if m:
                group = m.groupdict()
                objid = int(group['objid'])
                label_dict = ret_dict['lentry_label'][label_id].setdefault('label', {}).setdefault(objid, {})
                label_dict['link_type'] = str(group['link_type'])
                label_dict['local_label'] = int(group['local_label'])
                label_dict['outlabel'] = str(group['outlabel'])
                continue

            #flags:0x18:(POP,PHP,) pdflags:0:(INSTALL_HW_OK,) adj_handle:0x83000039
            m = p11.match(line)
            if m:
                group = m.groupdict()
                label_dict['flags'] = {}
                flagid = str(group['flagid'])
                flagstr = str(group['flagstr'])
                flaglist = list(flagstr.split(','))
                label_dict['flags'][flagid] = flaglist
                label_dict['pdflags'] = {}
                flagid = str(group['pdflagid'])
                flagstr = str(group['pdflagstr'])
                flaglist = list(flagstr.split(','))
                label_dict['pdflags'][flagid] = flaglist
                label_dict['adj_handle'] = str(group['adj_handle'])
                continue

            #unsupported recursion:0 olbl_changed 0 local_adj:0 modify_cnt:0
            m = p12.match(line)
            if m:
                group = m.groupdict()
                label_dict['unsupported_recursion'] = int(group['unsupported_recursion'])
                label_dict['olbl_changed'] = int(group['olbl_changed'])
                label_dict['local_adj'] = int(group['local_adj'])
                label_dict['modify_cnt'] = int(group['modify_cnt'])
                continue

            #bwalk_cnt:0 subwalk_cnt:0 collapsed_oce:0
            m = p13.match(line)
            if m:
                group = m.groupdict()
                label_dict['bwalk_cnt'] = int(group['bwalk_cnt'])
                label_dict['subwalk_cnt'] = int(group['subwalk_cnt'])
                label_dict['collapsed_oce'] = int(group['collapsed_oce'])
                continue

            #AAL: id:2197815353 lbl:0 smac:00a7.42d6.c41f dmac:0027.90bf.2ee7
            m = p14.match(line)
            if m:
                group = m.groupdict()
                id = int(group['id'])
                labelaal_dict = ret_dict['lentry_label'][label_id]['label'][objid].setdefault('label_aal', {}).setdefault(id, {})
                labelaal_dict['lbl'] = int(group['lbl'])
                labelaal_dict['smac'] = str(group['smac'])
                labelaal_dict['dmac'] = str(group['dmac'])
                continue

            #sub_type:0 link_type:2 adj_flags:0 label_type:1 rewrite_type:POP2MPLS(138)
            m = p15.match(line)
            if m:
                group = m.groupdict()
                labelaal_dict['sub_type'] = int(group['sub_type'])
                labelaal_dict['link_type'] = int(group['link_type'])
                labelaal_dict['adj_flags'] = str(group['adj_flags'])
                labelaal_dict['label_type'] = int(group['label_type'])
                labelaal_dict['rewrite_type'] = str(group['rewrite_type'])
                continue

            #vlan_id:0 vrf_id:0 ri:0x7f02737cc1e8, ri_id:0x3e phdl:0xab000447, ref_cnt:1
            m = p16.match(line)
            if m:
                group = m.groupdict()
                labelaal_dict['vlan_id'] = int(group['vlan_id'])
                labelaal_dict['vrf_id'] = int(group['vrf_id'])
                labelaal_dict['ri'] = str(group['ri'])
                labelaal_dict['ri_id'] = str(group['ri_id'])
                labelaal_dict['phdl'] = str(group['phdl'])
                labelaal_dict['ref_cnt'] = int(group['ref_cnt'])
                continue

            #si:0x7f02737cc6b8, si_id:0x4027, di_id:0x526d
            m = p17.match(line)
            if m:
                group = m.groupdict()
                labelaal_dict['si'] = str(group['si'])
                labelaal_dict['si_id'] = str(group['si_id'])
                labelaal_dict['di_id'] = str(group['di_id'])
                continue

            #ADJ:objid:71 {link_type:MPLS ifnum:0x7c, adj:0x53000020, si: 0x7ff791190278
            m = p18.match(line)
            if m:
                group = m.groupdict()
                objid = int(group['objid'])
                adj_dict = ret_dict['lentry_label'][label_id].setdefault('adj', {}).setdefault(objid, {})
                adj_dict['link_type'] = str(group['link_type'])
                adj_dict['ifnum'] = str(group['ifnum'])
                adj_dict['adj'] = str(group['adj'])
                adj_dict['si'] = str(group['si'])
                continue

            #ADJ:objid:139 {link_type:MPLS ifnum:0x36, adj:0x5c000037, si: 0x7f02737a2348  }
            m = p19.match(line)
            if m:
                group = m.groupdict()
                objid = int(group['objid'])
                adj_dict = ret_dict['lentry_label'][label_id].setdefault('adj', {}).setdefault(objid, {})
                adj_dict['link_type'] = str(group['link_type'])
                adj_dict['ifnum'] = str(group['ifnum'])
                adj_dict['adj'] = str(group['adj'])
                adj_dict['si'] = str(group['si'])
                adj_dict['IPv4'] = str(group['IPv4'])
                continue

            #LENTRY:label:75 not found...
            m = p20.match(line)
            if m:
                group = m.groupdict()
                label_id = int(group['label'])
                lentry_dict = ret_dict.setdefault('lentry_label', {}).setdefault(label_id,{})
                lentry_dict['label'] = int(group['label'])
                continue

            #AAL: Handle not found:0
            m = p21.match(line)
            if m:
                group = m.groupdict()
                labelaal_dict = ret_dict['lentry_label'][label_id].setdefault('aal', {})
                continue

            #LB:obj_id:38 ecr_map_objid:0 link_type:IP num_choices:2 Flags:0
            m = p22.match(line)
            if m:
                group = m.groupdict()
                objid1 = int(group['obj_id'])
                lb_dict = ret_dict['lentry_label'][label_id].setdefault('lb', {}).setdefault(objid1, {})
                lb_dict['ecr_map_objid'] = int(group['ecr_map_objid'])
                lb_dict['link_type'] = str(group['link_type'])
                lb_dict['num_choices'] = int(group['num_choices'])
                lb_dict['flags'] = str(group['flags'])
                continue

            #mpls_ecr:1 local_label:24 path_inhw:2 ecrh:0xf9000002 old_ecrh:0
            m = p23.match(line)
            if m:
                group = m.groupdict()
                lb_dict['mpls_ecr'] = int(group['mpls_ecr'])
                lb_dict['local_label'] = int(group['local_label'])
                lb_dict['path_inhw'] = int(group['path_inhw'])
                lb_dict['ecrh'] = str(group['ecrh'])
                lb_dict['old_ecrh'] = str(group['old_ecrh'])
                continue

            #modify_cnt:0 bwalk_cnt:0 subwalk_cnt:0 finish_cnt:0
            m = p24.match(line)
            if m:
                group = m.groupdict()
                lb_dict['modify_cnt'] = int(group['modify_cnt'])
                lb_dict['bwalk_cnt'] = int(group['bwalk_cnt'])
                lb_dict['subwalk_cnt'] = int(group['subwalk_cnt'])
                lb_dict['finish_cnt'] = int(group['finish_cnt'])
                lb_dict['aal'] = {}
                lb_dict['bwalk'] = {}
                continue

            #bwalk:[req:0 in_prog:0 nested:0]
            m = p25.match(line)
            if m:
                group = m.groupdict()
                lb_dict['bwalk']['req'] = int(group['req'])
                lb_dict['bwalk']['in_prog'] = int(group['in_prog'])
                lb_dict['bwalk']['nested'] = int(group['nested'])
                continue

            #AAL: ecr:id:4177526786 af:0 ecr_type:0 ref:3 ecrh:0x7f02737e49f8(28:2)
            m = p26.match(line)
            if m:
                group = m.groupdict()
                lb_dict['aal']['ecr_id'] = int(group['ecr_id'])
                lb_dict['aal']['af'] = int(group['af'])
                lb_dict['aal']['ecr_type'] = str(group['ecr_type'])
                lb_dict['aal']['ref'] = int(group['ref'])
                lb_dict['aal']['ecrh'] = str(group['ecrh'])
                continue

            #hwhdl:1937656312 ::0x7f02737e11c8,0x7f02737e2728,0x7f02737e11c8,0x7f02737e2728
            m = p27.match(line)
            if m:
                group = m.groupdict()
                lb_dict['aal']['hwhdl'] = str(group['hwhdl'])
                continue

            #Sw Enh ECR scale: objid:38 llabel:24 eos:1 #adjs:2 mixed_adj:0
            m = p28.match(line)
            if m:
                group = m.groupdict()
                objid = int(group['objid'])
                ecr_dict = ret_dict['lentry_label'][label_id].setdefault('sw_enh_ecr_scale', {}).setdefault(objid, {})
                ecr_dict['llabel'] = int(group['llabel'])
                ecr_dict['eos'] = int(group['eos'])
                ecr_dict['adjs'] = int(group['adjs'])
                ecr_dict['mixed_adj'] = str(group['mixed_adj'])
                continue

            #reprogram_hw:0 ecrhdl:0xf9000002 ecr_hwhdl:0x7f02737e49f8
            m = p29.match(line)
            if m:
                group = m.groupdict()
                ecr_dict['reprogram_hw'] = str(group['reprogram_hw'])
                ecr_dict['ecrhdl'] = str(group['ecrhdl'])
                ecr_dict['ecr_hwhdl'] = str(group['ecr_hwhdl'])
                continue

            # mod_cnt:0 prev_npath:0 pmismatch:0 pordermatch:0
            m = p30.match(line)
            if m:
                group = m.groupdict()
                ecr_dict['mod_cnt'] = int(group['mod_cnt'])
                ecr_dict['prev_npath'] = int(group['prev_npath'])
                ecr_dict['pmismatch'] = int(group['pmismatch'])
                ecr_dict['pordermatch'] = int(group['pordermatch'])
                ecr_dict['ecr_adj'] = {}
                continue

            #ecr_adj: id:1644167265 is_mpls_adj:1 l3adj_flags:0x100000
            m = p31.match(line)
            if m:
                group = m.groupdict()
                id1 = int(group['id'])
                ecr_dict['ecr_adj'][id1] = {}
                ecr_dict['ecr_adj'][id1]['is_mpls_adj'] = int(group['is_mpls_adj'])
                ecr_dict['ecr_adj'][id1]['l3adj_flags'] = str(group['l3adj_flags'])
                continue

            # recirc_adj_id:3120562239
            m = p32.match(line)
            if m:
                group = m.groupdict()
                ecr_dict['ecr_adj'][id1]['recirc_adj_id'] = int(group['recirc_adj_id'])
                continue

            # sih:0x7f02737e11c8(182) di_id:20499 rih:0x7f02737e0bf8(74)
            m = p33.match(line)
            if m:
                group = m.groupdict()
                ecr_dict['ecr_adj'][id1]['sih'] = str(group['sih'])
                ecr_dict['ecr_adj'][id1]['di_id'] = int(group['di_id'])
                ecr_dict['ecr_adj'][id1]['rih'] = str(group['rih'])
                continue

            # adj_lentry [eos0:0x7f02734123b8 eos1:0x7f02737ec5e8]
            m = p34.match(line)
            if m:
                group = m.groupdict()
                ecr_dict['ecr_adj'][id1]['adj_lentry'] = str(group['adj_lentry'])
                continue

            #ecr_prefix_adj: id:2483028067 (ref:1)
            m = p35.match(line)
            if m:
                group = m.groupdict()
                id1 = int(group['id'])
                ecr_dict['ecr_adj'][id1] = {}
                continue

            #objid:ADJ SPECIAL:0
            m = p36.match(line)
            if m:
                group = m.groupdict()
                lentry_dict['objid'] = {}
                id2 = str(group['objid'])
                lentry_dict['objid'][id2] = {}
                lentry_dict['objid'][id2]['SPECIAL'] = str(group['SPECIAL'])
                continue

        return ret_dict


# =============================================
# Schema for 'show platform software fed active acl counters hardware'
# =============================================
class ShowPlatformSoftwareFedactiveAclCountersHardwareSchema(MetaParser):
    """ Schema for
        * show platform software fed active acl counters hardware
    """

    schema = {
        'counters':{
            'unknown_stat_counter' : int,
            'ingress_ipv4_forward' : int,
            'ingress_ipv4_forward_from_cpu' : int,
            'ingress_ipv4_pacl_drop' : int,
            'ingress_ipv4_vacl_drop' : int,
            'ingress_ipv4_racl_drop' : int,
            'ingress_ipv4_gacl_drop' : int,
            'ingress_ipv4_racl_drop_and_log' : int,
            'ingress_ipv4_vacl_drop_and_log' : int,
            'ingress_ipv4_pacl_cpu' : int,
            'ingress_ipv4_vacl_cpu' : int,
            'ingress_ipv4_racl_cpu' : int,
            'ingress_ipv4_gacl_cpu' : int,
            'ingress_ipv4_tcp_mss_cpu' : int,
            'ingress_ipv6_forward' : int,
            'ingress_ipv6_forward_from_cpu' : int,
            'ingress_ipv6_pacl_drop' : int,
            'ingress_ipv6_vacl_drop' : int,
            'ingress_ipv6_racl_drop' : int,
            'ingress_ipv6_gacl_drop' : int,
            'ingress_ipv6_racl_drop_and_log' : int,
            'ingress_ipv6_vacl_drop_and_log' : int,
            'ingress_ipv6_pacl_cpu' : int,
            'ingress_ipv6_pacl_sisf_cpu' : int,
            'ingress_ipv6_vacl_cpu' : int,
            'ingress_ipv6_vacl_sisf_cpu' : int,
            'ingress_ipv6_racl_cpu' : int,
            'ingress_ipv6_gacl_cpu' : int,
            'ingress_ipv6_tcp_mss_cpu' : int,
            'ingress_mac_forward' : int,
            'ingress_mac_forward_from_cpu' : int,
            'ingress_mac_pacl_drop' : int,
            'ingress_mac_vacl_drop' : int,
            'ingress_mac_racl_drop' : int,
            'ingress_mac_gacl_drop' : int,
            'ingress_mac_racl_drop_and_log' : int,
            'ingress_mac_vacl_drop_and_log' : int,
            'ingress_mac_pacl_cpu' : int,
            'ingress_mac_vacl_cpu' : int,
            'ingress_mac_racl_cpu' : int,
            'ingress_mac_gacl_cpu' : int,
            'ingress_dai_smac_validation_drop' : int,
            'ingress_dai_dmac_validation_drop' : int,
            'ingress_dai_ip_validation_drop' : int,
            'ingress_arp_acl_permit' : int,
            'ingress_arp_acl_drop' : int,
            'ingress_auth_acl_drop' : int,
            'egress_ipv4_forward' : int,
            'egress_ipv4_forward_to_cpu' : int,
            Optional('egress_ipv4_forward_from_cpu') : int,
            'egress_ipv4_pacl_drop' : int,
            'egress_ipv4_vacl_drop' : int,
            'egress_ipv4_racl_drop' : int,
            'egress_ipv4_gacl_drop' : int,
            'egress_ipv4_racl_drop_and_log' : int,
            'egress_ipv4_vacl_drop_and_log' : int,
            'egress_ipv4_pacl_cpu' : int,
            'egress_ipv4_vacl_cpu' : int,
            'egress_ipv4_racl_cpu' : int,
            'egress_ipv4_gacl_cpu' : int,
            'egress_ipv4_tcp_mss_cpu' : int,
            'egress_ipv6_forward' : int,
            'egress_ipv6_forward_to_cpu' : int,
            Optional('egress_ipv6_forward_from_cpu') : int,
            'egress_ipv6_pacl_drop' : int,
            'egress_ipv6_vacl_drop' : int,
            'egress_ipv6_racl_drop' : int,
            'egress_ipv6_gacl_drop' : int,
            'egress_ipv6_racl_drop_and_log' : int,
            'egress_ipv6_vacl_drop_and_log' : int,
            'egress_ipv6_pacl_cpu' : int,
            'egress_ipv6_vacl_cpu' : int,
            'egress_ipv6_racl_cpu' : int,
            'egress_ipv6_gacl_cpu' : int,
            'egress_ipv6_tcp_mss_cpu' : int,
            'egress_mac_forward' : int,
            'egress_mac_forward_to_cpu' : int,
            Optional('egress_mac_forward_from_cpu') : int,
            'egress_mac_pacl_drop' : int,
            'egress_mac_vacl_drop' : int,
            'egress_mac_racl_drop' : int,
            'egress_mac_gacl_drop' : int,
            'egress_mac_racl_drop_and_log' : int,
            'egress_mac_vacl_drop_and_log' : int,
            'egress_mac_pacl_cpu' : int,
            'egress_mac_vacl_cpu' : int,
            'egress_mac_racl_cpu' : int,
            'egress_mac_gacl_cpu' : int,
            'egress_ipv4_cpu_queues_drop' : int,
            'egress_ipv4_p2p_drop' : int,
            'egress_ipv6_p2p_drop' : int,
            'egress_mac_p2p_drop' : int,
            'egress_ipv4_p2p_redirect' : int,
            'egress_ipv6_p2p_redirect' : int,
            'egress_mac_p2p_redirect' : int,
            'egress_ipv4_sgacl_drop' : int,
            'egress_ipv6_sgacl_drop' : int,
            'egress_ipv4_sgacl_test_cell_drop' : int,
            'egress_ipv6_sgacl_test_cell_drop' : int,
            'egress_ipv4_dns_response_cpu' : int,
            'egress_ipv6_dns_response_cpu' : int,
            'egress_ipv4_pre_sgacl_forward' : int,
        }
    }


class ShowPlatformSoftwareFedactiveAclCountersHardware(ShowPlatformSoftwareFedactiveAclCountersHardwareSchema):
    """ Parser for
        * show platform software fed active acl counters hardware
    """

    cli_command = 'show platform software fed active acl counters hardware'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        # Unknown Stat Counter    : 80
        p1 = re.compile(r'Unknown\s+Stat\s+Counter\s+:\s+(?P<unknown_stats>\d+)')

        # Ingress IPv4 Forward             (0x8d000003):       40365 frames
        # Ingress IPv6 GACL Drop           (0x0a000015):           0 frames
        # Ingress MAC Forward              (0x9100001f):       28270 frames
        # Egress IPv4 Forward              (0x77000030):       20480 frames
        # Egress IPv6 Forward to CPU       (0x5c00003e):           0 frames
        p2 = re.compile(r'^(?P<counter_name>.+[^ ])\s+(\(.+\))?:\s+(?P<num_frames>\d+)\s+frames$')


        for line in output.splitlines():
            line = line.strip()

            # Unknown Stat Counter             (0x49000001):      158905 frames
            m = p1.match(line)
            if m:
                group = m.groupdict()
                counters_dict = ret_dict.setdefault("counters", {})
                counters_dict["unknown_stat_counter"] = \
                    int(group["unknown_stats"])
                continue

            # Ingress IPv4 Forward             (0x8d000003):       40365 frames
            # Ingress IPv6 GACL Drop           (0x0a000015):           0 frames
            # Ingress MAC Forward              (0x9100001f):       28270 frames
            # Egress IPv4 Forward              (0x77000030):       20480 frames
            # Egress IPv6 Forward to CPU       (0x5c00003e):           0 frames
            m = p2.match(line)
            if m:
                group = m.groupdict()
                counter_name = group["counter_name"].lower().replace(" ", "_")
                counters_dict = ret_dict.setdefault("counters", {})
                counters_dict[counter_name] = int(group["num_frames"])
                continue

        return ret_dict


# =======================================================================
# Schema for 'show platform hardware throughput crypto'
# =======================================================================
class ShowPlatformHardwareThroughputCryptoSchema(MetaParser):
    schema = {
        'current_configured_crypto_throughput_level': str,
        'current_enforced_crypto_throughput_level': str,
        'default_crypto_throughput_level': str,
        'level': str,
        'reboot': str,
        'crypto_throughput': str,
        Optional('current_boot_level'): str
    }

# ================================================================
# Parser for 'show platform hardware throughput crypto'
# ================================================================
class ShowPlatformHardwareThroughputCrypto(ShowPlatformHardwareThroughputCryptoSchema):
    ''' Parser for 'show platform hardware throughput crypto' '''

    cli_command = ['show platform hardware throughput crypto']

    def cli(self, output=None):

        if output is None:
            out = self.device.execute(self.cli_command[0])
        else:
            out = output

        ret_dict = {}

        # Current configured crypto throughput level: T3
        p1 = re.compile(r'^Current configured crypto throughput level: (?P<level>.+)$')

        # Current enforced crypto throughput level: 10G
        p2 = re.compile(r'^Current enforced crypto throughput level: (?P<level>.+)$')

        # Default Crypto throughput level: 2.5G
        p3 = re.compile(r'^Default Crypto throughput level: (?P<level>.+)$')

        # Level is saved, reboot is not required
        p4 = re.compile(r'^Level is (?P<saved>[^,]+), reboot is (?P<reboot>.+)$')

        # Crypto Throughput is not throttled
        p5 = re.compile(r'^Crypto Throughput is (?P<throttled>.+)$')

        # Current boot level is network-premier
        p6 = re.compile(r'^Current boot level is (?P<level>.+)$')

        for line in out.splitlines():
            line = line.strip()
            # Current configured crypto throughput level: T3
            m = p1.match(line)
            if m:
                ret_dict['current_configured_crypto_throughput_level'] = m.groupdict()['level']
                continue

            # Current enforced crypto throughput level: 10G
            m = p2.match(line)
            if m:
                ret_dict['current_enforced_crypto_throughput_level'] = m.groupdict()['level']
                continue

            # Default Crypto throughput level: 2.5G
            m = p3.match(line)
            if m:
                ret_dict['default_crypto_throughput_level'] = m.groupdict()['level']
                continue

            # Level is saved, reboot is not required
            m = p4.match(line)
            if m:
                ret_dict['level'] = m.groupdict()['saved']
                ret_dict['reboot'] = m.groupdict()['reboot']
                continue

            # Crypto Throughput is not throttled
            m = p5.match(line)
            if m:
                ret_dict['crypto_throughput'] = m.groupdict()['throttled']
                continue

            # Current boot level is network-premier
            m = p6.match(line)
            if m:
                ret_dict['current_boot_level'] = m.groupdict()['level']
                continue

        return ret_dict

# ============================================================================
# Schema for 'show platform software fed active inject packet-capture detailed'
# ===========================================================================
class ShowPlatformSoftwareFedActiveInjectPacketCaptureDetailedSchema(MetaParser):
    """ Schema for
            * show platform software fed active inject packet-capture detailed
        """
    schema = {
        'inject_packet_capture': str,
        'buffer_wrapping': str,
        'total_captured': int,
        'capture_capacity': int,
        'capture_filter': str,
        'inject_packet_number': {
            Any():{
                'interface': {
                    'pal': {
                        'iifd': str
                    },
                },
                'metadata': {
                    'cause': str,
                    'sub_cause': str,
                    'q_no': str,
                    'linktype': str
                },
                'ether_hdr_1': {
                    'dest_mac': str,
                    'src_mac': str
                },
                'ether_hdr_2': {
                    'ether_type': str
                },
                'ipv4_hdr_1': {
                    'dest_ip': str,
                    'src_ip': str
                },
                'ipv4_hdr_2': {
                    'packet_len': str,
                    'ttl': str,
                    'protocol': str
                },
                'udp_hdr': {
                    'dest_port': str,
                    'src_port': str
                },
                'doppler_frame_descriptor': {
                    'fdformat': str,
                    'system_ttl': str,
                    'fdtype': str,
                    'span_session_map': str,
                    'qoslabel': str,
                    'fpe_first_header_type': str
                }

            }
        }
    }

# ================================================================
# Parser for:
#   * 'show platform software fed active inject packet-capture detailed'
# ================================================================
class ShowPlatformSoftwareFedActiveInjectPacketCaptureDetailed(
    ShowPlatformSoftwareFedActiveInjectPacketCaptureDetailedSchema):
    """ Parser for:
            show platform software fed active inject packet-capture detailed
    """

    cli_command = ['show platform software fed active inject packet-capture detailed']

    def cli(self, output=None):
        """ cli for:
         ' show platform software fed active inject packet-capture detailed '
        """

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        #Inject packet capturing: disabled. Buffer wrapping: disabled
        p1 = re.compile(r'^Inject +packet +capturing:+\s+(?P<inject_packet_capture>\w+)\.+\s+'
                        r'Buffer +wrapping:\s+(?P<buffer_wrapping>\w+)$')

        #Total captured so far: 4 packets. Capture capacity : 4096 packets
        p2 = re.compile(r'^Total +captured +so +far:\s(?P<total_captured>\d)+\s+packets+\.\s+'
                       r'Capture +capacity +:\s+(?P<capture_capacity>\d+)+\s+packets$')

        #Capture filter : "udp.port == 9995"
        p3 = re.compile(r'^Capture +filter +: +(?P<capture_filter>.+)$')

        #------ Inject Packet Number: 1, Timestamp: 2021/09/15 07:40:40.603 ------
        p4 = re.compile(r'^-+\s+Inject +Packet +Number: +(?P<inject_packet_no>\d+)')

        #interface : pal:  [if-id: 0x00000000]
        p5 = re.compile(r'^interface +: pal: \s+\[+if-id: +(?P<iifd>\S+)$')

        #metadata  : cause: 2 [QFP destination lookup], sub-cause: 1, q-no: 0, linktype: MCP_LINK_TYPE_IP [1]
        p6 = re.compile(r'^metadata +: +cause: +(?P<cause>.+)'
                        r'\s+sub-cause: +(?P<sub_cause>\d+)\, +q-no: +(?P<q_no>\d+)\,'
                        r'\s+linktype: +(?P<linktype>.+)')

        #ether hdr : dest mac: 3c57.3104.6a00, src mac: 3c57.3104.6a00
        p7 = re.compile(r'^ether +hdr +: +dest +mac: +(?P<dest_mac>\S+)\s+src +mac: +(?P<src_mac>\S+)')

        #ether hdr : ethertype: 0x0800 (IPv4)
        p8 = re.compile(r'^ether +hdr +: +ethertype: +(?P<ether_type>.+)$')

        #ipv4  hdr : dest ip: 111.0.0.2, src ip: 111.0.0.1
        p9 = re.compile(r'^ipv4 +hdr +: +dest +ip: +(?P<dest_ip>\S+)\s+src +ip: +(?P<src_ip>\S+)')

        #ipv4  hdr : packet len: 188, ttl: 255, protocol: 17 (UDP)
        p10 = re.compile(r'^ipv4 +hdr +: +packet +len: +(?P<packet_len>\d+)\,\s+ttl: +(?P<ttl>\d+)'
                         r'\,+\s+protocol: +(?P<protocol>.+)$')

        #udp   hdr : dest port: 9995, src port: 53926
        p11 = re.compile(r'^udp +hdr +: +dest +port: +(?P<dest_port>\d+)\,\s+src +port: +(?P<src_port>\d+)')

        #Doppler Frame Descriptor :
        p12 = re.compile(r'^Doppler +Frame +Descriptor +:(?P<doppler_frame_descriptor>)$')

        #fdFormat                  = 0x3            systemTtl                 = 0x8
        p13 = re.compile(r'^fdFormat\s+\= (?P<fdformat>\S+)\s+systemTtl\s+\= (?P<system_ttl>\S+$)')

        #fdType                    = 0x1            spanSessionMap            = 0
        p14 = re.compile(r'^fdType\s+\= (?P<fdtype>\S+)\s+spanSessionMap\s+\= (?P<span_session_map>\S+$)')

        #qosLabel                  = 0x81           fpeFirstHeaderType        = 0
        p15 = re.compile(r'^qosLabel\s+\= (?P<qoslabel>\S+)\s+fpeFirstHeaderType\s+\= (?P<fpe_first_header_type>\S+$)')

        ret_dict = {}
        for line in out.splitlines():
            line = line.strip()

            # Inject packet capturing: disabled. Buffer wrapping: disabled
            m = p1.match(line)
            if m:
                ret_dict.update({
                    'inject_packet_capture': m.groupdict()['inject_packet_capture'],
                    'buffer_wrapping': m.groupdict()['buffer_wrapping']
                })
                continue

            # Total captured so far: 4 packets. Capture capacity : 4096 packets
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({
                    'total_captured':int(group['total_captured']),
                    'capture_capacity':int(group['capture_capacity'])
                })
                continue

            # Capture filter : "udp.port == 9995"
            m = p3.match(line)
            if m:
                ret_dict.update({'capture_filter': m.groupdict()['capture_filter']})
                continue

            # ------ Inject Packet Number: 1, Timestamp: 2021/09/15 07:40:40.603 ------
            m = p4.match(line)
            if m:
                group = m.groupdict()
                inject_packet_num = group['inject_packet_no']
                inject_packet_dict = ret_dict.setdefault('inject_packet_number', {}).setdefault(inject_packet_num, {})
                continue

            # interface : pal:  [if-id: 0x00000000]
            m = p5.match(line)
            if m:
                group = m.groupdict()
                int_dict = ret_dict['inject_packet_number'][inject_packet_num].setdefault('interface', {})
                pal_dict = ret_dict['inject_packet_number'][inject_packet_num]['interface'].setdefault('pal',{})
                pal_dict['iifd'] = group['iifd']
                continue

            # metadata  : cause: 2 [QFP destination lookup], sub-cause: 1, q-no: 0, linktype: MCP_LINK_TYPE_IP [1]
            m = p6.match(line)
            if m:
                group = m.groupdict()
                meta_data_dict = ret_dict['inject_packet_number'][inject_packet_num].setdefault('metadata',{})
                meta_data_dict['cause'] = group['cause']
                meta_data_dict['sub_cause'] = group['sub_cause']
                meta_data_dict['q_no'] = group['q_no']
                meta_data_dict['linktype'] = group['linktype']
                continue

            # ether hdr : dest mac: 3c57.3104.6a00, src mac: 3c57.3104.6a00
            m = p7.match(line)
            if m:
                group = m.groupdict()
                ether_hdr_1_dict = ret_dict['inject_packet_number'][inject_packet_num].setdefault('ether_hdr_1',{})
                ether_hdr_1_dict['dest_mac'] = group['dest_mac']
                ether_hdr_1_dict['src_mac'] = group['src_mac']
                continue

            # ether hdr : ethertype: 0x0800 (IPv4)
            m = p8.match(line)
            if m:
                group = m.groupdict()
                ether_hdr_2_dict = ret_dict['inject_packet_number'][inject_packet_num].setdefault('ether_hdr_2',{})
                ether_hdr_2_dict['ether_type'] = group['ether_type']
                continue

            # ipv4  hdr : dest ip: 111.0.0.2, src ip: 111.0.0.1
            m = p9.match(line)
            if m:
                group = m.groupdict()
                ipv4_hdr_1_dict = ret_dict['inject_packet_number'][inject_packet_num].setdefault('ipv4_hdr_1',{})
                ipv4_hdr_1_dict['dest_ip'] = group['dest_ip']
                ipv4_hdr_1_dict['src_ip'] = group['src_ip']
                continue

            # ipv4  hdr : packet len: 188, ttl: 255, protocol: 17 (UDP)
            m = p10.match(line)
            if m:
                group = m.groupdict()
                ipv4_hdr_2_dict = ret_dict['inject_packet_number'][inject_packet_num].setdefault('ipv4_hdr_2',{})
                ipv4_hdr_2_dict['packet_len'] = group['packet_len']
                ipv4_hdr_2_dict['ttl'] = group['ttl']
                ipv4_hdr_2_dict['protocol'] = group['protocol']
                continue

            # udp   hdr : dest port: 9995, src port: 53926
            m = p11.match(line)
            if m:
                group = m.groupdict()
                udp_hdr_dict = ret_dict['inject_packet_number'][inject_packet_num].setdefault('udp_hdr',{})
                udp_hdr_dict['dest_port'] = group['dest_port']
                udp_hdr_dict['src_port'] = group['src_port']
                continue

            # Doppler Frame Descriptor :
            m = p12.match(line)
            if m:
                group = m.groupdict()
                doppler_frame_des_dict = ret_dict['inject_packet_number'][inject_packet_num].setdefault(
                    'doppler_frame_descriptor',{})
                continue

            # fdFormat                  = 0x3            systemTtl                 = 0x8
            m = p13.match(line)
            if m:
                group = m.groupdict()
                doppler_frame_des_dict['fdformat'] = group['fdformat']
                doppler_frame_des_dict['system_ttl'] = group['system_ttl']
                continue

            # fdType                    = 0x1            spanSessionMap            = 0
            m = p14.match(line)
            if m:
                group = m.groupdict()
                doppler_frame_des_dict['fdtype'] = group['fdtype']
                doppler_frame_des_dict['span_session_map'] = group['span_session_map']
                continue

            # qosLabel                  = 0x81           fpeFirstHeaderType        = 0
            m = p15.match(line)
            if m:
                group = m.groupdict()
                doppler_frame_des_dict['qoslabel'] = group['qoslabel']
                doppler_frame_des_dict['fpe_first_header_type'] = group['fpe_first_header_type']
                continue

        return ret_dict

 # ===============================================================================
# Schema for 'show platform software dpidb index'
# ===============================================================================
class ShowPlatformSoftwareDpidIndexSchema(MetaParser):
    """Schema for :
        show platform software dpidb index"""

    schema = {
        Any(): {
            'index' : int,
        },
    }

# ===============================================================================
# Parser for 'show platform software dpidb index'
# ===============================================================================
class ShowPlatformSoftwareDpidIndex(ShowPlatformSoftwareDpidIndexSchema):
    """parser for :
        show platform software dpidb index"""

    cli_command = 'show platform software dpidb index'

    def cli(self, output=None,):

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        result_dict = {}
        #Index 1030 -- swidb Hu1/0/1
        p1 = re.compile(r'^Index\s+(?P<index>\d+)\s+--\s+swidb\s+(?P<interface>\S+)$')

        for line in out.splitlines():
            line = line.strip()
            #Index 1030 -- swidb Hu1/0/1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                interface = group.pop('interface')
                interface_dict = result_dict.setdefault(interface,{})
                interface_dict.update({
                    'index' : int(group['index']),
                })
                continue

        return result_dict

# =============================================================================
#  Schema for
#  * 'show platform software fed switch active ifm mappings lpn'
#  * 'show platform software fed switch active ifm mappings lpn | {interface}'
# ==============================================================================
class ShowPlatformSoftwareFedSwitchActiveIfmMappingsLpnSchema(MetaParser):
    """Schema for 'show platform software fed switch active ifm mappings lpn'
    """
    schema = {
        'interfaces':{
            Any(): {
                'lpn': int,
                'asic': int,
                'port': int,
                'if_id': str,
                'active': str
            }
        },
    }

# ===============================================================================
#  Parser for
#  * 'show platform software fed switch active ifm mappings lpn'
#  * 'show platform software fed switch active ifm mappings lpn | i {interface}'
# ================================================================================
class ShowPlatformSoftwareFedSwitchActiveIfmMappingsLpn(ShowPlatformSoftwareFedSwitchActiveIfmMappingsLpnSchema):
    """
    Parser for :
        * show platform software fed switch active ifm mappings lpn
    """

    cli_command = ['show platform software fed switch active ifm mappings lpn',
                   'show platform software fed switch active ifm mappings lpn | include {interface}']

    def cli(self, interface="", output=None):
        if output is None:
            if interface:
                cmd = self.cli_command[1].format(interface=interface)
            else:
                cmd = self.cli_command[0]
            output = self.device.execute(cmd)

        #19   1     18    TenGigabitEthernet1/0/19   0x0000001b  y
        p = re.compile(r'^(?P<lpn>\d+)\s+(?P<asic>\d+)\s+(?P<port>\d+)\s+(?P<interfaces>\S+)\s+(?P<if_id>(0x([\da-fA-F]){8}))\s+(?P<active>\S+)$')

        # initial return dictionary
        ret_dict ={}

        for line in output.splitlines():
            line = line.strip()

            #19    1  18    TenGigabitEthernet1/0/19   0x0000001b  y
            m = p.match(line)
            if m:

                group = m.groupdict()
                interfaces = group['interfaces']
                sub_dict = ret_dict.setdefault('interfaces', {}).setdefault(interfaces, {})

                lpn = group['lpn']
                sub_dict['lpn'] = int(lpn)

                asic = group['asic']
                sub_dict['asic'] = int(asic)

                port = group['port']
                sub_dict['port'] = int(port)

                if_id = group['if_id']
                sub_dict['if_id'] = if_id

                active = group['active']
                sub_dict['active'] = active
                continue
        return ret_dict


# =================================================================
#  Schema for 'show platform software fed switch active ptp domain
# ================================================================
class ShowPlatformSoftwareFedSwitchActivePtpDomainSchema(MetaParser):
    """Schema for 'show platform software fed switch active ptp domain
    """
    schema = {
        'domain_number': {
            Any(): {
                'profile_type': str,
                'profile_state': str,
                Optional('clock_mode'): str,
                Optional('delay_mechanism'): str,
                Optional('ptp_clock'): str,
                Optional('mean_path_delay_ns'): int,
                'transport_method': str,
                'message_general_ip_dscp': int,
                'message_event_ip_dscp': int
            }
        },
    }
# =================================================================
#  Parser for 'show platform software fed switch active ptp domain
# ================================================================
class ShowPlatformSoftwareFedSwitchActivePtpDomain(ShowPlatformSoftwareFedSwitchActivePtpDomainSchema):
    """
    Parser for :
        * show platform software fed switch active ptp domain
    """

    cli_command = 'show platform software fed switch active ptp domain'

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)

        #Displaying data for domain number 0
        p1 = re.compile(r'^Displaying\sdata\sfor\sdomain\snumber\s(?P<domain_number>\d+)$')

        #Profile Type : DEFAULT
        p2 = re.compile(r'^Profile\sType\s\:\s(?P<profile_type>[a-zA-Z]+)$')

        #Profile State: enabled
        p3 = re.compile(r'^Profile\sState\:\s(?P<profile_state>\S+)$')

        #Clock Mode : BOUNDARY CLOCK
        p4 = re.compile(r'^Clock\sMode\s\:\s(?P<clock_mode>[A-Z\s]+)$')

        #Delay Mechanism: : END-TO-END
        p5 = re.compile(r'^Delay\sMechanism\:\s\:\s(?P<delay_mechanism>[A-Z\-]+)$')

        #PTP clock : 1970-1-24 22:41:20
        p6 = re.compile(r'^PTP\sclock\s\:\s(?P<ptp_clock>[\d\-\:\s]+)$')

        #mean_path_delay 83 nanoseconds
        p7 = re.compile(r'^mean_path_delay\s(?P<mean_path_delay_ns>\d+)\snanoseconds$')

        #Transport Method : 802.3
        p8 = re.compile(r'^Transport\sMethod\s\:\s(?P<transport_method>[\w\.\-]+)$')

        #Message general ip dscp  : 47
        p9 = re.compile(r'^Message\sgeneral\sip\sdscp\s+\:\s(?P<message_general_ip_dscp>\d+)$')

        #Message event ip dscp    : 59
        p10 = re.compile(r'^Message\sevent\sip\sdscp\s+\:\s(?P<message_event_ip_dscp>\d+)$')

        # initial return dictionary
        ret_dict ={}

        for line in output.splitlines():
            line = line.strip()

            #Displaying data for domain number 0
            m = p1.match(line)
            if m:
                ret_dict.setdefault('domain_number',{})
                domain_number = m.groupdict()['domain_number']
                sub_dict = ret_dict['domain_number'].setdefault(int(domain_number),{})
                continue

            #Profile Type : DEFAULT
            m = p2.match(line)
            if m:
                profile_type = m.groupdict()['profile_type']
                sub_dict['profile_type'] = profile_type
                continue

            #Profile State: enabled
            m = p3.match(line)
            if m:
                profile_state = m.groupdict()['profile_state']
                sub_dict['profile_state'] = profile_state
                continue

            #Clock Mode : BOUNDARY CLOCK
            m = p4.match(line)
            if m:
                clock_mode = m.groupdict()['clock_mode']
                sub_dict['clock_mode'] = clock_mode
                continue

            #Delay Mechanism: : END-TO-END
            m = p5.match(line)
            if m:
                delay_mechanism  = m.groupdict()['delay_mechanism']
                sub_dict['delay_mechanism'] = delay_mechanism
                continue

            #PTP clock : 1970-1-24 22:41:20
            m = p6.match(line)
            if m:
                ptp_clock = m.groupdict()['ptp_clock']
                sub_dict['ptp_clock'] = ptp_clock
                continue

            #mean_path_delay 83 nanoseconds
            m = p7.match(line)
            if m:
                mean_path_delay_ns = m.groupdict()['mean_path_delay_ns']
                sub_dict['mean_path_delay_ns'] = int(mean_path_delay_ns)
                continue

            #Transport Method : 802.3
            m = p8.match(line)
            if m:
                transport_method = m.groupdict()['transport_method']
                sub_dict['transport_method'] = transport_method
                continue

            #Message general ip dscp  : 47
            m = p9.match(line)
            if m:
                message_general_ip_dscp = m.groupdict()['message_general_ip_dscp']
                sub_dict['message_general_ip_dscp'] = int(message_general_ip_dscp)
                continue

            #Message event ip dscp    : 59
            m = p10.match(line)
            if m:
                message_event_ip_dscp = m.groupdict()['message_event_ip_dscp']
                sub_dict['message_event_ip_dscp'] = int(message_event_ip_dscp)
                continue
        return ret_dict

# ================================================================================
#  Schema for 'show platform software fed switch active ptp interface {interface}'
# ================================================================================
class ShowPlatformSoftwareFedSwitchActivePtpInterfaceInterfaceSchema(MetaParser):
    """Schema for 'show platform software fed switch active ptp interface {interface}'
    """
    schema = {
        'ptp_interface': {
            'ptp_info': {
                'if_id': str,
                'version': int,
                Optional('ptp_vlan_is_valid'): str,
                Optional('ptp_vlan_id'): int,
            },
            'port_info': {
                'mac_address': str,
                'clock_identity': str,
                'number': int,
                Optional('mode'): int,
                'state': str,
                'port_enabled': str
            },

            'num_info': {
                'num_sync_messages_transmitted': int,
                'num_followup_messages_transmitted': int,
                'num_sync_messages_received': int,
                'num_followup_messages_received': int,
                'num_delay_requests_transmitted': int,
            'num_delay_responses_received': int,
            'num_delay_requests_received': int,
            'num_delay_responses_transmitted': int
            },
            'domain_value': int,
            'profile_type': str,
            'clock_mode': str,
            'delay_mechanism': str,
            'ptt_port_enabled': str,
            'sync_seq_num': int,
            'delay_req_seq_num': int,
            'log_mean_sync_interval': int,
            'log_mean_delay_interval': int,
            Optional('tag_native_vlan'): str,
        }
    }

# =================================================================================
#  Parser for 'show platform software fed switch active ptp interface {interface}'
# =================================================================================
class ShowPlatformSoftwareFedSwitchActivePtpInterfaceInterface(ShowPlatformSoftwareFedSwitchActivePtpInterfaceInterfaceSchema):
    """
    Parser for :
        * show platform software fed switch active ptp interface {interface}
    """

    cli_command = 'show platform software fed switch active ptp interface {interface}'

    def cli(self, interface="", output=None):

        if output is None:
            output = self.device.execute(self.cli_command.format(interface=interface))

        #Displaying port data for if_id 2a
        #Displaying port data for if_id 29
        p1 = re.compile(r'^Displaying\sport\sdata\sfor\sif_id\s(?P<if_id>\S+)$')

        #Port Mac Address 34:ED:1B:7D:F2:A1
        p2 = re.compile(r'^Port\sMac\sAddress\s(?P<mac_address>([\da-fA-F]:?).*)$')

        #Port Clock Identity 34:ED:1B:FF:FE:7D:F2:80
        p3 = re.compile(r'^Port\sClock\sIdentity\s(?P<clock_identity>([\da-fA-F]:?).*)$')

        #Port number 33
        p4 = re.compile(r'^Port\snumber\s(?P<number>\d+)$')

        #PTP Version 2
        p5 = re.compile(r'^PTP\sVersion\s(?P<version>\d+)$')

        #domain_value 0
        p6 = re.compile(r'^domain_value\s(?P<domain_value>\d+)$')

        #Profile Type: : DEFAULT
        p7 = re.compile(r'^Profile\sType\:\s\:\s(?P<profile_type>\S+)$')

        #Clock Mode : BOUNDARY CLOCK
        p8 = re.compile(r'^Clock\sMode\s\:\s(?P<clock_mode>.*)$')

        #Delay mechanism: End-to-End
        p9 = re.compile(r'^Delay\smechanism\:\s(?P<delay_mechanism>\S+)$')

        #port_enabled: TRUE
        p10 = re.compile(r'^port_enabled\:\s(?P<port_enabled>\S+)$')

        #ptt_port_enabled: TRUE
        p11 = re.compile(r'^ptt_port_enabled\:\s(?P<ptt_port_enabled>\S+)$')

        #Port state: : SLAVE
        p12 = re.compile(r'^Port\sstate\:\s\:\s(?P<state>\S+)$')

        #sync_seq_num 2189
        p13 = re.compile(r'^sync_seq_num\s(?P<sync_seq_num>\d+)$')

        #delay_req_seq_num 0
        p14 = re.compile(r'^delay_req_seq_num\s(?P<delay_req_seq_num>\d+)$')

        #log mean sync interval -3
        p15 = re.compile(r'^log\smean\ssync\sinterval\s(?P<log_mean_sync_interval>[-?\d]+)$')

        #log mean delay interval -5
        p16 = re.compile(r'^log\smean\sdelay\sinterval\s(?P<log_mean_delay_interval>[-?\d]+)$')

        #ptp vlan is valid : FALSE
        p17 = re.compile(r'^ptp\svlan\sis\svalid\s\:\s(?P<ptp_vlan_is_valid>\S+)$')

        #ptp vlan id 0
        p18 = re.compile(r'^ptp\svlan\sid\s(?P<ptp_vlan_id>\d+)$')

        #port mode 2
        p19 = re.compile(r'^port\smode\s(?P<mode>\d+)$')

        #tag native vlan : FALSE
        p20 = re.compile(r'^tag\snative\svlan\s\:\s(?P<tag_native_vlan>\S+)$')

        #num sync messages transmitted  0
        p21 = re.compile(r'^num\ssync\smessages\stransmitted\s+(?P<num_sync_messages_transmitted>\d+)$')

        #num followup messages transmitted  0
        p22 = re.compile(r'^num\sfollowup\smessages\stransmitted\s+(?P<num_followup_messages_transmitted>\d+)$')

        #num sync messages received  8758
        p23 = re.compile(r'^num\ssync\smessages\sreceived\s+(?P<num_sync_messages_received>\d+)$')

        #num followup messages received  8757
        p24 = re.compile(r'^num\sfollowup\smessages\sreceived\s+(?P<num_followup_messages_received>\d+)$')

        #num delay requests transmitted  8753
        p25 = re.compile(r'^num\sdelay\srequests\stransmitted\s+(?P<num_delay_requests_transmitted>\d+)$')

        #num delay responses received 8753
        p26 = re.compile(r'^num\sdelay\sresponses\sreceived\s+(?P<num_delay_responses_received>\d+)$')

        #num delay requests received  0
        p27 = re.compile(r'^num\sdelay\srequests\sreceived\s+(?P<num_delay_requests_received>\d+)$')

        #num delay responses transmitted  0
        p28 = re.compile(r'^num\sdelay\sresponses\stransmitted\s+(?P<num_delay_responses_transmitted>\d+)$')

        # initial return dictionary
        ret_dict ={}
        for line in output.splitlines():
            line = line.strip()

            #Displaying port data for if_id 2a
            #Displaying port data for if_id 29
            m = p1.match(line)
            if m:
                ptp_interface = ret_dict.setdefault('ptp_interface', {})
                ptp_info = ptp_interface.setdefault('ptp_info',{})
                port_info = ptp_interface.setdefault('port_info',{})
                if_id = m.groupdict()['if_id']
                ptp_info['if_id'] = if_id
                continue

            #Port Mac Address 34:ED:1B:7D:F2:A1
            m = p2.match(line)
            if m:
                mac_address = m.groupdict()['mac_address']
                port_info['mac_address'] = mac_address
                continue

            #Port Clock Identity 34:ED:1B:FF:FE:7D:F2:80
            m = p3.match(line)
            if m:
                clock_identity = m.groupdict()['clock_identity']
                port_info['clock_identity'] = clock_identity
                continue

            #Port number 33
            m = p4.match(line)
            if m:
                number = m.groupdict()['number']
                port_info['number'] = int(number)
                continue

            #PTP Version 2
            m = p5.match(line)
            if m:
                version = m.groupdict()['version']
                ptp_info['version'] = int(version)
                continue

            #domain_value 0
            m = p6.match(line)
            if m:
                domain_value = m.groupdict()['domain_value']
                ptp_interface['domain_value'] = int(domain_value)
                continue

            #Profile Type: : DEFAULT
            m = p7.match(line)
            if m:
                profile_type = m.groupdict()['profile_type']
                ptp_interface['profile_type'] = profile_type
                continue

            #Clock Mode : BOUNDARY CLOCK
            m = p8.match(line)
            if m:
                clock_mode = m.groupdict()['clock_mode']
                ptp_interface['clock_mode'] = clock_mode
                continue

            #Delay mechanism: End-to-End
            m = p9.match(line)
            if m:
                delay_mechanism = m.groupdict()['delay_mechanism']
                ptp_interface['delay_mechanism'] = delay_mechanism
                continue

            #port_enabled: TRUE
            m = p10.match(line)
            if m:
                port_enabled = m.groupdict()['port_enabled']
                port_info['port_enabled'] = port_enabled
                continue

            #ptt_port_enabled: TRUE
            m = p11.match(line)
            if m:
                ptt_port_enabled = m.groupdict()['ptt_port_enabled']
                ptp_interface['ptt_port_enabled'] =  ptt_port_enabled
                continue

            #Port state: : SLAVE
            m = p12.match(line)
            if m:
                state = m.groupdict()['state']
                port_info['state'] = state
                continue

            #sync_seq_num 36853
            m = p13.match(line)
            if m:
                sync_seq_num = m.groupdict()['sync_seq_num']
                ptp_interface['sync_seq_num'] = int(sync_seq_num)
                continue

            #delay_req_seq_num 0
            m = p14.match(line)
            if m:
                delay_req_seq_num = m.groupdict()['delay_req_seq_num']
                ptp_interface['delay_req_seq_num'] = int(delay_req_seq_num)
                continue

            #log mean sync interval -3
            m = p15.match(line)
            if m:
                log_mean_sync_interval = m.groupdict()['log_mean_sync_interval']
                ptp_interface['log_mean_sync_interval'] = int(log_mean_sync_interval)
                continue

            #log mean delay interval -5
            m = p16.match(line)
            if m:
                log_mean_delay_interval = m.groupdict()['log_mean_delay_interval']
                ptp_interface['log_mean_delay_interval'] = int(log_mean_delay_interval)
                continue

            #ptp vlan is valid : FALSE
            m = p17.match(line)
            if m:
                ptp_vlan_is_valid = m.groupdict()['ptp_vlan_is_valid']
                ptp_info['ptp_vlan_is_valid'] = ptp_vlan_is_valid
                continue

            #ptp vlan id 0
            m = p18.match(line)
            if m:
                ptp_vlan_id = m.groupdict()['ptp_vlan_id']
                ptp_info['ptp_vlan_id'] = int(ptp_vlan_id)
                continue

            #port mode 2
            m = p19.match(line)
            if m:
                mode = m.groupdict()['mode']
                port_info['mode'] = int(mode)
                continue

            #tag native vlan : FALSE
            m = p20.match(line)
            if m:
                tag_native_vlan = m.groupdict()['tag_native_vlan']
                ptp_interface['tag_native_vlan'] = tag_native_vlan
                continue

            #num sync messages transmitted  17250
            m = p21.match(line)
            if m:
                num_sync_messages_transmitted = m.groupdict()['num_sync_messages_transmitted']
                num_info = ptp_interface.setdefault('num_info',{})
                num_info['num_sync_messages_transmitted'] = int(num_sync_messages_transmitted)
                continue

            #num followup messages transmitted  17250
            m = p22.match(line)
            if m:
                num_followup_messages_transmitted = m.groupdict()['num_followup_messages_transmitted']
                num_info['num_followup_messages_transmitted'] = int(num_followup_messages_transmitted)
                continue

            #num sync messages received  75403
            m = p23.match(line)
            if m:
                num_sync_messages_received = m.groupdict()['num_sync_messages_received']
                num_info['num_sync_messages_received'] = int(num_sync_messages_received)
                continue

            #num followup messages received  75401
            m = p24.match(line)
            if m:
                num_followup_messages_received = m.groupdict()['num_followup_messages_received']
                num_info['num_followup_messages_received'] = int(num_followup_messages_received)
                continue

            #num delay requests transmitted  75941
            m = p25.match(line)
            if m:
                num_delay_requests_transmitted = m.groupdict()['num_delay_requests_transmitted']
                num_info['num_delay_requests_transmitted'] = int(num_delay_requests_transmitted)
                continue

            #num delay responses received 75343
            m = p26.match(line)
            if m:
                num_delay_responses_received = m.groupdict()['num_delay_responses_received']
                num_info['num_delay_responses_received'] = int(num_delay_responses_received)
                continue

            #num delay requests received  17278
            m = p27.match(line)
            if m:
                num_delay_requests_received = m.groupdict()['num_delay_requests_received']
                num_info['num_delay_requests_received'] = int(num_delay_requests_received)
                continue

            #num delay responses transmitted  17278
            m = p28.match(line)
            if m:
                num_delay_responses_transmitted = m.groupdict()['num_delay_responses_transmitted']
                num_info['num_delay_responses_transmitted'] = int(num_delay_responses_transmitted)
                continue
        return ret_dict


# =========================================================
#  Schema for
#  * 'show platform software fed active acl usage'
#  * 'show platform software fed active acl usage | include {acl_name}'
# =========================================================
class ShowPlatformSoftwareFedActiveAclUsageSchema(MetaParser):
    """Schema for 'show platform software fed active acl usage
    """
    schema = {
        Optional('acl_usage'): {
            Optional('ace_software'): {
                 Optional('vmr_max') : int,
                 Optional('used') : int,
             },
            'acl_name': {
                Any(): {
                    'direction': {
                        Any(): {
                            'feature_type': str,
                            'acl_type': str,
                            'entries_used': int,
                        },
                    },
                },
            },
        }
    }

# =========================================================
#  Parser for
#  * 'show platform software fed active acl usage'
#  * 'show platform software fed active acl usage | include {acl_name}'
# =========================================================
class ShowPlatformSoftwareFedActiveAclUsage(ShowPlatformSoftwareFedActiveAclUsageSchema):
    """
    Parser for :
        * show platform software fed active acl usage
        * show platform software fed active acl usage | include {acl_name}
    """

    cli_command = ['show platform software fed active acl usage',
                   'show platform software fed active acl usage | include {acl_name}']

    def cli(self, acl_name="", output=None):
        if output is None:
            if acl_name:
                cmd = self.cli_command[1].format(acl_name=acl_name)
            else:
                cmd = self.cli_command[0]
            output = self.device.execute(cmd)

        ######  ACE Software VMR max:196608 used:253
        p1 = re.compile(r'^\#\#\#\#\#\s+ACE\sSoftware\sVMR\smax\:(?P<vmr_max>\d+)\sused\:(?P<used>\d+)$')


        #   RACL        IPV4     Ingress   PBR-DMVPN    92
        p2 = re.compile(r'^(?P<feature_type>\S+)\s+(?P<acl_type>\S+)\s+(?P<direction>\S+)\s+(?P<name>\S+)\s+(?P<entries_used>\d+)$')

        # initial return dictionary
        ret_dict ={}

        for line in output.splitlines():
            line = line.strip()

            acl_usage = ret_dict.setdefault('acl_usage', {})

            ######  ACE Software VMR max:196608 used:253
            m = p1.match(line)
            if m:
                group = m.groupdict()
                acl_usage = ret_dict.setdefault('acl_usage', {})
                ace_software = acl_usage.setdefault('ace_software',{})

                vmr_max = group['vmr_max']
                ace_software['vmr_max'] = int(vmr_max)

                used = group['used']
                ace_software['used'] = int(used)
                continue

            #   RACL        IPV4     Ingress   PBR-DMVPN    92
            m = p2.match(line)
            if m:
                group = m.groupdict()
                acl_name = acl_usage.setdefault('acl_name', {}).\
                                 setdefault(Common.convert_intf_name(group['name']), {})
                direction = acl_name.setdefault('direction',{}).\
                                 setdefault(Common.convert_intf_name(group['direction']), {})


                direction['feature_type'] = group['feature_type']
                direction['acl_type'] = group['acl_type']
                direction['entries_used'] = int(group['entries_used'])
                continue
        return ret_dict

# ============================================================================
# Schema for 'show platform software fed active inject packet-capture detailed'
# ===========================================================================
class ShowPlatformSoftwareFedActiveInjectPacketCaptureDetailedSchema(MetaParser):
    """ Schema for
            * show platform software fed active inject packet-capture detailed
        """
    schema = {
        'inject_packet_capture': str,
        'buffer_wrapping': str,
        'total_captured': int,
        'capture_capacity': int,
        'capture_filter': str,
        'inject_packet_number': {
            Any():{
                'interface': {
                    'pal': {
                        'iifd': str
                    },
                },
                'metadata': {
                    'cause': str,
                    'sub_cause': str,
                    'q_no': str,
                    'linktype': str
                },
                'ether_hdr_1': {
                    'dest_mac': str,
                    'src_mac': str
                },
                'ether_hdr_2': {
                    'ether_type': str
                },
                'ipv4_hdr_1': {
                    'dest_ip': str,
                    'src_ip': str
                },
                'ipv4_hdr_2': {
                    'packet_len': str,
                    'ttl': str,
                    'protocol': str
                },
                'udp_hdr': {
                    'dest_port': str,
                    'src_port': str
                },
                'doppler_frame_descriptor': {
                    'fdformat': str,
                    'system_ttl': str,
                    'fdtype': str,
                    'span_session_map': str,
                    'qoslabel': str,
                    'fpe_first_header_type': str
                }

            }
        }
    }

# ================================================================
# Parser for:
#   * 'show platform software fed active inject packet-capture detailed'
# ================================================================
class ShowPlatformSoftwareFedActiveInjectPacketCaptureDetailed(
    ShowPlatformSoftwareFedActiveInjectPacketCaptureDetailedSchema):
    """ Parser for:
            show platform software fed active inject packet-capture detailed
    """

    cli_command = ['show platform software fed active inject packet-capture detailed']

    def cli(self, output=None):
        """ cli for:
         ' show platform software fed active inject packet-capture detailed '
        """

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        #Inject packet capturing: disabled. Buffer wrapping: disabled
        p1 = re.compile(r'^Inject +packet +capturing:+\s+(?P<inject_packet_capture>\w+)\.+\s+'
                        r'Buffer +wrapping:\s+(?P<buffer_wrapping>\w+)$')

        #Total captured so far: 4 packets. Capture capacity : 4096 packets
        p2 = re.compile(r'^Total +captured +so +far:\s(?P<total_captured>\d)+\s+packets+\.\s+'
                       r'Capture +capacity +:\s+(?P<capture_capacity>\d+)+\s+packets$')

        #Capture filter : "udp.port == 9995"
        p3 = re.compile(r'^Capture +filter +: +(?P<capture_filter>.+)$')

        #------ Inject Packet Number: 1, Timestamp: 2021/09/15 07:40:40.603 ------
        p4 = re.compile(r'^-+\s+Inject +Packet +Number: +(?P<inject_packet_no>\d+)')

        #interface : pal:  [if-id: 0x00000000]
        p5 = re.compile(r'^interface +: pal: \s+\[+if-id: +(?P<iifd>\S+)$')

        #metadata  : cause: 2 [QFP destination lookup], sub-cause: 1, q-no: 0, linktype: MCP_LINK_TYPE_IP [1]
        p6 = re.compile(r'^metadata +: +cause: +(?P<cause>.+)'
                        r'\s+sub-cause: +(?P<sub_cause>\d+)\, +q-no: +(?P<q_no>\d+)\,'
                        r'\s+linktype: +(?P<linktype>.+)')

        #ether hdr : dest mac: 3c57.3104.6a00, src mac: 3c57.3104.6a00
        p7 = re.compile(r'^ether +hdr +: +dest +mac: +(?P<dest_mac>\S+)\s+src +mac: +(?P<src_mac>\S+)')

        #ether hdr : ethertype: 0x0800 (IPv4)
        p8 = re.compile(r'^ether +hdr +: +ethertype: +(?P<ether_type>.+)$')

        #ipv4  hdr : dest ip: 111.0.0.2, src ip: 111.0.0.1
        p9 = re.compile(r'^ipv4 +hdr +: +dest +ip: +(?P<dest_ip>\S+)\s+src +ip: +(?P<src_ip>\S+)')

        #ipv4  hdr : packet len: 188, ttl: 255, protocol: 17 (UDP)
        p10 = re.compile(r'^ipv4 +hdr +: +packet +len: +(?P<packet_len>\d+)\,\s+ttl: +(?P<ttl>\d+)'
                         r'\,+\s+protocol: +(?P<protocol>.+)$')

        #udp   hdr : dest port: 9995, src port: 53926
        p11 = re.compile(r'^udp +hdr +: +dest +port: +(?P<dest_port>\d+)\,\s+src +port: +(?P<src_port>\d+)')

        #Doppler Frame Descriptor :
        p12 = re.compile(r'^Doppler +Frame +Descriptor +:(?P<doppler_frame_descriptor>)$')

        #fdFormat                  = 0x3            systemTtl                 = 0x8
        p13 = re.compile(r'^fdFormat\s+\= (?P<fdformat>\S+)\s+systemTtl\s+\= (?P<system_ttl>\S+$)')

        #fdType                    = 0x1            spanSessionMap            = 0
        p14 = re.compile(r'^fdType\s+\= (?P<fdtype>\S+)\s+spanSessionMap\s+\= (?P<span_session_map>\S+$)')

        #qosLabel                  = 0x81           fpeFirstHeaderType        = 0
        p15 = re.compile(r'^qosLabel\s+\= (?P<qoslabel>\S+)\s+fpeFirstHeaderType\s+\= (?P<fpe_first_header_type>\S+$)')

        ret_dict = {}
        for line in out.splitlines():
            line = line.strip()

            # Inject packet capturing: disabled. Buffer wrapping: disabled
            m = p1.match(line)
            if m:
                ret_dict.update({
                    'inject_packet_capture': m.groupdict()['inject_packet_capture'],
                    'buffer_wrapping': m.groupdict()['buffer_wrapping']
                })
                continue

            # Total captured so far: 4 packets. Capture capacity : 4096 packets
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({
                    'total_captured':int(group['total_captured']),
                    'capture_capacity':int(group['capture_capacity'])
                })
                continue

            # Capture filter : "udp.port == 9995"
            m = p3.match(line)
            if m:
                ret_dict.update({'capture_filter': m.groupdict()['capture_filter']})
                continue

            # ------ Inject Packet Number: 1, Timestamp: 2021/09/15 07:40:40.603 ------
            m = p4.match(line)
            if m:
                group = m.groupdict()
                inject_packet_num = group['inject_packet_no']
                inject_packet_dict = ret_dict.setdefault('inject_packet_number', {}).setdefault(inject_packet_num, {})
                continue

            # interface : pal:  [if-id: 0x00000000]
            m = p5.match(line)
            if m:
                group = m.groupdict()
                int_dict = ret_dict['inject_packet_number'][inject_packet_num].setdefault('interface', {})
                pal_dict = ret_dict['inject_packet_number'][inject_packet_num]['interface'].setdefault('pal',{})
                pal_dict['iifd'] = group['iifd']
                continue

            # metadata  : cause: 2 [QFP destination lookup], sub-cause: 1, q-no: 0, linktype: MCP_LINK_TYPE_IP [1]
            m = p6.match(line)
            if m:
                group = m.groupdict()
                meta_data_dict = ret_dict['inject_packet_number'][inject_packet_num].setdefault('metadata',{})
                meta_data_dict['cause'] = group['cause']
                meta_data_dict['sub_cause'] = group['sub_cause']
                meta_data_dict['q_no'] = group['q_no']
                meta_data_dict['linktype'] = group['linktype']
                continue

            # ether hdr : dest mac: 3c57.3104.6a00, src mac: 3c57.3104.6a00
            m = p7.match(line)
            if m:
                group = m.groupdict()
                ether_hdr_1_dict = ret_dict['inject_packet_number'][inject_packet_num].setdefault('ether_hdr_1',{})
                ether_hdr_1_dict['dest_mac'] = group['dest_mac']
                ether_hdr_1_dict['src_mac'] = group['src_mac']
                continue

            # ether hdr : ethertype: 0x0800 (IPv4)
            m = p8.match(line)
            if m:
                group = m.groupdict()
                ether_hdr_2_dict = ret_dict['inject_packet_number'][inject_packet_num].setdefault('ether_hdr_2',{})
                ether_hdr_2_dict['ether_type'] = group['ether_type']
                continue

            # ipv4  hdr : dest ip: 111.0.0.2, src ip: 111.0.0.1
            m = p9.match(line)
            if m:
                group = m.groupdict()
                ipv4_hdr_1_dict = ret_dict['inject_packet_number'][inject_packet_num].setdefault('ipv4_hdr_1',{})
                ipv4_hdr_1_dict['dest_ip'] = group['dest_ip']
                ipv4_hdr_1_dict['src_ip'] = group['src_ip']
                continue

            # ipv4  hdr : packet len: 188, ttl: 255, protocol: 17 (UDP)
            m = p10.match(line)
            if m:
                group = m.groupdict()
                ipv4_hdr_2_dict = ret_dict['inject_packet_number'][inject_packet_num].setdefault('ipv4_hdr_2',{})
                ipv4_hdr_2_dict['packet_len'] = group['packet_len']
                ipv4_hdr_2_dict['ttl'] = group['ttl']
                ipv4_hdr_2_dict['protocol'] = group['protocol']
                continue

            # udp   hdr : dest port: 9995, src port: 53926
            m = p11.match(line)
            if m:
                group = m.groupdict()
                udp_hdr_dict = ret_dict['inject_packet_number'][inject_packet_num].setdefault('udp_hdr',{})
                udp_hdr_dict['dest_port'] = group['dest_port']
                udp_hdr_dict['src_port'] = group['src_port']
                continue

            # Doppler Frame Descriptor :
            m = p12.match(line)
            if m:
                group = m.groupdict()
                doppler_frame_des_dict = ret_dict['inject_packet_number'][inject_packet_num].setdefault(
                    'doppler_frame_descriptor',{})
                continue

            # fdFormat                  = 0x3            systemTtl                 = 0x8
            m = p13.match(line)
            if m:
                group = m.groupdict()
                doppler_frame_des_dict['fdformat'] = group['fdformat']
                doppler_frame_des_dict['system_ttl'] = group['system_ttl']
                continue

            # fdType                    = 0x1            spanSessionMap            = 0
            m = p14.match(line)
            if m:
                group = m.groupdict()
                doppler_frame_des_dict['fdtype'] = group['fdtype']
                doppler_frame_des_dict['span_session_map'] = group['span_session_map']
                continue

            # qosLabel                  = 0x81           fpeFirstHeaderType        = 0
            m = p15.match(line)
            if m:
                group = m.groupdict()
                doppler_frame_des_dict['qoslabel'] = group['qoslabel']
                doppler_frame_des_dict['fpe_first_header_type'] = group['fpe_first_header_type']
                continue

        return ret_dict

 # ===============================================================================
# Schema for 'show platform software dpidb index'
# ===============================================================================
class ShowPlatformSoftwareDpidIndexSchema(MetaParser):
    """Schema for :
        show platform software dpidb index"""

    schema = {
        Any(): {
            'index' : int,
        },
    }

# ===============================================================================
# Parser for 'show platform software dpidb index'
# ===============================================================================
class ShowPlatformSoftwareDpidIndex(ShowPlatformSoftwareDpidIndexSchema):
    """parser for :
        show platform software dpidb index"""

    cli_command = 'show platform software dpidb index'

    def cli(self, output=None,):

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        result_dict = {}
        #Index 1030 -- swidb Hu1/0/1
        p1 = re.compile(r'^Index\s+(?P<index>\d+)\s+--\s+swidb\s+(?P<interface>\S+)$')

        for line in out.splitlines():
            line = line.strip()
            #Index 1030 -- swidb Hu1/0/1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                interface = group.pop('interface')
                interface_dict = result_dict.setdefault(interface,{})
                interface_dict.update({
                    'index' : int(group['index']),
                })
                continue

        return result_dict

# ==================================================================================
# Parser for 'show platform hardware qfp active feature sdwan datapath fec global" #
# ==================================================================================
class ShowPlatformHardwareQfpActiveFeatureSdwanDpFecGlobalSchema(MetaParser):
    schema = {
        Any(): { # FEC Global Info
            "ses_chunk_head": int,
            "pak_chunk_head": int,
            "ses_add": int,
            "ses_del": int,
            "ses_alloc_fail": int,
            "ses_mem_req": int,
            "ses_mem_req_resp": int,
            "ses_mem_ret": int,
            "pkt_alloc": int,
            "pkt_free": int,
            "pkt_alloc_fail": int,
            "pak_mem_req": int,
            "pak_mem_req_resp": int,
            "pak_mem_ret": int,
            "win_seq_err": int,
            "mem_to_pkt_err": int,
            "fec_encap_err": int,
            "fec_decap_err": int,
            "fec_compute_err": int,
            "reconstruct_miss": int,
            "fec_recycle_err": int,
            "data_recycle_err": int
        }
    }

class ShowPlatformHardwareQfpActiveFeatureSdwanDpFecGlobal(ShowPlatformHardwareQfpActiveFeatureSdwanDpFecGlobalSchema):

    cli_command = 'show platform hardware qfp active feature sdwan datapath fec global'
    def cli(self, output=None):

        # if the user does not provide output to the parser
        # we need to get it from the device
        if output is None:
            output = self.device.execute(self.cli_command)

        # FEC Global Info
        p1 = re.compile(r'^(?P<key>[A-Za-z\s]+)$')

        # "ses_chunk_head": int
        # "pak_chunk_head": int
        p2 = re.compile(r'^(?P<key>[a-z\_]+)\s+:\s+(?P<value>[\d\D]+)')

        ret_dict = {}
        for line in output.splitlines():
            line = line.strip()
            # FEC Global Info
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                key = groups['key'].replace('-', '_').replace(' ', '_').replace(':', '').lower()
                fec_dict = ret_dict.setdefault(key, {})
                continue
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                key = groups['key']
                value = int(groups['value'],16)
                fec_dict.update({key:value})
                continue

        return ret_dict

# ===========================================================================================
# Parser for 'show platform hardware qfp active feature sdwan datapath fec session summary' #
# ===========================================================================================
class ShowPlatformHardwareQfpActiveFeatureSdwanDpFecSessionSummarySchema(MetaParser):
    schema = {
        'tunnel': {
            str: {
                'flags' : str,
                'tx_data' : int,
                'tx_parity' : int,
                'rx_data' : int,
                'rx_parity' : int,
                'reconstruct' : int,
                Optional('tx_rx_wins') : {
                    str : {
                        'win_flags' : str,
                        'count' : int,
                        'isn' : int,
                        'tos' : int,
                        'parity_len' : int,
                        'fec_len' : int,
                        'fec_data' : str
                    }
                }
            }
        }
    }

class ShowPlatformHardwareQfpActiveFeatureSdwanDpFecSessionSummary(ShowPlatformHardwareQfpActiveFeatureSdwanDpFecSessionSummarySchema):

    cli_command = 'show platform hardware qfp active feature sdwan datapath fec session summary'
    def cli(self, output=None):
        # if the user does not provide output to the parser
        # we need to get it from the device
        if output is None:
            output = self.device.execute(self.cli_command)

        # 12345     0x123    100        2       200         3          1
        p1 = re.compile(r'^(?P<index>[\S]+)\s+(?P<flags>[\S]+)\s+(?P<tx_data>[\d]+)\s+(?P<tx_parity>[\d]+)\s+(?P<rx_data>[\d]+)\s+(?P<rx_parity>[\d]+)\s+(?P<reconstruct>[\d]+)$')

        # 0     0X2     1     219329664 0     92        56        0xC85EAD30
        p2 = re.compile(r'^(?P<win_num>[\d]+)\s+(?P<win_flags>[\S]+)\s+(?P<count>[\d]+)\s+(?P<isn>[\d]+)\s+(?P<tos>[\d]+)\s+(?P<parity_len>[\d]+)\s+(?P<fec_len>[\d]+)\s+(?P<fec_data>[\S]+)$')

        ret_dict = {}
        for line in output.splitlines():
            line = line.strip()
            # 12345     0x123    100        2       200         3          1
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                index_dict = ret_dict.setdefault("tunnel", {}).setdefault(groups["index"],{})
                del groups["index"]
                for key in groups.keys():
                    value = groups[key]
                    # Check is Mandatory as i am iterations through different key/values pairs
                    # of different types.
                    if groups[key].isnumeric():
                        value = int(groups[key])
                    index_dict.update({key:value})
                continue
            # 0     0X2     1     219329664 0     92        56        0xC85EAD30
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                wins_dict = index_dict.setdefault("tx_rx_wins",{})
                win_num_dict = wins_dict.setdefault(groups["win_num"],{})
                del groups["win_num"]
                for key in groups.keys():
                    value = groups[key]
                    # Check is Mandatory as i am iterations through different key/values pairs
                    # of different types.
                    if groups[key].isnumeric():
                        value = int(groups[key])
                    win_num_dict.update({key:value})
                continue

        return ret_dict

# =============================================================================
#  Schema for
#  * 'show platform software fed switch active ifm mappings lpn'
#  * 'show platform software fed switch active ifm mappings lpn | {interface}'
# ==============================================================================
class ShowPlatformSoftwareFedSwitchActiveIfmMappingsLpnSchema(MetaParser):
    """Schema for 'show platform software fed switch active ifm mappings lpn'
    """
    schema = {
        'interfaces':{
            Any(): {
                'lpn': int,
                'asic': int,
                'port': int,
                'if_id': str,
                'active': str
            }
        },
    }

# ===============================================================================
#  Parser for
#  * 'show platform software fed switch active ifm mappings lpn'
#  * 'show platform software fed switch active ifm mappings lpn | i {interface}'
# ================================================================================
class ShowPlatformSoftwareFedSwitchActiveIfmMappingsLpn(ShowPlatformSoftwareFedSwitchActiveIfmMappingsLpnSchema):
    """
    Parser for :
        * show platform software fed switch active ifm mappings lpn
    """

    cli_command = ['show platform software fed switch active ifm mappings lpn',
                   'show platform software fed switch active ifm mappings lpn | include {interface}']

    def cli(self, interface="", output=None):
        if output is None:
            if interface:
                cmd = self.cli_command[1].format(interface=interface)
            else:
                cmd = self.cli_command[0]
            output = self.device.execute(cmd)

        #19   1     18    TenGigabitEthernet1/0/19   0x0000001b  y
        p = re.compile(r'^(?P<lpn>\d+)\s+(?P<asic>\d+)\s+(?P<port>\d+)\s+(?P<interfaces>\S+)\s+(?P<if_id>(0x([\da-fA-F]){8}))\s+(?P<active>\S+)$')

        # initial return dictionary
        ret_dict ={}

        for line in output.splitlines():
            line = line.strip()

            #19    1  18    TenGigabitEthernet1/0/19   0x0000001b  y
            m = p.match(line)
            if m:

                group = m.groupdict()
                interfaces = group['interfaces']
                sub_dict = ret_dict.setdefault('interfaces', {}).setdefault(interfaces, {})

                lpn = group['lpn']
                sub_dict['lpn'] = int(lpn)

                asic = group['asic']
                sub_dict['asic'] = int(asic)

                port = group['port']
                sub_dict['port'] = int(port)

                if_id = group['if_id']
                sub_dict['if_id'] = if_id

                active = group['active']
                sub_dict['active'] = active
                continue
        return ret_dict


# =================================================================
#  Schema for 'show platform software fed switch active ptp domain
# ================================================================
class ShowPlatformSoftwareFedSwitchActivePtpDomainSchema(MetaParser):
    """Schema for 'show platform software fed switch active ptp domain
    """
    schema = {
        'domain_number': {
            Any(): {
                'profile_type': str,
                'profile_state': str,
                Optional('clock_mode'): str,
                Optional('delay_mechanism'): str,
                Optional('ptp_clock'): str,
                Optional('mean_path_delay_ns'): int,
                'transport_method': str,
                'message_general_ip_dscp': int,
                'message_event_ip_dscp': int
            }
        },
    }
# =================================================================
#  Parser for 'show platform software fed switch active ptp domain
# ================================================================
class ShowPlatformSoftwareFedSwitchActivePtpDomain(ShowPlatformSoftwareFedSwitchActivePtpDomainSchema):
    """
    Parser for :
        * show platform software fed switch active ptp domain
    """

    cli_command = 'show platform software fed switch active ptp domain'

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)

        #Displaying data for domain number 0
        p1 = re.compile(r'^Displaying\sdata\sfor\sdomain\snumber\s(?P<domain_number>\d+)$')

        #Profile Type : DEFAULT
        p2 = re.compile(r'^Profile\sType\s\:\s(?P<profile_type>[a-zA-Z]+)$')

        #Profile State: enabled
        p3 = re.compile(r'^Profile\sState\:\s(?P<profile_state>\S+)$')

        #Clock Mode : BOUNDARY CLOCK
        p4 = re.compile(r'^Clock\sMode\s\:\s(?P<clock_mode>[A-Z\s]+)$')

        #Delay Mechanism: : END-TO-END
        p5 = re.compile(r'^Delay\sMechanism\:\s\:\s(?P<delay_mechanism>[A-Z\-]+)$')

        #PTP clock : 1970-1-24 22:41:20
        p6 = re.compile(r'^PTP\sclock\s\:\s(?P<ptp_clock>[\d\-\:\s]+)$')

        #mean_path_delay 83 nanoseconds
        p7 = re.compile(r'^mean_path_delay\s(?P<mean_path_delay_ns>\d+)\snanoseconds$')

        #Transport Method : 802.3
        p8 = re.compile(r'^Transport\sMethod\s\:\s(?P<transport_method>[\w\.\-]+)$')

        #Message general ip dscp  : 47
        p9 = re.compile(r'^Message\sgeneral\sip\sdscp\s+\:\s(?P<message_general_ip_dscp>\d+)$')

        #Message event ip dscp    : 59
        p10 = re.compile(r'^Message\sevent\sip\sdscp\s+\:\s(?P<message_event_ip_dscp>\d+)$')

        # initial return dictionary
        ret_dict ={}

        for line in output.splitlines():
            line = line.strip()

            #Displaying data for domain number 0
            m = p1.match(line)
            if m:
                ret_dict.setdefault('domain_number',{})
                domain_number = m.groupdict()['domain_number']
                sub_dict = ret_dict['domain_number'].setdefault(int(domain_number),{})
                continue

            #Profile Type : DEFAULT
            m = p2.match(line)
            if m:
                profile_type = m.groupdict()['profile_type']
                sub_dict['profile_type'] = profile_type
                continue

            #Profile State: enabled
            m = p3.match(line)
            if m:
                profile_state = m.groupdict()['profile_state']
                sub_dict['profile_state'] = profile_state
                continue

            #Clock Mode : BOUNDARY CLOCK
            m = p4.match(line)
            if m:
                clock_mode = m.groupdict()['clock_mode']
                sub_dict['clock_mode'] = clock_mode
                continue

            #Delay Mechanism: : END-TO-END
            m = p5.match(line)
            if m:
                delay_mechanism  = m.groupdict()['delay_mechanism']
                sub_dict['delay_mechanism'] = delay_mechanism
                continue

            #PTP clock : 1970-1-24 22:41:20
            m = p6.match(line)
            if m:
                ptp_clock = m.groupdict()['ptp_clock']
                sub_dict['ptp_clock'] = ptp_clock
                continue

            #mean_path_delay 83 nanoseconds
            m = p7.match(line)
            if m:
                mean_path_delay_ns = m.groupdict()['mean_path_delay_ns']
                sub_dict['mean_path_delay_ns'] = int(mean_path_delay_ns)
                continue

            #Transport Method : 802.3
            m = p8.match(line)
            if m:
                transport_method = m.groupdict()['transport_method']
                sub_dict['transport_method'] = transport_method
                continue

            #Message general ip dscp  : 47
            m = p9.match(line)
            if m:
                message_general_ip_dscp = m.groupdict()['message_general_ip_dscp']
                sub_dict['message_general_ip_dscp'] = int(message_general_ip_dscp)
                continue

            #Message event ip dscp    : 59
            m = p10.match(line)
            if m:
                message_event_ip_dscp = m.groupdict()['message_event_ip_dscp']
                sub_dict['message_event_ip_dscp'] = int(message_event_ip_dscp)
                continue
        return ret_dict

# ================================================================================
#  Schema for 'show platform software fed switch active ptp interface {interface}'
# ================================================================================
class ShowPlatformSoftwareFedSwitchActivePtpInterfaceInterfaceSchema(MetaParser):
    """Schema for 'show platform software fed switch active ptp interface {interface}'
    """

    schema = {
        'interface': {
            'ptp_info': {
                'version': int,
                Optional('ptp_vlan_is_valid'): str,
                Optional('ptp_vlan_id'): int,
            },
            'port_info': {
                'mac_address': str,
                'clock_identity': str,
                'number': int,
                Optional('mode'): int,
                'state': str,
                'port_enabled': str
            },
            'num_info': {
                'num_sync_messages_transmitted': int,
                'num_followup_messages_transmitted': int,
                'num_sync_messages_received': int,
                'num_followup_messages_received': int,
                Optional('num_delay_requests_transmitted'): int,
                Optional('num_delay_responses_received'): int,
                Optional('num_delay_requests_received'): int,
                Optional('num_delay_responses_transmitted'): int
            },
            'if_id': str,
            'domain_value': int,
            'profile_type': str,
            'clock_mode': str,
            'delay_mechanism': str,
            'ptt_port_enabled': str,
            'sync_seq_num': int,
            'delay_req_seq_num': int,
            Optional('log_mean_sync_interval'): int,
            Optional('log_mean_delay_interval'): int,
            Optional('tag_native_vlan'): str,
        }
    }

# =================================================================================
#  Parser for 'show platform software fed switch active ptp interface {interface}'
# =================================================================================
class ShowPlatformSoftwareFedSwitchActivePtpInterfaceInterface(ShowPlatformSoftwareFedSwitchActivePtpInterfaceInterfaceSchema):
    """
    Parser for :
        * show platform software fed switch active ptp interface {interface}
    """

    cli_command = 'show platform software fed switch active ptp interface {interface}'

    def cli(self, interface="", output=None):

        if output is None:
            output = self.device.execute(self.cli_command.format(interface=interface))

        #Displaying port data for if_id 2a
        #Displaying port data for if_id 29
        p1 = re.compile(r'^Displaying\sport\sdata\sfor\sif_id\s(?P<if_id>[0-9a-fA-F]+)$')

        #Port Mac Address 34:ED:1B:7D:F2:A1
        p2 = re.compile(r'^Port\sMac\sAddress\s(?P<mac_address>([\da-fA-F]:?).*)$')

        #Port Clock Identity 34:ED:1B:FF:FE:7D:F2:80
        p3 = re.compile(r'^Port\sClock\sIdentity\s(?P<clock_identity>([\da-fA-F]:?).*)$')

        #Port number 33
        p4 = re.compile(r'^Port\snumber\s(?P<number>\d+)$')

        #PTP Version 2
        p5 = re.compile(r'^PTP\sVersion\s(?P<version>\d+)$')

        #domain_value 0
        p6 = re.compile(r'^domain_value\s(?P<domain_value>\d+)$')

        #Profile Type: : DEFAULT
        p7 = re.compile(r'^Profile\sType\:\s\:\s(?P<profile_type>\S+)$')

        #Clock Mode : BOUNDARY CLOCK
        p8 = re.compile(r'^Clock\sMode\s\:\s(?P<clock_mode>.*)$')

        #Delay mechanism: End-to-End
        p9 = re.compile(r'^Delay\smechanism\:\s(?P<delay_mechanism>\S+)$')

        #port_enabled: TRUE
        p10 = re.compile(r'^port_enabled\:\s(?P<port_enabled>\S+)$')

        #ptt_port_enabled: TRUE
        p11 = re.compile(r'^ptt_port_enabled\:\s(?P<ptt_port_enabled>\S+)$')

        #Port state: : SLAVE
        p12 = re.compile(r'^Port\sstate\:\s\:\s(?P<state>\S+)$')

        #sync_seq_num 2189
        p13 = re.compile(r'^sync_seq_num\s(?P<sync_seq_num>\d+)$')

        #delay_req_seq_num 0
        p14 = re.compile(r'^delay_req_seq_num\s(?P<delay_req_seq_num>\d+)$')

        #log mean sync interval -3
        p15 = re.compile(r'^log\smean\ssync\sinterval\s(?P<log_mean_sync_interval>[-?\d]+)$')

        #log mean delay interval -5
        p16 = re.compile(r'^log\smean\sdelay\sinterval\s(?P<log_mean_delay_interval>[-?\d]+)$')

        #ptp vlan is valid : FALSE
        p17 = re.compile(r'^ptp\svlan\sis\svalid\s\:\s(?P<ptp_vlan_is_valid>\S+)$')

        #ptp vlan id 0
        p18 = re.compile(r'^ptp\svlan\sid\s(?P<ptp_vlan_id>\d+)$')

        #port mode 2
        p19 = re.compile(r'^port\smode\s(?P<mode>\d+)$')

        #tag native vlan : FALSE
        p20 = re.compile(r'^tag\snative\svlan\s\:\s(?P<tag_native_vlan>\S+)$')

        #num sync messages transmitted  0
        p21 = re.compile(r'^num\ssync\smessages\stransmitted\s+(?P<num_sync_messages_transmitted>\d+)$')

        #num followup messages transmitted  0
        p22 = re.compile(r'^num\sfollowup\smessages\stransmitted\s+(?P<num_followup_messages_transmitted>\d+)$')

        #num sync messages received  8758
        p23 = re.compile(r'^num\ssync\smessages\sreceived\s+(?P<num_sync_messages_received>\d+)$')

        #num followup messages received  8757
        p24 = re.compile(r'^num\sfollowup\smessages\sreceived\s+(?P<num_followup_messages_received>\d+)$')

        #num delay requests transmitted  8753
        p25 = re.compile(r'^num\sdelay\srequests\stransmitted\s+(?P<num_delay_requests_transmitted>\d+)$')

        #num delay responses received 8753
        p26 = re.compile(r'^num\sdelay\sresponses\sreceived\s+(?P<num_delay_responses_received>\d+)$')

        #num delay requests received  0
        p27 = re.compile(r'^num\sdelay\srequests\sreceived\s+(?P<num_delay_requests_received>\d+)$')

        #num delay responses transmitted  0
        p28 = re.compile(r'^num\sdelay\sresponses\stransmitted\s+(?P<num_delay_responses_transmitted>\d+)$')

        # initial return dictionary
        ret_dict ={}
        for line in output.splitlines():
            line = line.strip()

            #Displaying port data for if_id 2a
            #Displaying port data for if_id 29
            m = p1.match(line)
            if m:            
                group = m.groupdict()
                sub_dict = ret_dict.setdefault('interface', {})
                sub_dict['if_id'] = group['if_id']
                ptp_info = sub_dict.setdefault('ptp_info',{})
                port_info = sub_dict.setdefault('port_info',{})
                continue

            #Port Mac Address 34:ED:1B:7D:F2:A1
            m = p2.match(line)
            if m:
                mac_address = m.groupdict()['mac_address']
                port_info['mac_address'] = mac_address
                continue

            #Port Clock Identity 34:ED:1B:FF:FE:7D:F2:80
            m = p3.match(line)
            if m:
                clock_identity = m.groupdict()['clock_identity']
                port_info['clock_identity'] = clock_identity
                continue

            #Port number 33
            m = p4.match(line)
            if m:
                number = m.groupdict()['number']
                port_info['number'] = int(number)
                continue

            #PTP Version 2
            m = p5.match(line)
            if m:
                version = m.groupdict()['version']
                ptp_info['version'] = int(version)
                continue

            #domain_value 0
            m = p6.match(line)
            if m:
                domain_value = m.groupdict()['domain_value']
                sub_dict['domain_value'] = int(domain_value)
                continue

            #Profile Type: : DEFAULT
            m = p7.match(line)
            if m:
                profile_type = m.groupdict()['profile_type']
                sub_dict['profile_type'] = profile_type
                continue

            #Clock Mode : BOUNDARY CLOCK
            m = p8.match(line)
            if m:
                clock_mode = m.groupdict()['clock_mode']
                sub_dict['clock_mode'] = clock_mode
                continue

            #Delay mechanism: End-to-End
            m = p9.match(line)
            if m:
                delay_mechanism = m.groupdict()['delay_mechanism']
                sub_dict['delay_mechanism'] = delay_mechanism 
                continue

            #port_enabled: TRUE
            m = p10.match(line)
            if m:
                port_enabled = m.groupdict()['port_enabled']
                port_info['port_enabled'] = port_enabled
                continue

            #ptt_port_enabled: TRUE
            m = p11.match(line)
            if m:
                ptt_port_enabled = m.groupdict()['ptt_port_enabled']
                sub_dict['ptt_port_enabled'] =  ptt_port_enabled
                continue

            #Port state: : SLAVE
            m = p12.match(line)
            if m:
                state = m.groupdict()['state']
                port_info['state'] = state
                continue

            #sync_seq_num 36853
            m = p13.match(line)
            if m:
                sync_seq_num = m.groupdict()['sync_seq_num']
                sub_dict['sync_seq_num'] = int(sync_seq_num)
                continue

            #delay_req_seq_num 0
            m = p14.match(line)
            if m:
                delay_req_seq_num = m.groupdict()['delay_req_seq_num']
                sub_dict['delay_req_seq_num'] = int(delay_req_seq_num)
                continue

            #log mean sync interval -3
            m = p15.match(line)
            if m:
                log_mean_sync_interval = m.groupdict()['log_mean_sync_interval']
                sub_dict['log_mean_sync_interval'] = int(log_mean_sync_interval)
                continue

            #log mean delay interval -5
            m = p16.match(line)
            if m:
                log_mean_delay_interval = m.groupdict()['log_mean_delay_interval']
                sub_dict['log_mean_delay_interval'] = int(log_mean_delay_interval)
                continue

            #ptp vlan is valid : FALSE
            m = p17.match(line)
            if m:
                ptp_vlan_is_valid = m.groupdict()['ptp_vlan_is_valid']
                ptp_info['ptp_vlan_is_valid'] = ptp_vlan_is_valid
                continue

            #ptp vlan id 0
            m = p18.match(line)
            if m:
                ptp_vlan_id = m.groupdict()['ptp_vlan_id']
                ptp_info['ptp_vlan_id'] = int(ptp_vlan_id)
                continue

            #port mode 2
            m = p19.match(line)
            if m:
                mode = m.groupdict()['mode']
                port_info['mode'] = int(mode)
                continue

            #tag native vlan : FALSE
            m = p20.match(line)
            if m:
                tag_native_vlan = m.groupdict()['tag_native_vlan']
                sub_dict['tag_native_vlan'] = tag_native_vlan
                continue

            #num sync messages transmitted  17250
            m = p21.match(line)
            if m:
                num_sync_messages_transmitted = m.groupdict()['num_sync_messages_transmitted']
                num_info = sub_dict.setdefault('num_info',{})
                num_info['num_sync_messages_transmitted'] = int(num_sync_messages_transmitted)
                continue

            #num followup messages transmitted  17250
            m = p22.match(line)
            if m:
                num_followup_messages_transmitted = m.groupdict()['num_followup_messages_transmitted']
                num_info['num_followup_messages_transmitted'] = int(num_followup_messages_transmitted)
                continue

            #num sync messages received  75403
            m = p23.match(line)
            if m:
                num_sync_messages_received = m.groupdict()['num_sync_messages_received']
                num_info['num_sync_messages_received'] = int(num_sync_messages_received)
                continue

            #num followup messages received  75401
            m = p24.match(line)
            if m:
                num_followup_messages_received = m.groupdict()['num_followup_messages_received']
                num_info['num_followup_messages_received'] = int(num_followup_messages_received)
                continue

            #num delay requests transmitted  75941
            m = p25.match(line)
            if m:
                num_delay_requests_transmitted = m.groupdict()['num_delay_requests_transmitted']
                num_info['num_delay_requests_transmitted'] = int(num_delay_requests_transmitted)
                continue

            #num delay responses received 75343
            m = p26.match(line)
            if m:
                num_delay_responses_received = m.groupdict()['num_delay_responses_received']
                num_info['num_delay_responses_received'] = int(num_delay_responses_received)
                continue

            #num delay requests received  17278
            m = p27.match(line)
            if m:
                num_delay_requests_received = m.groupdict()['num_delay_requests_received']
                num_info['num_delay_requests_received'] = int(num_delay_requests_received)
                continue

            #num delay responses transmitted  17278
            m = p28.match(line)
            if m:
                num_delay_responses_transmitted = m.groupdict()['num_delay_responses_transmitted']
                num_info['num_delay_responses_transmitted'] = int(num_delay_responses_transmitted)
                continue
        return ret_dict


# =========================================================
#  Schema for
#  * 'show platform software fed active acl usage'
#  * 'show platform software fed active acl usage | include {acl_name}'
# =========================================================
class ShowPlatformSoftwareFedActiveAclUsageSchema(MetaParser):
    """Schema for 'show platform software fed active acl usage
    """
    schema = {
        Optional('acl_usage'): {
            Optional('ace_software'): {
                 Optional('vmr_max') : int,
                 Optional('used') : int,
             },
            'acl_name': {
                Any(): {
                    'direction': {
                        Any(): {
                            'feature_type': str,
                            'acl_type': str,
                            'entries_used': int,
                        },
                    },
                },
            },
        }
    }

# =========================================================
#  Parser for
#  * 'show platform software fed active acl usage'
#  * 'show platform software fed active acl usage | include {acl_name}'
# =========================================================
class ShowPlatformSoftwareFedActiveAclUsage(ShowPlatformSoftwareFedActiveAclUsageSchema):
    """
    Parser for :
        * show platform software fed active acl usage
        * show platform software fed active acl usage | include {acl_name}
    """

    cli_command = ['show platform software fed active acl usage',
                   'show platform software fed active acl usage | include {acl_name}']

    def cli(self, acl_name="", output=None):
        if output is None:
            if acl_name:
                cmd = self.cli_command[1].format(acl_name=acl_name)
            else:
                cmd = self.cli_command[0]
            output = self.device.execute(cmd)

        ######  ACE Software VMR max:196608 used:253
        p1 = re.compile(r'^\#\#\#\#\#\s+ACE\sSoftware\sVMR\smax\:(?P<vmr_max>\d+)\sused\:(?P<used>\d+)$')


        #   RACL        IPV4     Ingress   PBR-DMVPN    92
        p2 = re.compile(r'^(?P<feature_type>\S+)\s+(?P<acl_type>\S+)\s+(?P<direction>\S+)\s+(?P<name>\S+)\s+(?P<entries_used>\d+)$')

        # initial return dictionary
        ret_dict ={}

        for line in output.splitlines():
            line = line.strip()

            acl_usage = ret_dict.setdefault('acl_usage', {})

            ######  ACE Software VMR max:196608 used:253
            m = p1.match(line)
            if m:
                group = m.groupdict()
                acl_usage = ret_dict.setdefault('acl_usage', {})
                ace_software = acl_usage.setdefault('ace_software',{})

                vmr_max = group['vmr_max']
                ace_software['vmr_max'] = int(vmr_max)

                used = group['used']
                ace_software['used'] = int(used)
                continue

            #   RACL        IPV4     Ingress   PBR-DMVPN    92
            m = p2.match(line)
            if m:
                group = m.groupdict()
                acl_name = acl_usage.setdefault('acl_name', {}).\
                                 setdefault(Common.convert_intf_name(group['name']), {})
                direction = acl_name.setdefault('direction',{}).\
                                 setdefault(Common.convert_intf_name(group['direction']), {})

                direction['feature_type'] = group['feature_type']
                direction['acl_type'] = group['acl_type']
                direction['entries_used'] = int(group['entries_used'])
                continue
        return ret_dict

class ShowPlatformSoftwareFedQosPolicyTargetSchema(MetaParser):
    ''' search for
        * show platform software fed active qos policy target brief
    '''

    schema = {
        'tcg_sum_for_policy': {
            Any(): {
                'interface': {
                    Any(): {
                        'loc': str,
                        'iif_id': str,
                        'direction': str,
                        'tccg': int,
                        'child': int,
                        'mpq': str,
                        'state_cfg': str,
                        'state_opr': str,
                        'address': str
                    },
                }
            },
        }
    }

class ShowPlatformSoftwareFedQosPolicyTarget(ShowPlatformSoftwareFedQosPolicyTargetSchema):
    ''' parser for
            * show platform software fed active qos policy target brief
    '''

    cli_command = 'show platform software fed active qos policy target brief'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute('show platform software fed active qos policy target brief')
        else:
            out = output

        ret_dict = {}

        # TCG summary for policy: system-cpp-policy
        p1 = re.compile(r'TCG\ssummary\sfor\spolicy:\s+(?P<policy>\S+)')
        # L:2 GigabitEthernet4/0/9  0x00000000000056  IN    4     0 3/2/0   VALID,SET_INHW  0x7fe0a79f0b88
        p2 = re.compile(
            r'(?P<loc>\S+)\s+(?P<interface>[\w\-\/\s]+)\s+(?P<iif_id>\S+)\s+(?P<direction>(OUT|IN))\s+(?P<tccg>\d+)\s+(?P<child>\d+)\s+(?P<mpq>[\w//]+)\s+(?P<state_cfg>\w+),(?P<state_opr>\S+)\s+(?P<address>\S+)')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                if 'tcg_sum_for_policy' not in ret_dict:
                    sum_dict = ret_dict.setdefault('tcg_sum_for_policy', {})
                policy = str(group['policy'])
                sum_dict[policy] = {}
                sum_dict[policy]['interface'] = {}
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                interface = str(group['interface'])
                interface = interface.strip()
                sum_dict[policy]['interface'][interface] = {}
                sum_dict[policy]['interface'][interface]['loc'] = str(group['loc'])
                sum_dict[policy]['interface'][interface]['iif_id'] = str(group['iif_id'])
                sum_dict[policy]['interface'][interface]['direction'] = str(group['direction'])
                sum_dict[policy]['interface'][interface]['tccg'] = int(group['tccg'])
                sum_dict[policy]['interface'][interface]['child'] = int(group['child'])
                sum_dict[policy]['interface'][interface]['mpq'] = str(group['mpq'])
                sum_dict[policy]['interface'][interface]['state_cfg'] = str(group['state_cfg'])
                sum_dict[policy]['interface'][interface]['state_opr'] = str(group['state_opr'])
                sum_dict[policy]['interface'][interface]['address'] = str(group['address'])
                continue

        return ret_dict


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

    def cli(self,signature, output=None):
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

        # 7E873A87E287B685E823F7BC66CF13D43EC238D40DA7CBEA06F6926C04C8C5AFC21BA4C
        p5=re.compile('^(?P<signatur>\d[A-Z\d]+)$')

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
        'power_supply': {
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
    }


class ShowEnvironmentStatus(ShowEnvironmentStatusSchema):
    """ Parser for show environment status"""

    cli_command = 'show environment status'

    def cli(self,output=None):
        if output is None:
            # excute command to get output
            output = self.device.execute(self.cli_command)

        # initial variables
        ret_dict = {}
        # PS1     C9K-PWR-1500WAC-R     ac    n.a.      standby    good  good
        p1= re.compile('^(?P<power_supply>\w+)\s+(?P<model_num>[\w-]+)\s+(?P<type>\w+)\s+(?P<capacity>[\w.]+)[A-Z\s]+(?P<status>[\w-]+)\s+(?P<fan_state0>[\w.]+)\s+(?P<fan_state1>[\w.]+)$')

        # FM6     active      good  good
        p2= re.compile('^(?P<fan_tray>\w+\d+)\s+(?P<status>\w+)\s+(?P<fan_state0>\w+)\s+(?P<fan_state1>\w+)$')

        for line in output.splitlines():
            line = line.strip()

            # PS1     C9K-PWR-1500WAC-R     ac    n.a.      standby    good  good
            m=p1.match(line)
            if m:
                group= m.groupdict()
                root_dict=ret_dict.setdefault('power_supply',{}).setdefault(group['power_supply'],{})
                root_dict.setdefault('model_num',group['model_num'])
                root_dict.setdefault('type',group['type'])
                root_dict.setdefault('capacity',group['capacity'])
                root_dict.setdefault('status',group['status'])
                root_dict1=root_dict.setdefault('fan_states',{})
                root_dict1.setdefault(0,group['fan_state0'])
                root_dict1.setdefault(1,group['fan_state1'])
                continue

            # FM6     active      good  good
            m=p2.match(line)
            if m:
                group=m.groupdict()
                root_dict = ret_dict.setdefault('fan_tray', {}).setdefault(group['fan_tray'],{})
                root_dict.setdefault('status',group['status'])
                root_dict1=root_dict.setdefault('fan_states',{})
                root_dict1.setdefault(0,group['fan_state0'])
                root_dict1.setdefault(1,group['fan_state1'])
                continue

        return ret_dict


class ShowPlatformSoftwareDbalR0DataAllSchema(MetaParser):
  schema = {
  'db_name': {
         Any():{
           'db_mode':str,
            'batches_waiting':int,
            'batches_in_progress':int,
             'batches_done': int,
             'tunnels_active': int,
             'tunnels_closed': int
           }
       }
   }

class ShowPlatformSoftwareDbalR0DataAll(ShowPlatformSoftwareDbalR0DataAllSchema):
    cli_command = 'show platform software dbal smd R0 database all'
    def cli(self, output=None):
        out = self.device.execute(self.cli_command) if output is None else output

        ret_dict = {}


#SMD_CONF                  Local                       0                     0                30                 0                 0

        pr = re.compile(r'^(?P<db_name>\S+) +'
                       r'(?P<db_mode>\S+) +'
                       r'(?P<batches_waiting>\d+) +'
                       r'(?P<batches_in_progress>\d+) +'
                       r'(?P<batches_done>\d+) +'
                       r'(?P<tunnels_active>\d+) +'
                       r'(?P<tunnels_closed>\d+)$')

        for line in out.splitlines():
          line = line.strip()

          m =  pr.match(line)
          if m:
             group = m.groupdict()

             dbnames_dict = ret_dict.setdefault('db_name', {})
             dbname_dict = dbnames_dict.setdefault(group['db_name'],{})

             dbname_dict.update({
              'db_mode': group['db_mode'],
              'batches_waiting' : int(group['batches_waiting']),
              'batches_in_progress' : int(group['batches_in_progress']),
              'batches_done' : int(group['batches_done']),
              'tunnels_active' : int(group['tunnels_active']),
              'tunnels_closed' : int(group['tunnels_closed'])
             }) 
          
             continue

        return ret_dict

class showPlatformMplsRlistIdSchema(MetaParser):
    """
    Schema for show environment status
    """
    schema = {
        'rlist_id': {
            Any(): {
                'state': int,
                'status': str,
                'flags': str,
                'remote_ifs': int,
                'packets' : int,
                'pps': int
            },
        },
    }

class ShowPlatformMplsRlistId(showPlatformMplsRlistIdSchema):
    """Parser for:
        show platform software fed switch <switch_type> mpls rlist | in RLIST id:
        """
    cli_command = 'show platform software fed switch {switch_type} mpls rlist | in RLIST id:'

    def cli(self, switch_type="", output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(switch_type=switch_type))

        ret_dict = {}

        ###RLIST id: 0xf0001aeb State: 1 {OK} Flags: 0x0 remote_ifs: 0 packets: 0 (0 pps approx.)
        p1=re.compile(r"^RLIST\s+id:\s+(?P<rlist_id>\S+)\s+State:\s+(?P<state>\d+)\s+\{(?P<status>\S+)\}\s+Flags:\s+(?P<flags>\S+)\s+[A-Z\{\} ]*\s*remote_ifs:\s+(?P<remote_ifs>\d+)\s+packets:\s+(?P<packets>\d+)\s+\((?P<pps>\d+).*$")

        for line in output.splitlines():
            line = line.strip()

            ##RLIST id: 0xf0001aeb State: 1 {OK} Flags: 0x0 remote_ifs: 0 packets: 0 (0 pps approx.)
            m1=p1.match(line)
            if m1:
                r=m1.groupdict()
                res=ret_dict.setdefault('rlist_id',{}).setdefault(r['rlist_id'],{})
                r.pop('rlist_id')
                for key,value in r.items():
                    res[key]=int(value) if value.isdigit() else value
        return ret_dict

class ShowPlatformHardwareFedSwitchActiveFwdAsicDropsExceptionsSchema(MetaParser):
    """Schema for show platform hardware fed switch active fwd-asic drops exceptions in svl"""
    schema = {
        'asic': {
            Any(): {
                'name': {
                    Any(): {
                            'prev': int,
                            'current': int,
                            'delta': int,
                            }
                        }
                    }
                }
            }


class ShowPlatformHardwareFedSwitchActiveFwdAsicDropsExceptions(ShowPlatformHardwareFedSwitchActiveFwdAsicDropsExceptionsSchema):
    """Parser for show platform hardware fed switch active fwd-asic drops exceptions in svl """

    cli_command = 'show platform hardware fed switch active fwd-asic drops exceptions'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        #****EXCEPTION STATS ASIC INSTANCE 0 (asic/core 0/0)****
        p1=re.compile(r'^\*{4}EXCEPTION +STATS +ASIC +INSTANCE +(?P<asic>\d) +\(asic/core \d\/\d\)\*{4}$')

        #0  0  NO_EXCEPTION                                   354740102   354740637    535
        p2=re.compile(r'^\d +\d +(?P<name>\w+) +(?P<prev>\d+) +(?P<current>\d+) +(?P<delta>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            #****EXCEPTION STATS ASIC INSTANCE 0 (asic/core 0/0)****
            m = p1.match(line)
            if m:
                group = m.groupdict()
                asic_dict = ret_dict.setdefault('asic', {}).setdefault(group['asic'], {})
                continue
            #0  0  NO_EXCEPTION                                   354740102   354740637    535
            m = p2.match(line)
            if m:
                group = m.groupdict()
                dir_dict = asic_dict.setdefault('name', {}). \
                        setdefault(group['name'], {})
                group.pop('name')
                dir_dict.update({k: int(v) for k, v in group.items()})
                continue
        return ret_dict


class ShowPlatformMplsRlistSummarySchema(MetaParser):
    """
    Schema for show platform software fed switch <switch_type> mpls rlist summary
    """
    schema = {
        'mpls_rlist_summary': {
            'current_count': {
                'rlist': int,
                'rentry': int
            },
            'maximum_reached': {
                'rlist': int,
                'rentry': int
            },
            'total_retry_count': {
                'rlist': int,
                'rentry': int
            },
            'current_lspvif_adj_count': int,
            'max_lspvif_adj': int,
            'current_lspvif_adj_label_count': int,
            'max_lspvif_adj_label_info': int,
            'total_lspvif_adj_label_count' : int,
        },
    }

class ShowPlatformMplsRlistSummary(ShowPlatformMplsRlistSummarySchema):
    """Parser for:
        show platform software fed switch <switch_type> mpls rlist
        """
    cli_command = 'show platform software fed switch {switch_type} mpls rlist summary'

    def cli(self, switch_type, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(switch_type=switch_type))

        # Current Count (RLIST/RENTRY) : 4 / 2
        p1=re.compile(r"Current\s+Count\s+\(RLIST\/RENTRY\)\s+\:\s+(?P<rlist>\d+)\s+\/\s+(?P<rentry>\d+)")

        # Maximum Reached (RLIST/RENTRY) : 24 / 48
        p2=re.compile(r"Maximum\s+Reached\s+\(RLIST\/RENTRY\)\s+\:\s+(?P<rlist>\d+)\s+\/\s+(?P<rentry>\d+)")

        # Total Retry Count (RLIST/RENTRY) : 0 / 0
        p3=re.compile(r"Total\s+Retry\s+Count\s+\(RLIST\/RENTRY\)\s+\:\s+(?P<rlist>\d+)\s+\/\s+(?P<rentry>\d+)")

        # Current Lspvif Adjacency's Count : 5
        p4=re.compile(r"Current\s+Lspvif\s+Adjacency's\s+Count\s+\:\s+(?P<current_lspvif_adj_count>\d+)")

        # Max reached Lspvif Adjacency's : 40
        p5=re.compile(r"Max\s+reached\s+Lspvif\s+Adjacency's\s+\:\s+(?P<max_lspvif_adj>\d+)")

        # Current Lspvif Adj label info Count : 1
        p6=re.compile(r"Current\s+Lspvif\s+Adj\s+label\s+info\s+Count\s+\:\s+(?P<current_lspvif_adj_label_count>\d+)")

        # Max reached Lspvif Adj label info : 11
        p7=re.compile(r"Max\s+reached\s+Lspvif\s+Adj\s+label\s+info\s+\:\s+(?P<max_lspvif_adj_label_info>\d+)")

        # Total Retry Lspvif Adj label info Count : 0
        p8=re.compile(r"Total\s+Retry\s+Lspvif\s+Adj\s+label\s+info\s+Count\s+\:\s+(?P<total_lspvif_adj_label_count>\d+)")

        mpls_rlist_summary=dict()
        for line in output.splitlines():
            line=line.strip()

            # Current Count (RLIST/RENTRY) : 4 / 2
            m = p1.match(line)
            if m:
                mpls_rlist_summary_dict=mpls_rlist_summary.setdefault('mpls_rlist_summary',{})
                current_count_dict=mpls_rlist_summary_dict.setdefault('current_count',{})
                for item, value in m.groupdict().items():
                    current_count_dict.update({item:int(value)})

            # Maximum Reached (RLIST/RENTRY) : 24 / 48
            m = p2.match(line)
            if m:
                max_reached_dict=mpls_rlist_summary_dict.setdefault('maximum_reached',{})
                for item, value in m.groupdict().items():
                    max_reached_dict.update({item:int(value)})

            # Total Retry Count (RLIST/RENTRY) : 0 / 0
            m = p3.match(line)
            if m:
                total_retry_count_dict=mpls_rlist_summary_dict.setdefault('total_retry_count',{})
                for item, value in m.groupdict().items():
                    total_retry_count_dict.update({item:int(value)})

            # Current Lspvif Adjacency's Count : 5
            m = p4.match(line)
            if m:
                mpls_rlist_summary_dict.update({
                    'current_lspvif_adj_count':int(m.groupdict()['current_lspvif_adj_count'])})

            # Max reached Lspvif Adjacency's : 40
            m = p5.match(line)
            if m:
                mpls_rlist_summary_dict.update({
                    'max_lspvif_adj':int(m.groupdict()['max_lspvif_adj'])})

            # Current Lspvif Adj label info Count : 1
            m = p6.match(line)
            if m:
                mpls_rlist_summary_dict.update({
                    'current_lspvif_adj_label_count':int(m.groupdict()['current_lspvif_adj_label_count'])})

            # Max reached Lspvif Adj label info : 11
            m = p7.match(line)
            if m:
                mpls_rlist_summary_dict.update({
                    'max_lspvif_adj_label_info':int(m.groupdict()['max_lspvif_adj_label_info'])})

            # Total Retry Lspvif Adj label info Count : 0
            m = p8.match(line)
            if m:
                mpls_rlist_summary_dict.update({
                    'total_lspvif_adj_label_count':int(m.groupdict()['total_lspvif_adj_label_count'])})

        return mpls_rlist_summary


class ShowPlatformSoftwareInterfaceSwitchF0BriefSchema(MetaParser):
    """
    Schema for show platform software interface switch {mode} F0 brief
    """
    schema = {
        'forwarding_manager_interface_information': {
            Any():{
                'id': int,
                'qfp_id': int,
            },
        }
    }


class ShowPlatformSoftwareInterfaceSwitchF0Brief(ShowPlatformSoftwareInterfaceSwitchF0BriefSchema):
    """ Parser for show platform software interface switch {mode} F0 brief"""

    cli_command = 'show platform software interface switch {mode} F0 brief'

    def cli(self, mode, output=None):
        if output is None:
            # excute command to get output
            output = self.device.execute(self.cli_command.format(mode=mode))

        # initial variables
        ret_dict = {}
        # HundredGigE2/0/35/4                1285              1285
        p1=re.compile('^(?P<name>\S+)\s+(?P<id>\d+)\s+(?P<qfp_id>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            # HundredGigE2/0/35/4                1285              1285
            m=p1.match(line)
            if m:
                group=m.groupdict()
                root_dict = ret_dict\
                    .setdefault('forwarding_manager_interface_information',{})\
                    .setdefault(group['name'],{})
                root_dict['id']=int(group['id'])
                root_dict['qfp_id']=int(group['qfp_id'])
                continue

        return ret_dict


class ShowPlatformSoftwareFedSwitchPortSummarySchema(MetaParser):
    """
    Schema for show platform software fed switch {mode} port summary
    """
    schema = {
        'interface': {
            Any(): {
                'if_id': int,
                'port_enable': str,
            }
        }
    }


class ShowPlatformSoftwareFedSwitchPortSummary(ShowPlatformSoftwareFedSwitchPortSummarySchema):
    """ Parser for show platform software fed switch {mode} port summary"""

    cli_command = 'show platform software fed switch {mode} port summary'

    def cli(self, mode, output=None):
        if output is None:
            # excute command to get output
            output = self.device.execute(self.cli_command.format(mode=mode))

        # initial variables
        ret_dict = {}

        # 1266           HundredGigE2/0/27/1             true
        p1 = re.compile('^(?P<if_id>\d+)\s+(?P<if_name>\S+)\s+(?P<port_enable>\w+)$')

        for line in output.splitlines():
            line = line.strip()

            # 1266           HundredGigE2/0/27/1             true
            m=p1.match(line)
            if m:
                group = m.groupdict()
                root_dict = ret_dict.setdefault('interface',{}).setdefault(group['if_name'],{})
                root_dict['if_id'] = int(group['if_id'])
                root_dict['port_enable'] = group['port_enable']
                continue
        return ret_dict

# ==================================================
# Parser for 'show platform software fed mode count'
# ==================================================
class ShowPlatformSoftwareFedLspaAllPermodeSchema(MetaParser):

    ''' Schema for "show Platform software fed mode count" '''

    schema = {
        'lspa_mode_count':int
        }

# ==================================================
# Parser for 'show platform software fed mode count'
# ==================================================
class ShowPlatformSoftwareFedLspaAllPermode(ShowPlatformSoftwareFedLspaAllPermodeSchema):
    ''' Parser for
      "show platform software fed {switchvirtualstate} mpls lspa all | c {mode}"
    '''

    cli_command = ['show platform software fed {switchvirtualstate} mpls lspa all | c {mode}']

    def cli(self, switchvirtualstate="", mode="", output=None):
        if output is None:
            cmd = self.cli_command[0].format(switchvirtualstate=switchvirtualstate,mode=mode)
            output = self.device.execute(cmd)

        # Init vars
        ret_dict = {}

        #Number of lines which match regexp = 0
        p1 = re.compile(r'^Number +of +lines +which +match +regexp+\s+\W+\s+(?P<lspa_mode_count>(\d+))$')

        for line in output.splitlines():
            line = line.strip()

            #Number of lines which match regexp = 0
            m = p1.match(line)
            if m:
                lspa_mode_count=int(m.groupdict()['lspa_mode_count'])
                ret_dict['lspa_mode_count']= lspa_mode_count
                continue
        return ret_dict

# =======================================
# Parser for 'show platform software fed'
# =======================================
class ShowPlatformSoftwareFedLspaAllSchema(MetaParser):

    ''' Schema for "show Platform software fed" '''

    schema = {
            'lspa_info': {
                    Optional('total_lspa_entries'):int,
                    Optional('lspa_record'): {
                            Any(): {
                                    Optional('mode'):str,
                                    Optional('ref_cnt'):int
                            }
                    }
            }
    }

# =======================================
# Parser for 'show platform software fed'
# =======================================
class ShowPlatformSoftwareFedLspaAll(ShowPlatformSoftwareFedLspaAllSchema):
    ''' Parser for
      "show platform software fed {switchvirtualstate} mpls lspa all"
    '''

    cli_command = ['show platform software fed {switchvirtualstate} mpls lspa all']

    def cli(self, switchvirtualstate="", output=None):
        if output is None:
            cmd = self.cli_command[0].format(switchvirtualstate=switchvirtualstate)
            output = self.device.execute(cmd)

        # Init vars
        ret_dict = {}

        #Detailed LSPA info for all LSPA: (# of entries:2)
        p1 = re.compile(r'^Detailed +LSPA +info +for +all +LSPA+\W+of +entries\W+(?P<total_lspa_entries>\d+)\)$')
        #LSPA:NPD:lspa_rec:0x118804cdfb8 lspa:0x118804ce108 rm_hdl:0 mode:PER_VRF ref_cnt:11
        #       lspakey[pfx1_gid,vpnlbl]:[1010,22][0,0] mode:1
        #       lspa:[vrf_id:6 vpn_encap_gid:0 l3nh_oid:1501 paths:1 dst_oid:1495]
        #    SDK: fec:oid:1501 l3_fec_st:1495, type:la_prefix_object_base(oid=1495)
        p2 = re.compile(r'^\S+lspa_rec\W+(?P<lspa_rec>(\S+))+\s+\S+\s+\S+\s+mode\W+(?P<mode>(\S+))+\s+ref_cnt\W+(?P<ref_cnt>(\d+))$')

        for line in output.splitlines():
            line = line.strip()

            #Detailed LSPA info for all LSPA: (# of entries:2)
            m = p1.match(line)
            if m:
                lspa_dict = ret_dict.setdefault('lspa_info', {})
                total_lspa_entries=int(m.groupdict()['total_lspa_entries'])
                lspa_dict['total_lspa_entries'] = total_lspa_entries
                continue

            m = p2.match(line)
            if m:
                lspa_rec_dict = lspa_dict.setdefault('lspa_record', {})
                rec_id=m.groupdict()['lspa_rec']
                lspa_rec=lspa_rec_dict.setdefault(rec_id,{})
                mode = m.groupdict()['mode']
                ref_cnt = int(m.groupdict()['ref_cnt'])
                lspa_rec['mode']=mode
                lspa_rec['ref_cnt']=ref_cnt
                continue

        return ret_dict

# ==============================================================
# Parser for 'show platform software dns-umbrella statistics'
# ==============================================================
class ShowPlatformSoftwareDnsUmbrellaStatisticsSchema(MetaParser):
    """Schema for show platform software dns-umbrella statistics"""
    schema = {
        'umbrella_statistics': {
            'total_packets': int,
            'dns_crypt_queries': int,
            'dns_crypt_responses': int,
            'dns_queries': int,
            'dns_bypass_queries': int,
            'dns_umbrella_responses': int,
            'dns_other_responses': int,
            'aged_queries': int,
            'dropped_packets': int,
        },
    }

class ShowPlatformSoftwareDnsUmbrellaStatistics(ShowPlatformSoftwareDnsUmbrellaStatisticsSchema):
    """Parser for show platform software dns-umbrella statistics"""

    cli_command = 'show platform software dns-umbrella statistics'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # Umbrella Statistics
        p0 = re.compile(r'^Umbrella\s+Statistics$')

        #Total Packets               : 57057
        p1 = re.compile(r'^Total\s+Packets\s+:\s+(?P<TotalPacket>\d+)$')

        #DNSCrypt queries            : 0
        p2 = re.compile(r'^DNSCrypt\s+queries\s+:\s+(?P<DnsCryptQueri>\d+)$')

        #DNSCrypt responses          : 0
        p3 = re.compile(r'^DNSCrypt\s+responses\s+:\s+(?P<DnsCryptResp>\d+)$')

        #DNS queries                 : 32321
        p4 = re.compile(r'^DNS\s+queries\s+:\s+(?P<DnsQueri>\d+)$')

        #DNS bypassed queries(Regex) : 0
        p5 = re.compile(r'^DNS\s+bypassed\s+queries\(Regex\)\s+:\s+(?P<DnsBypassQueri>\d+)$')

        #DNS responses(Umbrella)     : 24693
        p6 = re.compile(r'^DNS\s+responses\(Umbrella\)\s+:\s+(?P<DnsUmbrellaResp>\d+)$')

        #DNS responses(Other)        : 37
        p7 = re.compile(r'^DNS\s+responses\(Other\)\s+:\s+(?P<DnsOtherResp>\d+)$')

        #Aged queries                : 7628
        p8 = re.compile(r'^Aged\s+queries\s+:\s+(?P<AgedQueri>\d+)$')

        #Dropped pkts                : 0
        p9 = re.compile(r'^Dropped\s+pkts\s+:\s+(?P<DroppedPkts>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            #Umbrella Statistics
            m = p0.match(line)
            if m:
                ret_dict['umbrella_statistics'] = {}
                continue

            #Total Packets               : 57057
            m = p1.match(line)
            if m:
                ret_dict['umbrella_statistics']['total_packets'] = int(m.groupdict()['TotalPacket'])
                continue

            #DNSCrypt queries            : 0
            m = p2.match(line)
            if m:
                ret_dict['umbrella_statistics']['dns_crypt_queries'] = int(m.groupdict()['DnsCryptQueri'])
                continue

            #DNSCrypt responses          : 0
            m = p3.match(line)
            if m:
                ret_dict['umbrella_statistics']['dns_crypt_responses'] = int(m.groupdict()['DnsCryptResp'])
                continue

            #DNS queries                 : 32321
            m = p4.match(line)
            if m:
                ret_dict['umbrella_statistics']['dns_queries'] = int(m.groupdict()['DnsQueri'])
                continue

            #DNS bypassed queries(Regex) : 0
            m = p5.match(line)
            if m:
                ret_dict['umbrella_statistics']['dns_bypass_queries'] = int(m.groupdict()['DnsBypassQueri'])
                continue

            #DNS responses(Umbrella)     : 24693
            m = p6.match(line)
            if m:
                ret_dict['umbrella_statistics']['dns_umbrella_responses'] = int(m.groupdict()['DnsUmbrellaResp'])
                continue

            #DNS responses(Other)        : 37
            m = p7.match(line)
            if m:
                ret_dict['umbrella_statistics']['dns_other_responses'] = int(m.groupdict()['DnsOtherResp'])
                continue

            #Aged queries                : 7628
            m = p8.match(line)
            if m:
                ret_dict['umbrella_statistics']['aged_queries'] = int(m.groupdict()['AgedQueri'])
                continue

            #Dropped pkts                : 0
            m = p9.match(line)
            if m:
                ret_dict['umbrella_statistics']['dropped_packets'] = int(m.groupdict()['DroppedPkts'])
                continue

        return ret_dict