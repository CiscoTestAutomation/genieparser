#!/bin/env python
import unittest
from unittest.mock import Mock
from ats.topology import Device

import genie.gre
from genie.metaparser.util.exceptions import (SchemaMissingKeyError,
                                              SchemaEmptyParserError)

from genie.libs.parser.nxos.show_isis import (ShowIsis,
                                              ShowIsisHostname,
                                              ShowIsisAdjacency,
                                              ShowIsisInterface,
                                            #    ShowIsisDatabaseDetail,
                                            #    ShowRunSectionIsis,
                                            #    ShowIsisNeighbors
                                               )


class TestShowIsis(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'test': {
            'process_id': 'test',
            'instance_number': 1,
            'uuid': '1090519320',
            'pid': 1581,
            'vrf': {
                'default': {
                    'vrf': 'default',
                    'system_id': '3333.3333.3333',
                    'is_type': 'L1-L2',
                    'sap': 412,
                    'queue_handle': 15,
                    'lsp_mtu': 1492,
                    'stateful_ha': 'enabled',
                    'graceful_restart': {
                        'enable': True,
                        'state': 'Inactive',
                        'last_gr_status': 'none',
                    },
                    'start_mode': 'Complete',
                    'bfd_ipv4': 'disabled',
                    'bfd_ipv6': 'disabled',
                    'topology_mode': 'Multitopology',
                    'metric_type': 'advertise(wide), accept(narrow, wide)',
                    'area_address': ['49.0001'],
                    'enable': True,
                    'vrf_id': 1,
                    'sr_ipv4': 'not configured and disabled',
                    'sr_ipv6': 'not configured and disabled',
                    'supported_interfaces': ['Loopback0', 'Ethernet1/1.115', 'Ethernet1/2.115'],
                    'topology': {
                        0: {
                            'ipv4_unicast': {
                                'number_of_interface': 3,
                                'distance': 115,
                            },
                            'ipv6_unicast': {
                                'number_of_interface': 0,
                                'distance': 115,
                            },
                        },
                        2: {
                            'ipv6_unicast': {
                                'number_of_interface': 3,
                                'distance': 115,
                            },
                        },
                    },
                    'authentication': {
                        'level_1': {
                            'authentication_type': {
                            },
                            'auth_check': 'set',
                        },
                        'level_2': {
                            'authentication_type': {
                            },
                            'auth_check': 'set',
                        },
                    },
                    'l1_next_spf': '00:00:07',
                    'l2_next_spf': '00:00:04',
                },
                'VRF1': {
                    'vrf': 'VRF1',
                    'system_id': '3333.3333.3333',
                    'is_type': 'L1-L2',
                    'sap': 412,
                    'queue_handle': 15,
                    'lsp_mtu': 1492,
                    'stateful_ha': 'enabled',
                    'graceful_restart': {
                        'enable': True,
                        'state': 'Inactive',
                        'last_gr_status': 'none',
                    },
                    'start_mode': 'Complete',
                    'bfd_ipv4': 'disabled',
                    'bfd_ipv6': 'disabled',
                    'topology_mode': 'Multitopology',
                    'metric_type': 'advertise(wide), accept(narrow, wide)',
                    'area_address': ['49.0001'],
                    'enable': True,
                    'vrf_id': 3,
                    'sr_ipv4': 'not configured and disabled',
                    'sr_ipv6': 'not configured and disabled',
                    'supported_interfaces': ['Loopback300', 'Ethernet1/1.415', 'Ethernet1/2.415'],
                    'topology': {
                        0: {
                            'ipv4_unicast': {
                                'number_of_interface': 3,
                                'distance': 115,
                            },
                            'ipv6_unicast': {
                                'number_of_interface': 0,
                                'distance': 115,
                            },
                        },
                        2: {
                            'ipv6_unicast': {
                                'number_of_interface': 3,
                                'distance': 115,
                            },
                        },
                    },
                    'authentication': {
                        'level_1': {
                            'authentication_type': {
                            },
                            'auth_check': 'set',
                        },
                        'level_2': {
                            'authentication_type': {
                            },
                            'auth_check': 'set',
                        },
                    },
                    'l1_next_spf': 'Inactive',
                    'l2_next_spf': 'Inactive',
                },
            },
        },
    }
    golden_output = {'execute.return_value': '''\
        R3_nx# show isis vrf all

        ISIS process : test
        Instance number :  1
        UUID: 1090519320
        Process ID 1581
        VRF: default
        System ID : 3333.3333.3333  IS-Type : L1-L2
        SAP : 412  Queue Handle : 15
        Maximum LSP MTU: 1492
        Stateful HA enabled
        Graceful Restart enabled. State: Inactive
        Last graceful restart status : none
        Start-Mode Complete
        BFD IPv4 is globally disabled for ISIS process: test
        BFD IPv6 is globally disabled for ISIS process: test
        Topology-mode is Multitopology
        Metric-style : advertise(wide), accept(narrow, wide)
        Area address(es) :
            49.0001
        Process is up and running
        VRF ID: 1
        Stale routes during non-graceful controlled restart
        Enable resolution of L3->L2 address for ISIS adjacency
        SR IPv4 is not configured and disabled for ISIS process: test
        SR IPv6 is not configured and disabled for ISIS process: test
        Interfaces supported by IS-IS :
            loopback0
            Ethernet1/1.115
            Ethernet1/2.115
        Topology : 0
        Address family IPv4 unicast :
            Number of interface : 3
            Distance : 115
        Address family IPv6 unicast :
            Number of interface : 0
            Distance : 115
        Topology : 2
        Address family IPv6 unicast :
            Number of interface : 3
            Distance : 115
        Level1
        No auth type and keychain
        Auth check set
        Level2
        No auth type and keychain
        Auth check set
        L1 Next SPF: 00:00:07
        L2 Next SPF: 00:00:04

        ISIS process : test
        Instance number :  1
        UUID: 1090519320
        Process ID 1581
        VRF: VRF1
        System ID : 3333.3333.3333  IS-Type : L1-L2
        SAP : 412  Queue Handle : 15
        Maximum LSP MTU: 1492
        Stateful HA enabled
        Graceful Restart enabled. State: Inactive
        Last graceful restart status : none
        Start-Mode Complete
        BFD IPv4 is globally disabled for ISIS process: test
        BFD IPv6 is globally disabled for ISIS process: test
        Topology-mode is Multitopology
        Metric-style : advertise(wide), accept(narrow, wide)
        Area address(es) :
            49.0001
        Process is up and running
        VRF ID: 3
        Stale routes during non-graceful controlled restart
        Enable resolution of L3->L2 address for ISIS adjacency
        SR IPv4 is not configured and disabled for ISIS process: test
        SR IPv6 is not configured and disabled for ISIS process: test
        Interfaces supported by IS-IS :
            loopback300
            Ethernet1/1.415
            Ethernet1/2.415
        Topology : 0
        Address family IPv4 unicast :
            Number of interface : 3
            Distance : 115
        Address family IPv6 unicast :
            Number of interface : 0
            Distance : 115
        Topology : 2
        Address family IPv6 unicast :
            Number of interface : 3
            Distance : 115
        Level1
        No auth type and keychain
        Auth check set
        Level2
        No auth type and keychain
        Auth check set
        L1 Next SPF: Inactive
        L2 Next SPF: Inactive
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIsis(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowIsis(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output,self.golden_parsed_output)


class TestShowIsisInterface(unittest.TestCase):
    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'test': {
            'vrf': {
                'default': {
                    'interfaces': {
                        'loopback0': {
                            'name': 'loopback0',
                            'status': 'protocol-up/link-up/admin-up',
                            'ipv4': '3.3.3.3',
                            'ipv4_subnet': '3.3.3.3/32',
                            'ipv6': '2001:3:3:3::3/128',
                            'ipv6_state': 'VALID',
                            'ipv6_subnet': '2001:3:3:3::3/128',
                            'ipv6_link_address': 'fe80::5c00:80ff:fe02:0',
                            'authentication': {
                                'level_1': {
                                    'authentication_type': {
                                    },
                                    'auth_check': 'set',
                                },
                                'level_2': {
                                    'authentication_type': {
                                    },
                                    'auth_check': 'set',
                                },
                            },
                            'index': '0x0001',
                            'local_circuit_id': '0x01',
                            'circuit_type': 'L1-2',
                            'bfd_ipv4': 'disabled',
                            'bfd_ipv6': 'disabled',
                            'mtr': 'enabled',
                            'levels': {
                                'level_1': {
                                    'metric': '1',
                                },
                                'level_2': {
                                    'metric': '1',
                                },
                            },
                            'topologies': {
                                1: {
                                    'level': '1',
                                    'mt': '0',
                                    'metric': '1',
                                    'metric_cfg': 'no',
                                    'fwdng': 'UP',
                                    'ipv4_mt': 'UP',
                                    'ipv4_cfg': 'yes',
                                    'ipv6_mt': 'DN',
                                    'ipv6_cfg': 'yes',
                                },
                                2: {
                                    'level': '1',
                                    'mt': '2',
                                    'metric': '1',
                                    'metric_cfg': 'no',
                                    'fwdng': 'UP',
                                    'ipv4_mt': 'DN',
                                    'ipv4_cfg': 'no',
                                    'ipv6_mt': 'UP',
                                    'ipv6_cfg': 'yes',
                                },
                                3: {
                                    'level': '2',
                                    'mt': '0',
                                    'metric': '1',
                                    'metric_cfg': 'no',
                                    'fwdng': 'UP',
                                    'ipv4_mt': 'UP',
                                    'ipv4_cfg': 'yes',
                                    'ipv6_mt': 'DN',
                                    'ipv6_cfg': 'yes',
                                },
                                4: {
                                    'level': '2',
                                    'mt': '2',
                                    'metric': '1',
                                    'metric_cfg': 'no',
                                    'fwdng': 'UP',
                                    'ipv4_mt': 'DN',
                                    'ipv4_cfg': 'no',
                                    'ipv6_mt': 'UP',
                                    'ipv6_cfg': 'yes',
                                },
                            },
                        },
                        'Ethernet1/1.115': {
                            'name': 'Ethernet1/1.115',
                            'status': 'protocol-up/link-up/admin-up',
                            'ipv4': '10.23.115.3',
                            'ipv4_subnet': '10.23.115.0/24',
                            'ipv6': '2001:10:23:115::3/64',
                            'ipv6_state': 'VALID',
                            'ipv6_subnet': '2001:10:23:115::/64',
                            'ipv6_link_address': 'fe80::5c00:80ff:fe02:7',
                            'authentication': {
                                'level_1': {
                                    'authentication_type': {
                                    },
                                    'auth_check': 'set',
                                },
                                'level_2': {
                                    'authentication_type': {
                                    },
                                    'auth_check': 'set',
                                },
                            },
                            'index': '0x0002',
                            'local_circuit_id': '0x01',
                            'circuit_type': 'L1-2',
                            'bfd_ipv4': 'disabled',
                            'bfd_ipv6': 'disabled',
                            'mtr': 'enabled',
                            'mtu': 1500,
                            'lsp_interval': '33 ms',
                            'levels': {
                                'level_1': {
                                    'designated_is': 'R2_xr',
                                    'metric_0': '40',
                                    'metric_2': '40',
                                    'csnp': '10',
                                    'next_csnp': '00:00:06',
                                    'hello': '10',
                                    'multi': '3',
                                    'next_iih': '00:00:04',
                                    'adjs': '1',
                                    'adjs_up': '1',
                                    'pri': '64',
                                    'circuit_id': 'R2_xr.03',
                                    'since': '5d01h',
                                },
                                'level_2': {
                                    'designated_is': 'R2_xr',
                                    'metric_0': '40',
                                    'metric_2': '40',
                                    'csnp': '10',
                                    'next_csnp': '00:00:03',
                                    'hello': '10',
                                    'multi': '3',
                                    'next_iih': '00:00:09',
                                    'adjs': '1',
                                    'adjs_up': '1',
                                    'pri': '64',
                                    'circuit_id': 'R2_xr.03',
                                    'since': '5d01h',
                                },
                            },
                            'topologies': {
                                1: {
                                    'level': '1',
                                    'mt': '0',
                                    'metric': '40',
                                    'metric_cfg': 'no',
                                    'fwdng': 'UP',
                                    'ipv4_mt': 'UP',
                                    'ipv4_cfg': 'yes',
                                    'ipv6_mt': 'DN',
                                    'ipv6_cfg': 'yes',
                                },
                                2: {
                                    'level': '1',
                                    'mt': '2',
                                    'metric': '40',
                                    'metric_cfg': 'no',
                                    'fwdng': 'UP',
                                    'ipv4_mt': 'DN',
                                    'ipv4_cfg': 'no',
                                    'ipv6_mt': 'UP',
                                    'ipv6_cfg': 'yes',
                                },
                                3: {
                                    'level': '2',
                                    'mt': '0',
                                    'metric': '40',
                                    'metric_cfg': 'no',
                                    'fwdng': 'UP',
                                    'ipv4_mt': 'UP',
                                    'ipv4_cfg': 'yes',
                                    'ipv6_mt': 'DN',
                                    'ipv6_cfg': 'yes',
                                },
                                4: {
                                    'level': '2',
                                    'mt': '2',
                                    'metric': '40',
                                    'metric_cfg': 'no',
                                    'fwdng': 'UP',
                                    'ipv4_mt': 'DN',
                                    'ipv4_cfg': 'no',
                                    'ipv6_mt': 'UP',
                                    'ipv6_cfg': 'yes',
                                },
                            },
                        },
                        'Ethernet1/2.115': {
                            'name': 'Ethernet1/2.115',
                            'status': 'protocol-up/link-up/admin-up',
                            'ipv4': '10.13.115.3',
                            'ipv4_subnet': '10.13.115.0/24',
                            'ipv6': '2001:10:13:115::3/64',
                            'ipv6_state': 'VALID',
                            'ipv6_subnet': '2001:10:13:115::/64',
                            'ipv6_link_address': 'fe80::5c00:80ff:fe02:7',
                            'authentication': {
                                'level_1': {
                                    'authentication_type': {
                                    },
                                    'auth_check': 'set',
                                },
                                'level_2': {
                                    'authentication_type': {
                                    },
                                    'auth_check': 'set',
                                },
                            },
                            'index': '0x0003',
                            'local_circuit_id': '0x02',
                            'circuit_type': 'L1-2',
                            'bfd_ipv4': 'disabled',
                            'bfd_ipv6': 'disabled',
                            'mtr': 'enabled',
                            'mtu': 1500,
                            'lsp_interval': '33 ms',
                            'levels': {
                                'level_1': {
                                    'designated_is': 'R1_xe',
                                    'metric_0': '40',
                                    'metric_2': '40',
                                    'csnp': '10',
                                    'next_csnp': '00:00:10',
                                    'hello': '10',
                                    'multi': '3',
                                    'next_iih': '00:00:03',
                                    'adjs': '1',
                                    'adjs_up': '1',
                                    'pri': '64',
                                    'circuit_id': 'R1_xe.02',
                                    'since': '5d01h',
                                },
                                'level_2': {
                                    'designated_is': 'R1_xe',
                                    'metric_0': '40',
                                    'metric_2': '40',
                                    'csnp': '10',
                                    'next_csnp': '00:00:02',
                                    'hello': '10',
                                    'multi': '3',
                                    'next_iih': '00:00:02',
                                    'adjs': '1',
                                    'adjs_up': '1',
                                    'pri': '64',
                                    'circuit_id': 'R1_xe.02',
                                    'since': '5d01h',
                                },
                            },
                            'topologies': {
                                1: {
                                    'level': '1',
                                    'mt': '0',
                                    'metric': '40',
                                    'metric_cfg': 'no',
                                    'fwdng': 'UP',
                                    'ipv4_mt': 'UP',
                                    'ipv4_cfg': 'yes',
                                    'ipv6_mt': 'DN',
                                    'ipv6_cfg': 'yes',
                                },
                                2: {
                                    'level': '1',
                                    'mt': '2',
                                    'metric': '40',
                                    'metric_cfg': 'no',
                                    'fwdng': 'UP',
                                    'ipv4_mt': 'DN',
                                    'ipv4_cfg': 'no',
                                    'ipv6_mt': 'UP',
                                    'ipv6_cfg': 'yes',
                                },
                                3: {
                                    'level': '2',
                                    'mt': '0',
                                    'metric': '40',
                                    'metric_cfg': 'no',
                                    'fwdng': 'UP',
                                    'ipv4_mt': 'UP',
                                    'ipv4_cfg': 'yes',
                                    'ipv6_mt': 'DN',
                                    'ipv6_cfg': 'yes',
                                },
                                4: {
                                    'level': '2',
                                    'mt': '2',
                                    'metric': '40',
                                    'metric_cfg': 'no',
                                    'fwdng': 'UP',
                                    'ipv4_mt': 'DN',
                                    'ipv4_cfg': 'no',
                                    'ipv6_mt': 'UP',
                                    'ipv6_cfg': 'yes',
                                },
                            },
                        },
                    },
                },
            },
        },
    }
    golden_output = {'execute.return_value': '''\
        R3_nx# show isis interface vrf default
        IS-IS process: test VRF: default
        loopback0, Interface status: protocol-up/link-up/admin-up
        IP address: 3.3.3.3, IP subnet: 3.3.3.3/32
        IPv6 address:
            2001:3:3:3::3/128 [VALID]
        IPv6 subnet:  2001:3:3:3::3/128
        IPv6 link-local address: fe80::5c00:80ff:fe02:0
        Level1
            No auth type and keychain
            Auth check set
        Level2
            No auth type and keychain
            Auth check set
        Index: 0x0001, Local Circuit ID: 0x01, Circuit Type: L1-2
        BFD IPv4 is locally disabled for Interface loopback0
        BFD IPv6 is locally disabled for Interface loopback0
        MTR is enabled
        Level      Metric
        1               1
        2               1
        Topologies enabled:
            L  MT  Metric  MetricCfg  Fwdng IPV4-MT  IPV4Cfg  IPV6-MT  IPV6Cfg
            1  0        1       no   UP    UP       yes      DN       yes
            1  2        1       no   UP    DN       no       UP       yes
            2  0        1       no   UP    UP       yes      DN       yes
            2  2        1       no   UP    DN       no       UP       yes

        Ethernet1/1.115, Interface status: protocol-up/link-up/admin-up
        IP address: 10.23.115.3, IP subnet: 10.23.115.0/24
        IPv6 address:
            2001:10:23:115::3/64 [VALID]
        IPv6 subnet:  2001:10:23:115::/64
        IPv6 link-local address: fe80::5c00:80ff:fe02:7
        Level1
            No auth type and keychain
            Auth check set
        Level2
            No auth type and keychain
            Auth check set
        Index: 0x0002, Local Circuit ID: 0x01, Circuit Type: L1-2
        BFD IPv4 is locally disabled for Interface Ethernet1/1.115
        BFD IPv6 is locally disabled for Interface Ethernet1/1.115
        MTR is enabled
        LSP interval: 33 ms, MTU: 1500
        Level-1 Designated IS: R2_xr
        Level-2 Designated IS: R2_xr
        Level   Metric-0   Metric-2   CSNP  Next CSNP  Hello   Multi   Next IIH
        1              40     40     10 00:00:06      10   3       00:00:04
        2              40     40     10 00:00:03      10   3       00:00:09
        Level  Adjs   AdjsUp Pri  Circuit ID         Since
        1         1        1  64  R2_xr.03           5d01h
        2         1        1  64  R2_xr.03           5d01h
        Topologies enabled:
            L  MT  Metric  MetricCfg  Fwdng IPV4-MT  IPV4Cfg  IPV6-MT  IPV6Cfg
            1  0        40      no   UP    UP       yes      DN       yes
            1  2        40      no   UP    DN       no       UP       yes
            2  0        40      no   UP    UP       yes      DN       yes
            2  2        40      no   UP    DN       no       UP       yes

        Ethernet1/2.115, Interface status: protocol-up/link-up/admin-up
        IP address: 10.13.115.3, IP subnet: 10.13.115.0/24
        IPv6 address:
            2001:10:13:115::3/64 [VALID]
        IPv6 subnet:  2001:10:13:115::/64
        IPv6 link-local address: fe80::5c00:80ff:fe02:7
        Level1
            No auth type and keychain
            Auth check set
        Level2
            No auth type and keychain
            Auth check set
        Index: 0x0003, Local Circuit ID: 0x02, Circuit Type: L1-2
        BFD IPv4 is locally disabled for Interface Ethernet1/2.115
        BFD IPv6 is locally disabled for Interface Ethernet1/2.115
        MTR is enabled
        LSP interval: 33 ms, MTU: 1500
        Level-1 Designated IS: R1_xe
        Level-2 Designated IS: R1_xe
        Level   Metric-0   Metric-2   CSNP  Next CSNP  Hello   Multi   Next IIH
        1              40     40     10 00:00:10      10   3       00:00:03
        2              40     40     10 00:00:02      10   3       00:00:02
        Level  Adjs   AdjsUp Pri  Circuit ID         Since
        1         1        1  64  R1_xe.02           5d01h
        2         1        1  64  R1_xe.02           5d01h
        Topologies enabled:
            L  MT  Metric  MetricCfg  Fwdng IPV4-MT  IPV4Cfg  IPV6-MT  IPV6Cfg
            1  0        40      no   UP    UP       yes      DN       yes
            1  2        40      no   UP    DN       no       UP       yes
            2  0        40      no   UP    UP       yes      DN       yes
            2  2        40      no   UP    DN       no       UP       yes
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIsisInterface(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowIsisInterface(device=self.device)
        parsed_output = obj.parse(vrf='default')
        self.assertEqual(parsed_output, self.golden_parsed_output)


class TestShowIsisHostname(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'test': {
            'vrf': {
                'default': {
                    'hostname_db': {
                        'hostname': {
                            '1111.1111.1111': {
                                'hostname': 'R1_ios',
                                'level': 1,
                            },
                            '2222.2222.2222': {
                                'hostname': 'R2_xr',
                                'level': 1,
                            },
                            '3333.3333.3333': {
                                'hostname': 'R3_nx',
                                'level': 1,
                                'local_router': True,
                            },
                        },
                    },
                },
                'VRF1': {
                    'hostname_db': {
                        'hostname': {
                            '3333.3333.3333': {
                                'hostname': 'R3_nx',
                                'level': 1,
                                'local_router': True,
                            },
                        },
                    },
                },
            },
        },
    }
    golden_output = {'execute.return_value': '''\
        R3_nx# show isis hostname vrf all
        IS-IS Process: test dynamic hostname table VRF: default
        Level  System ID       Dynamic hostname
        1      1111.1111.1111  R1_ios
        1      2222.2222.2222  R2_xr
        1      3333.3333.3333* R3_nx

        IS-IS Process: test dynamic hostname table VRF: VRF1
        Level  System ID       Dynamic hostname
        1      3333.3333.3333* R3_nx
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIsisHostname(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowIsisHostname(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output,self.golden_parsed_output)


class TestShowIsisAdjacency(unittest.TestCase):
    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'test': {
            'vrf': {
                'default': {
                    'interfaces': {
                        'Ethernet1/1.115': {
                            'adjacencies': {
                                'R2_xr': {
                                    'neighbor_snpa': {
                                        'fa16.3e44.0679': {
                                            'level': {
                                                1: {
                                                    'hold_time': '00:00:09',
                                                    'state': 'UP',
                                                },
                                                2: {
                                                    'hold_time': '00:00:07',
                                                    'state': 'UP',
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                        'Ethernet1/2.115': {
                            'adjacencies': {
                                'R1_ios': {
                                    'neighbor_snpa': {
                                        'fa16.3e0e.fd03': {
                                            'level': {
                                                1: {
                                                    'hold_time': '00:00:07',
                                                    'state': 'UP',
                                                },
                                                2: {
                                                    'hold_time': '00:00:10',
                                                    'state': 'UP',
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
                'VRF1': {
                    'interfaces': {
                        'Ethernet1/1.415': {
                            'adjacencies': {
                                '2222.2222.2222': {
                                    'neighbor_snpa': {
                                        'fa16.3e44.0679': {
                                            'level': {
                                                1: {
                                                    'hold_time': '00:00:32',
                                                    'state': 'INIT',
                                                },
                                                2: {
                                                    'hold_time': '00:00:24',
                                                    'state': 'INIT',
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }
    golden_output = {'execute.return_value': '''\
        R3_nx# show isis adjacency vrf all
        IS-IS process: test VRF: default
        IS-IS adjacency database:
        Legend: '!': No AF level connectivity in given topology
        System ID       SNPA            Level  State  Hold Time  Interface
        R2_xr           fa16.3e44.0679  1      UP     00:00:09   Ethernet1/1.115
        R2_xr           fa16.3e44.0679  2      UP     00:00:07   Ethernet1/1.115
        R1_ios          fa16.3e0e.fd03  1      UP     00:00:07   Ethernet1/2.115
        R1_ios          fa16.3e0e.fd03  2      UP     00:00:10   Ethernet1/2.115

        IS-IS process: test VRF: VRF1
        IS-IS adjacency database:
        Legend: '!': No AF level connectivity in given topology
        System ID       SNPA            Level  State  Hold Time  Interface
        2222.2222.2222  fa16.3e44.0679  1      INIT   00:00:32   Ethernet1/1.415
        2222.2222.2222  fa16.3e44.0679  2      INIT   00:00:24   Ethernet1/1.415
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIsisAdjacency(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowIsisAdjacency(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output, self.golden_parsed_output)


# class TestShowIsisDatabaseDetail(unittest.TestCase):
#     device = Device(name='aDevice')

#     empty_output = {'execute.return_value': ''}

#     golden_parsed_output = {
#         'tag':{
#             'VRF1':{
#                 'level':{
#                     1: {
#                         'R2.00-00':{
#                             'lsp_sequence_num': '0x00000007',
#                             'lsp_checksum': '0x8A6D',
#                             'local_router': True,
#                             'lsp_holdtime': '403',
#                             'lsp_rcvd': '*',
#                             'attach_bit': 1,
#                             'p_bit': 0,
#                             'overload_bit': 0,
#                             'area_address': '49.0001',
#                             'nlpid': '0xCC 0x8E',
#                             'topology': {
#                                 'ipv4': {
#                                     'code':'0x0',
#                                 },
#                                 'ipv6': {
#                                     'code': '0x4002 ATT'
#                                 }
#                             },
#                             'hostname': 'R2',
#                             'ip_address': '10.84.66.66',
#                             '10.229.7.0/24': {
#                                 'ip': {
#                                     'metric': 10,
#                                 },
#                             },
#                             '10.84.66.66/32':{
#                                 'ip': {
#                                     'metric': 10,
#                                 },
#                             },
#                             'ipv6_address': '2001:DB8:66:66:66::66',
#                             '2001:DB8:20:2::/64': {
#                                 'ipv6': {
#                                     'metric': 10,
#                                     'mt_ipv6': True
#                                 },
#                             },
#                             '2001:DB8:66:66:66::66/128': {
#                                 'ipv6':{
#                                     'metric': 10,
#                                     'mt_ipv6': True
#                                 },
#                             },
#                         },
#                     },
#                     2: {
#                         'R2.00-00': {
#                             'lsp_sequence_num': '0x00000008',
#                             'lsp_checksum': '0x621E',
#                             'local_router': True,
#                             'lsp_holdtime': '1158',
#                             'lsp_rcvd': '*',
#                             'attach_bit': 0,
#                             'p_bit': 0,
#                             'overload_bit': 0,
#                             'area_address': '49.0001',
#                             'nlpid': '0xCC 0x8E',
#                             'topology': {
#                                 'ipv4': {
#                                     'code': '0x0',
#                                 },
#                                 'ipv6': {
#                                     'code': '0x2'
#                                 }
#                             },
#                             'hostname': 'R2',
#                             'R2.01': {
#                                 'is-extended': {
#                                         'metric': 10,
#                                 },
#                                 'is': {
#                                     'metric': 10,
#                                     'mt_ipv6': True,
#                                 },
#                             },
#                             'ip_address': '10.84.66.66',
#                             '10.229.7.0/24': {
#                                 'ip': {
#                                     'metric': 10,
#                                 },
#                             },
#                             '10.84.66.66/32': {
#                                 'ip':{
#                                     'metric': 10,
#                                 },
#                             },
#                             'ipv6_address': '2001:DB8:66:66:66::66',
#                             '2001:DB8:20:2::/64': {
#                                     'ipv6': {
#                                         'metric': 10,
#                                         'mt_ipv6': True
#                                     },
#                                 },
#                                 '2001:DB8:66:66:66::66/128': {
#                                     'ipv6': {
#                                         'metric': 10,
#                                         'mt_ipv6': True
#                                     }
#                                 },
#                             },
#                         'R2.01-00': {
#                             'lsp_sequence_num': '0x00000002',
#                             'lsp_checksum': '0x3334',
#                             'local_router': True,
#                             'lsp_holdtime': '414',
#                             'lsp_rcvd': '*',
#                             'attach_bit': 0,
#                             'p_bit': 0,
#                             'overload_bit': 0,
#                             'R2.00': {
#                                 'is-extended': {
#                                     'metric': 0,
#                                 },
#                             },
#                             'R7.00': {
#                                 'is-extended': {
#                                     'metric': 0,
#                                 },
#                             },
#                         },
#                         'R7.00-00': {
#                             'lsp_sequence_num': '0x00000005',
#                             'lsp_checksum': '0x056E',
#                             'lsp_holdtime': '735',
#                             'lsp_rcvd': '1199',
#                             'attach_bit': 0,
#                             'p_bit': 0,
#                             'overload_bit': 0,
#                             'area_address': '49.0002',
#                             'nlpid': '0xCC 0x8E',
#                             'router_id': '10.1.77.77',
#                             'ip_address': '10.1.77.77',
#                             'topology': {
#                                 'ipv4': {
#                                     'code': '0x0',
#                                 },
#                                 'ipv6': {
#                                     'code': '0x2'
#                                 }
#                             },
#                             'hostname': 'R7',
#                             'R2.01': {
#                                 'is-extended': {
#                                     'metric': 40,
#                                 },
#                                 'is': {
#                                     'metric': 40,
#                                     'mt_ipv6': True,
#                                 },
#                             },
#                             '10.1.77.77/32':{
#                                 'ip': {
#                                     'metric': 1

#                                 }
#                             },
#                             '10.229.7.0/24': {
#                                 'ip': {
#                                     'metric': 40
#                                 }
#                             },
#                             '2001:DB8:77:77:77::77/128': {
#                                 'ipv6': {
#                                     'metric': 1,
#                                     'mt_ipv6': True
#                                 }
#                             },
#                             '2001:DB8:20:2::/64': {
#                                 'ipv6': {
#                                     'metric': 40,
#                                     'mt_ipv6': True
#                                 }
#                             },
#                         },
#                     }
#                 }
#             }
#         }
#     }

#     golden_output = {'execute.return_value': '''\
#     R2#show isis database detail

#     Tag VRF1:
#     IS-IS Level-1 Link State Database:
#     LSPID                 LSP Seq Num  LSP Checksum  LSP Holdtime/Rcvd      ATT/P/OL
#     R2.00-00            * 0x00000007   0x8A6D                 403/*         1/0/0
#       Area Address: 49.0001
#       NLPID:        0xCC 0x8E
#       Topology:     IPv4 (0x0)
#                     IPv6 (0x4002 ATT)
#       Hostname: R2
#       IP Address:   10.84.66.66
#       Metric: 10         IP 10.229.7.0/24
#       Metric: 10         IP 10.84.66.66/32
#       IPv6 Address: 2001:DB8:66:66:66::66
#       Metric: 10         IPv6 (MT-IPv6) 2001:DB8:20:2::/64
#       Metric: 10         IPv6 (MT-IPv6) 2001:DB8:66:66:66::66/128
#     IS-IS Level-2 Link State Database:
#     LSPID                 LSP Seq Num  LSP Checksum  LSP Holdtime/Rcvd      ATT/P/OL
#     R2.00-00            * 0x00000008   0x621E                1158/*         0/0/0
#       Area Address: 49.0001
#       NLPID:        0xCC 0x8E
#       Topology:     IPv4 (0x0)
#                     IPv6 (0x2)
#       Hostname: R2
#       Metric: 10         IS-Extended R2.01
#       Metric: 10         IS (MT-IPv6) R2.01
#       IP Address:   10.84.66.66
#       Metric: 10         IP 10.229.7.0/24
#       Metric: 10         IP 10.84.66.66/32
#       IPv6 Address: 2001:DB8:66:66:66::66
#       Metric: 10         IPv6 (MT-IPv6) 2001:DB8:20:2::/64
#       Metric: 10         IPv6 (MT-IPv6) 2001:DB8:66:66:66::66/128
#     R2.01-00            * 0x00000002   0x3334                 414/*         0/0/0
#       Metric: 0          IS-Extended R2.00
#       Metric: 0          IS-Extended R7.00
#     R7.00-00              0x00000005   0x056E                 735/1199      0/0/0
#       Area Address: 49.0002
#       NLPID:        0xCC 0x8E
#       Router ID:    10.1.77.77
#       IP Address:   10.1.77.77
#       Topology:     IPv6 (0x2)
#                     IPv4 (0x0)
#       Hostname: R7
#       Metric: 40         IS (MT-IPv6) R2.01
#       Metric: 40         IS-Extended R2.01
#       Metric: 1          IP 10.1.77.77/32
#       Metric: 40         IP 10.229.7.0/24
#       Metric: 1          IPv6 (MT-IPv6) 2001:DB8:77:77:77::77/128
#       Metric: 40         IPv6 (MT-IPv6) 2001:DB8:20:2::/64
#     '''
#     }

#     def test_empty(self):
#         self.device = Mock(**self.empty_output)
#         platform_obj = ShowIsisDatabaseDetail(device=self.device)
#         with self.assertRaises(SchemaEmptyParserError):
#             parsed_output = platform_obj.parse()

#     def test_golden(self):
#         self.maxDiff = None
#         self.device = Mock(**self.golden_output)
#         platform_obj = ShowIsisDatabaseDetail(device=self.device)
#         parsed_output = platform_obj.parse()
#         self.assertEqual(parsed_output, self.golden_parsed_output)

# class TestShowRunSecIsis(unittest.TestCase):
#     device = Device(name='aDevice')

#     empty_output = {'execute.return_value': ''}

#     golden_parsed_output = {
#         'instance':{
#             'test':{
#                 'vrf':{
#                     'default':{}
#                 }
#             },
#             'test1':{
#                 'vrf':{
#                     'VRF1':{}
#                 }
#             }
#         }
#     }

#     golden_output = {'execute.return_value': '''\

#     R2#show run | sec isis
#      ip router isis test
#      ipv6 router isis test
#      ip router isis test1
#      ipv6 router isis test1
#      ip router isis test
#      ipv6 router isis test
#      ip router isis test1
#      ipv6 router isis test1
#     router isis test
#      net 49.0001.1111.1111.1111.00
#      metric-style wide
#      !
#      address-family ipv6
#       multi-topology
#      exit-address-family
#     router isis test1
#      vrf VRF1
#      net 49.0001.1111.1111.1111.00
#      metric-style wide
#      !
#      address-family ipv6
#       multi-topology
#      exit-address-family
#     R1_xe#
#     '''
#     }

#     golden_parsed_output_2 = {
#         'instance': {
#             '': {
#                 'vrf': {
#                     'default': {}}}}}

#     golden_output_2 = {'execute.return_value': '''
#          ip router isis
#          ipv6 router isis
#          ip router isis
#          ipv6 router isis
#          ip router isis
#          ipv6 router isis
#          ip router isis
#          ipv6 router isis
#         router isis
#          net 47.0002.0000.0000.0002.00
#          is-type level-1
#          metric-style wide
#          mpls traffic-eng router-id Loopback0
#          mpls traffic-eng level-1
#     '''}

#     def test_golden(self):
#         self.maxDiff = None
#         self.device = Mock(**self.golden_output)
#         obj = ShowRunSectionIsis(device=self.device)
#         parsed_output = obj.parse()
#         self.assertEqual(parsed_output, self.golden_parsed_output)

#     def test_golden_2(self):
#         self.maxDiff = None
#         self.device = Mock(**self.golden_output_2)
#         obj = ShowRunSectionIsis(device=self.device)
#         parsed_output = obj.parse()
#         self.assertEqual(parsed_output, self.golden_parsed_output_2)

# # ====================================
# #  Unit test for 'show isis neighbors'
# # ====================================

# class TestShowIsisNeighbors(unittest.TestCase):
    # '''Unit test for "show isis neighbors"'''

    # device = Device(name='aDevice')
    # empty_output = {'execute.return_value': ''}

    # golden_parsed_output1 = {
    #     'isis': {
    #         'test': {
    #             'neighbors': {
    #                 'R2_xr': {
    #                     'type': {
    #                         'L1': {
    #                             'interface': 'Gi2.115',
    #                             'ip_address': '10.12.115.2',
    #                             'state': 'UP',
    #                             'holdtime': '7',
    #                             'circuit_id': 'R2_xr.01'},
    #                         'L2': {
    #                             'interface': 'Gi2.115',
    #                             'ip_address': '10.12.115.2',
    #                             'state': 'UP',
    #                             'holdtime': '7',
    #                             'circuit_id': 'R2_xr.01'}}},
    #                 'R3_nx': {
    #                     'type': {
    #                         'L1': {
    #                             'interface': 'Gi3.115',
    #                             'ip_address': '10.13.115.3',
    #                             'state': 'UP',
    #                             'holdtime': '28',
    #                             'circuit_id': 'R1_xe.02'},
    #                         'L2': {
    #                             'interface': 'Gi3.115',
    #                             'ip_address': '10.13.115.3',
    #                             'state': 'UP',
    #                             'holdtime': '23',
    #                             'circuit_id': 'R1_xe.02'}}}}},
    #         'test1': {
    #             'neighbors': {
    #                 '2222.2222.2222': {
    #                     'type': {
    #                         'L1': {
    #                             'interface': 'Gi2.415',
    #                             'ip_address': '10.12.115.2',
    #                             'state': 'INIT',
    #                             'holdtime': '21',
    #                             'circuit_id': '2222.2222.2222.01'},
    #                         'L2': {
    #                             'interface': 'Gi2.415',
    #                             'ip_address': '10.12.115.2',
    #                             'state': 'INIT',
    #                             'holdtime': '20',
    #                             'circuit_id': '2222.2222.2222.01'}}},
    #                 'R3_nx': {
    #                     'type': {
    #                         'L1': {
    #                             'interface': 'Gi3.415',
    #                             'ip_address': '10.13.115.3',
    #                             'state': 'UP',
    #                             'holdtime': '21',
    #                             'circuit_id': 'R1_xe.02'},
    #                         'L2': {
    #                             'interface': 'Gi3.415',
    #                             'ip_address': '10.13.115.3',
    #                             'state': 'UP',
    #                             'holdtime': '27',
    #                             'circuit_id': 'R1_xe.02'}}}}}}}

    # golden_output1 = {'execute.return_value': '''
    #     R1_xe#show isis neighbors 

    #     Tag test:
    #     System Id       Type Interface     IP Address      State Holdtime Circuit Id
    #     R2_xr           L1   Gi2.115       10.12.115.2     UP    7        R2_xr.01           
    #     R2_xr           L2   Gi2.115       10.12.115.2     UP    7        R2_xr.01           
    #     R3_nx           L1   Gi3.115       10.13.115.3     UP    28       R1_xe.02           
    #     R3_nx           L2   Gi3.115       10.13.115.3     UP    23       R1_xe.02           
        
    #     Tag test1:
    #     System Id       Type Interface     IP Address      State Holdtime Circuit Id
    #     2222.2222.2222  L1   Gi2.415       10.12.115.2     INIT  21       2222.2222.2222.01  
    #     2222.2222.2222  L2   Gi2.415       10.12.115.2     INIT  20       2222.2222.2222.01  
    #     R3_nx           L1   Gi3.415       10.13.115.3     UP    21       R1_xe.02           
    #     R3_nx           L2   Gi3.415       10.13.115.3     UP    27       R1_xe.02           
        
    # '''}

    # def test_show_isis_neighbors_empty(self):
    #     self.device = Mock(**self.empty_output)
    #     obj = ShowIsisNeighbors(device=self.device)
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    # def test_show_isis_neighbors_golden1(self):
    #     self.maxDiff = None
    #     self.device = Mock(**self.golden_output1)
    #     obj = ShowIsisNeighbors(device=self.device)
    #     parsed_output = obj.parse()
    #     self.assertEqual(parsed_output, self.golden_parsed_output1)


if __name__ == '__main__':
    unittest.main()