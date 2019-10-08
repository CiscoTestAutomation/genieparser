#!/bin/env python
import unittest
from unittest.mock import Mock
from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                       SchemaMissingKeyError
from genie.libs.parser.iosxe.show_lag import ShowLacpSysId,\
                                  ShowEtherchannelSummary,\
                                  ShowLacpCounters,\
                                  ShowLacpInternal,\
                                  ShowLacpNeighbor,\
                                  ShowPagpCounters, \
                                  ShowPagpNeighbor,\
                                  ShowPagpInternal,\
                                  ShowEtherChannelLoadBalancing,\
                                  ShowLacpNeighborDetail


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
        "interfaces": {
            "Port-channel1": {
                "name": "Port-channel1",
                "protocol": "lacp",
                "members": {
                    "GigabitEthernet2": {
                        "interface": "GigabitEthernet2",
                        "counters": {
                            "lacp_in_pkts": 22,
                            "lacp_out_pkts": 27,
                            "marker_in_pkts": 0,
                            "marker_out_pkts": 0,
                            "lacp_pkts": 0,
                            "marker_response_in_pkts": 0,
                            "marker_response_out_pkts": 0
                        }
                    },
                    "GigabitEthernet3": {
                        "interface": "GigabitEthernet3",
                        "counters": {
                            "lacp_in_pkts": 21,
                            "lacp_out_pkts": 24,
                            "marker_in_pkts": 0,
                            "marker_out_pkts": 0,
                            "lacp_pkts": 0,
                            "marker_response_in_pkts": 0,
                            "marker_response_out_pkts": 0
                        }
                    }
                }
            },
            "Port-channel2": {
                "name": "Port-channel2",
                "protocol": "lacp",
                "members": {
                    "GigabitEthernet4": {
                        "interface": "GigabitEthernet4",
                        "counters": {
                            "lacp_in_pkts": 31,
                            "lacp_out_pkts": 24,
                            "marker_in_pkts": 0,
                            "marker_out_pkts": 0,
                            "lacp_pkts": 0,
                            "marker_response_in_pkts": 0,
                            "marker_response_out_pkts": 0
                        }
                    },
                    "GigabitEthernet5": {
                        "interface": "GigabitEthernet5",
                        "counters": {
                            "lacp_in_pkts": 10,
                            "lacp_out_pkts": 14,
                            "marker_in_pkts": 0,
                            "marker_out_pkts": 0,
                            "lacp_pkts": 0,
                            "marker_response_in_pkts": 0,
                            "marker_response_out_pkts": 0
                        }
                    },
                    "GigabitEthernet6": {
                        "interface": "GigabitEthernet6",
                        "counters": {
                            "lacp_in_pkts": 11,
                            "lacp_out_pkts": 13,
                            "marker_in_pkts": 0,
                            "marker_out_pkts": 0,
                            "lacp_pkts": 0,
                            "marker_response_in_pkts": 0,
                            "marker_response_out_pkts": 0
                        }
                    }
                }
            }
        }
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

        Channel group 14 neighbors
                 Partner              Partner          Partner         Partner Group
        Port      Name                 Device ID        Port       Age  Flags   Cap.
        Gi1/0/7   R4                   ecbd.1d09.5680	Gi1/0/7     22s SC	E0001
        Gi1/0/8   R4                   ecbd.1d09.5680	Gi1/0/8     16s SC	E0001
        Gi1/0/9   R4                   ecbd.1d09.5680	Gi1/0/9     18s SC	E0001
    '''
    }

    golden_parsed_output = {
        "interfaces": {
            "Port-channel14": {
                "members": {
                    "GigabitEthernet1/0/7": {
                        "age": 22,
                        "flags": "SC",
                        "group_cap": "E0001",
                        "interface": "GigabitEthernet1/0/7",
                        "partner_id": "ecbd.1d09.5680",
                        "partner_name": "R4",
                        "partner_port": "GigabitEthernet1/0/7"
                    },
                    "GigabitEthernet1/0/8": {
                        "age": 16,
                        "flags": "SC",
                        "group_cap": "E0001",
                        "interface": "GigabitEthernet1/0/8",
                        "partner_id": "ecbd.1d09.5680",
                        "partner_name": "R4",
                        "partner_port": "GigabitEthernet1/0/8"
                    },
                    "GigabitEthernet1/0/9": {
                        "age": 18,
                        "flags": "SC",
                        "group_cap": "E0001",
                        "interface": "GigabitEthernet1/0/9",
                        "partner_id": "ecbd.1d09.5680",
                        "partner_name": "R4",
                        "partner_port": "GigabitEthernet1/0/9"
                    }
                },
                "name": "Port-channel14",
                "protocol": "pagp"
            }
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
    Gi1/0     S C    U6/S7   H       30s      1        128        Any      11
    Gi1/1     S C    U6/S7   H       30s      1        128        Any      11
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
                        'flags': 'S C',
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
                        'flags': 'S C',
                        'state': 'U6/S7',
                        'learn_method': 'any',
                    },
                },
            },
        }
    }

    golden_output_2 = {'execute.return_value': '''
    +++ R1: executing command 'show pagp internal' +++
    show pagp internal
    Flags:  S - Device is sending Slow hello.  C - Device is in Consistent state.
            A - Device is in Auto mode.        d - PAgP is down
    Timers: H - Hello timer is running.        Q - Quit timer is running.
            S - Switching timer is running.    I - Interface timer is running.

    Channel group 14
                                      Hello    Partner  PAgP       Learning  Group
    Port        Flags State   Timers  Interval Count    Priority   Method    Ifindex
    Gi1/0/7     d     U1/S1           1s       0        128        Any       0
    Gi1/0/8     d     U1/S1           1s       0        128        Any       0
    Gi1/0/9     d     U1/S1           1s       0        128        Any       0
    R1#
    '''}

    golden_parsed_output_2 = {
    'interfaces': {
        'Port-channel14': {
            'members': {
                'GigabitEthernet1/0/7': {
                    'interface': 'GigabitEthernet1/0/7',
                    'partner_count': 0,
                    'hello_interval': 1,
                    'learn_method': 'any',
                    'state': 'U1/S1',
                    'pagp_port_priority': 128,
                    'flags': 'd',
                    'group_ifindex': 0,
                    },
                'GigabitEthernet1/0/9': {
                    'interface': 'GigabitEthernet1/0/9',
                    'partner_count': 0,
                    'hello_interval': 1,
                    'learn_method': 'any',
                    'state': 'U1/S1',
                    'pagp_port_priority': 128,
                    'flags': 'd',
                    'group_ifindex': 0,
                    },
                'GigabitEthernet1/0/8': {
                    'interface': 'GigabitEthernet1/0/8',
                    'partner_count': 0,
                    'hello_interval': 1,
                    'learn_method': 'any',
                    'state': 'U1/S1',
                    'pagp_port_priority': 128,
                    'flags': 'd',
                    'group_ifindex': 0,
                    },
                },
            'name': 'Port-channel14',
            'protocol': 'pagp',
            },
        },
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

    def test_golden_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        obj = ShowPagpInternal(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_2)


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
    '''
    }

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
                        'port_channel': {
                           "port_channel_member": True,
                           "port_channel_int": "Port-channel1"
                        },
                        },
                    'GigabitEthernet3': {
                        'interface': 'GigabitEthernet3',
                        'flags': 'bndl',
                        'bundled': True,
                        'port_channel': {
                           "port_channel_member": True,
                           "port_channel_int": "Port-channel1"
                        },
                    },
                },
                'port_channel': {
                    'port_channel_member': True,
                    'port_channel_member_intfs': ['GigabitEthernet2', 'GigabitEthernet3'],
                }
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
                        'port_channel': {
                           "port_channel_member": True,
                           "port_channel_int": "Port-channel2"
                        },
                    },
                    'GigabitEthernet5': {
                        'interface': 'GigabitEthernet5',
                        'flags': 'hot-sby',
                        'bundled': False,
                        'port_channel': {
                           "port_channel_member": True,
                           "port_channel_int": "Port-channel2"
                        },
                    },
                    'GigabitEthernet6': {
                        'interface': 'GigabitEthernet6',
                        'flags': 'bndl',
                        'bundled': True,
                        'port_channel': {
                           "port_channel_member": True,
                           "port_channel_int": "Port-channel2"
                        },
                    },
                },
                'port_channel': {
                    'port_channel_member': True,
                    'port_channel_member_intfs': ['GigabitEthernet4', 'GigabitEthernet5', 'GigabitEthernet6'],
                }
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

    golden_output_2 = {'execute.return_value': '''
        show etherchannel summary
        Flags:  D - down        P - bundled in port-channel
                I - stand-alone s - suspended
                H - Hot-standby (LACP only)
                R - Layer3      S - Layer2
                U - in use      f - failed to allocate aggregator

                M - not in use, minimum links not met
                u - unsuitable for bundling
                w - waiting to be aggregated
                d - default port

                A - formed by Auto LAG


        Number of channel-groups in use: 1
        Number of aggregators:           1

        Group  Port-channel  Protocol    Ports
        ------+-------------+-----------+-----------------------------------------------
        10     Po10(SU)        PAgP        Gi1/0/15(P)     Gi1/0/16(P)     
                                           Gi1/0/17(P)     
        '''}

    golden_parsed_output_2 = {
        'number_of_aggregators': 1,
        'interfaces': {
            'Port-channel10': {
                'name': 'Port-channel10',
                'protocol': 'pagp',
                'members': {
                    'GigabitEthernet1/0/16': {
                        'interface': 'GigabitEthernet1/0/16',
                        'flags': 'P',
                        'bundled': True,
                        'port_channel': {
                            'port_channel_int': 'Port-channel10',
                            'port_channel_member': True,
                            },
                        },
                    'GigabitEthernet1/0/15': {
                        'interface': 'GigabitEthernet1/0/15',
                        'flags': 'P',
                        'bundled': True,
                        'port_channel': {
                            'port_channel_int': 'Port-channel10',
                            'port_channel_member': True,
                            },
                        },
                    'GigabitEthernet1/0/17': {
                        'interface': 'GigabitEthernet1/0/17',
                        'flags': 'P',
                        'bundled': True,
                        'port_channel': {
                            'port_channel_int': 'Port-channel10',
                            'port_channel_member': True,
                            },
                        },
                    },
                'oper_status': 'up',
                'bundle_id': 10,
                'port_channel': {
                    'port_channel_member_intfs': ['GigabitEthernet1/0/15', 'GigabitEthernet1/0/16', 'GigabitEthernet1/0/17'],
                    'port_channel_member': True,
                    },
                'flags': 'SU',
                },
            },
        'number_of_lag_in_use': 1,
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

    def test_golden_3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        obj = ShowEtherchannelSummary(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_2)

###################################################
# unit test for show etherchannel load-balancing
####################################################
class test_show_etherchannel_loadbalancing(unittest.TestCase):
    """unit test for show etherchannel load-balancing """

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'global_lb_method': 'flow-based',
        'lb_algo_type': 'Source Destination IP',
        'port_channel': {
            'Port-channel1': {
                'lb_method': 'flow-based (Source Destination IP)'
            }
        }
    }
    golden_output = {'execute.return_value': '''
        Router#sh etherchannel load-balancing
        Load for five secs: 50%/2%; one minute: 38%; five minutes: 56%
        Time source is NTP, *16:28:54.625 EST Sat Nov 12 2016
        EtherChannel Load-Balancing Method: 
        Global LB Method: flow-based
        LB Algo type: Source Destination IP

          Port-Channel:                       LB Method
            Port-channel1                   :  flow-based (Source Destination IP)
    '''}

    golden_parsed_output1 = {
        'global_lb_method': 'flow-based',
        'lb_algo_type': 'Source Destination IP',
    }
    golden_output1 = {'execute.return_value': '''
        P3#show etherchannel load-balancing
        Load for five secs: 3%/0%; one minute: 4%; five minutes: 2%
        No time source, *15:30:14.148 UTC Sat Jan 31 1970
        EtherChannel Load-Balancing Method: 
        Global LB Method: flow-based
        LB Algo type: Source Destination IP

          Port-Channel:                       LB Method

    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowEtherChannelLoadBalancing(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowEtherChannelLoadBalancing(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)
    
    def test_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowEtherChannelLoadBalancing(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output1)


###################################################
# unit test for show lacp neighbor detail
####################################################
class test_show_lacp_neighbor_detail(unittest.TestCase):
    """unit test for show lacp neighbor detail"""

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        Router#show lacp neighbor detail
        Load for five secs: 5%/1%; one minute: 6%; five minutes: 7%
        Time source is NTP, 20:56:57.454 EST Fri Nov 11 2016

        Flags:  S - Device is requesting Slow LACPDUs 
                F - Device is requesting Fast LACPDUs
                A - Device is in Active mode       P - Device is in Passive mode     

        Channel group 1 neighbors

        Partner's information:

                  Partner               Partner                     Partner
        Port           System ID             Port Number     Age         Flags
        Gi0/0/1         00127,6487.88af.b840  0x2              18s        FA

                  LACP Partner         Partner         Partner
                  Port Priority        Oper Key        Port State
                  100                  0x1             0x3F

                  Port State Flags Decode:
                  Activity:   Timeout:   Aggregation:   Synchronization:
                  Active      Short      Yes            Yes

                  Collecting:   Distributing:   Defaulted:   Expired:
                  Yes           Yes             No           No 
                  Partner               Partner                     Partner
        Port           System ID             Port Number     Age         Flags
        Gi0/0/7         00127,6487.88af.b840  0x1               0s        FA

                  LACP Partner         Partner         Partner
                  Port Priority        Oper Key        Port State
                  200                  0x1             0xF 

                  Port State Flags Decode:
                  Activity:   Timeout:   Aggregation:   Synchronization:
                  Active      Short      Yes            Yes

                  Collecting:   Distributing:   Defaulted:   Expired:
                  No            No              No           No 
        '''}

    golden_parsed_output = {
        'interfaces': {
            'Port-channel1': {
                'name': 'Port-channel1',
                'protocol': 'lacp',
                'members': {
                    'GigabitEthernet0/0/1': {
                        'activity': 'Active',
                        'age': 18,
                        'aggregatable': True,
                        'collecting': True,
                        'defaulted': False,
                        'distributing': True,
                        'expired': False,
                        'flags': 'FA',
                        'interface': 'GigabitEthernet0/0/1',
                        'lacp_port_priority': 100,
                        'oper_key': 1,
                        'port_num': 2,
                        'port_state': 63,
                        'synchronization': True,
                        'system_id': '00127,6487.88af.b840',
                        'timeout': 'Short'
                    },
                    'GigabitEthernet0/0/7': {
                        'activity': 'Active',
                        'age': 0,
                        'aggregatable': True,
                        'collecting': False,
                        'defaulted': False,
                        'distributing': False,
                        'expired': False,
                        'flags': 'FA',
                        'interface': 'GigabitEthernet0/0/7',
                        'lacp_port_priority': 200,
                        'oper_key': 1,
                        'port_num': 1,
                        'port_state': 15,
                        'synchronization': True,
                        'system_id': '00127,6487.88af.b840',
                        'timeout': 'Short'
                    }
                },
            }
        }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowLacpNeighborDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowLacpNeighborDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == '__main__':
    unittest.main()