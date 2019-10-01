# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

# iosxr show_mrib
from genie.libs.parser.iosxr.show_l2vpn import (ShowL2vpnBridgeDomain, ShowL2vpnForwardingProtectionMainInterface)

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
                        'aging': 300,
                        'mac_limit': 4000,
                        'action': 'none',
                        'notification': 'syslog',
                        'filter_mac_address': 0,
                        'ac': {
                            'ac': 1,
                            'ac_up': 1,
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
                            'vfi': 1,
                            1: {
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
                            'pw': 1,
                            'pw_up': 1,
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

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowL2vpnForwardingProtectionMainInterface(device=self.device)
        parsed_output = obj.parse(location='0/1/0')
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowL2vpnForwardingProtectionMainInterface(device=self.device)
        parsed_output = obj.parse(location='0/2/1')
        self.assertEqual(parsed_output, self.golden_parsed_output_1)


if __name__ == '__main__':
    unittest.main()
