"""show_platform.py

    IOS parsers for the following show commands:

    * show version
    * dir
    * show redundancy
    * show inventory
    * show bootvar
    * show processes cpu sorted
    * show processes cpu sorted <1min|5min|5sec>
    * show processes cpu sorted | include <WORD>
    * show processes cpu sorted <1min|5min|5sec> | include <WORD>
    * show processes cpu
    * show processes cpu | include <WORD>

"""
# python
import re

# genie
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
    Any, Optional

# import iosxe parser
from genie.libs.parser.iosxe.show_platform import \
    ShowVersion as ShowVersion_iosxe, \
    Dir as Dir_iosxe, \
    ShowInventorySchema as ShowInventorySchema_iosxe, \
    ShowRedundancy as ShowRedundancy_iosxe, \
    ShowProcessesCpuSorted as ShowProcessesCpuSorted_iosxe, \
    ShowProcessesCpu as ShowProcessesCpu_iosxe, \
    ShowVersionRp as ShowVersionRp_iosxe, \
    ShowPlatform as ShowPlatform_iosxe, \
    ShowPlatformPower as ShowPlatformPower_iosxe, \
    ShowProcessesCpuHistory as ShowProcessesCpuHistory_iosxe, \
    ShowProcessesCpuPlatform as ShowProcessesCpuPlatform_iosxe, \
    ShowPlatformSoftwareStatusControl as ShowPlatformSoftwareStatusControl_iosxe, \
    ShowPlatformSoftwareSlotActiveMonitorMem as ShowPlatformSoftwareSlotActiveMonitorMem_iosxe, \
    ShowPlatformHardware as ShowPlatformHardware_iosxe, \
    ShowPlatformHardwarePlim as ShowPlatformHardwarePlim_iosxe, \
    ShowPlatformHardwareQfpBqsOpmMapping as ShowPlatformHardwareQfpBqsOpmMapping_iosxe, \
    ShowPlatformHardwareQfpBqsIpmMapping as ShowPlatformHardwareQfpBqsIpmMapping_iosxe, \
    ShowPlatformHardwareSerdes as ShowPlatformHardwareSerdes_iosxe, \
    ShowPlatformHardwareSerdesInternal as ShowPlatformHardwareSerdesInternal_iosxe, \
    ShowPlatformHardwareQfpBqsStatisticsChannelAll as ShowPlatformHardwareQfpBqsStatisticsChannelAll_iosxe, \
    ShowPlatformHardwareQfpInterfaceIfnameStatistics as ShowPlatformHardwareQfpInterfaceIfnameStatistics_iosxe, \
    ShowPlatformHardwareQfpStatisticsDrop as ShowPlatformHardwareQfpStatisticsDrop_iosxe, \
    ShowEnvironment as ShowEnvironment_iosxe, \
    ShowModule as ShowModule_iosxe, \
    ShowSwitch as ShowSwitch_iosxe, \
    ShowSwitchDetail as ShowSwitchDetail_iosxe


class ShowVersion(ShowVersion_iosxe):
    """Parser for show version
    """
    exclude = ['system_restarted_at', 'uptime_this_cp', 'uptime']
    pass


class Dir(Dir_iosxe):
    """Parser for dir
    """
    exclude = ['last_modified_date', 'bytes_free', 'files']
    pass


class ShowRedundancyIosSchema(MetaParser):
    """Schema for show redundancy """
    schema = {
        'red_sys_info': {
            'available_system_uptime': str,
            'switchovers_system_experienced': str,
            'standby_failures': str,
            'last_switchover_reason': str,
            'hw_mode': str,
            Optional('conf_red_mode'): str,
            Optional('oper_red_mode'): str,
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


class ShowRedundancy(ShowRedundancyIosSchema, ShowRedundancy_iosxe):
    """Parser for show redundancy
    """
    pass


class ShowInventory(ShowInventorySchema_iosxe):
    """
    Parser for:
        * show inventory
    """
    cli_command = 'show inventory'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Init vars
        parsed_output = {}
        flag_is_slot = False
        oc_key_values = ['power', 'fan', 'clock']

        # NAME: "CLK-7600 1", DESCR: "OSR-7600 Clock FRU 1"
        # NAME: "WS-C6504-E", DESCR: "Cisco Systems Cisco 6500 4-slot Chassis System"
        r1 = re.compile(r'NAME\:\s*\"(?P<name>.+)\"\,\s*DESCR:\s*\"(?P<description>.+)\"')

        # 1
        # 2
        # 3
        r1_1 = re.compile(r'(?P<slot>\d+)')

        # msfc sub-module of 1
        # VS-F6K-PFC4 Policy Feature Card 4 EARL sub-module of 1
        r1_2 = re.compile(r'.*module of (?P<slot>\d+).*')

        # Switch 1 - Power Supply 1
        r1_2_2 = re.compile(r'Switch +(?P<subslot>\d+).*')

        # Transceiver Te2/1
        # Transceiver Te2/15
        # Transceiver Te5/1
        r1_3 = re.compile(r'Transceiver\s+Te(?P<slot>\d+)\/(?P<subslot>\d+)')

        # TenGigabitEthernet2 / 1 / 1
        # GigabitEthernet3 / 0 / 50
        r1_3_2 = re.compile(r'(?:Ten)?GigabitEthernet(?P<subslot>[\d\s\/]+)$')

        # VS-SUP2T-10G 5 ports Supervisor Engine 2T 10GE w/ CTS Rev. 1.5
        # WS-SUP720-3BXL 2 ports Supervisor Engine 720 Rev. 5.6
        r1_4 = re.compile(r'.*ports\s+Supervisor\s+Engine.*')

        # WS-X6824-SFP CEF720 24 port 1000mb SFP Rev. 1.0
        # WS-X6748-GE-TX CEF720 48 port 10/100/1000mb Ethernet Rev. 3.4
        r1_5 = re.compile(r'.*WS\-X.*')

        # NAME: "IOSv"
        r1_6 = re.compile(r'.*IOSv.*')

        # PID: WS-C6504-E        ,                     VID: V01, SN: FXS1712Q1R8
        # PID: CLK-7600          ,                     VID:    , SN: FXS170802GL
        r2 = re.compile(r'PID:\s*(?P<pid>.+)\s*\,\s*VID:\s*(?P<vid>.*)\,\s*SN:\s*(?P<sn>.+)')

        for line in output.splitlines():
            line = line.strip()

            result = r1.match(line)
            if result:
                group = result.groupdict()

                name = group['name']
                descr = group['description']

                continue

            result = r2.match(line)
            if result:
                group = result.groupdict()

                pid = group['pid'].strip()
                vid = group.get('vid', '')
                sn = group['sn']

                if 'Chassis' in descr:
                    chassis_dict = parsed_output.setdefault('main', {})\
                        .setdefault('chassis', {})\
                        .setdefault(pid, {})

                    chassis_dict['name'] = name
                    chassis_dict['descr'] = descr
                    chassis_dict['pid'] = pid                    
                    chassis_dict['vid'] = vid
                    chassis_dict['sn'] = sn

                    continue
                # 1
                # 2
                # 3
                result = r1_1.match(name)
                if result:
                    flag_is_slot = True
                    group = result.groupdict()
                    slot = group['slot']

                    # VS-SUP2T-10G 5 ports Supervisor Engine 2T 10GE w/ CTS Rev. 1.5
                    # WS-SUP720-3BXL 2 ports Supervisor Engine 720 Rev. 5.6
                    # PID: WS-C3750X-48T-S   , VID: V02  , SN: FDO1511R12W
                    if r1_4.match(descr) or 'WS-C' in pid:
                        slot_code = 'rp'

                    # WS-X6824-SFP CEF720 24 port 1000mb SFP Rev. 1.0
                    # WS-X6748-GE-TX CEF720 48 port 10/100/1000mb Ethernet Rev. 3.4
                    if r1_5.match(descr):
                        slot_code = 'lc'

                    slot_dict = parsed_output\
                        .setdefault('slot', {})\
                        .setdefault(slot, {})\
                        .setdefault(slot_code, {})\
                        .setdefault(pid, {})
                    
                    slot_dict['name'] = name
                    slot_dict['descr'] = descr
                    slot_dict['pid'] = pid
                    slot_dict['vid'] = vid
                    slot_dict['sn'] = sn

                    continue

                # msfc sub-module of 1
                # VS-F6K-PFC4 Policy Feature Card 4 EARL sub-module of 1
                result = r1_2.match(name)

                if result:
                    group = result.groupdict()
                    slot = group['slot']

                    subslot = "0"

                    subslot_dict = slot_dict\
                        .setdefault('subslot', {})\
                        .setdefault(subslot, {})\
                        .setdefault(pid, {})

                    subslot_dict['descr'] = descr
                    subslot_dict['name'] = name
                    subslot_dict['pid'] = pid
                    subslot_dict['sn'] = sn
                    subslot_dict['vid'] = vid

                    continue

                # Switch 1 - Power Supply 1
                # TenGigabitEthernet2 / 1 / 1
                # GigabitEthernet3/0/50
                result = r1_2_2.match(name)
                result_2 = r1_3_2.match(name)

                if result or result_2:
                    if result:
                        group = result.groupdict()
                    elif result_2:
                        group = result_2.groupdict()
                    subslot = group['subslot']

                    subslot_dict = slot_dict \
                        .setdefault('subslot', {}) \
                        .setdefault(subslot, {}) \
                        .setdefault(pid, {})

                    subslot_dict['descr'] = descr
                    subslot_dict['name'] = name
                    subslot_dict['pid'] = pid
                    subslot_dict['sn'] = sn
                    subslot_dict['vid'] = vid
                    continue

                # Transceiver Te2/1
                # Transceiver Te2/15
                # Transceiver Te5/1
                result = r1_3.match(name)
                if result:
                    group = result.groupdict()
                    slot = group['slot']
                    subslot = group['subslot']

                    subslot_dict = slot_dict\
                        .setdefault('subslot', {})\
                        .setdefault(subslot, {})\
                        .setdefault(pid, {})

                    subslot_dict['descr'] = descr
                    subslot_dict['name'] = name
                    subslot_dict['pid'] = pid
                    subslot_dict['sn'] = sn
                    subslot_dict['vid'] = vid

                    continue

                # NAME: "IOSv"
                result = r1_6.match(name)
                if result:
                    slot = '1'
                    slot_dict = parsed_output\
                        .setdefault('slot', {})\
                        .setdefault(slot, {})\
                        .setdefault('rp', {})\
                        .setdefault(pid, {})
                    
                    slot_dict['name'] = name
                    slot_dict['descr'] = descr
                    slot_dict['pid'] = pid
                    slot_dict['vid'] = vid
                    slot_dict['sn'] = sn

                    continue               

                # Name could be:
                # 2700W AC power supply for CISCO7604 2
                # High Speed Fan Module for CISCO7604 1
                if any(key in descr.lower() for key in oc_key_values):
                    other_dict = parsed_output\
                        .setdefault('slot', {})\
                        .setdefault(name, {})\
                        .setdefault('other', {})\
                        .setdefault(name, {})

                    other_dict['name'] = name
                    other_dict['descr'] = descr
                    other_dict['pid'] = pid
                    other_dict['vid'] = vid
                    other_dict['sn'] = sn

                    continue

        return parsed_output

class ShowBootvarSchema(MetaParser):
    """Schema for show bootvar"""

    schema = {
        Optional('current_boot_variable'): str,
        Optional('next_reload_boot_variable'): str,
        Optional('config_file'): str,
        Optional('bootldr'): str,
        Optional('active'): {
            'configuration_register': str,
            Optional('boot_variable'): str,
        },
        Optional('standby'): {
            'configuration_register': str,
            Optional('boot_variable'): str,
        },
    }


class ShowBootvar(ShowBootvarSchema):
    """Parser for show boot"""

    cli_command = 'show boot'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        boot_dict = {}
        boot_variable = None

        # BOOT variable = bootflash:/asr1000rpx.bin,12;
        # BOOT variable = flash:cat3k_caa-universalk9.BLD_POLARIS_DEV_LATEST_20150907_031219.bin;flash:cat3k_caa-universalk9.BLD_POLARIS_DEV_LATEST_20150828_174328.SSA.bin;flash:ISSUCleanGolden;
        p1 = re.compile(r'^BOOT +variable +=( *(?P<var>\S+);)?$')

        # Standby BOOT variable = bootflash:/asr1000rpx.bin,12;
        p2 = re.compile(r'^Standby +BOOT +variable +=( *(?P<var>\S+);)?$')

        # Configuration register is 0x2002
        p3 = re.compile(r'^Configuration +register +is +(?P<var>\w+)$')

        # Standby Configuration register is 0x2002
        p4 = re.compile(r'^Standby +Configuration +register +is +(?P<var>\w+)$')

        # CONFIG_FILE variable =
        p5 = re.compile(r'^CONFIG_FILE +variable += +(?P<var>\S+)$')

        # BOOTLDR variable =
        p6 = re.compile(r'^BOOTLDR +variable += +(?P<var>\S+)$')

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
                boot_dict.setdefault('active', {})['configuration_register'] = m.groupdict()['var']
                continue

            # Standby Configuration register is 0x2002
            m = p4.match(line)
            if m:
                boot_dict.setdefault('standby', {})['configuration_register'] = m.groupdict()['var']
                continue

            # CONFIG_FILE variable =
            m = p5.match(line)
            if m:
                if m.groupdict()['var']:
                    boot_dict.setdefault('active', {})['config_file'] = m.groupdict()['var']
                continue

            # BOOTLDR variable =
            m = p6.match(line)
            if m:
                if m.groupdict()['var']:
                    boot_dict.setdefault('standby', {})['bootldr'] = m.groupdict()['var']
                continue
        return boot_dict


class ShowProcessesCpuSorted(ShowProcessesCpuSorted_iosxe):
    """Parser for show processes cpu sorted
                  show processes cpu sorted <1min|5min|5sec>
                  show processes cpu sorted | include <WORD>
                  show processes cpu sorted <1min|5min|5sec> | include <WORD>
    """
    pass


class ShowProcessesCpu(ShowProcessesCpu_iosxe):
    """Parser for show processes cpu
                  show processes cpu | include <WORD>"""
    pass


class ShowVersionRp(ShowVersionRp_iosxe):
    """Parser for show version RP active [running|provisioned|installed]
                  show version RP standby [running|provisioned|installed]"""
    pass


class ShowPlatform(ShowPlatform_iosxe):
    """Parser for Parser for show platform"""
    pass


class ShowPlatformPower(ShowPlatformPower_iosxe):
    """Parser for Parser for show platform power"""
    pass


class ShowProcessesCpuHistory(ShowProcessesCpuHistory_iosxe):
    """Parser for show processes cpu history"""
    pass


class ShowProcessesCpuPlatform(ShowProcessesCpuPlatform_iosxe):
    """Parser for show processes cpu platform"""
    pass


class ShowPlatformSoftwareStatusControl(ShowPlatformSoftwareStatusControl_iosxe):
    """Parser for show platform software status control-processor brief"""
    pass


class ShowPlatformSoftwareSlotActiveMonitorMem(ShowPlatformSoftwareSlotActiveMonitorMem_iosxe):
    """Parser for show platform software process slot switch active R0 monitor | inc Mem :|Swap:"""
    pass


class ShowPlatformHardware(ShowPlatformHardware_iosxe):
    """Parser for show platform hardware qfp active infrastructure bqs queue output default all"""
    pass


class ShowPlatformHardwarePlim(ShowPlatformHardwarePlim_iosxe):
    """Parser for show platform hardware port <x/x/x> plim statistics
                  show platform hardware slot <x> plim statistics
                  show platform hardware slot <x> plim statistics internal
                  show platform hardware subslot <x/x> plim statistics"""
    pass


class ShowPlatformHardwareQfpBqsOpmMapping(ShowPlatformHardwareQfpBqsOpmMapping_iosxe):
    """Parser for show platform hardware qfp active bqs <x> opm mapping
                  show platform hardware qfp standby bqs <x> opm mapping"""
    pass


class ShowPlatformHardwareQfpBqsIpmMapping(ShowPlatformHardwareQfpBqsIpmMapping_iosxe):
    """Parser for show platform hardware qfp active bqs <x> ipm mapping
                  show platform hardware qfp standby bqs <x> ipm mapping"""
    pass


class ShowPlatformHardwareSerdes(ShowPlatformHardwareSerdes_iosxe):
    """Parser for show platform hardware slot <x> serdes statistics"""
    pass


class ShowPlatformHardwareSerdesInternal(ShowPlatformHardwareSerdesInternal_iosxe):
    """Parser for show platform hardware slot <x> serdes statistics internal"""
    pass


class ShowPlatformHardwareQfpBqsStatisticsChannelAll(ShowPlatformHardwareQfpBqsStatisticsChannelAll_iosxe):
    """Parser for show platform hardware qfp active bqs <x> ipm statistics channel all
                  show platform hardware qfp standby bqs <x> ipm statistics channel all
                  show platform hardware qfp active bqs <x> opm statistics channel all
                  show platform hardware qfp standby bqs <x> opm statistics channel all"""
    pass


class ShowPlatformHardwareQfpInterfaceIfnameStatistics(ShowPlatformHardwareQfpInterfaceIfnameStatistics_iosxe):
    """Parser for show platform hardware qfp active interface if-name <interface> statistics
                  show platform hardware qfp standby interface if-name <interface> statistics"""
    pass


class ShowPlatformHardwareQfpStatisticsDrop(ShowPlatformHardwareQfpStatisticsDrop_iosxe):
    """Parser for show platform hardware qfp active statistics drop
                  show platform hardware qfp standby statistics drop"""
    pass


class ShowEnvironment(ShowEnvironment_iosxe):
    """Parser for show environment"""
    pass


class ShowModule(ShowModule_iosxe):
    """Parser for show module"""
    pass


class ShowSwitch(ShowSwitch_iosxe):
    """Parser for show switch"""
    pass


class ShowSwitchDetail(ShowSwitchDetail_iosxe):
    """Parser for show switch detail"""
    pass
