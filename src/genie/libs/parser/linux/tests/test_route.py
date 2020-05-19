import re
import unittest
from unittest.mock import Mock

from pyats.topology import Device

from genie.metaparser.util.exceptions import (SchemaMissingKeyError,
                                              SchemaEmptyParserError)

from genie.libs.parser.linux.route import Route,\
                                          ShowNetworkStatusRoute


#############################################################################
# unitest for 'route'
#############################################################################

class TestRoute(unittest.TestCase):
    '''
    Unit test for
        * route
    '''
    
    device = Device(name='aDevice')
    maxDiff = None
    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        Kernel IP routing table
        Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
        default         _gateway        0.0.0.0         UG    600    0        0 wlo1
        172.17.0.0      0.0.0.0         255.255.0.0     U     0      0        0 docker0
        192.168.1.0     0.0.0.0         255.255.255.0   U     600    0        0 wlo1
        192.168.122.0   0.0.0.0         255.255.255.0   U     0      0        0 virbr0
        10.10.0.0       0.0.0.0         255.255.255.0   U     0      0        0 eth1-05
    '''}

    golden_parsed_output = {
        'routes': {
            '10.10.0.0': {
                'mask': {
                    '255.255.255.0': {
                        'nexthop': {
                            1: {
                                'flags': 'U',
                                'gateway': '0.0.0.0',
                                'interface': 'eth1-05',
                                'metric': 0,
                                'ref': 0,
                                'use': 0,
                            },
                        },
                    },
                },
            },
            '172.17.0.0': {
                'mask': {
                    '255.255.0.0': {
                        'nexthop': {
                            1: {
                                'flags': 'U',
                                'gateway': '0.0.0.0',
                                'interface': 'docker0',
                                'metric': 0,
                                'ref': 0,
                                'use': 0,
                            },
                        },
                    },
                },
            },
            '192.168.1.0': {
                'mask': {
                    '255.255.255.0': {
                        'nexthop': {
                            1: {
                                'flags': 'U',
                                'gateway': '0.0.0.0',
                                'interface': 'wlo1',
                                'metric': 600,
                                'ref': 0,
                                'use': 0,
                            },
                        },
                    },
                },
            },
            '192.168.122.0': {
                'mask': {
                    '255.255.255.0': {
                        'nexthop': {
                            1: {
                                'flags': 'U',
                                'gateway': '0.0.0.0',
                                'interface': 'virbr0',
                                'metric': 0,
                                'ref': 0,
                                'use': 0,
                            },
                        },
                    },
                },
            },
            'default': {
                'mask': {
                    '0.0.0.0': {
                        'nexthop': {
                            1: {
                                'flags': 'UG',
                                'gateway': '_gateway',
                                'interface': 'wlo1',
                                'metric': 600,
                                'ref': 0,
                                'use': 0,
                            },
                        },
                    },
                },
            },
        },
    }

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = Route(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = Route(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


#############################################################################
# unitest For netstat -rn
#############################################################################

class TestNetstatRn(unittest.TestCase):
    '''
    Unit test for
        * netstat -rn
    '''
    
    device = Device(name='aDevice')
    maxDiff = None
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        '10.10.0.0': {
            'destination': '10.10.0.0',
            'flags': 'U',
            'gateway': '0.0.0.0',
            'interface': 'eth1-05',
            'mask': '255.255.255.0',
            'mss': 0,
            'window': 0,
            'irtt': 0
                },
        '172.17.0.0': {
            'destination': '172.17.0.0',
            'flags': 'U',
            'gateway': '0.0.0.0',
            'interface': 'docker0',
            'mask': '255.255.0.0',
            'mss': 0,
            'window': 0,
            'irtt': 0
            },
        '192.168.1.0': {
            'destination': '192.168.1.0',
            'flags': 'U',
            'gateway': '0.0.0.0',
            'interface': 'wlo1',
            'mask': '255.255.255.0',
            'mss': 0,
            'window': 0,
            'irtt': 0
            },
        '192.168.122.0': {
            'destination': '192.168.122.0',
            'flags': 'U',
            'gateway': '0.0.0.0',
            'interface': 'virbr0',
            'mask': '255.255.255.0',
            'mss': 0,
            'window': 0,
            'irtt': 0
            },
        '0.0.0.0': {
            'destination': '0.0.0.0',
            'flags': 'UG',
            'gateway': '192.168.1.1',
            'interface': 'wlo1',
            'mask': '0.0.0.0',
            'mss': 0,
            'window': 0,
            'irtt': 0
            }
        }

    golden_output = {'execute.return_value': '''
        Kernel IP routing table
        Destination     Gateway         Genmask         Flags   MSS Window  irtt Iface
        0.0.0.0         192.168.1.1     0.0.0.0         UG        0 0          0 wlo1
        172.17.0.0      0.0.0.0         255.255.0.0     U         0 0          0 docker0
        192.168.1.0     0.0.0.0         255.255.255.0   U         0 0          0 wlo1
        192.168.122.0   0.0.0.0         255.255.255.0   U         0 0          0 virbr0
        10.10.0.0       0.0.0.0         255.255.255.0   U         0 0          0 eth1-05
    '''}


    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowNetworkStatusRoute(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowNetworkStatusRoute(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == '__main__':
    unittest.main()
