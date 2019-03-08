#!/bin/env python
import unittest
from unittest.mock import Mock
from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                       SchemaMissingKeyError

from genie.libs.parser.iosxe.show_mpls import ShowMplsLdpNeighbor,\
                                              ShowMplsLdpNeighborDetail,\
                                              ShowMplsLdpBindings



class test_show_mpls_ldp_neighbor(unittest.TestCase):
    dev1 = Device(name='empty')
    dev = Device(name='dev1')
    empty_output = {'execute.return_value': '      '}

    golden_parsed_output = {
        'vrf': {
            'default': {
                'neighbor': {
                    '106.162.197.252:0':{
                        'address_bound': ['106.162.197.252',
                                          '27.93.202.49',
                                          '106.162.197.101',
                                          '113.146.190.254',
                                          '106.162.197.93'],
                        'downstream': True,
                        'ldp_source': {
                            'interface': 'GigabitEthernet0/0/0',
                            'src_ip_address': '106.162.197.93'
                        },
                        'local_ldp': '106.162.197.254:0',
                        'msg_rcvd': 852,
                        'msg_sent': 851,
                        'state': 'oper',
                        'tcp_connection': ['106.162.197.252.646',
                                        '106.162.197.254.20170'],
                        'uptime': '04:50:30'
                    },
                    '106.162.197.253:0': {
                        'address_bound': ['20.1.1.2',
                                          '27.93.202.57',
                                          '106.162.197.97'],
                        'downstream': True,
                        'ldp_source': {
                            'interface': 'GigabitEthernet0/0/2',
                            'src_ip_address': '106.162.197.97'
                        },
                        'local_ldp': '106.162.197.254:0',
                        'msg_rcvd': 306,
                        'msg_sent': 858,
                        'state': 'oper',
                        'tcp_connection': ['106.162.197.253.646',
                                           '106.162.197.254.42450'],
                        'uptime': '04:50:30'
                    }
                }
            }
        }
    }

    golden_output = {'execute.return_value': '''\
    Router#show mpls ldp neighbor
Load for five secs: 59%/0%; one minute: 11%; five minutes: 7%
Time source is NTP, 20:53:42.709 JST Fri Nov 11 2016
    Peer LDP Ident: 106.162.197.252:0; Local LDP Ident 106.162.197.254:0
        TCP connection: 106.162.197.252.646 - 106.162.197.254.20170
        State: Oper; Msgs sent/rcvd: 851/852; Downstream
        Up time: 04:50:30
        LDP discovery sources:
          GigabitEthernet0/0/0, Src IP addr: 106.162.197.93
        Addresses bound to peer LDP Ident:
          106.162.197.252 27.93.202.49    106.162.197.101 113.146.190.254
          106.162.197.93
    Peer LDP Ident: 106.162.197.253:0; Local LDP Ident 106.162.197.254:0
        TCP connection: 106.162.197.253.646 - 106.162.197.254.42450
        State: Oper; Msgs sent/rcvd: 858/306; Downstream
        Up time: 04:50:30
        LDP discovery sources:
          GigabitEthernet0/0/2, Src IP addr: 106.162.197.97
        Addresses bound to peer LDP Ident:
          20.1.1.2        27.93.202.57    106.162.197.97
    '''
    }

    golden_parsed_output_vrf = {
    "vrf": {
        "vpn10": {
            "neighbor": {
                "14.14.14.14:0": {
                    "local_ldp": "30.29.0.2:0",
                    "msg_sent": 1423,
                    "downstream": True,
                    "address_bound": [
                        "3.3.36.9",
                        "30.7.0.1",
                        "14.14.14.14",
                        "30.13.0.1",
                        "30.15.0.1",
                        "30.17.0.1",
                        "30.19.0.1",
                        "30.21.0.1",
                        "30.23.0.1",
                        "30.25.0.1",
                        "30.27.0.1",
                        "30.29.0.1",
                        "30.31.0.1",
                        "30.33.0.1",
                        "30.35.0.1",
                        "30.37.0.1",
                        "30.39.0.1",
                        "30.41.0.1",
                        "30.43.0.1",
                        "30.45.0.1",
                        "30.47.0.1",
                        "30.49.0.1",
                        "30.51.0.1",
                        "30.53.0.1",
                        "30.55.0.1",
                        "30.57.0.1",
                        "30.59.0.1",
                        "30.61.0.1",
                        "30.63.0.1",
                        "30.65.0.1",
                        "30.67.0.1",
                        "30.69.0.1",
                        "30.71.0.1",
                        "30.73.0.1",
                        "30.75.0.1",
                        "30.77.0.1",
                        "30.79.0.1",
                        "30.81.0.1",
                        "30.83.0.1",
                        "30.85.0.1",
                        "30.87.0.1",
                        "30.89.0.1",
                        "30.91.0.1",
                        "30.93.0.1",
                        "30.95.0.1",
                        "30.97.0.1",
                        "30.99.0.1",
                        "30.101.0.1",
                        "30.103.0.1",
                        "30.105.0.1",
                        "30.107.0.1",
                        "30.109.0.1",
                        "30.4.0.2",
                        "30.3.0.2"
                    ],
                    "ldp_source": {
                        "interface": "ATM3/0/0.10",
                        "src_ip_address": "14.14.14.10"
                    },
                    "msg_rcvd": 800,
                    "state": "oper",
                    "tcp_connection": [
                        "14.14.14.14.646",
                        "30.29.0.2.11384"
                    ],
                    "uptime": "02:38:11"
                }
            }
        }
    }
}

    golden_output_vrf = {'execute.return_value': '''\
Router# show mpls ldp neighbor vrf vpn10

 Peer LDP Ident: 14.14.14.14:0; Local LDP Ident 30.29.0.2:0
         TCP connection: 14.14.14.14.646 - 30.29.0.2.11384
         State: Oper; Msgs sent/rcvd: 1423/800; Downstream
         Up time: 02:38:11
         LDP discovery sources:
           ATM3/0/0.10, Src IP addr: 14.14.14.10
         Addresses bound to peer LDP Ident:
           3.3.36.9        30.7.0.1        14.14.14.14     30.13.0.1
           30.15.0.1       30.17.0.1       30.19.0.1       30.21.0.1
           30.23.0.1       30.25.0.1       30.27.0.1       30.29.0.1
           30.31.0.1       30.33.0.1       30.35.0.1       30.37.0.1
           30.39.0.1       30.41.0.1       30.43.0.1       30.45.0.1
           30.47.0.1       30.49.0.1       30.51.0.1       30.53.0.1
           30.55.0.1       30.57.0.1       30.59.0.1       30.61.0.1
           30.63.0.1       30.65.0.1       30.67.0.1       30.69.0.1
           30.71.0.1       30.73.0.1       30.75.0.1       30.77.0.1
           30.79.0.1       30.81.0.1       30.83.0.1       30.85.0.1
           30.87.0.1       30.89.0.1       30.91.0.1       30.93.0.1
           30.95.0.1       30.97.0.1       30.99.0.1       30.101.0.1
           30.103.0.1      30.105.0.1      30.107.0.1      30.109.0.1
           30.4.0.2        30.3.0.2
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
            "neighbor": {
                "106.162.197.252:0": {
                    "msg_sent": 9981,
                    "address_bound": [
                        "106.162.197.252",
                        "202.239.165.49",
                        "27.93.202.49",
                        "202.239.165.57",
                        "106.162.197.101",
                        "106.162.197.93",
                        "111.111.111.2",
                        "113.146.190.254"
                    ],
                    "nsr": "Not Ready",
                    "capabilities_sent": {
                        "typed_wildcard": "0x050B",
                        "dynamic_anouncement": "0x0506",
                        "min_version": 0,
                        "mldp_point_to_multipoint": "0x0508",
                        "maj_version": 1,
                        "mldp_multipoint_to_multipoint": "0x0509",
                        "iccp_type": "0x0405"
                    },
                    "local_ldp": "106.162.197.254:0",
                    "password": "not required, none, in use",
                    "last_tib_rev_sent": 4103,
                    "ldp_source": {
                        "src_ip_address": "106.162.197.93",
                        "holdtime_ms": 15000,
                        "interface": "GigabitEthernet0/0/0",
                        "hello_interval_ms": 5000
                    },
                    "downstream": True,
                    "capabilities_received": {
                        "typed_wildcard": "0x050B",
                        "dynamic_anouncement": "0x0506",
                        "min_version": 0,
                        "mldp_point_to_multipoint": "0x0508",
                        "maj_version": 1,
                        "mldp_multipoint_to_multipoint": "0x0509",
                        "iccp_type": "0x0405"
                    },
                    "msg_rcvd": 10004,
                    "tcp_connection": [
                        "106.162.197.252.646",
                        "106.162.197.254.44315"
                    ],
                    "state": "oper",
                    "uptime": "3d21h"
                },
                "106.162.197.253:0": {
                    "msg_sent": 9966,
                    "address_bound": [
                        "27.93.202.57",
                        "106.162.197.97"
                    ],
                    "nsr": "Not Ready",
                    "capabilities_sent": {
                        "typed_wildcard": "0x050B",
                        "dynamic_anouncement": "0x0506",
                        "min_version": 0,
                        "mldp_point_to_multipoint": "0x0508",
                        "maj_version": 1,
                        "mldp_multipoint_to_multipoint": "0x0509",
                        "iccp_type": "0x0405"
                    },
                    "local_ldp": "106.162.197.254:0",
                    "password": "not required, none, in use",
                    "last_tib_rev_sent": 4103,
                    "ldp_source": {
                        "src_ip_address": "106.162.197.97",
                        "holdtime_ms": 15000,
                        "interface": "GigabitEthernet0/0/2",
                        "hello_interval_ms": 5000
                    },
                    "downstream": True,
                    "msg_rcvd": 9153,
                    "tcp_connection": [
                        "106.162.197.253.646",
                        "106.162.197.254.34904"
                    ],
                    "state": "oper",
                    "uptime": "3d21h"
                }
            }
        }
    }
}

    golden_output = {'execute.return_value': '''\
    Router#show mpls ldp neighbor detail
    Load for five secs: 2%/0%; one minute: 5%; five minutes: 5%
    Time source is NTP, 16:10:10.569 JST Tue Nov 8 2016
        Peer LDP Ident: 106.162.197.252:0; Local LDP Ident 106.162.197.254:0
            TCP connection: 106.162.197.252.646 - 106.162.197.254.44315
            Password: not required, none, in use
            State: Oper; Msgs sent/rcvd: 9981/10004; Downstream; Last TIB rev sent 4103
            Up time: 3d21h; UID: 4; Peer Id 0
            LDP discovery sources:
              GigabitEthernet0/0/0; Src IP addr: 106.162.197.93
                holdtime: 15000 ms, hello interval: 5000 ms
            Addresses bound to peer LDP Ident:
              106.162.197.252 202.239.165.49  27.93.202.49    202.239.165.57
              106.162.197.101 106.162.197.93  111.111.111.2   113.146.190.254
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
        Peer LDP Ident: 106.162.197.253:0; Local LDP Ident 106.162.197.254:0
            TCP connection: 106.162.197.253.646 - 106.162.197.254.34904
            Password: not required, none, in use
            State: Oper; Msgs sent/rcvd: 9966/9153; Downstream; Last TIB rev sent 4103
            Up time: 3d21h; UID: 5; Peer Id 1
            LDP discovery sources:
              GigabitEthernet0/0/2; Src IP addr: 106.162.197.97
                holdtime: 15000 ms, hello interval: 5000 ms
            Addresses bound to peer LDP Ident:
              27.93.202.57    106.162.197.97
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
    "lib_entry": {
        "27.93.202.64/32": {
            "rev": "1020",
            "remote_binding": {
                "index": {
                    1: {
                        "lsr": "106.162.197.252:0",
                        "label": "506"
                    },
                    2: {
                        "lsr": "106.162.197.253:0",
                        "label": "399712"
                    }
                }
            },
            "local_binding": {
                "label": "2532"
            }
        },
        "27.93.202.56/30": {
            "rev": "1024",
            "remote_binding": {
                "index": {
                    1: {
                        "lsr": "106.162.197.252:0",
                        "label": "505"
                    }
                }
            },
            "local_binding": {
                "label": "2534"
            }
        },
        "27.93.202.48/30": {
            "rev": "1034",
            "remote_binding": {
                "index": {
                    1: {
                        "lsr": "106.162.197.252:0",
                        "label": "imp-null"
                    }
                }
            },
            "local_binding": {
                "label": "2539"
            }
        },
        "20.1.1.0/24": {
            "rev": "1028",
            "remote_binding": {
                "index": {
                    1: {
                        "lsr": "106.162.197.252:0",
                        "label": "508"
                    }
                }
            },
            "local_binding": {
                "label": "2536"
            }
        },
        "106.162.197.96/30": {
            "rev": "4",
            "remote_binding": {
                "index": {
                    1: {
                        "lsr": "106.162.197.252:0",
                        "label": "1002"
                    }
                }
            },
            "local_binding": {
                "label": "imp-null"
            }
        },
        "106.162.197.92/30": {
            "rev": "2",
            "remote_binding": {
                "index": {
                    1: {
                        "lsr": "106.162.197.252:0",
                        "label": "imp-null"
                    },
                    2: {
                        "lsr": "106.162.197.253:0",
                        "label": "736112"
                    }
                }
            },
            "local_binding": {
                "label": "imp-null"
            }
        }
    }
}

    golden_output = {'execute.return_value': '''\
       Router#show mpls ldp bindings
Load for five secs: 55%/0%; one minute: 15%; five minutes: 10%
Time source is NTP, 20:29:28.227 JST Fri Nov 11 2016

  lib entry: 20.1.1.0/24, rev 1028
        local binding:  label: 2536
        remote binding: lsr: 106.162.197.252:0, label: 508
  lib entry: 27.93.202.48/30, rev 1034
        local binding:  label: 2539
        remote binding: lsr: 106.162.197.252:0, label: imp-null
  lib entry: 27.93.202.56/30, rev 1024
        local binding:  label: 2534
        remote binding: lsr: 106.162.197.252:0, label: 505
  lib entry: 27.93.202.64/32, rev 1020
        local binding:  label: 2532
        remote binding: lsr: 106.162.197.252:0, label: 506
        remote binding: lsr: 106.162.197.253:0, label: 399712
  lib entry: 106.162.197.92/30, rev 2
        local binding:  label: imp-null
        remote binding: lsr: 106.162.197.252:0, label: imp-null
        remote binding: lsr: 106.162.197.253:0, label: 736112
  lib entry: 106.162.197.96/30, rev 4
        local binding:  label: imp-null
        remote binding: lsr: 106.162.197.252:0, label: 1002
            '''}

    golden_output_all_detail = {'execute.return_value': '''\
    Router#show mpls ldp bindings all detail
Load for five secs: 2%/0%; one minute: 5%; five minutes: 5%
Time source is NTP, 16:10:10.910 JST Tue Nov 8 2016

  lib entry: 27.93.202.48/30, rev 18, chkpt: none
        local binding:  label: 2030 (owner LDP)
          Advertised to:
          106.162.197.252:0      106.162.197.253:0
        remote binding: lsr: 106.162.197.252:0, label: imp-null checkpointed
  lib entry: 27.93.202.56/30, rev 1085, chkpt: none
        local binding:  label: 6589 (owner LDP)
          Advertised to:
          106.162.197.252:0      106.162.197.253:0
        remote binding: lsr: 106.162.197.252:0, label: 1014 checkpointed
  lib entry: 27.93.202.64/32, rev 12, chkpt: none
        local binding:  label: 2027 (owner LDP)
          Advertised to:
          106.162.197.252:0      106.162.197.253:0
        remote binding: lsr: 106.162.197.252:0, label: 516 checkpointed
        remote binding: lsr: 106.162.197.253:0, label: 308016 checkpointed
  lib entry: 106.162.197.92/30, rev 4, chkpt: none
        local binding:  label: imp-null (owner LDP)
          Advertised to:
          106.162.197.252:0      106.162.197.253:0
        remote binding: lsr: 106.162.197.252:0, label: 126 checkpointed
    '''
    }
    golden_parsed_output_all_detail ={
   "lib_entry": {
      "106.162.197.92/30": {
         "local_binding": {
            "advertised_to": [
               "106.162.197.252:0",
               "106.162.197.253:0"
            ],
            "owner": "LDP",
            "label": "imp-null"
         },
         "checkpoint": "none",
         "rev": "4",
         "remote_binding": {
            "index": {
               1: {
                  "checkpointed": True,
                  "lsr": "106.162.197.252:0",
                  "label": "126"
               }
            }
         }
      },
      "27.93.202.56/30": {
         "local_binding": {
            "advertised_to": [
               "106.162.197.252:0",
               "106.162.197.253:0"
            ],
            "owner": "LDP",
            "label": "6589"
         },
         "checkpoint": "none",
         "rev": "1085",
         "remote_binding": {
            "index": {
               1: {
                  "checkpointed": True,
                  "lsr": "106.162.197.252:0",
                  "label": "1014"
               }
            }
         }
      },
      "27.93.202.48/30": {
         "local_binding": {
            "advertised_to": [
               "106.162.197.252:0",
               "106.162.197.253:0"
            ],
            "owner": "LDP",
            "label": "2030"
         },
         "checkpoint": "none",
         "rev": "18",
         "remote_binding": {
            "index": {
               1: {
                  "checkpointed": True,
                  "lsr": "106.162.197.252:0",
                  "label": "imp-null"
               }
            }
         }
      },
      "27.93.202.64/32": {
         "local_binding": {
            "advertised_to": [
               "106.162.197.252:0",
               "106.162.197.253:0"
            ],
            "owner": "LDP",
            "label": "2027"
         },
         "checkpoint": "none",
         "rev": "12",
         "remote_binding": {
            "index": {
               1: {
                  "checkpointed": True,
                  "lsr": "106.162.197.252:0",
                  "label": "516"
               },
               2: {
                  "checkpointed": True,
                  "lsr": "106.162.197.253:0",
                  "label": "308016"
               }
            }
         }
      }
   }
}

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

if __name__ == '__main__':
    unittest.main()

