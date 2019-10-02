# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

# iosxr show_mrib
from genie.libs.parser.iosxr.show_l2vpn import (ShowL2vpnBridgeDomain,
                                                ShowL2vpnBridgeDomainSummary,
                                                ShowL2vpnBridgeDomainBrief,
                                                ShowL2vpnBridgeDomainDetail)

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
                            'ac': 1,
                            'ac_up': 1,
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
                            'broadcast': 'enabled',
                            'multicast': 'enabled',
                            'unknown_unicast': 'enabled',
                        },
                        'mac_aging_time': 300,
                        'type': 'inactivity',
                        'mac_limit': 4000,
                        'action': 'none',
                        'notification': 'syslog',
                        'mac_limit_reached': 'yes',
                        'security': 'disabled',
                        'dhcp_v4_snooping': 'disabled',
                        'mtu': 1500,
                        'ac': {
                            'ac': 1,
                            'ac_up': 1,
                            'interfaces': {
                                'GigabitEthernet0/1/0/0': {
                                    'state': 'up',
                                    'type': 'inactivity',
                                    'mtu': 1500,
                                    'xc_id': '0x2000001',
                                    'interworking': 'none',
                                    'mst_i': 0,
                                    'mst_i_state': 'unprotected',
                                    'mac_learning': 'enabled',
                                    'flooding': {
                                        'broadcast': 'enabled',
                                        'multicast': 'enabled',
                                        'unknown_unicast': 'enabled',
                                    },
                                    'mac_aging_time': 300,
                                    'mac_limit': 4000,
                                    'action': 'none',
                                    'notification': 'syslog',
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
                            'vfi': 1,
                            '1': {
                                'neighbor': {
                                    '1.1.1.1': {
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
                                                'pw_backup': 'disable',
                                                'delay': 0,
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
                                                'vfi_statistics': {
                                                    'drops': 'illegal',
                                                    'vlan': 0,
                                                    'illegal_length': 0,
                                                },
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
            PW: neighbor 1.1.1.1, PW ID 1, state is up ( established )
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
                        'mtu': 1500,
                        'ac': {
                            'ac': 1,
                            'ac_up': 0,
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
                            'vfi': 1,
                            'foo_vfi': {
                                'neighbor': {
                                    '1.1.1.1': {
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
                                                'vfi_statistics': {
                                                    'drops': 'illegal',
                                                    'vlan': 0,
                                                    'illegal_length': 0,
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                        'pw': {
                            'pw': 2,
                            'pw_up': 2,
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
            PW: neighbor 1.1.1.1, PW ID 1, state is up ( established )
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
            PW: neighbor 1.1.1.1, PW ID 2, state is up ( established )
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

if __name__ == '__main__':
    unittest.main()
