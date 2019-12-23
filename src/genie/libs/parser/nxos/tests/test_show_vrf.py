
# Python
import re
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Parser
from genie.libs.parser.nxos.show_vrf import ShowVrf, ShowVrfInterface, \
                                 ShowVrfDetail, ShowRunningConfigVrf

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

 
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


# =======================================
#  Unit test for 'show vrf <WORD> detail'
# =======================================
class test_show_vrf_detail(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        "management": {
              "max_routes": 0,
              "state": "up",
              "vrf_id": 2,
              "address_family": {
                   "ipv6": {
                        "table_id": "0x80000002",
                        "state": "up",
                        "fwd_id": "0x80000002"
                   },
                   "ipv4": {
                        "table_id": "0x00000002",
                        "state": "up",
                        "fwd_id": "0x00000002"
                   }
              },
              "mid_threshold": 0,
              "route_distinguisher": "0:0"
         },
         "default": {
              "max_routes": 0,
              "state": "up",
              "vrf_id": 1,
              "address_family": {
                   "ipv6": {
                        "table_id": "0x80000001",
                        "state": "up",
                        "fwd_id": "0x80000001"
                   },
                   "ipv4": {
                        "table_id": "0x00000001",
                        "state": "up",
                        "fwd_id": "0x00000001"
                   }
              },
              "mid_threshold": 0,
              "route_distinguisher": "0:0"
         },
         "VRF2": {
              "max_routes": 0,
              "state": "up",
              "vrf_id": 4,
              "address_family": {
                   "ipv6": {
                        "table_id": "0x80000004",
                        "state": "up",
                        "fwd_id": "0x80000004"
                   },
                   "ipv4": {
                        "table_id": "0x00000004",
                        "state": "up",
                        "fwd_id": "0x00000004"
                   }
              },
              "mid_threshold": 0,
              "route_distinguisher": "400:1"
         },
         "VRF1": {
              "max_routes": 20000,
              "state": "up",
              "vrf_id": 3,
              "address_family": {
                   "ipv6": {
                        "table_id": "0x80000003",
                        "state": "up",
                        "fwd_id": "0x80000003"
                   },
                   "ipv4": {
                        "table_id": "0x00000003",
                        "state": "up",
                        "fwd_id": "0x00000003"
                   }
              },
              "mid_threshold": 17000,
              "route_distinguisher": "300:1"
         }
    }

    golden_output = {'execute.return_value': '''
        VRF-Name: VRF1, VRF-ID: 3, State: Up
            VPNID: unknown
            RD: 300:1
            Max Routes: 20000  Mid-Threshold: 17000
            Table-ID: 0x80000003, AF: IPv6, Fwd-ID: 0x80000003, State: Up
            Table-ID: 0x00000003, AF: IPv4, Fwd-ID: 0x00000003, State: Up

        VRF-Name: VRF2, VRF-ID: 4, State: Up
            VPNID: unknown
            RD: 400:1
            Max Routes: 0  Mid-Threshold: 0
            Table-ID: 0x80000004, AF: IPv6, Fwd-ID: 0x80000004, State: Up
            Table-ID: 0x00000004, AF: IPv4, Fwd-ID: 0x00000004, State: Up

        VRF-Name: default, VRF-ID: 1, State: Up
            VPNID: unknown
            RD: 0:0
            Max Routes: 0  Mid-Threshold: 0
            Table-ID: 0x80000001, AF: IPv6, Fwd-ID: 0x80000001, State: Up
            Table-ID: 0x00000001, AF: IPv4, Fwd-ID: 0x00000001, State: Up

        VRF-Name: management, VRF-ID: 2, State: Up
            VPNID: unknown
            RD: 0:0
            Max Routes: 0  Mid-Threshold: 0
            Table-ID: 0x80000002, AF: IPv6, Fwd-ID: 0x80000002, State: Up
            Table-ID: 0x00000002, AF: IPv4, Fwd-ID: 0x00000002, State: Up
        '''}

    golden_parsed_output_1 = {
         "VRF1": {
              "max_routes": 20000,
              "state": "up",
              "vrf_id": 3,
              "address_family": {
                   "ipv6": {
                        "table_id": "0x80000003",
                        "state": "up",
                        "fwd_id": "0x80000003"
                   },
                   "ipv4": {
                        "table_id": "0x00000003",
                        "state": "up",
                        "fwd_id": "0x00000003"
                   }
              },
              "mid_threshold": 17000,
              "route_distinguisher": "300:1"
         }}

    golden_output_1 = {'execute.return_value': '''
        VRF-Name: VRF1, VRF-ID: 3, State: Up
            VPNID: unknown
            RD: 300:1
            Max Routes: 20000  Mid-Threshold: 17000
            Table-ID: 0x80000003, AF: IPv6, Fwd-ID: 0x80000003, State: Up
            Table-ID: 0x00000003, AF: IPv4, Fwd-ID: 0x00000003, State: Up
        '''}

    def test_show_vrf_all(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowVrfDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_show_vrf_word(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowVrfDetail(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output,self.golden_parsed_output_1)

    def test_show_vrf_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowVrfDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

# ===============================================================
#  Unit test for 'show running-config vrf <vrf> | sec '^vrf'"
# ==========================================================
class test_show_running_config_vrf(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'vrf': {
            'vni_10100': {
                'vni': 10100,
                'rd': 'auto',
                'address_family': {
                    'ipv4 unicast': {
                        'route_target': {
                            'auto': {
                                'rt_type': 'both',
                                 'protocol': {
                                     'mvpn': {
                                         'rt': 'auto',
                                         'rt_type': 'both',
                                         'rt_mvpn': True,
                                     },
                                     'evpn': {
                                         'rt': 'auto',
                                         'rt_type': 'both',
                                         'rt_evpn': True,
                                     }
                                 }
                            },
                        }
                    },
                    'ipv6 unicast': {
                        'route_target': {
                            'auto': {
                                'rt_type': 'both',
                                'protocol': {
                                    'evpn': {
                                        'rt': 'auto',
                                        'rt_type': 'both',
                                        'rt_evpn': True,
                                    }
                                }
                            },
                        }
                    }
                }
            }
        },
    }

    golden_output = {'execute.return_value': '''
R2# show running-config vrf vni_10100 | sec '^vrf'
vrf context vni_10100
  vni 10100
  rd auto
  address-family ipv4 unicast
    route-target both auto
    route-target both auto mvpn
    route-target both auto evpn
  address-family ipv6 unicast
    route-target both auto
    route-target both auto evpn
        '''}

    def test_show_running_config_vrf(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowRunningConfigVrf(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


    def test_show_vrf_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowRunningConfigVrf(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


if __name__ == '__main__':
    unittest.main()


# vim: ft=python et sw=4
