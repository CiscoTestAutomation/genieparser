"""
 c7600 implementation of show_platform.py
"""

import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

# import cat6k parser
from genie.libs.parser.ios.cat6k.show_platform import Dir as Dir_cat6k


class ShowVersionSchema(MetaParser):
    """Schema for show version"""
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
                    'uptime': str,
                    'bootldr_version': str,
                    'control_processor_uptime': str,
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
                    'memory': {
                      'non_volatile_conf': int,
                      'packet_buffer': int,
                      'flash_internal_SIMM': int,
                    },
                    'curr_config_register': str,
                    'last_reload': {
                        'type': str,
                        'reason': str,
                    },
                    'interfaces': {
                        'virtual_ethernet': int,
                        'gigabit_ethenet': int,
                        'serial': int,
                    },
                    'controller': {
                        'type': str,
                        'counts': int,
                        'serial': int,
                    }
                }
            }


class ShowVersion(ShowVersionSchema):
    """
    parser for command: show version
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

        # Cisco IOS Software, s72033_rp Software (s72033_rp-ADVENTERPRISEK9_DBG-M), Version 15.4(0.10)S, EARLY DEPLOYMENT ENGINEERING WEEKLY BUILD, synced to  BLD_DARLING_122S_040709_1301
        p1 = re.compile(r'^[Cc]isco +(?P<os>[A-Z]+) +[Ss]oftware(.+)?\, '
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

        # ROM: System Bootstrap, Version 12.2(17r)S4, RELEASE SOFTWARE (fc1)
        p6 = re.compile(r'^ROM: +(?P<rom>.+) +(?P<rom_version>[\S\s]+)$')

        # BOOTLDR: s72033_rp Software (s72033_rp-ADVENTERPRISEK9_WAN-M), Version 12.2(18)SXF7, RELEASE SOFTWARE (fc1)
        p7 = re.compile(r'^BOOTLDR: +(?P<bootldr_version>[\S\s]+)$')

        # ipcore-ssr-uut2 uptime is 22 weeks, 6 days, 2 hours, 1 minute
        p8 = re.compile(r'^.* uptime +is +(?P<uptime>.+)$')

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

        # 1 Enhanced FlexWAN controller (4 Serial).
        p15 = re.compile(r'^(?P<counts>\d+) (?P<type>[\S\s]+) '
                         r'controller \((?P<serial>\d+) Serial\).$')

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

            # ipcore-ssr-uut2 uptime is 22 weeks, 6 days, 2 hours, 1 minute
            m = p8.match(line)
            if m:
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

            # 1 Enhanced FlexWAN controller (4 Serial).
            m = p15.match(line)
            if m:
                group = m.groupdict()
                if 'controller' not in version_dict:
                    controller_dict = version_dict.setdefault('controller', {})
                controller_dict['type'] = group['type']
                controller_dict['counts'] = int(group['counts'])
                controller_dict['serial'] = int(group['serial'])
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
                intf_dict['gigabit_ethenet'] = int(m.groupdict()['interface'])
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


class Dir(Dir_cat6k):
    """
    parser for command: dir
    """
    pass

