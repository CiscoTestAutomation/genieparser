'''
show_route.py

'''
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
    Any, \
    Optional


# ====================================================
#  schema for show cef {afi} {prefix} detail
# ====================================================
class ShowCefDetailSchema(MetaParser):
    """ Schema for:
        * show cef {afi} {prefix} detail
    """
    schema = {
        'vrf': {
            Any(): {
                'address_family': {
                    Any(): {
                        'prefix': {
                            Any(): {
                                'LW-LDI-TS': {
                                    'datetime': str,
                                    'via_entries': {
                                        Any(): {
                                            'dependencies': int,
                                            'path': {
                                                'nhid': str,
                                                'path_idx': int,
                                                'path_idx_nh': {
                                                    'local_label_nh': {
                                                        'local_label': int,
                                                        'local_label_nh_address': str,
                                                        'local_label_nh_interface': str,
                                                        'local_label_nh_labels': str
                                                    },
                                                    'path_idx_address': str,
                                                    'path_idx_via': str,
                                                },
                                            },
                                            'via_address': str,
                                            'via_flags': str,
                                        },
                                    },
                                    'load_distribution': {
                                        Any(): {
                                            'address': str,
                                            'hash': int,
                                            'interface': str,
                                            'ok': str,
                                        }
                                    },
                                    'weight_distribution': {
                                        Any(): {
                                            'class': int,
                                            'normalized_weight': int,
                                            'slot': int,
                                            'weight': int,
                                        }
                                    }
                                },
                                'gateway_array': {
                                    'LW-LDI': {
                                        'ptr': str,
                                        'refc': int,
                                        'sh_ldi': str,
                                        'type': int,
                                    },
                                    'backups': int,
                                    'flags': {
                                        'flag_count': int,
                                        'flag_internal': str,
                                        'flag_type': int,
                                    },
                                    'reference_count': int,
                                    'source_lsd': int,
                                    'update': {
                                        'type_time': int,
                                        'updated_at': str,
                                    }
                                },
                                'internal': str,
                                'ldi_update_time': str,
                                'length': int,
                                'precedence': str,
                                'priority': int,
                                'traffic_index': int,
                                'updated': str,
                                'version': int,
                            }
                        }
                    }
                }
            }
        }
    }


class ShowCefDetail(ShowCefDetailSchema):
    """ Parser for:
        * show cef {afi} {prefix} detail
    """

    cli_command = 'show cef {afi} {prefix} detail'

    def cli(self, afi="", prefix="", output=None):

        if not output:
            out = self.device.execute(
                self.cli_command.format(afi=afi, prefix=prefix))
        else:
            out = output

        vrf = 'default'

        # 10.4.16.16/32, version 13285, internal 0x1000001 0x0 (ptr 0x78b55d78) [2], 0x0 (0x78b064d8), 0xa00 (0x7a1a60a8)
        p1 = re.compile(r'^(?P<ip>[\d.\/]+), +version +(?P<version>[\d]+)'
                        ', +internal +(?P<internal>.+)+$')

        # Updated Oct 13 18:18:19.680
        p2 = re.compile(r'^Updated +(?P<updated>[\w\s:.]+)$')

        # Prefix Len 32, traffic index 0, precedence n/a, priority 3
        p3 = re.compile(r'^Prefix +Len +(?P<length>[\d]+), +traffic +index'
                        ' +(?P<traffic_index>[\d]+), +precedence'
                        ' +(?P<precedence>[\S]+), +priority'
                        ' +(?P<priority>[\d]+)$')

        # gateway array (0x78967928) reference count 2, flags 0x8078, source lsd (5), 1 backups
        p4 = re.compile(r'^gateway +array +\((?P<gateway_array>[\w\d]+)\)'
                        ' +reference +count +(?P<reference_count>[\d]+),'
                        ' +flags +(?P<flag_hex>[\w\d]+), +source +lsd'
                        ' +\((?P<source_lsd>[\d]+)\), (?P<backups>[\d]+) +backups$')

        # [3 type 4 flags 0x108441 (0x793d4b28) ext 0x0 (0x0)]
        p5 = re.compile(r'^\[(?P<flag_count>[\d]+) +type +(?P<flag_type>[\d]+)'
                        ' +flags +(?P<flags>[\S\s]+)$')

        # LW-LDI[type=1, refc=1, ptr=0x78b064d8, sh-ldi=0x793d4b28]
        p6 = re.compile(r'^LW-LDI\[type=(?P<type>[\d]+),'
                        ' +refc=(?P<refc>[\d]+), +ptr=(?P<ptr>[\w]+),'
                        ' +sh-ldi=(?P<sh_ldi>[\w]+)\]$')

        # gateway array update type-time 1 Oct 13 18:18:19.680
        p7 = re.compile(r'^gateway +array +update +type-time'
                        ' +(?P<type_time>[\d]+) +(?P<updated_at>[\w\s:.]+)$')

        # LDI Update time Oct 13 18:18:19.691
        p8 = re.compile(r'^LDI +Update +time +(?P<ldi_update_time>[\w\s:.]+)$')

        # LW-LDI-TS Oct 13 18:18:19.691
        p9 = re.compile(r'^LW-LDI-TS +(?P<datetime>[\w\s:.]+)$')

        # via 10.55.0.2/32, 4 dependencies, recursive [flags 0x0]
        # via 10.1.15.2/32, 4 dependencies, recursive [flags 0x0]
        p10 = re.compile(r'^via +(?P<via>[\S]+), +(?P<dependencies>[\w]{1,})'
                         ' +dependencies, +(?P<via_flags>[\w]+)'
                         ' +\[([\S\s]+)\]$')

        # path-idx 0 NHID 0x0 [0x78b4cbf8 0x0]
        # path-idx 1 NHID 0x0 [0x78b4fbf8 0x0]
        p11 = re.compile(r'^path-idx +(?P<idx>[\w]+) +NHID +(?P<nhid>[\S]+)'
                         ' +\[(?P<nhid_hex>[\w\s]+)\]$')

        # next hop 10.55.0.2/32 via 10.55.0.2/32
        # next hop 10.1.15.2/32 via 10.1.15.2/32
        p12 = re.compile(r'^next +hop +(?P<path_idx_address>[\S]+)'
                         ' +via +(?P<path_idx_via>[\S]+)$')

        # local label 24006
        p13 = re.compile(r'^local +label +(?P<local_label>[\d]+)$')

        # next hop 10.55.0.2/32 Te0/4/0/15.1 labels imposed {None}
        # next hop 10.1.15.2/32 Te0/3/0/15.16 labels imposed {None}
        p14 = re.compile(r'^next +hop +(?P<address>[\S]+)'
                         ' +(?P<interface>[\S]+) +labels'
                         ' +imposed +\{(?P<labels>[\S]+)\}')

        # Weight distribution:
        p15 = re.compile(r'^Weight +distribution:$')

        # slot 0, weight 1, normalized_weight 1, class 0
        # slot 31, weight 1, normalized_weight 1, class 0
        p16 = re.compile(r'^slot +(?P<slot>[\d]+), +weight'
                         ' +(?P<weight>[\d]+), +normalized_weight'
                         ' +(?P<normalized_weight>[\d]+), +class'
                         ' +(?P<class>[\d]+)$')

        # Load distribution: 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 (refcount 3)
        p17 = re.compile(r'^Load +distribution: +'
                         '(?P<distribution>[\d\s]+) +'
                         '\(refcount (?P<refcount>[\d]+)\)$')

        # Hash  OK  Interface                 Address
        # 0     Y   recursive                 10.55.0.2
        # 31    Y   recursive                 10.1.15.2
        p18 = re.compile(r'^(?P<hash>[\d]+)\s+(?P<ok>[Y|N])\s+(?P<interface>[\w]+)\s+(?P<address>[\S]+)$')

        result_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # 10.4.16.16/32, version 13285, internal 0x1000001 0x0 (ptr 0x78b55d78) [2], 0x0 (0x78b064d8), 0xa00 (0x7a1a60a8)
            m = p1.match(line)
            if m:
                group = m.groupdict()
                prefix_dict = result_dict.\
                    setdefault('vrf', {}).\
                    setdefault(vrf, {}).\
                    setdefault('address_family', {}).\
                    setdefault(afi, {}).\
                    setdefault('prefix', {}).\
                    setdefault(group['ip'], {})

                prefix_dict.update({
                    'version': int(group['version']),
                    'internal': group['internal'],
                })
                continue

            # Updated Oct 13 18:18:19.680
            m = p2.match(line)
            if m:
                group = m.groupdict()
                prefix_dict.update(
                    {'updated': group['updated']})
                continue

            # Prefix Len 32, traffic index 0, precedence n/a, priority 3
            m = p3.match(line)
            if m:
                group = m.groupdict()
                prefix_dict.update({
                    'length': int(group['length']),
                    'traffic_index': int(group['traffic_index']),
                    'precedence': group['precedence'],
                    'priority': int(group['priority']),
                })
                continue

            # gateway array (0x78967928) reference count 2, flags 0x8078, source lsd (5), 1 backups
            m = p4.match(line)
            if m:
                group = m.groupdict()
                gateway_dict = prefix_dict.\
                    setdefault('gateway_array', {})

                gateway_dict.update({
                    'reference_count': int(group['reference_count']),
                    'source_lsd': int(group['source_lsd']),
                    'backups': int(group['backups']),
                })

                flags_dict = gateway_dict.setdefault('flags', {})
                continue

            # [3 type 4 flags 0x108441 (0x793d4b28) ext 0x0 (0x0)]
            m = p5.match(line)
            if m:
                group = m.groupdict()
                flags_dict.update({
                    'flag_count': int(group['flag_count']),
                    'flag_type': int(group['flag_type']),
                    'flag_internal': group['flags']
                })
                continue

            # LW-LDI[type=1, refc=1, ptr=0x78b064d8, sh-ldi=0x793d4b28]
            m = p6.match(line)
            if m:
                group = m.groupdict()
                lw_ldi_dict = gateway_dict.\
                    setdefault('LW-LDI', {})

                lw_ldi_dict.update({
                    'type': int(group['type']),
                    'refc': int(group['refc']),
                    'ptr': group['ptr'],
                    'sh_ldi': group['sh_ldi'],
                })
                continue

            # gateway array update type-time 1 Oct 13 18:18:19.680
            m = p7.match(line)
            if m:
                group = m.groupdict()
                gateway_update_dict = gateway_dict.\
                    setdefault('update', {})

                gateway_update_dict.update({
                    'type_time': int(group['type_time']),
                    'updated_at': group['updated_at']
                })
                continue

            # LDI Update time Oct 13 18:18:19.691
            m = p8.match(line)
            if m:
                group = m.groupdict()
                prefix_dict.update({
                    'ldi_update_time': group['ldi_update_time']
                })
                continue

            # LW-LDI-TS Oct 13 18:18:19.691
            m = p9.match(line)
            if m:
                group = m.groupdict()
                lw_ldi_ts_dict = prefix_dict.\
                    setdefault('LW-LDI-TS', {})
                lw_ldi_ts_dict.update({
                    'datetime': group['datetime']
                })
                entries_dict = lw_ldi_ts_dict.\
                    setdefault('via_entries', {})
                entries_id = 0
                continue

            # via 10.55.0.2/32, 4 dependencies, recursive [flags 0x0]
            m = p10.match(line)
            if m:
                group = m.groupdict()
                via_dict = {
                    'via_address': group['via'],
                    'dependencies': int(group['dependencies']),
                    'via_flags': group['via_flags']
                }
                entries_dict.update({str(entries_id): via_dict})
                entries_id += 1
                continue

            # path-idx 0 NHID 0x0 [0x78b4cbf8 0x0]
            m = p11.match(line)
            if m:
                group = m.groupdict()
                path_dict = {
                    'path_idx': int(group['idx']),
                    'nhid': group['nhid']
                }
                via_dict.update({'path': path_dict})
                continue

            # next hop 10.55.0.2/32 via 10.55.0.2/32
            m = p12.match(line)
            if m:
                group = m.groupdict()
                path_nh_dict = path_dict.\
                    setdefault('path_idx_nh', {})
                path_nh_dict.update({k: v for k, v in group.items()})
                continue

            # local label 24006
            m = p13.match(line)
            if m:
                group = m.groupdict()
                local_label_dict = path_nh_dict.\
                    setdefault('local_label_nh', {})
                local_label_dict.update({
                    'local_label': int(group['local_label'])
                })
                continue

            # next hop 10.55.0.2/32 Te0/4/0/15.1 labels imposed {None}
            m = p14.match(line)
            if m:
                group = m.groupdict()
                local_label_dict.update(
                    {f'local_label_nh_{k}': v for k, v in group.items()})
                continue

            # Weight distribution:
            m = p15.match(line)
            if m:
                weight_dict = lw_ldi_ts_dict.\
                    setdefault('weight_distribution', {})
                continue

            # slot 0, weight 1, normalized_weight 1, class 0
            m = p16.match(line)
            if m:
                group = m.groupdict()
                slot_dict = {k: int(v) for k, v in group.items()}
                weight_dict.update({group['slot']: slot_dict})
                continue

            # Load distribution: 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 (refcount 3)
            m = p17.match(line)
            if m:
                load_dict = lw_ldi_ts_dict.\
                    setdefault('load_distribution', {})
                continue

            m = p18.match(line)
            if m:

                group = m.groupdict()
                hash_dict = {
                    'hash': int(group['hash']),
                    'ok': group['ok'],
                    'interface': group['interface'],
                    'address': group['address'],
                }
                load_dict.update({group['hash']: hash_dict})
                continue

        return result_dict


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
                                Optional('next_hop'): {
                                    Optional('outgoing_interface'): {
                                        Any(): {
                                            'outgoing_interface': str,
                                            Optional('updated'): str,
                                            Optional('metric'): int,
                                        }
                                    },
                                    Optional('next_hop_list'): {
                                        int: { # index
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
        # [110/2] via 10.1.3.1, 3w3d
        p3 = re.compile(r'^\[(?P<route_preference>\d+)\/(?P<metric>\d+)\] +'
                        r'via +(?P<next_hop>\S+)( +\(nexthop +in +vrf +\w+\))?,'
                        r'( +(?P<date>[\w:]+))?,?( +(?P<interface>[\w\/\.\-]+))?$')

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
        # Known via "isis RAN", distance 115, metric 101, candidate default path, type level-2
        p6 = re.compile(r'^Known +via +"(?P<known_via>[\w ]+)", +distance +(?P<distance>\d+), +metric +(?P<metric>\d+)'
                        r'( \(connected\))?(, +candidate +default +path)?(, +type +(?P<type>.+))?$')

        # * directly connected, via GigabitEthernet1.120
        p7 = re.compile(r'^(\* +)?directly +connected, via +(?P<interface>\S+)$')
        
        # Route metric is 10880, traffic share count is 1
        # Route metric is 0, Wt is 1
        p8 = re.compile(r'^Route +metric +is +(?P<metric>\d+)(, +'
                        r'traffic +share +count +is +(?P<share_count>\d+))?'
                        r'(, +Wt +is +\d+)?$')

        # eigrp/100 (protoid=5, clientid=22)
        p9 = re.compile(r'^(?P<redist_advertiser>\S+) +\(protoid=(?P<protoid>\d+)'
                        r', +clientid=(?P<clientid>\d+)\)$')
        
        # Installed Oct 23 22:09:38.380 for 5d21h
        p10 = re.compile(r'^Installed +(?P<date>[\S\s]+) +for +(?P<for>\S+)$')

        # 10.12.90.1, from 10.12.90.1, via GigabitEthernet0/0/0/0.90
        # 172.23.6.96, from 172.23.15.196
        # 172.25.253.121, from 172.25.253.121, BGP external
        # 2001:10::1, via GigabitEthernet0/0/0/0
        p11 = re.compile(r'^(?P<nexthop>\S+)(,\s+from\s+(?P<from>\S+))?(, '
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
                    setdefault(int(index), {})
                
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
                    setdefault(int(index), {})
                
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
            # Known via "isis RAN", distance 115, metric 101, candidate default path, type level-2
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
                    setdefault(int(index), {})
                outgoing_interface_dict.update({'index': index})
                if interface:
                    outgoing_interface_dict.update({'outgoing_interface': interface})
                if _from:
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
                        setdefault(int(index), {})

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
        'application route': ['a'],
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
        # S    2001:1:1:a::1/128
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
        # Routing entry for 2001:1:1:a::1/128
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
                        r'traffic +share +count +is +(?P<share_count>\d+))?'
                        r'(, +Wt +is +\d+)?$')

        # eigrp/100 (protoid=5, clientid=22)
        p10 = re.compile(r'^(?P<redist_advertiser>\S+) +\(protoid=(?P<protoid>\d+)'
                         r', +clientid=(?P<clientid>\d+)\)$')

        # Installed Oct 23 22:09:38.380 for 5d21h
        p11 = re.compile(r'^Installed +(?P<date>[\S\s]+) +for +(?P<for>\S+)$')

        # fe80::f816:3eff:fe76:b56d, from fe80::f816:3eff:fe76:b56d, via GigabitEthernet0/0/0/0.390
        p12 = re.compile(r'^(?P<nexthop>\S+)(, from +(?P<from>\S+))?, '
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
            # S    2001:1:1:a::1/128
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

            # [1/0] via 2001:20:1:2::1, 01:52:23, GigabitEthernet0/0/0/0
            # [200/0] via 2001:13:13:13::13, 00:53:22
            # [0/0] via ::, 5w2d
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
                    setdefault(int(index), {})

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
            # Routing entry for 2001:1:1:a::1/128
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
                    outgoing_interface_dict.update(
                        {'outgoing_interface': interface})

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
                    outgoing_interface_dict.update(
                        {'share_count': share_count})
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
                    setdefault(int(index), {})
                outgoing_interface_dict.update({'index': index})
                outgoing_interface_dict.update({'outgoing_interface': interface})
                if _from:
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


# ====================================================
#  schema for show route summary
# ====================================================
class ShowRouteAllSummarySchema(MetaParser):
    """Schema for :
       show route afi-all safi-all summary
       show route vrf all afi-all safi-all summary
       show route vrf <vrf> afi-all safi-all summary"""

    schema = {
        'vrf': {
            Any(): {
                'address_family': {
                    Any(): {
                        'total_route_source': {
                            'routes': int,
                            'backup': int,
                            'deleted': int,
                            'memory_bytes': int,
                        },
                        'route_source': {
                            Any(): {
                                Any(): {
                                    'routes': int,
                                    'backup': int,
                                    'deleted': int,
                                    'memory_bytes': int,
                                },
                                Optional('routes'): int,
                                Optional('backup'): int,
                                Optional('deleted'): int,
                                Optional('memory_bytes'): int,
                            },
                        }
                    },
                }
            },
        }
    }


# ====================================================
#  parser for show route summary
# ====================================================
class ShowRouteAllSummary(ShowRouteAllSummarySchema):
    """Parser for :
       show route afi-all safi-all summary
       show route vrf all afi-all safi-all summary
       show route vrf <vrf> afi-all safi-all summary"""

    cli_command = [
        'show route afi-all safi-all summary',
        'show route vrf {vrf} afi-all safi-all summary'
    ]

    def cli(self, vrf=None, output=None):
        if output is None:
            if vrf:
                cmd = self.cli_command[1].format(vrf=vrf)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        # VRF: VRF_NAME
        p1 = re.compile(r'^VRF: (?P<vrf>.*)')
        # IPv4 Unicast:
        p2 = re.compile(r'(?P<address_family>^IPv.*)+:')
        # connected                        0          0          0           0
        p3 = re.compile(
            r'^(?P<protocol>[a-zA-Z0-9(\-|\_)]+) +(?P<instance>[a-zA-Z0-9\.(\-|\_)]+)* * +('
            r'?P<routes>\d+) +(?P<backup>\d+) +(?P<deleted>\d+) +(?P<memory_bytes>\d+)')

        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            if vrf == 'all':
                # VRF: VRF_NAME
                m = p1.match(line)
                if m:
                    vrf_temp = m.groupdict()['vrf']
                    vrf_dict = ret_dict.setdefault('vrf',{}).setdefault(vrf_temp, {})
                    continue

            # IPv4 Unicast:
            m = p2.match(line)
            if m:
                if vrf is None:
                    vrf = 'default'
                    vrf_dict = ret_dict.setdefault('vrf',{}).setdefault(vrf, {})
                elif vrf != 'all':
                    vrf_dict = ret_dict.setdefault('vrf',{}).setdefault(vrf, {})
                addrs_fam = m.groupdict()['address_family']
                addrs_fam_dict = vrf_dict.setdefault('address_family', {}).setdefault(addrs_fam, {})
                vrf_rs_dict = addrs_fam_dict.setdefault('route_source', {})
            # connected                        0          0          0           0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                protocol = group.pop('protocol')
                instance = group.pop('instance')
                if protocol == 'Total':
                    protocol_dict = addrs_fam_dict.setdefault('total_route_source', {})
                else:
                    protocol_dict = vrf_rs_dict.setdefault(protocol, {})
                if instance is not None:
                    inst_dict = protocol_dict.setdefault(instance, {})
                    inst_dict.update({k:int(v) for k, v in group.items() if v is not None})
                else:
                    group = {k: int(v) for k, v in group.items() if v is not None}
                    protocol_dict.update(group)
                continue

        return ret_dict
