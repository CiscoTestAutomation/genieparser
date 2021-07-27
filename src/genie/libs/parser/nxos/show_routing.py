"""show_routing.py

NXOS parser for the following show commands:
    * show routing vrf all
    * show routing ipv6 vrf all
    * show ip route {route} {protocol} interface {interface} vrf {vrf}
    * show ip route {route} {protocol} interface {interface}
    * show ip route {route} {protocol} vrf {vrf}
    * show ip route {protocol} interface {interface} vrf {vrf}
    * show ip route {route} interface {interface} vrf {vrf}
    * show ip route {route} {protocol}
    * show ip route {protocol} interface {interface}
    * show ip route {protocol} vrf {vrf}
    * show ip route {route} interface {interface}
    * show ip route {route} vrf {vrf}
    * show ip route interface {interface} vrf {vrf}
    * show ip route {protocol}
    * show ip route {route}
    * show ip route interface {interface}
    * show ip route vrf {vrf}
    * show ip route vrf all
    * show ip route
    * show ipv6 route {route} {protocol} interface {interface} vrf {vrf}
    * show ipv6 route {route} {protocol} interface {interface}
    * show ipv6 route {route} {protocol} vrf {vrf}
    * show ipv6 route {protocol} interface {interface} vrf {vrf}
    * show ipv6 route {route} interface {interface} vrf {vrf}
    * show ipv6 route {route} {protocol}
    * show ipv6 route {protocol} interface {interface}
    * show ipv6 route {protocol} vrf {vrf}
    * show ipv6 route {route} interface {interface}
    * show ipv6 route {route} vrf {vrf}
    * show ipv6 route interface {interface} vrf {vrf}
    * show ipv6 route {protocol}
    * show ipv6 route {route}
    * show ipv6 route interface {interface}
    * show ipv6 route vrf {vrf}
    * show ipv6 route vrf all
    * show ipv6 route
    * show ip route summary vrf {vrf}
    * show ip route summary
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
        'vrf': {
            Any(): {
                Optional('address_family'): {
                    Any():{
                        Optional('bgp_distance_extern_as'): int,
                        Optional('bgp_distance_internal_as'): int,
                        Optional('bgp_distance_local'): int,
                        'ip': {
                            Any(): {
                                'ubest_num': str,
                                'mbest_num': str,
                                Optional('attach'): str,
                                Optional('best_route'): {
                                    Any(): {
                                        Optional('nexthop'): {
                                            Any(): {
                                                Optional('protocol'): {
                                                    Any(): {
                                                        Optional('route_table'): str,
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
                                Optional('routes'): {
                                    Optional('nexthop'): {
                                        Any(): {
                                            Optional('protocol'): {
                                                Any(): {
                                                    Optional('route_table'): str,
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
    }


class ShowRoutingVrfAll(ShowRoutingVrfAllSchema):

    """Parser for show routing ip vrf all
                show routing ip vrf <vrf>"""
    cli_command = ['show routing {ip} vrf all', 'show routing vrf all',
                   'show routing {ip} vrf {vrf}', 'show routing vrf {vrf}']
    exclude = ['uptime']

    def cli(self, ip='', vrf='', output=None):
        if ip and vrf:
            cmd = self.cli_command[2].format(ip=ip, vrf=vrf)
        elif ip :
            cmd = self.cli_command[0].format(ip=ip)
        elif vrf:
            cmd = self.cli_command[3].format(vrf=vrf)
        else:
            cmd = self.cli_command[1]
        # excute command to get output

        if output is None:
            out = self.device.execute(cmd)
        else:
            out = output

        # Init dict
        result_dict = {}
        address_family = None
        is_ipv6 = False

        if ip and (':' in ip or ip == 'ipv6'):
            is_ipv6 = True

        for line in out.splitlines():
            line = line.strip()

            # IP Route Table for VRF "default"
            # IPv6 Routing Table for VRF "default"
            # IPv6 Routing Table for VRF "otv-vrf139"
            p1 = re.compile(r'^(IP|IPv6) +(Route|Routing) +Table +for +VRF +"(?P<vrf>\S+)"$')
            m = p1.match(line)
            if m:
                vrf = str(m.groupdict()['vrf'])
                if vrf == 'default' and not is_ipv6:
                    address_family = 'ipv4 unicast'
                elif vrf != 'default' and not is_ipv6:
                    address_family = 'vpnv4 unicast'
                elif vrf == 'default' and is_ipv6:
                    address_family = 'ipv6 unicast'
                elif vrf != 'default' and is_ipv6:
                    address_family = 'vpnv6 unicast'
                continue

            # 10.144.0.1/32, ubest/mbest: 1/0 time, attached
            # 10.220.9.0/24, ubest/mbest: 1/0 time
            p2 = re.compile(r'(?P<ip_mask>[\w\:\.\/]+), +ubest/mbest: +'
                            r'(?P<ubest>\d+)/(?P<mbest>\d+)( +time)?'
                            r'(, +(?P<attach>\w+))?$')
            m = p2.match(line)
            if m:
                # Init af dict
                af_dict = result_dict.setdefault('vrf', {}).setdefault(vrf, {}).\
                                      setdefault('address_family', {}).\
                                      setdefault(address_family, {})

                # Init ip dict
                ip_mask = m.groupdict()['ip_mask']
                ip_dict = af_dict.setdefault('ip', {}).setdefault(ip_mask, {})

                ip_dict['ubest_num'] = m.groupdict()['ubest']
                ip_dict['mbest_num'] = m.groupdict()['mbest']
                if m.groupdict()['attach']:
                    ip_dict['attach'] = m.groupdict()['attach']
                continue

            # *via 2001:db8:8b05::1002%default, Eth1/1, [200/4444], 15:57:39, bgp-333, internal, tag 333
            # *via 10.36.3.3%default, [33/0], 5w0d, bgp-100, internal, tag 100 (mpls-vpn)
            # *via 2001:db8::5054:ff:fed5:63f9, Eth1/1, [0/0], 00:15:46, direct,
            # *via 2001:db8:2:2::2, Eth1/1, [0/0], 00:15:46, direct, , tag 222
            # *via 10.55.130.2%default, [200/0], 3d07h, bgp-1, internal, tag 1 (evpn), segid: 50009 tunnelid: 0x64008202 encap: VXLAN
            # via 10.13.110.1, Eth1/2.110, [110/41], 5d03h, ospf-1, intra
            # via 10.4.1.1, [200/0], 5d03h, bgp-65000, internal, tag 65000 (hidden)
            # *via 10.13.90.1, Eth1/2.90, [90/3072], 1w5d, eigrp-test, internal
            p3 = re.compile(r'^(?P<cast>.*)via +(?P<nexthop>[\w\.\:\s]+)'
                            r'(%(?P<table>[\w\:]+))?, *'
                            r'((?P<int>[a-zA-Z0-9\./_]+),)? *'
                            r'\[(?P<preference>\d+)/(?P<metric>\d+)\], *'
                            r'(?P<up_time>[\w\:\.]+), *'
                            r'(?P<protocol>\w+)(\-(?P<process>\w+))?,? *'
                            r'(?P<attribute>\w+)?,? *'
                            r'(tag *(?P<tag>\w+))?,? *(?P<vpn>[a-zA-Z\(\)\-]+)?'
                            r',?( +segid: +(?P<segid>\d+))?,?( +tunnelid: +'
                            r'(?P<tunnelid>[0-9x]+))?,?( +encap: +'
                            r'(?P<encap>[a-zA-Z0-9]+))?$')
            m = p3.match(line)
            if m:
                cast = m.groupdict()['cast']
                if cast:
                    cast = {'1': 'unicast',
                            '2': 'multicast'}['{}'.format(cast.count('*'))]
                    # Init 'best_route' dict
                    hop_dict = ip_dict.setdefault('best_route', {}).setdefault(cast, {}).\
                                        setdefault('nexthop', {})
                else:
                    hop_dict = ip_dict.setdefault('routes', {}).setdefault('nexthop', {})

                nexthop = m.groupdict()['nexthop']
                protocol = m.groupdict()['protocol']

                prot_dict = hop_dict.setdefault(nexthop, {}).setdefault('protocol', {}).\
                                        setdefault(protocol, {})

                table = m.groupdict()['table']
                if table:
                    prot_dict['route_table'] = table

                intf = m.groupdict()['int']
                if intf:
                    prot_dict['interface'] = Common.convert_intf_name(intf)

                preference = m.groupdict()['preference']
                if preference:
                    prot_dict['preference'] = preference

                metric = m.groupdict()['metric']
                if metric:
                    prot_dict['metric'] = metric

                up_time = m.groupdict()['up_time']
                if up_time:
                    prot_dict['uptime'] = up_time

                process = m.groupdict()['process']
                if process:
                    prot_dict['protocol_id'] = process

                attribute = m.groupdict()['attribute']
                if attribute:
                    prot_dict['attribute'] = attribute

                tag = m.groupdict()['tag']
                if tag:
                    prot_dict['tag'] = tag.strip()

                segid = m.groupdict()['segid']
                if segid:
                    prot_dict['segid'] = int(segid)

                tunnelid = m.groupdict()['tunnelid']
                if tunnelid:
                    prot_dict['tunnelid'] = tunnelid

                encap = m.groupdict()['encap']
                if encap:
                    prot_dict['encap'] = encap.lower()

                vpn = m.groupdict()['vpn']
                if vpn and 'mpls-vpn' in vpn:
                    prot_dict['mpls_vpn'] = True
                elif vpn and 'mpls' in vpn:
                    prot_dict['mpls'] = True
                elif vpn and 'evpn' in vpn:
                    prot_dict['evpn'] = True

                # Set extra values for BGP Ops
                if attribute == 'external' and protocol == 'bgp':
                    af_dict['bgp_distance_extern_as'] = int(preference)
                elif attribute == 'internal' and protocol == 'bgp':
                    af_dict['bgp_distance_internal_as'] = int(preference)
                elif attribute == 'discard' and protocol == 'bgp':
                    af_dict['bgp_distance_local'] = int(preference)
                continue

        return result_dict


class ShowRoutingIpv6VrfAll(ShowRoutingVrfAll):
    """Parser for show routing ipv6 vrf all,
            show routing ipv6 vrf <vrf>"""

    exclude = [
        'uptime']

    def cli(self, vrf='', output=None):
        return super().cli(ip='ipv6', vrf=vrf, output=output)


# =================================
# Parser for 'show ip route summary'
# Parser for 'show ip route summary vrf {vrf}'
# =================================

class ShowIpRouteSummarySchema(MetaParser):
    """Schema for
        * show ip route summary
        * show ip route summary vrf {vrf} """

    schema = {
        'vrf': {
            Any(): {
                'backup_paths': {
                    Optional(Any()): int,
                },
                'best_paths': {
                    Optional(Any()): int,
                },
                Optional('num_routes_per_mask'): {
                    Optional(Any()): int,
                },
                'total_paths': int,
                'total_routes': int,
              },
         },
}


class ShowIpRouteSummary(ShowIpRouteSummarySchema):
    """Parser for
        * show ip route summary
        * show ip route summary vrf {vrf}"""

    cli_command = ['show ip route summary vrf {vrf}',
                   'show ip route summary']

    def cli(self, vrf='', output=None):

        if output is None:
            if vrf:
                cmd = self.cli_command[0].format(vrf=vrf)
            else:
                cmd = self.cli_command[1]
            out = self.device.execute(cmd)
        else:
            out = output

        vrf = None
        parse_best_path = False
        parse_num_routes = False

        # Init dict
        routeSummary_dict = {}
        sub_dict = {}

        # IP Route Table for VRF "xxx"
        # IP Route Table for VRF "evpn-t-0003"
        p1 = re.compile(r'^(IP|IPv6) +(Route|Routing) +Table +for +VRF +\"(?P<vrf>\S+)\"$')

        # Total number of routes: 308
        p2 = re.compile(r'^Total +number +of +(?P<route_path>\w+): +(?P<route_path_val>\d+)$')

        # Best paths per protocol:      Backup paths per protocol:
        p3 = re.compile(r'^Best +paths +per +protocol.*$')

        # am             : 214          ospf-1000      : 10
        # local          : 14
        # am             : 1            None
        p4 = re.compile(r'^(?P<best>[\w-]+) +: +(?P<best_val>\d+)'
                        r'( +(None|((?P<backup>\S+) +: +(?P<backup_val>\d+))))?$')

        #   /8 : 1       /24: 4       /32: 12
        p5 = re.compile(r'(?P<route_mask>/\d+) *: +(?P<route_mask_len>\d+)')

        for line in out.splitlines():
            line = line.strip()

            # IP Route Table for VRF "default"
            # IP Route Table for VRF "evpn-t-0003"
            m = p1.match(line)
            if m:
                parse_num_routes = False
                parse_best_path = False
                vrf = m.groupdict()['vrf']
                continue

            # Total number of routes: 17
            # Total number of paths:  20
            m = p2.match(line)
            if m:
                group = m.groupdict()
                sub_dict = routeSummary_dict.setdefault('vrf', {}).setdefault(vrf, {})
                sub_dict.update({'total_'+group['route_path']: int(group['route_path_val'])})

                continue

            if parse_num_routes:
                # /0 : 1       /8 : 1       /24: 1       /32: 8
                for m1 in p5.finditer(line):
                    if m1:
                        sub_dict['num_routes_per_mask'][m1.group('route_mask')] = int(m1.group('route_mask_len'))

            # Number of routes per mask-length:
            if line.find('Number of routes per mask-length') >= 0:
                parse_best_path = False
                parse_num_routes = True
                sub_dict['num_routes_per_mask'] = {}

            if parse_best_path:
                # am             : 3            None
                # local          : 1
                #  am             : 4            ospf-1         : 1
                m = p4.match(line)
                if m:
                    group = m.groupdict()
                    sub_dict['best_paths'][group['best']] = int(group['best_val'])

                    if group['backup'] and group['backup_val']:
                        sub_dict['backup_paths'][group['backup']] = int(group['backup_val'])

            # Best paths per protocol:      Backup paths per protocol:
            m = p3.match(line)
            if m:
                parse_best_path = True
                if 'best_paths' not in sub_dict:
                    sub_dict['best_paths'] = {}
                    sub_dict['backup_paths'] = {}
                continue

        return routeSummary_dict

# ====================================================
# Schema for:
#   show ip route
#   show ip route vrf {vrf}
#   show ip route vrf all
#   show ip route interface {interface}
#   show ip route interface {interface} vrf {vrf}
# ====================================================
class ShowIpRouteSchema(MetaParser):
    """Schema for:
       show ip route
       show ip route vrf {vrf}
       show ip route vrf all
       show ip route interface {interface}
       show ip route interface {interface} vrf {vrf}
    """

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
                                Optional('process_id'): str,
                                Optional('route_preference'): int,
                                Optional('metric'): int,
                                Optional('tag'): int,
                                Optional('hidden'): bool,
                                Optional('source_protocol'): str,
                                Optional('source_protocol_status'): str,
                                Optional('attached'): bool,
                                Optional('active'): bool,
                                Optional('direct'): bool,
                                Optional('pervasive'): bool,
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
                                            Optional('source_protocol'): str,
                                            Optional('source_protocol_status'): str,
                                            Optional('next_hop'): str,
                                            Optional('next_hop_vrf'): str,
                                            Optional('next_hop_af'): str,
                                            Optional('best_ucast_nexthop'): bool,
                                            Optional('best_mcast_nexthop'): bool,
                                            Optional('outgoing_interface'): str,
                                            Optional('updated'): str,
                                            Optional('route_preference'): int,
                                            Optional('metric'): int,
                                            Optional('mpls'): bool,
                                            Optional('mpls_vpn'): bool,
                                            Optional('stale'): bool,
                                            Optional('evpn'): bool,
                                            Optional('segid'): int,
                                            Optional('asymmetric'): bool,
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
    }


# ====================================================
# Parser for:
# show ip route {route} {protocol} interface {interface} vrf {vrf}
# show ip route {route} {protocol} interface {interface}
# show ip route {route} {protocol} vrf {vrf}
# show ip route {protocol} interface {interface} vrf {vrf}
# show ip route {route} interface {interface} vrf {vrf}
# show ip route {route} {protocol}
# show ip route {protocol} interface {interface}
# show ip route {protocol} vrf {vrf}
# show ip route {route} interface {interface}
# show ip route {route} vrf {vrf}
# show ip route interface {interface} vrf {vrf}
# show ip route {protocol}
# show ip route {route}
# show ip route interface {interface}
# show ip route vrf {vrf}
# show ip route vrf all
# show ip route
# ====================================================
class ShowIpRoute(ShowIpRouteSchema):
    """Parser for :
        'show ip route {route} {protocol} interface {interface} vrf {vrf}',
        'show ip route {route} {protocol} interface {interface}',
        'show ip route {route} {protocol} vrf {vrf}',
        'show ip route {protocol} interface {interface} vrf {vrf}',
        'show ip route {route} interface {interface} vrf {vrf}',
        'show ip route {route} {protocol}',
        'show ip route {protocol} interface {interface}',
        'show ip route {protocol} vrf {vrf}',
        'show ip route {route} interface {interface}',
        'show ip route {route} vrf {vrf}',
        'show ip route interface {interface} vrf {vrf}',
        'show ip route {protocol}',
        'show ip route {route}',
        'show ip route interface {interface}',
        'show ip route vrf {vrf}',
        'show ip route vrf all',
        'show ip route'
    """

    cli_command = [ 'show ip route {route} {protocol} interface {interface} vrf {vrf}',
                    'show ip route {route} {protocol} interface {interface}',
                    'show ip route {route} {protocol} vrf {vrf}',
                    'show ip route {protocol} interface {interface} vrf {vrf}',
                    'show ip route {route} interface {interface} vrf {vrf}',
                    'show ip route {route} {protocol}',
                    'show ip route {protocol} interface {interface}',
                    'show ip route {protocol} vrf {vrf}',
                    'show ip route {route} interface {interface}',
                    'show ip route {route} vrf {vrf}',
                    'show ip route interface {interface} vrf {vrf}',
                    'show ip route {protocol}',
                    'show ip route {route}',
                    'show ip route interface {interface}',
                    'show ip route vrf {vrf}',
                    'show ip route vrf all',
                    'show ip route']
    exclude = [
        'updated']

    def sort_next_hop_list(self, obj: dict):
        for key, value in obj.items():
            if isinstance(value, dict):
                if key == 'next_hop_list':
                    # sort based on next_hop then source_protocol
                    sort_list = sorted(list(value.values()), \
                            key=lambda k: (k['next_hop'], k['source_protocol']), reverse=False)
                    sorted_next_hop_list = {}
                    for index, item in enumerate(sort_list):
                        item['index'] = index+1
                        sorted_next_hop_list[index+1] = item
                    obj[key] = sorted_next_hop_list
                else:
                    self.sort_next_hop_list(value)

    def cli(self, route=None, protocol=None, vrf=None, interface=None, output=None, cmd=None):

        # execute command to get output
        if output is None:
            if protocol and route and interface and vrf:
                cmd = self.cli_command[0].format(
                        protocol=protocol,
                        route=route,
                        interface=interface,
                        vrf=vrf,
                        )
            elif protocol and route and interface:
                cmd = self.cli_command[1].format(
                        protocol=protocol,
                        route=route,
                        interface=interface,
                        )
            elif protocol and route and vrf:
                cmd = self.cli_command[2].format(
                        protocol=protocol,
                        route=route,
                        vrf=vrf,
                        )
            elif protocol and interface and vrf:
                cmd = self.cli_command[3].format(
                        protocol=protocol,
                        vrf=vrf,
                        interface=interface,
                        )
            elif route and interface and vrf:
                cmd = self.cli_command[4].format(
                        vrf=vrf,
                        route=route,
                        interface=interface,
                        )
            elif protocol and route:
                cmd = self.cli_command[5].format(
                        protocol=protocol,
                        route=route,
                        )
            elif protocol and interface:
                cmd = self.cli_command[6].format(
                        protocol=protocol,
                        interface=interface,
                        )
            elif protocol and vrf:
                cmd = self.cli_command[7].format(
                        protocol=protocol,
                        vrf=vrf,
                        )
            elif route and interface:
                cmd = self.cli_command[8].format(
                        route=route,
                        interface=interface,
                        )
            elif route and vrf:
                cmd = self.cli_command[9].format(
                        route=route,
                        vrf=vrf,
                        )
            elif interface and vrf:
                cmd = self.cli_command[10].format(
                        interface=interface,
                        vrf=vrf,
                        )
            elif protocol:
                cmd = self.cli_command[11].format(
                        protocol=protocol,
                        )
            elif route:
                cmd = self.cli_command[12].format(
                        route=route,
                        )
            elif interface:
                cmd = self.cli_command[13].format(
                        interface=interface,
                        )
            elif vrf:
                cmd = self.cli_command[14].format(
                        vrf=vrf,
                        )
            else:
                cmd = self.cli_command[15]

            out = self.device.execute(cmd)
        else:
            out = output

        if not cmd:
            cmd = 'ipv4'
        af = 'ipv6' if 'v6' in cmd else 'ipv4'
        result_dict = {}

        # IP Route Table for VRF "default"
        # IP Route Table for Context "default"
        # IPv6 Routing Table for VRF "default"
        # IP Route Table for VRF "default"
        p1 = re.compile(r'^\s*(?P<af>IPv6|IP) +Rout(?:e|ing) +Table +for (VRF|Context) +\"(?P<vrf>\S+)\"$')

        # 10.4.1.1/32, ubest/mbest: 2/0
        # 10.36.3.3/32, ubest/mbest: 2/0, attached
        # 10.121.0.0/24, ubest/mbest: 1/0 time, attached
        # 10.94.77.1/32, ubest/mbest: 1/0 time
        # 0.0.0.0/0, 1 ucast next-hops, 0 mcast next-hops
        # 0.1.3.255/32, 1 ucast next-hops, 0 mcast next-hops, attached
        # 2001:db8:5f1:1::1/128, ubest/mbest: 1/0, attached
        # 192.168.1.1/32, ubest/mbest: 1/0, pending ufdm
        # 192.168.1.0/24, ubest/mbest: 1/0, attached, direct, pervasive
        # 192.168.1.1/32, ubest/mbest: 1/0, attached, pervasive

        p2 = re.compile(r'^(?P<route>[\w\/\.\:]+), +(ubest/mbest: +'
                        r'(?P<ubest_mbest>[\d\/]+)( +time)?)?((?P<ubest>\d+) '
                        r'+ucast +next-hops, +(?P<mbest>\d+) +mcast +next-hops)?'
                        r'(, +(?P<attached>[\w]+))?( +(?P<attached2>[\w]+))?'
                        r'(\,)?( +(?P<direct>direct))?(\,)?( +(?P<pervasive>pervasive))?$')

        # *via 10.2.3.2, Eth1/4, [1/0], 01:01:30, static
        # *via 10.1.3.1, Eth1/2, [110/41], 01:01:18, ospf-1, intra
        # *via 10.229.11.11, [200/0], 01:01:12, bgp-100, internal, tag 100
        # *via 2001:db8:5f1:1::1, Eth1/27, [0/0], 05:56:03, local
        # *via ::ffff:10.229.11.11%default:IPv4, [200/0], 01:01:43, bgp-100, internal,
        # *via 10.1.3.1, Eth1/2, [110/41], 01:01:18, ospf-1, intra, tag 100,
        # via 10.4.1.1, [200/0], 1w4d, bgp-65000, internal, tag 65000 (hidden)
        # via 10.23.120.2, Eth1/1.120, [120/2], 1w4d, rip-1, rip
        # **via 10.36.3.3%default, [33/0], 5w0d, bgp-100, internal, tag 100 (mpls-vpn)
        # *via vrf default, Null0, [20/0], 18:11:28, bgp-333, external, tag 333
        # *via 10.55.130.3%default, [33/0], 3d10h, bgp-1, internal, tag 1 (evpn), segid: 50051 tunnelid: 0x64008203 encap: VXLAN
        # *via 2001:db8:626b:2101::3/128, [200/7], 01:51:32, bgp-10001, internal, tag 20001
        # *via 100.100.100.1%default, [200/0], 01:25:26, bgp-1000, internal, tag 3000, segid: 601011 (Asymmetric) tunnelid: 0x64646401 encap: VXLAN
        p3 = re.compile(r'^\s*(?P<star>[*]+)?via +(?P<next_hop>[\s\w\:\.\/\%\!\#\$\*\+\-\;\=\@\^\_\{\}]+),'
                        r'( +(?P<interface>[\w\/\.]+))?,? +\[(?P<route_preference>[\d\/]+)\],'
                        r' +(?P<date>[0-9][\w\:]+)?,?( +(?P<source_protocol>[\w\-]+))?,?'
                        r'( +(?P<source_protocol_status>[\w-]+))?,?( +tag +(?P<tag>[\d]+))?,?'
                        r'( +\((?P<hidden>hidden)\))?'
                        r'\s*(?P<vpn>[a-zA-Z\(\)\-]+)?,?( +segid: +(?P<segid>\d+))?,?'
                        r'( +\((?P<asymmetric>Asymmetric)\))?'
                        r'( +tunnelid: +(?P<tunnelid>[0-9x]+))?,?( +encap: +(?P<encap>[a-zA-Z0-9]+))?$')

        #    tag 100
        p4 = re.compile(r'^tag +(?P<tag>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            # IP Route Table for VRF "default"
            # IP Route Table for Context "default"
            # IPv6 Routing Table for VRF "default"
            m = p1.match(line)
            if m:
                if 'vrf' not in result_dict:
                    vrfs_dict = result_dict.setdefault('vrf', {})

                group = m.groupdict()
                vrf = group['vrf']
                af = 'ipv6' if 'v6' in group['af'] else 'ipv4'

                routes_dict = vrfs_dict.setdefault(vrf, {}).setdefault('address_family', {}). \
                                        setdefault(af, {}).setdefault('routes', {})
                continue

            # 10.4.1.1/32, ubest/mbest: 2/0
            # 10.36.3.3/32, ubest/mbest: 2/0, attached
            # 10.121.0.0/24, ubest/mbest: 1/0 time, attached
            # 10.94.77.1/32, ubest/mbest: 1/0 time
            # 0.0.0.0/0, 1 ucast next-hops, 0 mcast next-hops
            # 0.1.3.255/32, 1 ucast next-hops, 0 mcast next-hops, attached
            # 2001:db8:5f1:1::1/128, ubest/mbest: 1/0, attached
            # 192.168.1.1/32, ubest/mbest: 1/0, pending ufdm
            # 192.168.1.0/24, ubest/mbest: 1/0, attached, direct, pervasive
            # 192.168.1.1/32, ubest/mbest: 1/0, attached, pervasive
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                route = groups['route']
                active = True
                direct = False
                pervasive = False

                index = 1

                if groups['ubest_mbest']:
                    ubest_mbest = groups['ubest_mbest']

                    if '/' in ubest_mbest:
                        ubest_mbest = ubest_mbest.split('/')
                        ubest = ubest_mbest[0]
                        mbest = ubest_mbest[1]
                elif groups['ubest'] and groups['mbest']:
                    ubest = groups['ubest']
                    mbest = groups['mbest']

                if groups['attached']:
                    attached = True if 'attached' in groups['attached'] else False

                if groups['direct']:
                    direct = True if 'direct' in groups['direct'] else False

                if groups['pervasive']:
                    pervasive = True if 'pervasive' in groups['pervasive'] else False

                # if vrf:
                if 'vrf' not in result_dict:
                    routes_dict = result_dict.setdefault('vrf', {}).setdefault('default', {}). \
                        setdefault('address_family', {}).setdefault(af, {}). \
                        setdefault('routes', {})
                route_dict = routes_dict.setdefault(route, {})
                route_dict.update({'route': route})
                route_dict.update({'active': active})

                if ubest:
                    route_dict.update({'ubest': int(ubest)})

                if mbest:
                    route_dict.update({'mbest': int(mbest)})

                if groups['attached']:
                    route_dict.update({'attached': attached})

                if direct:
                    route_dict.update({'direct': direct})

                if pervasive:
                    route_dict.update({'pervasive': pervasive})

                continue

            # *via 10.2.3.2, Eth1/4, [1/0], 01:01:30, static
            # *via 10.1.3.1, Eth1/2, [110/41], 01:01:18, ospf-1, intra
            # *via 10.229.11.11, [200/0], 01:01:12, bgp-100, internal, tag 100
            # *via 2001:db8:5f1:1::1, Eth1/27, [0/0], 05:56:03, local
            # *via ::ffff:10.229.11.11%default:IPv4, [200/0], 01:01:43, bgp-100, internal,
            # *via 10.1.3.1, Eth1/2, [110/41], 01:01:18, ospf-1, intra, tag 100,
            # via 10.4.1.1, [200/0], 1w4d, bgp-65000, internal, tag 65000 (hidden)
            # via 10.23.120.2, Eth1/1.120, [120/2], 1w4d, rip-1, rip
            # **via 10.36.3.3%default, [33/0], 5w0d, bgp-100, internal, tag 100 (mpls-vpn)
            # *via 10.55.130.3%default, [33/0], 3d10h, bgp-1, internal, tag 1 (evpn), segid: 50051 tunnelid: 0x64008203 encap: VXLAN
            # *via 100.100.100.1%default, [200/0], 01:25:26, bgp-1000, internal, tag 3000, segid: 601011 (Asymmetric) tunnelid: 0x64646401 encap: VXLAN
            m = p3.match(line)
            if m:
                groups = m.groupdict()

                tag = process_id = source_protocol_status = interface = next_hop_vrf = next_hop_af = ""
                star = m.groupdict()['star']
                cast = None

                star_rp, non_star_rp, star_metrics, non_star_metrics = None, None, None, None
                if groups['route_preference']:
                    rp_val = groups['route_preference'].split('/')
                    rp = int(rp_val[0])
                    metrics = int(rp_val[1])
                    if star:
                        if len(star) == 1:
                            cast = 'best_ucast_nexthop'
                        if len(star) == 2:
                            cast = 'best_mcast_nexthop'
                        star_rp = rp
                        star_metrics = metrics
                    else:
                        non_star_rp = rp
                        non_star_metrics = metrics

                if groups['next_hop']:
                    next_hop = groups['next_hop']
                    if '%' in next_hop:
                        next_hop_vrf = next_hop.split('%')[1]
                        next_hop = next_hop.split('%')[0]
                        if ':' in next_hop_vrf:
                            next_hop_af = next_hop_vrf.split(':')[1].lower()
                            next_hop_vrf = next_hop_vrf.split(':')[0]

                if groups['interface']:
                    interface = Common.convert_intf_name(groups['interface'])

                if groups['date']:
                    updated = groups['date']

                if groups['source_protocol_status']:
                    source_protocol_status = groups['source_protocol_status']

                if groups['source_protocol']:
                    if '-' in groups['source_protocol']:
                        source_protocol = groups['source_protocol'].split('-')[0]
                        process_id = groups['source_protocol'].split('-')[1]
                    else:
                        source_protocol = groups['source_protocol']

                if groups['tag']:
                    tag = groups['tag']

                hidden = True if groups.get('hidden') else False

                if hidden:
                    route_dict.update({'hidden': hidden})

                if star_metrics is not None:
                    route_dict.update({'metric': star_metrics})

                if star_rp is not None:
                    route_dict.update({'route_preference': int(star_rp)})

                if process_id:
                    route_dict.update({'process_id': process_id})

                if tag:
                    route_dict.update({'tag': int(tag)})

                next_hop_dict = route_dict.setdefault('next_hop', {})

                if not next_hop:
                    interface_dict = next_hop_dict.setdefault('outgoing_interface', {}).setdefault(interface, {})

                    if interface:
                        interface_dict.update({'outgoing_interface': interface})

                    if updated:
                        interface_dict.update({'updated': updated})

                else:
                    index_dict = next_hop_dict.setdefault('next_hop_list', {}).setdefault(index, {})
                    index_dict.update({'index': index})
                    index_dict.update({'next_hop': next_hop})
                    if source_protocol:
                        route_dict.update({'source_protocol': source_protocol})
                        index_dict.update({'source_protocol': source_protocol})

                    if source_protocol_status:
                        route_dict.update({'source_protocol_status': source_protocol_status})
                        index_dict.update({'source_protocol_status': source_protocol_status})

                    if cast:
                        index_dict.update({cast: True})

                    if updated:
                        index_dict.update({'updated': updated})

                    if interface:
                        index_dict.update({'outgoing_interface': interface})

                    if next_hop_vrf:
                        index_dict.update({'next_hop_vrf': next_hop_vrf})

                    if next_hop_af:
                        index_dict.update({'next_hop_af': next_hop_af})

                    if star_metrics is not None:
                        index_dict['metric'] = star_metrics

                    if non_star_metrics is not None:
                        index_dict['metric'] = non_star_metrics

                    if star_rp is not None:
                        index_dict['route_preference'] = star_rp

                    if non_star_rp is not None:
                        index_dict['route_preference'] = non_star_rp

                    segid = groups['segid']
                    if segid:
                        index_dict['segid'] = int(segid)

                    asymmetric = True if groups.get('asymmetric') else False

                    if asymmetric:
                        index_dict['asymmetric'] = asymmetric

                    tunnelid = groups['tunnelid']
                    if tunnelid:
                        index_dict['tunnelid'] = tunnelid

                    encap = groups['encap']
                    if encap:
                        index_dict['encap'] = encap.lower()

                    vpn = groups['vpn']
                    if vpn and 'mpls-vpn' in vpn:
                        index_dict['mpls_vpn'] = True
                    elif vpn and 'mpls' in vpn:
                        index_dict['mpls'] = True
                    elif vpn and 'evpn' in vpn:
                        index_dict['evpn'] = True
                    elif vpn and 'stale' in vpn:
                        index_dict['stale'] = True

                index += 1
                continue

            #    tag 100
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                if groups['tag']:
                    route_dict.update({'tag': int(groups['tag'])})

        self.sort_next_hop_list(result_dict)
        return result_dict


# ====================================================
#  parser for:
# show ipv6 route {route} {protocol} interface {interface} vrf {vrf}
# show ipv6 route {route} {protocol} interface {interface}
# show ipv6 route {route} {protocol} vrf {vrf}
# show ipv6 route {protocol} interface {interface} vrf {vrf}
# show ipv6 route {route} interface {interface} vrf {vrf}
# show ipv6 route {route} {protocol}
# show ipv6 route {protocol} interface {interface}
# show ipv6 route {protocol} vrf {vrf}
# show ipv6 route {route} interface {interface}
# show ipv6 route {route} vrf {vrf}
# show ipv6 route interface {interface} vrf {vrf}
# show ipv6 route {protocol}
# show ipv6 route {route}
# show ipv6 route interface {interface}
# show ipv6 route vrf {vrf}
# show ipv6 route vrf all
# show ipv6 route
# ====================================================
class ShowIpv6Route(ShowIpRoute):
    """Parser for :
        'show ipv6 route {route} {protocol} interface {interface} vrf {vrf}',
        'show ipv6 route {route} {protocol} interface {interface}',
        'show ipv6 route {route} {protocol} vrf {vrf}',
        'show ipv6 route {protocol} interface {interface} vrf {vrf}',
        'show ipv6 route {route} interface {interface} vrf {vrf}',
        'show ipv6 route {route} {protocol}',
        'show ipv6 route {protocol} interface {interface}',
        'show ipv6 route {protocol} vrf {vrf}',
        'show ipv6 route {route} interface {interface}',
        'show ipv6 route {route} vrf {vrf}',
        'show ipv6 route interface {interface} vrf {vrf}',
        'show ipv6 route {protocol}',
        'show ipv6 route {route}',
        'show ipv6 route interface {interface}',
        'show ipv6 route vrf {vrf}',
        'show ipv6 route vrf all',
        'show ipv6 route'
       """

    cli_command = [ 'show ipv6 route {route} {protocol} interface {interface} vrf {vrf}',
                    'show ipv6 route {route} {protocol} interface {interface}',
                    'show ipv6 route {route} {protocol} vrf {vrf}',
                    'show ipv6 route {protocol} interface {interface} vrf {vrf}',
                    'show ipv6 route {route} interface {interface} vrf {vrf}',
                    'show ipv6 route {route} {protocol}',
                    'show ipv6 route {protocol} interface {interface}',
                    'show ipv6 route {protocol} vrf {vrf}',
                    'show ipv6 route {route} interface {interface}',
                    'show ipv6 route {route} vrf {vrf}',
                    'show ipv6 route interface {interface} vrf {vrf}',
                    'show ipv6 route {protocol}',
                    'show ipv6 route {route}',
                    'show ipv6 route interface {interface}',
                    'show ipv6 route vrf {vrf}',
                    'show ipv6 route vrf all',
                    'show ipv6 route']

    exclude = [
        'updated',
        'metric',
        'next_hop',
        'outgoing_interface',
        'incoming_interface']

    def cli(self, protocol=None, route=None, vrf=None, interface=None, output=None, cmd=None):

        if output is None:
            if protocol and route and interface and vrf:
                cmd = self.cli_command[0].format(
                    protocol=protocol,
                    route=route,
                    interface=interface,
                    vrf=vrf,
                )
            elif protocol and route and interface:
                cmd = self.cli_command[1].format(
                    protocol=protocol,
                    route=route,
                    interface=interface,
                )
            elif protocol and route and vrf:
                cmd = self.cli_command[2].format(
                    protocol=protocol,
                    route=route,
                    vrf=vrf,
                )
            elif protocol and interface and vrf:
                cmd = self.cli_command[3].format(
                    protocol=protocol,
                    vrf=vrf,
                    interface=interface,
                )
            elif route and interface and vrf:
                cmd = self.cli_command[4].format(
                    vrf=vrf,
                    route=route,
                    interface=interface,
                )
            elif protocol and route:
                cmd = self.cli_command[5].format(
                    protocol=protocol,
                    route=route,
                )
            elif protocol and interface:
                cmd = self.cli_command[6].format(
                    protocol=protocol,
                    interface=interface,
                )
            elif protocol and vrf:
                cmd = self.cli_command[7].format(
                    protocol=protocol,
                    vrf=vrf,
                )
            elif route and interface:
                cmd = self.cli_command[8].format(
                    route=route,
                    interface=interface,
                )
            elif route and vrf:
                cmd = self.cli_command[9].format(
                    route=route,
                    vrf=vrf,
                )
            elif interface and vrf:
                cmd = self.cli_command[10].format(
                    interface=interface,
                    vrf=vrf,
                )
            elif protocol:
                cmd = self.cli_command[11].format(
                    protocol=protocol,
                )
            elif route:
                cmd = self.cli_command[12].format(
                    route=route,
                )
            elif interface:
                cmd = self.cli_command[13].format(
                    interface=interface,
                )
            elif vrf:
                cmd = self.cli_command[14].format(
                    vrf=vrf,
                )
            else:
                cmd = self.cli_command[15]
            out = self.device.execute(cmd)
        else:
            out = output

        return super().cli(vrf=vrf, output=out, cmd=cmd)


class ShowRouting(ShowIpRoute):
    """
        Parser for show routing
        show routing <ip>"""
    cli_command = ['show routing', 'show routing {protocol}']

    def cli(self, protocol=None, route=None, vrf=None, interface=None, output=None, cmd=None):

        if output is None:
            if protocol:
                cmd = self.cli_command[1].format(
                    protocol=protocol,
                )
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        return super().cli(protocol=protocol, route=route, vrf=vrf, interface=interface, output=out, cmd=cmd)



