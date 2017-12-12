''' show_platform.py

Example parser class

'''
import re
import logging

from metaparser import MetaParser
from metaparser.util.schemaengine import Schema, \
                                         Any, \
                                         Optional, \
                                         Or, \
                                         And, \
                                         Default, \
                                         Use
try:
    import parsergen
except ImportError:
    pass

logger = logging.getLogger(__name__)


class ShowVersionSchema(MetaParser):
    schema = {
                'version': {
                    'version_short': str,
                    'platform': str,
                    'version': str,
                    'image_id': str,
                    'rom': str,
                    Optional('bootldr'): str,
                    'hostname': str,
                    'uptime': str,
                    Optional('uptime_this_cp'): str,
                    'system_restarted_at': str,
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
    """ parser class - implements detail parsing mechanisms for cli, xml, and
    yang output.
    """
    # *************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).

    def cli(self):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: exe
        cuting, transforming, returning
        '''
        cmd = 'show version'.format()
        out = self.device.execute(cmd)
        version_dict = {}
        switch_number = '1'
        rtr_type = ''
        for line in out.splitlines():
            line = line.rstrip()

            # version
            p1 = re.compile(
                r'^\s*[Cc]isco +IOS +[Ss]oftware.+, (?P<platform>.+) Software +\((?P<image_id>.+)\).+[Vv]ersion +(?P<version>[a-zA-Z0-9\.\:]+) +')
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
                r'^\s*[Cc]isco +IOS +[Ss]oftware.+, (?P<platform>.+) Software +\((?P<image_id>.+)\).+( +Experimental)? +[Vv]ersion +(?P<version>[a-zA-Z0-9\.\:]+) *,? +')
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

            # rom
            p2 = re.compile(
                r'^\s*ROM\: +(?P<rom>.+)$')
            m = p2.match(line)
            if m:
                version_dict['version']['rom'] = \
                    m.groupdict()['rom']
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
            p8 = re.compile(
                r'^\s*cisco +(?P<chassis>[a-zA-Z0-9\-]+) +\((?P<processor_type>.+)\) +processor.+ +with +(?P<main_mem>[0-9]+)[kK]\/[0-9]+[kK]')
            m = p8.match(line)
            if m:
                version_dict['version']['chassis'] \
                    = m.groupdict()['chassis']
                version_dict['version']['main_mem'] \
                    = m.groupdict()['main_mem']
                version_dict['version']['processor_type'] \
                    = m.groupdict()['processor_type']
                if 'C3850' in version_dict['version']['chassis']:
                    version_dict['version']['rtr_type'] = rtr_type = 'Edison'
                elif 'ASR1' in version_dict['version']['chassis']:
                    version_dict['version']['rtr_type'] = rtr_type = 'ASR1K'
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
            p16 = re.compile(r'^s*[Ss]witch +0(?P<switch_number>\d+)')
            m = p16.match(line)
            if m:
                switch_number = m.groupdict()['switch_number']
            if 'Edison' in rtr_type:
                if 'switch_num' not in version_dict['version']:
                    version_dict['version']['switch_num'] = {}
                if switch_number not in version_dict['version']['switch_num']:
                    version_dict['version']['switch_num'][switch_number] = {}

            # uptime
            p17 = re.compile(
                r'^\s*[Ss]witch +uptime +\: +(?P<uptime>.+)$')
            m = p17.match(line)
            if m:
                version_dict['version']['switch_num'][switch_number]['uptime'] = m.groupdict()['uptime']
                continue

            # mac_address
            p18 = re.compile(
                r'^\s*[Bb]ase +[Ee]thernet +MAC +[Aa]ddress +\: +(?P<mac_address>.+)$')
            m = p18.match(line)
            if m:
                version_dict['version']['switch_num'][switch_number]['mac_address'] = m.groupdict()['mac_address']
                continue
            # mb_assembly_num
            p19 = re.compile(
                r'^\s*[Mm]otherboard +[Aa]ssembly +[Nn]umber +\: +(?P<mb_assembly_num>.+)$')
            m = p19.match(line)
            if m:
                version_dict['version']['switch_num'][switch_number]['mb_assembly_num'] = m.groupdict()['mb_assembly_num']
                continue
            # mb_sn
            p20 = re.compile(
                r'^\s*[Mm]otherboard +[Ss]erial +[Nn]umber +\: +(?P<mb_sn>.+)$')
            m = p20.match(line)
            if m:
                version_dict['version']['switch_num'][switch_number]['mb_sn'] = m.groupdict()['mb_sn']
                continue
            # model_rev_num
            p21 = re.compile(
                r'^\s*[Mm]odel +[Rr]evision +[Nn]umber +\: +(?P<model_rev_num>.+)$')
            m = p21.match(line)
            if m:
                version_dict['version']['switch_num'][switch_number]['model_rev_num'] = m.groupdict()['model_rev_num']
                continue
            # mb_rev_num
            p22 = re.compile(
                r'^\s*[Mm]otherboard +[Rr]evision +[Nn]umber +\: +(?P<mb_rev_num>.+)$')
            m = p22.match(line)
            if m:
                version_dict['version']['switch_num'][switch_number]['mb_rev_num'] = m.groupdict()['mb_rev_num']
                continue
            # model_num
            p23 = re.compile(
                r'^\s*[Mm]odel +[Nn]umber +\: +(?P<model_num>.+)$')
            m = p23.match(line)
            if m:
                version_dict['version']['switch_num'][switch_number]['model_num'] = m.groupdict()['model_num']
                continue
            # system_sn
            p24 = re.compile(
                r'^\s*[Ss]ystem +[Ss]erial +[Nn]umber +\: +(?P<system_sn>.+)$')
            m = p24.match(line)
            if m:
                version_dict['version']['switch_num'][switch_number]['system_sn'] = m.groupdict()['system_sn']
                continue

        # table2 for C3850
        tmp2 = parsergen.oper_fill_tabular(right_justified=True,
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
        tmp = parsergen.oper_fill_tabular(right_justified=True,
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
                else:
                    for k, v in res2.entries[key].items():
                        if key not in version_dict['version']['switch_num']:
                            version_dict['version']['switch_num'][key] = {}
                        if 'switch_num' != k:
                            version_dict['version']['switch_num'][key][k] = v
                    version_dict['version']['switch_num'][key]['active'] = False 

        return version_dict


class DirSchema(MetaParser):
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
    """ parser class - implements detail parsing mechanisms for cli, xml, and
    yang output.
    """
    # *************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).

    def cli(self):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: exe
        cuting, transforming, returning
        '''
        cmd = 'dir'.format()
        out = self.device.execute(cmd)
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
                        'boot': str,
                        Optional('config_file'): str,
                        Optional('bootldr'): str,
                        'config_register': str,
                    }
                }
            }


class ShowRedundancy(ShowRedundancySchema):
    """ parser class - implements detail parsing mechanisms for cli, xml, and
    yang output.
    """
    # *************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).

    def cli(self):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: exe
        cuting, transforming, returning
        '''
        cmd = 'show redundancy'.format()
        out = self.device.execute(cmd)
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
    """ parser class - implements detail parsing mechanisms for cli, xml, and
    yang output.
    """
    # *************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).

    def cli(self):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: exe
        cuting, transforming, returning
        '''
        cmd = 'show inventory'.format()
        out = self.device.execute(cmd)
        name = descr = slot = subslot = pid = ''
        inventory_dict = {}
        for line in out.splitlines():
            line = line.rstrip()

            # check 1st line and get slot number
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
            p2 = re.compile(r'^\s*PID\: +(?P<pid>\S+)\s+\,\s+VID\:\s+(?P<vid>\S+)\s+\,\s+SN\:\s+(?P<sn>.*)$')
            m = p2.match(line)
            if m:
                if 'WS-C' in pid:
                    old_pid = pid
                pid = m.groupdict()['pid']
                vid = m.groupdict()['vid']
                sn = m.groupdict()['sn']
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
                        elif 'SIP' in pid:
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
    """ parser class - implements detail parsing mechanisms for cli, xml, and
    yang output.
    """
    # *************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).

    def cli(self):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: exe
        cuting, transforming, returning
        '''

        cmd = 'show platform'.format()
        out = self.device.execute(cmd)
        platform_dict = {}
        sub_dict = {}
        if out:

            for line in out.splitlines():
                line = line.strip()

                # ----------      C3850    -------------

                # Switch/Stack Mac Address : 0057.d21b.cc00 - Local Mac Address
                p1 = re.compile(
                    r'^[Ss]witch\/[Ss]tack +[Mm]ac +[Aa]ddress +\: +'
                     '(?P<switch_mac_address>[\w\.]+) *(?P<local>[\w\s\-]+)?$')
                m = p1.match(line)
                if m:
                    if 'main' not in platform_dict:
                        platform_dict['main'] = {}
                    platform_dict['main']['switch_mac_address'] = m.groupdict()['switch_mac_address']
                    continue

                # Mac persistency wait time: Indefinite
                p2 = re.compile(r'^[Mm]ac +persistency +wait +time\: +(?P<mac_persistency_wait_time>[\w\.\:]+)$')
                m = p2.match(line)
                if m:
                    if 'main' not in platform_dict:
                        platform_dict['main'] = {}
                    platform_dict['main']['mac_persistency_wait_time'] = m.groupdict()['mac_persistency_wait_time'].lower()
                    continue

                # Switch  Ports    Model                Serial No.   MAC address     Hw Ver.       Sw Ver. 
                # ------  -----   ---------             -----------  --------------  -------       --------
                #  1       32     WS-C3850-24P-E        FCW1947C0HH  0057.d21b.cc00  V07           16.6.1
                p3 = re.compile(r'^(?P<switch>\d+) +(?P<ports>\d+) +'
                                 '(?P<model>[\w\-]+) +(?P<serial_no>\w+) +'
                                 '(?P<mac_address>[\w\.\:]+) +'
                                 '(?P<hw_ver>\w+) +(?P<sw_ver>[\w\.]+)$')
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

                #                                     Current
                # Switch#   Role        Priority      State 
                # -------------------------------------------
                # *1       Active          3          Ready
                p4 = re.compile(r'^\*?(?P<switch>\d+) +(?P<role>\w+) +'
                                 '(?P<priority>\d+) +(?P<state>\w+)$')
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

                # ----------      ASR1K    -------------
                # Chassis type: ASR1006
                p5 = re.compile(r'^[Cc]hassis +type: +(?P<chassis>\w+)$')
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
                p6 = re.compile(r'^(?P<slot>\w+)(\/(?P<subslot>\d+))? +(?P<name>\S+) +'
                                 '(?P<state>\w+(\, \w+)?) +(?P<insert_time>[\w\.\:]+)$')
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
                        except:
                            continue
                    else:
                        if 'slot' not in platform_dict:
                            platform_dict['slot'] = {}
                        if slot not in platform_dict['slot']:
                            platform_dict['slot'][slot] = {}
                        if ('ASR1000-SIP' in name) or ('ASR1000-2T' in name) or ('ASR1000-6T' in name):
                            lc_type = 'lc'
                        elif 'ASR1000-RP' in name:
                            lc_type = 'rp'
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

                # 4                             unknown               2d00h
                p6_1 = re.compile(r'^(?P<slot>\w+) +(?P<state>\w+(\, \w+)?)'
                                 ' +(?P<insert_time>[\w\.\:]+)$')
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


                # Slot      CPLD Version        Firmware Version                        
                # --------- ------------------- --------------------------------------- 
                # 0         00200800            16.2(1r) 
                p7 = re.compile(r'^(?P<slot>\w+) +(?P<cpld_version>\d+|N\/A) +'
                                 '(?P<fireware_ver>[\w\.\(\)\/]+)$')
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
    '''Schema for command 'show boot' '''

    schema = {Optional('current_boot_variable'): str,
              Optional('next_reload_boot_variable'): str,
              Optional('manual_boot'): bool,
              Optional('enable_break'): bool,
              Optional('boot_mode'): str,
              Optional('ipxe_timeout'): int,
              Optional('active'): {              
                  'configuration_register': str,
                  'boot_variable': str,
              },
              Optional('standby'): {              
                  'configuration_register': str,
                  'boot_variable': str,
              },
    }

class ShowBoot(ShowBootSchema):
    '''parser for command 'show boot' '''

    def cli(self):
        cmd = 'show boot'.format()
        out = self.device.execute(cmd)
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