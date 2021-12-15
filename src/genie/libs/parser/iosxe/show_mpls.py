"""  show_mpls.py
   supported commands:
        *  show mpls ldp neighbor
        *  show mpls ldp neighbor vrf <vrf>
        *  show mpls ldp neighbor detail
        *  show mpls ldp neighbor vrf <vrf> detail
        *  show mpls ldp bindings
        *  show mpls ldp bindings all
        *  show mpls ldp bindings all detail
        *  show mpls ldp capabilities
        *  show mpls ldp capabilities all
        *  show mpls ldp discovery
        *  show mpls ldp discovery detail
        *  show mpls ldp discovery all
        *  show mpls ldp discovery all detail
        *  show mpls ldp discovery vrf <vrf>
        *  show mpls ldp discovery vrf <vrf> detail
        *  show mpls ldp igp sync
        *  show mpls ldp igp sync all
        *  show mpls ldp igp sync interface <interface>
        *  show mpls ldp igp sync vrf <vrf>
        *  show mpls ldp statistics
        *  show mpls ldp parameters
        *  show mpls forwarding-table
        *  show mpls forwarding-table <prefix>
        *  show mpls forwarding-table interface tunnel <tunnelid>
        *  show mpls forwarding-table detail
        *  show mpls forwarding-table vrf <vrf>
        *  show mpls forwarding-table vrf <vrf> detail
        *  show mpls interfaces
        *  show mpls interfaces <interface>
        *  show mpls interfaces <interface> detail
        *  show mpls interfaces detail
        *  show mpls l2transport vc detail
        *  show mpls l2transport vc <vc_id> detail
        *  show mpls l2transport vc
        *  show mpls l2transport vc <vc_id>
        *  show mpls traffic-eng tunnels {tunnel}
        *  show mpls traffic-eng tunnels
        *  show mpls traffic-eng tunnels brief
"""

import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                               Any, \
                                               Optional

from genie.libs.parser.utils.common import Common
class ShowMplsLdpParametersSchema(MetaParser):
    """Schema for show mpls ldp Parameters"""

    schema = {
        Optional('ldp_featureset_manager'): {
            Any(): {
                'ldp_features': list,
            }
        },
        'ldp_backoff': {
            'initial': int,
            'maximum': int,
        },
        Optional('ldp_loop_detection'): str,
        Optional('ldp_nsr'): str,
        'version': int,
        'session_hold_time': int,
        'keep_alive_interval': int,
        Optional('ldp_for_targeted_sessions'): bool,
        'discovery_targeted_hello': {
            'holdtime': int,
            'interval': int,
        },
        'discovery_hello': {
            'holdtime': int,
            'interval': int,
        },
        Optional('downstream_on_demand_max_hop_count'): int,
    }

class ShowMplsLdpParameters(ShowMplsLdpParametersSchema):
    """Parser for show mpls ldp parameters"""

    cli_command = 'show mpls ldp parameters'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        result_dict = {}
        ldp_feature_flag = False
        ldp_feature_list = []

        # LDP Feature Set Manager: State Initialized
        p1 = re.compile(r'^LDP +Feature +Set +Manager: +(S|s)tate +(?P<state_initialized>\w+)$')
        #   LDP features:
        p2 = re.compile(r'^LDP +features:$')
        #  Auto-Configuration
        p2_1 = re.compile(r'^(?P<ldp_features>[\w\-]+)?$')
        # Protocol version: 1
        p3 = re.compile(r'^Protocol version: +(?P<version>\d+)$')
        # Session hold time: 180 sec; keep alive interval: 60 sec
        p4 = re.compile(r'^Session +hold +time: +(?P<session_holdtime>\d+) +sec;'
                        ' +keep +alive +interval: +(?P<keepalive_interval>\d+) +sec$')

        # Discovery hello: holdtime: 15 sec; interval: 5 sec
        p5 = re.compile(r'^Discovery +hello: +holdtime: +(?P<holdtime>\d+) +sec; +interval: +(?P<interval>\d+) +sec$')

        # Discovery targeted hello: holdtime: 90 sec; interval: 10 sec
        p6 = re.compile(r'^Discovery +targeted +hello: +holdtime: +(?P<targeted_holdtime>\d+) +sec; +interval:'
                        ' +(?P<targeted_interval>\d+) +sec$')

        # Downstream on Demand max hop count: 255
        p7 = re.compile(r'^Downstream +on +Demand +max +hop +count: +(?P<maxhop_count>\d+)$')
        # LDP for targeted sessions
        p8 = re.compile(r'^LDP +for +targeted +sessions$')
        # LDP initial/maximum backoff: 15/120 sec
        p9 = re.compile(r'^LDP +initial\/maximum +backoff: +(?P<initial>\w+)/+(?P<maximum>\w+) sec$')
        # LDP loop detection: off
        p10 = re.compile(r'^LDP +loop +detection: +(?P<loop_detection>\w+)$')
        # LDP NSR: Disabled
        p11 = re.compile(r'^LDP +NSR: +(?P<nsr>\w+)$')

        for line in out.splitlines():
            line = line.strip()

            # LDP Feature Set Manager: State Initialized
            m = p1.match(line)
            if m:
                ldp_feature_dict = result_dict.setdefault('ldp_featureset_manager', {}).setdefault('State Initialized', {})
                continue

            #  LDP features:
            m = p2.match(line)
            if m:
                ldp_feature_flag = True
                continue

            m = p2_1.match(line)
            if m:
                group = m.groupdict()
                if ldp_feature_flag:
                    ldp_feature_list.append(group['ldp_features'])
                    ldp_feature_dict.update({'ldp_features': ldp_feature_list})
                continue

            # Protocol version: 1
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ldp_feature_flag = False
                result_dict.update({'version': int(group['version'])})
                continue

            # Session hold time: 180 sec; keep alive interval: 60 sec
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ldp_feature_flag = False
                result_dict.update({'session_hold_time': int(group['session_holdtime'])})
                result_dict.update({'keep_alive_interval': int(group['keepalive_interval'])})
                continue

            # Discovery hello: holdtime: 15 sec; interval: 5 sec
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ldp_feature_flag = False
                discovery_hello = result_dict.setdefault('discovery_hello', {})
                discovery_hello.update({'holdtime': int(group['holdtime'])})
                discovery_hello.update({'interval': int(group['interval'])})
                continue

            # Discovery targeted hello: holdtime: 90 sec; interval: 10 sec
            m = p6.match(line)
            if m:
                group = m.groupdict()
                ldp_feature_flag = False
                discovery_targeted_hello = result_dict.setdefault('discovery_targeted_hello', {})
                discovery_targeted_hello.update({'holdtime': int(group['targeted_holdtime'])})
                discovery_targeted_hello.update({'interval': int(group['targeted_interval'])})
                continue

            # Downstream on Demand max hop count: 255
            m = p7.match(line)
            if m:
                group = m.groupdict()
                ldp_feature_flag = False
                result_dict.update({'downstream_on_demand_max_hop_count': int(group['maxhop_count'])})
                continue

            # LDP for targeted sessions
            m = p8.match(line)
            if m:
                ldp_feature_flag = False
                result_dict.update({'ldp_for_targeted_sessions': True})
                continue

            # LDP initial/maximum backoff: 15/120 sec
            m = p9.match(line)
            if m:
                group = m.groupdict()
                ldp_feature_flag = False
                backoff_dict = result_dict.setdefault('ldp_backoff', {})
                backoff_dict.update({'initial': int(group['initial'])})
                backoff_dict.update({'maximum': int(group['maximum'])})
                continue

            # LDP loop detection: off
            m = p10.match(line)
            if m:
                group = m.groupdict()
                ldp_feature_flag = False
                result_dict.update({'ldp_loop_detection': group['loop_detection']})
                continue

            # LDP NSR: Disabled
            m = p11.match(line)
            if m:
                group = m.groupdict()
                ldp_feature_flag = False
                result_dict.update({'ldp_nsr': group['nsr'].lower()})
                continue

        return result_dict


class ShowMplsLdpNsrStatisticsSchema(MetaParser):
    """Schema for show mpls ldp nsr statistics"""
    schema = {
        'statistics': {
            Optional('peer'): {
                Any(): {
                    'local_space_id': {
                        Any(): {
                            'in_label_request_records': {
                                'created': int,
                                'freed': int,
                            },
                            'in_label_withdraw_records': {
                                'created': int,
                                'freed': int,
                            },
                            'local_address_withdraw': {
                                'set': int,
                                'cleared': int,
                            },
                            'transmit_contexts': {
                                'enqueued': int,
                                'dequeued': int,
                            },
                        }
                    }
                },
            },
            'total_in_label_request_records': {
                'created': int,
                'freed': int,
            },
            'total_in_label_withdraw_records': {
                'created': int,
                'freed': int,
            },
            'total_local_address_withdraw_records': {
                'created': int,
                'freed': int,
            },
            'label_request_acks': {
                'number_of_chkpt_messages': {
                    'sent': int,
                    'in_queue': int,
                    'in_state_none': int,
                    'in_state_send': int,
                    'in_state_wait': int,
                },
            },
            'label_withdraw_acks': {
                'number_of_chkpt_messages': {
                    'sent': int,
                    'in_queue': int,
                    'in_state_none': int,
                    'in_state_send': int,
                    'in_state_wait': int,
                },
            },
            'address_withdraw_acks': {
                'number_of_chkpt_messages': {
                    'sent': int,
                    'in_queue': int,
                    'in_state_none': int,
                    'in_state_send': int,
                    'in_state_wait': int,
                },
            },
            'session_sync': {
                Any(): int,
            }
        }
    }

class ShowMplsLdpNsrStatistics(ShowMplsLdpNsrStatisticsSchema):
    """Parser for show mpls ldp nsr statistics"""

    cli_command = 'show mpls ldp nsr statistics'

    def cli(self,output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        result_dict = {}
        session_sync_flag = False

        # Peer: 10.169.197.253:0
        p1 = re.compile(
            r'^Peer: +(?P<peer>[\d\.]+):(?P<local_space_id>\d+)$')
        #   In label Request Records created: 0, freed: 0
        p2 = re.compile(
            r'^In +label +Request +Records +created: +(?P<created>\d+), +freed: +(?P<freed>\d+)$')

        #   In label Withdraw Records created: 0, freed: 0
        p3 = re.compile(
            r'^In +label +Withdraw +Records +created: +(?P<created>\d+), +freed: +(?P<freed>\d+)$')
        #   Local Address Withdraw Set: 0, Cleared: 0
        p4 = re.compile(
            r'^Local +Address +Withdraw +Set: +(?P<set>\d+), +Cleared: +(?P<cleared>\d+)$')

        #   Transmit contexts enqueued: 0, dequeued: 0
        p5 = re.compile(
            r'^Transmit +contexts +enqueued: +(?P<enqueued>\d+), +dequeued: +(?P<dequeued>\d+)$')
        # Total In label Request Records created: 0, freed: 0
        p6 = re.compile(
            r'^Total +In +label +Request +Records +created: +(?P<created>\d+), +freed: +(?P<freed>\d+)$')

        # Total In label Withdraw Records created: 0, freed: 0
        p7 = re.compile(
            r'^Total +In +label +Withdraw +Records +created: +(?P<created>\d+), +freed: +(?P<freed>\d+)$')
        # Total Local Address Withdraw Records created: 0, freed: 0
        p8 = re.compile(
            r'^Total +Local +Address +Withdraw +Records +created: +(?P<created>\d+), +freed: +(?P<freed>\d+)$')
        # Label Request Acks:
        p9 = re.compile(r'^Label +Request +Acks:$')

        #   Number of chkpt msg sent: 0
        p10 = re.compile(r'^Number +of +chkpt +msg +sent: +(?P<msg_sent>\d+)$')
        #   Number of chkpt msg in queue: 0
        p11 = re.compile(r'^Number +of +chkpt +msg +in +queue: +(?P<queue>\d+)$')
        #   Number of chkpt msg in state none: 0
        p12 = re.compile(r'^Number +of +chkpt +msg +in +state +none: +(?P<state_none>\d+)$')
        #   Number of chkpt msg in state send: 0
        p13 = re.compile(r'^Number +of +chkpt +msg +in +state +send: +(?P<state_send>\d+)$')
        #   Number of chkpt msg in state wait: 0
        p14 = re.compile(r'^Number +of +chkpt +msg +in +state +wait: +(?P<state_wait>\d+)$')
        # Label Withdraw Acks:
        p15= re.compile(r'^Label +Withdraw +Acks:$')
        # Address Withdraw Acks:
        p16 = re.compile(r'^Address +Withdraw +Acks:$')
        # Session Sync:
        p17 = re.compile(r'^Session +Sync:$')

        #   Number of session-sync msg sent: 0
        p18 = re.compile(r'^(?P<session_sync_keys>^(Number)[\S\s]+): (?P<session_sync_values>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            # Peer: 10.169.197.253:0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                statistic_dict = result_dict.setdefault('statistics', {})
                peer_dict = statistic_dict.setdefault('peer',{}).\
                                           setdefault(group['peer'], {}).\
                                           setdefault('local_space_id', {}).\
                                           setdefault(int(group['local_space_id']), {})
                continue

            #   In label Request Records created: 0, freed: 0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                label_request = peer_dict.setdefault('in_label_request_records', {})
                label_request.update({'created': int(group['created'])})
                label_request.update({'freed': int(group['freed'])})
                continue

            #   In label Withdraw Records created: 0, freed: 0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                label_withdraw = peer_dict.setdefault('in_label_withdraw_records', {})
                label_withdraw.update({'created': int(group['created'])})
                label_withdraw.update({'freed': int(group['freed'])})
                continue

            #   Local Address Withdraw Set: 0, Cleared: 0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                label_address_request = peer_dict.setdefault('local_address_withdraw', {})
                label_address_request.update({'set': int(group['set'])})
                label_address_request.update({'cleared': int(group['cleared'])})
                continue

            #   Transmit contexts enqueued: 0, dequeued: 0
            m = p5.match(line)
            if m:
                group = m.groupdict()
                transmit_dict = peer_dict.setdefault('transmit_contexts', {})
                transmit_dict.update({'enqueued': int(group['enqueued'])})
                transmit_dict.update({'dequeued': int(group['dequeued'])})
                continue

            # Total In label Request Records created: 0, freed: 0
            m = p6.match(line)
            if m:
                group = m.groupdict()
                statistic_dict = result_dict.setdefault('statistics', {})
                total_label_dict = statistic_dict.setdefault('total_in_label_request_records', {})
                total_label_dict.update({'created': int(group['created'])})
                total_label_dict.update({'freed': int(group['freed'])})
                continue

            # Total In label Withdraw Records created: 0, freed: 0
            m = p7.match(line)
            if m:
                group = m.groupdict()
                total_withdraw_dict = statistic_dict.setdefault('total_in_label_withdraw_records', {})
                total_withdraw_dict.update({'created': int(group['created'])})
                total_withdraw_dict.update({'freed': int(group['freed'])})
                continue

            # Total Local Address Withdraw Records created: 0, freed: 0
            m = p8.match(line)
            if m:
                group = m.groupdict()
                total_local_address_dict = statistic_dict.setdefault('total_local_address_withdraw_records', {})
                total_local_address_dict.update({'created': int(group['created'])})
                total_local_address_dict.update({'freed': int(group['freed'])})
                continue

            # Label Request Acks:
            m = p9.match(line)
            if m:
                # label_request_acks = True
                temp_dict = statistic_dict.setdefault('label_request_acks', {})
                continue

            #   Number of chkpt msg sent: 0
            m = p10.match(line)
            if m:
                group = m.groupdict()
                temp_dict.setdefault('number_of_chkpt_messages',{}).update({'sent': int(group['msg_sent'])})
                continue

            #   Number of chkpt msg in queue: 0
            m = p11.match(line)
            if m:
                session_sync_flag = False
                group = m.groupdict()
                temp_dict.setdefault('number_of_chkpt_messages', {}).update({'in_queue': int(group['queue'])})
                continue

            #   Number of chkpt msg in state none: 0
            m = p12.match(line)
            if m:
                session_sync_flag = False
                group = m.groupdict()
                temp_dict.setdefault('number_of_chkpt_messages', {}).update({'in_state_none': int(group['state_none'])})
                continue

            #   Number of chkpt msg in state send: 0
            m = p13.match(line)
            if m:
                session_sync_flag = False
                group = m.groupdict()
                temp_dict.setdefault('number_of_chkpt_messages', {}).update({'in_state_send': int(group['state_send'])})
                continue

            #   Number of chkpt msg in state wait: 0
            m = p14.match(line)
            if m:
                session_sync_flag = False
                group = m.groupdict()
                temp_dict.setdefault('number_of_chkpt_messages', {}).update({'in_state_wait': int(group['state_wait'])})
                continue

            # Label Withdraw Acks:
            m = p15.match(line)
            if m:
                temp_dict = statistic_dict.setdefault('label_withdraw_acks', {})
                continue

            # Address Withdraw Acks:
            m = p16.match(line)
            if m:
                temp_dict = statistic_dict.setdefault('address_withdraw_acks', {})
                continue

            # Session Sync:
            m = p17.match(line)
            if m:
                session_sync_flag = True
                session_sync_dict = statistic_dict.setdefault('session_sync', {})
                continue

            #   Number of session-sync msg sent: 0
            m = p18.match(line)
            if m:
                if session_sync_flag:
                    group = m.groupdict()
                    key = group['session_sync_keys'].lower().replace(' ','_')
                    session_sync_dict.update({key.replace('-','_'): int(group['session_sync_values'])})
                continue
        return result_dict


class ShowMplsLdpNeighborSchema(MetaParser):
    """Schema for show mpls ldp neighbor"""
    schema = {
        'vrf': {
            Any(): {
                'peers': {
                    Any(): {
                        'label_space_id':{
                            Any():{
                                'local_ldp_ident': str,
                                'tcp_connection': str,
                                'state': str,
                                'msg_sent': int,
                                'msg_rcvd': int,
                                'downstream': bool,
                                Optional('last_tib_rev_sent'): int,
                                Optional('password'): str,
                                Optional('uptime'): str,
                                Optional('peer_holdtime_ms'): int,
                                Optional('ka_interval_ms'): int,
                                Optional('peer_state'): str,
                                Optional('ldp_discovery_sources'): {
                                    'interface':{
                                          Any():{
                                          Optional('ip_address'): {
                                              Any(): {
                                                  Optional('holdtime_ms'): int,
                                                  Optional('hello_interval_ms'): int,
                                              }
                                          }
                                        }
                                    }
                                },
                                Optional('address_bound'): list,
                                Optional('nsr'): str,
                                Optional('capabilities'):{
                                     'sent': {
                                         Optional('ICCP'):{
                                            'type': str,
                                            'maj_ver': int,
                                            'min_ver': int,
                                         },
                                        Optional('dynamic_anouncement'): str,
                                        Optional('mldp_point_to_multipoint'): str,
                                        Optional('mldp_multipoint_to_multipoint'): str,
                                        Optional('typed_wildcard'): str,
                                     },
                                    Optional('received'): {
                                        Optional('ICCP'):{
                                            'type': str,
                                            'maj_ver': int,
                                            'min_ver': int,
                                        },
                                        Optional('dynamic_anouncement'): str,
                                        Optional('mldp_point_to_multipoint'): str,
                                        Optional('mldp_multipoint_to_multipoint'): str,
                                        Optional('typed_wildcard'): str,
                                    },

                                },
                            },
                        },
                    }
                }
            }
        },
    }


class ShowMplsLdpNeighbor(ShowMplsLdpNeighborSchema):
    """Parser for show mpls ldp neighbor,
                  show mpls ldp neighbor vrf <vrf>"""

    cli_command = ['show mpls ldp neighbor', 'show mpls ldp neighbor vrf {vrf}']

    def cli(self, vrf="", output=None):
        if output is None:
            if vrf:
                cmd = self.cli_command[1].format(vrf=vrf)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        if not vrf:
            vrf = 'default'

        # initial return dictionary
        result_dict = {}
        address_bound_flag = False
        received_flag = False
        sent_flag = False

        # Peer LDP Ident: 10.169.197.252:0; Local LDP Ident 10.169.197.254:0
        p1 = re.compile(r'^Peer +LDP +Ident: *(?P<peer_ldp>[\d\.]+):(?P<label_space_id>\d+); +Local +LDP +Ident +(?P<local_ldp>\S+)$')

        #     TCP connection: 10.169.197.252.646 - 10.169.197.254.20170
        p2 = re.compile(r'^TCP +connection: *(?P<tcp_connection>[\S\s]+)$')

        #     State: Oper; Msgs sent/rcvd: 824/825; Downstream
        #     State: Oper; Msgs sent/rcvd: 824/825; Downstream; Last TIB rev sent 4103
        #     State: Oper; Msgs sent/rcvd: 5855/6371; Downstream on demand
        p3 = re.compile(r'^State: *(?P<state>\w+); +Msgs +sent\/rcvd: *(?P<msg_sent>\d+)\/(?P<msg_rcvd>\d+);'
                                ' +(?P<downstream>[\w\s]+)(; +Last +TIB +rev +sent +(?P<last_tib_rev_sent>\d+))?$')

        #  Up time: 04:26:14
        #  Up time: 3d21h; UID: 4; Peer Id 0
        p4 = re.compile(r'^Up +time: *(?P<up_time>[\w\:]+)(; +UID: *(?P<uid>\d+); +Peer +Id +(?P<peer_id>\d+))?$')

        #     LDP discovery sources:
        #       GigabitEthernet0/0/0, Src IP addr: 10.169.197.93
        #       ATM3/0.1
        p5 = re.compile(r'^(?P<interface>[A-Za-z]+[\d/.]+)((,|;) +Src +IP +addr: *(?P<src_ip_address>[\d\.]+))?$')

        #       holdtime: 15000 ms, hello interval: 5000 ms
        p5_1 = re.compile(r'^holdtime: *(?P<holdtime>\d+) +ms, +hello +interval: *(?P<hello_interval>\d+) +ms$')

        #     Addresses bound to peer LDP Ident:
        p6 = re.compile(r'^Addresses +bound +to +peer +LDP +Ident:$')

        #       10.169.197.252 10.120.202.49    10.169.197.101 10.16.190.254
        p7 = re.compile(r'^(?P<address_bound_peer_ldp>[\d\.\s]+)$')

        # Peer holdtime: 180000 ms; KA interval: 60000 ms; Peer state: estab
        p8 = re.compile(r'^Peer +holdtime: *(?P<peer_holdtime>\d+) +ms; +KA +interval: *(?P<ka_interval>\d+) +ms;'
                         ' +Peer +state: +(?P<peer_state>\S+)$')

        # Password: not required, none, in use
        p9 = re.compile(r'^Password: +(?P<password>[\S\s]+)$')

        #NSR: Not Ready
        p10 = re.compile(r'^NSR: +(?P<nsr>[\S\s]+)$')

        # Capabilities Sent:
        p11 = re.compile(r'^Capabilities +Sent:$')

        #   [ICCP (type 0x0405) MajVer 1 MinVer 0]
        p12 = re.compile(r'^\[ICCP \(type +(?P<type>\w+)\) +MajVer +(?P<maj_ver>\d+) +MinVer +(?P<min_ver>\d+)\]$')

        #   [Dynamic Announcement (0x0506)]
        p13 = re.compile(r'^\[Dynamic +Announcement \((?P<dynamic_anouncement>\w+)\)\]$')

        #   [mLDP Point-to-Multipoint (0x0508)]
        p14 = re.compile(r'^\[mLDP +Point\-to\-Multipoint \((?P<mldp_point_to_multipoint>\w+)\)\]$')
        #   [mLDP Multipoint-to-Multipoint (0x0509)]
        p15 = re.compile(r'^\[mLDP +Multipoint\-to\-Multipoint \((?P<mldp_multipoint_to_multipoint>\w+)\)\]$')
        #   [Typed Wildcard (0x050B)]
        p16 = re.compile(r'^\[Typed +Wildcard \((?P<typed_wildcard>\w+)\)\]$')

        # Capabilities Received:
        p17 = re.compile(r'^Capabilities +Received:$')
        #   [None]
        p18 = re.compile(r'^\[None\]$')

        for line in out.splitlines():
            line = line.strip()
            # Peer LDP Ident: 10.169.197.252:0; Local LDP Ident 10.169.197.254:0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                address_bound_flag = False
                peer_dict = result_dict.setdefault('vrf', {}).\
                                        setdefault(vrf, {}).\
                                        setdefault('peers', {}).\
                                        setdefault(group['peer_ldp'], {}).\
                                        setdefault('label_space_id', {}).\
                                        setdefault(int(group['label_space_id']), {})
                peer_dict.update({'local_ldp_ident':group['local_ldp']})
                continue

            # TCP connection: 10.169.197.252.646 - 10.169.197.254.20170
            m = p2.match(line)
            if m:
                group = m.groupdict()
                tcpconnection = group['tcp_connection']
                peer_dict.update({'tcp_connection': tcpconnection})
                continue

            # State: Oper; Msgs sent/rcvd: 824/825; Downstream
            # State: Oper; Msgs sent/rcvd: 824/825; Downstream; Last TIB rev sent 4103
            m = p3.match(line)
            if m:
                group = m.groupdict()
                peer_dict.update({'state': group['state'].lower()})
                peer_dict.update({'msg_sent': int(group['msg_sent'])})
                peer_dict.update({'msg_rcvd': int(group['msg_rcvd'])})
                peer_dict.update({'downstream': True if 'downstream' in group['downstream'].lower() else False})
                if group['last_tib_rev_sent']:
                    peer_dict.update({'last_tib_rev_sent': int(group['last_tib_rev_sent'])})
                continue

            # Up time: 04:26:14
            m = p4.match(line)
            if m:
                group = m.groupdict()
                peer_dict.update({'uptime': group['up_time']})
                continue

            #  GigabitEthernet0/0/0, Src IP addr: 10.169.197.93
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ldp_source_dict = peer_dict.setdefault('ldp_discovery_sources',{}).\
                                            setdefault('interface',{}).\
                                            setdefault(group['interface'],{})
                if group['src_ip_address']:
                    ldp_source_ip_address_dict = ldp_source_dict.setdefault('ip_address',{}).\
                                                    setdefault(group['src_ip_address'],{})
                continue

            # holdtime: 15000 ms, hello interval: 5000 ms
            m = p5_1.match(line)
            if m:
                group = m.groupdict()
                ldp_source_ip_address_dict.update({'holdtime_ms': int(group['holdtime'])})
                ldp_source_ip_address_dict.update({'hello_interval_ms': int(group['hello_interval'])})
                continue

            #  Addresses bound to peer LDP Ident:
            m = p6.match(line)
            if m:
                address_bound_flag = True
                continue

            #  10.169.197.252 10.120.202.49    10.169.197.101 10.16.190.254
            m = p7.match(line)
            if m:
                group = m.groupdict()
                address_bound_list = group['address_bound_peer_ldp'].split()
                if address_bound_flag:
                    if 'address_bound' not in peer_dict:
                        peer_dict.update({'address_bound': address_bound_list})
                    else:
                        peer_dict['address_bound'].extend(address_bound_list)
                continue

            # Peer holdtime: 180000 ms; KA interval: 60000 ms; Peer state: estab
            m = p8.match(line)
            if m:
                group = m.groupdict()
                peer_dict.update({'peer_holdtime_ms': int(group['peer_holdtime'])})
                peer_dict.update({'ka_interval_ms': int(group['ka_interval'])})
                peer_dict.update({'peer_state': group['peer_state']})
                continue

            # Password: not required, none, in use
            m = p9.match(line)
            if m:
                group = m.groupdict()
                peer_dict.update({'password': group['password']})
                continue

            # NSR: Not Ready
            m = p10.match(line)
            if m:
                group = m.groupdict()
                peer_dict.update({'nsr': group['nsr']})
                continue

            # Capabilities Sent:
            m = p11.match(line)
            if m:
                received_flag = False
                sent_flag = True
                temp_dict = peer_dict.setdefault('capabilities', {}).setdefault('sent', {})
                continue

            #   [ICCP (type 0x0405) MajVer 1 MinVer 0]
            m = p12.match(line)
            if m:
                group = m.groupdict()
                iccp_dict = temp_dict.setdefault('ICCP',{})
                iccp_dict.update({'type': group['type']})
                iccp_dict.update({'maj_ver': int(group['maj_ver'])})
                iccp_dict.update({'min_ver': int(group['min_ver'])})

                continue

            #   [Dynamic Announcement (0x0506)]
            m = p13.match(line)
            if m:
                group = m.groupdict()
                temp_dict.update({'dynamic_anouncement': group['dynamic_anouncement']})
                continue

            #   [mLDP Point-to-Multipoint (0x0508)]
            m = p14.match(line)
            if m:
                group = m.groupdict()
                temp_dict.update({'mldp_point_to_multipoint': group['mldp_point_to_multipoint']})
                continue

            #   [mLDP Multipoint-to-Multipoint (0x0509)]
            m = p15.match(line)
            if m:
                group = m.groupdict()
                temp_dict.update({'mldp_multipoint_to_multipoint': group['mldp_multipoint_to_multipoint']})
                continue

            #   [Typed Wildcard (0x050B)]
            m = p16.match(line)
            if m:
                group = m.groupdict()
                temp_dict.update({'typed_wildcard': group['typed_wildcard']})
                continue

            # Capabilities Received:
            m = p17.match(line)
            if m:
                received_flag = True
                sent_flag = False
                temp_dict = peer_dict.setdefault('capabilities', {}).setdefault('received', {})
                continue

            # [None]
            m = p18.match(line)
            if m:
                if received_flag:
                    peer_dict['capabilities'].pop('received')
                if sent_flag:
                    peer_dict['capabilities'].pop('sent')
                continue

        return result_dict


class ShowMplsLdpNeighborDetail(ShowMplsLdpNeighbor):
    """Parser for show mpls ldp neighbor detail,
                  show mpls ldp neighbor vrf <vrf> detail"""

    cli_command = ['show mpls ldp neighbor detail', 'show mpls ldp neighbor vrf {vrf} detail']

    def cli(self, vrf="", output=None):
        if output is None:
            if vrf:
                cmd = self.cli_command[1].format(vrf=vrf)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        return super().cli(vrf=vrf, output=out)


class ShowMplsLdpBindingsSchema(MetaParser):
    """
    Schema for show mpls ldp bindings
               show mpls ldp bindings all
               show mpls ldp bindings all detail
    """
    schema = {
        'vrf':{
           Any():{
                'lib_entry':{
                    Any():{
                        'rev': str,
                        Optional('checkpoint'): str,
                        Optional('no_route'): bool,
                        Optional('label_binding'): {
                            'label':{
                                Any():{
                                    Optional('owner'): str,
                                    Optional('advertised_to'): list,
                                },
                            },
                        },
                        Optional('remote_binding'): {
                            'label': {
                                Any():{
                                    'lsr_id':{
                                        Any():{
                                            'label_space_id':{
                                                Any(): {
                                                    Optional('checkpointed'): bool,
                                                },
                                            }
                                        }
                                    }
                                }
                            }
                        },
                    },
                },
            },
        },
    }

class ShowMplsLdpBindings(ShowMplsLdpBindingsSchema):
    """
       Parser for show mpls ldp bindings
                  show mpls ldp bindings vrf <vrf>
                  show mpls ldp bindings all
                  show mpls ldp bindings all detail
       """
    cli_command = ['show mpls ldp bindings',
                   'show mpls ldp bindings {all}',
                   'show mpls ldp bindings {all} {detail}',
                   'show mpls ldp bindings vrf {vrf}']

    def cli(self, vrf="", all="", detail="", output=None):
        if output is None:
            if vrf:
                cmd = self.cli_command[3].format(vrf=vrf)
            else:
                vrf='default'
                if not all and not detail:
                    cmd = self.cli_command[0]
                if all and not detail:
                    cmd = self.cli_command[1].format(all=all)
                if all and detail:
                    cmd = self.cli_command[2].format(all=all, detail=detail)
            out = self.device.execute(cmd)
        else:
            out = output

        if not vrf:
            vrf = 'default'
        # initial return dictionary
        result_dict = {}

        # VRF vrf1:
        p0 = re.compile(r'^VRF +(?P<vrf>\S+):$')
        # lib entry: 10.186.1.0/24, rev 1028
        # lib entry: 10.186.1.0/24, rev 1028,
        # lib entry: 10.120.202.64/32, rev 12, chkpt: none
        # tib entry: 10.0.0.0/8, rev 4
        # 10.16.16.16/32, rev 775
        # lib entry: 10.0.0.0/8, rev 300(no route)
        p1 = re.compile(r'^([\w]+ +entry: +)?(?P<lib_entry>[\d\.\/]+), +rev +(?P<rev>\d+),'
            '?( +chkpt: +(?P<checkpoint>\S+))?(, +elc)?(?P<no_route>\(no route\))?$')

        #  local binding:  label: 2536
        #  local binding:  label: 2027 (owner LDP)
        p2 = re.compile(r'^local +binding: +label: +(?P<local_label>\S+)( +\(owner +(?P<owner>\w+)\))?$')

        #  Advertised to:
        # 10.169.197.252:0      10.169.197.253:0
        p3 = re.compile(r'^(?P<advertised_to>[\d\.\:\s]+)$')

        #  remote binding: lsr: 10.169.197.252:0, label: 508
        #  remote binding: lsr: 10.169.197.253:0, label: 308016 checkpointed
        p4 = re.compile(r'^remote +binding: +lsr: +(?P<lsr>[\d\.]+):(?P<label_space_id>[\d]+),'
                        ' +label: +(?P<remote_label>\S+)( +(?P<checkpointed>\w+))?(, +elc)?$')


        for line in out.splitlines():
            line = line.strip()

            # VRF vrf1:
            m = p0.match(line)
            if m:
                group = m.groupdict()
                vrf = group['vrf']
                continue

            # lib entry: 10.186.1.0/24, rev 1028
            # lib entry: 10.120.202.64/32, rev 12, chkpt: none
            m = p1.match(line)
            if m:
                group = m.groupdict()
                lib_entry_dict = result_dict.setdefault('vrf', {}).\
                                            setdefault(vrf, {}).\
                                            setdefault('lib_entry', {}).\
                                            setdefault(group['lib_entry'],{})
                lib_entry_dict.update({'rev': group['rev']})
                if group['checkpoint']:
                    lib_entry_dict.update({'checkpoint': group['checkpoint']})
                if group['no_route']:
                    lib_entry_dict.update({'no_route': True})
                continue

            # local binding:  label: 2536
            # local binding:  label: 2027 (owner LDP)
            m = p2.match(line)
            if m:
                group = m.groupdict()
                local_dict = lib_entry_dict.setdefault('label_binding', {}).setdefault('label',{}).\
                                            setdefault(group['local_label'],{})
                if group['owner']:
                    local_dict.update({'owner': group['owner']})
                continue

            # 10.169.197.252:0      10.169.197.253:0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                if 'advertised_to' not in local_dict:
                    local_dict.update({'advertised_to': group['advertised_to'].split()})
                else:
                    local_dict['advertised_to'].extend(group['advertised_to'].split())
                continue

            # remote binding: lsr: 10.169.197.252:0, label: 508
            # remote binding: lsr: 10.169.197.253:0, label: 308016 checkpointed
            m = p4.match(line)
            if m:
                group = m.groupdict()
                index_dict = lib_entry_dict.setdefault('remote_binding', {}).\
                                            setdefault('label',{}).\
                                            setdefault(group['remote_label'], {}).\
                                            setdefault('lsr_id', {}).\
                                            setdefault(group['lsr'],{}).\
                                            setdefault('label_space_id',{}).\
                                            setdefault(int(group['label_space_id']),{})
                if group['checkpointed']:
                    index_dict.update({'checkpointed': True})
                continue

        return result_dict

# ==============================================
#   Show mpls ldp capabilities
# ==============================================
class ShowMplsLdpCapabilitiesSchema(MetaParser):
    """
    Schema for show mpls ldp capabilities
               show mpls ldp capabilities all
    """
    schema = {
        'ldp_capabilities': {
            Optional('iccp_type'): str,
            Optional('maj_version'): int,
            Optional('min_version'): int,
            Optional('dynamic_anouncement'): str,
            Optional('mldp_point_to_multipoint'): str,
            Optional('mldp_multipoint_to_multipoint'): str,
            Optional('typed_wildcard'): str,
        }
    }

class ShowMplsLdpCapabilities(ShowMplsLdpCapabilitiesSchema):
    """
       Parser for show mpls ldp capabilities
                  show mpls ldp capabilities all
       """
    cli_command = ['show mpls ldp capabilities','show mpls ldp capabilities {all}']

    def cli(self, all="", output=None):
        if output is None:
            if not all:
                cmd = self.cli_command[0]
            else:
                cmd = self.cli_command[1].format(all=all)
            out = self.device.execute(cmd)
        else:
            out = output

        # initial return dictionary
        result_dict = {}
        # LDP Capabilities - [<description> (<type>)]
        p0 = re.compile(r'^LDP +Capabilities +\- +\[\<description\> +\(\<type\>\)\]$')

        #   [ICCP (type 0x0405) MajVer 1 MinVer 0]
        p1 = re.compile(r'^\[ICCP \(type +(?P<type>\w+)\) +MajVer +(?P<maj_ver>\d+) +MinVer +(?P<min_ver>\d+)\]$')

        #   [Dynamic Announcement (0x0506)]
        p2 = re.compile(r'^\[Dynamic +Announcement \((?P<dynamic_anouncement>\w+)\)\]$')

        #   [mLDP Point-to-Multipoint (0x0508)]
        p3 = re.compile(r'^\[mLDP +Point\-to\-Multipoint \((?P<mldp_point_to_multipoint>\w+)\)\]$')
        #   [mLDP Multipoint-to-Multipoint (0x0509)]
        p4 = re.compile(r'^\[mLDP +Multipoint\-to\-Multipoint \((?P<mldp_multipoint_to_multipoint>\w+)\)\]$')
        #   [Typed Wildcard (0x050B)]
        p5 = re.compile(r'^\[Typed +Wildcard \((?P<typed_wildcard>\w+)\)\]$')


        for line in out.splitlines():
            line = line.strip()

            m = p0.match(line)
            if m:
                ldp_dict = result_dict.setdefault('ldp_capabilities',{})
                continue

            #   [ICCP (type 0x0405) MajVer 1 MinVer 0]
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ldp_dict.update({'iccp_type': group['type']})
                ldp_dict.update({'maj_version': int(group['maj_ver'])})
                ldp_dict.update({'min_version': int(group['min_ver'])})

                continue

            # [Dynamic Announcement (0x0506)]
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ldp_dict.update({'dynamic_anouncement': group['dynamic_anouncement']})
                continue

            # [mLDP Point-to-Multipoint (0x0508)]
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ldp_dict.update({'mldp_point_to_multipoint': group['mldp_point_to_multipoint']})
                continue

            # [mLDP Multipoint-to-Multipoint (0x0509)]
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ldp_dict.update({'mldp_multipoint_to_multipoint': group['mldp_multipoint_to_multipoint']})
                continue

            # [Typed Wildcard (0x050B)]
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ldp_dict.update({'typed_wildcard': group['typed_wildcard']})
                continue

        return result_dict

# ==============================================
#   Show mpls ldp discovery
# ==============================================
class ShowMplsLdpDiscoverySchema(MetaParser):
    """
    Schema for show mpls ldp discovery
               show mpls ldp discovery all
               show mpls ldp discovery all detail
               show mpls ldp discovery detail
               show mpls ldp discovery vrf <vrf>
               show mpls ldp discovery vrf <vrf> detail
    """
    schema = {
        'vrf': {
            Any(): {
                Optional('local_ldp_identifier'): {
                    Any(): {
                        Optional('discovery_sources'): {
                            'interfaces': {
                                Any(): {
                                    Optional('enabled'): str,
                                    Optional('hello_interval_ms'): int,
                                    Optional('transport_ip_addr'): str,
                                    'session': str,
                                    Optional('xmit'): bool,
                                    Optional('recv'): bool,
                                    Any(): {
                                        Any(): {
                                            Optional('transport_ip_address'): str,
                                            Optional('source_ip_address'): str,
                                            Optional('holdtime_sec'): int,
                                            Optional('proposed_local'): int,
                                            Optional('proposed_peer'): int,
                                            Optional('reachable_via'): str,
                                            Optional('password'): str,
                                            Optional('clients'): str,
                                        },
                                    },
                                },
                            },
                        },
                        Optional('targeted_hellos'): {
                            Any(): {
                                Any(): {
                                    'session': str,
                                    Optional('ldp_id'): str,
                                    Optional('tdp_id'): str,
                                    Optional('xmit'): bool,
                                    Optional('recv'): bool,
                                    'active': bool,
                                },
                            },
                        },
                    },
                },
            },
        },

    }

class ShowMplsLdpDiscovery(ShowMplsLdpDiscoverySchema):
    """
        Parser for show mpls ldp discovery
                   show mpls ldp discovery all
                   show mpls ldp discovery all detail
                   show mpls ldp discovery detail
                   show mpls ldp discovery vrf <vrf>
                   show mpls ldp discovery vrf <vrf> detail
       """
    cli_command = ['show mpls ldp discovery',
                   'show mpls ldp discovery {all}',
                   'show mpls ldp discovery {detail}',
                   'show mpls ldp discovery {all} {detail}',
                   'show mpls ldp discovery vrf {vrf}',
                   'show mpls ldp discovery vrf {vrf} {detail}']

    def cli(self, all="", detail="", vrf="", output=None):
        if output is None:
            if vrf:
                if detail:
                    cmd = self.cli_command[5].format(vrf=vrf, detail=detail)
                else:
                    cmd = self.cli_command[4].format(vrf=vrf)
            else:
                if detail and all:
                    cmd = self.cli_command[3].format(all=all, detail=detail)
                if detail and not all:
                    cmd = self.cli_command[2].format(all=all, detail=detail)
                if not detail and all:
                    cmd = self.cli_command[1].format(all=all, detail=detail)
                else:
                    cmd = self.cli_command[0]

            out = self.device.execute(cmd)
        else:
            out = output

        if not vrf:
            vrf = "default"
        # initial return dictionary
        result_dict = {}
        discovery_flag = False
        targeted_flag = False

        # Local LDP Identifier:
        # VRF vpn1:Local LDP Identifier:
        # VRF vpn1: Local LDP Identifier:
        p1 = re.compile(r'^(VRF +(?P<vrf>\S+):)? *Local +LDP +Identifier:$')

        # 10.169.197.254:0
        p2 = re.compile(r'^(?P<local_ldp_identifier>[\d\.\:]+)$')
        # Discovery Sources:
        p2_1 = re.compile(r'^Discovery +Sources:$')

        #     GigabitEthernet0/0/0 (ldp): xmit/recv
        #     ATM1/1/0.1 (tdp):xmit/recv
        #     Ethernet3/0 (ldp): xmit
        #                (ldp): xmit/recv
        p3 = re.compile(r'^((?P<interface>\S+) +)?\((?P<session>[\w]+)\): *(?P<xmit>xmit)?\/?(?P<recv>recv)?$')

        #         Enabled: Interface config
        p4 = re.compile(r'^Enabled: +(?P<enabled>[\S\s]+)$')

        #         Hello interval: 5000 ms; Transport IP addr: 10.169.197.254
        p5 = re.compile(r'^Hello +interval: +(?P<hello_interval_ms>\d+) +ms;'
                        ' +Transport +IP +addr: (?P<transport_ip_address>[\d\.]+)$')

        #         LDP Id: 10.169.197.252:0
        p6 = re.compile(r'^(?P<ldp_tdp>\w+) +Id:(?P<space>\s{1,2})?(?P<ldp_tdp_id>[\d\.\:]+)$')

        #           Src IP addr: 10.169.197.93; Transport IP addr: 10.169.197.252
        p7 = re.compile(r'^Src +IP +addr: +(?P<source_ip_address>[\d\.]+);'
                        ' +Transport +IP +addr: +(?P<transport_ip_address>[\d\.]+)$')

        #           Hold time: 15 sec; Proposed local/peer: 15/15 sec
        p8 = re.compile(r'^Hold +time: +(?P<holdtime_sec>\d+) +sec; +Proposed +local\/peer:'
                        ' +(?P<proposed_local>\d+)\/(?P<proposed_peer>\d+) +sec$')

        #           Reachable via 10.169.197.252/32
        p9 = re.compile(r'^Reachable +via +(?P<reachable_via>[\d\.\/]+)$')

        #           Password: not required, none, in use
        p10 = re.compile(r'^Password: +(?P<password>[\S\s]+)$')

        #  Clients: IPv4, mLDP
        p11 = re.compile(r'^Clients: +(?P<clients>[\S\s]+)$')

        #  10.81.1.1 -> 172.16.94.33 (ldp): active, xmit/recv
        #  10.81.1.1 -> 172.16.25.16 (tdp): passive, xmit/recv
        #  10.131.191.252 -> 10.131.159.251 (ldp): active, xmit
        #  10.131.191.252 -> 10.131.159.252 (ldp): active/passive, xmit/recv
        p12 = re.compile(r'^(?P<source>[\d\.]+) +\-> +(?P<destination>[\d\.]+)'
                          ' +\((?P<session>(ldp|tdp)+)\): +(?P<status>(active|passive|active\/passive)+),'
                          ' +(?P<xmit>xmit)?\/?(?P<recv>recv)?$')

        # Targeted Hellos:
        p13 = re.compile(r'^Targeted +Hellos:$')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                if group['vrf']:
                    vrf = group['vrf']
                ldp_dict = result_dict.setdefault('vrf', {}).setdefault(vrf, {})
                continue

            #   10.169.197.254:0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                local_ldp_identifier_dict = ldp_dict.setdefault('local_ldp_identifier', {}). \
                    setdefault(group['local_ldp_identifier'], {})
                continue

            # Discovery Sources:
            m = p2_1.match(line)
            if m:
                discovery_flag = True
                targeted_flag = False
                continue

            # GigabitEthernet0/0/0 (ldp): xmit/recv
            m = p3.match(line)
            if m:
                group = m.groupdict()
                interface = group['interface'] if group['interface'] else "default"
                interface_dict = local_ldp_identifier_dict.setdefault('discovery_sources', {}) \
                    .setdefault('interfaces', {}) \
                    .setdefault(interface, {})
                interface_dict.update({'session': group['session']})
                interface_dict.update({'xmit': True if group['xmit'] else False})
                interface_dict.update({'recv': True if group['recv'] else False})
                continue

            # Enabled: Interface config
            m = p4.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({'enabled': group['enabled']})
                continue

            #  Hello interval: 5000 ms; Transport IP addr: 10.169.197.254
            m = p5.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({'hello_interval_ms': int(group['hello_interval_ms'])})
                interface_dict.update({'transport_ip_addr': group['transport_ip_address']})
                continue

            # LDP Id: 10.169.197.252:0
            m = p6.match(line)
            if m:
                group = m.groupdict()
                ldp_tdp = group['ldp_tdp'].lower()
                if discovery_flag:
                    ldp_dict = interface_dict.setdefault('{}_id'.format(ldp_tdp), {}).setdefault(
                        group['ldp_tdp_id'], {})

                if targeted_flag:
                    if targeted_dict:
                        targeted_dict.update({'{}_id'.format(ldp_tdp): group['ldp_tdp_id']})
                continue

            # Src IP addr: 10.169.197.93; Transport IP addr: 10.169.197.252
            m = p7.match(line)
            if m:
                group = m.groupdict()
                ldp_dict.update({k: v for k, v in group.items() if v})
                continue

            # Hold time: 15 sec; Proposed local/peer: 15/15 sec
            m = p8.match(line)
            if m:
                group = m.groupdict()
                ldp_dict.update({k: int(v) for k, v in group.items() if v})
                continue

            # Reachable via 10.169.197.252/32
            m = p9.match(line)
            if m:
                group = m.groupdict()
                ldp_dict.update({'reachable_via': group['reachable_via']})
                continue

            # Password: not required, none, in use
            m = p10.match(line)
            if m:
                group = m.groupdict()
                ldp_dict.update({'password': group['password']})
                continue

            # Clients: IPv4, mLDP
            m = p11.match(line)
            if m:
                group = m.groupdict()
                ldp_dict.update({'clients': group['clients']})
                continue

            # Targeted Hellos:
            m = p13.match(line)
            if m:
                discovery_flag = False
                targeted_flag = True
                continue

            #  10.81.1.1 -> 172.16.94.33 (ldp): active, xmit/recv
            #  10.81.1.1 -> 172.16.25.16 (tdp): passive, xmit/recv
            #  10.131.191.252 -> 10.131.159.251 (ldp): active, xmit
            #  10.131.191.252 -> 10.131.159.252 (ldp): active/passive, xmit/recv
            m = p12.match(line)
            if m:
                group = m.groupdict()
                targeted_dict = local_ldp_identifier_dict.setdefault('targeted_hellos', {}). \
                    setdefault(group['source'], {}). \
                    setdefault(group['destination'], {})
                targeted_dict.update({'session': group['session'].lower()})
                targeted_dict.update({'xmit': True if group['xmit'] else False})
                targeted_dict.update({'recv': True if group['recv'] else False})
                targeted_dict.update({'active': True if group['status'] == 'active' else False})
                continue
        return result_dict


# ================================================
#   Show mpls ldp igp sync
# ================================================
class ShowMplsLdpIgpSyncSchema(MetaParser):
    """
    Schema for show mpls ldp igp sync
               show mpls ldp igp sync all
               show mpls ldp igp sync interface <interface>
               show mpls ldp igp sync vrf <vrf>
    """
    schema = {
        'vrf': {
            Any(): {
                'interface': {
                    Any(): {
                        'ldp': {
                            'configured': bool,
                            'igp_synchronization_enabled': bool,
                        },
                        Optional('sync'): {
                            'status': {
                                Optional('enabled'): bool,
                                'sync_achieved': bool,
                                'peer_reachable': bool,
                            },
                            Optional('delay_time'): int,
                            Optional('left_time'): int,
                        },
                        Optional('igp'): {
                            'holddown_time': str,
                            'enabled': str
                        },
                        Optional('peer_ldp_ident'): str,
                    },
                },
            },
        }
    }

class ShowMplsLdpIgpSync(ShowMplsLdpIgpSyncSchema):
    """
        Parser for show mpls ldp igp sync
                   show mpls ldp igp sync all
                   show mpls ldp igp sync interface <interface>
                   show mpls ldp igp sync vrf <vrf>
       """
    cli_command = ['show mpls ldp igp sync',
                   'show mpls ldp igp sync {all}',
                   'show mpls ldp igp sync interface {interface}',
                   'show mpls ldp igp sync vrf {vrf}']

    def cli(self, vrf="", all="", interface="", output=None):
        if output is None:
            if vrf:
                cmd = self.cli_command[3].format(vrf=vrf)
            else:
                if all:
                    cmd = self.cli_command[1].format(all=all)
                if interface:
                    cmd = self.cli_command[2].format(interface=interface)
                if not interface and not all:
                    cmd = self.cli_command[0]

            out = self.device.execute(cmd)
        else:
            out = output

        if not vrf:
            vrf = "default"

        # initial return dictionary
        result_dict = {}

        # GigabitEthernet0/0/0:
        p1 = re.compile(r'^(?P<interface>\S+):$')

        #     LDP configured; LDP-IGP Synchronization enabled.
        #     LDP configured; LDP-IGP Synchronization not enabled.
        #     LDP configured;  SYNC enabled.
        #     LDP not configured; LDP-IGP Synchronization enabled.
        p2 = re.compile(r'^LDP +(?P<configured>[\w\s]+); +(LDP\-IGP +Synchronization '
                         '+(?P<state>[\w\s]+))?(SYNC +(?P<sync_enabled>[\w\s]+))?.$')

        #     Sync status: sync achieved; peer reachable.
        #     Sync status: sync not achieved; peer reachable.
        #     Sync status: sync not achieved; peer not reachable.
        p3 = re.compile(r'^(Sync|SYNC) +status: +sync +(?P<sync_status>[\w\s]+); +peer +(?P<reachable>[\w\s]+).$')

        #     Sync delay time: 0 seconds (0 seconds left)
        p4 = re.compile(r'^Sync +delay +time: +(?P<delay_time>\d+) +seconds \((?P<left_time>\d+) +seconds +left\)$')

        #     IGP holddown time: infinite.
        #     IGP holddown time: 1 milliseconds.
        p5 = re.compile(r'^IGP +holddown +time: +(?P<holddown_time>[\w\s]+).?$')

        #     Peer LDP Ident: 10.169.197.252:0
        p6 = re.compile(r'^Peer +LDP +Ident: +(?P<peer_ldp_ident>\S+).?$')

        #     IGP enabled: OSPF 65109
        p7 = re.compile(r'^IGP +enabled: +(?P<igp_enabled>[\S\s]+)$')

        for line in out.splitlines():
            line = line.strip()

            # GigabitEthernet0/0/0:
            m = p1.match(line)
            if m:
                group = m.groupdict()
                interface_dict = result_dict.setdefault('vrf', {}). \
                    setdefault(vrf, {}). \
                    setdefault('interface', {}). \
                    setdefault(group['interface'], {})
                continue

            # LDP configured; LDP-IGP Synchronization enabled.
            # LDP configured; LDP-IGP Synchronization not enabled.
            # LDP configured;  SYNC enabled.
            # LDP not configured; LDP-IGP Synchronization enabled.
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ldp_dict = interface_dict.setdefault('ldp', {})

                configured = group['configured']
                state = group['state']
                sync_enabled = group['sync_enabled']

                ldp_dict.update({'configured': True if configured == 'configured' else False})

                if state and state == 'enabled':
                    ldp_dict.update({'igp_synchronization_enabled': True})
                else:
                    ldp_dict.update({'igp_synchronization_enabled': False})

                if sync_enabled:
                    sync_status_dict = interface_dict.setdefault('sync', {}).setdefault('status', {})
                    sync_status_dict.update({'enabled': True if sync_enabled == 'enabled' else False})

                continue

            # Sync status: sync achieved; peer reachable.
            m = p3.match(line)
            if m:
                sync_dict = interface_dict.setdefault('sync', {})
                sync_status_dict = sync_dict.setdefault('status', {})
                sync_status = m.groupdict()['sync_status']
                reachable = m.groupdict()['reachable']
                sync_status_dict.update({'sync_achieved': True if sync_status == 'achieved' else False})
                sync_status_dict.update({'peer_reachable': True if reachable == 'reachable' else False})
                continue

            # Sync delay time: 0 seconds (0 seconds left)
            m = p4.match(line)
            if m:
                group = m.groupdict()
                sync_dict.update({'delay_time': int(group['delay_time'])})
                sync_dict.update({'left_time': int(group['left_time'])})
                continue

            # IGP holddown time: infinite.
            m = p5.match(line)
            if m:
                group = m.groupdict()
                igp_dict = interface_dict.setdefault('igp', {})
                igp_dict.update({'holddown_time': group['holddown_time']})
                continue

            # Peer LDP Ident: 10.169.197.252:0
            m = p6.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({'peer_ldp_ident': group['peer_ldp_ident']})
                continue

            # IGP enabled: OSPF 65109
            m = p7.match(line)
            if m:
                group = m.groupdict()
                igp_dict.update({'enabled': group['igp_enabled'].lower()})
                continue

        return result_dict


class ShowMplsForwardingTableSchema(MetaParser):
    """
    Schema for
        show mpls forwarding-table
        show mpls forwarding-table {prefix}
        show mpls forwarding-table vrf <vrf>
        show mpls forwarding-table detail
        show mpls forwarding-table interface tunnel <tunnelid>
        show mpls forwarding-table vrf <vrf> detail
        show mpls forwarding-table <prefix> <mask> algo <algo>
    """

    schema = {
        'vrf':{
            Any(): {
                'local_label': {
                    Any(): {
                        'outgoing_label_or_vc':{
                            Any():{
                                'prefix_or_tunnel_id':{
                                    Any(): {
                                        Optional('prefix_type'): str,
                                        Optional('prefix_no'): Any(),
                                        Optional('outgoing_interface'):{
                                            Any():{
                                                Optional('bytes_label_switched'): int,
                                                Optional('next_hop'): str,
                                                Optional('tsp_tunnel'): bool,
                                                Optional('merged'): bool,
                                                Optional('mac'): int,
                                                Optional('macstr'): str,
                                                Optional('lstack'): str,
                                                Optional('via'): str,
                                                Optional('encaps'): int,
                                                Optional('mru'): int,
                                                Optional('label_stack'): str,
                                                Optional('vpn_route'): str,
                                                Optional('output_feature_configured'): bool,
                                                Optional('load_sharing'): {
                                                    'method': str,
                                                    Optional('slots'): list,
                                                },
                                                Optional('broadcast'): bool,
                                                Optional('flexalgo_info'): {
                                                    'pdb_index': int,
                                                    'metric': int,
                                                    'algo': int,
                                                    'via_srms': int,
                                                },
                                            }
                                        }
                                    },
                                }
                            }
                        }
                    }
                }
            }
        }
    }

class ShowMplsForwardingTable(ShowMplsForwardingTableSchema):
    """
    Parser for
        show mpls forwarding-table
        show mpls forwarding-table {prefix}
        show mpls forwarding-table vrf {vrf}
        show mpls forwarding-table interface tunnel <tunnelid>
        show mpls forwarding-table <prefix> <mask> algo <algo>
        show mpls forwarding-table | sect <filter>
    """

    cli_command = ['show mpls forwarding-table vrf {vrf}',
                   'show mpls forwarding-table {prefix}',
                   'show mpls forwarding-table',
                   'show mpls forwarding-table interface tunnel {tunnelid}',
                   'show mpls forwarding-table {prefix} {mask} algo {algo}',
                   'show mpls forwarding-table | sect {filter}']

    def cli(self, vrf="", prefix="",tunnelid="", filter="", mask="", algo="", output=None):
        if output is None:
            if vrf:
                cmd = self.cli_command[0].format(vrf=vrf)
            elif prefix:
                cmd = self.cli_command[1].format(prefix=prefix)
            elif tunnelid:
                cmd = self.cli_command[3].format(tunnelid=tunnelid)
            elif prefix and mask and algo:
                cmd = self.cli_command[4].format(prefix=prefix, mask=mask, algo=algo)
            elif filter:
                cmd = self.cli_command[5].format(filter=filter)            
            else:
                cmd = self.cli_command[2]

            out = self.device.execute(cmd)
        else:
            out = output

        if not vrf:
            vrf = 'default'

        # initial return dictionary
        result_dict = {}

        # Local      Outgoing   Prefix           Bytes Label   Outgoing   Next Hop
        # Label      Label      or Tunnel Id     Switched      interface
        # 9301       No Label   172.16.100.1/32[V]   \
        #                                        0             Po1.51     192.168.10.253
        #            No Label   10.23.120.0/24[V]   \
        # None       No Label   10.0.0.16/30     0             Gi3        10.0.0.9
        # 39    [M]  16052      10.169.14.241/32   \
        # 235        211        10.55.0.0/24     0             Te0/2/0.102  192.168.4.1
        # 37         142409     172.16.100.1/32   \
        #                             0             Gi0/1/6    192.168.10.253
        #            107829     172.16.100.1/32   \
        #                             0             Gi0/1/7    192.168.10.254
        # 25         16021      0-23.23.23.23/32-4 (10:30:130:1)   \
        #                              0             Et0/2      13.1.1.2
        p1 = re.compile(r'^((?P<local_label>\d+|[Nn]one) +)?(?:\[(?P<info_tag>(?:T|M)+)\] +)?'
                        r'(?P<outgoing_label>(\w+|(No|Pop) +Label)) +(?P<prefix_or_tunnel_id>[\S]+) '
                        r'+\(?(?P<flexalgo_info>\d+:\d+:\d+:\d+)?\)?'
                        r'(?P<bytes_label_switched>\d*)( +(?P<interface>\S+))?( +(?P<next_hop>[\w\.]+))?$')

        #       [T]  16130      10.25.40.40/32   0             Tu1        point2point
        # 22    [M]  Pop Label  192.168.0.1/32   0             Gi2        192.168.0.2
        # 22    [T]  Pop Label  1/1[TE-Bind]     0             Tu1        point2point
        p2_1 = re.compile(r'^(?:(?P<local_label>\w+) +)?(?:\[(?P<info_tag>(?:T|M)+)\] +)?'
                           r'(?P<outgoing_label>(?:(?:A|a)ggregate|Untagged|(?:No|Pop) '
                           r'Label|(?:No|Pop) (?:T|t)ag|\d\/\w*|\d|\d\/)+)(?:\['
                           r'(?P<t1>(T)+)\] +)? +(?P<prefix_or_tunnel_id>[\w\(\)\:|\S]+) '
                           r'+\(?(?P<flexalgo_info>\d+:\d+:\d+:\d+)?\)?'
                           r' +(?P<bytes_label_switched>\d*)(?: +(?P<interface>\S+))?(?: +'
                           r'(?P<next_hop>[\w\.]+))?$')

        # 22    [T]  Pop Label  1/1[TE-Bind]     0             Tu1        point2point
        p2_2 = re.compile(r'^((?P<local_label>\w+) +)?(\[(?P<info_tag>(T)+)\] +)?'
                          r'(?P<outgoing_label>((A|a)ggregate|(No|Pop) Label|(No|Pop) tag|\d|\d\/)+)?'
                          r'(\[(?P<t1>(T)+)\] +)? +(?P<prefix_or_tunnel_id>[\w\.\[\]\-\s]+) '
                          r'+\(?(?P<flexalgo_info>\d+:\d+:\d+:\d+)?\)?'
                          r' +(?P<bytes_label_switched>\d+)( +(?P<interface>\S+))?( +(?P<next_hop>[\w\.]+))?$')
        
        #23    [T]  No Label   [mdt 3001:1 0][V]   \
        #                               200497062836  aggregate/vrf3001        
        p2_3 = re.compile(r'^((?P<local_label>\d+|[Nn]one)\s+)?(?:\[(?P<info_tag>(?:T|M)+)\]\s+)?'
                          r'(?P<outgoing_label>(\w+|(No|Pop) +Label))\s+\[(?P<prefix_type>\w+)\s+'
                          r'(?P<prefix_or_tunnel_id>\S+)\s+\(*(?P<prefix_no>[a-zA-Z0-9]+)\)*\]\[V\]\s+'
                          r'(?P<bytes_label_switched>\d*)(\s+(?P<interface>\S+))?(\s+(?P<next_hop>[\w\.]+))?$')

        #         MAC/Encaps=18/18, MRU=1530, Label Stack{}
        #         MAC/Encaps=18/18, MRU=1530, Label Stack{}, via Ls0
        #         MAC/Encaps=14/26, MRU=1492, Label Stack{16052 16062 16063}, via Gi0/1/7
        p3 = re.compile(r'^MAC\/Encaps=(?P<mac>\d+)\/(?P<encaps>\d+), +MRU=(?P<mru>[\d]+), '
                         '+Label +Stack{(?P<label_stack>.*)}(, via +(?P<via>\S+))?$')

        #         00002440156384B261CB1480810000330800
        #         AABBCC032800AABBCC0325018847 00010000
        #         0050568DA282BC16652F3A178847 03EB400003EBE00003EBF000
        p4 = re.compile(r'^(?P<code>[0-9A-F]+)( +(?P<lstack>\w+))?$')
        #         VPN route: L3VPN-0051
        p5 = re.compile(r'^VPN +route: +(?P<vpn_route>\S+)$')
        #         No output feature configured
        p6 = re.compile(r'^No +output +feature +configured$')
        #     Per-destination load-sharing, slots: 0 2 4 6 8 10 12 14
        p7 = re.compile(r'^(?P<method>\S+) +load\-sharing, +slots: +(?P<slots>[\d\s]+)$')
        #      Broadcast
        p8 = re.compile(r'^(B|b)roadcast$')

        partial_line = None
        local_label = "No Label"
        feature_dict = {}

        for line in out.splitlines():
            line = line.strip()
            line = line.replace('\t',' ')
            if '\\' in line:
                partial_line = line.replace('\\',' ')
                continue
            if partial_line is not None:
                line = partial_line + line
                partial_line = None

            # 9301       No Label   172.16.100.1/32[V]   \
            #                                       0             Po1.51     192.168.10.253
            outgoing_label = "No Label"
            prefix_or_tunnel_id = "None"
            m = p1.match(line)
            if m:
                group = m.groupdict()
                if group['local_label']:
                    local_label = group['local_label']
                    if local_label.isdigit():
                        local_label = int(local_label)
                outgoing_label = group['outgoing_label']
                prefix_or_tunnel_id = group['prefix_or_tunnel_id'].strip()

                base_feature_dict = result_dict.setdefault('vrf', {}).setdefault(vrf, {}). \
                                           setdefault('local_label', {}).\
                                           setdefault(local_label, {}).\
                                           setdefault('outgoing_label_or_vc', {}).\
                                           setdefault(outgoing_label.strip(), {}).\
                                           setdefault('prefix_or_tunnel_id', {}).\
                                           setdefault(prefix_or_tunnel_id,{})

                if group['interface']:
                    interface = Common.convert_intf_name(group['interface'])
                else:
                    interface = outgoing_label.strip()
                feature_dict = base_feature_dict.setdefault('outgoing_interface',{}).setdefault(interface, {})
                if group['next_hop']:
                    feature_dict.update({'next_hop': group['next_hop']})
                if group['info_tag']:
                    if 'T' in group['info_tag']:
                        feature_dict.update({'tsp_tunnel': True})
                    if 'M' in group['info_tag']:
                        feature_dict.update({'merged': True})
                if group['bytes_label_switched']:
                    feature_dict.update({'bytes_label_switched': int(group['bytes_label_switched'])})
                if group['flexalgo_info']:
                    pdb_index, metric, algo, via_srms = group['flexalgo_info'].split(':')
                    feature_dict.update({'flexalgo_info': {
                            'pdb_index': int(pdb_index),
                            'metric': int(metric),
                            'algo': int(algo),
                            'via_srms': int(via_srms),
                        }
                    })
                continue

            m = p2_1.match(line)
            if m:
                group = m.groupdict()
                if group['local_label']:
                    local_label = group['local_label']
                    if local_label.isdigit():
                        local_label = int(local_label)

                outgoing_label = group['outgoing_label']
                prefix_or_tunnel_id = group['prefix_or_tunnel_id'].strip()

                base_feature_dict = result_dict.setdefault('vrf', {}).setdefault(vrf, {}). \
                                           setdefault('local_label', {}). \
                                           setdefault(local_label, {}).\
                                           setdefault('outgoing_label_or_vc', {}).\
                                           setdefault(outgoing_label.strip(), {}). \
                                           setdefault('prefix_or_tunnel_id', {}). \
                                           setdefault(prefix_or_tunnel_id, {})

                if group['interface']:
                    interface = Common.convert_intf_name(group['interface'])
                else:
                    interface = outgoing_label.strip()

                feature_dict = base_feature_dict.setdefault('outgoing_interface', {}).setdefault(interface, {})
                if group['next_hop']:
                    feature_dict.update({'next_hop': group['next_hop']})
                if group['info_tag']:
                    if 'T' in group['info_tag']:
                        feature_dict.update({'tsp_tunnel': True})
                    if 'M' in group['info_tag']:
                        feature_dict.update({'merged': True})
                if group['t1']:
                    feature_dict.update({'tsp_tunnel': True})
                if group['bytes_label_switched']:
                    feature_dict.update({'bytes_label_switched': int(group['bytes_label_switched'])})
                if group['flexalgo_info']:
                    pdb_index, metric, algo, via_srms = group['flexalgo_info'].split(':')
                    feature_dict.update({'flexalgo_info': {
                            'pdb_index': int(pdb_index),
                            'metric': int(metric),
                            'algo': int(algo),
                            'via_srms': int(via_srms),
                        }
                    })
                continue

            m = p2_2.match(line)
            if m:
                group = m.groupdict()
                if group['local_label']:
                    local_label = group['local_label']
                    if local_label.isdigit():
                        local_label = int(local_label)

                outgoing_label = group['outgoing_label']
                prefix_or_tunnel_id = group['prefix_or_tunnel_id'].strip()

                base_feature_dict = result_dict.setdefault('vrf', {}).setdefault(vrf, {}). \
                                           setdefault('local_label', {}). \
                                           setdefault(local_label, {}). \
                                           setdefault('outgoing_label_or_vc', {}). \
                                           setdefault(outgoing_label.strip(), {}). \
                                           setdefault('prefix_or_tunnel_id', {}). \
                                           setdefault(prefix_or_tunnel_id, {})

                if group['interface']:
                    interface = Common.convert_intf_name(group['interface'])
                else:
                    interface = outgoing_label.strip()
                feature_dict = base_feature_dict.setdefault('outgoing_interface', {}).setdefault(interface, {})
                if group['next_hop']:
                    feature_dict.update({'next_hop': group['next_hop']})
                if group['info_tag']:
                    if 'T' in group['info_tag']:
                        feature_dict.update({'tsp_tunnel': True})
                    if 'M' in group['info_tag']:
                        feature_dict.update({'merged': True})
                if group['t1']:
                    feature_dict.update({'tsp_tunnel': True})
                if group['bytes_label_switched']:
                    feature_dict.update({'bytes_label_switched': int(group['bytes_label_switched'])})
                if group['flexalgo_info']:
                    pdb_index, metric, algo, via_srms = group['flexalgo_info'].split(':')
                    feature_dict.update({'flexalgo_info': {
                            'pdb_index': int(pdb_index),
                            'metric': int(metric),
                            'algo': int(algo),
                            'via_srms': int(via_srms),
                        }
                    })
                continue

            #23    [T]  No Label   [mdt 3001:1 0][V]   \
            #                               200497062836  aggregate/vrf3001            
            m = p2_3.match(line)
            if m:
                group = m.groupdict()
                if group['local_label']:
                    local_label = group['local_label']
                    if local_label.isdigit():
                        local_label = int(local_label)

                outgoing_label = group['outgoing_label']
                prefix_or_tunnel_id = group['prefix_or_tunnel_id']

                base_feature_dict = result_dict.setdefault('vrf', {}).setdefault(vrf, {}). \
                                           setdefault('local_label', {}). \
                                           setdefault(local_label, {}). \
                                           setdefault('outgoing_label_or_vc', {}). \
                                           setdefault(outgoing_label, {}). \
                                           setdefault('prefix_or_tunnel_id', {}). \
                                           setdefault(prefix_or_tunnel_id, {})

                if group['interface']:
                    interface = Common.convert_intf_name(group['interface'])
                else:
                    interface = outgoing_label
                prefix_no = int(group['prefix_no']) if group['prefix_no'].isdigit() else group['prefix_no']
                base_feature_dict.update({
                    'prefix_type': group['prefix_type'],
                    'prefix_no': prefix_no
                })
                feature_dict = base_feature_dict.setdefault('outgoing_interface', {}).setdefault(interface, {})
                if group['next_hop']:
                    feature_dict.update({'next_hop': group['next_hop']})
                if group['bytes_label_switched']:
                    feature_dict.update({'bytes_label_switched': int(group['bytes_label_switched'])})
                continue
                
            #     MAC/Encaps=18/18, MRU=1530, Label Stack{}
            m = p3.match(line)
            if m:
                group = m.groupdict()
                feature_dict.update({'mac': int(group['mac'])})
                feature_dict.update({'encaps': int(group['encaps'])})
                feature_dict.update({'mru': int(group['mru'])})
                feature_dict.update({'label_stack': group['label_stack']})
                if group['via']:
                    feature_dict.update({'via': Common.convert_intf_name(group['via'])})

                continue

            #     00002440156384B261CB1480810000330800
            m = p4.match(line)
            if m:
                group = m.groupdict()
                feature_dict.update({'macstr': group['code']})
                if group['lstack']:
                    feature_dict.update({'lstack': group['lstack']})
                continue

            #     VPN route: L3VPN-0051
            m = p5.match(line)
            if m:
                group = m.groupdict()
                feature_dict.update({'vpn_route': group['vpn_route']})
                continue

            #     No output feature configured
            m = p6.match(line)
            if m:
                feature_dict.update({'output_feature_configured': False})
                continue

            #    Per-destination load-sharing, slots: 0 2 4 6 8 10 12 14
            m = p7.match(line)
            if m:
                group = m.groupdict()
                load_dict = feature_dict.setdefault('load_sharing', {})
                load_dict.update({'method': group['method'].lower()})
                load_dict.update({'slots': group['slots'].split()})
                continue

            #   Broadcast
            m = p8.match(line)
            if m:
                feature_dict.update({'broadcast': True})
                continue

        return result_dict

class ShowMplsForwardingTableDetail(ShowMplsForwardingTable):
    """Parser for
        show mpls forwarding-table detail
        show mpls forwarding-table vrf <vrf> detail
        show mpls forwarding-table labels {label} detail
        show mpls forwarding-table {route} detail"""

    cli_command = ['show mpls forwarding-table detail',
                   'show mpls forwarding-table vrf {vrf} detail',
                   'show mpls forwarding-table labels {label} detail',
                   'show mpls forwarding-table {route} detail']

    def cli(self, vrf='', label='', route='', output=None):
        if output is None:
            if vrf:
                cmd = self.cli_command[1].format(vrf=vrf)
            elif label:
                cmd = self.cli_command[2].format(label=label)
            elif route:
                cmd = self.cli_command[3].format(route=route)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        return super().cli(vrf=vrf ,output=out)


class ShowMplsInterfaceSchema(MetaParser):
    """Schema for
        show mpls interfaces
        show mpls interfaces all
        show mpls interfaces vrf <vrf>
        show mpls interfaces <interface>
        show mpls interfaces <interface> detail
        show mpls interfaces detail"""

    schema = {
        'vrf':{
            Any():{
                'interfaces': {
                    Any(): {
                        Optional('ip'): str,
                        Optional('tunnel'): str,
                        Optional('bgp'): str,
                        Optional('static'): str,
                        Optional('operational'): str,
                        Optional('type'): str,
                        Optional('session'): str,
                        Optional('ip_labeling_enabled'):{
                            Any():{
                                'ldp': bool,
                                Optional('interface_config'): bool,
                            }
                        },
                        Optional('lsp_tunnel_labeling_enabled'): bool,
                        Optional('lp_frr_labeling_enabled'): bool,
                        Optional('bgp_labeling_enabled'): bool,
                        Optional('mpls_operational'): bool,
                        Optional('mtu'): int,
                    }
                }
            }
        }
    }


class ShowMplsInterface(ShowMplsInterfaceSchema):
    """Parser for
        show mpls interfaces
        show mpls interfaces all
        show mpls interfaces vrf <vrf>
        show mpls interfaces <interface>
        show mpls interfaces <interface> detail
        show mpls interfaces detail"""

    cli_command = ['show mpls interfaces',
                   'show mpls interfaces detail',
                   'show mpls interfaces {interface} detail',
                   'show mpls interfaces {interface}',
                   'show mpls interfaces {all}',
                   'show mpls interfaces vrf {vrf}']

    def cli(self, detail="", interface="",vrf="",all="", output=None):
        if output is None:
            if detail:
                if interface:
                    cmd = self.cli_command[2].format(interface=interface)
                else:
                    cmd = self.cli_command[1]
            else:
                if interface and not vrf:
                    cmd = self.cli_command[3].format(interface=interface)
                if not interface and not vrf:
                    cmd = self.cli_command[0]
                if vrf and not interface:
                    cmd = self.cli_command[5].format(vrf=vrf)
                if all:
                    cmd = self.cli_command[4].format(all=all)

            out = self.device.execute(cmd)
        else:
            out = output

        if not vrf:
            vrf = 'default'

        # initial return dictionary
        result_dict = {}

        # vrf vpn1:
        p0 = re.compile(r'^VRF +(?P<vrf>\S+):$')
        # Interface              IP            Tunnel   BGP Static Operational
        # GigabitEthernet6       Yes (ldp)     No       No  No     Yes
        # Interface              IP            Tunnel   Operational
        # GigabitEthernet6/0     Yes (ldp)     No       Yes
        p1 = re.compile(r'^(?P<interface>(?!Interface)[\S]+) +(?P<ip>((Y|y)es|(N|n)o)+)( +\((?P<session>\w+)\))? +(?P<tunnel>\w+)'
                        '( +(?P<bgp>\w+) +(?P<static>\w+))? +(?P<operational>\w+)$')
        # Interface GigabitEthernet0/0/0:
        p2 = re.compile(r'^Interface +(?P<interface>\S+):$')
        #     Type Unknown
        p3 = re.compile(r'^Type +(?P<type>\w+)$')
        #     IP labeling enabled (ldp) :
        p4 = re.compile(r'^IP +labeling +enabled \(+(?P<session>\w+)\)( +\:)?$')
        #       Interface config
        p5 = re.compile(r'^Interface +config$')
        #     LSP Tunnel labeling not enabled
        p6 = re.compile(r'^LSP +Tunnel +labeling +((?P<lsp_tunnel_enabled>\w+) )?enabled$')
        #     IP FRR labeling not enabled
        p7 = re.compile(r'^IP +FRR +labeling +((?P<lp_frr_labeling>\w+) )?enabled$')
        #     BGP labeling not enabled
        p8 = re.compile(r'^BGP +labeling +((?P<bgp_labeling>\w+) )?enabled$')
        #     MPLS operational
        #     MPLS not operational
        p9 = re.compile(r'^MPLS +(?P<mpls_status>[\w\s]+)$')
        #     MTU = 1552
        p10 = re.compile(r'^MTU \= +(?P<mtu>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            # vrf vpn1:
            m = p0.match(line)
            if m:
                group = m.groupdict()
                vrf = group['vrf']
                continue

            # Interface              IP            Tunnel   BGP Static Operational
            # GigabitEthernet6       Yes (ldp)     No       No  No     Yes
            m = p1.match(line)
            if m:
                group = m.groupdict()
                interface_dict_1 = result_dict.setdefault('vrf', {}).\
                                             setdefault(vrf, {}).\
                                             setdefault('interfaces', {}).\
                                             setdefault(group['interface'], {})
                interface_dict_1.update({'ip': group['ip'].lower()})
                interface_dict_1.update({'tunnel': group['tunnel'].lower()})
                if group['bgp']:
                    interface_dict_1.update({'bgp': group['bgp'].lower()})
                if group['static']:
                    interface_dict_1.update({'static': group['static'].lower()})
                if group['session']:
                    interface_dict_1.update({'session': group['session']})
                interface_dict_1.update({'operational': group['operational'].lower()})
                continue

            # Interface GigabitEthernet0/0/0:
            m = p2.match(line)
            if m:
                group = m.groupdict()
                interface_dict = result_dict.setdefault('vrf', {}).\
                                             setdefault(vrf, {}).\
                                             setdefault('interfaces', {}).setdefault(group['interface'], {})
                continue

            #    Type Unknown
            m = p3.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({'type': group['type']})
                continue

            #     IP labeling enabled (ldp) :
            m = p4.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({'session': group['session']})
                labeling_dict = interface_dict.setdefault('ip_labeling_enabled',{}).setdefault(True, {})
                labeling_dict.update({'ldp': True})
                continue

            #     Interface config
            m = p5.match(line)
            if m:
                labeling_dict.update({'interface_config': True})
                continue

            #     LSP Tunnel labeling not enabled
            m = p6.match(line)
            if m:
                group = m.groupdict()
                if group['lsp_tunnel_enabled'] and 'not' in group['lsp_tunnel_enabled']:
                    flag = False
                else:
                    flag = True
                interface_dict.update({'lsp_tunnel_labeling_enabled': flag})
                continue

            # IP FRR labeling not enabled
            m = p7.match(line)
            if m:
                group = m.groupdict()
                if group['lp_frr_labeling'] and 'not' in group['lp_frr_labeling']:
                    flag = False
                else:
                    flag = True
                interface_dict.update({'lp_frr_labeling_enabled': flag})
                continue

            #     BGP labeling not enabled
            m = p8.match(line)
            if m:
                group = m.groupdict()
                if group['bgp_labeling'] and 'not' in group['bgp_labeling']:
                    flag = False
                else:
                    flag = True
                interface_dict.update({'bgp_labeling_enabled': flag})
                continue

            #     MPLS operational
            m = p9.match(line)
            if m:
                group = m.groupdict()
                if 'not' in group['mpls_status']:
                    mpls_flag = False
                else:
                    mpls_flag = True
                interface_dict.update({'mpls_operational': mpls_flag})
                continue

            #     MTU = 1552
            m = p10.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({'mtu': int(group['mtu'])})
                continue

        return result_dict

# ================================================
#   Show mpls l2transport vc
# ================================================
class ShowMplsL2TransportSchema(MetaParser):
    """
    Schema for show mpls l2transport vc
               show mpls l2transport vc <vc_id>
               show mpls l2transport vc detail
               show mpls l2transport vc <vc_id> detail
    """

    schema = {
        'interface': {
            Any(): {
                Optional('status'): str,
                Optional('state'): str,
                Optional('destination_address'): {
                    Any():{
                        'vc_id': {
                            Any() : {
                                Optional('local_circuit'): str,
                                'vc_status': str,
                            },
                        },
                        Optional('tunnel_label'): str,
                        Optional('next_hop'): str,
                        Optional('output_interface'): str,
                        Optional('imposed_label_stack'): str,
                        Optional('default_path'): str,
                        Optional('preferred_path'): str,
                        Optional('preferred_path_state'): str,
                    },
                },
                Optional('line_protocol_status'): str,
                Optional('ethernet_vlan'): {
                    Any(): {
                        'status': str,
                    },
                },
                Optional('protocol_status'): {
                    Any(): str,
                },
                Optional('create_time'): str,
                Optional('last_status_change_time'): str,
                Optional('signaling_protocol'): {
                    Any(): {
                        'mpls_vc_labels': {
                            'local': str,
                            'remote': str,
                        },
                        'group_id': {
                            'local': str,
                            'remote': str,
                        },
                        'mtu': {
                            'local': str,
                            'remote': str,
                        },
                        Optional('mac_withdraw'): {
                            'sent': int,
                            'received': int,
                        },
                        Optional('remote_interface_description'): str,
                        Optional('peer_id'): str,
                        Optional('peer_state'): str,
                        Optional('id'): str,
                        Optional('status'): str,
                        Optional('targeted_hello_ip'): str,
                    },
                },
                Optional('sequencing'): {
                    'received': str,
                    'sent': str,
                },
                Optional('statistics'): {
                    Optional('packets'): {
                        'received': int,
                        'sent': int,
                    },
                    Optional('bytes'): {
                        'received': int,
                        'sent': int,
                    },
                    Optional('packets_drop'): {
                        'received': int,
                        Optional('seq_error'): int,
                        'sent': int,
                    },
                },
                Optional('last_label_fsm_state_change_time') : str,
                Optional('graceful_restart') : str,
                Optional('non_stop_routing'): str,
                Optional('status_tlv_support') : str,
                Optional('ldp_route_enabled'): str,
                Optional('last_status_name'): {
                    Any(): {
                        Optional('received'): str,
                        Optional('sent'): str
                    },
                },
                Optional('label_state_machine'): str,
            },
        }
    }


class ShowMplsL2TransportDetail(ShowMplsL2TransportSchema):
    """
    Parser for show mpls l2transport vc detail
    """
    cli_command = ['show mpls l2transport vc detail',
                   'show mpls l2transport vc {vc_id} detail'
                   ]

    def cli(self, vc_id="", output=None):
        if output is None:
            if not vc_id:
                out = self.device.execute(self.cli_command[0])
            else:
                out = self.device.execute(self.cli_command[1].format(vc_id=vc_id))
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # Local interface: VFI PE1-VPLS-A up
        # Local interface: Fa2/1/1.2 up, line protocol up, Eth VLAN 2 up
        p1 = re.compile(r'^Local +interface: +(?P<interface>[\w\d\/\.\s\-]+)'
                         ' +(?P<state>\w+)(, line +protocol +(?P<line_protocol_status>\w+),'
                         ' Eth +VLAN +(?P<number>\d+) +(?P<status>\w+))?$')

        # Local interface: Se0/1/0:0 up, line protocol up, HDLC up
        p1_1 = re.compile(r'^Local +interface: +(?P<interface>[\w\W]+) +(?P<state>\w+), +line +protocol +(?P<line_protocol_status>\w+), +(?P<protocol>\w+) +(?P<status>\w+)$')

        #   Destination address: 10.2.2.2, VC ID: 1002, VC status: recovering
        p2 = re.compile(r'^Destination +address: +(?P<address>[\d\.]+),'
                         ' +VC +ID: +(?P<vc_id>\d+), +VC +status: +(?P<vc_status>\w+)$')

        #   Preferred path: not configured
        p3 = re.compile(r'^Preferred +path: +(?P<preferred_path>[a-zA-Z0-9 ]+)(?:\,\s+(?P<state>\S+)$)?$')

        #   Default path: active
        p4 = re.compile(r'^Default +path: +(?P<default_path>[\S\s]+)$')

        #   Tunnel label: imp-null, next hop point2point
        p5 = re.compile(r'^Tunnel +label: +(?P<tunnel_label>\S+),'
                         ' +next +hop +(?P<next_hop>[\S\s]+)$')

        #   Next hop: point2point
        p5_1 = re.compile(r'^Next +hop: +(?P<next_hop>[\S\s]+)$')

        #   Output interface: Se2/0/2, imposed label stack {16}
        #   Output interface: Et0/1, imposed label stack {24 21}
        p6 = re.compile(r'^Output +interface: +(?P<output_interface>\S+),'
                         ' +imposed +label +stack +(?P<imposed_label_stack>[^}]+})')

        #   Create time: 1d00h, last status change time: 00:00:03
        p7 = re.compile(r'^Create +time: +(?P<create_time>\S+),'
                         ' +last +status +change +time: +(?P<last_status_change_time>\S+)$')

        #   Signaling protocol: LDP, peer 10.2.2.2:0 down
        #   Signaling protocol: LDP, peer unknown
        p8 = re.compile(r'^Signaling +protocol: +(?P<signaling_protocol>\S+)(,'
                         ' +peer +(?P<peer_id>\S+)( +(?P<peer_state>\w+))?)?$')

        #   MPLS VC labels: local 21, remote 16
        #   MPLS VC labels: local 21, remote unassigned
        p9 = re.compile(r'^MPLS +VC +labels: +local +(?P<mpls_local>\w+),'
                         ' +remote +(?P<mpls_remote>\w+)$')

        #   Group ID: local 0, remote 0
        #   Group ID: local 0, remote unknown
        p10 = re.compile(r'^Group +ID: +local +(?P<group_id_local>[\w\W]+),'
                          ' +remote +(?P<group_id_remote>[\w\W]+)$')

        #   MTU: local 1500, remote 1500
        p11 = re.compile(r'^MTU: +local +(?P<mtu_local>\w+),'
                          ' +remote +(?P<mtu_remote>\w+)$')

        #   Remote interface description: "xconnect to PE2"
        p12 = re.compile(r'^Remote +interface +description:'
                          ' \"+(?P<remote_interface_description>[\S\s]+)\"$')

        # Targeted Hello: 10.1.1.4(LDP Id) -> 10.1.1.1, LDP is UP
        # Targeted Hello: 10.1.1.1(LDP Id) -> 10.1.1.1
        p12_1 = re.compile(r'^Targeted +Hello: +(?P<targeted_hello_ip>\S+)\([A-Z]+ +Id\)'
                            ' +\-\> +(?P<id>[\d\.]+)(,'
                            ' +[A-Z]+ +is +(?P<status>\S+))?$')

        # MAC Withdraw: sent 5, received 3
        p12_2 = re.compile(r'^MAC Withdraw: +sent +(?P<sent>\d+),'
                            ' +received +(?P<received>\d+)$')

        #   Sequencing: receive disabled, send disabled
        p13 = re.compile(r'^Sequencing: +receive +(?P<receive>\S+),'
                          ' +send +(?P<send>\S+)$')

        #   VC statistics:
        p14 = re.compile(r'^VC +statistics:$')

        #   packet totals: receive 20040, send 28879
        p15 = re.compile(r'^(transit +)?packet +totals: +receive'
                          ' +(?P<pkts_receive>\d+), +send +(?P<pkts_send>\d+)$')

        #   byte totals:   receive 25073016, send 25992388
        p16 = re.compile(r'^(transit +)?byte +totals: +receive'
                          ' +(?P<byte_receive>\d+), +send +(?P<byte_send>\d+)$')

        #   transit packet drops:  receive 0, seq error 0, send 0
        p17 = re.compile(r'^(transit +)?packet +drops: +receive'
                          ' +(?P<pkts_drop_receive>\d+), +send +(?P<pkts_drop_send>\d+)$')

        #   packet drops:  receive 0, send 0
        p17_1 = re.compile(r'^(transit +)?packet +drops: +receive +(?P<pkts_drop_receive>\d+), +seq +error +(?P<seq_error>\d+), +send +(?P<pkts_drop_send>\d+)')


        #  Se5/0          FR DLCI 55         10.0.0.1        55         UP
        p18 = re.compile(r'^\s*(?P<local_intf>[\w\W]{0,13}) +(?P<local_circuit>' \
            '[\w\W]{0,26}) +(?P<dest_address>[\d\.]+) +(?P<vc_id>\d+) +' \
            '(?P<vc_status>\S+)')

        # Last label FSM state change time: 00:00:19
        p19 = re.compile(r'^\s*Last +label +FSM +state +change +time: +(?P<last_label_fsm_state_change_time>\d+:\d+:\d+)$')

        # Graceful restart: configured and enabled
        p20 = re.compile(r'^\s*Graceful +restart: +(?P<graceful_restart>[\w\W]+)$')

        # Non stop routing: not configured and not enabled
        p21 = re.compile(r'^\s*Non +stop +routing: +(?P<non_stop_routing>[\w\W]+)$')

        # Status TLV support (local/remote) : enabled/supported
        p22 = re.compile(r'^\s*Status +TLV +support +\(local\/remote\) +: +(?P<status_tlv_support>[\w\W]+)$')

        # LDP route watch : enabled
        p23 = re.compile(r'^\s*LDP +route +watch +: +(?P<ldp_route_enabled>[\w\W]+)$')

        # Last local PW i/f circ status rcvd: No fault
        p24 = re.compile(r'^\s*Last +(?P<last_status_name>[\w\W]+) +status +(rcvd): (?P<received>[\w\W]+)$')

        # Last local AC circuit status sent: No fault
        p25 = re.compile(r'^\s*Last +(?P<last_status_name>[\w\W]+) +status +(sent): (?P<sent>[\w\W]+)$')

        # Label/status state machine : established, LruRru
        p26 = re.compile(r'^\s*Label\/status +state +machine +: +(?P<label_state_machine>[\w\W]+)$')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                interface = Common.convert_intf_name(group['interface'])
                final_dict = ret_dict.setdefault('interface', {}).\
                    setdefault(interface, {})
                final_dict['status'] = group['state']
                if group['line_protocol_status']:
                    final_dict['line_protocol_status'] = group['line_protocol_status']
                if group['number'] and group['status']:
                    ether_number = int(group['number'])
                    final_dict.setdefault('ethernet_vlan', {}).\
                        setdefault(ether_number, {})
                    final_dict['ethernet_vlan'][ether_number]['status'] = \
                        group['status']
                continue

            m = p1_1.match(line)
            if m:
                group = m.groupdict()
                interface = Common.convert_intf_name(group['interface'])
                final_dict = ret_dict.setdefault('interface', {}).\
                    setdefault(interface, {})
                final_dict['state'] = group['state']
                final_dict['line_protocol_status'] = group['line_protocol_status']
                protocol = final_dict.setdefault('protocol_status', {})
                protocol.update({group['protocol'] : group['status']})
                continue


            m = p2.match(line)
            if m:
                group = m.groupdict()
                destination_address = group['address']
                new_final_dict = final_dict.setdefault('destination_address', {}).\
                    setdefault(destination_address, {})
                vc_id_dict = new_final_dict.setdefault('vc_id', {}). \
                    setdefault(group['vc_id'], {})
                vc_id_dict.update({'vc_status' : group['vc_status']})
                continue

            m = p3.match(line)
            if m:
                group = m.groupdict()
                new_final_dict['preferred_path'] = group['preferred_path']
                if group.get('state'):
                    new_final_dict['preferred_path_state'] = group['state']
                continue

            m = p4.match(line)
            if m:
                group = m.groupdict()
                new_final_dict['default_path'] = group['default_path']
                continue

            m = p5.match(line)
            if m:
                group = m.groupdict()
                new_final_dict.update({k:v for k, v in group.items()})
                continue

            m = p5_1.match(line)
            if m:
                group = m.groupdict()
                new_final_dict.update({k:v for k, v in group.items()})
                continue

            m = p6.match(line)
            if m:
                group = m.groupdict()
                new_final_dict['output_interface'] = Common.convert_intf_name(
                    group['output_interface'])
                new_final_dict['imposed_label_stack'] = group['imposed_label_stack']
                continue

            m = p7.match(line)
            if m:
                group = m.groupdict()
                final_dict.update({k:v for k, v in group.items()})
                continue

            m = p8.match(line)
            if m:
                group = m.groupdict()
                signaling_protocol = group['signaling_protocol']
                signaling_final_dict = final_dict.setdefault('signaling_protocol', {}).\
                    setdefault(signaling_protocol, {})
                if group['peer_id']:
                    signaling_final_dict['peer_id'] = group['peer_id']
                if group['peer_state']:
                    signaling_final_dict['peer_state'] = group['peer_state']
                continue

            m = p9.match(line)
            if m:
                group = m.groupdict()
                signaling_final_dict.setdefault('mpls_vc_labels', {})
                signaling_final_dict['mpls_vc_labels']['local'] = \
                    group['mpls_local']
                signaling_final_dict['mpls_vc_labels']['remote'] = \
                    group['mpls_remote']
                continue

            m = p10.match(line)
            if m:
                group = m.groupdict()
                signaling_final_dict.setdefault('group_id', {})
                signaling_final_dict['group_id']['local'] = group['group_id_local']
                signaling_final_dict['group_id']['remote'] = group['group_id_remote']
                continue

            m = p11.match(line)
            if m:
                group = m.groupdict()
                signaling_final_dict.setdefault('mtu', {})
                signaling_final_dict['mtu']['local'] = group['mtu_local']
                signaling_final_dict['mtu']['remote'] = group['mtu_remote']
                continue

            m = p12.match(line)
            if m:
                group = m.groupdict()
                signaling_final_dict['remote_interface_description'] = \
                    group['remote_interface_description']
                continue

            m = p12_1.match(line)
            if m:
                group = m.groupdict()
                signaling_final_dict['targeted_hello_ip'] = \
                    group['targeted_hello_ip']
                signaling_final_dict['id'] = group['id']
                if group['status']:
                    signaling_final_dict['status'] = group['status']
                continue

            m = p12_2.match(line)
            if m:
                group = m.groupdict()
                signaling_final_dict.setdefault('mac_withdraw', {})
                signaling_final_dict['mac_withdraw']['sent'] = \
                    int(group['sent'])
                signaling_final_dict['mac_withdraw']['received'] = \
                    int(group['received'])
                continue

            m = p13.match(line)
            if m:
                group = m.groupdict()
                final_dict.setdefault('sequencing', {})
                final_dict['sequencing']['received'] = group['receive']
                final_dict['sequencing']['sent'] = group['send']
                continue

            m = p14.match(line)
            if m:
                group = m.groupdict()
                statistics_final_dict = final_dict.setdefault('statistics', {})
                continue

            m = p15.match(line)
            if m:
                group = m.groupdict()
                statistics_final_dict.setdefault('packets', {})
                statistics_final_dict['packets']['received'] = int(group['pkts_receive'])
                statistics_final_dict['packets']['sent'] = int(group['pkts_send'])
                continue

            m = p16.match(line)
            if m:
                group = m.groupdict()
                statistics_final_dict.setdefault('bytes', {})
                statistics_final_dict['bytes']['received'] = int(group['byte_receive'])
                statistics_final_dict['bytes']['sent'] = int(group['byte_send'])
                continue

            m = p17.match(line)
            if m:
                group = m.groupdict()
                statistics_final_dict.setdefault('packets_drop', {})
                statistics_final_dict['packets_drop']['received'] = int(group['pkts_drop_receive'])
                statistics_final_dict['packets_drop']['sent'] = int(group['pkts_drop_send'])
                continue

            m = p17_1.match(line)
            if m:
                group = m.groupdict()
                statistics_final_dict.setdefault('packets_drop', {})
                statistics_final_dict['packets_drop']['received'] = int(group['pkts_drop_receive'])
                statistics_final_dict['packets_drop']['seq_error'] = int(group['seq_error'])
                statistics_final_dict['packets_drop']['sent'] = int(group['pkts_drop_send'])
                continue

            m = p18.match(line)
            if m:
                group = m.groupdict()
                local_interface = ret_dict.setdefault('interface', {}). \
                    setdefault(Common.convert_intf_name( \
                        group['local_intf'].strip()), {})


                dest_address = local_interface.setdefault( \
                    'destination_address', {}). \
                    setdefault(group['dest_address'], {})

                vc_id_dict = dest_address.setdefault('vc_id', {}). \
                    setdefault(group['vc_id'], {})
                vc_id_dict.update({'vc_status' : group['vc_status']})

                vc_id_dict.update({'local_circuit' : \
                    group['local_circuit'].strip()})
                continue

            m = p19.match(line)
            if m:
                group = m.groupdict()
                final_dict.update({k:v for k, v in group.items()})
                continue

            m = p20.match(line)
            if m:
                group = m.groupdict()
                final_dict.update({k:v for k, v in group.items()})
                continue

            m = p21.match(line)
            if m:
                group = m.groupdict()
                final_dict.update({k:v for k, v in group.items()})
                continue

            m = p22.match(line)
            if m:
                group = m.groupdict()
                final_dict.update({k:v for k, v in group.items()})
                continue

            m = p23.match(line)
            if m:
                group = m.groupdict()
                final_dict.update({k:v for k, v in group.items()})
                continue

            m = p24.match(line)
            if m:
                group = m.groupdict()
                key = group['last_status_name'].strip().replace(' ', '_'). \
                        replace('/', '').lower()
                last_status_name = final_dict.setdefault('last_status_name', {}). \
                    setdefault(key, {})
                last_status_name.update({'received': group['received']})
                continue

            m = p25.match(line)
            if m:
                group = m.groupdict()
                key = group['last_status_name'].strip().replace(' ', '_'). \
                        replace('/', '').lower()
                last_status_name = final_dict.setdefault('last_status_name', {}) .\
                    setdefault(key, {})
                last_status_name.update({'sent': group['sent']})
                continue

            m = p26.match(line)
            if m:
                group = m.groupdict()
                final_dict.update({k:v for k, v in group.items()})
                continue
        return ret_dict

class ShowMplsL2TransportVC(ShowMplsL2TransportDetail):
    """
    Parser for show mpls l2transport vc
    """
    cli_command = 'show mpls l2transport vc'

    def cli(self, output=None):
        if not output:
            output=self.device.execute(self.cli_command)
        else:
            output=output
        return super().cli(output=output)

class ShowMplsL2TransportVC_VC_Id(ShowMplsL2TransportDetail):
    """
    Parser for show mpls l2transport vc vc_id
    """
    cli_command = 'show mpls l2transport vc {vc_id}'

    def cli(self, vc_id,output=None):
        if not output:
            output=self.device.execute(self.cli_command.format(vc_id=vc_id))
        else:
            output=output
        return super().cli(output=output)

class ShowMplsL2TransportDetail_VC_Statistics_Schema(MetaParser):
    """Schema for show mpls l2 vc <vc_id> detail | sect VC Statistics"""

    schema = {
        'statistics': {
            Optional('packets'): {
                'received': int,
                'sent': int,
            },
            Optional('bytes'): {
                'received': int,
                'sent': int,
            },
            Optional('packets_drop'): {
                'received': int,
                Optional('seq_error'): int,
                'sent': int,
            },
        },

    }

class ShowMplsL2TransportDetail_VC_Statistics(ShowMplsL2TransportDetail_VC_Statistics_Schema):
    """
    Parser for show mpls l2transport vc <vc_id> detail | sect VC statistics
    """
    cli_command = 'show mpls l2transport vc {vc_id} detail | sect VC statistics'

    def cli(self, vc_id="",output=None):
        if output is None:
            out = self.device.execute(self.cli_command.format(vc_id=vc_id))
        else:
            out = output

        #   VC statistics:
        p1 = re.compile(r'^VC +statistics:$')

        #   packet totals: receive 20040, send 28879
        p2 = re.compile(r'^(transit +)?packet +totals: +receive'
                          ' +(?P<pkts_receive>\d+), +send +(?P<pkts_send>\d+)$')

        #   byte totals:   receive 25073016, send 25992388
        p3 = re.compile(r'^(transit +)?byte +totals: +receive'
                          ' +(?P<byte_receive>\d+), +send +(?P<byte_send>\d+)$')

        #   transit packet drops:  receive 0, seq error 0, send 0
        p4 = re.compile(r'^(transit +)?packet +drops: +receive'
                          ' +(?P<pkts_drop_receive>\d+), +send +(?P<pkts_drop_send>\d+)$')

        #   packet drops:  receive 0, send 0
        p4_1 = re.compile(r'^(transit +)?packet +drops: +receive +(?P<pkts_drop_receive>\d+), +seq +error +(?P<seq_error>\d+), +send +(?P<pkts_drop_send>\d+)')
        final_dict={}
        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                statistics_final_dict = final_dict.setdefault('statistics', {})
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                statistics_final_dict.setdefault('packets', {})
                statistics_final_dict['packets']['received'] = int(group['pkts_receive'])
                statistics_final_dict['packets']['sent'] = int(group['pkts_send'])
                continue

            m = p3.match(line)
            if m:
                group = m.groupdict()
                statistics_final_dict.setdefault('bytes', {})
                statistics_final_dict['bytes']['received'] = int(group['byte_receive'])
                statistics_final_dict['bytes']['sent'] = int(group['byte_send'])
                continue

            m = p4.match(line)
            if m:
                group = m.groupdict()
                statistics_final_dict.setdefault('packets_drop', {})
                statistics_final_dict['packets_drop']['received'] = int(group['pkts_drop_receive'])
                statistics_final_dict['packets_drop']['sent'] = int(group['pkts_drop_send'])
                continue

            m = p4_1.match(line)
            if m:
                group = m.groupdict()
                statistics_final_dict.setdefault('packets_drop', {})
                statistics_final_dict['packets_drop']['received'] = int(group['pkts_drop_receive'])
                statistics_final_dict['packets_drop']['seq_error'] = int(group['seq_error'])
                statistics_final_dict['packets_drop']['sent'] = int(group['pkts_drop_send'])
        return final_dict

class ShowMplsL2TransportDetail_Destination_address_Schema(MetaParser):
    """Schema for show mpls l2 vc <vc_id> detail | sect Destination address"""

    schema = {
        'destination_address': {
            Any():{
                'vc_id': {
                    Any() : {
                        Optional('local_circuit'): str,
                        'vc_status': str,
                    },
                },
                Optional('tunnel_label'): str,
                Optional('next_hop'): str,
                Optional('output_interface'): str,
                Optional('imposed_label_stack'): list,
                Optional('default_path'): str,
                Optional('preferred_path'): str,
                Optional('preferred_path_state'): str,
            },
        },
    }

class ShowMplsL2TransportDetail_Destination_address(ShowMplsL2TransportDetail_Destination_address_Schema):
    """
    Parser for show mpls l2transport vc <vc_id> detail | sect Destination address
    """
    cli_command = 'show mpls l2transport vc {vc_id} detail | sect Destination address'

    def cli(self, vc_id="",output=None):
        if output is None:
            out = self.device.execute(self.cli_command.format(vc_id=vc_id))
        else:
            out = output

        #   Destination address: 10.2.2.2, VC ID: 1002, VC status: recovering
        p1 = re.compile(r'^Destination +address: +(?P<address>[\d\.]+),'
                         ' +VC +ID: +(?P<vc_id>\d+), +VC +status: +(?P<vc_status>\w+)$')

        #   Preferred path: not configured
        p2 = re.compile(r'^Preferred +path: +(?P<preferred_path>[a-zA-Z0-9 ]+)(?:\,\s+(?P<state>\S+)$)?$')

        #   Default path: active
        p3 = re.compile(r'^Default +path: +(?P<default_path>[\S\s]+)$')

        #   Tunnel label: imp-null, next hop point2point
        p4 = re.compile(r'^Tunnel +label: +(?P<tunnel_label>\S+),'
                         ' +next +hop +(?P<next_hop>[\S\s]+)$')

        #   Next hop: point2point
        p4_1 = re.compile(r'^Next +hop: +(?P<next_hop>[\S\s]+)$')

        #   Output interface: Se2/0/2, imposed label stack {16}
        p5 = re.compile(r'^Output +interface: +(?P<output_interface>\S+),'
                         ' +imposed +label +stack +(?P<imposed_label_stack>\{[0-9 ]+\})$')

        final_dict={}
        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                destination_address = group['address']
                new_final_dict = final_dict.setdefault('destination_address', {}).\
                    setdefault(destination_address, {})
                vc_id_dict = new_final_dict.setdefault('vc_id', {}). \
                    setdefault(group['vc_id'], {})
                vc_id_dict.update({'vc_status' : group['vc_status']})
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                new_final_dict['preferred_path'] = group['preferred_path']
                if group.get('state'):
                    new_final_dict['preferred_path_state']=group['state'].strip()
                continue

            m = p3.match(line)
            if m:
                group = m.groupdict()
                new_final_dict['default_path'] = group['default_path']
                continue

            m = p4.match(line)
            if m:
                group = m.groupdict()
                new_final_dict.update({k:v for k, v in group.items()})
                continue

            m = p4_1.match(line)
            if m:
                group = m.groupdict()
                new_final_dict.update({k:v for k, v in group.items()})
                continue

            m = p5.match(line)
            if m:
                group = m.groupdict()
                new_final_dict['output_interface'] = Common.convert_intf_name(
                    group['output_interface'])
                new_final_dict['imposed_label_stack'] = re.findall('\d+',group['imposed_label_stack'])
                continue

        return final_dict


class ShowMplsTrafficEngTunnelTunnelidSchema(MetaParser):
    """Schema for show mpls traffic-eng tunnels {tunnel} """

    schema = {
        'tunnel': {
            Any(): {
                'destination': str,
                'status': {
                    'admin': str,
                    'oper': str,
                    'path': str,
                    'signalling': str,
                    'path_option': {
                        Optional(Any()): {
                            'type': str,
                            Optional('path_name'): str,
                            Optional('path_weight'): int,
                            Optional('path_attribute'): str,
                            Optional('lockdown'): bool,
                            Optional('attribute'): str,
                        },
                    },
                },
                'config_parameters': {
                    'bandwidth': int,
                    'bandwidth_unit': str,
                    'bandwidth_type': str,
                    'priority': {
                        'setup_priority': int,
                        'hold_priority': int
                    },
                    'affinity': str,
                    'metric_used': str,
                    Optional('metric_type'): str,
                    Optional('path_selection_tiebreaker'): {
                        'global': str,
                        'tunnel_specific': str,
                        'effective': str,
                        'effective_type': str
                    },
                    Optional('hop_limit'): str,
                    Optional('cost_limit'): str,
                    Optional('path_invalidation_timeout'): int,
                    Optional('path_invalidation_timeout_unit'): str,
                    Optional('path_invalidation_timeout_type'): str,
                    Optional('action'): str,
                    Optional('autoroute'): str,
                    Optional('lockdown'): str,
                    Optional('loadshare'): int,
                    Optional('max_load_share'): int,
                    Optional('load_share_type'): str,
                    Optional('auto_bw'): str,
                    Optional('fault_oam'): str,
                    Optional('wrap_protection'): str,
                    Optional('wrap_capable'): str,
                    Optional('autoroute_destination'): str
                },
                Optional('active_path_option_parameters'): {
                    'state': {
                        'active_path': str,
                        'path_type': str
                    },
                    Optional('bandwidthoverride'): str,
                    Optional('lockdown'): str,
                    Optional('verbatim'): str,
                },
                Optional('node_hop_count'): int,
                Optional('inlabel'): list,
                Optional('outlabel'): list,
                Optional('next_hop'): list,
                Optional('rsvp_signalling_info'): {
                    'src': str,
                    'dst': str,
                    'tun_id': int,
                    'tun_instance': int,
                    'rsvp_path_info': {
                        Optional('my_address'): str,
                        'explicit_route': list,
                        Optional('record_route'): str,
                        Optional('tspec'): {
                            'ave_rate': int,
                            'ave_rate_unit': str,
                            'burst': int,
                            'burst_unit': str,
                            'peak_rate': int,
                            'peak_rate_unit': str
                        }
                    },
                    Optional('rsvp_resv_info'): {
                        'record_route': str,
                        'fspec': {
                            'ave_rate': int,
                            'ave_rate_unit': str,
                            'burst': int,
                            'burst_unit': str,
                            'peak_rate': int,
                            'peak_rate_unit': str
                        },
                    },
                },
                Optional('shortest_unconstrained_path_info'): {
                    'path_weight': Any(),
                    Optional('path_weight_type'): str,
                    'explicit_route': list
                },
                Optional('history'): {
                    'tunnel': {
                        Any(): str,
                        'number_of_lsp_ids_used': int
                    },
                    Optional("current_lsp_id"): {
                        Any(): {
                            Any(): str
                        }
                    },
                    Optional('prior_lsp_id'): {
                        Any(): {
                            Optional('id'): str,
                            Optional('removal_trigger'): str,
                            Optional('last_error'): str
                        }
                    },
                },
            },
        },
    }


class ShowMplsTrafficEngTunnelTunnelid(ShowMplsTrafficEngTunnelTunnelidSchema):
    """Parser show mpls traffic-eng tunnels {tunnel}"""

    cli_command = ['show mpls traffic-eng tunnels {tunnel}']

    def cli(self, tunnel='', output=None):
        if not output:
            cmd = self.cli_command[0].format(tunnel=tunnel)
            output = self.device.execute(cmd)

        res = {}
        result = 1

        if not output.strip():
            return res

        ##Regex
        ###Name: R3_t100                             (Tunnel100) Destination: 2.2.2.2
        p1 = re.compile(
            r'^\S+:\s+\S+\s+\((?P<Tunnel>\S+)\)\s+\S+\s+(?P<destination>\S+)')

        ###Eg:Status:,Config Parameters:,Active Path Option Parameters:
        p2 = re.compile(r'^(?P<key>[a-zA-Z\- ]+)\:$')
        ###Mentions the keys to be considered
        p2_1 = re.compile(
            r'Status:|Config Parameters:|Active Path Option Parameters:|RSVP Signalling Info:|History:|Shortest Unconstrained Path Info:'
        )

        ###path option 1, type explicit R3_R4_R5_R2 (Basis for Setup, path weight 3)
        p3 = re.compile(
            r"^[a-zA-Z ]+(?P<path_option>[0-9 ]+)\,\s+(?P<lockdown>\([A-Z]+\))?"
            "\s*\S+\s(?P<type>[a-zA-Z_0-9 ]+)\s*(?:\(.*\,[a-z ]+(?P<path_weight>\S+)\))?$"
        )
        p3_1 = re.compile(r"^Path-option attribute:\s(?P<path_attribute>\S+)$")

        ###Src 3.3.3.3, Dst 2.2.2.2, Tun_Id 100, Tun_Instance 28
        p4 = re.compile(r"^Src\s+([0-9\. ]+)\,")

        ###State:
        p5 = re.compile(r"^State:")

        ###Time since created: 14 minutes, 44 seconds
        p6 = re.compile(r"^Time\s+")

        ###Bandwidth: 500      kbps (Global)  Priority: 7  7   Affinity: 0x0/0xFFFF
        p7 = re.compile(
            r'^Bandwidth:\s+(?P<bandwidth>.*)\s+[a-zA-Z ]+\:\s+(?P<priority>[0-9 ]+)'
            '\s+[a-zA-Z ]+\:\s+(?P<affinity>\S+)$')

        ### InLabel  :  -
        ###OutLabel : Port-channel30, 63
        ###Next Hop : 193.1.1.2
        p8 = re.compile(r"^([a-zA-Z ]+)\s+\:\s+([a-zA-Z\-0-9\.\, ]+)$")

        ###AutoRoute: enabled  LockDown: disabled Loadshare: 500 [4000000] bw-based
        p9 = re.compile(
            r"^AutoRoute\:\s+(?P<autoroute>\S+)\s+\S+\:\s+(?P<lockdown>\S+)"
            "\s+\S+\:\s+(?P<loadshare>\d+)\s+\[(?P<max_load_share>\d+)\]\s+(?P<load_share_type>\S+)$"
        )

        ###Record   Route:
        ###Tspec:,Fspec:
        p10 = re.compile(r"Record   Route:|[A-Za-z ]+spec\:\s+.*")

        ###Fault-OAM: disabled, Wrap-Protection: disabled, Wrap-Capable: No
        ###Hop Limit: disabled
        ###Cost Limit: disabled
        ###BandwidthOverride: disabled  LockDown: enabled   Verbatim: disabled
        ###auto-bw: disabled
        p11 = re.compile(
            r'Hop|Cost|auto-bw:'
            '|State:|Path Weight:|BandwidthOverride:|Fault-OAM:|AutoRoute destination:'
        )

        ###Explicit Route: 193.1.1.2 196.1.1.2 196.1.1.1 198.1.1.1
        #              198.1.1.2 2.2.2.2
        p12 = re.compile(r"^\d+\.\d+\.\d+\.\d+")

        ###Admin: up         Oper: up     Path: valid       Signalling: connected
        p13 = re.compile(
            r"(Admin|Oper|Path|Signalling):([a-zA-Z\- ]+\s|[a-zA-Z\- ]+)")

        ##Path-invalidation timeout: 10000 msec (default), Action: Tear
        p14 = re.compile(
            r"^Path-invalidation.+\:\s+(?P<path_invalidation_timeout>\d+)\s+"
            "(?P<path_invalidation_timeout_unit>\w+)\s+\((?P<path_invalidation_timeout_type>\S+)\)\,"
            "\s+\S+\s+(?P<action>\w+)$")

        ###Number of LSP IDs (Tun_Instances) used:
        p15 = re.compile(r"Number of LSP IDs \(Tun_Instances\) used:\s+\d+")

        ###Current LSP: [ID: 19]
        p16 = re.compile(r"^Current LSP:\s+\[ID:\s+(?P<id>\d+)\]$")

        ###Uptime: 9 hours, 52 minutes
        ###Selection: reoptimization
        p17 = re.compile(r"(Uptime|Selection):\s+([0-9a-zA-Z, ]+)")

        ##Metric Type: TE (default)
        p18 = re.compile(
            r"^Metric Type:\s+(?P<metric_used>\S+)(?:\s+\((?P<metric_type>\S+)\))*"
        )

        ###Prior LSP: [ID: 19]
        p19 = re.compile(r"^Prior LSP:\s+\[ID:\s+(?P<id>\d+)\]$")

        ##ID: path option 3 [35]
        ##Removal Trigger: tunnel shutdown
        ##Last Error: CTRL:: Explicit path has unknown address, 194.1.1.1
        p20 = re.compile(
            r"(ID|Removal Trigger|Last Error):\s+([0-9a-zA-Z,.: ]+)")

        ###Global: not set   Tunnel Specific: not set   Effective: min-fill (default)
        p21 = re.compile(
            r"^Global:\s+(?P<global>[a-zA-Z ]+)\s+Tunnel Specific:\s+(?P<tunnel_specific>[a-zA-Z ]+)\s+Effective:\s+(?P<effective>\S+)\s*\(?(?P<effective_type>[a-zA-Z ]+)?\)?$"
        )

        ###Path Weight: 1 (TE)
        p22 = re.compile(
            r"^Path Weight:\s+(?P<path_weight>(\d+))\s+\(?(?P<path_weight_type>[A-Za-z]+)?\)?$"
        )

        path_option = ""
        id = ''
        res['tunnel'] = {}
        for line in output.splitlines():
            line = line.strip()

            ###Name: R3_t100 (Tunnel100) Destination: 2.2.2.2
            ##Eg:{tunnel100:{destiantion:2.2.2.2}}
            m1 = p1.match(line)
            if m1:
                r = m1.groupdict()
                key = r['Tunnel']
                res['tunnel'][key] = {}
                res['tunnel'][key]['destination'] = r['destination']
                continue

            ###Create key,subkeys
            ###Matched line for key
            ###Eg:Status:,Config Parameters:,Active Path Option Parameters:
            ###Then subkeys, Eg:{config_parameters:{path_selection_tiebreaker:{}},...}
            m2 = p2.match(line)
            if m2:
                r1 = m2.groupdict()
                if r1['key'] == "Path-selection Tiebreaker":
                    ##{config_parameters:path_selection_tiebreaker}
                    res['tunnel'][key]["config_parameters"][r1['key'].lower()\
                        .replace(" ","_").replace("-","_").strip()]={}
                elif r1['key'] == "RSVP Path Info":
                    ##{rsvp_signalling_info:{rsvp_path_info:{}}
                    key3 = r1['key'].lower().replace(" ",
                                                     "_").replace("-",
                                                                  "_").strip()
                    res['tunnel'][key]["rsvp_signalling_info"][key3] = {}
                elif r1['key'] == "RSVP Resv Info":
                    ##{rsvp_signalling_info:{rsvp_resv_info:{}}
                    key3 = r1['key'].lower().replace(" ",
                                                     "_").replace("-",
                                                                  "_").strip()
                    res['tunnel'][key]["rsvp_signalling_info"][key3] = {}
                elif r1['key'] == "Tunnel":
                    ##tunnel:
                    res['tunnel'][key]["history"]['tunnel'] = {}
                else:
                    if p2_1.match(line):
                        key1 = r1['key'].lower().replace(" ", "_").strip()
                        res['tunnel'][key][key1] = {}
                continue

            ####path option 1, type explicit R3_R4_R5_R2 (Basis for Setup, path weight 3)
            m3 = p3.match(line)
            if m3:
                fin = m3.groupdict()
                path_option = "path_option"
                if result == 1:
                    res['tunnel'][key][key1][path_option] = {}
                    result = 0
                for item, value in fin.items():
                    if item == "path_option":
                        path = value
                        res['tunnel'][key][key1][path_option][path] = {}
                    else:
                        if item == "type":
                            s = value.split()
                            res['tunnel'][key][key1][path_option][path][
                                'type'] = s[0].strip()
                            if s[0] != "dynamic":
                                res['tunnel'][key][key1][path_option][path][
                                    'path_name'] = s[1].strip()
                        elif item == "lockdown":
                            if fin["lockdown"]:
                                res['tunnel'][key][key1][path_option][path][
                                    'lockdown'] = True
                        else:
                            if value:
                                res['tunnel'][key][key1][path_option][path][
                                    item] = int(value)
                continue

            ###Path-option attribute: TU1_attrib
            m3_1 = p3_1.match(line)
            if m3_1:
                grp = m3_1.groupdict()
                for item, value in grp.items():
                    res['tunnel'][key][key1][path_option][path][item] = value

            ###Src 3.3.3.3, Dst 2.2.2.2, Tun_Id 100, Tun_Instance 28
            m4 = p4.match(line)
            if m4:
                a = line.split(",")
                for i in a:
                    i = i.strip()
                    j = i.split(" ")[1]
                    res['tunnel'][key][key1][i.split(" ")[0].lower().strip()]=\
                            int(j) if j.isdigit() else j
                continue

            ###State: explicit path option 1 is active
            m5 = p5.match(line)
            if m5:
                res['tunnel'][key][key1]['state'] = {}
                res['tunnel'][key][key1]['state']['active_path']=\
                                re.findall(r"(\d+)",line.split(":")[1].strip())[0]
                res['tunnel'][key][key1]['state']['path_type']=\
                                line.split(":")[1].split()[0]
                continue

            ###Time since created: 14 minutes, 44 seconds
            m6 = p6.match(line)
            if m6:
                time = line.split(":")[0].lower().strip().replace(" ", "_")
                res['tunnel'][key][key1]['tunnel'][time] = line.split(
                    ":")[1].strip()
                continue

            ###Bandwidth: 500      kbps (Global)  Priority: 7  7   Affinity: 0x0/0xFFFF
            m7 = p7.match(line)
            if m7:
                r4 = m7.groupdict()
                for item, value in r4.items():
                    if item == "priority":
                        res['tunnel'][key][key1]['priority'] = {}
                        tg = value.split()
                        res['tunnel'][key][key1]['priority'][
                            'setup_priority'] = int(tg[0])
                        res['tunnel'][key][key1]['priority'][
                            'hold_priority'] = int(tg[1])
                    elif item == "bandwidth":
                        bandwidth_detail = value.split()
                        res['tunnel'][key][key1][item] = int(
                            bandwidth_detail[0])
                        res['tunnel'][key][key1][
                            "bandwidth_unit"] = bandwidth_detail[1]
                        res['tunnel'][key][key1]["bandwidth_type"]=\
                                        re.sub(r"[()]","",bandwidth_detail[2])
                    else:
                        res['tunnel'][key][key1][item] = value.strip()
                continue

            ###Match InLabel : -
            m8 = p8.match(line)
            if m8:
                r8 = m8.group()
                res['tunnel'][key][r8.split(":")[0].strip().lower().replace(" ","_")]=\
                                    r8.split(":")[1].strip().split(",")
                continue

            ###AutoRoute: enabled  LockDown: disabled Loadshare: 500 [4000000] bw-based
            m9 = p9.match(line)
            if m9:
                r9 = m9.groupdict()
                for item, value in r9.items():
                    res['tunnel'][key][key1][item.strip()]=\
                    int(value) if value.strip().isdecimal() else value
                continue

            ###Record   Route:   NONE
            ###Tspec: ave rate=500 kbits, burst=1000 bytes, peak rate=500 kbits
            m10 = p10.match(line)
            if m10:
                if "=" not in line:
                    res['tunnel'][key][key1][key3][
                        "record_route"] = line.split(":")[1].strip()
                else:
                    r7 = m10.group()
                    key5 = r7.split(":")[0].strip().lower()
                    res['tunnel'][key][key1][key3][key5] = {}
                    r8 = r7.split(":")[1].split(",")
                    for i in r8:
                        res10 = i.split("=")[1].split()
                        item = i.split("=")[0].lower().strip().replace(
                            " ", "_")
                        res['tunnel'][key][key1][key3][key5][item] = int(
                            res10[0])
                        res['tunnel'][key][key1][key3][key5][
                            item + "_unit"] = res10[1]
                continue

            ###Global: not set   Tunnel Specific: not set   Effective: min-fill (default)
            ###Make global part of path_selection_tiebreaker
            m21 = p21.match(line)
            if m21:
                re21 = m21.groupdict()
                for item, value in re21.items():
                    res['tunnel'][key]['config_parameters']["path_selection_tiebreaker"][item.split(":")[0].strip().replace(" ","_").lower()]=\
                    value.strip()
                continue

            ##Path Weight: 1 (TE)
            m22 = p22.match(line)
            if m22:
                re22 = m22.groupdict()
                for item, value in re22.items():
                    res['tunnel'][key][key1][item] = value.strip()
                continue

            ###Make explicit route as part of rsvp_path_info or shortest_unconstrained_path_info respectively
            ###Make my address as part of rsvp_path_info
            ###My Address: 192.1.1.1
            ###Explicit Route: 192.1.1.2 2.2.2.2
            if re.match("^Explicit Route:|My", line):
                if "Explicit Route:" in line:
                    explicit_route = []
                    explicit_route.extend(line.split(":")[1].split())

                    if key1 == "rsvp_signalling_info":
                        res['tunnel'][key][key1]['rsvp_path_info'][
                            'explicit_route'] = explicit_route
                    elif key1 == "shortest_unconstrained_path_info":
                        res['tunnel'][key][key1][
                            'explicit_route'] = explicit_route
                else:
                    res['tunnel'][key][key1]['rsvp_path_info'][line.split(":")[0]\
                    .strip().lower().replace(" ","_")]=line.split(":")[1].lower().strip()
                continue

            ##  Node Hop Count: 1
            if "Node Hop Count:" in line:
                ib = int(line.split(":")[1].lower().strip())
                res['tunnel'][key][line.split(":")[0].strip().lower().replace(
                    " ", "_")] = ib
                continue

            ###Fault-OAM: disabled, Wrap-Protection: disabled, Wrap-Capable: No
            ###Hop Limit: disabled
            ###Cost Limit: disabled
            ###BandwidthOverride: disabled  LockDown: enabled   Verbatim: disabled
            ###auto-bw: disabled
            m11 = p11.match(line)
            if m11:
                line = re.sub(r'\:\s{2,}', ": ", line.strip())
                re9 = re.split("\s{2,}|,", line.strip())
                for i in re9:
                    ib = i.split(":")[1].strip().replace(
                        "[ignore", "").replace("(te)", "").strip()
                    res['tunnel'][key][key1][i.split(":")[0].strip().lower()\
                    .replace(" ","_").replace("-","_").strip()]=int(ib) if ib.isdecimal() else ib
                continue

            #Explicit Route: 193.1.1.2 196.1.1.2 196.1.1.1 198.1.1.1
            #                198.1.1.2 2.2.2.2
            if p12.match(line):
                explicit_route.extend(line.split())

            ###Admin: up         Oper: up     Path: valid       Signalling: connected
            if "Admin:" in line:
                m13 = p13.findall(line)
                if m13:
                    line = re.sub(r'\:\s{1,}', ":", line.strip())
                    for match in m13:
                        res['tunnel'][key][key1][match[0].strip().lower(
                        )] = match[1].strip().lower()
                continue

            ##Path-invalidation timeout: 10000 msec (default), Action: Tear
            m14 = p14.match(line)
            if m14:
                re14 = m14.groupdict()
                for item, value in re14.items():
                    res['tunnel'][key][key1][item] = int(
                        value) if value.isdecimal() else value
                continue

            ###Number of LSP IDs (Tun_Instances) used: 19
            m15 = p15.match(line)
            if m15:
                res['tunnel'][key][key1]['tunnel'][
                    "number_of_lsp_ids_used"] = int(line.split(":")[1])
                continue

            ###Current LSP: [ID: 19]
            m16 = p16.match(line)
            if m16:
                id = m16.groupdict()
                res['tunnel'][key][key1]['current_lsp_id'] = {}
                res['tunnel'][key][key1]['current_lsp_id'][id['id']] = {}
                continue

            ###Uptime: 9 hours, 52 minutes
            ###Selection: reoptimization
            m17 = p17.match(line)
            if m17:
                res17 = p17.findall(line)
                res['tunnel'][key][key1]['current_lsp_id'][id['id']][
                    res17[0][0].lower()] = res17[0][1]
                continue

            #Metric Type: TE (default)
            m18 = p18.match(line)
            if m18:
                res18 = m18.groupdict()
                res['tunnel'][key]["config_parameters"]['metric_used'] = res18[
                    'metric_used']
                if res18.get("metric_type", None):
                    res['tunnel'][key]['config_parameters'][
                        'metric_type'] = res18['metric_type']
                continue

            ###Prior LSP: [ID: 19]
            m19 = p19.match(line)
            if m19:
                id = m19.groupdict()
                res['tunnel'][key][key1]['prior_lsp_id'] = {}
                res['tunnel'][key][key1]['prior_lsp_id'][id['id']] = {}
                continue

            ###ID: path option 3 [35]
            ###Removal Trigger: tunnel shutdown
            ###Last Error: CTRL:: Explicit path has unknown address, 194.1.1.1
            m20 = p20.match(line)
            if m20:
                res20 = p20.findall(line)
                for prior_key, prior_value in res20:
                    res['tunnel'][key][key1]['prior_lsp_id'][id['id']][
                        prior_key.lower().replace(" ", "_")] = prior_value
                continue

        return res


class ShowMplsTrafficEngTunnelSchema(MetaParser):
    """Schema for show mpls traffic-eng tunnels"""

    schema = {
        'tunnel_type': {
            Any(): {
                'tunnel_name': {
                    Any(): {
                        Optional('destination'): str,
                        Optional('signalled_state'): bool,
                        Optional('tunnel_state'): str,
                        Optional('status'): {
                            'admin': str,
                            'oper': str,
                            'path': str,
                            'signalling': str,
                            'path_option': {
                                Optional(Any()): {
                                    'type': str,
                                    Optional('path_name'): str,
                                    Optional('path_weight'): int,
                                    Optional('path_attribute'): str,
                                    Optional('lockdown'): bool,
                                    Optional('attribute'): str,
                                },
                            },
                        },
                        Optional('config_parameters'): {
                            'bandwidth': int,
                            'bandwidth_unit': str,
                            'bandwidth_type': str,
                            'priority': {
                                'setup_priority': int,
                                'hold_priority': int
                            },
                            'affinity': str,
                            'metric_used': str,
                            Optional('metric_type'): str,
                            Optional('path_selection_tiebreaker'): {
                                'global': str,
                                'tunnel_specific': str,
                                'effective': str,
                                'effective_type': str
                            },
                            Optional('hop_limit'): str,
                            Optional('cost_limit'): str,
                            Optional('path_invalidation_timeout'): int,
                            Optional('path_invalidation_timeout_unit'): str,
                            Optional('path_invalidation_timeout_type'): str,
                            Optional('action'): str,
                            Optional('autoroute'): str,
                            Optional('lockdown'): str,
                            Optional('max_load_share'): int,
                            Optional('load_share_type'): str,
                            Optional('loadshare'): int,
                            Optional('auto_bw'): str,
                            Optional('fault_oam'): str,
                            Optional('wrap_protection'): str,
                            Optional('wrap_capable'): str,
                            Optional('autoroute_destination'): str
                        },
                        Optional('active_path_option_parameters'): {
                            'state': {
                                'active_path': str,
                                'path_type': str
                            },
                            Optional('bandwidthoverride'): str,
                            Optional('lockdown'): str,
                            Optional('verbatim'): str,
                        },
                        Optional('node_hop_count'): int,
                        Optional('inlabel'): list,
                        Optional('outlabel'): list,
                        Optional('next_hop'): list,
                        Optional('prev_hop'): list,
                        Optional('rsvp_signalling_info'): {
                            'src': str,
                            'dst': str,
                            'tun_id': int,
                            'tun_instance': int,
                            'rsvp_path_info': {
                                Optional('my_address'): str,
                                'explicit_route': list,
                                Optional('record_route'): str,
                                Optional('tspec'): {
                                    'ave_rate': int,
                                    'ave_rate_unit': str,
                                    'burst': int,
                                    'burst_unit': str,
                                    'peak_rate': int,
                                    'peak_rate_unit': str
                                }
                            },
                            Optional('rsvp_resv_info'): {
                                'record_route': str,
                                'fspec': {
                                    'ave_rate': int,
                                    'ave_rate_unit': str,
                                    'burst': int,
                                    'burst_unit': str,
                                    'peak_rate': int,
                                    'peak_rate_unit': str
                                },
                            },
                        },
                        Optional('shortest_unconstrained_path_info'): {
                            'path_weight': Any(),
                            Optional('path_weight_type'): str,
                            'explicit_route': list
                        },
                        Optional('history'): {
                            'tunnel': {
                                Any(): str,
                                'number_of_lsp_ids_used': int
                            },
                            Optional("current_lsp_id"): {
                                Any(): {
                                    Any(): str
                                }
                            },
                            Optional('prior_lsp_id'): {
                                Any(): {
                                    Optional('id'): str,
                                    Optional('removal_trigger'): str,
                                    Optional('last_error'): str
                                }
                            }
                        },
                    },
                },
            },
        },
    }


class ShowMplsTrafficEngTunnel(ShowMplsTrafficEngTunnelSchema):
    """Parser show mpls traffic-eng tunnels"""

    cli_command = ['show mpls traffic-eng tunnels']

    def cli(self, output=None):
        if not output:
            cmd = self.cli_command[0]

            output = self.device.execute(cmd)

        res = {}
        result = 1
        base_key = ""
        path_opt, id = "", ""
        tunnel_types = ["P2P TUNNELS/LSPs", "P2MP TUNNELS", "P2MP SUB-LSPS"]
        if not output.strip():
            return res

        ##Regex
        ###Name: R3_t100                             (Tunnel100) Destination: 2.2.2.2
        p1 = re.compile(
            r'^\S+:\s+\S+\s+\((?P<Tunnel>\S+)\)\s+\S+\s+(?P<destination>\S+)')

        ###Eg:Status:,Config Parameters:,Active Path Option Parameters:
        p2 = re.compile(r'^(?P<key>[a-zA-Z\-0-9/LSPs ]+)\:$')
        ###Mentions the keys to be considered
        p2_1 = re.compile(
            r'Status:|Config Parameters:|Active Path Option Parameters:'
            '|RSVP Signalling Info:|History:|Shortest Unconstrained Path Info:'
        )

        ###path option 1, type explicit R3_R4_R5_R2 (Basis for Setup, path weight 3)
        p3 = re.compile(
            r"^[a-zA-Z ]+(?P<path_option>[0-9 ]+)\,\s+(?P<lockdown>\([A-Z]+\))?"
            "\s*\S+\s(?P<type>[a-zA-Z_0-9 ]+)\s*(?:\(.*\,[a-z ]+(?P<path_weight>\S+)\))?"
        )
        p3_1 = re.compile(r"^Path-option attribute:\s(?P<path_attribute>\S+)$")

        ###Src 3.3.3.3, Dst 2.2.2.2, Tun_Id 100, Tun_Instance 28
        p4 = re.compile(r"^Src\s+([0-9\. ]+)\,")

        ###Time since created: 14 minutes, 44 seconds
        p5 = re.compile(r"^Time\s+")

        ###Bandwidth: 500      kbps (Global)  Priority: 7  7   Affinity: 0x0/0xFFFF
        p6 = re.compile(
            r'^Bandwidth:\s+(?P<bandwidth>.*)\s+[a-zA-Z ]+\:\s+(?P<priority>[0-9 ]+)'
            '\s+[a-zA-Z ]+\:\s+(?P<affinity>\S+)$')

        ### InLabel  :  -
        ###OutLabel : Port-channel30, 63
        ###Next Hop : 193.1.1.2
        p7 = re.compile(r"^([a-zA-Z ]+)\s+\:\s+([a-zA-Z\/\-0-9\.\, ]+)$")

        ###AutoRoute: enabled  LockDown: disabled Loadshare: 500 [4000000] bw-based
        p8 = re.compile(
            r"^AutoRoute\:\s+(?P<autoroute>\S+)\s+\S+\:\s+(?P<lockdown>\S+)"
            "\s+\S+\:\s+(?P<loadshare>\d+)\s+\[(?P<max_load_share>\d+)\]\s+(?P<load_share_type>\S+)$"
        )

        ###Record   Route:
        ###Tspec:,Fspec:
        p9 = re.compile(r"Record   Route:|[A-Za-z ]+spec\:\s+.*")

        ###Fault-OAM: disabled, Wrap-Protection: disabled, Wrap-Capable: No
        ###Hop Limit: disabled
        ###Cost Limit: disabled
        ###BandwidthOverride: disabled  LockDown: enabled   Verbatim: disabled
        ###auto-bw: disabled
        p10 = re.compile(
            r'Hop|Cost|'
            'auto-bw:|State:|Path Weight:|BandwidthOverride:|Fault-OAM:|AutoRoute destination:'
        )

        ###Explicit Route: 193.1.1.2 196.1.1.2 196.1.1.1 198.1.1.1
        #              198.1.1.2 2.2.2.2 --matches line
        p11 = re.compile(r"^\d+\.\d+\.\d+\.\d+")

        ###State:
        p12 = re.compile(r"^State:")

        ###Admin: up         Oper: up     Path: valid       Signalling: connected
        p13 = re.compile(
            r"(Admin|Oper|Path|Signalling):([a-zA-Z\- ]+\s|[a-zA-Z\- ]+)")

        ##Path-invalidation timeout: 10000 msec (default), Action: Tear
        p14 = re.compile(
            r"^Path-invalidation.+\:\s+(?P<path_invalidation_timeout>\d+)\s+"
            "(?P<path_invalidation_timeout_unit>\w+)\s+\((?P<path_invalidation_timeout_type>\S+)\)"
            "\,\s+\S+\s+(?P<action>\w+)$")

        ####LSP Tunnel PE1_t100 is signalled, connection is up
        p15 = re.compile(
            r"^LSP\sTunnel\s+[a-zA-Z0-9]+\_\w"
            "(?P<tunnel_id>[0-9]+)\s+is\s+(?P<signalled>\S+)\,\s+connection\s+is\s+(?P<state>\S+)$"
        )

        ###Number of LSP IDs (Tun_Instances) used:
        p16 = re.compile(r"Number of LSP IDs \(Tun_Instances\) used:\s+\d+")

        ###Current LSP: [ID: 19]
        p17 = re.compile(r"^Current LSP:\s+\[ID:\s+(?P<id>\d+)\]$")

        ###Uptime: 9 hours, 52 minutes
        ###Selection: reoptimization
        p18 = re.compile(r"(Uptime|Selection):\s+([0-9a-zA-Z, ]+)")

        ##Metric Type: TE (default)
        p19 = re.compile(
            r"^Metric Type:\s+(?P<metric_used>\S+)(?:\s+\((?P<metric_type>\S+)\))*"
        )

        ###Prior LSP: [ID: 19]
        p20 = re.compile(r"^Prior LSP:\s+\[ID:\s+(?P<id>\d+)\]$")

        ##ID: path option 3 [35]
        ##Removal Trigger: tunnel shutdown
        ##Last Error: CTRL:: Explicit path has unknown address, 194.1.1.1
        p21 = re.compile(
            r"(ID|Removal Trigger|Last Error):\s+([0-9a-zA-Z,.: ]+)")

        ###Global: not set   Tunnel Specific: not set   Effective: min-fill (default)
        p22 = re.compile(
            r"^Global:\s+(?P<global>[a-zA-Z ]+)\s+Tunnel Specific:\s+(?P<tunnel_specific>[a-zA-Z ]+)\s+Effective:\s+(?P<effective>\S+)\s*\(?(?P<effective_type>[a-zA-Z ]+)?\)?$"
        )

        ###Path Weight: 1 (TE)
        p23 = re.compile(
            r"^Path Weight:\s+(?P<path_weight>(\d+))\s+\(?(?P<path_weight_type>[A-Za-z]+)?\)?$"
        )

        res['tunnel_type'] = {}
        for line in output.splitlines():
            line = line.strip()

            ###Matched line for key
            ###Eg:Status:, Config Parameters:, Active Path Option Parameters:
            ###P2MP TUNNELS:, P2MP SUB-LSPS, P2P TUNNELS/LSPs
            m2 = p2.match(line)
            if m2:
                r1 = m2.groupdict()
                if r1['key'] in tunnel_types:
                    base_key = r1['key'].lower().replace(" ", "_").replace(
                        "/lsps", "").replace("-", "_")
                    res['tunnel_type'][base_key] = {}
                    res['tunnel_type'][base_key]['tunnel_name'] = {}
                    continue
                else:
                    if r1['key'] == "Path-selection Tiebreaker":
                        res['tunnel_type'][base_key]['tunnel_name'][key]["config_parameters"][r1['key'].\
                        lower().replace(" ","_").replace("-","_").strip()]={}
                    elif r1['key'] == "RSVP Path Info":
                        key3 = r1['key'].lower().replace(" ", "_").replace(
                            "-", "_").strip()

                        res['tunnel_type'][base_key]['tunnel_name'][key][
                            "rsvp_signalling_info"][key3] = {}
                    elif r1['key'] == "RSVP Resv Info":
                        key3 = r1['key'].lower().replace(" ", "_").replace(
                            "-", "_").strip()
                        res['tunnel_type'][base_key]['tunnel_name'][key][
                            "rsvp_signalling_info"][key3] = {}
                    elif r1['key'] == "Tunnel":
                        ##tunnel:
                        res['tunnel_type'][base_key]['tunnel_name'][key][
                            "history"]['tunnel'] = {}
                    else:
                        if p2_1.match(line):
                            key1 = r1['key'].lower().replace(" ", "_").strip()
                            res['tunnel_type'][base_key]['tunnel_name'][key][
                                key1] = {}
                    continue

            ###LSP Tunnel PE1_t100 is signalled, connection is up
            m = p15.match(line)
            if m:
                m15 = m.groupdict()
                key = "Tunnel" + m15['tunnel_id']
                res['tunnel_type'][base_key]['tunnel_name'][key] = {}
                if m15['signalled'] == "signalled":
                    res['tunnel_type'][base_key]['tunnel_name'][key][
                        'signalled_state'] = True
                else:
                    res['tunnel_type'][base_key]['tunnel_name'][key][
                        'signalled_state'] = False
                res['tunnel_type'][base_key]['tunnel_name'][key][
                    'tunnel_state'] = m15['state']
                continue

            ###Name: R3_t100                             (Tunnel100) Destination: 2.2.2.2
            ##Eg:{tunnel100:{destiantion:2.2.2.2}}
            m1 = p1.match(line)
            if m1:
                r = m1.groupdict()
                key = r['Tunnel']
                res['tunnel_type'][base_key]['tunnel_name'][key] = {}
                res['tunnel_type'][base_key]['tunnel_name'][key][
                    'destination'] = r['destination']
                continue

            ####path option 1, type explicit R3_R4_R5_R2 (Basis for Setup, path weight 3)
##'path_option': {'1': {'type': 'explicit','path_name':'R3_R4_R5_R2', 'path_weight': 3}}
            m3 = p3.match(line)
            if m3:
                fin = m3.groupdict()
                path_option = "path_option"
                if result == 1:
                    res['tunnel_type'][base_key]['tunnel_name'][key][key1][
                        path_option] = {}
                    result = 0
                for item, value in fin.items():
                    if item == "path_option":
                        path = value
                        res['tunnel_type'][base_key]['tunnel_name'][key][key1][
                            path_option][path] = {}
                    else:
                        if item == "type":
                            s = value.split()
                            res['tunnel_type'][base_key]['tunnel_name'][key][
                                key1][path_option][path]['type'] = s[0].strip(
                                )
                            if s[0] != "dynamic":
                                res['tunnel_type'][base_key]['tunnel_name'][
                                    key][key1][path_option][path][
                                        'path_name'] = s[1].strip()
                        elif item == "lockdown":
                            if fin["lockdown"]:
                                res['tunnel_type'][base_key]['tunnel_name'][
                                    key][key1][path_option][path][
                                        'lockdown'] = True
                        else:
                            if value:
                                res['tunnel_type'][base_key]['tunnel_name'][
                                    key][key1][path_option][path][item] = int(
                                        value)

                continue

            ###Path-option attribute: TU1_attrib
            m3_1 = p3_1.match(line)
            if m3_1:
                grp = m3_1.groupdict()
                for item, value in grp.items():
                    res['tunnel_type'][base_key]['tunnel_name'][key][key1][
                        path_option][path][item] = value

            ###Src 3.3.3.3, Dst 2.2.2.2, Tun_Id 100, Tun_Instance 28
            ##Eg:{'src': '3.3.3.3', 'dst': '2.2.2.2', 'tun_id': 100, 'tun_instance': 28}
            m4 = p4.match(line)
            if m4:
                a = line.split(",")
                for i in a:
                    i = i.strip()
                    j = i.split(" ")[1]
                    res['tunnel_type'][base_key]['tunnel_name'][key][key1][i.split(" ")[0].lower().strip()]=\
                                            int(j) if j.isdigit() else j
                continue

            ###State: explicit path option 1 is active
            m12 = p12.match(line)
            if m12:
                res['tunnel_type'][base_key]['tunnel_name'][key][key1][
                    'state'] = {}
                res['tunnel_type'][base_key]['tunnel_name'][key][key1]['state']['active_path']=\
                            re.findall(r"(\d+)",line.split(":")[1].strip())[0]
                res['tunnel_type'][base_key]['tunnel_name'][key][key1]['state']['path_type']=\
                            line.split(":")[1].split()[0]
                continue

            ###Time since created: 14 minutes, 44 seconds
            m5 = p5.match(line)
            if m5:
                time = line.split(":")[0].lower().strip().replace(" ", "_")
                res['tunnel_type'][base_key]['tunnel_name'][key][key1][
                    'tunnel'][time] = line.split(":")[1].strip()
                continue

            ###Bandwidth: 500      kbps (Global)  Priority: 7  7   Affinity: 0x0/0xFFFF
            m6 = p6.match(line)
            if m6:
                result = 1
                r4 = m6.groupdict()
                for item, value in r4.items():
                    if item == "priority":
                        res['tunnel_type'][base_key]['tunnel_name'][key][key1][
                            'priority'] = {}
                        tg = value.split()
                        res['tunnel_type'][base_key]['tunnel_name'][key][key1][
                            'priority']['setup_priority'] = int(tg[0])
                        res['tunnel_type'][base_key]['tunnel_name'][key][key1][
                            'priority']['hold_priority'] = int(tg[1])
                    elif item == "bandwidth":
                        bandwidth_detail = value.split()
                        res['tunnel_type'][base_key]['tunnel_name'][key][key1][
                            item] = int(bandwidth_detail[0])
                        res['tunnel_type'][base_key]['tunnel_name'][key][key1][
                            "bandwidth_unit"] = bandwidth_detail[1]
                        res['tunnel_type'][base_key]['tunnel_name'][key][key1]["bandwidth_type"]=\
                                            re.sub(r"[()]","",bandwidth_detail[2])
                    else:
                        res['tunnel_type'][base_key]['tunnel_name'][key][key1][
                            item] = value.strip()
                continue

            ###Match InLabel : -
            m7 = p7.match(line)
            if m7:
                r5 = m7.group()
                res['tunnel_type'][base_key]['tunnel_name'][key][r5.split(":")[0].strip().lower().\
                                    replace(" ","_")]=list(map(str.strip,r5.split(":")[1].strip().split(",")))
                continue

            ###AutoRoute: enabled  LockDown: disabled Loadshare: 500 [4000000] bw-based
            m8 = p8.match(line)
            if m8:
                r6 = m8.groupdict()
                for item, value in r6.items():
                    res['tunnel_type'][base_key]['tunnel_name'][key][key1][item.strip()]=\
                                    int(value) if value.strip().isdecimal() else value
                continue

            ###Record   Route:   NONE
            ###Tspec: ave rate=500 kbits, burst=1000 bytes, peak rate=500 kbits
            m9 = p9.match(line)
            if m9:
                if "=" not in line:
                    res['tunnel_type'][base_key]['tunnel_name'][key][key1][key3]["record_route"]=\
                                    line.split(":")[1].strip()
                else:
                    r7 = m9.group()
                    key4 = r7.split(":")[0].strip().lower()
                    res['tunnel_type'][base_key]['tunnel_name'][key][key1][
                        key3][key4] = {}
                    r8 = r7.split(":")[1].split(",")
                    for i in r8:
                        res10 = i.split("=")[1].split()
                        item = i.split("=")[0].lower().strip().replace(
                            " ", "_")
                        res['tunnel_type'][base_key]['tunnel_name'][key][key1][
                            key3][key4][item] = int(res10[0])
                        res['tunnel_type'][base_key]['tunnel_name'][key][key1][
                            key3][key4][item + "_unit"] = res10[1]
                        continue

            ###Global: not set   Tunnel Specific: not set   Effective: min-fill (default)
            ###Make global part of path_selection_tiebreaker
            m22 = p22.match(line)
            if m22:
                re22 = m22.groupdict()
                for item, value in re22.items():
                    res['tunnel_type'][base_key]['tunnel_name'][key]['config_parameters']["path_selection_tiebreaker"][item.split(":")[0].strip().replace(" ","_").lower()]=\
                    value.strip()
                continue

            ##Path Weight: 1 (TE)
            m23 = p23.match(line)
            if m23:
                re23 = m23.groupdict()
                for item, value in re23.items():
                    res['tunnel_type'][base_key]['tunnel_name'][key][key1][
                        item] = value.strip()
                continue

            ###Make explicit route as part of rsvp_path_info or shortest_unconstrained_path_info respectively
            ###Make my address as part of rsvp_path_info
            ###My Address: 192.1.1.1
            ###Explicit Route: 192.1.1.2 2.2.2.2
            if re.match("^Explicit Route:|My", line):
                if "Explicit Route:" in line:
                    explicit_route = []
                    explicit_route.extend(line.split(":")[1].split())

                    if key1 == "rsvp_signalling_info":
                        res['tunnel_type'][base_key]['tunnel_name'][key][key1]['rsvp_path_info']\
                                ['explicit_route']=explicit_route
                    elif key1 == "shortest_unconstrained_path_info":
                        res['tunnel_type'][base_key]['tunnel_name'][key][key1][
                            'explicit_route'] = explicit_route
                else:
                    res['tunnel_type'][base_key]['tunnel_name'][key][key1]['rsvp_path_info']\
                    [line.split(":")[0].strip().lower().replace(" ","_")]=line.split(":")[1].\
                                                                            lower().strip()
                continue

            ##  Node Hop Count: 1
            if "Node Hop Count:" in line:
                ib = int(line.split(":")[1].lower().strip())
                res['tunnel_type'][base_key]['tunnel_name'][key][line.split(
                    ":")[0].strip().lower().replace(" ", "_")] = ib
                continue

            ###Fault-OAM: disabled, Wrap-Protection: disabled, Wrap-Capable: No
            ###Hop Limit: disabled
            ###Cost Limit: disabled
            ###BandwidthOverride: disabled  LockDown: enabled   Verbatim: disabled
            ###auto-bw: disabled
            m10 = p10.match(line)
            if m10:
                line = re.sub(r'\:\s{2,}', ": ", line.strip())
                re9 = re.split("\s{2,}|,", line.strip())
                for i in re9:
                    ib = i.split(":")[1].strip().replace("[ignore", "").strip()
                    res['tunnel_type'][base_key]['tunnel_name'][key][key1][i.split(":")[0].strip()\
                        .lower().replace(" ","_").replace("-","_").strip()]=\
                        int(ib) if ib.isdecimal() else ib
                continue

            #Explicit Route: 193.1.1.2 196.1.1.2 196.1.1.1 198.1.1.1
            #198.1.1.2 2.2.2.2
            if p11.match(line):
                explicit_route.extend(line.split())

            ###Admin: up         Oper: up     Path: valid       Signalling: connected
            if "Admin:" in line:
                m13 = p13.findall(line)
                if m13:
                    line = re.sub(r'\:\s{1,}', ":", line.strip())
                    for match in m13:
                        res['tunnel_type'][base_key]['tunnel_name'][key][key1][match[0].strip().lower()]=\
                                        match[1].strip().lower()
                continue

            ##Path-invalidation timeout: 10000 msec (default), Action: Tear
            m14 = p14.match(line)
            if m14:
                re14 = m14.groupdict()
                for item, value in re14.items():
                    res['tunnel_type'][base_key]['tunnel_name'][key][key1][item]=\
                                    int(value) if value.isdecimal() else value
                continue

            ###Number of LSP IDs (Tun_Instances) used: 19
            m16 = p16.match(line)
            if m16:
                res['tunnel_type'][base_key]['tunnel_name'][key][key1][
                    'tunnel']["number_of_lsp_ids_used"] = int(
                        line.split(":")[1])
                continue

            ###Current LSP: [ID: 19]
            m17 = p17.match(line)
            if m17:
                id = m17.groupdict()
                res['tunnel_type'][base_key]['tunnel_name'][key][key1][
                    'current_lsp_id'] = {}
                res['tunnel_type'][base_key]['tunnel_name'][key][key1][
                    'current_lsp_id'][id['id']] = {}
                continue

            ###Uptime: 9 hours, 52 minutes
            ###Selection: reoptimization
            m18 = p18.match(line)
            if m18:
                res18 = p18.findall(line)
                res['tunnel_type'][base_key]['tunnel_name'][key][key1][
                    'current_lsp_id'][id['id']][res18[0]
                                                [0].lower()] = res18[0][1]
                continue

            #Metric Type: TE (default)
            m19 = p19.match(line)
            if m19:
                res19 = m19.groupdict()
                res['tunnel_type'][base_key]['tunnel_name'][key][
                    "config_parameters"]['metric_used'] = res19['metric_used']
                if res19.get("metric_type", None):
                    res['tunnel_type'][base_key]['tunnel_name'][key][
                        'config_parameters']['metric_type'] = res19[
                            'metric_type']
                continue

            ###Prior LSP: [ID: 19]
            m20 = p20.match(line)
            if m20:
                id = m20.groupdict()
                res['tunnel_type'][base_key]['tunnel_name'][key][key1][
                    'prior_lsp_id'] = {}
                res['tunnel_type'][base_key]['tunnel_name'][key][key1][
                    'prior_lsp_id'][id['id']] = {}
                continue

            ###ID: path option 3 [35]
            ###Removal Trigger: tunnel shutdown
            ###Last Error: CTRL:: Explicit path has unknown address, 194.1.1.1
            m21 = p21.match(line)
            if m21:
                res21 = p21.findall(line)
                for prior_key, prior_value in res21:
                    res['tunnel_type'][base_key]['tunnel_name'][key][key1][
                        'prior_lsp_id'][id['id']][prior_key.lower().replace(
                            " ", "_")] = prior_value
                continue

        return res


# =============================================
# Parser for 'show mpls traffic-eng tunnels brief'
# =============================================


class ShowMplsTrafficEngTunnelBriefSchema(MetaParser):
    """Schema for show mpls traffic-eng tunnels brief
    """

    schema = {
        Optional('signalling_summary'): {
            Optional('lsp_tunnels_process'): str,
            Optional('passive_lsp_listener'): str,
            Optional('rsvp_process'): str,
            Optional('forwarding'): str,
            Optional('auto_tunnel'): {
                Optional('p2p_state'): str,
                Optional('min_range'): str,
                Optional('max_range'): str
            },
            Optional('periodic_reoptimization'): str,
            Optional('periodic_frr_promotion'): str,
            Optional('periodic_auto_bw_collection'): str,
            Optional('sr_tunnel_max_label_push'): str
        },
        'p2p_tunnels': {
            Optional('tunnel_id'): {
                Optional(Any()): {
                    Optional('destination_ip'): str,
                    Optional('up_intf'): str,
                    Optional('down_intf'): str,
                    Optional('state'): str,
                    Optional('prot'): str
                },
            },
        },
        'p2mp_tunnels': {
            Optional('tunnel_id'): str
        }
    }


class ShowMplsTrafficEngTunnelBrief(ShowMplsTrafficEngTunnelBriefSchema):
    """ Parser for show mpls traffic-eng tunnels brief"""

    cli_command = 'show mpls traffic-eng tunnels brief'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        result_dict = {}
        res = 1

        #Matches pattern with key:
        #Eg:
        #Signalling Summary:
        #P2P TUNNELS/LSPs:
        #P2MP TUNNELS:
        p1 = re.compile(r"^(?P<key>[a-zA-Z\/\d ]+)\:$")

        #Matched lines for p2 regex, all the string with the format, key: value
        # Eg: LSP Tunnels Process:            running
        p2 = re.compile(r'^(?P<key1>[\S ]+)\:\s+(?P<value1>[\S ]+)$')

        #Macallan-SVL_t100                2.2.2.2          -         Gi1/1/0/2 up/up
        p3 = re.compile(
            r'\S+\_(?P<tunnel_id>\S+)\s+(?P<destination_ip>\S+)\s+(?P<up_intf>\S+)\s+(?P<down_intf>\S+)\s+(?P<state>\S+)\/(?P<prot>\S+)'
        )

        #p2p    Disabled (0), id-range:62336-64335
        p4 = re.compile(
            r'\S+\s+(?P<p2p_state>\S+)\s+\S+\,\s+[a-z\- ]+\:(?P<min_range>\d+)\-(?P<max_range>\d+)'
        )

        for line in out.splitlines():
            line = line.strip()

            #P2P TUNNELS/LSPs:
            #line that contains <key>:
            m1 = p1.match(line)
            if m1:
                r = m1.groupdict()
                key = r['key'].lower().replace(" ", "_").replace(
                    "/lsps", "")  ##replace space and /lsps
                result_dict[key] = {}

            #    Periodic reoptimization:        every 180 seconds, next in 127 seconds
            m2 = p2.match(line)
            if m2:
                r1 = m2.groupdict()
                #Value that have , or ( fetch the first digit from that line else consider the value as it is.
                #Eg:Periodic reoptimization: every 180 seconds, next in 127 seconds
                if ("," in r1['value1']) or ("(" in r1['value1']):
                    res2 = re.findall('(\d+)', r1['value1'])[0]
                else:
                    #LSP Tunnels Process:            running
                    res2 = r1['value1']
                result_dict[key][r1['key1'].lower().replace(" ", "_").replace(
                    "-", "_")] = res2

            #Macallan-SVL_t100                          2.2.2.2          -         Po60      up/up
            m3 = p3.match(line)
            if m3:
                if res == 1:
                    result_dict[key]['tunnel_id'] = {}
                    res = 0
                r3 = m3.groupdict()
                key1 = r3['tunnel_id']
                del r3['tunnel_id']
                result_dict[key]['tunnel_id'][key1] = {}
                for item, value in r3.items():
                    result_dict[key]['tunnel_id'][key1][item] = value

            #Add 'auto-tunnel' as key
            if "auto-tunnel" in line:
                result_dict[key]['auto_tunnel'] = {}

            #	p2p    Disabled (0), id-range:62336-64335
            m4 = p4.match(line)
            if m4:
                r4 = m4.groupdict()
                for item, value in r4.items():
                    result_dict[key]['auto_tunnel'][item] = value
        return result_dict

class ShowMplsLabelRangeSchema(MetaParser):
    '''
    Search for
    show mpls label range
    '''

    schema = {
        'downstream_generic_label_region': {
            'min_label': int,
            'max_label': int
        },
    }

class ShowMplsLabelRange(ShowMplsLabelRangeSchema):
    '''
    Parser for
    show mpls label range
    '''

    cli_command = 'show mpls label range'

    def cli(self,output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        p1 = re.compile(r'^Downstream Generic label region: Min/Max label: (?P<min_label>\d+)\/(?P<max_label>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            #Downstream Generic label region: Min/Max label: 16/983039
            m = p1.match(line)
            if m:
                group = m.groupdict()
                if 'downstream_generic_label_region' not in ret_dict:
                    downstream_generic_label_region = ret_dict.setdefault('downstream_generic_label_region',{})
                downstream_generic_label_region.update({
                    'min_label': int(group['min_label']),
                    'max_label': int(group['max_label'])})
                continue

        return ret_dict
