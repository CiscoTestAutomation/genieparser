''' show_arp.py

IOSXE parsers for the following show commands:
    * show arp
    * show arp <WORD>
    * show arp vrf <vrf>
    * show arp vrf <vrf> <WORD>
    * show ip arp
    * show ip arp summary
    * show ip traffic
    * show arp application
    * show arp summary
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

# parser utils
from genie.libs.parser.utils.common import Common


# =============================================
# Parser for 'show arp [vrf <WORD>] <WORD>'
# =============================================

class ShowArpSchema(MetaParser):
    """Schema for show arp
                  show arp <WORD>
                  show arp vrf <vrf>
                  show arp vrf <vrf> <WORD>
    """

    schema = {
        'interfaces': {
            Any(): {
                'ipv4': {
                    'neighbors': {     
                        Any(): {
                            'ip': str,
                            'link_layer_address': str,
                            'origin': str,
                            'age': str,
                            'type': str,
                            'protocol': str
                        },
                    }
                }
            },
        }
    }


class ShowArp(ShowArpSchema):
    """ Parser for show arp
                  show arp <WROD>
                  show arp vrf <vrf>
                  show arp vrf <vrf> <WROD> """

    cli_command = ['show arp','show arp vrf {vrf}','show arp vrf {vrf} {intf_or_ip}','show arp {intf_or_ip}']

    def cli(self, vrf='', intf_or_ip='', cmd=None, output=None):
        if output is None:
            if not cmd:
                cmd = self.cli_command[0]
                if vrf and not intf_or_ip:
                    cmd = self.cli_command[1].format(vrf=vrf)
                if vrf and intf_or_ip:
                    cmd = self.cli_command[2].format(vrf=vrf,intf_or_ip=intf_or_ip)
                if not vrf and intf_or_ip:
                    cmd = self.cli_command[3].format(intf_or_ip=intf_or_ip)

            out = self.device.execute(cmd)
        else:
            out = output

        # initial regexp pattern
        p1 = re.compile(r'^(?P<protocol>\w+) +(?P<address>[\d\.\:]+) +(?P<age>[\d\-]+) +'
                         '(?P<mac>[\w\.]+) +(?P<type>\w+) +(?P<interface>[\w\.\/\-]+)$')
        # initial variables
        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # Internet  192.168.234.1           -   58bf.eab6.2f51  ARPA   Vlan100
            m = p1.match(line)
            if m:
                group = m.groupdict()
                address = group['address']
                interface = group['interface']
                final_dict = ret_dict.setdefault('interfaces', {}).setdefault(
                    interface, {}).setdefault('ipv4', {}).setdefault(
                    'neighbors', {}).setdefault(address, {})
                
                final_dict['ip'] = address
                final_dict['link_layer_address'] = group['mac']
                final_dict['age'] = group['age']
                if group['age'] == '-':
                    final_dict['origin'] = 'static'
                else:
                    final_dict['origin'] = 'dynamic'

                final_dict['type'] = group['type']
                final_dict['protocol'] = group['protocol']
                continue

        return ret_dict

# =====================================
# Schema for 'show ip arp summary'
# =====================================
class ShowIpArpSummarySchema(MetaParser):
    """Schema for show ip arp summary"""

    schema = {
        'total_entries': int,
        'incomp_entries': int,
        }

# =====================================
# Parser for 'show ip arp summary'
# =====================================
class ShowIpArpSummary(ShowIpArpSummarySchema):
    """Parser for:
        show ip arp summary
        parser class - implements detail parsing mechanisms for cli,xml and yang output.
    """
    cli_command = 'show ip arp summary'
    def cli(self,output=None):
        if output is None:
            # excute command to get output
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # 40 IP ARP entries, with 0 of them incomplete
        p1 = re.compile(r'^(?P<total_entries>\w+) +IP +ARP +entries, +with '
            '+(?P<incomp_entries>\w+) +of +them +incomplete$')

        # initial variables
        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                ret_dict['total_entries'] = int(m.groupdict()['total_entries'])
                ret_dict['incomp_entries'] = int(m.groupdict()['incomp_entries'])
                continue

        return ret_dict

# =====================================
# Schema for 'show ip traffic'
# =====================================
class ShowIpTrafficSchema(MetaParser):
    """Schema for show ip traffic"""

    schema = {
        'arp_statistics': {
            'arp_in_requests': int,
            'arp_in_replies': int,
            'arp_in_reverse': int,
            'arp_in_other': int,
            'arp_out_requests': int,
            'arp_out_replies': int,
            'arp_out_proxy': int,
            'arp_out_reverse': int,
            'arp_drops_input_full': int,
        },
        'ip_statistics': {
            'ip_rcvd_total': int,
            'ip_rcvd_local_destination': int,
            'ip_rcvd_format_errors': int,
            'ip_rcvd_checksum_errors': int,
            'ip_rcvd_bad_hop': int,
            'ip_rcvd_unknwn_protocol': int,
            'ip_rcvd_not_gateway': int,
            'ip_rcvd_sec_failures': int,
            'ip_rcvd_bad_optns': int,
            'ip_rcvd_with_optns': int,
            'ip_opts_end': int,
            'ip_opts_nop': int,
            'ip_opts_basic_security': int,
            'ip_opts_loose_src_route': int,
            'ip_opts_timestamp': int,
            'ip_opts_extended_security': int,
            'ip_opts_record_route': int,
            'ip_opts_strm_id': int,
            'ip_opts_strct_src_route': int,
            'ip_opts_alert': int,
            'ip_opts_cipso': int,
            'ip_opts_ump': int,
            'ip_opts_other': int,
            Optional('ip_opts_ignored'): int,
            'ip_frags_reassembled': int,
            'ip_frags_timeouts': int,
            'ip_frags_no_reassembled': int,
            'ip_frags_fragmented': int,
            Optional('ip_frags_fragments'): int,
            'ip_frags_no_fragmented': int,
            Optional('ip_frags_invalid_hole'): int,
            'ip_bcast_received': int,
            'ip_bcast_sent': int,
            'ip_mcast_received': int,
            'ip_mcast_sent': int,
            'ip_sent_generated': int,
            'ip_sent_forwarded': int,
            'ip_drop_encap_failed': int,
            'ip_drop_unresolved': int,
            'ip_drop_no_adj': int,
            'ip_drop_no_route': int,
            'ip_drop_unicast_rpf': int,
            'ip_drop_forced_drop': int,
            Optional('ip_drop_unsupp_address'): int,
            'ip_drop_opts_denied': int,
            Optional('ip_drop_src_ip'): int,
        },
        'icmp_statistics': {
            'icmp_received_format_errors': int,
            'icmp_received_checksum_errors': int,
            'icmp_received_redirects': int,
            'icmp_received_unreachable': int,
            'icmp_received_echo': int,
            'icmp_received_echo_reply': int,
            'icmp_received_mask_requests': int,
            'icmp_received_mask_replies': int,
            'icmp_received_quench': int,
            'icmp_received_parameter': int,
            'icmp_received_timestamp': int,
            Optional('icmp_received_timestamp_replies'): int,
            'icmp_received_info_request': int,
            'icmp_received_other': int,
            'icmp_received_irdp_solicitations': int,
            'icmp_received_irdp_advertisements': int,
            Optional('icmp_received_time_exceeded'): int,
            Optional('icmp_received_info_replies'): int,
            'icmp_sent_redirects': int,
            'icmp_sent_unreachable': int,
            'icmp_sent_echo': int,
            'icmp_sent_echo_reply': int,
            'icmp_sent_mask_requests': int,
            'icmp_sent_mask_replies': int,
            'icmp_sent_quench': int,
            'icmp_sent_timestamp': int,
            Optional('icmp_sent_timestamp_replies'): int,
            Optional('icmp_sent_info_reply'): int,
            Optional('icmp_sent_time_exceeded'): int,
            'icmp_sent_parameter_problem': int,
            'icmp_sent_irdp_solicitations': int,
            'icmp_sent_irdp_advertisements': int,
        },
        'udp_statistics': {
            'udp_received_total': int,
            'udp_received_udp_checksum_errors': int,
            'udp_received_no_port': int,
            Optional('udp_received_finput'): int,
            'udp_sent_total': int,
            'udp_sent_fwd_broadcasts': int,
        },
        'ospf_statistics': {
            Optional('ospf_traffic_cntrs_clear'): str,
            'ospf_received_total': int,
            'ospf_received_checksum_errors': int,
            'ospf_received_hello': int,
            'ospf_received_database_desc': int,
            'ospf_received_link_state_req': int,
            'ospf_received_lnk_st_updates': int,
            'ospf_received_lnk_st_acks': int,
            'ospf_sent_total': int,
            'ospf_sent_hello': int,
            'ospf_sent_database_desc': int,
            'ospf_sent_lnk_st_acks': int,
            'ospf_sent_lnk_st_updates': int,
            'ospf_sent_lnk_st_acks': int,
        },
        'pimv2_statistics': {
            'pimv2_total': str,
            'pimv2_checksum_errors': int,
            'pimv2_format_errors': int,
            'pimv2_registers': str,
            'pimv2_non_rp': int,
            'pimv2_non_sm_group': int,
            'pimv2_registers_stops': str,
            'pimv2_hellos': str,
            'pimv2_join_prunes': str,
            'pimv2_asserts': str,
            'pimv2_grafts': str,
            'pimv2_bootstraps': str,
            'pimv2_candidate_rp_advs': str,
            Optional('pimv2_queue_drops'): int,
            'pimv2_state_refresh': str,
        },
        'igmp_statistics': {
            'igmp_total': str,
            'igmp_format_errors': str,
            'igmp_checksum_errors': str,
            'igmp_host_queries': str,
            'igmp_host_reports': str,
            'igmp_host_leaves': str,
            'igmp_dvmrp': str,
            'igmp_pim': str,
            Optional('igmp_queue_drops'): int,
        },
        'tcp_statistics': {
            'tcp_received_total': int,
            'tcp_received_checksum_errors': int,
            'tcp_received_no_port': int,
            'tcp_sent_total': int,
        },
        'eigrp_ipv4_statistics': {
            'eigrp_ipv4_received_total': int,
            'eigrp_ipv4_sent_total': int,
        },
        'bgp_statistics': {
            'bgp_received_total': int,
            'bgp_received_opens': int,
            'bgp_received_notifications': int,
            'bgp_received_updates': int,
            'bgp_received_keepalives': int,
            'bgp_received_route_refresh': int,
            'bgp_received_unrecognized': int,
            'bgp_sent_total': int,
            'bgp_sent_opens': int,
            'bgp_sent_notifications': int,
            'bgp_sent_updates': int,
            'bgp_sent_keepalives': int,
            'bgp_sent_route_refresh': int,
        },
    }

# =====================================
# Parser for 'show ip traffic'
# =====================================
class ShowIpTraffic(ShowIpTrafficSchema):
    """Parser for:
        show ip traffic
        parser class - implements detail parsing mechanisms for cli,xml and yang output.
    """
    cli_command = 'show ip traffic'
    def cli(self,output=None):
        if output is None:
            # excute command to get output
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # ARP statistics:
        p1 = re.compile(r'^ARP +statistics:')

        # Rcvd: 2020 requests, 764 replies, 0 reverse, 0 other
        p2 = re.compile(r'^Rcvd: +(?P<arp_in_requests>\d+) +requests,'
            ' +(?P<arp_in_replies>\d+) +replies, +(?P<arp_in_reverse>\d+)'
            ' +reverse, +(?P<arp_in_other>\d+) +other$')

        # Sent: 29 requests, 126 replies (2 proxy), 0 reverse
        p3 = re.compile(r'^Sent: +(?P<arp_out_requests>\d+) +requests,'
            ' +(?P<arp_out_replies>\d+) +replies +\((?P<arp_out_proxy>[\w]+)'
            ' +proxy\), +(?P<arp_out_reverse>\d+) +reverse$')

        # Drop due to input queue full: 0
        p4 = re.compile(r'^Drop +due +to +input +queue +full:'
            ' +(?P<arp_drops>\w+)$')

        # IP statistics:
        p5 = re.compile(r'^IP +statistics:')

        # Rcvd:  17780 total, 110596 local destination
        p6 = re.compile(r'^Rcvd: +(?P<ip_rcvd_total>\d+) +total,'
            ' +(?P<ip_rcvd_local_destination>\d+)'
            ' +local +destination$')

        # 0 format errors, 0 checksum errors, 0 bad hop count
        p7 = re.compile(r'^(?P<ip_rcvd_format_errors>\d+) +format +errors,'
            ' +(?P<ip_rcvd_checksum_errors>\d+)'
            ' +checksum +errors, +(?P<ip_rcvd_bad_hop>\d+) +bad +hop +count$')

        # 0 unknown protocol, 5 not a gateway
        p8 = re.compile(r'^(?P<ip_rcvd_unknwn_protocol>\d+) +unknown +protocol,'
            ' +(?P<ip_rcvd_not_gateway>\d+)'
            ' +not +a +gateway$')

        # 0 security failures, 0 bad options, 12717 with options
        p9 = re.compile(r'^(?P<ip_rcvd_sec_failures>\d+) +security +failures,'
            ' +(?P<ip_rcvd_bad_optns>\d+)'
            ' +bad options, +(?P<ip_rcvd_with_optns>\d+) +with +options$')

        # Opts:  0 end, 0 nop, 0 basic security, 0 loose source route
        p10 = re.compile(r'^Opts: +(?P<ip_opts_end>\d+) +end,'
            ' +(?P<ip_opts_nop>\d+)'
            ' +nop, +(?P<ip_opts_basic_security>\d+) +basic +security, '
            '+(?P<ip_opts_loose_src_route>\d+) +loose +source +route$')

        # 0 timestamp, 0 extended security, 0 record route
        p11 = re.compile(r'^(?P<ip_opts_timestamp>\d+) +timestamp,'
            ' +(?P<ip_opts_extended_security>\d+)'
            ' +extended +security, +(?P<ip_opts_record_route>\d+)'
            ' +record +route$')

        # 0 stream ID, 0 strict source route, 12717 alert, 0 cipso, 0 ump
        p12 = re.compile(r'^(?P<ip_opts_strm_id>\d+) +stream +ID,'
            ' +(?P<ip_opts_strct_src_route>\d+)'
            ' +strict +source +route, +(?P<ip_opts_alert>\d+) +alert, '
            '+(?P<ip_opts_cipso>\d+) +cipso, +(?P<ip_opts_ump>\d+) +ump$')

        # 0 other, 0 ignored
        p13 = re.compile(r'^(?P<ip_opts_other>\d+) +other'
            '(, +(?P<ip_opts_ignored>\d+) +ignored)?$')

        # Frags: 0 reassembled, 0 timeouts, 0 couldn't reassemble
        p14 = re.compile(r'^Frags: +(?P<ip_frags_reassembled>\d+) +reassembled,'
            ' +(?P<ip_frags_timeouts>\d+)'
            ' +timeouts, +(?P<ip_frags_no_reassembled>\d+)'
            ' +couldn\'t +reassemble$')

        # 1 fragmented, 5 fragments, 0 couldn't fragment
        # 0 fragmented, 0 couldn't fragment
        p15 = re.compile(r'^(?P<ip_frags_fragmented>\d+) +fragmented,'
            '( +(?P<ip_frags_fragments>\d+) +fragments,)?'
            ' +(?P<ip_frags_no_fragmented>\d+)'
            ' +couldn\'t +fragment$')

        # 0 invalid hole
        p16 = re.compile(r'^(?P<ip_frags_invalid_hole>\d+) +invalid hole$')

        # Bcast: 33324 received, 5 sent
        p17 = re.compile(r'^Bcast: +(?P<ip_bcast_received>\d+) +received,'
            ' +(?P<ip_bcast_sent>\d+) +sent$')

        # Mcast: 144833 received, 66274 sent
        p18 = re.compile(r'^Mcast: +(?P<ip_mcast_received>\d+) +received,'
            ' +(?P<ip_mcast_sent>\d+) +sent$')

        # Sent:  85543 generated, 1654728 forwarded
        p19 = re.compile(r'^Sent: +(?P<ip_sent_generated>\d+) +generated,'
            ' +(?P<ip_sent_forwarded>\d+) +forwarded$')

        # Drop:  8 encapsulation failed, 0 unresolved, 20 no adjacency
        p20 = re.compile(r'^Drop: +(?P<ip_drop_encap_failed>\d+) +encapsulation'
            ' +failed, +(?P<ip_drop_unresolved>\d+)'
            ' +unresolved, +(?P<ip_drop_no_adj>\d+) +no +adjacency$')

        # 19 no route, 0 unicast RPF, 0 forced drop, 0 unsupported-addr
        # 0 no route, 0 unicast RPF, 0 forced drop
        p21 = re.compile(r'^(?P<ip_drop_no_route>\d+) +no +route,'
            ' +(?P<ip_drop_unicast_rpf>\d+)'
            ' +unicast +RPF, +(?P<ip_drop_forced_drop>\d+) +forced +drop'
            '(, +(?P<ip_drop_unsupp_address>\d+) +unsupported-addr)?$')

        # 0 options denied, 0 source IP address zero
        p22 = re.compile(r'^(?P<ip_drop_opts_denied>\d+) +options +denied(,'
            ' +(?P<ip_drop_src_ip>\d+) +source +IP +address +zero)?$')

        # ICMP statistics:
        p23 = re.compile(r'^ICMP +statistics:')

        # Rcvd: 0 format errors, 0 checksum errors, 0 redirects, 0 unreachable
        p24 = re.compile(r'^Rcvd: +(?P<icmp_received_format_errors>\d+) +format '
            '+errors, +(?P<icmp_received_checksum_errors>\d+) +checksum +errors, '
            '+(?P<icmp_received_redirects>\d+) +redirects, '
            '+(?P<icmp_received_unreachable>\d+) +unreachable$')

        # 284 echo, 9 echo reply, 0 mask requests, 0 mask replies, 0 quench
        # 43838 echo, 713 echo reply, 0 mask requests, 0 mask replies, 0 quench
        p25 = re.compile(r'^(?P<icmp_received_echo>\d+) +echo,'
            ' +(?P<icmp_received_echo_reply>\d+)'
            ' +echo +reply, +(?P<icmp_received_mask_requests>\d+) +mask'
            ' +requests, +(?P<icmp_received_mask_replies>\d+) +mask +replies, '
            '+(?P<icmp_received_quench>\d+) +quench$')

        # 0 parameter, 0 timestamp, 0 timestamp replies, 0 info request, 0 other
        # 0 parameter, 0 timestamp, 0 info request, 0 other
        p26 = re.compile(r'^(?P<icmp_received_parameter>\d+) +parameter,'
            ' +(?P<icmp_received_timestamp>\d+)'
            ' +timestamp(, +(?P<icmp_received_timestamp_replies>\d+) +timestamp'
            ' +replies)?, +(?P<icmp_received_info_request>\d+) +info +request,'
            ' +(?P<icmp_received_other>\d+) +other$')

        # 0 irdp solicitations, 0 irdp advertisements
        p27 = re.compile(r'^(?P<icmp_received_irdp_solicitations>\d+) '
            '+irdp +solicitations, +(?P<icmp_received_irdp_advertisements>\d+)'
            ' +irdp +advertisements$')

        # 0 time exceeded, 0 info replies
        p28 = re.compile(r'^(?P<icmp_received_time_exceeded>\d+) '
            '+time +exceeded, +(?P<icmp_received_info_replies>\d+)'
            ' +info +replies$')

        # Sent: 0 redirects, 14 unreachable, 9 echo, 134 echo reply
        p29 = re.compile(r'^Sent: +(?P<icmp_sent_redirects>\d+) +redirects, '
            '+(?P<icmp_sent_unreachable>\d+) +unreachable,'
            ' +(?P<icmp_sent_echo>\d+) +echo, +(?P<icmp_sent_echo_reply>\d+) '
            '+echo +reply$')

        # 0 mask requests, 0 mask replies, 0 quench, 0 timestamp, 0 timestamp replies
        # 0 mask requests, 0 mask replies, 0 quench, 0 timestamp
        p30 = re.compile(r'^(?P<icmp_sent_mask_requests>\d+) +mask +requests, '
            '+(?P<icmp_sent_mask_replies>\d+)'
            ' +mask +replies, +(?P<icmp_sent_quench>\d+) +quench, '
            '+(?P<icmp_sent_timestamp>\d+) +timestamp'
            '(, +(?P<icmp_sent_timestamp_replies>\d+) +timestamp +replies)?$')

        # 0 info reply, 0 time exceeded, 0 parameter problem
        p31 = re.compile(r'^(?P<icmp_sent_info_reply>\d+) +info +reply, '
            '+(?P<icmp_sent_time_exceeded>\d+) +time +exceeded, '
            '+(?P<icmp_sent_parameter_problem>\d+) +parameter +problem$')

        # 0 irdp solicitations, 0 irdp advertisements
        p32 = re.compile(r'^(?P<icmp_sent_irdp_solicitations>\d+) +irdp '
            '+solicitations, +(?P<icmp_sent_irdp_advertisements>\d+)'
            ' +irdp +advertisements$')

        # UDP statistics:
        p33 = re.compile(r'^UDP +statistics:')

        # Rcvd: 62515 total, 0 checksum errors, 15906 no port 0 finput
        # Rcvd: 682217 total, 0 checksum errors, 289579 no port
        p34 = re.compile(r'^Rcvd: +(?P<udp_received_total>\d+) +total,'
            ' +(?P<udp_received_udp_checksum_errors>\d+) +checksum +errors,'
            ' +(?P<udp_received_no_port>\d+) +no port( +(?P<udp_received_finput>\d+) '
            '+finput)?$')

        # Sent: 41486 total, 0 forwarded broadcasts
        p35 = re.compile(r'^Sent: +(?P<udp_sent_total>\d+) +total, '
            '+(?P<udp_sent_fwd_broadcasts>\d+) +forwarded +broadcasts$')

        # OSPF statistics:
        p36 = re.compile(r'^OSPF +statistics:')

        # Last clearing of OSPF traffic counters never
        p37 = re.compile(r'^Last +clearing +of +OSPF +traffic +counters '
            '+(?P<ospf_traffic_cntrs_clear>\w+)$')

        # Rcvd: 16222 total, 0 checksum errors
        p38 = re.compile(r'^Rcvd: +(?P<ospf_received_total>\d+) +total, '
            '+(?P<ospf_received_checksum_errors>\d+) +checksum errors$')

        # 15153 hello, 20 database desc, 2 link state req
        p39 = re.compile(r'^(?P<ospf_received_hello>\d+) +hello, '
            '+(?P<ospf_received_database_desc>\d+)'
            ' +database +desc, +(?P<ospf_received_link_state_req>\d+) '
            '+link +state +req$')

        # 359 link state updates, 688 link state acks
        p40 = re.compile(r'^(?P<ospf_received_lnk_st_updates>\d+) +link '
            '+state +updates, +(?P<ospf_received_lnk_st_acks>\d+) +link '
            '+state +acks$')

        # Sent: 9456 total
        p41 = re.compile(r'^Sent: +(?P<sent_total>\d+) +total$')

        # 8887 hello, 30 database desc, 8 link state req
        p42 = re.compile(r'^(?P<ospf_sent_hello>\d+) +hello, '
            '+(?P<ospf_sent_database_desc>\d+)'
            ' +database +desc, +(?P<ospf_sent_lnk_st_acks>\d+) +link +state '
            '+req$')

        # 299 link state updates, 239 link state acks
        p43 = re.compile(r'^(?P<ospf_sent_lnk_st_updates>\d+) +link '
            '+state +updates, +(?P<ospf_sent_lnk_st_acks>\d+) +link '
            '+state +acks$')

        # PIMv2 statistics: Sent/Received
        p44 = re.compile(r'^PIMv2 +statistics: +Sent/Received')

        # Total: 7458/8859, 0 checksum errors, 0 format errors
        p45 = re.compile(r'^Total: +(?P<pimv2_total>[\d\/]+), '
            '+(?P<pimv2_checksum_errors>\d+) +checksum +errors, '
            '+(?P<pimv2_format_errors>\d+) +format +errors$')

        # Registers: 1/1 (0 non-rp, 0 non-sm-group), Register Stops: 1/1,  Hellos: 5011/5008
        p46 = re.compile(r'^Registers: +(?P<pimv2_registers>[\d\/]+) +'
            '\((?P<pimv2_non_rp>\d+) +non-rp, +(?P<pimv2_non_sm_group>\d+) '
            '+non-sm-group\), +Register +Stops:'
            ' +(?P<pimv2_registers_stops>[\d\/]+),'
            ' +Hellos: +(?P<pimv2_hellos>[\d\/]+)$')

        # Join/Prunes: 5/712, Asserts: 0/697, grafts: 0/2
        p47 = re.compile(r'^Join/Prunes: +(?P<pimv2_join_prunes>[\d\/]+), '
            '+Asserts: +(?P<pimv2_asserts>[\d\/]+), +grafts: '
            '+(?P<pimv2_grafts>[\d\/]+)$')

        # Bootstraps: 2088/2438, Candidate_RP_Advertisements: 350/0
        p48 = re.compile(r'^Bootstraps: +(?P<pimv2_bootstraps>[\d\/]+), '
            '+Candidate_RP_Advertisements:'
            ' +(?P<pimv2_candidate_rp_advs>[\d\/]+)$')

        # Queue drops: 0
        p49 = re.compile(r'^Queue drops: +(?P<pimv2_queue_drops>[\d]+)$')

        # State-Refresh: 0/0
        p50 = re.compile(r'^State-Refresh: +(?P<pimv2_state_refresh>[\d\/]+)$')

        # IGMP statistics: Sent/Received
        p51 = re.compile(r'^IGMP +statistics: +Sent/Received')

        # Total: 2832/4946, Format errors: 0/0, Checksum errors: 0/0
        p52 = re.compile(r'^Total: +(?P<igmp_total>[\d\/]+),'
            ' +Format +errors: +(?P<igmp_format_errors>[\d\/]+),'
            ' +Checksum +errors: +(?P<igmp_checksum_errors>[\d\/]+)$')

        # Host Queries: 2475/1414, Host Reports: 357/3525, Host Leaves: 0/5
        p53 = re.compile(r'^Host +Queries: +(?P<igmp_host_queries>[\d\/]+),'
            ' +Host +Reports: +(?P<igmp_host_reports>[\d\/]+),'
            ' +Host +Leaves: +(?P<igmp_host_leaves>[\d\/]+)$')

        # DVMRP: 0/0, PIM: 0/0
        p54 = re.compile(r'^DVMRP: +(?P<igmp_dvmrp>[\d\/]+), '
            '+PIM: +(?P<igmp_pim>[\d\/]+)$')

        # Queue drops: 0
        p55 = re.compile(r'^Queue drops: +(?P<igmp_queue_drops>[\d]+)$')

        # TCP statistics:
        p56 = re.compile(r'^TCP +statistics:')

        # Rcvd: 15396 total, 0 checksum errors, 0 no port
        p57 = re.compile(r'^Rcvd: +(?P<tcp_received_total>\d+) +total,'
            ' +(?P<tcp_received_checksum_errors>\d+) +checksum +errors,'
            ' +(?P<tcp_received_no_port>\d+) +no +port$')

        # Sent: 19552 total
        p58 = re.compile(r'^Sent: +(?P<tcp_sent_total>\d+) +total$')

        # EIGRP-IPv4 statistics:
        p59 = re.compile(r'^EIGRP-IPv4 +statistics:')

        # Rcvd: 4612 total
        p60 = re.compile(r'^Rcvd: +(?P<eigrp_ipv4_received_total>\d+) +total$')

        # Sent: 4611 total
        p61 = re.compile(r'^Sent: +(?P<eigrp_ipv4_sent_total>\d+) +total$')

        # BGP statistics:
        p62 = re.compile(r'^BGP +statistics:')

        # Rcvd: 2185 total, 6 opens, 0 notifications, 12 updates
        p63 = re.compile(r'^Rcvd: +(?P<bgp_received_total>\d+) +total,'
            ' +(?P<bgp_received_opens>\d+) +opens,'
            ' +(?P<bgp_received_notifications>\d+) +notifications,'
            ' +(?P<bgp_received_updates>\d+) +updates$')

        # 2167 keepalives, 0 route-refresh, 0 unrecognized
        p64 = re.compile(r'^(?P<bgp_received_keepalives>\d+) +keepalives, '
            '+(?P<bgp_received_route_refresh>\d+)'
            ' +route-refresh, +(?P<bgp_received_unrecognized>\d+)'
            ' +unrecognized$')

        # Sent: 2304 total, 6 opens, 2 notifications, 0 updates
        p65 = re.compile(r'^Sent: +(?P<bgp_sent_total>\d+) +total,'
            ' +(?P<bgp_sent_opens>\d+) +opens,'
            ' +(?P<bgp_sent_notifications>\d+) +notifications,'
            ' +(?P<bgp_sent_updates>\d+) +updates$')

        # 2296 keepalives, 0 route-refresh
        p66 = re.compile(r'^(?P<bgp_sent_keepalives>\d+) +keepalives, '
            '+(?P<bgp_sent_route_refresh>\d+) +route-refresh$')

        # initial variables
        ret_dict = {}
        category = ''
        location = ''

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                ret_dict.setdefault('arp_statistics', {})
                continue

            m = p2.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['arp_statistics'].update({k: \
                    int(v) for k, v in groups.items()})
                continue

            m = p3.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['arp_statistics'].update({k: \
                    int(v) for k, v in groups.items()})
                continue

            m = p4.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['arp_statistics']['arp_drops_input_full'] = int(
                    groups['arp_drops'])
                continue

            m = p5.match(line)
            if m:
                ret_dict.setdefault('ip_statistics', {})
                continue

            m = p6.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['ip_statistics'].update({k: \
                    int(v) for k, v in groups.items()})
                continue

            m = p7.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['ip_statistics'].update({k: \
                    int(v) for k, v in groups.items()})
                continue

            m = p8.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['ip_statistics'].update({k: \
                    int(v) for k, v in groups.items()})
                continue

            m = p9.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['ip_statistics'].update({k: \
                    int(v) for k, v in groups.items()})
                continue

            m = p10.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['ip_statistics'].update({k: \
                    int(v) for k, v in groups.items()})
                continue

            m = p11.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['ip_statistics'].update({k: \
                    int(v) for k, v in groups.items()})
                continue

            m = p12.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['ip_statistics'].update({k: \
                    int(v) for k, v in groups.items()})
                continue

            m = p13.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['ip_statistics'].update({k: \
                    int(v) for k, v in groups.items() if v})
                continue

            m = p14.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['ip_statistics'].update({k: \
                    int(v) for k, v in groups.items()})
                continue

            m = p15.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['ip_statistics'].update({k: \
                    int(v) for k, v in groups.items() if v})
                continue

            m = p16.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['ip_statistics'].update({k: \
                    int(v) for k, v in groups.items()})
                continue

            m = p17.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['ip_statistics'].update({k: \
                    int(v) for k, v in groups.items()})
                continue

            m = p18.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['ip_statistics'].update({k: \
                    int(v) for k, v in groups.items()})
                continue

            m = p19.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['ip_statistics'].update({k: \
                    int(v) for k, v in groups.items()})
                continue

            m = p20.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['ip_statistics'].update({k: \
                    int(v) for k, v in groups.items()})
                continue

            m = p21.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['ip_statistics'].update({k: \
                    int(v) for k, v in groups.items() if v})
                continue

            m = p22.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['ip_statistics'].update({k: \
                    int(v) for k, v in groups.items() if v})
                continue

            m = p23.match(line)
            if m:
                ret_dict.setdefault('icmp_statistics', {})
                category = ''
                continue

            m = p24.match(line)
            if m:
                category = 'rcvd'
                groups = m.groupdict()
                ret_dict['icmp_statistics'].update({k: \
                    int(v) for k, v in groups.items()})
                continue

            m = p25.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['icmp_statistics'].update({k: \
                    int(v) for k, v in groups.items()})
                continue

            m = p26.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['icmp_statistics'].update({k: \
                    int(v) for k, v in groups.items() if v})
                continue

            m = p27.match(line)
            if m and category=='rcvd':
                groups = m.groupdict()
                ret_dict['icmp_statistics'].update({k: \
                    int(v) for k, v in groups.items()})
                continue

            m = p28.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['icmp_statistics'].update({k: \
                    int(v) for k, v in groups.items()})
                continue

            m = p29.match(line)
            if m:
                category = 'sent'
                groups = m.groupdict()
                ret_dict['icmp_statistics'].update({k: \
                    int(v) for k, v in groups.items()})
                continue

            m = p30.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['icmp_statistics'].update({k: \
                    int(v) for k, v in groups.items() if v})
                continue

            m = p31.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['icmp_statistics'].update({k: \
                    int(v) for k, v in groups.items()})
                continue

            m = p32.match(line)
            if m and category=='sent':
                groups = m.groupdict()
                ret_dict['icmp_statistics'].update({k: \
                    int(v) for k, v in groups.items()})
                continue

            m = p33.match(line)
            if m:
                ret_dict.setdefault('udp_statistics', {})
                location = 'udp_statistics'
                continue

            m = p34.match(line)
            if m and location == 'udp_statistics':
                groups = m.groupdict()
                ret_dict['udp_statistics'].update({k: \
                    int(v) for k, v in groups.items() if v})
                continue

            m = p35.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['udp_statistics'].update({k: \
                    int(v) for k, v in groups.items()})
                location = ''
                continue

            m = p36.match(line)
            if m:
                ret_dict.setdefault('ospf_statistics', {})
                category = 'rcvd'
                location = 'ospf_statistics'
                continue

            m = p37.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['ospf_statistics'].update({k: \
                    str(v) for k, v in groups.items()})
                continue

            m = p38.match(line)
            if m and category=='rcvd':
                groups = m.groupdict()
                ret_dict['ospf_statistics'].update({k: \
                    int(v) for k, v in groups.items()})
                continue

            m = p39.match(line)
            if m and category=='rcvd':
                groups = m.groupdict()
                ret_dict['ospf_statistics'].update({k: \
                    int(v) for k, v in groups.items()})
                continue

            m = p40.match(line)
            if m and category=='rcvd':
                groups = m.groupdict()
                ret_dict['ospf_statistics'].update({k: \
                    int(v) for k, v in groups.items()})
                continue

            m = p41.match(line)
            if m:
                groups = m.groupdict()
                if location == 'ospf_statistics':
                    category = 'sent'
                    sdict = ret_dict['ospf_statistics']
                    key = 'ospf_sent_total'
                elif location == 'tcp_statistics':
                    sdict = ret_dict['tcp_statistics']
                    key = 'tcp_sent_total'
                elif location == 'eigrp_ipv4_statistics':
                    sdict = ret_dict['eigrp_ipv4_statistics']
                    key = 'eigrp_ipv4_sent_total'
                else:
                    continue
                sdict[key] = int(groups['sent_total'])
                continue

            m = p42.match(line)
            if m and category=='sent':
                groups = m.groupdict()
                ret_dict['ospf_statistics'].update({k: \
                    int(v) for k, v in groups.items()})
                continue

            m = p43.match(line)
            if m and category=='sent':
                groups = m.groupdict()
                ret_dict['ospf_statistics'].update({k: \
                    int(v) for k, v in groups.items()})
                continue

            m = p44.match(line)
            if m:
                ret_dict.setdefault('pimv2_statistics', {})
                continue

            m = p45.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['pimv2_statistics']['pimv2_total'] = \
                    str(groups['pimv2_total'])
                ret_dict['pimv2_statistics']['pimv2_checksum_errors'] = \
                    int(groups['pimv2_checksum_errors'])
                ret_dict['pimv2_statistics']['pimv2_format_errors'] = \
                    int(groups['pimv2_format_errors'])
                continue

            m = p46.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['pimv2_statistics']['pimv2_registers'] = \
                    str(groups['pimv2_registers'])
                ret_dict['pimv2_statistics']['pimv2_non_rp'] = \
                    int(groups['pimv2_non_rp'])
                ret_dict['pimv2_statistics']['pimv2_non_sm_group'] = \
                    int(groups['pimv2_non_sm_group'])
                ret_dict['pimv2_statistics']['pimv2_registers_stops'] = \
                    str(groups['pimv2_registers_stops'])
                ret_dict['pimv2_statistics']['pimv2_hellos'] = \
                    str(groups['pimv2_hellos'])
                continue

            m = p47.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['pimv2_statistics'].update({k: \
                    str(v) for k, v in groups.items()})
                continue

            m = p48.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['pimv2_statistics'].update({k: \
                    str(v) for k, v in groups.items()})
                continue

            m = p49.match(line)
            if m and 'igmp_statistics' not in ret_dict:
                groups = m.groupdict()
                ret_dict['pimv2_statistics'].update({k: \
                    int(v) for k, v in groups.items()})
                continue

            m = p50.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['pimv2_statistics'].update({k: \
                    str(v) for k, v in groups.items()})
                continue

            m = p51.match(line)
            if m:
                ret_dict.setdefault('igmp_statistics', {})
                continue

            m = p52.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['igmp_statistics'].update({k: \
                    str(v) for k, v in groups.items()})
                continue

            m = p53.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['igmp_statistics'].update({k: \
                    str(v) for k, v in groups.items()})
                continue

            m = p54.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['igmp_statistics'].update({k: \
                    str(v) for k, v in groups.items()})
                continue

            m = p55.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['igmp_statistics']['igmp_queue_drops'] = \
                    int(groups['igmp_queue_drops'])
                continue

            m = p56.match(line)
            if m:
                ret_dict.setdefault('tcp_statistics', {})
                location = 'tcp_statistics'
                continue

            m = p57.match(line)
            if m and location == 'tcp_statistics':
                groups = m.groupdict()
                ret_dict['tcp_statistics'].update({k: \
                    int(v) for k, v in groups.items()})
                continue

            m = p59.match(line)
            if m:
                ret_dict.setdefault('eigrp_ipv4_statistics', {})
                location = 'eigrp_ipv4_statistics'
                continue

            m = p60.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['eigrp_ipv4_statistics'].update({k: \
                    int(v) for k, v in groups.items()})
                continue

            m = p62.match(line)
            if m:
                ret_dict.setdefault('bgp_statistics', {})
                continue

            m = p63.match(line)
            if m:
                category = 'rcvd'
                groups = m.groupdict()
                ret_dict['bgp_statistics'].update({k: \
                    int(v) for k, v in groups.items()})
                continue

            m = p64.match(line)
            if m and category == 'rcvd':
                groups = m.groupdict()
                ret_dict['bgp_statistics'].update({k: \
                    int(v) for k, v in groups.items()})
                continue

            m = p65.match(line)
            if m:
                category = 'sent'
                groups = m.groupdict()
                ret_dict['bgp_statistics'].update({k: \
                    int(v) for k, v in groups.items()})
                continue

            m = p66.match(line)
            if m and category == 'sent':
                groups = m.groupdict()
                ret_dict['bgp_statistics'].update({k: \
                    int(v) for k, v in groups.items()})
                continue

        return ret_dict


# ===========================================================
# Parser for 'show arp application'
# ===========================================================
class ShowArpApplicationSchema(MetaParser):
    """
    Schema for show arp application
    """
    
    schema = {
        'num_of_clients_registered': int,
        'applications': {
            Any(): {
                'id': int,
                'num_of_subblocks': int
            }
        }
    }

class ShowArpApplication(ShowArpApplicationSchema):
    """
    Parser for show arp application
    """
    
    cli_command = 'show arp application'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        
        # initial variables
        ret_dict = {}
        
        # Number of clients registered: 16
        p1 = re.compile(r'^\s*Number +of +clients +registered: +' \
                '(?P<num_of_clients>\d+)$')

        # ASR1000-RP SPA Ether215 10024
        p2 = re.compile(r'^(?P<application_name>[\w\W]{0,20})(?P<id>\d+)\s+(?P<num_of_subblocks>\d+)$')

        for line in out.splitlines():
            line = line.strip()
            # Number of clients registered: 16
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('num_of_clients_registered', \
                    int(group['num_of_clients']))
                continue
            
            # ASR1000-RP SPA Ether215 10024
            m = p2.match(line)
            if m:
                application = ret_dict.setdefault('applications', {})
                group = m.groupdict()
                application[group['application_name'].rstrip()] = {'id': \
                    int(group['id']), 'num_of_subblocks': \
                    int(group['num_of_subblocks'])}
                continue
        return ret_dict


# ========================================
# Parser for 'show arp summary'
# ========================================
class ShowArpSummarySchema(MetaParser):
    """
    Schema for 'show arp summary'
    """

    schema = {
        'total_num_of_entries':{
            Any(): int
        },
        'interface_entries': {
            Any(): int
        },
        Optional('maximum_entries'): {
            Any(): int
        },
        Optional('arp_entry_threshold'): int,
        Optional('permit_threshold'): int
    }

class ShowArpSummary(ShowArpSummarySchema):
    """ Parser for 'show arp summary'"""
    
    cli_command = "show arp summary"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        
        # initial variables
        ret_dict = {}

        # Total number of entries in the ARP table: 1233
        p1 = re.compile(r'^Total +number +of +entries +in +the +ARP +table: +' \
                '(?P<arp_table_entries>\d+)\.$')
        
        # Total number of Dynamic ARP entries: 1123
        p2 = re.compile(r'^Total +number +of +(?P<entry_name>[\S\s]+): +' \
                '(?P<num_of_entries>\d+)\.$')

        # GigabitEthernet0/0/4  4
        p3 = re.compile(r'^(?P<interface_name>[\w\/\.]+) +(?P<entry_count>\d+)')

        # Learn ARP Entry Threshold is 409600 and Permit Threshold is 486400.
        p4 = re.compile(r'^Learn +ARP +Entry +Threshold +is +' \
            '(?P<arp_entry_threshold>\d+) +and +Permit +Threshold +is +' \
            '(?P<permit_threshold>\d+).?$')

        # Maximum limit of Learn ARP entry : 512000.
        p5 = re.compile(r'^(?P<maximum_entries_name>[\w\W]+) +: +' \
            '(?P<maximum_entries>\d+).$')

        for line in out.splitlines():
            line = line.strip()
            # Total number of entries in the ARP table: 1233
            m = p1.match(line)
            if m:
                group = m.groupdict()
                total_num_of_entries = ret_dict.setdefault( \
                    'total_num_of_entries', {})
                total_num_of_entries.update({'arp_table_entries': 
                    int(group['arp_table_entries'])})
                continue
            
            # Total number of Dynamic ARP entries: 1123
            m = p2.match(line)
            if m:
                group = m.groupdict()
                total_num_of_entries = ret_dict.setdefault( \
                    'total_num_of_entries', {})
                key = group['entry_name'].replace(' ', '_').lower()
                total_num_of_entries.update({key: int(group['num_of_entries'])})
                continue

            # GigabitEthernet0/0/4  4
            m = p3.match(line)
            if m:
                group = m.groupdict()
                interfaces = ret_dict.setdefault('interface_entries', {})
                interfaces.update({Common.convert_intf_name(group['interface_name']) : 
                    int(group['entry_count'])})
                continue

            # Learn ARP Entry Threshold is 409600 and Permit Threshold is 486400.
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'arp_entry_threshold' : int(group['arp_entry_threshold'])})
                ret_dict.update({'permit_threshold' : int(group['permit_threshold'])})
                continue

            # Maximum limit of Learn ARP entry : 512000.
            m = p5.match(line)
            if m:
                group = m.groupdict()
                key = group['maximum_entries_name'].replace(' ', '_').lower()
                maximum_entries = ret_dict.setdefault('maximum_entries', {})
                maximum_entries.update({key : int(group['maximum_entries'])})

        return ret_dict
