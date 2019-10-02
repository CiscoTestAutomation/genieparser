# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device, loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

from genie.libs.parser.junos.show_route import ShowRouteTable

'''
Unit test for:
    * show route table {table}
    * show route table {table} {prefix}
'''
class test_show_route_table(unittest.TestCase):

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_output_1 = {'execute.return_value': '''
        #show route table inet.3 10.64.4.4
     
        inet.3: 3 destinations, 3 routes (3 active, 0 holddown, 0 hidden)
        + = Active Route, - = Last Active, * = Both
         
        10.64.4.4/32         *[LDP/9] 03:40:50, metric 110
                            > to 192.168.220.6 via ge-0/0/1.0

    '''}

    parsed_output_1 = {
        'table_name': {
            'inet.3': {
                'active_route_count': 3,
                'destination_count': 3,
                'hidden_route_count': 0,
                'holddown_route_count': 0,
                'routes': {
                    '10.64.4.4/32': {
                        'active_tag': '*',
                        'age': '03:40:50',
                        'metric': '110',
                        'next_hop': {
                            'next_hop_list': {
                                1: {
                                    'best_route': '>',
                                    'to': '192.168.220.6',
                                    'via': 'ge-0/0/1.0'}}},
                        'preference': '9',
                        'protocol_name': 'LDP'}},
                'total_route_count': 3}}}



    golden_output_2 = {'execute.return_value': '''
        #show route table inet.3 192.168.36.220
     
        inet.3: 3 destinations, 3 routes (3 active, 0 holddown, 0 hidden)
        + = Active Route, - = Last Active, * = Both
         
        192.168.36.220/32 *[LDP/9] 03:41:19, metric 1111
                            > to 192.168.220.6 via ge-0/0/1.0, Push 305550

    '''}

    parsed_output_2 = {
        'table_name': {
            'inet.3': {
                'active_route_count': 3,
                'destination_count': 3,
                'hidden_route_count': 0,
                'holddown_route_count': 0,
                'routes': {
                    '192.168.36.220/32': {
                        'active_tag': '*',
                        'age': '03:41:19',
                        'metric': '1111',
                        'next_hop': {
                            'next_hop_list': {
                                1: {
                                    'best_route': '>',
                                    'mpls_label': 'Push 305550',
                                    'to': '192.168.220.6',
                                    'via': 'ge-0/0/1.0'}}},
                        'preference': '9',
                        'protocol_name': 'LDP'}},
                'total_route_count': 3}}}


    golden_output_3 = {'execute.return_value': '''
        #show route table inet.3

        inet.3: 3 destinations, 3 routes (3 active, 0 holddown, 0 hidden)
        + = Active Route, - = Last Active, * = Both

        10.64.4.4/32         *[LDP/9/4] 02:30:55, metric 110
                            > to 192.168.220.6 via ge-0/0/1.0
        10.169.197.254/32 *[LDP/9] 02:14:05, metric 1001
                            > to 10.49.0.1 via ge-0/0/2.0
        192.168.36.220/32 *[LDP/9] 02:03:22, metric 1111
                            > to 192.168.220.6 via ge-0/0/1.0, Push 307742
    '''}

    parsed_output_3 = {        
        'table_name': {
            'inet.3': {
                'active_route_count': 3,
                'destination_count': 3,
                'hidden_route_count': 0,
                'holddown_route_count': 0,
                'routes': {
                    '10.169.197.254/32': {
                        'active_tag': '*',
                        'age': '02:14:05',
                        'metric': '1001',
                        'next_hop': {
                            'next_hop_list': {
                                1: {
                                    'best_route': '>',
                                    'to': '10.49.0.1',
                                    'via': 'ge-0/0/2.0'}}},
                        'preference': '9',
                        'protocol_name': 'LDP'},
                    '192.168.36.220/32': {
                        'active_tag': '*',
                        'age': '02:03:22',
                        'metric': '1111',
                        'next_hop': {
                            'next_hop_list': {
                                1: {
                                    'best_route': '>',
                                    'mpls_label': 'Push 307742',
                                    'to': '192.168.220.6',
                                    'via': 'ge-0/0/1.0'}}},
                        'preference': '9',
                        'protocol_name': 'LDP'},
                    '10.64.4.4/32': {
                        'active_tag': '*',
                        'age': '02:30:55',
                        'metric': '110',
                        'next_hop': {
                            'next_hop_list': {
                                1: {
                                    'best_route': '>',
                                    'to': '192.168.220.6',
                                    'via': 'ge-0/0/1.0'}}},
                        'preference': '9',
                        'preference2': '4',
                        'protocol_name': 'LDP'}},
                        'total_route_count': 3}}}

    golden_output_4= {'execute.return_value': '''
        #show route table inet.3
        inet.3: 5 destinations, 5 routes (5 active, 0 holddown, 0 hidden)
        + = Active Route, - = Last Active, * = Both

        10.0.0.5/32        *[LDP/9] 00:25:43, metric 10
                              to 10.2.94.2 via lt-1/2/0.49
                            > to 10.2.3.2 via lt-1/2/0.23

    '''}

    parsed_output_4 = {
        'table_name': {
            'inet.3': {
                'active_route_count': 5,
                'destination_count': 5,
                'hidden_route_count': 0,
                'holddown_route_count': 0,
                'routes': {
                    '10.0.0.5/32': {
                        'active_tag': '*',
                        'age': '00:25:43',
                        'metric': '10',
                        'next_hop': {
                            'next_hop_list': {
                                1: {
                                    'to': '10.2.94.2',
                                    'via': 'lt-1/2/0.49'},
                                2: {
                                    'best_route': '>',
                                    'to': '10.2.3.2',
                                    'via': 'lt-1/2/0.23'}}},
                        'preference': '9',
                        'protocol_name': 'LDP'}},
                'total_route_count': 5}}}


    def test_show_route_table_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowRouteTable(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(table='table.1')

    def test_show_route_table_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowRouteTable(device=self.device)
        parsed_output = obj.parse(table='inet.3', prefix='10.64.4.4')
        self.assertEqual(parsed_output, self.parsed_output_1)

    def test_show_route_table_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        obj = ShowRouteTable(device=self.device)
        parsed_output = obj.parse(table='inet.3', prefix='192.168.36.220')
        self.assertEqual(parsed_output, self.parsed_output_2)

    def test_show_route_table_3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_3)
        obj = ShowRouteTable(device=self.device)
        parsed_output = obj.parse(table='inet.3')
        self.assertEqual(parsed_output, self.parsed_output_3)

    def test_show_route_table_4(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_4)
        obj = ShowRouteTable(device=self.device)
        parsed_output = obj.parse(table='inet.3')
        self.assertEqual(parsed_output, self.parsed_output_4)

if __name__ == '__main__':
    unittest.main()
