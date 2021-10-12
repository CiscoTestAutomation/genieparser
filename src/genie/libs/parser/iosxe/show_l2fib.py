''' show_l2fib.py

IOSXE parsers for the following show commands:

    * show l2fib path-list {id}
    * show l2fib path-list detail
    * show l2fib bridge-domain {bd_id} port
    * show l2fib bridge-domain {bd_id} address unicast {mac_addr}

Copyright (c) 2021 by Cisco Systems, Inc.
All rights reserved.
'''

import re

# genie
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, ListOf, Optional


# ====================================================
# Schema for 'show l2fib path-list <id>'
# ====================================================
class ShowL2fibPathListIdSchema(MetaParser):
    """ Schema for show l2fib path-list {id}
                   show l2fib path-list detail
    """

    schema = {
        'pathlist_id': {
            Any(): {
               'type': str,
               'eth_seg': str,
               'path_cnt': int,
               'path_list': ListOf(
                    {
                      'path': str
                    }
                )
            }
        }
    }


# =============================================
# Parser for 'show l2fib path-list <id>'
# =============================================
class ShowL2fibPathListId(ShowL2fibPathListIdSchema):
    """ Parser for show l2fib path-list {id}
                   show l2fib path-list detail
    """

    cli_command = [
            'show l2fib path-list {id}',
            'show l2fib path-list detail'
    ]

    def cli(self, id=None, output=None):

        if output is None:
            if id:
                cli_cmd = self.cli_command[0].format(id=id)
            else:
                cli_cmd = self.cli_command[1]

            cli_output = self.device.execute(cli_cmd)
        else:
            cli_output = output

        # PathList ID                   : 28
        p1 = re.compile(r'^PathList ID\s+:\s+(?P<path_list_id>\d+)$')

        # PathList Type                 : MPLS_UC
        p2 = re.compile(r'^PathList Type\s+:\s+(?P<type>\w+)$')

        # Ethernet Segment              : 0000.0000.0000.0000.0000
        p3 = re.compile(r'^Ethernet Segment\s+:\s+'
                        r'(?P<eth_seg>[0-9a-fA-F\.]+)$')

        # Path Count                    : 1
        p4 = re.compile(r'^Path Count\s+:\s+(?P<path_cnt>\d+)$')

        # Paths                         : [MAC]16@2.2.2.1
        p5 = re.compile(r'^[Paths]*\s*:\s+(?P<path>\[\w+\]\d+'
                        r'[0-9a-fA-F\.:@ ]+)$')

        parser_dict = {}

        for line in cli_output.splitlines():
            line = line.strip()
            if not line:
                continue

            # PathList ID                   : 28
            m = p1.match(line)
            if m:
                group = m.groupdict()
                path_list_ids_dict = parser_dict.setdefault('pathlist_id', {})
                path_list = path_list_ids_dict.setdefault(int(group['path_list_id']), {})
                paths = path_list.setdefault('path_list', [])
                continue

            # PathList Type                 : MPLS_UC
            m = p2.match(line)
            if m:
                group = m.groupdict()
                path_list.update({'type': group['type']})
                continue

            # Ethernet Segment              : 0000.0000.0000.0000.0000
            m = p3.match(line)
            if m:
                group = m.groupdict()
                path_list.update({'eth_seg': group['eth_seg']})
                continue

            # Path Count                    : 1
            m = p4.match(line)
            if m:
                group = m.groupdict()
                path_list.update({'path_cnt': int(group['path_cnt'])})
                continue

            # Paths                         : [MAC]16@2.2.2.1
            m = p5.match(line)
            if m:
                group = m.groupdict()
                path = group['path']
                paths_dict = {}
                paths_dict.update({'path': path})
                paths.append(paths_dict)
                continue

        return parser_dict

# ====================================================
# Schema for 'show l2fib bridge-domain {bd_id} port'
# ====================================================
class ShowL2fibBdPortSchema(MetaParser):
    """ Schema for show l2fib bridge-domain {bd-id} port """

    schema = {
        Any(): {
            'type': str,
            'is_path_list': bool,
            Optional('port'): str,
            Optional('path_list'): {
                'id': int,
                'path_count': int,
                'type': str,
                'description': str
            }
        }
    }

# ==================================================
# Parser for 'show l2fib bridge-domain <bd_id> port'
# ==================================================
class ShowL2fibBdPort(ShowL2fibBdPortSchema):
    """ Parser for show l2fib bridge-domain {bd_id} port """

    cli_command = [ 'show l2fib bridge-domain {bd_id} port']

    def cli(self, output=None, bd_id=None):
        if output is None:
            cli_output = self.device.execute(self.cli_command[0].format(bd_id=bd_id))
        else:
            cli_output = output

        #BD_PORT   Et0/2:12
        p1 = re.compile(r'^(?P<port_type>BD_PORT)\s+(?P<interface>[\w:\/]+)$')

        #VXLAN_REP PL:1191(1) T:VXLAN_REP [IR]20012:2.2.2.2
        p2 = re.compile(r'^(?P<type>\w+)\s+PL:(?P<path_list_id>\d+)\((?P<path_list_count>\d+)\)'
                        r'\s+T:(?P<path_list_type>\w+)\s+(?P<path_list_desc>\[\w+\][0-9a-fA-F:@\.]+)$')

        parser_dict = {}

        for line in cli_output.splitlines():
            line = line.strip()
            if not line:
                continue

            #BD_PORT   Et0/2:12
            m = p1.match(line)
            if m:
                group = m.groupdict()
                port_type = group['port_type']
                interface_id = group['interface']
                parser_dict.update({
                    interface_id: {
                        'type': port_type,
                        'is_path_list': False,
                        'port': interface_id
                    }
                })
                continue

            #VXLAN_REP PL:1191(1) T:VXLAN_REP [IR]20012:2.2.2.2
            m = p2.match(line)
            if m:
                group = m.groupdict()
                parser_dict.update({
                    group['path_list_desc']: {
                        'type': group['type'],
                        'is_path_list': True,
                        'path_list': {
                            'id': int(group['path_list_id']),
                            'path_count': int(group['path_list_count']),
                            'type': group['path_list_type'],
                            'description': group['path_list_desc']
                        }
                    }
                })
                continue
        return parser_dict

# ========================================================================
# Schema for 'show l2fib bridge-domain <bd_id> address unicast <mac_addr>'
# ========================================================================
class ShowL2fibBridgedomainAddressUnicastSchema(MetaParser):
    """ Schema for show l2fib bridge-domin {bd-id} address unicast {mac_addr}"""

    schema = {
        'mac_addr': str,
        'reference_count': int,
        'epoch': int,
        'producer': str,
        'flags': ListOf(
            str
            ),
        'adjacency': {
            Optional('path_list'): {
                'path_list_id': int,
                'path_list_count': int,
                'path_list_type': str,
                'path_list_desc': str,
            },
            Optional('olist'): {
                'olist': int,
                'port_count': int
            },
            'type': str,
            'desc': str
        },
        'pd_adjacency': {
            Optional('path_list'): {
                'path_list_id': int,
                'path_list_count': int,
                'path_list_type': str,
                'path_list_desc': str,
            },
            Optional('olist'): {
                'olist': int,
                'port_count': int
            },
            'type': str,
            'desc': str
        },
        'packet_count': int,
        'bytes': int
    }

# ========================================================================
# Parser for 'show l2fib bridge-domain <bd_id> address unicast <mac_addr>'
# ========================================================================
class ShowL2fibBridgedomainAddressUnicast(ShowL2fibBridgedomainAddressUnicastSchema):
    """ Parser for show l2fib bridge-domain {bd_id} address unicast {mac_addr}"""

    cli_command = 'show l2fib bridge-domain {bd_id} address unicast {mac_addr}'

    def cli(self, output=None, bd_id=None, mac_addr=None):
        if output is None:
            out = self.device.execute(self.cli_command.format(bd_id=bd_id, mac_addr=mac_addr))
        else:
            out = output

        #MAC Address                   : aabb.0000.0002
        p1 = re.compile(r'^MAC\s+Address\s+:\s+(?P<mac_addr>[a-fA-F0-9\.]+)$')

        #Reference Count               : 1
        p2 = re.compile(r'^Reference\s+Count\s+:\s+(?P<reference_count>\d+)$')

        #Epoch                         : 0
        p3 = re.compile(r'^Epoch\s+:\s+(?P<epoch>\d+)$')

        #Producer                      : BGP
        #Producer : BD-ENG
        p4 = re.compile(r'^Producer\s+:\s+(?P<producer>.+)$')

        #Flags                         : Local Mac
        p5 = re.compile(r'^Flags\s+:\s+(?P<flags>[\w\s]+)$')

        #: CP Learn
        p6 = re.compile(r'^:\s+(?P<flags>[\w\s]+)$')

        #Adjacency                     : MPLS_UC   PL:5(1) T:MPLS_UC [MAC]16@2.2.2.1
        #PD Adjacency                  : MPLS_UC   PL:5(1) T:MPLS_UC [MAC]16@2.2.2.1
        p7 = re.compile(r'^(?P<tag>(Adjacency|PD Adjacency))\s+:\s+(?P<type>\w+)\s+PL:(?P<path_list_id>\d+)\((?P<path_list_count>\d+)\)'
                        r'\s+T:(?P<path_list_type>\w+)\s+(?P<path_list_desc>\[\w+\][0-9a-fA-F:@\.]+)$')

        #Adjacency                     : Olist: 3, Ports: 1
        #PD Adjacency                  : Olist: 3, Ports: 1
        p8 = re.compile(r'^(?P<tag>(Adjacency|PD Adjacency))\s+:\s+Olist:\s+(?P<olist>\d+),\s+Ports:\s+(?P<port_count>\d+)$')

        #Adjacency : VXLAN_CP L:20011:1.1.1.1 R:20012:2.2.2.2
        #PD Adjacency : VXLAN_CP L:20011:1.1.1.1 R:20012:2.2.2.2
        #Adjacency                     : BD_PORT   Et0/1:11
        #PD Adjacency                  : BD_PORT   Et0/1:11
        p9 = re.compile(r'^(?P<tag>(Adjacency|PD Adjacency))\s+:\s+(?P<type>\w+)\s+(?P<desc>.+)$')

        #Packets                       : 0
        p10 = re.compile(r'^Packets\s+:\s+(?P<packet_count>\d+)$')

        #Bytes                         : 0
        p11 = re.compile(r'^Bytes\s+:\s+(?P<bytes>\d+)$')

        parser_dict = {}

        for line in out.splitlines():
            line = line.strip()
            if not line:
                continue

            #MAC Address                   : aabb.0000.0002
            m = p1.match(line)
            if m:
                group = m.groupdict()
                parser_dict.update({
                    'mac_addr':group['mac_addr']
                })
                continue

            #Reference Count               : 1
            m = p2.match(line)
            if m:
                group = m.groupdict()
                parser_dict.update({'reference_count': int(group['reference_count']) })
                continue

            #Epoch                         : 0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                parser_dict.update({'epoch': int(group['epoch'])})
                continue

            #Producer                      : BGP
            m = p4.match(line)
            if m:
                group = m.groupdict()
                parser_dict.update({'producer': group['producer']})
                continue

            #Flags                         : Local Mac
            m = p5.match(line)
            if m:
                group = m.groupdict()
                flags_list = parser_dict.setdefault('flags', [])
                flags_list.append(group['flags'])
                continue

            #: CP Learn
            m = p6.match(line)
            if m:
                group = m.groupdict()
                flags_list.append(group['flags'])
                continue

            #Adjacency                     : MPLS_UC   PL:5(1) T:MPLS_UC [MAC]16@2.2.2.1
            #PD Adjacency                  : MPLS_UC   PL:5(1) T:MPLS_UC [MAC]16@2.2.2.1
            m = p7.match(line)
            if m:
                group = m.groupdict()
                adj_subdict = {}
                adj_subdict.update({
                    'type': group['type'],
                    'desc': 'PL:{pl_id}({pl_count}) T:{pl_type} {pl_desc}'.format( \
                        pl_id=group['path_list_id'], pl_count=group['path_list_count'], \
                        pl_type=group['path_list_type'], pl_desc=group['path_list_desc']),
                    'path_list': {
                        'path_list_id': int(group['path_list_id']),
                        'path_list_count': int(group['path_list_count']),
                        'path_list_type': group['path_list_type'],
                        'path_list_desc': group['path_list_desc']
                    }
                })
                if group['tag'] == 'Adjacency':
                    adjacency = parser_dict.setdefault('adjacency', adj_subdict)
                elif group['tag'] == 'PD Adjacency':
                    pd_adjacency = parser_dict.setdefault('pd_adjacency', adj_subdict)
                continue

            #Adjacency                     : Olist: 3, Ports: 1
            #PD Adjacency                  : Olist: 3, Ports: 1
            m = p8.match(line)
            if m:
                group = m.groupdict()
                adj_subdict = {}
                adj_subdict.update({
                    'type': 'olist',
                    'desc': 'Olist: {olist}, Ports: {port_count}'.format(\
                        olist=group['olist'], port_count=group['port_count']),
                    'olist': {
                        'olist': int(group['olist']),
                        'port_count': int(group['port_count'])
                    }
                })
                if group['tag'] == 'Adjacency':
                    adjacency = parser_dict.setdefault('adjacency', adj_subdict)
                elif group['tag'] == 'PD Adjacency':
                    pd_adjacency = parser_dict.setdefault('pd_adjacency', adj_subdict)
                continue

            #Adjacency : VXLAN_CP L:20011:1.1.1.1 R:20012:2.2.2.2
            #PD Adjacency : VXLAN_CP L:20011:1.1.1.1 R:20012:2.2.2.2
            #Adjacency                     : BD_PORT   Et0/1:11
            #PD Adjacency                  : BD_PORT   Et0/1:11
            m = p9.match(line)
            if m:
                group = m.groupdict()
                adj_subdict = {}
                adj_subdict.update({
                    'type': group['type'],
                    'desc': group['desc']
                })
                if group['tag'] == 'Adjacency':
                    parser_dict.setdefault('adjacency', adj_subdict)
                elif group['tag'] == 'PD Adjacency':
                    parser_dict.setdefault('pd_adjacency', adj_subdict)
                continue

            #Packets                       : 0
            m = p10.match(line)
            if m:
                group = m.groupdict()
                parser_dict.update({'packet_count': int(group['packet_count'])})
                continue

            #Bytes                         : 0
            m = p11.match(line)
            if m:
                group = m.groupdict()
                parser_dict.update({'bytes': int(group['bytes'])})
                continue
        return parser_dict
