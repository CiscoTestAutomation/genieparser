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
    * 'show stack-power detail'
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
        * show stack-power detail
    """

    schema = {
        'power_stack': {
            Any(): {
                'mode': str,
                'topology': str,
                'total_power': int,
                'reserved_power': int,
                'allocated_power': int,
                Optional('unused_power'): int,
                Optional('available_power'): int,
                'switch_num': int,
                'power_supply_num': int,
                Optional('power_stack_detail'):{  
                    'stack_mode': str,
                    'stack_topology': str,
                    'switch': {
                        Any(): {
                            'power_budget': int,
                            'power_allocated': int,
                            'low_port_priority_value': int,
                            'high_port_priority_value': int,
                            'switch_priority_value': int,
                            'port_1_status': str,
                            'port_2_status': str,
                            'neighbor_on_port_1': str,
                            'neighbor_on_port_2': str,
                        },
                    },
                },    
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

   
class ShowStackPowerDetail(ShowStackPowerSchema):
    """Parser for 
        * show stack-power detail
    """
    cli_command = ['show stack-power detail']
    
    def cli(self,output=None):
        if output is None:
            # get output from device
            out = self.device.execute(self.cli_command[0])
        else:
            out = output
                    
        ret_dict = {}
         
        # Powerstack-1                     SP-PS   Stndaln  1100    0       243     857       1    1  
        p1 = re.compile(r'^(?P<name>[\w\-]+) *'
                        r'(?P<mode>[\w\-]+) +'
                        r'(?P<topology>[\w\-]+) +'
                        r'(?P<total_power>\d+) +'
                        r'(?P<reserved_power>\d+) +'
                        r'(?P<allocated_power>\d+) +'
                        r'(?P<available_power>\d+) +'
                        r'(?P<switch_num>\d+) +'
                        r'(?P<power_supply_num>\d+)$')

        #Power stack name: Powerstack-1
        p2 = re.compile(r"^Power+\s+stack+\s+name:+\s+(?P<name>[\w\-]+)$")

        # Stack mode: Power sharing 
        p3 = re.compile(r"^Stack+\s+mode:+\s+(?P<stack_mode>.*)$")

        # Stack topology: Standalone
        p4 = re.compile(r"^Stack+\s+topology:+\s+(?P<stack_topology>[\w\-]+)$")
        
        # Switch 1 
        p5 = re.compile(r"^Switch+\s+\d")
        
        # Power budget: 1100
        p6= re.compile(r"^Power+\s+budget:+\s+(?P<power_budget>\d+)$")
        
        # Power allocated: 243
        p7 = re.compile(r"^Power+\s+allocated:+\s+(?P<power_allocated>\d+)$")
                
        # Low port priority value: 22
        p8 = re.compile(r"^Low+\s+port+\s+priority+\s+value:+\s+(?P<low_port_priority_value>\d+)$")
                
        # High port priority value: 13
        p9 = re.compile(r"^High+\s+port+\s+priority+\s+value:+\s+(?P<high_port_priority_value>\d+)$")
        
        # Switch priority value: 4
        p10 = re.compile(r"^Switch+\s+priority+\s+value:+\s+(?P<switch_priority_value>\d+)$")    
        
        # Port 1 status: Not connected
        p11 = re.compile(r"^Port+\s+1+\s+status:+\s+(?P<port_1_status>.*)$")
        
        #Port 2 status: Not connected
        p12 = re.compile(r"^Port+\s+2+\s+status:+\s+(?P<port_2_status>.*)$")
        
        # Neighbor on port 1: 0000.0000.0000
        p13 = re.compile(r"^Neighbor+\s+on+\s+port+\s+1:+\s+(?P<neighbor_on_port_1>.*)$")
        
        # Neighbor on port 2: 0000.0000.0000
        p14 = re.compile(r"^Neighbor+\s+on+\s+port+\s+2:+\s+(?P<neighbor_on_port_2>.*)$")


        for line in out.splitlines():
            line = line.strip()    
            
            # Powerstack-1                     SP-PS   Stndaln  1100    0       243     857       1    1  
            if p1.match(line):
                m = p1.match(line)
                group = m.groupdict()
                name = group.pop('name')
                stack_dict_1 = ret_dict.setdefault('power_stack', {})\
                                    .setdefault(name, {})
                stack_dict_1['mode'] = group.pop('mode')
                stack_dict_1['topology'] = group.pop('topology')
                stack_dict_1.update({k:int(v) for k, v in group.items()})
                continue
            
            #Power stack name: Powerstack-1
            if p2.match(line):
                match = p2.match(line)
                power_stack_name = match.group(1)
                stack_dict_2 = ret_dict['power_stack'][power_stack_name]
                stack_dict_2.setdefault('power_stack_detail', {})
                stack_dict_3 = ret_dict['power_stack'][power_stack_name]['power_stack_detail']
                continue
            
            # Stack mode: Power sharing
            if p3.match(line):
                match = p3.match(line)
                stack_dict_3['stack_mode'] = match.group('stack_mode')
                continue

            # Stack topology: Standalone            
            if p4.match(line):
                match = p4.match(line)
                stack_dict_3['stack_topology'] = match.group('stack_topology')
                continue
            
             # Switch 1 
            if p5.match(line):
                match = p5.match(line)
                switch = match.group()
                switch = int(switch[-1])
                stack_dict_4 = ret_dict['power_stack'][power_stack_name]['power_stack_detail']
                stack_dict_4.setdefault('switch', {})\
                                    .setdefault(switch, {})
                stack_dict_5 = ret_dict['power_stack'][power_stack_name]['power_stack_detail']['switch'][switch]
                continue

            # Power budget: 1100
            if p6.match(line):
                match = p6.match(line)
                stack_dict_5['power_budget'] = int(match.group('power_budget'))
                continue

            # Power allocated: 243
            if p7.match(line):
                match = p7.match(line)
                stack_dict_5['power_allocated'] = int(match.group('power_allocated'))
                continue
                
            # Low port priority value: 22
            if p8.match(line):
                match = p8.match(line)
                stack_dict_5['low_port_priority_value'] = int(match.group('low_port_priority_value'))
                continue
                
            # High port priority value: 13
            if p9.match(line):
                match = p9.match(line)
                stack_dict_5['high_port_priority_value'] = int(match.group('high_port_priority_value'))
                continue
            
            # Switch priority value: 4
            if p10.match(line):
                match = p10.match(line)
                stack_dict_5['switch_priority_value'] = int(match.group('switch_priority_value'))
                continue

            # Port 1 status: Not connected   
            if p11.match(line):
                match = p11.match(line)
                stack_dict_5['port_1_status'] = match.group('port_1_status')
                continue
                
            #Port 2 status: Not connected
            if p12.match(line):
                match = p12.match(line)
                stack_dict_5['port_2_status'] = match.group('port_2_status')
                continue
                
            # Neighbor on port 1: 0000.0000.0000
            if p13.match(line):
                match = p13.match(line)
                stack_dict_5['neighbor_on_port_1'] = match.group('neighbor_on_port_1')
                continue
                
            # Neighbor on port 2: 0000.0000.0000
            if p14.match(line):
                match = p14.match(line)
                stack_dict_5['neighbor_on_port_2'] = match.group('neighbor_on_port_2')
                continue
        
        return ret_dict
