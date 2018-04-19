"""show_platform.py

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

# import parser utils
from genie.libs.parser.utils.common import Common


class ShowStackPowerSchema(MetaParser):
    """Schema for show stack-power"""
    schema = {
        'power_stack': {
            Any(): {
                'mode': str,
                'topology': str,
                'total_power': int,
                'reserved_power': int,
                'allocated_power': int,
                'unused_power': int,
                'switch_num': int,
                'power_supply_num': int
            },
        }
    }


class ShowStackPower(ShowStackPowerSchema):
    """Parser for show stack-power"""

    def cli(self):
         # get output from device
        out = self.device.execute('show stack-power')

        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern
        p1 = re.compile(r'^(?P<name>[\w\-]+) *'
                         '(?P<mode>[\w\-]+) +'
                         '(?P<topology>[\w\-]+) +'
                         '(?P<total_power>\d+) +'
                         '(?P<reserved_power>\d+) +'
                         '(?P<allocated_power>\d+) +'
                         '(?P<unused_power>\d+) +'
                         '(?P<switch_num>\d+) +'
                         '(?P<power_supply_num>\d+)$')

        for line in out.splitlines():
            line = line.strip()
            
            # Power Stack           Stack   Stack    Total   Rsvd    Alloc   Unused  Num  Num
            # Name                  Mode    Topolgy  Pwr(W)  Pwr(W)  Pwr(W)  Pwr(W)  SW   PS
            # --------------------  ------  -------  ------  ------  ------  ------  ---  ---
            # Powerstack-1          SP-PS   Stndaln  715     30      200     485     1    1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                name = group.pop('name')
                stack_dict = ret_dict.setdefault('power_stack', {}).setdefault(name, {})
                stack_dict['mode'] = group.pop('mode')
                stack_dict['topology'] = group.pop('topology')
                stack_dict.update(
                       {k:int(v) for k, v in group.items()})
                continue
        return ret_dict


class ShowPowerInlineInterfaceSchema(MetaParser):
    """Schema for show power inline <interface>"""
    schema = {
        'interface': {
            Any(): {
                'admin_state': str,
                'oper_state': str,
                'power': float,
                Optional('device'): str,
                Optional('class'): str,
                'max': float
            },
        }
    }


class ShowPowerInlineInterface(ShowPowerInlineInterfaceSchema):
    """Parser for show power inline <interface>"""

    def cli(self, interface):
         # get output from device
        out = self.device.execute('show power inline {}'.format(interface))

        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern
        p1 = re.compile(r'^(?P<intf>[\w\-\/\.]+) *'
                         '(?P<admin_state>\w+) +'
                         '(?P<oper_state>\w+) +'
                         '(?P<power>[\d\.]+) +'
                         '(?P<device>[\w\-\/]+) +'
                         '(?P<class>[\w\/]+) +'
                         '(?P<max>[\d\.]+)$')

        for line in out.splitlines():
            line = line.strip()
            
            # Interface Admin  Oper       Power   Device              Class Max
            #                             (Watts)                            
            # --------- ------ ---------- ------- ------------------- ----- ----
            # Gi1/0/13  auto   on         15.4    AIR-CAP2602I-A-K9   3     30.0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                intf = Common.convert_intf_name(group.pop('intf'))
                intf_dict = ret_dict.setdefault('interface', {}).setdefault(intf, {})
                intf_dict['power'] = float(group.pop('power'))
                intf_dict['max'] = float(group.pop('max'))
                intf_dict.update(
                       {k:v for k, v in group.items() if 'n/a' not in v})
                continue
        return ret_dict