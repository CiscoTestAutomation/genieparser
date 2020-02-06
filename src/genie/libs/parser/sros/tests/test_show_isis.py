import unittest
import time
from unittest.mock import Mock
from pyats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                       SchemaMissingKeyError
from genie.libs.parser.sros.show_isis import ShowRouterIsisAdjacency,\
                                        ShowRouterIsisAdjacencyDetail


class TestShowRouterIsisAdjacency(unittest.TestCase):
    dev = Device(name='device')
    empty_output = {'execute.return_value': ''}

    sample_output = {'execute.return_value': '''
    A:admin@COTKON04XR2# show router  isis adjacency 
    ===============================================================================
    Rtr Base ISIS Instance 0 Adjacency 
    ===============================================================================
    System ID                Usage State Hold Interface                     MT-ID
    -------------------------------------------------------------------------------
    GENIE01R07              L2    Up    24   To-GENIE01R07-LAG-7          0
    GENIE04XR1              L2    Up    24   To-GENIE04XR1-LAG-4          0
    GENIE03R07              L2    Up    24   To-GENIE03R07-LAG-9          0
    -------------------------------------------------------------------------------
    Adjacencies : 3
    ===============================================================================
    []
    '''}

    sample_parsed_output = {
    'instance': {
        '0': {
            'level': {
                'L2': {
                    'interfaces': {
                        'To-GENIE01R07-LAG-7': {
                            'system_id': {
                                'GENIE01R07': {
                                    'hold_time': 24,
                                    'mt_id': 0,
                                    'state': 'Up',
                                },
                            },
                        },
                        'To-GENIE04XR1-LAG-4': {
                            'system_id': {
                                'GENIE04XR1': {
                                    'hold_time': 24,
                                    'mt_id': 0,
                                    'state': 'Up',
                                },
                            },
                        },
                        'To-GENIE03R07-LAG-9': {
                            'system_id': {
                                'GENIE03R07': {
                                    'hold_time': 24,
                                    'mt_id': 0,
                                    'state': 'Up',
                                },
                            },
                        },
                    },
                    'total_adjacency_count': 3,
                },
            },
        },
    },
}

    def test_empty(self):
        self.dev = Mock(**self.empty_output)
        obj = ShowRouterIsisAdjacency(device=self.dev)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev = Mock(**self.sample_output)
        obj = ShowRouterIsisAdjacency(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.sample_parsed_output)


class TestShowRouterIsisAdjacencyDetail(unittest.TestCase):
    dev = Device(name='device')
    empty_output = {'execute.return_value': ''}

    sample_output = {'execute.return_value': '''
    A:admin@COTKON04XR2# show router  isis adjacency detail 
    ===============================================================================
    Rtr Base ISIS Instance 0 Adjacency (detail)
    ===============================================================================
    Hostname    : GENIE01R07
    SystemID    : 0691.58ff.79a2                   SNPA        : 00:23:3e:ff:a6:27
    Interface   : To-GENIE01R07-LAG-7             Up Time     : 58d 03:24:48
    State       : Up                               Priority    : 0
    Nbr Sys Typ : L2                               L. Circ Typ : L2
    Hold Time   : 22                               Max Hold    : 30
    Adj Level   : L2                               MT Enabled  : No
    Topology    : Unicast
    IPv6 Neighbor     : ::
    IPv4 Neighbor     : 10.11.97.22
    IPv4 Adj SID      : Label 524213
    Restart Support   : Disabled
    Restart Status    : Not currently being helped
    Restart Supressed : Disabled
    Number of Restarts: 0
    Last Restart at   : Never
    Hostname    : GENIE04XR1
    SystemID    : 0670.70ff.b258                   SNPA        : 84:26:2b:ff:e9:9e
    Interface   : To-GENIE04XR1-LAG-4             Up Time     : 36d 23:21:57
    State       : Up                               Priority    : 0
    Nbr Sys Typ : L2                               L. Circ Typ : L2
    Hold Time   : 23                               Max Hold    : 30
    Adj Level   : L2                               MT Enabled  : No
    Topology    : Unicast
    IPv6 Neighbor     : ::
    IPv4 Neighbor     : 10.11.79.245
    IPv4 Adj SID      : Label 524127
    Restart Support   : Disabled
    Restart Status    : Not currently being helped
    Restart Supressed : Disabled
    Number of Restarts: 0
    Last Restart at   : Never
    Hostname    : GENIE03R07
    SystemID    : 0691.58ff.79aa                   SNPA        : 00:23:3e:ff:bc:27
    Interface   : To-GENIE03R07-LAG-9             Up Time     : 58d 03:24:48
    State       : Up                               Priority    : 0
    Nbr Sys Typ : L2                               L. Circ Typ : L2
    Hold Time   : 22                               Max Hold    : 30
    Adj Level   : L2                               MT Enabled  : No
    Topology    : Unicast
    IPv6 Neighbor     : ::
    IPv4 Neighbor     : 10.11.79.242
    IPv4 Adj SID      : Label 524214
    Restart Support   : Disabled
    Restart Status    : Not currently being helped
    Restart Supressed : Disabled
    Number of Restarts: 0
    Last Restart at   : Never
    ===============================================================================
    Rtr Base ISIS Instance 1 Adjacency (detail)
    ===============================================================================
    Hostname    : GENIE01R07
    SystemID    : 0691.58ff.79a2                   SNPA        : 00:23:3e:ff:a6:27
    Interface   : To-GENIE01R07-LAG-7             Up Time     : 58d 03:24:48
    State       : Up                               Priority    : 0
    Nbr Sys Typ : L2                               L. Circ Typ : L2
    Hold Time   : 22                               Max Hold    : 30
    Adj Level   : L2                               MT Enabled  : No
    Topology    : Unicast
    IPv6 Neighbor     : ::
    IPv4 Neighbor     : 10.11.97.22
    IPv4 Adj SID      : Label 524213
    Restart Support   : Disabled
    Restart Status    : Not currently being helped
    Restart Supressed : Disabled
    Number of Restarts: 0
    Last Restart at   : Never
    []
    '''}
    sample_parsed_output = {
    'instance': {
        '0': {
            'level': {
                'L2': {
                    'interfaces': {
                        'To-GENIE01R07-LAG-7': {
                            'system_id': {
                                '0691.58ff.79a2': {
                                    'hold_time': 22,
                                    'hostname': 'GENIE01R07',
                                    'ipv4_adj_sid': 'Label 524213',
                                    'ipv4_neighbor': '10.11.97.22',
                                    'ipv6_neighbor': '::',
                                    'l_circ_typ': 'L2',
                                    'last_restart_at': 'Never',
                                    'max_hold': 30,
                                    'mt_enabled': 'No',
                                    'nbr_sys_typ': 'L2',
                                    'number_of_restarts': 0,
                                    'priority': 0,
                                    'restart_support': 'Disabled',
                                    'restart_supressed': 'Disabled',
                                    'restart_status': 'Not currently being helped',
                                    'snpa': '00:23:3e:ff:a6:27',
                                    'state': 'Up',
                                    'topology': 'Unicast',
                                    'up_time': '58d 03:24:48',
                                },
                            },
                        },
                        'To-GENIE04XR1-LAG-4': {
                            'system_id': {
                                '0670.70ff.b258': {
                                    'hold_time': 23,
                                    'hostname': 'GENIE04XR1',
                                    'ipv4_adj_sid': 'Label 524127',
                                    'ipv4_neighbor': '10.11.79.245',
                                    'ipv6_neighbor': '::',
                                    'l_circ_typ': 'L2',
                                    'last_restart_at': 'Never',
                                    'max_hold': 30,
                                    'mt_enabled': 'No',
                                    'nbr_sys_typ': 'L2',
                                    'number_of_restarts': 0,
                                    'priority': 0,
                                    'restart_support': 'Disabled',
                                    'restart_supressed': 'Disabled',
                                    'restart_status': 'Not currently being helped',
                                    'snpa': '84:26:2b:ff:e9:9e',
                                    'state': 'Up',
                                    'topology': 'Unicast',
                                    'up_time': '36d 23:21:57',
                                },
                            },
                        },
                        'To-GENIE03R07-LAG-9': {
                            'system_id': {
                                '0691.58ff.79aa': {
                                    'hold_time': 22,
                                    'hostname': 'GENIE03R07',
                                    'ipv4_adj_sid': 'Label 524214',
                                    'ipv4_neighbor': '10.11.79.242',
                                    'ipv6_neighbor': '::',
                                    'l_circ_typ': 'L2',
                                    'last_restart_at': 'Never',
                                    'max_hold': 30,
                                    'mt_enabled': 'No',
                                    'nbr_sys_typ': 'L2',
                                    'number_of_restarts': 0,
                                    'priority': 0,
                                    'restart_support': 'Disabled',
                                    'restart_supressed': 'Disabled',
                                    'restart_status': 'Not currently being helped',
                                    'snpa': '00:23:3e:ff:bc:27',
                                    'state': 'Up',
                                    'topology': 'Unicast',
                                    'up_time': '58d 03:24:48',
                                },
                            },
                        },
                    },
                },
            },
        },
        '1': {
            'level': {
                'L2': {
                    'interfaces': {
                        'To-GENIE01R07-LAG-7': {
                            'system_id': {
                                '0691.58ff.79a2': {
                                    'hold_time': 22,
                                    'hostname': 'GENIE01R07',
                                    'ipv4_adj_sid': 'Label 524213',
                                    'ipv4_neighbor': '10.11.97.22',
                                    'ipv6_neighbor': '::',
                                    'l_circ_typ': 'L2',
                                    'last_restart_at': 'Never',
                                    'max_hold': 30,
                                    'mt_enabled': 'No',
                                    'nbr_sys_typ': 'L2',
                                    'number_of_restarts': 0,
                                    'priority': 0,
                                    'restart_support': 'Disabled',
                                    'restart_supressed': 'Disabled',
                                    'restart_status': 'Not currently being helped',
                                    'snpa': '00:23:3e:ff:a6:27',
                                    'state': 'Up',
                                    'topology': 'Unicast',
                                    'up_time': '58d 03:24:48',
                                },
                            },
                        },
                    },
                },
            },
        },
    },
}

    def test_empty(self):
        self.dev = Mock(**self.empty_output)
        obj = ShowRouterIsisAdjacencyDetail(device=self.dev)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev = Mock(**self.sample_output)
        obj = ShowRouterIsisAdjacencyDetail(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.sample_parsed_output)