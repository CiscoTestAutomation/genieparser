"""
 cat6k implementation of show_platform.py
"""

import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional


class ShowVersionSchema(MetaParser):
    """
    Schema for show version
    """
    schema = {
        'version': {
            'os': str,
            'platform': str,
            'version': str,
            'image_id': str,
            'compiled_by': str,
            'compiled_date': str,
            'rom': str,
            'rom_version': str,
            Optional('image'): {
                'text_base': str,
                'data_base': str,
            },
            'bootldr_version': str,
            'hostname': str,
            'uptime': str,
            'returned_to_rom_by': str,
            'system_image': str,
            'chassis': str,
            'processor_type': str,
            'main_mem': str,
            'processor_board_id': str,
            'cpu': {
                'name': str,
                'speed': str,
                'implementation': str,
                'rev': str,
                'l2_cache': str,
            },
            'last_reset': str,
            Optional('softwares'): list,
            'interfaces': {
                'virtual_ethernet': int,
                'gigabit_ethernet': int,
                Optional('serial'): int,
            },
            'memory': {
                'non_volatile_conf': int,
                'packet_buffer': int,
                'flash_internal_SIMM': int,
            },
            'curr_config_register': str,
            Optional('last_reload'): {
                'type': str,
                'reason': str,
            },
            Optional('control_processor_uptime'): str,
            Optional('controller'): {
                'type': str,
                'counts': int,
                'serial': int,
            }
        }
    }


class ShowVersion(ShowVersionSchema):
    """
    Parser for show version
    """

    cli_command = ['show version']
    exclude = ['uptime']

    def cli(self, output=None):

        if output is None:
            # Execute command to get output from device
            out = self.device.execute(self.cli_command[0])
        else:
            out = output

        ver_dict = {}
        version_dict = {}

        # IOS (tm) s72033_rp Software (s72033_rp-ADVENTERPRISEK9_WAN-M), Version 12.2(18)SXF7, RELEASE SOFTWARE (fc1)
        p1 = re.compile(r'^(?P<os>[A-Z]+) +\(.*\) +(?P<platform>.+) +Software'
                        r' +\((?P<image_id>.+)\).+( +Experimental)? +[Vv]ersion'
                        r' +(?P<version>\S+), +RELEASE SOFTWARE .*$')
        
        # Cisco IOS Software, s72033_rp Software (s72033_rp-ADVENTERPRISEK9_DBG-M), Version 15.4(0.10)S, EARLY DEPLOYMENT ENGINEERING WEEKLY BUILD, synced to  BLD_DARLING_122S_040709_1301
        p1_1 = re.compile(r'^[Cc]isco +(?P<os>[A-Z]+) +[Ss]oftware(.+)?\, '
                        r'+(?P<platform>.+) +Software +\((?P<image_id>.+)\).+( '
                        r'+Experimental)? +[Vv]ersion '
                        r'+(?P<version>[a-zA-Z0-9\.\:\(\)]+) *,?.*')

        # Technical Support: http://www.cisco.com/techsupport
        p2 = re.compile(r'^Technical +Support: +http\:\/\/www'
                        r'\.cisco\.com\/techsupport')

        # Copyright (c) 1986-2016 by Cisco Systems, Inc.
        p3 = re.compile(r'^Copyright +(.*)$')

        # Compiled Thu 23-Nov-06 06:26 by kellythw
        p4 = re.compile(r'^Compiled +(?P<compiled_date>[\S\s]+) +by '
                        r'+(?P<compiled_by>\S+)$')

        # Image text-base: 0x40101040, data-base: 0x42D98000
        p5 = re.compile(r'^Image text-base: (?P<text_base>\S+), '
                        r'data-base: (?P<data_base>\S+)$')

        # ROM: System Bootstrap, Version 12.2(17r)S4, RELEASE SOFTWARE (fc1)
        p6 = re.compile(r'^ROM: +(?P<rom>.+) +(?P<rom_version>[\S\s]+)$')

        # BOOTLDR: s72033_rp Software (s72033_rp-ADVENTERPRISEK9_WAN-M), Version 12.2(18)SXF7, RELEASE SOFTWARE (fc1)
        p7 = re.compile(r'^BOOTLDR: +(?P<bootldr_version>[\S\s]+)$')

        # cat6k_tb1 uptime is 21 weeks, 5 days, 41 minutes
        p8 = re.compile(r'^(?P<hostname>.+) +uptime +is +(?P<uptime>.+)$')

        # Uptime for this control processor is 22 weeks, 6 days, 1 hour, 57 minutes
        p8_2 = re.compile(r'^Uptime for this control processor is (?P<uptime>.+)$')

        # System returned to ROM by  power cycle at 21:57:23 UTC Sat Aug 28 2010 (SP by power on)
        p9 = re.compile(r'^System +returned +to +ROM +by '
                        r'+(?P<returned_to_rom_by>[\S\s]+)$')

        # System image file is "disk0:s72033-adventerprisek9_wan-mz.122-18.SXF7"
        p10 = re.compile(r'^System +image +file +is '
                         r'+\"(?P<system_image>.+)\"')

        # cisco WS-C6503-E (R7000) processor (revision 1.4) with 983008K/65536K bytes of memory.
        p11 = re.compile(r'^cisco +(?P<chassis>[\S]+) +\((?P<processor_type>[\S]+)\)'
                         r' +processor \(.+\) +with +(?P<main_mem>\d+).+ +bytes +of +memory.$')

        # Processor board ID FXS1821Q2H9
        p12 = re.compile(r'^Processor +board +ID +(?P<processor_board_id>.+)$')

        # SR71000 CPU at 600Mhz, Implementation 0x504, Rev 1.2, 512KB L2 Cache
        p13 = re.compile(r'^(?P<name>\S+) +(CPU|cpu|Cpu) +at '
                         r'+(?P<speed>\S+)\, Implementation (?P<implementation>\S+), '
                         r'Rev (?P<rev>\S+), +(?P<l2_cache>\S+) +L2 +[Cc]ache$')

        # Last reset from s/w reset
        p14 = re.compile(r'^Last reset from (?P<reset>\S+) reset$')

        # SuperLAT software (copyright 1990 by Meridian Technology Corp).
        p15 = re.compile(r'^(?P<software>SuperLAT software .+)$')

        # X.25 software, Version 3.0.0.
        p16 = re.compile(r'^(?P<software>X.25 software.+)$')

        # Bridging software.
        p17 = re.compile(r'^(?P<software>Bridging software.)$')

        # TN3270 Emulation software.
        p18 = re.compile(r'^(?P<software>TN3270 Emulation software.)$')

        # 1 Virtual Ethernet/IEEE 802.3 interface
        # 1 Virtual Ethernet/IEEE 802.3 interface(s)
        p19 = re.compile(r'^(?P<interface>\d+) +Virtual '
                         r'+Ethernet/IEEE 802.3 +interface(s|\(s\))?$')

        # 50 Gigabit Ethernet/IEEE 802.3 interfaces
        # 98 Gigabit Ethernet/IEEE 802.3 interface(s)
        p20 = re.compile(r'^(?P<interface>\d+) +Gigabit '
                         r'+Ethernet/IEEE 802.3 +interface(s|\(s\))?$')

        # 1917K bytes of non-volatile configuration memory.
        p21 = re.compile(r'^(?P<memory>\d+)K'
                         r' +bytes +of +non-volatile +configuration +memory.$')

        # 8192K bytes of packet buffer memory.
        p22 = re.compile(r'^(?P<memory>\d+)K'
                         r' +bytes +of +packet +buffer +memory.$')

        # 65536K bytes of Flash internal SIMM (Sector size 512K).
        p23 = re.compile(r'^(?P<memory>\d+)K bytes of Flash internal '
                         r'SIMM \(Sector size (?P<size>\d+)K\).$')

        # Configuration register is 0x102
        p30 = re.compile(r'^Configuration +register +is '
                         r'+(?P<curr_config_register>[\S]+)')
        
        # 1 Enhanced FlexWAN controller (4 Serial).
        p31 = re.compile(r'^(?P<counts>\d+) (?P<type>[\S\s]+) '
                         r'controller \((?P<serial>\d+) Serial\).$')
        
        # 1 Virtual Ethernet interface
        p31_1 = re.compile(r'^(?P<interface>\d+) Virtual Ethernet interface$')

        # 52 Gigabit Ethernet interfaces
        p31_2 = re.compile(r'^(?P<interface>\d+) Gigabit Ethernet interfaces$')

        # 4 Serial interfaces
        p31_3 = re.compile(r'^(?P<interface>\d+) Serial interfaces$')

        # Last reload type: Normal Reload
        p32_1 = re.compile(r'^Last reload type: (?P<type>[\S\s]+)$')

        # Last reload reason: abort at PC 0x433A11BC
        p32_2 = re.compile(r'^Last reload reason: (?P<reason>[\S\s]+)$')

        for line in out.splitlines():
            line = line.strip()

            # IOS (tm) s72033_rp Software (s72033_rp-ADVENTERPRISEK9_WAN-M), Version 12.2(18)SXF7, RELEASE SOFTWARE (fc1)
            m = p1.match(line)
            if m:
                if 'version' not in ver_dict:
                    version_dict = ver_dict.setdefault('version', {})
                for k in ['os', 'platform', 'image_id', 'version']:
                    version_dict[k] = m.groupdict()[k]
                continue
            
            # Cisco IOS Software, s72033_rp Software (s72033_rp-ADVENTERPRISEK9_DBG-M), Version 15.4(0.10)S, EARLY DEPLOYMENT ENGINEERING WEEKLY BUILD, synced to  BLD_DARLING_122S_040709_1301
            m = p1_1.match(line)
            if m:
                if 'version' not in ver_dict:
                    version_dict = ver_dict.setdefault('version', {})
                for k in ['os', 'platform', 'image_id', 'version']:
                    version_dict[k] = m.groupdict()[k]
                continue

            # Technical Support: http://www.cisco.com/techsupport
            # Copyright (c) 1986-2016 by Cisco Systems, Inc.
            m_2 = p2.match(line)
            m_3 = p3.match(line)
            if m_2 or m_3:
                continue

            # Compiled Thu 23-Nov-06 06:26 by kellythw
            m = p4.match(line)
            if m:
                for k in ['compiled_by', 'compiled_date']:
                    version_dict[k] = m.groupdict()[k]
                continue

            # Image text-base: 0x40101040, data-base: 0x42D98000
            m = p5.match(line)
            if m:
                if 'image' not in version_dict:
                    image_dict = version_dict.setdefault('image', {})
                for k in ['text_base', 'data_base']:
                    image_dict[k] = m.groupdict()[k]
                continue

            # ROM: System Bootstrap, Version 12.2(17r)S4, RELEASE SOFTWARE (fc1)
            m = p6.match(line)
            if m:
                for k in ['rom', 'rom_version']:
                    version_dict[k] = m.groupdict()[k]
                continue

            # BOOTLDR: s72033_rp Software (s72033_rp-ADVENTERPRISEK9_WAN-M), Version 12.2(18)SXF7, RELEASE SOFTWARE (fc1)
            m = p7.match(line)
            if m:
                version_dict['bootldr_version'] = m.groupdict()['bootldr_version']
                continue

            # cat6k_tb1 uptime is 21 weeks, 5 days, 41 minutes
            m = p8.match(line)
            if m:
                version_dict['hostname'] = m.groupdict()['hostname']
                version_dict['uptime'] = m.groupdict()['uptime']
                continue

            # Uptime for this control processor is 22 weeks, 6 days, 1 hour, 57 minutes
            m = p8_2.match(line)
            if m:
                version_dict['control_processor_uptime'] = m.groupdict()['uptime']
                continue

            # System returned to ROM by  power cycle at 21:57:23 UTC Sat Aug 28 2010 (SP by power on)
            m = p9.match(line)
            if m:
                version_dict['returned_to_rom_by'] = m.groupdict()['returned_to_rom_by']
                continue

            # System image file is "disk0:s72033-adventerprisek9_wan-mz.122-18.SXF7"
            m = p10.match(line)
            if m:
                version_dict['system_image'] = m.groupdict()['system_image']
                continue

            # cisco WS-C6503-E (R7000) processor (revision 1.4) with 983008K/65536K bytes of memory.
            m = p11.match(line)
            if m:
                for k in ['chassis', 'processor_type', 'main_mem']:
                    version_dict[k] = m.groupdict()[k]
                continue

            # Processor board ID FXS1821Q2H9
            m = p12.match(line)
            if m:
                version_dict['processor_board_id'] = m.groupdict()['processor_board_id']
                continue

            # SR71000 CPU at 600Mhz, Implementation 0x504, Rev 1.2, 512KB L2 Cache
            m = p13.match(line)
            if m:
                group = m.groupdict()
                if 'cpu' not in version_dict:
                    cpu_dict = version_dict.setdefault('cpu', {})
                for k in ['name', 'speed', 'implementation', 'rev', 'l2_cache']:
                    cpu_dict[k] = group[k]
                continue

            # Last reset from s/w reset
            m = p14.match(line)
            if m:
                version_dict['last_reset'] = m.groupdict()['reset']
                continue

            # SuperLAT software (copyright 1990 by Meridian Technology Corp).
            # X.25 software, Version 3.0.0.
            # Bridging software.
            # TN3270 Emulation software.
            m15 = p15.match(line)
            m16 = p16.match(line)
            m17 = p17.match(line)
            m18 = p18.match(line)
            if m15 or m16 or m17 or m18:
                if 'softwares' not in version_dict:
                    version_dict['softwares'] = []
                if m15:
                    version_dict['softwares'].append(m15.groupdict()['software'])
                elif m16:
                    version_dict['softwares'].append(m16.groupdict()['software'])
                elif m17:
                    version_dict['softwares'].append(m17.groupdict()['software'])
                elif m18:
                    version_dict['softwares'].append(m18.groupdict()['software'])
                continue

            # 1 Virtual Ethernet/IEEE 802.3 interface
            m = p19.match(line)
            if m:
                if 'interface' not in version_dict:
                    version_dict.setdefault('interfaces', {})
                version_dict['interfaces']['virtual_ethernet'] = \
                    int(m.groupdict()['interface'])
                continue

            # 50 Gigabit Ethernet/IEEE 802.3 interfaces
            m = p20.match(line)
            if m:
                version_dict['interfaces']['gigabit_ethernet'] = \
                    int(m.groupdict()['interface'])
                continue

            # 1917K bytes of non-volatile configuration memory.
            m21 = p21.match(line)
            # 8192K bytes of packet buffer memory.
            m22 = p22.match(line)
            # 65536K bytes of Flash internal SIMM (Sector size 512K).
            m23 = p23.match(line)

            if m21 or m22 or m23:
                if 'memory' not in version_dict:
                    mem_dict = version_dict.setdefault('memory', {})

                if m21:
                    mem_dict['non_volatile_conf'] = int(m21.groupdict()['memory'])
                elif m22:
                    mem_dict['packet_buffer'] = int(m22.groupdict()['memory'])
                elif m23:
                    mem_dict['flash_internal_SIMM'] = int(m23.groupdict()['memory'])
                continue

            # Configuration register is 0x102
            m = p30.match(line)
            if m:
                version_dict['curr_config_register'] = m.groupdict()['curr_config_register']
                continue

            # 1 Enhanced FlexWAN controller (4 Serial).
            m = p31.match(line)
            if m:
                group = m.groupdict()
                if 'controller' not in version_dict:
                    controller_dict = version_dict.setdefault('controller', {})
                controller_dict['type'] = group['type']
                controller_dict['counts'] = int(group['counts'])
                controller_dict['serial'] = int(group['serial'])
                continue

            # 1 Virtual Ethernet interface
            m = p31_1.match(line)
            if m:
                if 'interfaces' not in version_dict:
                    intf_dict = version_dict.setdefault('interfaces', {})
                intf_dict['virtual_ethernet'] = int(m.groupdict()['interface'])
                continue

            # 52 Gigabit Ethernet interfaces
            m = p31_2.match(line)
            if m:
                if 'interfaces' not in version_dict:
                    intf_dict = version_dict.setdefault('interfaces', {})
                intf_dict['gigabit_ethernet'] = int(m.groupdict()['interface'])
                continue

            # 4 Serial interfaces
            m = p31_3.match(line)
            if m:
                if 'interfaces' not in version_dict:
                    intf_dict = version_dict.setdefault('interfaces', {})
                intf_dict['serial'] = int(m.groupdict()['interface'])
                continue

            # Last reload type: Normal Reload
            m = p32_1.match(line)
            if m:
                if 'last_reload' not in version_dict:
                    last_reload_dict = version_dict.setdefault('last_reload', {})
                last_reload_dict['type'] = m.groupdict()['type']
                continue

            # Last reload reason: abort at PC 0x433A11BC
            m = p32_2.match(line)
            if m:
                if 'last_reload' not in version_dict:
                    last_reload_dict = version_dict.setdefault('last_reload', {})
                last_reload_dict['reason'] = m.groupdict()['reason']
                continue

        return ver_dict


class DirSchema(MetaParser):
    """
    Schema for command:
        * dir
    """
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
    """
    Parser for command:
        * dir
    """

    cli_command = ['dir', 'dir {directory}']
    exclude = ['last_modified_date', 'bytes_free', 'files']

    def cli(self, directory='', output=None):

        if output is None:
            if directory:
                out = self.device.execute(self.cli_command[1].format(directory=directory))
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
            p2 = re.compile(r'\s*(?P<index>\d+) +(?P<permissions>\S+) +(?P<size>\d+) '
                            r'+(?P<last_modified_date>\S+ +\d+ +\d+ +\d+\:\d+\:\d+ +\S+) '
                            r'+(?P<filename>.+)$')
            m = p2.match(line)
            if m:
                filename = m.groupdict()['filename']
                if 'files' not in dir_dict['dir'][dir1]:
                    dir_dict['dir'][dir1]['files'] = {}
                if filename not in dir_dict['dir'][dir1]['files']:
                    dir_dict['dir'][dir1]['files'][filename] = {}
                    dir_file_dict = dir_dict['dir'][dir1]['files'][filename]
                for k in ['index', 'permissions', 'size', 'last_modified_date']:
                    dir_file_dict[k] = m.groupdict()[k]
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
    """
    Schema for command:
        * show redundancy
    """
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
                        Optional('os'): str,
                        Optional('platform'): str,
                        Optional('image_id'): str,
                        Optional('version'): str,
                        Optional('boot'): str,
                        Optional('config_file'): str,
                        Optional('bootldr'): str,
                        'config_register': str,
                        'compiled_by': str,
                        'compiled_date': str,
                    }
                }
            }


class ShowRedundancy(ShowRedundancySchema):
    """
    Parser for command:
        * show redundancy
    """
    cli_command = ['show redundancy']
    exclude = ['available_system_uptime', 'uptime_in_curr_state']


    def cli(self, output=None):

        if output is None:
            out = self.device.execute(self.cli_command[0])
        else:
            out = output

        redundancy_dict = {}

        # Available system uptime = 21 weeks, 5 days, 1 hour, 3 minutes
        p1 = re.compile(
            r'Available +system +uptime += +(?P<available_system_uptime>[\S\s]+)$')

        # Switchovers system experienced = 0
        p2 = re.compile(
            r'Switchovers +system +experienced += +(?P<switchovers_system_experienced>\d+)$')

        # Standby failures = 0
        p3 = re.compile(
            r'Standby +failures += +(?P<standby_failures>\d+)$')

        # Last switchover reason = none
        p4 = re.compile(
            r'^Last +switchover +reason += +(?P<last_switchover_reason>[\S\s]+)$')

        # Hardware Mode = Simplex
        p5 = re.compile(
            r'^Hardware +Mode += +(?P<hw_mode>\S+)$')

        # Configured Redundancy Mode = sso
        p6 = re.compile(
            r'Configured +Redundancy +Mode += +(?P<conf_red_mode>\S+)$')

        # Operating Redundancy Mode = sso
        p7 = re.compile(
            r'^Operating +Redundancy +Mode += +(?P<oper_red_mode>\S+)$')

        # Maintenance Mode = Disabled
        p8 = re.compile(
            r'^Maintenance +Mode += +(?P<maint_mode>\S+)$')

        # Communications = Down      Reason: Simplex mode
        # Communications = Up
        p9 = re.compile(r'^Communications += +(?P<communications>\S+)'
                        r'(\s+Reason: +(?P<communications_reason>[\S\s]+))?$')

        # Active Location = slot 1
        # Standby Location = slot 5
        p10 = re.compile(r'^\S+ +Location += +(?P<slot>[\S ]+)$')

        # Current Software state = ACTIVE
        p11 = re.compile(r'^Current +Software +state += +(?P<curr_sw_state>[\S ]+)$')

        # Uptime in current state = 21 weeks, 5 days, 1 hour, 2 minutes
        p12 = re.compile(r'^Uptime +in +current +state += '
                         r'+(?P<uptime_in_curr_state>[\S\s]+)$')

        # Image Version = Cisco Internetwork Operating System Software
        p13 = re.compile(r'^Image +Version += +(?P<image_ver>.+)$')

        # BOOT = bootflash:/ecr.bin;
        p14 = re.compile(r'^BOOT += +(?P<boot>.+)$')

        # Configuration register = 0x102
        p15 = re.compile(r'^Configuration +register = (?P<config_register>\S+)$')

        # Compiled Thu 31-Oct-19 17:43 by makale
        p16 = re.compile(r'^Compiled +(?P<compiled_date>[\S\s]+) +by '
                         r'+(?P<compiled_by>\S+)$')

        # IOS (tm) s72033_rp Software (s72033_rp-ADVENTERPRISEK9_WAN-M), Version 12.2(18)SXF7, RELEASE SOFTWARE (fc1)
        p17 = re.compile(r'^(?P<os>[A-Z]+) +\(.*\) +(?P<platform>.+) +Software'
                        r' +\((?P<image_id>.+)\).+( +Experimental)? +[Vv]ersion'
                        r' +(?P<version>\S+), +RELEASE SOFTWARE .*$')

        # Technical Support: http://www.cisco.com/techsupport
        p18 = re.compile(r'^Technical +Support: +http\:\/\/www'
                        r'\.cisco\.com\/techsupport')

        # Copyright (c) 1986-2016 by Cisco Systems, Inc.
        p19 = re.compile(r'^Copyright +(.*)$')

        # CONFIG_FILE =
        p20 = re.compile(r'^CONFIG_FILE = +(?P<config_file>\S+)$')

        # BOOTLDR =
        p21 = re.compile(r'^BOOTLDR = +(?P<bootldr>\S+)$')

        for line in out.splitlines():
            line = line.strip()

            # Available system uptime = 1 day, 18 hours, 48 minutes
            m = p1.match(line)
            if m:
                red_dict = redundancy_dict.setdefault('red_sys_info', {})
                red_dict['available_system_uptime'] = \
                    m.groupdict()['available_system_uptime']
                continue

            # Switchovers system experienced = 0
            m = p2.match(line)
            if m:
                red_dict['switchovers_system_experienced'] = \
                    m.groupdict()['switchovers_system_experienced']
                continue

            # Standby failures = 0
            m = p3.match(line)
            if m:
                red_dict['standby_failures'] = \
                    m.groupdict()['standby_failures']
                continue

            # Last switchover reason = none
            m = p4.match(line)
            if m:
                red_dict['last_switchover_reason'] = \
                    m.groupdict()['last_switchover_reason']
                continue

            # Hardware Mode = Simplex
            m = p5.match(line)
            if m:
                red_dict['hw_mode'] = m.groupdict()['hw_mode']
                continue

            # Configured Redundancy Mode = Non-redundant
            m = p6.match(line)
            if m:
                red_dict['conf_red_mode'] = m.groupdict()['conf_red_mode']
                continue

            # Operating Redundancy Mode = Non-redundant
            m = p7.match(line)
            if m:
                red_dict['oper_red_mode'] = m.groupdict()['oper_red_mode']
                continue

            # Maintenance Mode = Disabled
            m = p8.match(line)
            if m:
                red_dict['maint_mode'] = m.groupdict()['maint_mode']
                continue

            # Communications = Down      Reason: Failure
            m = p9.match(line)
            if m:
                group = m.groupdict()
                red_dict['communications'] = group['communications']
                communications_reason = group.get('communications_reason')
                if communications_reason:
                    red_dict['communications_reason'] = group['communications_reason']
                continue

            # Active Location = slot 1
            m = p10.match(line)
            if m:
                slot = m.groupdict()['slot']
                slot_dict = redundancy_dict.setdefault(
                    'slot', {}).setdefault(slot, {})
                continue

            # Current Software state = ACTIVE
            # Current Software state = STANDBY HOT
            m = p11.match(line)
            if m:
                if 'slot' in redundancy_dict:
                    slot_dict['curr_sw_state'] = m.groupdict()['curr_sw_state']
                continue

            # Uptime in current state = 1 day, 18 hours, 48 minutes
            m = p12.match(line)
            if m:
                if 'slot' in redundancy_dict:
                    slot_dict['uptime_in_curr_state'] = \
                        m.groupdict()['uptime_in_curr_state']
                continue

            # Image Version = Cisco IOS Software [Amsterdam], Catalyst L3 Switch Software (CAT9K_IOSXE), Experimental Version 17.2.20191101:003833 [HEAD-/nobackup/makale/puntject2/polaris 106]
            m = p13.match(line)
            if m:
                if 'slot' in redundancy_dict:
                    slot_dict['image_ver'] = m.groupdict()['image_ver']
                continue

            # BOOT = bootflash:/ecr.bin;
            m = p14.match(line)
            if m:
                if 'slot' in redundancy_dict:
                    slot_dict['boot'] = m.groupdict()['boot']
                continue

            # Configuration register = 0x102
            m = p15.match(line)
            if m:
                if 'slot' in redundancy_dict:
                    slot_dict['config_register'] = m.groupdict()['config_register']
                continue

            # Compiled Thu 31-Oct-19 17:43 by makale
            m = p16.match(line)
            if m:
                if 'slot' in redundancy_dict:
                    slot_dict['compiled_by'] = m.groupdict()['compiled_by']
                    slot_dict['compiled_date'] = m.groupdict()['compiled_date']
                continue

            # IOS (tm) s72033_rp Software (s72033_rp-ADVENTERPRISEK9_WAN-M), Version 12.2(18)SXF7, RELEASE SOFTWARE (fc1)
            m = p17.match(line)
            if m:
                for k in ['os', 'platform', 'image_id', 'version']:
                    slot_dict[k] = m.groupdict()[k]
                continue

            # Technical Support: http://www.cisco.com/techsupport
            # Copyright (c) 1986-2016 by Cisco Systems, Inc.
            m_18 = p18.match(line)
            m_19 = p19.match(line)
            if m_18 or m_19:
                continue

            # CONFIG_FILE =
            m = p20.match(line)
            if m:
                if 'slot' in redundancy_dict:
                    slot_dict['config_file'] = m.groupdict()['config_file']
                continue

            # BOOTLDR =
            m = p21.match(line)
            if m:
                if 'slot' in redundancy_dict:
                    slot_dict['bootldr'] = m.groupdict()['bootldr']
                continue

        return redundancy_dict


class ShowInventorySchema(MetaParser):
    """
    Schema for:
        * 'show inventory'
    """

    schema = {
        'index': {
            Any():
                {'name': str,
                 'descr': str,
                 Optional('pid'): str,
                 Optional('vid'): str,
                 Optional('sn'): str,
                },
            }
        }


class ShowInventory(ShowInventorySchema):
    """
    Parser for:
        * show inventory
    """
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
        index = 0

        # NAME: "HundredGigE1/0/48", DESCR: "QSFP 100GE SR"
        p1 = re.compile(r'^NAME: +\"(?P<name>.*)\",'
                         ' +DESCR: +\"(?P<descr>.*)\"$')

        # PID: QSFP-100G-SR4-S     , VID: V03  , SN: AVF2243S10A
        p2 = re.compile(r'^PID: +(?P<pid>\S+)? *, +VID:(?: +(?P<vid>(\S+)))? *,'
                         ' +SN:(?: +(?P<sn>(\S+)))?$')

        for line in out.splitlines():
            line = line.strip()

            # NAME: "HundredGigE1/0/48", DESCR: "QSFP 100GE SR"
            m = p1.match(line)
            if m:
                index += 1
                group = m.groupdict()
                final_dict = ret_dict.setdefault('index', {}).setdefault(index, {})
                for key in group.keys():
                    if group[key]:
                        final_dict[key] = group[key]
                continue

            # PID: QSFP-100G-SR4-S     , VID: V03  , SN: AVF2243S10A
            m = p2.match(line)
            if m:
                group = m.groupdict()
                for key in group.keys():
                    if group[key]:
                        final_dict[key] = group[key]
                continue

        return ret_dict



class ShowModuleSchema(MetaParser):
    """ Schema for commands:
        * show module
    """
    schema = {
        'slot': {
            Any(): {
                Optional('rp'): {
                    'slot': int,
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
                    Optional('online_diag_status'): str,
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
                    'slot': int,
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
                    Optional('online_diag_status'): str,
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
                    'slot': int,
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

        # 1  0001.64ff.1958 to 0001.64ff.1959   3.9   6.1(3)       7.5(0.6)HUB9 Ok 
        # 3  0005.74ff.1b9d to 0005.74ff.1bac   1.3   12.1(5r)E1   12.1(13)E3,  Ok
        # 1  0001.64ff.1958 to 0001.64ff.1959   3.9   6.1(3)       7.5(0.6)HUB9 Ok    
        r4 = re.compile(r'(?P<mod>\d+)\s+(?P<mac_from>\S+)\s+to\s+(?P<mac_to>\S+)'
                         '\s+(?P<hw>\S+)\s+(?P<fw>\S+)\s+(?P<sw>[\d\.\(\)\w]+)\,'
                         '*\s+(?P<status>(Ok|Unknown))')

        # 1 Policy Feature Card 2       WS-F6K-PFC2     SAD062802AV      3.2    Ok     
        # 1 Cat6k MSFC 2 daughterboard  WS-F6K-MSFC2    SAD062803TX      2.5    Ok   
        # 6 Distributed Forwarding Card WS-F6K-DFC      SAL06261R0A      2.3    Ok     
        # 6 10GBASE-LR Serial 1310nm lo WS-G6488        SAD062201BN      1.1    Ok
        r5 = re.compile(r'(?P<mod>\d+)\s+(?P<sub_mod>.+)\s+(?P<model>\S+)\s+'
                         '(?P<serial>\S+)\s+(?P<hw>\S+)\s+(?P<status>(Ok|Unknown))')

        # 1  Pass
        r6 = re.compile(r'(?P<mod>\d+) +(?P<online_diag_status>\S+)$')

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
                    .setdefault('rp', {'slot': int(mod)})

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
                    .setdefault('lc', {'slot': int(mod)})

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
                    .setdefault('other', {'slot': int(mod)})

                module_dict['ports'] = ports
                module_dict['card_type'] = card_type
                module_dict['model'] = model
                module_dict['serial_number'] = serial_number

                continue

            # 1  0001.64ff.1958 to 0001.64ff.1959   3.9   6.1(3)       7.5(0.6)HUB9 Ok 
            # 3  0005.74ff.1b9d to 0005.74ff.1bac   1.3   12.1(5r)E1   12.1(13)E3,  Ok
            # 1  0001.64ff.1958 to 0001.64ff.1959   3.9   6.1(3)       7.5(0.6)HUB9 Ok   
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
                    .setdefault(slot_code, {'slot': int(mod)})

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

            # 1  Pass
            result = r6.match(line)
            if result:
                group = result.groupdict()
                mod = group['mod']

                slot_code = [*parsed_output.get('slot', {}).get(mod, {}).keys()][0]

                parsed_output\
                    .setdefault('slot', {})\
                    .setdefault(mod, {})\
                    .setdefault(slot_code, {})\
                    .setdefault('online_diag_status', group['online_diag_status'])
                continue

        return parsed_output