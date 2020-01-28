import unittest
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
    COPQON05R07              L2    Up    24   To-COPQON05R07-LAG-7          0
    COTKON04XR1              L2    Up    24   To-COTKON04XR1-LAG-4          0
    COTKPQ03R07              L2    Up    24   To-COTKPQ03R07-LAG-9          0
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
                        'To-COPQON05R07-LAG-7': {
                            'system_id': {
                                'COPQON05R07': {
                                    'hold': 24,
                                    'mt_id': 0,
                                    'state': 'Up',
                                },
                            },
                        },
                        'To-COTKON04XR1-LAG-4': {
                            'system_id': {
                                'COTKON04XR1': {
                                    'hold': 24,
                                    'mt_id': 0,
                                    'state': 'Up',
                                },
                            },
                        },
                        'To-COTKPQ03R07-LAG-9': {
                            'system_id': {
                                'COTKPQ03R07': {
                                    'hold': 24,
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
    Hostname    : COPQON05R07
    SystemID    : 0691.5819.6089                   SNPA        : 00:23:3e:8f:17:97
    Interface   : To-COPQON05R07-LAG-7             Up Time     : 58d 03:24:48
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
    Hostname    : COTKON04XR1
    SystemID    : 0670.7021.9137                   SNPA        : 84:26:2b:bc:2d:e1
    Interface   : To-COTKON04XR1-LAG-4             Up Time     : 36d 23:21:57
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
    Hostname    : COTKPQ03R07
    SystemID    : 0691.5819.6091                   SNPA        : 00:23:3e:8d:2f:99
    Interface   : To-COTKPQ03R07-LAG-9             Up Time     : 58d 03:24:48
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
    []
    '''}

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
        import pprint
        pprint.pprint(parsed_output)
        import pdb
        pdb.set_trace()

        # self.assertEqual(parsed_output,self.sample_parsed_output)



