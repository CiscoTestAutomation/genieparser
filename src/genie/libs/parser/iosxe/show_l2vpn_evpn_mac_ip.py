""" show_l2vpn_evpn_mac_ip.py

IOSXE parsers for the following show commands:

    * show l2vpn evpn mac ip
    * show l2vpn evpn mac ip address <ipv4_addr>
    * show l2vpn evpn mac ip address <ipv4_addr> detail
    * show l2vpn evpn mac ip address <ipv6_addr>
    * show l2vpn evpn mac ip address <ipv6_addr> detail
    * show l2vpn evpn mac ip bridge-domain <bd_id>
    * show l2vpn evpn mac ip bridge-domain <bd_id> address <ipv4_addr>
    * show l2vpn evpn mac ip bridge-domain <bd_id> address <ipv4_addr>  detail
    * show l2vpn evpn mac ip bridge-domain <bd_id> address <ipv6_addr>
    * show l2vpn evpn mac ip bridge-domain <bd_id> address <ipv6_addr> detail
    * show l2vpn evpn mac ip bridge-domain <bd_id> detail
    * show l2vpn evpn mac ip bridge-domain <bd_id> duplicate
    * show l2vpn evpn mac ip bridge-domain <bd_id> duplicate detail
    * show l2vpn evpn mac ip bridge-domain <bd_id> duplicate summary
    * show l2vpn evpn mac ip bridge-domain <bd_id> local
    * show l2vpn evpn mac ip bridge-domain <bd_id> local detail
    * show l2vpn evpn mac ip bridge-domain <bd_id> local summary
    * show l2vpn evpn mac ip bridge-domain <bd_id> mac <mac_addr>
    * show l2vpn evpn mac ip bridge-domain <bd_id> mac <mac_addr> address <ipv4_addr>
    * show l2vpn evpn mac ip bridge-domain <bd_id> mac <mac_addr> address <ipv4_addr> detail
    * show l2vpn evpn mac ip bridge-domain <bd_id> mac <mac_addr> address <ipv6_addr>
    * show l2vpn evpn mac ip bridge-domain <bd_id> mac <mac_addr> address <ipv6_addr> detail
    * show l2vpn evpn mac ip bridge-domain <bd_id> mac <mac_addr> detail
    * show l2vpn evpn mac ip bridge-domain <bd_id> mac <mac_addr> summary
    * show l2vpn evpn mac ip bridge-domain <bd_id> remote
    * show l2vpn evpn mac ip bridge-domain <bd_id> remote detail
    * show l2vpn evpn mac ip bridge-domain <bd_id> remote summary
    * show l2vpn evpn mac ip bridge-domain <bd_id> summary
    * show l2vpn evpn mac ip detail
    * show l2vpn evpn mac ip duplicate
    * show l2vpn evpn mac ip duplicate detail
    * show l2vpn evpn mac ip duplicate summary
    * show l2vpn evpn mac ip evi <evi_id>
    * show l2vpn evpn mac ip evi <evi_id> address <ipv4_addr>
    * show l2vpn evpn mac ip evi <evi_id> address <ipv4_addr> detail
    * show l2vpn evpn mac ip evi <evi_id> address <ipv6_addr>
    * show l2vpn evpn mac ip evi <evi_id> address <ipv6_addr> detail
    * show l2vpn evpn mac ip evi <evi_id> detail
    * show l2vpn evpn mac ip evi <evi_id> duplicate
    * show l2vpn evpn mac ip evi <evi_id> duplicate detail
    * show l2vpn evpn mac ip evi <evi_id> duplicate summary
    * show l2vpn evpn mac ip evi <evi_id> local
    * show l2vpn evpn mac ip evi <evi_id> local detail
    * show l2vpn evpn mac ip evi <evi_id> local summary
    * show l2vpn evpn mac ip evi <evi_id> mac <mac_addr>
    * show l2vpn evpn mac ip evi <evi_id> mac <mac_addr> address <ipv4_addr>
    * show l2vpn evpn mac ip evi <evi_id> mac <mac_addr> address <ipv4_addr> detail
    * show l2vpn evpn mac ip evi <evi_id> mac <mac_addr> address <ipv6_addr>
    * show l2vpn evpn mac ip evi <evi_id> mac <mac_addr> address <ipv6_addr> detail
    * show l2vpn evpn mac ip evi <evi_id> mac <mac_addr> detail
    * show l2vpn evpn mac ip evi <evi_id> mac <mac_addr> summary
    * show l2vpn evpn mac ip evi <evi_id> remote
    * show l2vpn evpn mac ip evi <evi_id> remote detail
    * show l2vpn evpn mac ip evi <evi_id> remote summary
    * show l2vpn evpn mac ip evi <evi_id> summary
    * show l2vpn evpn mac ip local
    * show l2vpn evpn mac ip local detail
    * show l2vpn evpn mac ip local summary
    * show l2vpn evpn mac ip mac <mac_addr>
    * show l2vpn evpn mac ip mac <mac_addr> address <ipv4_addr>
    * show l2vpn evpn mac ip mac <mac_addr> address <ipv4_addr> detail
    * show l2vpn evpn mac ip mac <mac_addr> address <ipv6_addr>
    * show l2vpn evpn mac ip mac <mac_addr> address <ipv6_addr> detail
    * show l2vpn evpn mac ip mac <mac_addr> detail
    * show l2vpn evpn mac ip mac <mac_addr> summary
    * show l2vpn evpn mac ip remote
    * show l2vpn evpn mac ip remote detail
    * show l2vpn evpn mac ip remote summary
    * show l2vpn evpn mac ip summary

Copyright (c) 2021 by Cisco Systems, Inc.
All rights reserved.
"""

import re

# Genie
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, \
                                               Optional

# ====================================
# Schema for 'show l2vpn evpn mac ip'
# ====================================
class ShowL2vpnEvpnMacIpSchema(MetaParser):

    """ Schema for show l2vpn evpn mac ip
                   show l2vpn evpn mac ip address <ipv4_addr>
                   show l2vpn evpn mac ip address <ipv6_addr>
                   show l2vpn evpn mac ip bridge-domain <bd_id>
                   show l2vpn evpn mac ip bridge-domain <bd_id> address <ipv4_addr>
                   show l2vpn evpn mac ip bridge-domain <bd_id> address <ipv6_addr>
                   show l2vpn evpn mac ip bridge-domain <bd_id> duplicate
                   show l2vpn evpn mac ip bridge-domain <bd_id> local
                   show l2vpn evpn mac ip bridge-domain <bd_id> mac <mac_addr>
                   show l2vpn evpn mac ip bridge-domain <bd_id> mac <mac_addr> address <ipv4_addr>
                   show l2vpn evpn mac ip bridge-domain <bd_id> mac <mac_addr> address <ipv6_addr>
                   show l2vpn evpn mac ip bridge-domain <bd_id> remote
                   show l2vpn evpn mac ip duplicate
                   show l2vpn evpn mac ip evi <evi_id>
                   show l2vpn evpn mac ip evi <evi_id> address <ipv4_addr>
                   show l2vpn evpn mac ip evi <evi_id> address <ipv6_addr>
                   show l2vpn evpn mac ip evi <evi_id> duplicate
                   show l2vpn evpn mac ip evi <evi_id> local
                   show l2vpn evpn mac ip evi <evi_id> mac <mac_addr>
                   show l2vpn evpn mac ip evi <evi_id> mac <mac_addr> address <ipv4_addr>
                   show l2vpn evpn mac ip evi <evi_id> mac <mac_addr> address <ipv6_addr>
                   show l2vpn evpn mac ip evi <evi_id> remote
                   show l2vpn evpn mac ip local
                   show l2vpn evpn mac ip mac <mac_addr>
                   show l2vpn evpn mac ip mac <mac_addr> address <ipv4_addr>
                   show l2vpn evpn mac ip mac <mac_addr> address <ipv6_addr>
                   show l2vpn evpn mac ip remote
    """

    schema = {
        Any(): { # IP Address
            'evi': int,
            'bd_id': int,
            'mac_addr': str,
            'next_hops': list,
        },
    }

# ====================================
# Parser for 'show l2vpn evpn mac ip'
# ====================================
class ShowL2vpnEvpnMacIp(ShowL2vpnEvpnMacIpSchema):

    """ Parser for show l2vpn evpn mac ip
                   show l2vpn evpn mac ip address <ipv4_addr>
                   show l2vpn evpn mac ip address <ipv6_addr>
                   show l2vpn evpn mac ip bridge-domain <bd_id>
                   show l2vpn evpn mac ip bridge-domain <bd_id> address <ipv4_addr>
                   show l2vpn evpn mac ip bridge-domain <bd_id> address <ipv6_addr>
                   show l2vpn evpn mac ip bridge-domain <bd_id> duplicate
                   show l2vpn evpn mac ip bridge-domain <bd_id> local
                   show l2vpn evpn mac ip bridge-domain <bd_id> mac <mac_addr>
                   show l2vpn evpn mac ip bridge-domain <bd_id> mac <mac_addr> address <ipv4_addr>
                   show l2vpn evpn mac ip bridge-domain <bd_id> mac <mac_addr> address <ipv6_addr>
                   show l2vpn evpn mac ip bridge-domain <bd_id> remote
                   show l2vpn evpn mac ip duplicate
                   show l2vpn evpn mac ip evi <evi_id>
                   show l2vpn evpn mac ip evi <evi_id> address <ipv4_addr>
                   show l2vpn evpn mac ip evi <evi_id> address <ipv6_addr>
                   show l2vpn evpn mac ip evi <evi_id> duplicate
                   show l2vpn evpn mac ip evi <evi_id> local
                   show l2vpn evpn mac ip evi <evi_id> mac <mac_addr>
                   show l2vpn evpn mac ip evi <evi_id> mac <mac_addr> address <ipv4_addr>
                   show l2vpn evpn mac ip evi <evi_id> mac <mac_addr> address <ipv6_addr>
                   show l2vpn evpn mac ip evi <evi_id> remote
                   show l2vpn evpn mac ip local
                   show l2vpn evpn mac ip mac <mac_addr>
                   show l2vpn evpn mac ip mac <mac_addr> address <ipv4_addr>
                   show l2vpn evpn mac ip mac <mac_addr> address <ipv6_addr>
                   show l2vpn evpn mac ip remote
    """

    cli_command = ['show l2vpn evpn mac ip', # 0
                   'show l2vpn evpn mac ip address {ip_addr}', # 1
                   'show l2vpn evpn mac ip {mac_ip_type}', # 2
                   'show l2vpn evpn mac ip mac {mac_addr}', # 3
                   'show l2vpn evpn mac ip mac {mac_addr} address {ip_addr}', # 4
                   'show l2vpn evpn mac ip bridge-domain {bd_id}', # 5
                   'show l2vpn evpn mac ip bridge-domain {bd_id} address {ip_addr}', # 6
                   'show l2vpn evpn mac ip bridge-domain {bd_id} {mac_ip_type}', # 7
                   'show l2vpn evpn mac ip bridge-domain {bd_id} mac {mac_addr}', # 8
                   'show l2vpn evpn mac ip bridge-domain {bd_id} mac {mac_addr} address {ip_addr}', # 9
                   'show l2vpn evpn mac ip evi {evi_id}', # 10
                   'show l2vpn evpn mac ip evi {evi_id} address {ip_addr}', # 11
                   'show l2vpn evpn mac ip evi {evi_id} {mac_ip_type}', # 12
                   'show l2vpn evpn mac ip evi {evi_id} mac {mac_addr}', # 13
                   'show l2vpn evpn mac ip evi {evi_id} mac {mac_addr} address {ip_addr}', # 14
    ]

    def cli(self, output=None, mac_addr=None, mac_ip_type=None, bd_id=None, evi_id=None, ip_addr=None):
        if not output:
            # Only these CLI options for mac_ip_type are supported.
            if mac_ip_type and mac_ip_type != 'local' and mac_ip_type != 'remote' and mac_ip_type != 'duplicate':
                raise Exception("Unsupported mac_ip_type {}".format(mac_ip_type))
            if bd_id:
                if mac_addr:
                    if ip_addr:
                        cli_cmd = self.cli_command[9].format(bd_id=bd_id, mac_addr=mac_addr, ip_addr=ip_addr)
                    else:
                        cli_cmd = self.cli_command[8].format(bd_id=bd_id, mac_addr=mac_addr)
                elif mac_ip_type:
                    cli_cmd = self.cli_command[7].format(bd_id=bd_id, mac_ip_type=mac_ip_type)
                else:
                    if ip_addr:
                        cli_cmd = self.cli_command[6].format(bd_id=bd_id, ip_addr=ip_addr)
                    else:
                        cli_cmd = self.cli_command[5].format(bd_id=bd_id)
            elif evi_id:
                if mac_addr:
                    if ip_addr:
                        cli_cmd = self.cli_command[14].format(evi_id=evi_id, mac_addr=mac_addr, ip_addr=ip_addr)
                    else:
                        cli_cmd = self.cli_command[13].format(evi_id=evi_id, mac_addr=mac_addr)
                elif mac_ip_type:
                    cli_cmd = self.cli_command[12].format(evi_id=evi_id, mac_ip_type=mac_ip_type)
                else:
                    if ip_addr:
                        cli_cmd = self.cli_command[11].format(evi_id=evi_id, ip_addr=ip_addr)
                    else:
                        cli_cmd = self.cli_command[10].format(evi_id=evi_id)
            else:
                if mac_addr:
                    if ip_addr:
                        cli_cmd = self.cli_command[4].format(mac_addr=mac_addr, ip_addr=ip_addr)
                    else:
                        cli_cmd = self.cli_command[3].format(mac_addr=mac_addr)
                elif mac_ip_type:
                    cli_cmd = self.cli_command[2].format(mac_ip_type=mac_ip_type)
                else:
                    if ip_addr:
                        cli_cmd = self.cli_command[1].format(ip_addr=ip_addr)
                    else:
                        cli_cmd = self.cli_command[0]

            cli_output = self.device.execute(cli_cmd)
        else:
            cli_output = output

        if not cli_output:
            return {}

        # Case 1 - BD header
        #
        # IP Address                EVI   BD    MAC Address    Next Hop(s)
        # ------------------------- ----- ----- -------------- -------------------------
        # 192.168.11.11             1     11    aabb.0011.0001 Et1/0:11
        # 2001:11::20               1     11    aabb.0011.0021 Duplicate
        # 2001:12::11               2     12    aabb.0012.0002 2.2.2.1
        #
        # Case 2 - VLAN header
        #
        # IP Address                EVI   VLAN  MAC Address    Next Hop(s)
        # ------------------------- ----- ----- -------------- -------------------------
        # 192.168.11.12             1     11    aabb.0011.0002 2.2.2.1
        # 2001:11::12               1     11    aabb.0011.0002 2.2.2.1
        #
        # Case 3 - Multiple Next Hops
        #
        # IP Address                EVI   BD    MAC Address    Next Hop(s)
        # ------------------------- ----- ----- -------------- -------------------------
        # 192.168.12.3              2     12    aabb.cc82.2800 Et1/0:12
        #                                                      3.3.3.1
        #                                                      5.5.5.1
        # 2001:12::3                2     12    aabb.cc82.2800 Et1/0:12
        #                                                      3.3.3.1
        #                                                      5.5.5.1
        #
        # Case 4 - Duplicate IP
        #
        # IP Address                EVI   BD    MAC Address    Next Hop(s)
        # ------------------------- ----- ----- -------------- -------------------------
        # 192.168.11.21             1     11    Duplicate      Et1/0:11
        p1 = re.compile(r'^IP Address\s+EVI\s+(BD|VLAN)\s+MAC Address\s+Next Hop\(s\)$')
        p2 = re.compile(r'^(?P<ip>[0-9a-fA-F\.:]+)\s+(?P<evi>\d+)\s+(?P<bd_id>\d+)\s+(?P<mac>[\d\w\.]+)\s+(?P<next_hop>[\w\d\s\.:()/]+)$')
        p3 = re.compile(r'^(?P<next_hop>[\w\d\s\.:()/]+)$')

        parser_dict = {}

        header_validated = False
        for line in cli_output.splitlines():
            line = line.strip()
            if not line:
                continue

            # Sanity check the header appears in the expected order.
            m = p1.match(line)
            if m:
                header_validated = True
                continue

            # 192.168.12.3              2     12    aabb.cc82.2800 Et1/0:12
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ip_vals = parser_dict.setdefault(group['ip'], {})
                ip_vals.update({
                    'evi': int(group['evi']),
                    'bd_id': int(group['bd_id']),
                    'mac_addr': group['mac'],
                })
                next_hops = ip_vals.setdefault('next_hops', [])
                next_hops.append(group['next_hop'])
                continue

            #                                                      3.3.3.1
            m = p3.match(line)
            if m:
                group = m.groupdict()
                next_hops.append(group['next_hop'])
                continue

        if not header_validated:
            return {}

        return parser_dict

# ===========================================
# Schema for 'show l2vpn evpn mac ip detail'
# ===========================================
class ShowL2vpnEvpnMacIpDetailSchema(MetaParser):

    """ Schema for show l2vpn evpn mac ip address <ipv4_addr> detail
                   show l2vpn evpn mac ip address <ipv6_addr> detail
                   show l2vpn evpn mac ip bridge-domain <bd_id> address <ipv4_addr>  detail
                   show l2vpn evpn mac ip bridge-domain <bd_id> address <ipv6_addr> detail
                   show l2vpn evpn mac ip bridge-domain <bd_id> detail
                   show l2vpn evpn mac ip bridge-domain <bd_id> duplicate detail
                   show l2vpn evpn mac ip bridge-domain <bd_id> local detail
                   show l2vpn evpn mac ip bridge-domain <bd_id> mac <mac_addr> address <ipv4_addr> detail
                   show l2vpn evpn mac ip bridge-domain <bd_id> mac <mac_addr> address <ipv6_addr> detail
                   show l2vpn evpn mac ip bridge-domain <bd_id> mac <mac_addr> detail
                   show l2vpn evpn mac ip bridge-domain <bd_id> remote detail
                   show l2vpn evpn mac ip detail
                   show l2vpn evpn mac ip duplicate detail
                   show l2vpn evpn mac ip evi <evi_id> address <ipv4_addr> detail
                   show l2vpn evpn mac ip evi <evi_id> address <ipv6_addr> detail
                   show l2vpn evpn mac ip evi <evi_id> detail
                   show l2vpn evpn mac ip evi <evi_id> duplicate detail
                   show l2vpn evpn mac ip evi <evi_id> local detail
                   show l2vpn evpn mac ip evi <evi_id> mac <mac_addr> address <ipv4_addr> detail
                   show l2vpn evpn mac ip evi <evi_id> mac <mac_addr> address <ipv6_addr> detail
                   show l2vpn evpn mac ip evi <evi_id> mac <mac_addr> detail
                   show l2vpn evpn mac ip evi <evi_id> remote detail
                   show l2vpn evpn mac ip local detail
                   show l2vpn evpn mac ip mac <mac_addr> address <ipv4_addr> detail
                   show l2vpn evpn mac ip mac <mac_addr> address <ipv6_addr> detail
                   show l2vpn evpn mac ip mac <mac_addr> detail
                   show l2vpn evpn mac ip remote detail
    """

    schema = {
        Any(): { # IP Address
            'stale': bool,
            'evi': int,
            'bd_id': int,
            'mac_addr': str,
            'esi': str,
            'etag': int,
            'next_hops': list,
            Optional('local_addr'): str,
            'seq_num': int,
            'ip_dup_detection': {
                'status': str,
                Optional('moves_count'): int,
                Optional('moves_limit'): int,
                Optional('expiry_time'): str,
            },
            Optional('last_local_mac_sent'): str,
            Optional('last_local_mac_learned'): str,
            Optional('last_remote_mac_received'): str,
            'label2_included': bool,
        },
    }

# ===========================================
# Parser for 'show l2vpn evpn mac ip detail'
# ===========================================
class ShowL2vpnEvpnMacIpDetail(ShowL2vpnEvpnMacIpDetailSchema):

    """ Parser for show l2vpn evpn mac ip address <ipv4_addr> detail
                   show l2vpn evpn mac ip address <ipv6_addr> detail
                   show l2vpn evpn mac ip bridge-domain <bd_id> address <ipv4_addr>  detail
                   show l2vpn evpn mac ip bridge-domain <bd_id> address <ipv6_addr> detail
                   show l2vpn evpn mac ip bridge-domain <bd_id> detail
                   show l2vpn evpn mac ip bridge-domain <bd_id> duplicate detail
                   show l2vpn evpn mac ip bridge-domain <bd_id> local detail
                   show l2vpn evpn mac ip bridge-domain <bd_id> mac <mac_addr> address <ipv4_addr> detail
                   show l2vpn evpn mac ip bridge-domain <bd_id> mac <mac_addr> address <ipv6_addr> detail
                   show l2vpn evpn mac ip bridge-domain <bd_id> mac <mac_addr> detail
                   show l2vpn evpn mac ip bridge-domain <bd_id> remote detail
                   show l2vpn evpn mac ip detail
                   show l2vpn evpn mac ip duplicate detail
                   show l2vpn evpn mac ip evi <evi_id> address <ipv4_addr> detail
                   show l2vpn evpn mac ip evi <evi_id> address <ipv6_addr> detail
                   show l2vpn evpn mac ip evi <evi_id> detail
                   show l2vpn evpn mac ip evi <evi_id> duplicate detail
                   show l2vpn evpn mac ip evi <evi_id> local detail
                   show l2vpn evpn mac ip evi <evi_id> mac <mac_addr> address <ipv4_addr> detail
                   show l2vpn evpn mac ip evi <evi_id> mac <mac_addr> address <ipv6_addr> detail
                   show l2vpn evpn mac ip evi <evi_id> mac <mac_addr> detail
                   show l2vpn evpn mac ip evi <evi_id> remote detail
                   show l2vpn evpn mac ip local detail
                   show l2vpn evpn mac ip mac <mac_addr> address <ipv4_addr> detail
                   show l2vpn evpn mac ip mac <mac_addr> address <ipv6_addr> detail
                   show l2vpn evpn mac ip mac <mac_addr> detail
                   show l2vpn evpn mac ip remote detail
    """

    cli_command = ['show l2vpn evpn mac ip detail', # 0
                   'show l2vpn evpn mac ip address {ip_addr} detail', # 1
                   'show l2vpn evpn mac ip {mac_ip_type} detail', # 2
                   'show l2vpn evpn mac ip mac {mac_addr} detail', # 3
                   'show l2vpn evpn mac ip mac {mac_addr} address {ip_addr} detail', # 4
                   'show l2vpn evpn mac ip bridge-domain {bd_id} detail', # 5
                   'show l2vpn evpn mac ip bridge-domain {bd_id} address {ip_addr}  detail', # 6
                   'show l2vpn evpn mac ip bridge-domain {bd_id} {mac_ip_type} detail', # 7
                   'show l2vpn evpn mac ip bridge-domain {bd_id} mac {mac_addr} detail', # 8
                   'show l2vpn evpn mac ip bridge-domain {bd_id} mac {mac_addr} address {ip_addr} detail', # 9
                   'show l2vpn evpn mac ip evi {evi_id} detail', # 10
                   'show l2vpn evpn mac ip evi {evi_id} address {ip_addr} detail', # 11
                   'show l2vpn evpn mac ip evi {evi_id} {mac_ip_type} detail',  # 12
                   'show l2vpn evpn mac ip evi {evi_id} mac {mac_addr} detail', # 13
                   'show l2vpn evpn mac ip evi {evi_id} mac {mac_addr} address {ip_addr} detail', # 14
    ]

    def cli(self, output=None, mac_addr=None, mac_ip_type=None, bd_id=None, evi_id=None, ip_addr=None):
        if not output:
            # Only these CLI options for mac_ip_type are supported.
            if mac_ip_type and mac_ip_type != 'local' and mac_ip_type != 'remote' and mac_ip_type != 'duplicate':
                raise Exception("Unsupported mac_ip_type {}".format(mac_ip_type))
            if bd_id:
                if mac_addr:
                    if ip_addr:
                        cli_cmd = self.cli_command[9].format(bd_id=bd_id, mac_addr=mac_addr, ip_addr=ip_addr)
                    else:
                        cli_cmd = self.cli_command[8].format(bd_id=bd_id, mac_addr=mac_addr)
                elif mac_ip_type:
                    cli_cmd = self.cli_command[7].format(bd_id=bd_id, mac_ip_type=mac_ip_type)
                else:
                    if ip_addr:
                        cli_cmd = self.cli_command[6].format(bd_id=bd_id, ip_addr=ip_addr)
                    else:
                        cli_cmd = self.cli_command[5].format(bd_id=bd_id)
            elif evi_id:
                if mac_addr:
                    if ip_addr:
                        cli_cmd = self.cli_command[14].format(evi_id=evi_id, mac_addr=mac_addr, ip_addr=ip_addr)
                    else:
                        cli_cmd = self.cli_command[13].format(evi_id=evi_id, mac_addr=mac_addr)
                elif mac_ip_type:
                    cli_cmd = self.cli_command[12].format(evi_id=evi_id, mac_ip_type=mac_ip_type)
                else:
                    if ip_addr:
                        cli_cmd = self.cli_command[11].format(evi_id=evi_id, ip_addr=ip_addr)
                    else:
                        cli_cmd = self.cli_command[10].format(evi_id=evi_id)
            else:
                if mac_addr:
                    if ip_addr:
                        cli_cmd = self.cli_command[4].format(mac_addr=mac_addr, ip_addr=ip_addr)
                    else:
                        cli_cmd = self.cli_command[3].format(mac_addr=mac_addr)
                elif mac_ip_type:
                    cli_cmd = self.cli_command[2].format(mac_ip_type=mac_ip_type)
                else:
                    if ip_addr:
                        cli_cmd = self.cli_command[1].format(ip_addr=ip_addr)
                    else:
                        cli_cmd = self.cli_command[0]

            cli_output = self.device.execute(cli_cmd)
        else:
            cli_output = output

        if not cli_output:
            return {}

        # IP Address:                192.168.11.21
        # IP Address:                2001:12::3
        # IP Address:                FE80::A8BB:FF:FE12:2 (stale)
        p1 = re.compile(r'^IP Address:\s+(?P<ip>[0-9a-fA-F\.:]+)(\s+(?P<ip_status>[\w\s\(\)]+))?$')

        # EVPN Instance:             1
        p2 = re.compile(r'^EVPN Instance:\s+(?P<evi>\d+)$')

        # Bridge Domain:             11
        # Vlan:                      11
        p3 = re.compile(r'^(Bridge Domain|Vlan):\s+(?P<bd_id>\d+)$')

        # MAC Address:               aabb.0012.0002
        p4 = re.compile(r'^MAC Address:\s+(?P<mac>[0-9a-fA-F\.]+)$')

        # Ethernet Segment:          03AA.BB00.0000.0200.0001
        p5 = re.compile(r'^Ethernet Segment:\s+(?P<esi>[0-9a-fA-F\.]+)$')

        # Ethernet Tag ID:           0
        p6 = re.compile(r'^Ethernet Tag ID:\s+(?P<etag>\d+)$')

        # Next Hop(s):               L:17 Ethernet1/0 service instance 12
        #                            L:17 3.3.3.1
        #                            L:17 5.5.5.1
        p7 = re.compile(r'^Next Hop\(s\):\s+(?P<next_hop>[\w\d\s\.:()/]+)$')
        p8 = re.compile(r'^(?P<next_hop>[\w\d\s\.:()/]+)$')

        # Local Address:             4.4.4.1
        p9 = re.compile(r'^Local Address:\s+(?P<local_addr>[\d\.]+)$')

        # Sequence Number:           0
        p10 = re.compile(r'^Sequence Number:\s+(?P<seq_num>\d+)$')

        # IP Duplication Detection:  Timer not running
        # IP Duplication Detection:  IP moves 4, limit 5
        #                            Timer expires in 09:19:15
        # IP Duplication Detection:  Duplicate IP address detected
        p11 = re.compile(r'^IP Duplication Detection:\s+(?P<ip_dup_status>[\w\d\s,]+)$')
        p12 = re.compile(r'^IP moves (?P<moves_count>\d+), limit (?P<moves_limit>\d+)$')
        p13 = re.compile(r'^\s+Timer expires in (?P<expiry_time>[\d:]+)$')

        # Last Local MAC sent:       aabb.0011.0022
        p14 = re.compile(r'^Last Local MAC sent:\s+(?P<last_local_mac_sent>[0-9a-fA-F\.]+)$')

        # Last Local MAC learned:    aabb.0011.0022
        p15 = re.compile(r'^Last Local MAC learned:\s+(?P<last_local_mac_learned>[0-9a-fA-F\.]+)$')

        # Last Remote MAC received:  aabb.0011.0022
        p16 = re.compile(r'^Last Remote MAC received:\s+(?P<last_local_mac_sent>[0-9a-fA-F\.]+)$')

        # Label2 included:           No
        p17 = re.compile(r'^Label2 included:\s+(?P<label2_included>(Yes|No))$')

        parser_dict = {}

        for line in cli_output.splitlines():
            line = line.strip()
            if not line:
                continue

            # IP Address:                192.168.11.21
            # IP Address:                2001:12::3
            # IP Address:                FE80::A8BB:FF:FE12:2 (stale)
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ip_vals = parser_dict.setdefault(group['ip'], {})
                stale = False
                if group['ip_status']:
                    stale = 'stale' in group['ip_status']
                ip_vals.update({
                    'stale': stale,
                })
                continue

            # EVPN Instance:             1
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ip_vals.update({'evi': int(group['evi'])})
                continue

            # Bridge Domain:             11
            # Vlan:                      11
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ip_vals.update({'bd_id': int(group['bd_id'])})
                continue

            # MAC Address:               aabb.0012.0002
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ip_vals.update({'mac_addr': group['mac']})
                continue

            # Ethernet Segment:          03AA.BB00.0000.0200.0001
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ip_vals.update({'esi': group['esi']})
                continue

            # Ethernet Tag ID:           0
            m = p6.match(line)
            if m:
                group = m.groupdict()
                ip_vals.update({'etag': int(group['etag'])})
                continue

            # Next Hop(s):               L:17 Ethernet1/0 service instance 12
            m = p7.match(line)
            if m:
                group = m.groupdict()
                next_hops = ip_vals.setdefault('next_hops', [])
                next_hops.append(group['next_hop'])
                continue

            # Local Address:             4.4.4.1
            m = p9.match(line)
            if m:
                group = m.groupdict()
                ip_vals.update({'local_addr': group['local_addr']})
                continue

            # Sequence Number:           0
            m = p10.match(line)
            if m:
                group = m.groupdict()
                ip_vals.update({'seq_num': int(group['seq_num'])})
                continue

            # IP Duplication Detection:  Timer not running
            # IP Duplication Detection:  IP moves 4, limit 5
            # IP Duplication Detection:  Duplicate IP address detected
            m = p11.match(line)
            if m:
                group = m.groupdict()
                ip_dup_status = group['ip_dup_status']
                ip_dup_vals = ip_vals.setdefault('ip_dup_detection', {})
                ip_dup_vals.update({'status': ip_dup_status})

                m = p12.match(ip_dup_status)
                if m:
                    ip_dup_vals.update({
                        'moves_count': int(group['moves_count']),
                        'moves_limit': int(group['moves_limit']),
                    })
                continue

            #                            Timer expires in 09:19:15
            m = p13.match(line)
            if m:
                group = m.groupdict()
                ip_dup_vals.update({'expiry_time': group['expiry_time']})
                continue

            # Last Local MAC sent:       aabb.0011.0022
            m = p14.match(line)
            if m:
                group = m.groupdict()
                ip_vals.update({'last_local_mac_sent': group['last_local_mac_sent']})
                continue

            # Last Local MAC learned:    aabb.0011.0022
            m = p15.match(line)
            if m:
                group = m.groupdict()
                ip_vals.update({'last_local_mac_learned': group['last_local_mac_learned']})
                continue

            # Last Remote MAC received:  aabb.0011.0022
            m = p16.match(line)
            if m:
                group = m.groupdict()
                ip_vals.update({'last_remote_mac_received': group['last_remote_mac_received']})
                continue

            # MAC only present:           Yes
            m = p17.match(line)
            if m:
                group = m.groupdict()
                label2_included = True if group['label2_included'] == 'Yes' else False
                ip_vals.update({'label2_included': label2_included})
                continue

            # Check this pattern last as it can match other fields.
            #                            L:17 5.5.5.1
            m = p8.match(line)
            if m:
                group = m.groupdict()
                next_hops.append(group['next_hop'])
                continue

        return parser_dict

# ============================================
# Schema for 'show l2vpn evpn mac ip summary'
# ============================================
class ShowL2vpnEvpnMacIpSummarySchema(MetaParser):

    """ Schema for show l2vpn evpn mac ip bridge-domain <bd_id> duplicate summary
                   show l2vpn evpn mac ip bridge-domain <bd_id> local summary
                   show l2vpn evpn mac ip bridge-domain <bd_id> mac <mac_addr> summary
                   show l2vpn evpn mac ip bridge-domain <bd_id> remote summary
                   show l2vpn evpn mac ip bridge-domain <bd_id> summary
                   show l2vpn evpn mac ip duplicate summary
                   show l2vpn evpn mac ip evi <evi_id> duplicate summary
                   show l2vpn evpn mac ip evi <evi_id> local summary
                   show l2vpn evpn mac ip evi <evi_id> mac <mac_addr> summary
                   show l2vpn evpn mac ip evi <evi_id> remote summary
                   show l2vpn evpn mac ip evi <evi_id> summary
                   show l2vpn evpn mac ip local summary
                   show l2vpn evpn mac ip mac <mac_addr> summary
                   show l2vpn evpn mac ip remote summary
                   show l2vpn evpn mac ip summary
    """

    schema = {
        'entry': {
            Any(): { # EVI
                Any(): { # BD
                    Any(): { # Ether Tag
                        Optional('remote_count'): int,
                        Optional('local_count'): int,
                        Optional('dup_count'): int,
                    },
                },
            },
        },
        Optional('total'): {
            Optional('remote_count'): int,
            Optional('local_count'): int,
            Optional('dup_count'): int,
        }
    }

# ============================================
# Parser for 'show l2vpn evpn mac ip summary'
# ============================================
class ShowL2vpnEvpnMacIpSummary(ShowL2vpnEvpnMacIpSummarySchema):

    """ Parser for show l2vpn evpn mac ip bridge-domain <bd_id> duplicate summary
                   show l2vpn evpn mac ip bridge-domain <bd_id> local summary
                   show l2vpn evpn mac ip bridge-domain <bd_id> mac <mac_addr> summary
                   show l2vpn evpn mac ip bridge-domain <bd_id> remote summary
                   show l2vpn evpn mac ip bridge-domain <bd_id> summary
                   show l2vpn evpn mac ip duplicate summary
                   show l2vpn evpn mac ip evi <evi_id> duplicate summary
                   show l2vpn evpn mac ip evi <evi_id> local summary
                   show l2vpn evpn mac ip evi <evi_id> mac <mac_addr> summary
                   show l2vpn evpn mac ip evi <evi_id> remote summary
                   show l2vpn evpn mac ip evi <evi_id> summary
                   show l2vpn evpn mac ip local summary
                   show l2vpn evpn mac ip mac <mac_addr> summary
                   show l2vpn evpn mac ip remote summary
                   show l2vpn evpn mac ip summary
    """

    cli_command = ['show l2vpn evpn mac ip summary', # 0
                   'show l2vpn evpn mac ip {mac_ip_type} summary', # 1
                   'show l2vpn evpn mac ip mac {mac_addr} summary', # 2
                   'show l2vpn evpn mac ip bridge-domain {bd_id} summary', # 3
                   'show l2vpn evpn mac ip bridge-domain {bd_id} {mac_ip_type} summary', # 4
                   'show l2vpn evpn mac ip bridge-domain {bd_id} mac {mac_addr} summary', # 5
                   'show l2vpn evpn mac ip evi {evi_id} summary', # 6
                   'show l2vpn evpn mac ip evi {evi_id} {mac_ip_type} summary', # 7
                   'show l2vpn evpn mac ip evi {evi_id} mac {mac_addr} summary', # 8
    ]

    def cli(self, output=None, mac_ip_type=None, bd_id=None, evi_id=None, mac_addr=None):
        if not output:
            # Only these CLI options for mac_ip_type are supported.
            if mac_ip_type and mac_ip_type != 'local' and mac_ip_type != 'remote' and mac_ip_type != 'duplicate':
                raise Exception("Unsupported mac_ip_type {}".format(mac_ip_type))
            if bd_id:
                if mac_ip_type:
                    cli_cmd = self.cli_command[4].format(bd_id=bd_id, mac_ip_type=mac_ip_type)
                else:
                    if mac_addr:
                        cli_cmd = self.cli_command[5].format(bd_id=bd_id, mac_addr=mac_addr)
                    else:
                        cli_cmd = self.cli_command[3].format(bd_id=bd_id)
            elif evi_id:
                if mac_ip_type:
                    cli_cmd = self.cli_command[7].format(evi_id=evi_id, mac_ip_type=mac_ip_type)
                else:
                    if mac_addr:
                        cli_cmd = self.cli_command[8].format(evi_id=evi_id, mac_addr=mac_addr)
                    else:
                        cli_cmd = self.cli_command[6].format(evi_id=evi_id)
            else:
                if mac_ip_type:
                    cli_cmd = self.cli_command[1].format(mac_ip_type=mac_ip_type)
                else:
                    if mac_addr:
                        cli_cmd = self.cli_command[2].format(mac_addr=mac_addr)
                    else:
                        cli_cmd = self.cli_command[0]

            cli_output = self.device.execute(cli_cmd)
        else:
            cli_output = output

        if not cli_output:
            return {}

        # PE1#show l2vpn evpn mac ip bridge-domain 11 duplicate summary
        # EVI   BD    Ether Tag  Dup IP     
        # ----- ----- ---------- ---------- 
        # 1     11    0          1         
        #
        # PE1#show l2vpn evpn mac ip bridge-domain 11 summary
        # EVI   BD    Ether Tag  Remote IP  Local IP   Dup IP
        # ----- ----- ---------- ---------- ---------- ----------
        # 1     11    0          4          5          1
        #
        # PE1#show l2vpn evpn mac ip evi 1 remote summary
        # EVI   BD    Ether Tag  Remote IP  
        # ----- ----- ---------- ---------- 
        # 1     11    0          4         
        #
        # Total                  4
        #
        # PE1#show l2vpn evpn mac ip summary
        # EVI   BD    Ether Tag  Remote IP  Local IP   Dup IP
        # ----- ----- ---------- ---------- ---------- ----------
        # 1     11    0          4          5          1
        # 2     12    0          2          2          0
        #
        # Total                  6          7          1
        #
        # VTEP1#show l2vpn evpn mac ip summary
        # EVI   VLAN  Ether Tag  Remote IP  Local IP   Dup IP
        # ----- ----- ---------- ---------- ---------- ----------
        # 1     11    0          2          0          0
        # 2     12    0          0          0          0
        #
        # Total                  2          0          0
        p1 = re.compile(r'^EVI\s+(BD|VLAN)\s+Ether Tag\s+Remote IP\s+Local IP\s+Dup IP$')
        p2 = re.compile(r'^EVI\s+(BD|VLAN)\s+Ether Tag\s+Remote IP$')
        p3 = re.compile(r'^EVI\s+(BD|VLAN)\s+Ether Tag\s+Local IP$')
        p4 = re.compile(r'^EVI\s+(BD|VLAN)\s+Ether Tag\s+Dup IP$')
        p5 = re.compile(r'^(?P<evi>\d+)\s+(?P<bd_id>\d+)\s+(?P<etag>\d+)\s+(?P<remote_count>\d+)\s+(?P<local_count>\d+)\s+(?P<dup_count>\d+)$')
        p6 = re.compile(r'^(?P<evi>\d+)\s+(?P<bd_id>\d+)\s+(?P<etag>\d+)\s+(?P<count>\d+)$')
        p7 = re.compile(r'^Total\s+(?P<remote_count>\d+)\s+(?P<local_count>\d+)\s+(?P<dup_count>\d+)$')
        p8 = re.compile(r'^Total\s+(?P<count>\d+)$')

        parser_dict = {}

        table_mac_types = None
        for line in cli_output.splitlines():
            line = line.strip()
            if not line:
                continue

            # EVI   BD    Ether Tag  Remote MAC Local MAC  Dup MAC
            m = p1.match(line)
            if m:
                table_mac_types = 'All'
                continue

            # EVI   BD    Ether Tag  Remote MAC 
            m = p2.match(line)
            if m:
                table_mac_types = 'Remote'
                continue

            # EVI   BD    Ether Tag  Local MAC  
            m = p3.match(line)
            if m:
                table_mac_types = 'Local'
                continue

            # EVI   BD    Ether Tag  Dup MAC    
            m = p4.match(line)
            if m:
                table_mac_types = 'Dup'
                continue

            # 1     11    0          4          5          1
            m = p5.match(line)
            if m:
                group = m.groupdict()
                entry_vals = parser_dict.setdefault('entry', {})
                evi_vals = entry_vals.setdefault(int(group['evi']), {})
                bd_vals = evi_vals.setdefault(int(group['bd_id']), {})
                etag_vals = bd_vals.setdefault(int(group['etag']), {})
                if table_mac_types == 'All':
                    etag_vals.update({
                        'remote_count': int(group['remote_count']),
                        'local_count': int(group['local_count']),
                        'dup_count': int(group['dup_count']),
                    })
                continue

            # 1     11    0          1         
            m = p6.match(line)
            if m:
                group = m.groupdict()
                entry_vals = parser_dict.setdefault('entry', {})
                evi_vals = entry_vals.setdefault(int(group['evi']), {})
                bd_vals = evi_vals.setdefault(int(group['bd_id']), {})
                etag_vals = bd_vals.setdefault(int(group['etag']), {})
                if table_mac_types == 'Remote':
                    etag_vals.update({
                        'remote_count': int(group['count']),
                    })
                elif table_mac_types == 'Local':
                    etag_vals.update({
                        'local_count': int(group['count']),
                    })
                elif table_mac_types == 'Dup':
                    etag_vals.update({
                        'dup_count': int(group['count']),
                    })
                continue

            # Total                  6          7          1
            m = p7.match(line)
            if m:
                group = m.groupdict()
                total_vals = parser_dict.setdefault('total', {})
                if table_mac_types == 'All':
                    total_vals.update({
                        'remote_count': int(group['remote_count']),
                        'local_count': int(group['local_count']),
                        'dup_count': int(group['dup_count']),
                    })
                continue

            # Total                  4
            m = p8.match(line)
            if m:
                group = m.groupdict()
                total_vals = parser_dict.setdefault('total', {})
                if table_mac_types == 'Remote':
                    total_vals.update({
                        'remote_count': int(group['count']),
                    })
                elif table_mac_types == 'Local':
                    total_vals.update({
                        'local_count': int(group['count']),
                    })
                elif table_mac_types == 'Dup':
                    total_vals.update({
                        'dup_count': int(group['count']),
                    })
                continue

        # Header must be invalid if this was never set.
        if not table_mac_types:
            return {}

        return parser_dict
