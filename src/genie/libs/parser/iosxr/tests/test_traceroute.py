
# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device
from pyats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                             SchemaMissingKeyError

# iosxr traceroute
from genie.libs.parser.iosxr.traceroute import Traceroute


# ================
# Unit test for:
#   * 'traceroute'
# ================
class TestTraceroute(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = ''

    golden_parsed_output1 = {
        'traceroute': {
            '10.4.1.1': {
                'address': '10.4.1.1',
                'hops': {
                    '1': {
                        'paths': {
                            1: {
                                'address': '10.4.1.2',
                                'label_info': {
                                    'MPLS': {
                                        'exp': 0,
                                        'label': '11111'}
                                },
                                'probe_msec': ['16',
                                               '4',
                                               '4']}
                        }
                    },
                    '2': {
                        'paths': {
                            1: {
                                'address': '10.9.1.3',
                                'probe_msec': ['9',
                                               '*',
                                               '8']}
                        }
                    }
                }
            }
        }
    }

    golden_output1 = '''\
        RP/0/RP0/CPU0:router#traceroute 10.4.1.1
        Mon Sep 30 13:23:56.830 EDT
        
        Type escape sequence to abort.
        Tracing the route to 10.4.1.1
        
         1  10.4.1.2 [MPLS: Label 11111 Exp 0] 16 msec  4 msec  4 msec 
         2  10.9.1.3 9 msec  *  8 msec 
        -> traceroute to 10.2.3.3 and check if label 11111(from above table) can be confirmed
           (=if traffic is passed based on SR labels)
        '''

    def test_traceroute_empty(self):
        obj = Traceroute(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(output=self.empty_output)

    def test_traceroute_golden1(self):
        self.maxDiff = None
        obj = Traceroute(device=self.device)
        parsed_output = obj.parse(output=self.golden_output1)
        self.assertEqual(parsed_output, self.golden_parsed_output1)

if __name__ == '__main__':
    unittest.main()
