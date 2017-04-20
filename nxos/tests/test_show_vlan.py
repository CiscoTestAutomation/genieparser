import re
import unittest
from unittest.mock import Mock

from ats.topology import Device

from metaparser.util.exceptions import SchemaEmptyParserError

from xbu_shared.parser.nxos.show_vlan import ShowVlan, \
                                             ShowVlanInternalInfo, \
                                             ShowVlanFilter, \
                                             ShowVlanAccessMap


class test_show_vlan(unittest.TestCase):
    device = Device(name='aDevice')
    device1 = Device(name='bDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {'vlan_id': 
                                {'108': 
                                    {'vl_mode': 'CE', 'status': 'active', 'name': 'VLAN0108', 'ports': None, 'vlan_type': 'enet'}, 
                                 '105': 
                                    {'vl_mode': 'CE', 'status': 'active', 'name': 'VLAN0105', 'ports': None, 'vlan_type': 'enet'}, 
                                 '110': 
                                    {'vl_mode': 'CE', 'status': 'active', 'name': 'VLAN0110', 'ports': None, 'vlan_type': 'enet'}, 
                                 '100': 
                                    {'vl_mode': 'CE', 'status': 'active', 'name': 'VLAN0100', 'ports': None, 'vlan_type': 'enet'}, 
                                 '101': 
                                    {'vl_mode': 'CE', 'status': 'active', 'name': 'VLAN0101', 'ports': None, 'vlan_type': 'enet'}, 
                                 '1': 
                                    {'vl_mode': 'CE', 'status': 'active', 'name': 'default', 'ports': 'Eth3/1, Eth3/2, Eth3/3, Eth3/4, Eth3/5, Eth3/6, Eth3/7, Eth3/8, Eth3/9, Eth3/10, Eth3/11, Eth3/12, Eth3/13, Eth3/14, Eth3/15, Eth3/16, Eth3/17, Eth3/18, Eth3/19, Eth3/20, Eth3/21, Eth3/22, Eth3/23, Eth3/24, Eth3/25, Eth3/26, Eth3/27, Eth3/28, Eth3/29, Eth3/30, Eth3/31, Eth3/32, Eth3/33, Eth3/34, Eth3/35, Eth3/36, Eth3/37, Eth3/38, Eth3/39, Eth3/40, Eth3/41, Eth3/42, Eth3/43, Eth3/44, Eth3/45, Eth3/46, Eth3/47, Eth3/48', 'vlan_type': 'enet'}, 
                                 '103': 
                                    {'vl_mode': 'CE', 'status': 'active', 'name': 'VLAN0103', 'ports': None, 'vlan_type': 'enet'}, 
                                 '102': 
                                    {'vl_mode': 'CE', 'status': 'active', 'name': 'VLAN0102', 'ports': None, 'vlan_type': 'enet'}, 
                                 '23': 
                                    {'vl_mode': 'CE', 'status': 'active', 'name': 'VLAN0023', 'ports': 'Eth6/24', 'vlan_type': 'enet'}, 
                                 '109': 
                                    {'vl_mode': 'CE', 'status': 'active', 'name': 'VLAN0109', 'ports': None, 'vlan_type': 'enet'}, 
                                 '106': 
                                    {'vl_mode': 'CE', 'status': 'active', 'name': 'VLAN0106', 'ports': None, 'vlan_type': 'enet'}, 
                                 '104': 
                                    {'vl_mode': 'CE', 'status': 'active', 'name': 'VLAN0104', 'ports': None, 'vlan_type': 'enet'}, 
                                 '107': 
                                    {'vl_mode': 'CE', 'status': 'active', 'name': 'VLAN0107', 'ports': None, 'vlan_type': 'enet'}
                                }
                            }

    golden_output = {'execute.return_value': '''
 VLAN Name                             Status    Ports
 ---- -------------------------------- --------- -------------------------------
 1    default                          active    Eth3/1, Eth3/2, Eth3/3, Eth3/4
                                                 Eth3/5, Eth3/6, Eth3/7, Eth3/8
                                                 Eth3/9, Eth3/10, Eth3/11
                                                 Eth3/12, Eth3/13, Eth3/14
                                                 Eth3/15, Eth3/16, Eth3/17
                                                 Eth3/18, Eth3/19, Eth3/20
                                                 Eth3/21, Eth3/22, Eth3/23
                                                 Eth3/24, Eth3/25, Eth3/26
                                                 Eth3/27, Eth3/28, Eth3/29
                                                 Eth3/30, Eth3/31, Eth3/32
                                                 Eth3/33, Eth3/34, Eth3/35
                                                 Eth3/36, Eth3/37, Eth3/38
                                                 Eth3/39, Eth3/40, Eth3/41
                                                 Eth3/42, Eth3/43, Eth3/44
                                                 Eth3/45, Eth3/46, Eth3/47
                                                 Eth3/48
 23   VLAN0023                         active    Eth6/24
 100  VLAN0100                         active    
 101  VLAN0101                         active    
 102  VLAN0102                         active    
 103  VLAN0103                         active    
 104  VLAN0104                         active    
 105  VLAN0105                         active    
 106  VLAN0106                         active    
 107  VLAN0107                         active    
 108  VLAN0108                         active    
 109  VLAN0109                         active    
 110  VLAN0110                         active    

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
 108  enet         CE     
 109  enet         CE     
 110  enet         CE     

 Remote SPAN VLANs
 -------------------------------------------------------------------------------

 Primary  Secondary  Type             Ports
 -------  ---------  ---------------  -------------------------------------------

'''}

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        vlan_obj = ShowVlan(device=self.device)
        parsed_output = vlan_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        vlan_obj = ShowVlan(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = vlan_obj.parse()

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

if __name__ == '__main__':
    unittest.main()