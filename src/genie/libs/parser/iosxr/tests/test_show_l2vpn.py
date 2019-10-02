# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

# iosxr show_l2vpn_mac_learning
from genie.libs.parser.iosxr.show_l2vpn import (ShowL2vpnMacLearning)


# ===========================================
# Unit test for 'show l2vpn mac-learning <mac_type> all location <location>'
# ===========================================
class TestShowL2vpnMacLearning(unittest.TestCase):
    """Unit test for 'show l2vpn mac-learning <mac_type> all location <location>'"""

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    expected_output = {
        'topo_id': {
            '1': {
                'producer': {
                    '0/0/CPU0': {
                        'next_hop': {
                            'BE1.7': {
                                'mac_address': {
                                    '7777.7777.0002': {}}}}}}},
            '6': {
                'producer': {
                    '0/0/CPU0': {
                        'next_hop': {
                            'BV1': {
                                'mac_address': {
                                    '0000.f65a.357c': {
                                        'ip_address': 'fe80::200:f6ff:fe5a:357c'},
                                '1000.0001.0001': {
                                        'ip_address': '10.1.1.11'}}}}}}},
            '7': {
                'producer': {
                    '0/0/CPU0': {
                        'next_hop': {
                            'BV2': {
                                'mac_address': {
                                    '0000.f65a.3570': {
                                        'ip_address': '10.1.2.91'},
                                    '0000.f65a.357d': {
                                        'ip_address': '10.1.2.93'}}}}}}}}}

    device_output = {'execute.return_value': '''
        Topo ID  Producer  Next Hop(s)  Mac Address     IP Address

        6        0/0/CPU0   BV1        1000.0001.0001      10.1.1.11
        7        0/0/CPU0   BV2        0000.f65a.3570      10.1.2.91
        7        0/0/CPU0   BV2        0000.f65a.357d      10.1.2.93
        1        0/0/CPU0   BE1.7      7777.7777.0002
        6        0/0/CPU0   BV1        0000.f65a.357c      fe80::200:f6ff:fe5a:357c
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowL2vpnMacLearning(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output)
        obj = ShowL2vpnMacLearning(device=self.device)

        parsed_output = obj.parse()

        self.assertEqual(parsed_output, self.expected_output)


if __name__ == '__main__':
    unittest.main()
