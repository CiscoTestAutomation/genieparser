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
"""
import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                               Any, \
                                               Optional


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
                # label_withraw_acks = True
                # label_request_acks = False

                temp_dict = statistic_dict.setdefault('label_withdraw_acks', {})
                continue

            # Address Withdraw Acks:
            m = p16.match(line)
            if m:
                # address_withraw_acks = True
                # label_withraw_acks = False
                # label_request_acks = False
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