''' show_mdns.py

IOSXE parsers for the following show commands:
    * show mdns-sd service-peer statistics 
    * show mdns-sd statistics interface vlan {vlan}
    * show mdns-sd statistics vlan {vlan} 
    * show mdns-sd controller statistics
    * show mdns-sd sdg service-peer summary
    * show mdns-sd service-list
    * show mdns-sd query-db
    * show mdns-sd location-group detail
    * show mdns-sd statistics cache vlan {vlan}
    
'''

# Python

import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                         Any, \
                                         ListOf, \
                                         Optional, \
                                         Or, \
                                         And, \
                                         Default, \
                                         Use

# parser utils
from genie.libs.parser.utils.common import Common


# =================
# Schema for:
#  * 'show mdns-sd service-peer statistics'
# =================
class ShowMdnsSdServicePeerStatisticsSchema(MetaParser):
    """Schema for show mdns-sd service-peer statistics"""

    schema = {
        'statistics': {
             Any(): {
                'received': {
                    'total': int,
                    Optional('queries'): {
                        'total': int,
                        'ipv4': int,
                        'ipv6': int
                    },
                    Optional('advertisements'): {
                        'total': int,
                        'ipv4': int,
                        'ipv6': int
                    }
                },
                'sent': {
                    'total': int,
                    Optional('queries'): {
                        Optional('total'): int,
                        Optional('ipv4'): int,
                        Optional('ipv6'): int
                    },
                    Optional('advertisements'): {
                        Optional('total'): int,
                        Optional('ipv4'): int,
                        Optional('ipv6'): int
                    },
                },
            },
        },
    }


# =================
# Parser for:
#  * 'show mdns-sd service-peer statistics'
# =================
class ShowMdnsSdServicePeerStatistics(ShowMdnsSdServicePeerStatisticsSchema):
    '''Parser for show mdns-sd service-peer statistics'''

    cli_command = 'show mdns-sd service-peer statistics'

    def cli(self, output=None):
       
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial variables
        ret_dict = {}

        # mDNS Packet statistics:
        p0 = re.compile(r"^mDNS +Packet +statistics:$")

        # Packets received from client  : 44
        p1 = re.compile(r"^Packets +received +from +(?P<peer_type>\w+) +: +(?P<packet_count>(\d)+)$")

        # IPv4                      : 0
        p2 = re.compile(r"^IPv4 +: +(?P<ipv4_count>[\d]+)$")

        # IPv6                      : 0
        p3 = re.compile(r"^IPv6 +: +(?P<ipv6_count>[\d]+)$")

        # Packets sent to client        : 114
        p4 = re.compile(r"^Packets +sent +to +(?P<peer_type>\w+) +: +(?P<packet_count>[\d]+)$")

        # Advertisements              : 36
        p6 = re.compile(r"^Advertisements +: +(?P<advertisements_count>[\d]+)$")

        # Queries                     : 108
        p7 = re.compile(r"^Queries +: +(?P<queries_count>[\d]+)$")

        for line in out.splitlines():
            line = line.strip()

            # mDNS Packet statistics:
            m = p0.match(line)
            if m:
                statistics = ret_dict.setdefault('statistics', {})
                continue

            # Packets received from client  : 44
            m = p1.match(line)
            if m:
                group = m.groupdict()
                peer_type = group['peer_type']
                packet_count = int(group['packet_count'])
                peer_dict = statistics.setdefault(peer_type, {})\
                                      .setdefault('received', {})
                peer_dict['total'] = packet_count
                continue
                
            # IPv4                      : 0
            m = p2.match(line)
            if m:
                stats_dict['ipv4'] = int(m.groupdict()['ipv4_count'])
                continue
                
            # IPv6                      : 0
            m = p3.match(line)
            if m:
                stats_dict['ipv6'] = int(m.groupdict()['ipv6_count'])
                continue

            # Packets sent to client        : 114
            m = p4.match(line)
            if m:
                group = m.groupdict()
                peer_type = group['peer_type']
                packet_count = int(group['packet_count'])
                peer_dict = statistics.setdefault(peer_type, {})\
                                      .setdefault('sent', {})
                peer_dict['total'] = packet_count
                continue

            # Advertisements              : 36
            m = p6.match(line)
            if m:
                stats_dict = peer_dict.setdefault('advertisements', {})
                stats_dict['total'] = int(m.groupdict()['advertisements_count'])
                continue
                
            # Queries                     : 108
            m = p7.match(line)
            if m:
                stats_dict = peer_dict.setdefault('queries', {})
                stats_dict['total'] = int(m.groupdict()['queries_count'])
                continue

        return ret_dict


# =================
# Schema for:
#  * 'show mdns-sd statistics interface vlan {vlan}'
# =================
class ShowMdnsSdStatisticsInterfaceVlanSchema(MetaParser):
    """Schema for:
        * show mdns-sd statistics interface vlan {vlan}
        * show mdns-sd statistics vlan {vlan}
    """
   
    schema = {
        'statistics': {
            'vlan': {
                Any() : int,
                'mdns_pkt_sent': {
                    'pkt_sent': int,
                    'ipv4_sent': {
                        'ipv4_sent_val': int,
                        'ipv4_adv_sent': int,
                        'ipv4_qry_sent': int,
                    },
                    'ipv6_sent': {
                        'ipv6_sent_val': int,
                        'ipv6_adv_sent': int,
                        'ipv6_qry_sent': int,
                    },
                }, 
                'mdns_pkt_rcvd': {
                    'pkt_rcvd': int,
                    'adv_rcvd': int,
                    'queries_rcvd': {
                        'qry_count': int,
                        'ipv4_rcvd': {
                            'ipv4_rcvd_val': int,
                            'ipv4_adv_rcvd': int,
                            'ipv4_qry_rcvd': int,
                        },
                        'ipv6_rcvd': {
                            'ipv6_rcvd_val': int,
                            'ipv6_adv_rcvd': int,
                            'ipv6_qry_rcvd': int,
                        },
                    },
                },
                'mdns_pkt_drop': int,
                'mdns_rate_lim': int,
                'qry_type': {
                    str : {
                        'qry_type_val': int,
                    },
                },
                Optional('ptr_name'): {
                    str : {
                        'adv_count': int,
                        'qry_count': int,
                    },
                },
            },
        },
    }
    
    
# ===============
# Parser for:
#  * 'show mdns-sd statistics interface vlan {vlan}'
# =================
class ShowMdnsSdStatisticsInterfaceVlan(ShowMdnsSdStatisticsInterfaceVlanSchema):
    '''Parser for show mdns-sd statistics interface vlan {vlan}'''
    
    cli_command = 'show mdns-sd statistics interface vlan {vlan}'

    def cli(self, vlan="", output=None):
        if output is None:
            # get output from device
            out = self.device.execute(self.cli_command.format(vlan=vlan))
        else:
            out = output

        # initial variables
        ret_dict = {}

        # mDNS Packet statistics:
        p0 = re.compile(r"^mDNS +Statistics$")
        
        # Vl301:
        p1 = re.compile(r"^Vl(?P<vlan>(\d)+):$")
        
        # mDNS packets sent                 : 561
        p2 = re.compile(r"^mDNS +packets +sent +: +(?P<pkt_sent>(\d)+)$")
        
        # IPv4 advertisements sent     : 1
        p3 = re.compile(r"^IPv4 +advertisements +sent +: +(?P<ipv4_adv_sent>[\d]+)$")
        
        # IPv4 queries sent
        p4 = re.compile(r"^IPv4 +queries +sent +: +(?P<ipv4_qry_sent>[\d]+)$")
        
        # IPv6 advertisements sent     : 0
        p5 = re.compile(r"^IPv6 +advertisements +sent +: +(?P<ipv6_adv_val>[\d]+)$")
        
        # IPv6 queries sent            : 0
        p6 = re.compile(r"^IPv6 +queries +sent +: +(?P<ipv6_qry_val>[\d]+)$")
        
        # IPv4 sent                      : 561
        p7 = re.compile(r"^IPv4 +sent +: +(?P<ipv4_sent_val>[\d]+)$")
        
        # IPv6 sent                      : 0
        p8 = re.compile(r"^IPv6 +sent +: +(?P<ipv6_sent_val>[\d]+)$")
        
        # mDNS packets received             : 10465
        p9 = re.compile(r"^mDNS +packets +received +: +(?P<pkt_rcvd>(\d)+)$")
        
        # advertisements received          : 5065
        p10 = re.compile(r"^advertisements +received +: +(?P<adv_rcvd>[\d]+)$")
        
        # queries received                 : 5400
        p11 = re.compile(r"^queries received +: +(?P<qry_count>[\d]+)$")
        
        # IPv4 received                  : 10465
        p12 = re.compile(r"^IPv4 +received +: +(?P<ipv4_rcvd_val>[\d]+)$")
        
        # IPv4 advertisements received : 5065
        p13 = re.compile(r"^IPv4 +advertisements +received +: +(?P<ipv4_adv_rcvd>[\d]+)$")
        
        # IPv4 queries received        : 5400
        p14 = re.compile(r"^IPv4 +queries +received +: +(?P<ipv4_qry_rcvd>[\d]+)$")
        
        # IPv6 received                  : 0
        p15 = re.compile(r"^IPv6 +received +: +(?P<ipv6_rcvd_val>[\d]+)$")
        
        # IPv6 advertisements received : 0
        p16 = re.compile(r"^IPv6 +advertisements +received +: +(?P<ipv6_adv_rcvd>[\d]+)$")
        
        # IPv6 queries received        : 0
        p17 = re.compile(r"^IPv6 +queries +received +: +(?P<ipv6_qry_rcvd>[\d]+)$")
        
        # mDNS packets rate limited         : 158
        p18 = re.compile(r"^mDNS +packets +rate +limited +: +(?P<mdns_rate_lim>[\d]+)$")
        
        # mDNS packets dropped              : 298
        p19 = re.compile(r"^mDNS +packets +dropped +: +(?P<mdns_pkt_drop>[\d]+)$")
        
        # PTR                               : 0
        p20 = re.compile(r"^(?P<qry_type>[\w]+) +: +(?P<qry_type_val>[\d]+)$")
        
        # _airplay._tcp.local                                       15         0
        p21 = re.compile(r"^(?P<ptr_name>[\w.-]+)  +(?P<adv_count>[\d]+) +(?P<qry_count>[\d]+)$")
        
        for line in out.splitlines():
            line = line.strip()
            
            # mDNS Packet statistics:
            m = p0.match(line)
            if m:
                statistics = ret_dict.setdefault('statistics', {})
                continue
            
            # Vl301:
            m = p1.match(line)
            if m:
                query_dict = statistics.setdefault('vlan', {})
                query_dict['vlan'] = int(m.groupdict()['vlan'])
                continue
               
            # mDNS packets sent                 : 561
            m = p2.match(line)
            if m:
                vlan_dict = query_dict.setdefault('mdns_pkt_sent', {})
                vlan_dict['pkt_sent'] = int(m.groupdict()['pkt_sent'])
                continue
            
            # IPv4 advertisements sent     : 1
            m = p3.match(line)
            if m:
                stats_dict['ipv4_adv_sent'] = \
                    int(m.groupdict()['ipv4_adv_sent'])
                continue
            
            # IPv4 queries sent
            m = p4.match(line)
            if m:
                stats_dict['ipv4_qry_sent'] = \
                    int(m.groupdict()['ipv4_qry_sent'])
                continue
            
            # IPv6 advertisements sent     : 0
            m = p5.match(line)
            if m:
                stats_dict['ipv6_adv_sent'] = \
                    int(m.groupdict()['ipv6_adv_val'])
                continue
            
            # IPv6 queries sent            : 0
            m = p6.match(line)
            if m:
                stats_dict['ipv6_qry_sent'] = int(m.groupdict()['ipv6_qry_val'])
                continue
            
            # IPv4 sent                      : 561
            m = p7.match(line)
            if m:
                stats_dict = vlan_dict.setdefault('ipv4_sent', {})
                stats_dict['ipv4_sent_val'] = \
                    int(m.groupdict()['ipv4_sent_val'])
                continue
           
            # IPv6 sent                      : 0
            m = p8.match(line)
            if m:
                stats_dict = vlan_dict.setdefault('ipv6_sent', {})
                stats_dict['ipv6_sent_val'] = \
                    int(m.groupdict()['ipv6_sent_val'])
                continue
            
            # mDNS packets received             : 10465
            m = p9.match(line)
            if m:
                vlan_dict = query_dict.setdefault('mdns_pkt_rcvd', {})
                vlan_dict['pkt_rcvd'] = int(m.groupdict()['pkt_rcvd'])
                continue
            
            # advertisements received          : 5065
            m = p10.match(line)
            if m:
                vlan_dict['adv_rcvd'] = int(m.groupdict()['adv_rcvd'])
                continue
            
            # queries received                 : 5400
            m = p11.match(line)
            if m:
                stats_dict = vlan_dict.setdefault('queries_rcvd', {})
                stats_dict['qry_count'] = int(m.groupdict()['qry_count'])
                continue
            
            # IPv4 received                  : 10465
            m = p12.match(line)
            if m:
                rcvd_dict = stats_dict.setdefault('ipv4_rcvd', {})
                rcvd_dict['ipv4_rcvd_val'] = int(m.groupdict()['ipv4_rcvd_val'])
                continue
            
            # IPv4 advertisements received : 5065
            m = p13.match(line)
            if m:
                rcvd_dict['ipv4_adv_rcvd'] = int(m.groupdict()['ipv4_adv_rcvd'])
                continue
            
            # IPv4 queries received        : 5400
            m = p14.match(line)
            if m:
                rcvd_dict['ipv4_qry_rcvd'] = int(m.groupdict()['ipv4_qry_rcvd'])
                continue
            
            # IPv6 received                  : 0
            m = p15.match(line)
            if m:
                rcvd_dict = stats_dict.setdefault('ipv6_rcvd', {})
                rcvd_dict['ipv6_rcvd_val'] = int(m.groupdict()['ipv6_rcvd_val'])
                continue
            
            # IPv6 advertisement received        : 0
            m = p16.match(line)
            if m:
                rcvd_dict['ipv6_adv_rcvd'] = int(m.groupdict()['ipv6_adv_rcvd'])
                continue
            
            # IPv6 queries received        : 0
            m = p17.match(line)
            if m:
                rcvd_dict['ipv6_qry_rcvd'] = int(m.groupdict()['ipv6_qry_rcvd'])
                continue
            
            # mDNS packets rate limited         : 158
            m = p18.match(line)
            if m:
                query_dict['mdns_rate_lim'] = \
                    int(m.groupdict()['mdns_rate_lim'])
                continue
            
            # mDNS packets dropped              : 298
            m = p19.match(line)
            if m:
                query_dict['mdns_pkt_drop'] = \
                    int(m.groupdict()['mdns_pkt_drop'])
                continue
            
            # PTR                               : 0
            m = p20.match(line)
            if m:
                group = m.groupdict()
                qry_types = query_dict.setdefault('qry_type', {})
                qry_type = qry_types.setdefault(group['qry_type'], {})
                qry_type.update({
                    'qry_type_val': int(group['qry_type_val']),
                })
                continue
       
            # _airplay._tcp.local      15  0              
            m = p21.match(line)
            if m:
                group = m.groupdict()
                ptr_names= query_dict.setdefault('ptr_name', {})
                ptr_name = ptr_names.setdefault(group['ptr_name'], {})
                ptr_name.update({
                    'adv_count': int(group['adv_count']),
                    'qry_count': int(group['qry_count']),
                })
                continue
            
        return ret_dict


# ===============
# Parser for:
#  * 'show mdns-sd statistics vlan {vlan}'
# =================
class ShowMdnsSdStatisticsVlan(ShowMdnsSdStatisticsInterfaceVlan):
    '''Parser for show mdns-sd statistics vlan {vlan}'''

    cli_command = 'show mdns-sd statistics vlan {vlan}'

    def cli(self, vlan="",output=None):
        return super().cli(vlan=vlan,output=output)


# =================
# Schema for:
#  * 'show mdns-sd controller statistics'
# =================
class ShowMdnsSdControllerStatisticsSchema(MetaParser):
    """Schema for show mdns-sd controller statistics"""

    schema = {
        'total_msg_sent': int,
        'total_msg_rcvd': int,
        'keepalive_msg_sent': int,
        'keepalive_msg_rcvd': int,
        'intf_withdraw_msg_sent': int,
        'vlan_withdraw_msg_sent': int,
        'clr_cache_msg_sent': int,
        'resync_state_count': int,
        'last_successful_resync': str,
        'srvc_adv': {
            'adv_sent': int,
            'withdraw_sent': int,
            'adv_filter': int,
            'tot_srvc_resync': int,
        },
        'srvc_qry': {
            'qry_sent': int,
            'qry_response_rcvd': int,
        },
    }  
 

# =================
# Parser for:
#  * 'show mdns-sd controller statistics'
# =================
class ShowMdnsSdControllerStatistics(ShowMdnsSdControllerStatisticsSchema):
    '''Parser for show mdns-sd controller statistics''' 
 
    cli_command = 'show mdns-sd controller statistics'    

    def cli(self, output=None):
        
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial variables
        ret_dict = {}
        
        # Total messages sent              : 0
        p0 = re.compile(r"^Total +messages +sent +: +(?P<total_msg_sent>(\d)+)$")
        
        # Total messages received          : 0
        p1 = re.compile(r"^Total +messages +received  +: +(?P<total_msg_rcvd>(\w)+)$")
        
        # Keepalive messages sent          : 0
        p2 = re.compile(r"^Keepalive +messages +sent  +: +(?P<keepalive_msg_sent>(\d)+)$")
        
        # Keepalive messages received      : 0
        p3 = re.compile(r"^Keepalive +messages +received +: +(?P<keepalive_msg_rcvd>[\d]+)$")
        
        # Interface WITHDRAW messages sent : 0
        p4 = re.compile(r"^Interface +WITHDRAW +messages +sent +: +(?P<intf_withdraw_msg_sent>[\d]+)$")
        
        # Vlan WITHDRAW messages sent      : 0
        p5 = re.compile(r"^Vlan +WITHDRAW +messages +sent +: +(?P<vlan_withdraw_msg_sent>[\d]+)$")
        
        # Clear cache messages sent        : 0
        p6 = re.compile(r"^Clear +cache +messages +sent +: +(?P<clr_cache_msg_sent>[\d]+)$")
        
        # Total RESYNC state count         : 0
        p7 = re.compile(r"^Total +RESYNC +state +count +: +(?P<resync_state_count>[\d]+)$")
        
        # Last successful RESYNC           : Not-Applicable
        p8 = re.compile(r"^Last +successful +RESYNC +: +(?P<last_successful_resync>[\w-]+)$")

        # Advertisements sent             : 0
        p9 = re.compile(r"^Advertisements +sent  +: +(?P<adv_sent>[\d]+)$")
        
        # Withdraws sent                  : 0
        p10 = re.compile(r"^Withdraws +sent +: +(?P<withdraw_sent>[\d]+)$")
        
        # Advertisements Filtered         : 0
        p11 = re.compile(r"^Advertisements +Filtered +: +(?P<adv_filter>[\d]+)$")
        
        # Total service resynced          : 0
        p12 = re.compile(r"^Total +service +resynced +: +(?P<tot_srvc_resync>[\d]+)$")
        
        # Queries sent                    : 0
        p13 = re.compile(r"^Queries +sent +: +(?P<qry_sent>[\d]+)$")
        
        # Query responses received        : 0
        p14 = re.compile(r"^Query +responses +received  +: +(?P<qry_response_rcvd>[\d]+)$")
       
        for line in out.splitlines():
            line = line.strip()
            
            # Total messages sent              : 0
            m = p0.match(line)
            if m:
                ret_dict['total_msg_sent'] = \
                    int(m.groupdict()['total_msg_sent'])
                continue

            # Total messages received          : 0
            m = p1.match(line)
            if m:
                ret_dict['total_msg_rcvd'] = \
                    int(m.groupdict()['total_msg_rcvd'])
                continue
            
            # Keepalive messages sent          : 0
            m = p2.match(line)
            if m:
                ret_dict['keepalive_msg_sent'] = \
                    int(m.groupdict()['keepalive_msg_sent'])
                continue
            
            # Keepalive messages received      : 0
            m = p3.match(line)
            if m:
                ret_dict['keepalive_msg_rcvd'] = \
                    int(m.groupdict()['keepalive_msg_rcvd'])
                continue

            # Interface WITHDRAW messages sent : 0
            m = p4.match(line)
            if m:
                ret_dict['intf_withdraw_msg_sent'] = \
                    int(m.groupdict()['intf_withdraw_msg_sent'])
                continue
 
            # Vlan WITHDRAW messages sent      : 0
            m = p5.match(line)         
            if m:
                ret_dict['vlan_withdraw_msg_sent'] = \
                    int(m.groupdict()['vlan_withdraw_msg_sent'])
                continue

            # Clear cache messages sent        : 0
            m = p6.match(line)
            if m:
                ret_dict['clr_cache_msg_sent'] = \
                    int(m.groupdict()['clr_cache_msg_sent'])
                continue

            # Total RESYNC state count         : 0
            m = p7.match(line)
            if m:
                ret_dict['resync_state_count'] = \
                    int(m.groupdict()['resync_state_count'])
                continue
            
            # Last successful RESYNC           : Not-Applicable
            m = p8.match(line)
            if m:
                ret_dict['last_successful_resync'] = \
                    m.groupdict()['last_successful_resync']
                continue
                
            # Advertisements sent             : 0
            m = p9.match(line)
            if m:
                src_dict = ret_dict.setdefault('srvc_adv', {})
                src_dict['adv_sent'] = int(m.groupdict()['adv_sent'])
                continue
                
            # Withdraws sent             : 0
            m = p10.match(line)
            if m:
                src_dict['withdraw_sent'] = int(m.groupdict()['withdraw_sent'])
                continue
            
            # Advertisements Filtered         : 0
            m = p11.match(line)
            if m:
                src_dict['adv_filter'] = int(m.groupdict()['adv_filter'])
                continue
            
            # Total service resynced          : 0
            m = p12.match(line)
            if m:
                src_dict['tot_srvc_resync'] = \
                    int(m.groupdict()['tot_srvc_resync'])
                continue
            
            # Queries sent                    : 0           
            m = p13.match(line)
            if m:
                src_dict = ret_dict.setdefault('srvc_qry', {})
                src_dict['qry_sent'] = int(m.groupdict()['qry_sent'])
                continue
        
            # Queries response received                    : 0
            m = p14.match(line)
            if m:
                src_dict['qry_response_rcvd'] = \
                    int(m.groupdict()['qry_response_rcvd'])
                continue
          
        return ret_dict


# =================
# Schema for:
#  * 'show mdns-sd sdg service-peer summary'
# =================
class ShowMdnsSdSdgServicePeerSummarySchema(MetaParser):
    """Schema for show mdns-sd sdg service-peer summary"""
    
    schema = {
        'sp_address': {
            Any(): {
                'port': int,
                'cache_sync_sent': int,
                'cache_sync_time': str,
                'uptime': str,
                'record_count': int,
            },
        },
    }          
              

# =================
# Parser for:
#  * 'show mdns-sd sdg service-peer summary'
# =================
class ShowMdnsSdSdgServicePeerSummary(ShowMdnsSdSdgServicePeerSummarySchema):
    '''Parser for show mdns-sd sdg service-peer summary'''

    cli_command = 'show mdns-sd sdg service-peer summary'

    def cli(self, output=None):
       
        if output is None:
            # get output from device
            out = out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial variables
        ret_dict = {}

        # 40.1.25.2/10991                                0           NA /May  7 18:08:12 2021               0 Hrs 2  Mins   0
        p0 = re.compile(r"^(?P<sp_address>[\d.]+|[\d:]+)/(?P<port>\d+)\s+(?P<cache_sync_sent>\d+)\s+(?P<cache_sync_time>NA|\w+\s+\d+\s+[\d:]+\s+\d+)\s+(?P<uptime>\d+\s+Hrs\s+\d+\s+Mins)\s+(?P<record_count>\d+)$")

        for line in out.splitlines():
            line = line.strip()
            
            # 40.1.25.2/10991                                0           NA /May  7 18:08:12 2021               0 Hrs 2  Mins   0
            m = p0.match(line)
            if m:
                group = m.groupdict()
                sp_address = group['sp_address']
                sp_dict = ret_dict.setdefault('sp_address', {})\
                                  .setdefault(sp_address, {})
                sp_dict['port']  = int(group['port'])
                sp_dict['cache_sync_sent']  = int(group['cache_sync_sent'])
                sp_dict['cache_sync_time']  = group['cache_sync_time']
                sp_dict['uptime']  = group['uptime']
                sp_dict['record_count']  = int(group['record_count'])
                continue
        
        return ret_dict


# =================
# Schema for:
#  * 'show mdns-sd service-list'
# =================
class ShowMdnsSdServiceListSchema(MetaParser):
    """Schema for show mdns-sd service-list"""
  
    schema = {
        'srvc_list': {
            Any(): {
                'services': {
                    Any(): {
                        'filter_dir': str,
                        'msg_type': str,
                        'source': str,
                        'loc_filter': str,
                    },
                },
            },
        },
    }       


# =================
# Parser for:
#  * 'show mdns-sd service-list'
# =================
class ShowMdnsSdServiceList(ShowMdnsSdServiceListSchema):
    '''Parser for show mdns-sd service-list'''

    cli_command = 'show mdns-sd service-list'

    def cli(self, output=None):
       
        if output is None:
            # get output from device
            out = out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial variables
        ret_dict = {}

        # default-mdns-out-service-list                        OUT         multifunction-printer            any                           ALL              default-mdns-location-filter
        p0 = re.compile(r"^(?P<srvc_list>[\w-]+)\s+(?P<filter_dir>(IN|OUT|CTRL))\s+(?P<srvc>[\w-]+)\s+(?P<msg_type>[\w-]+)\s+(?P<source>(ALL|-))\s+(?P<loc_filter>[\w-]+)$")
        
        # IN                  printer-ipps            any                             -           -
        p1 = re.compile(r"^(?P<filter_dir>(IN|OUT|CTRL))\s+(?P<srvc>[\w-]+)\s+(?P<msg_type>[\w-]+)\s+(?P<source>(ALL|-))\s+(?P<loc_filter>[\w-]+)$")
         
        for line in out.splitlines():
            line = line.strip()
        
            # default-mdns-out-service-list                        OUT         multifunction-printer            any                           ALL              default-mdns-location-filter
            m = p0.match(line)
            if m:
                group = m.groupdict()
                srvc_list = group['srvc_list']
                srvc_dict = ret_dict.setdefault('srvc_list', {})\
                                    .setdefault(srvc_list, {})
                services = srvc_dict.setdefault('services', {})
                srvc = services.setdefault(group['srvc'], {})
                srvc.update({
                    'filter_dir':  m.groupdict()['filter_dir'],
                    'msg_type':  m.groupdict()['msg_type'],
                    'source':  m.groupdict()['source'],
                    'loc_filter': m.groupdict()['loc_filter']
                })
                continue
            
            # IN                  printer-ipps            any                             -           -
            m = p1.match(line)
            if m:
                group = m.groupdict()
                srvc = services.setdefault(group['srvc'], {})
                if group['srvc']:
                    srvc.update({
                        'filter_dir': m.groupdict()['filter_dir'],
                        'msg_type':  m.groupdict()['msg_type'],
                        'source':  m.groupdict()['source'],
                        'loc_filter': m.groupdict()['loc_filter']
                    })
                continue
      
        return ret_dict


# =================
# Schema for:
#  * 'show mdns-sd query-db'
# =================
class ShowMdnsSdQueryDbSchema(MetaParser):
    """Schema for show mdns-sd query-db"""
    
    schema = {
       'query_name':{     
            Any(): {
                'client_mac': str,
                'vlan_id': int,
                'location_id': str,
                'usr_role': str,
            },
        },
    }


# =================
# Parser for:
#  * 'show mdns-sd query-db'
# =================
class ShowMdnsSdQueryDb(ShowMdnsSdQueryDbSchema):
    '''Parser for show mdns-sd query-db'''
    
    cli_command = 'show mdns-sd query-db'

    def cli(self, output=None):
       
        if output is None:
            # get output from device
            out =  self.device.execute(self.cli_command)
        else:
            out = output

        # initial variables
        ret_dict = {}
        
        # PTR Name: _ipp._tcp.local
        p0 = re.compile(r"^PTR Name: +(?P<query_name>[\w.-]+)$")
        
        # 000c.297d.4ed7      851        Default                       none
        p1 = re.compile(r"^(?P<client_mac>([a-zA-Z0-9]+\.){2}[a-zA-Z0-9]+)\s+(?P<vlan_id>[\d]+)\s+(?P<location_id>([\d]+)|[\w]+)\s+(?P<usr_role>[A-Za-z]+)$")
              
        for line in out.splitlines():
            line = line.strip()
            
            # PTR Name: _ipp._tcp.local
            m = p0.match(line)
            if m:
                group = m.groupdict()
                query_name = group['query_name']
                query_dict = ret_dict.setdefault('query_name', {})\
                                     .setdefault(query_name, {})
                continue
                
            # 000c.297d.4ed7      851        Default                       none
            m = p1.match(line)
            if m:
                query_dict['client_mac']  = m.groupdict()['client_mac']
                query_dict['vlan_id']  = int(m.groupdict()['vlan_id'])
                query_dict['location_id']  = m.groupdict()['location_id']
                query_dict['usr_role']  = m.groupdict()['usr_role']
                continue
             
        return ret_dict


# =================
# Schema for:
#  * 'show mdns-sd location-group detail'
# =================
class ShowMdnsSdLocationGroupDetailSchema(MetaParser):
    """Schema for show mdns-sd location-group detail"""
  
    schema = {
        'trust_links': str,
        'vlans_added': str,
        'total_loc_grps': str,
        'vlans': {
            Any(): {
                'no_of_lg': str,
                'lg_ids': {
                    Any(): {
                       'ports': str,
                    },
                },
            },
        },
    }         


# =================
# Parser for:
#  * 'show mdns-sd location-group detail'
# =================
class ShowMdnsSdLocationGroupDetail(ShowMdnsSdLocationGroupDetailSchema):
    '''Parser for show mdns-sd location-group detail'''  

    cli_command = 'show mdns-sd location-group detail'

    def cli(self, output=None):
       
        if output is None:
            # get output from device
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial variables
        ret_dict = {}
         
        # Trusted Trunks         : Te5/0/3 
        p0 = re.compile(r"^Trusted +Trunks\s+: +(?P<trust_links>(([A-Za-z\d\/]+[\d\/])+)|NA)$")
        
        # Vlan's                 : 851-854,1101-1102
        p1 = re.compile(r"^Vlan.*: +(?P<vlans_added>[\d\-,]+)$")
         
        # Total Number of Location Groups: 0
        p2 = re.compile(r"^Total +Number +of +Location +Groups: +(?P<total_loc_grps>([0-9]+))$")
        
        # 851                          1          0       Te5/0/27, 
        p3 = re.compile(r"^(?P<vlans>\d+)\s+(?P<no_of_lg>\d+)\s+(?P<lg_id>\d+)\s+(?P<ports>.*),?$")
        
        # 0       Te5/0/27, 
        p4 = re.compile(r"^(?P<lg_id>\d+)\s+(?P<ports>.*),?$")

        for line in out.splitlines():
            line = line.strip()
            
            # Trusted Trunks         : Te5/0/3 
            m = p0.match(line)
            if m:
                ret_dict['trust_links'] = \
                    Common.convert_intf_name(m.groupdict()['trust_links'])
                continue
                           
            # Vlan's                 : 851-854,1101-1102                    -           -
            m = p1.match(line)
            if m:
                ret_dict['vlans_added'] =  m.groupdict()['vlans_added']
                continue
            
            # Total Number of Location Groups: 0
            m = p2.match(line)
            if m:
                ret_dict['total_loc_grps'] =  m.groupdict()['total_loc_grps']
                continue
            
            # 851                          1          0       Te5/0/27, 
            m = p3.match(line)
            if m:
                group = m.groupdict()
                vlans = group['vlans']
                vlan_dict = ret_dict.setdefault('vlans', {})\
                                    .setdefault(vlans, {})
                vlan_dict['no_of_lg'] = m.groupdict()['no_of_lg']
                lg_ids = vlan_dict.setdefault('lg_ids', {})
                lg_id = lg_ids.setdefault(group['lg_id'], {})
                lg_id.update({
                    'ports': Common.convert_intf_name(m.groupdict()['ports']),
                })
                continue
                
            # 0       Te5/0/27,  
            m = p4.match(line)
            if m:
                group = m.groupdict()
                lg_id = lg_ids.setdefault(group['lg_id'], {})
                if group['lg_id']:
                    lg_id.update({
                        'ports': Common.convert_intf_name(
                            m.groupdict()['ports']),
                    })
                continue
               
        return ret_dict


# =================
# Schema for:
#  * 'show mdns-sd statistics cache vlan {vlan}:'
# =================
class ShowMdnsSdStatisticsCacheVlanSchema(MetaParser):
    """ Schema for:
        * show mdns-sd statistics cache vlan {vlan}
    """

    schema = {
            'number_of_service_types': int, 
            'number_of_records_of_types_PTR':  int,
            'number_of_records_of_types_SRV':  int,
            'number_of_records_of_types_A':  int,
            'number_of_records_of_types_AAAA':  int,
            'number_of_records_of_types_TXT':  int
        }


# =================
# Parser for:
#  * 'show mdns-sd statistics cache vlan {vlan}:'
# =================
class ShowMdnsSdStatisticsCacheVlan(ShowMdnsSdStatisticsCacheVlanSchema):
    """ Parser for
        * show mdns-sd statistics cache vlan {vlan}
    """
    
    cli_command = 'show mdns-sd statistics cache vlan {vlan}'

    def cli(self, vlan="", output=None):
        if output is None:
            # get output from device
            out = self.device.execute(self.cli_command.format(vlan=vlan))
        else:
            out = output
  
        ret_dict = {}
        
        # Number of service types : 14
        p1 = re.compile(r'^Number +of +service +types +: +(?P<srvc_types>\d+)$')
                
        # Number of records of type PTR : 913
        p2 = re.compile(r'^Number +of +records +of +type +PTR +: +(?P<srvc_PTR>\d+)$')
        
        # Number of records of type SRV : 913
        p3 = re.compile(r'^Number +of +records +of +type +SRV +: +(?P<srvc_SRV>\d+)$')

        # Number of records of type A : 78
        p4 = re.compile(r'^Number +of +records +of +type +A +: +(?P<srvc_A>\d+)$')

        # Number of records of type AAAA : 78
        p5 = re.compile(r'^Number +of +records +of +type +AAAA +: +(?P<srvc_AAAA>\d+)$')
        
        # Number of records of type TXT : 913
        p6 = re.compile(r'^Number +of +records +of +type +TXT +: +(?P<srvc_TXT>\d+)$')

        for line in out.splitlines():
            line = line.strip()
            
            # Number of service types : 14
            m1 = p1.match(line)
            if m1:
                group = m1.groupdict()
                ret_dict["number_of_service_types"] = int(group["srvc_types"])
                continue
                
            # Number of records of type PTR : 913    
            m2 = p2.match(line)
            if m2:
                group = m2.groupdict()
                ret_dict["number_of_records_of_types_PTR"] = \
                    int(group["srvc_PTR"])
                continue
                
            # Number of records of type SRV : 913    
            m3 = p3.match(line)
            if m3:
                group = m3.groupdict()
                ret_dict["number_of_records_of_types_SRV"] = \
                    int(group["srvc_SRV"])
                continue
                
            # Number of records of type A : 78
            m4 = p4.match(line)
            if m4:
                group = m4.groupdict()
                ret_dict["number_of_records_of_types_A"] = int(group["srvc_A"])
                continue
                
            # Number of records of type AAAA : 78
            m5 = p5.match(line)
            if m5:
                group = m5.groupdict()
                ret_dict["number_of_records_of_types_AAAA"] = \
                    int(group["srvc_AAAA"])
                continue
                
            # Number of records of type TXT : 913
            m6 = p6.match(line)
            if m6:
                group = m6.groupdict()
                ret_dict["number_of_records_of_types_TXT"] = \
                    int(group["srvc_TXT"])
                continue
                
        return ret_dict
