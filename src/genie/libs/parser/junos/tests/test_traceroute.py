# Python
import unittest
from unittest.mock import Mock

# pyATS
from pyats.topology import Device

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# junos traceroute
from genie.libs.parser.junos.traceroute import (TracerouteNoResolve)


class TestTracerouteNoResolve(unittest.TestCase):
    """ Unit tests for:
            * traceroute {ipaddress} no-resolve
    """

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        traceroute 10.135.0.2 no-resolve
        traceroute to example.local (10.135.0.2), 30 hops max, 52 byte packets
         1  r1 10.145.0.2  1.792 ms  1.142 ms  0.831 ms
         2  10.135.0.2  1.734 ms  1.234 ms  0.855 ms
    '''}

    golden_parsed_output = {
        'traceroute': {
            'to': {
                'domain': 'example.local',
                'address': '10.135.0.2'
            },
            'max-hops': '30',
            'packet-size': '52',
            'hops': [
                        {
                            'hop-number': '1',
                            'router-name': 'r1',
                            'address': '10.145.0.2',
                            'round-trip-time': '1.792 ms  1.142 ms  0.831 ms'
                        },
                        {
                            'hop-number': '2',
                            'address': '10.135.0.2',
                            'round-trip-time': '1.734 ms  1.234 ms  0.855 ms'
                        }
            ]
        }
    }

    golden_output_2 = {'execute.return_value': '''
        traceroute 10.121.0.1 no-resolve 
        traceroute to 10.121.0.1 (10.121.0.1), 30 hops max, 52 byte packets
        traceroute: sendto: No route to host
        1 traceroute: wrote 10.121.0.1 52 chars, ret=-1
        *traceroute: sendto: No route to host
        traceroute: wrote 10.121.0.1 52 chars, ret=-1
        *traceroute: sendto: No route to host
        traceroute: wrote 10.121.0.1 52 chars, ret=-1
        *
        traceroute: sendto: No route to host
        2 traceroute: wrote 10.121.0.1 52 chars, ret=-1
        * 10.121.0.1  2.111 ms  1.642 ms
        '''}

    golden_parsed_output_2 = {
        'traceroute': 
                {'max-hops': '30',
                'packet-size': '52',
                'to': {
                    'address': '10.121.0.1', 
                    'domain': '10.121.0.1'}}}

    golden_output_3 = {'execute.return_value':'''
        traceroute 2001::2 no-resolve 
        traceroute6 to 2001::2 (2001::2) from 2001::1, 64 hops max, 12 byte packets
        1  2001::2  1.487 ms  1.112 ms  1.311 ms
        '''
    }

    golden_parsed_output_3 = {
        'traceroute': {
            'hops': [{
                'address': '2001::2',
                'hop-number': '1',
                'round-trip-time': '1.487 ms  1.112 ms  1.311 ms'}],
                'max-hops': '64',
                'packet-size': '12',
                'to': {
                    'address': '2001::2', 
                    'domain': '2001::2'
                    }
                }
            }
    
    golden_output_4 = {'execute.return_value':'''
        traceroute 2001::2 no-resolve 
        traceroute6 to 2001::2 (2001::2) from 2001::1, 64 hops max, 12 byte packets
        traceroute: sendto: No route to host
        1 traceroute6: wrote 2001::2 12 chars, ret=-1
        * * 2001::2  1.719 ms    
    '''}

    golden_parsed_output_4 = {
        'traceroute': {
            'max-hops': '64',
            'packet-size': '12',
            'to': {
                'address': '2001::2', 
                'domain': '2001::2'
                }
            }
        }
        
    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = TracerouteNoResolve(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse(addr='10.135.0.2')

    def test_traceroute(self):
        self.device = Mock(**self.golden_output)
        obj = TracerouteNoResolve(device=self.device)
        parsed_output = obj.parse(addr='10.135.0.2')
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_traceroute_2(self):
        self.device = Mock(**self.golden_output_2)
        obj = TracerouteNoResolve(device=self.device)
        parsed_output = obj.parse(addr='10.121.0.1')
        self.assertEqual(parsed_output, self.golden_parsed_output_2) 

    def test_traceroute_3(self):
        self.device = Mock(**self.golden_output_3)
        obj = TracerouteNoResolve(device=self.device)
        parsed_output = obj.parse(addr='2001::2')
        self.assertEqual(parsed_output, self.golden_parsed_output_3)  

    def test_traceroute_4(self):
        self.device = Mock(**self.golden_output_4)
        obj = TracerouteNoResolve(device=self.device)
        parsed_output = obj.parse(addr='2001::2')
        self.assertEqual(parsed_output, self.golden_parsed_output_4)                        


if __name__ == '__main__':
    unittest.main()