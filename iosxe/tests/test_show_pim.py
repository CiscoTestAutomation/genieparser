# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparset
from metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

# Parser
from parser.iosxe.show_pim import ShowIpv6PimInterface,\
                                  ShowIpPimInterface,\
                                  ShowIpv6PimBsrCandidateRp, \
                                  ShowIpPimRpMapping, \
                                  ShowIpv6PimBsrElection

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
# Parser for 'show ip pim bsr election'
# Parser for 'show ip pim vrf xxx bsr election'
# ============================================
class test_show_ip_pim_bsr_election(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output_elec_2 = {
        'vrf':
            {'default':
                {
                'address_family':
                    {'ipv6':
                        {'rp':
                            {'bsr':
                                {'bsr_candidate': {
                                    'address': '2001:1:1:1::1',
                                    'priority': 0,
                                    'hash_mask_length': 126,
                                },
                                'bsr': {
                                    'address': '2001:1:1:1::1',
                                    'hash_mask_length': 126,
                                    'priority': 0,
                                    'up_time': '00:00:07',
                                    'scope_range_list': 'ff00::/8',
                                    'rpf_address': 'FE80::21E:F6FF:FE2D:3600',
                                    'rpf_interface': 'Loopback0',
                                    'expires': '00:00:52',
                                    },
                                },
                            },
                        },
                    },
                },
            },
        }
    golden_output_bsr_elec_2 = {'execute.return_value': '''
    R1_xe#show ipv6 pim bsr election
        PIMv2 BSR information

        BSR Election Information
          Scope Range List: ff00::/8
          This system is the Bootstrap Router (BSR)
             BSR Address: 2001:1:1:1::1
             Uptime: 00:00:07, BSR Priority: 0, Hash mask length: 126
             RPF: FE80::21E:F6FF:FE2D:3600,Loopback0
             BS Timer: 00:00:52
          This system is candidate BSR
              Candidate BSR address: 2001:1:1:1::1, priority: 0, hash mask length: 126
    '''}

    golden_parsed_output_bsr_elec_1 = {
        'vrf':
            {'VRF1':
                {
                    'address_family':
                        {'ipv6':
                            {'rp':
                                {'bsr':
                                    {'bsr_candidate': {
                                        'address': '2001:DB8:1:5::1',
                                        'priority': 0,
                                        'hash_mask_length': 126,
                                    },
                                        'bsr': {
                                            'address': '2001:DB8:1:5::1',
                                            'hash_mask_length': 126,
                                            'priority': 0,
                                            'up_time': '00:08:39',
                                            'scope_range_list': 'ff00::/8',
                                            'rpf_address': 'FE80::5054:FF:FEC3:D71C',
                                            'rpf_interface': 'GigabitEthernet3',
                                            'expires': '00:00:22',
                                        },
                                    },
                                },
                            },
                        },
                },
            },
    }
    golden_output_bsr_elec_1 = {'execute.return_value': '''
            R1_xe#show ipv6 pim vrf VRF1 bsr election
            PIMv2 BSR information

            BSR Election Information
              Scope Range List: ff00::/8
              This system is the Bootstrap Router (BSR)
                 BSR Address: 2001:DB8:1:5::1
                 Uptime: 00:08:39, BSR Priority: 0, Hash mask length: 126
                 RPF: FE80::5054:FF:FEC3:D71C,GigabitEthernet3
                 BS Timer: 00:00:22
              This system is candidate BSR
                  Candidate BSR address: 2001:DB8:1:5::1, priority: 0, hash mask length: 126

            '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpv6PimBsrElection(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_mapping_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_bsr_elec_1)
        obj = ShowIpv6PimBsrElection(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output, self.golden_parsed_output_bsr_elec_1)

    def test_golden_mapping_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_bsr_elec_2)
        obj = ShowIpv6PimBsrElection(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_elec_2)

# ============================================
# Parser for 'show ipv6 pim candidate-rp'
# Parser for 'show ipv6 pim vrf xxx candidate-rp'
# ============================================
class test_show_ipv6_pim_bsr_candidate_rp(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output_candidate_2 = {
        'vrf':
            {'default':
                {
                'address_family':
                    {'ipv6':
                        {'rp':
                            {'bsr':
                                {'2001:3:3:3::3': {
                                    'address': '2001:3:3:3::3',
                                    'priority': 5,
                                    'mode': 'SM',
                                    'holdtime': 150,
                                    'interval': 60,
                                },
                                'rp_candidate_next_advertisement': '00:00:48',
                                },
                            },
                        },
                    },
                },
            },
        }
    golden_output_bsr_candidate_2 = {'execute.return_value': '''
        R3_iosv#show ipv6 pim bsr candidate-rp
        PIMv2 C-RP information
          Candidate RP: 2001:3:3:3::3 SM
            Priority 5, Holdtime 150
            Advertisement interval 60 seconds
            Next advertisement in 00:00:48
    '''}

    golden_parsed_output_bsr_candidate_1 = {
        'vrf':
            {'VRF1':
                {
                'address_family':
                    {'ipv6':
                        {'rp':
                            {'bsr':
                                {'2001:DB8:1:5::1': {
                                    'address': '2001:DB8:1:5::1',
                                    'priority': 192,
                                    'mode': 'SM',
                                    'holdtime': 150,
                                    'interval': 60,
                                    },
                                'rp_candidate_next_advertisement':'00:00:50',
                                },
                            },
                        },
                    },
                },
            },
    }
    golden_output_bsr_candidate_1 = {'execute.return_value': '''
        R1_xe#show ipv6 pim vrf VRF1 bsr candidate-rp
        PIMv2 C-RP information
           Candidate RP: 2001:DB8:1:5::1 SM
             Priority 192, Holdtime 150
            Advertisement interval 60 seconds
            Next advertisement in 00:00:50
        '''}

    golden_output_bsr_candidate_3 = {'execute.return_value': '''
        R2_iosv#show ipv6 pim vrf VRF1 bsr candidate-rp
        %VPN Routing instance VRF1 does not exist. Create first
        '''
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpv6PimBsrCandidateRp(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_candidate_rp_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_bsr_candidate_1)
        obj = ShowIpv6PimBsrCandidateRp(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output, self.golden_parsed_output_bsr_candidate_1)

    def test_golden_candidate_rp_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_bsr_candidate_2)
        obj = ShowIpv6PimBsrCandidateRp(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_candidate_2)

    def test_golden_candidate_rp_3(self):
        self.device = Mock(**self.golden_output_bsr_candidate_3)
        obj = ShowIpv6PimBsrCandidateRp(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

# ============================================
# Parser for 'show ip pim interface'
# Parser for 'show ip pim vrf xxx interface'
# ============================================
class test_show_ip_pim_interface(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output_interface_1 = {
        'vrf':
            {'default':
                {'interfaces':
                     {'GigabitEthernet1':
                         {
                          'address_family': {
                                'ipv4': {
                                    'dr_priority': 1,
                                    'hello_interval': 30,
                                    'neighbor_count': 1,
                                    'version': 2,
                                    'mode': 'sparse-mode',
                                    'dr_address': '10.1.2.2',
                                    'address': ['10.1.2.1'],
                                    },
                          },
                         },
                     'GigabitEthernet2': {
                         'address_family': {
                             'ipv4': {
                                    'dr_priority': 1,
                                    'hello_interval': 30,
                                    'neighbor_count': 1,
                                    'version': 2,
                                    'mode': 'sparse-mode',
                                    'dr_address': '10.1.3.3',
                                    'address': ['10.1.3.1'],
                                 },
                         },
                     },
                     'Loopback0': {
                         'address_family': {
                             'ipv4': {
                                    'dr_priority': 1,
                                    'hello_interval': 30,
                                    'neighbor_count': 0,
                                    'version': 2,
                                    'mode': 'sparse-mode',
                                    'dr_address': '1.1.1.1',
                                    'address': ['1.1.1.1'],
                             },
                         },
                     },
                },
            },
        },
    }
    golden_output_interface_1 = {'execute.return_value': '''
    Address          Interface                Ver/   Nbr    Query  DR         DR
                                          Mode   Count  Intvl  Prior
    10.1.2.1         GigabitEthernet1         v2/S   1      30     1          10.1.2.2
    10.1.3.1         GigabitEthernet2         v2/S   1      30     1          10.1.3.3
    1.1.1.1          Loopback0                v2/S   0      30     1          1.1.1.1
     '''}

    golden_parsed_output_interface_2 = {
        'vrf':
            {'VRF1':
                {'interfaces':
                    {'GigabitEthernet3':
                        {
                        'address_family':
                            {
                            'ipv4': {
                                'dr_priority': 1,
                                'hello_interval': 30,
                                'neighbor_count': 1,
                                'version': 2,
                                'mode': 'sparse-mode',
                                'dr_address': '10.1.5.5',
                                'address': ['10.1.5.1'],
                                },
                        },  },
                    },
                },
            },
    }


    golden_output_interface_2 = {'execute.return_value':'''
    Address          Interface                Ver/   Nbr    Query  DR         DR
                                          Mode   Count  Intvl  Prior
    10.1.5.1         GigabitEthernet3         v2/S   1      30     1          10.1.5.5

    '''}
    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpPimInterface(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_mapping_1(self):
        self.maxDiff = None

        self.device = Mock(**self.golden_output_interface_1)
        obj = ShowIpPimInterface(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_interface_1)

    def test_golden_mapping_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_interface_2)
        obj = ShowIpPimInterface(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output,self.golden_parsed_output_interface_2)

# ============================================
# unit test for 'show ip pim mapping'
# unit test for 'show ip pim vrf xxx mapping'
# ============================================
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
                      'ipv4':
                          {
                            'rp':
                                {
                                'rp_mappings': {
                                    '224.0.0.0/4 3.3.3.3 bootstrap': {
                                      'group': '224.0.0.0/4',
                                      'rp_address': '3.3.3.3',
                                      'rp_address_host': '?',
                                      'up_time': '00:00:19',
                                      'expiration': '00:02:19',
                                      'priority': 5,
                                      'hold_time': 150,
                                      'protocol': 'bootstrap',
                                    },
                                    '224.0.0.0/4 2.2.2.2 bootstrap': {
                                        'group': '224.0.0.0/4',
                                        'rp_address': '2.2.2.2',
                                        'rp_address_host': '?',
                                        'up_time': '00:00:35',
                                        'expiration': '00:02:03',
                                        'priority': 10,
                                        'hold_time': 150,
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
                                        'rp_address': '20.0.0.3',
                                        'up_time': '00:22:08',
                                        'expiration': '00:02:40',
                                        'protocol': 'autorp',
                                    },

                                },
                                 'rp_list': {
                                    '3.3.3.3 bootstrap': {
                                          'address': '3.3.3.3',
                                          'up_time': '00:00:19',
                                          'expiration': '00:02:19',
                                          'bsr_version':'v2',
                                          'info_source_type': "bootstrap",
                                          "info_source_address": "4.4.4.4",
                                          },
                                     '3.3.3.3 static': {
                                         'address': '3.3.3.3',
                                         "info_source_type": "static",
                                     },
                                     '2.2.2.2 bootstrap': {
                                         'address': '2.2.2.2',
                                         'bsr_version': 'v2',
                                         'up_time': '00:00:35',
                                         'expiration': '00:02:03',
                                         "info_source_type": "bootstrap",
                                         "info_source_address": "4.4.4.4",
                                     },
                                     '20.0.0.3 autorp': {
                                         'address': '20.0.0.3',
                                         'bsr_version': 'v2v1',
                                         'up_time': '00:22:08',
                                         'expiration': '00:02:40',
                                         "info_source_type": "autorp",
                                         'info_source_address': '20.0.0.2',
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

    golden_parsed_output_mapping_2 = {
        'vrf':
            {'VRF1':
                {
                'address_family':
                    {'ipv4':
                        {
                        'rp':
                            {
                            'rp_mappings': {
                                '224.0.0.0/4 10.1.5.5 static': {
                                    'group': '224.0.0.0/4',
                                    'rp_address_host': '?',
                                    'rp_address': '10.1.5.5',
                                    'protocol': 'static',
                                    },
                                },
                            'rp_list': {
                                '10.1.5.5 static': {
                                      'address': '10.1.5.5',
                                      'info_source_type': 'static',
                                      },
                                },
                            },
                        },
                    },
                },
            },
        }

    golden_output_mapping_2 = {'execute.return_value':'''
    R1_xe#show ip pim vrf VRF1 rp mapping
        PIM Group-to-RP Mappings

        Group(s): 224.0.0.0/4, Static
            RP: 10.1.5.5 (?)
    '''}

    golden_output_mapping_3 = {'execute.return_value': '''
        R1_xe#show ip pim vrf VRF1 rp mapping
            PIM Group-to-RP Mappings
            % DDDDD
            '''
    }
    def test_empty_1(self):
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

    def test_golden_mapping_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_mapping_2)
        obj = ShowIpPimRpMapping(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output,self.golden_parsed_output_mapping_2)

    def test_empty_nodata(self):
        self.device = Mock(**self.golden_output_mapping_3)
        obj = ShowIpPimRpMapping(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

if __name__ == '__main__':
    unittest.main()