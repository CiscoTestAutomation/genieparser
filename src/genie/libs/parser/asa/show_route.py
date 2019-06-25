''' show_route.py

Parser for the following show commands:
    * show route
'''

import re
from netaddr import IPAddress
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
                                'candidate_default': bool,
                                Optional('subnet'): str,
                                'route': str,
                                Optional('active'): bool,
                                Optional('route_preference'): int,
                                Optional('metric'): int,
                                Optional('source_protocol'): str,
                                Optional('source_protocol_codes'): str,
                                Optional('next_hop'): {
                                    Optional('outgoing_interface_name'): {
                                        Any(): {  # context_name for interface if there is no next_hop
                                            Optional('outgoing_interface_name'): str
                                        },
                                    },
                                    Optional('next_hop_list'): {
                                        Any(): {  # index
                                            Optional('index'): int,
                                            Optional('next_hop'): str,
                                            Optional('outgoing_interface_name'): str
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

    cli_command = 'show route'

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
        # S 0.0.0.1 0.0.0.0 [10/5] via 10.16.255.1, outside
        p1 = re.compile(
            r'^\s*(?P<code>(?!is)(?!via)[\w\*]+)\s*(?P<network>\d+.\d+.\d+.\d+)\s*'
            '(?P<subnet>\d+.\d+.\d+.\d+)\s*(\[(?P<route_preference>[\d\/]+)\])?\s*'
            '(?P<route_check>[\S]*)\s*(?P<next_hop>\d+.\d+.\d+.\d+),\s*'
            '(?P<context_name>[\S\s]+)$')

        # via 10.16.251.2, pod1000
        p2 = re.compile(
            r'^(?P<network>\d+.\d+.\d+.\d+)?\s*?(?P<route_check>[\S\s]*)\s'
            '(?P<next_hop>\d+.\d+.\d+.\d+),\s*(?P<context_name>[\S\s]+)$')

        # C 10.10.1.2 255.255.254.0 is directly connected, outside
        p3 = re.compile(
            r'^\s*(?P<code>(?!is)(?!via)[\w\*]+)\s*(?P<network>\d+.\d+.\d+.\d+)\s*'
            '(?P<subnet>\d+.\d+.\d+.\d+)\s*(\[(?P<route_preference>[\d\/]+)\])?\s*'
            '(?P<route_check>[\S\s]*)\s*,\s*(?P<context_name>[\S\s]+)$')

        # is directly connected, pod2002
        # connected by VPN (advertised), admin
        p4 = re.compile(
            r'^(?P<route_check>[\S\s]*),\s*(?P<context_name>[\S\s]+)$')

        # V 10.10.1.4 255.255.255.255
        p5 = re.compile(
            r'^\s*(?P<code>(?!is)(?!via)[\w\*]+)\s*(?P<network>\d+.\d+.\d+.\d+)\s*'
            '(?P<subnet>\d+.\d+.\d+.\d+)\s*(\[(?P<route_preference>[\d\/]+)\])?\s*'
            '(?P<context_name>\S+)?$')

        for line in out.splitlines():
            line = line.strip()

            # S* 0.0.0.0 0.0.0.0 via 10.16.251.1, outside
            # S 0.0.0.1 0.0.0.0 [10/5] via 10.16.255.1, outside
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                dict_ipv4 = ret_dict.setdefault('vrf', {}).setdefault('default', {}). \
                setdefault('address_family', {}).setdefault('ipv4', {}). \
                setdefault('routes', {})
                if 'via' in groups['route_check'] and groups['next_hop']:
                    if groups['code']:
                        code = groups['code']
                        source_protocol_codes = groups['code'].strip()
                        for key, val in super().source_protocol_dict.items():
                            source_protocol_replaced = re.split \
                            ('\*',source_protocol_codes)[0].strip()
                            code = source_protocol_replaced
                            if source_protocol_replaced in val:
                                source_protocol = key
                    if groups['network']:
                        routes = groups['network']
                        subnet = groups['subnet']
                        if '0.0.0.0' == subnet:
                            prefix_length = str(0)
                        else:
                            prefix_length = str(IPAddress(subnet).netmask_bits())
                        combined_ip = routes+'/'+prefix_length
                        dict_routes = dict_ipv4.setdefault(combined_ip, {})
                        dict_routes.update({'active': True})
                        dict_routes.update({'route': combined_ip})
                        dict_routes.update({'source_protocol_codes': code})
                        dict_routes.update({'source_protocol': source_protocol})
                        if '*' in groups['code']:
                            dict_routes.update({'candidate_default': True})
                        else:
                            dict_routes.update({'candidate_default': False})
                        if groups['route_preference']:
                            routepreference = groups['route_preference']                        
                            if '/' in routepreference:
                                route_preference = int(routepreference.split('/')[0])
                                metric = int(routepreference.split('/')[1])
                                dict_routes.update \
                                ({'route_preference': route_preference})
                                dict_routes.update({'metric': metric})
                            else:
                                dict_routes.update \
                                ({'route_preference': int(routepreference)})
                        if groups['next_hop']:
                            if groups['network'] and groups['next_hop']:
                                index = 1
                            next_hop = groups['next_hop']
                            outgoing_interface_name = groups['context_name']
                            dict_next_hop = dict_routes.setdefault('next_hop', {}). \
                            setdefault('next_hop_list', {}).setdefault(index, {})
                            dict_next_hop.update({'index': index})
                            dict_next_hop.update({'next_hop': next_hop})
                            dict_next_hop.update \
                            ({'outgoing_interface_name': outgoing_interface_name})
                            index += 1
                continue

            # via 10.16.251.2, pod1000
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                if 'via' in groups['route_check']:
                    if groups['network'] and groups['next_hop']:
                        index = 1
                    next_hop = groups['next_hop']
                    outgoing_interface_name = groups['context_name']
                    dict_next_hop = dict_routes.setdefault('next_hop', {}). \
                    setdefault('next_hop_list', {}).setdefault(index, {})
                    dict_next_hop.update({'index': index})
                    dict_next_hop.update({'next_hop': next_hop})
                    dict_next_hop.update \
                    ({'outgoing_interface_name': outgoing_interface_name})
                    index += 1
                continue

            # C 10.10.1.2 255.255.254.0 is directly connected, outside
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                dict_ipv4 = ret_dict.setdefault('vrf', {}).setdefault('default', {}). \
                setdefault('address_family', {}).setdefault('ipv4', {}). \
                setdefault('routes', {})
                if 'is directly' in groups['route_check']:
                    if groups['code']:
                        source_protocol_codes = groups['code'].strip()
                        for key, val in super().source_protocol_dict.items():
                            source_protocol_replaced = re.split \
                            ('\*',source_protocol_codes)[0].strip()
                            if source_protocol_replaced in val:
                                source_protocol = key
                    if groups['network']:
                        routes = groups['network']
                        subnet = groups['subnet']
                        if '0.0.0.0' == subnet:
                            prefix_length = str(0)
                        else:
                            prefix_length = str(IPAddress(subnet).netmask_bits())
                        combined_ip = routes+'/'+prefix_length                    
                        dict_routes = dict_ipv4.setdefault(combined_ip, {})
                        dict_routes.update({'active': True})
                        dict_routes.update({'route': combined_ip})
                        dict_routes.update({'source_protocol_codes': groups['code']})
                        dict_routes.update({'source_protocol': source_protocol})
                        if '*' in groups['code']:
                            dict_routes.update({'candidate_default': True})
                        else:
                            dict_routes.update({'candidate_default': False})
                        if groups['route_preference']:
                            routepreference = groups['route_preference']                        
                            if '/' in routepreference:
                                route_preference = int(routepreference.split('/')[0])
                                metric = int(routepreference.split('/')[1])
                                dict_routes.update \
                                ({'route_preference': route_preference})
                                dict_routes.update({'metric': metric})
                            else:
                                dict_routes.update \
                                ({'route_preference': int(routepreference)})            
                        outgoing_interface_name = groups['context_name']
                        dict_via = dict_routes.setdefault('next_hop', {}). \
                        setdefault('outgoing_interface_name', {}). \
                        setdefault(outgoing_interface_name, {})
                        dict_via.update \
                        ({'outgoing_interface_name': outgoing_interface_name})
                continue

            # is directly connected, pod2002
            # connected by VPN (advertised), admin
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                if 'is directly' in groups['route_check'] or 'connected by' \
                in groups['route_check']:
                    outgoing_interface_name = groups['context_name']
                    dict_via = dict_routes.setdefault('next_hop', {}). \
                    setdefault('outgoing_interface_name', {}). \
                    setdefault(outgoing_interface_name, {})
                    dict_via.update \
                    ({'outgoing_interface_name': outgoing_interface_name})
                continue

            # V 10.10.1.4 255.255.255.255
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                dict_ipv4 = ret_dict.setdefault('vrf', {}).setdefault('default', {}). \
                setdefault('address_family', {}).setdefault('ipv4', {}). \
                setdefault('routes', {})
                if groups['network'] and groups['context_name'] is None:
                    if groups['code']:
                        source_protocol_codes = groups['code'].strip()
                        for key, val in super().source_protocol_dict.items():
                            source_protocol_replaced = re.split \
                            ('\*',source_protocol_codes)[0].strip()
                            if source_protocol_replaced in val:
                                source_protocol = key
                    if groups['network']:
                        routes = groups['network']
                        subnet = groups['subnet']
                        if '0.0.0.0' == subnet:
                            prefix_length = str(0)
                        else:
                            prefix_length = str(IPAddress(subnet).netmask_bits())
                        combined_ip = routes+'/'+prefix_length                    
                        dict_routes = dict_ipv4.setdefault(combined_ip, {})
                        dict_routes.update({'active': True})
                        dict_routes.update({'route': combined_ip})
                        dict_routes.update({'source_protocol_codes': groups['code']})
                        dict_routes.update({'source_protocol': source_protocol})
                        if '*' in groups['code']:
                            dict_routes.update({'candidate_default': True})
                        else:
                            dict_routes.update({'candidate_default': False})
                        if groups['route_preference']:
                            routepreference = groups['route_preference']                        
                            if '/' in routepreference:
                                route_preference = int(routepreference.split('/')[0])
                                metric = int(routepreference.split('/')[1])
                                dict_routes.update \
                                ({'route_preference': route_preference})
                                dict_routes.update({'metric': metric})
                            else:
                                dict_routes.update \
                                ({'route_preference': int(routepreference)})
                continue

        return ret_dict