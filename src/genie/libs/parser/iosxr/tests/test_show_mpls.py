# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device
from pyats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

# iosxr show_mpls
from genie.libs.parser.iosxr.show_mpls import (ShowMplsLabelRange,
                                               ShowMplsLdpNeighborBrief,
                                               ShowMplsLabelTableDetail,
                                               ShowMplsLabelTablePrivate,
                                               ShowMplsInterfaces,
                                               ShowMplsForwarding,
                                               ShowMplsForwardingVrf,
                                               ShowMplsLdpNeighbor,
                                               ShowMplsLdpNeighborDetail,
                                               ShowMplsLdpDiscovery,
                                               ShowMplsLdpBindings)


# ==================================================
#  Unit test for 'show mpls label range'
# ==================================================
class TestShowMplsLabelRange(unittest.TestCase):

    '''Unit test for 'show mpls label range' '''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'range_for_dynamic_labels': {
            'min_range': 24000,
            'max_range': 1048575
        },
    }

    golden_output = {'execute.return_value': '''
    RP/0/RP0/CPU0:R3#show mpls label range 
    Thu Aug 29 5:24:12.183 UTC
    Range for dynamic labels: Min/Max: 24000/1048575
    '''}

    def test_show_mpls_label_range_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowMplsLabelRange(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_mpls_label_range_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowMplsLabelRange(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


# ==================================================
#  Unit test for 'show mpls ldp neighbor'
# ==================================================
class test_show_mpls_ldp_neighbor(unittest.TestCase):

    empty_output = {'execute.return_value': ''}
    maxDiff = None

    golden_parsed_output = {
        'vrf': {
            'default': {
                'peers': {
                    '10.16.0.2': {
                        'label_space_id': {
                            0: {
                                'tcp_connection': '10.16.0.2:646 - 10.16.0.9:38143',
                                'graceful_restart': 'No',
                                'session_holdtime': 180,
                                'state': 'Oper',
                                'msg_sent': 24710,
                                'msg_rcvd': 24702,
                                'neighbor': 'Downstream-Unsolicited',
                                'uptime': '2w0d',
                                'address_family': {
                                    'ipv4': {
                                        'ldp_discovery_sources': {
                                            'interface': {
                                                'GigabitEthernet0/0/0/0': {}
                                            },
                                        },
                                        'address_bound': ['10.16.0.2', '10.16.27.2', '10.16.28.2', '10.16.29.2']
                                    }
                                }
                            },
                        },
                    },
                    '10.16.0.7': {
                        'label_space_id': {
                            0: {
                                'tcp_connection': '10.16.0.7:646 - 10.16.0.9:19323',
                                'graceful_restart': 'No',
                                'session_holdtime': 180,
                                'state': 'Oper',
                                'msg_sent': 24664,
                                'msg_rcvd': 24686,
                                'neighbor': 'Downstream-Unsolicited',
                                'uptime': '2w0d',
                                'address_family': {
                                    'ipv4': {
                                        'ldp_discovery_sources': {
                                            'interface': {
                                                'GigabitEthernet0/0/0/1': {}
                                            },
                                        },
                                        'address_bound': ['10.16.0.7', '10.16.27.7', '10.16.78.7', '10.16.79.7'],
                                    }
                                }
                            },
                        },
                    },
                },
            }
        }
    }

    golden_output = {'execute.return_value': '''
    RP/0/RP0/CPU0:R9#show mpls ldp neighbor 
    Thu Jan  2 20:51:12.829 UTC
    
    Peer LDP Identifier: 10.16.0.2:0
      TCP connection: 10.16.0.2:646 - 10.16.0.9:38143
      Graceful Restart: No
      Session Holdtime: 180 sec
      State: Oper; Msgs sent/rcvd: 24710/24702; Downstream-Unsolicited
      Up time: 2w0d
      LDP Discovery Sources:
        IPv4: (1)
          GigabitEthernet0/0/0/0
        IPv6: (0)
      Addresses bound to this peer:
        IPv4: (4)
          10.16.0.2        10.16.27.2       10.16.28.2       10.16.29.2       
        IPv6: (0)

    Peer LDP Identifier: 10.16.0.7:0
      TCP connection: 10.16.0.7:646 - 10.16.0.9:19323
      Graceful Restart: No
      Session Holdtime: 180 sec
      State: Oper; Msgs sent/rcvd: 24664/24686; Downstream-Unsolicited
      Up time: 2w0d
      LDP Discovery Sources:
        IPv4: (1)
          GigabitEthernet0/0/0/1
        IPv6: (0)
      Addresses bound to this peer:
        IPv4: (4)
          10.16.0.7        10.16.27.7       10.16.78.7       10.16.79.7  
        IPv6: (0)
    '''}

    def test_empty(self):
        self.dev = Mock(**self.empty_output)
        obj = ShowMplsLdpNeighbor(device=self.dev)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_mpls_ldp_neighbor_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowMplsLdpNeighbor(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


# ==================================================
#  Unit test for 'show mpls ldp neighbor detail'
# ==================================================
class test_show_mpls_ldp_neighbor_detail(unittest.TestCase):

    empty_output = {'execute.return_value': ''}
    maxDiff = None

    golden_parsed_output1 = {
        'vrf': {
            'default': {
                'peers': {
                    '192.168.70.6': {
                        'label_space_id': {
                            0: {
                                'tcp_connection': '192.168.70.6:15332 - 192.168.1.1:646',
                                'graceful_restart': 'Yes (Reconnect Timeout: 120 sec, Recovery: 180 sec)',
                                'session_holdtime': 180,
                                'state': 'Oper',
                                'msg_sent': 851,
                                'msg_rcvd': 232,
                                'neighbor': 'Downstream-Unsolicited',
                                'uptime': '00:02:44',
                                'address_family': {
                                    'ipv4': {
                                        'ldp_discovery_sources': {
                                            'interface': {
                                                'Bundle-Ether1.3': {}
                                            },
                                            'targeted_hello': {
                                                '192.168.1.1': {
                                                    '192.168.70.6': {
                                                        'active': False,
                                                    },
                                                },
                                            }
                                        },
                                        'address_bound': ['10.10.10.1', '10.126.249.223', '10.126.249.224', '10.76.23.2',
                                                          '10.219.1.2', '10.19.1.2', '10.76.1.2', '10.135.1.2',
                                                          '10.151.1.2', '192.168.106.1', '192.168.205.1', '192.168.51.1',
                                                          '192.168.196.1', '192.168.171.1', '192.168.70.6'],
                                    }
                                },
                                'peer_holdtime': 180,
                                'ka_interval': 60,
                                'peer_state': 'Estab',
                                'nsr': 'Operational',
                                'clients': 'Session Protection',
                                'session_protection': {
                                    'session_state': 'Ready',
                                    'duration_int': 86400,
                                },
                                'capabilities': {
                                    'sent': {
                                        '0x508': 'MP: Point-to-Multipoint (P2MP)',
                                        '0x509': 'MP: Multipoint-to-Multipoint (MP2MP)',
                                        '0x50b': 'Typed Wildcard FEC',
                                    },
                                    'received': {
                                        '0x508': 'MP: Point-to-Multipoint (P2MP)',
                                        '0x509': 'MP: Multipoint-to-Multipoint (MP2MP)',
                                        '0x50b': 'Typed Wildcard FEC',
                                    },
                                },
                            },
                        },
                    },
                },
            }
        }
    }

    golden_output1 = {'execute.return_value': ''' 
        RP/0/RP0/CPU0:R2#show mpls ldp neighbor detail

        Peer LDP Identifier: 192.168.70.6:0
          TCP connection: 192.168.70.6:15332 - 192.168.1.1:646
          Graceful Restart: Yes (Reconnect Timeout: 120 sec, Recovery: 180 sec)
          Session Holdtime: 180 sec
          State: Oper; Msgs sent/rcvd: 851/232; Downstream-Unsolicited
          Up time: 00:02:44
          LDP Discovery Sources:
            IPv4: (2)
              Bundle-Ether1.3
              Targeted Hello (192.168.1.1 -> 192.168.70.6, active/passive)
            IPv6: (0)
          Addresses bound to this peer:
            IPv4: (15)
              10.10.10.1     10.126.249.223  10.126.249.224  10.76.23.2
              10.219.1.2       10.19.1.2       10.76.1.2       10.135.1.2
              10.151.1.2       192.168.106.1    192.168.205.1    192.168.51.1
              192.168.196.1     192.168.171.1    192.168.70.6
            IPv6: (0)
          Peer holdtime: 180 sec; KA interval: 60 sec; Peer state: Estab
          NSR: Operational
          Clients: Session Protection
          Session Protection:
            Enabled, state: Ready
            Duration: 86400 sec
          Capabilities:
            Sent:
              0x508  (MP: Point-to-Multipoint (P2MP))
              0x509  (MP: Multipoint-to-Multipoint (MP2MP))
              0x50b  (Typed Wildcard FEC)
            Received:
              0x508  (MP: Point-to-Multipoint (P2MP))
              0x509  (MP: Multipoint-to-Multipoint (MP2MP))
              0x50b  (Typed Wildcard FEC)
    '''
                      }

    golden_parsed_output2 = {
        'vrf': {
            'all': {
                'peers': {
                    '192.168.70.6': {
                        'label_space_id': {
                            0: {
                                'tcp_connection': '192.168.70.6:15332 - 192.168.1.1:646',
                                'graceful_restart': 'Yes (Reconnect Timeout: 120 sec, Recovery: 180 sec)',
                                'session_holdtime': 180,
                                'state': 'Oper',
                                'msg_sent': 851,
                                'msg_rcvd': 232,
                                'neighbor': 'Downstream-Unsolicited',
                                'uptime': '00:02:44',
                                'address_family': {
                                    'ipv4': {
                                        'ldp_discovery_sources': {
                                            'interface': {
                                                'Bundle-Ether1.3': {}
                                            },
                                            'targeted_hello': {
                                                '192.168.1.1': {
                                                    '192.168.70.6': {
                                                        'active': False,
                                                    },
                                                },
                                            }
                                        },
                                        'address_bound': ['10.10.10.1', '10.126.249.223', '10.126.249.224', '10.76.23.2',
                                                          '10.219.1.2', '10.19.1.2', '10.76.1.2', '10.135.1.2',
                                                          '10.151.1.2', '192.168.106.1', '192.168.205.1', '192.168.51.1',
                                                          '192.168.196.1', '192.168.171.1', '192.168.70.6'],
                                    }
                                },
                                'peer_holdtime': 180,
                                'ka_interval': 60,
                                'peer_state': 'Estab',
                                'nsr': 'Operational',
                                'clients': 'Session Protection',
                                'session_protection': {
                                    'session_state': 'Ready',
                                    'duration_int': 86400,
                                },
                                'capabilities': {
                                    'sent': {
                                        '0x508': 'MP: Point-to-Multipoint (P2MP)',
                                        '0x509': 'MP: Multipoint-to-Multipoint (MP2MP)',
                                        '0x50b': 'Typed Wildcard FEC',
                                    },
                                    'received': {
                                        '0x508': 'MP: Point-to-Multipoint (P2MP)',
                                        '0x509': 'MP: Multipoint-to-Multipoint (MP2MP)',
                                        '0x50b': 'Typed Wildcard FEC',
                                    },
                                },
                            },
                        },
                    },
                },
            }
        }
    }

    golden_output2 = {'execute.return_value': ''' 
        RP/0/RP0/CPU0:R2#show mpls ldp vrf all neighbor detail

        Peer LDP Identifier: 192.168.70.6:0
          TCP connection: 192.168.70.6:15332 - 192.168.1.1:646
          Graceful Restart: Yes (Reconnect Timeout: 120 sec, Recovery: 180 sec)
          Session Holdtime: 180 sec
          State: Oper; Msgs sent/rcvd: 851/232; Downstream-Unsolicited
          Up time: 00:02:44
          LDP Discovery Sources:
            IPv4: (2)
              Bundle-Ether1.3
              Targeted Hello (192.168.1.1 -> 192.168.70.6, active/passive)
            IPv6: (0)
          Addresses bound to this peer:
            IPv4: (15)
              10.10.10.1     10.126.249.223  10.126.249.224  10.76.23.2
              10.219.1.2       10.19.1.2       10.76.1.2       10.135.1.2
              10.151.1.2       192.168.106.1    192.168.205.1    192.168.51.1
              192.168.196.1     192.168.171.1    192.168.70.6
            IPv6: (0)
          Peer holdtime: 180 sec; KA interval: 60 sec; Peer state: Estab
          NSR: Operational
          Clients: Session Protection
          Session Protection:
            Enabled, state: Ready
            Duration: 86400 sec
          Capabilities:
            Sent:
              0x508  (MP: Point-to-Multipoint (P2MP))
              0x509  (MP: Multipoint-to-Multipoint (MP2MP))
              0x50b  (Typed Wildcard FEC)
            Received:
              0x508  (MP: Point-to-Multipoint (P2MP))
              0x509  (MP: Multipoint-to-Multipoint (MP2MP))
              0x50b  (Typed Wildcard FEC)
    '''
                      }

    golden_parsed_output3 = {
        'vrf': {
            'default': {
                'peers': {
                    '10.16.0.7': {
                        'label_space_id': {
                            0: {
                                'tcp_connection': '10.16.0.7:646 - 10.16.0.9:19323',
                                'graceful_restart': 'No',
                                'session_holdtime': 180,
                                'state': 'Oper',
                                'msg_sent': 24671,
                                'msg_rcvd': 24693,
                                'neighbor': 'Downstream-Unsolicited',
                                'uptime': '2w1d',
                                'address_family': {
                                    'ipv4': {
                                        'ldp_discovery_sources': {
                                            'interface': {
                                                'GigabitEthernet0/0/0/1': {}
                                            },
                                        },
                                        'address_bound': ['10.16.0.7', '10.16.27.7', '10.16.78.7', '10.16.79.7'],
                                    }
                                },
                                'peer_holdtime': 180,
                                'ka_interval': 60,
                                'peer_state': 'Estab',
                                'nsr': 'Disabled',
                                'capabilities': {
                                    'sent': {
                                        '0x508': 'MP: Point-to-Multipoint (P2MP)',
                                        '0x509': 'MP: Multipoint-to-Multipoint (MP2MP)',
                                        '0x50b': 'Typed Wildcard FEC',
                                    },
                                    'received': {
                                        '0x508': 'MP: Point-to-Multipoint (P2MP)',
                                        '0x509': 'MP: Multipoint-to-Multipoint (MP2MP)',
                                        '0x50b': 'Typed Wildcard FEC',
                                    },
                                },
                            },
                        },
                    },
                },
            }
        }
    }

    golden_output3 = {'execute.return_value': ''' 
    RP/0/RP0/CPU0:R9#show mpls ldp neighbor GigabitEthernet0/0/0/1 detail 
    Thu Jan  2 20:56:36.689 UTC

    Peer LDP Identifier: 10.16.0.7:0
        TCP connection: 10.16.0.7:646 - 10.16.0.9:19323
        Graceful Restart: No
        Session Holdtime: 180 sec
        State: Oper; Msgs sent/rcvd: 24671/24693; Downstream-Unsolicited
        Up time: 2w1d
        LDP Discovery Sources:
          IPv4: (1)
            GigabitEthernet0/0/0/1
          IPv6: (0)
        Addresses bound to this peer:
          IPv4: (4)
            10.16.0.7        10.16.27.7       10.16.78.7       10.16.79.7       
          IPv6: (0)
        Peer holdtime: 180 sec; KA interval: 60 sec; Peer state: Estab
        NSR: Disabled
        Capabilities:
          Sent: 
            0x508  (MP: Point-to-Multipoint (P2MP))
            0x509  (MP: Multipoint-to-Multipoint (MP2MP))
            0x50b  (Typed Wildcard FEC)
          Received: 
            0x508  (MP: Point-to-Multipoint (P2MP))
            0x509  (MP: Multipoint-to-Multipoint (MP2MP))
            0x50b  (Typed Wildcard FEC)
    '''}

    golden_parsed_output4 = {
        'vrf': {
            'Vpn1': {
                'peers': {
                    '10.16.0.7': {
                        'label_space_id': {
                            0: {
                                'tcp_connection': '10.16.0.7:646 - 10.16.0.9:19323',
                                'graceful_restart': 'No',
                                'session_holdtime': 180,
                                'state': 'Oper',
                                'msg_sent': 24671,
                                'msg_rcvd': 24693,
                                'neighbor': 'Downstream-Unsolicited',
                                'uptime': '2w1d',
                                'address_family': {
                                    'ipv4': {
                                        'ldp_discovery_sources': {
                                            'interface': {
                                                'GigabitEthernet0/0/0/1': {}
                                            },
                                        },
                                        'address_bound': ['10.16.0.7', '10.16.27.7', '10.16.78.7', '10.16.79.7'],
                                    }
                                },
                                'peer_holdtime': 180,
                                'ka_interval': 60,
                                'peer_state': 'Estab',
                                'nsr': 'Disabled',
                                'capabilities': {
                                    'sent': {
                                        '0x508': 'MP: Point-to-Multipoint (P2MP)',
                                        '0x509': 'MP: Multipoint-to-Multipoint (MP2MP)',
                                        '0x50b': 'Typed Wildcard FEC',
                                    },
                                    'received': {
                                        '0x508': 'MP: Point-to-Multipoint (P2MP)',
                                        '0x509': 'MP: Multipoint-to-Multipoint (MP2MP)',
                                        '0x50b': 'Typed Wildcard FEC',
                                    },
                                },
                            },
                        },
                    },
                },
            }
        }
    }

    golden_output4 = {'execute.return_value': ''' 
    RP/0/RP0/CPU0:R9#show mpls ldp neighbor vrf Vpn1 GigabitEthernet0/0/0/1 detail 
    Thu Jan  2 20:56:36.689 UTC

    Peer LDP Identifier: 10.16.0.7:0
        TCP connection: 10.16.0.7:646 - 10.16.0.9:19323
        Graceful Restart: No
        Session Holdtime: 180 sec
        State: Oper; Msgs sent/rcvd: 24671/24693; Downstream-Unsolicited
        Up time: 2w1d
        LDP Discovery Sources:
          IPv4: (1)
            GigabitEthernet0/0/0/1
          IPv6: (0)
        Addresses bound to this peer:
          IPv4: (4)
            10.16.0.7        10.16.27.7       10.16.78.7       10.16.79.7       
          IPv6: (0)
        Peer holdtime: 180 sec; KA interval: 60 sec; Peer state: Estab
        NSR: Disabled
        Capabilities:
          Sent: 
            0x508  (MP: Point-to-Multipoint (P2MP))
            0x509  (MP: Multipoint-to-Multipoint (MP2MP))
            0x50b  (Typed Wildcard FEC)
          Received: 
            0x508  (MP: Point-to-Multipoint (P2MP))
            0x509  (MP: Multipoint-to-Multipoint (MP2MP))
            0x50b  (Typed Wildcard FEC)
    '''}

    def test_empty(self):
        self.dev = Mock(**self.empty_output)
        obj = ShowMplsLdpNeighborDetail(device=self.dev)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_mpls_ldp_neighbor_detail_golden1(self):
        self.device = Mock(**self.golden_output1)
        obj = ShowMplsLdpNeighborDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_mpls_ldp_neighbor_detail_golden2(self):
        self.device = Mock(**self.golden_output2)
        obj = ShowMplsLdpNeighborDetail(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_mpls_ldp_neighbor_detail_golden3(self):
        self.device = Mock(**self.golden_output3)
        obj = ShowMplsLdpNeighborDetail(device=self.device)
        parsed_output = obj.parse(interface='GigabitEthernet0/0/0/1')
        self.assertEqual(parsed_output, self.golden_parsed_output3)

    def test_show_mpls_ldp_neighbor_detail_golden4(self):
        self.device = Mock(**self.golden_output4)
        obj = ShowMplsLdpNeighborDetail(device=self.device)
        parsed_output = obj.parse(
            vrf='Vpn1', interface='GigabitEthernet0/0/0/1')
        self.assertEqual(parsed_output, self.golden_parsed_output4)



# ==================================================
#  Unit test for 'show mpls label table detail'
# ==================================================
class TestShowMplsLabelTableDetail(unittest.TestCase):

    '''Unit test for show mpls label table detail'''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'table': {
            0: {
                'label': {
                    0: {
                        'owner': {
                            'LSD(A)': {
                                'state': 'InUse',
                                'rewrite': 'Yes'
                            },
                        },
                    },
                    1: {
                        'owner': {
                            'LSD(A)': {
                                'state': 'InUse',
                                'rewrite': 'Yes'
                            },
                        },
                    },
                    2: {
                        'owner': {
                            'LSD(A)': {
                                'state': 'InUse',
                                'rewrite': 'Yes'
                            },
                        },
                    },
                    13: {
                        'owner': {
                            'LSD(A)': {
                                'state': 'InUse',
                                'rewrite': 'Yes'
                            },
                        },
                    },
                    16000: {
                        'owner': {
                            'ISIS(A):SR': {
                                'state': 'InUse',
                                'rewrite': 'No'
                            },
                        },
                        'label_type': {
                            'Lbl-blk SRGB': {
                                'vers': 0,
                                'start_label': 16000,
                                'size': 8000
                            },
                        },
                    },
                    24000: {
                        'owner': {
                            'ISIS(A):SR': {
                                'state': 'InUse',
                                'rewrite': 'Yes'
                            },
                        },
                        'label_type': {
                            'SR Adj Segment IPv4': {
                                'vers': 0,
                                'index': 0,
                                'type': 0,
                                'interface': 'Gi0/0/0/1',
                                'nh': '10.1.2.2'
                            },
                        },
                    },
                    24001: {
                        'owner': {
                            'ISIS(A):SR': {
                                'state': 'InUse',
                                'rewrite': 'Yes'
                            },
                        },
                        'label_type': {
                            'SR Adj Segment IPv4': {
                                'vers': 0,
                                'index': 2,
                                'type': 0,
                                'interface': 'Gi0/0/0/1',
                                'nh': '10.1.2.2'
                            },
                        },
                    },
                    24002: {
                        'owner': {
                            'ISIS(A):SR': {
                                'state': 'InUse',
                                'rewrite': 'Yes'
                            },
                        },
                        'label_type': {
                            'SR Adj Segment IPv4': {
                                'vers': 0,
                                'index': 1,
                                'type': 0,
                                'interface': 'Gi0/0/0/1',
                                'nh': '10.1.2.2'
                            },
                        },
                    },
                    24003: {
                        'owner': {
                            'ISIS(A):SR': {
                                'state': 'InUse',
                                'rewrite': 'Yes'
                            }
                        },
                        'label_type': {
                            'SR Adj Segment IPv4': {
                                'vers': 0,
                                'index': 3,
                                'type': 0,
                                'interface': 'Gi0/0/0/1',
                                'nh': '10.1.2.2'
                            },
                        },
                    },
                },
            },
        },
    }

    golden_output1 = {'execute.return_value': '''
        RP/0/RP0/CPU0:iosxrv9000-1#show mpls label table detail 
        Mon Sep 30 13:26:56.133 EDT
        Table Label   Owner                           State  Rewrite
        ----- ------- ------------------------------- ------ -------
        0     0       LSD(A)                          InUse  Yes
        0     1       LSD(A)                          InUse  Yes
        0     2       LSD(A)                          InUse  Yes
        0     13      LSD(A)                          InUse  Yes
        0     16000   ISIS(A):SR                      InUse  No
          (Lbl-blk SRGB, vers:0, (start_label=16000, size=8000)
        0     24000   ISIS(A):SR                      InUse  Yes
          (SR Adj Segment IPv4, vers:0, index=0, type=0, intf=Gi0/0/0/1, nh=10.1.2.2)
        0     24001   ISIS(A):SR                      InUse  Yes
          (SR Adj Segment IPv4, vers:0, index=2, type=0, intf=Gi0/0/0/1, nh=10.1.2.2)
        0     24002   ISIS(A):SR                      InUse  Yes
          (SR Adj Segment IPv4, vers:0, index=1, type=0, intf=Gi0/0/0/1, nh=10.1.2.2)
        0     24003   ISIS(A):SR                      InUse  Yes
          (SR Adj Segment IPv4, vers:0, index=3, type=0, intf=Gi0/0/0/1, nh=10.1.2.2)
        '''}

    golden_parsed_output2 = {
        'table': {
            0: {
                'label': {
                    0: {
                        'owner': {
                            'LSD(A)': {
                                'state': 'InUse',
                                'rewrite': 'Yes'
                            }
                        }
                    },
                    1: {
                        'owner': {
                            'LSD(A)': {
                                'state': 'InUse',
                                'rewrite': 'Yes'
                            }
                        }
                    },
                    2: {
                        'owner': {
                            'LSD(A)': {
                                'state': 'InUse',
                                'rewrite': 'Yes'
                            }
                        }
                    },
                    13: {
                        'owner': {
                            'LSD(A)': {
                                'state': 'InUse',
                                'rewrite': 'Yes'
                            }
                        }
                    },
                    15000: {
                        'owner': {
                            'LSD(A)': {
                                'state': 'InUse',
                                'rewrite': 'No'
                            }
                        },
                        'label_type': {
                            'Lbl-blk SRLB': {
                                'vers': 0,
                                'start_label': 15000,
                                'size': 1000,
                                'app_notify': 0
                            }
                        }
                    },
                    16000: {
                        'owner': {
                            'ISIS(A):SR': {
                                'state': 'InUse',
                                'rewrite': 'No'
                            }
                        },
                        'label_type': {
                            'Lbl-blk SRGB': {
                                'vers': 0,
                                'start_label': 16000,
                                'size': 7000
                            }
                        }
                    },
                    24000: {
                        'owner': {
                            'ISIS(A):SR': {
                                'state': 'InUse',
                                'rewrite': 'Yes'
                            }
                        },
                        'label_type': {
                            'SR Adj Segment IPv4': {
                                'vers': 0,
                                'index': 0,
                                'type': 0,
                                'interface': 'Gi0/0/0/0',
                                'nh': '10.1.3.1'
                            }
                        }
                    },
                    24001: {
                        'owner': {
                            'ISIS(A):SR': {
                                'state': 'InUse',
                                'rewrite': 'Yes'
                            }
                        },
                        'label_type': {
                            'SR Adj Segment IPv4': {
                                'vers': 0,
                                'index': 2,
                                'type': 0,
                                'interface': 'Gi0/0/0/0',
                                'nh': '10.1.3.1'
                            }
                        }
                    },
                    24002: {
                        'owner': {
                            'ISIS(A):SR': {
                                'state': 'InUse',
                                'rewrite': 'Yes'
                            }
                        },
                        'label_type': {
                            'SR Adj Segment IPv4': {
                                'vers': 0,
                                'index': 1,
                                'type': 0,
                                'interface': 'Gi0/0/0/0',
                                'nh': '10.1.3.1'
                            }
                        }
                    },
                    24003: {
                        'owner': {
                            'ISIS(A):SR': {
                                'state': 'InUse',
                                'rewrite': 'Yes'
                            }
                        },
                        'label_type': {
                            'SR Adj Segment IPv4': {
                                'vers': 0,
                                'index': 3,
                                'type': 0,
                                'interface': 'Gi0/0/0/0',
                                'nh': '10.1.3.1'
                            }
                        }
                    },
                    24004: {
                        'owner': {
                            'ISIS(A):SR': {
                                'state': 'InUse',
                                'rewrite': 'Yes'
                            }
                        },
                        'label_type': {
                            'SR Adj Segment IPv4': {
                                'vers': 0,
                                'index': 0,
                                'type': 0,
                                'interface': 'Gi0/0/0/1',
                                'nh': '10.3.4.4'
                            }
                        }
                    },
                    24005: {
                        'owner': {
                            'ISIS(A):SR': {
                                'state': 'InUse',
                                'rewrite': 'Yes'
                            }
                        },
                        'label_type': {
                            'SR Adj Segment IPv4': {
                                'vers': 0,
                                'index': 2,
                                'type': 0,
                                'interface': 'Gi0/0/0/1',
                                'nh': '10.3.4.4'
                            }
                        }
                    },
                    24006: {
                        'owner': {
                            'ISIS(A):SR': {
                                'state': 'InUse',
                                'rewrite': 'Yes'
                            }
                        },
                        'label_type': {
                            'SR Adj Segment IPv4': {
                                'vers': 0,
                                'index': 1,
                                'type': 0,
                                'interface': 'Gi0/0/0/1',
                                'nh': '10.3.4.4'
                            }
                        }
                    },
                    24007: {
                        'owner': {
                            'ISIS(A):SR': {
                                'state': 'InUse',
                                'rewrite': 'Yes'
                            }
                        },
                        'label_type': {
                            'SR Adj Segment IPv4': {
                                'vers': 0,
                                'index': 3,
                                'type': 0,
                                'interface': 'Gi0/0/0/1',
                                'nh': '10.3.4.4'
                            }
                        }
                    }
                }
            }
        }
    }

    golden_output2 = {'execute.return_value': '''
        RP/0/RP0/CPU0:R3#show mpls label table detail 
        Thu Aug 29 15:33:47.761 UTC
        Table Label   Owner                           State  Rewrite
        ----- ------- ------------------------------- ------ -------
        0     0       LSD(A)                          InUse  Yes
        0     1       LSD(A)                          InUse  Yes
        0     2       LSD(A)                          InUse  Yes
        0     13      LSD(A)                          InUse  Yes
        0     15000   LSD(A)                          InUse  No
          (Lbl-blk SRLB, vers:0, (start_label=15000, size=1000, app_notify=0)
        0     16000   ISIS(A):SR                      InUse  No
          (Lbl-blk SRGB, vers:0, (start_label=16000, size=7000)
        0     24000   ISIS(A):SR                      InUse  Yes
          (SR Adj Segment IPv4, vers:0, index=0, type=0, intf=Gi0/0/0/0, nh=10.1.3.1)
        0     24001   ISIS(A):SR                      InUse  Yes
          (SR Adj Segment IPv4, vers:0, index=2, type=0, intf=Gi0/0/0/0, nh=10.1.3.1)
        0     24002   ISIS(A):SR                      InUse  Yes
          (SR Adj Segment IPv4, vers:0, index=1, type=0, intf=Gi0/0/0/0, nh=10.1.3.1)
        0     24003   ISIS(A):SR                      InUse  Yes
          (SR Adj Segment IPv4, vers:0, index=3, type=0, intf=Gi0/0/0/0, nh=10.1.3.1)
        0     24004   ISIS(A):SR                      InUse  Yes
          (SR Adj Segment IPv4, vers:0, index=0, type=0, intf=Gi0/0/0/1, nh=10.3.4.4)
        0     24005   ISIS(A):SR                      InUse  Yes
          (SR Adj Segment IPv4, vers:0, index=2, type=0, intf=Gi0/0/0/1, nh=10.3.4.4)
        0     24006   ISIS(A):SR                      InUse  Yes
          (SR Adj Segment IPv4, vers:0, index=1, type=0, intf=Gi0/0/0/1, nh=10.3.4.4)
        0     24007   ISIS(A):SR                      InUse  Yes
          (SR Adj Segment IPv4, vers:0, index=3, type=0, intf=Gi0/0/0/1, nh=10.3.4.4)
    '''}
    golden_parsed_output3 = {
        'table': {
            0: {
                'label': {
                    0: {
                        'owner': {
                            'LSD': {
                                'state': 'InUse',
                                'rewrite': 'Yes'
                            }
                        }
                    },
                    1: {
                        'owner': {
                            'LSD': {
                                'state': 'InUse',
                                'rewrite': 'Yes'
                            }
                        }
                    },
                    2: {
                        'owner': {
                            'LSD': {
                                'state': 'InUse',
                                'rewrite': 'Yes'
                            }
                        }
                    },
                    13: {
                        'owner': {
                            'LSD': {
                                'state': 'InUse',
                                'rewrite': 'Yes'
                            }
                        }
                    },
                    44: {
                        'owner': {
                            'Static': {
                                'state': 'InUse',
                                'rewrite': 'No'
                            }
                        },
                        'label_type': {
                            'IPv4': {
                                'vers': 0,
                                'default': True,
                                'prefix': '10.16.2.2/3'
                            }
                        }
                    },
                    1999: {
                        'owner': {
                            'Static': {
                                'state': 'InUse',
                                'rewrite': 'No'
                            }
                        },
                        'label_type': {
                            'IPv4': {
                                'vers': 0,
                                'default': True,
                                'prefix': '10.4.1.1/24'
                            }
                        }
                    },
                    16001: {
                        'owner': {
                            'LDP:lsd_test_ut': {
                                'state': 'InUse',
                                'rewrite': 'No'
                            },
                            'Static:lsd_test_ut': {
                                'state': 'InUse',
                                'rewrite': 'No'
                            }
                        },
                        'label_type': {
                            'IPv4': {
                                'vers': 0,
                                'default': False,
                                'prefix': '10.106.10.10/15'
                            }
                        }
                    },
                    19990: {
                        'owner': {
                            'Static': {
                                'state': 'InUse',
                                'rewrite': 'No'
                            }
                        },
                        'label_type': {
                            'IPv4': {
                                'vers': 0,
                                'default': True,
                                'prefix': '10.4.1.4/24'
                            }
                        }
                    },
                    19999: {
                        'owner': {
                            'Static': {
                                'state': 'InUse',
                                'rewrite': 'No'
                            }
                        },
                        'label_type': {
                            'IPv4': {
                                'vers': 0,
                                'default': True,
                                'prefix': '10.4.1.3/24'
                            }
                        }
                    }
                }
            }
        }
    }

    golden_output3 = {'execute.return_value': ''' 
        RP/0/0/CPU0:Apr 30 16:30:55.494 : mpls_lsd[276]: app_bit:40  app_bit_pnd:0
        show mpls label table detail
        Tue Apr 30 16:31:05.102 EDT
        Table Label   Owner                        State  Rewrite
        ----- ------- ---------------------------- ------ -------
        0     0       LSD                          InUse  Yes
        0     1       LSD                          InUse  Yes
        0     2       LSD                          InUse  Yes
        0     13      LSD                          InUse  Yes
        0     44      Static                       InUse  No
          (IPv4, vers:0, default, 10.16.2.2/3)
        0     1999    Static                       InUse  No
          (IPv4, vers:0, default, 10.4.1.1/24)
        0     16001   LDP:lsd_test_ut              InUse  No
                      Static:lsd_test_ut           InUse  No
          (IPv4, vers:0, , 10.106.10.10/15)
        0     19990   Static                       InUse  No
          (IPv4, vers:0, default, 10.4.1.4/24)
        0     19999   Static                       InUse  No
          (IPv4, vers:0, default, 10.4.1.3/24)
    '''}

    def test_show_mpls_label_table_detail_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowMplsLabelTableDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_mpls_label_table_detail_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowMplsLabelTableDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_mpls_label_table_detail_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowMplsLabelTableDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_mpls_label_table_detail_golden3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        obj = ShowMplsLabelTableDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output3)


# ==================================================
#  Unit test for 'show mpls label table private'
# ==================================================
class TestShowMplsLabelTablePrivate(unittest.TestCase):

    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'table': {
            0: {
                'label': {
                    0: {
                        'owner': {
                            'LSD(A)': {
                                'state': 'InUse',
                                'rewrite': 'Yes'
                            }
                        }
                    },
                    1: {
                        'owner': {
                            'LSD(A)': {
                                'state': 'InUse',
                                'rewrite': 'Yes'
                            }
                        }
                    },
                    2: {
                        'owner': {
                            'LSD(A)': {
                                'state': 'InUse',
                                'rewrite': 'Yes'
                            }
                        }
                    },
                    13: {
                        'owner': {
                            'LSD(A)': {
                                'state': 'InUse',
                                'rewrite': 'Yes'
                            }
                        }
                    },
                    15000: {
                        'owner': {
                            'LSD(A)': {
                                'state': 'InUse',
                                'rewrite': 'No'
                            }
                        }
                    },
                    16000: {
                        'owner': {
                            'ISIS(A):SR': {
                                'state': 'InUse',
                                'rewrite': 'No'
                            }
                        }
                    },
                    24000: {
                        'owner': {
                            'ISIS(A):SR': {
                                'state': 'InUse',
                                'rewrite': 'Yes'
                            }
                        }
                    },
                    24001: {
                        'owner': {
                            'ISIS(A):SR': {
                                'state': 'InUse',
                                'rewrite': 'Yes'
                            }
                        }
                    }
                }
            }
        }
    }

    golden_output = {'execute.return_value': '''
    RP/0/RP0/CPU0:R3#show mpls label table private 
    Thu Aug 29 15:35:09.897 UTC
    Table Label   Owner                           State  Rewrite
    ----- ------- ------------------------------- ------ -------
    0     0       LSD(A)                          InUse  Yes
    0     1       LSD(A)                          InUse  Yes
    0     2       LSD(A)                          InUse  Yes
    0     13      LSD(A)                          InUse  Yes
    0     15000   LSD(A)                          InUse  No
    0     16000   ISIS(A):SR                      InUse  No
    0     24000   ISIS(A):SR                      InUse  Yes
    0     24001   ISIS(A):SR                      InUse  Yes
    '''}

    def test_show_mpls_label_table_private_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowMplsLabelTablePrivate(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_mpls_label_table_private_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowMplsLabelTablePrivate(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


# ==================================================
#  Unit test for 'show mpls interfaces'
# ==================================================
class TestShowMplsInterfaces(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'interfaces': {
            'GigabitEthernet0/0/0/0': {
                'enabled': 'Yes',
                'ldp': 'No',
                'static': 'No',
                'tunnel': 'No',
            },
            'GigabitEthernet0/0/0/1': {
                'enabled': 'Yes',
                'ldp': 'No',
                'static': 'No',
                'tunnel': 'No',
            },
        },
    }
    golden_output1 = {'execute.return_value': '''
        RP/0/RP0/CPU0:R3#show mpls interfaces 
        Thu Aug 29 15:32:55.170 UTC
        Interface                  LDP      Tunnel   Static   Enabled 
        -------------------------- -------- -------- -------- --------
        GigabitEthernet0/0/0/0     No       No       No       Yes
        GigabitEthernet0/0/0/1     No       No       No       Yes
    '''}

    golden_parsed_output2 = {
        'interfaces': {
            'GigabitEthernet0/0/0/0': {
                'enabled': 'Yes',
                'ldp': 'No',
                'static': 'No',
                'tunnel': 'No',
            },
        },
    }
    golden_output2 = {'execute.return_value': '''
        RP/0/RP0/CPU0:R3#show mpls interfaces GigabitEthernet0/0/0/0
        Thu Aug 29 15:32:55.170 UTC
        Interface                  LDP      Tunnel   Static   Enabled 
        -------------------------- -------- -------- -------- --------
        GigabitEthernet0/0/0/0     No       No       No       Yes
    '''}

    def test__empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowMplsInterfaces(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowMplsInterfaces(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowMplsInterfaces(device=self.device)
        parsed_output = obj.parse(interface='GigabitEthernet0/0/0/0')
        self.assertEqual(parsed_output, self.golden_parsed_output2)


# ==================================================
#  Unit test for 'show mpls forwarding'
# ==================================================
class TestShowMplsForwarding(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'local_label': {
            '16001': {
                'outgoing_label': {
                    'Pop': {
                        'prefix_or_id': {
                            'SR Pfx (idx 1)': {
                                'outgoing_interface': {
                                    'GigabitEthernet0/0/0/0': {
                                        'bytes_switched': 0,
                                        'next_hop': '10.1.3.1',
                                    },
                                },
                            },
                        },
                    },
                },
            },
            '16002': {
                'outgoing_label': {
                    '16002': {
                        'prefix_or_id': {
                            'SR Pfx (idx 2)': {
                                'outgoing_interface': {
                                    'GigabitEthernet0/0/0/0': {
                                        'bytes_switched': 0,
                                        'next_hop': '10.1.3.1',
                                    },
                                },
                            },
                        },
                    },
                },
            },
            '16004': {
                'outgoing_label': {
                    'Pop': {
                        'prefix_or_id': {
                            'SR Pfx (idx 4)': {
                                'outgoing_interface': {
                                    'GigabitEthernet0/0/0/1': {
                                        'bytes_switched': 0,
                                        'next_hop': '10.3.4.4',
                                    },
                                },
                            },
                        },
                    },
                },
            },
            '16005': {
                'outgoing_label': {
                    '16005': {
                        'prefix_or_id': {
                            'SR Pfx (idx 5)': {
                                'outgoing_interface': {
                                    'GigabitEthernet0/0/0/0': {
                                        'bytes_switched': 0,
                                        'next_hop': '10.1.3.1',
                                    },
                                },
                            },
                        },
                    },
                },
            },
            '24000': {
                'outgoing_label': {
                    'Pop': {
                        'prefix_or_id': {
                            'SR Adj (idx 0)': {
                                'outgoing_interface': {
                                    'GigabitEthernet0/0/0/0': {
                                        'bytes_switched': 0,
                                        'next_hop': '10.1.3.1',
                                    },
                                },
                            },
                        },
                    },
                },
            },
            '24001': {
                'outgoing_label': {
                    'Pop': {
                        'prefix_or_id': {
                            'SR Adj (idx 2)': {
                                'outgoing_interface': {
                                    'GigabitEthernet0/0/0/0': {
                                        'bytes_switched': 0,
                                        'next_hop': '10.1.3.1',
                                    },
                                },
                            },
                        },
                    },
                },
            },
            '24002': {
                'outgoing_label': {
                    'Pop': {
                        'prefix_or_id': {
                            'SR Adj (idx 1)': {
                                'outgoing_interface': {
                                    'GigabitEthernet0/0/0/0': {
                                        'bytes_switched': 0,
                                        'next_hop': '10.1.3.1',
                                    },
                                },
                            },
                        },
                    },
                },
            },
            '24003': {
                'outgoing_label': {
                    'Pop': {
                        'prefix_or_id': {
                            'SR Adj (idx 3)': {
                                'outgoing_interface': {
                                    'GigabitEthernet0/0/0/0': {
                                        'bytes_switched': 0,
                                        'next_hop': '10.1.3.1',
                                    },
                                },
                            },
                        },
                    },
                },
            },
            '24004': {
                'outgoing_label': {
                    'Pop': {
                        'prefix_or_id': {
                            'SR Adj (idx 0)': {
                                'outgoing_interface': {
                                    'GigabitEthernet0/0/0/1': {
                                        'bytes_switched': 0,
                                        'next_hop': '10.3.4.4',
                                    },
                                },
                            },
                        },
                    },
                },
            },
            '24005': {
                'outgoing_label': {
                    'Pop': {
                        'prefix_or_id': {
                            'SR Adj (idx 2)': {
                                'outgoing_interface': {
                                    'GigabitEthernet0/0/0/1': {
                                        'bytes_switched': 0,
                                        'next_hop': '10.3.4.4',
                                    },
                                },
                            },
                        },
                    },
                },
            },
            '24006': {
                'outgoing_label': {
                    'Pop': {
                        'prefix_or_id': {
                            'SR Adj (idx 1)': {
                                'outgoing_interface': {
                                    'GigabitEthernet0/0/0/1': {
                                        'bytes_switched': 0,
                                        'next_hop': '10.3.4.4',
                                    },
                                },
                            },
                        },
                    },
                },
            },
            '24007': {
                'outgoing_label': {
                    'Pop': {
                        'prefix_or_id': {
                            'SR Adj (idx 3)': {
                                'outgoing_interface': {
                                    'GigabitEthernet0/0/0/1': {
                                        'bytes_switched': 0,
                                        'next_hop': '10.3.4.4',
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }

    golden_output1 = {'execute.return_value': '''
        RP/0/RP0/CPU0:R3#show mpls forwarding 
        Thu Aug 29 15:29:39.411 UTC
        Local  Outgoing    Prefix             Outgoing     Next Hop        Bytes       
        Label  Label       or ID              Interface                    Switched    
        ------ ----------- ------------------ ------------ --------------- ------------
        16001  Pop         SR Pfx (idx 1)     Gi0/0/0/0    10.1.3.1        0           
        16002  16002       SR Pfx (idx 2)     Gi0/0/0/0    10.1.3.1        0           
        16004  Pop         SR Pfx (idx 4)     Gi0/0/0/1    10.3.4.4        0           
        16005  16005       SR Pfx (idx 5)     Gi0/0/0/0    10.1.3.1        0           
        24000  Pop         SR Adj (idx 0)     Gi0/0/0/0    10.1.3.1        0           
        24001  Pop         SR Adj (idx 2)     Gi0/0/0/0    10.1.3.1        0           
        24002  Pop         SR Adj (idx 1)     Gi0/0/0/0    10.1.3.1        0           
        24003  Pop         SR Adj (idx 3)     Gi0/0/0/0    10.1.3.1        0           
        24004  Pop         SR Adj (idx 0)     Gi0/0/0/1    10.3.4.4        0           
        24005  Pop         SR Adj (idx 2)     Gi0/0/0/1    10.3.4.4        0           
        24006  Pop         SR Adj (idx 1)     Gi0/0/0/1    10.3.4.4        0           
        24007  Pop         SR Adj (idx 3)     Gi0/0/0/1    10.3.4.4        0
    '''}

    golden_parsed_output2 = {
        "local_label": {
            "24000": {
                "outgoing_label": {
                    "Unlabelled": {
                        "prefix_or_id": {
                            "10.4.1.1/32": {
                                "outgoing_interface": {
                                    "GigabitEthernet0/0/0/0.90": {
                                        "next_hop": "10.12.90.1",
                                        "bytes_switched": 9321675
                                    }
                                }
                            }
                        }
                    }
                }
            },
            "24002": {
                "outgoing_label": {
                    "Pop": {
                        "prefix_or_id": {
                            "10.13.110.0/24": {
                                "outgoing_interface": {
                                    "GigabitEthernet0/0/0/0.110": {
                                        "next_hop": "10.12.110.1",
                                        "bytes_switched": 0
                                    }
                                }
                            }
                        }
                    }
                }
            },
            "24003": {
                "outgoing_label": {
                    "Unlabelled": {
                        "prefix_or_id": {
                            "10.13.115.0/24": {
                                "outgoing_interface": {
                                    "GigabitEthernet0/0/0/0.115": {
                                        "next_hop": "10.12.115.1",
                                        "bytes_switched": 0
                                    }
                                }
                            }
                        }
                    }
                }
            },
            "24004": {
                "outgoing_label": {
                    "Unlabelled": {
                        "prefix_or_id": {
                            "10.13.90.0/24": {
                                "outgoing_interface": {
                                    "GigabitEthernet0/0/0/0.90": {
                                        "next_hop": "10.12.90.1",
                                        "bytes_switched": 0
                                    },
                                    "GigabitEthernet0/0/0/1.90": {
                                        "next_hop": "10.23.90.3",
                                        "bytes_switched": 0
                                    }
                                }
                            }
                        }
                    }
                }
            },
            "24005": {
                "outgoing_label": {
                    "Unlabelled": {
                        "prefix_or_id": {
                            "2001:1:1:1::1/128[V]": {
                                "outgoing_interface": {
                                    "GigabitEthernet0/0/0/0.390": {
                                        "next_hop": "fe80::f816:3eff:fe53:2cc7",
                                        "bytes_switched": 3928399
                                    }
                                }
                            }
                        }
                    }
                }
            },
            "24006": {
                "outgoing_label": {
                    "Aggregate": {
                        "prefix_or_id": {
                            "VRF1: Per-VRF Aggr[V]": {
                                "outgoing_interface": {
                                    "VRF1": {
                                        "bytes_switched": 832
                                    }
                                }
                            }
                        }
                    }
                }
            },
            "24007": {
                "outgoing_label": {
                    "Unlabelled": {
                        "prefix_or_id": {
                            "2001:3:3:3::3/128[V]": {
                                "outgoing_interface": {
                                    "GigabitEthernet0/0/0/1.390": {
                                        "next_hop": "fe80::5c00:ff:fe02:7",
                                        "bytes_switched": 3762357
                                    }
                                }
                            }
                        }
                    }
                }
            },
            "24008": {
                "outgoing_label": {
                    "Unlabelled": {
                        "prefix_or_id": {
                            "10.4.1.1/32[V]": {
                                "outgoing_interface": {
                                    "GigabitEthernet0/0/0/0.390": {
                                        "next_hop": "10.12.90.1",
                                        "bytes_switched": 6281421
                                    }
                                }
                            }
                        }
                    }
                }
            },
            "24009": {
                "outgoing_label": {
                    "Aggregate": {
                        "prefix_or_id": {
                            "VRF1: Per-VRF Aggr[V]": {
                                "outgoing_interface": {
                                    "VRF1": {
                                        "bytes_switched": 0
                                    }
                                }
                            }
                        }
                    }
                }
            },
            "24010": {
                "outgoing_label": {
                    "Unlabelled": {
                        "prefix_or_id": {
                            "10.36.3.3/32[V]": {
                                "outgoing_interface": {
                                    "GigabitEthernet0/0/0/1.390": {
                                        "next_hop": "10.23.90.3",
                                        "bytes_switched": 7608898
                                    }
                                }
                            }
                        }
                    }
                }
            },
            "24011": {
                "outgoing_label": {
                    "Unlabelled": {
                        "prefix_or_id": {
                            "10.1.0.0/8": {
                                "outgoing_interface": {
                                    "GigabitEthernet0/0/0/0.120": {
                                        "next_hop": "10.12.120.1",
                                        "bytes_switched": 0
                                    }
                                }
                            }
                        }
                    }
                }
            },
            "24012": {
                "outgoing_label": {
                    "Unlabelled": {
                        "prefix_or_id": {
                            "10.13.120.0/24": {
                                "outgoing_interface": {
                                    "GigabitEthernet0/0/0/0.120": {
                                        "next_hop": "10.12.120.1",
                                        "bytes_switched": 0
                                    },
                                    "GigabitEthernet0/0/0/1.120": {
                                        "next_hop": "10.23.120.3",
                                        "bytes_switched": 0
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    golden_output2 = {'execute.return_value': r'''
        show mpls forwarding
        Mon Dec  2 19:56:50.899 UTC
        Local  Outgoing    Prefix             Outgoing     Next Hop        Bytes
        Label  Label       or ID              Interface                    Switched
        ------ ----------- ------------------ ------------ --------------- ------------
        24000  Unlabelled  10.4.1.1/32         Gi0/0/0/0.90 10.12.90.1      9321675
        24002  Pop         10.13.110.0/24     Gi0/0/0/0.110 10.12.110.1     0
        24003  Unlabelled  10.13.115.0/24     Gi0/0/0/0.115 10.12.115.1     0
        24004  Unlabelled  10.13.90.0/24      Gi0/0/0/0.90 10.12.90.1      0
            Unlabelled  10.13.90.0/24      Gi0/0/0/1.90 10.23.90.3      0
        24005  Unlabelled  2001:1:1:1::1/128[V]   \
                                            Gi0/0/0/0.390 fe80::f816:3eff:fe53:2cc7   \
                                                                        3928399
        24006  Aggregate   VRF1: Per-VRF Aggr[V]   \
                                            VRF1                         832
        24007  Unlabelled  2001:3:3:3::3/128[V]   \
                                            Gi0/0/0/1.390 fe80::5c00:ff:fe02:7   \
                                                                        3762357
        24008  Unlabelled  10.4.1.1/32[V]      Gi0/0/0/0.390 10.12.90.1      6281421
        24009  Aggregate   VRF1: Per-VRF Aggr[V]   \
                                            VRF1                         0
        24010  Unlabelled  10.36.3.3/32[V]      Gi0/0/0/1.390 10.23.90.3      7608898
        24011  Unlabelled  10.1.0.0/8          Gi0/0/0/0.120 10.12.120.1     0
        24012  Unlabelled  10.13.120.0/24     Gi0/0/0/0.120 10.12.120.1     0
            Unlabelled  10.13.120.0/24     Gi0/0/0/1.120 10.23.120.3     0
    '''}

    def test__empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowMplsForwarding(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowMplsForwarding(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowMplsForwarding(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)


# ==================================================
#  Unit test for 'show mpls forwarding vrf {vrf}'
# ==================================================
class TestShowMplsForwardingVrf(unittest.TestCase):
    maxDiff = None
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        "vrf": {
            "VRF1": {
                "local_label": {
                    "24005": {
                        "outgoing_label": {
                            "Unlabelled": {
                                "prefix_or_id": {
                                    "2001:1:1:1::1/128[V]": {
                                        "outgoing_interface": {
                                            "GigabitEthernet0/0/0/0.390": {
                                                "next_hop": "fe80::f816:3eff:fe53:2cc7",
                                                "bytes_switched": 4102415
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "24006": {
                        "outgoing_label": {
                            "Aggregate": {
                                "prefix_or_id": {
                                    "VRF1: Per-VRF Aggr[V]": {
                                        "outgoing_interface": {
                                            "VRF1": {
                                                "bytes_switched": 832
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "24007": {
                        "outgoing_label": {
                            "Unlabelled": {
                                "prefix_or_id": {
                                    "2001:3:3:3::3/128[V]": {
                                        "outgoing_interface": {
                                            "GigabitEthernet0/0/0/1.390": {
                                                "next_hop": "fe80::5c00:ff:fe02:7",
                                                "bytes_switched": 3929713
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "24008": {
                        "outgoing_label": {
                            "Unlabelled": {
                                "prefix_or_id": {
                                    "10.4.1.1/32[V]": {
                                        "outgoing_interface": {
                                            "GigabitEthernet0/0/0/0.390": {
                                                "next_hop": "10.12.90.1",
                                                "bytes_switched": 6560001
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "24009": {
                        "outgoing_label": {
                            "Aggregate": {
                                "prefix_or_id": {
                                    "VRF1: Per-VRF Aggr[V]": {
                                        "outgoing_interface": {
                                            "VRF1": {
                                                "bytes_switched": 0
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "24010": {
                        "outgoing_label": {
                            "Unlabelled": {
                                "prefix_or_id": {
                                    "10.36.3.3/32[V]": {
                                        "outgoing_interface": {
                                            "GigabitEthernet0/0/0/1.390": {
                                                "next_hop": "10.23.90.3",
                                                "bytes_switched": 7947290
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

    golden_output1 = {'execute.return_value': r'''
        show mpls forwarding vrf VRF1
        Tue Dec  3 16:00:45.325 UTC
        Local  Outgoing    Prefix             Outgoing     Next Hop        Bytes
        Label  Label       or ID              Interface                    Switched
        ------ ----------- ------------------ ------------ --------------- ------------
        24005  Unlabelled  2001:1:1:1::1/128[V]   \
                                              Gi0/0/0/0.390 fe80::f816:3eff:fe53:2cc7   \
                                                                          4102415
        24006  Aggregate   VRF1: Per-VRF Aggr[V]   \
                                              VRF1                         832
        24007  Unlabelled  2001:3:3:3::3/128[V]   \
                                              Gi0/0/0/1.390 fe80::5c00:ff:fe02:7   \
                                                                          3929713
        24008  Unlabelled  10.4.1.1/32[V]      Gi0/0/0/0.390 10.12.90.1      6560001
        24009  Aggregate   VRF1: Per-VRF Aggr[V]   \
                                              VRF1                         0
        24010  Unlabelled  10.36.3.3/32[V]      Gi0/0/0/1.390 10.23.90.3      7947290
    '''}

    def test__empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowMplsForwardingVrf(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(vrf='default')

    def test_golden(self):
        self.device = Mock(**self.golden_output1)
        obj = ShowMplsForwardingVrf(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output, self.golden_parsed_output1)


# ==================================================
#  Unit test for 'show mpls ldp discovery'
# ==================================================
class TestShowMplsDiscovery(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_output=[
        {
            'cmd': 'show mpls ldp discovery',
            'param': {
                'all': None,
                'detail': None,
                'vrf': None,
                'ldp': None
            },
            'output': {
                'execute.return_value': '''
                                    RP/0/RP0/CPU0:R3# show mpls ldp discovery

                                    Local LDP Identifier: 10.52.26.119:0
                                    Discovery Sources:
                                    Interfaces:
                                        Bundle-Ether1 : xmit/recv
                                        VRF: 'default' (0x60000000)
                                        LDP Id: 10.52.26.124:0, Transport address: 10.52.26.124
                                            Hold time: 15 sec (local:15 sec, peer:15 sec)
                                            Established: Nov  6 14:39:26.164 (5w2d ago)

                                        Bundle-Ether100 : xmit/recv
                                        VRF: 'default' (0x60000000)
                                        LDP Id: 10.52.31.244:0, Transport address: 10.52.31.244
                                            Hold time: 15 sec (local:15 sec, peer:15 sec)
                                            Established: Oct 30 12:06:32.962 (6w2d ago)

                                        Bundle-Ether3 : xmit/recv
                                        VRF: 'default' (0x60000000)
                                        LDP Id: 10.52.31.247:0, Transport address: 10.52.31.247
                                            Hold time: 15 sec (local:15 sec, peer:15 sec)
                                            Established: Dec  1 11:54:28.707 (1w5d ago)

                                        GigabitEthernet0/0/1/1 : xmit/recv
                                        VRF: 'default' (0x60000000)
                                        LDP Id: 10.52.26.123:0, Transport address: 10.52.26.123
                                            Hold time: 15 sec (local:15 sec, peer:15 sec)
                                            Established: Oct 30 12:06:32.786 (6w2d ago)

                                        GigabitEthernet0/0/1/18 : xmit/recv
                                        VRF: 'default' (0x60000000)
                                        LDP Id: 10.52.31.253:0, Transport address: 10.52.31.253
                                            Hold time: 15 sec (local:15 sec, peer:15 sec)
                                            Established: Oct 30 12:06:30.788 (6w2d ago)

                                        GigabitEthernet0/0/1/2 : xmit/recv
                                        VRF: 'default' (0x60000000)
                                        LDP Id: 10.52.26.120:0, Transport address: 10.52.26.120
                                            Hold time: 15 sec (local:15 sec, peer:15 sec)
                                            Established: Oct 30 12:06:27.565 (6w2d ago)

                                        GigabitEthernet0/0/1/6 : xmit/recv
                                        VRF: 'default' (0x60000000)
                                        LDP Id: 10.52.31.250:0, Transport address: 10.52.31.250
                                            Hold time: 15 sec (local:15 sec, peer:15 sec)
                                            Established: Oct 30 12:06:29.720 (6w2d ago)
                                    '''
            },
            'parsed': {
                'vrf': {
                    'default': {
                        'local_ldp_identifier': {
                            '10.52.26.119:0': {
                                'discovery_sources': {
                                    'interfaces': {
                                        'Bundle-Ether1': {
                                            'ldp_id': {
                                                '10.52.26.124:0': {
                                                    'established_date': 'Nov  6 14:39:26.164',
                                                    'established_elapsed': '5w2d',
                                                    'holdtime_sec': 15,
                                                    'proposed_local': 15,
                                                    'proposed_peer': 15
                                                }
                                            },
                                            'recv': True,
                                            'transport_ip_addr': '10.52.26.124',
                                            'xmit': True
                                        },
                                        'Bundle-Ether100': {
                                            'ldp_id': {
                                                '10.52.31.244:0': {
                                                    'established_date': 'Oct 30 12:06:32.962',
                                                    'established_elapsed': '6w2d',
                                                    'holdtime_sec': 15,
                                                    'proposed_local': 15,
                                                    'proposed_peer': 15
                                                }
                                            },
                                            'recv': True,
                                            'transport_ip_addr': '10.52.31.244',
                                            'xmit': True
                                        },
                                        'Bundle-Ether3': {
                                            'ldp_id': {
                                                '10.52.31.247:0': {
                                                    'established_date': 'Dec  1 11:54:28.707',
                                                    'established_elapsed': '1w5d',
                                                    'holdtime_sec': 15,
                                                    'proposed_local': 15,
                                                    'proposed_peer': 15
                                                }
                                            },
                                            'recv': True,
                                            'transport_ip_addr': '10.52.31.247',
                                            'xmit': True
                                        },
                                        'GigabitEthernet0/0/1/1': {
                                            'ldp_id': {
                                                '10.52.26.123:0': {
                                                    'established_date': 'Oct 30 12:06:32.786',
                                                    'established_elapsed': '6w2d',
                                                    'holdtime_sec': 15,
                                                    'proposed_local': 15,
                                                    'proposed_peer': 15
                                                }
                                            },
                                            'recv': True,
                                            'transport_ip_addr': '10.52.26.123',
                                            'xmit': True
                                        },
                                        'GigabitEthernet0/0/1/18': {
                                            'ldp_id': {
                                                '10.52.31.253:0': {
                                                    'established_date': 'Oct 30 12:06:30.788',
                                                    'established_elapsed': '6w2d',
                                                    'holdtime_sec': 15,
                                                    'proposed_local': 15,
                                                    'proposed_peer': 15
                                                }
                                            },
                                            'recv': True,
                                            'transport_ip_addr': '10.52.31.253',
                                            'xmit': True
                                        },
                                        'GigabitEthernet0/0/1/2': {
                                            'ldp_id': {
                                                '10.52.26.120:0': {
                                                    'established_date': 'Oct 30 12:06:27.565',
                                                    'established_elapsed': '6w2d',
                                                    'holdtime_sec': 15,
                                                    'proposed_local': 15,
                                                    'proposed_peer': 15
                                                }
                                            },
                                            'recv': True,
                                            'transport_ip_addr': '10.52.26.120',
                                            'xmit': True
                                        },
                                        'GigabitEthernet0/0/1/6': {
                                            'ldp_id': {
                                                '10.52.31.250:0': {
                                                    'established_date': 'Oct 30 12:06:29.720',
                                                    'established_elapsed': '6w2d',
                                                    'holdtime_sec': 15,
                                                    'proposed_local': 15,
                                                    'proposed_peer': 15
                                                }
                                            },
                                            'recv': True,
                                            'transport_ip_addr': '10.52.31.250',
                                            'xmit': True
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        {
            'cmd': 'show mpls ldp discovery 10.52.26.121',
            'param': {
                'all': None,
                'detail': None,
                'vrf': None,
                'ldp': '10.52.26.121'
            },
            'output': {
                'execute.return_value': '''
                                RP/0/RSP0/CPU0:TSTR2#show mpls ldp discovery 10.52.26.121
                                Mon Dec 21 17:38:00.299 UTC

                                Local LDP Identifier: 10.52.31.247:0
                                Discovery Sources:
                                Interfaces:
                                    TenGigE0/0/0/5.2097 : xmit/recv
                                    VRF: 'default' (0x60000000)
                                    LDP Id: 10.52.26.121:0, Transport address: 10.52.26.121
                                        Hold time: 15 sec (local:15 sec, peer:15 sec)
                                        Established: Dec 18 16:49:16.538 (3d00h ago)
                            '''
            },
            'parsed': {
                'vrf': {
                    'default': {
                        'local_ldp_identifier': {
                            '10.52.31.247:0': {
                                'discovery_sources': {
                                    'interfaces': {
                                        'TenGigE0/0/0/5.2097': {
                                            'ldp_id': {
                                                '10.52.26.121:0': {
                                                    'established_date': 'Dec 18 16:49:16.538',
                                                    'established_elapsed': '3d00h',
                                                    'holdtime_sec': 15,
                                                    'proposed_local': 15,
                                                    'proposed_peer': 15
                                                }
                                            },
                                            'recv': True,
                                            'transport_ip_addr': '10.52.26.121',
                                            'xmit': True
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        {
            'cmd': 'show mpls ldp vrf default discovery',
            'param': {
                'all': None,
                'detail': None,
                'vrf': None,
                'ldp': None
            },
            'output': {
                'execute.return_value': '''
                            RP/0/RSP0/CPU0:TSTR2#show mpls ldp vrf default discovery
                            Mon Dec 21 17:42:39.229 UTC

                            Local LDP Identifier: 10.112.31.247:0
                            Discovery Sources:
                            Interfaces:
                                Bundle-Ether100 : xmit/recv
                                VRF: 'default' (0x60000000)
                                LDP Id: 10.112.31.251:0, Transport address: 10.112.31.251
                                    Hold time: 15 sec (local:15 sec, peer:15 sec)
                                    Established: Dec  1 11:55:00.837 (2w6d ago)

                                Bundle-Ether20 : xmit/recv
                                VRF: 'default' (0x60000000)
                                LDP Id: 10.112.26.126:0, Transport address: 10.112.26.126
                                    Hold time: 15 sec (local:15 sec, peer:15 sec)
                                    Established: Dec 14 12:33:14.549 (1w0d ago)

                                Bundle-Ether3 : xmit/recv
                                VRF: 'default' (0x60000000)
                                LDP Id: 10.112.26.119:0, Transport address: 10.112.26.119
                                    Hold time: 15 sec (local:15 sec, peer:15 sec)
                                    Established: Dec  1 11:55:00.863 (2w6d ago)

                                GigabitEthernet0/0/1/0 : xmit/recv
                                VRF: 'default' (0x60000000)
                                LDP Id: 10.112.31.252:0, Transport address: 10.112.31.252
                                    Hold time: 15 sec (local:15 sec, peer:15 sec)
                                    Established: Dec  1 11:54:50.567 (2w6d ago)

                                GigabitEthernet0/0/1/1 : xmit/recv
                                VRF: 'default' (0x60000000)
                                LDP Id: 10.112.26.126:0, Transport address: 10.112.26.126
                                    Hold time: 15 sec (local:15 sec, peer:15 sec)
                                    Established: Dec 14 12:33:12.454 (1w0d ago)

                                GigabitEthernet0/0/1/18 : xmit/recv
                                VRF: 'default' (0x60000000)
                                LDP Id: 10.112.31.253:0, Transport address: 10.112.31.253
                                    Hold time: 15 sec (local:15 sec, peer:15 sec)
                                    Established: Dec  1 11:54:49.304 (2w6d ago)

                                GigabitEthernet0/0/1/2 : xmit/recv
                                VRF: 'default' (0x60000000)
                                LDP Id: 10.112.26.120:0, Transport address: 10.112.26.120
                                    Hold time: 15 sec (local:15 sec, peer:15 sec)
                                    Established: Dec  1 11:54:49.538 (2w6d ago)

                                GigabitEthernet0/0/1/4 : xmit/recv
                                VRF: 'default' (0x60000000)
                                LDP Id: 10.112.31.245:0, Transport address: 10.112.31.245
                                    Hold time: 15 sec (local:15 sec, peer:15 sec)
                                    Established: Dec  1 11:54:54.341 (2w6d ago)

                                TenGigE0/0/0/4.2096 : xmit
                                VRF: 'default' (0x60000000)


                                TenGigE0/0/0/4.2098 : xmit/recv
                                VRF: 'default' (0x60000000)
                                LDP Id: 10.112.26.29:0, Transport address: 10.112.26.29
                                    Hold time: 15 sec (local:15 sec, peer:15 sec)
                                    Established: Dec 18 14:40:03.639 (3d03h ago)

                                TenGigE0/0/0/5.2095 : xmit
                                VRF: 'default' (0x60000000)


                                TenGigE0/0/0/5.2097 : xmit/recv
                                VRF: 'default' (0x60000000)
                                LDP Id: 10.112.26.121:0, Transport address: 10.112.26.121
                                    Hold time: 15 sec (local:15 sec, peer:15 sec)
                                    Established: Dec 18 16:49:16.538 (3d00h ago)
                        '''
            },
            'parsed': {
                'vrf': {
                    'default': {
                        'local_ldp_identifier': {
                            '10.112.31.247:0': {
                                'discovery_sources': {
                                    'interfaces': {
                                        'Bundle-Ether100': {
                                            'ldp_id': {
                                                '10.112.31.251:0': {
                                                    'established_date': 'Dec  1 11:55:00.837',
                                                    'established_elapsed': '2w6d',
                                                    'holdtime_sec': 15,
                                                    'proposed_local': 15,
                                                    'proposed_peer': 15
                                                }
                                            },
                                            'recv': True,
                                            'transport_ip_addr': '10.112.31.251',
                                            'xmit': True
                                        },
                                        'Bundle-Ether20': {
                                            'ldp_id': {
                                                '10.112.26.126:0': {
                                                    'established_date': 'Dec 14 12:33:14.549',
                                                    'established_elapsed': '1w0d',
                                                    'holdtime_sec': 15,
                                                    'proposed_local': 15,
                                                    'proposed_peer': 15
                                                }
                                            },
                                            'recv': True,
                                            'transport_ip_addr': '10.112.26.126',
                                            'xmit': True
                                        },
                                        'Bundle-Ether3': {
                                            'ldp_id': {
                                                '10.112.26.119:0': {
                                                    'established_date': 'Dec  1 11:55:00.863',
                                                    'established_elapsed': '2w6d',
                                                    'holdtime_sec': 15,
                                                    'proposed_local': 15,
                                                    'proposed_peer': 15
                                                }
                                            },
                                            'recv': True,
                                            'transport_ip_addr': '10.112.26.119',
                                            'xmit': True
                                        },
                                        'GigabitEthernet0/0/1/0': {
                                            'ldp_id': {
                                                '10.112.31.252:0': {
                                                    'established_date': 'Dec  1 11:54:50.567',
                                                    'established_elapsed': '2w6d',
                                                    'holdtime_sec': 15,
                                                    'proposed_local': 15,
                                                    'proposed_peer': 15
                                                }
                                            },
                                            'recv': True,
                                            'transport_ip_addr': '10.112.31.252',
                                            'xmit': True
                                        },
                                        'GigabitEthernet0/0/1/1': {
                                            'ldp_id': {
                                                '10.112.26.126:0': {
                                                    'established_date': 'Dec 14 12:33:12.454',
                                                    'established_elapsed': '1w0d',
                                                    'holdtime_sec': 15,
                                                    'proposed_local': 15,
                                                    'proposed_peer': 15
                                                }
                                            },
                                            'recv': True,
                                            'transport_ip_addr': '10.112.26.126',
                                            'xmit': True
                                        },
                                        'GigabitEthernet0/0/1/18': {
                                            'ldp_id': {
                                                '10.112.31.253:0': {
                                                    'established_date': 'Dec  1 11:54:49.304',
                                                    'established_elapsed': '2w6d',
                                                    'holdtime_sec': 15,
                                                    'proposed_local': 15,
                                                    'proposed_peer': 15
                                                }
                                            },
                                            'recv': True,
                                            'transport_ip_addr': '10.112.31.253',
                                            'xmit': True
                                        },
                                        'GigabitEthernet0/0/1/2': {
                                            'ldp_id': {
                                                '10.112.26.120:0': {
                                                    'established_date': 'Dec  1 11:54:49.538',
                                                    'established_elapsed': '2w6d',
                                                    'holdtime_sec': 15,
                                                    'proposed_local': 15,
                                                    'proposed_peer': 15
                                                }
                                            },
                                            'recv': True,
                                            'transport_ip_addr': '10.112.26.120',
                                            'xmit': True
                                        },
                                        'GigabitEthernet0/0/1/4': {
                                            'ldp_id': {
                                                '10.112.31.245:0': {
                                                    'established_date': 'Dec  1 11:54:54.341',
                                                    'established_elapsed': '2w6d',
                                                    'holdtime_sec': 15,
                                                    'proposed_local': 15,
                                                    'proposed_peer': 15
                                                }
                                            },
                                            'recv': True,
                                            'transport_ip_addr': '10.112.31.245',
                                            'xmit': True
                                        },
                                        'TenGigE0/0/0/4.2096': {
                                            'recv': False,
                                            'xmit': True
                                        },
                                        'TenGigE0/0/0/4.2098': {
                                            'ldp_id': {
                                                '10.112.26.29:0': {
                                                    'established_date': 'Dec 18 14:40:03.639',
                                                    'established_elapsed': '3d03h',
                                                    'holdtime_sec': 15,
                                                    'proposed_local': 15,
                                                    'proposed_peer': 15
                                                }
                                            },
                                            'recv': True,
                                            'transport_ip_addr': '10.112.26.29',
                                            'xmit': True
                                        },
                                        'TenGigE0/0/0/5.2095': {
                                            'recv': False,
                                            'xmit': True
                                        },
                                        'TenGigE0/0/0/5.2097': {
                                            'ldp_id': {
                                                '10.112.26.121:0': {
                                                    'established_date': 'Dec 18 16:49:16.538',
                                                    'established_elapsed': '3d00h',
                                                    'holdtime_sec': 15,
                                                    'proposed_local': 15,
                                                    'proposed_peer': 15
                                                }
                                            },
                                            'recv': True,
                                            'transport_ip_addr': '10.112.26.121',
                                            'xmit': True
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        {
            'cmd': 'show mpls ldp discovery detail',
            'param': {
                'all': None,
                'detail': True,
                'vrf': None,
                'ldp': None
            },
            'output': {
                'execute.return_value': '''
                            P/0/RSP0/CPU0:TSTR2#show mpls ldp discovery detail
                            Mon Dec 21 17:37:08.717 UTC

                            Local LDP Identifier: 10.94.31.247:0
                            Discovery Sources:
                            Interfaces:
                                Bundle-Ether100 (0x80002e0) : xmit/recv
                                VRF: 'default' (0x60000000)
                                Source address: 10.166.0.57; Transport address: 10.94.31.247
                                Hello interval: 5 sec (due in 2.3 sec)
                                Quick-start: Enabled
                                LDP Id: 10.94.31.251:0
                                    Source address: 10.166.0.58; Transport address: 10.94.31.251
                                    Hold time: 15 sec (local:15 sec, peer:15 sec)
                                                (expiring in 13.7 sec)
                                    Established: Dec  1 11:55:00.837 (2w6d ago)

                                Bundle-Ether20 (0x80002a0) : xmit/recv
                                VRF: 'default' (0x60000000)
                                Source address: 10.166.0.25; Transport address: 10.94.31.247
                                Hello interval: 5 sec (due in 514 msec)
                                Quick-start: Enabled
                                LDP Id: 10.94.26.126:0
                                    Source address: 10.166.0.26; Transport address: 10.94.26.126
                                    Hold time: 15 sec (local:15 sec, peer:15 sec)
                                                (expiring in 11.3 sec)
                                    Established: Dec 14 12:33:14.549 (1w0d ago)

                                Bundle-Ether3 (0x8000260) : xmit/recv
                                VRF: 'default' (0x60000000)
                                Source address: 10.166.0.54; Transport address: 10.94.31.247
                                Hello interval: 5 sec (due in 4.5 sec)
                                Quick-start: Enabled
                                LDP Id: 10.94.26.119:0
                                    Source address: 10.166.0.53; Transport address: 10.94.26.119
                                    Hold time: 15 sec (local:15 sec, peer:15 sec)
                                                (expiring in 12.5 sec)
                                    Established: Dec  1 11:55:00.863 (2w6d ago)

                                GigabitEthernet0/0/1/0 (0xc0) : xmit/recv
                                VRF: 'default' (0x60000000)
                                Source address: 10.166.0.65; Transport address: 10.94.31.247
                                Hello interval: 5 sec (due in 4.4 sec)
                                Quick-start: Enabled
                                LDP Id: 10.94.31.252:0
                                    Source address: 10.166.0.66; Transport address: 10.94.31.252
                                    Hold time: 15 sec (local:15 sec, peer:15 sec)
                                                (expiring in 11.2 sec)
                                    Established: Dec  1 11:54:50.567 (2w6d ago)

                                GigabitEthernet0/0/1/1 (0x100) : xmit/recv
                                VRF: 'default' (0x60000000)
                                Source address: 10.166.0.45; Transport address: 10.94.31.247
                                Hello interval: 5 sec (due in 3 sec)
                                Quick-start: Enabled
                                LDP Id: 10.94.26.126:0
                                    Source address: 10.166.0.46; Transport address: 10.94.26.126
                                    Hold time: 15 sec (local:15 sec, peer:15 sec)
                                                (expiring in 14 sec)
                                    Established: Dec 14 12:33:12.454 (1w0d ago)

                                GigabitEthernet0/0/1/18 (0x540) : xmit/recv
                                VRF: 'default' (0x60000000)
                                Source address: 10.166.0.109; Transport address: 10.94.31.247
                                Hello interval: 5 sec (due in 518 msec)
                                Quick-start: Enabled
                                LDP Id: 10.94.31.253:0
                                    Source address: 10.166.0.110; Transport address: 10.94.31.253
                                    Hold time: 15 sec (local:15 sec, peer:15 sec)
                                                (expiring in 11.7 sec)
                                    Established: Dec  1 11:54:49.304 (2w6d ago)

                                GigabitEthernet0/0/1/2 (0x140) : xmit/recv
                                VRF: 'default' (0x60000000)
                                Source address: 10.166.0.29; Transport address: 10.94.31.247
                                Hello interval: 5 sec (due in 232 msec)
                                Quick-start: Enabled
                                LDP Id: 10.94.26.120:0
                                    Source address: 10.166.0.30; Transport address: 10.94.26.120
                                    Hold time: 15 sec (local:15 sec, peer:15 sec)
                                                (expiring in 14.8 sec)
                                    Established: Dec  1 11:54:49.538 (2w6d ago)

                                GigabitEthernet0/0/1/4 (0x1c0) : xmit/recv
                                VRF: 'default' (0x60000000)
                                Source address: 10.166.0.69; Transport address: 10.94.31.247
                                Hello interval: 5 sec (due in 3.7 sec)
                                Quick-start: Enabled
                                LDP Id: 10.94.31.245:0
                                    Source address: 10.166.0.70; Transport address: 10.94.31.245
                                    Hold time: 15 sec (local:15 sec, peer:15 sec)
                                                (expiring in 14.4 sec)
                                    Established: Dec  1 11:54:54.341 (2w6d ago)

                                TenGigE0/0/0/4.2096 (0x14c0) : xmit
                                VRF: 'default' (0x60000000)

                                Source address: 10.166.0.125; Transport address: 10.94.31.247
                                Hello interval: 5 sec (due in 4.1 sec)
                                Quick-start: Enabled

                                TenGigE0/0/0/4.2098 (0x1500) : xmit/recv
                                VRF: 'default' (0x60000000)
                                Source address: 10.166.0.133; Transport address: 10.94.31.247
                                Hello interval: 5 sec (due in 1.2 sec)
                                Quick-start: Enabled
                                LDP Id: 10.94.26.29:0
                                    Source address: 10.166.0.134; Transport address: 10.94.26.29
                                    Hold time: 15 sec (local:15 sec, peer:15 sec)
                                                (expiring in 11.6 sec)
                                    Established: Dec 18 14:40:03.639 (3d02h ago)

                                TenGigE0/0/0/5.2095 (0x1540) : xmit
                                VRF: 'default' (0x60000000)

                                Source address: 10.166.0.149; Transport address: 10.94.31.247
                                Hello interval: 5 sec (due in 2.8 sec)
                                Quick-start: Enabled

                                TenGigE0/0/0/5.2097 (0x1580) : xmit/recv
                                VRF: 'default' (0x60000000)
                                Source address: 10.166.0.137; Transport address: 10.94.31.247
                                Hello interval: 5 sec (due in 772 msec)
                                Quick-start: Enabled
                                LDP Id: 10.94.26.121:0
                                    Source address: 10.166.0.138; Transport address: 10.94.26.121
                                    Hold time: 15 sec (local:15 sec, peer:15 sec)
                                                (expiring in 14.1 sec)
                                    Established: Dec 18 16:49:16.538 (3d00h ago)
                                '''
            },
            'parsed': {
                'vrf': {
                    'default': {
                        'local_ldp_identifier': {
                            '10.94.31.247:0': {
                                'discovery_sources': {
                                    'interfaces': {
                                        'Bundle-Ether100': {
                                            'hello_due_time_ms': 2300,
                                            'hello_interval_ms': 5000,
                                            'ldp_id': {
                                                '10.94.31.251:0': {
                                                    'established_date': 'Dec  1 11:55:00.837',
                                                    'established_elapsed': '2w6d',
                                                    'expiring_in': 13.7,
                                                    'holdtime_sec': 15,
                                                    'proposed_local': 15,
                                                    'proposed_peer': 15,
                                                    'source_ip_addr': '10.166.0.58',
                                                    'transport_ip_addr': '10.94.31.251'
                                                }
                                            },
                                            'quick_start': 'enabled',
                                            'recv': True,
                                            'source_ip_addr': '10.166.0.57',
                                            'transport_ip_addr': '10.94.31.247',
                                            'xmit': True
                                        },
                                        'Bundle-Ether20': {
                                            'hello_due_time_ms': 514,
                                            'hello_interval_ms': 5000,
                                            'ldp_id': {
                                                '10.94.26.126:0': {
                                                    'established_date': 'Dec 14 12:33:14.549',
                                                    'established_elapsed': '1w0d',
                                                    'expiring_in': 11.3,
                                                    'holdtime_sec': 15,
                                                    'proposed_local': 15,
                                                    'proposed_peer': 15,
                                                    'source_ip_addr': '10.166.0.26',
                                                    'transport_ip_addr': '10.94.26.126'
                                                }
                                            },
                                            'quick_start': 'enabled',
                                            'recv': True,
                                            'source_ip_addr': '10.166.0.25',
                                            'transport_ip_addr': '10.94.31.247',
                                            'xmit': True
                                        },
                                        'Bundle-Ether3': {
                                            'hello_due_time_ms': 4500,
                                            'hello_interval_ms': 5000,
                                            'ldp_id': {
                                                '10.94.26.119:0': {
                                                    'established_date': 'Dec  1 11:55:00.863',
                                                    'established_elapsed': '2w6d',
                                                    'expiring_in': 12.5,
                                                    'holdtime_sec': 15,
                                                    'proposed_local': 15,
                                                    'proposed_peer': 15,
                                                    'source_ip_addr': '10.166.0.53',
                                                    'transport_ip_addr': '10.94.26.119'
                                                }
                                            },
                                            'quick_start': 'enabled',
                                            'recv': True,
                                            'source_ip_addr': '10.166.0.54',
                                            'transport_ip_addr': '10.94.31.247',
                                            'xmit': True
                                        },
                                        'GigabitEthernet0/0/1/0': {
                                            'hello_due_time_ms': 4400,
                                            'hello_interval_ms': 5000,
                                            'ldp_id': {
                                                '10.94.31.252:0': {
                                                    'established_date': 'Dec  1 11:54:50.567',
                                                    'established_elapsed': '2w6d',
                                                    'expiring_in': 11.2,
                                                    'holdtime_sec': 15,
                                                    'proposed_local': 15,
                                                    'proposed_peer': 15,
                                                    'source_ip_addr': '10.166.0.66',
                                                    'transport_ip_addr': '10.94.31.252'
                                                }
                                            },
                                            'quick_start': 'enabled',
                                            'recv': True,
                                            'source_ip_addr': '10.166.0.65',
                                            'transport_ip_addr': '10.94.31.247',
                                            'xmit': True
                                        },
                                        'GigabitEthernet0/0/1/1': {
                                            'hello_due_time_ms': 3000,
                                            'hello_interval_ms': 5000,
                                            'ldp_id': {
                                                '10.94.26.126:0': {
                                                    'established_date': 'Dec 14 12:33:12.454',
                                                    'established_elapsed': '1w0d',
                                                    'expiring_in': 14.0,
                                                    'holdtime_sec': 15,
                                                    'proposed_local': 15,
                                                    'proposed_peer': 15,
                                                    'source_ip_addr': '10.166.0.46',
                                                    'transport_ip_addr': '10.94.26.126'
                                                }
                                            },
                                            'quick_start': 'enabled',
                                            'recv': True,
                                            'source_ip_addr': '10.166.0.45',
                                            'transport_ip_addr': '10.94.31.247',
                                            'xmit': True
                                        },
                                        'GigabitEthernet0/0/1/18': {
                                            'hello_due_time_ms': 518,
                                            'hello_interval_ms': 5000,
                                            'ldp_id': {
                                                '10.94.31.253:0': {
                                                    'established_date': 'Dec  1 11:54:49.304',
                                                    'established_elapsed': '2w6d',
                                                    'expiring_in': 11.7,
                                                    'holdtime_sec': 15,
                                                    'proposed_local': 15,
                                                    'proposed_peer': 15,
                                                    'source_ip_addr': '10.166.0.110',
                                                    'transport_ip_addr': '10.94.31.253'
                                                }
                                            },
                                            'quick_start': 'enabled',
                                            'recv': True,
                                            'source_ip_addr': '10.166.0.109',
                                            'transport_ip_addr': '10.94.31.247',
                                            'xmit': True
                                        },
                                        'GigabitEthernet0/0/1/2': {
                                            'hello_due_time_ms': 232,
                                            'hello_interval_ms': 5000,
                                            'ldp_id': {
                                                '10.94.26.120:0': {
                                                    'established_date': 'Dec  1 11:54:49.538',
                                                    'established_elapsed': '2w6d',
                                                    'expiring_in': 14.8,
                                                    'holdtime_sec': 15,
                                                    'proposed_local': 15,
                                                    'proposed_peer': 15,
                                                    'source_ip_addr': '10.166.0.30',
                                                    'transport_ip_addr': '10.94.26.120'
                                                }
                                            },
                                            'quick_start': 'enabled',
                                            'recv': True,
                                            'source_ip_addr': '10.166.0.29',
                                            'transport_ip_addr': '10.94.31.247',
                                            'xmit': True
                                        },
                                        'GigabitEthernet0/0/1/4': {
                                            'hello_due_time_ms': 3700,
                                            'hello_interval_ms': 5000,
                                            'ldp_id': {
                                                '10.94.31.245:0': {
                                                    'established_date': 'Dec  1 11:54:54.341',
                                                    'established_elapsed': '2w6d',
                                                    'expiring_in': 14.4,
                                                    'holdtime_sec': 15,
                                                    'proposed_local': 15,
                                                    'proposed_peer': 15,
                                                    'source_ip_addr': '10.166.0.70',
                                                    'transport_ip_addr': '10.94.31.245'
                                                }
                                            },
                                            'quick_start': 'enabled',
                                            'recv': True,
                                            'source_ip_addr': '10.166.0.69',
                                            'transport_ip_addr': '10.94.31.247',
                                            'xmit': True
                                        },
                                        'TenGigE0/0/0/4.2096': {
                                            'hello_due_time_ms': 4100,
                                            'hello_interval_ms': 5000,
                                            'quick_start': 'enabled',
                                            'recv': False,
                                            'source_ip_addr': '10.166.0.125',
                                            'transport_ip_addr': '10.94.31.247',
                                            'xmit': True
                                        },
                                        'TenGigE0/0/0/4.2098': {
                                            'hello_due_time_ms': 1200,
                                            'hello_interval_ms': 5000,
                                            'ldp_id': {
                                                '10.94.26.29:0': {
                                                    'established_date': 'Dec 18 14:40:03.639',
                                                    'established_elapsed': '3d02h',
                                                    'expiring_in': 11.6,
                                                    'holdtime_sec': 15,
                                                    'proposed_local': 15,
                                                    'proposed_peer': 15,
                                                    'source_ip_addr': '10.166.0.134',
                                                    'transport_ip_addr': '10.94.26.29'
                                                }
                                            },
                                            'quick_start': 'enabled',
                                            'recv': True,
                                            'source_ip_addr': '10.166.0.133',
                                            'transport_ip_addr': '10.94.31.247',
                                            'xmit': True
                                        },
                                        'TenGigE0/0/0/5.2095': {
                                            'hello_due_time_ms': 2800,
                                            'hello_interval_ms': 5000,
                                            'quick_start': 'enabled',
                                            'recv': False,
                                            'source_ip_addr': '10.166.0.149',
                                            'transport_ip_addr': '10.94.31.247',
                                            'xmit': True
                                        },
                                        'TenGigE0/0/0/5.2097': {
                                            'hello_due_time_ms': 772,
                                            'hello_interval_ms': 5000,
                                            'ldp_id': {
                                                '10.94.26.121:0': {
                                                    'established_date': 'Dec 18 16:49:16.538',
                                                    'established_elapsed': '3d00h',
                                                    'expiring_in': 14.1,
                                                    'holdtime_sec': 15,
                                                    'proposed_local': 15,
                                                    'proposed_peer': 15,
                                                    'source_ip_addr': '10.166.0.138',
                                                    'transport_ip_addr': '10.94.26.121'
                                                }
                                            },
                                            'quick_start': 'enabled',
                                            'recv': True,
                                            'source_ip_addr': '10.166.0.137',
                                            'transport_ip_addr': '10.94.31.247',
                                            'xmit': True
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        {
            'cmd': 'show mpls ldp afi-all discovery',
            'param': {
                'all': True,
                'detail': True,
                'vrf': None,
                'ldp': None
            },
            'output': {
                'execute.return_value': '''
                            RP/0/RSP0/CPU0:TSTR2#show mpls ldp afi-all discovery
                            Mon Dec 21 17:57:47.138 UTC

                            Local LDP Identifier: 10.94.31.247:0
                            Discovery Sources:
                            Interfaces:
                                Bundle-Ether100 : xmit/recv
                                VRF: 'default' (0x60000000)
                                LDP Id: 10.94.31.251:0, Transport address: 10.94.31.251
                                    Hold time: 15 sec (local:15 sec, peer:15 sec)
                                    Established: Dec  1 11:55:00.837 (2w6d ago)

                                Bundle-Ether20 : xmit/recv
                                VRF: 'default' (0x60000000)
                                LDP Id: 10.94.26.126:0, Transport address: 10.94.26.126
                                    Hold time: 15 sec (local:15 sec, peer:15 sec)
                                    Established: Dec 14 12:33:14.549 (1w0d ago)

                                Bundle-Ether3 : xmit/recv
                                VRF: 'default' (0x60000000)
                                LDP Id: 10.94.26.119:0, Transport address: 10.94.26.119
                                    Hold time: 15 sec (local:15 sec, peer:15 sec)
                                    Established: Dec  1 11:55:00.863 (2w6d ago)

                                GigabitEthernet0/0/1/0 : xmit/recv
                                VRF: 'default' (0x60000000)
                                LDP Id: 10.94.31.252:0, Transport address: 10.94.31.252
                                    Hold time: 15 sec (local:15 sec, peer:15 sec)
                                    Established: Dec  1 11:54:50.567 (2w6d ago)

                                GigabitEthernet0/0/1/1 : xmit/recv
                                VRF: 'default' (0x60000000)
                                LDP Id: 10.94.26.126:0, Transport address: 10.94.26.126
                                    Hold time: 15 sec (local:15 sec, peer:15 sec)
                                    Established: Dec 14 12:33:12.454 (1w0d ago)

                                GigabitEthernet0/0/1/18 : xmit/recv
                                VRF: 'default' (0x60000000)
                                LDP Id: 10.94.31.253:0, Transport address: 10.94.31.253
                                    Hold time: 15 sec (local:15 sec, peer:15 sec)
                                    Established: Dec  1 11:54:49.304 (2w6d ago)

                                GigabitEthernet0/0/1/2 : xmit/recv
                                VRF: 'default' (0x60000000)
                                LDP Id: 10.94.26.120:0, Transport address: 10.94.26.120
                                    Hold time: 15 sec (local:15 sec, peer:15 sec)
                                    Established: Dec  1 11:54:49.538 (2w6d ago)

                                GigabitEthernet0/0/1/4 : xmit/recv
                                VRF: 'default' (0x60000000)
                                LDP Id: 10.94.31.245:0, Transport address: 10.94.31.245
                                    Hold time: 15 sec (local:15 sec, peer:15 sec)
                                    Established: Dec  1 11:54:54.341 (2w6d ago)

                                TenGigE0/0/0/4.2096 : xmit
                                VRF: 'default' (0x60000000)


                                TenGigE0/0/0/4.2098 : xmit/recv
                                VRF: 'default' (0x60000000)
                                LDP Id: 10.94.26.29:0, Transport address: 10.94.26.29
                                    Hold time: 15 sec (local:15 sec, peer:15 sec)
                                    Established: Dec 18 14:40:03.639 (3d03h ago)

                                TenGigE0/0/0/5.2095 : xmit
                                VRF: 'default' (0x60000000)


                                TenGigE0/0/0/5.2097 : xmit/recv
                                VRF: 'default' (0x60000000)
                                LDP Id: 10.94.26.121:0, Transport address: 10.94.26.121
                                    Hold time: 15 sec (local:15 sec, peer:15 sec)
                                    Established: Dec 18 16:49:16.538 (3d01h ago)
                                '''
            },
            'parsed': {
                'vrf': {
                    'default': {
                        'local_ldp_identifier': {
                            '10.94.31.247:0': {
                                'discovery_sources': {
                                    'interfaces': {
                                        'Bundle-Ether100': {
                                            'ldp_id': {
                                                '10.94.31.251:0': {
                                                    'established_date': 'Dec  1 11:55:00.837',
                                                    'established_elapsed': '2w6d',
                                                    'holdtime_sec': 15,
                                                    'proposed_local': 15,
                                                    'proposed_peer': 15
                                                }
                                            },
                                            'recv': True,
                                            'transport_ip_addr': '10.94.31.251',
                                            'xmit': True
                                        },
                                        'Bundle-Ether20': {
                                            'ldp_id': {
                                                '10.94.26.126:0': {
                                                    'established_date': 'Dec 14 12:33:14.549',
                                                    'established_elapsed': '1w0d',
                                                    'holdtime_sec': 15,
                                                    'proposed_local': 15,
                                                    'proposed_peer': 15
                                                }
                                            },
                                            'recv': True,
                                            'transport_ip_addr': '10.94.26.126',
                                            'xmit': True
                                        },
                                        'Bundle-Ether3': {
                                            'ldp_id': {
                                                '10.94.26.119:0': {
                                                    'established_date': 'Dec  1 11:55:00.863',
                                                    'established_elapsed': '2w6d',
                                                    'holdtime_sec': 15,
                                                    'proposed_local': 15,
                                                    'proposed_peer': 15
                                                }
                                            },
                                            'recv': True,
                                            'transport_ip_addr': '10.94.26.119',
                                            'xmit': True
                                        },
                                        'GigabitEthernet0/0/1/0': {
                                            'ldp_id': {
                                                '10.94.31.252:0': {
                                                    'established_date': 'Dec  1 11:54:50.567',
                                                    'established_elapsed': '2w6d',
                                                    'holdtime_sec': 15,
                                                    'proposed_local': 15,
                                                    'proposed_peer': 15
                                                }
                                            },
                                            'recv': True,
                                            'transport_ip_addr': '10.94.31.252',
                                            'xmit': True
                                        },
                                        'GigabitEthernet0/0/1/1': {
                                            'ldp_id': {
                                                '10.94.26.126:0': {
                                                    'established_date': 'Dec 14 12:33:12.454',
                                                    'established_elapsed': '1w0d',
                                                    'holdtime_sec': 15,
                                                    'proposed_local': 15,
                                                    'proposed_peer': 15
                                                }
                                            },
                                            'recv': True,
                                            'transport_ip_addr': '10.94.26.126',
                                            'xmit': True
                                        },
                                        'GigabitEthernet0/0/1/18': {
                                            'ldp_id': {
                                                '10.94.31.253:0': {
                                                    'established_date': 'Dec  1 11:54:49.304',
                                                    'established_elapsed': '2w6d',
                                                    'holdtime_sec': 15,
                                                    'proposed_local': 15,
                                                    'proposed_peer': 15
                                                }
                                            },
                                            'recv': True,
                                            'transport_ip_addr': '10.94.31.253',
                                            'xmit': True
                                        },
                                        'GigabitEthernet0/0/1/2': {
                                            'ldp_id': {
                                                '10.94.26.120:0': {
                                                    'established_date': 'Dec  1 11:54:49.538',
                                                    'established_elapsed': '2w6d',
                                                    'holdtime_sec': 15,
                                                    'proposed_local': 15,
                                                    'proposed_peer': 15
                                                }
                                            },
                                            'recv': True,
                                            'transport_ip_addr': '10.94.26.120',
                                            'xmit': True
                                        },
                                        'GigabitEthernet0/0/1/4': {
                                            'ldp_id': {
                                                '10.94.31.245:0': {
                                                    'established_date': 'Dec  1 11:54:54.341',
                                                    'established_elapsed': '2w6d',
                                                    'holdtime_sec': 15,
                                                    'proposed_local': 15,
                                                    'proposed_peer': 15
                                                }
                                            },
                                            'recv': True,
                                            'transport_ip_addr': '10.94.31.245',
                                            'xmit': True
                                        },
                                        'TenGigE0/0/0/4.2096': {
                                            'recv': False,
                                            'xmit': True
                                        },
                                        'TenGigE0/0/0/4.2098': {
                                            'ldp_id': {
                                                '10.94.26.29:0': {
                                                    'established_date': 'Dec 18 14:40:03.639',
                                                    'established_elapsed': '3d03h',
                                                    'holdtime_sec': 15,
                                                    'proposed_local': 15,
                                                    'proposed_peer': 15
                                                }
                                            },
                                            'recv': True,
                                            'transport_ip_addr': '10.94.26.29',
                                            'xmit': True
                                        },
                                        'TenGigE0/0/0/5.2095': {
                                            'recv': False,
                                            'xmit': True
                                        },
                                        'TenGigE0/0/0/5.2097': {
                                            'ldp_id': {
                                                '10.94.26.121:0': {
                                                    'established_date': 'Dec 18 16:49:16.538',
                                                    'established_elapsed': '3d01h',
                                                    'holdtime_sec': 15,
                                                    'proposed_local': 15,
                                                    'proposed_peer': 15
                                                }
                                            },
                                            'recv': True,
                                            'transport_ip_addr': '10.94.26.121',
                                            'xmit': True
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        {
            'cmd': 'show mpls ldp vrf default discovery detail',
            'param': {
                'all': None,
                'detail': True,
                'vrf': None,
                'ldp': None
            },
            'output': {
                'execute.return_value': '''
                                RP/0/RSP0/CPU0:TSTR2# show mpls ldp vrf default discovery detail
                                Mon Dec 21 18:00:45.636 UTC

                                Local LDP Identifier: 10.94.31.247:0
                                Discovery Sources:
                                Interfaces:
                                    Bundle-Ether100 (0x80002e0) : xmit/recv
                                    VRF: 'default' (0x60000000)
                                    Source address: 10.166.0.57; Transport address: 10.94.31.247
                                    Hello interval: 5 sec (due in 4 sec)
                                    Quick-start: Enabled
                                    LDP Id: 10.94.31.251:0
                                        Source address: 10.166.0.58; Transport address: 10.94.31.251
                                        Hold time: 15 sec (local:15 sec, peer:15 sec)
                                                    (expiring in 13.4 sec)
                                        Established: Dec  1 11:55:00.837 (2w6d ago)

                                    Bundle-Ether20 (0x80002a0) : xmit/recv
                                    VRF: 'default' (0x60000000)
                                    Source address: 10.166.0.25; Transport address: 10.94.31.247
                                    Hello interval: 5 sec (due in 1.2 sec)
                                    Quick-start: Enabled
                                    LDP Id: 10.94.26.126:0
                                        Source address: 10.166.0.26; Transport address: 10.94.26.126
                                        Hold time: 15 sec (local:15 sec, peer:15 sec)
                                                    (expiring in 12 sec)
                                        Established: Dec 14 12:33:14.549 (1w0d ago)

                                    Bundle-Ether3 (0x8000260) : xmit/recv
                                    VRF: 'default' (0x60000000)
                                    Source address: 10.166.0.54; Transport address: 10.94.31.247
                                    Hello interval: 5 sec (due in 133 msec)
                                    Quick-start: Enabled
                                    LDP Id: 10.94.26.119:0
                                        Source address: 10.166.0.53; Transport address: 10.94.26.119
                                        Hold time: 15 sec (local:15 sec, peer:15 sec)
                                                    (expiring in 13.4 sec)
                                        Established: Dec  1 11:55:00.863 (2w6d ago)

                                    GigabitEthernet0/0/1/0 (0xc0) : xmit/recv
                                    VRF: 'default' (0x60000000)
                                    Source address: 10.166.0.65; Transport address: 10.94.31.247
                                    Hello interval: 5 sec (due in 4.4 sec)
                                    Quick-start: Enabled
                                    LDP Id: 10.94.31.252:0
                                        Source address: 10.166.0.66; Transport address: 10.94.31.252
                                        Hold time: 15 sec (local:15 sec, peer:15 sec)
                                                    (expiring in 11.8 sec)
                                        Established: Dec  1 11:54:50.567 (2w6d ago)

                                    GigabitEthernet0/0/1/1 (0x100) : xmit/recv
                                    VRF: 'default' (0x60000000)
                                    Source address: 10.166.0.45; Transport address: 10.94.31.247
                                    Hello interval: 5 sec (due in 3.3 sec)
                                    Quick-start: Enabled
                                    LDP Id: 10.94.26.126:0
                                        Source address: 10.166.0.46; Transport address: 10.94.26.126
                                        Hold time: 15 sec (local:15 sec, peer:15 sec)
                                                    (expiring in 10.5 sec)
                                        Established: Dec 14 12:33:12.454 (1w0d ago)

                                    GigabitEthernet0/0/1/18 (0x540) : xmit/recv
                                    VRF: 'default' (0x60000000)
                                    Source address: 10.166.0.109; Transport address: 10.94.31.247
                                    Hello interval: 5 sec (due in 1 sec)
                                    Quick-start: Enabled
                                    LDP Id: 10.94.31.253:0
                                        Source address: 10.166.0.110; Transport address: 10.94.31.253
                                        Hold time: 15 sec (local:15 sec, peer:15 sec)
                                                    (expiring in 13.7 sec)
                                        Established: Dec  1 11:54:49.304 (2w6d ago)

                                    GigabitEthernet0/0/1/2 (0x140) : xmit/recv
                                    VRF: 'default' (0x60000000)
                                    Source address: 10.166.0.29; Transport address: 10.94.31.247
                                    Hello interval: 5 sec (due in 4.5 sec)
                                    Quick-start: Enabled
                                    LDP Id: 10.94.26.120:0
                                        Source address: 10.166.0.30; Transport address: 10.94.26.120
                                        Hold time: 15 sec (local:15 sec, peer:15 sec)
                                                    (expiring in 12.8 sec)
                                        Established: Dec  1 11:54:49.538 (2w6d ago)

                                    GigabitEthernet0/0/1/4 (0x1c0) : xmit/recv
                                    VRF: 'default' (0x60000000)
                                    Source address: 10.166.0.69; Transport address: 10.94.31.247
                                    Hello interval: 5 sec (due in 866 msec)
                                    Quick-start: Enabled
                                    LDP Id: 10.94.31.245:0
                                        Source address: 10.166.0.70; Transport address: 10.94.31.245
                                        Hold time: 15 sec (local:15 sec, peer:15 sec)
                                                    (expiring in 13.1 sec)
                                        Established: Dec  1 11:54:54.341 (2w6d ago)

                                    TenGigE0/0/0/4.2096 (0x14c0) : xmit
                                    VRF: 'default' (0x60000000)

                                    Source address: 10.166.0.125; Transport address: 10.94.31.247
                                    Hello interval: 5 sec (due in 155 msec)
                                    Quick-start: Enabled

                                    TenGigE0/0/0/4.2098 (0x1500) : xmit/recv
                                    VRF: 'default' (0x60000000)
                                    Source address: 10.166.0.133; Transport address: 10.94.31.247
                                    Hello interval: 5 sec (due in 1.3 sec)
                                    Quick-start: Enabled
                                    LDP Id: 10.94.26.29:0
                                        Source address: 10.166.0.134; Transport address: 10.94.26.29
                                        Hold time: 15 sec (local:15 sec, peer:15 sec)
                                                    (expiring in 12.5 sec)
                                        Established: Dec 18 14:40:03.639 (3d03h ago)

                                    TenGigE0/0/0/5.2095 (0x1540) : xmit
                                    VRF: 'default' (0x60000000)

                                    Source address: 10.166.0.149; Transport address: 10.94.31.247
                                    Hello interval: 5 sec (due in 3.4 sec)
                                    Quick-start: Enabled

                                    TenGigE0/0/0/5.2097 (0x1580) : xmit/recv
                                    VRF: 'default' (0x60000000)
                                    Source address: 10.166.0.137; Transport address: 10.94.31.247
                                    Hello interval: 5 sec (due in 2.3 sec)
                                    Quick-start: Enabled
                                    LDP Id: 10.94.26.121:0
                                        Source address: 10.166.0.138; Transport address: 10.94.26.121
                                        Hold time: 15 sec (local:15 sec, peer:15 sec)
                                                    (expiring in 14.5 sec)
                                        Established: Dec 18 16:49:16.538 (3d01h ago)
                                '''
            },
            'parsed': {
                'vrf': {
                    'default': {
                        'local_ldp_identifier': {
                            '10.94.31.247:0': {
                                'discovery_sources': {
                                    'interfaces': {
                                        'Bundle-Ether100': {
                                            'hello_due_time_ms': 4000,
                                            'hello_interval_ms': 5000,
                                            'ldp_id': {
                                                '10.94.31.251:0': {
                                                    'established_date': 'Dec  1 11:55:00.837',
                                                    'established_elapsed': '2w6d',
                                                    'expiring_in': 13.4,
                                                    'holdtime_sec': 15,
                                                    'proposed_local': 15,
                                                    'proposed_peer': 15,
                                                    'source_ip_addr': '10.166.0.58',
                                                    'transport_ip_addr': '10.94.31.251'
                                                }
                                            },
                                            'quick_start': 'enabled',
                                            'recv': True,
                                            'source_ip_addr': '10.166.0.57',
                                            'transport_ip_addr': '10.94.31.247',
                                            'xmit': True
                                        },
                                        'Bundle-Ether20': {
                                            'hello_due_time_ms': 1200,
                                            'hello_interval_ms': 5000,
                                            'ldp_id': {
                                                '10.94.26.126:0': {
                                                    'established_date': 'Dec 14 12:33:14.549',
                                                    'established_elapsed': '1w0d',
                                                    'expiring_in': 12.0,
                                                    'holdtime_sec': 15,
                                                    'proposed_local': 15,
                                                    'proposed_peer': 15,
                                                    'source_ip_addr': '10.166.0.26',
                                                    'transport_ip_addr': '10.94.26.126'
                                                }
                                            },
                                            'quick_start': 'enabled',
                                            'recv': True,
                                            'source_ip_addr': '10.166.0.25',
                                            'transport_ip_addr': '10.94.31.247',
                                            'xmit': True
                                        },
                                        'Bundle-Ether3': {
                                            'hello_due_time_ms': 133,
                                            'hello_interval_ms': 5000,
                                            'ldp_id': {
                                                '10.94.26.119:0': {
                                                    'established_date': 'Dec  1 11:55:00.863',
                                                    'established_elapsed': '2w6d',
                                                    'expiring_in': 13.4,
                                                    'holdtime_sec': 15,
                                                    'proposed_local': 15,
                                                    'proposed_peer': 15,
                                                    'source_ip_addr': '10.166.0.53',
                                                    'transport_ip_addr': '10.94.26.119'
                                                }
                                            },
                                            'quick_start': 'enabled',
                                            'recv': True,
                                            'source_ip_addr': '10.166.0.54',
                                            'transport_ip_addr': '10.94.31.247',
                                            'xmit': True
                                        },
                                        'GigabitEthernet0/0/1/0': {
                                            'hello_due_time_ms': 4400,
                                            'hello_interval_ms': 5000,
                                            'ldp_id': {
                                                '10.94.31.252:0': {
                                                    'established_date': 'Dec  1 11:54:50.567',
                                                    'established_elapsed': '2w6d',
                                                    'expiring_in': 11.8,
                                                    'holdtime_sec': 15,
                                                    'proposed_local': 15,
                                                    'proposed_peer': 15,
                                                    'source_ip_addr': '10.166.0.66',
                                                    'transport_ip_addr': '10.94.31.252'
                                                }
                                            },
                                            'quick_start': 'enabled',
                                            'recv': True,
                                            'source_ip_addr': '10.166.0.65',
                                            'transport_ip_addr': '10.94.31.247',
                                            'xmit': True
                                        },
                                        'GigabitEthernet0/0/1/1': {
                                            'hello_due_time_ms': 3300,
                                            'hello_interval_ms': 5000,
                                            'ldp_id': {
                                                '10.94.26.126:0': {
                                                    'established_date': 'Dec 14 12:33:12.454',
                                                    'established_elapsed': '1w0d',
                                                    'expiring_in': 10.5,
                                                    'holdtime_sec': 15,
                                                    'proposed_local': 15,
                                                    'proposed_peer': 15,
                                                    'source_ip_addr': '10.166.0.46',
                                                    'transport_ip_addr': '10.94.26.126'
                                                }
                                            },
                                            'quick_start': 'enabled',
                                            'recv': True,
                                            'source_ip_addr': '10.166.0.45',
                                            'transport_ip_addr': '10.94.31.247',
                                            'xmit': True
                                        },
                                        'GigabitEthernet0/0/1/18': {
                                            'hello_due_time_ms': 1000,
                                            'hello_interval_ms': 5000,
                                            'ldp_id': {
                                                '10.94.31.253:0': {
                                                    'established_date': 'Dec  1 11:54:49.304',
                                                    'established_elapsed': '2w6d',
                                                    'expiring_in': 13.7,
                                                    'holdtime_sec': 15,
                                                    'proposed_local': 15,
                                                    'proposed_peer': 15,
                                                    'source_ip_addr': '10.166.0.110',
                                                    'transport_ip_addr': '10.94.31.253'
                                                }
                                            },
                                            'quick_start': 'enabled',
                                            'recv': True,
                                            'source_ip_addr': '10.166.0.109',
                                            'transport_ip_addr': '10.94.31.247',
                                            'xmit': True
                                        },
                                        'GigabitEthernet0/0/1/2': {
                                            'hello_due_time_ms': 4500,
                                            'hello_interval_ms': 5000,
                                            'ldp_id': {
                                                '10.94.26.120:0': {
                                                    'established_date': 'Dec  1 11:54:49.538',
                                                    'established_elapsed': '2w6d',
                                                    'expiring_in': 12.8,
                                                    'holdtime_sec': 15,
                                                    'proposed_local': 15,
                                                    'proposed_peer': 15,
                                                    'source_ip_addr': '10.166.0.30',
                                                    'transport_ip_addr': '10.94.26.120'
                                                }
                                            },
                                            'quick_start': 'enabled',
                                            'recv': True,
                                            'source_ip_addr': '10.166.0.29',
                                            'transport_ip_addr': '10.94.31.247',
                                            'xmit': True
                                        },
                                        'GigabitEthernet0/0/1/4': {
                                            'hello_due_time_ms': 866,
                                            'hello_interval_ms': 5000,
                                            'ldp_id': {
                                                '10.94.31.245:0': {
                                                    'established_date': 'Dec  1 11:54:54.341',
                                                    'established_elapsed': '2w6d',
                                                    'expiring_in': 13.1,
                                                    'holdtime_sec': 15,
                                                    'proposed_local': 15,
                                                    'proposed_peer': 15,
                                                    'source_ip_addr': '10.166.0.70',
                                                    'transport_ip_addr': '10.94.31.245'
                                                }
                                            },
                                            'quick_start': 'enabled',
                                            'recv': True,
                                            'source_ip_addr': '10.166.0.69',
                                            'transport_ip_addr': '10.94.31.247',
                                            'xmit': True
                                        },
                                        'TenGigE0/0/0/4.2096': {
                                            'hello_due_time_ms': 155,
                                            'hello_interval_ms': 5000,
                                            'quick_start': 'enabled',
                                            'recv': False,
                                            'source_ip_addr': '10.166.0.125',
                                            'transport_ip_addr': '10.94.31.247',
                                            'xmit': True
                                        },
                                        'TenGigE0/0/0/4.2098': {
                                            'hello_due_time_ms': 1300,
                                            'hello_interval_ms': 5000,
                                            'ldp_id': {
                                                '10.94.26.29:0': {
                                                    'established_date': 'Dec 18 14:40:03.639',
                                                    'established_elapsed': '3d03h',
                                                    'expiring_in': 12.5,
                                                    'holdtime_sec': 15,
                                                    'proposed_local': 15,
                                                    'proposed_peer': 15,
                                                    'source_ip_addr': '10.166.0.134',
                                                    'transport_ip_addr': '10.94.26.29'
                                                }
                                            },
                                            'quick_start': 'enabled',
                                            'recv': True,
                                            'source_ip_addr': '10.166.0.133',
                                            'transport_ip_addr': '10.94.31.247',
                                            'xmit': True
                                        },
                                        'TenGigE0/0/0/5.2095': {
                                            'hello_due_time_ms': 3400,
                                            'hello_interval_ms': 5000,
                                            'quick_start': 'enabled',
                                            'recv': False,
                                            'source_ip_addr': '10.166.0.149',
                                            'transport_ip_addr': '10.94.31.247',
                                            'xmit': True
                                        },
                                        'TenGigE0/0/0/5.2097': {
                                            'hello_due_time_ms': 2300,
                                            'hello_interval_ms': 5000,
                                            'ldp_id': {
                                                '10.94.26.121:0': {
                                                    'established_date': 'Dec 18 16:49:16.538',
                                                    'established_elapsed': '3d01h',
                                                    'expiring_in': 14.5,
                                                    'holdtime_sec': 15,
                                                    'proposed_local': 15,
                                                    'proposed_peer': 15,
                                                    'source_ip_addr': '10.166.0.138',
                                                    'transport_ip_addr': '10.94.26.121'
                                                }
                                            },
                                            'quick_start': 'enabled',
                                            'recv': True,
                                            'source_ip_addr': '10.166.0.137',
                                            'transport_ip_addr': '10.94.31.247',
                                            'xmit': True
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
    ]
 
    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowMplsLdpDiscovery(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        for test in self.golden_output:
            self.maxDiff = None
            self.device = Mock(**test['output'])
            obj = ShowMplsLdpDiscovery(device=self.device)
            parsed_output = obj.parse(all=test['param']['all'],
                                      detail=test['param']['detail'],
                                      vrf=test['param']['vrf'],
                                      ldp=test['param']['ldp'],
                                    )
            self.assertEqual(parsed_output, test['parsed'])


if __name__ == '__main__':
    unittest.main()
