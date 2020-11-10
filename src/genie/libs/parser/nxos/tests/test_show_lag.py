# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device
from pyats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
    SchemaMissingKeyError

# iosxe show_lisp
from genie.libs.parser.nxos.show_lag import ShowLacpSystemIdentifier, \
    ShowLacpCounters, ShowLacpNeighbor, ShowPortChannelSummary, ShowPortChannelDatabase

# =================================
# Unit test for 'show lacp system-identifier'
# =================================
class test_show_system_identifier(unittest.TestCase):
    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {
        'system_id_mac': '5e-2-0-1-0-7',
        'system_priority': 32768,
    }
    golden_output = {'execute.return_value': '''
    32768,5e-2-0-1-0-7
    '''}


    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowLacpSystemIdentifier(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowLacpSystemIdentifier(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


# =================================
# Unit test for 'show lacp counters'
# =================================
class test_show_lacp_counters(unittest.TestCase):
    """unit test for show lacp counters """

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        "interfaces": {
            "Port-channel1": {
                "members": {
                    "Ethernet1/1": {
                        "interface": "Ethernet1/1",
                        "counters": {
                            "lacp_in_pkts": 85,
                            "lacp_out_pkts": 92,
                            "marker_resp_in_pkts": 0,
                            "marker_resp_out_pkts": 0,
                            "lacp_errors": 0
                        }
                    },
                    "Ethernet1/2": {
                        "interface": "Ethernet1/2",
                        "counters": {
                            "lacp_in_pkts": 87,
                            "lacp_out_pkts": 79,
                            "marker_resp_in_pkts": 0,
                            "marker_resp_out_pkts": 0,
                            "lacp_errors": 0,
                        }
                    }
                }
            },
            "Port-channel2": {
                "members": {
                    "Ethernet1/3": {
                        "interface": "Ethernet1/3",
                        "counters": {
                            "lacp_in_pkts": 112,
                            "lacp_out_pkts": 136,
                            "marker_resp_in_pkts": 0,
                            "marker_resp_out_pkts": 0,
                            "lacp_errors": 0,
                        }
                    },
                    "Ethernet1/4": {
                        "interface": "Ethernet1/4",
                        "counters": {
                            "lacp_in_pkts": 90,
                            "lacp_out_pkts": 95,
                            "marker_resp_in_pkts": 0,
                            "marker_resp_out_pkts": 0,
                            "lacp_errors": 0,
                        }
                    },
                    "Ethernet1/5": {
                        "interface": "Ethernet1/5",
                        "counters": {
                            "lacp_in_pkts": 146,
                            "lacp_out_pkts": 118,
                            "marker_resp_in_pkts": 0,
                            "marker_resp_out_pkts": 0,
                            "lacp_errors": 0,
                        }
                    }
                }
            }
        }
    }
    golden_output = {'execute.return_value': '''
        NOTE: Clear lacp counters to get accurate statistics
    
        ------------------------------------------------------------------------------
                                     LACPDUs                      Markers/Resp LACPDUs
        Port              Sent                Recv                  Recv Sent  Pkts Err
        ------------------------------------------------------------------------------
        port-channel1
        Ethernet1/1        92                   85                     0      0    0      
        Ethernet1/2        79                   87                     0      0    0      
        
        port-channel2
        Ethernet1/3        136                  112                    0      0    0      
        Ethernet1/4        95                   90                     0      0    0      
        Ethernet1/5        118                  146                    0      0    0  
    '''}



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
        self.assertDictEqual(parsed_output, self.golden_parsed_output)


# =================================
# Unit test for 'show lacp neighbors'
# =================================
class test_show_lacp_neighbors(unittest.TestCase):
    """unit test for show lacp counters """

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {
        'interfaces': {
            'Port-channel1': {
                'members': {
                    'Ethernet1/1': {
                        'interface': 'Ethernet1/1',
                        'activity': 'active',
                        'oper_key': 0x8000,
                        'port_num': 0x101,
                        'partner_id': '5e-2-0-1-0-7',
                        'age': 1140,
                        'interval': 'slow',
                        'lacp_port_priority': 32768,
                        'port_state': 0x3d,
                    },
                    'Ethernet1/2': {
                        'interface': 'Ethernet1/2',
                        'activity': 'active',
                        'oper_key': 0x8000,
                        'port_num': 0x102,
                        'partner_id': '5e-2-0-1-0-7',
                        'age': 1140,
                        'interval': 'slow',
                        'lacp_port_priority': 32768,
                        'port_state': 0x3d,
                    },
                }
            },
            'Port-channel2': {
                'members': {
                    'Ethernet1/3': {
                        'interface': 'Ethernet1/3',
                        'activity': 'active',
                        'oper_key': 0x1,
                        'port_num': 0x103,
                        'partner_id': '5e-2-0-1-0-7',
                        'age': 625,
                        'interval': 'slow',
                        'lacp_port_priority': 32768,
                        'port_state': 0x3d,
                    },
                    'Ethernet1/4': {
                        'interface': 'Ethernet1/4',
                        'activity': 'active',
                        'oper_key': 0x1,
                        'port_num': 0x104,
                        'partner_id': '5e-2-0-1-0-7',
                        'age': 638,
                        'interval': 'slow',
                        'lacp_port_priority': 32768,
                        'port_state': 0x3d,
                    },
                    'Ethernet1/5': {
                        'interface': 'Ethernet1/5',
                        'activity': 'active',
                        'oper_key': 0x1,
                        'port_num': 0x105,
                        'partner_id': '5e-2-0-1-0-7',
                        'age': 834,
                        'interval': 'slow',
                        'lacp_port_priority': 32768,
                        'port_state': 0xd,
                    }
                }
            }
        }
    }
    golden_output = {'execute.return_value': '''
Flags:  S - Device is sending Slow LACPDUs F - Device is sending Fast LACPDUs
        A - Device is in Active mode       P - Device is in Passive mode
port-channel1 neighbors
Partner's information
            Partner                Partner                     Partner
Port        System ID              Port Number     Age         Flags
Eth1/1      32768,5e-2-0-1-0-7     0x101           1140        SA

            LACP Partner           Partner                     Partner
            Port Priority          Oper Key                    Port State
            32768                  0x8000                      0x3d

Partner's information
            Partner                Partner                     Partner
Port        System ID              Port Number     Age         Flags
Eth1/2      32768,5e-2-0-1-0-7     0x102           1140        SA

            LACP Partner           Partner                     Partner
            Port Priority          Oper Key                    Port State
            32768                  0x8000                      0x3d


Po2 neighbors
Partner's information
            Partner                Partner                     Partner
Port        System ID              Port Number     Age         Flags
Eth1/3      32768,5e-2-0-1-0-7     0x103           625         SA

            LACP Partner           Partner                     Partner
            Port Priority          Oper Key                    Port State
            32768                  0x1                         0x3d

Partner's information
            Partner                Partner                     Partner
Port        System ID              Port Number     Age         Flags
Eth1/4      32768,5e-2-0-1-0-7     0x104           638         SA

            LACP Partner           Partner                     Partner
            Port Priority          Oper Key                    Port State
            32768                  0x1                         0x3d

Partner's information
            Partner                Partner                     Partner
Port        System ID              Port Number     Age         Flags
Eth1/5      32768,5e-2-0-1-0-7     0x105           834         SA

            LACP Partner           Partner                     Partner
            Port Priority          Oper Key                    Port State
            32768                  0x1                         0xd
'''}


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
        self.assertDictEqual(parsed_output, self.golden_parsed_output)


# =================================
# Unit test for 'show port-channel summary'
# =================================
class test_show_port_channel_summary(unittest.TestCase):
    """unittest for show port-channel summary"""
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {
        'interfaces': {
            'Port-channel1': {
                'bundle_id': 1,
                'oper_status': 'up',
                'layer': 'routed',
                'protocol': 'lacp',
                'type': 'eth',
                'members': {
                    'Ethernet1/1': {
                        'flags': 'P',
                    },
                    'Ethernet1/2': {
                        'flags': 'P'
                    }
                },
            },
            'Port-channel2': {
                'bundle_id': 2,
                'oper_status': 'up',
                'layer': 'switched',
                'protocol': 'lacp',
                'type': 'eth',
                'members': {
                    'Ethernet1/3': {
                        'flags': 'P',
                    },
                    'Ethernet1/4': {
                        'flags': 'P'
                    },
                    'Ethernet1/5': {
                        'flags': 'H'
                    }
                },

            }
        }
    }
    golden_output = {'execute.return_value': '''
Flags:  D - Down        P - Up in port-channel (members)
        I - Individual  H - Hot-standby (LACP only)
        s - Suspended   r - Module-removed
        b - BFD Session Wait
        S - Switched    R - Routed
        U - Up (port-channel)
        p - Up in delay-lacp mode (member)
        M - Not in use. Min-links not met
--------------------------------------------------------------------------------
Group Port-       Type     Protocol  Member Ports
      Channel
--------------------------------------------------------------------------------
1     Po1(RU)     Eth      LACP      Eth1/1(P)    Eth1/2(P)
2     Po2(SU)     Eth      LACP      Eth1/3(P)    Eth1/4(P)    Eth1/5(H)
'''}
    golden_parsed_output_1 = {
        'interfaces': {
            'Port-channel1': {'bundle_id': 1,
                              'layer': 'switched',
                              'members': {'Ethernet1/42': {'flags': 'D'},
                                          'Ethernet1/43': {'flags': 'D'},
                                          'Ethernet1/45': {'flags': 'P'},
                                          'Ethernet1/46': {'flags': 'P'},
                                          'Ethernet1/47': {'flags': 'D'},
                                          'Ethernet1/48': {'flags': 'P'}},
                              'oper_status': 'up',
                              'protocol': 'lacp',
                              'type': 'eth'},
            'Port-channel2': {'bundle_id': 2,
                              'layer': 'switched',
                              'members': {'Ethernet1/50': {'flags': 'P'},
                                          'Ethernet1/51': {'flags': 'P'}},
                              'oper_status': 'up',
                              'protocol': 'lacp',
                              'type': 'eth'}}}

    golden_output_1 = {'execute.return_value': '''
Flags:  D - Down        P - Up in port-channel (members)
        I - Individual  H - Hot-standby (LACP only)
        s - Suspended   r - Module-removed
        S - Switched    R - Routed
        U - Up (port-channel)
        M - Not in use. Min-links not met
--------------------------------------------------------------------------------
Group Port-       Type     Protocol  Member Ports
      Channel
--------------------------------------------------------------------------------
1     Po1(SU)     Eth      LACP      Eth1/42(D)   Eth1/43(D)   Eth1/45(P)
                                     Eth1/46(P)   Eth1/47(D)   Eth1/48(P)
2     Po2(SU)     Eth      LACP      Eth1/50(P)   Eth1/51(P)

'''}



    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowPortChannelSummary(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowPortChannelSummary(device=self.device)
        parsed_output = obj.parse()

        self.assertDictEqual(parsed_output, self.golden_parsed_output)

        self.device = Mock(**self.golden_output_1)
        obj = ShowPortChannelSummary(device=self.device)
        parsed_output = obj.parse()
        self.assertDictEqual(parsed_output, self.golden_parsed_output_1)



# =================================
# Unit test for 'show port-channel database'
# =================================
class test_show_port_channel_database(unittest.TestCase):
    """unittest for show port-channel database"""
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output = {
        'interfaces': {
            'Port-channel1': {
                'last_update_success': True,
                'total_ports': 2,
                'up_ports': 2,
                'first_oper_port': 'Ethernet1/1',
                'port_channel_age': '0d:02h:31m:22s',
                'time_last_bundle': '0d:02h:28m:30s',
                'last_bundled_member': 'Ethernet1/2',
                'members': {
                    'Ethernet1/1': {
                        'activity': 'active',
                        'status': 'up',
                        'is_first_oper_port': True
                    },
                    'Ethernet1/2': {
                        'activity': 'active',
                        'status': 'up',
                        'is_first_oper_port': False
                    }
                }

            },
            'Port-channel2': {
                'last_update_success': True,
                'total_ports': 3,
                'up_ports': 2,
                'first_oper_port': 'Ethernet1/4',
                'port_channel_age': '0d:02h:27m:37s',
                'time_last_bundle': '0d:00h:12m:50s',
                'last_bundled_member': 'Ethernet1/5',
                'time_last_unbundle': '0d:00h:14m:05s',
                'last_unbundled_member': 'Ethernet1/5',
                'members': {
                    'Ethernet1/3': {
                        'activity': 'passive',
                        'status': 'up',
                        'is_first_oper_port': False
                    },
                    'Ethernet1/4': {
                        'activity': 'passive',
                        'status': 'up',
                        'is_first_oper_port': True
                    },
                    'Ethernet1/5': {
                        'activity': 'passive',
                        'status': 'hot-standy',
                        'is_first_oper_port': False
                    }
                }

            }

        }
    }
    golden_output = {'execute.return_value': '''
port-channel1
    Last membership update is successful
    2 ports in total, 2 ports up
    First operational port is Ethernet1/1
    Age of the port-channel is 0d:02h:31m:22s
    Time since last bundle is 0d:02h:28m:30s
    Last bundled member is Ethernet1/2
    Ports:   Ethernet1/1     [active ] [up] *
             Ethernet1/2     [active ] [up]

port-channel2
    Last membership update is successful
    3 ports in total, 2 ports up
    First operational port is Ethernet1/4
    Age of the port-channel is 0d:02h:27m:37s
    Time since last bundle is 0d:00h:12m:50s
    Last bundled member is Ethernet1/5
    Time since last unbundle is 0d:00h:14m:05s
    Last unbundled member is Ethernet1/5
    Ports:   Ethernet1/3     [passive] [up]
             Ethernet1/4     [passive] [up] *
             Ethernet1/5     [passive] [hot-standy]
'''}




    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowPortChannelDatabase(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowPortChannelDatabase(device=self.device)
        parsed_output = obj.parse()
        self.assertDictEqual(parsed_output, self.golden_parsed_output)


if __name__ == '__main__':
    unittest.main()
