#!/bin/env python
import unittest
from unittest.mock import Mock
from ats.topology import Device

from metaparser.util.exceptions import SchemaEmptyParserError,\
                                       SchemaMissingKeyError
from parser.iosxe.show_lag import ShowLacpSysId,\
                                  ShowEtherchannelSummary,\
                                  ShowLacpCounters,\
                                  ShowLacpInternal,\
                                  ShowLacpNeighbor,\
                                  ShowPagpCounters, \
                                  ShowPagpNeighbor,\
                                  ShowPagpInternal

###################################################
# unit test for show lacp sys-id
####################################################
class test_show_lacp_sysid(unittest.TestCase):
    """unit test for show lacp sysid"""

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
    csr1000v-2#show lacp sys-id
    32768, 001e.49af.8c00
    '''}

    golden_parsed_output = {
        'system_id_mac': '001e.49af.8c00',
        'system_priority': 32768,
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowLacpSysId(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowLacpSysId(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)
###################################################
# unit test for show lacp counter
####################################################
class test_show_lacp_counters(unittest.TestCase):
    """unit test for show lacp counters """

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
    csr1000v-2#show lacp counters
                 LACPDUs         Marker      Marker Response    LACPDUs
    Port       Sent   Recv     Sent   Recv     Sent   Recv      Pkts Err
    ---------------------------------------------------------------------
    Channel group: 1
    Gi2         27     22       0      0        0      0         0
    Gi3         24     21       0      0        0      0         0

                 LACPDUs         Marker      Marker Response    LACPDUs
    Port       Sent   Recv     Sent   Recv     Sent   Recv      Pkts Err
    ---------------------------------------------------------------------
    Channel group: 2
    Gi4         24     31       0      0        0      0         0
    Gi5         14     10       0      0        0      0         0
    Gi6         13     11       0      0        0      0         0
    '''}

    golden_parsed_output = {
        'interfaces': {
            'Port-channel1': {
                'name': 'Port-channel1',
                'protocol': 'lacp',
                'members': {
                    'GigabitEthernet2': {
                        'interface': 'GigabitEthernet2',
                        'counters': {
                            'lacp_in_pkts': 22,
                            'lacp_out_pkts': 27,
                            'lacp_errors': 0,
                            'marker_in_pkts': 0,
                            'marker_out_pkts': 0,
                            'marker_response_in_pkts': 0,
                            'marker_response_out_pkts': 0,
                        },
                    },
                    'GigabitEthernet3': {
                        'interface': 'GigabitEthernet3',
                        'counters': {
                            'lacp_in_pkts': 21,
                            'lacp_out_pkts': 24,
                            'lacp_errors': 0,
                            'marker_in_pkts': 0,
                            'marker_out_pkts': 0,
                            'marker_response_in_pkts': 0,
                            'marker_response_out_pkts': 0,
                        },
                    },
                }
            },
            'Port-channel2': {
               'name': 'Port-channel2',
               'protocol': 'lacp',
               'members': {
                    'GigabitEthernet4': {
                        'interface': 'GigabitEthernet4',
                        'counters': {
                            'lacp_in_pkts': 31,
                            'lacp_out_pkts': 24,
                            'lacp_errors': 0,
                            'marker_in_pkts': 0,
                            'marker_out_pkts': 0,
                            'marker_response_in_pkts': 0,
                            'marker_response_out_pkts': 0,
                        },
                    },
                    'GigabitEthernet5': {
                        'interface': 'GigabitEthernet5',
                        'counters': {
                            'lacp_in_pkts': 10,
                            'lacp_out_pkts': 14,
                            'lacp_errors': 0,
                            'marker_in_pkts': 0,
                            'marker_out_pkts': 0,
                            'marker_response_in_pkts': 0,
                            'marker_response_out_pkts': 0,
                        },
                    },
                   'GigabitEthernet6': {
                       'interface': 'GigabitEthernet6',
                       'counters': {
                           'lacp_in_pkts': 11,
                           'lacp_out_pkts': 13,
                           'lacp_errors': 0,
                           'marker_in_pkts': 0,
                           'marker_out_pkts': 0,
                           'marker_response_in_pkts': 0,
                           'marker_response_out_pkts': 0,
                       },
                   },
               },
           },
        },
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowLacpCounters(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowLacpCounters(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

###################################################
# unit test for show lacp internal
####################################################
class test_show_lacp_internal(unittest.TestCase):
    """unit test for show lacp internal """

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
    csr1000v-2#show lacp internal
    Flags:  S - Device is requesting Slow LACPDUs
            F - Device is requesting Fast LACPDUs
            A - Device is in Active mode       P - Device is in Passive mode

    Channel group 1
                                LACP port     Admin     Oper    Port        Port
    Port      Flags   State     Priority      Key       Key     Number      State
    Gi2       SA      bndl      32768         0x1       0x1     0x1         0x3D
    Gi3       SA      bndl      32768         0x1       0x1     0x1         0x3D

    Channel group 2
                                LACP port     Admin     Oper    Port        Port
    Port      Flags   State     Priority      Key       Key     Number      State
    Gi4       SA      bndl      32768         0x2       0x2     0x1         0x3D
    Gi5       SA      bndl      32768         0x2       0x2     0x1         0x3D
    Gi6       SA      bndl      32768         0x2       0x2     0x1         0x3D
    '''}

    golden_parsed_output = {
        'interfaces': {
            'Port-channel1': {
                'name': 'Port-channel1',
                'protocol': 'lacp',
                'members': {
                    'GigabitEthernet2': {
                        'interface': 'GigabitEthernet2',
                        'oper_key': 1,
                        'admin_key': 1,
                        'port_num': 1,
                        'lacp_port_priority': 32768,
                        'flags': 'SA',
                        'activity': 'auto',
                        'state': 'bndl',
                        'bundled': True,
                        'port_state': 61,
                        },
                    'GigabitEthernet3': {
                        'interface': 'GigabitEthernet3',
                        'oper_key': 1,
                        'admin_key': 1,
                        'port_num': 1,
                        'lacp_port_priority': 32768,
                        'flags': 'SA',
                        'activity': 'auto',
                        'state': 'bndl',
                        'bundled': True,
                        'port_state': 61,
                    },
                },
            },
            'Port-channel2': {
                'name': 'Port-channel2',
                'protocol': 'lacp',
                'members': {
                    'GigabitEthernet4': {
                        'interface': 'GigabitEthernet4',
                        'oper_key': 2,
                        'admin_key': 2,
                        'port_num': 1,
                        'lacp_port_priority': 32768,
                        'flags': 'SA',
                        'state': 'bndl',
                        'activity': 'auto',
                        'bundled': True,
                        'port_state': 61,
                    },
                    'GigabitEthernet5': {
                        'interface': 'GigabitEthernet5',
                        'oper_key': 2,
                        'admin_key': 2,
                        'port_num': 1,
                        'lacp_port_priority': 32768,
                        'flags': 'SA',
                        'activity': 'auto',
                        'state': 'bndl',
                        'bundled': True,
                        'port_state': 61,
                    },
                    'GigabitEthernet6': {
                        'interface': 'GigabitEthernet6',
                        'oper_key': 2,
                        'admin_key': 2,
                        'port_num': 1,
                        'lacp_port_priority': 32768,
                        'flags': 'SA',
                        'activity': 'auto',
                        'state': 'bndl',
                        'bundled': True,
                        'port_state': 61,
                    },
                },
            },
        }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowLacpInternal(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowLacpInternal(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

###################################################
# unit test for show lacp neighbor
####################################################
class test_show_lacp_neighbor(unittest.TestCase):
    """unit test for show lacp neighbor """

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
    sr1000v-2#show lacp neighbor
    Flags:  S - Device is requesting Slow LACPDUs
            F - Device is requesting Fast LACPDUs
            A - Device is in Active mode       P - Device is in Passive mode

    Channel group 1 neighbors

                      LACP port                        Admin  Oper   Port    Port
    Port      Flags   Priority  Dev ID          Age    key    Key    Number  State
    Gi2       SA      32768     001e.49e6.bc00  25s    0x0    0x1    0x1     0x3D
    Gi3       SA      32768     001e.49e6.bc00  19s    0x0    0x1    0x1     0x3D

    Channel group 2 neighbors

                      LACP port                        Admin  Oper   Port    Port
    Port      Flags   Priority  Dev ID          Age    key    Key    Number  State
    Gi4       SP      32768     001e.49e6.bc00  15s    0x0    0x2    0x1     0x3C
    Gi5       SP      32768     001e.49e6.bc00   1s    0x0    0x2    0x1     0x3C
    Gi6       SP      32768     001e.49e6.bc00   0s    0x0    0x2    0x1     0x3C
    '''}

    golden_parsed_output = {
        'interfaces': {
            'Port-channel1': {
                'name': 'Port-channel1',
                'protocol': 'lacp',
                'members': {
                    'GigabitEthernet2': {
                        'interface': 'GigabitEthernet2',
                        'oper_key': 1,
                        'admin_key': 0,
                        'port_num': 1,
                        'lacp_port_priority': 32768,
                        'flags': 'SA',
                        'activity' : 'active',
                        'partner_id': '001e.49e6.bc00',
                        'age': 25,
                        'port_state': 61
                        },
                    'GigabitEthernet3': {
                        'interface': 'GigabitEthernet3',
                        'oper_key': 1,
                        'admin_key': 0,
                        'port_num': 1,
                        'lacp_port_priority': 32768,
                        'flags': 'SA',
                        'activity': 'active',
                        'port_state': 61,
                        'partner_id': '001e.49e6.bc00',
                        'age': 19,
                    },
                },
            },
            'Port-channel2': {
                'name': 'Port-channel2',
                'protocol': 'lacp',
                'members': {
                    'GigabitEthernet4': {
                        'interface': 'GigabitEthernet4',
                        'oper_key': 2,
                        'admin_key': 0,
                        'port_num': 1,
                        'lacp_port_priority': 32768,
                        'flags': 'SP',
                        'port_state': 60,
                        'activity': 'passive',
                        'partner_id': '001e.49e6.bc00',
                        'age': 15,
                    },
                    'GigabitEthernet5': {
                        'interface': 'GigabitEthernet5',
                        'oper_key': 2,
                        'admin_key': 0,
                        'port_num': 1,
                        'lacp_port_priority': 32768,
                        'flags': 'SP',
                        'port_state': 60,
                        'activity': 'passive',
                        'partner_id': '001e.49e6.bc00',
                        'age': 1
                    },
                    'GigabitEthernet6': {
                        'interface': 'GigabitEthernet6',
                        'oper_key': 2,
                        'admin_key': 0,
                        'port_num': 1,
                        'lacp_port_priority': 32768,
                        'flags': 'SP',
                        'port_state': 60,
                        'activity': 'passive',
                        'partner_id': '001e.49e6.bc00',
                        'age': 0
                    },
                },
            },
        }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowLacpNeighbor(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowLacpNeighbor(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

###################################################
# unit test for show pagp neighbor
####################################################
class test_show_pagp_neighbor(unittest.TestCase):
    """unit test for show pagp neighbor """

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
    iosvl2-1#show pagp neighbor
    Flags:  S - Device is sending Slow hello.  C - Device is in Consistent state.
            A - Device is in Auto mode.        P - Device learns on physical port.

    Channel group 1 neighbors
              Partner              Partner          Partner         Partner Group
    Port      Name                 Device ID        Port       Age  Flags   Cap.
    Gi0/1     iosvl2-2             5e02.4001.8000   Gi0/1       11s SC      10001
    Gi0/2     iosvl2-2             5e02.4001.8000   Gi0/2       16s SC      10001

    Channel group 2 neighbors
              Partner              Partner          Partner         Partner Group
    Port      Name                 Device ID        Port       Age  Flags   Cap.
    Gi0/3     iosvl2-2             5e02.4001.8000   Gi0/3       18s SC      20001
    Gi1/0     iosvl2-2             5e02.4001.8000   Gi1/0       25s SC      20001
    Gi1/1     iosvl2-2             5e02.4001.8000   Gi1/1        0s SC      20001
    '''}

    golden_parsed_output = {
        'interfaces': {
            'Port-channel1': {
                'name': 'Port-channel1',
                'protocol': 'pagp',
                'members': {
                    'GigabitEthernet0/1': {
                        'interface': 'GigabitEthernet0/1',
                        'partner_name': 'iosvl2-2',
                        'partner_id': '5e02.4001.8000',
                        'partner_port': 'GigabitEthernet0/1',
                        'age': 11,
                        'flags': 'SC',
                        'group_cap': 10001,
                    },
                    'GigabitEthernet0/2': {
                        'interface': 'GigabitEthernet0/2',
                        'partner_name': 'iosvl2-2',
                        'partner_id': '5e02.4001.8000',
                        'partner_port': 'GigabitEthernet0/2',
                        'age': 16,
                        'flags': 'SC',
                        'group_cap': 10001,
                    },
                },
            },
            'Port-channel2': {
                'name': 'Port-channel2',
                'protocol': 'pagp',
                'members': {
                    'GigabitEthernet0/3': {
                        'interface': 'GigabitEthernet0/3',
                        'partner_name': 'iosvl2-2',
                        'partner_id': '5e02.4001.8000',
                        'partner_port': 'GigabitEthernet0/3',
                        'age': 18,
                        'flags': 'SC',
                        'group_cap': 20001,
                    },
                    'GigabitEthernet1/0': {
                        'interface': 'GigabitEthernet1/0',
                        'partner_name': 'iosvl2-2',
                        'partner_id': '5e02.4001.8000',
                        'partner_port': 'GigabitEthernet1/0',
                        'age': 25,
                        'flags': 'SC',
                        'group_cap': 20001,
                    },
                    'GigabitEthernet1/1': {
                        'interface': 'GigabitEthernet1/1',
                        'partner_name': 'iosvl2-2',
                        'partner_id': '5e02.4001.8000',
                        'partner_port': 'GigabitEthernet1/1',
                        'age': 0,
                        'flags': 'SC',
                        'group_cap': 20001,
                    },
                },
            },
        }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowPagpNeighbor(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowPagpNeighbor(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)
###################################################
# unit test for show pagp counters
####################################################
class test_show_pagp_counters(unittest.TestCase):
    """unit test for show pagp counters"""

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
    iosvl2-1#show pagp counters
          Information         Flush        PAgP
    Port      Sent    Recv     Sent    Recv    Err Pkts
    ---------------------------------------------------
    Channel group: 1
    Gi0/1     60      52       0       0       0
    Gi0/2     59      52       0       0       0

              Information         Flush        PAgP
    Port      Sent    Recv     Sent    Recv    Err Pkts
    ---------------------------------------------------
    Channel group: 2
    Gi0/3     21      11       0       0       0
    Gi1/0     19      11       0       0       0
    Gi1/1     19      10       0       0       0
    '''}

    golden_parsed_output = {
        'interfaces': {
            'Port-channel1': {
                'name': 'Port-channel1',
                'protocol': 'pagp',
                'members': {
                    'GigabitEthernet0/1': {
                        'interface': 'GigabitEthernet0/1',
                        'counters': {
                            'information_in_pkts': 52,
                            'information_out_pkts': 60,
                            'pagp_errors': 0,
                            'flush_in_pkts': 0,
                            'flush_out_pkts': 0,
                            },
                        },
                    'GigabitEthernet0/2': {
                        'interface': 'GigabitEthernet0/2',
                        'counters': {
                            'information_in_pkts': 52,
                            'information_out_pkts': 59,
                            'pagp_errors': 0,
                            'flush_in_pkts': 0,
                            'flush_out_pkts': 0,
                        },
                    },
                },
            },
            'Port-channel2': {
                'name': 'Port-channel2',
                'protocol': 'pagp',
                'members': {
                    'GigabitEthernet0/3': {
                        'interface': 'GigabitEthernet0/3',
                        'counters': {
                            'information_in_pkts': 11,
                            'information_out_pkts': 21,
                            'pagp_errors': 0,
                            'flush_in_pkts': 0,
                            'flush_out_pkts': 0,
                        },
                    },
                    'GigabitEthernet1/0': {
                        'interface': 'GigabitEthernet1/0',
                        'counters': {
                            'information_in_pkts': 11,
                            'information_out_pkts': 19,
                            'pagp_errors': 0,
                            'flush_in_pkts': 0,
                            'flush_out_pkts': 0,
                        },
                    },
                    'GigabitEthernet1/1': {
                        'interface': 'GigabitEthernet1/1',
                        'counters': {
                            'information_in_pkts': 10,
                            'information_out_pkts': 19,
                            'pagp_errors': 0,
                            'flush_in_pkts': 0,
                            'flush_out_pkts': 0,
                        },
                    },

                },
            },
        }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowPagpCounters(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowPagpCounters(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

###################################################
# unit test for show pagp internal
####################################################
class test_show_pagp_internal(unittest.TestCase):
    """unit test for show pagp internal"""

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
    iosvl2-1#show pagp internal
    Flags:  S - Device is sending Slow hello.  C - Device is in Consistent state.
            A - Device is in Auto mode.        d - PAgP is down
    Timers: H - Hello timer is running.        Q - Quit timer is running.
            S - Switching timer is running.    I - Interface timer is running.

    Channel group 1
                                    Hello    Partner  PAgP     Learning  Group
    Port      Flags State   Timers  Interval Count   Priority   Method  Ifindex
    Gi0/1     SC    U6/S7   H       30s      1        128        Any      8
    Gi0/2     SC    U6/S7   H       30s      1        128        Any      8

    Channel group 2
                                    Hello    Partner  PAgP     Learning  Group
    Port      Flags State   Timers  Interval Count   Priority   Method  Ifindex
    Gi0/3     SC    U6/S7   H       30s      1        128        Any      11
    Gi1/0     SC    U6/S7   H       30s      1        128        Any      11
    Gi1/1     SC    U6/S7   H       30s      1        128        Any      11
        '''}

    golden_parsed_output = {
        'interfaces': {
            'Port-channel1': {
                'name': 'Port-channel1',
                'protocol': 'pagp',
                'members': {
                    'GigabitEthernet0/1': {
                        'interface': 'GigabitEthernet0/1',
                        'group_ifindex': 8,
                        'partner_count': 1,
                        'hello_interval': 30,
                        'timers': 'H',
                        'pagp_port_priority': 128,
                        'flags': 'SC',
                        'state': 'U6/S7',
                        'learn_method': 'any',
                    },
                    'GigabitEthernet0/2': {
                        'interface': 'GigabitEthernet0/2',
                        'group_ifindex': 8,
                        'partner_count': 1,
                        'hello_interval': 30,
                        'timers': 'H',
                        'pagp_port_priority': 128,
                        'flags': 'SC',
                        'state': 'U6/S7',
                        'learn_method': 'any',
                    },
                },
            },
            'Port-channel2': {
                'name': 'Port-channel2',
                'protocol': 'pagp',
                'members': {
                    'GigabitEthernet0/3': {
                        'interface': 'GigabitEthernet0/3',
                        'group_ifindex': 11,
                        'partner_count': 1,
                        'hello_interval': 30,
                        'timers': 'H',
                        'pagp_port_priority': 128,
                        'flags': 'SC',
                        'state': 'U6/S7',
                        'learn_method': 'any',
                    },
                    'GigabitEthernet1/0': {
                        'interface': 'GigabitEthernet1/0',
                        'group_ifindex': 11,
                        'partner_count': 1,
                        'hello_interval': 30,
                        'timers': 'H',
                        'pagp_port_priority': 128,
                        'flags': 'SC',
                        'state': 'U6/S7',
                        'learn_method': 'any',
                    },
                    'GigabitEthernet1/1': {
                        'interface': 'GigabitEthernet1/1',
                        'group_ifindex': 11,
                        'partner_count': 1,
                        'hello_interval': 30,
                        'timers': 'H',
                        'pagp_port_priority': 128,
                        'flags': 'SC',
                        'state': 'U6/S7',
                        'learn_method': 'any',
                    },
                },
            },
        }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowPagpInternal(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowPagpInternal(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


###################################################
# unit test for show etherchannel summary
####################################################
class test_show_etherchannel_summary(unittest.TestCase):
    """unit test for show etherchannel summary """

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
csr1000v-1#show etherchannel summary
Flags:  D - down        P/bndl - bundled in port-channel
        I - stand-alone s/susp - suspended
        H - Hot-standby (LACP only)
        R - Layer3      S - Layer2
        U - in use      f - failed to allocate aggregator

        M - not in use, minimum links not met
        u - unsuitable for bundling
        w - waiting to be aggregated
        d - default port


Number of channel-groups in use: 2
Number of aggregators:           2

Group  Port-channel  Protocol    Ports
------+-------------+-----------+-----------------------------------------------
1	Po1(RU)		LACP	 Gi2(bndl) Gi3(bndl)
2	Po2(RU)		LACP	 Gi4(bndl) Gi5(hot-sby) Gi6(bndl)


RU - L3 port-channel UP State
SU - L2 port-channel UP state
P/bndl -  Bundled
S/susp  - Suspended
    '''}

    golden_parsed_output = {
        'number_of_lag_in_use': 2,
        'number_of_aggregators': 2,
        'interfaces': {
            'Port-channel1': {
                'name': 'Port-channel1',
                'bundle_id': 1,
                'protocol': 'lacp',
                'flags': 'RU',
                'oper_status': 'up',
                'members': {
                    'GigabitEthernet2': {
                        'interface': 'GigabitEthernet2',
                        'flags': 'bndl',
                        'bundled': True,
                        },
                    'GigabitEthernet3': {
                        'interface': 'GigabitEthernet3',
                        'flags': 'bndl',
                        'bundled': True,
                       },
                    },
                },
            'Port-channel2': {
                'name': 'Port-channel2',
                'bundle_id': 2,
                'protocol': 'lacp',
                'flags': 'RU',
                'oper_status': 'up',
                'members': {
                    'GigabitEthernet4': {
                        'interface': 'GigabitEthernet4',
                        'flags': 'bndl',
                        'bundled': True,
                    },
                    'GigabitEthernet5': {
                        'interface': 'GigabitEthernet5',
                        'flags': 'hot-sby',
                        'bundled': False,
                    },
                    'GigabitEthernet6': {
                        'interface': 'GigabitEthernet6',
                        'flags': 'bndl',
                        'bundled': True,
                    },
                },
            },
        },
    }

    golden_output_1 = {'execute.return_value': '''
        csr1000v-1#show etherchannel summary
        Flags:  D - down        P/bndl - bundled in port-channel
                I - stand-alone s/susp - suspended
                H - Hot-standby (LACP only)
                R - Layer3      S - Layer2
                U - in use      f - failed to allocate aggregator

                M - not in use, minimum links not met
                u - unsuitable for bundling
                w - waiting to be aggregated
                d - default port


        Number of channel-groups in use: 1
        Number of aggregators:           1

        Group  Port-channel  Protocol    Ports
        ------+-------------+-----------+-----------------------------------------------
        2	Po2(RU)		-
        '''}

    golden_parsed_output_1 = {
        'number_of_lag_in_use': 1,
        'number_of_aggregators': 1,
        'interfaces': {
            'Port-channel2': {
                'name': 'Port-channel2',
                'bundle_id': 2,
                'flags': 'RU',
                'oper_status': 'up',
            },
        },
    }
    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowEtherchannelSummary(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowEtherchannelSummary(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowEtherchannelSummary(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_1)

if __name__ == '__main__':
    unittest.main()