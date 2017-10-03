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
                                  ShowIpPimRpMapping


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

class test_show_ip_pim_rp_mapping(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output_mapping_1 = {
        'vrf':
            {
                'default':
                    {
                        'address_family':
                            {
                              'ipv6':
                                  {
                                    'rp':
                                         {
                                            'rp_mappings': {
                                                '224.0.0.0/4 3.3.3.3 bootstrap': {
                                                  'group': '224.0.0.0/4',
                                                  'rp_address': '3.3.3.3',
                                                  'rp_address_host': '?',
                                                  'rp_version': 'v2',
                                                  'up_time': '00:00:19',
                                                  'expiration': '00:02:19',
                                                  'priority': 5,
                                                  'hold_time': 150,
                                                  'info_source': '4.4.4.4',
                                                  'protocol': 'bootstrap',
                                                },
                                                '224.0.0.0/4 2.2.2.2 bootstrap': {
                                                    'group': '224.0.0.0/4',
                                                    'rp_address': '2.2.2.2',
                                                    'rp_address_host': '?',
                                                    'rp_version': 'v2',
                                                    'up_time': '00:00:35',
                                                    'expiration': '00:02:03',
                                                    'priority': 10,
                                                    'hold_time': 150,
                                                    'info_source': '4.4.4.4',
                                                    'protocol': 'bootstrap',
                                                },
                                                '224.0.0.0/4 3.3.3.3 static': {
                                                    'group': '224.0.0.0/4',
                                                    'rp_address_host': '?',
                                                    'rp_address': '3.3.3.3',
                                                    'protocol': 'static',
                                                },
                                                '224.0.0.0/4 20.0.0.3 autorp': {
                                                    'group': '224.0.0.0/4',
                                                    'rp_address_host': '?',
                                                    'rp_version': 'v2v1',
                                                    'rp_address': '20.0.0.3',
                                                    'up_time': '00:22:08',
                                                    'expiration': '00:02:40',
                                                    'info_source': '20.0.0.2',
                                                    'protocol': 'autorp',
                                                },

                                            },
                                        },

                                  },
                            },

                    },
            },

    }
    golden_output_mapping_1 = {'execute.return_value': '''
    R1_xe#show ip pim rp mapping
    PIM Group-to-RP Mappings

    Group(s) 224.0.0.0/4
      RP 3.3.3.3 (?), v2
        Info source: 4.4.4.4 (?), via bootstrap, priority 5, holdtime 150
         Uptime: 00:00:19, expires: 00:02:19
      RP 2.2.2.2 (?), v2
        Info source: 4.4.4.4 (?), via bootstrap, priority 10, holdtime 150
         Uptime: 00:00:35, expires: 00:02:03
    Group(s): 224.0.0.0/4, Static
        RP: 3.3.3.3 (?)

    Group(s) 224.0.0.0/4
      RP 20.0.0.3 (?), v2v1
        Info source: 20.0.0.2 (?), via Auto-RP
         Uptime: 00:22:08, expires: 00:02:40

     '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpPimRpMapping(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_mapping_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_mapping_1)
        obj = ShowIpPimRpMapping(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_mapping_1)

if __name__ == '__main__':
    unittest.main()