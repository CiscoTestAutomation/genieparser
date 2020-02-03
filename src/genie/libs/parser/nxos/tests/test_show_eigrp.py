# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# nxos show ip eigrp
from genie.libs.parser.nxos.show_eigrp import ShowIpv4EigrpNeighbors,\
                                              ShowIpv6EigrpNeighbors,\
                                              ShowIpv4EigrpNeighborsDetail,\
                                              ShowIpv6EigrpNeighborsDetail


class test_show_eigrp_neighbors(unittest.TestCase):

    device = Device(name='aDevice')

    expected_parsed_output_1 = {
        'eigrp_instance': {
            '100': {
                'vrf': {
                    'default': {
                        'address_family': {
                            'ipv4': {
                                'eigrp_interface': {
                                    'Ethernet1/2.90': {
                                        'eigrp_nbr': {
                                            '10.13.90.1': {
                                                'peer_handle': 1,
                                                'hold': 13,
                                                'uptime': '01:56:49',
                                                'srtt': 0.001,
                                                'rto': 50,
                                                'q_cnt': 0,
                                                'last_seq_number': 16, }}},
                                    'Ethernet1/1.90': {
                                        'eigrp_nbr': {
                                            '10.23.90.2': {
                                                'peer_handle': 0,
                                                'hold': 11,
                                                'uptime': '01:46:12',
                                                'srtt': 0.015,
                                                'rto': 90,
                                                'q_cnt': 0,
                                                'last_seq_number': 22, }}}}}}},
                    'VRF1': {
                        'address_family': {
                            'ipv4': {
                                'eigrp_interface': {
                                    'Ethernet1/2.390': {
                                        'eigrp_nbr': {
                                            '10.13.90.1': {
                                                'peer_handle': 1,
                                                'hold': 13,
                                                'uptime': '01:43:23',
                                                'srtt': 0.001,
                                                'rto': 50,
                                                'q_cnt': 0,
                                                'last_seq_number': 7
                                            }
                                        }
                                    },
                                    'Ethernet1/1.390': {
                                        'eigrp_nbr': {
                                            '10.23.90.2': {
                                                'peer_handle': 0,
                                                'hold': 13,
                                                'uptime': '01:44:12',
                                                'srtt': 0.01,
                                                'rto': 60,
                                                'q_cnt': 0,
                                                'last_seq_number': 9, }}}}}}}}}}}

    device_output_1 = {'execute.return_value': '''
        # show ip eigrp neighbors vrf all
        IP-EIGRP neighbors for process 100 VRF default
        H   Address                 Interface       Hold  Uptime  SRTT   RTO  Q  Seq
                                                    (sec)         (ms)       Cnt Num
        1   10.13.90.1              Eth1/2.90       13   01:56:49  1    50    0   16
        0   10.23.90.2              Eth1/1.90       11   01:46:12  15   90    0   22

        IP-EIGRP neighbors for process 100 VRF VRF1
        H   Address                 Interface       Hold  Uptime  SRTT   RTO  Q  Seq
                                                    (sec)         (ms)       Cnt Num
        1   10.13.90.1              Eth1/2.390      13   01:43:23  1    50    0   7
        0   10.23.90.2              Eth1/1.390      13   01:44:12  10   60    0   9
    '''}

    expected_parsed_output_2 = {
        'eigrp_instance': {
            '100': {
                'vrf': {
                    'default': {
                        'address_family': {
                            'ipv6': {
                                'eigrp_interface': {
                                    'Ethernet1/1.90': {
                                        'eigrp_nbr': {
                                            'fe80::f816:3eff:fecf:5a5b': {
                                                'peer_handle': 0,
                                                'hold': 12,
                                                'uptime': '01:40:09',
                                                'srtt': 0.010,
                                                'rto': 60,
                                                'q_cnt': 0,
                                                'last_seq_number': 30}}},
                                    'Ethernet1/2.90': {
                                        'eigrp_nbr': {
                                            'fe80::f816:3eff:fe62:65af': {
                                                'peer_handle': 1,
                                                'hold': 12,
                                                'uptime': '01:40:07',
                                                'srtt': 0.004,
                                                'rto': 50,
                                                'q_cnt': 0,
                                                'last_seq_number': 22}}}}}}},
                    'VRF1': {
                        'address_family': {
                            'ipv6': {
                                'eigrp_interface': {
                                    'Ethernet1/1.390': {
                                        'eigrp_nbr': {
                                            'fe80::f816:3eff:fecf:5a5b': {
                                                'peer_handle': 0,
                                                'hold': 10,
                                                'uptime': '01:44:27',
                                                'srtt': 0.010,
                                                'rto': 60,
                                                'q_cnt': 0,
                                                'last_seq_number': 10
                                            }
                                        }
                                    },
                                    'Ethernet1/2.390': {
                                        'eigrp_nbr': {
                                            'fe80::f816:3eff:fe62:65af': {
                                                'peer_handle': 1,
                                                'hold': 13,
                                                'uptime': '01:43:38',
                                                'srtt': 0.004,
                                                'rto': 50,
                                                'q_cnt': 0,
                                                'last_seq_number': 8 }}}}}}}}}}}

    device_output_2 = {'execute.return_value': '''
        # show ipv6 eigrp neighbors vrf all
        IPv6-EIGRP neighbors for process 100 VRF default
        H   Address                                 Interface       Hold  Uptime  SRTT   RTO  Q  Seq
                                                                    (sec)         (ms)       Cnt Num
        0   fe80::f816:3eff:fecf:5a5b               Eth1/1.90       12   01:40:09  10   60    0   30
        1   fe80::f816:3eff:fe62:65af               Eth1/2.90       12   01:40:07  4    50    0   22
        IPv6-EIGRP neighbors for process 100 VRF VRF1
        H   Address                                 Interface       Hold  Uptime  SRTT   RTO  Q  Seq
                                                                    (sec)         (ms)       Cnt Num
        0   fe80::f816:3eff:fecf:5a5b               Eth1/1.390      10   01:44:27  10   60    0   10
        1   fe80::f816:3eff:fe62:65af               Eth1/2.390      13   01:43:38  4    50    0   8
    '''}

    device_output_empty = {'execute.return_value': ''}

    def test_show_eigrp_neighbors_1(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_1)
        obj = ShowIpv4EigrpNeighbors(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_1)

    def test_show_eigrp_neighbors_2(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_2)
        obj = ShowIpv6EigrpNeighbors(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_2)

    def test_show_eigrp_neighbors_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_empty)
        obj = ShowIpv4EigrpNeighbors(device=self.device)
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
                                'eigrp_interface': {
                                    'Ethernet1/2.90': {
                                        'eigrp_nbr': {
                                            '10.13.90.1': {
                                                'peer_handle': 1,
                                                'hold': 14,
                                                'uptime': '01:58:11',
                                                'srtt': 0.001,
                                                'rto': 50,
                                                'q_cnt': 0,
                                                'last_seq_number': 16,
                                                'nbr_sw_ver': {
                                                    'os_majorver': 23,
                                                    'os_minorver': 0,
                                                    'tlv_majorrev': 2,
                                                    'tlv_minorrev': 0
                                                },
                                                'retransmit_count': 1,
                                                'retry_count': 0,
                                                'bfd_state': 'N/A',
                                                'prefixes': 3, }, }, },
                                    'Ethernet1/1.90': {
                                        'eigrp_nbr': {
                                            '10.23.90.2': {
                                                'peer_handle': 0,
                                                'hold': 13,
                                                'uptime': '01:47:34',
                                                'srtt': 0.015,
                                                'rto': 90,
                                                'q_cnt': 0,
                                                'last_seq_number': 22,
                                                'nbr_sw_ver': {
                                                    'os_majorver': 3,
                                                    'os_minorver': 3,
                                                    'tlv_majorrev': 2,
                                                    'tlv_minorrev': 0
                                                },
                                                'retransmit_count': 1,
                                                'retry_count': 0,
                                                'bfd_state': 'N/A',
                                                'prefixes': 3}}}}}}},
                    'VRF1': {
                        'address_family': {
                            'ipv4': {
                                'eigrp_interface': {
                                    'Ethernet1/2.390': {
                                        'eigrp_nbr': {
                                            '10.13.90.1': {
                                                'peer_handle': 1,
                                                'hold': 14,
                                                'uptime': '01:44:45',
                                                'srtt': 0.001,
                                                'rto': 50,
                                                'q_cnt': 0,
                                                'last_seq_number': 7,
                                                'nbr_sw_ver': {
                                                    'os_majorver': 23,
                                                    'os_minorver': 0,
                                                    'tlv_majorrev': 2,
                                                    'tlv_minorrev': 0
                                                },
                                                'retransmit_count': 1,
                                                'retry_count': 0,
                                                'bfd_state': 'N/A',
                                                'prefixes': 3}, }, },
                                    'Ethernet1/1.390': {
                                        'eigrp_nbr': {
                                            '10.23.90.2': {
                                                'peer_handle': 0,
                                                'hold': 14,
                                                'uptime': '01:45:34',
                                                'srtt': 0.01,
                                                'rto': 60,
                                                'q_cnt': 0,
                                                'last_seq_number': 9,
                                                'nbr_sw_ver': {
                                                    'os_majorver': 3,
                                                    'os_minorver': 3,
                                                    'tlv_majorrev': 2,
                                                    'tlv_minorrev': 0
                                                },
                                                'retransmit_count': 1,
                                                'retry_count': 0,
                                                'bfd_state': 'N/A',
                                                'prefixes': 3}}}}}}}}}}}

    device_output_1 = {'execute.return_value': '''
        # show ip eigrp neighbors detail vrf all
        IP-EIGRP neighbors for process 100 VRF default
        H   Address                 Interface       Hold  Uptime  SRTT   RTO  Q  Seq
                                                    (sec)         (ms)       Cnt Num
        1   10.13.90.1              Eth1/2.90       14   01:58:11  1    50    0   16
           Version 23.0/2.0, Retrans: 1, Retries: 0, BFD state: N/A, Prefixes: 3
        0   10.23.90.2              Eth1/1.90       13   01:47:34  15   90    0   22
           Version 3.3/2.0, Retrans: 1, Retries: 0, BFD state: N/A, Prefixes: 3

        IP-EIGRP neighbors for process 100 VRF VRF1
        H   Address                 Interface       Hold  Uptime  SRTT   RTO  Q  Seq
                                                    (sec)         (ms)       Cnt Num
        1   10.13.90.1              Eth1/2.390      14   01:44:45  1    50    0   7
           Version 23.0/2.0, Retrans: 1, Retries: 0, BFD state: N/A, Prefixes: 3
        0   10.23.90.2              Eth1/1.390      14   01:45:34  10   60    0   9
           Version 3.3/2.0, Retrans: 1, Retries: 0, BFD state: N/A, Prefixes: 3
    '''}

    expected_parsed_output_2 = {
        'eigrp_instance': {
            '100': {
                'vrf': {
                    'default': {
                        'address_family': {
                            'ipv6': {
                                'eigrp_interface': {
                                    'Ethernet1/1.90': {
                                        'eigrp_nbr': {
                                            'fe80::f816:3eff:fecf:5a5b': {
                                                'peer_handle': 0,
                                                'hold': 12,
                                                'uptime': '01:41:31',
                                                'srtt': 0.010,
                                                'rto': 60,
                                                'q_cnt': 0,
                                                'last_seq_number': 30,
                                                'nbr_sw_ver': {
                                                    'os_majorver': 3,
                                                    'os_minorver': 3,
                                                    'tlv_majorrev': 2,
                                                    'tlv_minorrev': 0
                                                },
                                                'retransmit_count': 1,
                                                'retry_count': 0,
                                                'bfd_state': 'N/A',
                                                'prefixes': 0
                                            }
                                        }
                                    },
                                    'Ethernet1/2.90': {
                                        'eigrp_nbr': {
                                            'fe80::f816:3eff:fe62:65af': {
                                                'peer_handle': 1,
                                                'hold': 12,
                                                'uptime': '01:41:30',
                                                'srtt': 0.004,
                                                'rto': 50,
                                                'q_cnt': 0,
                                                'last_seq_number': 22,
                                                'nbr_sw_ver': {
                                                    'os_majorver': 23,
                                                    'os_minorver': 0,
                                                    'tlv_majorrev': 2,
                                                    'tlv_minorrev': 0
                                                },
                                                'retransmit_count': 0,
                                                'retry_count': 0,
                                                'bfd_state': 'N/A',
                                                'prefixes': 0}}}}}}},
                    'VRF1': {
                        'address_family': {
                            'ipv6': {
                                'eigrp_interface': {
                                    'Ethernet1/1.390': {
                                        'eigrp_nbr': {
                                            'fe80::f816:3eff:fecf:5a5b': {
                                                'peer_handle': 0,
                                                'hold': 11,
                                                'uptime': '01:45:50',
                                                'srtt': 0.010,
                                                'rto': 60,
                                                'q_cnt': 0,
                                                'last_seq_number': 10,
                                                'nbr_sw_ver': {
                                                    'os_majorver': 3,
                                                    'os_minorver': 3,
                                                    'tlv_majorrev': 2,
                                                    'tlv_minorrev': 0
                                                },
                                                'retransmit_count': 2,
                                                'retry_count': 0,
                                                'bfd_state': 'N/A',
                                                'prefixes': 0
                                            }
                                        }
                                    },
                                    'Ethernet1/2.390': {
                                        'eigrp_nbr': {
                                            'fe80::f816:3eff:fe62:65af': {
                                                'peer_handle': 1,
                                                'hold': 14,
                                                'uptime': '01:45:01',
                                                'srtt': 0.004,
                                                'rto': 50,
                                                'q_cnt': 0,
                                                'last_seq_number': 8,
                                                'nbr_sw_ver': {
                                                    'os_majorver': 23,
                                                    'os_minorver': 0,
                                                    'tlv_majorrev': 2,
                                                    'tlv_minorrev': 0
                                                },
                                                'retransmit_count': 1,
                                                'retry_count': 0,
                                                'bfd_state': 'N/A',
                                                'prefixes': 0}}}}}}}}}}}

    device_output_2 = {'execute.return_value': '''
        # show ipv6 eigrp neighbors detail vrf all
        IPv6-EIGRP neighbors for process 100 VRF default
        H   Address                                 Interface       Hold  Uptime  SRTT   RTO  Q  Seq
                                                                    (sec)         (ms)       Cnt Num
        0   fe80::f816:3eff:fecf:5a5b               Eth1/1.90       12   01:41:31  10   60    0   30
           Version 3.3/2.0, Retrans: 1, Retries: 0, BFD state: N/A
        1   fe80::f816:3eff:fe62:65af               Eth1/2.90       12   01:41:30  4    50    0   22
           Version 23.0/2.0, Retrans: 0, Retries: 0, BFD state: N/A
        IPv6-EIGRP neighbors for process 100 VRF VRF1
        H   Address                                 Interface       Hold  Uptime  SRTT   RTO  Q  Seq
                                                                    (sec)         (ms)       Cnt Num
        0   fe80::f816:3eff:fecf:5a5b               Eth1/1.390      11   01:45:50  10   60    0   10
           Version 3.3/2.0, Retrans: 2, Retries: 0, BFD state: N/A
        1   fe80::f816:3eff:fe62:65af               Eth1/2.390      14   01:45:01  4    50    0   8
           Version 23.0/2.0, Retrans: 1, Retries: 0, BFD state: N/A
    '''}

    device_output_empty = {'execute.return_value': ''}

    def test_show_eigrp_neighbors_detail_1(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_1)
        obj = ShowIpv4EigrpNeighborsDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_1)

    def test_show_eigrp_neighbors_detail_2(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_2)
        obj = ShowIpv6EigrpNeighborsDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_2)

    def test_show_eigrp_neighbors_detail_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_empty)
        obj = ShowIpv4EigrpNeighborsDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


if __name__ == '__main__':
    unittest.main()
