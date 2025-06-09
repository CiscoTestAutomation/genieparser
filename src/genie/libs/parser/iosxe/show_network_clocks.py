# Copyright (c) 2024 by Cisco Systems, Inc.
# All rights reserved.
'''  show_network_clocks.py

IOSXE parsers for the following show commands:
    * 'show network-clocks synchronization detail'
    * 'show network-clocks synchronization'
    * 'show network-clocks synchronization global detail'
    * 'show network-clocks synchronization global'
    * 'show network-clocks synchronization interface {interface}'
    * 'show network-clocks synchronization t0 detail'
    * 'show network-clocks synchronization t0'
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.libs.parser.utils.common import Common
from genie.metaparser.util.schemaengine import Any, Optional


class ShowNetworkClocksSynchronizationDetailSchema(MetaParser):
    ''' Schema for:
        * 'show network-clocks synchronization detail'
    '''

    schema = {
        'automatic_selection_process': str,
        'equipment_clock': str,
        'clock_state': str,
        'clock_mode': str,
        'esmc_state': str,
        'ssm_option': str,
        Optional('t0'): str,
        'global_hold_off_time': int,
        'global_wait_to_restore': int,
        'tsm_delay': int,
        'revertive': str,
        'nominated_interfaces': {
            Any(): {
                Optional('is_source'): bool,
                Optional('source_type'): str,
                'sigtype': str,
                'mode_or_ql': str,
                'prio': str,
                'ql_in': str,
                'esmc_tx': str,
                'esmc_rx': str
            },
        },
        Optional('force_switch'): str,
        Optional('manual_switch'): str,
        'num_of_sync_sources': int,
        'squelch_threshold': str,
        Optional('last_transition_recorded'): str,
        'local_interfaces': {
            Any(): {
                'signal_type': str,
                'mode': str,
                Optional('ssm_tx'): str,
                Optional('ssm_rx'): str,
                Optional('esmc_tx'): str,
                Optional('esmc_rx'): str,
                'priority': str,
                'ql_receive': str,
                'ql_receive_configured': str,
                'ql_receive_overrided': str,
                'ql_transmit': str,
                'ql_transmit_configured': str,
                'hold_off_time': int,
                'wait_to_restore': int,
                'lock_out': str,
                'signal_fail': str,
                'alarms': str,
                'active_alarms': str,
                'slot_disabled': str,
                'snmp_input_source_index': int,
                'snmp_parent_list_index': int,
                'description': str
            },
        },
    }


# =======================================================
# Parser for 'show network-clocks synchronization detail'
# =======================================================
class ShowNetworkClocksSynchronizationDetail(ShowNetworkClocksSynchronizationDetailSchema):
    ''' Parser for:
        * 'show network-clocks synchronization detail'
    '''
    cli_command = 'show network-clocks synchronization detail'

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)

        # Automatic selection process : Enable
        p0 = re.compile(r'^Automatic\s+selection\s+process\s*:\s*'
                        r'(?P<automatic_selection_process>.+)$')

        # Equipment Clock : 2048 (EEC-Option1)
        p1 = re.compile(r'^Equipment\s+Clock\s*:\s*'
                        r'(?P<equipment_clock>\d+\s*\(.+\))$')

        # Clock State : Frequency Locked
        p2 = re.compile(r'^Clock\s+State\s*:\s*'
                        r'(?P<clock_state>.+)$')

        # Clock Mode : QL-Enable
        p3 = re.compile(r'^Clock\s+Mode\s*:\s*'
                        r'(?P<clock_mode>.+)$')

        # ESMC : Enabled
        p4 = re.compile(r'^ESMC\s*:\s*'
                        r'(?P<esmc_state>.+)$')

        # SSM Option : 1
        # SSM Option : GEN1
        p5 = re.compile(r'^SSM\s+Option\s*:\s*'
                        r'(?P<ssm_option>.+)$')

        # T0 : Internal
        # T0 : GigabitEthernet0/0/2
        p6 = re.compile(r'^T0\s*:\s*'
                        r'(?P<t0>.+)$')

        # Hold-off (global) : 300 ms
        p7 = re.compile(r'^Hold-off\s+\(global\)\s*:\s*'
                        r'(?P<global_hold_off_time>\d+)\s*ms$')

        # Wait-to-restore (global) : 10 sec
        p8 = re.compile(r'^Wait-to-restore\s+\(global\)\s*:\s*'
                        r'(?P<global_wait_to_restore>\d+)\s*sec$')

        # Tsm Delay : 180 ms
        p9 = re.compile(r'^Tsm\s+Delay\s*:\s*'
                        r'(?P<tsm_delay>\d+)\s*ms$')

        # Revertive : No
        p10 = re.compile(r'^Revertive\s*:\s*'
                         r'(?P<revertive>.+)$')

        # Force Switch: FALSE
        p11 = re.compile(r'^Force\s+Switch\s*:\s*'
                         r'(?P<force_switch>.+)$')

        # Manual Switch: FALSE
        p12 = re.compile(r'^Manual\s+Switch\s*:\s*'
                         r'(?P<manual_switch>.+)$')

        # Number of synchronization sources: 4
        p13 = re.compile(r'^Number\s+of\s+synchronization\s+sources\s*:\s*'
                         r'(?P<num_of_sync_sources>\d+)$')

        # Squelch Threshold: QL-SEC
        p14 = re.compile(r'^Squelch\s+Threshold\s*:\s*'
                         r'(?P<squelch_threshold>.+)$')

        # Last transition recorded: (begin)-> 2A (ql_mode_enable)-> 1A
        p15 = re.compile(r'^Last\s+transition\s+recorded\s*:\s*'
                         r'(?P<last_transition_recorded>.+)$')

        #  Interface            SigType     Mode/QL      Prio  QL_IN  ESMC Tx  ESMC Rx
        #  Internal             NA          NA/Dis       251   QL-SEC    NA        NA
        # *Gi0/0/2              NA          Sync/En      1     QL-SEC    -         -
        p39 = re.compile(r'(?P<nominated_interface>\S+) +(?P<sigtype>\S+) +(?P<mode_or_ql>\S+/\S+) +(?P<prio>\d+) +'
                         r'(?P<ql_in>\S+) +(?P<esmc_tx>\S+) +(?P<esmc_rx>\S+)$')

        # Local Interface: Internal
        # Local Interface: Gi0/0/2
        p16 = re.compile(r'^Local\s+Interface\s*:\s*'
                         r'(?P<local_interface>.+)$')

        # Signal Type: NA
        p17 = re.compile(r'^Signal\s+Type\s*:\s*'
                         r'(?P<signal_type>.+)$')

        # Mode: NA(Ql-enabled)
        p18 = re.compile(r'^Mode\s*:\s*'
                         r'(?P<mode>.+)$')

        # SSM Tx: DISABLED
        p19 = re.compile(r'^SSM\s+Tx\s*:\s*'
                         r'(?P<ssm_tx>.+)$')

        # SSM Rx: DISABLED
        p20 = re.compile(r'^SSM\s+Rx\s*:\s*'
                         r'(?P<ssm_rx>.+)$')

        # ESMC Tx: ENABLED
        p21 = re.compile(r'^ESMC\s+Tx\s*:\s*'
                         r'(?P<esmc_tx>.+)$')

        # ESMC Rx: ENABLED
        p22 = re.compile(r'^ESMC\s+Rx\s*:\s*'
                         r'(?P<esmc_rx>.+)$')

        # Priority: 1
        p23 = re.compile(r'^Priority\s*:\s*'
                         r'(?P<priority>.+)$')

        # QL Receive: QL-SEC
        p24 = re.compile(r'^QL\s+Receive\s*:\s*'
                         r'(?P<ql_receive>.+)$')

        # QL Receive Configured: -
        p25 = re.compile(r'^QL\s+Receive\s+Configured\s*:\s*'
                         r'(?P<ql_receive_configured>.+)$')

        # QL Receive Overrided: -
        p26 = re.compile(r'^QL\s+Receive\s+Overrided\s*:\s*'
                         r'(?P<ql_receive_overrided>.+)$')

        # QL Transmit: QL-DNU
        p27 = re.compile(r'^QL\s+Transmit\s*:\s*'
                         r'(?P<ql_transmit>.+)$')

        # QL Transmit Configured: -
        p28 = re.compile(r'^QL\s+Transmit\s+Configured\s*:\s*'
                         r'(?P<ql_transmit_configured>.+)$')

        # Hold-off: 300
        p29 = re.compile(r'^Hold-off\s*:\s*'
                         r'(?P<hold_off_time>\d+)$')

        # Wait-to-restore: 10
        p30 = re.compile(r'^Wait-to-restore\s*:\s*'
                         r'(?P<wait_to_restore>\d+)$')

        # Lock Out: FALSE
        p31 = re.compile(r'^Lock\s+Out\s*:\s*'
                         r'(?P<lock_out>.+)$')

        # Signal Fail: FALSE
        p32 = re.compile(r'^Signal\s+Fail\s*:\s*'
                         r'(?P<signal_fail>.+)$')

        # Alarms: FALSE
        p33 = re.compile(r'^Alarms\s*:\s*'
                         r'(?P<alarms>.+)$')

        # Active Alarms :  None
        p34 = re.compile(r'^Active\s+Alarms\s*:\s*'
                         r'(?P<active_alarms>.+)$')

        # Slot Disabled: FALSE
        p35 = re.compile(r'^Slot\s+Disabled\s*:\s*'
                         r'(?P<slot_disabled>.+)$')

        # SNMP input source index: 2
        p36 = re.compile(r'^SNMP\s+input\s+source\s+index\s*:\s*'
                         r'(?P<snmp_input_source_index>\d+)$')

        # SNMP parent list index: 0
        p37 = re.compile(r'^SNMP\s+parent\s+list\s+index\s*:\s*'
                         r'(?P<snmp_parent_list_index>\d+)$')

        # Description: None
        p38 = re.compile(r'^Description\s*:\s*'
                         r'(?P<description>.+)$')

        # Init vars
        parsed_dict = {}
        interface_dict = {}
        nominated_interface_dict = {}
        for line in output.splitlines():
            line = line.strip()

            # Automatic selection process : Enable
            m = p0.match(line)
            if m:
                parsed_dict['automatic_selection_process'] = \
                    m.groupdict()['automatic_selection_process']
                continue

            # Equipment Clock : 2048 (EEC-Option1)
            m = p1.match(line)
            if m:
                parsed_dict['equipment_clock'] = \
                    m.groupdict()['equipment_clock']
                continue

            # Clock State : Frequency Locked
            m = p2.match(line)
            if m:
                parsed_dict['clock_state'] = \
                    m.groupdict()['clock_state']
                continue

            # Clock Mode : QL-Enable
            m = p3.match(line)
            if m:
                parsed_dict['clock_mode'] = \
                    m.groupdict()['clock_mode']
                continue

            # ESMC : Enabled
            m = p4.match(line)
            if m:
                parsed_dict['esmc_state'] = \
                    m.groupdict()['esmc_state']
                continue

            # SSM Option : 1
            # SSM Option : GEN1
            m = p5.match(line)
            if m:
                parsed_dict['ssm_option'] = \
                    m.groupdict()['ssm_option']
                continue

            # T0 : Internal
            # T0 : GigabitEthernet0/0/2
            m = p6.match(line)
            if m:
                intf = m.groupdict()['t0']
                # convert interface name to long name
                if intf.lower() != 'internal':
                    intf = \
                        Common.convert_intf_name(intf)
                parsed_dict['t0'] = intf
                continue

            # Hold-off (global) : 300 ms
            m = p7.match(line)
            if m:
                parsed_dict['global_hold_off_time'] = \
                    int(m.groupdict()['global_hold_off_time'])
                continue

            # Wait-to-restore (global) : 10 sec
            m = p8.match(line)
            if m:
                parsed_dict['global_wait_to_restore'] = \
                    int(m.groupdict()['global_wait_to_restore'])
                continue

            # Tsm Delay : 180 ms
            m = p9.match(line)
            if m:
                parsed_dict['tsm_delay'] = \
                    int(m.groupdict()['tsm_delay'])
                continue

            # Revertive : No
            m = p10.match(line)
            if m:
                parsed_dict['revertive'] = m.groupdict()['revertive']
                continue

            # Force Switch: FALSE
            m = p11.match(line)
            if m:
                parsed_dict['force_switch'] = m.groupdict()['force_switch']
                continue

            # Manual Switch: FALSE
            m = p12.match(line)
            if m:
                parsed_dict['manual_switch'] = \
                    m.groupdict()['manual_switch']
                continue

            # Number of synchronization sources: 4
            m = p13.match(line)
            if m:
                parsed_dict['num_of_sync_sources'] = \
                    int(m.groupdict()['num_of_sync_sources'])
                continue

            # Squelch Threshold: QL-SEC
            m = p14.match(line)
            if m:
                parsed_dict['squelch_threshold'] = \
                    m.groupdict()['squelch_threshold']
                continue

            # Last transition recorded: (begin)-> 2A (ql_mode_enable)-> 1A
            m = p15.match(line)
            if m:
                parsed_dict['last_transition_recorded'] = \
                    m.groupdict()['last_transition_recorded']
                continue

            #  Internal             NA          NA/Dis       251   QL-SEC    NA        NA
            # *Gi0/0/2              NA          Sync/En      1     QL-SEC    -         -
            #  Gi0/0/6              NA          Sync/En      2     QL-SEC    -         -
            m = p39.match(line)
            if m:
                nominated_interface = m.groupdict()['nominated_interface']
                interface_name = nominated_interface.replace('*', '').replace('#', '').replace('&', '')
                if interface_name.lower() != 'internal':
                    interface_name = Common.convert_intf_name(interface_name)
                nominated_interface_dict = parsed_dict.setdefault('nominated_interfaces', {}). \
                    setdefault(interface_name, {})
                if '*' in nominated_interface or '#' in nominated_interface or '&' in nominated_interface:
                    nominated_interface_dict['is_source'] = True
                    interface_dict['is_source'] = True
                    if '*' in nominated_interface:
                        nominated_interface_dict['source_type'] = 'Synchronization source selected'
                    elif '#' in nominated_interface:
                        nominated_interface_dict['source_type'] = 'Synchronization source force selected'
                    elif '&' in nominated_interface:
                        nominated_interface_dict['source_type'] = 'Synchronization source manually switched'
                else:
                    nominated_interface_dict['is_source'] = False
                nominated_interface_dict['sigtype'] = m.groupdict()['sigtype']
                nominated_interface_dict['mode_or_ql'] = m.groupdict()['mode_or_ql']
                nominated_interface_dict['prio'] = m.groupdict()['prio']
                nominated_interface_dict['ql_in'] = m.groupdict()['ql_in']
                nominated_interface_dict['esmc_tx'] = m.groupdict()['esmc_tx']
                nominated_interface_dict['esmc_rx'] = m.groupdict()['esmc_rx']
                continue

            # Local Interface: Internal
            # Local Interface: Gi0/0/2
            m = p16.match(line)
            if m:
                local_interface = m.groupdict()['local_interface']
                if local_interface.lower() != 'internal':
                    local_interface = Common.convert_intf_name(local_interface)
                interface_dict = parsed_dict.setdefault('local_interfaces', {}).setdefault(local_interface, {})
                continue

            # Signal Type: NA
            m = p17.match(line)
            if m:
                interface_dict['signal_type'] = m.groupdict()['signal_type']
                continue

            # Mode: NA(Ql-enabled)
            m = p18.match(line)
            if m:
                interface_dict['mode'] = m.groupdict()['mode']
                continue

            # SSM Tx: DISABLED
            m = p19.match(line)
            if m:
                interface_dict['ssm_tx'] = m.groupdict()['ssm_tx']
                continue

            # SSM Rx: DISABLED
            m = p20.match(line)
            if m:
                interface_dict['ssm_rx'] = m.groupdict()['ssm_rx']
                continue

            # ESMC Tx: ENABLED
            m = p21.match(line)
            if m:
                interface_dict['esmc_tx'] = m.groupdict()['esmc_tx']
                continue

            # ESMC Rx: ENABLED
            m = p22.match(line)
            if m:
                interface_dict['esmc_rx'] = m.groupdict()['esmc_rx']
                continue

            # Priority: 1
            m = p23.match(line)
            if m:
                interface_dict['priority'] = m.groupdict()['priority']
                continue

            # QL Receive: QL-SEC
            m = p24.match(line)
            if m:
                interface_dict['ql_receive'] = m.groupdict()['ql_receive']
                continue

            # QL Receive Configured: -
            m = p25.match(line)
            if m:
                interface_dict['ql_receive_configured'] = m.groupdict()['ql_receive_configured']
                continue

            # QL Receive Overrided: -
            m = p26.match(line)
            if m:
                interface_dict['ql_receive_overrided'] = m.groupdict()['ql_receive_overrided']
                continue

            # QL Transmit: QL-DNU
            m = p27.match(line)
            if m:
                interface_dict['ql_transmit'] = m.groupdict()['ql_transmit']
                continue

            # QL Transmit Configured: -
            m = p28.match(line)
            if m:
                interface_dict['ql_transmit_configured'] = m.groupdict()['ql_transmit_configured']
                continue

            # Hold-off: 300
            m = p29.match(line)
            if m:
                interface_dict['hold_off_time'] = int(m.groupdict()['hold_off_time'])
                continue

            # Wait-to-restore: 10
            m = p30.match(line)
            if m:
                interface_dict['wait_to_restore'] = int(m.groupdict()['wait_to_restore'])
                continue

            # Lock Out: FALSE
            m = p31.match(line)
            if m:
                interface_dict['lock_out'] = m.groupdict()['lock_out']
                continue

            # Signal Fail: FALSE
            m = p32.match(line)
            if m:
                interface_dict['signal_fail'] = m.groupdict()['signal_fail']
                continue

            # Alarms: FALSE
            m = p33.match(line)
            if m:
                interface_dict['alarms'] = m.groupdict()['alarms']
                continue

            # Active Alarms :  None
            m = p34.match(line)
            if m:
                interface_dict['active_alarms'] = m.groupdict()['active_alarms']
                continue

            # Slot Disabled: FALSE
            m = p35.match(line)
            if m:
                interface_dict['slot_disabled'] = m.groupdict()['slot_disabled']
                continue

            # SNMP input source index: 2
            m = p36.match(line)
            if m:
                interface_dict['snmp_input_source_index'] = int(m.groupdict()['snmp_input_source_index'])
                continue

            # SNMP parent list index: 0
            m = p37.match(line)
            if m:
                interface_dict['snmp_parent_list_index'] = int(m.groupdict()['snmp_parent_list_index'])
                continue

            # Description: None
            m = p38.match(line)
            if m:
                interface_dict['description'] = m.groupdict()['description']
                continue

        return parsed_dict


class ShowNetworkClocksSynchronizationSchema(MetaParser):
    ''' Schema for:
        * 'show network-clocks synchronization'
    '''

    schema = {
        'automatic_selection_process': str,
        'equipment_clock': str,
        'clock_mode': str,
        'esmc_state': str,
        'ssm_option': str,
        Optional('t0'): str,
        'global_hold_off_time': int,
        'global_wait_to_restore': int,
        'tsm_delay': int,
        'revertive': str,
        'nominated_interfaces': {
            Any(): {
                Optional('is_source'): bool,
                Optional('source_type'): str,
                'signal_type': str,
                'mode': str,
                'priority': int,
                'ql_in': str,
                'esmc_tx': str,
                'esmc_rx': str
            },
        },
    }


# ===============================================
# Parser for 'show network-clocks synchronization'
# ===============================================
class ShowNetworkClocksSynchronization(ShowNetworkClocksSynchronizationSchema):
    ''' Parser for:
        * 'show network-clocks synchronization'
    '''
    cli_command = 'show network-clocks synchronization'

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)

        # Automatic selection process : Enable
        p0 = re.compile(r'^Automatic\s+selection\s+process\s*:\s*'
                        r'(?P<automatic_selection_process>.+)$')

        # Equipment Clock : 2048 (EEC-Option1)
        p1 = re.compile(r'^Equipment\s+Clock\s*:\s*'
                        r'(?P<equipment_clock>\d+\s*\(.+\))$')

        # Clock Mode : QL-Enable
        p2 = re.compile(r'^Clock\s+Mode\s*:\s*'
                        r'(?P<clock_mode>.+)$')

        # ESMC : Enabled
        p3 = re.compile(r'^ESMC\s*:\s*'
                        r'(?P<esmc_state>.+)$')

        # SSM Option : 1
        # SSM Option : GEN1
        p4 = re.compile(r'^SSM\s+Option\s*:\s*'
                        r'(?P<ssm_option>.+)$')

        # T0 : Internal
        # T0 : GigabitEthernet0/0/2
        p5 = re.compile(r'^T0\s*:\s*'
                        r'(?P<t0>.+)$')

        # Hold-off (global) : 300 ms
        p6 = re.compile(r'^Hold-off\s+\(global\)\s*:\s*'
                        r'(?P<global_hold_off_time>\d+)\s*ms$')

        # Wait-to-restore (global) : 10 sec
        p7 = re.compile(r'^Wait-to-restore\s+\(global\)\s*:\s*'
                        r'(?P<global_wait_to_restore>\d+)\s*sec$')

        # Tsm Delay : 180 ms
        p8 = re.compile(r'^Tsm\s+Delay\s*:\s*'
                        r'(?P<tsm_delay>\d+)\s*ms$')

        # Revertive : No
        p9 = re.compile(r'^Revertive\s*:\s*'
                        r'(?P<revertive>.+)$')

        #  Internal             NA          NA/Dis       251   QL-SEC    NA        NA
        # *Gi0/0/2              NA          Sync/En      1     QL-SEC    -         -
        p10 = re.compile(r'(?P<local_interface>\S+) +'
                         r'(?P<signal_type>\S+) +'
                         r'(?P<mode>\S+/\S+) +(?P<priority>\d+) +'
                         r'(?P<ql_in>\S+) +'
                         r'(?P<esmc_tx>\S+) +'
                         r'(?P<esmc_rx>\S+)$')

        # Init vars
        parsed_dict = {}
        interface_dict = {}
        for line in output.splitlines():
            line = line.strip()

            # Automatic selection process : Enable
            m = p0.match(line)
            if m:
                parsed_dict['automatic_selection_process'] = \
                    m.groupdict()['automatic_selection_process']
                continue

            # Equipment Clock : 2048 (EEC-Option1)
            m = p1.match(line)
            if m:
                parsed_dict['equipment_clock'] = \
                    m.groupdict()['equipment_clock']
                continue

            # Clock Mode : QL-Enable
            m = p2.match(line)
            if m:
                parsed_dict['clock_mode'] = \
                    m.groupdict()['clock_mode']
                continue

            # ESMC : Enabled
            m = p3.match(line)
            if m:
                parsed_dict['esmc_state'] = \
                    m.groupdict()['esmc_state']
                continue

            # SSM Option : 1
            # SSM Option : GEN1
            m = p4.match(line)
            if m:
                parsed_dict['ssm_option'] = \
                    m.groupdict()['ssm_option']
                continue

            # T0 : Internal
            # T0 : GigabitEthernet0/0/2
            m = p5.match(line)
            if m:
                intf = m.groupdict()['t0']
                # convert interface name to long name
                if intf.lower() != 'internal':
                    intf = \
                        Common.convert_intf_name(intf)
                parsed_dict['t0'] = intf
                continue

            # Hold-off (global) : 300 ms
            m = p6.match(line)
            if m:
                parsed_dict['global_hold_off_time'] = \
                    int(m.groupdict()['global_hold_off_time'])
                continue

            # Wait-to-restore (global) : 10 sec
            m = p7.match(line)
            if m:
                parsed_dict['global_wait_to_restore'] = \
                    int(m.groupdict()['global_wait_to_restore'])
                continue

            # Tsm Delay : 180 ms
            m = p8.match(line)
            if m:
                parsed_dict['tsm_delay'] = \
                    int(m.groupdict()['tsm_delay'])
                continue

            # Revertive : No
            m = p9.match(line)
            if m:
                parsed_dict['revertive'] = \
                    m.groupdict()['revertive']

            #  Internal             NA          NA/Dis       251   QL-SEC    NA        NA
            # *Gi0/0/2              NA          Sync/En      1     QL-SEC    -         -
            #  Gi0/0/6              NA          Sync/En      2     QL-SEC    -         -
            m = p10.match(line)
            if m:
                local_interface = m.groupdict()['local_interface']
                interface_name = local_interface.replace('*', '').replace('#', '').replace('&', '')
                if interface_name.lower() != 'internal':
                    interface_name = Common.convert_intf_name(interface_name)
                interface_dict = parsed_dict.setdefault('nominated_interfaces', {}).setdefault(interface_name, {})
                if '*' in local_interface or '#' in local_interface or '&' in local_interface:
                    interface_dict['is_source'] = True
                    if '*' in local_interface:
                        interface_dict['source_type'] = 'Synchronization source selected'
                    elif '#' in local_interface:
                        interface_dict['source_type'] = 'Synchronization source force selected'
                    elif '&' in local_interface:
                        interface_dict['source_type'] = 'Synchronization source manually switched'
                else:
                    interface_dict['is_source'] = False
                interface_dict['signal_type'] = m.groupdict()['signal_type']
                interface_dict['mode'] = m.groupdict()['mode']
                interface_dict['priority'] = int(m.groupdict()['priority'])
                interface_dict['ql_in'] = m.groupdict()['ql_in']
                interface_dict['esmc_tx'] = m.groupdict()['esmc_tx']
                interface_dict['esmc_rx'] = m.groupdict()['esmc_rx']
                continue

        return parsed_dict


class ShowNetworkClocksSynchronizationGlobalDetailSchema(MetaParser):
    ''' Schema for:
        * 'show network-clocks synchronization global detail'
    '''

    schema = {
        'automatic_selection_process': str,
        'equipment_clock': str,
        'clock_state': str,
        'clock_mode': str,
        'esmc_state': str,
        'ssm_option': str,
        Optional('t0'): str,
        'global_hold_off_time': int,
        'global_wait_to_restore': int,
        'tsm_delay': int,
        'revertive': str,
        Optional('force_switch'): str,
        Optional('manual_switch'): str,
        'num_of_sync_sources': int,
        'squelch_threshold': str,
        Optional('last_transition_recorded'): str
    }


# =============================================================
# Parser for 'show network-clocks synchronization global detail'
# =============================================================
class ShowNetworkClocksSynchronizationGlobalDetail(ShowNetworkClocksSynchronizationGlobalDetailSchema):
    ''' Parser for:
        * 'show network-clocks synchronization global detail'
    '''
    cli_command = 'show network-clocks synchronization global detail'

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)

        # Automatic selection process : Enable
        p0 = re.compile(r'^Automatic\s+selection\s+process\s*:\s*'
                        r'(?P<automatic_selection_process>.+)$')

        # Equipment Clock : 2048 (EEC-Option1)
        p1 = re.compile(r'^Equipment\s+Clock\s*:\s*'
                        r'(?P<equipment_clock>\d+\s*\(.+\))$')

        # Clock State : Frequency Locked
        p2 = re.compile(r'^Clock\s+State\s*:\s*'
                        r'(?P<clock_state>.+)$')

        # Clock Mode : QL-Enable
        p3 = re.compile(r'^Clock\s+Mode\s*:\s*'
                        r'(?P<clock_mode>.+)$')

        # ESMC : Enabled
        p4 = re.compile(r'^ESMC\s*:\s*'
                        r'(?P<esmc_state>.+)$')

        # SSM Option : 1
        # SSM Option : GEN1
        p5 = re.compile(r'^SSM\s+Option\s*:\s*'
                        r'(?P<ssm_option>.+)$')

        # T0 : Internal
        # T0 : GigabitEthernet0/0/2
        p6 = re.compile(r'^T0\s*:\s*'
                        r'(?P<t0>.+)$')

        # Hold-off (global) : 300 ms
        p7 = re.compile(r'^Hold-off\s+\(global\)\s*:\s*'
                        r'(?P<global_hold_off_time>\d+)\s*ms$')

        # Wait-to-restore (global) : 10 sec
        p8 = re.compile(r'^Wait-to-restore\s+\(global\)\s*:\s*'
                        r'(?P<global_wait_to_restore>\d+)\s*sec$')

        # Tsm Delay : 180 ms
        p9 = re.compile(r'^Tsm\s+Delay\s*:\s*'
                        r'(?P<tsm_delay>\d+)\s*ms$')

        # Revertive : No
        p10 = re.compile(r'^Revertive\s*:\s*'
                         r'(?P<revertive>.+)$')

        # Force Switch: FALSE
        p11 = re.compile(r'^Force\s+Switch\s*:\s*'
                         r'(?P<force_switch>.+)$')

        # Manual Switch: FALSE
        p12 = re.compile(r'^Manual\s+Switch\s*:\s*'
                         r'(?P<manual_switch>.+)$')

        # Number of synchronization sources: 4
        p13 = re.compile(r'^Number\s+of\s+synchronization\s+sources\s*:\s*'
                         r'(?P<num_of_sync_sources>\d+)$')

        # Squelch Threshold: QL-SEC
        p14 = re.compile(r'^Squelch\s+Threshold\s*:\s*'
                         r'(?P<squelch_threshold>.+)$')

        # Last transition recorded: (begin)-> 2A (ql_mode_enable)-> 1A
        p15 = re.compile(r'^Last\s+transition\s+recorded\s*:\s*'
                         r'(?P<last_transition_recorded>.+)$')

        # Init vars
        parsed_dict = {}
        for line in output.splitlines():
            line = line.strip()

            # Automatic selection process : Enable
            m = p0.match(line)
            if m:
                parsed_dict['automatic_selection_process'] = \
                    m.groupdict()['automatic_selection_process']
                continue

            # Equipment Clock : 2048 (EEC-Option1)
            m = p1.match(line)
            if m:
                parsed_dict['equipment_clock'] = \
                    m.groupdict()['equipment_clock']
                continue

            # Clock State : Frequency Locked
            m = p2.match(line)
            if m:
                parsed_dict['clock_state'] = \
                    m.groupdict()['clock_state']
                continue

            # Clock Mode : QL-Enable
            m = p3.match(line)
            if m:
                parsed_dict['clock_mode'] = \
                    m.groupdict()['clock_mode']
                continue

            # ESMC : Enabled
            m = p4.match(line)
            if m:
                parsed_dict['esmc_state'] = \
                    m.groupdict()['esmc_state']
                continue

            # SSM Option : 1
            # SSM Option : GEN1
            m = p5.match(line)
            if m:
                parsed_dict['ssm_option'] = \
                    m.groupdict()['ssm_option']
                continue

            # T0 : Internal
            # T0 : GigabitEthernet0/0/2
            m = p6.match(line)
            if m:
                intf = m.groupdict()['t0']
                # convert interface name to long name
                if intf.lower() != 'internal':
                    intf = \
                        Common.convert_intf_name(intf)
                parsed_dict['t0'] = intf
                continue

            # Hold-off (global) : 300 ms
            m = p7.match(line)
            if m:
                parsed_dict['global_hold_off_time'] = \
                    int(m.groupdict()['global_hold_off_time'])
                continue

            # Wait-to-restore (global) : 10 sec
            m = p8.match(line)
            if m:
                parsed_dict['global_wait_to_restore'] = \
                    int(m.groupdict()['global_wait_to_restore'])
                continue

            # Tsm Delay : 180 ms
            m = p9.match(line)
            if m:
                parsed_dict['tsm_delay'] = \
                    int(m.groupdict()['tsm_delay'])
                continue

            # Revertive : No
            m = p10.match(line)
            if m:
                parsed_dict['revertive'] = \
                    m.groupdict()['revertive']
                continue

            # Force Switch: FALSE
            m = p11.match(line)
            if m:
                parsed_dict['force_switch'] = \
                    m.groupdict()['force_switch']
                continue

            # Manual Switch: FALSE
            m = p12.match(line)
            if m:
                parsed_dict['manual_switch'] = \
                    m.groupdict()['manual_switch']
                continue

            # Number of synchronization sources: 4
            m = p13.match(line)
            if m:
                parsed_dict['num_of_sync_sources'] = \
                    int(m.groupdict()['num_of_sync_sources'])
                continue

            # Squelch Threshold: QL-SEC
            m = p14.match(line)
            if m:
                parsed_dict['squelch_threshold'] = \
                    m.groupdict()['squelch_threshold']
                continue

            # Last transition recorded: (begin)-> 2A (ql_mode_enable)-> 1A
            m = p15.match(line)
            if m:
                parsed_dict['last_transition_recorded'] = \
                    m.groupdict()['last_transition_recorded']
                continue

        return parsed_dict


class ShowNetworkClocksSynchronizationGlobalSchema(MetaParser):
    ''' Schema for:
        * 'show network-clocks synchronization global'
    '''

    schema = {
        'automatic_selection_process': str,
        'equipment_clock': str,
        'clock_mode': str,
        'esmc_state': str,
        'ssm_option': str,
        Optional('t0'): str,
        'global_hold_off_time': int,
        'global_wait_to_restore': int,
        'tsm_delay': int,
        'revertive': str,
    }


# ======================================================
# Parser for 'show network-clocks synchronization global'
# ======================================================
class ShowNetworkClocksSynchronizationGlobal(ShowNetworkClocksSynchronizationGlobalSchema):
    ''' Parser for:
        * 'show network-clocks synchronization global'
    '''
    cli_command = 'show network-clocks synchronization global'

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)

        # Automatic selection process : Enable
        p0 = re.compile(r'^Automatic\s+selection\s+process\s*:\s*'
                        r'(?P<automatic_selection_process>.+)$')

        # Equipment Clock : 2048 (EEC-Option1)
        p1 = re.compile(r'^Equipment\s+Clock\s*:\s*'
                        r'(?P<equipment_clock>\d+\s*\(.+\))$')

        # Clock Mode : QL-Enable
        p2 = re.compile(r'^Clock\s+Mode\s*:\s*'
                        r'(?P<clock_mode>.+)$')

        # ESMC : Enabled
        p3 = re.compile(r'^ESMC\s*:\s*'
                        r'(?P<esmc_state>.+)$')

        # SSM Option : 1
        # SSM Option : GEN1
        p4 = re.compile(r'^SSM\s+Option\s*:\s*'
                        r'(?P<ssm_option>.+)$')

        # T0 : Internal
        # T0 : GigabitEthernet0/0/2
        p5 = re.compile(r'^T0\s*:\s*'
                        r'(?P<t0>.+)$')

        # Hold-off (global) : 300 ms
        p6 = re.compile(r'^Hold-off\s+\(global\)\s*:\s*'
                        r'(?P<global_hold_off_time>\d+)\s*ms$')

        # Wait-to-restore (global) : 10 sec
        p7 = re.compile(r'^Wait-to-restore\s+\(global\)\s*:\s*'
                        r'(?P<global_wait_to_restore>\d+)\s*sec$')

        # Tsm Delay : 180 ms
        p8 = re.compile(r'^Tsm\s+Delay\s*:\s*'
                        r'(?P<tsm_delay>\d+)\s*ms$')

        # Revertive : No
        p9 = re.compile(r'^Revertive\s*:\s*'
                        r'(?P<revertive>.+)$')

        # Init vars
        parsed_dict = {}
        for line in output.splitlines():
            line = line.strip()

            # Automatic selection process : Enable
            m = p0.match(line)
            if m:
                parsed_dict['automatic_selection_process'] = \
                    m.groupdict()['automatic_selection_process']
                continue

            # Equipment Clock : 2048 (EEC-Option1)
            m = p1.match(line)
            if m:
                parsed_dict['equipment_clock'] = \
                    m.groupdict()['equipment_clock']
                continue

            # Clock Mode : QL-Enable
            m = p2.match(line)
            if m:
                parsed_dict['clock_mode'] = \
                    m.groupdict()['clock_mode']
                continue

            # ESMC : Enabled
            m = p3.match(line)
            if m:
                parsed_dict['esmc_state'] = \
                    m.groupdict()['esmc_state']
                continue

            # SSM Option : 1
            # SSM Option : GEN1
            m = p4.match(line)
            if m:
                parsed_dict['ssm_option'] = \
                    m.groupdict()['ssm_option']
                continue

            # T0 : Internal
            # T0 : GigabitEthernet0/0/2
            m = p5.match(line)
            if m:
                intf = m.groupdict()['t0']
                # convert interface name to long name
                if intf.lower() != 'internal':
                    intf = \
                        Common.convert_intf_name(intf)
                parsed_dict['t0'] = intf
                continue

            # Hold-off (global) : 300 ms
            m = p6.match(line)
            if m:
                parsed_dict['global_hold_off_time'] = \
                    int(m.groupdict()['global_hold_off_time'])
                continue

            # Wait-to-restore (global) : 10 sec
            m = p7.match(line)
            if m:
                parsed_dict['global_wait_to_restore'] = \
                    int(m.groupdict()['global_wait_to_restore'])
                continue

            # Tsm Delay : 180 ms
            m = p8.match(line)
            if m:
                parsed_dict['tsm_delay'] = \
                    int(m.groupdict()['tsm_delay'])
                continue

            # Revertive : No
            m = p9.match(line)
            if m:
                parsed_dict['revertive'] = \
                    m.groupdict()['revertive']

        return parsed_dict


class ShowNetworkClocksSynchronizationInterfaceSchema(MetaParser):
    ''' Schema for:
        * 'show network-clocks synchronization interface {interface}'
    '''

    schema = {
        Any(): {
            'description': str,
            'signal_type': str,
            'mode': str,
            Optional('ssm_tx'): str,
            Optional('ssm_rx'): str,
            Optional('esmc_tx'): str,
            Optional('esmc_rx'): str,
            'ql_receive': str,
            'ql_receive_configured': str,
            'ql_receive_overrided': str,
            'ql_transmit': str,
            'ql_transmit_configured': str,
            'hold_off_time': int,
            'hold_off_configured': str,
            'wait_to_restore': int,
            'wtr_configured': str,
            'lock_out': str,
            'signal_fail': str,
            'alarms': str,
            'reason_for_alarm_flag': int,
            'slot_disabled': str,
            'hold_off_timer': str,
            'wait_to_restore_timer': str,
            'switchover_timer': str,
            'esmc_tx_timer': str,
            'esmc_rx_timer': str,
            'tsm_delay_timer': str
        },
        't0': {
            'selected_source': str,
            'priority': int,
            Optional('force_switch'): str,
            Optional('manual_switch'): str,
            'manual_switch_in_progress': str,
            'not_use': str,
            'been_selected': str,
            'snmp_input_source_index': int,
            'snmp_parent_source_index': int,
            'intf_sig_nv': str
        }
    }


# ======================================================================
# Parser for 'show network-clocks synchronization interface {interface}'
# ======================================================================
class ShowNetworkClocksSynchronizationInterface(ShowNetworkClocksSynchronizationInterfaceSchema):
    ''' Parser for:
        * 'show network-clocks synchronization interface {interface}'
    '''
    cli_command = 'show network-clocks synchronization interface {interface}'

    def cli(self, interface, output=None):

        if output is None:
            output = self.device. \
                execute(self.cli_command.format(interface=interface))

        # GigabitEthernet0/0/2
        p_intf = re.compile(r'^(?P<intf>[a-zA-Z]+[\d/]*)$')

        # T0
        p_t0 = re.compile(r'^T0$')

        # Description: None
        p0 = re.compile(r'^Description\s*:\s*'
                        r'(?P<description>.+)$')

        # Signal Type: NA
        p1 = re.compile(r'^Signal\s+Type\s*:\s*'
                        r'(?P<signal_type>.+)$')

        # Mode: NA(Ql-enabled)
        p2 = re.compile(r'^Mode\s*:\s*'
                        r'(?P<mode>.+)$')

        # SSM Tx: DISABLED
        p3 = re.compile(r'^SSM\s+Tx\s*:\s*'
                        r'(?P<ssm_tx>.+)$')

        # SSM Rx: DISABLED
        p4 = re.compile(r'^SSM\s+Rx\s*:\s*'
                        r'(?P<ssm_rx>.+)$')

        # ESMC Tx: ENABLED
        p5 = re.compile(r'^ESMC\s+Tx\s*:\s*'
                        r'(?P<esmc_tx>.+)$')

        # ESMC Rx: ENABLED
        p6 = re.compile(r'^ESMC\s+Rx\s*:\s*'
                        r'(?P<esmc_rx>.+)$')

        # QL Receive: QL-SEC
        p7 = re.compile(r'^QL\s+Receive\s*:\s*'
                        r'(?P<ql_receive>.+)$')

        # QL Receive Configured: -
        p8 = re.compile(r'^QL\s+Receive\s+Configured\s*:\s*'
                        r'(?P<ql_receive_configured>.+)$')

        # QL Receive Overrided: -
        p9 = re.compile(r'^QL\s+Receive\s+Overrided\s*:\s*'
                        r'(?P<ql_receive_overrided>.+)$')

        # QL Transmit: QL-DNU
        p10 = re.compile(r'^QL\s+Transmit\s*:\s*'
                         r'(?P<ql_transmit>.+)$')

        # QL Transmit Configured: -
        p11 = re.compile(r'^QL\s+Transmit\s+Configured\s*:\s*'
                         r'(?P<ql_transmit_configured>.+)$')

        # Hold-off: 300
        p12 = re.compile(r'^Hold-off\s*:\s*'
                         r'(?P<hold_off_time>\d+)$')

        # Holdoff Configured: TRUE
        p13 = re.compile(r'^Holdoff\s+Configured\s*:\s*'
                         r'(?P<hold_off_configured>.+)$')

        # Wait-to-restore: 10
        p14 = re.compile(r'^Wait-to-restore\s*:\s*'
                         r'(?P<wait_to_restore>\d+)$')

        # WTR Configured: FALSE
        p15 = re.compile(r'^WTR\s+Configured\s*:\s*'
                         r'(?P<wtr_configured>.+)$')

        # Lock out: FALSE
        p16 = re.compile(r'^Lock\s+out\s*:\s*'
                         r'(?P<lock_out>.+)$')

        # Signal Fail: FALSE
        p17 = re.compile(r'^Signal\s+Fail\s*:\s*'
                         r'(?P<signal_fail>.+)$')

        # Alarms: FALSE
        p18 = re.compile(r'^Alarms\s*:\s*'
                         r'(?P<alarms>.+)$')

        # Reason for alarm flag: 0
        p19 = re.compile(r'^Reason\s+for\s+alarm\s+flag\s*:\s*'
                         r'(?P<reason_for_alarm_flag>\d+)$')

        # Slot Disabled: FALSE
        p20 = re.compile(r'^Slot\s+Disabled\s*:\s*'
                         r'(?P<slot_disabled>.+)$')

        # Hold off Timer: STOPPED
        p21 = re.compile(r'^Hold\s+off\s+Timer\s*:\s*'
                         r'(?P<hold_off_timer>.+)$')

        # Wait to restore Timer: STOPPED
        p22 = re.compile(r'^Wait\s+to\s+restore\s+Timer\s*:\s*'
                         r'(?P<wait_to_restore_timer>.+)$')

        # Switchover Timer: STOPPED
        p23 = re.compile(r'^Switchover\s+Timer\s*:\s*'
                         r'(?P<switchover_timer>.+)$')

        # ESMC Tx Timer: RUNNING
        p24 = re.compile(r'^ESMC\s+Tx\s+Timer\s*:\s*'
                         r'(?P<esmc_tx_timer>.+)$')

        # ESMC Rx Timer: RUNNING
        p25 = re.compile(r'^ESMC\s+Rx\s+Timer\s*:\s*'
                         r'(?P<esmc_rx_timer>.+)$')

        # Tsm delay Timer: STOPPED
        p26 = re.compile(r'^Tsm\s+delay\s+Timer\s*:\s*'
                         r'(?P<tsm_delay_timer>.+)$')

        # Selected source: TRUE
        p27 = re.compile(r'^Selected\s+source\s*:\s*'
                         r'(?P<selected_source>.+)$')

        # Priority: 1
        p28 = re.compile(r'^Priority\s*:\s*'
                         r'(?P<priority>.+)$')

        # Force Switch: FALSE
        p29 = re.compile(r'^Force\s+Switch\s*:\s*'
                         r'(?P<force_switch>.+)$')

        # Manual Switch: FALSE
        p30 = re.compile(r'^Manual\s+Switch\s*:\s*'
                         r'(?P<manual_switch>.+)$')

        # Manual Switch in progress: FALSE
        p31 = re.compile(r'^Manual\s+Switch\s+in\s+progress\s*:\s*'
                         r'(?P<manual_switch_in_progress>.+)$')
        # Don't Use: FALSE
        p32 = re.compile(r'^Don\'t\s+Use\s*:\s*'
                         r'(?P<not_use>.+)$')

        # Been Selected: TRUE
        p33 = re.compile(r'^Been\s+Selected\s*:\s*'
                         r'(?P<been_selected>.+)$')

        # SNMP input source index: 2
        p34 = re.compile(r'^SNMP\s+input\s+source\s+index\s*:\s*'
                         r'(?P<snmp_input_source_index>\d+)$')

        # SNMP parent source index: 0
        p35 = re.compile(r'^SNMP\s+parent\s+source\s+index\s*:\s*'
                         r'(?P<snmp_parent_source_index>\d+)$')

        # Intf_sig_nv: 0
        p36 = re.compile(r'^Intf_sig_nv\s*:\s*'
                         r'(?P<intf_sig_nv>.+)$')

        # Init vars
        parsed_dict = {}
        interface_dict = {}
        t0_dict = {}
        for line in output.splitlines():
            line = line.strip()

            m_intf = p_intf.match(line)
            m_t0 = p_t0.match(line)
            if m_intf and not m_t0:
                # convert interface name to long name
                intf = m_intf.groupdict()['intf']
                intf = \
                    Common.convert_intf_name(intf)
                interface_dict = parsed_dict.setdefault(intf, {})
            if m_t0:
                t0_dict = parsed_dict.setdefault('t0', {})

            # Description: None
            m = p0.match(line)
            if m:
                interface_dict['description'] = \
                    m.groupdict()['description']
                continue

            # Signal Type: NA
            m = p1.match(line)
            if m:
                interface_dict['signal_type'] = m.groupdict()['signal_type']
                continue

            # Mode: NA(Ql-enabled)
            m = p2.match(line)
            if m:
                interface_dict['mode'] = m.groupdict()['mode']
                continue

            # SSM Tx: DISABLED
            m = p3.match(line)
            if m:
                interface_dict['ssm_tx'] = m.groupdict()['ssm_tx']
                continue

            # SSM Rx: DISABLED
            m = p4.match(line)
            if m:
                interface_dict['ssm_rx'] = m.groupdict()['ssm_rx']
                continue

            # ESMC Tx: ENABLED
            m = p5.match(line)
            if m:
                interface_dict['esmc_tx'] = m.groupdict()['esmc_tx']
                continue

            # ESMC Rx: ENABLED
            m = p6.match(line)
            if m:
                interface_dict['esmc_rx'] = m.groupdict()['esmc_rx']
                continue

            # QL Receive: QL-SEC
            m = p7.match(line)
            if m:
                interface_dict['ql_receive'] = m.groupdict()['ql_receive']
                continue

            # QL Receive Configured: -
            m = p8.match(line)
            if m:
                interface_dict['ql_receive_configured'] = \
                    m.groupdict()['ql_receive_configured']
                continue

            # QL Receive Overrided: -
            m = p9.match(line)
            if m:
                interface_dict['ql_receive_overrided'] = \
                    m.groupdict()['ql_receive_overrided']
                continue

            # QL Transmit: QL-DNU
            m = p10.match(line)
            if m:
                interface_dict['ql_transmit'] = \
                    m.groupdict()['ql_transmit']
                continue

            # QL Transmit Configured: -
            m = p11.match(line)
            if m:
                interface_dict['ql_transmit_configured'] = \
                    m.groupdict()['ql_transmit_configured']
                continue

            # Hold-off: 300
            m = p12.match(line)
            if m:
                interface_dict['hold_off_time'] = \
                    int(m.groupdict()['hold_off_time'])

            # Holdoff Configured: TRUE
            m = p13.match(line)
            if m:
                interface_dict['hold_off_configured'] = \
                    m.groupdict()['hold_off_configured']
                continue

            # Wait-to-restore: 10
            m = p14.match(line)
            if m:
                interface_dict['wait_to_restore'] = \
                    int(m.groupdict()['wait_to_restore'])
                continue

            # WTR Configured: FALSE
            m = p15.match(line)
            if m:
                interface_dict['wtr_configured'] = \
                    m.groupdict()['wtr_configured']
                continue

            # Lock Out: FALSE
            m = p16.match(line)
            if m:
                interface_dict['lock_out'] = \
                    m.groupdict()['lock_out']
                continue

            # Signal Fail: FALSE
            m = p17.match(line)
            if m:
                interface_dict['signal_fail'] = \
                    m.groupdict()['signal_fail']
                continue

            # Alarms: FALSE
            m = p18.match(line)
            if m:
                interface_dict['alarms'] = \
                    m.groupdict()['alarms']
                continue

            # Reason for alarm flag: 0
            m = p19.match(line)
            if m:
                interface_dict['reason_for_alarm_flag'] = \
                    int(m.groupdict()['reason_for_alarm_flag'])
                continue

            # Slot Disabled: FALSE
            m = p20.match(line)
            if m:
                interface_dict['slot_disabled'] = \
                    m.groupdict()['slot_disabled']
                continue

            # Hold off Timer: STOPPED
            m = p21.match(line)
            if m:
                interface_dict['hold_off_timer'] = \
                    m.groupdict()['hold_off_timer']
                continue

            # Wait to restore Timer: STOPPED
            m = p22.match(line)
            if m:
                interface_dict['wait_to_restore_timer'] = \
                    m.groupdict()['wait_to_restore_timer']
                continue

            # Switchover Timer: STOPPED
            m = p23.match(line)
            if m:
                interface_dict['switchover_timer'] = \
                    m.groupdict()['switchover_timer']
                continue

            # ESMC Tx Timer: RUNNING
            m = p24.match(line)
            if m:
                interface_dict['esmc_tx_timer'] = \
                    m.groupdict()['esmc_tx_timer']
                continue

            # ESMC Rx Timer: RUNNING
            m = p25.match(line)
            if m:
                interface_dict['esmc_rx_timer'] = \
                    m.groupdict()['esmc_rx_timer']
                continue

            # Tsm delay Timer: STOPPED
            m = p26.match(line)
            if m:
                interface_dict['tsm_delay_timer'] = \
                    m.groupdict()['tsm_delay_timer']
                continue

            # Selected source: TRUE
            m = p27.match(line)
            if m:
                t0_dict['selected_source'] = \
                    m.groupdict()['selected_source']
                continue

            # Priority: 1
            m = p28.match(line)
            if m:
                t0_dict['priority'] = int(m.groupdict()['priority'])
                continue

            # Force Switch: FALSE
            m = p29.match(line)
            if m:
                t0_dict['force_switch'] = \
                    m.groupdict()['force_switch']
                continue

            # Manual Switch: FALSE
            m = p30.match(line)
            if m:
                t0_dict['manual_switch'] = \
                    m.groupdict()['manual_switch']
                continue

            # Manual Switch in progress: FALSE
            m = p31.match(line)
            if m:
                t0_dict['manual_switch_in_progress'] = \
                    m.groupdict()['manual_switch_in_progress']
                continue

            # Don't Use: FALSE
            m = p32.match(line)
            if m:
                t0_dict['not_use'] = \
                    m.groupdict()['not_use']
                continue

            # Been Selected: TRUE
            m = p33.match(line)
            if m:
                t0_dict['been_selected'] = \
                    m.groupdict()['been_selected']
                continue

            # SNMP input source index: 2
            m = p34.match(line)
            if m:
                t0_dict['snmp_input_source_index'] = \
                    int(m.groupdict()['snmp_input_source_index'])
                continue

            # SNMP parent source index: 0
            m = p35.match(line)
            if m:
                t0_dict['snmp_parent_source_index'] = \
                    int(m.groupdict()['snmp_parent_source_index'])
                continue

            # Intf_sig_nv: 0
            m = p36.match(line)
            if m:
                t0_dict['intf_sig_nv'] = \
                    m.groupdict()['intf_sig_nv']
                continue

        return parsed_dict


class ShowNetworkClocksSynchronizationT0DetailSchema(MetaParser):
    ''' Schema for:
        * 'show network-clocks synchronization t0 detail'
    '''

    schema = {
        'automatic_selection_process': str,
        'equipment_clock': str,
        'clock_state': str,
        'clock_mode': str,
        'esmc_state': str,
        'ssm_option': str,
        Optional('t0'): str,
        'global_hold_off_time': int,
        'global_wait_to_restore': int,
        'tsm_delay': int,
        'revertive': str,
        Optional('force_switch'): str,
        Optional('manual_switch'): str,
        'num_of_sync_sources': int,
        'squelch_threshold': str,
        Optional('last_transition_recorded'): str,
        'local_interfaces': {
            Any(): {
                'description': str,
                'signal_type': str,
                'mode': str,
                Optional('ssm_tx'): str,
                Optional('ssm_rx'): str,
                Optional('esmc_tx'): str,
                Optional('esmc_rx'): str,
                'ql_receive': str,
                'ql_receive_configured': str,
                'ql_receive_overrided': str,
                'ql_transmit': str,
                'ql_transmit_configured': str
            },
        },
    }


# =========================================================
# Parser for 'show network-clocks synchronization t0 detail'
# =========================================================
class ShowNetworkClocksSynchronizationT0Detail(ShowNetworkClocksSynchronizationT0DetailSchema):
    ''' Parser for:
        * 'show network-clocks synchronization t0 detail'
    '''
    cli_command = 'show network-clocks synchronization t0 detail'

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)

        # Automatic selection process : Enable
        p0 = re.compile(r'^Automatic\s+selection\s+process\s*:\s*'
                        r'(?P<automatic_selection_process>.+)$')

        # Equipment Clock : 2048 (EEC-Option1)
        p1 = re.compile(r'^Equipment\s+Clock\s*:\s*'
                        r'(?P<equipment_clock>\d+\s*\(.+\))$')

        # Clock State : Frequency Locked
        p2 = re.compile(r'^Clock\s+State\s*:\s*'
                        r'(?P<clock_state>.+)$')

        # Clock Mode : QL-Enable
        p3 = re.compile(r'^Clock\s+Mode\s*:\s*'
                        r'(?P<clock_mode>.+)$')

        # ESMC : Enabled
        p4 = re.compile(r'^ESMC\s*:\s*'
                        r'(?P<esmc_state>.+)$')

        # SSM Option : 1
        # SSM Option : GEN1
        p5 = re.compile(r'^SSM\s+Option\s*:\s*'
                        r'(?P<ssm_option>.+)$')

        # T0 : Internal
        # T0 : GigabitEthernet0/0/2
        p6 = re.compile(r'^T0\s*:\s*'
                        r'(?P<t0>.+)$')

        # Hold-off (global) : 300 ms
        p7 = re.compile(r'^Hold-off\s+\(global\)\s*:\s*'
                        r'(?P<global_hold_off_time>\d+)\s*ms$')

        # Wait-to-restore (global) : 10 sec
        p8 = re.compile(r'^Wait-to-restore\s+\(global\)\s*:\s*'
                        r'(?P<global_wait_to_restore>\d+)\s*sec$')

        # Tsm Delay : 180 ms
        p9 = re.compile(r'^Tsm\s+Delay\s*:\s*'
                        r'(?P<tsm_delay>\d+)\s*ms$')

        # Revertive : No
        p10 = re.compile(r'^Revertive\s*:\s*'
                         r'(?P<revertive>.+)$')

        # Force Switch: FALSE
        p11 = re.compile(r'^Force\s+Switch\s*:\s*'
                         r'(?P<force_switch>.+)$')

        # Manual Switch: FALSE
        p12 = re.compile(r'^Manual\s+Switch\s*:\s*'
                         r'(?P<manual_switch>.+)$')

        # Number of synchronization sources: 4
        p13 = re.compile(r'^Number\s+of\s+synchronization\s+sources\s*:\s*'
                         r'(?P<num_of_sync_sources>\d+)$')

        # Squelch Threshold: QL-SEC
        p14 = re.compile(r'^Squelch\s+Threshold\s*:\s*'
                         r'(?P<squelch_threshold>.+)$')

        # Last transition recorded: (begin)-> 2A (ql_mode_enable)-> 1A
        p15 = re.compile(r'^Last\s+transition\s+recorded\s*:\s*'
                         r'(?P<last_transition_recorded>.+)$')

        # Internal
        # GigabitEthernet0/0/2
        p16 = re.compile(r'^(?P<local_interface>[a-zA-Z]+[\d/]*)$')

        # Description: None
        p17 = re.compile(r'^Description\s*:\s*'
                         r'(?P<description>.+)$')

        # Signal Type: NA
        p18 = re.compile(r'^Signal\s+Type\s*:\s*'
                         r'(?P<signal_type>.+)$')

        # Mode: NA(Ql-enabled)
        p19 = re.compile(r'^Mode\s*:\s*'
                         r'(?P<mode>.+)$')

        # SSM Tx: DISABLED
        p20 = re.compile(r'^SSM\s+Tx\s*:\s*'
                         r'(?P<ssm_tx>.+)$')

        # SSM Rx: DISABLED
        p21 = re.compile(r'^SSM\s+Rx\s*:\s*'
                         r'(?P<ssm_rx>.+)$')

        # ESMC Tx: ENABLED
        p22 = re.compile(r'^ESMC\s+Tx\s*:\s*'
                         r'(?P<esmc_tx>.+)$')

        # ESMC Rx: ENABLED
        p23 = re.compile(r'^ESMC\s+Rx\s*:\s*'
                         r'(?P<esmc_rx>.+)$')

        # QL Receive: QL-SEC
        p24 = re.compile(r'^QL\s+Receive\s*:\s*'
                         r'(?P<ql_receive>.+)$')

        # QL Receive Configured: -
        p25 = re.compile(r'^QL\s+Receive\s+Configured\s*:\s*'
                         r'(?P<ql_receive_configured>.+)$')

        # QL Receive Overrided: -
        p26 = re.compile(r'^QL\s+Receive\s+Overrided\s*:\s*'
                         r'(?P<ql_receive_overrided>.+)$')

        # QL Transmit: QL-DNU
        p27 = re.compile(r'^QL\s+Transmit\s*:\s*'
                         r'(?P<ql_transmit>.+)$')

        # QL Transmit Configured: -
        p28 = re.compile(r'^QL\s+Transmit\s+Configured\s*:\s*'
                         r'(?P<ql_transmit_configured>.+)$')

        # Init vars
        parsed_dict = {}
        interface_dict = {}
        for line in output.splitlines():
            line = line.strip()

            # Automatic selection process : Enable
            m = p0.match(line)
            if m:
                parsed_dict['automatic_selection_process'] = \
                    m.groupdict()['automatic_selection_process']
                continue

            # Equipment Clock : 2048 (EEC-Option1)
            m = p1.match(line)
            if m:
                parsed_dict['equipment_clock'] = \
                    m.groupdict()['equipment_clock']
                continue

            # Clock State : Frequency Locked
            m = p2.match(line)
            if m:
                parsed_dict['clock_state'] = \
                    m.groupdict()['clock_state']
                continue

            # Clock Mode : QL-Enable
            m = p3.match(line)
            if m:
                parsed_dict['clock_mode'] = \
                    m.groupdict()['clock_mode']
                continue

            # ESMC : Enabled
            m = p4.match(line)
            if m:
                parsed_dict['esmc_state'] = \
                    m.groupdict()['esmc_state']
                continue

            # SSM Option : 1
            # SSM Option : GEN1
            m = p5.match(line)
            if m:
                parsed_dict['ssm_option'] = \
                    m.groupdict()['ssm_option']
                continue

            # T0 : Internal
            # T0 : GigabitEthernet0/0/2
            m = p6.match(line)
            if m:
                intf = m.groupdict()['t0']
                # convert interface name to long name
                if intf.lower() != 'internal':
                    intf = \
                        Common.convert_intf_name(intf)
                parsed_dict['t0'] = intf
                continue

            # Hold-off (global) : 300 ms
            m = p7.match(line)
            if m:
                parsed_dict['global_hold_off_time'] = \
                    int(m.groupdict()['global_hold_off_time'])
                continue

            # Wait-to-restore (global) : 10 sec
            m = p8.match(line)
            if m:
                parsed_dict['global_wait_to_restore'] = \
                    int(m.groupdict()['global_wait_to_restore'])
                continue

            # Tsm Delay : 180 ms
            m = p9.match(line)
            if m:
                parsed_dict['tsm_delay'] = \
                    int(m.groupdict()['tsm_delay'])
                continue

            # Revertive : No
            m = p10.match(line)
            if m:
                parsed_dict['revertive'] = \
                    m.groupdict()['revertive']
                continue

            # Force Switch: FALSE
            m = p11.match(line)
            if m:
                parsed_dict['force_switch'] = \
                    m.groupdict()['force_switch']
                continue

            # Manual Switch: FALSE
            m = p12.match(line)
            if m:
                parsed_dict['manual_switch'] = \
                    m.groupdict()['manual_switch']
                continue

            # Number of synchronization sources: 4
            m = p13.match(line)
            if m:
                parsed_dict['num_of_sync_sources'] = \
                    int(m.groupdict()['num_of_sync_sources'])
                continue

            # Squelch Threshold: QL-SEC
            m = p14.match(line)
            if m:
                parsed_dict['squelch_threshold'] = \
                    m.groupdict()['squelch_threshold']
                continue

            # Last transition recorded: (begin)-> 2A (ql_mode_enable)-> 1A
            m = p15.match(line)
            if m:
                parsed_dict['last_transition_recorded'] = \
                    m.groupdict()['last_transition_recorded']
                continue

            # Internal
            # GigabitEthernet0/0/2
            m = p16.match(line)
            if m:
                local_interface = m.groupdict()['local_interface']

                # convert interface name to long name
                if local_interface.lower() != 'internal':
                    local_interface = \
                        Common.convert_intf_name(local_interface)

                interface_dict = parsed_dict.setdefault('local_interfaces', {}).setdefault(local_interface, {})
                continue

            # Description: None
            m = p17.match(line)
            if m:
                interface_dict['description'] = \
                    m.groupdict()['description']
                continue

            # Signal Type: NA
            m = p18.match(line)
            if m:
                interface_dict['signal_type'] = m.groupdict()['signal_type']
                continue

            # Mode: NA(Ql-enabled)
            m = p19.match(line)
            if m:
                interface_dict['mode'] = m.groupdict()['mode']
                continue

            # SSM Tx: DISABLED
            m = p20.match(line)
            if m:
                interface_dict['ssm_tx'] = m.groupdict()['ssm_tx']
                continue

            # SSM Rx: DISABLED
            m = p21.match(line)
            if m:
                interface_dict['ssm_rx'] = m.groupdict()['ssm_rx']
                continue

            # ESMC Tx: ENABLED
            m = p22.match(line)
            if m:
                interface_dict['esmc_tx'] = m.groupdict()['esmc_tx']
                continue

            # ESMC Rx: ENABLED
            m = p23.match(line)
            if m:
                interface_dict['esmc_rx'] = m.groupdict()['esmc_rx']
                continue

            # QL Receive: QL-SEC
            m = p24.match(line)
            if m:
                interface_dict['ql_receive'] = m.groupdict()['ql_receive']
                continue

            # QL Receive Configured: -
            m = p25.match(line)
            if m:
                interface_dict['ql_receive_configured'] = \
                    m.groupdict()['ql_receive_configured']
                continue

            # QL Receive Overrided: -
            m = p26.match(line)
            if m:
                interface_dict['ql_receive_overrided'] = \
                    m.groupdict()['ql_receive_overrided']
                continue

            # QL Transmit: QL-DNU
            m = p27.match(line)
            if m:
                interface_dict['ql_transmit'] = \
                    m.groupdict()['ql_transmit']
                continue

            # QL Transmit Configured: -
            m = p28.match(line)
            if m:
                interface_dict['ql_transmit_configured'] = \
                    m.groupdict()['ql_transmit_configured']
                continue

        return parsed_dict


class ShowNetworkClocksSynchronizationT0Schema(MetaParser):
    ''' Schema for:
        * 'show network-clocks synchronization t0'
    '''

    schema = {
        'automatic_selection_process': str,
        'equipment_clock': str,
        'clock_mode': str,
        'esmc_state': str,
        'ssm_option': str,
        Optional('t0'): str,
        'global_hold_off_time': int,
        'global_wait_to_restore': int,
        'tsm_delay': int,
        'revertive': str,
        'local_interfaces': {
            Any(): {
                'signal_type': str,
                'mode': str,
                'priority': int,
                'ql_in': str,
                'esmc_tx': str,
                'esmc_rx': str
            },
        },
    }


# ==================================================
# Parser for 'show network-clocks synchronization t0'
# ==================================================
class ShowNetworkClocksSynchronizationT0(ShowNetworkClocksSynchronizationT0Schema):
    ''' Parser for:
        * 'show network-clocks synchronization t0'
    '''
    cli_command = 'show network-clocks synchronization t0'

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)

        # Automatic selection process : Enable
        p0 = re.compile(r'^Automatic\s+selection\s+process\s*:\s*'
                        r'(?P<automatic_selection_process>.+)$')

        # Equipment Clock : 2048 (EEC-Option1)
        p1 = re.compile(r'^Equipment\s+Clock\s*:\s*'
                        r'(?P<equipment_clock>\d+\s*\(.+\))$')

        # Clock Mode : QL-Enable
        p2 = re.compile(r'^Clock\s+Mode\s*:\s*'
                        r'(?P<clock_mode>.+)$')

        # ESMC : Enabled
        p3 = re.compile(r'^ESMC\s*:\s*'
                        r'(?P<esmc_state>.+)$')

        # SSM Option : 1
        # SSM Option : GEN1
        p4 = re.compile(r'^SSM\s+Option\s*:\s*'
                        r'(?P<ssm_option>.+)$')

        # T0 : Internal
        # T0 : GigabitEthernet0/0/2
        p5 = re.compile(r'^T0\s*:\s*'
                        r'(?P<t0>.+)$')

        # Hold-off (global) : 300 ms
        p6 = re.compile(r'^Hold-off\s+\(global\)\s*:\s*'
                        r'(?P<global_hold_off_time>\d+)\s*ms$')

        # Wait-to-restore (global) : 10 sec
        p7 = re.compile(r'^Wait-to-restore\s+\(global\)\s*:\s*'
                        r'(?P<global_wait_to_restore>\d+)\s*sec$')

        # Tsm Delay : 180 ms
        p8 = re.compile(r'^Tsm\s+Delay\s*:\s*'
                        r'(?P<tsm_delay>\d+)\s*ms$')

        # Revertive : No
        p9 = re.compile(r'^Revertive\s*:\s*'
                        r'(?P<revertive>.+)$')

        #  Internal             NA          NA/Dis       251   QL-SEC    NA        NA
        # *Gi0/0/2              NA          Sync/En      1     QL-SEC    -         -
        p10 = re.compile(r'(?P<local_interface>\S+) +'
                         r'(?P<signal_type>\S+) +'
                         r'(?P<mode>\S+/\S+) +(?P<priority>\d+) +'
                         r'(?P<ql_in>\S+) +'
                         r'(?P<esmc_tx>\S+) +'
                         r'(?P<esmc_rx>\S+)$')

        # Init vars
        parsed_dict = {}
        interface_dict = {}
        for line in output.splitlines():
            line = line.strip()

            # Automatic selection process : Enable
            m = p0.match(line)
            if m:
                parsed_dict['automatic_selection_process'] = \
                    m.groupdict()['automatic_selection_process']
                continue

            # Equipment Clock : 2048 (EEC-Option1)
            m = p1.match(line)
            if m:
                parsed_dict['equipment_clock'] = \
                    m.groupdict()['equipment_clock']
                continue

            # Clock Mode : QL-Enable
            m = p2.match(line)
            if m:
                parsed_dict['clock_mode'] = \
                    m.groupdict()['clock_mode']
                continue

            # ESMC : Enabled
            m = p3.match(line)
            if m:
                parsed_dict['esmc_state'] = \
                    m.groupdict()['esmc_state']
                continue

            # SSM Option : 1
            # SSM Option : GEN1
            m = p4.match(line)
            if m:
                parsed_dict['ssm_option'] = \
                    m.groupdict()['ssm_option']
                continue

            # T0 : Internal
            # T0 : GigabitEthernet0/0/2
            m = p5.match(line)
            if m:
                intf = m.groupdict()['t0']
                # convert interface name to long name
                if intf.lower() != 'internal':
                    intf = \
                        Common.convert_intf_name(intf)
                parsed_dict['t0'] = intf
                continue

            # Hold-off (global) : 300 ms
            m = p6.match(line)
            if m:
                parsed_dict['global_hold_off_time'] = \
                    int(m.groupdict()['global_hold_off_time'])
                continue

            # Wait-to-restore (global) : 10 sec
            m = p7.match(line)
            if m:
                parsed_dict['global_wait_to_restore'] = \
                    int(m.groupdict()['global_wait_to_restore'])
                continue

            # Tsm Delay : 180 ms
            m = p8.match(line)
            if m:
                parsed_dict['tsm_delay'] = \
                    int(m.groupdict()['tsm_delay'])
                continue

            # Revertive : No
            m = p9.match(line)
            if m:
                parsed_dict['revertive'] = \
                    m.groupdict()['revertive']
                continue

            #  Internal             NA          NA/Dis       251   QL-SEC    NA        NA
            # *Gi0/0/2              NA          Sync/En      1     QL-SEC    -         -
            #  Gi0/0/6              NA          Sync/En      2     QL-SEC    -         -
            m = p10.match(line)
            if m:
                local_interface = m.groupdict()['local_interface']
                if local_interface.lower() != 'internal':
                    if local_interface[0] in ['*', '#', '&']:
                        local_interface = \
                            local_interface[0] + Common.convert_intf_name(local_interface[1:])
                    else:
                        local_interface = Common.convert_intf_name(local_interface)
                interface_dict = parsed_dict.setdefault('local_interfaces', {}).setdefault(local_interface, {})
                interface_dict['signal_type'] = m.groupdict()['signal_type']
                interface_dict['mode'] = m.groupdict()['mode']
                interface_dict['priority'] = int(m.groupdict()['priority'])
                interface_dict['ql_in'] = m.groupdict()['ql_in']
                interface_dict['esmc_tx'] = m.groupdict()['esmc_tx']
                interface_dict['esmc_rx'] = m.groupdict()['esmc_rx']
                continue

        return parsed_dict

