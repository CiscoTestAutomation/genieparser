# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError
from genie.libs.parser.junos.show_ldp import (
    ShowLDPSession, ShowLdpNeighbor, ShowLdpDatabaseSessionIpaddress)


# =================================
# Unit test for 'show ldp session'
# =================================
class TestShowLDPSession(unittest.TestCase):
    '''unit test for "show ldp session'''
    device = Device(name='aDevice')
    maxDiff = None

    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'ldp-session-information': {
            'ldp-session': [{
                'ldp-neighbor-address': '10.34.2.250',
                'ldp-session-state': 'Operational',
                'ldp-connection-state': 'Open',
                'ldp-remaining-time': '26',
                'ldp-session-adv-mode': 'DU'
            }]
        }
    }

    golden_output = {
        'execute.return_value':
        '''
          Address                           State       Connection  Hold time  Adv. Mode
        10.34.2.250                        Operational Open          26         DU
        '''
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowLDPSession(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowLDPSession(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


# =================================
# Unit test for 'show ldp neighbor'
# =================================
class TestShowLDPSession(unittest.TestCase):
    '''unit test for "show ldp session'''
    device = Device(name='aDevice')
    maxDiff = None

    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
            'ldp-neighbor-information': 
                {'ldp-neighbor': [
                    {'interface-name': 'ge-0/0/0.0',
                     'ldp-label-space-id': '10.34.2.250:0',
                     'ldp-neighbor-address': '10.169.14.158',
                     'ldp-remaining-time': '14'
                     }
                ]
            }
    }

    golden_output = {
        'execute.return_value':
        '''
          show ldp neighbor
        Address                             Interface       Label space ID     Hold time
        10.169.14.158                      ge-0/0/0.0      10.34.2.250:0       14
        '''
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowLdpNeighbor(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowLdpNeighbor(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


# =================================
# Unit test for 'show ldp database session ipaddress'
# =================================
class TestShowLDPSession(unittest.TestCase):
    '''unit test for "show ldp database session ipaddress'''
    device = Device(name='aDevice')
    maxDiff = None

    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        "ldp-database-information": {
        "ldp-database": [
            {
                "ldp-binding": [
                    {
                        "ldp-label": "3",
                        "ldp-prefix": "10.34.2.250/32"
                    },
                    {
                        "ldp-label": "16",
                        "ldp-prefix": "10.169.14.240/32"
                    }
                ],
                "ldp-database-type": "Input label database",
                "ldp-label-received": "2",
                "ldp-session-id": "10.169.14.240:0--10.34.2.250:0"
            },
            {
                "ldp-binding": [
                    {
                        "ldp-label": "16",
                        "ldp-prefix": "10.34.2.250/32"
                    },
                    {
                        "ldp-label": "3",
                        "ldp-prefix": "10.169.14.240/32"
                    }
                ],
                "ldp-database-type": "Output label database",
                "ldp-label-advertised": "2",
                "ldp-session-id": "10.169.14.240:0--10.34.2.250:0"
            }
        ]
    }
    }

    golden_output = {
        'execute.return_value':
        '''
          show ldp database 10.34.2.250 
        Input label database, 10.169.14.240:0--10.34.2.250:0
        Labels received: 2
        Label     Prefix
            3      10.34.2.250/32
            16      10.169.14.240/32

        Output label database, 10.169.14.240:0--10.34.2.250:0
        Labels advertised: 2
        Label     Prefix
            16      10.34.2.250/32
            3      10.169.14.240/32
        '''
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowLdpDatabaseSessionIpaddress(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowLdpDatabaseSessionIpaddress(device=self.device)
        parsed_output = obj.parse(ipaddress='10.34.2.250')
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == '__main__':
    unittest.main()
