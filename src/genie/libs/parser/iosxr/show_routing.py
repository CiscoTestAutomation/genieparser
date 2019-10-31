'''
show_route.py

'''
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
    Any, \
    Optional

# ====================================================
#  distributor class for show ip route
# ====================================================
class ShowRouteIpDistributor(MetaParser):
    """distributor class for show ip route"""
    cli_command = ['show route vrf {vrf} ipv4', 
                   'show route ipv4',
                   'show route ipv4 {route}',
                   'show route ipv4 {protocol}',
                   'show route vrf {vrf} ipv4 {protocol}',
                   'show route vrf {vrf} ipv4 {route}']

    protocol_set = {'ospf', 'odr', 'isis', 'eigrp', 'static', 'mobile',
                    'rip', 'lisp', 'nhrp', 'local', 'connected', 'bgp'}

    def cli(self, vrf=None, route=None, protocol=None, output=None):

        if output is None:
            if vrf and protocol:
                cmd = self.cli_command[4].format(vrf=vrf,
                        protocol=protocol)
            elif vrf and route:
                cmd = self.cli_command[5].format(vrf=vrf,
                        route=route)
            elif protocol:
                cmd = self.cli_command[3].format(protocol=protocol)
            elif route:
                cmd = self.cli_command[2].format(route=route)
            elif vrf:
                cmd = self.cli_command[0].format(vrf=vrf)
            else:
                cmd = self.cli_command[1]
            out = self.device.execute(cmd)
        else:
            out = output

        if (route or protocol) in self.protocol_set or (not route and not protocol):
            parser = ShowRouteIpv4(self.device)
            self.schema = parser.schema
            return parser.parse(vrf=vrf, output=out)

        else:
            parser = ShowRouteIpWord(self.device)
            self.schema=parser.schema
            return parser.parse(vrf=vrf, route=route, output=out)

# ====================================================
#  distributor class for show ipv6 route
# ====================================================
class ShowRouteIpv6Distributor(MetaParser):
    """distributor class for show ipv6 route"""
    cli_command = ['show route vrf {vrf} ipv6', 
                   'show route ipv6',
                   'show route ipv6 {route}',
                   'show route ipv6 {protocol}',
                   'show route vrf {vrf} ipv6 {protocol}',
                   'show route vrf {vrf} ipv6 {route}']

    protocol_set = {'ospf', 'odr', 'isis', 'eigrp', 'static', 'mobile',
                    'rip', 'lisp', 'nhrp', 'local', 'connected', 'bgp'}

    def cli(self, vrf=None, route=None, protocol=None, interface=None, output=None):
        
        if output is None:
            if vrf and protocol:
                cmd = self.cli_command[4].format(vrf=vrf,
                        protocol=protocol)
            elif vrf and route:
                cmd = self.cli_command[5].format(vrf=vrf,
                        route=route)
            elif protocol:
                cmd = self.cli_command[3].format(protocol=protocol)
            elif route:
                cmd = self.cli_command[2].format(route=route)
            elif vrf:
                cmd = self.cli_command[0].format(vrf=vrf)
            else:
                cmd = self.cli_command[1]
            out = self.device.execute(cmd)
        else:
            out = output
        
        if not vrf:
            vrf = 'default'

        if (route or protocol) in self.protocol_set or (not route and not protocol):
            parser = ShowRouteIpv6(self.device)
            self.schema = parser.schema
            return parser.parse(vrf=vrf, protocol=protocol, output=out)

        else:
            parser = ShowRouteIpv6Word(self.device)
            self.schema=parser.schema
            return parser.parse(vrf=vrf, route=route, output=out)

# ====================================================
#  schema for show route ipv4
# ====================================================
class ShowRouteIpv4Schema(MetaParser):
    """Schema for show route ipv4"""
    schema = {
        'vrf': {
            Any(): {
                Optional('address_family'): {
                    Any(): {
                        Optional('routes'): {
                            Any(): {
                                Optional('route'): str,
                                Optional('active'): bool,
                                Optional('route_preference'): int,
                                Optional('metric'): int,
                                Optional('source_protocol'): str,
                                Optional('source_protocol_codes'): str,
                                Optional('next_hop'): {
                                    Optional('outgoing_interface'): {
                                        Any(): {  # interface  if there is no next_hop
                                            Optional('outgoing_interface'): str,
                                            Optional('updated'): str,
                                        },
                                    },
                                    Optional('next_hop_list'): {
                                        Any(): {  # index
                                            Optional('index'): int,
                                            Optional('next_hop'): str,
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

    """
     Codes: C - connected, S - static, R - RIP, B - BGP, (>) - Diversion path
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2, E - EGP
       i - ISIS, L1 - IS-IS level-1, L2 - IS-IS level-2
       ia - IS-IS inter area, su - IS-IS summary null, * - candidate default
       U - per-user static route, o - ODR, L - local, G  - DAGR, l - LISP
       A - access/subscriber, a - Application route
       M - mobile route, r - RPL, t - Traffic Engineering, (!) - FRR Backup path
    """
    source_protocol_dict = {
        'ospf': ['O', 'IA', 'N1', 'N2', 'E1', 'E2'],
        'odr': ['o'],
        'isis': ['i', 'su', 'L1', 'L2', 'ia'],
        'eigrp': ['D', 'EX'],
        'static': ['S'],
        'egp': ['E'],
        'dagr': ['G'],
        'rpl': ['r'],
        'mobile router': ['M'],
        'lisp': ['I', 'l'],
        'nhrp': ['H'],
        'local': ['L'],
        'connected': ['C'],
        'bgp': ['B'],
        'rip': ['R'],
        'per-user static route': ['U'],
        'access/subscriber': ['A'],
        'traffic engineering': ['t'],
    }

# ====================================================
#  parser for show ip route
# ====================================================
class ShowRouteIpv4(ShowRouteIpv4Schema):
    """Parser for :
       show route ipv4
       show route vrf <vrf> ipv4"""
    command = [
        'show route vrf {vrf} ipv4', 
        'show route ipv4',
        'show route ipv4 {protocol}',
        'show route vrf {vrf} ipv4 {protocol}']
    exclude = ['updated']

    def cli(self, vrf=None, protocol=None, output=None):
        if output is None:
            if vrf and protocol:
                cmd = self.command[3].format(vrf=vrf,
                        protocol=protocol)
            elif vrf:
                cmd = self.command[0].format(vrf=vrf)
            elif protocol:
                cmd = self.command[2].format(protocol=protocol)
            else:
                cmd = self.command[1]
            out = self.device.execute(cmd)
        else:
            out = output

        if not vrf:
            vrf = 'default'

        af = 'ipv4'
        route = ""

        result_dict = {}

        # VRF: VRF501
        p1 = re.compile(r'^\s*VRF: +(?P<vrf>[\w]+)$')

        # i L2 10.154.219.32/32 [115/100030] via 10.4.1.1, 1d06h, HundredGigE0/0/1/1 (!)
        # S    10.4.1.1/32 is directly connected, 01:51:13, GigabitEthernet0/0/0/0
        # S    10.36.3.3/32 [1/0] via 10.2.3.3, 01:51:13, GigabitEthernet0/0/0/1
        # B    10.19.31.31/32 [200/0] via 10.229.11.11, 00:55:14
        # i L1 10.76.23.23/32 [115/11] via 10.2.3.3, 00:52:41, GigabitEthernet0/0/0/1
        # S*   192.168.4.4/10 [111/10] via 172.16.84.11, 1w0d
        # L    ::ffff:192.168.13.12/19 
        # O E1 2001:db8::/39
        # R    10.145.110.10/4 [10/10] via 192.168.10.12, 12:03:42, GigabitEthernet0/0/1/1.1
        # B    10.100.3.160/31 [200/0] via 172.23.6.198 (nexthop in vrf default), 5d13h
        p2 = re.compile(r'^(?P<code1>[\w](\*)*)\s*(?P<code2>\S+)? +(?P<network>\S+\.\S+\.\S+\.\S+)'
                        '( +is +directly +connected)?( +\[(?P<route_preference>[\d\/]+)\]?'
                        '( +via )?(?P<next_hop>[\w\/\:\.]+)?)?\s*'
                        '(:?\(nexthop +in +vrf +default\))?,'
                        '( +(?P<date>[0-9][\w\:]+))?,?( +(?P<interface>[\S]+))?( +(?P<code3>[\w\*\(\>\)\!]+))?$')

        #    [110/2] via 10.1.2.1, 01:50:49, GigabitEthernet0/0/0/3
        p3 = re.compile(r'^\[(?P<route_preference>[\d\/]+)\]'
                        ' +via +(?P<next_hop>[\d\.]+)?,?( +(?P<date>[0-9][\w\:]+),)?( +(?P<interface>[\S]+))?$')

        #       is directly connected, 01:51:13, GigabitEthernet0/0/0/3
        p4 = re.compile(r'^is +directly +connected,'
                        '( +(?P<date>[0-9][\w\:]+),)?( +(?P<interface>[\S]+))?$')

        for line in out.splitlines():
            line = line.strip()
            next_hop = interface = updated = metrics = route_preference = ""

            # VRF: VRF501
            m = p1.match(line)
            if m:
                vrf = m.groupdict()['vrf']
                continue

            # i L2 10.154.219.32/32 [115/100030] via 10.4.1.1, 1d06h, HundredGigE0/0/1/1 (!)
            # S    10.4.1.1/32 is directly connected, 01:51:13, GigabitEthernet0/0/0/0
            # S    10.36.3.3/32 [1/0] via 10.2.3.3, 01:51:13, GigabitEthernet0/0/0/1
            # B    10.19.31.31/32 [200/0] via 10.229.11.11, 00:55:14
            # i L1 10.76.23.23/32 [115/11] via 10.2.3.3, 00:52:41, GigabitEthernet0/0/0/1
            # S*   192.168.4.4/10 [111/10] via 172.16.84.11, 1w0d
            # L    ::ffff:192.168.13.12/19 
            # O E1 2001:db8::/39
            # R    10.145.110.10/4 [10/10] via 192.168.10.12, 12:03:42, GigabitEthernet0/0/1/1.1
            # B    10.100.3.160/31 [200/0] via 172.23.6.198 (nexthop in vrf default), 5d13h            
            m = p2.match(line)
            if m and not p4.match(line):

                group = m.groupdict()
                active = True
                updated = ""
                if group['code1']:
                    source_protocol_codes = group['code1'].strip()
                    for key, val in super().source_protocol_dict.items():
                        source_protocol_replaced = re.split('\*|\(\!\)|\(\>\)', source_protocol_codes)[0].strip()
                        if source_protocol_replaced in val:
                            source_protocol = key

                if group['code2']:
                    source_protocol_codes = '{} {}'.format(source_protocol_codes, m.groupdict()['code2'])

                if group['code3']:
                    source_protocol_codes = '{} {}'.format(source_protocol_codes, m.groupdict()['code3'])

                if group['network']:
                    route = m.groupdict()['network']

                if group['route_preference']:
                    routepreference = m.groupdict()['route_preference']
                    if '/' in routepreference:
                        route_preference = int(routepreference.split('/')[0])
                        metrics = routepreference.split('/')[1]

                index = 1
                if group['next_hop']:
                    next_hop = group['next_hop']
                if group['interface']:
                    interface = group['interface']

                if group['date']:
                    updated = group['date']

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

                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                        ['active'] = active

                    if metrics:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                            ['metric'] = int(metrics)
                    if route_preference:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                            ['route_preference'] = route_preference
                    if source_protocol_codes:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                            ['source_protocol_codes'] = source_protocol_codes
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                            ['source_protocol'] = source_protocol

                    if 'next_hop' not in result_dict['vrf'][vrf]['address_family'][af]['routes'][route]:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] = {}

                    if not next_hop:

                        if 'outgoing_interface' not in result_dict['vrf'][vrf]['address_family'][af] \
                                ['routes'][route]['next_hop']:
                            result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                                ['next_hop']['outgoing_interface'] = {}

                        if m.groupdict()['interface'] and interface not in \
                                result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                                        ['next_hop']['outgoing_interface']:
                            result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                                ['next_hop']['outgoing_interface'][interface] = {}

                        if interface:
                            result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                                ['next_hop']['outgoing_interface'][interface]['outgoing_interface'] = interface
                        if updated:
                            result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                                ['next_hop']['outgoing_interface'][interface]['updated'] = updated

                    else:
                        if 'next_hop_list' not in result_dict['vrf'][vrf]['address_family'][af]['routes'][route][
                            'next_hop']:
                            result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'][
                                'next_hop_list'] = {}

                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                            ['next_hop_list'][index] = {}

                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                            ['next_hop_list'][index]['index'] = index

                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                            ['next_hop_list'][index]['next_hop'] = next_hop

                        if updated:
                            result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                                ['next_hop_list'][index]['updated'] = updated

                        if interface:
                            result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                                ['next_hop_list'][index]['outgoing_interface'] = interface

                continue

            #    [110/2] via 10.1.2.1, 01:50:49, GigabitEthernet0/0/0/3
            m = p3.match(line)

            if m:
                updated = ""
                routepreference = m.groupdict()['route_preference']
                if '/' in routepreference:
                    route_preference = int(routepreference.split('/')[0])
                    metrics = routepreference.split('/')[1]

                next_hop = m.groupdict()['next_hop']

                index += 1
                if m.groupdict()['interface']:
                    interface = m.groupdict()['interface']

                if m.groupdict()['date']:
                    updated = m.groupdict()['date']

                if 'routes' not in result_dict['vrf'][vrf]['address_family'][af]:
                    result_dict['vrf'][vrf]['address_family'][af]['routes'] = {}
                if route not in result_dict['vrf'][vrf]['address_family'][af]['routes']:
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] = {}

                result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['route'] = route

                result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                    ['active'] = active

                if metrics:
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                        ['metric'] = int(metrics)
                if route_preference:
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                        ['route_preference'] = route_preference
                if source_protocol_codes:
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                        ['source_protocol_codes'] = source_protocol_codes
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                        ['source_protocol'] = source_protocol

                if 'next_hop' not in result_dict['vrf'][vrf]['address_family'][af]['routes'][route]:
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] = {}

                if not next_hop:
                    if 'outgoing_interface' not in result_dict['vrf'][vrf]['address_family'][af] \
                            ['routes'][route]['next_hop']:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                            ['next_hop']['outgoing_interface'] = {}

                    if m.groupdict()['interface'] and interface not in \
                            result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                                    ['next_hop']['outgoing_interface']:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                            ['next_hop']['outgoing_interface'][interface] = {}

                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                        ['next_hop']['outgoing_interface'][interface]['outgoing_interface'] = interface
                    if updated:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                            ['next_hop']['outgoing_interface'][interface]['updated'] = updated

                else:
                    if 'next_hop_list' not in result_dict['vrf'][vrf]['address_family'][af]['routes'][route][
                        'next_hop']:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'][
                            'next_hop_list'] = {}

                    if index not in result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                            ['next_hop_list']:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                            ['next_hop_list'][index] = {}

                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                        ['next_hop_list'][index]['index'] = index

                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                        ['next_hop_list'][index]['next_hop'] = next_hop

                    if updated:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                            ['next_hop_list'][index]['updated'] = updated

                    if interface:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                            ['next_hop_list'][index]['outgoing_interface'] = interface

                continue

            #       is directly connected, 01:51:13, GigabitEthernet0/0/0/3
            m = p4.match(line)
            if m:
                updated = ""
                if m.groupdict()['interface']:
                    interface = m.groupdict()['interface']

                if m.groupdict()['date']:
                    updated = m.groupdict()['date']

                if 'outgoing_interface' not in result_dict['vrf'][vrf]['address_family'][af] \
                        ['routes'][route]['next_hop']:
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                        ['next_hop']['outgoing_interface'] = {}

                if m.groupdict()['interface'] and interface not in \
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                                ['next_hop']['outgoing_interface']:
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                        ['next_hop']['outgoing_interface'][interface] = {}

                result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                    ['next_hop']['outgoing_interface'][interface]['outgoing_interface'] = interface
                if updated:
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                        ['next_hop']['outgoing_interface'][interface]['updated'] = updated

                continue

        return result_dict

# ====================================================
#  parser for show route ipv6
# ====================================================

class ShowRouteIpv6(ShowRouteIpv4Schema):
    """Parser for :
       show route ipv6
       show route vrf <vrf> ipv6"""
    command = [
        'show route vrf {vrf} ipv6', 
        'show route ipv6',
        'show route ipv6 {protocol}',
        'show route vrf {vrf} ipv6 {protocol}']

    def cli(self, vrf=None, protocol=None, output=None):
        if output is None:
            if vrf and protocol:
                cmd = self.command[3].format(
                    vrf=vrf,
                    protocol=protocol)
            elif protocol:
                cmd = self.command[2].format(
                    protocol=protocol
                )
            elif vrf:
                cmd = self.command[0].format(
                    vrf=vrf
                )
            else:
                cmd = self.command[1]
            out = self.device.execute(cmd)
        else:
            out = output

        if not vrf:
            vrf = 'default'

        af = 'ipv6'
        route = ""

        result_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # VRF: VRF501
            p1 = re.compile(r'^\s*VRF: +(?P<vrf>[\w]+)$')
            m = p1.match(line)
            if m:
                vrf = m.groupdict()['vrf']
                continue

            #   B    172.16.55.0/22 [200/0] via 10.154.219.128, 1w3d
            p2_1 = re.compile(r'^(?P<code1>[\w\*\(\>\)\!]+)'
                              r'( +(?P<code2>[\w\*\(\>\)\!]+))?'
                              r' +(?P<route>[\w\/\:\.]+) +\[.*$')
            m = p2_1.match(line)
            if m:
                group = m.groupdict()
                active = True
                if group['code1']:
                    source_protocol_codes = group['code1'].strip()
                    for key, val in super().source_protocol_dict.items():
                        source_protocol_replaced = re.split('\*|\(\!\)|\(\>\)', source_protocol_codes)[0].strip()
                        if source_protocol_replaced in val:
                            source_protocol = key

                if group['code2']:
                    source_protocol_codes = '{} {}'.format(source_protocol_codes, group['code2'])

                if group['route']:
                    route = group['route']

                index = 1

                if vrf:
                    if 'vrf' not in result_dict:
                        result_dict['vrf'] = {}

                    if vrf not in result_dict['vrf']:
                        result_dict['vrf'][vrf] = {}

                    if 'address_family' not in result_dict['vrf'][vrf]:
                        result_dict['vrf'][vrf]['address_family'] = {}
                        addr_dict = result_dict['vrf'][vrf]['address_family']

                    if af and af not in addr_dict:
                        addr_dict[af] = {}

                    if 'routes' not in addr_dict[af]:
                        addr_dict[af]['routes'] = {}
                    if route not in addr_dict[af]['routes']:
                        addr_dict[af]['routes'][route] = {}

                    addr_dict[af]['routes'][route]['route'] = route

                    addr_dict[af]['routes'][route]['active'] = active

                    if source_protocol_codes:
                        addr_dict[af]['routes'][route] \
                            ['source_protocol_codes'] = source_protocol_codes
                        addr_dict[af]['routes'][route] \
                            ['source_protocol'] = source_protocol

            #   [1/0] via 2001:20:1:2::1, 01:52:23, GigabitEthernet0/0/0/0
            #   [200/0] via ::ffff:10.229.11.11 (nexthop in vrf default), 00:55:12
            #   B    172.16.55.0/22 [200/0] via 10.154.219.128, 1w3d
            #   [0/0] via ::, 5w2d
            p3 = re.compile(r'.*\[(?P<route_preference>[\d\/]+)\]'
                            r' +via +(?P<next_hop>[\w\:\.\)]+)?( \(nexthop in '
                            r'vrf default\))?,? +(?P<date>[0-9][\w\:]+)?(?:,?( +'
                            r'(?P<interface>[\S]+))?$)?')

            m = p3.match(line)

            if m:
                updated = interface = ""
                routepreference = m.groupdict()['route_preference']
                if '/' in routepreference:
                    route_preference = int(routepreference.split('/')[0])
                    metrics = routepreference.split('/')[1]

                if m.groupdict()['next_hop']:
                    next_hop = m.groupdict()['next_hop']

                if m.groupdict()['interface']:
                    interface = m.groupdict()['interface']

                if m.groupdict()['date']:
                    updated = m.groupdict()['date']

                if 'vrf' not in result_dict:
                    result_dict['vrf'] = {}

                if vrf not in result_dict['vrf']:
                    result_dict['vrf'][vrf] = {}

                if 'address_family' not in result_dict['vrf'][vrf]:
                    addr_dict = {}

                if af and af not in addr_dict:
                    addr_dict[af] = {}
                if 'routes' not in addr_dict[af]:
                    addr_dict[af]['routes'] = {}
                if route not in addr_dict[af]['routes']:
                    addr_dict[af]['routes'][route] = {}

                addr_dict[af]['routes'][route]['route'] = route
                if metrics:
                    addr_dict[af]['routes'][route] \
                        ['metric'] = int(metrics)
                if route_preference:
                    addr_dict[af]['routes'][route] \
                        ['route_preference'] = route_preference

                if 'next_hop' not in addr_dict[af]['routes'][route]:
                    addr_dict[af]['routes'][route]['next_hop'] = {}

                if not next_hop:
                    if 'outgoing_interface' not in addr_dict[af] \
                            ['routes'][route]['next_hop']:
                        addr_dict[af]['routes'][route] \
                            ['next_hop']['outgoing_interface'] = {}

                    if m.groupdict()['interface'] and interface not in \
                            addr_dict[af]['routes'][route] \
                                    ['next_hop']['outgoing_interface']:
                        addr_dict[af]['routes'][route] \
                            ['next_hop']['outgoing_interface'][interface] = {}

                    if interface:
                        addr_dict[af]['routes'][route] \
                            ['next_hop']['outgoing_interface'][interface]['outgoing_interface'] = interface
                    if updated:
                        addr_dict[af]['routes'][route] \
                            ['next_hop']['outgoing_interface'][interface]['updated'] = updated

                else:
                    if 'next_hop_list' not in addr_dict[af]['routes'][route][
                        'next_hop']:
                        addr_dict[af]['routes'][route]['next_hop'][
                            'next_hop_list'] = {}

                    if index not in addr_dict[af]['routes'][route]['next_hop'] \
                            ['next_hop_list']:
                        addr_dict[af]['routes'][route]['next_hop'] \
                            ['next_hop_list'][index] = {}

                    addr_dict[af]['routes'][route]['next_hop'] \
                        ['next_hop_list'][index]['index'] = index

                    addr_dict[af]['routes'][route]['next_hop'] \
                        ['next_hop_list'][index]['next_hop'] = next_hop

                    if interface:
                        addr_dict[af]['routes'][route]['next_hop'] \
                            ['next_hop_list'][index]['outgoing_interface'] = interface

                    if updated:
                        addr_dict[af]['routes'][route]['next_hop'] \
                            ['next_hop_list'][index]['updated'] = updated
                index += 1
                continue

            #   01:52:24, Loopback0
            p4 = re.compile(r'^\s*(?P<date>[\w\:]+),'
                            ' +(?P<interface>[\S]+)$')
            m = p4.match(line)
            if m:
                interface = updated = ""
                if m.groupdict()['interface']:
                    interface = m.groupdict()['interface']

                if m.groupdict()['date']:
                    updated = m.groupdict()['date']

                if 'vrf' not in result_dict:
                    result_dict['vrf'] = {}

                if vrf not in result_dict['vrf']:
                    result_dict['vrf'][vrf] = {}

                if 'address_family' not in result_dict['vrf'][vrf]:
                    addr_dict = {}

                if af and af not in addr_dict:
                    addr_dict[af] = {}
                if 'routes' not in addr_dict[af]:
                    addr_dict[af]['routes'] = {}
                if route not in addr_dict[af]['routes']:
                    addr_dict[af]['routes'][route] = {}

                addr_dict[af]['routes'][route]['route'] = route

                if 'next_hop' not in addr_dict[af]['routes'][route]:
                    addr_dict[af]['routes'][route]['next_hop'] = {}

                if 'outgoing_interface' not in addr_dict[af] \
                        ['routes'][route]['next_hop']:
                    addr_dict[af]['routes'][route] \
                        ['next_hop']['outgoing_interface'] = {}

                if m.groupdict()['interface'] and interface not in \
                        addr_dict[af]['routes'][route] \
                                ['next_hop']['outgoing_interface']:
                    addr_dict[af]['routes'][route] \
                        ['next_hop']['outgoing_interface'][interface] = {}

                if interface:
                    addr_dict[af]['routes'][route] \
                        ['next_hop']['outgoing_interface'][interface]['outgoing_interface'] = interface
                if updated:
                    addr_dict[af]['routes'][route] \
                        ['next_hop']['outgoing_interface'][interface]['updated'] = updated

                continue
            
            # Routing Descriptor Blocks
            p5 = re.compile(r'^(Routing +Descriptor +Blocks)|(No +advertising +protos\.)$')
            m = p5.match(line)
            if m:
                continue

            # S    2001:1:1:1::1/128
            # L    2001:2:2:2::2/128 is directly connected,
            # i L1 2001:23:23:23::23/128
            # R*   ::/128 
            # L    ::ffff:192.168.1.1/10
            p6 = re.compile(r'^(?P<code1>[\w\*\(\>\)\!]+)( +'
                            r'(?P<code2>[\w\*\(\>\)\!]+))? +(?P<route>[\w\/\:\.]+)'
                            r'( +is +directly +connected,)?$')
            m = p6.match(line)

            if m:
                group = m.groupdict()
                active = True
                if group['code1']:
                    source_protocol_codes = group['code1'].strip()
                    for key, val in super().source_protocol_dict.items():
                        source_protocol_replaced = re.split('\*|\(\!\)|\(\>\)', source_protocol_codes)[0].strip()
                        if source_protocol_replaced in val:
                            source_protocol = key

                if group['code2']:
                    source_protocol_codes = '{} {}'.format(source_protocol_codes, group['code2'])

                if group['route']:
                    route = group['route']

                index = 1

                if vrf:
                    if 'vrf' not in result_dict:
                        result_dict['vrf'] = {}

                    if vrf not in result_dict['vrf']:
                        result_dict['vrf'][vrf] = {}

                    if 'address_family' not in result_dict['vrf'][vrf]:
                        result_dict['vrf'][vrf]['address_family'] = {}
                        addr_dict = result_dict['vrf'][vrf]['address_family']

                    if af and af not in addr_dict:
                        addr_dict[af] = {}

                    if 'routes' not in addr_dict[af]:
                        addr_dict[af]['routes'] = {}
                    if route not in addr_dict[af]['routes']:
                        addr_dict[af]['routes'][route] = {}

                    addr_dict[af]['routes'][route]['route'] = route

                    addr_dict[af]['routes'][route]['active'] = active
                    if source_protocol_codes:
                        addr_dict[af]['routes'][route] \
                            ['source_protocol_codes'] = source_protocol_codes
                        addr_dict[af]['routes'][route] \
                            ['source_protocol'] = source_protocol
                continue

        return result_dict


# ====================================================
#  schema for show ip route <WORD>
# ====================================================
class ShowRouteIpWordSchema(MetaParser):
    """Schema for show ip route <WORD>"""
    schema = {
        'entry': {
            Any(): {
                'ip': str,
                'mask': str,
                'known_via': str,
                'distance': str,
                'metric': str,
                Optional('type'): str,
                Optional('installed'):{
                    'date': str,
                    'for': str,
                },
                'paths': {
                    Any(): {
                        Optional('nexthop'): str,
                        Optional('from'): str,
                        Optional('interface'): str,
                        Optional('metric'): str,
                        Optional('share_count'): str,
                    }
                },
                Optional('redist_advertisers'):{
                    Any(): {
                        'protoid': int,
                        'clientid': int,
                    }
                }
            }
        },
        'total_prefixes': int,
    }

# ====================================================
#  parser for show ip route <WORD>
# ====================================================
class ShowRouteIpWord(ShowRouteIpWordSchema):
    """Parser for :
       show route ipv4 <Hostname or A.B.C.D>
       show route ipv4 vrf <vrf> <Hostname or A.B.C.D>"""
    command = ['show route ipv4 {route}',
                'show route vrf {vrf} ipv4 {route}']
    IP_VER = 'ip'

    def cli(self, route, vrf=None, output=None):

        if output is None:
            if vrf and route:
                cmd = self.command[1].format(vrf=vrf,
                        route=route)
            else:
                cmd = self.command[0].format(route=route)
            out = self.device.execute(cmd)
        else:
            out = output

        if not vrf:
            vrf = 'default'

        # initial regexp pattern
        # Routing entry for 10.151.0.0/24, 1 known subnets
        # Routing entry for 0.0.0.0/0, supernet
        # Routing entry for 192.168.154.0/24
        p1 = re.compile(r'^Routing +entry +for +(?P<entry>(?P<ip>[\w\:\.]+)'
                        r'\/(?P<mask>\d+))(?:, +(?P<net>[\w\s]+))?$')

        # Known via "connected", distance 0, metric 0 (connected)
        # Known via "eigrp 1", distance 130, metric 10880, type internal
        # Known via "bgp 65161", distance 20, metric 0, candidate default path
        p2 = re.compile(r'^Known +via +\"(?P<known_via>[\w\s]+)\", '
                        r'+distance +(?P<distance>\d+), +metric '
                        r'+(?P<metric>\d+),? *(?:\S+ (?P<type>[\w\- '
                        r']+))?,? *.*$')

        # * directly connected, via GigabitEthernet1.120
        p3 = re.compile(r'^(\* +)?directly +connected, via +(?P<interface>\S+)$')
        
        # Route metric is 10880, traffic share count is 1
        p4 = re.compile(r'^Route +metric +is +(?P<metric>\d+)(, +'
                        r'traffic +share +count +is +(?P<share_count>\d+))?$')

        # eigrp/100 (protoid=5, clientid=22)
        p5 = re.compile(r'^(?P<redist_advertiser>\S+) +\(protoid=(?P<protoid>\d+)'
                        r', +clientid=(?P<clientid>\d+)\)$')

        # fe80::f816:3eff:fe76:b56d, from fe80::f816:3eff:fe76:b56d, via GigabitEthernet0/0/0/0.390
        p6 = re.compile(r'^(?P<nexthop>\S+), from +(?P<from>\S+), '
                        r'+via +(?P<interface>\S+)$')
        
        # Installed Oct 23 22:09:38.380 for 5d21h
        p7 = re.compile(r'^^Installed +(?P<date>[\S\s]+) +for +(?P<for>\S+)$$')

        # initial variables
        ret_dict = {}
        index = 0

        for line in out.splitlines():
            line = line.strip()

            # Routing entry for 10.151.0.0/24, 1 known subnets
            # Routing entry for 0.0.0.0/0, supernet
            # Routing entry for 192.168.154.0/24
            m = p1.match(line)
            if m:
                group = m.groupdict()
                entry = group.pop('entry')
                entry_dict = ret_dict.setdefault('entry', {}).setdefault(entry, {})
                entry_dict.update({k:v for k,v in group.items() if v})
                continue

            # Known via "static", distance 1, metric 0, candidate default path
            # Known via "eigrp 1", distance 130, metric 10880, type internal
            # Known via "rip", distance 120, metric 2
            # Known via "connected", distance 0, metric 0 (connected)
            # Known via "eigrp 1", distance 130, metric 10880, type internal
            # Known via "bgp 65161", distance 20, metric 0, candidate default path
            m = p2.match(line)
            if m:
                group = m.groupdict()
                entry_dict.update({k:v for k,v in group.items() if v})
                continue

            # * directly connected, via GigabitEthernet1.120
            m = p3.match(line)
            if m:
                group = m.groupdict()
                index += 1
                path_dict = entry_dict.setdefault('paths', {}).setdefault(index, {})
                if group['interface']:
                    path_dict.update({'interface': group['interface']})
                continue

            # Route metric is 10880, traffic share count is 1
            m = p4.match(line)
            if m:
                group = m.groupdict()
                path_dict = entry_dict.setdefault('paths', {}).setdefault(index, {})
                path_dict.update({k:v for k,v in group.items() if v})
                continue
            
            # eigrp/100 (protoid=5, clientid=22)
            m = p5.match(line)
            if m:
                group = m.groupdict()
                redist_advertiser = group['redist_advertiser']
                protoid = int(group['protoid'])
                clientid = int(group['clientid'])
                redist_advertiser_dict = entry_dict.setdefault('redist_advertisers', {}). \
                                setdefault(redist_advertiser, {})
                redist_advertiser_dict.update({'protoid': protoid})
                redist_advertiser_dict.update({'clientid': clientid})
                continue
            
            # fe80::f816:3eff:fe76:b56d, from fe80::f816:3eff:fe76:b56d, via GigabitEthernet0/0/0/0.390
            m = p6.match(line)
            if m:
                group = m.groupdict()
                nexthop = group['nexthop']
                _from = group['from']
                interface = group['interface']
                index += 1
                path_dict = entry_dict.setdefault('paths', {}).setdefault(index, {})
                path_dict.update({'interface': interface})
                path_dict.update({'from': _from})
                path_dict.update({'nexthop': nexthop})
                continue
            
            # Installed Oct 23 22:09:38.380 for 5d21h
            m = p7.match(line)
            if m:
                group = m.groupdict()
                installed_dict = entry_dict.setdefault('installed', {})
                installed_dict.update({k:v for k,v in group.items() if v})
                continue

        ret_dict.update({'total_prefixes': index}) if ret_dict else None
        return ret_dict

# ====================================================
#  schema for show route ipv6 <WORD>
# ====================================================
class ShowRouteIpv6WordSchema(MetaParser):
    """Schema for show route ipv6 <WORD>"""
    schema = {
        'entry': {
            Any(): {
                'ip': str,
                'mask': str,
                'known_via': str,
                'distance': str,
                'metric': str,
                Optional('type'): str,
                Optional('installed'): {
                    'for': str,
                    'date': str,
                },
                'paths': {
                    Any(): {
                        Optional('nexthop'): str,
                        Optional('from'): str,
                        Optional('interface'): str,
                        Optional('metric'): str,
                        Optional('share_count'): str,
                    }
                },
                Optional('redist_advertisers'):{
                    Any(): {
                        'protoid': int,
                        'clientid': int,
                    }
                }
            }
        },
        'total_prefixes': int,
    }

# ====================================================
#  parser for show ipv6 route <WORD>
# ====================================================
class ShowRouteIpv6Word(ShowRouteIpv6WordSchema, ShowRouteIpWord):
    """Parser for :
       show route ipv6 <Hostname or A.B.C.D>
       show route ipv6 vrf <vrf> <Hostname or A.B.C.D>"""
    command = ['show route ipv6 {route}',
                'show route vrf {vrf} ipv6 {route}']
    IP_VER = 'ipv6'

    def cli(self, route, vrf=None, interface=None, output=None):
        
        if output is None:
            if vrf and route:
                cmd = self.command[1].format(vrf=vrf,
                        route=route)
            else:
                cmd = self.command[0].format(route=route)
            out = self.device.execute(cmd)
        else:
            out = output
        if not vrf:
            vrf = 'default'
        return super().cli(route=route, vrf=vrf, output=out)
