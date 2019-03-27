#!/bin/env python
import unittest
from unittest.mock import Mock
from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                             SchemaMissingKeyError

from genie.libs.parser.iosxe.show_l2vpn import ShowL2vpnVfi


class test_show_l2vpn_vfi(unittest.TestCase):

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
    'vfi': {
        'serviceCore1': {
            'signaling': 'LDP',
            'vpls_id': '9:10',
            'vpn_id': 100,
            'bd_vfi_name': 'serviceCore1',
            'bridge_domain': {
                100: {
                    'pseudo_port_interface': 'Virtual-Ethernet1000',
                    'vfi': {
                        '10.0.0.1': {
                            'pw_id': {
                                'Pw2000': {
                                    'discovered_router_id': '10.0.0.1',
                                    'vc_id': 10,
                                    'next_hop': '10.0.0.1',
                                    },
                                },
                            },
                        '10.0.0.4': {
                            'pw_id': {
                                'Pw5': {
                                    'discovered_router_id': '-',
                                    'vc_id': 10,
                                    'next_hop': '10.0.0.4',
                                    },
                                },
                            },
                        '10.0.0.3': {
                            'pw_id': {
                                'Pw2002': {
                                    'discovered_router_id': '10.1.1.3',
                                    'vc_id': 10,
                                    'next_hop': '10.0.0.3',
                                    },
                                },
                            },
                        '10.0.0.2': {
                            'pw_id': {
                                'Pw2001': {
                                    'discovered_router_id': '10.1.1.2',
                                    'vc_id': 10,
                                    'next_hop': '10.0.0.2',
                                    },
                                },
                            },
                        },
                    },
                },
            'rt': ['10.10.10.10:150'],
            'state': 'UP',
            'rd': '9:10',
            },
        },
    }

    golden_output = {'execute.return_value': '''\
    Device# show l2vpn vfi

    Legend: RT= Route-target

    VFI name: serviceCore1, State: UP, Signaling Protocol: LDP
      VPN ID: 100, VPLS-ID: 9:10, Bridge-domain vlan: 100
      RD: 9:10, RT: 10.10.10.10:150
      Pseudo-port Interface: Virtual-Ethernet1000

      Neighbors connected via pseudowires:
      Interface    Peer Address    VC ID      Discovered Router ID   Next Hop
      Pw2000       10.0.0.1        10         10.0.0.1               10.0.0.1
      Pw2001       10.0.0.2        10         10.1.1.2               10.0.0.2
      Pw2002       10.0.0.3        10         10.1.1.3               10.0.0.3
      Pw5          10.0.0.4        10         -                      10.0.0.4
    '''
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        platform_obj = ShowL2vpnVfi(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = platform_obj.parse()    

    def test_golden_full(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        platform_obj = ShowL2vpnVfi(device=self.device)
        parsed_output = platform_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


if __name__ == '__main__':
    unittest.main()