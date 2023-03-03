'''
show_fqdn.py
IOSxe parsers for the following show commands:
        * show fqdn packet statistics
        * show fqdn database
'''
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, ListOf

# ====================================================
# Schema for 'show fqdn packet statistics'
# ====================================================

class ShowFQDNPacketStatisticsSchema(MetaParser):
    """ Schema for show fqdn packet statistics """

    schema = {
        'fqdn_statistics': {
            'pkts_received': {
                'total_dns_pkts_rcvd': int,
                'ipv4_dns_pkts_rcvd': int,
                'ipv6_dns_pkts_rcvd': int
            },
            'total_registered_fqdn': int,
            'total_induced_latency': int,
            'dns_pkt_latency': {
                'min_latency': int,
                'max_latency': int,
                'avg_latency': int
            },
            'pkts_injected': {
                'total_pkts_injected': int,
                'pkts_injected_by_ack': int,
                'pkts_with_parse_error': int,
                'pkts_with_no_answer': int,
                'pkts_with_no_aaaa_record': int,
                'fqdn_not_registered': int,
                'fqdn_already_cached': int
            },
            'total_pkts_dropped_nack': int,
            'avg_input_rate_1_min': int,
            'avg_input_rate_5_min': int,
            'avg_input_rate_1_hr': int
     }        
}

# =============================================
# Parser for 'show fqdn packet statistics'
# =============================================

class ShowFQDNPacketStatistics(ShowFQDNPacketStatisticsSchema):

    cli_command = 'show fqdn packet statistics'

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        # Total DNS Pkts Rcvd                      : 108
        p = re.compile(r'^Total\s+DNS\s+Pkts\s+Rcvd\s+:\s+((?P<total_dns_pkts_rcvd>\d+)$)')

        # IPv4 DNS Pkts Rcvd                   : 108
        p1 = re.compile(r'^IPv4\s+DNS\s+Pkts\s+Rcvd\s+:\s+((?P<ipv4_dns_pkts_rcvd>\d+)$)')

        # IPv6 DNS Pkts Rcvd                   : 0
        p2 = re.compile(r'^IPv6\s+DNS\s+Pkts\s+Rcvd\s+:\s+((?P<ipv6_dns_pkts_rcvd>\d+)$)')

        # Total DNS Pkts for registered FQDNs      : 2
        p3 = re.compile(r'^Total\s+DNS\s+Pkts\s+for\s+registered\s+FQDNs\s+:\s+((?P<total_registered_fqdn>\d+)$)')

        # Total DNS Pkts with induced latency      : 2
        p4 = re.compile(r'^Total\s+DNS\s+Pkts\s+with\s+induced\s+latency\s+:\s+((?P<total_induced_latency>\d+)$)')

        # DNS Packet Latency:
        p5 = re.compile(r'^DNS\s+Packet\s+Latency:$')

        # Min                                  : 12 ms
        p6 = re.compile(r'^Min\s+:\s+((?P<min_latency>\d+)\s+ms$)')

        # Max                                  : 3000 ms
        p7 = re.compile(r'^Max\s+:\s+((?P<max_latency>\d+)\s+ms$)')

        # Avg                                  : 1506 ms
        p8 = re.compile(r'^Avg\s+:\s+((?P<avg_latency>\d+)\s+ms$)')

        # Total DNS Pkts Injected                  : 108
        p9 = re.compile(r'^Total\s+DNS\s+Pkts\s+Injected\s+:\s+((?P<total_pkts_injected>\d+)$)')

        # DNS Pkts Injected by Ack             : 2
        p10 = re.compile(r'^DNS\s+Pkts\s+Injected\s+by\s+Ack\s+:\s+((?P<pkts_injected_by_ack>\d+)$)')

        # DNS Pkts with parse error            : 0
        p11 = re.compile(r'^DNS\s+Pkts\s+with\s+parse\s+error\s+:\s+((?P<pkts_with_parse_error>\d+)$)')

        # DNS Pkts with no answer              : 106
        p12 = re.compile(r'^DNS\s+Pkts\s+with\s+no\s+answer\s+:\s+((?P<pkts_with_no_answer>\d+)$)')

        # DNS Pkts with no A/AAAA Record       : 0
        p13 = re.compile(r'^DNS\s+Pkts\s+with\s+no\s+A/AAAA\s+Record\s+:\s+((?P<pkts_with_no_aaaa_record>\d+)$)')

        # DNS Pkts with FQDN not registered    : 0
        p14 = re.compile(r'^DNS\s+Pkts\s+with\s+FQDN\s+not\s+registered\s+:\s+((?P<fqdn_not_registered>\d+)$)')

        # DNS Pkts with FQDN already cached    : 0
        p15 = re.compile(r'^DNS\s+Pkts\s+with\s+FQDN\s+already\s+cached\s+:\s+((?P<fqdn_already_cached>\d+)$)')

        # Total DNS Pkts Dropped by Nack           : 0
        p16 = re.compile(r'^Total\s+DNS\s+Pkts\s+Dropped\s+by\s+Nack\s+:\s+((?P<total_pkts_dropped_nack>\d+)$)')

        # Average Input rate - 1 min               : 1 pps
        p17 = re.compile(r'^Average\s+Input\s+rate\s+\-\s+1\s+min\s+\:\s+((?P<avg_input_rate_1_min>\d+)\s+pps$)')

        # Average Input rate - 5 min               : 1 pps
        p18 = re.compile(r'^Average\s+Input\s+rate\s+\-\s+5\s+min\s+\:\s+((?P<avg_input_rate_5_min>\d+)\s+pps$)')

        # Average Input rate - 1 hr                : 1 pps
        p19 = re.compile(r'^Average\s+Input\s+rate\s+\-\s+1\s+hr\s+\:\s+((?P<avg_input_rate_1_hr>\d+)\s+pps$)')

        for line in output.splitlines():
            line = line.strip()

            #Total DNS Pkts Rcvd                      : 108
            m = p.match(line)
            if m:
                fqdn_statistics = ret_dict.setdefault('fqdn_statistics',{})
                pkt_statistics = fqdn_statistics.setdefault('pkts_received',{})
                pkt_statistics.update({'total_dns_pkts_rcvd': 
                                        int(m.groupdict()['total_dns_pkts_rcvd'])})
                continue

            #IPv4 DNS Pkts Rcvd                   : 108
            m = p1.match(line)
            if m:
                pkt_statistics.update({'ipv4_dns_pkts_rcvd':
                                        int(m.groupdict()['ipv4_dns_pkts_rcvd'])})
                continue

            #IPv6 DNS Pkts Rcvd                   : 0
            m = p2.match(line)
            if m:
                pkt_statistics.update({'ipv6_dns_pkts_rcvd':
                                        int(m.groupdict()['ipv6_dns_pkts_rcvd'])})
                continue

            #Total DNS Pkts for registered FQDNs      : 2
            m = p3.match(line)
            if m:
                fqdn_statistics.update({'total_registered_fqdn': 
                                         int(m.groupdict()['total_registered_fqdn'])})
                continue

            #Total DNS Pkts with induced latency      : 2
            m = p4.match(line)
            if m:
                fqdn_statistics.update({'total_induced_latency': 
                                         int(m.groupdict()['total_induced_latency'])})
                continue

            #DNS Packet Latency:
            m = p5.match(line)
            if m:
                dns_pkt_latency = fqdn_statistics.setdefault('dns_pkt_latency',{})
                continue

            #     Min                                  : 12 ms
            m = p6.match(line)
            if m:
                dns_pkt_latency.update({'min_latency': int(m.groupdict()['min_latency'])})
                continue

            #     Max                                  : 3000 ms
            m = p7.match(line)
            if m:
                dns_pkt_latency.update({'max_latency': int(m.groupdict()['max_latency'])})
                continue

            #     Avg                                  : 1506 ms
            m = p8.match(line)
            if m:
                dns_pkt_latency.update({'avg_latency': int(m.groupdict()['avg_latency'])})
                continue

            # Total DNS Pkts Injected                  : 108
            m = p9.match(line)
            if m:
                pkts_injected = fqdn_statistics.setdefault('pkts_injected',{})
                pkts_injected.update({'total_pkts_injected':
                                       int(m.groupdict()['total_pkts_injected'])})
                continue

            #     DNS Pkts Injected by Ack             : 2
            m = p10.match(line)
            if m:
                pkts_injected.update({'pkts_injected_by_ack': 
                                       int(m.groupdict()['pkts_injected_by_ack'])})
                continue

            #     DNS Pkts with parse error            : 0
            m = p11.match(line)
            if m:
                pkts_injected.update({'pkts_with_parse_error': 
                                       int(m.groupdict()['pkts_with_parse_error'])})
                continue

            #     DNS Pkts with no answer              : 106
            m = p12.match(line)
            if m:
                pkts_injected.update({'pkts_with_no_answer': 
                                       int(m.groupdict()['pkts_with_no_answer'])})
                continue

            #     DNS Pkts with no A/AAAA Record       : 0
            m = p13.match(line)
            if m:
                pkts_injected.update({'pkts_with_no_aaaa_record': 
                                       int(m.groupdict()['pkts_with_no_aaaa_record'])})
                continue

            #     DNS Pkts with FQDN not registered    : 0
            m = p14.match(line)
            if m:
                pkts_injected.update({'fqdn_not_registered': 
                                       int(m.groupdict()['fqdn_not_registered'])})
                continue

            #     DNS Pkts with FQDN already cached    : 0
            m = p15.match(line)
            if m:
                pkts_injected.update({'fqdn_already_cached': 
                                       int(m.groupdict()['fqdn_already_cached'])})
                continue

           # Total DNS Pkts Dropped by Nack           : 0
            m = p16.match(line)
            if m:
                fqdn_statistics.update({'total_pkts_dropped_nack': 
                                         int(m.groupdict()['total_pkts_dropped_nack'])})
                continue

            # Average Input rate - 1 min               : 1 pps
            m = p17.match(line)
            if m:
                fqdn_statistics.update({'avg_input_rate_1_min': 
                                         int(m.groupdict()['avg_input_rate_1_min'])})
                continue

            # Average Input rate - 5 min               : 1 pps
            m = p18.match(line)
            if m:
                fqdn_statistics.update({'avg_input_rate_5_min': 
                                         int(m.groupdict()['avg_input_rate_5_min'])})
                continue

            # Average Input rate - 1 hr                : 1 pps
            m = p19.match(line)
            if m:
                fqdn_statistics.update({'avg_input_rate_1_hr': 
                                         int(m.groupdict()['avg_input_rate_1_hr'])})
                continue               

        return ret_dict

# ====================================================
# Schema for 'show fqdn database '
# ====================================================

class ShowFQDNDatabaseSchema(MetaParser):
    """ Schema for show fqdn database """

    schema = {
        'fqdn_database': {
            'fqdn_name': {
                Any(): {
                    'ip_address': ListOf(str),
                    'type': ListOf(str),
                    'ttl': ListOf(str),
                    'matched_fqdn': ListOf(str),
                }
            }
        }
    }

# =============================================
# Parser for 'show fqdn database'
# =============================================

class ShowFQDNDatabase(ShowFQDNDatabaseSchema):

    cli_command = 'show fqdn database'

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        # ================ Cached FQDN entries =================
        p = re.compile(r'^\=+\s+Cached\s+FQDN\s+entries\s+\=+$')

        # FQDN Name: *.msft404.com
        p1 = re.compile(r'^FQDN\s+Name:\s+(?P<fqdn_name>[\S]+)$')

        # 4.1.1.24                      IPv4       67/100       1
        # 2001:db8:4:1::1/64            IPv6       77/99        1
        p2 = re.compile(r'^(?P<ip_address>[\S]+)+\s+(?P<type>[\S]+)\s+(?P<ttl>[\S]+)\s+((?P<matched_fqdn>[\S]+)$)')

        for line in output.splitlines():
            line = line.strip()

            # ================ Cached FQDN entries =================
            m = p.match(line)
            if m:
                fqdn_entries = ret_dict.setdefault('fqdn_database', {})
                continue

            # FQDN Name : *.msft404.com
            m = p1.match(line)
            if m:
                fqdn_dict = fqdn_entries.setdefault(
                    'fqdn_name', {}).setdefault(m.groupdict()['fqdn_name'], {})
                continue

            # 4.1.1.24                      IPv4       67/100       1
            # 2001:db8:4:1::1/64            IPv6       77/99        1
            m = p2.match(line)
            if m:
                ip_addres = m.groupdict()['ip_address']
                ip_addres_list = fqdn_dict.setdefault('ip_address', [])
                ip_addres_list.append(ip_addres)

                type_dict = m.groupdict()['type']
                type_list = fqdn_dict.setdefault('type', [])
                type_list.append(type_dict)

                ttl_dict = m.groupdict()['ttl']
                ttl_list = fqdn_dict.setdefault('ttl', [])
                ttl_list.append(ttl_dict)

                matched_fqdn_dict = m.groupdict()['matched_fqdn']
                matched_fqdn_list = fqdn_dict.setdefault('matched_fqdn', [])
                matched_fqdn_list.append(matched_fqdn_dict)
                continue

        return ret_dict
