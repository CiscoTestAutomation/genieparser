"""
IOSXE C9300 parsers for the following show commands:
    * show inventory
"""
# Python
import re
import logging

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional


# ============================
#  Schema for 'show inventory'
# ============================
class ShowInventorySchema(MetaParser):

    """ Schema for:
        * show inventory
    """
    schema = {
        'index': {
            Any():
                {'name': str,
                 'descr': str,
                 Optional('pid'): str,
                 Optional('vid'): str,
                 Optional('sn'): str,
                }
            }
        }


# ============================
#  Parser for 'show inventory'
# ============================
class ShowInventory(ShowInventorySchema):
    """
    Parser for :
        * show inventory
    """

    cli_command = 'show inventory'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}
        index = 0

        # --------------------------------------------------------------
        # Regex patterns
        # --------------------------------------------------------------
        # NAME: "c93xx Stack", DESCR: "c93xx Stack"
        p1 = re.compile(r'^NAME: +\"(?P<name>[\s\S]+)\",'
                        r' +DESCR: +\"(?P<descr>[\s\S]+)\"$')

        # PID: C9300-48UXM       , VID: V02  , SN: FCW2242G0V3
        # PID: C9300-24T         , VID:      , SN:
        p2 = re.compile(r'^PID: +(?P<pid>\S+) +, +VID:( +(?P<vid>\S+))? +,'
                        r' +SN:( +(?P<sn>\S+))?$')

        # --------------------------------------------------------------
        # Build the parsed output
        # --------------------------------------------------------------
        for line in out.splitlines():
            line = line.strip()

            # NAME: "c93xx Stack", DESCR: "c93xx Stack"
            m = p1.match(line)
            if m:
                index += 1
                group = m.groupdict()
                final_dict = parsed_dict.setdefault('index', {}).setdefault(index, {})
                for key in group.keys():
                    if group[key]:
                        final_dict[key] = group[key]
                continue

            # PID: C9300-48UXM       , VID: V02  , SN: FCW2242G0V3
            m = p2.match(line)
            if m:
                group = m.groupdict()
                for key in group.keys():
                    if group[key]:
                        final_dict[key] = group[key]
                continue

        return parsed_dict


class ShowEnvironmentAllSchema(MetaParser):
    """Schema for show environment all"""
    schema = {
        'switch': {
            Any(): {
                'fan': {
                    Any(): {
                        'state': str,
                        Optional('direction'): str,
                        Optional('speed'): int,
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
                Optional('inlet_temperature'): {
                    'value': str,
                    'state': str,
                    'yellow_threshold': str,
                    'red_threshold': str
                },
                Optional('outlet_temperature'): {
                    'value': str,
                    'state': str,
                    'yellow_threshold': str,
                    'red_threshold': str
                },
                Optional('hotspot_temperature'): {
                    'value': str,
                    'state': str,
                    'yellow_threshold': str,
                    'red_threshold': str
                },
                Optional('asic_temperature'): {
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

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # Switch 1 FAN 1 is OK
        p1 = re.compile(r'^Switch +(?P<switch>\d+) +FAN +(?P<fan>\d+) +is +(?P<state>[\w\s]+)$')

        # Switch 1 FAN 1 direction is Front to Back
        p1_1 = re.compile(r'^Switch +(?P<switch>\d+) +FAN +(?P<fan>\d+) +direction +is +(?P<direction>[\w\s]+)$')

        # Switch   FAN     Speed   State
        # ----------------------------------
        # 1        1       14240     OK
        p1_2 = re.compile(r'^(?P<switch>\d+)\s+(?P<fan>\d+)\s+(?P<speed>\d+)\s+(?P<state>[\w\s]+)$')

        # FAN PS-1 is OK
        p2 = re.compile(r'^FAN +PS\-(?P<ps>\d+) +is +(?P<state>[\w\s]+)$')

        # Switch 1: SYSTEM TEMPERATURE is OK
        p3 = re.compile(r'^Switch +(?P<switch>\d+): +SYSTEM +TEMPERATURE +is +(?P<state>[\w\s]+)$')

        # Inlet Temperature Value: 21 Degree Celsius
        # Outlet Temperature Value: 32 Degree Celsius
        # Hotspot Temperature Value: 49 Degree Celsius
        p4 = re.compile(r'^(?P<type>\w+) +Temperature +Value: +(?P<temperature>\d+) +Degree +Celsius$')

        # Temperature State: GREEN
        p5 = re.compile(r'^Temperature +State: +(?P<state>\w+)$')

        # Yellow Threshold : 105 Degree Celsius
        # Red Threshold    : 125 Degree Celsius
        p6 = re.compile(r'^(?P<color>\w+) +Threshold *: +(?P<temperature>\d+) +Degree +Celsius$')

        # SW  PID                 Serial#     Status           Sys Pwr  PoE Pwr  Watts
        # --  ------------------  ----------  ---------------  -------  -------  -----
        # 1A  PWR-C1-350WAC-P     DCC2337B0K5  OK              Good     n/a      350
        # 1A  PWR-C4-950WAC-R     APS222700VU  No Input Power  Bad      n/a      950
        # 1B  Not Present
        p7 = re.compile(r'^(?P<sw>\d+)(?P<ps>\w+) *'
                        r'((?P<pid>[\w\-]+) +'
                        r'(?P<serial_number>\w+) +)?'
                        r'(?P<status>(\w+|Not Present|No Input Power)) *'
                        r'((?P<system_power>\w+) +'
                        r'(?P<poe_power>[\w\/]+) +'
                        r'(?P<watts>\w+))?$')

        for line in out.splitlines():
            line = line.strip()

            # Switch 1 FAN 1 is OK
            m = p1.match(line)
            if m:
                group = m.groupdict()
                switch = group['switch']
                fan = group['fan']
                root_dict = ret_dict.setdefault('switch', {}).setdefault(switch, {})
                root_dict.setdefault('fan', {}).setdefault(fan, {}).setdefault('state', group['state'])
                continue

            # Switch 1 FAN 1 direction is Front to Back
            m = p1_1.match(line)
            if m:
                group = m.groupdict()
                switch = group['switch']
                fan = group['fan']
                fan_dict = ret_dict.setdefault('switch', {}).setdefault(switch, {})\
                                   .setdefault('fan', {}).setdefault(fan, {})
                fan_dict.update({'direction': group['direction']})
                continue

            # Switch   FAN     Speed   State
            # ----------------------------------
            #   1       1      14240     OK
            m = p1_2.match(line)
            if m:
                group = m.groupdict()
                switch = group['switch']
                fan = group['fan']
                speed = int(group['speed'])
                state = group['state']

                root_dict = ret_dict.setdefault('switch', {}).setdefault(switch, {})
                fan_dict = root_dict.setdefault('fan', {}).setdefault(fan, {})
                fan_dict.update({'speed': speed,
                                 'state': state})
                continue

            # FAN PS-1 is OK
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ps = group['ps']
                power_supply_dict = root_dict.setdefault('power_supply', {}).setdefault(ps, {})
                power_supply_dict.setdefault('state', group['state'])
                continue

            # Switch 1: SYSTEM TEMPERATURE is OK
            m = p3.match(line)
            if m:
                group = m.groupdict()
                switch = group['switch']
                root_dict = ret_dict.setdefault('switch', {}).setdefault(switch, {})
                root_dict['system_temperature_state'] = group['state']
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
                temp_dict['state'] = m.groupdict()['state']
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
                power_supply_dict.update({k: v for k, v in group.items()
                        if k in ['pid', 'serial_number', 'watts'] and v})
                power_supply_dict.update({k: v for k, v in group.items()
                        if k in ['status', 'system_power', 'poe_power'] and v})
                continue
        return ret_dict
