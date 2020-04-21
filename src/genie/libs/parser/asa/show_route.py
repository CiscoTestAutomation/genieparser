''' show_route.py

Parser for the following show commands:
    * show route
'''

import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional
from netaddr import IPAddress


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
        'O': 'ospf',
        'IA': 'ospf',
        'N1': 'ospf',
        'N2': 'ospf',
        'E1': 'ospf',
        'E2': 'ospf',
        'o': 'odr',
        'i': 'isis',
        'su': 'isis',
        'L1': 'isis',
        'L2': 'isis',
        'ia': 'isis',
        'D': 'eigrp',
        'EX': 'eigrp',
        'S': 'static',
        'E': 'egp',
        'M': 'mobile',
        'L': 'local',
        'C': 'connected',
        'B': 'bgp',
        'U': 'per-user static route',
        'R': 'rip',
        'I': 'igrp',
        '+': 'replicated route',
        'V': 'periodic downloaded static route',
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
        out = re.sub(r'(?ms)(Codes:.+?)replicated\sroute', '', out, re.MULTILINE)
        r_routes = re.compile(r'(?:^\S{1,4})\s(?:.*)\r?\n(?:^\ +.*\r?\n)*', re.MULTILINE)  # All routes (split)

        r_static = re.compile(
            r'(?P<code>S|S\*)\s(?P<network>\S+)\s(?P<subnet>\S+)\s\[(?P<route_preference>[\d\/]+)\]'
            r'\svia\s(?P<next_hop>\S+),\s(?P<context_name>\S+)')

        r_connected_and_local = re.compile(
            r'(?i)(?P<code>(C|L|S))[ ]+(?P<network>\S+)\s+(?P<subnet>\S+)\s+is\s+directly\s+connected,'
            r'\s+(?P<context_name>\S+)')

        r_bgp = re.compile(
            r'(?i)(?P<code>B)[ ]+(?P<network>\S+)\s+(?P<subnet>\S+)\s+\[(?P<route_preference>.*?)\]'
            r'\s+via\s+(?P<next_hop>\S+),\s+(?P<age>\S+)')

        r_vpn = re.compile(
            r'(?P<code>V)\s(?P<network>\S+)\s(?P<subnet>\S+)\sconnected\sby\sVPN\s\(advertised\),\s'
            r'(?P<context_name>\S+)')

        r_ospf1 = re.compile(
            r'(?P<type>O)\s(?P<code>\S+)\s(?P<network>\S+)\s(?P<subnet>\S+)\s\[(?P<route_preference>'
            r'[\d\/]+)\]\svia\s(?P<next_hop>\S+),\s(?P<age>\S+),\s(?P<context_name>\S+)')

        r_ospf_eigrp = re.compile(
            r'(?P<code>O|D)\s(?P<network>\S+)\s(?P<subnet>\S+)\s\[(?P<route_preference>[\d\/]+)\]\svia'
            r'\s(?P<next_hop>\S+),\s(?P<age>\S+),\s(?P<context_name>\S+)')

        r_ospf_nh = re.compile(r'(via\s+(?P<next_hop>\S+),\s(?P<age>\S+)\s+(?P<context_name>\S+))')
        r_bgp_nh = re.compile(r'via\s+(?P<next_hop>\S+),\s(?P<age>\S+)')
        r_static_nh = re.compile(r'via\s+(?P<next_hop>\S+),\s(?P<context_name>\S+)')

        for line in r_routes.findall(out + "\n"):
            index = 1

            clean_line = ' '.join(line.split())
            groups = dict()
            next_hops = list()

            """ static """
            m = r_static.match(clean_line)
            if m:
                groups = m.groupdict()

            """ connected and local """
            m = r_connected_and_local.match(clean_line)
            if m:
                groups = m.groupdict()

            """ bgp """
            m = r_bgp.match(clean_line)
            if m:
                groups = m.groupdict()

            """ osp1 """
            m = r_ospf1.match(clean_line)
            if m:
                groups = m.groupdict()
            else:
                m = r_ospf_eigrp.match(clean_line)
                if m:
                    groups = m.groupdict()

            """ vpn """
            m = r_vpn.match(clean_line)
            if m:
                groups = m.groupdict()

            dict_ipv4 = ret_dict.setdefault('vrf', {}).setdefault('default', {}). \
                setdefault('address_family', {}).setdefault('ipv4', {}). \
                setdefault('routes', {})

            routes = groups['network']
            subnet = groups['subnet']
            prefix_length = str(IPAddress(subnet).netmask_bits())

            prefix = routes + '/' + prefix_length
            source_protocol = super().source_protocol_dict[groups['code'].strip('*')]

            dict_routes = dict_ipv4.setdefault(prefix, {})

            if '*' in groups['code']:
                dict_routes.update({'candidate_default': True})
                groups['code'] = groups['code'].strip('*')
            else:
                dict_routes.update({'candidate_default': False})

            dict_routes.update({'active': True})
            dict_routes.update({'route': prefix})
            dict_routes.update({'source_protocol_codes': groups['code']})
            dict_routes.update({'source_protocol': source_protocol})

            if "via" in clean_line and groups['code'] == 'S':
                """ static"""
                next_hops = [m.groupdict() for m in r_static_nh.finditer(clean_line)]

            if "via" in clean_line and dict_routes['source_protocol'] == 'ospf':
                """ ospf"""
                next_hops = [m.groupdict() for m in r_ospf_nh.finditer(clean_line)]

            if "via" in clean_line and groups['code'] == 'B':
                """ bgp"""
                next_hops = [m.groupdict() for m in r_bgp_nh.finditer(clean_line)]

            if 'route_preference' in groups.keys():
                if '/' in groups['route_preference']:
                    route_preference, metric = map(int, groups['route_preference'].split('/'))
                    dict_routes.update({'metric': metric})
                else:
                    route_preference = int(groups['route_preference'])
                dict_routes.update({'route_preference': route_preference})
            if not next_hops and groups.get('context_name'):
                dict_next_hop = dict_routes.setdefault('next_hop', {})
                dict_next_hop.update({'outgoing_interface_name': {
                    groups['context_name']: {'outgoing_interface_name': groups['context_name']}
                }})

            for nh in next_hops:
                dict_next_hop = dict_routes.setdefault('next_hop', {}).setdefault('next_hop_list', {}).setdefault(index,
                                                                                                                  {})
                dict_next_hop.update({'index': index})
                dict_next_hop.update({'next_hop': nh.get('next_hop')})
                if nh.get('context_name'):
                    dict_next_hop.update({'outgoing_interface_name': nh.get('context_name')})
                index += 1

        return ret_dict
