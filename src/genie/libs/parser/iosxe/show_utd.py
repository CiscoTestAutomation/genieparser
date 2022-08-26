# Python
import re

# Genie
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional

class ShowSdwanUtdEngineSchema(MetaParser):
    ''' Schema for show sdwan utd engine'''
    schema = {
        'version': str,
        'profile': str,
        'status': str,
        'reason': str,
        'memory_usage': float,
        'memory_status': str,
        Optional('engine_id'): {
            int: {
                'running': str,
                'status': str,
                'reason': str
                }
            }
        }


class ShowSdwanUtdEngine(ShowSdwanUtdEngineSchema):

    """ Parser for "show sdwan utd engine" """

    cli_command = "show sdwan utd engine"

    def cli(self, output=None):

        # if the user does not provide output to the parser
        # we need to get it from the device
        if not output:
            output = self.device.execute(self.cli_command)
        
        # utd-oper-data utd-engine-status version 1.0.6_SV2.9.13.0_XE17.3
        # utd-oper-data utd-engine-status profile Cloud-Medium
        # utd-oper-data utd-engine-status status utd-oper-status-green
        # utd-oper-data utd-engine-status reason ""
        # utd-oper-data utd-engine-status memory-usage 11.3
        # utd-oper-data utd-engine-status memory-status utd-oper-status-green
        p1 = re.compile(r'utd-oper-data utd-engine-status +(?P<key>[\S]+) +(?P<value>[\s\S]+)')

        # ID  RUNNING  STATUS                 REASON
        # 1   true     utd-oper-status-green 
        # 2   true     utd-oper-status-green 
        p2 = re.compile(r'^(?P<id>[\d]+)[\s]+(?P<running>[\w]+)[\s]+(?P<status>[s\S]+\S)(?P<reason>($|[\s\S]+))')

        parsed_dict = {}
        for line in output.splitlines():
            line = line.strip()
    
            # utd-oper-data utd-engine-status version 1.0.6_SV2.9.13.0_XE17.3
            # utd-oper-data utd-engine-status profile Cloud-Medium
            # utd-oper-data utd-engine-status status utd-oper-status-green
            # utd-oper-data utd-engine-status reason ""
            # utd-oper-data utd-engine-status memory-usage 11.3
            # utd-oper-data utd-engine-status memory-status utd-oper-status-green
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                key = groups['key'].replace('-', '_').replace(' ', '_').lower()
                value = groups['value']
                if "memory-usage" in groups['key']:
                    key = groups['key'].replace('-', '_').lower()
                    value = float(groups['value'])

                parsed_dict.update({key: value})
                continue

            # ID  RUNNING  STATUS                 REASON
            # 1   true     utd-oper-status-green 
            # 2   true     utd-oper-status-green 
            m = p2.match(line)
            if m:
                group = m.groupdict()
                id_dict = int(group['id'])

                connection_dict = parsed_dict.setdefault("engine_id", {}).setdefault(id_dict, {})
                keys = ['running', 'status', 'reason']
                for k in keys:
                    connection_dict[k] = group[k]

        return parsed_dict


class ShowUtdEngineStandardStatusSchema(MetaParser):
    ''' Schema for show utd engine standard status'''
    schema = {
        'engine_version': str,
        'profile': str,
        'system_memory': {
            'usage_percentage': float,
            'status': str
            },
        Optional('number_of_engines'): int,
        Optional('engine_id'): {
            int: {
                'running_status': str,
                'health': str,
                'reason': str
                }
            },
        'overall_system_status': str,
        'signature_update_status': {
            'current_signature_package_version': str,
            'last_update_status': str,
            'last_successful_update_time': str,
            'last_failed_update_time': str,
            'last_failed_update_reason': str,
            'next_update_scheduled_at': str,
            'current_status': str
            }
        }


class ShowUtdEngineStandardStatus(ShowUtdEngineStandardStatusSchema):

    """ Parser for "show utd engine standard status" """

    cli_command = "show utd engine standard status"

    def cli(self, output=None):

        # if the user does not provide output to the parser
        # we need to get it from the device
        if not output:
            output = self.device.execute(self.cli_command)
        
        # Engine version : 1.0.4_SV2.9.13.0_XE17.3
        # Profile : Cloud-Medium
        # Number of engines : 2
        # Overall system status: Green
        p1 = re.compile(r'(?P<key>[Engine version|Profile|Number of engines|Overall system status]+\w)(\s+:|:)+\s+(?P<value>[\s\S]+)$')

        # System memory :
        p2 = re.compile(r'^System +memory +:$')

        # Engine(#1): Yes Green None
        p3 = re.compile(r'^(?P<engine>[\s\S]+): +(?P<running_status>[\w]+) +(?P<health>[\w]+) +(?P<reason>[\s\S]+\S)$')

        # Signature update status
        p4 = re.compile(r'^Signature +update +status:$')

        # Usage : 8.80 %
        # Status : Green
        # Current signature package version: 29.0.c\n
        # Last update status: None\n
        # Last successful update time: None\n
        # Last failed update time: None\n
        # Last failed update reason: None\n
        # Next update scheduled at: None\n
        # Current status: Idle\n
        p5 = re.compile(r'^(?P<key>[\s\S]+\w)(\s+:|:)+\s+(?P<value>[\s\S]+)$')

        parsed_dict = {}
        last_dict_ptr = {}

        for line in output.splitlines():
            line = line.strip()

            # Engine version : 1.0.4_SV2.9.13.0_XE17.3
            # Profile : Cloud-Medium
            # Number of engines : 2
            # Overall system status: Green
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                key = groups['key'].replace(' ', '_').lower()
                try:
                    value = int(groups['value'])
                except ValueError:
                    value = groups['value']
                parsed_dict.update({key: value})
                continue

            # System memory :
            m = p2.match(line)
            if m:
                group = m.groupdict()
                system_memory_dict = parsed_dict.setdefault('system_memory', {})
                last_dict_ptr = system_memory_dict
                continue

            # Engine(#1): Yes Green None
            m = p3.match(line)
            if m:
                group = m.groupdict()
                id_dict = int(group['engine'].strip(')').strip('Engine(#'))
                utd_engine_dict = parsed_dict.setdefault("engine_id", {}).setdefault(id_dict, {})
                keys = ['running_status', 'health', 'reason']
                for k in keys:
                    utd_engine_dict[k] = group[k]
                continue

            # Signature update status
            m = p4.match(line)
            if m:
                group = m.groupdict()
                signature_update_status_dict = parsed_dict.setdefault('signature_update_status', {})
                last_dict_ptr = signature_update_status_dict
                continue

            # Engine version : 1.0.4_SV2.9.13.0_XE17.3
            # Profile : Cloud-Medium
            # Usage : 8.80 %
            # Status : Green
            # Overall system status: Green
            # Current signature package version: 29.0.c\n
            # Last update status: None\n
            # Last successful update time: None\n
            # Last failed update time: None\n
            # Last failed update reason: None\n
            # Next update scheduled at: None\n
            # Current status: Idle\n
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                key = groups['key'].replace('-', '_').replace(' ', '_').lower()
                value = groups['value']
                if "Usage" in groups['key']:
                    key = groups['key'].replace('-', '_').lower().replace('usage', 'usage_percentage')
                    value = float(groups['value'].strip('%'))

                last_dict_ptr.update({key: value})
        
        return parsed_dict


# =========================================================
#  Schema for 'show utd engine standard statistics'
# =========================================================
class ShowUtdEngineStandardStatisticsSchema(MetaParser):
    ''' show utd engine standard statistics'''
    schema = {
        'engine_number': {
            Any(): {
                'memry_usage_summary': {
                    'total_non_map_byts': int,
                    'byts_in_mapped_regions': int,
                    'total_alloc_space': int,
                    'total_free_space': int,
                    'topmost_reuse_blk': int
                },
                'pkt_inp_out_totals': {
                    'received': int,
                    'analyzed': int,
                    'dropped': int,
                    'filtered': int,
                    'outstanding': int,
                    'injected': int
                },
                'breakdown_by_protocol': {
                    'eth': int,
                    'vlan': int,
                    'ip4': int,
                    'frag': int,
                    'icmp': int,
                    'udp': int,
                    'tcp': int,
                    'ip6': int,
                    'ip6_ext': int,
                    'ip6_opts': int,
                    'frag6': int,
                    'icmp6': int,
                    'udp6': int,
                    'tcp6': int,
                    'teredo': int,
                    'icmp_ip': int,
                    'ip4_ip4': int,
                    'ip4_ip6': int,
                    'ip6_ip4': int,
                    'ip6_ip6': int,
                    'gre': int,
                    'gre_eth': int,
                    'gre_vlan': int,
                    'gre_ip4': int,
                    'gre_ip6': int,
                    'gre_ip6_ext': int,
                    'gre_pptp': int,
                    'gre_arp': int,
                    'gre_ipx': int,
                    'gre_loop': int,
                    'mpls': int,
                    'arp': int,
                    'ipx': int,
                    'eth_loop': int,
                    'eth_disc': int,
                    'ip6_disc': int,
                    'tcp_disc': int,
                    'udp_disc': int,
                    'icmp_disc': int,
                    'all_discard': int,
                    'other': int 
                },
                'action_stats': {
                    'bad_chk_sum': int,
                    'bad_ttl': int,
                    's5_g_1': int,
                    's5_g_2': int,
                    'total': int,
                    'alerts': int,
                    'logged': int,
                    'passed': int
                },
                'action_stats': {
                    'bad_chk_sum': int,
                    'bad_ttl': int,
                    's5_g_1': int,
                    's5_g_2': int,
                    'total': int,
                    'alerts': int,
                    'logged': int,
                    'passed': int
                }
            }
        }
    }

# =========================================================
#  Parser for 'show utd engine standard statistics'
# =========================================================
class ShowUtdEngineStandardStatistics(ShowUtdEngineStandardStatisticsSchema):

    """ Parser for "show utd engine standard statistics" """

    cli_command = "show utd engine standard statistics"

    def cli(self, output=None):
        if output == None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        # *************Engine #1*************
        p1 = re.compile(r'^\*+Engine\s+\S+(?P<engine_number>\d+)+(\*+)$')

        # Total non-mmapped bytes (arena):       24719360
        p2 = re.compile(r'^Total\snon-mmapped\sbytes\s+\(\w+\):+\s+(?P<total_non_map_byts>\d+)$')

        # Bytes in mapped regions (hblkhd):      437760000
        p3 = re.compile(r'^Bytes\sin\smapped\sregions\s+\(\w+\):+\s+(?P<byts_in_mapped_regions>\d+)$')

        # Total allocated space (uordblks):      23876960
        p4 = re.compile(r'^Total\sallocated\sspace\s+\(\w+\):+\s+(?P<total_alloc_space>\d+)$')

        # Total free space (fordblks):           842400
        p5 = re.compile(r'^Total\sfree\sspace\s+\(\w+\):+\s+(?P<total_free_space>\d+)$')

        # Topmost releasable block (keepcost):   45920
        p6 = re.compile(r'^Topmost\sreleasable\sblock\s+\(\w+\):\s+(?P<topmost_reuse_blk>[\d\.]+)$')

        # Received:            0
        p7 = re.compile(r'^Received:\s+(?P<received>\d+)$')

        # Analyzed:            0 (  0.000%)
        p8 = re.compile(r'^Analyzed:\s+(?P<analyzed>\d+)\s+\(\s+\d+\.\d+\S\)$')

        # Dropped:            0 (  0.000%)
        p9 = re.compile(r'^Dropped:\s+(?P<dropped>\d+)\s+\(\s+\d+\.\d+\S\)$')

        # Filtered:            0 (  0.000%)
        p10 = re.compile(r'^Filtered:\s+(?P<filtered>\d+)\s+\(\s+\d+\.\d+\S\)$')

        # Outstanding:            0 (  0.000%)
        p11 = re.compile(r'^Outstanding:\s+(?P<outstanding>\d+)\s+\(\s+\d+\.\d+\S\)$')

        # Injected:            0
        p12 = re.compile(r'^Injected:\s+(?P<injected>\d+)$')

        # Eth:            0 (  0.000%)
        p13 = re.compile(r'^Eth:\s+(?P<eth>\d+)\s+\(\s+\d+\.\d+\S\)$')

        # VLAN:            0 (  0.000%)
        p14 = re.compile(r'^VLAN:\s+(?P<vlan>\d+)\s+\(\s+\d+\.\d+\S\)$')

        # IP4:            0 (  0.000%)
        p15 = re.compile(r'^IP4:\s+(?P<ip4>\d+)\s+\(\s+\d+\.\d+\S\)$')

        # Frag:            0 (  0.000%)
        p16 = re.compile(r'^Frag:\s+(?P<frag>\d+)\s+\(\s+\d+\.\d+\S\)$')

        # ICMP:            0 (  0.000%)
        p17 = re.compile(r'^ICMP:\s+(?P<icmp>\d+)\s+\(\s+\d+\.\d+\S\)$')

        # UDP:            0 (  0.000%)
        p18 = re.compile(r'^UDP:\s+(?P<udp>\d+)\s+\(\s+\d+\.\d+\S\)$')

        # TCP:            0 (  0.000%)
        p19 = re.compile(r'^TCP:\s+(?P<tcp>\d+)\s+\(\s+\d+\.\d+\S\)$')

        # IP6:            0 (  0.000%)
        p20 = re.compile(r'^IP6:\s+(?P<ip6>\d+)\s+\(\s+\d+\.\d+\S\)$')

        # IP6 Ext:            0 (  0.000%)
        p21 = re.compile(r'^IP6\sExt:\s+(?P<ip6_ext>\d+)\s+\(\s+\d+\.\d+\S\)$')

        # IP6 Opts:            0 (  0.000%)
        p22 = re.compile(r'^IP6\sOpts:\s+(?P<ip6_opts>\d+)\s+\(\s+\d+\.\d+\S\)$')

        # Frag6:            0 (  0.000%)
        p23 = re.compile(r'^Frag6:\s+(?P<frag6>\d+)\s+\(\s+\d+\.\d+\S\)$')

        # ICMP6:            0 (  0.000%)
        p24 = re.compile(r'^ICMP6:\s+(?P<icmp6>\d+)\s+\(\s+\d+\.\d+\S\)$')

        # UDP6:            0 (  0.000%)
        p25 = re.compile(r'^UDP6:\s+(?P<udp6>\d+)\s+\(\s+\d+\.\d+\S\)$')

        # TCP6:            0 (  0.000%)
        p26 = re.compile(r'^TCP6:\s+(?P<tcp6>\d+)\s+\(\s+\d+\.\d+\S\)$')

        # Teredo:            0 (  0.000%)
        p27 = re.compile(r'Teredo:\s+(?P<teredo>\d+)\s+\(\s+\d+\.\d+\S\)$')

        # ICMP-IP:            0 (  0.000%)
        p28 = re.compile(r'ICMP-IP:\s+(?P<icmp_ip>\d+)\s+\(\s+\d+\.\d+\S\)$')

        # IP4/IP4:            0 (  0.000%)
        p29 = re.compile(r'IP4/IP4:\s+(?P<ip4_ip4>\d+)\s+\(\s+\d+\.\d+\S\)$')

        # IP4/IP6:            0 (  0.000%)
        p30 = re.compile(r'IP4/IP6:\s+(?P<ip4_ip6>\d+)\s+\(\s+\d+\.\d+\S\)$')

        # IP6/IP4:            0 (  0.000%)
        p31 = re.compile(r'IP6/IP4:\s+(?P<ip6_ip4>\d+)\s+\(\s+\d+\.\d+\S\)$')

        # IP6/IP6:            0 (  0.000%)
        p32 = re.compile(r'IP6/IP6:\s+(?P<ip6_ip6>\d+)\s+\(\s+\d+\.\d+\S\)$')

        # GRE:            0 (  0.000%)
        p33 = re.compile(r'GRE:\s+(?P<gre>\d+)\s+\(\s+\d+\.\d+\S\)$')

        # GRE Eth:            0 (  0.000%)
        p34 = re.compile(r'GRE\sEth:\s+(?P<gre_eth>\d+)\s+\(\s+\d+\.\d+\S\)$')

        # GRE VLAN:            0 (  0.000%)
        p35 = re.compile(r'GRE\sVLAN:\s+(?P<gre_vlan>\d+)\s+\(\s+\d+\.\d+\S\)$')

        # GRE IP4:            0 (  0.000%)
        p36 = re.compile(r'GRE\sIP4:\s+(?P<gre_ip4>\d+)\s+\(\s+\d+\.\d+\S\)$')

        # GRE IP6:            0 (  0.000%)
        p37 = re.compile(r'GRE\sIP6:\s+(?P<gre_ip6>\d+)\s+\(\s+\d+\.\d+\S\)$')

        # GRE IP6 Ext:            0 (  0.000%)
        p38 = re.compile(r'GRE\sIP6\sExt:\s+(?P<gre_ip6_ext>\d+)\s+\(\s+\d+\.\d+\S\)$')

        # GRE PPTP:            0 (  0.000%)
        p39 = re.compile(r'GRE\sPPTP:\s+(?P<gre_pptp>\d+)\s+\(\s+\d+\.\d+\S\)$')

        # GRE ARP:            0 (  0.000%)
        p40 = re.compile(r'GRE\sARP:\s+(?P<gre_arp>\d+)\s+\(\s+\d+\.\d+\S\)$')

        # GRE IPX:            0 (  0.000%)
        p41 = re.compile(r'GRE\sIPX:\s+(?P<gre_ipx>\d+)\s+\(\s+\d+\.\d+\S\)$')

        # GRE Loop:            0 (  0.000%)
        p42 = re.compile(r'GRE\sLoop:\s+(?P<gre_loop>\d+)\s+\(\s+\d+\.\d+\S\)$')

        # MPLS:            0 (  0.000%)
        p43 = re.compile(r'MPLS:\s+(?P<mpls>\d+)\s+\(\s+\d+\.\d+\S\)$')

        # ARP:            0 (  0.000%)
        p44 = re.compile(r'ARP:\s+(?P<arp>\d+)\s+\(\s+\d+\.\d+\S\)$')

        # IPX:            0 (  0.000%)
        p45 = re.compile(r'IPX:\s+(?P<ipx>\d+)\s+\(\s+\d+\.\d+\S\)$')

        # Eth Loop:            0 (  0.000%)
        p46 = re.compile(r'Eth\sLoop:\s+(?P<eth_loop>\d+)\s+\(\s+\d+\.\d+\S\)$')

        # Eth Disc:            0 (  0.000%)
        p47 = re.compile(r'Eth\sDisc:\s+(?P<eth_disc>\d+)\s+\(\s+\d+\.\d+\S\)$')

        # IP4 Disc:            0 (  0.000%)
        p48 = re.compile(r'IP4:\sDisc:\s+(?P<ip4_disc>\d+)\s+\(\s+\d+\.\d+\S\)$')

        # IP6 Disc:            0 (  0.000%)
        p49 = re.compile(r'IP6\sDisc:\s+(?P<ip6_disc>\d+)\s+\(\s+\d+\.\d+\S\)$')

        # TCP Disc:            0 (  0.000%)
        p50 = re.compile(r'TCP\sDisc:\s+(?P<tcp_disc>\d+)\s+\(\s+\d+\.\d+\S\)$')

        # UDP Disc:            0 (  0.000%)
        p51 = re.compile(r'UDP\sDisc:\s+(?P<udp_disc>\d+)\s+\(\s+\d+\.\d+\S\)$')

        # ICMP Disc:            0 (  0.000%)
        p52 = re.compile(r'ICMP\sDisc:\s+(?P<icmp_disc>\d+)\s+\(\s+\d+\.\d+\S\)$')

        # All Discard:            0 (  0.000%)
        p53 = re.compile(r'All\sDiscard:\s+(?P<all_discard>\d+)\s+\(\s+\d+\.\d+\S\)$')

        # Other:            0 (  0.000%)
        p54 = re.compile(r'Other:\s+(?P<other>\d+)\s+\(\s+\d+\.\d+\S\)$')

        # Bad Chk Sum:            0 (  0.000%)
        p55 = re.compile(r'Bad\sChk\sSum:\s+(?P<bad_chk_sum>\d+)\s+\(\s+\d+\.\d+\S\)$')

        # Bad TTL:            0 (  0.000%)
        p56 = re.compile(r'Bad\sTTL:\s+(?P<bad_ttl>\d+)\s+\(\s+\d+\.\d+\S\)$')

        # S5 G 1:            0 (  0.000%)
        p57 = re.compile(r'S5\sG\s1:\s+(?P<s5_g_1>\d+)\s+\(\s+\d+\.\d+\S\)$')

        # S5 G 2:            0 (  0.000%)
        p58 = re.compile(r'S5\sG\s2:\s+(?P<s5_g_2>\d+)\s+\(\s+\d+\.\d+\S\)$')

        # Total:            0
        p59 = re.compile(r'Total:\s+(?P<total>\d+)$')

        # Alerts:            0 (  0.000%)
        p60 = re.compile(r'Alerts:\s+(?P<alerts>\d+)\s+\(\s+\d+\.\d+\S\)$')

        # Logged:            0 (  0.000%)
        p61 = re.compile(r'Logged:\s+(?P<logged>\d+)\s+\(\s+\d+\.\d+\S\)$')

        # Passed:            0 (  0.000%)
        p62 = re.compile(r'Passed:\s+(?P<passed>\d+)\s+\(\s+\d+\.\d+\S\)$')

        for line in output.splitlines():
            line = line.strip()

            # *************Engine #1*************
            m = p1.match(line)
            if m:
                group = m.groupdict()
                engine_number = group['engine_number']
                engine_dict = ret_dict.setdefault('engine_number', {})
                memry_usage_summary_dict = engine_dict.setdefault(engine_number, {}).setdefault('memry_usage_summary', {})
                continue

            # Total non-mmapped bytes (arena):       24719360
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                memry_usage_summary_dict['total_non_map_byts'] = int(groups['total_non_map_byts'])
                continue

            # Bytes in mapped regions (hblkhd):      437760000
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                memry_usage_summary_dict['byts_in_mapped_regions'] = int(groups['byts_in_mapped_regions'])
                continue

            # Total allocated space (uordblks):      23876960
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                memry_usage_summary_dict['total_alloc_space'] = int(groups['total_alloc_space'])
                continue

            # Total free space (fordblks):           842400
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                memry_usage_summary_dict['total_free_space'] = int(groups['total_free_space'])
                continue

            # Topmost releasable block (keepcost):   45920
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                memry_usage_summary_dict['topmost_reuse_blk'] = int(groups['topmost_reuse_blk'])
                continue

            # Received:            0
            m = p7.match(line)
            if m:
                groups = m.groupdict()
                pkt_io_totals_dict = engine_dict.setdefault(engine_number, {}).setdefault('pkt_inp_out_totals', {})
                pkt_io_totals_dict['received'] = int(groups['received'])
                continue

            # Analyzed:            0 (  0.000%)
            m = p8.match(line)
            if m:
                groups = m.groupdict()
                pkt_io_totals_dict['analyzed'] = int(groups['analyzed'])
                continue

            # Dropped:            0 (  0.000%)
            m = p9.match(line)
            if m:
                groups = m.groupdict()
                pkt_io_totals_dict['dropped'] = int(groups['dropped'])
                continue

            # Filtered:            0 (  0.000%)
            m = p10.match(line)
            if m:
                groups = m.groupdict()
                pkt_io_totals_dict['filtered'] = int(groups['filtered'])
                continue

            # Outstanding:            0 (  0.000%)
            m = p11.match(line)
            if m:
                groups = m.groupdict()
                pkt_io_totals_dict['outstanding'] = int(groups['outstanding'])
                continue

            # Injected:            0
            m = p12.match(line)
            if m:
                groups = m.groupdict()
                pkt_io_totals_dict['injected'] = int(groups['injected'])
                continue

            # Eth:            0 (  0.000%)
            m = p13.match(line)
            if m:
                groups = m.groupdict()
                breakdown_by_protocol_dict = engine_dict.setdefault(engine_number, {}).setdefault('breakdown_by_protocol',{})
                breakdown_by_protocol_dict['eth'] = int(groups['eth'])
                continue

            # VLAN:            0 (  0.000%)
            m = p14.match(line)
            if m:
                groups = m.groupdict()
                breakdown_by_protocol_dict['vlan'] = int(groups['vlan'])
                continue

            # IP4:            0 (  0.000%)
            m = p15.match(line)
            if m:
                groups = m.groupdict()
                breakdown_by_protocol_dict['ip4'] = int(groups['ip4'])
                continue

            # Frag:            0 (  0.000%)
            m = p16.match(line)
            if m:
                groups = m.groupdict()
                breakdown_by_protocol_dict['frag'] = int(groups['frag'])
                continue

            # ICMP:            0 (  0.000%)
            m = p17.match(line)
            if m:
                groups = m.groupdict()
                breakdown_by_protocol_dict['icmp'] = int(groups['icmp'])
                continue

            # UDP:            0 (  0.000%)
            m = p18.match(line)
            if m:
                groups = m.groupdict()
                breakdown_by_protocol_dict['udp'] = int(groups['udp'])
                continue

            # TCP:            0 (  0.000%)
            m = p19.match(line)
            if m:
                groups = m.groupdict()
                breakdown_by_protocol_dict['tcp'] = int(groups['tcp'])
                continue

            # IP6:            0 (  0.000%)
            m = p20.match(line)
            if m:
                groups = m.groupdict()
                breakdown_by_protocol_dict['ip6'] = int(groups['ip6'])
                continue

            # IP6 Ext:            0 (  0.000%)
            m = p21.match(line)
            if m:
                groups = m.groupdict()
                breakdown_by_protocol_dict['ip6_ext'] = int(groups['ip6_ext'])
                continue

            # IP6 Opts:            0 (  0.000%)
            m = p22.match(line)
            if m:
                groups = m.groupdict()
                breakdown_by_protocol_dict['ip6_opts'] = int(groups['ip6_opts'])
                continue

            # Frag6:            0 (  0.000%)
            m = p23.match(line)
            if m:
                groups = m.groupdict()
                breakdown_by_protocol_dict['frag6'] = int(groups['frag6'])
                continue

            # ICMP6:            0 (  0.000%)
            m = p24.match(line)
            if m:
                groups = m.groupdict()
                breakdown_by_protocol_dict['icmp6'] = int(groups['icmp6'])
                continue

            # UDP6:            0 (  0.000%)
            m = p25.match(line)
            if m:
                groups = m.groupdict()
                breakdown_by_protocol_dict['udp6'] = int(groups['udp6'])
                continue

            # TCP6:            0 (  0.000%)
            m = p26.match(line)
            if m:
                groups = m.groupdict()
                breakdown_by_protocol_dict['tcp6'] = int(groups['tcp6'])
                continue

            # Teredo:            0 (  0.000%)
            m = p27.match(line)
            if m:
                groups = m.groupdict()
                breakdown_by_protocol_dict['teredo'] = int(groups['teredo'])
                continue

            # ICMP-IP:            0 (  0.000%)
            m = p28.match(line)
            if m:
                groups = m.groupdict()
                breakdown_by_protocol_dict['icmp_ip'] = int(groups['icmp_ip'])
                continue

            # IP4/IP4:            0 (  0.000%)
            m = p29.match(line)
            if m:
                groups = m.groupdict()
                breakdown_by_protocol_dict['ip4_ip4'] = int(groups['ip4_ip4'])
                continue

            # IP4/IP6:            0 (  0.000%)
            m = p30.match(line)
            if m:
                groups = m.groupdict()
                breakdown_by_protocol_dict['ip4_ip6'] = int(groups['ip4_ip6'])
                continue

            # IP6/IP4:            0 (  0.000%)
            m = p31.match(line)
            if m:
                groups = m.groupdict()
                breakdown_by_protocol_dict['ip6_ip4'] = int(groups['ip6_ip4'])
                continue

            # IP6/IP6:            0 (  0.000%)
            m = p32.match(line)
            if m:
                groups = m.groupdict()
                breakdown_by_protocol_dict['ip6_ip6'] = int(groups['ip6_ip6'])
                continue

            # GRE:            0 (  0.000%)
            m = p33.match(line)
            if m:
                groups = m.groupdict()
                breakdown_by_protocol_dict['gre'] = int(groups['gre'])
                continue

            # GRE Eth:            0 (  0.000%)
            m = p34.match(line)
            if m:
                groups = m.groupdict()
                breakdown_by_protocol_dict['gre_eth'] = int(groups['gre_eth'])
                continue

            # GRE VLAN:            0 (  0.000%)
            m = p35.match(line)
            if m:
                groups = m.groupdict()
                breakdown_by_protocol_dict['gre_vlan'] = int(groups['gre_vlan'])
                continue

            # GRE IP4:            0 (  0.000%)
            m = p36.match(line)
            if m:
                groups = m.groupdict()
                breakdown_by_protocol_dict['gre_ip4'] = int(groups['gre_ip4'])
                continue

            # GRE IP6:            0 (  0.000%)
            m = p37.match(line)
            if m:
                groups = m.groupdict()
                breakdown_by_protocol_dict['gre_ip6'] = int(groups['gre_ip6'])
                continue

            # GRE IP6 Ext:            0 (  0.000%)
            m = p38.match(line)
            if m:
                groups = m.groupdict()
                breakdown_by_protocol_dict['gre_ip6_ext'] = int(groups['gre_ip6_ext'])
                continue

            # GRE PPTP:            0 (  0.000%)
            m = p39.match(line)
            if m:
                groups = m.groupdict()
                breakdown_by_protocol_dict['gre_pptp'] = int(groups['gre_pptp'])
                continue

            # GRE ARP:            0 (  0.000%)
            m = p40.match(line)
            if m:
                groups = m.groupdict()
                breakdown_by_protocol_dict['gre_arp'] = int(groups['gre_arp'])
                continue

            # GRE IPX:            0 (  0.000%)
            m = p41.match(line)
            if m:
                groups = m.groupdict()
                breakdown_by_protocol_dict['gre_ipx'] = int(groups['gre_ipx'])
                continue

            # GRE Loop:            0 (  0.000%)
            m = p42.match(line)
            if m:
                groups = m.groupdict()
                breakdown_by_protocol_dict['gre_loop'] = int(groups['gre_loop'])
                continue

            # MPLS:            0 (  0.000%)
            m = p43.match(line)
            if m:
                groups = m.groupdict()
                breakdown_by_protocol_dict['mpls'] = int(groups['mpls'])
                continue

            # ARP:            0 (  0.000%)
            m = p44.match(line)
            if m:
                groups = m.groupdict()
                breakdown_by_protocol_dict['arp'] = int(groups['arp'])
                continue

            # IPX:            0 (  0.000%)
            m = p45.match(line)
            if m:
                groups = m.groupdict()
                breakdown_by_protocol_dict['ipx'] = int(groups['ipx'])
                continue

            # Eth Loop:            0 (  0.000%)
            m = p46.match(line)
            if m:
                groups = m.groupdict()
                breakdown_by_protocol_dict['eth_loop'] = int(groups['eth_loop'])
                continue

            # Eth Disc:            0 (  0.000%)
            m = p47.match(line)
            if m:
                groups = m.groupdict()
                breakdown_by_protocol_dict['eth_disc'] = int(groups['eth_disc'])
                continue

            # IP4 Disc:            0 (  0.000%)
            m = p48.match(line)
            if m:
                groups = m.groupdict()
                breakdown_by_protocol_dict['ip4_disc'] = int(groups['ip4_disc'])
                continue

            # IP6 Disc:            0 (  0.000%)
            m = p49.match(line)
            if m:
                groups = m.groupdict()
                breakdown_by_protocol_dict['ip6_disc'] = int(groups['ip6_disc'])
                continue

            # TCP Disc:            0 (  0.000%)
            m = p50.match(line)
            if m:
                groups = m.groupdict()
                breakdown_by_protocol_dict['tcp_disc'] = int(groups['tcp_disc'])
                continue

            # UDP Disc:            0 (  0.000%)
            m = p51.match(line)
            if m:
                groups = m.groupdict()
                breakdown_by_protocol_dict['udp_disc'] = int(groups['udp_disc'])
                continue

            # ICMP Disc:            0 (  0.000%)
            m = p52.match(line)
            if m:
                groups = m.groupdict()
                breakdown_by_protocol_dict['icmp_disc'] = int(groups['icmp_disc'])
                continue

            # All Discard:            0 (  0.000%)
            m = p53.match(line)
            if m:
                groups = m.groupdict()
                breakdown_by_protocol_dict['all_discard'] = int(groups['all_discard'])
                continue

            # Other:            0 (  0.000%)
            m = p54.match(line)
            if m:
                groups = m.groupdict()
                breakdown_by_protocol_dict['other'] = int(groups['other'])
                continue

            # Bad Chk Sum:            0 (  0.000%)
            m = p55.match(line)
            if m:
                groups = m.groupdict()
                action_stats_dict = engine_dict.setdefault(engine_number, {}).setdefault('action_stats', {})
                action_stats_dict['bad_chk_sum'] = int(groups['bad_chk_sum'])
                continue

            # Bad TTL:            0 (  0.000%)
            m = p56.match(line)
            if m:
                groups = m.groupdict()
                action_stats_dict = engine_dict.setdefault(engine_number, {}).setdefault('action_stats', {})
                action_stats_dict['bad_ttl'] = int(groups['bad_ttl'])
                continue

            # S5 G 1:            0 (  0.000%)
            m = p57.match(line)
            if m:
                groups = m.groupdict()
                action_stats_dict = engine_dict.setdefault(engine_number, {}).setdefault('action_stats', {})
                action_stats_dict['s5_g_1'] = int(groups['s5_g_1'])
                continue

            # S5 G 2:            0 (  0.000%)
            m = p58.match(line)
            if m:
                groups = m.groupdict()
                action_stats_dict = engine_dict.setdefault(engine_number, {}).setdefault('action_stats', {})
                action_stats_dict['s5_g_2'] = int(groups['s5_g_2'])
                continue

            # Total:            0
            m = p59.match(line)
            if m:
                groups = m.groupdict()
                action_stats_dict = engine_dict.setdefault(engine_number, {}).setdefault('action_stats', {})
                action_stats_dict['total'] = int(groups['total'])
                continue

            # Alerts:            0 (  0.000%)
            m = p60.match(line)
            if m:
                groups = m.groupdict()
                action_stats_dict = engine_dict.setdefault(engine_number, {}).setdefault('action_stats', {})
                action_stats_dict['alerts'] = int(groups['alerts'])
                continue

            # Logged:            0 (  0.000%)
            m = p61.match(line)
            if m:
                groups = m.groupdict()
                action_stats_dict = engine_dict.setdefault(engine_number, {}).setdefault('action_stats', {})
                action_stats_dict['logged'] = int(groups['logged'])
                continue

            # Passed:            0 (  0.000%)
            m = p62.match(line)
            if m:
                groups = m.groupdict()
                action_stats_dict = engine_dict.setdefault(engine_number, {}).setdefault('action_stats', {})
                action_stats_dict['passed'] = int(groups['passed'])
                continue

        return ret_dict

# =========================================================
#  Schema for 'show utd engine standard statistics daq all'
# =========================================================
class ShowUtdEngineStandardStatisticsDaqAllSchema(MetaParser):
    ''' show utd engine standard statistics daq all'''
    schema = {
	'engine_number': {
		Any(): {
			'ios_xe_daq_counters': {
				'frames_recevd': int,
				'bytes_recevd': int,
				'rx_frames_released': int,
				'pkts_after_vpath_decap': int,
				'bytes_after_vpath_decap': int,
				'pkts_before_vpath_encap': int,
				'bytes_before_vpath_encap': int,
				'frames_transmitted': int,
				'bytes_transmitted': int,
				'frames_injected': int,
				'bytes_injected': int,
				'memory_allocation': int,
				'memory_free': int,
				'memry_free_via_timer': int,
				'merged_pkt_buffer_allocation': int,
				'merged_pkt_buffer_free': int,
				'vpl_buffer_allocation': int,
				'vpl_buffer_free': int,
				'vpl_buffer_expand': int,
				'vpl_buffer_merge': int,
				'vpl_buffer_split': int,
				'vpl_pkt_incomplete': int,
				'vpl_api_error': int,
				'internal_error': int,
				'external_error': int,
				'memory_error': int,
				'timer_error': int,
				'sppi_receive_pkt_error': int,
				'sppi_acquire_pkt_error': int,
				'sppi_inject_pkt_error': int,
				'sppi_internal_error': int,
				'kernel_frames_rcvd': int,
				'kernel_frames_drp': 0
			},
			'ios_xe_daq_wcapi_counters': {
				'mesages_recevd': int,
				'messages_transmitted': int,
				'flow_create_recvd': int,
				'flow_create_transmitted': int,
				'flow_close_recvd': int,
				'flow_close_transmitted': int,
				'flow_data_recvd': int,
				'flow_data_bytes_recvd': int,
				'flow_data_transmitted': int,
				'flow_data_bytes_transmitted': int,
				'flow_delete_recevd': int,
				'unknown_type_msgs_rcvd': int,
				'ebp_cleanup_recvd': int,
				'ebp_cleanup_transmitted': int,
				'flow_control_injected': int,
				'flow_data_injected': int,
				'flow_data_bytes_injected': int,
				'verdict_allow': int,
				'verdict_deny': int,
				'decrypt_policy_ver_no_decrypt': int,
				'decrypt_policy_ver_decrypt': int,
				'decrypt_policy_ver_passthrough': int,
				'decrypt_policy_ver_unknown': int,
				'flow_create': int,
				'flow_delete': int,
				'flow_duplicate': int,
				'flow_data_not_found': int,
				'flow_close_not_found': int,
				'flow_delete_not_found': int,
				'flow_enqueue': int,
				'flow_dequeue': int,
				'retry_enqueue': int,
				'retry_dequeue': int,
				'retry_hold_flow': int,
				'retry_release_flow': int,
				'retry_add_flow': int,
				'closed_enqueue': int,
				'closed_dequeue': int,
				'socket_msg_recvd': int,
				'socket_ser_ready_msg_recvd': int,
				'socket_sipc_open_failed_msgs_rcvd': int,
				'socket_new_sipc_messages_rcvd': int,
				'sock_unexp_nw_sipc_msg_msgs_rcvd': int,
				'socket_ser_down_msg_recvd': int,
				'socket_tx_socket_ready_msg_recvd': int,
				'sock_tx_sockconn_failed_msg_rcvd': int,
				'sock_unknown_uds_msg_msgs_rcvd': int,
				'sock_unknown_msgs_rcvd': int,
				'tx_sock_msgs_rcvd': int,
				'tx_sock_resume_msgs_rcvd': int,
				'tx_sock_unknown_msgs_rcvd': int,
				'tx_paused': int,
				'memory_allocation': int,
				'memory_free': int,
				'memory_error': int,
				'ebp_get_buffer_local': int,
				'ebp_get_buffer_local_error': int,
				'ebp_return_buffer_local': int,
				'ebp_return_buffer': int,
				'sleep': int,
				'sleep_set_flag': int,
				'htx_up': int,
				'htx_down': int,
				'internal_error': int,
				'external_error': int,
				'wcapi_error': int
			},
			'vpl_stats': {
				'vpath_802_3_pkts_rcvd': int,
				'vpath_ipv4_pkts_rcvd': int,
				'vpath_pkts_transmitted': int,
				'vpath_ipv4_ping_pkts_rcvd': int,
				'vpath_ver_0_pkts_rcvd': int,
				'non_snap_802_3_pkts_rcvd': int,
				'non_cisco_802_3_pkts_rcvd': int,
				'non_ipv4_pkts_rcvd': int,
				'non_ipv4_udp_pkts_rcvd': int,
				'non_vpath_802_3_pkts_rcvd': int,
				'non_vpath_dot1q_pkts_rcvd': int,
				'non_vpath_ipv4_pkts_rcvd': int,
				'non_vpath_ipv4_udp_pkts_rcvd': int,
				'non_vpath_ipv4_gre_pkts_rcvd': int,
				'non_vpath_mac_pkts_rcvd': int,
				'vpath_ver_mismtch_pkts_rcvd': int,
				'checksum_mismtch_pkts_rcvd': int,
				'ip_inst_fragments': int,
				'ip_fragmented_packets': int,
				'ip_aged_fragmented_packets': int,
				'ip_exceed_max_fragmented_packets': int,
				'ip_overlapping_fragments': int,
				'ip_exceed_fragments_per_pkt': int,
				'ip_exceed_len_fragmented_pkt': int,
				'ip_tiny_fragmented_pkt': int,
				'ip_bad_length_fragmented_pkt': int,
				'l2_inst_fragments': int,
				'l2_fragmented_packets': int,
				'l2_aged_fragmented_packets': int,
				'l2_exceed_max_fragmented_packets': int,
				'l2_overlapping_fragments': int,
				'l2_exceed_fragments_per_pkt': int,
				'l2_exceed_len_fragmented_pkt': int,
				'l2_tiny_fragmented_pkt': int,
				'l2_bad_length_fragmented_pkt': int,
				'deacp_pkt_api_calls': int,
				'encap_gen_pkt_api_calls': int,
				'encap_nw_pkt_api_calls': int,
				'deacp_pkt_api_errors': int,
				'encap_gen_api_errors': int,
				'encap_nw_api_errors': int
			},
			'ios_xe_daq_cp_counters': {
				'packet_received': int,
				'bytes_received': int,
				'packets_transmitted': int,
				'bytes_transmitted': int,
				'memory_allocation': int,
				'memory_free': int,
				'vpl_api_error': int,
				'internal_error': int,
				'external_error': int,
				'memory_error': int,
				'timer_error': int,
				'rx_ring_full': int,
				'memry_status_changed_to_yellow': int,
				'memry_status_changed_to_red': int,
				'process_restart_notifications': int
			}
		}
    }
}

# =========================================================
#  Parser for 'show utd engine standard statistics daq all'
# =========================================================
class ShowUtdEngineStandardStatisticsDaqAll(ShowUtdEngineStandardStatisticsDaqAllSchema):

    """ Parser for "show utd engine standard statistics daq all" """

    cli_command = "show utd engine standard statistics daq all"

    def cli(self, output=None):
        if output == None:
            output = self.device.execute(self.cli_command)
            
        ret_dict = {}

        # IOS-XE DAQ Counters(Engine #1):
        p1 = re.compile(r'^IOS-XE\sDAQ\sCounters+\(+\w+\s+\#(?P<engine_number>\d+)(\):)$')

        # Frames received                         0
        p2 = re.compile(r'^Frames\sreceived\s+(?P<frames_recevd>\d+)$')

        # Bytes received                          0
        p3 = re.compile(r'^Bytes\sreceived\s+(?P<bytes_recevd>\d+)$')
        
        # RX frames released                      0
        p4 = re.compile(r'^RX\sframes\sreleased\s+(?P<rx_frames_released>\d+)$')
        
        # Packets after vPath decap               0
        p5 = re.compile(r'^Packets\safter\svPath\sdecap\s+(?P<pkts_after_vpath_decap>\d+)$')
        
        # Bytes after vPath decap                 0
        p6 = re.compile(r'^Bytes\safter\svPath\sdecap\s+(?P<bytes_after_vpath_decap>\d+)$')
        
        # Packets before vPath encap              0
        p7 = re.compile(r'^Packets\sbefore\svPath\sencap\s+(?P<pkts_before_vpath_encap>\d+)$')
        
        # Bytes before vPath encap                0
        p8 = re.compile(r'^Bytes\sbefore\svPath\sencap\s+(?P<bytes_before_vpath_encap>\d+)$')
        
        # Frames transmitted                      0
        p9 = re.compile(r'^Frames\stransmitted\s+(?P<frames_transmitted>\d+)$')
        
        # Bytes transmitted                       0
        p10 = re.compile(r'^Bytes\stransmitted\s+(?P<bytes_transmitted>\d+)$')
        
        # Frames injected                         0
        p11 = re.compile(r'^Frames\sinjected\s+(?P<frames_injected>\d+)$')
        
        # Bytes injected                          0
        p12 = re.compile(r'^Bytes\sinjected\s+(?P<bytes_injected>\d+)$')
        
        # Memory allocation                       388
        p13 = re.compile(r'^Memory\sallocation\s+(?P<memory_allocation>\d+)$')
        
        # Memory free                             0
        p14 = re.compile(r'^Memory\sfree\s+(?P<memory_free>\d+)$')
        
        # Memory free via timer                   0
        p15 = re.compile(r'^Memory\sfree\svia\stimer\s+(?P<memry_free_via_timer>\d+)$')
        
        # Merged packet buffer allocation         0
        p16 = re.compile(r'^Merged\spacket\sbuffer\sallocation\s+(?P<merged_pkt_buffer_allocation>\d+)$')
        
        # Merged packet buffer free               0
        p17 = re.compile(r'^Merged\spacket\sbuffer\sfree\s+(?P<merged_pkt_buffer_free>\d+)$')
        
        # VPL buffer allocation                   0
        p18 = re.compile(r'^VPL\sbuffer\sallocation\s+(?P<vpl_buffer_allocation>\d+)$')
        
        # VPL buffer free                         0
        p19 = re.compile(r'^VPL\sbuffer\sfree\s+(?P<vpl_buffer_free>\d+)$')
        
        # VPL buffer expand                       0
        p20 = re.compile(r'^VPL\sbuffer\sexpand\s+(?P<vpl_buffer_expand>\d+)$')
        
        # VPL buffer merge                        0
        p21 = re.compile(r'^VPL\sbuffer\smerge\s+(?P<vpl_buffer_merge>\d+)$')
        
        # VPL buffer split                        0
        p22 = re.compile(r'^VPL\sbuffer\ssplit\s+(?P<vpl_buffer_split>\d+)$')
        
        # VPL packet incomplete                   0
        p23 = re.compile(r'^VPL\spacket\sincomplete\s+(?P<vpl_pkt_incomplete>\d+)$')
        
        # VPL API error                           0
        p24 = re.compile(r'^VPL\sAPI\serror\s+(?P<vpl_api_error>\d+)$')
        
        # Internal error                          0
        p25 = re.compile(r'^Internal\serror\s+(|:)(?P<internal_error>\d+)$')
        
        # External error                          0
        p26 = re.compile(r'^External\serror\s+(|:)(?P<external_error>\d+)$')
        
        # Memory error                            0
        p27 = re.compile(r'^Memory\serror\s+(|:)(?P<memory_error>\d+)$')
        
        # Timer error                             0
        p28 = re.compile(r'^Timer\serror\s+(|:)(?P<timer_error>\d+)$')
        
        # SPPI Receive Packet error               0
        p29 = re.compile(r'^SPPI\sReceive\sPacket\serror\s+(?P<sppi_receive_pkt_error>\d+)$')
        
        # SPPI Acquire Transmit Packet error      0
        p30 = re.compile(r'^SPPI\sAcquire\sTransmit\sPacket\serror\s+(?P<sppi_acquire_pkt_error>\d+)$')
        
        # SPPI Inject Transmit Packet error       0
        p31 = re.compile(r'^SPPI\sInject\sTransmit\sPacket\serror\s+(?P<sppi_inject_pkt_error>\d+)$')
        
        # SPPI Encap Transmit Packet error        0
        p32 = re.compile(r'^SPPI\sEncap\sTransmit\s\sPacket\serror\s+(?P<sppi_encap_transmit_pkt_error>\d+)$')
        
        # SPPI Internal error                     0
        p33 = re.compile(r'^SPPI\sInternal\serror\s+(?P<sppi_internal_error>\d+)$')
        
        # Kernel frames received                  0
        p34 = re.compile(r'^Kernel\sframes\sreceived\s+(?P<kernel_frames_rcvd>\d+)$')
        
        # Kernel frames dropped                   0
        p35 = re.compile(r'^Kernel\sframes\sdropped\s+(?P<kernel_frames_drp>\d+)$')
        
        # IOS-XE DAQ WCAPI Counters (Engine #1):
        p36 = re.compile(r'^IOS-XE\sDAQ\sWCAPI\sCounters+\s+\(+\w+\s+\#(?P<engine_number>\d+)(\):)$')

        # Messages received                       0
        p37 = re.compile(r'^Messages\sreceived\s+(?P<mesages_recevd>\d+)$')

        # Messages transmitted                    0
        p38 = re.compile(r'^Messages\stransmitted\s+(?P<messages_transmitted>\d+)$')
        
        # Flow create received                    0
        p39 = re.compile(r'^Flow\screate\sreceived\s+(?P<flow_create_recvd>\d+)$')
        
        # Flow create transmitted                 0               0
        p40 = re.compile(r'^Flow\screate\stransmitted\s+(?P<flow_create_transmitted>\d+)$')
        
        # Flow close received                     0
        p41 = re.compile(r'^Flow\sclose\sreceived\s+(?P<flow_close_recvd>\d+)$')
        
        # Flow close transmitted                  0              0
        p42 = re.compile(r'^Flow\sclose\stransmitted\s+(?P<flow_close_transmitted>\d+)$')
        
        # Flow data received                      0
        p43 = re.compile(r'^Flow\sdata\sreceived\s+(?P<flow_data_recvd>\d+)$')
        
        # Flow data bytes received                0
        p44 = re.compile(r'^Flow\sdata\sbytes\sreceived\s+(?P<flow_data_bytes_recvd>\d+)$$')
        
        # Flow data transmitted                   0
        p45 = re.compile(r'^Flow\sdata\stransmitted\s+(?P<flow_data_transmitted>\d+)$')
        
        # Flow data bytes transmitted             0
        p46 = re.compile(r'^Flow\sdata\sbytes\stransmitted\s+(?P<flow_data_bytes_transmitted>\d+)$')
        
        # Flow delete received                    0
        p47 = re.compile(r'^Flow\sdelete\sreceived\s+(?P<flow_delete_recevd>\d+)$')
        
        # Unknown type messages received          0
        p48 = re.compile(r'^Unknown\stype\smessages\sreceived\s+(?P<unknown_type_msgs_rcvd>\d+)$')
        
        # EBP cleanup received                    0
        p49 = re.compile(r'^EBP\scleanup\sreceived\s+(?P<ebp_cleanup_recvd>\d+)$')
        
        # EBP cleanup transmitted                 0
        p50 = re.compile(r'^EBP\scleanup\stransmitted\s+(?P<ebp_cleanup_transmitted>\d+)$')
        
        # Flow control injected                   0
        p51 = re.compile(r'^Flow\scontrol\sinjected\s+(?P<flow_control_injected>\d+)$')
        
        # Flow data injected                      0
        p52 = re.compile(r'^Flow\sdata\sinjected\s+(?P<flow_data_injected>\d+)$')
        
        # Flow data bytes injected                0
        p53 = re.compile(r'^Flow\sdata\sbytes\sinjected\s+(?P<flow_data_bytes_injected>\d+)$')
        
        # Verdict allow                           0
        p54 = re.compile(r'^Verdict\sallow\s+(?P<verdict_allow>\d+)$')
        
        # Verdict deny                            0
        p55 = re.compile(r'^Verdict\sdeny\s+(?P<verdict_deny>\d+)$')
        
        # Decryption policy verdict no-decrypt    0
        p56 = re.compile(r'^Decryption\spolicy\sverdict\sno-decrypt\s+(?P<decrypt_policy_ver_no_decrypt>\d+)$')
        
        # Decryption policy verdict decrypt       0
        p57 = re.compile(r'^Decryption\spolicy\sverdict\sdecrypt\s+(?P<decrypt_policy_ver_decrypt>\d+)$')
        
        # Decryption policy verdict passthrough   0
        p58 = re.compile(r'^Decryption\spolicy\sverdict\spassthrough\s+(?P<decrypt_policy_ver_passthrough>\d+)$')
        
        # Decryption policy verdict unknown       0
        p59 = re.compile(r'^Decryption\spolicy\sverdict\sunknown\s+(?P<decrypt_policy_ver_unknown>\d+)$')
        
        # Flow create                             0
        p60 = re.compile(r'^Flow\screate\s+(?P<flow_create>\d+)$')
        
        # Flow delete                             0
        p61 = re.compile(r'^Flow\sdelete\s+(?P<flow_delete>\d+)$')
        
        # Flow duplicate                          0
        p62 = re.compile(r'^Flow\sduplicate\s+(?P<flow_duplicate>\d+)$')
        
        # Flow data not found                     0
        p63 = re.compile(r'^Flow\sdata\snot\sfound\s+(?P<flow_data_not_found>\d+)$')
        
        # Flow close not found                    0
        p64 = re.compile(r'^Flow\sclose\snot\sfound\s+(?P<flow_close_not_found>\d+)$')
        
        # Flow delete not found                   0
        p65 = re.compile(r'^Flow\sdelete\snot\sfound\s+(?P<flow_delete_not_found>\d+)$')
        
        # Flow enqueue                            0
        p66 = re.compile(r'^Flow\senqueue\s+(?P<flow_enqueue>\d+)$')
        
        # Flow dequeue                            0
        p67 = re.compile(r'^Flow\sdequeue\s+(?P<flow_dequeue>\d+)$')
        
        # Retry enqueue                           0
        p68 = re.compile(r'^Retry\senqueue\s+(?P<retry_enqueue>\d+)$')
        
        # Retry dequeue                           0
        p69 = re.compile(r'^Retry\sdequeue\s+(?P<retry_dequeue>\d+)$')
        
        # Retry hold flow                         0
        p70 = re.compile(r'^Retry\shold\sflow\s+(?P<retry_hold_flow>\d+)$')
        
        # Retry release flow                      0
        p71 = re.compile(r'^Retry\srelease\sflow\s+(?P<retry_release_flow>\d+)$')
        
        # Retry add flow                          0
        p72 = re.compile(r'^Retry\sadd\sflow\s+(?P<retry_add_flow>\d+)$')
        
        # Closed enqueue                          0
        p73 = re.compile(r'^Closed\senqueue\s+(?P<closed_enqueue>\d+)$')
        
        # Closed dequeue                          0
        p74 = re.compile(r'^Closed\sdequeue\s+(?P<closed_dequeue>\d+)$')
        
        # Socket messages received                0
        p75 = re.compile(r'^Socket\smessages\sreceived\s+(?P<socket_msg_recvd>\d+)$')
        
        # Socket server ready messages received   0
        p76 = re.compile(r'^Socket\sserver\sready\smessages\sreceived\s+(?P<socket_ser_ready_msg_recvd>\d+)$')
        
        # Socket sipc open failed msgs received   0
        p77 = re.compile(r'^Socket\ssipc\sopen\sfailed\smsgs\sreceived\s+(?P<socket_sipc_open_failed_msgs_rcvd>\d+)$')
        
        # Socket new sipc msg messages received   0
        p78 = re.compile(r'^Socket\snew\ssipc\smsg\smessages\sreceived\s+(?P<socket_new_sipc_messages_rcvd>\d+)$')
        
        # Socket unexpected new sipc msg messages received0
        p79 = re.compile(r'^Socket\sunexpected\snew\ssipc\smsg\smessages\sreceived(?P<sock_unexp_nw_sipc_msg_msgs_rcvd>\d+)$')
        
        # Socket server down messages received    0
        p80 = re.compile(r'^Socket\sserver\sdown\smessages\sreceived\s+(?P<socket_ser_down_msg_recvd>\d+)$')
        
        # Socket TX socket ready msgs received    0
        p81 = re.compile(r'^Socket\sTX\ssocket\sready\smsgs\sreceived\s+(?P<socket_tx_socket_ready_msg_recvd>\d+)$')
        
        # Socket TX sock conn failed msgs rcvd    0
        p82 = re.compile(r'^Socket\sTX\ssock\sconn\sfailed\smsgs\srcvd\s+(?P<sock_tx_sockconn_failed_msg_rcvd>\d+)$')
        
        # Socket unknown uds msg msgs received    0
        p83 = re.compile(r'^Socket\sunknown\suds\smsg\smsgs\sreceived\s+(?P<sock_unknown_uds_msg_msgs_rcvd>\d+)$')
        
        # Socket unknown messages received        0
        p84 = re.compile(r'^Socket\sunknown\smessages\sreceived\s+(?P<sock_unknown_msgs_rcvd>\d+)$')
        
        # TX socket messages received             0
        p85 = re.compile(r'^TX\ssocket\smessages\sreceived\s+(?P<tx_sock_msgs_rcvd>\d+)$')
        
        # TX socket resume messages received      0
        p86 = re.compile(r'^TX\ssocket\sresume\smessages\sreceived\s+(?P<tx_sock_resume_msgs_rcvd>\d+)$')
        
        # TX socket unknown messages received     0
        p87 = re.compile(r'^TX\ssocket\sunknown\smessages\sreceived\s+(?P<tx_sock_unknown_msgs_rcvd>\d+)$')
        
        # TX paused                               0
        p88 = re.compile(r'^TX\spaused\s+(?P<tx_paused>\d+)$')
        
        # EBP get buffer local                    0
        p89 = re.compile(r'^EBP\sget\sbuffer\slocal\s+(?P<ebp_get_buffer_local>\d+)$')
        
        # EBP get buffer local error              0
        p90 = re.compile(r'^EBP\sget\sbuffer\slocal\serror\s+(?P<ebp_get_buffer_local_error>\d+)$')
        
        # EBP return buffer local                 0
        p91 = re.compile(r'^EBP\sreturn\sbuffer\slocal\s+(?P<ebp_return_buffer_local>\d+)$')
        
        # EBP return buffer                       0
        p92 = re.compile(r'^EBP\sreturn\sbuffer\s+(?P<ebp_return_buffer>\d+)$')
        
        # Sleep                                   0
        p93 = re.compile(r'^Sleep\s+(?P<sleep>\d+)$')
        
        # Sleep set flag                          0
        p94 = re.compile(r'^Sleep\sset\sflag\s+(?P<sleep_set_flag>\d+)$')
        
        # HTX up                                  0
        p95 = re.compile(r'^HTX\sup\s+(?P<htx_up>\d+)$')
        
        # HTX down                                0
        p96 = re.compile(r'^HTX\sdown\s+(?P<htx_down>\d+)$')
        
        # WCAPI error                             0
        p97 = re.compile(r'^WCAPI\serror\s+(?P<wcapi_error>\d+)$')
        
        # VPL Stats(Engine #1):
        p98 = re.compile(r'^VPL\sStats+\(+\w+\s+\#(?P<engine_number>\d+)(\):)$')
        
        # vPath 802.3 packets received            0
        p99 = re.compile(r'^vPath\s802.3\spackets+\sreceived\s+(?P<vpath_802_3_pkts_rcvd>\d+)$')
        
        # vPath IPv4 packets received             0
        p100 = re.compile(r'^vPath\sIPv4\spackets+\sreceived\s+(?P<vpath_ipv4_pkts_rcvd>\d+)$')
        
        # vPath packets transmitted               0
        p101 = re.compile(r'^vPath\spackets+\stransmitted\s+(?P<vpath_pkts_transmitted>\d+)$')
        
        # vPath IPv4 ping packets received        0
        p102 = re.compile(r'^vPath\sIPv4\sping\spackets+\sreceived\s+(?P<vpath_ipv4_ping_pkts_rcvd>\d+)$')
        
        # vPath version 0 packets received        0
        p103 = re.compile(r'^vPath\sversion\s0\spackets+\sreceived\s+(?P<vpath_ver_0_pkts_rcvd>\d+)$')
        
        # non-snap 802.3 packets received         0
        p104 = re.compile(r'^non-snap\s802.3\spackets+\sreceived\s+(?P<non_snap_802_3_pkts_rcvd>\d+)$')
        
        # non-Cisco 802.3 packets received        0
        p105 = re.compile(r'^non-Cisco\s802.3\spackets+\sreceived\s+(?P<non_cisco_802_3_pkts_rcvd>\d+)$')
        
        # non-IPv4 packets received               0
        p106 = re.compile(r'^non-IPv4\spackets+\sreceived\s+(?P<non_ipv4_pkts_rcvd>\d+)$')
        
        # non-IPv4 UDP packets received           0
        p107 = re.compile(r'^non-IPv4\sUDP\spackets+\sreceived\s+(?P<non_ipv4_udp_pkts_rcvd>\d+)$')
        
        # non-vPath 802.3 packets received        0
        p108 = re.compile(r'^non-vPath\s802.3\spackets+\sreceived\s+(?P<non_vpath_802_3_pkts_rcvd>\d+)$')
        
        # non-vPath dot1q packets received        0
        p109 = re.compile(r'^non-vPath\sdot1q\spackets+\sreceived\s+(?P<non_vpath_dot1q_pkts_rcvd>\d+)$')
        
        # non-vPath IPv4 packets received         0
        p110 = re.compile(r'^non-vPath\sIPv4\spackets\sreceived\s+(?P<non_vpath_ipv4_pkts_rcvd>\d+)$')
        
        # non-vPath IPv4 UDP packets received     0
        p111 = re.compile(r'^non-vPath\sIPv4\sUDP\spackets\sreceived\s+(?P<non_vpath_ipv4_udp_pkts_rcvd>\d+)$')
        
        # non-vPath IPv4 GRE packets received     0
        p112 = re.compile(r'^non-vPath\sIPv4\sGRE\spackets\sreceived\s+(?P<non_vpath_ipv4_gre_pkts_rcvd>\d+)$')
        
        # non-vPath MAC packets received          0
        p113 = re.compile(r'^non-vPath\sMAC\spackets+\sreceived\s+(?P<non_vpath_mac_pkts_rcvd>\d+)$')
        
        # vPath version mismatch packets received 0
        p114 = re.compile(r'^vPath\sversion\smismatch\spackets\sreceived\s+(?P<vpath_ver_mismtch_pkts_rcvd>\d+)$')
        
        # checksum mismatch packets received      0
        p115 = re.compile(r'^checksum\smismatch\spackets\sreceived\s+(?P<checksum_mismtch_pkts_rcvd>\d+)$')
        
        # IP inst fragments                       0
        p116 = re.compile(r'^IP\sinst\sfragments\s+(?P<ip_inst_fragments>\d+)$')
        
        # IP fragmented packets                   0
        p117 = re.compile(r'^IP\sfragmented\spackets\s+(?P<ip_fragmented_packets>\d+)$')
        
        # IP aged fragmented packets              0
        p118 = re.compile(r'^IP\saged\sfragmented\spackets\s+(?P<ip_aged_fragmented_packets>\d+)$')
        
        # IP exceed max fragmented packets        0
        p119 = re.compile(r'^IP\sexceed\smax\sfragmented\spackets\s+(?P<ip_exceed_max_fragmented_packets>\d+)$')
        
        # IP overlapping fragments                0
        p120 = re.compile(r'^IP\soverlapping\sfragments\s+(?P<ip_overlapping_fragments>\d+)$')
        
        # IP exceed fragments per packet          0
        p121 = re.compile(r'^IP\sexceed\sfragments\sper\spacket\s+(?P<ip_exceed_fragments_per_pkt>\d+)$')
        
        # IP exceed length fragmented packets     0
        p122 = re.compile(r'^IP\sexceed\slength\sfragmented\spackets\s+(?P<ip_exceed_len_fragmented_pkt>\d+)$')
        
        # IP tiny fragmented packets              0
        p123 = re.compile(r'^IP\stiny\sfragmented\spackets\s+(?P<ip_tiny_fragmented_pkt>\d+)$')
        
        # IP bad length fragmented packets        0
        p124 = re.compile(r'^IP\sbad\slength\sfragmented\spackets\s+(?P<ip_bad_length_fragmented_pkt>\d+)$')
        
        # L2 inst fragments                       0
        p125 = re.compile(r'^L2\sinst\sfragments\s+(?P<l2_inst_fragments>\d+)$')
        
        # L2 fragmented packets                   0
        p126 = re.compile(r'^L2\sfragmented\spackets\s+(?P<l2_fragmented_packets>\d+)$')
        
        # L2 aged fragmented packets              0
        p127 = re.compile(r'^L2\saged\sfragmented\spackets\s+(?P<l2_aged_fragmented_packets>\d+)$')
        
        # L2 exceed max fragmented packets        0
        p128 = re.compile(r'^L2\sexceed\smax\sfragmented\spackets\s+(?P<l2_exceed_max_fragmented_packets>\d+)$')
        
        # L2 overlapping fragments                0
        p129 = re.compile(r'^L2\soverlapping\sfragments\s+(?P<l2_overlapping_fragments>\d+)$')
        
        # L2 exceed fragments per packet          0
        p130 = re.compile(r'^L2\sexceed\sfragments\sper\spacket\s+(?P<l2_exceed_fragments_per_pkt>\d+)$')
        
        # L2 exceed length fragmented packets     0
        p131 = re.compile(r'^L2\sexceed\slength\sfragmented\spackets\s+(?P<l2_exceed_len_fragmented_pkt>\d+)$')
        
        # L2 tiny fragmented packets              0
        p132 = re.compile(r'^L2\stiny\sfragmented\spackets\s+(?P<l2_tiny_fragmented_pkt>\d+)$')
        
        # L2 bad length fragmented packets        0
        p133 = re.compile(r'^L2\sbad\slength\sfragmented\spackets\s+(?P<l2_bad_length_fragmented_pkt>\d+)$')
        
        # decap packet API calls                  0
        p134 = re.compile(r'^decap\spacket\sAPI\scalls\s+(?P<deacp_pkt_api_calls>\d+)$')
        
        # encap gen packet API calls              0
        p135 = re.compile(r'^encap\sgen\spacket\sAPI\scalls\s+(?P<encap_gen_pkt_api_calls>\d+)$')
        
        # encap nw packet API calls               0
        p136 = re.compile(r'^encap\snw\spacket\sAPI\scalls\s+(?P<encap_nw_pkt_api_calls>\d+)$')
        
        # decap packet API errors                 0
        p137 = re.compile(r'^decap\spacket\sAPI\serrors\s+(?P<deacp_pkt_api_errors>\d+)$')
        
        # encap gen API errors                    0
        p138 = re.compile(r'^encap\sgen\sAPI\serrors\s+(?P<encap_gen_api_errors>\d+)$')
        
        # encap nw API errors                     0
        p139 = re.compile(r'^encap\snw\sAPI\serrors\s+(?P<encap_nw_api_errors>\d+)$')
        
        # IOS-XE DAQ CP Counters(Engine #1):
        p140 = re.compile(r'^IOS-XE\sDAQ\sCP\sCounters\(+\w+\s+\#(?P<engine_number>\d+)(\):)$')
        
        # Packets received                        :3488
        p141 = re.compile(r'^Packets\sreceived\s+:(?P<packet_received>\d+)$')
        
        # Bytes received                          :237156
        p142 = re.compile(r'^Bytes\sreceived\s+:(?P<bytes_received>\d+)$')
        
        # Packets transmitted                     :3488
        p143 = re.compile(r'^Packets\stransmitted\s+:(?P<packets_transmitted>\d+)$')
        
        # Bytes transmitted                       :362688
        p144 = re.compile(r'^Bytes\stransmitted\s+:(?P<bytes_transmitted>\d+)$')
        
        # Memory allocation                       :3490
        p145 = re.compile(r'^Memory\sallocation\s+:(?P<memory_allocation>\d+)$')
        
        # Memory free                             :3488
        p146 = re.compile(r'^Memory\sfree\s+:(?P<memory_free>\d+)$')
        
        # VPL API error                           :0
        p147 = re.compile(r'^VPL\sAPI\serror\s+:(?P<vpl_api_error>\d+)$')
        
        # RX ring full                            0
        p148 = re.compile(r'^RX\sring\sfull\s+(?P<rx_ring_full>\d+)$')
        
        # Memory status changed to yellow         :0
        p149 = re.compile(r'^Memory\sstatus\schanged\sto\syellow\s+:(?P<memry_status_changed_to_yellow>\d+)$')
        
        # Memory status changed to red            :0
        p150 = re.compile(r'^Memory\sstatus\schanged\sto\sred\s+:(?P<memry_status_changed_to_red>\d+)$')
        
        # Process restart notifications           :0
        p151 = re.compile(r'^Process\srestart\snotifications\s+:(?P<process_restart_notifications>\d+)$')

        for line in output.splitlines():
            line = line.strip()
         
            # IOS-XE DAQ Counters(Engine #1):
            m = p1.match(line)
            if m:
                group=m.groupdict()
                engine_number = group['engine_number']
                engine_dict = ret_dict.setdefault('engine_number', {})
                daq_counters_dict = engine_dict.setdefault(engine_number, {}).setdefault('ios_xe_daq_counters', {})
                storage_dict = daq_counters_dict
                continue
            
            # Frames received
            m = p2.match(line)
            if m:
                groups=m.groupdict()
                daq_counters_dict['frames_recevd']=int(groups['frames_recevd'])
                continue

            # Bytes received                          0
            m = p3.match(line)
            if m:
                groups=m.groupdict()
                daq_counters_dict['bytes_recevd']=int(groups['bytes_recevd'])
                continue
            
            # RX frames released                      0
            m = p4.match(line)
            if m:
                groups=m.groupdict()
                daq_counters_dict['rx_frames_released']=int(groups['rx_frames_released'])
                continue
            
            # Packets after vPath decap               0
            m = p5.match(line)
            if m:
                groups=m.groupdict()
                daq_counters_dict['pkts_after_vpath_decap']=int(groups['pkts_after_vpath_decap'])
                continue
            
            # Bytes after vPath decap                 0
            m = p6.match(line)
            if m:
                groups=m.groupdict()
                daq_counters_dict['bytes_after_vpath_decap']=int(groups['bytes_after_vpath_decap'])
                continue
            
            # Packets before vPath encap              0
            m = p7.match(line)
            if m:
                groups=m.groupdict()
                daq_counters_dict['pkts_before_vpath_encap']=int(groups['pkts_before_vpath_encap'])
                continue
            
            # Bytes before vPath encap                0
            m = p8.match(line)
            if m:
                groups=m.groupdict()
                daq_counters_dict['bytes_before_vpath_encap']=int(groups['bytes_before_vpath_encap'])
                continue
            
            # Frames transmitted                      0
            m = p9.match(line)
            if m:
                groups=m.groupdict()
                daq_counters_dict['frames_transmitted']=int(groups['frames_transmitted'])
                continue
            
            # Bytes transmitted                       0
            m = p10.match(line)
            if m:
                groups=m.groupdict()
                daq_counters_dict['bytes_transmitted']=int(groups['bytes_transmitted'])
                continue
            
            # Frames injected                         0
            m = p11.match(line)
            if m:
                groups=m.groupdict()
                daq_counters_dict['frames_injected']=int(groups['frames_injected'])
                continue
            
            # Bytes injected                          0
            m = p12.match(line)
            if m:
                groups=m.groupdict()
                daq_counters_dict['bytes_injected']=int(groups['bytes_injected'])
                continue
            
            # Memory allocation                       388
            m = p13.match(line)
            if m:
                groups=m.groupdict()
                storage_dict['memory_allocation']=int(groups['memory_allocation'])
                continue
            
            # Memory free                             0
            m = p14.match(line)
            if m:
                groups=m.groupdict()
                storage_dict['memory_free']=int(groups['memory_free'])
                continue
            
            # Memory free via timer                   0
            m = p15.match(line)
            if m:
                groups=m.groupdict()
                daq_counters_dict['memry_free_via_timer']=int(groups['memry_free_via_timer'])
                continue
            
            # Merged packet buffer allocation         0
            m = p16.match(line)
            if m:
                groups=m.groupdict()
                daq_counters_dict['merged_pkt_buffer_allocation']=int(groups['merged_pkt_buffer_allocation'])
                continue
            
            # Merged packet buffer free               0
            m = p17.match(line)
            if m:
                groups=m.groupdict()
                daq_counters_dict['merged_pkt_buffer_free']=int(groups['merged_pkt_buffer_free'])
                continue
            
            # VPL buffer allocation                   0
            m = p18.match(line)
            if m:
                groups=m.groupdict()
                daq_counters_dict['vpl_buffer_allocation']=int(groups['vpl_buffer_allocation'])
                continue
            
            # VPL buffer free                         0
            m = p19.match(line)
            if m:
                groups=m.groupdict()
                daq_counters_dict['vpl_buffer_free']=int(groups['vpl_buffer_free'])
                continue
            
            # VPL buffer expand                       0
            m = p20.match(line)
            if m:
                groups=m.groupdict()
                daq_counters_dict['vpl_buffer_expand']=int(groups['vpl_buffer_expand'])
                continue
            
            # VPL buffer merge                        0
            m = p21.match(line)
            if m:
                groups=m.groupdict()
                daq_counters_dict['vpl_buffer_merge']=int(groups['vpl_buffer_merge'])
                continue
            
            # VPL buffer split                        0
            m = p22.match(line)
            if m:
                groups=m.groupdict()
                daq_counters_dict['vpl_buffer_split']=int(groups['vpl_buffer_split'])
                continue
            
            # VPL packet incomplete                   0
            m = p23.match(line)
            if m:
                groups=m.groupdict()
                daq_counters_dict['vpl_pkt_incomplete']=int(groups['vpl_pkt_incomplete'])
                continue
            
            # VPL API error                           0
            m = p24.match(line)
            if m:
                groups=m.groupdict()
                daq_counters_dict['vpl_api_error']=int(groups['vpl_api_error'])
                continue
            
            # Internal error                          0
            m = p25.match(line)
            if m:
                groups=m.groupdict()
                storage_dict['internal_error']=int(groups['internal_error'])
                continue
            
            # External error                          0
            m = p26.match(line)
            if m:
                groups=m.groupdict()
                storage_dict['external_error']=int(groups['external_error'])
                continue
            
            # Memory error                            0
            m = p27.match(line)
            if m:
                groups=m.groupdict()
                storage_dict['memory_error']=int(groups['memory_error'])
                continue
            
            # Timer error                             0
            m = p28.match(line)
            if m:
                groups=m.groupdict()
                storage_dict['timer_error']=int(groups['timer_error'])
                continue
            
            # SPPI Receive Packet error               0
            m = p29.match(line)
            if m:
                groups=m.groupdict()
                daq_counters_dict['sppi_receive_pkt_error']=int(groups['sppi_receive_pkt_error'])
                continue
            
            # SPPI Acquire Transmit Packet error      0
            m = p30.match(line)
            if m:
                groups=m.groupdict()
                daq_counters_dict['sppi_acquire_pkt_error']=int(groups['sppi_acquire_pkt_error'])
                continue
            
            # SPPI Inject Transmit Packet error       0
            m = p31.match(line)
            if m:
                groups=m.groupdict()
                daq_counters_dict['sppi_inject_pkt_error']=int(groups['sppi_inject_pkt_error'])
                continue
            
            # SPPI Encap Transmit Packet error        0
            m = p32.match(line)
            if m:
                groups=m.groupdict()
                daq_counters_dict['sppi_encap_transmit_pkt_error']=int(groups['sppi_encap_transmit_pkt_error'])
                continue
            
            # SPPI Internal error                     0
            m = p33.match(line)
            if m:
                groups=m.groupdict()
                daq_counters_dict['sppi_internal_error']=int(groups['sppi_internal_error'])
                continue
            
            # Kernel frames received                  0
            m = p34.match(line)
            if m:
                groups=m.groupdict()
                daq_counters_dict['kernel_frames_rcvd']=int(groups['kernel_frames_rcvd'])
                continue
            
            # Kernel frames dropped                   0
            m = p35.match(line)
            if m:
                groups=m.groupdict()
                daq_counters_dict['kernel_frames_drp']=int(groups['kernel_frames_drp'])
                continue
            
            # IOS-XE DAQ WCAPI Counters (Engine #1):
            m = p36.match(line)
            if m:
                group=m.groupdict()
                daq_wcapi_counters_dict = engine_dict.setdefault(engine_number, {}).setdefault('ios_xe_daq_wcapi_counters', {})
                storage_dict = daq_wcapi_counters_dict
                continue
            
            # Messages received                       0
            m = p37.match(line)
            if m:
                groups=m.groupdict()
                daq_wcapi_counters_dict['mesages_recevd']=int(groups['mesages_recevd'])
                continue
            
            # Messages transmitted                    0
            m = p38.match(line)
            if m:
                groups=m.groupdict()
                daq_wcapi_counters_dict['messages_transmitted']=int(groups['messages_transmitted'])
                continue
            
            # Flow create received                    0
            m = p39.match(line)
            if m:
                groups=m.groupdict()
                daq_wcapi_counters_dict['flow_create_recvd']=int(groups['flow_create_recvd'])
                continue
            
            # Flow create transmitted                 0
            m = p40.match(line)
            if m:
                groups=m.groupdict()
                daq_wcapi_counters_dict['flow_create_transmitted']=int(groups['flow_create_transmitted'])
                continue
            
            # Flow close received                     0
            m = p41.match(line)
            if m:
                groups=m.groupdict()
                daq_wcapi_counters_dict['flow_close_recvd']=int(groups['flow_close_recvd'])
                continue
            
            # Flow close transmitted                  0
            m = p42.match(line)
            if m:
                groups=m.groupdict()
                daq_wcapi_counters_dict['flow_close_transmitted']=int(groups['flow_close_transmitted'])
                continue
            
            # Flow data received                      0
            m = p43.match(line)
            if m:
                groups=m.groupdict()
                daq_wcapi_counters_dict['flow_data_recvd']=int(groups['flow_data_recvd'])
                continue
            
            # Flow data bytes received                0
            m = p44.match(line)
            if m:
                groups=m.groupdict()
                daq_wcapi_counters_dict['flow_data_bytes_recvd']=int(groups['flow_data_bytes_recvd'])
                continue
            
            # Flow data transmitted                   0
            m = p45.match(line)
            if m:
                groups=m.groupdict()
                daq_wcapi_counters_dict['flow_data_transmitted']=int(groups['flow_data_transmitted'])
                continue
            
            # Flow data bytes transmitted             0
            m = p46.match(line)
            if m:
                groups=m.groupdict()
                daq_wcapi_counters_dict['flow_data_bytes_transmitted']=int(groups['flow_data_bytes_transmitted'])
                continue
            
            # Flow delete received                    0
            m = p47.match(line)
            if m:
                groups=m.groupdict()
                daq_wcapi_counters_dict['flow_delete_recevd']=int(groups['flow_delete_recevd'])
                continue
            
            # Unknown type messages received          0
            m = p48.match(line)
            if m:
                groups=m.groupdict()
                daq_wcapi_counters_dict['unknown_type_msgs_rcvd']=int(groups['unknown_type_msgs_rcvd'])
                continue
            
            # EBP cleanup received                    0
            m = p49.match(line)
            if m:
                groups=m.groupdict()
                daq_wcapi_counters_dict['ebp_cleanup_recvd']=int(groups['ebp_cleanup_recvd'])
                continue
            
            # EBP cleanup transmitted                 0
            m = p50.match(line)
            if m:
                groups=m.groupdict()
                daq_wcapi_counters_dict['ebp_cleanup_transmitted']=int(groups['ebp_cleanup_transmitted'])
                continue
            
            # Flow control injected                   0
            m = p51.match(line)
            if m:
                groups=m.groupdict()
                daq_wcapi_counters_dict['flow_control_injected']=int(groups['flow_control_injected'])
                continue
            
            # Flow data injected                      0
            m = p52.match(line)
            if m:
                groups=m.groupdict()
                daq_wcapi_counters_dict['flow_data_injected']=int(groups['flow_data_injected'])
                continue
            
            # Flow data bytes injected                0
            m = p53.match(line)
            if m:
                groups=m.groupdict()
                daq_wcapi_counters_dict['flow_data_bytes_injected']=int(groups['flow_data_bytes_injected'])
                continue
            
            # Verdict allow                           0
            m = p54.match(line)
            if m:
                groups=m.groupdict()
                daq_wcapi_counters_dict['verdict_allow']=int(groups['verdict_allow'])
                continue
            
            # Verdict deny                            0
            m = p55.match(line)
            if m:
                groups=m.groupdict()
                daq_wcapi_counters_dict['verdict_deny']=int(groups['verdict_deny'])
                continue
            
            # Decryption policy verdict no-decrypt    0
            m = p56.match(line)
            if m:
                groups=m.groupdict()
                daq_wcapi_counters_dict['decrypt_policy_ver_no_decrypt']=int(groups['decrypt_policy_ver_no_decrypt'])
                continue
            
            # Decryption policy verdict decrypt       0
            m = p57.match(line)
            if m:
                groups=m.groupdict()
                daq_wcapi_counters_dict['decrypt_policy_ver_decrypt']=int(groups['decrypt_policy_ver_decrypt'])
                continue
            
            # Decryption policy verdict passthrough   0
            m = p58.match(line)
            if m:
                groups=m.groupdict()
                daq_wcapi_counters_dict['decrypt_policy_ver_passthrough']=int(groups['decrypt_policy_ver_passthrough'])
                continue
            
            # Decryption policy verdict unknown       0
            m = p59.match(line)
            if m:
                groups=m.groupdict()
                daq_wcapi_counters_dict['decrypt_policy_ver_unknown']=int(groups['decrypt_policy_ver_unknown'])
                continue
            
            # Flow create                             0
            m = p60.match(line)
            if m:
                groups=m.groupdict()
                daq_wcapi_counters_dict['flow_create']=int(groups['flow_create'])
                continue
            
            # Flow delete                             0
            m = p61.match(line)
            if m:
                groups=m.groupdict()
                daq_wcapi_counters_dict['flow_delete']=int(groups['flow_delete'])
                continue
            
            # Flow duplicate                          0
            m = p62.match(line)
            if m:
                groups=m.groupdict()
                daq_wcapi_counters_dict['flow_duplicate']=int(groups['flow_duplicate'])
                continue
            
            # Flow data not found                     0
            m = p63.match(line)
            if m:
                groups=m.groupdict()
                daq_wcapi_counters_dict['flow_data_not_found']=int(groups['flow_data_not_found'])
                continue
            
            # Flow close not found                    0
            m = p64.match(line)
            if m:
                groups=m.groupdict()
                daq_wcapi_counters_dict['flow_close_not_found']=int(groups['flow_close_not_found'])
                continue
            
            # Flow delete not found                   0
            m = p65.match(line)
            if m:
                groups=m.groupdict()
                daq_wcapi_counters_dict['flow_delete_not_found']=int(groups['flow_delete_not_found'])
                continue
            
            # Flow enqueue                            0
            m = p66.match(line)
            if m:
                groups=m.groupdict()
                daq_wcapi_counters_dict['flow_enqueue']=int(groups['flow_enqueue'])
                continue
            
            # Flow dequeue                            0
            m = p67.match(line)
            if m:
                groups=m.groupdict()
                daq_wcapi_counters_dict['flow_dequeue']=int(groups['flow_dequeue'])
                continue
            
            # Retry enqueue                           0
            m = p68.match(line)
            if m:
                groups=m.groupdict()
                daq_wcapi_counters_dict['retry_enqueue']=int(groups['retry_enqueue'])
                continue
            
            # Retry dequeue                           0
            m = p69.match(line)
            if m:
                groups=m.groupdict()
                daq_wcapi_counters_dict['retry_dequeue']=int(groups['retry_dequeue'])
                continue
            
            # Retry hold flow                         0
            m = p70.match(line)
            if m:
                groups=m.groupdict()
                daq_wcapi_counters_dict['retry_hold_flow']=int(groups['retry_hold_flow'])
                continue
            
            # Retry release flow                      0
            m = p71.match(line)
            if m:
                groups=m.groupdict()
                daq_wcapi_counters_dict['retry_release_flow']=int(groups['retry_release_flow'])
                continue
            
            # Retry add flow                          0
            m = p72.match(line)
            if m:
                groups=m.groupdict()
                daq_wcapi_counters_dict['retry_add_flow']=int(groups['retry_add_flow'])
                continue
            
            # Closed enqueue                          0
            m = p73.match(line)
            if m:
                groups=m.groupdict()
                daq_wcapi_counters_dict['closed_enqueue']=int(groups['closed_enqueue'])
                continue
            
            # Closed dequeue                          0
            m = p74.match(line)
            if m:
                groups=m.groupdict()
                daq_wcapi_counters_dict['closed_dequeue']=int(groups['closed_dequeue'])
                continue
            
            # Socket messages received                0
            m = p75.match(line)
            if m:
                groups=m.groupdict()
                daq_wcapi_counters_dict['socket_msg_recvd']=int(groups['socket_msg_recvd'])
                continue
            
            # Socket server ready messages received   0
            m = p76.match(line)
            if m:
                groups=m.groupdict()
                daq_wcapi_counters_dict['socket_ser_ready_msg_recvd']=int(groups['socket_ser_ready_msg_recvd'])
                continue
            
            # Socket sipc open failed msgs received   0
            m = p77.match(line)
            if m:
                groups=m.groupdict()
                daq_wcapi_counters_dict['socket_sipc_open_failed_msgs_rcvd']=int(groups['socket_sipc_open_failed_msgs_rcvd'])
                continue
            
            # Socket new sipc msg messages received   0
            m = p78.match(line)
            if m:
                groups=m.groupdict()
                daq_wcapi_counters_dict['socket_new_sipc_messages_rcvd']=int(groups['socket_new_sipc_messages_rcvd'])
                continue
            
            # Socket unexpected new sipc msg messages received0
            m = p79.match(line)
            if m:
                groups=m.groupdict()
                daq_wcapi_counters_dict['sock_unexp_nw_sipc_msg_msgs_rcvd']=int(groups['sock_unexp_nw_sipc_msg_msgs_rcvd'])
                continue
            
            # Socket server down messages received    0
            m = p80.match(line)
            if m:
                groups=m.groupdict()
                daq_wcapi_counters_dict['socket_ser_down_msg_recvd']=int(groups['socket_ser_down_msg_recvd'])
                continue
            
            # Socket TX socket ready msgs received    0
            m = p81.match(line)
            if m:
                groups=m.groupdict()
                daq_wcapi_counters_dict['socket_tx_socket_ready_msg_recvd']=int(groups['socket_tx_socket_ready_msg_recvd'])
                continue
            
            # Socket TX sock conn failed msgs rcvd    0
            m = p82.match(line)
            if m:
                groups=m.groupdict()
                daq_wcapi_counters_dict['sock_tx_sockconn_failed_msg_rcvd']=int(groups['sock_tx_sockconn_failed_msg_rcvd'])
                continue
            
            # Socket unknown uds msg msgs received    0
            m = p83.match(line)
            if m:
                groups=m.groupdict()
                daq_wcapi_counters_dict['sock_unknown_uds_msg_msgs_rcvd']=int(groups['sock_unknown_uds_msg_msgs_rcvd'])
                continue
            
            # Socket unknown messages received        0
            m = p84.match(line)
            if m:
                groups=m.groupdict()
                daq_wcapi_counters_dict['sock_unknown_msgs_rcvd']=int(groups['sock_unknown_msgs_rcvd'])
                continue
            
            # TX socket messages received             0
            m = p85.match(line)
            if m:
                groups=m.groupdict()
                daq_wcapi_counters_dict['tx_sock_msgs_rcvd']=int(groups['tx_sock_msgs_rcvd'])
                continue
            
            # TX socket resume messages received      0
            m = p86.match(line)
            if m:
                groups=m.groupdict()
                daq_wcapi_counters_dict['tx_sock_resume_msgs_rcvd']=int(groups['tx_sock_resume_msgs_rcvd'])
                continue
            
            # TX socket unknown messages received     0
            m = p87.match(line)
            if m:
                groups=m.groupdict()
                daq_wcapi_counters_dict['tx_sock_unknown_msgs_rcvd']=int(groups['tx_sock_unknown_msgs_rcvd'])
                continue
            
            # TX paused                               0
            m = p88.match(line)
            if m:
                groups=m.groupdict()
                daq_wcapi_counters_dict['tx_paused']=int(groups['tx_paused'])
                continue
            
            # EBP get buffer local                    0
            m = p89.match(line)
            if m:
                groups=m.groupdict()
                daq_wcapi_counters_dict['ebp_get_buffer_local']=int(groups['ebp_get_buffer_local'])
                continue
            
            # EBP get buffer local error              0
            m = p90.match(line)
            if m:
                groups=m.groupdict()
                daq_wcapi_counters_dict['ebp_get_buffer_local_error']=int(groups['ebp_get_buffer_local_error'])
                continue
            
            # EBP return buffer local                 0
            m = p91.match(line)
            if m:
                groups=m.groupdict()
                daq_wcapi_counters_dict['ebp_return_buffer_local']=int(groups['ebp_return_buffer_local'])
                continue
            
            # EBP return buffer                       0
            m = p92.match(line)
            if m:
                groups=m.groupdict()
                daq_wcapi_counters_dict['ebp_return_buffer']=int(groups['ebp_return_buffer'])
                continue
            
            # Sleep                                   0
            m = p93.match(line)
            if m:
                groups=m.groupdict()
                daq_wcapi_counters_dict['sleep']=int(groups['sleep'])
                continue
            
            # Sleep set flag                          0
            m = p94.match(line)
            if m:
                groups=m.groupdict()
                daq_wcapi_counters_dict['sleep_set_flag']=int(groups['sleep_set_flag'])
                continue
            
            # HTX up                                  0
            m = p95.match(line)
            if m:
                groups=m.groupdict()
                daq_wcapi_counters_dict['htx_up']=int(groups['htx_up'])
                continue
            
            # HTX down                                0
            m = p96.match(line)
            if m:
                groups=m.groupdict()
                daq_wcapi_counters_dict['htx_down']=int(groups['htx_down'])
                continue
            
            # WCAPI error                             0
            m = p97.match(line)
            if m:
                groups=m.groupdict()
                daq_wcapi_counters_dict['wcapi_error']=int(groups['wcapi_error'])
                continue
            
            # VPL Stats(Engine #1):
            m = p98.match(line)
            if m:
                groups=m.groupdict()
                vpl_stats_dict = engine_dict.setdefault(engine_number, {}).setdefault('vpl_stats', {})
                continue
                
            # vPath 802.3 packets received            0
            m = p99.match(line)
            if m:
                groups=m.groupdict()
                vpl_stats_dict['vpath_802_3_pkts_rcvd']=int(groups['vpath_802_3_pkts_rcvd'])
                continue
                
            # vPath IPv4 packets received             0
            m = p100.match(line)
            if m:
                groups=m.groupdict()
                vpl_stats_dict['vpath_ipv4_pkts_rcvd']=int(groups['vpath_ipv4_pkts_rcvd'])
                continue
                
            # vPath packets transmitted               0
            m = p101.match(line)
            if m:
                groups=m.groupdict()
                vpl_stats_dict['vpath_pkts_transmitted']=int(groups['vpath_pkts_transmitted'])
                continue
            
            # vPath IPv4 ping packets received        0
            m = p102.match(line)
            if m:
                groups=m.groupdict()
                vpl_stats_dict['vpath_ipv4_ping_pkts_rcvd']=int(groups['vpath_ipv4_ping_pkts_rcvd'])
                continue
             
            # vPath version 0 packets received        0
            m = p103.match(line)
            if m:
                groups=m.groupdict()
                vpl_stats_dict['vpath_ver_0_pkts_rcvd']=int(groups['vpath_ver_0_pkts_rcvd'])
                continue
                
            # non-snap 802.3 packets received         0
            m = p104.match(line)
            if m:
                groups=m.groupdict()
                vpl_stats_dict['non_snap_802_3_pkts_rcvd']=int(groups['non_snap_802_3_pkts_rcvd'])
                continue
            
            # non-Cisco 802.3 packets received        0
            m = p105.match(line)
            if m:
                groups=m.groupdict()
                vpl_stats_dict['non_cisco_802_3_pkts_rcvd']=int(groups['non_cisco_802_3_pkts_rcvd'])
                continue   

            # non-IPv4 packets received               0
            m = p106.match(line)
            if m:
                groups=m.groupdict()
                vpl_stats_dict['non_ipv4_pkts_rcvd']=int(groups['non_ipv4_pkts_rcvd'])
                continue
            
            # non-IPv4 UDP packets received           0
            m = p107.match(line)
            if m:
                groups=m.groupdict()
                vpl_stats_dict['non_ipv4_udp_pkts_rcvd']=int(groups['non_ipv4_udp_pkts_rcvd'])
                continue
                
            # non-vPath 802.3 packets received        0
            m = p108.match(line)
            if m:
                groups=m.groupdict()
                vpl_stats_dict['non_vpath_802_3_pkts_rcvd']=int(groups['non_vpath_802_3_pkts_rcvd'])
                continue
                
            # non-vPath dot1q packets received        0
            m = p109.match(line)
            if m:
                groups=m.groupdict()
                vpl_stats_dict['non_vpath_dot1q_pkts_rcvd']=int(groups['non_vpath_dot1q_pkts_rcvd'])
                continue
                
            # non-vPath dot1q packets received        0
            m = p110.match(line)
            if m:
                groups=m.groupdict()
                vpl_stats_dict['non_vpath_ipv4_pkts_rcvd']=int(groups['non_vpath_ipv4_pkts_rcvd'])
                continue
                
            # non-vPath IPv4 UDP packets received     0
            m = p111.match(line)
            if m:
                groups=m.groupdict()
                vpl_stats_dict['non_vpath_ipv4_udp_pkts_rcvd']=int(groups['non_vpath_ipv4_udp_pkts_rcvd'])
                continue
            
            # non-vPath IPv4 GRE packets received     0
            m = p112.match(line)
            if m:
                groups=m.groupdict()
                vpl_stats_dict['non_vpath_ipv4_gre_pkts_rcvd']=int(groups['non_vpath_ipv4_gre_pkts_rcvd'])
                continue
            
            # non-vPath MAC packets received          0
            m = p113.match(line)
            if m:
                groups=m.groupdict()
                vpl_stats_dict['non_vpath_mac_pkts_rcvd']=int(groups['non_vpath_mac_pkts_rcvd'])
                continue
                
            # vPath version mismatch packets received 0
            m = p114.match(line)
            if m:
                groups=m.groupdict()
                vpl_stats_dict['vpath_ver_mismtch_pkts_rcvd']=int(groups['vpath_ver_mismtch_pkts_rcvd'])
                continue
                
            # checksum mismatch packets received      0
            m = p115.match(line)
            if m:
                groups=m.groupdict()
                vpl_stats_dict['checksum_mismtch_pkts_rcvd']=int(groups['checksum_mismtch_pkts_rcvd'])
                continue
            
            # IP inst fragments                       0
            m = p116.match(line)
            if m:
                groups=m.groupdict()
                vpl_stats_dict['ip_inst_fragments']=int(groups['ip_inst_fragments'])
                continue 
                
            # IP fragmented packets                   0
            m = p117.match(line)
            if m:
                groups=m.groupdict()
                vpl_stats_dict['ip_fragmented_packets']=int(groups['ip_fragmented_packets'])
                continue   

            # IP aged fragmented packets              0
            m = p118.match(line)
            if m:
                groups=m.groupdict()
                vpl_stats_dict['ip_aged_fragmented_packets']=int(groups['ip_aged_fragmented_packets'])
                continue 

            # IP exceed max fragmented packets        0
            m = p119.match(line)
            if m:
                groups=m.groupdict()
                vpl_stats_dict['ip_exceed_max_fragmented_packets']=int(groups['ip_exceed_max_fragmented_packets'])
                continue
            
            # IP overlapping fragments                0
            m = p120.match(line)
            if m:
                groups=m.groupdict()
                vpl_stats_dict['ip_overlapping_fragments']=int(groups['ip_overlapping_fragments'])
                continue
            
            # IP overlapping fragments                0
            m = p121.match(line)
            if m:
                groups=m.groupdict()
                vpl_stats_dict['ip_exceed_fragments_per_pkt']=int(groups['ip_exceed_fragments_per_pkt'])
                continue
            
            # IP exceed length fragmented packets     0
            m = p122.match(line)
            if m:
                groups=m.groupdict()
                vpl_stats_dict['ip_exceed_len_fragmented_pkt']=int(groups['ip_exceed_len_fragmented_pkt'])
                continue
            
            # IP tiny fragmented packets              0
            m = p123.match(line)
            if m:
                groups=m.groupdict()
                vpl_stats_dict['ip_tiny_fragmented_pkt']=int(groups['ip_tiny_fragmented_pkt'])
                continue 
            
            # IP bad length fragmented packets        0
            m = p124.match(line)
            if m:
                groups=m.groupdict()
                vpl_stats_dict['ip_bad_length_fragmented_pkt']=int(groups['ip_bad_length_fragmented_pkt'])
                continue  

            # L2 inst fragments                       0
            m = p125.match(line)
            if m:
                groups=m.groupdict()
                vpl_stats_dict['l2_inst_fragments']=int(groups['l2_inst_fragments'])
                continue 
                
            # L2 fragmented packets                   0
            m = p126.match(line)
            if m:
                groups=m.groupdict()
                vpl_stats_dict['l2_fragmented_packets']=int(groups['l2_fragmented_packets'])
                continue   

            # L2 aged fragmented packets              0
            m = p127.match(line)
            if m:
                groups=m.groupdict()
                vpl_stats_dict['l2_aged_fragmented_packets']=int(groups['l2_aged_fragmented_packets'])
                continue 

            # L2 exceed max fragmented packets        0
            m = p128.match(line)
            if m:
                groups=m.groupdict()
                vpl_stats_dict['l2_exceed_max_fragmented_packets']=int(groups['l2_exceed_max_fragmented_packets'])
                continue
            
            # L2 overlapping fragments                0
            m = p129.match(line)
            if m:
                groups=m.groupdict()
                vpl_stats_dict['l2_overlapping_fragments']=int(groups['l2_overlapping_fragments'])
                continue
            
            # L2 overlapping fragments                0
            m = p130.match(line)
            if m:
                groups=m.groupdict()
                vpl_stats_dict['l2_exceed_fragments_per_pkt']=int(groups['l2_exceed_fragments_per_pkt'])
                continue
            
            # L2 exceed length fragmented packets     0
            m = p131.match(line)
            if m:
                groups=m.groupdict()
                vpl_stats_dict['l2_exceed_len_fragmented_pkt']=int(groups['l2_exceed_len_fragmented_pkt'])
                continue
            
            # L2 tiny fragmented packets              0
            m = p132.match(line)
            if m:
                groups=m.groupdict()
                vpl_stats_dict['l2_tiny_fragmented_pkt']=int(groups['l2_tiny_fragmented_pkt'])
                continue 
            
            # L2 bad length fragmented packets        0
            m = p133.match(line)
            if m:
                groups=m.groupdict()
                vpl_stats_dict['l2_bad_length_fragmented_pkt']=int(groups['l2_bad_length_fragmented_pkt'])
                continue 

            # decap packet API calls                  0
            m = p134.match(line)
            if m:
                groups=m.groupdict()
                vpl_stats_dict['deacp_pkt_api_calls']=int(groups['deacp_pkt_api_calls'])
                continue

            # encap gen packet API calls              0
            m = p135.match(line)
            if m:
                groups=m.groupdict()
                vpl_stats_dict['encap_gen_pkt_api_calls']=int(groups['encap_gen_pkt_api_calls'])
                continue

            # encap nw packet API calls               0
            m = p136.match(line)
            if m:
                groups=m.groupdict()
                vpl_stats_dict['encap_nw_pkt_api_calls']=int(groups['encap_nw_pkt_api_calls'])
                continue
            
            # decap packet API errors                 0
            m = p137.match(line)
            if m:
                groups=m.groupdict()
                vpl_stats_dict['deacp_pkt_api_errors']=int(groups['deacp_pkt_api_errors'])
                continue
            
            # encap gen API errors                    0
            m = p138.match(line)
            if m:
                groups=m.groupdict()
                vpl_stats_dict['encap_gen_api_errors']=int(groups['encap_gen_api_errors'])
                continue
            
            # encap nw API errors                    0
            m = p139.match(line)
            if m:
                groups=m.groupdict()
                vpl_stats_dict['encap_nw_api_errors']=int(groups['encap_nw_api_errors'])
                continue
            
            # IOS-XE DAQ CP Counters(Engine #1):
            m = p140.match(line)
            if m:
                groups=m.groupdict()
                daq_cp_counters_dict = engine_dict.setdefault(engine_number, {}).setdefault('ios_xe_daq_cp_counters', {})
                storage_dict = daq_cp_counters_dict
                continue
            
            # Packets received                        :3488
            m = p141.match(line)
            if m:
                groups=m.groupdict()
                daq_cp_counters_dict['packet_received']=int(groups['packet_received'])
                continue

            # Bytes received                          :237156
            m = p142.match(line)
            if m:
                groups=m.groupdict()
                daq_cp_counters_dict['bytes_received']=int(groups['bytes_received'])
                continue
            
            # Packets transmitted                     :3488
            m = p143.match(line)
            if m:
                groups=m.groupdict()
                daq_cp_counters_dict['packets_transmitted']=int(groups['packets_transmitted'])
                continue
                
            # Bytes transmitted                       :362688
            m = p144.match(line)
            if m:
                groups=m.groupdict()
                daq_cp_counters_dict['bytes_transmitted']=int(groups['bytes_transmitted'])
                continue
                
            # Memory allocation                       :3490
            m = p145.match(line)
            if m:
                groups=m.groupdict()
                daq_cp_counters_dict['memory_allocation']=int(groups['memory_allocation'])
                continue
            
            # Memory free                             :3488
            m = p146.match(line)
            if m:
                groups=m.groupdict()
                daq_cp_counters_dict['memory_free']=int(groups['memory_free'])
                continue
                
            # VPL API error                           :0
            m = p147.match(line)
            if m:
                groups=m.groupdict()
                daq_cp_counters_dict['vpl_api_error']=int(groups['vpl_api_error'])
                continue
            
            # RX ring full                            0
            m = p148.match(line)
            if m:
                groups=m.groupdict()
                daq_cp_counters_dict['rx_ring_full']=int(groups['rx_ring_full'])
                continue
            
            # Memory status changed to yellow         :0
            m = p149.match(line)
            if m:
                groups=m.groupdict()
                daq_cp_counters_dict['memry_status_changed_to_yellow']=int(groups['memry_status_changed_to_yellow'])
                continue
            
            # Memory status changed to red            :0
            m = p150.match(line)
            if m:
                groups=m.groupdict()
                daq_cp_counters_dict['memry_status_changed_to_red']=int(groups['memry_status_changed_to_red'])
                continue
                
            # Process restart notifications           :0
            m = p151.match(line)
            if m:
                groups=m.groupdict()
                daq_cp_counters_dict['process_restart_notifications']=int(groups['process_restart_notifications'])
                continue
        return ret_dict

# =========================================================
#  Schema for 'show utd engine standard statistics url'
# =========================================================
class ShowUtdEngineStandardStatisticsUrlSchema(MetaParser):
    ''' show utd engine standard statistics url'''
    schema = {
        'utm_preprocessor_urlf_statistics': {
            'url_filter_request_sent': str,
            'url_filter_response_recvd': str,
            'blacklist_hit_count': str,
            'whitelist_hit_count': str,
            'reputation': {
                'reputation_lookup_count': str,
                'reputation_act_block': str,
                'reputation_act_pass': str,
                'reputation_act_def_pass': str,
                'reputation_act_def_block': str,
                'reputation_score_none': str,
                'reputation_score_out_range': str
            },
            'category': {
                'category_lookup_count': str,
                'category_act_block': str,
                'category_act_pass': str,
                'category_act_def_pass': str,
                'category_act_def_block': str,
                'category_none': str,
                'category_out_range': str
            }
        }
    }


# ========================================================
#  Parser for 'show utd engine standard statistics url'
# ========================================================
class ShowUtdEngineStandardStatisticsUrl(ShowUtdEngineStandardStatisticsUrlSchema):

    """ Parser for "show utd engine standard statistics url" """

    cli_command = "show utd engine standard statistics url"

    def cli(self, output=None):

        if not output:
            output = self.device.execute(self.cli_command)

        utm_data_dict = {}

        # URL Filter Requests Sent: 0 0
        p1 = re.compile(r'^URL\sFilter\sRequests\sSent:\s+(?P<url_filter_request_sent>\d+\s+\d+)$')

        # URL Filter Response Received: 0 0
        p2 = re.compile(r'^URL\sFilter\sResponse\sReceived:\s+(?P<url_filter_response_recvd>\d+\s+\d+)$')

        # Blacklist Hit Count: 0 0
        p3 = re.compile(r'^Blacklist\sHit\sCount:\s+(?P<blacklist_hit_count>\d+\s+\d+)$')

        # Whitelist Hit Count: 0 0
        p4 = re.compile(r'^Whitelist\sHit\sCount:\s+(?P<whitelist_hit_count>\d+\s+\d+)$')

        # Reputation Lookup Count: 0 0
        p5 = re.compile(r'^Reputation\sLookup\sCount:\s+(?P<reputation_lookup_count>\d+\s+\d+)$')

        # Reputation Action Block: 0 0
        p6 = re.compile(r'^Reputation\sAction\sBlock:\s+(?P<reputation_act_block>\d+\s+\d+)$')

        #  Reputation Action Pass: 0 0
        p7 = re.compile(r'^Reputation\sAction\sPass:\s+(?P<reputation_act_pass>\d+\s+\d+)$')

        # Reputation Action Default Pass: 0 0
        p8 = re.compile(r'^Reputation\sAction\sDefault\sPass:\s+(?P<reputation_act_def_pass>\d+\s+\d+)$')

        #  Reputation Action Default Block: 0 0
        p9 = re.compile(r'^Reputation\sAction\sDefault\sBlock:\s+(?P<reputation_act_def_block>\d+\s+\d+)$')

        # Reputation Score None: 0 0
        p10 = re.compile(r'^Reputation\sScore\sNone:\s+(?P<reputation_score_none>\d+\s+\d+)$')

        # Reputation Score Out of Range: 0 0
        p11 = re.compile(r'^Reputation\sScore\sOut\sof\sRange:\s+(?P<reputation_score_out_range>\d+\s+\d+)$')

        # Category Lookup Count: 0 0
        p12 = re.compile(r'^Category\sLookup\sCount:\s+(?P<category_lookup_count>\d+\s+\d+)$')

        # Category Action Block: 0 0
        p13 = re.compile(r'^Category\sAction\sBlock:\s+(?P<category_act_block>\d+\s+\d+)$')

        # Category Action Pass: 0 0
        p14 = re.compile(r'^Category\sAction\sPass:\s+(?P<category_act_pass>\d+\s+\d+)$')

        # Category Action Default Pass: 0 0
        p15 = re.compile(r'^Category\sAction\sDefault\sPass:\s+(?P<category_act_def_pass>\d+\s+\d+)$')

        # Category Action Default Block: 0 0
        p16 = re.compile(r'^Category\sAction\sDefault\sBlock:\s+(?P<category_act_def_block>\d+\s+\d+)$')

        # Category None: 0 0
        p17 = re.compile(r'^Category\sNone:\s+(?P<category_none>\d+\s+\d+)$')

        # Category Out of Range: 0 0
        p18 = re.compile(r'^Category\sOut\sof\sRange:\s+(?P<category_out_range>\d+\s+\d+)$')


        for line in output.splitlines():
            line = line.strip()

            # URL Filter Requests Sent: 0 0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                url_filter_request_sent = group['url_filter_request_sent']
                utm_dict = utm_data_dict.setdefault('utm_preprocessor_urlf_statistics', {})
                utm_dict.setdefault('url_filter_request_sent', url_filter_request_sent)
                continue
            
            # URL Filter Response Received: 0 0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                url_filter_response_recvd = group['url_filter_response_recvd']
                utm_dict['url_filter_response_recvd'] = url_filter_response_recvd
                continue
            
            # Blacklist Hit Count: 0 0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                blacklist_hit_count = group['blacklist_hit_count']
                utm_dict['blacklist_hit_count'] = blacklist_hit_count
                continue
            
            # Whitelist Hit Count: 0 0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                whitelist_hit_count = group['whitelist_hit_count']
                utm_dict['whitelist_hit_count'] = whitelist_hit_count
                continue
            
            # Reputation Lookup Count: 0 0
            m = p5.match(line)
            if m:
                group = m.groupdict()
                reputation_dict = utm_dict.setdefault('reputation', {})
                reputation_lookup_count = group['reputation_lookup_count']
                reputation_dict['reputation_lookup_count'] = reputation_lookup_count
                continue
            
            # Reputation Action Block: 0 0
            m = p6.match(line)
            if m:
                group = m.groupdict()
                reputation_act_block = group['reputation_act_block']
                reputation_dict['reputation_act_block'] = reputation_act_block
                continue
            
            # Reputation Action Pass: 0 0
            m = p7.match(line)
            if m:
                group = m.groupdict()
                reputation_act_pass = group['reputation_act_pass']
                reputation_dict['reputation_act_pass'] = reputation_act_pass
                continue
            
            # Reputation Action Default Pass: 0 0
            m = p8.match(line)
            if m:
                group = m.groupdict()
                reputation_act_def_pass = group['reputation_act_def_pass']
                reputation_dict['reputation_act_def_pass'] = reputation_act_def_pass
                continue
            
            # Reputation Action Default Block: 0 0
            m = p9.match(line)
            if m:
                group = m.groupdict()
                reputation_act_def_block = group['reputation_act_def_block']
                reputation_dict['reputation_act_def_block'] = reputation_act_def_block
                continue
            
            # Reputation Score None: 0 0
            m = p10.match(line)
            if m:
                group = m.groupdict()
                reputation_score_none = group['reputation_score_none']
                reputation_dict['reputation_score_none'] = reputation_score_none
                continue
            
            # Reputation Score Out of Range: 0 0
            m = p11.match(line)
            if m:
                group = m.groupdict()
                reputation_score_out_range = group['reputation_score_out_range']
                reputation_dict['reputation_score_out_range'] = reputation_score_out_range
                continue
            
            
            # Category Lookup Count: 0 0
            m = p12.match(line)
            if m:
                group = m.groupdict()
                category_lookup_count = group['category_lookup_count']
                category_dict = utm_dict.setdefault('category', {})
                category_dict['category_lookup_count'] = category_lookup_count
                continue
            
            # Category Action Block: 0 0
            m = p13.match(line)
            if m:
                group = m.groupdict()
                category_act_block = group['category_act_block']
                category_dict['category_act_block'] = category_act_block
                continue
            
            # Category Action Pass: 0 0
            m = p14.match(line)
            if m:
                group = m.groupdict()
                category_act_pass = group['category_act_pass']
                category_dict['category_act_pass'] = category_act_pass
                continue
            
            # Category Action Default Pass: 0 0
            m = p15.match(line)
            if m:
                group = m.groupdict()
                category_act_def_pass = group['category_act_def_pass']
                category_dict['category_act_def_pass'] = category_act_def_pass
                continue
            
            # Category Action Default Block: 0 0
            m = p16.match(line)
            if m:
                group = m.groupdict()
                category_act_def_block = group['category_act_def_block']
                category_dict['category_act_def_block'] = category_act_def_block
                continue
            
            # Category None: 0 0
            m = p17.match(line)
            if m:
                group = m.groupdict()
                category_none = group['category_none']
                category_dict['category_none'] = category_none
                continue
            
            # Category Out of Range: 0 0
            m = p18.match(line)
            if m:
                group = m.groupdict()
                category_out_range = group['category_out_range']
                category_dict['category_out_range'] = category_out_range
                continue
            
        return utm_data_dict

# ==========================================================================================
# Parser Schema for 'show utd engine standard config'
# ==========================================================================================

class ShowUtdEngineStandardConfigSchema(MetaParser):
    """Schema for "show utd engine standard config" """

    schema = {
        'utd_eng_std_config': {
            'unified_policy': str,
            'url_filtering_cloud_lookup': str,
            'url_filtering_on_box_lookup': str,
            'file_reputation_cloud_lookup': str,
            'file_analysis_cloud_submission': str,
            'utd_tls_decryption_dataplane_policy': str,
            'normalizer': str,
            'flow_logging': str,
            'utd_policy_table_entries': {
                'polciy': {
                    'name': str,
                    'threat_profile': str
                }
            },
            'virtual_port_group_id': int,
            'utd_threat_inspection_profile_table_entries': {
                'threat_profile': {
                    'threat_profile_name': str,
                    'mode': str,
                    'policy': str,
                    'logging_level': str
                }
            }
        }
    }

# ================================================================================
# Parser for 'show utd engine standard config'
# ================================================================================

class ShowUtdEngineStandardConfig(ShowUtdEngineStandardConfigSchema):
    """ parser for "show utd engine standard config" """

    cli_command = "show utd engine standard config"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        parsed_dict = {}

        # Unified Policy: Enabled
        p1 = re.compile(r'^Unified\s+Policy:\s+(?P<status>\w+)$')

        # URL-Filtering Cloud Lookup: Enabled
        p2 = re.compile(r'^URL-Filtering\s+Cloud\s+Lookup:\s+(?P<status>\w+)$')
        
        # URL-Filtering On-box Lookup: Disabled
        p3 = re.compile(r'^URL-Filtering\s+On-box\s+Lookup:\s+(?P<status>\w+)$')
        
        # File-Reputation Cloud Lookup: Disabled
        p4 = re.compile(r'^File-Reputation\s+Cloud\s+Lookup:\s+(?P<status>\w+)$')
        
        # File-Analysis Cloud Submission: Disabled
        p5 = re.compile(r'^File-Analysis\s+Cloud\s+Submission:\s+(?P<status>\w+)$')
        
        # UTD TLS-Decryption Dataplane Policy: Enabled
        p6 = re.compile(r'^UTD\s+TLS-Decryption\s+Dataplane\s+Policy:\s+(?P<status>\w+)$')
        
        # Normalizer: Enabled
        p7 = re.compile(r'^Normalizer:\s+(?P<status>\w+)$')
        
        # Flow Logging: Disabled
        p8 = re.compile(r'^Flow\s+Logging:\s+(?P<status>\w+)$')
        
        # UTD Policy table entries:
        p9 = re.compile(r'^(?P<name>(UTD\s+Policy\s+table\s+entries)|UTD\s+threat-inspection\s+profile\s+table\s+entries):$')
        
        # Policy: AIP1
        p10 = re.compile(r'^Policy:\s+(?P<status>[A-Z0-9]+)$')
        
        # Threat Profile: IPPuni1
        p11 = re.compile(r'^Threat\s+Profile:\s+(?P<status>\w+)$')
        
        # VirtualPortGroup Id: 1
        p12 = re.compile(r'^VirtualPortGroup\s+Id:\s+(?P<status>\w+)$')
        
        # Threat profile: IPPuni1
        p13 = re.compile(r'^Threat\s+profile:\s+(?P<status>\w+)$')
        
        #  Mode: Intrusion Detection
        p14 = re.compile(r'^Mode:\s+(?P<status>[A-Za-z ]+)$')
        
        #  Policy: Balanced
        p15 = re.compile(r'^Policy:\s+(?P<status>[A-Za-z]+)$')
        
        #  Logging level: Error
        p16 = re.compile(r'^Logging\s+level:\s+(?P<status>\w+)$')
        
        for line in output.splitlines():
            line = line.strip()

            # Unified Policy: Enabled
            m = p1.match(line)
            if m:
                group = m.groupdict()
                utd_eng_std_config_dict = parsed_dict.setdefault('utd_eng_std_config', {})
                utd_eng_std_config_dict['unified_policy'] = group['status']
                continue
                
            # URL-Filtering Cloud Lookup: Enabled
            m = p2.match(line)
            if m:
                group = m.groupdict()
                utd_eng_std_config_dict = parsed_dict.setdefault('utd_eng_std_config', {})
                utd_eng_std_config_dict['url_filtering_cloud_lookup'] = group['status']
                continue
            
            # URL-Filtering On-box Lookup: Disabled
            m = p3.match(line)
            if m:
                group = m.groupdict()
                utd_eng_std_config_dict = parsed_dict.setdefault('utd_eng_std_config', {})
                utd_eng_std_config_dict['url_filtering_on_box_lookup'] = group['status']
                continue
            
            # File-Reputation Cloud Lookup: Disabled
            m = p4.match(line)
            if m:
                group = m.groupdict()
                utd_eng_std_config_dict = parsed_dict.setdefault('utd_eng_std_config', {})
                utd_eng_std_config_dict['file_reputation_cloud_lookup'] = group['status']
                continue
            
            # File-Analysis Cloud Submission: Disabled
            m = p5.match(line)
            if m:
                group = m.groupdict()
                utd_eng_std_config_dict = parsed_dict.setdefault('utd_eng_std_config', {})
                utd_eng_std_config_dict['file_analysis_cloud_submission'] = group['status']
                continue
            
            # UTD TLS-Decryption Dataplane Policy: Enabled
            m = p6.match(line)
            if m:
                group = m.groupdict()
                utd_eng_std_config_dict = parsed_dict.setdefault('utd_eng_std_config', {})
                utd_eng_std_config_dict['utd_tls_decryption_dataplane_policy'] = group['status']
                continue
            
            # Normalizer: Enabled
            m = p7.match(line)
            if m:
                group = m.groupdict()
                utd_eng_std_config_dict = parsed_dict.setdefault('utd_eng_std_config', {})
                utd_eng_std_config_dict['normalizer'] = group['status']
                continue
            
            # Flow Logging: Disabled
            m = p8.match(line)
            if m:
                group = m.groupdict()
                utd_eng_std_config_dict = parsed_dict.setdefault('utd_eng_std_config', {})
                utd_eng_std_config_dict['flow_logging'] = group['status']
                continue
            
            # UTD Policy table entries:
            # UTD threat-inspection profile table entries:
            m = p9.match(line)
            if m:
                group = m.groupdict()
                name = group['name'].lower().replace('-','_').replace(' ','_')
                utd_policy_table_entries_dict = utd_eng_std_config_dict.setdefault(name, {})
                table_name = utd_policy_table_entries_dict
                continue
            
            #  Policy: AIP1
            m = p10.match(line)
            if m:
                group = m.groupdict()
                policy_table_name = table_name.setdefault('polciy',{})
                policy_table_name['name'] = group['status']
                continue
            
            # Threat Profile: IPPuni1
            m = p11.match(line)
            if m:
                group = m.groupdict()
                policy_table_name['threat_profile'] = group['status']
                continue
            
            # VirtualPortGroup Id: 1
            m = p12.match(line)
            if m:
                group = m.groupdict()
                utd_eng_std_config_dict['virtual_port_group_id'] = int(group['status'])
                continue
            
            # Threat profile: IPPuni1
            m = p13.match(line)
            if m:
                group = m.groupdict()
                threat_profile_table_name = table_name.setdefault('threat_profile',{})
                threat_profile_table_name['threat_profile_name'] = group['status']
                continue
            
            # Mode: Intrusion Detection
            m = p14.match(line)
            if m:
                group = m.groupdict()
                threat_profile_table_name['mode'] = group['status']
                continue
            
            # Policy: Balanced
            m = p15.match(line)
            if m:
                group = m.groupdict()
                threat_profile_table_name['policy'] = group['status']
                continue
            
            # Logging level: Error
            m = p16.match(line)
            if m:
                group = m.groupdict()
                threat_profile_table_name['logging_level'] = group['status']
                continue
            
        return parsed_dict
