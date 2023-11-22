''' show_u2m_sr.py
IOSXE parser for show commands:
   show platform hardware qfp active feature uni-sr

Copyright (c) 2022 by Cisco Systems, Inc.
All rights reserved.
'''
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional
import re

# ======================================================
# Schema for 'show platform hardware qfp active feature uni-sr'
# ======================================================


class ShowU2MSRSchema(MetaParser):
    """schema for 'show platform hardware qfp active feature uni-sr'"""
    schema = {
        Any(): {
            Any(): {
                'name': str,
                Optional('if_handle'): int,
                Optional('ingress_name'): str,
                Optional('ingress_hdl'): int,
                Optional('rep_cnt'): int,
                Optional('hash_val'): int,
                'prefix': str,
                Any(): {
                    Optional('src_filter'): str,
                    'trans_src': str,
                    'trans_dst': str,
                    Optional('octets'): int,
                    Optional('pkts'): int,
                }
            }
        }
    }


# ======================================================
# Parser for 'show platform hardware qfp active feature uni-sr'
# ======================================================

class ShowU2MSR(ShowU2MSRSchema):
    '''Parser for 'show plshow platform hardware qfp active feature uni-sr'
    '''

    cli_command = 'show platform hardware qfp active feature uni-sr'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Vif1:
        p1 = re.compile(r'Vif(?P<interface>\d+):')

        # unicast service reflect info:
        p2 = re.compile(r'unicast +service +reflect +info:')

        # vif name: Vif1
        p3 = re.compile(r'vif +name: *(?P<name>\w+)')

        # vif if_handle: 5997
        p4 = re.compile(r'vif +if_handle: *(?P<if_handle>\d+)')

        # ingress name: GigabitEthernet5
        p3_1 = re.compile(r'ingress +name: +(?P<ingress_name>\w+)')

        # ingress if_handle: 10
        p4_1 = re.compile(r'ingress +if_handle: +(?P<ingress_hdl>\d+)')

        # replica count: 1
        p5 = re.compile(r'replica +count: *(?P<rep_cnt>\d+)')

        # replica rule HW addr: 0x00000000e9d2fd60
        p6 = re.compile(r'replica +rule +HW +addr: *(?P<rep_hw_addr>\w+)')

        # hash val: 4
        p7 = re.compile(r'hash +val: *(?P<hash_val>\d+)')

        # prefix: 200.0.0.0/24
        p8 = re.compile(r'prefix: +(?P<prefix>\S+)')

        # replica node info:
        p9 = re.compile(r'replica +node +info:')

        # source filter: 66.1.1.0/24
        p10_1 = re.compile(r'source +filter: *(?P<src_filter>\S+)')

        # translated source: 100.1.1.1
        p10 = re.compile(r'translated +source: *(?P<trans_src>\S+)')

        # translated destination: 225.225.225.0/24
        p11 = re.compile(r'translated +destination: *(?P<trans_dst>\S+)')

        # replica rule HW addr: 0x00000000ed1a55c0
        p12 = re.compile(r'replica +rule +HW +addr: *(?P<rep_hw_addr>\w+)')

        # match: octets 0 packets 0
        p13 = re.compile(r'match: +octets *(?P<octets>\d+) +packets *(?P<pkts>\d+)')

        vif_sr_dict = {}
        uni_sr_num = 0
        rep_node_num = 0

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                intf = m.groupdict()['interface']
                intf = 'Vif' + intf
                uni_sr_num = 0
                rep_node_num = 0
                if intf not in vif_sr_dict:
                    vif_sr_dict[intf] = {}
                continue

            m = p2.match(line)
            if m:
                uni_sr_num += 1
                vif_sr_dict[intf][uni_sr_num] = {}
                rep_node_num = 0
                continue

            m = p3.match(line)
            if m:
                vif = m.groupdict()['name']
                vif_sr_dict[intf][uni_sr_num]['name'] = vif
                continue

            m = p4.match(line)
            if m:
                if_handle = m.groupdict()['if_handle']
                vif_sr_dict[intf][uni_sr_num]['if_handle'] = int(if_handle)
                continue

            m = p3_1.match(line)
            if m:
                ingress_name = m.groupdict()['ingress_name']
                vif_sr_dict[intf][uni_sr_num]['ingress_name'] = ingress_name
                continue

            m = p4_1.match(line)
            if m:
                ingress_hdl = m.groupdict()['ingress_hdl']
                vif_sr_dict[intf][uni_sr_num]['ingress_hdl'] = int(ingress_hdl)
                continue

            m = p5.match(line)
            if m:
                rep_cnt = m.groupdict()['rep_cnt']
                vif_sr_dict[intf][uni_sr_num]['rep_cnt'] = int(rep_cnt)
                continue

            m = p6.match(line)
            if m:
                continue

            m = p7.match(line)
            if m:
                hash_val = m.groupdict()['hash_val']
                vif_sr_dict[intf][uni_sr_num]['hash_val'] = int(hash_val)
                continue

            m = p8.match(line)
            if m:
                prefix = m.groupdict()['prefix']
                vif_sr_dict[intf][uni_sr_num]['prefix'] = prefix
                continue

            m = p9.match(line)
            if m:
                rep_node_num += 1
                vif_sr_dict[intf][uni_sr_num][rep_node_num] = {}
                continue

            m = p10_1.match(line)
            if m:
                src_filter = m.groupdict()['src_filter']
                vif_sr_dict[intf][uni_sr_num][
                    rep_node_num]['src_filter'] = src_filter
                continue

            m = p10.match(line)
            if m:
                trans_src = m.groupdict()['trans_src']
                vif_sr_dict[intf][uni_sr_num][
                    rep_node_num]['trans_src'] = trans_src
                continue

            m = p11.match(line)
            if m:
                trans_dst = m.groupdict()['trans_dst']
                vif_sr_dict[intf][uni_sr_num][
                    rep_node_num]['trans_dst'] = trans_dst
                continue

            m = p12.match(line)
            if m:
                continue

            m = p13.match(line)
            if m:
                octets = m.groupdict()['octets']
                pkts = m.groupdict()['pkts']
                vif_sr_dict[intf][uni_sr_num][rep_node_num]['octets'] = int(octets)
                vif_sr_dict[intf][uni_sr_num][rep_node_num]['pkts'] = int(pkts)
                continue

        return vif_sr_dict
