''' show_route.py

Parser for the following show commands:
    * show route
'''

import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional, Or
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
                        Optional(Or('routes', 'tunneled_routes')): {
                            Any(): {
                                'candidate_default': bool,
                                Optional('subnet'): str,
                                'route': str,
                                Optional('active'): bool,
                                Optional('date'): str,
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
           SI - Static InterVRF
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
        'V': 'VPN',
        'P': 'periodic downloaded static route',
        'SI': 'Static InterVRF',
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
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}
        # strip this patter from the original text
        # Codes: L - Local, C - connected, S - static, I - IGRP, R - RIP, M - mobile, B - BGP
        # D - EIGRP, E - EGP, EX - EIGRP external, O - OSPF, I - IGRP, IA - OSPF inter area
        # N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
        # E1 - OSPF external type 1, E2 - OSPF external type 2, E - EGP
        # i - IS-IS, L1 - IS-IS level-1, L2 - IS-IS level-2, ia - IS-IS inter area
        # * - candidate default, su - IS-IS summary, U - per-user static route, o - ODR
        # P - periodic downloaded static route, + - replicated route
        # SI - Static InterVRF
        p1 = re.sub(r'(?ms)(Codes:.+?)replicated\sroute(\s*SI\s-\sStatic\sInterVRF)?', '', out)

        lines = [x.strip() for x in p1.splitlines()]
        entries = dict()
        last_entry = str()
        clean_lines = list()

        for line in lines:
            if re.match(r'(^[A-Z]{1,2})', line):
                entries[line] = list()
                last_entry = line
            else:
                if last_entry == '':
                    continue

                entries[last_entry].append(line)

        for k, v in entries.items():
            clean_lines.append(' '.join(k.split()) + " " + " ".join(v))

        # clean_lines now holds a list of entries in a single line (easier for parsing)
        # Gateway of last resort is 10.16.251.1 to network 0.0.0.0
        # S* 0.0.0.0 0.0.0.0 [10] via 10.16.251.1, outside via 10.16.251.2, pod1000
        # S 0.0.0.1 0.0.0.0 [10/5] via 10.16.255.1, outside via 10.16.255.2, pod1001 via 10.16.255.3, pod1002
        # C 10.10.1.1 255.255.0.0 is directly connected, _internal_loopback
        # C 10.10.1.2 255.255.254.0 is directly connected, outside
        # B 10.122.3.0 255.255.255.0 [20/0] via 172.25.141.2, 7w0d
        # L 10.10.1.3 255.255.255.255 is directly connected, pod2000 is directly connected, pod2002
        # V 10.10.1.4 255.255.255.255 connected by VPN (advertised), admin
        # L 10.10.1.5 255.255.255.255 is directly connected, pod2500
        # C 10.10.1.6 255.255.255.0 is directly connected, pod3000
        # O E2 10.20.58.64 255.255.255.192 [110/11] via 172.20.192.3, 3w6d, wan1
        # O E2 10.20.2.64 255.255.255.192 [110/1] via 10.19.1.1, 2d03h, wan2
        # O E2 10.30.79.64 255.255.255.192 [110/11] via 10.20.192.3, 1w1d, wan3 [110/11] via 10.20.192.4, 1w1d, wan4
        # O 10.205.8.0 255.255.254.0 [110/20] via 172.20.1.1, 7w0d, wan5
        # D 10.0.0.0 255.255.255.0 [90/30720] via 192.168.1.1, 0:19:52, inside

        # [110/11] via 10.20.192.3, 1w1d, wan3 [110/11] via 10.20.192.4, 1w1d, wan4
        p2 = re.compile(
            r'\[(?P<route_preference>[\d\/]+)\]\svia\s+(?P<next_hop>\S+),\s(?P<date>\S+),\s+(?P<context_name>\S+)')

        # O E2
        p3 = re.compile(r'^(?P<protocol>\S+)\s(?P<code>[A-Z].+?)')

        # [20/0] via 172.25.141.2, 7w0d
        p4 = re.compile(r'\[(?P<route_preference>[\d\/]+)\]\svia\s+(?P<next_hop>\S+),\s(?P<date>\S+)')

        # L 10.10.1.5 255.255.255.255 is directly connected, pod2500
        p5 = re.compile(r'^(?P<code>\S+)\s(?P<network>\S+)\s(?P<subnet>\S+)\s(?:.*),\s(?P<context_name>\S+)')

        # SI 10.121.0.0 255.0.0.0 [1/0] is directly connected, gig3
        p5_1 = re.compile(
            r'^(?P<code>\S+)\s(?P<network>\S+)\s(?P<subnet>\S+)\s(\[(?P<route_preference>[\d\/]+)\])?\s(?:.*),\s(?P<context_name>\S+)')

        # S 0.0.0.1 0.0.0.0 [10/5]
        p6 = re.compile(r'^(?P<code>\S+)\s(?P<network>\S+)\s(?P<subnet>\S+)\s\[(?P<route_preference>[\d\/]+)\]')

        # via 10.16.255.1, outside via 10.16.255.2, pod1001 via 10.16.255.3, pod1002
        p7 = re.compile(r'via\s+(?P<next_hop>\S+),\s+(?P<context_name>\S+)')

        # D 10.0.0.0 255.255.255.0 [90/30720] via 192.168.1.1, 0:19:52, inside
        p8 = re.compile(
            r'^(?P<code>\S+)\s(?P<network>\S+)\s(?P<subnet>\S+)\s\[(?P<route_preference>[\d\/]+)\]'
            '\svia\s+(?P<next_hop>\S+),\s(?P<date>\S+),\s+(?P<context_name>\S+)')

        # B 10.122.3.0 255.255.255.0 [20/0]
        p9 = re.compile(r'(?P<code>\S+)\s(?P<network>\S+)\s(?P<subnet>\S+)\s\[(?P<route_preference>[\d\/]+)\]')

        # [170/345856] via 10.9.193.99, 2w1d, esavpn [170/345856] via 10.9.193.98, 2w1d, esavpn
        p10 = re.compile(
            r'\[(?P<route_preference>[\d\/]+)\]\svia\s+(?P<next_hop>\S+),\s(?P<date>\S+),'
            '\s(?P<context_name>\S+)')

        # D EX 10.121.67.0 255.255.255.0
        p11 = re.compile(r'^(?:\S+)\s(?P<code>\S+)\s(?P<network>\S+)\s(?P<subnet>\S+)')

        if not clean_lines:
            return

        dict_ipv4 = ret_dict.setdefault('vrf', {}).setdefault('default', {}). \
            setdefault('address_family', {}).setdefault('ipv4', {})
        dict_routes = dict_ipv4.setdefault('routes', {})

        for line in clean_lines:
            index = 1
            groups = dict()
            next_hops = list()

            target_dict = dict_routes
            if line.strip().endswith("tunneled"):
                target_dict = dict_ipv4.setdefault('tunneled_routes', {})

            if line.startswith('O'):
                """ OSPF """
                next_hops = [m.groupdict() for m in p2.finditer(line)]

                m = p3.match(line)
                """ The CODE pattern O or E2, IA etc"""
                if m:
                    code = m.groupdict()
                else:
                    code = {'code': line[0], 'protocol': line[0]}

                groups['code'] = code['code']
                strip = line.replace(code['protocol'], '').replace(code['code'], '')
                groups['network'], groups['subnet'] = strip.lstrip().split()[0], strip.lstrip().split()[1]

            elif line.startswith('B'):
                """ BGP """

                m = p9.match(line)
                if m:
                    groups = m.groupdict()

                groups['code'] = line[0]
                groups['network'], groups['subnet'] = line.split()[1], line.split()[2]
                next_hops = [m.groupdict() for m in p4.finditer(line)]

            elif line.startswith('L') or line.startswith('V') or line.startswith('C'):
                """ Local, Connected or VPN """
                m = p5.match(line)
                if m:
                    groups = m.groupdict()

            elif line.startswith('SI'):
                """ Static InterVRF """
                m = p5_1.match(line)
                if m:
                    groups = m.groupdict()

            elif line.startswith('S'):
                m = p6.match(line)
                groups = m.groupdict()
                next_hops = [m.groupdict() for m in p7.finditer(line)]

            elif line.startswith('D'):
                """ EIGRP """
                m = p8.match(line)
                if m:
                    groups = m.groupdict()
                else:
                    m = p11.match(line)
                    groups = m.groupdict()
                    next_hops = [m.groupdict() for m in p10.finditer(line)]

            else:
                continue

            prefix_length = str(IPAddress(groups['subnet']).netmask_bits())
            combined_ip = groups['network'] + '/' + prefix_length
            dict_route = target_dict.setdefault(combined_ip, {})

            if '*' in groups['code']:
                dict_route.update({'candidate_default': True})
                groups['code'] = groups['code'].strip('*')
            else:
                dict_route.update({'candidate_default': False})

            dict_route.update({'active': True})

            if 'date' not in groups.keys() and next_hops:
                date = next_hops[0].get('date')
            else:
                date = groups.get('date')
            if date:
                dict_route.update({'date': date})

            dict_route.update({'route': combined_ip})

            dict_route.update({'source_protocol_codes': groups['code']})
            dict_route.update({'source_protocol': self.source_protocol_dict[groups['code']].lower()})

            if 'route_preference' not in groups.keys() and next_hops:
                route_preference = next_hops[0]['route_preference']

            else:
                route_preference = groups.get('route_preference')

            if route_preference:
                if '/' in route_preference:
                    route_preference, metric = map(int, route_preference.split('/'))
                    dict_route.update({'metric': metric})
                else:
                    route_preference = int(route_preference)
                dict_route.update({'route_preference': route_preference})

            if not next_hops and groups.get('context_name'):
                dict_next_hop = dict_route.setdefault('next_hop', {})
                dict_next_hop.update({'outgoing_interface_name': {
                    groups['context_name']: {'outgoing_interface_name': groups['context_name']}
                }})

            for nh in next_hops:
                dict_next_hop = dict_route.setdefault('next_hop', {}).setdefault('next_hop_list', {}).setdefault(index,
                                                                                                                  {})
                dict_next_hop.update({'index': index})
                dict_next_hop.update({'next_hop': nh.get('next_hop')})
                if nh.get('context_name'):
                    dict_next_hop.update({'outgoing_interface_name': nh.get('context_name')})
                index += 1

        return ret_dict
