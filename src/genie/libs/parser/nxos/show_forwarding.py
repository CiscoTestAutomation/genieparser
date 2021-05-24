"""show_forwarding.py


NXOS parsers for the following commands

    * 'show forwarding ipv4'
    * 'show forwarding ipv4 vrf {vrf}'
"""
# Python
import re 
import xmltodict

#Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional

# import parser utils
from genie.libs.parser.utils.common import Common

# =====================
# Parser for 'show forwarding ipv4'
# Parser for 'show forwarding ipv4 vrf {vrf}'
# =====================
class ShowForwardingIpv4Schema(MetaParser):
    "schema for show forwarding ipv4"
    schema = {
        'slot':{
            Any():{
                'ip_version':{
                    Any():{  
                        'route_table':{
                            Any():{
                                'prefix':{
                                    Any():{
                                        'next_hop':{
                                            Any():{
                                                'interface': str,                   
                                                'is_best': bool,
                                                Optional('label'): str,
                                            }
                                        }
                                    }        
                                }        
                            }
                        }
                    }
                }
            }
        }                
    }



class ShowForwardingIpv4(ShowForwardingIpv4Schema):
    "parser for show forwarding ipv4"
    cli_command = ['show forwarding ipv4', 'show forwarding ipv4 vrf {vrf}']
    
    def cli(self, vrf='', output=None):
        if output is None:
            if vrf:
                out = self.device.execute(self.cli_command[1].format(vrf=vrf))
            else:
                out = self.device.execute(self.cli_command[0])
        else:
            out = output
              
        result_dict = {}  

        
        #slot  1
        #slot 27
        p1 = re.compile(r'^slot +(?P<slot>\d+)')
        
        #IPv4 routes for table default/base
        #IPv4 routes for table VRF_Flow1_1/base
        p2 = re.compile(r'^(?P<ip_version>\w+)'
                         ' +routes +for +table +(?P<route_table>(\w+\/+\w+)|(0x[0-5a-fA-F]+))')
        
        #0.0.0.0/32           Drop                                      Null0
        #*10.36.3.2/32          10.2.1.2                                  Ethernet1/1
        #10.36.3.2/32          10.2.1.2                                  Ethernet1/1       vni: 501003
        #10.4.1.1/32           10.2.1.2                                  Ethernet1/1           PUSH 16001
        p3 = re.compile(r'^(?P<is_best_next_hop>\*)?'
                          '(?P<prefix>[0-9\.]+\/[0-9]+)?'
                          ' +(?P<next_hop>[0-9A-Za-z.]+)'  
                          ' +(?P<interface>[\w\-\/\.]+)'                     
                          '\s*(?P<label>[\w\:\ \w]+)?'
                          )
        
        #10.2.1.2                                  Ethernet1/1
        #10.2.1.2                                  Ethernet1/1       vn: 501003
        p3_1 = re.compile(r'^(?P<next_hop>[0-9A-Za-z.]+)'  
                          ' +(?P<interface>[\w\-\/\.]+)'                     
                          '\s*(?P<label>[\w\:\ \w]+)?'
                          )
         
        for line in out.splitlines():
            line = line.strip()
            
            #slot  1
            m = p1.match(line)
            if m:
                slot_dict = {}
                group = m.groupdict()
                key = 'slot' 
                value = group[key]
                slot_dict = result_dict.setdefault(key, {}).setdefault(value, {})
                continue
             
            #IPv4 routes for table default/base
            #IPv4 routes for table VRF_Flow1_1/base
            m = p2.match(line)
            if m: 
                group = m.groupdict()
                ip_version = group['ip_version']
                route_table = group['route_table']
                
                #since this command is for ipv4 exclusively, this is not necessary for now.
                #But will be necessary for the future implementation of ipv6
                ip_version_dict = slot_dict.setdefault('ip_version', {}).setdefault(ip_version, {})

                route_table_dict = ip_version_dict.setdefault('route_table', {}).setdefault(route_table, {})
                continue
        
            #0.0.0.0/32           Drop                                      Null0
            #*10.36.3.2/32          10.2.1.2                                  Ethernet1/1
            #10.36.3.2/32          10.2.1.2                                  Ethernet1/1       vni: 501003
            m = p3.match(line)
            if m:
                group = m.groupdict()
                
                is_best = group['is_best_next_hop']
                prefix = group['prefix']
                next_hop = group['next_hop']
                interface = group['interface']
                label = group['label']

                if is_best is None:
                    is_best = False
                else:
                    is_best = True
                
                prefix_dict = route_table_dict.setdefault('prefix', {}).setdefault(prefix, {}) 
                
                next_hop_dict = prefix_dict.setdefault('next_hop', {}).setdefault(next_hop, {})
                
                next_hop_dict['is_best'] = is_best
                next_hop_dict['interface'] = interface
                if label is not None: 
                    next_hop_dict['label'] = label
                continue

            #10.2.1.2                                  Ethernet1/1
            #10.2.1.2                                  Ethernet1/1       vn: 501003
            m = p3_1.match(line)
            if m:
                group = m.groupdict()
                is_best = False           
                next_hop = group['next_hop']
                interface = group['interface']
                label = group['label']

                next_hop_dict = prefix_dict.setdefault('next_hop', {}).setdefault(next_hop, {})

                next_hop_dict['is_best'] = is_best              
                next_hop_dict['interface'] = interface
                if label is not None:
                    next_hop_dict['label'] = label
                continue
            

        return result_dict                    

    
        
             
        
    
    



