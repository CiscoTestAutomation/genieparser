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
                                          "interface": "GigabitEthernet1/0/8",
                                          "entry_type": "static"
                                      },
                                      "GigabitEthernet1/0/9": {
                                          "interface": "GigabitEthernet1/0/9",
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
          10    aaaa.bbbb.cccc    STATIC      Gi1/0/8 Gi1/0/9 
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

