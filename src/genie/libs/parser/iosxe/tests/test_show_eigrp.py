# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# iosxe show ip eigrp
from genie.libs.parser.iosxe.show_eigrp import ShowIpEigrpNeighbors,\
                                               ShowIpv6EigrpNeighbors,\
                                               ShowIpEigrpNeighborsDetail,\
                                               ShowIpv6EigrpNeighborsDetail

class test_show_eigrp_neighbors(unittest.TestCase):

    device = Device(name='aDevice')

    expected_parsed_output_1 = {
        'eigrp_instance': {
            '': {
                'vrf': {
                    'default': {
                        'address_family': {
                            'ipv4': {
                                'name': '',
                                'named_mode': False,
                                'eigrp_interface': {
                                    'GigabitEthernet0/0': {
                                        'eigrp_nbr': {
                                            '10.1.1.2': {
                                                'peer_handle': 0,
                                                'hold': 13,
                                                'uptime': '00:00:03',
                                                'srtt': 1.996,
                                                'rto': 5000,
                                                'q_cnt': 0,
                                                'last_seq_number': 5}}}}}}}}}}}

    device_output_1 = {'execute.return_value': '''
        Device# show ip eigrp neighbors
        H   Address      Interface  Hold  Uptime    SRTT   RTO    Q   Seq
                                    (sec)           (ms)          Cnt Num
        0   10.1.1.2     Gi0/0      13    00:00:03  1996   5000   0   5
    '''}

    expected_parsed_output_2 = {
        'eigrp_instance': {
            '': {
                'vrf': {
                    'default': {
                        'address_family': {
                            'ipv4': {
                                'name': '',
                                'named_mode': False,
                                'eigrp_interface': {
                                    'GigabitEthernet0/0': {
                                        'eigrp_nbr': {
                                            '10.1.1.9': {
                                                'peer_handle': 2,
                                                'hold': 14,
                                                'uptime': '00:02:24',
                                                'srtt': 0.206,
                                                'rto': 5000,
                                                'q_cnt': 0,
                                                'last_seq_number': 5
                                            },
                                            '10.1.1.2': {
                                                'peer_handle': 0,
                                                'hold': 13,
                                                'uptime': '00:00:03',
                                                'srtt': 1.996,
                                                'rto': 5000,
                                                'q_cnt': 0,
                                                'last_seq_number': 5}}}}}}}}}}}

    device_output_2 = {'execute.return_value': '''
        Device# show ip eigrp neighbors
        H   Address      Interface  Hold  Uptime    SRTT   RTO    Q   Seq
                                    (sec)           (ms)          Cnt Num
        2   10.1.1.9     Gi0/0      14    00:02:24  206    5000   0   5
        0   10.1.1.2     Gi0/0      13    00:00:03  1996   5000   0   5
    '''}

    expected_parsed_output_3 = {
        'eigrp_instance': {
            '': {
                'vrf': {
                    'default': {
                        'address_family': {
                            'ipv4': {
                                'name': '',
                                'named_mode': False,
                                'eigrp_interface': {
                                    'GigabitEthernet0/0': {
                                        'eigrp_nbr': {
                                            '10.1.1.9': {
                                                'peer_handle': 2,
                                                'hold': 14,
                                                'uptime': '00:02:24',
                                                'srtt': 0.206,
                                                'rto': 5000,
                                                'q_cnt': 0,
                                                'last_seq_number': 5
                                            }
                                        }
                                    },
                                    'GigabitEthernet0/1': {
                                        'eigrp_nbr': {
                                            '10.1.2.3': {
                                                'peer_handle': 1,
                                                'hold': 11,
                                                'uptime': '00:20:39',
                                                'srtt': 2.202,
                                                'rto': 5000,
                                                'q_cnt': 0,
                                                'last_seq_number': 5}}}}}}}}}}}

    device_output_3 = {'execute.return_value': '''
        Device# show ip eigrp neighbors
        H   Address      Interface  Hold  Uptime    SRTT   RTO    Q   Seq
                                    (sec)           (ms)          Cnt Num
        2   10.1.1.9     Gi0/0      14    00:02:24  206    5000   0   5
        1   10.1.2.3     Gi0/1      11    00:20:39  2202   5000   0   5
    '''}

    expected_parsed_output_4 ={
        'eigrp_instance': {
            '': {
                'vrf': {
                    'default': {
                        'address_family': {
                            'ipv4': {
                                'name': '',
                                'named_mode': False,
                                'eigrp_interface': {
                                    'GigabitEthernet0/0': {
                                        'eigrp_nbr': {
                                            '10.1.1.2': {
                                                'peer_handle': 0,
                                                'hold': 13,
                                                'uptime': '00:00:03',
                                                'srtt': 1.996,
                                                'rto': 5000,
                                                'q_cnt': 0,
                                                'last_seq_number': 5
                                            },
                                            '10.1.1.9': {
                                                'peer_handle': 2,
                                                'hold': 14,
                                                'uptime': '00:02:24',
                                                'srtt': 0.206,
                                                'rto': 5000,
                                                'q_cnt': 0,
                                                'last_seq_number': 5
                                            }
                                        }
                                    },
                                    'GigabitEthernet0/1': {
                                        'eigrp_nbr': {
                                            '10.1.2.3': {
                                                'peer_handle': 1,
                                                'hold': 11,
                                                'uptime': '00:20:39',
                                                'srtt': 2.202,
                                                'rto': 5000,
                                                'q_cnt': 0,
                                                'last_seq_number': 5}}}}}}}}}}}

    device_output_4 = {'execute.return_value': '''
        Device# show ip eigrp neighbors

        H   Address     Interface       Hold Uptime   SRTT   RTO  Q  Seq
                                        (sec)         (ms)       Cnt Num
        0   10.1.1.2     Gi0/0           13 00:00:03  1996   5000  0  5
        2   10.1.1.9     Gi0/0           14 00:02:24   206   5000  0  5
        1   10.1.2.3     Gi0/1           11 00:20:39  2202   5000  0  5

    '''}

    expected_parsed_output_5 = {
        'eigrp_instance': {
            '': {
                'vrf': {
                    'default': {
                        'address_family': {
                            'ipv4': {
                                'name': '',
                                'named_mode': False,
                                'eigrp_interface': {
                                    'GigabitEthernet0/0': {
                                        'eigrp_nbr': {
                                            '10.1.1.2': {
                                                'peer_handle': 0,
                                                'hold': 13,
                                                'uptime': '00:00:03',
                                                'srtt': 1.996,
                                                'rto': 5000,
                                                'q_cnt': 0,
                                                'last_seq_number': 5
                                            },
                                            '10.1.1.9': {
                                                'peer_handle': 2,
                                                'hold': 14,
                                                'uptime': '00:02:24',
                                                'srtt': 0.206,
                                                'rto': 5000,
                                                'q_cnt': 0,
                                                'last_seq_number': 5
                                            }
                                        }
                                    },
                                    'GigabitEthernet0/1': {
                                        'eigrp_nbr': {
                                            '10.1.2.3': {
                                                'peer_handle': 1,
                                                'hold': 11,
                                                'uptime': '00:20:39',
                                                'srtt': 2.202,
                                                'rto': 5000,
                                                'q_cnt': 0,
                                                'last_seq_number': 5}}}}}}}}}}}

    device_output_5 = {'execute.return_value': '''
        Device# show ip eigrp neighbors

        H   Address     Interface       Hold Uptime   SRTT   RTO  Q  Seq
                                        (sec)         (ms)       Cnt Num
        0   10.1.1.2     Gi0/0           13 00:00:03  1996   5000  0  5
        2   10.1.1.9     Gi0/0           14 00:02:24   206   5000  0  5
        1   10.1.2.3     Gi0/1           11 00:20:39  2202   5000  0  5

    '''}

    expected_parsed_output_6 = {
        'eigrp_instance': {
            '': {
                'vrf': {
                    'default': {
                        'address_family': {
                            'ipv4': {
                                'name': '',
                                'named_mode': False,
                                'eigrp_interface': {
                                    'Ethernet0/0': {
                                        'eigrp_nbr': {
                                            '10.1.1.2': {
                                                'peer_handle': 0,
                                                'hold': 13,
                                                'uptime': '00:00:03',
                                                'srtt': 1.996,
                                                'rto': 5000,
                                                'q_cnt': 0,
                                                'last_seq_number': 5
                                            },
                                            '10.1.1.9': {
                                                'peer_handle': 2,
                                                'hold': 14,
                                                'uptime': '00:02:24',
                                                'srtt': 0.206,
                                                'rto': 5000,
                                                'q_cnt': 0,
                                                'last_seq_number': 5
                                            }
                                        }
                                    },
                                    'Ethernet0/1': {
                                        'eigrp_nbr': {
                                            '10.1.2.3': {
                                                'peer_handle': 1,
                                                'hold': 11,
                                                'uptime': '00:20:39',
                                                'srtt': 2.202,
                                                'rto': 5000,
                                                'q_cnt': 0,
                                                'last_seq_number': 5}}}}}}}}}}}

    device_output_6 = {'execute.return_value': '''
        Router# show ip eigrp neighbors

        H   Address     Interface       Hold Uptime   SRTT   RTO  Q  Seq
                                        (sec)         (ms)       Cnt Num
        0   10.1.1.2     Et0/0             13 00:00:03 1996  5000  0  5
        2   10.1.1.9     Et0/0             14 00:02:24 206   5000  0  5
        1   10.1.2.3     Et0/1             11 00:20:39 2202  5000  0  5

    '''}

    expected_parsed_output_7 = {
        'eigrp_instance': {
            '1100': {
                'vrf': {
                    'VRF1': {
                        'address_family': {
                            'ipv4': {
                                'name': '',
                                'named_mode': False,
                                'eigrp_interface': {
                                    'GigabitEthernet3': {
                                        'eigrp_nbr': {
                                            '10.1.2.2': {
                                                'peer_handle': 0,
                                                'hold': 13,
                                                'uptime': '00:01:01',
                                                'srtt': 0.002,
                                                'rto': 100,
                                                'q_cnt': 0,
                                                'last_seq_number': 2}}}}}}}}}}}

    device_output_7 = {'execute.return_value': '''
        R1#show ip eigrp vrf VRF1 neighbors

        EIGRP-IPv4 Neighbors for AS(1100) VRF(VRF1)
        H   Address                 Interface              Hold Uptime   SRTT   RTO  Q  Seq
                                                           (sec)         (ms)       Cnt Num
        0   10.1.2.2                Gi3                      13 00:01:01    2   100  0  2
    '''}

    expected_parsed_output_8 = {
        'eigrp_instance': {
            '100': {
                'vrf': {
                    'default': {
                        'address_family': {
                            'ipv6': {
                                'name': 'test',
                                'named_mode': True,
                                'eigrp_interface': {
                                    'GigabitEthernet3.90': {
                                        'eigrp_nbr': {
                                            'FE80::5C00:FF:FE02:7': {
                                                'peer_handle': 1,
                                                'hold': 11,
                                                'uptime': '01:29:00',
                                                'srtt': 0.01,
                                                'rto': 100,
                                                'q_cnt': 0,
                                                'last_seq_number': 29}}},
                                    'GigabitEthernet2.90': {
                                        'eigrp_nbr': {
                                            'FE80::F816:3EFF:FE3D:AC68': {
                                                'peer_handle': 0,
                                                'hold': 14,
                                                'uptime': '02:23:03',
                                                'srtt': 0.01,
                                                'rto': 100,
                                                'q_cnt': 0,
                                                'last_seq_number': 29}}}}}}}}}}}


    device_output_8 = {'execute.return_value': '''
        R1_xe#show ipv6 eigrp neighbors 
        EIGRP-IPv6 VR(test) Address-Family Neighbors for AS(100)
        H   Address                 Interface              Hold Uptime   SRTT   RTO  Q  Seq
                                                           (sec)         (ms)       Cnt Num
        1   Link-local address:     Gi3.90                   11 01:29:00   10   100  0  29
            FE80::5C00:FF:FE02:7
        0   Link-local address:     Gi2.90                   14 02:23:03   10   100  0  29
            FE80::F816:3EFF:FE3D:AC68
    '''}

    expected_parsed_output_9 = {
        'eigrp_instance': {
            '100': {
                'vrf': {
                    'VRF1': {
                        'address_family': {
                            'ipv4': {
                                'name': 'test',
                                'named_mode': True,
                                'eigrp_interface': {
                                    'GigabitEthernet2.390': {
                                        'eigrp_nbr': {
                                            '10.12.90.2': {
                                                'peer_handle': 1,
                                                'hold': 13,
                                                'uptime': '2d10h',
                                                'srtt': 0.024,
                                                'rto': 144,
                                                'q_cnt': 0,
                                                'last_seq_number': 8
                                            }
                                        }
                                    },
                                    'GigabitEthernet3.390': {
                                        'eigrp_nbr': {
                                            '10.13.90.3': {
                                                'peer_handle': 0,
                                                'hold': 10,
                                                'uptime': '2d10h',
                                                'srtt': 0.005,
                                                'rto': 100,
                                                'q_cnt': 0,
                                                'last_seq_number': 9}}}}}}}}}}}

    device_output_9 = {'execute.return_value': '''
        # show ip eigrp vrf VRF1 neighbors
        EIGRP-IPv4 VR(test) Address-Family Neighbors for AS(100) 
                   VRF(VRF1)
        H   Address                 Interface              Hold Uptime   SRTT   RTO  Q  Seq
                                                           (sec)         (ms)       Cnt Num
        1   10.12.90.2              Gi2.390                  13 2d10h      24   144  0  8
        0   10.13.90.3              Gi3.390                  10 2d10h       5   100  0  9
    '''}

    expected_parsed_output_10 = {
        'eigrp_instance': {
            '100': {
                'vrf': {
                    'default': {
                        'address_family': {
                            'ipv4': {
                                'name': 'test',
                                'named_mode': True,
                                'eigrp_interface': {
                                    'GigabitEthernet2.90': {
                                        'eigrp_nbr': {
                                            '10.12.90.2': {
                                                'peer_handle': 1,
                                                'hold': 13,
                                                'uptime': '2d10h',
                                                'srtt': 1.283,
                                                'rto': 5000,
                                                'q_cnt': 0,
                                                'last_seq_number': 5
                                            }
                                        }
                                    },
                                    'GigabitEthernet3.90': {
                                        'eigrp_nbr': {
                                            '10.13.90.3': {
                                                'peer_handle': 0,
                                                'hold': 11,
                                                'uptime': '2d10h',
                                                'srtt': 0.006,
                                                'rto': 100,
                                                'q_cnt': 0,
                                                'last_seq_number': 9}}}}}}}}}}}

    device_output_10 = {'execute.return_value': '''
        # show ip eigrp neighbors
        EIGRP-IPv4 VR(test) Address-Family Neighbors for AS(100)
        H   Address                 Interface              Hold Uptime   SRTT   RTO  Q  Seq
                                                           (sec)         (ms)       Cnt Num
        1   10.12.90.2              Gi2.90                   13 2d10h    1283  5000  0  5
        0   10.13.90.3              Gi3.90                   11 2d10h       6   100  0  9
    '''}

    device_output_empty = {'execute.return_value': ''}

    def test_show_eigrp_neighbors_1(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_1)
        obj = ShowIpEigrpNeighbors(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_1)

    def test_show_eigrp_neighbors_2(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_2)
        obj = ShowIpEigrpNeighbors(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_2)

    def test_show_eigrp_neighbors_3(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_3)
        obj = ShowIpEigrpNeighbors(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_3)

    def test_show_eigrp_neighbors_4(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_4)
        obj = ShowIpEigrpNeighbors(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_4)

    def test_show_eigrp_neighbors_5(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_5)
        obj = ShowIpEigrpNeighbors(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_5)

    def test_show_eigrp_neighbors_6(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_6)
        obj = ShowIpEigrpNeighbors(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_6)

    def test_show_eigrp_neighbors_7(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_7)
        obj = ShowIpEigrpNeighbors(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_7)

    def test_show_eigrp_neighbors_8(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_8)
        obj = ShowIpv6EigrpNeighbors(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_8)

    def test_show_eigrp_neighbors_9(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_9)
        obj = ShowIpEigrpNeighbors(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_9)

    def test_show_eigrp_neighbors_10(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_10)
        obj = ShowIpEigrpNeighbors(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_10)

    def test_show_eigrp_neighbors_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_empty)
        obj = ShowIpEigrpNeighbors(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


class test_show_eigrp_neighbors_detail(unittest.TestCase):

    device = Device(name='aDevice')

    expected_parsed_output_1 = {
        'eigrp_instance': {
            '100': {
                'vrf': {
                    'default': {
                        'address_family': {
                            'ipv4': {
                                'name': '',
                                'named_mode': False,
                                'eigrp_interface': {
                                    'Ethernet1/0': {
                                        'eigrp_nbr': {
                                            '10.1.2.1': {
                                                'hold': 11,
                                                'last_seq_number': 6,
                                                'nbr_sw_ver': {
                                                    'os_majorver': 5,
                                                    'os_minorver': 1,
                                                    'tlv_majorrev': 3,
                                                    'tlv_minorrev': 0},
                                                'peer_handle': 0,
                                                'prefixes': 1,
                                                'q_cnt': 0,
                                                'retransmit_count': 2,
                                                'retry_count': 0,
                                                'rto': 200,
                                                'srtt': 12.0,
                                                'topology_ids_from_peer': 0,
                                                'uptime': '00:02:31',
                                                'topology_advert_to_peer': ''}}}}}}}}}}}

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

    expected_parsed_output_2 = {
        'eigrp_instance': {
            '1': {
                'vrf': {
                    'default': {
                        'address_family': {
                            'ipv4': {
                                'name': 'foo',
                                'named_mode': True,
                                'eigrp_interface': {
                                    'GigabitEthernet2/0': {
                                        'eigrp_nbr': {
                                            '192.168.10.1': {
                                                'peer_handle': 0, 
                                                'hold': 12, 
                                                'uptime': '00:00:21', 
                                                'srtt': 1600.0, 
                                                'rto': 5000, 
                                                'q_cnt': 0, 
                                                'last_seq_number': 3, 
                                                'nbr_sw_ver': {
                                                    'os_majorver': 8, 
                                                    'os_minorver': 0, 
                                                    'tlv_majorrev': 2, 
                                                    'tlv_minorrev': 0}, 
                                                'retransmit_count': 0, 
                                                'retry_count': 0, 
                                                'prefixes': 1, 
                                                'topology_ids_from_peer': 0,
                                                'topology_advert_to_peer': '',}}}}}}}}}}}

    device_output_2 = {'execute.return_value': '''
        Device# show ip eigrp neighbors detail

        EIGRP-IPv4 VR(foo) Address-Family Neighbors for AS(1)
        H   Address                 Interface       Hold Uptime   SRTT   RTO  Q  Seq
                                            (sec)         (ms)       Cnt Num
        0   192.168.10.1                 Gi2/0       12 00:00:21 1600  5000  0  3
        Version 8.0/2.0, Retrans: 0, Retries: 0, Prefixes: 1
        Topology-ids from peer - 0
    '''}

    expected_parsed_output_3 = {
        'eigrp_instance': {
            '1100': {
                'vrf': {
                    'VRF1': {
                        'address_family': {
                            'ipv4': {
                                'name': '',
                                'named_mode': False,
                                'eigrp_interface': {
                                    'GigabitEthernet3': {
                                        'eigrp_nbr': {
                                            '10.1.2.2': {
                                                'hold': 11,
                                                'last_seq_number': 2,
                                                'nbr_sw_ver': {
                                                    'os_majorver': 23,
                                                    'os_minorver': 0,
                                                    'tlv_majorrev': 2,
                                                    'tlv_minorrev': 0},
                                                'peer_handle': 0,
                                                'prefixes': 0,
                                                'q_cnt': 0,
                                                'retransmit_count': 0,
                                                'retry_count': 0,
                                                'rto': 100,
                                                'srtt': 2.0,
                                                'topology_ids_from_peer': 0,
                                                'topology_advert_to_peer': 'base',
                                                'uptime': '00:01:03'}}}}}}}}}}}

    device_output_3 = {'execute.return_value': '''
        R1#show ip eigrp vrf VRF1 neighbors detail 
        EIGRP-IPv4 Neighbors for AS(1100) VRF(VRF1)
        H   Address                 Interface              Hold Uptime   SRTT   RTO  Q  Seq
                                                   (sec)         (ms)       Cnt Num
        0   10.1.2.2                Gi3                      11 00:01:03    2   100  0  2
        Version 23.0/2.0, Retrans: 0, Retries: 0
        Topology-ids from peer - 0 
        Topologies advertised to peer:   base

        Max Nbrs: 0, Current Nbrs: 0
    '''}

    expected_parsed_output_4 = {
        'eigrp_instance': {
            '1': {
                'vrf': {
                    'VRF1': {
                        'address_family': {
                            'ipv4': {
                                'name': 'foo',
                                'named_mode': True,
                                'eigrp_interface': {
                                    'GigabitEthernet3': {
                                        'eigrp_nbr': {
                                            '10.1.2.2': {
                                                'peer_handle': 0,
                                                'hold': 11,
                                                'uptime': '00:01:03',
                                                'srtt': 2.0,
                                                'rto': 100,
                                                'q_cnt': 0,
                                                'last_seq_number': 2,
                                                'nbr_sw_ver': {
                                                    'os_majorver': 23,
                                                    'os_minorver': 0,
                                                    'tlv_majorrev': 2,
                                                    'tlv_minorrev': 0
                                                },
                                                'retransmit_count': 0,
                                                'retry_count': 0,
                                                'prefixes': 0,
                                                'topology_ids_from_peer': 0,
                                                'topology_advert_to_peer': 'base'}}}}}}}}}}}

    device_output_4 = {'execute.return_value': '''
        R1#show ip eigrp vrf VRF1 neighbors detail 
        EIGRP-IPv4 VR(foo) Address-Family Neighbors for AS(1) VRF(VRF1)
        H   Address                 Interface              Hold Uptime   SRTT   RTO  Q  Seq
                                                   (sec)         (ms)       Cnt Num
        0   10.1.2.2                Gi3                      11 00:01:03    2   100  0  2
        Version 23.0/2.0, Retrans: 0, Retries: 0
        Topology-ids from peer - 0 
        Topologies advertised to peer:   base

        Max Nbrs: 0, Current Nbrs: 0
    '''}

    expected_parsed_output_5 = {
        'eigrp_instance': {
            '100': {
                'vrf': {
                    'default': {
                        'address_family': {
                            'ipv6': {
                                'name': 'test',
                                'named_mode': True,
                                'eigrp_interface': {
                                    'GigabitEthernet3.90': {
                                        'eigrp_nbr': {
                                            'FE80::5C00:FF:FE02:7': {
                                                'peer_handle': 1,
                                                'hold': 11,
                                                'uptime': '01:30:32',
                                                'srtt': 0.01,
                                                'rto': 100,
                                                'q_cnt': 0,
                                                'last_seq_number': 29,
                                                'nbr_sw_ver': {
                                                    'os_majorver': 8,
                                                    'os_minorver': 0,
                                                    'tlv_majorrev': 1,
                                                    'tlv_minorrev': 2
                                                },
                                                'retransmit_count': 0,
                                                'retry_count': 0,
                                                'prefixes': 4,
                                                'topology_ids_from_peer': 0,
                                                'topology_advert_to_peer': 'base'
                                            }
                                        }
                                    },
                                    'GigabitEthernet2.90': {
                                        'eigrp_nbr': {
                                            'FE80::F816:3EFF:FE3D:AC68': {
                                                'peer_handle': 0,
                                                'hold': 14,
                                                'uptime': '02:24:36',
                                                'srtt': 0.01,
                                                'rto': 100,
                                                'q_cnt': 0,
                                                'last_seq_number': 29,
                                                'nbr_sw_ver': {
                                                    'os_majorver': 3,
                                                    'os_minorver': 3,
                                                    'tlv_majorrev': 2,
                                                    'tlv_minorrev': 0
                                                },
                                                'retransmit_count': 1,
                                                'retry_count': 0,
                                                'prefixes': 4,
                                                'topology_ids_from_peer': 0,
                                                'topology_advert_to_peer': 'base'}}}}}}}}}}}

    device_output_5 = {'execute.return_value': '''
        R1_xe#show ipv6 eigrp neighbors detail 
        EIGRP-IPv6 VR(test) Address-Family Neighbors for AS(100)
        H   Address                 Interface              Hold Uptime   SRTT   RTO  Q  Seq
                                                           (sec)         (ms)       Cnt Num
        1   Link-local address:     Gi3.90                   11 01:30:32   10   100  0  29
            FE80::5C00:FF:FE02:7
        Version 8.0/1.2, Retrans: 0, Retries: 0, Prefixes: 4
        Topology-ids from peer - 0 
        Topologies advertised to peer:   base

        0   Link-local address:     Gi2.90                   14 02:24:36   10   100  0  29
            FE80::F816:3EFF:FE3D:AC68
        Version 3.3/2.0, Retrans: 1, Retries: 0, Prefixes: 4
        Topology-ids from peer - 0 
        Topologies advertised to peer:   base
    '''}


    expected_parsed_output_6 = {
        'eigrp_instance': {
            '100': {
                'vrf': {
                    'default': {
                        'address_family': {
                            'ipv4': {
                                'name': 'test',
                                'named_mode': True,
                                'eigrp_interface': {
                                    'GigabitEthernet2.90': {
                                        'eigrp_nbr': {
                                            '10.12.90.2': {
                                                'peer_handle': 1,
                                                'hold': 12,
                                                'uptime': '2d10h',
                                                'srtt': 1283.0,
                                                'rto': 5000,
                                                'q_cnt': 0,
                                                'last_seq_number': 5,
                                                'topology_advert_to_peer': 'base',
                                                'nbr_sw_ver': {
                                                    'os_majorver': 3,
                                                    'os_minorver': 3,
                                                    'tlv_majorrev': 2,
                                                    'tlv_minorrev': 0
                                                },
                                                'retransmit_count': 0,
                                                'retry_count': 0,
                                                'prefixes': 3,
                                                'topology_ids_from_peer': 0
                                            }
                                        }
                                    },
                                    'GigabitEthernet3.90': {
                                        'eigrp_nbr': {
                                            '10.13.90.3': {
                                                'peer_handle': 0,
                                                'hold': 10,
                                                'uptime': '2d10h',
                                                'srtt': 6.0,
                                                'rto': 100,
                                                'q_cnt': 0,
                                                'last_seq_number': 9,
                                                'topology_advert_to_peer': 'base',
                                                'nbr_sw_ver': {
                                                    'os_majorver': 8,
                                                    'os_minorver': 0,
                                                    'tlv_majorrev': 1,
                                                    'tlv_minorrev': 2
                                                },
                                                'retransmit_count': 1,
                                                'retry_count': 0,
                                                'prefixes': 3,
                                                'topology_ids_from_peer': 0}}}}}}}}}}}

    device_output_6 = {'execute.return_value': '''
        #show ip eigrp neighbors detail
        EIGRP-IPv4 VR(test) Address-Family Neighbors for AS(100)
        H   Address                 Interface              Hold Uptime   SRTT   RTO  Q  Seq
                                                           (sec)         (ms)       Cnt Num
        1   10.12.90.2              Gi2.90                   12 2d10h    1283  5000  0  5
           Version 3.3/2.0, Retrans: 0, Retries: 0, Prefixes: 3
           Topology-ids from peer - 0
           Topologies advertised to peer:   base

        0   10.13.90.3              Gi3.90                   10 2d10h       6   100  0  9
           Version 8.0/1.2, Retrans: 1, Retries: 0, Prefixes: 3
           Topology-ids from peer - 0
           Topologies advertised to peer:   base

        Max Nbrs: 0, Current Nbrs: 0
    '''}

    device_output_empty = {'execute.return_value': ''}

    def test_show_eigrp_neighbors_detail_1(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_1)
        obj = ShowIpEigrpNeighborsDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_1)

    def test_show_eigrp_neighbors_detail_2(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_2)
        obj = ShowIpEigrpNeighborsDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_2)

    def test_show_eigrp_neighbors_detail_3(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_3)
        obj = ShowIpEigrpNeighborsDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_3)

    def test_show_eigrp_neighbors_detail_4(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_4)
        obj = ShowIpEigrpNeighborsDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_4)

    def test_show_eigrp_neighbors_detail_5(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_5)
        obj = ShowIpv6EigrpNeighborsDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_5)

    def test_show_eigrp_neighbors_detail_6(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_6)
        obj = ShowIpEigrpNeighborsDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_6)

    def test_show_eigrp_neighbors_detail_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_empty)
        obj = ShowIpEigrpNeighborsDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


if __name__ == '__main__':
    unittest.main()
