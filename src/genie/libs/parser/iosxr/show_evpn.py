""" show_evpn.py

show evpn parser class

"""

from ipaddress import ip_address
import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional

from genie.libs.parser.base import *

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
        # RD Auto  : (auto) 1.100.100.100:145
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
                sub_dict = ret_dict.setdefault('evi', {}). \
                    setdefault(evi, {})
                sub_dict.update({'bridge_domain': bridge_domain})
                sub_dict.update({'type': evi_type})
                continue
            
            # 100:145                        Import 
            # 100:145                        Export 
            m = p2.match(line)
            if m:
                group = m.groupdict()
                route_target_in_use = group['route_target_in_use']
                route_type = group['type']
                type_dict = sub_dict.setdefault('route_target_in_use', {}). \
                    setdefault(route_target_in_use, {})
                type_dict.update({route_type.lower(): True})
                continue
            
            # ------------------------------ -------
            m = p3.match(line)
            if m:
                continue

            # Unicast Label  : 24001
            # Multicast Label: 16001
            # RD Auto  : (auto) 1.100.100.100:145
            m = p4.match(line)
            if m:
                group = m.groupdict()
                key = group['key'].strip().lower().replace(' ', '_')
                value = group['value'].strip()
                sub_dict.update({key: value})
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
        return super().cli(output=output)

class ShowEvpnEviMac(MetaParser):
    """Parser class for 'show evpn evi mac' CLI."""
    exclude = ['entries']

    # TODO schema

    def __init__(self, mac=None, vpn_id=None, private=False, **kwargs):
        self.mac = mac
        self.private = private
        self.vpn_id = vpn_id
        super().__init__(**kwargs)

    cli_command = ['show evpn evi vpn-id {vpn_id} mac','show evpn evi mac']
    def cli(self):

        if self.vpn_id is not None:
            cmd = self.cli_command[0].format(vpn_id=self.vpn_id)
        else:
            cmd = self.cli_command[1]

        if self.mac:
            cmd += ' {mac}'.format(self.mac)
        if self.private:
            cmd += ' private'.format()

        out = self.device.execute(cmd)

        result = {
            'entries': [],
        }

        entry = None
        for line in out.splitlines():
            line = line.rstrip()

            # EVI        MAC address    IP address                               Nexthop                                 Label
            # ---------- -------------- ---------------------------------------- --------------------------------------- --------

            # 65535      02e5.7847.6000 ::                                       Local                                   0
            # 1          0000.0000.0001 ::                                       No remote pathlist
            m = re.match(r'^(?P<evi>[0-9]+)'
                         r' +(?P<mac>' + re_mac + ')'
                         r' +(?P<ip>' + re_ip + ')'
                         r'(?: +No remote pathlist|'
                         r' +(?P<next_hop>\S+)'
                         r' +(?:(?P<label_int>\d+)|(?P<label_str>' + re_label_str + '))'
                         r')'
                         r'$', line)
            if m:
                entry = {
                    'evi': int(m.group('evi')),
                    'mac': m.group('mac'),
                    'ip': ip_address(m.group('ip')),
                    'next_hop': m.group('next_hop'),
                    'label': m.group('label_str') \
                    or (m.group('label_int') and int(m.group('label_int'))),
                }
                try:
                    entry['next_hop'] = ip_address(entry['next_hop'])
                except (TypeError, ValueError):
                    pass
                result['entries'].append(entry)
                continue

            # OLD

            # MAC address    Nexthop                                 Label    vpn-id
            # -------------- --------------------------------------- -------- --------

            # 7777.7777.0002 N/A                                     24005    7
            m = re.match(r'^(?P<mac>' + re_mac + ')'
                         r' +(?:N/A|(?P<ip>' + re_ip + ')|(?P<next_hop>\S+))'
                         r' +(?:(?P<label_int>\d+)|(?P<label_str>' + re_label_str + '))'
                         r' +(?P<evi>[0-9]+)'
                         r'$', line)
            if m:
                entry = {
                    'mac': m.group('mac'),
                    'ip': m.group('ip') and ip_address(m.group('ip')),
                    'next_hop': m.group('next_hop'),
                    'label': m.group('label_str') or int(m.group('label_int')),
                    'evi': int(m.group('evi')),
                }
                try:
                    entry['label'] = int(entry['label'])
                except ValueError:
                    pass
                result['entries'].append(entry)
                continue

            if entry and self.private:
                #EVI        MAC address    IP address                               Nexthop                                 Label
                #---------- -------------- ---------------------------------------- --------------------------------------- --------
                #1          fc00.0001.0002 ::                                       Bundle-Ether1.0                         28100
                #   Ethernet Tag                            : 0
                #   Multi-paths Resolved                    : False
                #   Static                                  : No
                #   Local Ethernet Segment                  : 0001.2222.2222.2200.000a
                #   Remote Ethernet Segment                 : 0000.0000.0000.0000.0000
                #   Local Sequence Number                   : 0
                #   Remote Sequence Number                  : 0
                #   Encapsulation                           : N/A
                #   ESI Port Key                            : 1
                #   Source                                  : Local
                #   Multi-paths Local Label                 : 0
                #   SOO Nexthop                             : ::
                #   BP IFH                                  : 0x152
                #   MAC State                               : Local
                #
                #   Object: EVPN MAC
                #   Base info: version=0xdbdb0008, flags=0x4100, type=8, reserved=0
                #   EVPN MAC event history  [Num events: 3]
                #   ----------------------------------------------------------------------------
                #     Time                Event                         Flags      Flags
                #     ====                =====                         =====      =====
                #     Dec  7 01:46:49.088 Create                        00000000, 00000000 -  -
                #     Dec  7 01:46:49.088 Advertise to BGP              00204110, 00000000 -  -
                #     Dec  7 01:46:49.088 Ignore BGP update             00000000, 00000000 -  -
                #   ----------------------------------------------------------------------------
                #65535      02a0.0964.e800 ::                                       Local                                   0
                #   Ethernet Tag                            : 0
                #   Multi-paths Resolved                    : False
                #   Static                                  : No
                #   Local Ethernet Segment                  : 0000.0000.0000.0000.0000
                #   Remote Ethernet Segment                 : 0000.0000.0000.0000.0000
                #   Local Sequence Number                   : 0
                #   Remote Sequence Number                  : 0
                #   Encapsulation                           : N/A
                #   ESI Port Key                            : 0
                #   Source                                  : Local
                #   Multi-paths Local Label                 : 0
                #   SOO Nexthop                             : ::
                #   BP IFH                                  : 0x0
                #   MAC State                               : Local
                #
                #   Object: EVPN MAC
                #   Base info: version=0xdbdb0008, flags=0xc100, type=8, reserved=0
                #   EVPN MAC event history  [Num events: 13]
                #   ----------------------------------------------------------------------------
                #     Time                Event                         Flags      Flags
                #     ====                =====                         =====      =====
                #     Dec  7 01:41:11.168 Create                        00000000, 00000000 -  -
                #     Dec  7 01:41:11.168 MAC advertise rejected        00000000, 00000000 -  -
                #     Dec  7 01:41:11.168 Withdraw from BGP;filtered    0000c000, 00000000 -  -
                #     Dec  7 01:41:11.168 Modify Redundant              00000000, 00000000 -  -
                #     Dec  7 01:45:25.632 Replay EVI to BGP             00000000, 00000000 -  -
                #     Dec  7 01:45:25.632 MAC advertise rejected        00000000, 00000000 -  -
                #     Dec  7 01:45:25.632 Withdraw from BGP;filtered    0000c100, 00000000 -  -
                #     Dec  7 01:45:25.632 Replay EVI to BGP             00000000, 00000000 -  -
                #     Dec  7 01:45:25.632 MAC advertise rejected        00000000, 00000000 -  -
                #     Dec  7 01:45:25.632 Withdraw from BGP             0040c110, 00000000 -  -
                #     Dec  7 01:46:04.032 Replay EVI to BGP             00000000, 00000000 -  -
                #     Dec  7 01:46:04.032 MAC advertise rejected        00000000, 00000000 -  -
                #     Dec  7 01:46:04.032 Withdraw from BGP             0040c110, 00000000 -  -
                #   ----------------------------------------------------------------------------

                m = re.match(r'^ +Ethernet Tag *: +(?P<eth_tag>[0-9]+)$|'
                             r'^ +Multi-paths Resolved *: +(?P<multipath_resolved>(True|False))$|'
                             r'^ +Static *: +(?P<is_static>(Yes|No))$|'
                             r'^ +Local Ethernet Segment *: +(?P<local_esi>[A-Za-z0-9]{4}\.[A-Za-z0-9]{4}\.[A-Za-z0-9]{4}\.[A-Za-z0-9]{4}\.[A-Za-z0-9]{4})$|'
                             r'^ +Remote Ethernet Segment *: +(?P<remote_esi>[A-Za-z0-9]{4}\.[A-Za-z0-9]{4}\.[A-Za-z0-9]{4}\.[A-Za-z0-9]{4}\.[A-Za-z0-9]{4})$|'
                             r'^ +Local Sequence Number *: +(?P<local_seq_no>[0-9]+)$|'
                             r'^ +Remote Sequence Number *: +(?P<remote_seq_no>[0-9]+)$|'
                             r'^ +Encapsulation *: +(?P<encapsulation>\S+)$|'
                             r'^ +Local Encapsulation *: +(?P<encapsulation_local>\S+)$|'
                             r'^ +Remote Encapsulation *: +(?P<encapsulation_remote>\S+)$|'
                             r'^ +ESI Port Key *: +(?P<esi_port_key>[0-9]+)$|'
                             r'^ +Source *: +(?P<source>\S+)$|'
                             r'^ +Multi-paths Local Label *: +(?P<multipath_label>[0-9]+)$|'
                             r'^ +SOO Nexthop *: +(?P<remote_soo>\S+)$|'
                             r'^ +BP XCID *: +(?P<bp_xcid>0x[A-fa-f0-9]+)$|'
                             r'^ +BP IFH *: +(?P<bp_ifh>0x[A-fa-f0-9]+)$|'
                             r'^ +MAC State *: +(?P<mac_state>\S+)$', line)

                if m:
                    if m.lastgroup != None:
                        if m.lastgroup == 'eth_tag':
                            entry[m.lastgroup] = int(m.group(m.lastgroup))
                        elif m.lastgroup == 'multipath_resolved':
                            if m.group(m.lastgroup) == 'True':
                                entry[m.lastgroup] = True
                            elif m.group(m.lastgroup) == 'False':
                                entry[m.lastgroup] = False
                        elif m.lastgroup == 'is_static':
                            if m.group(m.lastgroup) == 'Yes':
                                entry['is_static'] = True
                            elif m.group(m.lastgroup) == 'No':
                                entry['is_static'] = False
                        elif m.lastgroup == 'local_seq_no':
                            entry[m.lastgroup] = int(m.group(m.lastgroup))
                        elif m.lastgroup == 'remote_seq_no':
                            entry[m.lastgroup] = int(m.group(m.lastgroup))
                        elif m.lastgroup == 'esi_port_key':
                            entry[m.lastgroup] = int(m.group(m.lastgroup))
                        elif m.lastgroup == 'source':
                            if m.group(m.lastgroup) == 'Local':
                                entry['is_local'] = True
                                entry['is_remote'] = False
                            elif m.group(m.lastgroup) == 'Remote':
                                entry['is_remote'] = True
                                entry['is_local'] = False
                        elif m.lastgroup == 'multipath_label':
                            entry[m.lastgroup] = int(m.group(m.lastgroup))
                        elif m.lastgroup == 'remote_soo':
                            try:
                                entry[m.lastgroup] = ip_address(m.group(m.lastgroup))
                            except (TypeError, ValueError):
                                pass
                        else:
                            entry[m.lastgroup] = m.group(m.lastgroup)
                    continue

        # Search through the result entries and populate the duplicate macs
        # with our private data
        if self.private:
            for entry in result['entries']:
                if 'eth_tag' not in entry:
                    evi_entry = entry['evi']
                    mac_entry = entry['mac']
                    for copy_entry in result['entries']:
                        if 'eth_tag' in copy_entry and copy_entry['evi'] == evi_entry \
                                                   and copy_entry['mac'] == mac_entry:
                            # Need to copy entry['next'hop'] to set the correct
                            # value again after the update
                            next_hop_copy = entry['next_hop']
                            entry.update(copy_entry)
                            entry['next_hop'] = next_hop_copy
                            continue

        return result


class ShowEvpnEthernetSegment(MetaParser):
    """Parser class for 'show evpn ethernet-segment' CLI."""

    # TODO schema

    def __init__(self, detail=False, private=False, carving=False, esi=None, **kwargs):
        self.esi = esi
        self.detail = detail
        self.private = private
        self.carving = carving
        super().__init__(**kwargs)

    cli_command = ['show evpn ethernet-segment esi {esi}','show evpn ethernet-segment']
    def cli(self):
        """parsing mechanism: cli
        """

        if self.esi:
            cmd = self.cli_command[0].format(esi=self.esi)
        else:
            cmd = self.cli_command[1]

        if self.carving:
            cmd += ' carving'

        if self.private:
            cmd += ' private'
        elif self.detail:
            cmd += ' detail'

        tcl_package_require_caas_parsers()
        kl = tcl_invoke_caas_abstract_parser(
            device=self.device, exec=cmd)

        return kl


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
        Optional('evi'):
            {Any():
                {'evi': int,
                'esi': str,
                'eth_tag': int,
                'internal_label': int,
                Optional('mp_resolved'): bool,
                Optional('mp_single_active'): str,
                Optional('pathlists'):
                    {Optional('mac'):
                        {'nexthop':
                            {Any():
                                {'label': int,
                                Optional('flag'): str,
                                },
                            },
                        },
                     Optional('es_ead'):
                        {'nexthop':
                            {Any():
                                {'label': int,
                                Optional('flag'): str,
                                },
                            },
                        },
                     Optional('evi_ead'):
                        {'nexthop':
                            {Any():
                                {'label': int,
                                Optional('flag'): str,
                                },
                            },
                        },
                     Optional('summary'):
                        {'nexthop':
                            {Any():
                                {'label': int,
                                Optional('flag'): str,
                                },
                            },
                        },
                    },
                },
            },
        Optional('vpn_id'):
            {Any():
                {'vpn_id': int,
                'esi': str,
                'eth_tag': int,
                'internal_label': int,
                Optional('mp_resolved'): bool,
                Optional('mp_single_active'): str,
                Optional('pathlists'):
                    {Optional('mac'):
                        {'nexthop':
                            {Any():
                                {'label': int,
                                Optional('flag'): str,
                                },
                            },
                        },
                     Optional('es_ead'):
                        {'nexthop':
                            {Any():
                                {'label': int,
                                Optional('flag'): str,
                                },
                            },
                        },
                     Optional('evi_ead'):
                        {'nexthop':
                            {Any():
                                {'label': int,
                                Optional('flag'): str,
                                },
                            },
                        },
                     Optional('summary'):
                        {'nexthop':
                            {Any():
                                {'label': int,
                                Optional('flag'): str,
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
        * 'show evpn internal-label detail location {location}'
    '''

    cli_command = ['show evpn internal-label detail',
                   'show evpn internal-label detail location {location}']

    def cli(self, location=None, output=None):

        if output is None:
            if location:
                out = self.device.execute(self.cli_command[1].\
                                                format(location=location))
            else:
                out = self.device.execute(self.cli_command[0])
        else:
            out = output

        # Init
        parsed_dict = {}
        type_dict = {
            'MAC': 'mac',
            'EAD/ES': 'es_ead',
            'EAD/EVI': 'evi_ead',
            'Summary': 'summary',
            }

        # EVI   Ethernet Segment Id                     EtherTag Label  
        # VPN-ID     Encap  Ethernet Segment Id         EtherTag   Label

        # 5     0012.1200.0000.0000.0002                0        24114
        # 100   0100.0000.acce.5500.0100                0        24005
        p1 = re.compile(r'^(?P<evi>(\d+)) +(?P<esi>([a-z0-9\.]+))'
                         ' +(?P<eth_tag>(\d+)) +(?P<internal_label>(\d+))$')

        # 16001      VXLAN  0001.0407.0405.0607.0811    0          24002
        # 16003      VXLAN  0001.0407.0405.0607.0811    0          24004
        p2 = re.compile(r'^(?P<vpn_id>(\d+)) +(?P<encap>([a-zA-Z]+))'
                         ' +(?P<esi>([a-z0-9\.]+)) +(?P<eth_tag>(\d+))'
                         ' +(?P<internal_label>(\d+))$')

        # Multi-paths resolved: TRUE
        # Multi-paths resolved: TRUE (Remote single-active)
        p3 = re.compile(r'^Multi-paths +resolved: +(?P<mp_resolved>(\S+))'
                         ' +\((?P<mp_single_active>(.*))\)$')

        # Pathlists:
        # MAC     10.70.20.20                              24212
        # EAD/ES  10.10.10.10                              0
        # EAD/EVI 10.10.10.10                              24012
        # Summary 10.70.20.20                              24212
        p4 = re.compile(r'^(?P<type>(MAC|EAD\/ES|EAD\/EVI|Summary)) +(?P<nexthop>(\S+)) +(?P<label>(\d+))$')

        #         10.70.20.20                              0
        #         10.10.10.10 (B)                          24012
        p5 = re.compile(r'^(?P<nexthop>(\S+))(?: +\((?P<flag>(\S+))\))? +(?P<label>(\d+))$')

        # Summary pathlist:
        #   0x03000001 123.1.1.2                                16002

        for line in out.splitlines():
            line = line.strip()

            # 5     0012.1200.0000.0000.0002                0        24114
            m = p1.match(line)
            if m:
                group = m.groupdict()
                sub_dict = parsed_dict.setdefault('evi', {}).\
                                       setdefault(int(group['evi']), {})
                for key, value in group.items():
                    if re.match('[a-z]+', value):
                        sub_dict[key] = value
                    else:
                        sub_dict[key] = int(value)
                continue

            # 16001      VXLAN  0001.0407.0405.0607.0811    0          24002
            # 16003      VXLAN  0001.0407.0405.0607.0811    0          24004
            m = p2.match(line)
            if m:
                group = m.groupdict()
                sub_dict = parsed_dict.setdefault('vpn_id', {}).\
                                       setdefault(int(group['vpn_id']), {})
                for key, value in group.items():
                    if re.match('[a-z]+', value):
                        sub_dict[key] = value
                    else:
                        sub_dict[key] = int(value)
                continue

            # Multi-paths resolved: TRUE
            # Multi-paths resolved: TRUE (Remote single-active)
            m = p3.match(line)
            if m:
                sub_dict['mp_resolved'] = True
                if m.groupdict()['mp_single_active']:
                    sub_dict['mp_single_active'] = m.groupdict()['mp_single_active']
                continue

            # MAC     10.70.20.20                              24212
            # EAD/ES  10.10.10.10                              0
            # EAD/EVI 10.10.10.10                              24012
            # Summary 10.70.20.20                              24212
            m = p4.match(line)
            if m:
                group = m.groupdict()
                pathlists_dict = sub_dict.setdefault('pathlists', {}).\
                                        setdefault(type_dict[group['type']], {})
                type_nh_dict = pathlists_dict.setdefault('nexthop', {}).\
                                              setdefault(group['nexthop'], {})
                type_nh_dict['label'] = int(group['label'])
                continue

            #         10.70.20.20                              0
            #         10.10.10.10 (B)                          24012
            m = p5.match(line)
            if m:
                group = m.groupdict()
                type_nh_dict = pathlists_dict.setdefault('nexthop', {}).\
                                              setdefault(group['nexthop'], {})
                type_nh_dict['label'] = int(group['label'])
                if group['flag']:
                    type_nh_dict['flag'] = group['flag']
                continue

        return parsed_dict


# vim: ft=python ts=8 sw=4 et

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
                        Optional('local_static'): str,
                        Optional('remote_static'): str,
                        Optional('local_ethernet_segment'): str,
                        Optional('ethernet_segment'): str,
                        Optional('remote_ethernet_segment'): str,
                        Optional('local_sequence_number'): int,
                        Optional('remote_sequence_number'): int,
                        Optional('local_encapsulation'): str,
                        Optional('remote_encapsulation'): str,
                        Optional('esi_port_key'): int,
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

        # 65535      N/A    0000.0000.0000 ::                                       Local                                   0
        p1 = re.compile(r'^(?P<vpn_id>\d+) +(?P<encap>\S+) +(?P<mac_address>[\w\.]+) +'
                '(?P<ip_address>[\w:\.]+) +(?P<next_hop>[\S ]+) +(?P<label>\d+)$')
        
        # 001b.0100.0001 N/A                                     24014    7  
        p1_1 = re.compile(r'^(?P<mac_address>\S+) +(?P<next_hop>\S+) +(?P<label>\d+) +(?P<vpn_id>\d+)$')

        # IP Address   : 7.7.7.8
        p1_2 = re.compile(r'^IP +Address +: +(?P<ip_address>\S+)$')

        # Ethernet Tag                            : 0
        p2 = re.compile(r'^Ethernet +Tag +: +(?P<ethernet_tag>\d+)$')

        # Multi-paths Resolved                    : False
        p3 = re.compile(r'^Multi-paths +Resolved +: +(?P<multipaths_resolved>\S+)$')

        # Multi-paths Internal label              : 0
        p4 = re.compile(r'^Multi-paths +Internal +label +: +(?P<multipaths_internal_label>\d+)$')

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
        p13 = re.compile(r'^ESI +Port +Key +: +(?P<esi_port_key>\d+)$')

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
        p19 = re.compile(r'^MAC +State +: +(?P<mac_state>\S+)$')

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
                ', +type=(?P<type>\d+), +reserved=(?P<reserved>\d+)$')
        
        # EVPN MAC event history  [Num events: 0]
        p25 = re.compile(r'^EVPN +MAC +event +history +\[Num +events: +(?P<num_events>\d+)\]$')

        # Jun 14 14:02:12.864 Create                        00000000, 00000000 -  -
        # Jun 14 14:02:12.864 MAC advertise rejected        00000003, 00000000 -  -
        p26 = re.compile(r'^(?P<time>\w+ +\d+ +\S+) +(?P<event>[\S ]+) +(?P<flag_1>\d+)'
                ', +(?P<flag_2>\d+) +(?P<code_1>\S+) +(?P<code_2>\S+)$')

        # Flush Count  : 0
        p27 = re.compile(r'^Flush +Count *: +(?P<flush_count>\d+)$')

        # BP IFH: 0
        p28 = re.compile(r'^BP +IFH: +(?P<bp_ifh>\d+)$')

        # Flush Seq ID : 0
        p29 = re.compile(r'^Flush +Seq +ID +: +(?P<flush_seq_id>\d+)$')

        # Static: No
        p30 = re.compile(r'^Static: +(?P<static>\S+)$')

        for line in out.splitlines():
            line = line.strip()

            # 65535      N/A    0000.0000.0000 ::                                       Local                                   0
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
                vpn_id_dict.update({'encap': encap}) 
                vpn_id_dict.update({'ip_address': ip_address})
                vpn_id_dict.update({'next_hop': next_hop}) 
                vpn_id_dict.update({'label': label}) 
                continue
            
            # 001b.0100.0001 N/A                                     24014    7
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
            
            # IP Address   : 7.7.7.8
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
                vpn_id_dict.update({k:int(v) for k, v in group.items() if v is not None})
                continue
            
            # Multi-paths Resolved                    : False
            m = p3.match(line)
            if m:
                group = m.groupdict()
                vpn_id_dict.update({k:v for k, v in group.items() if v is not None})
                continue
            
            # Multi-paths Internal label              : 0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                vpn_id_dict.update({k:int(v) for k, v in group.items() if v is not None})
                continue
            
            # Local Static                            : No
            m = p5.match(line)
            if m:
                group = m.groupdict()
                vpn_id_dict.update({k:v for k, v in group.items() if v is not None})
                continue
            
            # Remote Static                           : No
            m = p6.match(line)
            if m:
                group = m.groupdict()
                vpn_id_dict.update({k:v for k, v in group.items() if v is not None})
                continue
            
            # Local Ethernet Segment                  : 0000.0000.0000.0000.0000
            m = p7.match(line)
            if m:
                group = m.groupdict()
                vpn_id_dict.update({k:v for k, v in group.items() if v is not None})
                continue

            # Ether.Segment: 0000.0000.0000.0000.0000
            m = p7_1.match(line)
            if m:
                group = m.groupdict()
                vpn_id_dict.update({k:v for k, v in group.items() if v is not None})
                continue
            
            # Remote Ethernet Segment                 : 0000.0000.0000.0000.0000
            m = p8.match(line)
            if m:
                group = m.groupdict()
                vpn_id_dict.update({k:v for k, v in group.items() if v is not None})
                continue
            
            # Local Sequence Number                   : 0
            m = p9.match(line)
            if m:
                group = m.groupdict()
                vpn_id_dict.update({k:int(v) for k, v in group.items() if v is not None})
                continue

            # Remote Sequence Number                  : 0
            m = p10.match(line)
            if m:
                group = m.groupdict()
                vpn_id_dict.update({k:int(v) for k, v in group.items() if v is not None})
                continue

            # Local Encapsulation                     : N/A
            m = p11.match(line)
            if m:
                group = m.groupdict()
                vpn_id_dict.update({k:v for k, v in group.items() if v is not None})
                continue

            # Remote Encapsulation                    : N/A
            m = p12.match(line)
            if m:
                group = m.groupdict()
                vpn_id_dict.update({k:v for k, v in group.items() if v is not None})
                continue

            # ESI Port Key                            : 0
            m = p13.match(line)
            if m:
                group = m.groupdict()
                vpn_id_dict.update({k:int(v) for k, v in group.items() if v is not None})
                continue

            # Source                                  : Local
            m = p14.match(line)
            if m:
                group = m.groupdict()
                vpn_id_dict.update({k:v for k, v in group.items() if v is not None})
                continue

            # Flush Requested                         : 0
            m = p15.match(line)
            if m:
                group = m.groupdict()
                vpn_id_dict.update({k:int(v) for k, v in group.items() if v is not None})
                continue

            # Flush Received                          : 0
            m = p16.match(line)
            if m:
                group = m.groupdict()
                vpn_id_dict.update({k:int(v) for k, v in group.items() if v is not None})
                continue

            # SOO Nexthop                             : ::
            m = p17.match(line)
            if m:
                group = m.groupdict()
                vpn_id_dict.update({k:v for k, v in group.items() if v is not None})
                continue

            # BP XCID                                 : 0xffffffff
            m = p18.match(line)
            if m:
                group = m.groupdict()
                vpn_id_dict.update({k:v for k, v in group.items() if v is not None})
                continue

            # MAC State                               : Init
            m = p19.match(line)
            if m:
                group = m.groupdict()
                vpn_id_dict.update({k:v for k, v in group.items() if v is not None})
                continue

            # MAC Producers                           : 0x0 (Best: 0x0)
            m = p20.match(line)
            if m:
                group = m.groupdict()
                vpn_id_dict.update({k:v for k, v in group.items() if v is not None})
                continue

            # Local Router MAC                        : 0000.0000.0000
            m = p21.match(line)
            if m:
                group = m.groupdict()
                vpn_id_dict.update({k:v for k, v in group.items() if v is not None})
                continue

            # L3 Label                                : 0
            m = p22.match(line)
            if m:
                group = m.groupdict()
                vpn_id_dict.update({k:int(v) for k, v in group.items() if v is not None})
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
                object_dict.update({k:int(v) for k, v in group.items() if v is not None})
                continue
            
            # Jun 14 14:02:12.864 Create                        00000000, 00000000 -  -
            # Jun 14 14:02:12.864 MAC advertise rejected        00000003, 00000000 -  -
            m = p26.match(line)
            if m:
                group = m.groupdict()
                index = event_history_index.get('event_history', 0) + 1
                event_history_dict = object_dict.setdefault('event_history', {}). \
                    setdefault(index, {})
                event_history_dict.update({k:v.strip() for k, v in group.items() if v is not None})
                event_history_index.update({'event_history': index})
                continue
            
            # Flush Count  : 0
            m = p27.match(line)
            if m:
                vpn_id_dict.update({k:v for k, v in group.items() if v is not None})
                continue
            
            # # BP IFH: 0
            m = p28.match(line)
            if m:
                vpn_id_dict.update({k:v for k, v in group.items() if v is not None})
                continue
            
            # Flush Seq ID : 0
            m = p29.match(line)
            if m:
                vpn_id_dict.update({k:v for k, v in group.items() if v is not None})
                continue
            
            # Static: No
            m = p30.match(line)
            if m:
                vpn_id_dict.update({k:v for k, v in group.items() if v is not None})
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
                            'type': int,
                            'value': str,
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
                                'label': {
                                    Any(): {
                                        'nexthop': str
                                    }
                                }
                            }
                        },
                        Optional('flush_again_timer'): str,
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
        num_of_label = {}

        # 0210.0300.9e00.0210.0000 Gi0/3/0/0      1.100.100.100
        p1 = re.compile(r'^(?P<segment_id>\S+) +(?P<interface>\S+) +(?P<next_hop>[\d\.]+)$')

        # 2.100.100.100   
        p1_1 = re.compile(r'^(?P<next_hop>[\d\.]+)$')

        # ES to BGP Gates   : Ready
        p2 = re.compile(r'^ES +to +BGP +Gates +: +(?P<es_to_bgp_gates>\S+)$')

        # ES to L2FIB Gates : Ready
        p3 = re.compile(r'^ES +to +L2FIB +Gates +: +(?P<es_to_l2fib_gates>\S+)$')

        # Interface name : GigabitEthernet0/3/0/0
        p4 = re.compile(r'^Interface name +: +(?P<interface>\S+)$')

        # Interface MAC  : 008a.9644.d8dd
        p4_1 = re.compile(r'^Interface +MAC *: +(?P<interface_mac>[\S ]+)$')

        # IfHandle       : 0x1800300
        p5 = re.compile(r'^IfHandle +: +(?P<if_handle>\S+)$')

        # State          : Up
        p6 = re.compile(r'^State + : +(?P<state>\S+)$')

        # Redundancy     : Not Defined
        p7 = re.compile(r'^Redundancy +: +(?P<redundancy>[\S ]+)$')

        # Source MAC        : 0001.ed9e.0001 (PBB BSA)
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
        p21 = re.compile(r'^ESI +type *: +(?P<esi_type>\d+)$')

        # Value          : 36.3700.0000.0000.1100
        p22 = re.compile(r'^Value *: +(?P<value>[\S ]+)$')

        # ES Import RT      : 3637.0000.0000 (from ESI)
        p23 = re.compile(r'^ES +Import +RT *: +(?P<es_import_rt>[\S ]+)$')

        # Service Carving   : Auto-selection
        p24 = re.compile(r'^Service +Carving *: +(?P<service_carving>[\S ]+)$')

        # Peering Details   : 3.3.3.36[MOD:P:00] 3.3.3.37[MOD:P:00]
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

        # 64005 : nexthop 3.3.3.37
        p31 = re.compile(r'^(?P<shg_label>\d+) *: +nexthop +(?P<next_hop>\S+)$')

        for line in out.splitlines():
            line = line.strip()
            
            # ES to L2FIB Gates : Ready
            m = p2.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({k:v for k, v in group.items() if v is not None})
                continue
            
            # ES to L2FIB Gates : Ready
            m = p3.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({k:v for k, v in group.items() if v is not None})
                continue
            
            # Interface name : GigabitEthernet0/3/0/0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                main_port_dict = interface_dict.setdefault('main_port', {})
                main_port_dict.update({k:v for k, v in group.items() if v is not None})
                continue

            # Interface MAC  : 008a.9644.d8dd
            m = p4_1.match(line)
            if m:
                group = m.groupdict()
                main_port_dict = interface_dict.setdefault('main_port', {})
                main_port_dict.update({k:v for k, v in group.items() if v is not None})
                continue
            
            # IfHandle       : 0x1800300
            m = p5.match(line)
            if m:
                group = m.groupdict()
                main_port_dict = interface_dict.setdefault('main_port', {})
                main_port_dict.update({k:v for k, v in group.items() if v is not None})
                continue
            
            # State          : Up
            m = p6.match(line)
            if m:
                group = m.groupdict()
                main_port_dict = interface_dict.setdefault('main_port', {})
                main_port_dict.update({k:v for k, v in group.items() if v is not None})
                continue

            # Redundancy     : Not Defined
            m = p7.match(line)
            if m:
                group = m.groupdict()
                main_port_dict = interface_dict.setdefault('main_port', {})
                main_port_dict.update({k:v for k, v in group.items() if v is not None})
                continue

            # Source MAC        : 0001.ed9e.0001 (PBB BSA)
            m = p8.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({k:v for k, v in group.items() if v is not None})
                continue
            
            # Operational    : MHN
            m = p9.match(line)
            if m:
                group = m.groupdict()
                topology_dict = interface_dict.setdefault('topology', {})
                topology_dict.update({k:v for k, v in group.items() if v is not None})
                continue
            
            # Configured     : A/A per service (default)
            m = p10.match(line)
            if m:
                group = m.groupdict()
                topology_dict = interface_dict.setdefault('topology', {})
                topology_dict.update({k:v for k, v in group.items() if v is not None})
                continue
            
            # Primary Services  : Auto-selection
            m = p11.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({k:v for k, v in group.items() if v is not None})
                continue
            
            # Secondary Services: Auto-selection
            m = p12.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({k:v for k, v in group.items() if v is not None})
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
                interface_dict.update({k:v for k, v in group.items() if v is not None})
                continue

            # Peering timer     : 45 sec [not running]
            m = p18.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({k:v for k, v in group.items() if v is not None})
                continue

            # Recovery timer    : 20 sec [not running]
            m = p19.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({k:v for k, v in group.items() if v is not None})
                continue

            # Flushagain timer  : 60 sec
            m = p20.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({k:v for k, v in group.items() if v is not None})
                continue

            # ESI type          : 0
            m = p21.match(line)
            if m:
                group = m.groupdict()
                esi_type = group['esi_type']
                esi_dict = interface_dict.setdefault('esi', {})
                esi_dict.update({'type': int(esi_type)})
                continue

            # Value          : 36.3700.0000.0000.1100
            m = p22.match(line)
            if m:
                group = m.groupdict()
                esi_value = group['value']
                esi_dict.update({'value': esi_value})
                continue

            # ES Import RT      : 3637.0000.0000 (from ESI)
            m = p23.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({k:v for k, v in group.items() if v is not None})
                continue

            # Service Carving   : Auto-selection
            m = p24.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({k:v for k, v in group.items() if v is not None})
                continue

            # Peering Details   : 3.3.3.36[MOD:P:00] 3.3.3.37[MOD:P:00]
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
                service_carving_results.update({k:int(v) for k, v in group.items() if v is not None})
                continue

            # Permanent      : 0
            m = p27.match(line)
            if m:
                group = m.groupdict()
                service_carving_results = interface_dict.setdefault('service_carving_results', {})
                service_carving_results.update({k:int(v) for k, v in group.items() if v is not None})
                continue

            # Carving timer     : 0 sec [not running]
            m = p28.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({k:v for k, v in group.items() if v is not None})
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

            # 64005 : nexthop 3.3.3.37
            m = p31.match(line)
            if m:
                group = m.groupdict()
                shg_label = group['shg_label']
                next_hop = group['next_hop']
                label_dict.setdefault('label', {}). \
                    setdefault(shg_label, {}). \
                    update({'nexthop': next_hop})
                continue

            # 0210.0300.9e00.0210.0000 Gi0/3/0/0      1.100.100.100
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
            
            # 2.100.100.100
            m = p1_1.match(line)
            if m:
                group = m.groupdict()
                next_hop = group['next_hop']
                next_hop_list.append(next_hop)
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