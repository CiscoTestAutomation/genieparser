"""starOS implementation of show snmp communities.py
Author: Luis Antonio Villalobos(luisvill)
"""
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Schema

class ShowSNMPSchema(MetaParser):
    """Schema for show snmp communities"""

    schema = {
        'snmp_communities': {
            Any(): {
                'Community Name' : str,
                'Access Level': str,
            },
        }    
    }


class ShowSNMP(ShowSNMPSchema):
    """Parser for show snmp communities"""

    cli_command = 'show snmp communities'

    """
[local]COR-VPC-1# show snmp communities 
Thursday March 14 18:43:40 ART 2024
Community Name                   Access Level
-------------------------------- ------------
nm5r0c0m                         read-write
public                           read-only
readonly                         read-only
    """

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        communities_dict = {}
        
        result_dict = {}

        # initial regexp pattern
        p0 = re.compile(r'^(?P<community>(\S+)\s+)(?P<access>(read\-write|read\-only))$')
    
        for line in out.splitlines():
            line = line.strip()
            m = p0.match(line)
            if m:
                if 'snmp_communities' not in communities_dict:
                    result_dict = communities_dict.setdefault('snmp_communities',{})
                community = m.groupdict()['community']
                access = m.groupdict()['access']
            
                result_dict[community] = {}
                result_dict[community]["Community Name"]= community
                result_dict[community]["Access Level"]= access

        return communities_dict
