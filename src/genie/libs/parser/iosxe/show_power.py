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

    cli_command = 'show stack-power'

    def cli(self,output=None):
        if output is None:
            # get output from device
            out = self.device.execute(self.cli_command)
        else:
            out = output

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


class ShowPowerInlineSchema(MetaParser):
    """Schema for show power inline """
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
        },
        Optional('watts'): {
            Any(): {
                'module': str,
                'available': float,
                'used': float,
                'remaining': float
            }
        }
    }


class ShowPowerInline(ShowPowerInlineSchema):
    """Parser for show power inline
                  show power inline <interface>"""

    cli_command = ['show power inline', 'show power inline {interface}']

    def cli(self, interface='', output=None):
        if output is None:
            if interface:
                cmd = self.cli_command[1].format(interface=interface)
            else:
                cmd = self.cli_command[0]

            # get output from device
            out = self.device.execute(cmd)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern
        p1 = re.compile(r'^(?P<intf>[\w\-\/\.]+)\s*'
                         '(?P<admin_state>\w+)\s+'
                         '(?P<oper_state>\w+)\s+'
                         '(?P<power>[\d\.]+)\s+'
                         '(?P<device>(?=\S).*(?<=\S))\s+'
                         '(?P<class>[\w\/]+)\s+'
                         '(?P<max>[\d\.]+)$')

        # Module   Available     Used     Remaining
        #          (Watts)     (Watts)    (Watts)
        # ------   ---------   --------   ---------
        # 1          1550.0      147.0      1403.0
        p2 = re.compile(r'^(?P<module>\d+)\s+'
                         '(?P<available>[\d\.]+)\s+'
                         '(?P<used>[\d\.]+)\s+'
                         '(?P<remaining>[\d\.]+)\s*$')

        # Available:1170.0(w)  Used:212.2(w)  Remaining:957.8(w)
        p3 = re.compile(r'^\s*[Aa]vailable\:(?P<available>[\d\.]+)\(\w+\)\s+'
                         '[Uu]sed\:(?P<used>[\d\.]+)\(\w+\)\s+'
                         '[Rr]emaining\:(?P<remaining>[\d\.]+)\(\w+\)\s*$')

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
                intf_dict.update({k: v for k, v in group.items() if 'n/a' not in v})

                continue

            # Module   Available     Used     Remaining
            #          (Watts)     (Watts)    (Watts)
            # ------   ---------   --------   ---------
            # 1          1550.0      147.0      1403.0
            m = p2.match(line)
            if m:
                group = m.groupdict()

                module = group.pop('module')
                stat_dict = ret_dict.setdefault('watts', {}).setdefault(module, {})

                stat_dict['module'] = module
                stat_dict['available'] = float(group.pop('available'))
                stat_dict['used'] = float(group.pop('used'))
                stat_dict['remaining'] = float(group.pop('remaining'))

                continue

            # Available:1170.0(w)  Used:212.2(w)  Remaining:957.8(w)
            m = p3.match(line)
            if m:
                group = m.groupdict()

                stat_dict = ret_dict.setdefault('watts', {}).setdefault('0', {})

                stat_dict['module'] = '0'
                stat_dict['available'] = float(group.pop('available'))
                stat_dict['used'] = float(group.pop('used'))
                stat_dict['remaining'] = float(group.pop('remaining'))

        # Remove statistics if we don't have any interfaces
        if 'interface' not in ret_dict and 'watts' in ret_dict:
            ret_dict.pop('watts', None)

        return ret_dict