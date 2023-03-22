'''show_platform.py

IOSXE c9500 parsers for the following show commands:
   * show version
   * show platform
   * show redundancy
   * show inventory
   * show platform software object-manager switch {switchvirtualstate} {serviceprocessor} statistics
   * show platform hardware fed switch active fwd-asic resource tcam table pbr record 0 format 0 | begin {nat_region}
   * show platform hardware chassis fantray detail
   * show platform hardware chassis power-supply detail all
   * show platform hardware chassis fantray detail switch {mode}
   * show platform hardware chassis power-supply detail switch {mode} all
'''

# Python
import re
import logging
import xmltodict

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional, And, Default, Use

# import parser utils
from genie.libs.parser.utils.common import Common

# ==========================
#  Schema for 'show version'
# ==========================
class ShowVersionSchema(MetaParser):

    """Schema for show version"""

    schema = {
                'version': {
                    Optional('xe_version'): str,
                    'version_short': str,
                    'os': str,
                    Optional('code_name'): str,
                    'platform': str,
                    'version': str,
                    Optional('label'): str,
                    Optional('build_label'): str,
                    'image_id': str,
                    'rom': str,
                    'bootldr_version': str,
                    'hostname': str,
                    'uptime': str,
                    'uptime_this_cp': str,
                    'returned_to_rom_by': str,
                    'system_image': str,
                    'last_reload_reason': str,
                    'chassis': str,
                    'processor_type': str,
                    'main_mem': str,
                    'processor_board_id': str,
                    Optional('curr_config_register'): str,
                    'compiled_date': str,
                    'compiled_by': str,
                    'mac_address': str,
                    'mb_assembly_num': str,
                    'mb_sn': str,
                    'model_rev_num': str,
                    'mb_rev_num': str,
                    'model_num': str,
                    Optional ('system_sn'): str,
                    Optional('mem_size'): {
                        Any(): str,
                    },
                    Optional('license_level'): str,
                    Optional('next_reload_license_level'): str,
                    'smart_licensing_status': str,
                    Optional('number_of_intfs'): {
                        Any(): str,
                    },
                    Optional('disks'): {
                        Any(): {
                            'disk_size': str,
                        }
                    },
                }
            }


# ==========================
#  Parser for 'show version'
# ==========================
class ShowVersion(ShowVersionSchema):

    """Parser for show version"""

    cli_command = ['show version']
    exclude = ['uptime_this_cp', 'uptime']

    def cli(self, output=None):

        if output is None:
            # Execute command to get output from device
            out = self.device.execute(self.cli_command[0])
        else:
            out = output

        ver_dict = {}
        version_dict = {}

        # version
        # Cisco IOS XE Software, Version 2019-10-31_17.49_makale
        # Cisco IOS XE Software, Version BLD_POLARIS_DEV_LATEST_20210302_012043
        p0 = re.compile(
            r'^Cisco +([\S\s]+) +Software, +Version +(?P<xe_version>.*)$')

        # Cisco IOS Software [Amsterdam], Catalyst L3 Switch Software (CAT9K_IOSXE), Experimental Version 17.2.20191101:003833 [HEAD-/nobackup/makale/puntject2/polaris 106]
        # Cisco IOS Software [Bengaluru], Catalyst L3 Switch Software (CAT9K_IOSXE), Experimental Version 17.6.20210302:012459 [S2C-build-polaris_dev-132831-/nobackup/mcpre/BLD-BLD_POLARIS_DEV_LATEST_20210302_012043 149]
        p1 = re.compile(
            r'^Cisco +IOS +Software +\[(?P<code_name>([\S]+))\], +(?P<platform>([\S\s]+)) '
            r'+Software +\((?P<image_id>.+)\),( +Experimental)? +Version +(?P<version>[\d\.:]+),? *'
            r'(?P<label>(\[.+?(?P<build_label>BLD_\S+)? \d+\])|.*)$')

        # 16.6.5
        p1_1 = re.compile(r'^(?P<ver_short>\d+\.\d+).*')

        # Copyright (c) 1986-2016 by Cisco Systems, Inc.
        p2 = re.compile(r'^Copyright +(.*)$')

        # Technical Support: http://www.cisco.com/techsupport
        p3 = re.compile(r'^Technical +Support: +http\:\/\/www'
                        r'\.cisco\.com\/techsupport')

        # ROM: IOS-XE ROMMON
        p4 = re.compile(r'^ROM: +(?P<rom>.+)$')

        # BOOTLDR: System Bootstrap, Version 17.1.1[FC2], RELEASE SOFTWARE (P)
        p5 = re.compile(r'^BOOTLDR: +(?P<bootldr_version>[\S\s]+)$')

        # SF2 uptime is 1 day, 18 hours, 48 minutes
        p6 = re.compile(r'^(?P<hostname>.+) +uptime +is +(?P<uptime>.+)$')

        # Uptime for this control processor is 1 day, 18 hours, 49 minutes
        p7 = re.compile(r'^Uptime +for +this +control +processor '
                         r'+is +(?P<uptime_this_cp>.+)$')

        # System returned to ROM by Reload Command
        p8 = re.compile(r'^System +returned +to +ROM +by '
                         r'+(?P<returned_to_rom_by>[\S\s]+)$')

        # System image file is "harddisk:test-image-PE1-13113029"
        p9 = re.compile(r'^System +image +file +is '
                         r'+\"(?P<system_image>.+)\"')

        # Last reload reason: Reload Command
        p10 = re.compile(r'^Last +reload +reason\: '
                         r'+(?P<last_reload_reason>[\S\s]+)$')

        # AIR License Level: AIR DNA Advantage
        p11 = re.compile(r'^AIR +License +Level: +(?P<license_level>.+)$')

        # Next reload AIR license Level: AIR DNA Advantage
        p12 = re.compile(r'^Next +reload +AIR +license +Level: +(?P<next_reload_license_level>.+)$')

        # Smart Licensing Status: UNREGISTERED/EVAL EXPIRED
        p13 = re.compile(r'^Smart +Licensing +Status: +(?P<smart_licensing_status>.+)$')

        # cisco C9500-32QC (X86) processor with 1863083K/6147K bytes of memory.
        p14 = re.compile(r'^cisco +(?P<chassis>[\S]+) '
                         r'+\((?P<processor_type>[\S]+)\) +processor +with '
                         r'+(?P<main_mem>\d+).+ +bytes +of +memory.$')

        # Processor board ID CAT2242L6CG
        p15 = re.compile(r'^Processor +board +ID '
                         r'+(?P<processor_board_id>.+)$') 

        # 44 Virtual Ethernet interfaces
        p16 = re.compile(r'^(?P<virtual_ethernet_interfaces>\d+) +Virtual'
            r' +Ethernet +interfaces$')

        # 32 Forty Gigabit Ethernet interfaces
        p17 = re.compile(r'^(?P<forty_gigabit_ethernet_interfaces>\d+)'
            r' +Forty +Gigabit +Ethernet +interfaces$')

        # 16 Hundred Gigabit Ethernet interfaces
        p18 = re.compile(r'^(?P<hundred_gigabit_ethernet_interfaces>\d+)'
            r' +Hundred +Gigabit +Ethernet +interfaces$')

        # 32768K bytes of non-volatile configuration memory.
        p19 = re.compile(r'^(?P<non_volatile_memory>\d+)K'
            r' +bytes +of +non-volatile +configuration +memory.$')

        # 16002848K bytes of physical memory.
        p20 = re.compile(r'^(?P<physical_memory>\d+)K'
            r' +bytes +of +physical +memory.$')

        # 11161600K bytes of Bootflash at bootflash:.
        p21 = re.compile(r'^(?P<bootflash_size>\d+)K'
            r' +bytes +of +Bootflash +at +bootflash:.$')

        # 1638400K bytes of Crash Files at crashinfo:.
        p22 = re.compile(r'^(?P<crash_size>\d+)K'
            r' +bytes +of +Crash +Files +at +crashinfo:.$')

        # Base Ethernet MAC Address          : 70:b3:17:ff:65:60
        p23 = re.compile(r'^Base +Ethernet +MAC +Address +: '
                         r'+(?P<mac_address>\S+)$')

        # Motherboard Assembly Number        : 47A7
        p24 = re.compile(r'^Motherboard +Assembly +Number +: '
                         r'+(?P<mb_assembly_num>\S+)$')
        
        # Motherboard Serial Number          : CAT2242L6CG
        p25 = re.compile(r'^Motherboard +Serial +Number +: '
                         r'+(?P<mb_sn>\S+)$')

        # Model Revision Number              : V02
        p26 = re.compile(r'^Model +Revision +Number +: '
                         r'+(?P<model_rev_num>\S+)$')

        # Motherboard Revision Number        : A4
        p27 = re.compile(r'^Motherboard +Revision +Number +: '
                         r'+(?P<mb_rev_num>\S+)$')

        # Model Number                       : C9500-32QC 
        p28 = re.compile(r'^Model +Number +: +(?P<model_num>\S+)$')

        # System Serial Number               : CAT2242L6CG
        p29 = re.compile(r'^System +Serial +Number +\: +(?P<system_sn>\S+)$')

        # Configuration register is 0x102
        p30 = re.compile(r'^Configuration +register +is '
                         r'+(?P<curr_config_register>[\S]+)')

        # Compiled Thu 31-Oct-19 17:43 by makale
        p31 = re.compile(r'^Compiled +(?P<compiled_date>[\S\s]+) +by '
                         r'+(?P<compiled_by>\S+)$')

        # Cisco IOS-XE software, Copyright (c) 2005-2019 by cisco Systems, Inc.
        p32 = re.compile(r'^Cisco +(?P<os>\S+) +software.*$')

        for line in out.splitlines():
            line = line.strip()

            # Cisco IOS XE Software, Version 2019-10-31_17.49_makale
            # Cisco IOS XE Software, Version BLD_POLARIS_DEV_LATEST_20210302_012043
            m = p0.match(line)
            if m:
                if 'version' not in ver_dict:
                    version_dict = ver_dict.setdefault('version', {})
                xe_version = m.groupdict()['xe_version']
                version_dict['xe_version'] = xe_version
                continue

            # Cisco IOS Software [Amsterdam], Catalyst L3 Switch Software (CAT9K_IOSXE), Experimental Version 17.2.20191101:003833 [HEAD-/nobackup/makale/puntject2/polaris 106]
            m = p1.match(line)
            if m:
                if 'version' not in ver_dict:
                    version_dict = ver_dict.setdefault('version', {})

                version = m.groupdict()['version']
                m1_1 = p1_1.match(version)
                if m1_1:
                    version_dict['version_short'] = \
                        m1_1.groupdict()['ver_short']

                version_dict['code_name'] = m.groupdict()['code_name']
                version_dict['platform'] = m.groupdict()['platform']
                version_dict['image_id'] = m.groupdict()['image_id']
                version_dict['version'] = m.groupdict()['version']
                if m.groupdict()['label']:
                    version_dict['label'] = m.groupdict()['label']
                if m.groupdict()['build_label']:
                    version_dict['build_label'] = m.groupdict()['build_label']
                continue

            # Copyright (c) 1986-2016 by Cisco Systems, Inc.
            m = p2.match(line)
            if m:
                continue

            # Technical Support: http://www.cisco.com/techsupport
            m = p3.match(line)
            if m:
                continue

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
                intf_dict['virtual_ethernet_interfaces'] = m.groupdict()['virtual_ethernet_interfaces'].lower().replace(' ', '')
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

            # Base Ethernet MAC Address          : 70:b3:17:ff:65:60
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


# =============================
#  Schema for 'show redundancy'
# =============================
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
                        Optional('config_register'): str,
                        'compiled_by': str,
                        'compiled_date': str,
                    }
                }
            }


# =============================
#  Parser for 'show redundancy'
# =============================
class ShowRedundancy(ShowRedundancySchema):

    """Parser for show redundancy"""

    cli_command = ['show redundancy']
    exclude = ['available_system_uptime', 'uptime_in_curr_state']


    def cli(self, output=None):

        if output is None:
            out = self.device.execute(self.cli_command[0])
        else:
            out = output

        redundancy_dict = {}

        # Available system uptime = 1 day, 18 hours, 48 minutes
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

        # Configured Redundancy Mode = Non-redundant
        p6 = re.compile(
            r'Configured +Redundancy +Mode += +(?P<conf_red_mode>\S+)$')

        # Operating Redundancy Mode = Non-redundant
        p7 = re.compile(
            r'^Operating +Redundancy +Mode += +(?P<oper_red_mode>\S+)$')

        # Maintenance Mode = Disabled
        p8 = re.compile(
            r'^Maintenance +Mode += +(?P<maint_mode>\S+)$')

        # Communications = Down      Reason: Failure
        p9 = re.compile(r'^Communications += +(?P<communications>\S+)\s+Reason: +(?P<communications_reason>[\S\s]+)$')

        # Active Location = slot 1
        p10 = re.compile(r'^Active +Location += +(?P<slot>[\S\s]+)$')

        # Current Software state = ACTIVE
        p11 = re.compile(r'^Current +Software +state += +(?P<curr_sw_state>\S+)$')

        # Uptime in current state = 1 day, 18 hours, 48 minutes
        p12 = re.compile(r'^Uptime +in +current +state += +(?P<uptime_in_curr_state>[\S\s]+)$')

        # Image Version = Cisco IOS Software [Amsterdam], Catalyst L3 Switch Software (CAT9K_IOSXE), Experimental Version 17.2.20191101:003833 [HEAD-/nobackup/makale/puntject2/polaris 106]
        p13 = re.compile(r'^Image +Version += +(?P<image_ver>.+)$')

        # BOOT = bootflash:/ecr.bin;
        p14 = re.compile(r'^BOOT += +(?P<boot>.+)$')

        # Configuration register = 0x102
        p15 = re.compile(r'^Configuration +register = (?P<config_register>\S+)$')

        # Compiled Thu 31-Oct-19 17:43 by makale
        p16 = re.compile(r'^Compiled +(?P<compiled_date>[\S\s]+) +by '
                         r'+(?P<compiled_by>\S+)$')

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
                red_dict['hw_mode'] = \
                    m.groupdict()['hw_mode']
                continue

            # Configured Redundancy Mode = Non-redundant
            m = p6.match(line)
            if m:
                red_dict['conf_red_mode'] = \
                    m.groupdict()['conf_red_mode']
                continue

            # Operating Redundancy Mode = Non-redundant
            m = p7.match(line)
            if m:
                red_dict['oper_red_mode'] = \
                    m.groupdict()['oper_red_mode']
                continue

            # Maintenance Mode = Disabled
            m = p8.match(line)
            if m:
                red_dict['maint_mode'] = \
                    m.groupdict()['maint_mode']
                continue

            # Communications = Down      Reason: Failure
            m = p9.match(line)
            if m:
                red_dict['communications'] = \
                    m.groupdict()['communications']
                red_dict['communications_reason'] = \
                    m.groupdict()['communications_reason']
                continue

            # Active Location = slot 1
            m = p10.match(line)
            if m:
                slot = m.groupdict()['slot']
                if 'slot' not in redundancy_dict:
                    slot_dict = redundancy_dict.setdefault(
                        'slot', {}).setdefault(slot, {})
                continue

            # Current Software state = ACTIVE
            m = p11.match(line)
            if m:
                if 'slot' in redundancy_dict:
                    slot_dict['curr_sw_state'] = \
                        m.groupdict()['curr_sw_state']
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
                    slot_dict['image_ver'] = \
                        m.groupdict()['image_ver']
                continue

            # BOOT = bootflash:/ecr.bin;
            m = p14.match(line)
            if m:
                if 'slot' in redundancy_dict:
                    slot_dict['boot'] = \
                        m.groupdict()['boot']
                continue

            # Configuration register = 0x102
            m = p15.match(line)
            if m:
                if 'slot' in redundancy_dict:
                    slot_dict['config_register'] = \
                        m.groupdict()['config_register']
                continue

            # Compiled Thu 31-Oct-19 17:43 by makale
            m = p16.match(line)
            if m:
                if 'slot' in redundancy_dict:
                    slot_dict['compiled_by'] = \
                        m.groupdict()['compiled_by']
                    slot_dict['compiled_date'] = \
                        m.groupdict()['compiled_date']
                continue

        return redundancy_dict


# ============================
#  Schema for 'show inventory'
# ============================
class ShowInventorySchema(MetaParser):

    ''' Schema for:
        * 'show inventory'
    '''

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


# ============================
#  Parser for 'show inventory'
# ============================
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


# ===========================
#  Schema for 'show platform'
# ===========================
class ShowPlatformSchema(MetaParser):

    """Schema for show platform"""

    schema = {
            'chassis': str,
            'slot': {
                Any(): {
                    Optional('cpld_ver'): str,
                    Optional('fw_ver'): str,
                    'insert_time': str,
                    'name': str,
                    'slot': str,
                    'state': str,
                    Optional('subslot'): {
                        Any(): {
                            'insert_time': str,
                            'name': str,
                            'state': str,
                            'subslot': str,
                        },
                    }
                },
            }
        }


# ===========================
#  Parser for 'show platform'
# ===========================
class ShowPlatform(ShowPlatformSchema):

    ''' Parser for:
        * 'show platform'
    '''

    cli_command = ['show platform']
    exclude = ['insert_time']

    def cli(self, output=None):

        if output is None:
            out = self.device.execute(self.cli_command[0])
        else:
            out = output

        platform_dict = {}

        # Chassis type: C9500-32QC 
        p0 = re.compile(r'^Chassis +type: +(?P<chassis>\S+)$')

        # Slot      Type                State                 Insert time (ago) 
        # --------- ------------------- --------------------- ----------------- 
        # 1         C9500-32QC          ok                    1d18h
        p1 = re.compile(r'^(?P<slot>[\w\d]+) +(?P<name>\S+) +'
                         '(?P<state>\w+(\, \w+)?) +(?P<insert_time>\S+)$')

        # Slot      Type                State                 Insert time (ago) 
        # --------- ------------------- --------------------- ----------------- 
        #  1/0      C9500-32QC          ok                    1d18h
        p2 = re.compile(r'^(?P<slot>\S+)\/(?P<subslot>\d+) +(?P<name>\S+) +'
                         '(?P<state>\w+(\, \w+)?) +(?P<insert_time>\S+)$')

        # Slot      CPLD Version        Firmware Version                        
        # --------- ------------------- --------------------------------------- 
        # 1         19061022            17.1.1[FC2] 
        p3 = re.compile(r'^(?P<slot>\S+) +(?P<cpld_version>\d+) +'
                         '(?P<fireware_ver>\S+)$')

        for line in out.splitlines():
            line = line.strip()

            # Chassis type: C9500-32QC 
            m = p0.match(line)
            if m:
                chassis = m.groupdict()['chassis']
                platform_dict.setdefault('chassis', chassis)
                continue

            # Slot      Type                State                 Insert time (ago) 
            # --------- ------------------- --------------------- ----------------- 
            # 1         C9500-32QC          ok                    1d18h
            m = p1.match(line)
            if m:
                slot = m.groupdict()['slot']
                slot_dict = platform_dict.setdefault('slot', {}).setdefault(slot, {})
                slot_dict['name'] = m.groupdict()['name']
                slot_dict['state'] = m.groupdict()['state']
                slot_dict['insert_time'] = m.groupdict()['insert_time']
                slot_dict['slot'] = slot
                continue

            # Slot      Type                State                 Insert time (ago) 
            # --------- ------------------- --------------------- ----------------- 
            #  1/0      C9500-32QC          ok                    1d18h
            m = p2.match(line)
            if m:
                slot = m.groupdict()['slot']
                subslot = m.groupdict()['subslot']
                subslot_dict = platform_dict.setdefault('slot', {}).setdefault(
                    slot, {}).setdefault('subslot', {}).setdefault(subslot, {})
                subslot_dict['name'] = m.groupdict()['name']
                subslot_dict['state'] = m.groupdict()['state']
                subslot_dict['insert_time'] = m.groupdict()['insert_time']
                subslot_dict['subslot'] = subslot
                continue

            # Slot      CPLD Version        Firmware Version                        
            # --------- ------------------- --------------------------------------- 
            # 1         19061022            17.1.1[FC2] 
            m = p3.match(line)
            if m:
                slot = m.groupdict()['slot']
                slot_dict = platform_dict.setdefault('slot', {}).setdefault(slot, {})
                slot_dict['cpld_ver'] = m.groupdict()['cpld_version']
                slot_dict['fw_ver'] = m.groupdict()['fireware_ver']
                continue

        return platform_dict


# ============================================================
#  Schema for 'show platform software fed active ifm mappings'
# ============================================================
class ShowPlatformIfmMappingSchema(MetaParser):
    """Schema for show platform software fed switch active ifm mappings"""
    
    schema = {'interface':
                 {Any(): 
                     {'IF_ID': str,
                      'Inst': str,     
                      'Asic': str,
                      'Core': str,
                      'Port': str,  					
                      'SubPort': str,
                      'Mac' : str,
                      'Cntx': str,
                      'LPN' : str,
                      'GPN' : str,
                      'Type': str,
                      'Active': str,  				
                    }                
                },
            }


# ============================================================
#  Parser for 'show platform software fed active ifm mappings'
# ============================================================
class ShowPlatformIfmMapping(ShowPlatformIfmMappingSchema):

    """ Parser for show platform software fed switch active ifm mappings"""

    cli_command = ['show platform software fed switch {state} ifm mappings',
                   'show platform software fed active ifm mappings']

    def cli(self, state="", output=None):
       
        if output is None:
            if state:
                cmd = self.cli_command[0].format(state=state)            
            else:
                cmd = self.cli_command[1]
         
            # Execute command to get output from device	 
            out = self.device.execute(cmd)            
        else:
            out = output

        # TwentyFiveGigE1/0/1       0x8        1   0   1    20     0      16   4    1    1    NIF  Y  
        p1 = re.compile(r'^(?P<interface>\S+) +(?P<ifId>\S+) +(?P<inst>\d+) +(?P<asic>\d+) +(?P<core>\d+) +(?P<port>\d+) +(?P<sbPort>\d+) +(?P<mac>\d+) +(?P<cntx>\d+) +(?P<lpn>\d+) +(?P<gpn>\d+) +(?P<type>\w+) +(?P<act>\w+)$') 	
        
        # initial variables
        ret_dict = {}
        
        for line in out.splitlines():
            line = line.strip()
            if not line: 
                continue

            # TwentyFiveGigE1/0/1       0x8        1   0   1    20     0      16   4    1    1    NIF  Y
            m = p1.match(line)
            if m:
                group    = m.groupdict()		
                intfId   = group['interface']
                ifId     = group['ifId']
                instance = group['inst']
                asic     = group['asic']
                core     = group['core']
                port     = group['port']
                subPort  = group['sbPort']
                mac      = group['mac']
                cntx     = group['cntx']
                lpn      = group['lpn']
                gpn      = group['gpn']
                typ     = group['type']
                active   = group['act']  				
        
                final_dict = ret_dict.setdefault('interface',{}).setdefault(intfId,{})
        
                final_dict['IF_ID']   = ifId					
                final_dict['Inst']    = instance
                final_dict['Asic']    = asic 
                final_dict['Core']    = core
                final_dict['Port']    = port
                final_dict['SubPort'] = subPort
                final_dict['Mac']     = mac 
                final_dict['Cntx']    = cntx 
                final_dict['LPN']     = lpn 
                final_dict['GPN']     = gpn 
                final_dict['Type']    = typ
                final_dict['Active']  = active  				
                continue            
            
        return ret_dict


# ========================================
# Parser for 'show platform software'
# ========================================
class ShowPlatformSoftwareSchema(MetaParser):

    ''' Schema for "show Platform software" '''

    schema = {
        Optional('statistics'):
                {Optional('object-update'):
                    {Optional('pending-issue'):int,
                     Optional('pending-ack'):int,
                    },
                Optional('batch-begin'):
                    {Optional('pending-issue'):int,
                     Optional('pending-ack'):int,
                    },
                Optional('batch-end'):
                    {Optional('pending-issue'):int,
                     Optional('pending-ack'):int,
                    },
                Optional('command'):
                    {Optional('pending-ack'):int,
                    },
                Optional('total-objects'):int,
                Optional('stale-objects'): int,
                Optional('resolve-objects'): int,
                Optional('childless-delete-objects'): int,
                Optional('backplane-objects'): int,
                Optional('error-objects'): int,
                Optional('number-of-bundles'): int,
                Optional('paused-types'): int,
                },
        }

# ========================================
# Parser for 'show platform software'
# ========================================
class ShowPlatformSoftware(ShowPlatformSoftwareSchema):
    ''' Parser for
      "show platform software object-manager switch {switchvirtualstate} {serviceprocessor} statistics"
    '''

    cli_command = ['show platform software object-manager switch {switchvirtualstate} {serviceprocessor} statistics']

    def cli(self, switchvirtualstate="", serviceprocessor="", output=None):
        if output is None:
            cmd = self.cli_command[0].format(switchvirtualstate=switchvirtualstate,
                                             serviceprocessor=serviceprocessor)
            output = self.device.execute(cmd)

        # Init vars
        ret_dict = {}

        #Forwarding Manager Asynchronous Object Manager Statistics
        p1 = re.compile(r'^Forwarding +Manager +Asynchronous +Object Manager*\s+(?P<statistics>(\S+))$')

        #Object update: Pending-issue: 0, Pending-acknowledgement: 0
        p2 = re.compile(r'^Object +update:\s+Pending-issue:\s+(?P<pending_issue>\d+), +'
                         'Pending-acknowledgement:\s+(?P<pending_ack>\d+)$')

        #Batch begin:   Pending-issue: 0, Pending-acknowledgement: 0
        p3 = re.compile(r'Batch +begin:\s+Pending-issue:\s+(?P<pending_issue>\d+), +'
                         'Pending-acknowledgement:\s+(?P<pending_ack>\d+)$')

        #Batch end:     Pending-issue: 0, Pending-acknowledgement: 0
        p4 = re.compile(r'Batch +end:\s+Pending-issue:\s+(?P<pending_issue>\d+), +'
                         'Pending-acknowledgement:\s+(?P<pending_ack>\d+)$')

        #Command:       Pending-acknowledgement: 0
        p5 = re.compile(r'Command:\s+Pending-acknowledgement:\s+(?P<pending_ack>\d+)')

        #Total-objects: 1231
        #Stale-objects: 0
        #Resolve-objects: 0
        #Childless-delete-objects: 0
        #Backplane-objects: 0
        #Error-objects: 0
        #Number of bundles: 0
        #Paused-types: 5
        p6 = re.compile(r'^(?P<key>[\S ]+): +(?P<value>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            #Forwarding Manager Asynchronous Object Manager Statistics
            m = p1.match(line)
            if m:
                stats_dict = ret_dict.setdefault('statistics', {})
                continue

            #Object update: Pending-issue: 0, Pending-acknowledgement: 0
            m = p2.match(line)
            if m:
                object_update_dict = stats_dict.setdefault('object-update', {})
                pending_issue = int(m.groupdict()['pending_issue'])
                pending_ack = int(m.groupdict()['pending_ack'])
                object_update_dict['pending-issue']= pending_issue
                object_update_dict['pending-ack']= pending_ack
                continue

            #Batch begin:   Pending-issue: 0, Pending-acknowledgement: 0
            m = p3.match(line)
            if m:
                batch_begin_dict = stats_dict.setdefault('batch-begin', {})
                pending_issue = int(m.groupdict()['pending_issue'])
                pending_ack = int(m.groupdict()['pending_ack'])
                batch_begin_dict['pending-issue']= pending_issue
                batch_begin_dict['pending-ack']= pending_ack
                continue

            #Batch end:     Pending-issue: 0, Pending-acknowledgement: 0
            m = p4.match(line)
            if m:
                batch_end_dict = stats_dict.setdefault('batch-end', {})
                pending_issue = int(m.groupdict()['pending_issue'])
                pending_ack = int(m.groupdict()['pending_ack'])
                batch_end_dict['pending-issue']= pending_issue
                batch_end_dict['pending-ack']= pending_ack
                continue

            #Command:       Pending-acknowledgement: 0
            m = p5.match(line)
            if m:
                command_dict = stats_dict.setdefault('command', {})
                pending_ack = int(m.groupdict()['pending_ack'])
                command_dict['pending-ack']= pending_ack
                continue

            #Total-objects: 1231
            #Stale-objects: 0
            #Resolve-objects: 0
            #Childless-delete-objects: 0
            #Backplane-objects: 0
            #Error-objects: 0
            #Number of bundles: 0
            #Paused-types: 5

            m = p6.match(line)
            if m:
                groups = m.groupdict()
                scrubbed = groups['key'].replace(' ', '-')
                stats_dict.update({scrubbed.lower(): int(groups['value'])})
                continue

        return ret_dict

class ShowPlatformHardwareChassisFantrayDetailSchema(MetaParser):
    """
    Schema for show platform hardware chassis fantray detail 
    """
    schema = {
        Optional('control_mode'): str,
        Optional('monitor_mode'): str,
        Optional('duty_cycle'): str,
        'fantray_details':{
            Any(): {
                'fan':{
                    Any(): {
                        'inlet_rpm': int,
                        'outlet_rpm': int,
                    },
                },
            },
        },
    }

class ShowPlatformHardwareChassisFantrayDetail(ShowPlatformHardwareChassisFantrayDetailSchema):
    """ Parser for show platform hardware chassis fantray detail"""

    cli_command = 'show platform hardware chassis fantray detail'

    def cli(self, output=None): 
        if output is None:
            # excute command to get output
            output = self.device.execute(self.cli_command)

        # initial variables
        ret_dict = {}

        # Control Mode:   Auto, Monitor Mode:   Auto, Duty Cycle: 50.20%
        p1 = re.compile(r'^Control Mode:\s+(?P<control_mode>\w+)\, Monitor Mode:\s+(?P<monitor_mode>\w+)\, Duty Cycle:\s+(?P<duty_cycle>\S+)')

        #  Fan tray-1:
        p2 = re.compile(r'^(?P<fan_tray>\bFan \w+-\d+)')

        # FAN1 Inlet:  11062 RPM, Outlet:   9984 RPM
        # FAN2 Inlet:  11039 RPM, Outlet:  10007 RPM
        p3 = re.compile(r'^(?P<fan>\bFAN\d+) Inlet:\s+(?P<inlet_rpm>\d+) +RPM\, +Outlet:\s+(?P<outlet_rpm>\d+) +RPM$')

        for line in output.splitlines():
            line = line.strip()

            # Control Mode:   Auto, Monitor Mode:   Auto, Duty Cycle: 50.20%
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['control_mode'] = group['control_mode']
                ret_dict['monitor_mode'] = group['monitor_mode']
                ret_dict['duty_cycle'] = group['duty_cycle']
                continue

            #  Fan tray-1:
            m = p2.match(line)
            if m:
                group = m.groupdict()
                root_dict = ret_dict.setdefault('fantray_details',{}).setdefault(group['fan_tray'],{})
                continue
                
            # FAN1 Inlet:  11062 RPM, Outlet:   9984 RPM
            # FAN2 Inlet:  11039 RPM, Outlet:  10007 RPM
            m = p3.match(line)
            if m:
                group = m.groupdict()
                fan_dict = root_dict.setdefault('fan',{}).setdefault(group['fan'],{})
                fan_dict['inlet_rpm'] = int(group['inlet_rpm'])
                fan_dict['outlet_rpm'] = int(group['outlet_rpm'])
                continue

        return ret_dict



class ShowPlatformHardwareChassisPowerSupplyDetailAllSchema(MetaParser):
    """
    Schema for show platform hardware chassis power-supply detail all
    """
    schema = {
        'power_supply_details' : {
            Any(): {
                'input_voltage_volt': str,
                'output_voltage_volt': str,
                'input_power_watt':str,
                'output_power_watt': str,
                'input_current_amp': str,
                'output_current_amp':str,
                'temperature_celsius': {
                    'temperature_1': str,
                    'temperature_2': str,
                    'temperature_3':str,
                },
                Optional('fan_speed_1_rpm'):str
            },
        },
    }

class ShowPlatformHardwareChassisPowerSupplyDetailAll(ShowPlatformHardwareChassisPowerSupplyDetailAllSchema):
    """ Parser for show platform hardware chassis power-supply detail all"""

    cli_command = 'show platform hardware chassis power-supply detail all'

    def cli(self, output=None): 
        if output is None:
            # excute command to get output
            output = self.device.execute(self.cli_command)

        # initial variables
        ret_dict = {}

        # PS1:
        p1 = re.compile('^(?P<power_supply>.+)\:$')

        # Input Voltage   :     231.0000 V
        p2 = re.compile('^Input\s+Voltage\s+:\s+(?P<input_voltage_volt>\d+\.\d+) V$')

        # Output Voltage  :      11.9490 V
        p3 = re.compile('^Output\s+Voltage\s+:\s+(?P<output_voltage_volt>\d+\.\d+) V$')

        # Input Power     :     165.0000 W
        p4 = re.compile('^Input\s+Power\s+:\s+(?P<input_power_watt>\d+\.\d+) W$')

        # Output Power    :     150.0000 W
        p5 = re.compile('^Output\s+(Power|power)\s+:\s+(?P<output_power_watt>\d+\.\d+) W$')

        # Input Current   :       0.7180 A
        p6 = re.compile('^Input\s+Current\s+:\s+(?P<input_current_amp>\d+\.\d+) A$')

        # Output Current  :      12.4840 A
        p7 = re.compile('^Output\s+Current\s+:\s+(?P<output_current_amp>\d+\.\d+) A$')

        # Temperature 1   :      30.7500 C
        p8 = re.compile('^Temperature *1\s+:\s+(?P<temperature1_celsius>\d+\.\d+) C$')

        # Temperature 2   :      33.0000 C
        p9 = re.compile('^Temperature *2\s+:\s+(?P<temperature2_celsius>\d+\.\d+) C$')

        # Temperature 3   :      33.5000 C
        p10 = re.compile('^Temperature *3\s+:\s+(?P<temperature3_celsius>\d+\.\d+) C$')

        # Fan Speed 1     :   10016.0000 RPM
        p11= re.compile('^Fan\s+Speed\s+1\s+:\s+(?P<fan_speed_1_rpm>\d+\.\d+) RPM$')

        for line in output.splitlines():
            line=line.strip()

            # PS1:
            m = p1.match(line)
            if m:
                group = m.groupdict()
                power_dict=ret_dict.setdefault('power_supply_details',{})
                root_dict=power_dict.setdefault(group['power_supply'],{})
                temp_dict=root_dict.setdefault('temperature_celsius',{})
                continue

            # Input Voltage   :     231.0000 V    
            m = p2.match(line)
            if m:
                group = m.groupdict()
                root_dict['input_voltage_volt'] = group['input_voltage_volt']
                continue

            # Output Voltage  :      11.9490 V
            m = p3.match(line)
            if m:
                group = m.groupdict()
                root_dict['output_voltage_volt'] = group['output_voltage_volt']
                continue

            # Input Power     :     165.0000 W
            m = p4.match(line)
            if m:
                group = m.groupdict()
                root_dict['input_power_watt'] = group['input_power_watt']
                continue

            # Output Power    :     150.0000 W
            m = p5.match(line)
            if m:
                group = m.groupdict()
                root_dict['output_power_watt'] = group['output_power_watt']
                continue

            # Input Current   :       0.7180 A
            m = p6.match(line)
            if m:
                group = m.groupdict()
                root_dict['input_current_amp'] = group['input_current_amp']
                continue

            # Output Current  :      12.4840 A
            m = p7.match(line)
            if m:
                group = m.groupdict()
                root_dict['output_current_amp'] = group['output_current_amp']
                continue

            
            
            # Temperature 1   :      30.7500 C
            # Temperature1    :      23.5000 C
            m = p8.match(line)
            if m:
                group = m.groupdict()
                temp_dict['temperature_1'] = group['temperature1_celsius']
                continue

            # Temperature 2   :      33.0000 C
            # Temperature2    :      28.0000 C
            m = p9.match(line)
            if m:
                group = m.groupdict()
                temp_dict['temperature_2'] = group['temperature2_celsius']
                continue

            # Temperature 3   :      33.5000 C
            # Temperature3    :      23.7500 C
            m = p10.match(line)
            if m:
                group = m.groupdict()
                temp_dict['temperature_3'] = group['temperature3_celsius']
                continue

            # Fan Speed 1     :   10016.0000 RPM
            m = p11.match(line)
            if m:
                group = m.groupdict()
                root_dict['fan_speed_1_rpm'] = group['fan_speed_1_rpm']
                continue

        return ret_dict
        
class ShowPlatformHardwareChassisFantrayDetailSwitchSchema(MetaParser):
    """
    Schema for show platform hardware chassis fantray detail switch {mode}
    """
    schema = {
        Optional('control_mode'): str,
        Optional('monitor_mode'): str,
        Optional('duty_cycle'): str,
        'fantray_details':{
            Any(): {
                'fan':{
                    Any(): {
                        'inlet_rpm': int,
                        'outlet_rpm': int,
                    },
                },
            },
        },
    }

class ShowPlatformHardwareChassisFantrayDetailSwitch(ShowPlatformHardwareChassisFantrayDetailSwitchSchema):
    """ Parser for show platform hardware chassis fantray detail switch {mode}"""

    cli_command = 'show platform hardware chassis fantray detail switch {mode}'

    def cli(self, mode, output=None): 
        if output is None:
            # excute command to get output
            output = self.device.execute(self.cli_command.format(mode=mode))

        # initial variables
        ret_dict = {}

        # Control Mode:   Auto, Monitor Mode:   Auto, Duty Cycle: 50.20%
        p1 = re.compile(r'^Control Mode:\s+(?P<control_mode>\w+)\, Monitor Mode:\s+(?P<monitor_mode>\w+)\, Duty Cycle:\s+(?P<duty_cycle>\S+)')

        #  Fan tray-1:
        p2 = re.compile(r'^(?P<fan_tray>\bFan \w+-\d+)')

        # FAN1 Inlet:  11062 RPM, Outlet:   9984 RPM
        # FAN2 Inlet:  11039 RPM, Outlet:  10007 RPM
        p3 = re.compile(r'^(?P<fan>\bFAN\d+) Inlet:\s+(?P<inlet_rpm>\d+) +RPM\, +Outlet:\s+(?P<outlet_rpm>\d+) +RPM$')

        for line in output.splitlines():
            line = line.strip()

            # Control Mode:   Auto, Monitor Mode:   Auto, Duty Cycle: 50.20%
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['control_mode'] = group['control_mode']
                ret_dict['monitor_mode'] = group['monitor_mode']
                ret_dict['duty_cycle'] = group['duty_cycle']
                continue

            #  Fan tray-1:
            m = p2.match(line)
            if m:
                group = m.groupdict()
                root_dict = ret_dict.setdefault('fantray_details',{}).setdefault(group['fan_tray'],{})
                continue
                
            # FAN1 Inlet:  11062 RPM, Outlet:   9984 RPM
            # FAN2 Inlet:  11039 RPM, Outlet:  10007 RPM
            m = p3.match(line)
            if m:
                group = m.groupdict()
                fan_dict = root_dict.setdefault('fan',{}).setdefault(group['fan'],{})
                fan_dict['inlet_rpm'] = int(group['inlet_rpm'])
                fan_dict['outlet_rpm'] = int(group['outlet_rpm'])
                continue

        return ret_dict
        
class ShowPlatformHardwareChassisPowerSupplyDetailSwitchAllSchema(MetaParser):
    """
    Schema for show platform hardware chassis power-supply detail switch {mode} all
    """
    schema = {
        'power_supply_details' : {
            Any(): {
                'input_voltage_volt': str,
                'output_voltage_volt': str,
                'input_power_watt':str,
                'output_power_watt': str,
                'input_current_amp': str,
                'output_current_amp':str,
                'temperature_celsius': {
                    'temperature_1': str,
                    'temperature_2': str,
                    'temperature_3':str,
                },
                Optional('fan_speed_1_rpm'):str
            },
        },
    }

class ShowPlatformHardwareChassisPowerSupplyDetailSwitchAll(ShowPlatformHardwareChassisPowerSupplyDetailSwitchAllSchema):
    """ Parser for show platform hardware chassis power-supply detail switch {mode} all"""

    cli_command = 'show platform hardware chassis power-supply detail switch {mode} all'

    def cli(self, mode, output=None): 
        if output is None:
            # excute command to get output
            output = self.device.execute(self.cli_command.format(mode=mode))
        else:
            output = output
        # initial variables
        ret_dict = {}

        # PS1:
        p1 = re.compile('^(?P<power_supply>.+)\:$')

        # Input Voltage   :     231.0000 V
        p2 = re.compile('^Input\s+Voltage\s+:\s+(?P<input_voltage_volt>\d+\.\d+) V$')

        # Output Voltage  :      11.9490 V
        p3 = re.compile('^Output\s+Voltage\s+:\s+(?P<output_voltage_volt>\d+\.\d+) V$')

        # Input Power     :     165.0000 W
        p4 = re.compile('^Input\s+Power\s+:\s+(?P<input_power_watt>\d+\.\d+) W$')

        # Output Power    :     150.0000 W
        p5 = re.compile('^Output\s+(Power|power)\s+:\s+(?P<output_power_watt>\d+\.\d+) W$')

        # Input Current   :       0.7180 A
        p6 = re.compile('^Input\s+Current\s+:\s+(?P<input_current_amp>\d+\.\d+) A$')

        # Output Current  :      12.4840 A
        p7 = re.compile('^Output\s+Current\s+:\s+(?P<output_current_amp>\d+\.\d+) A$')

        # Temperature 1   :      30.7500 C
        p8 = re.compile('^Temperature *1\s+:\s+(?P<temperature1_celsius>\d+\.\d+) C$')

        # Temperature 2   :      33.0000 C
        p9 = re.compile('^Temperature *2\s+:\s+(?P<temperature2_celsius>\d+\.\d+) C$')

        # Temperature 3   :      33.5000 C
        p10 = re.compile('^Temperature *3\s+:\s+(?P<temperature3_celsius>\d+\.\d+) C$')

        # Fan Speed 1     :   10016.0000 RPM
        p11= re.compile('^Fan\s+Speed\s+1\s+:\s+(?P<fan_speed_1_rpm>\d+\.\d+) RPM$')

        for line in output.splitlines():
            line=line.strip()

            # PS1:
            m = p1.match(line)
            if m:
                group = m.groupdict()
                power_dict=ret_dict.setdefault('power_supply_details',{})
                root_dict=power_dict.setdefault(group['power_supply'],{})
                temp_dict=root_dict.setdefault('temperature_celsius',{})
                continue

            # Input Voltage   :     231.0000 V    
            m = p2.match(line)
            if m:
                group = m.groupdict()
                root_dict['input_voltage_volt'] = group['input_voltage_volt']
                continue

            # Output Voltage  :      11.9490 V
            m = p3.match(line)
            if m:
                group = m.groupdict()
                root_dict['output_voltage_volt'] = group['output_voltage_volt']
                continue

            # Input Power     :     165.0000 W
            m = p4.match(line)
            if m:
                group = m.groupdict()
                root_dict['input_power_watt'] = group['input_power_watt']
                continue

            # Output Power    :     150.0000 W
            m = p5.match(line)
            if m:
                group = m.groupdict()
                root_dict['output_power_watt'] = group['output_power_watt']
                continue

            # Input Current   :       0.7180 A
            m = p6.match(line)
            if m:
                group = m.groupdict()
                root_dict['input_current_amp'] = group['input_current_amp']
                continue

            # Output Current  :      12.4840 A
            m = p7.match(line)
            if m:
                group = m.groupdict()
                root_dict['output_current_amp'] = group['output_current_amp']
                continue

            
            
            # Temperature 1   :      30.7500 C
            # Temperature1    :      23.5000 C
            m = p8.match(line)
            if m:
                group = m.groupdict()
                temp_dict['temperature_1'] = group['temperature1_celsius']
                continue

            # Temperature 2   :      33.0000 C
            # Temperature2    :      28.0000 C
            m = p9.match(line)
            if m:
                group = m.groupdict()
                temp_dict['temperature_2'] = group['temperature2_celsius']
                continue

            # Temperature 3   :      33.5000 C
            # Temperature3    :      23.7500 C
            m = p10.match(line)
            if m:
                group = m.groupdict()
                temp_dict['temperature_3'] = group['temperature3_celsius']
                continue

            # Fan Speed 1     :   10016.0000 RPM
            m = p11.match(line)
            if m:
                group = m.groupdict()
                root_dict['fan_speed_1_rpm'] = group['fan_speed_1_rpm']
                continue
        return ret_dict

# ================================================================================================
# Schema for 'show platform hardware fed switch active fwd-asic resource tcam table pbr record 0 format 0'
# ================================================================================================

class ShowPlatformFedTcamPbrNatSchema(MetaParser):
    """Schema for show platform hardware fed switch active fwd-asic resource tcam table pbr record 0 format 0 | begin {nat_region}"""

    schema = {
        Any():{
            Optional('index'):{
                Any():{
                    Optional('mask'):{
                        Any(): str,
                    },
                    Optional('key'):{
                        Any(): str,
                    },
                    Optional('ad'): str
                }
            }
        }
    }

# ================================================================================================
# Parser for 'show platform hardware fed switch active fwd-asic resource tcam table pbr record 0 format 0'
# ================================================================================================

class ShowPlatformFedTcamPbrNat(ShowPlatformFedTcamPbrNatSchema):
    """
    show platform hardware fed switch active fwd-asic resource tcam table pbr record 0 format 0 | begin {nat_region}
    """

    cli_command = ['show platform hardware fed {switch} active fwd-asic resource tcam table pbr record 0 format 0 | begin {nat_region}',
                   'show platform hardware fed active fwd-asic resource tcam table pbr record 0 format 0 | begin {nat_region}']

    def cli(self, nat_region, switch="", output=None):

        if output is None:
            if switch:
                cmd = self.cli_command[0].format(switch=switch,nat_region=nat_region)
            else:
                cmd = self.cli_command[1].format(nat_region=nat_region)

            output = self.device.execute(cmd)

        # initial variables
        ret_dict = {}

        # Printing entries for region NAT_1 (387) type 6 asic 0
        p1 = re.compile(r'^Printing entries for region\s(?P<nat_r>\w+)\s\(\d+\)\stype\s\d+\sasic\s\d$')

        # TAQ-0 Index-576 (A:0,C:0) Valid StartF-1 StartA-1 SkipF-0 SkipA-0
        p2 = re.compile(r'^TAQ-\d+\sIndex-(?P<index>\d+)\s\([A-Z]\:\d+,[A-Z]\:\d+\)\sValid\sStart[A-Z]-\d+\sStart[A-Z]-\d+\sSkip[A-Z]-\d+\sSkip[A-Z]-\d+$')

        # Mask1 30fff000:0003ffff:00000000:0000ffff:00000000:00000000:ffffffff:ffffffff
        p3 = re.compile(r'^Mask(?P<mask_name>\d+) +(?P<mask_id>\S+)$')
        # Key1  10119000:00020014:00000000:00000028:00000000:00000000:0f000001:23000001
        p4 = re.compile(r'^Key(?P<key_name>\d+) +(?P<key_id>\S+)$')
        # AD    10087000:000000ae:00000000
        p5 = re.compile(r'^AD +(?P<ad>[\da-f:]+)$')

        for line in output.splitlines():
            line = line.strip()

            # Printing entries for region NAT_1 (387) type 6 asic 0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                nat_r = group['nat_r']
                nat_dict = ret_dict.setdefault(nat_r, {})
                continue

            # TAQ-0 Index-576 (A:0,C:0) Valid StartF-1 StartA-1 SkipF-0 SkipA-0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                index = group['index']
                index_dict = nat_dict.setdefault('index', {}).setdefault(index, {})
                mask_dict = index_dict.setdefault('mask', {})
                key_dict = index_dict.setdefault('key', {})
                continue

            # Mask1 30fff000:0003ffff:00000000:0000ffff:00000000:00000000:ffffffff:ffffffff
            m = p3.match(line)
            if m:
                group = m.groupdict()
                mask_name = group['mask_name']
                mask_dict[mask_name] = group['mask_id']
                continue

            # Key1  10119000:00020014:00000000:00000028:00000000:00000000:0f000001:23000001
            m = p4.match(line)
            if m:
                group = m.groupdict()
                key_name = group['key_name']
                key_dict[key_name] = group['key_id']
                continue

            # AD    10087000:000000ae:00000000
            m = p5.match(line)
            if m:
                group = m.groupdict()
                index_dict['ad'] = group['ad']
                continue

        return ret_dict
