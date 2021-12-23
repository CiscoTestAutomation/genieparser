"""show_nd.py

NXOS parser for the following show commands:
    * show ipv6 neighbor detail vrf all
    * show ipv6 neighbor detail
    * show ipv6 neighbor detail vrf <vrf>
    * show ipv6 nd interface
    * show ipv6 nd interface vrf all
    * show ipv6 nd interface vrf <vrf>
    * show ipv6 nd interface <interface>
    * show ipv6 nd interface <interface> vrf all
    * show ipv6 nd interface <interface> vrf <vrf>
    * show ipv6 icmp neighbor detail
    * show ipv6 icmp neighbor detail vrf all
    * show ipv6 icmp neighbor detail vrf <vrf>
    * show ipv6 icmp neighbor <interface> detail
    * show ipv6 icmp neighbor <interface> detail vrf all
    * show ipv6 icmp neighbor <interface> detail vrf <vrf>
    * show ipv6 routers
    * show ipv6 routers vrf all
    * show ipv6 routers vrf <vrf>
    * show ipv6 neighbor
    * show ipv6 neighbor vrf all
    * show ipv6 neighbor vrf <vrf>
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional
from genie.libs.parser.utils.common import Common
# ====================================================
#  schema for show ipv6 neighbor detail
# ====================================================


class ShowIpv6NeighborDetailSchema(MetaParser):
    """Schema for:
        show ipv6 neighbor detail
        show ipv6 neighbor detail vrf all
        show ipv6 neighbor detail vrf <vrf>"""

    schema = {
        Optional('interfaces'): {
            Any(): {
                'interface': str,
                'neighbors': {
                    Any(): {
                        'ip': str,
                        'link_layer_address': str,
                        'age': str,
                        Optional('preference'): int,
                        'origin': str,
                        Optional('physical_interface'): str,
                        Optional('packet_count'): int,
                        Optional('byte_count'): int,
                        Optional('best'): str,
                        Optional('throttled'): str,
                    },
                },
            },
        },
        'adjacency_hit': {
            Any(): {
                'packet_count': int,
                'byte_count': int
            },
        },
        'adjacency_statistics_last_updated_before': str,
        'total_number_of_entries': int
    }


# ====================================================
#  parser for show ipv6 neighbor detail
# ====================================================
class ShowIpv6NeighborDetail(ShowIpv6NeighborDetailSchema):
    """Parser for :
        show ipv6 neighbor detail
        show ipv6 neighbor detail vrf all
        show ipv6 neighbor detail vrf <vrf>"""

    cli_command = [
        'show ipv6 neighbor detail vrf {vrf}', 'show ipv6 neighbor detail']
    exclude = [
        'age']

    def cli(self, vrf="", output=None):
        if vrf:
            cmd = self.cli_command[0].format(vrf=vrf)
        else:
            cmd = self.cli_command[1]

            # excute command to get output
        if output is None:
            out = self.device.execute(cmd)
        else:
            out = output

        result_dict = {}
        interface = ""

        origin_list = ['dynamic', 'static']

        # No. of Adjacency hit with type INVALID: Packet count 0, Byte count 0
        # No. of Adjacency hit with type GLOBAL DROP: Packet count 0, Byte count 0
        # No. of Adjacency hit with type GLOBAL PUNT: Packet count 0, Byte count 0
        # No. of Adjacency hit with type GLOBAL GLEAN: Packet count 0, Byte count 0
        # No. of Adjacency hit with type GLEAN: Packet count 0, Byte count 0
        # No. of Adjacency hit with type NORMAL: Packet count 0, Byte count 0
        p1 = re.compile(r'^No. +of +Adjacency +hit +with +type +(?P<adjacency>([\w\s]+)): +Packet +count +'
                        '(?P<packet_count>(\d+)), +Byte +count +(?P<byte_count>(\d+))$')

        # Adjacency statistics last updated before: never
        p2 = re.compile(r'^Adjacency +statistics +last +updated +before: '
                        r'+(?P<adjacency_statistics_last_updated_before>(\w+))$')

        # Total number of entries: 11
        p3 = re.compile(
            r'^Total +number +of +entries: +(?P<total_number_of_entries>(\d+))$')

        # Address :            2001:db8:c56d:4::2
        # Age :                00:09:27
        # MacAddr :            fa16.3eff.e5a2
        # Preference :         50
        # Source :             icmpv6
        # Interface :          Ethernet1/1
        # Physical Interface : Ethernet1/1
        # Packet Count :       0
        # Byte Count :         0
        # Best :               Yes
        # Throttled :          No
        p4 = re.compile(
            r'^(?P<neighbor_key>(?!Total number of entries)[A-Za-z\s]+) +: +(?P<neighbor_value>[\w\/\.\:]+)$')

        for line in out.splitlines():
            if line:
                line = line.strip()
            else:
                continue

            m = p1.match(line)
            if m:
                adjacency = m.groupdict()['adjacency']
                packet_count = int(m.groupdict()['packet_count'])
                byte_count = int(m.groupdict()['byte_count'])

                adjacency_dict = result_dict.setdefault(
                    'adjacency_hit', {}).setdefault(adjacency, {})
                adjacency_dict.update({'packet_count': packet_count})
                adjacency_dict.update({'byte_count': byte_count})
                continue

            # Adjacency statistics last updated before: never
            m = p2.match(line)
            if m:
                result_dict.update({'adjacency_statistics_last_updated_before': m.groupdict()[
                    'adjacency_statistics_last_updated_before']})
                continue

            # Total number of entries: 11
            m = p3.match(line)
            if m:
                result_dict.update({'total_number_of_entries': int(
                    m.groupdict()['total_number_of_entries'])})
                continue

            m = p4.match(line)
            if m:
                group = m.groupdict()
                neighbor_key = group.pop(
                    'neighbor_key').lower().replace(" ", "_")
                neighbor_value = group.pop('neighbor_value')

                if 'address' in neighbor_key:
                    interface = ""
                    address = neighbor_value

                if 'macaddr' in neighbor_key:
                    neighbor_key = 'link_layer_address'
                    link_layer_address = neighbor_value

                if 'source' in neighbor_key:
                    neighbor_key = 'origin'
                    origin = 'other' if neighbor_value.lower(
                    ) not in origin_list else neighbor_value.lower()

                if 'age' in neighbor_key:
                    age = neighbor_value

                if 'preference' in neighbor_key:
                    preference = int(neighbor_value)

                if neighbor_key == 'interface':
                    interface = neighbor_value

                if interface:
                    res_dict = result_dict.setdefault(
                        'interfaces', {}).setdefault(interface, {})
                    res_dict.update({'interface': interface})
                    neighbor_dict = res_dict.setdefault(
                        'neighbors', {}).setdefault(address, {})
                    neighbor_dict.update({'ip': address})
                    neighbor_dict.update({'age': age})
                    neighbor_dict.update(
                        {'link_layer_address': link_layer_address})
                    neighbor_dict.update({'origin': origin})
                    neighbor_dict.update({'preference': preference})
                    if neighbor_key != 'interface':
                        try:
                            neighbor_dict.update(
                                {neighbor_key: int(neighbor_value)})
                        except ValueError:
                            neighbor_dict.update(
                                {neighbor_key: neighbor_value})
                continue

        return result_dict

# ====================================================
#  schema for show ipv6 nd interface
# ====================================================


class ShowIpv6NdInterfaceSchema(MetaParser):
    """Schema for:
        show ipv6 nd interface
        show ipv6 nd interface vrf all
        show ipv6 nd interface vrf <vrf>
        show ipv6 nd interface <interface>
        show ipv6 nd interface <interface> vrf all
        show ipv6 nd interface <interface> vrf <vrf>"""

    schema = {
        'vrf': {
            Any(): {
                'interfaces': {
                    Any(): {
                        'interface': str,
                        'oper_status': str,
                        'enable': bool,
                        'ip': str,
                        'mac_extract': str,
                        'local_address': str,
                        'link_status': str,
                        'router_advertisement': {
                            'interval': int,
                            'lifetime': int,
                            'managed_address_configuration': bool,
                            'other_stateful_configuration': bool,
                            'default_router_preference': str,
                            'current_hop_limit': int,
                            'mtu': int,
                            'reachable_time': int,
                            'retrans_timer': int,
                            'suppress': bool,
                            'suppress_mtu': bool,
                            'suppress_route_information': bool
                        },
                        'active_timers': {
                            'last_neighbor_solicitation': str,
                            'last_neighbor_advertisement': str,
                            'last_router_advertisement': str,
                            'next_router_advertisement': str,

                        },
                        'neighbor_solicitation': {
                            'interval': int,
                            'retry_base': int,
                            'retry_interval': int,
                            'retry_attempts': int,
                        },
                        'error_message': {
                            'redirects': bool,
                            'unreachables': bool,
                        },
                        'dad': {
                            'maximum_attempts': int,
                            'current_attempt': int,
                        },
                    },
                },
            },
        },
    }


# ====================================================
#  parser for show ipv6 nd interface
# ====================================================
class ShowIpv6NdInterface(ShowIpv6NdInterfaceSchema):
    """Parser for :
        show ipv6 nd interface
        show ipv6 nd interface vrf all
        show ipv6 nd interface vrf <vrf>
        show ipv6 nd interface <interface>
        show ipv6 nd interface <interface> vrf all
        show ipv6 nd interface <interface> vrf <vrf>"""

    cli_command = ['show ipv6 nd interface {interface} vrf {vrf}',
                   'show ipv6 nd interface {interface}',
                   'show ipv6 nd interface vrf {vrf}',
                   'show ipv6 nd interface', ]
    exclude = [
        'last_neighbor_advertisement',
        'last_neighbor_solicitation',
        'last_router_advertisement',
        'next_router_advertisement']

    def cli(self, vrf="", interface="", output=None):
        if vrf and interface:
            cmd = self.cli_command[0].format(vrf=vrf, interface=interface)
        elif interface:
            cmd = self.cli_command[1].format(interface=interface)
        elif vrf:
            cmd = self.cli_command[2].format(vrf=vrf)
        else:
            cmd = self.cli_command[3]

        # excute command to get output
        if output is None:
            out = self.device.execute(cmd)
        else:
            out = output

        result_dict = {}

        #   Router-Advertisement parameters:
        #       Periodic interval: 200 to 201 seconds
        #       Send "Managed Address Configuration" flag: false
        #       Send "Other Stateful Configuration" flag: false
        #       Send "Default Router Preference" value: Medium
        #       Send "Current Hop Limit" field: 64
        #       Send "MTU" option value: 1500
        #       Send "Router Lifetime" field: 1801 secs
        #       Send "Reachable Time" field: 0 ms
        #       Send "Retrans Timer" field: 0 ms
        #       Suppress RA: Enabled
        #       Suppress MTU in RA: Disabled
        #       Suppress Route Information Option in RA: Disabled
        #   Neighbor-Solicitation parameters:
        #       NS retransmit interval: 1000 ms
        #       ND NUD retry base: 1
        #       ND NUD retry interval: 1000
        #       ND NUD retry attempts: 3
        #   ICMPv6 error message parameters:
        #       Send redirects: true (0)
        #       Send unreachables: false
        #   ICMPv6 DAD parameters:
        #       Maximum DAD attempts: 1
        #       Current DAD attempt : 1

        # ICMPv6 ND Interfaces for VRF "default"
        p1 = re.compile(
            r'^\s*ICMPv6 ND Interfaces for VRF +\"(?P<vrf>[\w]+)\"$')
        # Ethernet1/1, Interface status: protocol-up/link-up/admin-up
        p2 = re.compile(r'^\s*(?P<interface>[\w\/\.]+), +Interface status:'
                        ' +protocol-(?P<protocol_status>[\w]+)/link-(?P<link_status>[\w]+)/admin-(?P<admin_status>[\w]+)$')
        #   IPv6 address:
        p3 = re.compile(r'^\s*IPv6 address:$')
        #     2001:db8:c56d:4::3/64 [VALID]
        p4 = re.compile(r'^\s*(?P<ipv6_address>[\w\:\/]+)( +\[VALID\])?$')
        # IPv6 link-local address: fe80::5c01:c0ff:fe02:7 [VALID]
        p5 = re.compile(
            r'^\s*IPv6 +link\-local +address: +(?P<link_address>[\w\:\/]+)( +\[VALID\])?$')
        # ND mac-extract : Disabled
        p6 = re.compile(r'^\s*ND mac-extract : +(?P<nd_mac_extract>[\w]+)$')
        # ICMPv6 active timers:
        p7 = re.compile(r'^\s* ICMPv6 active timers:$')
        #       Last Neighbor-Solicitation sent: 00:06:16
        p8 = re.compile(
            r'^\s*Last Neighbor-Solicitation sent: +(?P<last_neighbor_solicitation_sent>[\w\:]+)$')
        #       Last Neighbor-Advertisement sent: 00:02:12
        p9 = re.compile(
            r'^\s*Last Neighbor-Advertisement sent: +(?P<last_neighbor_advertisement_sent>[\w\:]+)$')
        #       Last Router-Advertisement sent: 1d18h
        p10 = re.compile(
            r'^\s*Last Router-Advertisement sent: +(?P<last_router_advertisement_sent>[\w\:]+)$')
        #       Next Router-Advertisement sent in: 0.000000
        p11 = re.compile(
            r'^\s*Next Router-Advertisement sent in: +(?P<next_router_advertisement_sent>[\w\.\:]+)$')
        p12 = re.compile(r'^\s*Router-Advertisement parameters:$')
        p13 = re.compile(
            r'^\s*Periodic +interval: +(?P<interval>\d+) +to +(?P<to_interval>\d+) +seconds$')
        p14 = re.compile(
            r'^\s*Send +\"(?P<router_adv_key>[\w\s]+)\" +(option value|flag|value|field): +(?P<value>\w+)( +(secs|ms))?$')
        p17 = re.compile(r'^\s*Suppress RA: +(?P<suppress>[\w]+)$')
        p18 = re.compile(r'^\s*Suppress MTU in RA: +(?P<suppress_mtu>[\w]+)$')
        p19 = re.compile(
            r'^\s*Suppress Route Information Option in RA: +(?P<suppress_route_information>[\w]+)$')
        p20 = re.compile(r'^\s*Neighbor-Solicitation parameters:$')
        p21 = re.compile(
            r'^\s*NS retransmit interval: +(?P<retransmit_interval>\d+) +ms$')
        p22 = re.compile(
            r'^\s*ND NUD retry +(?P<nd_nud_retry>\w+): +(?P<nd_nud_retry_value>\d+)$')
        p23 = re.compile(r'^\s*ICMPv6 error message parameters:$')
        p24 = re.compile(
            r'^\s*Send redirects: +(?P<redirects>\w+) +\((?P<redirects_count>\d+)\)$')
        p25 = re.compile(r'^\s*Send unreachables: +(?P<unreachables>\w+)$')
        p26 = re.compile(r'^\s*ICMPv6 DAD parameters:$')
        p27 = re.compile(
            r'^\s*Maximum +DAD +attempts: +(?P<maximum_attempts>\d+)$')
        p28 = re.compile(
            r'^\s*Current +DAD +attempt : +(?P<current_attempt>\d+)$')

        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue

            m = p1.match(line)
            if m:
                group = m.groupdict()
                vrf = group.pop('vrf')
                vrf_dict = result_dict.setdefault(
                    'vrf', {}).setdefault(vrf, {})
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                interface = group.pop('interface')
                interface_dict = vrf_dict.setdefault(
                    'interfaces', {}).setdefault(interface, {})

                interface_dict.update({'interface': interface})
                interface_dict.update(
                    {'oper_status': group.pop("protocol_status")})
                interface_dict.update(
                    {'link_status': group.pop("link_status")})
                interface_dict.update({'enable': True if group.pop(
                    "admin_status").lower() == 'up' else False})
                continue

            m = p4.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({"ip": group.pop("ipv6_address")})
                continue

            m = p5.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update(
                    {"local_address": group.pop("link_address")})
                continue

            m = p6.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update(
                    {"mac_extract": group.pop("nd_mac_extract").lower()})
                continue

            m = p7.match(line)
            if m:
                active_timers_dict = interface_dict.setdefault(
                    'active_timers', {})
                continue

            m = p8.match(line)
            if m:
                group = m.groupdict()
                active_timers_dict.update(
                    {"last_neighbor_solicitation": group.pop("last_neighbor_solicitation_sent")})
                continue

            m = p9.match(line)
            if m:
                group = m.groupdict()
                active_timers_dict.update(
                    {"last_neighbor_advertisement": group.pop("last_neighbor_advertisement_sent")})
                continue

            m = p10.match(line)
            if m:
                group = m.groupdict()
                active_timers_dict.update(
                    {"last_router_advertisement": group.pop("last_router_advertisement_sent")})
                continue

            m = p11.match(line)
            if m:
                group = m.groupdict()
                active_timers_dict.update(
                    {"next_router_advertisement": group.pop("next_router_advertisement_sent")})
                continue

            m = p12.match(line)
            if m:
                router_advertisement_dict = interface_dict.setdefault(
                    'router_advertisement', {})
                continue

            m = p13.match(line)
            if m:
                group = m.groupdict()
                router_advertisement_dict.update(
                    {"interval": int(group.pop("to_interval"))})
                continue

            m = p14.match(line)
            if m:
                group = m.groupdict()
                key = group.pop("router_adv_key").lower().replace(" ", "_")
                value = group.pop("value")
                if value == 'false':
                    value = False
                elif value == 'true':
                    value = True
                else:
                    try:
                        value = int(value)
                    except ValueError:
                        value = value.lower()

                if 'lifetime' in key:
                    key = 'lifetime'
                router_advertisement_dict.update({key: value})
                continue

            m = p17.match(line)
            if m:
                group = m.groupdict()
                router_advertisement_dict.update(
                    {'suppress': True if group.pop("suppress").lower() == 'enabled' else False})
                continue

            m = p18.match(line)
            if m:
                group = m.groupdict()
                router_advertisement_dict.update(
                    {'suppress_mtu': True if group.pop("suppress_mtu").lower() == 'enabled' else False})
                continue

            m = p19.match(line)
            if m:
                group = m.groupdict()
                router_advertisement_dict.update(
                    {'suppress_route_information': True if group.pop("suppress_route_information").lower() == 'enabled' else False})
                continue

            m = p20.match(line)
            if m:
                neighbor_solicitation_dict = interface_dict.setdefault(
                    'neighbor_solicitation', {})
                continue

            m = p21.match(line)
            if m:
                group = m.groupdict()
                neighbor_solicitation_dict.update(
                    {"interval": int(group.pop("retransmit_interval"))})
                continue

            m = p22.match(line)
            if m:
                group = m.groupdict()
                neighbor_solicitation_dict.update({"retry_{}".format(
                    group.pop("nd_nud_retry")): int(group.pop("nd_nud_retry_value"))})
                continue

            m = p23.match(line)
            if m:
                error_message_dict = interface_dict.setdefault(
                    'error_message', {})
                continue

            m = p24.match(line)
            if m:
                group = m.groupdict()
                error_message_dict.update(
                    {'redirects': True if group.pop("redirects") == 'true' else False})
                continue

            m = p25.match(line)
            if m:
                group = m.groupdict()
                error_message_dict.update(
                    {'unreachables': True if group.pop("unreachables") == 'true' else False})
                continue

            m = p26.match(line)
            if m:
                dad_dict = interface_dict.setdefault('dad', {})
                continue

            m = p27.match(line)
            if m:
                group = m.groupdict()
                dad_dict.update(
                    {'maximum_attempts': int(group.pop("maximum_attempts"))})
                continue

            m = p28.match(line)
            if m:
                group = m.groupdict()
                dad_dict.update(
                    {'current_attempt': int(group.pop("current_attempt"))})
                continue

        if result_dict:
            for key in list(result_dict['vrf'].keys()):
                if len(result_dict['vrf'][key]) == 0:
                    result_dict['vrf'].pop(key, None)
        return result_dict

# ====================================================
#  schema for show ipv6 icmp neighbor detail
# ====================================================


class ShowIpv6IcmpNeighborDetailSchema(MetaParser):
    """Schema for:
        show ipv6 icmp neighbor detail
        show ipv6 icmp neighbor detail vrf all
        show ipv6 icmp neighbor detail vrf <vrf>
        show ipv6 icmp neighbor <interface> detail
        show ipv6 icmp neighbor <interface> detail vrf all
        show ipv6 icmp neighbor <interface> detail vrf <vrf>"""

    schema = {
        'interfaces': {
            Any(): {
                'interface': str,
                'neighbors': {
                    Any(): {
                        'ip': str,
                        'link_layer_address': str,
                        'neighbor_state': str,
                        'age': str,
                        Optional('physical_interface'): str,
                    },
                },
            },
        },
    }


# ====================================================
#  parser for show ipv6 icmp neighbor detail
# ====================================================
class ShowIpv6IcmpNeighborDetail(ShowIpv6IcmpNeighborDetailSchema):
    """Parser for :
        show ipv6 icmp neighbor detail
        show ipv6 icmp neighbor detail vrf all
        show ipv6 icmp neighbor detail vrf <vrf>
        show ipv6 icmp neighbor <interface> detail
        show ipv6 icmp neighbor <interface> detail vrf all
        show ipv6 icmp neighbor <interface> detail vrf <vrf>"""

    cli_command = ['show ipv6 icmp neighbor {interface} detail vrf {vrf}',
                   'show ipv6 icmp neighbor {interface} detail',
                   'show ipv6 icmp neighbor detail vrf {vrf}',
                   'show ipv6 icmp neighbor detail', ]
    exclude = ['age']

    def cli(self, vrf="", interface="", output=None):
        if vrf and interface:
            cmd = self.cli_command[0].format(vrf=vrf, interface=interface)
        elif interface:
            cmd = self.cli_command[1].format(interface=interface)
        elif vrf:
            cmd = self.cli_command[2].format(vrf=vrf)
        else:
            cmd = self.cli_command[3]

        # excute command to get output
        if output is None:
            out = self.device.execute(cmd)
        else:
            out = output

        result_dict = {}

        #  ICMPv6 Adjacency Table for all VRFs
        # Address         Age       MAC Address     State      Interface  Phy-Interface
        # 2001:db8:c56d:4::2     00:15:02  fa16.3eff.e5a2  STALE       Eth1/1      Eth1/1

        # ICMPv6 Adjacency Table for all VRFs
        p1 = re.compile(
            r'^\s*ICMPv6 Adjacency Table for +(?P<vrf>[\w]+) +VRFs$')

        p2 = re.compile(r'^\s*(?P<neighbor>[\w\:]+)?( +(?P<age>[\d\:]+)'
                        ' +(?P<link_layer_address>[a-f0-9\.]+) +(?P<neighbor_state>[\w]+) +(?P<interface>[\w\/\.]+)'
                        ' +(?P<physical_interface>[\w\/\.]+))?$')

        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue

            m = p1.match(line)
            if m:
                group = m.groupdict()
                vrf = group.pop('vrf')
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                if group.get('neighbor'):
                    neighbor = group.pop('neighbor')

                if group.get('interface'):
                    interface_original = group.pop('interface')
                    interface = Common.convert_intf_name(interface_original)
                    interface_dict = result_dict.setdefault(
                        'interfaces', {}).setdefault(interface, {})
                    interface_dict.update({'interface': interface})

                    neighbor_dict = interface_dict.setdefault(
                        'neighbors', {}).setdefault(neighbor, {})

                    neighbor_dict.update({'ip': neighbor})
                    neighbor_dict.update(
                        {'link_layer_address': group.pop("link_layer_address")})
                    neighbor_dict.update(
                        {'neighbor_state': group.pop("neighbor_state").lower()})
                    neighbor_dict.update({'age': group.pop("age")})
                    neighbor_dict.update({'physical_interface': Common.convert_intf_name(
                        group.pop("physical_interface"))})
                continue

        return result_dict

# ====================================================
#  schema for show ipv6 routers
# ====================================================


class ShowIpv6RoutersSchema(MetaParser):
    """Schema for:
        show ipv6 routers
        show ipv6 routers vrf all
        show ipv6 routers vrf <vrf>"""

    schema = {
        'interfaces': {
            Any(): {
                'interface': str,
                'neighbors': {
                    Any(): {
                        'ip': str,
                        'is_router': bool,
                        'last_update': str,
                        'current_hop_limit': int,
                        'addr_flag': int,
                        'other_flag': int,
                        'mtu': int,
                        'lifetime': int,
                        'preference': str,
                        'homeagent_flag': int,
                        'retransmission_time': int,
                        'reachable_time': int,
                        Optional('prefix'): {
                            Any(): {
                                'autonomous_flag': int,
                                'onlink_flag': int,
                                'preferred_lifetime': int,
                                'valid_lifetime': int,
                            }
                        }
                    },
                },
            },
        },
    }


# ====================================================
#  parser for show ipv6 routers
# ====================================================
class ShowIpv6Routers(ShowIpv6RoutersSchema):
    """Parser for :
        show ipv6 routers
        show ipv6 routers vrf all
        show ipv6 routers vrf <vrf>"""

    cli_command = ['show ipv6 routers vrf {vrf}', 'show ipv6 routers']
    exclude = ['last_update']

    def cli(self, vrf="", output=None):
        if vrf:
            cmd = self.cli_command[0].format(vrf=vrf)
        else:
            cmd = self.cli_command[1]

        # excute command to get output
        if output is None:
            out = self.device.execute(cmd)
        else:
            out = output

        result_dict = {}

        # Router fe80::f816:3eff:feff:e5a2 on Ethernet1/1 , last update time 3.2 min
        # Router fe80::e6c7:22ff:fe15:4cc1 on port-channel1.100 , last update time 1.3 min
        p1 = re.compile(r'^((?P<router>\w+) )?(?P<neighbor>[a-f0-9\:]+) +on'
                        ' +(?P<interface>[\S]+) +,'
                        ' +last +update +time +(?P<last_update>[\d\.]+) +min$')

        # Current_hop_limit 64, Lifetime 1800, AddrFlag 0, OtherFlag 0, MTU 1500
        p2 = re.compile(r'^Current_hop_limit +(?P<current_hop_limit>\d+), +Lifetime +(?P<lifetime>\d+),'
                        ' +AddrFlag +(?P<addr_flag>\d+), +OtherFlag +(?P<other_flag>\d+),'
                        ' +MTU +(?P<mtu>\d+)$')

        #  HomeAgentFlag 0, Preference Medium
        p3 = re.compile(
            r'^HomeAgentFlag +(?P<homeagentflag>\d+), +Preference +(?P<preference>\w+)$')

        # Reachable time 0 msec, Retransmission time 0 msec
        p4 = re.compile(
            r'^Reachable time +(?P<reachable_time>\d+) +msec, +Retransmission time +(?P<retransmission_time>\d+) +msec$')

        # Prefix 2001:db8:c56d:4::/64  onlink_flag 1 autonomous_flag 1
        # Prefix 2001:db8:c56d:4::/64onlink_flag 1 autonomous_flag 1
        p5 = re.compile(
            r'^Prefix +(?P<prefix>[\w\:\/]+) *onlink_flag +(?P<onlink_flag>\d+) +autonomous_flag +(?P<autonomous_flag>\d+)$')

        #   valid lifetime 2592000, preferred lifetime 604800
        p6 = re.compile(
            r'^valid lifetime +(?P<valid_lifetime>\d+), +preferred lifetime +(?P<preferred_lifetime>\d+)$')

        for line in out.splitlines():
            if line:
                line = line.replace('\t', '    ').strip()
            else:
                continue

            # Router fe80::f816:3eff:feff:e5a2 on Ethernet1/1 , last update time 3.2 min
            # Router fe80::e6c7:22ff:fe15:4cc1 on port-channel1.100 , last update time 1.3 min
            m = p1.match(line)
            if m:
                group = m.groupdict()
                interface = group.pop("interface")
                interface_dict = result_dict.setdefault(
                    'interfaces', {}).setdefault(interface, {})
                interface_dict.update({'interface': interface})
                neighbor = group.pop('neighbor')
                neighbor_dict = interface_dict.setdefault(
                    'neighbors', {}).setdefault(neighbor, {})
                neighbor_dict.update(
                    {'is_router': True if 'router' in group.pop("router").lower() else False})
                neighbor_dict.update({'last_update': group.pop("last_update")})
                neighbor_dict.update({'ip': neighbor})
                continue

            # Current_hop_limit 64, Lifetime 1800, AddrFlag 0, OtherFlag 0, MTU 1500
            m = p2.match(line)
            if m:
                group = m.groupdict()
                neighbor_dict.update({k: int(v) for k, v in group.items()})
                continue

            #  HomeAgentFlag 0, Preference Medium
            m = p3.match(line)
            if m:
                group = m.groupdict()
                neighbor_dict.update(
                    {'homeagent_flag': int(group.pop('homeagentflag'))})
                neighbor_dict.update(
                    {'preference': group.pop('preference').lower()})
                continue

            # Reachable time 0 msec, Retransmission time 0 msec
            m = p4.match(line)
            if m:
                group = m.groupdict()
                neighbor_dict.update({k: int(v) for k, v in group.items()})
                continue

            #   Prefix 2001:db8:c56d:4::/64  onlink_flag 1 autonomous_flag 1
            m = p5.match(line)
            if m:
                group = m.groupdict()
                prefix_dict = neighbor_dict.setdefault(
                    'prefix', {}).setdefault(group.pop('prefix'), {})
                # neighbor_dict.update({'prefix':group.pop('prefix').strip()})
                prefix_dict.update({k: int(v) for k, v in group.items()})
                continue

            #   valid lifetime 2592000, preferred lifetime 604800
            m = p6.match(line)
            if m:
                group = m.groupdict()
                prefix_dict.update({k: int(v) for k, v in group.items()})
                continue
        return result_dict

# =====================================
# Schema for 'show ipv6 neighbor'
# =====================================


class ShowIpv6NeighborSchema(MetaParser):
    """Schema for show ipv6 neighbor"""

    schema = {
        Optional('vrf'): str,
        Optional('statistics'): {
            Optional('entries_total'): int
        },
        'interfaces': {
            Any(): {
                'ipv6': {
                    'neighbors': {
                        Any(): {
                            'ip': str,
                            'link_layer_address': str,
                            'age': str,
                            'origin': str,
                            'physical_interface': str,
                            'pref': int,
                            'source': str
                        }
                    }
                }
            }
        }
    }

# =====================================
# Parser for:
# 	show ipv6 neighbor
# 	show ipv6 neighbor vrf {vrf}
# 	show ipv6 neighbor vrf all
# =====================================


class ShowIpv6Neighbor(ShowIpv6NeighborSchema):
    """Parser for:
        show ipv6 neighbor
        show ipv6 neighbor vrf {vrf}
        show ipv6 neighbor vrf all
    """

    cli_command = ['show ipv6 neighbor', 'show ipv6 neighbor vrf {vrf}']
    exclude = ['age']

    def cli(self, vrf=None, output=None):

        if output is None:
            if vrf:
                cmd = self.cli_command[1].format(vrf=vrf)
            else:
                cmd = self.cli_command[0]
                
            output = self.device.execute(cmd)

        res_dict = {}

        # IPv6 Adjacency Table for VRF default
        # IPv6 Adjacency Table for VRF test
        # IPv6 Adjacency Table for all VRFs
        p1 = re.compile(
            r'^IPv6 +Adjacency +Table +for +(VRF +)?(?P<vrf>[\S]+)( +VRFs)?$')

        # Total number of entries: 2
        p2 = re.compile(
            r'^Total +number +of +entries:\s+(?P<num_entries>\d+)$')

        # Address         Age       MAC Address     Pref Source     Interface
        # 2001:db8:2::3   00:08:40  0000.0000.0203  50   icmpv6     Ethernet1/46

        p3 = re.compile(
            r'^(?P<ip_address>[\w\:]+)\s+(?P<age>[\d:-]+)\s+(?P<mac_address>[\w\.]+)\s+(?P<pref>\d+)\s+(?P<source>[\w]+)\s+(?P<interface>\S+)$')

        for line in output.splitlines():
            line = line.strip()
            # IPv6 Adjacency Table for VRF default
            # IPv6 Adjacency Table for VRF test
            # IPv6 Adjacency Table for all VRFs
            m = p1.match(line)
            if m:
                if 'interfaces' not in res_dict:
                    interfaces_dict = res_dict.setdefault('interfaces', {})

                res_dict.update({'vrf': m.groupdict()['vrf']})
                continue

                # Total number of entries: 2
            m = p2.match(line)

            if m:
                if 'statistics' not in res_dict:
                    statistics_dict = res_dict.setdefault('statistics', {})
                    groups = m.groupdict()
                    statistics_dict.update(
                        {'entries_total': int(groups['num_entries'])})
                    continue

            # Address         Age       MAC Address     Pref Source     Interface
            # 2001:db8:2::3   00:08:40  0000.0000.0203  50   icmpv6     Ethernet1/46
            m = p3.match(line)
            if m:
                # Rare case (but found through run_parsers) - Only used to
                # setup data structure when output lines never match p1
                if 'interfaces' not in res_dict:
                    interfaces_dict = res_dict.setdefault('interfaces', {})

                groups = m.groupdict()
                interface = groups['interface']
                ip_address = groups['ip_address']
                mac_address = groups['mac_address']
                age = groups['age']
                pref = groups['pref']
                source = groups['source']

                interface_dict = interfaces_dict.setdefault(interface, {})
                neighbors_dict = interface_dict.setdefault(
                    'ipv6', {}).setdefault('neighbors', {})
                ip_dict = neighbors_dict.setdefault(ip_address, {})
                ip_dict.update({'ip': ip_address})
                ip_dict.update({'link_layer_address': mac_address})
                ip_dict.update({'physical_interface': interface})
                ip_dict.update({'pref': int(pref)})
                ip_dict.update({'source': source})

                origin = 'static' if '-' in age else 'dynamic'

                ip_dict.update({'origin': origin})
                ip_dict.update({'age': age})
                continue

        return res_dict
