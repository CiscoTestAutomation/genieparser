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
                    'image': {
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
                      'l2_cache': str,
                    },
                    'last_reset': str,
                    'softwares': list,
                    'interfaces': {
                      'virtual_ethernet_ieee': int,
                      'gigabit_ethernet_ieee': int,
                    },
                    'memory': {
                      'non_volatile_conf': int,
                      'packet_buffer': int,
                      'flash_internal_SIMM': int,
                    },
                    'curr_config_register': str,
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
        p13 = re.compile(r'^(?P<cpu_name>\S+) +(CPU|cpu|Cpu) +at '
                         r'+(?P<speed>\S+)\, Implementation (?P<implementation>\S+), '
                         r'Rev (?P<rev>\S+), +(?P<l2_cache>\S+) +L2 +[Cc]ache$')

        # Last reset from s/w reset
        p14 = re.compile(r'^Last reset from (?P<reset>\S+) reset$')

        # SuperLAT software (copyright 1990 by Meridian Technology Corp).
        p15 = re.compile(r'^SuperLAT software .+$')

        # X.25 software, Version 3.0.0.
        p16 = re.compile(r'^X.25 software.+$')

        # Bridging software.
        p17 = re.compile(r'^Bridging software.$')

        # TN3270 Emulation software.
        p18 = re.compile(r'^TN3270 Emulation software.$')

        # 1 Virtual Ethernet/IEEE 802.3 interface
        p19 = re.compile(r'^(?P<interfaces>\d+) +Virtual '
                         r'+Ethernet/IEEE 802.3 +interface$')

        # 50 Gigabit Ethernet/IEEE 802.3 interfaces
        p20 = re.compile(r'^(?P<interfaces>\d+) +Gigabit '
                         r'+Ethernet/IEEE 802.3 +interfaces$')

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


            # ROM: IOS-XE ROMMON
            m = p4.match(line)
            if m:
                rom = m.groupdict()['rom']
                version_dict['rom'] = rom
                continue

            # BOOTLDR: System Bootstrap, Version 17.1.1[FC2], RELEASE SOFTWARE (P)
            m = p5.match(line)
            if m:
                version_dict['bootldr_version'] = m.groupdict()['bootldr_version']
                continue

            # SF2 uptime is 1 day, 18 hours, 48 minutes
            m = p6.match(line)
            if m:
                version_dict['hostname'] = m.groupdict()['hostname']
                version_dict['uptime'] = m.groupdict()['uptime']
                continue

            # Uptime for this control processor is 1 day, 18 hours, 49 minutes
            m = p7.match(line)
            if m:
                version_dict['uptime_this_cp'] = m.groupdict()['uptime_this_cp']
                continue

            # System returned to ROM by Reload Command
            m = p8.match(line)
            if m:
                version_dict['returned_to_rom_by'] = m.groupdict()['returned_to_rom_by']
                continue

            # System image file is "bootflash:/ecr.bin"
            m = p9.match(line)
            if m:
                version_dict['system_image'] = m.groupdict()['system_image']
                continue

            # Last reload reason: Reload Command
            m = p10.match(line)
            if m:
                version_dict['last_reload_reason'] = m.groupdict()['last_reload_reason']
                continue

            # AIR License Level: AIR DNA Advantage
            m = p11.match(line)
            if m:
                version_dict['license_level'] = m.groupdict()['license_level']
                continue

            # Next reload AIR license Level: AIR DNA Advantage
            m = p12.match(line)
            if m:
                version_dict['next_reload_license_level'] = m.groupdict()['next_reload_license_level']
                continue

            # Smart Licensing Status: UNREGISTERED/EVAL EXPIRED
            m = p13.match(line)
            if m:
                version_dict['smart_licensing_status'] = m.groupdict()['smart_licensing_status']
                continue

            # cisco C9500-32QC (X86) processor with 1863083K/6147K bytes of memory.
            m = p14.match(line)
            if m:
                version_dict['chassis'] = m.groupdict()['chassis']
                version_dict['processor_type'] = m.groupdict()['processor_type']
                version_dict['main_mem'] = m.groupdict()['main_mem']
                continue

            # Processor board ID CAT2242L6CG
            m = p15.match(line)
            if m:
                version_dict['processor_board_id'] = m.groupdict()['processor_board_id']
                continue

            # 44 Virtual Ethernet interfaces
            m = p16.match(line)
            if m:
                if 'number_of_intfs' not in version_dict:
                    intf_dict = version_dict.setdefault('number_of_intfs', {})
                intf_dict['virtual_ethernet_interfaces'] = m.groupdict()['virtual_ethernet_interfaces'].lower().replace(
                    ' ', '')
                continue

            # 32 Forty Gigabit Ethernet interfaces
            m = p17.match(line)
            if m:
                if 'number_of_intfs' not in version_dict:
                    intf_dict = version_dict.setdefault('number_of_intfs', {})
                intf_dict['forty_gigabit_ethernet_interfaces'] = m.groupdict()['forty_gigabit_ethernet_interfaces']
                continue

            # 16 Hundred Gigabit Ethernet interfaces
            m = p18.match(line)
            if m:
                if 'number_of_intfs' not in version_dict:
                    intf_dict = version_dict.setdefault('number_of_intfs', {})
                intf_dict['hundred_gigabit_ethernet_interfaces'] = m.groupdict()['hundred_gigabit_ethernet_interfaces']
                continue

            # 32768K bytes of non-volatile configuration memory.
            m = p19.match(line)
            if m:
                if 'mem_size' not in version_dict:
                    mem_dict = version_dict.setdefault('mem_size', {})
                mem_dict['non_volatile_memory'] = m.groupdict()['non_volatile_memory']
                continue

            # 16002848K bytes of physical memory.
            m = p20.match(line)
            if m:
                if 'mem_size' not in version_dict:
                    mem_dict = version_dict.setdefault('mem_size', {})
                mem_dict['physical_memory'] = m.groupdict()['physical_memory']
                continue

            # 11161600K bytes of Bootflash at bootflash:.
            m = p21.match(line)
            if m:
                if 'disks' not in version_dict:
                    disk_dict = version_dict.setdefault('disks', {})
                disk_dict.setdefault('bootflash:', {})['disk_size'] = \
                    m.groupdict()['bootflash_size']
                continue

            # 1638400K bytes of Crash Files at crashinfo:.
            m = p22.match(line)
            if m:
                if 'disks' not in version_dict:
                    disk_dict = version_dict.setdefault('disks', {})
                disk_dict.setdefault('crashinfo:', {})['disk_size'] = \
                    m.groupdict()['crash_size']
                continue

            # Base Ethernet MAC Address          : 70:b3:17:60:05:00
            m = p23.match(line)
            if m:
                mac_address = m.groupdict()['mac_address']
                version_dict['mac_address'] = mac_address
                continue

            # Motherboard Assembly Number        : 47A7
            m = p24.match(line)
            if m:
                mb_assembly_num = m.groupdict()['mb_assembly_num']
                version_dict['mb_assembly_num'] = mb_assembly_num
                continue

            # Motherboard Serial Number          : CAT2242L6CG
            m = p25.match(line)
            if m:
                mb_sn = m.groupdict()['mb_sn']
                version_dict['mb_sn'] = mb_sn
                continue

            # Model Revision Number              : V02
            m = p26.match(line)
            if m:
                model_rev_num = m.groupdict()['model_rev_num']
                version_dict['model_rev_num'] = model_rev_num
                continue

            # Motherboard Revision Number        : 4
            m = p27.match(line)
            if m:
                mb_rev_num = m.groupdict()['mb_rev_num']
                version_dict['mb_rev_num'] = mb_rev_num
                continue

            # Model Number                       : C9500-32QC
            m = p28.match(line)
            if m:
                model_num = m.groupdict()['model_num']
                version_dict['model_num'] = model_num
                continue

            # System Serial Number               : CAT2242L6CG
            m = p29.match(line)
            if m:
                system_sn = m.groupdict()['system_sn']
                version_dict['system_sn'] = system_sn
                continue

            # Configuration register is 0x102
            m = p30.match(line)
            if m:
                curr_config_register = m.groupdict()['curr_config_register']
                version_dict['curr_config_register'] = curr_config_register
                continue

            # Compiled Thu 31-Oct-19 17:43 by makale
            m = p31.match(line)
            if m:
                version_dict['compiled_date'] = m.groupdict()['compiled_date']
                version_dict['compiled_by'] = m.groupdict()['compiled_by']
                continue

            # Cisco IOS-XE software, Copyright (c) 2005-2019 by cisco Systems, Inc.
            m = p32.match(line)
            if m:
                os = m.groupdict()['os']
                version_dict['os'] = os
                continue

        return ver_dict


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
