# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device
from pyats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

# iosxr show_mrib
from genie.libs.parser.iosxr.show_l2vpn import (ShowL2vpnMacLearning,
                                                ShowL2vpnBridgeDomain,
                                                ShowL2vpnForwardingBridgeDomainMacAddress,
                                                ShowL2vpnForwardingProtectionMainInterface,
                                                ShowL2vpnBridgeDomainSummary,
                                                ShowL2vpnBridgeDomainBrief,
                                                ShowL2vpnBridgeDomainDetail)


# ===========================================
# Unit test for 'show l2vpn mac-learning {mac_type} all location {location}'
# ===========================================
class TestShowL2vpnMacLearning(unittest.TestCase):
    """Unit test for 'show l2vpn mac-learning <mac_type> all location <location>'"""

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    expected_output = {
        'topo_id': {
            '1': {
                'producer': {
                    '0/0/CPU0': {
                        'next_hop': {
                            'BE1.7': {
                                'mac_address': {
                                    '7777.77ff.7779': {
                                        'ip_address': []}}}}}}},
            '6': {
                'producer': {
                    '0/0/CPU0': {
                        'next_hop': {
                            'BV1': {
                                'mac_address': {
                                    '0000.f6ff.8fd6': {
                                        'ip_address': ['fe80::200:f6ff:feff:8fd6']},
                                    '1000.00ff.0102': {
                                        'ip_address': ['10.1.1.11']}}}}}}},
            '7': {
                'producer': {
                    '0/0/CPU0': {
                        'next_hop': {
                            'BV2': {
                                'mac_address': {
                                    '0000.f6ff.8fca': {
                                        'ip_address': [
                                            '10.1.2.91', '10.1.2.93']}}}}}}}}}

    device_output = {'execute.return_value': '''
        Topo ID  Producer  Next Hop(s)  Mac Address     IP Address

        6        0/0/CPU0   BV1        1000.00ff.0102      10.1.1.11
        7        0/0/CPU0   BV2        0000.f6ff.8fca      10.1.2.91
        7        0/0/CPU0   BV2        0000.f6ff.8fca      10.1.2.93
        1        0/0/CPU0   BE1.7      7777.77ff.7779
        6        0/0/CPU0   BV1        0000.f6ff.8fd6      fe80::200:f6ff:feff:8fd6

    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowL2vpnMacLearning(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output)
        obj = ShowL2vpnMacLearning(device=self.device)
        parsed_output = obj.parse()

        self.assertEqual(parsed_output, self.expected_output)


# ===========================================
#  Unit test for 'show l2vpn bridge-domain'
# ===========================================

class TestShowL2vpnBridgeDomain(unittest.TestCase):
    '''Unit test for "show l2vpn bridge-domain"'''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'bridge_group': {
            'g1': {
                'bridge_domain': {
                    'EVPN-Multicast-Genie': {
                        'id': 0,
                        'state': 'up',
                        'shg_id': 0,
                        'mst_i': 0,
                        'mac_aging_time': 300,
                        'mac_limit': 4000,
                        'mac_limit_action': 'none',
                        'mac_limit_notification': 'syslog',
                        'filter_mac_address': 0,
                        'ac': {
                            'num_ac': 1,
                            'num_ac_up': 1,
                            'interfaces': {
                                'GigabitEthernet0/1/0/0': {
                                    'state': 'up',
                                    'static_mac_address': 2,
                                    'mst_i': 0,
                                    'mst_i_state': 'unprotected',
                                },
                            },
                        },
                        'vfi': {
                            'num_vfi': 1,
                            '1': {
                                'neighbor': {
                                    '10.1.1.1': {
                                        'pw_id': {
                                            1: {
                                                'state': 'up',
                                                'static_mac_address': 0,
                                            },
                                        },
                                    },
                                },
                            },
                        },
                        'pw': {
                            'num_pw': 1,
                            'num_pw_up': 1,
                        },
                    },
                },
            },
        },
    }

    golden_output1 = {'execute.return_value': '''
        RP/0/RP0/CPU0:router# show l2vpn bridge-domain

        Bridge group: g1, bridge-domain: EVPN-Multicast-Genie, id: 0, state: up, ShgId: 0, MSTi: 0
          Aging: 300 s, MAC limit: 4000, Action: none, Notification: syslog
          Filter MAC addresses: 0
          ACs: 1 (1 up), VFIs: 1, PWs: 1 (1 up)
          List of ACs:
            Gi0/1/0/0, state: up, Static MAC addresses: 2, MSTi: 0 (unprotected)
          List of Access PWs:
          List of VFIs:
            VFI 1
              Neighbor 10.1.1.1 pw-id 1, state: up, Static MAC addresses: 0
    '''}

    golden_parsed_output2 = {
        'bridge_group': {
            'EVPN-Mulicast': {
                'bridge_domain': {
                    'EVPN-Multicast-Genie': {
                        'id': 0,
                        'state': 'up',
                        'shg_id': 0,
                        'mst_i': 0,
                        'mac_aging_time': 300,
                        'mac_limit': 4000,
                        'mac_limit_action': 'none',
                        'mac_limit_notification': 'syslog',
                        'filter_mac_address': 0,
                        'ac': {
                            'num_ac': 3,
                            'num_ac_up': 2,
                            'interfaces': {
                                'BV100': {
                                    'state': 'up',
                                    'bvi_mac_address': 1,
                                },
                                'Bundle-Ether3.100': {
                                    'state': 'down',
                                    'static_mac_address': 0,
                                    'mst_i': 5,
                                },
                                'Bundle-Ether4.100': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 5,
                                },
                            },
                        },
                        'vfi': {
                            'num_vfi': 0,
                        },
                        'pw': {
                            'num_pw': 0,
                            'num_pw_up': 0,
                        },
                        'pbb': {
                            'num_pbb': 0,
                            'num_pbb_up': 0,
                        },
                        'vni': {
                            'num_vni': 0,
                            'num_vni_up': 0,
                        },
                        'evpn': {
                            'EVPN': {
                                'state': 'up',
                            },
                        },
                    },
                },
            },
        },
    }

    golden_output2 = {'execute.return_value': '''
        show l2vpn bridge-domain

        Mon Oct  7 16:18:58.402 EDT
        Legend: pp = Partially Programmed.
        Bridge group: EVPN-Mulicast, bridge-domain: EVPN-Multicast-Genie, id: 0, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 4000, Action: none, Notification: syslog
        Filter MAC addresses: 0
        ACs: 3 (2 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            BV100, state: up, BVI MAC addresses: 1
            BE3.100, state: down, Static MAC addresses: 0, MSTi: 5
            BE4.100, state: up, Static MAC addresses: 0, MSTi: 5
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
    '''}

    golden_parsed_output3 = {
        'bridge_group': {
            'SBC-service': {
                'bridge_domain': {
                    'bd100': {
                        'id': 0,
                        'state': 'up',
                        'shg_id': 0,
                        'mst_i': 0,
                        'mac_aging_time': 300,
                        'mac_limit': 4000,
                        'mac_limit_action': 'none',
                        'mac_limit_notification': 'syslog',
                        'filter_mac_address': 0,
                        'ac': {
                            'num_ac': 2,
                            'num_ac_up': 2,
                            'interfaces': {
                                'BV100': {
                                    'state': 'up',
                                    'bvi_mac_address': 2,
                                },
                                'GigabitEthernet0/4/0/1.100': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                },
                            },
                        },
                        'vfi': {
                            'num_vfi': 1,
                            'vfi100': {
                                'state': 'up',
                                'neighbor': {
                                    '10.229.11.11': {
                                        'pw_id': {
                                            100100: {
                                                'state': 'up',
                                                'static_mac_address': 0,
                                            },
                                        },
                                    },
                                },
                            },
                        },
                        'pw': {
                            'num_pw': 1,
                            'num_pw_up': 1,
                        },
                        'pbb': {
                            'num_pbb': 0,
                            'num_pbb_up': 0,
                        },
                        'vni': {
                            'num_vni': 0,
                            'num_vni_up': 0,
                        },
                    },
                },
            },
            'evpn_access': {
                'bridge_domain': {
                    '100_evpn_access': {
                        'id': 1,
                        'state': 'up',
                        'shg_id': 0,
                        'mst_i': 0,
                        'mac_aging_time': 300,
                        'mac_limit': 100,
                        'mac_limit_action': 'limit, no-flood',
                        'mac_limit_notification': 'syslog, trap',
                        'filter_mac_address': 0,
                        'ac': {
                            'num_ac': 1,
                            'num_ac_up': 1,
                            'interfaces': {
                                'GigabitEthernet0/4/0/6.100': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 5,
                                },
                            },
                        },
                        'vfi': {
                            'num_vfi': 0,
                        },
                        'pw': {
                            'num_pw': 0,
                            'num_pw_up': 0,
                        },
                        'pbb': {
                            'num_pbb': 0,
                            'num_pbb_up': 0,
                        },
                        'vni': {
                            'num_vni': 0,
                            'num_vni_up': 0,
                        },
                        'evpn': {
                            'EVPN': {
                                'state': 'up',
                            },
                        },
                    },
                },
            },
        },
    }
    golden_output3 = {'execute.return_value': '''
        show l2vpn bridge-domain

        Mon Oct 21 11:04:45.164 EDT
        Legend: pp = Partially Programmed.
        Bridge group: SBC-service, bridge-domain: bd100, id: 0, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 4000, Action: none, Notification: syslog
        Filter MAC addresses: 0
        ACs: 2 (2 up), VFIs: 1, PWs: 1 (1 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of ACs:
            BV100, state: up, BVI MAC addresses: 2
            Gi0/4/0/1.100, state: up, Static MAC addresses: 0
        List of Access PWs:
        List of VFIs:
            VFI vfi100 (up)
            Neighbor 10.229.11.11 pw-id 100100, state: up, Static MAC addresses: 0
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 100_evpn_access, id: 1, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.100, state: up, Static MAC addresses: 0, MSTi: 5
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:

    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowL2vpnBridgeDomain(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowL2vpnBridgeDomain(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowL2vpnBridgeDomain(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_golden3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        obj = ShowL2vpnBridgeDomain(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output3)


# ====================================================================================
#  Unit test for 'show l2vpn forwarding bridge-domain mac-address location {location}'
# ====================================================================================
class TestShowL2vpnForwardingBridgeDomain(unittest.TestCase):
    '''Unit test for
        show l2vpn forwarding bridge-domain mac-address location {location}
        show l2vpn forwarding bridge-domain {bridge_domain} mac-address location {location}
    '''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'mac_table': {
            'Te0/0/1/0/3.3': {
                'mac_address': {
                    '0001.00ff.0002': {
                        'lc_learned': 'N/A',
                        'learned_from': 'Te0/0/1/0/3.3',
                        'mapped_to': 'N/A',
                        'resync_age': '0d '
                                      '0h '
                                      '0m '
                                      '14s',
                        'type': 'dynamic'},
                    '0001.00ff.0003': {
                        'lc_learned': 'N/A',
                        'learned_from': 'Te0/0/1/0/3.3',
                        'mapped_to': 'N/A',
                        'resync_age': '0d '
                                      '0h '
                                      '0m '
                                      '14s',
                        'type': 'dynamic'},
                    '0001.00ff.0004': {
                        'lc_learned': 'N/A',
                        'learned_from': 'Te0/0/1/0/3.3',
                        'mapped_to': 'N/A',
                        'resync_age': '0d '
                                      '0h '
                                      '0m '
                                      '14s',
                        'type': 'dynamic'},
                    '0001.00ff.0005': {
                        'lc_learned': 'N/A',
                        'learned_from': 'Te0/0/1/0/3.3',
                        'mapped_to': 'N/A',
                        'resync_age': '0d '
                                      '0h '
                                      '0m '
                                      '14s',
                        'type': 'dynamic'},
                    '0001.00ff.0006': {
                        'lc_learned': 'N/A',
                        'learned_from': 'Te0/0/1/0/3.3',
                        'mapped_to': 'N/A',
                        'resync_age': '0d '
                                      '0h '
                                      '0m '
                                      '14s',
                        'type': 'dynamic'},
                    '0001.00ff.0007': {
                        'lc_learned': 'N/A',
                        'learned_from': 'Te0/0/1/0/3.3',
                        'mapped_to': 'N/A',
                        'resync_age': '0d '
                                      '0h '
                                      '0m '
                                      '14s',
                        'type': 'dynamic'},
                    '0001.00ff.0008': {
                        'lc_learned': 'N/A',
                        'learned_from': 'Te0/0/1/0/3.3',
                        'mapped_to': 'N/A',
                        'resync_age': '0d '
                                      '0h '
                                      '0m '
                                      '14s',
                        'type': 'dynamic'},
                    '0001.00ff.0009': {
                        'lc_learned': 'N/A',
                        'learned_from': 'Te0/0/1/0/3.3',
                        'mapped_to': 'N/A',
                        'resync_age': '0d '
                                      '0h '
                                      '0m '
                                      '14s',
                        'type': 'dynamic'},
                    '0001.00ff.000a': {
                        'lc_learned': 'N/A',
                        'learned_from': 'Te0/0/1/0/3.3',
                        'mapped_to': 'N/A',
                        'resync_age': '0d '
                                      '0h '
                                      '0m '
                                      '14s',
                        'type': 'dynamic'},
                    '0001.00ff.000b': {
                        'lc_learned': 'N/A',
                        'learned_from': 'Te0/0/1/0/3.3',
                        'mapped_to': 'N/A',
                        'resync_age': '0d '
                                      '0h '
                                      '0m '
                                      '14s',
                        'type': 'dynamic'},
                    '0001.00ff.000c': {
                        'lc_learned': 'N/A',
                        'learned_from': 'Te0/0/1/0/3.3',
                        'mapped_to': 'N/A',
                        'resync_age': '0d '
                                      '0h '
                                      '0m '
                                      '14s',
                        'type': 'dynamic'},
                    '0001.00ff.000d': {
                        'lc_learned': 'N/A',
                        'learned_from': 'Te0/0/1/0/3.3',
                        'mapped_to': 'N/A',
                        'resync_age': '0d '
                                      '0h '
                                      '0m '
                                      '14s',
                        'type': 'dynamic'},
                    '0001.00ff.000e': {
                        'lc_learned': 'N/A',
                        'learned_from': 'Te0/0/1/0/3.3',
                        'mapped_to': 'N/A',
                        'resync_age': '0d '
                                      '0h '
                                      '0m '
                                      '14s',
                        'type': 'dynamic'},
                    '0001.00ff.000f': {
                        'lc_learned': 'N/A',
                        'learned_from': 'Te0/0/1/0/3.3',
                        'mapped_to': 'N/A',
                        'resync_age': '0d '
                                      '0h '
                                      '0m '
                                      '14s',
                        'type': 'dynamic'},
                    '0001.00ff.0010': {
                        'lc_learned': 'N/A',
                        'learned_from': 'Te0/0/1/0/3.3',
                        'mapped_to': 'N/A',
                        'resync_age': '0d '
                                      '0h '
                                      '0m '
                                      '14s',
                        'type': 'dynamic'},
                    '0001.00ff.0011': {
                        'lc_learned': 'N/A',
                        'learned_from': 'Te0/0/1/0/3.3',
                        'mapped_to': 'N/A',
                        'resync_age': '0d '
                                      '0h '
                                      '0m '
                                      '14s',
                        'type': 'dynamic'},
                    '0001.00ff.0012': {
                        'lc_learned': 'N/A',
                        'learned_from': 'Te0/0/1/0/3.3',
                        'mapped_to': 'N/A',
                        'resync_age': '0d '
                                      '0h '
                                      '0m '
                                      '14s',
                        'type': 'dynamic'},
                    '0001.00ff.0013': {
                        'lc_learned': 'N/A',
                        'learned_from': 'Te0/0/1/0/3.3',
                        'mapped_to': 'N/A',
                        'resync_age': '0d '
                                      '0h '
                                      '0m '
                                      '14s',
                        'type': 'dynamic'}
                }
            }
        }
    }

    golden_output = {'execute.return_value': '''
        RP/0/RP0/CPU0:ios#show l2vpn forwarding bridge-domain mac-address location 0/$
        Wed Jul 3 14:10:20.666 UTC
        To Resynchronize MAC table from the Network Processors, use the command...
        l2vpn resynchronize forwarding mac-address-table location <r/s/i>

        Mac Address Type Learned from/Filtered on LC learned Resync Age/Last Change Mapped to 
        -------------- ------- --------------------------- ---------- ---------------------- -------------- 
        0001.00ff.0002 dynamic Te0/0/1/0/3.3 N/A 0d 0h 0m 14s N/A 
        0001.00ff.0003 dynamic Te0/0/1/0/3.3 N/A 0d 0h 0m 14s N/A 
        0001.00ff.0004 dynamic Te0/0/1/0/3.3 N/A 0d 0h 0m 14s N/A 
        0001.00ff.0005 dynamic Te0/0/1/0/3.3 N/A 0d 0h 0m 14s N/A 
        0001.00ff.0006 dynamic Te0/0/1/0/3.3 N/A 0d 0h 0m 14s N/A 
        0001.00ff.0007 dynamic Te0/0/1/0/3.3 N/A 0d 0h 0m 14s N/A 
        0001.00ff.0008 dynamic Te0/0/1/0/3.3 N/A 0d 0h 0m 14s N/A 
        0001.00ff.0009 dynamic Te0/0/1/0/3.3 N/A 0d 0h 0m 14s N/A 
        0001.00ff.000a dynamic Te0/0/1/0/3.3 N/A 0d 0h 0m 14s N/A 
        0001.00ff.000b dynamic Te0/0/1/0/3.3 N/A 0d 0h 0m 14s N/A 
        0001.00ff.000c dynamic Te0/0/1/0/3.3 N/A 0d 0h 0m 14s N/A 
        0001.00ff.000d dynamic Te0/0/1/0/3.3 N/A 0d 0h 0m 14s N/A 
        0001.00ff.000e dynamic Te0/0/1/0/3.3 N/A 0d 0h 0m 14s N/A 
        0001.00ff.000f dynamic Te0/0/1/0/3.3 N/A 0d 0h 0m 14s N/A 
        0001.00ff.0010 dynamic Te0/0/1/0/3.3 N/A 0d 0h 0m 14s N/A 
        0001.00ff.0011 dynamic Te0/0/1/0/3.3 N/A 0d 0h 0m 14s N/A 
        0001.00ff.0012 dynamic Te0/0/1/0/3.3 N/A 0d 0h 0m 14s N/A 
        0001.00ff.0013 dynamic Te0/0/1/0/3.3 N/A 0d 0h 0m 14s N/A
    '''}

    golden_parsed_output_1 = {
        'mac_table': {
            '(10.25.40.40, 10007)': {
                'mac_address': {
                    '0021.00ff.0103': {
                        'lc_learned': 'N/A',
                        'learned_from': '(10.25.40.40, '
                                        '10007)',
                        'mapped_to': 'N/A',
                        'resync_age': '14 '
                                      'Mar '
                                      '12:46:04',
                        'type': 'dynamic'},
                    '1234.00ff.0106': {'lc_learned': 'N/A',
                                       'learned_from': '(10.25.40.40, '
                                                       '10007)',
                                       'mapped_to': 'N/A',
                                       'resync_age': 'N/A',
                                       'type': 'static'}
                }
            },
            'BD id:0': {
                'mac_address': {
                    '0021.00ff.0102': {
                        'lc_learned': 'N/A',
                        'learned_from': 'BD '
                                        'id:0',
                        'mapped_to': 'N/A',
                        'resync_age': 'N/A',
                        'type': 'EVPN'},
                    '0021.00ff.0104': {'lc_learned': 'N/A',
                                       'learned_from': 'BD '
                                                       'id:0',
                                       'mapped_to': 'N/A',
                                       'resync_age': 'N/A',
                                       'type': 'EVPN'},
                    '0021.00ff.0105': {'lc_learned': 'N/A',
                                       'learned_from': 'BD '
                                                       'id:0',
                                       'mapped_to': 'N/A',
                                       'resync_age': 'N/A',
                                       'type': 'EVPN'},
                    '0021.00ff.0106': {'lc_learned': 'N/A',
                                       'learned_from': 'BD '
                                                       'id:0',
                                       'mapped_to': 'N/A',
                                       'resync_age': 'N/A',
                                       'type': 'EVPN'},
                    '1234.00ff.0102': {'lc_learned': 'N/A',
                                       'learned_from': 'BD '
                                                       'id:0',
                                       'mapped_to': 'N/A',
                                       'resync_age': 'N/A',
                                       'type': 'EVPN'},
                    '1234.00ff.0103': {'lc_learned': 'N/A',
                                       'learned_from': 'BD '
                                                       'id:0',
                                       'mapped_to': 'N/A',
                                       'resync_age': 'N/A',
                                       'type': 'EVPN'},
                    '1234.00ff.0104': {'lc_learned': 'N/A',
                                       'learned_from': 'BD '
                                                       'id:0',
                                       'mapped_to': 'N/A',
                                       'resync_age': 'N/A',
                                       'type': 'EVPN'},
                    '1234.00ff.0105': {'lc_learned': 'N/A',
                                       'learned_from': 'BD '
                                                       'id:0',
                                       'mapped_to': 'N/A',
                                       'resync_age': 'N/A',
                                       'type': 'EVPN'}
                }
            },
            'BE1.2': {
                'mac_address': {
                    '0021.00ff.0207': {
                        'lc_learned': 'N/A',
                        'learned_from': 'BE1.2',
                        'mapped_to': 'N/A',
                        'resync_age': '14 '
                                      'Mar '
                                      '12:46:04',
                        'type': 'dynamic'},
                    '1234.00ff.0206': {
                        'lc_learned': 'N/A',
                        'learned_from': 'BE1.2',
                        'mapped_to': 'N/A',
                        'resync_age': 'N/A',
                        'type': 'static'}
                }
            }
        }
    }

    golden_output_1 = {'execute.return_value': '''
        RP/0/RP0/CPU0:router# show l2vpn forwarding bridge-domain mac-address location 0
        Mac Address    Type    Learned from/Filtered on    LC learned Resync Age/Last Change Mapped to
        -------------- ------- --------------------------- ---------- ---------------------- --------------
        0021.00ff.0102 EVPN    BD id: 0                    N/A        N/A                    N/A
        0021.00ff.0104 EVPN    BD id: 0                    N/A        N/A                    N/A
        0021.00ff.0105 EVPN    BD id: 0                    N/A        N/A                    N/A
        0021.00ff.0106 EVPN    BD id: 0                    N/A        N/A                    N/A
        1234.00ff.0102 EVPN    BD id: 0                    N/A        N/A                    N/A
        1234.00ff.0103 EVPN    BD id: 0                    N/A        N/A                    N/A
        1234.00ff.0104 EVPN    BD id: 0                    N/A        N/A                    N/A
        1234.00ff.0105 EVPN    BD id: 0                    N/A        N/A                    N/A
        0021.00ff.0103 dynamic (10.25.40.40, 10007)        N/A        14 Mar 12:46:04        N/A
        1234.00ff.0106 static  (10.25.40.40, 10007)        N/A        N/A                    N/A
        0021.00ff.0207 dynamic BE1.2                       N/A        14 Mar 12:46:04        N/A
        1234.00ff.0206 static  BE1.2                       N/A        N/A                    N/A
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowL2vpnForwardingBridgeDomainMacAddress(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(location=0)

    def test_missing_attribute(self):
        self.device = Mock(**self.empty_output)
        obj = ShowL2vpnForwardingBridgeDomainMacAddress(device=self.device)
        with self.assertRaises(TypeError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowL2vpnForwardingBridgeDomainMacAddress(device=self.device)
        parsed_output = obj.parse(location=0)
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowL2vpnForwardingBridgeDomainMacAddress(device=self.device)
        parsed_output = obj.parse(location=0, bridge_domain=0)
        self.assertEqual(parsed_output, self.golden_parsed_output_1)


# ====================================================================================
#  Unit test for 'show l2vpn forwarding protection main-interface location {location}'
# ====================================================================================
class TestShowL2vpnForwardingProtectionMainInterface(unittest.TestCase):
    '''Unit test for
        show l2vpn forwarding protection main-interface location {location}
    '''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'main_interface_id': {
            'GigabitEthernet0/0/0/0': {
                'instance': {
                    '1': {
                        'state': 'forward'},
                    '2': {
                        'state': 'forward'}
                }
            },
            'GigabitEthernet0/0/0/1': {
                'instance': {
                    '1': {
                        'state': 'forward'}
                }
            }
        }
    }

    golden_output = {'execute.return_value': '''
        RP/0/RP0/CPU0:router# show l2vpn forwarding protection main-interface location 0/1/0
        Main Interface ID                Instance    State    
        -------------------------------- -------------- -------- 
        GigabitEthernet0/0/0/0           1               forward       
        GigabitEthernet0/0/0/0           2               forward                
        GigabitEthernet0/0/0/1           1               forward  
    '''}

    golden_parsed_output_1 = {
        'main_interface_id': {
            'PW:10.25.40.40,10001': {
                'instance': {
                    '0': {
                        'state': 'FORWARDING'},
                    '1': {
                        'state': 'BLOCKED'}
                }
            },
            'PW:10.25.40.40,10007': {
                'instance': {
                    '0': {
                        'state': 'FORWARDING'},
                    '1': {
                        'state': 'FORWARDING'}
                }
            },
            'PW:10.25.40.40,10011': {
                'instance': {
                    '0': {
                        'state': 'FORWARDING'},
                    '1': {
                        'state': 'FORWARDING'}
                }
            },
            'PW:10.25.40.40,10017': {
                'instance': {
                    '0': {
                        'state': 'FORWARDING'}
                }
            },
            'VFI:ves-vfi-1': {
                'instance': {
                    '0': {
                        'state': 'FORWARDING'},
                    '1': {
                        'state': 'BLOCKED'}
                }
            },
            'VFI:ves-vfi-2': {
                'instance': {
                    '0': {
                        'state': 'FORWARDING'},
                    '1': {
                        'state': 'FORWARDING'}
                }
            },
            'VFI:ves-vfi-3': {
                'instance': {
                    '0': {
                        'state': 'FORWARDING'},
                    '1': {
                        'state': 'BLOCKED'}
                }
            },
            'VFI:ves-vfi-4': {
                'instance': {
                    '0': {
                        'state': 'FORWARDING'},
                    '1': {
                        'state': 'FORWARDING'}
                }
            }
        }
    }

    golden_output_1 = {'execute.return_value': '''
        RP/0/RP0/CPU0:router# show l2vpn forwarding protection main-interface location 0/2/1
        Main Interface ID                Instance   State
        -------------------------------- ---------- ------------
        VFI:ves-vfi-1                    0          FORWARDING
        VFI:ves-vfi-1                    1          BLOCKED
        VFI:ves-vfi-2                    0          FORWARDING
        VFI:ves-vfi-2                    1          FORWARDING
        VFI:ves-vfi-3                    0          FORWARDING
        VFI:ves-vfi-3                    1          BLOCKED
        VFI:ves-vfi-4                    0          FORWARDING
        VFI:ves-vfi-4                    1          FORWARDING
        PW:10.25.40.40,10001             0          FORWARDING
        PW:10.25.40.40,10001             1          BLOCKED
        PW:10.25.40.40,10007             0          FORWARDING
        PW:10.25.40.40,10007             1          FORWARDING
        PW:10.25.40.40,10011             0          FORWARDING
        PW:10.25.40.40,10011             1          FORWARDING
        PW:10.25.40.40,10017             0          FORWARDING
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowL2vpnForwardingProtectionMainInterface(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(location='0/1/0')

    def test_missing_argument(self):
        self.device = Mock(**self.empty_output)
        obj = ShowL2vpnForwardingProtectionMainInterface(device=self.device)
        with self.assertRaises(TypeError):
            parsed_output = obj.parse()


# ==================================================
#  Unit test for 'show l2vpn bridge-domain summary'
# ==================================================

class TestShowL2vpnBridgeDomainSummary(unittest.TestCase):
    '''Unit test for "show l2vpn bridge-domain summary"'''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'number_of_groups': 1,
        'bridge_domains': {
            'total': 1,
            'up': 1,
            'shutdown': 0,
        },
        'ac': {
            'total': 1,
            'up': 1,
            'down': 0,
        },
        'pw': {
            'total': 1,
            'up': 1,
            'down': 0,
        },
    }

    golden_output1 = {'execute.return_value': '''
        Device1# show l2vpn bridge-domain summary

        Number of groups: 1, bridge-domains: 1, Up: 1, Shutdown: 0
        Number of ACs: 1 Up: 1, Down: 0
        Number of PWs: 1 Up: 1, Down: 0
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowL2vpnBridgeDomainSummary(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowL2vpnBridgeDomainSummary(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)


# ==================================================
#  Unit test for 'show l2vpn bridge-domain summary'
# ==================================================

class TestShowL2vpnBridgeDomainBrief(unittest.TestCase):
    '''Unit test for "show l2vpn bridge-domain summary"'''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'bridge_group': {
            'g1': {
                'bridge_domain': {
                    'bd1': {
                        'id': 0,
                        'state': 'up',
                        'ac': {
                            'num_ac': 1,
                            'num_ac_up': 1,
                        },
                        'pw': {
                            'num_pw': 1,
                            'num_pw_up': 1,
                        },
                    },
                },
            },
        },
    }

    golden_output1 = {'execute.return_value': '''
        Device1# show l2vpn bridge-domain brief

        Bridge Group/Bridge-Domain Name  ID    State      Num ACs/up     Num PWs/up
        -------------------------------- ----- ---------- -------------- --------------
        g1/bd1                           0     up         1/1            1/1 
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowL2vpnBridgeDomainBrief(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowL2vpnBridgeDomainBrief(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)


# ==================================================
#  Unit test for 'show l2vpn bridge-domain summary'
# ==================================================

class TestShowL2vpnBridgeDomainSummary(unittest.TestCase):
    '''Unit test for "show l2vpn bridge-domain summary"'''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'number_of_groups': 1,
        'bridge_domains': {
            'total': 1,
            'up': 1,
            'shutdown': 0,
        },
        'ac': {
            'total': 1,
            'up': 1,
            'down': 0,
        },
        'pw': {
            'total': 1,
            'up': 1,
            'down': 0,
        },
    }

    golden_output1 = {'execute.return_value': '''
        Device1# show l2vpn bridge-domain summary

        Number of groups: 1, bridge-domains: 1, Up: 1, Shutdown: 0
        Number of ACs: 1 Up: 1, Down: 0
        Number of PWs: 1 Up: 1, Down: 0
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowL2vpnBridgeDomainSummary(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowL2vpnBridgeDomainSummary(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)


# ==================================================
#  Unit test for 'show l2vpn bridge-domain summary'
# ==================================================

class TestShowL2vpnBridgeDomainBrief(unittest.TestCase):
    '''Unit test for "show l2vpn bridge-domain summary"'''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'bridge_group': {
            'g1': {
                'bridge_domain': {
                    'bd1': {
                        'id': 0,
                        'state': 'up',
                        'ac': {
                            'num_ac': 1,
                            'num_ac_up': 1,
                        },
                        'pw': {
                            'num_pw': 1,
                            'num_pw_up': 1,
                        },
                    },
                },
            },
        },
    }

    golden_output1 = {'execute.return_value': '''
        Device1# show l2vpn bridge-domain brief

        Bridge Group/Bridge-Domain Name  ID    State      Num ACs/up     Num PWs/up
        -------------------------------- ----- ---------- -------------- --------------
        g1/bd1                           0     up         1/1            1/1 
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowL2vpnBridgeDomainBrief(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowL2vpnBridgeDomainBrief(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)


# =================================================
#  Unit test for 'show l2vpn bridge-domain detail'
# =================================================

class TestShowL2vpnBridgeDomainDetail(unittest.TestCase):
    '''Unit test for "show l2vpn bridge-domain detail"'''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'bridge_group': {
            'g1': {
                'bridge_domain': {
                    'bd1': {
                        'state': 'up',
                        'id': 0,
                        'shg_id': 0,
                        'mst_i': 0,
                        'mac_learning': 'enabled',
                        'mac_withdraw': 'disabled',
                        'flooding': {
                            'broadcast_multicast': 'enabled',
                            'unknown_unicast': 'enabled',
                        },
                        'mac_aging_time': 300,
                        'mac_aging_type': 'inactivity',
                        'mac_limit': 4000,
                        'mac_limit_action': 'none',
                        'mac_limit_notification': 'syslog',
                        'mac_limit_reached': 'yes',
                        'security': 'disabled',
                        'dhcp_v4_snooping': 'disabled',
                        'mtu': 1500,
                        'ac': {
                            'num_ac': 1,
                            'num_ac_up': 1,
                            'interfaces': {
                                'GigabitEthernet0/1/0/0': {
                                    'state': 'up',
                                    'type': 'Ethernet',
                                    'mtu': 1500,
                                    'xc_id': '0x2000001',
                                    'interworking': 'none',
                                    'mst_i': 0,
                                    'mst_i_state': 'unprotected',
                                    'mac_learning': 'enabled',
                                    'flooding': {
                                        'broadcast_multicast': 'enabled',
                                        'unknown_unicast': 'enabled',
                                    },
                                    'mac_aging_time': 300,
                                    'mac_aging_type': 'inactivity',
                                    'mac_limit': 4000,
                                    'mac_limit_action': 'none',
                                    'mac_limit_notification': 'syslog',
                                    'mac_limit_reached': 'yes',
                                    'security': 'disabled',
                                    'dhcp_v4_snooping': 'disabled',
                                    'static_mac_address': ['0000.0000.0000', '0001.00ff.0205'],
                                    'statistics': {
                                        'packet_totals': {
                                            'receive': 3919680,
                                            'send': 9328,
                                        },
                                        'byte_totals': {
                                            'receive': 305735040,
                                            'send': 15022146,
                                        },
                                    },
                                },
                            },
                        },
                        'vfi': {
                            'num_vfi': 1,
                            '1': {
                                'neighbor': {
                                    '10.4.1.1': {
                                        'pw_id': {
                                            '1': {
                                                'state': 'up ( established )',
                                                'pw_class': 'mpls',
                                                'xc_id': '0xff000001',
                                                'encapsulation': 'MPLS',
                                                'protocol': 'LDP',
                                                'pw_type': 'Ethernet',
                                                'control_word': 'disabled',
                                                'interworking': 'none',
                                                'pw_backup_disable_delay': 0,
                                                'sequencing': 'not set',
                                                'mpls': {
                                                    'label': {
                                                        'local': '16003',
                                                        'remote': '16003',
                                                    },
                                                    'group_id': {
                                                        'local': '0x0',
                                                        'remote': '0x0',
                                                    },
                                                    'interface': {
                                                        'local': '1',
                                                        'remote': '1',
                                                    },
                                                    'mtu': {
                                                        'local': '1500',
                                                        'remote': '1500',
                                                    },
                                                    'control_word': {
                                                        'local': 'disabled',
                                                        'remote': 'disabled',
                                                    },
                                                    'pw_type': {
                                                        'local': 'Ethernet',
                                                        'remote': 'Ethernet',
                                                    },
                                                    'vccv_cv_type': {
                                                        'local': '0x2',
                                                        'remote': '0x2',
                                                        'local_type': ['LSP ping verification'],
                                                        'remote_type': ['LSP ping verification'],
                                                    },
                                                    'vccv_cc_type': {
                                                        'local': '0x2',
                                                        'remote': '0x2',
                                                        'local_type': ['router alert label'],
                                                        'remote_type': ['router alert label'],
                                                    },
                                                },
                                                'create_time': '12/03/2008 14:03:00 (17:17:30 ago)',
                                                'last_time_status_changed': '13/03/2008 05:57:58 (01:22:31 ago)',
                                                'mac_withdraw_message': {
                                                    'send': 0,
                                                    'receive': 0,
                                                },
                                                'statistics': {
                                                    'packet_totals': {
                                                        'receive': 3918814,
                                                        'send': 3918024,
                                                    },
                                                    'byte_totals': {
                                                        'receive': 305667492,
                                                        'send': 321277968,
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                                'statistics': {
                                    'drop': {
                                        'illegal_vlan': 0,
                                        'illegal_length': 0,
                                    },
                                },
                            },
                        },
                        'pw': {
                            'num_pw': 1,
                            'num_pw_up': 1,
                        },
                    },
                },
            },
        },
    }

    golden_output1 = {'execute.return_value': '''
        Bridge group: g1, bridge-domain: bd1, id: 0, state: up, ShgId: 0, MSTi: 0
        MAC learning: enabled
        MAC withdraw: disabled
        Flooding:
            Broadcast & Multicast: enabled
            Unknown unicast: enabled
        MAC aging time: 300 s, Type: inactivity
        MAC limit: 4000, Action: none, Notification: syslog
        MAC limit reached: yes
        Security: disabled
        DHCPv4 snooping: disabled
        MTU: 1500
        Filter MAC addresses:
        ACs: 1 (1 up), VFIs: 1, PWs: 1 (1 up)
        List of ACs:
            AC: GigabitEthernet0/1/0/0, state is up
            Type Ethernet
            MTU 1500; XC ID 0x2000001; interworking none; MSTi 0 (unprotected)
            MAC learning: enabled
            Flooding:
                Broadcast & Multicast: enabled
                Unknown unicast: enabled
            MAC aging time: 300 s, Type: inactivity
            MAC limit: 4000, Action: none, Notification: syslog
            MAC limit reached: yes
            Security: disabled
            DHCPv4 snooping: disabled
            Static MAC addresses:
                0000.0000.0000
                0001.00ff.0205
            Statistics:
                packet totals: receive 3919680,send 9328
                byte totals: receive 305735040,send 15022146
        List of Access PWs:
        List of VFIs:
            VFI 1
            PW: neighbor 10.4.1.1, PW ID 1, state is up ( established )
                PW class mpls, XC ID 0xff000001
                Encapsulation MPLS, protocol LDP
                PW type Ethernet, control word disabled, interworking none
                PW backup disable delay 0 sec
                Sequencing not set
                        MPLS         Local                          Remote                        
                ------------ ------------------------------ -------------------------
                Label        16003                          16003                         
                Group ID     0x0                            0x0                           
                Interface    1                              1                             
                MTU          1500                           1500                          
                Control word disabled                       disabled                      
                PW type      Ethernet                       Ethernet                      
                VCCV CV type 0x2                            0x2                           
                             (LSP ping verification)        (LSP ping verification)       
                VCCV CC type 0x2                            0x2                           
                             (router alert label)           (router alert label)          
                ------------ ------------------------------ -------------------------
                Create time: 12/03/2008 14:03:00 (17:17:30 ago)
                Last time status changed: 13/03/2008 05:57:58 (01:22:31 ago)
                MAC withdraw message: send 0 receive 0
                Static MAC addresses:
                Statistics:
                packet totals: receive 3918814, send 3918024
                byte totals: receive 305667492, send 321277968
            VFI Statistics:
                drops: illegal VLAN 0, illegal length 0
    '''}

    golden_parsed_output2 = {
        'bridge_group': {
            'foo_group': {
                'bridge_domain': {
                    'foo_bd': {
                        'state': 'up',
                        'id': 0,
                        'shg_id': 0,
                        'mode': 'VPWS',
                        'mtu': 1500,
                        'ac': {
                            'num_ac': 1,
                            'num_ac_up': 0,
                            'interfaces': {
                                'GigabitEthernet0/5/1/4': {
                                    'state': 'admin down',
                                    'type': 'Ethernet',
                                    'mtu': 1500,
                                    'xc_id': '1',
                                    'interworking': 'none',
                                    'statistics': {
                                        'packet_totals': {
                                            'receive': 0,
                                            'send': 0,
                                        },
                                        'byte_totals': {
                                            'receive': 0,
                                            'send': 0,
                                        },
                                    },
                                },
                            },
                        },
                        'vfi': {
                            'num_vfi': 1,
                            'foo_vfi': {
                                'neighbor': {
                                    '10.4.1.1': {
                                        'pw_id': {
                                            '1': {
                                                'state': 'up ( established )',
                                                'pw_class': 'not set',
                                                'encapsulation': 'MPLS',
                                                'protocol': 'LDP',
                                                'pw_type': 'Ethernet',
                                                'control_word': 'enabled',
                                                'interworking': 'none',
                                                'sequencing': 'not set',
                                                'mpls': {
                                                    'label': {
                                                        'local': '16001',
                                                        'remote': '16001',
                                                    },
                                                    'group_id': {
                                                        'local': 'unassigned',
                                                        'remote': 'unknown',
                                                    },
                                                    'interface': {
                                                        'local': 'siva/vfi',
                                                        'remote': 'siva/vfi',
                                                    },
                                                    'mtu': {
                                                        'local': '1500',
                                                        'remote': '1500',
                                                    },
                                                    'control_word': {
                                                        'local': 'enabled',
                                                        'remote': 'enabled',
                                                    },
                                                    'pw_type': {
                                                        'local': 'Ethernet',
                                                        'remote': 'Ethernet',
                                                    },
                                                    'vccv_cv_type': {
                                                        'local': '0x2',
                                                        'remote': '0x2',
                                                        'local_type': ['LSP ping verification'],
                                                        'remote_type': ['LSP ping verification'],
                                                    },
                                                    'vccv_cc_type': {
                                                        'local': '0x3',
                                                        'remote': '0x3',
                                                        'local_type': ['control word', 'router alert label'],
                                                        'remote_type': ['control word', 'router alert label'],
                                                    },
                                                },
                                                'create_time': '25/06/2007 05:29:42 (2w0d ago)',
                                                'last_time_status_changed': '27/06/2007 06:50:35 (1w5d ago)',
                                            },
                                            '2': {
                                                'state': 'up ( established )',
                                                'pw_class': 'not set',
                                                'encapsulation': 'MPLS',
                                                'protocol': 'LDP',
                                                'pw_type': 'Ethernet',
                                                'control_word': 'enabled',
                                                'interworking': 'none',
                                                'sequencing': 'not set',
                                                'mpls': {
                                                    'label': {
                                                        'local': '16002',
                                                        'remote': '16002',
                                                    },
                                                    'group_id': {
                                                        'local': 'unassigned',
                                                        'remote': 'unknown',
                                                    },
                                                    'monitor_interface': {
                                                        'local': 'siva/vfi',
                                                        'remote': 'siva/vfi',
                                                    },
                                                    'mtu': {
                                                        'local': '1500',
                                                        'remote': '1500',
                                                    },
                                                    'control_word': {
                                                        'local': 'enabled',
                                                        'remote': 'enabled',
                                                    },
                                                    'pw_type': {
                                                        'local': 'Ethernet',
                                                        'remote': 'Ethernet',
                                                    },
                                                    'vccv_cv_type': {
                                                        'local': '0x2',
                                                        'remote': '0x2',
                                                        'local_type': ['LSP ping verification'],
                                                        'remote_type': ['LSP ping verification'],
                                                    },
                                                    'vccv_cc_type': {
                                                        'local': '0x3',
                                                        'remote': '0x3',
                                                        'local_type': ['control word', 'router alert label'],
                                                        'remote_type': ['control word', 'router alert label'],
                                                    },
                                                },
                                                'create_time': '25/06/2007 05:29:42 (2w0d ago)',
                                                'last_time_status_changed': '27/06/2007 06:50:35 (1w5d ago)',
                                            },
                                        },
                                    },
                                },
                                'statistics': {
                                    'drop': {
                                        'illegal_vlan': 0,
                                        'illegal_length': 0,
                                    },
                                },
                            },
                        },
                        'pw': {
                            'num_pw': 2,
                            'num_pw_up': 2,
                        },
                    },
                },
            },
        },
    }

    golden_output2 = {'execute.return_value': '''
        Bridge group: foo_group, bridge-domain: foo_bd, id: 0, state: up, ShgId: 0
        VPWS Mode
        MTU: 1500
        ACs: 1 (0 up), VFIs: 1, PWs: 2 (2 up)
        List of ACs:
            AC: GigabitEthernet0/5/1/4, state is admin down
            Type Ethernet      MTU 1500; XC ID 1; interworking none
            Static MAC addresses:
            Statistics:
                packet totals: receive 0,send 0
                byte totals: receive 0,send 0
        List of VFIs:
            VFI foo_vfi
            PW: neighbor 10.4.1.1, PW ID 1, state is up ( established )
                PW class not set
                Encapsulation MPLS, protocol LDP
                PW type Ethernet, control word enabled, interworking none
                Sequencing not set
                MPLS         Local                          Remote                        
                ------------ ------------------------------ ------------------------------
                Label        16001                          16001
                Group ID     unassigned                     unknown                       
                Interface    siva/vfi                       siva/vfi                      
                MTU          1500                           1500                          
                Control word enabled                        enabled                       
                PW type      Ethernet                       Ethernet                      
                VCCV CV type 0x2                            0x2                           
                             (LSP ping verification)        (LSP ping verification)       
                VCCV CC type 0x3                            0x3                           
                             (control word)                 (control word)                
                             (router alert label)           (router alert label)          
                ------------ ------------------------------ ------------------------------
                Create time: 25/06/2007 05:29:42 (2w0d ago)
                Last time status changed: 27/06/2007 06:50:35 (1w5d ago)
            Static MAC addresses:
            PW: neighbor 10.4.1.1, PW ID 2, state is up ( established )
                PW class not set
                Encapsulation MPLS, protocol LDP
                PW type Ethernet, control word enabled, interworking none
                Sequencing not set
                MPLS         Local                          Remote                        
                ------------ ------------------------------ ------------------------------
                Label        16002                          16002                         
                Group ID     unassigned                     unknown                       
                Interface    siva/vfi                       siva/vfi                      
                MTU          1500                           1500                          
                Control word enabled                        enabled                       
                PW type      Ethernet                       Ethernet                      
                VCCV CV type 0x2                            0x2                           
                            (LSP ping verification)        (LSP ping verification)       
                VCCV CC type 0x3                            0x3                           
                            (control word)                 (control word)                
                            (router alert label)           (router alert label)          
                ------------ ------------------------------ ------------------------------
                Create time: 25/06/2007 05:29:42 (2w0d ago)
                Last time status changed: 27/06/2007 06:50:35 (1w5d ago)
            Static MAC addresses:
            Statistics:
                drops: illegal VLAN 0, illegal length 0
    '''}

    golden_parsed_output3 = {
        'legend': 'pp = Partially Programmed.',
        'bridge_group': {
            'EVPN-Mulicast': {
                'bridge_domain': {
                    'EVPN-Multicast-Genie': {
                        'state': 'up',
                        'id': 0,
                        'shg_id': 0,
                        'mst_i': 0,
                        'coupled_state': 'disabled',
                        'vine_state': 'EVPN-IRB',
                        'mac_learning': 'enabled',
                        'mac_withdraw': 'enabled',
                        'mac_withdraw_for_access_pw': 'enabled',
                        'mac_withdraw_sent_on': 'bridge port up',
                        'mac_withdraw_relaying': 'disabled',
                        'flooding': {
                            'broadcast_multicast': 'enabled',
                            'unknown_unicast': 'enabled',
                        },
                        'mac_aging_time': 300,
                        'mac_aging_type': 'inactivity',
                        'mac_limit': 4000,
                        'mac_limit_action': 'none',
                        'mac_limit_notification': 'syslog',
                        'mac_limit_reached': 'no',
                        'mac_limit_threshold': '75%',
                        'mac_port_down_flush': 'enabled',
                        'mac_secure': 'disabled',
                        'mac_secure_logging': 'disabled',
                        'split_horizon_group': 'none',
                        'dynamic_arp_inspection': 'disabled',
                        'dynamic_arp_logging': 'disabled',
                        'ip_source_guard': 'disabled',
                        'ip_source_logging': 'disabled',
                        'dhcp_v4_snooping': 'disabled',
                        'dhcp_v4_snooping_profile': 'none',
                        'igmp_snooping': 'disabled',
                        'igmp_snooping_profile': 'none',
                        'mld_snooping_profile': 'none',
                        'storm_control': 'bridge-domain policer',
                        'bridge_mtu': '1500',
                        'mid_cvpls_config_index': '1',
                        'p2mp_pw': 'disabled',
                        'create_time': '27/08/2019 09:44:44 (5w6d ago)',
                        'status_changed_since_creation': 'No',
                        'ac': {
                            'num_ac': 3,
                            'num_ac_up': 2,
                            'interfaces': {
                                'BVI100': {
                                    'state': 'up',
                                    'type': 'Routed-Interface',
                                    'mtu': 1514,
                                    'xc_id': '0x8000000b',
                                    'interworking': 'none',
                                    'bvi_mac_address': ['1000.10ff.1000'],
                                    'split_horizon_group': 'Access',
                                },
                                'Bundle-Ether3.100': {
                                    'state': 'down (Segment-down)',
                                    'type': 'VLAN',
                                    'vlan_num_ranges': '1',
                                    'rewrite_tags': '',
                                    'vlan_ranges': ['100', '100'],
                                    'mtu': 9202,
                                    'xc_id': '0xc0000002',
                                    'interworking': 'none',
                                    'mst_i': 5,
                                    'mac_learning': 'enabled',
                                    'flooding': {
                                        'broadcast_multicast': 'enabled',
                                        'unknown_unicast': 'enabled',
                                    },
                                    'mac_aging_time': 300,
                                    'mac_aging_type': 'inactivity',
                                    'mac_limit': 4000,
                                    'mac_limit_action': 'none',
                                    'mac_limit_notification': 'syslog',
                                    'mac_limit_reached': 'no',
                                    'mac_limit_threshold': '75%',
                                    'split_horizon_group': 'none',
                                    'dhcp_v4_snooping': 'disabled',
                                    'dhcp_v4_snooping_profile': 'none',
                                    'igmp_snooping': 'disabled',
                                    'igmp_snooping_profile': 'none',
                                    'mld_snooping_profile': 'none',
                                },
                                'Bundle-Ether4.100': {
                                    'state': 'up',
                                    'type': 'VLAN',
                                    'vlan_num_ranges': '1',
                                    'rewrite_tags': '',
                                    'vlan_ranges': ['100', '100'],
                                    'mtu': 9202,
                                    'xc_id': '0xc0000004',
                                    'interworking': 'none',
                                    'mst_i': 5,
                                    'mac_learning': 'enabled',
                                    'flooding': {
                                        'broadcast_multicast': 'enabled',
                                        'unknown_unicast': 'enabled',
                                    },
                                    'mac_aging_time': 300,
                                    'mac_aging_type': 'inactivity',
                                    'mac_limit': 4000,
                                    'mac_limit_action': 'none',
                                    'mac_limit_notification': 'syslog',
                                    'mac_limit_reached': 'no',
                                    'mac_limit_threshold': '75%',
                                    'split_horizon_group': 'none',
                                    'dhcp_v4_snooping': 'disabled',
                                    'dhcp_v4_snooping_profile': 'none',
                                    'igmp_snooping': 'disabled',
                                    'igmp_snooping_profile': 'none',
                                    'mld_snooping_profile': 'none',
                                    'statistics': {
                                        'packet_totals': {
                                            'receive': 1017635,
                                            'send': 798,
                                        },
                                        'byte_totals': {
                                            'receive': 73168116,
                                            'send': 36708,
                                        },
                                        'mac_move': '0',
                                    },
                                    'storm_control_drop_counters': {
                                        'packets': {
                                            'broadcast': '0',
                                            'multicast': '0',
                                            'unknown_unicast': '0',
                                        },
                                        'bytes': {
                                            'broadcast': '0',
                                            'multicast': '0',
                                            'unknown_unicast': '0',
                                        },
                                    },
                                    'dynamic_arp_inspection_drop_counters': {
                                        'packets': '0',
                                        'bytes': '0',
                                    },
                                    'ip_source_guard_drop_counters': {
                                        'packets': '0',
                                        'bytes': '0',
                                    },
                                },
                            },
                        },
                        'vfi': {
                            'num_vfi': 0,
                        },
                        'pw': {
                            'num_pw': 0,
                            'num_pw_up': 0,
                        },
                        'pbb': {
                            'num_pbb': 0,
                            'num_pbb_up': 0,
                        },
                        'vni': {
                            'num_vni': 0,
                            'num_vni_up': 0,
                        },
                        'evpn': {
                            'EVPN': {
                                'state': 'up',
                                'evi': '1000',
                                'xc_id': '0x80000009',
                                'statistics': {
                                    'packet_totals': {
                                        'receive': 0,
                                        'send': 0,
                                    },
                                    'byte_totals': {
                                        'receive': 0,
                                        'send': 0,
                                    },
                                    'mac_move': '0',
                                },
                            },
                        },
                    },
                },
            },
        },
    }
    golden_output3 = {'execute.return_value': '''
        show l2vpn bridge-domain detail

        Mon Oct  7 16:18:59.168 EDT
        Legend: pp = Partially Programmed.
        Bridge group: EVPN-Mulicast, bridge-domain: EVPN-Multicast-Genie, id: 0, state: up, ShgId: 0, MSTi: 0
        Coupled state: disabled
        VINE state: EVPN-IRB
        MAC learning: enabled
        MAC withdraw: enabled
            MAC withdraw for Access PW: enabled
            MAC withdraw sent on: bridge port up
            MAC withdraw relaying (access to access): disabled
        Flooding:
            Broadcast & Multicast: enabled
            Unknown unicast: enabled
        MAC aging time: 300 s, Type: inactivity
        MAC limit: 4000, Action: none, Notification: syslog
        MAC limit reached: no, threshold: 75%
        MAC port down flush: enabled
        MAC Secure: disabled, Logging: disabled
        Split Horizon Group: none
        Dynamic ARP Inspection: disabled, Logging: disabled
        IP Source Guard: disabled, Logging: disabled
        DHCPv4 Snooping: disabled
        DHCPv4 Snooping profile: none
        IGMP Snooping: disabled
        IGMP Snooping profile: none
        MLD Snooping profile: none
        Storm Control: disabled
        Bridge MTU: 1500
        MIB cvplsConfigIndex: 1
        Filter MAC addresses:
        P2MP PW: disabled
        Create time: 27/08/2019 09:44:44 (5w6d ago)
        No status change since creation
        ACs: 3 (2 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
            evi: 1000
            XC ID 0x80000009
            Statistics:
            packets: received 0 (unicast 0), sent 0
            bytes: received 0 (unicast 0), sent 0
            MAC move: 0
        List of ACs:
            AC: BVI100, state is up
            Type Routed-Interface
            MTU 1514; XC ID 0x8000000b; interworking none
            BVI MAC address:
                1000.10ff.1000
            Split Horizon Group: Access
            AC: Bundle-Ether3.100, state is down (Segment-down)
            Type VLAN; Num Ranges: 1
            Rewrite Tags: []
            VLAN ranges: [100, 100]
            MTU 9202; XC ID 0xc0000002; interworking none; MSTi 5
            MAC learning: enabled
            Flooding:
                Broadcast & Multicast: enabled
                Unknown unicast: enabled
            MAC aging time: 300 s, Type: inactivity
            MAC limit: 4000, Action: none, Notification: syslog
            MAC limit reached: no, threshold: 75%
            MAC port down flush: enabled
            MAC Secure: disabled, Logging: disabled
            Split Horizon Group: none
            Dynamic ARP Inspection: disabled, Logging: disabled
            IP Source Guard: disabled, Logging: disabled
            DHCPv4 Snooping: disabled
            DHCPv4 Snooping profile: none
            IGMP Snooping: disabled
            IGMP Snooping profile: none
            MLD Snooping profile: none
            Storm Control: bridge-domain policer
            Static MAC addresses:
            AC: Bundle-Ether4.100, state is up
            Type VLAN; Num Ranges: 1
            Rewrite Tags: []
            VLAN ranges: [100, 100]
            MTU 9202; XC ID 0xc0000004; interworking none; MSTi 5
            MAC learning: enabled
            Flooding:
                Broadcast & Multicast: enabled
                Unknown unicast: enabled
            MAC aging time: 300 s, Type: inactivity
            MAC limit: 4000, Action: none, Notification: syslog
            MAC limit reached: no, threshold: 75%
            MAC port down flush: enabled
            MAC Secure: disabled, Logging: disabled
            Split Horizon Group: none
            Dynamic ARP Inspection: disabled, Logging: disabled
            IP Source Guard: disabled, Logging: disabled
            DHCPv4 Snooping: disabled
            DHCPv4 Snooping profile: none
            IGMP Snooping: disabled
            IGMP Snooping profile: none
            MLD Snooping profile: none
            Storm Control: bridge-domain policer
            Static MAC addresses:
            Statistics:
                packets: received 1017635 (multicast 1016837, broadcast 798, unknown unicast 0, unicast 0), sent 798
                bytes: received 73168116 (multicast 73120236, broadcast 47880, unknown unicast 0, unicast 0), sent 36708
                MAC move: 0
            Storm control drop counters: 
                packets: broadcast 0, multicast 0, unknown unicast 0 
                bytes: broadcast 0, multicast 0, unknown unicast 0 
            Dynamic ARP inspection drop counters: 
                packets: 0, bytes: 0
            IP source guard drop counters: 
                packets: 0, bytes: 0
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        RP/0/RSP0/CPU0:genie-Router#
    '''}

    golden_output4 = {'execute.return_value': '''
        show l2vpn bridge-domain detail

        Mon Oct 14 17:43:20.059 EDT
        Legend: pp = Partially Programmed.
        Bridge group: midlay, bridge-domain: bd601, id: 0, state: up, ShgId: 0, MSTi: 0
        Coupled state: disabled
        VINE state: BVI Resolved
        MAC learning: enabled
        MAC withdraw: enabled
            MAC withdraw for Access PW: enabled
            MAC withdraw sent on: bridge port up
            MAC withdraw relaying (access to access): disabled
        Flooding:
            Broadcast & Multicast: enabled
            Unknown unicast: enabled
        MAC aging time: 300 s, Type: inactivity
        MAC limit: 4000, Action: none, Notification: syslog
        MAC limit reached: no, threshold: 75%
        MAC port down flush: enabled
        MAC Secure: disabled, Logging: disabled
        Split Horizon Group: none
        Dynamic ARP Inspection: disabled, Logging: disabled
        IP Source Guard: disabled, Logging: disabled
        DHCPv4 Snooping: disabled
        DHCPv4 Snooping profile: none
        IGMP Snooping: disabled
        IGMP Snooping profile: none
        MLD Snooping profile: none
        Storm Control: disabled
        Bridge MTU: 1500
        MIB cvplsConfigIndex: 1
        Filter MAC addresses:
        P2MP PW: disabled
        Create time: 11/07/2019 13:01:43 (13w4d ago)
        No status change since creation
        ACs: 1 (0 up), VFIs: 0, PWs: 1 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of ACs:
            AC: BVI601, state is down (Segment-down)
            Type Routed-Interface
            MTU 1514; XC ID 0x8000000d; interworking none
            Error: Need at least 1 bridge port up
            BVI MAC address:
                00c1.64ff.f53f
            Split Horizon Group: Access
        List of Access PWs:
            EVPN: neighbor 0.0.0.0, PW ID: evi 601, ac-id 1, state is down ( local ready ) (Transport LSP Down)
            XC ID 0xa0000009
            Encapsulation MPLS
            Source address 10.154.219.85
            Encap type Ethernet, control word enabled
            Sequencing not set
            LSP : Up

                EVPN         Local                          Remote                        
                ------------ ------------------------------ ---------------------------
                Label        100482                         unknown                       
                MTU          1500                           unknown                       
                Control word enabled                        unknown                       
                AC ID        1                              1                             
                EVPN type    Ethernet                       unknown                       

                ------------ ------------------------------ ---------------------------
            Create time: 11/07/2019 13:01:43 (13w4d ago)
            Last time status changed: 11/07/2019 13:06:41 (13w4d ago)
            MAC withdraw messages: sent 0, received 0
            Forward-class: 0
            Static MAC addresses:
            MAC learning: enabled
            Flooding:
                Broadcast & Multicast: enabled
                Unknown unicast: enabled
            MAC aging time: 300 s, Type: inactivity
            MAC limit: 4000, Action: none, Notification: syslog
            MAC limit reached: no, threshold: 75%
            MAC port down flush: enabled
            MAC Secure: disabled, Logging: disabled
            Split Horizon Group: none
            DHCPv4 Snooping: disabled
            DHCPv4 Snooping profile: none
            IGMP Snooping: disabled
            IGMP Snooping profile: none
            MLD Snooping profile: none
            Storm Control: bridge-domain policer
        List of VFIs:
        List of Access VFIs:
        Bridge group: EVPN-Mulicast, bridge-domain: EVPN-Multicast-Genie, id: 1, state: up, ShgId: 0, MSTi: 0
        Coupled state: disabled
        VINE state: EVPN-IRB
        MAC learning: enabled
        MAC withdraw: enabled
            MAC withdraw for Access PW: enabled
            MAC withdraw sent on: bridge port up
            MAC withdraw relaying (access to access): disabled
        Flooding:
            Broadcast & Multicast: enabled
            Unknown unicast: enabled
        MAC aging time: 300 s, Type: inactivity
        MAC limit: 4000, Action: none, Notification: syslog
        MAC limit reached: no, threshold: 75%
        MAC port down flush: enabled
        MAC Secure: disabled, Logging: disabled
        Split Horizon Group: none
        Dynamic ARP Inspection: disabled, Logging: disabled
        IP Source Guard: disabled, Logging: disabled
        DHCPv4 Snooping: disabled
        DHCPv4 Snooping profile: none
        IGMP Snooping: disabled
        IGMP Snooping profile: none
        MLD Snooping profile: none
        Storm Control: disabled
        Bridge MTU: 1500
        MIB cvplsConfigIndex: 2
        Filter MAC addresses:
        P2MP PW: disabled
        Create time: 11/07/2019 13:01:43 (13w4d ago)
        No status change since creation
        ACs: 3 (0 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
            evi: 1000
            XC ID 0x80000007
            Statistics:
            packets: received 10305221406 (unicast 74), sent 41020743245
            bytes: received 10474510995022 (unicast 3108), sent 41841158015034
            MAC move: 0
        List of ACs:
            AC: BVI100, state is down (Segment-down)
            Type Routed-Interface
            MTU 1514; XC ID 0x8000000b; interworking none
            Error: Need at least 1 bridge port up
            BVI MAC address:
                1000.10ff.1000
            Split Horizon Group: Access
            AC: Bundle-Ether3.100, state is down (Segment-down)
            Type VLAN; Num Ranges: 1
            Rewrite Tags: []
            VLAN ranges: [100, 100]
            MTU 9202; XC ID 0xc0000004; interworking none; MSTi 5
            MAC learning: enabled
            Flooding:
                Broadcast & Multicast: enabled
                Unknown unicast: enabled
            MAC aging time: 300 s, Type: inactivity
            MAC limit: 4000, Action: none, Notification: syslog
            MAC limit reached: no, threshold: 75%
            MAC port down flush: enabled
            MAC Secure: disabled, Logging: disabled
            Split Horizon Group: none
            Dynamic ARP Inspection: disabled, Logging: disabled
            IP Source Guard: disabled, Logging: disabled
            DHCPv4 Snooping: disabled
            DHCPv4 Snooping profile: none
            IGMP Snooping: disabled
            IGMP Snooping profile: none
            MLD Snooping profile: none
            Storm Control: bridge-domain policer
            Static MAC addresses:
            AC: Bundle-Ether4.100, state is down (Segment-down)
            Type VLAN; Num Ranges: 1
            Rewrite Tags: []
            VLAN ranges: [100, 100]
            MTU 9202; XC ID 0xc0000006; interworking none; MSTi 5
            MAC learning: enabled
            Flooding:
                Broadcast & Multicast: enabled
                Unknown unicast: enabled
            MAC aging time: 300 s, Type: inactivity
            MAC limit: 4000, Action: none, Notification: syslog
            MAC limit reached: no, threshold: 75%
            MAC port down flush: enabled
            MAC Secure: disabled, Logging: disabled
            Split Horizon Group: none
            Dynamic ARP Inspection: disabled, Logging: disabled
            IP Source Guard: disabled, Logging: disabled
            DHCPv4 Snooping: disabled
            DHCPv4 Snooping profile: none
            IGMP Snooping: disabled
            IGMP Snooping profile: none
            MLD Snooping profile: none
            Storm Control: bridge-domain policer
            Static MAC addresses:
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:

    '''}

    golden_parsed_output4 = {
        'legend': 'pp = Partially Programmed.',
        'bridge_group': {
            'midlay': {
                'bridge_domain': {
                    'bd601': {
                        'state': 'up',
                        'id': 0,
                        'shg_id': 0,
                        'mst_i': 0,
                        'coupled_state': 'disabled',
                        'vine_state': 'BVI',
                        'mac_learning': 'enabled',
                        'mac_withdraw': 'enabled',
                        'mac_withdraw_for_access_pw': 'enabled',
                        'mac_withdraw_sent_on': 'bridge port up',
                        'mac_withdraw_relaying': 'disabled',
                        'flooding': {
                            'broadcast_multicast': 'enabled',
                            'unknown_unicast': 'enabled',
                        },
                        'mac_aging_time': 300,
                        'mac_aging_type': 'inactivity',
                        'mac_limit': 4000,
                        'mac_limit_action': 'none',
                        'mac_limit_notification': 'syslog',
                        'mac_limit_reached': 'no',
                        'mac_limit_threshold': '75%',
                        'mac_port_down_flush': 'enabled',
                        'mac_secure': 'disabled',
                        'mac_secure_logging': 'disabled',
                        'split_horizon_group': 'none',
                        'dynamic_arp_inspection': 'disabled',
                        'dynamic_arp_logging': 'disabled',
                        'ip_source_guard': 'disabled',
                        'ip_source_logging': 'disabled',
                        'dhcp_v4_snooping': 'disabled',
                        'dhcp_v4_snooping_profile': 'none',
                        'igmp_snooping': 'disabled',
                        'igmp_snooping_profile': 'none',
                        'mld_snooping_profile': 'none',
                        'storm_control': 'disabled',
                        'bridge_mtu': '1500',
                        'mid_cvpls_config_index': '1',
                        'p2mp_pw': 'disabled',
                        'create_time': '11/07/2019 13:01:43 (13w4d ago)',
                        'status_changed_since_creation': 'No',
                        'ac': {
                            'num_ac': 1,
                            'num_ac_up': 0,
                            'interfaces': {
                                'BVI601': {
                                    'state': 'down (Segment-down)',
                                    'type': 'Routed-Interface',
                                    'mtu': 1514,
                                    'xc_id': '0x8000000d',
                                    'interworking': 'none',
                                    'error': 'Need at least 1 bridge port up',
                                    'bvi_mac_address': ['00c1.64ff.f53f'],
                                    'split_horizon_group': 'Access',
                                },
                            },
                        },
                        'vfi': {
                            'num_vfi': 0,
                        },
                        'pw': {
                            'num_pw': 1,
                            'num_pw_up': 0,
                        },
                        'pbb': {
                            'num_pbb': 0,
                            'num_pbb_up': 0,
                        },
                        'vni': {
                            'num_vni': 0,
                            'num_vni_up': 0,
                        },
                        'access_pw': {
                            'EVPN': {
                                'neighbor': {
                                    '0.0.0.0': {
                                        'pw_id': {
                                            'evi 601': {
                                                'ac_id': '1',
                                                'state': 'down ( local ready ) (Transport LSP Down)',
                                                'xc_id': '0xa0000009',
                                                'encapsulation': 'MPLS',
                                                'source_address': '10.154.219.85',
                                                'encap_type': 'Ethernet',
                                                'control_word': 'enabled',
                                                'sequencing': 'not set',
                                                'lsp': {
                                                    'state': 'Up',
                                                    'evpn': {
                                                        'label': {
                                                            'local': '100482',
                                                            'remote': 'unknown',
                                                        },
                                                        'mtu': {
                                                            'local': '1500',
                                                            'remote': 'unknown',
                                                        },
                                                        'control_word': {
                                                            'local': 'enabled',
                                                            'remote': 'unknown',
                                                        },
                                                        'ac_id': {
                                                            'local': '1',
                                                            'remote': '1',
                                                        },
                                                        'evpn_type': {
                                                            'local': 'Ethernet',
                                                            'remote': 'unknown',
                                                        },
                                                    },
                                                },
                                                'create_time': '11/07/2019 13:01:43 (13w4d ago)',
                                                'last_time_status_changed': '11/07/2019 13:06:41 (13w4d ago)',
                                                'mac_withdraw_message': {
                                                    'send': 0,
                                                    'receive': 0,
                                                },
                                                'forward_class': '0',
                                                'mac_learning': 'enabled',
                                                'flooding': {
                                                    'broadcast_multicast': 'enabled',
                                                    'unknown_unicast': 'enabled',
                                                },
                                                'mac_aging_time': 300,
                                                'mac_aging_type': 'inactivity',
                                                'mac_limit': 4000,
                                                'mac_limit_action': 'none',
                                                'mac_limit_notification': 'syslog',
                                                'mac_limit_reached': 'no',
                                                'mac_limit_threshold': '75%',
                                                'mac_port_down_flush': 'enabled',
                                                'mac_secure': 'disabled',
                                                'mac_secure_logging': 'disabled',
                                                'split_horizon_group': 'none',
                                                'dhcp_v4_snooping': 'disabled',
                                                'dhcp_v4_snooping_profile': 'none',
                                                'igmp_snooping': 'disabled',
                                                'igmp_snooping_profile': 'none',
                                                'mld_snooping_profile': 'none',
                                                'storm_control': 'bridge-domain policer',
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
            'EVPN-Mulicast': {
                'bridge_domain': {
                    'EVPN-Multicast-Genie': {
                        'state': 'up',
                        'id': 1,
                        'shg_id': 0,
                        'mst_i': 0,
                        'coupled_state': 'disabled',
                        'vine_state': 'EVPN-IRB',
                        'mac_learning': 'enabled',
                        'mac_withdraw': 'enabled',
                        'mac_withdraw_for_access_pw': 'enabled',
                        'mac_withdraw_sent_on': 'bridge port up',
                        'mac_withdraw_relaying': 'disabled',
                        'flooding': {
                            'broadcast_multicast': 'enabled',
                            'unknown_unicast': 'enabled',
                        },
                        'mac_aging_time': 300,
                        'mac_aging_type': 'inactivity',
                        'mac_limit': 4000,
                        'mac_limit_action': 'none',
                        'mac_limit_notification': 'syslog',
                        'mac_limit_reached': 'no',
                        'mac_limit_threshold': '75%',
                        'mac_port_down_flush': 'enabled',
                        'mac_secure': 'disabled',
                        'mac_secure_logging': 'disabled',
                        'split_horizon_group': 'none',
                        'dynamic_arp_inspection': 'disabled',
                        'dynamic_arp_logging': 'disabled',
                        'ip_source_guard': 'disabled',
                        'ip_source_logging': 'disabled',
                        'dhcp_v4_snooping': 'disabled',
                        'dhcp_v4_snooping_profile': 'none',
                        'igmp_snooping': 'disabled',
                        'igmp_snooping_profile': 'none',
                        'mld_snooping_profile': 'none',
                        'storm_control': 'bridge-domain policer',
                        'bridge_mtu': '1500',
                        'mid_cvpls_config_index': '2',
                        'p2mp_pw': 'disabled',
                        'create_time': '11/07/2019 13:01:43 (13w4d ago)',
                        'status_changed_since_creation': 'No',
                        'ac': {
                            'num_ac': 3,
                            'num_ac_up': 0,
                            'interfaces': {
                                'BVI100': {
                                    'state': 'down (Segment-down)',
                                    'type': 'Routed-Interface',
                                    'mtu': 1514,
                                    'xc_id': '0x8000000b',
                                    'interworking': 'none',
                                    'error': 'Need at least 1 bridge port up',
                                    'bvi_mac_address': ['1000.10ff.1000'],
                                    'split_horizon_group': 'Access',
                                },
                                'Bundle-Ether3.100': {
                                    'state': 'down (Segment-down)',
                                    'type': 'VLAN',
                                    'vlan_num_ranges': '1',
                                    'rewrite_tags': '',
                                    'vlan_ranges': ['100', '100'],
                                    'mtu': 9202,
                                    'xc_id': '0xc0000004',
                                    'interworking': 'none',
                                    'mst_i': 5,
                                    'mac_learning': 'enabled',
                                    'flooding': {
                                        'broadcast_multicast': 'enabled',
                                        'unknown_unicast': 'enabled',
                                    },
                                    'mac_aging_time': 300,
                                    'mac_aging_type': 'inactivity',
                                    'mac_limit': 4000,
                                    'mac_limit_action': 'none',
                                    'mac_limit_notification': 'syslog',
                                    'mac_limit_reached': 'no',
                                    'mac_limit_threshold': '75%',
                                    'split_horizon_group': 'none',
                                    'dhcp_v4_snooping': 'disabled',
                                    'dhcp_v4_snooping_profile': 'none',
                                    'igmp_snooping': 'disabled',
                                    'igmp_snooping_profile': 'none',
                                    'mld_snooping_profile': 'none',
                                },
                                'Bundle-Ether4.100': {
                                    'state': 'down (Segment-down)',
                                    'type': 'VLAN',
                                    'vlan_num_ranges': '1',
                                    'rewrite_tags': '',
                                    'vlan_ranges': ['100', '100'],
                                    'mtu': 9202,
                                    'xc_id': '0xc0000006',
                                    'interworking': 'none',
                                    'mst_i': 5,
                                    'mac_learning': 'enabled',
                                    'flooding': {
                                        'broadcast_multicast': 'enabled',
                                        'unknown_unicast': 'enabled',
                                    },
                                    'mac_aging_time': 300,
                                    'mac_aging_type': 'inactivity',
                                    'mac_limit': 4000,
                                    'mac_limit_action': 'none',
                                    'mac_limit_notification': 'syslog',
                                    'mac_limit_reached': 'no',
                                    'mac_limit_threshold': '75%',
                                    'split_horizon_group': 'none',
                                    'dhcp_v4_snooping': 'disabled',
                                    'dhcp_v4_snooping_profile': 'none',
                                    'igmp_snooping': 'disabled',
                                    'igmp_snooping_profile': 'none',
                                    'mld_snooping_profile': 'none',
                                },
                            },
                        },
                        'vfi': {
                            'num_vfi': 0,
                        },
                        'pw': {
                            'num_pw': 0,
                            'num_pw_up': 0,
                        },
                        'pbb': {
                            'num_pbb': 0,
                            'num_pbb_up': 0,
                        },
                        'vni': {
                            'num_vni': 0,
                            'num_vni_up': 0,
                        },
                        'evpn': {
                            'EVPN': {
                                'state': 'up',
                                'evi': '1000',
                                'xc_id': '0x80000007',
                                'statistics': {
                                    'packet_totals': {
                                        'receive': 10305221406,
                                        'send': 41020743245,
                                    },
                                    'byte_totals': {
                                        'receive': 10474510995022,
                                        'send': 41841158015034,
                                    },
                                    'mac_move': '0',
                                },
                            },
                        },
                    },
                },
            },
        },
    }

    golden_output5 = {'execute.return_value': '''
        show l2vpn bridge-domain detail

        Mon Oct 21 10:42:15.158 EDT
        Legend: pp = Partially Programmed.
        Bridge group: EVPN-Multicast_genie, bridge-domain: EVPN-Multicast-Genie, id: 0, state: up, ShgId: 0, MSTi: 0
        Coupled state: disabled
        VINE state: EVPN-IRB
        MAC learning: enabled
        MAC withdraw: enabled
            MAC withdraw for Access PW: enabled
            MAC withdraw sent on: bridge port up
            MAC withdraw relaying (access to access): disabled
        Flooding:
            Broadcast & Multicast: enabled
            Unknown unicast: enabled
        MAC aging time: 300 s, Type: inactivity
        MAC limit: 64000, Action: none, Notification: syslog
        MAC limit reached: no, threshold: 75%
        MAC port down flush: enabled
        MAC Secure: disabled, Logging: disabled
        Split Horizon Group: none
        Dynamic ARP Inspection: disabled, Logging: disabled
        IP Source Guard: disabled, Logging: disabled
        DHCPv4 Snooping: disabled
        DHCPv4 Snooping profile: none
        IGMP Snooping: enabled
        IGMP Snooping profile: CUW-WTQQ
        MLD Snooping profile: none
        Storm Control: disabled
        Bridge MTU: 1500
        MIB cvplsConfigIndex: 1
        Filter MAC addresses:
        P2MP PW: disabled
        Multicast Source: Not Set
        Create time: 19/09/2019 10:23:31 (4w4d ago)
        No status change since creation
        ACs: 2 (0 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
            evi: 1000
            XC ID 0x80000004
            Statistics:
            packets: received 0 (unicast 0), sent 0
            bytes: received 0 (unicast 0), sent 0
            MAC move: 0
        List of ACs:
            AC: BVI100, state is down (Segment-down)
            Type Routed-Interface
            MTU 1514; XC ID 0x80000007; interworking none
            Error: Need at least 1 bridge port up
            BVI MAC address:
                1000.10ff.1000
            Split Horizon Group: Access
            PD System Data: AF-LIF-IPv4: 0x00000000  AF-LIF-IPv6: 0x00000000

            AC: Bundle-Ether11.100, state is down (Segment-down)
            Type VLAN; Num Ranges: 1
            Rewrite Tags: []
            VLAN ranges: [100, 100]
            MTU 9202; XC ID 0xa0000008; interworking none; MSTi 5
            MAC learning: enabled
            Flooding:
                Broadcast & Multicast: enabled
                Unknown unicast: enabled
            MAC aging time: 300 s, Type: inactivity
            MAC limit: 64000, Action: none, Notification: syslog
            MAC limit reached: no, threshold: 75%
            MAC port down flush: enabled
            MAC Secure: disabled, Logging: disabled
            Split Horizon Group: none
            E-Tree: Root
            Dynamic ARP Inspection: disabled, Logging: disabled
            IP Source Guard: disabled, Logging: disabled
            DHCPv4 Snooping: disabled
            DHCPv4 Snooping profile: none
            IGMP Snooping: enabled
            IGMP Snooping profile: CUW-WTQQ
            MLD Snooping profile: none
            Storm Control: bridge-domain policer
            Static MAC addresses:
            PD System Data: AF-LIF-IPv4: 0x00013807  AF-LIF-IPv6: 0x0001381d

        List of Access PWs:
        List of VFIs:
        List of Access VFIs:

    '''}

    golden_parsed_output5 = {
        'legend': 'pp = Partially Programmed.',
        'bridge_group': {
            'EVPN-Multicast_genie': {
                'bridge_domain': {
                    'EVPN-Multicast-Genie': {
                        'state': 'up',
                        'id': 0,
                        'shg_id': 0,
                        'mst_i': 0,
                        'coupled_state': 'disabled',
                        'vine_state': 'EVPN-IRB',
                        'mac_learning': 'enabled',
                        'mac_withdraw': 'enabled',
                        'mac_withdraw_for_access_pw': 'enabled',
                        'mac_withdraw_sent_on': 'bridge port up',
                        'mac_withdraw_relaying': 'disabled',
                        'flooding': {
                            'broadcast_multicast': 'enabled',
                            'unknown_unicast': 'enabled',
                        },
                        'mac_aging_time': 300,
                        'mac_aging_type': 'inactivity',
                        'mac_limit': 64000,
                        'mac_limit_action': 'none',
                        'mac_limit_notification': 'syslog',
                        'mac_limit_reached': 'no',
                        'mac_limit_threshold': '75%',
                        'mac_port_down_flush': 'enabled',
                        'mac_secure': 'disabled',
                        'mac_secure_logging': 'disabled',
                        'split_horizon_group': 'none',
                        'dynamic_arp_inspection': 'disabled',
                        'dynamic_arp_logging': 'disabled',
                        'ip_source_guard': 'disabled',
                        'ip_source_logging': 'disabled',
                        'dhcp_v4_snooping': 'disabled',
                        'dhcp_v4_snooping_profile': 'none',
                        'igmp_snooping': 'enabled',
                        'igmp_snooping_profile': 'CUW-WTQQ',
                        'mld_snooping_profile': 'none',
                        'storm_control': 'bridge-domain policer',
                        'bridge_mtu': '1500',
                        'mid_cvpls_config_index': '1',
                        'p2mp_pw': 'disabled',
                        'multicast_source': 'Not Set',
                        'create_time': '19/09/2019 10:23:31 (4w4d ago)',
                        'status_changed_since_creation': 'No',
                        'ac': {
                            'num_ac': 2,
                            'num_ac_up': 0,
                            'interfaces': {
                                'BVI100': {
                                    'state': 'down (Segment-down)',
                                    'type': 'Routed-Interface',
                                    'mtu': 1514,
                                    'xc_id': '0x80000007',
                                    'interworking': 'none',
                                    'error': 'Need at least 1 bridge port up',
                                    'bvi_mac_address': ['1000.10ff.1000'],
                                    'split_horizon_group': 'Access',
                                    'pd_system_data': {
                                        'af_lif_ipv4': '0x00000000',
                                        'af_lif_ipv6': '0x00000000',
                                    },
                                },
                                'Bundle-Ether11.100': {
                                    'state': 'down (Segment-down)',
                                    'type': 'VLAN',
                                    'vlan_num_ranges': '1',
                                    'rewrite_tags': '',
                                    'vlan_ranges': ['100', '100'],
                                    'mtu': 9202,
                                    'xc_id': '0xa0000008',
                                    'interworking': 'none',
                                    'mst_i': 5,
                                    'mac_learning': 'enabled',
                                    'flooding': {
                                        'broadcast_multicast': 'enabled',
                                        'unknown_unicast': 'enabled',
                                    },
                                    'mac_aging_time': 300,
                                    'mac_aging_type': 'inactivity',
                                    'mac_limit': 64000,
                                    'mac_limit_action': 'none',
                                    'mac_limit_notification': 'syslog',
                                    'mac_limit_reached': 'no',
                                    'mac_limit_threshold': '75%',
                                    'split_horizon_group': 'none',
                                    'dhcp_v4_snooping': 'disabled',
                                    'dhcp_v4_snooping_profile': 'none',
                                    'igmp_snooping': 'enabled',
                                    'igmp_snooping_profile': 'CUW-WTQQ',
                                    'mld_snooping_profile': 'none',
                                    'pd_system_data': {
                                        'af_lif_ipv4': '0x00013807',
                                        'af_lif_ipv6': '0x0001381d',
                                    },
                                },
                            },
                        },
                        'vfi': {
                            'num_vfi': 0,
                        },
                        'pw': {
                            'num_pw': 0,
                            'num_pw_up': 0,
                        },
                        'pbb': {
                            'num_pbb': 0,
                            'num_pbb_up': 0,
                        },
                        'vni': {
                            'num_vni': 0,
                            'num_vni_up': 0,
                        },
                        'evpn': {
                            'EVPN': {
                                'state': 'up',
                                'evi': '1000',
                                'xc_id': '0x80000004',
                                'statistics': {
                                    'packet_totals': {
                                        'receive': 0,
                                        'send': 0,
                                    },
                                    'byte_totals': {
                                        'receive': 0,
                                        'send': 0,
                                    },
                                    'mac_move': '0',
                                },
                            },
                        },
                    },
                },
            },
        },
    }

    golden_output6 = {'execute.return_value': '''
      show l2vpn bridge-domain detail

      Mon Oct 21 19:02:34.928 EDT
      Legend: pp = Partially Programmed.
      Bridge group: Genie-service, bridge-domain: genie100, id: 0, state: up, ShgId: 0, MSTi: 0
        Coupled state: disabled
        VINE state: BVI Resolved
        MAC learning: enabled
        MAC withdraw: enabled
          MAC withdraw for Access PW: enabled
          MAC withdraw sent on: bridge port up
          MAC withdraw relaying (access to access): disabled
        Flooding:
          Broadcast & Multicast: enabled
          Unknown unicast: enabled
        MAC aging time: 300 s, Type: inactivity
        MAC limit: 4000, Action: none, Notification: syslog
        MAC limit reached: no, threshold: 75%
        MAC port down flush: enabled
        MAC Secure: disabled, Logging: disabled
        Split Horizon Group: none
        Dynamic ARP Inspection: disabled, Logging: disabled
        IP Source Guard: disabled, Logging: disabled
        DHCPv4 Snooping: disabled
        DHCPv4 Snooping profile: none
        IGMP Snooping: disabled
        IGMP Snooping profile: none
        MLD Snooping profile: none
        Storm Control: disabled
        Bridge MTU: 1500
        MIB cvplsConfigIndex: 1
        Filter MAC addresses:
        P2MP PW: disabled
        Create time: 12/06/2019 11:46:11 (18w5d ago)
        No status change since creation
        ACs: 2 (2 up), VFIs: 1, PWs: 1 (1 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of ACs:
          AC: BVI100, state is up
            Type Routed-Interface
            MTU 1514; XC ID 0x800001ab; interworking none
            BVI MAC address:
              78ba.f9ff.106d
            Virtual MAC addresses:
              0000.5eff.0101
            Split Horizon Group: Access
          AC: GigabitEthernet0/4/0/1.100, state is up
            Type VLAN; Num Ranges: 1
            Rewrite Tags: []
            VLAN ranges: [100, 100]
            MTU 1500; XC ID 0x32001a8; interworking none
            MAC learning: enabled
            Flooding:
              Broadcast & Multicast: enabled
              Unknown unicast: enabled
            MAC aging time: 300 s, Type: inactivity
            MAC limit: 4000, Action: none, Notification: syslog
            MAC limit reached: no, threshold: 75%
            MAC port down flush: enabled
            MAC Secure: disabled, Logging: disabled
            Split Horizon Group: none
            Dynamic ARP Inspection: disabled, Logging: disabled
            IP Source Guard: disabled, Logging: disabled
            DHCPv4 Snooping: disabled
            DHCPv4 Snooping profile: none
            IGMP Snooping: disabled
            IGMP Snooping profile: none
            MLD Snooping profile: none
            Storm Control: bridge-domain policer
            Static MAC addresses:
            Statistics:
              packets: received 3894 (multicast 0, broadcast 29, unknown unicast 0, unicast 3865), sent 13809438
              bytes: received 291930 (multicast 0, broadcast 1740, unknown unicast 0, unicast 290190), sent 798698446
              MAC move: 0
            Storm control drop counters: 
              packets: broadcast 0, multicast 0, unknown unicast 0 
              bytes: broadcast 0, multicast 0, unknown unicast 0 
            Dynamic ARP inspection drop counters: 
              packets: 0, bytes: 0
            IP source guard drop counters: 
              packets: 0, bytes: 0
        List of Access PWs:
        List of VFIs:
          VFI vfi100 (up)
            PW: neighbor 10.229.11.11, PW ID 100100, state is up ( established )
              PW class link1, XC ID 0xa0000007
              Encapsulation MPLS, protocol LDP
              Source address 10.151.22.22
              PW type Ethernet, control word disabled, interworking none
              Sequencing not set

              PW Status TLV in use
                MPLS         Local                          Remote                        
                ------------ ------------------------------ -------------------------
                Label        100037                         100059                        
                Group ID     0x0                            0xed                          
                Interface    vfi100                         vfi100                        
                MTU          1500                           1500                          
                Control word disabled                       disabled                      
                PW type      Ethernet                       Ethernet                      
                VCCV CV type 0x2                            0x2                           
                            (LSP ping verification)        (LSP ping verification)       
                VCCV CC type 0x6                            0x6                           
                            (router alert label)           (router alert label)          
                            (TTL expiry)                   (TTL expiry)                  
                ------------ ------------------------------ -------------------------
              Incoming Status (PW Status TLV):
                Status code: 0x0 (Up) in Notification message
              MIB cpwVcIndex: 2684354567
              Create time: 12/06/2019 11:46:11 (18w5d ago)
              Last time status changed: 12/06/2019 12:08:57 (18w5d ago)
              MAC withdraw messages: sent 0, received 0
              Forward-class: 0
              Static MAC addresses:
              Statistics:
                packets: received 759749 (unicast 3068), sent 13054472
                bytes: received 48596976 (unicast 206670), sent 695167614
                MAC move: 0
              Storm control drop counters: 
                packets: broadcast 0, multicast 0, unknown unicast 0 
                bytes: broadcast 0, multicast 0, unknown unicast 0 
            DHCPv4 Snooping: disabled
            DHCPv4 Snooping profile: none
            IGMP Snooping: disabled
            IGMP Snooping profile: none
            MLD Snooping profile: none
            VFI Statistics:
              drops: illegal VLAN 0, illegal length 0
        List of Access VFIs:
    '''}

    golden_parsed_output6 = {
        'legend': 'pp = Partially Programmed.',
        'bridge_group': {
            'Genie-service': {
                'bridge_domain': {
                    'genie100': {
                        'state': 'up',
                        'id': 0,
                        'shg_id': 0,
                        'mst_i': 0,
                        'coupled_state': 'disabled',
                        'vine_state': 'BVI',
                        'mac_learning': 'enabled',
                        'mac_withdraw': 'enabled',
                        'mac_withdraw_for_access_pw': 'enabled',
                        'mac_withdraw_sent_on': 'bridge port up',
                        'mac_withdraw_relaying': 'disabled',
                        'flooding': {
                            'broadcast_multicast': 'enabled',
                            'unknown_unicast': 'enabled',
                        },
                        'mac_aging_time': 300,
                        'mac_aging_type': 'inactivity',
                        'mac_limit': 4000,
                        'mac_limit_action': 'none',
                        'mac_limit_notification': 'syslog',
                        'mac_limit_reached': 'no',
                        'mac_limit_threshold': '75%',
                        'mac_port_down_flush': 'enabled',
                        'mac_secure': 'disabled',
                        'mac_secure_logging': 'disabled',
                        'split_horizon_group': 'none',
                        'dynamic_arp_inspection': 'disabled',
                        'dynamic_arp_logging': 'disabled',
                        'ip_source_guard': 'disabled',
                        'ip_source_logging': 'disabled',
                        'dhcp_v4_snooping': 'disabled',
                        'dhcp_v4_snooping_profile': 'none',
                        'igmp_snooping': 'disabled',
                        'igmp_snooping_profile': 'none',
                        'mld_snooping_profile': 'none',
                        'storm_control': 'bridge-domain policer',
                        'bridge_mtu': '1500',
                        'mid_cvpls_config_index': '1',
                        'p2mp_pw': 'disabled',
                        'create_time': '12/06/2019 11:46:11 (18w5d ago)',
                        'status_changed_since_creation': 'No',
                        'ac': {
                            'num_ac': 2,
                            'num_ac_up': 2,
                            'interfaces': {
                                'BVI100': {
                                    'state': 'up',
                                    'type': 'Routed-Interface',
                                    'mtu': 1514,
                                    'xc_id': '0x800001ab',
                                    'interworking': 'none',
                                    'bvi_mac_address': ['78ba.f9ff.106d'],
                                    'virtual_mac_address': ['0000.5eff.0101'],
                                    'split_horizon_group': 'Access',
                                },
                                'GigabitEthernet0/4/0/1.100': {
                                    'state': 'up',
                                    'type': 'VLAN',
                                    'vlan_num_ranges': '1',
                                    'rewrite_tags': '',
                                    'vlan_ranges': ['100', '100'],
                                    'mtu': 1500,
                                    'xc_id': '0x32001a8',
                                    'interworking': 'none',
                                    'mac_learning': 'enabled',
                                    'flooding': {
                                        'broadcast_multicast': 'enabled',
                                        'unknown_unicast': 'enabled',
                                    },
                                    'mac_aging_time': 300,
                                    'mac_aging_type': 'inactivity',
                                    'mac_limit': 4000,
                                    'mac_limit_action': 'none',
                                    'mac_limit_notification': 'syslog',
                                    'mac_limit_reached': 'no',
                                    'mac_limit_threshold': '75%',
                                    'split_horizon_group': 'none',
                                    'dhcp_v4_snooping': 'disabled',
                                    'dhcp_v4_snooping_profile': 'none',
                                    'igmp_snooping': 'disabled',
                                    'igmp_snooping_profile': 'none',
                                    'mld_snooping_profile': 'none',
                                    'statistics': {
                                        'packet_totals': {
                                            'receive': 3894,
                                            'send': 13809438,
                                        },
                                        'byte_totals': {
                                            'receive': 291930,
                                            'send': 798698446,
                                        },
                                        'mac_move': '0',
                                    },
                                    'storm_control_drop_counters': {
                                        'packets': {
                                            'broadcast': '0',
                                            'multicast': '0',
                                            'unknown_unicast': '0',
                                        },
                                        'bytes': {
                                            'broadcast': '0',
                                            'multicast': '0',
                                            'unknown_unicast': '0',
                                        },
                                    },
                                    'dynamic_arp_inspection_drop_counters': {
                                        'packets': '0',
                                        'bytes': '0',
                                    },
                                    'ip_source_guard_drop_counters': {
                                        'packets': '0',
                                        'bytes': '0',
                                    },
                                },
                            },
                        },
                        'vfi': {
                            'num_vfi': 1,
                            'vfi100': {
                                'state': 'up',
                                'neighbor': {
                                    '10.229.11.11': {
                                        'pw_id': {
                                            '100100': {
                                                'state': 'up ( established )',
                                                'pw_class': 'link1',
                                                'xc_id': '0xa0000007',
                                                'encapsulation': 'MPLS',
                                                'protocol': 'LDP',
                                                'source_address': '10.151.22.22',
                                                'pw_type': 'Ethernet',
                                                'control_word': 'disabled',
                                                'interworking': 'none',
                                                'sequencing': 'not set',
                                                'mpls': {
                                                    'label': {
                                                        'local': '100037',
                                                        'remote': '100059',
                                                    },
                                                    'group_id': {
                                                        'local': '0x0',
                                                        'remote': '0xed',
                                                    },
                                                    'interface': {
                                                        'local': 'vfi100',
                                                        'remote': 'vfi100',
                                                    },
                                                    'mtu': {
                                                        'local': '1500',
                                                        'remote': '1500',
                                                    },
                                                    'control_word': {
                                                        'local': 'disabled',
                                                        'remote': 'disabled',
                                                    },
                                                    'pw_type': {
                                                        'local': 'Ethernet',
                                                        'remote': 'Ethernet',
                                                    },
                                                    'vccv_cv_type': {
                                                        'local': '0x2',
                                                        'remote': '0x2',
                                                        'local_type': ['LSP ping verification'],
                                                        'remote_type': ['LSP ping verification'],
                                                    },
                                                    'vccv_cc_type': {
                                                        'local': '0x6',
                                                        'remote': '0x6',
                                                        'local_type': ['router alert label', 'TTL expiry'],
                                                        'remote_type': ['router alert label', 'TTL expiry'],
                                                    },
                                                    'incoming_status_(pw': {
                                                        'local': 'Status',
                                                        'remote': 'TLV):',
                                                    },
                                                    'status_code:_0x0_(up)_in': {
                                                        'local': 'Notification',
                                                        'remote': 'message',
                                                    },
                                                    'mib': {
                                                        'local': 'cpwVcIndex:',
                                                        'remote': '2684354567',
                                                    },
                                                },
                                                'create_time': '12/06/2019 11:46:11 (18w5d ago)',
                                                'last_time_status_changed': '12/06/2019 12:08:57 (18w5d ago)',
                                                'mac_withdraw_message': {
                                                    'send': 0,
                                                    'receive': 0,
                                                },
                                                'forward_class': '0',
                                                'statistics': {
                                                    'packet_totals': {
                                                        'receive': 759749,
                                                        'send': 13054472,
                                                    },
                                                    'byte_totals': {
                                                        'receive': 48596976,
                                                        'send': 695167614,
                                                    },
                                                    'mac_move': '0',
                                                },
                                                'storm_control_drop_counters': {
                                                    'packets': {
                                                        'broadcast': '0',
                                                        'multicast': '0',
                                                        'unknown_unicast': '0',
                                                    },
                                                    'bytes': {
                                                        'broadcast': '0',
                                                        'multicast': '0',
                                                        'unknown_unicast': '0',
                                                    },
                                                },
                                                'dhcp_v4_snooping': 'disabled',
                                                'dhcp_v4_snooping_profile': 'none',
                                                'igmp_snooping': 'disabled',
                                                'igmp_snooping_profile': 'none',
                                                'mld_snooping_profile': 'none',
                                            },
                                        },
                                    },
                                },
                                'statistics': {
                                    'drop': {
                                        'illegal_vlan': 0,
                                        'illegal_length': 0,
                                    },
                                },
                            },
                        },
                        'pw': {
                            'num_pw': 1,
                            'num_pw_up': 1,
                        },
                        'pbb': {
                            'num_pbb': 0,
                            'num_pbb_up': 0,
                        },
                        'vni': {
                            'num_vni': 0,
                            'num_vni_up': 0,
                        },
                    },
                },
            },
        },
    }

    golden_parsed_output7 = {}

    golden_output7 = {'execute.return_value': '''
    +++ router with alias 'cli': executing command 'show l2vpn bridge-domain detail' +++
show l2vpn bridge-domain detail

Sun Jun 13 22:59:28.208 MSK
Legend: pp = Partially Programmed.
Bridge group: BS, bridge-domain: BS_1700, id: 385, state: up, ShgId: 0, MSTi: 0
  Coupled state: disabled
  VINE state: Default
  MAC learning: enabled
  MAC withdraw: enabled
    MAC withdraw for Access PW: enabled
    MAC withdraw sent on: bridge port up
    MAC withdraw relaying (access to access): disabled
  Flooding:
    Broadcast & Multicast: enabled
    Unknown unicast: enabled
  MAC aging time: 300 s, Type: inactivity
  MAC limit: 4000, Action: none, Notification: syslog
  MAC limit reached: no, threshold: 75%
  MAC port down flush: enabled
  MAC Secure: disabled, Logging: disabled
  Split Horizon Group: none
  Dynamic ARP Inspection: disabled, Logging: disabled
  IP Source Guard: disabled, Logging: disabled
  DHCPv4 Snooping: disabled
  DHCPv4 Snooping profile: none
  IGMP Snooping: disabled
  IGMP Snooping profile: none
  MLD Snooping profile: none
  Storm Control: disabled
  Bridge MTU: 1500
  MIB cvplsConfigIndex: 386
  Filter MAC addresses:
  Load Balance Hashing: src-dst-ip
  P2MP PW: disabled
  Create time: 08/12/2020 12:50:08 (26w5d ago)
  No status change since creation
  ACs: 2 (2 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
  List of ACs:
    AC: Bundle-Ether3.1700, state is up
      Type VLAN; Num Ranges: 1
      Rewrite Tags: []
      VLAN ranges: [1700, 1700]
      MTU 9000; XC ID 0xc0000548; interworking none
      MAC learning: enabled
      Flooding:
        Broadcast & Multicast: enabled
        Unknown unicast: enabled
      MAC aging time: 300 s, Type: inactivity
      MAC limit: 4000, Action: none, Notification: syslog
      MAC limit reached: no, threshold: 75%
      MAC port down flush: enabled
      MAC Secure: disabled, Logging: disabled
      Split Horizon Group: none
      Dynamic ARP Inspection: disabled, Logging: disabled
      IP Source Guard: disabled, Logging: disabled
      DHCPv4 Snooping: disabled
      DHCPv4 Snooping profile: none
      IGMP Snooping: disabled
      IGMP Snooping profile: none
      MLD Snooping profile: none
      Storm Control: bridge-domain policer
      Static MAC addresses:
      Statistics:
        packets: received 0 (multicast 0, broadcast 0, unknown unicast 0, unicast 0), sent 0
        bytes: received 0 (multicast 0, broadcast 0, unknown unicast 0, unicast 0), sent 0
        MAC move: 0
      Storm control drop counters:
        packets: broadcast 0, multicast 0, unknown unicast 0
        bytes: broadcast 0, multicast 0, unknown unicast 0
      Dynamic ARP inspection drop counters:
        packets: 0, bytes: 0
      IP source guard drop counters:
        packets: 0, bytes: 0
    AC: TenGigE0/2/0/14.1700, state is up
      Type VLAN; Num Ranges: 1
      Rewrite Tags: []
      VLAN ranges: [1700, 1700]
      MTU 1526; XC ID 0x1200556; interworking none
      MAC learning: enabled
      Flooding:
        Broadcast & Multicast: enabled
        Unknown unicast: enabled
      MAC aging time: 300 s, Type: inactivity
      MAC limit: 4000, Action: none, Notification: syslog
      MAC limit reached: no, threshold: 75%
      MAC port down flush: enabled
      MAC Secure: disabled, Logging: disabled
      Split Horizon Group: none
      Dynamic ARP Inspection: disabled, Logging: disabled
      IP Source Guard: disabled, Logging: disabled
      DHCPv4 Snooping: disabled
      DHCPv4 Snooping profile: none
      IGMP Snooping: disabled
      IGMP Snooping profile: none
      MLD Snooping profile: none
      Storm Control: bridge-domain policer
      Static MAC addresses:
      Statistics:
        packets: received 0 (multicast 0, broadcast 0, unknown unicast 0, unicast 0), sent 0
        bytes: received 0 (multicast 0, broadcast 0, unknown unicast 0, unicast 0), sent 0
        MAC move: 0
      Storm control drop counters:
        packets: broadcast 0, multicast 0, unknown unicast 0
        bytes: broadcast 0, multicast 0, unknown unicast 0
      Dynamic ARP inspection drop counters:
        packets: 0, bytes: 0
      IP source guard drop counters:
        packets: 0, bytes: 0
  List of Access PWs:
  List of VFIs:
  List of Access VFIs:
Bridge group: BS, bridge-domain: BS_2016, id: 406, state: up, ShgId: 0, MSTi: 0
  Coupled state: disabled
  VINE state: Default
  MAC learning: enabled
  MAC withdraw: enabled
    MAC withdraw for Access PW: enabled
    MAC withdraw sent on: bridge port up
    MAC withdraw relaying (access to access): disabled
  Flooding:
    Broadcast & Multicast: enabled
    Unknown unicast: enabled
  MAC aging time: 300 s, Type: inactivity
  MAC limit: 4000, Action: none, Notification: syslog
  MAC limit reached: no, threshold: 75%
  MAC port down flush: enabled
  MAC Secure: disabled, Logging: disabled
  Split Horizon Group: none
  Dynamic ARP Inspection: disabled, Logging: disabled
  IP Source Guard: disabled, Logging: disabled
  DHCPv4 Snooping: disabled
  DHCPv4 Snooping profile: none
  IGMP Snooping: disabled
  IGMP Snooping profile: none
  MLD Snooping profile: none
  Storm Control: disabled
  Bridge MTU: 1500
  MIB cvplsConfigIndex: 407
  Filter MAC addresses:
  Load Balance Hashing: src-dst-ip
  P2MP PW: disabled
  Create time: 20/05/2021 10:30:35 (3w3d ago)
  No status change since creation
  ACs: 2 (2 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
  List of ACs:
    AC: Bundle-Ether3.2016, state is up
      Type VLAN; Num Ranges: 1
      Rewrite Tags: []
      VLAN ranges: [2016, 2016]
      MTU 9000; XC ID 0xc00005a0; interworking none
      MAC learning: enabled
      Flooding:
        Broadcast & Multicast: enabled
        Unknown unicast: enabled
      MAC aging time: 300 s, Type: inactivity
      MAC limit: 4000, Action: none, Notification: syslog
      MAC limit reached: no, threshold: 75%
      MAC port down flush: enabled
      MAC Secure: disabled, Logging: disabled
      Split Horizon Group: none
      Dynamic ARP Inspection: disabled, Logging: disabled
      IP Source Guard: disabled, Logging: disabled
      DHCPv4 Snooping: disabled
      DHCPv4 Snooping profile: none
      IGMP Snooping: disabled
      IGMP Snooping profile: none
      MLD Snooping profile: none
      Storm Control: bridge-domain policer
      Static MAC addresses:
      Statistics:
        packets: received 0 (multicast 0, broadcast 0, unknown unicast 0, unicast 0), sent 0
        bytes: received 0 (multicast 0, broadcast 0, unknown unicast 0, unicast 0), sent 0
        MAC move: 0
      Storm control drop counters:
        packets: broadcast 0, multicast 0, unknown unicast 0
        bytes: broadcast 0, multicast 0, unknown unicast 0
      Dynamic ARP inspection drop counters:
        packets: 0, bytes: 0
      IP source guard drop counters:
        packets: 0, bytes: 0
    AC: TenGigE0/2/0/14.2016, state is up
      Type VLAN; Num Ranges: 1
      Rewrite Tags: []
      VLAN ranges: [2016, 2016]
      MTU 1526; XC ID 0x12005a4; interworking none
      MAC learning: enabled
      Flooding:
        Broadcast & Multicast: enabled
        Unknown unicast: enabled
      MAC aging time: 300 s, Type: inactivity
      MAC limit: 4000, Action: none, Notification: syslog
      MAC limit reached: no, threshold: 75%
      MAC port down flush: enabled
      MAC Secure: disabled, Logging: disabled
      Split Horizon Group: none
      Dynamic ARP Inspection: disabled, Logging: disabled
      IP Source Guard: disabled, Logging: disabled
      DHCPv4 Snooping: disabled
      DHCPv4 Snooping profile: none
      IGMP Snooping: disabled
      IGMP Snooping profile: none
      MLD Snooping profile: none
      Storm Control: bridge-domain policer
      Static MAC addresses:
      Statistics:
        packets: received 0 (multicast 0, broadcast 0, unknown unicast 0, unicast 0), sent 0
        bytes: received 0 (multicast 0, broadcast 0, unknown unicast 0, unicast 0), sent 0
        MAC move: 0
      Storm control drop counters:
        packets: broadcast 0, multicast 0, unknown unicast 0
        bytes: broadcast 0, multicast 0, unknown unicast 0
      Dynamic ARP inspection drop counters:
        packets: 0, bytes: 0
      IP source guard drop counters:
        packets: 0, bytes: 0
  List of Access PWs:
  List of VFIs:
  List of Access VFIs:
Bridge group: B2C, bridge-domain: SEG180, id: 138, state: up, ShgId: 0, MSTi: 0
  Coupled state: disabled
  VINE state: Default
  MAC learning: enabled
  MAC withdraw: enabled
    MAC withdraw for Access PW: enabled
    MAC withdraw sent on: bridge port up
    MAC withdraw relaying (access to access): disabled
  Flooding:
    Broadcast & Multicast: enabled
    Unknown unicast: enabled
  MAC aging time: 300 s, Type: inactivity
  MAC limit: 4000, Action: none, Notification: syslog, trap
  MAC limit reached: no, threshold: 75%
  MAC port down flush: enabled
  MAC Secure: disabled, Logging: disabled
  Split Horizon Group: none
  Dynamic ARP Inspection: disabled, Logging: disabled
  IP Source Guard: disabled, Logging: disabled
  DHCPv4 Snooping: disabled
  DHCPv4 Snooping profile: none
  IGMP Snooping: disabled
  IGMP Snooping profile: none
  MLD Snooping profile: none
  Storm Control: disabled
  Bridge MTU: 1500
  MIB cvplsConfigIndex: 139
  Filter MAC addresses:
  Load Balance Hashing: src-dst-ip
  P2MP PW: disabled
  Create time: 22/05/2020 03:04:51 (1y03w ago)
  No status change since creation
  ACs: 2 (2 up), VFIs: 1, PWs: 2 (1 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
  List of ACs:
    AC: Bundle-Ether10.180, state is up
      Type VLAN; Num Ranges: 1
      Outer Tag: 180
      Rewrite Tags: []
      VLAN ranges: [4096, 4096]
      MTU 9004; XC ID 0xc000019e; interworking none
      MAC learning: enabled
      Flooding:
        Broadcast & Multicast: enabled
        Unknown unicast: enabled
      MAC aging time: 300 s, Type: inactivity
      MAC limit: 4000, Action: none, Notification: syslog, trap
      MAC limit reached: no, threshold: 75%
      MAC port down flush: enabled
      MAC Secure: disabled, Logging: disabled
      Split Horizon Group: none
      Dynamic ARP Inspection: disabled, Logging: disabled
      IP Source Guard: disabled, Logging: disabled
      DHCPv4 Snooping: disabled
      DHCPv4 Snooping profile: none
      IGMP Snooping: disabled
      IGMP Snooping profile: none
      MLD Snooping profile: none
      Storm Control: bridge-domain policer
      Static MAC addresses:
      Statistics:
        packets: received 109 (multicast 0, broadcast 0, unknown unicast 0, unicast 109), sent 173009
        bytes: received 6976 (multicast 0, broadcast 0, unknown unicast 0, unicast 6976), sent 13241479
        MAC move: 0
      Storm control drop counters:
        packets: broadcast 0, multicast 0, unknown unicast 0
        bytes: broadcast 0, multicast 0, unknown unicast 0
      Dynamic ARP inspection drop counters:
        packets: 0, bytes: 0
      IP source guard drop counters:
        packets: 0, bytes: 0
    AC: Bundle-Ether101.180, state is up
      Type VLAN; Num Ranges: 1
      Outer Tag: 180
      Rewrite Tags: []
      VLAN ranges: [4096, 4096]
      MTU 9104; XC ID 0xc000063a; interworking none
      MAC learning: enabled
      Flooding:
        Broadcast & Multicast: enabled
        Unknown unicast: enabled
      MAC aging time: 300 s, Type: inactivity
      MAC limit: 4000, Action: none, Notification: syslog, trap
      MAC limit reached: no, threshold: 75%
      MAC port down flush: enabled
      MAC Secure: disabled, Logging: disabled
      Split Horizon Group: none
      Dynamic ARP Inspection: disabled, Logging: disabled
      IP Source Guard: disabled, Logging: disabled
      DHCPv4 Snooping: disabled
      DHCPv4 Snooping profile: none
      IGMP Snooping: disabled
      IGMP Snooping profile: none
      MLD Snooping profile: none
      Storm Control: bridge-domain policer
      Static MAC addresses:
      Statistics:
        packets: received 211212449 (multicast 0, broadcast 14929, unknown unicast 6, unicast 211197667), sent 106570486
        bytes: received 261086986801 (multicast 0, broadcast 1890891, unknown unicast 720, unicast 261085131250), sent 38098935003
        MAC move: 0
      Storm control drop counters:
        packets: broadcast 0, multicast 0, unknown unicast 0
        bytes: broadcast 0, multicast 0, unknown unicast 0
      Dynamic ARP inspection drop counters:
        packets: 0, bytes: 0
      IP source guard drop counters:
        packets: 0, bytes: 0
  List of Access PWs:
    PW: neighbor 10.11.44.8, PW ID 180, state is standby ( all ready )
      PW class PW_DEFAULT, XC ID 0xa0000131
      Encapsulation MPLS, protocol LDP
      Source address 10.11.44.91
      PW type Ethernet, control word enabled, interworking none
      PW backup disable delay 0 sec
      Sequencing not set
      LSP : Up
      Load Balance Hashing: src-dst-ip
      Flow Label flags configured (Tx=1,Rx=1), negotiated (Tx=0,Rx=0)

      PW Status TLV in use
        MPLS         Local                          Remote
        ------------ ------------------------------ ---------------------------
        Label        26303                          31
        Group ID     0x8a                           0x8
        Interface    Access PW                      [B2C]
        MTU          1500                           1500
        Control word enabled                        enabled
        PW type      Ethernet                       Ethernet
        VCCV CV type 0x2                            0x12
                     (LSP ping verification)        (LSP ping verification)
        VCCV CC type 0x7                            0x3
                     (control word)                 (control word)
                     (router alert label)           (router alert label)
                     (TTL expiry)
        ------------ ------------------------------ ---------------------------
      Incoming Status (PW Status TLV):
        Status code: 0x20 (Standby) in Notification message
      MIB cpwVcIndex: 2684354865
      Create time: 22/05/2020 03:04:51 (1y03w ago)
      Last time status changed: 10/06/2021 02:53:01 (3d20h ago)
      Last time PW went down: 10/06/2021 02:53:01 (3d20h ago)
      MAC withdraw messages: sent 0, received 22
      Forward-class: 0
      Static MAC addresses:
      MAC learning: enabled
      Flooding:
        Broadcast & Multicast: enabled
        Unknown unicast: enabled
      MAC aging time: 300 s, Type: inactivity
      MAC limit: 4000, Action: none, Notification: syslog, trap
      MAC limit reached: no, threshold: 75%
      MAC port down flush: enabled
      MAC Secure: disabled, Logging: disabled
      Split Horizon Group: none
      DHCPv4 Snooping: disabled
      DHCPv4 Snooping profile: none
      IGMP Snooping: disabled
      IGMP Snooping profile: none
      MLD Snooping profile: none
      Storm Control: bridge-domain policer
  List of VFIs:
    VFI SEG180 (up)
      PW: neighbor 10.11.44.92, PW ID 99180, state is up ( established )
        PW class PW_DEFAULT, XC ID 0xa0000133
        Encapsulation MPLS, protocol LDP
        Source address 10.11.44.91
        PW type Ethernet, control word enabled, interworking none
        Sequencing not set
        LSP : Up
        Load Balance Hashing: src-dst-ip
        Flow Label flags configured (Tx=1,Rx=1), negotiated (Tx=1,Rx=1)

        PW Status TLV in use
          MPLS         Local                          Remote
          ------------ ------------------------------ -------------------------
          Label        26304                          24276
          Group ID     0x8a                           0xa5
          Interface    SEG180                         SEG180
          MTU          1500                           1500
          Control word enabled                        enabled
          PW type      Ethernet                       Ethernet
          VCCV CV type 0x2                            0x2
                       (LSP ping verification)        (LSP ping verification)
          VCCV CC type 0x7                            0x7
                       (control word)                 (control word)
                       (router alert label)           (router alert label)
                       (TTL expiry)                   (TTL expiry)
          ------------ ------------------------------ -------------------------
        Incoming Status (PW Status TLV):
          Status code: 0x0 (Up) in Notification message
        MIB cpwVcIndex: 2684354867
        Create time: 22/05/2020 03:04:51 (1y03w ago)
        Last time status changed: 10/06/2021 02:53:01 (3d20h ago)
        Last time PW went down: 10/06/2021 02:44:34 (3d20h ago)
        MAC withdraw messages: sent 47, received 38
        Forward-class: 0
        Static MAC addresses:
        Statistics:
          packets: received 106567054 (unicast 106408978), sent 211212390
          bytes: received 38096946147 (unicast 38085596046), sent 261086280143
          MAC move: 0
        Storm control drop counters:
          packets: broadcast 0, multicast 0, unknown unicast 0
          bytes: broadcast 0, multicast 0, unknown unicast 0
      DHCPv4 Snooping: disabled
      DHCPv4 Snooping profile: none
      IGMP Snooping: disabled
      IGMP Snooping profile: none
      MLD Snooping profile: none
      VFI Statistics:
        drops: illegal VLAN 0, illegal length 0
  List of Access VFIs:
Bridge group: B2C, bridge-domain: SEG242, id: 252, state: up, ShgId: 0, MSTi: 0
  Coupled state: disabled
  VINE state: Default
  MAC learning: enabled
  MAC withdraw: enabled
    MAC withdraw for Access PW: enabled
    MAC withdraw sent on: bridge port up
    MAC withdraw relaying (access to access): disabled
  Flooding:
    Broadcast & Multicast: enabled
    Unknown unicast: enabled
  MAC aging time: 300 s, Type: inactivity
  MAC limit: 4000, Action: none, Notification: syslog, trap
  MAC limit reached: no, threshold: 75%
  MAC port down flush: enabled
  MAC Secure: disabled, Logging: disabled
  Split Horizon Group: none
  Dynamic ARP Inspection: disabled, Logging: disabled
  IP Source Guard: disabled, Logging: disabled
  DHCPv4 Snooping: disabled
  DHCPv4 Snooping profile: none
  IGMP Snooping: disabled
  IGMP Snooping profile: none
  MLD Snooping profile: none
  Storm Control: disabled
  Bridge MTU: 1600
  MIB cvplsConfigIndex: 253
  Filter MAC addresses:
  Load Balance Hashing: src-dst-ip
  P2MP PW: disabled
  Create time: 06/08/2020 03:00:38 (44w3d ago)
  No status change since creation
  ACs: 2 (2 up), VFIs: 1, PWs: 2 (1 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
  List of ACs:
    AC: Bundle-Ether10.242, state is up
      Type VLAN; Num Ranges: 1
      Outer Tag: 242
      Rewrite Tags: []
      VLAN ranges: [4096, 4096]
      MTU 9004; XC ID 0xc0000308; interworking none
      MAC learning: enabled
      Flooding:
        Broadcast & Multicast: enabled
        Unknown unicast: enabled
      MAC aging time: 300 s, Type: inactivity
      MAC limit: 4000, Action: none, Notification: syslog, trap
      MAC limit reached: no, threshold: 75%
      MAC port down flush: enabled
      MAC Secure: disabled, Logging: disabled
      Split Horizon Group: none
      Dynamic ARP Inspection: disabled, Logging: disabled
      IP Source Guard: disabled, Logging: disabled
      DHCPv4 Snooping: disabled
      DHCPv4 Snooping profile: none
      IGMP Snooping: disabled
      IGMP Snooping profile: none
      MLD Snooping profile: none
      Storm Control: bridge-domain policer
      Static MAC addresses:
      Statistics:
        packets: received 0 (multicast 0, broadcast 0, unknown unicast 0, unicast 0), sent 123583
        bytes: received 0 (multicast 0, broadcast 0, unknown unicast 0, unicast 0), sent 8618629
        MAC move: 0
      Storm control drop counters:
        packets: broadcast 0, multicast 0, unknown unicast 0
        bytes: broadcast 0, multicast 0, unknown unicast 0
      Dynamic ARP inspection drop counters:
        packets: 0, bytes: 0
      IP source guard drop counters:
        packets: 0, bytes: 0
    AC: Bundle-Ether101.242, state is up
      Type VLAN; Num Ranges: 1
      Outer Tag: 242
      Rewrite Tags: []
      VLAN ranges: [4096, 4096]
      MTU 9104; XC ID 0xc00006b0; interworking none
      MAC learning: enabled
      Flooding:
        Broadcast & Multicast: enabled
        Unknown unicast: enabled
      MAC aging time: 300 s, Type: inactivity
      MAC limit: 4000, Action: none, Notification: syslog, trap
      MAC limit reached: no, threshold: 75%
      MAC port down flush: enabled
      MAC Secure: disabled, Logging: disabled
      Split Horizon Group: none
      Dynamic ARP Inspection: disabled, Logging: disabled
      IP Source Guard: disabled, Logging: disabled
      DHCPv4 Snooping: disabled
      DHCPv4 Snooping profile: none
      IGMP Snooping: disabled
      IGMP Snooping profile: none
      MLD Snooping profile: none
      Storm Control: bridge-domain policer
      Static MAC addresses:
      Statistics:
        packets: received 316478673 (multicast 0, broadcast 6886, unknown unicast 2, unicast 316471917), sent 154259031
        bytes: received 455595024880 (multicast 0, broadcast 680129, unknown unicast 433, unicast 455594448929), sent 16267549475
        MAC move: 0
      Storm control drop counters:
        packets: broadcast 0, multicast 0, unknown unicast 0
        bytes: broadcast 0, multicast 0, unknown unicast 0
      Dynamic ARP inspection drop counters:
        packets: 0, bytes: 0
      IP source guard drop counters:
        packets: 0, bytes: 0
  List of Access PWs:
    PW: neighbor 10.11.44.12, PW ID 242, state is standby ( all ready )
      PW class PW_DEFAULT, XC ID 0xa0000229
      Encapsulation MPLS, protocol LDP
      Source address 10.11.44.91
      PW type Ethernet, control word enabled, interworking none
      PW backup disable delay 0 sec
      Sequencing not set
      LSP : Up
      Load Balance Hashing: src-dst-ip
      Flow Label flags configured (Tx=1,Rx=1), negotiated (Tx=0,Rx=0)

      PW Status TLV in use
        MPLS         Local                          Remote
        ------------ ------------------------------ ---------------------------
        Label        26468                          65
        Group ID     0xfc                           0x16
        Interface    Access PW                      [B2C]
        MTU          1600                           1600
        Control word enabled                        enabled
        PW type      Ethernet                       Ethernet
        VCCV CV type 0x2                            0x12
                     (LSP ping verification)        (LSP ping verification)
        VCCV CC type 0x7                            0x3
                     (control word)                 (control word)
                     (router alert label)           (router alert label)
                     (TTL expiry)
        ------------ ------------------------------ ---------------------------
      Incoming Status (PW Status TLV):
        Status code: 0x20 (Standby) in Notification message
      MIB cpwVcIndex: 2684355113
      Create time: 06/08/2020 03:00:38 (44w3d ago)
      Last time status changed: 10/06/2021 02:53:01 (3d20h ago)
      Last time PW went down: 10/06/2021 02:53:01 (3d20h ago)
      MAC withdraw messages: sent 0, received 23
      Forward-class: 0
      Static MAC addresses:
      MAC learning: enabled
      Flooding:
        Broadcast & Multicast: enabled
        Unknown unicast: enabled
      MAC aging time: 300 s, Type: inactivity
      MAC limit: 4000, Action: none, Notification: syslog, trap
      MAC limit reached: no, threshold: 75%
      MAC port down flush: enabled
      MAC Secure: disabled, Logging: disabled
      Split Horizon Group: none
      DHCPv4 Snooping: disabled
      DHCPv4 Snooping profile: none
      IGMP Snooping: disabled
      IGMP Snooping profile: none
      MLD Snooping profile: none
      Storm Control: bridge-domain policer
  List of VFIs:
    VFI SEG242 (up)
      PW: neighbor 10.11.44.92, PW ID 99242, state is up ( established )
        PW class PW_DEFAULT, XC ID 0xa000022b
        Encapsulation MPLS, protocol LDP
        Source address 10.11.44.91
        PW type Ethernet, control word enabled, interworking none
        Sequencing not set
        LSP : Up
        Load Balance Hashing: src-dst-ip
        Flow Label flags configured (Tx=1,Rx=1), negotiated (Tx=1,Rx=1)

        PW Status TLV in use
          MPLS         Local                          Remote
          ------------ ------------------------------ -------------------------
          Label        26469                          24341
          Group ID     0xfc                           0xe0
          Interface    SEG242                         SEG242
          MTU          1600                           1600
          Control word enabled                        enabled
          PW type      Ethernet                       Ethernet
          VCCV CV type 0x2                            0x2
                       (LSP ping verification)        (LSP ping verification)
          VCCV CC type 0x7                            0x7
                       (control word)                 (control word)
                       (router alert label)           (router alert label)
                       (TTL expiry)                   (TTL expiry)
          ------------ ------------------------------ -------------------------
        Incoming Status (PW Status TLV):
          Status code: 0x0 (Up) in Notification message
        MIB cpwVcIndex: 2684355115
        Create time: 06/08/2020 03:00:38 (44w3d ago)
        Last time status changed: 10/06/2021 02:53:01 (3d20h ago)
        Last time PW went down: 10/06/2021 02:44:34 (3d20h ago)
        MAC withdraw messages: sent 39, received 49
        Forward-class: 0
        Static MAC addresses:
        Statistics:
          packets: received 154264643 (unicast 154147945), sent 316478076
          bytes: received 16268069399 (unicast 16260131128), sent 455594105126
          MAC move: 0
        Storm control drop counters:
          packets: broadcast 0, multicast 0, unknown unicast 0
          bytes: broadcast 0, multicast 0, unknown unicast 0
      DHCPv4 Snooping: disabled
      DHCPv4 Snooping profile: none
      IGMP Snooping: disabled
      IGMP Snooping profile: none
      MLD Snooping profile: none
      VFI Statistics:
        drops: illegal VLAN 0, illegal length 0
  List of Access VFIs:
Bridge group: B2C, bridge-domain: SEG244, id: 253, state: up, ShgId: 0, MSTi: 0
  Coupled state: disabled
  VINE state: Default
  MAC learning: enabled
  MAC withdraw: enabled
    MAC withdraw for Access PW: enabled
    MAC withdraw sent on: bridge port up
    MAC withdraw relaying (access to access): disabled
  Flooding:
    Broadcast & Multicast: enabled
    Unknown unicast: enabled
  MAC aging time: 300 s, Type: inactivity
  MAC limit: 4000, Action: none, Notification: syslog, trap
  MAC limit reached: no, threshold: 75%
  MAC port down flush: enabled
  MAC Secure: disabled, Logging: disabled
  Split Horizon Group: none
  Dynamic ARP Inspection: disabled, Logging: disabled
  IP Source Guard: disabled, Logging: disabled
  DHCPv4 Snooping: disabled
  DHCPv4 Snooping profile: none
  IGMP Snooping: disabled
  IGMP Snooping profile: none
  MLD Snooping profile: none
  Storm Control: disabled
  Bridge MTU: 1600
  MIB cvplsConfigIndex: 254
  Filter MAC addresses:
  Load Balance Hashing: src-dst-ip
  P2MP PW: disabled
  Create time: 06/08/2020 03:00:38 (44w3d ago)
  No status change since creation
  ACs: 2 (2 up), VFIs: 1, PWs: 2 (1 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
  List of ACs:
    AC: Bundle-Ether10.244, state is up
      Type VLAN; Num Ranges: 1
      Outer Tag: 244
      Rewrite Tags: []
      VLAN ranges: [4096, 4096]
      MTU 9004; XC ID 0xc000030a; interworking none
      MAC learning: enabled
      Flooding:
        Broadcast & Multicast: enabled
        Unknown unicast: enabled
      MAC aging time: 300 s, Type: inactivity
      MAC limit: 4000, Action: none, Notification: syslog, trap
      MAC limit reached: no, threshold: 75%
      MAC port down flush: enabled
      MAC Secure: disabled, Logging: disabled
      Split Horizon Group: none
      Dynamic ARP Inspection: disabled, Logging: disabled
      IP Source Guard: disabled, Logging: disabled
      DHCPv4 Snooping: disabled
      DHCPv4 Snooping profile: none
      IGMP Snooping: disabled
      IGMP Snooping profile: none
      MLD Snooping profile: none
      Storm Control: bridge-domain policer
      Static MAC addresses:
      Statistics:
        packets: received 168583 (multicast 0, broadcast 0, unknown unicast 0, unicast 168583), sent 4000182
        bytes: received 10789312 (multicast 0, broadcast 0, unknown unicast 0, unicast 10789312), sent 507734366
        MAC move: 0
      Storm control drop counters:
        packets: broadcast 0, multicast 0, unknown unicast 0
        bytes: broadcast 0, multicast 0, unknown unicast 0
      Dynamic ARP inspection drop counters:
        packets: 0, bytes: 0
      IP source guard drop counters:
        packets: 0, bytes: 0
    AC: Bundle-Ether101.244, state is up
      Type VLAN; Num Ranges: 1
      Outer Tag: 244
      Rewrite Tags: []
      VLAN ranges: [4096, 4096]
      MTU 9104; XC ID 0xc00006b2; interworking none
      MAC learning: enabled
      Flooding:
        Broadcast & Multicast: enabled
        Unknown unicast: enabled
      MAC aging time: 300 s, Type: inactivity
      MAC limit: 4000, Action: none, Notification: syslog, trap
      MAC limit reached: no, threshold: 75%
      MAC port down flush: enabled
      MAC Secure: disabled, Logging: disabled
      Split Horizon Group: none
      Dynamic ARP Inspection: disabled, Logging: disabled
      IP Source Guard: disabled, Logging: disabled
      DHCPv4 Snooping: disabled
      DHCPv4 Snooping profile: none
      IGMP Snooping: disabled
      IGMP Snooping profile: none
      MLD Snooping profile: none
      Storm Control: bridge-domain policer
      Static MAC addresses:
      Statistics:
        packets: received 171074 (multicast 0, broadcast 0, unknown unicast 0, unicast 171075), sent 3705157
        bytes: received 10948736 (multicast 0, broadcast 0, unknown unicast 0, unicast 10948800), sent 469726393
        MAC move: 0
      Storm control drop counters:
        packets: broadcast 0, multicast 0, unknown unicast 0
        bytes: broadcast 0, multicast 0, unknown unicast 0
      Dynamic ARP inspection drop counters:
        packets: 0, bytes: 0
      IP source guard drop counters:
        packets: 0, bytes: 0
  List of Access PWs:
    PW: neighbor 10.11.44.12, PW ID 244, state is standby ( all ready )
      PW class PW_DEFAULT, XC ID 0xa000022d
      Encapsulation MPLS, protocol LDP
      Source address 10.11.44.91
      PW type Ethernet, control word enabled, interworking none
      PW backup disable delay 0 sec
      Sequencing not set
      LSP : Up
      Load Balance Hashing: src-dst-ip
      Flow Label flags configured (Tx=1,Rx=1), negotiated (Tx=0,Rx=0)

      PW Status TLV in use
        MPLS         Local                          Remote
        ------------ ------------------------------ ---------------------------
        Label        26470                          177
        Group ID     0xfd                           0x18
        Interface    Access PW                      [B2C]
        MTU          1600                           1600
        Control word enabled                        enabled
        PW type      Ethernet                       Ethernet
        VCCV CV type 0x2                            0x12
                     (LSP ping verification)        (LSP ping verification)
        VCCV CC type 0x7                            0x3
                     (control word)                 (control word)
                     (router alert label)           (router alert label)
                     (TTL expiry)
        ------------ ------------------------------ ---------------------------
      Incoming Status (PW Status TLV):
        Status code: 0x20 (Standby) in Notification message
      MIB cpwVcIndex: 2684355117
      Create time: 06/08/2020 03:00:38 (44w3d ago)
      Last time status changed: 10/06/2021 10:46:08 (3d12h ago)
      Last time PW went down: 05/09/2020 21:19:41 (40w1d ago)
      MAC withdraw messages: sent 1, received 1
      Forward-class: 0
      Static MAC addresses:
      MAC learning: enabled
      Flooding:
        Broadcast & Multicast: enabled
        Unknown unicast: enabled
      MAC aging time: 300 s, Type: inactivity
      MAC limit: 4000, Action: none, Notification: syslog, trap
      MAC limit reached: no, threshold: 75%
      MAC port down flush: enabled
      MAC Secure: disabled, Logging: disabled
      Split Horizon Group: none
      DHCPv4 Snooping: disabled
      DHCPv4 Snooping profile: none
      IGMP Snooping: disabled
      IGMP Snooping profile: none
      MLD Snooping profile: none
      Storm Control: bridge-domain policer
  List of VFIs:
    VFI SEG244 (up)
      PW: neighbor 10.11.44.92, PW ID 99244, state is up ( established )
        PW class PW_DEFAULT, XC ID 0xa000022f
        Encapsulation MPLS, protocol LDP
        Source address 10.11.44.91
        PW type Ethernet, control word enabled, interworking none
        Sequencing not set
        LSP : Up
        Load Balance Hashing: src-dst-ip
        Flow Label flags configured (Tx=1,Rx=1), negotiated (Tx=1,Rx=1)

        PW Status TLV in use
          MPLS         Local                          Remote
          ------------ ------------------------------ -------------------------
          Label        26471                          24343
          Group ID     0xfd                           0xe2
          Interface    SEG244                         SEG244
          MTU          1600                           1600
          Control word enabled                        enabled
          PW type      Ethernet                       Ethernet
          VCCV CV type 0x2                            0x2
                       (LSP ping verification)        (LSP ping verification)
          VCCV CC type 0x7                            0x7
                       (control word)                 (control word)
                       (router alert label)           (router alert label)
                       (TTL expiry)                   (TTL expiry)
          ------------ ------------------------------ -------------------------
        Incoming Status (PW Status TLV):
          Status code: 0x0 (Up) in Notification message
        MIB cpwVcIndex: 2684355119
        Create time: 06/08/2020 03:00:38 (44w3d ago)
        Last time status changed: 10/06/2021 10:37:03 (3d12h ago)
        MAC withdraw messages: sent 0, received 3
        Forward-class: 0
        Static MAC addresses:
        Statistics:
          packets: received 4193762 (unicast 193586), sent 339660
          bytes: received 768650456 (unicast 260916024), sent 21738240
          MAC move: 0
        Storm control drop counters:
          packets: broadcast 0, multicast 0, unknown unicast 0
          bytes: broadcast 0, multicast 0, unknown unicast 0
      DHCPv4 Snooping: disabled
      DHCPv4 Snooping profile: none
      IGMP Snooping: disabled
      IGMP Snooping profile: none
      MLD Snooping profile: none
      VFI Statistics:
        drops: illegal VLAN 0, illegal length 0
  List of Access VFIs:
Bridge group: LAB, bridge-domain: 9001, id: 0, state: up, ShgId: 0, MSTi: 0
  Coupled state: disabled
  VINE state: Default
  MAC learning: enabled
  MAC withdraw: enabled
    MAC withdraw for Access PW: enabled
    MAC withdraw sent on: bridge port up
    MAC withdraw relaying (access to access): disabled
  Flooding:
    Broadcast & Multicast: enabled
    Unknown unicast: enabled
  MAC aging time: 300 s, Type: inactivity
  MAC limit: 4000, Action: none, Notification: syslog
  MAC limit reached: no, threshold: 75%
  MAC port down flush: enabled
  MAC Secure: disabled, Logging: disabled
  Split Horizon Group: none
  Dynamic ARP Inspection: disabled, Logging: disabled
  IP Source Guard: disabled, Logging: disabled
  DHCPv4 Snooping: disabled
  DHCPv4 Snooping profile: none
  IGMP Snooping: disabled
  IGMP Snooping profile: none
  MLD Snooping profile: none
  Storm Control: disabled
  Bridge MTU: 1500
  MIB cvplsConfigIndex: 1
  Filter MAC addresses:
  Load Balance Hashing: src-dst-ip
  P2MP PW: disabled
  Create time: 01/10/2019 14:18:18 (1y36w ago)
  No status change since creation
  ACs: 1 (1 up), VFIs: 1, PWs: 3 (1 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
  List of ACs:
    AC: Bundle-Ether10.3999, state is up
      Type VLAN; Num Ranges: 1
      Outer Tag: 3999
      Rewrite Tags: []
      VLAN ranges: [1101, 1101]
      MTU 9004; XC ID 0xc0000002; interworking none
      MAC learning: enabled
      Flooding:
        Broadcast & Multicast: enabled
        Unknown unicast: enabled
      MAC aging time: 300 s, Type: inactivity
      MAC limit: 4000, Action: none, Notification: syslog
      MAC limit reached: no, threshold: 75%
      MAC port down flush: enabled
      MAC Secure: disabled, Logging: disabled
      Split Horizon Group: none
      Dynamic ARP Inspection: disabled, Logging: disabled
      IP Source Guard: disabled, Logging: disabled
      DHCPv4 Snooping: disabled
      DHCPv4 Snooping profile: none
      IGMP Snooping: disabled
      IGMP Snooping profile: none
      MLD Snooping profile: none
      Storm Control: bridge-domain policer
      Static MAC addresses:
      Statistics:
        packets: received 0 (multicast 0, broadcast 0, unknown unicast 0, unicast 0), sent 0
        bytes: received 0 (multicast 0, broadcast 0, unknown unicast 0, unicast 0), sent 0
        MAC move: 0
      Storm control drop counters:
        packets: broadcast 0, multicast 0, unknown unicast 0
        bytes: broadcast 0, multicast 0, unknown unicast 0
      Dynamic ARP inspection drop counters:
        packets: 0, bytes: 0
      IP source guard drop counters:
        packets: 0, bytes: 0
  List of Access PWs:
    PW: neighbor 10.11.44.81, PW ID 9001, state is down ( local ready ) (Transport LSP Down)
      PW class PW_DEFAULT, XC ID 0xa0000003
      Encapsulation MPLS, protocol LDP
      Source address 10.11.44.91
      PW type Ethernet, control word enabled, interworking none
      PW backup disable delay 0 sec
      Sequencing not set
      LSP : Down
      Load Balance Hashing: src-dst-ip
      Flow Label flags configured (Tx=1,Rx=1), negotiated (Tx=0,Rx=0)

      PW Status TLV in use
        MPLS         Local                          Remote
        ------------ ------------------------------ ---------------------------
        Label        24000                          unknown
        Group ID     0x0                            0x0
        Interface    Access PW                      unknown
        MTU          1500                           unknown
        Control word enabled                        unknown
        PW type      Ethernet                       unknown
        VCCV CV type 0x2                            0x0
                                                    (none)
                     (LSP ping verification)
        VCCV CC type 0x7                            0x0
                                                    (none)
                     (control word)
                     (router alert label)
                     (TTL expiry)
        ------------ ------------------------------ ---------------------------
      MIB cpwVcIndex: 2684354563
      Create time: 01/10/2019 14:18:18 (1y36w ago)
      Last time status changed: 21/10/2020 13:24:35 (33w4d ago)
      Last time PW went down: 21/10/2020 13:18:37 (33w4d ago)
      MAC withdraw messages: sent 13, received 0
      Forward-class: 0
      Static MAC addresses:
      MAC learning: enabled
      Flooding:
        Broadcast & Multicast: enabled
        Unknown unicast: enabled
      MAC aging time: 300 s, Type: inactivity
      MAC limit: 4000, Action: none, Notification: syslog
      MAC limit reached: no, threshold: 75%
      MAC port down flush: enabled
      MAC Secure: disabled, Logging: disabled
      Split Horizon Group: none
      DHCPv4 Snooping: disabled
      DHCPv4 Snooping profile: none
      IGMP Snooping: disabled
      IGMP Snooping profile: none
      MLD Snooping profile: none
      Storm Control: bridge-domain policer
    PW: neighbor 10.11.44.82, PW ID 9001, state is down ( local ready ) (Transport LSP Down)
      PW class not set, XC ID 0xa0000005
      Encapsulation MPLS, protocol LDP
      Source address 10.11.44.91
      PW type Ethernet, control word disabled, interworking none
      PW backup disable delay 0 sec
      Sequencing not set
      LSP : Down
      Load Balance Hashing: src-dst-ip

      PW Status TLV in use
        MPLS         Local                          Remote
        ------------ ------------------------------ ---------------------------
        Label        24001                          unknown
        Group ID     0x0                            0x0
        Interface    Access PW                      unknown
        MTU          1500                           unknown
        Control word disabled                       unknown
        PW type      Ethernet                       unknown
        VCCV CV type 0x2                            0x0
                                                    (none)
                     (LSP ping verification)
        VCCV CC type 0x6                            0x0
                                                    (none)
                     (router alert label)
                     (TTL expiry)
        ------------ ------------------------------ ---------------------------
      MIB cpwVcIndex: 2684354565
      Create time: 01/10/2019 14:18:18 (1y36w ago)
      Last time status changed: 10/06/2020 01:53:52 (1y00w ago)
      Last time PW went down: 10/06/2020 01:50:32 (1y00w ago)
      MAC withdraw messages: sent 0, received 0
      Forward-class: 0
      Static MAC addresses:
      MAC learning: enabled
      Flooding:
        Broadcast & Multicast: enabled
        Unknown unicast: enabled
      MAC aging time: 300 s, Type: inactivity
      MAC limit: 4000, Action: none, Notification: syslog
      MAC limit reached: no, threshold: 75%
      MAC port down flush: enabled
      MAC Secure: disabled, Logging: disabled
      Split Horizon Group: none
      DHCPv4 Snooping: disabled
      DHCPv4 Snooping profile: none
      IGMP Snooping: disabled
      IGMP Snooping profile: none
      MLD Snooping profile: none
      Storm Control: bridge-domain policer
  List of VFIs:
    VFI Seg101 (up)
      PW: neighbor 10.11.44.92, PW ID 5000, state is up ( established )
        PW class PW_DEFAULT, XC ID 0xa0000009
        Encapsulation MPLS, protocol LDP
        Source address 10.11.44.91
        PW type Ethernet, control word enabled, interworking none
        Sequencing not set
        LSP : Up
        Load Balance Hashing: src-dst-ip
        Flow Label flags configured (Tx=1,Rx=1), negotiated (Tx=1,Rx=1)

        PW Status TLV in use
          MPLS         Local                          Remote
          ------------ ------------------------------ -------------------------
          Label        25636                          24201
          Group ID     0x0                            0x11c
          Interface    Seg101                         Seg101
          MTU          1500                           1500
          Control word enabled                        enabled
          PW type      Ethernet                       Ethernet
          VCCV CV type 0x2                            0x2
                       (LSP ping verification)        (LSP ping verification)
          VCCV CC type 0x7                            0x7
                       (control word)                 (control word)
                       (router alert label)           (router alert label)
                       (TTL expiry)                   (TTL expiry)
          ------------ ------------------------------ -------------------------
        Incoming Status (PW Status TLV):
          Status code: 0x0 (Up) in Notification message
        MIB cpwVcIndex: 2684354569
        Create time: 22/11/2019 11:48:50 (1y29w ago)
        Last time status changed: 10/06/2021 02:53:01 (3d20h ago)
        Last time PW went down: 10/06/2021 02:44:34 (3d20h ago)
        MAC withdraw messages: sent 16, received 14
        Forward-class: 0
        Static MAC addresses:
        Statistics:
          packets: received 0 (unicast 0), sent 0
          bytes: received 0 (unicast 0), sent 0
          MAC move: 0
        Storm control drop counters:
          packets: broadcast 0, multicast 0, unknown unicast 0
          bytes: broadcast 0, multicast 0, unknown unicast 0
      DHCPv4 Snooping: disabled
      DHCPv4 Snooping profile: none
      IGMP Snooping: disabled
      IGMP Snooping profile: none
      MLD Snooping profile: none
      VFI Statistics:
        drops: illegal VLAN 0, illegal length 0
  List of Access VFIs:
Bridge group: B1-B, bridge-domain: B1-B, id: 1, state: up, ShgId: 0, MSTi: 0
  Coupled state: disabled
  VINE state: Default
  MAC learning: enabled
  MAC withdraw: enabled
    MAC withdraw for Access PW: enabled
    MAC withdraw sent on: bridge port up
    MAC withdraw relaying (access to access): disabled
  Flooding:
    Broadcast & Multicast: enabled
    Unknown unicast: enabled
  MAC aging time: 300 s, Type: inactivity
  MAC limit: 4000, Action: none, Notification: syslog
  MAC limit reached: no, threshold: 75%
  MAC port down flush: enabled
  MAC Secure: disabled, Logging: disabled
  Split Horizon Group: none
  Dynamic ARP Inspection: disabled, Logging: disabled
  IP Source Guard: disabled, Logging: disabled
  DHCPv4 Snooping: disabled
  DHCPv4 Snooping profile: none
  IGMP Snooping: disabled
  IGMP Snooping profile: none
  MLD Snooping profile: none
  Storm Control: disabled
  Bridge MTU: 1500
  MIB cvplsConfigIndex: 2
  Filter MAC addresses:
  Load Balance Hashing: src-dst-ip
  P2MP PW: disabled
  Create time: 15/11/2019 03:52:31 (1y30w ago)
  No status change since creation
  ACs: 1 (1 up), VFIs: 1, PWs: 1 (1 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
  List of ACs:
    AC: Bundle-Ether10.4000, state is up
      Type VLAN; Num Ranges: 1
      Rewrite Tags: []
      VLAN ranges: [4000, 4000]
      MTU 9000; XC ID 0xc000000e; interworking none
      MAC learning: enabled
      Flooding:
        Broadcast & Multicast: enabled
        Unknown unicast: enabled
      MAC aging time: 300 s, Type: inactivity
      MAC limit: 4000, Action: none, Notification: syslog
      MAC limit reached: no, threshold: 75%
      MAC port down flush: enabled
      MAC Secure: disabled, Logging: disabled
      Split Horizon Group: none
      Dynamic ARP Inspection: disabled, Logging: disabled
      IP Source Guard: disabled, Logging: disabled
      DHCPv4 Snooping: disabled
      DHCPv4 Snooping profile: none
      IGMP Snooping: disabled
      IGMP Snooping profile: none
      MLD Snooping profile: none
      Storm Control: bridge-domain policer
      Static MAC addresses:
      Statistics:
        packets: received 2263727831 (multicast 0, broadcast 0, unknown unicast 0, unicast 2263729426), sent 2601947451
        bytes: received 1695425622592 (multicast 0, broadcast 0, unknown unicast 0, unicast 1695426199797), sent 2615912696704
        MAC move: 0
      Storm control drop counters:
        packets: broadcast 0, multicast 0, unknown unicast 0
        bytes: broadcast 0, multicast 0, unknown unicast 0
      Dynamic ARP inspection drop counters:
        packets: 0, bytes: 0
      IP source guard drop counters:
        packets: 0, bytes: 0
  List of Access PWs:
  List of VFIs:
    VFI B1-B (up)
      PW: neighbor 10.11.44.92, PW ID 104001, state is up ( established )
        PW class not set, XC ID 0xa0000007
        Encapsulation MPLS, protocol LDP
        Source address 10.11.44.91
        PW type Ethernet, control word disabled, interworking none
        Sequencing not set
        LSP : Up
        Load Balance Hashing: src-dst-ip

        PW Status TLV in use
          MPLS         Local                          Remote
          ------------ ------------------------------ -------------------------
          Label        24748                          24344
          Group ID     0x1                            0x118
          Interface    B1-B                           B1-B
          MTU          1500                           1500
          Control word disabled                       disabled
          PW type      Ethernet                       Ethernet
          VCCV CV type 0x2                            0x2
                       (LSP ping verification)        (LSP ping verification)
          VCCV CC type 0x6                            0x6
                       (router alert label)           (router alert label)
                       (TTL expiry)                   (TTL expiry)
          ------------ ------------------------------ -------------------------
        Incoming Status (PW Status TLV):
          Status code: 0x0 (Up) in Notification message
        MIB cpwVcIndex: 2684354567
        Create time: 15/11/2019 03:52:31 (1y30w ago)
        Last time status changed: 10/06/2021 02:53:01 (3d20h ago)
        Last time PW went down: 10/06/2021 02:44:34 (3d20h ago)
        MAC withdraw messages: sent 13, received 0
        Forward-class: 0
        Static MAC addresses:
        Statistics:
          packets: received 2601882205 (unicast 2601882205), sent 2263733637
          bytes: received 2605419757847 (unicast 2605419757847), sent 1695428286863
          MAC move: 0
        Storm control drop counters:
          packets: broadcast 0, multicast 0, unknown unicast 0
          bytes: broadcast 0, multicast 0, unknown unicast 0
      DHCPv4 Snooping: disabled
      DHCPv4 Snooping profile: none
      IGMP Snooping: disabled
      IGMP Snooping profile: none
      MLD Snooping profile: none
      VFI Statistics:
        drops: illegal VLAN 0, illegal length 0
  List of Access VFIs:
Bridge group: Management, bridge-domain: 4010, id: 263, state: up, ShgId: 0, MSTi: 0
  Coupled state: disabled
  VINE state: Default
  MAC learning: enabled
  MAC withdraw: enabled
    MAC withdraw for Access PW: enabled
    MAC withdraw sent on: bridge port up
    MAC withdraw relaying (access to access): disabled
  Flooding:
    Broadcast & Multicast: enabled
    Unknown unicast: enabled
  MAC aging time: 300 s, Type: inactivity
  MAC limit: 4000, Action: none, Notification: syslog
  MAC limit reached: no, threshold: 75%
  MAC port down flush: enabled
  MAC Secure: disabled, Logging: disabled
  Split Horizon Group: none
  Dynamic ARP Inspection: disabled, Logging: disabled
  IP Source Guard: disabled, Logging: disabled
  DHCPv4 Snooping: disabled
  DHCPv4 Snooping profile: none
  IGMP Snooping: disabled
  IGMP Snooping profile: none
  MLD Snooping profile: none
  Storm Control: disabled
  Bridge MTU: 1500
  MIB cvplsConfigIndex: 264
  Filter MAC addresses:
  Load Balance Hashing: src-dst-ip
  P2MP PW: disabled
  Create time: 24/09/2020 03:22:47 (37w3d ago)
  No status change since creation
  ACs: 2 (2 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
  List of ACs:
    AC: Bundle-Ether20.4010, state is up
      Type VLAN; Num Ranges: 1
      Rewrite Tags: []
      VLAN ranges: [4010, 4010]
      MTU 1500; XC ID 0xc000042a; interworking none
      MAC learning: enabled
      Flooding:
        Broadcast & Multicast: enabled
        Unknown unicast: enabled
      MAC aging time: 300 s, Type: inactivity
      MAC limit: 4000, Action: none, Notification: syslog
      MAC limit reached: no, threshold: 75%
      MAC port down flush: enabled
      MAC Secure: disabled, Logging: disabled
      Split Horizon Group: none
      Dynamic ARP Inspection: disabled, Logging: disabled
      IP Source Guard: disabled, Logging: disabled
      DHCPv4 Snooping: disabled
      DHCPv4 Snooping profile: none
      IGMP Snooping: disabled
      IGMP Snooping profile: none
      MLD Snooping profile: none
      Storm Control: bridge-domain policer
      Static MAC addresses:
      Statistics:
        packets: received 868 (multicast 0, broadcast 859, unknown unicast 0, unicast 9), sent 1017603
        bytes: received 55552 (multicast 0, broadcast 54976, unknown unicast 0, unicast 576), sent 61874928
        MAC move: 0
      Storm control drop counters:
        packets: broadcast 0, multicast 0, unknown unicast 0
        bytes: broadcast 0, multicast 0, unknown unicast 0
      Dynamic ARP inspection drop counters:
        packets: 0, bytes: 0
      IP source guard drop counters:
        packets: 0, bytes: 0
    AC: Bundle-Ether3.4010, state is up
      Type VLAN; Num Ranges: 1
      Rewrite Tags: []
      VLAN ranges: [4010, 4010]
      MTU 9000; XC ID 0xc000033c; interworking none
      MAC learning: enabled
      Flooding:
        Broadcast & Multicast: enabled
        Unknown unicast: enabled
      MAC aging time: 300 s, Type: inactivity
      MAC limit: 4000, Action: none, Notification: syslog
      MAC limit reached: no, threshold: 75%
      MAC port down flush: enabled
      MAC Secure: disabled, Logging: disabled
      Split Horizon Group: none
      Dynamic ARP Inspection: disabled, Logging: disabled
      IP Source Guard: disabled, Logging: disabled
      DHCPv4 Snooping: disabled
      DHCPv4 Snooping profile: none
      IGMP Snooping: disabled
      IGMP Snooping profile: none
      MLD Snooping profile: none
      Storm Control: bridge-domain policer
      Static MAC addresses:
      Statistics:
        packets: received 1017608 (multicast 0, broadcast 1017599, unknown unicast 7, unicast 2), sent 868
        bytes: received 61875220 (multicast 0, broadcast 61874680, unknown unicast 420, unicast 120), sent 55552
        MAC move: 0
      Storm control drop counters:
        packets: broadcast 0, multicast 0, unknown unicast 0
        bytes: broadcast 0, multicast 0, unknown unicast 0
      Dynamic ARP inspection drop counters:
        packets: 0, bytes: 0
      IP source guard drop counters:
        packets: 0, bytes: 0
  List of Access PWs:
  List of VFIs:
  List of Access VFIs:
Bridge group: Management, bridge-domain: 4090, id: 264, state: up, ShgId: 0, MSTi: 0
  Coupled state: disabled
  VINE state: Default
  MAC learning: enabled
  MAC withdraw: enabled
    MAC withdraw for Access PW: enabled
    MAC withdraw sent on: bridge port up
    MAC withdraw relaying (access to access): disabled
  Flooding:
    Broadcast & Multicast: enabled
    Unknown unicast: enabled
  MAC aging time: 300 s, Type: inactivity
  MAC limit: 4000, Action: none, Notification: syslog
  MAC limit reached: no, threshold: 75%
  MAC port down flush: enabled
  MAC Secure: disabled, Logging: disabled
  Split Horizon Group: none
  Dynamic ARP Inspection: disabled, Logging: disabled
  IP Source Guard: disabled, Logging: disabled
  DHCPv4 Snooping: disabled
  DHCPv4 Snooping profile: none
  IGMP Snooping: disabled
  IGMP Snooping profile: none
  MLD Snooping profile: none
  Storm Control: disabled
  Bridge MTU: 1500
  MIB cvplsConfigIndex: 265
  Filter MAC addresses:
  Load Balance Hashing: src-dst-ip
  P2MP PW: disabled
  Create time: 24/09/2020 03:22:47 (37w3d ago)
  No status change since creation
  ACs: 2 (2 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
  List of ACs:
    AC: Bundle-Ether20.4090, state is up
      Type VLAN; Num Ranges: 1
      Rewrite Tags: []
      VLAN ranges: [4090, 4090]
      MTU 1500; XC ID 0xc000042c; interworking none
      MAC learning: enabled
      Flooding:
        Broadcast & Multicast: enabled
        Unknown unicast: enabled
      MAC aging time: 300 s, Type: inactivity
      MAC limit: 4000, Action: none, Notification: syslog
      MAC limit reached: no, threshold: 75%
      MAC port down flush: enabled
      MAC Secure: disabled, Logging: disabled
      Split Horizon Group: none
      Dynamic ARP Inspection: disabled, Logging: disabled
      IP Source Guard: disabled, Logging: disabled
      DHCPv4 Snooping: disabled
      DHCPv4 Snooping profile: none
      IGMP Snooping: disabled
      IGMP Snooping profile: none
      MLD Snooping profile: none
      Storm Control: bridge-domain policer
      Static MAC addresses:
      Statistics:
        packets: received 35510779266 (multicast 0, broadcast 0, unknown unicast 0, unicast 35510779266), sent 67290609967
        bytes: received 14204488780501 (multicast 0, broadcast 0, unknown unicast 0, unicast 14204488780501), sent 83879978440066
        MAC move: 0
      Storm control drop counters:
        packets: broadcast 0, multicast 0, unknown unicast 0
        bytes: broadcast 0, multicast 0, unknown unicast 0
      Dynamic ARP inspection drop counters:
        packets: 0, bytes: 0
      IP source guard drop counters:
        packets: 0, bytes: 0
    AC: Bundle-Ether3.4090, state is up
      Type VLAN; Num Ranges: 1
      Rewrite Tags: []
      VLAN ranges: [4090, 4090]
      MTU 9000; XC ID 0xc000033e; interworking none
      MAC learning: enabled
      Flooding:
        Broadcast & Multicast: enabled
        Unknown unicast: enabled
      MAC aging time: 300 s, Type: inactivity
      MAC limit: 4000, Action: none, Notification: syslog
      MAC limit reached: no, threshold: 75%
      MAC port down flush: enabled
      MAC Secure: disabled, Logging: disabled
      Split Horizon Group: none
      Dynamic ARP Inspection: disabled, Logging: disabled
      IP Source Guard: disabled, Logging: disabled
      DHCPv4 Snooping: disabled
      DHCPv4 Snooping profile: none
      IGMP Snooping: disabled
      IGMP Snooping profile: none
      MLD Snooping profile: none
      Storm Control: bridge-domain policer
      Static MAC addresses:
      Statistics:
        packets: received 67289104995 (multicast 0, broadcast 0, unknown unicast 0, unicast 67289104995), sent 35510093704
        bytes: received 83878025586583 (multicast 0, broadcast 0, unknown unicast 0, unicast 83878025586583), sent 14204351236525
        MAC move: 0
      Storm control drop counters:
        packets: broadcast 0, multicast 0, unknown unicast 0
        bytes: broadcast 0, multicast 0, unknown unicast 0
      Dynamic ARP inspection drop counters:
        packets: 0, bytes: 0
      IP source guard drop counters:
        packets: 0, bytes: 0
  List of Access PWs:
  List of VFIs:
  List of Access VFIs:
Bridge group: Subscriber, bridge-domain: Elf_1124, id: 396, state: up, ShgId: 0, MSTi: 0
  Coupled state: disabled
  VINE state: Default
  MAC learning: enabled
  MAC withdraw: enabled
    MAC withdraw for Access PW: enabled
    MAC withdraw sent on: bridge port up
    MAC withdraw relaying (access to access): disabled
  Flooding:
    Broadcast & Multicast: enabled
    Unknown unicast: enabled
  MAC aging time: 300 s, Type: inactivity
  MAC limit: 4000, Action: none, Notification: syslog
  MAC limit reached: no, threshold: 75%
  MAC port down flush: enabled
  MAC Secure: disabled, Logging: disabled
  Split Horizon Group: none
  Dynamic ARP Inspection: disabled, Logging: disabled
  IP Source Guard: disabled, Logging: disabled
  DHCPv4 Snooping: disabled
  DHCPv4 Snooping profile: none
  IGMP Snooping: disabled
  IGMP Snooping profile: none
  MLD Snooping profile: none
  Storm Control: disabled
  Bridge MTU: 1500
  MIB cvplsConfigIndex: 397
  Filter MAC addresses:
  Load Balance Hashing: src-dst-ip
  P2MP PW: disabled
  Create time: 20/04/2021 11:22:55 (7w5d ago)
  No status change since creation
  ACs: 2 (2 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
  List of ACs:
    AC: Bundle-Ether20.20011124, state is up
      Type VLAN; Num Ranges: 1
      Outer Tag: 2001
      Rewrite Tags: []
      VLAN ranges: [1124, 1124]
      MTU 1500; XC ID 0xc000058c; interworking none
      MAC learning: enabled
      Flooding:
        Broadcast & Multicast: enabled
        Unknown unicast: enabled
      MAC aging time: 300 s, Type: inactivity
      MAC limit: 4000, Action: none, Notification: syslog
      MAC limit reached: no, threshold: 75%
      MAC port down flush: enabled
      MAC Secure: disabled, Logging: disabled
      Split Horizon Group: none
      Dynamic ARP Inspection: disabled, Logging: disabled
      IP Source Guard: disabled, Logging: disabled
      DHCPv4 Snooping: disabled
      DHCPv4 Snooping profile: none
      IGMP Snooping: disabled
      IGMP Snooping profile: none
      MLD Snooping profile: none
      Storm Control: bridge-domain policer
      Static MAC addresses:
      Statistics:
        packets: received 398255446 (multicast 0, broadcast 0, unknown unicast 0, unicast 398255446), sent 166337423
        bytes: received 539316094013 (multicast 0, broadcast 0, unknown unicast 0, unicast 539316094013), sent 36890820969
        MAC move: 0
      Storm control drop counters:
        packets: broadcast 0, multicast 0, unknown unicast 0
        bytes: broadcast 0, multicast 0, unknown unicast 0
      Dynamic ARP inspection drop counters:
        packets: 0, bytes: 0
      IP source guard drop counters:
        packets: 0, bytes: 0
    AC: Bundle-Ether3.20011124, state is up
      Type VLAN; Num Ranges: 1
      Outer Tag: 2001
      Rewrite Tags: []
      VLAN ranges: [1124, 1124]
      MTU 9000; XC ID 0xc0000570; interworking none
      MAC learning: enabled
      Flooding:
        Broadcast & Multicast: enabled
        Unknown unicast: enabled
      MAC aging time: 300 s, Type: inactivity
      MAC limit: 4000, Action: none, Notification: syslog
      MAC limit reached: no, threshold: 75%
      MAC port down flush: enabled
      MAC Secure: disabled, Logging: disabled
      Split Horizon Group: none
      Dynamic ARP Inspection: disabled, Logging: disabled
      IP Source Guard: disabled, Logging: disabled
      DHCPv4 Snooping: disabled
      DHCPv4 Snooping profile: none
      IGMP Snooping: disabled
      IGMP Snooping profile: none
      MLD Snooping profile: none
      Storm Control: bridge-domain policer
      Static MAC addresses:
      Statistics:
        packets: received 166337150 (multicast 0, broadcast 1051, unknown unicast 0, unicast 166336099), sent 398251507
        bytes: received 36890796499 (multicast 0, broadcast 71468, unknown unicast 0, unicast 36890725031), sent 539311615942
        MAC move: 0
      Storm control drop counters:
        packets: broadcast 0, multicast 0, unknown unicast 0
        bytes: broadcast 0, multicast 0, unknown unicast 0
      Dynamic ARP inspection drop counters:
        packets: 0, bytes: 0
      IP source guard drop counters:
        packets: 0, bytes: 0
  List of Access PWs:
  List of VFIs:
  List of Access VFIs:
Bridge group: Subscriber, bridge-domain: Recom_2213, id: 371, state: up, ShgId: 0, MSTi: 0
  Coupled state: disabled
  VINE state: Default
  MAC learning: enabled
  MAC withdraw: enabled
    MAC withdraw for Access PW: enabled
    MAC withdraw sent on: bridge port up
    MAC withdraw relaying (access to access): disabled
  Flooding:
    Broadcast & Multicast: enabled
    Unknown unicast: enabled
  MAC aging time: 300 s, Type: inactivity
  MAC limit: 4000, Action: none, Notification: syslog
  MAC limit reached: no, threshold: 75%
  MAC port down flush: enabled
  MAC Secure: disabled, Logging: disabled
  Split Horizon Group: none
  Dynamic ARP Inspection: disabled, Logging: disabled
  IP Source Guard: disabled, Logging: disabled
  DHCPv4 Snooping: disabled
  DHCPv4 Snooping profile: none
  IGMP Snooping: disabled
  IGMP Snooping profile: none
  MLD Snooping profile: none
  Storm Control: disabled
  Bridge MTU: 1500
  MIB cvplsConfigIndex: 372
  Filter MAC addresses:
  Load Balance Hashing: src-dst-ip
  P2MP PW: disabled
  Create time: 24/09/2020 03:22:47 (37w3d ago)
  No status change since creation
  ACs: 2 (2 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
  List of ACs:
    AC: Bundle-Ether20.21002213, state is up
      Type VLAN; Num Ranges: 1
      Outer Tag: 2100
      Rewrite Tags: []
      VLAN ranges: [2213, 2213]
      MTU 1500; XC ID 0xc00004fe; interworking none
      MAC learning: enabled
      Flooding:
        Broadcast & Multicast: enabled
        Unknown unicast: enabled
      MAC aging time: 300 s, Type: inactivity
      MAC limit: 4000, Action: none, Notification: syslog
      MAC limit reached: no, threshold: 75%
      MAC port down flush: enabled
      MAC Secure: disabled, Logging: disabled
      Split Horizon Group: none
      Dynamic ARP Inspection: disabled, Logging: disabled
      IP Source Guard: disabled, Logging: disabled
      DHCPv4 Snooping: disabled
      DHCPv4 Snooping profile: none
      IGMP Snooping: disabled
      IGMP Snooping profile: none
      MLD Snooping profile: none
      Storm Control: bridge-domain policer
      Static MAC addresses:
      Statistics:
        packets: received 0 (multicast 0, broadcast 0, unknown unicast 0, unicast 0), sent 0
        bytes: received 0 (multicast 0, broadcast 0, unknown unicast 0, unicast 0), sent 0
        MAC move: 0
      Storm control drop counters:
        packets: broadcast 0, multicast 0, unknown unicast 0
        bytes: broadcast 0, multicast 0, unknown unicast 0
      Dynamic ARP inspection drop counters:
        packets: 0, bytes: 0
      IP source guard drop counters:
        packets: 0, bytes: 0
    AC: Bundle-Ether3.21002213, state is up
      Type VLAN; Num Ranges: 1
      Outer Tag: 2100
      Rewrite Tags: []
      VLAN ranges: [2213, 2213]
      MTU 9000; XC ID 0xc0000410; interworking none
      MAC learning: enabled
      Flooding:
        Broadcast & Multicast: enabled
        Unknown unicast: enabled
      MAC aging time: 300 s, Type: inactivity
      MAC limit: 4000, Action: none, Notification: syslog
      MAC limit reached: no, threshold: 75%
      MAC port down flush: enabled
      MAC Secure: disabled, Logging: disabled
      Split Horizon Group: none
      Dynamic ARP Inspection: disabled, Logging: disabled
      IP Source Guard: disabled, Logging: disabled
      DHCPv4 Snooping: disabled
      DHCPv4 Snooping profile: none
      IGMP Snooping: disabled
      IGMP Snooping profile: none
      MLD Snooping profile: none
      Storm Control: bridge-domain policer
      Static MAC addresses:
      Statistics:
        packets: received 0 (multicast 0, broadcast 0, unknown unicast 0, unicast 0), sent 0
        bytes: received 0 (multicast 0, broadcast 0, unknown unicast 0, unicast 0), sent 0
        MAC move: 0
      Storm control drop counters:
        packets: broadcast 0, multicast 0, unknown unicast 0
        bytes: broadcast 0, multicast 0, unknown unicast 0
      Dynamic ARP inspection drop counters:
        packets: 0, bytes: 0
      IP source guard drop counters:
        packets: 0, bytes: 0
  List of Access PWs:
  List of VFIs:
  List of Access VFIs:
Bridge group: Subscriber, bridge-domain: Recom_2215, id: 373, state: up, ShgId: 0, MSTi: 0
  Coupled state: disabled
  VINE state: Default
  MAC learning: enabled
  MAC withdraw: enabled
    MAC withdraw for Access PW: enabled
    MAC withdraw sent on: bridge port up
    MAC withdraw relaying (access to access): disabled
  Flooding:
    Broadcast & Multicast: enabled
    Unknown unicast: enabled
  MAC aging time: 300 s, Type: inactivity
  MAC limit: 4000, Action: none, Notification: syslog
  MAC limit reached: no, threshold: 75%
  MAC port down flush: enabled
  MAC Secure: disabled, Logging: disabled
  Split Horizon Group: none
  Dynamic ARP Inspection: disabled, Logging: disabled
  IP Source Guard: disabled, Logging: disabled
  DHCPv4 Snooping: disabled
  DHCPv4 Snooping profile: none
  IGMP Snooping: disabled
  IGMP Snooping profile: none
  MLD Snooping profile: none
  Storm Control: disabled
  Bridge MTU: 1500
  MIB cvplsConfigIndex: 374
  Filter MAC addresses:
  Load Balance Hashing: src-dst-ip
  P2MP PW: disabled
  Create time: 24/09/2020 03:22:47 (37w3d ago)
  No status change since creation
  ACs: 2 (2 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
  List of ACs:
    AC: Bundle-Ether20.21002215, state is up
      Type VLAN; Num Ranges: 1
      Outer Tag: 2100
      Rewrite Tags: []
      VLAN ranges: [2215, 2215]
      MTU 1500; XC ID 0xc0000502; interworking none
      MAC learning: enabled
      Flooding:
        Broadcast & Multicast: enabled
        Unknown unicast: enabled
      MAC aging time: 300 s, Type: inactivity
      MAC limit: 4000, Action: none, Notification: syslog
      MAC limit reached: no, threshold: 75%
      MAC port down flush: enabled
      MAC Secure: disabled, Logging: disabled
      Split Horizon Group: none
      Dynamic ARP Inspection: disabled, Logging: disabled
      IP Source Guard: disabled, Logging: disabled
      DHCPv4 Snooping: disabled
      DHCPv4 Snooping profile: none
      IGMP Snooping: disabled
      IGMP Snooping profile: none
      MLD Snooping profile: none
      Storm Control: bridge-domain policer
      Static MAC addresses:
      Statistics:
        packets: received 0 (multicast 0, broadcast 0, unknown unicast 0, unicast 0), sent 0
        bytes: received 0 (multicast 0, broadcast 0, unknown unicast 0, unicast 0), sent 0
        MAC move: 0
      Storm control drop counters:
        packets: broadcast 0, multicast 0, unknown unicast 0
        bytes: broadcast 0, multicast 0, unknown unicast 0
      Dynamic ARP inspection drop counters:
        packets: 0, bytes: 0
      IP source guard drop counters:
        packets: 0, bytes: 0
    AC: Bundle-Ether3.21002215, state is up
      Type VLAN; Num Ranges: 1
      Outer Tag: 2100
      Rewrite Tags: []
      VLAN ranges: [2215, 2215]
      MTU 9000; XC ID 0xc0000414; interworking none
      MAC learning: enabled
      Flooding:
        Broadcast & Multicast: enabled
        Unknown unicast: enabled
      MAC aging time: 300 s, Type: inactivity
      MAC limit: 4000, Action: none, Notification: syslog
      MAC limit reached: no, threshold: 75%
      MAC port down flush: enabled
      MAC Secure: disabled, Logging: disabled
      Split Horizon Group: none
      Dynamic ARP Inspection: disabled, Logging: disabled
      IP Source Guard: disabled, Logging: disabled
      DHCPv4 Snooping: disabled
      DHCPv4 Snooping profile: none
      IGMP Snooping: disabled
      IGMP Snooping profile: none
      MLD Snooping profile: none
      Storm Control: bridge-domain policer
      Static MAC addresses:
      Statistics:
        packets: received 0 (multicast 0, broadcast 0, unknown unicast 0, unicast 0), sent 0
        bytes: received 0 (multicast 0, broadcast 0, unknown unicast 0, unicast 0), sent 0
        MAC move: 0
      Storm control drop counters:
        packets: broadcast 0, multicast 0, unknown unicast 0
        bytes: broadcast 0, multicast 0, unknown unicast 0
      Dynamic ARP inspection drop counters:
        packets: 0, bytes: 0
      IP source guard drop counters:
        packets: 0, bytes: 0
  List of Access PWs:
  List of VFIs:
  List of Access VFIs:
Bridge group: Subscriber, bridge-domain: Recom_2217, id: 376, state: up, ShgId: 0, MSTi: 0
  Coupled state: disabled
  VINE state: Default
  MAC learning: enabled
  MAC withdraw: enabled
    MAC withdraw for Access PW: enabled
    MAC withdraw sent on: bridge port up
    MAC withdraw relaying (access to access): disabled
  Flooding:
    Broadcast & Multicast: enabled
    Unknown unicast: enabled
  MAC aging time: 300 s, Type: inactivity
  MAC limit: 4000, Action: none, Notification: syslog
  MAC limit reached: no, threshold: 75%
  MAC port down flush: enabled
  MAC Secure: disabled, Logging: disabled
  Split Horizon Group: none
  Dynamic ARP Inspection: disabled, Logging: disabled
  IP Source Guard: disabled, Logging: disabled
  DHCPv4 Snooping: disabled
  DHCPv4 Snooping profile: none
  IGMP Snooping: disabled
  IGMP Snooping profile: none
  MLD Snooping profile: none
  Storm Control: disabled
  Bridge MTU: 1500
  MIB cvplsConfigIndex: 377
  Filter MAC addresses:
  Load Balance Hashing: src-dst-ip
  P2MP PW: disabled
  Create time: 25/09/2020 09:43:41 (37w2d ago)
  No status change since creation
  ACs: 2 (2 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
  List of ACs:
    AC: Bundle-Ether20.21002217, state is up
      Type VLAN; Num Ranges: 1
      Outer Tag: 2100
      Rewrite Tags: []
      VLAN ranges: [2217, 2217]
      MTU 1500; XC ID 0xc0000508; interworking none
      MAC learning: enabled
      Flooding:
        Broadcast & Multicast: enabled
        Unknown unicast: enabled
      MAC aging time: 300 s, Type: inactivity
      MAC limit: 4000, Action: none, Notification: syslog
      MAC limit reached: no, threshold: 75%
      MAC port down flush: enabled
      MAC Secure: disabled, Logging: disabled
      Split Horizon Group: none
      Dynamic ARP Inspection: disabled, Logging: disabled
      IP Source Guard: disabled, Logging: disabled
      DHCPv4 Snooping: disabled
      DHCPv4 Snooping profile: none
      IGMP Snooping: disabled
      IGMP Snooping profile: none
      MLD Snooping profile: none
      Storm Control: bridge-domain policer
      Static MAC addresses:
      Statistics:
        packets: received 1857545 (multicast 0, broadcast 0, unknown unicast 0, unicast 1857545), sent 1284464
        bytes: received 1984810970 (multicast 0, broadcast 0, unknown unicast 0, unicast 1984810970), sent 281697660
        MAC move: 0
      Storm control drop counters:
        packets: broadcast 0, multicast 0, unknown unicast 0
        bytes: broadcast 0, multicast 0, unknown unicast 0
      Dynamic ARP inspection drop counters:
        packets: 0, bytes: 0
      IP source guard drop counters:
        packets: 0, bytes: 0
    AC: Bundle-Ether3.2217, state is up
      Type VLAN; Num Ranges: 1
      Rewrite Tags: []
      VLAN ranges: [2217, 2217]
      MTU 9000; XC ID 0xc0000506; interworking none
      MAC learning: enabled
      Flooding:
        Broadcast & Multicast: enabled
        Unknown unicast: enabled
      MAC aging time: 300 s, Type: inactivity
      MAC limit: 4000, Action: none, Notification: syslog
      MAC limit reached: no, threshold: 75%
      MAC port down flush: enabled
      MAC Secure: disabled, Logging: disabled
      Split Horizon Group: none
      Dynamic ARP Inspection: disabled, Logging: disabled
      IP Source Guard: disabled, Logging: disabled
      DHCPv4 Snooping: disabled
      DHCPv4 Snooping profile: none
      IGMP Snooping: disabled
      IGMP Snooping profile: none
      MLD Snooping profile: none
      Storm Control: bridge-domain policer
      Static MAC addresses:
      Statistics:
        packets: received 1284475 (multicast 0, broadcast 1, unknown unicast 0, unicast 1284474), sent 1857554
        bytes: received 276560922 (multicast 0, broadcast 64, unknown unicast 0, unicast 276560858), sent 1977382049
        MAC move: 0
      Storm control drop counters:
        packets: broadcast 0, multicast 0, unknown unicast 0
        bytes: broadcast 0, multicast 0, unknown unicast 0
      Dynamic ARP inspection drop counters:
        packets: 0, bytes: 0
      IP source guard drop counters:
        packets: 0, bytes: 0
  List of Access PWs:
  List of VFIs:
  List of Access VFIs:
Bridge group: Subscriber_MTS, bridge-domain: 1266, id: 256, state: up, ShgId: 0, MSTi: 0
  Coupled state: disabled
  VINE state: Default
  MAC learning: enabled
  MAC withdraw: enabled
    MAC withdraw for Access PW: enabled
    MAC withdraw sent on: bridge port up
    MAC withdraw relaying (access to access): disabled
  Flooding:
    Broadcast & Multicast: enabled
    Unknown unicast: enabled
  MAC aging time: 300 s, Type: inactivity
  MAC limit: 4000, Action: none, Notification: syslog
  MAC limit reached: no, threshold: 75%
  MAC port down flush: enabled
  MAC Secure: disabled, Logging: disabled
  Split Horizon Group: none
  Dynamic ARP Inspection: disabled, Logging: disabled
  IP Source Guard: disabled, Logging: disabled
  DHCPv4 Snooping: disabled
  DHCPv4 Snooping profile: none
  IGMP Snooping: disabled
  IGMP Snooping profile: none
  MLD Snooping profile: none
  Storm Control: disabled
  Bridge MTU: 1500
  MIB cvplsConfigIndex: 257
  Filter MAC addresses:
  Load Balance Hashing: src-dst-ip
  P2MP PW: disabled
  Create time: 17/09/2020 03:58:27 (38w3d ago)
  No status change since creation
  ACs: 2 (2 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
  List of ACs:
    AC: Bundle-Ether10.1266, state is up
      Type VLAN; Num Ranges: 1
      Outer Tag: 1023
      Rewrite Tags: []
      VLAN ranges: [1266, 1266]
      MTU 9000; XC ID 0xc0000318; interworking none
      MAC learning: enabled
      Flooding:
        Broadcast & Multicast: enabled
        Unknown unicast: enabled
      MAC aging time: 300 s, Type: inactivity
      MAC limit: 4000, Action: none, Notification: syslog
      MAC limit reached: no, threshold: 75%
      MAC port down flush: enabled
      MAC Secure: disabled, Logging: disabled
      Split Horizon Group: none
      Dynamic ARP Inspection: disabled, Logging: disabled
      IP Source Guard: disabled, Logging: disabled
      DHCPv4 Snooping: disabled
      DHCPv4 Snooping profile: none
      IGMP Snooping: disabled
      IGMP Snooping profile: none
      MLD Snooping profile: none
      Storm Control: bridge-domain policer
      Static MAC addresses:
      Statistics:
        packets: received 3245556280 (multicast 0, broadcast 8763, unknown unicast 166277, unicast 3245382797), sent 1465216351
        bytes: received 4339841715578 (multicast 0, broadcast 3233500, unknown unicast 149890469, unicast 4339690038523), sent 344268595837
        MAC move: 0
      Storm control drop counters:
        packets: broadcast 0, multicast 0, unknown unicast 0
        bytes: broadcast 0, multicast 0, unknown unicast 0
      Dynamic ARP inspection drop counters:
        packets: 0, bytes: 0
      IP source guard drop counters:
        packets: 0, bytes: 0
    AC: Bundle-Ether3.1266, state is up
      Type VLAN; Num Ranges: 1
      Rewrite Tags: []
      VLAN ranges: [1266, 1266]
      MTU 9000; XC ID 0xc0000314; interworking none
      MAC learning: enabled
      Flooding:
        Broadcast & Multicast: enabled
        Unknown unicast: enabled
      MAC aging time: 300 s, Type: inactivity
      MAC limit: 4000, Action: none, Notification: syslog
      MAC limit reached: no, threshold: 75%
      MAC port down flush: enabled
      MAC Secure: disabled, Logging: disabled
      Split Horizon Group: none
      Dynamic ARP Inspection: disabled, Logging: disabled
      IP Source Guard: disabled, Logging: disabled
      DHCPv4 Snooping: disabled
      DHCPv4 Snooping profile: none
      IGMP Snooping: disabled
      IGMP Snooping profile: none
      MLD Snooping profile: none
      Storm Control: bridge-domain policer
      Static MAC addresses:
      Statistics:
        packets: received 1465145657 (multicast 338510, broadcast 1736376, unknown unicast 2, unicast 1463070770), sent 3245432086
        bytes: received 338398661284 (multicast 34838238, broadcast 116685357, unknown unicast 162, unicast 338247137591), sent 4326687483580
        MAC move: 0
      Storm control drop counters:
        packets: broadcast 0, multicast 0, unknown unicast 0
        bytes: broadcast 0, multicast 0, unknown unicast 0
      Dynamic ARP inspection drop counters:
        packets: 0, bytes: 0
      IP source guard drop counters:
        packets: 0, bytes: 0
  List of Access PWs:
  List of VFIs:
  List of Access VFIs:
Bridge group: Subscriber_MTS, bridge-domain: 1267, id: 257, state: up, ShgId: 0, MSTi: 0
  Coupled state: disabled
  VINE state: Default
  MAC learning: enabled
  MAC withdraw: enabled
    MAC withdraw for Access PW: enabled
    MAC withdraw sent on: bridge port up
    MAC withdraw relaying (access to access): disabled
  Flooding:
    Broadcast & Multicast: enabled
    Unknown unicast: enabled
  MAC aging time: 300 s, Type: inactivity
  MAC limit: 4000, Action: none, Notification: syslog
  MAC limit reached: no, threshold: 75%
  MAC port down flush: enabled
  MAC Secure: disabled, Logging: disabled
  Split Horizon Group: none
  Dynamic ARP Inspection: disabled, Logging: disabled
  IP Source Guard: disabled, Logging: disabled
  DHCPv4 Snooping: disabled
  DHCPv4 Snooping profile: none
  IGMP Snooping: disabled
  IGMP Snooping profile: none
  MLD Snooping profile: none
  Storm Control: disabled
  Bridge MTU: 1500
  MIB cvplsConfigIndex: 258
  Filter MAC addresses:
  Load Balance Hashing: src-dst-ip
  P2MP PW: disabled
  Create time: 17/09/2020 03:58:27 (38w3d ago)
  No status change since creation
  ACs: 2 (2 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
  List of ACs:
    AC: Bundle-Ether10.1267, state is up
      Type VLAN; Num Ranges: 1
      Outer Tag: 1023
      Rewrite Tags: []
      VLAN ranges: [1267, 1267]
      MTU 9000; XC ID 0xc000031a; interworking none
      MAC learning: enabled
      Flooding:
        Broadcast & Multicast: enabled
        Unknown unicast: enabled
      MAC aging time: 300 s, Type: inactivity
      MAC limit: 4000, Action: none, Notification: syslog
      MAC limit reached: no, threshold: 75%
      MAC port down flush: enabled
      MAC Secure: disabled, Logging: disabled
      Split Horizon Group: none
      Dynamic ARP Inspection: disabled, Logging: disabled
      IP Source Guard: disabled, Logging: disabled
      DHCPv4 Snooping: disabled
      DHCPv4 Snooping profile: none
      IGMP Snooping: disabled
      IGMP Snooping profile: none
      MLD Snooping profile: none
      Storm Control: bridge-domain policer
      Static MAC addresses:
      Statistics:
        packets: received 4603415788 (multicast 0, broadcast 11739, unknown unicast 214080, unicast 4603192922), sent 2355034330
        bytes: received 5820136906653 (multicast 0, broadcast 4331672, unknown unicast 196243591, unicast 5819937825269), sent 818805396762
        MAC move: 0
      Storm control drop counters:
        packets: broadcast 0, multicast 0, unknown unicast 0
        bytes: broadcast 0, multicast 0, unknown unicast 0
      Dynamic ARP inspection drop counters:
        packets: 0, bytes: 0
      IP source guard drop counters:
        packets: 0, bytes: 0
    AC: Bundle-Ether3.1267, state is up
      Type VLAN; Num Ranges: 1
      Rewrite Tags: []
      VLAN ranges: [1267, 1267]
      MTU 9000; XC ID 0xc0000316; interworking none
      MAC learning: enabled
      Flooding:
        Broadcast & Multicast: enabled
        Unknown unicast: enabled
      MAC aging time: 300 s, Type: inactivity
      MAC limit: 4000, Action: none, Notification: syslog
      MAC limit reached: no, threshold: 75%
      MAC port down flush: enabled
      MAC Secure: disabled, Logging: disabled
      Split Horizon Group: none
      Dynamic ARP Inspection: disabled, Logging: disabled
      IP Source Guard: disabled, Logging: disabled
      DHCPv4 Snooping: disabled
      DHCPv4 Snooping profile: none
      IGMP Snooping: disabled
      IGMP Snooping profile: none
      MLD Snooping profile: none
      Storm Control: bridge-domain policer
      Static MAC addresses:
      Statistics:
        packets: received 2354966866 (multicast 445231, broadcast 2697447, unknown unicast 23501, unicast 2351800687), sent 4603284751
        bytes: received 809357601016 (multicast 34967010, broadcast 186220614, unknown unicast 1693794, unicast 809134719598), sent 5801561953485
        MAC move: 0
      Storm control drop counters:
        packets: broadcast 0, multicast 0, unknown unicast 0
        bytes: broadcast 0, multicast 0, unknown unicast 0
      Dynamic ARP inspection drop counters:
        packets: 0, bytes: 0
      IP source guard drop counters:
        packets: 0, bytes: 0
  List of Access PWs:
  List of VFIs:
  List of Access VFIs:
Bridge group: Subscriber_MTS, bridge-domain: 1268, id: 36, state: up, ShgId: 0, MSTi: 0
  Coupled state: disabled
  VINE state: Default
  MAC learning: enabled
  MAC withdraw: enabled
    MAC withdraw for Access PW: enabled
    MAC withdraw sent on: bridge port up
    MAC withdraw relaying (access to access): disabled
  Flooding:
    Broadcast & Multicast: enabled
    Unknown unicast: enabled
  MAC aging time: 300 s, Type: inactivity
  MAC limit: 4000, Action: none, Notification: syslog
  MAC limit reached: no, threshold: 75%
  MAC port down flush: enabled
  MAC Secure: disabled, Logging: disabled
  Split Horizon Group: none
  Dynamic ARP Inspection: disabled, Logging: disabled
  IP Source Guard: disabled, Logging: disabled
  DHCPv4 Snooping: disabled
  DHCPv4 Snooping profile: none
  IGMP Snooping: disabled
  IGMP Snooping profile: none
  MLD Snooping profile: none
  Storm Control: disabled
  Bridge MTU: 1500
  MIB cvplsConfigIndex: 37
  Filter MAC addresses:
  Load Balance Hashing: src-dst-ip
  P2MP PW: disabled
  Create time: 13/12/2019 02:49:09 (1y26w ago)
  No status change since creation
  ACs: 2 (2 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
  List of ACs:
    AC: Bundle-Ether10.1268, state is up
      Type VLAN; Num Ranges: 1
      Outer Tag: 1012
      Rewrite Tags: []
      VLAN ranges: [1268, 1268]
      MTU 9000; XC ID 0xc000009a; interworking none
      MAC learning: enabled
      Flooding:
        Broadcast & Multicast: enabled
        Unknown unicast: enabled
      MAC aging time: 300 s, Type: inactivity
      MAC limit: 4000, Action: none, Notification: syslog
      MAC limit reached: no, threshold: 75%
      MAC port down flush: enabled
      MAC Secure: disabled, Logging: disabled
      Split Horizon Group: none
      Dynamic ARP Inspection: disabled, Logging: disabled
      IP Source Guard: disabled, Logging: disabled
      DHCPv4 Snooping: disabled
      DHCPv4 Snooping profile: none
      IGMP Snooping: disabled
      IGMP Snooping profile: none
      MLD Snooping profile: none
      Storm Control: bridge-domain policer
      Static MAC addresses:
      Statistics:
        packets: received 0 (multicast 0, broadcast 0, unknown unicast 0, unicast 0), sent 0
        bytes: received 0 (multicast 0, broadcast 0, unknown unicast 0, unicast 0), sent 0
        MAC move: 0
      Storm control drop counters:
        packets: broadcast 0, multicast 0, unknown unicast 0
        bytes: broadcast 0, multicast 0, unknown unicast 0
      Dynamic ARP inspection drop counters:
        packets: 0, bytes: 0
      IP source guard drop counters:
        packets: 0, bytes: 0
    AC: Bundle-Ether3.1268, state is up
      Type VLAN; Num Ranges: 1
      Rewrite Tags: []
      VLAN ranges: [1268, 1268]
      MTU 9000; XC ID 0xc000007c; interworking none
      MAC learning: enabled
      Flooding:
        Broadcast & Multicast: enabled
        Unknown unicast: enabled
      MAC aging time: 300 s, Type: inactivity
      MAC limit: 4000, Action: none, Notification: syslog
      MAC limit reached: no, threshold: 75%
      MAC port down flush: enabled
      MAC Secure: disabled, Logging: disabled
      Split Horizon Group: none
      Dynamic ARP Inspection: disabled, Logging: disabled
      IP Source Guard: disabled, Logging: disabled
      DHCPv4 Snooping: disabled
      DHCPv4 Snooping profile: none
      IGMP Snooping: disabled
      IGMP Snooping profile: none
      MLD Snooping profile: none
      Storm Control: bridge-domain policer
      Static MAC addresses:
      Statistics:
        packets: received 0 (multicast 0, broadcast 0, unknown unicast 0, unicast 0), sent 0
        bytes: received 0 (multicast 0, broadcast 0, unknown unicast 0, unicast 0), sent 0
        MAC move: 0
      Storm control drop counters:
        packets: broadcast 0, multicast 0, unknown unicast 0
        bytes: broadcast 0, multicast 0, unknown unicast 0
      Dynamic ARP inspection drop counters:
        packets: 0, bytes: 0
      IP source guard drop counters:
        packets: 0, bytes: 0
  List of Access PWs:
  List of VFIs:
  List of Access VFIs:
Bridge group: Other_Connect_Tmp, bridge-domain: 1270, id: 157, state: up, ShgId: 0, MSTi: 0
  Coupled state: disabled
  VINE state: Default
  MAC learning: enabled
  MAC withdraw: enabled
    MAC withdraw for Access PW: enabled
    MAC withdraw sent on: bridge port up
    MAC withdraw relaying (access to access): disabled
  Flooding:
    Broadcast & Multicast: enabled
    Unknown unicast: enabled
  MAC aging time: 300 s, Type: inactivity
  MAC limit: 4000, Action: none, Notification: syslog
  MAC limit reached: no, threshold: 75%
  MAC port down flush: enabled
  MAC Secure: disabled, Logging: disabled
  Split Horizon Group: none
  Dynamic ARP Inspection: disabled, Logging: disabled
  IP Source Guard: disabled, Logging: disabled
  DHCPv4 Snooping: disabled
  DHCPv4 Snooping profile: none
  IGMP Snooping: disabled
  IGMP Snooping profile: none
  MLD Snooping profile: none
  Storm Control: disabled
  Bridge MTU: 1500
  MIB cvplsConfigIndex: 158
  Filter MAC addresses:
  Load Balance Hashing: src-dst-ip
  P2MP PW: disabled
  Create time: 04/06/2020 13:20:08 (1y01w ago)
  No status change since creation
  ACs: 2 (2 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
  List of ACs:
    AC: Bundle-Ether3.1270, state is up
      Type VLAN; Num Ranges: 1
      Rewrite Tags: []
      VLAN ranges: [1270, 1270]
      MTU 9000; XC ID 0xc0000242; interworking none
      MAC learning: enabled
      Flooding:
        Broadcast & Multicast: enabled
        Unknown unicast: enabled
      MAC aging time: 300 s, Type: inactivity
      MAC limit: 4000, Action: none, Notification: syslog
      MAC limit reached: no, threshold: 75%
      MAC port down flush: enabled
      MAC Secure: disabled, Logging: disabled
      Split Horizon Group: none
      Dynamic ARP Inspection: disabled, Logging: disabled
      IP Source Guard: disabled, Logging: disabled
      DHCPv4 Snooping: disabled
      DHCPv4 Snooping profile: none
      IGMP Snooping: disabled
      IGMP Snooping profile: none
      MLD Snooping profile: none
      Storm Control: bridge-domain policer
      Static MAC addresses:
      Statistics:
        packets: received 117707 (multicast 117707, broadcast 0, unknown unicast 0, unicast 0), sent 0
        bytes: received 8004076 (multicast 8004076, broadcast 0, unknown unicast 0, unicast 0), sent 0
        MAC move: 0
      Storm control drop counters:
        packets: broadcast 0, multicast 0, unknown unicast 0
        bytes: broadcast 0, multicast 0, unknown unicast 0
      Dynamic ARP inspection drop counters:
        packets: 0, bytes: 0
      IP source guard drop counters:
        packets: 0, bytes: 0
    AC: TenGigE0/2/0/11.1270, state is up
      Type VLAN; Num Ranges: 1
      Rewrite Tags: []
      VLAN ranges: [1270, 1270]
      MTU 1526; XC ID 0x1200220; interworking none
      MAC learning: enabled
      Flooding:
        Broadcast & Multicast: enabled
        Unknown unicast: enabled
      MAC aging time: 300 s, Type: inactivity
      MAC limit: 4000, Action: none, Notification: syslog
      MAC limit reached: no, threshold: 75%
      MAC port down flush: enabled
      MAC Secure: disabled, Logging: disabled
      Split Horizon Group: none
      Dynamic ARP Inspection: disabled, Logging: disabled
      IP Source Guard: disabled, Logging: disabled
      DHCPv4 Snooping: disabled
      DHCPv4 Snooping profile: none
      IGMP Snooping: disabled
      IGMP Snooping profile: none
      MLD Snooping profile: none
      Storm Control: bridge-domain policer
      Static MAC addresses:
      Statistics:
        packets: received 0 (multicast 0, broadcast 0, unknown unicast 0, unicast 0), sent 117708
        bytes: received 0 (multicast 0, broadcast 0, unknown unicast 0, unicast 0), sent 8004144
        MAC move: 0
      Storm control drop counters:
        packets: broadcast 0, multicast 0, unknown unicast 0
        bytes: broadcast 0, multicast 0, unknown unicast 0
      Dynamic ARP inspection drop counters:
        packets: 0, bytes: 0
      IP source guard drop counters:
        packets: 0, bytes: 0
  List of Access PWs:
  List of VFIs:
  List of Access VFIs:
Bridge group: Other_Connect_Tmp, bridge-domain: BS_3986, id: 259, state: up, ShgId: 0, MSTi: 0
  Coupled state: disabled
  VINE state: Default
  MAC learning: enabled
  MAC withdraw: enabled
    MAC withdraw for Access PW: enabled
    MAC withdraw sent on: bridge port up
    MAC withdraw relaying (access to access): disabled
  Flooding:
    Broadcast & Multicast: enabled
    Unknown unicast: enabled
  MAC aging time: 300 s, Type: inactivity
  MAC limit: 4000, Action: none, Notification: syslog
  MAC limit reached: no, threshold: 75%
  MAC port down flush: enabled
  MAC Secure: disabled, Logging: disabled
  Split Horizon Group: none
  Dynamic ARP Inspection: disabled, Logging: disabled
  IP Source Guard: disabled, Logging: disabled
  DHCPv4 Snooping: disabled
  DHCPv4 Snooping profile: none
  IGMP Snooping: disabled
  IGMP Snooping profile: none
  MLD Snooping profile: none
  Storm Control: disabled
  Bridge MTU: 1500
  MIB cvplsConfigIndex: 260
  Filter MAC addresses:
  Load Balance Hashing: src-dst-ip
  P2MP PW: disabled
  Create time: 21/09/2020 15:58:08 (37w6d ago)
  No status change since creation
  ACs: 2 (2 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
  List of ACs:
    AC: Bundle-Ether3.3986, state is up
      Type VLAN; Num Ranges: 1
      Rewrite Tags: []
      VLAN ranges: [3986, 3986]
      MTU 9000; XC ID 0xc000031e; interworking none
      MAC learning: enabled
      Flooding:
        Broadcast & Multicast: enabled
        Unknown unicast: enabled
      MAC aging time: 300 s, Type: inactivity
      MAC limit: 4000, Action: none, Notification: syslog
      MAC limit reached: no, threshold: 75%
      MAC port down flush: enabled
      MAC Secure: disabled, Logging: disabled
      Split Horizon Group: none
      Dynamic ARP Inspection: disabled, Logging: disabled
      IP Source Guard: disabled, Logging: disabled
      DHCPv4 Snooping: disabled
      DHCPv4 Snooping profile: none
      IGMP Snooping: disabled
      IGMP Snooping profile: none
      MLD Snooping profile: none
      Storm Control: bridge-domain policer
      Static MAC addresses:
      Statistics:
        packets: received 3901995 (multicast 0, broadcast 0, unknown unicast 0, unicast 3901995), sent 6335822
        bytes: received 275112570 (multicast 0, broadcast 0, unknown unicast 0, unicast 275112570), sent 7269237551
        MAC move: 0
      Storm control drop counters:
        packets: broadcast 0, multicast 0, unknown unicast 0
        bytes: broadcast 0, multicast 0, unknown unicast 0
      Dynamic ARP inspection drop counters:
        packets: 0, bytes: 0
      IP source guard drop counters:
        packets: 0, bytes: 0
    AC: TenGigE0/2/0/11.3986, state is up
      Type VLAN; Num Ranges: 1
      Rewrite Tags: []
      VLAN ranges: [3986, 3986]
      MTU 1526; XC ID 0x1200322; interworking none
      MAC learning: enabled
      Flooding:
        Broadcast & Multicast: enabled
        Unknown unicast: enabled
      MAC aging time: 300 s, Type: inactivity
      MAC limit: 4000, Action: none, Notification: syslog
      MAC limit reached: no, threshold: 75%
      MAC port down flush: enabled
      MAC Secure: disabled, Logging: disabled
      Split Horizon Group: none
      Dynamic ARP Inspection: disabled, Logging: disabled
      IP Source Guard: disabled, Logging: disabled
      DHCPv4 Snooping: disabled
      DHCPv4 Snooping profile: none
      IGMP Snooping: disabled
      IGMP Snooping profile: none
      MLD Snooping profile: none
      Storm Control: bridge-domain policer
      Static MAC addresses:
      Statistics:
        packets: received 6335693 (multicast 0, broadcast 0, unknown unicast 0, unicast 6335693), sent 3901902
        bytes: received 7269096652 (multicast 0, broadcast 0, unknown unicast 0, unicast 7269096652), sent 275105988
        MAC move: 0
      Storm control drop counters:
        packets: broadcast 0, multicast 0, unknown unicast 0
        bytes: broadcast 0, multicast 0, unknown unicast 0
      Dynamic ARP inspection drop counters:
        packets: 0, bytes: 0
      IP source guard drop counters:
        packets: 0, bytes: 0
  List of Access PWs:
  List of VFIs:
  List of Access VFIs:
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowL2vpnBridgeDomainDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowL2vpnBridgeDomainDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowL2vpnBridgeDomainDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_golden3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        obj = ShowL2vpnBridgeDomainDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output3)

    def test_golden4(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output4)
        obj = ShowL2vpnBridgeDomainDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output4)

    def test_golden5(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output5)
        obj = ShowL2vpnBridgeDomainDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output5)

    def test_golden6(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output6)
        obj = ShowL2vpnBridgeDomainDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output6)

    def test_golden7(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output7)
        obj = ShowL2vpnBridgeDomainDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output7)


if __name__ == '__main__':
    unittest.main()
