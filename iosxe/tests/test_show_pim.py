# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparset
from metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

# Parser
from parser.iosxe.show_pim import ShowIpv6PimInterface, \
                                  ShowIpPimBsrRouter

# ============================================
# Parser for 'show ipv6 pim interface'
# Parser for 'show ipv6 pim vrf xxx interface'
# ============================================
class test_show_ipv6_pim_interface(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {
        "vrf": {
          "default": {
               "interface": {
                    "Tunnel4": {
                         "dr_priority": 1,
                         "neighbor_count": 0,
                         "hello_interval": 30,
                         "pim_enabled": False
                    },
                    "Null0": {
                         "address": ["FE80::1"],
                         "dr_priority": 1,
                         "neighbor_count": 0,
                         "hello_interval": 30,
                         "pim_enabled": False
                    },
                    "Loopback0": {
                         "address": ["FE80::21E:F6FF:FEAC:A600"],
                         "dr_priority": 1,
                         "neighbor_count": 0,
                         "hello_interval": 30,
                         "pim_enabled": True
                    },
                    "Tunnel3": {
                         "dr_priority": 1,
                         "neighbor_count": 0,
                         "hello_interval": 30,
                         "pim_enabled": False
                    },
                    "Tunnel1": {
                         "address": ["FE80::21E:F6FF:FEAC:A600"],
                         "dr_priority": 1,
                         "neighbor_count": 0,
                         "hello_interval": 30,
                         "pim_enabled": False
                    },
                    "GigabitEthernet1": {
                         "address": ["FE80::5054:FF:FE2C:6CDF"],
                         "dr_address": "FE80::5054:FF:FEAC:64B3",
                         "pim_enabled": True,
                         "dr_priority": 1,
                         "neighbor_count": 1,
                         "hello_interval": 30
                    },
                    "Tunnel2": {
                         "dr_priority": 1,
                         "neighbor_count": 0,
                         "hello_interval": 30,
                         "pim_enabled": False
                    },
                    "GigabitEthernet2": {
                         "address": ["FE80::5054:FF:FEBE:8787"],
                         "dr_priority": 1,
                         "neighbor_count": 0,
                         "hello_interval": 30,
                         "pim_enabled": True
                    },
                    "Tunnel0": {
                         "address": ["FE80::21E:F6FF:FEAC:A600"],
                         "dr_priority": 1,
                         "neighbor_count": 0,
                         "hello_interval": 30,
                         "pim_enabled": False
                    }}}}}

    golden_output = {'execute.return_value': '''\
        Interface          PIM   Nbr   Hello  DR
                                 Count Intvl  Prior

        GigabitEthernet1   on    1     30     1     
            Address: FE80::5054:FF:FE2C:6CDF
            DR     : FE80::5054:FF:FEAC:64B3
        GigabitEthernet2   on    0     30     1     
            Address: FE80::5054:FF:FEBE:8787
            DR     : this system
        Tunnel2            off    0     30     1     
            Address: ::
            DR     : not elected
        Tunnel1            off    0     30     1     
            Address: FE80::21E:F6FF:FEAC:A600
            DR     : not elected
        Null0              off    0     30     1     
            Address: FE80::1
            DR     : not elected
        Tunnel3            off    0     30     1     
            Address: ::
            DR     : not elected
        Tunnel4            off    0     30     1     
            Address: ::
            DR     : not elected
        Loopback0          on    0     30     1     
            Address: FE80::21E:F6FF:FEAC:A600
            DR     : this system
        Tunnel0            off    0     30     1     
            Address: FE80::21E:F6FF:FEAC:A600
            DR     : not elected
    '''}

    golden_parsed_output2 = {
        "vrf": {
            "VRF1": {
                 "interface": {
                      "Loopback1": {
                           "dr_priority": 1,
                           "neighbor_count": 0,
                           "address": [
                                "FE80::21E:F6FF:FEAC:A600"
                           ],
                           "pim_enabled": True,
                           "hello_interval": 30
                      },
                      "Tunnel6": {
                           "dr_priority": 1,
                           "neighbor_count": 0,
                           "pim_enabled": False,
                           "hello_interval": 30
                      },
                      "Tunnel5": {
                           "dr_priority": 1,
                           "neighbor_count": 0,
                           "address": [
                                "FE80::21E:F6FF:FEAC:A600"
                           ],
                           "pim_enabled": False,
                           "hello_interval": 30
                      },
                      "Tunnel7": {
                           "dr_priority": 1,
                           "neighbor_count": 0,
                           "pim_enabled": False,
                           "hello_interval": 30
                      },
                      "GigabitEthernet3": {
                           "dr_priority": 1,
                           "neighbor_count": 0,
                           "address": [
                                "FE80::5054:FF:FE84:F097"
                           ],
                           "pim_enabled": True,
                           "hello_interval": 30
                      }}}}}

    golden_output2 = {'execute.return_value': '''\
        Interface          PIM   Nbr   Hello  DR
                                 Count Intvl  Prior

        GigabitEthernet3   on    0     30     1     
            Address: FE80::5054:FF:FE84:F097
            DR     : this system
        Tunnel5            off    0     30     1     
            Address: FE80::21E:F6FF:FEAC:A600
            DR     : not elected
        Tunnel6            off    0     30     1     
            Address: ::
            DR     : not elected
        Tunnel7            off    0     30     1     
            Address: ::
            DR     : not elected
        Loopback1          on    0     30     1     
            Address: FE80::21E:F6FF:FEAC:A600
            DR     : this system
    '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowIpv6PimInterface(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_vrf_default(self):
        self.device = Mock(**self.golden_output)
        obj = ShowIpv6PimInterface(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_vrf_non_default(self):
        self.device = Mock(**self.golden_output2)
        obj = ShowIpv6PimInterface(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output,self.golden_parsed_output2)

# ============================================
# Parser for 'show ip pim bsr-router'
# Parser for 'show ip pim vrf xxx bsr-router'
# ============================================
class test_show_ip_pim_bsr_router(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output_bsr_1 = {
        'vrf':
            {'VRF1':
                {
                'address_family':
                    {'ipv4':
                        {'rp':
                            {'bsr':
                                {'bsr_rp_candidate_interface': {
                                    'interface': 'GigabitEthernet3',
                                    'address': '10.1.5.1',
                                    'holdtime': 150 ,
                                    'next_advertisment': '00:00:27',
                                    'priority': 5,
                                    'interval': 60,
                                },
                                'bsr': {
                                    'address': '10.1.5.5',
                                    'hash_mask_length': 0,
                                    'priority': 0,
                                    'address_host': '?',
                                    'up_time': '00:00:26',
                                    'expires': '00:01:45',

                                    },
                                },
                            },
                        },
                    },
                },
            },
        }
    golden_output_bsr_1 = {'execute.return_value': '''
        R1_xe#show ip pim vrf VRF1 bsr-router
        PIMv2 Bootstrap information
          BSR address: 10.1.5.5 (?)
          Uptime:      00:00:26, BSR Priority: 0, Hash mask length: 0
          Expires:     00:01:45
          Candidate RP: 10.1.5.1(GigabitEthernet3)
            Holdtime 150 seconds
            Advertisement interval 60 seconds
            Next advertisement in 00:00:27
            Candidate RP priority : 5
    '''}

    golden_parsed_output_bsr_2 = {
        'vrf':
            {'default':
                {
                'address_family':
                    {'ipv4':
                        {'rp':
                            {'bsr':
                                {'bsr_candidate': {
                                    'address': '1.1.1.1',
                                    'priority': 0,
                                    'hash_mask_length': 0,
                                },
                                    'bsr': {
                                        'address': '4.4.4.4',
                                        'hash_mask_length': 0,
                                        'priority': 0,
                                        'address_host': '?',
                                        'up_time': '00:01:23',
                                        'expires': '00:01:46',

                                    },
                                },
                            },
                        },
                    },
                },
            },
    }
    golden_output_bsr_2 = {'execute.return_value': '''
        R1_xe#show ip pim bsr-router
        PIMv2 Bootstrap information
          BSR address: 4.4.4.4 (?)
          Uptime:      00:01:23, BSR Priority: 0, Hash mask length: 0
          Expires:     00:01:46
        This system is a candidate BSR
          Candidate BSR address: 1.1.1.1, priority: 0, hash mask length: 0

        '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpPimBsrRouter(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_mapping_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_bsr_1)
        obj = ShowIpPimBsrRouter(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output, self.golden_parsed_output_bsr_1)

    def test_golden_mapping_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_bsr_2)
        obj = ShowIpPimBsrRouter(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_bsr_2)

if __name__ == '__main__':
    unittest.main()