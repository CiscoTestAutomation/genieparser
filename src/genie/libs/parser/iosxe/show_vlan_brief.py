"""
IOSXE C9300 parsers for the following show commands:
    * show vlan brief
"""
# Python
import re
import logging

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional


# ============================
#  Schema for 'show vlan brief'
# ============================
class ShowVlanBriefSchema(MetaParser):

    """ Schema for:
        * show vlan brief
    """
    schema = {

        Any():{
            'vlan_id': int,
            'name': str,
            'status': str,
            Optional('ports'): str,
            }
            
        }
        


# ============================
#  Parser for 'show vlan brief'
# ============================
class ShowVlanBrief(ShowVlanBriefSchema):
    """
    Parser for :
        * show vlan brief
    """

    cli_command = 'show vlan brief'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}

        # --------------------------------------------------------------
        # Regex patterns
        # --------------------------------------------------------------
        # 1    default                          active    Gi1/0/2, Gi1/0/3, Gi1/0/4, Gi1/0/5, Gi1/0/6, Gi1/0/7, Gi1/0/8, Gi1/0/9, Gi1/0/10, Gi1/0/11, Gi1/0/12, Gi1/0/13, Gi1/0/14, Gi1/0/15, Gi1/0/17, Gi1/0/21, Gi1/0/22, Gi1/0/23, Gi1/0/24, Gi1/0/25, Gi1/0/26, Gi1/0/27, Gi1/0/28, Gi1/0/29, Gi1/0/30, Gi1/0/38, Gi1/0/39, Gi1/0/40, Gi1/0/47, Te1/1/3, Te1/1/4, Te1/1/5, Te1/1/6, Te1/1/7, Te1/1/8, Ap1/0/1
        p1 = re.compile(r'(?P<vlan_id>\d+)\s+(?P<name>\S+)\s+(?P<status>\S+)\s+(?P<ports>(?:\S+\s)+\d?)')

        # 2    VLAN0002                         active    
        p2 = re.compile(r'(?P<vlan_id>\d+)\s+(?P<name>\S+)\s+(?P<status>\S+)')

        # --------------------------------------------------------------
        # Build the parsed output
        # --------------------------------------------------------------
        for line in out.splitlines():
            per_vlan_dict = {}
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()

                per_vlan_dict = parsed_dict.setdefault(group['vlan_id'],{})

                per_vlan_dict['vlan_id'] = int(group['vlan_id'])
                per_vlan_dict['name'] = group['name']
                per_vlan_dict['status'] = group['status']
                per_vlan_dict['ports'] = group['ports']
                
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()

                per_vlan_dict = parsed_dict.setdefault(group['vlan_id'],{})

                per_vlan_dict['vlan_id'] = int(group['vlan_id'])
                per_vlan_dict['name'] = group['name']
                per_vlan_dict['status'] = group['status']
                per_vlan_dict['ports'] = ""
                
                continue
                
        return parsed_dict


