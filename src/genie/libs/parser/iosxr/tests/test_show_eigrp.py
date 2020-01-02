# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# iosxr show ip eigrp
from genie.libs.parser.iosxr.show_eigrp import ShowEigrpIpv4Neighbors,\
                                               ShowEigrpIpv6Neighbors,\
                                               ShowEigrpIpv4NeighborsDetail,\
                                               ShowEigrpIpv6NeighborsDetail


class test_show_eigrp_neighbors(unittest.TestCase):
    device = Device(name='aDevice')

    expected_parsed_output_1 = {
        'eigrp_instance': {
            '100': {
                'vrf': {
                    'default': {
                        'address_family': {
                            'ipv4': {
                                'name': 'test',
                                'named_mode': True,
                                'eigrp_interface': {
                                    'GigabitEthernet0/0/0/1.90': {
                                        'eigrp_nbr': {
                                            '10.23.90.3': {
                                                'peer_handle': 1,
                                                'hold': 13,
                                                'uptime': '01:41:56',
                                                'srtt': 0.013,
                                                'rto': 200,
                                                'q_cnt': 0,
                                                'last_seq_number': 23
                                            }
                                        }
                                    },
                                    'GigabitEthernet0/0/0/0.90': {
                                        'eigrp_nbr': {
                                            '10.12.90.1': {
                                                'peer_handle': 0,
                                                'hold': 14,
                                                'uptime': '02:55:10',
                                                'srtt': 0.001,
                                                'rto': 200,
                                                'q_cnt': 0,
                                                'last_seq_number': 17
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    device_output_1 = {'execute.return_value': '''
        # show eigrp ipv4 neighbors
        Mon Apr 15 18:02:40.121 UTC
        IPv4-EIGRP VR(test) Neighbors for AS(100) VRF default

        H   Address                 Interface       Hold Uptime   SRTT   RTO  Q  Seq
                                                    (sec)         (ms)       Cnt Num
        1   10.23.90.3              Gi0/0/0/1.90      13 01:41:56   13   200  0  23
        0   10.12.90.1              Gi0/0/0/0.90      14 02:55:10    1   200  0  17
    '''}

    expected_parsed_output_2 = {
        'eigrp_instance': {
            '100': {
                'vrf': {
                    'VRF1': {
                        'address_family': {
                            'ipv4': {
                                'name': 'test',
                                'named_mode': True,
                                'eigrp_interface': {
                                    'GigabitEthernet0/0/0/1.390': {
                                        'eigrp_nbr': {
                                            '10.23.90.3': {
                                                'peer_handle': 1,
                                                'hold': 12,
                                                'uptime': '01:40:17',
                                                'srtt': 0.004,
                                                'rto': 200,
                                                'q_cnt': 0,
                                                'last_seq_number': 15
                                            }
                                        }
                                    },
                                    'GigabitEthernet0/0/0/0.390': {
                                        'eigrp_nbr': {
                                            '10.12.90.1': {
                                                'peer_handle': 0,
                                                'hold': 12,
                                                'uptime': '02:52:31',
                                                'srtt': 0.816,
                                                'rto': 4896,
                                                'q_cnt': 0,
                                                'last_seq_number': 8
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    device_output_2 = {'execute.return_value': '''
        # show eigrp ipv4 vrf all neighbors
        Mon Apr 15 18:03:01.027 UTC

        IPv4-EIGRP VR(test) Neighbors for AS(100) VRF VRF1

        H   Address                 Interface       Hold Uptime   SRTT   RTO  Q  Seq
                                            (sec)         (ms)       Cnt Num
        1   10.23.90.3              Gi0/0/0/1.390     12 01:40:17    4   200  0  15
        0   10.12.90.1              Gi0/0/0/0.390     12 02:52:31  816  4896  0  8

    '''}

    expected_parsed_output_3 = {
        'eigrp_instance': {
            '100': {
                'vrf': {
                    'default': {
                        'address_family': {
                            'ipv6': {
                                'name': 'test',
                                'named_mode': True,
                                'eigrp_interface': {
                                    'GigabitEthernet0/0/0/1.90': {
                                        'eigrp_nbr': {
                                            'fe80::5c00:ff:fe02:7': {
                                                'peer_handle': 1,
                                                'hold': 12,
                                                'uptime': '01:36:14',
                                                'srtt': 0.011,
                                                'rto': 200,
                                                'q_cnt': 0,
                                                'last_seq_number': 28
                                            }
                                        }
                                    },
                                    'GigabitEthernet0/0/0/0.90': {
                                        'eigrp_nbr': {
                                            'fe80::f816:3eff:feb4:b131': {
                                                'peer_handle': 0,
                                                'hold': 11,
                                                'uptime': '02:30:16',
                                                'srtt': 0.001,
                                                'rto': 200,
                                                'q_cnt': 0,
                                                'last_seq_number': 23
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    device_output_3 = {'execute.return_value': '''
        # show eigrp ipv6 neighbors
        Mon Apr 15 18:03:17.730 UTC

        IPv6-EIGRP VR(test) Neighbors for AS(100) VRF default

        H   Address                 Interface       Hold Uptime   SRTT   RTO  Q  Seq
                                                    (sec)         (ms)       Cnt Num
        1   Link Local Address:     Gi0/0/0/1.90      12 01:36:14   11   200  0  28
            fe80::5c00:ff:fe02:7
        0   Link Local Address:     Gi0/0/0/0.90      11 02:30:16    1   200  0  23
            fe80::f816:3eff:feb4:b131
    '''}

    expected_parsed_output_4 = {
        'eigrp_instance': {
            '100': {
                'vrf': {
                    'VRF1': {
                        'address_family': {
                            'ipv6': {
                                'name': 'test',
                                'named_mode': True,
                                'eigrp_interface': {
                                    'GigabitEthernet0/0/0/1.390': {
                                        'eigrp_nbr': {
                                            'fe80::5c00:ff:fe02:': {
                                                'peer_handle': 1,
                                                'hold': 12,
                                                'uptime': '01:40:51',
                                                'srtt': 0.009,
                                                'rto': 200,
                                                'q_cnt': 0,
                                                'last_seq_number': 14
                                            }
                                        }
                                    },
                                    'GigabitEthernet0/0/0/0.390': {
                                        'eigrp_nbr': {
                                            'fe80::f816:3eff:feb4:b131': {
                                                'peer_handle': 0,
                                                'hold': 12,
                                                'uptime': '02:29:54',
                                                'srtt': 0.004,
                                                'rto': 200,
                                                'q_cnt': 0,
                                                'last_seq_number': 9
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    device_output_4 = {'execute.return_value': '''
        # show eigrp ipv6 vrf all neighbors
        Mon Apr 15 18:03:36.307 UTC

        IPv6-EIGRP VR(test) Neighbors for AS(100) VRF VRF1

        H   Address                 Interface       Hold Uptime   SRTT   RTO  Q  Seq
                                                    (sec)         (ms)       Cnt Num
        1   Link Local Address:     Gi0/0/0/1.390     12 01:40:51    9   200  0  14
            fe80::5c00:ff:fe02:
        0   Link Local Address:     Gi0/0/0/0.390     12 02:29:54    4   200  0  9
            fe80::f816:3eff:feb4:b131
    '''}

    device_output_empty = {'execute.return_value': ''}

    def test_show_eigrp_neighbors_1(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_1)
        obj = ShowEigrpIpv4Neighbors(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_1)

    def test_show_eigrp_neighbors_2(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_2)
        obj = ShowEigrpIpv4Neighbors(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_2)

    def test_show_eigrp_neighbors_3(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_3)
        obj = ShowEigrpIpv6Neighbors(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_3)

    def test_show_eigrp_neighbors_4(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_4)
        obj = ShowEigrpIpv6Neighbors(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_4)

    def test_show_eigrp_neighbors_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_empty)
        obj = ShowEigrpIpv4Neighbors(device=self.device)
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
                                'name': 'test',
                                'named_mode': True,
                                'eigrp_interface': {
                                    'GigabitEthernet0/0/0/1.90': {
                                        'eigrp_nbr': {
                                            '10.23.90.3': {
                                                'peer_handle': 1,
                                                'hold': 11,
                                                'uptime': '01:43:15',
                                                'srtt': 0.013,
                                                'rto': 200,
                                                'q_cnt': 0,
                                                'last_seq_number': 23,
                                                'nbr_sw_ver': {
                                                    'os_majorver': 8,
                                                    'os_minorver': 0,
                                                    'tlv_majorrev': 1,
                                                    'tlv_minorrev': 2
                                                },
                                                'retransmit_count': 1,
                                                'retry_count': 0,
                                                'bfd': 'disabled',
                                                'prefixes': 3
                                            }
                                        }
                                    },
                                    'GigabitEthernet0/0/0/0.90': {
                                        'eigrp_nbr': {
                                            '10.12.90.1': {
                                                'peer_handle': 0,
                                                'hold': 14,
                                                'uptime': '02:56:28',
                                                'srtt': 0.001,
                                                'rto': 200,
                                                'q_cnt': 0,
                                                'last_seq_number': 17,
                                                'nbr_sw_ver': {
                                                    'os_majorver': 23,
                                                    'os_minorver': 0,
                                                    'tlv_majorrev': 2,
                                                    'tlv_minorrev': 0
                                                },
                                                'retransmit_count': 1,
                                                'retry_count': 0,
                                                'bfd': 'disabled',
                                                'prefixes': 3
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    device_output_1 = {'execute.return_value': '''
        #show eigrp ipv4 neighbors detail
        Mon Apr 15 18:03:58.323 UTC

        IPv4-EIGRP VR(test) Neighbors for AS(100) VRF default

        H   Address                 Interface       Hold Uptime   SRTT   RTO  Q  Seq
                                            (sec)         (ms)       Cnt Num
        1   10.23.90.3              Gi0/0/0/1.90      11 01:43:15   13   200  0  23
        BFD disabled
        Version 8.0/1.2, Retrans: 1, Retries: 0, Prefixes: 3
        0   10.12.90.1              Gi0/0/0/0.90      14 02:56:28    1   200  0  17
        BFD disabled
        Version 23.0/2.0, Retrans: 1, Retries: 0, Prefixes: 3
    '''}

    expected_parsed_output_2 = {
        'eigrp_instance': {
            '100': {
                'vrf': {
                    'VRF1': {
                        'address_family': {
                            'ipv4': {
                                'name': 'test',
                                'named_mode': True,
                                'eigrp_interface': {
                                    'GigabitEthernet0/0/0/1.390': {
                                        'eigrp_nbr': {
                                            '10.23.90.3': {
                                                'peer_handle': 1,
                                                'hold': 14,
                                                'uptime': '01:41:47',
                                                'srtt': 0.004,
                                                'rto': 200,
                                                'q_cnt': 0,
                                                'last_seq_number': 15,
                                                'nbr_sw_ver': {
                                                    'os_majorver': 8,
                                                    'os_minorver': 0,
                                                    'tlv_majorrev': 1,
                                                    'tlv_minorrev': 2
                                                },
                                                'retransmit_count': 1,
                                                'retry_count': 0,
                                                'bfd': 'disabled',
                                                'prefixes': 3
                                            }
                                        }
                                    },
                                    'GigabitEthernet0/0/0/0.390': {
                                        'eigrp_nbr': {
                                            '10.12.90.1': {
                                                'peer_handle': 0,
                                                'hold': 13,
                                                'uptime': '02:54:01',
                                                'srtt': 0.816,
                                                'rto': 4896,
                                                'q_cnt': 0,
                                                'last_seq_number': 8,
                                                'nbr_sw_ver': {
                                                    'os_majorver': 23,
                                                    'os_minorver': 0,
                                                    'tlv_majorrev': 2,
                                                    'tlv_minorrev': 0
                                                },
                                                'retransmit_count': 0,
                                                'retry_count': 0,
                                                'bfd': 'disabled',
                                                'prefixes': 3
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    device_output_2 = {'execute.return_value': '''
        #show eigrp ipv4 vrf all neighbors detail
        Mon Apr 15 18:04:31.216 UTC

        IPv4-EIGRP VR(test) Neighbors for AS(100) VRF VRF1

        H   Address                 Interface       Hold Uptime   SRTT   RTO  Q  Seq
                                                    (sec)         (ms)       Cnt Num
        1   10.23.90.3              Gi0/0/0/1.390     14 01:41:47    4   200  0  15
           BFD disabled
           Version 8.0/1.2, Retrans: 1, Retries: 0, Prefixes: 3
        0   10.12.90.1              Gi0/0/0/0.390     13 02:54:01  816  4896  0  8
           BFD disabled
           Version 23.0/2.0, Retrans: 0, Retries: 0, Prefixes: 3
    '''}

    expected_parsed_output_3 = {
        'eigrp_instance': {
            '100': {
                'vrf': {
                    'default': {
                        'address_family': {
                            'ipv6': {
                                'name': 'test',
                                'named_mode': True,
                                'eigrp_interface': {
                                    'GigabitEthernet0/0/0/1.90': {
                                        'eigrp_nbr': {
                                            'fe80::5c00:ff:fe02:7': {
                                                'peer_handle': 1,
                                                'hold': 13,
                                                'uptime': '01:37:57',
                                                'srtt': 0.011,
                                                'rto': 200,
                                                'q_cnt': 0,
                                                'last_seq_number': 28,
                                                'nbr_sw_ver': {
                                                    'os_majorver': 8,
                                                    'os_minorver': 0,
                                                    'tlv_majorrev': 1,
                                                    'tlv_minorrev': 2
                                                },
                                                'retransmit_count': 1,
                                                'retry_count': 0,
                                                'bfd': 'disabled',
                                                'prefixes': 5
                                            }
                                        }
                                    },
                                    'GigabitEthernet0/0/0/0.90': {
                                        'eigrp_nbr': {
                                            'fe80::f816:3eff:feb4:b131': {
                                                'peer_handle': 0,
                                                'hold': 12,
                                                'uptime': '02:31:58',
                                                'srtt': 0.001,
                                                'rto': 200,
                                                'q_cnt': 0,
                                                'last_seq_number': 23,
                                                'nbr_sw_ver': {
                                                    'os_majorver': 23,
                                                    'os_minorver': 0,
                                                    'tlv_majorrev': 2,
                                                    'tlv_minorrev': 0
                                                },
                                                'retransmit_count': 1,
                                                'retry_count': 0,
                                                'bfd': 'disabled',
                                                'prefixes': 6
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    device_output_3 = {'execute.return_value': '''
        #show eigrp ipv6 neighbors detail
        Mon Apr 15 18:05:00.348 UTC

        IPv6-EIGRP VR(test) Neighbors for AS(100) VRF default

        H   Address                 Interface       Hold Uptime   SRTT   RTO  Q  Seq
                                                    (sec)         (ms)       Cnt Num
        1   Link Local Address:     Gi0/0/0/1.90      13 01:37:57   11   200  0  28
            fe80::5c00:ff:fe02:7
           BFD disabled
           Version 8.0/1.2, Retrans: 1, Retries: 0, Prefixes: 5
        0   Link Local Address:     Gi0/0/0/0.90      12 02:31:58    1   200  0  23
            fe80::f816:3eff:feb4:b131
           BFD disabled
           Version 23.0/2.0, Retrans: 1, Retries: 0, Prefixes: 6
    '''}

    expected_parsed_output_4 = {
        'eigrp_instance': {
            '100': {
                'vrf': {
                    'VRF1': {
                        'address_family': {
                            'ipv6': {
                                'name': 'test',
                                'named_mode': True,
                                'eigrp_interface': {
                                    'GigabitEthernet0/0/0/1.390': {
                                        'eigrp_nbr': {
                                            'fe80::5c00:ff:fe02:7': {
                                                'peer_handle': 1,
                                                'hold': 11,
                                                'uptime': '01:42:44',
                                                'srtt': 0.009,
                                                'rto': 200,
                                                'q_cnt': 0,
                                                'last_seq_number': 14,
                                                'nbr_sw_ver': {
                                                    'os_majorver': 8,
                                                    'os_minorver': 0,
                                                    'tlv_majorrev': 1,
                                                    'tlv_minorrev': 2
                                                },
                                                'retransmit_count': 1,
                                                'retry_count': 0,
                                                'bfd': 'disabled',
                                                'prefixes': 5
                                            }
                                        }
                                    },
                                    'GigabitEthernet0/0/0/0.390': {
                                        'eigrp_nbr': {
                                            'fe80::f816:3eff:feb4:b131': {
                                                'peer_handle': 0,
                                                'hold': 12,
                                                'uptime': '02:31:47',
                                                'srtt': 0.004,
                                                'rto': 200,
                                                'q_cnt': 0,
                                                'last_seq_number': 9,
                                                'nbr_sw_ver': {
                                                    'os_majorver': 23,
                                                    'os_minorver': 0,
                                                    'tlv_majorrev': 2,
                                                    'tlv_minorrev': 0
                                                },
                                                'retransmit_count': 1,
                                                'retry_count': 0,
                                                'bfd': 'disabled',
                                                'prefixes': 6
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    device_output_4 = {'execute.return_value': '''
        #show eigrp ipv6 vrf all neighbors detail
        Mon Apr 15 18:05:29.245 UTC

        IPv6-EIGRP VR(test) Neighbors for AS(100) VRF VRF1

        H   Address                 Interface       Hold Uptime   SRTT   RTO  Q  Seq
                                                    (sec)         (ms)       Cnt Num
        1   Link Local Address:     Gi0/0/0/1.390     11 01:42:44    9   200  0  14
            fe80::5c00:ff:fe02:7
           BFD disabled
           Version 8.0/1.2, Retrans: 1, Retries: 0, Prefixes: 5
        0   Link Local Address:     Gi0/0/0/0.390     12 02:31:47    4   200  0  9
            fe80::f816:3eff:feb4:b131
           BFD disabled
           Version 23.0/2.0, Retrans: 1, Retries: 0, Prefixes: 6
    '''}

    device_output_empty = {'execute.return_value': ''}

    def test_show_eigrp_neighbors_detail_1(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_1)
        obj = ShowEigrpIpv4NeighborsDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_1)

    def test_show_eigrp_neighbors_detail_2(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_2)
        obj = ShowEigrpIpv4NeighborsDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_2)

    def test_show_eigrp_neighbors_detail_3(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_3)
        obj = ShowEigrpIpv6NeighborsDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_3)

    def test_show_eigrp_neighbors_detail_4(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_4)
        obj = ShowEigrpIpv6NeighborsDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.expected_parsed_output_4)

    def test_show_eigrp_neighbors_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_empty)
        obj = ShowEigrpIpv4NeighborsDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


if __name__ == '__main__':
    unittest.main()
