'''show_platform.py

IOSXE c9606r parser for the following show command:
   * show platform hardware fed active fwd-asic resource tcam utilization
   * show platform hardware fed active fwd-asic resource tcam table pbr record 0 format 0 | begin {nat_region}
   * show ip nat translations
   
'''
# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional



class ShowPlatformHardwareFedActiveTcamUtilizationSchema(MetaParser):
    """Schema for show platform hardware fed active fwd-asic resource tcam utilization """
    schema = {
        'asic': {
            Any(): {
                'table': {
                    Any(): {
                        'subtype': {
                            Any(): {
                                'dir': {
                                    Any(): {
                                        'max': int,
                                        'used': int,
                                        'used_percent': str,
                                        'v4': int,
                                        'v6': int,
                                        'mpls': int,
                                        'other': int,
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    
class ShowPlatformHardwareFedActiveTcamUtilization(ShowPlatformHardwareFedActiveTcamUtilizationSchema):
    """Parser for show platform hardware fed active fwd-asic resource tcam utilization """

    cli_command = 'show platform hardware fed active fwd-asic resource tcam utilization'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern
        # CAM Utilization for ASIC  [0]
        p1 = re.compile(r'^CAM +Utilization +for +ASIC  +\[+(?P<asic>(\d+))\]$')

        #CTS Cell Matrix/VPN
        #Label                  EM           O       16384        0    0.00%        0        0        0        0
        #CTS Cell Matrix/VPN
        #Label                  TCAM         O        1024        1    0.10%        0        0        0        1
        # Mac Address Table      EM           I       16384       44    0.27%        0        0        0       44
        # Mac Address Table      TCAM         I        1024       21    2.05%        0        0        0       21
        p2 = re.compile(r'^(?P<table>.+?) +(?P<subtype>\S+) +(?P<dir>\S+) +(?P<max>\d+) +(?P<used>\d+) +(?P<used_percent>\S+\%) +(?P<v4>\d+) +(?P<v6>\d+) +(?P<mpls>\d+) +(?P<other>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            # CAM Utilization for ASIC  [0]
            m = p1.match(line)
            if m:
                group = m.groupdict()
                asic = group['asic']
                asic_dict = ret_dict.setdefault('asic', {}).setdefault(asic, {})
                continue

            #CTS Cell Matrix/VPN
            #Label                  EM           O       16384        0    0.00%        0        0        0        0
            #CTS Cell Matrix/VPN
            #Label                  TCAM         O        1024        1    0.10%        0        0        0        1
            # Mac Address Table      EM           I       16384       44    0.27%        0        0        0       44
            # Mac Address Table      TCAM         I        1024       21    2.05%        0        0        0       21
            m = p2.match(line)
            if m:
                group = m.groupdict()
                table_ = group.pop('table').lower().replace(' ','_')
                if table_ == 'label':
                    table_ = 'cts_cell_matrix_vpn_label'
                subtype_ = group.pop('subtype').lower().replace('/','_')
                dir_ = group.pop('dir').lower()
                dir_dict = asic_dict.setdefault('table', {}). \
                            setdefault(table_, {}). \
                            setdefault('subtype', {}). \
                            setdefault(subtype_, {}). \
                            setdefault('dir', {}). \
                            setdefault(dir_, {})
                dir_dict.update({k: v if k=='used_percent' else int(v) for k, v in group.items()})
                continue
                      
        return ret_dict
        
class ShowPlatformTcamPbrNatSchema(MetaParser):
    """Schema for show platform hardware fed active fwd-asic resource tcam table pbr record 0 format 0 | begin {nat_region}"""

    schema = {
        Any():{
            Optional('index'):{
                Any():{
                    Optional('mask'):{
                        Any(): str,
                    },                             
                    Optional('key'):{
                        Any(): str,
                    },
                    Optional('ad'): str
                }
            }
        }
    }
            
class ShowPlatformTcamPbrNat(ShowPlatformTcamPbrNatSchema):
    """
    show platform hardware fed active fwd-asic resource tcam table pbr record 0 format 0 | begin {nat_region} 
    """

    cli_command = ['show platform hardware fed {switch} active fwd-asic resource tcam table pbr record 0 format 0 | begin {nat_region}',
                   'show platform hardware fed active fwd-asic resource tcam table pbr record 0 format 0 | begin {nat_region}']
    
    def cli(self, nat_region, switch="", output=None):
        
        if output is None:
            if switch:  
                cmd = self.cli_command[0].format(switch=switch, nat_region=nat_region)
            else:
                cmd = self.cli_command[1].format(nat_region=nat_region)
            output = self.device.execute(cmd)

        # initial variables
        ret_dict = {}
        
        # Printing entries for region NAT_1 (387) type 6 asic 0
        p1 = re.compile(r'^Printing entries for region\s(?P<nat_r>\w+)\s\(\d+\)\stype\s\d\sasic\s\d$')
        
        # TAQ-0 Index-576 (A:0,C:0) Valid StartF-1 StartA-1 SkipF-0 SkipA-0
        p2 = re.compile(r'^TAQ-\d+\sIndex-(?P<index>\d+)\s\([A-Z]\:\d,[A-Z]\:\d\)\sValid\sStart[A-Z]-\d\sStart[A-Z]-\d\sSkip[A-Z]-\d\sSkip[A-Z]-\d$')
      
        # Mask1 30fff000:0003ffff:00000000:0000ffff:00000000:00000000:ffffffff:ffffffff
        p3 = re.compile(r'^(?P<mask_name>Mask\d+) +(?P<mask1>\S+)$')
      
        # Key1  10119000:00020014:00000000:00000028:00000000:00000000:0f000001:23000001
        p4 = re.compile(r'^(?P<key_name>Key\d+) +(?P<key1>\S+)$')
      
        # AD    10087000:000000ae:00000000
        p5 = re.compile(r'^AD +(?P<ad>[\da-f:]+)$')
      
        for line in output.splitlines():
            line = line.strip()
            
            # Printing entries for region NAT_1 (387) type 6 asic 0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                nat_r = group['nat_r'] 
                nat_dict = ret_dict.setdefault(nat_r, {})
                continue
                                                          
            # TAQ-0 Index-576 (A:0,C:0) Valid StartF-1 StartA-1 SkipF-0 SkipA-0 
            m = p2.match(line)
            if m:
                group = m.groupdict()
                index = group['index']
                index_dict = nat_dict.setdefault('index', {}).setdefault(index, {})
                mask_dict = index_dict.setdefault('mask', {})
                key_dict = index_dict.setdefault('key', {})
                continue
                                               
            # Mask1 30fff000:0003ffff:00000000:0000ffff:00000000:00000000:ffffffff:ffffffff
            m = p3.match(line)
            if m:
                group = m.groupdict()
                mask_name = group['mask_name']
                mask_dict[mask_name] = group['mask1']
                continue
      
            # Key1  10119000:00020014:00000000:00000028:00000000:00000000:0f000001:23000001
            m = p4.match(line)
            if m:
                group = m.groupdict()
                key_name = group['key_name']
                key_dict[key_name] = group['key1']
                continue
                
            # AD    10087000:000000ae:00000000
            m = p5.match(line)
            if m:
                group = m.groupdict()
                index_dict['ad'] = group['ad']
                continue
    
        return ret_dict
        
class ShowNatTranslationsSchema(MetaParser):
    """Schema for show ip nat translations"""

    schema = {
        'index':{
            Any():{
                Optional('protocol'): str,
                Optional('inside_global'): str,
                Optional('inside_local'): str,
                Optional('outside_local'): str,
                Optional('outside_global'): str
            }
        }
    }

class ShowNatTranslations(ShowNatTranslationsSchema):
    """
    show ip nat translations
    """

    cli_command = 'show ip nat translations'
    
    def cli(self, output=None):
        
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}
        index = 1

        # Pro Inside global      Inside local       Outside local      Outside global
        # --- 135.0.0.1          35.0.0.1           ---                ---
        p1 = re.compile(r'^(?P<protocol>\S+) +(?P<inside_global>\S+) +(?P<inside_local>\S+) +(?P<outside_local>\S+) +(?P<outside_global>\S+)$')
        
        for line in output.splitlines(): 
            line = line.strip()
            
            # Pro Inside global      Inside local       Outside local      Outside global
            # --- 135.0.0.1          35.0.0.1           ---                ---
            m = p1.match(line)
            if m:
                group = m.groupdict()
                index_dict = ret_dict.setdefault('index', {}).setdefault(index,{})
                index_dict['protocol'] = group['protocol']
                index_dict['inside_global'] = group['inside_global']
                index_dict['inside_local'] = group['inside_local']
                index_dict['outside_local'] = group['outside_local']
                index_dict['outside_global'] = group['outside_global']
                index += 1

        return ret_dict