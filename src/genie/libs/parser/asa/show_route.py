''' show_route.py

Parser for the following show commands:
    * show route
'''

import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                                Any, \
                                                Optional

# =============================================
# Schema for 'show route'
# =============================================
class ShowRouteSchema(MetaParser):
    """Schema for
        * show route
    """
    schema = {
        'vrf': {
            'default': {
                'address_family': {
                    'ipv4': {
                        Optional('routes'): {
                            Any(): {
                                Optional('mac_address'): str,
                                Optional('route'): str,
                                Optional('active'): bool,
                                Optional('route_preference'): int,
                                Optional('metric'): int,
                                Optional('source_protocol'): str,
                                Optional('source_protocol_codes'): str,
                                Optional('next_hop'): {
                                    Optional('outgoing_interface'): {
                                        Any(): {  # interface  if there is no next_hop
                                            Optional('outgoing_interface'): str
                                        },
                                    },
                                    Optional('next_hop_list'): {
                                        Any(): {  # index
                                            Optional('index'): int,
                                            Optional('next_hop'): str,
                                            Optional('outgoing_interface'): str
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
    Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
           D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
           N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
           E1 - OSPF external type 1, E2 - OSPF external type 2, V - VPN
           i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
           ia - IS-IS, * - candidate default, U - per-user static route
           o - ODR, P - periodic downloaded static route, + - replicated route
    """
    source_protocol_dict = {
        'ospf' : ['O','IA','N1','N2','E1','E2'],
        'odr' : ['o'],
        'isis' : ['i','su','L1','L2','ia'],
        'eigrp' : ['D','EX'],
        'static' : ['S'],
        'egp' : ['E'],
        'mobile' : ['M'],
        'local' : ['L'],
        'connected' : ['C'],
        'bgp' : ['B'],
        'per-user static route': ['U'],
        'rip' : ['R'],
        'igrp': ['I'],
        'replicated route': ['+'],
        'periodic downloaded static route': ['P'],
        'vpn': ['V']
    }


# =============================================
# Parser for 'show route'
# =============================================
class ShowRoute(ShowRouteSchema):
    """Parser for
        * show route
    """

    cli_command = 'show interface summary'

    def cli(self, output=None):
        if output is None:
            # excute command to get output
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}
        routes = source_protocol = ''
        index = 1

        # S* 0.0.0.0 0.0.0.0 via 10.16.251.1, outside
        #                    via 10.16.251.2, pod1000
        # S 0.0.0.1 0.0.0.0 [10/5] via 10.16.255.1, outside
        # L 192.16.168.251 255.255.255.255 is directly connected, pod2000
        #                                  is directly connected, pod2002
        # V 192.168.0.1 255.255.255.255
        #                      connected by VPN (advertised), admin
        p1 = re.compile(
            r'^\s*(?P<code>(?!is)(?!via)[\w\*\(\>\)\!]+)?(\ +)?'
            '(?P<network>\d+.\d+.\d+.\d+)?( )?(?P<mac_address>\d+.\d+.\d+.\d+)?( )?'
            '(?P<vpn>connected by VPN [\(\)\S]+)?(is +directly +connected, )?'
            '(\[(?P<route_preference>[\d\/]+)\])?( )?(via )?'
            '(?P<next_hop>\d+.\d+.\d+.\d+)?,?( )?(?P<interface>[\S]+)?$')

        for line in out.splitlines():
            line = line.strip()

            # S* 10.10.1.1 0.0.0.0 via 20.20.2.2, outside
            #                    via 20.20.2.2, pod1000
            # S 10.10.1.1 0.0.0.0 [10/5] via 20.20.2.2, outside
            # L 10.10.1.1 255.255.255.255 is directly connected, pod2000
            #                                 is directly connected, pod2002
            # V        10.10.1.1 255.255.255.255
            #                         connected by VPN (advertised), admin
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                dict_ipv4 = ret_dict.setdefault('vrf', {}).setdefault('default', {}). \
                setdefault('address_family', {}).setdefault('ipv4', {}). \
                setdefault('routes', {})
                if groups['code']:
                    source_protocol_codes = groups['code'].strip()
                    for key,val in super().source_protocol_dict.items():
                        source_protocol_replaced = re.split \
                        ('\*|\(\!\)|\(\>\)',source_protocol_codes)[0].strip()
                        if source_protocol_replaced in val:
                            source_protocol = key
                if groups['network']:
                    routes = groups['network']
                    dict_routes = dict_ipv4.setdefault(routes, {})
                    dict_routes.update({'active': True})
                    dict_routes.update({'route': routes})
                    dict_routes.update({'source_protocol_codes': groups['code']})
                    dict_routes.update({'source_protocol': source_protocol})
                    dict_routes.update({'mac_address': groups['mac_address']})
                    if groups['route_preference']:
                        routepreference = groups['route_preference']                        
                        if '/' in routepreference:
                            route_preference = int(routepreference.split('/')[0])
                            metric = int(routepreference.split('/')[1])
                            dict_routes.update({'route_preference': route_preference})
                            dict_routes.update({'metric': metric})
                        else:
                            dict_routes.update({'route_preference': route_preference})
                if groups['network'] is None and groups['interface']:
                    dict_routes = dict_ipv4.setdefault(routes, {})
                if groups['interface']:
                    if groups['next_hop'] is None:
                        outgoing_interface = groups['interface']
                        dict_via = dict_routes.setdefault('next_hop', {}). \
                        setdefault('outgoing_interface', {}). \
                        setdefault(outgoing_interface, {})
                        dict_via.update({'outgoing_interface': outgoing_interface})
                    if groups['next_hop']:
                        if groups['network'] and groups['next_hop']:
                            index = 1
                        next_hop = groups['next_hop']
                        outgoing_interface = groups['interface']
                        dict_next_hop = dict_routes.setdefault('next_hop', {}). \
                        setdefault('next_hop_list', {}).setdefault(index, {})
                        dict_next_hop.update({'index': index})
                        dict_next_hop.update({'next_hop': next_hop})
                        dict_next_hop.update({'outgoing_interface': outgoing_interface})
                        index += 1
            continue

        return ret_dict