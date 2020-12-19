
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
from genie.libs.parser.dellos6.show_ip_interface import ShowIPInterface


class test_show_ip_interface(unittest.TestCase):
    '''Unit test for "show ip ospf interface brief" '''

    device = Device(name='aDevice')
    
    empty_output = {'execute.return_value': ''}
    golden_parsed_output_brief = {
    'ints': {
        'gateway': '0.0.0.0',
        'L3_MAC': 'F8B1.5683.8734',
        'Vl1': {
            'state': 'Down',
            'ip_address': '10.10.10.216',
            'mask': '255.255.255.0',
            'method': 'DHCP'
        },
        'Vl20': {
            'state': 'Up',
            'ip_address': '10.10.21.70',
            'mask': '255.255.255.0',
            'method': 'DHCP'
        }
    }
}

    golden_output_brief = {'execute.return_value': '''
    Default Gateway................................ 0.0.0.0
    L3 MAC Address................................. F8B1.5683.8734

    Routing Interfaces:

    Interface    State   IP Address      IP Mask         Method
    ----------   -----   --------------- --------------- -------
    Vl1          Down    10.10.10.216    255.255.255.0   DHCP
    Vl20         Up      10.10.21.70     255.255.255.0   DHCP
    '''}

    def test_show_ip_interface(self):
        self.device = Mock(**self.golden_output_brief)
        obj = ShowIPInterface(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_brief)

if __name__ == '__main__':
    unittest.main()