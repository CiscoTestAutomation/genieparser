"""
Module:
    genie.libs.parser.ironware.tests.test_show_mpls_vll

Author:
    James Di Trapani <james@ditrapani.com.au> - https://github.com/jamesditrapani

Description:
    Unittest for show mpls vll {vll} on devices running IronWare
"""

import unittest
from unittest.mock import Mock

from pyats.topology import Device
from pyats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                             SchemaMissingKeyError

from genie.libs.parser.ironware.show_mpls import ShowMPLSVLL


class test_show_mpls_vll(unittest.TestCase):
    '''Unit test for show mpls vll {vll} '''

    device = Device(name='mlx8')

    empty_output = {'execute.return_value': ''}
    golden_parsed_output_brief = expected_output = {
    'vll': {
        'MY-FIRST-VLL': {
            'vcid': 2456,
            'vll_index': 2,
            'local': {
                'type': 'tagged',
                'interface': 'ethernet 2/5',
                'vlan_id': 3043,
                'state': 'Up',
                'mct_state': 'None',
                'ifl_id': '--',
                'vc_type': 'tag',
                'mtu': 9190,
                'cos': '--',
                'extended_counters': True,
                'counters': False
            },
            'peer': {
                'ip': '192.168.1.1',
                'state': 'UP',
                'vc_type': 'tag',
                'mtu': 9190,
                'local_label': 852217,
                'remote_label': 852417,
                'local_group_id': 0,
                'remote_group_id': 0,
                'tunnel_lsp': {
                    'name': 'mlx8.1_to_ces.2',
                    'tunnel_interface': 'tnl15'
                },
                'lsps_assigned': 'No LSPs assigned'
            }
        }
    }
}

    golden_output_brief = {
    'execute.return_value': '''
VLL MY-FIRST-VLL, VC-ID 2456, VLL-INDEX 2

  End-point        : tagged  vlan 3043  e 2/5
  End-Point state  : Up
  MCT state        : None
  IFL-ID           : --
  Local VC type    : tag
  Local VC MTU     : 9190
  COS              : --
  Extended Counters: Enabled
  Counter          : disabled

  Vll-Peer         : 192.168.1.1
      State          : UP
      Remote VC type : tag               Remote VC MTU  : 9190
      Local label    : 852217            Remote label   : 852417
      Local group-id : 0                 Remote group-id: 0
      Tunnel LSP     : mlx8.1_to_ces.2 (tnl15)
      MCT Status TLV : --
      LSPs assigned  : No LSPs assigned
    '''
  }

    def test_show_mpls_vll(self):
        self.device = Mock(**self.golden_output_brief)
        obj = ShowMPLSVLL(device=self.device)
        parsed_output = obj.parse(vll='MY-FIRST-VLL')
        self.assertEqual(parsed_output, self.golden_parsed_output_brief)

if __name__ == '__main__':
    unittest.main() 