''' show_inventory.py

IOSXE parsers for the following show commands:
    * show inventory raw
    * show incentory OID
'''
# python
import re

# metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

class ShowInventoryRawSchema(MetaParser):

    """Schema for
        * show inventory Raw
    """
    schema = {    
        'name': {
            Any(): {
                'description':   str,
                Optional('pid'): str,
                Optional('vid'): str, 
                Optional('sn'):  str,
                Optional('oid'): str
            }       
        }
    }
 
class ShowInventoryRaw(ShowInventoryRawSchema): 

    """Parser for
        * show inventory Raw
    """
    cli_command = ['show inventory raw | include {include}',
                   'show inventory raw']

    def cli(self, include='',output=None): 
        
        if output is None:
            if include:
                output = self.device.execute(self.cli_command[0].format(include=include))
            else:
                output = self.device.execute(self.cli_command[1])
        
        ret_dict = {} 
        
        #NAME: "Chassis", DESCR: "Cisco Catalyst Series C9500X-28C8D Chassis"
        p1 = re.compile(r'^NAME: "(?P<name>[\w\d\s(\/\-)?]+)", DESCR: "(?P<description>[\w\d\s(\-\.)?]+)"$')
        
        #PID: C9500X-28C8D      , VID: V00  , SN: FDO25030SLN
        p2 = re.compile(r'^PID:(?P<pid>[\w\d\-\s]+), VID:(?P<vid>[\d\w\s(\.)?]+), SN: (?P<sn>[\w\d\-]+)$')
        
        #OID: 1.3.6.1.4.1.9.12.3.1.3.2421
        p3 = re.compile(r'^OID: +(?P<oid>[\d\.]+)$')
        
        for line in output.splitlines():
            line = line.strip()
            
            #NAME: "Chassis", DESCR: "Cisco Catalyst Series C9500X-28C8D Chassis"
            m = p1.match(line)
            if m: 
                group = m.groupdict()
                name = group['name']
                name_dict = ret_dict.setdefault('name', {}).setdefault(name, {})
                name_dict['description'] = group['description']
                continue
                
            #PID: C9500X-28C8D      , VID: V00  , SN: FDO25030SLN
            m = p2.match(line)
            if m:   
                group = m.groupdict()
                name_dict['pid'] = group['pid'].replace(' ','')
                name_dict['vid'] = group['vid'].replace(' ','')
                name_dict['sn'] = group['sn'] 
                continue    
                
            #OID: 1.3.6.1.4.1.9.12.3.1.3.2421
            m = p3.match(line)
            if m:
                name_dict['oid'] = m.groupdict()['oid']
                continue
                
        return ret_dict
        

class ShowInventoryOID(ShowInventoryRaw): 

    cli_command = 'show inventory OID'
    
    def cli(self, output=None): 
    
        if output is None:           
            output = self.device.execute(self.cli_command)
            
        return super().cli(output=output)
