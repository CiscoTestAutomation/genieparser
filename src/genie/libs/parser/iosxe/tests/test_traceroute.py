
# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                             SchemaMissingKeyError

# iosxe traceroute
from genie.libs.parser.iosxe.traceroute import TracerouteNumericTimeoutProbeTTLSource


# =====================================================================================================
# Unit test for:
#   * 'traceroute {traceroute} numeric timeout {timeout} probe {probe} ttl {min} {max} source {source}'
# =====================================================================================================
class test_traceroute_numeric_timeout_probe_ttl_source(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'traceroute': 
            {'172.16.166.253': 
                {'hops': 
                    {'1': 
                        {'address': '172.31.255.125',
                        'label_name': 
                            {'MPLS': 
                                {'exp': 0,
                                'label': 624}},
                        'first': 70,
                        'second': 200,
                        'third': 19},
                    '2': 
                        {'address': '10.0.9.1',
                        'label_name': 
                            {'MPLS': 
                                {'exp': 0,
                                'label': 300678}},
                        'first': 177,
                        'second': 150,
                        'third': 9},
                    '3': 
                        {'address': '192.168.14.61',
                        'label_name': 
                            {'MPLS': 
                                {'exp': 0,
                            'label': 302537}},
                        'first': 134,
                        'second': 1,
                        'third': 55},
                    '4': 
                        {'address': '192.168.15.1',
                        'label_name': 
                            {'MPLS': 
                                {'exp': 0,
                                'label': 24133}},
                        'first': 6,
                        'second': 7,
                        'third': 64},
                    '5': 
                        {'address': '10.80.241.86',
                        'label_name': 
                            {'MPLS': 
                                {'exp': 0,
                                'label': 24147}},
                        'first': 69,
                        'second': 65,
                        'third': 111},
                    '6': 
                        {'address': '10.90.135.110',
                        'label_name': 
                            {'MPLS': 
                                {'exp': 0,
                                'label': 24140}},
                        'first': 21,
                        'second': 4,
                        'third': 104},
                    '7': 
                        {'address': '172.31.166.10',
                        'first': 92,
                        'second': 51,
                        'third': 148}},
                'vrf_in': 'name/id',
                'vrf_out': 'name/id'}}}

    golden_output1 = '''\
        router#traceroute 172.16.166.253 numeric timeout 1 probe 3 ttl 1 15 source 61.200.255.248 
        Type escape sequence to abort. 
        Tracing the route to 172.16.166.253 
        VRF info: (vrf in name/id, vrf out name/id) 
          1 172.31.255.125 [MPLS: Label 624 Exp 0] 70 msec 200 msec 19 msec 
          2 10.0.9.1 [MPLS: Label 300678 Exp 0] 177 msec 150 msec 9 msec 
          3 192.168.14.61 [MPLS: Label 302537 Exp 0] 134 msec 1 msec 55 msec 
          4 192.168.15.1 [MPLS: Label 24133 Exp 0] 6 msec 7 msec 64 msec 
          5 10.80.241.86 [MPLS: Label 24147 Exp 0] 69 msec 65 msec 111 msec 
          6 10.90.135.110 [MPLS: Label 24140 Exp 0] 21 msec 4 msec 104 msec 
          7 172.31.166.10 92 msec 51 msec 148 msec
        '''

    def test_traceroute_numeric_timeout_probe_ttl_source_empty(self):
        self.device = Mock(**self.empty_output)
        obj = TracerouteNumericTimeoutProbeTTLSource(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_traceroute_numeric_timeout_probe_ttl_source_golden1(self):
        obj = TracerouteNumericTimeoutProbeTTLSource(device=self.device)
        parsed_output = obj.parse(traceroute='172.16.166.253', timeout=1, probe=3, min=1, max=15, source='61.200.255.248', output=self.golden_output1)
        self.assertEqual(parsed_output, self.golden_parsed_output1)


if __name__ == '__main__':
    unittest.main()
