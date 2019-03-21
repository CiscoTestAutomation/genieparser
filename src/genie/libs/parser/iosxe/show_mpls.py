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
        *  show mpls forwarding-table detail
        *  show mpls forwarding-table vrf <vrf>
        *  show mpls forwarding-table vrf <vrf> detail
        *  show mpls interfaces
        *  show mpls interfaces <interface>
        *  show mpls interfaces <interface> detail
        *  show mpls interfaces detail
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
        'ldp_featureset_manager': {
            Any(): {
                'ldp_features': list,
            }
        },
        'ldp_backoff': {
            'initial': int,
            'maximum': int,
        },
        'ldp_loop_detection': str,
        'ldp_nsr': str,
        'version': int,
        'session_hold_time': int,
        'keep_alive_interval': int,
        'ldp_for_targeted_sessions': bool,
        'discovery_targeted_hello': {
            'holdtime': int,
            'interval': int,
        },
        'discovery_hello': {
            'holdtime': int,
            'interval': int,
        },
        'downstream_on_demand_max_hop_count': int,
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
                ldp_dict = result_dict
                ldp_feature_dict = ldp_dict.setdefault('ldp_featureset_manager', {}).setdefault('State Initialized', {})
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
                ldp_dict.update({'version': int(group['version'])})
                continue

            # Session hold time: 180 sec; keep alive interval: 60 sec
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ldp_feature_flag = False
                ldp_dict.update({'session_hold_time': int(group['session_holdtime'])})
                ldp_dict.update({'keep_alive_interval': int(group['keepalive_interval'])})
                continue

            # Discovery hello: holdtime: 15 sec; interval: 5 sec
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ldp_feature_flag = False
                discovery_hello = ldp_dict.setdefault('discovery_hello', {})
                discovery_hello.update({'holdtime': int(group['holdtime'])})
                discovery_hello.update({'interval': int(group['interval'])})
                continue

            # Discovery targeted hello: holdtime: 90 sec; interval: 10 sec
            m = p6.match(line)
            if m:
                group = m.groupdict()
                ldp_feature_flag = False
                discovery_targeted_hello = ldp_dict.setdefault('discovery_targeted_hello', {})
                discovery_targeted_hello.update({'holdtime': int(group['targeted_holdtime'])})
                discovery_targeted_hello.update({'interval': int(group['targeted_interval'])})
                continue

            # Downstream on Demand max hop count: 255
            m = p7.match(line)
            if m:
                group = m.groupdict()
                ldp_feature_flag = False
                ldp_dict.update({'downstream_on_demand_max_hop_count': int(group['maxhop_count'])})
                continue

            # LDP for targeted sessions
            m = p8.match(line)
            if m:
                ldp_feature_flag = False
                ldp_dict.update({'ldp_for_targeted_sessions': True})
                continue

            # LDP initial/maximum backoff: 15/120 sec
            m = p9.match(line)
            if m:
                group = m.groupdict()
                ldp_feature_flag = False
                backoff_dict = ldp_dict.setdefault('ldp_backoff', {})
                backoff_dict.update({'initial': int(group['initial'])})
                backoff_dict.update({'maximum': int(group['maximum'])})
                continue

            # LDP loop detection: off
            m = p10.match(line)
            if m:
                group = m.groupdict()
                ldp_feature_flag = False
                ldp_dict.update({'ldp_loop_detection': group['loop_detection']})
                continue

            # LDP NSR: Disabled
            m = p11.match(line)
            if m:
                group = m.groupdict()
                ldp_feature_flag = False
                ldp_dict.update({'ldp_nsr': group['nsr'].lower()})
                continue

        return result_dict


class ShowMplsLdpNsrStatisticsSchema(MetaParser):
    """Schema for show mpls ldp nsr statistics"""
    schema = {
        'statistics': {
            'peer': {
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

        # Peer: 106.162.197.253:0
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

            # Peer: 106.162.197.253:0
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


class ShowMplsLdpParametersSchema(MetaParser):
    """Schema for show mpls ldp Parameters"""

    schema = {
        'ldp_featureset_manager': {
            Any(): {
                'ldp_features': list,
            }
        },
        'ldp_backoff': {
            'initial': int,
            'maximum': int,
        },
        'ldp_loop_detection': str,
        'ldp_nsr': str,
        'version': int,
        'session_hold_time': int,
        'keep_alive_interval': int,
        'ldp_for_targeted_sessions': bool,
        'discovery_targeted_hello': {
            'holdtime': int,
            'interval': int,
        },
        'discovery_hello': {
            'holdtime': int,
            'interval': int,
        },
        'downstream_on_demand_max_hop_count': int,
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
                ldp_dict = result_dict
                ldp_feature_dict = ldp_dict.setdefault('ldp_featureset_manager', {}).setdefault('State Initialized', {})
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
                ldp_dict.update({'version': int(group['version'])})
                continue

            # Session hold time: 180 sec; keep alive interval: 60 sec
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ldp_feature_flag = False
                ldp_dict.update({'session_hold_time': int(group['session_holdtime'])})
                ldp_dict.update({'keep_alive_interval': int(group['keepalive_interval'])})
                continue

            # Discovery hello: holdtime: 15 sec; interval: 5 sec
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ldp_feature_flag = False
                discovery_hello = ldp_dict.setdefault('discovery_hello', {})
                discovery_hello.update({'holdtime': int(group['holdtime'])})
                discovery_hello.update({'interval': int(group['interval'])})
                continue

            # Discovery targeted hello: holdtime: 90 sec; interval: 10 sec
            m = p6.match(line)
            if m:
                group = m.groupdict()
                ldp_feature_flag = False
                discovery_targeted_hello = ldp_dict.setdefault('discovery_targeted_hello', {})
                discovery_targeted_hello.update({'holdtime': int(group['targeted_holdtime'])})
                discovery_targeted_hello.update({'interval': int(group['targeted_interval'])})
                continue

            # Downstream on Demand max hop count: 255
            m = p7.match(line)
            if m:
                group = m.groupdict()
                ldp_feature_flag = False
                ldp_dict.update({'downstream_on_demand_max_hop_count': int(group['maxhop_count'])})
                continue

            # LDP for targeted sessions
            m = p8.match(line)
            if m:
                ldp_feature_flag = False
                ldp_dict.update({'ldp_for_targeted_sessions': True})
                continue

            # LDP initial/maximum backoff: 15/120 sec
            m = p9.match(line)
            if m:
                group = m.groupdict()
                ldp_feature_flag = False
                backoff_dict = ldp_dict.setdefault('ldp_backoff', {})
                backoff_dict.update({'initial': int(group['initial'])})
                backoff_dict.update({'maximum': int(group['maximum'])})
                continue

            # LDP loop detection: off
            m = p10.match(line)
            if m:
                group = m.groupdict()
                ldp_feature_flag = False
                ldp_dict.update({'ldp_loop_detection': group['loop_detection']})
                continue

            # LDP NSR: Disabled
            m = p11.match(line)
            if m:
                group = m.groupdict()
                ldp_feature_flag = False
                ldp_dict.update({'ldp_nsr': group['nsr'].lower()})
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
                                'uptime': str,
                                Optional('peer_holdtime_ms'): str,
                                Optional('ka_interval_ms'): str,
                                Optional('peer_state'): str,
                                'ldp_discovery_sources': {
                                    'interface':{
                                          Any():{
                                          'ip_address': {
                                              Any(): {
                                                  Optional('holdtime_ms'): int,
                                                  Optional('hello_interval_ms'): int,
                                              }
                                          }
                                        }
                                    }
                                },
                                'address_bound': list,
                                Optional('nsr'): str,
                                Optional('capabilities'):{
                                     'sent': {
                                         'ICCP':{
                                            'type': str,
                                            'maj_ver': int,
                                            'min_ver': int,
                                         },
                                        'dynamic_anouncement': str,
                                        'mldp_point_to_multipoint': str,
                                        'mldp_multipoint_to_multipoint': str,
                                        'typed_wildcard': str,
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

    def cli(self, vrf="",cmd="",output=None):
        if output is None:
            if not cmd:
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
        p1 = re.compile(r'^Peer +LDP +Ident: +(?P<peer_ldp>[\d\.]+):(?P<label_space_id>\d+); +Local +LDP +Ident +(?P<local_ldp>\S+)$')

        #     TCP connection: 10.169.197.252.646 - 10.169.197.254.20170
        p2 = re.compile(r'^TCP +connection: +(?P<tcp_connection>[\S\s]+)$')

        #     State: Oper; Msgs sent/rcvd: 824/825; Downstream
        #     State: Oper; Msgs sent/rcvd: 824/825; Downstream; Last TIB rev sent 4103
        p3 = re.compile(r'^State: +(?P<state>\w+); +Msgs +sent\/rcvd: +(?P<msg_sent>\d+)\/(?P<msg_rcvd>\d+);'
                                ' +(?P<downstream>\w+)(; +Last +TIB +rev +sent +(?P<last_tib_rev_sent>\d+))?$')

        #  Up time: 04:26:14
        #  Up time: 3d21h; UID: 4; Peer Id 0
        p4 = re.compile(r'^Up +time: +(?P<up_time>[\w\:]+)(; +UID: (?P<uid>\d+); +Peer +Id +(?P<peer_id>\d+))?$')

        #     LDP discovery sources:
        #       GigabitEthernet0/0/0, Src IP addr: 10.169.197.93
        p5 = re.compile(r'^(?P<interface>[\S]+)(,|;) +Src +IP +addr: +(?P<src_ip_address>[\d\.]+)$')

        #       holdtime: 15000 ms, hello interval: 5000 ms
        p5_1 = re.compile(r'^holdtime: +(?P<holdtime>\d+) +ms, +hello +interval: +(?P<hello_interval>\d+) +ms$')

        #     Addresses bound to peer LDP Ident:
        p6 = re.compile(r'^Addresses +bound +to +peer +LDP +Ident:$')

        #       10.169.197.252 10.120.202.49    10.169.197.101 10.16.190.254
        p7 = re.compile(r'^(?P<address_bound_peer_ldp>[\d\.\s]+)$')

        # Peer holdtime: 180000 ms; KA interval: 60000 ms; Peer state: estab
        p8 = re.compile(r'^Peer +holdtime: +(?P<peer_holdtime>\d+) +ms, +KA +interval: +(?P<ka_interval>\d+) +ms;'
                         ' +Peer +state +(?P<peer_state>\S+)$')

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

    def cli(self, vrf="", cmd ="",output=None):
        return super().cli(cmd=self.cli_command,vrf=vrf,output=output)


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
        # lib entry: 10.120.202.64/32, rev 12, chkpt: none
        p1 = re.compile(r'^lib +entry: +(?P<lib_entry>[\d\.\/]+), +rev +(?P<rev>\d+)(, +chkpt: +(?P<checkpoint>\S+))?$')

        #  local binding:  label: 2536
        #  local binding:  label: 2027 (owner LDP)
        p2 = re.compile(r'^local +binding:  +label: +(?P<local_label>\S+)( +\(owner +(?P<owner>\w+)\))?$')

        #  Advertised to:
        # 10.169.197.252:0      10.169.197.253:0
        p3 = re.compile(r'^(?P<advertised_to>[\d\.\:\s]+)$')

        #  remote binding: lsr: 10.169.197.252:0, label: 508
        #  remote binding: lsr: 10.169.197.253:0, label: 308016 checkpointed
        p4 = re.compile(r'^remote +binding: +lsr: +(?P<lsr>[\d\.]+):(?P<label_space_id>[\d]+),'
                        ' +label: +(?P<remote_label>\S+)( +(?P<checkpointed>\w+))?$')


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
            'dynamic_anouncement': str,
            Optional('mldp_point_to_multipoint'): str,
            Optional('mldp_multipoint_to_multipoint'): str,
            'typed_wildcard': str,

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
                'local_ldp_identifier': {
                    Any(): {
                        'discovery_sources': {
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
                    if detail:
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
        p1 = re.compile(r'^(VRF +(?P<vrf>\S+):)?Local +LDP +Identifier:$')

        # 10.169.197.254:0
        p2 = re.compile(r'^(?P<local_ldp_identifier>[\d\.\:]+)$')
        # Discovery Sources:
        p2_1 = re.compile(r'^Discovery +Sources:$')

        #     GigabitEthernet0/0/0 (ldp): xmit/recv
        #     ATM1/1/0.1 (tdp):xmit/recv
        p3 = re.compile(r'^(?P<interface>\S+) +\((?P<session>[\w]+)\):(?P<space>\s{1})?xmit\/recv$')

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
        p12 = re.compile(r'^(?P<source>[\d\.]+) +\-> +(?P<destination>[\d\.]+)'
                         ' +\((?P<session>(ldp|tdp)+)\): +(?P<status>(active|passive)+), +xmit\/recv$')

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
                interface_dict = local_ldp_identifier_dict.setdefault('discovery_sources', {}) \
                    .setdefault('interfaces', {}) \
                    .setdefault(group['interface'], {})
                interface_dict.update({'session': group['session']})
                interface_dict.update({'xmit': True})
                interface_dict.update({'recv': True})
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
            m = p12.match(line)
            if m:
                group = m.groupdict()
                targeted_dict = local_ldp_identifier_dict.setdefault('targeted_hellos', {}). \
                    setdefault(group['source'], {}). \
                    setdefault(group['destination'], {})
                targeted_dict.update({'session': group['session'].lower()})
                targeted_dict.update({'xmit': True})
                targeted_dict.update({'recv': True})
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
        p2 = re.compile(r'^LDP +configured; +(LDP\-IGP +Synchronization( +(?P<state>\w+))?'
                        ' +(?P<synchronization_enabled>(enabled)+))?(SYNC +(?P<enabled>\w+))?.$')

        #     Sync status: sync achieved; peer reachable.
        p3 = re.compile(r'^(Sync|SYNC) +status: +sync +achieved; +peer +reachable.$')

        #     Sync delay time: 0 seconds (0 seconds left)
        p4 = re.compile(r'^Sync +delay +time: +(?P<delay_time>\d+) +seconds \((?P<left_time>\d+) +seconds +left\)$')

        #     IGP holddown time: infinite.
        p5 = re.compile(r'^IGP +holddown +time: +(?P<holddown_time>\w+).?$')

        #     Peer LDP Ident: 106.162.197.252:0
        p6 = re.compile(r'^Peer +LDP +Ident: +(?P<peer_ldp_ident>\S+).?$')

        #     IGP enabled: OSPF 9996
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
            #   LDP configured; LDP-IGP Synchronization not enabled.
            #   LDP configured;  SYNC enabled.
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ldp_dict = interface_dict.setdefault('ldp', {})
                if group['state']:
                    ldp_dict.update({'igp_synchronization_enabled': False})
                else:
                    if not group['synchronization_enabled']:
                        ldp_dict.update({'igp_synchronization_enabled': False})
                    if group['synchronization_enabled']:
                        ldp_dict.update({'igp_synchronization_enabled': True})

                if group['enabled']:
                    enabled_dict = interface_dict.setdefault('sync', {}).setdefault('status', {})
                    enabled_dict.update({'enabled': True})

                ldp_dict.update({'configured': True})
                continue

            # Sync status: sync achieved; peer reachable.
            m = p3.match(line)
            if m:
                sync_dict = interface_dict.setdefault('sync', {})
                sync_status_dict = sync_dict.setdefault('status', {})
                sync_status_dict.update({'sync_achieved': True})
                sync_status_dict.update({'peer_reachable': True})
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

            # Peer LDP Ident: 106.162.197.252:0
            m = p6.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({'peer_ldp_ident': group['peer_ldp_ident']})
                continue

            # IGP enabled: OSPF 9996
            m = p7.match(line)
            if m:
                group = m.groupdict()
                igp_dict.update({'enabled': group['igp_enabled'].lower()})
                continue

        return result_dict



class ShowMplsForwardingTableSchema(MetaParser):
    """Schema for
        show mpls forwarding-table
        show mpls forwarding-table detail
        show mpls forwarding-table vrf <vrf>
        show mpls forwarding-table vrf <vrf> detail"""

    schema = {
        'vrf':{
            Any(): {
                'interfaces': {
                    Any(): {
                        Any():{
                            'outgoing_label': str,
                            'prefix_or_tunnel_id': str,
                            'bytes_label_switched': int,
                            Optional('next_hop'): str,
                            'mac': int,
                            Optional('code'): str,
                            'encaps': int,
                            'mru': int,
                            'label_stack': str,
                            'vpn_route': str,
                            'output_feature_configured': bool,
                            Optional('pre_destination'): str,
                            Optional('slots'): list,
                        }
                    }
                }
            }
        }
    }

class ShowMplsForwardingTable(ShowMplsForwardingTableSchema):
    """Parser for
        show mpls forwarding-table
        show mpls forwarding-table detail
        show mpls forwarding-table vrf <vrf>
        show mpls forwarding-table vrf <vrf> detail"""

    cli_command = ['show mpls forwarding-table','show mpls forwarding-table detail',
                   'show mpls forwarding-table vrf {vrf}','show mpls forwarding-table vrf {vrf} detail']

    def cli(self, vrf="",detail="", output=None):
        if output is None:
            if vrf:
                if detail:
                    cmd = self.cli_command[3].format(vrf=vrf)
                else:
                    cmd = self.cli_command[2].format(vrf=vrf)
            else:
                if detail:
                    cmd = self.cli_command[1]
                else:
                    cmd = self.cli_command[0]

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
        p1 = re.compile(r'^(?P<local_label>\d+) +(?P<outgoing_label>[\w\s]+) +(?P<prefix_or_tunnel_id>\S +\\$')
        P2 = re.compile(r'^(?P<bytes_label_switched>\d+) +(?P<interface>\S+)( +(?P<next_hop>[\d\.]+))?$')
        # p2 = re.compile(r'^(?P<local_label>\d+) +(?P<outgoing_label>[\w\s]+) +(?P<prefix_or_tunnel_id>\S+)'
        #     ' +(?P<bytes_label_switched>\d+) +(?P<interface>\S+)( +(?P<next_hop>[\d\.]+))?$')
        #         MAC/Encaps=18/18, MRU=1530, Label Stack{}
        p3 = re.compile(r'^MAC/Encaps=(?P<mac>\d+)/(?P<encaps>\d+), +MRU=(?P<mru>[\d]+), +Label +Stack(?P<label_stack>[\S\s]+)$')
        #         00002440156384B261CB1480810000330800
        p4 = re.compile(r'^(?P<code>[0-9A-F]+)$')
        #         VPN route: L3VPN-0051
        p5 = re.compile(r'^VPN +route: +(?P<vpn_route>\S+)$')
        #         No output feature configured
        p6 = re.compile(r'^No +output +feature +configured$')
        #     Per-destination load-sharing, slots: 0 2 4 6 8 10 12 14
        p7 = re.compile(r'^Per\-destination +(?P<pre_destination>[\S\s]+), +slots: +(?P<slots>[\d\s]+)$')

        for line in out.splitlines():
            line = line.strip()

            # 9301       No Label   172.16.100.1/32[V]   \
            #
            #                                       0             Po1.51     192.168.10.253
            m = p1.match(line)
            if m:
                group = m.groupdict()
                local_label = int(group['local_label'])
                outgoing_label = group['outgoing_label']
                prefix_or_tunnel_id = group['prefix_or_tunnel_id']
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                # local_label = int(group['local_label'])
                # outgoing_label = group['outgoing_label']
                # prefix_or_tunnel_id = group['prefix_or_tunnel_id']
                interface = Common.convert_intf_name(group['interface'])
                feature_dict = result_dict.setdefault('vrf', {}).setdefault(vrf, {}). \
                                           setdefault('interfaces', {}).\
                                           setdefault(interface, {}).setdefault(local_label,{})

                feature_dict.update({'outgoing_label': outgoing_label.strip()})
                feature_dict.update({'prefix_or_tunnel_id': prefix_or_tunnel_id})
                if group['next_hop']:
                    feature_dict.update({'next_hop': group['next_hop']})
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
                continue

            #     00002440156384B261CB1480810000330800
            m = p4.match(line)
            if m:
                group = m.groupdict()
                feature_dict.update({'code': group['code']})
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
                feature_dict.update({'pre_destination': group['pre_destination']})
                feature_dict.update({'slots': group['slots'].split()})
                continue

        return result_dict

class ShowMplsInterfaceSchema(MetaParser):
    """Schema for
        show mpls interfaces
        show mpls interfaces detail"""

    schema = {
        'interfaces': {
            Any(): {
                Optional('ip'): str,
                Optional('tunnel'): str,
                Optional('bgp'): str,
                Optional('static'): str,
                Optional('operational'): str,
                Optional('type'): str,
                'session': str,
                Optional('ip_labeling_enabled'): str,
                Optional('lsp_tunnel_labeling_enabled'): bool,
                Optional('lp_frr_labeling_enabled'): bool,
                Optional('bgp_labeling_enabled'): bool,
                Optional('mpls'): str,
                Optional('mtu'): int,
            }
        }
    }


class ShowMplsInterface(ShowMplsInterfaceSchema):
    """Parser for
        show mpls interfaces
        show mpls interfaces <interface> detail
        show mpls interfaces detail"""

    cli_command = ['show mpls interfaces',
                   'show mpls interfaces detail',
                   'show mpls interfaces {interface} detail',
                   'show mpls interfaces {interface}']

    def cli(self, detail="", interface="", output=None):
        if output is None:
            if detail:
                if interface:
                    cmd = self.cli_command[2].format(interface=interface)
                else:
                    cmd = self.cli_command[1]
            else:
                if interface:
                    cmd = self.cli_command[3].format(interface=interface)
                else:
                    cmd = self.cli_command[0]

            out = self.device.execute(cmd)
        else:
            out = output

        # initial return dictionary
        result_dict = {}

        # Interface              IP            Tunnel   BGP Static Operational
        # GigabitEthernet6       Yes (ldp)     No       No  No     Yes
        p1 = re.compile(r'^(?P<interface>\S+) +(?P<ip>\w+) +\((?P<session>\w+)\) +(?P<tunnel>\w+)'
                        ' +(?P<bgp>\w+) +(?P<static>\w+) +(?P<operational>\w+)$')
        # Interface GigabitEthernet0/0/0:
        p2 = re.compile(r'^Interface +(?P<interface>\S+):$')
        #     Type Unknown
        p3 = re.compile(r'^Type +(?P<type>\w+)$')
        #     IP labeling enabled (ldp) :
        p4 = re.compile(r'^IP +labeling +enabled \(+(?P<session>\w+)\) +\:$')
        #       Interface config
        p5 = re.compile(r'^Interface +config$')
        #     LSP Tunnel labeling not enabled
        p6 = re.compile(r'^LSP +Tunnel +labeling +((?P<lsp_tunnel_enabled>\w+) )?enabled$')
        #     IP FRR labeling not enabled
        p7 = re.compile(r'^IP +FRR +labeling +((?P<lp_frr_labeling>\w+) )?enabled$')
        #     BGP labeling not enabled
        p8 = re.compile(r'^BGP +labeling +((?P<bgp_labeling>\w+) )?enabled$')
        #     MPLS operational
        p9 = re.compile(r'^MPLS +(?P<mpls_status>\w+)$')
        #     MTU = 1552
        p10 = re.compile(r'^MTU \= +(?P<mtu>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            # Interface              IP            Tunnel   BGP Static Operational
            # GigabitEthernet6       Yes (ldp)     No       No  No     Yes
            m = p1.match(line)
            if m:
                group = m.groupdict()
                interface_dict = result_dict.setdefault('interfaces', {}).setdefault(group['interface'], {})
                interface_dict.update({'ip': group['ip'].lower()})
                interface_dict.update({'tunnel': group['tunnel'].lower()})
                interface_dict.update({'bgp': group['bgp'].lower()})
                interface_dict.update({'static': group['static'].lower()})
                interface_dict.update({'session': group['session']})
                interface_dict.update({'operational': group['operational'].lower()})
                continue

            # Interface GigabitEthernet0/0/0:
            m = p2.match(line)
            if m:
                group = m.groupdict()
                interface_dict = result_dict.setdefault('interfaces', {}).setdefault(group['interface'], {})
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
                continue

            #     Interface config
            m = p5.match(line)
            if m:
                interface_dict.update({'ip_labeling_enabled': 'Interface config'})
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
                interface_dict.update({'mpls': group['mpls_status']})
                continue

            #     MTU = 1552
            m = p10.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({'mtu': int(group['mtu'])})
                continue

        return result_dict