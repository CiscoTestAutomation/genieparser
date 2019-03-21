#!/bin/env python
import unittest
from unittest.mock import Mock
from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                             SchemaMissingKeyError

from genie.libs.parser.iosxe.show_l2vpn import ShowBridgeDomain, \
                                               ShowEthernetServiceInstanceDetail

# import parser utils
from genie.libs.parser.utils.common import format_output


class test_show_bridge_domain(unittest.TestCase):

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output_full = {
        'bridge_domain': {
            2051: {
                'state': 'UP',
                'member_ports': ['vfi VPLS-2051 neighbor 27.93.202.64 2051', 'Port-channel1 service instance 2051'],
                'bd_domain_id': 2051,
                'aging_timer': 3600,
                'mac_table': {
                    'VPLS-2051.10200e6': {
                        'pseudoport': 'VPLS-2051.10200e6',
                        'mac_address': {
                            '0000.57C4.A8D9': {
                                'tag': 'dynamic',
                                'mac_address': '0000.57C4.A8D9',
                                'age': 3153,
                                'policy': 'forward',
                                'aed': 0,
                                },
                            },
                        },
                    'Port-channel1.EFP2051': {
                        'pseudoport': 'Port-channel1.EFP2051',
                        'mac_address': {
                            '0000.A000.0027': {
                                'tag': 'dynamic',
                                'mac_address': '0000.A000.0027',
                                'age': 3142,
                                'policy': 'forward',
                                'aed': 0,
                                },
                            '0000.A000.0097': {
                                'tag': 'dynamic',
                                'mac_address': '0000.A000.0097',
                                'age': 3153,
                                'policy': 'forward',
                                'aed': 0,
                                },
                            '0000.A000.013A': {
                                'tag': 'dynamic',
                                'mac_address': '0000.A000.013A',
                                'age': 3137,
                                'policy': 'forward',
                                'aed': 0,
                                },
                            '0000.A000.00BF': {
                                'tag': 'dynamic',
                                'mac_address': '0000.A000.00BF',
                                'age': 3125,
                                'policy': 'forward',
                                'aed': 0,
                                },
                            '0000.A000.010C': {
                                'tag': 'dynamic',
                                'mac_address': '0000.A000.010C',
                                'age': 3133,
                                'policy': 'forward',
                                'aed': 0,
                                },
                            '0000.A000.010F': {
                                'tag': 'dynamic',
                                'mac_address': '0000.A000.010F',
                                'age': 3133,
                                'policy': 'forward',
                                'aed': 0,
                                },
                            },
                        },
                    },
                'mac_learning_state': 'Enabled',
                'split-horizon_group': {
                    '0': {
                        'interfaces': ['Port-channel1 service instance 2051'],
                        'num_of_ports': '1',
                        },
                    },
                'number_of_ports_in_all': 2,
                },
            2052: {
                'state': 'UP',
                'member_ports': ['vfi VPLS-2052 neighbor 27.93.202.64 2052', 'Port-channel1 service instance 2052'],
                'bd_domain_id': 2052,
                'aging_timer': 3600,
                'mac_table': {
                    'Port-channel1.EFP2052': {
                        'pseudoport': 'Port-channel1.EFP2052',
                        'mac_address': {
                            '0000.A000.002C': {
                                'tag': 'dynamic',
                                'mac_address': '0000.A000.002C',
                                'age': 3143,
                                'policy': 'forward',
                                'aed': 0,
                                },
                            '0000.A000.0015': {
                                'tag': 'dynamic',
                                'mac_address': '0000.A000.0015',
                                'age': 3141,
                                'policy': 'forward',
                                'aed': 0,
                                },
                            },
                        },
                    },
                'mac_learning_state': 'Enabled',
                'split-horizon_group': {
                    '0': {
                        'interfaces': ['Port-channel1 service instance 2052'],
                        'num_of_ports': '1',
                        },
                    },
                'number_of_ports_in_all': 2,
                },
            },
        }

    golden_output_full = {'execute.return_value': '''\
        Router#show bridge-domain
        Load for five secs: 55%/0%; one minute: 15%; five minutes: 10%
        Time source is NTP, 20:29:29.871 JST Fri Nov 11 2016

        Bridge-domain 2051 (2 ports in all)
        State: UP                    Mac learning: Enabled
        Aging-Timer: 3600 second(s)
            vfi VPLS-2051 neighbor 27.93.202.64 2051
        1 ports belonging to split-horizon group 0
            Port-channel1 service instance 2051 (split-horizon)
           AED MAC address    Policy  Tag       Age  Pseudoport
           0   0000.A000.0027 forward dynamic   3142 Port-channel1.EFP2051
           0   0000.A000.00BF forward dynamic   3125 Port-channel1.EFP2051
           0   0000.A000.013A forward dynamic   3137 Port-channel1.EFP2051
           0   0000.A000.010F forward dynamic   3133 Port-channel1.EFP2051
           0   0000.57C4.A8D9 forward dynamic   3153 VPLS-2051.10200e6
           0   0000.A000.0097 forward dynamic   3153 Port-channel1.EFP2051
           0   0000.A000.010C forward dynamic   3133 Port-channel1.EFP2051

        Bridge-domain 2052 (2 ports in all)
        State: UP                    Mac learning: Enabled
        Aging-Timer: 3600 second(s)
            vfi VPLS-2052 neighbor 27.93.202.64 2052
        1 ports belonging to split-horizon group 0
            Port-channel1 service instance 2052 (split-horizon)
           AED MAC address    Policy  Tag       Age  Pseudoport
           0   0000.A000.0015 forward dynamic   3141 Port-channel1.EFP2052
           0   0000.A000.002C forward dynamic   3143 Port-channel1.EFP2052
    '''
    }

    golden_parsed_output_bridge_domain = {
        'bridge_domain': {
            3051: {
                'number_of_ports_in_all': 2,
                'state': 'UP',
                'member_ports': ['vfi VPLS-3051 neighbor 202.239.165.220 3051', 'GigabitEthernet0/0/3 service instance 3051'],
                'mac_table': {
                    'GigabitEthernet0/0/3.EFP3051': {
                        'pseudoport': 'GigabitEthernet0/0/3.EFP3051',
                        'mac_address': {
                            '0000.A000.0118': {
                                'tag': 'dynamic',
                                'age': 3441,
                                'aed': 0,
                                'mac_address': '0000.A000.0118',
                                'policy': 'forward',
                                },
                            '0000.A000.0077': {
                                'tag': 'dynamic',
                                'age': 3426,
                                'aed': 0,
                                'mac_address': '0000.A000.0077',
                                'policy': 'forward',
                                },
                            '0000.A000.011C': {
                                'tag': 'dynamic',
                                'age': 3442,
                                'aed': 0,
                                'mac_address': '0000.A000.011C',
                                'policy': 'forward',
                                },
                            '0000.A000.001F': {
                                'tag': 'dynamic',
                                'age': 3416,
                                'aed': 0,
                                'mac_address': '0000.A000.001F',
                                'policy': 'forward',
                                },
                            '0000.A000.0068': {
                                'tag': 'dynamic',
                                'age': 3424,
                                'aed': 0,
                                'mac_address': '0000.A000.0068',
                                'policy': 'forward',
                                },
                            '0000.A000.00C5': {
                                'tag': 'dynamic',
                                'age': 3433,
                                'aed': 0,
                                'mac_address': '0000.A000.00C5',
                                'policy': 'forward',
                                },
                            '0000.A000.0108': {
                                'tag': 'dynamic',
                                'age': 3440,
                                'aed': 0,
                                'mac_address': '0000.A000.0108',
                                'policy': 'forward',
                                },
                            '0000.A000.0010': {
                                'tag': 'dynamic',
                                'age': 3415,
                                'aed': 0,
                                'mac_address': '0000.A000.0010',
                                'policy': 'forward',
                                },
                            '0000.A000.000F': {
                                'tag': 'dynamic',
                                'age': 3415,
                                'aed': 0,
                                'mac_address': '0000.A000.000F',
                                'policy': 'forward',
                                },
                            '0000.A000.007F': {
                                'tag': 'dynamic',
                                'age': 3426,
                                'aed': 0,
                                'mac_address': '0000.A000.007F',
                                'policy': 'forward',
                                },
                            '0000.A000.007B': {
                                'tag': 'dynamic',
                                'age': 3426,
                                'aed': 0,
                                'mac_address': '0000.A000.007B',
                                'policy': 'forward',
                                },
                            '0000.A000.0087': {
                                'tag': 'dynamic',
                                'age': 3427,
                                'aed': 0,
                                'mac_address': '0000.A000.0087',
                                'policy': 'forward',
                                },
                            '0000.A000.00AA': {
                                'tag': 'dynamic',
                                'age': 3430,
                                'aed': 0,
                                'mac_address': '0000.A000.00AA',
                                'policy': 'forward',
                                },
                            '0000.A000.012C': {
                                'tag': 'dynamic',
                                'age': 3443,
                                'aed': 0,
                                'mac_address': '0000.A000.012C',
                                'policy': 'forward',
                                },
                            '0000.A000.00D0': {
                                'tag': 'dynamic',
                                'age': 3434,
                                'aed': 0,
                                'mac_address': '0000.A000.00D0',
                                'policy': 'forward',
                                },
                            '0000.A000.00F6': {
                                'tag': 'dynamic',
                                'age': 3438,
                                'aed': 0,
                                'mac_address': '0000.A000.00F6',
                                'policy': 'forward',
                                },
                            '0000.A000.00F7': {
                                'tag': 'dynamic',
                                'age': 3438,
                                'aed': 0,
                                'mac_address': '0000.A000.00F7',
                                'policy': 'forward',
                                },
                            '0000.A000.00F2': {
                                'tag': 'dynamic',
                                'age': 3438,
                                'aed': 0,
                                'mac_address': '0000.A000.00F2',
                                'policy': 'forward',
                                },
                            '0000.A000.0129': {
                                'tag': 'dynamic',
                                'age': 3443,
                                'aed': 0,
                                'mac_address': '0000.A000.0129',
                                'policy': 'forward',
                                },
                            },
                        },
                    },
                'aging_timer': 3600,
                'bd_domain_id': 3051,
                'split-horizon_group': {
                    '0': {
                        'num_of_ports': '1',
                        'interfaces': ['GigabitEthernet0/0/3 service instance 3051'],
                        },
                    },
                'mac_learning_state': 'Enabled',
                },
            },
        }


    golden_output_bridge_domain = {'execute.return_value': '''\
        Router#show bridge-domain 3051
        Load for five secs: 10%/1%; one minute: 11%; five minutes: 12%
        Time source is NTP, 19:54:46.940 JST Wed Nov 2 2016

        Bridge-domain 3051 (2 ports in all)
        State: UP                    Mac learning: Enabled
        Aging-Timer: 3600 second(s)
            vfi VPLS-3051 neighbor 202.239.165.220 3051
        1 ports belonging to split-horizon group 0
            GigabitEthernet0/0/3 service instance 3051 (split-horizon)
           AED MAC address    Policy  Tag       Age  Pseudoport
           0   0000.A000.00F2 forward dynamic   3438 GigabitEthernet0/0/3.EFP3051
           0   0000.A000.00AA forward dynamic   3430 GigabitEthernet0/0/3.EFP3051
           0   0000.A000.0077 forward dynamic   3426 GigabitEthernet0/0/3.EFP3051
           0   0000.A000.00D0 forward dynamic   3434 GigabitEthernet0/0/3.EFP3051
           0   0000.A000.001F forward dynamic   3416 GigabitEthernet0/0/3.EFP3051
           0   0000.A000.0129 forward dynamic   3443 GigabitEthernet0/0/3.EFP3051
           0   0000.A000.00F6 forward dynamic   3438 GigabitEthernet0/0/3.EFP3051
           0   0000.A000.007B forward dynamic   3426 GigabitEthernet0/0/3.EFP3051
           0   0000.A000.0068 forward dynamic   3424 GigabitEthernet0/0/3.EFP3051
           0   0000.A000.00C5 forward dynamic   3433 GigabitEthernet0/0/3.EFP3051
           0   0000.A000.0087 forward dynamic   3427 GigabitEthernet0/0/3.EFP3051
           0   0000.A000.00F7 forward dynamic   3438 GigabitEthernet0/0/3.EFP3051
           0   0000.A000.0118 forward dynamic   3441 GigabitEthernet0/0/3.EFP3051
           0   0000.A000.0108 forward dynamic   3440 GigabitEthernet0/0/3.EFP3051
           0   0000.A000.007F forward dynamic   3426 GigabitEthernet0/0/3.EFP3051
           0   0000.A000.011C forward dynamic   3442 GigabitEthernet0/0/3.EFP3051
           0   0000.A000.012C forward dynamic   3443 GigabitEthernet0/0/3.EFP3051
           0   0000.A000.0010 forward dynamic   3415 GigabitEthernet0/0/3.EFP3051
           0   0000.A000.000F forward dynamic   3415 GigabitEthernet0/0/3.EFP3051
    '''
    }

    golden_parsed_output_count = {'lines_match_regexp': 32102}

    golden_output_count = {'execute.return_value': '''\
        Router#show bridge-domain | count Port-channel1\.EFP2.*
        Number of lines which match regexp = 32102
    '''
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        platform_obj = ShowBridgeDomain(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = platform_obj.parse()    

    def test_golden_full(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_full)
        platform_obj = ShowBridgeDomain(device=self.device)
        parsed_output = platform_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_full)

    def test_golden_bridge_domain(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_bridge_domain)
        platform_obj = ShowBridgeDomain(device=self.device)
        parsed_output = platform_obj.parse(bd_id='3051')
        self.assertEqual(parsed_output, self.golden_parsed_output_bridge_domain)

    def test_golden_count(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_count)
        platform_obj = ShowBridgeDomain(device=self.device)
        parsed_output = platform_obj.parse(word='Port-channel1\.EFP2.*')
        self.assertEqual(parsed_output, self.golden_parsed_output_count)


class test_show_ethernet_service_instance_detail(unittest.TestCase):

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {'service_instance': {2051: {'associated_evc': 'L2protocol drop',
                             'associated_interface': 'GigabitEthernet0/0/3',
                             'description': 'xxx',
                             'dot1q_tunnel_ethertype': '0x8100',
                             'efp_statistics': {'bytes_in': 0,
                                                'bytes_out': 0,
                                                'pkts_in': 0,
                                                'pkts_out': 0},
                             'encapsulation': 'dot1q 2051 vlan protocol '
                                              'type 0x8100',
                             'id': 2051,
                             'rewrite': 'egress tag translate 1-to-1 dot1q '
                                        '2051 vlan-type 0x8100',
                             'state': 'Up',
                             'type': 'Static'},
                      2052: {'associated_evc': 'L2protocol drop',
                             'associated_interface': 'GigabitEthernet0/0/3',
                             'description': 'xxx',
                             'dot1q_tunnel_ethertype': '0x8100',
                             'efp_statistics': {'bytes_in': 0,
                                                'bytes_out': 0,
                                                'pkts_in': 0,
                                                'pkts_out': 0},
                             'encapsulation': 'dot1q 2052 vlan protocol '
                                              'type 0x8100',
                             'id': 2052,
                             'rewrite': 'egress tag translate 1-to-1 dot1q '
                                        '2052 vlan-type 0x8100',
                             'state': 'Up',
                             'type': 'Static'},
                      2053: {'associated_evc': 'L2protocol drop',
                             'associated_interface': 'GigabitEthernet0/0/3',
                             'description': 'xxx',
                             'dot1q_tunnel_ethertype': '0x8100',
                             'efp_statistics': {'bytes_in': 0,
                                                'bytes_out': 0,
                                                'pkts_in': 0,
                                                'pkts_out': 0},
                             'encapsulation': 'dot1q 2053 vlan protocol '
                                              'type 0x8100',
                             'id': 2053,
                             'rewrite': 'egress tag translate 1-to-1 dot1q '
                                        '2053 vlan-type 0x8100',
                             'state': 'Up',
                             'type': 'Static'},
                      2054: {'associated_evc': 'L2protocol drop',
                             'associated_interface': 'GigabitEthernet0/0/3',
                             'description': 'xxx',
                             'dot1q_tunnel_ethertype': '0x8100',
                             'efp_statistics': {'bytes_in': 0,
                                                'bytes_out': 0,
                                                'pkts_in': 0,
                                                'pkts_out': 0},
                             'encapsulation': 'dot1q 2054 vlan protocol '
                                              'type 0x8100',
                             'id': 2054,
                             'rewrite': 'egress tag translate 1-to-1 dot1q '
                                        '2054 vlan-type 0x8100',
                             'state': 'Up',
                             'type': 'Static'},
                      2055: {'associated_evc': 'L2protocol drop',
                             'associated_interface': 'GigabitEthernet0/0/3',
                             'description': 'xxx',
                             'dot1q_tunnel_ethertype': '0x8100',
                             'efp_statistics': {'bytes_in': 0,
                                                'bytes_out': 0,
                                                'pkts_in': 0,
                                                'pkts_out': 0},
                             'encapsulation': 'dot1q 2055 vlan protocol '
                                              'type 0x8100',
                             'id': 2055,
                             'rewrite': 'egress tag translate 1-to-1 dot1q '
                                        '2055 vlan-type 0x8100',
                             'state': 'Up',
                             'type': 'Static'}}}

    golden_output = {'execute.return_value': '''\
        Router#show ethernet service instance detail
        Load for five secs: 4%/0%; one minute: 5%; five minutes: 4%
        Time source is NTP, 16:31:09.701 JST Tue Nov 8 2016

        Service Instance ID: 2051
        Service Instance Type: Static
        Description: xxx
        Associated Interface: GigabitEthernet0/0/3
        Associated EVC: 
        L2protocol drop
        CE-Vlans:                                                                        
        Encapsulation: dot1q 2051 vlan protocol type 0x8100
        Rewrite: egress tag translate 1-to-1 dot1q 2051 vlan-type 0x8100
        Interface Dot1q Tunnel Ethertype: 0x8100
        State: Up
        EFP Statistics:
           Pkts In   Bytes In   Pkts Out  Bytes Out
                 0          0          0          0

        Service Instance ID: 2052
        Service Instance Type: Static
        Description: xxx
        Associated Interface: GigabitEthernet0/0/3
        Associated EVC: 
        L2protocol drop
        CE-Vlans:                                                                        
        Encapsulation: dot1q 2052 vlan protocol type 0x8100
        Rewrite: egress tag translate 1-to-1 dot1q 2052 vlan-type 0x8100
        Interface Dot1q Tunnel Ethertype: 0x8100
        State: Up
        EFP Statistics:
           Pkts In   Bytes In   Pkts Out  Bytes Out
                 0          0          0          0

        Service Instance ID: 2053
        Service Instance Type: Static
        Description: xxx
        Associated Interface: GigabitEthernet0/0/3
        Associated EVC: 
        L2protocol drop
        CE-Vlans:                                                                        
        Encapsulation: dot1q 2053 vlan protocol type 0x8100
        Rewrite: egress tag translate 1-to-1 dot1q 2053 vlan-type 0x8100
        Interface Dot1q Tunnel Ethertype: 0x8100
        State: Up
        EFP Statistics:
           Pkts In   Bytes In   Pkts Out  Bytes Out
                 0          0          0          0

        Service Instance ID: 2054
        Service Instance Type: Static
        Description: xxx
        Associated Interface: GigabitEthernet0/0/3
        Associated EVC: 
        L2protocol drop
        CE-Vlans:                                                                        
        Encapsulation: dot1q 2054 vlan protocol type 0x8100
        Rewrite: egress tag translate 1-to-1 dot1q 2054 vlan-type 0x8100
        Interface Dot1q Tunnel Ethertype: 0x8100
        State: Up
        EFP Statistics:
           Pkts In   Bytes In   Pkts Out  Bytes Out
                 0          0          0          0

        Service Instance ID: 2055
        Service Instance Type: Static
        Description: xxx
        Associated Interface: GigabitEthernet0/0/3
        Associated EVC: 
        L2protocol drop
        CE-Vlans:                                                                        
        Encapsulation: dot1q 2055 vlan protocol type 0x8100
        Rewrite: egress tag translate 1-to-1 dot1q 2055 vlan-type 0x8100
        Interface Dot1q Tunnel Ethertype: 0x8100
        State: Up
        EFP Statistics:
           Pkts In   Bytes In   Pkts Out  Bytes Out
                 0          0          0          0
    '''
    }

    golden_parsed_output_interface = {'service_instance': {1: {'associated_evc': 'L2protocol drop',
                          'associated_interface': 'Ethernet0/0',
                          'control_policy': 'ABC',
                          'dot1q_tunnel_ethertype': '0x8100',
                          'efp_statistics': {'bytes_in': 0,
                                             'bytes_out': 0,
                                             'pkts_in': 0,
                                             'pkts_out': 0},
                          'encapsulation': 'dot1q 200-300 vlan protocol '
                                           'type 0x8100',
                          'id': 1,
                          'intiators': 'unclassified vlan',
                          'state': 'Up',
                          'type': 'L2Context'},
                      2: {'associated_evc': 'L2protocol drop',
                          'associated_interface': 'Ethernet0/0',
                          'dot1q_tunnel_ethertype': '0x8100',
                          'efp_statistics': {'bytes_in': 0,
                                             'bytes_out': 0,
                                             'pkts_in': 0,
                                             'pkts_out': 0},
                          'encapsulation': 'dot1q 201 vlan protocol type '
                                           '0x8100',
                          'id': 2,
                          'state': 'Up',
                          'type': 'Dynamic',
                          'vlans': '10-20'},
                      3: {'associated_evc': 'L2protocol drop',
                          'associated_interface': 'Ethernet0/0',
                          'dot1q_tunnel_ethertype': '0x8100',
                          'efp_statistics': {'bytes_in': 0,
                                             'bytes_out': 0,
                                             'pkts_in': 0,
                                             'pkts_out': 0},
                          'encapsulation': 'dot1q 201 vlan protocol type '
                                           '0x8100',
                          'id': 3,
                          'state': 'Up',
                          'type': 'static',
                          'vlans': '10-20'}}}


    golden_output_interface = {'execute.return_value': '''\
        Device# show ethernet service instance interface ethernet 0/0 detail

        Service Instance ID: 1
        Service instance type: L2Context
        Intiators: unclassified vlan
        Control policy: ABC
        Associated Interface: Ethernet0/0
        Associated EVC:
        L2protocol drop
        CE-Vlans:
        Encapsulation: dot1q 200-300 vlan protocol type 0x8100
        Interface Dot1q Tunnel Ethertype: 0x8100
        State: Up
        EFP Statistics:
           Pkts In   Bytes In   Pkts Out  Bytes Out
                 0          0          0          0

        Service Instance ID: 2
        Service instance type: Dynamic

        Associated Interface: Ethernet0/0
        Associated EVC:
        L2protocol drop
        CE-Vlans: 10-20
        Encapsulation: dot1q 201 vlan protocol type 0x8100
        Interface Dot1q Tunnel Ethertype: 0x8100
        State: Up
        EFP Statistics:
           Pkts In   Bytes In   Pkts Out  Bytes Out
                 0          0          0          0

        Service Instance ID: 3
        Service instance type: static
        Associated Interface: Ethernet0/0
        Associated EVC:
        L2protocol drop
        CE-Vlans: 10-20
        Encapsulation: dot1q 201 vlan protocol type 0x8100
        Interface Dot1q Tunnel Ethertype: 0x8100
        State: Up
        EFP Statistics:
           Pkts In   Bytes In   Pkts Out  Bytes Out
                 0          0          0          0
    '''
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        platform_obj = ShowEthernetServiceInstanceDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = platform_obj.parse()    

    def test_golden_full(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        platform_obj = ShowEthernetServiceInstanceDetail(device=self.device)
        parsed_output = platform_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_interface(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_interface)
        platform_obj = ShowEthernetServiceInstanceDetail(device=self.device)
        parsed_output = platform_obj.parse(interface='ethernet 0/0')
        self.assertEqual(parsed_output, self.golden_parsed_output_interface)


if __name__ == '__main__':
    unittest.main()

