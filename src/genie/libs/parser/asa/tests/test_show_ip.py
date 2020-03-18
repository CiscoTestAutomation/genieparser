import unittest
from unittest.mock import Mock

# PyATS
from pyats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

from genie.libs.parser.asa.show_ip import (ShowIpLocalPool)

# ============================================
# unit test for 'show ip local pool {pool}'
# =============================================
class TestShowIpLocalPool(unittest.TestCase):
    '''
       unit test for show ip local pool {pool}
    '''
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    maxDiff = None
    golden_parsed_output = {
        'available_addresses': ['192.168.1.145', '192.168.1.146'],
        'begin': {
            '192.168.1.144': {
                'end': {
                    '192.168.1.147': {
                        'free': 2,
                        'held': 0,
                        'in_use': 2,
                        'mask': '255.255.255.252',
                    },
                },
            },
        },
        'in_use_addresses': ['192.168.1.144', '192.168.1.147'],
    }

    golden_output = {'execute.return_value': '''
        show ip local pool Colich-pool 
        Begin           End             Mask            Free     Held     In use
        192.168.1.144   192.168.1.147   255.255.255.252     2        0        2

        Available Addresses:
        192.168.1.145
        192.168.1.146

        In Use Addresses:
        192.168.1.144
        192.168.1.147
          '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpLocalPool(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(pool='Colich-pool')

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        route_obj = ShowIpLocalPool(device=self.device)
        parsed_output = route_obj.parse(pool='Colich-pool')
        self.assertEqual(parsed_output, self.golden_parsed_output)

if __name__ == '__main__':
    unittest.main()