# Python
import unittest
from unittest.mock import Mock
from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                             SchemaMissingKeyError

from genie.libs.parser.iosxe.show_mpls import ShowMplsLdpParameters,\
                                              ShowMplsLdpNsrStatistics,\
                                              ShowMplsLdpNeighbor,\
                                              ShowMplsLdpNeighborDetail,\
                                              ShowMplsLdpBindings,\
                                              ShowMplsLdpCapabilities,\
                                              ShowMplsLdpDiscovery,\
                                              ShowMplsLdpIgpSync,\
                                              ShowMplsForwardingTable,\
                                              ShowMplsInterface, \
                                              ShowMplsL2TransportDetail

class test_show_mpls_ldp_parameters(unittest.TestCase):
    dev1 = Device(name='empty')
    dev = Device(name='dev1')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'ldp_featureset_manager': {
            'State Initialized': {
                'ldp_features': [
                    'Auto-Configuration',
                    'Basic',
                    'ICPM',
                    'IP-over-MPLS',
                    'IGP-Sync',
                    'LLAF',
                    'TCP-MD5-Rollover',
                    'TDP',
                    'NSR'],
            },
        },
        'ldp_backoff': {
            'initial': 15,
            'maximum': 120,
        },
        'ldp_loop_detection': "off",
        'ldp_nsr': 'disabled',
        'ldp_for_targeted_sessions': True,
        'version': 1,
        'session_hold_time': 180,
        'keep_alive_interval': 60,
        'discovery_targeted_hello': {
            'holdtime': 90,
            'interval': 10,
        },
        'discovery_hello': {
            'holdtime': 15,
            'interval': 5,
        },
        'downstream_on_demand_max_hop_count': 255,
    }


    golden_output = {'execute.return_value': '''\

    Router#show mpls ldp parameters
    Load for five secs: 2%/0%; one minute: 5%; five minutes: 5%
    Time source is NTP, 16:10:10.454 JST Tue Nov 8 2016
    LDP Feature Set Manager: State Initialized
      LDP features:
        Auto-Configuration
        Basic
        ICPM
        IP-over-MPLS
        IGP-Sync
        LLAF
        TCP-MD5-Rollover
        TDP
        NSR
    Protocol version: 1
    Session hold time: 180 sec; keep alive interval: 60 sec
    Discovery hello: holdtime: 15 sec; interval: 5 sec
    Discovery targeted hello: holdtime: 90 sec; interval: 10 sec
    Downstream on Demand max hop count: 255
    LDP for targeted sessions
    LDP initial/maximum backoff: 15/120 sec
    LDP loop detection: off
    LDP NSR: Disabled
    Router#
    '''
    }

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowMplsLdpParameters(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output)
        obj = ShowMplsLdpParameters(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


class test_show_mpls_ldp_parameters(unittest.TestCase):
    dev1 = Device(name='empty')
    dev = Device(name='dev1')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'ldp_featureset_manager': {
            'State Initialized': {
                'ldp_features': [
                    'Auto-Configuration',
                    'Basic',
                    'ICPM',
                    'IP-over-MPLS',
                    'IGP-Sync',
                    'LLAF',
                    'TCP-MD5-Rollover',
                    'TDP',
                    'NSR'],
            },
        },
        'ldp_backoff': {
            'initial': 15,
            'maximum': 120,
        },
        'ldp_loop_detection': "off",
        'ldp_nsr': 'disabled',
        'ldp_for_targeted_sessions': True,
        'version': 1,
        'session_hold_time': 180,
        'keep_alive_interval': 60,
        'discovery_targeted_hello': {
            'holdtime': 90,
            'interval': 10,
        },
        'discovery_hello': {
            'holdtime': 15,
            'interval': 5,
        },
        'downstream_on_demand_max_hop_count': 255,
    }


    golden_output = {'execute.return_value': '''\

    Router#show mpls ldp parameters
    Load for five secs: 2%/0%; one minute: 5%; five minutes: 5%
    Time source is NTP, 16:10:10.454 JST Tue Nov 8 2016
    LDP Feature Set Manager: State Initialized
      LDP features:
        Auto-Configuration
        Basic
        ICPM
        IP-over-MPLS
        IGP-Sync
        LLAF
        TCP-MD5-Rollover
        TDP
        NSR
    Protocol version: 1
    Session hold time: 180 sec; keep alive interval: 60 sec
    Discovery hello: holdtime: 15 sec; interval: 5 sec
    Discovery targeted hello: holdtime: 90 sec; interval: 10 sec
    Downstream on Demand max hop count: 255
    LDP for targeted sessions
    LDP initial/maximum backoff: 15/120 sec
    LDP loop detection: off
    LDP NSR: Disabled
    Router#
    '''
    }

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowMplsLdpParameters(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output)
        obj = ShowMplsLdpParameters(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


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
        self.dev1 = Mock(**self.empty_output)
        obj = ShowMplsLdpParameters(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output)
        obj = ShowMplsLdpNsrStatistics(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


class test_show_mpls_ldp_neighbor(unittest.TestCase):
    dev1 = Device(name='empty')
    dev = Device(name='dev1')
    empty_output = {'execute.return_value': '      '}

    golden_parsed_output = {
        'vrf': {
            'default': {
                'peers': {
                    '10.169.197.252': {
                        'label_space_id': {
                            0: {
                                'address_bound': ['10.169.197.252',
                                                  '10.120.202.49',
                                                  '10.169.197.101',
                                                  '10.16.190.254',
                                                  '10.169.197.93'],
                                'downstream': True,
                                'ldp_discovery_sources': {
                                    'interface':{
                                        'GigabitEthernet0/0/0':{
                                            'ip_address': {
                                                '10.169.197.93': {},
                                            }
                                        }
                                    }
                                },
                                'local_ldp_ident': '10.169.197.254:0',
                                'msg_rcvd': 852,
                                'msg_sent': 851,
                                'state': 'oper',
                                'tcp_connection': "10.169.197.252.646 - 10.169.197.254.20170",
                                'uptime': '04:50:30'
                            },
                        },
                    },
                    '10.169.197.253': {
                        'label_space_id': {
                            0:{
                                'address_bound': ['10.186.1.2',
                                                  '10.120.202.57',
                                                  '10.169.197.97'],
                                'downstream': True,
                                'ldp_discovery_sources': {
                                    'interface': {
                                        'GigabitEthernet0/0/2':{
                                            'ip_address': {
                                                '10.169.197.97': {},
                                            },
                                        }
                                    },
                                },
                                'local_ldp_ident': '10.169.197.254:0',
                                'msg_rcvd': 306,
                                'msg_sent': 858,
                                'state': 'oper',
                                'tcp_connection': '10.169.197.253.646 - 10.169.197.254.42450',
                                'uptime': '04:50:30'
                            }
                        }
                    }
                }
            }
        }
    }

    golden_output = {'execute.return_value': '''\
    Router#show mpls ldp neighbor
Load for five secs: 59%/0%; one minute: 11%; five minutes: 7%
Time source is NTP, 20:53:42.709 JST Fri Nov 11 2016
    Peer LDP Ident: 10.169.197.252:0; Local LDP Ident 10.169.197.254:0
        TCP connection: 10.169.197.252.646 - 10.169.197.254.20170
        State: Oper; Msgs sent/rcvd: 851/852; Downstream
        Up time: 04:50:30
        LDP discovery sources:
          GigabitEthernet0/0/0, Src IP addr: 10.169.197.93
        Addresses bound to peer LDP Ident:
          10.169.197.252 10.120.202.49    10.169.197.101 10.16.190.254
          10.169.197.93
    Peer LDP Ident: 10.169.197.253:0; Local LDP Ident 10.169.197.254:0
        TCP connection: 10.169.197.253.646 - 10.169.197.254.42450
        State: Oper; Msgs sent/rcvd: 858/306; Downstream
        Up time: 04:50:30
        LDP discovery sources:
          GigabitEthernet0/0/2, Src IP addr: 10.169.197.97
        Addresses bound to peer LDP Ident:
          10.186.1.2        10.120.202.57    10.169.197.97
    '''
    }

    golden_parsed_output_vrf = {
    "vrf": {
        "vpn10": {
            "peers": {
                "10.19.14.14": {
                    'label_space_id': {
                        0:{
                            "local_ldp_ident": "10.166.0.2:0",
                            "msg_sent": 1423,
                            "downstream": True,
                            "address_bound": [
                                "10.36.36.9",
                                "10.94.0.1",
                                "10.19.14.14",
                                "10.64.0.1",
                                "10.240.0.1",
                                "10.169.0.1",
                                "10.106.0.1",
                                "10.51.0.1",
                                "10.4.0.1",
                                "10.220.0.1",
                                "10.189.0.1",
                                "10.166.0.1",
                                "10.151.0.1",
                                "10.144.0.1",
                                "10.145.0.1",
                                "10.154.0.1",
                                "10.171.0.1",
                                "10.196.0.1",
                                "10.229.0.1",
                                "10.15.0.1",
                                "10.64.0.1",
                                "10.121.0.1",
                                "10.186.0.1",
                                "10.4.0.1",
                                "10.85.0.1",
                                "10.174.0.1",
                                "10.16.0.1",
                                "10.121.0.1",
                                "10.234.0.1",
                                "10.100.0.1",
                                "10.229.0.1",
                                "10.111.0.1",
                                "10.1.0.1",
                                "10.154.0.1",
                                "10.60.0.1",
                                "10.229.0.1",
                                "10.151.0.1",
                                "10.81.0.1",
                                "10.19.0.1",
                                "10.220.0.1",
                                "10.174.0.1",
                                "10.136.0.1",
                                "10.106.0.1",
                                "10.84.0.1",
                                "10.70.0.1",
                                "10.64.0.1",
                                "10.66.0.1",
                                "10.76.0.1",
                                "10.94.0.1",
                                "10.120.0.1",
                                "10.154.0.1",
                                "10.196.0.1",
                                "10.136.0.2",
                                "10.69.0.2"
                            ],
                            "ldp_discovery_sources": {
                                "interface": {
                                    "ATM3/0/0.10":{
                                        "ip_address": {
                                            "10.19.14.10": {},
                                        }
                                    }
                                },
                            },
                            "msg_rcvd": 800,
                            "state": "oper",
                            "tcp_connection": "10.19.14.14.646 - 10.166.0.2.11384",
                            "uptime": "02:38:11"
                        }
                    }
                }
            }
        }
    }
}

    golden_output_vrf = {'execute.return_value': '''\
Router# show mpls ldp neighbor vrf vpn10

 Peer LDP Ident: 10.19.14.14:0; Local LDP Ident 10.166.0.2:0
         TCP connection: 10.19.14.14.646 - 10.166.0.2.11384
         State: Oper; Msgs sent/rcvd: 1423/800; Downstream
         Up time: 02:38:11
         LDP discovery sources:
           ATM3/0/0.10, Src IP addr: 10.19.14.10
         Addresses bound to peer LDP Ident:
           10.36.36.9        10.94.0.1        10.19.14.14     10.64.0.1
           10.240.0.1       10.169.0.1       10.106.0.1       10.51.0.1
           10.4.0.1       10.220.0.1       10.189.0.1       10.166.0.1
           10.151.0.1       10.144.0.1       10.145.0.1       10.154.0.1
           10.171.0.1       10.196.0.1       10.229.0.1       10.15.0.1
           10.64.0.1       10.121.0.1       10.186.0.1       10.4.0.1
           10.85.0.1       10.174.0.1       10.16.0.1       10.121.0.1
           10.234.0.1       10.100.0.1       10.229.0.1       10.111.0.1
           10.1.0.1       10.154.0.1       10.60.0.1       10.229.0.1
           10.151.0.1       10.81.0.1       10.19.0.1       10.220.0.1
           10.174.0.1       10.136.0.1       10.106.0.1       10.84.0.1
           10.70.0.1       10.64.0.1       10.66.0.1       10.76.0.1
           10.94.0.1      10.120.0.1      10.154.0.1      10.196.0.1
           10.136.0.2        10.69.0.2
 Router#
    '''
}
    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowMplsLdpNeighbor(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output)
        obj = ShowMplsLdpNeighbor(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_vrf(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output_vrf)
        obj = ShowMplsLdpNeighbor(device=self.dev)
        parsed_output = obj.parse(vrf="vpn10")
        self.assertEqual(parsed_output,self.golden_parsed_output_vrf)

class test_show_mpls_ldp_neighbor_detail(unittest.TestCase):
    dev1 = Device(name='empty')
    dev = Device(name='dev1')
    empty_output = {'execute.return_value': '      '}

    golden_parsed_output = {
    "vrf": {
        "default": {
            "peers": {
                "10.169.197.252": {
                    'label_space_id': {
                        0: {
                            "msg_sent": 9981,
                            "address_bound": [
                                "10.169.197.252",
                                "192.168.36.49",
                                "10.120.202.49",
                                "192.168.36.57",
                                "10.169.197.101",
                                "10.169.197.93",
                                "10.69.111.2",
                                "10.16.190.254"
                            ],
                            "nsr": "Not Ready",
                            "capabilities": {
                                "sent":{
                                    "ICCP":{
                                        "type": "0x0405",
                                        "maj_ver": 1,
                                        "min_ver": 0,
                                    },
                                    "typed_wildcard": "0x050B",
                                    "dynamic_anouncement": "0x0506",
                                    "mldp_point_to_multipoint": "0x0508",
                                    "mldp_multipoint_to_multipoint": "0x0509",
                                },
                                'received':{
                                    "ICCP": {
                                        "min_ver": 0,
                                        "type": "0x0405",
                                        "maj_ver": 1,
                                    },
                                    "typed_wildcard": "0x050B",
                                    "dynamic_anouncement": "0x0506",
                                    "mldp_point_to_multipoint": "0x0508",
                                    "mldp_multipoint_to_multipoint": "0x0509",
                                }
                            },
                            "local_ldp_ident": "10.169.197.254:0",
                            "password": "not required, none, in use",
                            "last_tib_rev_sent": 4103,
                            "ldp_discovery_sources": {
                                "interface":{
                                    "GigabitEthernet0/0/0":{
                                        "ip_address": {
                                            "10.169.197.93": {
                                                "holdtime_ms": 15000,
                                                "hello_interval_ms": 5000
                                            }
                                        },
                                    }
                                }
                            },
                            "downstream": True,
                            "msg_rcvd": 10004,
                            "tcp_connection": "10.169.197.252.646 - 10.169.197.254.44315",
                            "state": "oper",
                            "uptime": "3d21h"
                        }
                    }
                },
                "10.169.197.253": {
                    'label_space_id': {
                        0: {
                            "msg_sent": 9966,
                            "address_bound": [
                                "10.120.202.57",
                                "10.169.197.97"
                            ],
                            "nsr": "Not Ready",
                            "capabilities": {
                                "sent": {
                                    "ICCP":{
                                        "min_ver": 0,
                                        "maj_ver": 1,
                                        "type": "0x0405"
                                    },
                                    "typed_wildcard": "0x050B",
                                    "dynamic_anouncement": "0x0506",
                                    "mldp_point_to_multipoint": "0x0508",
                                    "mldp_multipoint_to_multipoint": "0x0509",
                                },
                            },
                            "local_ldp_ident": "10.169.197.254:0",
                            "password": "not required, none, in use",
                            "last_tib_rev_sent": 4103,
                            "ldp_discovery_sources": {
                                "interface":{
                                    "GigabitEthernet0/0/2":{
                                        "ip_address": {
                                            "10.169.197.97": {
                                                "holdtime_ms": 15000,
                                                "hello_interval_ms": 5000
                                            },
                                        },
                                    }
                                },
                            },
                            "downstream": True,
                            "msg_rcvd": 9153,
                            "tcp_connection": "10.169.197.253.646 - 10.169.197.254.34904",
                            "state": "oper",
                            "uptime": "3d21h"
                        }
                    }
                }
            }
        }
    }
}

    golden_output = {'execute.return_value': '''\
    Router#show mpls ldp neighbor detail
    Load for five secs: 2%/0%; one minute: 5%; five minutes: 5%
    Time source is NTP, 16:10:10.569 JST Tue Nov 8 2016
        Peer LDP Ident: 10.169.197.252:0; Local LDP Ident 10.169.197.254:0
            TCP connection: 10.169.197.252.646 - 10.169.197.254.44315
            Password: not required, none, in use
            State: Oper; Msgs sent/rcvd: 9981/10004; Downstream; Last TIB rev sent 4103
            Up time: 3d21h; UID: 4; Peer Id 0
            LDP discovery sources:
              GigabitEthernet0/0/0; Src IP addr: 10.169.197.93
                holdtime: 15000 ms, hello interval: 5000 ms
            Addresses bound to peer LDP Ident:
              10.169.197.252 192.168.36.49  10.120.202.49    192.168.36.57
              10.169.197.101 10.169.197.93  10.69.111.2   10.16.190.254
            Peer holdtime: 180000 ms; KA interval: 60000 ms; Peer state: estab
            NSR: Not Ready
            Capabilities Sent:
              [ICCP (type 0x0405) MajVer 1 MinVer 0]
              [Dynamic Announcement (0x0506)]
              [mLDP Point-to-Multipoint (0x0508)]
              [mLDP Multipoint-to-Multipoint (0x0509)]
              [Typed Wildcard (0x050B)]
            Capabilities Received:
              [ICCP (type 0x0405) MajVer 1 MinVer 0]
              [Dynamic Announcement (0x0506)]
              [mLDP Point-to-Multipoint (0x0508)]
              [mLDP Multipoint-to-Multipoint (0x0509)]
              [Typed Wildcard (0x050B)]
        Peer LDP Ident: 10.169.197.253:0; Local LDP Ident 10.169.197.254:0
            TCP connection: 10.169.197.253.646 - 10.169.197.254.34904
            Password: not required, none, in use
            State: Oper; Msgs sent/rcvd: 9966/9153; Downstream; Last TIB rev sent 4103
            Up time: 3d21h; UID: 5; Peer Id 1
            LDP discovery sources:
              GigabitEthernet0/0/2; Src IP addr: 10.169.197.97
                holdtime: 15000 ms, hello interval: 5000 ms
            Addresses bound to peer LDP Ident:
              10.120.202.57    10.169.197.97
            Peer holdtime: 180000 ms; KA interval: 60000 ms; Peer state: estab
            NSR: Not Ready
            Capabilities Sent:
              [ICCP (type 0x0405) MajVer 1 MinVer 0]
              [Dynamic Announcement (0x0506)]
              [mLDP Point-to-Multipoint (0x0508)]
              [mLDP Multipoint-to-Multipoint (0x0509)]
              [Typed Wildcard (0x050B)]
            Capabilities Received:
              [None]
        '''}

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowMplsLdpNeighborDetail(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output)
        obj = ShowMplsLdpNeighborDetail(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

class test_show_mpls_ldp_bindings(unittest.TestCase):
    dev1 = Device(name='empty')
    dev = Device(name='dev1')
    empty_output = {'execute.return_value': '      '}

    golden_parsed_output = {
            "vrf": {
                "default": {
                    "lib_entry": {
                        "10.120.202.48/30": {
                            "rev": "1034",
                            "label_binding": {
                                "label": {
                                    "2539": {}
                                }
                            },
                            "remote_binding": {
                                "label": {
                                    "imp-null": {
                                        "lsr_id": {
                                            "10.169.197.252": {
                                                "label_space_id": {
                                                    0: {}
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        "10.169.197.96/30": {
                            "rev": "4",
                            "label_binding": {
                                "label": {
                                    "imp-null": {}
                                }
                            },
                            "remote_binding": {
                                "label": {
                                    "1002": {
                                        "lsr_id": {
                                            "10.169.197.252": {
                                                "label_space_id": {
                                                    0: {}
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        "10.120.202.56/30": {
                            "rev": "1024",
                            "label_binding": {
                                "label": {
                                    "2534": {}
                                }
                            },
                            "remote_binding": {
                                "label": {
                                    "505": {
                                        "lsr_id": {
                                            "10.169.197.252": {
                                                "label_space_id": {
                                                    0: {}
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        "10.169.197.92/30": {
                            "rev": "2",
                            "label_binding": {
                                "label": {
                                    "imp-null": {}
                                }
                            },
                            "remote_binding": {
                                "label": {
                                    "736112": {
                                        "lsr_id": {
                                            "10.169.197.253": {
                                                "label_space_id": {
                                                    0: {}
                                                }
                                            }
                                        }
                                    },
                                    "imp-null": {
                                        "lsr_id": {
                                            "10.169.197.252": {
                                                "label_space_id": {
                                                    0: {}
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        "10.120.202.64/32": {
                            "rev": "1020",
                            "label_binding": {
                                "label": {
                                    "2532": {}
                                }
                            },
                            "remote_binding": {
                                "label": {
                                    "399712": {
                                        "lsr_id": {
                                            "10.169.197.253": {
                                                "label_space_id": {
                                                    0: {}
                                                }
                                            }
                                        }
                                    },
                                    "506": {
                                        "lsr_id": {
                                            "10.169.197.252": {
                                                "label_space_id": {
                                                    0: {}
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        "10.186.1.0/24": {
                            "rev": "1028",
                            "label_binding": {
                                "label": {
                                    "2536": {}
                                }
                            },
                            "remote_binding": {
                                "label": {
                                    "508": {
                                        "lsr_id": {
                                            "10.169.197.252": {
                                                "label_space_id": {
                                                    0: {}
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }

    golden_output = {'execute.return_value': '''\
       Router#show mpls ldp bindings
Load for five secs: 55%/0%; one minute: 15%; five minutes: 10%
Time source is NTP, 20:29:28.227 JST Fri Nov 11 2016

  lib entry: 10.186.1.0/24, rev 1028
        local binding:  label: 2536
        remote binding: lsr: 10.169.197.252:0, label: 508
  lib entry: 10.120.202.48/30, rev 1034
        local binding:  label: 2539
        remote binding: lsr: 10.169.197.252:0, label: imp-null
  lib entry: 10.120.202.56/30, rev 1024
        local binding:  label: 2534
        remote binding: lsr: 10.169.197.252:0, label: 505
  lib entry: 10.120.202.64/32, rev 1020
        local binding:  label: 2532
        remote binding: lsr: 10.169.197.252:0, label: 506
        remote binding: lsr: 10.169.197.253:0, label: 399712
  lib entry: 10.169.197.92/30, rev 2
        local binding:  label: imp-null
        remote binding: lsr: 10.169.197.252:0, label: imp-null
        remote binding: lsr: 10.169.197.253:0, label: 736112
  lib entry: 10.169.197.96/30, rev 4
        local binding:  label: imp-null
        remote binding: lsr: 10.169.197.252:0, label: 1002
            '''}

    golden_output_all_detail = {'execute.return_value': '''\
    Router#show mpls ldp bindings all detail
Load for five secs: 2%/0%; one minute: 5%; five minutes: 5%
Time source is NTP, 16:10:10.910 JST Tue Nov 8 2016

  lib entry: 10.120.202.48/30, rev 18, chkpt: none
        local binding:  label: 2030 (owner LDP)
          Advertised to:
          10.169.197.252:0      10.169.197.253:0
        remote binding: lsr: 10.169.197.252:0, label: imp-null checkpointed
  lib entry: 10.120.202.56/30, rev 1085, chkpt: none
        local binding:  label: 6589 (owner LDP)
          Advertised to:
          10.169.197.252:0      10.169.197.253:0
        remote binding: lsr: 10.169.197.252:0, label: 1014 checkpointed
  lib entry: 10.120.202.64/32, rev 12, chkpt: none
        local binding:  label: 2027 (owner LDP)
          Advertised to:
          10.169.197.252:0      10.169.197.253:0
        remote binding: lsr: 10.169.197.252:0, label: 516 checkpointed
        remote binding: lsr: 10.169.197.253:0, label: 308016 checkpointed
  lib entry: 10.169.197.92/30, rev 4, chkpt: none
        local binding:  label: imp-null (owner LDP)
          Advertised to:
          10.169.197.252:0      10.169.197.253:0
        remote binding: lsr: 10.169.197.252:0, label: 126 checkpointed
    '''
    }

    golden_parsed_output_all_detail = {
       "vrf": {
          "default": {
             "lib_entry": {
                "10.169.197.92/30": {
                   "rev": "4",
                   "label_binding": {
                      "label": {
                         "imp-null": {
                            "owner": "LDP",
                            "advertised_to": [
                               "10.169.197.252:0",
                               "10.169.197.253:0"
                            ]
                         }
                      }
                   },
                   "checkpoint": "none",
                   "remote_binding": {
                      "label": {
                         "126": {
                            "lsr_id": {
                               "10.169.197.252": {
                                  "label_space_id": {
                                     0: {
                                        "checkpointed": True
                                     }
                                  }
                               }
                            }
                         }
                      }
                   }
                },
                "10.120.202.64/32": {
                   "rev": "12",
                   "label_binding": {
                      "label": {
                         "2027": {
                            "owner": "LDP",
                            "advertised_to": [
                               "10.169.197.252:0",
                               "10.169.197.253:0"
                            ]
                         }
                      }
                   },
                   "checkpoint": "none",
                   "remote_binding": {
                      "label": {
                         "308016": {
                            "lsr_id": {
                               "10.169.197.253": {
                                  "label_space_id": {
                                     0: {
                                        "checkpointed": True
                                     }
                                  }
                               }
                            }
                         },
                         "516": {
                            "lsr_id": {
                               "10.169.197.252": {
                                  "label_space_id": {
                                     0: {
                                        "checkpointed": True
                                     }
                                  }
                               }
                            }
                         }
                      }
                   }
                },
                "10.120.202.56/30": {
                   "rev": "1085",
                   "label_binding": {
                      "label": {
                         "6589": {
                            "owner": "LDP",
                            "advertised_to": [
                               "10.169.197.252:0",
                               "10.169.197.253:0"
                            ]
                         }
                      }
                   },
                   "checkpoint": "none",
                   "remote_binding": {
                      "label": {
                         "1014": {
                            "lsr_id": {
                               "10.169.197.252": {
                                  "label_space_id": {
                                     0: {
                                        "checkpointed": True
                                     }
                                  }
                               }
                            }
                         }
                      }
                   }
                },
                "10.120.202.48/30": {
                   "rev": "18",
                   "label_binding": {
                      "label": {
                         "2030": {
                            "owner": "LDP",
                            "advertised_to": [
                               "10.169.197.252:0",
                               "10.169.197.253:0"
                            ]
                         }
                      }
                   },
                   "checkpoint": "none",
                   "remote_binding": {
                      "label": {
                         "imp-null": {
                            "lsr_id": {
                               "10.169.197.252": {
                                  "label_space_id": {
                                     0: {
                                        "checkpointed": True
                                     }
                                  }
                               }
                            }
                         }
                      }
                   }
                }
             }
          }
       }
    }

    golden_parsed_output_all = {
    "vrf": {
        "vrf1": {
            "lib_entry": {
                "10.11.0.0/24": {
                    "rev": "7",
                    "remote_binding": {
                        "label": {
                            "imp-null": {
                                "lsr_id": {
                                    "10.132.0.1": {
                                        "label_space_id": {
                                            0: {}
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                "10.12.0.0/24": {
                    "label_binding": {
                        "label": {
                            "17": {}
                        }
                    },
                    "rev": "8",
                    "remote_binding": {
                        "label": {
                            "imp-null": {
                                "lsr_id": {
                                    "10.132.0.1": {
                                        "label_space_id": {
                                            0: {}
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                "10.0.0.0/24": {
                    "rev": "6",
                    "remote_binding": {
                        "label": {
                            "imp-null": {
                                "lsr_id": {
                                    "10.132.0.1": {
                                        "label_space_id": {
                                            0: {}
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        "default": {
            "lib_entry": {
                "10.11.0.0/24": {
                    "label_binding": {
                        "label": {
                            "imp-null": {}
                        }
                    },
                    "rev": "15",
                    "remote_binding": {
                        "label": {
                            "imp-null": {
                                "lsr_id": {
                                    "10.131.0.1": {
                                        "label_space_id": {
                                            0: {}
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                "10.0.0.0/24": {
                    "label_binding": {
                        "label": {
                            "imp-null": {}
                        }
                    },
                    "rev": "4",
                    "remote_binding": {
                        "label": {
                            "imp-null": {
                                "lsr_id": {
                                    "10.131.0.1": {
                                        "label_space_id": {
                                            0: {}
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
    golden_output_all = {'execute.return_value': '''\
         Router# show mpls ldp bindings all

         lib entry: 10.0.0.0/24, rev 4
               local binding:  label: imp-null
               remote binding: lsr: 10.131.0.1:0, label: imp-null
         lib entry: 10.11.0.0/24, rev 15
               local binding:  label: imp-null
               remote binding: lsr: 10.131.0.1:0, label: imp-null
       VRF vrf1:
         lib entry: 10.0.0.0/24, rev 6
               remote binding: lsr: 10.132.0.1:0, label: imp-null
         lib entry: 10.11.0.0/24, rev 7
               remote binding: lsr: 10.132.0.1:0, label: imp-null
         lib entry: 10.12.0.0/24, rev 8
               local binding:  label: 17
               remote binding: lsr: 10.132.0.1:0, label: imp-null
     '''}
    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowMplsLdpBindings(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output)
        obj = ShowMplsLdpBindings(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_all_detail(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output_all_detail)
        obj = ShowMplsLdpBindings(device=self.dev)
        parsed_output = obj.parse(all='all',detail="detail")
        self.assertEqual(parsed_output, self.golden_parsed_output_all_detail)

    def test_golden_all(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output_all)
        obj = ShowMplsLdpBindings(device=self.dev)
        parsed_output = obj.parse(all='all')
        self.assertEqual(parsed_output, self.golden_parsed_output_all)

class test_show_mpls_ldp_capabilities(unittest.TestCase):
    dev = Device(name='dev1')
    empty_output = {'execute.return_value': '      '}

    golden_parsed_output_all = {
        "ldp_capabilities": {
            "iccp_type": "0x0405",
            "mldp_multipoint_to_multipoint": "0x0509",
            "dynamic_anouncement": "0x0506",
            "typed_wildcard": "0x050B",
            "maj_version": 1,
            "mldp_point_to_multipoint": "0x0508",
            "min_version": 0
            }
        }
    golden_output_all = {'execute.return_value':'''
    Router#show mpls ldp capabilities all
    Load for five secs: 2%/0%; one minute: 5%; five minutes: 5%
    Time source is NTP, 16:10:10.481 JST Tue Nov 8 2016

    LDP Capabilities - [<description> (<type>)]
    ---------------------------------------------------------
        [ICCP (type 0x0405) MajVer 1 MinVer 0]
        [Dynamic Announcement (0x0506)]
        [mLDP Point-to-Multipoint (0x0508)]
        [mLDP Multipoint-to-Multipoint (0x0509)]
        [Typed Wildcard (0x050B)]

    '''}

    golden_parsed_output = {
        "ldp_capabilities": {
            "typed_wildcard": "0x050B",
            "dynamic_anouncement": "0x0506"
        }
    }

    golden_output = {'execute.return_value':'''\
    Router#show mpls ldp capabilities

    LDP Capabilities - [<description> (<type>)]
    ---------------------------------------------------------
    [Dynamic Announcement (0x0506)]
    [Typed Wildcard (0x050B)]

    '''
    }
    def test_empty(self):
        self.dev = Mock(**self.empty_output)
        obj = ShowMplsLdpCapabilities(device=self.dev)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output_all)
        obj = ShowMplsLdpCapabilities(device=self.dev)
        parsed_output = obj.parse(all="all")
        self.assertEqual(parsed_output, self.golden_parsed_output_all)

    def test_golden(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output)
        obj = ShowMplsLdpCapabilities(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

class test_show_mpls_ldp_discovery(unittest.TestCase):
    dev = Device(name='dev1')
    empty_output = {'execute.return_value': '      '}

    golden_parsed_output_all_detail = {
            "vrf": {
                "default": {
                    "local_ldp_identifier": {
                        "106.162.197.254:0": {
                            'discovery_sources':{
                                "interfaces": {
                                    "GigabitEthernet0/0/0": {
                                        'session': 'ldp',
                                        "hello_interval_ms": 5000,
                                        "transport_ip_addr": "106.162.197.254",
                                        "xmit": True,
                                        "recv": True,
                                        "ldp_id": {
                                            "106.162.197.252:0": {
                                                "reachable_via": "106.162.197.252/32",
                                                "password": "not required, none, in use",
                                                "holdtime_sec": 15,
                                                "transport_ip_address": "106.162.197.252",
                                                "proposed_peer": 15,
                                                "clients": "IPv4, mLDP",
                                                "source_ip_address": "106.162.197.93",
                                                "proposed_local": 15
                                            }
                                        },
                                        "enabled": "Interface config",
                                    },
                                    "GigabitEthernet0/0/2": {
                                        "hello_interval_ms": 5000,
                                        "transport_ip_addr": "106.162.197.254",
                                        'session': 'ldp',
                                        "xmit": True,
                                        "recv": True,
                                        "ldp_id": {
                                            "106.162.197.253:0": {
                                                "reachable_via": "106.162.197.253/32",
                                                "password": "not required, none, in use",
                                                "holdtime_sec": 15,
                                                "transport_ip_address": "106.162.197.253",
                                                "proposed_peer": 15,
                                                "clients": "IPv4, mLDP",
                                                "source_ip_address": "106.162.197.97",
                                                "proposed_local": 15
                                            }
                                        },
                                        "enabled": "Interface config",
                                    }
                                }
                            },
                        },
                    }
                }
            }
        }
    golden_output_all_detail = {'execute.return_value': '''\

    Router#show mpls ldp discovery all detail
    Load for five secs: 2%/0%; one minute: 5%; five minutes: 5%
    Time source is NTP, 16:10:10.682 JST Tue Nov 8 2016
     Local LDP Identifier:
        106.162.197.254:0
        Discovery Sources:
        Interfaces:
            GigabitEthernet0/0/0 (ldp): xmit/recv
                Enabled: Interface config
                Hello interval: 5000 ms; Transport IP addr: 106.162.197.254
                LDP Id: 106.162.197.252:0
                  Src IP addr: 106.162.197.93; Transport IP addr: 106.162.197.252
                  Hold time: 15 sec; Proposed local/peer: 15/15 sec
                  Reachable via 106.162.197.252/32
                  Password: not required, none, in use
                Clients: IPv4, mLDP
            GigabitEthernet0/0/2 (ldp): xmit/recv
                Enabled: Interface config
                Hello interval: 5000 ms; Transport IP addr: 106.162.197.254
                LDP Id: 106.162.197.253:0
                  Src IP addr: 106.162.197.97; Transport IP addr: 106.162.197.253
                  Hold time: 15 sec; Proposed local/peer: 15/15 sec
                  Reachable via 106.162.197.253/32
                  Password: not required, none, in use
                Clients: IPv4, mLDP
    '''
    }

    golden_output = {'execute.return_value': '''\
    Router# show mpls ldp discovery

     Local LDP Identifier:
         8.1.1.1:0
     Discovery Sources:
         Interfaces:
             Ethernet1/1/3 (ldp): xmit/recv
                 LDP Id: 177.73.0.77:0
                 LDP Id: 144.0.0.44:0
                 LDP Id: 155.0.0.55:0
             ATM3/0.1 (ldp): xmit/recv
                 LDP Id: 203.0.7.7:2
             ATM0/0.2 (tdp): xmit/recv
                 TDP Id: 119.1.0.1:1
     Targeted Hellos:
             8.1.1.1 -> 133.0.0.33 (ldp): active, xmit/recv
                 LDP Id: 133.0.0.33:0
             8.1.1.1 -> 168.7.0.16 (tdp): passive, xmit/recv
                 TDP Id: 133.0.0.33:0
     Router#
        '''
                                }
    golden_parsed_output = {
        "vrf": {
            "default": {
                "local_ldp_identifier": {
                    "8.1.1.1:0": {
                        "targeted_hellos": {
                            "8.1.1.1": {
                                "168.7.0.16": {
                                    "session": "tdp",
                                    "active": False,
                                    'tdp_id': '133.0.0.33:0',
                                    "xmit": True,
                                    "recv": True,
                                },
                                "133.0.0.33": {
                                    "active": True,
                                    "session": "ldp",
                                    "ldp_id": "133.0.0.33:0",
                                    "xmit": True,
                                    "recv": True,
                                }
                            }
                        },
                        "discovery_sources": {
                            "interfaces": {
                                "Ethernet1/1/3": {
                                    "session": "ldp",
                                    "xmit": True,
                                    "recv": True,
                                    "ldp_id": {
                                        "177.73.0.77:0": {
                                        },
                                        "155.0.0.55:0": {
                                        },
                                        "144.0.0.44:0": {
                                        }
                                    }
                                },
                                "ATM3/0.1": {
                                    "session": "ldp",
                                    "xmit": True,
                                    "recv": True,
                                    "ldp_id": {
                                        "203.0.7.7:2": {
                                        }
                                    }
                                },
                                "ATM0/0.2": {
                                    "session": "tdp",
                                    "xmit": True,
                                    "recv": True,
                                    "tdp_id": {
                                        "119.1.0.1:1": {
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    golden_parsed_output_all = {
    "vrf": {
        "default": {
            "local_ldp_identifier": {
                "12.12.12.12:0": {
                    "discovery_sources": {
                        "interfaces": {
                            "ATM1/1/0.1": {
                                "session": "tdp",
                                "xmit": True,
                                "recv": True,
                                "tdp_id": {
                                    "11.11.11.11:0": {
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        "vpn2": {
            "local_ldp_identifier": {
                "30.13.0.2:0": {
                    "discovery_sources": {
                        "interfaces": {
                            "ATM3/0/0.2": {
                                "session": "ldp",
                                "xmit": True,
                                "recv": True,
                                "ldp_id": {
                                    "14.14.14.14:0": {
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        "vpn1": {
            "local_ldp_identifier": {
                "30.7.0.2:0": {
                    "discovery_sources": {
                        "interfaces": {
                            "ATM3/0/0.1": {
                                "session": "ldp",
                                "xmit": True,
                                "recv": True,
                                "ldp_id": {
                                    "14.14.14.14:0": {
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
    golden_output_all = {'execute.return_value':'''\
    Router# show mpls ldp discovery all

     Local LDP Identifier:
         12.12.12.12:0
         Discovery Sources:
         Interfaces:
             ATM1/1/0.1 (tdp):xmit/recv
                 TDP Id:11.11.11.11:0
     VRF vpn1:Local LDP Identifier:
         30.7.0.2:0
         Discovery Sources:
         Interfaces:
             ATM3/0/0.1 (ldp):xmit/recv
                 LDP Id:14.14.14.14:0
     VRF vpn2:Local LDP Identifier:
         30.13.0.2:0
         Discovery Sources:
         Interfaces:
             ATM3/0/0.2 (ldp):xmit/recv
                 LDP Id:14.14.14.14:0
    '''}

    def test_empty(self):
        self.dev = Mock(**self.empty_output)
        obj = ShowMplsLdpDiscovery(device=self.dev)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_all_detail(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output_all_detail)
        obj = ShowMplsLdpDiscovery(device=self.dev)
        parsed_output = obj.parse(all="all", detail="detail")
        self.assertEqual(parsed_output, self.golden_parsed_output_all_detail)

    def test_golden(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output)
        obj = ShowMplsLdpDiscovery(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_all(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output_all)
        obj = ShowMplsLdpDiscovery(device=self.dev)
        parsed_output = obj.parse(all='all')
        self.assertEqual(parsed_output, self.golden_parsed_output_all)


class test_show_mpls_ldp_igp_sync(unittest.TestCase):
    dev = Device(name='dev1')
    empty_output = {'execute.return_value': '      '}

    golden_parsed_output_all = {
        'vrf': {
            'default': {
                'interface':{
                    'GigabitEthernet0/0/0':{
                        'ldp':{
                            'configured': True,
                            'igp_synchronization_enabled':True,
                        },
                        'sync': {
                            'status':{
                                'sync_achieved': True,
                                'peer_reachable': True,
                            },
                            'delay_time': 0,
                            'left_time': 0,
                        },
                        'igp': {
                            'holddown_time': 'infinite',
                            'enabled': "ospf 9996"
                        },
                        'peer_ldp_ident': '106.162.197.252:0',
                    },
                    "GigabitEthernet0/0/2": {
                        'ldp': {
                            'configured': True,
                            'igp_synchronization_enabled': False,
                        },
                    },
                }
            }
        }
    }
    golden_output_all = {'execute.return_value':'''\

    Router#show mpls ldp igp sync all
    Load for five secs: 2%/0%; one minute: 5%; five minutes: 5%
    Time source is NTP, 16:10:10.780 JST Tue Nov 8 2016

    GigabitEthernet0/0/0:
        LDP configured; LDP-IGP Synchronization enabled.
        Sync status: sync achieved; peer reachable.
        Sync delay time: 0 seconds (0 seconds left)
        IGP holddown time: infinite.
        Peer LDP Ident: 106.162.197.252:0
        IGP enabled: OSPF 9996
    GigabitEthernet0/0/2:
        LDP configured; LDP-IGP Synchronization not enabled.

    Router#
    '''}
    golden_parsed_output = {
        "vrf": {
            "default": {
                "interface": {
                    "FastEthernet0/0/0": {
                        "sync": {
                            "status": {
                                "enabled": True,
                                "sync_achieved": True,
                                "peer_reachable": True
                            }
                        },
                        "ldp": {
                            "configured": True,
                            "igp_synchronization_enabled": False
                        },
                        "igp": {
                            "enabled": "ospf 1",
                            "holddown_time": "infinite"
                        },
                        "peer_ldp_ident": "10.0.0.1:0"
                    }
                }
            }
        }
    }
    golden_output = {'execute.return_value': '''\

    Router#show mpls ldp igp sync
        FastEthernet0/0/0:
            LDP configured;  SYNC enabled.
            SYNC status: sync achieved; peer reachable.
            IGP holddown time: infinite.
            Peer LDP Ident: 10.0.0.1:0
            IGP enabled: OSPF 1

    '''}

    def test_empty(self):
        self.dev = Mock(**self.empty_output)
        obj = ShowMplsLdpIgpSync(device=self.dev)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_all(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output_all)
        obj = ShowMplsLdpIgpSync(device=self.dev)
        parsed_output = obj.parse(all='all')
        self.assertEqual(parsed_output, self.golden_parsed_output_all)

    def test_golden_interface(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output)
        obj = ShowMplsLdpIgpSync(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


class test_show_mpls_forwarding_table(unittest.TestCase):
    dev1 = Device(name='empty')
    dev = Device(name='dev')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
    "vrf": {
        "L3VPN-0051": {
            "local_label": {
                9301: {
                    "outgoing_label_or_vc": {
                        "No Label": {
                            "prefix_or_tunnel_id": {
                                "172.16.100.1/32[V]": {
                                    "outgoing_interface": {
                                        "Port-channel1.51": {
                                            "next_hop": "192.168.10.253",
                                            "bytes_label_switched": 0,
                                            "mac": 18,
                                            "encaps": 18,
                                            "mru": 1530,
                                            "label_stack": "{}",
                                            "macstr": "00002440156384B261CB1480810000330800",
                                            "vpn_route": "L3VPN-0051",
                                            "output_feature_configured": False,
                                            "load_sharing": {
                                                "method": "per-destination",
                                                "slots": [
                                                    "0",
                                                    "2",
                                                    "4",
                                                    "6",
                                                    "8",
                                                    "10",
                                                    "12",
                                                    "14"
                                                ]
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                2641: {
                    "outgoing_label_or_vc": {
                        "No Label": {
                            "prefix_or_tunnel_id": {
                                "172.16.100.100/32[V]": {
                                    "outgoing_interface": {
                                        "Port-channel1.51": {
                                            "next_hop": "192.168.10.253",
                                            "bytes_label_switched": 0,
                                            "mac": 18,
                                            "encaps": 18,
                                            "mru": 1530,
                                            "label_stack": "{}",
                                            "via": "Ls0",
                                            "macstr": "AABBCC032800AABBCC0325018847",
                                            "lstack": "00010000",
                                            "vpn_route": "L3VPN-0051",
                                            "output_feature_configured": False
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                2642: {
                    "outgoing_label_or_vc": {
                        "No Label": {
                            "prefix_or_tunnel_id": {
                                "192.168.10.0/24[V]": {
                                    "outgoing_interface": {
                                        "Aggregate/L3VPN-0051": {
                                            "bytes_label_switched": 12189672,
                                            "mac": 0,
                                            "encaps": 0,
                                            "mru": 0,
                                            "label_stack": "{}",
                                            "vpn_route": "L3VPN-0051",
                                            "output_feature_configured": False,
                                            "broadcast": True
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
    golden_output = {'execute.return_value': '''\
    Router#show mpls forwarding-table vrf L3VPN-0051 detail
    Load for five secs: 71%/0%; one minute: 11%; five minutes: 9%
    Time source is NTP, 20:29:27.645 JST Fri Nov 11 2016

    Local      Outgoing   Prefix           Bytes Label   Outgoing   Next Hop
    Label      Label      or Tunnel Id     Switched      interface
    9301       No Label   172.16.100.1/32[V]   \
                                           0             Po1.51     192.168.10.253
            MAC/Encaps=18/18, MRU=1530, Label Stack{}
            00002440156384B261CB1480810000330800
            VPN route: L3VPN-0051
            No output feature configured
        Per-destination load-sharing, slots: 0 2 4 6 8 10 12 14
    2641       No Label   172.16.100.100/32[V]   \
                                           0             Po1.51     192.168.10.253
        MAC/Encaps=18/18, MRU=1530, Label Stack{}, via Ls0
        AABBCC032800AABBCC0325018847 00010000
        VPN route: L3VPN-0051
        No output feature configured
    2642       No Label   192.168.10.0/24[V]   \
                                           12189672      aggregate/L3VPN-0051
        MAC/Encaps=0/0, MRU=0, Label Stack{}
        VPN route: L3VPN-0051
        No output feature configured
        Broadcast
 '''
                     }

    golden_parsed_output_2 = {
        "vrf": {
            "default": {
                "local_label": {
                    201: {
                        "outgoing_label_or_vc": {
                            "Pop tag": {
                                "prefix_or_tunnel_id":{
                                    "10.18.18.18/32":{
                                        "outgoing_interface":{
                                            "Port-channel1/1/0":{
                                                "next_hop": "point2point",
                                                "bytes_label_switched": 0,
                                            }
                                        }
                                    }
                                }
                            },
                            "2/35": {
                                "prefix_or_tunnel_id": {
                                    "10.18.18.18/32":{
                                        "outgoing_interface":{
                                            "ATM4/1/0.1":{
                                                "next_hop": "point2point",
                                                "bytes_label_switched": 0
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    251: {
                        "outgoing_label_or_vc": {
                            "18": {
                                "prefix_or_tunnel_id": {
                                    "10.17.17.17/32": {
                                        "outgoing_interface": {
                                            "Port-channel1/1/0": {
                                                "next_hop": "point2point",
                                                "bytes_label_switched": 0
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }

    }
    golden_output_2 = {'execute.return_value':'''\
    Router# show mpls forwarding-table
Local  Outgoing    Prefix            Bytes tag  Outgoing   Next Hop
tag    tag or VC   or Tunnel Id      switched   interface
201    Pop tag     10.18.18.18/32    0          PO1/1/0    point2point
       2/35        10.18.18.18/32    0          AT4/1/0.1  point2point
251    18          10.17.17.17/32    0          PO1/1/0    point2point

    '''}

    golden_parsed_output_3 = {
        "vrf": {
            "default": {
                "local_label": {
                    16: {
                        "outgoing_label_or_vc": {
                            "16": {
                                "prefix_or_tunnel_id": {
                                    "10.0.0.1 1 [19]": {
                                        "outgoing_interface": {
                                            "Ethernet1/0": {
                                                "next_hop": "10.0.1.30",
                                                "bytes_label_switched": 0,
                                                "mac": 14,
                                                "encaps": 18,
                                                "mru": 1500,
                                                "label_stack": "{16}",
                                                "macstr": "AABBCC032800AABBCC0325018847",
                                                "lstack": "00010000",
                                                "output_feature_configured": False,
                                                "broadcast": True

                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    17: {
                        "outgoing_label_or_vc": {
                            "No Label": {
                                "prefix_or_tunnel_id": {
                                    "10.0.0.1 1 [19]": {
                                        "outgoing_interface": {
                                            "aggregate": {
                                                "bytes_label_switched": 342,
                                                "mac": 0,
                                                "encaps": 0,
                                                "mru": 0,
                                                "label_stack": "{}",
                                                "via": "Ls0"
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    golden_output_3 = {'execute.return_value': '''\
    Local      Outgoing   Prefix           Bytes Label   Outgoing   Next Hop
    Label      Label      or Tunnel Id     Switched      interface
    16         16         10.0.0.1 1 [19]  0             Et1/0      10.0.1.30
            MAC/Encaps=14/18, MRU=1500, Label Stack{16}
            AABBCC032800AABBCC0325018847 00010000
            No output feature configured
        Broadcast

    Local      Outgoing   Prefix           Bytes Label   Outgoing   Next Hop
    Label      Label      or Tunnel Id     Switched      interface
    17         No Label   10.0.0.1 1 [19]  342           aggregate
        MAC/Encaps=0/0, MRU=0, Label Stack{}, via Ls0

    '''
    }

    golden_parsed_output_4 = {
     "vrf": {
          "default": {
               "local_label": {
                    16: {
                         "outgoing_label_or_vc": {
                              "Pop Label": {
                                   "prefix_or_tunnel_id": {
                                        "1.1.1.2-A": {
                                             "outgoing_interface": {
                                                  "Ethernet0/0": {
                                                       "next_hop": "1.1.1.2",
                                                       "bytes_label_switched": 0
                                                  }
                                             }
                                        }
                                   }
                              }
                         }
                    },
                    17: {
                         "outgoing_label_or_vc": {
                              "Pop Label": {
                                   "prefix_or_tunnel_id": {
                                        "1.1.1.2-A": {
                                             "outgoing_interface": {
                                                  "Ethernet0/0": {
                                                       "next_hop": "1.1.1.2",
                                                       "bytes_label_switched": 0
                                                  }
                                             }
                                        }
                                   }
                              }
                         }
                    },
                    18: {
                         "outgoing_label_or_vc": {
                              "Pop Label": {
                                   "prefix_or_tunnel_id": {
                                        "1.1.1.2-A": {
                                             "outgoing_interface": {
                                                  "Ethernet0/0": {
                                                       "next_hop": "1.1.1.2",
                                                       "bytes_label_switched": 0
                                                  }
                                             }
                                        }
                                   }
                              }
                         }
                    },
                    19: {
                         "outgoing_label_or_vc": {
                              "Pop Label": {
                                   "prefix_or_tunnel_id": {
                                        "15.15.15.2-A": {
                                             "outgoing_interface": {
                                                  "Ethernet0/1": {
                                                       "next_hop": "15.15.15.2",
                                                       "bytes_label_switched": 0
                                                  }
                                             }
                                        }
                                   }
                              }
                         }
                    },
                    20: {
                         "outgoing_label_or_vc": {
                              "Pop Label": {
                                   "prefix_or_tunnel_id": {
                                        "15.15.15.2-A": {
                                             "outgoing_interface": {
                                                  "Ethernet0/1": {
                                                       "next_hop": "15.15.15.2",
                                                       "bytes_label_switched": 0
                                                  }
                                             }
                                        }
                                   }
                              }
                         }
                    },
                    21: {
                         "outgoing_label_or_vc": {
                              "Pop Label": {
                                   "prefix_or_tunnel_id": {
                                        "15.15.15.2-A": {
                                             "outgoing_interface": {
                                                  "Ethernet0/1": {
                                                       "next_hop": "15.15.15.2",
                                                       "bytes_label_switched": 0
                                                  }
                                             }
                                        }
                                   }
                              }
                         }
                    },
                    22: {
                         "outgoing_label_or_vc": {
                              "Pop Label": {
                                   "prefix_or_tunnel_id": {
                                        "1/1[TE-Bind]": {
                                             "outgoing_interface": {
                                                  "Tunnel1": {
                                                       "next_hop": "point2point",
                                                       "tsp_tunnel": True,
                                                       "bytes_label_switched": 0
                                                  }
                                             }
                                        }
                                   }
                              }
                         }
                    },
                    16110: {
                         "outgoing_label_or_vc": {
                              "Pop Label": {
                                   "prefix_or_tunnel_id": {
                                        "20.20.20.20/32": {
                                             "outgoing_interface": {
                                                  "Ethernet0/0": {
                                                       "next_hop": "1.1.1.2",
                                                       "bytes_label_switched": 0
                                                  }
                                             }
                                        }
                                   }
                              }
                         }
                    },
                    16120: {
                         "outgoing_label_or_vc": {
                              "16120": {
                                   "prefix_or_tunnel_id": {
                                        "30.30.30.30/32": {
                                             "outgoing_interface": {
                                                  "Ethernet0/0": {
                                                       "next_hop": "1.1.1.2",
                                                       "bytes_label_switched": 0
                                                  }
                                             }
                                        }
                                   }
                              }
                         }
                    },
                    16130: {
                         "outgoing_label_or_vc": {
                              "16130": {
                                   "prefix_or_tunnel_id": {
                                        "40.40.40.40/32": {
                                             "outgoing_interface": {
                                                  "Ethernet0/0": {
                                                       "next_hop": "1.1.1.2",
                                                       "bytes_label_switched": 0
                                                  },
                                                  "Tunnel1": {
                                                       "next_hop": "point2point",
                                                       "tsp_tunnel": True,
                                                       "bytes_label_switched": 0
                                                  }
                                             }
                                        }
                                   }
                              }
                         }
                    },
                    16140: {
                         "outgoing_label_or_vc": {
                              "Pop Label": {
                                   "prefix_or_tunnel_id": {
                                        "50.50.50.50/32": {
                                             "outgoing_interface": {
                                                  "Tunnel1": {
                                                       "next_hop": "point2point",
                                                       "tsp_tunnel": True,
                                                       "bytes_label_switched": 0
                                                  }
                                             }
                                        }
                                   }
                              }
                         }
                    },
                    16200: {
                         "outgoing_label_or_vc": {
                              "Pop Label": {
                                   "prefix_or_tunnel_id": {
                                        "100.100.100.100/32": {
                                             "outgoing_interface": {
                                                  "Ethernet0/1": {
                                                       "next_hop": "15.15.15.2",
                                                       "bytes_label_switched": 0
                                                  }
                                             }
                                        }
                                   }
                              }
                         }
                    },
                    17100: {
                         "outgoing_label_or_vc": {
                              "Pop Label": {
                                   "prefix_or_tunnel_id": {
                                        "0-20.20.20.20/32-0": {
                                             "outgoing_interface": {
                                                  "Ethernet0/0": {
                                                       "next_hop": "1.1.1.2",
                                                       "bytes_label_switched": 0
                                                  }
                                             }
                                        }
                                   }
                              }
                         }
                    },
                    17200: {
                         "outgoing_label_or_vc": {
                              "17200": {
                                   "prefix_or_tunnel_id": {
                                        "0-30.30.30.30/32-0": {
                                             "outgoing_interface": {
                                                  "Ethernet0/0": {
                                                       "next_hop": "1.1.1.2",
                                                       "bytes_label_switched": 0
                                                  }
                                             }
                                        }
                                   }
                              }
                         }
                    },
                    17300: {
                         "outgoing_label_or_vc": {
                              "17300": {
                                   "prefix_or_tunnel_id": {
                                        "0-40.40.40.40/32-0": {
                                             "outgoing_interface": {
                                                  "Ethernet0/1": {
                                                       "next_hop": "15.15.15.2",
                                                       "bytes_label_switched": 0
                                                  }
                                             }
                                        }
                                   }
                              }
                         }
                    },
                    17400: {
                         "outgoing_label_or_vc": {
                              "17400": {
                                   "prefix_or_tunnel_id": {
                                        "0-50.50.50.50/32-0": {
                                             "outgoing_interface": {
                                                  "Ethernet0/1": {
                                                       "next_hop": "15.15.15.2",
                                                       "bytes_label_switched": 0
                                                  }
                                             }
                                        }
                                   }
                              }
                         }
                    },
                    18000: {
                         "outgoing_label_or_vc": {
                              "Pop Label": {
                                   "prefix_or_tunnel_id": {
                                        "0-100.100.100.100/32-0": {
                                             "outgoing_interface": {
                                                  "Ethernet0/1": {
                                                       "next_hop": "15.15.15.2",
                                                       "bytes_label_switched": 0
                                                  }
                                             }
                                        }
                                   }
                              }
                         }
                    }
               }
          }
     }
}


    golden_output_4 = {'execute.return_value':'''\
    Local      Outgoing   Prefix           Bytes Label   Outgoing   Next Hop
    Label      Label      or Tunnel Id     Switched      interface
    16         Pop Label  1.1.1.2-A        0             Et0/0      1.1.1.2
    17         Pop Label  1.1.1.2-A        0             Et0/0      1.1.1.2
    18         Pop Label  1.1.1.2-A        0             Et0/0      1.1.1.2
    19         Pop Label  15.15.15.2-A     0             Et0/1      15.15.15.2
    20         Pop Label  15.15.15.2-A     0             Et0/1      15.15.15.2
    21         Pop Label  15.15.15.2-A     0             Et0/1      15.15.15.2
    22    [T]  Pop Label  1/1[TE-Bind]     0             Tu1        point2point
    16110      Pop Label  20.20.20.20/32   0             Et0/0      1.1.1.2
    16120      16120      30.30.30.30/32   0             Et0/0      1.1.1.2
    16130      16130      40.40.40.40/32   0             Et0/0      1.1.1.2
          [T]  16130      40.40.40.40/32   0             Tu1        point2point
    16140 [T]  Pop Label  50.50.50.50/32   0             Tu1        point2point
    16200      Pop Label  100.100.100.100/32   \
                                           0             Et0/1      15.15.15.2
    17100      Pop Label  0-20.20.20.20/32-0   \
                                           0             Et0/0      1.1.1.2
    17200      17200      0-30.30.30.30/32-0   \
                                           0             Et0/0      1.1.1.2
    17300      17300      0-40.40.40.40/32-0   \
                                           0             Et0/1      15.15.15.2
    17400      17400      0-50.50.50.50/32-0   \
                                           0             Et0/1      15.15.15.2
    18000      Pop Label  0-100.100.100.100/32-0   \
                                           0             Et0/1      15.15.15.2

    '''}

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowMplsForwardingTable(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output)
        obj = ShowMplsForwardingTable(device=self.dev)
        parsed_output = obj.parse(vrf='L3VPN-0051')
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_2(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output_2)
        obj = ShowMplsForwardingTable(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

    def test_golden_3(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output_3)
        obj = ShowMplsForwardingTable(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_3)

    def test_golden_4(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output_4)
        obj = ShowMplsForwardingTable(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_4)

class test_show_mpls_interface(unittest.TestCase):
    dev1 = Device(name='empty')
    dev = Device(name='dev')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'vrf':{
            'default':{
                "interfaces": {
                    "GigabitEthernet6": {
                        "ip": "yes",
                        "tunnel": "no",
                        "session": 'ldp',
                        "bgp": "no",
                        "static": "no",
                        "operational": "yes"
                    }
                }
            }
        }
    }
    golden_output = {'execute.return_value': '''\
    PE1#show mpls interfaces
    Interface              IP            Tunnel   BGP Static Operational
    GigabitEthernet6       Yes (ldp)     No       No  No     Yes
    '''
                     }
    golden_parsed_output_detail = {
        'vrf': {
            'default': {
                "interfaces": {
                    "GigabitEthernet0/0/0": {
                        "type": "Unknown",
                        "session": "ldp",
                        "ip_labeling_enabled": {
                            True: {
                                "ldp": True,
                                "interface_config": True
                            },
                        },
                        "lsp_tunnel_labeling_enabled": False,
                        "lp_frr_labeling_enabled": False,
                        "bgp_labeling_enabled": False,
                        "mtu": 1552,
                        "mpls_operational": True
                    }
                }
            }
        }
    }
    golden_output_detail = {'execute.return_value': '''\
    Router#show mpls interfaces detail
    Load for five secs: 2%/0%; one minute: 5%; five minutes: 5%
    Time source is NTP, 16:10:10.438 JST Tue Nov 8 2016

    Interface GigabitEthernet0/0/0:
            Type Unknown
            IP labeling enabled (ldp) :
              Interface config
            LSP Tunnel labeling not enabled
            IP FRR labeling not enabled
            BGP labeling not enabled
            MPLS operational
            MTU = 1552
    '''
                            }

    golden_parsed_output_all = {
        "vrf": {
            "default": {
                "interfaces": {
                    "GigabitEthernet6/0": {
                        "ip": "yes",
                        "tunnel": "no",
                        "session": "ldp",
                        "operational": "yes"
                    }
                }
            },
            "vpn1": {
                "interfaces": {
                    "Ethernet3/1": {
                        "ip": "no",
                        "tunnel": "no",
                        "operational": "yes"
                    }
                }
            }
        }

    }
    golden_output_all = {'execute.return_value': '''\
    Router# show mpls interfaces all

    Interface              IP            Tunnel   Operational
    GigabitEthernet6/0     Yes (ldp)     No       Yes
    VRF vpn1:
    Ethernet3/1            No            No       Yes
    '''}

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowMplsInterface(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output)
        obj = ShowMplsInterface(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_detail(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output_detail)
        obj = ShowMplsInterface(device=self.dev)
        parsed_output = obj.parse(detail='detail')
        self.assertEqual(parsed_output, self.golden_parsed_output_detail)

    def test_golden_all(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output_all)
        obj = ShowMplsInterface(device=self.dev)
        parsed_output = obj.parse(all='all')
        self.assertEqual(parsed_output, self.golden_parsed_output_all)


class test_show_mpls_l2transport_vc_detail(unittest.TestCase):
    dev = Device(name='dev1')
    empty_output = {'execute.return_value': '      '}

    golden_parsed_output = {
    'interface': {
        'FastEthernet2/1/1.2': {
            'signaling_protocol': {
                'LDP': {
                    'mtu': {
                        'local': 1500,
                        'remote': 1500,
                        },
                    'remote_interface_description': 'xconnect to PE2',
                    'group_id': {
                        'local': 0,
                        'remote': 0,
                        },
                    'peer_id': '10.2.2.2:0',
                    'mpls_vc_labels': {
                        'local': 21,
                        'remote': 16,
                        },
                    'peer_state': 'down',
                    },
                },
            'destination_address': {
                '10.2.2.2': {
                    'default_path': 'active',
                    'preferred_path': 'not configured',
                    'tunnel_label': 'imp-null',
                    'vc_id': 1002,
                    'output_interface': 'Serial2/0/2',
                    'vc_status': 'recovering',
                    'imposed_label_stack': '{16}',
                    'next_hop': 'point2point',
                    },
                },
            'line_protocol_status': 'up',
            'sequencing': {
                'received': 'disabled',
                'sent': 'disabled',
                },
            'status': 'up',
            'create_time': '1d00h',
            'statistics': {
                'bytes': {
                    'received': 25073016,
                    'sent': 25992388,
                    },
                'packets': {
                    'received': 20040,
                    'sent': 28879,
                    },
                },
            'last_status_change_time': '00:00:03',
            'ethernet_vlan': {
                2: {
                    'status': 'up',
                    },
                },
            },
        },
    }

    golden_output = {'execute.return_value': '''\
        Device# show mpls l2transport vc detail

        ip cef distributed

        Local interface: Fa2/1/1.2 up, line protocol up, Eth VLAN 2 up
          Destination address: 10.2.2.2, VC ID: 1002, VC status: up
            Preferred path: not configured
            Default path: active
            Tunnel label: imp-null, next hop point2point
            Output interface: Se2/0/2, imposed label stack {16}
          Create time: 1d00h, last status change time: 1d00h
          Signaling protocol: LDP, peer 10.2.2.2:0 up
            MPLS VC labels: local 21, remote 16
            Group ID: local 0, remote 0
            MTU: local 1500, remote 1500
            Remote interface description: "xconnect to PE2"
          Sequencing: receive disabled, send disabled
          VC statistics:
            packet totals: receive 3466, send 12286
            byte totals:   receive 4322368, send 5040220
            packet drops:  receive 0, send 0


        Local interface: Fa2/1/1.2 up, line protocol up, Eth VLAN 2 up
          Destination address: 10.2.2.2, VC ID: 1002, VC status: recovering
            Preferred path: not configured
            Default path: active
            Tunnel label: imp-null, next hop point2point
            Output interface: Se2/0/2, imposed label stack {16}
          Create time: 1d00h, last status change time: 00:00:03
          Signaling protocol: LDP, peer 10.2.2.2:0 down
            MPLS VC labels: local 21, remote 16
            Group ID: local 0, remote 0
            MTU: local 1500, remote 1500
            Remote interface description: "xconnect to PE2"
          Sequencing: receive disabled, send disabled
          VC statistics:
            packet totals: receive 20040, send 28879
            byte totals:   receive 25073016, send 25992388
            packet drops:  receive 0, send 0
    '''}

    golden_parsed_output_2 = {
    'interface': {
        'VFIPE1-VPLS-A': {
            'create_time': '3d15h',
            'status': 'up',
            'last_status_change_time': '1d03h',
            'sequencing': {
                'received': 'disabled',
                'sent': 'disabled',
                },
            'statistics': {
                'packets': {
                    'received': 0,
                    'sent': 0,
                    },
                'bytes': {
                    'received': 0,
                    'sent': 0,
                    },
                },
            'destination_address': {
                '10.2.2.2': {
                    'imposed_label_stack': '{18}',
                    'tunnel_label': 'imp-null',
                    'output_interface': 'Serial2/0',
                    'vc_status': 'up',
                    'vc_id': 100,
                    'next_hop': 'point2point',
                    },
                },
            'signaling_protocol': {
                'LDP': {
                    'group_id': {
                        'local': 0,
                        'remote': 0,
                        },
                    'peer_state': 'up',
                    'peer_id': '10.2.2.2:0',
                    'mtu': {
                        'local': 1500,
                        'remote': 1500,
                        },
                    'mpls_vc_labels': {
                        'local': 18,
                        'remote': 18,
                        },
                    },
                },
            },
        },
    }

    golden_output_2 = {'execute.return_value': '''\
        Device# show mpls l2transport vc detail

        Local interface: VFI PE1-VPLS-A up
          Destination address: 10.2.2.2, VC ID: 100, VC status: up
            Tunnel label: imp-null, next hop point2point
            Output interface: Se2/0, imposed label stack {18}
          Create time: 3d15h, last status change time: 1d03h
          Signaling protocol: LDP, peer 10.2.2.2:0 up
            MPLS VC labels: local 18, remote 18
            Group ID: local 0, remote 0
            MTU: local 1500, remote 1500
            Remote interface description:
          Sequencing: receive disabled, send disabled
          VC statistics:
            packet totals: receive 0, send 0
            byte totals:   receive 0, send 0
            packet drops:  receive 0, send 0
    '''}

    def test_empty(self):
        self.dev = Mock(**self.empty_output)
        obj = ShowMplsL2TransportDetail(device=self.dev)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output)
        obj = ShowMplsL2TransportDetail(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_2(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output_2)
        obj = ShowMplsL2TransportDetail(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_2)


if __name__ == '__main__':
    unittest.main()
