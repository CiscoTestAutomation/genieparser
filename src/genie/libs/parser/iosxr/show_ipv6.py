"""
    show_ipv6.py
    IOSXR parsers for the following show commands:

    * show ipv6 neighbors detail
    * show ipv6 vrf all interface
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Or, And,\
                                         Default, Use

# ======================================================
# Parser for 'show ipv6 neighbors detail '
# ======================================================

class ShowIpv6NeighborsDetailSchema(MetaParser):
    """Schema for show ipv6 neighbors detail"""

    schema = {
        'interface': {
            Any(): {
                'interface': str,
                'neighbors': {
                    Any(): {
                        'ip': str,  # Conf/Ops Str '2010:1:2::1'
                        'link_layer_address': str,  # Conf/Ops Str 'aaaa.beef.cccc'
                        'age': str,
                        'neighbor_state': str,
                        'location': str,
                        'static': str,
                        'dynamic': str,
                        'sync': str,
                        'serg_flags': str
                    },
                },
            },
        },
    }

class ShowIpv6NeighborsDetail(ShowIpv6NeighborsDetailSchema):
    """Parser for show ipv6 neighbors detail"""

    cli_command = 'show ipv6 neighbors detail'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # 2010:1:2::1  82   fa16.3e19.abba REACH Gi0/0/0/0  0/0/CPU0  -  Y  - ff
        p1 = re.compile(r'^(?P<ip>\S+)\s+(?P<age>\S+)\s+(?P<link_layer_address>\S+)\s+(?P<neighbor_state>\S+)\s+(?P<interface>\S+)\s+'
                         '(?P<location>\S+)\s+(?P<static>\S+)\s+(?P<dynamic>\S+)\s+(?P<sync>\S+)\s+(?P<serg_flags>\S+)$')

        #[Mcast adjacency]                - 0000.0000.0000 REACH Gi0/0/0/0            0/0/CPU0        -      -       -            ff
        p2 = re.compile(r'^\[(?P<ip>([\w\s]+))\]\s+(?P<age>\S+)\s+(?P<link_layer_address>\S+)\s+(?P<neighbor_state>\S+)\s+'
                         '(?P<interface>\S+)\s+(?P<location>\S+)\s+(?P<static>\S+)\s+(?P<dynamic>\S+)\s+(?P<sync>\S+)\s+(?P<serg_flags>\S+)$')

        for line in out.splitlines():
            line = line.strip()

            # 2010:1:2::1  82   fa16.3e19.abba REACH Gi0/0/0/0  0/0/CPU0  -  Y  - ff
            m = p1.match(line)
            if m:
                ip = m.groupdict()['ip']
                age = m.groupdict()['age']
                link_layer_address = m.groupdict()['link_layer_address']
                neighbor_state = m.groupdict()['neighbor_state']
                interface = m.groupdict()['interface']
                location = m.groupdict()['location']
                static = m.groupdict()['static']
                dynamic = m.groupdict()['dynamic']
                sync = m.groupdict()['sync']
                serg_flags = m.groupdict()['serg_flags']

                interface_dict = ret_dict.setdefault('interface', {}).setdefault(interface, {})
                interface_dict['interface'] = interface

                neighbor_dict = interface_dict.setdefault('neighbors', {}).setdefault(ip, {})

                neighbor_dict['age'] = age
                neighbor_dict['ip'] = ip
                neighbor_dict['link_layer_address'] = link_layer_address
                neighbor_dict['neighbor_state'] = neighbor_state
                neighbor_dict['location'] = location
                neighbor_dict['static'] = static
                neighbor_dict['dynamic'] = dynamic
                neighbor_dict['sync'] = sync
                neighbor_dict['serg_flags'] = serg_flags
                continue

            # [Mcast adjacency]  - 0000.0000.0000 REACH Gi0/0/0/0   0/0/CPU0  -      -       -            ff
            m = p2.match(line)
            if m:
                ip = m.groupdict()['ip']
                age = m.groupdict()['age']
                link_layer_address = m.groupdict()['link_layer_address']
                neighbor_state = m.groupdict()['neighbor_state']
                interface = m.groupdict()['interface']
                location = m.groupdict()['location']
                static = m.groupdict()['static']
                dynamic = m.groupdict()['dynamic']
                sync = m.groupdict()['sync']
                serg_flags = m.groupdict()['serg_flags']

                interface_dict = ret_dict.setdefault('interface', {}).setdefault(interface, {})
                interface_dict['interface'] = interface

                neighbor_dict = interface_dict.setdefault('neighbors', {}).setdefault(ip, {})

                neighbor_dict['age'] = age
                neighbor_dict['ip'] = ip

                neighbor_dict['link_layer_address'] = link_layer_address
                neighbor_dict['neighbor_state'] = neighbor_state
                neighbor_dict['location'] = location
                neighbor_dict['static'] = static
                neighbor_dict['dynamic'] = dynamic
                neighbor_dict['sync'] = sync
                neighbor_dict['serg_flags'] = serg_flags
                continue
        return ret_dict


# ======================================================
# Parser for 'show ipv6 vrf all interface '
# ======================================================

class ShowIpv6VrfAllInterfaceSchema(MetaParser):
    """Schema for show ipv6 vrf all interface"""

    schema = {
        Any(): {
            'oper_status': str,
            'int_status': str,
            'vrf': str,
            'vrf_id': str,
            'enabled': bool,
            'ipv6_enabled': bool,
            Optional('ipv6'): {
                Any(): {
                    Optional('ipv6'): str,
                    Optional('ipv6_prefix_length'): str,
                    Optional('ipv6_status'): str,
                    Optional('ipv6_route_tag'): str,
                    Optional('ipv6_eui64'): bool,
                    Optional('ipv6_subnet'): str},
                Optional('ipv6_link_local'): str,
                Optional('ipv6_link_local_state'): str,
                Optional('ipv6_group_address'): str,
                Optional('ipv6_groups'): list,
                Optional('ipv6_mtu'): str,
                Optional('ipv6_mtu_available'): str,
                Optional('icmp_redirects'): str,
                Optional('icmp_unreachables'): str,
                Optional('nd_dad'): str,
                Optional('dad_attempts'): str,
                Optional('nd_reachable_time'): str,
                Optional('nd_cache_limit'): str,
                Optional('nd_adv_retrans_int'): str,
                Optional('nd_adv_duration'): str,
                Optional('nd_router_adv'): str,
                Optional('stateless_autoconfig'): bool,
                Optional('out_access_list'): str,
                Optional('in_access_list'): str,
                Optional('in_common_access_list'): str,
                Optional('table_id'): str,
                Optional('complete_protocol_adj'): str,
                Optional('complete_glean_adj'): str,
                Optional('incomplete_protocol_adj'): str,
                Optional('incomplete_glean_adj'): str,
                Optional('dropped_protocol_req'): str,
                Optional('dropped_glean_req'): str
            },
        },
    }


class ShowIpv6VrfAllInterface(ShowIpv6VrfAllInterfaceSchema):
    """Parser for show ipv6 vrf all interface"""

    cli_command = 'show ipv6 vrf all interface'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # GigabitEthernet0/0/0/0 is Shutdown, ipv6 protocol is Down, Vrfid is VRF1 (0x60000002)
        # nve100 is Up, ipv6 protocol is Unknown, Vrfid is default (0x60000000)
        p1 = re.compile(r'^(?P<interface>\S+) +is +(?P<int_status>[a-zA-Z]+),'
                         ' +ipv6 +protocol +is +(?P<oper_status>[a-zA-Z]+),'
                         ' +Vrfid +is +(?P<vrf>\S+) +\((?P<vrf_id>[a-z0-9]+)\)$')

        # IPv6 is enabled, link-local address is fe80::a8aa:bbff:febb:cccc [TENTATIVE]
        p2 = re.compile(r'^(?P<enabled>(IPv6 is enabled)), +link-local +address +is +(?P<ipv6_link_local>[a-zA-Z0-9\:]+) +\[(?P<ipv6_link_local_state>[A-Z]+)\]$')

        # IPv6 is enabled, link-local address is fe80::a8aa:bbff:febb:cccc
        p2_1 = re.compile(r'^(?P<enabled>(IPv6 is enabled)), +link-local +address +is +(?P<ipv6_link_local>[a-zA-Z0-9\:]+)$')

        # IPv6 is disabled, link-local address unassigned
        p2_2 = re.compile(r'^(?P<enabled>(IPv6 is disabled)), +link-local +address +(?P<ipv6_link_local>[a-zA-Z]+)$')

        # Global unicast address(es):
        # 2001:db8:3:3:a8aa:bbff:febb:cccc, subnet is 2001:db8:3:3::/64 [TENTATIVE]
        p3 = re.compile(r'^(?P<ipv6>(.+)(ff:fe)(.+)), +subnet +is'
                         ' +(?P<ipv6_subnet>[a-zA-Z0-9\:]+)\/(?P<ipv6_prefix_length>[0-9]+)'
                         ' +\[(?P<ipv6_status>[A-Z]+)\](?: +with +route-tag'
                         ' +(?P<ipv6_route_tag>[0-9]+))?$')

        # Global unicast address(es):
        # 2001:db8:4:4::4, subnet is 2001:db8:4:4::/64 [TENTATIVE] with route-tag 10
        p3_1 = re.compile(r'^(?P<ipv6>[a-zA-Z0-9\:]+), +subnet +is +(?P<ipv6_subnet>[a-zA-Z0-9\:]+)\/'
                           '(?P<ipv6_prefix_length>[0-9]+) +\[(?P<ipv6_status>[A-Z]+)\] +with +route-tag +(?P<ipv6_route_tag>[0-9]+)$')

        # Global unicast address(es):
        # 2001:db8:1:1::1, subnet is 2001:db8:1:1::/64 [TENTATIVE]
        p3_2 = re.compile(r'^(?P<ipv6>[a-zA-Z0-9\:]+), +subnet +is +(?P<ipv6_subnet>[a-zA-Z0-9\:]+)\/'
                           '(?P<ipv6_prefix_length>[0-9]+) +\[(?P<ipv6_status>[A-Z]+)\]?$')

        # Global unicast address(es):
        # 2001:db8:1:1::1, subnet is 2001:db8:1:1::/64
        p3_3 = re.compile(r'^(?P<ipv6>[a-zA-Z0-9\:]+), +subnet +is +(?P<ipv6_subnet>[a-zA-Z0-9\:]+)\/(?P<ipv6_prefix_length>[0-9]+)$')

        # Joined group address(es): ff02::1:ff00:1 ff02::1:ffa6:78c5 ff02::2
        # ff02::1
        p4 = re.compile(r'^Joined +group +address\(es\): +(?P<ipv6_group_address>[a-z0-9\:\s]+)$')

        p4_1 = re.compile(r'^(?P<ipv6_group_address>[a-z0-9\:\s]+)$')

        # MTU is 1600 (1586 is available to IPv6)
        p5 = re.compile(r'^MTU +is +(?P<ipv6_mtu>[0-9]+) +\((?P<ipv6_mtu_available>[0-9]+) +is +available +to +IPv6\)$')

        # ICMP redirects are disabled
        p6 = re.compile(r'^ICMP +redirects +are +(?P<icmp_redirects>[a-z]+)$')

        # ICMP unreachables are enabled
        p7 = re.compile(r'^ICMP +unreachables +are +(?P<icmp_unreachables>[a-z]+)$')

        # ND DAD is enabled, number of DAD attempts 1
        p8 = re.compile(r'^ND +DAD +is +(?P<nd_dad>[a-z]+), +number +of +DAD +attempts +(?P<dad_attempts>[0-9]+)$')

        # ND reachable time is 0 milliseconds
        p9 = re.compile(r'^ND +reachable +time +is +(?P<nd_reachable_time>[0-9]+) +milliseconds$')

        # ND cache entry limit is 1000000000
        p10 = re.compile(r'^ND +cache +entry +limit +is +(?P<nd_cache_limit>[0-9]+)$')

        # ND advertised retransmit interval is 0 milliseconds
        p11 = re.compile(r'^ND +advertised +retransmit +interval +is +(?P<nd_adv_retrans_int>[0-9]+) +milliseconds$')

        # ND router advertisements are sent every 160 to 240 seconds
        p11_1 = re.compile(r'^ND +router +advertisements +are +sent +every +(?P<nd_adv_duration>[a-z0-9\s]+) +seconds$')

        # ND router advertisements live for 1800 seconds
        p11_2 = re.compile(r'^ND +router +advertisements +live +for +(?P<nd_router_adv>[0-9]+) +seconds$')

        # Hosts use stateless autoconfig for addresses.
        p12 = re.compile(r'^Hosts +use +(?P<stateless_autoconfig>(stateless)) +autoconfig +for +addresses.$')

        # Outgoing access list is not set
        p13 = re.compile(r'^Outgoing +access +list +is +(?P<out_access_list>[a-zA-Z\s]+)$')

        # Inbound  access list is not set
        p14 = re.compile(r'^Inbound +access +list +is +(?P<in_access_list>[a-zA-Z\s]+)$')

        # Inbound  common access list is not set, access list is not set
        p14_1 = re.compile(r'^Inbound +common +access +list +is +(?P<in_common_access_list>[a-zA-Z\s]+),'
                            ' +access +list +is +(?P<in_access_list>[a-zA-Z\s]+)$')

        # Table Id is 0xe0800011
        p15 = re.compile(r'^Table +Id +is +(?P<table_id>[a-z0-9]+)$')

        # Complete protocol adjacency: 0
        p16 = re.compile(r'^Complete +protocol +adjacency: +(?P<complete_protocol_adj>[0-9]+)$')

        # Complete glean adjacency: 0
        p17 = re.compile(r'^Complete +glean +adjacency: +(?P<complete_glean_adj>[0-9]+)$')

        # Incomplete protocol adjacency: 0
        p18 = re.compile(r'^Incomplete +protocol +adjacency: +(?P<incomplete_protocol_adj>[0-9]+)$')

        # Incomplete glean adjacency: 0
        p19 = re.compile(r'^Incomplete +glean +adjacency: +(?P<incomplete_glean_adj>[0-9]+)$')

        # Dropped protocol request: 0
        p20 = re.compile(r'^Dropped +protocol +request: +(?P<dropped_protocol_req>[0-9]+)$')

        # Dropped glean request: 0
        p21 = re.compile(r'^Dropped +glean +request: +(?P<dropped_glean_req>[0-9]+)$')

        for line in out.splitlines():
            line = line.strip()

            # GigabitEthernet0/0/0/0 is Shutdown, ipv6 protocol is Down, Vrfid is VRF1 (0x60000002)
            # nve100 is Up, ipv6 protocol is Unknown, Vrfid is default (0x60000000)
            p1 = re.compile(r'^\s*(?P<interface>\S+) +is +(?P<int_status>[a-zA-Z]+),'
                            ' +ipv6 +protocol +is +(?P<oper_status>[a-zA-Z]+),'
                            ' +Vrfid +is +(?P<vrf>\S+) +\((?P<vrf_id>[a-z0-9]+)\)$')
            m = p1.match(line)
            if m:
                interface = m.groupdict()['interface']
                int_status = m.groupdict()['int_status'].lower()
                oper_status = m.groupdict()['oper_status'].lower()
                vrf = m.groupdict()['vrf']
                vrf_id = m.groupdict()['vrf_id']

                ipv6_vrf_all_interface_dict = ret_dict.setdefault(interface, {})

                if oper_status == 'up':
                    ipv6_vrf_all_interface_dict['ipv6_enabled'] = True
                else:
                    ipv6_vrf_all_interface_dict['ipv6_enabled'] = False

                ipv6_vrf_all_interface_dict['int_status'] = int_status
                ipv6_vrf_all_interface_dict['oper_status'] = oper_status
                ipv6_vrf_all_interface_dict['vrf'] = vrf
                ipv6_vrf_all_interface_dict['vrf_id'] = vrf_id

                # init multicast groups list to empty for this interface
                ipv6_groups = []
                continue

            # IPv6 is enabled, link-local address is fe80::a8aa:bbff:febb:cccc [TENTATIVE]
            m = p2.match(line)
            if m:
                enabled = bool(m.groupdict()['enabled'])
                ipv6_link_local = m.groupdict()['ipv6_link_local']
                ipv6_link_local_state = m.groupdict()['ipv6_link_local_state'].lower()

                ipv6_vrf_all_interface_dict['enabled'] = True
                continue

            # IPv6 is enabled, link-local address is fe80::a8aa:bbff:febb:cccc
            m = p2_1.match(line)
            if m:
                enabled = bool(m.groupdict()['enabled'])
                ipv6_link_local = m.groupdict()['ipv6_link_local']
                ipv6_vrf_all_interface_dict['enabled'] = True
                continue

            # IPv6 is disabled, link-local address unassigned
            m = p2_2.match(line)
            if m:
                enabled = bool(m.groupdict()['enabled'])
                ipv6_link_local = m.groupdict()['ipv6_link_local']
                ipv6_vrf_all_interface_dict['enabled'] = False
                continue

            # Global unicast address(es):
            # 2001:db8:3:3:a8aa:bbff:febb:cccc, subnet is 2001:db8:3:3::/64 [TENTATIVE]
            m = p3.match(line)
            if m:
                ipv6 = m.groupdict()['ipv6']
                ipv6_subnet = m.groupdict()['ipv6_subnet']
                ipv6_prefix_length = m.groupdict()['ipv6_prefix_length']
                ipv6_status = m.groupdict()['ipv6_status'].lower()
                ipv6_route_tag = m.groupdict()['ipv6_route_tag']

                address = ipv6 + '/' + ipv6_prefix_length

                ipv6_key_dict = ipv6_vrf_all_interface_dict.setdefault('ipv6', {})
                ipv6_dict = ipv6_key_dict.setdefault(address, {})

                if ipv6_route_tag:
                    ipv6_dict['ipv6_route_tag'] = str(m.groupdict()['ipv6_route_tag'])
                    ipv6_dict['ipv6'] = ipv6
                    ipv6_dict['ipv6_prefix_length'] = ipv6_prefix_length
                    ipv6_dict['ipv6_status'] = ipv6_status
                    ipv6_dict['ipv6_subnet'] = ipv6_subnet
                    ipv6_dict['ipv6_eui64'] = True
                try:
                    ipv6_key_dict['ipv6_link_local_state'] = ipv6_link_local_state
                    ipv6_key_dict['ipv6_link_local'] = ipv6_link_local
                    continue
                except Exception:
                    pass

            # Global unicast address(es):
            # 2001:db8:4:4::4, subnet is 2001:db8:4:4::/64 [TENTATIVE] with route-tag 10
            m = p3_1.match(line)
            if m:
                ipv6 = m.groupdict()['ipv6']
                ipv6_subnet = m.groupdict()['ipv6_subnet']
                ipv6_prefix_length = m.groupdict()['ipv6_prefix_length']
                ipv6_status = m.groupdict()['ipv6_status'].lower()
                ipv6_route_tag = (m.groupdict()['ipv6_route_tag'])

                address = ipv6 + '/' + ipv6_prefix_length

                ipv6_key_dict = ipv6_vrf_all_interface_dict.setdefault('ipv6', {})
                ipv6_dict = ipv6_key_dict.setdefault(address, {})

                ipv6_dict['ipv6'] = ipv6
                ipv6_dict['ipv6_prefix_length'] = ipv6_prefix_length
                ipv6_dict['ipv6_status'] = ipv6_status
                ipv6_dict['ipv6_route_tag'] = ipv6_route_tag
                ipv6_dict['ipv6_subnet'] = ipv6_subnet
                try:
                    ipv6_key_dict['ipv6_link_local_state'] = ipv6_link_local_state
                    ipv6_key_dict['ipv6_link_local'] = ipv6_link_local
                    continue
                except Exception:
                    pass

            # Global unicast address(es):
            # 2001:db8:1:1::1, subnet is 2001:db8:1:1::/64 [TENTATIVE]
            m = p3_2.match(line)
            if m:
                ipv6 = m.groupdict()['ipv6']
                ipv6_subnet = m.groupdict()['ipv6_subnet']
                ipv6_prefix_length = m.groupdict()['ipv6_prefix_length']
                ipv6_status = m.groupdict()['ipv6_status'].lower()

                address = ipv6 + '/' + ipv6_prefix_length

                ipv6_key_dict = ipv6_vrf_all_interface_dict.setdefault('ipv6', {})
                ipv6_dict = ipv6_key_dict.setdefault(address, {})

                ipv6_dict['ipv6'] = ipv6
                ipv6_dict['ipv6_prefix_length'] = ipv6_prefix_length
                ipv6_dict['ipv6_status'] = ipv6_status
                ipv6_dict['ipv6_subnet'] = ipv6_subnet
                try:
                    ipv6_key_dict['ipv6_link_local_state'] = ipv6_link_local_state
                    ipv6_key_dict['ipv6_link_local'] = ipv6_link_local
                    continue
                except Exception:
                    pass

            # Global unicast address(es):
            # 2001:db8:1:1::1, subnet is 2001:db8:1:1::/64
            m = p3_3.match(line)
            if m:
                ipv6 = m.groupdict()['ipv6']
                ipv6_subnet = m.groupdict()['ipv6_subnet']
                ipv6_prefix_length = m.groupdict()['ipv6_prefix_length']

                address = ipv6 + '/' + ipv6_prefix_length

                ipv6_key_dict = ipv6_vrf_all_interface_dict.setdefault('ipv6', {})
                ipv6_dict = ipv6_key_dict.setdefault(address, {})

                ipv6_dict['ipv6'] = ipv6
                ipv6_dict['ipv6_prefix_length'] = ipv6_prefix_length
                ipv6_dict['ipv6_subnet'] = ipv6_subnet
                try:
                    ipv6_key_dict['ipv6_link_local'] = ipv6_link_local
                    continue
                except Exception:
                    pass

            # Joined group address(es): ff02::1:ff00:1 ff02::1:ffa6:78c5 ff02::2
            # ff02::1
            m = p4.match(line)
            if m:
                ipv6_group_address = str(m.groupdict()['ipv6_group_address'])

                # split string of addressed into a list
                ipv6_group_address = [str(i) for i in ipv6_group_address.split()]

                # Add to previous created list
                for group in ipv6_group_address:
                    ipv6_groups.append(group)

                ipv6_key_dict['ipv6_groups'] = ipv6_groups
                continue

            m = p4_1.match(line)
            if m:
                ipv6_group_address = str(m.groupdict()['ipv6_group_address'])

                # split string of addressed into a list
                ipv6_group_address = [str(i) for i in ipv6_group_address.split()]

                # Add to previous created list
                for group in ipv6_group_address:
                    ipv6_groups.append(group)

                ipv6_key_dict['ipv6_groups'] = ipv6_groups
                continue

            # MTU is 1600 (1586 is available to IPv6)
            m = p5.match(line)
            if m:
                ipv6_mtu = m.groupdict()['ipv6_mtu']
                ipv6_mtu_available = m.groupdict()['ipv6_mtu_available']

                ipv6_key_dict['ipv6_mtu'] = ipv6_mtu
                ipv6_key_dict['ipv6_mtu_available'] = ipv6_mtu_available
                continue

            # ICMP redirects are disabled
            m = p6.match(line)
            if m:
                icmp_redirects = m.groupdict()['icmp_redirects']
                ipv6_key_dict['icmp_redirects'] = icmp_redirects
                continue

            # ICMP unreachables are enabled
            m = p7.match(line)
            if m:
                icmp_unreachables = m.groupdict()['icmp_unreachables']

                ipv6_key_dict['icmp_unreachables'] = icmp_unreachables
                continue

            # ND DAD is enabled, number of DAD attempts 1
            m = p8.match(line)
            if m:
                nd_dad = m.groupdict()['nd_dad']
                dad_attempts = m.groupdict()['dad_attempts']
                ipv6_key_dict['nd_dad'] = nd_dad
                ipv6_key_dict['dad_attempts'] = dad_attempts
                continue

            # ND reachable time is 0 milliseconds
            m = p9.match(line)
            if m:
                nd_reachable_time = m.groupdict()['nd_reachable_time']
                ipv6_key_dict['nd_reachable_time'] = nd_reachable_time
                continue

            # ND cache entry limit is 1000000000
            m = p10.match(line)
            if m:
                nd_cache_limit = m.groupdict()['nd_cache_limit']
                ipv6_key_dict['nd_cache_limit'] = nd_cache_limit
                continue

            # ND advertised retransmit interval is 0 milliseconds
            m = p11.match(line)
            if m:
                nd_adv_retrans_int = m.groupdict()['nd_adv_retrans_int']
                ipv6_key_dict['nd_adv_retrans_int'] = nd_adv_retrans_int
                continue

            # ND router advertisements are sent every 160 to 240 seconds
            m = p11_1.match(line)
            if m:
                nd_adv_duration = m.groupdict()['nd_adv_duration']
                nd_adv_duration = nd_adv_duration.replace(" ", "")
                nd_adv_duration = nd_adv_duration.replace("to", "-")
                ipv6_key_dict['nd_adv_duration'] = nd_adv_duration
                continue

            # ND router advertisements live for 1800 seconds
            m = p11_2.match(line)
            if m:
                nd_router_adv = m.groupdict()['nd_router_adv']
                ipv6_key_dict['nd_router_adv'] = nd_router_adv
                continue

            # Hosts use stateless autoconfig for addresses.
            m = p12.match(line)
            if m:
                stateless_autoconfig = m.groupdict()['stateless_autoconfig']
                ipv6_key_dict['stateless_autoconfig'] = True
                continue

            # Outgoing access list is not set
            m = p13.match(line)
            if m:
                out_access_list = m.groupdict()['out_access_list']

                if out_access_list != "not set":
                    ipv6_key_dict['out_access_list'] = out_access_list
                continue

            # Inbound  access list is not set
            m = p14.match(line)
            if m:
                in_access_list = m.groupdict()['in_access_list']
                if in_access_list != "not set":
                    ipv6_key_dict['in_access_list'] = in_access_list
                continue

            # Inbound  common access list is not set, access list is not set
            m = p14_1.match(line)
            if m:
                in_common_access_list = m.groupdict()['in_common_access_list']
                in_access_list = m.groupdict()['in_access_list']
                if in_common_access_list != "not set":
                    ipv6_key_dict['in_common_access_list'] = in_common_access_list
                if in_access_list != "not set":
                    ipv6_key_dict['in_access_list'] = in_access_list
                continue

            # Table Id is 0xe0800011
            m = p15.match(line)
            if m:
                table_id = m.groupdict()['table_id']
                ipv6_key_dict['table_id'] = table_id
                continue

            # Complete protocol adjacency: 0
            m = p16.match(line)
            if m:
                complete_protocol_adj = m.groupdict()['complete_protocol_adj']

                ipv6_key_dict['complete_protocol_adj'] = complete_protocol_adj
                continue

            # Complete glean adjacency: 0
            m = p17.match(line)
            if m:
                complete_glean_adj = m.groupdict()['complete_glean_adj']
                ipv6_key_dict['complete_glean_adj'] = complete_glean_adj
                continue

            # Incomplete protocol adjacency: 0
            m = p18.match(line)
            if m:
                incomplete_protocol_adj = m.groupdict()['incomplete_protocol_adj']
                ipv6_key_dict['incomplete_protocol_adj'] = incomplete_protocol_adj
                continue

            # Incomplete glean adjacency: 0
            m = p19.match(line)
            if m:
                incomplete_glean_adj = m.groupdict()['incomplete_glean_adj']
                ipv6_key_dict['incomplete_glean_adj'] = incomplete_glean_adj
                continue

            # Dropped protocol request: 0
            m = p20.match(line)
            if m:
                dropped_protocol_req = m.groupdict()['dropped_protocol_req']
                ipv6_key_dict['dropped_protocol_req'] = dropped_protocol_req
                continue

            # Dropped glean request: 0
            m = p21.match(line)
            if m:
                dropped_glean_req = m.groupdict()['dropped_glean_req']
                ipv6_key_dict['dropped_glean_req'] = dropped_glean_req
                continue

        return ret_dict
