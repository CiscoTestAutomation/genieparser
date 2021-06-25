"""  show_power.py

IOSXE parsers for the following show command:

    * 'show stack-power'
    * 'show stack-power budgeting'
    * 'show power inline'
    * 'show power inline {interface}'
    * 'show power inline priority'
    * 'show power inline priority {interface}'
    * 'show power inline upoe-plus'
    * 'show power inline upoe-plus {interface}'
"""

import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional

# import parser utils
from genie.libs.parser.utils.common import Common


class ShowStackPowerSchema(MetaParser):
    """Schema for 
        * show stack-power
        * show stack-power budgeting
    """

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
                'power_supply_num': int,
                Optional('switches'): {
                    Any(): {
                        'power_supply_a': int,
                        'power_supply_b' : int,
                        'power_budget': int,
                        'allocated_power': int,
                        'available_power': int,
                        'consumed_power_sys': int,
                        'consumed_power_poe': int,
                    },
                },
            },
        },
        Optional('totals'): {
            'total_allocated_power': int,
            'total_available_power': int,
            'total_consumed_power_sys': int,
            'total_consumed_power_poe': int,
        },
    }


class ShowStackPower(ShowStackPowerSchema):
    """Parser for 
        * show stack-power
        * show stack-power budgeting
    """

    cli_command = ['show stack-power, show stack-power budgeting']

    def cli(self,output=None):
        if output is None:
            # get output from device
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # Powerstack-1          SP-PS   Stndaln  715     30      200     485     1    1
        p1 = re.compile(r'^(?P<name>[\w\-]+) *'
                        r'(?P<mode>[\w\-]+) +'
                        r'(?P<topology>[\w\-]+) +'
                        r'(?P<total_power>\d+) +'
                        r'(?P<reserved_power>\d+) +'
                        r'(?P<allocated_power>\d+) +'
                        r'(?P<unused_power>\d+) +'
                        r'(?P<switch_num>\d+) +'
                        r'(?P<power_supply_num>\d+)$')

        # 1   Powerstack-1         0        0      1200      240        960     129 /0
        p2 = re.compile(r'^(?P<switch_num>\d+) +'
                        r'(?P<name>[\w-]+) *'
                        r'(?P<power_supply_a>\d+) +'
                        r'(?P<power_supply_b>\d+) +'
                        r'(?P<power_budget>\d+) +'
                        r'(?P<allocated_power>\d+) +'
                        r'(?P<available_power>\d+) +'
                        r'(?P<consumed_power_sys>\d+)[ \/]+'
                        r'(?P<consumed_power_poe>\d+)$')

        # Totals:                               1150    1050      310/0
        p3 = re.compile(r'^Totals: +'
                        r'(?P<total_allocated_power>\d+) +'
                        r'(?P<total_available_power>\d+) +'
                        r'(?P<total_consumed_power_sys>\d+)[ \/]+'
                        r'(?P<total_consumed_power_poe>\d+)$')

        for line in out.splitlines():
            line = line.strip()
            
            # Powerstack-1          SP-PS   Stndaln  715     30      200     485     1    1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                name = group.pop('name')
                stack_dict = ret_dict.setdefault('power_stack', {})\
                                     .setdefault(name, {})
                stack_dict['mode'] = group.pop('mode')
                stack_dict['topology'] = group.pop('topology')
                stack_dict.update({k:int(v) for k, v in group.items()})
                continue

            # 1   Powerstack-1         0        0      1200      240        960     129 /0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                stack_name = group.pop('name')
                switch_num = group.pop('switch_num')
                switch_dict = ret_dict.setdefault('power_stack', {})\
                                      .setdefault(stack_name, {})\
                                      .setdefault('switches', {})\
                                      .setdefault(int(switch_num), {})
                switch_dict.update({k:int(v) for k, v in group.items()})
                continue

            # Totals:                               1150    1050      310/0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                total_dict = ret_dict.setdefault('totals', {})
                total_dict.update({k:int(v) for k, v in group.items()})
                continue

        return ret_dict


class ShowPowerInlineSchema(MetaParser):
    """Schema for show power inline """
    schema = {
        'interface': {
            Any(): {
                'admin_state': str,
                'oper_state': str,
                Optional('power'): float,
                Optional('device'): str,
                Optional('class'): str,
                Optional('priority'): str,
                Optional('max'): float
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
            out = self.device.execute(cmd)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern
        p1 = re.compile(r'^(?P<intf>[\w\-\/\.]+)\s*'
                        r'(?P<admin_state>\w+)\s+'
                        r'(?P<oper_state>\w+)\s+'
                        r'(?P<power>[\d\.]+)\s+'
                        r'(?P<device>(?=\S).*(?<=\S))\s+'
                        r'(?P<class>[\w\/]+)\s+'
                        r'(?P<max>[\d\.]+)$')


        # 1          1550.0      147.0      1403.0
        p2 = re.compile(r'^(?P<module>\d+)\s+'
                        r'(?P<available>[\d\.]+)\s+'
                        r'(?P<used>[\d\.]+)\s+'
                        r'(?P<remaining>[\d\.]+)\s*$')

        # Available:1170.0(w)  Used:212.2(w)  Remaining:957.8(w)
        p3 = re.compile(r'^\s*[Aa]vailable\:(?P<available>[\d\.]+)\(\w+\)\s+'
                        r'[Uu]sed\:(?P<used>[\d\.]+)\(\w+\)\s+'
                        r'[Rr]emaining\:(?P<remaining>[\d\.]+)\(\w+\)\s*$')

        for line in out.splitlines():
            line = line.strip()
            
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


class ShowPowerInlinePrioritySchema(MetaParser):
    """Schema for show power inline priority """
    schema = {
        'interface': {
            Any(): {
                'admin_state': str,
                'oper_state': str,
                'admin_priority': str,
            }
        }
    }


class ShowPowerInlinePriority(ShowPowerInlinePrioritySchema):
    """Parser for show power inline priority
                  show power inline priority <interface>"""

    cli_command = ['show power inline priority' , 'show power inline priority {interface}']

    def cli(self, interface='', output=None):
        if output is None:
            if interface:
                cmd = self.cli_command[1].format(interface=interface)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        #Gi1/0/1    auto   off        low
        p1 = re.compile(r'^(?P<intf>[\w\/]+)\s+'
                        r'(?P<admin_state>auto|off|static)\s+'
                        r'(?P<oper_state>\w+)\s+'
                        r'(?P<admin_priority>\w+)$')

        for line in out.splitlines():
            line = line.strip()

            #Gi1/0/1    auto   off        low
            m = p1.match(line)
            if m:
                group = m.groupdict()
                intf = group.pop('intf')
                intf_dict = ret_dict.setdefault('interface', {}).setdefault(intf, {})
                intf_dict.update(group)
                continue

        return ret_dict


class ShowPowerInlineUpoePlusSchema(MetaParser):
    """Schema for show power inline upoe-plus """
    schema = {
        'interface': {
            Any(): {
                'admin_state': str,
                'type': str,
                'oper_state': str,
                'allocated_power': float,
                'utilized_power': float,
                'class': str,
                'device': str,
            }
        }
    }


class ShowPowerInlineUpoePlus(ShowPowerInlineUpoePlusSchema):
    """Parser for show power inline upoe-plus
                  show power inline upoe-plus <interface>"""

    cli_command = ['show power inline upoe-plus', 'show power inline upoe-plus {interface}']

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

        # Gi1/0/4     auto   SP   on            4.0       3.8       1       Ieee PD
        # Gi1/0/15    auto   SS   on,on         60.0      10.5      6       Ieee PD
        # Gi1/0/23    auto   DS   on,on         45.4      26.9      3,4     Ieee PD
        p1 = re.compile(r'^(?P<intf>[\w\/]+)\s+(?P<admin_state>[a-zA-Z]+)\s+(?P<type>\w+)\s+(?P<oper_state>[\,\w+]+)\s+(?P<allocated_power>[\d\.]+)\s+(?P<utilized_power>[\d\.]+)\s+(?P<class>[\w\,\/]+)\s+(?P<device>.*)$')

        for line in out.splitlines():
            line = line.strip()
  
            # Gi1/0/4     auto   SP   on            4.0       3.8       1       Ieee PD
            # Gi1/0/15    auto   SS   on,on         60.0      10.5      6       Ieee PD
            # Gi1/0/23    auto   DS   on,on         45.4      26.9      3,4     Ieee PD
            m = p1.match(line)
            if m:
                group = m.groupdict()
                intf = Common.convert_intf_name(group.pop('intf'))
                intf_dict = ret_dict.setdefault('interface', {}).setdefault(intf, {})
                intf_dict['allocated_power'] = float(group.pop('allocated_power'))
                intf_dict['utilized_power'] = float(group.pop('utilized_power'))
                intf_dict['admin_state'] = group.pop('admin_state')
                intf_dict['oper_state'] = group.pop('oper_state')
                intf_dict['type'] = group.pop('type')
                intf_dict['class'] = group.pop('class')
                intf_dict['device'] = group.pop('device')
                intf_dict.update({k: v for k, v in group.items() if 'n/a' not in v})
                continue

        return ret_dict
