#!/bin/env python
import unittest
from unittest.mock import Mock
from pyats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError
from genie.libs.parser.nxos.show_fdb import ShowMacAddressTableVni, \
    ShowMacAddressTable, ShowMacAddressTableAgingTime, \
    ShowMacAddressTableLimit, ShowSystemInternalL2fwderMac


# ==================================================
#  Unit test for: 
#   'show mac address-table vni <WORD> | grep <WORD>'
#   'show mac address-table local vni <WORD>'
#   'show mac address-table'
#   'show mac address-table aging-time'
#   'show mac address-table limit'
#   'show system internal l2fwder mac'
# ==================================================

class test_show_mac_address_table_vni(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
    'mac_table': {
        'vlans': {
            '1001': {
                'mac_addresses': {
                    '0000.04ff.b1b1': {
                        'entry': 'C',
                        'mac_address': '0000.04ff.b1b1',
                        'interfaces': {
                            'Nve1(10.9.0.101)': {
                                'age': '0',
                                'mac_type': 'dynamic',
                                'interface': 'Nve1(10.9.0.101)',
                                },
                            },
                        'ntfy': 'F',
                        'secure': 'F',
                        },
                    },
                'vlan': '1001',
                },
            },
        },
    }

    golden_output = {'execute.return_value': '''\
      CH-P2-TOR-1# show mac address-table vni 2001001 | grep nve1 
    C 1001     0000.04ff.b1b1   dynamic  0         F      F    nve1(10.9.0.101)
    '''
                     }

    golden_parsed_output_1 =  {
      'mac_table': {
          'vlans': {
              '1001': {
                  'mac_addresses': {
                      '0000.01ff.9191': {
                          'entry': '*',
                          'mac_address': '0000.01ff.9191',
                          'ntfy': 'F',
                          'interfaces': {
                              'Ethernet1/11': {
                                  'age': '0',
                                  'mac_type': 'dynamic',
                                  'interface': 'Ethernet1/11',
                                  },
                              },
                          'secure': 'F',
                          },
                      '00f1.00ff.0000': {
                          'entry': '*',
                          'mac_address': '00f1.00ff.0000',
                          'ntfy': 'F',
                          'interfaces': {
                              'Ethernet1/11': {
                                  'age': '0',
                                  'mac_type': 'dynamic',
                                  'interface': 'Ethernet1/11',
                                  },
                              },
                          'secure': 'F',
                          },
                      '00f5.00ff.0000': {
                          'entry': '*',
                          'mac_address': '00f5.00ff.0000',
                          'ntfy': 'F',
                          'interfaces': {
                              'Ethernet1/11': {
                                  'age': '0',
                                  'mac_type': 'dynamic',
                                  'interface': 'Ethernet1/11',
                                  },
                              },
                          'secure': 'F',
                          },
                      },
                  'vlan': '1001',
                  },
              },
          },
      }

    golden_output_1 = {'execute.return_value': '''\
CH-P2-TOR-1# show mac address-table local vni 2001001 
Legend: 
        * - primary entry, G - Gateway MAC, (R) - Routed MAC, O - Overlay MAC
        age - seconds since last seen,+ - primary entry using vPC Peer-Link,
        (T) - True, (F) - False, C - ControlPlane MAC, ~ - vsan
   VLAN     MAC Address      Type      age     Secure NTFY Ports
---------+-----------------+--------+---------+------+----+------------------
* 1001     0000.01ff.9191   dynamic  0         F      F    Eth1/11
* 1001     00f1.00ff.0000   dynamic  0         F      F    Eth1/11
* 1001     00f5.00ff.0000   dynamic  0         F      F    Eth1/11
    '''
                       }

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowMacAddressTableVni(device=self.device)
        parsed_output = obj.parse(vni='2001001', interface='nve1')
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowMacAddressTableVni(device=self.device)
        parsed_output = obj.parse(vni='2001001')
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowMacAddressTableVni(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(vni='2001001', interface='nve1')


class test_show_mac_address_table_aging_time(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {'mac_aging_time': 120}

    golden_output = {'execute.return_value': '''\
        N95_1# show mac address-table aging-time 
        Aging Time
        ----------
            120
    '''
                     }

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowMacAddressTableAgingTime(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowMacAddressTableAgingTime(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


class test_show_mac_address_table(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output =  {
      'mac_table': {
          'vlans': {
              '-': {
                  'mac_addresses': {
                      '0000.deff.6c9d': {
                          'entry': 'G',
                          'mac_address': '0000.deff.6c9d',
                          'ntfy': 'F',
                          'interfaces': {
                              'Sup-eth1(R)': {
                                  'age': '-',
                                  'mac_type': 'static',
                                  'interface': 'Sup-eth1(R)',
                                  },
                              },
                          'secure': 'F',
                          },
                      '5e00.c0ff.0007': {
                          'entry': 'G',
                          'mac_address': '5e00.c0ff.0007',
                          'ntfy': 'F',
                          'interfaces': {
                              '(R)': {
                                  'age': '-',
                                  'mac_type': 'static',
                                  'interface': '(R)',
                                  },
                              'Sup-eth1(R)(Lo0)': {
                                  'age': '-',
                                  'mac_type': 'static',
                                  'interface': 'Sup-eth1(R)(Lo0)',
                                  },
                              },
                          'secure': 'F',
                          }
                      },
                  'vlan': '-',
                  },
              '10': {
                  'mac_addresses': {
                      'aaaa.bbff.8888': {
                          'entry': '*',
                          'mac_address': 'aaaa.bbff.8888',
                          'ntfy': 'F',
                          'interfaces': {
                              'Ethernet1/2': {
                                  'age': '-',
                                  'mac_type': 'static',
                                  'interface': 'Ethernet1/2',
                                  },
                              },
                          'secure': 'F',
                          },
                      },
                  'vlan': '10',
                  },
              '100': {
                  'mac_addresses': {
                      '5e00.c0ff.0007': {
                          'entry': 'G',
                          'mac_address': '5e00.c0ff.0007',
                          'ntfy': 'F',
                          'interfaces': {
                              'Sup-eth1(R)': {
                                  'age': '-',
                                  'mac_type': 'static',
                                  'interface': 'Sup-eth1(R)',
                                  },
                              },
                          'secure': 'F',
                          },
                      },
                  'vlan': '100',
                  },
              '1000': {
                  'mac_addresses': {
                      '5e00.c0ff.0007': {
                          'entry': 'G',
                          'mac_address': '5e00.c0ff.0007',
                          'ntfy': 'F',
                          'interfaces': {
                              'Sup-eth1(R)': {
                                  'age': '-',
                                  'mac_type': 'static',
                                  'interface': 'Sup-eth1(R)',
                                  },
                              },
                          'secure': 'F',
                          },
                      },
                  'vlan': '1000',
                  },
              '1005': {
                  'mac_addresses': {
                      '5e00.c0ff.0007': {
                          'entry': 'G',
                          'mac_address': '5e00.c0ff.0007',
                          'ntfy': 'F',
                          'interfaces': {
                              'Sup-eth1(R)': {
                                  'age': '-',
                                  'mac_type': 'static',
                                  'interface': 'Sup-eth1(R)',
                                  },
                              },
                          'secure': 'F',
                          },
                      },
                  'vlan': '1005',
                  },
              '1006': {
                  'mac_addresses': {
                      '5e00.c0ff.0007': {
                          'entry': 'G',
                          'mac_address': '5e00.c0ff.0007',
                          'ntfy': 'F',
                          'interfaces': {
                              'Sup-eth1(R)': {
                                  'age': '-',
                                  'mac_type': 'static',
                                  'interface': 'Sup-eth1(R)',
                                  },
                              },
                          'secure': 'F',
                          },
                      },
                  'vlan': '1006',
                  },
              '1007': {
                  'mac_addresses': {
                      '5e00.c0ff.0007': {
                          'entry': 'G',
                          'mac_address': '5e00.c0ff.0007',
                          'ntfy': 'F',
                          'interfaces': {
                              'Sup-eth1(R)': {
                                  'age': '-',
                                  'mac_type': 'static',
                                  'interface': 'Sup-eth1(R)',
                                  },
                              },
                          'secure': 'F',
                          },
                      },
                  'vlan': '1007',
                  },
              '1008': {
                  'mac_addresses': {
                      '5e00.c0ff.0007': {
                          'entry': 'G',
                          'mac_address': '5e00.c0ff.0007',
                          'ntfy': 'F',
                          'interfaces': {
                              'Sup-eth1(R)': {
                                  'age': '-',
                                  'mac_type': 'static',
                                  'interface': 'Sup-eth1(R)',
                                  },
                              },
                          'secure': 'F',
                          },
                      },
                  'vlan': '1008',
                  },
              '1009': {
                  'mac_addresses': {
                      '5e00.c0ff.0007': {
                          'entry': 'G',
                          'mac_address': '5e00.c0ff.0007',
                          'ntfy': 'F',
                          'interfaces': {
                              'Sup-eth1(R)': {
                                  'age': '-',
                                  'mac_type': 'static',
                                  'interface': 'Sup-eth1(R)',
                                  },
                              },
                          'secure': 'F',
                          },
                      },
                  'vlan': '1009',
                  },
              '101': {
                  'mac_addresses': {
                      '5e00.c0ff.0007': {
                          'entry': 'G',
                          'mac_address': '5e00.c0ff.0007',
                          'ntfy': 'F',
                          'interfaces': {
                              'Sup-eth1(R)': {
                                  'age': '-',
                                  'mac_type': 'static',
                                  'interface': 'Sup-eth1(R)',
                                  },
                              },
                          'secure': 'F',
                          },
                      },
                  'vlan': '101',
                  },
              '102': {
                  'mac_addresses': {
                      '5e00.c0ff.0007': {
                          'entry': 'G',
                          'mac_address': '5e00.c0ff.0007',
                          'ntfy': 'F',
                          'interfaces': {
                              'Sup-eth1(R)': {
                                  'age': '-',
                                  'mac_type': 'static',
                                  'interface': 'Sup-eth1(R)',
                                  },
                              },
                          'secure': 'F',
                          },
                      },
                  'vlan': '102',
                  },
              '103': {
                  'mac_addresses': {
                      '5e00.c0ff.0007': {
                          'entry': 'G',
                          'mac_address': '5e00.c0ff.0007',
                          'ntfy': 'F',
                          'interfaces': {
                              'Sup-eth1(R)': {
                                  'age': '-',
                                  'mac_type': 'static',
                                  'interface': 'Sup-eth1(R)',
                                  },
                              },
                          'secure': 'F',
                          },
                      },
                  'vlan': '103',
                  },
              '105': {
                  'mac_addresses': {
                      '5e00.c0ff.0007': {
                          'entry': 'G',
                          'mac_address': '5e00.c0ff.0007',
                          'ntfy': 'F',
                          'interfaces': {
                              'Sup-eth1(R)': {
                                  'age': '-',
                                  'mac_type': 'static',
                                  'interface': 'Sup-eth1(R)',
                                  },
                              },
                          'secure': 'F',
                          },
                      },
                  'vlan': '105',
                  },
              '106': {
                  'mac_addresses': {
                      '5e00.c0ff.0007': {
                          'entry': 'G',
                          'mac_address': '5e00.c0ff.0007',
                          'ntfy': 'F',
                          'interfaces': {
                              'Sup-eth1(R)': {
                                  'age': '-',
                                  'mac_type': 'static',
                                  'interface': 'Sup-eth1(R)',
                                  },
                              },
                          'secure': 'F',
                          },
                      },
                  'vlan': '106',
                  },
              '107': {
                  'mac_addresses': {
                      '5e00.c0ff.0007': {
                          'entry': 'G',
                          'mac_address': '5e00.c0ff.0007',
                          'ntfy': 'F',
                          'interfaces': {
                              'Sup-eth1(R)': {
                                  'age': '-',
                                  'mac_type': 'static',
                                  'interface': 'Sup-eth1(R)',
                                  },
                              },
                          'secure': 'F',
                          },
                      },
                  'vlan': '107',
                  },
              '108': {
                  'mac_addresses': {
                      '5e00.c0ff.0007': {
                          'entry': 'G',
                          'mac_address': '5e00.c0ff.0007',
                          'ntfy': 'F',
                          'interfaces': {
                              'Sup-eth1(R)': {
                                  'age': '-',
                                  'mac_type': 'static',
                                  'interface': 'Sup-eth1(R)',
                                  },
                              },
                          'secure': 'F',
                          },
                      },
                  'vlan': '108',
                  },
              '109': {
                  'mac_addresses': {
                      '5e00.c0ff.0007': {
                          'entry': 'G',
                          'mac_address': '5e00.c0ff.0007',
                          'ntfy': 'F',
                          'interfaces': {
                              'Sup-eth1(R)': {
                                  'age': '-',
                                  'mac_type': 'static',
                                  'interface': 'Sup-eth1(R)',
                                  },
                              },
                          'secure': 'F',
                          },
                      },
                  'vlan': '109',
                  },
              '110': {
                  'mac_addresses': {
                      '5e00.c0ff.0007': {
                          'entry': 'G',
                          'mac_address': '5e00.c0ff.0007',
                          'ntfy': 'F',
                          'interfaces': {
                              'Sup-eth1(R)': {
                                  'age': '-',
                                  'mac_type': 'static',
                                  'interface': 'Sup-eth1(R)',
                                  },
                              },
                          'secure': 'F',
                          },
                      },
                  'vlan': '110',
                  },
              '111': {
                  'mac_addresses': {
                      '5e00.c0ff.0007': {
                          'entry': 'G',
                          'mac_address': '5e00.c0ff.0007',
                          'ntfy': 'F',
                          'interfaces': {
                              'Sup-eth1(R)': {
                                  'age': '-',
                                  'mac_type': 'static',
                                  'interface': 'Sup-eth1(R)',
                                  },
                              },
                          'secure': 'F',
                          },
                      },
                  'vlan': '111',
                  },
              '112': {
                  'mac_addresses': {
                      '5e00.c0ff.0007': {
                          'entry': 'G',
                          'mac_address': '5e00.c0ff.0007',
                          'ntfy': 'F',
                          'interfaces': {
                              'Sup-eth1(R)': {
                                  'age': '-',
                                  'mac_type': 'static',
                                  'interface': 'Sup-eth1(R)',
                                  },
                              },
                          'secure': 'F',
                          },
                      },
                  'vlan': '112',
                  },
              '113': {
                  'mac_addresses': {
                      '5e00.c0ff.0007': {
                          'entry': 'G',
                          'mac_address': '5e00.c0ff.0007',
                          'ntfy': 'F',
                          'interfaces': {
                              'Sup-eth1(R)': {
                                  'age': '-',
                                  'mac_type': 'static',
                                  'interface': 'Sup-eth1(R)',
                                  },
                              },
                          'secure': 'F',
                          },
                      },
                  'vlan': '113',
                  },
              '114': {
                  'mac_addresses': {
                      '5e00.c0ff.0007': {
                          'entry': 'G',
                          'mac_address': '5e00.c0ff.0007',
                          'ntfy': 'F',
                          'interfaces': {
                              'Sup-eth1(R)': {
                                  'age': '-',
                                  'mac_type': 'static',
                                  'interface': 'Sup-eth1(R)',
                                  },
                              },
                          'secure': 'F',
                          },
                      },
                  'vlan': '114',
                  },
              '20': {
                  'mac_addresses': {
                      'aaaa.bbff.8888': {
                          'drop': {
                              'age': '-',
                              'drop': True,
                              'mac_type': 'static',
                              },
                          'entry': '*',
                          'mac_address': 'aaaa.bbff.8888',
                          'ntfy': 'F',
                          'secure': 'F',
                          },
                      },
                  'vlan': '20',
                  },
              '30': {
                  'mac_addresses': {
                      'aaaa.bbff.8888': {
                          'drop': {
                              'age': '-',
                              'drop': True,
                              'mac_type': 'static',
                              },
                          'entry': '*',
                          'mac_address': 'aaaa.bbff.8888',
                          'ntfy': 'F',
                          'secure': 'F',
                          },
                      },
                  'vlan': '30',
                  },
              '2000': {
                  'mac_addresses': {
                      '7e00.c0ff.0007': {
                          'mac_address': '7e00.c0ff.0007',
                          'ntfy': 'F',
                          'interfaces': {
                              'vPC Peer-Link(R)': {
                                  'age': '-',
                                  'mac_type': 'static',
                                  'interface': 'vPC Peer-Link(R)',
                                  },
                              },
                          'secure': 'F',
                          },
                      },
                  'vlan': '2000',
                  },
              '3000': {
                  'mac_addresses': {
                      '5e00.c0ff.0007': {
                          'mac_address': '5e00.c0ff.0007',
                          'ntfy': 'F',
                          'interfaces': {
                              'Sup-eth1(R)': {
                                  'age': '-',
                                  'mac_type': 'static',
                                  'interface': 'Sup-eth1(R)',
                                  },
                              },
                          'secure': 'F',
                          },
                      },
                  'vlan': '3000',
                  },
              '4000': {
                  'mac_addresses': {
                      '5e00.c0ff.0007': {
                          'mac_address': '5e00.c0ff.0007',
                          'ntfy': 'F',
                          'interfaces': {
                              'Sup-eth1(R)': {
                                  'age': '~~~',
                                  'mac_type': 'static',
                                  'interface': 'Sup-eth1(R)',
                                  },
                              },
                          'secure': 'F',
                          },
                      },
                  'vlan': '4000',
                  }
              }
          }
      }

    golden_output = {'execute.return_value': '''\
    N95_1# show mac address-table 
    Legend: 
        * - primary entry, G - Gateway MAC, (R) - Routed MAC, O - Overlay MAC
        age - seconds since last seen,+ - primary entry using vPC Peer-Link,
        (T) - True, (F) - False, C - ControlPlane MAC, ~ - vsan
       VLAN     MAC Address      Type      age     Secure NTFY Ports
    ---------+-----------------+--------+---------+------+----+---------------
    *   10     aaaa.bbff.8888   static   -         F      F    Eth1/2
    *   20     aaaa.bbff.8888   static   -         F      F    Drop
    *   30     aaaa.bbff.8888   static   -         F      F    Drop
    G    -     0000.deff.6c9d   static   -         F      F    sup-eth1(R)
    G    -     5e00.c0ff.0007   static   -         F      F     (R)
    G    -     5e00.c0ff.0007   static   -         F      F  sup-eth1(R) (Lo0)
    G  100     5e00.c0ff.0007   static   -         F      F    sup-eth1(R)
    G  101     5e00.c0ff.0007   static   -         F      F    sup-eth1(R)
    G  102     5e00.c0ff.0007   static   -         F      F    sup-eth1(R)
    G  103     5e00.c0ff.0007   static   -         F      F    sup-eth1(R)
    G  105     5e00.c0ff.0007   static   -         F      F    sup-eth1(R)
    G  106     5e00.c0ff.0007   static   -         F      F    sup-eth1(R)
    G  107     5e00.c0ff.0007   static   -         F      F    sup-eth1(R)
    G  108     5e00.c0ff.0007   static   -         F      F    sup-eth1(R)
    G  109     5e00.c0ff.0007   static   -         F      F    sup-eth1(R)
    G  110     5e00.c0ff.0007   static   -         F      F    sup-eth1(R)
    G  111     5e00.c0ff.0007   static   -         F      F    sup-eth1(R)
    G  112     5e00.c0ff.0007   static   -         F      F    sup-eth1(R)
    G  113     5e00.c0ff.0007   static   -         F      F    sup-eth1(R)
    G  114     5e00.c0ff.0007   static   -         F      F    sup-eth1(R)
    G 1000     5e00.c0ff.0007   static   -         F      F    sup-eth1(R)
    G 1005     5e00.c0ff.0007   static   -         F      F    sup-eth1(R)
    G 1006     5e00.c0ff.0007   static   -         F      F    sup-eth1(R)
    G 1007     5e00.c0ff.0007   static   -         F      F    sup-eth1(R)
    G 1008     5e00.c0ff.0007   static   -         F      F    sup-eth1(R)
    G 1009     5e00.c0ff.0007   static   -         F      F    sup-eth1(R)
      2000     7e00.c0ff.0007    static       -       F    F  vPC Peer-Link(R)
      3000     5e00.c0ff.0007   static   -         F      F    sup-eth1(R)
      4000     5e00.c0ff.0007   static   ~~~         F      F    sup-eth1(R)

    '''
    }

    golden_output_address_interface_vlan = {'execute.return_value': '''
        N95_1# show mac address-table address 5e00.c0ff.0007 interface ethernet1/2 vlan 1006
        Legend: 
            * - primary entry, G - Gateway MAC, (R) - Routed MAC, O - Overlay MAC
            age - seconds since last seen,+ - primary entry using vPC Peer-Link,
            (T) - True, (F) - False, C - ControlPlane MAC, ~ - vsan
           VLAN     MAC Address      Type      age     Secure NTFY Ports
        ---------+-----------------+--------+---------+------+----+---------------
        G 1006     5e00.c0ff.0007   static   -         F      F    Eth1/2
        '''}

    golden_parsed_output_address_interface_vlan = {
        'mac_table': {
            'vlans': {
                '1006': {
                    'vlan': '1006',
                    'mac_addresses': {
                        '5e00.c0ff.0007': {
                            'mac_address': '5e00.c0ff.0007',
                            'entry': 'G',
                            'interfaces': {
                                'Ethernet1/2': {
                                    'interface': 'Ethernet1/2',
                                    'mac_type': 'static',
                                    'age': '-'
                                }
                            },
                            'secure': 'F',
                            'ntfy': 'F'
                        }
                    }
                }
            }
        }
    }

    golden_output_address_interface = {'execute.return_value': '''
        N95_1# show mac address-table address 5e00.c0ff.0007 interface ethernet1/2
        Legend: 
            * - primary entry, G - Gateway MAC, (R) - Routed MAC, O - Overlay MAC
            age - seconds since last seen,+ - primary entry using vPC Peer-Link,
            (T) - True, (F) - False, C - ControlPlane MAC, ~ - vsan
           VLAN     MAC Address      Type      age     Secure NTFY Ports
        ---------+-----------------+--------+---------+------+----+---------------
        G  102     5e00.c0ff.0007   static   -         F      F    Eth1/2
        G  107     5e00.c0ff.0007   static   -         F      F    Eth1/2
        G 1006     5e00.c0ff.0007   static   -         F      F    Eth1/2
        '''}

    golden_parsed_output_address_interface = {
        'mac_table': {
            'vlans': {
                '102': {
                    'vlan': '102',
                    'mac_addresses': {
                        '5e00.c0ff.0007': {
                            'mac_address': '5e00.c0ff.0007',
                            'entry': 'G',
                            'interfaces': {
                                'Ethernet1/2': {
                                    'interface': 'Ethernet1/2',
                                    'mac_type': 'static',
                                    'age': '-'
                                }
                            },
                            'secure': 'F',
                            'ntfy': 'F'
                        }
                    }
                },
                '107': {
                    'vlan': '107',
                    'mac_addresses': {
                        '5e00.c0ff.0007': {
                            'mac_address': '5e00.c0ff.0007',
                            'entry': 'G',
                            'interfaces': {
                                'Ethernet1/2': {
                                    'interface': 'Ethernet1/2',
                                    'mac_type': 'static',
                                    'age': '-'
                                }
                            },
                            'secure': 'F',
                            'ntfy': 'F'
                        }
                    }
                },
                '1006': {
                    'vlan': '1006',
                    'mac_addresses': {
                        '5e00.c0ff.0007': {
                            'mac_address': '5e00.c0ff.0007',
                            'entry': 'G',
                            'interfaces': {
                                'Ethernet1/2': {
                                    'interface': 'Ethernet1/2',
                                    'mac_type': 'static',
                                    'age': '-'
                                }
                            },
                            'secure': 'F',
                            'ntfy': 'F'
                        }
                    }
                }
            }
        }
    }

    golden_output_2 = {'execute.return_value': '''
    +++ genie_device: executing command 'show mac address-table' +++
    
    show mac address-table
    
    Legend:
    
        * - primary entry, G - Gateway MAC, (R) - Routed MAC, O - Overlay MAC

        age - seconds since last seen,+ - primary entry using vPC Peer-Link,

        (T) - True, (F) - False, C - ControlPlane MAC, ~ - vsan
    
       VLAN     MAC Address      Type      age     Secure NTFY Ports
    
    ---------+-----------------+--------+---------+------+----+------------------
    
    *  390     000f.53ff.e5a5   dynamic  0         F      F    Po113
    
    +  390     000f.53ff.1446   dynamic  0         F      F    Po103
    
    +  390     000f.53ff.d708   dynamic  0         F      F    Po115
    
    *  390     000f.53ff.fd77   dynamic  0         F      F    Po116
    
    *  390     000f.53ff.d0fc   dynamic  0         F      F    Po127
    
    *  390     000f.53ff.037d   dynamic  0         F      F    Po133
    
    +  390     000f.53ff.061e   dynamic  0         F      F    Po132
    
    *  390     000f.53ff.1e9c   dynamic  0         F      F    Po124
    
    +  390     000f.53ff.1f1d   dynamic  0         F      F    Po125             
    '''}

    golden_parsed_output_2 = {
        'mac_table': {
            'vlans': {
                '390': {
                    'mac_addresses': {
                        '000f.53ff.e5a5': {
                            'entry': '*',
                            'interfaces': {
                                'Port-channel113': {
                                    'age': '0',
                                    'interface': 'Port-channel113',
                                    'mac_type': 'dynamic',
                                },
                            },
                            'mac_address': '000f.53ff.e5a5',
                            'ntfy': 'F',
                            'secure': 'F',
                        },
                        '000f.53ff.1446': {
                            'entry': '+',
                            'interfaces': {
                                'Port-channel103': {
                                    'age': '0',
                                    'interface': 'Port-channel103',
                                    'mac_type': 'dynamic',
                                },
                            },
                            'mac_address': '000f.53ff.1446',
                            'ntfy': 'F',
                            'secure': 'F',
                        },
                        '000f.53ff.d708': {
                            'entry': '+',
                            'interfaces': {
                                'Port-channel115': {
                                    'age': '0',
                                    'interface': 'Port-channel115',
                                    'mac_type': 'dynamic',
                                },
                            },
                            'mac_address': '000f.53ff.d708',
                            'ntfy': 'F',
                            'secure': 'F',
                        },
                        '000f.53ff.fd77': {
                            'entry': '*',
                            'interfaces': {
                                'Port-channel116': {
                                    'age': '0',
                                    'interface': 'Port-channel116',
                                    'mac_type': 'dynamic',
                                },
                            },
                            'mac_address': '000f.53ff.fd77',
                            'ntfy': 'F',
                            'secure': 'F',
                        },
                        '000f.53ff.d0fc': {
                            'entry': '*',
                            'interfaces': {
                                'Port-channel127': {
                                    'age': '0',
                                    'interface': 'Port-channel127',
                                    'mac_type': 'dynamic',
                                },
                            },
                            'mac_address': '000f.53ff.d0fc',
                            'ntfy': 'F',
                            'secure': 'F',
                        },
                        '000f.53ff.037d': {
                            'entry': '*',
                            'interfaces': {
                                'Port-channel133': {
                                    'age': '0',
                                    'interface': 'Port-channel133',
                                    'mac_type': 'dynamic',
                                },
                            },
                            'mac_address': '000f.53ff.037d',
                            'ntfy': 'F',
                            'secure': 'F',
                        },
                        '000f.53ff.061e': {
                            'entry': '+',
                            'interfaces': {
                                'Port-channel132': {
                                    'age': '0',
                                    'interface': 'Port-channel132',
                                    'mac_type': 'dynamic',
                                },
                            },
                            'mac_address': '000f.53ff.061e',
                            'ntfy': 'F',
                            'secure': 'F',
                        },
                        '000f.53ff.1e9c': {
                            'entry': '*',
                            'interfaces': {
                                'Port-channel124': {
                                    'age': '0',
                                    'interface': 'Port-channel124',
                                    'mac_type': 'dynamic',
                                },
                            },
                            'mac_address': '000f.53ff.1e9c',
                            'ntfy': 'F',
                            'secure': 'F',
                        },
                        '000f.53ff.1f1d': {
                            'entry': '+',
                            'interfaces': {
                                'Port-channel125': {
                                    'age': '0',
                                    'interface': 'Port-channel125',
                                    'mac_type': 'dynamic',
                                },
                            },
                            'mac_address': '000f.53ff.1f1d',
                            'ntfy': 'F',
                            'secure': 'F',
                        },
                    },
                    'vlan': '390',
                },
            },
        },
    }

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowMacAddressTable(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowMacAddressTable(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_address_interface_vlan(self):
        self.device = Mock(**self.golden_output_address_interface_vlan)
        obj = ShowMacAddressTable(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_address_interface_vlan)

    def test_address_interface(self):
        self.device = Mock(**self.golden_output_address_interface)
        obj = ShowMacAddressTable(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_address_interface)

    def test_address_table_2(self):
        self.device = Mock(**self.golden_output_2)
        obj = ShowMacAddressTable(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_2)


class test_show_mac_address_table_limit(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
      'configured_system_action': 'Flood',
      'configured_system_limit': 111,
      'current_system_count': 3,
      'currently_system_is': 'Flooding Unknown SA',
      'mac_table': {
          'vlans': {
              '1': {
                  'cfg_action': 'Flood',
                  'conf_limit': 196000,
                  'curr_count': 0,
                  'currently': 'Flooding Unknown SA',
                  'vlan': '1',
                  },
              '10': {
                  'cfg_action': 'Flood',
                  'conf_limit': 196000,
                  'curr_count': 1,
                  'currently': 'Flooding Unknown SA',
                  'vlan': '10',
                  },
              '100': {
                  'cfg_action': 'Flood',
                  'conf_limit': 200,
                  'curr_count': 0,
                  'currently': 'Flooding Unknown SA',
                  'vlan': '100',
                  },
              '1000': {
                  'cfg_action': 'Flood',
                  'conf_limit': 196000,
                  'curr_count': 0,
                  'currently': 'Flooding Unknown SA',
                  'vlan': '1000',
                  },
              '1005': {
                  'cfg_action': 'Flood',
                  'conf_limit': 196000,
                  'curr_count': 0,
                  'currently': 'Flooding Unknown SA',
                  'vlan': '1005',
                  },
              '1006': {
                  'cfg_action': 'Flood',
                  'conf_limit': 196000,
                  'curr_count': 0,
                  'currently': 'Flooding Unknown SA',
                  'vlan': '1006',
                  },
              '1007': {
                  'cfg_action': 'Flood',
                  'conf_limit': 196000,
                  'curr_count': 0,
                  'currently': 'Flooding Unknown SA',
                  'vlan': '1007',
                  },
              '1008': {
                  'cfg_action': 'Flood',
                  'conf_limit': 196000,
                  'curr_count': 0,
                  'currently': 'Flooding Unknown SA',
                  'vlan': '1008',
                  },
              '1009': {
                  'cfg_action': 'Flood',
                  'conf_limit': 196000,
                  'curr_count': 0,
                  'currently': 'Flooding Unknown SA',
                  'vlan': '1009',
                  },
              '101': {
                  'cfg_action': 'Flood',
                  'conf_limit': 196000,
                  'curr_count': 0,
                  'currently': 'Flooding Unknown SA',
                  'vlan': '101',
                  },
              '102': {
                  'cfg_action': 'Flood',
                  'conf_limit': 196000,
                  'curr_count': 0,
                  'currently': 'Flooding Unknown SA',
                  'vlan': '102',
                  },
              '103': {
                  'cfg_action': 'Flood',
                  'conf_limit': 196000,
                  'curr_count': 0,
                  'currently': 'Flooding Unknown SA',
                  'vlan': '103',
                  },
              '104': {
                  'cfg_action': 'Flood',
                  'conf_limit': 196000,
                  'curr_count': 0,
                  'currently': 'Flooding Unknown SA',
                  'vlan': '104',
                  },
              '105': {
                  'cfg_action': 'Flood',
                  'conf_limit': 196000,
                  'curr_count': 0,
                  'currently': 'Flooding Unknown SA',
                  'vlan': '105',
                  },
              '106': {
                  'cfg_action': 'Flood',
                  'conf_limit': 196000,
                  'curr_count': 0,
                  'currently': 'Flooding Unknown SA',
                  'vlan': '106',
                  },
              '107': {
                  'cfg_action': 'Flood',
                  'conf_limit': 196000,
                  'curr_count': 0,
                  'currently': 'Flooding Unknown SA',
                  'vlan': '107',
                  },
              '108': {
                  'cfg_action': 'Flood',
                  'conf_limit': 196000,
                  'curr_count': 0,
                  'currently': 'Flooding Unknown SA',
                  'vlan': '108',
                  },
              '109': {
                  'cfg_action': 'Flood',
                  'conf_limit': 196000,
                  'curr_count': 0,
                  'currently': 'Flooding Unknown SA',
                  'vlan': '109',
                  },
              '110': {
                  'cfg_action': 'Flood',
                  'conf_limit': 196000,
                  'curr_count': 0,
                  'currently': 'Flooding Unknown SA',
                  'vlan': '110',
                  },
              '111': {
                  'cfg_action': 'Flood',
                  'conf_limit': 196000,
                  'curr_count': 0,
                  'currently': 'Flooding Unknown SA',
                  'vlan': '111',
                  },
              '112': {
                  'cfg_action': 'Flood',
                  'conf_limit': 196000,
                  'curr_count': 0,
                  'currently': 'Flooding Unknown SA',
                  'vlan': '112',
                  },
              '113': {
                  'cfg_action': 'Flood',
                  'conf_limit': 196000,
                  'curr_count': 0,
                  'currently': 'Flooding Unknown SA',
                  'vlan': '113',
                  },
              '114': {
                  'cfg_action': 'Flood',
                  'conf_limit': 196000,
                  'curr_count': 0,
                  'currently': 'Flooding Unknown SA',
                  'vlan': '114',
                  },
              '115': {
                  'cfg_action': 'Flood',
                  'conf_limit': 196000,
                  'curr_count': 0,
                  'currently': 'Flooding Unknown SA',
                  'vlan': '115',
                  },
              '185': {
                  'cfg_action': 'Flood',
                  'conf_limit': 196000,
                  'curr_count': 0,
                  'currently': 'Flooding Unknown SA',
                  'vlan': '185',
                  },
              '20': {
                  'cfg_action': 'Flood',
                  'conf_limit': 196000,
                  'curr_count': 1,
                  'currently': 'Flooding Unknown SA',
                  'vlan': '20',
                  },
              '285': {
                  'cfg_action': 'Flood',
                  'conf_limit': 196000,
                  'curr_count': 0,
                  'currently': 'Flooding Unknown SA',
                  'vlan': '285',
                  },
              '30': {
                  'cfg_action': 'Flood',
                  'conf_limit': 196000,
                  'curr_count': 1,
                  'currently': 'Flooding Unknown SA',
                  'vlan': '30',
                  },
              '910': {
                  'cfg_action': 'Flood',
                  'conf_limit': 196000,
                  'curr_count': 0,
                  'currently': 'Flooding Unknown SA',
                  'vlan': '910',
                  },
              },
          },
      }

    golden_output = {'execute.return_value': '''\
        N95_1# show mac address-table limit 
         
        Configured System Limit: 111
        Current System Count: 3
        Configured System Action: Flood
        Currently System is: Flooding Unknown SA
         
         
    Vlan    Conf Limit     Curr Count    Cfg Action    Currently
    ----    ------------   ---------     ---------    --------
    1       196000              0           Flood         Flooding Unknown SA
    10      196000              1           Flood         Flooding Unknown SA
    20      196000              1           Flood         Flooding Unknown SA
    30      196000              1           Flood         Flooding Unknown SA
    100     200               0           Flood         Flooding Unknown SA
    101     196000              0           Flood         Flooding Unknown SA
    102     196000              0           Flood         Flooding Unknown SA
    103     196000              0           Flood         Flooding Unknown SA
    104     196000              0           Flood         Flooding Unknown SA
    105     196000              0           Flood         Flooding Unknown SA
    106     196000              0           Flood         Flooding Unknown SA
    107     196000              0           Flood         Flooding Unknown SA
    108     196000              0           Flood         Flooding Unknown SA
    109     196000              0           Flood         Flooding Unknown SA
    110     196000              0           Flood         Flooding Unknown SA
    111     196000              0           Flood         Flooding Unknown SA
    112     196000              0           Flood         Flooding Unknown SA
    113     196000              0           Flood         Flooding Unknown SA
    114     196000              0           Flood         Flooding Unknown SA
    115     196000              0           Flood         Flooding Unknown SA
    185     196000              0           Flood         Flooding Unknown SA
    285     196000              0           Flood         Flooding Unknown SA
    910     196000              0           Flood         Flooding Unknown SA
    1000    196000              0           Flood         Flooding Unknown SA
    1005    196000              0           Flood         Flooding Unknown SA
    1006    196000              0           Flood         Flooding Unknown SA
    1007    196000              0           Flood         Flooding Unknown SA
    1008    196000              0           Flood         Flooding Unknown SA
    1009    196000              0           Flood         Flooding Unknown SA
    '''
                     }

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowMacAddressTableLimit(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowMacAddressTableLimit(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


class test_show_system_internal_l2fwder_mac(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
      'mac_table': {
          'vlans': {
              '-': {
                  'mac_addresses': {
                      '5e00:c000:0007': {
                          'entry': 'G',
                          'mac_address': '5e00:c000:0007',
                          'ntfy': 'F',
                          'interfaces': {
                              'Sup-eth1(R)': {
                                  'age': '-',
                                  'mac_type': 'static',
                                  'interface': 'Sup-eth1(R)',
                                  },
                              },
                          'secure': 'F',
                          },
                      },
                  'vlan': '-',
                  },
              '10': {
                  'mac_addresses': {
                      'aaaa.bbff.8888': {
                          'entry': '*',
                          'mac_address': 'aaaa.bbff.8888',
                          'ntfy': 'F',
                          'interfaces': {
                              'Ethernet1/2': {
                                  'age': '-',
                                  'mac_type': 'static',
                                  'interface': 'Ethernet1/2',
                                  },
                              },
                          'secure': 'F',
                          },
                      },
                  'vlan': '10',
                  },
              '100': {
                  'mac_addresses': {
                      '5e00.c0ff.0007': {
                          'entry': 'G',
                          'mac_address': '5e00.c0ff.0007',
                          'ntfy': 'F',
                          'interfaces': {
                              'Sup-eth1(R)': {
                                  'age': '-',
                                  'mac_type': 'static',
                                  'interface': 'Sup-eth1(R)',
                                  },
                              },
                          'secure': 'F',
                          },
                      },
                  'vlan': '100',
                  },
              '1000': {
                  'mac_addresses': {
                      '5e00.c0ff.0007': {
                          'entry': 'G',
                          'mac_address': '5e00.c0ff.0007',
                          'ntfy': 'F',
                          'interfaces': {
                              'Sup-eth1(R)': {
                                  'age': '-',
                                  'mac_type': 'static',
                                  'interface': 'Sup-eth1(R)',
                                  },
                              },
                          'secure': 'F',
                          },
                      },
                  'vlan': '1000',
                  },
              '1005': {
                  'mac_addresses': {
                      '5e00.c0ff.0007': {
                          'entry': 'G',
                          'mac_address': '5e00.c0ff.0007',
                          'ntfy': 'F',
                          'interfaces': {
                              'Sup-eth1(R)': {
                                  'age': '-',
                                  'mac_type': 'static',
                                  'interface': 'Sup-eth1(R)',
                                  },
                              },
                          'secure': 'F',
                          },
                      },
                  'vlan': '1005',
                  },
              '1006': {
                  'mac_addresses': {
                      '5e00.c0ff.0007': {
                          'entry': 'G',
                          'mac_address': '5e00.c0ff.0007',
                          'ntfy': 'F',
                          'interfaces': {
                              'Sup-eth1(R)': {
                                  'age': '-',
                                  'mac_type': 'static',
                                  'interface': 'Sup-eth1(R)',
                                  },
                              },
                          'secure': 'F',
                          },
                      },
                  'vlan': '1006',
                  },
              '1007': {
                  'mac_addresses': {
                      '5e00.c0ff.0007': {
                          'entry': 'G',
                          'mac_address': '5e00.c0ff.0007',
                          'ntfy': 'F',
                          'interfaces': {
                              'Sup-eth1(R)': {
                                  'age': '-',
                                  'mac_type': 'static',
                                  'interface': 'Sup-eth1(R)',
                                  },
                              },
                          'secure': 'F',
                          },
                      },
                  'vlan': '1007',
                  },
              '1008': {
                  'mac_addresses': {
                      '5e00.c0ff.0007': {
                          'entry': 'G',
                          'mac_address': '5e00.c0ff.0007',
                          'ntfy': 'F',
                          'interfaces': {
                              'Sup-eth1(R)': {
                                  'age': '-',
                                  'mac_type': 'static',
                                  'interface': 'Sup-eth1(R)',
                                  },
                              },
                          'secure': 'F',
                          },
                      },
                  'vlan': '1008',
                  },
              '1009': {
                  'mac_addresses': {
                      '5e00.c0ff.0007': {
                          'entry': 'G',
                          'mac_address': '5e00.c0ff.0007',
                          'ntfy': 'F',
                          'interfaces': {
                              'Sup-eth1(R)': {
                                  'age': '-',
                                  'mac_type': 'static',
                                  'interface': 'Sup-eth1(R)',
                                  },
                              },
                          'secure': 'F',
                          },
                      },
                  'vlan': '1009',
                  },
              '101': {
                  'mac_addresses': {
                      '5e00.c0ff.0007': {
                          'entry': 'G',
                          'mac_address': '5e00.c0ff.0007',
                          'ntfy': 'F',
                          'interfaces': {
                              'Sup-eth1(R)': {
                                  'age': '-',
                                  'mac_type': 'static',
                                  'interface': 'Sup-eth1(R)',
                                  },
                              },
                          'secure': 'F',
                          },
                      },
                  'vlan': '101',
                  },
              '102': {
                  'mac_addresses': {
                      '5e00.c0ff.0007': {
                          'entry': 'G',
                          'mac_address': '5e00.c0ff.0007',
                          'ntfy': 'F',
                          'interfaces': {
                              'Sup-eth1(R)': {
                                  'age': '-',
                                  'mac_type': 'static',
                                  'interface': 'Sup-eth1(R)',
                                  },
                              },
                          'secure': 'F',
                          },
                      },
                  'vlan': '102',
                  },
              '103': {
                  'mac_addresses': {
                      '5e00.c0ff.0007': {
                          'entry': 'G',
                          'mac_address': '5e00.c0ff.0007',
                          'ntfy': 'F',
                          'interfaces': {
                              'Sup-eth1(R)': {
                                  'age': '-',
                                  'mac_type': 'static',
                                  'interface': 'Sup-eth1(R)',
                                  },
                              },
                          'secure': 'F',
                          },
                      },
                  'vlan': '103',
                  },
              '105': {
                  'mac_addresses': {
                      '5e00.c0ff.0007': {
                          'entry': 'G',
                          'mac_address': '5e00.c0ff.0007',
                          'ntfy': 'F',
                          'interfaces': {
                              'Sup-eth1(R)': {
                                  'age': '-',
                                  'mac_type': 'static',
                                  'interface': 'Sup-eth1(R)',
                                  },
                              },
                          'secure': 'F',
                          },
                      },
                  'vlan': '105',
                  },
              '106': {
                  'mac_addresses': {
                      '5e00.c0ff.0007': {
                          'entry': 'G',
                          'mac_address': '5e00.c0ff.0007',
                          'ntfy': 'F',
                          'interfaces': {
                              'Sup-eth1(R)': {
                                  'age': '-',
                                  'mac_type': 'static',
                                  'interface': 'Sup-eth1(R)',
                                  },
                              },
                          'secure': 'F',
                          },
                      },
                  'vlan': '106',
                  },
              '107': {
                  'mac_addresses': {
                      '5e00.c0ff.0007': {
                          'entry': 'G',
                          'mac_address': '5e00.c0ff.0007',
                          'ntfy': 'F',
                          'interfaces': {
                              'Sup-eth1(R)': {
                                  'age': '-',
                                  'mac_type': 'static',
                                  'interface': 'Sup-eth1(R)',
                                  },
                              },
                          'secure': 'F',
                          },
                      },
                  'vlan': '107',
                  },
              '108': {
                  'mac_addresses': {
                      '5e00.c0ff.0007': {
                          'entry': 'G',
                          'mac_address': '5e00.c0ff.0007',
                          'ntfy': 'F',
                          'interfaces': {
                              'Sup-eth1(R)': {
                                  'age': '-',
                                  'mac_type': 'static',
                                  'interface': 'Sup-eth1(R)',
                                  },
                              },
                          'secure': 'F',
                          },
                      },
                  'vlan': '108',
                  },
              '109': {
                  'mac_addresses': {
                      '5e00.c0ff.0007': {
                          'entry': 'G',
                          'mac_address': '5e00.c0ff.0007',
                          'ntfy': 'F',
                          'interfaces': {
                              'Sup-eth1(R)': {
                                  'age': '-',
                                  'mac_type': 'static',
                                  'interface': 'Sup-eth1(R)',
                                  },
                              },
                          'secure': 'F',
                          },
                      },
                  'vlan': '109',
                  },
              '110': {
                  'mac_addresses': {
                      '5e00.c0ff.0007': {
                          'entry': 'G',
                          'mac_address': '5e00.c0ff.0007',
                          'ntfy': 'F',
                          'interfaces': {
                              'Sup-eth1(R)': {
                                  'age': '-',
                                  'mac_type': 'static',
                                  'interface': 'Sup-eth1(R)',
                                  },
                              },
                          'secure': 'F',
                          },
                      },
                  'vlan': '110',
                  },
              '111': {
                  'mac_addresses': {
                      '5e00.c0ff.0007': {
                          'entry': 'G',
                          'mac_address': '5e00.c0ff.0007',
                          'ntfy': 'F',
                          'interfaces': {
                              'Sup-eth1(R)': {
                                  'age': '-',
                                  'mac_type': 'static',
                                  'interface': 'Sup-eth1(R)',
                                  },
                              },
                          'secure': 'F',
                          },
                      },
                  'vlan': '111',
                  },
              '112': {
                  'mac_addresses': {
                      '5e00.c0ff.0007': {
                          'entry': 'G',
                          'mac_address': '5e00.c0ff.0007',
                          'ntfy': 'F',
                          'interfaces': {
                              'Sup-eth1(R)': {
                                  'age': '-',
                                  'mac_type': 'static',
                                  'interface': 'Sup-eth1(R)',
                                  },
                              },
                          'secure': 'F',
                          },
                      },
                  'vlan': '112',
                  },
              '113': {
                  'mac_addresses': {
                      '5e00.c0ff.0007': {
                          'entry': 'G',
                          'mac_address': '5e00.c0ff.0007',
                          'ntfy': 'F',
                          'interfaces': {
                              'Sup-eth1(R)': {
                                  'age': '-',
                                  'mac_type': 'static',
                                  'interface': 'Sup-eth1(R)',
                                  },
                              },
                          'secure': 'F',
                          },
                      },
                  'vlan': '113',
                  },
              '114': {
                  'mac_addresses': {
                      '5e00.c0ff.0007': {
                          'entry': 'G',
                          'mac_address': '5e00.c0ff.0007',
                          'ntfy': 'F',
                          'interfaces': {
                              'Sup-eth1(R)': {
                                  'age': '-',
                                  'mac_type': 'static',
                                  'interface': 'Sup-eth1(R)',
                                  },
                              },
                          'secure': 'F',
                          },
                      },
                  'vlan': '114',
                  },
              },
          },
      }

    golden_output = {'execute.return_value': '''\
    N95_1# show system internal l2fwder mac
    Legend: 
        * - primary entry, G - Gateway MAC, (R) - Routed MAC, O - Overlay MAC
        age - seconds since last seen,+ - primary entry using vPC Peer-Link,
        (T) - True, (F) - False, C - ControlPlane MAC
       VLAN     MAC Address      Type      age     Secure NTFY Ports
    ---------+-----------------+--------+---------+------+----+---------------
    G   114    5e00.c0ff.0007    static   -          F     F   sup-eth1(R)
    G   112    5e00.c0ff.0007    static   -          F     F   sup-eth1(R)
    G   113    5e00.c0ff.0007    static   -          F     F   sup-eth1(R)
    G   110    5e00.c0ff.0007    static   -          F     F   sup-eth1(R)
    G   111    5e00.c0ff.0007    static   -          F     F   sup-eth1(R)
    G   108    5e00.c0ff.0007    static   -          F     F   sup-eth1(R)
    G   109    5e00.c0ff.0007    static   -          F     F   sup-eth1(R)
    G   106    5e00.c0ff.0007    static   -          F     F   sup-eth1(R)
    G   107    5e00.c0ff.0007    static   -          F     F   sup-eth1(R)
    G   105    5e00.c0ff.0007    static   -          F     F   sup-eth1(R)
    G   102    5e00.c0ff.0007    static   -          F     F   sup-eth1(R)
    G   103    5e00.c0ff.0007    static   -          F     F   sup-eth1(R)
    G   100    5e00.c0ff.0007    static   -          F     F   sup-eth1(R)
    G   101    5e00.c0ff.0007    static   -          F     F   sup-eth1(R)
    G     -    5e00:c000:0007    static   -          F     F   sup-eth1(R)
    *     1    fa16.3eff.5e69   dynamic   00:01:02   F     F     Eth1/4  
    *   100    fa16.3eff.5e69   dynamic   00:05:38   F     F     Eth1/4  
    G  1008    5e00.c0ff.0007    static   -          F     F   sup-eth1(R)
    G  1009    5e00.c0ff.0007    static   -          F     F   sup-eth1(R)
    G  1006    5e00.c0ff.0007    static   -          F     F   sup-eth1(R)
    G  1007    5e00.c0ff.0007    static   -          F     F   sup-eth1(R)
    G  1005    5e00.c0ff.0007    static   -          F     F   sup-eth1(R)
    G  1000    5e00.c0ff.0007    static   -          F     F   sup-eth1(R)
    *    10    aaaa.bbff.8888    static   -          F     F     Eth1/2  
        1           1         -00:00:de:ff:6c:9d         -             1
    '''
                     }

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowSystemInternalL2fwderMac(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowSystemInternalL2fwderMac(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


if __name__ == '__main__':
    unittest.main()
