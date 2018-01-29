'''
show_route.py

'''
import re
from metaparser import MetaParser
from metaparser.util.schemaengine import Schema, \
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
                                Optional('next_hop'): {
                                    Optional('outgoing_interface'): {
                                        Any(): {  # interface  if there is no next_hop
                                            Optional('outgoing_interface'): str,
                                            Optional('last_updated'): str,
                                        },
                                    },
                                    Optional('next_hop_list'): {
                                        Any(): {  # index
                                            Optional('index'): int,
                                            Optional('next_hop'): str,
                                            Optional('last_updated'): str,
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
       show ip route vrf <vrf>"""

    def cli(self, vrf=""):
        if vrf:
            cmd = 'show ip route vrf {}'.format(vrf)
        else:
            cmd = 'show ip route'
            vrf = 'default'
        out = self.device.execute(cmd)

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
        for line in out.splitlines():
            if line:
                line = line.rstrip()
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
            p3 = re.compile(r'^\s*(?P<code>[\w]+) +(?P<code1>[\w]+)? +(?P<network>[\d\/\.]+)?'
                            '( +is +directly +connected,)?( +\[(?P<route_preference>[\d\/]+)\]'
                            ' +via +(?P<next_hop>[\d\.]+)?,)?( +(?P<date>[0-9][\w\:]+))?,?( +(?P<interface>[\w\/\.]+))?$')
            m = p3.match(line)
            if m:

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
                            ' +via +(?P<next_hop>[\d\.]+)?,?( +(?P<date>[0-9][\w\:]+),)?( +(?P<interface>[\w\/\.]+))?$')
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
                            ' +via +(?P<next_hop>[\d\.]+)?,)?( +(?P<date>[0-9][\w\:]+),)?( +(?P<interface>[\w\/\.]+))?$')
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

                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                            ['next_hop']['outgoing_interface'][interface]['outgoing_interface'] = interface

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
        return result_dict

# ====================================================
#  schema for show ipv6 route updated
# ====================================================
class ShowIpv6RouteUpdatedSchema(MetaParser):
    """Schema for show ipv6 route updated"""
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
                                            Optional('last_updated'): str,
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

    def cli(self, vrf=""):
        if vrf:
            cmd = 'show ipv6 route vrf {} updated'.format(vrf)
        else:
            cmd = 'show ipv6 route updated'
            vrf = 'default'
        out = self.device.execute(cmd)

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
                            '( +(?P<interface>[\w\/\.]+))?,?( +receive)?( +directly connected)?( +indirectly connected)?$')
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
                            ' +(?P<interface>[\w\/\.]+)$')
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
        return result_dict