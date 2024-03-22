''' show_bd_datapath.py

IOSXE parsers for the following show commands:

    * 'show platform hardware qfp active feature bridge-domain datapath {bd_id}'

Copyright (c) 2022 by Cisco Systems, Inc.
All rights reserved.
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional, Or, Schema
from genie.parsergen import oper_fill_tabular


# ====================================================
#  schema for show nve peers
# ====================================================
class ShowBdDatapathSchema(MetaParser):
    """Schema for:
        * 'show platform hardware qfp active feature bridge-domain datapath {bd_id}'
    """

    schema = {
        Any(): {
            'state_enabled': str,
            Optional('aging_timeout'): int,
            Optional('aging_active_entry'): str,
            'max_mac_limit': int,
            Optional('unkwn_mac_limit_flood'): str,
            Optional('mac_learn_enabled'): str,
            Optional('mac_learn_controled'): str,
            Optional('unknown_unicast_olist'): str,
            Optional('otv_aed_enabled'): str,
            Optional('otv_enabled'): str,
            Optional('mcast_snooping_enabled'): str,
            Optional('feature'): str,
            Optional('sisf_snoop_protocols'): list,
            Optional('mac_learned'): int,
            Optional('bdi_outer_vtag'): str,
            Optional('bdi_inner_vtag'): str,
            'bridged': {
                'pkts': int,
                Optional('bytes'): int,
            },
            'unknown_unicast': {
                'pkts': int,
                Optional('bytes'): int,
            },
            'broadcasted': {
                'pkts': int,
                Optional('bytes'): int,
            },
            Optional('to_bdi'): {
                'pkts': int,
                Optional('bytes'): int,
            },
            Optional('injected'): {
                'pkts': int,
                Optional('bytes'): int,
            },
            Optional('violation_drop'): {
                'pkts': int,
                Optional('bytes'): int,
            },
            Optional('move_drop'): {
                'pkts': int,
                Optional('bytes'): int,
            },
            Optional('unknown_drop'): {
                'pkts': int,
                Optional('bytes'): int,
            },
            Optional('source_filter_drop'): {
                'pkts': int,
                Optional('bytes'): int,
            },
            Optional('bfib_policy_drop'): {
                'pkts': int,
                Optional('bytes'): int,
            },
            Optional('replication_start_drop'): {
                'pkts': int,
                Optional('bytes'): int,
            },
            Optional('recycle_tail_drop'): {
                'pkts': int,
                Optional('bytes'): int,
            },
            Optional('static_mac_move_drop'): {
                'pkts': int,
                Optional('bytes'): int,
            },
            Optional('bd_disabled_drop'): {
                'pkts': int,
                Optional('bytes'): int,
            },
            Optional('stp_state_drop'): {
                'pkts': int,
                Optional('bytes'): int,
            },
            Optional('uuf_suppression_drop'): {
                'pkts': int,
                Optional('bytes'): int,
            },
            'sisf_ctrl_punt': {
                'pkts': int,
                Optional('bytes'): int,
            },
            Optional('sisf_ctrl_drop'): {
                'pkts': int,
                Optional('bytes'): int,
            }
        }
    }

# ============================================
# Super Parser for:
#   * 'show nve peers '
#   * 'show nve peers interface nve {nve}'
#   * 'show nve peers peer-ip {peer_ip}'
#   * 'show nve peers vni {vni}'
# ============================================
class ShowBdDatapath(ShowBdDatapathSchema):
    """ Parser for the following show commands:
        * 'show platform hardware qfp active feature bridge-domain datapath {bd_id}'
    """

    cli_command = 'show platform hardware qfp active feature bridge-domain datapath {bd_id}'

    def cli(self, bd_id='', output=None):

        if output is None:
            cmd = self.cli_command.format(bd_id=bd_id)
            out = self.device.execute(cmd)
        else:
            out = output

        res_dict = {}
        # BD id                  : 2450
        p1 = re.compile(r'^\s*BD id[ :]*(?P<bd_id>[\d]+)\s*$')
        # State enabled          : Yes
        p2 = re.compile(r'^\s*State enabled[ :]*(?P<state_enabled>[a-zA-Z]+)\s*$')
        # Aging timeout (sec)    : 1800
        p3 = re.compile(r'^\s*Aging timeout[ :a-zA-Z\(\)]*(?P<aging_timeout>[\d]+)\s*$')
        # Aging active entry     : Yes
        p4 = re.compile(r'^\s*Aging active entry[ :]*(?P<aging_active_entry>[a-zA-Z]+)\s*$')
        # Max mac limit          : 65536
        p5 = re.compile(r'^\s*Max mac limit[ :]*(?P<max_mac_limit>[\d]+)\s*$')
        # Unkwn mac limit flood  : Yes
        p6 = re.compile(r'^\s*Unkwn mac limit flood[ :]*(?P<unkwn_mac_limit_flood>[a-zA-Z]+)\s*$')
        # mac_learn_enabled      : Yes
        p7 = re.compile(r'^\s*mac_learn_enabled[ :]*(?P<mac_learn_enabled>[a-zA-Z]+)\s*$')
        # mac_learn_controled    : Yes
        p8 = re.compile(r'^\s*mac_learn_controled[ :]*(?P<mac_learn_controled>[a-zA-Z]+)\s*$')
        # Unknown unicast olist  : Yes
        p9 = re.compile(r'^\s*Unknown unicast olist[ :]*(?P<unknown_unicast_olist>[a-zA-Z]+)\s*$')
        # otv_aed_enabled : No
        p10 = re.compile(r'^\s*otv_aed_enabled[ :]*(?P<otv_aed_enabled>[a-zA-Z]+)\s*$')
        # otv_enabled : No
        p11 = re.compile(r'^\s*otv_enabled[ :]*(?P<otv_enabled>[a-zA-Z]+)\s*$')
        # mcast_snooping_enabled : No
        p12 = re.compile(r'^\s*mcast_snooping_enabled[ :]*(?P<mcast_snooping_enabled>[a-zA-Z]+)\s*$')
        # Feature : evpn
        p13 = re.compile(r'^\s*Feature[ :]*(?P<feature>[a-zA-Z]+)\s*$')
        # SISF snoop protocols   : arp, ndp, dhcpv4, dhcpv6
        p14 = re.compile(r'^\s*SISF snoop protocols[ :]*(?P<sisf_snoop_protocols>[\D\d]+)\s*$')
        # Mac learned            : 2
        p15 = re.compile(r'^\s*Mac learned[ :]*(?P<mac_learned>[\d]+)\s*$')
        # BDI outer vtag         : 00000000
        p16 = re.compile(r'^\s*BDI outer vtag[ :]*(?P<bdi_outer_vtag>[\d]+)\s*$')
        # BDI inner vtag         : 00000000
        p17 = re.compile(r'^\s*BDI inner vtag[ :]*(?P<bdi_inner_vtag>[\d]+)\s*$')
        # Total bridged                pkts : 58379711   bytes: 5370933172
        p18 = re.compile(r'^\s*Total bridged(?P<bridged>)[\D]*(?P<pkts>[\d]+)[\D]*(?P<bytes>[\d]+)\s*$')
        # Total unknown unicast        pkts : 0          bytes: 0
        p19 = re.compile(r'^\s*Total unknown unicast(?P<unknown_unicast>)[\D]*(?P<pkts>[\d]+)[\D]*(?P<bytes>[\d]+)\s*$')
        # Total broadcasted            pkts : 34         bytes: 4012
        p20 = re.compile(r'^\s*Total broadcasted(?P<broadcasted>)[\D]*(?P<pkts>[\d]+)[\D]*(?P<bytes>[\d]+)\s*$')
        # Total to BDI                 pkts : 0          bytes: 0
        p21 = re.compile(r'^\s*Total to BDI(?P<to_bdi>)[\D]*(?P<pkts>[\d]+)[\D]*(?P<bytes>[\d]+)\s*$')
        # Total injected               pkts : 0          bytes: 0
        p22 = re.compile(r'^\s*Total injected(?P<injected>)[\D]*(?P<pkts>[\d]+)[\D]*(?P<bytes>[\d]+)\s*$')
        # Total mac-sec violation drop pkts : 0          bytes: 0
        p23 = re.compile(r'^\s*Total mac-sec violation drop pkts(?P<violation_drop>)[\D]*(?P<pkts>[\d]+)[\D]*(?P<bytes>[\d]+)\s*$')
        # Total mac-sec move drop      pkts : 0          bytes: 0
        p24 = re.compile(r'^\s*Total mac-sec move drop(?P<move_drop>)[\D]*(?P<pkts>[\d]+)[\D]*(?P<bytes>[\d]+)\s*$')
        # Total mac-sec unknown drop   pkts : 0          bytes: 0
        p25 = re.compile(r'^\s*Total mac-sec unknown drop(?P<unknown_drop>)[\D]*(?P<pkts>[\d]+)[\D]*(?P<bytes>[\d]+)\s*$')
        # Total source filter drop     pkts : 0          bytes: 0
        p26 = re.compile(r'^\s*Total source filter drop(?P<source_filter_drop>)[\D]*(?P<pkts>[\d]+)[\D]*(?P<bytes>[\d]+)\s*$')
        # Total bfib policy drop       pkts : 0          bytes: 0
        p27 = re.compile(r'^\s*Total bfib policy drop(?P<bfib_policy_drop>)[\D]*(?P<pkts>[\d]+)[\D]*(?P<bytes>[\d]+)\s*$')
        # Total replication start drop pkts : 0          bytes: 0
        p28 = re.compile(r'^\s*Total replication start drop pkts(?P<replication_start_drop>)[\D]*(?P<pkts>[\d]+)[\D]*(?P<bytes>[\d]+)\s*$')
        # Total recycle tail drop      pkts : 0          bytes: 0
        p29 = re.compile(r'^\s*Total recycle tail drop(?P<recycle_tail_drop>)[\D]*(?P<pkts>[\d]+)[\D]*(?P<bytes>[\d]+)\s*$')
        # Total static MAC move drop   pkts : 0          bytes: 0
        p30 = re.compile(r'^\s*Total static MAC move drop(?P<static_mac_move_drop>)[\D]*(?P<pkts>[\d]+)[\D]*(?P<bytes>[\d]+)\s*$')
        # Total BD disabled drop       pkts : 0          bytes: 0
        p31 = re.compile(r'^\s*Total BD disabled drop(?P<bd_disabled_drop>)[\D]*(?P<pkts>[\d]+)[\D]*(?P<bytes>[\d]+)\s*$')
        # Total STP state drop         pkts : 0          bytes: 0
        p32 = re.compile(r'^\s*Total STP state drop(?P<stp_state_drop>)[\D]*(?P<pkts>[\d]+)[\D]*(?P<bytes>[\d]+)\s*$')
        # Total UUF suppression drop   pkts : 0          bytes: 0
        p33 = re.compile(r'^\s*Total UUF suppression drop(?P<uuf_suppression_drop>)[\D]*(?P<pkts>[\d]+)[\D]*(?P<bytes>[\d]+)\s*$')
        # Total sisf ctrl punt         pkts : 24         bytes: 1968
        p34 = re.compile(r'^\s*Total sisf ctrl punt(?P<sisf_ctrl_punt>)[\D]*(?P<pkts>[\d]+)[\D]*(?P<bytes>[\d]+)\s*$')
        # Total sisf ctrl drop         pkts : 0          bytes: 0
        p35 = re.compile(r'^\s*Total sisf ctrl drop(?P<sisf_ctrl_drop>)[\D]*(?P<pkts>[\d]+)[\D]*(?P<bytes>[\d]+)\s*$')
        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue

            m = p1.match(line)
            if m:
                group = m.groupdict()
                bd_id = int(group['bd_id'])
                res_dict[bd_id] = {}
                continue
            m = p2.match(line)
            if m:
                group = m.groupdict()
                res_dict[bd_id]['state_enabled'] = group['state_enabled']
                continue
            m = p3.match(line)
            if m:
                group = m.groupdict()
                res_dict[bd_id]['aging_timeout'] = int(group['aging_timeout'])
                continue
            m = p4.match(line)
            if m:
                group = m.groupdict()
                res_dict[bd_id]['aging_active_entry'] = group['aging_active_entry']
                continue
            m = p5.match(line)
            if m:
                group = m.groupdict()
                res_dict[bd_id]['max_mac_limit'] = int(group['max_mac_limit'])
                continue
            m = p6.match(line)
            if m:
                group = m.groupdict()
                res_dict[bd_id]['unkwn_mac_limit_flood'] = group['unkwn_mac_limit_flood']
                continue
            m = p7.match(line)
            if m:
                group = m.groupdict()
                res_dict[bd_id]['mac_learn_enabled'] = group['mac_learn_enabled']
                continue
            m = p8.match(line)
            if m:
                group = m.groupdict()
                res_dict[bd_id]['mac_learn_controled'] = group['mac_learn_controled']
                continue
            m = p9.match(line)
            if m:
                group = m.groupdict()
                res_dict[bd_id]['unknown_unicast_olist'] = group['unknown_unicast_olist']
                continue
            m = p10.match(line)
            if m:
                group = m.groupdict()
                res_dict[bd_id]['otv_aed_enabled'] = group['otv_aed_enabled']
                continue
            m = p11.match(line)
            if m:
                group = m.groupdict()
                res_dict[bd_id]['otv_enabled'] = group['otv_enabled']
                continue
            m = p12.match(line)
            if m:
                group = m.groupdict()
                res_dict[bd_id]['mcast_snooping_enabled'] = group['mcast_snooping_enabled']
                continue
            m = p13.match(line)
            if m:
                group = m.groupdict()
                res_dict[bd_id]['feature'] = group['feature']
                continue
            m = p14.match(line)
            if m:
                group = m.groupdict()
                res_dict[bd_id]['sisf_snoop_protocols'] = group['sisf_snoop_protocols'].replace(' ','').split(',')
                continue
            m = p15.match(line)
            if m:
                group = m.groupdict()
                res_dict[bd_id]['mac_learned'] = int(group['mac_learned'])
                continue
            m = p16.match(line)
            if m:
                group = m.groupdict()
                res_dict[bd_id]['bdi_outer_vtag'] = group['bdi_outer_vtag']
                continue
            m = p17.match(line)
            if m:
                group = m.groupdict()
                res_dict[bd_id]['bdi_inner_vtag'] = group['bdi_inner_vtag']
                continue
            m = p18.match(line)
            if m:
                group = m.groupdict()
                res_dict[bd_id]['bridged'] = {}
                res_dict[bd_id]['bridged']['pkts'] = int(group['pkts'])
                res_dict[bd_id]['bridged']['bytes'] = int(group['bytes'])
                continue
            m = p19.match(line)
            if m:
                group = m.groupdict()
                res_dict[bd_id]['unknown_unicast'] = {}
                res_dict[bd_id]['unknown_unicast']['pkts'] = int(group['pkts'])
                res_dict[bd_id]['unknown_unicast']['bytes'] = int(group['bytes'])
                continue
            m = p20.match(line)
            if m:
                group = m.groupdict()
                res_dict[bd_id]['broadcasted'] = {}
                res_dict[bd_id]['broadcasted']['pkts'] = int(group['pkts'])
                res_dict[bd_id]['broadcasted']['bytes'] = int(group['bytes'])
                continue
            m = p21.match(line)
            if m:
                group = m.groupdict()
                res_dict[bd_id]['to_bdi'] = {}
                res_dict[bd_id]['to_bdi']['pkts'] = int(group['pkts'])
                res_dict[bd_id]['to_bdi']['bytes'] = int(group['bytes'])
                continue
            m = p22.match(line)
            if m:
                group = m.groupdict()
                res_dict[bd_id]['injected'] = {}
                res_dict[bd_id]['injected']['pkts'] = int(group['pkts'])
                res_dict[bd_id]['injected']['bytes'] = int(group['bytes'])
                continue
            m = p23.match(line)
            if m:
                group = m.groupdict()
                res_dict[bd_id]['violation_drop'] = {}
                res_dict[bd_id]['violation_drop']['pkts'] = int(group['pkts'])
                res_dict[bd_id]['violation_drop']['bytes'] = int(group['bytes'])
                continue
            m = p24.match(line)
            if m:
                group = m.groupdict()
                res_dict[bd_id]['move_drop'] = {}
                res_dict[bd_id]['move_drop']['pkts'] = int(group['pkts'])
                res_dict[bd_id]['move_drop']['bytes'] = int(group['bytes'])
                continue
            m = p25.match(line)
            if m:
                group = m.groupdict()
                res_dict[bd_id]['unknown_drop'] = {}
                res_dict[bd_id]['unknown_drop']['pkts'] = int(group['pkts'])
                res_dict[bd_id]['unknown_drop']['bytes'] = int(group['bytes'])
                continue
            m = p26.match(line)
            if m:
                group = m.groupdict()
                res_dict[bd_id]['source_filter_drop'] = {}
                res_dict[bd_id]['source_filter_drop']['pkts'] = int(group['pkts'])
                res_dict[bd_id]['source_filter_drop']['bytes'] = int(group['bytes'])
                continue
            m = p27.match(line)
            if m:
                group = m.groupdict()
                res_dict[bd_id]['bfib_policy_drop'] = {}
                res_dict[bd_id]['bfib_policy_drop']['pkts'] = int(group['pkts'])
                res_dict[bd_id]['bfib_policy_drop']['bytes'] = int(group['bytes'])
                continue
            m = p28.match(line)
            if m:
                group = m.groupdict()
                res_dict[bd_id]['replication_start_drop'] = {}
                res_dict[bd_id]['replication_start_drop']['pkts'] = int(group['pkts'])
                res_dict[bd_id]['replication_start_drop']['bytes'] = int(group['bytes'])
                continue
            m = p29.match(line)
            if m:
                group = m.groupdict()
                res_dict[bd_id]['recycle_tail_drop'] = {}
                res_dict[bd_id]['recycle_tail_drop']['pkts'] = int(group['pkts'])
                res_dict[bd_id]['recycle_tail_drop']['bytes'] = int(group['bytes'])
                continue
            m = p30.match(line)
            if m:
                group = m.groupdict()
                res_dict[bd_id]['static_mac_move_drop'] = {}
                res_dict[bd_id]['static_mac_move_drop']['pkts'] = int(group['pkts'])
                res_dict[bd_id]['static_mac_move_drop']['bytes'] = int(group['bytes'])
                continue
            m = p31.match(line)
            if m:
                group = m.groupdict()
                res_dict[bd_id]['bd_disabled_drop'] = {}
                res_dict[bd_id]['bd_disabled_drop']['pkts'] = int(group['pkts'])
                res_dict[bd_id]['bd_disabled_drop']['bytes'] = int(group['bytes'])
                continue
            m = p32.match(line)
            if m:
                group = m.groupdict()
                res_dict[bd_id]['stp_state_drop'] = {}
                res_dict[bd_id]['stp_state_drop']['pkts'] = int(group['pkts'])
                res_dict[bd_id]['stp_state_drop']['bytes'] = int(group['bytes'])
                continue
            m = p33.match(line)
            if m:
                group = m.groupdict()
                res_dict[bd_id]['uuf_suppression_drop'] = {}
                res_dict[bd_id]['uuf_suppression_drop']['pkts'] = int(group['pkts'])
                res_dict[bd_id]['uuf_suppression_drop']['bytes'] = int(group['bytes'])
                continue
            m = p34.match(line)
            if m:
                group = m.groupdict()
                res_dict[bd_id]['sisf_ctrl_punt'] = {}
                res_dict[bd_id]['sisf_ctrl_punt']['pkts'] = int(group['pkts'])
                res_dict[bd_id]['sisf_ctrl_punt']['bytes'] = int(group['bytes'])
                continue
            m = p35.match(line)
            if m:
                group = m.groupdict()
                res_dict[bd_id]['sisf_ctrl_drop'] = {}
                res_dict[bd_id]['sisf_ctrl_drop']['pkts'] = int(group['pkts'])
                res_dict[bd_id]['sisf_ctrl_drop']['bytes'] = int(group['bytes'])
                continue

        return res_dict
