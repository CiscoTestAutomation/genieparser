#!/bin/env python
import unittest
from unittest.mock import Mock
from pyats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                       SchemaMissingKeyError
from genie.libs.parser.iosxe.show_power import ShowStackPower, ShowPowerInline


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

    golden_output_1 = {'execute.return_value': '''\
        Module   Available     Used     Remaining
                  (Watts)     (Watts)    (Watts) 
        ------   ---------   --------   ---------
        1          1550.0      147.0      1403.0
        Interface Admin  Oper       Power   Device              Class Max
                                    (Watts)                            
        --------- ------ ---------- ------- ------------------- ----- ----
        Gi1/0/1   auto   off        0.0     n/a                 n/a   30.0 
        Gi1/0/2   auto   off        0.0     n/a                 n/a   30.0 
        Gi1/0/3   auto   off        0.0     n/a                 n/a   30.0 
        
        Module   Available     Used     Remaining
                  (Watts)     (Watts)    (Watts) 
        ------   ---------   --------   ---------
        2          1550.0      424.7      1125.3
        Interface Admin  Oper       Power   Device              Class Max
                                    (Watts)                            
        --------- ------ ---------- ------- ------------------- ----- ----
        Gi2/0/1   auto   on         7.1     IP Phone 8845       2     30.0 
        Gi2/0/2   auto   off        0.0     n/a                 n/a   30.0 
        Gi2/0/3   auto   on         26.1    AIR-AP2802I-E-K9    4     30.0 
        
        Module   Available     Used     Remaining
                  (Watts)     (Watts)    (Watts) 
        ------   ---------   --------   ---------
        3          1550.0      397.4      1152.6
        Interface Admin  Oper       Power   Device              Class Max
                                    (Watts)                            
        --------- ------ ---------- ------- ------------------- ----- ----
        Gi3/0/1   auto   on         26.1    AIR-AP2802I-E-K9    4     30.0 
        Gi3/0/2   auto   on         26.1    AIR-AP2802I-E-K9    4     30.0 
        
        Module   Available     Used     Remaining
        Interface Admin  Oper       Power   Device              Class Max
                                    (Watts)                            
        --------- ------ ---------- ------- ------------------- ----- ----
                  (Watts)     (Watts)    (Watts) 
        ------   ---------   --------   ---------
        4          1550.0      267.0      1283.0
        Interface Admin  Oper       Power   Device              Class Max
                                    (Watts)                            
        --------- ------ ---------- ------- ------------------- ----- ----
        Gi4/0/1   auto   off        0.0     n/a                 n/a   30.0 
        Gi4/0/2   auto   off        0.0     n/a                 n/a   30.0 
        Gi4/0/3   auto   off        0.0     n/a                 n/a   30.0 
        Gi4/0/4   auto   on         14.8    IP Phone 8865       4     30.0 
        
        Module   Available     Used     Remaining
                  (Watts)     (Watts)    (Watts) 
        ------   ---------   --------   ---------
        5          1550.0       80.6      1469.4
        Interface Admin  Oper       Power   Device              Class Max
                                    (Watts)                            
        --------- ------ ---------- ------- ------------------- ----- ----
        Gi5/0/1   auto   off        0.0     n/a                 n/a   30.0 
        Gi5/0/2   auto   off        0.0     n/a                 n/a   30.0 
        Gi5/0/3   auto   off        0.0     n/a                 n/a   30.0 
        Gi5/0/4   auto   off        0.0     n/a                 n/a   30.0 
        Gi5/0/5   auto   off        0.0     n/a                 n/a   30.0 
        Gi5/0/6   auto   off        0.0     n/a                 n/a   30.0 
        Interface Admin  Oper       Power   Device              Class Max
                                    (Watts)                            
        --------- ------ ---------- ------- ------------------- ----- ----
        Gi5/0/7   auto   off        0.0     n/a                 n/a   30.0 
        Gi5/0/8   auto   off        0.0     n/a                 n/a   30.0 
        Gi5/0/9   auto   off        0.0     n/a                 n/a   30.0 
        Gi5/0/10  auto   off        0.0     n/a                 n/a   30.0 
        Gi5/0/11  auto   off        0.0     n/a                 n/a   30.0 
        Gi5/0/12  auto   off        0.0     n/a                 n/a   30.0 
        Gi5/0/13  auto   on         15.2    IP Phone 8865       4     30.0 
       '''}

    golden_parsed_output_1 = {
        'watts': {
            '1': {
              'module': '1',
              'available': 1550.0,
              'used': 147.0,
              'remaining': 1403.0
            },
            '2': {
              'module': '2',
              'available': 1550.0,
              'used': 424.7,
              'remaining': 1125.3
            },
            '3': {
              'module': '3',
              'available': 1550.0,
              'used': 397.4,
              'remaining': 1152.6
            },
            '4': {
              'module': '4',
              'available': 1550.0,
              'used': 267.0,
              'remaining': 1283.0
            },
            '5': {
              'module': '5',
              'available': 1550.0,
              'used': 80.6,
              'remaining': 1469.4
            }
        },
        'interface': {
            'GigabitEthernet1/0/1': {
              'power': 0.0,
              'max': 30.0,
              'admin_state': 'auto',
              'oper_state': 'off'
            },
            'GigabitEthernet1/0/2': {
              'power': 0.0,
              'max': 30.0,
              'admin_state': 'auto',
              'oper_state': 'off'
            },
            'GigabitEthernet1/0/3': {
              'power': 0.0,
              'max': 30.0,
              'admin_state': 'auto',
              'oper_state': 'off'
            },
            'GigabitEthernet2/0/1': {
              'power': 7.1,
              'max': 30.0,
              'admin_state': 'auto',
              'oper_state': 'on',
              'device': 'IP Phone 8845',
              'class': '2'
            },
            'GigabitEthernet2/0/2': {
              'power': 0.0,
              'max': 30.0,
              'admin_state': 'auto',
              'oper_state': 'off'
            },
            'GigabitEthernet2/0/3': {
              'power': 26.1,
              'max': 30.0,
              'admin_state': 'auto',
              'oper_state': 'on',
              'device': 'AIR-AP2802I-E-K9',
              'class': '4'
            },
            'GigabitEthernet3/0/1': {
              'power': 26.1,
              'max': 30.0,
              'admin_state': 'auto',
              'oper_state': 'on',
              'device': 'AIR-AP2802I-E-K9',
              'class': '4'
            },
            'GigabitEthernet3/0/2': {
              'power': 26.1,
              'max': 30.0,
              'admin_state': 'auto',
              'oper_state': 'on',
              'device': 'AIR-AP2802I-E-K9',
              'class': '4'
            },
            'GigabitEthernet4/0/1': {
              'power': 0.0,
              'max': 30.0,
              'admin_state': 'auto',
              'oper_state': 'off'
            },
            'GigabitEthernet4/0/2': {
              'power': 0.0,
              'max': 30.0,
              'admin_state': 'auto',
              'oper_state': 'off'
            },
            'GigabitEthernet4/0/3': {
              'power': 0.0,
              'max': 30.0,
              'admin_state': 'auto',
              'oper_state': 'off'
            },
            'GigabitEthernet4/0/4': {
              'power': 14.8,
              'max': 30.0,
              'admin_state': 'auto',
              'oper_state': 'on',
              'device': 'IP Phone 8865',
              'class': '4'
            },
            'GigabitEthernet5/0/1': {
              'power': 0.0,
              'max': 30.0,
              'admin_state': 'auto',
              'oper_state': 'off'
            },
            'GigabitEthernet5/0/2': {
              'power': 0.0,
              'max': 30.0,
              'admin_state': 'auto',
              'oper_state': 'off'
            },
            'GigabitEthernet5/0/3': {
              'power': 0.0,
              'max': 30.0,
              'admin_state': 'auto',
              'oper_state': 'off'
            },
            'GigabitEthernet5/0/4': {
              'power': 0.0,
              'max': 30.0,
              'admin_state': 'auto',
              'oper_state': 'off'
            },
            'GigabitEthernet5/0/5': {
              'power': 0.0,
              'max': 30.0,
              'admin_state': 'auto',
              'oper_state': 'off'
            },
            'GigabitEthernet5/0/6': {
              'power': 0.0,
              'max': 30.0,
              'admin_state': 'auto',
              'oper_state': 'off'
            },
            'GigabitEthernet5/0/7': {
              'power': 0.0,
              'max': 30.0,
              'admin_state': 'auto',
              'oper_state': 'off'
            },
            'GigabitEthernet5/0/8': {
              'power': 0.0,
              'max': 30.0,
              'admin_state': 'auto',
              'oper_state': 'off'
            },
            'GigabitEthernet5/0/9': {
              'power': 0.0,
              'max': 30.0,
              'admin_state': 'auto',
              'oper_state': 'off'
            },
            'GigabitEthernet5/0/10': {
              'power': 0.0,
              'max': 30.0,
              'admin_state': 'auto',
              'oper_state': 'off'
            },
            'GigabitEthernet5/0/11': {
              'power': 0.0,
              'max': 30.0,
              'admin_state': 'auto',
              'oper_state': 'off'
            },
            'GigabitEthernet5/0/12': {
              'power': 0.0,
              'max': 30.0,
              'admin_state': 'auto',
              'oper_state': 'off'
            },
            'GigabitEthernet5/0/13': {
              'power': 15.2,
              'max': 30.0,
              'admin_state': 'auto',
              'oper_state': 'on',
              'device': 'IP Phone 8865',
              'class': '4'
            }
        }
    }

    golden_output_2 = {'execute.return_value': '''\
        Available:1170.0(w)  Used:212.2(w)  Remaining:957.8(w)
        
        Interface Admin  Oper       Power   Device              Class Max
                                    (Watts)                            
        --------- ------ ---------- ------- ------------------- ----- ----
        Gi0/1     auto   off        0.0     n/a                 n/a   30.0 
        Gi0/2     auto   on         6.4     IP Phone 8945       2     30.0 
        Gi0/3     auto   on         6.4     IP Phone 8845       2     30.0 
        Gi0/4     auto   off        0.0     n/a                 n/a   30.0 
    '''}

    golden_parsed_output_2 = {
        'watts': {
            '0': {
              'module': '0',
              'available': 1170.0,
              'used': 212.2,
              'remaining': 957.8
            }
        },
        'interface': {
            'GigabitEthernet0/1': {
              'power': 0.0,
              'max': 30.0,
              'admin_state': 'auto',
              'oper_state': 'off'
            },
            'GigabitEthernet0/2': {
              'power': 6.4,
              'max': 30.0,
              'admin_state': 'auto',
              'oper_state': 'on',
              'device': 'IP Phone 8945',
              'class': '2'
            },
            'GigabitEthernet0/3': {
              'power': 6.4,
              'max': 30.0,
              'admin_state': 'auto',
              'oper_state': 'on',
              'device': 'IP Phone 8845',
              'class': '2'
            },
            'GigabitEthernet0/4': {
              'power': 0.0,
              'max': 30.0,
              'admin_state': 'auto',
              'oper_state': 'off'
            }
        }
    }

    golden_output_3 = {'execute.return_value': '''\
        Available:0.0(w)  Used:0.0(w)  Remaining:0.0(w)

        Interface Admin  Oper       Power   Device              Class Max
                                    (Watts)                            
        --------- ------ ---------- ------- ------------------- ----- ----
    '''}

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        platform_obj = ShowPowerInline(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = platform_obj.parse(interface='Gi1/0/13')    

    def test_golden(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_c3850)
        platform_obj = ShowPowerInline(device=self.dev_c3850)
        parsed_output = platform_obj.parse(interface='Gi1/0/13')
        self.assertEqual(parsed_output,self.golden_parsed_output_c3850)

    def test_golden_1(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_1)
        platform_obj = ShowPowerInline(device=self.dev_c3850)
        parsed_output = platform_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

    def test_golden_2(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_2)
        platform_obj = ShowPowerInline(device=self.dev_c3850)
        parsed_output = platform_obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

    def test_golden_3(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_3)
        platform_obj = ShowPowerInline(device=self.dev_c3850)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = platform_obj.parse()


if __name__ == '__main__':
    unittest.main()

