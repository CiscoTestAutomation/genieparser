'''show_topology.py

IOSXE parsers for the following show commands:
   * show topology
   * show topology all
   * show topology detail all
   * show topology detail {ipv4 | ipv6} all
   * show topology detail {ipv4 | ipv6} topo <topo_name>
   * show topology detail {ipv4 | ipv6} multicast all
   * show topology detail {ipv4 | ipv6} multicast topo {topo_name}
   * show topology detail vrf {vrf} all
   * show topology detail vrf {vrf} {ipv4 | ipv6} all
   * show topology detail vrf {vrf} {ipv4 | ipv6} topo <topo_name>
   * show topology detail vrf {vrf} {ipv4 | ipv6} {multicast} all
   * show topology detail vrf {vrf} {address_family} {multicast} topo {topo_name}
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional, ListOf


class ShowTopologySchema(MetaParser):
    '''Schema for
          * show topology
          * show topology detail {ipv4 | ipv6} all
          * show topology detail {ipv4 | ipv6} topo <topo_name>
          * show topology detail {ipv4 | ipv6} multicast all
          * show topology detail {ipv4 | ipv6} multicast topo {topo_name}
          * show topology detail vrf {vrf} {ipv4 | ipv6} all
          * show topology detail vrf {vrf} {ipv4 | ipv6} topo {topo_name}
          * show topology detail vrf {vrf} {ipv4 | ipv6} multicast all
          * show topology detail vrf {vrf} {ipv4 | ipv6} multicast topo {topo_name}
    '''

    schema = {
        'topologies': {
            Any(): {                                           # Topology name
                'address_families': {
                    Any(): {                                   # Address family
                        'vrfs': {
                            Any(): {                           # VRF name
                                'state': str,
                                Optional('topo_id'): str,
                                Optional('topo_flags'): str,
                                Optional('vrf_id'): str,
                                Optional('is_ivrf'): bool,
                                Optional('cef_forwarding'): str,
                                Optional('lock_count'): int,
                                Optional('user_lock_count'): int,
                                Optional('fallback'): bool,
                                Optional('topo_events'): str,
                                Optional('all_interfaces'): bool,
                                Optional('mcast_multitopology'): bool,
                                Optional('use_topo_afi'): str,
                                Optional('use_topo_name'): str,
                                Optional('used_by'): ListOf({
                                    Optional('used_by_topo_afi'): str,
                                    Optional('used_by_topo_name'): str
                                }),
                                Optional('max_route_limit'): int,
                                Optional('warn_limit_percent'): int,
                                Optional('warn_limit'): int,
                                Optional('threshold_percent'): int,
                                Optional('threshold'): int,
                                Optional('topo_deleted'): bool,
                                Optional('is_replicated'): bool,
                                Optional('rpl_routes'): ListOf({
                                    Optional('source_vrf'): str,
                                    Optional('safi'): str,
                                    Optional('rpl_topo'): str,
                                    Optional('protocol'): str,
                                    Optional('router_id'): str,
                                    Optional('route_map_name'): str,
                                    Optional('src_topo_fwdref'): bool
                                }),
                                Optional('assoc_interfaces'): ListOf({
                                    Optional('if_name'): str,
                                    Optional('oper_state'): str,
                                    Optional('upstream'): bool
                                })
                            }
                        }
                    }
                }
            }
        }
    }


class ShowTopology(ShowTopologySchema):
    """ Parser for:
          show topology
    """
    cli_command = ['show topology']

    def cli(self, output=None):
        cmd = self.cli_command[0]

        if output is None:
            out = self.device.execute(cmd)
        else:
            out = output

        ret_dict = {}
        afi_dict = {}
        vrf_dict = {}

        # Topology                 Address Family   Associated VRF   State
        # base                     ipv4             default          UP
        # t1                       ipv4             default          UP
        # base                     ipv4             foo              UP
        # base                     ipv4 __Platform_iVRF:_ID00_       UP
        # base                     ipv6             default          DOWN
        # base                     ipv4 multicast   default          DOWN
        # base                     ipv4 multicast   foo              DOWN
        # base                     ipv6 multicast   default          DOWN
        p1 = re.compile(r'^(?P<topo_name>\S+)\s+'
                        r'(?P<afi>ipv[46]|ipv[46] multicast)\s+'
                        r'(?P<vrf_name>[\w\-\_\:\.]+)\s+'
                        r'(?P<topo_state>UP|DOWN)$')

        # Topology: base
        #   Topology ID = 0x0, topo_flags = 0x15
        #   Address-family: ipv4
        #   Associated VPN VRF is default
        #   <...>
        #   Associated VPN VRF is __Platform_iVRF:_ID00_
        #   Topology is in a private internal VRF.
        #   Topology state is UP
        #   <...>
        p1_1 = re.compile(r'^Topology: +(?P<topo_name>\S+)$')
        p1_1_1 = re.compile(r'^Topology +ID += +(?P<topo_id>0x[0-9a-fA-F]+),'
                            r' +topo_flags += +(?P<topo_flags>0x[0-9a-fA-F]+)$')

        p1_2 = re.compile(r'^Address-family: +'
                          '(?P<afi>ipv[46]|ipv[46] multicast)$')
        p1_3 = re.compile(r'^Associated VPN VRF is +'
                          r'(?P<vrf_name>[\w\-\_\:\.]+)[^\w]*(VRF ID)*[^\w]*(?P<vrf_id>0x[0-9a-fA-F]+)*$')
        p1_4 = re.compile(r'^(?P<is_ivrf>Topology is in a private internal VRF)[^\w]*$')
        p1_5 = re.compile(r'^Topology state is +(?P<topo_state>UP|DOWN)$')

        p2 = re.compile(r'^Topology CEF forwarding is +'
                        r'(?P<cef_forwarding>enabled|disabled)$')

        p3 = re.compile(r'^(?P<fallback>Topology fallback is enabled)[^\w]*$')

        #   Topology internal lock count = 1
        p4_1 = re.compile(r'^Topology internal lock count[^\w]+'
                          r'(?P<lock_count>[0-9]+)$')
        p4_2 = re.compile(r'^Topology total user lock count[^\w]*(?P<user_lock_count>[0-9]+)$')

        #   Multicast multi-topology mode is enabled.
        p5_1 = re.compile(r'^(?P<mcast_multitopology>Multicast multi-topology mode is enabled)[^\w]*$')
        # Use topology: ipv4 topology foo
        p5_2 = re.compile(r'^Use topology[^\w]* +'
                          r'(?P<use_topo_afi>ipv[46]|ipv[46] multicast) +topology +(?P<use_topo_name>\S+)$')
        # Used by topologies:
        #   ipv4 multicast topology base
        #   ipv4 multicast topology test
        p5_3 = re.compile(r'^(?P<used_by_topo_afi>ipv[46]|ipv[46] multicast) +'
                          r'topology +(?P<used_by_topo_name>\S+)[^\w]*$')

        #   Event queue is not empty, topology has events(0x1122)
        p6 = re.compile(r'^Event queue is not empty, topology has events.*'
                        r'(?P<topo_events>0x[0-9a-fA-F]+).*$')

        #   Topology maximum route limit 100, warning limit 7% (7)
        #         reinstall threshold 15% (11)
        #   <...>
        #   Topology maximum route warning limit 789
        p7_1 = re.compile(r'^Topology maximum route limit +'
                          r'(?P<max_route_limit>\d+)[^\w]*'
                          r' +warning limit +(?P<warn_limit_percent>\d+)% +'
                          r'[^\w]*(?P<warn_limit>\d+)[^\w]*$')
        p7_2 = re.compile(r'^reinstall threshold +(?P<threshold_percent>\d+)% +'
                          r'[^\w]*(?P<threshold>\d+)[^\w]*$')
        p7_3 = re.compile(r'^Topology maximum route warning limit +(?P<warn_limit>\d+)$')

        #   Associated interfaces:
        #     GigabitEthernet1, operation state: UP
        #     GigabitEthernet2, operation state: UP
        #     Tunnel4, operation state: DOWN, Upstream
        p8_1 = re.compile(r'^(?P<if_name>[\w\s./-:]+)[^\w]*'
                          r'operation state[^\w]*(?P<oper_state>UP|DOWN)'
                          r'[^\w]*(?P<upstream>(Upstream)*)$')
        p8_2 = re.compile(r'^(?P<all_interfaces>Topology is enabled on all interfaces)[^\w]*$')

        p9 = re.compile(r'^(?P<topo_deleted>Topology is being deleted)[^\w]*$')

        # Route Replication Enabled:
        #   from unicast static
        #   from unicast ospf 11
        #   from unicast topology test static
        #   from vrf foo unicast connected
        #   from vrf global unicast connected route-map rm1
        #   from vrf v1 unicast topology t1 bgp 65001
        #   from vrf bar unicast bgp 11.12
        #   from vrf vrf-a unicast isis tag123
        #   from vrf global unicast ospfv3 777
        #   from vrf test unicast connected route-map rm1 (Source topology missing)
        p10_1 = re.compile(r'^(?P<is_replicated>Route Replication Enabled)[^\w]*$')
        p10_2 = re.compile(r'^from +(vrf +(?P<source_vrf>[\w\-\_\:\.]+))?'
                           r' *(?P<safi>unicast|multicast)?'
                           r'( +topology +(?P<rpl_topo>\w+))?'
                           r' +(?P<protocol>all|static|connected|ospf|bgp|eigrp|isis|mobile|rip)'
                           r' *(?P<router_id>[\w\-\_\:\.]+)?'
                           r'( +route-map +(?P<route_map_name>[\w\-\_\:\.]+))?'
                           r'(?P<src_topo_fwdref> +\(Source topology missing\)[^\w]*?)?$')

        for line in out.splitlines():
            line = line.strip()

            # base                     ipv4             default          UP
            # t1                       ipv4 multicast   default          DOWN
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                ret_dict.setdefault(
                    'topologies', {}).setdefault(
                        groups['topo_name'], {}).setdefault(
                            'address_families', {}).setdefault(
                                groups['afi'], {}).setdefault(
                                    'vrfs', {}).setdefault(
                                        groups['vrf_name'],{
                                            'state': groups['topo_state']})
                continue

            # Topology: base
            m = p1_1.match(line)
            if m:
                attr_dict = {}
                afi_dict = \
                    ret_dict.setdefault(
                        'topologies', {}).setdefault(
                            m.groupdict()['topo_name'],{}).setdefault(
                                'address_families', {})
                continue

            # Address-family: ipv4
            # Address-family: ipv6 multicast
            m = p1_2.match(line)
            if m:
                vrf_dict = \
                    afi_dict.setdefault(
                        m.groupdict()['afi'],{}).setdefault('vrfs', {})
                continue

            # Associated VPN VRF is foo
            m = p1_3.match(line)
            if m:
                vrf_dict.update({m.groupdict()['vrf_name']: attr_dict})
                if m.groupdict()['vrf_id']:
                    attr_dict['vrf_id'] = m.groupdict()['vrf_id']
                continue

            # Topology is in a private internal VRF
            m = p1_4.match(line)
            if m:
                attr_dict['is_ivrf'] = True
                continue

            # Topology state is UP
            m = p1_5.match(line)
            if m:
                attr_dict.update({'state': m.groupdict()['topo_state']})
                continue

            # Topology ID = 0x0, topo_flags = 0x15
            m = p1_1_1.match(line)
            if m:
                attr_dict['topo_id'] = m.groupdict()['topo_id']
                attr_dict['topo_flags'] = m.groupdict()['topo_flags']
                continue

            # Topology CEF forwarding is enabled
            # Topology CEF forwarding is disabled
            m = p2.match(line)
            if m:
                attr_dict['cef_forwarding'] = m.groupdict()['cef_forwarding']
                continue

            # Topology fallback is enabled
            m = p3.match(line)
            if m:
                attr_dict['fallback'] = True
                continue

            # Topology internal lock count = 2
            m = p4_1.match(line)
            if m:
                attr_dict['lock_count'] = int(m.groupdict()['lock_count'])
                continue

            # Topology total user lock count: 0
            m = p4_2.match(line)
            if m:
                attr_dict['user_lock_count'] = \
                    int(m.groupdict()['user_lock_count'])
                continue

            # Multicast multi-topology mode is enabled
            m = p5_1.match(line)
            if m:
                attr_dict['mcast_multitopology'] = True
                continue

            # Use topology: ipv4 topology t1
            # Use topology: ipv6 topology foo
            m = p5_2.match(line)
            if m:
                attr_dict['use_topo_afi'] = m.groupdict()['use_topo_afi']
                attr_dict['use_topo_name'] = m.groupdict()['use_topo_name']
                continue

            # ipv4 multicast topology base
            # ipv4 multicast topology test
            m = p5_3.match(line)
            if m:
                used_by_topos_list = attr_dict.setdefault('used_by', [])
                used_by_topos_list.append(
                    {'used_by_topo_afi': m.groupdict()['used_by_topo_afi'],
                     'used_by_topo_name': m.groupdict()['used_by_topo_name']})
                continue

            # Event queue is not empty, topology has events(0x1122)
            m = p6.match(line)
            if m:
                attr_dict['topo_events'] = m.groupdict()['topo_events']
                continue

            # Topology maximum route limit 100, warning limit 7% (7)
            m = p7_1.match(line)
            if m:
                attr_dict['max_route_limit'] = \
                    int(m.groupdict()['max_route_limit'])
                attr_dict['warn_limit_percent'] = \
                    int(m.groupdict()['warn_limit_percent'])
                attr_dict['warn_limit'] = int(m.groupdict()['warn_limit'])
                continue

            # reinstall threshold 15% (11)
            m = p7_2.match(line)
            if m:
                attr_dict['threshold_percent'] = \
                    int(m.groupdict()['threshold_percent'])
                attr_dict['threshold'] = int(m.groupdict()['threshold'])
                continue

            # Topology maximum route warning limit 789
            m = p7_3.match(line)
            if m:
                attr_dict['warn_limit'] = int(m.groupdict()['warn_limit'])
                continue

            # GigabitEthernet2, operation state: UP
            # Tunnel4, operation state: DOWN, Upstream
            m = p8_1.match(line)
            if m:
                is_upstream = False
                if m.groupdict()['upstream']:
                    is_upstream = True
                if_list = attr_dict.setdefault('assoc_interfaces', [])
                if_list.append({'if_name': m.groupdict()['if_name'],
                                'oper_state': m.groupdict()['oper_state'],
                                'upstream': is_upstream})
                continue

            # Topology is enabled on all interfaces
            m = p8_2.match(line)
            if m:
                attr_dict['all_interfaces'] = True
                continue

            # Topology is being deleted
            m = p9.match(line)
            if m:
                attr_dict['topo_deleted'] = True
                continue

            # Route Replication Enabled:
            m = p10_1.match(line)
            if m:
                attr_dict['is_replicated'] = True
                continue

            # from unicast static
            # from unicast topology test static
            # from vrf foo unicast connected
            # from vrf global unicast connected route-map rm1
            # from vrf v1 unicast topology t1 bgp 65001
            # from vrf bar unicast bgp 11.12
            # from vrf vrf-a unicast isis tag123
            # from vrf test unicast connected route-map rm1 (Source topology missing)
            m = p10_2.match(line)
            if m:
                gd = m.groupdict()

                source_vrf = gd['source_vrf'] if gd['source_vrf'] else ''
                safi = gd['safi'] if gd['safi'] else 'unicast'
                rpl_topo = gd['rpl_topo'] if gd['rpl_topo'] else ''
                router_id = gd['router_id'] if gd['router_id'] else ''
                route_map_name = \
                    gd['route_map_name'] if gd['route_map_name'] else ''
                src_topo_fwdref = True if gd['src_topo_fwdref'] else False

                rpl_routes_list = attr_dict.setdefault('rpl_routes', [])
                rpl_routes_list.append({'source_vrf': source_vrf,
                                        'safi': safi,
                                        'rpl_topo': rpl_topo,
                                        'protocol': m.groupdict()['protocol'],
                                        'router_id': router_id,
                                        'route_map_name': route_map_name,
                                        'src_topo_fwdref': src_topo_fwdref
                                        })
                continue

        return ret_dict


class ShowTopologyAll(ShowTopology):
    """ Parser for:
          show topology all
    """
    cli_command = 'show topology all'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        return super().cli(output=out)


class ShowTopologyDetailAll(ShowTopology):
    """ Parser for:
          show topology detail all
    """
    cli_command = 'show topology detail all'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        return super().cli(output=out)


class ShowTopologyDetailAfi(ShowTopology):
    """ Parser for:
          show topology detail {address_family} all
          show topology detail {address_family} topo {topo_name}
          show topology detail {address_family} {multicast} all
          show topology detail {address_family} {multicast} topo {topo_name}
    """
    cli_command = [
        'show topology detail {address_family} all',
        'show topology detail {address_family} topo {topo_name}',
        'show topology detail {address_family} {multicast} all',
        'show topology detail {address_family} {multicast} topo {topo_name}'
    ]

    def cli(self,
            address_family=None,
            topo_name=None,
            multicast=None,
            output=None):
        if output is None:
            if address_family and multicast and topo_name:
                cmd = self.cli_command[3].format(address_family=address_family,
                                                 multicast=multicast,
                                                 topo_name=topo_name)
            elif address_family and multicast:
                cmd = self.cli_command[2].format(address_family=address_family,
                                                 multicast=multicast)
            elif address_family and topo_name:
                cmd = self.cli_command[1].format(address_family=address_family,
                                                 topo_name=topo_name)
            else:
                cmd = self.cli_command[0].format(address_family=address_family)
            out = self.device.execute(cmd)
        else:
            out = output

        return super().cli(output=out)


class ShowTopologyDetailVrf(ShowTopology):
    """ Parser for:
          show topology detail vrf {vrf} all
          show topology detail vrf {vrf} {address_family} all
          show topology detail vrf {vrf} {address_family} topo {topo_name}
          show topology detail vrf {vrf} {address_family} {multicast} all
          show topology detail vrf {vrf} {address_family} {multicast} topo {topo_name}
    """
    cli_command = [
        'show topology detail vrf {vrf} all',
        'show topology detail vrf {vrf} {address_family} all',
        'show topology detail vrf {vrf} {address_family} topo {topo_name}',
        'show topology detail vrf {vrf} {address_family} {multicast} all',
        'show topology detail vrf {vrf} {address_family} {multicast} topo {topo_name}',
    ]

    def cli(self,
            vrf=None,
            address_family=None,
            topo_name=None,
            multicast=None,
            output=None):
        if output is None:
            if vrf and address_family and multicast and topo_name:
                cmd = self.cli_command[4].format(vrf=vrf,
                                                 address_family=address_family,
                                                 multicast=multicast,
                                                 topo_name=topo_name)
            elif vrf and address_family and multicast:
                cmd = self.cli_command[3].format(vrf=vrf,
                                                 address_family=address_family,
                                                 multicast=multicast)
            elif vrf and address_family and topo_name:
                cmd = self.cli_command[2].format(vrf=vrf,
                                                 address_family=address_family,
                                                 topo_name=topo_name)
            elif vrf and address_family:
                cmd = self.cli_command[1].format(vrf=vrf,
                                                 address_family=address_family)
            else:
                cmd = self.cli_command[0].format(vrf=vrf)
            out = self.device.execute(cmd)
        else:
            out = output

        return super().cli(output=out)
