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
                                              ShowMplsForwardingTableDetail,\
                                              ShowMplsInterface, \
                                              ShowMplsL2TransportDetail, \
                                              ShowMplsL2TransportVC

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
    Time source is NTP, 16:10:10.454 EST Tue Nov 8 2016
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
    Time source is NTP, 16:10:10.454 EST Tue Nov 8 2016
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
                   '10.169.197.252': {
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
                   '10.169.197.253': {
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
    Time source is NTP, 16:10:12.625 EST Tue Nov 8 2016

    Peer: 10.169.197.252:0
      In label Request Records created: 0, freed: 0
      In label Withdraw Records created: 0, freed: 0
      Local Address Withdraw Set: 0, Cleared: 0
      Transmit contexts enqueued: 0, dequeued: 0
    Peer: 10.169.197.253:0
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
    Time source is NTP, 20:53:42.709 EST Fri Nov 11 2016
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
    '''}

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
                      "label_space_id": {
                          0: {
                              "local_ldp_ident": "10.169.197.254:0",
                              "tcp_connection": "10.169.197.252.646 - 10.169.197.254.44315",
                              "password": "not required, none, in use",
                              "state": "oper",
                              "msg_sent": 9981,
                              "msg_rcvd": 10004,
                              "downstream": True,
                              "last_tib_rev_sent": 4103,
                              "uptime": "3d21h",
                              "ldp_discovery_sources": {
                                  "interface": {
                                      "GigabitEthernet0/0/0": {
                                          "ip_address": {
                                              "10.169.197.93": {
                                                  "holdtime_ms": 15000,
                                                  "hello_interval_ms": 5000
                                              }
                                          }
                                      }
                                  }
                              },
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
                              "peer_holdtime_ms": 180000,
                              "ka_interval_ms": 60000,
                              "peer_state": "estab",
                              "nsr": "Not Ready",
                              "capabilities": {
                                  "sent": {
                                      "ICCP": {
                                          "type": "0x0405",
                                          "maj_ver": 1,
                                          "min_ver": 0
                                      },
                                      "dynamic_anouncement": "0x0506",
                                      "mldp_point_to_multipoint": "0x0508",
                                      "mldp_multipoint_to_multipoint": "0x0509",
                                      "typed_wildcard": "0x050B"
                                  },
                                  "received": {
                                      "ICCP": {
                                          "type": "0x0405",
                                          "maj_ver": 1,
                                          "min_ver": 0
                                      },
                                      "dynamic_anouncement": "0x0506",
                                      "mldp_point_to_multipoint": "0x0508",
                                      "mldp_multipoint_to_multipoint": "0x0509",
                                      "typed_wildcard": "0x050B"
                                  }
                              }
                          }
                      }
                  },
                  "10.169.197.253": {
                      "label_space_id": {
                          0: {
                              "local_ldp_ident": "10.169.197.254:0",
                              "tcp_connection": "10.169.197.253.646 - 10.169.197.254.34904",
                              "password": "not required, none, in use",
                              "state": "oper",
                              "msg_sent": 9966,
                              "msg_rcvd": 9153,
                              "downstream": True,
                              "last_tib_rev_sent": 4103,
                              "uptime": "3d21h",
                              "ldp_discovery_sources": {
                                  "interface": {
                                      "GigabitEthernet0/0/2": {
                                          "ip_address": {
                                              "10.169.197.97": {
                                                  "holdtime_ms": 15000,
                                                  "hello_interval_ms": 5000
                                              }
                                          }
                                      }
                                  }
                              },
                              "address_bound": [
                                  "10.120.202.57",
                                  "10.169.197.97"
                              ],
                              "peer_holdtime_ms": 180000,
                              "ka_interval_ms": 60000,
                              "peer_state": "estab",
                              "nsr": "Not Ready",
                              "capabilities": {
                                  "sent": {
                                      "ICCP": {
                                          "type": "0x0405",
                                          "maj_ver": 1,
                                          "min_ver": 0
                                      },
                                      "dynamic_anouncement": "0x0506",
                                      "mldp_point_to_multipoint": "0x0508",
                                      "mldp_multipoint_to_multipoint": "0x0509",
                                      "typed_wildcard": "0x050B"
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
    Router#show mpls ldp neighbor detail
    Load for five secs: 2%/0%; one minute: 5%; five minutes: 5%
    Time source is NTP, 16:10:10.569 EST Tue Nov 8 2016
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
        Time source is NTP, 20:29:28.227 EST Fri Nov 11 2016

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
    Time source is NTP, 16:10:10.910 EST Tue Nov 8 2016

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
    Time source is NTP, 16:10:10.481 EST Tue Nov 8 2016

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
                        "10.169.197.254:0": {
                            'discovery_sources':{
                                "interfaces": {
                                    "GigabitEthernet0/0/0": {
                                        'session': 'ldp',
                                        "hello_interval_ms": 5000,
                                        "transport_ip_addr": "10.169.197.254",
                                        "xmit": True,
                                        "recv": True,
                                        "ldp_id": {
                                            "10.169.197.252:0": {
                                                "reachable_via": "10.169.197.252/32",
                                                "password": "not required, none, in use",
                                                "holdtime_sec": 15,
                                                "transport_ip_address": "10.169.197.252",
                                                "proposed_peer": 15,
                                                "clients": "IPv4, mLDP",
                                                "source_ip_address": "10.169.197.93",
                                                "proposed_local": 15
                                            }
                                        },
                                        "enabled": "Interface config",
                                    },
                                    "GigabitEthernet0/0/2": {
                                        "hello_interval_ms": 5000,
                                        "transport_ip_addr": "10.169.197.254",
                                        'session': 'ldp',
                                        "xmit": True,
                                        "recv": True,
                                        "ldp_id": {
                                            "10.169.197.253:0": {
                                                "reachable_via": "10.169.197.253/32",
                                                "password": "not required, none, in use",
                                                "holdtime_sec": 15,
                                                "transport_ip_address": "10.169.197.253",
                                                "proposed_peer": 15,
                                                "clients": "IPv4, mLDP",
                                                "source_ip_address": "10.169.197.97",
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
    Time source is NTP, 16:10:10.682 EST Tue Nov 8 2016
     Local LDP Identifier:
        10.169.197.254:0
        Discovery Sources:
        Interfaces:
            GigabitEthernet0/0/0 (ldp): xmit/recv
                Enabled: Interface config
                Hello interval: 5000 ms; Transport IP addr: 10.169.197.254
                LDP Id: 10.169.197.252:0
                  Src IP addr: 10.169.197.93; Transport IP addr: 10.169.197.252
                  Hold time: 15 sec; Proposed local/peer: 15/15 sec
                  Reachable via 10.169.197.252/32
                  Password: not required, none, in use
                Clients: IPv4, mLDP
            GigabitEthernet0/0/2 (ldp): xmit/recv
                Enabled: Interface config
                Hello interval: 5000 ms; Transport IP addr: 10.169.197.254
                LDP Id: 10.169.197.253:0
                  Src IP addr: 10.169.197.97; Transport IP addr: 10.169.197.253
                  Hold time: 15 sec; Proposed local/peer: 15/15 sec
                  Reachable via 10.169.197.253/32
                  Password: not required, none, in use
                Clients: IPv4, mLDP
    '''
    }

    golden_output = {'execute.return_value': '''\
    Router# show mpls ldp discovery

     Local LDP Identifier:
         10.81.1.1:0
     Discovery Sources:
         Interfaces:
             Ethernet1/1/3 (ldp): xmit/recv
                 LDP Id: 172.16.25.77:0
                 LDP Id: 172.16.81.44:0
                 LDP Id: 172.16.55.55:0
             ATM3/0.1 (ldp): xmit/recv
                 LDP Id: 192.168.240.7:2
             ATM0/0.2 (tdp): xmit/recv
                 TDP Id: 10.120.0.1:1
     Targeted Hellos:
             10.81.1.1 -> 172.16.94.33 (ldp): active, xmit/recv
                 LDP Id: 172.16.94.33:0
             10.81.1.1 -> 172.16.25.16 (tdp): passive, xmit/recv
                 TDP Id: 172.16.94.33:0
     Router#
        '''
                                }
    golden_parsed_output = {
        "vrf": {
            "default": {
                "local_ldp_identifier": {
                    "10.81.1.1:0": {
                        "targeted_hellos": {
                            "10.81.1.1": {
                                "172.16.25.16": {
                                    "session": "tdp",
                                    "active": False,
                                    'tdp_id': '172.16.94.33:0',
                                    "xmit": True,
                                    "recv": True,
                                },
                                "172.16.94.33": {
                                    "active": True,
                                    "session": "ldp",
                                    "ldp_id": "172.16.94.33:0",
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
                                        "172.16.25.77:0": {
                                        },
                                        "172.16.55.55:0": {
                                        },
                                        "172.16.81.44:0": {
                                        }
                                    }
                                },
                                "ATM3/0.1": {
                                    "session": "ldp",
                                    "xmit": True,
                                    "recv": True,
                                    "ldp_id": {
                                        "192.168.240.7:2": {
                                        }
                                    }
                                },
                                "ATM0/0.2": {
                                    "session": "tdp",
                                    "xmit": True,
                                    "recv": True,
                                    "tdp_id": {
                                        "10.120.0.1:1": {
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
                    "10.66.12.12:0": {
                        "discovery_sources": {
                            "interfaces": {
                                "ATM1/1/0.1": {
                                    "session": "tdp",
                                    "xmit": True,
                                    "recv": True,
                                    "tdp_id": {
                                        "10.229.11.11:0": {
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
                    "10.64.0.2:0": {
                        "discovery_sources": {
                            "interfaces": {
                                "ATM3/0/0.2": {
                                    "session": "ldp",
                                    "xmit": True,
                                    "recv": True,
                                    "ldp_id": {
                                        "10.19.14.14:0": {
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
                    "10.94.0.2:0": {
                        "discovery_sources": {
                            "interfaces": {
                                "ATM3/0/0.1": {
                                    "session": "ldp",
                                    "xmit": True,
                                    "recv": True,
                                    "ldp_id": {
                                        "10.19.14.14:0": {
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
         10.66.12.12:0
         Discovery Sources:
         Interfaces:
             ATM1/1/0.1 (tdp):xmit/recv
                 TDP Id:10.229.11.11:0
     VRF vpn1:Local LDP Identifier:
         10.94.0.2:0
         Discovery Sources:
         Interfaces:
             ATM3/0/0.1 (ldp):xmit/recv
                 LDP Id:10.19.14.14:0
     VRF vpn2:Local LDP Identifier:
         10.64.0.2:0
         Discovery Sources:
         Interfaces:
             ATM3/0/0.2 (ldp):xmit/recv
                 LDP Id:10.19.14.14:0
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
                            'enabled': "ospf 65109"
                        },
                        'peer_ldp_ident': '10.169.197.252:0',
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
    Time source is NTP, 16:10:10.780 EST Tue Nov 8 2016

    GigabitEthernet0/0/0:
        LDP configured; LDP-IGP Synchronization enabled.
        Sync status: sync achieved; peer reachable.
        Sync delay time: 0 seconds (0 seconds left)
        IGP holddown time: infinite.
        Peer LDP Ident: 10.169.197.252:0
        IGP enabled: OSPF 65109
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
                                "sync_achieved": False,
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
            SYNC status: sync not achieved; peer reachable.
            IGP holddown time: infinite.
            Peer LDP Ident: 10.0.0.1:0
            IGP enabled: OSPF 1

    '''}

    golden_parsed_output1 = {
        'vrf': {
            'default': {
                'interface': {
                    'GigabitEthernet0/0/0': {
                        'ldp': {
                            'configured': False,
                            'igp_synchronization_enabled': True,
                        },
                        'sync': {
                            'status': {
                                'sync_achieved': False,
                                'peer_reachable': False,
                            },
                            'delay_time': 0,
                            'left_time': 0,
                        },
                        'igp': {
                            'holddown_time': 'infinite',
                            'enabled': 'ospf 88',
                        },
                    },
                    'TenGigabitEthernet0/1/0': {
                        'ldp': {
                            'configured': True,
                            'igp_synchronization_enabled': True,
                        },
                        'sync': {
                            'status': {
                                'sync_achieved': True,
                                'peer_reachable': True,
                            },
                            'delay_time': 0,
                            'left_time': 0,
                        },
                        'igp': {
                            'holddown_time': '1 milliseconds',
                            'enabled': 'ospf 88',
                        },
                        'peer_ldp_ident': '10.169.197.252:0',
                    },
                    'TenGigabitEthernet0/2/0': {
                        'ldp': {
                            'configured': True,
                            'igp_synchronization_enabled': True,
                        },
                        'sync': {
                            'status': {
                                'sync_achieved': True,
                                'peer_reachable': True,
                            },
                            'delay_time': 0,
                            'left_time': 0,
                        },
                        'igp': {
                            'holddown_time': 'infinite',
                            'enabled': 'ospf 88',
                        },
                        'peer_ldp_ident': '192.168.36.220:0',
                    },
                },
            },
        },
    }
    golden_output1 = {'execute.return_value': '''\
        show mpls ldp igp sync

        GigabitEthernet0/0/0:
            LDP not configured; LDP-IGP Synchronization enabled.
            Sync status: sync not achieved; peer not reachable.
            Sync delay time: 0 seconds (0 seconds left)
            IGP holddown time: infinite.
            IGP enabled: OSPF 88
        TenGigabitEthernet0/1/0:
            LDP configured; LDP-IGP Synchronization enabled.
            Sync status: sync achieved; peer reachable.
            Sync delay time: 0 seconds (0 seconds left)
            IGP holddown time: 1 milliseconds.
            Peer LDP Ident: 10.169.197.252:0
            IGP enabled: OSPF 88
        TenGigabitEthernet0/2/0:
            LDP configured; LDP-IGP Synchronization enabled.
            Sync status: sync achieved; peer reachable.
            Sync delay time: 0 seconds (0 seconds left)
            IGP holddown time: infinite.
            Peer LDP Ident: 192.168.36.220:0
            IGP enabled: OSPF 88
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

    def test_golden1(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output1)
        obj = ShowMplsLdpIgpSync(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)


class TestShowMplsForwardingTable(unittest.TestCase):
    dev1 = Device(name='empty')
    dev = Device(name='dev')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
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
    golden_output = {'execute.return_value':'''\
        Router# show mpls forwarding-table
        Local  Outgoing    Prefix            Bytes tag  Outgoing   Next Hop
        tag    tag or VC   or Tunnel Id      switched   interface
        201    Pop tag     10.18.18.18/32    0          PO1/1/0    point2point
               2/35        10.18.18.18/32    0          AT4/1/0.1  point2point
        251    18          10.17.17.17/32    0          PO1/1/0    point2point
    '''}

    golden_parsed_output_2 = {
        "vrf": {
            "default": {
                "local_label": {
                    16: {
                        "outgoing_label_or_vc": {
                            "Pop Label": {
                                "prefix_or_tunnel_id": {
                                    "10.4.1.2-A": {
                                        "outgoing_interface": {
                                            "Ethernet0/0": {
                                                "next_hop": "10.4.1.2",
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
                                    "10.4.1.2-A": {
                                        "outgoing_interface": {
                                            "Ethernet0/0": {
                                                "next_hop": "10.4.1.2",
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
                                    "10.4.1.2-A": {
                                        "outgoing_interface": {
                                            "Ethernet0/0": {
                                                "next_hop": "10.4.1.2",
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
                                    "10.135.15.2-A": {
                                        "outgoing_interface": {
                                            "Ethernet0/1": {
                                                "next_hop": "10.135.15.2",
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
                                    "10.135.15.2-A": {
                                        "outgoing_interface": {
                                            "Ethernet0/1": {
                                                "next_hop": "10.135.15.2",
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
                                    "10.135.15.2-A": {
                                        "outgoing_interface": {
                                            "Ethernet0/1": {
                                                "next_hop": "10.135.15.2",
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
                                    "192.168.0.1/32": {
                                        "outgoing_interface": {
                                            "GigabitEthernet2": {
                                                "next_hop": "192.168.0.2",
                                                "merged": True,
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
                                    "10.70.20.20/32": {
                                        "outgoing_interface": {
                                            "Ethernet0/0": {
                                                "next_hop": "10.4.1.2",
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
                                    "10.30.30.30/32": {
                                        "outgoing_interface": {
                                            "Ethernet0/0": {
                                                "next_hop": "10.4.1.2",
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
                                    "10.25.40.40/32": {
                                        "outgoing_interface": {
                                            "Ethernet0/0": {
                                                "next_hop": "10.4.1.2",
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
                                    "10.55.50.50/32": {
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
                                    "10.220.100.100/32": {
                                        "outgoing_interface": {
                                            "Ethernet0/1": {
                                                "next_hop": "10.135.15.2",
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
                                    "0-10.70.20.20/32-0": {
                                        "outgoing_interface": {
                                            "Ethernet0/0": {
                                                "next_hop": "10.4.1.2",
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
                                    "0-10.30.30.30/32-0": {
                                        "outgoing_interface": {
                                            "Ethernet0/0": {
                                                "next_hop": "10.4.1.2",
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
                                    "0-10.25.40.40/32-0": {
                                        "outgoing_interface": {
                                            "Ethernet0/1": {
                                                "next_hop": "10.135.15.2",
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
                                    "0-10.55.50.50/32-0": {
                                        "outgoing_interface": {
                                            "Ethernet0/1": {
                                                "next_hop": "10.135.15.2",
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
                                    "0-10.220.100.100/32-0": {
                                        "outgoing_interface": {
                                            "Ethernet0/1": {
                                                "next_hop": "10.135.15.2",
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
        show mpls forwarding-table
        Local      Outgoing   Prefix           Bytes Label   Outgoing   Next Hop
        Label      Label      or Tunnel Id     Switched      interface
        16         Pop Label  10.4.1.2-A       0             Et0/0      10.4.1.2
        17         Pop Label  10.4.1.2-A       0             Et0/0      10.4.1.2
        18         Pop Label  10.4.1.2-A       0             Et0/0      10.4.1.2
        19         Pop Label  10.135.15.2-A    0             Et0/1      10.135.15.2
        20         Pop Label  10.135.15.2-A    0             Et0/1      10.135.15.2
        21         Pop Label  10.135.15.2-A    0             Et0/1      10.135.15.2
        22    [M]  Pop Label  192.168.0.1/32  0        Gi2    192.168.0.2
        16110      Pop Label  10.70.20.20/32   0             Et0/0      10.4.1.2
        16120      16120      10.30.30.30/32   0             Et0/0      10.4.1.2
        16130      16130      10.25.40.40/32   0             Et0/0      10.4.1.2
              [T]  16130      10.25.40.40/32   0             Tu1        point2point
        16140 [T]  Pop Label  10.55.50.50/32   0             Tu1        point2point
        16200      Pop Label  10.220.100.100/32   \
                                               0             Et0/1      10.135.15.2
        17100      Pop Label  0-10.70.20.20/32-0   \
                                               0             Et0/0      10.4.1.2
        17200      17200      0-10.30.30.30/32-0   \
                                               0             Et0/0      10.4.1.2
        17300      17300      0-10.25.40.40/32-0   \
                                               0             Et0/1      10.135.15.2
        17400      17400      0-10.55.50.50/32-0   \
                                               0             Et0/1      10.135.15.2
        18000      Pop Label  0-10.220.100.100/32-0   \
                                               0             Et0/1      10.135.15.2
    '''}

    golden_parsed_output_3 = {
        "vrf": {
            "default": {
                "local_label": {
                    16: {
                        "outgoing_label_or_vc": {
                            "Pop Label": {
                                "prefix_or_tunnel_id": {
                                    "192.168.154.2-A": {
                                        "outgoing_interface": {
                                            "GigabitEthernet0/1/2": {
                                                "bytes_label_switched": 0,
                                                "next_hop": "192.168.154.2"
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
                                    "192.168.4.2-A": {
                                        "outgoing_interface": {
                                            "GigabitEthernet0/1/1": {
                                                "bytes_label_switched": 0,
                                                "next_hop": "192.168.4.2"
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
                                    "192.168.111.2-A": {
                                        "outgoing_interface": {
                                            "GigabitEthernet0/1/0": {
                                                "bytes_label_switched": 0,
                                                "next_hop": "192.168.111.2"
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
                                    "192.168.220.2-A": {
                                        "outgoing_interface": {
                                            "TenGigabitEthernet0/0/0": {
                                                "bytes_label_switched": 0,
                                                "next_hop": "192.168.220.2"
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    16002: {
                        "outgoing_label_or_vc": {
                            "Pop Label": {
                                "prefix_or_tunnel_id": {
                                    "10.16.2.2/32": {
                                        "outgoing_interface": {
                                            "GigabitEthernet0/1/0": {
                                                "bytes_label_switched": 0,
                                                "next_hop": "192.168.111.2"
                                            },
                                            "GigabitEthernet0/1/1": {
                                                "bytes_label_switched": 0,
                                                "next_hop": "192.168.4.2"
                                            },
                                            "GigabitEthernet0/1/2": {
                                                "bytes_label_switched": 0,
                                                "next_hop": "192.168.154.2"
                                            },
                                            "TenGigabitEthernet0/0/0": {
                                                "bytes_label_switched": 0,
                                                "next_hop": "192.168.220.2"
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
    golden_output_3 = {'execute.return_value':'''
        PE1#show mpls forwarding-table
        Local      Outgoing   Prefix           Bytes Label   Outgoing   Next Hop   
        Label      Label      or Tunnel Id     Switched      interface             
        16         Pop Label  192.168.154.2-A      0             Gi0/1/2    192.168.154.2  
        17         Pop Label  192.168.4.2-A      0             Gi0/1/1    192.168.4.2  
        18         Pop Label  192.168.111.2-A      0             Gi0/1/0    192.168.111.2  
        19         Pop Label  192.168.220.2-A      0             Te0/0/0    192.168.220.2  
        16002      Pop Label  10.16.2.2/32       0             Te0/0/0    192.168.220.2  
                   Pop Label  10.16.2.2/32       0             Gi0/1/0    192.168.111.2  
                   Pop Label  10.16.2.2/32       0             Gi0/1/1    192.168.4.2  
                   Pop Label  10.16.2.2/32       0             Gi0/1/2    192.168.154.2  
         
        A  - Adjacency SID
        PE1#
    '''}

    golden_parsed_output_4 = {
        "vrf": {
            "default": {
                "local_label": {
                    16022: {
                        "outgoing_label_or_vc": {
                            "Pop Label": {
                                "prefix_or_tunnel_id": {
                                    "10.151.22.22/32": {
                                        "outgoing_interface": {
                                            "GigabitEthernet4": {
                                                "next_hop": "10.0.0.13",
                                                "bytes_label_switched": 0
                                            },
                                            "GigabitEthernet5": {
                                                "next_hop": "10.0.0.25",
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
    golden_output_4 = {'execute.return_value':'''
        #show mpls forwarding-table 10.151.22.22
        Local      Outgoing   Prefix           Bytes Label   Outgoing   Next Hop    
        Label      Label      or Tunnel Id     Switched      interface              
        16022      Pop Label  10.151.22.22/32   0             Gi4        10.0.0.13   
                   Pop Label  10.151.22.22/32   0             Gi5        10.0.0.25    
    '''}

    golden_parsed_output_5 = {
        "vrf": {
            "default": {
                "local_label": {
                    "None": {
                        "outgoing_label_or_vc": {
                            "No Label": {
                                "prefix_or_tunnel_id": {
                                    "10.0.0.16/30": {
                                        "outgoing_interface": {
                                            "GigabitEthernet3": {
                                                "next_hop": "10.0.0.9",
                                                "bytes_label_switched": 0
                                            },
                                            "GigabitEthernet4": {
                                                "next_hop": "10.0.0.13",
                                                "bytes_label_switched": 0
                                            },
                                            "GigabitEthernet5": {
                                                "next_hop": "10.0.0.25",
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
    golden_output_5 = {'execute.return_value':'''
        show mpls forwarding-table 10.0.0.16
        Local      Outgoing   Prefix           Bytes Label   Outgoing   Next Hop    
        Label      Label      or Tunnel Id     Switched      interface              
        None       No Label   10.0.0.16/30     0             Gi3        10.0.0.9    
                   No Label   10.0.0.16/30     0             Gi4        10.0.0.13   
                   No Label   10.0.0.16/30     0             Gi5        10.0.0.25     
    '''}

    golden_parsed_output_6 = {
        "vrf": {
            "default": {
                "local_label": {
                    24: {
                        "outgoing_label_or_vc": {
                            "No Label": {
                                "prefix_or_tunnel_id": {
                                    "10.23.120.0/24": {
                                        "outgoing_interface": {
                                            "GigabitEthernet2.120": {
                                                "next_hop": "10.12.120.2",
                                                "bytes_label_switched": 0
                                            },
                                            "GigabitEthernet3.120": {
                                                "next_hop": "10.13.120.3",
                                                "bytes_label_switched": 0
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    25: {
                        "outgoing_label_or_vc": {
                            "No Label": {
                                "prefix_or_tunnel_id": {
                                    "10.23.120.0/24[V]": {
                                        "outgoing_interface": {
                                            "GigabitEthernet2.420": {
                                                "next_hop": "10.12.120.2",
                                                "bytes_label_switched": 0
                                            },
                                            "GigabitEthernet3.420": {
                                                "next_hop": "10.13.120.3",
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
    golden_output_6 = {'execute.return_value':'''
        show mpls forwarding-table
        Local      Outgoing   Prefix           Bytes Label   Outgoing   Next Hop
        Label      Label      or Tunnel Id     Switched      interface
        24      No Label   10.23.120.0/24   0             Gi2.120    10.12.120.2
                No Label   10.23.120.0/24   0             Gi3.120    10.13.120.3
        25      No Label   10.23.120.0/24[V]   \
                                            0             Gi2.420    10.12.120.2
                No Label   10.23.120.0/24[V]   \
                                            0             Gi3.420    10.13.120.3  
    '''}

    golden_output_7 = {'execute.return_value': '''
    Local      Outgoing   Prefix           Bytes Label   Outgoing   Next Hop    
    Label      Label      or Tunnel Id     Switched      interface              
    39    [M]  16052      10.169.14.241/32   \
                                           0             Gi0/1/7    10.169.196.217
    16052 [M]  16052      10.169.14.241/32   \
                                           0             Gi0/1/7    10.169.196.217
    '''}

    golden_parsed_output_7 = {
    'vrf': {
        'default': {
            'local_label': {
                39: {
                    'outgoing_label_or_vc': {
                        '16052': {
                            'prefix_or_tunnel_id': {
                                '10.169.14.241/32': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/1/7': {
                                            'bytes_label_switched': 0,
                                            'merged': True,
                                            'next_hop': '10.169.196.217',
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
                16052: {
                    'outgoing_label_or_vc': {
                        '16052': {
                            'prefix_or_tunnel_id': {
                                '10.169.14.241/32': {
                                    'outgoing_interface': {
                                        'GigabitEthernet0/1/7': {
                                            'bytes_label_switched': 0,
                                            'merged': True,
                                            'next_hop': '10.169.196.217',
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    },
}

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowMplsForwardingTable(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output)
        obj = ShowMplsForwardingTable(device=self.dev)
        parsed_output = obj.parse()
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
        parsed_output = obj.parse(prefix='10.16.2.2')
        self.assertEqual(parsed_output, self.golden_parsed_output_4)

    def test_golden_5(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output_5)
        obj = ShowMplsForwardingTable(device=self.dev)
        parsed_output = obj.parse(prefix='10.0.0.16')
        self.assertEqual(parsed_output, self.golden_parsed_output_5)

    def test_golden_6(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output_6)
        obj = ShowMplsForwardingTable(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_6)

    def test_golden_7(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output_7)
        obj = ShowMplsForwardingTable(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_7)


class test_show_mpls_forwarding_table_detail(unittest.TestCase):
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
                                                "label_stack": "",
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
                                                "label_stack": "",
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
                                                "label_stack": "",
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
        Time source is NTP, 20:29:27.645 EST Fri Nov 11 2016

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
    '''}

    golden_parsed_output_2 = {
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
                                                "label_stack": "16",
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
                                                "label_stack": "",
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
    golden_output_2 = {'execute.return_value': '''\
        show mpls forwarding-table detail 
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
    '''}

    golden_parsed_output_3 = {
        'vrf': {
            'default': {
                'local_label': {
                    40: {
                        'outgoing_label_or_vc': {
                            'Pop Label': {
                                'prefix_or_tunnel_id': {
                                    '65536/1[TE-Bind]': {
                                        'outgoing_interface': {
                                            'Tunnel65536': {
                                                'next_hop': 'point2point',
                                                'bytes_label_switched': 0,
                                                'mac': 14,
                                                'encaps': 26,
                                                'mru': 1492,
                                                'label_stack': '16052 16062 16063',
                                                'via': 'GigabitEthernet0/1/7',
                                                'macstr': '0050568DA282BC16652F3A178847',
                                                'lstack': '03EB400003EBE00003EBF000',
                                                'output_feature_configured': False,
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }
    golden_output_3 = {'execute.return_value': '''\
        PE1# show mpls forwarding-table labels 40 detail
        Local      Outgoing   Prefix           Bytes Label   Outgoing   Next Hop
        Label      Label      or Tunnel Id     Switched      interface
        40         Pop Label  65536/1[TE-Bind] 0             Tu65536    point2point
                MAC/Encaps=14/26, MRU=1492, Label Stack{16052 16062 16063}, via Gi0/1/7
                0050568DA282BC16652F3A178847 03EB400003EBE00003EBF000
                No output feature configured
    '''}

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowMplsForwardingTableDetail(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output)
        obj = ShowMplsForwardingTableDetail(device=self.dev)
        parsed_output = obj.parse(vrf='L3VPN-0051')
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_2(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output_2)
        obj = ShowMplsForwardingTableDetail(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

    def test_golden_3(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output_3)
        obj = ShowMplsForwardingTableDetail(device=self.dev)
        parsed_output = obj.parse(label='40')
        self.assertEqual(parsed_output, self.golden_parsed_output_3)


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
    Time source is NTP, 16:10:10.438 EST Tue Nov 8 2016

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
            'ethernet_vlan': {
                2: {
                    'status': 'up',
                    },
                },
            'status': 'up',
            'destination_address': {
                '10.2.2.2': {
                    'default_path': 'active',
                    'imposed_label_stack': '{16}',
                    'next_hop': 'point2point',
                    'output_interface': 'Serial2/0/2',
                    'tunnel_label': 'imp-null',
                    'vc_id': {
                      '1002' : {
                        'vc_status': 'up',
                      },
                    },
                    'preferred_path': 'not configured',
                    },
                },
            'last_status_change_time': '1d00h',
            'line_protocol_status': 'up',
            'signaling_protocol': {
                'LDP': {
                    'peer_id': '10.2.2.2:0',
                    'remote_interface_description': 'xconnect to PE2',
                    'group_id': {
                        'local': '0',
                        'remote': '0',
                        },
                    'peer_state': 'up',
                    'mtu': {
                        'local': '1500',
                        'remote': '1500',
                        },
                    'mpls_vc_labels': {
                        'local': '21',
                        'remote': '16',
                        },
                    },
                },
            'create_time': '1d00h',
            'statistics': {
                'bytes': {
                    'received': 4322368,
                    'sent': 5040220,
                    },
                'packets': {
                    'received': 3466,
                    'sent': 12286,
                    },
                'packets_drop': {
                    'received': 0,
                    'sent': 0,
                    },
                },
            'sequencing': {
                'received': 'disabled',
                'sent': 'disabled',
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
    '''}

    golden_parsed_output_2 = {
    'interface': {
        'VFIPE1-VPLS-A': {
            'signaling_protocol': {
                'LDP': {
                    'mtu': {
                        'remote': '1500',
                        'local': '1500',
                        },
                    'group_id': {
                        'remote': '0',
                        'local': '0',
                        },
                    'peer_id': '10.2.2.2:0',
                    'peer_state': 'up',
                    'mpls_vc_labels': {
                        'remote': '18',
                        'local': '18',
                        },
                    },
                },
            'last_status_change_time': '1d03h',
            'status': 'up',
            'destination_address': {
                '10.2.2.2': {
                    'imposed_label_stack': '{18}',
                    'output_interface': 'Serial2/0',
                    'next_hop': 'point2point',
                    'vc_id': {
                      '100' : {
                        'vc_status': 'up',
                      },
                    },
                    'tunnel_label': 'imp-null',
                    },
                },
            'statistics': {
                'packets_drop': {
                    'received': 0,
                    'sent': 0,
                    },
                'packets': {
                    'received': 0,
                    'sent': 0,
                    },
                'bytes': {
                    'received': 0,
                    'sent': 0,
                    },
                },
            'sequencing': {
                'received': 'disabled',
                'sent': 'disabled',
                },
            'create_time': '3d15h',
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

    golden_parsed_output_3 = {
      'interface': {
          'GigabitEthernet3': {
              'state': 'up',
              'line_protocol_status': 'up',
              'protocol_status': {
                  'Ethernet': 'up',
                  },
              'destination_address': {
                  '10.4.1.1': {
                      'vc_id': {
                          '888': {
                              'vc_status': 'up',
                              },
                          },
                      'output_interface': 'GigabitEthernet2',
                      'imposed_label_stack': '{32}',
                      'preferred_path': 'not configured',
                      'default_path': 'active',
                      'next_hop': '10.1.2.1',
                      },
                  },
              'create_time': '00:00:22',
              'last_status_change_time': '00:00:10',
              'last_label_fsm_state_change_time': '00:00:10',
              'signaling_protocol': {
                  'LDP': {
                      'peer_id': '10.4.1.1:0',
                      'peer_state': 'up',
                      'targeted_hello_ip': '10.16.2.2',
                      'id': '10.4.1.1',
                      'status': 'UP',
                      'mpls_vc_labels': {
                          'local': '17',
                          'remote': '32',
                          },
                      'group_id': {
                          'local': 'n/a',
                          'remote': '0',
                          },
                      'mtu': {
                          'local': '1500',
                          'remote': '1500',
                          },
                      },
                  },
              'graceful_restart': 'not configured and not enabled',
              'non_stop_routing': 'not configured and not enabled',
              'status_tlv_support': 'enabled/supported',
              'ldp_route_enabled': 'enabled',
              'label_state_machine': 'established, LruRru',
              'last_status_name': {
                  'local_dataplane': {
                      'received': 'No fault',
                      },
                  'bfd_dataplane': {
                      'received': 'Not sent',
                      },
                  'bfd_peer_monitor': {
                      'received': 'No fault',
                      },
                  'local_ac__circuit': {
                      'received': 'No fault',
                      'sent': 'No fault',
                      },
                  'local_pw_if_circ': {
                      'received': 'No fault',
                      },
                  'local_ldp_tlv': {
                      'sent': 'No fault',
                      },
                  'remote_ldp_tlv': {
                      'received': 'No fault',
                      },
                  'remote_ldp_adj': {
                      'received': 'No fault',
                      },
                  },
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
                  'packets_drop': {
                      'received': 0,
                      'seq_error': 0,
                      'sent': 0,
                      },
                  },
              },
          },
      }

    golden_output_3 = {'execute.return_value': '''\
      Local interface: Gi3 up, line protocol up, Ethernet up
        Destination address: 10.4.1.1, VC ID: 888, VC status: up
          Output interface: Gi2, imposed label stack {32}
          Preferred path: not configured  
          Default path: active
          Next hop: 10.1.2.1
        Create time: 00:00:22, last status change time: 00:00:10
          Last label FSM state change time: 00:00:10
        Signaling protocol: LDP, peer 10.4.1.1:0 up
          Targeted Hello: 10.16.2.2(LDP Id) -> 10.4.1.1, LDP is UP
          Graceful restart: not configured and not enabled
          Non stop routing: not configured and not enabled
          Status TLV support (local/remote)   : enabled/supported
            LDP route watch                   : enabled
            Label/status state machine        : established, LruRru
            Last local dataplane   status rcvd: No fault
            Last BFD dataplane     status rcvd: Not sent
            Last BFD peer monitor  status rcvd: No fault
            Last local AC  circuit status rcvd: No fault
            Last local AC  circuit status sent: No fault
            Last local PW i/f circ status rcvd: No fault
            Last local LDP TLV     status sent: No fault
            Last remote LDP TLV    status rcvd: No fault
            Last remote LDP ADJ    status rcvd: No fault
          MPLS VC labels: local 17, remote 32 
          Group ID: local n/a, remote 0
          MTU: local 1500, remote 1500
          Remote interface description: 
        Sequencing: receive disabled, send disabled
        Control Word: On (configured: autosense)
        SSO Descriptor: 10.4.1.1/888, local label: 17
        Dataplane:
          SSM segment/switch IDs: 8195/4097 (used), PWID: 1
        VC statistics:
          transit packet totals: receive 0, send 0
          transit byte totals:   receive 0, send 0
          transit packet drops:  receive 0, seq error 0, send 0
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
    
    def test_golden_3(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output_3)
        obj = ShowMplsL2TransportDetail(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_3)


# ============================================
# Parser for 'show mpls l2transport vc'
# ============================================
class test_show_mpls_l2transport_vc(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_output = {'execute.return_value': 
    '''
    Local intf     Local circuit      Dest address    VC ID      Status    
     -------------  ------------------ --------------- ---------- ----------
     Se5/0          FR DLCI 55         10.0.0.1        55         UP        
     AT4/0          ATM AAL5 0/100     10.0.0.1        100        UP        
     AT4/0          ATM AAL5 0/200     10.0.0.1        200        UP        
     AT4/0.300      ATM AAL5 0/300     10.0.0.1        300        UP 
    '''
    }

    golden_output_2 = {'execute.return_value': 
    '''
    Load for five secs: 4%/1%; one minute: 4%; five minutes: 2%
    Time source is hardware calendar, *17:26:56.066 GMT Mon Oct 18 2010


    Local intf     Local circuit              Dest address    VC ID      Status    
    -------------  -------------------------- --------------- ---------- ----------
    VFI auto       VFI                        10.1.1.1        100         UP      
    '''
    }

    golden_parsed_output = {
      'interface': {
          'Serial5/0': {
            'destination_address': {
              '10.0.0.1': {
                  'vc_id': {
                    '55': {
                      'vc_status': 'UP',
                      'local_circuit': 'FR DLCI 55',
                    },
                  },
                },
            },
          },
         'ATM4/0': {
              'destination_address': {
                  '10.0.0.1': {
                      'vc_id': {
                        '100': {
                          'vc_status': 'UP',
                          'local_circuit': 'ATM AAL5 0/100',
                        },
                        '200': {
                          'vc_status': 'UP',
                          'local_circuit': 'ATM AAL5 0/200',
                        },
                      }
                    },
                },
          },
          'ATM4/0.300': {
              'destination_address': {
                  '10.0.0.1': {
                      'vc_id': {
                        '300': {
                          'vc_status': 'UP',
                          'local_circuit': 'ATM AAL5 0/300',
                        },
                      },
                    },
                },
            },
      },
    }
    golden_parsed_output_2 = {
      'interface': {
          'VFI auto': {
              'destination_address': {
                  '10.1.1.1': {
                      'vc_id': {
                        '100' : {
                          'vc_status': 'UP',
                          'local_circuit': 'VFI',
                        }
                      },
                    },
                  },
              },
          },
      }

    golden_parsed_output_3 = {
      'interface': {
          'Serial0/1/0': {
              'destination_address': {
                  '10.0.0.1': {
                      'vc_id': {
                        '101': {
                          'vc_status': 'UP',
                          'local_circuit': 'HDLC',
                          },
                        },
                  },
              },
          },
        },
      }


    golden_output_3 = {'execute.return_value': '''
      Local intf     Local circuit              Dest address    VC ID      Status    
      -------------  -------------------------- --------------- ---------- ----------
      Se0/1/0:0       HDLC                        10.0.0.1        101         UP      

    '''
    }
    def test_empty(self):
            self.device = Mock(**self.empty_output)
            obj = ShowMplsL2TransportVC(device=self.device)
            with self.assertRaises(SchemaEmptyParserError):
                parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowMplsL2TransportVC(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_2(self):
        self.device = Mock(**self.golden_output_2)
        obj = ShowMplsL2TransportVC(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_2)

    def test_golden_3(self):
        self.device = Mock(**self.golden_output_3)
        obj = ShowMplsL2TransportVC(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_3)

if __name__ == '__main__':
    unittest.main()
