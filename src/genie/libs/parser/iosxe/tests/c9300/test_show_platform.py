#!/bin/env python
import unittest

from unittest.mock import Mock
from pyats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                             SchemaMissingKeyError
from genie.libs.parser.iosxe.c9500.show_platform import ShowInventory


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


if __name__ == '__main__':
    unittest.main()