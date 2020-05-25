#!/bin/env python
import unittest
from unittest.mock import Mock
from pyats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                       SchemaMissingKeyError
from genie.libs.parser.iosxe.show_fdb import ShowMacAddressTable, \
                                  ShowMacAddressTableAgingTime, \
                                  ShowMacAddressTableLearning


class TestShowMacAddressTable(unittest.TestCase):

    maxDiff = None
    dev1 = Device(name='empty')
    dev_c3850 = Device(name='c3850')
    empty_output = {'execute.return_value': '      '}

    golden_parsed_output = {
        "mac_table": {
            "vlans": {
                  '100': {
                      "mac_addresses": {
                            "ecbd.1dff.5f92": {
                                "drop": {
                                      "drop": True,
                                      "entry_type": "dynamic"
                                },
                                "mac_address": "ecbd.1dff.5f92"
                            },
                            "3820.56ff.6f75": {
                                "interfaces": {
                                      "Port-channel12": {
                                          "interface": "Port-channel12",
                                          "entry_type": "dynamic"
                                      }
                                },
                                "mac_address": "3820.56ff.6f75"
                            },
                            "58bf.eaff.e508": {
                                "interfaces": {
                                      "Vlan100": {
                                          "interface": "Vlan100",
                                          "entry_type": "static"
                                      }
                                },
                                "mac_address": "58bf.eaff.e508"
                            }
                      },
                      "vlan": 100
                  },
                  "all": {
                      "mac_addresses": {
                            "0100.0cff.9999": {
                                "interfaces": {
                                      "CPU": {
                                          "interface": "CPU",
                                          "entry_type": "static"
                                      }
                                },
                                "mac_address": "0100.0cff.9999"
                            },
                            "0100.0cff.999a": {
                                "interfaces": {
                                      "CPU": {
                                          "interface": "CPU",
                                          "entry_type": "static"
                                      }
                                },
                                "mac_address": "0100.0cff.999a"
                            }
                      },
                      "vlan": "all"
                  },
                  '20': {
                      "mac_addresses": {
                            "aaaa.bbff.8888": {
                                "drop": {
                                      "drop": True,
                                      "entry_type": "static"
                                },
                                "mac_address": "aaaa.bbff.8888"
                            }
                      },
                      "vlan": 20
                  },
                  '10': {
                      "mac_addresses": {
                            "aaaa.bbff.8888": {
                                "interfaces": {
                                      "GigabitEthernet1/0/8": {
                                          "entry": "*",
                                          "interface": "GigabitEthernet1/0/8",
                                          "entry_type": "static"
                                      },
                                      "GigabitEthernet1/0/9": {
                                          "entry": "*",
                                          "interface": "GigabitEthernet1/0/9",
                                          "entry_type": "static"
                                      },
                                       'Vlan101': {
                                          "entry": "*",
                                          "interface": "Vlan101",
                                          "entry_type": "static"
                                      }
                                    
                                },
                                "mac_address": "aaaa.bbff.8888"
                            }
                      },
                      "vlan": 10
                  },
                  '101': {
                      "mac_addresses": {
                            "58bf.eaff.e5f7": {
                                "interfaces": {
                                      "Vlan101": {
                                          "interface": "Vlan101",
                                          "entry_type": "static"
                                      }
                                },
                                "mac_address": "58bf.eaff.e5f7"
                            },
                            "3820.56ff.6fb3": {
                                "interfaces": {
                                      "Port-channel12": {
                                          "interface": "Port-channel12",
                                          "entry_type": "dynamic"
                                      }
                                },
                                "mac_address": "3820.56ff.6fb3"
                            },
                            "3820.56ff.6f75": {
                                "interfaces": {
                                      "Port-channel12": {
                                          "interface": "Port-channel12",
                                          "entry_type": "dynamic"
                                      }
                                },
                                "mac_address": "3820.56ff.6f75"
                            }
                      },
                      "vlan": 101
                  }
            }
        },
        "total_mac_addresses": 10
    }

    golden_output = {'execute.return_value': '''\
                 Mac Address Table
        -------------------------------------------

        Vlan    Mac Address       Type        Ports
        ----    -----------       --------    -----
         All    0100.0cff.9999    STATIC      CPU
         All    0100.0cff.999a    STATIC      CPU
          20    aaaa.bbff.8888    STATIC      Drop
         100    3820.56ff.6f75    DYNAMIC     Po12
         100    58bf.eaff.e508    STATIC      Vl100
         100    ecbd.1dff.5f92    DYNAMIC     Drop
         101    3820.56ff.6f75    DYNAMIC     Po12
         101    3820.56ff.6fb3    DYNAMIC     Po12
         101    58bf.eaff.e5f7    STATIC      Vl101
         * 10    aaaa.bbff.8888    STATIC      Gi1/0/8 Gi1/0/9
                                              Vl101
        Total Mac Addresses for this criterion: 10
    '''}

    golden_parsed_output1 = {
        'mac_table': {
            'vlans': {
                '101': {
                    'mac_addresses': {
                        '701f.53ff.4de2': {
                            'interfaces': {
                                'GigabitEthernet2/0/30': {
                                    'entry_type': 'static',
                                    'interface': 'GigabitEthernet2/0/30',
                                },
                            },
                            'mac_address': '701f.53ff.4de2',
                        },
                        'cc5a.53ff.acc7': {
                            'interfaces': {
                                'Vlan101': {
                                    'entry_type': 'static',
                                    'interface': 'Vlan101',
                                },
                            },
                            'mac_address': 'cc5a.53ff.acc7',
                        },
                        'cc98.91ff.cbc2': {
                            'interfaces': {
                                'GigabitEthernet1/0/32': {
                                    'entry_type': 'dynamic',
                                    'interface': 'GigabitEthernet1/0/32',
                                },
                            },
                            'mac_address': 'cc98.91ff.cbc2',
                        },
                        'cc98.91ff.e84f': {
                            'interfaces': {
                                'GigabitEthernet1/0/31': {
                                    'entry_type': 'dynamic',
                                    'interface': 'GigabitEthernet1/0/31',
                                },
                            },
                            'mac_address': 'cc98.91ff.e84f',
                        },
                        'cc98.91ff.e97e': {
                            'interfaces': {
                                'GigabitEthernet1/0/28': {
                                    'entry_type': 'dynamic',
                                    'interface': 'GigabitEthernet1/0/28',
                                },
                            },
                            'mac_address': 'cc98.91ff.e97e',
                        },
                        'cc98.91ff.09b8': {
                            'interfaces': {
                                'GigabitEthernet1/0/34': {
                                    'entry_type': 'dynamic',
                                    'interface': 'GigabitEthernet1/0/34',
                                },
                            },
                            'mac_address': 'cc98.91ff.09b8',
                        },
                        'cc98.91ff.0cc4': {
                            'interfaces': {
                                'GigabitEthernet1/0/33': {
                                    'entry_type': 'dynamic',
                                    'interface': 'GigabitEthernet1/0/33',
                                },
                            },
                            'mac_address': 'cc98.91ff.0cc4',
                        },
                        'cc98.91ff.0d94': {
                            'interfaces': {
                                'GigabitEthernet1/0/29': {
                                    'entry_type': 'dynamic',
                                    'interface': 'GigabitEthernet1/0/29',
                                },
                            },
                            'mac_address': 'cc98.91ff.0d94',
                        },
                    },
                    'vlan': 101,
                },
            },
        },
        'total_mac_addresses': 8,
    }

    golden_output1 = {'execute.return_value': '''\
        show mac address-table vlan 101

                    Mac Address Table
        -------------------------------------------

        Vlan    Mac Address       Type        Ports
        ----    -----------       --------    -----
        101    701f.53ff.4de2    STATIC      Gi2/0/30 
        101    cc5a.53ff.acc7    STATIC      Vl101 
        101    cc98.91ff.cbc2    DYNAMIC     Gi1/0/32
        101    cc98.91ff.e84f    DYNAMIC     Gi1/0/31
        101    cc98.91ff.e97e    DYNAMIC     Gi1/0/28
        101    cc98.91ff.09b8    DYNAMIC     Gi1/0/34
        101    cc98.91ff.0cc4    DYNAMIC     Gi1/0/33
        101    cc98.91ff.0d94    DYNAMIC     Gi1/0/29
        Total Mac Addresses for this criterion: 8
    '''}

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowMacAddressTable(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.dev_c3850 = Mock(**self.golden_output)
        obj = ShowMacAddressTable(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden1(self):
        self.dev_c3850 = Mock(**self.golden_output1)
        obj = ShowMacAddressTable(device=self.dev_c3850)
        parsed_output = obj.parse(vlan='101')
        self.assertEqual(parsed_output, self.golden_parsed_output1)


class TestShowMacAddressTable2(unittest.TestCase):
    dev1 = Device(name='empty')
    dev_c3850 = Device(name='c3850')
    empty_output = {'execute.return_value': '      '}

    golden_parsed_output = {
        "mac_table": {
            "vlans": {
                  '100': {
                      "mac_addresses": {
                            "11aa.22ff.ee88": {
                                "interfaces": {
                                      "Router": {
                                          "entry": "*",
                                          "interface": "Router",
                                          "entry_type": "static",
                                          "learn": "No"
                                      }
                                },
                                "mac_address": "11aa.22ff.ee88"
                            }
                      },
                      "vlan": 100
                  },
                  '101': {
                      "mac_addresses": {
                            "44dd.eeff.55bb": {
                                "interfaces": {
                                      "GigabitEthernet1/40": {
                                          "entry": "*",
                                          "interface": "GigabitEthernet1/40",
                                          "entry_type": "dynamic",
                                          "learn": "Yes",
                                          "age": 10
                                      }
                                },
                                "mac_address": "44dd.eeff.55bb"
                            }
                      },
                      "vlan": 101
                  },
                  '102': {
                      "mac_addresses": {
                            "aa11.bbff.ee55": {
                                "interfaces": {
                                      "GigabitEthernet1/2": {
                                          "entry": "*",
                                          "interface": "GigabitEthernet1/2",
                                          "entry_type": "static",
                                          "learn": "Yes"
                                      },
                                      "GigabitEthernet1/4": {
                                          "entry": "*",
                                          "interface": "GigabitEthernet1/4",
                                          "entry_type": "static",
                                          "learn": "Yes"
                                      },
                                      "GigabitEthernet1/5": {
                                          "entry": "*",
                                          "interface": "GigabitEthernet1/5",
                                          "entry_type": "static",
                                          "learn": "Yes"
                                      },
                                      "GigabitEthernet1/6": {
                                          "entry": "*",
                                          "interface": "GigabitEthernet1/6",
                                          "entry_type": "static",
                                          "learn": "Yes"
                                      },
                                      "GigabitEthernet1/9": {
                                          "entry": "*",
                                          "interface": "GigabitEthernet1/9",
                                          "entry_type": "static",
                                          "learn": "Yes"
                                      },
                                      "GigabitEthernet1/10": {
                                          "entry": "*",
                                          "interface": "GigabitEthernet1/10",
                                          "entry_type": "static",
                                          "learn": "Yes"
                                      },
                                      "GigabitEthernet1/11": {
                                          "entry": "*",
                                          "interface": "GigabitEthernet1/11",
                                          "entry_type": "static",
                                          "learn": "Yes"
                                      },
                                      "GigabitEthernet1/12": {
                                          "entry": "*",
                                          "interface": "GigabitEthernet1/12",
                                          "entry_type": "static",
                                          "learn": "Yes"
                                      },
                                      "Router": {
                                          "entry": "*",
                                          "interface": "Router",
                                          "entry_type": "static",
                                          "learn": "Yes"
                                      },
                                      "Switch": {
                                          "entry": "*",
                                          "interface": "Switch",
                                          "entry_type": "static",
                                          "learn": "Yes"
                                      }
                                },
                                "mac_address": "aa11.bbff.ee55"
                            }
                      },
                      "vlan": 102
                  },
                  '200': {
                      "mac_addresses": {
                            "dd44.55ff.55ee": {
                                "interfaces": {
                                      "TenGigabitEthernet1/1": {
                                          "entry": "*",
                                          "interface": "TenGigabitEthernet1/1",
                                          "entry_type": "static",
                                          "learn": "Yes"
                                      },
                                      "TenGigabitEthernet1/2": {
                                          "entry": "*",
                                          "interface": "TenGigabitEthernet1/2",
                                          "entry_type": "static",
                                          "learn": "Yes"
                                      },
                                      "TenGigabitEthernet1/4": {
                                          "entry": "*",
                                          "interface": "TenGigabitEthernet1/4",
                                          "entry_type": "static",
                                          "learn": "Yes"
                                      },
                                      "TenGigabitEthernet1/8": {
                                          "entry": "*",
                                          "interface": "TenGigabitEthernet1/8",
                                          "entry_type": "static",
                                          "learn": "Yes"
                                      },
                                },
                                "mac_address": "dd44.55ff.55ee"
                            }
                      },
                      "vlan": 200
                  },
                  '300': {
                      "mac_addresses": {
                            "11aa.22ff.ee88": {
                                "interfaces": {
                                      "Router": {
                                          "interface": "Router",
                                          "entry_type": "static",
                                          "learn": "No"
                                      }
                                },
                                "mac_address": "11aa.22ff.ee88"
                            }
                      },
                      "vlan": 300
                  },
                  '301': {
                      "mac_addresses": {
                            "11aa.22ff.ee88": {
                                "drop": {
                                      "drop": True,
                                      "entry_type": "static"
                                },
                                "mac_address": "11aa.22ff.ee88"
                            }
                      },
                      "vlan": 301
                  },
                  '---': {
                      "mac_addresses": {
                            "0000.0000.0000": {
                                "interfaces": {
                                      "Router": {
                                          "entry": "*",
                                          "interface": "Router",
                                          "entry_type": "static",
                                          "learn": "No"
                                      }
                                },
                                "mac_address": "0000.0000.0000"
                            }
                      },
                      "vlan": "---"
                  },
                  '400': {
                      "mac_addresses": {
                            "0000.0000.0000": {
                                "interfaces": {
                                      "vPC Peer-Link": {
                                          "entry": "*",
                                          "interface": "vPC Peer-Link",
                                          "entry_type": "static",
                                          "learn": "No"
                                      },
                                      "Router": {
                                          "entry": "*",
                                          "interface": "Router",
                                          "entry_type": "static",
                                          "learn": "No"
                                      }
                                },
                                "mac_address": "0000.0000.0000"
                            }
                      },
                      "vlan": 400
                  }
            }
        },
        "total_mac_addresses": 8
    }

    golden_output = {'execute.return_value': '''\
      show mac address-table
      Legend: * - primary entry
              age - seconds since last seen
              n/a - not available

        vlan   mac address     type    learn     age              ports
      ------+----------------+--------+-----+----------+--------------------------
      *  100  11aa.22ff.ee88    static  No           -   Router
      *  101  44dd.eeff.55bb   dynamic  Yes         10   Gi1/40
      *  102  aa11.bbff.ee55    static  Yes          -   Gi1/2,Gi1/4,Gi1/5,Gi1/6
                                                         Gi1/9,Gi1/10,Gi1/11,Gi1/12
                                                         Router,Switch
      *  200  dd44.55ff.55ee    static  Yes          -   Te1/1,Te1/2,Te1/4,Te1/8
      300  11aa.22ff.ee88    static  No           -   Router
      301  11aa.22ff.ee88    static  No           -   Drop
      *  ---  0000.0000.0000    static  No           -   Router
      *  400  0000.0000.0000    static  No           -   vPC Peer-Link
                                                        Router
                                                       
              Total Mac Addresses for this criterion: 8
    '''
    }

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowMacAddressTable(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output)
        obj = ShowMacAddressTable(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


class TestShowMacAddressTableAgingTime(unittest.TestCase):
    dev1 = Device(name='empty')
    dev_c3850 = Device(name='c3850')
    empty_output = {'execute.return_value': '      '}

    golden_parsed_output = {
        'mac_aging_time': 0,
        'vlans': {
            '10': {
                'mac_aging_time': 10,
                'vlan': 10
            }
        }
    }

    golden_output = {'execute.return_value': '''\
        Global Aging Time:    0
        Vlan    Aging Time
        ----    ----------
          10      10
    '''
    }

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowMacAddressTableAgingTime(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output)
        obj = ShowMacAddressTableAgingTime(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


class TestShowMacAddressTableLearning(unittest.TestCase):
    dev1 = Device(name='empty')
    dev_c3850 = Device(name='c3850')
    empty_output = {'execute.return_value': '      '}

    golden_parsed_output = {
        "vlans": {
            '10': {
                 "vlan": 10,
                 "mac_learning": False
            },
            '105': {
                 "vlan": 105,
                 "mac_learning": False
            },
            '101': {
                 "vlan": 101,
                 "mac_learning": False
            },
            '102': {
                 "vlan": 102,
                 "mac_learning": False
            },
            '103': {
                 "vlan": 103,
                 "mac_learning": False
            }
        }
    }

    golden_output = {'execute.return_value': '''\
        Learning disabled on vlans: 10,101-103,105
    '''
    }

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowMacAddressTableLearning(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output)
        obj = ShowMacAddressTableLearning(device=self.dev_c3850)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


if __name__ == '__main__':
    unittest.main()
