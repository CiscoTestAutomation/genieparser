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
   * show platform software fed active punt entries
   * show platform software fed {switch} active punt entries
   * show platform software fed {switch} active punt entries | include {label}
   * show platform software fed active punt entries | include {label}
   * show platform software fed {switch} active ip route vrf {vrf_name}
   * show platform hardware fed {switch} {mode} fwd-asic resource tcam utilization
   * show platform hardware fed active fwd-asic resource tcam utilization
   * show platform software fed {mode} ip mfib vrf {vrf_name} {group} detail
   * show platform software fed {switch} {mode} ip mfib vrf {vrf_name} {group} detail
   * show platform hardware fed active qos queue config interface {interface}
   * show platform hardware fed switch {switch_var} qos queue config interface {interface}
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
                    'bootldr': str,
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
                    Optional('revision') : str,
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
                    Optional('defect_id'): {
                        Any(): {
                            Optional('type'): str,
                            Optional('sum_version'): str,
                            Optional('state'): str,
                            Optional('file_name'): str,
                        }
                    },
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

        # ROM: IOS-XE ROMMONBOOTLDR: System Bootstrap, Version 17.11.0.1r, DEVELOPMENT SOFTWARE
        p4and5 = re.compile(r'^ROM: +(?P<rom>.+)BOOTLDR: +(?P<bootldr>[\S\s]+)$')

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

        # SMU   CSCvz54210   17.03.03. C  cat9k_iosxe.17.03.03.CSCvz54210.SPA.smu.bin
        # SMU   CSCwc80043   17.03.03. C  cat9k_iosxe.17.03.03.CSCwc80043.SPA.smu.bin
        # SMU   CSCwh29778   17.03.03. C  cat9k_iosxe.17.03.03.CSCwh29778.SPA.smu.bin
        p12_1 = re.compile(r'^(?P<type1>\w+) +(?P<defect_id>\S+) +(?P<sum_version>[\w.]+) +(?P<state>C|U) +(?P<file_name>\S+)$')

        # Next reload AIR license Level: AIR DNA Advantage
        p12 = re.compile(r'^Next +reload +AIR +license +Level: +(?P<next_reload_license_level>.+)$')

        # Smart Licensing Status: UNREGISTERED/EVAL EXPIRED
        p13 = re.compile(r'^Smart +Licensing +Status: +(?P<smart_licensing_status>.+)$')


        # cisco C9500X-60L4D (X86) processor (revision V00) with 5875522K/6147K bytes of memory.
        # cisco C9500-32QC (X86) processor with 1863083K/6147K bytes of memory.
        p14 = re.compile(r'^cisco +(?P<chassis>[\S]+) \((?P<processor_type>[\S]+)\) +processor '
                         r'+(?:(\(revision (?P<revision>\S+)\) +)?)?'
                         r'with +(?P<main_mem>(?<!\S)\d+)+.+bytes +of +memory.$')

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
                if "ROMMONBOOTLDR" not in rom:
                    version_dict['rom'] = rom
                    continue

            # BOOTLDR: System Bootstrap, Version 17.1.1[FC2], RELEASE SOFTWARE (P)
            m = p5.match(line)
            if m:
                version_dict['bootldr_version'] = m.groupdict()['bootldr_version']
                version_dict['bootldr'] = m.groupdict()['bootldr_version']
                continue

            # ROM: IOS-XE ROMMONBOOTLDR: System Bootstrap, Version 17.11.0.1r, DEVELOPMENT SOFTWARE
            m = p4and5.match(line)
            if m:
                version_dict['bootldr_version'] = m.groupdict()['bootldr']
                version_dict['bootldr'] = m.groupdict()['bootldr']
                version_dict['rom'] = m.groupdict()['rom']
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

            # SMU   CSCvz54210   17.03.03. C  cat9k_iosxe.17.03.03.CSCvz54210.SPA.smu.bin
            # SMU   CSCwc80043   17.03.03. C  cat9k_iosxe.17.03.03.CSCwc80043.SPA.smu.bin
            # SMU   CSCwh29778   17.03.03. C  cat9k_iosxe.17.03.03.CSCwh29778.SPA.smu.bin
            m = p12_1.match(line)
            if m:
                group = m.groupdict()
                defect_dict = version_dict.setdefault('defect_id', {}).setdefault(group['defect_id'], {})
                defect_dict.update({
                    'type': group['type1'],
                    'sum_version': group['sum_version'],
                    'state': group['state'],
                    'file_name': group['file_name'],
                })

            # Smart Licensing Status: UNREGISTERED/EVAL EXPIRED
            m = p13.match(line)
            if m:
                version_dict['smart_licensing_status'] = m.groupdict()['smart_licensing_status']
                continue
            # cisco C9500X-60L4D (X86) processor (revision V00) with 5875522K/6147K bytes of memory.
            # cisco C9500-32QC (X86) processor with 1863083K/6147K bytes of memory.
            m = p14.match(line)
            if m:
                version_dict['chassis'] = m.groupdict()['chassis']
                version_dict['processor_type'] = m.groupdict()['processor_type']
                version_dict['main_mem'] = m.groupdict()['main_mem']
                if m.groupdict()['revision'] is not None:
                     version_dict['revision'] = m.groupdict()['revision']


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
                    Optional('communications'): str,
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
                         r' +DESCR: +\"(?P<descr>.*)\"$')

        # PID: QSFP-100G-SR4-S     , VID: V03  , SN: AVF2243S10A
        p2 = re.compile(r'^PID: +(?P<pid>\S+)? *, +VID:(?: +(?P<vid>(\S+)))? *,'
                         r' +SN:(?: +(?P<sn>(\S+)))?$')

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
            Optional('chassis'): str,
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
                         r'(?P<state>\w+(\, \w+)?) +(?P<insert_time>\S+)$')

        # Slot      Type                State                 Insert time (ago)
        # --------- ------------------- --------------------- -----------------
        #  1/0      C9500-32QC          ok                    1d18h
        p2 = re.compile(r'^(?P<slot>\S+)\/(?P<subslot>\d+) +(?P<name>\S+) +'
                         r'(?P<state>\w+(\, \w+)?) +(?P<insert_time>\S+)$')

        # Slot      CPLD Version        Firmware Version
        # --------- ------------------- ---------------------------------------
        # 1         19061022            17.1.1[FC2]
        p3 = re.compile(r'^(?P<slot>\S+) +(?P<cpld_version>\d+) +'
                         r'(?P<fireware_ver>\S+)$')

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

    schema = {
        'interface': {
            Any(): {
                'IF_ID': str,
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
                Optional('ifg_id'): int,
                Optional('first_serdes'): int,
                Optional('last_serdes'): int
            }
        }
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
        # Interface                 IF_ID  Inst Asic Core IFG_ID Port SubPort Mac  First Serdes Last Serdes  Cntx LPN  GPN   Type Active
        # HundredGigE1/0/1          0x406    0   0    5      1    0      0     1    0            1            0    1    1    NIF    Y
        p1 = re.compile(r'^(?P<interface>\S+) +(?P<ifId>\S+) +(?P<inst>\d+) +(?P<asic>\d+) +(?P<core>\d+) +'
                        r'((?P<ifg_id>\d+)\s+)?(?P<port>\d+) +(?P<sbPort>\d+) +(?P<mac>\d+) +((?P<first_serdes>\d+)\s+'
                        r'(?P<last_serdes>\d+)\s+)?(?P<cntx>\d+) +(?P<lpn>\d+) +(?P<gpn>\d+) +(?P<type>\w+) +(?P<act>\w+)$')

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
                if group['ifg_id']:
                    final_dict['ifg_id'] = int(group['ifg_id'])
                if group['first_serdes'] and group['last_serdes']:
                    final_dict['first_serdes'] = int(group['first_serdes'])
                    final_dict['last_serdes'] = int(group['last_serdes'])
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
                         r'Pending-acknowledgement:\s+(?P<pending_ack>\d+)$')

        #Batch begin:   Pending-issue: 0, Pending-acknowledgement: 0
        p3 = re.compile(r'Batch +begin:\s+Pending-issue:\s+(?P<pending_issue>\d+), +'
                         r'Pending-acknowledgement:\s+(?P<pending_ack>\d+)$')

        #Batch end:     Pending-issue: 0, Pending-acknowledgement: 0
        p4 = re.compile(r'Batch +end:\s+Pending-issue:\s+(?P<pending_issue>\d+), +'
                         r'Pending-acknowledgement:\s+(?P<pending_ack>\d+)$')

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
        p1 = re.compile(r'^(?P<power_supply>.+)\:$')

        # Input Voltage   :     231.0000 V
        p2 = re.compile(r'^Input\s+Voltage\s+:\s+(?P<input_voltage_volt>\d+\.\d+) V$')

        # Output Voltage  :      11.9490 V
        p3 = re.compile(r'^Output\s+Voltage\s+:\s+(?P<output_voltage_volt>\d+\.\d+) V$')

        # Input Power     :     165.0000 W
        p4 = re.compile(r'^Input\s+Power\s+:\s+(?P<input_power_watt>\d+\.\d+) W$')

        # Output Power    :     150.0000 W
        p5 = re.compile(r'^Output\s+(Power|power)\s+:\s+(?P<output_power_watt>\d+\.\d+) W$')

        # Input Current   :       0.7180 A
        p6 = re.compile(r'^Input\s+Current\s+:\s+(?P<input_current_amp>\d+\.\d+) A$')

        # Output Current  :      12.4840 A
        p7 = re.compile(r'^Output\s+Current\s+:\s+(?P<output_current_amp>\d+\.\d+) A$')

        # Temperature 1   :      30.7500 C
        p8 = re.compile(r'^Temperature *1\s+:\s+(?P<temperature1_celsius>\d+\.\d+) C$')

        # Temperature 2   :      33.0000 C
        p9 = re.compile(r'^Temperature *2\s+:\s+(?P<temperature2_celsius>\d+\.\d+) C$')

        # Temperature 3   :      33.5000 C
        p10 = re.compile(r'^Temperature *3\s+:\s+(?P<temperature3_celsius>\d+\.\d+) C$')

        # Fan Speed 1     :   10016.0000 RPM
        p11= re.compile(r'^Fan\s+Speed\s+1\s+:\s+(?P<fan_speed_1_rpm>\d+\.\d+) RPM$')

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
        p1 = re.compile(r'^(?P<power_supply>.+)\:$')

        # Input Voltage   :     231.0000 V
        p2 = re.compile(r'^Input\s+Voltage\s+:\s+(?P<input_voltage_volt>\d+\.\d+) V$')

        # Output Voltage  :      11.9490 V
        p3 = re.compile(r'^Output\s+Voltage\s+:\s+(?P<output_voltage_volt>\d+\.\d+) V$')

        # Input Power     :     165.0000 W
        p4 = re.compile(r'^Input\s+Power\s+:\s+(?P<input_power_watt>\d+\.\d+) W$')

        # Output Power    :     150.0000 W
        p5 = re.compile(r'^Output\s+(Power|power)\s+:\s+(?P<output_power_watt>\d+\.\d+) W$')

        # Input Current   :       0.7180 A
        p6 = re.compile(r'^Input\s+Current\s+:\s+(?P<input_current_amp>\d+\.\d+) A$')

        # Output Current  :      12.4840 A
        p7 = re.compile(r'^Output\s+Current\s+:\s+(?P<output_current_amp>\d+\.\d+) A$')

        # Temperature 1   :      30.7500 C
        p8 = re.compile(r'^Temperature *1\s+:\s+(?P<temperature1_celsius>\d+\.\d+) C$')

        # Temperature 2   :      33.0000 C
        p9 = re.compile(r'^Temperature *2\s+:\s+(?P<temperature2_celsius>\d+\.\d+) C$')

        # Temperature 3   :      33.5000 C
        p10 = re.compile(r'^Temperature *3\s+:\s+(?P<temperature3_celsius>\d+\.\d+) C$')

        # Fan Speed 1     :   10016.0000 RPM
        p11= re.compile(r'^Fan\s+Speed\s+1\s+:\s+(?P<fan_speed_1_rpm>\d+\.\d+) RPM$')

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

# ======================================================================================
#  Schema for
#  * show platform software fed active punt entries
#  * show platform software fed {switch} active punt entries
#  * show platform software fed {switch} active punt entries | include {label}
#  * show platform software fed active punt entries | include {label}
# =======================================================================================
class ShowPlatformSoftwareFedSwitchActivePuntEntriesSchema(MetaParser):
    """Schema for 'show platform software fed active punt entries'
                    'show platform software fed {switch} active punt entries'
                    'show platform software fed {switch} active punt entries | include {label}'
                    'show platform software fed active punt entries | include {label}'
    """
    schema = {
        'entries_name': {
            Any(): {
                'source': str,
                'pri': int,
                'tc': int,
                'policy': str,
                'cir_sw': int,
                'cir_hw': int,
                'pkts_a': int,
                'bytes_a': int,
                'pkts_d': int,
                'bytes_d': int,
            },
        }
    }

# =======================================================================================
#  Parser for
#  * 'show platform software fed active punt entries'
#  * 'show platform software fed {switch} active punt entries'
#  * 'show platform software fed {switch} active punt entries | include {label}'
#  * 'show platform software fed active punt entries | include {label}'
# =======================================================================================

class ShowPlatformSoftwareFedSwitchActivePuntEntries(ShowPlatformSoftwareFedSwitchActivePuntEntriesSchema):
    """
    Parser for :
        * show platform software fed active punt entries
        * show platform software fed {switch} active punt entries
        * show platform software fed {switch} active punt entries | include {label}
        * show platform software fed active punt entries | include {label}
    """
    cli_command = ['show platform software fed {switch} active punt entries | include {label}',\
                    'show platform software fed {switch} active punt entries',\
                    'show platform software fed active punt entries | include {label}',\
                    'show platform software fed active punt entries']

    def cli(self, label=None, switch=None, output=None):
        if output is None:
            if switch:
                if label:
                    cmd = self.cli_command[0].format(switch=switch, label=label)
                else:
                    cmd = self.cli_command[1].format(switch=switch)
            else:
                if label:
                    cmd= self.cli_command[2].format(label=label)
                else:
                    cmd= self.cli_command[3]
            output = self.device.execute(cmd)

        # initial return dictionary
        ret_dict ={}

        #Punject Punt Entries
        p1 = re.compile(r'^Punject Punt Entries$')

        # MIRROR   ARP   4    4    system-cpp-police-arp 1000     965      0           0         0           0
        p2 = re.compile(r'^(?P<source>\w*)\s+(?P<name>((\w+\s)+\w*\S\w*\S*)|(\w*(\S\w*\S){1,}))\s+'
                        r'(?P<pri>\d+)\s+(?P<tc>\d+)\s+(?P<policy>(\w+(-\w+)*))\s+(?P<cir_sw>\d+)\s+'
                        r'(?P<cir_hw>\d+)\s+(?P<pkts_a>\d+)\s+(?P<bytes_a>\d+)\s+(?P<pkts_d>\d+)\s+(?P<bytes_d>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            # Punject Punt Entries
            m = p1.match(line)
            if m:
                ret_dict.setdefault('entries_name', {})
                continue

            # MIRROR   ARP   4    4    system-cpp-police-arp 1000     965      0           0         0           0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                entries_name = group['name']
                sub_dict = ret_dict.setdefault('entries_name', {}).setdefault(entries_name, {})
                sub_dict.update({
                    'source': group['source'],
                    'pri': int(group['pri']),
                    'tc': int(group['tc']),
                    'pri': int(group['pri']),
                    'policy': group['policy'],
                    'cir_sw': int(group['cir_sw']),
                    'cir_hw': int(group['cir_hw']),
                    'pkts_a': int(group['pkts_a']),
                    'bytes_a': int(group['bytes_a']),
                    'pkts_d': int(group['pkts_d']),
                    'bytes_d': int(group['bytes_d'])
                })
                continue

        return ret_dict

# ==============================================================================
# Schema for 'show platform software fed {switch} active ip route vrf {vrf_name}'
# ==============================================================================

class ShowPlatformSoftwareFedActiveIpRouteVrfSchema(MetaParser):
    """Schema for show platform software fed {switch} active ip route vrf {vrf_name}"""
    schema = {
        'object_id':{
             Any(): {
                Optional('ipv4_address'): str,
                Optional('mask_length'): int,
                Optional('parent_type'): str,
                Optional('parent_object_id'): str,
            }
        },
        'number_entries': int,
    }

# ==============================================================================
# Parser for 'show platform software fed {switch} active ip route vrf {vrf_name}'
# ==============================================================================

class ShowPlatformSoftwareFedActiveIpRouteVrf(ShowPlatformSoftwareFedActiveIpRouteVrfSchema):
    """Parser for show platform software fed {switch} active ip route vrf {vrf_name}"""

    cli_command = 'show platform software fed {switch} active ip route vrf {vrf_name}'
    def cli(self, switch='', vrf_name='', output=None):
        if output is None:
            output = self.device.execute(self.cli_command[0].format(switch=switch, vrf_name=vrf_name))
        else:
            output = output

        # initial return dictionary
        ret_dict = {}

        # Number of npi_ipv4route entries = 19
        p0 = re.compile(r'^Number of npi_ipv4route entries\s+=\s+(?P<number_entries>\d*)$')

        # 0x5b60bb7077c8      40.1.1.3            32                  PUSH_COUNTER        0x169
        p1 = re.compile(r'^(?P<object_id>0x\w+)(?:\s*)'
                        r'(?P<ipv4_address>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(?:\s*)'
                        r'(?P<mask_length>\d*)(?:\s*)(?P<parent_type>\w*)(?:\s*)(?P<parent_object_id>0x\w*)$')

        for line in output.splitlines():
            line = line.strip()

            # Number of npi_ipv4route entries = 19
            m = p0.match(line)
            if m:
                group = m.groupdict()
                number_entries = group['number_entries']
                ret_dict.setdefault('number_entries', int(number_entries))
                continue

            # 0x5b60bb7077c8      40.1.1.3            32                  PUSH_COUNTER        0x169
            m = p1.match(line)
            if m:
                group = m.groupdict()
                object_id = group['object_id']
                sub_dict = ret_dict.setdefault('object_id', {}).setdefault(object_id, {})

                ipv4_address = group['ipv4_address']
                sub_dict['ipv4_address'] = str(ipv4_address)

                mask_length = group['mask_length']
                sub_dict['mask_length'] = int(mask_length)

                parent_type = group['parent_type']
                sub_dict['parent_type'] = str(parent_type)

                parent_object_id = group['parent_object_id']
                sub_dict['parent_object_id'] = str(parent_object_id)
                continue

        return ret_dict


class ShowPlatformHardwareFedSwitchQosQueueStatsInterfaceSchema(MetaParser):
    """Schema for show platform hardware fed {switch} {switch_var} qos queue stats interface {interface}"""

    schema = {
        'interface': {
            Any(): {
                'voq_id': {
                    Any(): {
                        'packets': {
                            'enqueued': int,
                            'dropped': int,
                            'total': int
                        },
                        'bytes': {
                            'enqueued': int,
                            'dropped': int,
                            'total': int
                        },
                        'slice': {
                            Any(): {
                                'sms_bytes': int,
                                'hbm_blocks': int,
                                'hbm_bytes': int
                            }
                        }
                    }
                }
            }
        }
    }


class ShowPlatformHardwareFedSwitchQosQueueStatsInterface(ShowPlatformHardwareFedSwitchQosQueueStatsInterfaceSchema):
    """Parser for show platform hardware fed {switch} {switch_var} qos queue stats interface {interface}"""

    cli_command = ['show platform hardware fed active qos queue stats interface {interface}',
        'show platform hardware fed switch {switch_num} qos queue stats interface {interface}']

    def cli(self, interface, switch_num=None, output=None):
        if output is None:
            if switch_num:
                cmd = self.cli_command[1].format(switch_num=switch_num, interface=interface)
            else:
                cmd = self.cli_command[0].format(interface=interface)

            output = self.device.execute(cmd)

        # VOQ Stats For : HundredGigE1/0/5 [ 0x544 ]
        # VOQ Stats For : HundredGigE2/0/2.1 [ 0x550 ]
        p1 = re.compile(r'^VOQ Stats For : (?P<interface>[\w\/\.]+)\s+.*$')

        # 0      | Enqueued |                        1194566957 |                       78841419162 |
        # | Dropped  |                                 0 |                                 0 |
        # | Total    |                        1194566957 |                       78841419162 |
        # |----------|-----------------------------------------------------------------------|
        p2 = re.compile(r'^(?P<voq_id>\d+)?\s*\|\s+(?P<header>\w+)\s+\|\s+(?P<packets>\d+)\s+\|\s+(?P<bytes>\d+)\s+\|$')

        # |   Slice  |         0 |         1 |         2 |         3 |         4 |         5 |
        p3 = re.compile(r'^\|\s+Slice\s+\|\s+(?P<slice0>\d+)\s\|\s+(?P<slice1>\d+)\s\|\s+(?P<slice2>\d+)\s\|'
                    r'\s+(?P<slice3>\d+)\s\|\s+(?P<slice4>\d+)\s\|\s+(?P<slice5>\d+)\s\|$')

        # |SMS Bytes |         0 |         0 |         0 |         0 |         0 |         0 |
        p4 = re.compile(r'^\|\s*(?P<slice_type>SMS Bytes|HBM Blocks|HBM Bytes)\s*\|\s+(?P<slice0>\d+)\s\|\s+(?P<slice1>\d+)\s\|'
            r'\s+(?P<slice2>\d+)\s\|\s+(?P<slice3>\d+)\s\|\s+(?P<slice4>\d+)\s\|\s+(?P<slice5>\d+)\s\|$')

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # VOQ Stats For : HundredGigE1/0/5 [ 0x544 ]
            m = p1.match(line)
            if m:
                int_dict = ret_dict.setdefault('interface', {}).setdefault(Common.convert_intf_name(m.groupdict()['interface']), {})
                continue

            # 0      | Enqueued |                        1194566957 |                       78841419162 |
            # | Dropped  |                                 0 |                                 0 |
            # | Total    |                        1194566957 |                       78841419162 |
            # |----------|-----------------------------------------------------------------------|
            m = p2.match(line)
            if m:
                res_dict = m.groupdict()
                if res_dict['voq_id']:
                    voq_dict = int_dict.setdefault('voq_id', {}).setdefault(res_dict['voq_id'], {})

                pkts_dict = voq_dict.setdefault('packets', {})
                bytes_dict = voq_dict.setdefault('bytes', {})
                pkts_dict.setdefault(res_dict['header'].lower(), int(res_dict['packets']))
                bytes_dict.setdefault(res_dict['header'].lower(), int(res_dict['bytes']))
                continue

            # |   Slice  |         0 |         1 |         2 |         3 |         4 |         5 |
            m = p3.match(line)
            if m:
                slice_dict = voq_dict.setdefault('slice', {})
                slice_dict0 = slice_dict.setdefault(m.groupdict()['slice0'], {})
                slice_dict1 = slice_dict.setdefault(m.groupdict()['slice1'], {})
                slice_dict2 = slice_dict.setdefault(m.groupdict()['slice2'], {})
                slice_dict3 = slice_dict.setdefault(m.groupdict()['slice3'], {})
                slice_dict4 = slice_dict.setdefault(m.groupdict()['slice4'], {})
                slice_dict5 = slice_dict.setdefault(m.groupdict()['slice5'], {})
                continue

            # |SMS Bytes |         0 |         0 |         0 |         0 |         0 |         0 |
            m = p4.match(line)
            if m:
                grp_output = m.groupdict()
                slice_type = grp_output['slice_type'].replace(' ', '_').lower()
                slice_dict0.setdefault(slice_type, int(grp_output['slice0']))
                slice_dict1.setdefault(slice_type, int(grp_output['slice1']))
                slice_dict2.setdefault(slice_type, int(grp_output['slice2']))
                slice_dict3.setdefault(slice_type, int(grp_output['slice3']))
                slice_dict4.setdefault(slice_type, int(grp_output['slice4']))
                slice_dict5.setdefault(slice_type, int(grp_output['slice5']))
                continue

        return ret_dict


class ShowPlatformHardwareFedSwitchQosQueueStatsInterfaceClear(ShowPlatformHardwareFedSwitchQosQueueStatsInterface):
    """Parser for show platform hardware fed switch {switch} qos queue stats interface {interface} clear"""

    cli_command = ['show platform hardware fed active qos queue stats interface {interface} clear',
            'show platform hardware fed switch {switch_num} qos queue stats interface {interface} clear']

    def cli(self, interface, switch_num=None, output=None):

        return super().cli(interface=interface, switch_num=switch_num, output=output)


class ShowPlatformTcamUtilizationSchema(MetaParser):
    """Schema for
        show platform hardware fed {switch} {mode} fwd-asic resource tcam utilization
        show platform hardware fed active fwd-asic resource tcam utilization
    """
    schema = {
        Optional('resource'): {
            Any(): {
                'slice': {
                    Any(): {
                        'used': int,
                        'free': int
                    }
                }
            }
        },
        Optional('asic'): {
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
    """Parser for
        show platform hardware fed {switch} {mode} fwd-asic resource tcam utilization
        show platform hardware fed active fwd-asic resource tcam utilization
    """

    cli_command = ['show platform hardware fed {switch} {mode} fwd-asic resource tcam utilization',
                   'show platform hardware fed active fwd-asic resource tcam utilization',
                   'show platform hardware fed switch {mode} fwd-asic resource tcam utilization',
                   'show platform hardware fed {switch} {mode} fwd-asic resource tcam utilization {asic}',
                   'show platform hardware fed active fwd-asic resource tcam utilization {asic}',
                   'show platform hardware fed switch {mode} fwd-asic resource tcam utilization {asic}']

    def cli(self, switch=None, mode=None, output=None, asic=None):
        if output is None:
            if asic:
                if switch and mode:
                    cmd = self.cli_command[3].format(switch=switch, mode=mode, asic=asic)
                elif mode:
                    cmd = self.cli_command[5].format(mode=mode, asic=asic)
                else:
                    cmd = self.cli_command[4].format(asic=asic)
            else:
                if switch and mode:
                    cmd = self.cli_command[0].format(switch=switch, mode=mode)
                elif mode:
                    cmd = self.cli_command[2].format(mode=mode)
                else:
                    cmd = self.cli_command[1]
            output = self.device.execute(cmd)

        # initial return dictionary
        ret_dict = {}

        #                                        Slice0       Slice1       Slice2       Slice3       Slice4       Slice5
        #     Resource                        Used  Free   Used  Free   Used  Free   Used  Free   Used  Free   Used  Free
        # IPv4 LPTS TCAM entries                   35  8634     35  8634     35  8634     35  8634     35  8628     35  8634
        # IPv6 LPTS TCAM entries                   30  4538     30  4538     30  4538     30  4538     30  4532     30  4538
        p1 = re.compile(r'(?P<resource>.+)\s+(?P<slice0_used>\d+)\s+(?P<slice0_free>\d+)\s+(?P<slice1_used>\d+)\s+'
                        r'(?P<slice1_free>\d+)\s+(?P<slice2_used>\d+)\s+(?P<slice2_free>\d+)\s+(?P<slice3_used>\d+)\s+'
                        r'(?P<slice3_free>\d+)\s+(?P<slice4_used>\d+)\s+(?P<slice4_free>\d+)\s+(?P<slice5_used>\d+)\s+(?P<slice5_free>\d+)$')

        # CAM Utilization for ASIC  [0]
        p2 = re.compile(r'CAM +Utilization +for +ASIC  +\[+(?P<asic>(\d+))\]$')

        # CTS Cell Matrix/VPN
        # Label                  TCAM         O         512        1    0.20%        0        0        0        1
        # CTS Cell Matrix/VPN
        # Label                  TCAM         O        1024        1    0.10%        0        0        0        1
        # Mac Address Table      EM           I       16384       45    0.27%        0        0        0       45
        p3 = re.compile(r'(?P<table>.*(\S+)) +(?P<subtype>\S+) +(?P<dir>\S+) +(?P<max>\d+) +(?P<used>\d+) +(?P<used_percent>\S+\%) +(?P<v4>\d+) +(?P<v6>\d+) +(?P<mpls>\d+) +(?P<other>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            #                                        Slice0       Slice1       Slice2       Slice3       Slice4       Slice5
            #     Resource                        Used  Free   Used  Free   Used  Free   Used  Free   Used  Free   Used  Free
            # IPv4 LPTS TCAM entries                   35  8634     35  8634     35  8634     35  8634     35  8628     35  8634
            # IPv6 LPTS TCAM entries                   30  4538     30  4538     30  4538     30  4538     30  4532     30  4538
            m = p1.match(line)
            if m:
                group = m.groupdict()
                resource_name = group['resource'].strip().lower().replace(' ', '_')
                resource_dict = ret_dict.setdefault('resource', {}).setdefault(resource_name, {})
                slice_dict = resource_dict.setdefault('slice', {}).setdefault(0, {})
                slice_dict['used'] = int(group['slice0_used'])
                slice_dict['free'] = int(group['slice0_free'])
                slice_dict = resource_dict.setdefault('slice').setdefault(1, {})
                slice_dict['used'] = int(group['slice1_used'])
                slice_dict['free'] = int(group['slice1_free'])
                slice_dict = resource_dict.setdefault('slice').setdefault(2, {})
                slice_dict['used'] = int(group['slice2_used'])
                slice_dict['free'] = int(group['slice2_free'])
                slice_dict = resource_dict.setdefault('slice').setdefault(3, {})
                slice_dict['used'] = int(group['slice3_used'])
                slice_dict['free'] = int(group['slice3_free'])
                slice_dict = resource_dict.setdefault('slice').setdefault(4, {})
                slice_dict['used'] = int(group['slice4_used'])
                slice_dict['free'] = int(group['slice4_free'])
                slice_dict = resource_dict.setdefault('slice').setdefault(5, {})
                slice_dict['used'] = int(group['slice5_used'])
                slice_dict['free'] = int(group['slice5_free'])
                continue

            # CAM Utilization for ASIC  [0]
            m = p2.match(line)
            if m:
                group = m.groupdict()
                asic = group['asic']
                asic_dict = ret_dict.setdefault('asic', {}).setdefault(asic, {})
                continue

            # CTS Cell Matrix/VPN
            # Label                  TCAM         O         512        1    0.20%        0        0        0        1
            # CTS Cell Matrix/VPN
            # Label                  TCAM         O        1024        1    0.10%        0        0        0        1
            # Mac Address Table      EM           I       16384       45    0.27%        0        0        0       45
            m = p3.match(line)
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


# ======================================================================================================#
#  Schema for 'show platform software fed switch active punt packet-capture display-filter <key> brief' #
# ======================================================================================================#
class ShowPlatformSoftwareFedSwitchActivePuntPacketCaptureDisplayFilterKeyBriefSchema(MetaParser):

    schema = {
        'total_captured_so_far': int,
        'punt_packet_number': {
            'timestamp': str,
            Any(): {
                'interface': {
                    'phy': {
                        'val': str,
                        'if_id': str
                    },
                    'pal': {
                        'val': str,
                        'if_id': str
                    }
                },
                'misc_info': {
                    'cause': str,
                    'cause_number': int
                },
                Optional('ce_hdr'): {
                    'src_mac': str,
                    'dest_mac': str,
                    'ethertype': str
                },
                'ether_hdr': {
                    'src_mac': str,
                    'dest_mac': str,
                    'vlan': int,
                    'ethertype': str
                },
                'arp_hdr': {
                    'opcode': {
                        'val': str,
                        Optional('opcode_number'): int
                    },
                    'src_mac': str,
                    'dest_mac': str,
                    'src_ip': str,
                    'dest_ip': str
                }
            }
        }
    }

# =====================================================================================================#
#  Parser for 'show platform software fed switch active punt packet-capture display-filter <key> brief #
# =====================================================================================================#
class ShowPlatformSoftwareFedSwitchActivePuntPacketCaptureDisplayFilterKeyBrief(ShowPlatformSoftwareFedSwitchActivePuntPacketCaptureDisplayFilterKeyBriefSchema):

    cli_command = [
        "show platform software fed {switch} {switch_num} punt packet-capture display-filter {key} brief",
        "show platform software fed {switch_num} punt packet-capture display-filter {key} brief"
        ]

    def cli(self, switch_num, key, output=None ,switch=""):
        if output is None:
            if switch :
                out = self.device.execute(self.cli_command[0].format(switch = switch,switch_num = switch_num, key = key))
            else :
                out = self.device.execute(self.cli_command[1].format(key = key , switch_num = switch_num))
        else:
            out = output

        res_dict = {}


        # Total captured so far :  4096 packet(s)

        p0 = re.compile(r"Total captured so far :\s+(?P<total_captured_so_far>\d+)\s+packet")

        # Punt Packet Number: 3659

        p1 = re.compile(r".+Punt Packet Number\s*:\s*(?P<punt_packet_number>[\d]+)\s*\,\s*Timestamp\s*\:\s*(?P<timestamp>[\d\/\s\:\.]+).+")

        # interface : phy: Port11lVlan101 [if-id: 0x50000000b0065], pal: Vlan101 [if-id: 0x000005ce]

        p2 = re.compile(r"interface\s*:\s*phy\s*:\s*(?P<phy_val>[\w]+)\s+\[[\w\-\:]+\s*(?P<phy_if_id>[\w]+)\]\s*\,\s*pal\s*\:\s*(?P<pal_val>[\w]+)\s*\[[\w\-\:]+\s*(?P<pal_if_id>[\w]+)\]")

        # misc info : cause: 7 [ARP request or response], sub-cause: 1, linktype: IP [1]

        p3 = re.compile(r"misc info\s*\:\s*cause\s*\:\s*(?P<cause_number>[\d]+)\s*\[(?P<cause>[\w\s]+)\]\s*\,")

        # CE hdr : dest mac: 4e41.5000.0010, src mac: 4e41.5000.0111, ethertype: 0x7102

        p4 = re.compile(r"CE\s*hdr\s*\:\s*dest mac\s*\:\s*(?P<dest_mac>[\w\.]+)\s*\,\s*src mac\s*\:\s*(?P<src_mac>[\w\.]+)\s*\,\s*ethertype\s*\:\s*(?P<ethertype>[\w]+)")

        # ether hdr : dest mac: ffff.ffff.ffff, src mac: 00a7.428a.7fbf

        p5 = re.compile(r"ether\s*hdr\s*\:\s*dest mac\s*\:\s*(?P<dest_mac>[\w\.]+)\s*\,\s*src mac\s*\:\s*(?P<src_mac>[\w\.]+)")

        # ether hdr : vlan: 101, ethertype: 0x8100

        p6 = re.compile(r"ether\s*hdr\s*\:\s*vlan\s*\:\s*(?P<vlan>[\d]+)\s*\,\s*ethertype\s*\:\s*(?P<ethertype>[\w]+)")

        # arp hdr : opcode: 2 (ARP Reply), src mac: 00a7.428a.7fbf dest mac: ffff.ffff.ffff

        p7 = re.compile(r"arp\s*hdr\s*\:\s*opcode\s*\:\s*(?P<opcode>[\w\s\(\)]+)\s*\,\s*src mac\s*\:\s*(?P<src_mac>[\w\.]+)\s*dest mac\s*\:\s*(?P<dest_mac>[\w\.]+)")

        # arp   hdr : src ip: 14.0.1.2, dest ip: 14.0.1.2

        p8 = re.compile(r"arp\s*hdr\s*\:\s*src ip\s*\:\s*(?P<src_ip>[\d\.]+)\s*\,\s*dest ip\s*\:\s*(?P<dest_ip>[\d\.]+)")

        for line in out.splitlines():
            line = line.strip()

            # Total captured so far :  4096 packet(s)

            m = p0.match(line)

            if m:
                group = m.groupdict()
                res_dict.setdefault('total_captured_so_far' , int(group['total_captured_so_far']))
                continue

            # Punt Packet Number: 3659

            m = p1.match(line)

            if m:
                group = m.groupdict()
                punt_packet = res_dict.setdefault('punt_packet_number', {})
                punt_packet.setdefault('timestamp',group['timestamp'])
                punt_packet_details = punt_packet.setdefault(group['punt_packet_number'], {})
                continue

            # interface : phy: Port11lVlan101 [if-id: 0x50000000b0065], pal: Vlan101 [if-id: 0x000005ce]

            m = p2.match(line)

            if m:
                group = m.groupdict()
                phy = punt_packet_details.setdefault('interface', {}).setdefault('phy',{})
                pal = punt_packet_details.setdefault('interface', {}).setdefault('pal',{})
                phy['val'] = group['phy_val']
                phy['if_id'] = group['phy_if_id']
                pal['val'] = group['phy_val']
                pal['if_id'] = group['pal_if_id']
                continue

            # misc info : cause: 7 [ARP request or response], sub-cause: 1, linktype: IP [1]

            m = p3.match(line)

            if m:
                group = m.groupdict()
                misc = punt_packet_details.setdefault('misc_info', {})
                misc['cause'] = group['cause']
                misc['cause_number'] = int(group['cause_number'])
                continue

            # CE hdr : dest mac: 4e41.5000.0010, src mac: 4e41.5000.0111, ethertype: 0x7102

            m = p4.match(line)

            if m:
                group = m.groupdict()
                ce_hdr = punt_packet_details.setdefault('ce_hdr', {})
                ce_hdr['src_mac'] = group['src_mac']
                ce_hdr['dest_mac'] = group['dest_mac']
                ce_hdr['ethertype'] = group['ethertype']
                continue

            # ether hdr : dest mac: ffff.ffff.ffff, src mac: 00a7.428a.7fbf

            m = p5.match(line)

            if m:
                group = m.groupdict()
                ether_hdr = punt_packet_details.setdefault('ether_hdr', {})
                ether_hdr['src_mac'] = group['src_mac']
                ether_hdr['dest_mac'] = group['dest_mac']
                continue

            # ether hdr : vlan: 101, ethertype: 0x8100

            m = p6.match(line)

            if m:
                group = m.groupdict()
                ether_hdr = punt_packet_details.setdefault('ether_hdr', {})
                ether_hdr['vlan'] = int(group['vlan'])
                ether_hdr['ethertype'] = group['ethertype']
                continue

            # arp hdr : opcode: 2 (ARP Reply), src mac: 00a7.428a.7fbf dest mac: ffff.ffff.ffff

            m = p7.match(line)

            if m:
                group = m.groupdict()
                arp_hdr = punt_packet_details.setdefault('arp_hdr', {})
                opcode = arp_hdr.setdefault('opcode', {})
                opcode['val'] = group['opcode']
                match = re.match(r'^(\d+)', group['opcode'])
                if match:
                    opcode['opcode_number'] = int(match.group(1))
                arp_hdr['src_mac'] = group['src_mac']
                arp_hdr['dest_mac'] = group['dest_mac']
                continue

            # arp   hdr : src ip: 14.0.1.2, dest ip: 14.0.1.2

            m = p8.match(line)

            if m:
                group = m.groupdict()
                arp_hdr['src_ip'] = group['src_ip']
                arp_hdr['dest_ip'] = group['dest_ip']
                continue

        return res_dict

# =========================================
# Schema for 'show platform software fed switch active punt packet-capture status'
# =========================================
class ShowPlatformSoftwareFedSwitchActivePuntPacketcaptureStatusSchema(MetaParser):

    """
    Schema for
        'show platform software fed {switch} {switch_num} punt packet-capture status',
        'show platform software fed {switch_num} punt packet-capture status'
    """

    schema = {
        'punt_packet_capturing': str,
        'buffer_wrapping': str,
        'total_captured_so_far': int,
        'capture_capacity': int,
        'max_meta_header_size_bytes': int,
        'max_packet_data_size_bytes': int
    }
# =========================================
# Parser for 'show platform software fed switch active punt packet-capture status'
# =========================================
class ShowPlatformSoftwareFedSwitchActivePuntPacketcaptureStatus(ShowPlatformSoftwareFedSwitchActivePuntPacketcaptureStatusSchema):
    """

    Parser for
        'show platform software fed {switch} {switch_num} punt packet-capture status',
        'show platform software fed {switch_num} punt packet-capture status'
    """

    cli_command = ['show platform software fed {switch} {switch_num} punt packet-capture status',
                   'show platform software fed {switch_num} punt packet-capture status']

    def cli(self, switch_num, switch='', output=None):
        if output is None:
            if switch:
                output = self.device.execute(self.cli_command[0].format(switch=switch, switch_num=switch_num))
            else:
                output = self.device.execute(self.cli_command[1].format(switch_num=switch_num))

        # Init vars
        ret_dict = {}

        # punt packet capturing: disabled. buffer wrapping: disabled
        p1 = re.compile(r'^punt\s+packet\s+capturing:\s+(?P<punt_packet_capturing>\w+)\.\s+buffer\s+wrapping:\s+(?P<buffer_wrapping>\w+)$')

        # Total captured so far :    13 packet(s)
        p2 = re.compile(r'^total\s+captured\s+so\s+far\s+:\s+(?P<total_captured_so_far>(\d+)\s)+packet\(s\)$')

        # Capture capacity      :  4096 packet(s)
        p3 = re.compile(r'^capture\s+capacity\s+:\s+(?P<capture_capacity>(\d+)\s)+packet\(s\)$')

        # Max. Meta header size :    88 byte(s)
        p4 = re.compile(r'^max.\s+meta\s+header\s+size\s+:\s+(?P<max_meta_header_size_bytes>(\d+))\s+byte\(s\)$')

        # Max. Packet data size :   128 byte(s)
        p5 = re.compile(r'^max.\s+packet\s+data\s+size\s+:\s+(?P<max_packet_data_size_bytes>(\d+))\s+byte\(s\)$')

        for line in output.splitlines():
            line = line.strip()

            # punt packet capturing: disabled. buffer wrapping: disabled
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['punt_packet_capturing'] = group['punt_packet_capturing']
                ret_dict['buffer_wrapping'] = group['buffer_wrapping']
                continue

            # Total captured so far :    13 packet(s)
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('total_captured_so_far', int(group['total_captured_so_far']))
                continue

            # Capture capacity      :  4096 packet(s)
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('capture_capacity', int(group['capture_capacity']))
                continue

            # Max. Meta header size :    88 byte(s)
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('max_meta_header_size_bytes', int(group['max_meta_header_size_bytes']))
                continue

            # Max. Packet data size :   128 byte(s)
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('max_packet_data_size_bytes', int(group['max_packet_data_size_bytes']))
                continue

        return ret_dict

# ======================================================================================================#
#  Schema for 'show platform software fed switch active punt packet-capture display-filter icmp brief' #
# ======================================================================================================#
class ShowPlatformSoftwareFedSwitchActivePuntPacketCaptureDisplayFilterIcmpBriefSchema(MetaParser):

    """
    Schema for
        'show platform software fed {switch} {switch_num} punt packet-capture display-filter icmp brief'
        'show platform software fed {switch_num} punt packet-capture display-filter icmp brief'
    """

    schema = {
        'punt_packet_number': {
            'timestamp': str,
            Any(): {
                'interface': {
                    'phy': {
                        'val': str,
                        'if_id': str
                    },
                    'pal': {
                        'val': str,
                        'if_id': str
                    }
                },
                'misc_info': {
                    'cause': str,
                    'cause_number': str,
                    'link_type': str
                },
                Optional('ce_hdr'): {
                    'src_mac': str,
                    'dest_mac': str,
                    'ethertype': str
                },
                'meta_hdr':{
                    'nxt_hdr': str,
                    'fwd_hdr': str,
                    'ssp': str,
                    'dsp': str,
                    'slp': str,
                    'dlp':str
                },
                'ether_hdr': {
                    'src_mac': str,
                    'dest_mac': str,
                    'vlan': int,
                    'ether_type': str
                },
                'ipv4_hdr': {
                    'src_ip': str,
                    'dest_ip': str,
                    'packet_len': int,
                    'ttl': int,
                    'protocol': str
                },
                'icmp_hdr': {
                    'icmp_type': int,
                    'code': int
                }
			}
		}
	}


# =====================================================================================================#
#  Parser for 'show platform software fed switch active punt packet-capture display-filter icmp brief #
# =====================================================================================================#
class ShowPlatformSoftwareFedSwitchActivePuntPacketCaptureDisplayFilterIcmpBrief(ShowPlatformSoftwareFedSwitchActivePuntPacketCaptureDisplayFilterIcmpBriefSchema):
    """

    Parser for
        'show platform software fed {switch} {switch_num} punt packet-capture display-filter icmp brief'
        'show platform software fed {switch_num} punt packet-capture display-filter icmp brief'
    """
    cli_command = [
        "show platform software fed {switch} {switch_num} punt packet-capture display-filter icmp brief",
        "show platform software fed {switch_num} punt packet-capture display-filter icmp brief"
        ]

    def cli(self, switch_num, output=None ,switch=""):
        if output is None:
            if switch :
                out = self.device.execute(self.cli_command[0].format(switch = switch,switch_num = switch_num))
            else :
                out = self.device.execute(self.cli_command[1].format(switch_num = switch_num))
        else:
            out = output

        res_dict = {}

        # ------ Punt Packet Number: 41, Timestamp: 2024/06/25 16:07:00.656 ------
        p1 = re.compile(r'^------\s+Punt\s+Packet\sNumber:\s+(?P<punt_packet_number>(\d+,))\s+Timestamp:\s+(?P<timestamp>(\d+\/\d+\/\d+\s+\d+:\d+:\d+.\d+\s+------))$')

        # interface : phy: Vlan100 [if-id: 0x00000624], pal: Vlan100 [if-id: 0x00000624]
        p2 = re.compile(r'^interface\s*:\s*phy\s*:\s*(?P<phy_val>[\w+]+)\s+\[[\w\-\:]+\s*(?P<phy_if_id>[\w+]+)\]\s*\,\s*pal\s*\:\s*(?P<pal_val>[\w+]+)\s*\[[\w\-\:]+\s*(?P<pal_if_id>(\w+\]))$')

        # misc info : cause: 55 [For-us control], sub-cause: 0 [CPP_PUNT_SUBCAUSE_TRANSPORT_NONE], linktype: IP [1]
        p3 = re.compile(r'^misc\s*info\s*\:\s*cause\s*\:\s*(?P<cause_number>(\d+)+)\s*\[(?P<cause>[\w+\-\s+\]]+)+,\s*sub-cause\s*:\s*(?P<sub_cause_num>(\d+)\s+\[(?P<sub_cause>(\w+\]))),\s+linktype\s*:\s*(?P<link_type>(\w+\s*\[(\d)\]))$')

        # CE    hdr : dest mac: 4e41.5000.0111, src mac: 4e41.5000.0111, ethertype: 0x7106
        p4 = re.compile(r'^CE\s*hdr\s*\:\s*dest mac\s*\:\s*(?P<dest_mac>[\w\.]+)\s*\,\s*src mac\s*\:\s*(?P<src_mac>[\w\.]+)\s*\,\s*ethertype\s*\:\s*(?P<ethertype>[\w]+)$')

        # meta  hdr : Nxt. Hdr: 0x1, Fwd. Hdr: 0x2, SSP: 0x119
        p5 = re.compile(r'^meta\s*hdr\s*:\s+Nxt.\s*Hdr:\s*(?P<nxt_hdr>(\w*)),\s*Fwd.\s*Hdr:\s*(?P<fwd_hdr>(\w*)),\s*SSP:\s*(?P<ssp>(\w*))$')

        # meta  hdr : DSP: 0xffff, SLP: 0x122, DLP: 0xef
        p6 = re.compile(r'^meta\s*hdr\s*:\s+DSP:\s*(?P<dsp>(\w*)),\s*SLP:\s*(?P<slp>(\w*)),\s*DLP:\s*(?P<dlp>(\w*))$')

        # ether hdr : dest mac: 3c57.3104.7045, src mac: a0b4.39cd.70ff
        p7 = re.compile(r'^ether\s*hdr\s*\:\s*dest mac\s*\:\s*(?P<dest_mac>[\w\.]+)\s*\,\s*src mac\s*\:\s*(?P<src_mac>[\w\.]+)$')

        # ether hdr : vlan: 100, ethertype: 0x8100
        p8 = re.compile(r'^ether\s*hdr\s*\:\s*vlan\s*\:\s*(?P<vlan>[\d]+)\s*\,\s*ethertype\s*\:\s*(?P<ether_type>[\w]+)$')

        # ipv4  hdr : dest ip: 100.10.1.1, src ip: 1.0.0.3
        p9 = re.compile(r'^ipv4\s*hdr\s*:\s*dest\s*ip:\s*(?P<dest_ip>(\d*\.\d*\.\d*\.\d*)),\s*src\s*ip:\s*(?P<src_ip>(\d*\.\d*\.\d*\.\d*))$')

        # ipv4  hdr : packet len: 100, ttl: 254, protocol: 1 (ICMP)
        p10 = re.compile(r'^ipv4\s*hdr\s*:\s*packet\s*len:\s*(?P<packet_len>(\d*)),\s*ttl:\s*(?P<ttl>(\d*)),\s*protocol:\s*(?P<protocol>(\d*\s*\(\w*\)))$')

        # icmp  hdr : icmp type: 8, code: 0
        p11 = re.compile(r'^icmp\s*hdr\s*:\s*icmp\s*type:\s*(?P<icmp_type>(\d*)),\s*code:\s*(?P<code>(\d*))$')

        for line in out.splitlines():
            line = line.strip()

            # Punt Packet Number: 41, Timestamp: 2024/06/25 16:07:00.656
            m = p1.match(line)
            if m:
                group = m.groupdict()
                punt_packet = res_dict.setdefault('punt_packet_number', {})
                punt_packet.setdefault('timestamp',group['timestamp'])
                punt_packet_details = punt_packet.setdefault(group['punt_packet_number'], {})
                continue

            # interface : phy: Vlan100 [if-id: 0x00000624], pal: Vlan100 [if-id: 0x00000624]
            m = p2.match(line)
            if m:
                group = m.groupdict()
                phy = punt_packet_details.setdefault('interface', {}).setdefault('phy',{})
                pal = punt_packet_details.setdefault('interface', {}).setdefault('pal',{})
                phy['val'] = group['phy_val']
                phy['if_id'] = group['phy_if_id']
                pal['val'] = group['phy_val']
                pal['if_id'] = group['pal_if_id']
                continue

            # misc info : cause: 55 [For-us control], sub-cause: 0 [CPP_PUNT_SUBCAUSE_TRANSPORT_NONE], linktype: IP [1]
            m = p3.match(line)
            if m:
                group = m.groupdict()
                misc_info = punt_packet_details.setdefault('misc_info', {})
                misc_info['cause'] = group['cause']
                misc_info['cause_number'] = group['cause_number']
                misc_info['link_type'] = group['link_type']
                continue

            # CE    hdr : dest mac: 4e41.5000.0111, src mac: 4e41.5000.0111, ethertype: 0x7106
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ce_hdr = punt_packet_details.setdefault('ce_hdr', {})
                ce_hdr['src_mac'] = group['src_mac']
                ce_hdr['dest_mac'] = group['dest_mac']
                ce_hdr['ethertype'] = group['ethertype']
                continue

            # meta  hdr : Nxt. Hdr: 0x1, Fwd. Hdr: 0x2, SSP: 0x119
            m = p5.match(line)
            if m:
                group = m.groupdict()
                meta_hdr = punt_packet_details.setdefault('meta_hdr', {})
                meta_hdr['nxt_hdr'] = group['nxt_hdr']
                meta_hdr['fwd_hdr'] = group['fwd_hdr']
                meta_hdr['ssp'] = group['ssp']
                continue

            # meta  hdr : DSP: 0xffff, SLP: 0x122, DLP: 0xef
            m = p6.match(line)
            if m:
                group = m.groupdict()
                meta_hdr = punt_packet_details.setdefault('meta_hdr', {})
                meta_hdr['dsp'] = group['dsp']
                meta_hdr['slp'] = group['slp']
                meta_hdr['dlp'] = group['dlp']
                continue

            # ether hdr : dest mac: 3c57.3104.7045, src mac: a0b4.39cd.70ff
            m = p7.match(line)
            if m:
                group = m.groupdict()
                ether_hdr = punt_packet_details.setdefault('ether_hdr', {})
                ether_hdr['src_mac'] = group['src_mac']
                ether_hdr['dest_mac'] = group['dest_mac']
                continue

            # ether hdr : vlan: 100, ethertype: 0x8100
            m = p8.match(line)
            if m:
                group = m.groupdict()
                ether_hdr = punt_packet_details.setdefault('ether_hdr', {})
                ether_hdr['vlan'] = int(group['vlan'])
                ether_hdr['ether_type'] = group['ether_type']
                continue

            # ipv4  hdr : dest ip: 100.10.1.1, src ip: 1.0.0.3
            m = p9.match(line)
            if m:
                group = m.groupdict()
                ipv4_hdr = punt_packet_details.setdefault('ipv4_hdr', {})
                ipv4_hdr['src_ip'] = group['src_ip']
                ipv4_hdr['dest_ip'] = group['dest_ip']
                continue

            # ipv4  hdr : packet len: 100, ttl: 254, protocol: 1 (ICMP)
            m = p10.match(line)
            if m:
                group = m.groupdict()
                ipv4_hdr = punt_packet_details.setdefault('ipv4_hdr', {})
                ipv4_hdr['packet_len'] = int(group['packet_len'])
                ipv4_hdr['ttl'] = int(group['ttl'])
                ipv4_hdr['protocol'] = group['protocol']
                continue

            # icmp  hdr : icmp type: 8, code: 0
            m = p11.match(line)
            if m:
                group = m.groupdict()
                icmp_hdr = punt_packet_details.setdefault('icmp_hdr', {})
                icmp_hdr['icmp_type'] = int(group['icmp_type'])
                icmp_hdr['code'] = int(group['code'])
                continue

        return res_dict

# =========================================
# Schema for 'show platform software fed switch {switch_num} acl usage | include {acl_name}'
# =========================================

class ShowPlatformSoftwareFedSwitchAclUsageIncludeAclSchema(MetaParser):
    """Schema for show platform software fed switch {switch_num} acl usage | include {acl_name}"""

    schema = {
        'feature_type': str,
        'acl_type': str,
        'dir': str,
        'name': str,
        'entries_used': int,
    }

# =====================================================
# Parser for 'show platform software fed switch {switch_num} acl usage | include {acl_name}'
# =====================================================
class ShowPlatformSoftwareFedSwitchAclUsageIncludeAcl(ShowPlatformSoftwareFedSwitchAclUsageIncludeAclSchema):
    """
    Parser for
        * 'show platform software fed switch {switch_num} acl usage'
        * 'show platform software fed switch {switch_num} acl usage | include {acl_name}'
    """

    cli_command = ['show plaform software fed switch {switch_num} acl usage', 'show plaform software fed switch {switch_num} acl usage | include {acl_name}']

    def cli(self, switch_num, output=None, acl_name = ''):
        if output is None:
            if acl_name:
                cmd = self.cli_command[1].format(switch_num = switch_num, acl_name = acl_name)
            else:
                cmd = self.cli_command[0].format(switch_num = switch_num)
            output = self.device.execute(cmd)

        ret_dict = {}

        # PACL          IPV4          Egress          racl_permit_egress          2
        p1 = re.compile(
            r"^(?P<feature_type>\w+)\s+(?P<acl_type>IPV[46])\s+(?P<dir>\w+)\s+(?P<name>\w+)\s+(?P<entries_used>\d+)$"
        )

        for line in output.splitlines():
            line = line.strip()

            # PACL          IPV4          Egress          racl_permit_egress          2
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['feature_type'] = group['feature_type']
                ret_dict['acl_type'] = group['acl_type']
                ret_dict['dir'] = group['dir']
                ret_dict['name'] = group['name']
                ret_dict['entries_used'] = int(group['entries_used'])
                continue

        return ret_dict


# ======================================================================================================#
#  Schema for 'show platform software fed switch active punt packet-capture display-filter icmpv6 brief' #
# ======================================================================================================#
class ShowPlatformSoftwareFedSwitchActivePuntPacketCapturedisplayFiltericmpv6BriefSchema(MetaParser):
    """
    Schema for
        'show platform software fed {switch} {switch_num} punt packet-capture display-filter icmpv6 brief'
        'show platform software fed {switch_num} punt packet-capture display-filter icmpv6 brief'
    """

    schema = {
        'punt_packet_number': {
            Any(): {
                'timestamp': str,
                'interface': {
                    'phy': {
                        'val': str,
                        'if_id': str
                    },
                    'pal': {
                        'val': str,
                        'if_id': str
                    }
                },
                'misc_info': {
                    'cause_number': int,
                    'cause_desc': str,
                    'subcause_number': int,
                    'subcause_desc': str,
                    'link_type': str
                },
                Optional('ce_hdr'): {
                    'src_mac': str,
                    'dest_mac': str,
                    'ethertype': str
                },
                'meta_hdr':{
                    'nxt_hdr': str,
                    'fwd_hdr': int,
                    'ssp': str,
                    'dsp': str,
                    'slp': str,
                    'dlp': str
                },
                'ether_hdr': {
                    'src_mac': str,
                    'dest_mac': str,
                    'vlan': int,
                    'ether_type': str
                },
                'ipv6_hdr': {
                    'dest_ip': str,
                    'src_ip': str,
                    'payload_len': int,
                    'hop_count': int,
                    'next_hdr': int

                }
            }
        }
    }


# =====================================================================================================#
#  Parser for 'show platform software fed switch active punt packet-capture display-filter icmpv6 brief #
# =====================================================================================================#
class ShowPlatformSoftwareFedSwitchActivePuntPacketCapturedisplayFiltericmpv6Brief(ShowPlatformSoftwareFedSwitchActivePuntPacketCapturedisplayFiltericmpv6BriefSchema):
    """

    Parser for
        'show platform software fed {switch} {switch_num} punt packet-capture display-filter icmpv6 brief'
        'show platform software fed {switch_num} punt packet-capture display-filter icmpv6 brief'
    """

    cli_command = ["show platform software fed {switch} {switch_num} punt packet-capture display-filter icmpv6 brief",
                   "show platform software fed {switch_num} punt packet-capture display-filter icmpv6 brief"]

    def cli(self, switch_num, switch , output=None):
        if output is None:
            if switch:
                cmd = self.cli_command[0].format(switch = switch,switch_num = switch_num)
            else:
                cmd = self.cli_command[1].format(switch_num = switch_num)

            output = self.device.execute(cmd)

        res_dict = {}

        #------ Punt Packet Number: 6, Timestamp: 2024/06/25 16:17:59.842 ------
        p0 = re.compile(r".+\s*Punt Packet Number\s*:\s*(?P<punt_packet_number>[\d]+)\s*\,\s*Timestamp\s*\:\s*(?P<timestamp>[\d\/\s\:\.]+).+")

        #interface : phy: Port-channel10 [if-id: 0x0000058a], pal: Port-channel10 [if-id: 0x0000058a]
        p1 = re.compile(r"interface\s*:\s*phy\s*:\s*(?P<phy_val>[\w\-]+)\s*\[if-id:\s*(?P<phy_if_id>[\w]+)\]\s*,\s*pal\s*:\s*(?P<pal_val>[\w\-]+)\s*\[if-id:\s*(?P<pal_if_id>[\w]+)\]")

        #misc info : cause: 58 [Layer2 bridge domain data packet], sub-cause: 11 [NONE], linktype: IPV6 [4]
        p2 = re.compile(r"misc info : cause:\s*(?P<cause>\d+)\s*\[(?P<cause_description>[^\]]+)\],\s*sub-cause:\s*(?P<sub_cause>\d+)\s*\[(?P<sub_cause_description>[^\]]+)\],\s*linktype:\s*(?P<link_type>[A-Z0-9\s]+)\s*\[\d+\]")

        #CE    hdr : dest mac: f4bd.9eff.fff0, src mac: f4bd.9eff.fff1, ethertype: 0x7106
        p3 = re.compile(r"CE\s+hdr\s*:\s*dest mac:\s*(?P<dest_mac>[0-9a-fA-F\.]+),\s*src mac:\s*(?P<src_mac>[0-9a-fA-F\.]+),\s*ethertype:\s*(?P<ethertype>0x[0-9a-fA-F]+)")

        #meta  hdr : Nxt. Hdr: 0x1, Fwd. Hdr: 0, SSP: 0x55f
        p4=re.compile(r"meta\s+hdr\s*:\s*Nxt\. Hdr:\s*(?P<nxt_hdr>0x[0-9a-fA-F]+),\s*Fwd\. Hdr:\s*(?P<fwd_hdr>\d+),\s*SSP:\s*(?P<ssp>0x[0-9a-fA-F]+)")

        #meta  hdr : DSP: 0xffff, SLP: 0x800fb, DLP: 0xef
        p5=re.compile(r"meta\s+hdr\s*:\s*D?SP:\s*(?P<dsp>0x[0-9a-fA-F]+),\s*SLP:\s*(?P<slp>0x[0-9a-fA-F]+),\s*D?LP:\s*(?P<dlp>0x[0-9a-fA-F]+)")

        #ether hdr : dest mac: 3333.0000.0016, src mac: a0b4.39cd.70ff
        p6 = re.compile(r"ether\s+hdr\s*:\s*dest mac:\s*(?P<dest_mac>[0-9a-fA-F\.]+),\s*src mac:\s*(?P<src_mac>[0-9a-fA-F\.]+)")

        #ether hdr : vlan: 100, ethertype: 0x8100
        p7 = re.compile(r"ether\s+hdr\s*:\s*vlan:\s*(?P<vlan>\d+),\s*ethertype:\s*(?P<ether_type>0x[0-9a-fA-F]+)")

        #ipv6  hdr : dest ip: ff02::16
        p8 = re.compile(r"ipv6\s+hdr\s*:\s*dest ip:\s*(?P<dest_ip>[a-fA-F0-9:]+)")

        #ipv6  hdr : src ip : fe80::a2b4:39ff:fecd:70ff
        p9 = re.compile(r"ipv6\s+hdr\s*:\s*src ip\s*:\s*(?P<src_ip>[a-fA-F0-9:]+)")

        #ipv6  hdr : payload len: 36, hop count: 1, next hdr: 0
        p10 = re.compile(r"ipv6\s+hdr\s*:\s*payload len:\s*(?P<payload_len>\d+),\s*hop count:\s*(?P<hop_count>\d+),\s*next hdr:\s*(?P<next_hdr>\d+)")

        for line in output.splitlines():
            line = line.strip()

            # Punt Packet Number: 6, Timestamp: 2024/06/25 16:17:59.842
            m = p0.match(line)
            if m:
                group = m.groupdict()
                punt_packet = res_dict.setdefault('punt_packet_number', {})
                punt_packet_details=punt_packet.setdefault(group['punt_packet_number'], {})
                punt_packet_details.setdefault('timestamp',group['timestamp'].strip())
                continue

            # interface : phy: Port-channel10 [if-id: 0x0000058a], pal: Port-channel10 [if-id: 0x0000058a]
            m = p1.match(line)
            if m:
                group = m.groupdict()
                phy = punt_packet_details.setdefault('interface', {}).setdefault('phy',{})
                pal = punt_packet_details.setdefault('interface', {}).setdefault('pal',{})
                phy['val'] = group['phy_val']
                phy['if_id'] = group['phy_if_id']
                pal['val'] = group['phy_val']
                pal['if_id'] = group['pal_if_id']
                continue

            # misc info : cause: 58 [Layer2 bridge domain data packet], sub-cause: 11 [NONE], linktype: IPV6 [4]
            m = p2.match(line)
            if m:
                group = m.groupdict()
                misc = punt_packet_details.setdefault('misc_info', {})
                misc.setdefault('cause_number' , int(group['cause']))
                misc.setdefault('cause_desc', group['cause_description'])
                misc.setdefault('subcause_number' , int(group['sub_cause']))
                misc.setdefault('subcause_desc', group['sub_cause_description'])
                misc['link_type'] = group['link_type']
                continue

            # CE    hdr : dest mac: f4bd.9eff.fff0, src mac: f4bd.9eff.fff1, ethertype: 0x7106
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ce_hdr = punt_packet_details.setdefault('ce_hdr', {})
                ce_hdr['src_mac'] = group['src_mac']
                ce_hdr['dest_mac'] = group['dest_mac']
                ce_hdr['ethertype'] = group['ethertype']
                continue

            # meta  hdr : Nxt. Hdr: 0x1, Fwd. Hdr: 0, SSP: 0x55f
            m=p4.match(line)
            if m:
                group = m.groupdict()
                meta_hdr = punt_packet_details.setdefault('meta_hdr', {})
                meta_hdr['nxt_hdr'] = group['nxt_hdr']
                meta_hdr['fwd_hdr'] = int(group['fwd_hdr'])
                meta_hdr['ssp'] = group['ssp']
                continue

            # meta  hdr : DSP: 0xffff, SLP: 0x800fb, DLP: 0xef
            m=p5.match(line)
            if m:
                group = m.groupdict()
                meta_hdr = punt_packet_details.setdefault('meta_hdr', {})
                meta_hdr['dsp'] = group['dsp']
                meta_hdr['dlp'] = group['dlp']
                meta_hdr['slp'] = group['slp']
                continue

            # ether hdr : dest mac: 3333.0000.0016, src mac: a0b4.39cd.70ff
            m = p6.match(line)
            if m:
                group = m.groupdict()
                ether_hdr = punt_packet_details.setdefault('ether_hdr', {})
                ether_hdr['src_mac'] = group['src_mac']
                ether_hdr['dest_mac'] = group['dest_mac']
                continue

            # ether hdr : vlan: 100, ethertype: 0x8100
            m = p7.match(line)
            if m:
                group = m.groupdict()
                ether_hdr = punt_packet_details.setdefault('ether_hdr', {})
                ether_hdr['vlan'] = int(group['vlan'])
                ether_hdr['ether_type'] = group['ether_type']
                continue

            # ipv6  hdr : dest ip: ff02::16
            m = p8.match(line)
            if m:
                group = m.groupdict()
                ipv6_hdr = punt_packet_details.setdefault('ipv6_hdr', {})
                ipv6_hdr['dest_ip'] = group['dest_ip']
                continue

            # ipv6  hdr : src ip : fe80::a2b4:39ff:fecd:70ff
            m = p9.match(line)
            if m:
                group = m.groupdict()
                ipv6_hdr['src_ip'] = group['src_ip']
                continue

            # ipv6  hdr : payload len: 36, hop count: 1, next hdr: 0
            m = p10.match(line)
            if m:
                group = m.groupdict()
                ipv6_hdr['payload_len'] = int(group['payload_len'])
                ipv6_hdr['hop_count'] = int(group['hop_count'])
                ipv6_hdr['next_hdr']  =int(group['next_hdr'])
                continue

        return res_dict


# =========================================
# Parser for 'show platform software fed active ip mfib vrf vrf_mcast group detail'
# =========================================

class ShowPlatformSoftwareFedIpMfibVrfGroupDetailSchema(MetaParser):
    """Schema for show platform software fed active ip mfib vrf {vrf_name} {group} detail"""

    schema = {
    'mvrf_table': {
        Any(): {
            'mcast_table': {
                'cpu_credit': int,
                'fset_aux_urid': str,
                'fset_urid': str,
                'gid': int,
                'group_ip': str,
                'hardware_info_asic': {
                    'cookie_urid': str,
                    'enable_rpf_check': int,
                    'ip_mcid_oid': int,
                    'punt_and_forward': int,
                    'punt_on_rpf_fail': int,
                    'rpf_port_oid': int,
                    'rpfid': int,
                    'use_rpfid': int
                },
                'hw_flag': str,
                'mcid_oid_asic': int,
                'mlist_handle': str,
                'mlist_urid': str,
                'npi_mroute_ent': str,
                'oif_details': {
                    Any(): {
                        'adj_id': str,
                        'flags': str,
                        'hw_flag': str,
                        'interface': str,
                        'intf_type': str,
                        'msg_type': str,
                        'parent_if': str
                    }
                },
                'rpf_adjancency_id': str,
                'source_ip': str,
                'svi_fwd_ifs': int,
                'total_packets': int
                }
            },
        }
    }


class ShowPlatformSoftwareFedIpMfibVrfGroupDetail(ShowPlatformSoftwareFedIpMfibVrfGroupDetailSchema):
    """Parser for show platform software fed active ip mfib vrf vrf_mcast 225.0.0.1 detail"""

    cli_command = [
        "show platform software fed {mode} ip mfib vrf {vrf_name} {group} detail",
        "show platform software fed {switch} {mode} ip mfib vrf {vrf_name} {group} detail",
    ]

    def cli(self, mode='', vrf_name='', group='', switch=None, output=None):
        if output is None:
            if switch:
                cmd = self.cli_command[1].format(mode=mode, vrf_name=vrf_name, group=group, switch=switch)
            else:
                cmd = self.cli_command[0].format(mode=mode, vrf_name=vrf_name, group=group)
            output = self.device.execute(cmd)

        ret_dict = {}
        index = 1
        index1 = 1

        # Mvrf: 2  ( 14.14.14.2, 225.0.0.1 ) Attrs:
        p1 = re.compile(r'.* +\( +(?P<source_ip>[\w\:\.\*\/]+)+\, +(?P<group_ip>[\w\:\.\/]+)')

        # Hw Flag                 : InHw
        p2 = re.compile(r'Hw Flag +\: +(?P<hw_flag>\w+)')

        # Mlist_hndl (Id)         : 0x118831561f8 ( 0x1fd2 )
        p3 = re.compile(r'Mlist_hndl +\(Id\) +\: +(?P<mlist_handle>\S+)')

        # Mlist Urid              : 0x1000000000001f91
        p4 = re.compile(r'Mlist Urid +\: +(?P<mlist_urid>\S+)')

        # Fset Urid (Hash)        : 0x3000000000000059 ( cad91c96 )
        p5 = re.compile(r'Fset Urid +\(Hash\) +\: +(?P<fset_urid>\S+)')

        # Fset Aux Urid           : 0x0
        p6 = re.compile(r'Fset Aux Urid +\: +(?P<fset_aux_urid>\S+)')

        # RPF Adjacency ID        : 0xf80054f1
        p7 = re.compile(r'RPF Adjacency ID +\: +(?P<rpf_adjancency_id>\S+)')

        # CPU Credit              : 0
        p8 = re.compile(r'CPU Credit +\: +(?P<cpu_credit>\d+)')

        # Total Packets           : 17918 ( 19 pps approx.)
        p9 = re.compile(r'Total Packets +\: +(?P<total_packets>\d+)')

        # npi_mroute_ent          : 0x118831bdc90
        p10 = re.compile(r'npi_mroute_ent +\: +(?P<npi_mroute_ent>\S+)')

        # svi_fwd_ifs             : 0
        p11 = re.compile(r'svi_fwd_ifs +\: +(?P<svi_fwd_ifs>\d+)')

        # OIF Details:
        #  AdjID          Interface          ParentIf        HwFlag      Flags      IntfType       MsgType
        #  0xf80054a1     Hu1/0/9            --------         ---        F NS       --------       NORMAL
        #  0xf80054f1     Hu1/0/23           --------         ---        A          --------       NORMAL
        p12 = re.compile(
            r'(?P<adj_id>\d\S+) +(?P<interface>[\w\:\.\/]+) +(?P<parent_if>\S+) +(?P<hw_flag>\S+) +(?P<flags>\D+) +(?P<intf_type>\S+) +(?P<msg_type>\w+)')

        # GID                   : 8276
        p13 = re.compile(r'GID +\: +(?P<gid>\d+)')

        # MCID OID Asic[0]      : 2282
        p14 = re.compile(r'MCID OID Asic\[0\] +\: +(?P<mcid_oid_asic>\d+)')

        # IP MCID OID         :2282 (cookie: urid:0x30::59)
        p15 = re.compile(r'IP MCID OID +\:+(?P<ip_mcid_oid>\d+) +\(cookie\: +urid\:(?P<cookie_urid>\S+)\)')

        # RPF PORT OID        :2130
        p16 = re.compile(r'RPF PORT OID  +\:+(?P<rpf_port_oid>\d+)')

        # punt_on_rpf_fail    :1
        p17 = re.compile(r'punt_on_rpf_fail  +\:+(?P<punt_on_rpf_fail>\d+)')

        # punt_and_forward    :0
        p18 = re.compile(r'punt_and_forward  +\:+(?P<punt_and_forward>\d+)')

        # use_rpfid           :0
        p19 = re.compile(r'use_rpfid  +\:+(?P<use_rpfid>\d+)')

        # rpfid               :0
        p20 = re.compile(r'rpfid  +\:+(?P<rpfid>\d+)')

        # enable_rpf_check    :1
        p21 = re.compile(r'enable_rpf_check  +\:+(?P<enable_rpf_check>\d+)')

        ret_dict = {}
        for line in output.splitlines():
            line = line.strip()

            # Mvrf: 2  ( 14.14.14.2, 225.0.0.1 ) Attrs:
            m = p1.match(line)
            if m:
                group = m.groupdict()
                vrf_dict = ret_dict.setdefault('mvrf_table', {}).setdefault(index, {})
                mvrf_dict = vrf_dict.setdefault('mcast_table', {})
                mvrf_dict['source_ip'] = group['source_ip']
                mvrf_dict['group_ip'] = group['group_ip']
                index += 1
                index1 = 1
                continue

            # Hw Flag                 : InHw
            m = p2.match(line)
            if m:
                group = m.groupdict()
                mvrf_dict['hw_flag'] = group['hw_flag']
                continue

            # Mlist_hndl (Id)         : 0x118831561f8 ( 0x1fd2 )
            m = p3.match(line)
            if m:
                group = m.groupdict()
                mvrf_dict['mlist_handle'] = group['mlist_handle']
                continue

            # Mlist Urid              : 0x1000000000001f91
            m = p4.match(line)
            if m:
                group = m.groupdict()
                mvrf_dict['mlist_urid'] = group['mlist_urid']
                continue

            # Fset Urid (Hash)        : 0x3000000000000059 ( cad91c96 )
            m = p5.match(line)
            if m:
                group = m.groupdict()
                mvrf_dict['fset_urid'] = group['fset_urid']
                continue

            # Fset Aux Urid           : 0x0
            m = p6.match(line)
            if m:
                group = m.groupdict()
                mvrf_dict['fset_aux_urid'] = group['fset_aux_urid']
                continue

            # RPF Adjacency ID        : 0xf80054f1
            m = p7.match(line)
            if m:
                group = m.groupdict()
                mvrf_dict['rpf_adjancency_id'] = group['rpf_adjancency_id']
                continue

            # CPU Credit              : 0
            m = p8.match(line)
            if m:
                group = m.groupdict()
                mvrf_dict['cpu_credit'] = int(group['cpu_credit'])
                continue

            # Total Packets           : 17918 ( 19 pps approx.)
            m = p9.match(line)
            if m:
                group = m.groupdict()
                mvrf_dict['total_packets'] = int(group['total_packets'])
                continue

            # npi_mroute_ent          : 0x118831bdc90
            m = p10.match(line)
            if m:
                group = m.groupdict()
                mvrf_dict['npi_mroute_ent'] = group['npi_mroute_ent']
                continue

            # svi_fwd_ifs             : 0
            m = p11.match(line)
            if m:
                group = m.groupdict()
                mvrf_dict['svi_fwd_ifs'] = int(group['svi_fwd_ifs'])
                continue

            # OIF Details:
            #  AdjID          Interface          ParentIf        HwFlag      Flags      IntfType       MsgType
            #  0xf80054a1     Hu1/0/9            --------         ---        F NS       --------       NORMAL
            #  0xf80054f1     Hu1/0/23           --------         ---        A          --------       NORMAL
            m = p12.match(line)
            if m:
                group = m.groupdict()
                global_dict = mvrf_dict.setdefault('oif_details', {}).setdefault(index1, {})
                global_dict['adj_id'] = group['adj_id']
                global_dict['interface'] = group['interface']
                global_dict['parent_if'] = group['parent_if']
                global_dict['hw_flag'] = group['hw_flag']
                global_dict['flags'] = group['flags'].strip()
                global_dict['intf_type'] = group['intf_type']
                global_dict['msg_type'] = group['msg_type']
                index1 += 1
                continue

            # GID                   : 8276
            m = p13.match(line)
            if m:
                group = m.groupdict()
                mvrf_dict['gid'] = int(group['gid'])
                continue

            # MCID OID Asic[0]      : 2282
            m = p14.match(line)
            if m:
                group = m.groupdict()
                mvrf_dict['mcid_oid_asic'] = int(group['mcid_oid_asic'])
                continue

            # IP MCID OID         :2282 (cookie: urid:0x30::59)
            m = p15.match(line)
            if m:
                group = m.groupdict()
                local_dict = mvrf_dict.setdefault('hardware_info_asic', {})
                local_dict['ip_mcid_oid'] = int(group['ip_mcid_oid'])
                local_dict['cookie_urid'] = group['cookie_urid']
                continue

            # RPF PORT OID        :2130
            m = p16.match(line)
            if m:
                group = m.groupdict()
                local_dict['rpf_port_oid'] = int(group['rpf_port_oid'])
                continue

            # punt_on_rpf_fail    :1
            m = p17.match(line)
            if m:
                group = m.groupdict()
                local_dict['punt_on_rpf_fail'] = int(group['punt_on_rpf_fail'])
                continue

            # punt_and_forward    :0
            m = p18.match(line)
            if m:
                group = m.groupdict()
                local_dict['punt_and_forward'] = int(group['punt_and_forward'])
                continue

            # use_rpfid           :0
            m = p19.match(line)
            if m:
                group = m.groupdict()
                local_dict['use_rpfid'] = int(group['use_rpfid'])
                continue

            # rpfid               :0
            m = p20.match(line)
            if m:
                group = m.groupdict()
                local_dict['rpfid'] = int(group['rpfid'])
                continue

            # enable_rpf_check    :1
            m = p21.match(line)
            if m:
                group = m.groupdict()
                local_dict['enable_rpf_check'] = int(group['enable_rpf_check'])
                continue

        return ret_dict


class ShowPlatformHardwareFedSwitchQosQueueConfigSchema(MetaParser):
    """
    Schema for
        * 'show platform hardware fed switch {switch_var} qos queue config interface {interface}'
    """

    schema = {
        "interface": {
            Any(): {
                "interface_id": str,
                "voq_id": str,
                "voq_oid": str,
                "voq_set_size": str,
                "base_voq_id": str,
                "base_vsc_ids": list,
                "voq_state": str,
                "voq_flush": str,
                "is_empty": str,
                "profile_oid": {
                    Any(): {
                        "profile_id": str,
                        "device_id": str,
                        "cgm_type": str,
                        "profile_reference_count": str,
                        "is_reserved": str,
                        "for_speeds": str,
                        "associated_voq_offsets": Or(str, list),
                        "hbm_enabled": str,
                        Optional("hgm_block_size"): str,
                        Optional("red_enabled"): str,
                        Optional("fcn_enabled"): str,
                        Optional("queue_user_config"): {
                            Optional("q_limit_hbm_blocks"): str,
                            "red_ema_coefficient": str,
                            Optional("red_flag"): {
                                Any(): {
                                    Optional("minimun_hbm_blocks"): str,
                                    Optional("maximum_hbm_blocks"): str,
                                    Optional("maximum_probability"): str,
                                },
                            },
                        },
                        Optional("queue_hw_values"): {
                            "red_action": str,
                            Optional("red_drop_thresholds"): list,
                            Optional("hbm_free_thresholds"): list,
                            Optional("hbm_voq_age_thresholds"): list,
                            Optional("hbm_voq_thresholds"): list,
                            Optional("red_flag"): {
                                Any(): {
                                    "red_drop_probabilities": list,
                                }
                            },
                        },
                    }
                },
            }
        }
    }


class ShowPlatformHardwareFedSwitchQosQueueConfig(
    ShowPlatformHardwareFedSwitchQosQueueConfigSchema
):
    """
    Parser for
        * 'show platform hardware fed switch {switch_var} qos queue config interface {interface}'
    """

    cli_command = [
        "show platform hardware fed active qos queue config interface {interface}",
        "show platform hardware fed switch {switch_num} qos queue config interface {interface}",
    ]

    def cli(self, command=None, output=None, **kwargs):
        if output is None:
            output = self.device.execute(command)

        # Interface : HundredGigE2/0/34.100 (0x54C)
        p0 = re.compile(
            r"^Interface\s+: (?P<interface>\S+) \((?P<interface_id>\S+)\)$"
        )

        # VOQ OID        : 2114(0x842)
        p1 = re.compile(r"^VOQ OID\s+: (?P<voq_oid>\S+)\((?P<voq_id>\S+)\)$")

        # VOQ Set Size   : 3
        p2 = re.compile(r"^VOQ Set Size\s+: (?P<voq_set_size>\S+)$")

        # Base VOQ ID    : 28952
        p3 = re.compile(r"^Base VOQ ID\s+: (?P<base_voq_id>\S+)$")

        # Base VSC IDs   : 728, 792, 856, 920, 984, 1048
        p4 = re.compile(r"^Base VSC IDs\s+: (?P<base_vsc_ids>[\w\s\,]+)$")

        # VOQ State      : Active
        p5 = re.compile(r"^VOQ State\s+: (?P<voq_state>\S+)$")

        # VOQ Flush      : Flush not active
        p6 = re.compile(r"^VOQ Flush\s+: (?P<voq_flush>.+)$")

        # Is Empty       : Yes
        p7 = re.compile(r"^Is Empty\s+: (?P<is_empty>.+)$")

        # Profile OID            : 433(0x1B1)
        p8_1 = re.compile(
            r"^Profile OID\s+: (?P<profile_oid>\d+)\((?P<profile_id>\w+)\)$"
        )

        # Device ID              : 0
        p9 = re.compile(r"^Device ID\s+: (?P<device_id>\d+)$")

        # CGM Type               : Unicast
        p10 = re.compile(r"^CGM Type\s+: (?P<cgm_type>\w+)$")

        # Profile reference count: 73
        p11 = re.compile(
            r"^Profile reference count\s*: (?P<profile_reference_count>\d+)$"
        )

        # Is Reserved            : Yes
        p12 = re.compile(r"^Is Reserved\s+: (?P<is_reserved>[\w\s]+)$")

        # For speeds             : 10000000000
        p13 = re.compile(r"^For speeds\s+: (?P<for_speeds>\d+)$")

        # Associated VOQ Offsets : 0
        p14 = re.compile(
            r"^Associated VOQ Offsets\s+: (?P<associated_voq_offsets>[\d, ]+)$"
        )

        # HBM Enabled            : Enabled
        p15 = re.compile(r"^HBM Enabled\s+: (?P<hbm_enabled>\w+)$")

        # HBM Block Size         : 6144
        p16 = re.compile(r"^HBM Block Size\s+: (?P<hgm_block_size>\w+)$")

        # RED Enabled            : Enabled
        p17 = re.compile(r"^RED Enabled\s+: (?P<red_enabled>\w+)$")

        # FCN Enabled            : Disabled
        p18 = re.compile(r"^FCN Enabled\s+: (?P<fcn_enabled>\w+)$")

        # Queue User Config      :
        p19 = re.compile(r"^Queue User Config\s+:$")

        # Q-Limit(HBM Blocks)    : 4882
        p19_1 = re.compile(
            r"^Q-Limit\(HBM Blocks\)\s+: (?P<q_limit_hbm_blocks>\d+)$"
        )

        # RED EMA Coefficient    : 1.000000
        p19_2 = re.compile(
            r"^RED EMA Coefficient\s+: (?P<red_ema_coefficient>[\w\.]+)$"
        )

        # RED Green :
        p19_3 = re.compile(r"^RED\s+(?P<red_flag>\w+)\s:$")

        # Minium(HBM BLOCKS)   : 0
        p19_4 = re.compile(
            r"^Minium\(HBM BLOCKS\)\s*: (?P<minimun_hbm_blocks>\d+)$"
        )

        # Maximum(HBM BLOCKS)  : 1220
        p19_5 = re.compile(
            r"^Maximum\(HBM BLOCKS\)\s*: (?P<maximum_hbm_blocks>\d+)$"
        )

        # Maximum Probability  : 0
        p19_6 = re.compile(
            r"^Maximum Probability\s*: (?P<maximum_probability>\d+)$"
        )

        # Queue H/W Values       :
        p20 = re.compile(r"^Queue H/W Values\s+:$")

        # RED Action                     : Drop
        p20_1 = re.compile(r"^RED Action\s+: (?P<red_action>\w+)$")

        # RED Drop thresholds            : 0, 1220, 1220, 1220, 1220, 1220, 1220, 1220, 1220, 1220, 1220, 1220, 1220, 1220, 1220
        p20_2 = re.compile(
            r"^RED Drop thresholds\s+: (?P<red_drop_thresholds>[\w\s\,]+)$"
        )

        # RED Drop Probabilities[Green]  : 0.000000, 0.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000
        p20_3 = re.compile(
            r"^RED Drop Probabilities\[(?P<red_flag>[\w]+)\]\s+: (?P<red_drop_probabilities>[\w\s\,\.]+)$"
        )

        # HBM Free Thresholds            : 10000, 20000, 40000, 60000, 124992, 250000, 500000, 1000000
        p20_4 = re.compile(
            r"^HBM Free Thresholds\s+: (?P<hbm_free_thresholds>[\w\s\,\.]+)$"
        )

        # HBM VOQ Age Thresholds         : 1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 16, 24, 32, 64, 128
        p20_5 = re.compile(
            r"^HBM VOQ Age Thresholds\s+: (?P<hbm_voq_age_thresholds>[\w\s\,\.]+)$"
        )

        # HBM VOQ Thresholds             : 96, 992, 2000, 4000, 6000, 8000, 12000, 16000, 24000, 32000, 40000, 48000, 56000, 64000, 64512, 65536,
        p20_6 = re.compile(
            r"^HBM VOQ Thresholds\s+: (?P<hbm_voq_thresholds>[\w\s\,\.]+)$"
        )

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # Interface              : HundredGigE1/0/5 (0x54A)
            m = p0.match(line)
            if m:
                int_dict = ret_dict.setdefault("interface", {}).setdefault(
                    Common.convert_intf_name(m.groupdict()["interface"]), {}
                )
                int_dict["interface_id"] = m.groupdict()["interface_id"]
                continue

            # VOQ OID        : 2114(0x842)
            m = p1.match(line)
            if m:
                int_dict["voq_id"] = m.groupdict()["voq_id"]
                int_dict["voq_oid"] = m.groupdict()["voq_oid"]
                continue

            # VOQ Set Size   : 3
            m = p2.match(line)
            if m:
                int_dict["voq_set_size"] = m.groupdict()["voq_set_size"]
                continue

            # Base VOQ ID    : 28952
            m = p3.match(line)
            if m:
                int_dict["base_voq_id"] = m.groupdict()["base_voq_id"]
                continue

            # Base VSC IDs   : 728, 792, 856, 920, 984, 1048
            m = p4.match(line)
            if m:
                int_dict["base_vsc_ids"] = (
                    m.groupdict()["base_vsc_ids"].replace(" ", "").split(",")
                )
                continue

            # VOQ State      : Active
            m = p5.match(line)
            if m:
                int_dict["voq_state"] = m.groupdict()["voq_state"]
                continue

            # VOQ Flush      : Flush not active
            m = p6.match(line)
            if m:
                int_dict["voq_flush"] = m.groupdict()["voq_flush"]
                continue

            # Is Empty       : Yes
            m = p7.match(line)
            if m:
                int_dict["is_empty"] = m.groupdict()["is_empty"]
                continue

            # Profile OID            : 433(0x1B1)
            m = p8_1.match(line)
            if m:
                profile_dict = int_dict.setdefault("profile_oid", {}).setdefault(
                    m.groupdict()["profile_oid"], {}
                )
                profile_dict["profile_id"] = m.groupdict()["profile_id"]
                continue

            # Device ID              : 0
            m = p9.match(line)
            if m:
                profile_dict["device_id"] = m.groupdict()["device_id"]
                continue

            # CGM Type               : Unicast
            m = p10.match(line)
            if m:
                profile_dict["cgm_type"] = m.groupdict()["cgm_type"]
                continue

            # Profile reference count: 73
            m = p11.match(line)
            if m:
                profile_dict["profile_reference_count"] = m.groupdict()[
                    "profile_reference_count"
                ]
                continue

            # Is Reserved            : Yes
            m = p12.match(line)
            if m:
                profile_dict["is_reserved"] = m.groupdict()["is_reserved"]
                continue

            # For speeds             : 10000000000
            m = p13.match(line)
            if m:
                profile_dict["for_speeds"] = m.groupdict()["for_speeds"]
                continue

            # Associated VOQ Offsets : 0
            m = p14.match(line)
            if m:
                profile_dict["associated_voq_offsets"] = (
                    m.groupdict()["associated_voq_offsets"]
                    .replace(" ", "")
                    .split(",")
                )
                continue

            # HBM Enabled            : Enabled
            m = p15.match(line)
            if m:
                profile_dict["hbm_enabled"] = m.groupdict()["hbm_enabled"]
                continue

            # HBM Block Size         : 6144
            m = p16.match(line)
            if m:
                profile_dict["hgm_block_size"] = m.groupdict()["hgm_block_size"]
                continue

            # RED Enabled            : Enabled
            m = p17.match(line)
            if m:
                profile_dict["red_enabled"] = m.groupdict()["red_enabled"]
                continue

            # FCN Enabled            : Disabled
            m = p18.match(line)
            if m:
                profile_dict["fcn_enabled"] = m.groupdict()["fcn_enabled"]
                continue

            # Queue User Config      :
            m = p18.match(line)
            if m:
                profile_dict["fcn_enabled"] = m.groupdict()["fcn_enabled"]
                continue

            # Queue User Config      :
            m = p19.match(line)
            if m:
                queue_config_dict = profile_dict.setdefault("queue_user_config", {})
                continue

            # Q-Limit(HBM Blocks)    : 1220
            m = p19_1.match(line)
            if m:
                queue_config_dict["q_limit_hbm_blocks"] = m.groupdict()[
                    "q_limit_hbm_blocks"
                ]
                continue

            # RED EMA Coefficient    : 1.000000
            m = p19_2.match(line)
            if m:
                queue_config_dict["red_ema_coefficient"] = m.groupdict()[
                    "red_ema_coefficient"
                ]
                continue

            # RED Green :
            m = p19_3.match(line)
            if m:
                red_dict = queue_config_dict.setdefault("red_flag", {}).setdefault(
                    m.groupdict()["red_flag"], {}
                )
                continue

            # Minium(HBM BLOCKS)   : 0
            m = p19_4.match(line)
            if m:
                red_dict["minimun_hbm_blocks"] = m.groupdict()["minimun_hbm_blocks"]
                continue

            # Maximum(HBM BLOCKS)  : 1220
            m = p19_5.match(line)
            if m:
                red_dict["maximum_hbm_blocks"] = m.groupdict()["maximum_hbm_blocks"]
                continue

            # Maximum Probability  : 0
            m = p19_6.match(line)
            if m:
                red_dict["maximum_probability"] = m.groupdict()[
                    "maximum_probability"
                ]
                continue

            # Queue H/W Values       :
            m = p20.match(line)
            if m:
                queue_hw_dict = profile_dict.setdefault("queue_hw_values", {})
                continue

            # RED Action                     : Drop
            m = p20_1.match(line)
            if m:
                queue_hw_dict["red_action"] = m.groupdict()["red_action"]
                continue

            # RED Drop thresholds            : 0, 1220, 1220, 1220, 1220, 1220, 1220, 1220, 1220, 1220, 1220, 1220, 1220, 1220, 1220
            m = p20_2.match(line)
            if m:
                queue_hw_dict["red_drop_thresholds"] = (
                    m.groupdict()["red_drop_thresholds"].replace(" ", "").split(",")
                )
                continue

            # RED Drop Probabilities[Green]  : 0.000000, 0.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000
            m = p20_3.match(line)
            if m:
                red_hw_dict = queue_hw_dict.setdefault("red_flag", {}).setdefault(
                    m.groupdict()["red_flag"], {}
                )
                red_hw_dict["red_drop_probabilities"] = (
                    m.groupdict()["red_drop_probabilities"]
                    .replace(" ", "")
                    .split(",")
                )
                continue

            # HBM Free Thresholds            : 10000, 20000, 40000, 60000, 124992, 250000, 500000, 1000000
            m = p20_4.match(line)
            if m:
                queue_hw_dict["hbm_free_thresholds"] = (
                    m.groupdict()["hbm_free_thresholds"].replace(" ", "").split(",")
                )
                continue

            # HBM VOQ Age Thresholds         : 1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 16, 24, 32, 64, 128
            m = p20_5.match(line)
            if m:
                queue_hw_dict["hbm_voq_age_thresholds"] = (
                    m.groupdict()["hbm_voq_age_thresholds"]
                    .replace(" ", "")
                    .split(",")
                )
                continue

            # HBM VOQ Thresholds             : 96, 992, 2000, 4000, 6000, 8000, 12000, 16000, 24000, 32000, 40000, 48000, 56000, 64000, 64512, 65536,
            m = p20_6.match(line)
            if m:
                queue_hw_dict["hbm_voq_thresholds"] = (
                    m.groupdict()["hbm_voq_thresholds"].replace(" ", "").split(",")
                )
                continue

        return ret_dict
