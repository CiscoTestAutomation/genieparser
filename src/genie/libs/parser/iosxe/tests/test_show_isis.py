#!/bin/env python
import unittest
from unittest.mock import Mock
from pyats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                             SchemaMissingKeyError

from genie.libs.parser.iosxe.show_isis import ShowIsisHostname,\
                                              ShowIsisLspLog,\
                                              ShowIsisDatabaseDetail,\
                                              ShowRunSectionIsis,\
                                              ShowIsisNeighbors


class TestShowIsisHostname(unittest.TestCase):
    maxDiff = None
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'tag':{
            'VRF1':{
                'hostname_db': {
                    'hostname': {
                        '7777.77ff.eeee': {
                            'hostname': 'R7',
                            'level': 2,
                        },
                        '2222.22ff.4444':{
                            'hostname': 'R2',
                            'local_router': True,
                        }
                    }
                }
            },
            'test':{
                'hostname_db': {
                    'hostname': {
                        '9999.99ff.3333': {
                            'hostname': 'R9',
                            'level': 2,
                        },

                        '8888.88ff.1111': {
                            'hostname': 'R8',
                            'level': 2,
                        },
                        '7777.77ff.eeee': {
                            'hostname': 'R7',
                            'level': 2,
                        },
                        '5555.55ff.aaaa': {
                            'hostname': 'R5',
                            'level': 2,
                        },
                        '3333.33ff.6666': {
                            'hostname': 'R3',
                            'level': 2,
                        },
                        '1111.11ff.2222': {
                            'hostname': 'R1',
                            'level': 1,
                        },
                        '2222.22ff.4444': {
                            'hostname': 'R2',
                            'local_router': True,
                        },
                    },
                },
            }
        }
    }

    golden_output = {'execute.return_value': '''\
    R2#show isis hostname
    Level  System ID      Dynamic Hostname  (VRF1)
     2     7777.77ff.eeee R7
         * 2222.22ff.4444 R2
    Level  System ID      Dynamic Hostname  (test)
     2     9999.99ff.3333 R9
     2     8888.88ff.1111 R8
     2     7777.77ff.eeee R7
     2     5555.55ff.aaaa R5
     2     3333.33ff.6666 R3
     1     1111.11ff.2222 R1
         * 2222.22ff.4444 R2
           '''
    }

    golden_parsed_output_2 = {
        'tag': {
            'default': {}
        }
    }

    # No hostnames at all
    golden_output_2 = {'execute.return_value': '''
        #show isis hostname        
        Level  System ID      Dynamic Hostname  (default)
    '''}


    def test_empty(self):
        device = Mock(**self.empty_output)
        obj = ShowIsisHostname(device=device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_1(self):        
        device = Mock(**self.golden_output)
        obj = ShowIsisHostname(device=device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_2(self):       
        device = Mock(**self.golden_output_2)
        obj = ShowIsisHostname(device=device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_2)


class TestShowIsisLspLog(unittest.TestCase):
    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        "tag": {
            "VRF1": {
                "lsp_log": {
                    "level": {
                        1: {
                            "index": {
                                1: {
                                    "when": "01:13:52",
                                    "count": 5,
                                    "triggers": "CONFIG OTVINFOCHG"
                                },
                                2: {
                                    "when": "00:25:46",
                                    "count": 1,
                                    "triggers": "ATTACHFLAG"
                                },
                                3: {
                                    "when": "00:25:44",
                                    "count": 2,
                                    "triggers": "ATTACHFLAG IPV6IA"
                                }
                            }
                        },
                        2: {
                            "index": {
                                1: {
                                    "when": "01:13:52",
                                    "count": 5,
                                    "triggers": "CONFIG OTVINFOCHG"
                                },
                                2: {
                                    "when": "00:25:46",
                                    "count": 2,
                                    "triggers": "NEWADJ DIS",
                                    "interface": "GigabitEthernet4"
                                },
                                3: {
                                    "when": "00:25:45",
                                    "count": 1,
                                    "triggers": "ADJMTIDCHG",
                                    "interface": "GigabitEthernet4"
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    golden_output = {'execute.return_value': '''\
    R2#show isis lsp-log
    Tag VRF1:

       Level 1 LSP log
      When       Count             Interface         Triggers
    01:13:52        5                            CONFIG OTVINFOCHG
    00:25:46        1                            ATTACHFLAG
    00:25:44        2                            ATTACHFLAG IPV6IA

       Level 2 LSP log
      When       Count             Interface         Triggers
    01:13:52        5                            CONFIG OTVINFOCHG
    00:25:46        2         GigabitEthernet4   NEWADJ DIS
    00:25:45        1         GigabitEthernet4   ADJMTIDCHG

           '''
                     }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIsisLspLog(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowIsisLspLog(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


class TestShowIsisDatabaseDetail(unittest.TestCase):
    maxDiff = None
    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'tag': {
            'VRF1': {
                'level': {
                    1: {
                        'R2.00-00': {
                            'local_router': True,
                            'lsp_sequence_num': '0x00000007',
                            'lsp_checksum': '0x8A6D',
                            'lsp_holdtime': '403',
                            'lsp_rcvd': '*',
                            'attach_bit': 1,
                            'p_bit': 0,
                            'overload_bit': 0,
                            'area_address': '49.0001',
                            'nlpid': '0xCC 0x8E',
                            'topology': {
                                'ipv4': {
                                    'code': '0x0',
                                },
                                'ipv6': {
                                    'code': '0x4002 ATT',
                                },
                            },
                            'hostname': 'R2',
                            'ip_address': '10.84.66.66',
                            'ipv4_internal_reachability': {
                                '10.229.7.0/24': {
                                    'ip_prefix': '10.229.7.0',
                                    'prefix_len': '24',
                                    'metric': 10,
                                },
                                '10.84.66.66/32': {
                                    'ip_prefix': '10.84.66.66',
                                    'prefix_len': '32',
                                    'metric': 10,
                                },
                            },
                            'ipv6_address': '2001:DB8:66:66:66::66',
                            'mt_ipv6_reachability': {
                                '2001:DB8:20:2::/64': {
                                    'ip_prefix': '2001:DB8:20:2::',
                                    'prefix_len': '64',
                                    'metric': 10,
                                },
                                '2001:DB8:66:66:66::66/128': {
                                    'ip_prefix': '2001:DB8:66:66:66::66',
                                    'prefix_len': '128',
                                    'metric': 10,
                                },
                            },
                        },
                    },
                    2: {
                        'R2.00-00': {
                            'local_router': True,
                            'lsp_sequence_num': '0x00000008',
                            'lsp_checksum': '0x621E',
                            'lsp_holdtime': '1158',
                            'lsp_rcvd': '*',
                            'attach_bit': 0,
                            'p_bit': 0,
                            'overload_bit': 0,
                            'area_address': '49.0001',
                            'nlpid': '0xCC 0x8E',
                            'topology': {
                                'ipv4': {
                                    'code': '0x0',
                                },
                                'ipv6': {
                                    'code': '0x2',
                                },
                            },
                            'hostname': 'R2',
                            'extended_is_neighbor': {
                                'R2.01': {
                                    'neighbor_id': 'R2.01',
                                    'metric': 10,
                                },
                            },
                            'mt_is_neighbor': {
                                'R2.01': {
                                    'neighbor_id': 'R2.01',
                                    'metric': 10,
                                },
                            },
                            'ip_address': '10.84.66.66',
                            'ipv4_internal_reachability': {
                                '10.229.7.0/24': {
                                    'ip_prefix': '10.229.7.0',
                                    'prefix_len': '24',
                                    'metric': 10,
                                },
                                '10.84.66.66/32': {
                                    'ip_prefix': '10.84.66.66',
                                    'prefix_len': '32',
                                    'metric': 10,
                                },
                            },
                            'ipv6_address': '2001:DB8:66:66:66::66',
                            'mt_ipv6_reachability': {
                                '2001:DB8:20:2::/64': {
                                    'ip_prefix': '2001:DB8:20:2::',
                                    'prefix_len': '64',
                                    'metric': 10,
                                },
                                '2001:DB8:66:66:66::66/128': {
                                    'ip_prefix': '2001:DB8:66:66:66::66',
                                    'prefix_len': '128',
                                    'metric': 10,
                                },
                            },
                        },
                        'R2.01-00': {
                            'local_router': True,
                            'lsp_sequence_num': '0x00000002',
                            'lsp_checksum': '0x3334',
                            'lsp_holdtime': '414',
                            'lsp_rcvd': '*',
                            'attach_bit': 0,
                            'p_bit': 0,
                            'overload_bit': 0,
                            'extended_is_neighbor': {
                                'R2.00': {
                                    'neighbor_id': 'R2.00',
                                    'metric': 0,
                                },
                                'R7.00': {
                                    'neighbor_id': 'R7.00',
                                    'metric': 0,
                                },
                            },
                        },
                        'R7.00-00': {
                            'lsp_sequence_num': '0x00000005',
                            'lsp_checksum': '0x056E',
                            'lsp_holdtime': '735',
                            'lsp_rcvd': '1199',
                            'attach_bit': 0,
                            'p_bit': 0,
                            'overload_bit': 0,
                            'area_address': '49.0002',
                            'nlpid': '0xCC 0x8E',
                            'router_id': '10.1.77.77',
                            'ip_address': '10.1.77.77',
                            'topology': {
                                'ipv6': {
                                    'code': '0x2',
                                },
                                'ipv4': {
                                    'code': '0x0',
                                },
                            },
                            'hostname': 'R7',
                            'mt_is_neighbor': {
                                'R2.01': {
                                    'neighbor_id': 'R2.01',
                                    'metric': 40,
                                },
                            },
                            'extended_is_neighbor': {
                                'R2.01': {
                                    'neighbor_id': 'R2.01',
                                    'metric': 40,
                                },
                            },
                            'ipv4_internal_reachability': {
                                '10.1.77.77/32': {
                                    'ip_prefix': '10.1.77.77',
                                    'prefix_len': '32',
                                    'metric': 1,
                                },
                                '10.229.7.0/24': {
                                    'ip_prefix': '10.229.7.0',
                                    'prefix_len': '24',
                                    'metric': 40,
                                },
                            },
                            'mt_ipv6_reachability': {
                                '2001:DB8:77:77:77::77/128': {
                                    'ip_prefix': '2001:DB8:77:77:77::77',
                                    'prefix_len': '128',
                                    'metric': 1,
                                },
                                '2001:DB8:20:2::/64': {
                                    'ip_prefix': '2001:DB8:20:2::',
                                    'prefix_len': '64',
                                    'metric': 40,
                                },
                            },
                        },
                    },
                },
            },
        },
    }

    golden_output = {'execute.return_value': '''\
        R2#show isis database detail

        Tag VRF1:
        IS-IS Level-1 Link State Database:
        LSPID                 LSP Seq Num  LSP Checksum  LSP Holdtime/Rcvd      ATT/P/OL
        R2.00-00            * 0x00000007   0x8A6D                 403/*         1/0/0
        Area Address: 49.0001
        NLPID:        0xCC 0x8E
        Topology:     IPv4 (0x0)
                        IPv6 (0x4002 ATT)
        Hostname: R2
        IP Address:   10.84.66.66
        Metric: 10         IP 10.229.7.0/24
        Metric: 10         IP 10.84.66.66/32
        IPv6 Address: 2001:DB8:66:66:66::66
        Metric: 10         IPv6 (MT-IPv6) 2001:DB8:20:2::/64
        Metric: 10         IPv6 (MT-IPv6) 2001:DB8:66:66:66::66/128
        IS-IS Level-2 Link State Database:
        LSPID                 LSP Seq Num  LSP Checksum  LSP Holdtime/Rcvd      ATT/P/OL
        R2.00-00            * 0x00000008   0x621E                1158/*         0/0/0
        Area Address: 49.0001
        NLPID:        0xCC 0x8E
        Topology:     IPv4 (0x0)
                        IPv6 (0x2)
        Hostname: R2
        Metric: 10         IS-Extended R2.01
        Metric: 10         IS (MT-IPv6) R2.01
        IP Address:   10.84.66.66
        Metric: 10         IP 10.229.7.0/24
        Metric: 10         IP 10.84.66.66/32
        IPv6 Address: 2001:DB8:66:66:66::66
        Metric: 10         IPv6 (MT-IPv6) 2001:DB8:20:2::/64
        Metric: 10         IPv6 (MT-IPv6) 2001:DB8:66:66:66::66/128
        R2.01-00            * 0x00000002   0x3334                 414/*         0/0/0
        Metric: 0          IS-Extended R2.00
        Metric: 0          IS-Extended R7.00
        R7.00-00              0x00000005   0x056E                 735/1199      0/0/0
        Area Address: 49.0002
        NLPID:        0xCC 0x8E
        Router ID:    10.1.77.77
        IP Address:   10.1.77.77
        Topology:     IPv6 (0x2)
                        IPv4 (0x0)
        Hostname: R7
        Metric: 40         IS (MT-IPv6) R2.01
        Metric: 40         IS-Extended R2.01
        Metric: 1          IP 10.1.77.77/32
        Metric: 40         IP 10.229.7.0/24
        Metric: 1          IPv6 (MT-IPv6) 2001:DB8:77:77:77::77/128
        Metric: 40         IPv6 (MT-IPv6) 2001:DB8:20:2::/64
    '''}

    golden_parsed_output1 = {
        'tag': {
            'test': {
                'level': {
                    1: {
                        'R1_xe.00-00': {
                            'local_router': True,
                            'lsp_sequence_num': '0x0000011D',
                            'lsp_checksum': '0x2165',
                            'lsp_holdtime': '519',
                            'lsp_rcvd': '*',
                            'attach_bit': 0,
                            'p_bit': 0,
                            'overload_bit': 0,
                            'area_address': '49.0001',
                            'nlpid': '0xCC 0x8E',
                            'topology': {
                                'ipv4': {
                                    'code': '0x0',
                                },
                                'ipv6': {
                                    'code': '0x2',
                                },
                            },
                            'hostname': 'R1_xe',
                            'extended_is_neighbor': {
                                'R1_xe.02': {
                                    'neighbor_id': 'R1_xe.02',
                                    'metric': 10,
                                },
                                'R1_xe.01': {
                                    'neighbor_id': 'R1_xe.01',
                                    'metric': 10,
                                },
                            },
                            'mt_is_neighbor': {
                                'R1_xe.02': {
                                    'neighbor_id': 'R1_xe.02',
                                    'metric': 10,
                                },
                                'R1_xe.01': {
                                    'neighbor_id': 'R1_xe.01',
                                    'metric': 10,
                                },
                            },
                            'ip_address': '10.13.115.1',
                            'ipv4_internal_reachability': {
                                '10.12.115.0/24': {
                                    'ip_prefix': '10.12.115.0',
                                    'prefix_len': '24',
                                    'metric': 10,
                                },
                                '10.13.115.0/24': {
                                    'ip_prefix': '10.13.115.0',
                                    'prefix_len': '24',
                                    'metric': 10,
                                },
                            },
                            'ipv6_address': '2001:10:13:115::1',
                            'mt_ipv6_reachability': {
                                '2001:10:12:115::/64': {
                                    'ip_prefix': '2001:10:12:115::',
                                    'prefix_len': '64',
                                    'metric': 10,
                                },
                                '2001:10:13:115::/64': {
                                    'ip_prefix': '2001:10:13:115::',
                                    'prefix_len': '64',
                                    'metric': 10,
                                },
                            },
                        },
                        'R1_xe.01-00': {
                            'local_router': True,
                            'lsp_sequence_num': '0x00000118',
                            'lsp_checksum': '0x850F',
                            'lsp_holdtime': '1087',
                            'lsp_rcvd': '*',
                            'attach_bit': 0,
                            'p_bit': 0,
                            'overload_bit': 0,
                            'extended_is_neighbor': {
                                'R1_xe.00': {
                                    'neighbor_id': 'R1_xe.00',
                                    'metric': 0,
                                },
                                'R2_xr.00': {
                                    'neighbor_id': 'R2_xr.00',
                                    'metric': 0,
                                },
                            },
                        },
                        'R1_xe.02-00': {
                            'local_router': True,
                            'lsp_sequence_num': '0x00000118',
                            'lsp_checksum': '0x7EAE',
                            'lsp_holdtime': '752',
                            'lsp_rcvd': '*',
                            'attach_bit': 0,
                            'p_bit': 0,
                            'overload_bit': 0,
                            'extended_is_neighbor': {
                                'R1_xe.00': {
                                    'neighbor_id': 'R1_xe.00',
                                    'metric': 0,
                                },
                                'R3_nx.00': {
                                    'neighbor_id': 'R3_nx.00',
                                    'metric': 0,
                                },
                            },
                        },
                        'R2_xr.00-00': {
                            'lsp_sequence_num': '0x00000120',
                            'lsp_checksum': '0xC84E',
                            'lsp_holdtime': '754',
                            'lsp_rcvd': '1200',
                            'attach_bit': 0,
                            'p_bit': 0,
                            'overload_bit': 0,
                            'area_address': '49.0001',
                            'extended_is_neighbor': {
                                'R1_xe.01': {
                                    'neighbor_id': 'R1_xe.01',
                                    'metric': 10,
                                },
                                'R2_xr.03': {
                                    'neighbor_id': 'R2_xr.03',
                                    'metric': 10,
                                },
                            },
                            'nlpid': '0xCC 0x8E',
                            'ip_address': '10.16.2.2',
                            'ipv4_internal_reachability': {
                                '10.16.2.2/32': {
                                    'ip_prefix': '10.16.2.2',
                                    'prefix_len': '32',
                                    'metric': 10,
                                },
                                '10.12.115.0/24': {
                                    'ip_prefix': '10.12.115.0',
                                    'prefix_len': '24',
                                    'metric': 10,
                                },
                                '10.23.115.0/24': {
                                    'ip_prefix': '10.23.115.0',
                                    'prefix_len': '24',
                                    'metric': 10,
                                },
                            },
                            'hostname': 'R2_xr',
                            'mt_is_neighbor': {
                                'R1_xe.01': {
                                    'neighbor_id': 'R1_xe.01',
                                    'metric': 10,
                                },
                                'R2_xr.03': {
                                    'neighbor_id': 'R2_xr.03',
                                    'metric': 10,
                                },
                            },
                            'ipv6_address': '2001:2:2:2::2',
                            'mt_ipv6_reachability': {
                                '2001:2:2:2::2/128': {
                                    'ip_prefix': '2001:2:2:2::2',
                                    'prefix_len': '128',
                                    'metric': 10,
                                },
                                '2001:10:12:115::/64': {
                                    'ip_prefix': '2001:10:12:115::',
                                    'prefix_len': '64',
                                    'metric': 10,
                                },
                                '2001:10:23:115::/64': {
                                    'ip_prefix': '2001:10:23:115::',
                                    'prefix_len': '64',
                                    'metric': 10,
                                },
                            },
                            'topology': {
                                'ipv4': {
                                    'code': '0x0',
                                },
                                'ipv6': {
                                    'code': '0x2',
                                },
                            },
                        },
                        'R2_xr.03-00': {
                            'lsp_sequence_num': '0x00000118',
                            'lsp_checksum': '0xF5F1',
                            'lsp_holdtime': '563',
                            'lsp_rcvd': '1200',
                            'attach_bit': 0,
                            'p_bit': 0,
                            'overload_bit': 0,
                            'extended_is_neighbor': {
                                'R2_xr.00': {
                                    'neighbor_id': 'R2_xr.00',
                                    'metric': 0,
                                },
                                'R3_nx.00': {
                                    'neighbor_id': 'R3_nx.00',
                                    'metric': 0,
                                },
                            },
                        },
                        'R3_nx.00-00': {
                            'lsp_sequence_num': '0x00000193',
                            'lsp_checksum': '0x8022',
                            'lsp_holdtime': '1018',
                            'lsp_rcvd': '1200',
                            'attach_bit': 0,
                            'p_bit': 0,
                            'overload_bit': 0,
                            'area_address': '49.0001',
                            'nlpid': '0xCC 0x8E',
                            'router_id': '10.36.3.3',
                            'ip_address': '10.36.3.3',
                            'topology': {
                                'ipv6': {
                                    'code': '0x2',
                                },
                                'ipv4': {
                                    'code': '0x0',
                                },
                            },
                            'hostname': 'R3_nx',
                            'mt_is_neighbor': {
                                'R2_xr.03': {
                                    'neighbor_id': 'R2_xr.03',
                                    'metric': 40,
                                },
                                'R1_xe.02': {
                                    'neighbor_id': 'R1_xe.02',
                                    'metric': 40,
                                },
                            },
                            'extended_is_neighbor': {
                                'R2_xr.03': {
                                    'neighbor_id': 'R2_xr.03',
                                    'metric': 40,
                                },
                                'R1_xe.02': {
                                    'neighbor_id': 'R1_xe.02',
                                    'metric': 40,
                                },
                            },
                            'ipv4_internal_reachability': {
                                '10.36.3.3/32': {
                                    'ip_prefix': '10.36.3.3',
                                    'prefix_len': '32',
                                    'metric': 1,
                                },
                                '10.13.115.0/24': {
                                    'ip_prefix': '10.13.115.0',
                                    'prefix_len': '24',
                                    'metric': 40,
                                },
                                '10.23.115.0/24': {
                                    'ip_prefix': '10.23.115.0',
                                    'prefix_len': '24',
                                    'metric': 40,
                                },
                            },
                            'mt_ipv6_reachability': {
                                '2001:3:3:3::3/128': {
                                    'ip_prefix': '2001:3:3:3::3',
                                    'prefix_len': '128',
                                    'metric': 1,
                                },
                                '2001:10:13:115::/64': {
                                    'ip_prefix': '2001:10:13:115::',
                                    'prefix_len': '64',
                                    'metric': 40,
                                },
                                '2001:10:23:115::/64': {
                                    'ip_prefix': '2001:10:23:115::',
                                    'prefix_len': '64',
                                    'metric': 40,
                                },
                            },
                        },
                    },
                    2: {
                        'R1_xe.00-00': {
                            'local_router': True,
                            'lsp_sequence_num': '0x0000011D',
                            'lsp_checksum': '0x27D0',
                            'lsp_holdtime': '521',
                            'lsp_rcvd': '*',
                            'attach_bit': 0,
                            'p_bit': 0,
                            'overload_bit': 0,
                            'area_address': '49.0001',
                            'nlpid': '0xCC 0x8E',
                            'topology': {
                                'ipv4': {
                                    'code': '0x0',
                                },
                                'ipv6': {
                                    'code': '0x2',
                                },
                            },
                            'hostname': 'R1_xe',
                            'extended_is_neighbor': {
                                'R1_xe.02': {
                                    'neighbor_id': 'R1_xe.02',
                                    'metric': 10,
                                },
                                'R1_xe.01': {
                                    'neighbor_id': 'R1_xe.01',
                                    'metric': 10,
                                },
                            },
                            'mt_is_neighbor': {
                                'R1_xe.02': {
                                    'neighbor_id': 'R1_xe.02',
                                    'metric': 10,
                                },
                                'R1_xe.01': {
                                    'neighbor_id': 'R1_xe.01',
                                    'metric': 10,
                                },
                            },
                            'ip_address': '10.13.115.1',
                            'ipv4_internal_reachability': {
                                '10.12.115.0/24': {
                                    'ip_prefix': '10.12.115.0',
                                    'prefix_len': '24',
                                    'metric': 10,
                                },
                                '10.13.115.0/24': {
                                    'ip_prefix': '10.13.115.0',
                                    'prefix_len': '24',
                                    'metric': 10,
                                },
                                '10.23.115.0/24': {
                                    'ip_prefix': '10.23.115.0',
                                    'prefix_len': '24',
                                    'metric': 20,
                                },
                            },
                            'ipv6_address': '2001:10:13:115::1',
                            'mt_ipv6_reachability': {
                                '2001:10:12:115::/64': {
                                    'ip_prefix': '2001:10:12:115::',
                                    'prefix_len': '64',
                                    'metric': 10,
                                },
                                '2001:10:13:115::/64': {
                                    'ip_prefix': '2001:10:13:115::',
                                    'prefix_len': '64',
                                    'metric': 10,
                                },
                                '2001:10:23:115::/64': {
                                    'ip_prefix': '2001:10:23:115::',
                                    'prefix_len': '64',
                                    'metric': 20,
                                },
                            },
                        },
                        'R1_xe.01-00': {
                            'local_router': True,
                            'lsp_sequence_num': '0x00000118',
                            'lsp_checksum': '0x9D7F',
                            'lsp_holdtime': '930',
                            'lsp_rcvd': '*',
                            'attach_bit': 0,
                            'p_bit': 0,
                            'overload_bit': 0,
                            'extended_is_neighbor': {
                                'R1_xe.00': {
                                    'neighbor_id': 'R1_xe.00',
                                    'metric': 0,
                                },
                                'R2_xr.00': {
                                    'neighbor_id': 'R2_xr.00',
                                    'metric': 0,
                                },
                            },
                        },
                        'R1_xe.02-00': {
                            'local_router': True,
                            'lsp_sequence_num': '0x0000011E',
                            'lsp_checksum': '0x8A25',
                            'lsp_holdtime': '1098',
                            'lsp_rcvd': '*',
                            'attach_bit': 0,
                            'p_bit': 0,
                            'overload_bit': 0,
                            'extended_is_neighbor': {
                                'R1_xe.00': {
                                    'neighbor_id': 'R1_xe.00',
                                    'metric': 0,
                                },
                                'R3_nx.00': {
                                    'neighbor_id': 'R3_nx.00',
                                    'metric': 0,
                                },
                            },
                        },
                        'R2_xr.00-00': {
                            'lsp_sequence_num': '0x00000120',
                            'lsp_checksum': '0x1585',
                            'lsp_holdtime': '662',
                            'lsp_rcvd': '1200',
                            'attach_bit': 0,
                            'p_bit': 0,
                            'overload_bit': 0,
                            'area_address': '49.0001',
                            'extended_is_neighbor': {
                                'R1_xe.01': {
                                    'neighbor_id': 'R1_xe.01',
                                    'metric': 10,
                                },
                                'R2_xr.03': {
                                    'neighbor_id': 'R2_xr.03',
                                    'metric': 10,
                                },
                            },
                            'nlpid': '0xCC 0x8E',
                            'ip_address': '10.16.2.2',
                            'ipv4_internal_reachability': {
                                '10.16.2.2/32': {
                                    'ip_prefix': '10.16.2.2',
                                    'prefix_len': '32',
                                    'metric': 10,
                                },
                                '10.12.115.0/24': {
                                    'ip_prefix': '10.12.115.0',
                                    'prefix_len': '24',
                                    'metric': 10,
                                },
                                '10.23.115.0/24': {
                                    'ip_prefix': '10.23.115.0',
                                    'prefix_len': '24',
                                    'metric': 10,
                                },
                                '10.36.3.3/32': {
                                    'ip_prefix': '10.36.3.3',
                                    'prefix_len': '32',
                                    'metric': 11,
                                },
                                '10.13.115.0/24': {
                                    'ip_prefix': '10.13.115.0',
                                    'prefix_len': '24',
                                    'metric': 20,
                                },
                            },
                            'hostname': 'R2_xr',
                            'mt_is_neighbor': {
                                'R1_xe.01': {
                                    'neighbor_id': 'R1_xe.01',
                                    'metric': 10,
                                },
                                'R2_xr.03': {
                                    'neighbor_id': 'R2_xr.03',
                                    'metric': 10,
                                },
                            },
                            'ipv6_address': '2001:2:2:2::2',
                            'mt_ipv6_reachability': {
                                '2001:2:2:2::2/128': {
                                    'ip_prefix': '2001:2:2:2::2',
                                    'prefix_len': '128',
                                    'metric': 10,
                                },
                                '2001:10:12:115::/64': {
                                    'ip_prefix': '2001:10:12:115::',
                                    'prefix_len': '64',
                                    'metric': 10,
                                },
                                '2001:10:23:115::/64': {
                                    'ip_prefix': '2001:10:23:115::',
                                    'prefix_len': '64',
                                    'metric': 10,
                                },
                                '2001:3:3:3::3/128': {
                                    'ip_prefix': '2001:3:3:3::3',
                                    'prefix_len': '128',
                                    'metric': 11,
                                },
                                '2001:10:13:115::/64': {
                                    'ip_prefix': '2001:10:13:115::',
                                    'prefix_len': '64',
                                    'metric': 20,
                                },
                            },
                            'topology': {
                                'ipv4': {
                                    'code': '0x0',
                                },
                                'ipv6': {
                                    'code': '0x2',
                                },
                            },
                        },
                        'R2_xr.03-00': {
                            'lsp_sequence_num': '0x00000118',
                            'lsp_checksum': '0xF5F1',
                            'lsp_holdtime': '872',
                            'lsp_rcvd': '1200',
                            'attach_bit': 0,
                            'p_bit': 0,
                            'overload_bit': 0,
                            'extended_is_neighbor': {
                                'R2_xr.00': {
                                    'neighbor_id': 'R2_xr.00',
                                    'metric': 0,
                                },
                                'R3_nx.00': {
                                    'neighbor_id': 'R3_nx.00',
                                    'metric': 0,
                                },
                            },
                        },
                        'R3_nx.00-00': {
                            'lsp_sequence_num': '0x00000192',
                            'lsp_checksum': '0x8221',
                            'lsp_holdtime': '1132',
                            'lsp_rcvd': '1199',
                            'attach_bit': 0,
                            'p_bit': 0,
                            'overload_bit': 0,
                            'area_address': '49.0001',
                            'nlpid': '0xCC 0x8E',
                            'router_id': '10.36.3.3',
                            'ip_address': '10.36.3.3',
                            'topology': {
                                'ipv6': {
                                    'code': '0x2',
                                },
                                'ipv4': {
                                    'code': '0x0',
                                },
                            },
                            'hostname': 'R3_nx',
                            'mt_is_neighbor': {
                                'R2_xr.03': {
                                    'neighbor_id': 'R2_xr.03',
                                    'metric': 40,
                                },
                                'R1_xe.02': {
                                    'neighbor_id': 'R1_xe.02',
                                    'metric': 40,
                                },
                            },
                            'extended_is_neighbor': {
                                'R2_xr.03': {
                                    'neighbor_id': 'R2_xr.03',
                                    'metric': 40,
                                },
                                'R1_xe.02': {
                                    'neighbor_id': 'R1_xe.02',
                                    'metric': 40,
                                },
                            },
                            'ipv4_internal_reachability': {
                                '10.36.3.3/32': {
                                    'ip_prefix': '10.36.3.3',
                                    'prefix_len': '32',
                                    'metric': 1,
                                },
                                '10.13.115.0/24': {
                                    'ip_prefix': '10.13.115.0',
                                    'prefix_len': '24',
                                    'metric': 40,
                                },
                                '10.23.115.0/24': {
                                    'ip_prefix': '10.23.115.0',
                                    'prefix_len': '24',
                                    'metric': 40,
                                },
                            },
                            'mt_ipv6_reachability': {
                                '2001:3:3:3::3/128': {
                                    'ip_prefix': '2001:3:3:3::3',
                                    'prefix_len': '128',
                                    'metric': 1,
                                },
                                '2001:10:13:115::/64': {
                                    'ip_prefix': '2001:10:13:115::',
                                    'prefix_len': '64',
                                    'metric': 40,
                                },
                                '2001:10:23:115::/64': {
                                    'ip_prefix': '2001:10:23:115::',
                                    'prefix_len': '64',
                                    'metric': 40,
                                },
                            },
                        },
                    },
                },
            },
            'test1': {
                'level': {
                    1: {
                        'R1_xe.00-00': {
                            'local_router': True,
                            'lsp_sequence_num': '0x0000011B',
                            'lsp_checksum': '0x3941',
                            'lsp_holdtime': '810',
                            'lsp_rcvd': '*',
                            'attach_bit': 0,
                            'p_bit': 0,
                            'overload_bit': 0,
                            'area_address': '49.0001',
                            'nlpid': '0xCC 0x8E',
                            'topology': {
                                'ipv4': {
                                    'code': '0x0',
                                },
                                'ipv6': {
                                    'code': '0x2',
                                },
                            },
                            'hostname': 'R1_xe',
                            'extended_is_neighbor': {
                                'R1_xe.02': {
                                    'neighbor_id': 'R1_xe.02',
                                    'metric': 10,
                                },
                            },
                            'mt_is_neighbor': {
                                'R1_xe.02': {
                                    'neighbor_id': 'R1_xe.02',
                                    'metric': 10,
                                },
                            },
                            'ip_address': '10.13.115.1',
                            'ipv4_internal_reachability': {
                                '10.12.115.0/24': {
                                    'ip_prefix': '10.12.115.0',
                                    'prefix_len': '24',
                                    'metric': 10,
                                },
                                '10.13.115.0/24': {
                                    'ip_prefix': '10.13.115.0',
                                    'prefix_len': '24',
                                    'metric': 10,
                                },
                            },
                            'ipv6_address': '2001:10:13:115::1',
                            'mt_ipv6_reachability': {
                                '2001:10:12:115::/64': {
                                    'ip_prefix': '2001:10:12:115::',
                                    'prefix_len': '64',
                                    'metric': 10,
                                },
                                '2001:10:13:115::/64': {
                                    'ip_prefix': '2001:10:13:115::',
                                    'prefix_len': '64',
                                    'metric': 10,
                                },
                            },
                        },
                        'R1_xe.02-00': {
                            'local_router': True,
                            'lsp_sequence_num': '0x0000011A',
                            'lsp_checksum': '0x7AB0',
                            'lsp_holdtime': '1080',
                            'lsp_rcvd': '*',
                            'attach_bit': 0,
                            'p_bit': 0,
                            'overload_bit': 0,
                            'extended_is_neighbor': {
                                'R1_xe.00': {
                                    'neighbor_id': 'R1_xe.00',
                                    'metric': 0,
                                },
                                'R3_nx.00': {
                                    'neighbor_id': 'R3_nx.00',
                                    'metric': 0,
                                },
                            },
                        },
                        'R3_nx.00-00': {
                            'lsp_sequence_num': '0x00000191',
                            'lsp_checksum': '0x7535',
                            'lsp_holdtime': '1068',
                            'lsp_rcvd': '1199',
                            'attach_bit': 0,
                            'p_bit': 0,
                            'overload_bit': 0,
                            'area_address': '49.0001',
                            'nlpid': '0xCC 0x8E',
                            'router_id': '10.36.3.3',
                            'ip_address': '10.36.3.3',
                            'topology': {
                                'ipv6': {
                                    'code': '0x2',
                                },
                                'ipv4': {
                                    'code': '0x0',
                                },
                            },
                            'hostname': 'R3_nx',
                            'mt_is_neighbor': {
                                'R1_xe.02': {
                                    'neighbor_id': 'R1_xe.02',
                                    'metric': 40,
                                },
                            },
                            'extended_is_neighbor': {
                                'R1_xe.02': {
                                    'neighbor_id': 'R1_xe.02',
                                    'metric': 40,
                                },
                            },
                            'ipv4_internal_reachability': {
                                '10.36.3.3/32': {
                                    'ip_prefix': '10.36.3.3',
                                    'prefix_len': '32',
                                    'metric': 1,
                                },
                                '10.13.115.0/24': {
                                    'ip_prefix': '10.13.115.0',
                                    'prefix_len': '24',
                                    'metric': 40,
                                },
                                '10.23.115.0/24': {
                                    'ip_prefix': '10.23.115.0',
                                    'prefix_len': '24',
                                    'metric': 40,
                                },
                            },
                            'mt_ipv6_reachability': {
                                '2001:3:3:3::3/128': {
                                    'ip_prefix': '2001:3:3:3::3',
                                    'prefix_len': '128',
                                    'metric': 1,
                                },
                                '2001:10:13:115::/64': {
                                    'ip_prefix': '2001:10:13:115::',
                                    'prefix_len': '64',
                                    'metric': 40,
                                },
                                '2001:10:23:115::/64': {
                                    'ip_prefix': '2001:10:23:115::',
                                    'prefix_len': '64',
                                    'metric': 40,
                                },
                            },
                        },
                    },
                    2: {
                        'R1_xe.00-00': {
                            'local_router': True,
                            'lsp_sequence_num': '0x0000011C',
                            'lsp_checksum': '0x9618',
                            'lsp_holdtime': '1009',
                            'lsp_rcvd': '*',
                            'attach_bit': 0,
                            'p_bit': 0,
                            'overload_bit': 0,
                            'area_address': '49.0001',
                            'nlpid': '0xCC 0x8E',
                            'topology': {
                                'ipv4': {
                                    'code': '0x0',
                                },
                                'ipv6': {
                                    'code': '0x2',
                                },
                            },
                            'hostname': 'R1_xe',
                            'extended_is_neighbor': {
                                'R1_xe.02': {
                                    'neighbor_id': 'R1_xe.02',
                                    'metric': 10,
                                },
                            },
                            'mt_is_neighbor': {
                                'R1_xe.02': {
                                    'neighbor_id': 'R1_xe.02',
                                    'metric': 10,
                                },
                            },
                            'ip_address': '10.13.115.1',
                            'ipv4_internal_reachability': {
                                '10.12.115.0/24': {
                                    'ip_prefix': '10.12.115.0',
                                    'prefix_len': '24',
                                    'metric': 10,
                                },
                                '10.13.115.0/24': {
                                    'ip_prefix': '10.13.115.0',
                                    'prefix_len': '24',
                                    'metric': 10,
                                },
                                '10.23.115.0/24': {
                                    'ip_prefix': '10.23.115.0',
                                    'prefix_len': '24',
                                    'metric': 50,
                                },
                            },
                            'ipv6_address': '2001:10:13:115::1',
                            'mt_ipv6_reachability': {
                                '2001:10:12:115::/64': {
                                    'ip_prefix': '2001:10:12:115::',
                                    'prefix_len': '64',
                                    'metric': 10,
                                },
                                '2001:10:13:115::/64': {
                                    'ip_prefix': '2001:10:13:115::',
                                    'prefix_len': '64',
                                    'metric': 10,
                                },
                                '2001:10:23:115::/64': {
                                    'ip_prefix': '2001:10:23:115::',
                                    'prefix_len': '64',
                                    'metric': 50,
                                },
                            },
                        },
                        'R1_xe.02-00': {
                            'local_router': True,
                            'lsp_sequence_num': '0x0000011B',
                            'lsp_checksum': '0x9022',
                            'lsp_holdtime': '995',
                            'lsp_rcvd': '*',
                            'attach_bit': 0,
                            'p_bit': 0,
                            'overload_bit': 0,
                            'extended_is_neighbor': {
                                'R1_xe.00': {
                                    'neighbor_id': 'R1_xe.00',
                                    'metric': 0,
                                },
                                'R3_nx.00': {
                                    'neighbor_id': 'R3_nx.00',
                                    'metric': 0,
                                },
                            },
                        },
                        'R3_nx.00-00': {
                            'lsp_sequence_num': '0x00000191',
                            'lsp_checksum': '0x7535',
                            'lsp_holdtime': '958',
                            'lsp_rcvd': '1199',
                            'attach_bit': 0,
                            'p_bit': 0,
                            'overload_bit': 0,
                            'area_address': '49.0001',
                            'nlpid': '0xCC 0x8E',
                            'router_id': '10.36.3.3',
                            'ip_address': '10.36.3.3',
                            'topology': {
                                'ipv6': {
                                    'code': '0x2',
                                },
                                'ipv4': {
                                    'code': '0x0',
                                },
                            },
                            'hostname': 'R3_nx',
                            'mt_is_neighbor': {
                                'R1_xe.02': {
                                    'neighbor_id': 'R1_xe.02',
                                    'metric': 40,
                                },
                            },
                            'extended_is_neighbor': {
                                'R1_xe.02': {
                                    'neighbor_id': 'R1_xe.02',
                                    'metric': 40,
                                },
                            },
                            'ipv4_internal_reachability': {
                                '10.36.3.3/32': {
                                    'ip_prefix': '10.36.3.3',
                                    'prefix_len': '32',
                                    'metric': 1,
                                },
                                '10.13.115.0/24': {
                                    'ip_prefix': '10.13.115.0',
                                    'prefix_len': '24',
                                    'metric': 40,
                                },
                                '10.23.115.0/24': {
                                    'ip_prefix': '10.23.115.0',
                                    'prefix_len': '24',
                                    'metric': 40,
                                },
                            },
                            'mt_ipv6_reachability': {
                                '2001:3:3:3::3/128': {
                                    'ip_prefix': '2001:3:3:3::3',
                                    'prefix_len': '128',
                                    'metric': 1,
                                },
                                '2001:10:13:115::/64': {
                                    'ip_prefix': '2001:10:13:115::',
                                    'prefix_len': '64',
                                    'metric': 40,
                                },
                                '2001:10:23:115::/64': {
                                    'ip_prefix': '2001:10:23:115::',
                                    'prefix_len': '64',
                                    'metric': 40,
                                },
                            },
                        },
                    },
                },
            },
        },
    }

    golden_output1 = {'execute.return_value': '''\
        R1_xe#show isis database detail

        Tag test:
        IS-IS Level-1 Link State Database:
        LSPID                 LSP Seq Num  LSP Checksum  LSP Holdtime/Rcvd      ATT/P/OL
        R1_xe.00-00         * 0x0000011D   0x2165                 519/*         0/0/0
          Area Address: 49.0001
          NLPID:        0xCC 0x8E
          Topology:     IPv4 (0x0)
                        IPv6 (0x2)
          Hostname: R1_xe
          Metric: 10         IS-Extended R1_xe.02
          Metric: 10         IS (MT-IPv6) R1_xe.02
          Metric: 10         IS-Extended R1_xe.01
          Metric: 10         IS (MT-IPv6) R1_xe.01
          IP Address:   10.13.115.1
          Metric: 10         IP 10.12.115.0/24
          Metric: 10         IP 10.13.115.0/24
          IPv6 Address: 2001:10:13:115::1
          Metric: 10         IPv6 (MT-IPv6) 2001:10:12:115::/64
          Metric: 10         IPv6 (MT-IPv6) 2001:10:13:115::/64
        R1_xe.01-00         * 0x00000118   0x850F                1087/*         0/0/0
          Metric: 0          IS-Extended R1_xe.00
          Metric: 0          IS-Extended R2_xr.00
        R1_xe.02-00         * 0x00000118   0x7EAE                 752/*         0/0/0
          Metric: 0          IS-Extended R1_xe.00
          Metric: 0          IS-Extended R3_nx.00
        R2_xr.00-00           0x00000120   0xC84E                 754/1200      0/0/0
          Area Address: 49.0001
          Metric: 10         IS-Extended R1_xe.01
          Metric: 10         IS-Extended R2_xr.03
          NLPID:        0xCC 0x8E
          IP Address:   10.16.2.2
          Metric: 10         IP 10.16.2.2/32
          Metric: 10         IP 10.12.115.0/24
          Metric: 10         IP 10.23.115.0/24
          Hostname: R2_xr
          Metric: 10         IS (MT-IPv6) R1_xe.01
          Metric: 10         IS (MT-IPv6) R2_xr.03
          IPv6 Address: 2001:2:2:2::2
          Metric: 10         IPv6 (MT-IPv6) 2001:2:2:2::2/128
          Metric: 10         IPv6 (MT-IPv6) 2001:10:12:115::/64
          Metric: 10         IPv6 (MT-IPv6) 2001:10:23:115::/64
          Topology:     IPv4 (0x0)
                        IPv6 (0x2)
        R2_xr.03-00           0x00000118   0xF5F1                 563/1200      0/0/0
          Metric: 0          IS-Extended R2_xr.00
          Metric: 0          IS-Extended R3_nx.00
        R3_nx.00-00           0x00000193   0x8022                1018/1200      0/0/0
          Area Address: 49.0001
          NLPID:        0xCC 0x8E
          Router ID:    10.36.3.3
          IP Address:   10.36.3.3
          Topology:     IPv6 (0x2)
                        IPv4 (0x0)
          Hostname: R3_nx
          Metric: 40         IS (MT-IPv6) R2_xr.03
          Metric: 40         IS (MT-IPv6) R1_xe.02
          Metric: 40         IS-Extended R2_xr.03
          Metric: 40         IS-Extended R1_xe.02
          Metric: 1          IP 10.36.3.3/32
          Metric: 40         IP 10.13.115.0/24
          Metric: 40         IP 10.23.115.0/24
          Metric: 1          IPv6 (MT-IPv6) 2001:3:3:3::3/128
          Metric: 40         IPv6 (MT-IPv6) 2001:10:13:115::/64
          Metric: 40         IPv6 (MT-IPv6) 2001:10:23:115::/64
        IS-IS Level-2 Link State Database:
        LSPID                 LSP Seq Num  LSP Checksum  LSP Holdtime/Rcvd      ATT/P/OL
        R1_xe.00-00         * 0x0000011D   0x27D0                 521/*         0/0/0
          Area Address: 49.0001
          NLPID:        0xCC 0x8E
          Topology:     IPv4 (0x0)
                        IPv6 (0x2)
          Hostname: R1_xe
          Metric: 10         IS-Extended R1_xe.02
          Metric: 10         IS (MT-IPv6) R1_xe.02
          Metric: 10         IS-Extended R1_xe.01
          Metric: 10         IS (MT-IPv6) R1_xe.01
          IP Address:   10.13.115.1
          Metric: 10         IP 10.12.115.0/24
          Metric: 10         IP 10.13.115.0/24
          Metric: 20         IP 10.23.115.0/24
          IPv6 Address: 2001:10:13:115::1
          Metric: 10         IPv6 (MT-IPv6) 2001:10:12:115::/64
          Metric: 10         IPv6 (MT-IPv6) 2001:10:13:115::/64
          Metric: 20         IPv6 (MT-IPv6) 2001:10:23:115::/64
        R1_xe.01-00         * 0x00000118   0x9D7F                 930/*         0/0/0
          Metric: 0          IS-Extended R1_xe.00
          Metric: 0          IS-Extended R2_xr.00
        R1_xe.02-00         * 0x0000011E   0x8A25                1098/*         0/0/0
          Metric: 0          IS-Extended R1_xe.00
          Metric: 0          IS-Extended R3_nx.00
        R2_xr.00-00           0x00000120   0x1585                 662/1200      0/0/0
          Area Address: 49.0001
          Metric: 10         IS-Extended R1_xe.01
          Metric: 10         IS-Extended R2_xr.03
          NLPID:        0xCC 0x8E
          IP Address:   10.16.2.2
          Metric: 10         IP 10.16.2.2/32
          Metric: 10         IP 10.12.115.0/24
          Metric: 10         IP 10.23.115.0/24
          Metric: 11         IP 10.36.3.3/32
          Metric: 20         IP 10.13.115.0/24
          Hostname: R2_xr
          Metric: 10         IS (MT-IPv6) R1_xe.01
          Metric: 10         IS (MT-IPv6) R2_xr.03
          IPv6 Address: 2001:2:2:2::2
          Metric: 10         IPv6 (MT-IPv6) 2001:2:2:2::2/128
          Metric: 10         IPv6 (MT-IPv6) 2001:10:12:115::/64
          Metric: 10         IPv6 (MT-IPv6) 2001:10:23:115::/64
          Metric: 11         IPv6 (MT-IPv6) 2001:3:3:3::3/128
          Metric: 20         IPv6 (MT-IPv6) 2001:10:13:115::/64
          Topology:     IPv4 (0x0)
                        IPv6 (0x2)
        R2_xr.03-00           0x00000118   0xF5F1                 872/1200      0/0/0
          Metric: 0          IS-Extended R2_xr.00
          Metric: 0          IS-Extended R3_nx.00
        R3_nx.00-00           0x00000192   0x8221                1132/1199      0/0/0
          Area Address: 49.0001
          NLPID:        0xCC 0x8E
          Router ID:    10.36.3.3
          IP Address:   10.36.3.3
          Topology:     IPv6 (0x2)
                        IPv4 (0x0)
          Hostname: R3_nx
          Metric: 40         IS (MT-IPv6) R2_xr.03
          Metric: 40         IS (MT-IPv6) R1_xe.02
          Metric: 40         IS-Extended R2_xr.03
          Metric: 40         IS-Extended R1_xe.02
          Metric: 1          IP 10.36.3.3/32
          Metric: 40         IP 10.13.115.0/24
          Metric: 40         IP 10.23.115.0/24
          Metric: 1          IPv6 (MT-IPv6) 2001:3:3:3::3/128
          Metric: 40         IPv6 (MT-IPv6) 2001:10:13:115::/64
          Metric: 40         IPv6 (MT-IPv6) 2001:10:23:115::/64

        Tag test1:
        IS-IS Level-1 Link State Database:
        LSPID                 LSP Seq Num  LSP Checksum  LSP Holdtime/Rcvd      ATT/P/OL
        R1_xe.00-00         * 0x0000011B   0x3941                 810/*         0/0/0
          Area Address: 49.0001
          NLPID:        0xCC 0x8E
          Topology:     IPv4 (0x0)
                        IPv6 (0x2)
          Hostname: R1_xe
          Metric: 10         IS-Extended R1_xe.02
          Metric: 10         IS (MT-IPv6) R1_xe.02
          IP Address:   10.13.115.1
          Metric: 10         IP 10.12.115.0/24
          Metric: 10         IP 10.13.115.0/24
          IPv6 Address: 2001:10:13:115::1
          Metric: 10         IPv6 (MT-IPv6) 2001:10:12:115::/64
          Metric: 10         IPv6 (MT-IPv6) 2001:10:13:115::/64
        R1_xe.02-00         * 0x0000011A   0x7AB0                1080/*         0/0/0
          Metric: 0          IS-Extended R1_xe.00
          Metric: 0          IS-Extended R3_nx.00
        R3_nx.00-00           0x00000191   0x7535                1068/1199      0/0/0
          Area Address: 49.0001
          NLPID:        0xCC 0x8E
          Router ID:    10.36.3.3
          IP Address:   10.36.3.3
          Topology:     IPv6 (0x2)
                        IPv4 (0x0)
          Hostname: R3_nx
          Metric: 40         IS (MT-IPv6) R1_xe.02
          Metric: 40         IS-Extended R1_xe.02
          Metric: 1          IP 10.36.3.3/32
          Metric: 40         IP 10.13.115.0/24
          Metric: 40         IP 10.23.115.0/24
          Metric: 1          IPv6 (MT-IPv6) 2001:3:3:3::3/128
          Metric: 40         IPv6 (MT-IPv6) 2001:10:13:115::/64
          Metric: 40         IPv6 (MT-IPv6) 2001:10:23:115::/64
        IS-IS Level-2 Link State Database:
        LSPID                 LSP Seq Num  LSP Checksum  LSP Holdtime/Rcvd      ATT/P/OL
        R1_xe.00-00         * 0x0000011C   0x9618                1009/*         0/0/0
          Area Address: 49.0001
          NLPID:        0xCC 0x8E
          Topology:     IPv4 (0x0)
                        IPv6 (0x2)
          Hostname: R1_xe
          Metric: 10         IS-Extended R1_xe.02
          Metric: 10         IS (MT-IPv6) R1_xe.02
          IP Address:   10.13.115.1
          Metric: 10         IP 10.12.115.0/24
          Metric: 10         IP 10.13.115.0/24
          Metric: 50         IP 10.23.115.0/24
          IPv6 Address: 2001:10:13:115::1
          Metric: 10         IPv6 (MT-IPv6) 2001:10:12:115::/64
          Metric: 10         IPv6 (MT-IPv6) 2001:10:13:115::/64
          Metric: 50         IPv6 (MT-IPv6) 2001:10:23:115::/64
        R1_xe.02-00         * 0x0000011B   0x9022                 995/*         0/0/0
          Metric: 0          IS-Extended R1_xe.00
          Metric: 0          IS-Extended R3_nx.00
        R3_nx.00-00           0x00000191   0x7535                 958/1199      0/0/0
          Area Address: 49.0001
          NLPID:        0xCC 0x8E
          Router ID:    10.36.3.3
          IP Address:   10.36.3.3
          Topology:     IPv6 (0x2)
                        IPv4 (0x0)
          Hostname: R3_nx
          Metric: 40         IS (MT-IPv6) R1_xe.02
          Metric: 40         IS-Extended R1_xe.02
          Metric: 1          IP 10.36.3.3/32
          Metric: 40         IP 10.13.115.0/24
          Metric: 40         IP 10.23.115.0/24
          Metric: 1          IPv6 (MT-IPv6) 2001:3:3:3::3/128
          Metric: 40         IPv6 (MT-IPv6) 2001:10:13:115::/64
          Metric: 40         IPv6 (MT-IPv6) 2001:10:23:115::/64
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        platform_obj = ShowIsisDatabaseDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = platform_obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        platform_obj = ShowIsisDatabaseDetail(device=self.device)
        parsed_output = platform_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden1(self):
        self.device = Mock(**self.golden_output1)
        platform_obj = ShowIsisDatabaseDetail(device=self.device)
        parsed_output = platform_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)


class TestShowRunSecIsis(unittest.TestCase):
    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'instance':{
            'test':{
                'vrf':{
                    'default':{}
                }
            },
            'test1':{
                'vrf':{
                    'VRF1':{}
                }
            }
        }
    }

    golden_output = {'execute.return_value': '''\

    R2#show run | sec isis
     ip router isis test
     ipv6 router isis test
     ip router isis test1
     ipv6 router isis test1
     ip router isis test
     ipv6 router isis test
     ip router isis test1
     ipv6 router isis test1
    router isis test
     net 49.0001.11ff.2211.2222.00
     metric-style wide
     !
     address-family ipv6
      multi-topology
     exit-address-family
    router isis test1
     vrf VRF1
     net 49.0001.11ff.2211.2222.00
     metric-style wide
     !
     address-family ipv6
      multi-topology
     exit-address-family
    R1_xe#
    '''
    }

    golden_parsed_output_2 = {
        'instance': {
            '': {
                'vrf': {
                    'default': {}}}}}

    golden_output_2 = {'execute.return_value': '''
         ip router isis
         ipv6 router isis
         ip router isis
         ipv6 router isis
         ip router isis
         ipv6 router isis
         ip router isis
         ipv6 router isis
        router isis
         net 47.0002.00ff.0000.0002.00
         is-type level-1
         metric-style wide
         mpls traffic-eng router-id Loopback0
         mpls traffic-eng level-1
    '''}

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowRunSectionIsis(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        obj = ShowRunSectionIsis(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_2)


# ====================================
#  Unit test for 'show isis neighbors'
# ====================================
class TestShowIsisNeighbors(unittest.TestCase):
    '''Unit test for "show isis neighbors"'''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'isis': {
            'test': {
                'neighbors': {
                    'R2_xr': {
                        'type': {
                            'L1': {
                                'interface': 'Gi2.115',
                                'ip_address': '10.12.115.2',
                                'state': 'UP',
                                'holdtime': '7',
                                'circuit_id': 'R2_xr.01'},
                            'L2': {
                                'interface': 'Gi2.115',
                                'ip_address': '10.12.115.2',
                                'state': 'UP',
                                'holdtime': '7',
                                'circuit_id': 'R2_xr.01'}}},
                    'R3_nx': {
                        'type': {
                            'L1': {
                                'interface': 'Gi3.115',
                                'ip_address': '10.13.115.3',
                                'state': 'UP',
                                'holdtime': '28',
                                'circuit_id': 'R1_xe.02'},
                            'L2': {
                                'interface': 'Gi3.115',
                                'ip_address': '10.13.115.3',
                                'state': 'UP',
                                'holdtime': '23',
                                'circuit_id': 'R1_xe.02'}}}}},
            'test1': {
                'neighbors': {
                    '2222.22ff.4444': {
                        'type': {
                            'L1': {
                                'interface': 'Gi2.415',
                                'ip_address': '10.12.115.2',
                                'state': 'INIT',
                                'holdtime': '21',
                                'circuit_id': '2222.22ff.4444.01'},
                            'L2': {
                                'interface': 'Gi2.415',
                                'ip_address': '10.12.115.2',
                                'state': 'INIT',
                                'holdtime': '20',
                                'circuit_id': '2222.22ff.4444.01'}}},
                    'R3_nx': {
                        'type': {
                            'L1': {
                                'interface': 'Gi3.415',
                                'ip_address': '10.13.115.3',
                                'state': 'UP',
                                'holdtime': '21',
                                'circuit_id': 'R1_xe.02'},
                            'L2': {
                                'interface': 'Gi3.415',
                                'ip_address': '10.13.115.3',
                                'state': 'UP',
                                'holdtime': '27',
                                'circuit_id': 'R1_xe.02'}}}}}}}

    golden_output1 = {'execute.return_value': '''
        R1_xe#show isis neighbors 

        Tag test:
        System Id       Type Interface     IP Address      State Holdtime Circuit Id
        R2_xr           L1   Gi2.115       10.12.115.2     UP    7        R2_xr.01           
        R2_xr           L2   Gi2.115       10.12.115.2     UP    7        R2_xr.01           
        R3_nx           L1   Gi3.115       10.13.115.3     UP    28       R1_xe.02           
        R3_nx           L2   Gi3.115       10.13.115.3     UP    23       R1_xe.02           
        
        Tag test1:
        System Id       Type Interface     IP Address      State Holdtime Circuit Id
        2222.22ff.4444  L1   Gi2.415       10.12.115.2     INIT  21       2222.22ff.4444.01  
        2222.22ff.4444  L2   Gi2.415       10.12.115.2     INIT  20       2222.22ff.4444.01  
        R3_nx           L1   Gi3.415       10.13.115.3     UP    21       R1_xe.02           
        R3_nx           L2   Gi3.415       10.13.115.3     UP    27       R1_xe.02           
        
    '''}

    def test_show_isis_neighbors_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIsisNeighbors(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_isis_neighbors_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowIsisNeighbors(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)


if __name__ == '__main__':
    unittest.main()