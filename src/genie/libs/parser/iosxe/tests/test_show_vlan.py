#!/bin/env python
import re
import unittest
from unittest.mock import Mock

from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError

from genie.libs.parser.iosxe.show_vlan import ShowVlan, \
                                          ShowVlanMtu, \
                                          ShowVlanAccessMap, \
                                          ShowVlanRemoteSpan, \
                                          ShowVlanFilter

# ============================================
# unit test for 'show vlan'
# =============================================
class test_show_vlan(unittest.TestCase):
    '''
       unit test show vlan
    '''
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    golden_output_vlan_1 = {'execute.return_value': '''
VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Gi1/0/1, Gi1/0/2, Gi1/0/3, Gi1/0/5, Gi1/0/6, Gi1/0/12, Gi1/0/13, Gi1/0/14, Gi1/0/15, Gi1/0/16, Gi1/0/17, Gi1/0/18
                                                Gi1/0/19, Gi1/0/20, Gi1/0/21, Gi1/0/22
2    VLAN0002                         active
20   VLAN0020                         active
100  V100                             suspended
101  VLAN0101                         active
102  VLAN0102                         active
103  VLAN0103                         active
104  VLAN0104                         act/lshut

VLAN Type  SAID       MTU   Parent RingNo BridgeNo Stp  BrdgMode Trans1 Trans2
---- ----- ---------- ----- ------ ------ -------- ---- -------- ------ ------
1    enet  100001     1500  -      -      -        -    -        0      0
100  enet  100100     1500  -      -      -        -    -        0      0
101  enet  100101     1500  -      -      -        -    -        0      0


Remote SPAN VLANs
------------------------------------------------------------------------------
20,21,102,24-27

Primary Secondary Type              Ports
------- --------- ----------------- ------------------------------------------
2       301       community         Fa5/3, Fa5/25
 2       302       community
         10        community
 20      105       isolated
 100     151       non-operational
 none    202       community
         303       community
 101     402       non-operational

    '''
}
    golden_parsed_output_vlan_1 = {
        'vlans':{
            '1':{
                'vlan_id': '1',
                'name': 'default',
                'state': 'active',
                'shutdown': False,
                'mtu': 1500,
                'said': 100001,
                'trans1': 0,
                'trans2': 0,
                'type': 'enet',
                'interfaces': ['GigabitEthernet1/0/1', 'GigabitEthernet1/0/2', 'GigabitEthernet1/0/3',
                               'GigabitEthernet1/0/5', 'GigabitEthernet1/0/6', 'GigabitEthernet1/0/12',
                               'GigabitEthernet1/0/13', 'GigabitEthernet1/0/14', 'GigabitEthernet1/0/15',
                               'GigabitEthernet1/0/16', 'GigabitEthernet1/0/17', 'GigabitEthernet1/0/18',
                               'GigabitEthernet1/0/19', 'GigabitEthernet1/0/20', 'GigabitEthernet1/0/21',
                               'GigabitEthernet1/0/22']
                },
            '2': {
                'vlan_id': '2',
                'name': 'VLAN0002',
                'state': 'active',
                'shutdown': False,
                'private_vlan':{
                    'primary': True,
                    'association': ['301', '302'],
                    },
                },
            '301': {
                'private_vlan': {
                    'primary': False,
                    'type': 'community',
                    'ports': ['FastEthernet5/3', 'FastEthernet5/25']
                    }
                },
            '302': {
                'private_vlan': {
                    'primary': False,
                    'type': 'community',
                    }
                },
            '10': {
                'private_vlan': {
                    'primary': False,
                    'type': 'community',
                    },
                },
            '20': {
                'vlan_id': '20',
                'name': 'VLAN0020',
                'shutdown': False,
                'state': 'active',
                'remote_span_vlan':True,
                'private_vlan': {
                    'primary': True,
                    'association': ['105'],
                    },
                },
            '21': {'remote_span_vlan': True},
            '24': {'remote_span_vlan': True},
            '25': {'remote_span_vlan': True},
            '26': {'remote_span_vlan': True},
            '27': {'remote_span_vlan': True},

            '105': {
                'private_vlan': {
                    'primary': False,
                    'type': 'isolated',
                    },
                },
            '100': {
                'vlan_id': '100',
                'name': 'V100',
                'state': 'suspend',
                'shutdown': False,
                'mtu': 1500,
                'said': 100100,
                'trans1': 0,
                'trans2': 0,
                'type': 'enet',
                'private_vlan': {
                    'primary': True,
                    'association': ['151'],
                    },
                },
            '151': {
                'private_vlan': {
                    'primary': False,
                    'type': 'non-operational',
                    },
                },
            '202': {
                'private_vlan': {
                    'primary': False,
                    'type': 'community',
                    },
                },
            '303': {
                'private_vlan': {
                    'primary': False,
                    'type': 'community',
                    },
                },
            '101': {
                'vlan_id': '101',
                'shutdown': False,
                'name': 'VLAN0101',
                'state': 'active',
                'mtu': 1500,
                'said': 100101,
                'trans1': 0,
                'trans2': 0,
                'type': 'enet',
                'private_vlan': {
                    'primary': True,
                    'association': ['402'],
                    },
                },
            '402': {
                'private_vlan': {
                    'primary': False,
                    'type': 'non-operational',
                    },
                },
            '102': {
                'vlan_id': '102',
                'shutdown': False,
                'name': 'VLAN0102',
                'state': 'active',
                'remote_span_vlan': True,
                },
            '103': {
                'vlan_id': '103',
                'shutdown': False,
                'name': 'VLAN0103',
                'state': 'active',
                },
            '104': {
                'vlan_id': '104',
                'name': 'VLAN0104',
                'state': 'shutdown',
                'shutdown': True,
            },
        },
    }

    golden_output_vlan_2 = {'execute.return_value': '''
VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Gi1/0/1, Gi1/0/2, Gi1/0/3, Gi1/0/5, Gi1/0/6, Gi1/0/12, Gi1/0/13, Gi1/0/14, Gi1/0/15, Gi1/0/16, Gi1/0/17, Gi1/0/18
                                                Gi1/0/19, Gi1/0/20, Gi1/0/21, Gi1/0/22
2    VLAN_0002                        active
20   VLAN-0020                        active
100  V100                             suspended
101  VLAN-0101                        active
102  VLAN_0102                        active
103  VLAN-0103                        act/unsup
104  VLAN_0104                        act/lshut

VLAN Type  SAID       MTU   Parent RingNo BridgeNo Stp  BrdgMode Trans1 Trans2
---- ----- ---------- ----- ------ ------ -------- ---- -------- ------ ------
1    enet  100001     1500  -      -      -        -    -        0      0
100  enet  100100     1500  -      -      -        -    -        0      0
101  enet  100101     1500  -      -      -        -    -        0      0


Remote SPAN VLANs
------------------------------------------------------------------------------
20,21,102,24-27

Primary Secondary Type              Ports
------- --------- ----------------- ------------------------------------------
2       301       community         Fa5/3, Fa5/25
2       302       community
        10        community
20      105       isolated
100     151       non-operational
none    202       community
        303       community
101     402       non-operational

'''
    }
    golden_parsed_output_vlan_2 = {
        'vlans':{
            '1':{
                'vlan_id': '1',
                'name': 'default',
                'state': 'active',
                'shutdown': False,
                'mtu': 1500,
                'said': 100001,
                'trans1': 0,
                'trans2': 0,
                'type': 'enet',
                'interfaces': ['GigabitEthernet1/0/1', 'GigabitEthernet1/0/2', 'GigabitEthernet1/0/3',
                               'GigabitEthernet1/0/5', 'GigabitEthernet1/0/6', 'GigabitEthernet1/0/12',
                               'GigabitEthernet1/0/13', 'GigabitEthernet1/0/14', 'GigabitEthernet1/0/15',
                               'GigabitEthernet1/0/16', 'GigabitEthernet1/0/17', 'GigabitEthernet1/0/18',
                               'GigabitEthernet1/0/19', 'GigabitEthernet1/0/20', 'GigabitEthernet1/0/21',
                               'GigabitEthernet1/0/22']
                },
            '2': {
                'vlan_id': '2',
                'name': 'VLAN_0002',
                'state': 'active',
                'shutdown': False,
                'private_vlan':{
                    'primary': True,
                    'association': ['301', '302'],
                    },
                },
            '301': {
                'private_vlan': {
                    'primary': False,
                    'type': 'community',
                    'ports': ['FastEthernet5/3', 'FastEthernet5/25']
                    }
                },
            '302': {
                'private_vlan': {
                    'primary': False,
                    'type': 'community',
                    }
                },
            '10': {
                'private_vlan': {
                    'primary': False,
                    'type': 'community',
                    },
                },
            '20': {
                'vlan_id': '20',
                'name': 'VLAN-0020',
                'shutdown': False,
                'state': 'active',
                'remote_span_vlan':True,
                'private_vlan': {
                    'primary': True,
                    'association': ['105'],
                    },
                },
            '21': {'remote_span_vlan': True},
            '24': {'remote_span_vlan': True},
            '25': {'remote_span_vlan': True},
            '26': {'remote_span_vlan': True},
            '27': {'remote_span_vlan': True},

            '105': {
                'private_vlan': {
                    'primary': False,
                    'type': 'isolated',
                    },
                },
            '100': {
                'vlan_id': '100',
                'name': 'V100',
                'state': 'suspend',
                'shutdown': False,
                'mtu': 1500,
                'said': 100100,
                'trans1': 0,
                'trans2': 0,
                'type': 'enet',
                'private_vlan': {
                    'primary': True,
                    'association': ['151'],
                    },
                },
            '151': {
                'private_vlan': {
                    'primary': False,
                    'type': 'non-operational',
                    },
                },
            '202': {
                'private_vlan': {
                    'primary': False,
                    'type': 'community',
                    },
                },
            '303': {
                'private_vlan': {
                    'primary': False,
                    'type': 'community',
                    },
                },
            '101': {
                'vlan_id': '101',
                'shutdown': False,
                'name': 'VLAN-0101',
                'state': 'active',
                'mtu': 1500,
                'said': 100101,
                'trans1': 0,
                'trans2': 0,
                'type': 'enet',
                'private_vlan': {
                    'primary': True,
                    'association': ['402'],
                    },
                },
            '402': {
                'private_vlan': {
                    'primary': False,
                    'type': 'non-operational',
                    },
                },
            '102': {
                'vlan_id': '102',
                'shutdown': False,
                'name': 'VLAN_0102',
                'state': 'active',
                'remote_span_vlan': True,
                },
            '103': {
                'vlan_id': '103',
                'shutdown': False,
                'name': 'VLAN-0103',
                'state': 'unsupport',
                },
            '104': {
                'vlan_id': '104',
                'name': 'VLAN_0104',
                'state': 'shutdown',
                'shutdown': True,
            },
        },
    }
    def test_empty_1(self):
        self.device = Mock(**self.empty_output)
        obj = ShowVlan(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


    def test_show_vlan_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_vlan_1)
        obj = ShowVlan(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_vlan_1)

    def test_show_vlan_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_vlan_2)
        obj = ShowVlan(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_vlan_2)

###########################################################################
#
# parsers with old schema may in feature we need to delete or improve them
#
###########################################################################

class test_show_vlan_mtu(unittest.TestCase):
    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {'vlan_id': 
                            {'200': 
                                {'vlan_min_mtu': '1500', 'vlan_max_mtu': '1500', 'mtu_mismatch': 'No', 'vlan_mtu': '-'}, 
                             '1005': 
                                {'vlan_min_mtu': '1500', 'vlan_max_mtu': '1500', 'mtu_mismatch': 'No', 'vlan_mtu': '-'}, 
                             '1003': 
                                {'vlan_min_mtu': '1500', 'vlan_max_mtu': '1500', 'mtu_mismatch': 'No', 'vlan_mtu': '-'}, 
                             '300': 
                                {'vlan_min_mtu': '1500', 'vlan_max_mtu': '1500', 'mtu_mismatch': 'No', 'vlan_mtu': '-'}, 
                             '1002': 
                                {'vlan_min_mtu': '1500', 'vlan_max_mtu': '1500', 'mtu_mismatch': 'No', 'vlan_mtu': '-'}, 
                             '1004': 
                                {'vlan_min_mtu': '1500', 'vlan_max_mtu': '1500', 'mtu_mismatch': 'No', 'vlan_mtu': '-'}, 
                             '100': 
                                {'vlan_min_mtu': '1500', 'vlan_max_mtu': '1500', 'mtu_mismatch': 'No', 'vlan_mtu': '1500'}, 
                             '1': 
                                {'vlan_min_mtu': '1500', 'vlan_max_mtu': '1500', 'mtu_mismatch': 'No', 'vlan_mtu': '1500'}
                            }
                        }

    golden_output = {'execute.return_value': '''
 VLAN    SVI_MTU    MinMTU(port)      MaxMTU(port)     MTU_Mismatch
 ---- ------------- ----------------  ---------------  ------------
 1    1500          1500              1500              No
 100  1500          1500              1500              No
 200    -           1500              1500              No
 300    -           1500              1500              No
 1002   -           1500              1500              No
 1003   -           1500              1500              No
 1004   -           1500              1500              No
 1005   -           1500              1500              No
'''}

    silver_output = {'execute.return_value': '''
 VLAN    SVI_MTU    MinMTU(port)      MTU_Mismatch
 ---- ------------- ----------------  ------------
 1    1500          1500              No
 100  1500          1500              No
 200    -           1500              No
 300    -           1500              No
 1002   -           1500              No
 1003   -           1500              No
 1004   -           1500              No
 1005   -           1500              No
'''}

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        vlan_obj = ShowVlanMtu(device=self.device)
        parsed_output = vlan_obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        vlan_obj = ShowVlanMtu(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = vlan_obj.parse()

    def test_missing_parsed_key(self):
        self.device = Mock(**self.silver_output)
        vlan_obj = ShowVlanMtu(device=self.device)
        with self.assertRaises(Exception):
            parsed_output = vlan_obj.parse()

class test_show_vlan_remote_span(unittest.TestCase):
    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {'vlan_id': 
                            {'400': 
                                {'vlan_is_remote_span': True}, 
                             '500': 
                                {'vlan_is_remote_span': True}, 
                             '100': 
                                {'vlan_is_remote_span': True}
                            }
                        }

    golden_output = {'execute.return_value': '''
 Remote SPAN VLANs
 ------------------------------------------------------------------------------
 100,400,500
'''}

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        vlan_obj = ShowVlanRemoteSpan(device=self.device)
        parsed_output = vlan_obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        vlan_obj = ShowVlanRemoteSpan(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = vlan_obj.parse()

class test_show_vlan_access_map(unittest.TestCase):
    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {'access_map_id': 
    {'vlan': 
        {'access_map_sequence': 
            {'10': {'access_map_action_value': 'forward'}}}, 
     'fg': 
        {'access_map_sequence': 
            {'10': {'access_map_action_value': 'forward'}}}, 
     'kari3': 
        {'access_map_sequence': 
            {'10': {'access_map_action_value': 'forward'}}}, 
     'ed': 
        {'access_map_sequence': 
            {'20': {'access_map_action_value': 'drop'}}}, 
     'takashi': 
        {'access_map_sequence': 
            {'10': {'access_map_action_value': 'drop'}}}, 
     'karim': 
        {'access_map_sequence': 
            {'10': {'access_map_action_value': 'forward'}}}, 
     'mordred': 
        {'access_map_sequence': 
            {'10': {'access_map_action_value': 'forward'}}
        }
    }
}

    golden_output = {'execute.return_value': '''
Vlan access-map "ed"  20
  Match clauses:
  Action:
    drop
Vlan access-map "fg"  10
  Match clauses:
  Action:
    forward
Vlan access-map "takashi"  10
  Match clauses:
  Action:
    drop
Vlan access-map "mordred"  10
  Match clauses:
  Action:
    forward
Vlan access-map "karim"  10
  Match clauses:
  Action:
    forward
Vlan access-map "vlan"  10
  Match clauses:
  Action:
    forward
Vlan access-map "kari3"  10
  Match clauses:
  Action:
    forward
'''}

    silver_output = {'execute.return_value': '''
Vlan access-map "ed"  20
  Match clauses:
  Action:
    drop
Vlan access-map "fg"  10
  Match clauses:
  Action:
    forward
Vlan access-map "takashi"  10
  Match clauses:
  Action:
    drop
Vlan access-map "mordred"  10
  Match clauses:
  Action:
    forward
Vlan access-map "karim"  10
  Match clauses:
  Action:
    forward
Vlan access-map "vlan"  10
  Match clauses:
  Action:
    forward
Vlan access-map "kari3"  10
  Match clauses:
  Action:
    forward
'''}

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        vlan_obj = ShowVlanAccessMap(device=self.device)
        parsed_output = vlan_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        vlan_obj = ShowVlanAccessMap(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = vlan_obj.parse()

class test_show_vlan_filter(unittest.TestCase):
    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {'vlan_id': 
                                {'100': 
                                    {'access_map_tag': 'karim'}, 
                                 '3': 
                                    {'access_map_tag': 'mordred'}, 
                                 '15': 
                                    {'access_map_tag': 'mordred'}, 
                                 '5': 
                                    {'access_map_tag': 'mordred'}
                                }
                            }

    golden_output = {'execute.return_value': '''
 VLAN Map mordred is filtering VLANs:
   3-5,15
 VLAN Map karim is filtering VLANs:
   100
'''}

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        vlan_obj = ShowVlanFilter(device=self.device)
        parsed_output = vlan_obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        vlan_obj = ShowVlanFilter(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = vlan_obj.parse()

###########################################################################
#
# old parsers
#
###########################################################################
if __name__ == '__main__':
    unittest.main()