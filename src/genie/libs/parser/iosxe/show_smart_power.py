''' show_smartpower.py

IOSXE parsers for the following show commands:
    * show smartpower usage
    * show smartpower children
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.libs.parser.utils.common import Common
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional


class ShowSmartPowerUsageSchema(MetaParser):
    """ schema for show smart power version """
    schema = {
        "switches": {
            Any(): {
                Optional("usage"): float,
                Optional("category"): str,
                Optional("caliber"): str
            },
        } 
    }

class ShowSmartPowerUsage(ShowSmartPowerUsageSchema):
    """Parser for show smartpower usage"""

    cli_command = 'show smartpower usage'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # initial return dictionary
        ret_dict = {}
        # Interface   Name          Usage      Category  Caliber
        #  ---------   ----         -----      --------  -------
        # switch-1                 30.0 (W)  consumer  actual
        # switch-2                 213.0(W)   consumer  actual
        # switch-3                 213.0(W)   consumer  actual
        # switch-4                 30.0 (W)   consumer  actual
        
        # switch-1                 30.0 (W)  consumer  actual
        p1 = re.compile(r'^switch-(?P<switch>\d+)+\s+(?P<usage>[\S\s]+)\s+(?P<category>\w+)\s+(?P<caliber>\w+)$')
        for line in output.splitlines():
            line = line.strip()

            # switch-1                 30.0 (W)  consumer  actual
            m = p1.match(line)
            if m:
                group = m.groupdict()
                result_dict = ret_dict.setdefault('switches', {})
                switch=int(group['switch'])
                result_dict[switch] = {
                    'usage': float(group['usage'].split('(')[0].strip()),
                    'category': group['category'],
                    'caliber': group['caliber']
                }
                continue

        return ret_dict


class ShowSmartPowerChildrenSchema(MetaParser):
    """ schema for show smart power version """
    schema = {
        Or("interfaces", "device_models"): {
            Any(): {
                Optional("interface"): str,
                Optional("role"): str,
                Optional("name"): str,
                Optional("usage"): str,
                Optional("category"): str,
                Optional("level"): str,
                Optional("imp"): str,
                Optional("type"): str,
            },
            Optional("consumer"): float,
            Optional("meter"): float,
            Optional("producer"): float,
            Optional("total"): float,
            Optional("count"): int
        },
    }
    

class ShowSmartPowerChildren(ShowSmartPowerChildrenSchema):
    """Parser for show smartpower children"""

    cli_command = 'show smartpower children'

    def cli(self, output=None):
        if output is None:
            #execute command to get output
            output = self.device.execute(self.cli_command)
        # initial return dictionary
        ret_dict = {}
        # Module/
        # Interface   Role              Name                  Usage      Category  Lvl   Imp  Type
        # ---------   ----              ----                  -----      --------  ---   ---  ----
        # Tw1/0/1     IP Phone 9971     SEP10BD18DD4A19       8.0   (W)  consumer  10    1    PoE
        # C9300-48UXM       Peer1-topo1-ott-1     92.0  (W)  consumer  10    1    parent
        # Te2/0/2     IP Phone 9971     SEP08CC6830C3B1       7.7   (W)  consumer  10    1    PoE
        # C9300X-24HX       Peer1-topo1-ott-2     110.0 (W)  consumer  10    1    parent
        # Gi3/0/20    IP Phone 7960     SEP001C58D5C981       2.0   (W)  consumer  10    1    PoE
        # C9300-24P         Peer1-topo1-ott-3     99.0  (W)  consumer  10    1    parent
        # Subtotals: (Consumer: 424.7 (W), Meter: 0.0 (W), Producer: 0.0 (W))
        # Total: 424.7 (W), Count: 20
        

        # Tw1/0/1     IP Phone 9971     SEP10BD18DD4A19       8.0   (W)  consumer  10    1    PoE
        p1 = re.compile(r'^(?P<interface>\S+)\s+(?P<role>IP Phone.*\d+)\s+(?P<name>\w+)\s+(?P<usage>[\S\s]+)\s+(?P<category>\w+)\s+(?P<level>\d+)\s+(?P<imp>\d+)\s+(?P<type>\w+)$')

        # Subtotals: (Consumer: 424.7 (W), Meter: 0.0 (W), Producer: 0.0 (W))
        p2 = re.compile(r'^Subtotals: \(Consumer: (?P<consumer>[\S\s]+)\s+Meter: (?P<meter>[\S\s]+)\s+Producer: (?P<producer>[\S\s]+)$')

        # Total: 424.7 (W), Count: 20
        p3 = re.compile(r'^Total: (?P<total>[\S\s]+)\s+Count: (?P<count>[\S\s]+)$')

        # C9300X-24HX       Peer1-topo1-ott-2     110.0 (W)  consumer  10    1    parent
        p4 = re.compile(r'^(?P<role>[\w\-]+)\s+(?P<name>\S+)\s+(?P<usage>[\S\s]+)\s+(?P<category>\w+)\s+(?P<level>\d+)\s+(?P<imp>\d+)\s+(?P<type>\w+)$')
        for line in output.splitlines():
            line = line.strip()
            
            # Tw1/0/1     IP Phone 9971     SEP10BD18DD4A19       8.0   (W)  consumer  10    1    PoE
            m = p1.match(line)
            if m:
                group = m.groupdict()
                result_dict=ret_dict.setdefault('interfaces', {})
                interface=Common.convert_intf_name(group['interface'])
                result_dict[interface]={}
                result_dict[interface].update({ 
                    'interface': Common.convert_intf_name(group.pop('interface')),
                    'role': group['role'].strip(),
                    'name': group['name'],
                    'usage': group['usage'].split('(')[0].strip(),
                    'category': group['category'],
                    'level': group['level'],
                    'imp': group['imp'],
                    'type': group['type']
                })
                continue  
            
            # Subtotals: (Consumer: 424.7 (W), Meter: 0.0 (W), Producer: 0.0 (W))
            m = p2.match(line)
            if m:
                group = m.groupdict()
                result_dict.update({
                    'consumer': float(group['consumer'].split(' ')[0].strip()),
                    'meter': float(group['meter'].split(' ')[0].strip()),
                    'producer': float(group['producer'].split(' ')[0].strip())
                })
                continue

            # Total: 424.7 (W), Count: 20
            m = p3.match(line)
            if m:
                group = m.groupdict()
                result_dict.update({
                    'total': float(group['total'].split(' ')[0].strip()),
                    'count': int(group['count'])
                })
                continue
            
            # C9300X-24HX       Peer1-topo1-ott-2     110.0 (W)  consumer  10    1    parent
            m = p4.match(line)
            if m:
                group = m.groupdict()
                result_dict=ret_dict.setdefault('device_models', {})
                usages=group['usage'].split('(')
                usages=usages[0].strip()
                result_dict[usages]={}
                result_dict[usages].update({
                    'usage': usages,
                    'name': group['name'],
                    'role': group['role'],
                    'category': group['category'],
                    'level': group['level'],
                    'imp': group['imp'],
                    'type': group['type']
                })

                continue

        return ret_dict
    