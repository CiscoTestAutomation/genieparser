
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
from genie.libs.parser.iosxe.traceroute import Traceroute


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
                        'probe_msec': ['70', '200', '19']},
                    '2': 
                        {'address': '10.0.9.1',
                        
                        'label_name': 
                            {'MPLS': 
                                {'exp': 0,
                                'label': 300678}},
                        'probe_msec': ['177', '150', '9']},
                    '3': 
                        {'address': '192.168.14.61',
                        'label_name': 
                            {'MPLS': 
                                {'exp': 0,
                            'label': 302537}},
                        'probe_msec': ['134', '1', '55']},
                    '4': 
                        {'address': '192.168.15.1',
                        'label_name': 
                            {'MPLS': 
                                {'exp': 0,
                                'label': 24133}},
                        'probe_msec': ['6', '7', '64']},
                    '5': 
                        {'address': '10.80.241.86',
                        'label_name': 
                            {'MPLS': 
                                {'exp': 0,
                                'label': 24147}},
                        'probe_msec': ['69', '65', '111']},
                    '6': 
                        {'address': '10.90.135.110',
                        'label_name': 
                            {'MPLS': 
                                {'exp': 0,
                                'label': 24140}},
                        'probe_msec': ['21', '4', '104']},
                    '7': 
                        {'address': '172.31.166.10',
                        'probe_msec': ['92', '51', '148']},
                    '8': 
                        {'address': '10.1.1.2',
                        'vrf_in_id': '1001',
                        'vrf_in_name': 'red',
                        'vrf_out_id': '2001',
                        'vrf_out_name': 'blue'},
                    '9': 
                        {'address': '10.2.1.2',
                        'vrf_in_id': '1001',
                        'vrf_in_name': 'red',
                        'vrf_out_id': '2001',
                        'vrf_out_name': 'blue'}}}}}

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
          8 10.1.1.2 (red/1001, blue/2001)
          9 10.2.1.2 (red/1001, blue/2001)
        '''

    def test_traceroute_numeric_timeout_probe_ttl_source_empty(self):
        self.device = Mock(**self.empty_output)
        obj = Traceroute(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_traceroute_numeric_timeout_probe_ttl_source_golden1(self):
        self.maxDiff = None
        obj = Traceroute(device=self.device)
        parsed_output = obj.parse(address='172.16.166.253', timeout=1, probe=3, min=1, max=15, source='61.200.255.248', output=self.golden_output1)
        self.assertEqual(parsed_output, self.golden_parsed_output1)


if __name__ == '__main__':
    unittest.main()
