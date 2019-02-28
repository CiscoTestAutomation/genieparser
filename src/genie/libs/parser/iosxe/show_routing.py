'''
show_route.py

'''
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                         Any, \
                                         Optional


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
    cli_command = ['show ip route vrf {vrf}','show ip route','show ip route {route}','show ip route vrf {vrf} {route}']

    def cli(self,vrf="",route="",output=None):
        if output is None:
            if vrf and not route:
                cmd = self.cli_command[0].format(vrf=vrf)
            elif not route  and not vrf :
                cmd = self.cli_command[1]
                vrf = 'default'
            elif route and not vrf :
                cmd = self.cli_command[2].format(route=route)
                vrf = 'default'
            elif route and vrf :
                cmd = self.cli_command[3].format(route=route,vrf=vrf)

            out = self.device.execute(cmd)
        else:
            out = output

        af = 'ipv4'
        route = ""
        source_protocol_dict = {}
        source_protocol_dict['ospf'] = ['O','IA','N1','N2','E1','E2']
        source_protocol_dict['odr'] = ['o']
        source_protocol_dict['isis'] = ['i','su','L1','L2','ia']
        source_protocol_dict['eigrp'] = ['D','EX']
        source_protocol_dict['static'] = ['S']
        source_protocol_dict['mobile'] = ['M']
        source_protocol_dict['rip'] = ['R']
        source_protocol_dict['lisp'] = ['I']
        source_protocol_dict['nhrp'] = ['H']
        source_protocol_dict['local'] = ['L']
        source_protocol_dict['connected'] = ['C']
        source_protocol_dict['bgp'] = ['B']

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


        for line in out.splitlines():
            if line:
                line = line.strip()
            else:
                continue
            next_hop = interface = updated = metrics = route_preference = ""
            # Routing Table: VRF1
            p1 = re.compile(r'^\s*Routing Table: +(?P<vrf>[\w]+)$')
            m = p1.match(line)
            if m:
                vrf = m.groupdict()['vrf']
                continue

            # 1.0.0.0/32 is subnetted, 1 subnets
            # 10.0.0.0/8 is variably subnetted, 5 subnets, 2 masks
            p2 = re.compile(r'^\s*(?P<subnetted_ip>[\d\/\.]+)'
                            ' +is +(variably )?subnetted, +(?P<number_of_subnets>[\d]+) +subnets(, +(?P<number_of_masks>[\d]+) +masks)?$')
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

            # C        1.1.1.1 is directly connected, Loopback0
            # S        2.2.2.2 [1/0] via 20.1.2.2, GigabitEthernet0/1
            # O        10.2.3.0/24 [110/2] via 20.1.2.2, 06:46:59, GigabitEthernet0/1
            # i L1     22.22.22.22 [115/20] via 20.1.2.2, 06:47:04, GigabitEthernet0/1
            # D        200.1.4.1
            p3 = re.compile(r'^\s*(?P<code>[\w\*]+) +(?P<code1>[\w]+)? +(?P<network>[\d\/\.]+)?'
                            '( +is +directly +connected,)?( +\[(?P<route_preference>[\d\/]+)\]?'
                            '( +via )?(?P<next_hop>[\d\.]+)?,)?( +(?P<date>[0-9][\w\:]+))?,?( +(?P<interface>[\S]+))?$')
            m = p3.match(line)
            if m:
                active = True
                if m.groupdict()['code']:
                    source_protocol_codes = m.groupdict()['code'].strip()
                    for key,val in source_protocol_dict.items():
                        if source_protocol_codes in val:
                            source_protocol = key

                if m.groupdict()['code1']:
                    source_protocol_codes = '{} {}'.format(source_protocol_codes, m.groupdict()['code1'])

                if m.groupdict()['network']:
                    network = m.groupdict()['network']
                    if '/' in network:
                        route = network
                    else:
                        route = '{}/{}'.format(network,netmask)

                if not m.groupdict()['network']:
                    route = route
                if m.groupdict()['route_preference']:
                    routepreference = m.groupdict()['route_preference']
                    if '/' in routepreference:
                        route_preference = int(routepreference.split('/')[0])
                        metrics = routepreference.split('/')[1]

                index = 1
                if m.groupdict()['next_hop']:
                    next_hop = m.groupdict()['next_hop']
                if m.groupdict()['interface']:
                    interface = m.groupdict()['interface']

                if m.groupdict()['date']:
                    updated = m.groupdict()['date']

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

                        if updated:
                            result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                                ['next_hop_list'][index]['updated'] = updated

                        if interface:
                            result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                                ['next_hop_list'][index]['outgoing_interface'] = interface

                continue

            #    [110/2] via 10.1.2.2, 06:46:59, GigabitEthernet0/0
            p4 = re.compile(r'^\s*\[(?P<route_preference>[\d\/]+)\]'
                            ' +via +(?P<next_hop>[\d\.]+)?,?( +(?P<date>[0-9][\w\:]+),)?( +(?P<interface>[\S]+))?$')
            m = p4.match(line)
            if m:

                routepreference = m.groupdict()['route_preference']
                if '/' in routepreference:
                    route_preference = int(routepreference.split('/')[0])
                    metrics = routepreference.split('/')[1]

                next_hop = m.groupdict()['next_hop']
                index +=1
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

                    if m.groupdict()['interface'] and interface not in result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                            ['next_hop']['outgoing_interface']:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                            ['next_hop']['outgoing_interface'][interface] = {}

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

                    if updated:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                            ['next_hop_list'][index]['updated'] = updated

                    if interface:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                            ['next_hop_list'][index]['outgoing_interface'] = interface

                continue

            #       is directly connected, GigabitEthernet0/2
            p5 = re.compile(r'^\s*is +directly +connected,( +\[(?P<route_preference>[\d\/]+)\]'
                            ' +via +(?P<next_hop>[\d\.]+)?,)?( +(?P<date>[0-9][\w\:]+),)?( +(?P<interface>[\S]+))?$')
            m = p5.match(line)
            if m:

                if m.groupdict()['route_preference']:
                    routepreference = m.groupdict()['route_preference']
                    if '/' in routepreference:
                        route_preference = int(routepreference.split('/')[0])
                        metrics = routepreference.split('/')[1]

                index += 1
                if m.groupdict()['next_hop']:
                    next_hop = m.groupdict()['next_hop']
                if m.groupdict()['interface']:
                    interface = m.groupdict()['interface']

                if m.groupdict()['date']:
                    updated = m.groupdict()['date']

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
                            ['route_preference'] = route_preference

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
                        if 'next_hop_list' not in result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop']:
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
            # Routing entry for 61.0.0.0/24, 1 known subnets
            # Routing entry for 0.0.0.0/0, supernet
            # Routing entry for 200.1.2.0/24
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

            # Last update from 201.1.12.2 on Vlan101, 2w3d ago
            # Last update from 201.3.12.2 on Vlan103, 00:00:12 ago
            m = p400.match(line)
            if m:
                group = m.groupdict()
                update_dict = route_dict.setdefault('update', {})
                update_dict.update({k: v for k, v in group.items() if v})
                continue

            # * 201.1.12.2, from 201.1.12.2, 2w3d ago, via Vlan101
            # * 18.0.1.2
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

    cli_command = ['show ipv6 route vrf {vrf} updated', 'show ipv6 route updated']

    def cli(self, vrf="", output=None):
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
        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue

            # IPv6 Routing Table - default - 23 entries
            # IPv6 Routing Table - VRF1 - 104 entries
            p1 = re.compile(r'^\s*IPv6 +Routing +Table +\- +(?P<vrf>[\w]+) +\- +(?P<entries>[\d]+) +entries$')
            m = p1.match(line)
            if m:
                vrf = m.groupdict()['vrf']
                continue

            # LC  2001:1:1:1::1/128 [0/0]
            p2 = re.compile(r'^\s*(?P<code>[\w]+) +(?P<route>[\w\/\:]+)?'
                            ' +\[(?P<route_preference>[\d\/]+)\]$')
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
            #   via 200.0.4.1%default, indirectly connected
            p3 = re.compile(r'^\s*via( +(?P<next_hop>[0-9][\w\:\.\%]+)?,)?'
                            '( +(?P<interface>[\w\.\/\-\_]+))?,?( +receive)?( +directly connected)?( +indirectly connected)?$')
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
            p4 = re.compile(r'^\s*via +(?P<next_hop>[\w\:\.\%]+),'
                            ' +(?P<interface>[\S]+)$')
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
            p5 = re.compile(r'^\s*Last +updated +(?P<last_updated>[\S\s]+)$')
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
                Optional('update'): {
                    'from': str,
                    'interface': str,
                    'age': str
                },
                'paths': {
                    Any(): {
                        'nexthop': str,
                        Optional('from'): str,
                        Optional('age'): str,
                        Optional('interface'): str,
                        Optional('metric'): str,
                        Optional('share_count'): str
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
    IP_VER = 'ip'

    cli_command = ['show {ip} route vrf {vrf} {route}', 'show {ip} route {route}']

    def cli(self, route, vrf='', output=None):
        if output is None:
            # excute command to get output
            if vrf:
                cmd = self.cli_command[0].format(vrf=vrf, route=route, ip=self.IP_VER)
            else:
                cmd = self.cli_command[1].format(route=route, ip=self.IP_VER)

            out = self.device.execute(cmd)
        else:
            out = output

        # initial regexp pattern
        p1 = re.compile(r'^Routing +entry +for +'
                         '(?P<entry>(?P<ip>[\w\:\.]+)\/(?P<mask>\d+))'
                         '(, +(?P<net>[\w\s]+))?$')
        p2 = re.compile(r'^Known +via +\"(?P<known_via>[\w\s]+)\", +'
                         'distance +(?P<distance>\d+), +'
                         'metric +(?P<metric>\d+)'
                         '(, +(?P<type>[\w\-\s]+)(?P<connected>, connected)?)?$')
        p3 = re.compile(r'^Redistributing +via +(?P<redist_via>\w+) *'
                         '(?P<redist_via_tag>\d+)?$')
        p4 = re.compile(r'^Last +update +from +(?P<from>[\w\.]+) +'
                         'on +(?P<interface>[\w\.\/\-]+), +'
                         '(?P<age>[\w\.\:]+) +ago$')
        p5 = re.compile(r'^\*? *(?P<nexthop>[\w\.]+)(, +'
                         'from +(?P<from>[\w\.]+), +'
                         '(?P<age>[\w\.\:]+) +ago, +'
                         'via +(?P<interface>[\w\.\/\-]+))?$')
        p6 = re.compile(r'^Route +metric +is +(?P<metric>\d+), +'
                         'traffic +share +count +is +(?P<share_count>\d+)$')

        # ipv6 specific
        p7 = re.compile(r'^Route +count +is +(?P<route_count>[\d\/]+), +'
        	             'share +count +(?P<share_count>[\d\/]+)$')
        p8 = re.compile(r'^(?P<fwd_ip>[\w\:]+)(, +(?P<fwd_intf>[\w\.\/\-]+)'
        	             '( indirectly connected)?)?$')
        p8_1 = re.compile(r'^receive +via +(?P<fwd_intf>[\w\.\/\-]+)$')
        p9 = re.compile(r'^Last +updated +(?P<age>[\w\:\.]+) +ago$')
        p10 = re.compile(r'^From +(?P<from>[\w\:]+)$')

        # initial variables
        ret_dict = {}
        index = 0

        for line in out.splitlines():
            line = line.strip()

            # Routing entry for 61.0.0.0/24, 1 known subnets
            # Routing entry for 0.0.0.0/0, supernet
            # Routing entry for 200.1.2.0/24
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
            m = p2.match(line)
            if m:
                group = m.groupdict()
                entry_dict.update({k:v for k,v in group.items() if v})
                continue

            # Redistributing via rip
            # Redistributing via eigrp 1
            m = p3.match(line)
            if m:
                group = m.groupdict()
                entry_dict.update({k:v for k,v in group.items() if v})
                continue

            # Last update from 201.1.12.2 on Vlan101, 2w3d ago
            # Last update from 201.3.12.2 on Vlan103, 00:00:12 ago
            m = p4.match(line)
            if m:
                group = m.groupdict()
                update_dict = entry_dict.setdefault('update', {})
                update_dict.update({k:v for k,v in group.items() if v})
                continue

            # * 201.1.12.2, from 201.1.12.2, 2w3d ago, via Vlan101
            # * 18.0.1.2
            m = p5.match(line)
            if m:
                group = m.groupdict()
                index += 1
                path_dict = entry_dict.setdefault('paths', {}).setdefault(index, {})
                path_dict.update({k:v for k,v in group.items() if v})
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
    IP_VER = 'ipv6'