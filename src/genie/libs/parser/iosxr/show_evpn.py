""" show_evpn.py

show evpn parser class

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
                    'mac': EUI(m.group('mac')),
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
                    'mac': EUI(m.group('mac')),
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

class ShowEvpnInternalLabelSchema(MetaParser):
    schema = {
        'evi':{
            Any(): {
                'ethernet_segment_id': {
                    Any(): {
                        'index': {
                            Any(): {
                                'ether_tag': str,
                                'label': str,
                                Optional('encap'): str
                            }
                        }
                    }
                }
            }
        }
    }

class ShowEvpnInternalLabel(ShowEvpnInternalLabelSchema):

    cli_command = 'show evpn internal-label'
    def cli(self, output=None):
        
        ret_dict = {}
        index_dict = {}

        out = output if output else self.device.execute(self.cli_command)
        
        # 1000 0000.0102.0304.0506.07aa 0 None
        # 1000 0000.0102.0304.0506.07aa 200 24011
        p1 = re.compile(r'^(?P<evi>\d+)( +(?P<encap>\S+))? +'
                '(?P<ethernet_segment_id>[\w\.]+) +(?P<ether_tag>\S+) +(?P<label>\S+)$')

        for line in out.splitlines():
            line = line.strip()
            
            # 1000 0000.0102.0304.0506.07aa 0 None
            # 1000 0000.0102.0304.0506.07aa 200 24011
            # 100        MPLS   0036.3700.0000.0000.1100    0          64006
            m = p1.match(line)
            if m:
                group = m.groupdict()
                evi = int(group['evi'])
                ethernet_segment_id = group['ethernet_segment_id']
                ether_tag = group['ether_tag']
                label = group['label']

                index = index_dict.get(ethernet_segment_id, 0) + 1
                
                segment_id_dict = ret_dict.setdefault('evi', {}). \
                    setdefault(evi, {}). \
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
            
            # Multi-paths resolved: TRUE


        return ret_dict

# vim: ft=python ts=8 sw=4 et
