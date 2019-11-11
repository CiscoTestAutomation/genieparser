# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device, loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

from genie.libs.parser.junos.show_ted import ShowTedDatabaseExtensive

'''
Unit tests for:
    * 'show ted database extensive'
    * 'show ted database extensive {node_id}'
'''
class test_show_ted_database(unittest.TestCase):
    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        show ted database extensive
        TED database: 0 ISIS nodes 6 INET nodes
        NodeID: 10.4.1.1
          Type: Rtr, Age: 1024 secs, LinkIn: 0, LinkOut: 1
          Protocol: OSPF(0.0.0.4)
            To: 172.16.1.1, Local: 10.4.0.2, Remote: 10.4.0.1
              Local interface index: 0, Remote interface index: 0
              Color: 0 <none>
              Metric: 1
              Static BW: 2000Mbps
              Reservable BW: 0bps
              Available BW [priority] bps:
                  [0] 10bps         [1] 10bps        [2] 0bps        [3] 0bps
                  [4] 10bps         [5] 0bps        [6] 0bps        [7] 0bps
              Interface Switching Capability Descriptor(1):
                Switching type: Packet
                Encoding type: Packet
                Maximum LSP BW [priority] bps:
                  [0] 0bps         [1] 0bps        [2] 0bps        [3] 0bps
                  [4] 0bps         [5] 0bps        [6] 0bps        [7] 0bps
              P2P Adjacency-SID:
                IPV4, SID: 12345, Flags: 0x24, Weight: 0
           Prefixes:
             10.4.1.1/32
              Flags: 0x60
              Prefix-SID:
                SID: 1234, Flags: 0x00, Algo: 0
           SPRING-Capabilities:
             SRGB block [Start: 12000, Range: 3000, Flags: 0x00]
           SPRING-Algorithms:
             Algo: 0
             Algo: 1
        NodeID: 10.16.2.2-1
          Type: Net, Age: 1024 secs, LinkIn: 0, LinkOut: 2
          Protocol: OSPF(0.0.0.4)
            To: 10.16.2.34, Local: 0.0.0.0, Remote: 0.0.0.0
              Local interface index: 0, Remote interface index: 0
              Metric: 0
              Interface Switching Capability Descriptor(1):
                Switching type: Packet
                Encoding type: Packet
                Maximum LSP BW [priority] bps:
                  [0] 0bps         [1] 0bps        [2] 0bps        [3] 0bps
                  [4] 0bps         [5] 0bps        [6] 1000bps        [7] 0bps
            To: 10.16.2.42, Local: 0.0.0.0, Remote: 0.0.0.0
              Local interface index: 0, Remote interface index: 0
              Metric: 0
              Interface Switching Capability Descriptor(1):
                Switching type: Packet
                Encoding type: Packet
                Maximum LSP BW [priority] bps:
                  [0] 0bps         [1] 0bps        [2] 0bps        [3] 0bps
                  [4] 0bps         [5] 0bps        [6] 0bps        [7] 0bps
        NodeID: 172.16.1.4-1
          Type: Net, Age: 2048 secs, LinkIn: 0, LinkOut: 2
          Protocol: OSPF(0.0.0.4)
            To: 172.16.85.48, Local: 0.0.0.0, Remote: 0.0.0.0
              Local interface index: 0, Remote interface index: 0
              Metric: 0
              Interface Switching Capability Descriptor(1):
                Switching type: Packet
                Encoding type: Packet
                Maximum LSP BW [priority] bps:
                  [0] 0bps         [1] 0bps        [2] 0bps        [3] 0bps
                  [4] 0bps         [5] 0bps        [6] 0bps        [7] 0bps
            To: 172.16.85.52, Local: 0.0.0.0, Remote: 0.0.0.0
              Local interface index: 0, Remote interface index: 0
              Metric: 0
              Interface Switching Capability Descriptor(1):
                Switching type: Packet
                Encoding type: Packet
                Maximum LSP BW [priority] bps:
                  [0] 0bps         [1] 0bps        [2] 0bps        [3] 0bps
                  [4] 0bps         [5] 0bps        [6] 0bps        [7] 0bps
        NodeID: 10.36.3.3
          Type: ---, Age: 3440 secs, LinkIn: 1, LinkOut: 0
        NodeID: 10.64.4.4
          Type: ---, Age: 2560 secs, LinkIn: 1, LinkOut: 0
    '''}

    golden_parsed_output = {
        'isis_nodes': 0,
        'inet_nodes': 6,
        'node': {
            '10.4.1.1': {
                'type': 'Rtr',
                'age': 1024,
                'link_in': 0,
                'link_out': 1,
                'protocol': {
                    'OSPF(0.0.0.4)': {
                        'to': {
                            '172.16.1.1': {
                                'local': {
                                    '10.4.0.2': {
                                        'remote': {
                                            '10.4.0.1': {
                                                'local_interface_index': 0,
                                                'remote_interface_index': 0,
                                                'color': '0 <none>',
                                                'metric': 1,
                                                'static_bw': '2000Mbps',
                                                'reservable_bw': '0bps',
                                                'available_bw': {
                                                    0: {
                                                        'bw': '10bps'
                                                    },
                                                    1: {
                                                        'bw': '10bps'
                                                    },
                                                    2: {
                                                        'bw': '0bps'
                                                    },
                                                    3: {
                                                        'bw': '0bps'
                                                    },
                                                    4: {
                                                        'bw': '10bps'
                                                    },
                                                    5: {
                                                        'bw': '0bps'
                                                    },
                                                    6: {
                                                        'bw': '0bps'
                                                    },
                                                    7: {
                                                        'bw': '0bps'
                                                    }
                                                },
                                                'interface_switching_capability_descriptor': {
                                                    '1': {
                                                        'switching_type': 'Packet',
                                                        'encoding_type': 'Packet',
                                                        'maximum_lsp_bw': {
                                                            0: {
                                                                'bw': '0bps'
                                                            },
                                                            1: {
                                                                'bw': '0bps'
                                                            },
                                                            2: {
                                                                'bw': '0bps'
                                                            },
                                                            3: {
                                                                'bw': '0bps'
                                                            },
                                                            4: {
                                                                'bw': '0bps'
                                                            },
                                                            5: {
                                                                'bw': '0bps'
                                                            },
                                                            6: {
                                                                'bw': '0bps'
                                                            },
                                                            7: {
                                                                'bw': '0bps'
                                                            }
                                                        }
                                                    }
                                                },
                                                'p2p_adj_sid': {
                                                    'sid': {
                                                        '12345': {
                                                            'address_family': 'IPV4',
                                                            'flags': '0x24',
                                                            'weight': 0
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        'prefixes': {
                            '10.4.1.1/32': {
                                'flags': '0x60',
                                'prefix_sid': {
                                    1234: {
                                        'flags': '0x00',
                                        'algo': 0
                                    }
                                }
                            }
                        },
                        'spring_capabilities': {
                            'srgb_block': {
                                'start': 12000,
                                'range': 3000,
                                'flags': '0x00'
                            }
                        },
                        'spring_algorithms': ['0', '1']
                    }
                }
            },
            '10.16.2.2-1': {
                'type': 'Net',
                'age': 1024,
                'link_in': 0,
                'link_out': 2,
                'protocol': {
                    'OSPF(0.0.0.4)': {
                        'to': {
                            '10.16.2.34': {
                                'local': {
                                    '0.0.0.0': {
                                        'remote': {
                                            '0.0.0.0': {
                                                'local_interface_index': 0,
                                                'remote_interface_index': 0,
                                                'metric': 0,
                                                'interface_switching_capability_descriptor': {
                                                    '1': {
                                                        'switching_type': 'Packet',
                                                        'encoding_type': 'Packet',
                                                        'maximum_lsp_bw': {
                                                            0: {
                                                                'bw': '0bps'
                                                            },
                                                            1: {
                                                                'bw': '0bps'
                                                            },
                                                            2: {
                                                                'bw': '0bps'
                                                            },
                                                            3: {
                                                                'bw': '0bps'
                                                            },
                                                            4: {
                                                                'bw': '0bps'
                                                            },
                                                            5: {
                                                                'bw': '0bps'
                                                            },
                                                            6: {
                                                                'bw': '1000bps'
                                                            },
                                                            7: {
                                                                'bw': '0bps'
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            },
                            '10.16.2.42': {
                                'local': {
                                    '0.0.0.0': {
                                        'remote': {
                                            '0.0.0.0': {
                                                'local_interface_index': 0,
                                                'remote_interface_index': 0,
                                                'metric': 0,
                                                'interface_switching_capability_descriptor': {
                                                    '1': {
                                                        'switching_type': 'Packet',
                                                        'encoding_type': 'Packet',
                                                        'maximum_lsp_bw': {
                                                            0: {
                                                                'bw': '0bps'
                                                            },
                                                            1: {
                                                                'bw': '0bps'
                                                            },
                                                            2: {
                                                                'bw': '0bps'
                                                            },
                                                            3: {
                                                                'bw': '0bps'
                                                            },
                                                            4: {
                                                                'bw': '0bps'
                                                            },
                                                            5: {
                                                                'bw': '0bps'
                                                            },
                                                            6: {
                                                                'bw': '0bps'
                                                            },
                                                            7: {
                                                                'bw': '0bps'
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
                }
            },
            '172.16.1.4-1': {
                'type': 'Net',
                'age': 2048,
                'link_in': 0,
                'link_out': 2,
                'protocol': {
                    'OSPF(0.0.0.4)': {
                        'to': {
                            '172.16.85.48': {
                                'local': {
                                    '0.0.0.0': {
                                        'remote': {
                                            '0.0.0.0': {
                                                'local_interface_index': 0,
                                                'remote_interface_index': 0,
                                                'metric': 0,
                                                'interface_switching_capability_descriptor': {
                                                    '1': {
                                                        'switching_type': 'Packet',
                                                        'encoding_type': 'Packet',
                                                        'maximum_lsp_bw': {
                                                            0: {
                                                                'bw': '0bps'
                                                            },
                                                            1: {
                                                                'bw': '0bps'
                                                            },
                                                            2: {
                                                                'bw': '0bps'
                                                            },
                                                            3: {
                                                                'bw': '0bps'
                                                            },
                                                            4: {
                                                                'bw': '0bps'
                                                            },
                                                            5: {
                                                                'bw': '0bps'
                                                            },
                                                            6: {
                                                                'bw': '0bps'
                                                            },
                                                            7: {
                                                                'bw': '0bps'
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            },
                            '172.16.85.52': {
                                'local': {
                                    '0.0.0.0': {
                                        'remote': {
                                            '0.0.0.0': {
                                                'local_interface_index': 0,
                                                'remote_interface_index': 0,
                                                'metric': 0,
                                                'interface_switching_capability_descriptor': {
                                                    '1': {
                                                        'switching_type': 'Packet',
                                                        'encoding_type': 'Packet',
                                                        'maximum_lsp_bw': {
                                                            0: {
                                                                'bw': '0bps'
                                                            },
                                                            1: {
                                                                'bw': '0bps'
                                                            },
                                                            2: {
                                                                'bw': '0bps'
                                                            },
                                                            3: {
                                                                'bw': '0bps'
                                                            },
                                                            4: {
                                                                'bw': '0bps'
                                                            },
                                                            5: {
                                                                'bw': '0bps'
                                                            },
                                                            6: {
                                                                'bw': '0bps'
                                                            },
                                                            7: {
                                                                'bw': '0bps'
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
                }
            },
            '10.36.3.3': {
                'type': '---',
                'age': 3440,
                'link_in': 1,
                'link_out': 0
            },
            '10.64.4.4': {
                'type': '---',
                'age': 2560,
                'link_in': 1,
                'link_out': 0
            }
        }
    }

    golden_output_node_id = {'execute.return_value': '''
    show ted database extensive 10.4.1.1
    TED database: 0 ISIS nodes 13 INET nodes
    NodeID: 10.4.1.1
      Type: Rtr, Age: 2048 secs, LinkIn: 6, LinkOut: 2
      Protocol: OSPF(0.0.0.4)
        To: 172.16.1.1, Local: 172.16.1.2, Remote: 172.16.1.3
          Local interface index: 123, Remote interface index: 0
          Color: 0 <none>
          Metric: 4
          Static BW: 500Mbps
          Reservable BW: 500Mbps
          Available BW [priority] bps:
              [0] 500Mbps     [1] 500Mbps    [2] 500Mbps    [3] 500Mbps
              [4] 500Mbps     [5] 500Mbps    [6] 500Mbps    [7] 500Mbps
          Interface Switching Capability Descriptor(1):
            Switching type: Packet
            Encoding type: Packet
            Maximum LSP BW [priority] bps:
              [0] 500Mbps     [1] 500Mbps    [2] 500Mbps    [3] 500Mbps
              [4] 500Mbps     [5] 500Mbps    [6] 500Mbps    [7] 500Mbps
          P2P Adjacency-SID:
            IPV4, SID: 8, Flags: 0x35, Weight: 0
        To: 172.16.1.4, Local: 172.16.1.5, Remote: 172.16.1.6
          Local interface index: 456, Remote interface index: 0
          Color: 0x2 blue
          Metric: 350
          Static BW: 500Mbps
          Reservable BW: 500Mbps
          Available BW [priority] bps:
              [0] 500Mbps     [1] 500Mbps    [2] 500Mbps    [3] 500Mbps
              [4] 500Mbps     [5] 500Mbps    [6] 500Mbps    [7] 500Mbps
          Interface Switching Capability Descriptor(1):
            Switching type: Packet
            Encoding type: Packet
            Maximum LSP BW [priority] bps:
              [0] 500Mbps     [1] 500Mbps    [2] 500Mbps    [3] 500Mbps
              [4] 500Mbps     [5] 500Mbps    [6] 500Mbps    [7] 500Mbps
          P2P Adjacency-SID:
            IPV4, SID: 39, Flags: 0x40, Weight: 0
       Prefixes:
         192.168.0.1/32
          Flags: 0x30
          Prefix-SID:
            SID: 42, Flags: 0x00, Algo: 0
       SPRING-Capabilities:
         SRGB block [Start: 8000, Range: 6000, Flags: 0x00]
       SPRING-Algorithms:
         Algo: 0
    '''}

    golden_parsed_output_node_id = {
        'isis_nodes': 0,
        'inet_nodes': 13,
        'node': {
            '10.4.1.1': {
                'type': 'Rtr',
                'age': 2048,
                'link_in': 6,
                'link_out': 2,
                'protocol': {
                    'OSPF(0.0.0.4)': {
                        'to': {
                            '172.16.1.1': {
                                'local': {
                                    '172.16.1.2': {
                                        'remote': {
                                            '172.16.1.3': {
                                                'local_interface_index': 123,
                                                'remote_interface_index': 0,
                                                'color': '0 <none>',
                                                'metric': 4,
                                                'static_bw': '500Mbps',
                                                'reservable_bw': '500Mbps',
                                                'available_bw': {
                                                    0: {
                                                        'bw': '500Mbps'
                                                    },
                                                    1: {
                                                        'bw': '500Mbps'
                                                    },
                                                    2: {
                                                        'bw': '500Mbps'
                                                    },
                                                    3: {
                                                        'bw': '500Mbps'
                                                    },
                                                    4: {
                                                        'bw': '500Mbps'
                                                    },
                                                    5: {
                                                        'bw': '500Mbps'
                                                    },
                                                    6: {
                                                        'bw': '500Mbps'
                                                    },
                                                    7: {
                                                        'bw': '500Mbps'
                                                    }
                                                },
                                                'interface_switching_capability_descriptor': {
                                                    '1': {
                                                        'switching_type': 'Packet',
                                                        'encoding_type': 'Packet',
                                                        'maximum_lsp_bw': {
                                                            0: {
                                                                'bw': '500Mbps'
                                                            },
                                                            1: {
                                                                'bw': '500Mbps'
                                                            },
                                                            2: {
                                                                'bw': '500Mbps'
                                                            },
                                                            3: {
                                                                'bw': '500Mbps'
                                                            },
                                                            4: {
                                                                'bw': '500Mbps'
                                                            },
                                                            5: {
                                                                'bw': '500Mbps'
                                                            },
                                                            6: {
                                                                'bw': '500Mbps'
                                                            },
                                                            7: {
                                                                'bw': '500Mbps'
                                                            }
                                                        }
                                                    }
                                                },
                                                'p2p_adj_sid': {
                                                    'sid': {
                                                        '8': {
                                                            'address_family': 'IPV4',
                                                            'flags': '0x35',
                                                            'weight': 0
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            },
                            '172.16.1.4': {
                                'local': {
                                    '172.16.1.5': {
                                        'remote': {
                                            '172.16.1.6': {
                                                'local_interface_index': 456,
                                                'remote_interface_index': 0,
                                                'color': '0x2 blue',
                                                'metric': 350,
                                                'static_bw': '500Mbps',
                                                'reservable_bw': '500Mbps',
                                                'available_bw': {
                                                    0: {
                                                        'bw': '500Mbps'
                                                    },
                                                    1: {
                                                        'bw': '500Mbps'
                                                    },
                                                    2: {
                                                        'bw': '500Mbps'
                                                    },
                                                    3: {
                                                        'bw': '500Mbps'
                                                    },
                                                    4: {
                                                        'bw': '500Mbps'
                                                    },
                                                    5: {
                                                        'bw': '500Mbps'
                                                    },
                                                    6: {
                                                        'bw': '500Mbps'
                                                    },
                                                    7: {
                                                        'bw': '500Mbps'
                                                    }
                                                },
                                                'interface_switching_capability_descriptor': {
                                                    '1': {
                                                        'switching_type': 'Packet',
                                                        'encoding_type': 'Packet',
                                                        'maximum_lsp_bw': {
                                                            0: {
                                                                'bw': '500Mbps'
                                                            },
                                                            1: {
                                                                'bw': '500Mbps'
                                                            },
                                                            2: {
                                                                'bw': '500Mbps'
                                                            },
                                                            3: {
                                                                'bw': '500Mbps'
                                                            },
                                                            4: {
                                                                'bw': '500Mbps'
                                                            },
                                                            5: {
                                                                'bw': '500Mbps'
                                                            },
                                                            6: {
                                                                'bw': '500Mbps'
                                                            },
                                                            7: {
                                                                'bw': '500Mbps'
                                                            }
                                                        }
                                                    }
                                                },
                                                'p2p_adj_sid': {
                                                    'sid': {
                                                        '39': {
                                                            'address_family': 'IPV4',
                                                            'flags': '0x40',
                                                            'weight': 0
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        'prefixes': {
                            '192.168.0.1/32': {
                                'flags': '0x30',
                                'prefix_sid': {
                                    42: {
                                        'flags': '0x00',
                                        'algo': 0
                                    }
                                }
                            }
                        },
                        'spring_capabilities': {
                            'srgb_block': {
                                'start': 8000,
                                'range': 6000,
                                'flags': '0x00'
                            }
                        },
                        'spring_algorithms': ['0']
                    }
                }
            }
        }
    }


    def test_show_ted_database_extensive_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowTedDatabaseExtensive(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_show_ted_database_extensive(self):
        self.device = Mock(**self.golden_output)
        obj = ShowTedDatabaseExtensive(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_show_ted_database_extensive_node_id(self):
        self.device = Mock(**self.golden_output_node_id)
        obj = ShowTedDatabaseExtensive(device=self.device)
        parsed_output = obj.parse(node_id='10.34.2.250')
        self.assertEqual(parsed_output, self.golden_parsed_output_node_id)


if __name__ == '__main__':
    unittest.main()
