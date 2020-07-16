# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError
from genie.libs.parser.junos.show_bfd import (
    ShowBFDSession, ShowBFDSessionDetail)


# =================================
# Unit test for 'show bfd session'
# =================================
class TestShowBFDSession(unittest.TestCase):
    '''unit test for "show bfd session'''
    device = Device(name='aDevice')
    maxDiff = None

    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'bfd-session-information': {
            'bfd-session': [{
                'session-adaptive-multiplier': '3',
                'session-detection-time': '1.500',
                'session-neighbor': '10.0.0.1',
                'session-state': 'Up',
                'session-transmission-interval': '0.500'
            }, {
                'session-adaptive-multiplier': '3',
                'session-detection-time': '1.500',
                'session-interface': 'ge-0/0/0.0',
                'session-neighbor': '10.0.0.2',
                'session-state': 'Up',
                'session-transmission-interval': '0.500'
            }]
        }
    }

    golden_output = {
        'execute.return_value':
        '''
        Address                  State     Interface      Time     Interval  Multiplier
        10.0.0.1             Up                       1.500     0.500        3
        10.0.0.2               Up        ge-0/0/0.0     1.500     0.500        3
        '''
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowBFDSession(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowBFDSession(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


class TestShowBFDSessionDetail(unittest.TestCase):
    '''unit test for "show bfd session {ipaddress} detail'''

    device = Device(name='aDevice')
    maxDiff = None

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value':'''
    show bfd session address 10.34.2.250 detail
                                                      Detect   Transmit
    Address                  State     Interface      Time     Interval  Multiplier
    10.34.2.250             Up                       1.500     0.500        3
     Client LDP-OAM, TX interval 0.050, RX interval 0.050
     Session up time 00:02:46
     Local diagnostic None, remote diagnostic None
     Remote state Up, version 1
     Session type: Multi hop BFD
    
    1 sessions, 1 clients
    Cumulative transmit rate 2.0 pps, cumulative receive rate 2.0 pps    
    '''}
    golden_parsed_output = {
        "bfd-session-information": {
            "bfd-session": {
                "bfd-client": {
                    "client-name": "LDP-OAM",
                    "client-reception-interval": "0.050",
                    "client-transmission-interval": "0.050"
                },
                "local-diagnostic": "None",
                "remote-diagnostic": "None",
                "remote-state": "Up",
                "session-adaptive-multiplier": "3",
                "session-detection-time": "1.500",
                "session-neighbor": "10.34.2.250",
                "session-state": "Up",
                "session-transmission-interval": "0.500",
                "session-type": "Multi hop BFD",
                "session-up-time": "00:02:46",
                "session-version": "1"
            },
            "clients": "1",
            "cumulative-reception-rate": "2.0",
            "cumulative-transmission-rate": "2.0",
            "sessions": "1"
        }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowBFDSessionDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(ipaddress='')

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowBFDSessionDetail(device=self.device)
        parsed_output = obj.parse(ipaddress='10.34.2.250')
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == '__main__':
    unittest.main()
