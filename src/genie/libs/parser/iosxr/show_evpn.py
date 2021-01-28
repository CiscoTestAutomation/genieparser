""" show_evpn.py

show evpn parser class

"""

import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional
from genie.libs.parser.utils.common import Common


class ShowEvpnEviSchema(MetaParser):
    schema = {
        'evi': {
            Any(): {
                'bridge_domain': str,
                'type': str,
                Optional('route_target_in_use'): {
                    Any(): {
                        Any(): bool
                    }
                },
                Optional(Any()): str,
            }
        }
    }


class ShowEvpnEvi(ShowEvpnEviSchema):
    """Parser class for 'show evpn evi'"""

    cli_command = 'show evpn evi'

    def cli(self, output=None):

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}
        # 1000  VPWS:1000       VPWS (vlan-unaware)
        # 2000  XC-POD1-EVPN    EVPN
        # 2001  XC-POD2-EVPN    EVPN
        p1 = re.compile(r'^(?P<evi>\d+) +(?P<bridge_domain>\S+) +(?P<type>.+)$')

        # 100:145                        Import
        # 100:145                        Export
        p2 = re.compile(r'^(?P<route_target_in_use>[\d+:\d+]+) +(?P<type>\S+)$')

        # ------------------------------ -------
        p3 = re.compile(r'(-+ *)+$')

        # Unicast Label  : 24001
        # Multicast Label: 16001
        # RD Auto  : (auto) 10.1.100.100:145
        p4 = re.compile(r'^(?P<key>[\S ]+) *: +(?P<value>[\S ]+)$')

        for line in out.splitlines():
            line = line.strip()

            # 1000  VPWS:1000       VPWS (vlan-unaware)
            # 2000  XC-POD1-EVPN    EVPN
            # 2001  XC-POD2-EVPN    EVPN
            m = p1.match(line)
            if m:
                group = m.groupdict()
                evi = int(group['evi'])
                bridge_domain = group['bridge_domain']
                evi_type = group['type']
                evi_dict = ret_dict.setdefault('evi', {}). \
                    setdefault(evi, {})
                evi_dict.update({'bridge_domain': bridge_domain})
                evi_dict.update({'type': evi_type})
                continue

            # 100:145                        Import
            # 100:145                        Export
            m = p2.match(line)
            if m:
                group = m.groupdict()
                route_target_in_use = group['route_target_in_use']
                route_type = group['type']
                type_dict = evi_dict.setdefault('route_target_in_use', {}). \
                    setdefault(route_target_in_use, {})
                type_dict.update({route_type.lower(): True})
                continue

            # ------------------------------ -------
            m = p3.match(line)
            if m:
                continue

            # Unicast Label  : 24001
            # Multicast Label: 16001
            # RD Auto  : (auto) 10.1.100.100:145
            m = p4.match(line)
            if m:
                group = m.groupdict()
                key = group['key'].strip().lower().replace(' ', '_')
                value = group['value'].strip()
                evi_dict.update({key: value})
                continue

        return ret_dict


class ShowEvpnEviDetail(ShowEvpnEvi):
    """Parser class for 'show evpn evi detail' CLI."""

    cli_command = 'show evpn evi detail'

    def cli(self, output=None):
        """parsing mechanism: cli
        """

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        return super().cli(output=out)

# vim: ft=python ts=8 sw=4 et


# =========================================================
# Schema for:
#   * 'show evpn internal-label detail'
#   * 'show evpn internal-label detail location {location}'
# =========================================================
class ShowEvpnInternalLabelDetailSchema(MetaParser):
    '''Schema for:
        * show evpn internal-label detail
    '''

    schema = {
        Optional('evi'): {
            Any(): {
                'evi': int,
                'esi': str,
                'eth_tag': int,
                'label': int,
                Optional('mp_resolved'): bool,
                Optional('mp_info'): str,
                Optional('pathlists'): {
                    Optional('mac'): {
                        'nexthop': {
                            Any(): {
                                'label': int,
                                Optional('df_role'): str,
                            },
                        },
                    },
                    Optional('ead_es'): {
                        'nexthop': {
                            Any(): {
                                'label': int,
                                Optional('df_role'): str,
                            },
                        },
                    },
                    Optional('ead_evi'): {
                        'nexthop': {
                            Any(): {
                                'label': int,
                                Optional('df_role'): str,
                            },
                        },
                    },
                    Optional('summary'): {
                        'nexthop': {
                            Any(): {
                                'label': int,
                                Optional('df_role'): str,
                            },
                        },
                    },
                },
            },
        },
        Optional('vpn_id'): {
            Any(): {
                'vpn_id': int,
                'encap': str,
                'esi': str,
                'eth_tag': int,
                Optional('label'): int,
                Optional('mp_resolved'): bool,
                Optional('mp_info'): str,
                Optional('mp_internal_label'): int,
                Optional('pathlists'): {
                    Optional('mac'): {
                        'nexthop': {
                            Any(): {
                                'label': int,
                                Optional('df_role'): str,
                            },
                        },
                    },
                    Optional('ead_es'): {
                        'nexthop': {
                            Any(): {
                                'label': int,
                                Optional('df_role'): str,
                            },
                        },
                    },
                    Optional('ead_evi'): {
                        'nexthop': {
                            Any(): {
                                'label': int,
                                Optional('df_role'): str,
                            },
                        },
                    },
                    Optional('summary'): {
                        'nexthop': {
                            Any(): {
                                'label': int,
                                Optional('df_role'): str,
                                Optional('value'): str,
                            },
                        },
                    },
                },
            },
        },
    }


# =========================================================
# Parser for:
#   * 'show evpn internal-label detail'
#   * 'show evpn internal-label detail location {location}'
# =========================================================
class ShowEvpnInternalLabelDetail(ShowEvpnInternalLabelDetailSchema):
    '''Parser for:
        * show evpn internal-label detail
        * show evpn internal-label detail location {location}
    '''

    cli_command = ['show evpn internal-label detail',
                   'show evpn internal-label detail location {location}']

    def cli(self, location=None, output=None):

        if output is None:
            if location:
                out = self.device.execute(self.cli_command[1].format(location=location))
            else:
                out = self.device.execute(self.cli_command[0])
        else:
            out = output

        # Init
        parsed_dict = {}

        # EVI   Ethernet Segment Id                     EtherTag Label
        # VPN-ID     Encap  Ethernet Segment Id         EtherTag   Label

        # 5     0012.12ff.0000.0000.0002                0        24114
        # 100   0100.00ff.acce.5500.0100                0        24005
        p1 = re.compile(r'^(?P<evi>(\d+)) +(?P<esi>([a-z0-9\.]+))'
                        r' +(?P<eth_tag>(\d+))( +(?P<label>(\d+)))?$')

        # 16001      VXLAN  0001.04ff.0b0c.0607.0811    0          24002
        # 16003      VXLAN  0001.04ff.0b0c.0607.0811    0          24004
        # 1000       MPLS   0001.00ff.0102.0000.0011    0
        p2 = re.compile(r'^(?P<vpn_id>(\d+)) +(?P<encap>([a-zA-Z]+))'
                        r' +(?P<esi>([a-z0-9\.]+)) +(?P<eth_tag>(\d+))'
                        r'( +(?P<mp_internal_label>(\d+)))?$')

        # Multi-paths resolved: TRUE
        # Multi-paths resolved: TRUE (Remote single-active)
        p3 = re.compile(r'^Multi-paths +resolved: +(?P<mp_resolved>(\S+))'
                        r' +\((?P<mp_info>(.*))\)$')

        # Multi-paths Internal label: 24002
        p4 = re.compile(r'^Multi-paths +Internal +label: +(?P<internal>(\d+))$')
        # Pathlists:
        # MAC     10.70.20.20                              24212
        # EAD/ES  10.10.10.10                              0
        # EAD/EVI 10.10.10.10                              24012
        # Summary 10.70.20.20                              24212
        p5 = re.compile(r'^(?P<type>(MAC|EAD\/ES|EAD\/EVI|Summary))'
                        r' +(?P<nexthop>(\S+)) +(?P<label>(\d+))$')

        #         10.70.20.20                              0
        #         10.10.10.10 (B)                          24012
        p6 = re.compile(r'^(?P<nexthop>(\S+))(?: +\((?P<df_role>(\S+))\))?'
                        r' +(?P<label>(\d+))$')

        # Summary pathlist:
        p7 = re.compile(r'^Summary pathlist:$')

        #   0x03000001 10.76.1.2                                16002
        #   0xffffffff (P) 10.16.2.2                              100001
        p8 = re.compile(r'^(?P<value>(\S+))(?: +(?P<df_role>\(\S+\)))? '
                        r'+(?P<nexthop>(\S+)) +(?P<label>(\d+))$')

        for line in out.splitlines():
            line = line.strip()

            # 5     0012.12ff.0000.0000.0002                0        24114
            m = p1.match(line)
            if m:
                group = m.groupdict()
                sub_dict = parsed_dict.setdefault('evi', {}).setdefault(int(group['evi']), {})
                sub_dict['evi'] = int(group['evi'])
                sub_dict['esi'] = group['esi']
                sub_dict['eth_tag'] = int(group['eth_tag'])
                if group['label']:
                    sub_dict['label'] = int(group['label'])
                continue

            # 16001      VXLAN  0001.04ff.0b0c.0607.0811    0          24002
            # 16003      VXLAN  0001.04ff.0b0c.0607.0811    0          24004
            m = p2.match(line)
            if m:
                group = m.groupdict()
                sub_dict = parsed_dict.setdefault('vpn_id', {}).\
                    setdefault(int(group['vpn_id']), {})
                sub_dict['vpn_id'] = int(group['vpn_id'])
                sub_dict['encap'] = group['encap']
                sub_dict['esi'] = group['esi']
                sub_dict['eth_tag'] = int(group['eth_tag'])
                if group['mp_internal_label']:
                    sub_dict['label'] = int(group['mp_internal_label'])
                continue

            # Multi-paths resolved: TRUE
            # Multi-paths resolved: TRUE (Remote single-active)
            # Multi-paths resolved: TRUE (Remote all-active) (ECMP Disable)
            m = p3.match(line)
            if m:
                sub_dict['mp_resolved'] = True
                if m.groupdict()['mp_info']:
                    mp_info = m.groupdict()['mp_info']
                    sub_dict['mp_info'] = re.sub(r'\) \(', ', ', mp_info)
                continue

            # Multi-paths Internal label: 24002
            m = p4.match(line)
            if m:
                sub_dict['mp_internal_label'] = int(m.groupdict()['internal'])
                continue

            # MAC     10.70.20.20                              24212
            # EAD/ES  10.10.10.10                              0
            # EAD/EVI 10.10.10.10                              24012
            # Summary 10.70.20.20                              24212
            m = p5.match(line)
            if m:
                group = m.groupdict()
                pathlists_dict = sub_dict.setdefault('pathlists', {}).\
                    setdefault(group['type'].lower().replace("/", "_"), {})
                type_nh_dict = pathlists_dict.setdefault('nexthop', {}).\
                    setdefault(group['nexthop'], {})
                type_nh_dict['label'] = int(group['label'])
                continue

            #         10.70.20.20                              0
            #         10.10.10.10 (B)                          24012
            m = p6.match(line)
            if m:
                group = m.groupdict()
                type_nh_dict = pathlists_dict.setdefault('nexthop', {}).\
                    setdefault(group['nexthop'], {})
                type_nh_dict['label'] = int(group['label'])
                if group['df_role']:
                    type_nh_dict['df_role'] = group['df_role']
                continue

            # Summary pathlist:
            m = p7.match(line)
            if m:
                pathlists_dict = sub_dict.setdefault('pathlists', {}).\
                                        setdefault('summary', {})
                continue

            #   0x03000001 10.76.1.2                                16002
            m = p8.match(line)
            if m:
                group = m.groupdict()
                type_nh_dict = pathlists_dict.setdefault('nexthop', {}).\
                    setdefault(group['nexthop'], {})
                type_nh_dict['label'] = int(group['label'])
                type_nh_dict['value'] = group['value']
                if group['df_role']:
                    type_nh_dict['df_role'] = group['df_role']
                continue

        return parsed_dict


class ShowEvpnEviMacSchema(MetaParser):
    ''' Schema for:
        * 'show evpn evi mac'
        * 'show evpn evi mac private'
        * 'show evpn evi vpn-id {vpn_id} mac'
    '''

    schema = {
        'vpn_id': {
            Any(): {
                'mac_address': {
                    Any(): {
                        Optional('encap'): str,
                        'ip_address': str,
                        'next_hop': str,
                        'label': int,
                        Optional('ethernet_tag'): int,
                        Optional('multipaths_resolved'): str,
                        Optional('multipaths_internal_label'): int,
                        Optional('multipaths_local_label'): int,
                        Optional('local_static'): str,
                        Optional('remote_static'): str,
                        Optional('local_ethernet_segment'): str,
                        Optional('ethernet_segment'): str,
                        Optional('remote_ethernet_segment'): str,
                        Optional('local_sequence_number'): int,
                        Optional('remote_sequence_number'): int,
                        Optional('local_encapsulation'): str,
                        Optional('remote_encapsulation'): str,
                        Optional('esi_port_key'): str,
                        Optional('source'): str,
                        Optional('flush_requested'): int,
                        Optional('flush_received'): int,
                        Optional('flush_count'): int,
                        Optional('flush_seq_id'): int,
                        Optional('static'): str,
                        Optional('soo_nexthop'): str,
                        Optional('bp_xcid'): str,
                        Optional('bp_ifh'): str,
                        Optional('mac_state'): str,
                        Optional('mac_producers'): str,
                        Optional('local_router_mac'): str,
                        Optional('l3_label'): int,
                        Optional('object'): {
                            Any(): {
                                Optional('base_info'): {
                                    'version': str,
                                    'flags': str,
                                    'type': int,
                                    'reserved': int
                                },
                                Optional('num_events'): int,
                                Optional('event_history'): {
                                    Any(): {
                                        'time': str,
                                        'event': str,
                                        'flag_1': str,
                                        'flag_2': str,
                                        'code_1': str,
                                        'code_2': str,
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }


# =====================================================
# Parser for:
#   * 'show evpn evi mac'
#   * 'show evpn evi vpn-id {vpn_id} mac'
# =====================================================

class ShowEvpnEviMac(ShowEvpnEviMacSchema):
    ''' Parser for:
        * 'show evpn evi mac'
        * 'show evpn evi vpn-id {vpn_id} mac'
    '''

    cli_command = ['show evpn evi mac',
                   'show evpn evi vpn-id {vpn_id} mac']

    def cli(self, vpn_id=None, output=None):
        ret_dict = {}
        event_history_index = {}

        if output is None:
            cmd = self.cli_command[1].format(vpn_id=vpn_id) if vpn_id else self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        # 65535      N/A    0000.0000.0000 ::                                       Local                             0
        p1 = re.compile(r'^(?P<vpn_id>\d+)( +(?P<encap>\S+))? +(?P<mac_address>[\w\.]+) +'
                        r'(?P<ip_address>[\w:\.]+) +(?P<next_hop>[\S ]+) +(?P<label>\d+)$')

        # 001b.01ff.0001 N/A                                     24014    7
        p1_1 = re.compile(r'^(?P<mac_address>\S+) +(?P<next_hop>\S+) +(?P<label>\d+) +(?P<vpn_id>\d+)$')

        # IP Address   : 10.196.7.8
        p1_2 = re.compile(r'^IP +Address +: +(?P<ip_address>\S+)$')

        # Ethernet Tag                            : 0
        p2 = re.compile(r'^Ethernet +Tag +: +(?P<ethernet_tag>\d+)$')

        # Multi-paths Resolved                    : False
        p3 = re.compile(r'^Multi-paths +Resolved +: +(?P<multipaths_resolved>\S+)$')

        # Multi-paths Internal label              : 0
        p4 = re.compile(r'^Multi-paths +Internal +label +: +(?P<multipaths_internal_label>\d+)$')

        # Multi-paths Local Label
        p4_1 = re.compile(r'^Multi-paths +Local +Label +: +(?P<multipaths_local_label>\d+)$')

        # Local Static                            : No
        p5 = re.compile(r'^Local +Static +: +(?P<local_static>\S+)$')

        # Remote Static                           : No
        p6 = re.compile(r'^Remote +Static +: +(?P<remote_static>\S+)$')

        # Local Ethernet Segment                  : 0000.0000.0000.0000.0000
        p7 = re.compile(r'^Local +Ethernet +Segment +: +(?P<local_ethernet_segment>\S+)$')

        # Ether.Segment: 0000.0000.0000.0000.0000
        p7_1 = re.compile(r'^Ether\S+Segment *: +(?P<ethernet_segment>\S+)$')

        # Remote Ethernet Segment                 : 0000.0000.0000.0000.0000
        p8 = re.compile(r'^Remote +Ethernet +Segment +: +(?P<remote_ethernet_segment>\S+)$')

        # Local Sequence Number                   : 0
        p9 = re.compile(r'^Local +Sequence +Number +: +(?P<local_sequence_number>\d+)$')

        # Remote Sequence Number                  : 0
        p10 = re.compile(r'^Remote +Sequence +Number +: +(?P<remote_sequence_number>\d+)$')

        # Local Encapsulation                     : N/A
        p11 = re.compile(r'^Local +Encapsulation +: +(?P<local_encapsulation>\S+)$')

        # Remote Encapsulation                    : N/A
        p12 = re.compile(r'^Remote +Encapsulation +: +(?P<remote_encapsulation>\S+)$')

        # ESI Port Key                            : 0
        # ESI Port Key                            : bef5
        p13 = re.compile(r'^ESI +Port +Key +: +(?P<esi_port_key>\w+)$')

        # Source                                  : Local
        p14 = re.compile(r'^Source +: +(?P<source>\S+)$')

        # Flush Requested                         : 0
        p15 = re.compile(r'^Flush +Requested +: +(?P<flush_requested>\d+)$')

        # Flush Received                          : 0
        p16 = re.compile(r'^Flush +Received +: +(?P<flush_received>\d+)$')

        # SOO Nexthop                             : ::
        p17 = re.compile(r'^SOO +Nexthop +: +(?P<soo_nexthop>\S+)$')

        # BP XCID                                 : 0xffffffff
        p18 = re.compile(r'^BP +XCID +: +(?P<bp_xcid>\S+)$')

        # MAC State                               : Init
        p19 = re.compile(r'^MAC +State +: +(?P<mac_state>[\S ]+)$')

        # MAC Producers                           : 0x0 (Best: 0x0)
        p20 = re.compile(r'^MAC +Producers +: +(?P<mac_producers>[\S ]+)$')

        # Local Router MAC                        : 0000.0000.0000
        p21 = re.compile(r'^Local +Router +MAC +: +(?P<local_router_mac>\S+)$')

        # L3 Label                                : 0
        p22 = re.compile(r'^L3 +Label +: +(?P<l3_label>\d+)$')

        # Object: EVPN MAC
        p23 = re.compile(r'^Object: +(?P<object_name>[\S ]+)$')

        # Base info: version=0xdbdb0008, flags=0x4000, type=8, reserved=0
        p24 = re.compile(r'^Base info: +version=(?P<version>\S+), +flags=(?P<flags>\S+)'
                         r', +type=(?P<type>\d+), +reserved=(?P<reserved>\d+)$')

        # EVPN MAC event history  [Num events: 0]
        p25 = re.compile(r'^EVPN +MAC +event +history +\[Num +events: +(?P<num_events>\d+)\]$')

        # Jun 14 14:02:12.864 Create                        00000000, 00000000 -  -
        # Jun 14 14:02:12.864 MAC advertise rejected        00000003, 00000000 -  -
        # Aug 15 22:10:12.736  Create                       00000000 00000001 -  -
        # Sep 24 07:09:27.424 L2RIB Download                0001888a, 01010000 -  -
        p26 = re.compile(r'^(?P<time>\w+ +\d+ +\S+) +(?P<event>[\S ]+) +(?P<flag_1>\w+)'
                         r',? +(?P<flag_2>\w+) +(?P<code_1>\S+) +(?P<code_2>\S+)$')

        # Flush Count  : 0
        p27 = re.compile(r'^Flush +Count *: +(?P<flush_count>\d+)$')

        # BP IFH: 0
        p28 = re.compile(r'^BP +IFH: +(?P<bp_ifh>\d+)$')

        # Flush Seq ID : 0
        p29 = re.compile(r'^Flush +Seq +ID +: +(?P<flush_seq_id>\d+)$')

        # Static: No
        p30 = re.compile(r'^Static *: +(?P<static>\S+)$')

        for line in out.splitlines():
            line = line.strip()

            # 65535      N/A    0000.0000.0000 ::                                       Local                         0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                vpn_id = int(group['vpn_id'])
                encap = group['encap']
                mac_address = group['mac_address']
                ip_address = group['ip_address']
                next_hop = group['next_hop'].strip()
                label = int(group['label'])

                vpn_id_dict = ret_dict.setdefault('vpn_id', {}). \
                    setdefault(vpn_id, {}). \
                    setdefault('mac_address', {}). \
                    setdefault(mac_address, {})
                if encap:
                    vpn_id_dict.update({'encap': encap})
                vpn_id_dict.update({'ip_address': ip_address})
                vpn_id_dict.update({'next_hop': next_hop})
                vpn_id_dict.update({'label': label})
                continue

            # 001b.01ff.0001 N/A                                     24014    7
            m = p1_1.match(line)
            if m:
                group = m.groupdict()
                vpn_id = int(group['vpn_id'])
                mac_address = group['mac_address']
                next_hop = group['next_hop'].strip()
                label = int(group['label'])

                vpn_id_dict = ret_dict.setdefault('vpn_id', {}). \
                    setdefault(vpn_id, {}). \
                    setdefault('mac_address', {}). \
                    setdefault(mac_address, {})
                vpn_id_dict.update({'next_hop': next_hop})
                vpn_id_dict.update({'label': label})
                continue

            # IP Address   : 10.196.7.8
            m = p1_2.match(line)
            if m:
                group = m.groupdict()
                ip_address = group['ip_address']
                vpn_id_dict.update({'ip_address': ip_address})
                continue

            # Ethernet Tag                            : 0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                vpn_id_dict.update({k: int(v) for k, v in group.items() if v is not None})
                continue

            # Multi-paths Resolved                    : False
            m = p3.match(line)
            if m:
                group = m.groupdict()
                vpn_id_dict.update({k: v for k, v in group.items() if v is not None})
                continue

            # Multi-paths Internal label              : 0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                vpn_id_dict.update({k: int(v) for k, v in group.items() if v is not None})
                continue

            # Multi-paths Local Label                 : 0
            m = p4_1.match(line)
            if m:
                group = m.groupdict()
                vpn_id_dict.update({k: int(v) for k, v in group.items() if v is not None})
                continue

            # Local Static                            : No
            m = p5.match(line)
            if m:
                group = m.groupdict()
                vpn_id_dict.update({k: v for k, v in group.items() if v is not None})
                continue

            # Remote Static                           : No
            m = p6.match(line)
            if m:
                group = m.groupdict()
                vpn_id_dict.update({k: v for k, v in group.items() if v is not None})
                continue

            # Local Ethernet Segment                  : 0000.0000.0000.0000.0000
            m = p7.match(line)
            if m:
                group = m.groupdict()
                vpn_id_dict.update({k: v for k, v in group.items() if v is not None})
                continue

            # Ether.Segment: 0000.0000.0000.0000.0000
            m = p7_1.match(line)
            if m:
                group = m.groupdict()
                vpn_id_dict.update({k: v for k, v in group.items() if v is not None})
                continue

            # Remote Ethernet Segment                 : 0000.0000.0000.0000.0000
            m = p8.match(line)
            if m:
                group = m.groupdict()
                vpn_id_dict.update({k: v for k, v in group.items() if v is not None})
                continue

            # Local Sequence Number                   : 0
            m = p9.match(line)
            if m:
                group = m.groupdict()
                vpn_id_dict.update({k: int(v) for k, v in group.items() if v is not None})
                continue

            # Remote Sequence Number                  : 0
            m = p10.match(line)
            if m:
                group = m.groupdict()
                vpn_id_dict.update({k: int(v) for k, v in group.items() if v is not None})
                continue

            # Local Encapsulation                     : N/A
            m = p11.match(line)
            if m:
                group = m.groupdict()
                vpn_id_dict.update({k: v for k, v in group.items() if v is not None})
                continue

            # Remote Encapsulation                    : N/A
            m = p12.match(line)
            if m:
                group = m.groupdict()
                vpn_id_dict.update({k: v for k, v in group.items() if v is not None})
                continue

            # ESI Port Key                            : 0
            # ESI Port Key                            : bef5
            m = p13.match(line)
            if m:
                group = m.groupdict()
                vpn_id_dict.update({k: v for k, v in group.items() if v is not None})
                continue

            # Source                                  : Local
            m = p14.match(line)
            if m:
                group = m.groupdict()
                vpn_id_dict.update({k: v for k, v in group.items() if v is not None})
                continue

            # Flush Requested                         : 0
            m = p15.match(line)
            if m:
                group = m.groupdict()
                vpn_id_dict.update({k: int(v) for k, v in group.items() if v is not None})
                continue

            # Flush Received                          : 0
            m = p16.match(line)
            if m:
                group = m.groupdict()
                vpn_id_dict.update({k: int(v) for k, v in group.items() if v is not None})
                continue

            # SOO Nexthop                             : ::
            m = p17.match(line)
            if m:
                group = m.groupdict()
                vpn_id_dict.update({k: v for k, v in group.items() if v is not None})
                continue

            # BP XCID                                 : 0xffffffff
            m = p18.match(line)
            if m:
                group = m.groupdict()
                vpn_id_dict.update({k: v for k, v in group.items() if v is not None})
                continue

            # MAC State                               : Init
            m = p19.match(line)
            if m:
                group = m.groupdict()
                vpn_id_dict.update({k: v for k, v in group.items() if v is not None})
                continue

            # MAC Producers                           : 0x0 (Best: 0x0)
            m = p20.match(line)
            if m:
                group = m.groupdict()
                vpn_id_dict.update({k: v for k, v in group.items() if v is not None})
                continue

            # Local Router MAC                        : 0000.0000.0000
            m = p21.match(line)
            if m:
                group = m.groupdict()
                vpn_id_dict.update({k: v for k, v in group.items() if v is not None})
                continue

            # L3 Label                                : 0
            m = p22.match(line)
            if m:
                group = m.groupdict()
                vpn_id_dict.update({k: int(v) for k, v in group.items() if v is not None})
                continue

            # Object: EVPN MAC
            m = p23.match(line)
            if m:
                group = m.groupdict()
                object_name = group['object_name']
                object_dict = vpn_id_dict.setdefault('object', {}). \
                    setdefault(object_name, {})
                continue

            # Base info: version=0xdbdb0008, flags=0x4000, type=8, reserved=0
            m = p24.match(line)
            if m:
                group = m.groupdict()
                version = group['version']
                flags = group['flags']
                base_info_type = int(group['type'])
                reserved = int(group['reserved'])
                base_info_dict = object_dict.setdefault('base_info', {})
                base_info_dict.update({'version': version})
                base_info_dict.update({'flags': flags})
                base_info_dict.update({'type': base_info_type})
                base_info_dict.update({'reserved': reserved})
                continue

            # EVPN MAC event history  [Num events: 0]
            m = p25.match(line)
            if m:
                group = m.groupdict()
                object_dict.update({k: int(v) for k, v in group.items() if v is not None})
                continue

            # Jun 14 14:02:12.864 Create                        00000000, 00000000 -  -
            # Jun 14 14:02:12.864 MAC advertise rejected        00000003, 00000000 -  -
            # Aug 15 22:10:12.992 API Provision                 00000000 00000000 -  -
            # Aug 15 22:10:12.992 API BP Ifname delete          45138200 0aa6ab70 M  -
            m = p26.match(line)
            if m:
                group = m.groupdict()
                index = event_history_index.get('event_history', 0) + 1
                event_history_dict = object_dict.setdefault('event_history', {}). \
                    setdefault(index, {})
                event_history_dict.update({k: v.strip() for k, v in group.items() if v is not None})
                event_history_index.update({'event_history': index})
                continue

            # Flush Count  : 0
            m = p27.match(line)
            if m:
                group = m.groupdict()
                vpn_id_dict.update({k: int(v) for k, v in group.items() if v is not None})
                continue

            # # BP IFH: 0
            m = p28.match(line)
            if m:
                group = m.groupdict()
                vpn_id_dict.update({k: v for k, v in group.items() if v is not None})
                continue

            # Flush Seq ID : 0
            m = p29.match(line)
            if m:
                group = m.groupdict()
                vpn_id_dict.update({k: int(v) for k, v in group.items() if v is not None})
                continue

            # Static: No
            m = p30.match(line)
            if m:
                group = m.groupdict()
                vpn_id_dict.update({k: v for k, v in group.items() if v is not None})
                continue

        return ret_dict


# =====================================================
# Parser for:
#   * 'show evpn evi mac private'
# =====================================================

class ShowEvpnEviMacPrivate(ShowEvpnEviMac):
    """Parser class for 'show evpn evi mac private' CLI."""

    cli_command = 'show evpn evi mac private'

    def cli(self, output=None):
        """parsing mechanism: cli
        """

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        return super().cli(output=out)


class ShowEvpnEthernetSegmentSchema(MetaParser):
    schema = {
        'segment_id': {
            Any(): {
                'interface': {
                    Any(): {
                        'next_hops': list,
                        Optional('es_to_bgp_gates'): str,
                        Optional('es_to_l2fib_gates'): str,
                        Optional('main_port'): {
                            'interface': str,
                            Optional('interface_mac'): str,
                            'if_handle': str,
                            'state': str,
                            'redundancy': str,
                        },
                        Optional('esi'): {
                            'type': str,
                            Optional('value'): str,
                            Optional('system_id'): str,
                            Optional('port_key'): str,
                        },
                        Optional('value'): str,
                        Optional('es_import_rt'): str,
                        Optional('source_mac'): str,
                        Optional('topology'): {
                            'operational': str,
                            'configured': str,
                        },
                        Optional('primary_services'): str,
                        Optional('secondary_services'): str,
                        Optional('service_carving'): str,
                        Optional('peering_details'): list,
                        Optional('service_carving_results'): {
                            Optional('forwarders'): int,
                            Optional('permanent'): int,
                            Optional('bridge_ports'): {
                                'num_of_total': int,
                            },
                            'elected': {
                                'num_of_total': int,
                                Optional('i_sid_e'): list,
                            },
                            'not_elected': {
                                'num_of_total': int,
                                Optional('i_sid_ne'): list,
                            },
                        },
                        Optional('mac_flushing_mode'): str,
                        Optional('peering_timer'): str,
                        Optional('recovery_timer'): str,
                        Optional('carving_timer'): str,
                        Optional('local_shg_label'): str,
                        Optional('remote_shg_labels'): {
                            Any(): {
                                Optional('label'): {
                                    Any(): {
                                        'nexthop': str
                                    }
                                }
                            }
                        },
                        Optional('flush_again_timer'): str,
                        Optional('object'): {
                            Any(): {
                                Optional('base_info'): {
                                    'version': str,
                                    'flags': str,
                                    'type': int,
                                    'reserved': int
                                },
                                Optional('num_events'): int,
                                Optional('event_history'): {
                                    Any(): {
                                        'time': str,
                                        'event': str,
                                        'flag_1': str,
                                        'flag_2': str,
                                        'code_1': str,
                                        'code_2': str,
                                    }
                                },
                                Optional('statistics'): {
                                    Any(): {
                                        'adv_cnt': int,
                                        Optional('adv_last_time'): str,
                                        'adv_last_arg': str,
                                        Optional('wdw_cnt'): int,
                                        Optional('wdw_last_time'): str,
                                        Optional('wdw_last_arg'): str,
                                    }
                                }
                            }
                        },
                        Optional('es_ead_update'): {
                            'num_rds': int,
                            Optional('rd'): {
                                Any(): {
                                    Optional('num_rts'): int,
                                    Optional('rt_list'): list,
                                }
                            }
                        },
                        Optional('chkpt_objid'): str,
                        Optional('checkpoint_info'): {
                            Optional('msti_mask'): str,
                            Optional('if_type'): int,
                            Optional('nexthop'): list,
                        },
                        Optional(Any()): Any()
                    }
                }
            }
        }
    }


class ShowEvpnEthernetSegment(ShowEvpnEthernetSegmentSchema):
    """Parser class for 'show evpn ethernet-segment' CLI."""

    cli_command = 'show evpn ethernet-segment'

    def cli(self, output=None):
        """parsing mechanism: cli
        """

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}
        # num_of_label = {}
        event_history_index = {}
        key_dict = {
            'diagnosticesrt': 'diagnostic_es_rt'
        }
        detail_type = None

        # 0210.03ff.9e00.0210.0000 Gi0/3/0/0      10.1.100.100
        # 0210.03ff.9e00.0210.0000 BE4                                78.81.321.95<
        p1 = re.compile(r'^(?P<segment_id>(\w+\.\w+\.\w+\.\w+\.\w+|N/A)) +(?P<interface>\S+) +(?P<next_hop>[\d\.\<]+)$')

        # 10.204.100.100
        p1_1 = re.compile(r'^(?P<next_hop>[\d\.]+)$')

        # ES to BGP Gates   : Ready
        p2 = re.compile(r'^ES +to +BGP +Gates +: +(?P<es_to_bgp_gates>\S+)$')

        # ES to L2FIB Gates : Ready
        p3 = re.compile(r'^ES +to +L2FIB +Gates +: +(?P<es_to_l2fib_gates>\S+)$')

        # Interface name : GigabitEthernet0/3/0/0
        p4 = re.compile(r'^Interface name +: +(?P<interface>\S+)$')

        # Interface MAC  : 008a.96ff.1d22
        p4_1 = re.compile(r'^Interface +MAC *: +(?P<interface_mac>[\S ]+)$')

        # IfHandle       : 0x1800300
        p5 = re.compile(r'^IfHandle +: +(?P<if_handle>\S+)$')

        # State          : Up
        p6 = re.compile(r'^State + : +(?P<state>\S+)$')

        # Redundancy     : Not Defined
        p7 = re.compile(r'^Redundancy +: +(?P<redundancy>[\S ]+)$')

        # Source MAC        : 0001.edff.9e9f (PBB BSA)
        p8 = re.compile(r'^Source +MAC +: +(?P<source_mac>[\S ]+)$')

        # Operational    : MHN
        # Operational    : MH, All-active
        p9 = re.compile(r'^Operational +: +(?P<operational>[\S+ ]+)$')

        # Configured     : A/A per service (default)
        p10 = re.compile(r'^Configured +: +(?P<configured>[\S ]+)$')

        # Primary Services  : Auto-selection
        p11 = re.compile(r'^Primary +Services +: +(?P<primary_services>\S+)$')

        # Secondary Services: Auto-selection
        p12 = re.compile(r'^Secondary +Services *: +(?P<secondary_services>\S+)$')

        # Bridge ports   : 3
        p13 = re.compile(r'^Bridge +ports +: +(?P<bridge_ports>\d+)$')

        # Elected        : 0
        p14 = re.compile(r'^Elected +: +(?P<elected>\d+)$')

        # Not Elected    : 3
        p15 = re.compile(r'^Not +Elected +: +(?P<not_elected>\d+)$')

        # I-Sid E  :  1450101, 1650205, 1850309
        p16 = re.compile(r'^I-Sid +E +: +(?P<i_sid_e>[\S ]+)$')

        # I-Sid NE  :  1450101, 1650205, 1850309
        p16_1 = re.compile(r'^I-Sid +NE +: +(?P<i_sid_ne>[\S ]+)$')

        # MAC Flushing mode : STP-TCN
        p17 = re.compile(r'^MAC +Flushing +mode +: +(?P<mac_flushing_mode>\S+)$')

        # Peering timer     : 45 sec [not running]
        p18 = re.compile(r'^Peering +timer +: +(?P<peering_timer>[\S ]+)$')

        # Recovery timer    : 20 sec [not running]
        p19 = re.compile(r'^Recovery +timer +: +(?P<recovery_timer>[\S ]+)$')

        # Flushagain timer  : 60 sec
        p20 = re.compile(r'^Flushagain +timer +: +(?P<flush_again_timer>[\S ]+)$')

        # ESI type          : 0
        p21 = re.compile(r'^ESI +type *: +(?P<esi_type>\S+)$')

        # Value          : 36.3700.00ff.0000.1100
        p22 = re.compile(r'^Value *: +(?P<value>[\S ]+)$')

        # ES Import RT      : 3637.00ff.0000 (from ESI)
        p23 = re.compile(r'^ES +Import +RT *: +(?P<es_import_rt>[\S ]+)$')

        # Service Carving   : Auto-selection
        p24 = re.compile(r'^Service +Carving *: +(?P<service_carving>[\S ]+)$')

        # Peering Details   : 10.36.3.36[MOD:P:00] 10.36.3.37[MOD:P:00]
        p25 = re.compile(r'^Peering +Details *: +(?P<peering_details>[\S ]+)$')

        # Forwarders     : 1
        p26 = re.compile(r'^Forwarders *: +(?P<forwarders>\d+)$')

        # Permanent      : 0
        p27 = re.compile(r'^Permanent *: +(?P<permanent>\d+)$')

        # Carving timer     : 0 sec [not running]
        p28 = re.compile(r'^Carving +timer *: +(?P<carving_timer>[\S ]+)$')

        # Local SHG label   : 64005
        # Local SHG label   : None
        p29 = re.compile(r'^Local +SHG +label *: +(?P<local_shg_label>\S+)$')

        # Remote SHG labels : 1
        p30 = re.compile(r'^Remote +SHG +labels? *: +(?P<remote_shg_label>\d+)$')

        # 64005 : nexthop 10.36.3.37
        p31 = re.compile(r'^(?P<shg_label>\d+) *: +nexthop +(?P<next_hop>\S+)$')

        # Object: EVPN MAC
        p32 = re.compile(r'^Object: +(?P<object_name>[\S ]+)$')

        # Base info: version=0xdbdb0008, flags=0x4000, type=8, reserved=0
        p33 = re.compile(r'^Base info: +version=(?P<version>\S+), +flags=(?P<flags>\S+)'
                         r', +type=(?P<type>\d+), +reserved=(?P<reserved>\d+)$')

        # EVPN ES event history  [Num events: 0]
        p34 = re.compile(r'^EVPN +ES +event +history +\[Num +events: +(?P<num_events>\d+)\]$')

        # Jun 14 14:02:12.864 Create                        00000000, 00000000 -  -
        # Jun 14 14:02:12.864 MAC advertise rejected        00000003, 00000000 -  -
        # Aug 15 22:10:12.992 API Provision                 00000000 00000000 -  -
        # Aug 15 22:10:12.992 API BP Ifname delete          45138200 0aa6ab70 M  -
        p35 = re.compile(r'^(?P<time>\w+ +\d+ +\S+) +(?P<event>[\S ]+) +(?P<flag_1>[\d\w]+)'
                         r',? +(?P<flag_2>[\d\w]+) +(?P<code_1>\S+) +(?P<code_2>\S+)$')

        # EVPN ES Statistics
        # p36 = re.compile(r'^EVPN +ES +Statistics$')

        # RT|   1 27/08 09:49:15.582 00000000|   0                    00000000
        # LocalBMAC|   0                    00000000|   0                    00000000
        # ESI|   0                    00000000|   0                    00000000
        p37 = re.compile(r'^(?P<label>[\S ]+)\| +(?P<adv_cnt>\d+)( +(?P<adv_last_time>\d+\/\d+ +\S+))?'
                         r' +(?P<adv_last_arg>[\w\d]+)\|( +(?P<wdw_cnt>\d+))?( +(?P<wdw_last_time>\d+\/\d+ +\S+))?'
                         r'( +(?P<wdw_last_arg>[\w\d]+))?$')

        # Num RDs:       : 1
        p38 = re.compile(r'^Num +RDs: *: +(?P<num_rds>\d+)$')

        # Diagnostic ESI : N/A                     Interface Name : N/A
        # Diagnostic Flag: 0x00000043              DiagnosticES-RT: 0000.0000.0000
        # Port Key       : 0x000088d4              MAC winner     : 1
        p39 = re.compile(r'^(?P<label_1>[\S ]+): +(?P<val_1>\S+)( +\((?P<per_es_1>\w+)\))? +(?P<label_2>[\S ]+): +(?P<val_2>\S+)( +\((?P<per_es_2>\w+)\))?$')  # noqa

        # Carving Timer  : 0    (global)
        # Number of EVIs : 1
        p40 = re.compile(r'^(?P<label_1>[\S ]+): +(?P<val_1>\S+)( +\((?P<per_es_1>\w+)\))?$')

        # RD: 10.154.219.84:1, Num RTs: 1      RT List:
        p41 = re.compile(r'^RD: +(?P<rd>\S+), +Num +RTs: +(?P<num_rts>\d+) +RT +List:( +(?P<rt_list>\d+:\d+))?$')

        # 4:1000,
        # 00:1, 100:2, 100:3, 100:4, 100:5,
        # 100:6, 100:13, 100:14, 100:15, 100:16,
        # 100:17, 100:18,
        p42 = re.compile(r'^(?P<rt_list>((\d+:\d+), ?)+)$')

        # Chkpt ObjId    : 0x40002f18
        p43 = re.compile(r'^Chkpt +ObjId *: +(?P<chkpt_objid>\S+)$')

        # MSTi Mask      : 0x7fff
        p44 = re.compile(r'^MSTi +Mask *: +(?P<msti_mask>\S+)$')

        # 192.168.0.1 [MOD:P:00][1]
        p45 = re.compile(r'^(?P<nexthop>\d+\.\d+\.\d+\.\d+) +(?P<nexthopinfo>\[\S+\])$')

        # IF Type      : 1
        p46 = re.compile(r'^IF +Type *: +(?P<if_type>\d+)$')

        # Peering Details   :
        p47 = re.compile(r'^Peering +Details *:$')

        # EVPN-VPWS Service Carving Results:
        p48 = re.compile(r'^EVPN-VPWS +Service +Carving +Results:$')

        # Primary        : 0
        p49 = re.compile(r'^Primary +: +(?P<primary>\d+)$')

        # Backup         : 0
        p50 = re.compile(r'^Backup +: +(?P<backup>\d+)$')

        # Non-DF         : 18
        p51 = re.compile(r'^Non-DF +: +(?P<non_df>\d+)$')

        # Checkpoint Info:
        p52 = re.compile(r'^Checkpoint +Info:$')

        interface_dict = {}
        for line in out.splitlines():
            line = line.strip()
            # ES to L2FIB Gates : Ready
            m = p2.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({k: v for k, v in group.items() if v is not None})
                continue

            # ES to L2FIB Gates : Ready
            m = p3.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({k: v for k, v in group.items() if v is not None})
                continue

            # Interface name : GigabitEthernet0/3/0/0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                main_port_dict = interface_dict.setdefault('main_port', {})
                main_port_dict.update({k: v for k, v in group.items() if v is not None})
                continue

            # Interface MAC  : 008a.96ff.1d22
            m = p4_1.match(line)
            if m:
                group = m.groupdict()
                main_port_dict = interface_dict.setdefault('main_port', {})
                main_port_dict.update({k: v for k, v in group.items() if v is not None})
                continue

            # IfHandle       : 0x1800300
            m = p5.match(line)
            if m:
                group = m.groupdict()
                main_port_dict = interface_dict.setdefault('main_port', {})
                main_port_dict.update({k: v for k, v in group.items() if v is not None})
                continue

            # State          : Up
            m = p6.match(line)
            if m:
                group = m.groupdict()
                main_port_dict = interface_dict.setdefault('main_port', {})
                main_port_dict.update({k: v for k, v in group.items() if v is not None})
                continue

            # Redundancy     : Not Defined
            m = p7.match(line)
            if m:
                group = m.groupdict()
                main_port_dict = interface_dict.setdefault('main_port', {})
                main_port_dict.update({k: v for k, v in group.items() if v is not None})
                continue

            # Source MAC        : 0001.edff.9e9f (PBB BSA)
            m = p8.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({k: v for k, v in group.items() if v is not None})
                continue

            # Operational    : MHN
            m = p9.match(line)
            if m:
                group = m.groupdict()
                topology_dict = interface_dict.setdefault('topology', {})
                topology_dict.update({k: v for k, v in group.items() if v is not None})
                continue

            # Configured     : A/A per service (default)
            m = p10.match(line)
            if m:
                group = m.groupdict()
                topology_dict = interface_dict.setdefault('topology', {})
                topology_dict.update({k: v for k, v in group.items() if v is not None})
                continue

            # Primary Services  : Auto-selection
            m = p11.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({k: v for k, v in group.items() if v is not None})
                continue

            # Secondary Services: Auto-selection
            m = p12.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({k: v for k, v in group.items() if v is not None})
                continue

            # Bridge ports   : 3
            m = p13.match(line)
            if m:
                group = m.groupdict()
                bridge_ports = int(group['bridge_ports'])
                bridge_ports_dict = interface_dict.setdefault('service_carving_results', {}). \
                    setdefault('bridge_ports', {})
                bridge_ports_dict.update({'num_of_total': bridge_ports})
                continue

            # Elected        : 0
            m = p14.match(line)
            if m:
                group = m.groupdict()
                elected = int(group['elected'])
                elected_dict = interface_dict.setdefault('service_carving_results', {}). \
                    setdefault('elected', {})
                elected_dict.update({'num_of_total': elected})
                continue

            # Not Elected    : 3
            m = p15.match(line)
            if m:
                group = m.groupdict()
                not_elected = int(group['not_elected'])
                not_elected_dict = interface_dict.setdefault('service_carving_results', {}). \
                    setdefault('not_elected', {})
                not_elected_dict.update({'num_of_total': not_elected})
                continue

            # I-Sid E  :  1450101, 1650205, 1850309
            m = p16.match(line)
            if m:
                group = m.groupdict()
                i_sid_e = group['i_sid_e']
                elected_dict.update({'i_sid_e': i_sid_e.replace(' ', '').split(',')})
                continue

            # I-Sid NE  :  1450101, 1650205, 1850309
            m = p16_1.match(line)
            if m:
                group = m.groupdict()
                i_sid_ne = group['i_sid_ne']
                not_elected_dict.update({'i_sid_ne': i_sid_ne.replace(' ', '').split(',')})
                continue

            # MAC Flushing mode : STP-TCN
            m = p17.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({k: v for k, v in group.items() if v is not None})
                continue

            # Peering timer     : 45 sec [not running]
            m = p18.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({k: v for k, v in group.items() if v is not None})
                continue

            # Recovery timer    : 20 sec [not running]
            m = p19.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({k: v for k, v in group.items() if v is not None})
                continue

            # Flushagain timer  : 60 sec
            m = p20.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({k: v for k, v in group.items() if v is not None})
                continue

            # ESI type          : 0
            # ESI type          : Invalid
            m = p21.match(line)
            if m:
                group = m.groupdict()
                esi_type = group['esi_type']
                esi_dict = interface_dict.setdefault('esi', {})
                esi_dict.update({'type': esi_type})
                continue

            # Value          : 36.3700.00ff.0000.1100
            m = p22.match(line)
            if m:
                group = m.groupdict()
                esi_value = group['value']
                esi_dict.update({'value': esi_value})
                continue

            # ES Import RT      : 3637.00ff.0000 (from ESI)
            m = p23.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({k: v for k, v in group.items() if v is not None})
                continue

            # Service Carving   : Auto-selection
            m = p24.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({k: v for k, v in group.items() if v is not None})
                continue

            # Peering Details   : 10.36.3.36[MOD:P:00] 10.36.3.37[MOD:P:00]
            m = p25.match(line)
            if m:
                group = m.groupdict()
                peering_details = group['peering_details']
                interface_dict.update({'peering_details': peering_details.split(' ')})
                continue

            # Forwarders     : 1
            m = p26.match(line)
            if m:
                group = m.groupdict()
                service_carving_results = interface_dict.setdefault('service_carving_results', {})
                service_carving_results.update({k: int(v) for k, v in group.items() if v is not None})
                continue

            # Permanent      : 0
            m = p27.match(line)
            if m:
                group = m.groupdict()
                service_carving_results = interface_dict.setdefault('service_carving_results', {})
                service_carving_results.update({k: int(v) for k, v in group.items() if v is not None})
                continue

            # Carving timer     : 0 sec [not running]
            m = p28.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({k: v for k, v in group.items() if v is not None})
                continue

            # Local SHG label   : 64005
            # Local SHG label   : None
            m = p29.match(line)
            if m:
                group = m.groupdict()
                local_shg_label = group['local_shg_label']
                interface_dict.update({'local_shg_label': local_shg_label})
                continue

            # Remote SHG labels : 1
            m = p30.match(line)
            if m:
                group = m.groupdict()
                remote_shg_label = group['remote_shg_label']
                label_dict = interface_dict.setdefault('remote_shg_labels', {}). \
                    setdefault(remote_shg_label, {})
                continue

            # 64005 : nexthop 10.36.3.37
            m = p31.match(line)
            if m:
                group = m.groupdict()
                shg_label = group['shg_label']
                next_hop = group['next_hop']
                label_dict.setdefault('label', {}). \
                    setdefault(shg_label, {}). \
                    update({'nexthop': next_hop})
                continue

            # Object: EVPN MAC
            m = p32.match(line)
            if m:
                group = m.groupdict()
                object_name = group['object_name']
                object_dict = interface_dict.setdefault('object', {}). \
                    setdefault(object_name, {})
                continue

            # Base info: version=0xdbdb0008, flags=0x4000, type=8, reserved=0
            m = p33.match(line)
            if m:
                group = m.groupdict()
                version = group['version']
                flags = group['flags']
                base_info_type = int(group['type'])
                reserved = int(group['reserved'])
                base_info_dict = object_dict.setdefault('base_info', {})
                base_info_dict.update({'version': version})
                base_info_dict.update({'flags': flags})
                base_info_dict.update({'type': base_info_type})
                base_info_dict.update({'reserved': reserved})
                continue

            # EVPN ES event history  [Num events: 0]
            m = p34.match(line)
            if m:
                group = m.groupdict()
                object_dict.update({k: int(v) for k, v in group.items() if v is not None})
                continue

            # Jun 14 14:02:12.864 Create                        00000000, 00000000 -  -
            # Jun 14 14:02:12.864 MAC advertise rejected        00000003, 00000000 -  -
            # Aug 15 22:10:12.992 API Provision                 00000000 00000000 -  -
            # Aug 15 22:10:12.992 API BP Ifname delete          45138200 0aa6ab70 M  -
            m = p35.match(line)
            if m:
                group = m.groupdict()
                index = event_history_index.get('event_history', 0) + 1
                event_history_dict = object_dict.setdefault('event_history', {}). \
                    setdefault(index, {})
                event_history_dict.update({k: v.strip() for k, v in group.items() if v is not None})
                event_history_index.update({'event_history': index})
                continue

            # RT|   1 27/08 09:49:15.582 00000000|   0                    00000000
            # LocalBMAC|   0                    00000000|   0                    00000000
            # ESI|   0                    00000000|   0                    00000000
            m = p37.match(line)
            if m:
                group = m.groupdict()
                label = (group.get('label').strip().lower().replace(' ', '_').replace('-', '_').replace('/', '_'))
                adv_cnt = group.get('adv_cnt', None)
                adv_last_time = group.get('adv_last_time', None)
                adv_last_arg = group.get('adv_last_arg', None)
                wdw_cnt = group.get('wdw_cnt', None)
                wdw_last_time = group.get('wdw_last_time', None)
                wdw_last_arg = group.get('wdw_last_arg', None)

                es_statistics_dict = object_dict.setdefault('statistics', {}). \
                    setdefault(label, {})

                es_statistics_dict.update({'adv_cnt': int(adv_cnt)})
                if adv_last_time:
                    es_statistics_dict.update({'adv_last_time': adv_last_time})
                if adv_last_arg:
                    es_statistics_dict.update({'adv_last_arg': adv_last_arg})

                if wdw_cnt:
                    es_statistics_dict.update({'wdw_cnt': int(wdw_cnt)})
                if wdw_last_time:
                    es_statistics_dict.update({'wdw_last_time': wdw_last_time})
                if wdw_last_arg:
                    es_statistics_dict.update({'wdw_last_arg': wdw_last_arg})
                continue

            # Num RDs:       : 1
            m = p38.match(line)
            if m:
                group = m.groupdict()
                ead_update_dict = interface_dict.setdefault('es_ead_update', {})
                ead_update_dict.update({'num_rds': int(group['num_rds'])})
                continue

            # RD: 10.154.219.84:1, Num RTs: 1      RT List:
            m = p41.match(line)
            if m:
                group = m.groupdict()
                rd = group['rd']
                num_rts = int(group['num_rts'])
                rt_list = group.get('rt_list', None)
                rd_dict = ead_update_dict.setdefault('rd', {}).setdefault(rd, {})
                rd_dict.update({'num_rts': num_rts})
                if rt_list:
                    rd_dict.update({'rt_list': rt_list})
                continue

            # 4:1000,
            # 00:1, 100:2, 100:3, 100:4, 100:5,
            # 100:6, 100:13, 100:14, 100:15, 100:16,
            # 100:17, 100:18,
            m = p42.match(line)
            if m:
                group = m.groupdict()
                rt_list = rd_dict.get('rt_list', [])
                for rt in group['rt_list'].split(','):
                    rt = rt.strip()
                    if rt:
                        rt_list.append(rt)
                rd_dict.update({'rt_list': rt_list})
                continue

            # Chkpt ObjId    : 0x40002f18
            m = p43.match(line)
            if m:
                group = m.groupdict()
                chkpt_objid = group['chkpt_objid']
                interface_dict.update({'chkpt_objid': chkpt_objid})
                continue

            # MSTi Mask      : 0x7fff
            m = p44.match(line)
            if m:
                group = m.groupdict()
                msti_mask = group['msti_mask']
                checkpoint_info_dict = interface_dict.setdefault('checkpoint_info', {})
                checkpoint_info_dict.update({'msti_mask': msti_mask})
                continue

            # 192.168.0.1 [MOD:P:00][1]
            m = p45.match(line)
            if m:
                group = m.groupdict()
                # nexthop = group['nexthop']
                # nexthopinfo = group['nexthopinfo']
                if detail_type == 'peering_details':
                    details_list = interface_dict.get('peering_details', [])
                    details_list.append(line)
                    interface_dict.setdefault('peering_details', details_list)
                else:
                    checkpoint_info_dict = interface_dict.setdefault('checkpoint_info', {})
                    details_list = checkpoint_info_dict.get('nexthop', [])
                    details_list.append(line)
                    checkpoint_info_dict.update({'nexthop': details_list})
                continue

            # IF Type      : 1
            m = p46.match(line)
            if m:
                group = m.groupdict()
                if_type = int(group['if_type'])
                checkpoint_info_dict = interface_dict.setdefault('checkpoint_info', {})
                checkpoint_info_dict.update({'if_type': if_type})
                continue

            # Peering Details   :
            m = p47.match(line)
            if m:
                detail_type = 'peering_details'
                continue

            # Primary        : 0
            m = p49.match(line)
            if m:
                group = m.groupdict()
                primary = group['primary']
                evpn_vpws_service_carving_results_dict = interface_dict.setdefault('evpn_vpws_service_carving_results',{})  # noqa
                evpn_vpws_service_carving_results_dict.update({'primary': primary})
                continue

            # Backup         : 0
            m = p50.match(line)
            if m:
                group = m.groupdict()
                backup = group['backup']
                evpn_vpws_service_carving_results_dict = interface_dict.setdefault('evpn_vpws_service_carving_results',{})  # noqa
                evpn_vpws_service_carving_results_dict.update({'backup': backup})
                continue

            # Non-DF         : 18
            m = p51.match(line)
            if m:
                group = m.groupdict()
                non_df = group['non_df']
                evpn_vpws_service_carving_results_dict = interface_dict.setdefault('evpn_vpws_service_carving_results',{})  # noqa
                evpn_vpws_service_carving_results_dict.update({'non_df': non_df})
                continue

            # Checkpoint Info:
            m = p52.match(line)
            if m:
                detail_type = 'checkpoint_info'
                continue

            # EVPN-VPWS Service Carving Results:
            m = p48.match(line)
            if m:
                evpn_vpws_service_carving_results_dict = interface_dict.setdefault('evpn_vpws_service_carving_results',{})  # noqa
                continue

            # 0210.03ff.9e00.0210.0000 Gi0/3/0/0      10.1.100.100
            m = p1.match(line)
            if m:
                group = m.groupdict()
                segment_id = group['segment_id']
                interface = Common.convert_intf_name(group['interface'])
                next_hop = group['next_hop']
                interface_dict = ret_dict.setdefault('segment_id', {}). \
                    setdefault(segment_id, {}). \
                    setdefault('interface', {}). \
                    setdefault(interface, {})
                next_hop_list = interface_dict.setdefault('next_hops', [next_hop])
                continue

            # 10.204.100.100
            m = p1_1.match(line)
            if m:
                group = m.groupdict()
                next_hop = group['next_hop']
                next_hop_list.append(next_hop)
                continue

            # Diagnostic ESI : N/A                     Interface Name : N/A
            # Diagnostic Flag: 0x00000043              DiagnosticES-RT: 0000.0000.0000
            # Port Key       : 0x000088d4              MAC winner     : 1
            m = p39.match(line)
            if m:
                group = m.groupdict()
                label_1 = group['label_1'].strip().lower().replace(' ', '_').replace('-', '').replace('/', '_')
                label_1 = key_dict.get(label_1, label_1)
                val_1 = group['val_1'].strip()

                label_2 = group['label_2'].strip().lower().replace(' ', '_').replace('-', '')
                label_2 = key_dict.get(label_2, label_2)
                val_2 = group['val_2'].strip()
                interface_dict.update({label_1: val_1})
                interface_dict.update({label_2: val_2})

                per_es_1 = group['per_es_1']
                if per_es_1:
                    interface_dict.update({'{}_per_es'.format(label_1): per_es_1})
                per_es_2 = group['per_es_2']
                if per_es_2:
                    interface_dict.update({'{}_per_es'.format(label_2): per_es_2})
                continue

            # Carving Timer  : 0    (global)
            # Number of EVIs : 1
            m = p40.match(line)
            if m:
                group = m.groupdict()
                label_1 = group['label_1'].strip().lower().replace(' ', '_').replace('-', '').replace('/', '_')
                label_1 = key_dict.get(label_1, label_1)
                val_1 = group['val_1'].strip()
                per_es_1 = group['per_es_1']
                if per_es_1:
                    interface_dict.update({'{}_per_es'.format(label_1): per_es_1})
                interface_dict.update({label_1: val_1})
                continue
        return ret_dict


class ShowEvpnEthernetSegmentDetail(ShowEvpnEthernetSegment):
    """Parser class for 'show evpn ethernet-segment detail' CLI."""

    cli_command = 'show evpn ethernet-segment detail'

    def cli(self, output=None):
        """parsing mechanism: cli
        """

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        return super().cli(output=out)


class ShowEvpnEthernetSegmentPrivate(ShowEvpnEthernetSegment):
    """Parser class for 'show evpn ethernet-segment private' CLI."""

    cli_command = 'show evpn ethernet-segment private'

    def cli(self, output=None):
        """parsing mechanism: cli
        """

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        return super().cli(output=out)


class ShowEvpnEthernetSegmentEsiDetail(ShowEvpnEthernetSegment):
    """Parser class for 'show evpn ethernet-segment esi {esi} detail' CLI."""

    cli_command = 'show evpn ethernet-segment esi {esi} detail'

    def cli(self, esi, output=None):
        """parsing mechanism: cli
        """

        if output is None:
            out = self.device.execute(self.cli_command.format(
                    esi=esi))
        else:
            out = output
        return super().cli(output=out)


# =====================================================
# Schema for:
#   * 'show evpn internal-label'
# =====================================================
class ShowEvpnInternalLabelSchema(MetaParser):
    schema = {
        'evi': {
            Any(): {
                'ethernet_segment_id': {
                    Any(): {
                        'index': {
                            Any(): {
                                'ether_tag': str,
                                'label': str,
                                Optional('encap'): str,
                                Optional('summary_pathlist'): {
                                    'index': {
                                        Any(): {
                                            'tep_id': str,
                                            'df_role': str,
                                            'nexthop': str,
                                            'label': str
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
            }
        }
    }


# =====================================================
# Parser for:
#   * 'show evpn internal-label'
# =====================================================
class ShowEvpnInternalLabel(ShowEvpnInternalLabelSchema):

    cli_command = 'show evpn internal-label'

    def cli(self, output=None):

        ret_dict = {}
        index_dict = {}
        summary_pathlist_index = 0
        out = output if output else self.device.execute(self.cli_command)

        # 1000 0000.01ff.0506.0506.07aa 0 None
        # 1000 0000.01ff.0506.0506.07aa 200 24011
        p1 = re.compile(r'^(?P<evi>\d+)( +(?P<encap>\S+))? +'
                        r'(?P<ethernet_segment_id>[\w\.]+) +(?P<ether_tag>\S+) +(?P<label>\S+)$')

        # 0xffffffff (P) 192.168.0.3                              29213
        p2 = re.compile(r'^(?P<tep_id>\S+) +(?P<df_role>\(\w\)) +'
                        r'(?P<nexthop>\S+) +(?P<label>\S+)$')

        for line in out.splitlines():
            line = line.strip()

            # 1000 0000.01ff.0506.0506.07aa 0 None
            # 1000 0000.01ff.0506.0506.07aa 200 24011
            # 100        MPLS   0036.37ff.0000.0000.1100    0          64006
            m = p1.match(line)
            if m:
                group = m.groupdict()
                evi = int(group['evi'])
                ethernet_segment_id = group['ethernet_segment_id']
                ether_tag = group['ether_tag']
                label = group['label']

                index = index_dict.get(ethernet_segment_id, 0) + 1

                evi_dict = ret_dict.setdefault('evi', {}). \
                    setdefault(evi, {})

                segment_id_dict = evi_dict. \
                    setdefault('ethernet_segment_id', {}). \
                    setdefault(ethernet_segment_id, {}). \
                    setdefault('index', {}). \
                    setdefault(index, {})

                segment_id_dict.update({'ether_tag': ether_tag})
                segment_id_dict.update({'label': label})

                if group['encap']:
                    segment_id_dict.update({'encap': group['encap']})

                index_dict.update({ethernet_segment_id: index})
                continue

            # 0xffffffff (P) 192.168.0.3                              29213
            m = p2.match(line)
            if m:
                group = m.groupdict()
                tep_id = group['tep_id']
                df_role = group['df_role']
                nexthop = group['nexthop']
                label = group['label']
                summary_pathlist_index += 1
                summary_pathlist_dict = segment_id_dict.setdefault('summary_pathlist', {}). \
                    setdefault('index', {}). \
                    setdefault(summary_pathlist_index, {})

                summary_pathlist_dict.update({'tep_id': tep_id})
                summary_pathlist_dict.update({'df_role': df_role})
                summary_pathlist_dict.update({'nexthop': nexthop})
                summary_pathlist_dict.update({'label': label})
                continue

        return ret_dict
