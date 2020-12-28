"""
Module:
    genie.libs.parser.ironware.tests.test_show_mpls_lsp

Author:
    James Di Trapani <james@ditrapani.com.au> - https://github.com/jamesditrapani

Description:
    Unittest for show mpls lsp on devices running IronWare
"""

import unittest
from unittest.mock import Mock

from pyats.topology import Device
from pyats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                             SchemaMissingKeyError

from genie.libs.parser.ironware.show_mpls import ShowMPLSLSP


class test_show_mpls_lsp(unittest.TestCase):
    '''Unit test for show mpls lsp '''

    device = Device(name='mlx8')

    empty_output = {'execute.return_value': ''}
    golden_parsed_output_brief = expected_output = {
    'lsps': {
        'mlx8.1_to_ces.2': {
        'destination': '1.1.1.1',
        'admin': 'UP',
        'operational': 'UP',
        'flap_count': 1,
        'retry_count': 0,
        'tunnel_interface': 'tnl0'
        },
        'mlx8.1_to_ces.1': {
        'destination': '2.2.2.2',
        'admin': 'UP',
        'operational': 'UP',
        'flap_count': 1,
        'retry_count': 0,
        'tunnel_interface': 'tnl56'
        },
        'mlx8.1_to_mlx8.2': {
        'destination': '3.3.3.3',
        'admin': 'UP',
        'operational': 'UP',
        'flap_count': 1,
        'retry_count': 0,
        'tunnel_interface': 'tnl63'
        },
        'mlx8.1_to_mlx8.3': {
        'destination': '4.4.4.4',
        'admin': 'DOWN',
        'operational': 'DOWN',
        'flap_count': 0,
        'retry_count': 0
        }
    }
}

    golden_output_brief = {
    'execute.return_value': '''
      Note: LSPs marked with * are taking a Secondary Path
                                                                        Admin Oper  Tunnel   Up/Dn Retry Active
      Name                                              To              State State Intf     Times No.   Path
      mlx8.1_to_ces.2                                   1.1.1.1  UP    UP    tnl0     1     0     --   
      mlx8.1_to_ces.1                                   2.2.2.2   UP    UP    tnl56    1     0     --   
      mlx8.1_to_mlx8.2                                  3.3.3.3   UP    UP    tnl63    1     0     --   
      mlx8.1_to_mlx8.3                                  4.4.4.4   DOWN  DOWN  --       0     0     --
    '''
  }

    def test_show_mpls_lsp(self):
        self.device = Mock(**self.golden_output_brief)
        obj = ShowMPLSLSP(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_brief)

if __name__ == '__main__':
    unittest.main() 