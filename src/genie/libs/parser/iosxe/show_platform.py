''' show_platform.py

IOSXE parsers for the following show commands:

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
'''

# Python
import re
import logging

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional

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
                    Optional('system_restarted_at'): str,
                    'system_image': str,
                    'last_reload_reason': str,
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

    def cli(self,output=None):
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
        for line in out.splitlines():
            line = line.rstrip()

            # version
            # Cisco IOS Software [Everest], ISR Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 16.6.5, RELEASE SOFTWARE (fc3)
            p1 = re.compile(
                r'^\s*[Cc]isco +IOS +[Ss]oftware.+, (?P<platform>.+) '
                 'Software +\((?P<image_id>.+)\).+[Vv]ersion +'
                 '(?P<version>\S+) +')
            m = p1.match(line)
            if m:
                version = m.groupdict()['version']
                p1_2 = re.compile(r'^\s*(?P<ver_short>\d+\.\d+).*')
                m2 = p1_2.match(version)
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
                    continue

            # Cisco IOS Software [Fuji], ASR1000 Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 16.7.1prd4, RELEASE SOFTWARE (fc1)
            # Cisco IOS Software [Fuji], Catalyst L3 Switch Software (CAT3K_CAA-UNIVERSALK9-M), Experimental Version 16.8.20170924:182909 [polaris_dev-/nobackup/mcpre/BLD-BLD_POLARIS_DEV_LATEST_20170924_191550 132]
            # Cisco IOS Software, 901 Software (ASR901-UNIVERSALK9-M), Version 15.6(2)SP4, RELEASE SOFTWARE (fc3)
            p1_1 = re.compile(
                r'^\s*[Cc]isco +(?P<os>([A-Z]+)) +[Ss]oftware(.+)?, +(?P<platform>.+) '
                 'Software +\((?P<image_id>.+)\).+( +Experimental)? +'
                 '[Vv]ersion +(?P<version>[a-zA-Z0-9\.\:\(\)]+) *,?.*')
            m = p1_1.match(line)
            if m:
                version = m.groupdict()['version']
                p1_2 = re.compile(r'^\s*(?P<ver_short>\d+\.\d+).*')
                m2 = p1_2.match(version)
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
            p25 = re.compile(
                r'^\s*Copyright +(.*)$')
            m = p25.match(line)
            if m:
                version_dict.setdefault('version', {}).setdefault('image_type', 'developer image')
                continue

            # Technical Support: http://www.cisco.com/techsupport
            p25_1 = re.compile(
                r'^\s*Technical +Support: +http\:\/\/www\.cisco\.com\/techsupport')
            m = p25_1.match(line)
            if m:
                version_dict.setdefault('version', {}).setdefault('image_type', 'production image')
                continue

            # rom
            p2 = re.compile(
                r'^\s*ROM\: +(?P<rom>.+)$')
            m = p2.match(line)
            if m:
                rom = m.groupdict()['rom']
                version_dict['version']['rom'] = rom                    

                # ROM: Bootstrap program is IOSv
                p2_1 = re.compile(
                    r'^Bootstrap +program +is +(?P<os>.+)$')
                m = p2_1.match(rom)
                if m:
                    version_dict['version']['os'] = \
                        m.groupdict()['os']
                continue

            # bootldr
            p3 = re.compile(
                r'^\s*BOOTLDR\: +(?P<bootldr>.+)$')
            m = p3.match(line)
            if m:
                version_dict['version']['bootldr'] = \
                    m.groupdict()['bootldr']
                continue

            # hostname & uptime
            p4 = re.compile(
                r'^\s*(?P<hostname>.+) +uptime +is +(?P<uptime>.+)$')
            m = p4.match(line)
            if m:
                version_dict['version']['hostname'] = \
                    m.groupdict()['hostname']
                version_dict['version']['uptime'] = \
                    m.groupdict()['uptime']
                continue

            # uptime_this_cp
            p4 = re.compile(
                r'^\s*[Uu]ptime +for +this +control +processor +is +(?P<uptime_this_cp>.+)$')
            m = p4.match(line)
            if m:
                version_dict['version']['uptime_this_cp'] = \
                    m.groupdict()['uptime_this_cp']
                uptime_this_cp = m.groupdict()['uptime_this_cp']
                continue

            # system_restarted_at
            p5 = re.compile(
                r'^\s*[Ss]ystem +restarted +at +(?P<system_restarted_at>.+)$')
            m = p5.match(line)
            if m:
                version_dict['version']['system_restarted_at'] = \
                    m.groupdict()['system_restarted_at']
                continue

            # system_image
            p6 = re.compile(
                r'^\s*[Ss]ystem +image +file +is +\"(?P<system_image>.+)\"')
            m = p6.match(line)
            if m:
                version_dict['version']['system_image'] = \
                    m.groupdict()['system_image']
                continue

            # last_reload_reason
            p7 = re.compile(
                r'^\s*[Ll]ast +reload +reason\: +(?P<last_reload_reason>.+)$')
            m = p7.match(line)
            if m:
                version_dict['version']['last_reload_reason'] = \
                    m.groupdict()['last_reload_reason']
                continue

            # last_reload_reason
            # Last reset from power-on
            p7_1 = re.compile(
                r'^\s*[Ll]ast +reset +from +(?P<last_reload_reason>.+)$')
            m = p7_1.match(line)
            if m:
                version_dict['version']['last_reload_reason'] = \
                    m.groupdict()['last_reload_reason']
                continue

            # license_type
            p8 = re.compile(
                r'^\s*[Ll]icense +[Tt]ype\: +(?P<license_type>.+)$')
            m = p8.match(line)
            if m:
                version_dict['version']['license_type'] = \
                    m.groupdict()['license_type']
                continue

            # license_level
            p8 = re.compile(
                r'^\s*[Ll]icense +[Ll]evel\: +(?P<license_level>.+)$')
            m = p8.match(line)
            if m:
                version_dict['version']['license_level'] = \
                    m.groupdict()['license_level']
                continue

            # next_reload_license_level
            p8 = re.compile(
                r'^\s*[Nn]ext +reload +license +Level\: +(?P<next_reload_license_level>.+)$')
            m = p8.match(line)
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
            p8 = re.compile(
                r'^\s*(C|c)isco +(?P<chassis>[a-zA-Z0-9\-\/]+) +\((?P<processor_type>.+)\) +((processor.*)|with) +with +(?P<main_mem>[0-9]+)[kK](\/[0-9]+[kK])?')
            m = p8.match(line)
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
            p9 = re.compile(
                r'^\s*[pP]rocessor +board +ID +(?P<chassis_sn>[a-zA-Z0-9]+)')
            m = p9.match(line)
            if m:
                version_dict['version']['chassis_sn'] \
                    = m.groupdict()['chassis_sn']
                continue

            # number_of_intfs
            p10 = re.compile(
                r'^\s*(?P<number_of_ports>\d+) +(?P<interface>.+) +interfaces')
            m = p10.match(line)
            if m:
                interface = m.groupdict()['interface']
                if 'number_of_intfs' not in version_dict['version']:
                    version_dict['version']['number_of_intfs'] = {}
                version_dict['version']['number_of_intfs'][interface] = \
                    m.groupdict()['number_of_ports']
                continue

            # mem_size
            p11 = re.compile(
                r'^\s*(?P<mem_size>\d+)K +bytes +of +(?P<memories>.+) +[Mm]emory\.')
            m = p11.match(line)
            if m:
                memories = m.groupdict()['memories']
                if 'mem_size' not in version_dict['version']:
                    version_dict['version']['mem_size'] = {}
                version_dict['version']['mem_size'][memories] = \
                    m.groupdict()['mem_size']
                continue

            # disks, disk_size and type_of_disk
            p12 = re.compile(
                r'^\s*(?P<disk_size>\d+)K bytes of (?P<type_of_disk>.*) at (?P<disks>.+)$')
            m = p12.match(line)
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
            p13 = re.compile(
                r'^\s*[Cc]isco +(?P<os>[a-zA-Z\-]+) +[Ss]oftware,')
            m = p13.match(line)
            if m:
                version_dict['version']['os'] = m.groupdict()['os']
                continue

            # curr_config_register
            p14 = re.compile(
                r'^\s*[Cc]onfiguration +register +is +(?P<curr_config_register>[a-zA-Z0-9]+)')
            m = p14.match(line)
            if m:
                version_dict['version']['curr_config_register'] \
                    = m.groupdict()['curr_config_register']

            # next_config_register
            p15 = re.compile(
                r'^\s*[Cc]onfiguration +register +is +[a-zA-Z0-9]+ +\(will be (?P<next_config_register>[a-zA-Z0-9]+) at next reload\)')
            m = p15.match(line)
            if m:
                version_dict['version']['next_config_register'] \
                    = m.groupdict()['next_config_register']
                continue

            # switch_number
            p16 = re.compile(r'^\s*[Ss]witch +0(?P<switch_number>\d+)$')
            m = p16.match(line)
            if m:
                switch_number = m.groupdict()['switch_number']
                if 'Edison' in rtr_type:
                    if 'switch_num' not in version_dict['version']:
                        version_dict['version']['switch_num'] = {}
                    if switch_number not in version_dict['version']['switch_num']:
                        version_dict['version']['switch_num'][switch_number] = {}
                continue

            # uptime
            p17 = re.compile(
                r'^\s*[Ss]witch +uptime +\: +(?P<uptime>.+)$')
            m = p17.match(line)
            if m:
                if 'switch_num' not in version_dict['version']:
                    continue
                version_dict['version']['switch_num'][switch_number]['uptime'] = m.groupdict()['uptime']
                continue

            # mac_address
            p18 = re.compile(
                r'^\s*[Bb]ase +[Ee]thernet +MAC +[Aa]ddress +\: +(?P<mac_address>.+)$')
            m = p18.match(line)
            if m:
                if 'switch_num' not in version_dict['version']:
                    active_dict.setdefault('mac_address', m.groupdict()['mac_address'])
                    continue
                version_dict['version']['switch_num'][switch_number]['mac_address'] = m.groupdict()['mac_address']
                continue

            # mb_assembly_num
            p19 = re.compile(
                r'^\s*[Mm]otherboard +[Aa]ssembly +[Nn]umber +\: +(?P<mb_assembly_num>.+)$')
            m = p19.match(line)
            if m:
                if 'switch_num' not in version_dict['version']:
                    active_dict.setdefault('mb_assembly_num', m.groupdict()['mb_assembly_num'])
                    continue
                version_dict['version']['switch_num'][switch_number]['mb_assembly_num'] = m.groupdict()['mb_assembly_num']
                continue

            # mb_sn
            p20 = re.compile(
                r'^\s*[Mm]otherboard +[Ss]erial +[Nn]umber +\: +(?P<mb_sn>.+)$')
            m = p20.match(line)
            if m:
                if 'switch_num' not in version_dict['version']:
                    active_dict.setdefault('mb_sn', m.groupdict()['mb_sn'])
                    continue
                version_dict['version']['switch_num'][switch_number]['mb_sn'] = m.groupdict()['mb_sn']
                continue

            # model_rev_num
            p21 = re.compile(
                r'^\s*[Mm]odel +[Rr]evision +[Nn]umber +\: +(?P<model_rev_num>.+)$')
            m = p21.match(line)
            if m:
                if 'switch_num' not in version_dict['version']:
                    active_dict.setdefault('model_rev_num', m.groupdict()['model_rev_num'])
                    continue
                version_dict['version']['switch_num'][switch_number]['model_rev_num'] = m.groupdict()['model_rev_num']
                continue

            # mb_rev_num
            p22 = re.compile(
                r'^\s*[Mm]otherboard +[Rr]evision +[Nn]umber +\: +(?P<mb_rev_num>.+)$')
            m = p22.match(line)
            if m:
                if 'switch_num' not in version_dict['version']:
                    active_dict.setdefault('mb_rev_num', m.groupdict()['mb_rev_num'])
                    continue
                version_dict['version']['switch_num'][switch_number]['mb_rev_num'] = m.groupdict()['mb_rev_num']
                continue

            # model_num
            p23 = re.compile(
                r'^\s*[Mm]odel +[Nn]umber +\: +(?P<model_num>.+)$')
            m = p23.match(line)
            if m:
                if 'switch_num' not in version_dict['version']:
                    active_dict.setdefault('model_num', m.groupdict()['model_num'])
                    continue
                version_dict['version']['switch_num'][switch_number]['model_num'] = m.groupdict()['model_num']
                continue

            # system_sn
            p24 = re.compile(
                r'^\s*[Ss]ystem +[Ss]erial +[Nn]umber +\: +(?P<system_sn>.+)$')
            m = p24.match(line)
            if m:
                if 'switch_num' not in version_dict['version']:
                    active_dict.setdefault('system_sn', m.groupdict()['system_sn'])
                    continue
                version_dict['version']['switch_num'][switch_number]['system_sn'] = m.groupdict()['system_sn']
                continue

        # table2 for C3850
        tmp2 = genie.parsergen.oper_fill_tabular(right_justified=True,
                                           header_fields=
                                                  [ "Switch",
                                                    "Ports",
                                                    "Model             ",
                                                    'SW Version       ',
                                                    "SW Image              ",
                                                    "Mode   "],
                                              label_fields=
                                                  [ "switch_num",
                                                    "ports",
                                                    "model",
                                                    "sw_ver",
                                                    'sw_image',
                                                    'mode'],
                                              index=[0,],
                                              table_terminal_pattern=r"^\n",
                                              device_output=out,
                                              device_os='iosxe')

        if tmp2.entries:
            res2 = tmp2
            # switch_number
        # license table for Cat3850
        tmp = genie.parsergen.oper_fill_tabular(right_justified=True,
                                          header_fields=
                                                  [ "Current            ",
                                                    "Type            ",
                                                    "Next reboot  "],
                                              label_fields=
                                                  [ "license_level",
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
                        version_dict['version']['switch_num'][switch_no].\
                            update(active_dict) if active_dict else None
                else:
                    for k, v in res2.entries[key].items():
                        if key not in version_dict['version']['switch_num']:
                            version_dict['version']['switch_num'][key] = {}
                        if 'switch_num' != k:
                            version_dict['version']['switch_num'][key][k] = v
                    version_dict['version']['switch_num'][key]['active'] = False 

        return version_dict


class DirSchema(MetaParser):
    """Schema for dir"""
    schema = {
                'dir': {
                    'dir': str,
                    Any(): {
                        'files': {
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
    cli_command = 'dir'

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
            p3 = re.compile(
                r'\s*(?P<bytes_total>\d+) +bytes +total +\((?P<bytes_free>\d+) +bytes +free\)')
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
                        'config_register': str,
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

    def cli(self,output=None):
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
        if out:
            redundancy_dict['red_sys_info'] = {}
        for line in out.splitlines():
            line = line.rstrip()

            # available_system_uptime
            p1 = re.compile(
                r'\s*[Aa]vailable +[Ss]ystem +[Uu]ptime +\= +(?P<available_system_uptime>.+)$')
            m = p1.match(line)
            if m:
                redundancy_dict['red_sys_info']['available_system_uptime'] = \
                    m.groupdict()['available_system_uptime']
                continue

            # switchovers_system_experienced
            p2 = re.compile(
                r'\s*[Ss]witchovers +system +experienced +\= +(?P<switchovers_system_experienced>\d+)$')
            m = p2.match(line)
            if m:
                redundancy_dict['red_sys_info']['switchovers_system_experienced'] = \
                    m.groupdict()['switchovers_system_experienced']
                continue

            # standby_failures
            p3 = re.compile(
                r'\s*[Ss]tandby +failures +\= +(?P<standby_failures>\d+)$')
            m = p3.match(line)
            if m:
                redundancy_dict['red_sys_info']['standby_failures'] = \
                    m.groupdict()['standby_failures']
                continue

            # last_switchover_reason
            p4 = re.compile(
                r'^\s*[Ll]ast +[Ss]witchover +[Rr]eason +\= +(?P<last_switchover_reason>.+)$')
            m = p4.match(line)
            if m:
                redundancy_dict['red_sys_info']['last_switchover_reason'] = \
                    m.groupdict()['last_switchover_reason']
                continue

            # hw_mode
            p5 = re.compile(
                r'\s*[Hh]ardware +[Mm]ode +\= +(?P<hw_mode>\S+)$')
            m = p5.match(line)
            if m:
                redundancy_dict['red_sys_info']['hw_mode'] = \
                    m.groupdict()['hw_mode']
                continue

            # conf_red_mode
            p6 = re.compile(
                r'\s*[Cc]onfigured +[Rr]edundancy +[Mm]ode +\= +(?P<conf_red_mode>\S+)$')
            m = p6.match(line)
            if m:
                redundancy_dict['red_sys_info']['conf_red_mode'] = \
                    m.groupdict()['conf_red_mode']
                continue

            # oper_red_mode
            p7 = re.compile(
                r'\s*[Oo]perating +[Rr]edundancy +[Mm]ode +\= +(?P<oper_red_mode>.+)$')
            m = p7.match(line)
            if m:
                redundancy_dict['red_sys_info']['oper_red_mode'] = \
                    m.groupdict()['oper_red_mode']
                continue

            # maint_mode
            p7 = re.compile(
                r'\s*[Mm]aintenance +[Mm]ode +\= +(?P<maint_mode>\S+)$')
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
            Optional('chassis'):
                {Any():
                    {Optional('name'): str,
                    Optional('descr'): str,
                    Optional('pid'): str,
                    Optional('vid'): str,
                    Optional('sn'): str,
                    },
                },
            },
        'slot':
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
        p1 = re.compile(r'^NAME: +\"(?P<name>(.*))\",'
                         ' +DESCR: +\"(?P<descr>(.*))\"$')

        # PID: ASR-920-24SZ-IM   , VID: V01  , SN: CAT1902V19M
        # PID: SFP-10G-LR        , VID: CSCO , SN: CD180456291
        # PID: A900-IMA3G-IMSG   , VID: V01  , SN: FOC2204PAP1
        # PID: SFP-GE-T          , VID: V02  , SN: MTC2139029X
        # PID: ISR4331-3x1GE     , VID: V01  , SN:
        # PID: ISR4331/K9        , VID:      , SN: FDO21520TGH
        # PID: ISR4331/K9        , VID:      , SN:
        p2 = re.compile(r'^PID: +(?P<pid>(\S+)) *, +VID:(?: +(?P<vid>(\S+)))? *,'
                         ' +SN:(?: +(?P<sn>(\S+)))?$')


        for line in out.splitlines():
            line = line.strip()

            # NAME: "Switch 1", DESCR: "WS-C3850-24P-E"
            # NAME: "StackPort5/2", DESCR: "StackPort5/2"
            # NAME: "Switch 5 - Power Supply A", DESCR: "Switch 5 - Power Supply A"
            # NAME: "subslot 0/0 transceiver 2", DESCR: "GE T"
            # NAME: "NIM subslot 0/0", DESCR: "Front Panel 3 ports Gigabitethernet Module"
            m = p1.match(line)
            if m:
                group = m.groupdict()
                name = group['name'].strip()
                descr = group['descr'].strip()

                # Switch 1
                # module 0
                p1_1 = re.compile(r'^(Switch|[Mm]odule) +(?P<slot>(\S+))')
                m1_1 = p1_1.match(name)
                if m1_1:
                    slot = m1_1.groupdict()['slot']
                    # Creat slot_dict
                    slot_dict = ret_dict.setdefault('slot', {}).setdefault(slot, {})

                # Power Supply Module 0
                # Power Supply Module 1
                p1_2 = re.compile(r'Power Supply Module')
                m1_2 = p1_2.match(name)
                if m1_2:
                    slot = name.replace('Power Supply Module ', 'P')
                    # Creat slot_dict
                    slot_dict = ret_dict.setdefault('slot', {}).setdefault(slot, {})

                # SPA subslot 0/0
                # IM subslot 0/1
                # NIM subslot 0/0
                p1_3 = re.compile(r'^(SPA|IM|NIM) +subslot +(?P<slot>(\d+))/(?P<subslot>(\d+))')
                m1_3 = p1_3.match(name)
                if m1_3:
                    group = m1_3.groupdict()
                    slot = group['slot']
                    subslot = group['subslot']
                    # Creat slot_dict
                    slot_dict = ret_dict.setdefault('slot', {}).setdefault(slot, {})

                # subslot 0/0 transceiver 0
                p1_4 = re.compile(r'^subslot +(?P<slot>(\d+))\/(?P<subslot>(.*))')
                m1_4 = p1_4.match(name)
                if m1_4:
                    group = m1_4.groupdict()
                    slot = group['slot']
                    subslot = group['subslot']
                    # Creat slot_dict
                    slot_dict = ret_dict.setdefault('slot', {}).setdefault(slot, {})

                # StackPort1/1
                p1_5 = re.compile(r'^StackPort(?P<slot>(\d+))/(?P<subslot>(\d+))$')
                m1_5 = p1_5.match(name)
                if m1_5:
                    group = m1_5.groupdict()
                    slot = group['slot']
                    subslot = group['subslot']
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
            m = p2.match(line)
            if m:
                group = m.groupdict()
                pid = group['pid']
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
                if ('RP' in pid) or ('WS-C' in pid):
                    rp_dict = slot_dict.setdefault('rp', {}).\
                                        setdefault(pid, {})
                    rp_dict['name'] = name
                    rp_dict['descr'] = descr
                    rp_dict['pid'] = pid
                    rp_dict['vid'] = vid
                    rp_dict['sn'] = sn

                # PID: ASR1000-SIP40     , VID: V02  , SN: JAE200609WP
                # PID: ISR4331/K9        , VID:      , SN: FDO21520TGH
                elif ('SIP' in pid) or ('ISR' in pid):
                    lc_dict = slot_dict.setdefault('lc', {}).\
                                        setdefault(pid, {})
                    lc_dict['name'] = name
                    lc_dict['descr'] = descr
                    lc_dict['pid'] = pid
                    lc_dict['vid'] = vid
                    lc_dict['sn'] = sn

                # PID: SP7041-E          , VID: E    , SN: MTC164204VE
                # PID: SFP-GE-T          , VID: V02  , SN: MTC2139029X   
                elif subslot:
                    if ('STACK' in pid) or asr900_rp:
                        subslot_dict = rp_dict.setdefault('subslot', {}).\
                                               setdefault(subslot, {}).\
                                               setdefault(pid, {})
                    else:
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
                    Optional('chassis'): str
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

        # Switch/Stack Mac Address : 0057.d21b.cc00 - Local Mac Address
        p1 = re.compile(
            r'^[Ss]witch\/[Ss]tack +[Mm]ac +[Aa]ddress +\: +'
             '(?P<switch_mac_address>[\w\.]+) *(?P<local>[\w\s\-]+)?$')

        # Mac persistency wait time: Indefinite
        p2 = re.compile(r'^[Mm]ac +persistency +wait +time\: +(?P<mac_persistency_wait_time>[\w\.\:]+)$')

        # Switch  Ports    Model                Serial No.   MAC address     Hw Ver.       Sw Ver. 
        # ------  -----   ---------             -----------  --------------  -------       --------
        #  1       32     WS-C3850-24P-E        FCW1947C0HH  0057.d21b.cc00  V07           16.6.1
        p3 = re.compile(r'^(?P<switch>\d+) +(?P<ports>\d+) +'
                         '(?P<model>[\w\-]+) +(?P<serial_no>\w+) +'
                         '(?P<mac_address>[\w\.\:]+) +'
                         '(?P<hw_ver>\w+) +(?P<sw_ver>[\w\.]+)$')


        #                                     Current
        # Switch#   Role        Priority      State 
        # -------------------------------------------
        # *1       Active          3          Ready
        p4 = re.compile(r'^\*?(?P<switch>\d+) +(?P<role>\w+) +'
                         '(?P<priority>\d+) +(?P<state>[\w\s]+)$')


        # ----------      ASR1K    -------------
        # Chassis type: ASR1006
        p5 = re.compile(r'^[Cc]hassis +type: +(?P<chassis>\w+)$')

        # Slot      Type                State                 Insert time (ago) 
        # --------- ------------------- --------------------- ----------------- 
        # 0         ASR1000-SIP40       ok                    00:33:53
        #  0/0      SPA-1XCHSTM1/OC3    ok                    2d00h
        p6 = re.compile(r'^(?P<slot>\w+)(\/(?P<subslot>\d+))? +(?P<name>\S+) +'
                         '(?P<state>\w+(\, \w+)?) +(?P<insert_time>[\w\.\:]+)$')

        # 4                             unknown               2d00h
        p6_1 = re.compile(r'^(?P<slot>\w+) +(?P<state>\w+(\, \w+)?)'
                         ' +(?P<insert_time>[\w\.\:]+)$')

        # Slot      CPLD Version        Firmware Version                        
        # --------- ------------------- --------------------------------------- 
        # 0         00200800            16.2(1r) 
        p7 = re.compile(r'^(?P<slot>\w+) +(?P<cpld_version>\d+|N\/A) +'
                         '(?P<fireware_ver>[\w\.\(\)\/]+)$')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                if 'main' not in platform_dict:
                    platform_dict['main'] = {}
                platform_dict['main']['switch_mac_address'] = m.groupdict()['switch_mac_address']
                continue


            m = p2.match(line)
            if m:
                if 'main' not in platform_dict:
                    platform_dict['main'] = {}
                platform_dict['main']['mac_persistency_wait_time'] = m.groupdict()['mac_persistency_wait_time'].lower()
                continue

            m = p3.match(line)
            if m:
                slot = m.groupdict()['switch']
                model = m.groupdict()['model']
                if 'slot' not in platform_dict:
                    platform_dict['slot'] = {}
                if slot not in platform_dict['slot']:
                    platform_dict['slot'][slot] = {}
                if 'WS-C' in model:
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

            m = p4.match(line)
            if m:
                slot = m.groupdict()['switch']
                if 'slot' not in platform_dict:
                    continue
                if slot not in platform_dict['slot']:
                    continue

                for key, value in platform_dict['slot'][slot].items():
                    for key, last in value.items():
                        last['priority'] = m.groupdict()['priority']
                        last['role'] = m.groupdict()['role']
                        last['state'] = m.groupdict()['state']
                continue

            m = p5.match(line)
            if m:
                if 'main' not in platform_dict:
                    platform_dict['main'] = {}
                platform_dict['main']['chassis'] = m.groupdict()['chassis']
                continue

            m = p6.match(line)
            if m:
                slot = m.groupdict()['slot']
                subslot = m.groupdict()['subslot']
                name = m.groupdict()['name']
                if not name:
                    continue

                # subslot
                if subslot:
                    try:
                        if slot not in platform_dict['slot']:
                            continue
                        for key, value in platform_dict['slot'][slot].items():
                            for key, last in value.items():
                                if 'subslot' not in last:
                                    last['subslot'] = {}
                                if subslot not in last['subslot']:
                                    last['subslot'][subslot] = {}
                                if name not in last['subslot'][subslot]:
                                    last['subslot'][subslot][name] = {}
                                sub_dict = last['subslot'][subslot][name]
                        sub_dict['subslot'] = subslot
                    except Exception:
                        continue
                else:
                    if 'slot' not in platform_dict:
                        platform_dict['slot'] = {}
                    if slot not in platform_dict['slot']:
                        platform_dict['slot'][slot] = {}
                    if ('ASR1000-SIP' in name) or ('ASR1000-2T' in name) or ('ASR1000-6T' in name) or ('ISR' in name):
                        lc_type = 'lc'
                    elif 'ASR1000-RP' in name:
                        lc_type = 'rp'
                    elif 'CSR1000V' in name:
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

            m = p6_1.match(line)
            if m:                    
                slot = m.groupdict()['slot']
                if 'slot' not in platform_dict:
                    platform_dict['slot'] = {}
                if slot not in platform_dict['slot']:
                    platform_dict['slot'][slot] = {}

                if 'other' not in platform_dict['slot'][slot]:
                    platform_dict['slot'][slot]['other'] ={}
                    platform_dict['slot'][slot]['other'][''] ={}
                platform_dict['slot'][slot]['other']['']['slot'] = slot
                platform_dict['slot'][slot]['other']['']['name'] = ''
                platform_dict['slot'][slot]['other']['']['state'] = m.groupdict()['state']
                platform_dict['slot'][slot]['other']['']['insert_time'] = m.groupdict()['insert_time']
                continue

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

        return platform_dict


class ShowBootSchema(MetaParser):
    """Schema for show boot"""

    schema = {Optional('current_boot_variable'): str,
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
    }

class ShowBoot(ShowBootSchema):
    """Parser for show boot"""

    cli_command = 'show boot'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        boot_dict = {}
        boot_variable = None

        for line in out.splitlines():
            line = line.strip()

            # Current Boot Variables:
            p1 = re.compile(r'Current +Boot +Variables:$')
            m = p1.match(line)
            if m:
                boot_variable = 'current'
                continue

            # Boot Variables on next reload:
            p1_2 = re.compile(r'Boot +Variables +on +next +reload:$')
            m = p1_2.match(line)
            if m:
                boot_variable = 'next'
                continue

            # BOOT variable = bootflash:/asr1000rpx.bin,12;
            # BOOT variable = flash:cat3k_caa-universalk9.BLD_POLARIS_DEV_LATEST_20150907_031219.bin;
            #                 flash:cat3k_caa-universalk9.BLD_POLARIS_DEV_LATEST_20150828_174328.SSA.bin;flash:ISSUCleanGolden;
            p1_1 = re.compile(r'^BOOT +variable +=( *(?P<var>\S+);)?$')
            m = p1_1.match(line)
            if m:
                boot = m.groupdict()['var']
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
            p2 = re.compile(r'^Standby +BOOT +variable +=( *(?P<var>\S+);)?$')
            m = p2.match(line)
            if m:
                if m.groupdict()['var']:
                    if 'standby' not in boot_dict:
                        boot_dict['standby'] = {}
                        boot_dict['standby']['boot_variable'] = m.groupdict()['var']
                continue

            # Configuration register is 0x2002
            p3 = re.compile(r'^Configuration +register +is +(?P<var>\w+)$')
            m = p3.match(line)
            if m:
                if 'active' not in boot_dict:
                    boot_dict['active'] = {}
                boot_dict['active']['configuration_register'] = m.groupdict()['var']
                continue

            # Standby Configuration register is 0x2002
            p4 = re.compile(r'^Standby +Configuration +register'
                             ' +is +(?P<var>\w+)$')
            m = p4.match(line)
            if m:
                if 'standby' not in boot_dict:
                    boot_dict['standby'] = {}
                boot_dict['standby']['configuration_register'] = m.groupdict()['var']
                continue

            # Manual Boot = yes
            p6 = re.compile(r'^Manual +Boot += +(?P<var>\w+)$')
            m = p6.match(line)
            if m:
                boot_dict['manual_boot'] = True if \
                    m.groupdict()['var'].lower() == 'yes' else\
                        False
                continue

            # Enable Break = yes
            p6 = re.compile(r'^Enable +Break += +(?P<var>\w+)$')
            m = p6.match(line)
            if m:
                boot_dict['enable_break'] = True if \
                    m.groupdict()['var'].lower() == 'yes' else\
                        False
                continue

            # Boot Mode = DEVICE
            p6 = re.compile(r'^Boot +Mode += +(?P<var>\w+)$')
            m = p6.match(line)
            if m:
                boot_dict['boot_mode'] = m.groupdict()['var'].lower()
                continue

            # iPXE Timeout = 0
            p6 = re.compile(r'^iPXE +Timeout += +(?P<var>\w+)$')
            m = p6.match(line)
            if m:
                boot_dict['ipxe_timeout'] = int(m.groupdict()['var'])
                continue
        return boot_dict


class ShowSwitchDetailSchema(MetaParser):
    """Schema for show switch detail"""
    schema = {
        'switch': {
            'mac_address': str,
            'mac_persistency_wait_time': str,
            'stack': {
                Any(): {
                    'role': str,
                    'mac_address': str,
                    'priority': str,
                    'hw_ver': str,
                    'state': str,
                    'ports': {
                        Any(): {
                            'stack_port_status': str,
                            'neighbors_num': int
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

    def cli(self,output=None):

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
        p1 = re.compile(r'^[Ss]witch\/[Ss]tack +[Mm]ac +[Aa]ddress +\: +'
                         '(?P<switch_mac_address>[\w\.]+) *(?P<local>[\w\s\-]+)?$')
        
        p2 = re.compile(r'^[Mm]ac +persistency +wait +time\: +'
                         '(?P<mac_persistency_wait_time>[\w\.\:]+)$')

        p3 = re.compile(r'^\*?(?P<switch>\d+) +(?P<role>\w+) +'
                         '(?P<mac_address>[\w\.]+) +'
                         '(?P<priority>\d+) +'
                         '(?P<hw_ver>\w+) +'
                         '(?P<state>[\w\s]+)$')

        p4 = re.compile(r'^(?P<switch>\d+) +(?P<status1>\w+) +'
                         '(?P<status2>\w+) +'
                         '(?P<nbr_num_1>\d+) +'
                         '(?P<nbr_num_2>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            # Switch/Stack Mac Address : 0057.d21b.cc00 - Local Mac Address
            m = p1.match(line)
            if m:
                ret_dict['mac_address'] = m.groupdict()['switch_mac_address']
                continue

            # Mac persistency wait time: Indefinite
            m = p2.match(line)
            if m:
                ret_dict['mac_persistency_wait_time'] = m.groupdict()['mac_persistency_wait_time'].lower()
                continue

            #                                              H/W   Current
            # Switch#   Role    Mac Address     Priority Version  State 
            # -----------------------------------------------------------
            # *1       Active   689c.e2d9.df00     3      V04     Ready 
            m = p3.match(line)
            if m:
                group = m.groupdict()
                stack = group['switch']
                match_dict = {k:v.lower() for k, v in group.items() if k in ['role', 'state']}
                match_dict.update({k:v for k, v in group.items() if k in ['priority', 'mac_address', 'hw_ver']})
                ret_dict.setdefault('stack', {}).setdefault(stack, {}).update(match_dict)
                continue


            #          Stack Port Status             Neighbors     
            # Switch#  Port 1     Port 2           Port 1   Port 2 
            # --------------------------------------------------------
            #   1         OK         OK               3        2 
            m = p4.match(line)
            if m:
                group = m.groupdict()
                stack = group['switch']
                stack_ports = ret_dict.setdefault('stack', {}).setdefault(stack, {}).setdefault('ports', {})
                for port in self.STACK_PORT_RANGE:
                    port_dict = stack_ports.setdefault(port, {})
                    port_dict['stack_port_status'] = group['status{}'.format(port)].lower()
                    port_dict['neighbors_num'] = int(group['nbr_num_{}'.format(port)])
                continue

        return {'switch': ret_dict} if ret_dict else {}


class ShowSwitchSchema(MetaParser):
    """Schema for show switch"""
    schema = {
        'switch': {
            'mac_address': str,
            'mac_persistency_wait_time': str,
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


# c3850
class ShowEnvironmentAllSchema(MetaParser):
    """Schema for show environment all"""
    schema = {
        'switch': {
            Any(): {
                'fan': {
                    Any(): {
                        'state': str,
                    }
                },
                'power_supply': {
                    Any(): {
                        'state': str,
                        Optional('pid'): str,
                        Optional('serial_number'): str,
                        'status': str,
                        Optional('system_power'): str,
                        Optional('poe_power'): str,
                        Optional('watts'): str
                    }
                },
                'system_temperature_state': str,
                'inlet_temperature':{
                    'value': str,
                    'state': str,
                    'yellow_threshold': str,
                    'red_threshold': str
                },
                'hotspot_temperature':{
                    'value': str,
                    'state': str,
                    'yellow_threshold': str,
                    'red_threshold': str
                }
            }
        },
    }


class ShowEnvironmentAll(ShowEnvironmentAllSchema):
    """Parser for show environment all"""
    PS_MAPPING = {'A': '1', 'B': '2'}

    cli_command = 'show environment all'

    def cli(self,output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern
        p1 = re.compile(r'^Switch +(?P<switch>\d+) +FAN +(?P<fan>\d+) +is +(?P<state>[\w\s]+)$')

        p2 = re.compile(r'^FAN +PS\-(?P<ps>\d+) +is +(?P<state>[\w\s]+)$')

        p3 = re.compile(r'^Switch +(?P<switch>\d+): +SYSTEM +TEMPERATURE +is +(?P<state>[\w\s]+)$')

        p4 = re.compile(r'^(?P<type>\w+) +Temperature +Value: +(?P<temperature>\d+) +Degree +Celsius$')

        p5 = re.compile(r'^Temperature +State: +(?P<state>\w+)$')

        p6 = re.compile(r'^(?P<color>\w+) +Threshold *: +(?P<temperature>\d+) +Degree +Celsius$')

        p7 = re.compile(r'^(?P<sw>\d+)(?P<ps>\w+) *'
                         '((?P<pid>[\w\-]+) +'
                         '(?P<serial_number>\w+) +)?'
                         '(?P<status>(\w+|Not Present)) *'
                         '((?P<system_power>\w+) +'
                         '(?P<poe_power>[\w\/]+) +'
                         '(?P<watts>\w+))?$')

        for line in out.splitlines():
            line = line.strip()

            # Switch 1 FAN 1 is OK
            m = p1.match(line)
            if m:
                group = m.groupdict()
                switch = group['switch']
                fan = group['fan']
                root_dict = ret_dict.setdefault('switch', {}).setdefault(switch, {})
                root_dict.setdefault('fan', {}).setdefault(fan, {}).setdefault('state', group['state'].lower())
                continue
                
            # FAN PS-1 is OK
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ps = group['ps']
                power_supply_dict = root_dict.setdefault('power_supply', {}).setdefault(ps, {})
                power_supply_dict.setdefault('state', group['state'].lower())
                continue

            # Switch 1: SYSTEM TEMPERATURE is OK
            m = p3.match(line)
            if m:
                group = m.groupdict()
                switch = group['switch']
                root_dict = ret_dict.setdefault('switch', {}).setdefault(switch, {})
                root_dict['system_temperature_state'] = group['state'].lower()
                continue

            # Inlet Temperature Value: 34 Degree Celsius
            # Hotspot Temperature Value: 45 Degree Celsius
            m = p4.match(line)
            if m:
                group = m.groupdict()
                temp_type = group['type'].lower() + '_temperature'
                temp_dict = root_dict.setdefault(temp_type, {})
                temp_dict['value'] = group['temperature']
                continue

            # Temperature State: GREEN
            m = p5.match(line)
            if m:
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

            # SW  PID                 Serial#     Status           Sys Pwr  PoE Pwr  Watts
            # --  ------------------  ----------  ---------------  -------  -------  -----
            # 1A  PWR-C1-715WAC       DCB1844G1ZY  OK              Good     Good     715 
            # 1B  Not Present
            m = p7.match(line)
            if m:
                group = m.groupdict()
                switch = group.pop('sw')
                ps = self.PS_MAPPING[group.pop('ps')]
                root_dict = ret_dict.setdefault('switch', {}).setdefault(switch, {})
                power_supply_dict = root_dict.setdefault('power_supply', {}).setdefault(ps, {})
                power_supply_dict.update(
                       {k:v for k, v in group.items() if k in ['pid', 'serial_number', 'watts'] and v})
                power_supply_dict.update(
                       {k:v.lower() for k, v in group.items() \
                           if k in ['status', 'system_power', 'poe_power'] and v})
                continue
        return ret_dict


class ShowModuleSchema(MetaParser):
    """Schema for show module"""
    schema = {
        'switch': {
            Any(): {
                'port': str,
                'model': str,
                'serial_number': str,
                'mac_address': str,
                'hw_ver': str,
                'sw_ver': str
            },
        }
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

        for line in out.splitlines():
            line = line.strip()

            # Switch  Ports    Model                Serial No.   MAC address     Hw Ver.       Sw Ver. 
            # ------  -----   ---------             -----------  --------------  -------       --------
            #  1       56     WS-C3850-48P-E        FOC1902X062  689c.e2d9.df00  V04           16.9.1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                switch = group.pop('switch')
                switch_dict = ret_dict.setdefault('switch', {}).setdefault(switch, {})
                switch_dict.update(
                       {k:v.lower() for k, v in group.items()})
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
                name_dict.update({k:int(v) for k, v in group.items()})
                continue

            # KiB Swap:        0 total,        0 free,        0 used.  1778776 avail Mem
            m = p2.match(line)
            if m:
                group = m.groupdict()
                name_dict = ret_dict.setdefault('swap', {})
                name_dict.update({k:int(v) for k, v in group.items()})
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
                         '(?P<total>\d+) +(?P<used>\d+) +\((?P<used_percentage>\d+)\%\) +'
                         '(?P<free>\d+) +\((?P<free_percentage>\d+)\%\) +'
                         '(?P<committed>\d+) +\((?P<committed_percentage>\d+)\%\)$')

        p3 = re.compile(r'^(?P<slot>\S+)? *(?P<cpu>\d+) +'
                         '(?P<user>[\d\.]+) +(?P<system>[\d\.]+) +'
                         '(?P<nice_process>[\d\.]+) +(?P<idle>[\d\.]+) +'
                         '(?P<irq>[\d\.]+) +(?P<sirq>[\d\.]+) +'
                         '(?P<waiting>[\d\.]+)$')

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
                mem_dict.update({k:int(v) for k, v in group.items()})
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
                cpu_dict.update({k:float(v) for k, v in group.items()})
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
                ret_dict.update({k:int(v) for k, v in m.groupdict().items()})
                continue

            # PID Runtime(ms)     Invoked      uSecs   5Sec   1Min   5Min TTY Process 
            # 539     6061647    89951558         67  0.31%  0.36%  0.38%   0 HSRP Common 
            m = p2.match(line)
            if m:
                group = m.groupdict()
                index += 1
                sort_dict = ret_dict.setdefault('sort', {}).setdefault(index, {})
                sort_dict['process'] = group['process']
                sort_dict.update({k:int(v) for k, v in group.items() 
                    if k in ['runtime', 'invoked', 'usecs', 'tty', 'pid']})
                sort_dict.update({k:float(v) for k, v in group.items() 
                    if k in ['five_sec_cpu', 'one_min_cpu', 'five_min_cpu']})
                if float(group['five_sec_cpu']) or \
                   float(group['one_min_cpu']) or \
                   float(group['five_min_cpu']):
                    nonzero_cpu_processes.append(group['process'])
                else:
                    zero_cpu_processes.append(group['process'])
                continue

        ret_dict.setdefault('zero_cpu_processes', zero_cpu_processes) if zero_cpu_processes else None
        ret_dict.setdefault('nonzero_cpu_processes', nonzero_cpu_processes) if nonzero_cpu_processes else None
        return ret_dict


class ShowProcessesCpuPlatformSchema(MetaParser):
    """Schema for show processes cpu platform"""
    schema = {
        'cpu_utilization': {
            'cpu_util_five_secs': str,
            'cpu_util_one_min': str,
            'cpu_util_five_min': str,
            'core': {
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
                ret_dict['cpu_utilization'].update({k:str(v) for k, v in group.items()})
                continue

            # Core 0: CPU utilization for five seconds:  2%, one minute:  8%, five minutes: 18%
            m = p2.match(line)
            if m:
                group = m.groupdict()
                core = group.pop('core')
                if 'cpu_utilization' not in ret_dict:
                    ret_dict.setdefault('cpu_utilization', {})
                ret_dict['cpu_utilization'].setdefault('core', {}).setdefault(core, {})
                ret_dict['cpu_utilization']['core'][core].update({k:str(v) for k, v in group.items()})
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
    """Schema for show environment"""

    schema = {
        'critical_larams': int,
        'major_alarms': int,
        'minor_alarms': int,
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
    """Parser for show environment"""

    cli_command = 'show environment'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        p1 = re.compile(r'^Number +of +Critical +alarms: +(?P<critic_larams>\d+)$')

        p2 = re.compile(r'^Number +of +Major +alarms: +(?P<maj_alarms>\d+)$')

        p3 = re.compile(r'^Number +of +Minor +alarms: +(?P<min_alarms>\d+)$')

        p4 = re.compile(r'^(?P<slot>([\w\d]+)) +(?P<sensor_name>([\w\d\:]+( [\w]+( [\w]+)?)?))'
                         ' +(?P<state>([\w]+ [\w]+ [\d%]+)|([\w]+)) +(?P<reading>[\w\d\s]+)$')

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
                fin_dict.update({k:str(v) for k, v in group.items()})
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

                ret_dict['rp'][rp]['slot'][rp_slot]['package'].setdefault(
                    package_name, {})
                ret_dict['rp'][rp]['slot'][rp_slot]['package'][package_name]\
                    ['version'] = version
                ret_dict['rp'][rp]['slot'][rp_slot]['package'][package_name]\
                    ['status'] = status
                ret_dict['rp'][rp]['slot'][rp_slot]['package'][package_name]\
                    ['file'] = file
                continue

            m = p3.match(line)
            if m:
                # Safer, return empty dictionary instead of an error
                if not package_name or not rp_slot:
                    return ret_dict

                group = m.groupdict()
                built_time = group['built_time']

                ret_dict['rp'][rp]['slot'][rp_slot]['package']\
                    [package_name]['built_time'] = built_time
                ret_dict['rp'][rp]['slot'][rp_slot]['package']\
                    [package_name]['built_by'] = group['built_by']
                continue

            m = p4.match(line)
            if m:
                # Safer, return empty dictionary instead of an error
                if not package_name or not rp_slot:
                    return ret_dict
                group = m.groupdict()
                ret_dict['rp'][rp]['slot'][rp_slot]['package']\
                    [package_name]['file_sha1_checksum'] = group['file_sha1_checksum']
                continue

        return ret_dict


class ShowPlatformHardwareSchema(MetaParser):
    """Schema for show platform hardware qfp active infrastructure bqs queue output default all"""

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
                        'qlimit_bytes': int,
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
                        'defer_obj_refcnt': int,
                    },
                    'statistics': {
                        'tail_drops_bytes': int,
                        'tail_drops_packets': int,
                        'total_enqs_bytes': int,
                        'total_enqs_packets': int,
                        'queue_depth_bytes': int,
                        'lic_throughput_oversub_drops_bytes': int,
                        'lic_throughput_oversub_drops_packets': int,
                    }
                },
            }
        },
    }


class ShowPlatformHardware(ShowPlatformHardwareSchema):
    """Parser for show platform hardware qfp active infrastructure bqs queue output default all"""

    cli_command = 'show platform hardware qfp active infrastructure bqs queue output default all'

    def cli(self, output=None):

        if output is None:
            out = self.device.execute(self.cli_command)
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
        p3_1 = re.compile(r'^Software Control Info:$')

        #       (cache) queue id: 0x000000a6, wred: 0x88b16ac2, qlimit (bytes): 3281312
        p3_2 = re.compile(r'^\(cache\) +queue +id: +(?P<cache_queue_id>[\w\d]+),'
                         ' +wred: +(?P<wred>[\w\d]+),'
                         ' +qlimit +\(bytes\): +(?P<qlimit_bytes>\d+)$')

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
        p12 = re.compile(r'^defer_obj_refcnt: +(?P<defer_obj_refcnt>\d+)$')  

        #     Statistics:
        p13_1 = re.compile(r'^Statistics:$')  

        #       tail drops  (bytes): 0                   ,          (packets): 0   
        p13_2 = re.compile(r'^tail +drops  +\(bytes\): +(?P<tail_drops_bytes>\d+) +,'
                         ' +\(packets\): +(?P<tail_drops_packets>\d+)$')  

        #       total enqs  (bytes): 0                   ,          (packets): 0   
        p14 = re.compile(r'^total +enqs  +\(bytes\): +(?P<total_enqs_bytes>\d+) +,'
                         ' +\(packets\): +(?P<total_enqs_packets>\d+)$')  

        #       queue_depth (bytes): 0    
        p15 = re.compile(r'^queue_depth +\(bytes\): +(?P<queue_depth_bytes>\d+)$')  

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
                ret_dict[interface]['index'][index].setdefault(
                    'software_control_info', {})
                continue

            m = p3_2.match(line)
            if m:
                group = m.groupdict()
                ret_dict[interface]['index'][index]['software_control_info']\
                    ['cache_queue_id'] = group['cache_queue_id']
                ret_dict[interface]['index'][index]['software_control_info']\
                    ['wred'] = group['wred']
                ret_dict[interface]['index'][index]['software_control_info']\
                    ['qlimit_bytes'] = int(group['qlimit_bytes'])
                continue

            m = p4.match(line)
            if m:
                group = m.groupdict()
                ret_dict[interface]['index'][index]['software_control_info'].\
                    update({k:v for k, v in group.items()})
                continue

            m = p5.match(line)
            if m:
                group = m.groupdict()
                ret_dict[interface]['index'][index]['software_control_info']\
                    ['sw_flags'] = group['sw_flags']
                ret_dict[interface]['index'][index]['software_control_info']\
                    ['sw_state'] = group['sw_state']
                ret_dict[interface]['index'][index]['software_control_info']\
                    ['port_uidb'] = int(group['port_uidb'])
                continue

            m = p6.match(line)
            if m:
                group = m.groupdict()
                ret_dict[interface]['index'][index]['software_control_info'].\
                    update({k:int(v) for k, v in group.items()})
                continue
   
            m = p7.match(line)
            if m:
                group = m.groupdict()
                ret_dict[interface]['index'][index]['software_control_info'].\
                    update({k:int(v) for k, v in group.items()})
                continue

            m = p8.match(line)
            if m:
                group = m.groupdict()
                ret_dict[interface]['index'][index]['software_control_info'].\
                    update({k:int(v) for k, v in group.items()})
                continue

            m = p9.match(line)
            if m:
                group = m.groupdict()
                ret_dict[interface]['index'][index]['software_control_info'].\
                    update({k:int(v) for k, v in group.items()})
                continue

            m = p10.match(line)
            if m:
                group = m.groupdict()
                ret_dict[interface]['index'][index]['software_control_info']\
                    ['share'] = int(group['share'])
                continue

            m = p11.match(line)
            if m:
                group = m.groupdict()
                ret_dict[interface]['index'][index]['software_control_info'].\
                    update({k:int(v) for k, v in group.items()})
                continue

            m = p12.match(line)
            if m:
                group = m.groupdict()
                ret_dict[interface]['index'][index]['software_control_info']\
                    ['defer_obj_refcnt'] = int(group['defer_obj_refcnt'])
                continue

            m = p13_1.match(line)
            if m:
                ret_dict[interface]['index'][index].setdefault('statistics', {})

            m = p13_2.match(line)
            if m:
                group = m.groupdict()
                ret_dict[interface]['index'][index]['statistics'].update(
                    {k:int(v) for k, v in group.items()})
                continue
    
            m = p14.match(line)
            if m:
                group = m.groupdict()
                ret_dict[interface]['index'][index]['statistics'].update(
                    {k:int(v) for k, v in group.items()})
                continue
               
            m = p15.match(line)
            if m:
                group = m.groupdict()
                ret_dict[interface]['index'][index]['statistics']\
                    ['queue_depth_bytes'] = int(group['queue_depth_bytes'])
                continue

            m = p16.match(line)
            if m:
                group = m.groupdict()
                ret_dict[interface]['index'][index]['statistics'].update(
                    {k:int(v) for k, v in group.items()})
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
                    ret_dict['port'][port]['received'][low_high]\
                        ['pkts'] = int(group['rx_total_pkts'])
                    ret_dict['port'][port]['received'][low_high]\
                        ['bytes'] = int(group['rx_total_bytes'])
                else:
                    if 'received' not in ret_dict['slot'][slot]['subslot'][subslot]:
                        ret_dict['slot'][slot]['subslot'][subslot].\
                            setdefault('received', {})
                    ret_dict['slot'][slot]['subslot'][subslot]\
                        ['received']['pkts'] = int(group['rx_total_pkts'])
                    ret_dict['slot'][slot]['subslot'][subslot]\
                        ['received']['bytes'] = int(group['rx_total_bytes'])
                continue

            m = p4.match(line)
            if m:
                group = m.groupdict()
                ret_dict['port'][port]['received'][low_high]\
                    ['dropped_pkts'] = int(group['rx_dropped_pkts'])
                ret_dict['port'][port]['received'][low_high]\
                    ['dropped_bytes'] = int(group['rx_dropped_bytes'])
                continue

            m = p5.match(line)
            if m:
                group = m.groupdict()
                ret_dict['port'][port]['received'][low_high]\
                    ['errored_pkts'] = int(group['rx_errored_pkts'])
                ret_dict['port'][port]['received'][low_high]\
                    ['errored_bytes'] = int(group['rx_errored_bytes'])
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
                    ret_dict['port'][port]['transmitted'][low_high]\
                        ['pkts'] = int(group['tx_total_pkts'])
                    ret_dict['port'][port]['transmitted'][low_high]\
                        ['bytes'] = int(group['tx_total_bytes'])
                else:
                    if 'transmitted' not in ret_dict['slot'][slot]['subslot'][subslot]:
                        ret_dict['slot'][slot]['subslot'][subslot].setdefault(
                            'transmitted', {})
                    ret_dict['slot'][slot]['subslot'][subslot]['transmitted']\
                        ['pkts'] = int(group['tx_total_pkts'])
                    ret_dict['slot'][slot]['subslot'][subslot]['transmitted']\
                        ['bytes'] = int(group['tx_total_bytes'])
                continue
  
            m = p8.match(line)
            if m:
                group = m.groupdict()
                ret_dict['port'][port]['transmitted'][low_high]\
                    ['dropped_pkts'] = int(group['tx_dropped_pkts'])
                ret_dict['port'][port]['transmitted'][low_high]\
                    ['dropped_bytes'] = int(group['tx_dropped_bytes'])
                continue

            m = p9.match(line)
            if m:
                group = m.groupdict()
                slot = group['slot']
                subslot = group['subslot']
                ret_dict.setdefault('slot', {}).setdefault(slot, {})
                if 'subslot' not in ret_dict['slot'][slot]:
                    ret_dict['slot'][slot].setdefault('subslot', {})
                ret_dict['slot'][slot]['subslot'].setdefault(subslot,{})
                ret_dict['slot'][slot]['subslot'][subslot]['name'] = \
                    group['name']
                ret_dict['slot'][slot]['subslot'][subslot]['status'] = \
                    group['status']
                continue

            m = p10.match(line)
            if m:
                group = m.groupdict()
                if 'received' not in ret_dict['slot'][slot]['subslot'][subslot]:
                    ret_dict['slot'][slot]['subslot'][subslot].setdefault(
                        'received', {})
                ret_dict['slot'][slot]['subslot'][subslot]['received']\
                    ['ipc_pkts'] = int(group['rx_ipc_pkts'])
                ret_dict['slot'][slot]['subslot'][subslot]['received']\
                    ['ipc_bytes'] = int(group['rx_ipc_bytes'])
                continue

            m = p11.match(line)
            if m:
                group = m.groupdict()
                if 'transmitted' not in ret_dict['slot'][slot]['subslot'][subslot]:
                    ret_dict['slot'][slot]['subslot'][subslot].setdefault(
                        'transmitted', {})
                ret_dict['slot'][slot]['subslot'][subslot]['transmitted']\
                    ['ipc_pkts'] = int(group['tx_ipc_pkts'])
                ret_dict['slot'][slot]['subslot'][subslot]['transmitted']\
                    ['ipc_bytes'] = int(group['tx_ipc_bytes'])
                continue

            m = p12.match(line)
            if m:
                group = m.groupdict()
                ret_dict['slot'][slot]['subslot'][subslot].setdefault(
                    'received', {})
                ret_dict['slot'][slot]['subslot'][subslot]['received']\
                    ['ipc_err'] = int(group['rx_ipc_err'])
                continue

            m = p13.match(line)
            if m:
                group = m.groupdict()
                ret_dict['slot'][slot]['subslot'][subslot].setdefault(
                    'transmitted', {})
                ret_dict['slot'][slot]['subslot'][subslot]['transmitted']\
                    ['ipc_err'] = int(group['tx_ipc_err'])
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
                ret_dict['slot'][slot]['subslot'][subslot][new_direction]\
                    ['spi4_interrupt_counters']['out_of_frame'] = int(group['out_of_frame'])
                continue

            m = p16.match(line)
            if m:
                group = m.groupdict()
                ret_dict['slot'][slot]['subslot'][subslot][new_direction]\
                    ['spi4_interrupt_counters']['dip4_error'] = int(group['rx_dip4_error'])
                continue

            m = p17.match(line)
            if m:
                group = m.groupdict()
                ret_dict['slot'][slot]['subslot'][subslot][new_direction]\
                    ['spi4_interrupt_counters']['disabled'] = int(group['rx_disbaled'])
                continue

            m = p18.match(line)
            if m:
                group = m.groupdict()
                ret_dict['slot'][slot]['subslot'][subslot][new_direction]\
                    ['spi4_interrupt_counters']['loss_of_sync'] = int(group['rx_loss_of_sync'])
                continue

            m = p19.match(line)
            if m:
                group = m.groupdict()
                ret_dict['slot'][slot]['subslot'][subslot][new_direction]\
                    ['spi4_interrupt_counters']['sequence_error'] = int(group['rx_sequence_error'])
                continue

            m = p20.match(line)
            if m:
                group = m.groupdict()
                ret_dict['slot'][slot]['subslot'][subslot][new_direction]\
                    ['spi4_interrupt_counters']['burst_error'] = int(group['rx_burst_error'])
                continue

            m = p21.match(line)
            if m:
                group = m.groupdict()
                ret_dict['slot'][slot]['subslot'][subslot][new_direction]\
                    ['spi4_interrupt_counters']['eop_abort'] = int(group['rx_eop_abort'])
                continue

            m = p22.match(line)
            if m:
                group = m.groupdict()
                ret_dict['slot'][slot]['subslot'][subslot][new_direction]\
                    ['spi4_interrupt_counters']['packet_gap_error'] = int(group['rx_packet_gap_error'])
                continue

            m = p23.match(line)
            if m:
                group = m.groupdict()
                ret_dict['slot'][slot]['subslot'][subslot][new_direction]\
                    ['spi4_interrupt_counters']['control_word_error'] = int(group['rx_control_word_error'])
                continue

            m = p24.match(line)
            if m:
                group = m.groupdict()
                ret_dict['slot'][slot]['subslot'][subslot][new_direction]\
                    ['spi4_interrupt_counters']['frame_error'] = int(group['tx_frame_error'])
                continue

            m = p25.match(line)
            if m:
                group = m.groupdict()
                ret_dict['slot'][slot]['subslot'][subslot][new_direction]\
                    ['spi4_interrupt_counters']['fifo_over_flow'] = int(group['tx_fifo_over_flow'])
                continue

            m = p26.match(line)
            if m:
                group = m.groupdict()
                ret_dict['slot'][slot]['subslot'][subslot][new_direction]\
                    ['spi4_interrupt_counters']['dip2_error'] = int(group['tx_dip2_error'])
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
                final_dict.update({'interface':group['interface'].strip()})
                final_dict.update({'name':group['name'].strip()})
                final_dict.update({'logical_channel':int(group['logical_channel'])})
                final_dict.update({'drain_mode':drained})
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                unmapped_number = group['unmapped_number']
                if 'channel' not in ret_dict:
                    ret_dict.setdefault('channel', {})
                ret_dict['channel'].setdefault(unmapped_number, {})
                ret_dict['channel'][unmapped_number].update({'name':'unmapped'})
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
                final_dict.update({'interface':group['interface'].strip()})
                final_dict.update({'name':group['name'].strip()})
                final_dict.update({'port':int(group['port'])})
                final_dict.update({'cfifo':int(group['cfifo'])})
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                unmapped_number = group['unmapped_number']
                if 'channel' not in ret_dict:
                    ret_dict.setdefault('channel', {})
                ret_dict['channel'].setdefault(unmapped_number, {})
                ret_dict['channel'][unmapped_number].update({'name':'unmapped'})
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
                Optional('errors'):{
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
        Optional('serdes_exception_counts'):{
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
                    to_dict= ret_dict['link'][slot].setdefault('to', {}).setdefault('pkts', {})
                    to_dict.update({k:int(v) for k, v in group.items() if v})
                    continue

                pkts_dict = ret_dict['link'][slot]['from'].setdefault('pkts', {})
                pkts_dict.update({k:int(v) for k, v in group.items()})
                continue

            m = p3.match(line)
            if m:
                group = m.groupdict()
                bytes_dict = ret_dict['link'][slot]['from'].setdefault('bytes', {})
                bytes_dict.update({k:int(v) for k, v in group.items()})
                continue

            m = p4.match(line)
            if m:
                group = m.groupdict()
                pkts_dict.update({k:int(v) for k, v in group.items()})
                continue

            m = p5.match(line)
            if m:
                group = m.groupdict()
                bytes_dict.update({k:int(v) for k, v in group.items()})
                continue

            m = p6.match(line)
            if m:
                group = m.groupdict()
                from_dict.update({k:int(v) for k, v in group.items()})
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
                new_dict['errors'].update({k:int(v) for k, v in group.items()})
                continue

            m = p10.match(line)
            if m:
                group = m.groupdict()
                if 'errors' in ret_dict['link'][link]:
                    new_dict['errors'].update({k:int(v) for k, v in group.items()})
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
        'slot':{
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

    def cli(self,output=None):

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
                slot_dict = ret_dict.setdefault('slot', {}).setdefault(slot,{})
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
                slot_dict = ret_dict.setdefault('slot', {}).setdefault(slot,{})
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
        'channel':{
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
            cmd = self.cli_command.format(status=status, slot=slot, iotype=iotype)
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
                chan_dict.update({k:v for k, v in group.items()})
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
                final_dict.update({'interface':group['interface'].strip()})
                final_dict.update({'name':group['name'].strip()})
                final_dict.update({'logical_channel':int(group['logical_channel'])})
                final_dict.update({'drain_mode':drained})
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                unmapped_number = group['unmapped_number']
                if 'channel' not in ret_dict:
                    ret_dict.setdefault('channel', {})
                ret_dict['channel'].setdefault(unmapped_number, {})
                ret_dict['channel'][unmapped_number].update({'name':'unmapped'})
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
                final_dict.update({'interface':group['interface'].strip()})
                final_dict.update({'name':group['name'].strip()})
                final_dict.update({'port':int(group['port'])})
                final_dict.update({'cfifo':int(group['cfifo'])})
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                unmapped_number = group['unmapped_number']
                if 'channel' not in ret_dict:
                    ret_dict.setdefault('channel', {})
                ret_dict['channel'].setdefault(unmapped_number, {})
                ret_dict['channel'][unmapped_number].update({'name':'unmapped'})
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
        'global_drop_stats':{
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
                stats_dict.update({k:int(v) for k, v in group.items()})
                continue

        return ret_dict


class ShowProcessesCpuHistorySchema(MetaParser):
    """Schema for show processes cpu history"""

    schema = {
        '60s':{
            Any(): {
                'maximum': int,
                Optional('average'): int,
            },
        },
        '60m':{
            Any(): {
                'maximum': int,
                Optional('average'): int,
            },
        },
        '72h':{
            Any(): {
                'maximum': int,
                Optional('average'): int,
            },
        },
    }


class ShowProcessesCpuHistory(ShowProcessesCpuHistorySchema):
    """Parser for show processes cpu history"""
    
    cli_command = 'show processes cpu history'

    def cli(self, output=None):

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        #           888886666611111                    11111          
        # 777775555599999666664444466666333335555544444666667777777777
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
                    if v is ' ':
                        pass
                    else:
                        tmp[i] += v
            else:
                if count == 0:
                    sub_dict = ret_dict.setdefault('60s', {})
                    for i in range(60):
                        sub_dict.setdefault(i + 1, {}).update({'maximum': int(tmp[i]) if tmp[i] is not '' else 0})

                elif count == 1:
                    sub_dict = ret_dict.setdefault('60m', {})
                    for i in range(60):
                        sub_dict.setdefault(i + 1, {}).update({'maximum': int(tmp[i]) if tmp[i] is not '' else 0})

                else:
                    sub_dict = ret_dict.setdefault('72h', {})
                    for i in range(72):
                        sub_dict.setdefault(i + 1, {}).update({'maximum': int(tmp[i]) if tmp[i] is not '' else 0})
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