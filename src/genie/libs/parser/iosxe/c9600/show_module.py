import re
import logging
from collections import OrderedDict
import xml.etree.ElementTree as ET
from xml.dom import minidom

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional, Use
from genie.libs.parser.utils.common import Common
# genie.parsergen
try:
    import genie.parsergen
except (ImportError, OSError):
    pass

# pyATS
from pyats.utils.exceptions import SchemaTypeError

log = logging.getLogger(__name__)


class ShowModuleSchema(MetaParser):
    """Schema for show module"""
    schema = {
        Optional('switch'): {
            Any(): {
                'port': str,
                'model': str,
                'serial_number': str,
                'mac_address': str,
                'hw_ver': str,
                'sw_ver': str
            },
        },
        'module':{
            int:{
                'ports':int,
                'card_type':str,
                'model':str,
                'serial':str,
            }
        },
        'status':{
            str:{ 
                'mac_address': str,           
                'hw':str,
                'fw':str,
                'sw':str,
                'status':str,
            }
        },
        'sup':{
            Any(): {              
                'operating_redundancy_mode':str,
                'configured_redundancy_mode':str,
            }    
        },
        
        Optional('number_of_mac_address'):int,
        Optional('chassis_mac_address_lower_range'):str,
        Optional('chassis_mac_address_upper_range'):str,
    }


class ShowModule(ShowModuleSchema):
    """Parser for show module"""

    cli_command = 'show module'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        # initial return dictionary
        switch_dict=ret_dict={}
        #initial regex pattern
        p1=re.compile(r'^(?P<switch>\d+) *'
                        '(?P<port>\w+) +'
                        '(?P<model>[\w\-]+) +'
                        '(?P<serial_number>\w+) +'
                        '(?P<mac_address>[\w\.]+) +'
                        '(?P<hw_ver>\w+) +'
                        '(?P<sw_ver>[\w\.]+)$')
              
	#Chassis Type: C9606R              

        #Mod Ports Card Type                                   Model          Serial No.
        #---+-----+--------------------------------------+--------------+--------------
        #1   48   48-Port 10GE / 25GE                         C9600-LC-48YL    FDO24170FSK
        #2   48   48-Port 10GE / 25GE                         C9600-LC-48YL    FDO24170FQV
        #3   0    Supervisor 1 Module                         C9600-SUP-1      CAT2239L096
        #4   0    Supervisor 1 Module                         C9600-SUP-1      FDO25460SGH
        #5   24   24-Port 40GE/12-Port 100GE                  C9600-LC-24C     FDO253115DY
        #6   24   24-Port 40GE/12-Port 100GE                  C9600-LC-24C     FDO241609F5
        
        p2=re.compile(r'^(?P<mod>\d+) *(?P<ports>\d+) +(?P<card_type>.*) +(?P<model>\S+) +(?P<serial>\S+)$')
        
        #Mod MAC addresses                    Hw   Fw           Sw                 Status
        #---+--------------------------------+----+------------+------------------+--------
        #1   AC4A.67AA.CE80 to AC4A.67AA.CEFF 2.0  17.7.1r[FC3]  17.03.01           ok         
        #2   AC4A.67AA.CB00 to AC4A.67AA.CB7F 2.0  17.7.1r[FC3]  17.03.01           ok         
        #3   70B3.171E.EB00 to 70B3.171E.EB7F 0.8  17.7.1r[FC3]  17.03.01           ok         
        #4   E069.BA16.0C80 to E069.BA16.0CFF 2.6  17.7.1r[FC3]  17.03.01           ok         
        #5   A478.0633.5D80 to A478.0633.5DFF 2.0  17.7.1r[FC3]  17.03.01           ok         
        #6   AC7A.5650.1A00 to AC7A.5650.1A7F 2.0  17.7.1r[FC3]  17.03.01           ok
        
        p3=re.compile(r'^(?P<mod>\d .* +)(?P<mac_address>[\w\.]+) .*(?P<hw>\d+.?\d+?) +(?P<fw>\S+) +(?P<sw>\S+) +(?P<status>\S+)$')
    
        #Mod Redundancy Role     Operating Redundancy Mode Configured Redundancy Mode
        #---+-------------------+-------------------------+---------------------------
        #3   Standby             sso                       sso                       
        #4   Active              sso                       sso   
    
        p4=re.compile(r'^\d+ *(?P<redundancy_role>\S+) *(?P<operating_redundancy_mode>\S+) *(?P<configured_redundancy_mode>\S+)$')
        
        #Chassis MAC address range: 64 addresses from 6cb2.ae4a.5540 to 6cb2.ae4a.557f 
        	
        p5=re.compile(r'^Chassis MAC address range: (?P<number_of_mac_address>\d+) addresses from (?P<chassis_mac_address_lower_range>.*) to (?P<chassis_mac_address_upper_range>.*)$')
        for line in out.splitlines():
            line = line.strip()
            m = p1.match(line)
            if m:
                group = m.groupdict()
                switch = group.pop('switch')
                switch_dict = ret_dict.setdefault('switch', {}).setdefault(switch, {})
                switch_dict.update({k: v.lower() for k, v in group.items()})
                switch_dict=ret_dict
                continue
            m = p2.match(line)
            if m:
                group = m.groupdict()
                switch = group.pop('mod')
                switch_dict = ret_dict.setdefault('module', {}).setdefault(int(switch), {})
                switch_dict.update({k: v.strip() for k, v in group.items()})
                switch_dict['ports']=int(group['ports'])
                switch_dict=ret_dict
                continue
            m=p3.match(line)
            if m:
                group = m.groupdict()
                switch = group.pop('mod')
                switch_dict = ret_dict.setdefault('status', {}).setdefault(str(switch), {})            
                switch_dict.update({k: v.strip() for k, v in group.items()})
                switch_dict=ret_dict
                continue
            m=p4.match(line)
            if m:
                group = m.groupdict()
                switch = group.pop('redundancy_role')
                switch_dict = ret_dict.setdefault('sup', {}).setdefault(str(switch), {})
                switch_dict.update({k: v.lower().strip() for k, v in group.items()})
                switch_dict=ret_dict
                continue
            m=p5.match(line)
            if m:
                group=m.groupdict()
                ret_dict.update({k: v.lower().strip() for k, v in group.items()})
                ret_dict['number_of_mac_address'] = int(group['number_of_mac_address'])
                switch_dict=ret_dict
                continue
        return switch_dict
