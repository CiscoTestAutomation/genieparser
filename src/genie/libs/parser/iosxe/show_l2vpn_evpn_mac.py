""" show_l2vpn_evpn_mac.py

IOSXE parsers for the following show commands:

    * show l2vpn evpn mac
    * show l2vpn evpn mac address <mac_addr>
    * show l2vpn evpn mac address <mac_addr> detail
    * show l2vpn evpn mac bridge-domain <bd_id>
    * show l2vpn evpn mac bridge-domain <bd_id> address <mac_addr>
    * show l2vpn evpn mac bridge-domain <bd_id> address <mac_addr> detail
    * show l2vpn evpn mac bridge-domain <bd_id> detail
    * show l2vpn evpn mac bridge-domain <bd_id> duplicate
    * show l2vpn evpn mac bridge-domain <bd_id> duplicate detail
    * show l2vpn evpn mac bridge-domain <bd_id> duplicate summary
    * show l2vpn evpn mac bridge-domain <bd_id> local
    * show l2vpn evpn mac bridge-domain <bd_id> local detail
    * show l2vpn evpn mac bridge-domain <bd_id> local summary
    * show l2vpn evpn mac bridge-domain <bd_id> remote
    * show l2vpn evpn mac bridge-domain <bd_id> remote detail
    * show l2vpn evpn mac bridge-domain <bd_id> remote summary
    * show l2vpn evpn mac bridge-domain <bd_id> summary
    * show l2vpn evpn mac detail
    * show l2vpn evpn mac duplicate
    * show l2vpn evpn mac duplicate detail
    * show l2vpn evpn mac duplicate summary
    * show l2vpn evpn mac evi <evi_id>
    * show l2vpn evpn mac evi <evi_id> address <mac_addr>
    * show l2vpn evpn mac evi <evi_id> address <mac_addr> detail
    * show l2vpn evpn mac evi <evi_id> detail
    * show l2vpn evpn mac evi <evi_id> duplicate
    * show l2vpn evpn mac evi <evi_id> duplicate detail
    * show l2vpn evpn mac evi <evi_id> duplicate summary
    * show l2vpn evpn mac evi <evi_id> local
    * show l2vpn evpn mac evi <evi_id> local detail
    * show l2vpn evpn mac evi <evi_id> local summary
    * show l2vpn evpn mac evi <evi_id> remote
    * show l2vpn evpn mac evi <evi_id> remote detail
    * show l2vpn evpn mac evi <evi_id> remote summary
    * show l2vpn evpn mac evi <evi_id> summary
    * show l2vpn evpn mac local
    * show l2vpn evpn mac local detail
    * show l2vpn evpn mac local summary
    * show l2vpn evpn mac remote
    * show l2vpn evpn mac remote detail
    * show l2vpn evpn mac remote summary
    * show l2vpn evpn mac summary

Copyright (c) 2021 by Cisco Systems, Inc.
All rights reserved.
"""

import re

# Genie
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, \
                                               Optional

# =================================
# Schema for 'show l2vpn evpn mac'
# =================================
class ShowL2vpnEvpnMacSchema(MetaParser):

    """ Schema for show l2vpn evpn mac
                   show l2vpn evpn mac address <mac_addr>
                   show l2vpn evpn mac bridge-domain <bd_id>
                   show l2vpn evpn mac bridge-domain <bd_id> address <mac_addr>
                   show l2vpn evpn mac bridge-domain <bd_id> duplicate
                   show l2vpn evpn mac bridge-domain <bd_id> local
                   show l2vpn evpn mac bridge-domain <bd_id> remote
                   show l2vpn evpn mac duplicate
                   show l2vpn evpn mac evi <evi_id>
                   show l2vpn evpn mac evi <evi_id> address <mac_addr>
                   show l2vpn evpn mac evi <evi_id> duplicate
                   show l2vpn evpn mac evi <evi_id> local
                   show l2vpn evpn mac evi <evi_id> remote
                   show l2vpn evpn mac local
                   show l2vpn evpn mac remote
    """

    schema = {
        Any(): { # MAC Address
            'evi': int,
            'bd_id': int,
            'esi': str,
            'etag': int,
            'next_hops': list,
        },
    }

# =================================
# Parser for 'show l2vpn evpn mac'
# =================================
class ShowL2vpnEvpnMac(ShowL2vpnEvpnMacSchema):

    """ Parser for show l2vpn evpn mac
                   show l2vpn evpn mac address <mac_addr>
                   show l2vpn evpn mac bridge-domain <bd_id>
                   show l2vpn evpn mac bridge-domain <bd_id> address <mac_addr>
                   show l2vpn evpn mac bridge-domain <bd_id> duplicate
                   show l2vpn evpn mac bridge-domain <bd_id> local
                   show l2vpn evpn mac bridge-domain <bd_id> remote
                   show l2vpn evpn mac duplicate
                   show l2vpn evpn mac evi <evi_id>
                   show l2vpn evpn mac evi <evi_id> address <mac_addr>
                   show l2vpn evpn mac evi <evi_id> duplicate
                   show l2vpn evpn mac evi <evi_id> local
                   show l2vpn evpn mac evi <evi_id> remote
                   show l2vpn evpn mac local
                   show l2vpn evpn mac remote
    """

    cli_command = ['show l2vpn evpn mac', # 0
                   'show l2vpn evpn mac address {mac_addr}', # 1
                   'show l2vpn evpn mac {mac_type}', # 2
                   'show l2vpn evpn mac bridge-domain {bd_id}', # 3
                   'show l2vpn evpn mac bridge-domain {bd_id} address {mac_addr}', # 4
                   'show l2vpn evpn mac bridge-domain {bd_id} {mac_type}', # 5
                   'show l2vpn evpn mac evi {evi_id}', # 6
                   'show l2vpn evpn mac evi {evi_id} address {mac_addr}', # 7
                   'show l2vpn evpn mac evi {evi_id} {mac_type}', # 8
    ]

    def cli(self, output=None, mac_addr=None, mac_type=None, bd_id=None, evi_id=None):
        if not output:
            # Only these CLI options for mac_type are supported.
            if mac_type and mac_type != 'local' and mac_type != 'remote' and mac_type != 'duplicate':
                raise Exception("Unsupported mac_type {}".format(mac_type))
            if bd_id:
                if mac_addr:
                    cli_cmd = self.cli_command[4].format(bd_id=bd_id, mac_addr=mac_addr)
                elif mac_type:
                    cli_cmd = self.cli_command[5].format(bd_id=bd_id, mac_type=mac_type)
                else:
                    cli_cmd = self.cli_command[3].format(bd_id=bd_id)
            elif evi_id:
                if mac_addr:
                    cli_cmd = self.cli_command[7].format(evi_id=evi_id, mac_addr=mac_addr)
                elif mac_type:
                    cli_cmd = self.cli_command[8].format(evi_id=evi_id, mac_type=mac_type)
                else:
                    cli_cmd = self.cli_command[6].format(evi_id=evi_id)
            else:
                if mac_addr:
                    cli_cmd = self.cli_command[1].format(mac_addr=mac_addr)
                elif mac_type:
                    cli_cmd = self.cli_command[2].format(mac_type=mac_type)
                else:
                    cli_cmd = self.cli_command[0]

            cli_output = self.device.execute(cli_cmd)
        else:
            cli_output = output

        if not cli_output:
            return {}

        # Case 1 - BD header
        #
        # MAC Address    EVI   BD    ESI                      Ether Tag  Next Hop(s)
        # -------------- ----- ----- ------------------------ ---------- ---------------
        # aabb.0011.0001 1     11    0000.0000.0000.0000.0000 0          Et1/0:11
        # aabb.0011.0021 1     11    0000.0000.0000.0000.0000 0          Duplicate
        # aabb.0012.0002 2     12    0000.0000.0000.0000.0000 0          2.2.2.1
        #
        # Case 2 - VLAN header
        #
        # MAC Address    EVI   VLAN  ESI                      Ether Tag  Next Hop(s)
        # -------------- ----- ----- ------------------------ ---------- ---------------
        # aabb.0011.0002 1     11    0000.0000.0000.0000.0000 0          2.2.2.1
        #
        # Case 3 - Multiple Next Hops
        #
        # MAC Address    EVI   BD    ESI                      Ether Tag  Next Hop(s)
        # -------------- ----- ----- ------------------------ ---------- ---------------
        # aabb.0012.0002 2     12    0000.0000.0000.0000.0000 0          2.2.2.1
        # aabb.cc02.2800 2     12    03AA.BB00.0000.0200.0001 0          3.3.3.1
        # aabb.cc82.2800 2     12    03AA.BB00.0000.0200.0001 0          Et1/0:12
        #                                                                3.3.3.1
        p1 = re.compile(r'^MAC Address\s+EVI\s+(BD|VLAN)\s+ESI\s+Ether Tag\s+Next Hop\(s\)$')
        p2 = re.compile(r'^(?P<mac>[0-9a-fA-F\.]+)\s+(?P<evi>\d+)\s+(?P<bd_id>\d+)\s+(?P<esi>[0-9a-fA-F\.]+)\s+(?P<etag>\d+)\s+(?P<next_hop>[\w\d\s\.:()/]+)$')
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

            # aabb.0011.0001 1     11    0000.0000.0000.0000.0000 0          Et1/0:11
            m = p2.match(line)
            if m:
                group = m.groupdict()
                mac_vals = parser_dict.setdefault(group['mac'], {})
                mac_vals.update({
                    'evi': int(group['evi']),
                    'bd_id': int(group['bd_id']),
                    'esi': group['esi'],
                    'etag': int(group['etag']),
                })
                next_hops = mac_vals.setdefault('next_hops', [])
                next_hops.append(group['next_hop'])
                continue

            #                                                                3.3.3.1
            m = p3.match(line)
            if m:
                group = m.groupdict()
                next_hops.append(group['next_hop'])
                continue

        if not header_validated:
            return {}

        return parser_dict

# ========================================
# Schema for 'show l2vpn evpn mac detail'
# ========================================
class ShowL2vpnEvpnMacDetailSchema(MetaParser):

    """ Schema for show l2vpn evpn mac address <mac_addr> detail
                   show l2vpn evpn mac bridge-domain <bd_id> address <mac_addr> detail
                   show l2vpn evpn mac bridge-domain <bd_id> detail
                   show l2vpn evpn mac bridge-domain <bd_id> duplicate detail
                   show l2vpn evpn mac bridge-domain <bd_id> local detail
                   show l2vpn evpn mac bridge-domain <bd_id> remote detail
                   show l2vpn evpn mac detail
                   show l2vpn evpn mac duplicate detail
                   show l2vpn evpn mac evi <evi_id> address <mac_addr> detail
                   show l2vpn evpn mac evi <evi_id> detail
                   show l2vpn evpn mac evi <evi_id> duplicate detail
                   show l2vpn evpn mac evi <evi_id> local detail
                   show l2vpn evpn mac evi <evi_id> remote detail
                   show l2vpn evpn mac local detail
                   show l2vpn evpn mac remote detail
    """

    schema = {
        Any(): { # MAC Address
            'sticky': bool,
            'stale': bool,
            'evi': int,
            'bd_id': int,
            'esi': str,
            'etag': int,
            'next_hops': list,
            Optional('local_addr'): str,
            'seq_num': int,
            'mac_only_present': bool,
            'mac_dup_detection': {
                'status': str,
                Optional('moves_count'): int,
                Optional('moves_limit'): int,
                Optional('expiry_time'): str,
            },
        },
    }

# ========================================
# Parser for 'show l2vpn evpn mac detail'
# ========================================
class ShowL2vpnEvpnMacDetail(ShowL2vpnEvpnMacDetailSchema):

    """ Parser for show l2vpn evpn mac address <mac_addr> detail
                   show l2vpn evpn mac bridge-domain <bd_id> address <mac_addr> detail
                   show l2vpn evpn mac bridge-domain <bd_id> detail
                   show l2vpn evpn mac bridge-domain <bd_id> duplicate detail
                   show l2vpn evpn mac bridge-domain <bd_id> local detail
                   show l2vpn evpn mac bridge-domain <bd_id> remote detail
                   show l2vpn evpn mac detail
                   show l2vpn evpn mac duplicate detail
                   show l2vpn evpn mac evi <evi_id> address <mac_addr> detail
                   show l2vpn evpn mac evi <evi_id> detail
                   show l2vpn evpn mac evi <evi_id> duplicate detail
                   show l2vpn evpn mac evi <evi_id> local detail
                   show l2vpn evpn mac evi <evi_id> remote detail
                   show l2vpn evpn mac local detail
                   show l2vpn evpn mac remote detail
    """

    cli_command = ['show l2vpn evpn mac detail', # 0
                   'show l2vpn evpn mac address {mac_addr} detail', # 1
                   'show l2vpn evpn mac {mac_type} detail', # 2
                   'show l2vpn evpn mac bridge-domain {bd_id} detail', # 3
                   'show l2vpn evpn mac bridge-domain {bd_id} address {mac_addr} detail', # 4
                   'show l2vpn evpn mac bridge-domain {bd_id} {mac_type} detail', # 5
                   'show l2vpn evpn mac evi {evi_id} detail', # 6
                   'show l2vpn evpn mac evi {evi_id} address {mac_addr} detail', # 7
                   'show l2vpn evpn mac evi {evi_id} {mac_type} detail', # 8
    ]

    def cli(self, output=None, mac_addr=None, mac_type=None, bd_id=None, evi_id=None):
        if not output:
            # Only these CLI options for mac_type are supported.
            if mac_type and mac_type != 'local' and mac_type != 'remote' and mac_type != 'duplicate':
                raise Exception("Unsupported mac_type {}".format(mac_type))
            if bd_id:
                if mac_addr:
                    cli_cmd = self.cli_command[4].format(bd_id=bd_id, mac_addr=mac_addr)
                elif mac_type:
                    cli_cmd = self.cli_command[5].format(bd_id=bd_id, mac_type=mac_type)
                else:
                    cli_cmd = self.cli_command[3].format(bd_id=bd_id)
            elif evi_id:
                if mac_addr:
                    cli_cmd = self.cli_command[7].format(evi_id=evi_id, mac_addr=mac_addr)
                elif mac_type:
                    cli_cmd = self.cli_command[8].format(evi_id=evi_id, mac_type=mac_type)
                else:
                    cli_cmd = self.cli_command[6].format(evi_id=evi_id)
            else:
                if mac_addr:
                    cli_cmd = self.cli_command[1].format(mac_addr=mac_addr)
                elif mac_type:
                    cli_cmd = self.cli_command[2].format(mac_type=mac_type)
                else:
                    cli_cmd = self.cli_command[0]

            cli_output = self.device.execute(cli_cmd)
        else:
            cli_output = output

        if not cli_output:
            return {}

        # MAC Address:                aabb.0011.0020
        # MAC Address:                aabb.0012.0002, sticky
        # MAC Address:                aabb.0012.0002 (stale)
        # MAC Address:                aabb.0012.0002, sticky (stale)
        p1 = re.compile(r'^MAC Address:\s+(?P<mac>[0-9a-fA-F\.]+)(,?\s+(?P<mac_status>[\w\s\(\)]+))?$')

        # EVPN Instance:              2
        p2 = re.compile(r'^EVPN Instance:\s+(?P<evi>\d+)$')

        # Bridge Domain:              11
        # Vlan:                       11
        p3 = re.compile(r'^(Bridge Domain|Vlan):\s+(?P<bd_id>\d+)$')

        # Ethernet Segment:           03AA.BB00.0000.0200.0001
        p4 = re.compile(r'^Ethernet Segment:\s+(?P<esi>[0-9a-fA-F\.]+)$')

        # Ethernet Tag ID:            0
        p5 = re.compile(r'^Ethernet Tag ID:\s+(?P<etag>\d+)$')

        # Next Hop(s):                L:17 Ethernet1/0 service instance 12
        #                             L:17 3.3.3.1
        #                             L:17 5.5.5.1
        p6 = re.compile(r'^Next Hop\(s\):\s+(?P<next_hop>[\w\d\s\.:()/]+)$')
        p7 = re.compile(r'^(?P<next_hop>[\w\d\s\.:()/]+)$')

        # Local Address:              4.4.4.1
        p8 = re.compile(r'^Local Address:\s+(?P<local_addr>[\d\.]+)$')

        # Sequence Number:            0
        p9 = re.compile(r'^Sequence Number:\s+(?P<seq_num>\d+)$')

        # MAC only present:           Yes
        p10 = re.compile(r'^MAC only present:\s+(?P<mac_only_present>(Yes|No))$')

        # MAC Duplication Detection:  Timer not running
        # MAC Duplication Detection:  MAC moves 3, limit 5
        #                             Timer expires in 09:56:34
        # MAC Duplication Detection:  Duplicate MAC address detected
        p11 = re.compile(r'^MAC Duplication Detection:\s+(?P<mac_dup_status>[\w\d\s,]+)$')
        p12 = re.compile(r'^MAC moves (?P<moves_count>\d+), limit (?P<moves_limit>\d+)$')
        p13 = re.compile(r'^\s+Timer expires in (?P<expiry_time>[\d:]+)$')

        parser_dict = {}

        for line in cli_output.splitlines():
            line = line.strip()
            if not line:
                continue

            # MAC Address:                aabb.0011.0020
            # MAC Address:                aabb.0012.0002, sticky
            # MAC Address:                aabb.0012.0002 (stale)
            # MAC Address:                aabb.0012.0002, sticky (stale)
            m = p1.match(line)
            if m:
                group = m.groupdict()
                mac_vals = parser_dict.setdefault(group['mac'], {})
                sticky = False
                stale = False
                if group['mac_status']:
                    sticky = 'sticky' in group['mac_status']
                    stale = 'stale' in group['mac_status']
                mac_vals.update({
                    'sticky': sticky,
                    'stale': stale,
                })
                continue

            # EVPN Instance:              2
            m = p2.match(line)
            if m:
                group = m.groupdict()
                mac_vals.update({'evi': int(group['evi'])})
                continue

            # Bridge Domain:              11
            # Vlan:                       11
            m = p3.match(line)
            if m:
                group = m.groupdict()
                mac_vals.update({'bd_id': int(group['bd_id'])})
                continue

            # Ethernet Segment:           03AA.BB00.0000.0200.0001
            m = p4.match(line)
            if m:
                group = m.groupdict()
                mac_vals.update({'esi': group['esi']})
                continue

            # Ethernet Tag ID:            0
            m = p5.match(line)
            if m:
                group = m.groupdict()
                mac_vals.update({'etag': int(group['etag'])})
                continue

            # Next Hop(s):                L:17 Ethernet1/0 service instance 12
            m = p6.match(line)
            if m:
                group = m.groupdict()
                next_hops = mac_vals.setdefault('next_hops', [])
                next_hops.append(group['next_hop'])
                continue

            # Local Address:              4.4.4.1
            m = p8.match(line)
            if m:
                group = m.groupdict()
                mac_vals.update({'local_addr': group['local_addr']})
                continue

            # Sequence Number:            0
            m = p9.match(line)
            if m:
                group = m.groupdict()
                mac_vals.update({'seq_num': int(group['seq_num'])})
                continue

            # MAC only present:           Yes
            m = p10.match(line)
            if m:
                group = m.groupdict()
                mac_only_present = True if group['mac_only_present'] == 'Yes' else False
                mac_vals.update({'mac_only_present': mac_only_present})
                continue

            # MAC Duplication Detection:  Timer not running
            # MAC Duplication Detection:  MAC moves 3, limit 5
            # MAC Duplication Detection:  Duplicate MAC address detected
            m = p11.match(line)
            if m:
                group = m.groupdict()
                mac_dup_status = group['mac_dup_status']
                mac_dup_vals = mac_vals.setdefault('mac_dup_detection', {})
                mac_dup_vals.update({'status': mac_dup_status})

                m = p12.match(mac_dup_status)
                if m:
                    mac_dup_vals.update({
                        'moves_count': int(group['moves_count']),
                        'moves_limit': int(group['moves_limit']),
                    })
                continue

            #                             Timer expires in 09:56:34
            m = p13.match(line)
            if m:
                group = m.groupdict()
                mac_dup_vals.update({'expiry_time': group['expiry_time']})
                continue

            # Check this pattern last as it can match other fields.
            #                             L:17 5.5.5.1
            m = p7.match(line)
            if m:
                group = m.groupdict()
                next_hops.append(group['next_hop'])
                continue

        return parser_dict

# =========================================
# Schema for 'show l2vpn evpn mac summary'
# =========================================
class ShowL2vpnEvpnMacSummarySchema(MetaParser):

    """ Schema for show l2vpn evpn mac bridge-domain <bd_id> duplicate summary
                   show l2vpn evpn mac bridge-domain <bd_id> local summary
                   show l2vpn evpn mac bridge-domain <bd_id> remote summary
                   show l2vpn evpn mac bridge-domain <bd_id> summary
                   show l2vpn evpn mac duplicate summary
                   show l2vpn evpn mac evi <evi_id> duplicate summary
                   show l2vpn evpn mac evi <evi_id> local summary
                   show l2vpn evpn mac evi <evi_id> remote summary
                   show l2vpn evpn mac evi <evi_id> summary
                   show l2vpn evpn mac local summary
                   show l2vpn evpn mac remote summary
                   show l2vpn evpn mac summary
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

# =========================================
# Parser for 'show l2vpn evpn mac summary'
# =========================================
class ShowL2vpnEvpnMacSummary(ShowL2vpnEvpnMacSummarySchema):

    """ Parser for show l2vpn evpn mac bridge-domain <bd_id> duplicate summary
                   show l2vpn evpn mac bridge-domain <bd_id> local summary
                   show l2vpn evpn mac bridge-domain <bd_id> remote summary
                   show l2vpn evpn mac bridge-domain <bd_id> summary
                   show l2vpn evpn mac duplicate summary
                   show l2vpn evpn mac evi <evi_id> duplicate summary
                   show l2vpn evpn mac evi <evi_id> local summary
                   show l2vpn evpn mac evi <evi_id> remote summary
                   show l2vpn evpn mac evi <evi_id> summary
                   show l2vpn evpn mac local summary
                   show l2vpn evpn mac remote summary
                   show l2vpn evpn mac summary
    """

    cli_command = ['show l2vpn evpn mac summary', # 0
                   'show l2vpn evpn mac {mac_type} summary', # 1
                   'show l2vpn evpn mac bridge-domain {bd_id} summary', # 2
                   'show l2vpn evpn mac bridge-domain {bd_id} {mac_type} summary', # 3
                   'show l2vpn evpn mac evi {evi_id} summary', # 4
                   'show l2vpn evpn mac evi {evi_id} {mac_type} summary', # 5
    ]

    def cli(self, output=None, mac_type=None, bd_id=None, evi_id=None):
        if not output:
            # Only these CLI options for mac_type are supported.
            if mac_type and mac_type != 'local' and mac_type != 'remote' and mac_type != 'duplicate':
                raise Exception("Unsupported mac_type {}".format(mac_type))
            if bd_id:
                if mac_type:
                    cli_cmd = self.cli_command[3].format(bd_id=bd_id, mac_type=mac_type)
                else:
                    cli_cmd = self.cli_command[2].format(bd_id=bd_id)
            elif evi_id:
                if mac_type:
                    cli_cmd = self.cli_command[5].format(evi_id=evi_id, mac_type=mac_type)
                else:
                    cli_cmd = self.cli_command[4].format(evi_id=evi_id)
            else:
                if mac_type:
                    cli_cmd = self.cli_command[1].format(mac_type=mac_type)
                else:
                    cli_cmd = self.cli_command[0]

            cli_output = self.device.execute(cli_cmd)
        else:
            cli_output = output

        if not cli_output:
            return {}

        # PE1#show l2vpn evpn mac bridge-domain 11 duplicate summary
        # EVI   BD    Ether Tag  Dup MAC    
        # ----- ----- ---------- ---------- 
        # 1     11    0          1         
        #
        # PE1#show l2vpn evpn mac bridge-domain 11 summary
        # EVI   BD    Ether Tag  Remote MAC Local MAC  Dup MAC
        # ----- ----- ---------- ---------- ---------- ----------
        # 1     11    0          4          6          1
        #
        # PE1#show l2vpn evpn mac remote summary
        # EVI   BD    Ether Tag  Remote MAC 
        # ----- ----- ---------- ---------- 
        # 1     11    0          4         
        # 2     12    0          2         
        #
        # Total                  6
        #
        # PE1#show l2vpn evpn mac summary
        # EVI   BD    Ether Tag  Remote MAC Local MAC  Dup MAC
        # ----- ----- ---------- ---------- ---------- ----------
        # 1     11    0          4          6          1
        # 2     12    0          2          2          0
        #
        # Total                  6          8          1
        #
        # VTEP1#show l2vpn evpn mac summary
        # EVI   VLAN  Ether Tag  Remote MAC Local MAC  Dup MAC
        # ----- ----- ---------- ---------- ---------- ----------
        # 1     11    0          1          0          0
        # 2     12    0          0          0          0
        #
        # Total                  1          0          0
        p1 = re.compile(r'^EVI\s+(BD|VLAN)\s+Ether Tag\s+Remote MAC\s+Local MAC\s+Dup MAC$')
        p2 = re.compile(r'^EVI\s+(BD|VLAN)\s+Ether Tag\s+Remote MAC$')
        p3 = re.compile(r'^EVI\s+(BD|VLAN)\s+Ether Tag\s+Local MAC$')
        p4 = re.compile(r'^EVI\s+(BD|VLAN)\s+Ether Tag\s+Dup MAC$')
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

            # 1     11    0          4          6          1
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

            # 1     11    0          4         
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

            # Total                  6          8          1
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

            # Total                  6
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
