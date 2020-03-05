#!/bin/env python
import unittest
from unittest.mock import Mock
from pyats.topology import Device

from genie.metaparser.util.exceptions import (SchemaMissingKeyError,
                                              SchemaEmptyParserError)

from genie.libs.parser.nxos.show_isis import (ShowIsis,
                                              ShowIsisHostname,
                                              ShowIsisAdjacency,
                                              ShowIsisInterface,
                                              ShowIsisSpfLogDetail,
                                              ShowIsisDatabaseDetail,
                                              ShowIsisHostnameDetail)


class TestShowIsis(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    maxDiff = None

    golden_parsed_output = {
        'instance': {
            'test': {
                'isis_process': 'test',
                'instance_number': 1,
                'uuid': '1090519320',
                'process_id': 1581,
                'vrf': {
                    'default': {
                        'vrf': 'default',
                        'system_id': '3333.33ff.6666',
                        'is_type': 'L1-L2',
                        'sap': 412,
                        'queue_handle': 15,
                        'maximum_lsp_mtu': 1492,
                        'stateful_ha': 'enabled',
                        'graceful_restart': {
                            'enable': True,
                            'state': 'Inactive',
                            'last_gr_status': 'none',
                        },
                        'start_mode': 'Complete',
                        'bfd_ipv4': 'globally disabled',
                        'bfd_ipv6': 'globally disabled',
                        'topology_mode': 'Multitopology',
                        'metric_type': {
                            'advertise': ['wide'],
                            'accept': ['narrow', 'wide'],
                        },
                        'area_address': ['49.0001'],
                        'process': 'up and running',
                        'vrf_id': 1,
                        'during_non_graceful_controlled_restart': 'Stale routes',
                        'resolution_of_l3_to_l2': 'Enable',
                        'sr_ipv4': 'not configured and disabled',
                        'sr_ipv6': 'not configured and disabled',
                        'supported_interfaces': ['Loopback0', 'Ethernet1/1.115', 'Ethernet1/2.115'],
                        'topology': {
                            0: {
                                'address_family': {
                                    'ipv4_unicast': {
                                        'number_of_interface': 3,
                                        'distance': 115,
                                    },
                                    'ipv6_unicast': {
                                        'number_of_interface': 0,
                                        'distance': 115,
                                    },
                                },
                            },
                            2: {
                                'address_family': {
                                    'ipv6_unicast': {
                                        'number_of_interface': 3,
                                        'distance': 115,
                                    },
                                },
                            },
                        },
                        'authentication': {
                            'level_1': {
                                'auth_check': 'set',
                            },
                            'level_2': {
                                'auth_check': 'set',
                            },
                        },
                        'l1_next_spf': '00:00:07',
                        'l2_next_spf': '00:00:04',
                    },
                    'VRF1': {
                        'vrf': 'VRF1',
                        'system_id': '3333.33ff.6666',
                        'is_type': 'L1-L2',
                        'sap': 412,
                        'queue_handle': 15,
                        'maximum_lsp_mtu': 1492,
                        'stateful_ha': 'enabled',
                        'graceful_restart': {
                            'enable': True,
                            'state': 'Inactive',
                            'last_gr_status': 'none',
                        },
                        'start_mode': 'Complete',
                        'bfd_ipv4': 'globally disabled',
                        'bfd_ipv6': 'globally disabled',
                        'topology_mode': 'Multitopology',
                        'metric_type': {
                            'advertise': ['wide'],
                            'accept': ['narrow', 'wide'],
                        },
                        'area_address': ['49.0001'],
                        'process': 'up and running',
                        'vrf_id': 3,
                        'during_non_graceful_controlled_restart': 'Stale routes',
                        'resolution_of_l3_to_l2': 'Enable',
                        'sr_ipv4': 'not configured and disabled',
                        'sr_ipv6': 'not configured and disabled',
                        'supported_interfaces': ['Loopback300', 'Ethernet1/1.415', 'Ethernet1/2.415'],
                        'topology': {
                            0: {
                                'address_family': {
                                    'ipv4_unicast': {
                                        'number_of_interface': 3,
                                        'distance': 115,
                                    },
                                    'ipv6_unicast': {
                                        'number_of_interface': 0,
                                        'distance': 115,
                                    },
                                },
                            },
                            2: {
                                'address_family': {
                                    'ipv6_unicast': {
                                        'number_of_interface': 3,
                                        'distance': 115,
                                    },
                                },
                            },
                        },
                        'authentication': {
                            'level_1': {
                                'auth_check': 'set',
                            },
                            'level_2': {
                                'auth_check': 'set',
                            },
                        },
                        'l1_next_spf': 'Inactive',
                        'l2_next_spf': 'Inactive',
                    },
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
        System ID : 3333.33ff.6666  IS-Type : L1-L2
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
        System ID : 3333.33ff.6666  IS-Type : L1-L2
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
        self.device = Mock(**self.golden_output)
        obj = ShowIsis(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output,self.golden_parsed_output)


class TestShowIsisInterface(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    maxDiff = None

    golden_parsed_output = {
        'instance': {
            'test': {
                'vrf': {
                    'default': {
                        'interfaces': {
                            'loopback0': {
                                'name': 'loopback0',
                                'status': 'protocol-up/link-up/admin-up',
                                'ipv4': '10.36.3.3',
                                'ipv4_subnet': '10.36.3.3/32',
                                'ipv6': {
                                    '2001:10:13:115::3/64': {
                                        'state': 'VALID'
                                    },
                                    '2001:10:13:115::33/64': {
                                        'state': 'VALID'
                                    },
                                    '2001:10::33/48': {
                                        'state': 'VALID'
                                    },
                                    '2001:3:3:3:3::/128': {
                                        'state': 'VALID'
                                    },
                                },
                                'ipv6_subnet': '2001:3:3:3::3/128',
                                'ipv6_link_local_address': 'fe80::5c00:80ff:fe02:0',
                                'authentication': {
                                    'level_1': {
                                        'auth_check': 'set',
                                    },
                                    'level_2': {
                                        'auth_check': 'set',
                                    },
                                },
                                'index': '0x0001',
                                'local_circuit_id': '0x01',
                                'circuit_type': 'L1-2',
                                'bfd_ipv4': 'locally disabled',
                                'bfd_ipv6': 'locally disabled',
                                'mtr': 'enabled',
                                'levels': {
                                    '1': {
                                        'metric': '1',
                                    },
                                    '2': {
                                        'metric': '1',
                                    },
                                },
                                'topologies': {
                                    '0': {
                                        'level': {
                                            '1': {
                                                'metric': '1',
                                                'metric_cfg': 'no',
                                                'fwdng': 'UP',
                                                'ipv4_mt': 'UP',
                                                'ipv4_cfg': 'yes',
                                                'ipv6_mt': 'DN',
                                                'ipv6_cfg': 'yes',
                                            },
                                            '2': {
                                                'metric': '1',
                                                'metric_cfg': 'no',
                                                'fwdng': 'UP',
                                                'ipv4_mt': 'UP',
                                                'ipv4_cfg': 'yes',
                                                'ipv6_mt': 'DN',
                                                'ipv6_cfg': 'yes',
                                            },
                                        },
                                    },
                                    '2': {
                                        'level': {
                                            '1': {
                                                'metric': '1',
                                                'metric_cfg': 'no',
                                                'fwdng': 'UP',
                                                'ipv4_mt': 'DN',
                                                'ipv4_cfg': 'no',
                                                'ipv6_mt': 'UP',
                                                'ipv6_cfg': 'yes',
                                            },
                                            '2': {
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
                                },
                            },
                            'Ethernet1/1.115': {
                                'name': 'Ethernet1/1.115',
                                'status': 'protocol-up/link-up/admin-up',
                                'ipv4': '10.23.115.3',
                                'ipv4_subnet': '10.23.115.0/24',
                                'ipv6': {
                                    '2001:10:23:115::3/64': {
                                        'state': 'VALID',
                                    },
                                },
                                'ipv6_subnet': '2001:10:23:115::/64',
                                'ipv6_link_local_address': 'fe80::5c00:80ff:fe02:7',
                                'authentication': {
                                    'level_1': {
                                        'auth_check': 'set',
                                    },
                                    'level_2': {
                                        'auth_check': 'set',
                                    },
                                },
                                'index': '0x0002',
                                'local_circuit_id': '0x01',
                                'circuit_type': 'L1-2',
                                'bfd_ipv4': 'locally disabled',
                                'bfd_ipv6': 'locally disabled',
                                'mtr': 'enabled',
                                'mtu': 1500,
                                'lsp_interval_ms': 33,
                                'levels': {
                                    '1': {
                                        'designated_is': 'R2_xr',
                                        'metric_0': '40',
                                        'metric_2': '40',
                                        'csnp': '10',
                                        'next_csnp': 'Inactive',
                                        'hello': '10',
                                        'multi': '3',
                                        'next_iih': '00:00:04',
                                        'adjs': '1',
                                        'adjs_up': '1',
                                        'pri': '64',
                                        'circuit_id': 'R2_xr.03',
                                        'since': '5d01h',
                                    },
                                    '2': {
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
                                    '0': {
                                        'level': {
                                            '1': {
                                                'metric': '40',
                                                'metric_cfg': 'no',
                                                'fwdng': 'UP',
                                                'ipv4_mt': 'UP',
                                                'ipv4_cfg': 'yes',
                                                'ipv6_mt': 'DN',
                                                'ipv6_cfg': 'yes',
                                            },
                                            '2': {
                                                'metric': '40',
                                                'metric_cfg': 'no',
                                                'fwdng': 'UP',
                                                'ipv4_mt': 'UP',
                                                'ipv4_cfg': 'yes',
                                                'ipv6_mt': 'DN',
                                                'ipv6_cfg': 'yes',
                                            },
                                        },
                                    },
                                    '2': {
                                        'level': {
                                            '1': {
                                                'metric': '40',
                                                'metric_cfg': 'no',
                                                'fwdng': 'UP',
                                                'ipv4_mt': 'DN',
                                                'ipv4_cfg': 'no',
                                                'ipv6_mt': 'UP',
                                                'ipv6_cfg': 'yes',
                                            },
                                            '2': {
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
                            'Ethernet1/2.115': {
                                'name': 'Ethernet1/2.115',
                                'status': 'protocol-up/link-up/admin-up',
                                'ipv4': '10.13.115.3',
                                'ipv4_subnet': '10.13.115.0/24',
                                'ipv6': {
                                    '2001:10:13:115::3/64': {
                                        'state': 'VALID',
                                    },
                                },
                                'ipv6_subnet': '2001:10:13:115::/64',
                                'ipv6_link_local_address': 'fe80::5c00:80ff:fe02:7',
                                'authentication': {
                                    'level_1': {
                                        'auth_check': 'set',
                                    },
                                    'level_2': {
                                        'auth_check': 'set',
                                    },
                                },
                                'index': '0x0003',
                                'local_circuit_id': '0x02',
                                'circuit_type': 'L1-2',
                                'bfd_ipv4': 'locally disabled',
                                'bfd_ipv6': 'locally disabled',
                                'mtr': 'enabled',
                                'mtu': 1500,
                                'lsp_interval_ms': 33,
                                'levels': {
                                    '1': {
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
                                    '2': {
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
                                    '0': {
                                        'level': {
                                            '1': {
                                                'metric': '40',
                                                'metric_cfg': 'no',
                                                'fwdng': 'UP',
                                                'ipv4_mt': 'UP',
                                                'ipv4_cfg': 'yes',
                                                'ipv6_mt': 'DN',
                                                'ipv6_cfg': 'yes',
                                            },
                                            '2': {
                                                'metric': '40',
                                                'metric_cfg': 'no',
                                                'fwdng': 'UP',
                                                'ipv4_mt': 'UP',
                                                'ipv4_cfg': 'yes',
                                                'ipv6_mt': 'DN',
                                                'ipv6_cfg': 'yes',
                                            },
                                        },
                                    },
                                    '2': {
                                        'level': {
                                            '1': {
                                                'metric': '40',
                                                'metric_cfg': 'no',
                                                'fwdng': 'UP',
                                                'ipv4_mt': 'DN',
                                                'ipv4_cfg': 'no',
                                                'ipv6_mt': 'UP',
                                                'ipv6_cfg': 'yes',
                                            },
                                            '2': {
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
                },
            },
        },
    }
    golden_output = {'execute.return_value': '''\
        R3_nx# show isis interface vrf default
        IS-IS process: test VRF: default
        loopback0, Interface status: protocol-up/link-up/admin-up
        IP address: 10.36.3.3, IP subnet: 10.36.3.3/32
        IPv6 address:
            2001:10:13:115::3/64 [VALID]
            2001:10:13:115::33/64 [VALID]
            2001:10::33/48 [VALID]
            2001:3:3:3:3::/128 [VALID]
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
        1              40     40     10 Inactive      10   3       00:00:04
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

    golden_parsed_output1 = {
        "instance": {
            "test": {
                "vrf": {
                    "default": {
                        "interfaces": {
                            "Ethernet1/1": {
                                "name": "Ethernet1/1",
                                "status": "protocol-up/link-up/admin-up",
                                "ipv4": "10.5.7.7",
                                "ipv4_subnet": "10.5.7.0/24",
                                "ipv6": {
                                    "2001:db8:10:5:7::7/64": {
                                        "state": "VALID"
                                    }
                                },
                                "ipv6_subnet": "2001:db8:10:5::/64",
                                "ipv6_link_local_address": "fe80::5c00:40ff:fe06:7",
                                "authentication": {
                                    "level_1": {
                                        "auth_check": "set"
                                    },
                                    "level_2": {
                                        "auth_check": "set"
                                    }
                                },
                                "index": "0x0002",
                                "local_circuit_id": "0x01",
                                "circuit_type": "L1-2",
                                "bfd_ipv4": "locally disabled",
                                "bfd_ipv6": "locally disabled",
                                "mtr": "enabled",
                                "passive": "level-1-2",
                                "mtu": 1500,
                                "lsp_interval_ms": 33,
                                "levels": {
                                    "1": {
                                        "metric_0": "40",
                                        "metric_2": "40",
                                        "csnp": "10",
                                        "next_csnp": "Inactive",
                                        "hello": "10",
                                        "multi": "3",
                                        "next_iih": "Inactive",
                                        "adjs": "0",
                                        "adjs_up": "0",
                                        "pri": "64",
                                        "circuit_id": "0000.0000.0000.00",
                                        "since": "2w2d"
                                    },
                                    "2": {
                                        "metric_0": "40",
                                        "metric_2": "40",
                                        "csnp": "10",
                                        "next_csnp": "Inactive",
                                        "hello": "10",
                                        "multi": "3",
                                        "next_iih": "Inactive",
                                        "adjs": "0",
                                        "adjs_up": "0",
                                        "pri": "64",
                                        "circuit_id": "0000.0000.0000.00",
                                        "since": "2w2d"
                                    }
                                },
                                "topologies": {
                                    "0": {
                                        "level": {
                                            "1": {
                                                "metric": "40",
                                                "metric_cfg": "no",
                                                "fwdng": "UP",
                                                "ipv4_mt": "DN",
                                                "ipv4_cfg": "yes",
                                                "ipv6_mt": "DN",
                                                "ipv6_cfg": "yes"
                                            },
                                            "2": {
                                                "metric": "40",
                                                "metric_cfg": "no",
                                                "fwdng": "UP",
                                                "ipv4_mt": "DN",
                                                "ipv4_cfg": "yes",
                                                "ipv6_mt": "DN",
                                                "ipv6_cfg": "yes"
                                            }
                                        }
                                    },
                                    "2": {
                                        "level": {
                                            "1": {
                                                "metric": "40",
                                                "metric_cfg": "no",
                                                "fwdng": "UP",
                                                "ipv4_mt": "DN",
                                                "ipv4_cfg": "no",
                                                "ipv6_mt": "DN",
                                                "ipv6_cfg": "yes"
                                            },
                                            "2": {
                                                "metric": "40",
                                                "metric_cfg": "no",
                                                "fwdng": "UP",
                                                "ipv4_mt": "DN",
                                                "ipv4_cfg": "no",
                                                "ipv6_mt": "DN",
                                                "ipv6_cfg": "yes"
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
    golden_output1 = {'execute.return_value': '''\
        show isis interface
        IS-IS process: test VRF: default
        Ethernet1/1, Interface status: protocol-up/link-up/admin-up
          IP address: 10.5.7.7, IP subnet: 10.5.7.0/24
          IPv6 address:
            2001:db8:10:5:7::7/64 [VALID]
          IPv6 subnet:  2001:db8:10:5::/64
          IPv6 link-local address: fe80::5c00:40ff:fe06:7
          Level1
            No auth type and keychain
            Auth check set
          Level2
            No auth type and keychain
            Auth check set
          Index: 0x0002, Local Circuit ID: 0x01, Circuit Type: L1-2
          BFD IPv4 is locally disabled for Interface Ethernet1/1
          BFD IPv6 is locally disabled for Interface Ethernet1/1
          MTR is enabled
          Passive level: level-1-2
          LSP interval: 33 ms, MTU: 1500
          Level   Metric-0   Metric-2   CSNP  Next CSNP  Hello   Multi   Next IIH
          1              40     40     10 Inactive      10   3       Inactive
          2              40     40     10 Inactive      10   3       Inactive
          Level  Adjs   AdjsUp Pri  Circuit ID         Since
          1         0        0  64  0000.0000.0000.00  2w2d
          2         0        0  64  0000.0000.0000.00  2w2d
          Topologies enabled:
            L  MT  Metric  MetricCfg  Fwdng IPV4-MT  IPV4Cfg  IPV6-MT  IPV6Cfg
            1  0        40      no   UP    DN       yes      DN       yes
            1  2        40      no   UP    DN       no       DN       yes
            2  0        40      no   UP    DN       yes      DN       yes
            2  2        40      no   UP    DN       no       DN       yes
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIsisInterface(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowIsisInterface(device=self.device)
        parsed_output = obj.parse(vrf='default')
        self.assertEqual(parsed_output, self.golden_parsed_output)
    
    def test_golden1(self):
        self.device = Mock(**self.golden_output1)
        obj = ShowIsisInterface(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)


class TestShowIsisSpfLogDetail(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    maxDiff = None

    golden_parsed_output = {
        'instance': {
            'test': {
                'vrf': {
                    'default': {
                        'topology': {
                            '0': {
                                'total_num_of_spf_calc': 362685,
                                'log_entry': {
                                    'current': 20,
                                    'max': 20,
                                },
                                'entrys': {
                                    '01': {
                                        'ago': '00:01:23',
                                        'date': 'Tue Oct 22 18:33:26 2019',
                                        'level': {
                                            1: {
                                                'instance': '0x0002C453',
                                                'init': 0.000728,
                                                'spf': 0.000813,
                                                'is_update': 0.00016,
                                                'urib_update': 0.00052,
                                                'total': 0.002374,
                                                'node': 4,
                                                'count': 6,
                                                'changed': 0,
                                                'reason': 'New adj R2_xr on Ethernet1/1.115',
                                            },
                                        },
                                    },
                                    '02': {
                                        'ago': '00:01:18',
                                        'date': 'Tue Oct 22 18:33:31 2019',
                                        'level': {
                                            2: {
                                                'instance': '0x0002C458',
                                                'init': 0.000878,
                                                'spf': 0.000771,
                                                'is_update': 0.000127,
                                                'urib_update': 0.000375,
                                                'total': 0.002283,
                                                'node': 4,
                                                'count': 6,
                                                'changed': 0,
                                                'reason': 'New adj R1_xe on Ethernet1/2.115',
                                            },
                                        },
                                    },
                                },
                            },
                            '2': {
                                'total_num_of_spf_calc': 362754,
                                'log_entry': {
                                    'current': 4,
                                    'max': 4,
                                },
                                'entrys': {
                                    '01': {
                                        'ago': '00:01:20',
                                        'date': 'Tue Oct 22 18:33:29 2019',
                                        'level': {
                                            1: {
                                                'instance': '0x0002C476',
                                                'init': 0.000681,
                                                'spf': 0.001235,
                                                'is_update': 0.000155,
                                                'urib_update': 0.000713,
                                                'total': 0.002985,
                                                'node': 4,
                                                'count': 5,
                                                'changed': 0,
                                                'reason': 'New adj R2_xr on Ethernet1/1.115',
                                            },
                                        },
                                    },
                                    '02': {
                                        'ago': '00:01:17',
                                        'date': 'Tue Oct 22 18:33:32 2019',
                                        'level': {
                                            2: {
                                                'instance': '0x0002C47A',
                                                'init': 0.000891,
                                                'spf': 0.00138,
                                                'is_update': 0.000291,
                                                'urib_update': 0.00053,
                                                'total': 0.003275,
                                                'node': 4,
                                                'count': 6,
                                                'changed': 0,
                                                'reason': 'New adj R1_xe on Ethernet1/2.115',
                                            },
                                        },
                                    },
                                    '03': {
                                        'ago': '00:01:12',
                                        'date': 'Tue Oct 22 18:33:37 2019',
                                        'level': {
                                            1: {
                                                'instance': '0x0002C477',
                                                'init': 0.001086,
                                                'spf': 0.000931,
                                                'is_update': 0.0002,
                                                'urib_update': 0.001112,
                                                'total': 0.003581,
                                                'node': 4,
                                                'count': 6,
                                                'changed': 0,
                                                'reason': 'New adj R1_xe on Ethernet1/2.115',
                                            },
                                        },
                                    },
                                    '04': {
                                        'ago': '00:01:09',
                                        'date': 'Tue Oct 22 18:33:40 2019',
                                        'level': {
                                            2: {
                                                'instance': '0x0002C47B',
                                                'init': 0.001284,
                                                'spf': 0.001047,
                                                'is_update': 0.000209,
                                                'urib_update': 0.000336,
                                                'total': 0.003068,
                                                'node': 4,
                                                'count': 6,
                                                'changed': 0,
                                                'reason': 'New adj R2_xr on Ethernet1/1.115',
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                    'VRF1': {
                        'topology': {
                            '0': {
                                'total_num_of_spf_calc': 361971,
                                'log_entry': {
                                    'current': 3,
                                    'max': 3,
                                },
                                'entrys': {
                                    '01': {
                                        'ago': '00:01:24',
                                        'date': 'Tue Oct 22 18:33:25 2019',
                                        'level': {
                                            2: {
                                                'instance': '0x0002C2F5',
                                                'init': 0.000793,
                                                'spf': 0.000268,
                                                'is_update': 7.8e-05,
                                                'urib_update': 0.000395,
                                                'total': 0.001709,
                                                'node': 2,
                                                'count': 3,
                                                'changed': 0,
                                                'reason': 'New adj R1_xe on Ethernet1/2.415',
                                            },
                                        },
                                    },
                                    '02': {
                                        'ago': '00:01:19',
                                        'date': 'Tue Oct 22 18:33:30 2019',
                                        'level': {
                                            1: {
                                                'instance': '0x0002C2EC',
                                                'init': 0.000547,
                                                'spf': 0.000655,
                                                'is_update': 9.9e-05,
                                                'urib_update': 0.000507,
                                                'total': 0.001968,
                                                'node': 2,
                                                'count': 3,
                                                'changed': 0,
                                                'reason': 'New adj R1_xe on Ethernet1/2.415',
                                            },
                                        },
                                    },
                                    '03': {
                                        'ago': '00:01:15',
                                        'date': 'Tue Oct 22 18:33:34 2019',
                                        'level': {
                                            2: {
                                                'instance': '0x0002C2F6',
                                                'init': 0.000728,
                                                'spf': 0.0002,
                                                'is_update': 6.3e-05,
                                                'urib_update': 0.000298,
                                                'total': 0.001445,
                                                'node': 2,
                                                'count': 3,
                                                'changed': 0,
                                                'reason': 'New adj R1_xe on Ethernet1/2.415',
                                            },
                                        },
                                    },
                                },
                            },
                            '2': {
                                'total_num_of_spf_calc': 362019,
                                'log_entry': {
                                    'current': 3,
                                    'max': 3,
                                },
                                'entrys': {
                                    '01': {
                                        'ago': '00:01:25',
                                        'date': 'Tue Oct 22 18:33:24 2019',
                                        'level': {
                                            2: {
                                                'instance': '0x0002C305',
                                                'init': 0.000499,
                                                'spf': 0.000217,
                                                'is_update': 6.4e-05,
                                                'urib_update': 0.000208,
                                                'total': 0.001116,
                                                'node': 2,
                                                'count': 3,
                                                'changed': 0,
                                                'reason': 'New adj R1_xe on Ethernet1/2.415',
                                            },
                                        },
                                    },
                                    '02': {
                                        'ago': '00:01:21',
                                        'date': 'Tue Oct 22 18:33:29 2019',
                                        'level': {
                                            1: {
                                                'instance': '0x0002C30C',
                                                'init': 0.001635,
                                                'spf': 0.000398,
                                                'is_update': 8.3e-05,
                                                'urib_update': 0.000547,
                                                'total': 0.002902,
                                                'node': 2,
                                                'count': 3,
                                                'changed': 0,
                                                'reason': 'New adj R1_xe on Ethernet1/2.415',
                                            },
                                        },
                                    },
                                    '03': {
                                        'ago': '00:01:16',
                                        'date': 'Tue Oct 22 18:33:33 2019',
                                        'level': {
                                            2: {
                                                'instance': '0x0002C306',
                                                'init': 0.000615,
                                                'spf': 0.000236,
                                                'is_update': 6.4e-05,
                                                'urib_update': 0.000219,
                                                'total': 0.001268,
                                                'node': 2,
                                                'count': 3,
                                                'changed': 0,
                                                'reason': 'New adj R1_xe on Ethernet1/2.415',
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
        R3_nx# show isis spf-log detail vrf all
        IS-IS Process: test SPF information VRF: default
        SPF log for Topology 0
        Total number of SPF calculations: 362685

        Log entry (current/max): 20/20
        Log entry: 01, Ago: 00:01:23, Date: Tue Oct 22 18:33:26 2019
        Level  Instance    Init      SPF       IS Update  URIB Update  Total
        1      0x0002C453  0.000728  0.000813  0.000160   0.000520     0.002374
        Level  Node Count   Changed  Reason
        1         4     6         0  New adj R2_xr on Ethernet1/1.115

        Log entry: 02, Ago: 00:01:18, Date: Tue Oct 22 18:33:31 2019
        Level  Instance    Init      SPF       IS Update  URIB Update  Total
        2      0x0002C458  0.000878  0.000771  0.000127   0.000375     0.002283
        Level  Node Count   Changed  Reason
        2         4     6         0  New adj R1_xe on Ethernet1/2.115

        SPF log for Topology 2
        Total number of SPF calculations: 362754

        Log entry (current/max): 4/4
        Log entry: 01, Ago: 00:01:20, Date: Tue Oct 22 18:33:29 2019
        Level  Instance    Init      SPF       IS Update  URIB Update  Total
        1      0x0002C476  0.000681  0.001235  0.000155   0.000713     0.002985
        Level  Node Count   Changed  Reason
        1         4     5         0  New adj R2_xr on Ethernet1/1.115

        Log entry: 02, Ago: 00:01:17, Date: Tue Oct 22 18:33:32 2019
        Level  Instance    Init      SPF       IS Update  URIB Update  Total
        2      0x0002C47A  0.000891  0.001380  0.000291   0.000530     0.003275
        Level  Node Count   Changed  Reason
        2         4     6         0  New adj R1_xe on Ethernet1/2.115

        Log entry: 03, Ago: 00:01:12, Date: Tue Oct 22 18:33:37 2019
        Level  Instance    Init      SPF       IS Update  URIB Update  Total
        1      0x0002C477  0.001086  0.000931  0.000200   0.001112     0.003581
        Level  Node Count   Changed  Reason
        1         4     6         0  New adj R1_xe on Ethernet1/2.115

        Log entry: 04, Ago: 00:01:09, Date: Tue Oct 22 18:33:40 2019
        Level  Instance    Init      SPF       IS Update  URIB Update  Total
        2      0x0002C47B  0.001284  0.001047  0.000209   0.000336     0.003068
        Level  Node Count   Changed  Reason
        2         4     6         0  New adj R2_xr on Ethernet1/1.115

        IS-IS Process: test SPF information VRF: VRF1
        SPF log for Topology 0
        Total number of SPF calculations: 361971

        Log entry (current/max): 3/3
        Log entry: 01, Ago: 00:01:24, Date: Tue Oct 22 18:33:25 2019
        Level  Instance    Init      SPF       IS Update  URIB Update  Total
        2      0x0002C2F5  0.000793  0.000268  0.000078   0.000395     0.001709
        Level  Node Count   Changed  Reason
        2         2     3         0  New adj R1_xe on Ethernet1/2.415

        Log entry: 02, Ago: 00:01:19, Date: Tue Oct 22 18:33:30 2019
        Level  Instance    Init      SPF       IS Update  URIB Update  Total
        1      0x0002C2EC  0.000547  0.000655  0.000099   0.000507     0.001968
        Level  Node Count   Changed  Reason
        1         2     3         0  New adj R1_xe on Ethernet1/2.415

        Log entry: 03, Ago: 00:01:15, Date: Tue Oct 22 18:33:34 2019
        Level  Instance    Init      SPF       IS Update  URIB Update  Total
        2      0x0002C2F6  0.000728  0.000200  0.000063   0.000298     0.001445
        Level  Node Count   Changed  Reason
        2         2     3         0  New adj R1_xe on Ethernet1/2.415

        SPF log for Topology 2
        Total number of SPF calculations: 362019

        Log entry (current/max): 3/3
        Log entry: 01, Ago: 00:01:25, Date: Tue Oct 22 18:33:24 2019
        Level  Instance    Init      SPF       IS Update  URIB Update  Total
        2      0x0002C305  0.000499  0.000217  0.000064   0.000208     0.001116
        Level  Node Count   Changed  Reason
        2         2     3         0  New adj R1_xe on Ethernet1/2.415

        Log entry: 02, Ago: 00:01:21, Date: Tue Oct 22 18:33:29 2019
        Level  Instance    Init      SPF       IS Update  URIB Update  Total
        1      0x0002C30C  0.001635  0.000398  0.000083   0.000547     0.002902
        Level  Node Count   Changed  Reason
        1         2     3         0  New adj R1_xe on Ethernet1/2.415

        Log entry: 03, Ago: 00:01:16, Date: Tue Oct 22 18:33:33 2019
        Level  Instance    Init      SPF       IS Update  URIB Update  Total
        2      0x0002C306  0.000615  0.000236  0.000064   0.000219     0.001268
        Level  Node Count   Changed  Reason
        2         2     3         0  New adj R1_xe on Ethernet1/2.415

    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIsisSpfLogDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowIsisSpfLogDetail(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output,self.golden_parsed_output)


class TestShowIsisHostname(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    maxDiff = None

    golden_parsed_output = {
        'instance': {
            'test': {
                'vrf': {
                    'VRF1': {
                        'hostname_db': {
                            'hostname': {
                                '3333.33ff.6666': {
                                    'hostname': 'R3_nx',
                                    'level': [1],
                                    'local_router': True,
                                },
                            },
                        },
                    },
                    'default': {
                        'hostname_db': {
                            'hostname': {
                                '1111.11ff.2222': {
                                    'hostname': 'R1_ios',
                                    'level': [1],
                                },
                                '2222.22ff.4444': {
                                    'hostname': 'R2_xr',
                                    'level': [1],
                                },
                                '3333.33ff.6666': {
                                    'hostname': 'R3_nx',
                                    'level': [1],
                                    'local_router': True,
                                },
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
        1      1111.11ff.2222  R1_ios
        1      2222.22ff.4444  R2_xr
        1      3333.33ff.6666* R3_nx

        IS-IS Process: test dynamic hostname table VRF: VRF1
        Level  System ID       Dynamic hostname
        1      3333.33ff.6666* R3_nx
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIsisHostname(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowIsisHostname(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output,self.golden_parsed_output)

class TestShowIsisHostnameDetail(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    maxDiff = None

    golden_parsed_output = {
        'instance': {
            'test': {
                'vrf': {
                    'VRF1': {
                        'hostname_db': {
                            'hostname': {
                                '1111.11ff.2222': {
                                    'hostname': 'R1_ios',
                                    'level': [1],
                                },
                                '2222.22ff.4444.00-00': {
                                    'hostname': 'R2',
                                    'level': [2],
                                },
                                '3333.33ff.6666': {
                                    'hostname': 'R3_nx',
                                    'level': [1],
                                    'local_router': True,
                                },
                                '7777.77ff.eeee.00-00': {
                                    'hostname': 'R7',
                                    'level': [1, 2],
                                    'local_router': True,
                                },
                            },
                        },
                    },
                    'default': {
                        'hostname_db': {
                            'hostname': {
                                '2222.22ff.4444.00-00': {
                                    'hostname': 'R2',
                                    'level': [2],
                                },
                                '3333.33ff.6666.00-00': {
                                    'hostname': 'R3',
                                    'level': [1, 2],
                                },
                                '4444.44ff.8888.00-00': {
                                    'hostname': 'R4',
                                    'level': [1],
                                },
                                '5555.55ff.aaaa.00-00': {
                                    'hostname': 'R5',
                                    'level': [1, 2],
                                },
                                '6666.66ff.cccc.00-00': {
                                    'hostname': 'R6',
                                    'level': [1],
                                },
                                '7777.77ff.eeee.00-00': {
                                    'hostname': 'R7',
                                    'level': [1, 2],
                                    'local_router': True,
                                },
                                '8888.88ff.1111.00-00': {
                                    'hostname': 'R8',
                                    'level': [2],
                                },
                                '9999.99ff.3333.00-00': {
                                    'hostname': 'R9',
                                    'level': [2],
                                },
                            },
                        },
                    },
                },
            },
        },
    }

    golden_output = {'execute.return_value': '''\
        IS-IS Process: test dynamic hostname table VRF: default
        Level  LSP ID                Dynamic hostname
        2      2222.22ff.4444.00-00  R2
        1      3333.33ff.6666.00-00  R3
        2      3333.33ff.6666.00-00  R3
        1      4444.44ff.8888.00-00  R4
        1      5555.55ff.aaaa.00-00  R5
        2      5555.55ff.aaaa.00-00  R5
        1      6666.66ff.cccc.00-00  R6
        1      7777.77ff.eeee.00-00* R7
        2      7777.77ff.eeee.00-00* R7
        2      8888.88ff.1111.00-00  R8
        2      9999.99ff.3333.00-00  R9

        IS-IS Process: test dynamic hostname table VRF: VRF1
        Level  LSP ID                Dynamic hostname
        2      2222.22ff.4444.00-00  R2
        1      7777.77ff.eeee.00-00* R7
        2      7777.77ff.eeee.00-00* R7
        1      1111.11ff.2222  R1_ios
        1      3333.33ff.6666* R3_nx
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIsisHostnameDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowIsisHostnameDetail(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output,self.golden_parsed_output)

class TestShowIsisAdjacency(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    maxDiff = None

    golden_parsed_output = {
        'instance': {
            'test': {
                'vrf': {
                    'default': {
                        'interfaces': {
                            'Ethernet1/1.115': {
                                'adjacencies': {
                                    'R2_xr': {
                                        'neighbor_snpa': {
                                            'fa16.3eff.4abd': {
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
                                            'fa16.3eff.0c11': {
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
                                    '2222.22ff.4444': {
                                        'neighbor_snpa': {
                                            'fa16.3eff.4abd': {
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
        },
    }
    golden_output = {'execute.return_value': '''\
        R3_nx# show isis adjacency vrf all
        IS-IS process: test VRF: default
        IS-IS adjacency database:
        Legend: '!': No AF level connectivity in given topology
        System ID       SNPA            Level  State  Hold Time  Interface
        R2_xr           fa16.3eff.4abd  1      UP     00:00:09   Ethernet1/1.115
        R2_xr           fa16.3eff.4abd  2      UP     00:00:07   Ethernet1/1.115
        R1_ios          fa16.3eff.0c11  1      UP     00:00:07   Ethernet1/2.115
        R1_ios          fa16.3eff.0c11  2      UP     00:00:10   Ethernet1/2.115

        IS-IS process: test VRF: VRF1
        IS-IS adjacency database:
        Legend: '!': No AF level connectivity in given topology
        System ID       SNPA            Level  State  Hold Time  Interface
        2222.22ff.4444  fa16.3eff.4abd  1      INIT   00:00:32   Ethernet1/1.415
        2222.22ff.4444  fa16.3eff.4abd  2      INIT   00:00:24   Ethernet1/1.415
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIsisAdjacency(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowIsisAdjacency(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output, self.golden_parsed_output)


class TestShowIsisDatabaseDetail(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    maxDiff = None

    golden_parsed_output = {
        'instance': {
            'test': {
                'vrf': {
                    'default': {
                        'level_db': {
                            1: {
                                'R1_xe.00-00': {
                                    'lsp_id': 'R1_xe.00-00',
                                    'sequence': '0x000007CD',
                                    'checksum': '0xAD22',
                                    'lifetime': 1199,
                                    'attach_bit': 0,
                                    'p_bit': 0,
                                    'overload_bit': 0,
                                    't_bit': 3,
                                    'lsp_status': '',
                                    'instance': '0x000007C9',
                                    'area_address': '49.0001',
                                    'nlpid': '0xCC 0x8E',
                                    'mt_entries': {
                                        0: {
                                            'att': 0,
                                            'ol': 0,
                                        },
                                        2: {
                                            'att': 0,
                                            'ol': 0,
                                        },
                                    },
                                    'hostname': 'R1_xe',
                                    'length': 5,
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
                                            'topo_id': 2,
                                        },
                                        'R1_xe.01': {
                                            'neighbor_id': 'R1_xe.01',
                                            'metric': 10,
                                            'topo_id': 2,
                                        },
                                    },
                                    'ip_address': '10.13.115.1',
                                    'extended_ip': {
                                        '10.12.115.0/24': {
                                            'metric': 10,
                                            'up_down': 'U',
                                            'sub_tlv_length': 1,
                                            'sub_tlv_type': 4,
                                        },
                                        '10.13.115.0/24': {
                                            'metric': 10,
                                            'up_down': 'U',
                                            'sub_tlv_length': 1,
                                            'sub_tlv_type': 4,
                                        },
                                    },
                                    'ipv6_address': '2001:10:13:115::1',
                                    'mt_ipv6_prefix': {
                                        '2001:10:12:115::/64': {
                                            'metric': 10,
                                            'topo_id': 2,
                                            'up_down': 'U',
                                            'ext_origin': 'I',
                                            'sub_tlv_length': 1,
                                            'sub_tlv_type': 4,
                                        },
                                        '2001:10:13:115::/64': {
                                            'metric': 10,
                                            'topo_id': 2,
                                            'up_down': 'U',
                                            'ext_origin': 'I',
                                            'sub_tlv_length': 1,
                                            'sub_tlv_type': 4,
                                        },
                                    },
                                    'digest_offset': 0,
                                },
                                'R1_xe.01-00': {
                                    'lsp_id': 'R1_xe.01-00',
                                    'sequence': '0x000007C7',
                                    'checksum': '0x14CA',
                                    'lifetime': 846,
                                    'attach_bit': 0,
                                    'p_bit': 0,
                                    'overload_bit': 0,
                                    't_bit': 3,
                                    'lsp_status': '',
                                    'instance': '0x000007C6',
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
                                    'digest_offset': 0,
                                },
                                'R1_xe.02-00': {
                                    'lsp_id': 'R1_xe.02-00',
                                    'sequence': '0x000007C7',
                                    'checksum': '0x0D6A',
                                    'lifetime': 852,
                                    'attach_bit': 0,
                                    'p_bit': 0,
                                    'overload_bit': 0,
                                    't_bit': 3,
                                    'lsp_status': '',
                                    'instance': '0x000007C6',
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
                                    'digest_offset': 0,
                                },
                                'R2_xr.00-00': {
                                    'lsp_id': 'R2_xr.00-00',
                                    'sequence': '0x000007C5',
                                    'checksum': '0x94D6',
                                    'lifetime': 887,
                                    'attach_bit': 0,
                                    'p_bit': 0,
                                    'overload_bit': 0,
                                    't_bit': 3,
                                    'lsp_status': '',
                                    'instance': '0x000007BD',
                                    'area_address': '49.0001',
                                    'nlpid': '0xCC 0x8E',
                                    'ip_address': '10.16.2.2',
                                    'extended_ip': {
                                        '10.16.2.2/32': {
                                            'metric': 10,
                                            'up_down': 'U',
                                            'sub_tlv_length': 1,
                                            'sub_tlv_type': 4,
                                        },
                                        '10.12.115.0/24': {
                                            'metric': 10,
                                            'up_down': 'U',
                                            'sub_tlv_length': 1,
                                            'sub_tlv_type': 4,
                                        },
                                        '10.23.115.0/24': {
                                            'metric': 10,
                                            'up_down': 'U',
                                            'sub_tlv_length': 1,
                                            'sub_tlv_type': 4,
                                        },
                                    },
                                    'hostname': 'R2_xr',
                                    'length': 5,
                                    'ipv6_address': '2001:2:2:2::2',
                                    'mt_ipv6_prefix': {
                                        '2001:2:2:2::2/128': {
                                            'metric': 10,
                                            'topo_id': 2,
                                            'up_down': 'U',
                                            'ext_origin': 'I',
                                            'sub_tlv_length': 1,
                                            'sub_tlv_type': 4,
                                        },
                                        '2001:10:12:115::/64': {
                                            'metric': 10,
                                            'topo_id': 2,
                                            'up_down': 'U',
                                            'ext_origin': 'I',
                                            'sub_tlv_length': 1,
                                            'sub_tlv_type': 4,
                                        },
                                        '2001:10:23:115::/64': {
                                            'metric': 10,
                                            'topo_id': 2,
                                            'up_down': 'U',
                                            'ext_origin': 'I',
                                            'sub_tlv_length': 1,
                                            'sub_tlv_type': 4,
                                        },
                                    },
                                    'mt_entries': {
                                        0: {
                                            'att': 0,
                                            'ol': 0,
                                        },
                                        2: {
                                            'att': 0,
                                            'ol': 0,
                                        },
                                    },
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
                                    'mt_is_neighbor': {
                                        'R2_xr.03': {
                                            'neighbor_id': 'R2_xr.03',
                                            'metric': 10,
                                            'topo_id': 2,
                                        },
                                    },
                                    'digest_offset': 0,
                                },
                                'R2_xr.03-00': {
                                    'lsp_id': 'R2_xr.03-00',
                                    'sequence': '0x000007C6',
                                    'checksum': '0x86AC',
                                    'lifetime': 594,
                                    'attach_bit': 0,
                                    'p_bit': 0,
                                    'overload_bit': 0,
                                    't_bit': 3,
                                    'lsp_status': '',
                                    'instance': '0x000007C5',
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
                                    'digest_offset': 0,
                                },
                                'R3_nx.00-00': {
                                    'lsp_id': 'R3_nx.00-00',
                                    'sequence': '0x00000B05',
                                    'checksum': '0x7FA7',
                                    'lifetime': 653,
                                    'attach_bit': 0,
                                    'p_bit': 0,
                                    'overload_bit': 0,
                                    't_bit': 3,
                                    'lsp_status': '*',
                                    'instance': '0x00000B05',
                                    'area_address': '49.0001',
                                    'nlpid': '0xCC 0x8E',
                                    'router_id': '10.36.3.3',
                                    'ip_address': '10.36.3.3',
                                    'mt_entries': {
                                        2: {
                                            'att': 0,
                                            'ol': 0,
                                        },
                                        0: {
                                            'att': 0,
                                            'ol': 0,
                                        },
                                    },
                                    'hostname': 'R3_nx',
                                    'length': 5,
                                    'mt_is_neighbor': {
                                        'R3_nx.00': {
                                            'neighbor_id': 'R1_xe.02',
                                            'metric': 40,
                                            'topo_id': 2,
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
                                    'extended_ip': {
                                        '10.36.3.3/32': {
                                            'metric': 1,
                                            'up_down': 'U',
                                        },
                                        '10.13.115.0/24': {
                                            'metric': 40,
                                            'up_down': 'U',
                                        },
                                        '10.23.115.0/24': {
                                            'metric': 40,
                                            'up_down': 'U',
                                        },
                                    },
                                    'mt_ipv6_prefix': {
                                        '2001:3:3:3::3/128': {
                                            'metric': 1,
                                            'topo_id': 2,
                                            'up_down': 'U',
                                            'ext_origin': 'I',
                                        },
                                        '2001:10:13:115::/64': {
                                            'metric': 40,
                                            'topo_id': 2,
                                            'up_down': 'U',
                                            'ext_origin': 'I',
                                        },
                                        '2001:10:23:115::/64': {
                                            'metric': 40,
                                            'topo_id': 2,
                                            'up_down': 'U',
                                            'ext_origin': 'I',
                                        },
                                    },
                                    'digest_offset': 0,
                                },
                            },
                            2: {
                                'R1_xe.00-00': {
                                    'lsp_id': 'R1_xe.00-00',
                                    'sequence': '0x000007C9',
                                    'checksum': '0xBB89',
                                    'lifetime': 1087,
                                    'attach_bit': 0,
                                    'p_bit': 0,
                                    'overload_bit': 0,
                                    't_bit': 3,
                                    'lsp_status': '',
                                    'instance': '0x000007C4',
                                    'area_address': '49.0001',
                                    'nlpid': '0xCC 0x8E',
                                    'mt_entries': {
                                        0: {
                                            'att': 0,
                                            'ol': 0,
                                        },
                                        2: {
                                            'att': 0,
                                            'ol': 0,
                                        },
                                    },
                                    'hostname': 'R1_xe',
                                    'length': 5,
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
                                            'topo_id': 2,
                                        },
                                        'R1_xe.01': {
                                            'neighbor_id': 'R1_xe.01',
                                            'metric': 10,
                                            'topo_id': 2,
                                        },
                                    },
                                    'ip_address': '10.13.115.1',
                                    'extended_ip': {
                                        '10.12.115.0/24': {
                                            'metric': 10,
                                            'up_down': 'U',
                                            'sub_tlv_length': 1,
                                            'sub_tlv_type': 4,
                                        },
                                        '10.13.115.0/24': {
                                            'metric': 10,
                                            'up_down': 'U',
                                            'sub_tlv_length': 1,
                                            'sub_tlv_type': 4,
                                        },
                                        '10.23.115.0/24': {
                                            'metric': 20,
                                            'up_down': 'U',
                                            'sub_tlv_length': 1,
                                            'sub_tlv_type': 4,
                                        },
                                    },
                                    'ipv6_address': '2001:10:13:115::1',
                                    'mt_ipv6_prefix': {
                                        '2001:10:12:115::/64': {
                                            'metric': 10,
                                            'topo_id': 2,
                                            'up_down': 'U',
                                            'ext_origin': 'I',
                                            'sub_tlv_length': 1,
                                            'sub_tlv_type': 4,
                                        },
                                        '2001:10:13:115::/64': {
                                            'metric': 10,
                                            'topo_id': 2,
                                            'up_down': 'U',
                                            'ext_origin': 'I',
                                            'sub_tlv_length': 1,
                                            'sub_tlv_type': 4,
                                        },
                                        '2001:10:23:115::/64': {
                                            'metric': 20,
                                            'topo_id': 2,
                                            'up_down': 'U',
                                            'ext_origin': 'I',
                                            'sub_tlv_length': 1,
                                            'sub_tlv_type': 4,
                                        },
                                    },
                                    'digest_offset': 0,
                                },
                                'R1_xe.01-00': {
                                    'lsp_id': 'R1_xe.01-00',
                                    'sequence': '0x000007C0',
                                    'checksum': '0x3A34',
                                    'lifetime': 1137,
                                    'attach_bit': 0,
                                    'p_bit': 0,
                                    'overload_bit': 0,
                                    't_bit': 3,
                                    'lsp_status': '',
                                    'instance': '0x000007BF',
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
                                    'digest_offset': 0,
                                },
                                'R1_xe.02-00': {
                                    'lsp_id': 'R1_xe.02-00',
                                    'sequence': '0x000007C8',
                                    'checksum': '0x23DB',
                                    'lifetime': 867,
                                    'attach_bit': 0,
                                    'p_bit': 0,
                                    'overload_bit': 0,
                                    't_bit': 3,
                                    'lsp_status': '',
                                    'instance': '0x000007C7',
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
                                    'digest_offset': 0,
                                },
                                'R2_xr.00-00': {
                                    'lsp_id': 'R2_xr.00-00',
                                    'sequence': '0x000007D1',
                                    'checksum': '0xE002',
                                    'lifetime': 813,
                                    'attach_bit': 0,
                                    'p_bit': 0,
                                    'overload_bit': 0,
                                    't_bit': 3,
                                    'lsp_status': '',
                                    'instance': '0x000007C9',
                                    'area_address': '49.0001',
                                    'nlpid': '0xCC 0x8E',
                                    'ip_address': '10.16.2.2',
                                    'extended_ip': {
                                        '10.16.2.2/32': {
                                            'metric': 10,
                                            'up_down': 'U',
                                            'sub_tlv_length': 1,
                                            'sub_tlv_type': 4,
                                        },
                                        '10.12.115.0/24': {
                                            'metric': 10,
                                            'up_down': 'U',
                                            'sub_tlv_length': 1,
                                            'sub_tlv_type': 4,
                                        },
                                        '10.23.115.0/24': {
                                            'metric': 10,
                                            'up_down': 'U',
                                            'sub_tlv_length': 1,
                                            'sub_tlv_type': 4,
                                        },
                                        '10.36.3.3/32': {
                                            'metric': 11,
                                            'up_down': 'U',
                                            'sub_tlv_length': 1,
                                            'sub_tlv_type': 4,
                                        },
                                        '10.13.115.0/24': {
                                            'metric': 20,
                                            'up_down': 'U',
                                            'sub_tlv_length': 1,
                                            'sub_tlv_type': 4,
                                        },
                                    },
                                    'hostname': 'R2_xr',
                                    'length': 5,
                                    'ipv6_address': '2001:2:2:2::2',
                                    'mt_ipv6_prefix': {
                                        '2001:2:2:2::2/128': {
                                            'metric': 10,
                                            'topo_id': 2,
                                            'up_down': 'U',
                                            'ext_origin': 'I',
                                            'sub_tlv_length': 1,
                                            'sub_tlv_type': 4,
                                        },
                                        '2001:10:12:115::/64': {
                                            'metric': 10,
                                            'topo_id': 2,
                                            'up_down': 'U',
                                            'ext_origin': 'I',
                                            'sub_tlv_length': 1,
                                            'sub_tlv_type': 4,
                                        },
                                        '2001:10:23:115::/64': {
                                            'metric': 10,
                                            'topo_id': 2,
                                            'up_down': 'U',
                                            'ext_origin': 'I',
                                            'sub_tlv_length': 1,
                                            'sub_tlv_type': 4,
                                        },
                                        '2001:3:3:3::3/128': {
                                            'metric': 11,
                                            'topo_id': 2,
                                            'up_down': 'U',
                                            'ext_origin': 'I',
                                            'sub_tlv_length': 1,
                                            'sub_tlv_type': 4,
                                        },
                                        '2001:10:13:115::/64': {
                                            'metric': 20,
                                            'topo_id': 2,
                                            'up_down': 'U',
                                            'ext_origin': 'I',
                                            'sub_tlv_length': 1,
                                            'sub_tlv_type': 4,
                                        },
                                    },
                                    'mt_entries': {
                                        0: {
                                            'att': 0,
                                            'ol': 0,
                                        },
                                        2: {
                                            'att': 0,
                                            'ol': 0,
                                        },
                                    },
                                    'extended_is_neighbor': {
                                        'R2_xr.03': {
                                            'neighbor_id': 'R2_xr.03',
                                            'metric': 10,
                                        },
                                        'R1_xe.01': {
                                            'neighbor_id': 'R1_xe.01',
                                            'metric': 10,
                                        },
                                    },
                                    'mt_is_neighbor': {
                                        'R1_xe.01': {
                                            'neighbor_id': 'R1_xe.01',
                                            'metric': 10,
                                            'topo_id': 2,
                                        },
                                    },
                                    'digest_offset': 0,
                                },
                                'R2_xr.03-00': {
                                    'lsp_id': 'R2_xr.03-00',
                                    'sequence': '0x000007C2',
                                    'checksum': '0x8EA8',
                                    'lifetime': 784,
                                    'attach_bit': 0,
                                    'p_bit': 0,
                                    'overload_bit': 0,
                                    't_bit': 3,
                                    'lsp_status': '',
                                    'instance': '0x000007C1',
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
                                    'digest_offset': 0,
                                },
                                'R3_nx.00-00': {
                                    'lsp_id': 'R3_nx.00-00',
                                    'sequence': '0x00000B05',
                                    'checksum': '0x7FA7',
                                    'lifetime': 1040,
                                    'attach_bit': 0,
                                    'p_bit': 0,
                                    'overload_bit': 0,
                                    't_bit': 3,
                                    'lsp_status': '*',
                                    'instance': '0x00000B05',
                                    'area_address': '49.0001',
                                    'nlpid': '0xCC 0x8E',
                                    'router_id': '10.36.3.3',
                                    'ip_address': '10.36.3.3',
                                    'mt_entries': {
                                        2: {
                                            'att': 0,
                                            'ol': 0,
                                        },
                                        0: {
                                            'att': 0,
                                            'ol': 0,
                                        },
                                    },
                                    'hostname': 'R3_nx',
                                    'length': 5,
                                    'mt_is_neighbor': {
                                        'R3_nx.00': {
                                            'neighbor_id': 'R1_xe.02',
                                            'metric': 40,
                                            'topo_id': 2,
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
                                    'extended_ip': {
                                        '10.36.3.3/32': {
                                            'metric': 1,
                                            'up_down': 'U',
                                        },
                                        '10.13.115.0/24': {
                                            'metric': 40,
                                            'up_down': 'U',
                                        },
                                        '10.23.115.0/24': {
                                            'metric': 40,
                                            'up_down': 'U',
                                        },
                                    },
                                    'mt_ipv6_prefix': {
                                        '2001:3:3:3::3/128': {
                                            'metric': 1,
                                            'topo_id': 2,
                                            'up_down': 'U',
                                            'ext_origin': 'I',
                                        },
                                        '2001:10:13:115::/64': {
                                            'metric': 40,
                                            'topo_id': 2,
                                            'up_down': 'U',
                                            'ext_origin': 'I',
                                        },
                                        '2001:10:23:115::/64': {
                                            'metric': 40,
                                            'topo_id': 2,
                                            'up_down': 'U',
                                            'ext_origin': 'I',
                                        },
                                    },
                                    'digest_offset': 0,
                                },
                            },
                        },
                    },
                    'VRF1': {
                        'level_db': {
                            1: {
                                'R1_xe.00-00': {
                                    'lsp_id': 'R1_xe.00-00',
                                    'sequence': '0x000007CA',
                                    'checksum': '0xC7FC',
                                    'lifetime': 616,
                                    'attach_bit': 0,
                                    'p_bit': 0,
                                    'overload_bit': 0,
                                    't_bit': 3,
                                    'lsp_status': '',
                                    'instance': '0x000007C6',
                                    'area_address': '49.0001',
                                    'nlpid': '0xCC 0x8E',
                                    'mt_entries': {
                                        0: {
                                            'att': 0,
                                            'ol': 0,
                                        },
                                        2: {
                                            'att': 0,
                                            'ol': 0,
                                        },
                                    },
                                    'hostname': 'R1_xe',
                                    'length': 5,
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
                                            'topo_id': 2,
                                        },
                                    },
                                    'ip_address': '10.13.115.1',
                                    'extended_ip': {
                                        '10.12.115.0/24': {
                                            'metric': 10,
                                            'up_down': 'U',
                                            'sub_tlv_length': 1,
                                            'sub_tlv_type': 4,
                                        },
                                        '10.13.115.0/24': {
                                            'metric': 10,
                                            'up_down': 'U',
                                            'sub_tlv_length': 1,
                                            'sub_tlv_type': 4,
                                        },
                                    },
                                    'ipv6_address': '2001:10:13:115::1',
                                    'mt_ipv6_prefix': {
                                        '2001:10:12:115::/64': {
                                            'metric': 10,
                                            'topo_id': 2,
                                            'up_down': 'U',
                                            'ext_origin': 'I',
                                            'sub_tlv_length': 1,
                                            'sub_tlv_type': 4,
                                        },
                                        '2001:10:13:115::/64': {
                                            'metric': 10,
                                            'topo_id': 2,
                                            'up_down': 'U',
                                            'ext_origin': 'I',
                                            'sub_tlv_length': 1,
                                            'sub_tlv_type': 4,
                                        },
                                    },
                                    'digest_offset': 0,
                                },
                                'R1_xe.02-00': {
                                    'lsp_id': 'R1_xe.02-00',
                                    'sequence': '0x000007C7',
                                    'checksum': '0x0D6A',
                                    'lifetime': 625,
                                    'attach_bit': 0,
                                    'p_bit': 0,
                                    'overload_bit': 0,
                                    't_bit': 3,
                                    'lsp_status': '',
                                    'instance': '0x000007C6',
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
                                    'digest_offset': 0,
                                },
                                'R3_nx.00-00': {
                                    'lsp_id': 'R3_nx.00-00',
                                    'sequence': '0x00000B09',
                                    'checksum': '0x68C0',
                                    'lifetime': 841,
                                    'attach_bit': 0,
                                    'p_bit': 0,
                                    'overload_bit': 0,
                                    't_bit': 3,
                                    'lsp_status': '*',
                                    'instance': '0x00000B09',
                                    'area_address': '49.0001',
                                    'nlpid': '0xCC 0x8E',
                                    'router_id': '10.36.3.3',
                                    'ip_address': '10.36.3.3',
                                    'mt_entries': {
                                        2: {
                                            'att': 0,
                                            'ol': 0,
                                        },
                                        0: {
                                            'att': 0,
                                            'ol': 0,
                                        },
                                    },
                                    'hostname': 'R3_nx',
                                    'length': 5,
                                    'mt_is_neighbor': {
                                        'R3_nx.00': {
                                            'neighbor_id': 'R1_xe.02',
                                            'metric': 40,
                                            'topo_id': 2,
                                        },
                                    },
                                    'extended_is_neighbor': {
                                        'R1_xe.02': {
                                            'neighbor_id': 'R1_xe.02',
                                            'metric': 40,
                                        },
                                    },
                                    'extended_ip': {
                                        '10.36.3.3/32': {
                                            'metric': 1,
                                            'up_down': 'U',
                                        },
                                        '10.13.115.0/24': {
                                            'metric': 40,
                                            'up_down': 'U',
                                        },
                                        '10.23.115.0/24': {
                                            'metric': 40,
                                            'up_down': 'U',
                                        },
                                    },
                                    'mt_ipv6_prefix': {
                                        '2001:3:3:3::3/128': {
                                            'metric': 1,
                                            'topo_id': 2,
                                            'up_down': 'U',
                                            'ext_origin': 'I',
                                        },
                                        '2001:10:13:115::/64': {
                                            'metric': 40,
                                            'topo_id': 2,
                                            'up_down': 'U',
                                            'ext_origin': 'I',
                                        },
                                        '2001:10:23:115::/64': {
                                            'metric': 40,
                                            'topo_id': 2,
                                            'up_down': 'U',
                                            'ext_origin': 'I',
                                        },
                                    },
                                    'digest_offset': 0,
                                },
                            },
                            2: {
                                'R1_xe.00-00': {
                                    'lsp_id': 'R1_xe.00-00',
                                    'sequence': '0x000007CB',
                                    'checksum': '0x25D3',
                                    'lifetime': 908,
                                    'attach_bit': 0,
                                    'p_bit': 0,
                                    'overload_bit': 0,
                                    't_bit': 3,
                                    'lsp_status': '',
                                    'instance': '0x000007C6',
                                    'area_address': '49.0001',
                                    'nlpid': '0xCC 0x8E',
                                    'mt_entries': {
                                        0: {
                                            'att': 0,
                                            'ol': 0,
                                        },
                                        2: {
                                            'att': 0,
                                            'ol': 0,
                                        },
                                    },
                                    'hostname': 'R1_xe',
                                    'length': 5,
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
                                            'topo_id': 2,
                                        },
                                    },
                                    'ip_address': '10.13.115.1',
                                    'extended_ip': {
                                        '10.12.115.0/24': {
                                            'metric': 10,
                                            'up_down': 'U',
                                            'sub_tlv_length': 1,
                                            'sub_tlv_type': 4,
                                        },
                                        '10.13.115.0/24': {
                                            'metric': 10,
                                            'up_down': 'U',
                                            'sub_tlv_length': 1,
                                            'sub_tlv_type': 4,
                                        },
                                        '10.23.115.0/24': {
                                            'metric': 50,
                                            'up_down': 'U',
                                            'sub_tlv_length': 1,
                                            'sub_tlv_type': 4,
                                        },
                                    },
                                    'ipv6_address': '2001:10:13:115::1',
                                    'mt_ipv6_prefix': {
                                        '2001:10:12:115::/64': {
                                            'metric': 10,
                                            'topo_id': 2,
                                            'up_down': 'U',
                                            'ext_origin': 'I',
                                            'sub_tlv_length': 1,
                                            'sub_tlv_type': 4,
                                        },
                                        '2001:10:13:115::/64': {
                                            'metric': 10,
                                            'topo_id': 2,
                                            'up_down': 'U',
                                            'ext_origin': 'I',
                                            'sub_tlv_length': 1,
                                            'sub_tlv_type': 4,
                                        },
                                        '2001:10:23:115::/64': {
                                            'metric': 50,
                                            'topo_id': 2,
                                            'up_down': 'U',
                                            'ext_origin': 'I',
                                            'sub_tlv_length': 1,
                                            'sub_tlv_type': 4,
                                        },
                                    },
                                    'digest_offset': 0,
                                },
                                'R1_xe.02-00': {
                                    'lsp_id': 'R1_xe.02-00',
                                    'sequence': '0x000007C6',
                                    'checksum': '0x27D9',
                                    'lifetime': 1174,
                                    'attach_bit': 0,
                                    'p_bit': 0,
                                    'overload_bit': 0,
                                    't_bit': 3,
                                    'lsp_status': '',
                                    'instance': '0x000007C5',
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
                                    'digest_offset': 0,
                                },
                                'R3_nx.00-00': {
                                    'lsp_id': 'R3_nx.00-00',
                                    'sequence': '0x00000B06',
                                    'checksum': '0x6EBD',
                                    'lifetime': 1136,
                                    'attach_bit': 0,
                                    'p_bit': 0,
                                    'overload_bit': 0,
                                    't_bit': 3,
                                    'lsp_status': '*',
                                    'instance': '0x00000B06',
                                    'area_address': '49.0001',
                                    'nlpid': '0xCC 0x8E',
                                    'router_id': '10.36.3.3',
                                    'ip_address': '10.36.3.3',
                                    'mt_entries': {
                                        2: {
                                            'att': 0,
                                            'ol': 0,
                                        },
                                        0: {
                                            'att': 0,
                                            'ol': 0,
                                        },
                                    },
                                    'hostname': 'R3_nx',
                                    'length': 5,
                                    'mt_is_neighbor': {
                                        'R3_nx.00': {
                                            'neighbor_id': 'R1_xe.02',
                                            'metric': 40,
                                            'topo_id': 2,
                                        },
                                    },
                                    'extended_is_neighbor': {
                                        'R1_xe.02': {
                                            'neighbor_id': 'R1_xe.02',
                                            'metric': 40,
                                        },
                                    },
                                    'extended_ip': {
                                        '10.36.3.3/32': {
                                            'metric': 1,
                                            'up_down': 'U',
                                        },
                                        '10.13.115.0/24': {
                                            'metric': 40,
                                            'up_down': 'U',
                                        },
                                        '10.23.115.0/24': {
                                            'metric': 40,
                                            'up_down': 'U',
                                        },
                                    },
                                    'mt_ipv6_prefix': {
                                        '2001:3:3:3::3/128': {
                                            'metric': 1,
                                            'topo_id': 2,
                                            'up_down': 'U',
                                            'ext_origin': 'I',
                                        },
                                        '2001:10:13:115::/64': {
                                            'metric': 40,
                                            'topo_id': 2,
                                            'up_down': 'U',
                                            'ext_origin': 'I',
                                        },
                                        '2001:10:23:115::/64': {
                                            'metric': 40,
                                            'topo_id': 2,
                                            'up_down': 'U',
                                            'ext_origin': 'I',
                                        },
                                    },
                                    'digest_offset': 0,
                                },
                            },
                        },
                    },
                },
            },
        },
    }
    golden_output = {'execute.return_value': '''\
        R3_nx# show isis database detail vrf all
        IS-IS Process: test LSP database VRF: default
        IS-IS Level-1 Link State Database
        LSPID                 Seq Number   Checksum  Lifetime   A/P/O/T
        R1_xe.00-00           0x000007CD   0xAD22    1199       0/0/0/3
            Instance      :  0x000007C9
            Area Address  :  49.0001
            NLPID         :  0xCC 0x8E
            MT TopoId     : TopoId:0 Att: 0 Ol: 0
                            TopoId:2 Att: 0 Ol: 0
            Hostname      :  R1_xe              Length : 5
            Extended IS   :  R1_xe.02           Metric : 10
            TopoId: 2
            MtExtend IS   :  R1_xe.02           Metric : 10
            Extended IS   :  R1_xe.01           Metric : 10
            TopoId: 2
            MtExtend IS   :  R1_xe.01           Metric : 10
            IP Address    :  10.13.115.1
            Extended IP   :     10.12.115.0/24  Metric : 10          (U)
            Unknown Sub-TLV      :  Length : 1  Type :   4
            Extended IP   :     10.13.115.0/24  Metric : 10          (U)
            Unknown Sub-TLV      :  Length : 1  Type :   4
            IPv6 Address  :  2001:10:13:115::1
            MT-IPv6 Prefx :  TopoId : 2
                            2001:10:12:115::/64  Metric : 10          (U/I)
            Unknown Sub-TLV      :  Length : 1  Type :   4
        2001:10:13:115::/64  Metric : 10          (U/I)
            Unknown Sub-TLV      :  Length : 1  Type :   4
            Digest Offset :  0
        R1_xe.01-00           0x000007C7   0x14CA    846        0/0/0/3
            Instance      :  0x000007C6
            Extended IS   :  R1_xe.00           Metric : 0
            Extended IS   :  R2_xr.00           Metric : 0
            Digest Offset :  0
        R1_xe.02-00           0x000007C7   0x0D6A    852        0/0/0/3
            Instance      :  0x000007C6
            Extended IS   :  R1_xe.00           Metric : 0
            Extended IS   :  R3_nx.00           Metric : 0
            Digest Offset :  0
        R2_xr.00-00           0x000007C5   0x94D6    887        0/0/0/3
            Instance      :  0x000007BD
            Area Address  :  49.0001
            NLPID         :  0xCC 0x8E
            IP Address    :  10.16.2.2
            Extended IP   :         10.16.2.2/32  Metric : 10          (U)
            Unknown Sub-TLV      :  Length : 1  Type :   4
            Extended IP   :     10.12.115.0/24  Metric : 10          (U)
            Unknown Sub-TLV      :  Length : 1  Type :   4
            Extended IP   :     10.23.115.0/24  Metric : 10          (U)
            Unknown Sub-TLV      :  Length : 1  Type :   4
            Hostname      :  R2_xr              Length : 5
            IPv6 Address  :  2001:2:2:2::2
            MT-IPv6 Prefx :  TopoId : 2
                            2001:2:2:2::2/128  Metric : 10          (U/I)
            Unknown Sub-TLV      :  Length : 1  Type :   4
        2001:10:12:115::/64  Metric : 10          (U/I)
            Unknown Sub-TLV      :  Length : 1  Type :   4
        2001:10:23:115::/64  Metric : 10          (U/I)
            Unknown Sub-TLV      :  Length : 1  Type :   4
            MT TopoId     : TopoId:0 Att: 0 Ol: 0
                            TopoId:2 Att: 0 Ol: 0
            Extended IS   :  R1_xe.01           Metric : 10
            Extended IS   :  R2_xr.03           Metric : 10
            TopoId: 2
            MtExtend IS   :  R1_xe.01           Metric : 10
                            R2_xr.03           Metric : 10
            Digest Offset :  0
        R2_xr.03-00           0x000007C6   0x86AC    594        0/0/0/3
            Instance      :  0x000007C5
            Extended IS   :  R2_xr.00           Metric : 0
            Extended IS   :  R3_nx.00           Metric : 0
            Digest Offset :  0
        R3_nx.00-00         * 0x00000B05   0x7FA7    653        0/0/0/3
            Instance      :  0x00000B05
            Area Address  :  49.0001
            NLPID         :  0xCC 0x8E
            Router ID     :  10.36.3.3
            IP Address    :  10.36.3.3
            MT TopoId     : TopoId:2 Att: 0 Ol: 0
                            TopoId:0 Att: 0 Ol: 0
            Hostname      :  R3_nx              Length : 5
            TopoId: 2
            MtExtend IS   :  R2_xr.03           Metric : 40
                            R1_xe.02           Metric : 40
            Extended IS   :  R2_xr.03           Metric : 40
            Extended IS   :  R1_xe.02           Metric : 40
            Extended IP   :         10.36.3.3/32  Metric : 1           (U)
            Extended IP   :     10.13.115.0/24  Metric : 40          (U)
            Extended IP   :     10.23.115.0/24  Metric : 40          (U)
            MT-IPv6 Prefx :  TopoId : 2
                            2001:3:3:3::3/128  Metric : 1           (U/I)
            MT-IPv6 Prefx :  TopoId : 2
                            2001:10:13:115::/64  Metric : 40          (U/I)
            MT-IPv6 Prefx :  TopoId : 2
                            2001:10:23:115::/64  Metric : 40          (U/I)
            Digest Offset :  0

        IS-IS Level-2 Link State Database
        LSPID                 Seq Number   Checksum  Lifetime   A/P/O/T
        R1_xe.00-00           0x000007C9   0xBB89    1087       0/0/0/3
            Instance      :  0x000007C4
            Area Address  :  49.0001
            NLPID         :  0xCC 0x8E
            MT TopoId     : TopoId:0 Att: 0 Ol: 0
                            TopoId:2 Att: 0 Ol: 0
            Hostname      :  R1_xe              Length : 5
            Extended IS   :  R1_xe.02           Metric : 10
            TopoId: 2
            MtExtend IS   :  R1_xe.02           Metric : 10
            Extended IS   :  R1_xe.01           Metric : 10
            TopoId: 2
            MtExtend IS   :  R1_xe.01           Metric : 10
            IP Address    :  10.13.115.1
            Extended IP   :     10.12.115.0/24  Metric : 10          (U)
            Unknown Sub-TLV      :  Length : 1  Type :   4
            Extended IP   :     10.13.115.0/24  Metric : 10          (U)
            Unknown Sub-TLV      :  Length : 1  Type :   4
            Extended IP   :     10.23.115.0/24  Metric : 20          (U)
            Unknown Sub-TLV      :  Length : 1  Type :   4
            IPv6 Address  :  2001:10:13:115::1
            MT-IPv6 Prefx :  TopoId : 2
                            2001:10:12:115::/64  Metric : 10          (U/I)
            Unknown Sub-TLV      :  Length : 1  Type :   4
        2001:10:13:115::/64  Metric : 10          (U/I)
            Unknown Sub-TLV      :  Length : 1  Type :   4
        2001:10:23:115::/64  Metric : 20          (U/I)
            Unknown Sub-TLV      :  Length : 1  Type :   4
            Digest Offset :  0
        R1_xe.01-00           0x000007C0   0x3A34    1137       0/0/0/3
            Instance      :  0x000007BF
            Extended IS   :  R1_xe.00           Metric : 0
            Extended IS   :  R2_xr.00           Metric : 0
            Digest Offset :  0
        R1_xe.02-00           0x000007C8   0x23DB    867        0/0/0/3
            Instance      :  0x000007C7
            Extended IS   :  R1_xe.00           Metric : 0
            Extended IS   :  R3_nx.00           Metric : 0
            Digest Offset :  0
        R2_xr.00-00           0x000007D1   0xE002    813        0/0/0/3
            Instance      :  0x000007C9
            Area Address  :  49.0001
            NLPID         :  0xCC 0x8E
            IP Address    :  10.16.2.2
            Extended IP   :         10.16.2.2/32  Metric : 10          (U)
            Unknown Sub-TLV      :  Length : 1  Type :   4
            Extended IP   :     10.12.115.0/24  Metric : 10          (U)
            Unknown Sub-TLV      :  Length : 1  Type :   4
            Extended IP   :     10.23.115.0/24  Metric : 10          (U)
            Unknown Sub-TLV      :  Length : 1  Type :   4
            Extended IP   :         10.36.3.3/32  Metric : 11          (U)
            Unknown Sub-TLV      :  Length : 1  Type :   4
            Extended IP   :     10.13.115.0/24  Metric : 20          (U)
            Unknown Sub-TLV      :  Length : 1  Type :   4
            Hostname      :  R2_xr              Length : 5
            IPv6 Address  :  2001:2:2:2::2
            MT-IPv6 Prefx :  TopoId : 2
                            2001:2:2:2::2/128  Metric : 10          (U/I)
            Unknown Sub-TLV      :  Length : 1  Type :   4
        2001:10:12:115::/64  Metric : 10          (U/I)
            Unknown Sub-TLV      :  Length : 1  Type :   4
        2001:10:23:115::/64  Metric : 10          (U/I)
            Unknown Sub-TLV      :  Length : 1  Type :   4
        2001:3:3:3::3/128  Metric : 11          (U/I)
            Unknown Sub-TLV      :  Length : 1  Type :   4
        2001:10:13:115::/64  Metric : 20          (U/I)
            Unknown Sub-TLV      :  Length : 1  Type :   4
            MT TopoId     : TopoId:0 Att: 0 Ol: 0
                            TopoId:2 Att: 0 Ol: 0
            Extended IS   :  R2_xr.03           Metric : 10
            Extended IS   :  R1_xe.01           Metric : 10
            TopoId: 2
            MtExtend IS   :  R2_xr.03           Metric : 10
                            R1_xe.01           Metric : 10
            Digest Offset :  0
        R2_xr.03-00           0x000007C2   0x8EA8    784        0/0/0/3
            Instance      :  0x000007C1
            Extended IS   :  R2_xr.00           Metric : 0
            Extended IS   :  R3_nx.00           Metric : 0
            Digest Offset :  0
        R3_nx.00-00         * 0x00000B05   0x7FA7    1040       0/0/0/3
            Instance      :  0x00000B05
            Area Address  :  49.0001
            NLPID         :  0xCC 0x8E
            Router ID     :  10.36.3.3
            IP Address    :  10.36.3.3
            MT TopoId     : TopoId:2 Att: 0 Ol: 0
                            TopoId:0 Att: 0 Ol: 0
            Hostname      :  R3_nx              Length : 5
            TopoId: 2
            MtExtend IS   :  R2_xr.03           Metric : 40
                            R1_xe.02           Metric : 40
            Extended IS   :  R2_xr.03           Metric : 40
            Extended IS   :  R1_xe.02           Metric : 40
            Extended IP   :         10.36.3.3/32  Metric : 1           (U)
            Extended IP   :     10.13.115.0/24  Metric : 40          (U)
            Extended IP   :     10.23.115.0/24  Metric : 40          (U)
            MT-IPv6 Prefx :  TopoId : 2
                            2001:3:3:3::3/128  Metric : 1           (U/I)
            MT-IPv6 Prefx :  TopoId : 2
                            2001:10:13:115::/64  Metric : 40          (U/I)
            MT-IPv6 Prefx :  TopoId : 2
                            2001:10:23:115::/64  Metric : 40          (U/I)
            Digest Offset :  0

        IS-IS Process: test LSP database VRF: VRF1
        IS-IS Level-1 Link State Database
        LSPID                 Seq Number   Checksum  Lifetime   A/P/O/T
        R1_xe.00-00           0x000007CA   0xC7FC    616        0/0/0/3
            Instance      :  0x000007C6
            Area Address  :  49.0001
            NLPID         :  0xCC 0x8E
            MT TopoId     : TopoId:0 Att: 0 Ol: 0
                            TopoId:2 Att: 0 Ol: 0
            Hostname      :  R1_xe              Length : 5
            Extended IS   :  R1_xe.02           Metric : 10
            TopoId: 2
            MtExtend IS   :  R1_xe.02           Metric : 10
            IP Address    :  10.13.115.1
            Extended IP   :     10.12.115.0/24  Metric : 10          (U)
            Unknown Sub-TLV      :  Length : 1  Type :   4
            Extended IP   :     10.13.115.0/24  Metric : 10          (U)
            Unknown Sub-TLV      :  Length : 1  Type :   4
            IPv6 Address  :  2001:10:13:115::1
            MT-IPv6 Prefx :  TopoId : 2
                            2001:10:12:115::/64  Metric : 10          (U/I)
            Unknown Sub-TLV      :  Length : 1  Type :   4
        2001:10:13:115::/64  Metric : 10          (U/I)
            Unknown Sub-TLV      :  Length : 1  Type :   4
            Digest Offset :  0
        R1_xe.02-00           0x000007C7   0x0D6A    625        0/0/0/3
            Instance      :  0x000007C6
            Extended IS   :  R1_xe.00           Metric : 0
            Extended IS   :  R3_nx.00           Metric : 0
            Digest Offset :  0
        R3_nx.00-00         * 0x00000B09   0x68C0    841        0/0/0/3
            Instance      :  0x00000B09
            Area Address  :  49.0001
            NLPID         :  0xCC 0x8E
            Router ID     :  10.36.3.3
            IP Address    :  10.36.3.3
            MT TopoId     : TopoId:2 Att: 0 Ol: 0
                            TopoId:0 Att: 0 Ol: 0
            Hostname      :  R3_nx              Length : 5
            TopoId: 2
            MtExtend IS   :  R1_xe.02           Metric : 40
            Extended IS   :  R1_xe.02           Metric : 40
            Extended IP   :         10.36.3.3/32  Metric : 1           (U)
            Extended IP   :     10.13.115.0/24  Metric : 40          (U)
            Extended IP   :     10.23.115.0/24  Metric : 40          (U)
            MT-IPv6 Prefx :  TopoId : 2
                            2001:3:3:3::3/128  Metric : 1           (U/I)
            MT-IPv6 Prefx :  TopoId : 2
                            2001:10:13:115::/64  Metric : 40          (U/I)
            MT-IPv6 Prefx :  TopoId : 2
                            2001:10:23:115::/64  Metric : 40          (U/I)
            Digest Offset :  0

        IS-IS Level-2 Link State Database
        LSPID                 Seq Number   Checksum  Lifetime   A/P/O/T
        R1_xe.00-00           0x000007CB   0x25D3    908        0/0/0/3
            Instance      :  0x000007C6
            Area Address  :  49.0001
            NLPID         :  0xCC 0x8E
            MT TopoId     : TopoId:0 Att: 0 Ol: 0
                            TopoId:2 Att: 0 Ol: 0
            Hostname      :  R1_xe              Length : 5
            Extended IS   :  R1_xe.02           Metric : 10
            TopoId: 2
            MtExtend IS   :  R1_xe.02           Metric : 10
            IP Address    :  10.13.115.1
            Extended IP   :     10.12.115.0/24  Metric : 10          (U)
            Unknown Sub-TLV      :  Length : 1  Type :   4
            Extended IP   :     10.13.115.0/24  Metric : 10          (U)
            Unknown Sub-TLV      :  Length : 1  Type :   4
            Extended IP   :     10.23.115.0/24  Metric : 50          (U)
            Unknown Sub-TLV      :  Length : 1  Type :   4
            IPv6 Address  :  2001:10:13:115::1
            MT-IPv6 Prefx :  TopoId : 2
                            2001:10:12:115::/64  Metric : 10          (U/I)
            Unknown Sub-TLV      :  Length : 1  Type :   4
        2001:10:13:115::/64  Metric : 10          (U/I)
            Unknown Sub-TLV      :  Length : 1  Type :   4
        2001:10:23:115::/64  Metric : 50          (U/I)
            Unknown Sub-TLV      :  Length : 1  Type :   4
            Digest Offset :  0
        R1_xe.02-00           0x000007C6   0x27D9    1174       0/0/0/3
            Instance      :  0x000007C5
            Extended IS   :  R1_xe.00           Metric : 0
            Extended IS   :  R3_nx.00           Metric : 0
            Digest Offset :  0
        R3_nx.00-00         * 0x00000B06   0x6EBD    1136       0/0/0/3
            Instance      :  0x00000B06
            Area Address  :  49.0001
            NLPID         :  0xCC 0x8E
            Router ID     :  10.36.3.3
            IP Address    :  10.36.3.3
            MT TopoId     : TopoId:2 Att: 0 Ol: 0
                            TopoId:0 Att: 0 Ol: 0
            Hostname      :  R3_nx              Length : 5
            TopoId: 2
            MtExtend IS   :  R1_xe.02           Metric : 40
            Extended IS   :  R1_xe.02           Metric : 40
            Extended IP   :         10.36.3.3/32  Metric : 1           (U)
            Extended IP   :     10.13.115.0/24  Metric : 40          (U)
            Extended IP   :     10.23.115.0/24  Metric : 40          (U)
            MT-IPv6 Prefx :  TopoId : 2
                            2001:3:3:3::3/128  Metric : 1           (U/I)
            MT-IPv6 Prefx :  TopoId : 2
                            2001:10:13:115::/64  Metric : 40          (U/I)
            MT-IPv6 Prefx :  TopoId : 2
                            2001:10:23:115::/64  Metric : 40          (U/I)
            Digest Offset :  0

        R3_nx#
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIsisDatabaseDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowIsisDatabaseDetail(device=self.device)
        parsed_output = obj.parse(vrf='all')
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == '__main__':
    unittest.main()