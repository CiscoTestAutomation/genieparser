
# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                             SchemaMissingKeyError

# iosxe traceroute
from genie.libs.parser.iosxe.traceroute import Traceroute


# ================
# Unit test for:
#   * 'traceroute'
# ================
class TestTraceroute(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = ''

    golden_parsed_output1 = {
        'traceroute': {
            '172.16.166.253': {
                'address': '172.16.166.253',
                'hops': {
                    '9': {
                        'paths': {
                            1: {
                                'address': '10.2.1.2',
                                'vrf_out_id': '2001',
                                'vrf_out_name': 'blue',
                                'vrf_in_id': '1001',
                                'vrf_in_name': 'red',
                            }}},
                    '4': {
                        'paths': {
                            1: {
                                'address': '192.168.15.1',
                                'label_info': {
                                    'MPLS': {
                                        'label': '24133',
                                        'exp': 0,
                                    },
                                },
                                'probe_msec': ['6', '7', '64'],
                            }}},
                    '5': {
                        'paths': {
                            1: {
                                'address': '10.80.241.86',
                                'label_info': {
                                    'MPLS': {
                                        'label': '24147',
                                        'exp': 0,
                                    },
                                },
                                'probe_msec': ['69', '65', '111'],
                            }}},
                    '8': {
                        'paths': {
                            1: {
                                'address': '10.1.1.2',
                                'vrf_out_id': '2001',
                                'vrf_out_name': 'blue',
                                'vrf_in_id': '1001',
                                'vrf_in_name': 'red',
                            }}},
                    '2': {
                        'paths': {
                            1: {
                                'address': '10.0.9.1',
                                'label_info': {
                                    'MPLS': {
                                        'label': '300678',
                                        'exp': 0,
                                    },
                                },
                                'probe_msec': ['177', '150', '9'],
                            }}},
                    '1': {
                        'paths': {
                            1: {
                                'address': '172.31.255.125',
                                'label_info': {
                                    'MPLS': {
                                        'label': '624',
                                        'exp': 0,
                                    },
                                },
                                'probe_msec': ['70', '200', '19'],
                            }}},
                    '6': {
                        'paths': {
                            1: {
                                'address': '10.90.135.110',
                                'label_info': {
                                    'MPLS': {
                                        'label': '24140',
                                        'exp': 0,
                                    },
                                },
                                'probe_msec': ['21', '4', '104'],
                            }}},
                    '3': {
                        'paths': {
                            1: {
                                'address': '192.168.14.61',
                                'label_info': {
                                    'MPLS': {
                                        'label': '302537',
                                        'exp': 0,
                                    },
                                },
                                'probe_msec': ['134', '1', '55'],
                            }}},
                    '7': {
                        'paths': {
                            1: {
                                'address': '172.31.166.10',
                                'probe_msec': ['92', '51', '148'],
                            },
                        },
                    }}}
        },
    }

    golden_output1 = '''\
        router#traceroute 172.16.166.253 numeric timeout 1 probe 3 ttl 1 15 source 10.36.255.248 
        Type escape sequence to abort. 
        Tracing the route to 172.16.166.253 
        VRF info: (vrf in name/id, vrf out name/id) 
          1 172.31.255.125 [MPLS: Label 624 Exp 0] 70 msec 200 msec 19 msec 
          2 10.0.9.1 [MPLS: Label 300678 Exp 0] 177 msec 150 msec 9 msec 
          3 192.168.14.61 [MPLS: Label 302537 Exp 0] 134 msec 1 msec 55 msec 
          4 192.168.15.1 [MPLS: Label 24133 Exp 0] 6 msec 7 msec 64 msec 
          5 10.80.241.86 [MPLS: Label 24147 Exp 0] 69 msec 65 msec 111 msec 
          6 10.90.135.110 [MPLS: Label 24140 Exp 0] 21 msec 4 msec 104 msec 
          7 172.31.166.10 92 msec 51 msec 148 msec
          8 10.1.1.2 (red/1001, blue/2001)
          9 10.2.1.2 (red/1001, blue/2001)
        '''

    golden_parsed_output2 = {
        'traceroute': {
            '172.31.165.220/32': {
                'address': '172.31.165.220',
                'mask': '32',
                'timeout_seconds': 2,
                'hops': {
                    '1': {
                        'paths': {
                            1: {
                                'address': '192.168.197.93',

                                'label_info': {
                                    'label_name': 'implicit-null',
                                    'exp': 0,
                                },
                                'probe_msec': ['1'],
                                'mru': 1552,
                            }},
                        'code': 'L', },
                    '2': {
                        'paths': {
                            1: {
                                'address': '192.168.197.102',
                                'probe_msec': ['1'],
                            }},
                        'code': '!', },
                    '0': {
                        'paths': {
                            1: {
                                'address': '192.168.197.94',
                                'label_info': {
                                    'label_name': '1015',
                                    'exp': 0,
                                },
                                'mru': 1552,
                            }}}
                },
            },
        },
    }

    golden_output2 = '''\
        router#traceroute mpls ipv4 172.31.165.220 255.255.255.255
        Tracing MPLS Label Switched Path to 172.31.165.220/32, timeout is 2 seconds

        Codes: '!' - success, 'Q' - request not sent, '.' - timeout,
          'L' - labeled output interface, 'B' - unlabeled output interface,
          'D' - DS Map mismatch, 'F' - no FEC mapping, 'f' - FEC mismatch,
          'M' - malformed request, 'm' - unsupported tlvs, 'N' - no label entry,
          'P' - no rx intf label prot, 'p' - premature termination of LSP,
          'R' - transit router, 'I' - unknown upstream index,
          'l' - Label switched with FEC change, 'd' - see DDMAP for return code,
          'X' - unknown return code, 'x' - return code 0

        Type escape sequence to abort.
          0 192.168.197.94 MRU 1552 [Labels: 1015 Exp: 0]
        L 1 192.168.197.93 MRU 1552 [Labels: implicit-null Exp: 0] 1 ms
        ! 2 192.168.197.102 1 ms
        '''

    golden_parsed_output3 = {
        'traceroute': {
            '10.4.1.1': {
                'address': '10.4.1.1',
                'hops': {
                    '1': {
                        'paths': {
                            1: {
                                'address': '10.10.10.10',
                                'probe_msec': ['1', '1', '*'],
                            },
                        }
                    }
                },
                'name_of_address': 'www.xyz.com',
            },
        },
    }

    golden_output3 = '''\
        [2019-04-11 11:02:15,834] +++ PE1: executing command 'traceroute www.xyz.com' +++
        traceroute www.xyz.com
        Type escape sequence to abort.
        Tracing the route to www.xyz.com (10.4.1.1)
        VRF info: (vrf in name/id, vrf out name/id)
          1 10.10.10.10 1 msec 1 msec * 
        PE1#
        '''
    golden_parsed_output4 = {
        'traceroute': {
            '172.16.51.1': {
                'address': '172.16.51.1',
                'hops': {
                    '1': {
                        'paths': {
                            1: {'address': '*'},
                            2: {'address': '172.16.51.1',
                                'probe_msec': ['41', '*'],
                                },
                            3: {'address': '*'},

                        }
                    },
                    '2': {
                        'paths': {
                            1: {'address': '10.1.2.6',
                                'probe_msec': ['148']},
                            2: {'address': '10.1.1.6',
                                'probe_msec': ['120']},
                            3: {'address': '10.1.2.6',
                                'probe_msec': ['132']}}}
                },
                'vrf': 'CE1test',
            },
        },
    }

    golden_output4 = '''
        traceroute vrf CE1test 172.16.51.1
        Type escape sequence to abort.
        Tracing the route to 172.16.51.1
        VRF info: (vrf in name/id, vrf out name/id)
        1  *
            172.16.51.1 41 msec *
            *
        2 10.1.2.6 148 msec
            10.1.1.6 120 msec
            10.1.2.6 132 msec
    '''

    golden_parsed_output5 = {
        'traceroute': {
            '192.168.1.1': {
                'address': '192.168.1.1',
                'hops': {
                    '1': {
                        'paths': {
                            1: {
                                'address': '10.19.198.29',
                                'probe_msec': ['2', '2', '2'],
                                'label_info': {
                                    'MPLS': {
                                        'label': '16052/16062/16063/39',
                                        'exp': 0,
                                    },
                                },
                            },
                        },
                    },
                    '2': {
                        'paths': {
                            1: {
                                'address': '10.169.14.129',
                                'probe_msec': ['3', '1', '1'],
                                'label_info': {
                                    'MPLS': {
                                        'label': '16062/16063/39',
                                        'exp': 0,
                                    },
                                },
                            },
                        },
                    },
                    '3': {
                        'paths': {
                            1: {
                                'address': '10.169.14.34',
                                'probe_msec': ['3', '1', '2'],
                                'label_info': {
                                    'MPLS': {
                                        'label': '16063/39',
                                        'exp': 0,
                                    },
                                },
                            },
                        },
                    },
                    '4': {
                        'paths': {
                            1: {
                                'address': '192.168.1.1',
                                'probe_msec': ['2', '*', '2'],
                            },
                        },
                    },
                },
                'vrf': 'MG501',
            },
        },
    }
    golden_output5 = '''
        traceroute vrf MG501 192.168.1.1 numeric    
        Type escape sequence to abort.
        Tracing the route to 192.168.1.1
        VRF info: (vrf in name/id, vrf out name/id)
        1 10.19.198.29 [MPLS: Labels 16052/16062/16063/39 Exp 0] 2 msec 2 msec 2 msec
        2 10.169.14.129 [MPLS: Labels 16062/16063/39 Exp 0] 3 msec 1 msec 1 msec
        3 10.169.14.34 [MPLS: Labels 16063/39 Exp 0] 3 msec 1 msec 2 msec
        4 192.168.1.1 2 msec *  2 msec
    '''

    golden_parsed_output6 = {
        'traceroute': {
            '10.151.22.22': {
                'address': '10.151.22.22',
                'hops': {
                    '1': {
                        'paths': {
                            1: {
                                'address': '10.0.0.5',
                                'probe_msec': ['307', '10', '2'],
                                'label_info': {
                                    'MPLS': {
                                        'label': '16022',
                                        'exp': 0,
                                    },
                                },
                            },
                        },
                    },
                    '2': {
                        'paths': {
                            1: {
                                'address': '10.0.0.18',
                                'probe_msec': ['351', '*', '8'],
                            },
                        },
                    },
                },
            },
        },
    }

    golden_output6 = '''
        traceroute 10.151.22.22
        Type escape sequence to abort.
        Tracing the route to 10.151.22.22
        VRF info: (vrf in name/id, vrf out name/id)
        1 10.0.0.5 [MPLS: Label 16022 Exp 0] 307 msec 10 msec 2 msec
        2 10.0.0.18 351 msec *  8 msec
    '''

    def test_traceroute_empty(self):
        obj = Traceroute(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(output=self.empty_output)

    def test_traceroute_golden1(self):
        self.maxDiff = None
        obj = Traceroute(device=self.device)
        parsed_output = obj.parse(output=self.golden_output1)
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_traceroute_golden2(self):
        self.maxDiff = None
        obj = Traceroute(device=self.device)
        parsed_output = obj.parse(output=self.golden_output2)
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_traceroute_golden3(self):
        self.maxDiff = None
        obj = Traceroute(device=self.device)
        parsed_output = obj.parse(output=self.golden_output3)
        self.assertEqual(parsed_output, self.golden_parsed_output3)

    def test_traceroute_golden4(self):
        self.maxDiff = None
        obj = Traceroute(device=self.device)
        parsed_output = obj.parse(output=self.golden_output4)
        self.assertEqual(parsed_output, self.golden_parsed_output4)

    def test_traceroute_golden5(self):
        self.maxDiff = None
        obj = Traceroute(device=self.device)
        parsed_output = obj.parse(output=self.golden_output5)
        self.assertEqual(parsed_output, self.golden_parsed_output5)

    def test_traceroute_golden6(self):
        self.maxDiff = None
        obj = Traceroute(device=self.device)
        parsed_output = obj.parse(output=self.golden_output6)
        self.assertEqual(parsed_output, self.golden_parsed_output6)

if __name__ == '__main__':
    unittest.main()
