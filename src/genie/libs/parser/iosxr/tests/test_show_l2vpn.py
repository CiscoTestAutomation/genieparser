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


if __name__ == '__main__':
    unittest.main()
