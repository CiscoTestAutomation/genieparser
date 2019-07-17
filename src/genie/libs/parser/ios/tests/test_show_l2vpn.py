#!/bin/env python
import unittest
from unittest.mock import Mock
from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                             SchemaMissingKeyError

from genie.libs.parser.ios.show_l2vpn import ShowL2vpnVfi, \
                                             ShowL2vpnServiceAll, \
                                             ShowEthernetServiceInstanceStats, \
                                             ShowEthernetServiceInstanceSummary, \
                                             ShowEthernetServiceInstanceDetail, \
                                             ShowBridgeDomain

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
    'vpls_name': {
        'serviceStit3': {
            'state': 'UP',
            'interface': {
                'Pw4': {
                    'encapsulation': 'MPLS 10.1.8.8:300',
                    'state': 'UP',
                    'priority': 0,
                    'group': 'right',
                    'state_in_l2vpn_service': 'UP',
                    },
                'Pw3': {
                    'encapsulation': 'MPLS 10.196.7.7:300',
                    'state': 'UP',
                    'priority': 0,
                    'group': 'left',
                    'state_in_l2vpn_service': 'UP',
                    },
                },
            },
        'serviceWire1': {
            'state': 'UP',
            'interface': {
                'Eth3/1:20': {
                    'encapsulation': 'EVC 55',
                    'state': 'DN',
                    'priority': 0,
                    'group': 'core_conn',
                    'state_in_l2vpn_service': 'IA',
                    },
                'Pw2': {
                    'encapsulation': 'MPLS 10.144.6.6:200',
                    'state': 'SB',
                    'priority': 1,
                    'group': 'core',
                    'state_in_l2vpn_service': 'IA',
                    },
                'Pw1': {
                    'encapsulation': 'MPLS 10.100.5.5:100',
                    'state': 'UP',
                    'priority': 0,
                    'group': 'core',
                    'state_in_l2vpn_service': 'UP',
                    },
                'Eth1/1:10': {
                    'encapsulation': 'EVC 45',
                    'state': 'UP',
                    'priority': 0,
                    'group': 'access',
                    'state_in_l2vpn_service': 'UP',
                    },
                'Eth2/1:20': {
                    'encapsulation': 'EVC 55',
                    'state': 'UP',
                    'priority': 0,
                    'group': 'access_conn',
                    'state_in_l2vpn_service': 'UP',
                    },
                'Eth4/1:20': {
                    'encapsulation': 'EVC 55',
                    'state': 'UP',
                    'priority': 1,
                    'group': 'core_conn',
                    'state_in_l2vpn_service': 'UP',
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
      Pw1                core        MPLS 10.100.5.5:100        0     UP  UP
      Pw2                core        MPLS 10.144.6.6:200        1     SB  IA
    XC name: serviceConn2, State:UP
      Eth2/1:20          access_conn EVC 55                  0     UP  UP
      Eth3/1:20          core_conn   EVC 55                  0     DN  IA
      Eth4/1:20          core_conn   EVC 55                  1     UP  UP
    XC name: serviceStit3, State: UP
      Pw3                left        MPLS 10.196.7.7:300        0     UP  UP
      Pw4                right       MPLS 10.1.8.8:300        0     UP  UP
    '''
    }


    golden_parsed_output_2 = {
    'vpls_name': {
        'Gi1/1/1-1001': {
            'interface': {
                'pw100001': {
                    'encapsulation': '10.9.1.2:1234000(MPLS)',
                    'priority': 0,
                    'state_in_l2vpn_service': 'UP',
                    'state': 'UP',
                    'group': 'right',
                    },
                'Gi1/1/1': {
                    'encapsulation': 'Gi1/1/1:1001(Gi VLAN)',
                    'priority': 0,
                    'state_in_l2vpn_service': 'UP',
                    'state': 'UP',
                    'group': 'left',
                    },
                },
            'state': 'UP',
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
      pw100001           right       10.9.1.2:1234000(MPLS)           0     UP  UP
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


class test_show_ethernet_service_instance_stats(unittest.TestCase):

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'max_num_of_service_instances': 32768,
        'service_instance': {
            2051: {
                'pkts_out': 0,
                'pkts_in': 0,
                'interface': 'GigabitEthernet0/0/5',
                'bytes_in': 0,
                'bytes_out': 0,
                },
            2052: {
                'pkts_out': 0,
                'pkts_in': 0,
                'interface': 'GigabitEthernet0/0/5',
                'bytes_in': 0,
                'bytes_out': 0,
                },
            2053: {
                'pkts_out': 0,
                'pkts_in': 0,
                'interface': 'GigabitEthernet0/0/5',
                'bytes_in': 0,
                'bytes_out': 0,
                },
            2054: {
                'pkts_out': 0,
                'pkts_in': 0,
                'interface': 'GigabitEthernet0/0/5',
                'bytes_in': 0,
                'bytes_out': 0,
                },
            2055: {
                'pkts_out': 0,
                'pkts_in': 0,
                'interface': 'GigabitEthernet0/0/5',
                'bytes_in': 0,
                'bytes_out': 0,
                },
            2056: {
                'pkts_out': 0,
                'pkts_in': 0,
                'interface': 'GigabitEthernet0/0/5',
                'bytes_in': 0,
                'bytes_out': 0,
                },
            2057: {
                'pkts_out': 0,
                'pkts_in': 0,
                'interface': 'GigabitEthernet0/0/5',
                'bytes_in': 0,
                'bytes_out': 0,
                },
            2058: {
                'pkts_out': 0,
                'pkts_in': 0,
                'interface': 'GigabitEthernet0/0/5',
                'bytes_in': 0,
                'bytes_out': 0,
                },
            2059: {
                'pkts_out': 0,
                'pkts_in': 0,
                'interface': 'GigabitEthernet0/0/5',
                'bytes_in': 0,
                'bytes_out': 0,
                },
            2060: {
                'pkts_out': 0,
                'pkts_in': 0,
                'interface': 'GigabitEthernet0/0/5',
                'bytes_in': 0,
                'bytes_out': 0,
                },
            2061: {
                'pkts_out': 0,
                'pkts_in': 0,
                'interface': 'GigabitEthernet0/0/5',
                'bytes_in': 0,
                'bytes_out': 0,
                },
            2062: {
                'pkts_out': 0,
                'pkts_in': 0,
                'interface': 'GigabitEthernet0/0/5',
                'bytes_in': 0,
                'bytes_out': 0,
                },
            2063: {
                'pkts_out': 0,
                'pkts_in': 0,
                'interface': 'GigabitEthernet0/0/5',
                'bytes_in': 0,
                'bytes_out': 0,
                },
            2064: {
                'pkts_out': 0,
                'pkts_in': 0,
                'interface': 'GigabitEthernet0/0/5',
                'bytes_in': 0,
                'bytes_out': 0,
                },
            2065: {
                'pkts_out': 0,
                'pkts_in': 0,
                'interface': 'GigabitEthernet0/0/5',
                'bytes_in': 0,
                'bytes_out': 0,
                },
            2066: {
                'pkts_out': 0,
                'pkts_in': 0,
                'interface': 'GigabitEthernet0/0/5',
                'bytes_in': 0,
                'bytes_out': 0,
                },
            2067: {
                'pkts_out': 0,
                'pkts_in': 0,
                'interface': 'GigabitEthernet0/0/5',
                'bytes_in': 0,
                'bytes_out': 0,
                },
            2068: {
                'pkts_out': 0,
                'pkts_in': 0,
                'interface': 'GigabitEthernet0/0/5',
                'bytes_in': 0,
                'bytes_out': 0,
                },
            2069: {
                'pkts_out': 0,
                'pkts_in': 0,
                'interface': 'GigabitEthernet0/0/5',
                'bytes_in': 0,
                'bytes_out': 0,
                },
            2070: {
                'pkts_out': 0,
                'pkts_in': 0,
                'interface': 'GigabitEthernet0/0/5',
                'bytes_in': 0,
                'bytes_out': 0,
                },
            2071: {
                'pkts_out': 0,
                'pkts_in': 0,
                'interface': 'GigabitEthernet0/0/5',
                'bytes_in': 0,
                'bytes_out': 0,
                },
            2072: {
                'pkts_out': 0,
                'pkts_in': 0,
                'interface': 'GigabitEthernet0/0/5',
                'bytes_in': 0,
                'bytes_out': 0,
                },
            2073: {
                'pkts_out': 0,
                'pkts_in': 0,
                'interface': 'GigabitEthernet0/0/5',
                'bytes_in': 0,
                'bytes_out': 0,
                },
            2074: {
                'pkts_out': 0,
                'pkts_in': 0,
                'interface': 'GigabitEthernet0/0/5',
                'bytes_in': 0,
                'bytes_out': 0,
                },
            2075: {
                'pkts_out': 0,
                'pkts_in': 0,
                'interface': 'GigabitEthernet0/0/5',
                'bytes_in': 0,
                'bytes_out': 0,
                },
            2076: {
                'pkts_out': 0,
                'pkts_in': 0,
                'interface': 'GigabitEthernet0/0/5',
                'bytes_in': 0,
                'bytes_out': 0,
                },
            2077: {
                'pkts_out': 0,
                'pkts_in': 0,
                'interface': 'GigabitEthernet0/0/5',
                'bytes_in': 0,
                'bytes_out': 0,
                },
            2078: {
                'pkts_out': 0,
                'pkts_in': 0,
                'interface': 'GigabitEthernet0/0/5',
                'bytes_in': 0,
                'bytes_out': 0,
                },
            2079: {
                'pkts_out': 0,
                'pkts_in': 0,
                'interface': 'GigabitEthernet0/0/5',
                'bytes_in': 0,
                'bytes_out': 0,
                },
            2080: {
                'pkts_out': 0,
                'pkts_in': 0,
                'interface': 'GigabitEthernet0/0/5',
                'bytes_in': 0,
                'bytes_out': 0,
                },
            2081: {
                'pkts_out': 0,
                'pkts_in': 0,
                'interface': 'GigabitEthernet0/0/5',
                'bytes_in': 0,
                'bytes_out': 0,
                },
            2082: {
                'pkts_out': 0,
                'pkts_in': 0,
                'interface': 'GigabitEthernet0/0/5',
                'bytes_in': 0,
                'bytes_out': 0,
                },
            2083: {
                'pkts_out': 0,
                'pkts_in': 0,
                'interface': 'GigabitEthernet0/0/5',
                'bytes_in': 0,
                'bytes_out': 0,
                },
            2084: {
                'pkts_out': 0,
                'pkts_in': 0,
                'interface': 'GigabitEthernet0/0/5',
                'bytes_in': 0,
                'bytes_out': 0,
                },
            2085: {
                'pkts_out': 0,
                'pkts_in': 0,
                'interface': 'GigabitEthernet0/0/5',
                'bytes_in': 0,
                'bytes_out': 0,
                },
            2086: {
                'pkts_out': 0,
                'pkts_in': 0,
                'interface': 'GigabitEthernet0/0/5',
                'bytes_in': 0,
                'bytes_out': 0,
                },
            2087: {
                'pkts_out': 0,
                'pkts_in': 0,
                'interface': 'GigabitEthernet0/0/5',
                'bytes_in': 0,
                'bytes_out': 0,
                },
            2088: {
                'pkts_out': 0,
                'pkts_in': 0,
                'interface': 'GigabitEthernet0/0/5',
                'bytes_in': 0,
                'bytes_out': 0,
                },
            2089: {
                'pkts_out': 0,
                'pkts_in': 0,
                'interface': 'GigabitEthernet0/0/5',
                'bytes_in': 0,
                'bytes_out': 0,
                },
            2090: {
                'pkts_out': 0,
                'pkts_in': 0,
                'interface': 'GigabitEthernet0/0/5',
                'bytes_in': 0,
                'bytes_out': 0,
                },
            2091: {
                'pkts_out': 0,
                'pkts_in': 0,
                'interface': 'GigabitEthernet0/0/5',
                'bytes_in': 0,
                'bytes_out': 0,
                },
            },
        }

    golden_output = {'execute.return_value': '''\
        Router#show ethernet service instance stats
        Load for five secs: 4%/0%; one minute: 9%; five minutes: 8%
        Time source is NTP, 13:26:05.117 EST Tue Nov 12 2016

        System maximum number of service instances: 32768
        Service Instance 2051, Interface GigabitEthernet0/0/5
           Pkts In   Bytes In   Pkts Out  Bytes Out
                 0          0          0          0

        Service Instance 2052, Interface GigabitEthernet0/0/5
           Pkts In   Bytes In   Pkts Out  Bytes Out
                 0          0          0          0

        Service Instance 2053, Interface GigabitEthernet0/0/5
           Pkts In   Bytes In   Pkts Out  Bytes Out
                 0          0          0          0

        Service Instance 2054, Interface GigabitEthernet0/0/5
           Pkts In   Bytes In   Pkts Out  Bytes Out
                 0          0          0          0

        Service Instance 2055, Interface GigabitEthernet0/0/5
           Pkts In   Bytes In   Pkts Out  Bytes Out
                 0          0          0          0

        Service Instance 2056, Interface GigabitEthernet0/0/5
           Pkts In   Bytes In   Pkts Out  Bytes Out
                 0          0          0          0

        Service Instance 2057, Interface GigabitEthernet0/0/5
           Pkts In   Bytes In   Pkts Out  Bytes Out
                 0          0          0          0

        Service Instance 2058, Interface GigabitEthernet0/0/5
           Pkts In   Bytes In   Pkts Out  Bytes Out
                 0          0          0          0

        Service Instance 2059, Interface GigabitEthernet0/0/5
           Pkts In   Bytes In   Pkts Out  Bytes Out
                 0          0          0          0

        Service Instance 2060, Interface GigabitEthernet0/0/5
           Pkts In   Bytes In   Pkts Out  Bytes Out
                 0          0          0          0

        Service Instance 2061, Interface GigabitEthernet0/0/5
           Pkts In   Bytes In   Pkts Out  Bytes Out
                 0          0          0          0

        Service Instance 2062, Interface GigabitEthernet0/0/5
           Pkts In   Bytes In   Pkts Out  Bytes Out
                 0          0          0          0

        Service Instance 2063, Interface GigabitEthernet0/0/5
           Pkts In   Bytes In   Pkts Out  Bytes Out
                 0          0          0          0

        Service Instance 2064, Interface GigabitEthernet0/0/5
           Pkts In   Bytes In   Pkts Out  Bytes Out
                 0          0          0          0

        Service Instance 2065, Interface GigabitEthernet0/0/5
           Pkts In   Bytes In   Pkts Out  Bytes Out
                 0          0          0          0

        Service Instance 2066, Interface GigabitEthernet0/0/5
           Pkts In   Bytes In   Pkts Out  Bytes Out
                 0          0          0          0

        Service Instance 2067, Interface GigabitEthernet0/0/5
           Pkts In   Bytes In   Pkts Out  Bytes Out
                 0          0          0          0

        Service Instance 2068, Interface GigabitEthernet0/0/5
           Pkts In   Bytes In   Pkts Out  Bytes Out
                 0          0          0          0

        Service Instance 2069, Interface GigabitEthernet0/0/5
           Pkts In   Bytes In   Pkts Out  Bytes Out
                 0          0          0          0

        Service Instance 2070, Interface GigabitEthernet0/0/5
           Pkts In   Bytes In   Pkts Out  Bytes Out
                 0          0          0          0

        Service Instance 2071, Interface GigabitEthernet0/0/5
           Pkts In   Bytes In   Pkts Out  Bytes Out
                 0          0          0          0

        Service Instance 2072, Interface GigabitEthernet0/0/5
           Pkts In   Bytes In   Pkts Out  Bytes Out
                 0          0          0          0

        Service Instance 2073, Interface GigabitEthernet0/0/5
           Pkts In   Bytes In   Pkts Out  Bytes Out
                 0          0          0          0

        Service Instance 2074, Interface GigabitEthernet0/0/5
           Pkts In   Bytes In   Pkts Out  Bytes Out
                 0          0          0          0

        Service Instance 2075, Interface GigabitEthernet0/0/5
           Pkts In   Bytes In   Pkts Out  Bytes Out
                 0          0          0          0

        Service Instance 2076, Interface GigabitEthernet0/0/5
           Pkts In   Bytes In   Pkts Out  Bytes Out
                 0          0          0          0

        Service Instance 2077, Interface GigabitEthernet0/0/5
           Pkts In   Bytes In   Pkts Out  Bytes Out
                 0          0          0          0

        Service Instance 2078, Interface GigabitEthernet0/0/5
           Pkts In   Bytes In   Pkts Out  Bytes Out
                 0          0          0          0

        Service Instance 2079, Interface GigabitEthernet0/0/5
           Pkts In   Bytes In   Pkts Out  Bytes Out
                 0          0          0          0

        Service Instance 2080, Interface GigabitEthernet0/0/5
           Pkts In   Bytes In   Pkts Out  Bytes Out
                 0          0          0          0

        Service Instance 2081, Interface GigabitEthernet0/0/5
           Pkts In   Bytes In   Pkts Out  Bytes Out
                 0          0          0          0

        Service Instance 2082, Interface GigabitEthernet0/0/5
           Pkts In   Bytes In   Pkts Out  Bytes Out
                 0          0          0          0

        Service Instance 2083, Interface GigabitEthernet0/0/5
           Pkts In   Bytes In   Pkts Out  Bytes Out
                 0          0          0          0

        Service Instance 2084, Interface GigabitEthernet0/0/5
           Pkts In   Bytes In   Pkts Out  Bytes Out
                 0          0          0          0

        Service Instance 2085, Interface GigabitEthernet0/0/5
           Pkts In   Bytes In   Pkts Out  Bytes Out
                 0          0          0          0

        Service Instance 2086, Interface GigabitEthernet0/0/5
           Pkts In   Bytes In   Pkts Out  Bytes Out
                 0          0          0          0

        Service Instance 2087, Interface GigabitEthernet0/0/5
           Pkts In   Bytes In   Pkts Out  Bytes Out
                 0          0          0          0

        Service Instance 2088, Interface GigabitEthernet0/0/5
           Pkts In   Bytes In   Pkts Out  Bytes Out
                 0          0          0          0

        Service Instance 2089, Interface GigabitEthernet0/0/5
           Pkts In   Bytes In   Pkts Out  Bytes Out
                 0          0          0          0

        Service Instance 2090, Interface GigabitEthernet0/0/5
           Pkts In   Bytes In   Pkts Out  Bytes Out
                 0          0          0          0

        Service Instance 2091, Interface GigabitEthernet0/0/5
           Pkts In   Bytes In   Pkts Out  Bytes Out
                 0          0          0          0
    '''
    }

    golden_parsed_output_interface = {
        'service_instance': {
            1: {
                'bytes_in': 15408,
                'pkts_out': 97150,
                'interface': 'GigabitEthernet0/0/13',
                'pkts_in': 214,
                'bytes_out': 6994800,
                },
            2: {
                'bytes_in': 6768,
                'pkts_out': 9090,
                'interface': 'GigabitEthernet0/0/13',
                'pkts_in': 654,
                'bytes_out': 34565,
                },
            },
        }

    golden_output_interface = {'execute.return_value': '''\
        Router# show ethernet service instance interface gigabitEthernet 0/0/13 stats
        Service Instance 1, Interface GigabitEthernet0/0/13
        Pkts In   Bytes In   Pkts Out  Bytes Out
               214      15408      97150    6994800
        Service Instance 2, Interface GigabitEthernet0/0/13
        Pkts In   Bytes In   Pkts Out  Bytes Out
               654      6768      9090    34565
    '''
    }

    golden_parsed_output_shrinked = {
        'max_num_of_service_instances': 32768,
    }

    golden_output_shrinked = {'execute.return_value': '''\
        1006#show ethernet service instance stats
        Load for five secs: 1%/0%; one minute: 0%; five minutes: 0%
        Time source is NTP, 15:44:40.696 EST Fri Nov 11 2016

        System maximum number of service instances: 32768
    '''
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        platform_obj = ShowEthernetServiceInstanceStats(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = platform_obj.parse()    

    def test_golden_full(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        platform_obj = ShowEthernetServiceInstanceStats(device=self.device)
        parsed_output = platform_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_interface(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_interface)
        platform_obj = ShowEthernetServiceInstanceStats(device=self.device)
        parsed_output = platform_obj.parse(interface='gigabitEthernet 0/0/13')
        self.assertEqual(parsed_output, self.golden_parsed_output_interface)

    def test_golden_shrinked(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_shrinked)
        platform_obj = ShowEthernetServiceInstanceStats(device=self.device)
        parsed_output = platform_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_shrinked)


class test_show_ethernet_service_instance_summary(unittest.TestCase):

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
    'system_summary': {
        'bdomain': {
            'deleted': 0,
            'total': 502,
            'admin_do': 0,
            'up': 502,
            'error_di': 0,
            'bd_adm_do': 0,
            'down': 0,
            'unknown': 0,
            },
        'other': {
            'deleted': 0,
            'total': 110,
            'admin_do': 0,
            'up': 110,
            'error_di': 0,
            'bd_adm_do': 0,
            'down': 0,
            'unknown': 0,
            },
        'local sw': {
            'deleted': 0,
            'total': 0,
            'admin_do': 0,
            'up': 0,
            'error_di': 0,
            'bd_adm_do': 0,
            'down': 0,
            'unknown': 0,
            },
        'xconnect': {
            'deleted': 0,
            'total': 0,
            'admin_do': 0,
            'up': 0,
            'error_di': 0,
            'bd_adm_do': 0,
            'down': 0,
            'unknown': 0,
            },
        'all': {
            'deleted': 0,
            'total': 612,
            'admin_do': 0,
            'up': 612,
            'error_di': 0,
            'bd_adm_do': 0,
            'down': 0,
            'unknown': 0,
            },
        },
    'GigabitEthernet0/0/7': {
        'bdomain': {
            'deleted': 0,
            'total': 0,
            'admin_do': 0,
            'up': 0,
            'error_di': 0,
            'bd_adm_do': 0,
            'down': 0,
            'unknown': 0,
            },
        'other': {
            'deleted': 0,
            'total': 356,
            'admin_do': 0,
            'up': 356,
            'error_di': 0,
            'bd_adm_do': 0,
            'down': 0,
            'unknown': 0,
            },
        'local sw': {
            'deleted': 0,
            'total': 0,
            'admin_do': 0,
            'up': 0,
            'error_di': 0,
            'bd_adm_do': 0,
            'down': 0,
            'unknown': 0,
            },
        'xconnect': {
            'deleted': 0,
            'total': 0,
            'admin_do': 0,
            'up': 0,
            'error_di': 0,
            'bd_adm_do': 0,
            'down': 0,
            'unknown': 0,
            },
        'all': {
            'deleted': 0,
            'total': 356,
            'admin_do': 0,
            'up': 356,
            'error_di': 0,
            'bd_adm_do': 0,
            'down': 0,
            'unknown': 0,
            },
        },
    'Port-channel1': {
        'bdomain': {
            'deleted': 0,
            'total': 532,
            'admin_do': 0,
            'up': 532,
            'error_di': 0,
            'bd_adm_do': 0,
            'down': 0,
            'unknown': 0,
            },
        'other': {
            'deleted': 0,
            'total': 0,
            'admin_do': 0,
            'up': 0,
            'error_di': 0,
            'bd_adm_do': 0,
            'down': 0,
            'unknown': 0,
            },
        'local sw': {
            'deleted': 0,
            'total': 0,
            'admin_do': 0,
            'up': 0,
            'error_di': 0,
            'bd_adm_do': 0,
            'down': 0,
            'unknown': 0,
            },
        'xconnect': {
            'deleted': 0,
            'total': 0,
            'admin_do': 0,
            'up': 0,
            'error_di': 0,
            'bd_adm_do': 0,
            'down': 0,
            'unknown': 0,
            },
        'all': {
            'deleted': 0,
            'total': 532,
            'admin_do': 0,
            'up': 532,
            'error_di': 0,
            'bd_adm_do': 0,
            'down': 0,
            'unknown': 0,
            },
        },
    }

    golden_output = {'execute.return_value': '''\
        Router#show ethernet service instance summary
        Load for five secs: 2%/0%; one minute: 5%; five minutes: 4%
        Time source is NTP, 16:31:09.005 EST Tue Nov 8 2016

        System summary
                    Total       Up  AdminDo     Down  ErrorDi  Unknown  Deleted  BdAdmDo  
        bdomain       502      502        0        0        0        0        0        0  
        xconnect        0        0        0        0        0        0        0        0  
        local sw        0        0        0        0        0        0        0        0  
        other         110      110        0        0        0        0        0        0  
        all           612      612        0        0        0        0        0        0  
        Associated interface: GigabitEthernet0/0/7
                    Total       Up  AdminDo     Down  ErrorDi  Unknown  Deleted  BdAdmDo  
        bdomain         0        0        0        0        0        0        0        0  
        xconnect        0        0        0        0        0        0        0        0  
        local sw        0        0        0        0        0        0        0        0  
        other         356      356        0        0        0        0        0        0  
        all           356      356        0        0        0        0        0        0  
        Associated interface: Port-channel1
                    Total       Up  AdminDo     Down  ErrorDi  Unknown  Deleted  BdAdmDo  
        bdomain       532      532        0        0        0        0        0        0  
        xconnect        0        0        0        0        0        0        0        0  
        local sw        0        0        0        0        0        0        0        0  
        other           0        0        0        0        0        0        0        0  
        all           532      532        0        0        0        0        0        0  
    '''
    }


    def test_empty(self):
        self.device = Mock(**self.empty_output)
        platform_obj = ShowEthernetServiceInstanceSummary(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = platform_obj.parse()    

    def test_golden_full(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        platform_obj = ShowEthernetServiceInstanceSummary(device=self.device)
        parsed_output = platform_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


class test_show_ethernet_service_instance_detail(unittest.TestCase):

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
    'service_instance': {
            1: {
                'interfaces': {
                    'Ethernet0/0': {
                        'control_policy': 'ABC',
                        'dot1q_tunnel_ethertype': '0x8100',
                        'efp_statistics': {
                            'bytes_in': 0,
                            'bytes_out': 0,
                            'pkts_in': 0,
                            'pkts_out': 0
                        },
                        'encapsulation': 'dot1q 200-300 vlan protocol type 0x8100',
                        'intiators': 'unclassified vlan',
                        'l2protocol_drop': True,
                        'state': 'Up',
                        'type': 'L2Context'
                    }
                }
            },
            2: {
                'interfaces': {
                    'Ethernet0/0': {
                        'ce_vlans': '10-20',
                        'dot1q_tunnel_ethertype': '0x8100',
                        'efp_statistics': {
                            'bytes_in': 0,
                            'bytes_out': 0,
                            'pkts_in': 0,
                            'pkts_out': 0
                        },
                        'encapsulation': 'dot1q 201 vlan protocol type 0x8100',
                        'l2protocol_drop': True,
                        'state': 'Up',
                        'type': 'Dynamic'
                    }
                }
            }
        }
    }

    golden_output = {'execute.return_value': '''\
    Device# show ethernet service instance detail

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
    '''
    }

    golden_parsed_output_2 = {
    'service_instance': {
        400: {
            'interfaces': {
                'Ethernet1/3': {
                    'associated_evc': '50',
                    'ce_vlans': '30',
                    'state': 'AdminDown',
                    'efp_statistics': {
                        'pkts_in': 0,
                        'bytes_in': 0,
                        'pkts_out': 0,
                        'bytes_out': 0,
                        },
                    },
                },
            },
        },
    }

    golden_output_2 = {'execute.return_value': '''\
    Router# show ethernet service instance detail

    Service Instance ID: 400
    Associated Interface: Ethernet1/3
    Associated EVC: 50
    CE-Vlans: 30
    State: AdminDown
    EFP Statistics:
       Pkts In   Bytes In   Pkts Out  Bytes Out
             0          0          0          0
    '''
    }

    golden_parsed_output_interface = {
        'service_instance': {
            1: {
                'interfaces': {
                    'Ethernet0/0': {
                        'control_policy': 'ABC',
                        'dot1q_tunnel_ethertype': '0x8100',
                        'efp_statistics': {
                            'bytes_in': 0,
                            'bytes_out': 0,
                            'pkts_in': 0,
                            'pkts_out': 0
                        },
                        'encapsulation': 'dot1q 200-300 vlan protocol type 0x8100',
                        'intiators': 'unclassified vlan',
                        'l2protocol_drop': True,
                        'state': 'Up',
                        'type': 'L2Context'
                    }
                }
            },
            2: {
                'interfaces': {
                    'Ethernet0/0': {
                        'ce_vlans': '10-20',
                        'dot1q_tunnel_ethertype': '0x8100',
                        'efp_statistics': {
                            'bytes_in': 0,
                            'bytes_out': 0,
                            'pkts_in': 0,
                            'pkts_out': 0
                        },
                        'encapsulation': 'dot1q 201 vlan protocol type 0x8100',
                        'l2protocol_drop': True,
                        'state': 'Up',
                        'type': 'Dynamic'
                    }
                }
            },
            3: {
                'interfaces': {
                    'Ethernet0/0': {
                        'ce_vlans': '10-20',
                        'dot1q_tunnel_ethertype': '0x8100',
                        'efp_statistics': {
                            'bytes_in': 0,
                            'bytes_out': 0,
                            'pkts_in': 0,
                            'pkts_out': 0
                        },
                        'encapsulation': 'dot1q 201 vlan protocol type 0x8100',
                        'l2protocol_drop': True,
                        'state': 'Up',
                          'type': 'static'
                    }
                }
            }
        }
    }

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

    def test_golden_full_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        platform_obj = ShowEthernetServiceInstanceDetail(device=self.device)
        parsed_output = platform_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_2)

    def test_golden_interface(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_interface)
        platform_obj = ShowEthernetServiceInstanceDetail(device=self.device)
        parsed_output = platform_obj.parse(interface='ethernet 0/0')
        self.assertEqual(parsed_output, self.golden_parsed_output_interface)


class test_show_bridge_domain(unittest.TestCase):

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        "bridge_domain": {
            10: {
                "number_of_ports_in_all": 3,
                "bd_domain_id": 10,
                "state": "UP",
                "mac_learning_state": "Enabled",
                "aging_timer": 30,
                "member_ports": [
                    "GigabitEthernet6 service instance 10",
                    "GigabitEthernet7 service instance 10",
                    "EVPN Instance 10"
                ],
                "mac_table": {
                    "OCE_PTR:0xe8eb04a0": {
                        "mac_address": {
                            "000C.29B0.3E16": {
                                "mac_address": "000C.29B0.3E16",
                                "aed": 0,
                                "policy": "forward",
                                "tag": "static_r",
                                "age": 0
                            }
                        },
                        "pseudoport": "OCE_PTR:0xe8eb04a0"
                    },
                    "GigabitEthernet6.EFP10": {
                        "mac_address": {
                            "000C.29AF.F904": {
                                "mac_address": "000C.29AF.F904",
                                "aed": 0,
                                "policy": "forward",
                                "tag": "dynamic_c",
                                "age": 29
                            }
                        },
                        "pseudoport": "GigabitEthernet6.EFP10"
                    },
                    "GigabitEthernet7.EFP10": {
                        "mac_address": {
                            "000C.2993.130E": {
                                "mac_address": "000C.2993.130E",
                                "aed": 0,
                                "policy": "forward",
                                "tag": "dynamic_c",
                                "age": 26
                            }
                        },
                        "pseudoport": "GigabitEthernet7.EFP10"
                    },
                    "OCE_PTR:0xe8eb0500": {
                        "mac_address": {
                            "000C.29EE.EC0D": {
                                "mac_address": "000C.29EE.EC0D",
                                "aed": 0,
                                "policy": "forward",
                                "tag": "static_r",
                                "age": 0
                            }
                        },
                        "pseudoport": "OCE_PTR:0xe8eb0500"
                    }
                }
            }
        }
    }

    golden_output = {'execute.return_value': '''\
        PE1#show bridge-domain 10
        Bridge-domain 10 (3 ports in all)
        State: UP                    Mac learning: Enabled
        Aging-Timer: 30 second(s)
            GigabitEthernet6 service instance 10
            GigabitEthernet7 service instance 10
            EVPN Instance 10
           AED MAC address    Policy  Tag       Age  Pseudoport
           -   000C.29B0.3E16 forward static_r  0    OCE_PTR:0xe8eb04a0
           -   000C.29AF.F904 forward dynamic_c 29   GigabitEthernet6.EFP10
           -   000C.2993.130E forward dynamic_c 26   GigabitEthernet7.EFP10
           -   000C.29EE.EC0D forward static_r  0    OCE_PTR:0xe8eb0500
    '''
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        platform_obj = ShowBridgeDomain(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = platform_obj.parse()    

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        platform_obj = ShowBridgeDomain(device=self.device)
        parsed_output = platform_obj.parse(bd_id='10')
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == '__main__':
    unittest.main()