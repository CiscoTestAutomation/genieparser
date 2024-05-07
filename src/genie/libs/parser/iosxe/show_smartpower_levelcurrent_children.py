''' show_smartpower.py

IOSXE parsers for the following show commands:
    * show smartpower current
    * show smartpower current level
'''

# Python
import re
# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional

class ShowSmartPowerLevelCurrentChildrenSchema(MetaParser):
    """ schema for show smart power version """
    schema = {
        'interfaces': {
            Any(): {
                Optional('interface'): str,
                Optional('name'): str,
                Optional('level'): int,
                Optional('value'): float,
            },
        },
        'models': {
            Any(): {
                Optional('name'): str,
                Optional('level'): int,
                Optional('value'): float,
            },
        },
    }
    
class ShowSmartPowerLevelCurrentChildren(ShowSmartPowerLevelCurrentChildrenSchema):
    """Parser for show smartpower level current children"""

    cli_command = 'show smartpower level current children'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # initial return dictionary
        ret_dict = {}
        # Interface   Name                     Level  Value
        # ---------   ----                     -----  ----- 
        # Te1/0/48    Te1.0.48                 10     60.0  (W)  
        #             Peer1-topo1-ott-1        10     545.0 (W)  
        # Te2/0/9     SEPC40ACBE062FF          10     24.5  (W)  
        #             Peer1-topo1-ott-2        10     0.0   (W)  
        
        # Te1/0/48    Te1.0.48                 10     60.0  (W)  
        p1 = re.compile(r'^(?P<interface>\S+)\s+(?P<name>\S+)\s+(?P<level>\d+)\s+(?P<value>[\S\s]+)$')

        #             Peer1-topo1-ott-1        10     545.0 (W) 
        p2 = re.compile(r'^(?P<name>\S+)\s+(?P<level>\d+)\s+(?P<value>[\S\s]+)$')
        for line in output.splitlines():
            line = line.strip()

            # Te1/0/48    Te1.0.48                 10     60.0  (W)
            m = p1.match(line)
            if m:
                group = m.groupdict()
                result_dict=ret_dict.setdefault('interfaces', {})
                interface=group['interface']
                result_dict[interface]={}
                result_dict[interface]['interface']=group['interface']
                result_dict[interface]['name']=group['name']
                result_dict[interface]['level']=int(group['level'])
                value=group['value'].split('(')
                value=value[0].strip()
                result_dict[interface]['value']=float(value)
                continue  

            #             Peer1-topo1-ott-2        10     0.0   (W) 
            m = p2.match(line)
            if m:
                group = m.groupdict()
                result_dict=ret_dict.setdefault('models', {})
                model=group['name']
                result_dict[model]={}
                result_dict[model]['name']=group['name']
                result_dict[model]['level']=int(group['level'])
                value=group['value'].split('(')
                value=value[0].strip()
                result_dict[model]['value']=float(value)
                continue

        return ret_dict
