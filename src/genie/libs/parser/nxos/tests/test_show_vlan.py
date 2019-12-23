import re
import unittest
from unittest.mock import Mock

from pyats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError

from genie.libs.parser.nxos.show_vlan import ShowVlan, ShowVlanIdVnSegment, \
                                             ShowVlanInternalInfo, \
                                             ShowVlanFilter, \
                                             ShowVlanAccessMap, \
                                             ShowVxlan

# =========================================
#  show vlan
# =========================================
class test_show_vlan(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    golden_output_vlan_1 = {'execute.return_value': '''
VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Po4, Po100, Eth1/2, Eth1/3
                                                Eth1/4, Eth1/5, Eth1/6, Eth1/7
                                                Eth1/8, Eth1/9, Eth1/10, Eth1/11
                                                Eth1/12, Eth1/13, Eth1/14
                                                Eth2/1, Eth2/2, Eth2/3, Eth2/4
                                                Eth2/5, Eth2/6
2    VLAN0002                         active    Po4, Po100, Eth1/7, Eth1/8
                                                Eth1/28
3    VLAN0003                         active    Po4, Po100, Eth1/7, Eth1/8
                                                Eth1/28
4    VLAN0004                         active    Po4, Po100, Eth1/7, Eth1/8
                                                Eth1/28
5    VLAN0005                         active    Po4, Po100, Eth1/7, Eth1/8
                                                Eth1/28
6    VLAN0006                         sus/lshut

VLAN Type         Vlan-mode
 ---- -----        ----------
 1    enet         CE
 23   enet         CE
 100  enet         CE
 101  enet         CE
 102  enet         CE
 103  enet         CE
 104  enet         CE
 105  enet         CE
 106  enet         CE
 107  enet         CE

Remote SPAN VLANs
-------------------------------------------------------------------------------
10,20,30-33

Primary  Secondary  Type             Ports
-------  ---------  ---------------  -------------------------------------------
         303        community        Fa2/3, Fa3/5
403      500        non-operational
  '''}

    golden_parsed_output_vlan_1 = {
        'vlans':{
            '1':{
                'vlan_id': '1',
                'name': 'default',
                'state': 'active',
                'shutdown': False,
                'interfaces': ['Port-channel4', 'Port-channel100', 'Ethernet1/2',
                               'Ethernet1/3', 'Ethernet1/4', 'Ethernet1/5',
                               'Ethernet1/6', 'Ethernet1/7', 'Ethernet1/8',
                               'Ethernet1/9', 'Ethernet1/10', 'Ethernet1/11',
                               'Ethernet1/12', 'Ethernet1/13', 'Ethernet1/14',
                               'Ethernet2/1','Ethernet2/2','Ethernet2/3','Ethernet2/4',
                               'Ethernet2/5','Ethernet2/6'],
                'mode': 'ce',
                'type': 'enet',
                },
            '2': {
                'vlan_id': '2',
                'name': 'VLAN0002',
                'state': 'active',
                'shutdown': False,
                'interfaces': ['Port-channel4', 'Port-channel100', 'Ethernet1/7',
                               'Ethernet1/8','Ethernet1/28']
                },
            '3': {
                'vlan_id': '3',
                'name': 'VLAN0003',
                'state': 'active',
                'shutdown': False,
                'interfaces': ['Port-channel4', 'Port-channel100', 'Ethernet1/7',
                               'Ethernet1/8', 'Ethernet1/28']
                },
            '4': {
                'vlan_id': '4',
                'name': 'VLAN0004',
                'state': 'active',
                'shutdown': False,
                'interfaces': ['Port-channel4', 'Port-channel100', 'Ethernet1/7',
                               'Ethernet1/8', 'Ethernet1/28']
                },
            '5': {
                'vlan_id': '5',
                'name': 'VLAN0005',
                'state': 'active',
                'shutdown': False,
                'interfaces': ['Port-channel4', 'Port-channel100', 'Ethernet1/7',
                               'Ethernet1/8', 'Ethernet1/28']
                },
            '6': {
                'vlan_id': '6',
                'name': 'VLAN0006',
                'state': 'shutdown',
                'shutdown': True,
            },
            '10': {'remote_span_vlan': True},
            '20': {'remote_span_vlan': True},
            '30': {'remote_span_vlan': True},
            '31': {'remote_span_vlan': True},
            '32': {'remote_span_vlan': True},
            '33': {'remote_span_vlan': True},
            '303': {
                'private_vlan': {
                    'primary': False,
                    'type': 'community',
                    'ports': ['FastEthernet2/3', 'FastEthernet3/5']
                    },
                },
            '500': {
                'private_vlan': {
                    'primary': False,
                    'type': 'non-operational',
                    },
                },
            '403': {
                'private_vlan': {
                    'primary': True,
                    'association': ['500'],
                },
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
        self.assertEqual(parsed_output, self.golden_parsed_output_vlan_1)


class test_show_vlan_id_segmant(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_output_vlan_1 = {'execute.return_value': '''
    best-n6k-pe1# show vlan id 1-4093 vn-segment

    VLAN Segment-id
    ---- -----------
    10   5010
    20   5020
    30   5030
    40   5040
    50   5050
    555  5555
    556  5556
        '''}
    golden_parsed_output_vlan_1 = {
        'vlans':{
            '10':{
                'vlan_id': '10',
                'vn_segment_id': 5010,
                },
            '20': {
                'vlan_id': '20',
                'vn_segment_id': 5020,
            },
            '30': {
                'vlan_id': '30',
                'vn_segment_id': 5030,
            },
            '40': {
                'vlan_id': '40',
                'vn_segment_id': 5040,
            },
            '50': {
                'vlan_id': '50',
                'vn_segment_id': 5050,
            },
            '555': {
                'vlan_id': '555',
                'vn_segment_id': 5555,
            },
            '556': {
                'vlan_id': '556',
                'vn_segment_id': 5556,
            },

        },
    }

    def test_empty_1(self):
        self.device = Mock(**self.empty_output)
        obj = ShowVlanIdVnSegment(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_vlan_segmant_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_vlan_1)
        obj = ShowVlanIdVnSegment(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_vlan_1)


class test_show_vlan_internal_info(unittest.TestCase):
    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {'vlan_id': 
                            {'3': 
                                {'vlan_configuration': True}, 
                             '8': 
                                {'vlan_configuration': True}, 
                             '5': 
                                {'vlan_configuration': True}
                            }
                        }

    golden_output = {'execute.return_value': '''
 
 VLAN_INFO_GLOBAL
 
 Build date: Feb 10 2017 05:12:28
 
 vlan-mgr MTS appcode: 23
 
 Global Lock(1) NOT Locked
 Is VTP Reserved VLANs Present: No
 vdc_info_db.requester_sap 0
 PVLAN fex trunk knob - FEX_TRUNK_KNOB_INVALID
 All PVLANs in system - 
 
 Write to file Variable           : -1
 Log Trace to file Variable       : 0
 Log Errors to file Variable      : 0
 Log debug pss to file Variable   : 0
 Log debug db to file Variable    : 0
 Log debug vpc to file Variable   : 0
 Per VLAN Details
 
 ================
 
 vlan configuration 3-5,8
 VLAN configmode operation in progress flag 0
 config pss uri volatile:/dev/shm/vlan_mgr_config
 saved config pss uri readonly:/var/sysmgr/startup-cfg/bin/vlan_mgr_config
 vlan_mgr_init_done flag 1
 long vlan name knob 0(in gsdb 0)
 
 Entry No: 0
 ------------
   vlan id 1
   vdc 1 bd_id = 1, bd_id_orig = 1, vlan_type = USER_VLAN(1)
   sdb_vlan_type USER_VLAN(1, err 0x0), oper =down
   vlan_state = active, vlan_oper = down,  sdb_oper_state unknown(0, err 0x0)
   oper up technologies:   oper down technologies:  configured technologies:  
   vlan_shut_state = no-shutdown, vlan_modes = (0)ce
   sdb_vlan_mode 0(ce, err 0x0), n_access_ports 0, n_native_ports 0
   mtu = 1500, internal_state = 0, cfg_flags 0 
  vlan_name = default  segment_id = 0(err 0x0, sdb 0) 
 
'''}

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        vlan_obj = ShowVlanInternalInfo(device=self.device)
        parsed_output = vlan_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        vlan_obj = ShowVlanInternalInfo(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = vlan_obj.parse()

class test_show_vlan_Filter(unittest.TestCase):
    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {'vlan_id': 
    {'3': 
        {'access_map_tag': 'ed'}, 
     '402': 
        {'access_map_tag': 'ed'}
    }
}

    golden_output = {'execute.return_value': '''
 
vlan map ed:
        Configured on VLANs:    3,402

'''}

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        vlan_obj = ShowVlanFilter(device=self.device)
        parsed_output = vlan_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        vlan_obj = ShowVlanFilter(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = vlan_obj.parse()

class test_show_vlan_Access_Map(unittest.TestCase):
    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {'access_map_id': 
            {'ed': 
                {'access_map_sequence': 
                    {'10': 
                        {'access_map_action_value': 'forward', 'access_map_match_protocol_value': 'foo', 'access_map_match_protocol': 'ip'}
                    }
                }
            }
        }

    golden_output = {'execute.return_value': '''

Vlan access-map ed 10
        match ip: foo 
        action: forward 


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

class test_show_vxlan(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
      'vlan':
        {'100': {'vni': '8100'},
         '1000': {'vni': '9100'},
         '1005': {'vni': '9105'},
         '1006': {'vni': '9106'},
         '1007': {'vni': '9107'},
         '1008': {'vni': '9108'},
         '1009': {'vni': '9109'},
         '101': {'vni': '8101'},
         '103': {'vni': '8103'},
         '105': {'vni': '8105'},
         '106': {'vni': '8106'},
         '107': {'vni': '8107'},
         '108': {'vni': '8108'},
         '109': {'vni': '8109'},
         '110': {'vni': '8110'},
         '111': {'vni': '8111'},
         '112': {'vni': '8112'},
         '113': {'vni': '8113'},
         '114': {'vni': '8114'}
        }
      }

    golden_output = {'execute.return_value': '''
        N95_1# show vxlan 
        Vlan            VN-Segment
        ====            ==========
        100             8100
        101             8101
        103             8103
        105             8105
        106             8106
        107             8107
        108             8108
        109             8109
        110             8110
        111             8111
        112             8112
        113             8113
        114             8114
        1000            9100
        1005            9105
        1006            9106
        1007            9107
        1008            9108
        1009            9109
    '''}

    def test_show_vxlan_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowVxlan(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_show_vxlan_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowVxlan(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

if __name__ == '__main__':
    unittest.main()