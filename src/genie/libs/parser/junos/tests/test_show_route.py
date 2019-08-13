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
    #show route table inet.3 4.4.4.4
 
    inet.3: 3 destinations, 3 routes (3 active, 0 holddown, 0 hidden)
    + = Active Route, - = Last Active, * = Both
     
    4.4.4.4/32         *[LDP/9] 03:40:50, metric 110
                        > to 200.0.0.6 via ge-0/0/1.0

    '''}

    parsed_output_1 = {
        'route_information': {
            'route_table': {
                'table_name': {
                    'inet.3:': {
                        'active_route_count': 3,
                        'destination_count': 3,
                        'hidden_route_count': 0,
                        'holddown_route_count': 0,
                        'rt': {
                            'rt_destination': {
                                '4.4.4.4/32': {
                                    'active_tag': '*',
                                    'age': '03:40:50',
                                    'metric': '110',
                                    'nh': {
                                        'to': '200.0.0.6',
                                        'via': 'GigabitEthernet0/0/1.0'},
                            'preference': '9',
                            'protocol_name': 'LDP'}}},
                            'total_route_count': 3}}}}}


    golden_output_2 = {'execute.return_value': '''
    #show route table inet.3 202.239.165.220
 
    inet.3: 3 destinations, 3 routes (3 active, 0 holddown, 0 hidden)
    + = Active Route, - = Last Active, * = Both
     
    202.239.165.220/32 *[LDP/9] 03:41:19, metric 1111
                        > to 200.0.0.6 via ge-0/0/1.0, Push 305550

    '''}

    parsed_output_2 = {
        'route_information': {
            'route_table': {
                'table_name': {
                    'inet.3:': {
                        'active_route_count': 3,
                        'destination_count': 3,
                        'hidden_route_count': 0,
                        'holddown_route_count': 0,
                        'rt': {
                            'rt_destination': {
                                '202.239.165.220/32': {
                                    'active_tag': '*',
                                    'age': '03:41:19',
                                    'metric': '1111',
                                    'nh': {
                                        'mpls_label': 'Push 305550',
                                        'to': '200.0.0.6',
                                        'via': 'GigabitEthernet0/0/1.0'},
                                    'preference': '9',
                                    'protocol_name': 'LDP'}}},
                        'total_route_count': 3}}}}}

    golden_output_3 = {'execute.return_value': '''
    #show route table inet.3

    inet.3: 3 destinations, 3 routes (3 active, 0 holddown, 0 hidden)
    + = Active Route, - = Last Active, * = Both

    4.4.4.4/32         *[LDP/9] 02:30:55, metric 110
                        > to 200.0.0.6 via ge-0/0/1.0
    106.162.197.254/32 *[LDP/9] 02:14:05, metric 1001
                        > to 7.0.0.1 via ge-0/0/2.0
    202.239.165.220/32 *[LDP/9] 02:03:22, metric 1111
                        > to 200.0.0.6 via ge-0/0/1.0, Push 307742
    '''}

    parsed_output_3 = {
        'route_information': {
            'route_table': {
                'table_name': {
                    'inet.3:': {
                        'active_route_count': 3,
                        'destination_count': 3,
                        'hidden_route_count': 0,
                        'holddown_route_count': 0,
                        'rt': {
                            'rt_destination': {
                                '106.162.197.254/32': {
                                    'active_tag': '*',
                                    'age': '02:14:05',
                                    'metric': '1001',
                                    'nh': {
                                        'to': '7.0.0.1',
                                        'via': 'GigabitEthernet0/0/2.0'},
                                        'preference': '9',
                                        'protocol_name': 'LDP'},
                                '202.239.165.220/32': {
                                    'active_tag': '*',
                                    'age': '02:03:22',
                                    'metric': '1111',
                                    'nh': {
                                        'mpls_label': 'Push 307742',
                                        'to': '200.0.0.6',
                                        'via': 'GigabitEthernet0/0/1.0'},
                                    'preference': '9',
                                    'protocol_name': 'LDP'},
                                '4.4.4.4/32': {
                                    'active_tag': '*',
                                    'age': '02:30:55',
                                    'metric': '110',
                                    'nh': {
                                        'to': '200.0.0.6',
                                        'via': 'GigabitEthernet0/0/1.0'},
                                        'preference': '9',
                                        'protocol_name': 'LDP'}}},
                        'total_route_count': 3}}}}}

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
        parsed_output = obj.parse(table='inet.3', prefix='4.4.4.4')
        self.assertEqual(parsed_output, self.parsed_output_1)

    def test_show_route_table_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        obj = ShowRouteTable(device=self.device)
        parsed_output = obj.parse(table='inet.3', prefix='202.239.165.220')
        self.assertEqual(parsed_output, self.parsed_output_2)

    def test_show_route_table_3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_3)
        obj = ShowRouteTable(device=self.device)
        parsed_output = obj.parse(table='inet.3')
        self.assertEqual(parsed_output, self.parsed_output_3)

if __name__ == '__main__':
    unittest.main()
