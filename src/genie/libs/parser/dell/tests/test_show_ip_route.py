
# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device
from pyats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                             SchemaMissingKeyError

# iosxe show_ospf
from genie.libs.parser.dell.show_ip_route import ShowIPRoute


class test_show_ip_route(unittest.TestCase):
    '''Unit test for "show ip ospf interface brief" '''

    device = Device(name='aDevice')
    
    empty_output = {'execute.return_value': ''}
    golden_parsed_output_brief = {
    'routes': {
        'route-0_0_0_0': {
            'source_proto': 'S',
            'is_preferred': True,
            'prefix': '0.0.0.0/0',
            'subnet': '0.0.0.0',
            'mask': '0',
            'admin_dist': 254,
            'metric': 1,
            'next_hop': '10.10.21.1',
            'vlan': '20'
        },
        'route-10_10_21_0': {
            'source_proto': 'C',
            'is_preferred': True,
            'prefix': '10.10.21.0/24',
            'subnet': '10.10.21.0',
            'mask': '24',
            'admin_dist': 0,
            'metric': 0,
            'next_hop': 'connected',
            'vlan': '20'
        }
    }
}

    golden_output_brief = {'execute.return_value': '''
    S      *0.0.0.0/0 [254/1] via 10.10.21.1,   02d:06h:00m,  Vl20
    C      *10.10.21.0/24 [0/0] directly connected,   Vl20
    '''}

    def test_show_ip_route(self):
        self.device = Mock(**self.golden_output_brief)
        obj = ShowIPRoute(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_brief)

if __name__ == '__main__':
    unittest.main()