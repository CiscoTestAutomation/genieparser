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
    * 'show power inline consumption'
    * 'show power inline consumption {interface}'
    * 'show power'
    * 'show power {detail}'
"""

import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional,Or

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
                        'power_supply_a': Or(int, float),
                        'power_supply_b' : Or(int, float),
                        'power_budget': Or(int, float),
                        'allocated_power': Or(int, float),
                        'available_power': Or(int, float),
                        'consumed_power_sys': Or(int, float),
                        'consumed_power_poe': Or(int, float),
                    },
                },
            },
        },
        Optional('totals'): {
            'total_allocated_power': Or(int, float),
            'total_available_power': Or(int, float),
            'total_consumed_power_sys': Or(int, float),
            'total_consumed_power_poe': Or(int, float),
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
        # 1   Powerstack-1         350      0      235       235.0      0.0     136/0.0
        p2 = re.compile(r'^(?P<switch_num>\d+) +'
                        r'(?P<name>[\w-]+) *'
                        r'(?P<power_supply_a>\d+) +'
                        r'(?P<power_supply_b>\d+) +'
                        r'(?P<power_budget>\d+) +'
                        r'(?P<allocated_power>[\d.]+) +'
                        r'(?P<available_power>[\d.]+) +'
                        r'(?P<consumed_power_sys>[\d.]+)[ \/]+'
                        r'(?P<consumed_power_poe>[\d.]+)$')

        # Totals:                               1150    1050      310/0
        # Totals:                               235.0   0.0       136/0.0
        p3 = re.compile(r'^Totals: +'
                        r'(?P<total_allocated_power>[\d.]+) +'
                        r'(?P<total_available_power>[\d.]+) +'
                        r'(?P<total_consumed_power_sys>[\d.]+)[ \/]+'
                        r'(?P<total_consumed_power_poe>[\d.]+)$')

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
            # 1   Powerstack-1         350      0      235       235.0      0.0     136/0.0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                stack_name = group.pop('name')
                switch_num = group.pop('switch_num')
                switch_dict = ret_dict.setdefault('power_stack', {})\
                                      .setdefault(stack_name, {})\
                                      .setdefault('switches', {})\
                                      .setdefault(int(switch_num), {})
                switch_dict.update({k:int(v) if v.isdigit() else float(v) 
                    for k, v in group.items()})
                continue

            # Totals:                               1150    1050      310/0
            # Totals:                               235.0   0.0       136/0.0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                total_dict = ret_dict.setdefault('totals', {})
                total_dict.update({k:int(v) if v.isdigit() else float(v) 
                    for k, v in group.items()})
                continue

        return ret_dict


class ShowStackPowerBudgeting(ShowStackPower):
    """Parser for 
        * show stack-power budgeting
    """

    cli_command = ['show stack-power budgeting']

    def cli(self,output=None):
        if output is None:
            output = self.device.execute(self.cli_command[0])

        return super().cli(output=output)


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
        # Gi1/0/13  auto   on         15.4    AIR-CAP2602I-A-K9   3     30.0
        p1a = re.compile(r'^(?P<intf>[\w\-\/\.]+)\s*'
                        r'(?P<admin_state>\w+)\s+'
                        r'(?P<oper_state>[\w\-]+)\s+'
                        r'(?P<power>\d+\.\d+)\s+'
                        r'(?P<device>(?=\S).*(?<=\S))\s+'
                        r'(?P<class>[\w\/]+)\s+'
                        r'(?P<max>\d+\.\d+)$')

        # alternate regexp pattern
        # Gi1/46    auto   on         27.5       26.1       AIR-AP2802I-B-K9    4
        p1b = re.compile(r'^(?P<intf>[\w\-\/\.]+)\s*'
                        r'(?P<admin_state>\w+)\s+'
                        r'(?P<oper_state>[\w\-]+)\s+'
                        r'(?P<max>\d+\.\d+)\s+'
                        r'(?P<power>\d+\.\d+)\s+'
                        r'(?P<device>(?=\S).*(?<=\S))\s+'
                        r'(?P<class>[\w\/]+)$')

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
            m = p1a.match(line)
            if m:
                group = m.groupdict()
                intf = Common.convert_intf_name(group.pop('intf'))
                intf_dict = ret_dict.setdefault('interface', {}).setdefault(intf, {})
                intf_dict['power'] = float(group.pop('power'))
                intf_dict['max'] = float(group.pop('max'))
                intf_dict.update({k: v for k, v in group.items() if 'n/a' not in v})
                continue

            # Gi1/46    auto   on         27.5       26.1       AIR-AP2802I-B-K9    4
            m = p1b.match(line)
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
                Optional('oper_priority'): str,
            },
        },
        Optional('power_inline_auto_shutdown'): str,
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
        
        # Te2/0/48   auto   on         n/a        1
        p1a = re.compile(r'^(?P<intf>[\w\/]+)\s+'
                        r'(?P<admin_state>auto|off|static)\s+'
                        r'(?P<oper_state>\w+)\s+'
                        r'(?P<admin_priority>[\w\/]+)\s+'
                        r'(?P<oper_priority>[\w]+)$')
        
        p2 = re.compile(r'^Power\s+inline\s+auto\s+shutdown:\s+(?P<power_inline_auto_shutdown>[\w]+)$')

        for line in out.splitlines():
            line = line.strip()

            #Gi1/0/1    auto   off        low
            m = p1.match(line)
            if m:
                group = m.groupdict()
                intf = Common.convert_intf_name(group.pop('intf'))
                intf_dict = ret_dict.setdefault('interface', {}).setdefault(intf, {})
                intf_dict.update(group)
                continue
            
            m = p1a.match(line)
            if m:
                group = m.groupdict()
                intf = Common.convert_intf_name(group.pop('intf'))
                # intf = group.pop('intf')
                intf_dict = ret_dict.setdefault('interface', {}).setdefault(intf, {})
                intf_dict.update(group)
                continue
            
            m = p2.match(line)
            if m:
                ret_dict['power_inline_auto_shutdown'] = m.groupdict()['power_inline_auto_shutdown']
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

        # Gi1/0/3     auto   n/a  off           0.0       0.0       n/a             
        # Gi1/0/4     auto   SP   on            4.0       3.8       1       Ieee PD
        # Gi1/0/15    auto   SS   on,on         60.0      10.5      6       Ieee PD
        # Gi1/0/23    auto   DS   on,on         45.4      26.9      3,4     Ieee PD
        p1 = re.compile(r'^(?P<intf>[\w\/]+)\s+(?P<admin_state>[a-zA-Z]+)\s+(?P<type>[\w\/]+)\s+(?P<oper_state>[\,\w+]+)\s+(?P<allocated_power>[\d\.]+)\s+(?P<utilized_power>[\d\.]+)\s+(?P<class>[\w\,\/]+)\s+(?P<device>.*)$')

        for line in out.splitlines():
            line = line.strip()
  
            # Gi1/0/3     auto   n/a  off           0.0       0.0       n/a             
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

class ShowPowerInlineConsumptionSchema(MetaParser):
    """
    Schema for 
        show power inline consumption 
        show power inline consumption  {interface} 
    """
    schema = {
        'interface': {
            Any(): {
                'consumption_configured': str, 
                'admin_consumption': float  
            },
        },
        Optional('consumption'): {
            Any(): {
                'consumption_configured': str, 
                'admin_consumption': float 
            }
        }
    
    }


class ShowPowerInlineConsumption(ShowPowerInlineConsumptionSchema):
    """Parser for show power inline consumption 
                  show power inline consumption <interface> """

    cli_command = ['show power inline consumption','show power inline consumption {interface}']

    def cli(self, interface='', output=None):
        if output is None:
            if interface:
                cmd = self.cli_command[1].format(interface=interface)
            else:
                cmd = self.cli_command[0]

            # get output from device
            output = self.device.execute(cmd)

        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern
        p1 = re.compile(r'^(?P<intf>[\w\-\/\.]+)\s*'
                         '(?P<consumption_configured>\w+)\s+'
                         '(?P<admin_consumption>[\d\.]+)$')
        
        

        for line in output.splitlines():
            line = line.strip()
        
            # Interface  Consumption      Admin             
            #            Configured    Consumption (Watts)  
            # ---------- -----------  -------------------   
            # Gi1/3          NO                 0.0
    
            m = p1.match(line)
            if m:
                group = m.groupdict()
                intf = Common.convert_intf_name(group.pop('intf'))
                intf_dict = ret_dict.setdefault('interface', {}).setdefault(intf, {})
                intf_dict['consumption_configured'] = str(group.pop('consumption_configured'))
                intf_dict['admin_consumption'] = float(group.pop('admin_consumption'))
                intf_dict.update({k: v for k, v in group.items() if 'n/a' not in v})
            

        # Remove statistics if we don't have any interfaces
        if 'interface' not in ret_dict and 'consumption' in ret_dict:
            ret_dict.pop('consumption', None)

        return ret_dict

# ===============================================================================
# Schema for :
#      * 'show power'
#      * 'show power {detail}'
# ===============================================================================
class ShowPowerSchema(MetaParser):
    """Schema for :
        * show power
        * show power {detail}
    """
    
    schema = {
        'switch': {
            Any(): {
                'power_supply': {
                    Any(): {
                        'model_no' : str,
                        'type' : str,
                        'capacity' : str,
                        'status' : str,
                        'fan_state_0' : str,
                        'fan_state_1' : str,
                    },
                },
                'fan_tray': {
                    Any(): {
                        'status' : str,
                        'fan_state_0' : str,
                        'fan_state_1' : str,
                    },
                }
            },
        }
    }

# ===============================================================================
# Parser for :
#    * 'show power'
#    * 'show power {detail}'
# ===============================================================================
class ShowPower(ShowPowerSchema):
    """parser for :
         * show power
         * show power {detail}
    """
    
    cli_command = ['show power', 'show power {detail}']

    def cli(self, detail="", output=None):
        
        if output == None:
            if detail:
                output = self.device.execute(self.cli_command[1].format(detail=detail))
            else :
                output = self.device.execute(self.cli_command[0])

        result_dict = {}

        #Switch:1
        p1 = re.compile(r'^Switch:(?P<switch>\S+)$')

        #PS1     C9K-PWR-1500WAC-R     ac    n.a.      bad-input  n.a.  n.a. 
        #PS2     C9K-PWR-1500WAC-R     ac    1500 W    active     good  n.a.
        p2 = re.compile(r'^(?P<power_supply>\S+) +'
                        r'(?P<model_no>\S+) +'
                        r'(?P<type>\S+) +'
                        r'(?P<capacity>\S+) +W?\s*'
                        r'(?P<status>\S+) +'
                        r'(?P<fan_state_0>\S+) +'
                        r'(?P<fan_state_1>\S+)$')

        #FT1     active      good  good
        p3 = re.compile(r'^(?P<fan_tray>\S+) +'
                        r'(?P<status>\S+) +'
                        r'(?P<fan_state_0>\S+) +'
                        r'(?P<fan_state_1>\S+)$')

        for line in output.splitlines():
            line = line.strip()

            #Switch:1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                switch = group['switch']
                switch_dict = result_dict.setdefault('switch',{})
                switch_id_dict = switch_dict.setdefault(switch,{})
                continue

            #PS1     C9K-PWR-1500WAC-R     ac    n.a.      bad-input  n.a.  n.a. 
            #PS2     C9K-PWR-1500WAC-R     ac    1500 W    active     good  n.a.
            m = p2.match(line)
            if m:
                group = m.groupdict()
                power_supply = group['power_supply']
                power_supply_dict = switch_id_dict.setdefault('power_supply',{})
                power_supply_unit_dict = power_supply_dict.setdefault(power_supply,{})
                power_supply_unit_dict.update({
                    'model_no' : group['model_no'],
                    'type' : group['type'],
                    'capacity' : group['capacity'],
                    'status' : group['status'],
                    'fan_state_0' : group['fan_state_0'],
                    'fan_state_1' : group['fan_state_1'],
                })
                continue

            #FT1     active      good  good
            m = p3.match(line)
            if m:
                group = m.groupdict()
                fan_tray = group['fan_tray']
                if fan_tray == "Tray":
                    # don't store in the key 'Tray' as it is just the header of the table
                    continue
                fan_tray_dict = switch_id_dict.setdefault('fan_tray',{})
                fan_tray_unit_dict = fan_tray_dict.setdefault(fan_tray,{})
                fan_tray_unit_dict.update({
                    'status' : group['status'],
                    'fan_state_0' : group['fan_state_0'],
                    'fan_state_1' : group['fan_state_1'],
                })
                continue
        return result_dict


class ShowPowerInlineUpoePlusModuleSchema(MetaParser):
    """Schema for show power inline upoe-plus module {mod_num}"""
    schema = {
        'module':{
            int:{
                'available': float, 
                'used': float, 
                'remaining': float, 
                Optional('ieee_mode'): str,
            },
        },
        'interface': {
            Any(): {
                'admin_state': str,
                'type': str,
                'operating_state': str,
                'allocated_power': float,
                'utilized_power': float,
                'class': str,
                'device': str,
            },
        },
        'total':{
            'type':int,
            'operating_state':str,
            'allocated_power':float,
            'utilized_power':float,
        },
    }


class ShowPowerInlineUpoePlusModule(ShowPowerInlineUpoePlusModuleSchema):
    """Parser for show power inline upoe-plus module {mod_num}"""

    cli_command = 'show power inline upoe-plus module {mod_num}'

    def cli(self, mod_num, output=None):
        if output is None and mod_num:
                output = self.device.execute(self.cli_command.format(mod_num=mod_num))
                
        # initial return dictionary
        ret_dict = {}

        # 1           675.0        0.0       675.0
        p1 = re.compile(r'^(?P<module>\d+)\s+(?P<available>[\d\.]+)\s+(?P<used>[\d\.]+)\s+(?P<remaining>[\d\.]+)$')
        
        # Available:22565.0(w)  Used:244.7(w)  Remaining:22320.3(w)
        p1a = re.compile(r'^Available:(?P<available>[\d\.]+).*\s+Used:(?P<used>[\d\.]+).*\s+Remaining:(?P<remaining>[\d\.]+)')
        
        #Device IEEE Mode - BT
        p2 = re.compile(r'^Device IEEE Mode\s+\-\s+(?P<ieee_mode>\w+)$')
        
        #Gi1/0/1     auto   n/a  off           0.0       0.0       n/a
        p3 = re.compile(r'^(?P<intf>[\w\/]+)\s+(?P<admin_state>\w+)\s+(?P<type>[\w\/?]+)\s+(?P<operating_state>[\w,?]+)\s+(?P<allocated_power>[\d\.]+)\s+(?P<utilized_power>[\d\.]+)\s+(?P<class>[\w(\/,)?]+)(\s+(?P<device>.*))?')
        
        #Totals:            0    on          0.0      0.0
        p4 = re.compile(r'^Totals: +(?P<type>\d+) +(?P<operating_state>\w+) +(?P<allocated_power>[\d\.]+) +(?P<utilized_power>[\d\.]+)$')
        
        for line in output.splitlines():
            line = line.strip()
            
            # 1           675.0        0.0       675.0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                module = int(group.pop('module'))
                root_dict = ret_dict.setdefault('module', {}).setdefault(module, {})
                root_dict['available'] = float(group['available'])
                root_dict['used'] = float(group['used'])
                root_dict['remaining'] = float(group['remaining'])
                continue
            
            m = p1a.match(line)
            if m:
                group = m.groupdict()
                module = int(mod_num)
                root_dict = ret_dict.setdefault('module', {}).setdefault(module, {})
                root_dict['available'] = float(group['available'])
                root_dict['used'] = float(group['used'])
                root_dict['remaining'] = float(group['remaining'])
                continue
                
            #Device IEEE Mode - BT
            m = p2.match(line)
            if m:
                group = m.groupdict() 
                root_dict['ieee_mode'] = group['ieee_mode']
                continue
            
            #Gi1/0/1     auto   n/a  off           0.0       0.0       n/a
            m = p3.match(line)
            if m:
                group = m.groupdict()
                interface = Common.convert_intf_name(group.pop('intf'))
                if group['device']== None:
                    group['device']=""
                group['allocated_power'] = float(group['allocated_power'])
                group['utilized_power'] = float(group['utilized_power'])
                interface_dict = ret_dict.setdefault('interface', {}).setdefault(interface, {})
                interface_dict.update({k: v for k, v in group.items()})
                continue
                
            #Totals:            0    on          0.0      0.0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                totals_dict=ret_dict.setdefault('total', {})
                totals_dict['type'] = int(group['type'])
                totals_dict['operating_state']=group['operating_state']
                totals_dict['allocated_power'] = float(group['allocated_power'])
                totals_dict['utilized_power'] = float(group['utilized_power'])
                continue
                
        return ret_dict
    
    
class ShowPowerInlineDetailSchema(MetaParser):
    """Schema for show power inline {interface} detail"""
    schema = {
        'interface': {
            Any(): {
                'inline_power_mode': str,
                'operational_status': str,
                'device_detected': str,
                'device_type': str,
                Optional('connection_check'): str,
                'ieee_class': str,
                Optional('physical_assigned_class'): str,
                'discovery_mechanism': str,
                'police': str,
                'admin_value': float,
                'power_drawn': float,
                'power_available': float,
                Optional('allocated_power'): str,
                'measured_consumption': str,
                'max_consumption': float,
                'absent_counter': int,
                'over_curent_counter': int,
                'short_curent_counter': int,
                'invalid_signature_counter': int,
                'power_denied_counter': int,
                'power_negotiation_used': str,
                'power_type_to_pd': str,
                'power_type_from_pd': str,
                'power_source_to_pd': str,
                'power_source_from_pd': str,
                'power_priority_to_pd': str,
                'power_priority_from_pd': str,
                'requested_power_to_pd': str,
                'requested_power_from_pd': str,
                'allocated_power_to_pd': str,
                'allocated_power_from_pd': str,
                'four_pair_poe_supported': str,
                'spare_pair_power_enabled': str,
                'four_pair_pd_architecture': str,
                Optional('perpetual_poe_enabled'): str,
                Optional('fast_poe_enabled'): str,
            },
        },
    }
    
class ShowPowerInlineDetail(ShowPowerInlineDetailSchema):
    """Parser for show power inline <interface> detail"""

    cli_command = 'show power inline {interface} detail'

    def cli(self, interface='', output=None):
        if output is None:
            cmd = self.cli_command.format(interface=interface)
            output = self.device.execute(cmd)

        # initial return dictionary
        ret_dict = {}
        
        # Interface: Te2/0/41
        p1 = re.compile(r'^\s*Interface:\s+(?P<intf>[\w\-\/\.]+)$')

        # Inline Power Mode: auto
        p2 = re.compile(r'^\s*Inline\sPower\sMode:\s+(?P<inline_power_mode>\w+)$')

        # Operational status (Alt-A,B): on,off
        p3 = re.compile(r'^\s*Operational\s+status.*:\s+(?P<operational_status>[\w\,]+)$')

        # Device Detected: yes
        p4 = re.compile(r'^\s*Device\s+Detected:\s+(?P<device_detected>\w+)$')

        # Device Type: cisco AIR-AP1252G-A
        p5 = re.compile(r'^\s*Device\s+Type:\s+(?P<device_type>[\w\/\-\s]+)$')

        # Connection Check: SS
        p6 = re.compile(r'^\s*Connection\s+Check:\s+(?P<connection_check>[\w]+)$')

        # IEEE Class (Alt-A,B): 3
        p7 = re.compile(r'^\s*IEEE\s+Class.*:\s+(?P<ieee_class>[\w\,\/]+)$')

        # Physical Assigned Class (Alt-A,B): 3
        p8 = re.compile(r'^\s*Physical\s+Assigned\s+Class.*:\s+(?P<physical_assigned_class>[\w\,\/]*)$')

        # Discovery mechanism used/configured: Ieee and Cisco
        p9 = re.compile(r'^\s*Discovery\s+mechanism\s+used\/configured:\s+(?P<discovery_mechanism>[\w\s]+$)')

        # Police: off
        p10 = re.compile(r'^\s*Police:\s+(?P<police>[\w]+)$')

        # Power Allocated 
        # Admin Value: 90.0
        p11 = re.compile(r'^\s*Admin\s+Value:\s+(?P<admin_value>[\d\.]+)$')

        # Power drawn from the source: 0.0
        p12 = re.compile(r'^\s*Power\s+drawn\s+from\s+the\s+source:\s+(?P<power_drawn>[\d\.]+)$')

        # Power available to the device: 0.0
        p13 = re.compile(r'^\s*Power\s+available\s+to\s+the\s+device:\s+(?P<power_available>[\d\.]+)$')

        # Allocated Power (Alt-A,B): 0.0
        p14 = re.compile(r'^\s*Allocated\s+Power.*:\s+(?P<allocated_power>[\d\.\,]+)$')

        # Measured at the port(watts) (Alt-A,B): 10.0
        p15 = re.compile(r'^\s*Measured\s+at\s+the\s+port.*:\s+(?P<measured_consumption>[\d\.\,]+)$')

        # Maximum Power drawn by the device since powered on: 5.3
        p16 = re.compile(r'^\s*Maximum\s+Power\s+drawn.*:\s+(?P<max_consumption>[\d\.]+)$')

        #Absent Counter: 0
        p17 = re.compile(r'^\s*Absent\s+Counter:\s+(?P<absent_counter>[\d]+)$')

        # Over Current Counter: 0
        p18 = re.compile(r'^\s*Over\s+Current\s+Counter:\s+(?P<over_curent_counter>[\d]+)$')

        # Short Current Counter: 0
        p19 = re.compile(r'^\s*Short\s+Current\s+Counter:\s+(?P<short_curent_counter>[\d]+)$')

        # Invalid Signature Counter: 0
        p20 = re.compile(r'^\s*Invalid\s+Signature\s+Counter:\s+(?P<invalid_signature_counter>[\d]+)$')

        # Power Denied Counter: 0
        p21 = re.compile(r'^\s*Power\s+Denied\s+Counter:\s+(?P<power_denied_counter>[\d]+)$')

        # Power Negotiation Used: LLDP-MED
        p22 = re.compile(r'^\s*Power\s+Negotiation\s+Used:\s+(?P<power_negotiation_used>[\w\-\s\.]+)$')

        # Power Type:                  PSE                  PD
        # Power Type:                  Type 2 PSE           Type 2 PSE
        p23 = re.compile(r'^\s*Power\s+Type:\s+(?P<power_type_to_pd>[\w\-]+|Type\s\d\s[\w]+)\s{2,}(?P<power_type_from_pd>[\w\-]+|Type\s\d\s[\w]+)$')

        # Power Source:                Primary              PSE
        p24 = re.compile(r'^\s*Power\s+Source:\s+(?P<power_source_to_pd>[\w\-]+)\s+(?P<power_source_from_pd>[\w\-]+)$')

        # Power Priority:              critical             unknown
        p25 = re.compile(r'^\s*Power\s+Priority:\s+(?P<power_priority_to_pd>[\w\-]+)\s+(?P<power_priority_from_pd>[\w\-]+)$')

        # Requested Power(W):          -                    8.5
        p26 = re.compile(r'^\s*Requested\s+Power\(W\):\s+(?P<requested_power_to_pd>[\d\.\-]+)\s+(?P<requested_power_from_pd>[\d\.\-]+)$')

        # Allocated Power(W):          8.5                    -
        p27 = re.compile(r'^\s*Allocated\s+Power\(W\):\s+(?P<allocated_power_to_pd>[\d\.\-]+)\s+(?P<allocated_power_from_pd>[\d\.\-]+)$')

        # Four-Pair PoE Supported: Yes
        p28 = re.compile(r'^\s*Four\-Pair\s+PoE\s+Supported:\s+(?P<four_pair_poe_supported>[\w]+)$')

        # Spare Pair Power Enabled: No
        p29 = re.compile(r'^\s*Spare\s+Pair\s+Power\s+Enabled:\s+(?P<spare_pair_power_enabled>[\w]+)$')

        # Four-Pair PD Architecture: Shared
        p30 = re.compile(r'^\s*Four\-Pair\s+PD\s+Architecture:\s+(?P<four_pair_pd_architecture>[\w\/]+)$')

        # Perpetual POE Enabled: TRUE
        p31 = re.compile(r'^\s*Perpetual\s+POE\s+Enabled:\s+(?P<perpetual_poe_enabled>[\w]+)$')

        # Fast POE Enabled: FALSE
        p32 = re.compile(r'^\s*Fast\s+POE\s+Enabled:\s+(?P<fast_poe_enabled>[\w]+)$')
                
        for line in output.splitlines():
            line = line.strip()
            
            # Interface: Te2/0/41
            m = p1.match(line)
            if m:
                intf = Common.convert_intf_name(m.groupdict()['intf'])
                intf_dict = ret_dict.setdefault('interface', {}).setdefault(intf, {})
                continue
            
            # Inline Power Mode: auto
            m = p2.match(line)
            if m:
                intf_dict['inline_power_mode'] = m.groupdict()['inline_power_mode']
                continue
            
            # Operational status (Alt-A,B): on,off
            m = p3.match(line)
            if m:
                intf_dict['operational_status'] = m.groupdict()['operational_status']
                continue       
                    
            # Device Detected: yes
            m = p4.match(line)
            if m:
                intf_dict['device_detected'] = m.groupdict()['device_detected']
                continue
            
            # Device Type: cisco AIR-AP1252G-A
            m = p5.match(line)
            if m:
                intf_dict['device_type'] = m.groupdict()['device_type']
                continue
            
            # Connection Check: SS
            m = p6.match(line)
            if m:
                intf_dict['connection_check'] = m.groupdict()['connection_check']
                continue
            
            # IEEE Class (Alt-A,B): 3
            m = p7.match(line)
            if m:
                intf_dict['ieee_class'] = m.groupdict()['ieee_class']
                continue
            
            # Physical Assigned Class (Alt-A,B): 3
            m = p8.match(line)
            if m:
                intf_dict['physical_assigned_class'] = m.groupdict()['physical_assigned_class']
                continue
            
            # Discovery mechanism used/configured: Ieee and Cisco
            m = p9.match(line)
            if m:
                intf_dict['discovery_mechanism'] = m.groupdict()['discovery_mechanism']
                continue
            
            # Police: off
            m = p10.match(line)
            if m:
                intf_dict['police'] = m.groupdict()['police']
                continue
            
            # Power Allocated 
            # Admin Value: 90.0
            m = p11.match(line)
            if m:
                intf_dict['admin_value'] = float(m.groupdict()['admin_value'])
                continue
            
            # Power drawn from the source: 0.0
            m = p12.match(line)
            if m:
                intf_dict['power_drawn'] = float(m.groupdict()['power_drawn'])
                continue
            
            # Power available to the device: 0.0
            m = p13.match(line)
            if m:
                intf_dict['power_available'] = float(m.groupdict()['power_available'])
                continue
            
            # Allocated Power (Alt-A,B): 0.0
            m = p14.match(line)
            if m:
                intf_dict['allocated_power'] = m.groupdict()['allocated_power']
                continue
            
            # Measured at the port(watts) (Alt-A,B): 10.0
            m = p15.match(line)
            if m:
                intf_dict['measured_consumption'] = m.groupdict()['measured_consumption']
                continue
            
            # Maximum Power drawn by the device since powered on: 5.3
            m = p16.match(line)
            if m:
                intf_dict['max_consumption'] = float(m.groupdict()['max_consumption'])
                continue
            
            #Absent Counter: 0
            m = p17.match(line)
            if m:
                intf_dict['absent_counter'] = int(m.groupdict()['absent_counter'])
                continue
            
            # Over Current Counter: 0
            m = p18.match(line)
            if m:
                intf_dict['over_curent_counter'] = int(m.groupdict()['over_curent_counter'])
                continue
            
            # Short Current Counter: 0
            m = p19.match(line)
            if m:
                intf_dict['short_curent_counter'] = int(m.groupdict()['short_curent_counter'])
                continue
            
            # Invalid Signature Counter: 0
            m = p20.match(line)
            if m:
                intf_dict['invalid_signature_counter'] = int(m.groupdict()['invalid_signature_counter'])
                continue
            
            # Power Denied Counter: 0
            m = p21.match(line)
            if m:
                intf_dict['power_denied_counter'] = int(m.groupdict()['power_denied_counter'])
                continue
            
            # Power Negotiation Used: LLDP-MED
            m = p22.match(line)
            if m:
                intf_dict['power_negotiation_used'] = m.groupdict()['power_negotiation_used']
                continue
            
            # Power Type:                  PSE                  PD
            m = p23.match(line)
            if m:
                intf_dict['power_type_to_pd'] = m.groupdict()['power_type_to_pd']
                intf_dict['power_type_from_pd'] = m.groupdict()['power_type_from_pd']
                continue
            
            # Power Source:                Primary              PSE
            m = p24.match(line)
            if m:
                intf_dict['power_source_to_pd'] = m.groupdict()['power_source_to_pd']
                intf_dict['power_source_from_pd'] = m.groupdict()['power_source_from_pd']
                continue
            
            # Power Priority:              critical             unknown
            m = p25.match(line)
            if m:
                intf_dict['power_priority_to_pd'] = m.groupdict()['power_priority_to_pd']
                intf_dict['power_priority_from_pd'] = m.groupdict()['power_priority_from_pd']
                continue
            
            # Requested Power(W):          -                    8.5
            m = p26.match(line)
            if m:
                intf_dict['requested_power_to_pd'] = m.groupdict()['requested_power_to_pd']
                intf_dict['requested_power_from_pd'] = m.groupdict()['requested_power_from_pd']
                continue
            
            # Allocated Power(W):          8.5                    -
            m = p27.match(line)
            if m:
                intf_dict['allocated_power_to_pd'] = m.groupdict()['allocated_power_to_pd']
                intf_dict['allocated_power_from_pd'] = m.groupdict()['allocated_power_from_pd']
                continue
            
            # Four-Pair PoE Supported: Yes
            m = p28.match(line)
            if m:
                intf_dict['four_pair_poe_supported'] = m.groupdict()['four_pair_poe_supported']
                continue
            
            # Spare Pair Power Enabled: No
            m = p29.match(line)
            if m:
                intf_dict['spare_pair_power_enabled'] = m.groupdict()['spare_pair_power_enabled']
                continue
            
            # Four-Pair PD Architecture: Shared
            m = p30.match(line)
            if m:
                intf_dict['four_pair_pd_architecture'] = m.groupdict()['four_pair_pd_architecture']
                continue
            
            # Perpetual POE Enabled: TRUE
            m = p31.match(line)
            if m:
                intf_dict['perpetual_poe_enabled'] = m.groupdict()['perpetual_poe_enabled']
                continue
            
            # Fast POE Enabled: FALSE
            m = p32.match(line)
            if m:
                intf_dict['fast_poe_enabled'] = m.groupdict()['fast_poe_enabled']
                continue
            
        return ret_dict
    
class ShowPowerInlinePoliceSchema(MetaParser):
    """Schema for show power inline police """
    schema = {
        'interface': {
            Any(): {
                'admin_state': str,
                'oper_state': str,
                'admin_police': str,
                'oper_police': str,
                'cutoff_power': str,
                'oper_power': str,
            },
        },
    }


class ShowPowerInlinePolice(ShowPowerInlinePoliceSchema):
    """Parser for show power inline police
                  show power inline police <interface>"""

    cli_command = ['show power inline police', 'show power inline police {interface}']

    def cli(self, interface='', output=None):
        if output is None:
            if interface:
                cmd = self.cli_command[1].format(interface=interface)
            else:
                cmd = self.cli_command[0]

            # get output from device
            output = self.device.execute(cmd)

        # initial return dictionary
        ret_dict = {}

        # Te7/0/28  auto   on         log        overdrawn  15.4   16.0 
        # Te7/0/29  auto   on         none       n/a        n/a    n/a  
        p1 = re.compile(r'^(?P<intf>[\w\d\/]+)\s+(?P<admin_state>[\w]+)\s+(?P<oper_state>[\,\w]+)\s+(?P<admin_police>[\w]+)\s+(?P<oper_police>[\w\/]+)\s+(?P<cutoff_power>[\w\d\.\/]+)\s+(?P<oper_power>[\w\d\.\/]+)\s*$')

        for line in output.splitlines():
            line = line.strip()
  
            # Te7/0/28  auto   on         log        overdrawn  15.4   16.0 
            # Te7/0/29  auto   off         none       n/a        n/a    n/a  
            m = p1.match(line)
            if m:
                group = m.groupdict()
                intf = Common.convert_intf_name(group.pop('intf'))
                if intf == 'Interface':
                    continue
                intf_dict = ret_dict.setdefault('interface', {}).setdefault(intf, {})
                intf_dict.update(group)
                continue

        return ret_dict
