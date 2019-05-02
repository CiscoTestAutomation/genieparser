# Python
import unittest
from unittest.mock import Mock
 
# ATS
from ats.topology import Device
from ats.topology import loader
 
# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError
 
# iosxe show_lisp
# from genie.libs.parser.iosxe.show_lisp import ShowLispSession

# iosxe show_ip_parser
from genie.libs.parser.iosxe.show_ip_parser import ShowIPAlias
 
# =================================
# Unit test for 'show ip alias', 'show ip aliases default-vrf', 'show ip aliases vrf {vrf}'
# =================================
class test_show_ip_alias(unittest.TestCase):
    ''' 
	Unit test for:
	show ip alias 
	show ip aliases default-vrf
	sshow ip aliases vrf {vrf}
	'''

    device = Device(name = 'aDevice')
    empty_output = { 'execute.return_value' : '' }

    # show ip alias
    golden_parsed_output1 = {
        'vrf': {
            '1': {
                'address_type': 'Interface',
                'ip_address': '106.162.197.94',
            },
            '2': {
                'address_type': 'Interface',
                'ip_address': '106.162.197.254',
            },
            '3': {
                'address_type': 'Interface',
                'ip_address': '172.16.1.56',
            },
            '4': {
                'address_type': 'Interface',
                'ip_address': '192.168.10.254',
            },
            '5': {
                'address_type': 'Interface',
                'ip_address': '192.168.10.2544',
            },
            '6': {
                'address_type': 'Interface',
                'ip_address': '192.168.10.254',
            },
            '7': {
                'address_type': 'Interface',
                'ip_address': '192.168.10.254',
            },
            '8': {
                'address_type': 'Interface',
                'ip_address': '192.168.10.254',
            },
            '9': {
                'address_type': 'Interface',
                'ip_address': '192.255.255.254',
            },
        },
    }

    golden_output1 = { 'execute.return_value': 
        '''
        Address Type             IP Address      Port
        Interface                106.162.197.94
        Interface                106.162.197.254
        Interface                172.16.1.56
        Interface                192.168.10.254
        Interface                192.168.10.254
        Interface                192.168.10.254
        Interface                192.168.10.254
        Interface                192.168.10.254
        Interface                192.255.255.254
        '''
    }

    # show ip aliases default-vrf
    golden_parsed_output2 = {
        'vrf': {
            '1': {
                'address_type': 'Interface',
                'ip_address': '106.162.197.94',
            },
            '2': {
                'address_type': 'Interface',
                'ip_address': '106.162.197.254',
            },
            '3': {
                'address_type': 'Interface',
                'ip_address': '172.16.1.56',
            },
            '4': {
                'address_type': 'Interface',
                'ip_address': '192.168.10.254',
            },
            '5': {
                'address_type': 'Interface',
                'ip_address': '192.168.10.2544',
            },
            '6': {
                'address_type': 'Interface',
                'ip_address': '192.168.10.254',
            },
            '7': {
                'address_type': 'Interface',
                'ip_address': '192.168.10.254',
            },
            '8': {
                'address_type': 'Interface',
                'ip_address': '192.168.10.254',
            },
            '9': {
                'address_type': 'Interface',
                'ip_address': '192.255.255.254',
            },
        },
    }

    golden_output2 = { 'execute.return_value': 
        '''
        Address Type             IP Address      Port
        Interface                106.162.197.94
        Interface                106.162.197.254
        Interface                172.16.1.56
        Interface                192.168.10.254
        Interface                192.168.10.254
        Interface                192.168.10.254
        Interface                192.168.10.254
        Interface                192.168.10.254
        Interface                192.255.255.254
        '''
    }

    # show ip aliases vrf {vrf}
    golden_parsed_output3 = {
        'vrf': {
            '1': {
                'address_type': 'Interface',
                'ip_address': '192.168.10.254',
            },
        },
    }

    golden_output3 = { 'execute.return_value': 
        '''
        Address Type             IP Address      Port
        Interface                192.168.10.254
        '''
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIPAlias(device = self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden2(self):
        self.device = Mock(**self.golden_output2)
        obj = ShowIPAlias(device = self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_golden3(self):
        self.device = Mock(**self.golden_output3)
        obj = ShowIPAlias(device = self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output3)
