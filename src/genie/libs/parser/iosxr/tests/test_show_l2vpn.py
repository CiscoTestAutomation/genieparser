# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

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
                                    '7777.7777.0002': {
                                        'ip_address': []}}}}}}},
            '6': {
                'producer': {
                    '0/0/CPU0': {
                        'next_hop': {
                            'BV1': {
                                'mac_address': {
                                    '0000.f65a.357c': {
                                        'ip_address': ['fe80::200:f6ff:fe5a:357c']},
                                    '1000.0001.0001': {
                                        'ip_address': ['10.1.1.11']}}}}}}},
            '7': {
                'producer': {
                    '0/0/CPU0': {
                        'next_hop': {
                            'BV2': {
                                'mac_address': {
                                    '0000.f65a.3570': {
                                        'ip_address': [
                                            '10.1.2.91', '10.1.2.93']}}}}}}}}}

    device_output = {'execute.return_value': '''
        Topo ID  Producer  Next Hop(s)  Mac Address     IP Address

        6        0/0/CPU0   BV1        1000.0001.0001      10.1.1.11
        7        0/0/CPU0   BV2        0000.f65a.3570      10.1.2.91
        7        0/0/CPU0   BV2        0000.f65a.3570      10.1.2.93
        1        0/0/CPU0   BE1.7      7777.7777.0002
        6        0/0/CPU0   BV1        0000.f65a.357c      fe80::200:f6ff:fe5a:357c

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
                    'EVPN-Multicast-BTV': {
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

        Bridge group: g1, bridge-domain: EVPN-Multicast-BTV, id: 0, state: up, ShgId: 0, MSTi: 0
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
                    'EVPN-Multicast-BTV': {
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
        Bridge group: EVPN-Mulicast, bridge-domain: EVPN-Multicast-BTV, id: 0, state: up, ShgId: 0, MSTi: 0
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
                            'vfi100 (up)': {
                                'neighbor': {
                                    '11.11.11.11': {
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
                    '101_evpn_access': {
                        'id': 2,
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
                                'GigabitEthernet0/4/0/6.101': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 6,
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
                    '102_evpn_access': {
                        'id': 3,
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
                                'GigabitEthernet0/4/0/6.102': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 7,
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
                    '103_evpn_access': {
                        'id': 4,
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
                                'GigabitEthernet0/4/0/6.103': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 8,
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
                    '104_evpn_access': {
                        'id': 5,
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
                                'GigabitEthernet0/4/0/6.104': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 9,
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
                    '105_evpn_access': {
                        'id': 6,
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
                                'GigabitEthernet0/4/0/6.105': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 10,
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
                    '106_evpn_access': {
                        'id': 7,
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
                                'GigabitEthernet0/4/0/6.106': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 11,
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
                    '107_evpn_access': {
                        'id': 8,
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
                                'GigabitEthernet0/4/0/6.107': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 12,
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
                    '108_evpn_access': {
                        'id': 9,
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
                                'GigabitEthernet0/4/0/6.108': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 1,
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
                    '109_evpn_access': {
                        'id': 10,
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
                                'GigabitEthernet0/4/0/6.109': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 2,
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
                    '110_evpn_access': {
                        'id': 11,
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
                                'GigabitEthernet0/4/0/6.110': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 3,
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
                    '111_evpn_access': {
                        'id': 12,
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
                                'GigabitEthernet0/4/0/6.111': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 4,
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
                    '112_evpn_access': {
                        'id': 13,
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
                                'GigabitEthernet0/4/0/6.112': {
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
                    '113_evpn_access': {
                        'id': 14,
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
                                'GigabitEthernet0/4/0/6.113': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 6,
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
                    '114_evpn_access': {
                        'id': 15,
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
                                'GigabitEthernet0/4/0/6.114': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 7,
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
                    '115_evpn_access': {
                        'id': 16,
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
                                'GigabitEthernet0/4/0/6.115': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 8,
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
                    '116_evpn_access': {
                        'id': 17,
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
                                'GigabitEthernet0/4/0/6.116': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 9,
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
                    '117_evpn_access': {
                        'id': 18,
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
                                'GigabitEthernet0/4/0/6.117': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 10,
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
                    '118_evpn_access': {
                        'id': 19,
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
                                'GigabitEthernet0/4/0/6.118': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 11,
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
                    '119_evpn_access': {
                        'id': 20,
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
                                'GigabitEthernet0/4/0/6.119': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 12,
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
                    '120_evpn_access': {
                        'id': 21,
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
                                'GigabitEthernet0/4/0/6.120': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 1,
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
                    '121_evpn_access': {
                        'id': 22,
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
                                'GigabitEthernet0/4/0/6.121': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 2,
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
                    '122_evpn_access': {
                        'id': 23,
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
                                'GigabitEthernet0/4/0/6.122': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 3,
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
                    '123_evpn_access': {
                        'id': 24,
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
                                'GigabitEthernet0/4/0/6.123': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 4,
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
                    '124_evpn_access': {
                        'id': 25,
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
                                'GigabitEthernet0/4/0/6.124': {
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
                    '125_evpn_access': {
                        'id': 26,
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
                                'GigabitEthernet0/4/0/6.125': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 6,
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
                    '126_evpn_access': {
                        'id': 27,
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
                                'GigabitEthernet0/4/0/6.126': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 7,
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
                    '127_evpn_access': {
                        'id': 28,
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
                                'GigabitEthernet0/4/0/6.127': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 8,
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
                    '128_evpn_access': {
                        'id': 29,
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
                                'GigabitEthernet0/4/0/6.128': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 9,
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
                    '129_evpn_access': {
                        'id': 30,
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
                                'GigabitEthernet0/4/0/6.129': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 10,
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
                    '130_evpn_access': {
                        'id': 31,
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
                                'GigabitEthernet0/4/0/6.130': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 11,
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
                    '131_evpn_access': {
                        'id': 32,
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
                                'GigabitEthernet0/4/0/6.131': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 12,
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
                    '132_evpn_access': {
                        'id': 33,
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
                                'GigabitEthernet0/4/0/6.132': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 1,
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
                    '133_evpn_access': {
                        'id': 34,
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
                                'GigabitEthernet0/4/0/6.133': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 2,
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
                    '134_evpn_access': {
                        'id': 35,
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
                                'GigabitEthernet0/4/0/6.134': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 3,
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
                    '135_evpn_access': {
                        'id': 36,
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
                                'GigabitEthernet0/4/0/6.135': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 4,
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
                    '136_evpn_access': {
                        'id': 37,
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
                                'GigabitEthernet0/4/0/6.136': {
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
                    '137_evpn_access': {
                        'id': 38,
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
                                'GigabitEthernet0/4/0/6.137': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 6,
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
                    '138_evpn_access': {
                        'id': 39,
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
                                'GigabitEthernet0/4/0/6.138': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 7,
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
                    '139_evpn_access': {
                        'id': 40,
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
                                'GigabitEthernet0/4/0/6.139': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 8,
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
                    '140_evpn_access': {
                        'id': 41,
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
                                'GigabitEthernet0/4/0/6.140': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 9,
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
                    '141_evpn_access': {
                        'id': 42,
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
                                'GigabitEthernet0/4/0/6.141': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 10,
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
                    '142_evpn_access': {
                        'id': 43,
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
                                'GigabitEthernet0/4/0/6.142': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 11,
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
                    '143_evpn_access': {
                        'id': 44,
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
                                'GigabitEthernet0/4/0/6.143': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 12,
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
                    '144_evpn_access': {
                        'id': 45,
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
                                'GigabitEthernet0/4/0/6.144': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 1,
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
                    '145_evpn_access': {
                        'id': 46,
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
                                'GigabitEthernet0/4/0/6.145': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 2,
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
                    '146_evpn_access': {
                        'id': 47,
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
                                'GigabitEthernet0/4/0/6.146': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 3,
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
                    '147_evpn_access': {
                        'id': 48,
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
                                'GigabitEthernet0/4/0/6.147': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 4,
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
                    '148_evpn_access': {
                        'id': 49,
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
                                'GigabitEthernet0/4/0/6.148': {
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
                    '149_evpn_access': {
                        'id': 50,
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
                                'GigabitEthernet0/4/0/6.149': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 6,
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
                    '150_evpn_access': {
                        'id': 51,
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
                                'GigabitEthernet0/4/0/6.150': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 7,
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
                    '151_evpn_access': {
                        'id': 52,
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
                                'GigabitEthernet0/4/0/6.151': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 8,
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
                    '152_evpn_access': {
                        'id': 53,
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
                                'GigabitEthernet0/4/0/6.152': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 9,
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
                    '153_evpn_access': {
                        'id': 54,
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
                                'GigabitEthernet0/4/0/6.153': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 10,
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
                    '154_evpn_access': {
                        'id': 55,
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
                                'GigabitEthernet0/4/0/6.154': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 11,
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
                    '155_evpn_access': {
                        'id': 56,
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
                                'GigabitEthernet0/4/0/6.155': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 12,
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
                    '156_evpn_access': {
                        'id': 57,
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
                                'GigabitEthernet0/4/0/6.156': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 1,
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
                    '157_evpn_access': {
                        'id': 58,
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
                                'GigabitEthernet0/4/0/6.157': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 2,
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
                    '158_evpn_access': {
                        'id': 59,
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
                                'GigabitEthernet0/4/0/6.158': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 3,
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
                    '159_evpn_access': {
                        'id': 60,
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
                                'GigabitEthernet0/4/0/6.159': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 4,
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
                    '160_evpn_access': {
                        'id': 61,
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
                                'GigabitEthernet0/4/0/6.160': {
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
                    '161_evpn_access': {
                        'id': 62,
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
                                'GigabitEthernet0/4/0/6.161': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 6,
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
                    '162_evpn_access': {
                        'id': 63,
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
                                'GigabitEthernet0/4/0/6.162': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 7,
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
                    '163_evpn_access': {
                        'id': 64,
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
                                'GigabitEthernet0/4/0/6.163': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 8,
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
                    '164_evpn_access': {
                        'id': 65,
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
                                'GigabitEthernet0/4/0/6.164': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 9,
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
                    '165_evpn_access': {
                        'id': 66,
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
                                'GigabitEthernet0/4/0/6.165': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 10,
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
                    '166_evpn_access': {
                        'id': 67,
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
                                'GigabitEthernet0/4/0/6.166': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 11,
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
                    '167_evpn_access': {
                        'id': 68,
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
                                'GigabitEthernet0/4/0/6.167': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 12,
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
                    '168_evpn_access': {
                        'id': 69,
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
                                'GigabitEthernet0/4/0/6.168': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 1,
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
                    '169_evpn_access': {
                        'id': 70,
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
                                'GigabitEthernet0/4/0/6.169': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 2,
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
                    '170_evpn_access': {
                        'id': 71,
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
                                'GigabitEthernet0/4/0/6.170': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 3,
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
                    '171_evpn_access': {
                        'id': 72,
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
                                'GigabitEthernet0/4/0/6.171': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 4,
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
                    '172_evpn_access': {
                        'id': 73,
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
                                'GigabitEthernet0/4/0/6.172': {
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
                    '173_evpn_access': {
                        'id': 74,
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
                                'GigabitEthernet0/4/0/6.173': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 6,
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
                    '174_evpn_access': {
                        'id': 75,
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
                                'GigabitEthernet0/4/0/6.174': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 7,
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
                    '175_evpn_access': {
                        'id': 76,
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
                                'GigabitEthernet0/4/0/6.175': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 8,
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
                    '176_evpn_access': {
                        'id': 77,
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
                                'GigabitEthernet0/4/0/6.176': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 9,
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
                    '177_evpn_access': {
                        'id': 78,
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
                                'GigabitEthernet0/4/0/6.177': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 10,
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
                    '178_evpn_access': {
                        'id': 79,
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
                                'GigabitEthernet0/4/0/6.178': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 11,
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
                    '179_evpn_access': {
                        'id': 80,
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
                                'GigabitEthernet0/4/0/6.179': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 12,
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
                    '180_evpn_access': {
                        'id': 81,
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
                                'GigabitEthernet0/4/0/6.180': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 1,
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
                    '181_evpn_access': {
                        'id': 82,
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
                                'GigabitEthernet0/4/0/6.181': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 2,
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
                    '182_evpn_access': {
                        'id': 83,
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
                                'GigabitEthernet0/4/0/6.182': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 3,
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
                    '183_evpn_access': {
                        'id': 84,
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
                                'GigabitEthernet0/4/0/6.183': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 4,
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
                    '184_evpn_access': {
                        'id': 85,
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
                                'GigabitEthernet0/4/0/6.184': {
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
                    '185_evpn_access': {
                        'id': 86,
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
                                'GigabitEthernet0/4/0/6.185': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 6,
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
                    '186_evpn_access': {
                        'id': 87,
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
                                'GigabitEthernet0/4/0/6.186': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 7,
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
                    '187_evpn_access': {
                        'id': 88,
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
                                'GigabitEthernet0/4/0/6.187': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 8,
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
                    '188_evpn_access': {
                        'id': 89,
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
                                'GigabitEthernet0/4/0/6.188': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 9,
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
                    '189_evpn_access': {
                        'id': 90,
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
                                'GigabitEthernet0/4/0/6.189': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 10,
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
                    '190_evpn_access': {
                        'id': 91,
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
                                'GigabitEthernet0/4/0/6.190': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 11,
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
                    '191_evpn_access': {
                        'id': 92,
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
                                'GigabitEthernet0/4/0/6.191': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 12,
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
                    '192_evpn_access': {
                        'id': 93,
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
                                'GigabitEthernet0/4/0/6.192': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 1,
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
                    '193_evpn_access': {
                        'id': 94,
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
                                'GigabitEthernet0/4/0/6.193': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 2,
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
                    '194_evpn_access': {
                        'id': 95,
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
                                'GigabitEthernet0/4/0/6.194': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 3,
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
                    '195_evpn_access': {
                        'id': 96,
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
                                'GigabitEthernet0/4/0/6.195': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 4,
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
                    '196_evpn_access': {
                        'id': 97,
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
                                'GigabitEthernet0/4/0/6.196': {
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
                    '197_evpn_access': {
                        'id': 98,
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
                                'GigabitEthernet0/4/0/6.197': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 6,
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
                    '198_evpn_access': {
                        'id': 99,
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
                                'GigabitEthernet0/4/0/6.198': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 7,
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
                    '199_evpn_access': {
                        'id': 100,
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
                                'GigabitEthernet0/4/0/6.199': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 8,
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
                    '200_evpn_access': {
                        'id': 101,
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
                                'GigabitEthernet0/4/0/6.200': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 9,
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
                    '201_evpn_access': {
                        'id': 102,
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
                                'GigabitEthernet0/4/0/6.201': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 10,
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
                    '202_evpn_access': {
                        'id': 103,
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
                                'GigabitEthernet0/4/0/6.202': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 11,
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
                    '203_evpn_access': {
                        'id': 104,
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
                                'GigabitEthernet0/4/0/6.203': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 12,
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
                    '204_evpn_access': {
                        'id': 105,
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
                                'GigabitEthernet0/4/0/6.204': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 1,
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
                    '205_evpn_access': {
                        'id': 106,
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
                                'GigabitEthernet0/4/0/6.205': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 2,
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
                    '206_evpn_access': {
                        'id': 107,
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
                                'GigabitEthernet0/4/0/6.206': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 3,
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
                    '207_evpn_access': {
                        'id': 108,
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
                                'GigabitEthernet0/4/0/6.207': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 4,
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
                    '208_evpn_access': {
                        'id': 109,
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
                                'GigabitEthernet0/4/0/6.208': {
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
                    '209_evpn_access': {
                        'id': 110,
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
                                'GigabitEthernet0/4/0/6.209': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 6,
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
                    '210_evpn_access': {
                        'id': 111,
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
                                'GigabitEthernet0/4/0/6.210': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 7,
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
                    '211_evpn_access': {
                        'id': 112,
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
                                'GigabitEthernet0/4/0/6.211': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 8,
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
                    '212_evpn_access': {
                        'id': 113,
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
                                'GigabitEthernet0/4/0/6.212': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 9,
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
                    '213_evpn_access': {
                        'id': 114,
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
                                'GigabitEthernet0/4/0/6.213': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 10,
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
                    '214_evpn_access': {
                        'id': 115,
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
                                'GigabitEthernet0/4/0/6.214': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 11,
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
                    '215_evpn_access': {
                        'id': 116,
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
                                'GigabitEthernet0/4/0/6.215': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 12,
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
                    '216_evpn_access': {
                        'id': 117,
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
                                'GigabitEthernet0/4/0/6.216': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 1,
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
                    '217_evpn_access': {
                        'id': 118,
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
                                'GigabitEthernet0/4/0/6.217': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 2,
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
                    '218_evpn_access': {
                        'id': 119,
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
                                'GigabitEthernet0/4/0/6.218': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 3,
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
                    '219_evpn_access': {
                        'id': 120,
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
                                'GigabitEthernet0/4/0/6.219': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 4,
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
                    '220_evpn_access': {
                        'id': 121,
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
                                'GigabitEthernet0/4/0/6.220': {
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
                    '221_evpn_access': {
                        'id': 122,
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
                                'GigabitEthernet0/4/0/6.221': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 6,
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
                    '222_evpn_access': {
                        'id': 123,
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
                                'GigabitEthernet0/4/0/6.222': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 7,
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
                    '223_evpn_access': {
                        'id': 124,
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
                                'GigabitEthernet0/4/0/6.223': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 8,
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
                    '224_evpn_access': {
                        'id': 125,
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
                                'GigabitEthernet0/4/0/6.224': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 9,
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
                    '225_evpn_access': {
                        'id': 126,
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
                                'GigabitEthernet0/4/0/6.225': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 10,
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
                    '226_evpn_access': {
                        'id': 127,
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
                                'GigabitEthernet0/4/0/6.226': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 11,
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
                    '227_evpn_access': {
                        'id': 128,
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
                                'GigabitEthernet0/4/0/6.227': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 12,
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
                    '228_evpn_access': {
                        'id': 129,
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
                                'GigabitEthernet0/4/0/6.228': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 1,
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
                    '229_evpn_access': {
                        'id': 130,
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
                                'GigabitEthernet0/4/0/6.229': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 2,
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
                    '230_evpn_access': {
                        'id': 131,
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
                                'GigabitEthernet0/4/0/6.230': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 3,
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
                    '231_evpn_access': {
                        'id': 132,
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
                                'GigabitEthernet0/4/0/6.231': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 4,
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
                    '232_evpn_access': {
                        'id': 133,
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
                                'GigabitEthernet0/4/0/6.232': {
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
                    '233_evpn_access': {
                        'id': 134,
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
                                'GigabitEthernet0/4/0/6.233': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 6,
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
                    '234_evpn_access': {
                        'id': 135,
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
                                'GigabitEthernet0/4/0/6.234': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 7,
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
                    '235_evpn_access': {
                        'id': 136,
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
                                'GigabitEthernet0/4/0/6.235': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 8,
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
                    '236_evpn_access': {
                        'id': 137,
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
                                'GigabitEthernet0/4/0/6.236': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 9,
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
                    '237_evpn_access': {
                        'id': 138,
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
                                'GigabitEthernet0/4/0/6.237': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 10,
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
                    '238_evpn_access': {
                        'id': 139,
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
                                'GigabitEthernet0/4/0/6.238': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 11,
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
                    '239_evpn_access': {
                        'id': 140,
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
                                'GigabitEthernet0/4/0/6.239': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 12,
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
                    '240_evpn_access': {
                        'id': 141,
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
                                'GigabitEthernet0/4/0/6.240': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 1,
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
                    '241_evpn_access': {
                        'id': 142,
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
                                'GigabitEthernet0/4/0/6.241': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 2,
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
                    '242_evpn_access': {
                        'id': 143,
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
                                'GigabitEthernet0/4/0/6.242': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 3,
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
                    '243_evpn_access': {
                        'id': 144,
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
                                'GigabitEthernet0/4/0/6.243': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 4,
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
                    '244_evpn_access': {
                        'id': 145,
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
                                'GigabitEthernet0/4/0/6.244': {
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
                    '245_evpn_access': {
                        'id': 146,
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
                                'GigabitEthernet0/4/0/6.245': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 6,
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
                    '246_evpn_access': {
                        'id': 147,
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
                                'GigabitEthernet0/4/0/6.246': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 7,
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
                    '247_evpn_access': {
                        'id': 148,
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
                                'GigabitEthernet0/4/0/6.247': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 8,
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
                    '248_evpn_access': {
                        'id': 149,
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
                                'GigabitEthernet0/4/0/6.248': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 9,
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
                    '249_evpn_access': {
                        'id': 150,
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
                                'GigabitEthernet0/4/0/6.249': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 10,
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
                    '250_evpn_access': {
                        'id': 151,
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
                                'GigabitEthernet0/4/0/6.250': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 11,
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
                    '251_evpn_access': {
                        'id': 152,
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
                                'GigabitEthernet0/4/0/6.251': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 12,
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
                    '252_evpn_access': {
                        'id': 153,
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
                                'GigabitEthernet0/4/0/6.252': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 1,
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
                    '253_evpn_access': {
                        'id': 154,
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
                                'GigabitEthernet0/4/0/6.253': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 2,
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
                    '254_evpn_access': {
                        'id': 155,
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
                                'GigabitEthernet0/4/0/6.254': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 3,
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
                    '255_evpn_access': {
                        'id': 156,
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
                                'GigabitEthernet0/4/0/6.255': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 4,
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
                    '256_evpn_access': {
                        'id': 157,
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
                                'GigabitEthernet0/4/0/6.256': {
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
                    '257_evpn_access': {
                        'id': 158,
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
                                'GigabitEthernet0/4/0/6.257': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 6,
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
                    '258_evpn_access': {
                        'id': 159,
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
                                'GigabitEthernet0/4/0/6.258': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 7,
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
                    '259_evpn_access': {
                        'id': 160,
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
                                'GigabitEthernet0/4/0/6.259': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 8,
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
                    '260_evpn_access': {
                        'id': 161,
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
                                'GigabitEthernet0/4/0/6.260': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 9,
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
                    '261_evpn_access': {
                        'id': 162,
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
                                'GigabitEthernet0/4/0/6.261': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 10,
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
                    '262_evpn_access': {
                        'id': 163,
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
                                'GigabitEthernet0/4/0/6.262': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 11,
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
                    '263_evpn_access': {
                        'id': 164,
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
                                'GigabitEthernet0/4/0/6.263': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 12,
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
                    '264_evpn_access': {
                        'id': 165,
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
                                'GigabitEthernet0/4/0/6.264': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 1,
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
                    '265_evpn_access': {
                        'id': 166,
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
                                'GigabitEthernet0/4/0/6.265': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 2,
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
                    '266_evpn_access': {
                        'id': 167,
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
                                'GigabitEthernet0/4/0/6.266': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 3,
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
                    '267_evpn_access': {
                        'id': 168,
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
                                'GigabitEthernet0/4/0/6.267': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 4,
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
                    '268_evpn_access': {
                        'id': 169,
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
                                'GigabitEthernet0/4/0/6.268': {
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
                    '269_evpn_access': {
                        'id': 170,
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
                                'GigabitEthernet0/4/0/6.269': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 6,
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
                    '270_evpn_access': {
                        'id': 171,
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
                                'GigabitEthernet0/4/0/6.270': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 7,
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
                    '271_evpn_access': {
                        'id': 172,
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
                                'GigabitEthernet0/4/0/6.271': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 8,
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
                    '272_evpn_access': {
                        'id': 173,
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
                                'GigabitEthernet0/4/0/6.272': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 9,
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
                    '273_evpn_access': {
                        'id': 174,
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
                                'GigabitEthernet0/4/0/6.273': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 10,
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
                    '274_evpn_access': {
                        'id': 175,
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
                                'GigabitEthernet0/4/0/6.274': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 11,
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
                    '275_evpn_access': {
                        'id': 176,
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
                                'GigabitEthernet0/4/0/6.275': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 12,
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
                    '276_evpn_access': {
                        'id': 177,
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
                                'GigabitEthernet0/4/0/6.276': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 1,
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
                    '277_evpn_access': {
                        'id': 178,
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
                                'GigabitEthernet0/4/0/6.277': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 2,
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
                    '278_evpn_access': {
                        'id': 179,
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
                                'GigabitEthernet0/4/0/6.278': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 3,
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
                    '279_evpn_access': {
                        'id': 180,
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
                                'GigabitEthernet0/4/0/6.279': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 4,
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
                    '280_evpn_access': {
                        'id': 181,
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
                                'GigabitEthernet0/4/0/6.280': {
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
                    '281_evpn_access': {
                        'id': 182,
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
                                'GigabitEthernet0/4/0/6.281': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 6,
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
                    '282_evpn_access': {
                        'id': 183,
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
                                'GigabitEthernet0/4/0/6.282': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 7,
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
                    '283_evpn_access': {
                        'id': 184,
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
                                'GigabitEthernet0/4/0/6.283': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 8,
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
                    '284_evpn_access': {
                        'id': 185,
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
                                'GigabitEthernet0/4/0/6.284': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 9,
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
                    '285_evpn_access': {
                        'id': 186,
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
                                'GigabitEthernet0/4/0/6.285': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 10,
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
                    '286_evpn_access': {
                        'id': 187,
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
                                'GigabitEthernet0/4/0/6.286': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 11,
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
                    '287_evpn_access': {
                        'id': 188,
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
                                'GigabitEthernet0/4/0/6.287': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 12,
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
                    '288_evpn_access': {
                        'id': 189,
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
                                'GigabitEthernet0/4/0/6.288': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 1,
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
                    '289_evpn_access': {
                        'id': 190,
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
                                'GigabitEthernet0/4/0/6.289': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 2,
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
                    '290_evpn_access': {
                        'id': 191,
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
                                'GigabitEthernet0/4/0/6.290': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 3,
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
                    '291_evpn_access': {
                        'id': 192,
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
                                'GigabitEthernet0/4/0/6.291': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 4,
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
                    '292_evpn_access': {
                        'id': 193,
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
                                'GigabitEthernet0/4/0/6.292': {
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
                    '293_evpn_access': {
                        'id': 194,
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
                                'GigabitEthernet0/4/0/6.293': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 6,
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
                    '294_evpn_access': {
                        'id': 195,
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
                                'GigabitEthernet0/4/0/6.294': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 7,
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
                    '295_evpn_access': {
                        'id': 196,
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
                                'GigabitEthernet0/4/0/6.295': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 8,
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
                    '296_evpn_access': {
                        'id': 197,
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
                                'GigabitEthernet0/4/0/6.296': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 9,
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
                    '297_evpn_access': {
                        'id': 198,
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
                                'GigabitEthernet0/4/0/6.297': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 10,
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
                    '298_evpn_access': {
                        'id': 199,
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
                                'GigabitEthernet0/4/0/6.298': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 11,
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
                    '299_evpn_access': {
                        'id': 200,
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
                                'GigabitEthernet0/4/0/6.299': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 12,
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
                    '300_evpn_access': {
                        'id': 201,
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
                                'GigabitEthernet0/4/0/6.300': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 1,
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
                    '1994_evpn_access': {
                        'id': 202,
                        'state': 'up',
                        'shg_id': 0,
                        'mst_i': 0,
                        'mac_aging_time': 300,
                        'mac_limit': 1000,
                        'mac_limit_action': 'limit, no-flood',
                        'mac_limit_notification': 'syslog, trap',
                        'filter_mac_address': 0,
                        'ac': {
                            'num_ac': 2,
                            'num_ac_up': 1,
                            'interfaces': {
                                'BV900': {
                                    'state': 'down',
                                    'bvi_mac_address': 1,
                                },
                                'GigabitEthernet0/4/0/6.1994': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 3,
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
                    '2112_evpn_access': {
                        'id': 203,
                        'state': 'up',
                        'shg_id': 0,
                        'mst_i': 0,
                        'mac_aging_time': 300,
                        'mac_limit': 1000,
                        'mac_limit_action': 'limit, no-flood',
                        'mac_limit_notification': 'syslog, trap',
                        'filter_mac_address': 0,
                        'ac': {
                            'num_ac': 1,
                            'num_ac_up': 1,
                            'interfaces': {
                                'GigabitEthernet0/4/0/6.900': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 1,
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
            'evpn_fortinet': {
                'bridge_domain': {
                    'evpn_fortinet': {
                        'id': 204,
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
                            'num_ac_up': 3,
                            'interfaces': {
                                'BV19': {
                                    'state': 'up',
                                    'bvi_mac_address': 1,
                                },
                                'Bundle-Ether1.19': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 8,
                                },
                                'Bundle-Ether3.19': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                    'mst_i': 8,
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
            'E911-v2535-vpls': {
                'bridge_domain': {
                    'bd60': {
                        'id': 205,
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
                                'BV60': {
                                    'state': 'up',
                                    'bvi_mac_address': 1,
                                },
                                'GigabitEthernet0/4/0/1.60': {
                                    'state': 'up',
                                    'static_mac_address': 0,
                                },
                            },
                        },
                        'vfi': {
                            'num_vfi': 1,
                            'vfi60 (up)': {
                                'neighbor': {
                                    '67.70.219.150': {
                                        'pw_id': {
                                            100200: {
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
            Neighbor 11.11.11.11 pw-id 100100, state: up, Static MAC addresses: 0
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
        Bridge group: evpn_access, bridge-domain: 101_evpn_access, id: 2, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.101, state: up, Static MAC addresses: 0, MSTi: 6
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 102_evpn_access, id: 3, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.102, state: up, Static MAC addresses: 0, MSTi: 7
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 103_evpn_access, id: 4, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.103, state: up, Static MAC addresses: 0, MSTi: 8
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 104_evpn_access, id: 5, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.104, state: up, Static MAC addresses: 0, MSTi: 9
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 105_evpn_access, id: 6, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.105, state: up, Static MAC addresses: 0, MSTi: 10
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 106_evpn_access, id: 7, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.106, state: up, Static MAC addresses: 0, MSTi: 11
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 107_evpn_access, id: 8, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.107, state: up, Static MAC addresses: 0, MSTi: 12
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 108_evpn_access, id: 9, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.108, state: up, Static MAC addresses: 0, MSTi: 1
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 109_evpn_access, id: 10, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.109, state: up, Static MAC addresses: 0, MSTi: 2
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 110_evpn_access, id: 11, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.110, state: up, Static MAC addresses: 0, MSTi: 3
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 111_evpn_access, id: 12, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.111, state: up, Static MAC addresses: 0, MSTi: 4
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 112_evpn_access, id: 13, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.112, state: up, Static MAC addresses: 0, MSTi: 5
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 113_evpn_access, id: 14, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.113, state: up, Static MAC addresses: 0, MSTi: 6
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 114_evpn_access, id: 15, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.114, state: up, Static MAC addresses: 0, MSTi: 7
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 115_evpn_access, id: 16, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.115, state: up, Static MAC addresses: 0, MSTi: 8
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 116_evpn_access, id: 17, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.116, state: up, Static MAC addresses: 0, MSTi: 9
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 117_evpn_access, id: 18, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.117, state: up, Static MAC addresses: 0, MSTi: 10
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 118_evpn_access, id: 19, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.118, state: up, Static MAC addresses: 0, MSTi: 11
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 119_evpn_access, id: 20, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.119, state: up, Static MAC addresses: 0, MSTi: 12
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 120_evpn_access, id: 21, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.120, state: up, Static MAC addresses: 0, MSTi: 1
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 121_evpn_access, id: 22, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.121, state: up, Static MAC addresses: 0, MSTi: 2
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 122_evpn_access, id: 23, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.122, state: up, Static MAC addresses: 0, MSTi: 3
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 123_evpn_access, id: 24, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.123, state: up, Static MAC addresses: 0, MSTi: 4
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 124_evpn_access, id: 25, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.124, state: up, Static MAC addresses: 0, MSTi: 5
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 125_evpn_access, id: 26, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.125, state: up, Static MAC addresses: 0, MSTi: 6
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 126_evpn_access, id: 27, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.126, state: up, Static MAC addresses: 0, MSTi: 7
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 127_evpn_access, id: 28, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.127, state: up, Static MAC addresses: 0, MSTi: 8
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 128_evpn_access, id: 29, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.128, state: up, Static MAC addresses: 0, MSTi: 9
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 129_evpn_access, id: 30, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.129, state: up, Static MAC addresses: 0, MSTi: 10
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 130_evpn_access, id: 31, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.130, state: up, Static MAC addresses: 0, MSTi: 11
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 131_evpn_access, id: 32, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.131, state: up, Static MAC addresses: 0, MSTi: 12
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 132_evpn_access, id: 33, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.132, state: up, Static MAC addresses: 0, MSTi: 1
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 133_evpn_access, id: 34, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.133, state: up, Static MAC addresses: 0, MSTi: 2
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 134_evpn_access, id: 35, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.134, state: up, Static MAC addresses: 0, MSTi: 3
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 135_evpn_access, id: 36, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.135, state: up, Static MAC addresses: 0, MSTi: 4
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 136_evpn_access, id: 37, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.136, state: up, Static MAC addresses: 0, MSTi: 5
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 137_evpn_access, id: 38, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.137, state: up, Static MAC addresses: 0, MSTi: 6
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 138_evpn_access, id: 39, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.138, state: up, Static MAC addresses: 0, MSTi: 7
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 139_evpn_access, id: 40, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.139, state: up, Static MAC addresses: 0, MSTi: 8
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 140_evpn_access, id: 41, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.140, state: up, Static MAC addresses: 0, MSTi: 9
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 141_evpn_access, id: 42, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.141, state: up, Static MAC addresses: 0, MSTi: 10
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 142_evpn_access, id: 43, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.142, state: up, Static MAC addresses: 0, MSTi: 11
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 143_evpn_access, id: 44, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.143, state: up, Static MAC addresses: 0, MSTi: 12
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 144_evpn_access, id: 45, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.144, state: up, Static MAC addresses: 0, MSTi: 1
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 145_evpn_access, id: 46, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.145, state: up, Static MAC addresses: 0, MSTi: 2
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 146_evpn_access, id: 47, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.146, state: up, Static MAC addresses: 0, MSTi: 3
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 147_evpn_access, id: 48, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.147, state: up, Static MAC addresses: 0, MSTi: 4
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 148_evpn_access, id: 49, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.148, state: up, Static MAC addresses: 0, MSTi: 5
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 149_evpn_access, id: 50, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.149, state: up, Static MAC addresses: 0, MSTi: 6
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 150_evpn_access, id: 51, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.150, state: up, Static MAC addresses: 0, MSTi: 7
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 151_evpn_access, id: 52, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.151, state: up, Static MAC addresses: 0, MSTi: 8
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 152_evpn_access, id: 53, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.152, state: up, Static MAC addresses: 0, MSTi: 9
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 153_evpn_access, id: 54, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.153, state: up, Static MAC addresses: 0, MSTi: 10
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 154_evpn_access, id: 55, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.154, state: up, Static MAC addresses: 0, MSTi: 11
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 155_evpn_access, id: 56, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.155, state: up, Static MAC addresses: 0, MSTi: 12
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 156_evpn_access, id: 57, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.156, state: up, Static MAC addresses: 0, MSTi: 1
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 157_evpn_access, id: 58, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.157, state: up, Static MAC addresses: 0, MSTi: 2
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 158_evpn_access, id: 59, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.158, state: up, Static MAC addresses: 0, MSTi: 3
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 159_evpn_access, id: 60, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.159, state: up, Static MAC addresses: 0, MSTi: 4
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 160_evpn_access, id: 61, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.160, state: up, Static MAC addresses: 0, MSTi: 5
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 161_evpn_access, id: 62, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.161, state: up, Static MAC addresses: 0, MSTi: 6
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 162_evpn_access, id: 63, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.162, state: up, Static MAC addresses: 0, MSTi: 7
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 163_evpn_access, id: 64, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.163, state: up, Static MAC addresses: 0, MSTi: 8
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 164_evpn_access, id: 65, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.164, state: up, Static MAC addresses: 0, MSTi: 9
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 165_evpn_access, id: 66, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.165, state: up, Static MAC addresses: 0, MSTi: 10
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 166_evpn_access, id: 67, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.166, state: up, Static MAC addresses: 0, MSTi: 11
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 167_evpn_access, id: 68, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.167, state: up, Static MAC addresses: 0, MSTi: 12
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 168_evpn_access, id: 69, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.168, state: up, Static MAC addresses: 0, MSTi: 1
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 169_evpn_access, id: 70, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.169, state: up, Static MAC addresses: 0, MSTi: 2
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 170_evpn_access, id: 71, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.170, state: up, Static MAC addresses: 0, MSTi: 3
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 171_evpn_access, id: 72, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.171, state: up, Static MAC addresses: 0, MSTi: 4
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 172_evpn_access, id: 73, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.172, state: up, Static MAC addresses: 0, MSTi: 5
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 173_evpn_access, id: 74, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.173, state: up, Static MAC addresses: 0, MSTi: 6
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 174_evpn_access, id: 75, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.174, state: up, Static MAC addresses: 0, MSTi: 7
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 175_evpn_access, id: 76, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.175, state: up, Static MAC addresses: 0, MSTi: 8
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 176_evpn_access, id: 77, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.176, state: up, Static MAC addresses: 0, MSTi: 9
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 177_evpn_access, id: 78, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.177, state: up, Static MAC addresses: 0, MSTi: 10
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 178_evpn_access, id: 79, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.178, state: up, Static MAC addresses: 0, MSTi: 11
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 179_evpn_access, id: 80, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.179, state: up, Static MAC addresses: 0, MSTi: 12
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 180_evpn_access, id: 81, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.180, state: up, Static MAC addresses: 0, MSTi: 1
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 181_evpn_access, id: 82, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.181, state: up, Static MAC addresses: 0, MSTi: 2
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 182_evpn_access, id: 83, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.182, state: up, Static MAC addresses: 0, MSTi: 3
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 183_evpn_access, id: 84, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.183, state: up, Static MAC addresses: 0, MSTi: 4
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 184_evpn_access, id: 85, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.184, state: up, Static MAC addresses: 0, MSTi: 5
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 185_evpn_access, id: 86, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.185, state: up, Static MAC addresses: 0, MSTi: 6
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 186_evpn_access, id: 87, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.186, state: up, Static MAC addresses: 0, MSTi: 7
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 187_evpn_access, id: 88, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.187, state: up, Static MAC addresses: 0, MSTi: 8
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 188_evpn_access, id: 89, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.188, state: up, Static MAC addresses: 0, MSTi: 9
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 189_evpn_access, id: 90, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.189, state: up, Static MAC addresses: 0, MSTi: 10
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 190_evpn_access, id: 91, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.190, state: up, Static MAC addresses: 0, MSTi: 11
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 191_evpn_access, id: 92, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.191, state: up, Static MAC addresses: 0, MSTi: 12
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 192_evpn_access, id: 93, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.192, state: up, Static MAC addresses: 0, MSTi: 1
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 193_evpn_access, id: 94, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.193, state: up, Static MAC addresses: 0, MSTi: 2
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 194_evpn_access, id: 95, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.194, state: up, Static MAC addresses: 0, MSTi: 3
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 195_evpn_access, id: 96, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.195, state: up, Static MAC addresses: 0, MSTi: 4
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 196_evpn_access, id: 97, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.196, state: up, Static MAC addresses: 0, MSTi: 5
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 197_evpn_access, id: 98, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.197, state: up, Static MAC addresses: 0, MSTi: 6
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 198_evpn_access, id: 99, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.198, state: up, Static MAC addresses: 0, MSTi: 7
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 199_evpn_access, id: 100, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.199, state: up, Static MAC addresses: 0, MSTi: 8
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 200_evpn_access, id: 101, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.200, state: up, Static MAC addresses: 0, MSTi: 9
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 201_evpn_access, id: 102, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.201, state: up, Static MAC addresses: 0, MSTi: 10
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 202_evpn_access, id: 103, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.202, state: up, Static MAC addresses: 0, MSTi: 11
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 203_evpn_access, id: 104, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.203, state: up, Static MAC addresses: 0, MSTi: 12
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 204_evpn_access, id: 105, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.204, state: up, Static MAC addresses: 0, MSTi: 1
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 205_evpn_access, id: 106, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.205, state: up, Static MAC addresses: 0, MSTi: 2
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 206_evpn_access, id: 107, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.206, state: up, Static MAC addresses: 0, MSTi: 3
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 207_evpn_access, id: 108, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.207, state: up, Static MAC addresses: 0, MSTi: 4
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 208_evpn_access, id: 109, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.208, state: up, Static MAC addresses: 0, MSTi: 5
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 209_evpn_access, id: 110, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.209, state: up, Static MAC addresses: 0, MSTi: 6
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 210_evpn_access, id: 111, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.210, state: up, Static MAC addresses: 0, MSTi: 7
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 211_evpn_access, id: 112, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.211, state: up, Static MAC addresses: 0, MSTi: 8
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 212_evpn_access, id: 113, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.212, state: up, Static MAC addresses: 0, MSTi: 9
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 213_evpn_access, id: 114, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.213, state: up, Static MAC addresses: 0, MSTi: 10
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 214_evpn_access, id: 115, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.214, state: up, Static MAC addresses: 0, MSTi: 11
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 215_evpn_access, id: 116, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.215, state: up, Static MAC addresses: 0, MSTi: 12
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 216_evpn_access, id: 117, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.216, state: up, Static MAC addresses: 0, MSTi: 1
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 217_evpn_access, id: 118, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.217, state: up, Static MAC addresses: 0, MSTi: 2
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 218_evpn_access, id: 119, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.218, state: up, Static MAC addresses: 0, MSTi: 3
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 219_evpn_access, id: 120, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.219, state: up, Static MAC addresses: 0, MSTi: 4
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 220_evpn_access, id: 121, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.220, state: up, Static MAC addresses: 0, MSTi: 5
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 221_evpn_access, id: 122, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.221, state: up, Static MAC addresses: 0, MSTi: 6
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 222_evpn_access, id: 123, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.222, state: up, Static MAC addresses: 0, MSTi: 7
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 223_evpn_access, id: 124, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.223, state: up, Static MAC addresses: 0, MSTi: 8
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 224_evpn_access, id: 125, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.224, state: up, Static MAC addresses: 0, MSTi: 9
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 225_evpn_access, id: 126, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.225, state: up, Static MAC addresses: 0, MSTi: 10
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 226_evpn_access, id: 127, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.226, state: up, Static MAC addresses: 0, MSTi: 11
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 227_evpn_access, id: 128, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.227, state: up, Static MAC addresses: 0, MSTi: 12
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 228_evpn_access, id: 129, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.228, state: up, Static MAC addresses: 0, MSTi: 1
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 229_evpn_access, id: 130, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.229, state: up, Static MAC addresses: 0, MSTi: 2
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 230_evpn_access, id: 131, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.230, state: up, Static MAC addresses: 0, MSTi: 3
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 231_evpn_access, id: 132, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.231, state: up, Static MAC addresses: 0, MSTi: 4
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 232_evpn_access, id: 133, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.232, state: up, Static MAC addresses: 0, MSTi: 5
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 233_evpn_access, id: 134, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.233, state: up, Static MAC addresses: 0, MSTi: 6
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 234_evpn_access, id: 135, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.234, state: up, Static MAC addresses: 0, MSTi: 7
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 235_evpn_access, id: 136, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.235, state: up, Static MAC addresses: 0, MSTi: 8
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 236_evpn_access, id: 137, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.236, state: up, Static MAC addresses: 0, MSTi: 9
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 237_evpn_access, id: 138, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.237, state: up, Static MAC addresses: 0, MSTi: 10
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 238_evpn_access, id: 139, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.238, state: up, Static MAC addresses: 0, MSTi: 11
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 239_evpn_access, id: 140, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.239, state: up, Static MAC addresses: 0, MSTi: 12
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 240_evpn_access, id: 141, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.240, state: up, Static MAC addresses: 0, MSTi: 1
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 241_evpn_access, id: 142, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.241, state: up, Static MAC addresses: 0, MSTi: 2
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 242_evpn_access, id: 143, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.242, state: up, Static MAC addresses: 0, MSTi: 3
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 243_evpn_access, id: 144, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.243, state: up, Static MAC addresses: 0, MSTi: 4
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 244_evpn_access, id: 145, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.244, state: up, Static MAC addresses: 0, MSTi: 5
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 245_evpn_access, id: 146, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.245, state: up, Static MAC addresses: 0, MSTi: 6
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 246_evpn_access, id: 147, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.246, state: up, Static MAC addresses: 0, MSTi: 7
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 247_evpn_access, id: 148, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.247, state: up, Static MAC addresses: 0, MSTi: 8
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 248_evpn_access, id: 149, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.248, state: up, Static MAC addresses: 0, MSTi: 9
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 249_evpn_access, id: 150, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.249, state: up, Static MAC addresses: 0, MSTi: 10
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 250_evpn_access, id: 151, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.250, state: up, Static MAC addresses: 0, MSTi: 11
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 251_evpn_access, id: 152, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.251, state: up, Static MAC addresses: 0, MSTi: 12
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 252_evpn_access, id: 153, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.252, state: up, Static MAC addresses: 0, MSTi: 1
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 253_evpn_access, id: 154, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.253, state: up, Static MAC addresses: 0, MSTi: 2
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 254_evpn_access, id: 155, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.254, state: up, Static MAC addresses: 0, MSTi: 3
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 255_evpn_access, id: 156, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.255, state: up, Static MAC addresses: 0, MSTi: 4
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 256_evpn_access, id: 157, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.256, state: up, Static MAC addresses: 0, MSTi: 5
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 257_evpn_access, id: 158, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.257, state: up, Static MAC addresses: 0, MSTi: 6
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 258_evpn_access, id: 159, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.258, state: up, Static MAC addresses: 0, MSTi: 7
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 259_evpn_access, id: 160, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.259, state: up, Static MAC addresses: 0, MSTi: 8
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 260_evpn_access, id: 161, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.260, state: up, Static MAC addresses: 0, MSTi: 9
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 261_evpn_access, id: 162, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.261, state: up, Static MAC addresses: 0, MSTi: 10
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 262_evpn_access, id: 163, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.262, state: up, Static MAC addresses: 0, MSTi: 11
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 263_evpn_access, id: 164, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.263, state: up, Static MAC addresses: 0, MSTi: 12
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 264_evpn_access, id: 165, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.264, state: up, Static MAC addresses: 0, MSTi: 1
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 265_evpn_access, id: 166, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.265, state: up, Static MAC addresses: 0, MSTi: 2
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 266_evpn_access, id: 167, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.266, state: up, Static MAC addresses: 0, MSTi: 3
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 267_evpn_access, id: 168, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.267, state: up, Static MAC addresses: 0, MSTi: 4
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 268_evpn_access, id: 169, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.268, state: up, Static MAC addresses: 0, MSTi: 5
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 269_evpn_access, id: 170, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.269, state: up, Static MAC addresses: 0, MSTi: 6
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 270_evpn_access, id: 171, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.270, state: up, Static MAC addresses: 0, MSTi: 7
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 271_evpn_access, id: 172, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.271, state: up, Static MAC addresses: 0, MSTi: 8
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 272_evpn_access, id: 173, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.272, state: up, Static MAC addresses: 0, MSTi: 9
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 273_evpn_access, id: 174, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.273, state: up, Static MAC addresses: 0, MSTi: 10
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 274_evpn_access, id: 175, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.274, state: up, Static MAC addresses: 0, MSTi: 11
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 275_evpn_access, id: 176, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.275, state: up, Static MAC addresses: 0, MSTi: 12
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 276_evpn_access, id: 177, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.276, state: up, Static MAC addresses: 0, MSTi: 1
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 277_evpn_access, id: 178, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.277, state: up, Static MAC addresses: 0, MSTi: 2
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 278_evpn_access, id: 179, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.278, state: up, Static MAC addresses: 0, MSTi: 3
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 279_evpn_access, id: 180, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.279, state: up, Static MAC addresses: 0, MSTi: 4
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 280_evpn_access, id: 181, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.280, state: up, Static MAC addresses: 0, MSTi: 5
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 281_evpn_access, id: 182, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.281, state: up, Static MAC addresses: 0, MSTi: 6
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 282_evpn_access, id: 183, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.282, state: up, Static MAC addresses: 0, MSTi: 7
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 283_evpn_access, id: 184, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.283, state: up, Static MAC addresses: 0, MSTi: 8
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 284_evpn_access, id: 185, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.284, state: up, Static MAC addresses: 0, MSTi: 9
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 285_evpn_access, id: 186, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.285, state: up, Static MAC addresses: 0, MSTi: 10
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 286_evpn_access, id: 187, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.286, state: up, Static MAC addresses: 0, MSTi: 11
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 287_evpn_access, id: 188, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.287, state: up, Static MAC addresses: 0, MSTi: 12
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 288_evpn_access, id: 189, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.288, state: up, Static MAC addresses: 0, MSTi: 1
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 289_evpn_access, id: 190, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.289, state: up, Static MAC addresses: 0, MSTi: 2
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 290_evpn_access, id: 191, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.290, state: up, Static MAC addresses: 0, MSTi: 3
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 291_evpn_access, id: 192, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.291, state: up, Static MAC addresses: 0, MSTi: 4
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 292_evpn_access, id: 193, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.292, state: up, Static MAC addresses: 0, MSTi: 5
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 293_evpn_access, id: 194, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.293, state: up, Static MAC addresses: 0, MSTi: 6
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 294_evpn_access, id: 195, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.294, state: up, Static MAC addresses: 0, MSTi: 7
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 295_evpn_access, id: 196, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.295, state: up, Static MAC addresses: 0, MSTi: 8
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 296_evpn_access, id: 197, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.296, state: up, Static MAC addresses: 0, MSTi: 9
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 297_evpn_access, id: 198, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.297, state: up, Static MAC addresses: 0, MSTi: 10
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 298_evpn_access, id: 199, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.298, state: up, Static MAC addresses: 0, MSTi: 11
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 299_evpn_access, id: 200, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.299, state: up, Static MAC addresses: 0, MSTi: 12
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 300_evpn_access, id: 201, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.300, state: up, Static MAC addresses: 0, MSTi: 1
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 1994_evpn_access, id: 202, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 1000, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 2 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            BV900, state: down, BVI MAC addresses: 1
            Gi0/4/0/6.1994, state: up, Static MAC addresses: 0, MSTi: 3
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_access, bridge-domain: 2112_evpn_access, id: 203, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 1000, Action: limit, no-flood, Notification: syslog, trap
        Filter MAC addresses: 0
        ACs: 1 (1 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            Gi0/4/0/6.900, state: up, Static MAC addresses: 0, MSTi: 1
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: evpn_fortinet, bridge-domain: evpn_fortinet, id: 204, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 4000, Action: none, Notification: syslog
        Filter MAC addresses: 0
        ACs: 3 (3 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of EVPNs:
            EVPN, state: up
        List of ACs:
            BV19, state: up, BVI MAC addresses: 1
            BE1.19, state: up, Static MAC addresses: 0, MSTi: 8
            BE3.19, state: up, Static MAC addresses: 0, MSTi: 8
        List of Access PWs:
        List of VFIs:
        List of Access VFIs:
        Bridge group: E911-v2535-vpls, bridge-domain: bd60, id: 205, state: up, ShgId: 0, MSTi: 0
        Aging: 300 s, MAC limit: 4000, Action: none, Notification: syslog
        Filter MAC addresses: 0
        ACs: 2 (2 up), VFIs: 1, PWs: 1 (1 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        List of ACs:
            BV60, state: up, BVI MAC addresses: 1
            Gi0/4/0/1.60, state: up, Static MAC addresses: 0
        List of Access PWs:
        List of VFIs:
            VFI vfi60 (up)
            Neighbor 67.70.219.150 pw-id 100200, state: up, Static MAC addresses: 0
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
                    '0001.0000.0002': {
                        'lc_learned': 'N/A',
                        'learned_from': 'Te0/0/1/0/3.3',
                        'mapped_to': 'N/A',
                        'resync_age': '0d '
                                      '0h '
                                      '0m '
                                      '14s',
                        'type': 'dynamic'},
                    '0001.0000.0003': {
                        'lc_learned': 'N/A',
                        'learned_from': 'Te0/0/1/0/3.3',
                        'mapped_to': 'N/A',
                        'resync_age': '0d '
                                      '0h '
                                      '0m '
                                      '14s',
                        'type': 'dynamic'},
                    '0001.0000.0004': {
                        'lc_learned': 'N/A',
                        'learned_from': 'Te0/0/1/0/3.3',
                        'mapped_to': 'N/A',
                        'resync_age': '0d '
                                      '0h '
                                      '0m '
                                      '14s',
                        'type': 'dynamic'},
                    '0001.0000.0005': {
                        'lc_learned': 'N/A',
                        'learned_from': 'Te0/0/1/0/3.3',
                        'mapped_to': 'N/A',
                        'resync_age': '0d '
                                      '0h '
                                      '0m '
                                      '14s',
                        'type': 'dynamic'},
                    '0001.0000.0006': {
                        'lc_learned': 'N/A',
                        'learned_from': 'Te0/0/1/0/3.3',
                        'mapped_to': 'N/A',
                        'resync_age': '0d '
                                      '0h '
                                      '0m '
                                      '14s',
                        'type': 'dynamic'},
                    '0001.0000.0007': {
                        'lc_learned': 'N/A',
                        'learned_from': 'Te0/0/1/0/3.3',
                        'mapped_to': 'N/A',
                        'resync_age': '0d '
                                      '0h '
                                      '0m '
                                      '14s',
                        'type': 'dynamic'},
                    '0001.0000.0008': {
                        'lc_learned': 'N/A',
                        'learned_from': 'Te0/0/1/0/3.3',
                        'mapped_to': 'N/A',
                        'resync_age': '0d '
                                      '0h '
                                      '0m '
                                      '14s',
                        'type': 'dynamic'},
                    '0001.0000.0009': {
                        'lc_learned': 'N/A',
                        'learned_from': 'Te0/0/1/0/3.3',
                        'mapped_to': 'N/A',
                        'resync_age': '0d '
                                      '0h '
                                      '0m '
                                      '14s',
                        'type': 'dynamic'},
                     '0001.0000.000a': {
                        'lc_learned': 'N/A',
                        'learned_from': 'Te0/0/1/0/3.3',
                        'mapped_to': 'N/A',
                        'resync_age': '0d '
                                      '0h '
                                      '0m '
                                      '14s',
                        'type': 'dynamic'},
                    '0001.0000.000b': {
                        'lc_learned': 'N/A',
                        'learned_from': 'Te0/0/1/0/3.3',
                        'mapped_to': 'N/A',
                        'resync_age': '0d '
                                      '0h '
                                      '0m '
                                      '14s',
                        'type': 'dynamic'},
                    '0001.0000.000c': {
                        'lc_learned': 'N/A',
                        'learned_from': 'Te0/0/1/0/3.3',
                        'mapped_to': 'N/A',
                        'resync_age': '0d '
                                      '0h '
                                      '0m '
                                      '14s',
                        'type': 'dynamic'},
                    '0001.0000.000d': {
                        'lc_learned': 'N/A',
                        'learned_from': 'Te0/0/1/0/3.3',
                        'mapped_to': 'N/A',
                        'resync_age': '0d '
                                      '0h '
                                      '0m '
                                      '14s',
                        'type': 'dynamic'},
                    '0001.0000.000e': {
                        'lc_learned': 'N/A',
                        'learned_from': 'Te0/0/1/0/3.3',
                        'mapped_to': 'N/A',
                        'resync_age': '0d '
                                      '0h '
                                      '0m '
                                      '14s',
                        'type': 'dynamic'},
                    '0001.0000.000f': {
                        'lc_learned': 'N/A',
                        'learned_from': 'Te0/0/1/0/3.3',
                        'mapped_to': 'N/A',
                        'resync_age': '0d '
                                      '0h '
                                      '0m '
                                      '14s',
                        'type': 'dynamic'},
                    '0001.0000.0010': {
                        'lc_learned': 'N/A',
                        'learned_from': 'Te0/0/1/0/3.3',
                        'mapped_to': 'N/A',
                        'resync_age': '0d '
                                      '0h '
                                      '0m '
                                      '14s',
                        'type': 'dynamic'},
                    '0001.0000.0011': {
                        'lc_learned': 'N/A',
                        'learned_from': 'Te0/0/1/0/3.3',
                        'mapped_to': 'N/A',
                        'resync_age': '0d '
                                      '0h '
                                      '0m '
                                      '14s',
                        'type': 'dynamic'},
                    '0001.0000.0012': {
                        'lc_learned': 'N/A',
                        'learned_from': 'Te0/0/1/0/3.3',
                        'mapped_to': 'N/A',
                        'resync_age': '0d '
                                      '0h '
                                      '0m '
                                      '14s',
                        'type': 'dynamic'},
                    '0001.0000.0013': {
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
        0001.0000.0002 dynamic Te0/0/1/0/3.3 N/A 0d 0h 0m 14s N/A 
        0001.0000.0003 dynamic Te0/0/1/0/3.3 N/A 0d 0h 0m 14s N/A 
        0001.0000.0004 dynamic Te0/0/1/0/3.3 N/A 0d 0h 0m 14s N/A 
        0001.0000.0005 dynamic Te0/0/1/0/3.3 N/A 0d 0h 0m 14s N/A 
        0001.0000.0006 dynamic Te0/0/1/0/3.3 N/A 0d 0h 0m 14s N/A 
        0001.0000.0007 dynamic Te0/0/1/0/3.3 N/A 0d 0h 0m 14s N/A 
        0001.0000.0008 dynamic Te0/0/1/0/3.3 N/A 0d 0h 0m 14s N/A 
        0001.0000.0009 dynamic Te0/0/1/0/3.3 N/A 0d 0h 0m 14s N/A 
        0001.0000.000a dynamic Te0/0/1/0/3.3 N/A 0d 0h 0m 14s N/A 
        0001.0000.000b dynamic Te0/0/1/0/3.3 N/A 0d 0h 0m 14s N/A 
        0001.0000.000c dynamic Te0/0/1/0/3.3 N/A 0d 0h 0m 14s N/A 
        0001.0000.000d dynamic Te0/0/1/0/3.3 N/A 0d 0h 0m 14s N/A 
        0001.0000.000e dynamic Te0/0/1/0/3.3 N/A 0d 0h 0m 14s N/A 
        0001.0000.000f dynamic Te0/0/1/0/3.3 N/A 0d 0h 0m 14s N/A 
        0001.0000.0010 dynamic Te0/0/1/0/3.3 N/A 0d 0h 0m 14s N/A 
        0001.0000.0011 dynamic Te0/0/1/0/3.3 N/A 0d 0h 0m 14s N/A 
        0001.0000.0012 dynamic Te0/0/1/0/3.3 N/A 0d 0h 0m 14s N/A 
        0001.0000.0013 dynamic Te0/0/1/0/3.3 N/A 0d 0h 0m 14s N/A
    '''}

    golden_parsed_output_1 = {
        'mac_table': {
            '(10.25.40.40, 10007)': {
                'mac_address': {
                    '0021.0001.0002': {
                        'lc_learned': 'N/A',
                        'learned_from': '(10.25.40.40, '
                                       '10007)',
                        'mapped_to': 'N/A',
                        'resync_age': '14 '
                                     'Mar '
                                     '12:46:04',
                        'type': 'dynamic'},
                    '1234.0001.0005': {'lc_learned': 'N/A',
                        'learned_from': '(10.25.40.40, '
                                       '10007)',
                        'mapped_to': 'N/A',
                        'resync_age': 'N/A',
                        'type': 'static'}
                }
            },
            'BD id:0': {
                'mac_address': {
                    '0021.0001.0001': {
                        'lc_learned': 'N/A',
                                      'learned_from': 'BD '
                                                      'id:0',
                                      'mapped_to': 'N/A',
                                      'resync_age': 'N/A',
                                      'type': 'EVPN'},
                    '0021.0001.0003': {'lc_learned': 'N/A',
                                      'learned_from': 'BD '
                                                      'id:0',
                                      'mapped_to': 'N/A',
                                      'resync_age': 'N/A',
                                      'type': 'EVPN'},
                    '0021.0001.0004': {'lc_learned': 'N/A',
                                      'learned_from': 'BD '
                                                      'id:0',
                                      'mapped_to': 'N/A',
                                      'resync_age': 'N/A',
                                      'type': 'EVPN'},
                    '0021.0001.0005': {'lc_learned': 'N/A',
                                      'learned_from': 'BD '
                                                      'id:0',
                                      'mapped_to': 'N/A',
                                      'resync_age': 'N/A',
                                      'type': 'EVPN'},
                    '1234.0001.0001': {'lc_learned': 'N/A',
                                      'learned_from': 'BD '
                                                      'id:0',
                                      'mapped_to': 'N/A',
                                      'resync_age': 'N/A',
                                      'type': 'EVPN'},
                    '1234.0001.0002': {'lc_learned': 'N/A',
                                      'learned_from': 'BD '
                                                      'id:0',
                                      'mapped_to': 'N/A',
                                      'resync_age': 'N/A',
                                      'type': 'EVPN'},
                    '1234.0001.0003': {'lc_learned': 'N/A',
                                      'learned_from': 'BD '
                                                      'id:0',
                                      'mapped_to': 'N/A',
                                      'resync_age': 'N/A',
                                      'type': 'EVPN'},
                    '1234.0001.0004': {'lc_learned': 'N/A',
                                      'learned_from': 'BD '
                                                      'id:0',
                                      'mapped_to': 'N/A',
                                      'resync_age': 'N/A',
                                      'type': 'EVPN'}
                }
            },
            'BE1.2': {
                'mac_address': {
                    '0021.0002.0005': {
                        'lc_learned': 'N/A',
                        'learned_from': 'BE1.2',
                        'mapped_to': 'N/A',
                        'resync_age': '14 '
                                      'Mar '
                                      '12:46:04',
                        'type': 'dynamic'},
                    '1234.0002.0004': {
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
        0021.0001.0001 EVPN    BD id: 0                    N/A        N/A                    N/A
        0021.0001.0003 EVPN    BD id: 0                    N/A        N/A                    N/A
        0021.0001.0004 EVPN    BD id: 0                    N/A        N/A                    N/A
        0021.0001.0005 EVPN    BD id: 0                    N/A        N/A                    N/A
        1234.0001.0001 EVPN    BD id: 0                    N/A        N/A                    N/A
        1234.0001.0002 EVPN    BD id: 0                    N/A        N/A                    N/A
        1234.0001.0003 EVPN    BD id: 0                    N/A        N/A                    N/A
        1234.0001.0004 EVPN    BD id: 0                    N/A        N/A                    N/A
        0021.0001.0002 dynamic (10.25.40.40, 10007)        N/A        14 Mar 12:46:04        N/A
        1234.0001.0005 static  (10.25.40.40, 10007)        N/A        N/A                    N/A
        0021.0002.0005 dynamic BE1.2                       N/A        14 Mar 12:46:04        N/A
        1234.0002.0004 static  BE1.2                       N/A        N/A                    N/A
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
                                    'static_mac_address': ['0000.0000.0000', '0001.0002.0003'],
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
                0001.0002.0003
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
                    'EVPN-Multicast-BTV': {
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
                                    'bvi_mac_address': ['1000.1000.1000'],
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
        Bridge group: EVPN-Mulicast, bridge-domain: EVPN-Multicast-BTV, id: 0, state: up, ShgId: 0, MSTi: 0
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
                1000.1000.1000
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
                00c1.6474.81ca
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
        Bridge group: EVPN-Mulicast, bridge-domain: EVPN-Multicast-BTV, id: 1, state: up, ShgId: 0, MSTi: 0
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
                1000.1000.1000
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
                        'split_horizon_group': 'Access',
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
                                    'bvi_mac_address': ['00c1.6474.81ca'],
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
                    'EVPN-Multicast-BTV': {
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
                                    'bvi_mac_address': ['1000.1000.1000'],
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
        
if __name__ == '__main__':
    unittest.main()