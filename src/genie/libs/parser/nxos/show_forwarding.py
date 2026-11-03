"""show_forwarding.py


NXOS parsers for the following commands

    * 'show forwarding ipv4'
    * 'show forwarding ipv4 vrf {vrf}'
    * 'show forwarding ipv4 recursive'
    * 'show forwarding ipv4 recursive vrf {vrf}'
    * 'show forwarding route {prefix} detail module {module}'
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
                         r' +routes +for +table +(?P<route_table>(\w+\/+\w+)|(0x[0-5a-fA-F]+))')
        
        #0.0.0.0/32           Drop                                      Null0
        #*10.36.3.2/32          10.2.1.2                                  Ethernet1/1
        #10.36.3.2/32          10.2.1.2                                  Ethernet1/1       vni: 501003
        #10.4.1.1/32           10.2.1.2                                  Ethernet1/1           PUSH 16001
        p3 = re.compile(r'^(?P<is_best_next_hop>\*)?'
                          r'(?P<prefix>[0-9\.]+\/[0-9]+)?'
                          r' +(?P<next_hop>[0-9A-Za-z.]+)'  
                          r' +(?P<interface>[\w\-\/\.]+)'                     
                          r'\s*(?P<label>[\w\:\ \w]+)?'
                          )
        
        #10.2.1.2                                  Ethernet1/1
        #10.2.1.2                                  Ethernet1/1       vn: 501003
        p3_1 = re.compile(r'^(?P<next_hop>[0-9A-Za-z.]+)'  
                          r' +(?P<interface>[\w\-\/\.]+)'                     
                          r'\s*(?P<label>[\w\:\ \w]+)?'
                          )
         
        #1.1.1.2/32           fe80::a111:2222:3333:e13                  Ethernet1/1
        p4 = re.compile(r'^(?P<is_best_next_hop>\*)?'
                        r'(?P<prefix>[0-9\.]+\/[0-9]+)'
                        r' +(?P<next_hop>[a-fA-F0-9\:]+)'
                        r' +(?P<interface>[\w\-\/\.]+)$')

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
            
            #1.1.1.2/32           fe80::a111:2222:3333:e13                  Ethernet1/1   
            #*1.1.1.2/32           fe80::a111:2222:3333:e13                  Ethernet1/1   
            m = p4.match(line)
            if m:
                group = m.groupdict()
                prefix = group['prefix']
                next_hop = group['next_hop']
                interface = group['interface']
                is_best = group['is_best_next_hop']

                is_best = is_best is not None

                prefix_dict = route_table_dict.setdefault('prefix', {}).setdefault(prefix, {}) 
                next_hop_dict = prefix_dict.setdefault('next_hop', {}).setdefault(next_hop, {})
                next_hop_dict['interface'] = interface          
                next_hop_dict['is_best'] = is_best      
                continue

        return result_dict                    


class ShowForwardingIpv4Recursive(ShowForwardingIpv4, ShowForwardingIpv4Schema):
    "parser for show forwarding ipv4 recursive"
    cli_command = ['show forwarding ipv4 recursive', 'show forwarding ipv4 recursive vrf {vrf}']

    def cli(self, vrf='', output=None):
        if output is None:
            if vrf:
                output = self.device.execute(self.cli_command[1].format(vrf=vrf))
            else:
                output = self.device.execute(self.cli_command[0])
    
        ret_dict = super().cli(output=output)

        return ret_dict


# ============================================
# Parser for 'show forwarding route {prefix} detail module {module}'
# ============================================
class ShowForwardingRouteDetailSchema(MetaParser):
    """Schema for show forwarding route {prefix} detail module {module}"""

    schema = {
        'prefix': {
            Any(): {
                'number_of_paths': int,
                'update_time': str,
                'vobj_id': int,
                'orig_as': int,
                'peer_as': int,
                'rnh': str,
                'paths': {
                    Any(): {
                        'interface': str,
                        'dmac': str,
                        Optional('packets'): int,
                        Optional('bytes'): int,
                        Optional('repair_path'): {
                            'next_hop': str,
                            'interface': str,
                            'dmac': str,
                            'packets': int,
                            Optional('bytes'): int,
                        },
                    },
                },
            },
        },
    }


class ShowForwardingRouteDetail(ShowForwardingRouteDetailSchema):
    """Parser for show forwarding route {prefix} detail module {module}"""

    cli_command = 'show forwarding route {prefix} detail module {module}'

    def cli(self, command, output=None):
        if output is None:
            output = self.device.execute(command)

        ret_dict = {}
        prefix_dict = None
        path_dict = None
        repair_path_dict = None

        # Prefix 123.1.1.0/24, No of paths: 1, Update time: Wed Jul 11 19:00:12 2018
        p1 = re.compile(r'^Prefix +(?P<prefix>\S+), +No +of +paths: +(?P<number_of_paths>\d+), +Update +time: +(?P<update_time>[A-Za-z]{3} +[A-Za-z]{3} +\d+ +\d{2}:\d{2}:\d{2} +\d{4})$')

        # Vobj id: 141   orig_as: 65002   peer_as: 65100  rnh: 10.3.0.2
        p2 = re.compile(r'^Vobj +id: +(?P<vobj_id>\d+) +orig_as: +(?P<orig_as>\d+) +peer_as: +(?P<peer_as>\d+) +rnh: +(?P<rnh>[\da-fA-F:.]+)$')

        # 10.4.0.2           Ethernet8/4         DMAC: 0018.bad8.4dfd
        p3 = re.compile(r'^(?P<next_hop>[\da-fA-F:.]+) +(?P<interface>\S+) +DMAC: +(?P<dmac>[0-9a-fA-F.]+)$')

        # packets: 2  bytes: 3484   Repair path  10.3.0.2   Ethernet8/3 DMAC: 0018.bad8.4dfd packets: 0
        p4 = re.compile(r'^packets: +(?P<packets>\d+) +bytes: +(?P<bytes>\d+) +Repair +path +(?P<repair_next_hop>[\da-fA-F:.]+) +(?P<repair_interface>\S+) +DMAC: +(?P<repair_dmac>[0-9a-fA-F.]+) +packets: +(?P<repair_packets>\d+)$')

        # bytes: 1
        p5 = re.compile(r'^bytes: +(?P<repair_bytes>\d+)$')

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            # Prefix 123.1.1.0/24, No of paths: 1, Update time: Wed Jul 11 19:00:12 2018
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                prefix_dict = ret_dict.setdefault('prefix', {}) \
                    .setdefault(groups['prefix'], {})
                prefix_dict.update({
                    'number_of_paths': int(groups['number_of_paths']),
                    'update_time': groups['update_time'],
                })
                continue

            # Vobj id: 141   orig_as: 65002   peer_as: 65100  rnh: 10.3.0.2
            m = p2.match(line)
            if m and prefix_dict is not None:
                groups = m.groupdict()
                prefix_dict.update({
                    'vobj_id': int(groups['vobj_id']),
                    'orig_as': int(groups['orig_as']),
                    'peer_as': int(groups['peer_as']),
                    'rnh': groups['rnh'],
                })
                continue

            # 10.4.0.2           Ethernet8/4         DMAC: 0018.bad8.4dfd
            m = p3.match(line)
            if m and prefix_dict is not None:
                groups = m.groupdict()
                path_dict = prefix_dict.setdefault('paths', {}) \
                    .setdefault(groups['next_hop'], {})
                path_dict.update({
                    'interface': groups['interface'],
                    'dmac': groups['dmac'],
                })
                repair_path_dict = None
                continue

            # packets: 2  bytes: 3484   Repair path  10.3.0.2   Ethernet8/3 DMAC: 0018.bad8.4dfd packets: 0
            m = p4.match(line)
            if m and path_dict is not None:
                groups = m.groupdict()
                path_dict.update({
                    'packets': int(groups['packets']),
                    'bytes': int(groups['bytes']),
                })
                repair_path_dict = path_dict.setdefault('repair_path', {})
                repair_path_dict.update({
                    'next_hop': groups['repair_next_hop'],
                    'interface': groups['repair_interface'],
                    'dmac': groups['repair_dmac'],
                    'packets': int(groups['repair_packets']),
                })
                continue

            # bytes: 1
            m = p5.match(line)
            if m and repair_path_dict is not None:
                groups = m.groupdict()
                repair_path_dict['bytes'] = int(groups['repair_bytes'])
                continue

        return ret_dict
