""" show_evpn.py

show evpn parser class
show evpn evi mac
show evpn evi mac private
show evpn evi vpn-id {vpn_id} mac
"""

from netaddr import EUI
from ipaddress import ip_address
import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (Any,
                                                Optional)

from genie.libs.parser.base import *

re_8bit_u = r'(?:' + r'|'.join([
    r'[0-9]',
    r'[1-9][0-9]',
    r'1[0-9][0-9]',
    r'2[0-4][0-9]',
    r'25[0-5]',
]) + r')'
re_8bit_x = r'(?:[A-Fa-f0-9]{1,2})'
re_8bit_02x = r'(?:[A-Fa-f0-9]{2})'
re_16bit_x = r'(?:[A-Fa-f0-9]{1,4})'
re_16bit_04x = r'(?:[A-Fa-f0-9]{4})'
re_mac = r'(?:' + r'|'.join([
    r'\.'.join([re_16bit_x] * 3),
    r':'.join([re_8bit_x] * 6),
    r'-'.join([re_8bit_x] * 6),
    r'\.'.join([re_8bit_x] * 6),
]) + r')'
re_ipv4 = r'(?:' + r'\.'.join([re_8bit_u] * 4) + r')'
re_ipv6 = r'(?:[A-Fa-f0-9:]*:[A-Fa-f0-9:]*(?::' + re_ipv4 + ')?)'
re_ip = r'(?:' + r'|'.join([re_ipv4, re_ipv6]) + ')'
re_label_str = r'(?:' + r'|'.join([
    r'[0-9]+',
    r'[A-Za-z0-9-]+',  # See mpls_label_strings @ mpls/base/include/mpls_label_defs_extra.h
]) + r')'


class ShowEvpnEvi(MetaParser):
    """Parser class for 'show evpn evi' CLI."""

    # TODO schema
    cli_command = 'show evpn evi'

    def cli(self):
        """parsing mechanism: cli"""

        tcl_package_require_caas_parsers()
        kl = tcl_invoke_caas_abstract_parser(
            device=self.device, exec=self.cli_command)

        return kl


class ShowEvpnEviDetail(MetaParser):
    """Parser class for 'show evpn evi detail' CLI."""

    # TODO schema
    cli_command = 'show evpn evi detail'
    def cli(self):
        """parsing mechanism: cli
        """
        tcl_package_require_caas_parsers()
        kl = tcl_invoke_caas_abstract_parser(
            device=self.device, exec=self.cli_command)

        return kl


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


class ShowEvpnInternalLabelDetail(MetaParser):

    # TODO schema

    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    cli_command = 'show evpn internal-label detail'

    def cli(self,output=None):
        """parsing mechanism: cli
        """
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        res = {
            'entries': [],
        }

        for line in out.splitlines():
            line = line.rstrip()

            # 5     0012.1200.0000.0000.0002                0        24114
            m = re.match(r'^\s*(?P<evi>\d+)\s+'
                          '(?P<esi>[\w.]+)\s+'
                          '(?P<eth_tag>\d+)\s+'
                          '(?P<internal_label>\w+)$',line)

            if m:
                # create new record
                record = { 'evi' : m.group('evi'),
                           'esi' : m.group('esi'),
                           'eth_tag' : m.group('eth_tag'),
                           'internal_label' : m.group('internal_label'),
                           'pathlists' : {
                                'mac' : [],
                                'es_ead' : [],
                                'evi_ead' : [],
                                'summary' : []
                            }
                         }

                res['entries'].append(record)

            # Multi-paths resolved: TRUE
            m = re.match(r'^\s+Multi-paths resolved: '
                          '(?P<mp_resolved>\w+)$',line)

            if m:
                res['entries'][-1]['mp_resolved'] = m.group('mp_resolved')


            # Multi-paths resolved: TRUE (Remote single-active)
            m = re.match(r'^\s+Multi-paths resolved: '
                          '(?P<mp_resolved>\w+) '
                          '\((?P<mp_single_active>.+)\)$',line)

            if m:
                res['entries'][-1]['mp_resolved'] = m.group('mp_resolved')
                res['entries'][-1]['mp_single_active'] = m.group('mp_single_active')

            # MAC     10.70.20.20                              24212
            m = re.match(r'^\s+MAC\s+'
                          '(?P<nexthop>[\d.]+)\s+'
                          '(?P<label>\d+)$',line)

            if m:
                mac_flag = True
                es_ead_flag = False
                evi_ead_flag = False
                summary_flag = False

                res['entries'][-1]['pathlists']['mac'].append(
                    {'nexthop' : m.group('nexthop'),
                     'label' : m.group('label')}
                )

            # EAD/ES  10.10.10.10                              0
            m = re.match(r'^\s+EAD/ES\s+'
                          '(?P<nexthop>[\d.]+)\s+'
                          '(?P<label>\d+)$',line)

            if m:
                mac_flag = False
                es_ead_flag = True
                evi_ead_flag = False
                summary_flag = False

                res['entries'][-1]['pathlists']['es_ead'].append(
                    {'nexthop' : m.group('nexthop'),
                     'label' : m.group('label')}
                )

            # EAD/EVI 10.10.10.10                              24012
            m = re.match(r'^\s+EAD/EVI\s+'
                          '(?P<nexthop>[\d.]+)\s+'
                          '(?P<label>\d+)$',line)

            if m:
                mac_flag = False
                es_ead_flag = False
                evi_ead_flag = True
                summary_flag = False

                res['entries'][-1]['pathlists']['evi_ead'].append(
                    {'nexthop' : m.group('nexthop'),
                     'label' : m.group('label')}
                )

            # Summary 10.70.20.20                              24212
            m = re.match(r'^\s+Summary\s+'
                          '(?P<nexthop>[\d.]+)\s+'
                          '(?P<label>\d+)$',line)

            if m:
                mac_flag = False
                es_ead_flag = False
                evi_ead_flag = False
                summary_flag = True

                res['entries'][-1]['pathlists']['summary'].append(
                    {'nexthop' : m.group('nexthop'),
                     'label' : m.group('label')}
                )

            #         10.70.20.20                              0
            m = re.match(r'^\s+'
                         '(?P<nexthop>[\d.]+)\s+'
                         '(?P<label>\d+)$',line)

            if m:
               if mac_flag:
                   res['entries'][-1]['pathlists']['mac'].append(
                       {'nexthop' : m.group('nexthop'),
                        'label' : m.group('label')}
                   )
               elif es_ead_flag:
                   res['entries'][-1]['pathlists']['es_ead'].append(
                       {'nexthop' : m.group('nexthop'),
                        'label' : m.group('label')}
                   )
               elif evi_ead_flag:
                   res['entries'][-1]['pathlists']['evi_ead'].append(
                       {'nexthop' : m.group('nexthop'),
                        'label' : m.group('label')}
                   )
               elif summary_flag:
                   res['entries'][-1]['pathlists']['summary'].append(
                       {'nexthop' : m.group('nexthop'),
                        'label' : m.group('label')}
                   )

            #         10.10.10.10 (B)                          24012
            m = re.match(r'^\s+'
                         '(?P<nexthop>[\d.]+)\s+'
                         '\((?P<flag>\w+)\)\s+'
                         '(?P<label>\d+)$',line)

            if m:
               res['entries'][-1]['pathlists']['summary'].append(
                   {'nexthop' : m.group('nexthop'),
                    'label' : m.group('label'),
                    'flag' : m.group('flag')}
               )

        return res

# vim: ft=python ts=8 sw=4 et