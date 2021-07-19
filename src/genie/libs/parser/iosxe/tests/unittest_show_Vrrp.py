# Import the Python mock functionality
import unittest
from unittest.mock import Mock

# pyATS
from pyats.topology import Device
from pyats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

# iosxe show_vrrp
from genie.libs.parser.iosxe.show_vrrp import ShowVrrpAll

# =================================
# Unit test for 'show lisp session'
# =================================
class test_show_vrrp_session(unittest.TestCase):

    '''Unit test for "show lisp session"'''

    empty_output = {'execute.return_value': ''}

    # Specify the expected result for the parsed output
    golden_parsed_output1 = {
            'interface' : {
                'GigabitEthernet1/0/19': {
            'group': {
                1: {
                    'description': 'single_Vrrp',
                    'state': 'MASTER',
                    'virtual_ip_address': '10.50.10.104',
                    'virtual_mac_address': '0000.5E00.0101',
                    'advertise_interval_secs': 1.0,
                    'preemption': 'enabled',
                    'priority': 100,
                    'master_router_ip': '10.50.10.106',
                    'master_router': 'local',
                    'master_router_priority': 100,
                    'master_advertisement_interval_secs': 1.0,
                    'master_advertisement_expiration_secs': 0.441,
                    'master_down_interval_secs': 'unknown',
                    'flags': '1/1'
                },
            },
        },
    } }

    # Specify the expected unparsed output
    golden_output1 = {'execute.return_value': '''
        GigabitEthernet1/0/19 - Group 1 - Address-Family IPv4
        Description is "single_Vrrp"
        State is MASTER
        State duration 23.134 secs
        Virtual IP address is 10.50.10.104
        Virtual MAC address is 0000.5E00.0101
        Advertisement interval is 1000 msec
        Preemption enabled
        Priority is 100
        State change reason:2
        Tloc preference not configured, value 0
        Master Router is 10.50.10.106 (local), priority is 100
        Master Advertisement interval is 1000 msec (expires in 441 msec)
        Master Down interval is unknown
        FLAGS: 1/1
        '''}

    def test_show_vrrp_session_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowVrrpAll(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_vrrp_session_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowVrrpAll(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

if __name__ == '__main__':
    unittest.main()
