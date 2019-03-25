"""
show_isis.py

IOSXR parsers for the following show commands:
    * show isis adjacency
    * show isis neighbors

"""

# Python
import re
from netaddr import IPAddress, IPNetwork

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional
from genie.libs.parser.utils.common import Common


#==================================
# Schema for 'show isis adjacency'
#==================================
class ShowIsisAdjacencySchema(MetaParser):
    """Schema for show run isis adjacency"""
        
    schema = {
        'isis': {
            Any(): {
                'level': {
                    Any(): {
                        'total_adjacency_count': int,
                        'system_id': {
                            Any(): {
                                'interface': str,
                                'snpa': str,
                                'state': str,
                                'hold': str,
                                'changed': str,
                                Optional('nsf'): str,
                                Optional('ipv4_bfd'): str,
                                Optional('ipv6_bfd'): str,
                            },
                        }
                    },
                },
            },
        }
    }

class ShowIsisAdjacency(ShowIsisAdjacencySchema):
    """Parser for show isis adjacency"""
    
    cli_command = 'show isis adjacency'
    
    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        
        isis_adjacency_dict = {}
        for line in out.splitlines():
            line = line.rstrip()
            
            # IS-IS 4445 Level-2 adjacencies:
            p1 = re.compile(r'^\s*IS-IS\s+(?P<isis_name>\S+)\s+(?P<level_name>\S+)\s*adjacencies:\s*$')
            m = p1.match(line)
            if m:
                isis_adjacency_dict.setdefault('isis', {})
                isis_name = m.groupdict()['isis_name']
                level_name = m.groupdict()['level_name']
                isis_adjacency_dict['isis'][isis_name] = {'level': {level_name: {} } }
                continue
            
            # BKL-P-C9010-02 BE2              *PtoP*         Up    23   16w0d    Yes Up   None
            p2 = re.compile(r'^\s*(?P<system_id>\S+)\s+(?P<interface>\S+)\s+(?P<snpa>\S+)\s+(?P<state>(Up|Down|None)+)\s+(?P<hold>\S+)\s+(?P<changed>\S+)\s+(?P<nsf>\S+)\s+(?P<ipv4_bfd>(Up|Down|None)+)\s+(?P<ipv6_bfd>(Up|Down|None)+)\s*$')
            m = p2.match(line)
            if m:
                system_id = m.groupdict()['system_id']
                isis_adjacency_dict['isis'][isis_name]['level'][level_name].setdefault('system_id', {}).setdefault(system_id, {})
                isis_adjacency_dict['isis'][isis_name]['level'][level_name]['system_id'][system_id]['interface'] = Common.convert_intf_name(m.groupdict()['interface'])
                isis_adjacency_dict['isis'][isis_name]['level'][level_name]['system_id'][system_id]['snpa'] = m.groupdict()['snpa']
                isis_adjacency_dict['isis'][isis_name]['level'][level_name]['system_id'][system_id]['state'] = m.groupdict()['state']
                isis_adjacency_dict['isis'][isis_name]['level'][level_name]['system_id'][system_id]['hold'] = m.groupdict()['hold']
                isis_adjacency_dict['isis'][isis_name]['level'][level_name]['system_id'][system_id]['changed'] = m.groupdict()['changed']
                isis_adjacency_dict['isis'][isis_name]['level'][level_name]['system_id'][system_id]['nsf'] = m.groupdict()['nsf']
                isis_adjacency_dict['isis'][isis_name]['level'][level_name]['system_id'][system_id]['ipv4_bfd'] = m.groupdict()['ipv4_bfd']
                isis_adjacency_dict['isis'][isis_name]['level'][level_name]['system_id'][system_id]['ipv6_bfd'] = m.groupdict()['ipv6_bfd']
                continue
            
            # Total adjacency count: 1
            p3 = re.compile(r'^\s*Total\sadjacency\scount:\s+(?P<adjacency_count>\S+)\s*$')
            m = p3.match(line)
            if m:
                isis_adjacency_dict['isis'][isis_name]['level'][level_name]['total_adjacency_count'] = int(m.groupdict()['adjacency_count'])
                continue
        
        return isis_adjacency_dict


#======================================
# Schema for 'show isis neighbors'
#======================================
class ShowIsisNeighborsSchema(MetaParser):
    """Schema for show run isis neighbors"""
    
    schema = {
        'isis': {
            Any(): {
                'total_neighbor_count': int,
                'neighbors': {
                    Any(): {
                        'interface': str,
                        'snpa': str,
                        'state': str,
                        'holdtime': str,
                        'type': str,
                        Optional('ietf_nsf'): str,
                    },
                },
            },
        }
    }

class ShowIsisNeighbors(ShowIsisNeighborsSchema):
    """Parser for show isis neighbors"""
    
    cli_command = 'show isis neighbors'
    
    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        
        isis_neighbors_dict = {}
        for line in out.splitlines():
            line = line.rstrip()
        
            # IS-IS 4445 neighbors:
            p1 = re.compile(r'^\s*IS-IS\s+(?P<isis_name>\S+)\s*neighbors:\s*$')
            m = p1.match(line)
            if m:
                isis_name = m.groupdict()['isis_name']
                continue
            
            # BKL-P-C9010-02 BE2              *PtoP*         Up    23       L2   Capable
            p2 = re.compile(r'^\s*(?P<system_id>\S+)\s+(?P<interface>\S+)\s+(?P<snpa>\S+)\s+(?P<state>(Up|Down|None)+)\s+(?P<holdtime>\S+)\s+(?P<type>\S+)\s+(?P<ietf_nsf>\S+)\s*$')
            m = p2.match(line)
            if m:
                system_id = m.groupdict()['system_id']
                isis_neighbors_dict.setdefault('isis', {}).setdefault(isis_name, {}).setdefault('neighbors', {}).setdefault(system_id, {})
                isis_neighbors_dict['isis'][isis_name]['neighbors'][system_id]['interface'] = Common.convert_intf_name(m.groupdict()['interface'])
                isis_neighbors_dict['isis'][isis_name]['neighbors'][system_id]['snpa'] = m.groupdict()['snpa']
                isis_neighbors_dict['isis'][isis_name]['neighbors'][system_id]['state'] = m.groupdict()['state']
                isis_neighbors_dict['isis'][isis_name]['neighbors'][system_id]['holdtime'] = m.groupdict()['holdtime']
                isis_neighbors_dict['isis'][isis_name]['neighbors'][system_id]['type'] = m.groupdict()['type']
                isis_neighbors_dict['isis'][isis_name]['neighbors'][system_id]['ietf_nsf'] = m.groupdict()['ietf_nsf']
                continue
            
            # Total neighbor count: 1
            p3 = re.compile(r'^\s*Total\sneighbor\scount:\s+(?P<neighbor_count>\S+)\s*$')
            m = p3.match(line)
            if m:
                isis_neighbors_dict['isis'][isis_name]['total_neighbor_count'] = int(m.groupdict()['neighbor_count'])
                continue
        
        return isis_neighbors_dict



