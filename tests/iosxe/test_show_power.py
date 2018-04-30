#!/bin/env python
import unittest
from unittest.mock import Mock
from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                       SchemaMissingKeyError
from genie.libs.parser.iosxe.show_power import ShowStackPower, ShowPowerInlineInterface


class test_show_stack_power(unittest.TestCase):
    dev1 = Device(name='empty')
    dev_c3850 = Device(name='c3850')
    empty_output = {'execute.return_value': '      '}

    golden_parsed_output_c3850 = {
        "power_stack": {
            "Powerstack-1": {
                "switch_num": 1,
                "allocated_power": 200,
                "topology": "Stndaln",
                "unused_power": 485,
                "power_supply_num": 1,
                "total_power": 715,
                "mode": "SP-PS",
                "reserved_power": 30
            },
            "Powerstack-12": {
                "switch_num": 1,
                "allocated_power": 200,
                "topology": "Stndaln",
                "unused_power": 485,
                "power_supply_num": 1,
                "total_power": 715,
                "mode": "SP-PS",
                "reserved_power": 30
            },
            "Powerstack-11": {
                "switch_num": 1,
                "allocated_power": 295,
                "topology": "Stndaln",
                "unused_power": 390,
                "power_supply_num": 1,
                "total_power": 715,
                "mode": "SP-PS",
                "reserved_power": 30
            }
        }
    }

    golden_output_c3850 = {'execute.return_value': '''\
        Power Stack           Stack   Stack    Total   Rsvd    Alloc   Unused  Num  Num
        Name                  Mode    Topolgy  Pwr(W)  Pwr(W)  Pwr(W)  Pwr(W)  SW   PS
        --------------------  ------  -------  ------  ------  ------  ------  ---  ---
        Powerstack-1          SP-PS   Stndaln  715     30      200     485     1    1   
        Powerstack-11         SP-PS   Stndaln  715     30      295     390     1    1   
        Powerstack-12         SP-PS   Stndaln  715     30      200     485     1    1 
    '''
    }

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        platform_obj = ShowStackPower(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = platform_obj.parse()    

    def test_golden(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_c3850)
        platform_obj = ShowStackPower(device=self.dev_c3850)
        parsed_output = platform_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_c3850)


class test_show_power_inline_interface(unittest.TestCase):
    dev1 = Device(name='empty')
    dev_c3850 = Device(name='c3850')
    empty_output = {'execute.return_value': '      '}

    golden_parsed_output_c3850 = {
        "interface": {
            "GigabitEthernet1/0/13": {
               "admin_state": "auto",
               "power": 15.4,
               "class": "3",
               "oper_state": "on",
               "device": "AIR-CAP2602I-A-K9",
               "max": 30.0
            }
        }
    }

    golden_output_c3850 = {'execute.return_value': '''\
        Interface Admin  Oper       Power   Device              Class Max
                                    (Watts)                            
        --------- ------ ---------- ------- ------------------- ----- ----
        Gi1/0/13  auto   on         15.4    AIR-CAP2602I-A-K9   3     30.0
    '''
    }

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        platform_obj = ShowPowerInlineInterface(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = platform_obj.parse(interface='Gi1/0/13')    

    def test_golden(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_c3850)
        platform_obj = ShowPowerInlineInterface(device=self.dev_c3850)
        parsed_output = platform_obj.parse(interface='Gi1/0/13')
        self.assertEqual(parsed_output,self.golden_parsed_output_c3850)

if __name__ == '__main__':
    unittest.main()

