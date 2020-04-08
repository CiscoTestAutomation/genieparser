# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device, loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

from genie.libs.parser.junos.show_route import (ShowRouteTable,
                                                ShowRouteProtocol)

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

'''
Unit test for:
    * show route protocol {protocol}
    * show route protocol {protocol} {ip_address}
    * show route protocol {protocol} table {table}
'''
class TestShowRouteProtocol(unittest.TestCase):

    device = Device(name='aDevice')
    maxDiff = None

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        show route protocol static 10.169.14.240/32

        inet.0: 932 destinations, 1618 routes (932 active, 0 holddown, 0 hidden)
        + = Active Route, - = Last Active, * = Both

        10.169.14.240/32  *[Static/5] 5w2d 15:42:25
                            >  to 10.169.14.121 via ge-0/0/1.0

        inet.3: 12 destinations, 12 routes (12 active, 0 holddown, 0 hidden)
    '''}

    golden_parsed_output = {
        "route-information": {
            "route-table": [
                {
                    "active-route-count": "932",
                    "destination-count": "932",
                    "hidden-route-count": "0",
                    "holddown-route-count": "0",
                    "rt": [{
                        "rt-destination": "10.169.14.240/32",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {
                                "#text":"5w2d 15:42:25",
                            },
                            "nh": [{
                                "to": "10.169.14.121",
                                "via": "ge-0/0/1.0"
                            }],
                            "preference": "5",
                            "protocol-name": "Static"
                        }
                    }],
                    "table-name": "inet.0",
                    "total-route-count": "1618"
                },
                {
                    "active-route-count": "12",
                    "destination-count": "12",
                    "hidden-route-count": "0",
                    "holddown-route-count": "0",
                    "table-name": "inet.3",
                    "total-route-count": "12"
                }
            ]
        }
    }

    golden_output_2 = {'execute.return_value': '''
        show route protocol static 2001:db8:eb18:ca45::1

        inet6.0: 23 destinations, 24 routes (23 active, 0 holddown, 0 hidden)
        + = Active Route, - = Last Active, * = Both

        2001:db8:eb18:ca45::1/128
                        *[Static/5] 3w5d 18:30:36
                            >  to 2001:db8:eb18:6337::1 via ge-0/0/1.0
    '''}

    golden_parsed_output_2 = {
        "route-information": {
            "route-table": [
                {
                    "active-route-count": "23",
                    "destination-count": "23",
                    "hidden-route-count": "0",
                    "holddown-route-count": "0",
                    "rt": [{
                        "rt-destination": "2001:db8:eb18:ca45::1/128",
                        "rt-entry": {
                            "active-tag": "*",
                            "age": {
                                "#text": "3w5d 18:30:36",
                            },
                            "nh": [{
                                "to": "2001:db8:eb18:6337::1",
                                "via": "ge-0/0/1.0"
                            }],
                            "preference": "5",
                            "protocol-name": "Static"
                        }
                    }],
                    "table-name": "inet6.0",
                    "total-route-count": "24"
                }
            ]
        }
    }

    golden_output_3 = {'execute.return_value': '''
        show route protocol ospf

        inet.0: 929 destinations, 1615 routes (929 active, 0 holddown, 0 hidden)
        + = Active Route, - = Last Active, * = Both

        0.0.0.0/0          *[OSPF/150/10] 3w3d 03:24:58, metric 101, tag 0
                            >  to 10.169.14.121 via ge-0/0/1.0
        10.1.0.0/24          [OSPF/150/10] 3w3d 03:24:58, metric 20, tag 0
                            >  to 10.169.14.121 via ge-0/0/1.0
        10.36.3.3/32         *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        10.16.0.0/30         *[OSPF/10/10] 3w0d 04:51:49, metric 1200
                            >  to 10.169.14.121 via ge-0/0/1.0
        10.100.5.5/32         *[OSPF/10/10] 3w0d 04:51:49, metric 1201
                            >  to 10.169.14.121 via ge-0/0/1.0
        10.19.198.28/30    *[OSPF/10/10] 3w1d 17:03:19, metric 1005
                            >  to 10.189.5.94 via ge-0/0/0.0
        10.19.198.239/32   *[OSPF/10/10] 1w6d 20:52:58, metric 1001
                            >  to 10.19.198.26 via ge-0/0/2.0
        10.174.132.237/32   *[OSPF/150/10] 3w3d 03:24:58, metric 150, tag 0
                            >  to 10.169.14.121 via ge-0/0/1.0
        10.34.2.200/30    *[OSPF/10/10] 3w0d 04:51:49, metric 205
                            >  to 10.169.14.121 via ge-0/0/1.0
        10.34.2.250/32    *[OSPF/10/10] 3w0d 04:51:49, metric 200
                            >  to 10.169.14.121 via ge-0/0/1.0
        10.34.2.251/32    *[OSPF/10/10] 3w0d 04:51:49, metric 205
                            >  to 10.169.14.121 via ge-0/0/1.0
        10.15.0.0/30        *[OSPF/10/10] 1w6d 20:52:58, metric 1001
                            >  to 10.19.198.26 via ge-0/0/2.0
        10.64.0.0/30        *[OSPF/10/10] 1w0d 15:56:54, metric 1201
                            >  to 10.169.14.121 via ge-0/0/1.0
        10.169.196.212/30 *[OSPF/10/10] 3w0d 04:51:49, metric 1200
                            >  to 10.169.14.121 via ge-0/0/1.0
        10.169.196.216/30 *[OSPF/10/10] 3w0d 04:51:49, metric 1205
                            >  to 10.169.14.121 via ge-0/0/1.0
        10.169.196.241/32 *[OSPF/10/10] 1w0d 15:56:54, metric 1201
                            >  to 10.169.14.121 via ge-0/0/1.0
        10.169.14.16/30   *[OSPF/10/10] 3w3d 03:24:58, metric 105
                            >  to 10.169.14.121 via ge-0/0/1.0
        10.169.14.32/30   *[OSPF/10/10] 3w0d 04:11:46, metric 225
                            >  to 10.169.14.121 via ge-0/0/1.0
        10.169.14.128/30  *[OSPF/10/10] 3w1d 17:03:19, metric 125
                            >  to 10.189.5.94 via ge-0/0/0.0
        10.169.14.156/30  *[OSPF/10/10] 3w0d 04:51:51, metric 200
                            >  to 10.169.14.121 via ge-0/0/1.0
        10.169.14.240/32   [OSPF/10/10] 3w3d 03:24:58, metric 100
                            >  to 10.169.14.121 via ge-0/0/1.0
        10.169.14.241/32  *[OSPF/10/10] 3w3d 03:24:58, metric 105
                            >  to 10.169.14.121 via ge-0/0/1.0
        10.169.14.242/32  *[OSPF/10/10] 3w3d 03:24:58, metric 100
                            >  to 10.169.14.121 via ge-0/0/1.0
        10.169.14.243/32  *[OSPF/10/10] 3w3d 03:24:58, metric 105
                            >  to 10.169.14.121 via ge-0/0/1.0
        10.189.5.253/32    *[OSPF/10/10] 3w1d 17:03:19, metric 5
                            >  to 10.189.5.94 via ge-0/0/0.0
        192.168.220.0/30       *[OSPF/10/10] 3w0d 04:51:49, metric 1200
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.0/32       *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.1/32       *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.2/32       *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.3/32       *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.4/32       *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.5/32       *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.6/32       *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.7/32       *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.8/32       *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.9/32       *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.10/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.11/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.12/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.13/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.14/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.15/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.16/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.17/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.18/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.19/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.20/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.21/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.22/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.23/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.24/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.25/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.26/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.27/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.28/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.29/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.30/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.31/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.32/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.33/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.34/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.35/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.36/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.37/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.38/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.39/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.40/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.41/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.42/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.43/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.44/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.45/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.46/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.47/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.48/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.49/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.50/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.51/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.52/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.53/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.54/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.55/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.56/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.57/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.58/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.59/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.60/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.61/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.62/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.63/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.64/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.65/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.66/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.67/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.68/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.69/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.70/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.71/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.72/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.73/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.74/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.75/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.76/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.77/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.78/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.79/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.80/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.81/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.82/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.83/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.84/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.85/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.86/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.87/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.88/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.89/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.90/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.91/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.92/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.93/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.94/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.95/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.96/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.97/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.98/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.99/32      *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.100/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.101/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.102/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.103/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.104/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.105/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.106/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.107/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.108/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.109/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.110/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.111/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.112/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.113/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.114/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.115/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.116/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.117/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.118/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.119/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.120/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.121/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.122/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.123/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.124/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.125/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.126/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.127/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.128/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.129/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.130/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.131/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.132/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.133/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.134/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.135/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.136/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.137/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.138/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.139/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.140/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.141/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.142/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.143/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.144/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.145/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.146/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.147/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.148/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.149/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.150/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.151/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.152/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.153/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.154/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.155/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.156/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.157/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.158/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.159/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.160/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.161/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.162/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.163/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.164/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.165/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.166/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.167/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.168/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.169/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.170/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.171/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.172/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.173/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.174/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.175/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.176/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.177/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.178/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.179/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.180/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.181/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.182/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.183/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.184/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.185/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.186/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.187/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.188/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.189/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.190/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.191/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.192/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.193/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.194/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.195/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.196/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.197/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.198/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.199/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.200/32     *[OSPF/10/10] 1w0d 15:56:54, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.111.0/30       *[OSPF/10/10] 1w0d 15:56:54, metric 1201
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.4.0/30       *[OSPF/10/10] 1w0d 15:56:29, metric 1201
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.100.0/25   *[OSPF/150/10] 2w6d 15:00:08, metric 32000, tag 65000500
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.100.252/32 *[OSPF/150/10] 2w6d 15:00:08, metric 32000, tag 65000500
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.36.48/30  *[OSPF/10/10] 3w3d 03:24:58, metric 10100
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.36.56/30  *[OSPF/10/10] 3w3d 03:24:58, metric 10100
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.36.119/32 *[OSPF/10/10] 3w3d 03:24:58, metric 10101
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.36.120/32 *[OSPF/10/10] 3w3d 03:24:58, metric 10101
                            >  to 10.169.14.121 via ge-0/0/1.0
        224.0.0.5/32       *[OSPF/10] 29w6d 21:48:09, metric 1
                            MultiRecv

        inet.3: 11 destinations, 11 routes (11 active, 0 holddown, 0 hidden)
        + = Active Route, - = Last Active, * = Both

        10.100.5.5/32         *[L-OSPF/10/5] 3w0d 04:11:34, metric 1201
                            >  to 10.169.14.121 via ge-0/0/1.0, Push 17000
                            to 10.189.5.94 via ge-0/0/0.0, Push 17000, Push 1650, Push 1913(top)
        10.19.198.239/32   *[L-OSPF/10/5] 1w6d 20:52:49, metric 1001
                            >  to 10.19.198.26 via ge-0/0/2.0
                            to 10.189.5.94 via ge-0/0/0.0, Push 16073
        10.34.2.250/32    *[L-OSPF/10/5] 3w0d 04:51:49, metric 200
                            >  to 10.169.14.121 via ge-0/0/1.0, Push 16061
        10.34.2.251/32    *[L-OSPF/10/5] 3w0d 04:51:49, metric 205
                            >  to 10.169.14.121 via ge-0/0/1.0, Push 16062
        10.169.196.241/32 *[L-OSPF/10/5] 1w0d 15:56:49, metric 1201
                            >  to 10.169.14.121 via ge-0/0/1.0, Push 16063
                            to 10.189.5.94 via ge-0/0/0.0, Push 16063, Push 1650, Push 1913(top)
        10.169.14.240/32  *[L-OSPF/10/5] 3w1d 17:03:14, metric 100
                            >  to 10.169.14.121 via ge-0/0/1.0
                            to 10.189.5.94 via ge-0/0/0.0, Push 16051, Push 1913(top)
        10.169.14.241/32  *[L-OSPF/10/5] 3w3d 03:24:58, metric 105
                            >  to 10.169.14.121 via ge-0/0/1.0, Push 16052
        10.189.5.253/32    *[L-OSPF/10/5] 3w1d 17:03:19, metric 5
                            >  to 10.189.5.94 via ge-0/0/0.0

        mpls.0: 44 destinations, 44 routes (44 active, 0 holddown, 0 hidden)
        + = Active Route, - = Last Active, * = Both

        2567               *[L-OSPF/10/5] 2w0d 19:07:25, metric 0
                            >  to 10.169.14.121 via ge-0/0/1.0, Pop      
                            to 10.189.5.94 via ge-0/0/0.0, Swap 16051, Push 1913(top)
        2567(S=0)          *[L-OSPF/10/5] 2w0d 19:07:25, metric 0
                            >  to 10.169.14.121 via ge-0/0/1.0, Pop      
                            to 10.189.5.94 via ge-0/0/0.0, Swap 16051, Push 1913(top)
        2568               *[L-OSPF/10/5] 3w3d 03:24:58, metric 0
                            >  to 10.169.14.121 via ge-0/0/1.0, Pop      
        2568(S=0)          *[L-OSPF/10/5] 3w3d 03:24:58, metric 0
                            >  to 10.169.14.121 via ge-0/0/1.0, Pop      
        16051              *[L-OSPF/10/5] 3w1d 17:03:14, metric 100
                            >  to 10.169.14.121 via ge-0/0/1.0, Pop      
                            to 10.189.5.94 via ge-0/0/0.0, Swap 16051, Push 1913(top)
        16051(S=0)         *[L-OSPF/10/5] 3w1d 17:03:14, metric 100
                            >  to 10.169.14.121 via ge-0/0/1.0, Pop      
                            to 10.189.5.94 via ge-0/0/0.0, Swap 16051, Push 1913(top)
        16052              *[L-OSPF/10/5] 3w3d 03:24:58, metric 105
                            >  to 10.169.14.121 via ge-0/0/1.0, Swap 16052
        16061              *[L-OSPF/10/5] 3w0d 04:51:49, metric 200
                            >  to 10.169.14.121 via ge-0/0/1.0, Swap 16061
        16062              *[L-OSPF/10/5] 3w0d 04:51:49, metric 205
                            >  to 10.169.14.121 via ge-0/0/1.0, Swap 16062
        16063              *[L-OSPF/10/5] 1w0d 15:56:49, metric 1201
                            >  to 10.169.14.121 via ge-0/0/1.0, Swap 16063
                            to 10.189.5.94 via ge-0/0/0.0, Swap 16063, Push 1650, Push 1913(top)
        16072              *[L-OSPF/10/5] 3w1d 17:03:19, metric 5
                            >  to 10.189.5.94 via ge-0/0/0.0, Pop      
        16072(S=0)         *[L-OSPF/10/5] 3w1d 17:03:19, metric 5
                            >  to 10.189.5.94 via ge-0/0/0.0, Pop      
        16073              *[L-OSPF/10/5] 1w6d 20:52:49, metric 1001
                            >  to 10.19.198.26 via ge-0/0/2.0, Pop      
                            to 10.189.5.94 via ge-0/0/0.0, Swap 16073
        16073(S=0)         *[L-OSPF/10/5] 1w6d 20:52:49, metric 1001
                            >  to 10.19.198.26 via ge-0/0/2.0, Pop      
                            to 10.189.5.94 via ge-0/0/0.0, Swap 16073
        17000              *[L-OSPF/10/5] 3w0d 04:11:34, metric 1201
                            >  to 10.169.14.121 via ge-0/0/1.0, Swap 17000
                            to 10.189.5.94 via ge-0/0/0.0, Swap 17000, Push 1650, Push 1913(top)
        28985              *[L-OSPF/10/5] 3w1d 17:03:19, metric 0
                            >  to 10.189.5.94 via ge-0/0/0.0, Pop      
        28985(S=0)         *[L-OSPF/10/5] 3w1d 17:03:19, metric 0
                            >  to 10.189.5.94 via ge-0/0/0.0, Pop      
        28986              *[L-OSPF/10/5] 3w1d 17:03:19, metric 0
                            >  to 10.189.5.94 via ge-0/0/0.0, Pop      
        28986(S=0)         *[L-OSPF/10/5] 3w1d 17:03:19, metric 0
                            >  to 10.189.5.94 via ge-0/0/0.0, Pop      
        167966             *[L-OSPF/10/5] 1w6d 20:52:49, metric 0
                            >  to 10.19.198.26 via ge-0/0/2.0, Pop      
                            to 10.189.5.94 via ge-0/0/0.0, Swap 16073
        167966(S=0)        *[L-OSPF/10/5] 1w6d 20:52:49, metric 0
                            >  to 10.19.198.26 via ge-0/0/2.0, Pop      
                            to 10.189.5.94 via ge-0/0/0.0, Swap 16073
        167967             *[L-OSPF/10/5] 1w6d 20:52:58, metric 0
                            >  to 10.19.198.26 via ge-0/0/2.0, Pop      
        167967(S=0)        *[L-OSPF/10/5] 1w6d 20:52:58, metric 0
                            >  to 10.19.198.26 via ge-0/0/2.0, Pop      

        inet6.0: 22 destinations, 23 routes (22 active, 0 holddown, 0 hidden)
        + = Active Route, - = Last Active, * = Both

        ::/0               *[OSPF3/150] 3w1d 17:03:18, metric 101, tag 0
                            >  to fe80::250:56ff:fe8d:72bd via ge-0/0/1.0
        2001:db8:6aa8:6a53::1001/128
                        *[OSPF3/150] 3w1d 17:03:18, metric 150, tag 0
                            >  to fe80::250:56ff:fe8d:72bd via ge-0/0/1.0
        2001:db8:b0f8:ca45::13/128
                        *[OSPF3/10] 3w0d 04:51:40, metric 200
                            >  to fe80::250:56ff:fe8d:72bd via ge-0/0/1.0
        2001:db8:b0f8:ca45::14/128
                        *[OSPF3/10] 3w0d 04:51:40, metric 205
                            >  to fe80::250:56ff:fe8d:72bd via ge-0/0/1.0
        2001:db8:b0f8:3ab::/64
                        *[OSPF3/10] 3w0d 04:51:40, metric 205
                            >  to fe80::250:56ff:fe8d:72bd via ge-0/0/1.0
        2001:db8:eb18:ca45::1/128
                            [OSPF3/10] 3w1d 17:03:18, metric 100
                            >  to fe80::250:56ff:fe8d:72bd via ge-0/0/1.0
        2001:db8:eb18:ca45::2/128
                        *[OSPF3/10] 3w1d 17:03:18, metric 105
                            >  to fe80::250:56ff:fe8d:72bd via ge-0/0/1.0
        2001:db8:eb18:e26e::/64
                        *[OSPF3/10] 3w1d 17:03:18, metric 105
                            >  to fe80::250:56ff:fe8d:72bd via ge-0/0/1.0
        2001:db8:eb18:f5e6::/64
                        *[OSPF3/10] 3w0d 04:11:35, metric 225
                            >  to fe80::250:56ff:fe8d:72bd via ge-0/0/1.0
        2001:db8:eb18:6d57::/64
                        *[OSPF3/10] 3w1d 17:03:23, metric 125
                            >  to fe80::250:56ff:fe8d:53c0 via ge-0/0/0.0
        2001:db8:eb18:9627::/64
                        *[OSPF3/10] 3w0d 04:51:40, metric 200
                            >  to fe80::250:56ff:fe8d:72bd via ge-0/0/1.0
        2001:db8:223c:ca45::c/128
                        *[OSPF3/10] 3w1d 17:03:23, metric 5
                            >  to fe80::250:56ff:fe8d:53c0 via ge-0/0/0.0
        ff02::5/128        *[OSPF3/10] 29w6d 21:48:09, metric 1
                            MultiRecv
    '''}

    golden_parsed_output_3 = {
        "route-information": {
            "route-table": [
                {
                    "active-route-count": "929",
                    "destination-count": "929",
                    "hidden-route-count": "0",
                    "holddown-route-count": "0",
                    "rt": [
                        {
                            "rt-destination": "0.0.0.0/0",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w3d 03:24:58"
                                },
                                "metric": "101",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "150",
                                "preference2": "10",
                                "protocol-name": "OSPF",
                                "rt-tag": "0"
                            }
                        },
                        {
                            "rt-destination": "10.1.0.0/24",
                            "rt-entry": {
                                "age": {
                                    "#text": "3w3d 03:24:58"
                                },
                                "metric": "20",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "150",
                                "preference2": "10",
                                "protocol-name": "OSPF",
                                "rt-tag": "0"
                            }
                        },
                        {
                            "rt-destination": "10.36.3.3/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "10.16.0.0/30",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w0d 04:51:49"
                                },
                                "metric": "1200",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "10.100.5.5/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w0d 04:51:49"
                                },
                                "metric": "1201",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "10.19.198.28/30",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w1d 17:03:19"
                                },
                                "metric": "1005",
                                "nh": [
                                    {
                                        "to": "10.189.5.94",
                                        "via": "ge-0/0/0.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "10.19.198.239/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w6d 20:52:58"
                                },
                                "metric": "1001",
                                "nh": [
                                    {
                                        "to": "10.19.198.26",
                                        "via": "ge-0/0/2.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "10.174.132.237/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w3d 03:24:58"
                                },
                                "metric": "150",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "150",
                                "preference2": "10",
                                "protocol-name": "OSPF",
                                "rt-tag": "0"
                            }
                        },
                        {
                            "rt-destination": "10.34.2.200/30",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w0d 04:51:49"
                                },
                                "metric": "205",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "10.34.2.250/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w0d 04:51:49"
                                },
                                "metric": "200",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "10.34.2.251/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w0d 04:51:49"
                                },
                                "metric": "205",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "10.15.0.0/30",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w6d 20:52:58"
                                },
                                "metric": "1001",
                                "nh": [
                                    {
                                        "to": "10.19.198.26",
                                        "via": "ge-0/0/2.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "10.64.0.0/30",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1201",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "10.169.196.212/30",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w0d 04:51:49"
                                },
                                "metric": "1200",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "10.169.196.216/30",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w0d 04:51:49"
                                },
                                "metric": "1205",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "10.169.196.241/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1201",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "10.169.14.16/30",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w3d 03:24:58"
                                },
                                "metric": "105",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "10.169.14.32/30",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w0d 04:11:46"
                                },
                                "metric": "225",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "10.169.14.128/30",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w1d 17:03:19"
                                },
                                "metric": "125",
                                "nh": [
                                    {
                                        "to": "10.189.5.94",
                                        "via": "ge-0/0/0.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "10.169.14.156/30",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w0d 04:51:51"
                                },
                                "metric": "200",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "10.169.14.240/32",
                            "rt-entry": {
                                "age": {
                                    "#text": "3w3d 03:24:58"
                                },
                                "metric": "100",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "10.169.14.241/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w3d 03:24:58"
                                },
                                "metric": "105",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "10.169.14.242/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w3d 03:24:58"
                                },
                                "metric": "100",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "10.169.14.243/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w3d 03:24:58"
                                },
                                "metric": "105",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "10.189.5.253/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w1d 17:03:19"
                                },
                                "metric": "5",
                                "nh": [
                                    {
                                        "to": "10.189.5.94",
                                        "via": "ge-0/0/0.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.0/30",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w0d 04:51:49"
                                },
                                "metric": "1200",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.0/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.1/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.2/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.3/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.4/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.5/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.6/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.7/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.8/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.9/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.10/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.11/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.12/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.13/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.14/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.15/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.16/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.17/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.18/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.19/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.20/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.21/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.22/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.23/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.24/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.25/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.26/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.27/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.28/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.29/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.30/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.31/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.32/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.33/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.34/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.35/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.36/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.37/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.38/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.39/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.40/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.41/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.42/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.43/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.44/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.45/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.46/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.47/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.48/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.49/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.50/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.51/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.52/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.53/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.54/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.55/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.56/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.57/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.58/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.59/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.60/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.61/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.62/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.63/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.64/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.65/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.66/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.67/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.68/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.69/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.70/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.71/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.72/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.73/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.74/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.75/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.76/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.77/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.78/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.79/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.80/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.81/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.82/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.83/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.84/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.85/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.86/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.87/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.88/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.89/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.90/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.91/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.92/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.93/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.94/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.95/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.96/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.97/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.98/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.99/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.100/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.101/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.102/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.103/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.104/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.105/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.106/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.107/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.108/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.109/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.110/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.111/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.112/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.113/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.114/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.115/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.116/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.117/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.118/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.119/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.120/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.121/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.122/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.123/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.124/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.125/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.126/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.127/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.128/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.129/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.130/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.131/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.132/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.133/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.134/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.135/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.136/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.137/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.138/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.139/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.140/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.141/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.142/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.143/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.144/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.145/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.146/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.147/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.148/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.149/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.150/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.151/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.152/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.153/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.154/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.155/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.156/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.157/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.158/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.159/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.160/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.161/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.162/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.163/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.164/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.165/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.166/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.167/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.168/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.169/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.170/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.171/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.172/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.173/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.174/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.175/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.176/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.177/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.178/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.179/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.180/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.181/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.182/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.183/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.184/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.185/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.186/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.187/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.188/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.189/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.190/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.191/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.192/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.193/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.194/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.195/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.196/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.197/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.198/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.199/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.200/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.111.0/30",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:54"
                                },
                                "metric": "1201",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.4.0/30",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:29"
                                },
                                "metric": "1201",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.100.0/25",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "2w6d 15:00:08"
                                },
                                "metric": "32000",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "150",
                                "preference2": "10",
                                "protocol-name": "OSPF",
                                "rt-tag": "65000500"
                            }
                        },
                        {
                            "rt-destination": "192.168.100.252/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "2w6d 15:00:08"
                                },
                                "metric": "32000",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "150",
                                "preference2": "10",
                                "protocol-name": "OSPF",
                                "rt-tag": "65000500"
                            }
                        },
                        {
                            "rt-destination": "192.168.36.48/30",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w3d 03:24:58"
                                },
                                "metric": "10100",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.36.56/30",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w3d 03:24:58"
                                },
                                "metric": "10100",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.36.119/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w3d 03:24:58"
                                },
                                "metric": "10101",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.36.120/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w3d 03:24:58"
                                },
                                "metric": "10101",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "224.0.0.5/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "29w6d 21:48:09"
                                },
                                "metric": "1",
                                "nh-type": "MultiRecv",
                                "preference": "10",
                                "protocol-name": "OSPF"
                            }
                        }
                    ],
                    "table-name": "inet.0",
                    "total-route-count": "1615"
                },
                {
                    "active-route-count": "11",
                    "destination-count": "11",
                    "hidden-route-count": "0",
                    "holddown-route-count": "0",
                    "rt": [
                        {
                            "rt-destination": "10.100.5.5/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w0d 04:11:34"
                                },
                                "metric": "1201",
                                "nh": [
                                    {
                                        "mpls-label": "Push 17000",
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    },
                                    {
                                        "mpls-label": "Push 17000, Push 1650, Push 1913(top)",
                                        "to": "10.189.5.94",
                                        "via": "ge-0/0/0.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "5",
                                "protocol-name": "L-OSPF"
                            }
                        },
                        {
                            "rt-destination": "10.19.198.239/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w6d 20:52:49"
                                },
                                "metric": "1001",
                                "nh": [
                                    {
                                        "to": "10.19.198.26",
                                        "via": "ge-0/0/2.0"
                                    },
                                    {
                                        "mpls-label": "Push 16073",
                                        "to": "10.189.5.94",
                                        "via": "ge-0/0/0.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "5",
                                "protocol-name": "L-OSPF"
                            }
                        },
                        {
                            "rt-destination": "10.34.2.250/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w0d 04:51:49"
                                },
                                "metric": "200",
                                "nh": [
                                    {
                                        "mpls-label": "Push 16061",
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "5",
                                "protocol-name": "L-OSPF"
                            }
                        },
                        {
                            "rt-destination": "10.34.2.251/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w0d 04:51:49"
                                },
                                "metric": "205",
                                "nh": [
                                    {
                                        "mpls-label": "Push 16062",
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "5",
                                "protocol-name": "L-OSPF"
                            }
                        },
                        {
                            "rt-destination": "10.169.196.241/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:49"
                                },
                                "metric": "1201",
                                "nh": [
                                    {
                                        "mpls-label": "Push 16063",
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    },
                                    {
                                        "mpls-label": "Push 16063, Push 1650, Push 1913(top)",
                                        "to": "10.189.5.94",
                                        "via": "ge-0/0/0.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "5",
                                "protocol-name": "L-OSPF"
                            }
                        },
                        {
                            "rt-destination": "10.169.14.240/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w1d 17:03:14"
                                },
                                "metric": "100",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    },
                                    {
                                        "mpls-label": "Push 16051, Push 1913(top)",
                                        "to": "10.189.5.94",
                                        "via": "ge-0/0/0.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "5",
                                "protocol-name": "L-OSPF"
                            }
                        },
                        {
                            "rt-destination": "10.169.14.241/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w3d 03:24:58"
                                },
                                "metric": "105",
                                "nh": [
                                    {
                                        "mpls-label": "Push 16052",
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "5",
                                "protocol-name": "L-OSPF"
                            }
                        },
                        {
                            "rt-destination": "10.189.5.253/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w1d 17:03:19"
                                },
                                "metric": "5",
                                "nh": [
                                    {
                                        "to": "10.189.5.94",
                                        "via": "ge-0/0/0.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "5",
                                "protocol-name": "L-OSPF"
                            }
                        }
                    ],
                    "table-name": "inet.3",
                    "total-route-count": "11"
                },
                {
                    "active-route-count": "44",
                    "destination-count": "44",
                    "hidden-route-count": "0",
                    "holddown-route-count": "0",
                    "rt": [
                        {
                            "rt-destination": "2567",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "2w0d 19:07:25"
                                },
                                "metric": "0",
                                "nh": [
                                    {
                                        "mpls-label": "Pop",
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    },
                                    {
                                        "mpls-label": "Swap 16051, Push 1913(top)",
                                        "to": "10.189.5.94",
                                        "via": "ge-0/0/0.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "5",
                                "protocol-name": "L-OSPF"
                            }
                        },
                        {
                            "rt-destination": "2567(S=0)",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "2w0d 19:07:25"
                                },
                                "metric": "0",
                                "nh": [
                                    {
                                        "mpls-label": "Pop",
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    },
                                    {
                                        "mpls-label": "Swap 16051, Push 1913(top)",
                                        "to": "10.189.5.94",
                                        "via": "ge-0/0/0.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "5",
                                "protocol-name": "L-OSPF"
                            }
                        },
                        {
                            "rt-destination": "2568",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w3d 03:24:58"
                                },
                                "metric": "0",
                                "nh": [
                                    {
                                        "mpls-label": "Pop",
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "5",
                                "protocol-name": "L-OSPF"
                            }
                        },
                        {
                            "rt-destination": "2568(S=0)",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w3d 03:24:58"
                                },
                                "metric": "0",
                                "nh": [
                                    {
                                        "mpls-label": "Pop",
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "5",
                                "protocol-name": "L-OSPF"
                            }
                        },
                        {
                            "rt-destination": "16051",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w1d 17:03:14"
                                },
                                "metric": "100",
                                "nh": [
                                    {
                                        "mpls-label": "Pop",
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    },
                                    {
                                        "mpls-label": "Swap 16051, Push 1913(top)",
                                        "to": "10.189.5.94",
                                        "via": "ge-0/0/0.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "5",
                                "protocol-name": "L-OSPF"
                            }
                        },
                        {
                            "rt-destination": "16051(S=0)",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w1d 17:03:14"
                                },
                                "metric": "100",
                                "nh": [
                                    {
                                        "mpls-label": "Pop",
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    },
                                    {
                                        "mpls-label": "Swap 16051, Push 1913(top)",
                                        "to": "10.189.5.94",
                                        "via": "ge-0/0/0.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "5",
                                "protocol-name": "L-OSPF"
                            }
                        },
                        {
                            "rt-destination": "16052",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w3d 03:24:58"
                                },
                                "metric": "105",
                                "nh": [
                                    {
                                        "mpls-label": "Swap 16052",
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "5",
                                "protocol-name": "L-OSPF"
                            }
                        },
                        {
                            "rt-destination": "16061",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w0d 04:51:49"
                                },
                                "metric": "200",
                                "nh": [
                                    {
                                        "mpls-label": "Swap 16061",
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "5",
                                "protocol-name": "L-OSPF"
                            }
                        },
                        {
                            "rt-destination": "16062",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w0d 04:51:49"
                                },
                                "metric": "205",
                                "nh": [
                                    {
                                        "mpls-label": "Swap 16062",
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "5",
                                "protocol-name": "L-OSPF"
                            }
                        },
                        {
                            "rt-destination": "16063",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w0d 15:56:49"
                                },
                                "metric": "1201",
                                "nh": [
                                    {
                                        "mpls-label": "Swap 16063",
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    },
                                    {
                                        "mpls-label": "Swap 16063, Push 1650, Push 1913(top)",
                                        "to": "10.189.5.94",
                                        "via": "ge-0/0/0.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "5",
                                "protocol-name": "L-OSPF"
                            }
                        },
                        {
                            "rt-destination": "16072",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w1d 17:03:19"
                                },
                                "metric": "5",
                                "nh": [
                                    {
                                        "mpls-label": "Pop",
                                        "to": "10.189.5.94",
                                        "via": "ge-0/0/0.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "5",
                                "protocol-name": "L-OSPF"
                            }
                        },
                        {
                            "rt-destination": "16072(S=0)",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w1d 17:03:19"
                                },
                                "metric": "5",
                                "nh": [
                                    {
                                        "mpls-label": "Pop",
                                        "to": "10.189.5.94",
                                        "via": "ge-0/0/0.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "5",
                                "protocol-name": "L-OSPF"
                            }
                        },
                        {
                            "rt-destination": "16073",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w6d 20:52:49"
                                },
                                "metric": "1001",
                                "nh": [
                                    {
                                        "mpls-label": "Pop",
                                        "to": "10.19.198.26",
                                        "via": "ge-0/0/2.0"
                                    },
                                    {
                                        "mpls-label": "Swap 16073",
                                        "to": "10.189.5.94",
                                        "via": "ge-0/0/0.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "5",
                                "protocol-name": "L-OSPF"
                            }
                        },
                        {
                            "rt-destination": "16073(S=0)",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w6d 20:52:49"
                                },
                                "metric": "1001",
                                "nh": [
                                    {
                                        "mpls-label": "Pop",
                                        "to": "10.19.198.26",
                                        "via": "ge-0/0/2.0"
                                    },
                                    {
                                        "mpls-label": "Swap 16073",
                                        "to": "10.189.5.94",
                                        "via": "ge-0/0/0.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "5",
                                "protocol-name": "L-OSPF"
                            }
                        },
                        {
                            "rt-destination": "17000",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w0d 04:11:34"
                                },
                                "metric": "1201",
                                "nh": [
                                    {
                                        "mpls-label": "Swap 17000",
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    },
                                    {
                                        "mpls-label": "Swap 17000, Push 1650, Push 1913(top)",
                                        "to": "10.189.5.94",
                                        "via": "ge-0/0/0.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "5",
                                "protocol-name": "L-OSPF"
                            }
                        },
                        {
                            "rt-destination": "28985",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w1d 17:03:19"
                                },
                                "metric": "0",
                                "nh": [
                                    {
                                        "mpls-label": "Pop",
                                        "to": "10.189.5.94",
                                        "via": "ge-0/0/0.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "5",
                                "protocol-name": "L-OSPF"
                            }
                        },
                        {
                            "rt-destination": "28985(S=0)",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w1d 17:03:19"
                                },
                                "metric": "0",
                                "nh": [
                                    {
                                        "mpls-label": "Pop",
                                        "to": "10.189.5.94",
                                        "via": "ge-0/0/0.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "5",
                                "protocol-name": "L-OSPF"
                            }
                        },
                        {
                            "rt-destination": "28986",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w1d 17:03:19"
                                },
                                "metric": "0",
                                "nh": [
                                    {
                                        "mpls-label": "Pop",
                                        "to": "10.189.5.94",
                                        "via": "ge-0/0/0.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "5",
                                "protocol-name": "L-OSPF"
                            }
                        },
                        {
                            "rt-destination": "28986(S=0)",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w1d 17:03:19"
                                },
                                "metric": "0",
                                "nh": [
                                    {
                                        "mpls-label": "Pop",
                                        "to": "10.189.5.94",
                                        "via": "ge-0/0/0.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "5",
                                "protocol-name": "L-OSPF"
                            }
                        },
                        {
                            "rt-destination": "167966",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w6d 20:52:49"
                                },
                                "metric": "0",
                                "nh": [
                                    {
                                        "mpls-label": "Pop",
                                        "to": "10.19.198.26",
                                        "via": "ge-0/0/2.0"
                                    },
                                    {
                                        "mpls-label": "Swap 16073",
                                        "to": "10.189.5.94",
                                        "via": "ge-0/0/0.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "5",
                                "protocol-name": "L-OSPF"
                            }
                        },
                        {
                            "rt-destination": "167966(S=0)",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w6d 20:52:49"
                                },
                                "metric": "0",
                                "nh": [
                                    {
                                        "mpls-label": "Pop",
                                        "to": "10.19.198.26",
                                        "via": "ge-0/0/2.0"
                                    },
                                    {
                                        "mpls-label": "Swap 16073",
                                        "to": "10.189.5.94",
                                        "via": "ge-0/0/0.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "5",
                                "protocol-name": "L-OSPF"
                            }
                        },
                        {
                            "rt-destination": "167967",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w6d 20:52:58"
                                },
                                "metric": "0",
                                "nh": [
                                    {
                                        "mpls-label": "Pop",
                                        "to": "10.19.198.26",
                                        "via": "ge-0/0/2.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "5",
                                "protocol-name": "L-OSPF"
                            }
                        },
                        {
                            "rt-destination": "167967(S=0)",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w6d 20:52:58"
                                },
                                "metric": "0",
                                "nh": [
                                    {
                                        "mpls-label": "Pop",
                                        "to": "10.19.198.26",
                                        "via": "ge-0/0/2.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "5",
                                "protocol-name": "L-OSPF"
                            }
                        }
                    ],
                    "table-name": "mpls.0",
                    "total-route-count": "44"
                },
                {
                    "active-route-count": "22",
                    "destination-count": "22",
                    "hidden-route-count": "0",
                    "holddown-route-count": "0",
                    "rt": [
                        {
                            "rt-destination": "::/0",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w1d 17:03:18"
                                },
                                "metric": "101",
                                "nh": [
                                    {
                                        "to": "fe80::250:56ff:fe8d:72bd",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "150",
                                "protocol-name": "OSPF3",
                                "rt-tag": "0"
                            }
                        },
                        {
                            "rt-destination": "2001:db8:6aa8:6a53::1001/128",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w1d 17:03:18"
                                },
                                "metric": "150",
                                "nh": [
                                    {
                                        "to": "fe80::250:56ff:fe8d:72bd",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "150",
                                "protocol-name": "OSPF3",
                                "rt-tag": "0"
                            }
                        },
                        {
                            "rt-destination": "2001:db8:b0f8:ca45::13/128",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w0d 04:51:40"
                                },
                                "metric": "200",
                                "nh": [
                                    {
                                        "to": "fe80::250:56ff:fe8d:72bd",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "protocol-name": "OSPF3"
                            }
                        },
                        {
                            "rt-destination": "2001:db8:b0f8:ca45::14/128",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w0d 04:51:40"
                                },
                                "metric": "205",
                                "nh": [
                                    {
                                        "to": "fe80::250:56ff:fe8d:72bd",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "protocol-name": "OSPF3"
                            }
                        },
                        {
                            "rt-destination": "2001:db8:b0f8:3ab::/64",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w0d 04:51:40"
                                },
                                "metric": "205",
                                "nh": [
                                    {
                                        "to": "fe80::250:56ff:fe8d:72bd",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "protocol-name": "OSPF3"
                            }
                        },
                        {
                            "rt-destination": "2001:db8:eb18:ca45::1/128",
                            "rt-entry": {
                                "age": {
                                    "#text": "3w1d 17:03:18"
                                },
                                "metric": "100",
                                "nh": [
                                    {
                                        "to": "fe80::250:56ff:fe8d:72bd",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "protocol-name": "OSPF3"
                            }
                        },
                        {
                            "rt-destination": "2001:db8:eb18:ca45::2/128",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w1d 17:03:18"
                                },
                                "metric": "105",
                                "nh": [
                                    {
                                        "to": "fe80::250:56ff:fe8d:72bd",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "protocol-name": "OSPF3"
                            }
                        },
                        {
                            "rt-destination": "2001:db8:eb18:e26e::/64",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w1d 17:03:18"
                                },
                                "metric": "105",
                                "nh": [
                                    {
                                        "to": "fe80::250:56ff:fe8d:72bd",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "protocol-name": "OSPF3"
                            }
                        },
                        {
                            "rt-destination": "2001:db8:eb18:f5e6::/64",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w0d 04:11:35"
                                },
                                "metric": "225",
                                "nh": [
                                    {
                                        "to": "fe80::250:56ff:fe8d:72bd",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "protocol-name": "OSPF3"
                            }
                        },
                        {
                            "rt-destination": "2001:db8:eb18:6d57::/64",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w1d 17:03:23"
                                },
                                "metric": "125",
                                "nh": [
                                    {
                                        "to": "fe80::250:56ff:fe8d:53c0",
                                        "via": "ge-0/0/0.0"
                                    }
                                ],
                                "preference": "10",
                                "protocol-name": "OSPF3"
                            }
                        },
                        {
                            "rt-destination": "2001:db8:eb18:9627::/64",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w0d 04:51:40"
                                },
                                "metric": "200",
                                "nh": [
                                    {
                                        "to": "fe80::250:56ff:fe8d:72bd",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "protocol-name": "OSPF3"
                            }
                        },
                        {
                            "rt-destination": "2001:db8:223c:ca45::c/128",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w1d 17:03:23"
                                },
                                "metric": "5",
                                "nh": [
                                    {
                                        "to": "fe80::250:56ff:fe8d:53c0",
                                        "via": "ge-0/0/0.0"
                                    }
                                ],
                                "preference": "10",
                                "protocol-name": "OSPF3"
                            }
                        },
                        {
                            "rt-destination": "ff02::5/128",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "29w6d 21:48:09"
                                },
                                "metric": "1",
                                "nh-type": "MultiRecv",
                                "preference": "10",
                                "protocol-name": "OSPF3"
                            }
                        }
                    ],
                    "table-name": "inet6.0",
                    "total-route-count": "23"
                }
            ]
        }
    }

    golden_output_4 = {'execute.return_value': '''
        show route protocol ospf table inet.0

        inet.0: 929 destinations, 1615 routes (929 active, 0 holddown, 0 hidden)
        + = Active Route, - = Last Active, * = Both

        0.0.0.0/0          *[OSPF/150/10] 3w2d 04:45:37, metric 101, tag 0
                            >  to 10.169.14.121 via ge-0/0/1.0
        10.1.0.0/24          [OSPF/150/10] 3w2d 04:45:37, metric 20, tag 0
                            >  to 10.169.14.121 via ge-0/0/1.0
        10.36.3.3/32         *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        10.16.0.0/30         *[OSPF/10/10] 2w6d 06:12:28, metric 1200
                            >  to 10.169.14.121 via ge-0/0/1.0
        10.100.5.5/32         *[OSPF/10/10] 2w6d 06:12:28, metric 1201
                            >  to 10.169.14.121 via ge-0/0/1.0
        10.19.198.28/30    *[OSPF/10/10] 3w0d 18:23:58, metric 1005
                            >  to 10.189.5.94 via ge-0/0/0.0
        10.19.198.239/32   *[OSPF/10/10] 1w5d 22:13:37, metric 1001
                            >  to 10.19.198.26 via ge-0/0/2.0
        10.174.132.237/32   *[OSPF/150/10] 3w2d 04:45:37, metric 150, tag 0
                            >  to 10.169.14.121 via ge-0/0/1.0
        10.34.2.200/30    *[OSPF/10/10] 2w6d 06:12:28, metric 205
                            >  to 10.169.14.121 via ge-0/0/1.0
        10.34.2.250/32    *[OSPF/10/10] 2w6d 06:12:28, metric 200
                            >  to 10.169.14.121 via ge-0/0/1.0
        10.34.2.251/32    *[OSPF/10/10] 2w6d 06:12:28, metric 205
                            >  to 10.169.14.121 via ge-0/0/1.0
        10.15.0.0/30        *[OSPF/10/10] 1w5d 22:13:37, metric 1001
                            >  to 10.19.198.26 via ge-0/0/2.0
        10.64.0.0/30        *[OSPF/10/10] 6d 17:17:33, metric 1201
                            >  to 10.169.14.121 via ge-0/0/1.0
        10.169.196.212/30 *[OSPF/10/10] 2w6d 06:12:28, metric 1200
                            >  to 10.169.14.121 via ge-0/0/1.0
        10.169.196.216/30 *[OSPF/10/10] 2w6d 06:12:28, metric 1205
                            >  to 10.169.14.121 via ge-0/0/1.0
        10.169.196.241/32 *[OSPF/10/10] 6d 17:17:33, metric 1201
                            >  to 10.169.14.121 via ge-0/0/1.0
        10.169.14.16/30   *[OSPF/10/10] 3w2d 04:45:37, metric 105
                            >  to 10.169.14.121 via ge-0/0/1.0
        10.169.14.32/30   *[OSPF/10/10] 2w6d 05:32:25, metric 225
                            >  to 10.169.14.121 via ge-0/0/1.0
        10.169.14.128/30  *[OSPF/10/10] 3w0d 18:23:58, metric 125
                            >  to 10.189.5.94 via ge-0/0/0.0
        10.169.14.156/30  *[OSPF/10/10] 2w6d 06:12:30, metric 200
                            >  to 10.169.14.121 via ge-0/0/1.0
        10.169.14.240/32   [OSPF/10/10] 3w2d 04:45:37, metric 100
                            >  to 10.169.14.121 via ge-0/0/1.0
        10.169.14.241/32  *[OSPF/10/10] 3w2d 04:45:37, metric 105
                            >  to 10.169.14.121 via ge-0/0/1.0
        10.169.14.242/32  *[OSPF/10/10] 3w2d 04:45:37, metric 100
                            >  to 10.169.14.121 via ge-0/0/1.0
        10.169.14.243/32  *[OSPF/10/10] 3w2d 04:45:37, metric 105
                            >  to 10.169.14.121 via ge-0/0/1.0
        10.189.5.253/32    *[OSPF/10/10] 3w0d 18:23:58, metric 5
                            >  to 10.189.5.94 via ge-0/0/0.0
        192.168.220.0/30       *[OSPF/10/10] 2w6d 06:12:28, metric 1200
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.0/32       *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.1/32       *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.2/32       *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.3/32       *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.4/32       *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.5/32       *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.6/32       *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.7/32       *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.8/32       *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.9/32       *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.10/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.11/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.12/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.13/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.14/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.15/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.16/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.17/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.18/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.19/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.20/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.21/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.22/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.23/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.24/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.25/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.26/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.27/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.28/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.29/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.30/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.31/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.32/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.33/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.34/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.35/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.36/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.37/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.38/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.39/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.40/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.41/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.42/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.43/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.44/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.45/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.46/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.47/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.48/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.49/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.50/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.51/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.52/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.53/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.54/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.55/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.56/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.57/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.58/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.59/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.60/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.61/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.62/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.63/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.64/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.65/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.66/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.67/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.68/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.69/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.70/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.71/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.72/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.73/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.74/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.75/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.76/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.77/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.78/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.79/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.80/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.81/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.82/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.83/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.84/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.85/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.86/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.87/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.88/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.89/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.90/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.91/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.92/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.93/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.94/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.95/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.96/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.97/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.98/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.99/32      *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.100/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.101/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.102/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.103/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.104/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.105/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.106/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.107/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.108/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.109/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.110/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.111/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.112/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.113/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.114/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.115/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.116/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.117/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.118/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.119/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.120/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.121/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.122/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.123/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.124/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.125/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.126/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.127/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.128/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.129/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.130/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.131/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.132/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.133/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.134/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.135/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.136/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.137/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.138/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.139/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.140/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.141/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.142/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.143/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.144/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.145/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.146/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.147/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.148/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.149/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.150/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.151/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.152/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.153/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.154/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.155/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.156/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.157/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.158/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.159/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.160/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.161/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.162/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.163/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.164/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.165/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.166/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.167/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.168/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.169/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.170/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.171/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.172/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.173/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.174/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.175/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.176/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.177/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.178/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.179/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.180/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.181/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.182/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.183/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.184/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.185/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.186/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.187/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.188/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.189/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.190/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.191/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.192/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.193/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.194/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.195/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.196/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.197/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.198/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.199/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.220.200/32     *[OSPF/10/10] 6d 17:17:33, metric 1202
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.111.0/30       *[OSPF/10/10] 6d 17:17:33, metric 1201
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.4.0/30       *[OSPF/10/10] 6d 17:17:08, metric 1201
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.100.0/25   *[OSPF/150/10] 2w5d 16:20:47, metric 32000, tag 65000500
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.100.252/32 *[OSPF/150/10] 2w5d 16:20:47, metric 32000, tag 65000500
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.36.48/30  *[OSPF/10/10] 3w2d 04:45:37, metric 10100
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.36.56/30  *[OSPF/10/10] 3w2d 04:45:37, metric 10100
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.36.119/32 *[OSPF/10/10] 3w2d 04:45:37, metric 10101
                            >  to 10.169.14.121 via ge-0/0/1.0
        192.168.36.120/32 *[OSPF/10/10] 3w2d 04:45:37, metric 10101
                            >  to 10.169.14.121 via ge-0/0/1.0
        224.0.0.5/32       *[OSPF/10] 29w5d 23:08:48, metric 1
                            MultiRecv
    '''}

    golden_parsed_output_4 = {
        "route-information": {
            "route-table": [
                {
                    "active-route-count": "929",
                    "destination-count": "929",
                    "hidden-route-count": "0",
                    "holddown-route-count": "0",
                    "rt": [
                        {
                            "rt-destination": "0.0.0.0/0",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w2d 04:45:37"
                                },
                                "metric": "101",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "150",
                                "preference2": "10",
                                "protocol-name": "OSPF",
                                "rt-tag": "0"
                            }
                        },
                        {
                            "rt-destination": "10.1.0.0/24",
                            "rt-entry": {
                                "age": {
                                    "#text": "3w2d 04:45:37"
                                },
                                "metric": "20",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "150",
                                "preference2": "10",
                                "protocol-name": "OSPF",
                                "rt-tag": "0"
                            }
                        },
                        {
                            "rt-destination": "10.36.3.3/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "10.16.0.0/30",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "2w6d 06:12:28"
                                },
                                "metric": "1200",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "10.100.5.5/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "2w6d 06:12:28"
                                },
                                "metric": "1201",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "10.19.198.28/30",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w0d 18:23:58"
                                },
                                "metric": "1005",
                                "nh": [
                                    {
                                        "to": "10.189.5.94",
                                        "via": "ge-0/0/0.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "10.19.198.239/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w5d 22:13:37"
                                },
                                "metric": "1001",
                                "nh": [
                                    {
                                        "to": "10.19.198.26",
                                        "via": "ge-0/0/2.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "10.174.132.237/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w2d 04:45:37"
                                },
                                "metric": "150",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "150",
                                "preference2": "10",
                                "protocol-name": "OSPF",
                                "rt-tag": "0"
                            }
                        },
                        {
                            "rt-destination": "10.34.2.200/30",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "2w6d 06:12:28"
                                },
                                "metric": "205",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "10.34.2.250/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "2w6d 06:12:28"
                                },
                                "metric": "200",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "10.34.2.251/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "2w6d 06:12:28"
                                },
                                "metric": "205",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "10.15.0.0/30",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "1w5d 22:13:37"
                                },
                                "metric": "1001",
                                "nh": [
                                    {
                                        "to": "10.19.198.26",
                                        "via": "ge-0/0/2.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "10.64.0.0/30",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1201",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "10.169.196.212/30",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "2w6d 06:12:28"
                                },
                                "metric": "1200",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "10.169.196.216/30",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "2w6d 06:12:28"
                                },
                                "metric": "1205",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "10.169.196.241/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1201",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "10.169.14.16/30",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w2d 04:45:37"
                                },
                                "metric": "105",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "10.169.14.32/30",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "2w6d 05:32:25"
                                },
                                "metric": "225",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "10.169.14.128/30",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w0d 18:23:58"
                                },
                                "metric": "125",
                                "nh": [
                                    {
                                        "to": "10.189.5.94",
                                        "via": "ge-0/0/0.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "10.169.14.156/30",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "2w6d 06:12:30"
                                },
                                "metric": "200",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "10.169.14.240/32",
                            "rt-entry": {
                                "age": {
                                    "#text": "3w2d 04:45:37"
                                },
                                "metric": "100",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "10.169.14.241/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w2d 04:45:37"
                                },
                                "metric": "105",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "10.169.14.242/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w2d 04:45:37"
                                },
                                "metric": "100",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "10.169.14.243/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w2d 04:45:37"
                                },
                                "metric": "105",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "10.189.5.253/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w0d 18:23:58"
                                },
                                "metric": "5",
                                "nh": [
                                    {
                                        "to": "10.189.5.94",
                                        "via": "ge-0/0/0.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.0/30",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "2w6d 06:12:28"
                                },
                                "metric": "1200",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.0/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.1/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.2/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.3/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.4/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.5/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.6/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.7/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.8/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.9/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.10/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.11/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.12/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.13/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.14/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.15/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.16/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.17/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.18/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.19/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.20/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.21/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.22/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.23/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.24/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.25/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.26/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.27/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.28/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.29/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.30/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.31/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.32/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.33/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.34/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.35/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.36/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.37/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.38/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.39/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.40/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.41/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.42/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.43/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.44/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.45/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.46/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.47/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.48/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.49/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.50/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.51/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.52/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.53/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.54/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.55/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.56/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.57/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.58/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.59/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.60/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.61/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.62/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.63/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.64/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.65/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.66/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.67/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.68/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.69/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.70/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.71/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.72/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.73/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.74/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.75/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.76/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.77/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.78/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.79/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.80/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.81/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.82/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.83/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.84/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.85/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.86/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.87/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.88/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.89/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.90/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.91/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.92/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.93/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.94/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.95/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.96/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.97/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.98/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.99/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.100/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.101/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.102/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.103/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.104/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.105/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.106/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.107/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.108/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.109/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.110/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.111/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.112/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.113/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.114/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.115/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.116/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.117/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.118/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.119/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.120/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.121/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.122/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.123/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.124/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.125/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.126/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.127/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.128/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.129/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.130/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.131/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.132/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.133/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.134/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.135/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.136/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.137/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.138/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.139/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.140/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.141/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.142/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.143/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.144/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.145/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.146/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.147/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.148/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.149/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.150/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.151/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.152/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.153/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.154/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.155/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.156/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.157/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.158/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.159/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.160/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.161/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.162/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.163/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.164/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.165/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.166/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.167/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.168/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.169/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.170/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.171/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.172/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.173/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.174/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.175/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.176/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.177/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.178/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.179/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.180/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.181/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.182/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.183/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.184/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.185/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.186/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.187/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.188/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.189/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.190/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.191/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.192/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.193/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.194/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.195/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.196/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.197/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.198/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.199/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.220.200/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1202",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.111.0/30",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:33"
                                },
                                "metric": "1201",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.4.0/30",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "6d 17:17:08"
                                },
                                "metric": "1201",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.100.0/25",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "2w5d 16:20:47"
                                },
                                "metric": "32000",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "150",
                                "preference2": "10",
                                "protocol-name": "OSPF",
                                "rt-tag": "65000500"
                            }
                        },
                        {
                            "rt-destination": "192.168.100.252/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "2w5d 16:20:47"
                                },
                                "metric": "32000",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "150",
                                "preference2": "10",
                                "protocol-name": "OSPF",
                                "rt-tag": "65000500"
                            }
                        },
                        {
                            "rt-destination": "192.168.36.48/30",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w2d 04:45:37"
                                },
                                "metric": "10100",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.36.56/30",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w2d 04:45:37"
                                },
                                "metric": "10100",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.36.119/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w2d 04:45:37"
                                },
                                "metric": "10101",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "192.168.36.120/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "3w2d 04:45:37"
                                },
                                "metric": "10101",
                                "nh": [
                                    {
                                        "to": "10.169.14.121",
                                        "via": "ge-0/0/1.0"
                                    }
                                ],
                                "preference": "10",
                                "preference2": "10",
                                "protocol-name": "OSPF"
                            }
                        },
                        {
                            "rt-destination": "224.0.0.5/32",
                            "rt-entry": {
                                "active-tag": "*",
                                "age": {
                                    "#text": "29w5d 23:08:48"
                                },
                                "metric": "1",
                                "nh-type": "MultiRecv",
                                "preference": "10",
                                "protocol-name": "OSPF"
                            }
                        }
                    ],
                    "table-name": "inet.0",
                    "total-route-count": "1615"
                }
            ]
        }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowRouteProtocol(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(
                protocol='static',
                ip_address='10.169.14.240/32')

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowRouteProtocol(device=self.device)
        parsed_output = obj.parse(
            protocol='static',
            ip_address='10.169.14.240/32')
        self.assertEqual(parsed_output, self.golden_parsed_output)
    
    def test_golden_2(self):
        self.device = Mock(**self.golden_output_2)
        obj = ShowRouteProtocol(device=self.device)
        parsed_output = obj.parse(
            protocol='static',
            ip_address='2001:db8:eb18:ca45::1')
        self.assertEqual(parsed_output, self.golden_parsed_output_2)
    
    def test_golden_3(self):
        self.device = Mock(**self.golden_output_3)
        obj = ShowRouteProtocol(device=self.device)
        parsed_output = obj.parse(
            protocol='ospf')
        self.assertEqual(parsed_output, self.golden_parsed_output_3)

    def test_golden_4(self):
        self.device = Mock(**self.golden_output_4)
        obj = ShowRouteProtocol(device=self.device)
        parsed_output = obj.parse(
            protocol='ospf',
            table='inet.0')
        self.assertEqual(parsed_output, self.golden_parsed_output_4)

if __name__ == '__main__':
    unittest.main()
