#!/bin/env python
import unittest
from unittest.mock import Mock
from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                       SchemaMissingKeyError
from genie.libs.parser.iosxe.show_fdb import ShowMacAddressTable, \
                                  ShowMacAddressTableAgingTime, \
                                  ShowMacAddressTableLearning


class test_show_mac_address_table(unittest.TestCase):
    dev1 = Device(name='empty')
    dev_c3850 = Device(name='c3850')
    empty_output = {'execute.return_value': '      '}

    golden_parsed_output = {
        "mac_table": {
            "vlans": {
                  '100': {
                      "mac_addresses": {
                            "ecbd.1d09.5689": {
                                "drop": {
                                      "drop": True,
                                      "entry_type": "dynamic"
                                },
                                "mac_address": "ecbd.1d09.5689"
                            },
                            "3820.5672.fc03": {
                                "interfaces": {
                                      "Port-channel12": {
                                          "interface": "Port-channel12",
                                          "entry_type": "dynamic"
                                      }
                                },
                                "mac_address": "3820.5672.fc03"
                            },
                            "58bf.eab6.2f51": {
                                "interfaces": {
                                      "Vlan100": {
                                          "interface": "Vlan100",
                                          "entry_type": "static"
                                      }
                                },
                                "mac_address": "58bf.eab6.2f51"
                            }
                      },
                      "vlan": 100
                  },
                  "all": {
                      "mac_addresses": {
                            "0100.0ccc.cccc": {
                                "interfaces": {
                                      "CPU": {
                                          "interface": "CPU",
                                          "entry_type": "static"
                                      }
                                },
                                "mac_address": "0100.0ccc.cccc"
                            },
                            "0100.0ccc.cccd": {
                                "interfaces": {
                                      "CPU": {
                                          "interface": "CPU",
                                          "entry_type": "static"
                                      }
                                },
                                "mac_address": "0100.0ccc.cccd"
                            }
                      },
                      "vlan": "all"
                  },
                  '20': {
                      "mac_addresses": {
                            "aaaa.bbbb.cccc": {
                                "drop": {
                                      "drop": True,
                                      "entry_type": "static"
                                },
                                "mac_address": "aaaa.bbbb.cccc"
                            }
                      },
                      "vlan": 20
                  },
                  '10': {
                      "mac_addresses": {
                            "aaaa.bbbb.cccc": {
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
                                "mac_address": "aaaa.bbbb.cccc"
                            }
                      },
                      "vlan": 10
                  },
                  '101': {
                      "mac_addresses": {
                            "58bf.eab6.2f41": {
                                "interfaces": {
                                      "Vlan101": {
                                          "interface": "Vlan101",
                                          "entry_type": "static"
                                      }
                                },
                                "mac_address": "58bf.eab6.2f41"
                            },
                            "3820.5672.fc41": {
                                "interfaces": {
                                      "Port-channel12": {
                                          "interface": "Port-channel12",
                                          "entry_type": "dynamic"
                                      }
                                },
                                "mac_address": "3820.5672.fc41"
                            },
                            "3820.5672.fc03": {
                                "interfaces": {
                                      "Port-channel12": {
                                          "interface": "Port-channel12",
                                          "entry_type": "dynamic"
                                      }
                                },
                                "mac_address": "3820.5672.fc03"
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
         All    0100.0ccc.cccc    STATIC      CPU
         All    0100.0ccc.cccd    STATIC      CPU
          20    aaaa.bbbb.cccc    STATIC      Drop
         100    3820.5672.fc03    DYNAMIC     Po12
         100    58bf.eab6.2f51    STATIC      Vl100
         100    ecbd.1d09.5689    DYNAMIC     Drop
         101    3820.5672.fc03    DYNAMIC     Po12
         101    3820.5672.fc41    DYNAMIC     Po12
         101    58bf.eab6.2f41    STATIC      Vl101
         * 10    aaaa.bbbb.cccc    STATIC      Gi1/0/8 Gi1/0/9
                                              Vl101
        Total Mac Addresses for this criterion: 10
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


class test_show_mac_address_table_2(unittest.TestCase):
    dev1 = Device(name='empty')
    dev_c3850 = Device(name='c3850')
    empty_output = {'execute.return_value': '      '}

    golden_parsed_output = {
        "mac_table": {
            "vlans": {
                  '100': {
                      "mac_addresses": {
                            "11aa.22bb.33cc": {
                                "interfaces": {
                                      "Router": {
                                          "entry": "*",
                                          "interface": "Router",
                                          "entry_type": "static",
                                          "learn": "No"
                                      }
                                },
                                "mac_address": "11aa.22bb.33cc"
                            }
                      },
                      "vlan": 100
                  },
                  '101': {
                      "mac_addresses": {
                            "44dd.ee55.ff66": {
                                "interfaces": {
                                      "GigabitEthernet1/40": {
                                          "entry": "*",
                                          "interface": "GigabitEthernet1/40",
                                          "entry_type": "dynamic",
                                          "learn": "Yes",
                                          "age": 10
                                      }
                                },
                                "mac_address": "44dd.ee55.ff66"
                            }
                      },
                      "vlan": 101
                  },
                  '102': {
                      "mac_addresses": {
                            "aa11.bb22.cc33": {
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
                                "mac_address": "aa11.bb22.cc33"
                            }
                      },
                      "vlan": 102
                  },
                  '200': {
                      "mac_addresses": {
                            "dd44.55ee.66ff": {
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
                                "mac_address": "dd44.55ee.66ff"
                            }
                      },
                      "vlan": 200
                  },
                  '300': {
                      "mac_addresses": {
                            "11aa.22bb.33cc": {
                                "interfaces": {
                                      "Router": {
                                          "interface": "Router",
                                          "entry_type": "static",
                                          "learn": "No"
                                      }
                                },
                                "mac_address": "11aa.22bb.33cc"
                            }
                      },
                      "vlan": 300
                  },
                  '301': {
                      "mac_addresses": {
                            "11aa.22bb.33cc": {
                                "drop": {
                                      "drop": True,
                                      "entry_type": "static"
                                },
                                "mac_address": "11aa.22bb.33cc"
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
      *  100  11aa.22bb.33cc    static  No           -   Router
      *  101  44dd.ee55.ff66   dynamic  Yes         10   Gi1/40
      *  102  aa11.bb22.cc33    static  Yes          -   Gi1/2,Gi1/4,Gi1/5,Gi1/6
                                                         Gi1/9,Gi1/10,Gi1/11,Gi1/12
                                                         Router,Switch
      *  200  dd44.55ee.66ff    static  Yes          -   Te1/1,Te1/2,Te1/4,Te1/8
      300  11aa.22bb.33cc    static  No           -   Router
      301  11aa.22bb.33cc    static  No           -   Drop
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


class test_show_mac_address_table_aging_time(unittest.TestCase):
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


class test_show_mac_address_table_learning(unittest.TestCase):
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
