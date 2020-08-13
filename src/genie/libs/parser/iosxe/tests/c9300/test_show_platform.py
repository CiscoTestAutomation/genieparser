#!/bin/env python
import unittest

from unittest.mock import Mock
from pyats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                             SchemaMissingKeyError
from genie.libs.parser.iosxe.c9500.show_platform import ShowInventory
from genie.libs.parser.iosxe.show_platform import ShowPlatformTcamUtilization


class TestShowInventory(unittest.TestCase):
    maxDiff = None
    device_empty = Device(name='empty')
    device = Device(name='C9300-FE3')
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
          '0': {
            'Mac Address Table': {
              'EM': {
                'I': {
                  'max_entry': '32768',
                  'use_entry': '33',
                  'percent': '0.10',
                  'v4': '0',
                  'v6': '0',
                  'mpls': '0',
                  'other': '33'
                }
              },
              'TCAM': {
                'I': {
                  'max_entry': '1024',
                  'use_entry': '21',
                  'percent': '2.05',
                  'v4': '0',
                  'v6': '0',
                  'mpls': '0',
                  'other': '21'
                }
              }
            },
            'L3 Multicast': {
              'EM': {
                'I': {
                  'max_entry': '8192',
                  'use_entry': '0',
                  'percent': '0.00',
                  'v4': '0',
                  'v6': '0',
                  'mpls': '0',
                  'other': '0'
                }
              },
              'TCAM': {
                'I': {
                  'max_entry': '512',
                  'use_entry': '67',
                  'percent': '13.09',
                  'v4': '3',
                  'v6': '64',
                  'mpls': '0',
                  'other': '0'
                }
              }
            },
            'L2 Multicast': {
              'EM': {
                'I': {
                  'max_entry': '8192',
                  'use_entry': '0',
                  'percent': '0.00',
                  'v4': '0',
                  'v6': '0',
                  'mpls': '0',
                  'other': '0'
                }
              },
              'TCAM': {
                'I': {
                  'max_entry': '512',
                  'use_entry': '11',
                  'percent': '2.15',
                  'v4': '3',
                  'v6': '8',
                  'mpls': '0',
                  'other': '0'
                }
              }
            },
            'IP Route Table': {
              'EM': {
                'I': {
                  'max_entry': '24576',
                  'use_entry': '40',
                  'percent': '0.16',
                  'v4': '25',
                  'v6': '4',
                  'mpls': '11',
                  'other': '0'
                }
              },
              'TCAM': {
                'I': {
                  'max_entry': '8192',
                  'use_entry': '76',
                  'percent': '0.93',
                  'v4': '29',
                  'v6': '44',
                  'mpls': '2',
                  'other': '1'
                }
              }
            },
            'QOS ACL': {
              'TCAM': {
                'IO': {
                  'max_entry': '5120',
                  'use_entry': '85',
                  'percent': '1.66',
                  'v4': '28',
                  'v6': '38',
                  'mpls': '0',
                  'other': '19'
                }
              }
            },
            'Security ACL': {
              'TCAM': {
                'IO': {
                  'max_entry': '5120',
                  'use_entry': '129',
                  'percent': '2.52',
                  'v4': '26',
                  'v6': '58',
                  'mpls': '0',
                  'other': '45'
                }
              }
            },
            'Netflow ACL': {
              'TCAM': {
                'I': {
                  'max_entry': '256',
                  'use_entry': '6',
                  'percent': '2.34',
                  'v4': '2',
                  'v6': '2',
                  'mpls': '0',
                  'other': '2'
                },
                'O': {
                  'max_entry': '768',
                  'use_entry': '6',
                  'percent': '0.78',
                  'v4': '2',
                  'v6': '2',
                  'mpls': '0',
                  'other': '2'
                }
              }
            },
            'PBR ACL': {
              'TCAM': {
                'I': {
                  'max_entry': '1024',
                  'use_entry': '22',
                  'percent': '2.15',
                  'v4': '16',
                  'v6': '6',
                  'mpls': '0',
                  'other': '0'
                }
              }
            },
            'Flow SPAN ACL': {
              'TCAM': {
                'IO': {
                  'max_entry': '1024',
                  'use_entry': '13',
                  'percent': '1.27',
                  'v4': '3',
                  'v6': '6',
                  'mpls': '0',
                  'other': '4'
                }
              }
            },
            'Control Plane': {
              'TCAM': {
                'I': {
                  'max_entry': '512',
                  'use_entry': '263',
                  'percent': '51.37',
                  'v4': '114',
                  'v6': '106',
                  'mpls': '0',
                  'other': '43'
                }
              }
            },
            'Tunnel Termination': {
              'TCAM': {
                'I': {
                  'max_entry': '512',
                  'use_entry': '51',
                  'percent': '9.96',
                  'v4': '41',
                  'v6': '10',
                  'mpls': '0',
                  'other': '0'
                }
              }
            },
            'Lisp Inst Mapping': {
              'TCAM': {
                'I': {
                  'max_entry': '2048',
                  'use_entry': '1',
                  'percent': '0.05',
                  'v4': '0',
                  'v6': '0',
                  'mpls': '0',
                  'other': '1'
                }
              }
            },
            'Security Association': {
              'TCAM': {
                'I': {
                  'max_entry': '256',
                  'use_entry': '4',
                  'percent': '1.56',
                  'v4': '2',
                  'v6': '2',
                  'mpls': '0',
                  'other': '0'
                }
              }
            },
            'CTS Cell Matrix/VPN Label': {
              'EM': {
                'O': {
                  'max_entry': '8192',
                  'use_entry': '0',
                  'percent': '0.00',
                  'v4': '0',
                  'v6': '0',
                  'mpls': '0',
                  'other': '0'
                }
              },
              'TCAM': {
                'O': {
                  'max_entry': '512',
                  'use_entry': '1',
                  'percent': '0.20',
                  'v4': '0',
                  'v6': '0',
                  'mpls': '0',
                  'other': '1'
                }
              }
            },
            'Client Table': {
              'EM': {
                'I': {
                  'max_entry': '4096',
                  'use_entry': '5',
                  'percent': '0.12',
                  'v4': '0',
                  'v6': '0',
                  'mpls': '0',
                  'other': '5'
                }
              },
              'TCAM': {
                'I': {
                  'max_entry': '256',
                  'use_entry': '0',
                  'percent': '0.00',
                  'v4': '0',
                  'v6': '0',
                  'mpls': '0',
                  'other': '0'
                }
              }
            },
            'Input Group LE': {
              'TCAM': {
                'I': {
                  'max_entry': '1024',
                  'use_entry': '0',
                  'percent': '0.00',
                  'v4': '0',
                  'v6': '0',
                  'mpls': '0',
                  'other': '0'
                }
              }
            },
            'Output Group LE': {
              'TCAM': {
                'O': {
                  'max_entry': '1024',
                  'use_entry': '0',
                  'percent': '0.00',
                  'v4': '0',
                  'v6': '0',
                  'mpls': '0',
                  'other': '0'
                }
              }
            },
            'Macsec SPD': {
              'TCAM': {
                'I': {
                  'max_entry': '256',
                  'use_entry': '2',
                  'percent': '0.78',
                  'v4': '0',
                  'v6': '0',
                  'mpls': '0',
                  'other': '2'
                }
              }
            }
          },
          '1': {
            'Mac Address Table': {
              'EM': {
                'I': {
                  'max_entry': '32768',
                  'use_entry': '33',
                  'percent': '0.10',
                  'v4': '0',
                  'v6': '0',
                  'mpls': '0',
                  'other': '33'
                }
              },
              'TCAM': {
                'I': {
                  'max_entry': '1024',
                  'use_entry': '21',
                  'percent': '2.05',
                  'v4': '0',
                  'v6': '0',
                  'mpls': '0',
                  'other': '21'
                }
              }
            },
            'L3 Multicast': {
              'EM': {
                'I': {
                  'max_entry': '8192',
                  'use_entry': '0',
                  'percent': '0.00',
                  'v4': '0',
                  'v6': '0',
                  'mpls': '0',
                  'other': '0'
                }
              },
              'TCAM': {
                'I': {
                  'max_entry': '512',
                  'use_entry': '67',
                  'percent': '13.09',
                  'v4': '3',
                  'v6': '64',
                  'mpls': '0',
                  'other': '0'
                }
              }
            },
            'L2 Multicast': {
              'EM': {
                'I': {
                  'max_entry': '8192',
                  'use_entry': '0',
                  'percent': '0.00',
                  'v4': '0',
                  'v6': '0',
                  'mpls': '0',
                  'other': '0'
                }
              },
              'TCAM': {
                'I': {
                  'max_entry': '512',
                  'use_entry': '11',
                  'percent': '2.15',
                  'v4': '3',
                  'v6': '8',
                  'mpls': '0',
                  'other': '0'
                }
              }
            },
            'IP Route Table': {
              'EM': {
                'I': {
                  'max_entry': '24576',
                  'use_entry': '40',
                  'percent': '0.16',
                  'v4': '25',
                  'v6': '4',
                  'mpls': '11',
                  'other': '0'
                }
              },
              'TCAM': {
                'I': {
                  'max_entry': '8192',
                  'use_entry': '76',
                  'percent': '0.93',
                  'v4': '29',
                  'v6': '44',
                  'mpls': '2',
                  'other': '1'
                }
              }
            },
            'QOS ACL': {
              'TCAM': {
                'IO': {
                  'max_entry': '5120',
                  'use_entry': '81',
                  'percent': '1.58',
                  'v4': '27',
                  'v6': '36',
                  'mpls': '0',
                  'other': '18'
                }
              }
            },
            'Security ACL': {
              'TCAM': {
                'IO': {
                  'max_entry': '5120',
                  'use_entry': '129',
                  'percent': '2.52',
                  'v4': '26',
                  'v6': '58',
                  'mpls': '0',
                  'other': '45'
                }
              }
            },
            'Netflow ACL': {
              'TCAM': {
                'I': {
                  'max_entry': '256',
                  'use_entry': '7',
                  'percent': '2.73',
                  'v4': '3',
                  'v6': '2',
                  'mpls': '0',
                  'other': '2'
                },
                'O': {
                  'max_entry': '768',
                  'use_entry': '7',
                  'percent': '0.91',
                  'v4': '3',
                  'v6': '2',
                  'mpls': '0',
                  'other': '2'
                }
              }
            },
            'PBR ACL': {
              'TCAM': {
                'I': {
                  'max_entry': '1024',
                  'use_entry': '22',
                  'percent': '2.15',
                  'v4': '16',
                  'v6': '6',
                  'mpls': '0',
                  'other': '0'
                }
              }
            },
            'Flow SPAN ACL': {
              'TCAM': {
                'IO': {
                  'max_entry': '1024',
                  'use_entry': '13',
                  'percent': '1.27',
                  'v4': '3',
                  'v6': '6',
                  'mpls': '0',
                  'other': '4'
                }
              }
            },
            'Control Plane': {
              'TCAM': {
                'I': {
                  'max_entry': '512',
                  'use_entry': '263',
                  'percent': '51.37',
                  'v4': '114',
                  'v6': '106',
                  'mpls': '0',
                  'other': '43'
                }
              }
            },
            'Tunnel Termination': {
              'TCAM': {
                'I': {
                  'max_entry': '512',
                  'use_entry': '51',
                  'percent': '9.96',
                  'v4': '41',
                  'v6': '10',
                  'mpls': '0',
                  'other': '0'
                }
              }
            },
            'Lisp Inst Mapping': {
              'TCAM': {
                'I': {
                  'max_entry': '2048',
                  'use_entry': '1',
                  'percent': '0.05',
                  'v4': '0',
                  'v6': '0',
                  'mpls': '0',
                  'other': '1'
                }
              }
            },
            'Security Association': {
              'TCAM': {
                'I': {
                  'max_entry': '256',
                  'use_entry': '3',
                  'percent': '1.17',
                  'v4': '1',
                  'v6': '2',
                  'mpls': '0',
                  'other': '0'
                }
              }
            },
            'CTS Cell Matrix/VPN Label': {
              'EM': {
                'O': {
                  'max_entry': '8192',
                  'use_entry': '0',
                  'percent': '0.00',
                  'v4': '0',
                  'v6': '0',
                  'mpls': '0',
                  'other': '0'
                }
              },
              'TCAM': {
                'O': {
                  'max_entry': '512',
                  'use_entry': '1',
                  'percent': '0.20',
                  'v4': '0',
                  'v6': '0',
                  'mpls': '0',
                  'other': '1'
                }
              }
            },
            'Client Table': {
              'EM': {
                'I': {
                  'max_entry': '4096',
                  'use_entry': '11',
                  'percent': '0.27',
                  'v4': '0',
                  'v6': '0',
                  'mpls': '0',
                  'other': '11'
                }
              },
              'TCAM': {
                'I': {
                  'max_entry': '256',
                  'use_entry': '0',
                  'percent': '0.00',
                  'v4': '0',
                  'v6': '0',
                  'mpls': '0',
                  'other': '0'
                }
              }
            },
            'Input Group LE': {
              'TCAM': {
                'I': {
                  'max_entry': '1024',
                  'use_entry': '0',
                  'percent': '0.00',
                  'v4': '0',
                  'v6': '0',
                  'mpls': '0',
                  'other': '0'
                }
              }
            },
            'Output Group LE': {
              'TCAM': {
                'O': {
                  'max_entry': '1024',
                  'use_entry': '0',
                  'percent': '0.00',
                  'v4': '0',
                  'v6': '0',
                  'mpls': '0',
                  'other': '0'
                }
              }
            },
            'Macsec SPD': {
              'TCAM': {
                'I': {
                  'max_entry': '256',
                  'use_entry': '2',
                  'percent': '0.78',
                  'v4': '0',
                  'v6': '0',
                  'mpls': '0',
                  'other': '2'
                }
              }
            }
          }
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
