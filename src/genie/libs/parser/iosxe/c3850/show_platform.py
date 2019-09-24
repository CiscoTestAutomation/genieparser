"""c3850 implementation of show_platform.py

"""
import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                         Any, \
                                         Optional, \
                                         Or, \
                                         And, \
                                         Default, \
                                         Use


class ShowEnvironmentAllSchema(MetaParser):
    """Schema for show environment all"""
    schema = {
        'switch': {
            Any(): {
                'fan': {
                    Any(): {
                        'state': str,
                        Optional('direction'): str,
                    },
                },
                'power_supply': {
                    Any(): {
                        'state': str,
                        Optional('pid'): str,
                        Optional('serial_number'): str,
                        'status': str,
                        Optional('system_power'): str,
                        Optional('poe_power'): str,
                        Optional('watts'): str
                    }
                },
                'system_temperature_state': str,
                Optional('inlet_temperature'):{
                    'value': str,
                    'state': str,
                    'yellow_threshold': str,
                    'red_threshold': str
                },
                Optional('hotspot_temperature'):{
                    'value': str,
                    'state': str,
                    'yellow_threshold': str,
                    'red_threshold': str
                },
                Optional('asic_temperature'):{
                    'value': str,
                    'state': str,
                    'yellow_threshold': str,
                    'red_threshold': str
                },
            },
        },
    }


class ShowEnvironmentAll(ShowEnvironmentAllSchema):
    """Parser for show environment all"""
    PS_MAPPING = {'A': '1', 'B': '2'}

    cli_command = 'show environment all'

    def cli(self,output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern
        p1 = re.compile(r'^Switch +(?P<switch>\d+) +FAN +(?P<fan>\d+) +is +(?P<state>[\w\s]+)$')

        # Switch 1 FAN 1 direction is Front to Back
        p1_1 = re.compile(r'^Switch +(?P<switch>\d+) +FAN +(?P<fan>\d+) '
                           '+direction +is +(?P<direction>[\w\s]+)$')

        p2 = re.compile(r'^FAN +PS\-(?P<ps>\d+) +is +(?P<state>[\w\s]+)$')

        p3 = re.compile(r'^Switch +(?P<switch>\d+): +SYSTEM +TEMPERATURE +is +(?P<state>[\w\s]+)$')

        p4 = re.compile(r'^(?P<type>\w+) +Temperature +Value: +(?P<temperature>\d+) +Degree +Celsius$')

        p5 = re.compile(r'^Temperature +State: +(?P<state>\w+)$')

        p6 = re.compile(r'^(?P<color>\w+) +Threshold *: +(?P<temperature>\d+) +Degree +Celsius$')

        p7 = re.compile(r'^(?P<sw>\d+)(?P<ps>\w+) *'
                         '((?P<pid>[\w\-]+) +'
                         '(?P<serial_number>\w+) +)?'
                         '(?P<status>(\w+|Not Present)) *'
                         '((?P<system_power>\w+) +'
                         '(?P<poe_power>[\w\/]+) +'
                         '(?P<watts>\w+))?$')

        for line in out.splitlines():
            line = line.strip()

            # Switch 1 FAN 1 is OK
            m = p1.match(line)
            if m:
                group = m.groupdict()
                switch = group['switch']
                fan = group['fan']
                root_dict = ret_dict.setdefault('switch', {}).setdefault(switch, {})
                root_dict.setdefault('fan', {}).setdefault(fan, {}).setdefault('state', group['state'].lower())
                continue
            
            # Switch 1 FAN 1 direction is Front to Back
            m = p1_1.match(line)
            if m:
                group = m.groupdict()
                switch = group['switch']
                fan = group['fan']
                fan_dict = ret_dict.setdefault('switch', {}).setdefault(switch, {})\
                                   .setdefault('fan', {}).setdefault(fan, {})
                fan_dict.update({'direction': group['direction'].lower()})
                continue
                
            # FAN PS-1 is OK
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ps = group['ps']
                power_supply_dict = root_dict.setdefault('power_supply', {}).setdefault(ps, {})
                power_supply_dict.setdefault('state', group['state'].lower())
                continue

            # Switch 1: SYSTEM TEMPERATURE is OK
            m = p3.match(line)
            if m:
                group = m.groupdict()
                switch = group['switch']
                root_dict = ret_dict.setdefault('switch', {}).setdefault(switch, {})
                root_dict['system_temperature_state'] = group['state'].lower()
                continue

            # Inlet Temperature Value: 34 Degree Celsius
            # Hotspot Temperature Value: 45 Degree Celsius
            # ASIC Temperature Value: 36 Degree Celsius
            m = p4.match(line)
            if m:
                group = m.groupdict()
                temp_type = group['type'].lower() + '_temperature'
                temp_dict = root_dict.setdefault(temp_type, {})
                temp_dict['value'] = group['temperature']
                continue

            # Temperature State: GREEN
            m = p5.match(line)
            if m:
                temp_dict['state'] = m.groupdict()['state'].lower()
                continue

            # Yellow Threshold : 46 Degree Celsius
            # Red Threshold    : 56 Degree Celsius
            m = p6.match(line)
            if m:
                group = m.groupdict()
                color_type = group['color'].lower() + '_threshold'
                temp_dict[color_type] = group['temperature']
                continue

            # SW  PID                 Serial#     Status           Sys Pwr  PoE Pwr  Watts
            # --  ------------------  ----------  ---------------  -------  -------  -----
            # 1A  PWR-C1-715WAC       DCB1844G1ZY  OK              Good     Good     715 
            # 1B  Not Present
            m = p7.match(line)
            if m:
                group = m.groupdict()
                switch = group.pop('sw')
                ps = self.PS_MAPPING[group.pop('ps')]
                root_dict = ret_dict.setdefault('switch', {}).setdefault(switch, {})
                power_supply_dict = root_dict.setdefault('power_supply', {}).setdefault(ps, {})
                power_supply_dict.update(
                       {k:v for k, v in group.items() if k in ['pid', 'serial_number', 'watts'] and v})
                power_supply_dict.update(
                       {k:v.lower() for k, v in group.items() \
                           if k in ['status', 'system_power', 'poe_power'] and v})
                continue
        return ret_dict
