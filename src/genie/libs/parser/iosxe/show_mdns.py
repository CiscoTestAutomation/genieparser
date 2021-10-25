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
    * show mdns-sd service-policy association vlan 
    * show mdns-sd sp-sdg statistics
    * show mdns-sd statistics cache all 
    * show mdns-sd summary
    * show mdns-sd summary interface vlan
    * show mdns-sd summary vlan
    * show mdns-sd service-policy association role
    * show mdns-sd controller summary
    
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
           output = self.device.execute(self.cli_command)
           
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
       
        for line in output.splitlines():
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
            out = self.device.execute(self.cli_command)
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
            output = self.device.execute(self.cli_command.format(vlan=vlan))
  
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

        for line in output.splitlines():
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
        
class ShowMdnsSdServicePolicyAssociationVlanSchema(MetaParser):
    """ Schema for
    
        * show mdns-sd service-policy association vlan
    """
    schema = {
        'vlan': {
            Any():{
                'service_policy': str
            }
        }
    }
            
class ShowMdnsSdServicePolicyAssociationVlan(ShowMdnsSdServicePolicyAssociationVlanSchema):
    """ Parser for
    
        * show mdns-sd service-policy association vlan
        
    """
    
    cli_command = 'show mdns-sd service-policy association vlan'

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)
        
        ret_dict = {}
        
        #VLAN            Service-policy
        p1 = re.compile(r'^(?P<VLAN>\d+) +(?P<Service_policy>.+)$')
        
        for line in output.splitlines():
            line = line.strip()
            
            #VLAN            Service-policy
            m = p1.match(line)            
            if m:
                group = m.groupdict()
                vlan = group['VLAN']
                mac_dict = ret_dict.setdefault('vlan', {}).setdefault(vlan, {})
                mac_dict['service_policy'] = group['Service_policy'] 
                                      
        return ret_dict
                
class ShowMdnsSdSpSdgStatisticsSchema(MetaParser):
    """ Schema for
    
        * show mdns-sd sp-sdg statistics
    """
    schema = {
        'average_input_rate_pps': {
            'one_min': int,
            '5_mins': int,
            '1_hour': int
        },
        'average_output_rate_pps': {
            'one_min': int,
            '5_mins': int,
            '1_hour': int
        },
        'messages_sent': {
            'query':  int,
            'any_query':  int,
            'advertisements':  int,
            'advertisement_withdraw':  int,
            'interface_down':  int,
            'vlan_down':  int,
            'service_peer_cache_clear':  int,
            'resync_response':  int,
            'srvc_discovery_response':  int,
            'keep_alive':  int,
        },
        'messages_received':{
            'query_response':  int,
            'any_query_response':  int,
            'cache_sync':  int,
            'get_service_instance':  int,
            'srvc_discovery_request':  int,
            'keep_alive_response':  int,
        },
    }
               
class ShowMdnsSdSpSdgStatistics(ShowMdnsSdSpSdgStatisticsSchema):
    """ Parser for
    
        * show mdns-sd sp-sdg statistics
        
    """
    
    cli_command = 'show mdns-sd sp-sdg statistics'

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)
               
        ret_dict = {}
        
        #Average Input rate (pps) : 0, 0, 0
        p0 = re.compile(r'Average Input rate +\(pps\) +: +(?P<one_min>\d+),\s+(?P<five_mins>\d+),\s+(?P<one_hour>\d+)')
        
        #Average Output rate (pps) : 0, 0, 0
        p1 = re.compile(r'Average Output rate +\(pps\) +: +(?P<one_min>\d+),\s+(?P<five_mins>\d+),\s+(?P<one_hour>\d+)')
               
        # Messages sent:
        p2 = re.compile(r'Messages sent')
        
        # Query : 15050
        p3 = re.compile(r'Query +: +(?P<query>\d+)')
        
        # ANY query : 0
        p4 = re.compile(r'ANY +query +: +(?P<any_qry>\d+)')
        
        # Advertisements : 2684
        p5 = re.compile(r'Advertisements +: +(?P<advts>\d+)')
        
        # Advertisement Withdraw : 0
        p6 = re.compile(r'Advertisement +Withdraw +: +(?P<advt_wtdrw>\d+)')
        
        # Interface down : 0
        p7 = re.compile(r'Interface +down +: +(?P<intf_down>\d+)')
        
        # Vlan down : 0
        p8 = re.compile(r'Vlan +down +: +(?P<vlan_down>\d+)')
        
        # Service-peer cache clear : 0
        p9 = re.compile(r'Service-peer +cache +clear +: +(?P<srvic_cach_clear>\d+)')
        
        # Resync response : 0
        p10 = re.compile(r'Resync +response +: +(?P<rsync_resp>\d+)')
        
        # Srvc Discovery response : 0
        p11 = re.compile(r'Srvc +Discovery +response +: +(?P<srvc_discv_resp>\d+)')
        
        # Keep-Alive : 5421
        p12 = re.compile(r'Keep-Alive +: +(?P<keep_alive>\d+)')
        
        # Messages received:
        p13 = re.compile(r'Messages received')
        
        # Query response : 0
        p14 = re.compile(r'Query +response +: +(?P<qry_resp>\d+)')
        
        # ANY Query response : 0
        p15 = re.compile(r'ANY +Query +response +: +(?P<any_qry_resp>\d+)')
        
        # Cache-sync : 60
        p16 = re.compile(r'Cache-sync +: +(?P<cache_sync>\d+)')
        
        # Get service-instance : 0
        p17 = re.compile(r'Get +service-instance +: +(?P<get_srvc_inst>\d+)')
        
        # Srvc Discovery request : 0
        p18 = re.compile(r'Srvc +Discovery +request +: +(?P<srvc_discv_reqst>\d+)')
        
        # Keep-Alive Response : 5421
        p19 = re.compile(r'Keep-Alive +Response +: +(?P<keep_alive_resp>\d+)')
        
        for line in output.splitlines():
            line = line.strip()
            
            # Average Input rate (pps) : One min, 5 mins, 1 hour  
            m = p0.match(line)
            if m:
                group = m.groupdict()
                average_input_rate_pps = ret_dict.setdefault('average_input_rate_pps', {})
                average_input_rate_pps['one_min'] = int(group["one_min"])
                average_input_rate_pps['5_mins'] = int(group["five_mins"])
                average_input_rate_pps['1_hour'] = int(group["one_hour"])
                                                      
            # Average Output rate (pps) : One min, 5 mins, 1 hour
            m = p1.match(line) 
            if m:            
                group = m.groupdict()
                average_output_rate_pps = ret_dict.setdefault('average_output_rate_pps', {})
                average_output_rate_pps['one_min'] = int(group["one_min"])
                average_output_rate_pps['5_mins'] = int(group["five_mins"])
                average_output_rate_pps['1_hour'] = int(group["one_hour"])
                            
            # Messages sent:
            m = p2.match(line)
            if m:
                messages_sent = ret_dict.setdefault('messages_sent', {})
                
            # Query : 15050    
            m = p3.match(line)
            if m:
                group = m.groupdict()
                messages_sent["query"] = int(group["query"])
                
            # ANY query : 0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                messages_sent["any_query"] = int(group["any_qry"])
                
            # Advertisements : 2684    
            m = p5.match(line)
            if m:
                group = m.groupdict()
                messages_sent["advertisements"] = int(group["advts"])
                
            # Advertisement Withdraw : 0    
            m = p6.match(line)
            if m:
                group = m.groupdict()
                messages_sent["advertisement_withdraw"] = int(group["advt_wtdrw"])
                
            # Interface down : 0    
            m = p7.match(line)
            if m:
                group = m.groupdict()
                messages_sent["interface_down"] = int(group["intf_down"])
                
            # Vlan down : 0    
            m = p8.match(line)
            if m:
                group = m.groupdict()
                messages_sent["vlan_down"] = int(group["vlan_down"])
                
            # Service-peer cache clear : 0    
            m = p9.match(line)
            if m:
                group = m.groupdict()
                messages_sent["service_peer_cache_clear"] = int(group["srvic_cach_clear"])
                
            # Resync response : 0    
            m = p10.match(line)
            if m:
                group = m.groupdict()
                messages_sent["resync_response"] = int(group["rsync_resp"])
                
            # Srvc Discovery response : 0    
            m = p11.match(line)
            if m:
                group = m.groupdict()
                messages_sent["srvc_discovery_response"] = int(group["srvc_discv_resp"])
                
            # Keep-Alive : 5421
            m = p12.match(line)
            if m:
                group = m.groupdict()
                messages_sent["keep_alive"] = int(group["keep_alive"])
                
            # Messages received:
            m = p13.match(line)
            if m:
                messages_received = ret_dict.setdefault('messages_received', {})
                
            # Query response : 0
            m = p14.match(line)
            if m:
                group = m.groupdict()
                messages_received["query_response"] = int(group["qry_resp"])
                
            # ANY Query response : 0
            m = p15.match(line)
            if m:
                group = m.groupdict()
                messages_received["any_query_response"] = int(group["any_qry_resp"])
                
            # Cache-sync : 60
            m = p16.match(line)
            if m:
                group = m.groupdict()
                messages_received["cache_sync"] = int(group["cache_sync"])
                
            # Get service-instance : 0
            m = p17.match(line)
            if m:
                group = m.groupdict()
                messages_received["get_service_instance"] = int(group["get_srvc_inst"])
                
            # Srvc Discovery request : 0
            m = p18.match(line)
            if m:
                group = m.groupdict()
                messages_received["srvc_discovery_request"] = int(group["srvc_discv_reqst"])
                
            # Keep-Alive Response : 5421
            m = p19.match(line)
            if m:
                group = m.groupdict()
                messages_received["keep_alive_response"] = int(group["keep_alive_resp"])
                
        return ret_dict
        
class ShowMdnsSdStatisticsCacheAllSchema(MetaParser):
    """ Schema for
    
        * show mdns-sd statistics cache all
    """
    schema = {
        'mdns_cache_statistics': {
            'number_of_service_types': int,
            'number_of_records_of_type': {
                Any(): int 
            }
        },
        'top_service_types_by_instances': {
            'service_type':{
                Any(): int 
            }
        },
        'top_advertisers_of_record': {
            'mac_address':{
                Any(): int 
            }
        }
    }
                        
class ShowMdnsSdStatisticsCacheAll(ShowMdnsSdStatisticsCacheAllSchema):
    """ Parser for
    
        * show mdns-sd statistics cache all
        
    """
    
    cli_command = 'show mdns-sd statistics cache all'

    def cli(self, output=None):

        if output is None:
           output = self.device.execute(self.cli_command)
             
        ret_dict = {}
        
        # mDNS cache statistics:
        p0 = re.compile(r'mDNS cache statistics')
        
        #Number of service types : 14
        p1 = re.compile(r'Number +of +service +types +: +(?P<srvc_types>\d+)')
                
        # Number of records of type PTR : 913
        p2 = re.compile(r'^Number +of +records +of +type +(?P<record_type>\S+) +: +(?P<count>\d+)$')
        
        # Top service types by instances:
        p3 = re.compile(r'Top service types by instances')
                
        #Service type
        p4 = re.compile(r'^Service type')
        
        #service instances _http._tcp.local : 76
        p5 = re.compile(r'^(?P<service_instance>_\S+) +: +(?P<count>\d+)$')
        
        # Top advertisers of record:
        p6 = re.compile(r'Top advertisers of record')
        
        #MAC Address
        p7 = re.compile(r'^MAC Address')
        
        #MAC Address records 0242.2d01.0f04 : 74
        p8 = re.compile(r'^(?P<mac_address_records>[a-zA-Z0-9]+\.\w+\.\w+) +: +(?P<count>\d+)$')

        for line in output.splitlines():
            line = line.strip()
            
            # mDNS cache statistics:
            m = p0.match(line)
            if m:
                mdns_cache_statistics = ret_dict.setdefault('mdns_cache_statistics', {})
            
            #Number of service types : 14
            m = p1.match(line)
            if m:
                group = m.groupdict()
                mdns_cache_statistics["number_of_service_types"] = int(group["srvc_types"])
                
            #Number of records of type PTR : 913     
            m = p2.match(line)
            if m:
                number_of_records_of_type = mdns_cache_statistics.setdefault('number_of_records_of_type', {})
                groups = m.groupdict()
                record_type = groups['record_type'].lower()
                value = int(groups['count'])
                number_of_records_of_type.update({record_type: value})               
            
            #Top service types by instances:
            m = p3.match(line)
            if m:
                top_service_types_by_instances = ret_dict.setdefault('top_service_types_by_instances', {})
            
            #Service type    
            m = p4.match(line)
            if m:
                service_type = top_service_types_by_instances.setdefault('service_type', {})
                                            
            #service instances _http._tcp.local : 76    
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                service_instance = groups['service_instance'].lower()
                value = int(groups['count'])
                service_type.update({service_instance: value})   
            
            #Top advertisers of record:    
            m = p6.match(line)
            if m:
                top_advertisers_of_record = ret_dict.setdefault('top_advertisers_of_record', {})
            
            #MAC Address
            m = p7.match(line)
            if m:
                mac_address = top_advertisers_of_record.setdefault('mac_address', {})
                                               
            #MAC Address : 0242.2d01.0f04 : 74    
            m = p8.match(line)
            if m:
                groups = m.groupdict()
                mac_address_records = groups['mac_address_records'].lower()
                value = int(groups['count'])
                mac_address.update({mac_address_records: value})  
                             
        return ret_dict
        
class ShowMdnsSdSummarySchema(MetaParser):
    """ Schema for
        * show mdns-sd summary
    """
    schema = {
        'global_mdns_gateway': {
            'mdns_gateway': str,
            Optional('rate_limit_pps'): int,
            Optional('rate_limit_mode'): str,
            Optional('airprint_helper'): str,
            'mode': str,
            Optional('sdg_agent_ip'): str,
            Optional('source_interface'): str,
            Optional('cache_sync_periodicity_minutes'): int,
            Optional('cache_sync_periodicity_mode'): str,
            Optional('active_response_timer'): str,
            Optional('active_query_timer'): str,
            Optional('active_query_timer_minutes'): int,
            Optional('active_query_timer_mode'): str,
            'mdns_query_type': str,
            Optional('service_eumeration_period'): str,
            'sso': str
        }           
    }

class ShowMdnsSdSummary(ShowMdnsSdSummarySchema):
    """ Parser for
    
        * show mdns-sd summary
         
    """
    cli_command = 'show mdns-sd summary'

    def cli(self, output=None):
        
        if output is None:
           output = self.device.execute(self.cli_command)
              
        ret_dict = {}
        
        #Global mDNS Gateway
        p0 = re.compile(r"Global mDNS Gateway")

        # mDNS Gateway               : Enabled
        p1 = re.compile(r'mDNS +Gateway +: +(?P<mdns_gty>\w+)')
    
        # Rate Limit PPS             : 60
        p2 = re.compile(r'Rate +Limit +PPS +: +(?P<rate_lmt>\d+)')
        
        # Rate Limit Mode            : default
        p3 = re.compile(r'Rate +Limit +Mode +: +(?P<rate_lmt_mode>\w+)')
    
        # AirPrint Helper            : Disabled
        p4 = re.compile(r'AirPrint +Helper +: +(?P<air_prnt>\w+)')
    
        # Mode                       : SDG-Agent
        p5 = re.compile(r'Mode +: +(?P<mode>\S+)')
    
        # SDG Agent IP               : 40.1.3.1
        p6 = re.compile(r'SDG +Agent +IP +: +(?P<sdg_ip>\d+.+\d+.+\d+.+\d+)')
    
        # Source Interface : Vl1301
        p7 = re.compile(r'Source +Interface +\: +(?P<src_intef>(.*))')
    
        # Cache-Sync Periodicity Minutes   : 30 
        p8 = re.compile(r'Cache-Sync +Periodicity +Minutes +: +(?P<cache_sync>\d+)')
        
        # Cache-Sync Periodicity Mode    : default
        p9 = re.compile(r'Cache-Sync +Periodicity +Mode +: +(?P<cache_sync_mode>\w+)')
    
        # Active Response Timer      : Disabled
        p10 = re.compile(r'Active +Response +Timer +: +(?P<act_tmr>\w+)')
    
        # Active Query Timer         : Enabled
        p11 = re.compile(r'Active +Query +Timer +: +(?P<act_qtmr>\w+)')
        
        # Active Query Timer Minutes        : 30
        p12 = re.compile(r'Active +Query +Timer +Minutes +: +(?P<act_qtmr_mins>\d+)')
        
        # Active Query Timer Mode        : default
        p13 = re.compile(r'Active +Query +Timer +Mode +: +(?P<act_qtmr_mode>\w+)')
    
        # mDNS Query Type            : PTR only
        p14 = re.compile(r'mDNS +Query +Type +: +(?P<mdns_qry_type>\w+ +\w+)')
    
        # Service Enumeration period : Default
        p15 = re.compile(r'Service +Enumeration +period +: +(?P<srv_prd>\w+)')
    
        # SSO                        : Active
        p16 = re.compile(r'SSO +: +(?P<sso>\w+)')
        
        for line in output.splitlines():
            line = line.strip()
            
            #Global mDNS Gateway  
            m = p0.match(line)
            if m:
                global_mdns_gateway = ret_dict.setdefault('global_mdns_gateway', {}) 
                
            # mDNS Gateway               : Enabled                     
            m = p1.match(line)
            if m:
                group = m.groupdict()
                global_mdns_gateway["mdns_gateway"] = group["mdns_gty"]
                
            # Rate Limit PPS             : 60
            m = p2.match(line)
            if m:
                group = m.groupdict()
                global_mdns_gateway["rate_limit_pps"] = int(group["rate_lmt"])
                
            # Rate Limit Mode            : (default)
            m = p3.match(line)
            if m:
                group = m.groupdict()
                global_mdns_gateway["rate_limit_mode"] = group["rate_lmt_mode"]
                
            # AirPrint Helper            : Disabled
            m = p4.match(line)
            if m:
                group = m.groupdict()
                global_mdns_gateway["airprint_helper"] = group["air_prnt"]
                
            # Mode                       : SDG-Agent
            m = p5.match(line)
            if m:
                group = m.groupdict()
                global_mdns_gateway["mode"] = group["mode"]
                
            # SDG Agent IP               : 40.1.3.1
            m = p6.match(line)
            if m:
                group = m.groupdict()
                global_mdns_gateway["sdg_agent_ip"] = group["sdg_ip"]
                
            # Source Interface : Vl1301
            m = p7.match(line)
            if m:
                group = m.groupdict()
                global_mdns_gateway["source_interface"] = group["src_intef"]
                
            # Cache-Sync Periodicity Minutes    : 30
            m = p8.match(line)
            if m:
                group = m.groupdict()
                global_mdns_gateway["cache_sync_periodicity_minutes"] = int(group["cache_sync"])
                
            # Cache-Sync Periodicity Mode    : default
            m = p9.match(line)
            if m:
                group = m.groupdict()
                global_mdns_gateway["cache_sync_periodicity_mode"] = group["cache_sync_mode"]
                
            # Active Response Timer      : Disabled
            m = p10.match(line)
            if m:
                group = m.groupdict()
                global_mdns_gateway["active_response_timer"] = group["act_tmr"]
                
            # Active Query Timer         : Enabled
            m = p11.match(line)
            if m:
                group = m.groupdict()
                global_mdns_gateway["active_query_timer"] = group["act_qtmr"]
                
            # Active Query Timer Minutes         : 30
            m = p12.match(line)
            if m:
                group = m.groupdict()
                global_mdns_gateway["active_query_timer_minutes"] = int(group["act_qtmr_mins"])
                
            # Active Query Timer Mode         : default
            m = p13.match(line)
            if m:
                group = m.groupdict()
                global_mdns_gateway["active_query_timer_mode"] = group["act_qtmr_mode"]
                
            # mDNS Query Type            : PTR only
            m = p14.match(line)
            if m:
                group = m.groupdict()
                global_mdns_gateway["mdns_query_type"] = group["mdns_qry_type"]
                
            # Service Enumeration period : Default
            m = p15.match(line)
            if m:
                group = m.groupdict()
                global_mdns_gateway["service_eumeration_period"] = group["srv_prd"]
                
            # SSO                        : Active
            m = p16.match(line)
            if m:
                group = m.groupdict()
                global_mdns_gateway["sso"] = group["sso"]   
                   
        return ret_dict

class ShowMdnsSdSummaryInterfaceVlanSchema(MetaParser):
    """ Schema for
        * show mdns-sd summary interface vlan 300
    """
    schema = {
        'interface': str,
        'mdns_gateway': str,
        'mdns_service_policy': str,
        'active_query': str,
        'periodicity_seconds': int,
        'transport_type': str,
        'service_instance_suffix': str,
        'mdns_query_type': str
    }

class ShowMdnsSdSummaryInterfaceVlan(ShowMdnsSdSummaryInterfaceVlanSchema):
    """ Parser for
        * show mdns-sd summary interface vlan 300     
        
    """
    cli_command = 'show mdns-sd summary interface vlan {vlan}'
    

    def cli(self, output=None,vlan=None):
        
        if output is None:
           output = self.device.execute(self.cli_command.format(vlan=vlan))
              
        ret_dict = {}

        # Interface : Vlan300
        p1 = re.compile(r'Interface +: +(?P<inter>(.*))')
        
        # mDNS Gateway               : Enabled
        p2 = re.compile(r'mDNS +Gateway +: +(?P<mdns_gty>\w+)')
    
        # mDNS Service Policy      : Not-Configured
        p3 = re.compile(r'mDNS +Service +Policy +: +(?P<mdns_plcy>(.*))')
        
        # Active Query             : Enabled
        p4 = re.compile(r'Active +Query +: +(?P<act_qry>\w+)')
    
        # Periodicity Seconds : 60
        p5 = re.compile(r'Periodicity +Seconds +: +(?P<prdcty>\d+)')
        
        # Transport Type           : IPv6
        p6 = re.compile(r'Transport +Type +\: +(?P<trnsprt_type>(.*))')
        
        # Service Instance Suffix  : Not-Configured
        p7 = re.compile(r'Service +Instance +Suffix +: +(?P<srvc_inst>(.*))')
    
        # mDNS Query Type            : PTR only
        p8 = re.compile(r'mDNS +Query +Type +: +(?P<mdns_qry_type>\w+ +\w+)')
    
        for line in output.splitlines():
            line = line.strip()
            
            # Interface : Vlan300            
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict["interface"] = group["inter"]
                
            # mDNS Gateway               : Enabled    
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict["mdns_gateway"] = group["mdns_gty"]
                
            # mDNS Service Policy      : Not-Configured
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict["mdns_service_policy"] = group["mdns_plcy"]
                
            # Active Query             : Enabled
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ret_dict["active_query"] = group["act_qry"]
                
            # Periodicity Seconds : 60    
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ret_dict["periodicity_seconds"] = int(group["prdcty"])
                
            # Transport Type           : IPv6
            m = p6.match(line)
            if m:
                group = m.groupdict()
                ret_dict["transport_type"] = group["trnsprt_type"]
                
            # Service Instance Suffix  : Not-Configured
            m = p7.match(line)
            if m:
                group = m.groupdict()
                ret_dict["service_instance_suffix"] = group["srvc_inst"]
                
            # mDNS Query Type            : PTR only
            m = p8.match(line)
            if m:
                group = m.groupdict()
                ret_dict["mdns_query_type"] = group["mdns_qry_type"]
                              
        return ret_dict
                     
class ShowMdnsSdSummaryVlanSchema(MetaParser):
    """ Schema for
        * show mdns-sd summary vlan 1101
    """
    schema = {
        'vlan': str,
        'mdns_gateway': str,  
        'mdns_service_policy': str,  
        'active_query': {
            'status': str,
            Optional('periodicity_mins'): int,
        },
        'transport_type': str,
        'service_instance_suffix': str,   
        'mdns_query_type': str,     
        'sdg_agent_ip': str,
        'source_interface': str           
    }

class ShowMdnsSdSummaryVlan(ShowMdnsSdSummaryVlanSchema):
    """ Parser for
        * show mdns-sd summary vlan 1101       
        
    """
    cli_command = 'show mdns-sd summary vlan {vlan}'
    
    def cli(self, output=None,vlan=None):
    
        if output is None:
           output = self.device.execute(self.cli_command.format(vlan=vlan))
              
        ret_dict = {}

        # VLAN  :  1101
        p1 = re.compile(r'VLAN +: +(?P<vln>\d+)')

        # mDNS Gateway               : Enabled
        p2 = re.compile(r'mDNS +Gateway +: +(?P<mdns_gty>\w+)')

        # mDNS Service Policy : default-mdns-service-policy
        p3 = re.compile(r'mDNS +Service +Policy +: +(?P<mdns_plcy>(.*))')

        # Active Query :
        p4 = re.compile(r'Active Query')

        #Status             : Enabled
        p5 = re.compile(r'Status +: +(?P<stats>\w+)')

        # Periodicity mins    : 30
        p6 = re.compile(r'Periodicity +mins +: +(?P<prdcty>\d+)')

        # Transport Type           : IPv4
        p7 = re.compile(r'Transport +Type +\: +(?P<trnsprt_type>(.*))')

        # Service Instance Suffix  : Not-Configured
        p8 = re.compile(r'Service +Instance +Suffix +: +(?P<srvc_inst>(.*))')

        # mDNS Query Type            : ALL
        p9 = re.compile(r'mDNS +Query +Type +: +(?P<mdns_qry_type>(.*))')

        # SDG Agent IP               : 10.1.1.2
        p10 = re.compile(r'SDG +Agent +IP +: +(?P<sdg_ip>\d+.+\d+.+\d+.+\d+)')

        # Source Interface : Vlan4025
        p11 = re.compile(r'Source +Interface +\: +(?P<src_intef>(.*))')

        for line in output.splitlines():
            line = line.strip()
            
            # VLAN  :  1101
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict["vlan"] = group["vln"]

            # mDNS Gateway               : Enabled
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict["mdns_gateway"] = group["mdns_gty"]

            # mDNS Service Policy : default-mdns-service-policy
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict["mdns_service_policy"] = group["mdns_plcy"]

            # Active Query:
            m = p4.match(line)
            if m:
                active_query = ret_dict.setdefault('active_query', {})

            #status             : Enabled
            m = p5.match(line)
            if m:
                group = m.groupdict()
                active_query["status"] = group["stats"]

            # periodicity mins     : Periodicity 30 minutes
            m = p6.match(line)
            if m:
                group = m.groupdict()
                active_query["periodicity_mins"] = int(group["prdcty"])

            # Transport Type           : IPv4
            m = p7.match(line)
            if m:
                group = m.groupdict()
                ret_dict["transport_type"] = group["trnsprt_type"]

            # Service Instance Suffix  : Not-Configured
            m = p8.match(line)
            if m:
                group = m.groupdict()
                ret_dict["service_instance_suffix"] = group["srvc_inst"]

            # mDNS Query Type            : ALL
            m = p9.match(line)
            if m:
                group = m.groupdict()
                ret_dict["mdns_query_type"] = group["mdns_qry_type"]

            # SDG Agent IP               : 10.1.1.2
            m = p10.match(line)
            if m:
                group = m.groupdict()
                ret_dict["sdg_agent_ip"] = group["sdg_ip"]

            # Source Interface : Vlan4025
            m = p11.match(line)
            if m:
                group = m.groupdict()
                ret_dict["source_interface"] = group["src_intef"]
               
        return ret_dict
        
class ShowMdnsSdServicePolicyAssociationRoleSchema(MetaParser):
    """ Schema for
    
        * show mdns-sd service-policy association role
    """
    schema = {
        'mac': {
            Any(): {
                'mac': str, 
                'service_policy': str,
                'lg_id': int, 
                'role':  str
            }
        }
    }
                        
class ShowMdnsSdServicePolicyAssociationRole(ShowMdnsSdServicePolicyAssociationRoleSchema):
    """ Parser for
    
        * show mdns-sd service-policy association role
           
    """
    
    cli_command = 'show mdns-sd service-policy association role'

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}
        #                     Mac                 Service-policy                Lg-Id           Role
        p1 = re.compile(r'(?P<Mac>[\w\.\:]+) +(?P<Service_policy>([\w_]+)) +(?P<Lg_Id>\d+) +(?P<Role>\w+)')
        
        for line in output.splitlines():
            line = line.strip()
            
            #                     Mac                 Service-policy                Lg-Id           Role
            m = p1.match(line)
            if m:
                group = m.groupdict()
                mac = group['Mac']
                mac_dict = ret_dict.setdefault('mac', {}).setdefault(mac, {})
                mac_dict['mac'] = group['Mac']
                mac_dict['service_policy'] = group['Service_policy']
                mac_dict['lg_id'] = int(group['Lg_Id'])
                mac_dict['role'] = group['Role']
                        
        return ret_dict
                
class ShowMdnsSdControllerSummarySchema(MetaParser):
    """ Schema for
    
        * sh mdns-sd controller summary
    """
    schema = {
        'controller_summary': {
            'controller_name': str,
            'controller_ip': str,
            'state': str,
            'port': int,
            'interface': str,
            'filter_list': str,
            'dead_time': str,
            'service_buffer': str
        }           
    }
                        
class ShowMdnsSdControllerSummary(ShowMdnsSdControllerSummarySchema):
    """ Parser for
    
        * show mdns-sd controller summary
           
    """
    
    cli_command = 'show mdns-sd controller summary'

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)        

        ret_dict = {}
        
        #Controller Summary
        p0 = re.compile(r"Controller Summary")
        
        #Controller Name : DNAC
        p1 = re.compile(r'Controller +Name +: +(?P<contrl_name>\w+)')
                
        # Controller IP : 11.12.13.14
        p2 = re.compile(r'Controller +IP +: +(?P<cntrl_ip>\d+.+\d+.+\d+.+\d+)')
        
        #State : UP
        p3 = re.compile(r'State +: +(?P<state>\w+)')

        #Port : 9991
        p4 = re.compile(r'Port +: +(?P<port>\d+)')

        #Interface : Loopback0
        p5 = re.compile(r'Interface +: +(?P<intf>(.*))')
        
        #Filter List : policy-con
        p6 = re.compile(r'Filter +List +: +(?P<filt_lst>(.*))')
        
        #Dead Time : 00:00:00
        p7 = re.compile(r'Dead +Time +: +(?P<dead_time>(.*))')
        
        #Service Buffer : Enabled
        p8 = re.compile(r'Service +Buffer +: +(?P<servc_buff>\w+)')

        for line in output.splitlines():
            line = line.strip()
            
            #Controller Summary  
            m = p0.match(line)
            if m:
                controller_summary = ret_dict.setdefault('controller_summary', {})
            
            #Controller Name : DNAC
            m = p1.match(line)
            if m:
                group = m.groupdict()
                controller_summary["controller_name"] = group["contrl_name"]
                
            #Controller IP : 11.12.13.14    
            m = p2.match(line)
            if m:
                group = m.groupdict()
                controller_summary["controller_ip"] = group["cntrl_ip"]
                
            #State : UP    
            m = p3.match(line)
            if m:
                group = m.groupdict()
                controller_summary["state"] = group["state"]
                
            #Port : 9991
            m = p4.match(line)
            if m:
                group = m.groupdict()
                controller_summary["port"] = int(group["port"])
                
            #Interface : Loopback0
            m = p5.match(line)
            if m:
                group = m.groupdict()
                controller_summary["interface"] = group["intf"]
                
            #Filter List : policy-con
            m = p6.match(line)
            if m:
                group = m.groupdict()
                controller_summary["filter_list"] = group["filt_lst"]
                
            #Dead Time : 00:00:00
            m = p7.match(line)
            if m:
                group = m.groupdict()
                controller_summary["dead_time"] = group["dead_time"]
                
            #Service Buffer : Enabled
            m = p8.match(line)
            if m:
                group = m.groupdict()
                controller_summary["service_buffer"] = group["servc_buff"]
                
        return ret_dict