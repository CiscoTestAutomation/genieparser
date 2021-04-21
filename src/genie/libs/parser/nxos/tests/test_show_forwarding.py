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
        'slot': {'1': {'ip_version': {'IPv4': {'route_table': {'default/base': {'prefix': {'10.4.1.1/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                     'is_best': False}}},
                                                                                            '10.4.1.2/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                     'is_best': True}}},
                                                                                            '10.2.1.0/32': {'next_hop': {'Drop': {'interface': 'Null0',
                                                                                                                                  'is_best': False}}},
                                                                                            '10.2.1.1/32': {'next_hop': {'Receive': {'interface': 'sup-eth1',
                                                                                                                                     'is_best': False}}},
                                                                                            '10.2.1.2/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                      'is_best': False}}},
                                                                                            '10.2.1.255/32': {'next_hop': {'Attached': {'interface': 'Ethernet1/1',
                                                                                                                                        'is_best': False}}},
                                                                                            '10.16.2.1/32': {'next_hop': {'Receive': {'interface': 'sup-eth1',
                                                                                                                                    'is_best': False}}},
                                                                                            '10.16.2.2/32': {'next_hop': {'Receive': {'interface': 'sup-eth1',
                                                                                                                                    'is_best': False}}},
                                                                                            '10.229.1.0/32': {'next_hop': {'Drop': {'interface': 'Null0',
                                                                                                                                  'is_best': False}}},
                                                                                            '10.229.1.1/32': {'next_hop': {'Receive': {'interface': 'sup-eth1',
                                                                                                                                     'is_best': False}}},
                                                                                            '10.229.1.2/32': {'next_hop': {'10.229.1.2': {'interface': 'Ethernet1/2',
                                                                                                                                      'is_best': False}}},
                                                                                            '10.229.1.255/32': {'next_hop': {'Attached': {'interface': 'Ethernet1/2',
                                                                                                                                        'is_best': False}}},
                                                                                            '192.168.195.1/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                           'is_best': False}}},
                                                                                            '10.36.3.1/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                     'is_best': False}}},
                                                                                            '10.36.3.2/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                     'is_best': True}}},
                                                                                            '10.64.4.1/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                     'is_best': False}}},
                                                                                            '10.64.4.2/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                     'is_best': True}}},
                                                                                            '10.166.98.98/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                         'is_best': False}}},
                                                                                            '10.189.99.99/32': {'next_hop': {'10.229.1.2': {'interface': 'Ethernet1/2',
                                                                                                                                         'is_best': False}}}}}}}}},
                  '27': {'ip_version': {'IPv4': {'route_table': {'default/base': {'prefix': {'0.0.0.0/32': {'next_hop': {'Drop': {'interface': 'Null0',
                                                                                                                                  'is_best': False}}},
                                                                                             '10.4.1.1/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                      'is_best': False},
                                                                                                                         '10.229.1.2': {'interface': 'Ethernet1/2',
                                                                                                                                      'is_best': False}}},
                                                                                             '10.4.1.2/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                      'is_best': True},
                                                                                                                         '10.229.1.2': {'interface': 'Ethernet1/2',
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
                                                                                             '10.69.111.0/24': {'next_hop': {'Drop': {'interface': 'Null0',
                                                                                                                                        'is_best': False}}},
                                                                                             '127.0.0.0/8': {'next_hop': {'Drop': {'interface': 'Null0',
                                                                                                                                   'is_best': False}}},
                                                                                             '10.16.2.1/32': {'next_hop': {'Receive': {'interface': 'sup-eth1',
                                                                                                                                     'is_best': False}}},
                                                                                             '10.16.2.2/32': {'next_hop': {'Receive': {'interface': 'sup-eth1',
                                                                                                                                     'is_best': False}}},
                                                                                             '10.186.1.0/24': {'next_hop': {'10.229.1.2': {'interface': 'Ethernet1/2',
                                                                                                                                       'is_best': False}}},
                                                                                             '10.229.1.0/24': {'next_hop': {'Attached': {'interface': 'Ethernet1/2',
                                                                                                                                       'is_best': False}}},
                                                                                             '10.229.1.0/32': {'next_hop': {'Drop': {'interface': 'Null0',
                                                                                                                                   'is_best': False}}},
                                                                                             '10.229.1.1/32': {'next_hop': {'Receive': {'interface': 'sup-eth1',
                                                                                                                                      'is_best': False}}},
                                                                                             '10.229.1.2/32': {'next_hop': {'10.229.1.2': {'interface': 'Ethernet1/2',
                                                                                                                                       'is_best': False}}},
                                                                                             '10.229.1.255/32': {'next_hop': {'Attached': {'interface': 'Ethernet1/2',
                                                                                                                                         'is_best': False}}},
                                                                                             '10.19.1.0/24': {'next_hop': {'10.229.1.2': {'interface': 'Ethernet1/2',
                                                                                                                                       'is_best': False}}},
                                                                                             '10.66.1.0/24': {'next_hop': {'10.229.1.2': {'interface': 'Ethernet1/2',
                                                                                                                                       'is_best': False}}},
                                                                                             '192.168.195.1/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                            'is_best': False}}},
                                                                                             '10.205.0.0/16': {'next_hop': {'Drop': {'interface': 'Null0',
                                                                                                                                    'is_best': False}}},
                                                                                             '10.205.25.0/24': {'next_hop': {'Drop': {'interface': 'Null0',
                                                                                                                                     'is_best': False}}},
                                                                                             '255.255.255.255/32': {'next_hop': {'Receive': {'interface': 'sup-eth1',
                                                                                                                                             'is_best': False}}},
                                                                                             '10.36.3.1/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                      'is_best': False},
                                                                                                                         '10.229.1.2': {'interface': 'Ethernet1/2',
                                                                                                                                      'is_best': False}}},
                                                                                             '10.36.3.2/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                      'is_best': True},
                                                                                                                         '10.229.1.2': {'interface': 'Ethernet1/2',
                                                                                                                                      'is_best': False}}},
                                                                                             '10.64.4.1/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                      'is_best': False},
                                                                                                                         '10.229.1.2': {'interface': 'Ethernet1/2',
                                                                                                                                      'is_best': False}}},
                                                                                             '10.64.4.2/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                      'is_best': True},
                                                                                                                         '10.229.1.2': {'interface': 'Ethernet1/2',
                                                                                                                                      'is_best': False}}},
                                                                                             '10.166.98.98/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                          'is_best': False}}},
                                                                                             '10.189.99.99/32': {'next_hop': {'10.229.1.2': {'interface': 'Ethernet1/2',
                                                                                                                                          'is_best': False}}}}}}}}}}}

    golden_output = {'execute.return_value': '''
        #vtep1 show forwarding ipv4
        slot  1
        =======
        
        
        IPv4 routes for table default/base
        
        ------------------+-----------------------------------------+----------------------+-----------------+-----------------
        Prefix            | Next-hop                                | Interface            | Labels          | Partial Install 
        ------------------+-----------------------------------------+----------------------+-----------------+-----------------
        10.4.1.1/32           10.2.1.2                                  Ethernet1/1         
        *10.4.1.2/32          10.2.1.2                                  Ethernet1/1         
        10.16.2.1/32           Receive                                   sup-eth1
        10.16.2.2/32           Receive                                   sup-eth1
        10.36.3.1/32           10.2.1.2                                  Ethernet1/1         
        *10.36.3.2/32          10.2.1.2                                  Ethernet1/1         
        10.64.4.1/32           10.2.1.2                                  Ethernet1/1         
        *10.64.4.2/32          10.2.1.2                                  Ethernet1/1         
        10.2.1.0/32          Drop                                      Null0
        10.2.1.1/32          Receive                                   sup-eth1
        10.2.1.2/32          10.2.1.2                                  Ethernet1/1         
        10.2.1.255/32        Attached                                  Ethernet1/1
        10.229.1.0/32          Drop                                      Null0
        10.229.1.1/32          Receive                                   sup-eth1
        10.229.1.2/32          10.229.1.2                                  Ethernet1/2         
        10.229.1.255/32        Attached                                  Ethernet1/2
        10.166.98.98/32       10.2.1.2                                  Ethernet1/1         
        10.189.99.99/32       10.229.1.2                                  Ethernet1/2         
        192.168.195.1/32     10.2.1.2                                  Ethernet1/1         
        
        slot 27
        =======
        
        
        IPv4 routes for table default/base
        
        ------------------+-----------------------------------------+----------------------+-----------------+-----------------
        Prefix            | Next-hop                                | Interface            | Labels          | Partial Install 
        ------------------+-----------------------------------------+----------------------+-----------------+-----------------
        0.0.0.0/32           Drop                                      Null0
        127.0.0.0/8          Drop                                      Null0
        255.255.255.255/32   Receive                                   sup-eth1
        10.4.1.1/32           10.2.1.2                                  Ethernet1/1         
                             10.229.1.2                                  Ethernet1/2         
        *10.4.1.2/32          10.2.1.2                                  Ethernet1/1         
                             10.229.1.2                                  Ethernet1/2         
        10.16.2.1/32           Receive                                   sup-eth1
        10.16.2.2/32           Receive                                   sup-eth1
        10.36.3.1/32           10.2.1.2                                  Ethernet1/1         
                             10.229.1.2                                  Ethernet1/2         
        *10.36.3.2/32          10.2.1.2                                  Ethernet1/1         
                             10.229.1.2                                  Ethernet1/2         
        10.64.4.1/32           10.2.1.2                                  Ethernet1/1         
                             10.229.1.2                                  Ethernet1/2         
        *10.64.4.2/32          10.2.1.2                                  Ethernet1/1         
                             10.229.1.2                                  Ethernet1/2         
        10.1.1.0/24          10.2.1.2                                  Ethernet1/1         
        10.2.1.0/24          Attached                                  Ethernet1/1
        10.2.1.0/32          Drop                                      Null0
        10.2.1.1/32          Receive                                   sup-eth1
        10.2.1.2/32          10.2.1.2                                  Ethernet1/1         
        10.2.1.255/32        Attached                                  Ethernet1/1
        10.3.1.0/24          10.2.1.2                                  Ethernet1/1         
        10.4.1.0/24          10.2.1.2                                  Ethernet1/1         
        10.186.1.0/24          10.229.1.2                                  Ethernet1/2         
        10.229.1.0/24          Attached                                  Ethernet1/2
        10.229.1.0/32          Drop                                      Null0
        10.229.1.1/32          Receive                                   sup-eth1
        10.229.1.2/32          10.229.1.2                                  Ethernet1/2         
        10.229.1.255/32        Attached                                  Ethernet1/2
        10.19.1.0/24          10.229.1.2                                  Ethernet1/2         
        10.66.1.0/24          10.229.1.2                                  Ethernet1/2         
        10.205.0.0/16         Drop                                      Null0
        10.205.25.0/24        Drop                                      Null0
        10.166.98.98/32       10.2.1.2                                  Ethernet1/1         
        10.189.99.99/32       10.229.1.2                                  Ethernet1/2         
        10.69.111.0/24     Drop                                      Null0
        192.168.195.1/32     10.2.1.2                                  Ethernet1/1         
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
                                                                'VRF_Flow1_1/base': {'prefix': {'10.1.1.1/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501001'}}},
                                                                                                '10.1.1.10/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501001'}}},
                                                                                                '10.1.1.2/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501001'}}},
                                                                                                '10.1.1.3/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501001'}}},
                                                                                                '10.1.1.4/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501001'}}},
                                                                                                '10.1.1.5/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501001'}}},
                                                                                                '10.1.1.6/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501001'}}},
                                                                                                '10.1.1.7/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501001'}}},
                                                                                                '10.1.1.8/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501001'}}},
                                                                                                '10.1.1.9/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501001'}}},
                                                                                                '10.1.2.1/32': {'next_hop': {'192.168.21.2': {'interface': 'Ethernet1/3.21',
                                                                                                                                               'is_best': True}}},
                                                                                                '10.1.2.10/32': {'next_hop': {'192.168.21.2': {'interface': 'Ethernet1/3.21',
                                                                                                                                                'is_best': True}}},
                                                                                                '10.1.2.2/32': {'next_hop': {'192.168.21.2': {'interface': 'Ethernet1/3.21',
                                                                                                                                               'is_best': True}}},
                                                                                                '10.1.2.3/32': {'next_hop': {'192.168.21.2': {'interface': 'Ethernet1/3.21',
                                                                                                                                               'is_best': True}}},
                                                                                                '10.1.2.4/32': {'next_hop': {'192.168.21.2': {'interface': 'Ethernet1/3.21',
                                                                                                                                               'is_best': True}}},
                                                                                                '10.1.2.5/32': {'next_hop': {'192.168.21.2': {'interface': 'Ethernet1/3.21',
                                                                                                                                               'is_best': True}}},
                                                                                                '10.1.2.6/32': {'next_hop': {'192.168.21.2': {'interface': 'Ethernet1/3.21',
                                                                                                                                               'is_best': True}}},
                                                                                                '10.1.2.7/32': {'next_hop': {'192.168.21.2': {'interface': 'Ethernet1/3.21',
                                                                                                                                               'is_best': True}}},
                                                                                                '10.1.2.8/32': {'next_hop': {'192.168.21.2': {'interface': 'Ethernet1/3.21',
                                                                                                                                               'is_best': True}}},
                                                                                                '10.1.2.9/32': {'next_hop': {'192.168.21.2': {'interface': 'Ethernet1/3.21',
                                                                                                                                               'is_best': True}}},
                                                                                                '10.1.3.1/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501001'}}},
                                                                                                '10.1.3.10/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501001'}}},
                                                                                                '10.1.3.2/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501001'}}},
                                                                                                '10.1.3.3/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501001'}}},
                                                                                                '10.1.3.4/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501001'}}},
                                                                                                '10.1.3.5/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501001'}}},
                                                                                                '10.1.3.6/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501001'}}},
                                                                                                '10.1.3.7/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501001'}}},
                                                                                                '10.1.3.8/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501001'}}},
                                                                                                '10.1.3.9/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501001'}}},
                                                                                                '10.1.4.1/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501001'}}},
                                                                                                '10.1.4.10/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501001'}}},
                                                                                                '10.1.4.2/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501001'}}},
                                                                                                '10.1.4.3/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501001'}}},
                                                                                                '10.1.4.4/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501001'}}},
                                                                                                '10.1.4.5/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501001'}}},
                                                                                                '10.1.4.6/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501001'}}},
                                                                                                '10.1.4.7/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501001'}}},
                                                                                                '10.1.4.8/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501001'}}},
                                                                                                '10.1.4.9/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
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
                                                                'VRF_Flow1_2/base': {'prefix': {'10.204.1.1/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501002'}}},
                                                                                                '10.204.1.10/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501002'}}},
                                                                                                '10.204.1.2/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501002'}}},
                                                                                                '10.204.1.3/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501002'}}},
                                                                                                '10.204.1.4/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501002'}}},
                                                                                                '10.204.1.5/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501002'}}},
                                                                                                '10.204.1.6/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501002'}}},
                                                                                                '10.204.1.7/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501002'}}},
                                                                                                '10.204.1.8/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501002'}}},
                                                                                                '10.204.1.9/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501002'}}},
                                                                                                '10.204.2.1/32': {'next_hop': {'192.168.22.2': {'interface': 'Ethernet1/3.22',
                                                                                                                                               'is_best': True}}},
                                                                                                '10.204.2.10/32': {'next_hop': {'192.168.22.2': {'interface': 'Ethernet1/3.22',
                                                                                                                                                'is_best': True}}},
                                                                                                '10.204.2.2/32': {'next_hop': {'192.168.22.2': {'interface': 'Ethernet1/3.22',
                                                                                                                                               'is_best': True}}},
                                                                                                '10.204.2.3/32': {'next_hop': {'192.168.22.2': {'interface': 'Ethernet1/3.22',
                                                                                                                                               'is_best': True}}},
                                                                                                '10.204.2.4/32': {'next_hop': {'192.168.22.2': {'interface': 'Ethernet1/3.22',
                                                                                                                                               'is_best': True}}},
                                                                                                '10.204.2.5/32': {'next_hop': {'192.168.22.2': {'interface': 'Ethernet1/3.22',
                                                                                                                                               'is_best': True}}},
                                                                                                '10.204.2.6/32': {'next_hop': {'192.168.22.2': {'interface': 'Ethernet1/3.22',
                                                                                                                                               'is_best': True}}},
                                                                                                '10.204.2.7/32': {'next_hop': {'192.168.22.2': {'interface': 'Ethernet1/3.22',
                                                                                                                                               'is_best': True}}},
                                                                                                '10.204.2.8/32': {'next_hop': {'192.168.22.2': {'interface': 'Ethernet1/3.22',
                                                                                                                                               'is_best': True}}},
                                                                                                '10.204.2.9/32': {'next_hop': {'192.168.22.2': {'interface': 'Ethernet1/3.22',
                                                                                                                                               'is_best': True}}},
                                                                                                '10.204.3.1/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501002'}}},
                                                                                                '10.204.3.10/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501002'}}},
                                                                                                '10.204.3.2/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501002'}}},
                                                                                                '10.204.3.3/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501002'}}},
                                                                                                '10.204.3.4/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501002'}}},
                                                                                                '10.204.3.5/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501002'}}},
                                                                                                '10.204.3.6/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501002'}}},
                                                                                                '10.204.3.7/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501002'}}},
                                                                                                '10.204.3.8/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501002'}}},
                                                                                                '10.204.3.9/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501002'}}},
                                                                                                '10.204.4.1/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501002'}}},
                                                                                                '10.204.4.10/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501002'}}},
                                                                                                '10.204.4.2/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501002'}}},
                                                                                                '10.204.4.3/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501002'}}},
                                                                                                '10.204.4.4/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501002'}}},
                                                                                                '10.204.4.5/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501002'}}},
                                                                                                '10.204.4.6/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501002'}}},
                                                                                                '10.204.4.7/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501002'}}},
                                                                                                '10.204.4.8/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501002'}}},
                                                                                                '10.204.4.9/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
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
                                                                'VRF_Flow1_3/base': {'prefix': {'10.154.1.1/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501003'}}},
                                                                                                '10.154.1.10/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501003'}}},
                                                                                                '10.154.1.2/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501003'}}},
                                                                                                '10.154.1.3/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501003'}}},
                                                                                                '10.154.1.4/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501003'}}},
                                                                                                '10.154.1.5/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501003'}}},
                                                                                                '10.154.1.6/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501003'}}},
                                                                                                '10.154.1.7/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501003'}}},
                                                                                                '10.154.1.8/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501003'}}},
                                                                                                '10.154.1.9/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501003'}}},
                                                                                                '10.154.2.1/32': {'next_hop': {'192.168.23.2': {'interface': 'Ethernet1/3.23',
                                                                                                                                               'is_best': True}}},
                                                                                                '10.154.2.10/32': {'next_hop': {'192.168.23.2': {'interface': 'Ethernet1/3.23',
                                                                                                                                                'is_best': True}}},
                                                                                                '10.154.2.2/32': {'next_hop': {'192.168.23.2': {'interface': 'Ethernet1/3.23',
                                                                                                                                               'is_best': True}}},
                                                                                                '10.154.2.3/32': {'next_hop': {'192.168.23.2': {'interface': 'Ethernet1/3.23',
                                                                                                                                               'is_best': True}}},
                                                                                                '10.154.2.4/32': {'next_hop': {'192.168.23.2': {'interface': 'Ethernet1/3.23',
                                                                                                                                               'is_best': True}}},
                                                                                                '10.154.2.5/32': {'next_hop': {'192.168.23.2': {'interface': 'Ethernet1/3.23',
                                                                                                                                               'is_best': True}}},
                                                                                                '10.154.2.6/32': {'next_hop': {'192.168.23.2': {'interface': 'Ethernet1/3.23',
                                                                                                                                               'is_best': True}}},
                                                                                                '10.154.2.7/32': {'next_hop': {'192.168.23.2': {'interface': 'Ethernet1/3.23',
                                                                                                                                               'is_best': True}}},
                                                                                                '10.154.2.8/32': {'next_hop': {'192.168.23.2': {'interface': 'Ethernet1/3.23',
                                                                                                                                               'is_best': True}}},
                                                                                                '10.154.2.9/32': {'next_hop': {'192.168.23.2': {'interface': 'Ethernet1/3.23',
                                                                                                                                               'is_best': True}}},
                                                                                                '10.154.3.1/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501003'}}},
                                                                                                '10.154.3.10/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501003'}}},
                                                                                                '10.154.3.2/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501003'}}},
                                                                                                '10.154.3.3/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501003'}}},
                                                                                                '10.154.3.4/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501003'}}},
                                                                                                '10.154.3.5/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501003'}}},
                                                                                                '10.154.3.6/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501003'}}},
                                                                                                '10.154.3.7/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501003'}}},
                                                                                                '10.154.3.8/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501003'}}},
                                                                                                '10.154.3.9/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501003'}}},
                                                                                                '10.154.4.1/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501003'}}},
                                                                                                '10.154.4.10/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501003'}}},
                                                                                                '10.154.4.2/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501003'}}},
                                                                                                '10.154.4.3/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501003'}}},
                                                                                                '10.154.4.4/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501003'}}},
                                                                                                '10.154.4.5/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501003'}}},
                                                                                                '10.154.4.6/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501003'}}},
                                                                                                '10.154.4.7/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501003'}}},
                                                                                                '10.154.4.8/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501003'}}},
                                                                                                '10.154.4.9/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
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
                                                                'VRF_Flow1_4/base': {'prefix': {'10.106.1.1/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501004'}}},
                                                                                                '10.106.1.10/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501004'}}},
                                                                                                '10.106.1.2/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501004'}}},
                                                                                                '10.106.1.3/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501004'}}},
                                                                                                '10.106.1.4/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501004'}}},
                                                                                                '10.106.1.5/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501004'}}},
                                                                                                '10.106.1.6/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501004'}}},
                                                                                                '10.106.1.7/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501004'}}},
                                                                                                '10.106.1.8/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501004'}}},
                                                                                                '10.106.1.9/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501004'}}},
                                                                                                '10.106.2.1/32': {'next_hop': {'192.168.24.2': {'interface': 'Ethernet1/3.24',
                                                                                                                                               'is_best': True}}},
                                                                                                '10.106.2.10/32': {'next_hop': {'192.168.24.2': {'interface': 'Ethernet1/3.24',
                                                                                                                                                'is_best': True}}},
                                                                                                '10.106.2.2/32': {'next_hop': {'192.168.24.2': {'interface': 'Ethernet1/3.24',
                                                                                                                                               'is_best': True}}},
                                                                                                '10.106.2.3/32': {'next_hop': {'192.168.24.2': {'interface': 'Ethernet1/3.24',
                                                                                                                                               'is_best': True}}},
                                                                                                '10.106.2.4/32': {'next_hop': {'192.168.24.2': {'interface': 'Ethernet1/3.24',
                                                                                                                                               'is_best': True}}},
                                                                                                '10.106.2.5/32': {'next_hop': {'192.168.24.2': {'interface': 'Ethernet1/3.24',
                                                                                                                                               'is_best': True}}},
                                                                                                '10.106.2.6/32': {'next_hop': {'192.168.24.2': {'interface': 'Ethernet1/3.24',
                                                                                                                                               'is_best': True}}},
                                                                                                '10.106.2.7/32': {'next_hop': {'192.168.24.2': {'interface': 'Ethernet1/3.24',
                                                                                                                                               'is_best': True}}},
                                                                                                '10.106.2.8/32': {'next_hop': {'192.168.24.2': {'interface': 'Ethernet1/3.24',
                                                                                                                                               'is_best': True}}},
                                                                                                '10.106.2.9/32': {'next_hop': {'192.168.24.2': {'interface': 'Ethernet1/3.24',
                                                                                                                                               'is_best': True}}},
                                                                                                '10.106.3.1/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501004'}}},
                                                                                                '10.106.3.10/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501004'}}},
                                                                                                '10.106.3.2/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501004'}}},
                                                                                                '10.106.3.3/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501004'}}},
                                                                                                '10.106.3.4/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501004'}}},
                                                                                                '10.106.3.5/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501004'}}},
                                                                                                '10.106.3.6/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501004'}}},
                                                                                                '10.106.3.7/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501004'}}},
                                                                                                '10.106.3.8/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501004'}}},
                                                                                                '10.106.3.9/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501004'}}},
                                                                                                '10.106.4.1/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501004'}}},
                                                                                                '10.106.4.10/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501004'}}},
                                                                                                '10.106.4.2/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501004'}}},
                                                                                                '10.106.4.3/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501004'}}},
                                                                                                '10.106.4.4/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501004'}}},
                                                                                                '10.106.4.5/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501004'}}},
                                                                                                '10.106.4.6/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501004'}}},
                                                                                                '10.106.4.7/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501004'}}},
                                                                                                '10.106.4.8/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                          'is_best': False,
                                                                                                                                          'label': 'vni:   501004'}}},
                                                                                                '10.106.4.9/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
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
                                                                'default/base': {'prefix': {'10.4.1.1/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                     'is_best': False}}},
                                                                                            '10.4.1.2/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                     'is_best': True}}},
                                                                                            '10.2.1.0/32': {'next_hop': {'Drop': {'interface': 'Null0',
                                                                                                                                  'is_best': False}}},
                                                                                            '10.2.1.1/32': {'next_hop': {'Receive': {'interface': 'sup-eth1',
                                                                                                                                     'is_best': False}}},
                                                                                            '10.2.1.2/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                      'is_best': False}}},
                                                                                            '10.2.1.255/32': {'next_hop': {'Attached': {'interface': 'Ethernet1/1',
                                                                                                                                        'is_best': False}}},
                                                                                            '10.16.2.1/32': {'next_hop': {'Receive': {'interface': 'sup-eth1',
                                                                                                                                    'is_best': False}}},
                                                                                            '10.16.2.2/32': {'next_hop': {'Receive': {'interface': 'sup-eth1',
                                                                                                                                    'is_best': False}}},
                                                                                            '10.229.1.0/32': {'next_hop': {'Drop': {'interface': 'Null0',
                                                                                                                                  'is_best': False}}},
                                                                                            '10.229.1.1/32': {'next_hop': {'Receive': {'interface': 'sup-eth1',
                                                                                                                                     'is_best': False}}},
                                                                                            '10.229.1.2/32': {'next_hop': {'10.229.1.2': {'interface': 'Ethernet1/2',
                                                                                                                                      'is_best': False}}},
                                                                                            '10.229.1.255/32': {'next_hop': {'Attached': {'interface': 'Ethernet1/2',
                                                                                                                                        'is_best': False}}},
                                                                                            '192.168.195.1/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                           'is_best': False}}},
                                                                                            '10.36.3.1/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                     'is_best': False}}},
                                                                                            '10.36.3.2/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                     'is_best': True}}},
                                                                                            '10.64.4.1/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                     'is_best': False}}},
                                                                                            '10.64.4.2/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                     'is_best': True}}},
                                                                                            '10.166.98.98/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                         'is_best': False}}},
                                                                                            '10.189.99.99/32': {'next_hop': {'10.229.1.2': {'interface': 'Ethernet1/2',
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
                                                                                                 '10.1.1.1/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501001'}}},
                                                                                                 '10.1.1.10/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                            'is_best': False,
                                                                                                                                            'label': 'vni:   501001'}}},
                                                                                                 '10.1.1.2/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501001'}}},
                                                                                                 '10.1.1.3/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501001'}}},
                                                                                                 '10.1.1.4/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501001'}}},
                                                                                                 '10.1.1.5/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501001'}}},
                                                                                                 '10.1.1.6/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501001'}}},
                                                                                                 '10.1.1.7/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501001'}}},
                                                                                                 '10.1.1.8/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501001'}}},
                                                                                                 '10.1.1.9/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501001'}}},
                                                                                                 '10.1.2.1/32': {'next_hop': {'192.168.21.2': {'interface': 'Ethernet1/3.21',
                                                                                                                                                'is_best': True}}},
                                                                                                 '10.1.2.10/32': {'next_hop': {'192.168.21.2': {'interface': 'Ethernet1/3.21',
                                                                                                                                                 'is_best': True}}},
                                                                                                 '10.1.2.2/32': {'next_hop': {'192.168.21.2': {'interface': 'Ethernet1/3.21',
                                                                                                                                                'is_best': True}}},
                                                                                                 '10.1.2.3/32': {'next_hop': {'192.168.21.2': {'interface': 'Ethernet1/3.21',
                                                                                                                                                'is_best': True}}},
                                                                                                 '10.1.2.4/32': {'next_hop': {'192.168.21.2': {'interface': 'Ethernet1/3.21',
                                                                                                                                                'is_best': True}}},
                                                                                                 '10.1.2.5/32': {'next_hop': {'192.168.21.2': {'interface': 'Ethernet1/3.21',
                                                                                                                                                'is_best': True}}},
                                                                                                 '10.1.2.6/32': {'next_hop': {'192.168.21.2': {'interface': 'Ethernet1/3.21',
                                                                                                                                                'is_best': True}}},
                                                                                                 '10.1.2.7/32': {'next_hop': {'192.168.21.2': {'interface': 'Ethernet1/3.21',
                                                                                                                                                'is_best': True}}},
                                                                                                 '10.1.2.8/32': {'next_hop': {'192.168.21.2': {'interface': 'Ethernet1/3.21',
                                                                                                                                                'is_best': True}}},
                                                                                                 '10.1.2.9/32': {'next_hop': {'192.168.21.2': {'interface': 'Ethernet1/3.21',
                                                                                                                                                'is_best': True}}},
                                                                                                 '10.1.3.1/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501001'}}},
                                                                                                 '10.1.3.10/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                            'is_best': False,
                                                                                                                                            'label': 'vni:   501001'}}},
                                                                                                 '10.1.3.2/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501001'}}},
                                                                                                 '10.1.3.3/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501001'}}},
                                                                                                 '10.1.3.4/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501001'}}},
                                                                                                 '10.1.3.5/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501001'}}},
                                                                                                 '10.1.3.6/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501001'}}},
                                                                                                 '10.1.3.7/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501001'}}},
                                                                                                 '10.1.3.8/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501001'}}},
                                                                                                 '10.1.3.9/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501001'}}},
                                                                                                 '10.1.4.1/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501001'}}},
                                                                                                 '10.1.4.10/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                            'is_best': False,
                                                                                                                                            'label': 'vni:   501001'}}},
                                                                                                 '10.1.4.2/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501001'}}},
                                                                                                 '10.1.4.3/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501001'}}},
                                                                                                 '10.1.4.4/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501001'}}},
                                                                                                 '10.1.4.5/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501001'}}},
                                                                                                 '10.1.4.6/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501001'}}},
                                                                                                 '10.1.4.7/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501001'}}},
                                                                                                 '10.1.4.8/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501001'}}},
                                                                                                 '10.1.4.9/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
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
                                                                                                 '10.204.1.1/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501002'}}},
                                                                                                 '10.204.1.10/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                            'is_best': False,
                                                                                                                                            'label': 'vni:   501002'}}},
                                                                                                 '10.204.1.2/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501002'}}},
                                                                                                 '10.204.1.3/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501002'}}},
                                                                                                 '10.204.1.4/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501002'}}},
                                                                                                 '10.204.1.5/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501002'}}},
                                                                                                 '10.204.1.6/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501002'}}},
                                                                                                 '10.204.1.7/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501002'}}},
                                                                                                 '10.204.1.8/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501002'}}},
                                                                                                 '10.204.1.9/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501002'}}},
                                                                                                 '10.204.2.1/32': {'next_hop': {'192.168.22.2': {'interface': 'Ethernet1/3.22',
                                                                                                                                                'is_best': True}}},
                                                                                                 '10.204.2.10/32': {'next_hop': {'192.168.22.2': {'interface': 'Ethernet1/3.22',
                                                                                                                                                 'is_best': True}}},
                                                                                                 '10.204.2.2/32': {'next_hop': {'192.168.22.2': {'interface': 'Ethernet1/3.22',
                                                                                                                                                'is_best': True}}},
                                                                                                 '10.204.2.3/32': {'next_hop': {'192.168.22.2': {'interface': 'Ethernet1/3.22',
                                                                                                                                                'is_best': True}}},
                                                                                                 '10.204.2.4/32': {'next_hop': {'192.168.22.2': {'interface': 'Ethernet1/3.22',
                                                                                                                                                'is_best': True}}},
                                                                                                 '10.204.2.5/32': {'next_hop': {'192.168.22.2': {'interface': 'Ethernet1/3.22',
                                                                                                                                                'is_best': True}}},
                                                                                                 '10.204.2.6/32': {'next_hop': {'192.168.22.2': {'interface': 'Ethernet1/3.22',
                                                                                                                                                'is_best': True}}},
                                                                                                 '10.204.2.7/32': {'next_hop': {'192.168.22.2': {'interface': 'Ethernet1/3.22',
                                                                                                                                                'is_best': True}}},
                                                                                                 '10.204.2.8/32': {'next_hop': {'192.168.22.2': {'interface': 'Ethernet1/3.22',
                                                                                                                                                'is_best': True}}},
                                                                                                 '10.204.2.9/32': {'next_hop': {'192.168.22.2': {'interface': 'Ethernet1/3.22',
                                                                                                                                                'is_best': True}}},
                                                                                                 '10.204.3.1/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501002'}}},
                                                                                                 '10.204.3.10/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                            'is_best': False,
                                                                                                                                            'label': 'vni:   501002'}}},
                                                                                                 '10.204.3.2/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501002'}}},
                                                                                                 '10.204.3.3/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501002'}}},
                                                                                                 '10.204.3.4/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501002'}}},
                                                                                                 '10.204.3.5/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501002'}}},
                                                                                                 '10.204.3.6/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501002'}}},
                                                                                                 '10.204.3.7/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501002'}}},
                                                                                                 '10.204.3.8/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501002'}}},
                                                                                                 '10.204.3.9/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501002'}}},
                                                                                                 '10.204.4.1/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501002'}}},
                                                                                                 '10.204.4.10/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                            'is_best': False,
                                                                                                                                            'label': 'vni:   501002'}}},
                                                                                                 '10.204.4.2/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501002'}}},
                                                                                                 '10.204.4.3/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501002'}}},
                                                                                                 '10.204.4.4/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501002'}}},
                                                                                                 '10.204.4.5/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501002'}}},
                                                                                                 '10.204.4.6/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501002'}}},
                                                                                                 '10.204.4.7/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501002'}}},
                                                                                                 '10.204.4.8/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501002'}}},
                                                                                                 '10.204.4.9/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
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
                                                                                                 '10.154.1.1/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501003'}}},
                                                                                                 '10.154.1.10/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                            'is_best': False,
                                                                                                                                            'label': 'vni:   501003'}}},
                                                                                                 '10.154.1.2/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501003'}}},
                                                                                                 '10.154.1.3/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501003'}}},
                                                                                                 '10.154.1.4/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501003'}}},
                                                                                                 '10.154.1.5/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501003'}}},
                                                                                                 '10.154.1.6/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501003'}}},
                                                                                                 '10.154.1.7/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501003'}}},
                                                                                                 '10.154.1.8/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501003'}}},
                                                                                                 '10.154.1.9/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501003'}}},
                                                                                                 '10.154.2.1/32': {'next_hop': {'192.168.23.2': {'interface': 'Ethernet1/3.23',
                                                                                                                                                'is_best': True}}},
                                                                                                 '10.154.2.10/32': {'next_hop': {'192.168.23.2': {'interface': 'Ethernet1/3.23',
                                                                                                                                                 'is_best': True}}},
                                                                                                 '10.154.2.2/32': {'next_hop': {'192.168.23.2': {'interface': 'Ethernet1/3.23',
                                                                                                                                                'is_best': True}}},
                                                                                                 '10.154.2.3/32': {'next_hop': {'192.168.23.2': {'interface': 'Ethernet1/3.23',
                                                                                                                                                'is_best': True}}},
                                                                                                 '10.154.2.4/32': {'next_hop': {'192.168.23.2': {'interface': 'Ethernet1/3.23',
                                                                                                                                                'is_best': True}}},
                                                                                                 '10.154.2.5/32': {'next_hop': {'192.168.23.2': {'interface': 'Ethernet1/3.23',
                                                                                                                                                'is_best': True}}},
                                                                                                 '10.154.2.6/32': {'next_hop': {'192.168.23.2': {'interface': 'Ethernet1/3.23',
                                                                                                                                                'is_best': True}}},
                                                                                                 '10.154.2.7/32': {'next_hop': {'192.168.23.2': {'interface': 'Ethernet1/3.23',
                                                                                                                                                'is_best': True}}},
                                                                                                 '10.154.2.8/32': {'next_hop': {'192.168.23.2': {'interface': 'Ethernet1/3.23',
                                                                                                                                                'is_best': True}}},
                                                                                                 '10.154.2.9/32': {'next_hop': {'192.168.23.2': {'interface': 'Ethernet1/3.23',
                                                                                                                                                'is_best': True}}},
                                                                                                 '10.154.3.1/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501003'}}},
                                                                                                 '10.154.3.10/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                            'is_best': False,
                                                                                                                                            'label': 'vni:   501003'}}},
                                                                                                 '10.154.3.2/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501003'}}},
                                                                                                 '10.154.3.3/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501003'}}},
                                                                                                 '10.154.3.4/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501003'}}},
                                                                                                 '10.154.3.5/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501003'}}},
                                                                                                 '10.154.3.6/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501003'}}},
                                                                                                 '10.154.3.7/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501003'}}},
                                                                                                 '10.154.3.8/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501003'}}},
                                                                                                 '10.154.3.9/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501003'}}},
                                                                                                 '10.154.4.1/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501003'}}},
                                                                                                 '10.154.4.10/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                            'is_best': False,
                                                                                                                                            'label': 'vni:   501003'}}},
                                                                                                 '10.154.4.2/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501003'}}},
                                                                                                 '10.154.4.3/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501003'}}},
                                                                                                 '10.154.4.4/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501003'}}},
                                                                                                 '10.154.4.5/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501003'}}},
                                                                                                 '10.154.4.6/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501003'}}},
                                                                                                 '10.154.4.7/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501003'}}},
                                                                                                 '10.154.4.8/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501003'}}},
                                                                                                 '10.154.4.9/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
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
                                                                                                 '10.106.1.1/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501004'}}},
                                                                                                 '10.106.1.10/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                            'is_best': False,
                                                                                                                                            'label': 'vni:   501004'}}},
                                                                                                 '10.106.1.2/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501004'}}},
                                                                                                 '10.106.1.3/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501004'}}},
                                                                                                 '10.106.1.4/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501004'}}},
                                                                                                 '10.106.1.5/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501004'}}},
                                                                                                 '10.106.1.6/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501004'}}},
                                                                                                 '10.106.1.7/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501004'}}},
                                                                                                 '10.106.1.8/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501004'}}},
                                                                                                 '10.106.1.9/32': {'next_hop': {'10.4.1.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501004'}}},
                                                                                                 '10.106.2.1/32': {'next_hop': {'192.168.24.2': {'interface': 'Ethernet1/3.24',
                                                                                                                                                'is_best': True}}},
                                                                                                 '10.106.2.10/32': {'next_hop': {'192.168.24.2': {'interface': 'Ethernet1/3.24',
                                                                                                                                                 'is_best': True}}},
                                                                                                 '10.106.2.2/32': {'next_hop': {'192.168.24.2': {'interface': 'Ethernet1/3.24',
                                                                                                                                                'is_best': True}}},
                                                                                                 '10.106.2.3/32': {'next_hop': {'192.168.24.2': {'interface': 'Ethernet1/3.24',
                                                                                                                                                'is_best': True}}},
                                                                                                 '10.106.2.4/32': {'next_hop': {'192.168.24.2': {'interface': 'Ethernet1/3.24',
                                                                                                                                                'is_best': True}}},
                                                                                                 '10.106.2.5/32': {'next_hop': {'192.168.24.2': {'interface': 'Ethernet1/3.24',
                                                                                                                                                'is_best': True}}},
                                                                                                 '10.106.2.6/32': {'next_hop': {'192.168.24.2': {'interface': 'Ethernet1/3.24',
                                                                                                                                                'is_best': True}}},
                                                                                                 '10.106.2.7/32': {'next_hop': {'192.168.24.2': {'interface': 'Ethernet1/3.24',
                                                                                                                                                'is_best': True}}},
                                                                                                 '10.106.2.8/32': {'next_hop': {'192.168.24.2': {'interface': 'Ethernet1/3.24',
                                                                                                                                                'is_best': True}}},
                                                                                                 '10.106.2.9/32': {'next_hop': {'192.168.24.2': {'interface': 'Ethernet1/3.24',
                                                                                                                                                'is_best': True}}},
                                                                                                 '10.106.3.1/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501004'}}},
                                                                                                 '10.106.3.10/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                            'is_best': False,
                                                                                                                                            'label': 'vni:   501004'}}},
                                                                                                 '10.106.3.2/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501004'}}},
                                                                                                 '10.106.3.3/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501004'}}},
                                                                                                 '10.106.3.4/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501004'}}},
                                                                                                 '10.106.3.5/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501004'}}},
                                                                                                 '10.106.3.6/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501004'}}},
                                                                                                 '10.106.3.7/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501004'}}},
                                                                                                 '10.106.3.8/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501004'}}},
                                                                                                 '10.106.3.9/32': {'next_hop': {'10.36.3.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501004'}}},
                                                                                                 '10.106.4.1/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501004'}}},
                                                                                                 '10.106.4.10/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                            'is_best': False,
                                                                                                                                            'label': 'vni:   501004'}}},
                                                                                                 '10.106.4.2/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501004'}}},
                                                                                                 '10.106.4.3/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501004'}}},
                                                                                                 '10.106.4.4/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501004'}}},
                                                                                                 '10.106.4.5/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501004'}}},
                                                                                                 '10.106.4.6/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501004'}}},
                                                                                                 '10.106.4.7/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501004'}}},
                                                                                                 '10.106.4.8/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
                                                                                                                                           'is_best': False,
                                                                                                                                           'label': 'vni:   501004'}}},
                                                                                                 '10.106.4.9/32': {'next_hop': {'10.64.4.2': {'interface': 'nve1',
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
                                                                                             '10.4.1.1/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                      'is_best': False},
                                                                                                                         '10.229.1.2': {'interface': 'Ethernet1/2',
                                                                                                                                      'is_best': False}}},
                                                                                             '10.4.1.2/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                      'is_best': True},
                                                                                                                         '10.229.1.2': {'interface': 'Ethernet1/2',
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
                                                                                             '10.69.111.0/24': {'next_hop': {'Drop': {'interface': 'Null0',
                                                                                                                                        'is_best': False}}},
                                                                                             '127.0.0.0/8': {'next_hop': {'Drop': {'interface': 'Null0',
                                                                                                                                   'is_best': False}}},
                                                                                             '10.16.2.1/32': {'next_hop': {'Receive': {'interface': 'sup-eth1',
                                                                                                                                     'is_best': False}}},
                                                                                             '10.16.2.2/32': {'next_hop': {'Receive': {'interface': 'sup-eth1',
                                                                                                                                     'is_best': False}}},
                                                                                             '10.186.1.0/24': {'next_hop': {'10.229.1.2': {'interface': 'Ethernet1/2',
                                                                                                                                       'is_best': False}}},
                                                                                             '10.229.1.0/24': {'next_hop': {'Attached': {'interface': 'Ethernet1/2',
                                                                                                                                       'is_best': False}}},
                                                                                             '10.229.1.0/32': {'next_hop': {'Drop': {'interface': 'Null0',
                                                                                                                                   'is_best': False}}},
                                                                                             '10.229.1.1/32': {'next_hop': {'Receive': {'interface': 'sup-eth1',
                                                                                                                                      'is_best': False}}},
                                                                                             '10.229.1.2/32': {'next_hop': {'10.229.1.2': {'interface': 'Ethernet1/2',
                                                                                                                                       'is_best': False}}},
                                                                                             '10.229.1.255/32': {'next_hop': {'Attached': {'interface': 'Ethernet1/2',
                                                                                                                                         'is_best': False}}},
                                                                                             '10.19.1.0/24': {'next_hop': {'10.229.1.2': {'interface': 'Ethernet1/2',
                                                                                                                                       'is_best': False}}},
                                                                                             '10.66.1.0/24': {'next_hop': {'10.229.1.2': {'interface': 'Ethernet1/2',
                                                                                                                                       'is_best': False}}},
                                                                                             '192.168.195.1/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                            'is_best': False}}},
                                                                                             '10.205.0.0/16': {'next_hop': {'Drop': {'interface': 'Null0',
                                                                                                                                    'is_best': False}}},
                                                                                             '10.205.25.0/24': {'next_hop': {'Drop': {'interface': 'Null0',
                                                                                                                                     'is_best': False}}},
                                                                                             '255.255.255.255/32': {'next_hop': {'Receive': {'interface': 'sup-eth1',
                                                                                                                                             'is_best': False}}},
                                                                                             '10.36.3.1/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                      'is_best': False},
                                                                                                                         '10.229.1.2': {'interface': 'Ethernet1/2',
                                                                                                                                      'is_best': False}}},
                                                                                             '10.36.3.2/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                      'is_best': True},
                                                                                                                         '10.229.1.2': {'interface': 'Ethernet1/2',
                                                                                                                                      'is_best': False}}},
                                                                                             '10.64.4.1/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                      'is_best': False},
                                                                                                                         '10.229.1.2': {'interface': 'Ethernet1/2',
                                                                                                                                      'is_best': False}}},
                                                                                             '10.64.4.2/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                      'is_best': True},
                                                                                                                         '10.229.1.2': {'interface': 'Ethernet1/2',
                                                                                                                                      'is_best': False}}},
                                                                                             '10.166.98.98/32': {'next_hop': {'10.2.1.2': {'interface': 'Ethernet1/1',
                                                                                                                                          'is_best': False}}},
                                                                                             '10.189.99.99/32': {'next_hop': {'10.229.1.2': {'interface': 'Ethernet1/2',
                                                                                                                                          'is_best': False}}}}}}}}}}}
    golden_output = {'execute.return_value':'''
        #vtep1 show forwarding ipv4 vrf all 
        slot  1
        =======
        
        
        IPv4 routes for table default/base
        
        ------------------+-----------------------------------------+----------------------+-----------------+-----------------
        Prefix            | Next-hop                                | Interface            | Labels          | Partial Install 
        ------------------+-----------------------------------------+----------------------+-----------------+-----------------
        10.4.1.1/32           10.2.1.2                                  Ethernet1/1         
        *10.4.1.2/32          10.2.1.2                                  Ethernet1/1         
        10.16.2.1/32           Receive                                   sup-eth1
        10.16.2.2/32           Receive                                   sup-eth1
        10.36.3.1/32           10.2.1.2                                  Ethernet1/1         
        *10.36.3.2/32          10.2.1.2                                  Ethernet1/1         
        10.64.4.1/32           10.2.1.2                                  Ethernet1/1         
        *10.64.4.2/32          10.2.1.2                                  Ethernet1/1         
        10.2.1.0/32          Drop                                      Null0
        10.2.1.1/32          Receive                                   sup-eth1
        10.2.1.2/32          10.2.1.2                                  Ethernet1/1         
        10.2.1.255/32        Attached                                  Ethernet1/1
        10.229.1.0/32          Drop                                      Null0
        10.229.1.1/32          Receive                                   sup-eth1
        10.229.1.2/32          10.229.1.2                                  Ethernet1/2         
        10.229.1.255/32        Attached                                  Ethernet1/2
        10.166.98.98/32       10.2.1.2                                  Ethernet1/1         
        10.189.99.99/32       10.229.1.2                                  Ethernet1/2         
        192.168.195.1/32     10.2.1.2                                  Ethernet1/1         
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
        10.1.1.1/32         10.4.1.2            nve1        vni:   501001    
        10.1.1.2/32         10.4.1.2            nve1        vni:   501001    
        10.1.1.3/32         10.4.1.2            nve1        vni:   501001    
        10.1.1.4/32         10.4.1.2            nve1        vni:   501001    
        10.1.1.5/32         10.4.1.2            nve1        vni:   501001    
        10.1.1.6/32         10.4.1.2            nve1        vni:   501001    
        10.1.1.7/32         10.4.1.2            nve1        vni:   501001    
        10.1.1.8/32         10.4.1.2            nve1        vni:   501001    
        10.1.1.9/32         10.4.1.2            nve1        vni:   501001    
        10.1.1.10/32        10.4.1.2            nve1        vni:   501001    
        *10.1.2.1/32        192.168.21.2                              Ethernet1/3.21      
        *10.1.2.2/32        192.168.21.2                              Ethernet1/3.21      
        *10.1.2.3/32        192.168.21.2                              Ethernet1/3.21      
        *10.1.2.4/32        192.168.21.2                              Ethernet1/3.21      
        *10.1.2.5/32        192.168.21.2                              Ethernet1/3.21      
        *10.1.2.6/32        192.168.21.2                              Ethernet1/3.21      
        *10.1.2.7/32        192.168.21.2                              Ethernet1/3.21      
        *10.1.2.8/32        192.168.21.2                              Ethernet1/3.21      
        *10.1.2.9/32        192.168.21.2                              Ethernet1/3.21      
        *10.1.2.10/32       192.168.21.2                              Ethernet1/3.21      
        10.1.3.1/32         10.36.3.2            nve1        vni:   501001    
        10.1.3.2/32         10.36.3.2            nve1        vni:   501001    
        10.1.3.3/32         10.36.3.2            nve1        vni:   501001    
        10.1.3.4/32         10.36.3.2            nve1        vni:   501001    
        10.1.3.5/32         10.36.3.2            nve1        vni:   501001    
        10.1.3.6/32         10.36.3.2            nve1        vni:   501001    
        10.1.3.7/32         10.36.3.2            nve1        vni:   501001    
        10.1.3.8/32         10.36.3.2            nve1        vni:   501001    
        10.1.3.9/32         10.36.3.2            nve1        vni:   501001    
        10.1.3.10/32        10.36.3.2            nve1        vni:   501001    
        10.1.4.1/32         10.64.4.2            nve1        vni:   501001    
        10.1.4.2/32         10.64.4.2            nve1        vni:   501001    
        10.1.4.3/32         10.64.4.2            nve1        vni:   501001    
        10.1.4.4/32         10.64.4.2            nve1        vni:   501001    
        10.1.4.5/32         10.64.4.2            nve1        vni:   501001    
        10.1.4.6/32         10.64.4.2            nve1        vni:   501001    
        10.1.4.7/32         10.64.4.2            nve1        vni:   501001    
        10.1.4.8/32         10.64.4.2            nve1        vni:   501001    
        10.1.4.9/32         10.64.4.2            nve1        vni:   501001    
        10.1.4.10/32        10.64.4.2            nve1        vni:   501001    
        192.168.21.0/24      Attached                                  Ethernet1/3.21
        192.168.21.0/32      Drop                                      Null0
        192.168.21.1/32      Receive                                   sup-eth1
        192.168.21.2/32      192.168.21.2                              Ethernet1/3.21      
        192.168.21.255/32    Attached                                  Ethernet1/3.21
        IPv4 routes for table VRF_Flow1_2/base
        
        ------------------+-----------------------------------------+----------------------+-----------------+-----------------
        Prefix            | Next-hop                                | Interface            | Labels          | Partial Install 
        ------------------+-----------------------------------------+----------------------+-----------------+-----------------
        10.204.1.1/32         10.4.1.2            nve1        vni:   501002    
        10.204.1.2/32         10.4.1.2            nve1        vni:   501002    
        10.204.1.3/32         10.4.1.2            nve1        vni:   501002    
        10.204.1.4/32         10.4.1.2            nve1        vni:   501002    
        10.204.1.5/32         10.4.1.2            nve1        vni:   501002    
        10.204.1.6/32         10.4.1.2            nve1        vni:   501002    
        10.204.1.7/32         10.4.1.2            nve1        vni:   501002    
        10.204.1.8/32         10.4.1.2            nve1        vni:   501002    
        10.204.1.9/32         10.4.1.2            nve1        vni:   501002    
        10.204.1.10/32        10.4.1.2            nve1        vni:   501002    
        *10.204.2.1/32        192.168.22.2                              Ethernet1/3.22      
        *10.204.2.2/32        192.168.22.2                              Ethernet1/3.22      
        *10.204.2.3/32        192.168.22.2                              Ethernet1/3.22      
        *10.204.2.4/32        192.168.22.2                              Ethernet1/3.22      
        *10.204.2.5/32        192.168.22.2                              Ethernet1/3.22      
        *10.204.2.6/32        192.168.22.2                              Ethernet1/3.22      
        *10.204.2.7/32        192.168.22.2                              Ethernet1/3.22      
        *10.204.2.8/32        192.168.22.2                              Ethernet1/3.22      
        *10.204.2.9/32        192.168.22.2                              Ethernet1/3.22      
        *10.204.2.10/32       192.168.22.2                              Ethernet1/3.22      
        10.204.3.1/32         10.36.3.2            nve1        vni:   501002    
        10.204.3.2/32         10.36.3.2            nve1        vni:   501002    
        10.204.3.3/32         10.36.3.2            nve1        vni:   501002    
        10.204.3.4/32         10.36.3.2            nve1        vni:   501002    
        10.204.3.5/32         10.36.3.2            nve1        vni:   501002    
        10.204.3.6/32         10.36.3.2            nve1        vni:   501002    
        10.204.3.7/32         10.36.3.2            nve1        vni:   501002    
        10.204.3.8/32         10.36.3.2            nve1        vni:   501002    
        10.204.3.9/32         10.36.3.2            nve1        vni:   501002    
        10.204.3.10/32        10.36.3.2            nve1        vni:   501002    
        10.204.4.1/32         10.64.4.2            nve1        vni:   501002    
        10.204.4.2/32         10.64.4.2            nve1        vni:   501002    
        10.204.4.3/32         10.64.4.2            nve1        vni:   501002    
        10.204.4.4/32         10.64.4.2            nve1        vni:   501002    
        10.204.4.5/32         10.64.4.2            nve1        vni:   501002    
        10.204.4.6/32         10.64.4.2            nve1        vni:   501002    
        10.204.4.7/32         10.64.4.2            nve1        vni:   501002    
        10.204.4.8/32         10.64.4.2            nve1        vni:   501002    
        10.204.4.9/32         10.64.4.2            nve1        vni:   501002    
        10.204.4.10/32        10.64.4.2            nve1        vni:   501002    
        192.168.22.0/24      Attached                                  Ethernet1/3.22
        192.168.22.0/32      Drop                                      Null0
        192.168.22.1/32      Receive                                   sup-eth1
        192.168.22.2/32      192.168.22.2                              Ethernet1/3.22      
        192.168.22.255/32    Attached                                  Ethernet1/3.22
        IPv4 routes for table VRF_Flow1_3/base
        
        ------------------+-----------------------------------------+----------------------+-----------------+-----------------
        Prefix            | Next-hop                                | Interface            | Labels          | Partial Install 
        ------------------+-----------------------------------------+----------------------+-----------------+-----------------
        10.154.1.1/32         10.4.1.2            nve1        vni:   501003    
        10.154.1.2/32         10.4.1.2            nve1        vni:   501003    
        10.154.1.3/32         10.4.1.2            nve1        vni:   501003    
        10.154.1.4/32         10.4.1.2            nve1        vni:   501003    
        10.154.1.5/32         10.4.1.2            nve1        vni:   501003    
        10.154.1.6/32         10.4.1.2            nve1        vni:   501003    
        10.154.1.7/32         10.4.1.2            nve1        vni:   501003    
        10.154.1.8/32         10.4.1.2            nve1        vni:   501003    
        10.154.1.9/32         10.4.1.2            nve1        vni:   501003    
        10.154.1.10/32        10.4.1.2            nve1        vni:   501003    
        *10.154.2.1/32        192.168.23.2                              Ethernet1/3.23      
        *10.154.2.2/32        192.168.23.2                              Ethernet1/3.23      
        *10.154.2.3/32        192.168.23.2                              Ethernet1/3.23      
        *10.154.2.4/32        192.168.23.2                              Ethernet1/3.23      
        *10.154.2.5/32        192.168.23.2                              Ethernet1/3.23      
        *10.154.2.6/32        192.168.23.2                              Ethernet1/3.23      
        *10.154.2.7/32        192.168.23.2                              Ethernet1/3.23      
        *10.154.2.8/32        192.168.23.2                              Ethernet1/3.23      
        *10.154.2.9/32        192.168.23.2                              Ethernet1/3.23      
        *10.154.2.10/32       192.168.23.2                              Ethernet1/3.23      
        10.154.3.1/32         10.36.3.2            nve1        vni:   501003    
        10.154.3.2/32         10.36.3.2            nve1        vni:   501003    
        10.154.3.3/32         10.36.3.2            nve1        vni:   501003    
        10.154.3.4/32         10.36.3.2            nve1        vni:   501003    
        10.154.3.5/32         10.36.3.2            nve1        vni:   501003    
        10.154.3.6/32         10.36.3.2            nve1        vni:   501003    
        10.154.3.7/32         10.36.3.2            nve1        vni:   501003    
        10.154.3.8/32         10.36.3.2            nve1        vni:   501003    
        10.154.3.9/32         10.36.3.2            nve1        vni:   501003    
        10.154.3.10/32        10.36.3.2            nve1        vni:   501003    
        10.154.4.1/32         10.64.4.2            nve1        vni:   501003    
        10.154.4.2/32         10.64.4.2            nve1        vni:   501003    
        10.154.4.3/32         10.64.4.2            nve1        vni:   501003    
        10.154.4.4/32         10.64.4.2            nve1        vni:   501003    
        10.154.4.5/32         10.64.4.2            nve1        vni:   501003    
        10.154.4.6/32         10.64.4.2            nve1        vni:   501003    
        10.154.4.7/32         10.64.4.2            nve1        vni:   501003    
        10.154.4.8/32         10.64.4.2            nve1        vni:   501003    
        10.154.4.9/32         10.64.4.2            nve1        vni:   501003    
        10.154.4.10/32        10.64.4.2            nve1        vni:   501003    
        192.168.23.0/24      Attached                                  Ethernet1/3.23
        192.168.23.0/32      Drop                                      Null0
        192.168.23.1/32      Receive                                   sup-eth1
        192.168.23.2/32      192.168.23.2                              Ethernet1/3.23      
        192.168.23.255/32    Attached                                  Ethernet1/3.23
        IPv4 routes for table VRF_Flow1_4/base
        
        ------------------+-----------------------------------------+----------------------+-----------------+-----------------
        Prefix            | Next-hop                                | Interface            | Labels          | Partial Install 
        ------------------+-----------------------------------------+----------------------+-----------------+-----------------
        10.106.1.1/32         10.4.1.2            nve1        vni:   501004    
        10.106.1.2/32         10.4.1.2            nve1        vni:   501004    
        10.106.1.3/32         10.4.1.2            nve1        vni:   501004    
        10.106.1.4/32         10.4.1.2            nve1        vni:   501004    
        10.106.1.5/32         10.4.1.2            nve1        vni:   501004    
        10.106.1.6/32         10.4.1.2            nve1        vni:   501004    
        10.106.1.7/32         10.4.1.2            nve1        vni:   501004    
        10.106.1.8/32         10.4.1.2            nve1        vni:   501004    
        10.106.1.9/32         10.4.1.2            nve1        vni:   501004    
        10.106.1.10/32        10.4.1.2            nve1        vni:   501004    
        *10.106.2.1/32        192.168.24.2                              Ethernet1/3.24      
        *10.106.2.2/32        192.168.24.2                              Ethernet1/3.24      
        *10.106.2.3/32        192.168.24.2                              Ethernet1/3.24      
        *10.106.2.4/32        192.168.24.2                              Ethernet1/3.24      
        *10.106.2.5/32        192.168.24.2                              Ethernet1/3.24      
        *10.106.2.6/32        192.168.24.2                              Ethernet1/3.24      
        *10.106.2.7/32        192.168.24.2                              Ethernet1/3.24      
        *10.106.2.8/32        192.168.24.2                              Ethernet1/3.24      
        *10.106.2.9/32        192.168.24.2                              Ethernet1/3.24      
        *10.106.2.10/32       192.168.24.2                              Ethernet1/3.24      
        10.106.3.1/32         10.36.3.2            nve1        vni:   501004    
        10.106.3.2/32         10.36.3.2            nve1        vni:   501004    
        10.106.3.3/32         10.36.3.2            nve1        vni:   501004    
        10.106.3.4/32         10.36.3.2            nve1        vni:   501004    
        10.106.3.5/32         10.36.3.2            nve1        vni:   501004    
        10.106.3.6/32         10.36.3.2            nve1        vni:   501004    
        10.106.3.7/32         10.36.3.2            nve1        vni:   501004    
        10.106.3.8/32         10.36.3.2            nve1        vni:   501004    
        10.106.3.9/32         10.36.3.2            nve1        vni:   501004    
        10.106.3.10/32        10.36.3.2            nve1        vni:   501004    
        10.106.4.1/32         10.64.4.2            nve1        vni:   501004    
        10.106.4.2/32         10.64.4.2            nve1        vni:   501004    
        10.106.4.3/32         10.64.4.2            nve1        vni:   501004    
        10.106.4.4/32         10.64.4.2            nve1        vni:   501004    
        10.106.4.5/32         10.64.4.2            nve1        vni:   501004    
        10.106.4.6/32         10.64.4.2            nve1        vni:   501004    
        10.106.4.7/32         10.64.4.2            nve1        vni:   501004    
        10.106.4.8/32         10.64.4.2            nve1        vni:   501004    
        10.106.4.9/32         10.64.4.2            nve1        vni:   501004    
        10.106.4.10/32        10.64.4.2            nve1        vni:   501004    
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
        10.4.1.1/32           10.2.1.2                                  Ethernet1/1         
                             10.229.1.2                                  Ethernet1/2         
        *10.4.1.2/32          10.2.1.2                                  Ethernet1/1         
                             10.229.1.2                                  Ethernet1/2         
        10.16.2.1/32           Receive                                   sup-eth1
        10.16.2.2/32           Receive                                   sup-eth1
        10.36.3.1/32           10.2.1.2                                  Ethernet1/1         
                             10.229.1.2                                  Ethernet1/2         
        *10.36.3.2/32          10.2.1.2                                  Ethernet1/1         
                             10.229.1.2                                  Ethernet1/2         
        10.64.4.1/32           10.2.1.2                                  Ethernet1/1         
                             10.229.1.2                                  Ethernet1/2         
        *10.64.4.2/32          10.2.1.2                                  Ethernet1/1         
                             10.229.1.2                                  Ethernet1/2         
        10.1.1.0/24          10.2.1.2                                  Ethernet1/1         
        10.2.1.0/24          Attached                                  Ethernet1/1
        10.2.1.0/32          Drop                                      Null0
        10.2.1.1/32          Receive                                   sup-eth1
        10.2.1.2/32          10.2.1.2                                  Ethernet1/1         
        10.2.1.255/32        Attached                                  Ethernet1/1
        10.3.1.0/24          10.2.1.2                                  Ethernet1/1         
        10.4.1.0/24          10.2.1.2                                  Ethernet1/1         
        10.186.1.0/24          10.229.1.2                                  Ethernet1/2         
        10.229.1.0/24          Attached                                  Ethernet1/2
        10.229.1.0/32          Drop                                      Null0
        10.229.1.1/32          Receive                                   sup-eth1
        10.229.1.2/32          10.229.1.2                                  Ethernet1/2         
        10.229.1.255/32        Attached                                  Ethernet1/2
        10.19.1.0/24          10.229.1.2                                  Ethernet1/2         
        10.66.1.0/24          10.229.1.2                                  Ethernet1/2         
        10.205.0.0/16         Drop                                      Null0
        10.205.25.0/24        Drop                                      Null0
        10.166.98.98/32       10.2.1.2                                  Ethernet1/1         
        10.189.99.99/32       10.229.1.2                                  Ethernet1/2         
        10.69.111.0/24     Drop                                      Null0
        192.168.195.1/32     10.2.1.2                                  Ethernet1/1         
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
        10.1.1.1/32         10.4.1.2            nve1        vni:   501001    
        10.1.1.2/32         10.4.1.2            nve1        vni:   501001    
        10.1.1.3/32         10.4.1.2            nve1        vni:   501001    
        10.1.1.4/32         10.4.1.2            nve1        vni:   501001    
        10.1.1.5/32         10.4.1.2            nve1        vni:   501001    
        10.1.1.6/32         10.4.1.2            nve1        vni:   501001    
        10.1.1.7/32         10.4.1.2            nve1        vni:   501001    
        10.1.1.8/32         10.4.1.2            nve1        vni:   501001    
        10.1.1.9/32         10.4.1.2            nve1        vni:   501001    
        10.1.1.10/32        10.4.1.2            nve1        vni:   501001    
        *10.1.2.1/32        192.168.21.2                              Ethernet1/3.21      
        *10.1.2.2/32        192.168.21.2                              Ethernet1/3.21      
        *10.1.2.3/32        192.168.21.2                              Ethernet1/3.21      
        *10.1.2.4/32        192.168.21.2                              Ethernet1/3.21      
        *10.1.2.5/32        192.168.21.2                              Ethernet1/3.21      
        *10.1.2.6/32        192.168.21.2                              Ethernet1/3.21      
        *10.1.2.7/32        192.168.21.2                              Ethernet1/3.21      
        *10.1.2.8/32        192.168.21.2                              Ethernet1/3.21      
        *10.1.2.9/32        192.168.21.2                              Ethernet1/3.21      
        *10.1.2.10/32       192.168.21.2                              Ethernet1/3.21      
        10.1.3.1/32         10.36.3.2            nve1        vni:   501001    
        10.1.3.2/32         10.36.3.2            nve1        vni:   501001    
        10.1.3.3/32         10.36.3.2            nve1        vni:   501001    
        10.1.3.4/32         10.36.3.2            nve1        vni:   501001    
        10.1.3.5/32         10.36.3.2            nve1        vni:   501001    
        10.1.3.6/32         10.36.3.2            nve1        vni:   501001    
        10.1.3.7/32         10.36.3.2            nve1        vni:   501001    
        10.1.3.8/32         10.36.3.2            nve1        vni:   501001    
        10.1.3.9/32         10.36.3.2            nve1        vni:   501001    
        10.1.3.10/32        10.36.3.2            nve1        vni:   501001    
        10.1.4.1/32         10.64.4.2            nve1        vni:   501001    
        10.1.4.2/32         10.64.4.2            nve1        vni:   501001    
        10.1.4.3/32         10.64.4.2            nve1        vni:   501001    
        10.1.4.4/32         10.64.4.2            nve1        vni:   501001    
        10.1.4.5/32         10.64.4.2            nve1        vni:   501001    
        10.1.4.6/32         10.64.4.2            nve1        vni:   501001    
        10.1.4.7/32         10.64.4.2            nve1        vni:   501001    
        10.1.4.8/32         10.64.4.2            nve1        vni:   501001    
        10.1.4.9/32         10.64.4.2            nve1        vni:   501001    
        10.1.4.10/32        10.64.4.2            nve1        vni:   501001    
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
        10.204.1.1/32         10.4.1.2            nve1        vni:   501002    
        10.204.1.2/32         10.4.1.2            nve1        vni:   501002    
        10.204.1.3/32         10.4.1.2            nve1        vni:   501002    
        10.204.1.4/32         10.4.1.2            nve1        vni:   501002    
        10.204.1.5/32         10.4.1.2            nve1        vni:   501002    
        10.204.1.6/32         10.4.1.2            nve1        vni:   501002    
        10.204.1.7/32         10.4.1.2            nve1        vni:   501002    
        10.204.1.8/32         10.4.1.2            nve1        vni:   501002    
        10.204.1.9/32         10.4.1.2            nve1        vni:   501002    
        10.204.1.10/32        10.4.1.2            nve1        vni:   501002    
        *10.204.2.1/32        192.168.22.2                              Ethernet1/3.22      
        *10.204.2.2/32        192.168.22.2                              Ethernet1/3.22      
        *10.204.2.3/32        192.168.22.2                              Ethernet1/3.22      
        *10.204.2.4/32        192.168.22.2                              Ethernet1/3.22      
        *10.204.2.5/32        192.168.22.2                              Ethernet1/3.22      
        *10.204.2.6/32        192.168.22.2                              Ethernet1/3.22      
        *10.204.2.7/32        192.168.22.2                              Ethernet1/3.22      
        *10.204.2.8/32        192.168.22.2                              Ethernet1/3.22      
        *10.204.2.9/32        192.168.22.2                              Ethernet1/3.22      
        *10.204.2.10/32       192.168.22.2                              Ethernet1/3.22      
        10.204.3.1/32         10.36.3.2            nve1        vni:   501002    
        10.204.3.2/32         10.36.3.2            nve1        vni:   501002    
        10.204.3.3/32         10.36.3.2            nve1        vni:   501002    
        10.204.3.4/32         10.36.3.2            nve1        vni:   501002    
        10.204.3.5/32         10.36.3.2            nve1        vni:   501002    
        10.204.3.6/32         10.36.3.2            nve1        vni:   501002    
        10.204.3.7/32         10.36.3.2            nve1        vni:   501002    
        10.204.3.8/32         10.36.3.2            nve1        vni:   501002    
        10.204.3.9/32         10.36.3.2            nve1        vni:   501002    
        10.204.3.10/32        10.36.3.2            nve1        vni:   501002    
        10.204.4.1/32         10.64.4.2            nve1        vni:   501002    
        10.204.4.2/32         10.64.4.2            nve1        vni:   501002    
        10.204.4.3/32         10.64.4.2            nve1        vni:   501002    
        10.204.4.4/32         10.64.4.2            nve1        vni:   501002    
        10.204.4.5/32         10.64.4.2            nve1        vni:   501002    
        10.204.4.6/32         10.64.4.2            nve1        vni:   501002    
        10.204.4.7/32         10.64.4.2            nve1        vni:   501002    
        10.204.4.8/32         10.64.4.2            nve1        vni:   501002    
        10.204.4.9/32         10.64.4.2            nve1        vni:   501002    
        10.204.4.10/32        10.64.4.2            nve1        vni:   501002    
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
        10.154.1.1/32         10.4.1.2            nve1        vni:   501003    
        10.154.1.2/32         10.4.1.2            nve1        vni:   501003    
        10.154.1.3/32         10.4.1.2            nve1        vni:   501003    
        10.154.1.4/32         10.4.1.2            nve1        vni:   501003    
        10.154.1.5/32         10.4.1.2            nve1        vni:   501003    
        10.154.1.6/32         10.4.1.2            nve1        vni:   501003    
        10.154.1.7/32         10.4.1.2            nve1        vni:   501003    
        10.154.1.8/32         10.4.1.2            nve1        vni:   501003    
        10.154.1.9/32         10.4.1.2            nve1        vni:   501003    
        10.154.1.10/32        10.4.1.2            nve1        vni:   501003    
        *10.154.2.1/32        192.168.23.2                              Ethernet1/3.23      
        *10.154.2.2/32        192.168.23.2                              Ethernet1/3.23      
        *10.154.2.3/32        192.168.23.2                              Ethernet1/3.23      
        *10.154.2.4/32        192.168.23.2                              Ethernet1/3.23      
        *10.154.2.5/32        192.168.23.2                              Ethernet1/3.23      
        *10.154.2.6/32        192.168.23.2                              Ethernet1/3.23      
        *10.154.2.7/32        192.168.23.2                              Ethernet1/3.23      
        *10.154.2.8/32        192.168.23.2                              Ethernet1/3.23      
        *10.154.2.9/32        192.168.23.2                              Ethernet1/3.23      
        *10.154.2.10/32       192.168.23.2                              Ethernet1/3.23      
        10.154.3.1/32         10.36.3.2            nve1        vni:   501003    
        10.154.3.2/32         10.36.3.2            nve1        vni:   501003    
        10.154.3.3/32         10.36.3.2            nve1        vni:   501003    
        10.154.3.4/32         10.36.3.2            nve1        vni:   501003    
        10.154.3.5/32         10.36.3.2            nve1        vni:   501003    
        10.154.3.6/32         10.36.3.2            nve1        vni:   501003    
        10.154.3.7/32         10.36.3.2            nve1        vni:   501003    
        10.154.3.8/32         10.36.3.2            nve1        vni:   501003    
        10.154.3.9/32         10.36.3.2            nve1        vni:   501003    
        10.154.3.10/32        10.36.3.2            nve1        vni:   501003    
        10.154.4.1/32         10.64.4.2            nve1        vni:   501003    
        10.154.4.2/32         10.64.4.2            nve1        vni:   501003    
        10.154.4.3/32         10.64.4.2            nve1        vni:   501003    
        10.154.4.4/32         10.64.4.2            nve1        vni:   501003    
        10.154.4.5/32         10.64.4.2            nve1        vni:   501003    
        10.154.4.6/32         10.64.4.2            nve1        vni:   501003    
        10.154.4.7/32         10.64.4.2            nve1        vni:   501003    
        10.154.4.8/32         10.64.4.2            nve1        vni:   501003    
        10.154.4.9/32         10.64.4.2            nve1        vni:   501003    
        10.154.4.10/32        10.64.4.2            nve1        vni:   501003    
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
        10.106.1.1/32         10.4.1.2            nve1        vni:   501004    
        10.106.1.2/32         10.4.1.2            nve1        vni:   501004    
        10.106.1.3/32         10.4.1.2            nve1        vni:   501004    
        10.106.1.4/32         10.4.1.2            nve1        vni:   501004    
        10.106.1.5/32         10.4.1.2            nve1        vni:   501004    
        10.106.1.6/32         10.4.1.2            nve1        vni:   501004    
        10.106.1.7/32         10.4.1.2            nve1        vni:   501004    
        10.106.1.8/32         10.4.1.2            nve1        vni:   501004    
        10.106.1.9/32         10.4.1.2            nve1        vni:   501004    
        10.106.1.10/32        10.4.1.2            nve1        vni:   501004    
        *10.106.2.1/32        192.168.24.2                              Ethernet1/3.24      
        *10.106.2.2/32        192.168.24.2                              Ethernet1/3.24      
        *10.106.2.3/32        192.168.24.2                              Ethernet1/3.24      
        *10.106.2.4/32        192.168.24.2                              Ethernet1/3.24      
        *10.106.2.5/32        192.168.24.2                              Ethernet1/3.24      
        *10.106.2.6/32        192.168.24.2                              Ethernet1/3.24      
        *10.106.2.7/32        192.168.24.2                              Ethernet1/3.24      
        *10.106.2.8/32        192.168.24.2                              Ethernet1/3.24      
        *10.106.2.9/32        192.168.24.2                              Ethernet1/3.24      
        *10.106.2.10/32       192.168.24.2                              Ethernet1/3.24      
        10.106.3.1/32         10.36.3.2            nve1        vni:   501004    
        10.106.3.2/32         10.36.3.2            nve1        vni:   501004    
        10.106.3.3/32         10.36.3.2            nve1        vni:   501004    
        10.106.3.4/32         10.36.3.2            nve1        vni:   501004    
        10.106.3.5/32         10.36.3.2            nve1        vni:   501004    
        10.106.3.6/32         10.36.3.2            nve1        vni:   501004    
        10.106.3.7/32         10.36.3.2            nve1        vni:   501004    
        10.106.3.8/32         10.36.3.2            nve1        vni:   501004    
        10.106.3.9/32         10.36.3.2            nve1        vni:   501004    
        10.106.3.10/32        10.36.3.2            nve1        vni:   501004    
        10.106.4.1/32         10.64.4.2            nve1        vni:   501004    
        10.106.4.2/32         10.64.4.2            nve1        vni:   501004    
        10.106.4.3/32         10.64.4.2            nve1        vni:   501004    
        10.106.4.4/32         10.64.4.2            nve1        vni:   501004    
        10.106.4.5/32         10.64.4.2            nve1        vni:   501004    
        10.106.4.6/32         10.64.4.2            nve1        vni:   501004    
        10.106.4.7/32         10.64.4.2            nve1        vni:   501004    
        10.106.4.8/32         10.64.4.2            nve1        vni:   501004    
        10.106.4.9/32         10.64.4.2            nve1        vni:   501004    
        10.106.4.10/32        10.64.4.2            nve1        vni:   501004    
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
