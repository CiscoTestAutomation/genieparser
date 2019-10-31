#!/bin/env python
import unittest
from unittest.mock import Mock
from ats.topology import Device

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
                        '7777.7777.7777': {
                            'hostname': 'R7',
                            'level': 2,
                        },
                        '2222.2222.2222':{
                            'hostname': 'R2',
                            'local_router': True,
                        }
                    }
                }
            },
            'test':{
                'hostname_db': {
                    'hostname': {
                        '9999.9999.9999': {
                            'hostname': 'R9',
                            'level': 2,
                        },

                        '8888.8888.8888': {
                            'hostname': 'R8',
                            'level': 2,
                        },
                        '7777.7777.7777': {
                            'hostname': 'R7',
                            'level': 2,
                        },
                        '5555.5555.5555': {
                            'hostname': 'R5',
                            'level': 2,
                        },
                        '3333.3333.3333': {
                            'hostname': 'R3',
                            'level': 2,
                        },
                        '1111.1111.1111': {
                            'hostname': 'R1',
                            'level': 1,
                        },
                        '2222.2222.2222': {
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
     2     7777.7777.7777 R7
         * 2222.2222.2222 R2
    Level  System ID      Dynamic Hostname  (test)
     2     9999.9999.9999 R9
     2     8888.8888.8888 R8
     2     7777.7777.7777 R7
     2     5555.5555.5555 R5
     2     3333.3333.3333 R3
     1     1111.1111.1111 R1
         * 2222.2222.2222 R2
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
    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'tag':{
            'VRF1':{
                'level':{
                    1: {
                        'R2.00-00':{
                            'lsp_sequence_num': '0x00000007',
                            'lsp_checksum': '0x8A6D',
                            'local_router': True,
                            'lsp_holdtime': '403',
                            'lsp_rcvd': '*',
                            'attach_bit': 1,
                            'p_bit': 0,
                            'overload_bit': 0,
                            'area_address': '49.0001',
                            'nlpid': '0xCC 0x8E',
                            'topology': {
                                'ipv4': {
                                    'code':'0x0',
                                },
                                'ipv6': {
                                    'code': '0x4002 ATT'
                                }
                            },
                            'hostname': 'R2',
                            'ip_address': '10.84.66.66',
                            '10.229.7.0/24': {
                                'ip': {
                                    'metric': 10,
                                },
                            },
                            '10.84.66.66/32':{
                                'ip': {
                                    'metric': 10,
                                },
                            },
                            'ipv6_address': '2001:DB8:66:66:66::66',
                            '2001:DB8:20:2::/64': {
                                'ipv6': {
                                    'metric': 10,
                                    'mt_ipv6': True
                                },
                            },
                            '2001:DB8:66:66:66::66/128': {
                                'ipv6':{
                                    'metric': 10,
                                    'mt_ipv6': True
                                },
                            },
                        },
                    },
                    2: {
                        'R2.00-00': {
                            'lsp_sequence_num': '0x00000008',
                            'lsp_checksum': '0x621E',
                            'local_router': True,
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
                                    'code': '0x2'
                                }
                            },
                            'hostname': 'R2',
                            'R2.01': {
                                'is-extended': {
                                        'metric': 10,
                                },
                                'is': {
                                    'metric': 10,
                                    'mt_ipv6': True,
                                },
                            },
                            'ip_address': '10.84.66.66',
                            '10.229.7.0/24': {
                                'ip': {
                                    'metric': 10,
                                },
                            },
                            '10.84.66.66/32': {
                                'ip':{
                                    'metric': 10,
                                },
                            },
                            'ipv6_address': '2001:DB8:66:66:66::66',
                            '2001:DB8:20:2::/64': {
                                    'ipv6': {
                                        'metric': 10,
                                        'mt_ipv6': True
                                    },
                                },
                                '2001:DB8:66:66:66::66/128': {
                                    'ipv6': {
                                        'metric': 10,
                                        'mt_ipv6': True
                                    }
                                },
                            },
                        'R2.01-00': {
                            'lsp_sequence_num': '0x00000002',
                            'lsp_checksum': '0x3334',
                            'local_router': True,
                            'lsp_holdtime': '414',
                            'lsp_rcvd': '*',
                            'attach_bit': 0,
                            'p_bit': 0,
                            'overload_bit': 0,
                            'R2.00': {
                                'is-extended': {
                                    'metric': 0,
                                },
                            },
                            'R7.00': {
                                'is-extended': {
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
                                'ipv4': {
                                    'code': '0x0',
                                },
                                'ipv6': {
                                    'code': '0x2'
                                }
                            },
                            'hostname': 'R7',
                            'R2.01': {
                                'is-extended': {
                                    'metric': 40,
                                },
                                'is': {
                                    'metric': 40,
                                    'mt_ipv6': True,
                                },
                            },
                            '10.1.77.77/32':{
                                'ip': {
                                    'metric': 1

                                }
                            },
                            '10.229.7.0/24': {
                                'ip': {
                                    'metric': 40
                                }
                            },
                            '2001:DB8:77:77:77::77/128': {
                                'ipv6': {
                                    'metric': 1,
                                    'mt_ipv6': True
                                }
                            },
                            '2001:DB8:20:2::/64': {
                                'ipv6': {
                                    'metric': 40,
                                    'mt_ipv6': True
                                }
                            },
                        },
                    }
                }
            }
        }
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
    '''
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        platform_obj = ShowIsisDatabaseDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = platform_obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        platform_obj = ShowIsisDatabaseDetail(device=self.device)
        parsed_output = platform_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

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
     net 49.0001.1111.1111.1111.00
     metric-style wide
     !
     address-family ipv6
      multi-topology
     exit-address-family
    router isis test1
     vrf VRF1
     net 49.0001.1111.1111.1111.00
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
         net 47.0002.0000.0000.0002.00
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
                    '2222.2222.2222': {
                        'type': {
                            'L1': {
                                'interface': 'Gi2.415',
                                'ip_address': '10.12.115.2',
                                'state': 'INIT',
                                'holdtime': '21',
                                'circuit_id': '2222.2222.2222.01'},
                            'L2': {
                                'interface': 'Gi2.415',
                                'ip_address': '10.12.115.2',
                                'state': 'INIT',
                                'holdtime': '20',
                                'circuit_id': '2222.2222.2222.01'}}},
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
        2222.2222.2222  L1   Gi2.415       10.12.115.2     INIT  21       2222.2222.2222.01  
        2222.2222.2222  L2   Gi2.415       10.12.115.2     INIT  20       2222.2222.2222.01  
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