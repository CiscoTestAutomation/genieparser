import re
import unittest
from unittest.mock import Mock

from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError

from genie.libs.parser.asa.show_interface import ShowInterfaceSummary


class test_show_interface(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'interfaces': {
            'Vlan1000': {
                'name': 'pod100',
                'oper_status': 'up',
                'protocol_status': 'up',
                'mac_address': '286f.7fb1.032c',
                'mtu': 1500,
                'ip_address': '172.16.100.251',
                'subnet': '255.255.255.0'
            }
        }
    }

    golden_output = {'execute.return_value': '''
		Interface Vlan1000 "pod100", is up, line protocol is up
		MAC address 286f.7fb1.032c, MTU 1500
		IP address 172.16.100.251, subnet mask 255.255.255.0
	'''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        interface_obj = ShowInterfaceSummary(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = interface_obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        interface_obj = ShowInterfaceSummary(device=self.device)
        parsed_output = interface_obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == '__main__':
    unittest.main()
