# Python
import re
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Parser
from genie.libs.parser.nxos.show_forwarding import ShowForwardingIpv4

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError


# =========================
#  Unit test for 'show forwarding ipv4'
# =========================

class test_show_forwarding_ipv4(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'slot': {'1': {'ip_version': {'IPv4': {'route_table': {'default/base': {'prefix': {'1.1.1.1/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                     'is_best': False}}},
                                                                                            '1.1.1.2/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                     'is_best': True}}},
                                                                                            '10.2.1.0/32': {'next_hop': {'Drop': {'interface': 'Null0',
                                                                                                                                  'is_best': False}}},
                                                                                            '10.2.1.1/32': {'next_hop': {'Receive': {'interface': 'sup-eth1',
                                                                                                                                     'is_best': False}}},
                                                                                            '10.2.1.2/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                      'is_best': False}}},
                                                                                            '10.2.1.255/32': {'next_hop': {'Attached': {'interface': 'Ethernet1/1',
                                                                                                                                        'is_best': False}}},
                                                                                            '2.2.2.1/32': {'next_hop': {'Receive': {'interface': 'sup-eth1',
                                                                                                                                    'is_best': False}}},
                                                                                            '2.2.2.2/32': {'next_hop': {'Receive': {'interface': 'sup-eth1',
                                                                                                                                    'is_best': False}}},
                                                                                            '20.2.1.0/32': {'next_hop': {'Drop': {'interface': 'Null0',
                                                                                                                                  'is_best': False}}},
                                                                                            '20.2.1.1/32': {'next_hop': {'Receive': {'interface': 'sup-eth1',
                                                                                                                                     'is_best': False}}},
                                                                                            '20.2.1.2/32': {'next_hop': {'20.2.1.2': {'interface': 'Ethernet1/2',
                                                                                                                                      'is_best': False}}},
                                                                                            '20.2.1.255/32': {'next_hop': {'Attached': {'interface': 'Ethernet1/2',
                                                                                                                                        'is_best': False}}},
                                                                                            '200.200.200.1/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                           'is_best': False}}},
                                                                                            '3.3.3.1/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                     'is_best': False}}},
                                                                                            '3.3.3.2/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                     'is_best': True}}},
                                                                                            '4.4.4.1/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                     'is_best': False}}},
                                                                                            '4.4.4.2/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                     'is_best': True}}},
                                                                                            '98.98.98.98/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                         'is_best': False}}},
                                                                                            '99.99.99.99/32': {'next_hop': {'20.2.1.2': {'interface': 'Ethernet1/2',
                                                                                                                                         'is_best': False}}}}}}}}},
                  '27': {'ip_version': {'IPv4': {'route_table': {'default/base': {'prefix': {'0.0.0.0/32': {'next_hop': {'Drop': {'interface': 'Null0',
                                                                                                                                  'is_best': False}}},
                                                                                             '1.1.1.1/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                      'is_best': False},
                                                                                                                         '20.2.1.2': {'interface': 'Ethernet1/2',
                                                                                                                                      'is_best': False}}},
                                                                                             '1.1.1.2/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                      'is_best': True},
                                                                                                                         '20.2.1.2': {'interface': 'Ethernet1/2',
                                                                                                                                      'is_best': False}}},
                                                                                             '10.1.1.0/24': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                       'is_best': False}}},
                                                                                             '10.2.1.0/24': {'next_hop': {'Attached': {'interface': 'Ethernet1/1',
                                                                                                                                       'is_best': False}}},
                                                                                             '10.2.1.0/32': {'next_hop': {'Drop': {'interface': 'Null0',
                                                                                                                                   'is_best': False}}},
                                                                                             '10.2.1.1/32': {'next_hop': {'Receive': {'interface': 'sup-eth1',
                                                                                                                                      'is_best': False}}},
                                                                                             '10.2.1.2/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                       'is_best': False}}},
                                                                                             '10.2.1.255/32': {'next_hop': {'Attached': {'interface': 'Ethernet1/1',
                                                                                                                                         'is_best': False}}},
                                                                                             '10.3.1.0/24': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                       'is_best': False}}},
                                                                                             '10.4.1.0/24': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                       'is_best': False}}},
                                                                                             '111.111.111.0/24': {'next_hop': {'Drop': {'interface': 'Null0',
                                                                                                                                        'is_best': False}}},
                                                                                             '127.0.0.0/8': {'next_hop': {'Drop': {'interface': 'Null0',
                                                                                                                                   'is_best': False}}},
                                                                                             '2.2.2.1/32': {'next_hop': {'Receive': {'interface': 'sup-eth1',
                                                                                                                                     'is_best': False}}},
                                                                                             '2.2.2.2/32': {'next_hop': {'Receive': {'interface': 'sup-eth1',
                                                                                                                                     'is_best': False}}},
                                                                                             '20.1.1.0/24': {'next_hop': {'20.2.1.2': {'interface': 'Ethernet1/2',
                                                                                                                                       'is_best': False}}},
                                                                                             '20.2.1.0/24': {'next_hop': {'Attached': {'interface': 'Ethernet1/2',
                                                                                                                                       'is_best': False}}},
                                                                                             '20.2.1.0/32': {'next_hop': {'Drop': {'interface': 'Null0',
                                                                                                                                   'is_best': False}}},
                                                                                             '20.2.1.1/32': {'next_hop': {'Receive': {'interface': 'sup-eth1',
                                                                                                                                      'is_best': False}}},
                                                                                             '20.2.1.2/32': {'next_hop': {'20.2.1.2': {'interface': 'Ethernet1/2',
                                                                                                                                       'is_best': False}}},
                                                                                             '20.2.1.255/32': {'next_hop': {'Attached': {'interface': 'Ethernet1/2',
                                                                                                                                         'is_best': False}}},
                                                                                             '20.3.1.0/24': {'next_hop': {'20.2.1.2': {'interface': 'Ethernet1/2',
                                                                                                                                       'is_best': False}}},
                                                                                             '20.4.1.0/24': {'next_hop': {'20.2.1.2': {'interface': 'Ethernet1/2',
                                                                                                                                       'is_best': False}}},
                                                                                             '200.200.200.1/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                            'is_best': False}}},
                                                                                             '25.25.0.0/16': {'next_hop': {'Drop': {'interface': 'Null0',
                                                                                                                                    'is_best': False}}},
                                                                                             '25.25.25.0/24': {'next_hop': {'Drop': {'interface': 'Null0',
                                                                                                                                     'is_best': False}}},
                                                                                             '255.255.255.255/32': {'next_hop': {'Receive': {'interface': 'sup-eth1',
                                                                                                                                             'is_best': False}}},
                                                                                             '3.3.3.1/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                      'is_best': False},
                                                                                                                         '20.2.1.2': {'interface': 'Ethernet1/2',
                                                                                                                                      'is_best': False}}},
                                                                                             '3.3.3.2/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                      'is_best': True},
                                                                                                                         '20.2.1.2': {'interface': 'Ethernet1/2',
                                                                                                                                      'is_best': False}}},
                                                                                             '4.4.4.1/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                      'is_best': False},
                                                                                                                         '20.2.1.2': {'interface': 'Ethernet1/2',
                                                                                                                                      'is_best': False}}},
                                                                                             '4.4.4.2/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                      'is_best': True},
                                                                                                                         '20.2.1.2': {'interface': 'Ethernet1/2',
                                                                                                                                      'is_best': False}}},
                                                                                             '98.98.98.98/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                          'is_best': False}}},
                                                                                             '99.99.99.99/32': {'next_hop': {'20.2.1.2': {'interface': 'Ethernet1/2',
                                                                                                                                          'is_best': False}}}}}}}}}}}

    golden_output = {'execute.return_value': '''
        #vtep1 show forwarding ipv4
        slot  1
        =======
        
        
        IPv4 routes for table default/base
        
        ------------------+-----------------------------------------+----------------------+-----------------+-----------------
        Prefix            | Next-hop                                | Interface            | Labels          | Partial Install 
        ------------------+-----------------------------------------+----------------------+-----------------+-----------------
        1.1.1.1/32           10.2.1.2                                  Ethernet1/1         
        *1.1.1.2/32          10.2.1.2                                  Ethernet1/1         
        2.2.2.1/32           Receive                                   sup-eth1
        2.2.2.2/32           Receive                                   sup-eth1
        3.3.3.1/32           10.2.1.2                                  Ethernet1/1         
        *3.3.3.2/32          10.2.1.2                                  Ethernet1/1         
        4.4.4.1/32           10.2.1.2                                  Ethernet1/1         
        *4.4.4.2/32          10.2.1.2                                  Ethernet1/1         
        10.2.1.0/32          Drop                                      Null0
        10.2.1.1/32          Receive                                   sup-eth1
        10.2.1.2/32          10.2.1.2                                  Ethernet1/1         
        10.2.1.255/32        Attached                                  Ethernet1/1
        20.2.1.0/32          Drop                                      Null0
        20.2.1.1/32          Receive                                   sup-eth1
        20.2.1.2/32          20.2.1.2                                  Ethernet1/2         
        20.2.1.255/32        Attached                                  Ethernet1/2
        98.98.98.98/32       10.2.1.2                                  Ethernet1/1         
        99.99.99.99/32       20.2.1.2                                  Ethernet1/2         
        200.200.200.1/32     10.2.1.2                                  Ethernet1/1         
        
        slot 27
        =======
        
        
        IPv4 routes for table default/base
        
        ------------------+-----------------------------------------+----------------------+-----------------+-----------------
        Prefix            | Next-hop                                | Interface            | Labels          | Partial Install 
        ------------------+-----------------------------------------+----------------------+-----------------+-----------------
        0.0.0.0/32           Drop                                      Null0
        127.0.0.0/8          Drop                                      Null0
        255.255.255.255/32   Receive                                   sup-eth1
        1.1.1.1/32           10.2.1.2                                  Ethernet1/1         
                             20.2.1.2                                  Ethernet1/2         
        *1.1.1.2/32          10.2.1.2                                  Ethernet1/1         
                             20.2.1.2                                  Ethernet1/2         
        2.2.2.1/32           Receive                                   sup-eth1
        2.2.2.2/32           Receive                                   sup-eth1
        3.3.3.1/32           10.2.1.2                                  Ethernet1/1         
                             20.2.1.2                                  Ethernet1/2         
        *3.3.3.2/32          10.2.1.2                                  Ethernet1/1         
                             20.2.1.2                                  Ethernet1/2         
        4.4.4.1/32           10.2.1.2                                  Ethernet1/1         
                             20.2.1.2                                  Ethernet1/2         
        *4.4.4.2/32          10.2.1.2                                  Ethernet1/1         
                             20.2.1.2                                  Ethernet1/2         
        10.1.1.0/24          10.2.1.2                                  Ethernet1/1         
        10.2.1.0/24          Attached                                  Ethernet1/1
        10.2.1.0/32          Drop                                      Null0
        10.2.1.1/32          Receive                                   sup-eth1
        10.2.1.2/32          10.2.1.2                                  Ethernet1/1         
        10.2.1.255/32        Attached                                  Ethernet1/1
        10.3.1.0/24          10.2.1.2                                  Ethernet1/1         
        10.4.1.0/24          10.2.1.2                                  Ethernet1/1         
        20.1.1.0/24          20.2.1.2                                  Ethernet1/2         
        20.2.1.0/24          Attached                                  Ethernet1/2
        20.2.1.0/32          Drop                                      Null0
        20.2.1.1/32          Receive                                   sup-eth1
        20.2.1.2/32          20.2.1.2                                  Ethernet1/2         
        20.2.1.255/32        Attached                                  Ethernet1/2
        20.3.1.0/24          20.2.1.2                                  Ethernet1/2         
        20.4.1.0/24          20.2.1.2                                  Ethernet1/2         
        25.25.0.0/16         Drop                                      Null0
        25.25.25.0/24        Drop                                      Null0
        98.98.98.98/32       10.2.1.2                                  Ethernet1/1         
        99.99.99.99/32       20.2.1.2                                  Ethernet1/2         
        111.111.111.0/24     Drop                                      Null0
        200.200.200.1/32     10.2.1.2                                  Ethernet1/1         
    '''}

    def test_show_forwarding_ipv4_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowForwardingIpv4(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_show_forwarding_ipv4_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowForwardingIpv4(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

# =========================
#  Unit test for 'show forwarding ipv4 vrf all'
# =========================

class test_show_forwarding_ipv4_vrf_all(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = { 
        'slot': {'1': {'ip_version': {'IPv4': {'route_table': {'VRF_230/base': {'prefix': {'192.168.20.0/24': {'next_hop': {'Attached': {'interface': 'Vlan20',
                                                                                                                                          'is_best': False}}},
                                                                                            '192.168.20.0/32': {'next_hop': {'Drop': {'interface': 'Null0',
                                                                                                                                      'is_best': False}}},
                                                                                            '192.168.20.254/32': {'next_hop': {'Receive': {'interface': 'sup-eth1',
                                                                                                                                           'is_best': False}}},
                                                                                            '192.168.20.255/32': {'next_hop': {'Attached': {'interface': 'Vlan20',
                                                                                                                                            'is_best': False}}},
                                                                                            '192.168.30.0/24': {'next_hop': {'Attached': {'interface': 'Vlan30',
                                                                                                                                          'is_best': False}}},
                                                                                            '192.168.30.0/32': {'next_hop': {'Drop': {'interface': 'Null0',
                                                                                                                                      'is_best': False}}},
                                                                                            '192.168.30.254/32': {'next_hop': {'Receive': {'interface': 'sup-eth1',
                                                                                                                                           'is_best': False}}},
                                                                                            '192.168.30.255/32': {'next_hop': {'Attached': {'interface': 'Vlan30',
                                                                                                                                            'is_best': False}}}}},
                                                                'VRF_450/base': {'prefix': {'192.168.40.0/24': {'next_hop': {'Attached': {'interface': 'Vlan40',
                                                                                                                                          'is_best': False}}},
                                                                                            '192.168.40.0/32': {'next_hop': {'Drop': {'interface': 'Null0',
                                                                                                                                      'is_best': False}}},
                                                                                            '192.168.40.254/32': {'next_hop': {'Receive': {'interface': 'sup-eth1',
                                                                                                                                           'is_best': False}}},
                                                                                            '192.168.40.255/32': {'next_hop': {'Attached': {'interface': 'Vlan40',
                                                                                                                                            'is_best': False}}},
                                                                                            '192.168.50.0/24': {'next_hop': {'Attached': {'interface': 'Vlan50',
                                                                                                                                          'is_best': False}}},
                                                                                            '192.168.50.0/32': {'next_hop': {'Drop': {'interface': 'Null0',
                                                                                                                                      'is_best': False}}},
                                                                                            '192.168.50.254/32': {'next_hop': {'Receive': {'interface': 'sup-eth1',
                                                                                                                                           'is_best': False}}},
                                                                                            '192.168.50.255/32': {'next_hop': {'Attached': {'interface': 'Vlan50',
                                                                                                                                            'is_best': False}}}}},
                                                                'VRF_Flow1_1/base': {'prefix': {'100.1.1.1/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501001'}}},
                                                                                                '100.1.1.10/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501001'}}},
                                                                                                '100.1.1.2/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501001'}}},
                                                                                                '100.1.1.3/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501001'}}},
                                                                                                '100.1.1.4/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501001'}}},
                                                                                                '100.1.1.5/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501001'}}},
                                                                                                '100.1.1.6/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501001'}}},
                                                                                                '100.1.1.7/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501001'}}},
                                                                                                '100.1.1.8/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501001'}}},
                                                                                                '100.1.1.9/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501001'}}},
                                                                                                '100.1.2.1/32': {'next_hop': {'192.168.21.2': {'interface': 'Ethernet1/3.21',
                                                                                                                                               'is_best': True}}},
                                                                                                '100.1.2.10/32': {'next_hop': {'192.168.21.2': {'interface': 'Ethernet1/3.21',
                                                                                                                                                'is_best': True}}},
                                                                                                '100.1.2.2/32': {'next_hop': {'192.168.21.2': {'interface': 'Ethernet1/3.21',
                                                                                                                                               'is_best': True}}},
                                                                                                '100.1.2.3/32': {'next_hop': {'192.168.21.2': {'interface': 'Ethernet1/3.21',
                                                                                                                                               'is_best': True}}},
                                                                                                '100.1.2.4/32': {'next_hop': {'192.168.21.2': {'interface': 'Ethernet1/3.21',
                                                                                                                                               'is_best': True}}},
                                                                                                '100.1.2.5/32': {'next_hop': {'192.168.21.2': {'interface': 'Ethernet1/3.21',
                                                                                                                                               'is_best': True}}},
                                                                                                '100.1.2.6/32': {'next_hop': {'192.168.21.2': {'interface': 'Ethernet1/3.21',
                                                                                                                                               'is_best': True}}},
                                                                                                '100.1.2.7/32': {'next_hop': {'192.168.21.2': {'interface': 'Ethernet1/3.21',
                                                                                                                                               'is_best': True}}},
                                                                                                '100.1.2.8/32': {'next_hop': {'192.168.21.2': {'interface': 'Ethernet1/3.21',
                                                                                                                                               'is_best': True}}},
                                                                                                '100.1.2.9/32': {'next_hop': {'192.168.21.2': {'interface': 'Ethernet1/3.21',
                                                                                                                                               'is_best': True}}},
                                                                                                '100.1.3.1/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501001'}}},
                                                                                                '100.1.3.10/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501001'}}},
                                                                                                '100.1.3.2/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501001'}}},
                                                                                                '100.1.3.3/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501001'}}},
                                                                                                '100.1.3.4/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501001'}}},
                                                                                                '100.1.3.5/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501001'}}},
                                                                                                '100.1.3.6/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501001'}}},
                                                                                                '100.1.3.7/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501001'}}},
                                                                                                '100.1.3.8/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501001'}}},
                                                                                                '100.1.3.9/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501001'}}},
                                                                                                '100.1.4.1/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501001'}}},
                                                                                                '100.1.4.10/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501001'}}},
                                                                                                '100.1.4.2/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501001'}}},
                                                                                                '100.1.4.3/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501001'}}},
                                                                                                '100.1.4.4/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501001'}}},
                                                                                                '100.1.4.5/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501001'}}},
                                                                                                '100.1.4.6/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501001'}}},
                                                                                                '100.1.4.7/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501001'}}},
                                                                                                '100.1.4.8/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501001'}}},
                                                                                                '100.1.4.9/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501001'}}},
                                                                                                '192.168.21.0/24': {'next_hop': {'Attached': {'interface': 'Ethernet1/3.21',
                                                                                                                                              'is_best': False}}},
                                                                                                '192.168.21.0/32': {'next_hop': {'Drop': {'interface': 'Null0',
                                                                                                                                          'is_best': False}}},
                                                                                                '192.168.21.1/32': {'next_hop': {'Receive': {'interface': 'sup-eth1',
                                                                                                                                             'is_best': False}}},
                                                                                                '192.168.21.2/32': {'next_hop': {'192.168.21.2': {'interface': 'Ethernet1/3.21',
                                                                                                                                                  'is_best': False}}},
                                                                                                '192.168.21.255/32': {'next_hop': {'Attached': {'interface': 'Ethernet1/3.21',
                                                                                                                                                'is_best': False}}}}},
                                                                'VRF_Flow1_2/base': {'prefix': {'100.2.1.1/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501002'}}},
                                                                                                '100.2.1.10/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501002'}}},
                                                                                                '100.2.1.2/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501002'}}},
                                                                                                '100.2.1.3/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501002'}}},
                                                                                                '100.2.1.4/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501002'}}},
                                                                                                '100.2.1.5/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501002'}}},
                                                                                                '100.2.1.6/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501002'}}},
                                                                                                '100.2.1.7/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501002'}}},
                                                                                                '100.2.1.8/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501002'}}},
                                                                                                '100.2.1.9/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501002'}}},
                                                                                                '100.2.2.1/32': {'next_hop': {'192.168.22.2': {'interface': 'Ethernet1/3.22',
                                                                                                                                               'is_best': True}}},
                                                                                                '100.2.2.10/32': {'next_hop': {'192.168.22.2': {'interface': 'Ethernet1/3.22',
                                                                                                                                                'is_best': True}}},
                                                                                                '100.2.2.2/32': {'next_hop': {'192.168.22.2': {'interface': 'Ethernet1/3.22',
                                                                                                                                               'is_best': True}}},
                                                                                                '100.2.2.3/32': {'next_hop': {'192.168.22.2': {'interface': 'Ethernet1/3.22',
                                                                                                                                               'is_best': True}}},
                                                                                                '100.2.2.4/32': {'next_hop': {'192.168.22.2': {'interface': 'Ethernet1/3.22',
                                                                                                                                               'is_best': True}}},
                                                                                                '100.2.2.5/32': {'next_hop': {'192.168.22.2': {'interface': 'Ethernet1/3.22',
                                                                                                                                               'is_best': True}}},
                                                                                                '100.2.2.6/32': {'next_hop': {'192.168.22.2': {'interface': 'Ethernet1/3.22',
                                                                                                                                               'is_best': True}}},
                                                                                                '100.2.2.7/32': {'next_hop': {'192.168.22.2': {'interface': 'Ethernet1/3.22',
                                                                                                                                               'is_best': True}}},
                                                                                                '100.2.2.8/32': {'next_hop': {'192.168.22.2': {'interface': 'Ethernet1/3.22',
                                                                                                                                               'is_best': True}}},
                                                                                                '100.2.2.9/32': {'next_hop': {'192.168.22.2': {'interface': 'Ethernet1/3.22',
                                                                                                                                               'is_best': True}}},
                                                                                                '100.2.3.1/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501002'}}},
                                                                                                '100.2.3.10/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501002'}}},
                                                                                                '100.2.3.2/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501002'}}},
                                                                                                '100.2.3.3/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501002'}}},
                                                                                                '100.2.3.4/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501002'}}},
                                                                                                '100.2.3.5/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501002'}}},
                                                                                                '100.2.3.6/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501002'}}},
                                                                                                '100.2.3.7/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501002'}}},
                                                                                                '100.2.3.8/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501002'}}},
                                                                                                '100.2.3.9/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501002'}}},
                                                                                                '100.2.4.1/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501002'}}},
                                                                                                '100.2.4.10/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501002'}}},
                                                                                                '100.2.4.2/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501002'}}},
                                                                                                '100.2.4.3/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501002'}}},
                                                                                                '100.2.4.4/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501002'}}},
                                                                                                '100.2.4.5/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501002'}}},
                                                                                                '100.2.4.6/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501002'}}},
                                                                                                '100.2.4.7/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501002'}}},
                                                                                                '100.2.4.8/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501002'}}},
                                                                                                '100.2.4.9/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501002'}}},
                                                                                                '192.168.22.0/24': {'next_hop': {'Attached': {'interface': 'Ethernet1/3.22',
                                                                                                                                              'is_best': False}}},
                                                                                                '192.168.22.0/32': {'next_hop': {'Drop': {'interface': 'Null0',
                                                                                                                                          'is_best': False}}},
                                                                                                '192.168.22.1/32': {'next_hop': {'Receive': {'interface': 'sup-eth1',
                                                                                                                                             'is_best': False}}},
                                                                                                '192.168.22.2/32': {'next_hop': {'192.168.22.2': {'interface': 'Ethernet1/3.22',
                                                                                                                                                  'is_best': False}}},
                                                                                                '192.168.22.255/32': {'next_hop': {'Attached': {'interface': 'Ethernet1/3.22',
                                                                                                                                                'is_best': False}}}}},
                                                                'VRF_Flow1_3/base': {'prefix': {'100.3.1.1/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501003'}}},
                                                                                                '100.3.1.10/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501003'}}},
                                                                                                '100.3.1.2/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501003'}}},
                                                                                                '100.3.1.3/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501003'}}},
                                                                                                '100.3.1.4/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501003'}}},
                                                                                                '100.3.1.5/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501003'}}},
                                                                                                '100.3.1.6/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501003'}}},
                                                                                                '100.3.1.7/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501003'}}},
                                                                                                '100.3.1.8/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501003'}}},
                                                                                                '100.3.1.9/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501003'}}},
                                                                                                '100.3.2.1/32': {'next_hop': {'192.168.23.2': {'interface': 'Ethernet1/3.23',
                                                                                                                                               'is_best': True}}},
                                                                                                '100.3.2.10/32': {'next_hop': {'192.168.23.2': {'interface': 'Ethernet1/3.23',
                                                                                                                                                'is_best': True}}},
                                                                                                '100.3.2.2/32': {'next_hop': {'192.168.23.2': {'interface': 'Ethernet1/3.23',
                                                                                                                                               'is_best': True}}},
                                                                                                '100.3.2.3/32': {'next_hop': {'192.168.23.2': {'interface': 'Ethernet1/3.23',
                                                                                                                                               'is_best': True}}},
                                                                                                '100.3.2.4/32': {'next_hop': {'192.168.23.2': {'interface': 'Ethernet1/3.23',
                                                                                                                                               'is_best': True}}},
                                                                                                '100.3.2.5/32': {'next_hop': {'192.168.23.2': {'interface': 'Ethernet1/3.23',
                                                                                                                                               'is_best': True}}},
                                                                                                '100.3.2.6/32': {'next_hop': {'192.168.23.2': {'interface': 'Ethernet1/3.23',
                                                                                                                                               'is_best': True}}},
                                                                                                '100.3.2.7/32': {'next_hop': {'192.168.23.2': {'interface': 'Ethernet1/3.23',
                                                                                                                                               'is_best': True}}},
                                                                                                '100.3.2.8/32': {'next_hop': {'192.168.23.2': {'interface': 'Ethernet1/3.23',
                                                                                                                                               'is_best': True}}},
                                                                                                '100.3.2.9/32': {'next_hop': {'192.168.23.2': {'interface': 'Ethernet1/3.23',
                                                                                                                                               'is_best': True}}},
                                                                                                '100.3.3.1/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501003'}}},
                                                                                                '100.3.3.10/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501003'}}},
                                                                                                '100.3.3.2/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501003'}}},
                                                                                                '100.3.3.3/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501003'}}},
                                                                                                '100.3.3.4/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501003'}}},
                                                                                                '100.3.3.5/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501003'}}},
                                                                                                '100.3.3.6/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501003'}}},
                                                                                                '100.3.3.7/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501003'}}},
                                                                                                '100.3.3.8/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501003'}}},
                                                                                                '100.3.3.9/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501003'}}},
                                                                                                '100.3.4.1/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501003'}}},
                                                                                                '100.3.4.10/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501003'}}},
                                                                                                '100.3.4.2/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501003'}}},
                                                                                                '100.3.4.3/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501003'}}},
                                                                                                '100.3.4.4/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501003'}}},
                                                                                                '100.3.4.5/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501003'}}},
                                                                                                '100.3.4.6/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501003'}}},
                                                                                                '100.3.4.7/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501003'}}},
                                                                                                '100.3.4.8/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501003'}}},
                                                                                                '100.3.4.9/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501003'}}},
                                                                                                '192.168.23.0/24': {'next_hop': {'Attached': {'interface': 'Ethernet1/3.23',
                                                                                                                                              'is_best': False}}},
                                                                                                '192.168.23.0/32': {'next_hop': {'Drop': {'interface': 'Null0',
                                                                                                                                          'is_best': False}}},
                                                                                                '192.168.23.1/32': {'next_hop': {'Receive': {'interface': 'sup-eth1',
                                                                                                                                             'is_best': False}}},
                                                                                                '192.168.23.2/32': {'next_hop': {'192.168.23.2': {'interface': 'Ethernet1/3.23',
                                                                                                                                                  'is_best': False}}},
                                                                                                '192.168.23.255/32': {'next_hop': {'Attached': {'interface': 'Ethernet1/3.23',
                                                                                                                                                'is_best': False}}}}},
                                                                'VRF_Flow1_4/base': {'prefix': {'100.4.1.1/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501004'}}},
                                                                                                '100.4.1.10/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501004'}}},
                                                                                                '100.4.1.2/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501004'}}},
                                                                                                '100.4.1.3/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501004'}}},
                                                                                                '100.4.1.4/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501004'}}},
                                                                                                '100.4.1.5/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501004'}}},
                                                                                                '100.4.1.6/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501004'}}},
                                                                                                '100.4.1.7/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501004'}}},
                                                                                                '100.4.1.8/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501004'}}},
                                                                                                '100.4.1.9/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501004'}}},
                                                                                                '100.4.2.1/32': {'next_hop': {'192.168.24.2': {'interface': 'Ethernet1/3.24',
                                                                                                                                               'is_best': True}}},
                                                                                                '100.4.2.10/32': {'next_hop': {'192.168.24.2': {'interface': 'Ethernet1/3.24',
                                                                                                                                                'is_best': True}}},
                                                                                                '100.4.2.2/32': {'next_hop': {'192.168.24.2': {'interface': 'Ethernet1/3.24',
                                                                                                                                               'is_best': True}}},
                                                                                                '100.4.2.3/32': {'next_hop': {'192.168.24.2': {'interface': 'Ethernet1/3.24',
                                                                                                                                               'is_best': True}}},
                                                                                                '100.4.2.4/32': {'next_hop': {'192.168.24.2': {'interface': 'Ethernet1/3.24',
                                                                                                                                               'is_best': True}}},
                                                                                                '100.4.2.5/32': {'next_hop': {'192.168.24.2': {'interface': 'Ethernet1/3.24',
                                                                                                                                               'is_best': True}}},
                                                                                                '100.4.2.6/32': {'next_hop': {'192.168.24.2': {'interface': 'Ethernet1/3.24',
                                                                                                                                               'is_best': True}}},
                                                                                                '100.4.2.7/32': {'next_hop': {'192.168.24.2': {'interface': 'Ethernet1/3.24',
                                                                                                                                               'is_best': True}}},
                                                                                                '100.4.2.8/32': {'next_hop': {'192.168.24.2': {'interface': 'Ethernet1/3.24',
                                                                                                                                               'is_best': True}}},
                                                                                                '100.4.2.9/32': {'next_hop': {'192.168.24.2': {'interface': 'Ethernet1/3.24',
                                                                                                                                               'is_best': True}}},
                                                                                                '100.4.3.1/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501004'}}},
                                                                                                '100.4.3.10/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501004'}}},
                                                                                                '100.4.3.2/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501004'}}},
                                                                                                '100.4.3.3/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501004'}}},
                                                                                                '100.4.3.4/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501004'}}},
                                                                                                '100.4.3.5/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501004'}}},
                                                                                                '100.4.3.6/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501004'}}},
                                                                                                '100.4.3.7/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501004'}}},
                                                                                                '100.4.3.8/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501004'}}},
                                                                                                '100.4.3.9/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501004'}}},
                                                                                                '100.4.4.1/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501004'}}},
                                                                                                '100.4.4.10/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501004'}}},
                                                                                                '100.4.4.2/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501004'}}},
                                                                                                '100.4.4.3/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501004'}}},
                                                                                                '100.4.4.4/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501004'}}},
                                                                                                '100.4.4.5/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501004'}}},
                                                                                                '100.4.4.6/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501004'}}},
                                                                                                '100.4.4.7/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501004'}}},
                                                                                                '100.4.4.8/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501004'}}},
                                                                                                '100.4.4.9/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501004'}}},
                                                                                                '192.168.24.0/24': {'next_hop': {'Attached': {'interface': 'Ethernet1/3.24',
                                                                                                                                              'is_best': False}}},
                                                                                                '192.168.24.0/32': {'next_hop': {'Drop': {'interface': 'Null0',
                                                                                                                                          'is_best': False}}},
                                                                                                '192.168.24.1/32': {'next_hop': {'Receive': {'interface': 'sup-eth1',
                                                                                                                                             'is_best': False}}},
                                                                                                '192.168.24.2/32': {'next_hop': {'192.168.24.2': {'interface': 'Ethernet1/3.24',
                                                                                                                                                  'is_best': False}}},
                                                                                                '192.168.24.255/32': {'next_hop': {'Attached': {'interface': 'Ethernet1/3.24',
                                                                                                                                                'is_best': False}}}}},
                                                                'default/base': {'prefix': {'1.1.1.1/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                     'is_best': False}}},
                                                                                            '1.1.1.2/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                     'is_best': True}}},
                                                                                            '10.2.1.0/32': {'next_hop': {'Drop': {'interface': 'Null0',
                                                                                                                                  'is_best': False}}},
                                                                                            '10.2.1.1/32': {'next_hop': {'Receive': {'interface': 'sup-eth1',
                                                                                                                                     'is_best': False}}},
                                                                                            '10.2.1.2/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                      'is_best': False}}},
                                                                                            '10.2.1.255/32': {'next_hop': {'Attached': {'interface': 'Ethernet1/1',
                                                                                                                                        'is_best': False}}},
                                                                                            '2.2.2.1/32': {'next_hop': {'Receive': {'interface': 'sup-eth1',
                                                                                                                                    'is_best': False}}},
                                                                                            '2.2.2.2/32': {'next_hop': {'Receive': {'interface': 'sup-eth1',
                                                                                                                                    'is_best': False}}},
                                                                                            '20.2.1.0/32': {'next_hop': {'Drop': {'interface': 'Null0',
                                                                                                                                  'is_best': False}}},
                                                                                            '20.2.1.1/32': {'next_hop': {'Receive': {'interface': 'sup-eth1',
                                                                                                                                     'is_best': False}}},
                                                                                            '20.2.1.2/32': {'next_hop': {'20.2.1.2': {'interface': 'Ethernet1/2',
                                                                                                                                      'is_best': False}}},
                                                                                            '20.2.1.255/32': {'next_hop': {'Attached': {'interface': 'Ethernet1/2',
                                                                                                                                        'is_best': False}}},
                                                                                            '200.200.200.1/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                           'is_best': False}}},
                                                                                            '3.3.3.1/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                     'is_best': False}}},
                                                                                            '3.3.3.2/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                     'is_best': True}}},
                                                                                            '4.4.4.1/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                     'is_best': False}}},
                                                                                            '4.4.4.2/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                     'is_best': True}}},
                                                                                            '98.98.98.98/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                         'is_best': False}}},
                                                                                            '99.99.99.99/32': {'next_hop': {'20.2.1.2': {'interface': 'Ethernet1/2',
                                                                                                                                         'is_best': False}}}}}}}}},
                  '27': {'ip_version': {'IPv4': {'route_table': {'0xfffe': {'prefix': {'0.0.0.0/32': {'next_hop': {'Drop': {'interface': 'Null0',
                                                                                                                            'is_best': False}}},
                                                                                       '127.0.0.0/8': {'next_hop': {'Drop': {'interface': 'Null0',
                                                                                                                             'is_best': False}}},
                                                                                       '255.255.255.255/32': {'next_hop': {'Receive': {'interface': 'sup-eth1',
                                                                                                                                       'is_best': False}}}}},
                                                                 'VRF_230/base': {'prefix': {'0.0.0.0/32': {'next_hop': {'Drop': {'interface': 'Null0',
                                                                                                                                  'is_best': False}}},
                                                                                             '127.0.0.0/8': {'next_hop': {'Drop': {'interface': 'Null0',
                                                                                                                                   'is_best': False}}},
                                                                                             '192.168.20.0/24': {'next_hop': {'Attached': {'interface': 'Vlan20',
                                                                                                                                           'is_best': False}}},
                                                                                             '192.168.20.0/32': {'next_hop': {'Drop': {'interface': 'Null0',
                                                                                                                                       'is_best': False}}},
                                                                                             '192.168.20.254/32': {'next_hop': {'Receive': {'interface': 'sup-eth1',
                                                                                                                                            'is_best': False}}},
                                                                                             '192.168.20.255/32': {'next_hop': {'Attached': {'interface': 'Vlan20',
                                                                                                                                             'is_best': False}}},
                                                                                             '192.168.30.0/24': {'next_hop': {'Attached': {'interface': 'Vlan30',
                                                                                                                                           'is_best': False}}},
                                                                                             '192.168.30.0/32': {'next_hop': {'Drop': {'interface': 'Null0',
                                                                                                                                       'is_best': False}}},
                                                                                             '192.168.30.254/32': {'next_hop': {'Receive': {'interface': 'sup-eth1',
                                                                                                                                            'is_best': False}}},
                                                                                             '192.168.30.255/32': {'next_hop': {'Attached': {'interface': 'Vlan30',
                                                                                                                                             'is_best': False}}},
                                                                                             '255.255.255.255/32': {'next_hop': {'Receive': {'interface': 'sup-eth1',
                                                                                                                                             'is_best': False}}}}},
                                                                 'VRF_450/base': {'prefix': {'0.0.0.0/32': {'next_hop': {'Drop': {'interface': 'Null0',
                                                                                                                                  'is_best': False}}},
                                                                                             '127.0.0.0/8': {'next_hop': {'Drop': {'interface': 'Null0',
                                                                                                                                   'is_best': False}}},
                                                                                             '192.168.40.0/24': {'next_hop': {'Attached': {'interface': 'Vlan40',
                                                                                                                                           'is_best': False}}},
                                                                                             '192.168.40.0/32': {'next_hop': {'Drop': {'interface': 'Null0',
                                                                                                                                       'is_best': False}}},
                                                                                             '192.168.40.254/32': {'next_hop': {'Receive': {'interface': 'sup-eth1',
                                                                                                                                            'is_best': False}}},
                                                                                             '192.168.40.255/32': {'next_hop': {'Attached': {'interface': 'Vlan40',
                                                                                                                                             'is_best': False}}},
                                                                                             '192.168.50.0/24': {'next_hop': {'Attached': {'interface': 'Vlan50',
                                                                                                                                           'is_best': False}}},
                                                                                             '192.168.50.0/32': {'next_hop': {'Drop': {'interface': 'Null0',
                                                                                                                                       'is_best': False}}},
                                                                                             '192.168.50.254/32': {'next_hop': {'Receive': {'interface': 'sup-eth1',
                                                                                                                                            'is_best': False}}},
                                                                                             '192.168.50.255/32': {'next_hop': {'Attached': {'interface': 'Vlan50',
                                                                                                                                             'is_best': False}}},
                                                                                             '255.255.255.255/32': {'next_hop': {'Receive': {'interface': 'sup-eth1',
                                                                                                                                             'is_best': False}}}}},
                                                                 'VRF_Flow1_1/base': {'prefix': {'0.0.0.0/32': {'next_hop': {'Drop': {'interface': 'Null0',
                                                                                                                                      'is_best': False}}},
                                                                                                 '100.1.1.1/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501001'}}},
                                                                                                 '100.1.1.10/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                            'is_best': False,
                                                                                                                                            'label': 'vni:   501001'}}},
                                                                                                 '100.1.1.2/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501001'}}},
                                                                                                 '100.1.1.3/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501001'}}},
                                                                                                 '100.1.1.4/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501001'}}},
                                                                                                 '100.1.1.5/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501001'}}},
                                                                                                 '100.1.1.6/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501001'}}},
                                                                                                 '100.1.1.7/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501001'}}},
                                                                                                 '100.1.1.8/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501001'}}},
                                                                                                 '100.1.1.9/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501001'}}},
                                                                                                 '100.1.2.1/32': {'next_hop': {'192.168.21.2': {'interface': 'Ethernet1/3.21',
                                                                                                                                                'is_best': True}}},
                                                                                                 '100.1.2.10/32': {'next_hop': {'192.168.21.2': {'interface': 'Ethernet1/3.21',
                                                                                                                                                 'is_best': True}}},
                                                                                                 '100.1.2.2/32': {'next_hop': {'192.168.21.2': {'interface': 'Ethernet1/3.21',
                                                                                                                                                'is_best': True}}},
                                                                                                 '100.1.2.3/32': {'next_hop': {'192.168.21.2': {'interface': 'Ethernet1/3.21',
                                                                                                                                                'is_best': True}}},
                                                                                                 '100.1.2.4/32': {'next_hop': {'192.168.21.2': {'interface': 'Ethernet1/3.21',
                                                                                                                                                'is_best': True}}},
                                                                                                 '100.1.2.5/32': {'next_hop': {'192.168.21.2': {'interface': 'Ethernet1/3.21',
                                                                                                                                                'is_best': True}}},
                                                                                                 '100.1.2.6/32': {'next_hop': {'192.168.21.2': {'interface': 'Ethernet1/3.21',
                                                                                                                                                'is_best': True}}},
                                                                                                 '100.1.2.7/32': {'next_hop': {'192.168.21.2': {'interface': 'Ethernet1/3.21',
                                                                                                                                                'is_best': True}}},
                                                                                                 '100.1.2.8/32': {'next_hop': {'192.168.21.2': {'interface': 'Ethernet1/3.21',
                                                                                                                                                'is_best': True}}},
                                                                                                 '100.1.2.9/32': {'next_hop': {'192.168.21.2': {'interface': 'Ethernet1/3.21',
                                                                                                                                                'is_best': True}}},
                                                                                                 '100.1.3.1/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501001'}}},
                                                                                                 '100.1.3.10/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                            'is_best': False,
                                                                                                                                            'label': 'vni:   501001'}}},
                                                                                                 '100.1.3.2/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501001'}}},
                                                                                                 '100.1.3.3/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501001'}}},
                                                                                                 '100.1.3.4/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501001'}}},
                                                                                                 '100.1.3.5/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501001'}}},
                                                                                                 '100.1.3.6/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501001'}}},
                                                                                                 '100.1.3.7/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501001'}}},
                                                                                                 '100.1.3.8/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501001'}}},
                                                                                                 '100.1.3.9/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501001'}}},
                                                                                                 '100.1.4.1/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501001'}}},
                                                                                                 '100.1.4.10/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                            'is_best': False,
                                                                                                                                            'label': 'vni:   501001'}}},
                                                                                                 '100.1.4.2/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501001'}}},
                                                                                                 '100.1.4.3/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501001'}}},
                                                                                                 '100.1.4.4/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501001'}}},
                                                                                                 '100.1.4.5/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501001'}}},
                                                                                                 '100.1.4.6/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501001'}}},
                                                                                                 '100.1.4.7/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501001'}}},
                                                                                                 '100.1.4.8/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501001'}}},
                                                                                                 '100.1.4.9/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501001'}}},
                                                                                                 '127.0.0.0/8': {'next_hop': {'Drop': {'interface': 'Null0',
                                                                                                                                       'is_best': False}}},
                                                                                                 '192.168.21.0/24': {'next_hop': {'Attached': {'interface': 'Ethernet1/3.21',
                                                                                                                                               'is_best': False}}},
                                                                                                 '192.168.21.0/32': {'next_hop': {'Drop': {'interface': 'Null0',
                                                                                                                                           'is_best': False}}},
                                                                                                 '192.168.21.1/32': {'next_hop': {'Receive': {'interface': 'sup-eth1',
                                                                                                                                              'is_best': False}}},
                                                                                                 '192.168.21.2/32': {'next_hop': {'192.168.21.2': {'interface': 'Ethernet1/3.21',
                                                                                                                                                   'is_best': False}}},
                                                                                                 '192.168.21.255/32': {'next_hop': {'Attached': {'interface': 'Ethernet1/3.21',
                                                                                                                                                 'is_best': False}}},
                                                                                                 '255.255.255.255/32': {'next_hop': {'Receive': {'interface': 'sup-eth1',
                                                                                                                                                 'is_best': False}}}}},
                                                                 'VRF_Flow1_2/base': {'prefix': {'0.0.0.0/32': {'next_hop': {'Drop': {'interface': 'Null0',
                                                                                                                                      'is_best': False}}},
                                                                                                 '100.2.1.1/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501002'}}},
                                                                                                 '100.2.1.10/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                            'is_best': False,
                                                                                                                                            'label': 'vni:   501002'}}},
                                                                                                 '100.2.1.2/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501002'}}},
                                                                                                 '100.2.1.3/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501002'}}},
                                                                                                 '100.2.1.4/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501002'}}},
                                                                                                 '100.2.1.5/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501002'}}},
                                                                                                 '100.2.1.6/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501002'}}},
                                                                                                 '100.2.1.7/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501002'}}},
                                                                                                 '100.2.1.8/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501002'}}},
                                                                                                 '100.2.1.9/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501002'}}},
                                                                                                 '100.2.2.1/32': {'next_hop': {'192.168.22.2': {'interface': 'Ethernet1/3.22',
                                                                                                                                                'is_best': True}}},
                                                                                                 '100.2.2.10/32': {'next_hop': {'192.168.22.2': {'interface': 'Ethernet1/3.22',
                                                                                                                                                 'is_best': True}}},
                                                                                                 '100.2.2.2/32': {'next_hop': {'192.168.22.2': {'interface': 'Ethernet1/3.22',
                                                                                                                                                'is_best': True}}},
                                                                                                 '100.2.2.3/32': {'next_hop': {'192.168.22.2': {'interface': 'Ethernet1/3.22',
                                                                                                                                                'is_best': True}}},
                                                                                                 '100.2.2.4/32': {'next_hop': {'192.168.22.2': {'interface': 'Ethernet1/3.22',
                                                                                                                                                'is_best': True}}},
                                                                                                 '100.2.2.5/32': {'next_hop': {'192.168.22.2': {'interface': 'Ethernet1/3.22',
                                                                                                                                                'is_best': True}}},
                                                                                                 '100.2.2.6/32': {'next_hop': {'192.168.22.2': {'interface': 'Ethernet1/3.22',
                                                                                                                                                'is_best': True}}},
                                                                                                 '100.2.2.7/32': {'next_hop': {'192.168.22.2': {'interface': 'Ethernet1/3.22',
                                                                                                                                                'is_best': True}}},
                                                                                                 '100.2.2.8/32': {'next_hop': {'192.168.22.2': {'interface': 'Ethernet1/3.22',
                                                                                                                                                'is_best': True}}},
                                                                                                 '100.2.2.9/32': {'next_hop': {'192.168.22.2': {'interface': 'Ethernet1/3.22',
                                                                                                                                                'is_best': True}}},
                                                                                                 '100.2.3.1/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501002'}}},
                                                                                                 '100.2.3.10/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                            'is_best': False,
                                                                                                                                            'label': 'vni:   501002'}}},
                                                                                                 '100.2.3.2/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501002'}}},
                                                                                                 '100.2.3.3/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501002'}}},
                                                                                                 '100.2.3.4/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501002'}}},
                                                                                                 '100.2.3.5/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501002'}}},
                                                                                                 '100.2.3.6/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501002'}}},
                                                                                                 '100.2.3.7/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501002'}}},
                                                                                                 '100.2.3.8/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501002'}}},
                                                                                                 '100.2.3.9/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501002'}}},
                                                                                                 '100.2.4.1/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501002'}}},
                                                                                                 '100.2.4.10/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                            'is_best': False,
                                                                                                                                            'label': 'vni:   501002'}}},
                                                                                                 '100.2.4.2/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501002'}}},
                                                                                                 '100.2.4.3/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501002'}}},
                                                                                                 '100.2.4.4/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501002'}}},
                                                                                                 '100.2.4.5/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501002'}}},
                                                                                                 '100.2.4.6/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501002'}}},
                                                                                                 '100.2.4.7/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501002'}}},
                                                                                                 '100.2.4.8/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501002'}}},
                                                                                                 '100.2.4.9/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501002'}}},
                                                                                                 '127.0.0.0/8': {'next_hop': {'Drop': {'interface': 'Null0',
                                                                                                                                       'is_best': False}}},
                                                                                                 '192.168.22.0/24': {'next_hop': {'Attached': {'interface': 'Ethernet1/3.22',
                                                                                                                                               'is_best': False}}},
                                                                                                 '192.168.22.0/32': {'next_hop': {'Drop': {'interface': 'Null0',
                                                                                                                                           'is_best': False}}},
                                                                                                 '192.168.22.1/32': {'next_hop': {'Receive': {'interface': 'sup-eth1',
                                                                                                                                              'is_best': False}}},
                                                                                                 '192.168.22.2/32': {'next_hop': {'192.168.22.2': {'interface': 'Ethernet1/3.22',
                                                                                                                                                   'is_best': False}}},
                                                                                                 '192.168.22.255/32': {'next_hop': {'Attached': {'interface': 'Ethernet1/3.22',
                                                                                                                                                 'is_best': False}}},
                                                                                                 '255.255.255.255/32': {'next_hop': {'Receive': {'interface': 'sup-eth1',
                                                                                                                                                 'is_best': False}}}}},
                                                                 'VRF_Flow1_3/base': {'prefix': {'0.0.0.0/32': {'next_hop': {'Drop': {'interface': 'Null0',
                                                                                                                                      'is_best': False}}},
                                                                                                 '100.3.1.1/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501003'}}},
                                                                                                 '100.3.1.10/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                            'is_best': False,
                                                                                                                                            'label': 'vni:   501003'}}},
                                                                                                 '100.3.1.2/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501003'}}},
                                                                                                 '100.3.1.3/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501003'}}},
                                                                                                 '100.3.1.4/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501003'}}},
                                                                                                 '100.3.1.5/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501003'}}},
                                                                                                 '100.3.1.6/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501003'}}},
                                                                                                 '100.3.1.7/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501003'}}},
                                                                                                 '100.3.1.8/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501003'}}},
                                                                                                 '100.3.1.9/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501003'}}},
                                                                                                 '100.3.2.1/32': {'next_hop': {'192.168.23.2': {'interface': 'Ethernet1/3.23',
                                                                                                                                                'is_best': True}}},
                                                                                                 '100.3.2.10/32': {'next_hop': {'192.168.23.2': {'interface': 'Ethernet1/3.23',
                                                                                                                                                 'is_best': True}}},
                                                                                                 '100.3.2.2/32': {'next_hop': {'192.168.23.2': {'interface': 'Ethernet1/3.23',
                                                                                                                                                'is_best': True}}},
                                                                                                 '100.3.2.3/32': {'next_hop': {'192.168.23.2': {'interface': 'Ethernet1/3.23',
                                                                                                                                                'is_best': True}}},
                                                                                                 '100.3.2.4/32': {'next_hop': {'192.168.23.2': {'interface': 'Ethernet1/3.23',
                                                                                                                                                'is_best': True}}},
                                                                                                 '100.3.2.5/32': {'next_hop': {'192.168.23.2': {'interface': 'Ethernet1/3.23',
                                                                                                                                                'is_best': True}}},
                                                                                                 '100.3.2.6/32': {'next_hop': {'192.168.23.2': {'interface': 'Ethernet1/3.23',
                                                                                                                                                'is_best': True}}},
                                                                                                 '100.3.2.7/32': {'next_hop': {'192.168.23.2': {'interface': 'Ethernet1/3.23',
                                                                                                                                                'is_best': True}}},
                                                                                                 '100.3.2.8/32': {'next_hop': {'192.168.23.2': {'interface': 'Ethernet1/3.23',
                                                                                                                                                'is_best': True}}},
                                                                                                 '100.3.2.9/32': {'next_hop': {'192.168.23.2': {'interface': 'Ethernet1/3.23',
                                                                                                                                                'is_best': True}}},
                                                                                                 '100.3.3.1/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501003'}}},
                                                                                                 '100.3.3.10/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                            'is_best': False,
                                                                                                                                            'label': 'vni:   501003'}}},
                                                                                                 '100.3.3.2/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501003'}}},
                                                                                                 '100.3.3.3/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501003'}}},
                                                                                                 '100.3.3.4/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501003'}}},
                                                                                                 '100.3.3.5/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501003'}}},
                                                                                                 '100.3.3.6/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501003'}}},
                                                                                                 '100.3.3.7/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501003'}}},
                                                                                                 '100.3.3.8/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501003'}}},
                                                                                                 '100.3.3.9/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501003'}}},
                                                                                                 '100.3.4.1/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501003'}}},
                                                                                                 '100.3.4.10/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                            'is_best': False,
                                                                                                                                            'label': 'vni:   501003'}}},
                                                                                                 '100.3.4.2/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501003'}}},
                                                                                                 '100.3.4.3/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501003'}}},
                                                                                                 '100.3.4.4/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501003'}}},
                                                                                                 '100.3.4.5/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501003'}}},
                                                                                                 '100.3.4.6/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501003'}}},
                                                                                                 '100.3.4.7/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501003'}}},
                                                                                                 '100.3.4.8/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501003'}}},
                                                                                                 '100.3.4.9/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501003'}}},
                                                                                                 '127.0.0.0/8': {'next_hop': {'Drop': {'interface': 'Null0',
                                                                                                                                       'is_best': False}}},
                                                                                                 '192.168.23.0/24': {'next_hop': {'Attached': {'interface': 'Ethernet1/3.23',
                                                                                                                                               'is_best': False}}},
                                                                                                 '192.168.23.0/32': {'next_hop': {'Drop': {'interface': 'Null0',
                                                                                                                                           'is_best': False}}},
                                                                                                 '192.168.23.1/32': {'next_hop': {'Receive': {'interface': 'sup-eth1',
                                                                                                                                              'is_best': False}}},
                                                                                                 '192.168.23.2/32': {'next_hop': {'192.168.23.2': {'interface': 'Ethernet1/3.23',
                                                                                                                                                   'is_best': False}}},
                                                                                                 '192.168.23.255/32': {'next_hop': {'Attached': {'interface': 'Ethernet1/3.23',
                                                                                                                                                 'is_best': False}}},
                                                                                                 '255.255.255.255/32': {'next_hop': {'Receive': {'interface': 'sup-eth1',
                                                                                                                                                 'is_best': False}}}}},
                                                                 'VRF_Flow1_4/base': {'prefix': {'0.0.0.0/32': {'next_hop': {'Drop': {'interface': 'Null0',
                                                                                                                                      'is_best': False}}},
                                                                                                 '100.4.1.1/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501004'}}},
                                                                                                 '100.4.1.10/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                            'is_best': False,
                                                                                                                                            'label': 'vni:   501004'}}},
                                                                                                 '100.4.1.2/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501004'}}},
                                                                                                 '100.4.1.3/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501004'}}},
                                                                                                 '100.4.1.4/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501004'}}},
                                                                                                 '100.4.1.5/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501004'}}},
                                                                                                 '100.4.1.6/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501004'}}},
                                                                                                 '100.4.1.7/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501004'}}},
                                                                                                 '100.4.1.8/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501004'}}},
                                                                                                 '100.4.1.9/32': {'next_hop': {'1.1.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501004'}}},
                                                                                                 '100.4.2.1/32': {'next_hop': {'192.168.24.2': {'interface': 'Ethernet1/3.24',
                                                                                                                                                'is_best': True}}},
                                                                                                 '100.4.2.10/32': {'next_hop': {'192.168.24.2': {'interface': 'Ethernet1/3.24',
                                                                                                                                                 'is_best': True}}},
                                                                                                 '100.4.2.2/32': {'next_hop': {'192.168.24.2': {'interface': 'Ethernet1/3.24',
                                                                                                                                                'is_best': True}}},
                                                                                                 '100.4.2.3/32': {'next_hop': {'192.168.24.2': {'interface': 'Ethernet1/3.24',
                                                                                                                                                'is_best': True}}},
                                                                                                 '100.4.2.4/32': {'next_hop': {'192.168.24.2': {'interface': 'Ethernet1/3.24',
                                                                                                                                                'is_best': True}}},
                                                                                                 '100.4.2.5/32': {'next_hop': {'192.168.24.2': {'interface': 'Ethernet1/3.24',
                                                                                                                                                'is_best': True}}},
                                                                                                 '100.4.2.6/32': {'next_hop': {'192.168.24.2': {'interface': 'Ethernet1/3.24',
                                                                                                                                                'is_best': True}}},
                                                                                                 '100.4.2.7/32': {'next_hop': {'192.168.24.2': {'interface': 'Ethernet1/3.24',
                                                                                                                                                'is_best': True}}},
                                                                                                 '100.4.2.8/32': {'next_hop': {'192.168.24.2': {'interface': 'Ethernet1/3.24',
                                                                                                                                                'is_best': True}}},
                                                                                                 '100.4.2.9/32': {'next_hop': {'192.168.24.2': {'interface': 'Ethernet1/3.24',
                                                                                                                                                'is_best': True}}},
                                                                                                 '100.4.3.1/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501004'}}},
                                                                                                 '100.4.3.10/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                            'is_best': False,
                                                                                                                                            'label': 'vni:   501004'}}},
                                                                                                 '100.4.3.2/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501004'}}},
                                                                                                 '100.4.3.3/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501004'}}},
                                                                                                 '100.4.3.4/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501004'}}},
                                                                                                 '100.4.3.5/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501004'}}},
                                                                                                 '100.4.3.6/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501004'}}},
                                                                                                 '100.4.3.7/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501004'}}},
                                                                                                 '100.4.3.8/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501004'}}},
                                                                                                 '100.4.3.9/32': {'next_hop': {'3.3.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501004'}}},
                                                                                                 '100.4.4.1/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501004'}}},
                                                                                                 '100.4.4.10/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                            'is_best': False,
                                                                                                                                            'label': 'vni:   501004'}}},
                                                                                                 '100.4.4.2/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501004'}}},
                                                                                                 '100.4.4.3/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501004'}}},
                                                                                                 '100.4.4.4/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501004'}}},
                                                                                                 '100.4.4.5/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501004'}}},
                                                                                                 '100.4.4.6/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501004'}}},
                                                                                                 '100.4.4.7/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501004'}}},
                                                                                                 '100.4.4.8/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501004'}}},
                                                                                                 '100.4.4.9/32': {'next_hop': {'4.4.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501004'}}},
                                                                                                 '192.168.24.0/24': {'next_hop': {'Attached': {'interface': 'Ethernet1/3.24',
                                                                                                                                               'is_best': False}}},
                                                                                                 '192.168.24.0/32': {'next_hop': {'Drop': {'interface': 'Null0',
                                                                                                                                           'is_best': False}}},
                                                                                                 '192.168.24.1/32': {'next_hop': {'Receive': {'interface': 'sup-eth1',
                                                                                                                                              'is_best': False}}},
                                                                                                 '192.168.24.2/32': {'next_hop': {'192.168.24.2': {'interface': 'Ethernet1/3.24',
                                                                                                                                                   'is_best': False}}},
                                                                                                 '192.168.24.255/32': {'next_hop': {'Attached': {'interface': 'Ethernet1/3.24',
                                                                                                                                                 'is_best': False}}}}},
                                                                 'default/base': {'prefix': {'0.0.0.0/32': {'next_hop': {'Drop': {'interface': 'Null0',
                                                                                                                                  'is_best': False}}},
                                                                                             '1.1.1.1/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                      'is_best': False},
                                                                                                                         '20.2.1.2': {'interface': 'Ethernet1/2',
                                                                                                                                      'is_best': False}}},
                                                                                             '1.1.1.2/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                      'is_best': True},
                                                                                                                         '20.2.1.2': {'interface': 'Ethernet1/2',
                                                                                                                                      'is_best': False}}},
                                                                                             '10.1.1.0/24': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                       'is_best': False}}},
                                                                                             '10.2.1.0/24': {'next_hop': {'Attached': {'interface': 'Ethernet1/1',
                                                                                                                                       'is_best': False}}},
                                                                                             '10.2.1.0/32': {'next_hop': {'Drop': {'interface': 'Null0',
                                                                                                                                   'is_best': False}}},
                                                                                             '10.2.1.1/32': {'next_hop': {'Receive': {'interface': 'sup-eth1',
                                                                                                                                      'is_best': False}}},
                                                                                             '10.2.1.2/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                       'is_best': False}}},
                                                                                             '10.2.1.255/32': {'next_hop': {'Attached': {'interface': 'Ethernet1/1',
                                                                                                                                         'is_best': False}}},
                                                                                             '10.3.1.0/24': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                       'is_best': False}}},
                                                                                             '10.4.1.0/24': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                       'is_best': False}}},
                                                                                             '111.111.111.0/24': {'next_hop': {'Drop': {'interface': 'Null0',
                                                                                                                                        'is_best': False}}},
                                                                                             '127.0.0.0/8': {'next_hop': {'Drop': {'interface': 'Null0',
                                                                                                                                   'is_best': False}}},
                                                                                             '2.2.2.1/32': {'next_hop': {'Receive': {'interface': 'sup-eth1',
                                                                                                                                     'is_best': False}}},
                                                                                             '2.2.2.2/32': {'next_hop': {'Receive': {'interface': 'sup-eth1',
                                                                                                                                     'is_best': False}}},
                                                                                             '20.1.1.0/24': {'next_hop': {'20.2.1.2': {'interface': 'Ethernet1/2',
                                                                                                                                       'is_best': False}}},
                                                                                             '20.2.1.0/24': {'next_hop': {'Attached': {'interface': 'Ethernet1/2',
                                                                                                                                       'is_best': False}}},
                                                                                             '20.2.1.0/32': {'next_hop': {'Drop': {'interface': 'Null0',
                                                                                                                                   'is_best': False}}},
                                                                                             '20.2.1.1/32': {'next_hop': {'Receive': {'interface': 'sup-eth1',
                                                                                                                                      'is_best': False}}},
                                                                                             '20.2.1.2/32': {'next_hop': {'20.2.1.2': {'interface': 'Ethernet1/2',
                                                                                                                                       'is_best': False}}},
                                                                                             '20.2.1.255/32': {'next_hop': {'Attached': {'interface': 'Ethernet1/2',
                                                                                                                                         'is_best': False}}},
                                                                                             '20.3.1.0/24': {'next_hop': {'20.2.1.2': {'interface': 'Ethernet1/2',
                                                                                                                                       'is_best': False}}},
                                                                                             '20.4.1.0/24': {'next_hop': {'20.2.1.2': {'interface': 'Ethernet1/2',
                                                                                                                                       'is_best': False}}},
                                                                                             '200.200.200.1/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                            'is_best': False}}},
                                                                                             '25.25.0.0/16': {'next_hop': {'Drop': {'interface': 'Null0',
                                                                                                                                    'is_best': False}}},
                                                                                             '25.25.25.0/24': {'next_hop': {'Drop': {'interface': 'Null0',
                                                                                                                                     'is_best': False}}},
                                                                                             '255.255.255.255/32': {'next_hop': {'Receive': {'interface': 'sup-eth1',
                                                                                                                                             'is_best': False}}},
                                                                                             '3.3.3.1/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                      'is_best': False},
                                                                                                                         '20.2.1.2': {'interface': 'Ethernet1/2',
                                                                                                                                      'is_best': False}}},
                                                                                             '3.3.3.2/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                      'is_best': True},
                                                                                                                         '20.2.1.2': {'interface': 'Ethernet1/2',
                                                                                                                                      'is_best': False}}},
                                                                                             '4.4.4.1/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                      'is_best': False},
                                                                                                                         '20.2.1.2': {'interface': 'Ethernet1/2',
                                                                                                                                      'is_best': False}}},
                                                                                             '4.4.4.2/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                      'is_best': True},
                                                                                                                         '20.2.1.2': {'interface': 'Ethernet1/2',
                                                                                                                                      'is_best': False}}},
                                                                                             '98.98.98.98/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                          'is_best': False}}},
                                                                                             '99.99.99.99/32': {'next_hop': {'20.2.1.2': {'interface': 'Ethernet1/2',
                                                                                                                                          'is_best': False}}}}}}}}}}}
    golden_output = {'execute.return_value':'''
        #vtep1 show forwarding ipv4 vrf all 
        slot  1
        =======
        
        
        IPv4 routes for table default/base
        
        ------------------+-----------------------------------------+----------------------+-----------------+-----------------
        Prefix            | Next-hop                                | Interface            | Labels          | Partial Install 
        ------------------+-----------------------------------------+----------------------+-----------------+-----------------
        1.1.1.1/32           10.2.1.2                                  Ethernet1/1         
        *1.1.1.2/32          10.2.1.2                                  Ethernet1/1         
        2.2.2.1/32           Receive                                   sup-eth1
        2.2.2.2/32           Receive                                   sup-eth1
        3.3.3.1/32           10.2.1.2                                  Ethernet1/1         
        *3.3.3.2/32          10.2.1.2                                  Ethernet1/1         
        4.4.4.1/32           10.2.1.2                                  Ethernet1/1         
        *4.4.4.2/32          10.2.1.2                                  Ethernet1/1         
        10.2.1.0/32          Drop                                      Null0
        10.2.1.1/32          Receive                                   sup-eth1
        10.2.1.2/32          10.2.1.2                                  Ethernet1/1         
        10.2.1.255/32        Attached                                  Ethernet1/1
        20.2.1.0/32          Drop                                      Null0
        20.2.1.1/32          Receive                                   sup-eth1
        20.2.1.2/32          20.2.1.2                                  Ethernet1/2         
        20.2.1.255/32        Attached                                  Ethernet1/2
        98.98.98.98/32       10.2.1.2                                  Ethernet1/1         
        99.99.99.99/32       20.2.1.2                                  Ethernet1/2         
        200.200.200.1/32     10.2.1.2                                  Ethernet1/1         
        IPv4 routes for table VRF_230/base
        
        ------------------+-----------------------------------------+----------------------+-----------------+-----------------
        Prefix            | Next-hop                                | Interface            | Labels          | Partial Install 
        ------------------+-----------------------------------------+----------------------+-----------------+-----------------
        192.168.20.0/24      Attached                                  Vlan20
        192.168.20.0/32      Drop                                      Null0
        192.168.20.254/32    Receive                                   sup-eth1
        192.168.20.255/32    Attached                                  Vlan20
        192.168.30.0/24      Attached                                  Vlan30
        192.168.30.0/32      Drop                                      Null0
        192.168.30.254/32    Receive                                   sup-eth1
        192.168.30.255/32    Attached                                  Vlan30
        IPv4 routes for table VRF_450/base
        
        ------------------+-----------------------------------------+----------------------+-----------------+-----------------
        Prefix            | Next-hop                                | Interface            | Labels          | Partial Install 
        ------------------+-----------------------------------------+----------------------+-----------------+-----------------
        192.168.40.0/24      Attached                                  Vlan40
        192.168.40.0/32      Drop                                      Null0
        192.168.40.254/32    Receive                                   sup-eth1
        192.168.40.255/32    Attached                                  Vlan40
        192.168.50.0/24      Attached                                  Vlan50
        192.168.50.0/32      Drop                                      Null0
        192.168.50.254/32    Receive                                   sup-eth1
        192.168.50.255/32    Attached                                  Vlan50
        IPv4 routes for table VRF_Flow1_1/base
        
        ------------------+-----------------------------------------+----------------------+-----------------+-----------------
        Prefix            | Next-hop                                | Interface            | Labels          | Partial Install 
        ------------------+-----------------------------------------+----------------------+-----------------+-----------------
        100.1.1.1/32         1.1.1.2            nve1        vni:   501001    
        100.1.1.2/32         1.1.1.2            nve1        vni:   501001    
        100.1.1.3/32         1.1.1.2            nve1        vni:   501001    
        100.1.1.4/32         1.1.1.2            nve1        vni:   501001    
        100.1.1.5/32         1.1.1.2            nve1        vni:   501001    
        100.1.1.6/32         1.1.1.2            nve1        vni:   501001    
        100.1.1.7/32         1.1.1.2            nve1        vni:   501001    
        100.1.1.8/32         1.1.1.2            nve1        vni:   501001    
        100.1.1.9/32         1.1.1.2            nve1        vni:   501001    
        100.1.1.10/32        1.1.1.2            nve1        vni:   501001    
        *100.1.2.1/32        192.168.21.2                              Ethernet1/3.21      
        *100.1.2.2/32        192.168.21.2                              Ethernet1/3.21      
        *100.1.2.3/32        192.168.21.2                              Ethernet1/3.21      
        *100.1.2.4/32        192.168.21.2                              Ethernet1/3.21      
        *100.1.2.5/32        192.168.21.2                              Ethernet1/3.21      
        *100.1.2.6/32        192.168.21.2                              Ethernet1/3.21      
        *100.1.2.7/32        192.168.21.2                              Ethernet1/3.21      
        *100.1.2.8/32        192.168.21.2                              Ethernet1/3.21      
        *100.1.2.9/32        192.168.21.2                              Ethernet1/3.21      
        *100.1.2.10/32       192.168.21.2                              Ethernet1/3.21      
        100.1.3.1/32         3.3.3.2            nve1        vni:   501001    
        100.1.3.2/32         3.3.3.2            nve1        vni:   501001    
        100.1.3.3/32         3.3.3.2            nve1        vni:   501001    
        100.1.3.4/32         3.3.3.2            nve1        vni:   501001    
        100.1.3.5/32         3.3.3.2            nve1        vni:   501001    
        100.1.3.6/32         3.3.3.2            nve1        vni:   501001    
        100.1.3.7/32         3.3.3.2            nve1        vni:   501001    
        100.1.3.8/32         3.3.3.2            nve1        vni:   501001    
        100.1.3.9/32         3.3.3.2            nve1        vni:   501001    
        100.1.3.10/32        3.3.3.2            nve1        vni:   501001    
        100.1.4.1/32         4.4.4.2            nve1        vni:   501001    
        100.1.4.2/32         4.4.4.2            nve1        vni:   501001    
        100.1.4.3/32         4.4.4.2            nve1        vni:   501001    
        100.1.4.4/32         4.4.4.2            nve1        vni:   501001    
        100.1.4.5/32         4.4.4.2            nve1        vni:   501001    
        100.1.4.6/32         4.4.4.2            nve1        vni:   501001    
        100.1.4.7/32         4.4.4.2            nve1        vni:   501001    
        100.1.4.8/32         4.4.4.2            nve1        vni:   501001    
        100.1.4.9/32         4.4.4.2            nve1        vni:   501001    
        100.1.4.10/32        4.4.4.2            nve1        vni:   501001    
        192.168.21.0/24      Attached                                  Ethernet1/3.21
        192.168.21.0/32      Drop                                      Null0
        192.168.21.1/32      Receive                                   sup-eth1
        192.168.21.2/32      192.168.21.2                              Ethernet1/3.21      
        192.168.21.255/32    Attached                                  Ethernet1/3.21
        IPv4 routes for table VRF_Flow1_2/base
        
        ------------------+-----------------------------------------+----------------------+-----------------+-----------------
        Prefix            | Next-hop                                | Interface            | Labels          | Partial Install 
        ------------------+-----------------------------------------+----------------------+-----------------+-----------------
        100.2.1.1/32         1.1.1.2            nve1        vni:   501002    
        100.2.1.2/32         1.1.1.2            nve1        vni:   501002    
        100.2.1.3/32         1.1.1.2            nve1        vni:   501002    
        100.2.1.4/32         1.1.1.2            nve1        vni:   501002    
        100.2.1.5/32         1.1.1.2            nve1        vni:   501002    
        100.2.1.6/32         1.1.1.2            nve1        vni:   501002    
        100.2.1.7/32         1.1.1.2            nve1        vni:   501002    
        100.2.1.8/32         1.1.1.2            nve1        vni:   501002    
        100.2.1.9/32         1.1.1.2            nve1        vni:   501002    
        100.2.1.10/32        1.1.1.2            nve1        vni:   501002    
        *100.2.2.1/32        192.168.22.2                              Ethernet1/3.22      
        *100.2.2.2/32        192.168.22.2                              Ethernet1/3.22      
        *100.2.2.3/32        192.168.22.2                              Ethernet1/3.22      
        *100.2.2.4/32        192.168.22.2                              Ethernet1/3.22      
        *100.2.2.5/32        192.168.22.2                              Ethernet1/3.22      
        *100.2.2.6/32        192.168.22.2                              Ethernet1/3.22      
        *100.2.2.7/32        192.168.22.2                              Ethernet1/3.22      
        *100.2.2.8/32        192.168.22.2                              Ethernet1/3.22      
        *100.2.2.9/32        192.168.22.2                              Ethernet1/3.22      
        *100.2.2.10/32       192.168.22.2                              Ethernet1/3.22      
        100.2.3.1/32         3.3.3.2            nve1        vni:   501002    
        100.2.3.2/32         3.3.3.2            nve1        vni:   501002    
        100.2.3.3/32         3.3.3.2            nve1        vni:   501002    
        100.2.3.4/32         3.3.3.2            nve1        vni:   501002    
        100.2.3.5/32         3.3.3.2            nve1        vni:   501002    
        100.2.3.6/32         3.3.3.2            nve1        vni:   501002    
        100.2.3.7/32         3.3.3.2            nve1        vni:   501002    
        100.2.3.8/32         3.3.3.2            nve1        vni:   501002    
        100.2.3.9/32         3.3.3.2            nve1        vni:   501002    
        100.2.3.10/32        3.3.3.2            nve1        vni:   501002    
        100.2.4.1/32         4.4.4.2            nve1        vni:   501002    
        100.2.4.2/32         4.4.4.2            nve1        vni:   501002    
        100.2.4.3/32         4.4.4.2            nve1        vni:   501002    
        100.2.4.4/32         4.4.4.2            nve1        vni:   501002    
        100.2.4.5/32         4.4.4.2            nve1        vni:   501002    
        100.2.4.6/32         4.4.4.2            nve1        vni:   501002    
        100.2.4.7/32         4.4.4.2            nve1        vni:   501002    
        100.2.4.8/32         4.4.4.2            nve1        vni:   501002    
        100.2.4.9/32         4.4.4.2            nve1        vni:   501002    
        100.2.4.10/32        4.4.4.2            nve1        vni:   501002    
        192.168.22.0/24      Attached                                  Ethernet1/3.22
        192.168.22.0/32      Drop                                      Null0
        192.168.22.1/32      Receive                                   sup-eth1
        192.168.22.2/32      192.168.22.2                              Ethernet1/3.22      
        192.168.22.255/32    Attached                                  Ethernet1/3.22
        IPv4 routes for table VRF_Flow1_3/base
        
        ------------------+-----------------------------------------+----------------------+-----------------+-----------------
        Prefix            | Next-hop                                | Interface            | Labels          | Partial Install 
        ------------------+-----------------------------------------+----------------------+-----------------+-----------------
        100.3.1.1/32         1.1.1.2            nve1        vni:   501003    
        100.3.1.2/32         1.1.1.2            nve1        vni:   501003    
        100.3.1.3/32         1.1.1.2            nve1        vni:   501003    
        100.3.1.4/32         1.1.1.2            nve1        vni:   501003    
        100.3.1.5/32         1.1.1.2            nve1        vni:   501003    
        100.3.1.6/32         1.1.1.2            nve1        vni:   501003    
        100.3.1.7/32         1.1.1.2            nve1        vni:   501003    
        100.3.1.8/32         1.1.1.2            nve1        vni:   501003    
        100.3.1.9/32         1.1.1.2            nve1        vni:   501003    
        100.3.1.10/32        1.1.1.2            nve1        vni:   501003    
        *100.3.2.1/32        192.168.23.2                              Ethernet1/3.23      
        *100.3.2.2/32        192.168.23.2                              Ethernet1/3.23      
        *100.3.2.3/32        192.168.23.2                              Ethernet1/3.23      
        *100.3.2.4/32        192.168.23.2                              Ethernet1/3.23      
        *100.3.2.5/32        192.168.23.2                              Ethernet1/3.23      
        *100.3.2.6/32        192.168.23.2                              Ethernet1/3.23      
        *100.3.2.7/32        192.168.23.2                              Ethernet1/3.23      
        *100.3.2.8/32        192.168.23.2                              Ethernet1/3.23      
        *100.3.2.9/32        192.168.23.2                              Ethernet1/3.23      
        *100.3.2.10/32       192.168.23.2                              Ethernet1/3.23      
        100.3.3.1/32         3.3.3.2            nve1        vni:   501003    
        100.3.3.2/32         3.3.3.2            nve1        vni:   501003    
        100.3.3.3/32         3.3.3.2            nve1        vni:   501003    
        100.3.3.4/32         3.3.3.2            nve1        vni:   501003    
        100.3.3.5/32         3.3.3.2            nve1        vni:   501003    
        100.3.3.6/32         3.3.3.2            nve1        vni:   501003    
        100.3.3.7/32         3.3.3.2            nve1        vni:   501003    
        100.3.3.8/32         3.3.3.2            nve1        vni:   501003    
        100.3.3.9/32         3.3.3.2            nve1        vni:   501003    
        100.3.3.10/32        3.3.3.2            nve1        vni:   501003    
        100.3.4.1/32         4.4.4.2            nve1        vni:   501003    
        100.3.4.2/32         4.4.4.2            nve1        vni:   501003    
        100.3.4.3/32         4.4.4.2            nve1        vni:   501003    
        100.3.4.4/32         4.4.4.2            nve1        vni:   501003    
        100.3.4.5/32         4.4.4.2            nve1        vni:   501003    
        100.3.4.6/32         4.4.4.2            nve1        vni:   501003    
        100.3.4.7/32         4.4.4.2            nve1        vni:   501003    
        100.3.4.8/32         4.4.4.2            nve1        vni:   501003    
        100.3.4.9/32         4.4.4.2            nve1        vni:   501003    
        100.3.4.10/32        4.4.4.2            nve1        vni:   501003    
        192.168.23.0/24      Attached                                  Ethernet1/3.23
        192.168.23.0/32      Drop                                      Null0
        192.168.23.1/32      Receive                                   sup-eth1
        192.168.23.2/32      192.168.23.2                              Ethernet1/3.23      
        192.168.23.255/32    Attached                                  Ethernet1/3.23
        IPv4 routes for table VRF_Flow1_4/base
        
        ------------------+-----------------------------------------+----------------------+-----------------+-----------------
        Prefix            | Next-hop                                | Interface            | Labels          | Partial Install 
        ------------------+-----------------------------------------+----------------------+-----------------+-----------------
        100.4.1.1/32         1.1.1.2            nve1        vni:   501004    
        100.4.1.2/32         1.1.1.2            nve1        vni:   501004    
        100.4.1.3/32         1.1.1.2            nve1        vni:   501004    
        100.4.1.4/32         1.1.1.2            nve1        vni:   501004    
        100.4.1.5/32         1.1.1.2            nve1        vni:   501004    
        100.4.1.6/32         1.1.1.2            nve1        vni:   501004    
        100.4.1.7/32         1.1.1.2            nve1        vni:   501004    
        100.4.1.8/32         1.1.1.2            nve1        vni:   501004    
        100.4.1.9/32         1.1.1.2            nve1        vni:   501004    
        100.4.1.10/32        1.1.1.2            nve1        vni:   501004    
        *100.4.2.1/32        192.168.24.2                              Ethernet1/3.24      
        *100.4.2.2/32        192.168.24.2                              Ethernet1/3.24      
        *100.4.2.3/32        192.168.24.2                              Ethernet1/3.24      
        *100.4.2.4/32        192.168.24.2                              Ethernet1/3.24      
        *100.4.2.5/32        192.168.24.2                              Ethernet1/3.24      
        *100.4.2.6/32        192.168.24.2                              Ethernet1/3.24      
        *100.4.2.7/32        192.168.24.2                              Ethernet1/3.24      
        *100.4.2.8/32        192.168.24.2                              Ethernet1/3.24      
        *100.4.2.9/32        192.168.24.2                              Ethernet1/3.24      
        *100.4.2.10/32       192.168.24.2                              Ethernet1/3.24      
        100.4.3.1/32         3.3.3.2            nve1        vni:   501004    
        100.4.3.2/32         3.3.3.2            nve1        vni:   501004    
        100.4.3.3/32         3.3.3.2            nve1        vni:   501004    
        100.4.3.4/32         3.3.3.2            nve1        vni:   501004    
        100.4.3.5/32         3.3.3.2            nve1        vni:   501004    
        100.4.3.6/32         3.3.3.2            nve1        vni:   501004    
        100.4.3.7/32         3.3.3.2            nve1        vni:   501004    
        100.4.3.8/32         3.3.3.2            nve1        vni:   501004    
        100.4.3.9/32         3.3.3.2            nve1        vni:   501004    
        100.4.3.10/32        3.3.3.2            nve1        vni:   501004    
        100.4.4.1/32         4.4.4.2            nve1        vni:   501004    
        100.4.4.2/32         4.4.4.2            nve1        vni:   501004    
        100.4.4.3/32         4.4.4.2            nve1        vni:   501004    
        100.4.4.4/32         4.4.4.2            nve1        vni:   501004    
        100.4.4.5/32         4.4.4.2            nve1        vni:   501004    
        100.4.4.6/32         4.4.4.2            nve1        vni:   501004    
        100.4.4.7/32         4.4.4.2            nve1        vni:   501004    
        100.4.4.8/32         4.4.4.2            nve1        vni:   501004    
        100.4.4.9/32         4.4.4.2            nve1        vni:   501004    
        100.4.4.10/32        4.4.4.2            nve1        vni:   501004    
        192.168.24.0/24      Attached                                  Ethernet1/3.24
        192.168.24.0/32      Drop                                      Null0
        192.168.24.1/32      Receive                                   sup-eth1
        192.168.24.2/32      192.168.24.2                              Ethernet1/3.24      
        192.168.24.255/32    Attached                                  Ethernet1/3.24
        
        slot 27
        =======
        
        
        IPv4 routes for table default/base
        
        ------------------+-----------------------------------------+----------------------+-----------------+-----------------
        Prefix            | Next-hop                                | Interface            | Labels          | Partial Install 
        ------------------+-----------------------------------------+----------------------+-----------------+-----------------
        0.0.0.0/32           Drop                                      Null0
        127.0.0.0/8          Drop                                      Null0
        255.255.255.255/32   Receive                                   sup-eth1
        1.1.1.1/32           10.2.1.2                                  Ethernet1/1         
                             20.2.1.2                                  Ethernet1/2         
        *1.1.1.2/32          10.2.1.2                                  Ethernet1/1         
                             20.2.1.2                                  Ethernet1/2         
        2.2.2.1/32           Receive                                   sup-eth1
        2.2.2.2/32           Receive                                   sup-eth1
        3.3.3.1/32           10.2.1.2                                  Ethernet1/1         
                             20.2.1.2                                  Ethernet1/2         
        *3.3.3.2/32          10.2.1.2                                  Ethernet1/1         
                             20.2.1.2                                  Ethernet1/2         
        4.4.4.1/32           10.2.1.2                                  Ethernet1/1         
                             20.2.1.2                                  Ethernet1/2         
        *4.4.4.2/32          10.2.1.2                                  Ethernet1/1         
                             20.2.1.2                                  Ethernet1/2         
        10.1.1.0/24          10.2.1.2                                  Ethernet1/1         
        10.2.1.0/24          Attached                                  Ethernet1/1
        10.2.1.0/32          Drop                                      Null0
        10.2.1.1/32          Receive                                   sup-eth1
        10.2.1.2/32          10.2.1.2                                  Ethernet1/1         
        10.2.1.255/32        Attached                                  Ethernet1/1
        10.3.1.0/24          10.2.1.2                                  Ethernet1/1         
        10.4.1.0/24          10.2.1.2                                  Ethernet1/1         
        20.1.1.0/24          20.2.1.2                                  Ethernet1/2         
        20.2.1.0/24          Attached                                  Ethernet1/2
        20.2.1.0/32          Drop                                      Null0
        20.2.1.1/32          Receive                                   sup-eth1
        20.2.1.2/32          20.2.1.2                                  Ethernet1/2         
        20.2.1.255/32        Attached                                  Ethernet1/2
        20.3.1.0/24          20.2.1.2                                  Ethernet1/2         
        20.4.1.0/24          20.2.1.2                                  Ethernet1/2         
        25.25.0.0/16         Drop                                      Null0
        25.25.25.0/24        Drop                                      Null0
        98.98.98.98/32       10.2.1.2                                  Ethernet1/1         
        99.99.99.99/32       20.2.1.2                                  Ethernet1/2         
        111.111.111.0/24     Drop                                      Null0
        200.200.200.1/32     10.2.1.2                                  Ethernet1/1         
        IPv4 routes for table VRF_230/base
        
        ------------------+-----------------------------------------+----------------------+-----------------+-----------------
        Prefix            | Next-hop                                | Interface            | Labels          | Partial Install 
        ------------------+-----------------------------------------+----------------------+-----------------+-----------------
        0.0.0.0/32           Drop                                      Null0
        127.0.0.0/8          Drop                                      Null0
        255.255.255.255/32   Receive                                   sup-eth1
        192.168.20.0/24      Attached                                  Vlan20
        192.168.20.0/32      Drop                                      Null0
        192.168.20.254/32    Receive                                   sup-eth1
        192.168.20.255/32    Attached                                  Vlan20
        192.168.30.0/24      Attached                                  Vlan30
        192.168.30.0/32      Drop                                      Null0
        192.168.30.254/32    Receive                                   sup-eth1
        192.168.30.255/32    Attached                                  Vlan30
        IPv4 routes for table VRF_450/base
        
        ------------------+-----------------------------------------+----------------------+-----------------+-----------------
        Prefix            | Next-hop                                | Interface            | Labels          | Partial Install 
        ------------------+-----------------------------------------+----------------------+-----------------+-----------------
        0.0.0.0/32           Drop                                      Null0
        127.0.0.0/8          Drop                                      Null0
        255.255.255.255/32   Receive                                   sup-eth1
        192.168.40.0/24      Attached                                  Vlan40
        192.168.40.0/32      Drop                                      Null0
        192.168.40.254/32    Receive                                   sup-eth1
        192.168.40.255/32    Attached                                  Vlan40
        192.168.50.0/24      Attached                                  Vlan50
        192.168.50.0/32      Drop                                      Null0
        192.168.50.254/32    Receive                                   sup-eth1
        192.168.50.255/32    Attached                                  Vlan50
        IPv4 routes for table VRF_Flow1_1/base
        
        ------------------+-----------------------------------------+----------------------+-----------------+-----------------
        Prefix            | Next-hop                                | Interface            | Labels          | Partial Install 
        ------------------+-----------------------------------------+----------------------+-----------------+-----------------
        0.0.0.0/32           Drop                                      Null0
        127.0.0.0/8          Drop                                      Null0
        255.255.255.255/32   Receive                                   sup-eth1
        100.1.1.1/32         1.1.1.2            nve1        vni:   501001    
        100.1.1.2/32         1.1.1.2            nve1        vni:   501001    
        100.1.1.3/32         1.1.1.2            nve1        vni:   501001    
        100.1.1.4/32         1.1.1.2            nve1        vni:   501001    
        100.1.1.5/32         1.1.1.2            nve1        vni:   501001    
        100.1.1.6/32         1.1.1.2            nve1        vni:   501001    
        100.1.1.7/32         1.1.1.2            nve1        vni:   501001    
        100.1.1.8/32         1.1.1.2            nve1        vni:   501001    
        100.1.1.9/32         1.1.1.2            nve1        vni:   501001    
        100.1.1.10/32        1.1.1.2            nve1        vni:   501001    
        *100.1.2.1/32        192.168.21.2                              Ethernet1/3.21      
        *100.1.2.2/32        192.168.21.2                              Ethernet1/3.21      
        *100.1.2.3/32        192.168.21.2                              Ethernet1/3.21      
        *100.1.2.4/32        192.168.21.2                              Ethernet1/3.21      
        *100.1.2.5/32        192.168.21.2                              Ethernet1/3.21      
        *100.1.2.6/32        192.168.21.2                              Ethernet1/3.21      
        *100.1.2.7/32        192.168.21.2                              Ethernet1/3.21      
        *100.1.2.8/32        192.168.21.2                              Ethernet1/3.21      
        *100.1.2.9/32        192.168.21.2                              Ethernet1/3.21      
        *100.1.2.10/32       192.168.21.2                              Ethernet1/3.21      
        100.1.3.1/32         3.3.3.2            nve1        vni:   501001    
        100.1.3.2/32         3.3.3.2            nve1        vni:   501001    
        100.1.3.3/32         3.3.3.2            nve1        vni:   501001    
        100.1.3.4/32         3.3.3.2            nve1        vni:   501001    
        100.1.3.5/32         3.3.3.2            nve1        vni:   501001    
        100.1.3.6/32         3.3.3.2            nve1        vni:   501001    
        100.1.3.7/32         3.3.3.2            nve1        vni:   501001    
        100.1.3.8/32         3.3.3.2            nve1        vni:   501001    
        100.1.3.9/32         3.3.3.2            nve1        vni:   501001    
        100.1.3.10/32        3.3.3.2            nve1        vni:   501001    
        100.1.4.1/32         4.4.4.2            nve1        vni:   501001    
        100.1.4.2/32         4.4.4.2            nve1        vni:   501001    
        100.1.4.3/32         4.4.4.2            nve1        vni:   501001    
        100.1.4.4/32         4.4.4.2            nve1        vni:   501001    
        100.1.4.5/32         4.4.4.2            nve1        vni:   501001    
        100.1.4.6/32         4.4.4.2            nve1        vni:   501001    
        100.1.4.7/32         4.4.4.2            nve1        vni:   501001    
        100.1.4.8/32         4.4.4.2            nve1        vni:   501001    
        100.1.4.9/32         4.4.4.2            nve1        vni:   501001    
        100.1.4.10/32        4.4.4.2            nve1        vni:   501001    
        192.168.21.0/24      Attached                                  Ethernet1/3.21
        192.168.21.0/32      Drop                                      Null0
        192.168.21.1/32      Receive                                   sup-eth1
        192.168.21.2/32      192.168.21.2                              Ethernet1/3.21      
        192.168.21.255/32    Attached                                  Ethernet1/3.21
        IPv4 routes for table VRF_Flow1_2/base
        
        ------------------+-----------------------------------------+----------------------+-----------------+-----------------
        Prefix            | Next-hop                                | Interface            | Labels          | Partial Install 
        ------------------+-----------------------------------------+----------------------+-----------------+-----------------
        0.0.0.0/32           Drop                                      Null0
        127.0.0.0/8          Drop                                      Null0
        255.255.255.255/32   Receive                                   sup-eth1
        100.2.1.1/32         1.1.1.2            nve1        vni:   501002    
        100.2.1.2/32         1.1.1.2            nve1        vni:   501002    
        100.2.1.3/32         1.1.1.2            nve1        vni:   501002    
        100.2.1.4/32         1.1.1.2            nve1        vni:   501002    
        100.2.1.5/32         1.1.1.2            nve1        vni:   501002    
        100.2.1.6/32         1.1.1.2            nve1        vni:   501002    
        100.2.1.7/32         1.1.1.2            nve1        vni:   501002    
        100.2.1.8/32         1.1.1.2            nve1        vni:   501002    
        100.2.1.9/32         1.1.1.2            nve1        vni:   501002    
        100.2.1.10/32        1.1.1.2            nve1        vni:   501002    
        *100.2.2.1/32        192.168.22.2                              Ethernet1/3.22      
        *100.2.2.2/32        192.168.22.2                              Ethernet1/3.22      
        *100.2.2.3/32        192.168.22.2                              Ethernet1/3.22      
        *100.2.2.4/32        192.168.22.2                              Ethernet1/3.22      
        *100.2.2.5/32        192.168.22.2                              Ethernet1/3.22      
        *100.2.2.6/32        192.168.22.2                              Ethernet1/3.22      
        *100.2.2.7/32        192.168.22.2                              Ethernet1/3.22      
        *100.2.2.8/32        192.168.22.2                              Ethernet1/3.22      
        *100.2.2.9/32        192.168.22.2                              Ethernet1/3.22      
        *100.2.2.10/32       192.168.22.2                              Ethernet1/3.22      
        100.2.3.1/32         3.3.3.2            nve1        vni:   501002    
        100.2.3.2/32         3.3.3.2            nve1        vni:   501002    
        100.2.3.3/32         3.3.3.2            nve1        vni:   501002    
        100.2.3.4/32         3.3.3.2            nve1        vni:   501002    
        100.2.3.5/32         3.3.3.2            nve1        vni:   501002    
        100.2.3.6/32         3.3.3.2            nve1        vni:   501002    
        100.2.3.7/32         3.3.3.2            nve1        vni:   501002    
        100.2.3.8/32         3.3.3.2            nve1        vni:   501002    
        100.2.3.9/32         3.3.3.2            nve1        vni:   501002    
        100.2.3.10/32        3.3.3.2            nve1        vni:   501002    
        100.2.4.1/32         4.4.4.2            nve1        vni:   501002    
        100.2.4.2/32         4.4.4.2            nve1        vni:   501002    
        100.2.4.3/32         4.4.4.2            nve1        vni:   501002    
        100.2.4.4/32         4.4.4.2            nve1        vni:   501002    
        100.2.4.5/32         4.4.4.2            nve1        vni:   501002    
        100.2.4.6/32         4.4.4.2            nve1        vni:   501002    
        100.2.4.7/32         4.4.4.2            nve1        vni:   501002    
        100.2.4.8/32         4.4.4.2            nve1        vni:   501002    
        100.2.4.9/32         4.4.4.2            nve1        vni:   501002    
        100.2.4.10/32        4.4.4.2            nve1        vni:   501002    
        192.168.22.0/24      Attached                                  Ethernet1/3.22
        192.168.22.0/32      Drop                                      Null0
        192.168.22.1/32      Receive                                   sup-eth1
        192.168.22.2/32      192.168.22.2                              Ethernet1/3.22      
        192.168.22.255/32    Attached                                  Ethernet1/3.22
        IPv4 routes for table VRF_Flow1_3/base
        
        ------------------+-----------------------------------------+----------------------+-----------------+-----------------
        Prefix            | Next-hop                                | Interface            | Labels          | Partial Install 
        ------------------+-----------------------------------------+----------------------+-----------------+-----------------
        0.0.0.0/32           Drop                                      Null0
        127.0.0.0/8          Drop                                      Null0
        255.255.255.255/32   Receive                                   sup-eth1
        100.3.1.1/32         1.1.1.2            nve1        vni:   501003    
        100.3.1.2/32         1.1.1.2            nve1        vni:   501003    
        100.3.1.3/32         1.1.1.2            nve1        vni:   501003    
        100.3.1.4/32         1.1.1.2            nve1        vni:   501003    
        100.3.1.5/32         1.1.1.2            nve1        vni:   501003    
        100.3.1.6/32         1.1.1.2            nve1        vni:   501003    
        100.3.1.7/32         1.1.1.2            nve1        vni:   501003    
        100.3.1.8/32         1.1.1.2            nve1        vni:   501003    
        100.3.1.9/32         1.1.1.2            nve1        vni:   501003    
        100.3.1.10/32        1.1.1.2            nve1        vni:   501003    
        *100.3.2.1/32        192.168.23.2                              Ethernet1/3.23      
        *100.3.2.2/32        192.168.23.2                              Ethernet1/3.23      
        *100.3.2.3/32        192.168.23.2                              Ethernet1/3.23      
        *100.3.2.4/32        192.168.23.2                              Ethernet1/3.23      
        *100.3.2.5/32        192.168.23.2                              Ethernet1/3.23      
        *100.3.2.6/32        192.168.23.2                              Ethernet1/3.23      
        *100.3.2.7/32        192.168.23.2                              Ethernet1/3.23      
        *100.3.2.8/32        192.168.23.2                              Ethernet1/3.23      
        *100.3.2.9/32        192.168.23.2                              Ethernet1/3.23      
        *100.3.2.10/32       192.168.23.2                              Ethernet1/3.23      
        100.3.3.1/32         3.3.3.2            nve1        vni:   501003    
        100.3.3.2/32         3.3.3.2            nve1        vni:   501003    
        100.3.3.3/32         3.3.3.2            nve1        vni:   501003    
        100.3.3.4/32         3.3.3.2            nve1        vni:   501003    
        100.3.3.5/32         3.3.3.2            nve1        vni:   501003    
        100.3.3.6/32         3.3.3.2            nve1        vni:   501003    
        100.3.3.7/32         3.3.3.2            nve1        vni:   501003    
        100.3.3.8/32         3.3.3.2            nve1        vni:   501003    
        100.3.3.9/32         3.3.3.2            nve1        vni:   501003    
        100.3.3.10/32        3.3.3.2            nve1        vni:   501003    
        100.3.4.1/32         4.4.4.2            nve1        vni:   501003    
        100.3.4.2/32         4.4.4.2            nve1        vni:   501003    
        100.3.4.3/32         4.4.4.2            nve1        vni:   501003    
        100.3.4.4/32         4.4.4.2            nve1        vni:   501003    
        100.3.4.5/32         4.4.4.2            nve1        vni:   501003    
        100.3.4.6/32         4.4.4.2            nve1        vni:   501003    
        100.3.4.7/32         4.4.4.2            nve1        vni:   501003    
        100.3.4.8/32         4.4.4.2            nve1        vni:   501003    
        100.3.4.9/32         4.4.4.2            nve1        vni:   501003    
        100.3.4.10/32        4.4.4.2            nve1        vni:   501003    
        192.168.23.0/24      Attached                                  Ethernet1/3.23
        192.168.23.0/32      Drop                                      Null0
        192.168.23.1/32      Receive                                   sup-eth1
        192.168.23.2/32      192.168.23.2                              Ethernet1/3.23      
        192.168.23.255/32    Attached                                  Ethernet1/3.23
        IPv4 routes for table VRF_Flow1_4/base
        
        ------------------+-----------------------------------------+----------------------+-----------------+-----------------
        Prefix            | Next-hop                                | Interface            | Labels          | Partial Install 
        ------------------+-----------------------------------------+----------------------+-----------------+-----------------
        0.0.0.0/32           Drop                                      Null0
        100.4.1.1/32         1.1.1.2            nve1        vni:   501004    
        100.4.1.2/32         1.1.1.2            nve1        vni:   501004    
        100.4.1.3/32         1.1.1.2            nve1        vni:   501004    
        100.4.1.4/32         1.1.1.2            nve1        vni:   501004    
        100.4.1.5/32         1.1.1.2            nve1        vni:   501004    
        100.4.1.6/32         1.1.1.2            nve1        vni:   501004    
        100.4.1.7/32         1.1.1.2            nve1        vni:   501004    
        100.4.1.8/32         1.1.1.2            nve1        vni:   501004    
        100.4.1.9/32         1.1.1.2            nve1        vni:   501004    
        100.4.1.10/32        1.1.1.2            nve1        vni:   501004    
        *100.4.2.1/32        192.168.24.2                              Ethernet1/3.24      
        *100.4.2.2/32        192.168.24.2                              Ethernet1/3.24      
        *100.4.2.3/32        192.168.24.2                              Ethernet1/3.24      
        *100.4.2.4/32        192.168.24.2                              Ethernet1/3.24      
        *100.4.2.5/32        192.168.24.2                              Ethernet1/3.24      
        *100.4.2.6/32        192.168.24.2                              Ethernet1/3.24      
        *100.4.2.7/32        192.168.24.2                              Ethernet1/3.24      
        *100.4.2.8/32        192.168.24.2                              Ethernet1/3.24      
        *100.4.2.9/32        192.168.24.2                              Ethernet1/3.24      
        *100.4.2.10/32       192.168.24.2                              Ethernet1/3.24      
        100.4.3.1/32         3.3.3.2            nve1        vni:   501004    
        100.4.3.2/32         3.3.3.2            nve1        vni:   501004    
        100.4.3.3/32         3.3.3.2            nve1        vni:   501004    
        100.4.3.4/32         3.3.3.2            nve1        vni:   501004    
        100.4.3.5/32         3.3.3.2            nve1        vni:   501004    
        100.4.3.6/32         3.3.3.2            nve1        vni:   501004    
        100.4.3.7/32         3.3.3.2            nve1        vni:   501004    
        100.4.3.8/32         3.3.3.2            nve1        vni:   501004    
        100.4.3.9/32         3.3.3.2            nve1        vni:   501004    
        100.4.3.10/32        3.3.3.2            nve1        vni:   501004    
        100.4.4.1/32         4.4.4.2            nve1        vni:   501004    
        100.4.4.2/32         4.4.4.2            nve1        vni:   501004    
        100.4.4.3/32         4.4.4.2            nve1        vni:   501004    
        100.4.4.4/32         4.4.4.2            nve1        vni:   501004    
        100.4.4.5/32         4.4.4.2            nve1        vni:   501004    
        100.4.4.6/32         4.4.4.2            nve1        vni:   501004    
        100.4.4.7/32         4.4.4.2            nve1        vni:   501004    
        100.4.4.8/32         4.4.4.2            nve1        vni:   501004    
        100.4.4.9/32         4.4.4.2            nve1        vni:   501004    
        100.4.4.10/32        4.4.4.2            nve1        vni:   501004    
        192.168.24.0/24      Attached                                  Ethernet1/3.24
        192.168.24.0/32      Drop                                      Null0
        192.168.24.1/32      Receive                                   sup-eth1
        192.168.24.2/32      192.168.24.2                              Ethernet1/3.24      
        192.168.24.255/32    Attached                                  Ethernet1/3.24
        IPv4 routes for table 0xfffe
        
        ------------------+-----------------------------------------+----------------------+-----------------+-----------------
        Prefix            | Next-hop                                | Interface            | Labels          | Partial Install 
        ------------------+-----------------------------------------+----------------------+-----------------+-----------------
        0.0.0.0/32           Drop                                      Null0
        127.0.0.0/8          Drop                                      Null0
        255.255.255.255/32   Receive                                   sup-eth1 
        '''}


    def test_show_forwarding_ipv4_vrf_all_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowForwardingIpv4(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_show_forwarding_ipv4_vrf_all_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowForwardingIpv4(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()
        
if __name__ == '__main__':
    unittest.main()
