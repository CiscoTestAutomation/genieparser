import re
import unittest
from unittest.mock import Mock

from pyats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                             SchemaMissingKeyError

from genie.libs.parser.iosxr.show_ipv6 import ShowIpv6NeighborsDetail, ShowIpv6Neighbors


#############################################################################
# unitest For show ipv6 neighbors detail
#############################################################################

class test_show_ipv6_neighbors_detail(unittest.TestCase):

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'interfaces': {
            'GigabitEthernet0/0/0/0': {
                'interface': 'GigabitEthernet0/0/0/0',
                'neighbors': {
                    '2001:db8:8548:1::1': {
                        'age': '82',
                        'ip': '2001:db8:8548:1::1',
                        'link_layer_address': 'fa16.3eff.c4d3',
                        'neighbor_state': 'REACH',
                        'location': '0/0/CPU0',
                        'static': '-',
                        'dynamic': 'Y',
                        'sync': '-',
                        'serg_flags': 'ff',
                        'origin': 'dynamic',
                    },
                    '2001:db8:8548:1::22': {
                        'age': '-',
                        'ip': '2001:db8:8548:1::22',
                        'link_layer_address': 'aaaa.beff.6b6b',
                        'neighbor_state': 'REACH',
                        'location': '0/0/CPU0',
                        'static': 'Y',
                        'dynamic': '-',
                        'sync': '-',
                        'serg_flags': 'ff',
                        'origin': 'static',
                    },
                    'fe80::f816:3eff:feff:c4d3': {
                        'age': '158',
                        'ip': 'fe80::f816:3eff:feff:c4d3',
                        'link_layer_address': 'fa16.3eff.c4d3',
                        'neighbor_state': 'REACH',
                        'location': '0/0/CPU0',
                        'static': '-',
                        'dynamic': 'Y',
                        'sync': '-',
                        'serg_flags': 'ff',
                        'origin': 'dynamic',
                    },
                    'Mcast adjacency': {
                        'age': '-',
                        'ip': 'Mcast adjacency',
                        'link_layer_address': '0000.0000.0000',
                        'neighbor_state': 'REACH',
                        'location': '0/0/CPU0',
                        'static': '-',
                        'dynamic': '-',
                        'sync': '-',
                        'serg_flags': 'ff',
                        'origin': 'other',
                    },
                },
            },
            'GigabitEthernet0/0/0/3': {
                'interface': 'GigabitEthernet0/0/0/3',
                'neighbors': {
                    '2001:db8:c8d1:4::3': {
                        'age': '114',
                        'ip': '2001:db8:c8d1:4::3',
                        'link_layer_address': '5e01.c0ff.0209',
                        'neighbor_state': 'REACH',
                        'location': '0/0/CPU0',
                        'static': '-',
                        'dynamic': 'Y',
                        'sync': '-',
                        'serg_flags': 'ff',
                        'origin': 'dynamic',
                    },
                    'fe80::5c01:c0ff:feff:209': {
                        'age': '12',
                        'ip': 'fe80::5c01:c0ff:feff:209',
                        'link_layer_address': '5e01.c0ff.0209',
                        'neighbor_state': 'REACH',
                        'location': '0/0/CPU0',
                        'static': '-',
                        'dynamic': 'Y',
                        'sync': '-',
                        'serg_flags': 'ff',
                        'origin': 'dynamic',
                    },
                    'Mcast adjacency': {
                        'age': '-',
                        'ip': 'Mcast adjacency',
                        'link_layer_address': '0000.0000.0000',
                        'neighbor_state': 'REACH',
                        'location': '0/0/CPU0',
                        'static': '-',
                        'dynamic': '-',
                        'sync': '-',
                        'serg_flags': 'ff',
                        'origin': 'other',
                    },
                },
            },
            'GigabitEthernet0/0/0/2': {
                'interface': 'GigabitEthernet0/0/0/2',
                'neighbors': {
                    '2001:db8:c56d:4::3': {
                        'age': '1',
                        'ip': '2001:db8:c56d:4::3',
                        'link_layer_address': '5e01.c0ff.0209',
                        'neighbor_state': 'REACH',
                        'location': '0/0/CPU0',
                        'static': '-',
                        'dynamic': 'Y',
                        'sync': '-',
                        'serg_flags': 'ff',
                        'origin': 'dynamic',
                    },
                    'fe80::5c01:c0ff:feff:209': {
                        'age': '12',
                        'ip': 'fe80::5c01:c0ff:feff:209',
                        'link_layer_address': '5e01.c0ff.0209',
                        'neighbor_state': 'REACH',
                        'location': '0/0/CPU0',
                        'static': '-',
                        'dynamic': 'Y',
                        'sync': '-',
                        'serg_flags': 'ff',
                        'origin': 'dynamic',
                    },
                    'Mcast adjacency': {
                        'age': '-',
                        'ip': 'Mcast adjacency',
                        'link_layer_address': '0000.0000.0000',
                        'neighbor_state': 'REACH',
                        'location': '0/0/CPU0',
                        'static': '-',
                        'dynamic': '-',
                        'sync': '-',
                        'serg_flags': 'ff',
                        'origin': 'other',
                    },
                },
            },
            'GigabitEthernet0/0/0/1': {
                'interface': 'GigabitEthernet0/0/0/1',
                'neighbors': {
                    '2001:db8:888c:1::1': {
                        'age': '4',
                        'ip': '2001:db8:888c:1::1',
                        'link_layer_address': 'fa16.3eff.f679',
                        'neighbor_state': 'REACH',
                        'location': '0/0/CPU0',
                        'static': '-',
                        'dynamic': 'Y',
                        'sync': '-',
                        'serg_flags': 'ff',
                        'origin': 'dynamic',
                    },
                    '2001:db8:888c:1::22': {
                        'age': '-',
                        'ip': '2001:db8:888c:1::22',
                        'link_layer_address': 'dddd.beff.9a9a',
                        'neighbor_state': 'REACH',
                        'location': '0/0/CPU0',
                        'static': 'Y',
                        'dynamic': '-',
                        'sync': '-',
                        'serg_flags': 'ff',
                        'origin': 'static',
                    },
                    'fe80::f816:3eff:feff:f679': {
                        'age': '37',
                        'ip': 'fe80::f816:3eff:feff:f679',
                        'link_layer_address': 'fa16.3eff.f679',
                        'neighbor_state': 'REACH',
                        'location': '0/0/CPU0',
                        'static': '-',
                        'dynamic': 'Y',
                        'sync': '-',
                        'serg_flags': 'ff',
                        'origin': 'dynamic',
                    },
                    'Mcast adjacency': {
                        'age': '-',
                        'ip': 'Mcast adjacency',
                        'link_layer_address': '0000.0000.0000',
                        'neighbor_state': 'REACH',
                        'location': '0/0/CPU0',
                        'static': '-',
                        'dynamic': '-',
                        'sync': '-',
                        'serg_flags': 'ff',
                        'origin': 'other',
                    },
                },
            },
        },
    }

    golden_output = {'execute.return_value': '''
        RP/0/RP0/CPU0:xr9kv-2#show ipv6 neighbors detail
        Thu Apr 26 13:09:53.379 UTC
        IPv6 Address                             Age  Link-layer Add State Interface            Location      Static Dynamic Sync       Serg-Flags 
        2001:db8:8548:1::1                              82   fa16.3eff.c4d3 REACH Gi0/0/0/0            0/0/CPU0        -      Y       -            ff
        2001:db8:8548:1::22                                - aaaa.beff.6b6b REACH Gi0/0/0/0            0/0/CPU0        Y      -       -            ff
        fe80::f816:3eff:feff:c4d3                158  fa16.3eff.c4d3 REACH Gi0/0/0/0            0/0/CPU0        -      Y       -            ff
        [Mcast adjacency]                           - 0000.0000.0000 REACH Gi0/0/0/0            0/0/CPU0        -      -       -            ff
        2001:db8:c8d1:4::3                              114  5e01.c0ff.0209 REACH Gi0/0/0/3            0/0/CPU0        -      Y       -            ff
        fe80::5c01:c0ff:feff:209                   12   5e01.c0ff.0209 REACH Gi0/0/0/3            0/0/CPU0        -      Y       -            ff
        [Mcast adjacency]                           - 0000.0000.0000 REACH Gi0/0/0/3            0/0/CPU0        -      -       -            ff
        2001:db8:c56d:4::3                              1    5e01.c0ff.0209 REACH Gi0/0/0/2            0/0/CPU0        -      Y       -            ff
        fe80::5c01:c0ff:feff:209                   12   5e01.c0ff.0209 REACH Gi0/0/0/2            0/0/CPU0        -      Y       -            ff
        [Mcast adjacency]                           - 0000.0000.0000 REACH Gi0/0/0/2            0/0/CPU0        -      -       -            ff
        2001:db8:888c:1::1                              4    fa16.3eff.f679 REACH Gi0/0/0/1            0/0/CPU0        -      Y       -            ff
        2001:db8:888c:1::22                                - dddd.beff.9a9a REACH Gi0/0/0/1            0/0/CPU0        Y      -       -            ff
        fe80::f816:3eff:feff:f679                37   fa16.3eff.f679 REACH Gi0/0/0/1            0/0/CPU0        -      Y       -            ff
        [Mcast adjacency]                           - 0000.0000.0000 REACH Gi0/0/0/1            0/0/CPU0        -      -       -            ff
    '''}

    def test_show_ipv6_neighbors_detail_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpv6NeighborsDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_ipv6_neighbors_detail_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowIpv6NeighborsDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


#############################################################################
# unitest For show ipv6 neighbors
#############################################################################

class TestShowIpv6Neighbors(unittest.TestCase):

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'interfaces': {
            'GigabitEthernet0/0/0/0.90': {
                'interface': 'GigabitEthernet0/0/0/0.90',
                'neighbors': {
                    'fe80::f816:3eff:feff:384a': {
                        'age': '119',
                        'ip': 'fe80::f816:3eff:feff:384a',
                        'link_layer_address': 'fa16.3eff.384a',
                        'neighbor_state': 'REACH',
                        'location': '0/0/CPU0',
                    },
                    'Mcast adjacency': {
                        'age': '-',
                        'ip': 'Mcast adjacency',
                        'link_layer_address': '0000.0000.0000',
                        'neighbor_state': 'REACH',
                        'location': '0/0/CPU0',
                    },
                },
            },
            'GigabitEthernet0/0/0/1.90': {
                'interface': 'GigabitEthernet0/0/0/1.90',
                'neighbors': {
                    'fe80::5c00:40ff:feff:209': {
                        'age': '128',
                        'ip': 'fe80::5c00:40ff:feff:209',
                        'link_layer_address': '5e00.40ff.0209',
                        'neighbor_state': 'REACH',
                        'location': '0/0/CPU0',
                    },
                    'Mcast adjacency': {
                        'age': '-',
                        'ip': 'Mcast adjacency',
                        'link_layer_address': '0000.0000.0000',
                        'neighbor_state': 'REACH',
                        'location': '0/0/CPU0',
                    },
                },
            },
            'GigabitEthernet0/0/0/0.110': {
                'interface': 'GigabitEthernet0/0/0/0.110',
                'neighbors': {
                    'fe80::f816:3eff:feff:384a': {
                        'age': '94',
                        'ip': 'fe80::f816:3eff:feff:384a',
                        'link_layer_address': 'fa16.3eff.384a',
                        'neighbor_state': 'REACH',
                        'location': '0/0/CPU0',
                    },
                    'Mcast adjacency': {
                        'age': '-',
                        'ip': 'Mcast adjacency',
                        'link_layer_address': '0000.0000.0000',
                        'neighbor_state': 'REACH',
                        'location': '0/0/CPU0',
                    },
                },
            },
            'GigabitEthernet0/0/0/0.115': {
                'interface': 'GigabitEthernet0/0/0/0.115',
                'neighbors': {
                    'fe80::f816:3eff:feff:384a': {
                        'age': '27',
                        'ip': 'fe80::f816:3eff:feff:384a',
                        'link_layer_address': 'fa16.3eff.384a',
                        'neighbor_state': 'REACH',
                        'location': '0/0/CPU0',
                    },
                    'Mcast adjacency': {
                        'age': '-',
                        'ip': 'Mcast adjacency',
                        'link_layer_address': '0000.0000.0000',
                        'neighbor_state': 'REACH',
                        'location': '0/0/CPU0',
                    },
                },
            },
            'GigabitEthernet0/0/0/0.120': {
                'interface': 'GigabitEthernet0/0/0/0.120',
                'neighbors': {
                    'Mcast adjacency': {
                        'age': '-',
                        'ip': 'Mcast adjacency',
                        'link_layer_address': '0000.0000.0000',
                        'neighbor_state': 'REACH',
                        'location': '0/0/CPU0',
                    },
                },
            },
        },
    }
    golden_output = {'execute.return_value': '''
        RP/0/RP0/CPU0:R2_xr#show ipv6 neighbors
        Thu Sep 26 22:11:10.340 UTC
        IPv6 Address                             Age  Link-layer Add State Interface            Location
        fe80::f816:3eff:feff:384a                119  fa16.3eff.384a REACH Gi0/0/0/0.90         0/0/CPU0
        [Mcast adjacency]                           - 0000.0000.0000 REACH Gi0/0/0/0.90         0/0/CPU0
        fe80::5c00:40ff:feff:209                   128  5e00.40ff.0209 REACH Gi0/0/0/1.90         0/0/CPU0
        [Mcast adjacency]                           - 0000.0000.0000 REACH Gi0/0/0/1.90         0/0/CPU0
        fe80::f816:3eff:feff:384a                94   fa16.3eff.384a REACH Gi0/0/0/0.110        0/0/CPU0
        [Mcast adjacency]                           - 0000.0000.0000 REACH Gi0/0/0/0.110        0/0/CPU0
        fe80::f816:3eff:feff:384a                27   fa16.3eff.384a REACH Gi0/0/0/0.115        0/0/CPU0
        [Mcast adjacency]                           - 0000.0000.0000 REACH Gi0/0/0/0.115        0/0/CPU0
        [Mcast adjacency]                           - 0000.0000.0000 REACH Gi0/0/0/0.120        0/0/CPU0
    '''}

    golden_parsed_output1 = {
        'interfaces': {
            'GigabitEthernet0/0/0/0.390': {
                'interface': 'GigabitEthernet0/0/0/0.390',
                'neighbors': {
                    'fe80::f816:3eff:feff:384a': {
                        'age': '47',
                        'ip': 'fe80::f816:3eff:feff:384a',
                        'link_layer_address': 'fa16.3eff.384a',
                        'neighbor_state': 'REACH',
                        'location': '0/0/CPU0',
                    },
                    'Mcast adjacency': {
                        'age': '-',
                        'ip': 'Mcast adjacency',
                        'link_layer_address': '0000.0000.0000',
                        'neighbor_state': 'REACH',
                        'location': '0/0/CPU0',
                    },
                },
            },
        },
    }
    golden_output1 = {'execute.return_value': '''
        RP/0/RP0/CPU0:R2_xr# show ipv6 neighbors vrf VRF1 Gi0/0/0/0.390
        Thu Sep 26 22:12:55.701 UTC
        IPv6 Address                             Age  Link-layer Add State Interface            Location
        fe80::f816:3eff:feff:384a                47   fa16.3eff.384a REACH Gi0/0/0/0.390        0/0/CPU0
        [Mcast adjacency]                           - 0000.0000.0000 REACH Gi0/0/0/0.390        0/0/CPU0
    '''}

    golden_parsed_output2 = {
        'interfaces': {
            'GigabitEthernet0/0/0/0.390': {
                'interface': 'GigabitEthernet0/0/0/0.390',
                'neighbors': {
                    'fe80::f816:3eff:feff:384a': {
                        'age': '90',
                        'ip': 'fe80::f816:3eff:feff:384a',
                        'link_layer_address': 'fa16.3eff.384a',
                        'neighbor_state': 'REACH',
                        'location': '0/0/CPU0',
                    },
                    'Mcast adjacency': {
                        'age': '-',
                        'ip': 'Mcast adjacency',
                        'link_layer_address': '0000.0000.0000',
                        'neighbor_state': 'REACH',
                        'location': '0/0/CPU0',
                    },
                },
            },
            'GigabitEthernet0/0/0/0.410': {
                'interface': 'GigabitEthernet0/0/0/0.410',
                'neighbors': {
                    'Mcast adjacency': {
                        'age': '-',
                        'ip': 'Mcast adjacency',
                        'link_layer_address': '0000.0000.0000',
                        'neighbor_state': 'REACH',
                        'location': '0/0/CPU0',
                    },
                },
            },
            'GigabitEthernet0/0/0/0.415': {
                'interface': 'GigabitEthernet0/0/0/0.415',
                'neighbors': {
                    'Mcast adjacency': {
                        'age': '-',
                        'ip': 'Mcast adjacency',
                        'link_layer_address': '0000.0000.0000',
                        'neighbor_state': 'REACH',
                        'location': '0/0/CPU0',
                    },
                },
            },
            'GigabitEthernet0/0/0/0.420': {
                'interface': 'GigabitEthernet0/0/0/0.420',
                'neighbors': {
                    'Mcast adjacency': {
                        'age': '-',
                        'ip': 'Mcast adjacency',
                        'link_layer_address': '0000.0000.0000',
                        'neighbor_state': 'REACH',
                        'location': '0/0/CPU0',
                    },
                },
            },
        },
    }
    golden_output2 = {'execute.return_value': '''
        RP/0/RP0/CPU0:R2_xr#show ipv6 neighbors vrf VRF1
        Thu Sep 26 22:13:39.221 UTC
        IPv6 Address                             Age  Link-layer Add State Interface            Location
        fe80::f816:3eff:feff:384a                90   fa16.3eff.384a REACH Gi0/0/0/0.390        0/0/CPU0
        [Mcast adjacency]                           - 0000.0000.0000 REACH Gi0/0/0/0.390        0/0/CPU0
        [Mcast adjacency]                           - 0000.0000.0000 REACH Gi0/0/0/0.410        0/0/CPU0
        [Mcast adjacency]                           - 0000.0000.0000 REACH Gi0/0/0/0.415        0/0/CPU0
        [Mcast adjacency]                           - 0000.0000.0000 REACH Gi0/0/0/0.420        0/0/CPU0
    '''}

    golden_parsed_output3 = {
        'interfaces': {
            'GigabitEthernet0/0/0/0.390': {
                'interface': 'GigabitEthernet0/0/0/0.390',
                'neighbors': {
                    'fe80::f816:3eff:feff:384a': {
                        'age': '129',
                        'ip': 'fe80::f816:3eff:feff:384a',
                        'link_layer_address': 'fa16.3eff.384a',
                        'neighbor_state': 'REACH',
                        'location': '0/0/CPU0',
                    },
                    'Mcast adjacency': {
                        'age': '-',
                        'ip': 'Mcast adjacency',
                        'link_layer_address': '0000.0000.0000',
                        'neighbor_state': 'REACH',
                        'location': '0/0/CPU0',
                    },
                },
            },
        },
    }
    golden_output3 = {'execute.return_value': '''
        RP/0/RP0/CPU0:R2_xr#show ipv6 neighbors Gi0/0/0/0.390
        Thu Sep 26 22:14:18.343 UTC
        IPv6 Address                             Age  Link-layer Add State Interface            Location
        fe80::f816:3eff:feff:384a                129  fa16.3eff.384a REACH Gi0/0/0/0.390        0/0/CPU0
        [Mcast adjacency]                           - 0000.0000.0000 REACH Gi0/0/0/0.390        0/0/CPU0
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpv6Neighbors(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowIpv6Neighbors(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)
    
    def test_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowIpv6Neighbors(device=self.device)
        parsed_output = obj.parse(vrf='VRF1', interface='Gi0/0/0/0.390')
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowIpv6Neighbors(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output, self.golden_parsed_output2)
    
    def test_golden3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        obj = ShowIpv6Neighbors(device=self.device)
        parsed_output = obj.parse(interface='Gi0/0/0/0.390')
        self.assertEqual(parsed_output, self.golden_parsed_output3)


if __name__ == '__main__':
    unittest.main()