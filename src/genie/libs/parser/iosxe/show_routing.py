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
class ShowIpRouteDistributor(MetaParser):
    """distributor class for show ip route"""
    cli_command = ['show ip route vrf {vrf}',
                   'show ip route vrf {vrf} {route}',
                   'show ip route vrf {vrf} {protocol}',
                   'show ip route',
                   'show ip route {route}',
                   'show ip route {protocol}']

    protocol_set = {'ospf', 'odr', 'isis', 'eigrp', 'static', 'mobile',
                    'rip', 'lisp', 'nhrp', 'local', 'connected', 'bgp'}

    def cli(self, vrf=None, route=None, protocol=None, output=None):

        if output is None:
            if vrf and protocol:
                cmd = self.cli_command[2].format(vrf=vrf, protocol=protocol)
            elif vrf and route:
                cmd = self.cli_command[1].format(vrf=vrf, route=route)
            elif vrf:
                cmd = self.cli_command[0].format(vrf=vrf)
            elif protocol:
                cmd = self.cli_command[5].format(protocol=protocol)
            elif route:
                cmd = self.cli_command[4].format(route=route)
            else:
                cmd = self.cli_command[3]
            out = self.device.execute(cmd)
        else:
            out = output

        if (route or protocol) in self.protocol_set or (not route and not protocol):
            parser = ShowIpRoute(self.device)
            self.schema = parser.schema
            return parser.parse(output=out)

        else:
            parser = ShowIpRouteWord(self.device)
            self.schema=parser.schema
            return parser.parse(output=out)

# ====================================================
#  distributor class for show ipv6 route
# ====================================================
class ShowIpv6RouteDistributor(MetaParser):
    """distributor class for show ipv6 route"""
    cli_command = ['show ipv6 route vrf {vrf}',
                   'show ipv6 route vrf {vrf} {route}',
                   'show ipv6 route vrf {vrf} {protocol}',
                   'show ipv6 route',
                   'show ipv6 route {route}',
                   'show ipv6 route {protocol}',
                   'show ipv6 route interface {interface}',
                   'show ipv6 route vrf {vrf} interface {interface}']

    protocol_set = {'ospf', 'odr', 'isis', 'eigrp', 'static', 'mobile',
                    'rip', 'lisp', 'nhrp', 'local', 'connected', 'bgp'}

    def cli(self, vrf=None, route=None, protocol=None, interface=None, output=None):
        
        if output is None:

            if vrf and route:
                cmd = self.cli_command[1].format(vrf=vrf, route=route)
            elif vrf and protocol:
                cmd = self.cli_command[2].format(vrf=vrf, protocol=protocol)
            elif vrf and interface:
                cmd = self.cli_command[7].format(vrf=vrf, interface=interface)
            elif vrf:
                cmd = self.cli_command[0].format(vrf=vrf)
            elif route:
                cmd = self.cli_command[4].format(route=route)
            elif protocol:
                cmd = self.cli_command[5].format(protocol=protocol)
            elif interface:
                cmd = self.cli_command[6].format(interface=interface)
            else:
                cmd = self.cli_command[3]
            out = self.device.execute(cmd)
        else:
            out = output
        
        if not vrf:
            vrf = 'default'

        if (route or protocol) in self.protocol_set or (not route and not protocol):
            parser = ShowIpv6Route(self.device)
            self.schema = parser.schema
            return parser.parse(vrf=vrf, protocol=protocol, output=out)

        else:
            parser = ShowIpv6RouteWord(self.device)
            self.schema=parser.schema
            return parser.parse(vrf=vrf, route=route, output=out)

# ====================================================
#  schema for show ip route
# ====================================================
class ShowIpRouteSchema(MetaParser):
    """Schema for show ip route"""
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
                                Optional('mask'): str,
                                Optional('known_via'): str,
                                Optional('distance'): int,
                                Optional('type'): str,
                                Optional('net'): str,
                                Optional('redist_via'): str,
                                Optional('redist_via_tag'): str,
                                Optional('update'): {
                                    'from': str,
                                    'interface': str,
                                    'age': str
                                },
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
                                            Optional('age'): str,
                                            Optional('from'): str,
                                            Optional('metric'): str,
                                            Optional('share_count'): str,
                                            Optional('loading'): str,
                                            Optional('hops'): str,
                                            Optional('minimum_mtu'): str,
                                            Optional('reliability'): str,
                                            Optional('minimum_bandwidth'): str,
                                            Optional('total_delay'): str,
                                            Optional('vrf'): str
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
        show ip route vrf <vrf>"""
    # not using name 'cli_command' because dont want find_parsers() to discover them
    parser_command = ['show ip route vrf {vrf}', 'show ip route vrf {vrf} {protocol}',
                   'show ip route', 'show ip route {protocol}']
    exclude = ['updated']
    IP_VER='ipv4'

    def cli(self, vrf=None, protocol=None, output=None):

        if output is None:
            if vrf and protocol:
                cmd = self.parser_command[1].format(vrf=vrf, protocol=protocol)
            elif vrf:
                cmd = self.parser_command[0].format(vrf=vrf)
            elif protocol:
                cmd = self.parser_command[3].format(protocol=protocol)
            else:
                cmd = self.parser_command[2]
            out = self.device.execute(cmd)
        else:
            out = output

        af = self.IP_VER
        route = ""
        if not vrf:
            vrf = 'default'

        source_protocol_dict = {}
        source_protocol_dict['ospf'] = ['O','OI','OE1','OE2','ON1','ON2','IA','N1','N2','E1','E2', '+', '%', 'p', '&']
        source_protocol_dict['odr'] = ['o']
        source_protocol_dict['isis'] = ['i','su','L1','L2','IA', 'I1', 'I2']
        source_protocol_dict['eigrp'] = ['D','EX', '+', '%', 'p', '&']
        source_protocol_dict['static'] = ['S', '+', '%', 'p', '&']
        source_protocol_dict['mobile'] = ['M']
        source_protocol_dict['rip'] = ['R']
        source_protocol_dict['lisp'] = ['l','la','lr','ld','lA','le','lp','ls']
        source_protocol_dict['nhrp'] = ['H']
        source_protocol_dict['local'] = ['L']
        source_protocol_dict['connected'] = ['C', '+', '%', 'p', '&']
        source_protocol_dict['local_connected'] = ['LC']
        source_protocol_dict['bgp'] = ['B', '+', '%', 'p', '&']
        source_protocol_dict['nd'] = ['ND','NDp']
        source_protocol_dict['Per-user Static route'] = ['U']
        source_protocol_dict['Destination'] = ['DCE']
        source_protocol_dict['Redirect'] = ['NDr']


        result_dict = {}

        # initial regexp pattern
        p100 = re.compile(r'^Routing +entry +for +'
                        '(?P<entry>(?P<ip>[\w\:\.]+)\/(?P<mask>\d+))'
                        '(, +(?P<net>[\w\s]+))?$')
        p200 = re.compile(r'^Known +via +\"(?P<known_via>[\w\s]+)\", +'
                        'distance +(?P<distance>\d+), +'
                        'metric +(?P<metric>\d+)'
                        '(, +type +(?P<type>[\w\-\s]+)(?P<connected>, connected)?)?$')
        p300 = re.compile(r'^Redistributing +via +(?P<redist_via>\w+) *'
                        '(?P<redist_via_tag>\d+)?$')
        p400 = re.compile(r'^Last +update +from +(?P<from>[\w\.]+) +'
                        'on +(?P<interface>[\w\.\/\-]+), +'
                        '(?P<age>[\w\.\:]+) +ago$')
        p500 = re.compile(r'^\*? *(?P<nexthop>[\w\.]+)(, +'
                        'from +(?P<from>[\w\.]+), +'
                        '(?P<age>[\w\.\:]+) +ago, +'
                        'via +(?P<interface>[\w\.\/\-]+))?$')
        p600 = re.compile(r'^Route +metric +is +(?P<metric>\d+), +'
                        'traffic +share +count +is +(?P<share_count>\d+)$')

        p600 = re.compile(r'^Route +metric +is +(?P<metric>\d+), +'
                          'traffic +share +count +is +(?P<share_count>\d+)$')
        p700 = re.compile(r'^Total +delay +is +(?P<total_delay>\d+) +microseconds, '
                          '+minimum +bandwidth +is +(?P<minimum_bandwidth>\d+) +Kbit$')
        p800 = re.compile(r'^Reliability +(?P<reliability>[\d\/]+), +minimum +MTU +(?P<minimum_mtu>\d+) +bytes$')
        p900 = re.compile(r'^Loading +(?P<loading>[\d\/]+), Hops +(?P<hops>\d+)$')

        # initial variables
        ret_dict = {}
        index = 0
        active = False

        # Routing Table: VRF1
        # Routing Table: VRF-infra
        p1 = re.compile(r'^Routing Table: +(?P<vrf>[\w?-]+)$')

        # 10.1.0.0/32 is subnetted, 1 subnets
        # 10.0.0.0/8 is variably subnetted, 5 subnets, 2 masks
        p2 = re.compile(r'^(?P<subnetted_ip>[\d\/\.]+) +is +(variably )?subnetted, '
                        r'+(?P<number_of_subnets>[\d]+) +subnets(, +(?P<number_of_masks>[\d]+) +masks)?$')
        
        # C        10.4.1.1 is directly connected, Loopback0
        # S        10.16.2.2 [1/0] via 10.186.2.2, GigabitEthernet0/1
        # S*       10.16.2.2 [1/0] via 10.186.2.2, GigabitEthernet0/1
        # O        10.2.3.0/24 [110/2] via 10.186.2.2, 06:46:59, GigabitEthernet0/1
        # i L1     10.151.22.22 [115/20] via 10.186.2.2, 06:47:04, GigabitEthernet0/1
        # D        192.168.205.1
        # S*       0.0.0.0/0 [1/0] via 10.50.15.1
        # L        FF00::/8 [0/0]
        # S   %    10.34.0.1 [1/0] via 192.168.16.1
        # C   p    10.34.0.2 is directly connected, Loopback0
        # S   &    10.69.0.0 [1/0] via 10.34.0.1
        # S   +    10.186.1.0 [1/0] via 10.144.0.1 (red)
        # B   +    10.55.0.0 [20/0] via 10.144.0.1 (red), 00:00:09
        # i*L1  0.0.0.0/0 [115/100] via 10.12.7.37, 3w6d, Vlan101
        # ND  ::/0 [2/0]
        # NDp 2001:103::/64 [2/0]
        if self.IP_VER == 'ipv4':
            p3 = re.compile(
                r'^(?P<code>[A-Za-z]{0,2}[0-9]*(\*[A-Za-z]{0,2}[0-9]*)?) +(?P<code1>[A-Z][a-z]|[A-Z][\d]|[a-z]{2}|[+%&p])?\s*(?P<network>[0-9\.\:\/]+)?( '
                r'+is +directly +connected,)? *\[?(?P<route_preference>[\d\/]+)?\]?,?(\s+tag\s(?P<tag_id>\d+))?( *('
                r'via +)?(?P<next_hop>[\d\.]+))?,?( +\((?P<nh_vrf>[\w+]+)\))?,?( +(?P<date>[0-9][\w\:]+))?,?( +(?P<interface>[\S]+))?$')
        else:
            p3 = re.compile(
                r'^(?!via)(?P<code>[A-Za-z]{0,3}[0-9]*(\*[A-Za-z]{0,2}[0-9]*)?) +(?P<code1>[A-Z][a-z]|[A-Z][\d]|[a-z]{2}[+%&p])?\s*(?P<network>[\w\.\:\/]+)?'
                r'( +is +directly +connected,)? *\[?(?P<route_preference>[\d\/]+)?\]?,?(\s+tag\s(?P<tag_id>\d+))?'
                r'( *(via +)?(?P<next_hop>[\d\.]+))?,?( +\((?P<nh_vrf>[\w+]+)\))?,?( +(?P<date>[0-9][\w\:]+))?,?( +(?P<interface>[\S]+))?$')
        
        #    [110/2] via 10.1.2.2, 06:46:59, GigabitEthernet0/0
        p4 = re.compile(r'^\[(?P<route_preference>[\d\/]+)\] +via +(?P<next_hop>[\d\.]+)?,?'
                        r'( +(?P<date>[0-9][\w\:]+),?)?( +(?P<interface>[\S]+))?$')
        
        #       is directly connected, GigabitEthernet0/2
        p5 = re.compile(r'^is +directly +connected,( +\[(?P<route_preference>[\d\/]+)\] '
                        r'+via +(?P<next_hop>[\d\.]+)?,)?( +(?P<date>[0-9][\w\:]+),)?'
                        r'( +(?P<interface>[\S]+))?$')

        #      via 2001:DB8:1:1::2
        #      via 10.4.1.1%default, indirectly connected
        #      via 2001:DB8:4:6::6
        #      via 2001:DB8:20:4:6::6%VRF2
        #      via Null0, receive
        #      via 33.33.33.33%default, Vlan100%default
        p6 = re.compile(r'^via( +(?P<next_hop>[\w]+[.:][\w\:\.\%]{4,}),?)?'
                        r'( +(?P<interface>[\w\.\/\-\_]+[\w\:\.\%]+),?)?,?( +receive)?'
                        r'( +directly connected)?( +indirectly connected)?$')

        for line in out.splitlines():
            if line:
                line = line.strip()
            else:
                continue

            next_hop = interface = updated = metrics = route_preference = nh_vrf = ""
            # Routing Table: VRF1
            # Routing Table: VRF-infra
            m = p1.match(line)
            if m:
                vrf = m.groupdict()['vrf']
                results_dict = result_dict.setdefault('vrf', {}).setdefault(vrf, {})
                continue

            # 10.1.0.0/32 is subnetted, 1 subnets
            # 10.0.0.0/8 is variably subnetted, 5 subnets, 2 masks
            m = p2.match(line)
            if m:
                # if you see the issue by "show ip route", it means that active is True.
                # it means all routes in the output should be active=True
                active = True
                netmask = number_of_masks= ""
                number_of_subnets = m.groupdict()['number_of_subnets']
                if m.groupdict()['number_of_masks']:
                    number_of_masks = m.groupdict()['number_of_masks']

                if m.groupdict()['subnetted_ip']:
                    subnetted_ip = m.groupdict()['subnetted_ip']
                    if '/' in subnetted_ip:
                        netmask = subnetted_ip.split('/')[1]
                continue

            # C        10.4.1.1 is directly connected, Loopback0
            # S        10.16.2.2 [1/0] via 10.186.2.2, GigabitEthernet0/1
            # S*       10.16.2.2 [1/0] via 10.186.2.2, GigabitEthernet0/1
            # O        10.2.3.0/24 [110/2] via 10.186.2.2, 06:46:59, GigabitEthernet0/1
            # i L1     10.151.22.22 [115/20] via 10.186.2.2, 06:47:04, GigabitEthernet0/1
            # D        192.168.205.1
            # S*       0.0.0.0/0 [1/0] via 10.50.15.1
            # L        FF00::/8 [0/0]
            # S   %    10.34.0.1 [1/0] via 192.168.16.1
            # C   p    10.34.0.2 is directly connected, Loopback0
            # S   &    10.69.0.0 [1/0] via 10.34.0.1
            # S   +    10.186.1.0 [1/0] via 10.144.0.1 (red)
            # B   +    10.55.0.0 [20/0] via 10.144.0.1 (red), 00:00:09
            # ND  ::/0 [2/0]
            # NDp 2001:103::/64 [2/0]
            m = p3.match(line)
            if m:
                active = True
                if m.groupdict()['code']:
                    source_protocol_codes = m.groupdict()['code'].strip()
                    for key,val in source_protocol_dict.items():
                        source_protocol_replaced = source_protocol_codes.split('*')[0]
                        if source_protocol_replaced in val:
                            source_protocol = key

                if m.groupdict()['code1']:
                    source_protocol_codes = '{} {}'.format(source_protocol_codes, m.groupdict()['code1'])

                if m.groupdict()['network']:
                    network = m.groupdict()['network']
                    if '/' not in network and self.IP_VER == 'ipv4':
                        route = '{}/{}'.format(network,netmask)
                    else:
                        route = network

                if not m.groupdict()['network']:
                    route = route

                if m.groupdict()['route_preference']:
                    routepreference = m.groupdict()['route_preference']
                    if '/' in routepreference:
                        route_preference = routepreference.split('/')[0]
                        metrics = routepreference.split('/')[1]

                if m.groupdict()['next_hop']:
                    next_hop = m.groupdict()['next_hop']
                    index = 1
                else:
                    index = 0

                if m.groupdict()['interface']:
                    interface = m.groupdict()['interface']

                if m.groupdict()['date']:
                    updated = m.groupdict()['date']

                if m.groupdict()['nh_vrf']:
                    nh_vrf = m.groupdict()['nh_vrf']

                route_dict = result_dict.setdefault('vrf', {}).setdefault(vrf, {})\
                                        .setdefault('address_family', {}).setdefault(af, {})\
                                        .setdefault('routes', {}).setdefault(route, {})

                route_dict['route'] = route
                route_dict['active'] = active

                if metrics:
                    route_dict['metric'] = int(metrics)
                if route_preference:
                    route_dict['route_preference'] = int(route_preference)
                if source_protocol_codes:
                    route_dict['source_protocol_codes'] = source_protocol_codes
                    route_dict['source_protocol'] = source_protocol

                next_hop_dict = route_dict.setdefault('next_hop', {})

                if not next_hop and interface:
                    intf_dict = next_hop_dict.setdefault('outgoing_interface', {})
                    intf_dict.setdefault(interface, {}).update({'outgoing_interface': interface})

                elif next_hop:
                    idx_dict = next_hop_dict.setdefault('next_hop_list', {}).setdefault(index, {})
                    idx_dict['index'] = index
                    idx_dict['next_hop'] = next_hop

                    if updated:
                        idx_dict['updated'] = updated
                    if interface:
                        idx_dict['outgoing_interface'] = interface
                    if nh_vrf:
                        idx_dict['vrf'] = nh_vrf

                continue

            #    [110/2] via 10.1.2.2, 06:46:59, GigabitEthernet0/0
            m = p4.match(line)
            if m:
                routepreference = m.groupdict()['route_preference']
                if routepreference and '/' in routepreference:
                    route_preference = routepreference.split('/')[0]
                    metrics = routepreference.split('/')[1]

                next_hop = m.groupdict()['next_hop']
                index +=1
                if m.groupdict()['interface']:
                    interface = m.groupdict()['interface']

                if m.groupdict()['date']:
                    updated = m.groupdict()['date']

                route_dict = result_dict.setdefault('vrf', {}).setdefault(vrf, {})\
                                        .setdefault('address_family', {}).setdefault(af, {})\
                                        .setdefault('routes', {}).setdefault(route, {})

                route_dict['route'] = route
                route_dict['active'] = active

                if metrics:
                    route_dict['metric'] = int(metrics)
                if route_preference:
                    route_dict['route_preference'] = int(route_preference)
                if source_protocol_codes:
                    route_dict['source_protocol_codes'] = source_protocol_codes
                    route_dict['source_protocol'] = source_protocol

                next_hop_dict = route_dict.setdefault('next_hop', {})

                if not next_hop and interface:
                    intf_dict = next_hop_dict.setdefault('outgoing_interface', {})
                    intf_dict.setdefault(interface, {}).update({'outgoing_interface': interface})

                elif next_hop:
                    idx_dict = next_hop_dict.setdefault('next_hop_list', {}).setdefault(index, {})
                    idx_dict['index'] = index
                    idx_dict['next_hop'] = next_hop

                    if updated:
                        idx_dict['updated'] = updated
                    if interface:
                        idx_dict['outgoing_interface'] = interface

                continue

            #       is directly connected, GigabitEthernet0/2
            m = p5.match(line)
            if m:

                if m.groupdict()['route_preference']:
                    routepreference = m.groupdict()['route_preference']
                    if '/' in routepreference:
                        route_preference = routepreference.split('/')[0]
                        metrics = routepreference.split('/')[1]

                index += 1
                if m.groupdict()['next_hop']:
                    next_hop = m.groupdict()['next_hop']
                if m.groupdict()['interface']:
                    interface = m.groupdict()['interface']
                if m.groupdict()['date']:
                    updated = m.groupdict()['date']

                route_dict = result_dict.setdefault('vrf', {}).setdefault(vrf, {})\
                                        .setdefault('address_family', {}).setdefault(af, {})\
                                        .setdefault('routes', {}).setdefault(route, {})

                route_dict['route'] = route

                if metrics:
                    route_dict['metric'] = int(metrics)
                if route_preference:
                    route_dict['route_preference'] = int(route_preference)

                next_hop_dict = route_dict.setdefault('next_hop', {})

                if not next_hop and interface:
                    intf_dict = next_hop_dict.setdefault('outgoing_interface', {})
                    intf_dict.setdefault(interface, {}).update({'outgoing_interface': interface})

                elif next_hop:
                    idx_dict = next_hop_dict.setdefault('next_hop_list', {}).setdefault(index, {})
                    idx_dict['index'] = index
                    idx_dict['next_hop'] = next_hop

                    if updated:
                        idx_dict['updated'] = updated
                    if interface:
                        idx_dict['outgoing_interface'] = interface

                continue

            #      via 2001:DB8:1:1::2
            #      via 10.4.1.1%default, indirectly connected
            #      via 2001:DB8:4:6::6
            #      via 2001:DB8:20:4:6::6%VRF2
            #      via Null0, receive
            #      via 33.33.33.33%default, Vlan100%default
            m = p6.match(line)
            if m:
                vrf_val = ''
                tmp_next_hop = m.groupdict()['next_hop']
                if tmp_next_hop:
                    if '%' in  tmp_next_hop:
                        next_hop = tmp_next_hop.split('%')[0]
                        vrf_val = tmp_next_hop.split('%')[1]
                    else:
                        next_hop = tmp_next_hop

                if m.groupdict()['interface']:
                    interface = m.groupdict()['interface']

                index += 1
                route_dict = result_dict.setdefault('vrf', {}).setdefault(vrf, {})\
                                        .setdefault('address_family', {}).setdefault(af, {})\
                                        .setdefault('routes', {}).setdefault(route, {})

                route_dict['route'] = route
                route_dict['active'] = active

                next_hop_dict = route_dict.setdefault('next_hop', {})

                if not next_hop and interface:
                    intf_dict = next_hop_dict.setdefault('outgoing_interface', {})
                    intf_dict.setdefault(interface, {}).update({'outgoing_interface': interface})

                elif next_hop:
                    idx_dict = next_hop_dict.setdefault('next_hop_list', {}).setdefault(index, {})
                    idx_dict['index'] = index
                    idx_dict['next_hop'] = next_hop

                    if updated:
                        idx_dict['updated'] = updated
                    if interface:
                        if '%' in interface and '%' in tmp_next_hop:
                            if tmp_next_hop.split('%')[1] == interface.split('%')[1]:
                                idx_dict['outgoing_interface'] = interface.split('%')[0]
                            else:
                                idx_dict['outgoing_interface'] = interface
                        else:
                            idx_dict['outgoing_interface'] = interface
                    if vrf_val:
                        idx_dict['vrf'] = vrf_val

                continue

            # Routing entry for 10.151.0.0/24, 1 known subnets
            # Routing entry for 0.0.0.0/0, supernet
            # Routing entry for 192.168.154.0/24
            m = p100.match(line)
            if m:
                group = m.groupdict()
                entry_dict = result_dict.setdefault('vrf', {}).setdefault(vrf, {}).setdefault('address_family',
                                                                                              {}).setdefault(af, {})
                route_dict = entry_dict.setdefault('routes', {}).setdefault(route, {})
                route_dict.update({'route': group['ip']})
                route_dict.update({'mask': group['mask']})
                route_dict.update({'active': True})
                continue

            # Known via "eigrp 1", distance 130, metric 10880, type internal
            # Known via "rip", distance 120, metric 2
            m = p200.match(line)
            if m:
                group = m.groupdict()
                route_dict.update({'distance': int(group['distance'])})
                route_dict.update({'metric': int(group['metric'])})
                if group['type']:
                    route_dict.update({'type': group['type']})
                continue

            # Redistributing via rip
            # Redistributing via eigrp 1
            m = p300.match(line)
            if m:
                group = m.groupdict()
                route_dict.update({k: v for k, v in group.items() if v})
                continue

            # Last update from 192.168.151.2 on Vlan101, 2w3d ago
            # Last update from 192.168.246.2 on Vlan103, 00:00:12 ago
            m = p400.match(line)
            if m:
                group = m.groupdict()
                update_dict = route_dict.setdefault('update', {})
                update_dict.update({k: v for k, v in group.items() if v})
                continue

            # * 192.168.151.2, from 192.168.151.2, 2w3d ago, via Vlan101
            # * 10.69.1.2
            m = p500.match(line)
            if m:
                group = m.groupdict()
                index += 1
                path_dict = route_dict.setdefault('next_hop',{}).setdefault('next_hop_list', {}).setdefault(index, {})
                path_dict.update({'index': index})
                path_dict.update({'next_hop': group['nexthop']})
                path_dict.update({'age': group['age']})
                path_dict.update({'from': group['from']})
                path_dict.update({'outgoing_interface': group['interface']})
                continue

            # Route metric is 10880, traffic share count is 1
            m = p600.match(line)
            if m:
                group = m.groupdict()
                path_dict.update({k: v for k, v in group.items() if v})

            # Total delay is 20 microseconds, minimum bandwidth is 1000000 Kbit
            m = p700.match(line)
            if m:
                group = m.groupdict()
                path_dict.update({k: v for k, v in group.items() if v})
                continue

            # Reliability 255/255, minimum MTU 1500 bytes
            m = p800.match(line)
            if m:
                group = m.groupdict()
                path_dict.update({k: v for k, v in group.items() if v})
                continue

            # Loading 1/255, Hops 1
            m = p900.match(line)
            if m:
                group = m.groupdict()
                path_dict.update({k: v for k, v in group.items() if v})
                continue

        return result_dict

class ShowIpv6Route(ShowIpRoute):
    """Parser for:
        show ipv6 route
        show ipv6 route vrf <vrf>"""
    parser_command = ['show ipv6 route vrf {vrf}',
                'show ipv6 route vrf {vrf} {protocol}',
               'show ipv6 route', 
               'show ipv6 route {protocol}',
               'show ipv6 route interface {interface}']
    exclude = ['uptime']

    IP_VER = 'ipv6'
    def cli(self, vrf=None, protocol=None, interface=None, output=None):
        
        if output is None:
            if vrf and protocol:
                cmd = self.parser_command[1].format(vrf=vrf, protocol=protocol)
            elif vrf:
                cmd = self.parser_command[0].format(vrf=vrf)
            elif protocol:
                cmd = self.parser_command[3].format(protocol=protocol)
            elif interface:
                cmd = self.parser_command[4].format(interface=interface)
            else:
                cmd = self.parser_command[2]
            out = self.device.execute(cmd)
        else:
            out = output
        if not vrf:
            vrf = 'default'
        return super().cli(vrf=vrf, protocol=protocol, output=out)

# ====================================================
#  schema for show ipv6 route updated
# ====================================================
class ShowIpv6RouteUpdatedSchema(MetaParser):
    """Schema for show ipv6 route updated"""
    schema = {
        'ipv6_unicast_routing_enabled': bool,
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


# ====================================================
#  parser for show ipv6 route updated
# ====================================================
class ShowIpv6RouteUpdated(ShowIpv6RouteUpdatedSchema):
    """Parser for :
       show ipv6 route updated
       show ipv6 route vrf <vrf> updated"""
    exclude = ['updated']

    cli_command = ['show ipv6 route vrf {vrf} updated', 'show ipv6 route updated']

    def cli(self, vrf=None, output=None):
        if output is None:
            if vrf:
                cmd = self.cli_command[0].format(vrf=vrf)
            else:
                cmd = self.cli_command[1]
                vrf = 'default'
            out = self.device.execute(cmd)
        else:
            out = output

        af = 'ipv6'
        route = ""
        next_hop = interface = metrics = route_preference = ""
        source_protocol_dict = {}
        source_protocol_dict['ospf'] = ['O','OI','ON1','ON2','OE1','OE2']
        source_protocol_dict['isis'] = ['IS','I1','I2','IA']
        source_protocol_dict['eigrp'] = ['D','EX']
        source_protocol_dict['static'] = ['S']
        source_protocol_dict['mobile'] = ['M']
        source_protocol_dict['rip'] = ['R']
        source_protocol_dict['lisp'] = ['Ir','Ia','Id']
        source_protocol_dict['nhrp'] = ['H']
        source_protocol_dict['local'] = ['L']
        source_protocol_dict['connected'] = ['C']
        source_protocol_dict['bgp'] = ['B']
        source_protocol_dict['static route'] = ['U']
        source_protocol_dict['home agent'] = ['HA']
        source_protocol_dict['mobile router'] = ['MR']
        source_protocol_dict['nemo'] = ['NM']
        source_protocol_dict['nd'] = ['ND','NDp']
        source_protocol_dict['destination'] = ['DCE']
        source_protocol_dict['redirect'] = ['NDr']

        result_dict = {}
        # IPv6 Routing Table - default - 23 entries
        # IPv6 Routing Table - VRF1 - 104 entries
        p1 = re.compile(r'^\s*IPv6 +Routing +Table +\- +(?P<vrf>[\w]+) +\- +(?P<entries>[\d]+) +entries$')

        # LC  2001:1:1:1::1/128 [0/0]
        p2 = re.compile(r'^\s*(?P<code>[\w]+) +(?P<route>[\w\/\:]+)?'
                        ' +\[(?P<route_preference>[\d\/]+)\]$')

        #   via Loopback0, receive
        #   via 2001:10:1:2::2, GigabitEthernet0/0
        #   via GigabitEthernet0/2, directly connected
        #   via 192.168.51.1%default, indirectly connected
        p3 = re.compile(r'^\s*via( +(?P<next_hop>[0-9][\w\:\.\%]+),?)?'
                        '( +(?P<interface>[\w\.\/\-\_]+[\w\:\.\%]+))?,?( +receive)?( +directly connected)?( +indirectly connected)?$')

        #   via FE80::211:1FF:FE00:1, GigabitEthernet0/0/2.100
        p4 = re.compile(r'^\s*via +(?P<next_hop>[\w\:\.\%]+),'
                        ' +(?P<interface>[\S]+)$')

        #      Last updated 14:15:23 06 December 2017
        p5 = re.compile(r'^\s*Last +updated +(?P<last_updated>[\S\s]+)$')

        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue

            # IPv6 Routing Table - default - 23 entries
            # IPv6 Routing Table - VRF1 - 104 entries
            m = p1.match(line)
            if m:
                vrf = m.groupdict()['vrf']
                continue

            # LC  2001:1:1:1::1/128 [0/0]
            m = p2.match(line)
            if m:
                active = True
                next_hop = interface = ""
                if m.groupdict()['code']:
                    source_protocol_codes = m.groupdict()['code'].strip()

                    for key, val in source_protocol_dict.items():
                        if source_protocol_codes in val:
                            source_protocol = key
                            break
                        else:
                            if 'L' in source_protocol_codes:
                                source_protocol = 'local'
                            # else:
                            #    source_protocol = source_protocol_codes

                if m.groupdict()['route']:
                    route = m.groupdict()['route']

                if m.groupdict()['route_preference']:
                    routepreference = m.groupdict()['route_preference']
                    if '/' in routepreference:
                        route_preference = routepreference.split('/')[0]
                        metrics = routepreference.split('/')[1]
                index = 1

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
                            ['route_preference'] = int(route_preference)
                    if source_protocol_codes:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                            ['source_protocol_codes'] = source_protocol_codes
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                            ['source_protocol'] = source_protocol
                continue

            #   via Loopback0, receive
            #   via 2001:10:1:2::2, GigabitEthernet0/0
            #   via GigabitEthernet0/2, directly connected
            #   via 192.168.51.1%default, indirectly connected
            m = p3.match(line)
            if m:
                if m.groupdict()['next_hop']:
                    if '%' in  m.groupdict()['next_hop']:
                        next_hop = m.groupdict()['next_hop'].split('%')[0]
                    else:
                        next_hop = m.groupdict()['next_hop']

                if m.groupdict()['interface']:
                    interface = m.groupdict()['interface']

                if 'routes' not in result_dict['vrf'][vrf]['address_family'][af]:
                    result_dict['vrf'][vrf]['address_family'][af]['routes'] = {}
                if route not in result_dict['vrf'][vrf]['address_family'][af]['routes']:
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] = {}

                result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['route'] = route


                if 'next_hop' not in result_dict['vrf'][vrf]['address_family'][af]['routes'][route]:
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] = {}

                if not next_hop:
                    if 'outgoing_interface' not in result_dict['vrf'][vrf]['address_family'][af] \
                            ['routes'][route]['next_hop']:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                            ['next_hop']['outgoing_interface'] = {}

                    if m.groupdict()['interface'] and interface not in result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                            ['next_hop']['outgoing_interface']:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                            ['next_hop']['outgoing_interface'][interface] = {}

                    if interface:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                            ['next_hop']['outgoing_interface'][interface]['outgoing_interface'] = interface

                else:
                    if 'next_hop_list' not in result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop']:
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

                    if interface:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                            ['next_hop_list'][index]['outgoing_interface'] = interface

                continue

            #   via FE80::211:1FF:FE00:1, GigabitEthernet0/0/2.100
            m = p4.match(line)
            if m:
                if m.groupdict()['next_hop']:
                    if '%' in m.groupdict()['next_hop']:
                        next_hop = m.groupdict()['next_hop'].split('%')[0]
                    else:
                        next_hop = m.groupdict()['next_hop']

                if m.groupdict()['interface']:
                    interface = m.groupdict()['interface']

                if 'routes' not in result_dict['vrf'][vrf]['address_family'][af]:
                    result_dict['vrf'][vrf]['address_family'][af]['routes'] = {}
                if route not in result_dict['vrf'][vrf]['address_family'][af]['routes']:
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] = {}

                result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['route'] = route

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

                    if interface:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                            ['next_hop_list'][index]['outgoing_interface'] = interface

                continue
            #      Last updated 14:15:23 06 December 2017
            m = p5.match(line)
            if m:

                last_updated = m.groupdict()['last_updated']

                if 'routes' not in result_dict['vrf'][vrf]['address_family'][af]:
                    result_dict['vrf'][vrf]['address_family'][af]['routes'] = {}
                if route not in result_dict['vrf'][vrf]['address_family'][af]['routes']:
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] = {}

                result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['route'] = route


                if 'next_hop' not in result_dict['vrf'][vrf]['address_family'][af]['routes'][route]:
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] = {}


                if not next_hop:
                    if 'outgoing_interface' not in result_dict['vrf'][vrf]['address_family'][af] \
                            ['routes'][route]['next_hop']:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                            ['next_hop']['outgoing_interface'] = {}

                    if interface and interface not in result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                            ['next_hop']['outgoing_interface']:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                            ['next_hop']['outgoing_interface'][interface] = {}

                    if interface:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]\
                        ['next_hop']['outgoing_interface'][interface]['updated'] = last_updated

                else:

                    if 'next_hop_list' not in result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop']:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'][
                            'next_hop_list'] = {}

                    if index not in result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                            ['next_hop_list']:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                            ['next_hop_list'][index] = {}

                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop']\
                        ['next_hop_list'][index]['updated'] = last_updated

                index += 1

                continue

        if len(result_dict):
            result_dict['ipv6_unicast_routing_enabled'] = True
        return result_dict


# ====================================================
#  schema for show ip route <WORD>
# ====================================================
class ShowIpRouteWordSchema(MetaParser):
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
                Optional('net'): str,
                Optional('redist_via'): str,
                Optional('redist_via_tag'): str,
                Optional('sr_incoming_label'): str,
                Optional('tag_name'): str,
                Optional('tag_type'): str,
                Optional('advertised_by'): str,
                Optional('update'): {
                    'from': str,
                    Optional('interface'): str,
                    'age': str
                },
                'paths': {
                    Any(): {
                        Optional('nexthop'): str,
                        Optional('from'): str,
                        Optional('age'): str,
                        Optional('interface'): str,
                        Optional('metric'): str,
                        Optional('share_count'): str,
                        Optional('mpls_label'): str,
                        Optional('mpls_flags'): str,
                        Optional('as_hops'): str,
                        Optional('route_tag'): str,
                        Optional('prefer_non_rib_labels'): bool,
                        Optional('merge_labels'): bool,
                        Optional('repair_path'): {
                            'repair_path': str,
                            'via': str
                        }
                    }
                }
            }
        },
        'total_prefixes': int,
    }


# ====================================================
#  parser for show ip route <WORD>
# ====================================================
class ShowIpRouteWord(ShowIpRouteWordSchema):
    """Parser for :
       show ip route <Hostname or A.B.C.D>
       show ip route vrf <vrf> <Hostname or A.B.C.D>"""
    parser_command = ['show ip route vrf {vrf}',
                'show ip route vrf {vrf} {route}',
                'show ip route', 
                'show ip route {route}',
                'show ip route interface {interface}']
    IP_VER = 'ip'

    def cli(self, route=None, vrf=None, interface=None, output=None):

        if output is None:
            if vrf and route:
                cmd = self.parser_command[1].format(vrf=vrf, route=route)
            elif route:
                cmd = self.parser_command[3].format(route=route)
            elif vrf:
                cmd = self.parser_command[0].format(vrf=vrf)
            elif interface:
                cmd = self.parser_command[4].format(interface=interface)
            else:
                cmd = self.parser_command[2].format()
            out = self.device.execute(cmd)
        else:
            out = output

        if not vrf:
            vrf = 'default'

        # Routing Table: Mgmt-intf
        # Routing Table: test_vrf1
        p0 = re.compile(r'^Routing +Table: +(?P<routing_table>\S+)$')

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

        # Redistributing via rip
        # Redistributing via eigrp 1
        p3 = re.compile(r'^Redistributing +via +(?P<redist_via>\w+) *'
                        r'(?P<redist_via_tag>\d+)?$')

        # Last update from 192.168.151.2 on Vlan101, 2w3d ago
        # Last update from 192.168.246.2 on Vlan103, 00:00:12 ago
        # Last update from 10.101.146.10 2d07h ago
        # Last update from 192.168.0.3 on GigabitEthernet2, 00:00:14 ago
        p4 = re.compile(r'^Last +update +from +(?P<from>[\w\.]+) +(?:on '
                        r'+(?P<interface>[\w\.\/\-]+), )?(?P<age>[ '
                        r'\w\.\:]+) +ago$')

        # 0.0.0.0, from 0.0.0.0, 00:00:00 ago, via GigabitEthernet0/0/0, prefer-non-rib-labels, merge-labels
        # 0.0.0.0, from 0.0.0.0, 00:00:00 ago, via GigabitEthernet0/0/0, merge-labels
        # 0.0.0.0, from 0.0.0.0, 00:00:00 ago, via GigabitEthernet0/0/0
        # * 10.101.146.10, from 10.101.146.10, 2d07h ago
        # * 10.255.207.129
        p5 = re.compile(r'^(?:\* +)?(?P<nexthop>[\w\.]+)(?:, +from +(?P<from>[\w\.]+)?, +'
                        r'(?P<age>[\w\.\:]+) +ago(?:, +via +(?P<interface>\S+))?(?:, +'
                        r'(?P<rib_labels>prefer-non-rib-labels))?(:?, +(?P<merge_labels>merge-labels))?)?$')

        # * directly connected, via GigabitEthernet1.120
        p5_1 = re.compile(r'^\* +directly +connected, via +(?P<interface>\S+)$')
        
        # Route metric is 10880, traffic share count is 1
        p6 = re.compile(r'^Route +metric +is +(?P<metric>\d+), +'
                        r'traffic +share +count +is +(?P<share_count>\d+)$')

        # ipv6 specific
        p7 = re.compile(r'^Route +count +is +(?P<route_count>[\d\/]+), +'
                        r'share +count +(?P<share_count>[\d\/]+)$')

        # FE80::EEBD:1DFF:FE09:56C2, Vlan202
        # FE80::EEBD:1DFF:FE09:56C2
        p8 = re.compile(r'^(?P<fwd_ip>[\w\:]+)(, +(?P<fwd_intf>[\w\.\/\-]+)'
                        r'( indirectly connected)?)?$')
        
        # receive via Loopback4
        p8_1 = re.compile(r'^receive +via +(?P<fwd_intf>[\w\.\/\-]+)$')

        # Last updated 2w4d ago       
        p9 = re.compile(r'^Last +updated +(?P<age>[\w\:\.]+) +ago$')

        # From FE80::EEBD:1DFF:FE09:56C2
        p10 = re.compile(r'^From +(?P<from>[\w\:]+)$')

        # MPLS label: implicit-null
        p11 = re.compile(r'^MPLS +label: +(?P<mpls_label>\S+)$')

        # MPLS Flags: NSF
        p12 = re.compile(r'^MPLS +Flags: +(?P<mpls_flags>\S+)$')

        # SR Incoming Label: 00000
        p13 = re.compile(r'^SR +Incoming +Label: +(?P<sr_incoming_label>\d+)')

        # Repair Path: 0.0.0.0, via GigabitEthernet0
        p14 = re.compile(r'^Repair +Path: +(?P<path>[\d\.]+), +via +(?P<via>\w+)')

        # Tag 65161, type external
        p15 = re.compile(r'^Tag (?P<tag_name>\S+), +type +(?P<tag_type>\S+)$')

        # AS Hops 9
        p16 = re.compile(r'^AS +Hops (?P<num_hops>\d+)$')

        # Route tag 65161
        p17 = re.compile(r'^Route +tag (?P<route_tag>\S+)$')

        # Advertised by eigrp 10 route-map GENIE_STATIC_INTO_EIGRP
        p18 = re.compile(r'^Advertised +by +(?P<advertised_by>[\S ]+)$')

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

            # Tag 65161, type external
            m = p15.match(line)
            if m:
                group = m.groupdict()
                tag_dict = ret_dict.setdefault('entry', {}).setdefault(entry, {})
                tag_dict.update({'tag_name' : group['tag_name']})
                tag_dict.update({'tag_type' : group['tag_type']})

                continue

            # Redistributing via rip
            # Redistributing via eigrp 1
            m = p3.match(line)
            if m:
                group = m.groupdict()
                entry_dict.update({k:v for k,v in group.items() if v})
                continue
            # Last update from 192.168.151.2 on Vlan101, 2w3d ago
            # Last update from 192.168.246.2 on Vlan103, 00:00:12 ago
            # Last update from 10.101.146.10 2d07h ago
            # Last update from 192.168.0.3 on GigabitEthernet2, 00:00:14 ago
            # Last update from 192.168.151.2 on Vlan101, 2w3d ago
            # Last update from 192.168.246.2 on Vlan103, 00:00:12 ago
            # Last update from 10.101.146.10 2d07h ago
            # Last update from 192.168.0.3 on GigabitEthernet2, 00:00:14 ago
            m = p4.match(line)
            if m:
                group = m.groupdict()
                update_dict = entry_dict.setdefault('update', {})
                update_dict.update({k:v for k,v in group.items() if v})
                continue

            # * 192.168.151.2, from 192.168.151.2, 2w3d ago, via Vlan101
            # * 10.69.1.2
            # 0.0.0.0, from 0.0.0.0, 00:00:00 ago, via GigabitEthernet0/0/0, prefer-non-rib-labels, merge-labels
            # 0.0.0.0, from 0.0.0.0, 00:00:00 ago, via GigabitEthernet0/0/0
            # * 10.101.146.10, from 10.101.146.10, 2d07h ago
            m = p5.match(line)
            if m:
                group = m.groupdict()
                index += 1
                path_dict = entry_dict.setdefault('paths', {}).setdefault(index, {})

                if group['nexthop']:
                    path_dict.update({'nexthop': group['nexthop']})
                if group['from']:
                    path_dict.update({'from': group['from']})
                if group['age']:
                    path_dict.update({'age': group['age']})
                if group['interface']:
                    path_dict.update({'interface': group['interface']})

                path_dict.update({'prefer_non_rib_labels': True if group['rib_labels'] else False})
                path_dict.update({'merge_labels': True if group['merge_labels'] else False})
                continue

            # * directly connected, via GigabitEthernet1.120
            m = p5_1.match(line)
            if m:
                group = m.groupdict()
                index += 1
                path_dict = entry_dict.setdefault('paths', {}).setdefault(index, {})
                if group['interface']:
                    path_dict.update({'interface': group['interface']})
                continue

            # AS Hops 9
            m = p16.match(line)
            if m:
                hops_dict = entry_dict.setdefault('paths', {}).setdefault(index, {})
                hops_dict.update({'as_hops' : m.groupdict()['num_hops']})

                continue
            
            # Route tag 65161
            m = p17.match(line)
            if m:
                route_dict = entry_dict.setdefault('paths', {}).setdefault(index, {})
                route_dict.update({'route_tag' : m.groupdict()['route_tag']})

                continue

            # Route metric is 10880, traffic share count is 1
            m = p6.match(line)
            if m:
                group = m.groupdict()
                path_dict = entry_dict.setdefault('paths', {}).setdefault(index, {})
                path_dict.update({k:v for k,v in group.items() if v})
                continue

            # Route count is 1/1, share count 0
            m = p7.match(line)
            if m:
                group = m.groupdict()
                entry_dict.update({k:v for k,v in group.items() if v})
                continue

            # FE80::EEBD:1DFF:FE09:56C2, Vlan202
            # FE80::EEBD:1DFF:FE09:56C2
            m = p8.match(line)
            if m:
                group = m.groupdict()
                index += 1
                path_dict = entry_dict.setdefault('paths', {}).setdefault(index, {})
                path_dict.update({k:v for k,v in group.items() if v})
                continue

            # receive via Loopback4
            m = p8_1.match(line)
            if m:
                group = m.groupdict()
                index += 1
                path_dict = entry_dict.setdefault('paths', {}).setdefault(index, {})
                path_dict.update({k:v for k,v in group.items() if v})
                continue

            # From FE80::EEBD:1DFF:FE09:56C2
            m = p10.match(line)
            if m:
                path_dict['from'] = m.groupdict()['from']
                continue

            # Last updated 2w4d ago
            m = p9.match(line)
            if m:
                path_dict['age'] = m.groupdict()['age']
                continue

            # MPLS label: implicit-null
            m = p11.match(line)
            if m:
                path_dict = entry_dict.setdefault('paths', {}).setdefault(index, {})
                path_dict.update({'mpls_label': m.groupdict()['mpls_label']})
                continue

            # MPLS Flags: NSF
            m = p12.match(line)
            if m:
                path_dict = entry_dict.setdefault('paths', {}).setdefault(index, {})
                path_dict.update({'mpls_flags': m.groupdict()['mpls_flags']})
                continue

            # SR Incoming Label: 00000
            m = p13.match(line)
            if m:
                entry_dict.update({'sr_incoming_label': m.groupdict()['sr_incoming_label']})
                continue

            # Repair Path: 0.0.0.0, via GigabitEthernet0
            m = p14.match(line)
            if m:
                path_dict = entry_dict.setdefault('paths', {}).setdefault(index, {}).setdefault('repair_path', {})
                path_dict.update({'repair_path': m.groupdict()['path']})
                path_dict.update({'via': m.groupdict()['via']})
                continue

            # Advertised by eigrp 10 route-map GENIE_STATIC_INTO_EIGRP
            m18 = p18.match(line)
            if m18:
                entry_dict.update({'advertised_by' : m18.groupdict()['advertised_by']})
                continue

        ret_dict.update({'total_prefixes': index}) if ret_dict else None
        return ret_dict


# ====================================================
#  schema for show ipv6 route <WORD>
# ====================================================
class ShowIpv6RouteWordSchema(MetaParser):
    """Schema for show ipv6 route <WORD>"""
    schema = {
        'entry': {
            Any(): {
                'ip': str,                
                'mask': str,
                'known_via': str,
                'distance': str,
                'metric': str,
                Optional('route_count'): str,
                Optional('share_count'): str,
                Optional('type'): str,
                'paths': {
                    Any(): {
                        Optional('fwd_ip'): str,
                        Optional('fwd_intf'): str,
                        Optional('from'): str,
                        Optional('age'): str
                    }
                }
            }
        },
        'total_prefixes': int,
    }


# ====================================================
#  parser for show ipv6 route <WORD>
# ====================================================
class ShowIpv6RouteWord(ShowIpv6RouteWordSchema, ShowIpRouteWord):
    """Parser for :
       show ipv6 route <Hostname or A.B.C.D>
       show ipv6 route vrf <vrf> <Hostname or A.B.C.D>"""
    parser_command = ['show ipv6 route vrf {vrf}',
                'show ipv6 route vrf {vrf} {route}',
                'show ipv6 route', 
                'show ipv6 route {route}',
                'show ipv6 route interface {interface}']
    IP_VER = 'ipv6'

    def cli(self, route=None, vrf=None, interface=None, output=None):
        
        if output is None:
            if vrf and route:
                cmd = self.parser_command[1].format(vrf=vrf, route=route)
            elif vrf:
                cmd = self.parser_command[0].format(vrf=vrf)
            elif route:
                cmd = self.parser_command[3].format(route=route)
            elif interface:
                cmd = self.parser_command[4].format(interface=interface)
            else:
                cmd = self.parser_command[2]
            out = self.device.execute(cmd)
        else:
            out = output
        if not vrf:
            vrf = 'default'
        return super().cli(route=route, vrf=vrf, output=out)


# ====================================================
#  schema for show ip cef
# ====================================================
class ShowIpCefSchema(MetaParser):
    """Schema for show ip cef
                  show ip cef vrf <vrf>
                  show ip cef <prefix>
                  show ip cef <prefix> detail
                  show ip cef vrf <vrf> <prefix>"""
    schema = {
        'vrf': {
            Any(): {
                'address_family': {
                    Any(): {
                        'prefix': {
                            Any(): {
                                Optional('nexthop'): {
                                    Any(): {
                                        Optional('outgoing_interface'): {
                                            Any(): {
                                                Optional('local_label'): int,
                                                Optional('sid'): str,
                                                Optional('local_sid'): str,
                                                Optional('outgoing_label'): list,
                                                Optional('outgoing_label_backup'): str,
                                                Optional('outgoing_label_info'): str,
                                                Optional('repair'): str,
                                            },
                                        },
                                    },
                                },
                                Optional('epoch'): int,
                                Optional('per_destination_sharing'): bool,
                                Optional('sr_local_label_info'): str,
                                Optional('flags'): list,
                            },
                        },
                    },
                },
            },
        },
    }

# ====================================================
#  parser  for show ip cef <ip>
# ====================================================
class ShowIpCef(ShowIpCefSchema):
    """parser for show ip cef
                  show ip cef vrf <vrf>
                  show ip cef <prefix>
                  show ip cef <prefix> detail
                  show ip cef vrf <vrf> <prefix>"""

    cli_command = ['show ip cef',
                   'show ip cef vrf {vrf}',
                   'show ip cef {prefix}',
                   'show ip cef vrf {vrf} {prefix}']

    def cli(self, vrf="", prefix="", cmd="", output=None):

        if output is None:
            if not cmd:
                if vrf:
                    if prefix:
                        cmd = self.cli_command[3].format(vrf=vrf,prefix=prefix)
                    else:
                        cmd = self.cli_command[1].format(vrf=vrf)
                else:
                    if prefix:
                        cmd = self.cli_command[2].format(prefix=prefix)
                    else:
                        cmd = self.cli_command[0]

            out = self.device.execute(cmd)
        else:
            out = output

        if not vrf:
            vrf = 'default'

        # initial return dictionary
        result_dict = {}

        # 10.169.197.104/30
        # 2001:DB8:1:3::/64
        # 10.16.2.2/32, epoch 2, per-destination sharing
        p1 = re.compile(r'^(?P<prefix>[\w\:\.]+[\/]+[\d]+)'
                        r'(?:, +epoch +(?P<epoch>(\d+)))?'
                        r'(?:, +(?P<sharing>(per-destination sharing)))?$')

        # sr local label info: global/16002 [0x1B]
        p1_1 = re.compile(r'^sr +local +label +info: +(?P<sr_local_label_info>(.*))$')

        #     nexthop 10.169.197.93 TenGigabitEthernet0/2/0 label 22-(local:2043)
        #     nexthop 10.1.2.2 GigabitEthernet2.100
        #     nexthop FE80::A8BB:CCFF:FE03:2101 FastEthernet0/0/0 label 18
        #     nexthop 10.2.3.3 FastEthernet1/0/0 label 17 24
        #     nexthop 10.1.2.2 GigabitEthernet0/1/6 label 16063(elc)-(local:17063)
        #     nexthop 10.169.196.213 GigabitEthernet0/3/6 label 16051-(local:16051) 453955
        p2 = re.compile(r'^nexthop +(?P<nexthop>\S+) +(?P<interface>\S+)'
                        r'( +label +(?P<outgoing_label>[\w\-\ ]+)(\((?P<outgoing_label_info>\w+)\))?'
                        r'(-\(local:(?P<local_label>\w+)\))?)?( +(?P<sid>\d+))?(-\(local:(?P<local_sid>\d+)\))?$')

        # nexthop 10.0.0.5 GigabitEthernet2 label [16002|16002]-(local:16002)
        # nexthop 10.0.0.9 GigabitEthernet3 label [16022|implicit-null]-(local:16022)
        # nexthop 10.0.0.10 GigabitEthernet3 label [16022|16002](elc)-(local:16022)
        # nexthop 10.169.196.213 GigabitEthernet0/1/6 label [16051|16051]-(local:16051) 64588
        # nexthop 10.169.196.213 GigabitEthernet0/3/6 label [16051|16051]-(local:16051) 453955-(local:223555)
        p2_1 = re.compile(r'^nexthop +(?P<nexthop>\S+) +(?P<interface>\S+) +label +\[(?P<outgoing_label>[\S]+)\|'
                          r'(?P<outgoing_label_backup>[\S]+)\](?:\((?P<outgoing_label_info>\w+)\))?'
                          r'\-\(local\:(?P<local_label>(\d+))\)( +(?P<sid>\d+))?(-\(local:(?P<local_sid>\d+)\))?$')

        #     attached to GigabitEthernet3.100
        p3 = re.compile(r'^(?P<nexthop>\w+) +(to|for) +(?P<interface>\S+)$')

        #  no route
        p4 = re.compile(r'^(?P<nexthop>[a-z\ ]+)$')

        # 10.1.2.255/32        receive              GigabitEthernet2.100
        # 10.1.3.0/24          10.1.2.1             GigabitEthernet2.100
        #                      10.2.3.3             GigabitEthernet3.100
        # ::/0, epoch 0, flags [cover, sc, defrt], RIB[S], refcnt 4, per-destination sharing
        p5 = re.compile(r'^((?P<prefix>[\w\:\.]+[\/]+[\d]+) +)?(?P<nexthop>[\w\.]+)( +(?P<interface>[^a-z][\S]+))?$')

        # repair: attached-nexthop 10.0.0.9 GigabitEthernet3
        p6 = re.compile(r'^repair: +(?P<repair>(.*))$')

        # 0.0.0.0/0, epoch 3, flags [default route handler, default route]
        p7 = re.compile(r'(?P<prefix>\S+)\,\s*epoch\s*(?P<epoch>\d+)\,\s*flags\s*\[(?P<flags>[\w\s\,]+)\]')

        for line in out.splitlines():
            line = line.strip()

            # 10.169.197.104/30
            # 2001:DB8:1:3::/64
            # 10.16.2.2/32, epoch 2, per-destination sharing
            m = p1.match(line)
            if m:
                group = m.groupdict()
                if ':' in group['prefix']:
                    address_family = 'ipv6'
                else:
                    address_family = 'ipv4'
                prefix_dict = result_dict.setdefault('vrf',{}).\
                                          setdefault(vrf, {}).\
                                          setdefault('address_family', {}).\
                                          setdefault(address_family,{}).\
                                          setdefault('prefix',{}).\
                                          setdefault(group['prefix'], {})
                if group['epoch']:
                    prefix_dict['epoch'] = int(group['epoch'])
                if group['sharing']:
                    prefix_dict['per_destination_sharing'] = True
                continue

            # sr local label info: global/16002 [0x1B]
            m = p1_1.match(line)
            if m:
                prefix_dict['sr_local_label_info'] = m.groupdict()['sr_local_label_info']
                continue

            #   nexthop 10.169.197.93 TenGigabitEthernet0/2/0 label 22-(local:2043)
            #   nexthop 10.1.2.2 GigabitEthernet2.100
            m = p2.match(line)
            if m:
                group = m.groupdict()
                nexthop_dict = prefix_dict.setdefault('nexthop', {}).\
                                           setdefault(group['nexthop'], {}).\
                                           setdefault('outgoing_interface', {}).\
                                           setdefault(group['interface'], {})

                if group['local_label']:
                    nexthop_dict.update({'local_label': int(group['local_label'])})
                if group['outgoing_label']:
                    nexthop_dict.update({'outgoing_label': group['outgoing_label'].split()})
                if group['outgoing_label_info']:
                    nexthop_dict.update({'outgoing_label_info': group['outgoing_label_info']})
                if group['sid']:
                    nexthop_dict.update({'sid': group['sid']})
                if group['local_sid']:
                    nexthop_dict.update({'local_sid': group['local_sid']})
                continue

            #     nexthop 10.0.0.5 GigabitEthernet2 label [16002|16002]-(local:16002)
            m = p2_1.match(line)
            if m:
                group = m.groupdict()
                nexthop_dict = prefix_dict.setdefault('nexthop', {}).\
                                           setdefault(group['nexthop'], {}).\
                                           setdefault('outgoing_interface', {}).\
                                           setdefault(group['interface'], {})

                nexthop_dict.update({'local_label': int(group['local_label'])})
                nexthop_dict.update({'outgoing_label': group['outgoing_label'].split()})
                nexthop_dict.update({'outgoing_label_backup': group['outgoing_label_backup']})

                if group['outgoing_label_info']:
                    nexthop_dict.update({'outgoing_label_info': group['outgoing_label_info']})
                
                if group.get('sid', None):
                    nexthop_dict.update({'sid': group['sid']})
                if group['local_sid']:
                    nexthop_dict.update({'local_sid': group['local_sid']})
                continue

            # attached to GigabitEthernet3.100
            m = p3.match(line)
            if m:
                group = m.groupdict()
                prefix_dict.setdefault('nexthop', {}). \
                            setdefault(group['nexthop'], {}). \
                            setdefault('outgoing_interface', {}). \
                            setdefault(group['interface'], {})
                continue

            #  no route
            #  discard
            m = p4.match(line)
            if m:
                group = m.groupdict()
                prefix_dict.setdefault('nexthop', {}). \
                            setdefault(group['nexthop'], {})

                continue

            # 10.1.2.255/32        receive              GigabitEthernet2.100
            # 10.1.3.0/24          10.1.2.1             GigabitEthernet2.100
            #                      10.2.3.3             GigabitEthernet3.100
            m = p5.match(line)
            if m:
                group = m.groupdict()
                if group['prefix']:
                    prefix = group['prefix']

                    if ':' in group['prefix']:
                        address_family = 'ipv6'
                    else:
                        address_family = 'ipv4'
                prefix_dict = result_dict.setdefault('vrf', {}). \
                    setdefault(vrf, {}). \
                    setdefault('address_family', {}). \
                    setdefault(address_family, {}). \
                    setdefault('prefix', {}). \
                    setdefault(prefix, {}).\
                    setdefault('nexthop', {}).\
                    setdefault(group['nexthop'], {})
                if group['interface']:
                    prefix_dict.setdefault('outgoing_interface', {}).\
                                setdefault(group['interface'], {})
                continue

            # repair: attached-nexthop 10.0.0.9 GigabitEthernet3
            m = p6.match(line)
            if m:
                nexthop_dict.update({'repair': m.groupdict()['repair']})
                continue

            # 0.0.0.0/0, epoch 3, flags [default route handler, default route]
            m = p7.match(line)
            if m:
                group = m.groupdict()
                prefix = group['prefix']
                epoch = int(group['epoch'])
                flags = group['flags']               

                if ':' in prefix:
                    address_family = 'ipv6'
                else:
                    address_family = 'ipv4'

                prefix_dict = result_dict.setdefault('vrf', {}). \
                    setdefault(vrf, {}). \
                    setdefault('address_family', {}). \
                    setdefault(address_family, {}). \
                    setdefault('prefix', {}). \
                    setdefault(prefix, {})

                prefix_dict['epoch'] = epoch
                prefix_dict['flags'] = list(map(str.strip, flags.split(',')))

                continue

        return result_dict


# ====================================================
#  parser  for show ipv6 cef
# ====================================================
class ShowIpv6Cef(ShowIpCef):
    """parser for show ipv6 cef
                  show ipv6 cef vrf <vrf>
                  show ipv6 cef <prefix>
                  show ipv6 cef vrf <vrf> <prefix>"""

    cli_command = ['show ipv6 cef',
                   'show ipv6 cef vrf {vrf}',
                   'show ipv6 cef {prefix}',
                   'show ipv6 cef vrf {vrf} {prefix}']

    def cli(self, vrf="", prefix="", cmd="", output=None):

        if output is None:
            if vrf:
                if prefix:
                    cmd = self.cli_command[3].format(vrf=vrf,prefix=prefix)
                else:
                    cmd = self.cli_command[1].format(vrf=vrf)
            else:
                if prefix:
                    cmd = self.cli_command[2].format(prefix=prefix)
                else:
                    cmd = self.cli_command[0]
        else:
            output = output

        return super().cli(cmd=cmd, vrf=vrf, prefix=prefix, output=output)


# =========================================
#  Parser for 'show ip cef <prefix> detail'
# =========================================
class ShowIpCefDetail(ShowIpCef):
    ''' Parser for:
        * 'show ip cef <prefix> detail'
    '''

    cli_command = 'show ip cef {prefix} detail'

    def cli(self, prefix, output=None):

        if output is None:
            output = self.device.execute(self.cli_command.format(prefix=prefix))
        else:
            output = output

        return super().cli(prefix=prefix, output=output)


# ====================================================
#  schema for show ip route summary
# ====================================================
class ShowIpRouteSummarySchema(MetaParser):
    """Schema for show ip route summary
                  show ip route vrf <vrf> summary
    """
    schema = {
        'vrf': {
            Any(): {
                'vrf_id': str,
                'maximum_paths': int,
                Optional('removing_queue_size'): int,
                'total_route_source': {
                    'networks': int,
                    'subnets': int,
                    Optional('replicates'): int,
                    'overhead': int,
                    'memory_bytes': int,
                },
                'route_source': {
                    Any(): {
                        Optional('networks'): int,
                        Optional('subnets'): int,
                        Optional('replicates'): int,
                        Optional('overhead'): int,
                        Optional('memory_bytes'): int,
                        Optional('intra_area'): int,
                        Optional('inter_area'): int,
                        Optional('external_1'): int,
                        Optional('external_2'): int,
                        Optional('nssa_external_1'): int,
                        Optional('nssa_external_2'): int,
                        Optional('level_1'): int,
                        Optional('level_2'): int,
                        Optional('external'): int,
                        Optional('internal'): int,
                        Optional('local'): int,
                        Any(): {
                            'networks': int,
                            'subnets': int,
                            Optional('replicates'): int,
                            'overhead': int,
                            'memory_bytes': int,
                            Optional('intra_area'): int,
                            Optional('inter_area'): int,
                            Optional('external_1'): int,
                            Optional('external_2'): int,
                            Optional('nssa_external_1'): int,
                            Optional('nssa_external_2'): int,
                            Optional('level_1'): int,
                            Optional('level_2'): int,
                            Optional('external'): int,
                            Optional('internal'): int,
                            Optional('local'): int,
                        },
                    },
                }
            }
        }
    }


# ====================================================
#  parser for show ip route summary
# ====================================================
class ShowIpRouteSummary(ShowIpRouteSummarySchema):
    """Parser for show ip route summary
                  show ip route vrf <vrf> summary
        """

    cli_command = ['show ip route summary', 'show ip route vrf {vrf} summary']

    def cli(self, vrf='', output=None):
        if output is None:
            if vrf:
                cmd = self.cli_command[1].format(vrf=vrf)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        # IP routing table name is default (0x0)
        # IP routing table name is VRF-1 (0x27)
        # IP routing table name is Default-IP-Routing-Table(0)
        p1 = re.compile(r'^IP +routing +table +name +is +(?P<vrf>\S+) *\((?P<vrf_id>\w+)\)$')
        # IP routing table maximum-paths is 32
        p2 = re.compile(r'^IP +routing +table +maximum-paths +is +(?P<max_path>[\d]+)$')

        # Route Source Networks Subnets Replicates Overhead Memory (bytes)
        # Route Source Networks Subnets Overhead Memory (bytes)
        p3_0 = re.compile(
            r'^(?P<replicates>(Route +Source +Networks +Subnets +Replicates +Overhead +Memory +\(bytes\)))|'
            r'(?P<no_replicates>(Route +Source +Networks +Subnets +Overhead +Memory +\(bytes\)))$'
        )

        # Route Source Networks Subnets Replicates Overhead Memory (bytes)
        # connected 0 68 0 4080 11968
        # static 0 0 0 0 0
        # eigrp 120 0 54 0 4320 9504
        # ospf 100 0 0 0 0 0
        p3 = re.compile(r'^(?P<protocol>\w+)\s(?P<instance>\w+)?\s+(?P<networks>\d+)\s+(?P<subnets>\d+)?\s+'
                        r'(?P<replicates>\d+)?\s+(?P<overhead>\d+)?\s+(?P<memory_bytes>\d+)$')
        
        # Route Source Networks Subnets Overhead Memory (bytes)
        # connected 2 43 9260 6480
        # static 6 58 19508 9216
        # eigrp 1 0 0 0 0
        # ospf 100 101 4344 352008 642124
        p3_1 = re.compile(r'^(?P<protocol>\w+) +(?P<instance>\w+)*? *(?P<networks>\d+) '
                          r'+(?P<subnets>\d+)? +(?P<overhead>\d+)? +(?P<memory_bytes>\d+)$')
        
        # Intra-area: 1 Inter-area: 0 External-1: 0 External-2: 0
        p7 = re.compile(
            r'^Intra-area: +(?P<intra_area>\d+) +Inter-area: +(?P<inter_area>\d+) '
            r'+External-1: +(?P<external_1>\d+) +External-2: +(?P<external_2>\d+)$')
        #   NSSA External-1: 0 NSSA External-2: 0
        p8 = re.compile(
            r'^NSSA +External-1: +(?P<nssa_external_1>\d+) +NSSA +External-2: +('
            r'?P<nssa_external_2>\d+)$')
        #   Level 1: 1 Level 2: 0 Inter-area: 0
        p9_1 = re.compile(
            r'^Level +1: +(?P<level_1>\d+) +Level +2: +(?P<level_2>\d+) +Inter-area: +('
            r'?P<inter_area>\d+)$')
        #   External: 0 Internal: 0 Local: 0
        p13 = re.compile(
            r'^External: +(?P<external>\d+) +Internal: +(?P<internal>\d+) +Local: +(?P<local>\d+)$')

        # Removing Queue Size 0
        p14 = re.compile(r'^Removing +Queue +Size +(?P<q_size>\d+)')

        ret_dict = {}
        replicates_flag = None
        for line in out.splitlines():
            line = line.strip()
            # IP routing table name is default (0x0)
            m = p1.match(line)
            if m:
                vrf = m.groupdict()['vrf']
                vrf_dict = ret_dict.setdefault('vrf',{}).setdefault(vrf, {})
                vrf_dict['vrf_id'] = m.groupdict()['vrf_id']
                vrf_rs_dict = vrf_dict.setdefault('route_source', {})
                continue
            # IP routing table maximum-paths is 32
            m = p2.match(line)
            if m:
                vrf_dict['maximum_paths'] = int(m.groupdict()['max_path'])
                continue

            m = p3_0.match(line)
            if m:
                if m.groupdict()['replicates']:
                    replicates_flag = True
                elif m.groupdict()['no_replicates']:
                    replicates_flag = False

            # application     0           0           0           0           0
            m = p3.match(line)
            if m:
                if replicates_flag:
                    group = m.groupdict()
                    protocol = group.pop('protocol')
                    instance = group.pop('instance')
                    if protocol == 'Total':
                        protocol_dict = vrf_dict.setdefault('total_route_source', {})
                    else:
                        protocol_dict = vrf_rs_dict.setdefault(protocol, {})
                    if instance:
                        inst_dict = protocol_dict.setdefault(instance, {})
                        inst_dict.update({k: int(v) for k, v in group.items() if v})
                    else:
                        group = {k: int(v) for k, v in group.items() if v}
                        protocol_dict.update(group)
                    continue

            m = p3_1.match(line)
            if m:
                if not replicates_flag:
                    group = m.groupdict()
                    protocol = group.pop('protocol')
                    instance = group.pop('instance')
                    if protocol == 'Total':
                        protocol_dict = vrf_dict.setdefault('total_route_source', {})
                    else:
                        protocol_dict = vrf_rs_dict.setdefault(protocol, {})
                    if instance:
                        inst_dict = protocol_dict.setdefault(instance, {})
                        inst_dict.update({k:int(v) for k, v in group.items() if v})
                    else:
                        group = {k: int(v) for k, v in group.items() if v}
                        protocol_dict.update(group)
                    continue

            # Intra-area: 1 Inter-area: 0 External-1: 0 External-2: 0
            m = p7.match(line)
            if m:
                group = {k: int(v) for k, v in m.groupdict().items()}
                vrf_rs_dict.setdefault(protocol, {})
                vrf_rs_dict[protocol][instance].update(group)
                continue
            #   NSSA External-1: 0 NSSA External-2: 0
            m = p8.match(line)
            if m:
                group = {k: int(v) for k, v in m.groupdict().items()}
                vrf_rs_dict.setdefault(protocol, {})
                vrf_rs_dict[protocol][instance].update(group)
                continue

            #   Level 1: 1 Level 2: 0 Inter-area: 0
            m = p9_1.match(line)
            if m:
                group = {k: int(v) for k, v in m.groupdict().items()}
                vrf_rs_dict.setdefault('isis', {})
                # isis can have no area-tag defined
                if instance:
                    vrf_rs_dict['isis'][instance].update(group)
                else:
                    vrf_rs_dict['isis'].update(group)
                continue

            #   External: 0 Internal: 0 Local: 0
            m = p13.match(line)
            if m:
                group = {k: int(v) for k, v in m.groupdict().items()}
                vrf_rs_dict.setdefault('bgp', {})
                vrf_rs_dict['bgp'][instance].update(group)
                continue

            # Removing Queue Size 0
            m = p14.match(line)
            if m:
                vrf_dict.update({'removing_queue_size': int(m.groupdict()['q_size'])})

        return ret_dict


# =========================================
#  Parser for 'show ip cef internal'
# =========================================
class ShowIpCefInternalSchema(MetaParser):
    """Schema for show ip cef internal
                  show ip cef <ip> internal"""
    schema = {
        'vrf': {
            Any(): {
                'address_family': {
                    Any(): {
                        'prefix': {
                            Any(): {
                                Optional('epoch'): int,
                                Optional('sharing'): str,
                                Optional('rib'): str,
                                Optional('refcnt'): int,
                                Optional('feature_space'): {
                                    Optional('iprm'): str,
                                    Optional('broker'): {
                                      'distribution_priority': int,
                                    },
                                    Optional('lfd'): {
                                        Any(): {
                                            'local_labels': int,
                                        }
                                    },
                                    Optional('local_label_info'): {
                                      Optional('dflt'): str,
                                      Optional('sr'): str,
                                    },
                                    Optional('path_extension_list'): {
                                        'dflt': {
                                            'disposition_chain': {
                                                Any(): {
                                                    Optional('label'): int,
                                                    Optional('frr'): {
                                                        'primary': {
                                                            'primary': {
                                                                'tag_adj': {
                                                                    Any(): {
                                                                        'addr': str,
                                                                    }
                                                                }
                                                            },
                                                        }
                                                    }
                                                }
                                            },
                                            Optional('label_switch_chain'): {
                                                Any(): {
                                                    Optional('label'): int,
                                                    Optional('frr'): {
                                                        'primary': {
                                                            'primary': {
                                                                'tag_adj': {
                                                                    Any(): {
                                                                        'addr': str,
                                                                    }
                                                                }
                                                            },
                                                        }
                                                    }
                                                }
                                            }
                                        },
                                        Optional('sr'): {
                                            'disposition_chain': {
                                                Any(): {
                                                    Optional('label'): int,
                                                    Optional('frr'): {
                                                        'primary': {
                                                            'primary': {
                                                                'tag_adj': {
                                                                    Any(): {
                                                                        'addr': str,
                                                                    }
                                                                }
                                                            },
                                                        }
                                                    }
                                                }
                                            },
                                            Optional('label_switch_chain'): {
                                                Any(): {
                                                    Optional('label'): int,
                                                    Optional('frr'): {
                                                        'primary': {
                                                            'primary': {
                                                                'tag_adj': {
                                                                    Any(): {
                                                                        'addr': str,
                                                                    }
                                                                }
                                                            },
                                                        }
                                                    }
                                                }
                                            }
                                        },
                                    },
                                },
                                Optional('subblocks'): {
                                  Any(): {
                                      'rr_source': list,
                                      'non_eos_chain_loadinfo': str,
                                      'per-session': bool,
                                      'flags': str,
                                      'locks': int,
                                  }
                                },
                                Optional('ifnums'): {
                                    Any(): {
                                        'ifnum': int,
                                        Optional('address'): str,
                                    }
                                },
                                Optional('flags'): list,
                                Optional('sources'): list,
                                Optional('path_list'): {
                                    Any(): {
                                        'sharing': str,
                                        'flags': str,
                                        'locks': int,
                                        'path': {
                                            Any(): {
                                                Optional('share'): str,
                                                Optional('type'): str,
                                                Optional('for'): str,
                                                Optional('flags'): str,
                                                Optional('nexthop'): {
                                                    Any(): {
                                                        Optional('outgoing_interface'): {
                                                            Any(): {
                                                                Optional('local_label'): int,
                                                                Optional('outgoing_label'): list,
                                                                Optional('outgoing_label_backup'): str,
                                                                Optional('outgoing_label_info'): str,
                                                                Optional('repair'): str,
                                                                Optional('ip_adj'): {
                                                                    Any(): {
                                                                        Optional('addr'): str,
                                                                        Optional('addr_info'): str,
                                                                    }
                                                                }
                                                            },
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                                'output_chain': {
                                    Optional('label'): list,
                                    Optional('tag_midchain'): {
                                        Any(): { # tag_midchain_dict
                                            'tag_midchain_info': str,
                                            'label': list,
                                            Optional('frr'): { # frr_dict
                                                'primary': { # frr_primary_dict
                                                    'info': str,
                                                    'primary': {
                                                        Optional('tag_adj'): {
                                                            Any(): {
                                                                'addr': str,
                                                                'addr_info': str,
                                                            }
                                                        }
                                                    },
                                                    'repair': {
                                                        Optional('tag_midchain'): {
                                                            'interface': str,
                                                        },
                                                        Optional('label'): list,
                                                        Optional('tag_adj'): {
                                                            Any(): {
                                                                'addr': str,
                                                                'addr_info': str,
                                                            }
                                                        },
                                                    },
                                                }
                                            },
                                        }
                                    },
                                    Optional('frr'): {
                                        'primary': {
                                            Optional('info'): str,
                                            'primary': {
                                                Optional('tag_adj'): {
                                                    Any(): {
                                                        'addr': str,
                                                        'addr_info': str,
                                                    }
                                                }
                                            },
                                            Optional('repair'): {
                                                Optional('tag_midchain'): {
                                                    Any(): {
                                                        Optional('tag_midchain_info'): str,
                                                        Optional('label'): list,
                                                        Optional('tag_adj'): {
                                                            Any(): {
                                                                'addr': str,
                                                                'addr_info': str,
                                                            }
                                                        },
                                                    }
                                                },
                                                Optional('tag_adj'): {
                                                    Any(): {
                                                        'addr': str,
                                                        'addr_info': str,
                                                    },
                                                },
                                            },
                                        }
                                    },
                                    Optional('tag_adj'): {
                                        Any(): {
                                            'addr': str,
                                            'addr_info': str,
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


class ShowIpCefInternal(ShowIpCefInternalSchema):
    ''' Parser for:
        * 'show ip cef internal'
        * 'show ip cef <prefix> internal'
        * 'show ip cef vrf <vrf> <prefix> internal'
    '''

    cli_command = ['show ip cef {ip} internal',
                   'show ip cef internal',
                   'show ip cef vrf {vrf} {ip} internal']

    def cli(self, ip="", vrf="", output=None):

        if output is None:
            if ip and vrf:
                cmd = self.cli_command[2].format(ip=ip, vrf=vrf)
            elif ip:
                cmd = self.cli_command[0].format(ip=ip)
            else:
                cmd = self.cli_command[1]
            out = self.device.execute(cmd)
        else:
            out = output

        if not vrf:
            vrf = 'default'

        result_dict = {}

        # 10.19.198.239/32, epoch 2, RIB[I], refcnt 7, per-destination sharing
        # 0.0.0.0/8, epoch 2, refcnt 6, per-destination sharing
        p1 = re.compile(r'^(?P<prefix>[\w:.\/d]+), +epoch '
                        r'+(?P<epoch>\d+),(?: +RIB(?P<rib>\S+),)? '
                        r'+refcnt +(?P<refcnt>\d+), +(?P<sharing>\S+) sharing$')

        # 10.4.1.1/32, epoch 2, flags [att, cnn, rcv, local, SrcElgbl], RIB[C], refcnt 6, per-destination sharing
        # 10.4.1.1/32, epoch 2, flags [att, cnn, rcv, local, SrcElgbl], intf-rcv, RIB[C], refcnt 6, per-destination sharing
        # 0.0.0.0/0, epoch 2, flags [DefRtHndlr, defrt], refcnt 5, per-destination sharing
        # 10.19.198.239/32, epoch 2, RIB[I], refcnt 7, per-packet sharing
        p1_1 = re.compile(r'^(?P<prefix>[\w:./d]+), +epoch +(?P<epoch>\d+), '
                          r'+flags +\[(?P<flags>[a-zA-Z, ]+)\],(?:(?: +intf-rcv,)? '
                          r'+RIB+(?P<rib>\S+),)? +refcnt +(?P<refcnt>\d+), '
                          r'+(?P<sharing>\S+) sharing$')

        #   sources: RIB, RR, LTE
        p2 = re.compile(r'^sources: +(?P<sources>[a-zA-Z, ]+)$')

        # dflt local label info: global/28 [0x3]
        # sr local label info: global/16073 [0x1B]
        p3 = re.compile(r'^(?P<local_label>dflt|sr) +local +label +info: +(?P<info>(.*))$')

        # path list 7F0FEC884768, 19 locks, per-destination, flags 0x4D [shble, hvsh, rif, hwcn]
        p5 = re.compile(r'^path +list +(?P<path_list_id>[A-Z0-9]+), '
                        r'+(?P<locks>\d+) +locks, +(?P<sharing>per-destination),'
                        r' +flags +(?P<flags>[\S\s]+)$')

        # path 7F0FF11E0AE0, share 1/1, type attached nexthop, for IPv4, flags [has-rpr]
        p6 = re.compile(r'path +(?P<path_id>[A-Z0-9]+), share +(?P<share>\S+), +type '
                        r'+(?P<type>[\w\s]+), +for +(?P<for>[\w\d\-\s]+)(?:, flags +(?P<flags>\S+))?')

        # nexthop 10.169.196.213 GigabitEthernet0/1/6 label [51885|16073]-(local:28), IP adj out of GigabitEthernet0/1/6, addr 10.169.196.213 7F0FF08D4900
        p7 = re.compile(r'^nexthop +(?P<nexthop>\S+) +(?P<interface>\S+) +label '
                        r'+\[(?P<outgoing_label>[\S]+)\|(?P<outgoing_label_backup>[\S]+)\]'
                        r'(?:\((?P<outgoing_label_info>\w+)\))?\-\(local\:(?P<local_label>(\d+))\)'
                        r'(?:, +(?P<ip_adj>IP adj) +out +of +(?P<interface2>\S+), +addr +(?P<addr>\S+) '
                        r'+(?P<addr_info>\S+))?(.*)$')

        # nexthop 10.169.14.241 MPLS-SR-Tunnel1 label 16073-(local:16073), repair, IP midchain out of MPLS-SR-Tunnel1 7F0FF0AFAE98
        p7_1 = re.compile(r'^nexthop +(?P<nexthop>\S+) +(?P<interface>\S+)'
                          r'( +label +(?P<outgoing_label>[\w\-\ ]+)(\((?P<outgoing_label_info>\w+)\))?'
                          r'(-\(local:(?P<local_label>\w+)\))?)?,.*$')

        # FRR Primary (0x80007F0FF094DD88)
        p8_0 = re.compile(r'^FRR +Primary +\((?P<info>\S+)\)$')

        # TAG midchain out of Tunnel65537 7F4F881C0718
        p8_1 = re.compile(r'^TAG +midchain +out +of +(?P<tunnel>[a-zA-Z\d]+) +(?P<info>[A-Z\d]+)$')

        # TAG adj out of GigabitEthernet0/1/7, addr 10.19.198.29 7F9C9D304A90
        p8_2 = re.compile(r'^TAG +adj +out +of +(?P<interface>\S+), +addr '
                          r'+(?P<addr>\S+)(?: +(?P<addr_info>[A-Z\d]+))?$')

        # <primary: TAG adj out of GigabitEthernet0/1/6, addr 10.169.196.213 7F0FF08D46D0>
        # <primary: TAG adj out of GigabitEthernet0/1/6, addr 10.19.198.25>
        p8 = re.compile(r'^<primary: +TAG +adj +out +of +(?P<interface>\S+), '
                        r'addr +(?P<addr>[\d.]+)(?: +(?P<addr_info>[A-Z\d]+))?>$')

        # TAG adj out of GigabitEthernet0/1/7, addr 10.169.196.217 7F0FF0AFB2F8>
        # <repair:  TAG adj out of GigabitEthernet0/1/7, addr 10.19.198.29 7F2B21B24148>
        p9 = re.compile(r'^(?:<repair: +)?TAG +adj +out +of +(?P<interface>[a-zA-Z\d\/]+), '
                        r'+addr +(?P<addr>[\d.]+) +(?P<addr_info>[A-Z\d]+)>$')

        # <repair:  TAG midchain out of MPLS-SR-Tunnel1 7F0FF0AFAC68
        p9_1 = re.compile(r'^<repair: +TAG +midchain +out +of '
                          r'+(?P<interface>[a-zA-Z\d\/-]+) +(?P<addr_info>[A-Z\d]+)$')

        # label 98
        # label implicit-null
        # label [16073|16073]
        # label [51885|16073]-(local:28)
        # label none
        p10 = re.compile(r'^label +(?P<label>.*)$')

        # <repair:  label 16061
        p11 = re.compile(r'<repair: +label +(?P<label>.*)')

        # IPRM: 0x00018000
        p12 = re.compile(r'^IPRM: +(?P<iprm>\S+)$')

        # Broker: linked, distributed at 2nd priority
        p13 = re.compile(r'^Broker: +(?P<status>\w+), +distributed +at '
                         r'+(?P<priority>\d+).* +priority$')

        # LFD: 10.13.110.0/24 0 local labels
        p14 = re.compile(r'^LFD: +(?P<address>\S+) +(?P<labels>\d+) +local +labels$')

        # dflt disposition chain 0x7F0FF19606C0
        # sr disposition chain 0x7F0FF1960590
        # dflt label switch chain 0x7F0FF19606C0
        # sr label switch chain 0x7F0FF1960590
        p15 = re.compile(r'^(?P<type>dflt|sr) +(?P<chain_type>label '
                         r'+switch|disposition) +chain +(?P<id>\S+)$')

        # GigabitEthernet0/1/6(15): 10.169.196.213
        # MPLS-SR-Tunnel1(29)
        p16 = re.compile(r'^(?P<interface>[\w\/-]+)\((?P<ifnum>\d+)\)'
                         r'(?:\: +(?P<addr>[\d.]+))?$')

        # 1 RR source [non-eos indirection, heavily shared]
        p17 = re.compile(r'^(?P<counts>\d+) +RR +source +\[(?P<rr_source>[\s\S]+)\]$')

        # non-eos chain loadinfo 7F0FF16E6F38, per-session, flags 0111, 8 locks
        p18 = re.compile(r'^non-eos +chain +loadinfo +(?P<non_eos_chain_loadinfo>\S+),'
                         r' +(?P<per_session>per-session), +flags +(?P<flags>\S+), '
                         r'+(?P<locks>\d+) +locks$')

        label_list = []
        label_list2 = []
        for line in out.splitlines():
            line = line.strip()

            # 10.19.198.239/32, epoch 2, RIB[I], refcnt 7, per-destination sharing
            # 0.0.0.0/8, epoch 2, refcnt 6, per-destination sharing
            m1 = p1.match(line)

            # 10.4.1.1/32, epoch 2, flags [att, cnn, rcv, local, SrcElgbl], RIB[C], refcnt 6, per-destination sharing
            # 10.4.1.1/32, epoch 2, flags [att, cnn, rcv, local, SrcElgbl], intf-rcv, RIB[C], refcnt 6, per-destination sharing
            # 0.0.0.0/0, epoch 2, flags [DefRtHndlr, defrt], refcnt 5, per-destination sharing
            m1_1 = p1_1.match(line)
            if m1 or m1_1:
                if m1:
                    group = m1.groupdict()
                elif m1_1:
                    group = m1_1.groupdict()

                if ':' in group['prefix']:
                    address_family = 'ipv6'
                else:
                    address_family = 'ipv4'

                prefix_dict = result_dict.setdefault('vrf', {}). \
                    setdefault(vrf, {}). \
                    setdefault('address_family', {}). \
                    setdefault(address_family, {}). \
                    setdefault('prefix', {}). \
                    setdefault(group['prefix'], {})
                output_chain_dict = prefix_dict.setdefault('output_chain', {})
                if group['epoch']:
                    prefix_dict['epoch'] = int(group['epoch'])
                if group['sharing']:
                    prefix_dict['sharing'] = group['sharing']
                if 'rib' in group and group['rib']:
                    prefix_dict['rib'] = group['rib']
                if 'refcnt' in group and group['refcnt']:
                    prefix_dict['refcnt'] = int(group['refcnt'])
                if 'flags' in group and group['flags']:
                    prefix_dict['flags'] = group['flags'].split(', ')

                continue

            #   sources: RIB, RR, LTE
            m2 = p2.match(line)
            if m2:
                prefix_dict['sources'] = m2.groupdict()['sources'].split()

                continue

            # IPRM: 0x00028000
            m = p12.match(line)
            if m:
                group = m.groupdict()
                feature_space_dict = prefix_dict.setdefault('feature_space', {})
                feature_space_dict['iprm'] = group['iprm']

                continue

            # Broker: linked, distributed at 1st priority
            m = p13.match(line)
            if m:
                group = m.groupdict()
                if 'feature_space_dict' not in prefix_dict:
                    feature_space_dict = prefix_dict.setdefault('feature_space', {})
                broker_dict = feature_space_dict.setdefault('broker', {})
                if group['priority']:
                    broker_dict['distribution_priority'] = int(group['priority'])
                continue

            # LFD: 10.13.110.0/24 0 local labels
            m = p14.match(line)
            if m:
                group = m.groupdict()
                lfd_dict = feature_space_dict.setdefault('lfd', {})
                lfd_dict.setdefault(group['address'], {}). \
                         setdefault('local_labels', int(group['labels']))
                continue

            # dflt local label info: global/28 [0x3]
            # sr local label info: global/16073 [0x1B]
            m3 = p3.match(line)
            if m3:
                group = m3.groupdict()
                local_label_info_dict = feature_space_dict.setdefault('local_label_info', {})
                local_label_info_dict[group['local_label']] = group['info']

                continue

            # dflt disposition chain 0x7F0FF19606C0
            # sr disposition chain 0x7F0FF1960590
            # dflt label switch chain 0x7F0FF19606C0
            # sr label switch chain 0x7F0FF1960590
            m = p15.match(line)
            if m:
                group = m.groupdict()
                if group['type'] == 'dflt' and group['chain_type'] == 'label switch':
                    dft_lb_dict = feature_space_dict.setdefault('path_extension_list', {}). \
                                              setdefault('dflt', {}). \
                                              setdefault('label_switch_chain', {}). \
                                              setdefault(group['id'], {})
                elif group['type'] == 'dflt' and group['chain_type'] == 'disposition':
                    dft_dp_dict = feature_space_dict.setdefault('path_extension_list', {}). \
                                              setdefault('dflt', {}). \
                                              setdefault('disposition_chain', {}). \
                                              setdefault(group['id'], {})

                if group['type'] == 'sr' and group['chain_type'] == 'label switch':
                    sr_lb_dict = feature_space_dict.setdefault('path_extension_list', {}). \
                                              setdefault('sr', {}). \
                                              setdefault('label_switch_chain', {}). \
                                              setdefault(group['id'], {})
                elif group['type'] == 'sr' and group['chain_type'] == 'disposition':
                    sr_dp_dict = feature_space_dict.setdefault('path_extension_list', {}). \
                                              setdefault('sr', {}). \
                                              setdefault('disposition_chain', {}). \
                                              setdefault(group['id'], {})
                continue

            # GigabitEthernet0/1/6(15): 10.169.196.213
            # MPLS-SR-Tunnel1(29)
            m = p16.match(line)
            if m:
                group = m.groupdict()
                ifnum_dict = prefix_dict.setdefault('ifnums', {}). \
                                setdefault(group['interface'], {})
                ifnum_dict['ifnum'] = int(group['ifnum'])
                if group['addr']:
                    ifnum_dict.setdefault('address', group['addr'])

                continue

            # 1 RR source [non-eos indirection, heavily shared]
            m = p17.match(line)
            if m:
                group = m.groupdict()
                rr_dict = prefix_dict.setdefault('subblocks', {}).setdefault(int(group['counts']), {})
                rr_dict['rr_source'] = group['rr_source'].split(', ')
                continue

            # non-eos chain loadinfo 7F0FF16E6F38, per-session, flags 0111, 8 locks
            m = p18.match(line)
            if m:
                group = m.groupdict()
                if group['per_session'] == 'per-session':
                    rr_dict['per-session'] = True
                else:
                    rr_dict['per-session'] = False
                for i in ['non_eos_chain_loadinfo', 'flags', 'locks']:
                    rr_dict[i] = int(group[i]) if i == 'locks' else group[i]
                continue

            # path list 7F0FEC884768, 19 locks, per-destination, flags 0x4D [shble, hvsh, rif, hwcn]
            m5 = p5.match(line)
            if m5:
                group = m5.groupdict()
                pathlist_dict = prefix_dict.setdefault('path_list', {}). \
                    setdefault(group['path_list_id'], {})
                if group['locks']:
                    pathlist_dict['locks'] = int(group['locks'])
                if group['sharing']:
                    pathlist_dict['sharing'] = group['sharing']
                if group['flags']:
                    pathlist_dict['flags'] = group['flags']

                continue

            # path 7F0FF11E0AE0, share 1/1, type attached nexthop, for IPv4, flags [has-rpr]
            m6 = p6.match(line)
            if m6:
                group = m6.groupdict()
                path_dict = pathlist_dict.setdefault('path', {}). \
                    setdefault(group['path_id'], {})
                for i in ['share', 'type', 'for', 'flags']:
                    if group[i]:
                        path_dict[i] = group[i]

                continue

            # nexthop 10.169.196.213 GigabitEthernet0/1/6 label [51885|16073]-(local:28), IP adj out of GigabitEthernet0/1/6, addr 10.169.196.213 7F0FF08D4900
            m7 = p7.match(line)
            # nexthop 10.169.14.241 MPLS-SR-Tunnel1 label 16073-(local:16073), repair, IP midchain out of MPLS-SR-Tunnel1 7F0FF0AFAE98
            m7_1 = p7_1.match(line)
            if m7 or m7_1:
                if m7:
                    group = m7.groupdict()
                elif m7_1:
                    group = m7_1.groupdict()
                nexthop_dict = path_dict.setdefault('nexthop', {}). \
                    setdefault(group['nexthop'], {}). \
                    setdefault('outgoing_interface', {}). \
                    setdefault(group['interface'], {})

                if group['local_label']:
                    nexthop_dict['local_label'] = int(group['local_label'])

                if 'outgoing_label' in group and group['outgoing_label']:
                    nexthop_dict['outgoing_label'] = group['outgoing_label'].split()

                for i in ['outgoing_label_backup', 'outgoing_label_info']:
                    if i in group and group[i]:
                        nexthop_dict[i] = group[i]

                if 'ip_adj' in group and group['ip_adj']:
                    ip_adj_dict = nexthop_dict.setdefault('ip_adj', {}).setdefault(group['interface2'], {})
                    ip_adj_dict['addr'] = group['addr']
                    ip_adj_dict['addr_info'] = group['addr_info']

                continue

            # FRR Primary (0x80007F0FF094DD88)
            m8_0 = p8_0.match(line)
            if m8_0:
                group = m8_0.groupdict()
                empty_dict = {}
                frr_dict = empty_dict.setdefault('frr', {})
                frr_primary_dict = frr_dict.setdefault('primary', {})
                frr_primary_dict['info'] = group['info']

                if 'tag_midchain' in output_chain_dict:
                    tag_midchain_dict.setdefault('frr', frr_dict)
                else:
                    output_chain_dict.setdefault('frr', frr_dict)

                continue

            # TAG midchain out of Tunnel65537 7F4F881C0718
            m8_1 = p8_1.match(line)
            if m8_1:
                group = m8_1.groupdict()
                if 'output_chain' in prefix_dict:
                    tag_midchain_dict = output_chain_dict.setdefault('tag_midchain', {}). \
                        setdefault(group['tunnel'], {})
                    tag_midchain_dict['tag_midchain_info'] = group['info']
                continue

            # TAG adj out of GigabitEthernet0/1/7, addr 10.19.198.29 7F9C9D304A90
            m8_2 = p8_2.match(line)
            if m8_2:
                group = m8_2.groupdict()
                tag_adj_dict = output_chain_dict.setdefault('tag_adj', {}). \
                                                 setdefault(group['interface'], {})

                tag_adj_dict['addr'] = group['addr']
                if group['addr_info']:
                    tag_adj_dict['addr_info'] = group['addr_info']
                continue

            # <primary: TAG adj out of GigabitEthernet0/1/6, addr 10.169.196.213 7F0FF08D46D0>
            m8 = p8.match(line)
            if m8:
                group = m8.groupdict()

                if 'path_list' in prefix_dict:
                    if 'tag_midchain' in output_chain_dict:
                        primary_dict = tag_midchain_dict['frr']['primary'].setdefault('primary', {}). \
                                                    setdefault('tag_adj', {}). \
                                                    setdefault(group['interface'], {})
                    else:

                        primary_dict = output_chain_dict.setdefault('frr', {}). \
                                                    setdefault('primary', {}). \
                                                    setdefault('primary', {}). \
                                                    setdefault('tag_adj', {}). \
                                                    setdefault(group['interface'], {})

                    primary_dict['addr'] = group['addr']
                    primary_dict['addr_info'] = group['addr_info']
                elif 'path_extension_list' in feature_space_dict:

                    path_ext_frr_dict = {}
                    path_ext_frr_dict.setdefault('tag_adj', {}). \
                                      setdefault(group['interface'], {'addr': group['addr']})

                    if 'sr' in feature_space_dict['path_extension_list']:
                        if 'label_switch_chain' in feature_space_dict['path_extension_list']['sr']:
                            sr_lb_dict.setdefault('frr', {}).\
                                setdefault('primary', {}).setdefault('primary', path_ext_frr_dict)
                        elif 'disposition_chain' in feature_space_dict['path_extension_list']['sr']:
                            sr_dp_dict.setdefault('frr', {}).\
                                setdefault('primary', {}).setdefault('primary', path_ext_frr_dict)

                    elif 'dflt' in feature_space_dict['path_extension_list']:
                        if 'label_switch_chain' in feature_space_dict['path_extension_list']['dflt']:
                            dft_lb_dict.setdefault('frr', {}).\
                                setdefault('primary', {}).setdefault('primary', path_ext_frr_dict)
                        elif 'disposition_chain' in feature_space_dict['path_extension_list']['dflt']:
                            dft_dp_dict.setdefault('frr', {}).\
                                setdefault('primary', {}).setdefault('primary', path_ext_frr_dict)
                continue

            # TAG adj out of GigabitEthernet0/1/7, addr 10.169.196.217 7F0FF0AFB2F8>
            # <repair:  TAG adj out of GigabitEthernet0/1/7, addr 10.19.198.29 7F2B21B24148>
            m9 = p9.match(line)
            if m9:
                group = m9.groupdict()
                if 'output_chain' in prefix_dict:
                    if 'tag_midchain' in output_chain_dict:
                        repair_adj_dict = tag_midchain_dict['frr']['primary'].setdefault('repair', {}). \
                                                       setdefault('tag_adj', {}). \
                                                       setdefault(group['interface'], {})
                    elif 'frr' in output_chain_dict:
                        if 'repair' in output_chain_dict['frr']['primary']:
                            if 'tag_midchain' in output_chain_dict['frr']['primary']['repair']:
                                temp_tag_dict = output_chain_dict['frr']['primary']['repair']['tag_midchain']
                                temp_key = list(temp_tag_dict.keys())[0]
                                repair_adj_dict = output_chain_dict['frr']['primary']['repair']['tag_midchain'][temp_key]. \
                                    setdefault('tag_adj', {}). \
                                    setdefault(group['interface'], {})
                        else:
                            repair_adj_dict = output_chain_dict['frr']['primary'].setdefault('repair', {}). \
                                setdefault('tag_adj', {}). \
                                setdefault(group['interface'], {})

                    repair_adj_dict['addr'] = group['addr']
                    repair_adj_dict['addr_info'] = group['addr_info']

                continue

            # <repair:  TAG midchain out of MPLS-SR-Tunnel1 7F0FF0AFAC68
            m9_1 = p9_1.match(line)
            if m9_1:
                group = m9_1.groupdict()
                if 'output_chain' in prefix_dict:
                    if 'tag_midchain' in output_chain_dict:
                        repair_mid_dict = tag_midchain_dict['frr']['primary'].setdefault('repair', {}). \
                            setdefault('tag_midchain', {}).setdefault(group['interface'], {})

                    else:
                        repair_mid_dict = output_chain_dict['frr']['primary'].setdefault('repair', {}). \
                            setdefault('tag_midchain', {}).setdefault(group['interface'], {})

                    repair_mid_dict['tag_midchain_info'] = group['addr_info']

                continue

            # label 98
            # label implicit-null
            # label [16073|16073]
            # label [51885|16073]-(local:28)
            m10 = p10.match(line)

            if m10:
                label_val = m10.groupdict()['label']
                if label_val == 'none':
                    continue

                if 'path_list' in prefix_dict:
                    if 'tag_midchain' in output_chain_dict:

                        if 'frr' in tag_midchain_dict:
                            temp_tag_dict = tag_midchain_dict['frr']['primary']['repair']['tag_adj']
                            temp_key = list(temp_tag_dict.keys())[0]
                            tag_midchain_dict['frr']['primary']['repair']['tag_adj'][temp_key]['label'] = label_val.split()

                        else:
                            for i in label_val.split():
                                label_list2.append(i)
                            tag_midchain_dict['label'] = label_list2

                    elif 'frr' in output_chain_dict and 'repair' in output_chain_dict['frr']['primary']:
                        temp_tag_dict = output_chain_dict['frr']['primary']['repair']['tag_midchain']
                        temp_key = list(temp_tag_dict.keys())[0]
                        output_chain_dict['frr']['primary']['repair']['tag_midchain'][temp_key]['label'] = label_val.split()

                    else:
                        for i in label_val.split():
                            label_list.append(i)
                        output_chain_dict['label'] = label_list

                elif 'path_extension_list' in feature_space_dict:
                    if 'sr' in feature_space_dict['path_extension_list']:
                        if 'label_switch_chain' in feature_space_dict['path_extension_list']['sr']:
                            sr_lb_dict['label'] = int(label_val)
                        elif 'disposition_chain' in feature_space_dict['path_extension_list']['sr']:
                            sr_dp_dict['label'] = int(label_val)
                    elif 'dflt' in feature_space_dict['path_extension_list']:
                        if 'label_switch_chain' in feature_space_dict['path_extension_list']['dflt']:
                            dft_lb_dict['label'] = int(label_val)
                        elif 'disposition_chain' in feature_space_dict['path_extension_list']['dflt']:
                            dft_dp_dict['label'] = int(label_val)
                continue

            # <repair:  label 16061
            m11 = p11.match(line)
            if m11:
                label_val = m11.groupdict()['label']
                if 'tag_midchain' in output_chain_dict:
                    if 'frr' in tag_midchain_dict:
                        temp_tag_dict = tag_midchain_dict['frr']['primary'].setdefault('repair', {})
                        temp_tag_dict['label'] = label_val.split()
                continue

        return result_dict

# ====================================================
#  schema for show ipv6 route summary
# ====================================================
class ShowIpv6RouteSummarySchema(MetaParser):
    """Schema for show ipv6 route summary
                  show ipv6 route vrf <vrf> summary
    """
    schema = {
        'vrf': {
            Any(): {
                'vrf_id': str,
                'maximum_paths': int,
                'total_route_source': {
                    'networks': int,
                    'overhead': int,
                    'memory_bytes': int,
                },
                'number_of_prefixes': {
                    'prefix_8': int,
                    'prefix_64': int,
                    'prefix_128': int,
                },
                'route_source': {
                    Any(): {
                        Optional('networks'): int,
                        Optional('overhead'): int,
                        Optional('memory_bytes'): int,
                        Optional('intra_area'): int,
                        Optional('inter_area'): int,
                        Optional('external_1'): int,
                        Optional('external_2'): int,
                        Optional('nssa_external_1'): int,
                        Optional('nssa_external_2'): int,
                        Optional('level_1'): int,
                        Optional('level_2'): int,
                        Optional('external'): int,
                        Optional('internal'): int,
                        Optional('local'): int,
                        Optional('default'): int,
                        Optional('prefix'): int,
                        Optional('destination'): int,
                        Optional('redirect'): int,
                        Optional('static'): int,
                        Optional('per_user_static'): int,
                        Any(): {
                            'networks': int,
                            'overhead': int,
                            'memory_bytes': int,
                            Optional('intra_area'): int,
                            Optional('inter_area'): int,
                            Optional('external_1'): int,
                            Optional('external_2'): int,
                            Optional('nssa_external_1'): int,
                            Optional('nssa_external_2'): int,
                            Optional('level_1'): int,
                            Optional('level_2'): int,
                            Optional('external'): int,
                            Optional('internal'): int,
                            Optional('local'): int,
                            Optional('default'): int,
                            Optional('prefix'): int,
                            Optional('destination'): int,
                            Optional('redirect'): int,
                            Optional('static'): int,
                            Optional('per_user_static'): int,
                        },
                    },
                }
            }
        }
    }

# ====================================================
#  parser for show ipv6 route summary
# ====================================================
class ShowIpv6RouteSummary(ShowIpv6RouteSummarySchema):
    """Parser for show ipv6 route summary
                  show ipv6 route vrf <vrf> summary
        """

    cli_command = ['show ipv6 route summary', 'show ipv6 route vrf {vrf} summary']

    def cli(self, vrf='', output=None):
        if output is None:
            if vrf:
                cmd = self.cli_command[1].format(vrf=vrf)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        # IPv6 routing table name is default(0) global scope - 526 entries
        p1 = re.compile(
            r'^IPv6\s+routing\s+table\s+name\s+is\s+(?P<vrf>\S+) *\((?P<vrf_id>\w+)\)\sglobal\sscope\s\-\s(?P<total_entries>\d+)\sentries$')
        # IPv6 routing table default maximum-paths is 16
        p2 = re.compile(r'^IPv6\s+routing\s+table\s+default\s+maximum-paths\s+is\s+(?P<max_path>[\d]+)$')

        # Route Source    Networks    Overhead    Memory (bytes)
        p3 = re.compile(r'^(Route\s+Source\s+Networks\s+Overhead\s+Memory\s+\(bytes\))$')

        # Route Source    Networks    Overhead    Memory (bytes)
        # connected       7           1344        1512
        # local           8           1536        1728
        # ND              0           0           0
        # ospf 200        500         96000       108000
        p4 = re.compile(
            r'^(?P<protocol>\w+)\s(?P<instance>\d+)?\s+(?P<networks>\d+)\s+(?P<overhead>\d+)\s+(?P<memory_bytes>\d+)$')

        # Default: 0  Prefix: 0  Destination: 0  Redirect: 0
        p5 = re.compile(
            r'^Default:\s+(?P<default>\d+)\s+Prefix\:\s+(?P<prefix>\d+)\s+Destination\:\s+(?P<destination>\d+)\s+Redirect\:\s+(?P<redirect>\d+)$')

        # Intra-area: 1 Inter-area: 0 External-1: 0 External-2: 0
        p6 = re.compile(
            r'^Intra-area:\s+(?P<intra_area>\d+)\s+Inter-area:\s+(?P<inter_area>\d+) '
            r'+External-1:\s+(?P<external_1>\d+)\s+External-2:\s+(?P<external_2>\d+)$')

        # NSSA External 1: 0 NSSA External 2: 0
        p7 = re.compile(
            r'^NSSA\sExternal\s1\:\s+(?P<nssa_external_1>\d+)\s+NSSA\sExternal\s2\:\s+('
            r'?P<nssa_external_2>\d+)$')

        # Level 1: 1 Level 2: 0 Inter-area: 0
        p8 = re.compile(
            r'^Level\s1\:\s+(?P<level_1>\d+)\s+Level\s2:\s+(?P<level_2>\d+)\s+Inter\-area:\s+('
            r'?P<inter_area>\d+)$')

        # Internal: 0  External: 0  Local: 0
        p9 = re.compile(r'^Internal:\s+(?P<external>\d+)\s+External:\s+(?P<internal>\d+)\s+Local:\s+(?P<local>\d+)$')

        # Static: 0  Per-user static: 0
        p10 = re.compile(r'^Static\:\s+(?P<static>\d+)\s+Per\-user\s+static\:\s+(?P<per_user_static>\d+)$')

        # /8: 1, /64: 8, /128: 517
        p11 = re.compile(
            r'^\/\d+\:\s+(?P<prefix_8>\d+),\s+/\d+\:\s+(?P<prefix_64>\d+),\s+/\d+\:\s+(?P<prefix_128>\d+)$')

        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()
            # IPv6 routing table name is default(0) global scope - 526 entries
            m = p1.match(line)
            if m:
                vrf = m.groupdict()['vrf']
                vrf_dict = ret_dict.setdefault('vrf', {}).setdefault(vrf, {})
                vrf_dict['vrf_id'] = m.groupdict()['vrf_id']
                vrf_rs_dict = vrf_dict.setdefault('route_source', {})
                continue
            # IPv6 routing table default maximum-paths is 16
            m = p2.match(line)
            if m:
                vrf_dict['maximum_paths'] = int(m.groupdict()['max_path'])
                continue

            # Route Source    Networks    Overhead    Memory (bytes)
            # connected       7           1344        1512
            # local           8           1536        1728
            # ND              0           0           0
            # ospf 200        500         96000       108000
            m = p4.match(line)
            if m:
                group = m.groupdict()
                protocol = group.pop('protocol')
                instance = group.pop('instance')
                if protocol == 'Total':
                    protocol_dict = vrf_dict.setdefault('total_route_source', {})
                else:
                    protocol_dict = vrf_rs_dict.setdefault(protocol, {})
                if instance:
                    inst_dict = protocol_dict.setdefault(instance, {})
                    inst_dict.update({k: int(v) for k, v in group.items() if v})
                else:
                    group = {k: int(v) for k, v in group.items() if v}
                    protocol_dict.update(group)
                continue

            # Default: 0  Prefix: 0  Destination: 0  Redirect: 0
            m = p5.match(line)
            if m:
                group = {k: int(v) for k, v in m.groupdict().items()}
                vrf_rs_dict.setdefault('ND', {})
                vrf_rs_dict['ND'].update(group)
                continue

            # Intra-area: 1 Inter-area: 0 External-1: 0 External-2: 0
            m = p6.match(line)
            if m:
                group = {k: int(v) for k, v in m.groupdict().items()}
                vrf_rs_dict.setdefault(protocol, {})
                vrf_rs_dict[protocol][instance].update(group)
                continue

            # NSSA External 1: 0 NSSA External 2: 0
            m = p7.match(line)
            if m:
                group = {k: int(v) for k, v in m.groupdict().items()}
                vrf_rs_dict.setdefault(protocol, {})
                vrf_rs_dict[protocol][instance].update(group)
                continue

            # Level 1: 1 Level 2: 0 Inter-area: 0
            m = p8.match(line)
            if m:
                group = {k: int(v) for k, v in m.groupdict().items()}
                vrf_rs_dict.setdefault('isis', {})
                # isis can have no area-tag defined
                if instance:
                    vrf_rs_dict['isis'][instance].update(group)
                else:
                    vrf_rs_dict['isis'].update(group)
                continue

            #  Internal: 0  External: 0  Local: 0
            m = p9.match(line)
            if m:
                group = {k: int(v) for k, v in m.groupdict().items()}
                vrf_rs_dict.setdefault('bgp', {})
                vrf_rs_dict['bgp'][instance].update(group)
                continue

            # Static: 0  Per-user static: 0
            m = p10.match(line)
            if m:
                group = {k: int(v) for k, v in m.groupdict().items()}
                vrf_rs_dict.setdefault('static', {})
                vrf_rs_dict['static'].update(group)
                continue

            # /8: 1, /64: 8, /128: 517
            m = p11.match(line)
            if m:
                group = {k: int(v) for k, v in m.groupdict().items()}
                vrf_dict.setdefault('number_of_prefixes', {})
                vrf_dict['number_of_prefixes'].update(group)
                continue

        return ret_dict

