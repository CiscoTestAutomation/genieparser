''' show_l2fib.py

IOSXE parsers for the following show commands:

    * show l2fib path-list {id}
    * show l2fib path-list detail
    * show l2fib bridge-domain {bd_id} port
    * show l2fib bridge-domain {bd_id} address unicast {mac_addr}
    * show l2fib output-list
    * show l2fib output-list {output_id}

Copyright (c) 2021 by Cisco Systems, Inc.
All rights reserved.
'''

import re

# genie
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, ListOf, Optional


# ====================================================
# Schema for 'show l2fib output-list <id>'
# ====================================================
class ShowL2fibOlistSchema(MetaParser):
    """ Schema for show l2fib output-list {id} """

    schema = {
        'olist_id': int,
        'bd_id': int,
        'ref_cnt': int,
        'flags': str,
        Optional('ports'): list,
        'port_cnt': int,
        Optional('ports_desc'): {
            Any(): {
                'type': str,
                'is_pathlist': bool,
                Optional('desc'): {
                    'pl_id': int,
                    'pl_cnt': int,
                    'pl_type': str,
                    'pl_desc': str,
                }
            },
        }
    }


# =============================================
# Parser for 'show l2fib output-list <id>'
# =============================================
class ShowL2fibOlist(ShowL2fibOlistSchema):
    """ Parser for show l2fib output-list {id} """

    cli_command = ['show l2fib output-list {id}']

    def cli(self, id=None, output=None):

        if output is None:
            cli_output = self.device.execute(self.cli_command[0].format(id=id))
        else:
            cli_output = output

        # ID                            : 3
        p1 = re.compile(r'^ID\s+:\s+(?P<olist_id>\d+)$')

        # Bridge Domain                 : 11
        p2 = re.compile(r'^Bridge Domain\s+:\s+(?P<bd_id>\d+)$')

        # Reference Count               : 4
        p3 = re.compile(r'^Reference Count\s+:\s+(?P<ref_cnt>\d+)$')

        # Flags                         : flood list
        p4 = re.compile(r'^Flags\s+:\s+(?P<flags>[\w ]+)$')

        # Port Count                    : 3
        p5 = re.compile(r'^Port Count\s+:\s+(?P<port_cnt>\d+)$')

        # Port(s) : VXLAN_REP PL:1(1) T:VXLAN_REP [SMC]20011:227.0.0.1
        p6 = re.compile(r'^(Port\(s\)\s+)?'
                        r':\s+(?P<type>\w+)\s+'
                        r'PL:(?P<pl_id>\d+)\((?P<pl_cnt>\d+)\)\s+'
                        r'T:(?P<pl_type>\w+)\s+'
                        r'(?P<pl_desc>\[\w+\][0-9a-fA-F\.:@ ]+)$')

        # Port(s) : BD_PORT   Et0/1:11
        p7 = re.compile(r'^(Port\(s\)\s+)?'
                        r':\s+(?P<type>BD_PORT)\s+(?P<port>[\w:\/]+)$')

        parser_dict = {}

        with_ports = 'Port(s)' in cli_output
        if with_ports:
            ports = parser_dict.setdefault('ports', [])
            ports_desc = parser_dict.setdefault('ports_desc', {})

        for line in cli_output.splitlines():
            line = line.strip()
            if not line:
                continue

            # ID                            : 3
            m = p1.match(line)
            if m:
                group = m.groupdict()
                parser_dict.update({'olist_id': int(group['olist_id'])})
                continue

            # Bridge Domain                 : 11
            m = p2.match(line)
            if m:
                group = m.groupdict()
                parser_dict.update({'bd_id': int(group['bd_id'])})
                continue

            # Reference Count               : 4
            m = p3.match(line)
            if m:
                group = m.groupdict()
                parser_dict.update({'ref_cnt': int(group['ref_cnt'])})
                continue

            # Flags                         : flood list
            m = p4.match(line)
            if m:
                group = m.groupdict()
                parser_dict.update({'flags': group['flags']})
                continue

            # Port Count                    : 3
            m = p5.match(line)
            if m:
                group = m.groupdict()
                parser_dict.update({'port_cnt': int(group['port_cnt'])})
                continue

            if with_ports:
                # Port(s) : VXLAN_REP PL:1(1) T:VXLAN_REP [SMC]20011:227.0.0.1
                m = p6.match(line)
                if m:
                    group = m.groupdict()
                    port = group['pl_desc']

                    ports.append(port)
                    ports_desc.update({port: {
                        'type': group['type'],
                        'is_pathlist': True,
                        'desc': {'pl_id': int(group['pl_id']),
                                 'pl_cnt': int(group['pl_cnt']),
                                 'pl_type': group['pl_type'],
                                 'pl_desc': group['pl_desc']}
                    }})
                    continue

                # Port(s) : BD_PORT   Et0/1:11
                m = p7.match(line)
                if m:
                    group = m.groupdict()
                    port = group['port']

                    ports.append(port)
                    ports_desc.update({port: {'type': group['type'],
                                              'is_pathlist': False
                                              }
                                       })
                    continue

        return parser_dict


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
        #Adjacency                     : MPLS_UC   PL:5(2) T:MPLS_UC [MAC]16@2.2.2.1 ...
        #PD Adjacency                  : MPLS_UC   PL:5(2) T:MPLS_UC [MAC]16@2.2.2.1 ...
        p7 = re.compile(r'^(?P<tag>(Adjacency|PD Adjacency))\s+:\s+(?P<type>\w+)\s+PL:(?P<path_list_id>\d+)\((?P<path_list_count>\d+)\)'
                        r'\s+T:(?P<path_list_type>\w+)\s+(?P<path_list_desc>\[\w+\][0-9a-fA-F:@\.]+)(\s+...)?$')

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
            #Adjacency                     : MPLS_UC   PL:5(2) T:MPLS_UC [MAC]16@2.2.2.1 ...
            #PD Adjacency                  : MPLS_UC   PL:5(2) T:MPLS_UC [MAC]16@2.2.2.1 ...
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


# ======================================================
# Parser for 'show l2fib output-list '
# ======================================================

class ShowL2fibOutputListSchema(MetaParser):
    """Schema for show l2fib output-list"""

    schema = {
        'bridge_domain': {
            Any(): {
                'output_id': int,
                'port': int,
                'flags': str,
            },
        },
    }

class ShowL2fibOutputList(ShowL2fibOutputListSchema):
    """Parser for show l2fib output-list"""

    cli_command = 'show l2fib output-list'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # 1055 31   3    flood list
        p1 = re.compile(r"^(?P<output_id>\d+)\s+(?P<bridge_domain>\d+)\s+(?P<port>\d+)\s+(?P<flags>\S+\s+\S+)$")

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # 1055 31   3    flood list
            m = p1.match(line)
            if m:
                dict_val = m.groupdict()
                bridge_domain = int(dict_val['bridge_domain'])
                l2fib_dict = ret_dict.setdefault('bridge_domain', {})
                output_flag_dict = l2fib_dict.setdefault(bridge_domain, {})
                output_flag_dict['output_id'] = int(dict_val['output_id'])
                output_flag_dict['port'] = int(dict_val['port'])
                output_flag_dict['flags'] = dict_val['flags']
                continue

        return ret_dict


# ======================================================
# Parser for 'show l2fib output-list {output_id} '
# ======================================================

class ShowL2fibOutputListIdSchema(MetaParser):
    """Schema for show l2fib output-list {output_id}"""

    schema = {
        'output_id': {
            Any(): {
                'bridge_domain': int,
                'ref_count': int,
                'flags': str,
                'port_count': int,
                'ports': ListOf(str),
                'vlan_rep': ListOf(int),
                'vni_id': ListOf(int),
                'loopback_ip': ListOf(str),
            },
	}
    }

class ShowL2fibOutputListId(ShowL2fibOutputListIdSchema):
    """Parser for show l2fib output-list {output_id}"""

    cli_command = 'show l2fib output-list {output_id}'

    def cli(self, output_id, output=None):
        if output is None:
           output = self.device.execute(self.cli_command.format(output_id = output_id))

        # ID                            : 1225
        p1 = re.compile(r"^ID\s+:\s+(?P<output_id>\d+)$")
        # Bridge Domain                 : 201
        p2 = re.compile(r"^Bridge\s+Domain\s+:\s+(?P<bridge_domain>\d+)$")
        # Reference Count               : 1
        p3 = re.compile(r"^Reference\s+Count\s+:\s+(?P<ref_count>\d+)$")
        # Flags                         : flood list
        p4 = re.compile(r"^Flags\s+:\s+(?P<flags>\S+\s+\S+)$")
        # Port Count                    : 3
        p5 = re.compile(r"^Port\s+Count\s+:\s+(?P<port_count>\d+)$")
        # Port(s)                       : BD_PORT   Hu1/0/31:201
        p6 = re.compile(r"^Port\(s\)\s+:\s+BD_PORT\s+(?P<ports>\S+):\d+$")
        #                               : BD_PORT   Gi1/0/24:201
        p6_1 = re.compile(r"^:\s+BD_PORT\s+(?P<ports>\S+):\d+$")
        #                               : VXLAN_REP PL:1110(1) T:VXLAN_REP [IR]100201:172.11.1.1
        p7 = re.compile(r"^:\s+VXLAN_REP\s+PL:(?P<vlan_rep>\d+)\S+\s+T:VXLAN_REP\s+\[IR\](?P<vni_id>\d+)+:+(?P<loopback_ip>\S+)$")
        # Port(s)                       : VXLAN_REP PL:1110(1) T:VXLAN_REP [IR]100201:172.11.1.1
        p7_1 = re.compile(r"^Port\(s\)\s+:\s+VXLAN_REP\s+PL:(?P<vlan_rep>\d+)\S+\s+T:VXLAN_REP\s+\[IR\](?P<vni_id>\d+)+:+(?P<loopback_ip>\S+)$")

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # ID                            : 1225
            m = p1.match(line)
            if m:
                dict_val = m.groupdict()
                output_id = int(dict_val['output_id'])
                l2fib_dict = ret_dict.setdefault('output_id', {})
                output_flag_dict = l2fib_dict.setdefault(output_id, {})
                continue

            # Bridge Domain                 : 201
            m = p2.match(line)
            if m:
                dict_val = m.groupdict()
                output_flag_dict['bridge_domain'] = int(dict_val['bridge_domain'])
                continue

            # Reference Count               : 1
            m = p3.match(line)
            if m:
                dict_val = m.groupdict()
                output_flag_dict['ref_count'] = int(dict_val['ref_count'])
                continue

            # Flags                         : flood list
            m = p4.match(line)
            if m:
                dict_val = m.groupdict()
                output_flag_dict['flags'] = dict_val['flags']
                continue

            # Port Count                    : 3
            m = p5.match(line)
            if m:
                dict_val = m.groupdict()
                output_flag_dict['port_count'] = int(dict_val['port_count'])
                continue

            # Port(s)                       : BD_PORT   Hu1/0/31:201
            #                               : BD_PORT   Gi1/0/24:201

            m = p6.match(line) or p6_1.match(line)
            if m:
                port = m.groupdict()['ports']
                port_list = output_flag_dict.setdefault('ports',[])
                port_list.append(port)
                continue

            #                               : VXLAN_REP PL:1110(1) T:VXLAN_REP [IR]100201:172.11.1.1
            m = p7.match(line) or p7_1.match(line)
            if m:
                dict_val = m.groupdict()
                vlan_rep = int(dict_val['vlan_rep'])
                vlan_rep_list = output_flag_dict.setdefault('vlan_rep',[])
                vlan_rep_list.append(vlan_rep)
                vni_id = int(dict_val['vni_id'])
                vni_id_list = output_flag_dict.setdefault('vni_id',[])
                vni_id_list.append(vni_id)
                loopback_ip = dict_val['loopback_ip']
                loopback_ip_list = output_flag_dict.setdefault('loopback_ip',[])
                loopback_ip_list.append(loopback_ip)
                continue
        
        return ret_dict

# ========================================================================
# Schema for 'show l2fib bridge-domain <bd_id> detail'
# ========================================================================
class ShowL2fibBridgeDomainDetailSchema(MetaParser):
    """
    Schema for
                * 'show l2fib bridge-domain {bd_id} detail'
    """
    schema = {
        'bridge_domain':int,	
        'reference_count': int,
        'replication_ports_count': int,
        'unicast_addr_table_size': int,
        'ip_multicast_prefix_table_size': int,
        'flood_list_info': {
            'olist': int,
            'ports': int
        },
        Optional('port_info'): {
            Any():{
                'type': str,
                'description': str, 
                Optional('path_list_id'): int,
                Optional('path_list_count'): int,
                Optional('path_list_type'): str,
            }
        },
        Optional('unicast_addr_table_info'): {
            Any():{ 
                'type': str, 
                Optional('unicast_path_list'):{
                    'unicast_id': int, 
                    'unicast_path_count': int, 
                    'unicast_type': str, 
                    'unicast_description': str 
                }
            }
        },
        Optional('ip_multicast_prefix_table_info'): {
            Any():{
                'source': str,
                'group': str,
                'iif': str,
                'adjacency': str,
                'olist': int,
                'port_count': int
            }
        }
    }

# ==========================================================================================
# Parser for 'show l2fib bridge-domain <bd_id> detail'
# ==========================================================================================
class ShowL2fibBridgeDomainDetail(ShowL2fibBridgeDomainDetailSchema):
    """
    Parser for
        * 'show l2fib bridge-domain {bd_id} detail'
    """
    cli_command = 'show l2fib bridge-domain {bd_id} detail'

    def cli(self, bd_id, output=None):

        if output is None:
            output = self.device.execute(self.cli_command.format(bd_id=bd_id))

        #Bridge Domain : 101
        p1 =  re.compile(r'^Bridge Domain : (?P<bd_id>\d+)$')

        #Reference Count : 10
        p2 =  re.compile(r'^Reference Count : (?P<reference_count>\d+)$')

        #Replication ports count : 2
        p3 =  re.compile(r'^Replication ports count : (?P<replication_ports_count>\d+)$')

        #Unicast Address table size : 1
        p4 =  re.compile(r'^Unicast Address table size : (?P<unicast_addr_table_size>\d+)$')

        #IP Multicast Prefix table size : 3
        p5 =  re.compile(r'^IP Multicast Prefix table size : (?P<ip_multicast_pref_table_size>\d+)$')

        #Olist: 1125, Ports: 2
        p6 =  re.compile(r'^Olist: (?P<olist>\d+)\,\s*Ports: (?P<port_count>\d+)$')

        #BD_PORT   Gi1/0/10:101
        p7 =  re.compile(r'^(?P<port_type>BD_PORT)\s+(?P<desc>[\w:\/]+)$')

        #VXLAN_REP PL:25(1) T:VXLAN_REP [IR]10101:172.16.254.2
        p8 =  re.compile(r'^(?P<type>\w+)\s+PL:(?P<path_list_id>\d+)\((?P<path_count>\d+)\)\s'
                        r'+T:(?P<path_list_type>\w+)\s+(?P<desc>[\[\]\w:.]+)$')

        #44d3.ca28.6cc2  VXLAN_UC  PL:24(1) T:VXLAN_UC [MAC]10101:172.16.254.2
        p9 =  re.compile(r'^(?P<unicast_mac_addr>[a-fA-F0-9\.]+)\s+(?P<type>\w+)\s'
                        r'+PL:(?P<path_list_id>\d+)\((?P<path_count>\d+)\)\s+T:(?P<path_list_type>\w+)\s'
                        r'+(?P<path_list_desc>[\w\[\]:.]+)$') 

        #Source: *, Group: 224.0.0.0/24, IIF: Null, Adjacency: Olist: 1125, Ports: 2  
        p10 =  re.compile(r'^Source: (?P<source>[\w*]+),\s+Group: (?P<group>[\d.\/]+),\s'
                        r'+IIF: (?P<iif>\w+),\s+Adjacency:(?P<adjacency>[\s\S]+)Olist:\s'
                        r'+(?P<olist>\d+),\s+Ports:\s+(?P<port_count>\d+)$')   

        ret_dict = {}		
        for line in output.splitlines():
            line = line.strip()

            #Bridge Domain : 101
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['bridge_domain']=int(group['bd_id'])
                continue

            #Reference Count : 10
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict['reference_count'] = int(group['reference_count'])
                continue

            #Replication ports count : 2
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict['replication_ports_count'] = int(group['replication_ports_count'])
                continue

            #Unicast Address table size : 1
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ret_dict['unicast_addr_table_size'] = int(group['unicast_addr_table_size'])
                continue

            #IP Multicast Prefix table size : 3
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ret_dict['ip_multicast_prefix_table_size'] = int(group['ip_multicast_pref_table_size'])
                continue

            #Olist: 1125, Ports: 2
            m = p6.match(line)
            if m:
                group = m.groupdict()
                flood_dict = ret_dict.setdefault('flood_list_info',{})
                flood_dict['olist'] = int(group['olist'])
                flood_dict['ports'] = int(group['port_count'])
                continue

            #BD_PORT   Gi1/0/10:101
            m = p7.match(line)
            if m:
                group = m.groupdict()
                port_dict = ret_dict.setdefault('port_info',{}).setdefault(group['desc'],{})
                port_dict['type'] = group['port_type']
                port_dict['description'] = group['desc']
                continue

            #VXLAN_REP PL:25(1) T:VXLAN_REP [IR]10101:172.16.254.2
            m = p8.match(line)
            if m:
                group = m.groupdict()
                port_dict = ret_dict.setdefault('port_info',{}).setdefault(group['desc'],{})
                port_dict['type'] = group['type']
                port_dict['path_list_id'] = int(group['path_list_id'])
                port_dict['path_list_count'] = int(group['path_count'])
                port_dict['path_list_type'] = group['path_list_type']
                port_dict['description'] = group['desc']
                continue

            #44d3.ca28.6cc2  VXLAN_UC  PL:24(1) T:VXLAN_UC [MAC]10101:172.16.254.2
            m = p9.match(line)
            if m:
                group = m.groupdict()
                unicast_dict = ret_dict.setdefault('unicast_addr_table_info',{}).setdefault(group['unicast_mac_addr'],{})
                unicast_dict['type'] = group['type']
                # unicast_dict['unicast_mac_addr'] = group['unicast_mac_addr']
                unipath_dict = unicast_dict.setdefault('unicast_path_list',{})
                unipath_dict['unicast_id'] = int(group['path_list_id'])
                unipath_dict['unicast_path_count'] = int(group['path_count'])
                unipath_dict['unicast_type'] = group['path_list_type']
                unipath_dict['unicast_description'] = group['path_list_desc']
                continue

            #Source: *, Group: 224.0.0.0/24, IIF: Null, Adjacency: Olist: 1125, Ports: 2  
            m = p10.match(line)
            if m:
                group = m.groupdict()
                ip_dict = ret_dict.setdefault('ip_multicast_prefix_table_info',{}).setdefault(group['group'],{})
                ip_dict['source'] = group['source']
                ip_dict['group'] = group['group']
                ip_dict['iif'] = group['iif']
                ip_dict['adjacency'] = group['adjacency']
                ip_dict['olist'] = int(group['olist'])
                ip_dict['port_count'] = int(group['port_count'])
                continue

        return ret_dict
