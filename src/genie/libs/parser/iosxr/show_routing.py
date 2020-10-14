'''
show_route.py

'''
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
    Any, \
    Optional


# ====================================================
#  schema for show route ipv4
# ====================================================
class ShowRouteIpv4Schema(MetaParser):
    """Schema for show route ipv4"""
    schema = {
        'vrf': {
            Any(): {
                'address_family': {
                    Any(): {
                        Optional('routes'): {
                            Any(): {
                                'route': str,
                                'active': bool,
                                Optional('ip'): str,
                                Optional('mask'): str,
                                Optional('route_preference'): int,
                                Optional('metric'): int,
                                Optional('source_protocol'): str,
                                Optional('source_protocol_codes'): str,
                                Optional('known_via'): str,
                                Optional('distance'): int,
                                Optional('type'): str,
                                Optional('tag'): str,
                                Optional('installed'): {
                                    'date': str,
                                    'for': str,
                                },
                                Optional('redist_advertisers'): {
                                    Any(): {
                                        'protoid': int,
                                        'clientid': int,
                                    },
                                },
                                'next_hop': {
                                    Optional('outgoing_interface'): {
                                        Any(): {
                                            'outgoing_interface': str,
                                            Optional('updated'): str,
                                            Optional('metric'): int,
                                        }
                                    },
                                    Optional('next_hop_list'): {
                                        Any(): { # index
                                            'index': int,
                                            Optional('next_hop'): str,
                                            Optional('outgoing_interface'): str,
                                            Optional('updated'): str,
                                            Optional('metric'): int,
                                            Optional('from'): str,
                                            Optional('table'): str,
                                            Optional('address_family'): str,
                                            Optional('table_id'): str,
                                            Optional('nexthop_in_vrf'): str,
                                        }
                                    }
                                }
                            }
                        },
                    },
                },
                Optional('last_resort'): {
                    Optional('gateway'): str,
                    Optional('to_network'): str,
                },
            },
        }
    }


# ====================================================
#  parser for show route ipv4
# ====================================================
class ShowRouteIpv4(ShowRouteIpv4Schema):
    cli_command = [
        'show route ipv4',
        'show route vrf {vrf} ipv4',
        'show route ipv4 {protocol}',
        'show route vrf {vrf} ipv4 {protocol}',
        'show route ipv4 {route}',
        'show route vrf {vrf} ipv4 {route}'
    ]

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

    protocol_set = {'ospf', 'odr', 'isis', 'eigrp', 'static', 'mobile',
                    'rip', 'lisp', 'nhrp', 'local', 'connected', 'bgp'}

    def cli(self, vrf=None, route=None, protocol=None, output=None):
        
        # Check if argument from device.parse is protocol or route
        if protocol and protocol not in self.protocol_set:
            route = protocol
            protocol = None

        if output is None:
            if vrf and route:
                cmd = self.cli_command[5].format(
                    vrf=vrf,
                    route=route
                )
            elif vrf and protocol:
                cmd = self.cli_command[3].format(
                    vrf=vrf,
                    protocol=protocol
                )
            elif vrf:
                cmd = self.cli_command[1].format(
                    vrf=vrf
                )
            elif protocol:
                cmd = self.cli_command[2].format(
                    protocol=protocol
                )
            elif route:
                cmd = self.cli_command[4].format(
                    route=route
                )
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output
        
        # VRF: VRF501
        # VRF: L:123
        p1 = re.compile(r'^\s*VRF: +(?P<vrf>\S+)$')

        # R    10.1.0.0/8 [120/1] via 10.12.120.1, 1w0d, GigabitEthernet0/0/0/0.120
        # B    10.21.33.33/32 [200/0] via 10.166.13.13, 00:52:31
        # i L2 10.154.219.32/32 [115/100030] via 10.4.1.1, 1d06h, HundredGigE0/0/1/1 (!)
        # S    10.36.3.3/32 [1/0] via 10.2.3.3, 01:51:13, GigabitEthernet0/0/0/1
        # B    10.19.31.31/32 [200/0] via 10.229.11.11, 00:55:14
        # i L1 10.76.23.23/32 [115/11] via 10.2.3.3, 00:52:41, GigabitEthernet0/0/0/1
        # S*   192.168.4.4/10 [111/10] via 172.16.84.11, 1w0d
        # R    10.145.110.10/4 [10/10] via 192.168.10.12, 12:03:42, GigabitEthernet0/0/1/1.1
        # B    10.100.3.160/31 [200/0] via 172.23.6.198 (nexthop in vrf default), 5d13h
        p2 = re.compile(r'^(?P<code1>[\w](\*)*)\s*(?P<code2>\S+)? +(?P<network>\S+) +'
                        r'\[(?P<route_preference>\d+)\/(?P<metric>\d+)\] +via +'
                        r'(?P<next_hop>\S+)( +\(nexthop +in +vrf +\w+\))?,'
                        r'( +(?P<date>[\w:]+),?)?( +(?P<interface>[\w\/\.\-]+))?'
                        r'( +(?P<code3>[\w\*\(\>\)\!]+))?$')

        # [90/15360] via 10.23.90.3, 1w0d, GigabitEthernet0/0/0/1.90
        # [110/2] via 10.1.2.1, 01:50:49, GigabitEthernet0/0/0/3
        p3 = re.compile(r'^\[(?P<route_preference>\d+)\/(?P<metric>\d+)\] +via +'
                        r'(?P<next_hop>\S+),( +(?P<date>[\w:]+))?,? +'
                        r'(?P<interface>[\w\/\.\-]+)$')

        # L    10.16.2.2/32 is directly connected, 3w5d, Loopback0
        # is directly connected, 01:51:13, GigabitEthernet0/0/0/3
        # S    10.4.1.1/32 is directly connected, 01:51:13, GigabitEthernet0/0/0/0
        # S 10.2.2.2/32 is directly connected, 00:06:36, Null0
        p4 = re.compile(r'^((?P<code1>[\w])\s*(?P<code2>\S+)?(\s+'
                        r'(?P<network>\S+)\s+))?(is\s+directly\s+connected,\s+'
                        r'(?P<date>[\w:]+))?,?\s+(?P<interface>[\w\/\.\-]+)?$')

        # Routing entry for 10.151.0.0/24, 1 known subnets
        # Routing entry for 0.0.0.0/0, supernet
        # Routing entry for 192.168.154.0/24
        p5 = re.compile(r'^Routing +entry +for +(?P<network>(?P<ip>[\w\:\.]+)'
                        r'\/(?P<mask>\d+))(?:, +(?P<net>[\w\s]+))?$')
        
        # Known via "connected", distance 0, metric 0 (connected)
        # Known via "eigrp 1", distance 130, metric 10880, type internal
        # Known via "bgp 65161", distance 20, metric 0, candidate default path
        # Known via "ospf 3", distance 110, metric 32001, type extern 1
        p6 = re.compile(r'^Known +via +\"(?P<known_via>[\w ]+)\", +distance +'
                r'(?P<distance>\d+), +metric +(?P<metric>\d+)( \(connected\))?'
                r'(, +type +(?P<type>[\S\s]+))?(, +candidate +default +path)?$')

        # * directly connected, via GigabitEthernet1.120
        p7 = re.compile(r'^(\* +)?directly +connected, via +(?P<interface>\S+)$')
        
        # Route metric is 10880, traffic share count is 1
        p8 = re.compile(r'^Route +metric +is +(?P<metric>\d+)(, +'
                        r'traffic +share +count +is +(?P<share_count>\d+))?$')

        # eigrp/100 (protoid=5, clientid=22)
        p9 = re.compile(r'^(?P<redist_advertiser>\S+) +\(protoid=(?P<protoid>\d+)'
                        r', +clientid=(?P<clientid>\d+)\)$')
        
        # Installed Oct 23 22:09:38.380 for 5d21h
        p10 = re.compile(r'^Installed +(?P<date>[\S\s]+) +for +(?P<for>\S+)$')

        # 10.12.90.1, from 10.12.90.1, via GigabitEthernet0/0/0/0.90
        # 172.23.6.96, from 172.23.15.196
        # 172.25.253.121, from 172.25.253.121, BGP external
        p11 = re.compile(r'^(?P<nexthop>\S+),\s+from\s+(?P<from>\S+)(, '
                         r'+via\s+(?P<interface>\S+))?'
                         r'(, +BGP external)?$')
        
        # R2_xrv#show route ipv4
        # Routing Descriptor Blocks
        # No advertising protos.
        p12 = re.compile(r'^((\S+#)?(show +route))|(Routing +Descriptor +'
                r'Blocks)|(No +advertising +protos\.)|(Redist +Advertisers:)')
        
        # Tag 10584, type internal
        p13 = re.compile(r'^Tag\s+(?P<tag>\d+)\,\s+type\s+(?P<type>\w+)$')

        # Nexthop in Vrf: "default", Table: "default", IPv4 Unicast, Table Id: 0xe0000000
        p14 = re.compile(r'^Nexthop\s+in\s+[V|v]rf\:\s+\"(?P<interface>\w+)\"\, '
                         r'+[T|t]able\:\s+\"(?P<table>\w+)\"\, '
                         r'+(?P<address_family>[\w\s]+)\,\s+[T|t]able '
                         r'+[I|i]d\:\s+(?P<table_id>\S+)$')

        # Gateway of last resort is 172.16.0.88 to network 0.0.0.0
        p15 = re.compile(r'^Gateway +of +last +resort +is '
                         r'+(?P<gateway>(not +set)|\S+)( +to +network '
                         r'+(?P<to_network>\S+))?$')

        # initial variables
        ret_dict = {}
        index = 0
        address_family = 'ipv4'
        if not vrf:
            vrf = 'default'

        for line in out.splitlines():
            line = line.strip()
            
            # R2_xrv#show route ipv4
            # Routing Descriptor Blocks
            # No advertising protos.
            m = p12.match(line)
            if m or not line:
                continue

            # VRF: VRF501
            # VRF: L:123
            m = p1.match(line)
            if m:
                vrf = m.groupdict()['vrf']
                continue
            
            # R    10.1.0.0/8 [120/1] via 10.12.120.1, 1w0d, GigabitEthernet0/0/0/0.120
            m = p2.match(line)
            if m:
                group = m.groupdict()
                code1 = group['code1']
                source_protocol_code = re.split('\*|\(\!\)|\(\>\)', code1)[0].strip()
                for key,val in self.source_protocol_dict.items():
                    if source_protocol_code in val:
                        source_protocol = key
                
                code2 = group['code2']
                if code2:
                    code1 = '{} {}'.format(code1, code2)

                code3 = group['code3']
                if code3:
                    code1 = '{} {}'.format(code1, code3)
                
                network = group['network']
                route_preference = int(group['route_preference'])
                metric = int(group['metric'])
                next_hop = group['next_hop']
                updated = group['date']
                interface = group['interface']

                route_dict = ret_dict.setdefault('vrf', {}). \
                    setdefault(vrf, {}). \
                    setdefault('address_family', {}). \
                    setdefault(address_family, {}). \
                    setdefault('routes', {}). \
                    setdefault(network, {})

                route_dict.update({'route': network})
                route_dict.update({'active': True})
                route_dict.update({'route_preference': route_preference})
                route_dict.update({'metric': metric})
                route_dict.update({'source_protocol': source_protocol})
                route_dict.update({'source_protocol_codes': code1})

                index = 1

                next_hop_list_dict = route_dict.setdefault('next_hop', {}). \
                    setdefault('next_hop_list', {}). \
                    setdefault(index, {})
                
                next_hop_list_dict.update({'index': index})
                next_hop_list_dict.update({'next_hop': next_hop})
                if interface:
                    next_hop_list_dict.update({'outgoing_interface': interface})
                if updated:
                    next_hop_list_dict.update({'updated': updated})
                continue
            
            # [90/15360] via 10.23.90.3, 1w0d, GigabitEthernet0/0/0/1.90
            m = p3.match(line)
            if m:
                group = m.groupdict()
                route_preference = int(group['route_preference'])
                metric = int(group['metric'])
                next_hop = group['next_hop']
                updated = group['date']
                interface = group['interface']
                route_dict.update({'route_preference': route_preference})
                route_dict.update({'metric': metric})
                index += 1

                next_hop_list_dict = route_dict.setdefault('next_hop', {}). \
                    setdefault('next_hop_list', {}). \
                    setdefault(index, {})
                
                next_hop_list_dict.update({'index': index})
                next_hop_list_dict.update({'next_hop': next_hop})
                if interface:
                    next_hop_list_dict.update({'outgoing_interface': interface})
                if updated:
                    next_hop_list_dict.update({'updated': updated})
                continue

            # L    10.16.2.2/32 is directly connected, 3w5d, Loopback0
            #                 is directly connected, 01:51:13, GigabitEthernet0/0/0/3
            # S 10.2.2.2/32 is directly connected, 00:06:36, Null0
            m = p4.match(line)
            if m:
                try:
                    group = m.groupdict()
                    code1 = group.get('code1', None)
                    source_protocol = None
                    network = group.get('network', None)
                    updated = group.get('date', None)
                    interface = group.get('interface', None)

                    if network:
                        route_dict = ret_dict.setdefault('vrf', {}). \
                            setdefault(vrf, {}). \
                            setdefault('address_family', {}). \
                            setdefault(address_family, {}). \
                            setdefault('routes', {}). \
                            setdefault(network, {})

                        route_dict.update({'route': network})
                        route_dict.update({'active': True})
                    
                    if code1:
                        source_protocol_code = re.split('\*|\(\!\)|\(\>\)', code1)[0].strip()
                        for key,val in self.source_protocol_dict.items():
                            if source_protocol_code in val:
                                source_protocol = key
                        
                        code2 = group.get('code2', None)
                        if code2:
                            code1 = '{} {}'.format(code1, code2)

                        if source_protocol:
                            route_dict.update({'source_protocol': source_protocol})
                        route_dict.update({'source_protocol_codes': code1})
                    
                    outgoing_interface_dict = route_dict.setdefault('next_hop', {}). \
                        setdefault('outgoing_interface', {}). \
                        setdefault(interface, {})
                    
                    if interface:
                        outgoing_interface_dict.update({'outgoing_interface': interface})
                    
                    if updated:
                        outgoing_interface_dict.update({'updated': updated})
                except Exception:
                    print('--->'+line)
                continue
            
            # Routing entry for 10.151.0.0/24, 1 known subnets
            # Routing entry for 0.0.0.0/0, supernet
            # Routing entry for 192.168.154.0/24
            m = p5.match(line)
            if m:
                group = m.groupdict()
                network = group['network']
                ip = group['ip']
                mask = group['mask']
                route_dict = ret_dict.setdefault('vrf', {}). \
                    setdefault(vrf, {}). \
                    setdefault('address_family', {}). \
                    setdefault(address_family, {}). \
                    setdefault('routes', {}). \
                    setdefault(network, {})
                route_dict.update({'route': network})
                route_dict.update({'ip': ip})
                route_dict.update({'mask': mask})
                route_dict.update({'active': True})
                continue

            # Known via "static", distance 1, metric 0, candidate default path
            # Known via "eigrp 1", distance 130, metric 10880, type internal
            # Known via "rip", distance 120, metric 2
            # Known via "connected", distance 0, metric 0 (connected)
            # Known via "eigrp 1", distance 130, metric 10880, type internal
            # Known via "bgp 65161", distance 20, metric 0, candidate default path
            # Known via "ospf 3", distance 110, metric 32001, type extern 1
            m = p6.match(line)
            if m:
                group = m.groupdict()
                known_via = group['known_via']
                metric = int(group['metric'])
                distance = int(group['distance'])
                _type = group['type']
                route_dict.update({'known_via': known_via})
                route_dict.update({'metric': metric})
                route_dict.update({'distance': distance})
                if _type:
                    route_dict.update({'type': _type})
                continue

            # * directly connected, via GigabitEthernet1.120
            m = p7.match(line)
            if m:
                group = m.groupdict()
                code1 = group.get('code1', None)
                source_protocol = None
                network = group.get('network', None)
                updated = group.get('date', None)
                interface = group.get('interface', None)

                if network:
                    route_dict = ret_dict.setdefault('vrf', {}). \
                        setdefault(vrf, {}). \
                        setdefault('address_family', {}). \
                        setdefault(address_family, {}). \
                        setdefault('routes', {}). \
                        setdefault(network, {})

                    route_dict.update({'route': network})
                    route_dict.update({'active': True})
                
                if code1:
                    source_protocol_code = re.split('\*|\(\!\)|\(\>\)', code1)[0].strip()
                    for key,val in self.source_protocol_dict.items():
                        if source_protocol_code in val:
                            source_protocol = key
                    
                    code2 = group.get('code2', None)
                    if code2:
                        code1 = '{} {}'.format(code1, code2)
                    route_dict.update({'source_protocol': source_protocol})
                    route_dict.update({'source_protocol_codes': code1})
                
                if interface:
                    outgoing_interface_dict = route_dict.setdefault('next_hop', {}). \
                        setdefault('outgoing_interface', {}). \
                        setdefault(interface, {})
                    outgoing_interface_dict.update({'outgoing_interface': interface})
                
                if updated:
                    outgoing_interface_dict.update({'updated': updated})

            # Route metric is 10880, traffic share count is 1
            m = p8.match(line)
            if m:
                group = m.groupdict()
                metric = int(group['metric'])
                outgoing_interface_dict.update({'metric': metric})
                if group.get('share_count', None):
                    share_count = int(group['share_count'])
                    outgoing_interface_dict.update({'share_count': share_count})
                # outgoing_interface_dict.update({k:v for k,v in group.items() if v})
                continue
            
            # eigrp/100 (protoid=5, clientid=22)
            m = p9.match(line)
            if m:
                group = m.groupdict()
                redist_advertiser = group['redist_advertiser']
                protoid = int(group['protoid'])
                clientid = int(group['clientid'])
                redist_advertiser_dict = route_dict.setdefault('redist_advertisers', {}). \
                                setdefault(redist_advertiser, {})
                redist_advertiser_dict.update({'protoid': protoid})
                redist_advertiser_dict.update({'clientid': clientid})
                continue
            
            # Installed Oct 23 22:09:38.380 for 5d21h
            m = p10.match(line)
            if m:
                group = m.groupdict()
                installed_dict = route_dict.setdefault('installed', {})
                installed_dict.update({k:v for k,v in group.items() if v})
                continue

            # 10.12.90.1, from 10.12.90.1, via GigabitEthernet0/0/0/0.90
            # 172.23.6.96, from 172.23.15.196
            m = p11.match(line)
            if m:
                group = m.groupdict()
                nexthop = group['nexthop']
                _from = group['from']
                interface = group['interface']

                index += 1
                outgoing_interface_dict = route_dict.setdefault('next_hop', {}). \
                    setdefault('next_hop_list', {}). \
                    setdefault(index, {})
                outgoing_interface_dict.update({'index': index})
                if interface:
                    outgoing_interface_dict.update({'outgoing_interface': interface})

                outgoing_interface_dict.update({'from': _from})
                outgoing_interface_dict.update({'next_hop': nexthop})
                continue

            # Tag 10584, type internal
            m13 = p13.match(line)
            if m13:
                group = m13.groupdict()

                route_dict.update({'tag': group['tag']})
                route_dict.update({'type': group['type']})

                continue

            # Nexthop in Vrf: "default", Table: "default", IPv4 Unicast, Table Id: 0xe0000000
            m14 = p14.match(line)
            if m14:
                group = m14.groupdict()
                
                interface = group['interface']
                table = group['table']
                address_family = group['address_family']
                table_id = group['table_id']

                if interface:
                    nexthop_intf_dict = route_dict.setdefault('next_hop', {}).\
                        setdefault('next_hop_list', {}). \
                        setdefault(index, {})

                nexthop_intf_dict.update({'index': index})
                if interface:
                    nexthop_intf_dict.update({'nexthop_in_vrf': interface})
                
                nexthop_intf_dict.update({'table': table})
                nexthop_intf_dict.update({'address_family': address_family})
                nexthop_intf_dict.update({'table_id': table_id})

                continue
            
            # Gateway of last resort is 172.16.0.88 to network 0.0.0.0
            m15 = p15.match(line)
            if m15:
                group = m15.groupdict()
                gw_dict = ret_dict.setdefault('vrf', {}).\
                    setdefault(vrf, {}).\
                    setdefault('last_resort', {})
                gw_dict.update({'gateway': group['gateway']})

                if group['to_network']:
                    gw_dict.update({'to_network': group['to_network']})
        
        return ret_dict


# ====================================================
#  parser for show route ipv6
# ====================================================
class ShowRouteIpv6(ShowRouteIpv4Schema):
    """Parser for :
       show route ipv6
       show route vrf <vrf> ipv6"""
    
    cli_command = [
        'show route ipv6',
        'show route vrf {vrf} ipv6',
        'show route ipv6 {protocol}',
        'show route vrf {vrf} ipv6 {protocol}',
        'show route ipv6 {route}',
        'show route vrf {vrf} ipv6 {route}'
    ]

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
        'application route' : ['a'],
    }


    protocol_set = {'ospf', 'odr', 'isis', 'eigrp', 'static', 'mobile',
                    'rip', 'lisp', 'nhrp', 'local', 'connected', 'bgp'}

    def cli(self, vrf=None, route=None, protocol=None, output=None):
        
        # Check if argument from device.parse is protocol or route
        if protocol and protocol not in self.protocol_set:
            route = protocol
            protocol = None

        if output is None:
            if vrf and route:
                cmd = self.cli_command[5].format(
                    vrf=vrf,
                    route=route
                )
            elif vrf and protocol:
                cmd = self.cli_command[3].format(
                    vrf=vrf,
                    protocol=protocol
                )
            elif vrf:
                cmd = self.cli_command[1].format(
                    vrf=vrf
                )
            elif protocol:
                cmd = self.cli_command[2].format(
                    protocol=protocol
                )
            elif route:
                cmd = self.cli_command[4].format(
                    route=route
                )
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output
        
        # VRF: VRF501
        # VRF: L:123
        p1 = re.compile(r'^\s*VRF: +(?P<vrf>\S+)$')

        # S    2001:1:1:1::1/128
        # L    2001:2:2:2::2/128 is directly connected,
        # i L2 2001:0:10:204:0:33::/126
        # i L1 2001:21:21:21::21/128
        # i*L2 ::/0
        # a*   ::/0
        p2 = re.compile(r'^((?P<code1>[\w](\*)*)(\s*)?(?P<code2>\w+)? '
                        r'+(?P<network>\S+))?( +is +directly +connected\,)?$')

        # [1/0] via 2001:20:1:2::1, 01:52:23, GigabitEthernet0/0/0/0
        # [200/0] via 2001:13:13:13::13, 00:53:22
        # [0/0] via ::, 5w2d
        p3 = re.compile(r'^\[(?P<route_preference>\d+)\/(?P<metric>\d+)\] +'
                r'via +(?P<next_hop>\S+)( +\(nexthop +in +vrf +\w+\))?,'
                r'( +(?P<date>[\w:]+))?,?( +(?P<interface>[\w\/\.\-]+))?$')

        # 01:52:24, Loopback0
        p5 = re.compile(r'^(?P<date>[\w+:]+), +(?P<interface>\S+)$')

        # Routing entry for 2001:1:1:1::1/128, 1 known subnets
        # Routing entry for 2001:1:1:1::1/128, supernet
        # Routing entry for 2001:1:1:1::1/128
        p6 = re.compile(r'^Routing +entry +for +(?P<network>(?P<ip>[\w\:\.]+)'
                        r'\/(?P<mask>\d+))(?:, +(?P<net>[\w\s]+))?$')
        
        # Known via "connected", distance 0, metric 0 (connected)
        # Known via "eigrp 1", distance 130, metric 10880, type internal
        # Known via "bgp 65161", distance 20, metric 0, candidate default path
        p7 = re.compile(r'^Known +via +\"(?P<known_via>[\w ]+)\", +'
                r'distance +(?P<distance>\d+), +metric +(?P<metric>\d+)'
                r'( \(connected\))?(, +type +(?P<type>\S+))?(, +candidate +'
                r'default +path)?$')

        # * directly connected, via GigabitEthernet1.120
        p8 = re.compile(r'^(\* +)?directly +connected, via +(?P<interface>\S+)$')
        
        # Route metric is 10880, traffic share count is 1
        p9 = re.compile(r'^Route +metric +is +(?P<metric>\d+)(, +'
                        r'traffic +share +count +is +(?P<share_count>\d+))?$')

        # eigrp/100 (protoid=5, clientid=22)
        p10 = re.compile(r'^(?P<redist_advertiser>\S+) +\(protoid=(?P<protoid>\d+)'
                        r', +clientid=(?P<clientid>\d+)\)$')
        
        # Installed Oct 23 22:09:38.380 for 5d21h
        p11 = re.compile(r'^Installed +(?P<date>[\S\s]+) +for +(?P<for>\S+)$')

        # fe80::f816:3eff:fe76:b56d, from fe80::f816:3eff:fe76:b56d, via GigabitEthernet0/0/0/0.390
        p12 = re.compile(r'^(?P<nexthop>\S+), from +(?P<from>\S+), '
                        r'+via +(?P<interface>\S+)$')

        # R2_xrv#show route ipv6
        p13 = re.compile(r'^((\S+#)?(show +route))|(Routing +Descriptor +'
                r'Blocks)|(No +advertising +protos\.)|(Redist +Advertisers:)')
        
        # Gateway of last resort is fe80::10ff:fe04:209e to network ::
        # Gateway of last resort is not set
        # Gateway of last resort is 10.50.15.1 to network 0.0.0.0
        p14 = re.compile(r'^Gateway +of +last +resort +is '
                         r'+(?P<gateway>(not +set)|\S+)( +to +network '
                         r'+(?P<to_network>\S+))?$')

        ret_dict = {}
        address_family = 'ipv6'
        index = 0
        if not vrf:
            vrf = 'default'

        for line in out.splitlines():
            line = line.strip()

            # R2_xrv#show route ipv6
            # Routing Descriptor Blocks
            # No advertising protos.
            m = p13.match(line)

            if m or not line:
                continue

            # VRF: VRF501
            m = p1.match(line)
            if m:
                vrf = m.groupdict()['vrf']
                continue

            # S    2001:1:1:1::1/128
            # L    2001:2:2:2::2/128 is directly connected,
            # i L2 2001:0:10:204:0:33::/126
            # i L1 2001:21:21:21::21/128
            # i*L2 ::/0
            # a*   ::/0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                code1 = group['code1']
                source_protocol_code = re.split(r'\*|\(\!\)|\(\>\)', code1)[0].strip()
                for key,val in self.source_protocol_dict.items():
                    if source_protocol_code in val:
                        source_protocol = key
                
                code2 = group['code2']
                if code2:
                    code1 = '{} {}'.format(code1, code2)

                network = group['network']
                route_dict = ret_dict.setdefault('vrf', {}). \
                    setdefault(vrf, {}). \
                    setdefault('address_family', {}). \
                    setdefault(address_family, {}). \
                    setdefault('routes', {}). \
                    setdefault(network, {})

                route_dict.update({'source_protocol': source_protocol})
                route_dict.update({'source_protocol_codes': code1})
                route_dict.update({'route': network})
                route_dict.update({'active': True})
                index = 0
                continue
            
            m = p3.match(line)
            if m:
                group = m.groupdict()
                route_preference = int(group['route_preference'])
                metric = int(group['metric'])
                next_hop = group.get('next_hop', None)
                updated = group.get('date', None)
                interface = group.get('interface', None)
                route_dict.update({'route_preference': route_preference})
                route_dict.update({'metric': metric})
                index += 1

                next_hop_list_dict = route_dict.setdefault('next_hop', {}). \
                    setdefault('next_hop_list', {}). \
                    setdefault(index, {})
                
                next_hop_list_dict.update({'index': index})
                if next_hop:
                    next_hop_list_dict.update({'next_hop': next_hop})
                if interface:
                    next_hop_list_dict.update({'outgoing_interface': interface})
                if updated:
                    next_hop_list_dict.update({'updated': updated})
                continue

            # 01:52:24, Loopback0
            m = p5.match(line)
            if m:
                group = m.groupdict()
                updated = group['date']
                interface = group['interface']
                
                outgoing_interface_dict = route_dict.setdefault('next_hop', {}). \
                    setdefault('outgoing_interface', {}). \
                    setdefault(interface, {})
                outgoing_interface_dict.update({'outgoing_interface': interface})
                outgoing_interface_dict.update({'updated': updated})
                continue
            
            # Routing entry for 2001:1:1:1::1/128, 1 known subnets
            # Routing entry for 2001:1:1:1::1/128, supernet
            # Routing entry for 2001:1:1:1::1/128
            m = p6.match(line)
            if m:
                group = m.groupdict()
                network = group['network']
                ip = group['ip']
                mask = group['mask']
                route_dict = ret_dict.setdefault('vrf', {}). \
                    setdefault(vrf, {}). \
                    setdefault('address_family', {}). \
                    setdefault(address_family, {}). \
                    setdefault('routes', {}). \
                    setdefault(network, {})
                route_dict.update({'route': network})
                route_dict.update({'ip': ip})
                route_dict.update({'mask': mask})
                route_dict.update({'active': True})
                continue

            # Known via "static", distance 1, metric 0, candidate default path
            # Known via "eigrp 1", distance 130, metric 10880, type internal
            # Known via "rip", distance 120, metric 2
            # Known via "connected", distance 0, metric 0 (connected)
            # Known via "eigrp 1", distance 130, metric 10880, type internal
            # Known via "bgp 65161", distance 20, metric 0, candidate default path
            m = p7.match(line)
            if m:
                group = m.groupdict()
                known_via = group['known_via']
                metric = int(group['metric'])
                distance = int(group['distance'])
                _type = group['type']
                route_dict.update({'known_via': known_via})
                route_dict.update({'metric': metric})
                route_dict.update({'distance': distance})
                if _type:
                    route_dict.update({'type': _type})
                continue

            # * directly connected, via GigabitEthernet1.120
            m = p8.match(line)
            if m:
                group = m.groupdict()
                code1 = group.get('code1', None)
                source_protocol = None
                network = group.get('network', None)
                updated = group.get('date', None)
                interface = group.get('interface', None)
                if network:
                    route_dict = ret_dict.setdefault('vrf', {}). \
                        setdefault(vrf, {}). \
                        setdefault('address_family', {}). \
                        setdefault(address_family, {}). \
                        setdefault('routes', {}). \
                        setdefault(network, {})

                    route_dict.update({'route': network})
                    route_dict.update({'active': True})
                
                if code1:
                    source_protocol_code = re.split(r'\*|\(\!\)|\(\>\)', code1)[0].strip()
                    for key,val in self.source_protocol_dict.items():
                        if source_protocol_code in val:
                            source_protocol = key
                    
                    code2 = group.get('code2', None)
                    if code2:
                        code1 = '{} {}'.format(code1, code2)
                    route_dict.update({'source_protocol': source_protocol})
                    route_dict.update({'source_protocol_codes': code1})
                
                outgoing_interface_dict = route_dict.setdefault('next_hop', {}). \
                    setdefault('outgoing_interface', {}). \
                    setdefault(interface, {})
                
                if interface:
                    outgoing_interface_dict.update({'outgoing_interface': interface})
                
                if updated:
                    outgoing_interface_dict.update({'updated': updated})

            # Route metric is 10880, traffic share count is 1
            m = p9.match(line)
            if m:
                group = m.groupdict()
                metric = int(group['metric'])
                outgoing_interface_dict.update({'metric': metric})
                if group.get('share_count', None):
                    share_count = int(group['share_count'])
                    outgoing_interface_dict.update({'share_count': share_count})
                # outgoing_interface_dict.update({k:v for k,v in group.items() if v})
                continue
            
            # eigrp/100 (protoid=5, clientid=22)
            m = p10.match(line)
            if m:
                group = m.groupdict()
                redist_advertiser = group['redist_advertiser']
                protoid = int(group['protoid'])
                clientid = int(group['clientid'])
                redist_advertiser_dict = route_dict.setdefault('redist_advertisers', {}). \
                                setdefault(redist_advertiser, {})
                redist_advertiser_dict.update({'protoid': protoid})
                redist_advertiser_dict.update({'clientid': clientid})
                continue
            
            # Installed Oct 23 22:09:38.380 for 5d21h
            m = p11.match(line)
            if m:
                group = m.groupdict()
                installed_dict = route_dict.setdefault('installed', {})
                installed_dict.update({k:v for k,v in group.items() if v})
                continue
            
            # fe80::f816:3eff:fe76:b56d, from fe80::f816:3eff:fe76:b56d, via GigabitEthernet0/0/0/0.390
            m = p12.match(line)
            if m:
                group = m.groupdict()
                nexthop = group['nexthop']
                _from = group['from']
                interface = group['interface']

                index += 1
                outgoing_interface_dict = route_dict.setdefault('next_hop', {}). \
                    setdefault('next_hop_list', {}). \
                    setdefault(index, {})
                outgoing_interface_dict.update({'index': index})
                outgoing_interface_dict.update({'outgoing_interface': interface})
                outgoing_interface_dict.update({'from': _from})
                outgoing_interface_dict.update({'next_hop': nexthop})
                continue

            # Gateway of last resort is fe80::10ff:fe04:209e to network ::
            # Gateway of last resort is not set
            # Gateway of last resort is 10.50.15.1 to network 0.0.0.0
            m14 = p14.match(line)
            if m14:
                group = m14.groupdict()
                gw_dict = ret_dict.setdefault('vrf', {}).\
                        setdefault(vrf, {}).\
                        setdefault('last_resort', {})
                gw_dict.update({'gateway': group['gateway']})
                
                if group['to_network']:
                    gw_dict.update({'to_network' : group['to_network']})
                
                continue

        return ret_dict
