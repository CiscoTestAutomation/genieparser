# Import the Python mock functionality
import unittest
from unittest.mock import Mock

# pyATS
from pyats.topology import Device
from pyats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

# iosxe show_dmvpn
from genie.libs.parser.iosxe.show_dmvpn import ShowDmvpn


# =================================
# Unit test for 'show dmvpn'
# =================================
class TestShowDmvpn(unittest.TestCase):
    """Unit test for
        *show dmvpn
    """

    maxDiff = None

    empty_output = {'execute.return_value': ''}

    # Specify the expected result for the parsed output
    golden_parsed_output1 = {
            'interfaces': {
                'Tunnel84': {
                    'ent': {
                        1: {
                            'peers': {
                                '172.30.84.1': {
                                    'tunnel_addr': {
                                        '172.29.0.1': {
                                            'attrb': {
                                                'SC': {
                                                    'state': 'NHRP',
                                                    'time': 'never',
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                    'nhrp_peers': 1,
                    'type': 'Spoke',
                },
                'Tunnel90': {
                    'ent': {
                        1: {
                            'peers': {
                                '172.29.0.1': {
                                    'tunnel_addr': {
                                        '172.30.90.1': {
                                            'attrb': {
                                                'S': {
                                                    'state': 'IKE',
                                                    'time': '3w5d',
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                        2: {
                            'peers': {
                                '172.29.0.2': {
                                    'tunnel_addr': {
                                        '172.30.90.2': {
                                            'attrb': {
                                                'S': {
                                                    'state': 'UP',
                                                    'time': '6d12h',
                                                },
                                            },
                                        },
                                        '172.30.90.25': {
                                            'attrb': {
                                                'S': {
                                                    'state': 'UP',
                                                    'time': '6d12h',
                                                },
                                            },
                                        },
                                    },
                                },
                                '172.29.134.1': {
                                    'tunnel_addr': {
                                        '172.30.72.72': {
                                            'attrb': {
                                                'DT1': {
                                                    'state': 'UP',
                                                    'time': '00:29:40',
                                                },
                                                'DT2': {
                                                    'state': 'UP',
                                                    'time': '00:29:40',
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                    'nhrp_peers': 3,
                    'type': 'Spoke',
                },
            },
        }

    # show dmvpn
    golden_output1 = {'execute.return_value': '''
        Legend: Attrb --> S - Static, D - Dynamic, I - Incomplete
                N - NATed, L - Local, X - No Socket
                T1 - Route Installed, T2 - Nexthop-override
                C - CTS Capable
                # Ent --> Number of NHRP entries with same NBMA peer
                NHS Status: E --> Expecting Replies, R --> Responding, W --> Waiting
                UpDn Time --> Up or Down Time for a Tunnel
        ==========================================================================

        Interface: Tunnel84, IPv4 NHRP Details
        Type:Spoke, NHRP Peers:1,

         # Ent  Peer NBMA Addr Peer Tunnel Add State  UpDn Tm Attrb
         ----- --------------- --------------- ----- -------- -----
             1 172.30.84.1          172.29.0.1  NHRP    never    SC

        Interface: Tunnel90, IPv4 NHRP Details        
        Type:Spoke, NHRP Peers:3,

         # Ent  Peer NBMA Addr Peer Tunnel Add State  UpDn Tm Attrb
         ----- --------------- --------------- ----- -------- -----
             1 172.29.0.1          172.30.90.1   IKE     3w5d     S
             2 172.29.0.2          172.30.90.2    UP    6d12h     S
                                   172.30.90.25   UP    6d12h     S
             2 172.29.134.1       172.30.72.72    UP 00:29:40   DT2
                                  172.30.72.72    UP 00:29:40   DT1
'''}

    def test_show_dmvpn_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowDmvpn(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_dmvpn_full1(self):
        self.device = Mock(**self.golden_output1)
        obj = ShowDmvpn(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)


if __name__ == '__main__':
    unittest.main()