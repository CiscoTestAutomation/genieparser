"""
Module:
    genie.libs.parser.ironware.tests.test_show_ip_route

Author:
    James Di Trapani <james@ditrapani.com.au> - https://github.com/jamesditrapani

Description:
    Unittest for show ip route on devices running IronWare
"""

import unittest
from unittest.mock import Mock

from pyats.topology import Device
from pyats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                             SchemaMissingKeyError

from genie.libs.parser.ironware.show_routing import ShowIPRoute

__author__ = 'James Di Trapani <james@ditrapani.com.au>'


class test_show_ip_route(unittest.TestCase):
    '''Unit test for show ip route '''

    device = Device(name='mlx8')

    empty_output = {'execute.return_value': ''}
    golden_parsed_output_brief = {
    'total_routes': 13,
    'routes': {
      '10.200.0.12/30': {
        'network': '10.200.0.12',
        'cidr': 30,
        'via': {
          '10.254.248.10': {
            'interface': 'eth 2/2',
            'cost': '110/28',
            'type': 'O',
            'uptime': '40d0h',
            'src-vrf': '-'
          }
        }
      },
      '10.200.0.16/30': {
        'network': '10.200.0.16',
        'cidr': 30,
        'via': {
          '10.254.248.10': {
            'interface': 'eth 2/2',
            'cost': '110/194',
            'type': 'O',
            'uptime': '6d12h',
            'src-vrf': '-'
          }
        }
      },
      '10.200.0.28/30': {
        'network': '10.200.0.28',
        'cidr': 30,
        'via': {
          '10.254.248.10': {
            'interface': 'eth 2/2',
            'cost': '110/138',
            'type': 'O',
            'uptime': '40d0h',
            'src-vrf': '-'
          }
        }
      },
      '10.200.0.32/30': {
        'network': '10.200.0.32',
        'cidr': 30,
        'via': {
          '10.254.248.10': {
            'interface': 'eth 2/2',
            'cost': '110/36',
            'type': 'O',
            'uptime': '40d0h',
            'src-vrf': '-'
          }
        }
      },
      '10.200.0.56/30': {
        'network': '10.200.0.56',
        'cidr': 30,
        'via': {
          '10.254.248.10': {
            'interface': 'eth 2/2',
            'cost': '110/36',
            'type': 'O',
            'uptime': '12d4h',
            'src-vrf': '-'
          }
        }
      },
      '10.200.0.60/30': {
        'network': '10.200.0.60',
        'cidr': 30,
        'via': {
          '10.254.248.10': {
            'interface': 'eth 2/2',
            'cost': '110/38',
            'type': 'O',
            'uptime': '40d0h',
            'src-vrf': '-'
          }
        }
      },
      '10.200.0.65/32': {
        'network': '10.200.0.65',
        'cidr': 32,
        'via': {
          '10.254.248.10': {
            'interface': 'eth 2/2',
            'cost': '110/63',
            'type': 'O',
            'uptime': '40d0h',
            'src-vrf': '-'
          }
        }
      },
      '10.200.0.73/32': {
        'network': '10.200.0.73',
        'cidr': 32,
        'via': {
          '10.254.248.10': {
            'interface': 'eth 2/2',
            'cost': '110/73',
            'type': 'O',
            'uptime': '40d0h',
            'src-vrf': '-'
          }
        }
      },
      '10.200.0.80/30': {
        'network': '10.200.0.80',
        'cidr': 30,
        'via': {
          '10.254.248.10': {
            'interface': 'eth 2/2',
            'cost': '110/76',
            'type': 'O',
            'uptime': '1d1h',
            'src-vrf': '-'
          }
        }
      },
      '10.200.0.85/32': {
        'network': '10.200.0.85',
        'cidr': 32,
        'via': {
          '10.254.248.10': {
            'interface': 'eth 2/2',
            'cost': '110/27',
            'type': 'O',
            'uptime': '40d0h',
            'src-vrf': '-'
          }
        }
      },
      '200.200.200.200/32': {
        'network': '200.200.200.200',
        'cidr': 32,
        'via': {
          'DIRECT': {
            'interface': 'loopback 1',
            'cost': '0/0',
            'type': 'D',
            'uptime': '248d',
            'src-vrf': 'Unknown'
          }
        }
      },
      '1.1.1.1/32': {
        'network': '1.1.1.1',
        'cidr': 32,
        'via': {
          '10.254.251.2': {
            'interface': 'eth 5/1',
            'cost': '110/52',
            'type': 'O',
            'uptime': '15h47m',
            'src-vrf': '-'
          },
          '10.254.251.108': {
            'interface': 'eth 7/1',
            'cost': '110/52',
            'type': 'O',
            'uptime': '15h47m',
            'src-vrf': '-'
          }
        }
      },
      '2.2.2.2/32': {
        'network': '2.2.2.2',
        'cidr': 32,
        'via': {
          '10.254.251.2': {
            'interface': 'eth 5/1',
            'cost': '110/42',
            'type': 'O',
            'uptime': '15h47m',
            'src-vrf': '-'
          },
          '10.254.251.108': {
            'interface': 'eth 7/1',
            'cost': '110/42',
            'type': 'O',
            'uptime': '15h47m',
            'src-vrf': '-'
          }
        }
      }
    }
  }

    golden_output_brief = {
    'execute.return_value': '''
      Total number of IP routes: 13
      Type Codes - B:BGP D:Connected I:ISIS O:OSPF R:RIP S:Static; Cost - Dist/Metric
      BGP  Codes - i:iBGP e:eBGP
      ISIS Codes - L1:Level-1 L2:Level-2
      OSPF Codes - i:Inter Area 1:External Type 1 2:External Type 2 s:Sham Link
      STATIC Codes - d:DHCPv6
              Destination        Gateway         Port           Cost          Type Uptime src-vrf
      1       10.200.0.12/30     10.254.248.10   eth 2/2        110/28        O    40d0h  -
      2       10.200.0.16/30     10.254.248.10   eth 2/2        110/194       O    6d12h  -
      3       10.200.0.28/30     10.254.248.10   eth 2/2        110/138       O    40d0h  -
      4       10.200.0.32/30     10.254.248.10   eth 2/2        110/36        O    40d0h  -
      5       10.200.0.56/30     10.254.248.10   eth 2/2        110/36        O    12d4h  -
      6       10.200.0.60/30     10.254.248.10   eth 2/2        110/38        O    40d0h  -
      7       10.200.0.65/32     10.254.248.10   eth 2/2        110/63        O    40d0h  -
      8       10.200.0.73/32     10.254.248.10   eth 2/2        110/73        O    40d0h  -
      9       10.200.0.80/30     10.254.248.10   eth 2/2        110/76        O    1d1h   -
      10      10.200.0.85/32     10.254.248.10   eth 2/2        110/27        O    40d0h  -
      11     200.200.200.200/32   DIRECT          loopback 1     0/0           D    248d   
      -
      12      1.1.1.1/32         10.254.251.2    eth 5/1       110/52        O    15h47m -
              1.1.1.1/32         10.254.251.108  eth 7/1       110/52        O    15h47m -
      13      2.2.2.2/32         10.254.251.2    eth 5/1       110/42        O    15h47m -
              2.2.2.2/32         10.254.251.108  eth 7/1       110/42        O    15h47m -
    '''
  }

    def test_show_ip_route(self):
        self.device = Mock(**self.golden_output_brief)
        obj = ShowIPRoute(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_brief)

if __name__ == '__main__':
    unittest.main() 