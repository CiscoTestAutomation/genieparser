""" show_ip_rsvp_fast_reroute.py

IOSXE parsers for the following show commands:
    * 'show ip rsvp fast-reroute'

Copyright (c) 2022-2024 by cisco Systems, Inc.
All rights reserved
    * show ip rsvp sender detail filter dst-port 30
"""

# Python
import re
import logging

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional, ListOf
from genie.libs.parser.utils.common import Common

log = logging.getLogger(__name__)


class ShowIpRsvpFastRerouteSchema(MetaParser):
    """Schema for show ip rsvp fast-reroute"""

    schema = {
        Optional('p2p_protected_lsps'): {
            Any(): {
                'protect_intf': str,
                'bandwidth': str,
                'bandwidth_type': str,
                'backup_tunnel': str,
                'backup_label': str,
                'state': str,
                'level': str,
                'type': str
            }
        },
        Optional('p2p_protected_sub_lsps'): {
            Any(): {
                'protect_intf': str,
                'bandwidth': str,
                'bandwidth_type': str,
                'backup_tunnel': str,
                'backup_label': str,
                'state': str
            }
        }
    }


# =====================================
# Parser for 'show ip rsvp fast-reroute'
# =====================================
class ShowIpRsvpFastReroute(ShowIpRsvpFastRerouteSchema):
    """show ip rsvp fast-reroute
    """

    cli_command = 'show ip rsvp fast-reroute'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Protected LSP
        p0 = re.compile(r'Protected\s+LSP')

        # Bender_08_t13             Te0/0/8  250M:G     Tu232:3       Ready  any-unl Nhop
        p1 = re.compile(
            r"(?P<p2p_protected_lsp>\S+)\s+"
            r"(?P<protect_intf>\S+)\s+"
            r"(?P<bandwidth_and_type>\d+[a-zA-Z]+\:\w+)\s+"
            r"(?P<backup_tunnel_and_label>\w+\:\w+)\s+"
            r"(?P<state>\S+)\s+"
            r"(?P<level>\S+)\s+"
            r"(?P<type>\S+)\s*$")

        # *Protected Sub-LSP
        p2 = re.compile(r'\*Protected\s+Sub\-LSP')

        # Bender_08_t13             Te0/0/8  250M:G     Tu232:3       Ready
        p3 = re.compile(
            r"(?P<p2p_protected_sub_lsp>\S+)\s+"
            r"(?P<protect_intf>\S+)\s+"
            r"(?P<bandwidth_and_type>\d+[a-zA-Z]+\:\w+)\s+"
            r"(?P<backup_tunnel_and_label>\w+\:\w+)\s+"
            r"(?P<state>\S+)\s*$")

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # Protected LSP
            m = p0.match(line)
            if m:
                p2p_protected_lsps_dict = ret_dict.setdefault('p2p_protected_lsps', {})
                continue

            # Bender_08_t13             Te0/0/8  250M:G     Tu232:3       Ready  any-unl Nhop
            m = p1.match(line)
            if m:
                group_dict = m.groupdict()
                p2p_protected_lsp_dict = \
                    p2p_protected_lsps_dict.setdefault(group_dict['p2p_protected_lsp'], {})
                bandwidth, bandwidth_type = group_dict['bandwidth_and_type'].strip().split(":")
                backup_tunnel, backup_label = group_dict['backup_tunnel_and_label'].strip().split(":")
                p2p_protected_lsp_dict.update({
                    'protect_intf': Common.convert_intf_name(group_dict['protect_intf']),
                    'bandwidth': bandwidth,
                    'bandwidth_type': bandwidth_type,
                    'backup_tunnel': Common.convert_intf_name(backup_tunnel),
                    'backup_label': backup_label,
                    'state': group_dict['state'],
                    'level': group_dict['level'],
                    'type': group_dict['type']})
                continue

            # *Protected Sub-LSP
            m = p2.match(line)
            if m:
                p2p_protected_sub_lsps_dict = ret_dict.setdefault('p2p_protected_sub_lsps', {})
                continue

            # Bender_08_t13             Te0/0/8  250M:G     Tu232:3       Ready
            m = p3.match(line)
            if m:
                group_dict = m.groupdict()
                p2p_protected_sub_lsp_dict = \
                    p2p_protected_sub_lsps_dict.setdefault(group_dict['p2p_protected_sub_lsp'], {})
                bandwidth, bandwidth_type = group_dict['bandwidth_and_type'].strip().split(":")
                backup_tunnel, backup_label = group_dict['backup_tunnel_and_label'].strip().split(":")
                p2p_protected_sub_lsp_dict.update({
                    'protect_intf': Common.convert_intf_name(group_dict['protect_intf']),
                    'bandwidth': bandwidth,
                    'bandwidth_type': bandwidth_type,
                    'backup_tunnel': Common.convert_intf_name(backup_tunnel),
                    'backup_label': backup_label,
                    'state': group_dict['state']})
                continue

        return ret_dict


class ShowIpRsvpSenderDetailFilterDstPort30Schema(MetaParser):
    schema = {
        'sessions': {
            Any(): {
                'name': str,
                Optional('details'): dict,
                Optional('path'): {
                    'tunnel_destination': str,
                    'tunnel_id': int,
                    'ext_tunnel_id': str,
                    'tunnel_sender': str,
                    'lsp_id': int,
                    'path_refreshes': {
                        'sent': {
                            'nhop': str,
                            'outgoing_interface': str
                        }
                    },
                    'session_attributes': {
                        'setup_priority': int,
                        'holding_priority': int,
                        'flags': {
                            'hex': str,
                            'local_protection_desired': bool,
                            'label_recording': bool,
                            'se_style': bool
                        },
                        'session_name': str
                    },
                    'ero': {
                        'incoming': ListOf(dict),
                        'outgoing': ListOf(dict)
                    },
                    'traffic_parameters': {
                        'rate': str,
                        'max_burst': str,
                        'min_policed_unit_bytes': int,
                        'max_packet_size_bytes': int
                    },
                    'fast_reroute': {
                        'inbound_frr': str,
                        'outbound_frr': str,
                        'backup_tunnel': {
                            'name': str,
                            'label': int
                        },
                        'backup_sender_template': {
                            'tunnel_sender': str,
                            'lsp_id': int
                        },
                        'backup_filterspec': {
                            'tunnel_sender': str,
                            'lsp_id': int
                        }
                    },
                    'path_id_handle': str,
                    'incoming_policy': {
                        'status': str,
                        'policy_sources': ListOf(str)
                    },
                    'status': str,
                    'output_interface': str,
                    'output_policy_status': str,
                    'output_handle': str,
                    'output_policy_sources': ListOf(str)
                }
            }
        }
    }


class ShowIpRsvpSenderDetailFilterDstPort30(ShowIpRsvpSenderDetailFilterDstPort30Schema):
    cli_command = "show ip rsvp sender detail filter dst-port 30"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        ret_dict = {}
        if not output:
            return ret_dict

        # Session Type 1 (rsvp)
        p1 = re.compile(r'^\s*Session\s+Type\s+(?P<session_type>\d+)\s*\((?P<name>[^)]+)\)$')

        # PATH:
        p2 = re.compile(r'^\s*PATH\s*:\s*$')

        #   Tun Dest:   100.1.1.2  Tun ID: 30  Ext Tun ID: 100.1.1.3
        p3 = re.compile(
            r'^\s*Tun\s+Dest\s*:\s*(?P<tun_dest>\S+)\s+Tun\s+ID\s*:\s*(?P<tun_id>\d+)\s+Ext\s+Tun\s+ID\s*:\s*(?P<ext_tun_id>\S+)\s*$')

        #   Tun Sender: 100.1.1.3  LSP ID: 40
        p4 = re.compile(r'^\s*Tun\s+Sender\s*:\s*(?P<tunnel_sender>\S+)\s+LSP\s+ID\s*:\s*(?P<lsp_id>\d+)\s*$')

        #   Path refreshes:
        p5 = re.compile(r'^\s*Path\s+refreshes\s*:\s*$')

        #     sent:     to   NHOP 10.1.1.5 on FiveGigabitEthernet0/0/2
        p6 = re.compile(r'^\s*sent\s*:\s*to\s+NHOP\s+(?P<nhop>\S+)\s+on\s+(?P<intf>\S+)\s*$')

        #   Session Attr:
        p7 = re.compile(r'^\s*Session\s+Attr\s*:\s*$')

        #     Setup Prio: 2, Holding Prio: 2
        p8 = re.compile(r'^\s*Setup\s+Prio\s*:\s*(?P<setup>\d+)\s*,\s*Holding\s+Prio\s*:\s*(?P<holding>\d+)\s*$')

        #     Flags: (0x7) Local Prot desired, Label Recording, SE Style
        p9 = re.compile(r'^\s*Flags\s*:\s*\((?P<hex>0x[0-9a-fA-F]+)\)\s*(?P<flags_text>.*)$')

        #     Session Name: rt3_t30
        p10 = re.compile(r'^\s*Session\s+Name\s*:\s*(?P<session_name>\S+)\s*$')

        #   ERO: (incoming)
        p11 = re.compile(r'^\s*ERO\s*:\s*\((?P<direction>incoming|outgoing)\)\s*$')

        #     100.1.1.3 (Strict IPv4 Prefix, 8 bytes, /32)
        p12 = re.compile(
            r'^\s*(?P<address>\S+)\s+\((?P<type>[^,]+),\s*(?P<bytes>\d+)\s+bytes,\s*/(?P<prefix_length>\d+)\)\s*$')

        #   Traffic params - Rate: 158K bits/sec, Max. burst: 1K bytes
        p13 = re.compile(
            r'^\s*Traffic\s+params\s*-\s*Rate\s*:\s*(?P<rate>[^,]+),\s*Max\.\s*burst\s*:\s*(?P<max_burst>.+)\s*$')

        #     Min Policed Unit: 0 bytes, Max Pkt Size 2147483647 bytes
        p14 = re.compile(
            r'^\s*Min\s+Policed\s+Unit\s*:\s*(?P<min>\d+)\s+bytes,\s*Max\s+Pkt\s+Size\s*(?P<max>\d+)\s+bytes\s*$')

        #   Fast-Reroute Backup info:
        p15 = re.compile(r'^\s*Fast\-Reroute\s+Backup\s+info\s*:\s*$')

        #     Inbound  FRR: Not active
        p16 = re.compile(r'^\s*Inbound\s+FRR\s*:\s*(?P<inbound>.+)\s*$')

        #     Outbound FRR: Ready -- backup tunnel selected
        p17 = re.compile(r'^\s*Outbound\s+FRR\s*:\s*(?P<outbound>.+)\s*$')

        #       Backup Tunnel: Tu31       (label 3)
        p18 = re.compile(r'^\s*Backup\s+Tunnel\s*:\s*(?P<name>\S+)\s*\(label\s*(?P<label>\d+)\)\s*$')

        #       Bkup Sender Template:
        p19 = re.compile(r'^\s*Bkup\s+Sender\s+Template\s*:\s*$')

        #         Tun Sender: 10.1.1.9  LSP ID: 40
        p20 = re.compile(r'^\s*Tun\s+Sender\s*:\s*(?P<tunnel_sender>\S+)\s+LSP\s+ID\s*:\s*(?P<lsp_id>\d+)\s*$')

        #       Bkup FilerSpec:
        p21 = re.compile(r'^\s*Bkup\s+FilerSpec\s*:\s*$')

        #         Tun Sender: 10.1.1.9, LSP ID: 40
        p22 = re.compile(r'^\s*Tun\s+Sender\s*:\s*(?P<tunnel_sender>\S+)\s*,\s*LSP\s+ID\s*:\s*(?P<lsp_id>\d+)\s*$')

        #   Path ID handle: FC000428.
        p23 = re.compile(r'^\s*Path\s+ID\s+handle\s*:\s*(?P<handle>[A-F0-9]+)\.?$')

        #   Incoming policy: Accepted. Policy source(s): MPLS/TE
        p24 = re.compile(
            r'^\s*Incoming\s+policy\s*:\s*(?P<status>[^.]+)\.\s*Policy\s+source\(s\)\s*:\s*(?P<sources>.+)\s*$')

        #   Status: Proxied
        p25 = re.compile(r'^\s*Status\s*:\s*(?P<status>.+)\s*$')

        #   Output on FiveGigabitEthernet0/0/2. Policy status: Forwarding. Handle: 7D000405
        p26 = re.compile(
            r'^\s*Output\s+on\s+(?P<intf>\S+)\.\s*Policy\s+status\s*:\s*(?P<pol_status>[^.]+)\.\s*Handle\s*:\s*(?P<handle>[A-F0-9]+)\s*$')

        #     Policy source(s): MPLS/TE
        p27 = re.compile(r'^\s*Policy\s+source\(s\)\s*:\s*(?P<sources>.+)\s*$')

        sessions_dict = ret_dict.setdefault('sessions', {})
        current_session_id = None
        path_dict = None
        in_path = False
        current_ero_direction = None
        fast_reroute_dict = None
        in_backup_sender_template = False
        in_backup_filterspec = False

        for raw_line in output.splitlines():
            line = raw_line.strip()
            if not line:
                continue

            # Session Type 1 (rsvp)
            m = p1.match(line)
            if m:
                group = m.groupdict()
                current_session_id = group['session_type']
                session_dict = sessions_dict.setdefault(current_session_id, {})
                session_dict['name'] = group['name']
                if group['name'] == "rsvp":
                    session_dict['details'] = {}
                in_path = False
                path_dict = None
                current_ero_direction = None
                fast_reroute_dict = None
                in_backup_sender_template = False
                in_backup_filterspec = False
                continue

            # PATH:
            m = p2.match(line)
            if m and current_session_id:
                session_dict = sessions_dict.setdefault(current_session_id, {})
                path_dict = session_dict.setdefault('path', {})
                in_path = True
                current_ero_direction = None
                fast_reroute_dict = None
                in_backup_sender_template = False
                in_backup_filterspec = False
                continue

            #   Tun Dest:   100.1.1.2  Tun ID: 30  Ext Tun ID: 100.1.1.3
            m = p3.match(line)
            if m and in_path and path_dict is not None:
                gd = m.groupdict()
                path_dict['tunnel_destination'] = gd['tun_dest']
                path_dict['tunnel_id'] = int(gd['tun_id'])
                path_dict['ext_tunnel_id'] = gd['ext_tun_id']
                continue

            #   Tun Sender: 100.1.1.3  LSP ID: 40
            m = p4.match(line)
            if m and in_path and path_dict is not None and not in_backup_sender_template and not in_backup_filterspec:
                gd = m.groupdict()
                path_dict['tunnel_sender'] = gd['tunnel_sender']
                path_dict['lsp_id'] = int(gd['lsp_id'])
                continue

            #   Path refreshes:
            m = p5.match(line)
            if m and in_path and path_dict is not None:
                pr_dict = path_dict.setdefault('path_refreshes', {})
                sent_dict = pr_dict.setdefault('sent', {})
                continue

            #     sent:     to   NHOP 10.1.1.5 on FiveGigabitEthernet0/0/2
            m = p6.match(line)
            if m and in_path and path_dict is not None:
                gd = m.groupdict()
                pr_dict = path_dict.setdefault('path_refreshes', {})
                sent_dict = pr_dict.setdefault('sent', {})
                sent_dict['nhop'] = gd['nhop']
                sent_dict['outgoing_interface'] = gd['intf']
                continue

            #   Session Attr:
            m = p7.match(line)
            if m and in_path and path_dict is not None:
                sa_dict = path_dict.setdefault('session_attributes', {})
                continue

            #     Setup Prio: 2, Holding Prio: 2
            m = p8.match(line)
            if m and in_path and path_dict is not None:
                gd = m.groupdict()
                sa_dict = path_dict.setdefault('session_attributes', {})
                sa_dict['setup_priority'] = int(gd['setup'])
                sa_dict['holding_priority'] = int(gd['holding'])
                continue

            #     Flags: (0x7) Local Prot desired, Label Recording, SE Style
            m = p9.match(line)
            if m and in_path and path_dict is not None:
                gd = m.groupdict()
                sa_dict = path_dict.setdefault('session_attributes', {})
                flags_dict = sa_dict.setdefault('flags', {})
                flags_dict['hex'] = gd['hex']
                flags_text = gd['flags_text']
                flags_dict['local_protection_desired'] = 'Local Prot desired' in flags_text
                flags_dict['label_recording'] = 'Label Recording' in flags_text
                flags_dict['se_style'] = 'SE Style' in flags_text
                continue

            #     Session Name: rt3_t30
            m = p10.match(line)
            if m and in_path and path_dict is not None:
                gd = m.groupdict()
                sa_dict = path_dict.setdefault('session_attributes', {})
                sa_dict['session_name'] = gd['session_name']
                continue

            #   ERO: (incoming)
            m = p11.match(line)
            if m and in_path and path_dict is not None:
                gd = m.groupdict()
                current_ero_direction = gd['direction']
                ero_dict = path_dict.setdefault('ero', {})
                ero_dict.setdefault(current_ero_direction, [])
                continue

            #     100.1.1.3 (Strict IPv4 Prefix, 8 bytes, /32)
            m = p12.match(line)
            if m and in_path and path_dict is not None and current_ero_direction in ('incoming', 'outgoing'):
                gd = m.groupdict()
                entry = {
                    'address': gd['address'],
                    'type': gd['type'],
                    'bytes': int(gd['bytes']),
                    'prefix_length': int(gd['prefix_length'])
                }
                ero_dict = path_dict.setdefault('ero', {})
                ero_list = ero_dict.setdefault(current_ero_direction, [])
                ero_list.append(entry)
                continue

            #   Traffic params - Rate: 158K bits/sec, Max. burst: 1K bytes
            m = p13.match(line)
            if m and in_path and path_dict is not None:
                gd = m.groupdict()
                tp_dict = path_dict.setdefault('traffic_parameters', {})
                tp_dict['rate'] = gd['rate']
                tp_dict['max_burst'] = gd['max_burst']
                continue

            #     Min Policed Unit: 0 bytes, Max Pkt Size 2147483647 bytes
            m = p14.match(line)
            if m and in_path and path_dict is not None:
                gd = m.groupdict()
                tp_dict = path_dict.setdefault('traffic_parameters', {})
                tp_dict['min_policed_unit_bytes'] = int(gd['min'])
                tp_dict['max_packet_size_bytes'] = int(gd['max'])
                continue

            #   Fast-Reroute Backup info:
            m = p15.match(line)
            if m and in_path and path_dict is not None:
                fast_reroute_dict = path_dict.setdefault('fast_reroute', {})
                in_backup_sender_template = False
                in_backup_filterspec = False
                continue

            #     Inbound  FRR: Not active
            m = p16.match(line)
            if m and fast_reroute_dict is not None:
                gd = m.groupdict()
                fast_reroute_dict['inbound_frr'] = gd['inbound']
                continue

            #     Outbound FRR: Ready -- backup tunnel selected
            m = p17.match(line)
            if m and fast_reroute_dict is not None:
                gd = m.groupdict()
                fast_reroute_dict['outbound_frr'] = gd['outbound']
                continue

            #       Backup Tunnel: Tu31       (label 3)
            m = p18.match(line)
            if m and fast_reroute_dict is not None:
                gd = m.groupdict()
                bt_dict = fast_reroute_dict.setdefault('backup_tunnel', {})
                bt_dict['name'] = gd['name']
                bt_dict['label'] = int(gd['label'])
                continue

            #       Bkup Sender Template:
            m = p19.match(line)
            if m and fast_reroute_dict is not None:
                fast_reroute_dict.setdefault('backup_sender_template', {})
                in_backup_sender_template = True
                in_backup_filterspec = False
                continue

            #         Tun Sender: 10.1.1.9  LSP ID: 40
            m = p20.match(line)
            if m and fast_reroute_dict is not None and in_backup_sender_template:
                gd = m.groupdict()
                bst = fast_reroute_dict.setdefault('backup_sender_template', {})
                bst['tunnel_sender'] = gd['tunnel_sender']
                bst['lsp_id'] = int(gd['lsp_id'])
                in_backup_sender_template = False
                continue

            #       Bkup FilerSpec:
            m = p21.match(line)
            if m and fast_reroute_dict is not None:
                fast_reroute_dict.setdefault('backup_filterspec', {})
                in_backup_filterspec = True
                in_backup_sender_template = False
                continue

            #         Tun Sender: 10.1.1.9, LSP ID: 40
            m = p22.match(line)
            if m and fast_reroute_dict is not None and in_backup_filterspec:
                gd = m.groupdict()
                bfs = fast_reroute_dict.setdefault('backup_filterspec', {})
                bfs['tunnel_sender'] = gd['tunnel_sender']
                bfs['lsp_id'] = int(gd['lsp_id'])
                in_backup_filterspec = False
                continue

            #   Path ID handle: FC000428.
            m = p23.match(line)
            if m and in_path and path_dict is not None:
                gd = m.groupdict()
                path_dict['path_id_handle'] = gd['handle']
                continue

            #   Incoming policy: Accepted. Policy source(s): MPLS/TE
            m = p24.match(line)
            if m and in_path and path_dict is not None:
                gd = m.groupdict()
                ip_dict = path_dict.setdefault('incoming_policy', {})
                ip_dict['status'] = gd['status'].strip()
                sources = [s.strip() for s in gd['sources'].split(',')]
                ip_dict['policy_sources'] = sources
                continue

            #   Status: Proxied
            m = p25.match(line)
            if m and in_path and path_dict is not None:
                gd = m.groupdict()
                path_dict['status'] = gd['status'].strip()
                continue

            #   Output on FiveGigabitEthernet0/0/2. Policy status: Forwarding. Handle: 7D000405
            m = p26.match(line)
            if m and in_path and path_dict is not None:
                gd = m.groupdict()
                path_dict['output_interface'] = gd['intf']
                path_dict['output_policy_status'] = gd['pol_status'].strip()
                path_dict['output_handle'] = gd['handle']
                continue

            #     Policy source(s): MPLS/TE
            m = p27.match(line)
            if m and in_path and path_dict is not None:
                gd = m.groupdict()
                sources = [s.strip() for s in gd['sources'].split(',')]
                path_dict['output_policy_sources'] = sources
                continue

        return ret_dict
