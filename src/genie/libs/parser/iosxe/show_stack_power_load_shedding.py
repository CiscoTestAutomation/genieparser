import re

from genie.libs.parser.utils.common import Common
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (And, Any, Default, Optional,
                                                Or, Schema, Use)

# ======================================================
# Parser for      'show stack-power load-shedding ' 
# ======================================================

class ShowStackPowerLoadSheddingSchema(MetaParser):
    """Schema for show stack-power load-shedding """

    schema = {
        'power_stack': {
            Any(): {
                'power_name': str,
                'stack_mode': str,
                'stack_topology': str,
                'stack_pwr': int,
                'total_pwr': int,
                'rsvd_pwr': int,
                'alloc_pwr': int,
                'sw_avail_num': int,
                'num_ps': int,
            },
        },
        'priority': {
            Any(): {
                'sw': int,
                'power_name': str,
                'stack_priority': str,
                'consumd_sw': int,
                'consumd_hi': float,
                'consumd_lo': float,
                'alloc_hi': float,
                'alloc_lo': float,
            },
        },
        'totals': {
            'consumd_sw': int,
            'consumd_hi': float,
            'consumd_lo': float,
            'alloc_hi': float,
            'alloc_lo': float,
        },
    }

class ShowStackPowerLoadShedding(ShowStackPowerLoadSheddingSchema):
    """Parser for show stack-power load-shedding"""

    cli_command = 'show stack-power load-shedding'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Powerstack-6 SP-PS Stndaln 1100 0 505 595 1 1
        p1 = re.compile(r"^(?P<power_name>\S+)\s+(?P<stack_mode>\S+)\s+(?P<stack_topology>\w+)\s+(?P<stack_pwr>\d+)"
                        r"\s+(?P<total_pwr>\d+)\s+(?P<rsvd_pwr>\d+)\s+(?P<alloc_pwr>\d+)\s+(?P<sw_avail_num>\d+)\s+(?P<num_ps>\d+)$")
        
        # 1 Powerstack-1 2-11-20 108 0.0 0.0 0.0 0.0
        # 1   Powerstack-2           1-12-21  173.8    0.0      8.8      0.0      22.3
        p2 = re.compile(r"^(?P<sw>\d+)\s+(?P<power_name>\S+)\s+(?P<stack_priority>\d+\s*-\s*\d+\s*-\s*\d+)\s+(?P<consumd_sw>\S+)"
                        r"\s+(?P<consumd_hi>\S+)\s+(?P<consumd_lo>\S+)\s+(?P<alloc_hi>\S+)\s+(?P<alloc_lo>\S+)$")
        
        # 1109 0.0 0.0 0.0 0.0
        # Totals:                             529.1    0.0      54.9     0.0      107.8
        p3 = re.compile(r"^Totals:\s+(?P<consumd_sw>\S+)\s+(?P<consumd_hi>\S+)\s+(?P<consumd_lo>\S+)\s+(?P<alloc_hi>\S+)\s+(?P<alloc_lo>\S+)$")
        
        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()
            
            # Powerstack-6 SP-PS Stndaln 1100 0 505 595 1 1
            m = p1.match(line)
            if m:
                dict_val = m.groupdict()
                power_name_var = dict_val['power_name']
                power_stack = ret_dict.setdefault('power_stack', {})
                power_name_dict = ret_dict['power_stack'].setdefault(power_name_var, {})
                power_name_dict['power_name'] = dict_val['power_name']
                power_name_dict['stack_mode'] = dict_val['stack_mode']
                power_name_dict['stack_topology'] = dict_val['stack_topology']
                power_name_dict['stack_pwr'] = int(dict_val['stack_pwr'])
                power_name_dict['total_pwr'] = int(dict_val['total_pwr'])
                power_name_dict['rsvd_pwr'] = int(dict_val['rsvd_pwr'])
                power_name_dict['alloc_pwr'] = int(dict_val['alloc_pwr'])
                power_name_dict['sw_avail_num'] = int(dict_val['sw_avail_num'])
                power_name_dict['num_ps'] = int(dict_val['num_ps'])
                continue

            # 1 Powerstack-1 2-11-20 108 0.0 0.0 0.0 0.0
            m = p2.match(line)
            if m:
                dict_val = m.groupdict()
                sw_var = dict_val['sw']
                priority = ret_dict.setdefault('priority', {})
                sw_dict = ret_dict['priority'].setdefault(sw_var, {})
                sw_dict['sw'] = int(dict_val['sw'])
                sw_dict['power_name'] = dict_val['power_name']
                sw_dict['stack_priority'] = dict_val['stack_priority']
                sw_dict['consumd_sw'] = int(float(dict_val['consumd_sw']))
                sw_dict['consumd_hi'] = float(dict_val['consumd_hi'])
                sw_dict['consumd_lo'] = float(dict_val['consumd_lo'])
                sw_dict['alloc_hi'] = float(dict_val['alloc_hi'])
                sw_dict['alloc_lo'] = float(dict_val['alloc_lo'])
                continue

            # 1109 0.0 0.0 0.0 0.0
            m = p3.match(line)
            if m:
                dict_val = m.groupdict()
                totals_dict = ret_dict.setdefault('totals', {})
                totals_dict['consumd_sw'] = int(float(dict_val['consumd_sw']))
                totals_dict['consumd_hi'] = float(dict_val['consumd_hi'])
                totals_dict['consumd_lo'] = float(dict_val['consumd_lo'])
                totals_dict['alloc_hi'] = float(dict_val['alloc_hi'])
                totals_dict['alloc_lo'] = float(dict_val['alloc_lo'])
                continue

        return ret_dict

# ======================================================
# Schema for 'show stack-power detail switch {switch}'
# ======================================================
class ShowStackPowerDetailSwitchSchema(MetaParser):
    """Schema for 'show stack-power detail switch {switch}'"""
    schema = {
        'power_stack': {
            Any(): {
                'stack_mode': str,
                'stack_topology': str,
                'total_powr': int,
                'rsvd_pwr': int,
                'alloc_pwr': int,
                'sw_avail_pwr': int,
                'num_sw': int,
                'num_ps': int,
                'switches': {
                    Any(): {
                        'power_budget': int,
                        'power_allocated': int,
                        'low_port_priority_value': int,
                        'high_port_priority_value': int,
                        'switch_priority_value': int,
                        'port_status': {
                            'port_1': str,
                            'port_2': str,
                        },
                        'neighbor': {
                            'port_1': str,
                            'port_2': str,
                        }
                    }
                }
            }
        }
    }

class ShowStackPowerDetailSwitch(ShowStackPowerDetailSwitchSchema):
    """Parser for 'show stack-power detail switch {switch}'"""
    cli_command = ['show stack-power detail switch {switch}']

    def cli(self, switch, output=None):
        if output is None:
            cmd = self.cli_command[0].format(switch=switch)
            output = self.device.execute(cmd)

        # Initialize the return dictionary
        ret_dict = {}

        # Regex patterns for summary table
        # Powerstack-6 SP-PS Stndaln 1100 0 505 595 1 1
        p1 = re.compile(
            r'^(?P<power_stack_name>\S+)\s+(?P<stack_mode>\S+)\s+(?P<stack_topology>\S+)\s+'
            r'(?P<total_powr>\d+)\s+(?P<rsvd_pwr>\d+)\s+(?P<alloc_pwr>\d+)\s+'
            r'(?P<sw_avail_pwr>\d+)\s+(?P<num_sw>\d+)\s+(?P<num_ps>\d+)$'
        )

        # Power stack name
        p2 = re.compile(r'^Power stack name: +(?P<power_stack_name>[\w\-]+)$')
        # Stack mode
        p3 = re.compile(r'^Stack mode: +(?P<stack_mode>[\w\s]+)$')
        # Stack topology
        p4 = re.compile(r'^Stack topology: +(?P<stack_topology>[\w\s]+)$')
        # Switch ID
        p5 = re.compile(r'^Switch (?P<switch_id>\d+):$')
        # Power budget
        p6 = re.compile(r'^Power budget: +(?P<power_budget>\d+)$')
        # Power allocated
        p7 = re.compile(r'^Power allocated: +(?P<power_allocated>\d+)$')
        # Low port priority value
        p8 = re.compile(r'^Low port priority value: +(?P<low_port_priority_value>\d+)$')
        # High port priority value
        p9 = re.compile(r'^High port priority value: +(?P<high_port_priority_value>\d+)$')
        # Switch priority value
        p10 = re.compile(r'^Switch priority value: +(?P<switch_priority_value>\d+)$')
        # Port 1 status
        p11 = re.compile(r'^Port 1 status: +(?P<port_1_status>\w+)$')
        # Port 2 status
        p12 = re.compile(r'^Port 2 status: +(?P<port_2_status>\w+)$')
        # Neighbor on port 1
        p13 = re.compile(r'^Neighbor on port 1: +(?P<neighbor_port_1>[\w\.]+)$')
        # Neighbor on port 2
        p14 = re.compile(r'^Neighbor on port 2: +(?P<neighbor_port_2>[\w\.]+)$')

        current_power_stack = None
        current_switch = None

        for line in output.splitlines():
            line = line.strip()

            # Match summary table
            # PowerStack-1 SP-PS Ring 1100 100 500 500 2 2
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                current_power_stack = groups['power_stack_name']
                power_stack_dict = ret_dict.setdefault('power_stack', {}).setdefault(current_power_stack, {})
                power_stack_dict['stack_mode'] = groups['stack_mode']
                power_stack_dict['stack_topology'] = groups['stack_topology']
                power_stack_dict['total_powr'] = int(groups['total_powr'])
                power_stack_dict['rsvd_pwr'] = int(groups['rsvd_pwr'])
                power_stack_dict['alloc_pwr'] = int(groups['alloc_pwr'])
                power_stack_dict['sw_avail_pwr'] = int(groups['sw_avail_pwr'])
                power_stack_dict['num_sw'] = int(groups['num_sw'])
                power_stack_dict['num_ps'] = int(groups['num_ps'])
                continue

            # Power stack name: PowerStack-1
            m = p2.match(line)
            if m:
                current_power_stack = m.group('power_stack_name')
                continue

            # Stack mode: SP-PS
            m = p3.match(line)
            if m and current_power_stack:
                power_stack_dict['stack_mode'] = m.group('stack_mode')
                continue

            # Stack topology: Ring
            m = p4.match(line)
            if m and current_power_stack:
                power_stack_dict['stack_topology'] = m.group('stack_topology')
                continue

            # Switch 1:
            m = p5.match(line)
            if m and current_power_stack:
                current_switch = int(m.group('switch_id'))
                switches_dict = power_stack_dict.setdefault('switches', {}).setdefault(current_switch, {})
                continue

            # Power budget: 1100
            m = p6.match(line)
            if m and current_switch is not None:
                switches_dict['power_budget'] = int(m.group('power_budget'))
                continue

            # Power allocated: 500
            m = p7.match(line)
            if m and current_switch is not None:
                switches_dict['power_allocated'] = int(m.group('power_allocated'))
                continue

            # Low port priority value: 1
            m = p8.match(line)
            if m and current_switch is not None:
                switches_dict['low_port_priority_value'] = int(m.group('low_port_priority_value'))
                continue

            # High port priority value: 2
            m = p9.match(line)
            if m and current_switch is not None:
                switches_dict['high_port_priority_value'] = int(m.group('high_port_priority_value'))
                continue

            # Switch priority value: 3
            m = p10.match(line)
            if m and current_switch is not None:
                switches_dict['switch_priority_value'] = int(m.group('switch_priority_value'))
                continue

            # Port 1 status: Active
            m = p11.match(line)
            if m and current_switch is not None:
                port_status_dict = switches_dict.setdefault('port_status', {})
                port_status_dict['port_1'] = m.group('port_1_status')
                continue

            # Port 2 status: Inactive
            m = p12.match(line)
            if m and current_switch is not None:
                port_status_dict = switches_dict.setdefault('port_status', {})
                port_status_dict['port_2'] = m.group('port_2_status')
                continue

            # Neighbor on port 1: Switch-2
            m = p13.match(line)
            if m and current_switch is not None:
                neighbor_dict = switches_dict.setdefault('neighbor', {})
                neighbor_dict['port_1'] = m.group('neighbor_port_1')
                continue

            # Neighbor on port 2: Switch-3
            m = p14.match(line)
            if m and current_switch is not None:
                neighbor_dict = switches_dict.setdefault('neighbor', {})
                neighbor_dict['port_2'] = m.group('neighbor_port_2')
                continue

        return ret_dict