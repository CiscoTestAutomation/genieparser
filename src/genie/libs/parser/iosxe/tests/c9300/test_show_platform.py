#!/bin/env python
import unittest

from unittest.mock import Mock
from pyats.topology import Device

from genie.metaparser.util.exceptions import (SchemaMissingKeyError,
                                              SchemaEmptyParserError)
from genie.libs.parser.iosxe.c9300.show_platform import (ShowInventory,
                                                         ShowEnvironmentAll)
from genie.libs.parser.iosxe.show_platform import ShowPlatformTcamUtilization


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
                        'speed': 14240,
                        'state': 'OK',
                    },
                    '2': {
                        'speed': 14240,
                        'state': 'OK',
                    },
                    '3': {
                        'speed': 14240,
                        'state': 'OK',
                    },
                },
                'hotspot_temperature': {
                    'red_threshold': '125',
                    'state': 'GREEN',
                    'value': '49',
                    'yellow_threshold': '105',
                },
                'inlet_temperature': {
                    'red_threshold': '56',
                    'state': 'GREEN',
                    'value': '21',
                    'yellow_threshold': '46',
                },
                'outlet_temperature': {
                    'red_threshold': '125',
                    'state': 'GREEN',
                    'value': '32',
                    'yellow_threshold': '105',
                },
                'power_supply': {
                    '1': {
                        'pid': 'PWR-C1-350WAC-P',
                        'poe_power': 'n/a',
                        'serial_number': 'DCC2337B0K5',
                        'state': 'OK',
                        'status': 'OK',
                        'system_power': 'Good',
                        'watts': '350',
                    },
                    '2': {
                        'state': 'NOT PRESENT',
                        'status': 'Not Present',
                    },
                },
                'system_temperature_state': 'OK',
            },
            '2': {
                'fan': {
                    '1': {
                        'speed': 14240,
                        'state': 'OK',
                    },
                    '2': {
                        'speed': 14240,
                        'state': 'OK',
                    },
                    '3': {
                        'speed': 14240,
                        'state': 'OK',
                    },
                },
                'hotspot_temperature': {
                    'red_threshold': '125',
                    'state': 'GREEN',
                    'value': '52',
                    'yellow_threshold': '105',
                },
                'inlet_temperature': {
                    'red_threshold': '56',
                    'state': 'GREEN',
                    'value': '21',
                    'yellow_threshold': '46',
                },
                'outlet_temperature': {
                    'red_threshold': '125',
                    'state': 'GREEN',
                    'value': '31',
                    'yellow_threshold': '105',
                },
                'power_supply': {
                    '1': {
                        'pid': 'PWR-C1-350WAC-P',
                        'poe_power': 'n/a',
                        'serial_number': 'DCC2337B0HT',
                        'state': 'OK',
                        'status': 'OK',
                        'system_power': 'Good',
                        'watts': '350',
                    },
                    '2': {
                        'state': 'NOT PRESENT',
                        'status': 'Not Present',
                    },
                },
                'system_temperature_state': 'OK',
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


class TestShowPlatformTcamUtilization(unittest.TestCase):
    maxDiff = None
    device_empty = Device(name='empty')
    device = Device(name='9300-FE3')
    empty_output = {'execute.return_value': ''}


    # show inventory
    golden_output = {'execute.return_value': '''
    Codes: EM - Exact_Match, I - Input, O - Output, IO - Input & Output, NA - Not Applicable
    CAM Utilization for ASIC  [0]
    Table                  Subtype      Dir      Max     Used    %Used       V4       V6     MPLS    Other
    ------------------------------------------------------------------------------------------------------
    Mac Address Table      EM           I       32768       33    0.10%        0        0        0       33
    Mac Address Table      TCAM         I        1024       21    2.05%        0        0        0       21
    L3 Multicast           EM           I        8192        0    0.00%        0        0        0        0
    L3 Multicast           TCAM         I         512       67   13.09%        3       64        0        0
    L2 Multicast           EM           I        8192        0    0.00%        0        0        0        0
    L2 Multicast           TCAM         I         512       11    2.15%        3        8        0        0
    IP Route Table         EM           I       24576       40    0.16%       25        4       11        0
    IP Route Table         TCAM         I        8192       76    0.93%       29       44        2        1
    QOS ACL                TCAM         IO       5120       85    1.66%       28       38        0       19
    Security ACL           TCAM         IO       5120      129    2.52%       26       58        0       45
    Netflow ACL            TCAM         I         256        6    2.34%        2        2        0        2
    PBR ACL                TCAM         I        1024       22    2.15%       16        6        0        0
    Netflow ACL            TCAM         O         768        6    0.78%        2        2        0        2
    Flow SPAN ACL          TCAM         IO       1024       13    1.27%        3        6        0        4
    Control Plane          TCAM         I         512      263   51.37%      114      106        0       43
    Tunnel Termination     TCAM         I         512       51    9.96%       41       10        0        0
    Lisp Inst Mapping      TCAM         I        2048        1    0.05%        0        0        0        1
    Security Association   TCAM         I         256        4    1.56%        2        2        0        0
    CTS Cell Matrix/VPN
    Label                  EM           O        8192        0    0.00%        0        0        0        0
    CTS Cell Matrix/VPN
    Label                  TCAM         O         512        1    0.20%        0        0        0        1
    Client Table           EM           I        4096        5    0.12%        0        0        0        5
    Client Table           TCAM         I         256        0    0.00%        0        0        0        0
    Input Group LE         TCAM         I        1024        0    0.00%        0        0        0        0
    Output Group LE        TCAM         O        1024        0    0.00%        0        0        0        0
    Macsec SPD             TCAM         I         256        2    0.78%        0        0        0        2

    CAM Utilization for ASIC  [1]

    Table                  Subtype      Dir      Max     Used    %Used       V4       V6     MPLS    Other
    ------------------------------------------------------------------------------------------------------
    Mac Address Table      EM           I       32768       33    0.10%        0        0        0       33
    Mac Address Table      TCAM         I        1024       21    2.05%        0        0        0       21
    L3 Multicast           EM           I        8192        0    0.00%        0        0        0        0
    L3 Multicast           TCAM         I         512       67   13.09%        3       64        0        0
    L2 Multicast           EM           I        8192        0    0.00%        0        0        0        0
    L2 Multicast           TCAM         I         512       11    2.15%        3        8        0        0
    IP Route Table         EM           I       24576       40    0.16%       25        4       11        0
    IP Route Table         TCAM         I        8192       76    0.93%       29       44        2        1
    QOS ACL                TCAM         IO       5120       81    1.58%       27       36        0       18
    Security ACL           TCAM         IO       5120      129    2.52%       26       58        0       45
    Netflow ACL            TCAM         I         256        7    2.73%        3        2        0        2
    PBR ACL                TCAM         I        1024       22    2.15%       16        6        0        0
    Netflow ACL            TCAM         O         768        7    0.91%        3        2        0        2
    Flow SPAN ACL          TCAM         IO       1024       13    1.27%        3        6        0        4
    Control Plane          TCAM         I         512      263   51.37%      114      106        0       43
    Tunnel Termination     TCAM         I         512       51    9.96%       41       10        0        0
    Lisp Inst Mapping      TCAM         I        2048        1    0.05%        0        0        0        1
    Security Association   TCAM         I         256        3    1.17%        1        2        0        0
    CTS Cell Matrix/VPN
    Label                  EM           O        8192        0    0.00%        0        0        0        0
    CTS Cell Matrix/VPN
    Label                  TCAM         O         512        1    0.20%        0        0        0        1
    Client Table           EM           I        4096       11    0.27%        0        0        0       11
    Client Table           TCAM         I         256        0    0.00%        0        0        0        0
    Input Group LE         TCAM         I        1024        0    0.00%        0        0        0        0
    Output Group LE        TCAM         O        1024        0    0.00%        0        0        0        0
    Macsec SPD             TCAM         I         256        2    0.78%        0        0        0        2
    '''}

    golden_parsed_output = {
        'asic': {
            '0': {
                'table': {
                    'CTS Cell Matrix/VPN Label': {
                        'subtype': {
                            'EM': {
                                'dir': {
                                    'O': {
                                        'max': '8192',
                                        'mpls': '0',
                                        'other': '0',
                                        'used': '0',
                                        'used_percent': '0.00%',
                                        'v4': '0',
                                        'v6': '0',
                                    },
                                },
                            },
                            'TCAM': {
                                'dir': {
                                    'O': {
                                        'max': '512',
                                        'mpls': '0',
                                        'other': '1',
                                        'used': '1',
                                        'used_percent': '0.20%',
                                        'v4': '0',
                                        'v6': '0',
                                    },
                                },
                            },
                        },
                    },
                    'Client Table': {
                        'subtype': {
                            'EM': {
                                'dir': {
                                    'I': {
                                        'max': '4096',
                                        'mpls': '0',
                                        'other': '5',
                                        'used': '5',
                                        'used_percent': '0.12%',
                                        'v4': '0',
                                        'v6': '0',
                                    },
                                },
                            },
                            'TCAM': {
                                'dir': {
                                    'I': {
                                        'max': '256',
                                        'mpls': '0',
                                        'other': '0',
                                        'used': '0',
                                        'used_percent': '0.00%',
                                        'v4': '0',
                                        'v6': '0',
                                    },
                                },
                            },
                        },
                    },
                    'Control Plane': {
                        'subtype': {
                            'TCAM': {
                                'dir': {
                                    'I': {
                                        'max': '512',
                                        'mpls': '0',
                                        'other': '43',
                                        'used': '263',
                                        'used_percent': '51.37%',
                                        'v4': '114',
                                        'v6': '106',
                                    },
                                },
                            },
                        },
                    },
                    'Flow SPAN ACL': {
                        'subtype': {
                            'TCAM': {
                                'dir': {
                                    'IO': {
                                        'max': '1024',
                                        'mpls': '0',
                                        'other': '4',
                                        'used': '13',
                                        'used_percent': '1.27%',
                                        'v4': '3',
                                        'v6': '6',
                                    },
                                },
                            },
                        },
                    },
                    'IP Route Table': {
                        'subtype': {
                            'EM': {
                                'dir': {
                                    'I': {
                                        'max': '24576',
                                        'mpls': '11',
                                        'other': '0',
                                        'used': '40',
                                        'used_percent': '0.16%',
                                        'v4': '25',
                                        'v6': '4',
                                    },
                                },
                            },
                            'TCAM': {
                                'dir': {
                                    'I': {
                                        'max': '8192',
                                        'mpls': '2',
                                        'other': '1',
                                        'used': '76',
                                        'used_percent': '0.93%',
                                        'v4': '29',
                                        'v6': '44',
                                    },
                                },
                            },
                        },
                    },
                    'Input Group LE': {
                        'subtype': {
                            'TCAM': {
                                'dir': {
                                    'I': {
                                        'max': '1024',
                                        'mpls': '0',
                                        'other': '0',
                                        'used': '0',
                                        'used_percent': '0.00%',
                                        'v4': '0',
                                        'v6': '0',
                                    },
                                },
                            },
                        },
                    },
                    'L2 Multicast': {
                        'subtype': {
                            'EM': {
                                'dir': {
                                    'I': {
                                        'max': '8192',
                                        'mpls': '0',
                                        'other': '0',
                                        'used': '0',
                                        'used_percent': '0.00%',
                                        'v4': '0',
                                        'v6': '0',
                                    },
                                },
                            },
                            'TCAM': {
                                'dir': {
                                    'I': {
                                        'max': '512',
                                        'mpls': '0',
                                        'other': '0',
                                        'used': '11',
                                        'used_percent': '2.15%',
                                        'v4': '3',
                                        'v6': '8',
                                    },
                                },
                            },
                        },
                    },
                    'L3 Multicast': {
                        'subtype': {
                            'EM': {
                                'dir': {
                                    'I': {
                                        'max': '8192',
                                        'mpls': '0',
                                        'other': '0',
                                        'used': '0',
                                        'used_percent': '0.00%',
                                        'v4': '0',
                                        'v6': '0',
                                    },
                                },
                            },
                            'TCAM': {
                                'dir': {
                                    'I': {
                                        'max': '512',
                                        'mpls': '0',
                                        'other': '0',
                                        'used': '67',
                                        'used_percent': '13.09%',
                                        'v4': '3',
                                        'v6': '64',
                                    },
                                },
                            },
                        },
                    },
                    'Lisp Inst Mapping': {
                        'subtype': {
                            'TCAM': {
                                'dir': {
                                    'I': {
                                        'max': '2048',
                                        'mpls': '0',
                                        'other': '1',
                                        'used': '1',
                                        'used_percent': '0.05%',
                                        'v4': '0',
                                        'v6': '0',
                                    },
                                },
                            },
                        },
                    },
                    'Mac Address Table': {
                        'subtype': {
                            'EM': {
                                'dir': {
                                    'I': {
                                        'max': '32768',
                                        'mpls': '0',
                                        'other': '33',
                                        'used': '33',
                                        'used_percent': '0.10%',
                                        'v4': '0',
                                        'v6': '0',
                                    },
                                },
                            },
                            'TCAM': {
                                'dir': {
                                    'I': {
                                        'max': '1024',
                                        'mpls': '0',
                                        'other': '21',
                                        'used': '21',
                                        'used_percent': '2.05%',
                                        'v4': '0',
                                        'v6': '0',
                                    },
                                },
                            },
                        },
                    },
                    'Macsec SPD': {
                        'subtype': {
                            'TCAM': {
                                'dir': {
                                    'I': {
                                        'max': '256',
                                        'mpls': '0',
                                        'other': '2',
                                        'used': '2',
                                        'used_percent': '0.78%',
                                        'v4': '0',
                                        'v6': '0',
                                    },
                                },
                            },
                        },
                    },
                    'Netflow ACL': {
                        'subtype': {
                            'TCAM': {
                                'dir': {
                                    'I': {
                                        'max': '256',
                                        'mpls': '0',
                                        'other': '2',
                                        'used': '6',
                                        'used_percent': '2.34%',
                                        'v4': '2',
                                        'v6': '2',
                                    },
                                    'O': {
                                        'max': '768',
                                        'mpls': '0',
                                        'other': '2',
                                        'used': '6',
                                        'used_percent': '0.78%',
                                        'v4': '2',
                                        'v6': '2',
                                    },
                                },
                            },
                        },
                    },
                    'Output Group LE': {
                        'subtype': {
                            'TCAM': {
                                'dir': {
                                    'O': {
                                        'max': '1024',
                                        'mpls': '0',
                                        'other': '0',
                                        'used': '0',
                                        'used_percent': '0.00%',
                                        'v4': '0',
                                        'v6': '0',
                                    },
                                },
                            },
                        },
                    },
                    'PBR ACL': {
                        'subtype': {
                            'TCAM': {
                                'dir': {
                                    'I': {
                                        'max': '1024',
                                        'mpls': '0',
                                        'other': '0',
                                        'used': '22',
                                        'used_percent': '2.15%',
                                        'v4': '16',
                                        'v6': '6',
                                    },
                                },
                            },
                        },
                    },
                    'QOS ACL': {
                        'subtype': {
                            'TCAM': {
                                'dir': {
                                    'IO': {
                                        'max': '5120',
                                        'mpls': '0',
                                        'other': '19',
                                        'used': '85',
                                        'used_percent': '1.66%',
                                        'v4': '28',
                                        'v6': '38',
                                    },
                                },
                            },
                        },
                    },
                    'Security ACL': {
                        'subtype': {
                            'TCAM': {
                                'dir': {
                                    'IO': {
                                        'max': '5120',
                                        'mpls': '0',
                                        'other': '45',
                                        'used': '129',
                                        'used_percent': '2.52%',
                                        'v4': '26',
                                        'v6': '58',
                                    },
                                },
                            },
                        },
                    },
                    'Security Association': {
                        'subtype': {
                            'TCAM': {
                                'dir': {
                                    'I': {
                                        'max': '256',
                                        'mpls': '0',
                                        'other': '0',
                                        'used': '4',
                                        'used_percent': '1.56%',
                                        'v4': '2',
                                        'v6': '2',
                                    },
                                },
                            },
                        },
                    },
                    'Tunnel Termination': {
                        'subtype': {
                            'TCAM': {
                                'dir': {
                                    'I': {
                                        'max': '512',
                                        'mpls': '0',
                                        'other': '0',
                                        'used': '51',
                                        'used_percent': '9.96%',
                                        'v4': '41',
                                        'v6': '10',
                                    },
                                },
                            },
                        },
                    },
                },
            },
            '1': {
                'table': {
                    'CTS Cell Matrix/VPN Label': {
                        'subtype': {
                            'EM': {
                                'dir': {
                                    'O': {
                                        'max': '8192',
                                        'mpls': '0',
                                        'other': '0',
                                        'used': '0',
                                        'used_percent': '0.00%',
                                        'v4': '0',
                                        'v6': '0',
                                    },
                                },
                            },
                            'TCAM': {
                                'dir': {
                                    'O': {
                                        'max': '512',
                                        'mpls': '0',
                                        'other': '1',
                                        'used': '1',
                                        'used_percent': '0.20%',
                                        'v4': '0',
                                        'v6': '0',
                                    },
                                },
                            },
                        },
                    },
                    'Client Table': {
                        'subtype': {
                            'EM': {
                                'dir': {
                                    'I': {
                                        'max': '4096',
                                        'mpls': '0',
                                        'other': '11',
                                        'used': '11',
                                        'used_percent': '0.27%',
                                        'v4': '0',
                                        'v6': '0',
                                    },
                                },
                            },
                            'TCAM': {
                                'dir': {
                                    'I': {
                                        'max': '256',
                                        'mpls': '0',
                                        'other': '0',
                                        'used': '0',
                                        'used_percent': '0.00%',
                                        'v4': '0',
                                        'v6': '0',
                                    },
                                },
                            },
                        },
                    },
                    'Control Plane': {
                        'subtype': {
                            'TCAM': {
                                'dir': {
                                    'I': {
                                        'max': '512',
                                        'mpls': '0',
                                        'other': '43',
                                        'used': '263',
                                        'used_percent': '51.37%',
                                        'v4': '114',
                                        'v6': '106',
                                    },
                                },
                            },
                        },
                    },
                    'Flow SPAN ACL': {
                        'subtype': {
                            'TCAM': {
                                'dir': {
                                    'IO': {
                                        'max': '1024',
                                        'mpls': '0',
                                        'other': '4',
                                        'used': '13',
                                        'used_percent': '1.27%',
                                        'v4': '3',
                                        'v6': '6',
                                    },
                                },
                            },
                        },
                    },
                    'IP Route Table': {
                        'subtype': {
                            'EM': {
                                'dir': {
                                    'I': {
                                        'max': '24576',
                                        'mpls': '11',
                                        'other': '0',
                                        'used': '40',
                                        'used_percent': '0.16%',
                                        'v4': '25',
                                        'v6': '4',
                                    },
                                },
                            },
                            'TCAM': {
                                'dir': {
                                    'I': {
                                        'max': '8192',
                                        'mpls': '2',
                                        'other': '1',
                                        'used': '76',
                                        'used_percent': '0.93%',
                                        'v4': '29',
                                        'v6': '44',
                                    },
                                },
                            },
                        },
                    },
                    'Input Group LE': {
                        'subtype': {
                            'TCAM': {
                                'dir': {
                                    'I': {
                                        'max': '1024',
                                        'mpls': '0',
                                        'other': '0',
                                        'used': '0',
                                        'used_percent': '0.00%',
                                        'v4': '0',
                                        'v6': '0',
                                    },
                                },
                            },
                        },
                    },
                    'L2 Multicast': {
                        'subtype': {
                            'EM': {
                                'dir': {
                                    'I': {
                                        'max': '8192',
                                        'mpls': '0',
                                        'other': '0',
                                        'used': '0',
                                        'used_percent': '0.00%',
                                        'v4': '0',
                                        'v6': '0',
                                    },
                                },
                            },
                            'TCAM': {
                                'dir': {
                                    'I': {
                                        'max': '512',
                                        'mpls': '0',
                                        'other': '0',
                                        'used': '11',
                                        'used_percent': '2.15%',
                                        'v4': '3',
                                        'v6': '8',
                                    },
                                },
                            },
                        },
                    },
                    'L3 Multicast': {
                        'subtype': {
                            'EM': {
                                'dir': {
                                    'I': {
                                        'max': '8192',
                                        'mpls': '0',
                                        'other': '0',
                                        'used': '0',
                                        'used_percent': '0.00%',
                                        'v4': '0',
                                        'v6': '0',
                                    },
                                },
                            },
                            'TCAM': {
                                'dir': {
                                    'I': {
                                        'max': '512',
                                        'mpls': '0',
                                        'other': '0',
                                        'used': '67',
                                        'used_percent': '13.09%',
                                        'v4': '3',
                                        'v6': '64',
                                    },
                                },
                            },
                        },
                    },
                    'Lisp Inst Mapping': {
                        'subtype': {
                            'TCAM': {
                                'dir': {
                                    'I': {
                                        'max': '2048',
                                        'mpls': '0',
                                        'other': '1',
                                        'used': '1',
                                        'used_percent': '0.05%',
                                        'v4': '0',
                                        'v6': '0',
                                    },
                                },
                            },
                        },
                    },
                    'Mac Address Table': {
                        'subtype': {
                            'EM': {
                                'dir': {
                                    'I': {
                                        'max': '32768',
                                        'mpls': '0',
                                        'other': '33',
                                        'used': '33',
                                        'used_percent': '0.10%',
                                        'v4': '0',
                                        'v6': '0',
                                    },
                                },
                            },
                            'TCAM': {
                                'dir': {
                                    'I': {
                                        'max': '1024',
                                        'mpls': '0',
                                        'other': '21',
                                        'used': '21',
                                        'used_percent': '2.05%',
                                        'v4': '0',
                                        'v6': '0',
                                    },
                                },
                            },
                        },
                    },
                    'Macsec SPD': {
                        'subtype': {
                            'TCAM': {
                                'dir': {
                                    'I': {
                                        'max': '256',
                                        'mpls': '0',
                                        'other': '2',
                                        'used': '2',
                                        'used_percent': '0.78%',
                                        'v4': '0',
                                        'v6': '0',
                                    },
                                },
                            },
                        },
                    },
                    'Netflow ACL': {
                        'subtype': {
                            'TCAM': {
                                'dir': {
                                    'I': {
                                        'max': '256',
                                        'mpls': '0',
                                        'other': '2',
                                        'used': '7',
                                        'used_percent': '2.73%',
                                        'v4': '3',
                                        'v6': '2',
                                    },
                                    'O': {
                                        'max': '768',
                                        'mpls': '0',
                                        'other': '2',
                                        'used': '7',
                                        'used_percent': '0.91%',
                                        'v4': '3',
                                        'v6': '2',
                                    },
                                },
                            },
                        },
                    },
                    'Output Group LE': {
                        'subtype': {
                            'TCAM': {
                                'dir': {
                                    'O': {
                                        'max': '1024',
                                        'mpls': '0',
                                        'other': '0',
                                        'used': '0',
                                        'used_percent': '0.00%',
                                        'v4': '0',
                                        'v6': '0',
                                    },
                                },
                            },
                        },
                    },
                    'PBR ACL': {
                        'subtype': {
                            'TCAM': {
                                'dir': {
                                    'I': {
                                        'max': '1024',
                                        'mpls': '0',
                                        'other': '0',
                                        'used': '22',
                                        'used_percent': '2.15%',
                                        'v4': '16',
                                        'v6': '6',
                                    },
                                },
                            },
                        },
                    },
                    'QOS ACL': {
                        'subtype': {
                            'TCAM': {
                                'dir': {
                                    'IO': {
                                        'max': '5120',
                                        'mpls': '0',
                                        'other': '18',
                                        'used': '81',
                                        'used_percent': '1.58%',
                                        'v4': '27',
                                        'v6': '36',
                                    },
                                },
                            },
                        },
                    },
                    'Security ACL': {
                        'subtype': {
                            'TCAM': {
                                'dir': {
                                    'IO': {
                                        'max': '5120',
                                        'mpls': '0',
                                        'other': '45',
                                        'used': '129',
                                        'used_percent': '2.52%',
                                        'v4': '26',
                                        'v6': '58',
                                    },
                                },
                            },
                        },
                    },
                    'Security Association': {
                        'subtype': {
                            'TCAM': {
                                'dir': {
                                    'I': {
                                        'max': '256',
                                        'mpls': '0',
                                        'other': '0',
                                        'used': '3',
                                        'used_percent': '1.17%',
                                        'v4': '1',
                                        'v6': '2',
                                    },
                                },
                            },
                        },
                    },
                    'Tunnel Termination': {
                        'subtype': {
                            'TCAM': {
                                'dir': {
                                    'I': {
                                        'max': '512',
                                        'mpls': '0',
                                        'other': '0',
                                        'used': '51',
                                        'used_percent': '9.96%',
                                        'v4': '41',
                                        'v6': '10',
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }

    def test_empty(self):
        self.device_empty = Mock(**self.empty_output)
        version_obj = ShowPlatformTcamUtilization(device=self.device_empty)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = version_obj.parse()

    def test_show_tcam_c9300(self):
        self.device = Mock(**self.golden_output)
        obj = ShowPlatformTcamUtilization(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == '__main__':
    unittest.main()
