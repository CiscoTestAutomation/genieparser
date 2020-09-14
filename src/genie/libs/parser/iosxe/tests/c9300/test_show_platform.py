#!/bin/env python
import unittest

from unittest.mock import Mock
from pyats.topology import Device

from genie.metaparser.util.exceptions import (SchemaMissingKeyError,
                                              SchemaEmptyParserError)
from genie.libs.parser.iosxe.c9300.show_platform import (ShowInventory,
                                                         ShowEnvironmentAll)


class TestShowInventory(unittest.TestCase):
    maxDiff = None
    device_empty = Device(name='empty')
    device = Device(name='c9300')
    empty_output = {'execute.return_value': ''}

    # show inventory
    golden_output = {'execute.return_value': '''
        NAME: "c93xx Stack", DESCR: "c93xx Stack"
        PID: C9300-48UXM       , VID: V02  , SN: FCW2242G0V3
        
        NAME: "Switch 1", DESCR: "C9300-48UXM"
        PID: C9300-48UXM       , VID: V02  , SN: FCW2242G114
        
        NAME: "StackPort1/1", DESCR: "StackPort1/1"
        PID: STACK-T1-1M       , VID: V01  , SN: MOC2236A6JM
        
        NAME: "StackPort1/2", DESCR: "StackPort1/2"
        PID: STACK-T1-1M       , VID: V01  , SN: MOC2240A2JM
        
        NAME: "Switch 1 - Power Supply A", DESCR: "Switch 1 - Power Supply A"
        PID: PWR-C1-1100WAC    , VID: V02  , SN: DTN2236V68C
        
        NAME: "Switch 1 FRU Uplink Module 1", DESCR: "8x10G Uplink Module"
        PID: C9300-NM-8X       , VID: V02  , SN: FOC22423G0U
        
        NAME: "Te1/1/1", DESCR: "SFP-10GBase-SR"
        PID: SFP-10G-SR          , VID: V03  , SN: AVD223594E6
        
        NAME: "Switch 2", DESCR: "C9300-48UXM"
        PID: C9300-48UXM       , VID: V02  , SN: FCW2242G0V3
        
        NAME: "StackPort2/1", DESCR: "StackPort2/1"
        PID: STACK-T1-1M       , VID: V01  , SN: MOC2240A2JM
        
        NAME: "StackPort2/2", DESCR: "StackPort2/2"
        PID: STACK-T1-1M       , VID: V01  , SN: MOC2236A6JM
        
        NAME: "Switch 2 - Power Supply A", DESCR: "Switch 2 - Power Supply A"
        PID: PWR-C1-1100WAC    , VID: V02  , SN: DTN2236V6DL
        
        NAME: "Switch 2 FRU Uplink Module 1", DESCR: "8x10G Uplink Module"
        PID: C9300-NM-8X       , VID: V02  , SN: FOC22423FF4
    '''}

    golden_parsed_output = {
        'index': {
            1: {
                'vid': 'V02',
                'pid': 'C9300-48UXM',
                'name': 'c93xx Stack',
                'descr': 'c93xx Stack',
                'sn': 'FCW2242G0V3',
            },
            2: {
                'vid': 'V02',
                'pid': 'C9300-48UXM',
                'name': 'Switch 1',
                'descr': 'C9300-48UXM',
                'sn': 'FCW2242G114',
            },
            3: {
                'vid': 'V01',
                'pid': 'STACK-T1-1M',
                'name': 'StackPort1/1',
                'descr': 'StackPort1/1',
                'sn': 'MOC2236A6JM',
            },
            4: {
                'vid': 'V01',
                'pid': 'STACK-T1-1M',
                'name': 'StackPort1/2',
                'descr': 'StackPort1/2',
                'sn': 'MOC2240A2JM',
            },
            5: {
                'vid': 'V02',
                'pid': 'PWR-C1-1100WAC',
                'name': 'Switch 1 - Power Supply A',
                'descr': 'Switch 1 - Power Supply A',
                'sn': 'DTN2236V68C',
            },
            6: {
                'vid': 'V02',
                'pid': 'C9300-NM-8X',
                'name': 'Switch 1 FRU Uplink Module 1',
                'descr': '8x10G Uplink Module',
                'sn': 'FOC22423G0U',
            },
            7: {
                'vid': 'V03',
                'pid': 'SFP-10G-SR',
                'name': 'Te1/1/1',
                'descr': 'SFP-10GBase-SR',
                'sn': 'AVD223594E6',
            },
            8: {
                'vid': 'V02',
                'pid': 'C9300-48UXM',
                'name': 'Switch 2',
                'descr': 'C9300-48UXM',
                'sn': 'FCW2242G0V3',
            },
            9: {
                'vid': 'V01',
                'pid': 'STACK-T1-1M',
                'name': 'StackPort2/1',
                'descr': 'StackPort2/1',
                'sn': 'MOC2240A2JM',
            },
            10: {
                'vid': 'V01',
                'pid': 'STACK-T1-1M',
                'name': 'StackPort2/2',
                'descr': 'StackPort2/2',
                'sn': 'MOC2236A6JM',
            },
            11: {
                'vid': 'V02',
                'pid': 'PWR-C1-1100WAC',
                'name': 'Switch 2 - Power Supply A',
                'descr': 'Switch 2 - Power Supply A',
                'sn': 'DTN2236V6DL',
            },
            12: {
                'vid': 'V02',
                'pid': 'C9300-NM-8X',
                'name': 'Switch 2 FRU Uplink Module 1',
                'descr': '8x10G Uplink Module',
                'sn': 'FOC22423FF4',
            },
        },
    }

    golden_output1 = {'execute.return_value': '''
        NAME: "c93xx Stack", DESCR: "c93xx Stack"
        PID: C9300-24T         , VID: V03  , SN: FCW2347C0DB

        NAME: "Switch 1", DESCR: "C9300-24T"
        PID: C9300-24T         , VID: V03  , SN: FCW2347C0DB

        NAME: "StackPort1/1", DESCR: "StackPort1/1"
        PID: STACK-T1-50CM     , VID: V01  , SN: MOC2346A691

        NAME: "StackPort1/2", DESCR: "StackPort1/2"
        PID: STACK-T1-50CM     , VID: V01  , SN: MOC2346A69X

        NAME: "Switch 1 - Power Supply A", DESCR: "Switch 1 - Power Supply A"
        PID: PWR-C1-350WAC-P   , VID: V01  , SN: DCC2337B0K5

        NAME: "Switch 1 FRU Uplink Module 1", DESCR: "8x10G Uplink Module"
        PID: C9300-NM-8X       , VID: V02  , SN: FOC23473K4U

        NAME: "Switch 2", DESCR: "C9300-24T"
        PID: C9300-24T         , VID: V03  , SN: FOC2347X0GE

        NAME: "StackPort2/1", DESCR: "StackPort2/1"
        PID: STACK-T1-50CM     , VID: V01  , SN: MOC2346A69X

        NAME: "StackPort2/2", DESCR: "StackPort2/2"
        PID: STACK-T1-50CM     , VID: V01  , SN: MOC2346A691

        NAME: "Switch 2 - Power Supply A", DESCR: "Switch 2 - Power Supply A"
        PID: PWR-C1-350WAC-P   , VID: V01  , SN: DCC2337B0HT

        NAME: "Switch 2 FRU Uplink Module 1", DESCR: "8x10G Uplink Module"
        PID: C9300-NM-8X       , VID: V02  , SN: FOC23456CVT

        NAME: "Switch 3", DESCR: "C9300-24T - Provisioned"
        PID: C9300-24T         , VID:      , SN:
    '''}

    golden_parsed_output1 = {
        'index': {
            1: {
                'descr': 'c93xx Stack',
                'name': 'c93xx Stack',
                'pid': 'C9300-24T',
                'sn': 'FCW2347C0DB',
                'vid': 'V03',
            },
            2: {
                'descr': 'C9300-24T',
                'name': 'Switch 1',
                'pid': 'C9300-24T',
                'sn': 'FCW2347C0DB',
                'vid': 'V03',
            },
            3: {
                'descr': 'StackPort1/1',
                'name': 'StackPort1/1',
                'pid': 'STACK-T1-50CM',
                'sn': 'MOC2346A691',
                'vid': 'V01',
            },
            4: {
                'descr': 'StackPort1/2',
                'name': 'StackPort1/2',
                'pid': 'STACK-T1-50CM',
                'sn': 'MOC2346A69X',
                'vid': 'V01',
            },
            5: {
                'descr': 'Switch 1 - Power Supply A',
                'name': 'Switch 1 - Power Supply A',
                'pid': 'PWR-C1-350WAC-P',
                'sn': 'DCC2337B0K5',
                'vid': 'V01',
            },
            6: {
                'descr': '8x10G Uplink Module',
                'name': 'Switch 1 FRU Uplink Module 1',
                'pid': 'C9300-NM-8X',
                'sn': 'FOC23473K4U',
                'vid': 'V02',
            },
            7: {
                'descr': 'C9300-24T',
                'name': 'Switch 2',
                'pid': 'C9300-24T',
                'sn': 'FOC2347X0GE',
                'vid': 'V03',
            },
            8: {
                'descr': 'StackPort2/1',
                'name': 'StackPort2/1',
                'pid': 'STACK-T1-50CM',
                'sn': 'MOC2346A69X',
                'vid': 'V01',
            },
            9: {
                'descr': 'StackPort2/2',
                'name': 'StackPort2/2',
                'pid': 'STACK-T1-50CM',
                'sn': 'MOC2346A691',
                'vid': 'V01',
            },
            10: {
                'descr': 'Switch 2 - Power Supply A',
                'name': 'Switch 2 - Power Supply A',
                'pid': 'PWR-C1-350WAC-P',
                'sn': 'DCC2337B0HT',
                'vid': 'V01',
            },
            11: {
                'descr': '8x10G Uplink Module',
                'name': 'Switch 2 FRU Uplink Module 1',
                'pid': 'C9300-NM-8X',
                'sn': 'FOC23456CVT',
                'vid': 'V02',
            },
            12: {
                'descr': 'C9300-24T - Provisioned',
                'name': 'Switch 3',
                'pid': 'C9300-24T',
            },
        },
    }

    def test_empty(self):
        self.device_empty = Mock(**self.empty_output)
        version_obj = ShowInventory(device=self.device_empty)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = version_obj.parse()

    def test_show_inventory_c9300(self):
        self.device = Mock(**self.golden_output)
        obj = ShowInventory(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden1(self):
        self.device = Mock(**self.golden_output1)
        obj = ShowInventory(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)


class TestShowEnvironmentAll(unittest.TestCase):
    maxDiff = None
    device_empty = Device(name='empty')
    device = Device(name='c9300')
    empty_output = {'execute.return_value': ''}

    # show environment all
    golden_output = {'execute.return_value': '''
        Switch   FAN     Speed   State
        ---------------------------------------------------
          1       1     14240     OK
          1       2     14240     OK
          1       3     14240     OK
        FAN PS-1 is OK
        FAN PS-2 is NOT PRESENT
        Switch   FAN     Speed   State
        ---------------------------------------------------
          2       1     14240     OK
          2       2     14240     OK
          2       3     14240     OK
        FAN PS-1 is OK
        FAN PS-2 is NOT PRESENT
        Switch 1: SYSTEM TEMPERATURE is OK
        Inlet Temperature Value: 21 Degree Celsius
        Temperature State: GREEN
        Yellow Threshold : 46 Degree Celsius
        Red Threshold    : 56 Degree Celsius

        Outlet Temperature Value: 32 Degree Celsius
        Temperature State: GREEN
        Yellow Threshold : 105 Degree Celsius
        Red Threshold    : 125 Degree Celsius

        Hotspot Temperature Value: 49 Degree Celsius
        Temperature State: GREEN
        Yellow Threshold : 105 Degree Celsius
        Red Threshold    : 125 Degree Celsius
        Switch 2: SYSTEM TEMPERATURE is OK
        Inlet Temperature Value: 21 Degree Celsius
        Temperature State: GREEN
        Yellow Threshold : 46 Degree Celsius
        Red Threshold    : 56 Degree Celsius

        Outlet Temperature Value: 31 Degree Celsius
        Temperature State: GREEN
        Yellow Threshold : 105 Degree Celsius
        Red Threshold    : 125 Degree Celsius

        Hotspot Temperature Value: 52 Degree Celsius
        Temperature State: GREEN
        Yellow Threshold : 105 Degree Celsius
        Red Threshold    : 125 Degree Celsius
        SW  PID                 Serial#     Status           Sys Pwr  PoE Pwr  Watts
        --  ------------------  ----------  ---------------  -------  -------  -----
        1A  PWR-C1-350WAC-P     DCC2337B0K5  OK              Good     n/a      350
        1B  Not Present
        2A  PWR-C1-350WAC-P     DCC2337B0HT  OK              Good     n/a      350
        2B  Not Present

    '''}

    golden_parsed_output = {
        'switch': {
            '1': {
                'fan': {
                    '1': {
                        'speed': '14240',
                        'state': 'ok',
                    },
                    '2': {
                        'speed': '14240',
                        'state': 'ok',
                    },
                    '3': {
                        'speed': '14240',
                        'state': 'ok',
                    },
                },
                'hotspot_temperature': {
                    'red_threshold': '125',
                    'state': 'green',
                    'value': '49',
                    'yellow_threshold': '105',
                },
                'inlet_temperature': {
                    'red_threshold': '56',
                    'state': 'green',
                    'value': '21',
                    'yellow_threshold': '46',
                },
                'outlet_temperature': {
                    'red_threshold': '125',
                    'state': 'green',
                    'value': '32',
                    'yellow_threshold': '105',
                },
                'power_supply': {
                    '1': {
                        'pid': 'PWR-C1-350WAC-P',
                        'poe_power': 'n/a',
                        'serial_number': 'DCC2337B0K5',
                        'state': 'ok',
                        'status': 'ok',
                        'system_power': 'good',
                        'watts': '350',
                    },
                    '2': {
                        'state': 'not present',
                        'status': 'not present',
                    },
                },
                'system_temperature_state': 'ok',
            },
            '2': {
                'fan': {
                    '1': {
                        'speed': '14240',
                        'state': 'ok',
                    },
                    '2': {
                        'speed': '14240',
                        'state': 'ok',
                    },
                    '3': {
                        'speed': '14240',
                        'state': 'ok',
                    },
                },
                'hotspot_temperature': {
                    'red_threshold': '125',
                    'state': 'green',
                    'value': '52',
                    'yellow_threshold': '105',
                },
                'inlet_temperature': {
                    'red_threshold': '56',
                    'state': 'green',
                    'value': '21',
                    'yellow_threshold': '46',
                },
                'outlet_temperature': {
                    'red_threshold': '125',
                    'state': 'green',
                    'value': '31',
                    'yellow_threshold': '105',
                },
                'power_supply': {
                    '1': {
                        'pid': 'PWR-C1-350WAC-P',
                        'poe_power': 'n/a',
                        'serial_number': 'DCC2337B0HT',
                        'state': 'ok',
                        'status': 'ok',
                        'system_power': 'good',
                        'watts': '350',
                    },
                    '2': {
                        'state': 'not present',
                        'status': 'not present',
                    },
                },
                'system_temperature_state': 'ok',
            },
        },
    }

    def test_empty(self):
        self.device_empty = Mock(**self.empty_output)
        version_obj = ShowEnvironmentAll(device=self.device_empty)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = version_obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowEnvironmentAll(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == '__main__':
    unittest.main()