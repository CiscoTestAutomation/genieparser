"""
 cat6k implementation of show_platform.py
"""

import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

# genie.parsergen
try:
    import genie.parsergen
except (ImportError, OSError):
    pass

# import parser utils
from genie.libs.parser.utils.common import Common


class ShowVersionSchema(MetaParser):
    """Schema for show version"""
    schema = {
                'version': {
                    'version_short': str,
                    'platform': str,
                    'version': str,
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
                    Optional('image_text_base'): str,
                    Optional('image_data_base'): str,
                    Optional('system_restarted_at'): str,
                    Optional('system_image'): str,
                    Optional('last_reload_reason'): str,
                    Optional('license_type'): str,
                    Optional('license_level'): str,
                    Optional('next_reload_license_level'): str,
                    Optional('chassis'): str,
                    Optional('processor_type'): str,
                    Optional('chassis_sn'): str,
                    Optional('rtr_type'): str,
                    'os': str,
                    'curr_config_register': str,
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
                            Optional('mb_sn'): str,
                            Optional('model_rev_num'): str,
                            Optional('mb_rev_num'): str,
                            Optional('model_num'): str,
                            Optional('system_sn'): str,
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
                }
            }


class ShowVersion(ShowVersionSchema):
    """ Parser for show version"""

    cli_command = 'show version'
    exclude = ['system_restarted_at', 'uptime_this_cp', 'uptime']

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        version_dict = {}
        active_dict = {}
        rtr_type = ''
        suite_flag = False
        license_flag = False

        # IOS (tm) s72033_rp Software (s72033_rp-ADVENTERPRISEK9_WAN-M), Version 12.2(18)SXF7, RELEASE SOFTWARE (fc1)
        p1 = re.compile(r'^(?P<os>[A-Z]+) +\(.*\) +(?P<platform>.+) +Software'
                        r' +\((?P<image_id>.+)\).+( +Experimental)? +[Vv]ersion'
                        r' +(?P<version>\S+), +RELEASE SOFTWARE .*$')

        # match version: 12.2(18)SXF7
        p2 = re.compile(r'^(?P<ver_short>\d+\.\d+).*')

        # Technical Support: http://www.cisco.com/techsupport
        p3 = re.compile(r'^Technical +Support: +http\:\/\/www'
                        r'\.cisco\.com\/techsupport')

        # Copyright (c) 1986-2016 by Cisco Systems, Inc.
        p4 = re.compile(r'^Copyright +(.*)$')

        # Compiled Mon 10-Apr-17 04:35 by mcpre
        # Compiled Mon 19-Mar-18 16:39 by prod_rel_team
        p36 = re.compile(r'^Compiled +(?P<compiled_date>[\S\s]+) +by '
                         r'+(?P<compiled_by>\w+)$')

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

        # next_reload_license_level
        p17 = re.compile(r'^[Nn]ext +(reload|reboot) +license +Level\: '
                         r'+(?P<next_reload_license_level>.+)$')

        # chassis, processor_type, main_mem and rtr_type
        # cisco WS-C3650-24PD (MIPS) processor (revision H0) with 829481K/6147K bytes of memory.
        # cisco CSR1000V (VXE) processor (revision VXE) with 1987991K/3075K bytes of memory.
        # cisco C1111-4P (1RU) processor with 1453955K/6147K bytes of memory.
        # Cisco IOSv (revision 1.0) with  with 435457K/87040K bytes of memory.
        # cisco WS-C3750X-24P (PowerPC405) processor (revision W0) with 262144K bytes of memory.
        # cisco ISR4451-X/K9 (2RU) processor with 1795979K/6147K bytes of memory.
        # cisco WS-C4507R+E (MPC8572) processor (revision 10) with 2097152K/20480K bytes of memory.
        p18 = re.compile(r'^(C|c)isco +(?P<chassis>[a-zA-Z0-9\-\/\+]+) '
                         r'+\((?P<processor_type>.+)\) +((processor.*)|with) '
                         r'+with +(?P<main_mem>[0-9]+)[kK](\/[0-9]+[kK])?')

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
        p27 = re.compile(r'^[Ss]witch +uptime +\: +(?P<uptime>.+)$')

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

        # IOS (tm) s72033_rp Software (s72033_rp-ADVENTERPRISEK9_WAN-M), Version 12.2(18)SXF7, RELEASE SOFTWARE (fc1)
        p35 = re.compile(r'(?P<os>([A-Z]+)) \(\S+\)\s+(?P<platform>\S+)\s+'
                         r'Software\s+\((?P<image_id>\S+)\), Version (?P<version>\S+),'
                         r'\s*RELEASE\s+SOFTWARE\s+\(\S+\)')


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
        p38 = re.compile(r'^Last +reload +type\: +(?P<last_reload_type>[\S ]+)$')

        # P2020 CPU at 800MHz, E500v2 core, 512KB L2 Cache
        p39 = re.compile(r'^(?P<cpu_name>\S+) +(CPU|cpu|Cpu) +at '
                         r'+(?P<speed>\S+)\,(( +(?P<core>\S+) +core\, '
                         r'+(?P<l2_cache>\S+) +L2 +[Cc]ache)|( +Supervisor '
                         r'+(?P<supervisor>\S+)))$')

        # 98304K bytes of processor board System flash (Read/Write)
        p40 = re.compile(r'^(?P<processor_board_flash>\S+) +bytes .+$')

        # Running default software
        p41 = re.compile(
            r'^Running +(?P<running_default_software>\S+) +software$')

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

        for line in out.splitlines():
            line = line.strip()

            # version
            # Cisco IOS Software [Everest], ISR Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 16.6.5, RELEASE SOFTWARE (fc3)
            # Cisco IOS Software, IOS-XE Software, Catalyst 4500 L3 Switch Software (cat4500e-UNIVERSALK9-M), Version 03.03.02.SG RELEASE SOFTWARE (fc1)
            m = p1.match(line)
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
                    # entservices   Type: Permanent
                    p16_1 = re.compile(r'(?P<license_level>\S+) +Type\: '
                                       r'+(?P<license_type>\S+)')
                    lic_type = group['license_level'].strip()
                    m_1 = p16_1.match(lic_type)
                    group = m_1.groupdict()
                    version_dict['version']['license_type'] = group['license_type']
                    version_dict['version']['license_level'] = group['license_level']
                else:
                    version_dict['version']['license_level'] = group['license_level']
                continue

            # next_reload_license_level
            # Next reboot license Level: entservices
            # Next reload license Level: advipservices
            m = p17.match(line)
            if m:
                version_dict['version']['next_reload_license_level'] = \
                    m.groupdict()['next_reload_license_level']
                continue

            # chassis, processor_type, main_mem and rtr_type
            # cisco WS-C3650-24PD (MIPS) processor (revision H0) with 829481K/6147K bytes of memory.
            # cisco CSR1000V (VXE) processor (revision VXE) with 1987991K/3075K bytes of memory.
            # cisco C1111-4P (1RU) processor with 1453955K/6147K bytes of memory.
            # Cisco IOSv (revision 1.0) with  with 435457K/87040K bytes of memory.
            # cisco WS-C3750X-24P (PowerPC405) processor (revision W0) with 262144K bytes of memory.
            # cisco ISR4451-X/K9 (2RU) processor with 1795979K/6147K bytes of memory.
            m = p18.match(line)
            if m:
                version_dict['version']['chassis'] \
                    = m.groupdict()['chassis']
                version_dict['version']['main_mem'] \
                    = m.groupdict()['main_mem']
                version_dict['version']['processor_type'] \
                    = m.groupdict()['processor_type']
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
                if 'Edison' in rtr_type:
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
                version_dict['version']['switch_num'][switch_number]['mb_assembly_num'] = m.groupdict()[
                    'mb_assembly_num']
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

            # IOS (tm) s72033_rp Software (s72033_rp-ADVENTERPRISEK9_WAN-M), Version 12.2(18)SXF7, RELEASE SOFTWARE (fc1)
            m = p35.match(line)
            if m:
                group = m.groupdict()
                os = group['os']
                platform = group['platform']
                image_id = group['image_id']
                version = group['version']

                # 16.6.5
                result = p2.match(version)
                version_short_dict = result.groupdict()
                version_short = version_short_dict['ver_short']

                version_dict2 = version_dict.setdefault('version', {})

                version_dict2['os'] = os
                version_dict2['version_short'] = version_short
                version_dict2['platform'] = platform
                version_dict2['version'] = version
                version_dict2['image_id'] = image_id

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
                        license_dict.update(
                            {'next_reload_license_level': group['next_boot']})

                if suite_flag:
                    suite_lic_dict = suite_dict.setdefault(group['technology'], {})

                    if group['license_level']:
                        suite_lic_dict.update(
                            {'suite_current': group['license_level']})

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

        # table2 for C3850
        tmp2 = genie.parsergen.oper_fill_tabular(right_justified=True,
                                                 header_fields=
                                                 ["Switch",
                                                  "Ports",
                                                  "Model             ",
                                                  'SW Version       ',
                                                  "SW Image              ",
                                                  "Mode   "],
                                                 label_fields=
                                                 ["switch_num",
                                                  "ports",
                                                  "model",
                                                  "sw_ver",
                                                  'sw_image',
                                                  'mode'],
                                                 index=[0, ],
                                                 table_terminal_pattern=r"^\n",
                                                 device_output=out,
                                                 device_os='iosxe')

        # switch_number
        # license table for Cat3850
        tmp = genie.parsergen.oper_fill_tabular(right_justified=True,
                                                header_fields=
                                                ["Current            ",
                                                 "Type            ",
                                                 "Next reboot  "],
                                                label_fields=
                                                ["license_level",
                                                 "license_type",
                                                 "next_reload_license_level"],
                                                table_terminal_pattern=r"^\n",
                                                device_output=out,
                                                device_os='iosxe')

        if tmp.entries:
            res = tmp
            for key in res.entries.keys():
                for k, v in res.entries[key].items():
                    version_dict['version'][k] = v
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
                            version_dict['version']['switch_num'][switch_no]['uptime'] = uptime_this_cp
                            version_dict['version']['switch_num'][switch_no]['active'] = True
                            version_dict['version']['switch_num'][switch_no]. \
                                update(active_dict) if active_dict else None
                    else:
                        for k, v in res2.entries[key].items():
                            if key not in version_dict['version']['switch_num']:
                                version_dict['version']['switch_num'][key] = {}
                            if 'switch_num' != k:
                                version_dict['version']['switch_num'][key][k] = v
                        version_dict['version']['switch_num'][key]['active'] = False

        return version_dict


class ShowModuleSchema(MetaParser):
    """ Schema for commands:
        * show module
    """
    schema = {
        'slot': {
            Any(): {
                Optional('rp'): {
                    'ports': int,
                    'card_type': str,
                    'model': str,
                    'serial_number': str,
                    'mac_address_from': str,
                    'mac_address_to': str,
                    'hw_ver': str,
                    Optional('fw_ver'): str,
                    Optional('sw_ver'): str,
                    'status': str,
                    Optional('subslot'): {
                        Any(): {
                            'hw_ver': str,
                            'status': str,
                            'serial_number': str,
                            'model': str,
                        }
                    }
                },
                Optional('lc'): {
                    'ports': int,
                    'card_type': str,
                    'model': str,
                    'serial_number': str,
                    'mac_address_from': str,
                    'mac_address_to': str,
                    'hw_ver': str,
                    Optional('fw_ver'): str,
                    Optional('sw_ver'): str,
                    'status': str,
                    Optional('subslot'): {
                        Any(): {
                            'hw_ver': str,
                            'status': str,
                            'serial_number': str,
                            'model': str,
                        }
                    }
                },
                Optional('other'): {                    
                    'ports': int,
                    'card_type': str,
                    'model': str,
                    'serial_number': str,
                    'mac_address_from': str,
                    'mac_address_to': str,
                    'hw_ver': str,
                    Optional('fw_ver'): str,
                    Optional('sw_ver'): str,
                    'status': str,
                    Optional('subslot'): {
                        Any(): {
                            'hw_ver': str,
                            'status': str,
                            'serial_number': str,
                            'model': str,
                        }
                    }                    
                } 
            }
        }
    }


class ShowModule(ShowModuleSchema):
    ''' Parser for commands: 
        * show module 
    '''

    cli_command = 'show module'
    
    def cli(self, output=None):
        
        if output is None:
            output = self.device.execute(self.cli_command)

        parsed_output = {}

        # 1    2  Catalyst 6000 supervisor 2 (Active)    WS-X6K-S2U-MSFC2   SAD0628035C
        # 2    0  Supervisor-Other                       unknown            unknown        
        r1 = re.compile(r'(?P<mod>\d)\s+(?P<ports>\d+)\s+(?P<card_type>.+'
                         '(S|s)upervisor.+)\s+(?P<model>\S+)\s+'
                         '(?P<serial_number>\S+)')
        
        # 6    1  1 port 10-Gigabit Ethernet Module      WS-X6502-10GE      SAD062003CM
        # 3   16  Pure SFM-mode 16 port 1000mb GBIC      WS-X6816-GBIC      SAL061218K3
        r2 = re.compile(r'(?P<mod>\d)\s+(?P<ports>\d+)\s+(?P<card_type>.+\d+\s+'
                         'port.+)\s{2,}(?P<model>\S+)\s+(?P<serial_number>\S+)')

        # 5    0  Switching Fabric Module-136 (Active)   WS-X6500-SFM2      SAD061701YC
        r3 = re.compile('(?P<mod>\d)\s+(?P<ports>\d+)\s+(?P<card_type>.+)\s{2,}'
                        '(?P<model>\S+)\s+(?P<serial_number>\S+)')

        # 1  0001.6416.0342 to 0001.6416.0343   3.9   6.1(3)       7.5(0.6)HUB9 Ok 
        # 3  0005.7485.9518 to 0005.7485.9527   1.3   12.1(5r)E1   12.1(13)E3,  Ok
        # 1  0001.6416.0342 to 0001.6416.0343   3.9   6.1(3)       7.5(0.6)HUB9 Ok    
        r4 = re.compile(r'(?P<mod>\d+)\s+(?P<mac_from>\S+)\s+to\s+(?P<mac_to>\S+)'
                         '\s+(?P<hw>\S+)\s+(?P<fw>\S+)\s+(?P<sw>[\d\.\(\)\w]+)\,'
                         '*\s+(?P<status>(Ok|Unknown))')

        # 1 Policy Feature Card 2       WS-F6K-PFC2     SAD062802AV      3.2    Ok     
        # 1 Cat6k MSFC 2 daughterboard  WS-F6K-MSFC2    SAD062803TX      2.5    Ok   
        # 6 Distributed Forwarding Card WS-F6K-DFC      SAL06261R0A      2.3    Ok     
        # 6 10GBASE-LR Serial 1310nm lo WS-G6488        SAD062201BN      1.1    Ok
        r5 = re.compile(r'(?P<mod>\d+)\s+(?P<sub_mod>.+)\s+(?P<model>\S+)\s+'
                         '(?P<serial>\S+)\s+(?P<hw>\S+)\s+(?P<status>(Ok|Unknown))')

        for line in output.splitlines():
            line = line.strip()

            # 1    2  Catalyst 6000 supervisor 2 (Active)    WS-X6K-S2U-MSFC2   SAD0628035C
            # 2    0  Supervisor-Other                       unknown            unknown        
            result = r1.match(line)
            if result:
                group = result.groupdict()

                mod = group['mod']
                ports = int(group['ports'])
                card_type = group['card_type'].strip()
                model = group['model']
                serial_number = group['serial_number']

                module_dict = parsed_output\
                    .setdefault('slot', {})\
                    .setdefault(mod, {})\
                    .setdefault('rp', {})

                module_dict['ports'] = ports
                module_dict['card_type'] = card_type
                module_dict['model'] = model
                module_dict['serial_number'] = serial_number

                continue

            # 6    1  1 port 10-Gigabit Ethernet Module      WS-X6502-10GE      SAD062003CM
            # 3   16  Pure SFM-mode 16 port 1000mb GBIC      WS-X6816-GBIC      SAL061218K3
            result = r2.match(line)
            if result:
                group = result.groupdict()
                mod = group['mod']
                ports = int(group['ports'])
                card_type = group['card_type'].strip()
                model = group['model']
                serial_number = group['serial_number']

                module_dict = parsed_output\
                    .setdefault('slot', {})\
                    .setdefault(mod, {})\
                    .setdefault('lc', {})

                module_dict['ports'] = ports
                module_dict['card_type'] = card_type
                module_dict['model'] = model
                module_dict['serial_number'] = serial_number

                continue

            # 5    0  Switching Fabric Module-136 (Active)   WS-X6500-SFM2      SAD061701YC
            result = r3.match(line)
            if result:
                group = result.groupdict()
                mod = group['mod']
                ports = int(group['ports'])
                card_type = group['card_type'].strip()
                model = group['model']
                serial_number = group['serial_number']

                module_dict = parsed_output\
                    .setdefault('slot', {})\
                    .setdefault(mod, {})\
                    .setdefault('other', {})

                module_dict['ports'] = ports
                module_dict['card_type'] = card_type
                module_dict['model'] = model
                module_dict['serial_number'] = serial_number

                continue

            # 1  0001.6416.0342 to 0001.6416.0343   3.9   6.1(3)       7.5(0.6)HUB9 Ok 
            # 3  0005.7485.9518 to 0005.7485.9527   1.3   12.1(5r)E1   12.1(13)E3,  Ok
            # 1  0001.6416.0342 to 0001.6416.0343   3.9   6.1(3)       7.5(0.6)HUB9 Ok   
            result = r4.match(line)
            if result:
                group = result.groupdict()

                mod = group['mod']
                mac_from = group['mac_from']
                mac_to = group['mac_to']
                hw = group['hw']
                fw = group['fw']
                sw = group['sw']
                status = group['status']
                
                slot_code = [*parsed_output.get('slot', {}).get(mod, {}).keys()][0]

                module_dict = parsed_output\
                    .setdefault('slot', {})\
                    .setdefault(mod, {})\
                    .setdefault(slot_code, {})

                module_dict['mac_address_from'] = mac_from
                module_dict['mac_address_to'] = mac_to
                module_dict['hw_ver'] = hw
                module_dict['fw_ver'] = fw
                module_dict['sw_ver'] = sw
                module_dict['status'] = status

                continue

            # 1 Policy Feature Card 2       WS-F6K-PFC2     SAD062802AV      3.2    Ok        
            # 1 Cat6k MSFC 2 daughterboard  WS-F6K-MSFC2    SAD062803TX      2.5    Ok   
            # 6 Distributed Forwarding Card WS-F6K-DFC      SAL06261R0A      2.3    Ok     
            # 6 10GBASE-LR Serial 1310nm lo WS-G6488        SAD062201BN      1.1    Ok
            result = r5.match(line)
            if result:
                group = result.groupdict()
                mod = group['mod']
                sub_mod = group['sub_mod']
                model = group['model']
                serial = group['serial']
                hw = group['hw']
                status = group['status']

                slot_code = [*parsed_output.get('slot', {}).get(mod, {}).keys()][0]

                submodule_dict = parsed_output\
                    .setdefault('slot', {})\
                    .setdefault(mod, {})\
                    .setdefault(slot_code, {})\
                    .setdefault('subslot', {})\
                    .setdefault(model, {})

                submodule_dict['hw_ver'] = hw
                submodule_dict['status'] = status
                submodule_dict['serial_number'] = serial
                submodule_dict['model'] = model

                continue

        return parsed_output
