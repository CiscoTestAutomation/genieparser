
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


# ================
# Unit test for:
#   * 'traceroute'
# ================
class test_traceroute(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = ''

    golden_parsed_output1 = {
        'traceroute': 
            {'172.16.166.253': 
                {'hops': 
                    {'1': 
                        {'address': '172.31.255.125',
                        'label_info': 
                            {'MPLS': 
                                {'exp': 0,
                                'label': '624'}},
                        'probe_msec': ['70', '200', '19']},
                    '2': 
                        {'address': '10.0.9.1',
                        
                        'label_info': 
                            {'MPLS': 
                                {'exp': 0,
                                'label': '300678'}},
                        'probe_msec': ['177', '150', '9']},
                    '3': 
                        {'address': '192.168.14.61',
                        'label_info': 
                            {'MPLS': 
                                {'exp': 0,
                            'label': '302537'}},
                        'probe_msec': ['134', '1', '55']},
                    '4': 
                        {'address': '192.168.15.1',
                        'label_info': 
                            {'MPLS': 
                                {'exp': 0,
                                'label': '24133'}},
                        'probe_msec': ['6', '7', '64']},
                    '5': 
                        {'address': '10.80.241.86',
                        'label_info': 
                            {'MPLS': 
                                {'exp': 0,
                                'label': '24147'}},
                        'probe_msec': ['69', '65', '111']},
                    '6': 
                        {'address': '10.90.135.110',
                        'label_info': 
                            {'MPLS': 
                                {'exp': 0,
                                'label': '24140'}},
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

    golden_parsed_output2 = {
        'traceroute': 
            {'172.31.165.220/32': 
                {'hops': 
                    {'0': 
                        {'address': '192.168.197.94',
                        'label_info': 
                            {'label_name': '1015',
                            'exp': 0},
                        'mru': 1552},
                    '1': 
                        {'address': '192.168.197.93',
                        'code': 'L',
                        'label_info': 
                            {'label_name': 'implicit-null',
                            'exp': 0},
                        'mru': 1552,
                        'probe_msec': ['1']},
                    '2': 
                        {'address': '192.168.197.102',
                        'code': '!',
                        'probe_msec': ['1']}},
                'timeout_seconds': 2}}}

    golden_output2 = '''\
        router#traceroute mpls ipv4 172.31.165.220 255.255.255.255
        Tracing MPLS Label Switched Path to 172.31.165.220/32, timeout is 2 seconds

        Codes: '!' - success, 'Q' - request not sent, '.' - timeout,
          'L' - labeled output interface, 'B' - unlabeled output interface,
          'D' - DS Map mismatch, 'F' - no FEC mapping, 'f' - FEC mismatch,
          'M' - malformed request, 'm' - unsupported tlvs, 'N' - no label entry,
          'P' - no rx intf label prot, 'p' - premature termination of LSP,
          'R' - transit router, 'I' - unknown upstream index,
          'l' - Label switched with FEC change, 'd' - see DDMAP for return code,
          'X' - unknown return code, 'x' - return code 0

        Type escape sequence to abort.
          0 192.168.197.94 MRU 1552 [Labels: 1015 Exp: 0]
        L 1 192.168.197.93 MRU 1552 [Labels: implicit-null Exp: 0] 1 ms
        ! 2 192.168.197.102 1 ms
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

    def test_traceroute_golden2(self):
        self.maxDiff = None
        obj = Traceroute(device=self.device)
        parsed_output = obj.parse(output=self.golden_output2)
        self.assertEqual(parsed_output, self.golden_parsed_output2)

if __name__ == '__main__':
    unittest.main()
