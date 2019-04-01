# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

# Parser
from genie.libs.parser.iosxe.show_pim import ShowIpv6PimInterface,\
                                  ShowIpPimInterfaceDetail,\
                                  ShowIpPimInterface, \
                                  ShowIpv6PimBsrCandidateRp, \
                                  ShowIpPimRpMapping, \
                                  ShowIpv6PimBsrElection, \
                                  ShowIpPimBsrRouter, \
                                  ShowIpPimNeighbor, \
                                  ShowIpv6PimNeighbor, \
                                  ShowIpv6PimNeighborDetail, \
                                  ShowIpPimInterfaceDf


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
                                    'dr_address': '10.4.1.1',
                                    'address': ['10.4.1.1'],
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
    10.4.1.1         Loopback0                v2/S   0      30     1          10.4.1.1
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
                                        'mode': 'dense-mode',
                                        'dr_address': '10.1.5.5',
                                        'address': ['10.1.5.1'],
                                    },
                                },
                        },
                    },
                },
            },
    }
    golden_output_interface_2 = {'execute.return_value': '''
    Address          Interface                Ver/   Nbr    Query  DR         DR
                                          Mode   Count  Intvl  Prior
    10.1.5.1         GigabitEthernet3         v2/D   1      30     1          10.1.5.5

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
        self.assertEqual(parsed_output, self.golden_parsed_output_interface_1)

    def test_golden_mapping_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_interface_2)
        obj = ShowIpPimInterface(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output, self.golden_parsed_output_interface_2)

# ============================================
# Parser for 'show ipv6 pim bsr election'
# Parser for 'show ipv6 pim vrf xxx bsr election'
# ============================================
class test_show_ipv6_pim_bsr_election(unittest.TestCase):
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
                                            'rp_candidate_next_advertisement': '00:00:50',
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
                                {'GigabitEthernet3': {
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
                                    'address': '10.4.1.1',
                                    'priority': 0,
                                    'hash_mask_length': 0,
                                },
                                    'bsr': {
                                        'address': '10.64.4.4',
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
          BSR address: 10.64.4.4 (?)
          Uptime:      00:01:23, BSR Priority: 0, Hash mask length: 0
          Expires:     00:01:46
        This system is a candidate BSR
          Candidate BSR address: 10.4.1.1, priority: 0, hash mask length: 0

        '''}

    golden_parsed_output_bsr_3 = {
        'vrf':
            {'default':
                {
                    'address_family':
                        {'ipv4':
                            {'rp':
                                {'bsr':
                                    {'Loopback0': {
                                        'interface': 'Loopback0',
                                        'address': '10.16.2.2',
                                        'holdtime': 150,
                                        'next_advertisment': '00:00:26',
                                        'priority': 10,
                                        'interval': 60,
                                        },
                                    'bsr': {
                                        'address': '10.64.4.4',
                                        'hash_mask_length': 0,
                                        'priority': 0,
                                        'address_host': '?',
                                        'up_time': '3d07h',
                                    },
                                    'bsr_next_bootstrap':'00:00:06',
                                },
                            },
                        },
                    },
                },
            },
    }
    golden_output_bsr_3 = {'execute.return_value': '''
            R2_iosv#show ip pim bsr-router
            PIMv2 Bootstrap information
              BSR address: 10.64.4.4 (?)
              Uptime:      3d07h, BSR Priority: 0, Hash mask length: 0
              Next bootstrap message in 00:00:06
              Candidate RP: 10.16.2.2(Loopback0)
                Holdtime 150 seconds
                Advertisement interval 60 seconds
                Next advertisement in 00:00:26
                Candidate RP priority : 10
    '''}

    golden_parsed_output_bsr_4 = {
        'vrf':
            {'VRF1':
                {
                    'address_family':
                        {'ipv4':
                            {'rp':
                                {'bsr':
                                    {'GigabitEthernet0/2': {
                                        'interface': 'GigabitEthernet0/2',
                                        'address': '10.4.6.4',
                                        'holdtime': 150,
                                        'next_advertisment': '00:00:00',
                                        'priority': 5,
                                        'interval': 60,
                                    },
                                    'bsr': {
                                        'address': '10.4.6.6',
                                        'hash_mask_length': 0,
                                        'priority': 0,
                                        'address_host': '?',
                                        'up_time': '4d03h',
                                        'expires': '00:02:00',
                                    },
                                },
                            },
                        },
                    },
                },
            },
    }

    golden_output_bsr_4 = {'execute.return_value':'''
            R4_iosv#show ip pim vrf VRF1 bsr-router
        PIMv2 Bootstrap information
          BSR address: 10.4.6.6 (?)
          Uptime:      4d03h, BSR Priority: 0, Hash mask length: 0
          Expires:     00:02:00
          Candidate RP: 10.4.6.4(GigabitEthernet0/2)
            Holdtime 150 seconds
            Advertisement interval 60 seconds
            Next advertisement in 00:00:00
            Candidate RP priority : 5
        '''
    }
    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpPimBsrRouter(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_bsr_router_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_bsr_1)
        obj = ShowIpPimBsrRouter(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output, self.golden_parsed_output_bsr_1)

    def test_golden_bsr_router_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_bsr_2)
        obj = ShowIpPimBsrRouter(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_bsr_2)

    def test_golden_bsr_router_3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_bsr_3)
        obj = ShowIpPimBsrRouter(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_bsr_3)

    def test_golden_bsr_router_4(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_bsr_4)
        obj = ShowIpPimBsrRouter(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output, self.golden_parsed_output_bsr_4)

# ============================================
# unit test for 'show ip pim mapping'
# unit test for 'show ip pim vrf xxx mapping'
# ============================================
class test_show_ip_pim_rp_mapping(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output_mapping_1 = {
        "vrf": {
              "default": {
                   "address_family": {
                        "ipv4": {
                             "rp": {
                                  "rp_list": {
                                       "10.36.3.3 BIDIR static": {
                                            "info_source_type": "static",
                                            "address": "10.36.3.3",
                                            'mode': 'BIDIR'
                                       },
                                       "10.145.0.3 SM autorp": {
                                            "address": "10.145.0.3",
                                            "info_source_address": "10.145.0.2",
                                            "bsr_version": "v2v1",
                                            "info_source_type": "autorp",
                                            "expiration": "00:02:40",
                                            "up_time": "00:22:08",
                                            'mode': 'SM'
                                       },
                                       "10.16.2.2 SM bootstrap": {
                                            "address": "10.16.2.2",
                                            "info_source_address": "10.64.4.4",
                                            "bsr_version": "v2",
                                            "info_source_type": "bootstrap",
                                            "expiration": "00:02:03",
                                            "up_time": "00:00:35",
                                            'mode': 'SM'
                                       },
                                       "10.36.3.3 SM bootstrap": {
                                            "address": "10.36.3.3",
                                            "info_source_address": "10.64.4.4",
                                            "bsr_version": "v2",
                                            "info_source_type": "bootstrap",
                                            "expiration": "00:02:19",
                                            "up_time": "00:00:19",
                                            'mode': 'SM'
                                       }
                                  },
                                  "rp_mappings": {
                                       "224.0.0.0/4 10.145.0.3 autorp": {
                                            "group": "224.0.0.0/4",
                                            "rp_address_host": "?",
                                            "protocol": "autorp",
                                            "expiration": "00:02:40",
                                            "rp_address": "10.145.0.3",
                                            "up_time": "00:22:08"
                                       },
                                       "224.0.0.0/4 10.16.2.2 bootstrap": {
                                            "group": "224.0.0.0/4",
                                            "rp_address_host": "?",
                                            "hold_time": 150,
                                            "priority": 10,
                                            "protocol": "bootstrap",
                                            "expiration": "00:02:03",
                                            "rp_address": "10.16.2.2",
                                            "up_time": "00:00:35"
                                       },
                                       "224.0.0.0/4 10.36.3.3 bootstrap": {
                                            "group": "224.0.0.0/4",
                                            "rp_address_host": "?",
                                            "hold_time": 150,
                                            "priority": 5,
                                            "protocol": "bootstrap",
                                            "expiration": "00:02:19",
                                            "rp_address": "10.36.3.3",
                                            "up_time": "00:00:19"
                                       },
                                       "224.0.0.0/4 10.36.3.3 static": {
                                            "group": "224.0.0.0/4",
                                            "protocol": "static",
                                            "rp_address": "10.36.3.3",
                                            "rp_address_host": "?"
                                       }
                                  },
                                  "static_rp": {
                                       "10.36.3.3": {
                                            "bidir": {}
                                       }
                                  },
                                  "bsr": {
                                       "rp": {
                                            "rp_address": "10.16.2.2",
                                            "up_time": "00:22:08",
                                            "group_policy": "224.0.0.0/4"
                                       }
                                  },
                             }
                        }
                   }
              }
         }
    }
    golden_output_mapping_1 = {'execute.return_value': '''
    R1_xe#show ip pim rp mapping
    PIM Group-to-RP Mappings

    Group(s) 224.0.0.0/4
      RP 10.36.3.3 (?), v2
        Info source: 10.64.4.4 (?), via bootstrap, priority 5, holdtime 150
         Uptime: 00:00:19, expires: 00:02:19
      RP 10.16.2.2 (?), v2
        Info source: 10.64.4.4 (?), via bootstrap, priority 10, holdtime 150
         Uptime: 00:00:35, expires: 00:02:03

    Group(s): 224.0.0.0/4, Static, Bidir Mode 
        RP: 10.36.3.3 (?)

    Group(s) 224.0.0.0/4
      RP 10.145.0.3 (?), v2v1
        Info source: 10.145.0.2 (?), via Auto-RP
         Uptime: 00:22:08, expires: 00:02:40

     '''}

    golden_parsed_output_mapping_2 = {
        "vrf": {
              "VRF1": {
                   "address_family": {
                        "ipv4": {
                             "rp": {
                                  "rp_mappings": {
                                       "STATIC_RP_V4 192.168.151.1 static": {
                                            "rp_address_host": "?",
                                            "protocol": "static",
                                            "rp_address": "192.168.151.1",
                                            "group": "STATIC_RP_V4"
                                       },
                                       "224.0.0.0/4 10.1.5.5 static": {
                                            "rp_address_host": "?",
                                            "protocol": "static",
                                            "rp_address": "10.1.5.5",
                                            "group": "224.0.0.0/4"
                                       }
                                  },
                                  "rp_list": {
                                       "10.1.5.5 SM static": {
                                            "mode": "SM",
                                            "address": "10.1.5.5",
                                            "info_source_type": "static"
                                       },
                                       "192.168.151.1 SM static": {
                                            "mode": "SM",
                                            "address": "192.168.151.1",
                                            "info_source_type": "static"
                                       }
                                  },
                                  "static_rp": {
                                       "192.168.151.1": {
                                            "sm": {
                                                 "policy_name": "STATIC_RP_V4",
                                                 "override": True
                                            }
                                       }
                                  }
                             }
                        }
                   }
              }
        }
    }

    golden_output_mapping_2 = {'execute.return_value':'''
    R1_xe#show ip pim vrf VRF1 rp mapping
        PIM Group-to-RP Mappings

        Group(s): 224.0.0.0/4, Static
            RP: 10.1.5.5 (?)
        Acl: STATIC_RP_V4, Static-Override
            RP: 192.168.151.1 (?)
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

# =============================================================
# parser for : show ip pim interface detail
# parser for : show ip pim vrf <vrf_name> interface detail
# =============================================================

class test_show_ip_pim_interface_detail(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output_detail = {'execute.return_value': ''}

    golden_parsed_output_intf_detail_1 = {
        'vrf':
            {'default':
                {'interfaces':{
                    'GigabitEthernet1':{
                        'address_family':{
                            'ipv4': {
                                'bfd': {
                                    'enable': False,
                                },
                                'hello_interval': 30,
                                'hello_packets_in': 8,
                                'hello_packets_out': 10,
                                'oper_status': 'up',
                                'enable': True,
                                'neighbor_filter': '7',
                                'address': ['10.1.2.1/24'],
                                'multicast': {
                                    'switching': 'fast',
                                    'packets_in': 5,
                                    'packets_out': 0,
                                    'ttl_threshold': 0,
                                    'tag_switching': False,
                                },
                                'pim_status': 'enabled',
                                'version': 2,
                                'mode': 'sparse',
                                'sm': {},
                                'dr_address': '10.1.2.2',
                                'neighbor_count': 1,
                                'jp_interval': 60,
                                'state_refresh_processing': 'enabled',
                                'state_refresh_origination': 'disabled',
                                'nbma_mode': 'disabled',
                                'atm_multipoint_signalling': 'disabled',
                                'bsr_border': False,
                                'neighbors_rpf_proxy_capable': True,
                                'none_dr_join': False,
                            },
                        },
                    },
                    'GigabitEthernet2': {
                        'address_family': {
                            'ipv4': {
                                'bfd': {
                                    'enable': False,
                                },
                                'hello_interval': 30,
                                'hello_packets_in': 7,
                                'hello_packets_out': 10,
                                'oper_status': 'up',
                                'enable': True,
                                'address': ['10.1.3.1/24'],
                                'multicast': {
                                    'switching': 'fast',
                                    'packets_in': 5,
                                    'packets_out': 0,
                                    'ttl_threshold': 0,
                                    'tag_switching': False,
                                },
                                'pim_status': 'enabled',
                                'version': 2,
                                'mode': 'dense',
                                'dm': {},
                                'dr_address': '10.1.3.3',
                                'neighbor_count': 1,
                                'jp_interval': 60,
                                'state_refresh_processing': 'enabled',
                                'state_refresh_origination': 'disabled',
                                'nbma_mode': 'disabled',
                                'atm_multipoint_signalling': 'disabled',
                                'bsr_border': False,
                                'neighbors_rpf_proxy_capable': True,
                                'none_dr_join': False,
                            },
                        },
                    },
                    'Loopback0': {
                        'address_family': {
                            'ipv4': {
                                'bfd': {
                                    'enable': False,
                                },
                                'hello_interval': 30,
                                'hello_packets_in': 8,
                                'hello_packets_out': 8,
                                'oper_status': 'up',
                                'enable': True,
                                'address': ['10.4.1.1/32'],
                                'multicast': {
                                    'switching': 'fast',
                                    'packets_in': 0,
                                    'packets_out': 0,
                                    'ttl_threshold': 0,
                                    'tag_switching': False,
                                },
                                'pim_status': 'enabled',
                                'version': 2,
                                'mode': 'sparse',
                                'sm': {},
                                'dr_address': '10.4.1.1',
                                'neighbor_count': 0,
                                'jp_interval': 60,
                                'state_refresh_processing': 'enabled',
                                'state_refresh_origination': 'disabled',
                                'nbma_mode': 'disabled',
                                'atm_multipoint_signalling': 'disabled',
                                'bsr_border': False,
                                'neighbors_rpf_proxy_capable': False,
                                'none_dr_join': False,
                            },
                        },
                    },
                },
            },
        }
    }
    golden_output_intf_detail_1 = {'execute.return_value': '''
        R1_xe#show ip pim interface detail
        GigabitEthernet1 is up, line protocol is up
          Internet address is 10.1.2.1/24
          Multicast switching: fast
          Multicast packets in/out: 5/0
          Multicast TTL threshold: 0
          PIM: enabled
            PIM version: 2, mode: sparse
            PIM DR: 10.1.2.2
            PIM neighbor count: 1
            PIM neighbor filter: 7
            PIM Hello/Query interval: 30 seconds
            PIM Hello packets in/out: 8/10
            PIM J/P interval: 60 seconds
            PIM State-Refresh processing: enabled
            PIM State-Refresh origination: disabled
            PIM NBMA mode: disabled
            PIM ATM multipoint signalling: disabled
            PIM domain border: disabled
            PIM neighbors rpf proxy capable: TRUE
            PIM BFD: disabled
            PIM Non-DR-Join: FALSE
          Multicast Tagswitching: disabled
        GigabitEthernet2 is up, line protocol is up
          Internet address is 10.1.3.1/24
          Multicast switching: fast
          Multicast packets in/out: 5/0
          Multicast TTL threshold: 0
          PIM: enabled
            PIM version: 2, mode: dense
            PIM DR: 10.1.3.3
            PIM neighbor count: 1
            PIM Hello/Query interval: 30 seconds
            PIM Hello packets in/out: 7/10
            PIM J/P interval: 60 seconds
            PIM State-Refresh processing: enabled
            PIM State-Refresh origination: disabled
            PIM NBMA mode: disabled
            PIM ATM multipoint signalling: disabled
            PIM domain border: disabled
            PIM neighbors rpf proxy capable: TRUE
            PIM BFD: disabled
            PIM Non-DR-Join: FALSE
          Multicast Tagswitching: disabled
        Loopback0 is up, line protocol is up
          Internet address is 10.4.1.1/32
          Multicast switching: fast
          Multicast packets in/out: 0/0
          Multicast TTL threshold: 0
          PIM: enabled
            PIM version: 2, mode: sparse
            PIM DR: 10.4.1.1 (this system)
            PIM neighbor count: 0
            PIM Hello/Query interval: 30 seconds
            PIM Hello packets in/out: 8/8
            PIM J/P interval: 60 seconds
            PIM State-Refresh processing: enabled
            PIM State-Refresh origination: disabled
            PIM NBMA mode: disabled
            PIM ATM multipoint signalling: disabled
            PIM domain border: disabled
            PIM neighbors rpf proxy capable: FALSE
            PIM BFD: disabled
            PIM Non-DR-Join: FALSE
          Multicast Tagswitching: disabled
     '''}

    golden_parsed_output_intf_detail_2 = {
        'vrf':
            {'VRF1':
                {'interfaces':
                    {'GigabitEthernet3':
                        {
                        'address_family':
                            {
                            'ipv4': {
                                'bfd': {
                                    'enable': False,
                                },
                                'hello_interval': 30,
                                'hello_packets_in': 6,
                                'hello_packets_out': 6,
                                'oper_status': 'up',
                                'enable': True,
                                'address': ['10.1.5.1/24'],
                                'multicast': {
                                    'switching': 'fast',
                                    'packets_in': 4,
                                    'packets_out': 0,
                                    'ttl_threshold': 0,
                                    'tag_switching': False,
                                },
                                'pim_status': 'enabled',
                                'version': 2,
                                'mode': 'passive',
                                'sm': {
                                    'passive': True,
                                },
                                'dr_address': '10.1.5.5',
                                'neighbor_count': 1,
                                'jp_interval': 60,
                                'state_refresh_processing': 'enabled',
                                'state_refresh_origination': 'disabled',
                                'nbma_mode': 'disabled',
                                'atm_multipoint_signalling': 'disabled',
                                'bsr_border': False,
                                'neighbors_rpf_proxy_capable': True,
                                'none_dr_join': False,
                                },
                             },
                        },
                    },
                },
            },
        }
    golden_output_intf_detail_2 = {'execute.return_value':'''
        R1_xe#show ip pim vrf VRF1 interface detail
        GigabitEthernet3 is up, line protocol is up
          Internet address is 10.1.5.1/24
          Multicast switching: fast
          Multicast packets in/out: 4/0
          Multicast TTL threshold: 0
          PIM: enabled
            PIM version: 2, mode: passive
            PIM DR: 10.1.5.5
            PIM neighbor count: 1
            PIM Hello/Query interval: 30 seconds
            PIM Hello packets in/out: 6/6
            PIM J/P interval: 60 seconds
            PIM State-Refresh processing: enabled
            PIM State-Refresh origination: disabled
            PIM NBMA mode: disabled
            PIM ATM multipoint signalling: disabled
            PIM domain border: disabled
            PIM neighbors rpf proxy capable: TRUE
            PIM BFD: disabled
            PIM Non-DR-Join: FALSE
          Multicast Tagswitching: disabled
    '''}

    def test_empty_detail(self):
        self.device = Mock(**self.empty_output_detail)
        obj = ShowIpPimInterfaceDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


    def test_golden_detail_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_intf_detail_1)
        obj = ShowIpPimInterfaceDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_intf_detail_1)

    def test_golden_intf_detail_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_intf_detail_2)
        obj = ShowIpPimInterfaceDetail(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output,self.golden_parsed_output_intf_detail_2)


# ============================================
# Parser for 'show ip pim neighbor'
# Parser for 'show ip pim vrf xxx neighborrrr'
# ============================================
class test_show_ip_pim_neighbor(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    parsed_output = {
        "vrf": {
              "default": {
                   "interfaces": {
                        "Port-channel1.100": {
                             "address_family": {
                                  "ipv4": {
                                       "neighbors": {
                                            "192.168.4.1": {
                                                 "dr_priority": 1,
                                                 "state_refresh_capable": True,
                                                 "proxy_capable": True,
                                                 "interface": "Port-channel1.100",
                                                 "genid_capable": True,
                                                 "version": "v2",
                                                 "expiration": "00:01:40",
                                                 "up_time": "4w4d"
                                            }
                                       }
                                  }
                             }
                        },
                        "GigabitEthernet0/2/3.100": {
                             "address_family": {
                                  "ipv4": {
                                       "neighbors": {
                                            "192.168.205.2": {
                                                 "dr_priority": 1,
                                                 "designated_router": True,
                                                 "proxy_capable": True,
                                                 "interface": "GigabitEthernet0/2/3.100",
                                                 "bidir_capable": True,
                                                 "expiration": "00:01:19",
                                                 "version": "v2",
                                                 "state_refresh_capable": True,
                                                 "genid_capable": True,
                                                 "up_time": "4w4d"
                                            }
                                       }
                                  }
                             }
                        }
                   }
              }
         }        
    }
    golden_output = {'execute.return_value': '''
        PIM Neighbor Table
        Mode: B - Bidir Capable, DR - Designated Router, N - Default DR Priority,
              P - Proxy Capable, S - State Refresh Capable, G - GenID Capable,
              L - DR Load-balancing Capable
        Neighbor          Interface                Uptime/Expires    Ver   DR
        Address                                                            Prio/Mode
        192.168.4.1       Port-channel1.100        4w4d/00:01:40     v2    1 / S P G
        192.168.205.2     GigabitEthernet0/2/3.100 4w4d/00:01:19     v2    1 / DR B S P G
    
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpPimNeighbor(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_default_vrf(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowIpPimNeighbor(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.parsed_output)


# ============================================
# Parser for 'show ipv6 pim neighbor'
# Parser for 'show ipv6 pim vrf xxx neighbor'
# ============================================
class test_show_ipv6_pim_neighbor(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    parsed_output = {
        "vrf": {
              "default": {
                   "interfaces": {
                        "Port-channel2.103": {
                             "address_family": {
                                  "ipv6": {
                                       "neighbors": {
                                            "FE80::21A:30FF:FE47:6EC1": {
                                                 "dr_priority": 1,
                                                 "expiration": "00:01:31",
                                                 "bidir_capable": True,
                                                 "up_time": "1d13h",
                                                 "interface": "Port-channel2.103",
                                                 "genid_capable": True
                                            }
                                       }
                                  }
                             }
                        },
                        "Port-channel2.101": {
                             "address_family": {
                                  "ipv6": {
                                       "neighbors": {
                                            "FE80::21A:30FF:FE47:6EC1": {
                                                 "dr_priority": 1,
                                                 "expiration": "00:01:31",
                                                 "bidir_capable": True,
                                                 "up_time": "1d13h",
                                                 "interface": "Port-channel2.101",
                                                 "genid_capable": True
                                            }
                                       }
                                  }
                             }
                        },
                        "Port-channel2.100": {
                             "address_family": {
                                  "ipv6": {
                                       "neighbors": {
                                            "FE80::21A:30FF:FE47:6EC1": {
                                                 "dr_priority": 1,
                                                 "expiration": "00:01:36",
                                                 "bidir_capable": True,
                                                 "up_time": "1d13h",
                                                 "interface": "Port-channel2.100",
                                                 "genid_capable": True
                                            }
                                       }
                                  }
                             }
                        }
                   }
              }
         }        
    }
    golden_output = {'execute.return_value': '''
        PIM Neighbor Table
        Mode: B - Bidir Capable, G - GenID Capable
        Neighbor Address           Interface          Uptime    Expires  Mode DR pri

        FE80::21A:30FF:FE47:6EC1   Port-channel2.100  1d13h     00:01:36 B G     1
        FE80::21A:30FF:FE47:6EC1   Port-channel2.101  1d13h     00:01:31 B G     1
        FE80::21A:30FF:FE47:6EC1   Port-channel2.103  1d13h     00:01:31 B G     1    
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpv6PimNeighbor(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_default_vrf(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowIpv6PimNeighbor(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.parsed_output)


# ===================================================
# Parser for 'show ipv6 pim neighbor detail'
# Parser for 'show ipv6 pim vrf xxx neighbor detail'
# ====================================================
class test_show_ipv6_pim_neighbor_detail(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    parsed_output = {
        "vrf": {
              "default": {
                   "interfaces": {
                        "Port-channel1.100": {
                             "address_family": {
                                  "ipv6": {
                                       "neighbors": {
                                            "secondary_address": [
                                                 "2001::1:1"
                                            ],
                                            "FE80::21A:30FF:FE47:6EC0": {
                                                 "up_time": "3w3d",
                                                 "dr_priority": 1,
                                                 "expiration": "00:01:37",
                                                 "interface": "Port-channel1.100",
                                                 "genid_capable": True,
                                                 "bidir_capable": True
                                            }
                                       }
                                  }
                             }
                        },
                        "Port-channel1.101": {
                             "address_family": {
                                  "ipv6": {
                                       "neighbors": {
                                            "secondary_address": [
                                                 "2001:1::1:1"
                                            ],
                                            "FE80::21A:30FF:FE47:6EC0": {
                                                 "up_time": "3w3d",
                                                 "dr_priority": 1,
                                                 "expiration": "00:01:38",
                                                 "interface": "Port-channel1.101",
                                                 "genid_capable": True,
                                                 "bidir_capable": True
                                            }
                                       }
                                  }
                             }
                        },
                        "GigabitEthernet0/2/3.100": {
                             "address_family": {
                                  "ipv6": {
                                       "neighbors": {
                                            "secondary_address": [
                                                 "2001::4:2"
                                            ],
                                            "FE80::2D7:8FFF:FECB:8602": {
                                                 "up_time": "3w3d",
                                                 "designated_router": True,
                                                 "dr_priority": 1,
                                                 "expiration": "00:01:25",
                                                 "interface": "GigabitEthernet0/2/3.100",
                                                 "genid_capable": True,
                                                 "bidir_capable": True
                                            }
                                       }
                                  }
                             }
                        },
                        "GigabitEthernet0/2/0.101": {
                             "address_family": {
                                  "ipv6": {
                                       "neighbors": {
                                            "FE80::21A:30FF:FE47:6E01": {
                                                 "up_time": "3w3d",
                                                 "dr_priority": 1,
                                                 "expiration": "00:01:24",
                                                 "interface": "GigabitEthernet0/2/0.101",
                                                 "genid_capable": True,
                                                 "bidir_capable": True
                                            },
                                            "secondary_address": [
                                                 "2001:1::1"
                                            ]
                                       }
                                  }
                             }
                        },
                        "GigabitEthernet0/2/3.101": {
                             "address_family": {
                                  "ipv6": {
                                       "neighbors": {
                                            "secondary_address": [
                                                 "2001:1::4:2"
                                            ],
                                            "FE80::2D7:8FFF:FECB:8602": {
                                                 "up_time": "3w3d",
                                                 "designated_router": True,
                                                 "dr_priority": 1,
                                                 "expiration": "00:01:42",
                                                 "interface": "GigabitEthernet0/2/3.101",
                                                 "genid_capable": True,
                                                 "bidir_capable": True
                                            }
                                       }
                                  }
                             }
                        },
                        "GigabitEthernet0/2/0.100": {
                             "address_family": {
                                  "ipv6": {
                                       "neighbors": {
                                            "FE80::21A:30FF:FE47:6E01": {
                                                 "up_time": "3w3d",
                                                 "dr_priority": 1,
                                                 "expiration": "00:01:33",
                                                 "interface": "GigabitEthernet0/2/0.100",
                                                 "genid_capable": True,
                                                 "bidir_capable": True
                                            },
                                            "secondary_address": [
                                                 "2001::1"
                                            ]
                                       }
                                  }
                             }
                        }
                   }
              }
         }
    }
    golden_output = {'execute.return_value': '''
        PIM Neighbor Table
        Mode: B - Bidir Capable, G - GenID Capable
        Neighbor Address(es)       Interface          Uptime    Expires  Mode DR pri
        Address-list Hello option included as type 24 and 65001

        FE80::21A:30FF:FE47:6EC0   Port-channel1.100  3w3d      00:01:37 B G     1
        2001::1:1

        FE80::21A:30FF:FE47:6EC0   Port-channel1.101  3w3d      00:01:38 B G     1
        2001:1::1:1

        FE80::21A:30FF:FE47:6E01   Gi0/2/0.100        3w3d      00:01:33 B G     1
        2001::1

        FE80::21A:30FF:FE47:6E01   Gi0/2/0.101        3w3d      00:01:24 B G     1
        2001:1::1

        FE80::2D7:8FFF:FECB:8602   Gi0/2/3.100        3w3d      00:01:25 B G  DR 1
        2001::4:2

        FE80::2D7:8FFF:FECB:8602   Gi0/2/3.101        3w3d      00:01:42 B G  DR 1
        2001:1::4:2

    
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpv6PimNeighborDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_default_vrf(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowIpv6PimNeighborDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.parsed_output)


# ============================================
# Parser for 'show ip pim interface df'
# Parser for 'show ip pim vrf xxx interface df'
# ============================================
class test_show_ip_pim_interface_df(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    parsed_output = {
        "vrf": {
            "default": {
               "address_family": {
                    "ipv4": {
                         "rp": {
                              "bidir": {
                                   "interface_df_election": {
                                        "10.10.0.2 Ethernet3/3": {
                                             "df_address": "10.4.0.2",
                                             "metric": 0,
                                             "df_uptime": "00:03:49",
                                             "address": "10.10.0.2",
                                             "winner_metric": 0,
                                             "interface_name": "Ethernet3/3"
                                        },
                                        "10.10.0.3 Ethernet3/3": {
                                             "df_address": "10.4.0.3",
                                             "metric": 0,
                                             "df_uptime": "00:01:49",
                                             "address": "10.10.0.3",
                                             "winner_metric": 0,
                                             "interface_name": "Ethernet3/3"
                                        },
                                        "10.10.0.3 Ethernet3/4": {
                                             "df_address": "10.5.0.2",
                                             "metric": 409600,
                                             "df_uptime": "00:02:32",
                                             "address": "10.10.0.3",
                                             "winner_metric": 409600,
                                             "interface_name": "Ethernet3/4"
                                        },
                                        "10.10.0.5 Ethernet3/4": {
                                             "df_address": "10.5.0.2",
                                             "metric": 435200,
                                             "df_uptime": "00:02:16",
                                             "address": "10.10.0.5",
                                             "winner_metric": 435200,
                                             "interface_name": "Ethernet3/4"
                                        },
                                        "10.10.0.2 Loopback0": {
                                             "df_address": "10.10.0.2",
                                             "metric": 0,
                                             "df_uptime": "00:03:49",
                                             "address": "10.10.0.2",
                                             "winner_metric": 0,
                                             "interface_name": "Loopback0"
                                        },
                                        "10.10.0.2 Ethernet3/4": {
                                             "df_address": "10.5.0.2",
                                             "metric": 0,
                                             "df_uptime": "00:03:49",
                                             "address": "10.10.0.2",
                                             "winner_metric": 0,
                                             "interface_name": "Ethernet3/4"
                                        },
                                        "10.10.0.3 Loopback0": {
                                             "df_address": "10.10.0.2",
                                             "metric": 409600,
                                             "df_uptime": "00:02:32",
                                             "address": "10.10.0.3",
                                             "winner_metric": 409600,
                                             "interface_name": "Loopback0"
                                        },
                                        "10.10.0.5 Loopback0": {
                                             "df_address": "10.10.0.2",
                                             "metric": 435200,
                                             "df_uptime": "00:02:16",
                                             "address": "10.10.0.5",
                                             "winner_metric": 435200,
                                             "interface_name": "Loopback0"
                                        },
                                        "10.10.0.5 Ethernet3/3": {
                                             "df_address": "10.4.0.4",
                                             "metric": 409600,
                                             "df_uptime": "00:01:49",
                                             "address": "10.10.0.5",
                                             "winner_metric": 409600,
                                             "interface_name": "Ethernet3/3"
                                        }
                                   }
                              }
                         }
                    }
               }
            }
        }
    }
    golden_output = {'execute.return_value': '''
        Interface          RP               DF Winner        Metric          Uptime
        Ethernet3/3        10.10.0.2        10.4.0.2         0               00:03:49
                           10.10.0.3        10.4.0.3         0               00:01:49
                           10.10.0.5        10.4.0.4         409600          00:01:49
        Ethernet3/4        10.10.0.2        10.5.0.2         0               00:03:49
                           10.10.0.3        10.5.0.2         409600          00:02:32
                           10.10.0.5        10.5.0.2         435200          00:02:16
        Loopback0          10.10.0.2        10.10.0.2        0               00:03:49
                           10.10.0.3        10.10.0.2        409600          00:02:32
                           10.10.0.5        10.10.0.2        435200          00:02:16   
    '''}

    parsed_output_1 = {
        "vrf": {
            "VRF1": {
               "address_family": {
                    "ipv4": {
                         "rp": {
                              "bidir": {
                                   "interface_df_election": {
                                        "10.186.0.1 Tunnel9": {
                                             "address": "10.186.0.1",
                                             "interface_name": "Tunnel9",
                                             "metric": 20,
                                             "df_address": "0.0.0.0",
                                             "df_uptime": "00:00:00",
                                             "winner_metric": 20
                                        },
                                        "10.186.0.1 Ethernet0/1": {
                                             "address": "10.186.0.1",
                                             "interface_name": "Ethernet0/1",
                                             "metric": 20,
                                             "df_address": "10.4.0.4",
                                             "df_uptime": "00:00:39",
                                             "winner_metric": 20
                                        }
                                   }
                              }
                         }
                    }
                }
            }
        }
    }
    golden_output_1 = {'execute.return_value': '''
        * implies this system is the DF
        Interface                RP               DF Winner        Metric     Uptime
        Tunnel9                  10.186.0.1       0.0.0.0          20         00:00:00
        Ethernet0/1              10.186.0.1      *10.4.0.4         20         00:00:39   
    '''}
    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpPimInterfaceDf(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_default_vrf(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowIpPimInterfaceDf(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.parsed_output)

    def test_golden_vrf(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowIpPimInterfaceDf(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output, self.parsed_output_1)


if __name__ == '__main__':
    unittest.main()