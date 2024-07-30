"""show_lisp_platform.py

    * show lisp platform
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (Any,
                                                ListOf,
                                                Optional,
                                                Or)
from genie.libs.parser.utils.common import Common

from genie.libs.parser.iosxe.show_lisp_super import *

# ===============================
# Schema for 'show lisp platform'
# ===============================
class ShowLispPlatformSchema(MetaParser):

    ''' Schema for "show lisp platform" '''

    schema = {
        'parallel_lisp_instance_limit': int,
        'rloc_forwarding_support': {
            'local': {
                'ipv4': str,
                'ipv6': str,
                'mac': str,
            },
            'remote': {
                'ipv4': str,
                'ipv6': str,
                'mac': str,
            },
        },
        'latest_supported_config_style': str,
        'current_config_style': str,
        Optional('support_for_signal_forward'): {
            'ipv4': str,
            'ipv6': str,
            'mac': str,
        },
        Optional('platform_reported_limits'): {
            'l3_limit': {
                'l3_limit': int,
                'total_current_utilization': str,
                'ipv4': {
                    'local_eid': int,
                    'multiplier': int,
                    'remote_eid': int,
                    Optional('remote_eid_idle'): int,
                    Optional('mapping_cache_full'): str,
                },
                'ipv6': {
                    'local_eid': int,
                    'multiplier': int,
                    'remote_eid': int,
                    Optional('remote_eid_idle'): int,
                    Optional('mapping_cache_full'): str,
                },
            },
            'l2_limit': {
                'l2_limit': int,
                'total_current_utilization': str,
                'mac': {
                    'local_eid': int,
                    'multiplier': int,
                    'remote_eid': int,
                    Optional('remote_eid_idle'): int,
                    Optional('mapping_cache_full'): str,
                }
            },
            Optional('software_only'): {
                'ipv4': {
                    'local_eid': int,
                    'remote_eid': int,
                },
                'ipv6': {
                    'local_eid': int,
                    'remote_eid': int,
                },
                'mac': {
                    'local_eid': int,
                    'remote_eid': int,
                }
            } 
        }
    }


# ==============================
# Parser for 'show lisp platform'
# ==============================
class ShowLispPlatform(ShowLispPlatformSchema):

    ''' Parser for "show lisp platform" '''

    cli_command = 'show lisp platform'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Init vars
        parsed_dict = {}

        # Parallel LISP instance limit:      2000
        p1 = re.compile(r'Parallel +LISP +instance +limit: +(?P<limit>(\d+))$')

        # IPv4 RLOC, local:                 OK
        # IPv6 RLOC, local:                 OK
        # MAC RLOC, local:                  Unsupported
        p2 = re.compile(r'(?P<type>(IPv4|IPv6|MAC)) RLOC,'
                            ' +local: +(?P<local>(\S+))$')

        # IPv4 RLOC, remote:                OK
        # IPv6 RLOC, remote:                OK
        # MAC RLOC, remote:                 Unsupported
        p3 = re.compile(r'(?P<type>(IPv4|IPv6|MAC)) RLOC,'
                            ' +remote: +(?P<remote>(\S+))$')

        # Latest supported config style:     Service and instance
        p4 = re.compile(r'Latest +supported +config +style:'
                            ' +(?P<supported>([a-zA-Z\s]+))$')

        # Current config style:              Service and instance
        p5 = re.compile(r'Current +config +style:'
                            ' +(?P<current>([a-zA-Z\s]+))$')

        # Support for signal+forward:
        p6 = re.compile(r'^Support for signal\Sforward:$')

        # IPv4:                             Unsupported
        # IPv6:                             Unsupported
        # MAC:                              Unsupported
        p7 = re.compile(r'^(?P<support_type>(IPv4|IPv6|MAC)):(:?\s*)(?P<status>\w*)$')

        #Platform reported limits:
        p8 = re.compile(r'^Platform reported limits:$')

        # L3 limit:                         114688
        # L2 limit:                         65536
        # p10 = re.compile(r'^(?P<type>(L2 limit)):(?:\s*)(?P<l2_limit>(\d*))$')
        p9 = re.compile(r'^(?P<type>(L3 limit|L2 limit)):(?:\s*)(?P<l_limit>(\d*))$')
        
        # Software-only counters:
        p9_1 = re.compile(r'^(?P<type>(Software-only))\scounters:')

        #     Total Current utilization:      0%
        p10 = re.compile(r'^Total Current utilization:(?:\s*)+(?P<total_current_utilization>(\d*%))$')

        # IPv4 local EID counter:         3
        # IPv4 remote EID counter:        6
        # IPv4 remote EID idle counter:   1
        p11 = re.compile(r'^IPv4 (?P<type>(multiplier|local\sEID\scounter|remote\sEID\scounter|remote\sEID\sidle\scounter)):(?:\s*)(?P<ipv4>(\d*))$')

        #IPv4 mapping cache full:        no
        p12 = re.compile(r'^IPv4 mapping cache full:(?:\s*)(?P<ipv4_1>(\w*))$')

        # IPv6 multiplier:                2
        # IPv6 local EID counter:         3
        # IPv6 remote EID counter:        4
        # IPv6 remote EID idle counter:   0
        p13 = re.compile(r'^IPv6 (?P<type>(multiplier|local\sEID\scounter|remote\sEID\scounter|remote\sEID\sidle\scounter)):(?:\s*)(?P<ipv6>(\d*))$')

        #IPv6 mapping cache full:        no
        p14 = re.compile(r'^IPv6 mapping cache full:(?:\s*)(?P<ipv6_1>(\w*))$')

        # MAC multiplier:                 1
        # MAC local EID counter:          0
        # MAC remote EID counter:         0
        # MAC remote EID idle counter:    0
        p15 = re.compile(r'^MAC (?P<type>(multiplier|local\sEID\scounter|remote\sEID\scounter|remote\sEID\sidle\scounter)):(?:\s*)(?P<mac>(\d*))$')

        #MAC mapping cache full:         no
        p16 = re.compile(r'^MAC mapping cache full:(?:\s*)(?P<mac_1>(\w*))$')

        # loop to split lines of output
        for line in out.splitlines():
            if line.strip():
                line = line.strip()

                # Parallel LISP instance limit:      2000
                m = p1.match(line)
                if m:
                    parsed_dict['parallel_lisp_instance_limit'] = \
                        int(m.groupdict()['limit'])
                    continue

                # IPv4 RLOC, local:                 OK
                # IPv6 RLOC, local:                 OK
                # MAC RLOC, local:                  Unsupported
                m = p2.match(line)
                if m:
                    local_type = m.groupdict()['type'].lower()
                    rloc_dict = parsed_dict.\
                                setdefault('rloc_forwarding_support', {}).\
                                setdefault('local', {})
                    rloc_dict[local_type] = m.groupdict()['local'].lower()
                    continue

                # IPv4 RLOC, remote:                 OK
                # IPv6 RLOC, remote:                 OK
                # MAC RLOC, remote:                  Unsupported
                m = p3.match(line)
                if m:
                    remote_type = m.groupdict()['type'].lower()
                    rloc_dict = parsed_dict.\
                                setdefault('rloc_forwarding_support', {}).\
                                setdefault('remote', {})
                    rloc_dict[remote_type] = m.groupdict()['remote'].lower()
                    continue

                # Latest supported config style:     Service and instance
                m = p4.match(line)
                if m:
                    parsed_dict['latest_supported_config_style'] = \
                        m.groupdict()['supported'].lower()
                    continue

                # Current config style:              Service and instance
                m = p5.match(line)
                if m:
                    parsed_dict['current_config_style'] = \
                        m.groupdict()['current'].lower()
                    continue
                
                # Support for signal+forward:
                m = p6.match(line)
                if m:
                    signal_dict = parsed_dict.setdefault('support_for_signal_forward', {})
                    continue
                    
                # IPv4:                             Unsupported
                # IPv6:                             Unsupported
                # MAC:                              Unsupported
                m = p7.match(line)
                if m:
                    group_type = m.groupdict()
                    group_key = group_type['support_type'].lower()
                    signal_dict.setdefault(group_key,str(group_type['status']))
                    continue

                #Platform reported limits:
                m = p8.match(line)
                if m:
                    parsed_dict.setdefault('platform_reported_limits', {})
                    continue
                
                # L3 limit:                         114688
                m = p9.match(line)
                if m:
                    groups = m.groupdict()
                    limit_type = groups['type'].lower().replace(' ', '_')
                    limit_dict = parsed_dict.setdefault('platform_reported_limits', {}).setdefault(limit_type, {})
                    limit_dict.setdefault('total_current_utilization', str())
                    limit_dict.update({
                        limit_type: int(groups['l_limit']),
                    })
                    continue
                  
                # Software-only counters:
                m = p9_1.match(line)
                if m:
                    groups = m.groupdict()
                    limit_type = groups['type'].lower().replace('-', '_')
                    limit_dict = parsed_dict.setdefault('platform_reported_limits', {}).setdefault(limit_type, {})
                    continue

                # Total Current utilization:      0%
                m = p10.match(line)
                if m:
                    group_utl = m.groupdict()
                    limit_type = groups['type'].lower().replace(' ', '_')
                    parsed_dict.setdefault('platform_reported_limits', {}).\
                        setdefault(limit_type, {}).\
                        update({'total_current_utilization': group_utl['total_current_utilization']})
                    continue
                
                # IPv4 multiplier:                1
                # IPv4 local EID counter:         3
                # IPv4 remote EID counter:        6
                # IPv4 remote EID idle counter:   1
                m = p11.match(line)
                if m:
                    ip_type = m.groupdict()['type'].lower().replace(' counter', '').replace(' ', '_')
                    ipv4_dict = limit_dict.setdefault('ipv4', {})
                    ipv4_dict[ip_type] = int(m.groupdict()['ipv4'].lower())
                    continue

                # IPv4 mapping cache full:        no
                m = p12.match(line)
                if m:
                    ipv4_dict.setdefault('mapping_cache_full', str())
                    ipv4_dict.update({'mapping_cache_full':str(m.groupdict()['ipv4_1'].lower())})
                    continue

                # IPv6 multiplier:                2
                # IPv6 local EID counter:         3
                # IPv6 remote EID counter:        4
                # IPv6 remote EID idle counter:   0
                m = p13.match(line)
                if m:
                    ip_type = m.groupdict()['type'].lower().replace(' counter', '').replace(' ', '_')
                    ipv6_dict = limit_dict.setdefault('ipv6', {})
                    ipv6_dict[ip_type] = int(m.groupdict()['ipv6'].lower())
                    continue

                # IPv6 mapping cache full:        no
                m = p14.match(line)
                if m:
                    ipv6_dict.setdefault('mapping_cache_full', str())
                    ipv6_dict.update({'mapping_cache_full':str(m.groupdict()['ipv6_1'].lower())})
                    continue

                # MAC multiplier:                 1
                # MAC local EID counter:          0
                # MAC remote EID counter:         0
                # MAC remote EID idle counter:    0
                m = p15.match(line)
                if m:
                    mac_type = m.groupdict()['type'].lower().replace(' counter', '').replace(' ', '_')
                    mac_dict = limit_dict.setdefault('mac', {})
                    mac_dict[mac_type] = int(m.groupdict()['mac'].lower())
                    continue

                # IPv4 mapping cache full:        no
                m = p16.match(line)
                if m:
                    mac_dict.setdefault('mapping_cache_full', str())
                    mac_dict.update({'mapping_cache_full':str(m.groupdict()['mac_1'].lower())})
                    continue

        return parsed_dict


class ShowLispPlatformStatisticsSchema(MetaParser):

    ''' Schema for
        * show lisp platform statistics
    '''
    schema = {
        'fib': {
            'notifications': {
                'received': int,
                'processed': int
                },
            'invalid': {
                'received': int,
                'processed': int
                },
            'data_packet': {
                'received': int,
                'processed': int
                },
            'l2_data_packet': {
                'received': int,
                'processed': int
                },
            'status_report': {
                'received': int,
                'processed': int
                },
            'dyn_eid_detected': {
                'received': int,
                'processed': int
                },
            'dyn_eid_decap_statle': {
                'received': int,
                'processed': int
                },
            'l2_dyn_eid_decap_statle': {
                'received': int,
                'processed': int
                },
            'dyn_eid_adjacency': {
                'received': int,
                'processed': int
                },
            'delete_map_cache': {
                'received': int,
                'processed': int
                }
            },
        'l2_rib': {
            'remote_update_requests': int,
            'local_update_requests': int,
            'delete_requests': int,
            'update_test': int,
            'delete_test': int,
            'message_sent': int,
            'message_received': int,
            'unknown_message_received': int,
            'send_errors': int,
            'flow_control': int
            },
        'cef': {
            'dropped_notifications': int,
            'total_notifications': int,
            'dropped_control_packets': int,
            'high_priority_queue': int,
            'normal_priority_queue': int
            },
        'deffered': {
            'ddt_referral': {
                'deferred': int,
                'dropped': int
                },
            'ddt_request': {
                'deferred': int,
                'dropped': int
                },
            'ddt_query': {
                'deferred': int,
                'dropped': int
                },
            'map_request': {
                'deferred': int,
                'dropped': int
                },
            'map_register': {
                'deferred': int,
                'dropped': int
                },
            'map_reply': {
                'deferred': int,
                'dropped': int
                },
            'mr_negative_map_reply': {
                'deferred': int,
                'dropped': int
                },
            'mr_map_request_fwd': {
                'deferred': int,
                'dropped': int
                },
            'ms_map_request_fwd': {
                'deferred': int,
                'dropped': int
                },
            'ms_proxy_map_reply': {
                'deferred': int,
                'dropped': int
                },
            'xtr_mcast_map_notify': {
                'deferred': int,
                'dropped': int
                },
            'ms_info_reply': {
                'deferred': int,
                'dropped': int
                },
            'ms_map_notify': {
                'deferred': int,
                'dropped': int
                },
            'rtr_map_register_fwd': {
                'deferred': int,
                'dropped': int
                },
            'rtr_map_notify_fwd': {
                'deferred': int,
                'dropped': int
                },
            'etr_info_request': {
                'deferred': int,
                'dropped': int
                },
            },
        'errors': {
            'invalid_ip_version_drops': int
            },
        'udp_control_packets': {
            'ipv4': {
                'received_total_packets': int,
                'received_invalid_vrf': int,
                'received_invalid_ip_header': int,
                'received_invalid_protocol': int,
                'received_invalid_size': int,
                'received_invalid_port': int,
                'received_invalid_checksum': int,
                'received_unsupported_lisp': int,
                'received_not_lisp_control': int,
                'received_unknown_lisp_control': int,
                'sent_total': int,
                'sent_flow_controlled': int,
                },
            'ipv6': {
                'received_total_packets': int,
                'received_invalid_vrf': int,
                'received_invalid_ip_header': int,
                'received_invalid_protocol': int,
                'received_invalid_size': int,
                'received_invalid_port': int,
                'received_invalid_checksum': int,
                'received_unsupported_lisp': int,
                'received_not_lisp_control': int,
                'received_unknown_lisp_control': int,
                'sent_total': int,
                'sent_flow_controlled': int,
                }
            }
        }


class ShowLispPlatformStatistics(ShowLispPlatformStatisticsSchema):

    ''' Parser for
        * show lisp platform statistics
    '''
    cli_command = 'show lisp platform statistics'

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)
        ret_dict = {}

        #  FIB notications received/processed:                    35669/35669
        p1 = re.compile(r"^FIB\s+notications\s+received\/processed:\s+"
                        r"(?P<received>\d+)\/(?P<processed>\d+)$")

        # Invalid received/processed:                          0/0
        p2 = re.compile(r"^Invalid\s+received\/processed:\s+"
                        r"(?P<received>\d+)\/(?P<processed>\d+)$")

        # Data packet signal received/processed:               35669/35669
        p3 = re.compile(r"^Data\s+packet\s+signal\s+received\/processed:\s+"
                        r"(?P<received>\d+)\/(?P<processed>\d+)$")

        # L2 data packet signal received/processed:            0/0
        p4 = re.compile(r"^L2\s+data\s+packet\s+signal\s+received\/processed:\s+"
                        r"(?P<received>\d+)\/(?P<processed>\d+)$")

        # Status report received/processed:                    0/0
        p5 = re.compile(r"^Status\s+report\s+received\/processed:\s+"
                        r"(?P<received>\d+)\/(?P<processed>\d+)$")

        # Dyn-EID detected received/processed:                 0/0
        p6 = re.compile(r"^Dyn-EID\s+detected\s+received\/processed:\s+"
                        r"(?P<received>\d+)\/(?P<processed>\d+)$")

        # Dyn-EID decap stale detected received/processed:     0/0
        p7 = re.compile(r"^Dyn-EID\s+decap\s+stale\s+detected\s+received\/processed:\s+"
                        r"(?P<received>\d+)\/(?P<processed>\d+)$")

        # L2 dyn-EID decap stale detected received/processed:  0/0
        p8 = re.compile(r"^L2\s+dyn-EID\s+decap\s+stale\s+detected\s+"
                        r"received\/processed:\s+(?P<received>\d+)\/(?P<processed>\d+)$")

        # Dyn-EID adjacency discover received/processed:       0/0
        p9 = re.compile(r"^Dyn-EID\s+adjacency\s+discover\s+received\/"
                        r"processed:\s+(?P<received>\d+)\/(?P<processed>\d+)$")

        # delete map-cache received/processed:                 0/0
        p10 = re.compile(r"^delete\s+map-cache\s+received\/processed:\s+"
                         r"(?P<received>\d+)\/(?P<processed>\d+)$")

        # Remote update requests:                              0
        p11 = re.compile(r"^Remote\s+update\s+requests:\s+(?P<remote_update_requests>\d+)$")

        # Local update requests:                               5
        p12 = re.compile(r"^Local\s+update\s+requests:\s+(?P<local_update_requests>\d+)$")

        # Delete requests:                                     1
        p13 = re.compile(r"^Delete\s+requests:\s+(?P<delete_requests>\d+)$")

        # Update test:                                         0
        p14 = re.compile(r"^Update\s+test:\s+(?P<update_test>\d+)$")

        # Delete test:                                         0
        p15 = re.compile(r"^Delete\s+test:\s+(?P<delete_test>\d+)$")

        # Message sent:                                        6
        p16 = re.compile(r"^Message\s+sent:\s+(?P<message_sent>\d+)$")

        # Message received:                                    6
        p17 = re.compile(r"^Message\s+received:\s+(?P<message_received>\d+)$")

        # Unknown message received:                            0
        p18 = re.compile(r"^Unknown\s+message\s+received:\s+(?P<unknown_message_received>\d+)$")

        # Send Error:                                          0
        p19 = re.compile(r"^Send\s+Error:\s+(?P<send_errors>\d+)$")

        # Number of times blocked (flow control):              0
        p20 = re.compile(r"^Number\s+of\s+times\s+blocked\s+"
                         r"\(flow\s+control\):\s+(?P<flow_control>\d+)$")

        # Dropped notications from CEF:                          0
        p21 = re.compile(r"^Dropped\s+notications\s+"
                         r"from\s+CEF:\s+(?P<dropped_notifications>\d+)$")

        # Total notications from CEF:                            35669
        p22 = re.compile(r"^Total\s+notications\s+from\s+CEF:\s+(?P<total_notifications>\d+)$")

        # Dropped control packets in input queue:                0
        p23 = re.compile(r"^Dropped\s+control\s+packets\s+in\s+"
                         r"input\s+queue:\s+(?P<dropped_control_packets>\d+)$")

        # High priority input queue:                           0
        p24 = re.compile(r"^High\s+priority\s+input\s+queue:\s+(?P<high_priority_queue>\d+)$")

        # Normal priority input queue:                         0
        p25 = re.compile(r"^Normal\s+priority\s+input\s+queue:\s+(?P<normal_priority_queue>\d+)$")

        # DDT referral deferred/dropped:                       0/0
        p26 = re.compile(r"^DDT\s+referral\s+deferred\/dropped:\s+"
                         r"(?P<deferred>\d+)\/(?P<dropped>\d+)$")

        # DDT request deferred/dropped:                        0/0
        p27 = re.compile(r"^DDT\s+request\s+deferred\/dropped:\s+"
                         r"(?P<deferred>\d+)\/(?P<dropped>\d+)$")

        # DDT query deferred/dropped:                          0/0
        p28 = re.compile(r"^DDT\s+query\s+deferred\/dropped:\s+"
                         r"(?P<deferred>\d+)\/(?P<dropped>\d+)$")

        # Map-Request deferred/dropped:                        0/0
        p29 = re.compile(r"^Map-Request\s+deferred\/dropped:\s+"
                         r"(?P<deferred>\d+)\/(?P<dropped>\d+)$")

        # Map-Register deferred/dropped:                       0/0
        p30 = re.compile(r"^Map-Register\s+deferred\/dropped:\s+"
                         r"(?P<deferred>\d+)\/(?P<dropped>\d+)$")

        # Map-Reply deferred/dropped:                          0/0
        p31 = re.compile(r"^Map-Reply\s+deferred\/dropped:\s+"
                         r"(?P<deferred>\d+)\/(?P<dropped>\d+)$")

        # MR negative Map-Reply deferred/dropped:              0/0
        p32 = re.compile(r"^MR\s+negative\s+Map-Reply\s+deferred\/dropped:"
                         r"\s+(?P<deferred>\d+)\/(?P<dropped>\d+)$")

        # MR Map-Request fwd deferred/dropped:                 0/0
        p33 = re.compile(r"^MR\s+Map-Request\s+fwd\s+deferred\/dropped:"
                         r"\s+(?P<deferred>\d+)\/(?P<dropped>\d+)$")

        # MS Map-Request fwd deferred/dropped:                 0/0
        p34 = re.compile(r"^MS\s+Map-Request\s+fwd\s+deferred\/dropped:"
                         r"\s+(?P<deferred>\d+)\/(?P<dropped>\d+)$")

        # MS proxy Map-Reply deferred/dropped:                 0/0
        p35 = re.compile(r"^MS\s+proxy\s+Map-Reply\s+deferred\/dropped:"
                         r"\s+(?P<deferred>\d+)\/(?P<dropped>\d+)$")

        # xTR mcast Map-Notify deferred/dropped:               0/0
        p36 = re.compile(r"^xTR\s+mcast\s+Map-Notify\s+deferred\/dropped:"
                         r"\s+(?P<deferred>\d+)\/(?P<dropped>\d+)$")

        # MS Info-Reply deferred/dropped:                      0/0
        p37 = re.compile(r"^MS\s+Info-Reply\s+deferred\/dropped:\s+"
                         r"(?P<deferred>\d+)\/(?P<dropped>\d+)$")

        # MS Map-Notify deferred/dropped:                      0/0
        p38 = re.compile(r"^MS\s+Map-Notify\s+deferred\/dropped:\s+"
                         r"(?P<deferred>\d+)\/(?P<dropped>\d+)$")

        # RTR Map-Register fwd deferred/dropped:               0/0
        p39 = re.compile(r"^RTR\s+Map-Register\s+fwd\s+deferred\/dropped:"
                         r"\s+(?P<deferred>\d+)\/(?P<dropped>\d+)$")

        # RTR Map-Notify fwd deferred/dropped:                 0/0
        p40 = re.compile(r"^RTR\s+Map-Notify\s+fwd\s+deferred\/dropped:"
                         r"\s+(?P<deferred>\d+)\/(?P<dropped>\d+)$")

        # ETR Info-Request deferred/dropped:                   0/0
        p41 = re.compile(r"^ETR\s+Info-Request\s+deferred\/dropped:"
                         r"\s+(?P<deferred>\d+)\/(?P<dropped>\d+)$")

        # Invalid IP version drops:                              0
        p42 = re.compile(r"^Invalid\s+IP\s+version\s+drops:"
                         r"\s+(?P<invalid_ip_version_drops>\d+)$")

        # IPv4 UDP control packets:
        # IPv6 UDP control packets:
        p43 = re.compile(r"^IP(?P<ip_version>v4|v6)\s+UDP\s+control\s+packets:$")

        # Rcvd total packets:                                    0
        p44 = re.compile(r"^Rcvd\s+total\s+packets:\s+(?P<received_total_packets>\d+)$")

        # Rcvd invalid vrf:                                      0
        p45 = re.compile(r"^Rcvd\s+invalid\s+vrf:\s+(?P<received_invalid_vrf>\d+)$")

        # Rcvd invalid IP header:                                0
        p46 = re.compile(r"^Rcvd\s+invalid\s+IP\s+header:\s+(?P<received_invalid_ip_header>\d+)$")

        # Rcvd invalid protocol:                                 0
        p47 = re.compile(r"^Rcvd\s+invalid\s+protocol:\s+(?P<received_invalid_protocol>\d+)$")

        # Rcvd invalid size:                                     0
        p48 = re.compile(r"^Rcvd\s+invalid\s+size:\s+(?P<received_invalid_size>\d+)$")

        # Rcvd invalid port:                                     0
        p49 = re.compile(r"^Rcvd\s+invalid\s+port:\s+(?P<received_invalid_port>\d+)$")

        # Rcvd invalid checksum:                                 0
        p50 = re.compile(r"^Rcvd\s+invalid\s+checksum:\s+(?P<received_invalid_checksum>\d+)$")

        # Rcvd unsupported LISP:                                 0
        p51 = re.compile(r"^Rcvd\s+unsupported\s+LISP:\s+(?P<received_unsupported_lisp>\d+)$")

        # Rcvd not LISP control:                                 0
        p52 = re.compile(r"^Rcvd\s+not\s+LISP\s+control:\s+(?P<received_not_lisp_control>\d+)$")

        # Rcvd unknown LISP control:                             0
        p53 = re.compile(r"^Rcvd\s+unknown\s+LISP\s+control:\s+(?P<received_unknown_lisp_control>\d+)$")

        # Sent total packets:                                    0
        p54 = re.compile(r"^Sent\s+total\s+packets:\s+(?P<sent_total>\d+)$")

        # Sent flow controlled:                                  0
        p55 = re.compile(r"^Sent\s+flow\s+controlled:\s+(?P<sent_flow_controlled>\d+)$")

        for line in output.splitlines():
            line = line.strip()

            # FIB notications received/processed:                    35669/35669
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                received = int(groups['received'])
                processed = int(groups['processed'])
                fib_dict = ret_dict.setdefault('fib', {})
                notification_dict = fib_dict.setdefault('notifications', {})
                notification_dict.update({'received':received,
                                          'processed':processed})
                continue

            # Invalid received/processed:                          0/0
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                received = int(groups['received'])
                processed = int(groups['processed'])
                invalid_dict = fib_dict.setdefault('invalid', {})
                invalid_dict.update({'received':received,
                                     'processed':processed})
                continue

            # Data packet signal received/processed:               35669/35669
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                received = int(groups['received'])
                processed = int(groups['processed'])
                data_dict = fib_dict.setdefault('data_packet', {})
                data_dict.update({'received':received,
                                  'processed':processed})
                continue

            # L2 data packet signal received/processed:            0/0
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                received = int(groups['received'])
                processed = int(groups['processed'])
                l2_data_dict = fib_dict.setdefault('l2_data_packet', {})
                l2_data_dict.update({'received':received,
                                     'processed':processed})
                continue

            # Status report received/processed:                    0/0
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                received = int(groups['received'])
                processed = int(groups['processed'])
                status_dict = fib_dict.setdefault('status_report', {})
                status_dict.update({'received':received,
                                    'processed':processed})
                continue

            # Dyn-EID detected received/processed:                 0/0
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                received = int(groups['received'])
                processed = int(groups['processed'])
                dyn_dict = fib_dict.setdefault('dyn_eid_detected', {})
                dyn_dict.update({'received':received,
                                 'processed':processed})
                continue

            # Dyn-EID decap stale detected received/processed:     0/0
            m = p7.match(line)
            if m:
                groups = m.groupdict()
                received = int(groups['received'])
                processed = int(groups['processed'])
                dyn_decap_dict = fib_dict.setdefault('dyn_eid_decap_statle', {})
                dyn_decap_dict.update({'received':received,
                                       'processed':processed})
                continue

            # L2 dyn-EID decap stale detected received/processed:  0/0
            m = p8.match(line)
            if m:
                groups = m.groupdict()
                received = int(groups['received'])
                processed = int(groups['processed'])
                l2_dyn_decap_dict = fib_dict.setdefault('l2_dyn_eid_decap_statle', {})
                l2_dyn_decap_dict.update({'received':received,
                                          'processed':processed})
                continue

            # Dyn-EID adjacency discover received/processed:       0/0
            m = p9.match(line)
            if m:
                groups = m.groupdict()
                received = int(groups['received'])
                processed = int(groups['processed'])
                dyn_adjacency_dict = fib_dict.setdefault('dyn_eid_adjacency', {})
                dyn_adjacency_dict.update({'received':received,
                                           'processed':processed})
                continue

            # delete map-cache received/processed:                 0/0
            m = p10.match(line)
            if m:
                groups = m.groupdict()
                received = int(groups['received'])
                processed = int(groups['processed'])
                delete_dict = fib_dict.setdefault('delete_map_cache', {})
                delete_dict.update({'received':received,
                                    'processed':processed})
                continue

            # Remote update requests:                              0
            m = p11.match(line)
            if m:
                groups = m.groupdict()
                remote_update_requests = int(groups['remote_update_requests'])
                l2_dict = ret_dict.setdefault('l2_rib', {})
                l2_dict.update({'remote_update_requests':remote_update_requests})
                continue

            # Local update requests:                               5
            m = p12.match(line)
            if m:
                groups = m.groupdict()
                local_update_requests = int(groups['local_update_requests'])
                l2_dict.update({'local_update_requests':local_update_requests})
                continue

            # Delete requests:                                     1
            m = p13.match(line)
            if m:
                groups = m.groupdict()
                delete_requests = int(groups['delete_requests'])
                l2_dict.update({'delete_requests':delete_requests})
                continue

            # Update test:                                         0
            m = p14.match(line)
            if m:
                groups = m.groupdict()
                update_test = int(groups['update_test'])
                l2_dict.update({'update_test':update_test})
                continue

            # Delete test:                                         0
            m = p15.match(line)
            if m:
                groups = m.groupdict()
                delete_test = int(groups['delete_test'])
                l2_dict.update({'delete_test':delete_test})
                continue

            # Message sent:                                        6
            m = p16.match(line)
            if m:
                groups = m.groupdict()
                message_sent = int(groups['message_sent'])
                l2_dict.update({'message_sent':message_sent})
                continue

            # Message received:                                    6
            m = p17.match(line)
            if m:
                groups = m.groupdict()
                message_received = int(groups['message_received'])
                l2_dict.update({'message_received':message_received})
                continue

            # Unknown message received:                            0
            m = p18.match(line)
            if m:
                groups = m.groupdict()
                unknown_message_received = int(groups['unknown_message_received'])
                l2_dict.update({'unknown_message_received':unknown_message_received})
                continue

            # Send Error:                                          0
            m = p19.match(line)
            if m:
                groups = m.groupdict()
                send_errors = int(groups['send_errors'])
                l2_dict.update({'send_errors':send_errors})
                continue

            # Number of times blocked (flow control):              0
            m = p20.match(line)
            if m:
                groups = m.groupdict()
                flow_control = int(groups['flow_control'])
                l2_dict.update({'flow_control':flow_control})
                continue

            # Dropped notications from CEF:                          0
            m = p21.match(line)
            if m:
                groups = m.groupdict()
                dropped_notifications = int(groups['dropped_notifications'])
                cef_dict = ret_dict.setdefault('cef', {})
                cef_dict.update({'dropped_notifications':dropped_notifications})
                continue

            # Total notications from CEF:                            35669
            m = p22.match(line)
            if m:
                groups = m.groupdict()
                total_notifications = int(groups['total_notifications'])
                cef_dict.update({'total_notifications':total_notifications})
                continue

            # Dropped control packets in input queue:                0
            m = p23.match(line)
            if m:
                groups = m.groupdict()
                dropped_control_packets = int(groups['dropped_control_packets'])
                cef_dict.update({'dropped_control_packets':dropped_control_packets})
                continue

            # High priority input queue:                           0
            m = p24.match(line)
            if m:
                groups = m.groupdict()
                high_priority_queue = int(groups['high_priority_queue'])
                cef_dict.update({'high_priority_queue':high_priority_queue})
                continue

            # Normal priority input queue:                         0
            m = p25.match(line)
            if m:
                groups = m.groupdict()
                normal_priority_queue = int(groups['normal_priority_queue'])
                cef_dict.update({'normal_priority_queue':normal_priority_queue})
                continue

            # DDT referral deferred/dropped:                       0/0
            m = p26.match(line)
            if m:
                groups = m.groupdict()
                deferred = int(groups['deferred'])
                dropped = int(groups['dropped'])
                deferred_dict = ret_dict.setdefault('deffered', {})
                ddt_referral_dict = deferred_dict.setdefault('ddt_referral', {})
                ddt_referral_dict.update({'deferred':deferred,
                                          'dropped':dropped})
                continue

            # DDT request deferred/dropped:                        0/0
            m = p27.match(line)
            if m:
                groups = m.groupdict()
                deferred = int(groups['deferred'])
                dropped = int(groups['dropped'])
                ddt_request_dict = deferred_dict.setdefault('ddt_request', {})
                ddt_request_dict.update({'deferred':deferred,
                                         'dropped':dropped})
                continue

            # DDT query deferred/dropped:                          0/0
            m = p28.match(line)
            if m:
                groups = m.groupdict()
                deferred = int(groups['deferred'])
                dropped = int(groups['dropped'])
                ddt_query_dict = deferred_dict.setdefault('ddt_query', {})
                ddt_query_dict.update({'deferred':deferred,
                                       'dropped':dropped})
                continue

            # Map-Request deferred/dropped:                        0/0
            m = p29.match(line)
            if m:
                groups = m.groupdict()
                deferred = int(groups['deferred'])
                dropped = int(groups['dropped'])
                map_request_dict = deferred_dict.setdefault('map_request', {})
                map_request_dict.update({'deferred':deferred,
                                         'dropped':dropped})
                continue

            # Map-Register deferred/dropped:                       0/0
            m = p30.match(line)
            if m:
                groups = m.groupdict()
                deferred = int(groups['deferred'])
                dropped = int(groups['dropped'])
                map_register_dict = deferred_dict.setdefault('map_register', {})
                map_register_dict.update({'deferred':deferred,
                                          'dropped':dropped})
                continue

            # Map-Reply deferred/dropped:                          0/0
            m = p31.match(line)
            if m:
                groups = m.groupdict()
                deferred = int(groups['deferred'])
                dropped = int(groups['dropped'])
                map_reply_dict = deferred_dict.setdefault('map_reply', {})
                map_reply_dict.update({'deferred':deferred,
                                       'dropped':dropped})
                continue

            # MR negative Map-Reply deferred/dropped:              0/0
            m = p32.match(line)
            if m:
                groups = m.groupdict()
                deferred = int(groups['deferred'])
                dropped = int(groups['dropped'])
                mr_negative_dict = deferred_dict.setdefault('mr_negative_map_reply', {})
                mr_negative_dict.update({'deferred':deferred,
                                         'dropped':dropped})
                continue

            # MR Map-Request fwd deferred/dropped:                 0/0
            m = p33.match(line)
            if m:
                groups = m.groupdict()
                deferred = int(groups['deferred'])
                dropped = int(groups['dropped'])
                mr_map_request_dict = deferred_dict.setdefault('mr_map_request_fwd', {})
                mr_map_request_dict.update({'deferred':deferred,
                                            'dropped':dropped})
                continue

            # MS Map-Request fwd deferred/dropped:                 0/0
            m = p34.match(line)
            if m:
                groups = m.groupdict()
                deferred = int(groups['deferred'])
                dropped = int(groups['dropped'])
                ms_map_request_dict = deferred_dict.setdefault('ms_map_request_fwd', {})
                ms_map_request_dict.update({'deferred':deferred,
                                            'dropped':dropped})
                continue

            # MS proxy Map-Reply deferred/dropped:                 0/0
            m = p35.match(line)
            if m:
                groups = m.groupdict()
                deferred = int(groups['deferred'])
                dropped = int(groups['dropped'])
                ms_proxy_map_dict = deferred_dict.setdefault('ms_proxy_map_reply', {})
                ms_proxy_map_dict.update({'deferred':deferred,
                                          'dropped':dropped})
                continue

            # xTR mcast Map-Notify deferred/dropped:               0/0
            m = p36.match(line)
            if m:
                groups = m.groupdict()
                deferred = int(groups['deferred'])
                dropped = int(groups['dropped'])
                xtr_mcast_map_dict = deferred_dict.setdefault('xtr_mcast_map_notify', {})
                xtr_mcast_map_dict.update({'deferred':deferred,
                                           'dropped':dropped})
                continue

            # MS Info-Reply deferred/dropped:                      0/0
            m = p37.match(line)
            if m:
                groups = m.groupdict()
                deferred = int(groups['deferred'])
                dropped = int(groups['dropped'])
                ms_info_dict = deferred_dict.setdefault('ms_info_reply', {})
                ms_info_dict.update({'deferred':deferred,
                                     'dropped':dropped})
                continue

            # MS Map-Notify deferred/dropped:                      0/0
            m = p38.match(line)
            if m:
                groups = m.groupdict()
                deferred = int(groups['deferred'])
                dropped = int(groups['dropped'])
                ms_map_dict = deferred_dict.setdefault('ms_map_notify', {})
                ms_map_dict.update({'deferred':deferred,
                                    'dropped':dropped})
                continue

            # RTR Map-Register fwd deferred/dropped:               0/0
            m = p39.match(line)
            if m:
                groups = m.groupdict()
                deferred = int(groups['deferred'])
                dropped = int(groups['dropped'])
                rtr_map_dict = deferred_dict.setdefault('rtr_map_register_fwd', {})
                rtr_map_dict.update({'deferred':deferred,
                                     'dropped':dropped})
                continue

            # RTR Map-Notify fwd deferred/dropped:                 0/0
            m = p40.match(line)
            if m:
                groups = m.groupdict()
                deferred = int(groups['deferred'])
                dropped = int(groups['dropped'])
                rtr_map_notify_dict = deferred_dict.setdefault('rtr_map_notify_fwd', {})
                rtr_map_notify_dict.update({'deferred':deferred,
                                            'dropped':dropped})
                continue

            # ETR Info-Request deferred/dropped:                   0/0
            m = p41.match(line)
            if m:
                groups = m.groupdict()
                deferred = int(groups['deferred'])
                dropped = int(groups['dropped'])
                etr_info_request_dict = deferred_dict.setdefault('etr_info_request', {})
                etr_info_request_dict.update({'deferred':deferred,
                                              'dropped':dropped})
                continue

            # Invalid IP version drops:                              0
            m = p42.match(line)
            if m:
                groups = m.groupdict()
                invalid_ip_version_drops = int(groups['invalid_ip_version_drops'])
                invalid_dict = ret_dict.setdefault('errors', {})
                invalid_dict.update({'invalid_ip_version_drops':invalid_ip_version_drops})
                continue

            # IPv4 UDP control packets:
            # IPv6 UDP control packets:
            m = p43.match(line)
            if m:
                groups = m.groupdict()
                ip_version = groups['ip_version']
                ip_dict = ret_dict.setdefault('udp_control_packets', {}).setdefault(f'ip{ip_version}', {})

            # Rcvd total packets:                                    0
            m = p44.match(line)
            if m:
                groups = m.groupdict()
                received_total_packets = int(groups['received_total_packets'])
                ip_dict['received_total_packets'] = received_total_packets
                continue

            # Rcvd invalid vrf:                                      0
            m = p45.match(line)
            if m:
                groups = m.groupdict()
                received_invalid_vrf = int(groups['received_invalid_vrf'])
                ip_dict['received_invalid_vrf'] = received_invalid_vrf
                continue

            # Rcvd invalid IP header:                                0
            m = p46.match(line)
            if m:
                groups = m.groupdict()
                received_invalid_ip_header = int(groups['received_invalid_ip_header'])
                ip_dict['received_invalid_ip_header'] = received_invalid_ip_header
                continue

            # Rcvd invalid protocol:                                 0
            m = p47.match(line)
            if m:
                groups = m.groupdict()
                received_invalid_protocol = int(groups['received_invalid_protocol'])
                ip_dict['received_invalid_protocol'] = received_invalid_protocol
                continue

            # Rcvd invalid size:                                     0
            m = p48.match(line)
            if m:
                groups = m.groupdict()
                received_invalid_size = int(groups['received_invalid_size'])
                ip_dict['received_invalid_size'] = received_invalid_size
                continue

            # Rcvd invalid port:                                     0
            m = p49.match(line)
            if m:
                groups = m.groupdict()
                received_invalid_port = int(groups['received_invalid_port'])
                ip_dict['received_invalid_port'] = received_invalid_port
                continue

            # Rcvd invalid checksum:                                 0
            m = p50.match(line)
            if m:
                groups = m.groupdict()
                received_invalid_checksum = int(groups['received_invalid_checksum'])
                ip_dict['received_invalid_checksum'] = received_invalid_checksum
                continue

            # Rcvd unsupported LISP:                                 0
            m = p51.match(line)
            if m:
                groups = m.groupdict()
                received_unsupported_lisp = int(groups['received_unsupported_lisp'])
                ip_dict['received_unsupported_lisp'] = received_unsupported_lisp
                continue

            # Rcvd not LISP control:                                 0
            m = p52.match(line)
            if m:
                groups = m.groupdict()
                received_not_lisp_control = int(groups['received_not_lisp_control'])
                ip_dict['received_not_lisp_control'] = received_not_lisp_control
                continue

            # Rcvd unknown LISP control:                             0
            m = p53.match(line)
            if m:
                groups = m.groupdict()
                received_unknown_lisp_control = int(groups['received_unknown_lisp_control'])
                ip_dict['received_unknown_lisp_control'] = received_unknown_lisp_control
                continue

            # Sent total packets:                                    0
            m = p54.match(line)
            if m:
                groups = m.groupdict()
                sent_total = int(groups['sent_total'])
                ip_dict['sent_total'] = sent_total
                continue

            # Sent flow controlled:                                  0
            m = p55.match(line)
            if m:
                groups = m.groupdict()
                sent_flow_controlled = int(groups['sent_flow_controlled'])
                ip_dict['sent_flow_controlled'] = sent_flow_controlled
                continue
        return ret_dict

class ShowLispPlatformSmrKnownLocatorsSchema(MetaParser):

    schema = {
        'vrf': str,
        'address_family': str,
        'bits': int,
        Optional('locators'): {
            str: {
                'known_from': ListOf(str)
            }
        }
    }


class ShowLispPlatformSmrKnownLocatorsParser(ShowLispPlatformSmrKnownLocatorsSchema):

    """
    Parser for
      show lisp platform smr known-locators
    """

    cli_command = ['show lisp platform smr known-locators']

    def cli(self, output=None):

        if output is None:
            out = self.device.execute(self.cli_command[0])
        else:
            out = output

        ret_dict = {}

        # Platform requested masked SMR for:
        #  IPv6: 32 bits
        p1 = re.compile(r'^(?P<address_family>IPv\d): (?P<bits>\d+) bits$')

        # LISP known locators in VRF default
        p2 = re.compile(r'^LISP known locators in VRF (?P<vrf>\S+)$')

        # RLOC                    Known from
        # 2::2                    MS 3::3
        p3 = re.compile(r'^(?P<locator>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|'
                        r'([a-fA-F\d\:]+))\s+(?P<known_from>.+)$')

        for line in out.splitlines():
            line = line.strip()

            # Platform requested masked SMR for:
            #  IPv6: 32 bits            m = p1.match(line)
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['bits'] = int(groups['bits'])
                ret_dict['address_family'] = groups['address_family']
                continue

            # LISP known locators in VRF default        
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['vrf'] = groups['vrf']
                continue

            # RLOC                    Known from
            # 2::2                    MS 3::3   
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                locator = groups['locator']
                known_from = groups['known_from']

                source_list = ret_dict.setdefault('locators', {}).\
                                       setdefault(locator, {}).\
                                       setdefault('known_from', [])

                # Post pocessing
                sources = known_from.split(",")
                for source in sources:
                    element = source.strip()
                    source_list.append(element)
                continue

        return ret_dict

