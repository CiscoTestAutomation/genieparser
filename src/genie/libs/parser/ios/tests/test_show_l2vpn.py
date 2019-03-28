#!/bin/env python
import unittest
from unittest.mock import Mock
from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                             SchemaMissingKeyError

from genie.libs.parser.ios.show_l2vpn import ShowL2vpnVfi, \
                                             ShowL2vpnServiceAll


class test_show_l2vpn_vfi(unittest.TestCase):

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
    'vfi': {
        'serviceCore1': {
            'signaling': 'LDP',
            'vpls_id': '9:10',
            'vpn_id': 100,
            'bd_vfi_name': 'serviceCore1',
            'bridge_domain': {
                100: {
                    'pseudo_port_interface': 'Virtual-Ethernet1000',
                    'vfi': {
                        '10.0.0.1': {
                            'pw_id': {
                                'Pw2000': {
                                    'discovered_router_id': '10.0.0.1',
                                    'vc_id': 10,
                                    'next_hop': '10.0.0.1',
                                    },
                                },
                            },
                        '10.0.0.4': {
                            'pw_id': {
                                'Pw5': {
                                    'discovered_router_id': '-',
                                    'vc_id': 10,
                                    'next_hop': '10.0.0.4',
                                    },
                                },
                            },
                        '10.0.0.3': {
                            'pw_id': {
                                'Pw2002': {
                                    'discovered_router_id': '10.1.1.3',
                                    'vc_id': 10,
                                    'next_hop': '10.0.0.3',
                                    },
                                },
                            },
                        '10.0.0.2': {
                            'pw_id': {
                                'Pw2001': {
                                    'discovered_router_id': '10.1.1.2',
                                    'vc_id': 10,
                                    'next_hop': '10.0.0.2',
                                    },
                                },
                            },
                        },
                    },
                },
            'rt': ['10.10.10.10:150'],
            'state': 'UP',
            'rd': '9:10',
            },
        },
    }

    golden_output = {'execute.return_value': '''\
    Device# show l2vpn vfi

    Legend: RT= Route-target

    VFI name: serviceCore1, State: UP, Signaling Protocol: LDP
      VPN ID: 100, VPLS-ID: 9:10, Bridge-domain vlan: 100
      RD: 9:10, RT: 10.10.10.10:150
      Pseudo-port Interface: Virtual-Ethernet1000

      Neighbors connected via pseudowires:
      Interface    Peer Address    VC ID      Discovered Router ID   Next Hop
      Pw2000       10.0.0.1        10         10.0.0.1               10.0.0.1
      Pw2001       10.0.0.2        10         10.1.1.2               10.0.0.2
      Pw2002       10.0.0.3        10         10.1.1.3               10.0.0.3
      Pw5          10.0.0.4        10         -                      10.0.0.4
    '''
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        platform_obj = ShowL2vpnVfi(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = platform_obj.parse()    

    def test_golden_full(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        platform_obj = ShowL2vpnVfi(device=self.device)
        parsed_output = platform_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


class test_show_l2vpn_service_all(unittest.TestCase):

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
    'instance': {
        'default': {
            'vrf': {
                'default': {
                    'address_family': {
                        'l2vpn_vpls': {
                            'serviceStit3': {
                                'interface': {
                                    'Pw4': {
                                        'group': 'right',
                                        'state_in_l2vpn_service': 'UP',
                                        'state': 'UP',
                                        'encapsulation': 'MPLS 8.8.8.8:300',
                                        'priority': 0,
                                        },
                                    'Pw3': {
                                        'group': 'left',
                                        'state_in_l2vpn_service': 'UP',
                                        'state': 'UP',
                                        'encapsulation': 'MPLS 7.7.7.7:300',
                                        'priority': 0,
                                        },
                                    },
                                'state': 'UP',
                                'name': 'serviceStit3',
                                },
                            'serviceWire1': {
                                'interface': {
                                    'Eth4/1:20': {
                                        'group': 'core_conn',
                                        'state_in_l2vpn_service': 'UP',
                                        'state': 'UP',
                                        'encapsulation': 'EVC 55',
                                        'priority': 1,
                                        },
                                    'Eth1/1:10': {
                                        'group': 'access',
                                        'state_in_l2vpn_service': 'UP',
                                        'state': 'UP',
                                        'encapsulation': 'EVC 45',
                                        'priority': 0,
                                        },
                                    'Eth3/1:20': {
                                        'group': 'core_conn',
                                        'state_in_l2vpn_service': 'IA',
                                        'state': 'DN',
                                        'encapsulation': 'EVC 55',
                                        'priority': 0,
                                        },
                                    'Pw2': {
                                        'group': 'core',
                                        'state_in_l2vpn_service': 'IA',
                                        'state': 'SB',
                                        'encapsulation': 'MPLS 6.6.6.6:200',
                                        'priority': 1,
                                        },
                                    'Pw1': {
                                        'group': 'core',
                                        'state_in_l2vpn_service': 'UP',
                                        'state': 'UP',
                                        'encapsulation': 'MPLS 5.5.5.5:100',
                                        'priority': 0,
                                        },
                                    'Eth2/1:20': {
                                        'group': 'access_conn',
                                        'state_in_l2vpn_service': 'UP',
                                        'state': 'UP',
                                        'encapsulation': 'EVC 55',
                                        'priority': 0,
                                        },
                                    },
                                'state': 'UP',
                                'name': 'serviceWire1',
                                },
                            },
                        },
                    },
                },
            },
        },
    }

    golden_output = {'execute.return_value': '''\
    Device# show l2vpn service all

    Legend: St=State    Prio=Priority
            UP=Up       DN=Down            AD=Admin Down      IA=Inactive
            SB=Standby  HS=Hot Standby     RV=Recovering      NH=No Hardware

      Interface          Group       Encapsulation           Prio  St  XC St
      ---------          -----       -------------           ----  --  -----
    XC name: serviceWire1, State: UP
      Eth1/1:10          access      EVC 45                  0     UP  UP
      Pw1                core        MPLS 5.5.5.5:100        0     UP  UP
      Pw2                core        MPLS 6.6.6.6:200        1     SB  IA
    XC name: serviceConn2, State:UP
      Eth2/1:20          access_conn EVC 55                  0     UP  UP
      Eth3/1:20          core_conn   EVC 55                  0     DN  IA
      Eth4/1:20          core_conn   EVC 55                  1     UP  UP
    XC name: serviceStit3, State: UP
      Pw3                left        MPLS 7.7.7.7:300        0     UP  UP
      Pw4                right       MPLS 8.8.8.8:300        0     UP  UP
    '''
    }


    golden_parsed_output_2 = {
    'instance': {
        'default': {
            'vrf': {
                'default': {
                    'address_family': {
                        'l2vpn_vpls': {
                            'Gi1/1/1-1001': {
                                'interface': {
                                    'pw100001': {
                                        'group': 'right',
                                        'state_in_l2vpn_service': 'UP',
                                        'state': 'UP',
                                        'encapsulation': '2.1.1.2:1234000(MPLS)',
                                        'priority': 0,
                                        },
                                    'Gi1/1/1': {
                                        'group': 'left',
                                        'state_in_l2vpn_service': 'UP',
                                        'state': 'UP',
                                        'encapsulation': 'Gi1/1/1:1001(Gi VLAN)',
                                        'priority': 0,
                                        },
                                    },
                                'state': 'UP',
                                'name': 'Gi1/1/1-1001',
                                },
                            },
                        },
                    },
                },
            },
        },
    }

    golden_output_2 = {'execute.return_value': '''\
    Device# show l2vpn service all
    Legend: St=State    XC St=State in the L2VPN Service      Prio=Priority
            UP=Up       DN=Down            AD=Admin Down      IA=Inactive
            SB=Standby  HS=Hot Standby     RV=Recovering      NH=No Hardware
            m=manually selected

      Interface          Group       Encapsulation                   Prio  St  XC St
      ---------          -----       -------------                   ----  --  -----
    VPWS name: Gi1/1/1-1001, State: UP
      Gi1/1/1            left        Gi1/1/1:1001(Gi VLAN)          0     UP  UP
      pw100001           right       2.1.1.2:1234000(MPLS)           0     UP  UP
    '''
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        platform_obj = ShowL2vpnServiceAll(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = platform_obj.parse()    

    def test_golden_full(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        platform_obj = ShowL2vpnServiceAll(device=self.device)
        parsed_output = platform_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_full_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        platform_obj = ShowL2vpnServiceAll(device=self.device)
        parsed_output = platform_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_2)


if __name__ == '__main__':
    unittest.main()