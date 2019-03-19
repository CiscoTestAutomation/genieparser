# Python
import unittest
from unittest.mock import Mock
from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                             SchemaMissingKeyError

from genie.libs.parser.iosxe.show_mpls import ShowMplsLdpNsrStatistics

class test_show_mpls_ldp_nsr_statistics(unittest.TestCase):
    dev = Device(name='dev1')
    empty_output = {'execute.return_value': ' '}

    golden_parsed_output = {
           'statistics': {
               'peer': {
                   '106.162.197.252': {
                       'local_space_id':{
                           0: {
                               'in_label_request_records':{
                                   'created': 0,
                                   'freed': 0,
                               },
                               'in_label_withdraw_records': {
                                   'created': 0,
                                   'freed': 0,
                               },
                               'local_address_withdraw': {
                                   'set': 0,
                                   'cleared': 0,
                               },
                               'transmit_contexts': {
                                   'enqueued': 0,
                                   'dequeued': 0,
                               },
                           }
                       }
                   },
                   '106.162.197.253': {
                       'local_space_id': {
                           0: {
                               'in_label_request_records': {
                                   'created': 0,
                                   'freed': 0,
                               },
                               'in_label_withdraw_records': {
                                   'created': 0,
                                   'freed': 0,
                               },
                               'local_address_withdraw': {
                                   'set': 0,
                                   'cleared': 0,
                               },
                               'transmit_contexts': {
                                   'enqueued': 0,
                                   'dequeued': 0,
                               },
                           }
                       }
                   },
               },
               'total_in_label_request_records': {
                   'created': 0,
                   'freed': 0,
               },
               'total_in_label_withdraw_records': {
                   'created': 0,
                   'freed': 0,
               },
               'total_local_address_withdraw_records': {
                   'created': 0,
                   'freed': 0,
               },
               'label_request_acks': {
                   'number_of_chkpt_messages':{
                       'sent': 0,
                       'in_queue': 0,
                       'in_state_none': 0,
                       'in_state_send': 0,
                       'in_state_wait': 0,
                   },
               },
               'label_withdraw_acks': {
                   'number_of_chkpt_messages': {
                       'sent': 0,
                       'in_queue': 0,
                       'in_state_none': 0,
                       'in_state_send': 0,
                       'in_state_wait': 0,
                   },
               },
               'address_withdraw_acks': {
                   'number_of_chkpt_messages': {
                       'sent': 0,
                       'in_queue': 0,
                       'in_state_none': 0,
                       'in_state_send': 0,
                       'in_state_wait': 0,
                   },
               },
               'session_sync':{
                    'number_of_session_sync_msg_sent': 0,
                    'number_of_address_records_created': 0,
                    'number_of_address_records_freed': 0,
                    'number_of_dup_address_records_created': 0,
                    'number_of_dup_address_records_freed': 0,
                    'number_of_remote_binding_records_created': 0,
                    'number_of_remote_binding_records_freed': 0,
                    'number_of_capability_records_created': 0,
                    'number_of_capability_records_freed': 0,
                    'number_of_addr_msg_in_state_none': 0,
                    'number_of_dup_addr_msg_in_state_none': 0,
                    'number_of_remote_binding_msg_in_state_none': 0,
                    'number_of_capability_msg_in_state_none': 0,
                    'number_of_addr_msg_in_state_send': 0,
                    'number_of_dup_addr_msg_in_state_send': 0,
                    'number_of_remote_binding_msg_in_state_send': 0,
                    'number_of_capability_msg_in_state_send': 0,
                    'number_of_addr_msg_in_state_wait': 0,
                    'number_of_dup_addr_msg_in_state_wait': 0,
                    'number_of_remote_binding_msg_in_state_wait': 0,
                    'number_of_capability_msg_in_state_wait': 0,
                    'number_of_sync_done_msg_sent': 0,

               }
           }
    }

    golden_output = {'execute.return_value': '''\
    Router#show mpls ldp nsr statistics
    Load for five secs: 2%/0%; one minute: 5%; five minutes: 5%
    Time source is NTP, 16:10:12.625 JST Tue Nov 8 2016

    Peer: 106.162.197.252:0
      In label Request Records created: 0, freed: 0
      In label Withdraw Records created: 0, freed: 0
      Local Address Withdraw Set: 0, Cleared: 0
      Transmit contexts enqueued: 0, dequeued: 0
    Peer: 106.162.197.253:0
      In label Request Records created: 0, freed: 0
      In label Withdraw Records created: 0, freed: 0
      Local Address Withdraw Set: 0, Cleared: 0
      Transmit contexts enqueued: 0, dequeued: 0
    Total In label Request Records created: 0, freed: 0
    Total In label Withdraw Records created: 0, freed: 0
    Total Local Address Withdraw Records created: 0, freed: 0
    Label Request Acks:
      Number of chkpt msg sent: 0
      Number of chkpt msg in queue: 0
      Number of chkpt msg in state none: 0
      Number of chkpt msg in state send: 0
      Number of chkpt msg in state wait: 0
    Label Withdraw Acks:
      Number of chkpt msg sent: 0
      Number of chkpt msg in queue: 0
      Number of chkpt msg in state none: 0
      Number of chkpt msg in state send: 0
      Number of chkpt msg in state wait: 0
    Address Withdraw Acks:
      Number of chkpt msg sent: 0
      Number of chkpt msg in queue: 0
      Number of chkpt msg in state none: 0
      Number of chkpt msg in state send: 0
      Number of chkpt msg in state wait: 0
    Session Sync:
      Number of session-sync msg sent: 0
      Number of address records created: 0
      Number of address records freed: 0
      Number of dup-address records created: 0
      Number of dup-address records freed: 0
      Number of remote binding records created: 0
      Number of remote binding records freed: 0
      Number of capability records created: 0
      Number of capability records freed: 0
      Number of addr msg in state none: 0
      Number of dup-addr msg in state none: 0
      Number of remote binding msg in state none: 0
      Number of capability msg in state none: 0
      Number of addr msg in state send: 0
      Number of dup-addr msg in state send: 0
      Number of remote binding msg in state send: 0
      Number of capability msg in state send: 0
      Number of addr msg in state wait: 0
      Number of dup-addr msg in state wait: 0
      Number of remote binding msg in state wait: 0
      Number of capability msg in state wait: 0
      Number of sync-done msg sent: 0

    '''       }

    def test_empty(self):
        self.dev = Mock(**self.empty_output)
        obj = ShowMplsLdpNsrStatistics(device=self.dev)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output)
        obj = ShowMplsLdpNsrStatistics(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

if __name__ == '__main__':
    unittest.main()