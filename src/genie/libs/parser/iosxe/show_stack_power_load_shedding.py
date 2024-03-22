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
