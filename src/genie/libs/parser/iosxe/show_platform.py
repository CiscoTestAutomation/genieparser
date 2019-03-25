"""show_platform.py

"""
import re
import logging

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                         Any, \
                                         Optional, \
                                         Or, \
                                         And, \
                                         Default, \
                                         Use
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
                    'chassis': str,
                    'processor_type': str,
                    Optional('chassis_sn'): str,
                    'rtr_type': str,
                    'os': str,
                    'curr_config_register': str,
                    Optional('next_config_register'): str,
                    'main_mem': str,
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

            p1_1 = re.compile(
                r'^\s*[Cc]isco +IOS +[Ss]oftware(.+)?, +(?P<platform>.+) '
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


class ShowInventorySchema(MetaParser):
    """Schema for show inventory"""
    schema = {
                Optional('main'): {
                    Optional('swstack'): bool,
                    Optional('chassis'): {
                        Any(): {
                            Optional('name'): str,
                            Optional('descr'): str,
                            Optional('pid'): str,
                            Optional('vid'): str,
                            Optional('sn'): str,
                        }
                    }
                },
                'slot': {
                    Any(): {
                        Optional('rp'): {
                            Any(): {
                                Optional('name'): str,
                                Optional('descr'): str,
                                Optional('pid'): str,
                                Optional('vid'): str,
                                Optional('sn'): str,
                                Optional('swstack_power'): str,
                                Optional('swstack_power_sn'): str,
                                Optional('subslot'): {
                                    Any(): {
                                        Any(): {
                                            Optional('name'): str,
                                            Optional('descr'): str,
                                            Optional('pid'): str,
                                            Optional('vid'): str,
                                            Optional('sn'): str,
                                        }
                                    }
                                }
                            }
                        },
                        Optional('lc'): {
                            Any(): {
                                Optional('name'): str,
                                Optional('descr'): str,
                                Optional('pid'): str,
                                Optional('vid'): str,
                                Optional('sn'): str,
                                Optional('subslot'): {
                                    Any(): {
                                        Any(): {
                                            Optional('name'): str,
                                            Optional('descr'): str,
                                            Optional('pid'): str,
                                            Optional('vid'): str,
                                            Optional('sn'): str,
                                        }
                                    }
                                }
                            }
                        },
                        Optional('other'): {
                            Any(): {
                                Optional('name'): str,
                                Optional('descr'): str,
                                Optional('pid'): str,
                                Optional('vid'): str,
                                Optional('sn'): str
                            }
                        }
                    }
                }
            }


class ShowInventory(ShowInventorySchema):
    """Parser for show Inventory
    parser class - implements detail parsing mechanisms for cli output.
    """
    # *************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).
    cli_command = 'show inventory'

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

        name = descr = slot = subslot = pid = ''
        inventory_dict = {}
        for line in out.splitlines():
            line = line.strip()

            # check 1st line and get slot number
            # NAME: "subslot 0/0 transceiver 2", DESCR: "GE T"
            # NAME: "NIM subslot 0/0", DESCR: "Front Panel 3 ports Gigabitethernet Module"
            p1 = re.compile(r'^\s*NAME\:\s+\"(?P<name>.*)\",\s+DESCR\:\s+\"(?P<descr>.*)\"')
            m = p1.match(line)
            if m:
                name = m.groupdict()['name']
                descr = m.groupdict()['descr']
                p1_2 = re.compile(r'\s*\S+[ t](?P<slot>[a-zA-Z]*\d+)[ /]*')
                m = p1_2.match(name)
                if m:
                    slot = m.groupdict()['slot']
                    if 'slot' not in inventory_dict:
                        inventory_dict['slot'] = {}
                    if slot not in inventory_dict['slot']:
                        inventory_dict['slot'][slot] = {}

                p1_2 = re.compile(r'SPA subslot (?P<slot>\d+)/(?P<subslot>\d+)')
                m = p1_2.match(name)
                if m:
                    slot = m.groupdict()['slot']
                    subslot = m.groupdict()['subslot']
                    if 'slot' not in inventory_dict:
                        inventory_dict['slot'] = {}
                    if slot not in inventory_dict['slot']:
                        inventory_dict['slot'][slot] = {}

                if 'Power Supply Module' in name:
                    slot = name.replace('Power Supply Module ', 'P')
                    if 'slot' not in inventory_dict:
                        inventory_dict['slot'] = {}
                    if slot not in inventory_dict['slot']:
                        inventory_dict['slot'][slot] = {}

                p1_3 = re.compile(r'\s*\S+ *\d+[ /]*(?P<subslot>\d+.*)$')
                m = p1_3.match(name)
                if m:
                    subslot = m.groupdict()['subslot']
                continue

            # check 2nd line

            # PID: SFP-GE-T            , VID: V02  , SN: MTC2139029X
            # PID: ISR4331-3x1GE     , VID: V01  , SN:
            # PID: ISR4331/K9        , VID:   , SN: FDO21520TGH
            # PID: ISR4331/K9        , VID:      , SN:
            p2 = re.compile(r'^\s*PID: +(?P<pid>\S+) +, +VID: +((?P<vid>\S+) +)?, +SN:( +(?P<sn>.*))?$')
            m = p2.match(line)
            if m:
                if 'WS-C' in pid:
                    old_pid = pid
                pid = m.groupdict()['pid']
                vid = m.groupdict()['vid'] or ''
                sn = m.groupdict()['sn'] or ''
                if name:
                    if 'STACK' in pid:
                        inventory_dict['main'] = {}
                        inventory_dict['main']['swstack'] = True
                    if pid and ('Chassis' in name):
                        inventory_dict['main'] = {}
                        inventory_dict['main']['chassis'] = {}
                        inventory_dict['main']['chassis'][pid] = {}
                        inventory_dict['main']['chassis'][pid]['name'] = name
                        inventory_dict['main']['chassis'][pid]['descr'] = descr
                        inventory_dict['main']['chassis'][pid]['pid'] = pid
                        inventory_dict['main']['chassis'][pid]['vid'] = vid
                        inventory_dict['main']['chassis'][pid]['sn'] = sn
                    if slot:
                        if 'WS-C' in pid or 'RP' in pid:
                            if 'rp' not in inventory_dict['slot'][slot]:
                                inventory_dict['slot'][slot]['rp'] = {}
                                if pid not in inventory_dict['slot'][slot]['rp']:
                                    inventory_dict['slot'][slot]['rp'][pid] = {}
                                    if 'PWR' in pid:
                                        inventory_dict['slot'][slot]['rp'][pid][swstack_power] = pid
                                        inventory_dict['slot'][slot]['rp'][pid][swstack_power_sn] = sn
                                    else:
                                        inventory_dict['slot'][slot]['rp'][pid]['name'] = name
                                        inventory_dict['slot'][slot]['rp'][pid]['descr'] = descr
                                        inventory_dict['slot'][slot]['rp'][pid]['pid'] = pid
                                        inventory_dict['slot'][slot]['rp'][pid]['vid'] = vid
                                        inventory_dict['slot'][slot]['rp'][pid]['sn'] = sn
                        elif 'SIP' in pid or 'ISR' in pid:
                            if 'lc' not in inventory_dict['slot'][slot]:
                                inventory_dict['slot'][slot]['lc'] = {}
                                if pid not in inventory_dict['slot'][slot]['lc']:
                                    inventory_dict['slot'][slot]['lc'][pid] = {}
                                    inventory_dict['slot'][slot]['lc'][pid]['name'] = name
                                    inventory_dict['slot'][slot]['lc'][pid]['descr'] = descr
                                    inventory_dict['slot'][slot]['lc'][pid]['pid'] = pid
                                    inventory_dict['slot'][slot]['lc'][pid]['vid'] = vid
                                    inventory_dict['slot'][slot]['lc'][pid]['sn'] = sn
                                    mod = pid
                        elif ('STACK' in pid) and subslot:
                            if 'rp' not in inventory_dict['slot'][slot]:
                                inventory_dict['slot'][slot]['rp'] = {}
                            if old_pid not in inventory_dict['slot'][slot]['rp']:
                                inventory_dict['slot'][slot]['rp'][old_pid] = {}
                            if 'subslot' not in inventory_dict['slot'][slot]['rp'][old_pid]:
                                inventory_dict['slot'][slot]['rp'][old_pid]['subslot'] = {}
                            if subslot not in inventory_dict['slot'][slot]['rp'][old_pid]['subslot']:
                                inventory_dict['slot'][slot]['rp'][old_pid]['subslot'][subslot] = {}
                            if pid not in inventory_dict['slot'][slot]['rp'][old_pid]['subslot'][subslot]:
                                inventory_dict['slot'][slot]['rp'][old_pid]['subslot'][subslot][pid] = {}
                            inventory_dict['slot'][slot]['rp'][old_pid]['subslot'][subslot][pid]['name'] = name
                            inventory_dict['slot'][slot]['rp'][old_pid]['subslot'][subslot][pid]['descr'] = descr
                            inventory_dict['slot'][slot]['rp'][old_pid]['subslot'][subslot][pid]['pid'] = pid
                            inventory_dict['slot'][slot]['rp'][old_pid]['subslot'][subslot][pid]['vid'] = vid
                            inventory_dict['slot'][slot]['rp'][old_pid]['subslot'][subslot][pid]['sn'] = sn
                            slot = subslot = ''
                        elif subslot:
                            if 'subslot' not in inventory_dict['slot'][slot]['lc'][mod]:
                                inventory_dict['slot'][slot]['lc'][mod]['subslot'] = {}
                            if subslot not in inventory_dict['slot'][slot]['lc'][mod]['subslot']:
                                inventory_dict['slot'][slot]['lc'][mod]['subslot'][subslot] = {}
                            if pid not in inventory_dict['slot'][slot]['lc'][mod]['subslot'][subslot]:
                                inventory_dict['slot'][slot]['lc'][mod]['subslot'][subslot][pid] = {}
                            inventory_dict['slot'][slot]['lc'][mod]['subslot'][subslot][pid]['name'] = name
                            inventory_dict['slot'][slot]['lc'][mod]['subslot'][subslot][pid]['descr'] = descr
                            inventory_dict['slot'][slot]['lc'][mod]['subslot'][subslot][pid]['pid'] = pid
                            inventory_dict['slot'][slot]['lc'][mod]['subslot'][subslot][pid]['vid'] = vid
                            inventory_dict['slot'][slot]['lc'][mod]['subslot'][subslot][pid]['sn'] = sn
                            slot = subslot = ''
                        else:
                            if 'other' not in inventory_dict['slot'][slot]:
                                inventory_dict['slot'][slot]['other'] = {}
                                if pid not in inventory_dict['slot'][slot]['other']:
                                    inventory_dict['slot'][slot]['other'][pid] = {}
                                    inventory_dict['slot'][slot]['other'][pid]['name'] = name
                                    inventory_dict['slot'][slot]['other'][pid]['descr'] = descr
                                    inventory_dict['slot'][slot]['other'][pid]['pid'] = pid
                                    inventory_dict['slot'][slot]['other'][pid]['vid'] = vid
                                    inventory_dict['slot'][slot]['other'][pid]['sn'] = sn
                name = descr = slot = subslot = ''
                continue

        return inventory_dict


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
            # BOOT variable = flash:cat3k_caa-universalk9.BLD_POLARIS_DEV_LATEST_20150907_031219.bin;flash:cat3k_caa-universalk9.BLD_POLARIS_DEV_LATEST_20150828_174328.SSA.bin;flash:ISSUCleanGolden;
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

        p3 = re.compile(r'^Load +for +five +secs: +(?P<five_secs>[\d\/\%]+); '
                         '+one +minute: +(?P<one_min>[\d]+)\%; '
                         '+five +minutes: +(?P<five_min>[\d]+)\%$')

        p4 = re.compile(r'^Time +source +is +(?P<source>\w+),'
                         ' +(?P<time>[\d\:\.]+) +(?P<zone>\w+)'
                         ' +(?P<week_day>\w+) +(?P<month>\w+) +'
                         '(?P<day>\d+) +(?P<year>\d+)$')

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

            # Load for five secs: 1%/0%; one minute: 2%; five minutes: 3%
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('load', {})
                ret_dict['load'].update({k:str(v) for k, v in group.items()})
                continue

            # Time source is NTP, 18:56:04.554 JST Mon Oct 17 2016
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({k:str(v) for k, v in group.items()})
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