'''show lslib.py
IOSXE parser for the following show command:
  * show lslib producer all lscache links detail
'''

import re
# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Or, And, \
    Default, Use


class ShowLslibProducerAllLscacheLinksDetailSchema(MetaParser):
    """Schema for show lslib producer all lscache links detail"""
    schema = {
        'link': {
            int: {
                'protocol': str,
                'identifier': str,
                Or('local_node_descriptor', 'remote_node_descriptor'): {
                    Optional('as_number'): int,
                    Optional('bgp_identifier'): str,
                    Optional('area_id'): str,
                    Optional('router_id'): str,
                    Optional('iso_node_id'): str,
                },
                'link_descriptor': {
                    Optional('link_id'): str,
                    Optional('local_intf_address'): str,
                    Optional('neighbor_intf_address'): str,
                    Optional('multi_topology'): str,
                },
                'internal_flag': str,
                'action': str,
                'merged_link_attr': {
                    Optional('metric'): int,
                    Optional('admin_group'): str,
                    Optional('max_link_bw'): int,
                    Optional('max_reserv_link_bw'): int,
                    Optional('max_unreserv_link_bw'): list,
                    Optional('te_default_metric'): int,
                    Optional('link_protection_type'): str,
                    Optional('mpls_proto_mask'): str,
                    Optional('opaque_link_attr'): str,
                    Optional('link_name'): str,
                    Optional('adj_sid'): list,
                    Optional('lan_adj_sid'): list,
                    Optional('srlg') : list,
                    Optional('extended_admin_group'): str,
                    Optional('link_delay'): int,
                    Optional('min_delay'): int,
                    Optional('max_delay'): int,
                    Optional('delay_variation'): int,
                    Optional('link_loss'): str,
                    Optional('residual_bw'): int,
                    Optional('available_bw'): int,
                    Optional('utilized_bw'): int,
                    Optional('asla'): {
                        Optional('sabm'): str,
                        Optional('te_default_metric'): int,
                    },
                },
            },
        },
    }


# ====================================
#  Parser for 'show lslib producer all lscache links detail'
# ====================================
class ShowLslibProducerAllLscacheLinksDetail(ShowLslibProducerAllLscacheLinksDetailSchema):
    """Parser for show lslib producer all lscache links detail"""

    cli_command = ['show lslib producer all lscache links detail']

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command[0])

        # Init parsed dict
        parsed_dict = {}

        # Type: Link
        p0 = re.compile(r'^Type: (?P<type>[\w]+)$')

        # Protocol: ISIS L1
        p1 = re.compile(r'^Protocol: (?P<protocol>[\w ]+)$')

        # Identifier: 0x0
        p2 = re.compile(r'^Identifier: (?P<identifier>[\w]+)$')

        # Local Node Descriptor:
        p3 = re.compile(r'^Local Node Descriptor:$')

        # Remote Node Descriptor:
        p4 = re.compile(r'^Remote Node Descriptor:$')

        # Link Descriptor:
        p5 = re.compile(r'^Link Descriptor:$')

        # Merged Link Attributes:
        p6 = re.compile(r'^Merged Link Attributes:$')

        # AS Number: 50
        p7 = re.compile(r'^AS Number: (?P<asnum>[\d]+)$')

        # BGP Identifier: 0.0.0.0
        p8 = re.compile(r'^BGP Identifier: (?P<bgpid>[\w.]+)$')

        # Area ID: 0.0.0.0
        p9 = re.compile(r'^Area ID: (?P<areaid>[\w.]+)$')

        # Router ID IPv4: 22.2.2.2
        p10 = re.compile(r'^Router ID IPv4: (?P<routerid>[\w.]+)$')

        # ISO Node ID: 2222.2222.2222
        p17 = re.compile(r'^ISO Node ID: (?P<isonode>[\w.]+)$')

        # Link ID: 1.2
        p11 = re.compile(r'^Link ID: (?P<linkid>[\d.]+)$')

        # Local Interface Address IPv4: 1.2.0.12
        p12 = re.compile(r'^Local Interface Address IPv4: (?P<localintfaddr>[\w.]+)$')

        # Neighbor Interface Address IPv4: 1.2.0.21
        p13 = re.compile(r'^Neighbor Interface Address IPv4: (?P<Neighborintfaddr>[\w.]+)$')

        # Multi-Topology: 121x7
        p18 = re.compile(r'^Multi-Topology: (?P<multi_topo>[\w]+)$')

        # Internal flags: 0x0
        p14 = re.compile(r'^Internal flags: (?P<internal_flag>[\d\w]+)$')

        # Action: Update
        p15 = re.compile(r'^Action: (?P<action>[\w]+)$')

        # Metric: 10
        p16 = re.compile(r'^Metric: (?P<metric>[\d]+)$')

        # Admin-group: 0x00000001
        p19 = re.compile(r'^Admin-group: (?P<admin_group>[\w]+)$')

        # Max-link-bw (kbits/sec): 9
        p20 = re.compile(r'^Max-link-bw \(kbits\/sec\): (?P<max_link>[\d]+)$')

        # Max-reserv-link-bw (kbits/sec): 17
        p21 = re.compile(r'^Max-reserv-link-bw \(kbits\/sec\): (?P<max_res_link>[\d]+)$')

        # TE-default-metric: 301989888
        p22 = re.compile(r'^TE-default-metric: (?P<te_metric>[\d]+)$')

        # ADJ-SID:
        p23 = re.compile(r'^ADJ-SID:$')

        # LAN-ADJ-SID:
        p25 = re.compile(r'^LAN-ADJ-SID:$')

        # 18(0x1)
        # 4608(0x2)(18.0.18.0)
        p26 = re.compile(r'(?P<sid>[\d()x]+\((\d+.)+)$')

        #ASLA:
        p27 = re.compile(r'^ASLA:$')

        #SABM:(4,
        p28 = re.compile(r'^SABM: (?P<sabm>[(\d,]+)*$')

        p29 = re.compile(r'^(?P<sab>[\s+\d+x+[\d]+\))$')

        # Link-protection-type: 0x1200
        p30 = re.compile(r'^Link-protection-type: (?P<link_protection>[\w]+)$')

        # MPLS-proto-mask: 0x12
        p31 = re.compile(r'^MPLS-proto-mask: (?P<mpls_proto>[\w]+)$')

        # Link-name: L12
        p32 = re.compile(r'^Link-name: (?P<link_name>[\w]+)$')

        # Link-delay (us): 1179648 (A)
        p33 = re.compile(r'^Link-delay \(us\): (?P<link_delay>[\w]+).*$')

        # Min-delay (us): 18 Max-delay (us): 1179666
        p34 = re.compile(r'^Min-delay \(us\): (?P<min_delay>[\d]+) Max-delay \(us\): (?P<max_delay>[\d]+)$')

        # Delay-variation (us): 1184274
        p35 = re.compile(r'^Delay-variation \(us\): (?P<delay_var>[\d]+)$')

        # Link-loss (%): 18 * 0.000003 (A)
        p36 = re.compile(r'^Link-loss \(%\): (?P<link_loss>.*)')

        # Residual-bw (kbits/sec): 9
        p37 = re.compile(r'^Residual-bw \(kbits\/sec\): (?P<res>[\d]+)$')

        # Available-bw (kbits/sec): 9
        p38 = re.compile(r'^Available-bw \(kbits\/sec\): (?P<available_bw>[\d]+)$')

        # Utilized-bw (kbits/sec): 9
        p39 = re.compile(r'^Utilized-bw \(kbits\/sec\): (?P<utilized_bw>[\d]+)$')

        # Max-unreserv-link-bw (kbits/sec):
        p40 = re.compile(r'^Max-unreserv-link-bw \(kbits\/sec\):$')

        # Opaque-link-attr:
        p41 = re.compile(r'^Opaque-link-attr:$')

        # 0x4C.0x69.0x6E.0x6B.0x20.0x4F.0x6E.0x65.0x20.0x54.0x77
        p41_1 = re.compile(r'^(?P<opaque>(\w*\.)+.*)$')

        # SRLG:
        p42 = re.compile(r'^SRLG:$')

        # 18         4608       1184256    303174144
        p43 = re.compile(r'^(?P<srlg_links>(\d+\s+)+)')

        # Link Attributes of Group 0x1:
        p44 = re.compile(r'^Link Attributes of Group.*$')

        # Extended Admin-group:
        p45 = re.compile(r'^Extended Admin-group:$')

        # 0x00000001 0x00000002 0x00000004 0x00000008
        p46 = re.compile(r'^(?P<ext_admin>(\dx\w+\s*)+$)')

        sabm = ''
        link_attr = False
        for line in output.splitlines():
            line = line.strip()

            # Type: Link
            m = p0.match(line)
            if m:
                res_dict = parsed_dict.setdefault('link', {})
                result_dict_index = len(res_dict) + 1
                result_dict = res_dict.setdefault(result_dict_index, {})
                link_attr = False
                continue

            # Protocol: ISIS L1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                result_dict['protocol'] = group['protocol']
                continue

            # Identifier: 0x0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                result_dict['identifier'] = group['identifier']
                continue

            # Local Node Descriptor:
            m = p3.match(line)
            if m:
                descriptor_dict = result_dict.setdefault('local_node_descriptor', {})
                continue

            # Remote Node Descriptor:
            m = p4.match(line)
            if m:
                descriptor_dict = result_dict.setdefault('remote_node_descriptor', {})
                continue

            # Link Descriptor:
            m = p5.match(line)
            if m:
                link_dict = result_dict.setdefault('link_descriptor', {})
                continue

            # Merged Link Attributes:
            m = p6.match(line)
            if m:
                merge_dict = result_dict.setdefault('merged_link_attr',{})
                continue

            # AS Number: 50
            m = p7.match(line)
            if m:
                descriptor_dict['as_number'] = int(m.groupdict()['asnum'])
                continue

            # BGP Identifier: 0.0.0.0
            m = p8.match(line)
            if m:
                descriptor_dict['bgp_identifier'] = m.groupdict()['bgpid']
                continue

            # Area ID: 0.0.0.0
            m = p9.match(line)
            if m:
                descriptor_dict['area_id'] = m.groupdict()['areaid']
                continue

            # Router ID IPv4: 22.2.2.2
            m = p10.match(line)
            if m:
                descriptor_dict['router_id'] = m.groupdict()['routerid']
                continue

            # Link ID: 1.2
            m = p11.match(line)
            if m:
                link_dict['link_id'] = m.groupdict()['linkid']
                continue

            # Local Interface Address IPv4: 1.2.0.12
            m = p12.match(line)
            if m:
                link_dict['local_intf_address'] = m.groupdict()['localintfaddr']
                continue

            # Neighbor Interface Address IPv4: 1.2.0.21
            m = p13.match(line)
            if m:
                link_dict['neighbor_intf_address'] = m.groupdict()['Neighborintfaddr']
                continue

            # Internal flags: 0x0
            m = p14.match(line)
            if m:
                result_dict['internal_flag'] = m.groupdict()['internal_flag']
                continue

            # Action: Update
            m = p15.match(line)
            if m:
                result_dict['action'] = m.groupdict()['action']
                continue

            # Metric: 10
            m = p16.match(line)
            if m:
                merge_dict['metric'] = int(m.groupdict()['metric'])
                continue

            # ISO Node ID: 2222.2222.2222
            m = p17.match(line)
            if m:
                descriptor_dict['iso_node_id'] = m.groupdict()['isonode']
                continue

            # Multi-Topology: 121x7
            m = p18.match(line)
            if m:
                link_dict['multi_topology'] = m.groupdict()['multi_topo']
                continue

            # Admin-group: 0x00000001
            m = p19.match(line)
            if m:
                merge_dict['admin_group'] = m.groupdict()['admin_group']
                continue

            # Max-link-bw (kbits/sec): 9
            m = p20.match(line)
            if m:
                merge_dict['max_link_bw'] = int(m.groupdict()['max_link'])
                continue

            # Max-reserv-link-bw (kbits/sec): 17
            m = p21.match(line)
            if m:
                merge_dict['max_reserv_link_bw'] = int(m.groupdict()['max_res_link'])
                continue

            # TE-default-metric: 301989888
            m = p22.match(line)
            if m:
                if 'asla' in merge_dict and not link_attr:
                    result = merge_dict['asla']
                    result['te_default_metric'] = int(m.groupdict()['te_metric'])
                else:
                    merge_dict['te_default_metric'] = int(m.groupdict()['te_metric'])
                continue

            # ADJ-SID:
            m = p23.match(line)
            if m:
                sid_dict = merge_dict.setdefault('adj_sid', [])
                continue

            # LAN-ADJ-SID:
            m = p25.match(line)
            if m:
                sid_dict = merge_dict.setdefault('lan_adj_sid', [])
                continue

            # 18(0x1)
            # 4608(0x2)(18.0.18.0)
            m = p26.match(line)
            if m:
                if not link_attr:
                    sid_dict.append(m.groupdict()['sid'])
                continue

            # ASLA:
            m = p27.match(line)
            if m:
                asla_dict = merge_dict.setdefault('asla', {})
                continue

            # SABM:(4,
            m = p28.match(line)
            if m:
                sabm = m.groupdict()['sabm']
                continue

            m = p29.match(line)
            if m:
                asla_dict['sabm'] = sabm + m.groupdict()['sab']
                continue

            # Link-protection-type: 0x1200
            m = p30.match(line)
            if m:
                merge_dict['link_protection_type'] = m.groupdict()['link_protection']
                continue

            # MPLS-proto-mask: 0x12
            m = p31.match(line)
            if m:
                merge_dict['mpls_proto_mask'] = m.groupdict()['mpls_proto']
                continue

            # Link-name: L12
            m = p32.match(line)
            if m:
                merge_dict['link_name'] = m.groupdict()['link_name']
                continue

            # Link-delay (us): 1179648 (A)
            m = p33.match(line)
            if m:
                merge_dict['link_delay'] = int(m.groupdict()['link_delay'])
                continue

            # Min-delay (us): 18 Max-delay (us): 1179666
            m = p34.match(line)
            if m:
                merge_dict['min_delay'] = int(m.groupdict()['min_delay'])
                merge_dict['max_delay'] = int(m.groupdict()['max_delay'])
                continue

            # Delay-variation (us): 1184274
            m = p35.match(line)
            if m:
                merge_dict['delay_variation'] = int(m.groupdict()['delay_var'])
                continue

            # Link-loss (%): 18 * 0.000003 (A)
            m = p36.match(line)
            if m:
                merge_dict['link_loss'] = m.groupdict()['link_loss']
                continue

            # Residual-bw (kbits/sec): 9
            m = p37.match(line)
            if m:
                merge_dict['residual_bw'] = int(m.groupdict()['res'])
                continue

            # Available-bw (kbits/sec): 9
            m = p38.match(line)
            if m:
                merge_dict['available_bw'] = int(m.groupdict()['available_bw'])
                continue

            # Utilized-bw (kbits/sec): 9
            m = p39.match(line)
            if m:
                merge_dict['utilized_bw'] = int(m.groupdict()['utilized_bw'])
                continue

            # Max-unreserv-link-bw (kbits/sec):
            m = p40.match(line)
            if m:
                unreserv_srlg_link = merge_dict.setdefault('max_unreserv_link_bw', [])
                continue

            # 0x4C.0x69.0x6E.0x6B.0x20.0x4F.0x6E.0x65.0x20.0x54.0x77
            m = p41_1.match(line)
            if m:
                if not link_attr:
                    merge_dict['opaque_link_attr'] = ' '.join(
                        filter(None, [merge_dict.get('opaque_link_attr'), line]))
                continue

            # SRLG:
            m = p42.match(line)
            if m:
                unreserv_srlg_link = merge_dict.setdefault('srlg', [])
                continue

            # 18         4608       1184256    303174144
            m = p43.match(line)
            if m:
                if not link_attr:
                    line1 = list(filter(None, line.split(' ')))
                    for items in line1:
                        unreserv_srlg_link.append(int(items))
                continue

            # Link Attributes of Group 0x1:
            m = p44.match(line)
            if m:
                link_attr = True
                continue

            # 0x00000001 0x00000002 0x00000004 0x00000008
            m = p46.match(line)
            if m:
                if not link_attr:
                    merge_dict['extended_admin_group'] = ' '.join(
                        filter(None, [merge_dict.get('extended_admin_group'), line]))
                continue

        return parsed_dict
