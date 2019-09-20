# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
    SchemaMissingKeyError

# Parser
from genie.libs.parser.iosxe.show_ip_vrf import ShowIpVrf, ShowIpVrfDetail


# ============================================
# Unit test for 
#    * 'show ip vrf '
#    * 'show ip vrf <vrf> '
#    * 'show ip vrf detail'
#    * 'show ip vrf detail <vrf> '
# ============================================


class test_show_ip_vrf(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'vrf': {
            'Mgmt-intf': {
                'interfaces': ['GigabitEthernet1'],
            },
            'VRF1': {
                'route_distinguisher': '65000:1',
                'interfaces': ['Tunnel1',
                               'Loopback300',
                               'GigabitEthernet2.390',
                               'GigabitEthernet2.410',
                               'GigabitEthernet2.415',
                               'GigabitEthernet2.420',
                               'GigabitEthernet3.390',
                               'GigabitEthernet3.410',
                               'GigabitEthernet3.415',
                               'GigabitEthernet3.420',
                               'Tunnel3',
                               'Tunnel4',
                               'Tunnel6',
                               'Tunnel8'],
                },
            },
        }

    golden_output = {'execute.return_value': '''
        R1_xe#show ip vrf
        Name                         Default RD            Interfaces
        Mgmt-intf                    <not set>             Gi1
        VRF1                         65000:1               Tu1
                                                           Lo300
                                                           Gi2.390
                                                           Gi2.410
                                                           Gi2.415
                                                           Gi2.420
                                                           Gi3.390
                                                           Gi3.410
                                                           Gi3.415
                                                           Gi3.420
                                                           Tu3
                                                           Tu4
                                                           Tu6
                                                           Tu8 
    '''}

    golden_parsed_output1 = {
        'vrf': {
            'VRF1': {
                'route_distinguisher': '65000:1',
                'interfaces': ['Tunnel1',
                               'Loopback300',
                               'GigabitEthernet2.390',
                               'GigabitEthernet2.410',
                               'GigabitEthernet2.415',
                               'GigabitEthernet2.420',
                               'GigabitEthernet3.390',
                               'GigabitEthernet3.410',
                               'GigabitEthernet3.415',
                               'GigabitEthernet3.420',
                               'Tunnel3',
                               'Tunnel4',
                               'Tunnel6',
                               'Tunnel8'],
            },
        },
    }

    golden_output1 = {'execute.return_value': '''
    R1_xe#show ip vrf VRF1
    Name                             Default RD          Interfaces
    VRF1                         65000:1                 Tu1
                                                         Lo300
                                                         Gi2.390
                                                         Gi2.410
                                                         Gi2.415
                                                         Gi2.420
                                                         Gi3.390
                                                         Gi3.410
                                                         Gi3.415
                                                         Gi3.420
                                                         Tu3
                                                         Tu4
                                                         Tu6
                                                         Tu8 
    '''
                      }

    golden_parsed_output2 = {
        'vrf': {
            'Mgmt-intf': {
                'interfaces': ['GigabitEthernet1'],
            },
        },
    }

    golden_output2 = {'execute.return_value': '''
        R1_xe#show ip vrf Mgmt-intf
        Name                             Default RD            Interfaces
        Mgmt-intf                        <not set>             Gi1
    '''
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpVrf(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowIpVrf(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_empty1(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpVrf(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(vrf='VRF1')

    def test_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowIpVrf(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_empty2(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpVrf(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(vrf='Mgmt-intf')

    def test_golden2(self):
        self.device = Mock(**self.golden_output2)
        obj = ShowIpVrf(device=self.device)
        parsed_output = obj.parse(vrf='Mgmt-intf')
        self.assertEqual(parsed_output, self.golden_parsed_output2)


class test_show_ip_vrf_detail(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
      'Mgmt-intf': {
          'address_family': {
              'ipv4 unicast': {
                  'flags': '0x0',
                  'table_id': '0x1',
                  'vrf_label': {
                      'allocation_mode': 'per-prefix',
                      },
                  },
              },
          'cli_format': 'New',
          'flags': '0x1808',
          'interface': {
              'GigabitEthernet1': {
                  'vrf': 'Mgmt-intf',
                  },
              },
          'interfaces': ['GigabitEthernet1'],
          'support_af': 'multiple address-families',
          'vrf_id': 1,
          },
      'VRF1': {
          'address_family': {
              'ipv4 unicast': {
                  'flags': '0x0',
                  'table_id': '0x2',
                  'vrf_label': {
                      'allocation_mode': 'per-prefix',
                      'distribution_protocol': 'LDP',
                      },
                  },
              },
          'cli_format': 'New',
          'flags': '0x180C',
          'interface': {
              'GigabitEthernet2.390': {
                  'vrf': 'VRF1',
                  },
              'GigabitEthernet2.410': {
                  'vrf': 'VRF1',
                  },
              'GigabitEthernet2.415': {
                  'vrf': 'VRF1',
                  },
              'GigabitEthernet2.420': {
                  'vrf': 'VRF1',
                  },
              'GigabitEthernet3.390': {
                  'vrf': 'VRF1',
                  },
              'GigabitEthernet3.410': {
                  'vrf': 'VRF1',
                  },
              'GigabitEthernet3.415': {
                  'vrf': 'VRF1',
                  },
              'GigabitEthernet3.420': {
                  'vrf': 'VRF1',
                  },
              'Loopback300': {
                  'vrf': 'VRF1',
                  },
              'Tunnel1': {
                  'vrf': 'VRF1',
                  },
              'Tunnel3': {
                  'vrf': 'VRF1',
                  },
              'Tunnel4': {
                  'vrf': 'VRF1',
                  },
              'Tunnel6': {
                  'vrf': 'VRF1',
                  },
              'Tunnel8': {
                  'vrf': 'VRF1',
                  },
              },
          'interfaces': ['Tunnel1', 'Loopback300', 'GigabitEthernet2.390', 
                         'GigabitEthernet2.410', 'GigabitEthernet2.415', 
                         'GigabitEthernet2.420', 'GigabitEthernet3.390', 
                         'GigabitEthernet3.410', 'GigabitEthernet3.415', 
                         'GigabitEthernet3.420', 'Tunnel3', 'Tunnel4', 
                         'Tunnel6', 'Tunnel8'],
          'route_distinguisher': '65000:1',
          'support_af': 'multiple address-families',
          'vrf_id': 2,
          },
      }

    golden_output = {'execute.return_value': '''
        R1_xe#show ip vrf detail
        VRF Mgmt-intf (VRF Id = 1); default RD <not set>; default VPNID <not set>
          New CLI format, supports multiple address-families
          Flags: 0x1808
          Interfaces:
            Gi1                     
        Address family ipv4 unicast (Table ID = 0x1):
          Flags: 0x0
          No Export VPN route-target communities
          No Import VPN route-target communities
          No import route-map
          No global export route-map
          No export route-map
          VRF label distribution protocol: not configured
          VRF label allocation mode: per-prefix
        
        VRF VRF1 (VRF Id = 2); default RD 65000:1; default VPNID <not set>
          New CLI format, supports multiple address-families
          Flags: 0x180C
          Interfaces:
            Tu1                      Lo300                    Gi2.390                 
            Gi2.410                  Gi2.415                  Gi2.420                 
            Gi3.390                  Gi3.410                  Gi3.415                 
            Gi3.420                  Tu3                      Tu4                     
            Tu6                      Tu8                     
        Address family ipv4 unicast (Table ID = 0x2):
          Flags: 0x0
          No Export VPN route-target communities
          No Import VPN route-target communities
          No import route-map
          No global export route-map
          No export route-map
          VRF label distribution protocol: LDP
          VRF label allocation mode: per-prefix
  '''}

    golden_parsed_output1 = {
      'Mgmt-intf': {
          'address_family': {
              'ipv4 unicast': {
                  'flags': '0x0',
                  'table_id': '0x1',
                  'vrf_label': {
                      'allocation_mode': 'per-prefix',
                      },
                  },
              },
          'cli_format': 'New',
          'flags': '0x1808',
          'interface': {
              'GigabitEthernet1': {
                  'vrf': 'Mgmt-intf',
                  },
              },
          'interfaces': ['GigabitEthernet1'],
          'support_af': 'multiple address-families',
          'vrf_id': 1,
          },
      }

    golden_output1 = {'execute.return_value': '''
    R1_xe#show ip vrf detail Mgmt-intf
    VRF Mgmt-intf (VRF Id = 1); default RD <not set>; default VPNID <not set>
      New CLI format, supports multiple address-families
      Flags: 0x1808
      Interfaces:
        Gi1                     
    Address family ipv4 unicast (Table ID = 0x1):
      Flags: 0x0
      No Export VPN route-target communities
      No Import VPN route-target communities
      No import route-map
      No global export route-map
      No export route-map
      VRF label distribution protocol: not configured
      VRF label allocation mode: per-prefix
    '''
    }

    golden_parsed_output2 = {
      'VRF1': {
          'address_family': {
              'ipv4 unicast': {
                  'flags': '0x0',
                  'table_id': '0x2',
                  'vrf_label': {
                      'allocation_mode': 'per-prefix',
                      'distribution_protocol': 'LDP',
                      },
                  },
              },
          'cli_format': 'New',
          'flags': '0x180C',
          'interface': {
              'GigabitEthernet2.390': {
                  'vrf': 'VRF1',
                  },
              'GigabitEthernet2.410': {
                  'vrf': 'VRF1',
                  },
              'GigabitEthernet2.415': {
                  'vrf': 'VRF1',
                  },
              'GigabitEthernet2.420': {
                  'vrf': 'VRF1',
                  },
              'GigabitEthernet3.390': {
                  'vrf': 'VRF1',
                  },
              'GigabitEthernet3.410': {
                  'vrf': 'VRF1',
                  },
              'GigabitEthernet3.415': {
                  'vrf': 'VRF1',
                  },
              'GigabitEthernet3.420': {
                  'vrf': 'VRF1',
                  },
              'Loopback300': {
                  'vrf': 'VRF1',
                  },
              'Tunnel1': {
                  'vrf': 'VRF1',
                  },
              'Tunnel3': {
                  'vrf': 'VRF1',
                  },
              'Tunnel4': {
                  'vrf': 'VRF1',
                  },
              'Tunnel6': {
                  'vrf': 'VRF1',
                  },
              'Tunnel8': {
                  'vrf': 'VRF1',
                  },
              },
          'interfaces': ['Tunnel1', 'Loopback300', 'GigabitEthernet2.390', 
                         'GigabitEthernet2.410', 'GigabitEthernet2.415', 
                         'GigabitEthernet2.420', 'GigabitEthernet3.390', 
                         'GigabitEthernet3.410', 'GigabitEthernet3.415', 
                         'GigabitEthernet3.420', 'Tunnel3', 'Tunnel4', 
                         'Tunnel6', 'Tunnel8'],
          'route_distinguisher': '65000:1',
          'support_af': 'multiple address-families',
          'vrf_id': 2,
          },
      }

    golden_output2 = {'execute.return_value': '''
    show ip vrf detail VRF1
    VRF VRF1 (VRF Id = 2); default RD 65000:1; default VPNID <not set>
      New CLI format, supports multiple address-families
      Flags: 0x180C
      Interfaces:
        Tu1                      Lo300                    Gi2.390
        Gi2.410                  Gi2.415                  Gi2.420
        Gi3.390                  Gi3.410                  Gi3.415
        Gi3.420                  Tu3                      Tu4
        Tu6                      Tu8
    Address family ipv4 unicast (Table ID = 0x2):
      Flags: 0x0
      No Export VPN route-target communities
      No Import VPN route-target communities
      No import route-map
      No global export route-map
      No export route-map
      VRF label distribution protocol: LDP
      VRF label allocation mode: per-prefix
    '''}

    golden_parsed_output3 = {
        "Mgmt-intf": {
            "vrf_id": 1,
            "cli_format": "New",
            "support_af": "multiple address-families",
            "flags": "0x1808",
            "interfaces": [
                "GigabitEthernet0"
            ],
            "interface": {
                "GigabitEthernet0": {
                    "vrf": "Mgmt-intf"
                }
            },
            "address_family": {
                "none": {
                    "table_id": "1",
                    "flags": "0x0",
                    "vrf_label": {
                        "allocation_mode": "per-prefix"
                    }
                }
            }
        }
    }
    golden_output3 = {'execute.return_value': '''
        show ip vrf detail
        VRF Mgmt-intf (VRF Id = 1); default RD <not set>; default VPNID <not set>
        New CLI format, supports multiple address-families
        Flags: 0x1808
        Interfaces:
            Gi0                     
        VRF Table ID = 1
        Flags: 0x0
        No Export VPN route-target communities
        No Import VPN route-target communities
        No import route-map
        No global export route-map
        No export route-map
        VRF label distribution protocol: not configured
        VRF label allocation mode: per-prefix
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpVrfDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowIpVrfDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_empty1(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpVrfDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(vrf='Mgmt-intf')

    def test_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowIpVrfDetail(device=self.device)
        parsed_output = obj.parse(vrf='Mgmt-intf')
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_empty2(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpVrfDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(vrf='VRF1')

    def test_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowIpVrfDetail(device=self.device)
        parsed_output = obj.parse(vrf='VRF1')
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_golden3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        obj = ShowIpVrfDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output3)


if __name__ == '__main__':
    unittest.main()
