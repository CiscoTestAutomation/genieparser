"""show_routing.py

NXOS parser for the following show commands:
    * show routing vrf all
    * show routing ipv6 vrf all
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Or, And,\
                                         Default, Use
                                         
# import parser utils
from genie.libs.parser.utils.common import Common

# =================================
# Parser for 'show routing vrf all'
# =================================

class ShowRoutingVrfAllSchema(MetaParser):
    """Schema for show routing vrf all"""

    schema = {
        'vrf':
            {Any():
                {Optional('address_family'):
                    {Any():
                        {Optional('bgp_distance_extern_as'): int,
                        Optional('bgp_distance_internal_as'): int,
                        Optional('bgp_distance_local'): int,
                        'ip':
                            {Any():
                                {'ubest_num': str,
                                'mbest_num': str,
                                Optional('attach'): str,
                                Optional('best_route'):
                                    {Optional(Any()):
                                        {Optional('nexthop'):
                                            {Optional(Any()):
                                                {Optional('protocol'):
                                                    {Optional(Any()):
                                                        {Optional('route_table'): str,
                                                        Optional('uptime'): str,
                                                        Optional('interface'): str,
                                                        Optional('preference'): str,
                                                        Optional('metric'): str,
                                                        Optional('protocol_id'): str,
                                                        Optional('attribute'): str,
                                                        Optional('tag'): str, 
                                                        Optional('mpls'): bool,
                                                        Optional('mpls_vpn'): bool,
                                                        Optional('evpn'): bool,
                                                        Optional('segid'): int,
                                                        Optional('tunnelid'): str,
                                                        Optional('encap'): str,
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }


class ShowRoutingVrfAll(ShowRoutingVrfAllSchema):
    """Parser for show ip routing vrf all"""
    cli_command = ['show routing {ip} vrf all', 'show routing vrf all']

    def cli(self, ip='',output=None):
        if ip:
            cmd = self.cli_command[0].format(ip=ip)
        else:
            cmd = self.cli_command[1]

        # excute command to get output
        if output is None:
            out = self.device.execute(cmd)
        else:
            out = output
        
        # Init dict
        bgp_dict = {}
        sub_dict = {}
        address_family = None

        for line in out.splitlines():
            line = line.strip()

            # IP Route Table for VRF "default"
            # IPv6 Routing Table for VRF "default"
            p1 = re.compile(r'^(IP|IPv6) +(Route|Routing) +Table +for +VRF +"(?P<vrf>\w+)"$')
            m = p1.match(line)
            if m:
                vrf = str(m.groupdict()['vrf'])
                if vrf == 'default' and not ip:
                    address_family = 'ipv4 unicast'
                elif vrf != 'default' and not ip:
                    address_family = 'vpnv4 unicast'
                elif vrf == 'default' and ip:
                    address_family = 'ipv6 unicast'
                elif vrf != 'default' and ip:
                    address_family = 'vpnv6 unicast'
                continue

            # 20.43.0.1/32, ubest/mbest: 1/0 time, attached
            # 55.0.9.0/24, ubest/mbest: 1/0 time
            p2 = re.compile(r'(?P<ip_mask>[\w\:\.\/]+), +ubest/mbest: +'
                             '(?P<ubest>\d+)/(?P<mbest>\d+)( +time)?'
                             '(, +(?P<attach>\w+))?$')
            m = p2.match(line)
            if m:
                # Init vrf dict
                if 'vrf' not in bgp_dict:
                    bgp_dict['vrf'] = {}
                if vrf and vrf not in bgp_dict['vrf']:
                    bgp_dict['vrf'][vrf] = {}
                
                # Init address_family dict
                if 'address_family' not in bgp_dict['vrf'][vrf]:
                    bgp_dict['vrf'][vrf]['address_family'] = {}
                if address_family is not None and \
                   address_family not in bgp_dict['vrf'][vrf]['address_family']:
                   bgp_dict['vrf'][vrf]['address_family'][address_family] = {}

                # Create sub_dict
                sub_dict = bgp_dict['vrf'][vrf]['address_family'][address_family]

                # Init ip dict
                ip_mask = m.groupdict()['ip_mask']
                if 'ip' not in sub_dict:
                    sub_dict['ip'] = {}
                if ip_mask not in sub_dict['ip']:
                    sub_dict['ip'][ip_mask] = {}
                
                sub_dict['ip'][ip_mask]['ubest_num'] = m.groupdict()['ubest']
                sub_dict['ip'][ip_mask]['mbest_num'] = m.groupdict()['mbest']
                if m.groupdict()['attach']:
                    sub_dict['ip'][ip_mask]['attach'] = m.groupdict()['attach']
                    continue

            # *via fec1::1002%default, Eth1/1, [200/4444], 15:57:39, bgp-333, internal, tag 333
            # *via 3.3.3.3%default, [33/0], 5w0d, bgp-100, internal, tag 100 (mpls-vpn)
            # *via 2001:db8::5054:ff:fed5:63f9, Eth1/1, [0/0], 00:15:46, direct,
            # *via 2001:db8:2:2::2, Eth1/1, [0/0], 00:15:46, direct, , tag 222
            # *via 100.0.130.2%default, [200/0], 3d07h, bgp-1, internal, tag 1 (evpn), segid: 50009 tunnelid: 0x64008202 encap: VXLAN
            p3 = re.compile(r'^(?P<cast>.*)via +(?P<nexthop>[\w\.\:\s]+)'
                             '(%(?P<table>[\w\:]+))?, *'
                             '((?P<int>[a-zA-Z0-9\./_]+),)? *'
                             '\[(?P<preference>\d+)/(?P<metric>\d+)\], *'
                             '(?P<up_time>[\w\:\.]+), *'
                             '(?P<protocol>\w+)(\-(?P<process>\d+))?,? *'
                             '(?P<attribute>\w+)?,? *'
                             '(tag *(?P<tag>\w+))?,? *(?P<vpn>[a-zA-Z\(\)\-]+)?'
                             ',?( +segid: +(?P<segid>\d+))?,?( +tunnelid: +'
                             '(?P<tunnelid>[0-9x]+))?,?( +encap: +'
                             '(?P<encap>[a-zA-Z0-9]+))?$')
            m = p3.match(line)
            if m:
                cast = m.groupdict()['cast']
                cast = {'1': 'unicast',
                        '2': 'multicast'}['{}'.format(cast.count('*'))]

                 # Init 'best_route' dict
                if 'best_route' not in sub_dict['ip'][ip_mask]:
                    sub_dict['ip'][ip_mask]['best_route'] = {}
                if cast not in sub_dict['ip'][ip_mask]['best_route']:
                    sub_dict['ip'][ip_mask]['best_route'][cast] = {}
                    sub_dict['ip'][ip_mask]['best_route'][cast]\
                        ['nexthop'] = {}

                nexthop = m.groupdict()['nexthop']
                if nexthop not in sub_dict\
                   ['ip'][ip_mask]['best_route'][cast]['nexthop']:
                    sub_dict['ip'][ip_mask]\
                      ['best_route'][cast]['nexthop'][nexthop] = {}
                    prot_dict = sub_dict['ip'][ip_mask]\
                      ['best_route'][cast]['nexthop'][nexthop]['protocol'] = {}

                protocol = m.groupdict()['protocol'] if \
                    m.groupdict()['protocol'] else m.groupdict()['prot']
                if protocol not in prot_dict:
                    prot_dict[protocol] = {}

                table = m.groupdict()['table']
                if table:
                    prot_dict[protocol]['route_table'] = table

                intf = m.groupdict()['int']
                if intf:
                    prot_dict[protocol]['interface'] = Common.convert_intf_name(intf)

                preference = m.groupdict()['preference']
                if preference:
                    prot_dict[protocol]['preference'] = preference

                metric = m.groupdict()['metric']
                if metric:
                    prot_dict[protocol]['metric'] = metric

                up_time = m.groupdict()['up_time']
                if up_time:
                    prot_dict[protocol]['uptime'] = up_time

                process = m.groupdict()['process']
                if process:
                    prot_dict[protocol]['protocol_id'] = process

                attribute = m.groupdict()['attribute']
                if attribute:
                    prot_dict[protocol]['attribute'] = attribute
                
                tag = m.groupdict()['tag']
                if tag:
                    prot_dict[protocol]['tag'] = tag.strip()
                
                segid = m.groupdict()['segid']
                if segid:
                    prot_dict[protocol]['segid'] = int(segid)

                tunnelid = m.groupdict()['tunnelid']
                if tunnelid:
                    prot_dict[protocol]['tunnelid'] = tunnelid

                encap = m.groupdict()['encap']
                if encap:
                    prot_dict[protocol]['encap'] = encap.lower()

                vpn = m.groupdict()['vpn']
                if vpn and 'mpls-vpn' in vpn:
                    prot_dict[protocol]['mpls_vpn'] = True
                elif vpn and 'mpls' in vpn:
                    prot_dict[protocol]['mpls'] = True
                elif vpn and 'evpn' in vpn:
                    prot_dict[protocol]['evpn'] = True

                # Set extra values for BGP Ops
                if attribute == 'external' and protocol == 'bgp':
                    sub_dict['bgp_distance_extern_as'] = int(preference)
                elif attribute == 'internal' and protocol == 'bgp':
                    sub_dict['bgp_distance_internal_as'] = int(preference)
                elif attribute == 'discard' and protocol == 'bgp':
                    sub_dict['bgp_distance_local'] = int(preference)
                    continue

        return bgp_dict


class ShowRoutingIpv6VrfAll(ShowRoutingVrfAll):
    """Parser for show ipv6 routing vrf all"""

    def cli(self,output=None):
        return(super().cli(ip='ipv6',output=output))


# ====================================================
#  schema for show ip route
# ====================================================
class ShowIpRouteSchema(MetaParser):
    """Schema for:
        show ip route
        show ip route vrf all"""

    schema = {
        'vrf': {
            Any(): {
                Optional('address_family'): {
                    Any(): {
                        Optional('routes'): {
                            Any(): {
                                Optional('route'): str,
                                Optional('ubest'): int,
                                Optional('mbest'): int,
                                Optional('source_protocol'): str,
                                Optional('source_protocol_status'): str,
                                Optional('process_id'): str,
                                Optional('route_preference'): int,
                                Optional('metric'): int,
                                Optional('tag'): int,
                                Optional('attached'): bool,
                                Optional('active'): bool,
                                Optional('next_hop'): {
                                    Optional('outgoing_interface'): {
                                        Any(): {  # interface  if there is no next_hop
                                            Optional('outgoing_interface'): str,
                                            Optional('updated'): str,
                                            Optional('best_ucast_nexthop'): bool,
                                            Optional('best_mcast_nexthop'): bool,
                                        },
                                    },
                                    Optional('next_hop_list'): {
                                        Any(): {  # index
                                            Optional('index'): int,
                                            Optional('next_hop'): str,
                                            Optional('next_hop_vrf'): str,
                                            Optional('best_ucast_nexthop'): bool,
                                            Optional('best_mcast_nexthop'): bool,
                                            Optional('outgoing_interface'): str,
                                            Optional('updated'): str,
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }


# ====================================================
#  parser for show ip route
# ====================================================
class ShowIpRoute(ShowIpRouteSchema):
    """Parser for :
       show ip route
       show ip route vrf <vrf>
       show ip route vrf all"""
    cli_command = ['show ip route vrf {vrf}', 'show ip route vrf']

    def cli(self, vrf='', output=None):
        if vrf:
            cmd = self.cli_command[0].format(vrf=vrf)
        else:
            vrf = 'default'
            cmd = self.cli_command[1]

        # excute command to get output
        if output is None:
            out = self.device.execute(cmd)
        else:
            out = output

        af = 'ipv4'
        route = ""

        result_dict = {}
        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue

            # IP Route Table for VRF "default"
            p1 = re.compile(r'^\s*IP +Route +Table +for VRF +\"(?P<vrf>[\w\_]+)\"$')
            m = p1.match(line)
            if m:
                vrf = m.groupdict()['vrf']
                continue

            # 1.1.1.1/32, ubest/mbest: 2/0
            # 3.3.3.3/32, ubest/mbest: 2/0, attached
            # 11.0.0.0/24, ubest/mbest: 1/0 time, attached
            # 90.77.77.1/32, ubest/mbest: 1/0 time
            p2 = re.compile(r'^\s*(?P<route>[\d\/\.]+)'
                            ', +ubest/mbest: +(?P<ubest_mbest>[\d\/]+)'
                            '( +time)?(, +(?P<attached>[\w]+))?$')
            m = p2.match(line)
            if m:
                active = True
                ubest = mcbest = route_preference = ""
                if m.groupdict()['ubest_mbest']:
                    ubest_mbest = m.groupdict()['ubest_mbest']
                    if '/' in ubest_mbest:
                        ubest = ubest_mbest.split('/')[0]
                        mbest = ubest_mbest.split('/')[1]

                route = m.groupdict()['route']
                index = 1
                if m.groupdict()['attached']:
                    if 'attached' in m.groupdict()['attached']:
                        attached = True
                    else:
                        attached = False

                if vrf:
                    if 'vrf' not in result_dict:
                        result_dict['vrf'] = {}

                    if vrf not in result_dict['vrf']:
                        result_dict['vrf'][vrf] = {}

                    if 'address_family' not in result_dict['vrf'][vrf]:
                        result_dict['vrf'][vrf]['address_family'] = {}

                    if af and af not in result_dict['vrf'][vrf]['address_family']:
                        result_dict['vrf'][vrf]['address_family'][af] = {}

                    if 'routes' not in result_dict['vrf'][vrf]['address_family'][af]:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'] = {}
                    if route not in result_dict['vrf'][vrf]['address_family'][af]['routes']:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route] = {}

                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['route'] = route
                    if ubest:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['ubest'] = int(ubest)
                    if mbest:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['mbest'] = int(mbest)

                    if m.groupdict()['attached']:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['attached'] = attached

                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                        ['active'] = active

                continue

            # *via 10.2.3.2, Eth1/4, [1/0], 01:01:30, static
            # *via 10.1.3.1, Eth1/2, [110/41], 01:01:18, ospf-1, intra
            # *via 11.11.11.11, [200/0], 01:01:12, bgp-100, internal, tag 100
            p3 = re.compile(r'^\s*(?P<star>[*]+)via +(?P<next_hop>[\d\.]+),'
                            '( +(?P<interface>[\w\/\.]+))?,? +\[(?P<route_preference>[\d\/]+)\],'
                            ' +(?P<date>[0-9][\w\:]+)?,?( +(?P<source_protocol>[\w\-]+))?,?'
                            '( +(?P<source_protocol_status>[\w]+))?,?( +tag +(?P<tag>[\d]+))?$')
            m = p3.match(line)
            if m:
                tag = process_id = source_protocol_status = interface = next_hop_vrf= ""
                star = m.groupdict()['star']
                if len(star) == 1:
                    cast = 'best_ucast_nexthop'
                if len(star) == 2:
                    cast = 'best_mcast_nexthop'

                if m.groupdict()['next_hop']:
                    next_hop = m.groupdict()['next_hop']
                    if '%' in next_hop:
                        next_hop_vrf = next_hop.split('%')[1]
                        next_hop = next_hop.split('%')[0]

                if m.groupdict()['route_preference']:
                    routepreference = m.groupdict()['route_preference']
                    if '/' in routepreference:
                        route_preference = routepreference.split('/')[0]
                        metrics = routepreference.split('/')[1]

                if m.groupdict()['interface']:
                    interface = Common.convert_intf_name(m.groupdict()['interface'])

                if m.groupdict()['date']:
                    updated = m.groupdict()['date']

                if m.groupdict()['source_protocol_status']:
                    source_protocol_status = m.groupdict()['source_protocol_status']

                if m.groupdict()['source_protocol']:
                    if '-' in m.groupdict()['source_protocol']:
                        source_protocol = m.groupdict()['source_protocol'].split('-')[0]
                        process_id = m.groupdict()['source_protocol'].split('-')[1]
                    else:
                        if index > 1 :
                            source_protocol_second = m.groupdict()['source_protocol']
                            if source_protocol_second != source_protocol:
                                if 'local' in source_protocol_second or 'local' in source_protocol_second:
                                        source_protocol = 'local'
                                else:
                                    source_protocol = source_protocol
                        else:
                            source_protocol = m.groupdict()['source_protocol']

                if m.groupdict()['tag']:
                    tag = m.groupdict()['tag']

                if vrf:
                    if 'vrf' not in result_dict:
                        result_dict['vrf'] = {}

                    if vrf not in result_dict['vrf']:
                        result_dict['vrf'][vrf] = {}

                    if 'address_family' not in result_dict['vrf'][vrf]:
                        result_dict['vrf'][vrf]['address_family'] = {}

                    if af and af not in result_dict['vrf'][vrf]['address_family']:
                        result_dict['vrf'][vrf]['address_family'][af] = {}

                    if 'routes' not in result_dict['vrf'][vrf]['address_family'][af]:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'] = {}
                    if route not in result_dict['vrf'][vrf]['address_family'][af]['routes']:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route] = {}

                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['route'] = route


                    if metrics:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                            ['metric'] = int(metrics)
                    if route_preference:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                            ['route_preference'] = int(route_preference)
                    if process_id:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]\
                            ['process_id'] = process_id
                    if source_protocol:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]\
                            ['source_protocol'] = source_protocol

                    if source_protocol_status:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]\
                            ['source_protocol_status'] = source_protocol_status

                    if tag:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]\
                            ['tag'] = int(tag)

                    if 'next_hop' not in result_dict['vrf'][vrf]['address_family'][af]['routes'][route]:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] = {}

                    if not next_hop:
                        if 'outgoing_interface' not in result_dict['vrf'][vrf]['address_family'][af] \
                                ['routes'][route]['next_hop']:
                            result_dict['vrf'][vrf]['address_family'][af]['routes'][route]\
                                ['next_hop']['outgoing_interface'] = {}

                        if m.groupdict()['interface'] and interface not in \
                                result_dict['vrf'][vrf]['address_family'][af]['routes'][route]\
                                ['next_hop']['outgoing_interface']:
                            result_dict['vrf'][vrf]['address_family'][af]['routes'][route]\
                                ['next_hop']['outgoing_interface'][interface] = {}

                        if interface:
                            result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                                ['next_hop']['outgoing_interface'][interface]['outgoing_interface'] = interface

                        if updated:
                            result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                                ['outgoing_interface'][interface]['updated'] = updated


                    else:
                        if 'next_hop_list' not in result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop']:
                            result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'][
                                'next_hop_list'] = {}

                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                            ['next_hop_list'][index] = {}

                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                            ['next_hop_list'][index]['index'] = index

                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                            ['next_hop_list'][index]['next_hop'] = next_hop

                        if cast:
                            result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                            ['next_hop_list'][index][cast] = True

                        if updated:
                            result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                                ['next_hop_list'][index]['updated'] = updated

                        if interface:
                            result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                                ['next_hop_list'][index]['outgoing_interface'] = interface
                        if next_hop_vrf:
                            result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                                ['next_hop_list'][index]['next_hop_vrf'] = next_hop_vrf

                index += 1

                continue

        return result_dict


# ====================================================
#  schema for show ipv6 route
# ====================================================
class ShowIpv6RouteSchema(MetaParser):
    """Schema for:
        show ipv6 route
        show ipv6 route vrf all"""

    schema = {
        'vrf': {
            Any(): {
                Optional('address_family'): {
                    Any(): {
                        Optional('routes'): {
                            Any(): {
                                Optional('route'): str,
                                Optional('ubest'): int,
                                Optional('mbest'): int,
                                Optional('source_protocol'): str,
                                Optional('source_protocol_status'): str,
                                Optional('process_id'): str,
                                Optional('route_preference'): int,
                                Optional('metric'): int,
                                Optional('tag'): int,
                                Optional('attached'): bool,
                                Optional('active'): bool,
                                Optional('next_hop'): {
                                    Optional('outgoing_interface'): {
                                        Any(): {  # interface  if there is no next_hop
                                            Optional('outgoing_interface'): str,
                                            Optional('updated'): str,
                                            Optional('best_ucast_nexthop'): bool,
                                            Optional('best_mcast_nexthop'): bool,
                                        },
                                    },
                                    Optional('next_hop_list'): {
                                        Any(): {  # index
                                            Optional('index'): int,
                                            Optional('next_hop'): str,
                                            Optional('next_hop_vrf'): str,
                                            Optional('next_hop_af'): str,
                                            Optional('best_ucast_nexthop'): bool,
                                            Optional('best_mcast_nexthop'): bool,
                                            Optional('outgoing_interface'): str,
                                            Optional('updated'): str,
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }


# ====================================================
#  parser for show ipv6 route
# ====================================================
class ShowIpv6Route(ShowIpv6RouteSchema):
    """Parser for :
       show ipv6 route
       show ipv6 route vrf <vrf>
       show ipv6 route vrf all"""

    cli_command = ['show ipv6 route vrf {vrf}', 'show ipv6 route']

    def cli(self, vrf='', output=None):
        if vrf and vrf != 'default':
            cmd = self.cli_command[0].format(vrf=vrf)
        else:
            vrf = 'default'
            cmd = self.cli_command[1]

        # excute command to get output
        if output is None:
            out = self.device.execute(cmd)
        else:
            out = output

        af = 'ipv6'
        route = ""

        result_dict = {}
        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue

            # IP Route Table for VRF "default"
            p1 = re.compile(r'^\s*IPv6 +Routing +Table +for VRF +\"(?P<vrf>[\w]+)\"$')
            m = p1.match(line)
            if m:
                vrf = m.groupdict()['vrf']
                continue

            # 1.1.1.1/32, ubest/mbest: 2/0
            # 3.3.3.3/32, ubest/mbest: 2/0, attached
            # 2004:ab4:123:13::1/128, ubest/mbest: 1/0, attached
            p2 = re.compile(r'^\s*(?P<route>[\w\/\:]+)'
                            ', +ubest/mbest: +(?P<ubest_mbest>[\d\/]+)(, +(?P<attached>[\w]+))?$')
            m = p2.match(line)
            if m:

                active = True
                ubest = mbest = route_preference = ""
                if m.groupdict()['ubest_mbest']:
                    ubest_mbest = m.groupdict()['ubest_mbest']
                    if '/' in ubest_mbest:
                        ubest = ubest_mbest.split('/')[0]
                        mbest = ubest_mbest.split('/')[1]

                route = m.groupdict()['route']
                index = 1
                if m.groupdict()['attached']:
                    if 'attached' in m.groupdict()['attached']:
                        attached = True
                    else:
                        attached = False

                if vrf:
                    if 'vrf' not in result_dict:
                        result_dict['vrf'] = {}

                    if vrf not in result_dict['vrf']:
                        result_dict['vrf'][vrf] = {}

                    if 'address_family' not in result_dict['vrf'][vrf]:
                        result_dict['vrf'][vrf]['address_family'] = {}

                    if af and af not in result_dict['vrf'][vrf]['address_family']:
                        result_dict['vrf'][vrf]['address_family'][af] = {}

                    if 'routes' not in result_dict['vrf'][vrf]['address_family'][af]:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'] = {}
                    if route not in result_dict['vrf'][vrf]['address_family'][af]['routes']:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route] = {}

                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['route'] = route
                    if ubest:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['ubest'] = int(ubest)
                    if mbest:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['mbest'] = int(mbest)

                    if m.groupdict()['attached']:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['attached'] = attached

                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                        ['active'] = active

                continue

            # *via 10.2.3.2, Eth1/4, [1/0], 01:01:30, static
            # *via 10.1.3.1, Eth1/2, [110/41], 01:01:18, ospf-1, intra
            # *via 11.11.11.11, [200/0], 01:01:12, bgp-100, internal, tag 100
            p3 = re.compile(r'^\s*(?P<star>[*]+)via +(?P<next_hop>[\w\.\:\%]+),'
                            '( +(?P<interface>[\w\/\.]+))?,? +\[(?P<route_preference>[\d\/]+)\],'
                            ' +(?P<date>[0-9][\w\:]+)?,?( +(?P<source_protocol>[\w\-]+))?,?'
                            '( +(?P<source_protocol_status>[\w]+))?,?( +tag +(?P<tag>[\d]+))?$')
            m = p3.match(line)
            if m:
                tag = process_id = source_protocol_status = interface =\
                    nexthop_vrf = next_hop_vrf = next_hop_af= ""
                star = m.groupdict()['star']
                if len(star) == 1:
                    cast = 'best_ucast_nexthop'
                if len(star) == 2:
                    cast = 'best_mcast_nexthop'

                if m.groupdict()['next_hop']:
                    next_hop = m.groupdict()['next_hop']
                    if '%' in next_hop:
                        nexthop_vrf = next_hop.split('%')[1]
                        next_hop = next_hop.split('%')[0]
                        if ':' in nexthop_vrf:
                            next_hop_vrf = nexthop_vrf.split(':')[0]
                            next_hop_af = nexthop_vrf.split(':')[1].lower()


                if m.groupdict()['route_preference']:
                    routepreference = m.groupdict()['route_preference']
                    if '/' in routepreference:
                        route_preference = routepreference.split('/')[0]
                        metrics = routepreference.split('/')[1]

                if m.groupdict()['interface']:
                    interface = Common.convert_intf_name(m.groupdict()['interface'])

                if m.groupdict()['date']:
                    updated = m.groupdict()['date']

                if m.groupdict()['source_protocol_status']:
                    source_protocol_status = m.groupdict()['source_protocol_status']

                if m.groupdict()['source_protocol']:
                    if '-' in m.groupdict()['source_protocol']:
                        source_protocol = m.groupdict()['source_protocol'].split('-')[0]
                        process_id = m.groupdict()['source_protocol'].split('-')[1]
                    else:
                        if index > 1 :
                            source_protocol_second = m.groupdict()['source_protocol']
                            if source_protocol_second != source_protocol:
                                if 'local' in source_protocol_second or 'local' in source_protocol_second:
                                        source_protocol = 'local'
                                else:
                                    source_protocol = source_protocol
                        else:
                            source_protocol = m.groupdict()['source_protocol']

                if m.groupdict()['tag']:
                    tag = m.groupdict()['tag']

                if vrf:
                    if 'vrf' not in result_dict:
                        result_dict['vrf'] = {}

                    if vrf not in result_dict['vrf']:
                        result_dict['vrf'][vrf] = {}

                    if 'address_family' not in result_dict['vrf'][vrf]:
                        result_dict['vrf'][vrf]['address_family'] = {}

                    if af and af not in result_dict['vrf'][vrf]['address_family']:
                        result_dict['vrf'][vrf]['address_family'][af] = {}

                    if 'routes' not in result_dict['vrf'][vrf]['address_family'][af]:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'] = {}
                    if route not in result_dict['vrf'][vrf]['address_family'][af]['routes']:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route] = {}

                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['route'] = route


                    if metrics:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                            ['metric'] = int(metrics)
                    if route_preference:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                            ['route_preference'] = int(route_preference)
                    if process_id:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]\
                            ['process_id'] = process_id
                    if source_protocol:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]\
                            ['source_protocol'] = source_protocol

                    if source_protocol_status:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]\
                            ['source_protocol_status'] = source_protocol_status

                    if tag:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]\
                            ['tag'] = int(tag)

                    if 'next_hop' not in result_dict['vrf'][vrf]['address_family'][af]['routes'][route]:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] = {}

                    if not next_hop:
                        if 'outgoing_interface' not in result_dict['vrf'][vrf]['address_family'][af] \
                                ['routes'][route]['next_hop']:
                            result_dict['vrf'][vrf]['address_family'][af]['routes'][route]\
                                ['next_hop']['outgoing_interface'] = {}

                        if m.groupdict()['interface'] and interface not in \
                                result_dict['vrf'][vrf]['address_family'][af]['routes'][route]\
                                ['next_hop']['outgoing_interface']:
                            result_dict['vrf'][vrf]['address_family'][af]['routes'][route]\
                                ['next_hop']['outgoing_interface'][interface] = {}

                        if interface:
                            result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                                ['next_hop']['outgoing_interface'][interface]['outgoing_interface'] = interface

                        if updated:
                            result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                                ['outgoing_interface'][interface]['updated'] = updated


                    else:
                        if 'next_hop_list' not in result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop']:
                            result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'][
                                'next_hop_list'] = {}

                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                            ['next_hop_list'][index] = {}

                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                            ['next_hop_list'][index]['index'] = index

                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                            ['next_hop_list'][index]['next_hop'] = next_hop

                        if cast:
                            result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                            ['next_hop_list'][index][cast] = True

                        if updated:
                            result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                                ['next_hop_list'][index]['updated'] = updated

                        if interface:
                            result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                                ['next_hop_list'][index]['outgoing_interface'] = interface

                        if next_hop_af:
                            result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                                ['next_hop_list'][index]['next_hop_af'] = next_hop_af
                        if nexthop_vrf:
                            result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                                ['next_hop_list'][index]['next_hop_vrf'] = next_hop_vrf if next_hop_vrf else nexthop_vrf

                index += 1
                continue

            # tag 100
            p5 = re.compile(r'^\s*tag +(?P<tag>[\d]+)$')
            m = p5.match(line)
            if m:
                tag = m.groupdict()['tag']
                result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['tag'] = int(tag)

            continue

        return result_dict
