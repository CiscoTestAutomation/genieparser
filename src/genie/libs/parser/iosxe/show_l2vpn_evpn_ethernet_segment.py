# ------------------------------------------------------------------
#
# Copyright (c) 2021 by Cisco Systems, Inc.
# All rights reserved.
# ------------------------------------------------------------------

import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional
from genie.parsergen import oper_fill_tabular

# ============================================
# Schema for 'show l2vpn evpn ethernet-segment detail'
# ============================================
class ShowL2vpnEvpnEthernetSegmentDetailSchema(MetaParser):
    """ Schema for show l2vpn evpn ethernet-segment detail
                   show l2vpn evpn ethernet-segment interface {id} detail
    """

    schema = {
        Any(): {
            'interface': str,
            'redundancy_mode': str,
            'df_wait_time': int,
            'split_horizon_label': int,
            'state': str,
            'encap_type': str,
            'ordinal': str,
            'core_isolation': str,
            'rd': str,
            'export_rt': str,
            'forwarder_list': list,
        }
    }


# ==================================================
# Parser for 'show l2vpn evpn ethernet-segment detail'
# ==================================================
class ShowL2vpnEvpnEthernetSegmentDetail(ShowL2vpnEvpnEthernetSegmentDetailSchema):
    """ Parser for: show l2vpn evpn ethernet-segment detail
                    show l2vpn evpn ethernet-segment interface {id} detail
    """

    cli_command = [
           'show l2vpn evpn ethernet-segment interface {id} detail',
           'show l2vpn evpn ethernet-segment detail'
                  ]

    def cli(self, id=None, output=None):

        if output is None:
            # Execute command
            if id:
                cli_cmd = self.device.execute(self.cli_command[0].format(id=id))
            else:
                cli_cmd = self.device.execute(self.cli_command[1])
            cli_output = self.device.execute(cli_cmd)
        else:
            cli_output = output

        # EVPN Ethernet Segment ID: 03AA.BB00.0000.0200.0001
        p1 = re.compile(r'^EVPN +Ethernet +Segment +ID: +(?P<eth_seg>[0-9a-fA-F\.]+)$')

        # Interface:              Po1
        p2 = re.compile(r'^Interface: +(?P<intf>.*)$')

        # Redundancy mode:        all-active
        p3 = re.compile(r'^Redundancy +mode: +(?P<redundancy_mode>[a-z\-]+)$')

        # DF election wait time:  3 seconds
        p4 = re.compile(r'^DF +election +wait +time: +(?P<df_time>[0-9]+) +seconds$')

        # Split Horizon label:    16 
        p5 = re.compile(r'^Split +Horizon +label: +(?P<sh_label>\d+)$')

        # State:                  Ready
        p6 = re.compile(r'^State: +(?P<state>\w+)$')

        # Encapsulation:          mpls
        p7 = re.compile(r'^Encapsulation: +(?P<encap_type>\w+)$')

        # Ordinal:                1
        p8 = re.compile(r'^Ordinal: +(?P<ordinal>\d+)$')

        # Core Isolation:         No
        p9 = re.compile(r'^Core +Isolation: +(?P<core_iso>\w+)$')

        # RD:                     4.4.4.3:1
        p10 = re.compile(r'^RD: +(?P<rd>[0-9\.:]+)$')

        # Export-RTs:           100:2
        p11 = re.compile(r'^Export-RTs: +(?P<export_rt>[0-9: ]+)$')

        # Forwarder List:         3.3.3.3 4.4.4.3
        p12 = re.compile(r'^Forwarder +List: +(?P<fwd>[0-9\. /]+)$')

        parser_dict = {}

        if not cli_output:
            return

        for line in cli_output.splitlines():
            line = line.strip()

            #EVPN Ethernet Segment ID: 03AA.BB00.0000.0200.0001
            m = p1.match(line)
            if m:
                group = m.groupdict()
                eth_seg = parser_dict.setdefault(group['eth_seg'], {}) 
                continue

            #  Interface:              Po1
            m = p2.match(line)
            if m:
                group = m.groupdict()
                eth_seg.update({'interface': group['intf']})
                continue

            #  Redundancy mode:        all-active
            m = p3.match(line)
            if m:
                group = m.groupdict()
                eth_seg.update({'redundancy_mode': group['redundancy_mode']})
                continue

            #  DF election wait time:  3 seconds
            m = p4.match(line)
            if m:
                group = m.groupdict()
                eth_seg.update({'df_wait_time': int(group['df_time'])})
                continue

            #  Split Horizon label:    16
            m = p5.match(line)
            if m:
                group = m.groupdict()
                eth_seg.update({'split_horizon_label': int(group['sh_label'])})
                continue
            #  State:                  Ready
            m = p6.match(line)
            if m:
                group = m.groupdict()
                eth_seg.update({'state': group['state']})
                continue
            #  Encapsulation:          mpls
            m = p7.match(line)
            if m:
                group = m.groupdict()
                eth_seg.update({'encap_type': group['encap_type']})
                continue
            #  Ordinal:                1
            m = p8.match(line)
            if m:
                group = m.groupdict()
                eth_seg.update({'ordinal': group['ordinal']})
                continue
            #  Core Isolation:         No
            m = p9.match(line)
            if m:
                group = m.groupdict()
                eth_seg.update({'core_isolation': group['core_iso']})
                continue
            #  RD:                     4.4.4.3:1
            m = p10.match(line)
            if m:
                group = m.groupdict()
                eth_seg.update({'rd': group['rd']})
                continue
            #    Export-RTs:           100:2
            m = p11.match(line)
            if m:
                group = m.groupdict()
                eth_seg.update({'export_rt': group['export_rt']})
                continue

            #  Forwarder List:         3.3.3.3 4.4.4.3
            m = p12.match(line)
            if m:
                group = m.groupdict()
                fwd = group['fwd']
                fwd_list = eth_seg.setdefault('forwarder_list', [])
                for item in fwd.split():
                    fwd_list.append(item) 
                continue

        return parser_dict

# ============================================
# Schema for 'show l2vpn evpn ethernet-segment'
# ============================================
class ShowL2vpnEvpnEthernetSegmentSchema(MetaParser):
    """ Schema for show l2vpn evpn ethernet-segment
    """

    schema = {
        'esi': {
            Any(): {
                'port': str,
                'redundancy_mode': str,
                'df_wait_time': int,
                'split_horizon_label': int,
            }
        }
    }

# ==================================================
# Parser for 'show l2vpn evpn ethernet-segment'
# ==================================================
class ShowL2vpnEvpnEthernetSegment(ShowL2vpnEvpnEthernetSegmentSchema):
    """ Parser for: show l2vpn evpn ethernet-segment """

    cli_command = 'show l2vpn evpn ethernet-segment'

    def cli(self, output=None):

        parsed_dict = {}

        if output is None:
            # Execute command
            cli_output = self.device.execute(self.cli_command)
        else:
            cli_output = output

        #03AA.AABB.BBCC.CC00.0001 Et0/2      single-active   3       16
        p1 = re.compile(r'^(?P<esi>(\w+\.\w+\.\w+\.\w+\.\w+|N/A)) +(?P<port>\S+) +(?P<redundancy_mode>\S+) +(?P<df_time>\S+) +(?P<sh_label>\S+)$')
        parser_dict = {}

        if not cli_output:
            return

        for line in cli_output.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                esi = parser_dict.setdefault('esi', {})
                eth_seg = esi.setdefault(group['esi'], {}) 
                eth_seg.update({'port':group['port']})
                eth_seg.update({'redundancy_mode':group['redundancy_mode']})
                eth_seg.update({'df_wait_time':int(group['df_time'])})
                eth_seg.update({'split_horizon_label':int(group['sh_label'])})
                continue

        return parser_dict

