import unittest
from unittest.mock import Mock

from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError

from genie.libs.parser.iosxe.show_eigrp import ShowEigrpNeighbors, ShowEigrpNeighborsDetail

class test_show_eigrp_neighbors(unittest.TestCase):

    device = Device(name='aDevice')

    expected_parsed_output_1 = {
        'eigrp_interface': {
            'Gi0/0': {
                'index': {
                    1: {
                        '10.1.1.2': {
                            'hold_time': 13,
                            'last_seq_number': 5,
                            'peer_handle': 0,
                            'q_cnt': 0,
                            'rto': 5000,
                            'srtt': 1996.0,
                            'uptime': '00:00:03'},},},
            },
        },
    }

    expected_parsed_output_2 = {
        'eigrp_interface': {
            'Gi0/0': {
                'index': {
                    1: {
                        '10.1.1.9': {
                            'hold_time': 14,
                            'last_seq_number': 5,
                            'peer_handle': 2,
                            'q_cnt': 0,
                            'rto': 5000,
                            'srtt': 206.0,
                            'uptime': '00:02:24'}},
                    2: {
                        '10.1.1.2': {
                            'hold_time': 13,
                            'last_seq_number': 5,
                            'peer_handle': 0,
                            'q_cnt': 0,
                            'rto': 5000,
                            'srtt': 1996.0,
                            'uptime': '00:00:03'}}}}}}

    expected_parsed_output_3 = {
        'eigrp_interface': {
            'Gi0/0': {
                'index': {
                    1: {
                        '10.1.1.9': {
                            'hold_time': 14,
                            'last_seq_number': 5,
                            'peer_handle': 2,
                            'q_cnt': 0,
                            'rto': 5000,
                            'srtt': 206.0,
                            'uptime': '00:02:24'}}}},
            'Gi0/1': {
                'index': {
                    1: {
                        '10.1.2.3': {
                            'hold_time': 11,
                            'last_seq_number': 5,
                            'peer_handle': 1,
                            'q_cnt': 0,
                            'rto': 5000,
                            'srtt': 2202.0,
                            'uptime': '00:20:39'}}}}}}

    expected_parsed_output_empty = {
        'eigrp_interface': {}
    }


    device_output_1 = {'execute.return_value': '''
        H   Address      Interface  Hold  Uptime    SRTT   RTO    Q   Seq
                                    (sec)           (ms)          Cnt Num
        0   10.1.1.2     Gi0/0      13    00:00:03  1996   5000   0   5
    '''}

    device_output_2 = {'execute.return_value': '''
        H   Address      Interface  Hold  Uptime    SRTT   RTO    Q   Seq
                                    (sec)           (ms)          Cnt Num        
        2   10.1.1.9     Gi0/0      14    00:02:24  206    5000   0   5        
        0   10.1.1.2     Gi0/0      13    00:00:03  1996   5000   0   5
    '''}

    device_output_3 = {'execute.return_value': '''
        H   Address      Interface  Hold  Uptime    SRTT   RTO    Q   Seq
                                    (sec)           (ms)          Cnt Num
        2   10.1.1.9     Gi0/0      14    00:02:24  206    5000   0   5
        1   10.1.2.3     Gi0/1      11    00:20:39  2202   5000   0   5
    '''}


    device_output_empty = {'execute.return_value': ''}



    def test_show_eigrp_neighbors_1(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_1)
        obj = ShowEigrpNeighbors(device=self.device)        
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_1)

    def test_show_eigrp_neighbors_2(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_2)
        obj = ShowEigrpNeighbors(device=self.device)        
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_2)

    def test_show_eigrp_neighbors_3(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_3)
        obj = ShowEigrpNeighbors(device=self.device)        
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_3)

    def test_show_eigrp_neighbors_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_empty)
        obj = ShowEigrpNeighbors(device=self.device)        
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_empty)

class test_show_eigrp_neighbors_detail(unittest.TestCase):

    device = Device(name='aDevice')

    expected_parsed_output_1 = {}

    device_output_1 = {'execute.return_value': '''
        Device# show ip eigrp neighbors detail

        EIGRP-IPv4 Neighbors for AS(100)
        H   Address                 Interface       Hold Uptime   SRTT   RTO  Q  Seq
                                            (sec)         (ms)       Cnt Num
        0   10.1.2.1                 Et1/0             11 00:00:25   10   200  0  5
        Version 5.1/3.0, Retrans: 2, Retries: 0, Prefixes: 1
        Topology-ids from peer - 0

        EIGRP-IPv4 Neighbors for AS(100)
        H   Address                 Interface       Hold Uptime   SRTT   RTO  Q  Seq
                                            (sec)         (ms)       Cnt Num
        0   10.1.2.1                 Et1/0             11 00:02:31   12   200  0  6
    
        Time since Restart 00:01:34
        Version 5.1/3.0, Retrans: 2, Retries: 0, Prefixes: 1
        Topology-ids from peer - 0
    '''}

    def test_show_eigrp_neighbors_detail_1(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_1)
        obj = ShowEigrpNeighborsDetail(device=self.device)        
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_1)

if __name__ == '__main__':
    unittest.main()
    