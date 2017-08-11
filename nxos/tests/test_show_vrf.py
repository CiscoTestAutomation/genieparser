
# Python
import re
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Parser
from parser.nxos.show_vrf import ShowVrf, ShowVrfInterface

# Metaparser
from metaparser.util.exceptions import SchemaEmptyParserError

 
# =========================
#  Unit test for 'show vrf'
# =========================

class test_show_vrf(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'vrfs':
            {'VRF':
                {'reason': '--',
                'vrf_id': 5,
                'vrf_state': 'Up'},
            'VRF1':
                {'reason': '--',
                'vrf_id': 3,
                'vrf_state': 'Up'},
            'VRF2':
                {'reason': '--',
                'vrf_id': 4,
                'vrf_state': 'Up'},
            'default':
                {'reason': '--',
                'vrf_id': 1,
                'vrf_state': 'Up'},
            'management':
                {'reason': '--',
                'vrf_id': 2,
                'vrf_state': 'Up'}}}

    golden_output = {'execute.return_value': '''
        N7k# show vrf
        VRF-Name                           VRF-ID State   Reason                        
        VRF                                     5 Up      --                            
        VRF1                                    3 Up      --                            
        VRF2                                    4 Up      --                            
        default                                 1 Up      --                            
        management                              2 Up      --
        '''}

    def test_show_vrf_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowVrf(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


    def test_show_vrf_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowVrf(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


class test_show_vrf_interface(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {'vrf_interface': 
                              {'Ethernet1/1': {'site_of_origin': '--',
                                               'vrf_id': '1',
                                               'vrf_name': 'default'},
                               'Ethernet1/2': {'site_of_origin': '--',
                                               'vrf_id': '1',
                                               'vrf_name': 'default'},
                               'Null0': {'site_of_origin': '--',
                                         'vrf_id': '1',
                                         'vrf_name': 'default'},
                               'loopback0': {'site_of_origin': '--',
                                             'vrf_id': '1',
                                             'vrf_name': 'default'},
                               'mgmt0': {'site_of_origin': '--',
                                         'vrf_id': '2',
                                         'vrf_name': 'management'}}}

    golden_output = {'execute.return_value': '''
        pinxdt-n9kv-3# show vrf interface
        Interface                 VRF-Name                        VRF-ID  Site-of-Origin
        loopback0                 default                              1  --
        Null0                     default                              1  --
        Ethernet1/1               default                              1  --
        Ethernet1/2               default                              1  --
        mgmt0                     management                           2  --
        '''}

    def test_show_vrf_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowVrfInterface(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_show_vrf_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowVrfInterface(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


if __name__ == '__main__':
    unittest.main()


# vim: ft=python et sw=4
