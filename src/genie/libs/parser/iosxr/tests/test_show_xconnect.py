# Python
import unittest
from unittest.mock import Mock
from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError

from genie.libs.parser.iosxr.show_xconnect import (ShowL2vpnXconnect,
                                                   ShowL2vpnXconnectDetail,
                                                   ShowL2vpnXconnectSummary,
                                                   ShowL2VpnXconnectBrief,
                                                   ShowL2vpnXconnectMp2mpDetail)

# ==========================================
#  Unit test for 'show l2vpn xconnect brief'
# ==========================================
class TestShowL2vpnXconnectBrief(unittest.TestCase):
    '''Unit test for 'show l2vpn xconnect brief' '''

    maxDiff = None
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'atom': 
            {'like_to_like': 
                {'efp': 
                    {'down': 0,
                    'unr': 0,
                    'up': 10},
                'total': 
                    {'down': 0,
                    'unr': 0,
                    'up': 10}},
            'total':
                {'down': 0,
                'unr': 0,
                'up': 10}},
        'locally_switching': 
            {'like_to_like': 
                {'efp': 
                    {'down': 0,
                    'unr': 0,
                    'up': 3},
                'efp_invalid_ac':
                    {'down': 0,
                    'unr': 1,
                    'up': 0},
                'invalid_ac': 
                    {'down': 0,
                    'unr': 1,
                    'up': 0},
                'total': 
                    {'down': 0,
                    'unr': 2,
                    'up': 3}},
            'total':
                {'down': 0,
                'unr': 2,
                'up': 3}}}

    golden_output1 = {'execute.return_value': '''
        RP/0/RP0/CPU0:ios# show l2vpn xconnect brief 
        Mon Sep 19 10:52:27.818 UTC
        Locally Switching
          Like-to-Like                        UP       DOWN        UNR
            Invalid AC                         0          0          1
            EFP/Invalid AC                     0          0          1
            EFP                                3          0          0
            Total                              3          0          2

          Total                                3          0          2

        AToM
          Like-to-Like                        UP       DOWN        UNR
            EFP                               10          0          0
            Total                             10          0          0

          Total                               10          0          0
        '''}

    golden_parsed_output2 = {
        'atom': 
            {'like_to_like': 
                {'efp': 
                    {'down': 0,
                    'unr': 0,
                    'up': 32},
                'total': 
                    {'down': 0,
                    'unr': 0,
                    'up': 32}},
            'total': 
                {'down': 0,
                'unr': 0,
                'up': 32}},
        'locally_switching': 
            {'like_to_like': 
                {'ether': 
                    {'down': 0,
                    'unr': 0,
                    'up': 1},
                'total':
                    {'down': 0,
                    'unr': 0,
                    'up': 1}},
            'total':
                {'down': 0,
                'unr': 0,
                'up': 1}}}

    golden_output2 = {'execute.return_value': '''
        RP/0/RP0/CPU0:SIT-540#show l2vpn xconnect brief 
        Sat Aug  4 14:48:34.079 IST
        Locally Switching
          Like-to-Like                        UP       DOWN        UNR
            Ether                              1          0          0
            Total                              1          0          0

          Total                                1          0          0

        AToM
          Like-to-Like                        UP       DOWN        UNR
            EFP                               32          0          0
            Total                             32          0          0

          Total                               32          0          0
        '''}

    golden_parsed_output3 = {
        'total': 
            {'down': 0,
            'unr': 0,
            'up': 0}}

    golden_output3 = {'execute.return_value': '''
        [2019-10-08 09:30:35,071] +++ R2_xr: executing command 'show l2vpn xconnect brief' +++
        show l2vpn xconnect brief
        Tue Oct  8 16:30:05.044 UTC
        Total: 0 UP, 0 DOWN, 0 UNRESOLVED
        '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowL2VpnXconnectBrief(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden1(self):
        self.device = Mock(**self.golden_output1)
        obj = ShowL2VpnXconnectBrief(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)
    
    def test_golden2(self):
        self.device = Mock(**self.golden_output2)
        obj = ShowL2VpnXconnectBrief(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_golden3(self):
        self.device = Mock(**self.golden_output3)
        obj = ShowL2VpnXconnectBrief(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output3)


# ==================================================
#  Unit test for 'show l2vpn xconnect'
# ==================================================
class TestShowL2vpnXconnect(unittest.TestCase):
    """Unit test for 'show l2vpn xconnect' """

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'groups': {
            'Test_XCONN_Group': {
                'name': {
                    '1000': {
                        'status': 'DN',
                        'segment1': {
                            'GigabitEthernet0/0/0/5.1000': {
                                'status': 'UP',
                                'segment2': {
                                    '10.4.1.206       1000': {
                                        'status': 'DN',
                                    },
                                },
                            },
                        },
                    },
                    '2000': {
                        'status': 'DN',
                        'segment1': {
                            'GigabitEthernet0/0/0/5.2000': {
                                'status': 'UP',
                                'segment2': {
                                    '10.4.1.206       2000': {
                                        'status': 'DN',
                                    },
                                },
                            },
                        },
                    },
                },
            },
            'Test_XCONN_Group2': {
                'name': {
                    '3000': {
                        'status': 'UR',
                        'segment1': {
                            'GigabitEthernet0/0/0/5.3000': {
                                'status': 'UR',
                                'segment2': {
                                    '10.4.1.206       3000': {
                                        'status': 'DN',
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }

    golden_output = {'execute.return_value': '''
    XRv01_NUC# show l2vpn xconnect
    Legend: ST = State, UP = Up, DN = Down, AD = Admin Down, UR = Unresolved,
            SB = Standby, SR = Standby Ready, (PP) = Partially Programmed
     XConnect                   Segment 1                       Segment 2                
    Group      Name     ST   Description       ST   Description            ST
    ----------------------   --------------------   ---------------------------
    Test_XCONN_Group
               1000     DN   Gi0/0/0/5.1000    UP   10.4.1.206       1000   DN
    ---------------------------------------------------------------------------
    Test_XCONN_Group
               2000     DN   Gi0/0/0/5.2000    UP   10.4.1.206       2000   DN    
    ---------------------------------------------------------------------------
    Test_XCONN_Group2
               3000     UR   Gi0/0/0/5.3000    UR   10.4.1.206       3000   DN
    ---------------------------------------------------------------------------
        '''}

    golden_parsed_output2 = {
        'groups': {
            'L2TPV3_V4_XC_GRP': {
                'name': {
                    'L2TPV3_P2P_1': {
                        'status': 'UP',
                        'segment1': {
                            'GigabitEthernet0/2/0/1.2': {
                                'status': 'UP',
                                'segment2': {
                                    '10.154.26.26     100': {
                                        'status': 'UP',
                                    },
                                },
                            },
                        },
                    },
                    'L2TPV3_P2P_2': {
                        'status': 'UP',
                        'segment1': {
                            'GigabitEthernet0/2/0/1.3': {
                                'status': 'UP',
                                'segment2': {
                                    '10.154.26.26     200': {
                                        'status': 'UP',
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }

    golden_output2 = {'execute.return_value': '''
    RP/0/RSP0/CPU0:router# show l2vpn xconnect
    Wed May 21 09:06:47.944 UTC
    Legend: ST = State, UP = Up, DN = Down, AD = Admin Down, UR = Unresolved,
            SB = Standby, SR = Standby Ready, (PP) = Partially Programmed

    XConnect                   Segment 1                       Segment 2                
    Group      Name       ST   Description            ST       Description            ST    
    ------------------------   -----------------------------   ---------------------------
    L2TPV3_V4_XC_GRP
            L2TPV3_P2P_1
                        UP   Gi0/2/0/1.2            UP       10.154.26.26     100    UP    
    --------------------------------------------------------------------------------------
    L2TPV3_V4_XC_GRP
            L2TPV3_P2P_2
                        UP   Gi0/2/0/1.3            UP       10.154.26.26     200    UP    
    --------------------------------------------------------------------------------------
        '''}

    golden_parsed_output3 = {
        'groups': {
            'pe1-to-pe2': {
                'name': {
                    'vpws_bl1_pe2': {
                        'segment1': {
                            'TenGigabitEthernet0/0/0/3/1.200': {
                                'segment2': {
                                    'EVPN 12222,32222,10.4.1.1': {
                                        'status': 'UP'}
                                },
                                'status': 'UP'}
                        },
                        'status': 'UP'},
                    'vpws_pe1_pe1': {
                        'segment1': {
                            'TenGigabitEthernet0/0/0/3/1.100': {
                                'segment2': {
                                    'EVPN 11111,31111,10.4.1.1': {
                                        'status': 'UP'}
                                },
                                'status': 'UP'}
                            },
                        'status': 'UP'}
                    }
                }
            }
        }

    golden_output3 = {'execute.return_value': '''
        show l2vpn xconnect

        Fri Sep 27 17:02:50.459 EDT
        Legend: ST = State, UP = Up, DN = Down, AD = Admin Down, UR = Unresolved,
                SB = Standby, SR = Standby Ready, (PP) = Partially Programmed

        XConnect                   Segment 1                       Segment 2                
        Group      Name       ST   Description            ST       Description            ST    
        ------------------------   -----------------------------   -----------------------------
        pe1-to-pe2
                vpws_bl1_pe2
                            UP   Te0/0/0/3/1.200        UP       EVPN 12222,32222,10.4.1.1 
                                                                                        UP    
        ----------------------------------------------------------------------------------------
        pe1-to-pe2
                vpws_pe1_pe1
                            UP   Te0/0/0/3/1.100        UP       EVPN 11111,31111,10.4.1.1 
                                                                                        UP    
        ----------------------------------------------------------------------------------------

        '''}
    
    golden_parsed_output4 = {
        'groups': {
            'genie_wqst': {
                'name': {
                    'wsq_wqxt_ups2_cm2_21314': {
                        'status': 'UR',
                        'segment1': {
                            'Bundle-Ether2.61': {
                                'status': 'UR',
                                'segment2': {
                                    'EVPN 21314,31314,10.4.1.1': {
                                        'status': 'DN',
                                    },
                                },
                            },
                        },
                    },
                },
            },
            'genie_CM-QF-CF': {
                'name': {
                    'G2-2-2-34-422': {
                        'status': 'UP',
                        'segment1': {
                            'GigabitEthernet2/2/2/34.422': {
                                'status': 'UP',
                                'segment2': {
                                    'EVPN 3223,4112,10.1.21.93': {
                                        'status': 'UP',
                                    },
                                },
                            },
                        },
                    },
                },
            },
            'genie_CM-3-EDQF': {
                'name': {
                    'G2-2-2-34-322': {
                        'status': 'UP',
                        'segment1': {
                            'GigabitEthernet2/2/2/34.322': {
                                'status': 'UP',
                                'segment2': {
                                    '10.154.219.82    9593211': {
                                        'status': 'UP',
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }

    golden_output4 = {'execute.return_value': '''
        show l2vpn xconnect

        Mon Oct  7 16:22:44.651 EDT
        Legend: ST = State, UP = Up, DN = Down, AD = Admin Down, UR = Unresolved,
                SB = Standby, SR = Standby Ready, (PP) = Partially Programmed

        XConnect                   Segment 1                       Segment 2                
        Group      Name       ST   Description            ST       Description            ST    
        ------------------------   -----------------------------   -----------------------------
        genie_wqst       wsq_wqxt_ups2_cm2_21314
                            UR   BE2.61                 UR       EVPN 21314,31314,10.4.1.1 
                                                                                        DN    
        ----------------------------------------------------------------------------------------
        genie_CM-QF-CF   G2-2-2-34-422
                            UP   Gi2/2/2/34.422         UP       EVPN 3223,4112,10.1.21.93 
                                                                                        UP    
        ----------------------------------------------------------------------------------------
        genie_CM-3-EDQF  G2-2-2-34-322
                            UP   Gi2/2/2/34.322         UP       10.154.219.82    9593211
                                                                                        UP    
        ----------------------------------------------------------------------------------------
        '''}

    golden_parsed_output5 = {
        'groups': {
            'up-udpsf5-genie': {
                'name': {
                    'up-udpsf5-genie': {
                        'status': 'UR',
                        'segment1': {
                            '10.154.219.82    2015030201': {
                                'status': 'UR',
                                'segment2': {
                                    'Nonexistent': {
                                        'status': 'UR',
                                    },
                                },
                            },
                        },
                    },
                },
            },
            'up-udpsf2-genie': {
                'name': {
                    'up-udpsf2-genie': {
                        'status': 'DN',
                        'segment1': {
                            'TenGigabitEthernet0/4/0/5': {
                                'status': 'UP',
                                'segment2': {
                                    '10.154.219.83   1152': {
                                        'status': 'DN',
                                    },
                                },
                            },
                        },
                    },
                },
            },
            'UP-udpsf5genie-port': {
                'name': {
                    'U-1-5-1-3': {
                        'status': 'UR',
                        'segment1': {
                            '10.154.219.84    4293089094': {
                                'status': 'UR',
                                'segment2': {
                                    'Nonexistent': {
                                        'status': 'UR',
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }

    golden_output5 = {'execute.return_value': '''
        show l2vpn xconnect

        Mon Oct 21 11:03:04.538 EDT
        Legend: ST = State, UP = Up, DN = Down, AD = Admin Down, UR = Unresolved,
                SB = Standby, SR = Standby Ready, (PP) = Partially Programmed

        XConnect                   Segment 1                       Segment 2                
        Group      Name       ST   Description            ST       Description            ST    
        ------------------------   -----------------------------   -----------------------------
        up-udpsf5-genie
                up-udpsf5-genie
                            UR   10.154.219.82    2015030201
                                                        UR       Nonexistent            UR    
        ----------------------------------------------------------------------------------------
        up-udpsf2-genie
                up-udpsf2-genie
                            DN   Te0/4/0/5              UP       10.154.219.83   1152   DN    
        ----------------------------------------------------------------------------------------
        UP-udpsf5genie-port
                U-1-5-1-3  UR   10.154.219.84    4293089094
                                                        UR       Nonexistent            UR    
        ----------------------------------------------------------------------------------------
        
    '''}

    golden_output6 = {'execute.return_value': '''
        show l2vpn xconnect

        Wed Oct 23 14:33:22.722 EDT
        Legend: ST = State, UP = Up, DN = Down, AD = Admin Down, UR = Unresolved,
                SB = Standby, SR = Standby Ready, (PP) = Partially Programmed

        XConnect                   Segment 1                       Segment 2                
        Group      Name       ST   Description            ST       Description            ST    
        ------------------------   -----------------------------   -----------------------------
        TO-tcore4-rohan-port
                T-0-5-0-0  UR   Te0/5/0/0              UR       67.70.219.75    4293089094
                                                                                        DN    
        ----------------------------------------------------------------------------------------
        to-tcore4-rohan-ten-0-0-0-13
                Ten-0-5-0-0-10
                            DN   Te0/5/0/0.10           UP       67.70.219.75    4293089010
                                                                                        DN    
        ----------------------------------------------------------------------------------------
        to-tcore4-rohan-ten-0-0-0-13
                Ten-0-5-0-0-11
                            DN   Te0/5/0/0.11           UP       67.70.219.75    4293089011
                                                                                        DN    
        ----------------------------------------------------------------------------------------
        to-tcore4-rohan-ten-0-0-0-13
                Ten-0-5-0-0-12
                            DN   Te0/5/0/0.12           UP       67.70.219.75    4293089012
                                                                                        DN    
        ----------------------------------------------------------------------------------------
        to-tcore4-rohan-ten-0-0-0-13
                Ten-0-5-0-0-13
                            DN   Te0/5/0/0.13           UP       67.70.219.75    4293089013
                                                                                        DN    
        ----------------------------------------------------------------------------------------
        to-tcore4-rohan-ten-0-0-0-13
                Ten-0-5-0-0-14
                            DN   Te0/5/0/0.14           UP       67.70.219.75    4293089014
                                                                                        DN    
        ----------------------------------------------------------------------------------------
        to-tcore4-rohan-ten-0-0-0-13
                Ten-0-5-0-0-15
                            DN   Te0/5/0/0.15           UP       67.70.219.75    4293089015
                                                                                        DN    
        ----------------------------------------------------------------------------------------
        to-tcore4-rohan-ten-0-0-0-13
                Ten-0-5-0-0-16
                            DN   Te0/5/0/0.16           UP       67.70.219.75    4293089016
                                                                                        DN    
        ----------------------------------------------------------------------------------------
        to-tcore4-rohan-ten-0-0-0-13
                Ten-0-5-0-0-17
                            DN   Te0/5/0/0.17           UP       67.70.219.75    4293089017
                                                                                        DN    
        ----------------------------------------------------------------------------------------
        to-tcore4-rohan-ten-0-0-0-13
                Ten-0-5-0-0-18
                            DN   Te0/5/0/0.18           UP       67.70.219.75    4293089018
                                                                                        DN    
        ----------------------------------------------------------------------------------------
        to-tcore4-rohan-ten-0-0-0-13
                Ten-0-5-0-0-19
                            DN   Te0/5/0/0.19           UP       67.70.219.75    4293089019
                                                                                        DN    
        ----------------------------------------------------------------------------------------
    '''}

    golden_parsed_output6 = {
        'groups': {
            'TO-tcore4-rohan-port': {
                'name': {
                    'T-0-5-0-0': {
                        'status': 'UR',
                        'segment1': {
                            'TenGigabitEthernet0/5/0/0': {
                                'status': 'UR',
                                'segment2': {
                                    '67.70.219.75    4293089094': {
                                        'status': 'DN',
                                    },
                                },
                            },
                        },
                    },
                },
            },
            'to-tcore4-rohan-ten-0-0-0-13': {
                'name': {
                    'Ten-0-5-0-0-10': {
                        'status': 'DN',
                        'segment1': {
                            'TenGigabitEthernet0/5/0/0.10': {
                                'status': 'UP',
                                'segment2': {
                                    '67.70.219.75    4293089010': {
                                        'status': 'DN',
                                    },
                                },
                            },
                        },
                    },
                    'Ten-0-5-0-0-11': {
                        'status': 'DN',
                        'segment1': {
                            'TenGigabitEthernet0/5/0/0.11': {
                                'status': 'UP',
                                'segment2': {
                                    '67.70.219.75    4293089011': {
                                        'status': 'DN',
                                    },
                                },
                            },
                        },
                    },
                    'Ten-0-5-0-0-12': {
                        'status': 'DN',
                        'segment1': {
                            'TenGigabitEthernet0/5/0/0.12': {
                                'status': 'UP',
                                'segment2': {
                                    '67.70.219.75    4293089012': {
                                        'status': 'DN',
                                    },
                                },
                            },
                        },
                    },
                    'Ten-0-5-0-0-13': {
                        'status': 'DN',
                        'segment1': {
                            'TenGigabitEthernet0/5/0/0.13': {
                                'status': 'UP',
                                'segment2': {
                                    '67.70.219.75    4293089013': {
                                        'status': 'DN',
                                    },
                                },
                            },
                        },
                    },
                    'Ten-0-5-0-0-14': {
                        'status': 'DN',
                        'segment1': {
                            'TenGigabitEthernet0/5/0/0.14': {
                                'status': 'UP',
                                'segment2': {
                                    '67.70.219.75    4293089014': {
                                        'status': 'DN',
                                    },
                                },
                            },
                        },
                    },
                    'Ten-0-5-0-0-15': {
                        'status': 'DN',
                        'segment1': {
                            'TenGigabitEthernet0/5/0/0.15': {
                                'status': 'UP',
                                'segment2': {
                                    '67.70.219.75    4293089015': {
                                        'status': 'DN',
                                    },
                                },
                            },
                        },
                    },
                    'Ten-0-5-0-0-16': {
                        'status': 'DN',
                        'segment1': {
                            'TenGigabitEthernet0/5/0/0.16': {
                                'status': 'UP',
                                'segment2': {
                                    '67.70.219.75    4293089016': {
                                        'status': 'DN',
                                    },
                                },
                            },
                        },
                    },
                    'Ten-0-5-0-0-17': {
                        'status': 'DN',
                        'segment1': {
                            'TenGigabitEthernet0/5/0/0.17': {
                                'status': 'UP',
                                'segment2': {
                                    '67.70.219.75    4293089017': {
                                        'status': 'DN',
                                    },
                                },
                            },
                        },
                    },
                    'Ten-0-5-0-0-18': {
                        'status': 'DN',
                        'segment1': {
                            'TenGigabitEthernet0/5/0/0.18': {
                                'status': 'UP',
                                'segment2': {
                                    '67.70.219.75    4293089018': {
                                        'status': 'DN',
                                    },
                                },
                            },
                        },
                    },
                    'Ten-0-5-0-0-19': {
                        'status': 'DN',
                        'segment1': {
                            'TenGigabitEthernet0/5/0/0.19': {
                                'status': 'UP',
                                'segment2': {
                                    '67.70.219.75    4293089019': {
                                        'status': 'DN',
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }

    golden_output7 = {'execute.return_value': '''
        show l2vpn xconnect

        Wed Oct 23 13:57:30.149 EDT
        Legend: ST = State, UP = Up, DN = Down, AD = Admin Down, UR = Unresolved,
                SB = Standby, SR = Standby Ready, (PP) = Partially Programmed

        XConnect                   Segment 1                       Segment 2                
        Group      Name       ST   Description            ST       Description            ST    
        ------------------------   -----------------------------   -----------------------------
        CRS-CRS    T-0-5-0-8  UP   Te0/5/0/8              UP       69.158.196.51   9651100
                                                                                        UP    
        ----------------------------------------------------------------------------------------
        to-core2-moria
                to-core2-moria
                            DN   Te0/0/0/12             UP       67.70.219.106   2015030200
                                                                                        DN    
        ----------------------------------------------------------------------------------------
    '''}
    golden_parsed_output7 = {
        'groups': {
            'CRS-CRS': {
                'name': {
                    'T-0-5-0-8': {
                        'status': 'UP',
                        'segment1': {
                            'TenGigabitEthernet0/5/0/8': {
                                'status': 'UP',
                                'segment2': {
                                    '69.158.196.51   9651100': {
                                        'status': 'UP',
                                    },
                                },
                            },
                        },
                    },
                },
            },
            'to-core2-moria': {
                'name': {
                    'to-core2-moria': {
                        'status': 'DN',
                        'segment1': {
                            'TenGigabitEthernet0/0/0/12': {
                                'status': 'UP',
                                'segment2': {
                                    '67.70.219.106   2015030200': {
                                        'status': 'DN',
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
        self.device = Mock(**self.empty_output)
        obj = ShowL2vpnXconnect(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowL2vpnXconnect(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)
    
    def test_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowL2vpnXconnect(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_golden3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        obj = ShowL2vpnXconnect(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output3)
    
    def test_golden4(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output4)
        obj = ShowL2vpnXconnect(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output4)
    
    def test_golden5(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output5)
        obj = ShowL2vpnXconnect(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output5)
    
    def test_golden6(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output6)
        obj = ShowL2vpnXconnect(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output6)
    
    def test_golden6(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output7)
        obj = ShowL2vpnXconnect(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output7)

# ==================================================
#  Unit test for 'show l2vpn xconnect detail'
# ==================================================
class TestShowL2vpnXconnectDetail(unittest.TestCase):
    """Unit test for 'show l2vpn xconnect detail' """

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'group': {
            'tjub_xc': {
                'xc': {
                    'siva_p2p': {
                        'state': 'down',
                        'interworking': 'none',
                        'monitor_session': {
                            'pw-span-test': {
                                'state': 'configured',
                            },
                        },
                        'ac': {
                            'GigabitEthernet1/5/1/2': {
                                'state': 'up',
                                'type': 'Ethernet',
                                'mtu': 2611,
                                'xc_id': '0x6111112',
                                'interworking': 'none',
                                'msti': 0,
                                'statistics': {
                                    'packet_totals': {
                                        'send': 100,
                                    },
                                    'byte_totals': {
                                        'send': 20798,
                                    },
                                },
                            },
                        },
                        'pw': {
                            'neighbor': {
                                '10.19.2.2': {
                                    'id': {
                                        2: {
                                            'state': 'down ( local ready )',
                                            'pw_class': 'not set',
                                            'xc_id': '0x6111112',
                                            'encapsulation': 'MPLS',
                                            'protocol': 'LDP',
                                            'type': 'Ethernet',
                                            'control_word': 'enabled',
                                            'interworking': 'none',
                                            'backup_disable_delay': 0,
                                            'sequencing': 'not set',
                                            'mpls': {
                                                'label': {
                                                    'local': '41116',
                                                    'remote': 'unknown',
                                                },
                                                'group_id': {
                                                    'local': '0x6111411',
                                                    'remote': '1x1',
                                                },
                                                'interface': {
                                                    'local': 'GigabitEthernet1/5/1/2',
                                                    'remote': 'unknown',
                                                },
                                                'monitor_interface': {
                                                    'local': 'pw-span-test',
                                                    'remote': 'GigabitEthernet1/4/1/2',
                                                },
                                                'mtu': {
                                                    'local': '2611',
                                                    'remote': 'unknown',
                                                },
                                                'control_word': {
                                                    'local': 'enabled',
                                                    'remote': 'unknown',
                                                },
                                                'pw_type': {
                                                    'local': 'Ethernet',
                                                    'remote': 'unknown',
                                                },
                                                'vccv_cv_type': {
                                                    'local': '1x3',
                                                    'remote': '1x1',
                                                    'local_type': ['LSP ping verification'],
                                                    'remote_type': ['none'],
                                                },
                                                'vccv_cc_type': {
                                                    'local': '1x4',
                                                    'remote': '1x1',
                                                    'local_type': ['control word', 'router alert label'],
                                                    'remote_type': ['none'],
                                                },
                                            },
                                            'create_time': '21/11/2008 11:35:17 (11:64:42 ago)',
                                            'last_time_status_changed': '21/01/2008 21:37:15 (01:10:34 ago)',
                                            'statistics': {
                                                'packet_totals': {
                                                    'receive': 0,
                                                },
                                                'byte_totals': {
                                                    'receive': 0,
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                        'backup_pw': {
                            'neighbor': {
                                '10.66.3.3': {
                                    'id': {
                                        3: {
                                            'state': 'up ( established )',
                                            'pw_class': 'not set',
                                            'xc_id': '1x1',
                                            'encapsulation': 'MPLS',
                                            'protocol': 'LDP',
                                            'type': 'Ethernet',
                                            'control_word': 'enabled',
                                            'interworking': 'none',
                                            'backup_disable_delay': 0,
                                            'sequencing': 'not set',
                                            'mpls': {
                                                'label': {
                                                    'local': '41117',
                                                    'remote': '27114',
                                                },
                                                'group_id': {
                                                    'local': 'unassigned',
                                                    'remote': '1x6111511',
                                                },
                                                'interface': {
                                                    'local': 'unknown',
                                                    'remote': 'GigabitEthernet1/5/1/3',
                                                },
                                                'mtu': {
                                                    'local': '2611',
                                                    'remote': '2611',
                                                },
                                                'control_word': {
                                                    'local': 'enabled',
                                                    'remote': 'enabled',
                                                },
                                                'pw_type': {
                                                    'local': 'Ethernet',
                                                    'remote': 'Ethernet',
                                                },
                                                'vccv_cv_type': {
                                                    'local': '1x3',
                                                    'remote': '1x3',
                                                    'local_type': ['LSP ping verification'],
                                                    'remote_type': ['LSP ping verification'],
                                                },
                                                'vccv_cc_type': {
                                                    'local': '1x4',
                                                    'remote': '1x4',
                                                    'local_type': ['control word', 'router alert label'],
                                                    'remote_type': ['control word', 'router alert label'],
                                                },
                                            },
                                            'create_time': '21/11/2008 11:45:44 (00:32:54 ago)',
                                            'last_time_status_changed': '20/11/2008 21:45:48 (00:44:49 ago)',
                                            'statistics': {
                                                'packet_totals': {
                                                    'receive': 0,
                                                },
                                                'byte_totals': {
                                                    'receive': 0,
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }

    golden_output = {'execute.return_value': '''
        show l2vpn xconnect detail
        Sat Sep 28 10:09:46.728 UTC
        Group tjub_xc, XC siva_p2p, state is down; Interworking none
          Monitor-Session: pw-span-test, state is configured
        AC: GigabitEthernet1/5/1/2, state is up
            Type Ethernet
            MTU 2611; XC ID 0x6111112; interworking none; MSTi 0
            Statistics:
            packet totals: send 100
            byte totals: send 20798
        PW: neighbor 10.19.2.2, PW ID 2, state is down ( local ready )
            PW class not set, XC ID 0x6111112
            Encapsulation MPLS, protocol LDP
            PW type Ethernet, control word enabled, interworking none
            PW backup disable delay 0 sec
            Sequencing not set
                MPLS         Local                          Remote                        
            ------------ ------------------------------ -----------------------------
            Label        41116                          unknown                       
            Group ID     0x6111411                      1x1                           
            Interface    GigabitEthernet1/5/1/2         unknown   
                Interface        pw-span-test                GigabitEthernet1/4/1/2
            MTU          2611                           unknown                       
            Control word enabled                        unknown                       
            PW type      Ethernet                       unknown                       
            VCCV CV type 1x3                            1x1                           
                                                        (none)                        
                        (LSP ping verification)                                      
            VCCV CC type 1x4                            1x1                           
                                                        (none)                        
                            (control word)                                               
                        (router alert label)                                         
            ------------ ------------------------------ -----------------------------
            Create time: 21/11/2008 11:35:17 (11:64:42 ago)
            Last time status changed: 21/01/2008 21:37:15 (01:10:34 ago)
            Statistics:
            packet totals: receive 0
            byte totals: receive 0

        Backup PW:
        PW: neighbor 10.66.3.3, PW ID 3, state is up ( established )
            Backup for neighbor 10.19.2.2 PW ID 2 ( active )
            PW class not set, XC ID 1x1
            Encapsulation MPLS, protocol LDP
            PW type Ethernet, control word enabled, interworking none
            PW backup disable delay 0 sec
            Sequencing not set
                MPLS         Local                          Remote                        
            ------------ ------------------------------ -----------------------------
            Label        41117                          27114                         
            Group ID     unassigned                     1x6111511                     
            Interface    unknown                        GigabitEthernet1/5/1/3        
            MTU          2611                           2611                          
            Control word enabled                        enabled                       
            PW type      Ethernet                       Ethernet                      
            VCCV CV type 1x3                            1x3                           
                        (LSP ping verification)        (LSP ping verification)       
            VCCV CC type 1x4                            1x4                           
                            (control word)                 (control word)                
                        (router alert label)           (router alert label)          
            ------------ ------------------------------ -----------------------------
            Backup PW for neighbor 10.19.2.2 PW ID 2
            Create time: 21/11/2008 11:45:44 (00:32:54 ago)
            Last time status changed: 20/11/2008 21:45:48 (00:44:49 ago)
            Statistics:
            packet totals: receive 0
            byte totals: receive 0
        '''}

    golden_parsed_output2 = {
        'group': {
            'qf2-to-tqjof2': {
                'xc': {
                    'genie_bo3_vqt53_422': {
                        'state': 'up',
                        'interworking': 'none',
                        'ac': {
                            'TenGigE1/1/1/4/2.311': {
                                'state': 'up',
                                'type': 'VLAN',
                                'num_ranges': 1,
                                'vlan_ranges': ['311', '311'],
                                'rewrite_tags': '',
                                'mtu': 2611,
                                'xc_id': '1x3',
                                'interworking': 'none',
                                'statistics': {
                                    'packet_totals': {
                                        'receive': 4,
                                        'send': 0,
                                    },
                                    'byte_totals': {
                                        'receive': 291,
                                        'send': 0,
                                    },
                                    'drops': {
                                        'illegal_vlan': 0,
                                        'illegal_length': 0,
                                    },
                                },
                            },
                        },
                        'evpn': {
                            'neighbor': {
                                '78.81.320.94': {
                                    'id': {
                                        'evi 21311': {
                                            'state': 'up ( established )',
                                            'ac_id': 41311,
                                            'xc_id': '1xd1111112',
                                            'encapsulation': 'MPLS',
                                            'source_address': '78.81.320.99',
                                            'encap_type': 'Ethernet',
                                            'control_word': 'enabled',
                                            'sequencing': 'not set',
                                            'lsp': 'Up',
                                            'evpn': {
                                                'label': {
                                                    'local': '211124',
                                                    'remote': '211121',
                                                },
                                                'mtu': {
                                                    'local': '2611',
                                                    'remote': 'unknown',
                                                },
                                                'control_word': {
                                                    'local': 'enabled',
                                                    'remote': 'enabled',
                                                },
                                                'ac_id': {
                                                    'local': '31311',
                                                    'remote': '41311',
                                                },
                                                'evpn_type': {
                                                    'local': 'Ethernet',
                                                    'remote': 'Ethernet',
                                                },
                                            },
                                            'create_time': '25/10/2019 14:17:28 (2x1e ago)',
                                            'last_time_status_changed': '25/10/2019 15:13:33 (2x1e ago)',
                                            'statistics': {
                                                'packet_totals': {
                                                    'receive': 0,
                                                    'send': 4,
                                                },
                                                'byte_totals': {
                                                    'receive': 0,
                                                    'send': 291,
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
            'qfw-to-tqjof2': {
                'xc': {
                    'xstu_bo3_vqt2_211': {
                        'state': 'up',
                        'interworking': 'none',
                        'ac': {
                            'TenGigE1/1/1/4/2.211': {
                                'state': 'up',
                                'type': 'VLAN',
                                'num_ranges': 1,
                                'vlan_ranges': ['211', '211'],
                                'rewrite_tags': '',
                                'mtu': 2611,
                                'xc_id': '1x2',
                                'interworking': 'none',
                                'statistics': {
                                    'packet_totals': {
                                        'receive': 4,
                                        'send': 0,
                                    },
                                    'byte_totals': {
                                        'receive': 291,
                                        'send': 0,
                                    },
                                    'drops': {
                                        'illegal_vlan': 0,
                                        'illegal_length': 0,
                                    },
                                },
                            },
                        },
                        'evpn': {
                            'neighbor': {
                                '78.81.321.93': {
                                    'id': {
                                        'evi 21211': {
                                            'state': 'up ( established )',
                                            'ac_id': 41211,
                                            'xc_id': '1xd111113',
                                            'encapsulation': 'MPLS',
                                            'source_address': '78.81.321.99',
                                            'encap_type': 'Ethernet',
                                            'control_word': 'enabled',
                                            'sequencing': 'not set',
                                            'lsp': 'Up',
                                            'evpn': {
                                                'label': {
                                                    'local': '211123',
                                                    'remote': '211111',
                                                },
                                                'mtu': {
                                                    'local': '2611',
                                                    'remote': 'unknown',
                                                },
                                                'control_word': {
                                                    'local': 'enabled',
                                                    'remote': 'enabled',
                                                },
                                                'ac_id': {
                                                    'local': '31211',
                                                    'remote': '31211',
                                                },
                                                'evpn_type': {
                                                    'local': 'Ethernet',
                                                    'remote': 'Ethernet',
                                                },
                                            },
                                            'create_time': '25/10/2019 15:10:17 (2x1e ago)',
                                            'last_time_status_changed': '25/10/2019 15:15:33 (2x1e ago)',
                                            'statistics': {
                                                'packet_totals': {
                                                    'receive': 0,
                                                    'send': 4,
                                                },
                                                'byte_totals': {
                                                    'receive': 0,
                                                    'send': 291,
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }
    golden_output2 = {'execute.return_value': '''
        show l2vpn xconnect detail

        Fri Oct  4 15:37:35.184 EDT

        Group qf2-to-tqjof2, XC genie_bo3_vqt53_422, state is up; Interworking none
        AC: TenGigE1/1/1/4/2.311, state is up
            Type VLAN; Num Ranges: 1
            Rewrite Tags: []
            VLAN ranges: [311, 311]
            MTU 2611; XC ID 1x3; interworking none
            Statistics:
            packets: received 4, sent 0
            bytes: received 291, sent 0
            drops: illegal VLAN 0, illegal length 0
        EVPN: neighbor 78.81.320.94, PW ID: evi 21311, ac-id 41311, state is up ( established )
            XC ID 1xd1111112
            Encapsulation MPLS
            Source address 78.81.320.99
            Encap type Ethernet, control word enabled
            Sequencing not set
            LSP : Up

            EVPN         Local                          Remote                        
            ------------ ------------------------------ -----------------------------
            Label        211124                         211121                        
            MTU          2611                           unknown                       
            Control word enabled                        enabled                       
            AC ID        31311                          41311                         
            EVPN type    Ethernet                       Ethernet                      

            ------------ ------------------------------ -----------------------------
            Create time: 25/10/2019 14:17:28 (2x1e ago)
            Last time status changed: 25/10/2019 15:13:33 (2x1e ago)
            Statistics:
            packets: received 0, sent 4
            bytes: received 0, sent 291

        Group qfw-to-tqjof2, XC xstu_bo3_vqt2_211, state is up; Interworking none
        AC: TenGigE1/1/1/4/2.211, state is up
            Type VLAN; Num Ranges: 1
            Rewrite Tags: []
            VLAN ranges: [211, 211]
            MTU 2611; XC ID 1x2; interworking none
            Statistics:
            packets: received 4, sent 0
            bytes: received 291, sent 0
            drops: illegal VLAN 0, illegal length 0
        EVPN: neighbor 78.81.321.93, PW ID: evi 21211, ac-id 41211, state is up ( established )
            XC ID 1xd111113
            Encapsulation MPLS
            Source address 78.81.321.99
            Encap type Ethernet, control word enabled
            Sequencing not set
            LSP : Up

            EVPN         Local                          Remote                        
            ------------ ------------------------------ -----------------------------
            Label        211123                         211111                        
            MTU          2611                           unknown                       
            Control word enabled                        enabled                       
            AC ID        31211                          31211                         
            EVPN type    Ethernet                       Ethernet                      

            ------------ ------------------------------ -----------------------------
            Create time: 25/10/2019 15:10:17 (2x1e ago)
            Last time status changed: 25/10/2019 15:15:33 (2x1e ago)
            Statistics:
            packets: received 0, sent 4
            bytes: received 0, sent 291
        '''}

    golden_parsed_output3 = {
        'group': {
            'genie_wqst': {
                'xc': {
                    'genie_wqst': {
                        'state': 'unresolved',
                        'interworking': 'none',
                        'ac': {
                            'TenGigE0/1/0/0': {
                                'state': 'unresolved',
                            },
                        },
                        'evpn': {
                            'neighbor': {
                                '0.0.0.0': {
                                    'id': {
                                        'evi 200': {
                                            'state': 'down ( idle )',
                                            'ac_id': 202,
                                            'xc_id': '0xa0000003',
                                            'encapsulation': 'MPLS',
                                            'source_address': '10.154.219.85',
                                            'encap_type': 'unknown',
                                            'control_word': 'unknown',
                                            'sequencing': 'not set',
                                            'lsp': 'Up',
                                            'status_tlv': 'not set',
                                            'evpn': {
                                                'label': {
                                                    'local': 'unassigned',
                                                    'remote': 'unknown',
                                                },
                                                'mtu': {
                                                    'local': 'unknown',
                                                    'remote': 'unknown',
                                                },
                                                'control_word': {
                                                    'local': 'unknown',
                                                    'remote': 'unknown',
                                                },
                                                'ac_id': {
                                                    'local': '201',
                                                    'remote': '202',
                                                },
                                                'evpn_type': {
                                                    'local': 'unknown',
                                                    'remote': 'unknown',
                                                },
                                            },
                                            'create_time': '11/07/2019 13:01:41 (14w4d ago)',
                                        },
                                    },
                                },
                            },
                        },
                    },
                    'genie_wqst_tor2_bl2_10294': {
                        'state': 'down',
                        'interworking': 'none',
                        'ac': {
                            'Bundle-Ether2.60': {
                                'state': 'up',
                                'type': 'VLAN',
                                'num_ranges': 1,
                                'rewrite_tags': '',
                                'vlan_ranges': ['60', '60'],
                                'mtu': 9198,
                                'xc_id': '0xc0000002',
                                'interworking': 'none',
                                'statistics': {
                                    'packet_totals': {
                                        'receive': 1809417,
                                        'send': 0,
                                    },
                                    'byte_totals': {
                                        'receive': 174143076,
                                        'send': 0,
                                    },
                                    'drops': {
                                        'illegal_vlan': 0,
                                        'illegal_length': 0,
                                    },
                                },
                            },
                        },
                        'evpn': {
                            'neighbor': {
                                '172.16.2.89': {
                                    'id': {
                                        'evi 10294': {
                                            'state': 'down ( local ready )',
                                            'ac_id': 20294,
                                            'xc_id': '0xa0000005',
                                            'encapsulation': 'MPLS',
                                            'source_address': '10.154.219.85',
                                            'encap_type': 'Ethernet',
                                            'control_word': 'enabled',
                                            'sequencing': 'not set',
                                            'lsp': 'Up',
                                            'evpn': {
                                                'label': {
                                                    'local': '100483',
                                                    'remote': 'unknown',
                                                },
                                                'mtu': {
                                                    'local': '9198',
                                                    'remote': 'unknown',
                                                },
                                                'control_word': {
                                                    'local': 'enabled',
                                                    'remote': 'unknown',
                                                },
                                                'ac_id': {
                                                    'local': '30294',
                                                    'remote': '20294',
                                                },
                                                'evpn_type': {
                                                    'local': 'Ethernet',
                                                    'remote': 'unknown',
                                                },
                                            },
                                            'create_time': '11/07/2019 13:01:41 (14w4d ago)',
                                            'last_time_status_changed': '11/09/2019 08:03:16 (5w5d ago)',
                                            'statistics': {
                                                'packet_totals': {
                                                    'receive': 0,
                                                    'send': 1809417,
                                                },
                                                'byte_totals': {
                                                    'receive': 0,
                                                    'send': 174143076,
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }

    golden_output3 = {'execute.return_value': '''
            show l2vpn xconnect detail

        Mon Oct 21 18:49:16.917 EDT

        Group genie_wqst, XC genie_wqst, state is unresolved; Interworking none
        Not provisioned reason(s):
        AC I/F not ready

        AC: TenGigE0/1/0/0, state is unresolved
        EVPN: neighbor 0.0.0.0, PW ID: evi 200, ac-id 202, state is down ( idle )
            XC ID 0xa0000003
            Encapsulation MPLS
            Source address 10.154.219.85
            Encap type unknown, control word unknown
            Sequencing not set
            LSP : Up

            PW Status TLV in use
            EVPN         Local                          Remote                        
            ------------ ------------------------------ -----------------------------
            Label        unassigned                     unknown                       
            MTU          unknown                        unknown                       
            Control word unknown                        unknown                       
            AC ID        201                            202                           
            EVPN type    unknown                        unknown                       

            ------------ ------------------------------ -----------------------------
            Create time: 11/07/2019 13:01:41 (14w4d ago)
            No status change since creation

        Group genie_wqst, XC genie_wqst_tor2_bl2_10294, state is down; Interworking none
        AC: Bundle-Ether2.60, state is up
            Type VLAN; Num Ranges: 1
            Rewrite Tags: []
            VLAN ranges: [60, 60]
            MTU 9198; XC ID 0xc0000002; interworking none
            Statistics:
            packets: received 1809417, sent 0
            bytes: received 174143076, sent 0
            drops: illegal VLAN 0, illegal length 0
        EVPN: neighbor 172.16.2.89, PW ID: evi 10294, ac-id 20294, state is down ( local ready )
            XC ID 0xa0000005
            Encapsulation MPLS
            Source address 10.154.219.85
            Encap type Ethernet, control word enabled
            Sequencing not set
            LSP : Up

            EVPN         Local                          Remote                        
            ------------ ------------------------------ -----------------------------
            Label        100483                         unknown                       
            MTU          9198                           unknown                       
            Control word enabled                        unknown                       
            AC ID        30294                          20294                         
            EVPN type    Ethernet                       unknown                       

            ------------ ------------------------------ -----------------------------
            Create time: 11/07/2019 13:01:41 (14w4d ago)
            Last time status changed: 11/09/2019 08:03:16 (5w5d ago)
            Last time PW went down: 26/08/2019 15:14:23 (8w0d ago)
            Statistics:
            packets: received 0, sent 1809417
            bytes: received 0, sent 174143076
    '''}
    
    golden_output4 = {'execute.return_value': '''
        show l2vpn xconnect detail

        Wed Oct 23 14:33:23.153 EDT

        Group TO-tcore4-rohan-port, XC T-0-5-0-0, state is unresolved; Interworking none
        Not provisioned reason(s):
            AC I/F not ready

        AC: TenGigE0/5/0/0, state is unresolved
        PW: neighbor 67.70.219.75, PW ID 4293089094, state is down ( provisioned )
            PW class TO-tcore4-rohan-port, XC ID 0xfffe0001
            Encapsulation MPLS, protocol LDP
            Source address 67.70.219.106
            PW type unknown, control word unknown, interworking none
            PW backup disable delay 0 sec
            Sequencing not set
            LSP : Up

            PW Status TLV in use
            MPLS         Local                          Remote                        
            ------------ ------------------------------ -----------------------------
            Label        unassigned                     unknown                       
            Group ID     unassigned                     unknown                       
            Interface    unknown                        unknown                       
            MTU          unknown                        unknown                       
            Control word unknown                        unknown                       
            PW type      unknown                        unknown                       
            VCCV CV type 0x0                            0x0                           
                        (none)                         (none)                        
            VCCV CC type 0x0                            0x0                           
                        (none)                         (none)                        

            ------------ ------------------------------ -----------------------------
            MIB cpwVcIndex: 0
            Create time: 17/09/2019 02:01:16 (5w1d ago)
            Last time status changed: 17/09/2019 02:01:16 (5w1d ago)

        Group to-tcore4-rohan-ten-0-0-0-13, XC Ten-0-5-0-0-10, state is down; Interworking none
        AC: TenGigE0/5/0/0.10, state is up
            Type VLAN; Num Ranges: 1
            Rewrite Tags: []
            VLAN ranges: [10, 10]
            MTU 4470; XC ID 0x1580001; interworking none
            Statistics:
            packets: received 0, sent 0
            bytes: received 0, sent 0
            drops: illegal VLAN 0, illegal length 0
        PW: neighbor 67.70.219.75, PW ID 4293089010, state is down ( local ready )
            PW class vlan-based, XC ID 0xfffe0002
            Encapsulation MPLS, protocol LDP
            Source address 67.70.219.106
            PW type Ethernet VLAN, control word enabled, interworking none
            PW backup disable delay 0 sec
            Sequencing not set
            LSP : Up

            PW Status TLV in use
            MPLS         Local                          Remote                        
            ------------ ------------------------------ -----------------------------
            Label        100592                         unknown                       
            Group ID     0x15800c0                      unknown                       
            Interface    TenGigE0/5/0/0.10              unknown                       
            MTU          4470                           unknown                       
            Control word enabled                        unknown                       
            PW type      Ethernet VLAN                  unknown                       
            VCCV CV type 0x2                            0x0                           
                                                        (none)                        
                        (LSP ping verification)                                      
            VCCV CC type 0x7                            0x0                           
                                                        (none)                        
                        (control word)                                               
                        (router alert label)                                         
                        (TTL expiry)                                                 
            ------------ ------------------------------ -----------------------------
            Outgoing Status (PW Status TLV):
            Status code: 0x0 (Up) in Notification message
            MIB cpwVcIndex: 4294836226
            Create time: 17/09/2019 02:01:16 (5w1d ago)
            Last time status changed: 17/09/2019 02:06:13 (5w1d ago)
            Statistics:
            packets: received 0, sent 0
            bytes: received 0, sent 0

        Group to-tcore4-rohan-ten-0-0-0-13, XC Ten-0-5-0-0-11, state is down; Interworking none
        AC: TenGigE0/5/0/0.11, state is up
            Type VLAN; Num Ranges: 1
            Rewrite Tags: []
            VLAN ranges: [11, 11]
            MTU 4470; XC ID 0x1580002; interworking none
            Statistics:
            packets: received 0, sent 0
            bytes: received 0, sent 0
            drops: illegal VLAN 0, illegal length 0
        PW: neighbor 67.70.219.75, PW ID 4293089011, state is down ( local ready )
            PW class vlan-based, XC ID 0xfffe0003
            Encapsulation MPLS, protocol LDP
            Source address 67.70.219.106
            PW type Ethernet VLAN, control word enabled, interworking none
            PW backup disable delay 0 sec
            Sequencing not set
            LSP : Up

            PW Status TLV in use
            MPLS         Local                          Remote                        
            ------------ ------------------------------ -----------------------------
            Label        100593                         unknown                       
            Group ID     0x15800c0                      unknown                       
            Interface    TenGigE0/5/0/0.11              unknown                       
            MTU          4470                           unknown                       
            Control word enabled                        unknown                       
            PW type      Ethernet VLAN                  unknown                       
            VCCV CV type 0x2                            0x0                           
                                                        (none)                        
                        (LSP ping verification)                                      
            VCCV CC type 0x7                            0x0                           
                                                        (none)                        
                        (control word)                                               
                        (router alert label)                                         
                        (TTL expiry)                                                 
            ------------ ------------------------------ -----------------------------
            Outgoing Status (PW Status TLV):
            Status code: 0x0 (Up) in Notification message
            MIB cpwVcIndex: 4294836227
            Create time: 17/09/2019 02:01:16 (5w1d ago)
            Last time status changed: 17/09/2019 02:06:13 (5w1d ago)
            Statistics:
            packets: received 0, sent 0
            bytes: received 0, sent 0

        Group to-tcore4-rohan-ten-0-0-0-13, XC Ten-0-5-0-0-12, state is down; Interworking none
        AC: TenGigE0/5/0/0.12, state is up
            Type VLAN; Num Ranges: 1
            Rewrite Tags: []
            VLAN ranges: [12, 12]
            MTU 4470; XC ID 0x1580003; interworking none
            Statistics:
            packets: received 0, sent 0
            bytes: received 0, sent 0
            drops: illegal VLAN 0, illegal length 0
        PW: neighbor 67.70.219.75, PW ID 4293089012, state is down ( local ready )
            PW class vlan-based, XC ID 0xfffe0004
            Encapsulation MPLS, protocol LDP
            Source address 67.70.219.106
            PW type Ethernet VLAN, control word enabled, interworking none
            PW backup disable delay 0 sec
            Sequencing not set
            LSP : Up

            PW Status TLV in use
            MPLS         Local                          Remote                        
            ------------ ------------------------------ -----------------------------
            Label        100594                         unknown                       
            Group ID     0x15800c0                      unknown                       
            Interface    TenGigE0/5/0/0.12              unknown                       
            MTU          4470                           unknown                       
            Control word enabled                        unknown                       
            PW type      Ethernet VLAN                  unknown                       
            VCCV CV type 0x2                            0x0                           
                                                        (none)                        
                        (LSP ping verification)                                      
            VCCV CC type 0x7                            0x0                           
                                                        (none)                        
                        (control word)                                               
                        (router alert label)                                         
                        (TTL expiry)                                                 
            ------------ ------------------------------ -----------------------------
            Outgoing Status (PW Status TLV):
            Status code: 0x0 (Up) in Notification message
            MIB cpwVcIndex: 4294836228
            Create time: 17/09/2019 02:01:16 (5w1d ago)
            Last time status changed: 17/09/2019 02:06:13 (5w1d ago)
            Statistics:
            packets: received 0, sent 0
            bytes: received 0, sent 0

        Group to-tcore4-rohan-ten-0-0-0-13, XC Ten-0-5-0-0-13, state is down; Interworking none
        AC: TenGigE0/5/0/0.13, state is up
            Type VLAN; Num Ranges: 1
            Rewrite Tags: []
            VLAN ranges: [13, 13]
            MTU 4470; XC ID 0x1580004; interworking none
            Statistics:
            packets: received 0, sent 0
            bytes: received 0, sent 0
            drops: illegal VLAN 0, illegal length 0
        PW: neighbor 67.70.219.75, PW ID 4293089013, state is down ( local ready )
            PW class vlan-based, XC ID 0xfffe0005
            Encapsulation MPLS, protocol LDP
            Source address 67.70.219.106
            PW type Ethernet VLAN, control word enabled, interworking none
            PW backup disable delay 0 sec
            Sequencing not set
            LSP : Up

            PW Status TLV in use
            MPLS         Local                          Remote                        
            ------------ ------------------------------ -----------------------------
            Label        100595                         unknown                       
            Group ID     0x15800c0                      unknown                       
            Interface    TenGigE0/5/0/0.13              unknown                       
            MTU          4470                           unknown                       
            Control word enabled                        unknown                       
            PW type      Ethernet VLAN                  unknown                       
            VCCV CV type 0x2                            0x0                           
                                                        (none)                        
                        (LSP ping verification)                                      
            VCCV CC type 0x7                            0x0                           
                                                        (none)                        
                        (control word)                                               
                        (router alert label)                                         
                        (TTL expiry)                                                 
            ------------ ------------------------------ -----------------------------
            Outgoing Status (PW Status TLV):
            Status code: 0x0 (Up) in Notification message
            MIB cpwVcIndex: 4294836229
            Create time: 17/09/2019 02:01:16 (5w1d ago)
            Last time status changed: 17/09/2019 02:06:13 (5w1d ago)
            Statistics:
            packets: received 0, sent 0
            bytes: received 0, sent 0

        Group to-tcore4-rohan-ten-0-0-0-13, XC Ten-0-5-0-0-14, state is down; Interworking none
        AC: TenGigE0/5/0/0.14, state is up
            Type VLAN; Num Ranges: 1
            Rewrite Tags: []
            VLAN ranges: [14, 14]
            MTU 4470; XC ID 0x1580005; interworking none
            Statistics:
            packets: received 0, sent 0
            bytes: received 0, sent 0
            drops: illegal VLAN 0, illegal length 0
        PW: neighbor 67.70.219.75, PW ID 4293089014, state is down ( local ready )
            PW class vlan-based, XC ID 0xfffe0006
            Encapsulation MPLS, protocol LDP
            Source address 67.70.219.106
            PW type Ethernet VLAN, control word enabled, interworking none
            PW backup disable delay 0 sec
            Sequencing not set
            LSP : Up

            PW Status TLV in use
            MPLS         Local                          Remote                        
            ------------ ------------------------------ -----------------------------
            Label        100596                         unknown                       
            Group ID     0x15800c0                      unknown                       
            Interface    TenGigE0/5/0/0.14              unknown                       
            MTU          4470                           unknown                       
            Control word enabled                        unknown                       
            PW type      Ethernet VLAN                  unknown                       
            VCCV CV type 0x2                            0x0                           
                                                        (none)                        
                        (LSP ping verification)                                      
            VCCV CC type 0x7                            0x0                           
                                                        (none)                        
                        (control word)                                               
                        (router alert label)                                         
                        (TTL expiry)                                                 
            ------------ ------------------------------ -----------------------------
            Outgoing Status (PW Status TLV):
            Status code: 0x0 (Up) in Notification message
            MIB cpwVcIndex: 4294836230
            Create time: 17/09/2019 02:01:16 (5w1d ago)
            Last time status changed: 17/09/2019 02:06:13 (5w1d ago)
            Statistics:
            packets: received 0, sent 0
            bytes: received 0, sent 0

        Group to-tcore4-rohan-ten-0-0-0-13, XC Ten-0-5-0-0-15, state is down; Interworking none
        AC: TenGigE0/5/0/0.15, state is up
            Type VLAN; Num Ranges: 1
            Rewrite Tags: []
            VLAN ranges: [15, 15]
            MTU 4470; XC ID 0x1580006; interworking none
            Statistics:
            packets: received 0, sent 0
            bytes: received 0, sent 0
            drops: illegal VLAN 0, illegal length 0
        PW: neighbor 67.70.219.75, PW ID 4293089015, state is down ( local ready )
            PW class vlan-based, XC ID 0xfffe0007
            Encapsulation MPLS, protocol LDP
            Source address 67.70.219.106
            PW type Ethernet VLAN, control word enabled, interworking none
            PW backup disable delay 0 sec
            Sequencing not set
            LSP : Up

            PW Status TLV in use
            MPLS         Local                          Remote                        
            ------------ ------------------------------ -----------------------------
            Label        100597                         unknown                       
            Group ID     0x15800c0                      unknown                       
            Interface    TenGigE0/5/0/0.15              unknown                       
            MTU          4470                           unknown                       
            Control word enabled                        unknown                       
            PW type      Ethernet VLAN                  unknown                       
            VCCV CV type 0x2                            0x0                           
                                                        (none)                        
                        (LSP ping verification)                                      
            VCCV CC type 0x7                            0x0                           
                                                        (none)                        
                        (control word)                                               
                        (router alert label)                                         
                        (TTL expiry)                                                 
            ------------ ------------------------------ -----------------------------
            Outgoing Status (PW Status TLV):
            Status code: 0x0 (Up) in Notification message
            MIB cpwVcIndex: 4294836231
            Create time: 17/09/2019 02:01:16 (5w1d ago)
            Last time status changed: 17/09/2019 02:06:13 (5w1d ago)
            Statistics:
            packets: received 0, sent 0
            bytes: received 0, sent 0

        Group to-tcore4-rohan-ten-0-0-0-13, XC Ten-0-5-0-0-16, state is down; Interworking none
        AC: TenGigE0/5/0/0.16, state is up
            Type VLAN; Num Ranges: 1
            Rewrite Tags: []
            VLAN ranges: [16, 16]
            MTU 4470; XC ID 0x1580007; interworking none
            Statistics:
            packets: received 0, sent 0
            bytes: received 0, sent 0
            drops: illegal VLAN 0, illegal length 0
        PW: neighbor 67.70.219.75, PW ID 4293089016, state is down ( local ready )
            PW class vlan-based, XC ID 0xfffe0008
            Encapsulation MPLS, protocol LDP
            Source address 67.70.219.106
            PW type Ethernet VLAN, control word enabled, interworking none
            PW backup disable delay 0 sec
            Sequencing not set
            LSP : Up

            PW Status TLV in use
            MPLS         Local                          Remote                        
            ------------ ------------------------------ -----------------------------
            Label        100598                         unknown                       
            Group ID     0x15800c0                      unknown                       
            Interface    TenGigE0/5/0/0.16              unknown                       
            MTU          4470                           unknown                       
            Control word enabled                        unknown                       
            PW type      Ethernet VLAN                  unknown                       
            VCCV CV type 0x2                            0x0                           
                                                        (none)                        
                        (LSP ping verification)                                      
            VCCV CC type 0x7                            0x0                           
                                                        (none)                        
                        (control word)                                               
                        (router alert label)                                         
                        (TTL expiry)                                                 
            ------------ ------------------------------ -----------------------------
            Outgoing Status (PW Status TLV):
            Status code: 0x0 (Up) in Notification message
            MIB cpwVcIndex: 4294836232
            Create time: 17/09/2019 02:01:16 (5w1d ago)
            Last time status changed: 17/09/2019 02:06:13 (5w1d ago)
            Statistics:
            packets: received 0, sent 0
            bytes: received 0, sent 0

        Group to-tcore4-rohan-ten-0-0-0-13, XC Ten-0-5-0-0-17, state is down; Interworking none
        AC: TenGigE0/5/0/0.17, state is up
            Type VLAN; Num Ranges: 1
            Rewrite Tags: []
            VLAN ranges: [17, 17]
            MTU 4470; XC ID 0x1580008; interworking none
            Statistics:
            packets: received 0, sent 0
            bytes: received 0, sent 0
            drops: illegal VLAN 0, illegal length 0
        PW: neighbor 67.70.219.75, PW ID 4293089017, state is down ( local ready )
            PW class vlan-based, XC ID 0xfffe0009
            Encapsulation MPLS, protocol LDP
            Source address 67.70.219.106
            PW type Ethernet VLAN, control word enabled, interworking none
            PW backup disable delay 0 sec
            Sequencing not set
            LSP : Up

            PW Status TLV in use
            MPLS         Local                          Remote                        
            ------------ ------------------------------ -----------------------------
            Label        100599                         unknown                       
            Group ID     0x15800c0                      unknown                       
            Interface    TenGigE0/5/0/0.17              unknown                       
            MTU          4470                           unknown                       
            Control word enabled                        unknown                       
            PW type      Ethernet VLAN                  unknown                       
            VCCV CV type 0x2                            0x0                           
                                                        (none)                        
                        (LSP ping verification)                                      
            VCCV CC type 0x7                            0x0                           
                                                        (none)                        
                        (control word)                                               
                        (router alert label)                                         
                        (TTL expiry)                                                 
            ------------ ------------------------------ -----------------------------
            Outgoing Status (PW Status TLV):
            Status code: 0x0 (Up) in Notification message
            MIB cpwVcIndex: 4294836233
            Create time: 17/09/2019 02:01:16 (5w1d ago)
            Last time status changed: 17/09/2019 02:06:13 (5w1d ago)
            Statistics:
            packets: received 0, sent 0
            bytes: received 0, sent 0

        Group to-tcore4-rohan-ten-0-0-0-13, XC Ten-0-5-0-0-18, state is down; Interworking none
        AC: TenGigE0/5/0/0.18, state is up
            Type VLAN; Num Ranges: 1
            Rewrite Tags: []
            VLAN ranges: [18, 18]
            MTU 4470; XC ID 0x1580009; interworking none
            Statistics:
            packets: received 0, sent 0
            bytes: received 0, sent 0
            drops: illegal VLAN 0, illegal length 0
        PW: neighbor 67.70.219.75, PW ID 4293089018, state is down ( local ready )
            PW class vlan-based, XC ID 0xfffe000a
            Encapsulation MPLS, protocol LDP
            Source address 67.70.219.106
            PW type Ethernet VLAN, control word enabled, interworking none
            PW backup disable delay 0 sec
            Sequencing not set
            LSP : Up

            PW Status TLV in use
            MPLS         Local                          Remote                        
            ------------ ------------------------------ -----------------------------
            Label        100600                         unknown                       
            Group ID     0x15800c0                      unknown                       
            Interface    TenGigE0/5/0/0.18              unknown                       
            MTU          4470                           unknown                       
            Control word enabled                        unknown                       
            PW type      Ethernet VLAN                  unknown                       
            VCCV CV type 0x2                            0x0                           
                                                        (none)                        
                        (LSP ping verification)                                      
            VCCV CC type 0x7                            0x0                           
                                                        (none)                        
                        (control word)                                               
                        (router alert label)                                         
                        (TTL expiry)                                                 
            ------------ ------------------------------ -----------------------------
            Outgoing Status (PW Status TLV):
            Status code: 0x0 (Up) in Notification message
            MIB cpwVcIndex: 4294836234
            Create time: 17/09/2019 02:01:16 (5w1d ago)
            Last time status changed: 17/09/2019 02:06:13 (5w1d ago)
            Statistics:
            packets: received 0, sent 0
            bytes: received 0, sent 0

        Group to-tcore4-rohan-ten-0-0-0-13, XC Ten-0-5-0-0-19, state is down; Interworking none
        AC: TenGigE0/5/0/0.19, state is up
            Type VLAN; Num Ranges: 1
            Rewrite Tags: []
            VLAN ranges: [19, 19]
            MTU 4470; XC ID 0x158000a; interworking none
            Statistics:
            packets: received 0, sent 0
            bytes: received 0, sent 0
            drops: illegal VLAN 0, illegal length 0
        PW: neighbor 67.70.219.75, PW ID 4293089019, state is down ( local ready )
            PW class vlan-based, XC ID 0xfffe000b
            Encapsulation MPLS, protocol LDP
            Source address 67.70.219.106
            PW type Ethernet VLAN, control word enabled, interworking none
            PW backup disable delay 0 sec
            Sequencing not set
            LSP : Up

            PW Status TLV in use
            MPLS         Local                          Remote                        
            ------------ ------------------------------ -----------------------------
            Label        100601                         unknown                       
            Group ID     0x15800c0                      unknown                       
            Interface    TenGigE0/5/0/0.19              unknown                       
            MTU          4470                           unknown                       
            Control word enabled                        unknown                       
            PW type      Ethernet VLAN                  unknown                       
            VCCV CV type 0x2                            0x0                           
                                                        (none)                        
                        (LSP ping verification)                                      
            VCCV CC type 0x7                            0x0                           
                                                        (none)                        
                        (control word)                                               
                        (router alert label)                                         
                        (TTL expiry)                                                 
            ------------ ------------------------------ -----------------------------
            Outgoing Status (PW Status TLV):
            Status code: 0x0 (Up) in Notification message
            MIB cpwVcIndex: 4294836235
            Create time: 17/09/2019 02:01:16 (5w1d ago)
            Last time status changed: 17/09/2019 02:06:13 (5w1d ago)
            Statistics:
            packets: received 0, sent 0
            bytes: received 0, sent 0
    '''}

    golden_parsed_output4 = {
        'group': {
            'TO-tcore4-rohan-port': {
                'xc': {
                    'T-0-5-0-0': {
                        'state': 'unresolved',
                        'interworking': 'none',
                        'ac': {
                            'TenGigE0/5/0/0': {
                                'state': 'unresolved',
                            },
                        },
                        'pw': {
                            'neighbor': {
                                '67.70.219.75': {
                                    'id': {
                                        4293089094: {
                                            'state': 'down ( provisioned )',
                                            'pw_class': 'TO-tcore4-rohan-port',
                                            'xc_id': '0xfffe0001',
                                            'encapsulation': 'MPLS',
                                            'protocol': 'LDP',
                                            'source_address': '67.70.219.106',
                                            'type': 'unknown',
                                            'control_word': 'unknown',
                                            'interworking': 'none',
                                            'backup_disable_delay': 0,
                                            'sequencing': 'not set',
                                            'lsp': 'Up',
                                            'status_tlv': 'not set',
                                            'mpls': {
                                                'label': {
                                                    'local': 'unassigned',
                                                    'remote': 'unknown',
                                                },
                                                'group_id': {
                                                    'local': 'unassigned',
                                                    'remote': 'unknown',
                                                },
                                                'interface': {
                                                    'local': 'unknown',
                                                    'remote': 'unknown',
                                                },
                                                'mtu': {
                                                    'local': 'unknown',
                                                    'remote': 'unknown',
                                                },
                                                'control_word': {
                                                    'local': 'unknown',
                                                    'remote': 'unknown',
                                                },
                                                'pw_type': {
                                                    'local': 'unknown',
                                                    'remote': 'unknown',
                                                },
                                                'vccv_cv_type': {
                                                    'local': '0x0',
                                                    'remote': '0x0',
                                                    'local_type': ['none'],
                                                    'remote_type': ['none'],
                                                },
                                                'vccv_cc_type': {
                                                    'local': '0x0',
                                                    'remote': '0x0',
                                                    'local_type': ['none'],
                                                    'remote_type': ['none'],
                                                },
                                            },
                                            'create_time': '17/09/2019 02:01:16 (5w1d ago)',
                                            'last_time_status_changed': '17/09/2019 02:01:16 (5w1d ago)',
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
            'to-tcore4-rohan-ten-0-0-0-13': {
                'xc': {
                    'Ten-0-5-0-0-10': {
                        'state': 'down',
                        'interworking': 'none',
                        'ac': {
                            'TenGigE0/5/0/0.10': {
                                'state': 'up',
                                'type': 'VLAN',
                                'num_ranges': 1,
                                'rewrite_tags': '',
                                'vlan_ranges': ['10', '10'],
                                'mtu': 4470,
                                'xc_id': '0x1580001',
                                'interworking': 'none',
                                'statistics': {
                                    'packet_totals': {
                                        'receive': 0,
                                        'send': 0,
                                    },
                                    'byte_totals': {
                                        'receive': 0,
                                        'send': 0,
                                    },
                                    'drops': {
                                        'illegal_vlan': 0,
                                        'illegal_length': 0,
                                    },
                                },
                            },
                        },
                        'pw': {
                            'neighbor': {
                                '67.70.219.75': {
                                    'id': {
                                        4293089010: {
                                            'state': 'down ( local ready )',
                                            'pw_class': 'vlan-based',
                                            'xc_id': '0xfffe0002',
                                            'encapsulation': 'MPLS',
                                            'protocol': 'LDP',
                                            'source_address': '67.70.219.106',
                                            'backup_disable_delay': 0,
                                            'sequencing': 'not set',
                                            'lsp': 'Up',
                                            'status_tlv': 'not set',
                                            'mpls': {
                                                'label': {
                                                    'local': '100592',
                                                    'remote': 'unknown',
                                                },
                                                'group_id': {
                                                    'local': '0x15800c0',
                                                    'remote': 'unknown',
                                                },
                                                'monitor_interface': {
                                                    'local': 'TenGigE0/5/0/0.10',
                                                    'remote': 'unknown',
                                                },
                                                'mtu': {
                                                    'local': '4470',
                                                    'remote': 'unknown',
                                                },
                                                'control_word': {
                                                    'local': 'enabled',
                                                    'remote': 'unknown',
                                                },
                                                'pw_type': {
                                                    'local': 'Ethernet VLAN',
                                                    'remote': 'unknown',
                                                },
                                                'vccv_cv_type': {
                                                    'local': '0x2',
                                                    'remote': '0x0',
                                                    'local_type': ['LSP ping verification'],
                                                    'remote_type': ['none'],
                                                },
                                                'vccv_cc_type': {
                                                    'local': '0x7',
                                                    'remote': '0x0',
                                                    'local_type': ['control word', 'router alert label', 'TTL expiry'],
                                                    'remote_type': ['none'],
                                                },
                                            },
                                            'create_time': '17/09/2019 02:01:16 (5w1d ago)',
                                            'last_time_status_changed': '17/09/2019 02:06:13 (5w1d ago)',
                                            'statistics': {
                                                'packet_totals': {
                                                    'receive': 0,
                                                    'send': 0,
                                                },
                                                'byte_totals': {
                                                    'receive': 0,
                                                    'send': 0,
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                    'Ten-0-5-0-0-11': {
                        'state': 'down',
                        'interworking': 'none',
                        'ac': {
                            'TenGigE0/5/0/0.11': {
                                'state': 'up',
                                'type': 'VLAN',
                                'num_ranges': 1,
                                'rewrite_tags': '',
                                'vlan_ranges': ['11', '11'],
                                'mtu': 4470,
                                'xc_id': '0x1580002',
                                'interworking': 'none',
                                'statistics': {
                                    'packet_totals': {
                                        'receive': 0,
                                        'send': 0,
                                    },
                                    'byte_totals': {
                                        'receive': 0,
                                        'send': 0,
                                    },
                                    'drops': {
                                        'illegal_vlan': 0,
                                        'illegal_length': 0,
                                    },
                                },
                            },
                        },
                        'pw': {
                            'neighbor': {
                                '67.70.219.75': {
                                    'id': {
                                        4293089011: {
                                            'state': 'down ( local ready )',
                                            'pw_class': 'vlan-based',
                                            'xc_id': '0xfffe0003',
                                            'encapsulation': 'MPLS',
                                            'protocol': 'LDP',
                                            'source_address': '67.70.219.106',
                                            'backup_disable_delay': 0,
                                            'sequencing': 'not set',
                                            'lsp': 'Up',
                                            'status_tlv': 'not set',
                                            'mpls': {
                                                'label': {
                                                    'local': '100593',
                                                    'remote': 'unknown',
                                                },
                                                'group_id': {
                                                    'local': '0x15800c0',
                                                    'remote': 'unknown',
                                                },
                                                'monitor_interface': {
                                                    'local': 'TenGigE0/5/0/0.11',
                                                    'remote': 'unknown',
                                                },
                                                'mtu': {
                                                    'local': '4470',
                                                    'remote': 'unknown',
                                                },
                                                'control_word': {
                                                    'local': 'enabled',
                                                    'remote': 'unknown',
                                                },
                                                'pw_type': {
                                                    'local': 'Ethernet VLAN',
                                                    'remote': 'unknown',
                                                },
                                                'vccv_cv_type': {
                                                    'local': '0x2',
                                                    'remote': '0x0',
                                                    'local_type': ['LSP ping verification'],
                                                    'remote_type': ['none'],
                                                },
                                                'vccv_cc_type': {
                                                    'local': '0x7',
                                                    'remote': '0x0',
                                                    'local_type': ['control word', 'router alert label', 'TTL expiry'],
                                                    'remote_type': ['none'],
                                                },
                                            },
                                            'create_time': '17/09/2019 02:01:16 (5w1d ago)',
                                            'last_time_status_changed': '17/09/2019 02:06:13 (5w1d ago)',
                                            'statistics': {
                                                'packet_totals': {
                                                    'receive': 0,
                                                    'send': 0,
                                                },
                                                'byte_totals': {
                                                    'receive': 0,
                                                    'send': 0,
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                    'Ten-0-5-0-0-12': {
                        'state': 'down',
                        'interworking': 'none',
                        'ac': {
                            'TenGigE0/5/0/0.12': {
                                'state': 'up',
                                'type': 'VLAN',
                                'num_ranges': 1,
                                'rewrite_tags': '',
                                'vlan_ranges': ['12', '12'],
                                'mtu': 4470,
                                'xc_id': '0x1580003',
                                'interworking': 'none',
                                'statistics': {
                                    'packet_totals': {
                                        'receive': 0,
                                        'send': 0,
                                    },
                                    'byte_totals': {
                                        'receive': 0,
                                        'send': 0,
                                    },
                                    'drops': {
                                        'illegal_vlan': 0,
                                        'illegal_length': 0,
                                    },
                                },
                            },
                        },
                        'pw': {
                            'neighbor': {
                                '67.70.219.75': {
                                    'id': {
                                        4293089012: {
                                            'state': 'down ( local ready )',
                                            'pw_class': 'vlan-based',
                                            'xc_id': '0xfffe0004',
                                            'encapsulation': 'MPLS',
                                            'protocol': 'LDP',
                                            'source_address': '67.70.219.106',
                                            'backup_disable_delay': 0,
                                            'sequencing': 'not set',
                                            'lsp': 'Up',
                                            'status_tlv': 'not set',
                                            'mpls': {
                                                'label': {
                                                    'local': '100594',
                                                    'remote': 'unknown',
                                                },
                                                'group_id': {
                                                    'local': '0x15800c0',
                                                    'remote': 'unknown',
                                                },
                                                'monitor_interface': {
                                                    'local': 'TenGigE0/5/0/0.12',
                                                    'remote': 'unknown',
                                                },
                                                'mtu': {
                                                    'local': '4470',
                                                    'remote': 'unknown',
                                                },
                                                'control_word': {
                                                    'local': 'enabled',
                                                    'remote': 'unknown',
                                                },
                                                'pw_type': {
                                                    'local': 'Ethernet VLAN',
                                                    'remote': 'unknown',
                                                },
                                                'vccv_cv_type': {
                                                    'local': '0x2',
                                                    'remote': '0x0',
                                                    'local_type': ['LSP ping verification'],
                                                    'remote_type': ['none'],
                                                },
                                                'vccv_cc_type': {
                                                    'local': '0x7',
                                                    'remote': '0x0',
                                                    'local_type': ['control word', 'router alert label', 'TTL expiry'],
                                                    'remote_type': ['none'],
                                                },
                                            },
                                            'create_time': '17/09/2019 02:01:16 (5w1d ago)',
                                            'last_time_status_changed': '17/09/2019 02:06:13 (5w1d ago)',
                                            'statistics': {
                                                'packet_totals': {
                                                    'receive': 0,
                                                    'send': 0,
                                                },
                                                'byte_totals': {
                                                    'receive': 0,
                                                    'send': 0,
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                    'Ten-0-5-0-0-13': {
                        'state': 'down',
                        'interworking': 'none',
                        'ac': {
                            'TenGigE0/5/0/0.13': {
                                'state': 'up',
                                'type': 'VLAN',
                                'num_ranges': 1,
                                'rewrite_tags': '',
                                'vlan_ranges': ['13', '13'],
                                'mtu': 4470,
                                'xc_id': '0x1580004',
                                'interworking': 'none',
                                'statistics': {
                                    'packet_totals': {
                                        'receive': 0,
                                        'send': 0,
                                    },
                                    'byte_totals': {
                                        'receive': 0,
                                        'send': 0,
                                    },
                                    'drops': {
                                        'illegal_vlan': 0,
                                        'illegal_length': 0,
                                    },
                                },
                            },
                        },
                        'pw': {
                            'neighbor': {
                                '67.70.219.75': {
                                    'id': {
                                        4293089013: {
                                            'state': 'down ( local ready )',
                                            'pw_class': 'vlan-based',
                                            'xc_id': '0xfffe0005',
                                            'encapsulation': 'MPLS',
                                            'protocol': 'LDP',
                                            'source_address': '67.70.219.106',
                                            'backup_disable_delay': 0,
                                            'sequencing': 'not set',
                                            'lsp': 'Up',
                                            'status_tlv': 'not set',
                                            'mpls': {
                                                'label': {
                                                    'local': '100595',
                                                    'remote': 'unknown',
                                                },
                                                'group_id': {
                                                    'local': '0x15800c0',
                                                    'remote': 'unknown',
                                                },
                                                'monitor_interface': {
                                                    'local': 'TenGigE0/5/0/0.13',
                                                    'remote': 'unknown',
                                                },
                                                'mtu': {
                                                    'local': '4470',
                                                    'remote': 'unknown',
                                                },
                                                'control_word': {
                                                    'local': 'enabled',
                                                    'remote': 'unknown',
                                                },
                                                'pw_type': {
                                                    'local': 'Ethernet VLAN',
                                                    'remote': 'unknown',
                                                },
                                                'vccv_cv_type': {
                                                    'local': '0x2',
                                                    'remote': '0x0',
                                                    'local_type': ['LSP ping verification'],
                                                    'remote_type': ['none'],
                                                },
                                                'vccv_cc_type': {
                                                    'local': '0x7',
                                                    'remote': '0x0',
                                                    'local_type': ['control word', 'router alert label', 'TTL expiry'],
                                                    'remote_type': ['none'],
                                                },
                                            },
                                            'create_time': '17/09/2019 02:01:16 (5w1d ago)',
                                            'last_time_status_changed': '17/09/2019 02:06:13 (5w1d ago)',
                                            'statistics': {
                                                'packet_totals': {
                                                    'receive': 0,
                                                    'send': 0,
                                                },
                                                'byte_totals': {
                                                    'receive': 0,
                                                    'send': 0,
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                    'Ten-0-5-0-0-14': {
                        'state': 'down',
                        'interworking': 'none',
                        'ac': {
                            'TenGigE0/5/0/0.14': {
                                'state': 'up',
                                'type': 'VLAN',
                                'num_ranges': 1,
                                'rewrite_tags': '',
                                'vlan_ranges': ['14', '14'],
                                'mtu': 4470,
                                'xc_id': '0x1580005',
                                'interworking': 'none',
                                'statistics': {
                                    'packet_totals': {
                                        'receive': 0,
                                        'send': 0,
                                    },
                                    'byte_totals': {
                                        'receive': 0,
                                        'send': 0,
                                    },
                                    'drops': {
                                        'illegal_vlan': 0,
                                        'illegal_length': 0,
                                    },
                                },
                            },
                        },
                        'pw': {
                            'neighbor': {
                                '67.70.219.75': {
                                    'id': {
                                        4293089014: {
                                            'state': 'down ( local ready )',
                                            'pw_class': 'vlan-based',
                                            'xc_id': '0xfffe0006',
                                            'encapsulation': 'MPLS',
                                            'protocol': 'LDP',
                                            'source_address': '67.70.219.106',
                                            'backup_disable_delay': 0,
                                            'sequencing': 'not set',
                                            'lsp': 'Up',
                                            'status_tlv': 'not set',
                                            'mpls': {
                                                'label': {
                                                    'local': '100596',
                                                    'remote': 'unknown',
                                                },
                                                'group_id': {
                                                    'local': '0x15800c0',
                                                    'remote': 'unknown',
                                                },
                                                'monitor_interface': {
                                                    'local': 'TenGigE0/5/0/0.14',
                                                    'remote': 'unknown',
                                                },
                                                'mtu': {
                                                    'local': '4470',
                                                    'remote': 'unknown',
                                                },
                                                'control_word': {
                                                    'local': 'enabled',
                                                    'remote': 'unknown',
                                                },
                                                'pw_type': {
                                                    'local': 'Ethernet VLAN',
                                                    'remote': 'unknown',
                                                },
                                                'vccv_cv_type': {
                                                    'local': '0x2',
                                                    'remote': '0x0',
                                                    'local_type': ['LSP ping verification'],
                                                    'remote_type': ['none'],
                                                },
                                                'vccv_cc_type': {
                                                    'local': '0x7',
                                                    'remote': '0x0',
                                                    'local_type': ['control word', 'router alert label', 'TTL expiry'],
                                                    'remote_type': ['none'],
                                                },
                                            },
                                            'create_time': '17/09/2019 02:01:16 (5w1d ago)',
                                            'last_time_status_changed': '17/09/2019 02:06:13 (5w1d ago)',
                                            'statistics': {
                                                'packet_totals': {
                                                    'receive': 0,
                                                    'send': 0,
                                                },
                                                'byte_totals': {
                                                    'receive': 0,
                                                    'send': 0,
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                    'Ten-0-5-0-0-15': {
                        'state': 'down',
                        'interworking': 'none',
                        'ac': {
                            'TenGigE0/5/0/0.15': {
                                'state': 'up',
                                'type': 'VLAN',
                                'num_ranges': 1,
                                'rewrite_tags': '',
                                'vlan_ranges': ['15', '15'],
                                'mtu': 4470,
                                'xc_id': '0x1580006',
                                'interworking': 'none',
                                'statistics': {
                                    'packet_totals': {
                                        'receive': 0,
                                        'send': 0,
                                    },
                                    'byte_totals': {
                                        'receive': 0,
                                        'send': 0,
                                    },
                                    'drops': {
                                        'illegal_vlan': 0,
                                        'illegal_length': 0,
                                    },
                                },
                            },
                        },
                        'pw': {
                            'neighbor': {
                                '67.70.219.75': {
                                    'id': {
                                        4293089015: {
                                            'state': 'down ( local ready )',
                                            'pw_class': 'vlan-based',
                                            'xc_id': '0xfffe0007',
                                            'encapsulation': 'MPLS',
                                            'protocol': 'LDP',
                                            'source_address': '67.70.219.106',
                                            'backup_disable_delay': 0,
                                            'sequencing': 'not set',
                                            'lsp': 'Up',
                                            'status_tlv': 'not set',
                                            'mpls': {
                                                'label': {
                                                    'local': '100597',
                                                    'remote': 'unknown',
                                                },
                                                'group_id': {
                                                    'local': '0x15800c0',
                                                    'remote': 'unknown',
                                                },
                                                'monitor_interface': {
                                                    'local': 'TenGigE0/5/0/0.15',
                                                    'remote': 'unknown',
                                                },
                                                'mtu': {
                                                    'local': '4470',
                                                    'remote': 'unknown',
                                                },
                                                'control_word': {
                                                    'local': 'enabled',
                                                    'remote': 'unknown',
                                                },
                                                'pw_type': {
                                                    'local': 'Ethernet VLAN',
                                                    'remote': 'unknown',
                                                },
                                                'vccv_cv_type': {
                                                    'local': '0x2',
                                                    'remote': '0x0',
                                                    'local_type': ['LSP ping verification'],
                                                    'remote_type': ['none'],
                                                },
                                                'vccv_cc_type': {
                                                    'local': '0x7',
                                                    'remote': '0x0',
                                                    'local_type': ['control word', 'router alert label', 'TTL expiry'],
                                                    'remote_type': ['none'],
                                                },
                                            },
                                            'create_time': '17/09/2019 02:01:16 (5w1d ago)',
                                            'last_time_status_changed': '17/09/2019 02:06:13 (5w1d ago)',
                                            'statistics': {
                                                'packet_totals': {
                                                    'receive': 0,
                                                    'send': 0,
                                                },
                                                'byte_totals': {
                                                    'receive': 0,
                                                    'send': 0,
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                    'Ten-0-5-0-0-16': {
                        'state': 'down',
                        'interworking': 'none',
                        'ac': {
                            'TenGigE0/5/0/0.16': {
                                'state': 'up',
                                'type': 'VLAN',
                                'num_ranges': 1,
                                'rewrite_tags': '',
                                'vlan_ranges': ['16', '16'],
                                'mtu': 4470,
                                'xc_id': '0x1580007',
                                'interworking': 'none',
                                'statistics': {
                                    'packet_totals': {
                                        'receive': 0,
                                        'send': 0,
                                    },
                                    'byte_totals': {
                                        'receive': 0,
                                        'send': 0,
                                    },
                                    'drops': {
                                        'illegal_vlan': 0,
                                        'illegal_length': 0,
                                    },
                                },
                            },
                        },
                        'pw': {
                            'neighbor': {
                                '67.70.219.75': {
                                    'id': {
                                        4293089016: {
                                            'state': 'down ( local ready )',
                                            'pw_class': 'vlan-based',
                                            'xc_id': '0xfffe0008',
                                            'encapsulation': 'MPLS',
                                            'protocol': 'LDP',
                                            'source_address': '67.70.219.106',
                                            'backup_disable_delay': 0,
                                            'sequencing': 'not set',
                                            'lsp': 'Up',
                                            'status_tlv': 'not set',
                                            'mpls': {
                                                'label': {
                                                    'local': '100598',
                                                    'remote': 'unknown',
                                                },
                                                'group_id': {
                                                    'local': '0x15800c0',
                                                    'remote': 'unknown',
                                                },
                                                'monitor_interface': {
                                                    'local': 'TenGigE0/5/0/0.16',
                                                    'remote': 'unknown',
                                                },
                                                'mtu': {
                                                    'local': '4470',
                                                    'remote': 'unknown',
                                                },
                                                'control_word': {
                                                    'local': 'enabled',
                                                    'remote': 'unknown',
                                                },
                                                'pw_type': {
                                                    'local': 'Ethernet VLAN',
                                                    'remote': 'unknown',
                                                },
                                                'vccv_cv_type': {
                                                    'local': '0x2',
                                                    'remote': '0x0',
                                                    'local_type': ['LSP ping verification'],
                                                    'remote_type': ['none'],
                                                },
                                                'vccv_cc_type': {
                                                    'local': '0x7',
                                                    'remote': '0x0',
                                                    'local_type': ['control word', 'router alert label', 'TTL expiry'],
                                                    'remote_type': ['none'],
                                                },
                                            },
                                            'create_time': '17/09/2019 02:01:16 (5w1d ago)',
                                            'last_time_status_changed': '17/09/2019 02:06:13 (5w1d ago)',
                                            'statistics': {
                                                'packet_totals': {
                                                    'receive': 0,
                                                    'send': 0,
                                                },
                                                'byte_totals': {
                                                    'receive': 0,
                                                    'send': 0,
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                    'Ten-0-5-0-0-17': {
                        'state': 'down',
                        'interworking': 'none',
                        'ac': {
                            'TenGigE0/5/0/0.17': {
                                'state': 'up',
                                'type': 'VLAN',
                                'num_ranges': 1,
                                'rewrite_tags': '',
                                'vlan_ranges': ['17', '17'],
                                'mtu': 4470,
                                'xc_id': '0x1580008',
                                'interworking': 'none',
                                'statistics': {
                                    'packet_totals': {
                                        'receive': 0,
                                        'send': 0,
                                    },
                                    'byte_totals': {
                                        'receive': 0,
                                        'send': 0,
                                    },
                                    'drops': {
                                        'illegal_vlan': 0,
                                        'illegal_length': 0,
                                    },
                                },
                            },
                        },
                        'pw': {
                            'neighbor': {
                                '67.70.219.75': {
                                    'id': {
                                        4293089017: {
                                            'state': 'down ( local ready )',
                                            'pw_class': 'vlan-based',
                                            'xc_id': '0xfffe0009',
                                            'encapsulation': 'MPLS',
                                            'protocol': 'LDP',
                                            'source_address': '67.70.219.106',
                                            'backup_disable_delay': 0,
                                            'sequencing': 'not set',
                                            'lsp': 'Up',
                                            'status_tlv': 'not set',
                                            'mpls': {
                                                'label': {
                                                    'local': '100599',
                                                    'remote': 'unknown',
                                                },
                                                'group_id': {
                                                    'local': '0x15800c0',
                                                    'remote': 'unknown',
                                                },
                                                'monitor_interface': {
                                                    'local': 'TenGigE0/5/0/0.17',
                                                    'remote': 'unknown',
                                                },
                                                'mtu': {
                                                    'local': '4470',
                                                    'remote': 'unknown',
                                                },
                                                'control_word': {
                                                    'local': 'enabled',
                                                    'remote': 'unknown',
                                                },
                                                'pw_type': {
                                                    'local': 'Ethernet VLAN',
                                                    'remote': 'unknown',
                                                },
                                                'vccv_cv_type': {
                                                    'local': '0x2',
                                                    'remote': '0x0',
                                                    'local_type': ['LSP ping verification'],
                                                    'remote_type': ['none'],
                                                },
                                                'vccv_cc_type': {
                                                    'local': '0x7',
                                                    'remote': '0x0',
                                                    'local_type': ['control word', 'router alert label', 'TTL expiry'],
                                                    'remote_type': ['none'],
                                                },
                                            },
                                            'create_time': '17/09/2019 02:01:16 (5w1d ago)',
                                            'last_time_status_changed': '17/09/2019 02:06:13 (5w1d ago)',
                                            'statistics': {
                                                'packet_totals': {
                                                    'receive': 0,
                                                    'send': 0,
                                                },
                                                'byte_totals': {
                                                    'receive': 0,
                                                    'send': 0,
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                    'Ten-0-5-0-0-18': {
                        'state': 'down',
                        'interworking': 'none',
                        'ac': {
                            'TenGigE0/5/0/0.18': {
                                'state': 'up',
                                'type': 'VLAN',
                                'num_ranges': 1,
                                'rewrite_tags': '',
                                'vlan_ranges': ['18', '18'],
                                'mtu': 4470,
                                'xc_id': '0x1580009',
                                'interworking': 'none',
                                'statistics': {
                                    'packet_totals': {
                                        'receive': 0,
                                        'send': 0,
                                    },
                                    'byte_totals': {
                                        'receive': 0,
                                        'send': 0,
                                    },
                                    'drops': {
                                        'illegal_vlan': 0,
                                        'illegal_length': 0,
                                    },
                                },
                            },
                        },
                        'pw': {
                            'neighbor': {
                                '67.70.219.75': {
                                    'id': {
                                        4293089018: {
                                            'state': 'down ( local ready )',
                                            'pw_class': 'vlan-based',
                                            'xc_id': '0xfffe000a',
                                            'encapsulation': 'MPLS',
                                            'protocol': 'LDP',
                                            'source_address': '67.70.219.106',
                                            'backup_disable_delay': 0,
                                            'sequencing': 'not set',
                                            'lsp': 'Up',
                                            'status_tlv': 'not set',
                                            'mpls': {
                                                'label': {
                                                    'local': '100600',
                                                    'remote': 'unknown',
                                                },
                                                'group_id': {
                                                    'local': '0x15800c0',
                                                    'remote': 'unknown',
                                                },
                                                'monitor_interface': {
                                                    'local': 'TenGigE0/5/0/0.18',
                                                    'remote': 'unknown',
                                                },
                                                'mtu': {
                                                    'local': '4470',
                                                    'remote': 'unknown',
                                                },
                                                'control_word': {
                                                    'local': 'enabled',
                                                    'remote': 'unknown',
                                                },
                                                'pw_type': {
                                                    'local': 'Ethernet VLAN',
                                                    'remote': 'unknown',
                                                },
                                                'vccv_cv_type': {
                                                    'local': '0x2',
                                                    'remote': '0x0',
                                                    'local_type': ['LSP ping verification'],
                                                    'remote_type': ['none'],
                                                },
                                                'vccv_cc_type': {
                                                    'local': '0x7',
                                                    'remote': '0x0',
                                                    'local_type': ['control word', 'router alert label', 'TTL expiry'],
                                                    'remote_type': ['none'],
                                                },
                                            },
                                            'create_time': '17/09/2019 02:01:16 (5w1d ago)',
                                            'last_time_status_changed': '17/09/2019 02:06:13 (5w1d ago)',
                                            'statistics': {
                                                'packet_totals': {
                                                    'receive': 0,
                                                    'send': 0,
                                                },
                                                'byte_totals': {
                                                    'receive': 0,
                                                    'send': 0,
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                    'Ten-0-5-0-0-19': {
                        'state': 'down',
                        'interworking': 'none',
                        'ac': {
                            'TenGigE0/5/0/0.19': {
                                'state': 'up',
                                'type': 'VLAN',
                                'num_ranges': 1,
                                'rewrite_tags': '',
                                'vlan_ranges': ['19', '19'],
                                'mtu': 4470,
                                'xc_id': '0x158000a',
                                'interworking': 'none',
                                'statistics': {
                                    'packet_totals': {
                                        'receive': 0,
                                        'send': 0,
                                    },
                                    'byte_totals': {
                                        'receive': 0,
                                        'send': 0,
                                    },
                                    'drops': {
                                        'illegal_vlan': 0,
                                        'illegal_length': 0,
                                    },
                                },
                            },
                        },
                        'pw': {
                            'neighbor': {
                                '67.70.219.75': {
                                    'id': {
                                        4293089019: {
                                            'state': 'down ( local ready )',
                                            'pw_class': 'vlan-based',
                                            'xc_id': '0xfffe000b',
                                            'encapsulation': 'MPLS',
                                            'protocol': 'LDP',
                                            'source_address': '67.70.219.106',
                                            'backup_disable_delay': 0,
                                            'sequencing': 'not set',
                                            'lsp': 'Up',
                                            'status_tlv': 'not set',
                                            'mpls': {
                                                'label': {
                                                    'local': '100601',
                                                    'remote': 'unknown',
                                                },
                                                'group_id': {
                                                    'local': '0x15800c0',
                                                    'remote': 'unknown',
                                                },
                                                'monitor_interface': {
                                                    'local': 'TenGigE0/5/0/0.19',
                                                    'remote': 'unknown',
                                                },
                                                'mtu': {
                                                    'local': '4470',
                                                    'remote': 'unknown',
                                                },
                                                'control_word': {
                                                    'local': 'enabled',
                                                    'remote': 'unknown',
                                                },
                                                'pw_type': {
                                                    'local': 'Ethernet VLAN',
                                                    'remote': 'unknown',
                                                },
                                                'vccv_cv_type': {
                                                    'local': '0x2',
                                                    'remote': '0x0',
                                                    'local_type': ['LSP ping verification'],
                                                    'remote_type': ['none'],
                                                },
                                                'vccv_cc_type': {
                                                    'local': '0x7',
                                                    'remote': '0x0',
                                                    'local_type': ['control word', 'router alert label', 'TTL expiry'],
                                                    'remote_type': ['none'],
                                                },
                                            },
                                            'create_time': '17/09/2019 02:01:16 (5w1d ago)',
                                            'last_time_status_changed': '17/09/2019 02:06:13 (5w1d ago)',
                                            'statistics': {
                                                'packet_totals': {
                                                    'receive': 0,
                                                    'send': 0,
                                                },
                                                'byte_totals': {
                                                    'receive': 0,
                                                    'send': 0,
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }

    golden_output5 = {'execute.return_value': '''
        show l2vpn xconnect detail

        Wed Oct 23 14:13:50.133 EDT

        Group to-tcore4-rohan, XC to-tcore4-rohan, state is unresolved; Interworking none
        Not provisioned reason(s):
            Only one segment (Pseudowire) is present

        PW: neighbor 67.70.219.75, PW ID 2015030201, state is unresolved
        segment state is unresolved

        Group to-tcore1-mordor, XC to-tcore1-mordor, state is down; Interworking none
        AC: TenGigE0/4/0/5, state is up
            Type Ethernet
            MTU 4470; XC ID 0x1480001; interworking none
            Statistics:
            packets: received 0, sent 0
            bytes: received 0, sent 0
        PW: neighbor 69.158.196.10, PW ID 1152, state is down ( local ready )
            PW class port-based, XC ID 0xfffe0001
            Encapsulation MPLS, protocol LDP
            Source address 67.70.219.115
            PW type Ethernet, control word enabled, interworking none
            PW backup disable delay 0 sec
            Sequencing not set
            LSP : Up

            PW Status TLV in use
            MPLS         Local                          Remote                        
            ------------ ------------------------------ -----------------------------
            Label        100483                         unknown                       
            Group ID     0x1480520                      unknown                       
            Interface    TenGigE0/4/0/5                 unknown                       
            MTU          4470                           unknown                       
            Control word enabled                        unknown                       
            PW type      Ethernet                       unknown                       
            VCCV CV type 0x2                            0x0                           
                                                        (none)                        
                        (LSP ping verification)                                      
            VCCV CC type 0x7                            0x0                           
                                                        (none)                        
                        (control word)                                               
                        (router alert label)                                         
                        (TTL expiry)                                                 
            ------------ ------------------------------ -----------------------------
            Outgoing Status (PW Status TLV):
            Status code: 0x0 (Up) in Notification message
            MIB cpwVcIndex: 4294836225
            Create time: 11/10/2019 11:09:47 (1w5d ago)
            Last time status changed: 11/10/2019 11:13:16 (1w5d ago)
            Statistics:
            packets: received 0, sent 0
            bytes: received 0, sent 0

        Group TO-tcore4gondor-port, XC T-0-4-0-2, state is unresolved; Interworking none
        Not provisioned reason(s):
            Only one segment (Pseudowire) is present

        PW: neighbor 67.70.219.98, PW ID 4293089094, state is unresolved
        segment state is unresolved
    '''}

    golden_parsed_output5 = {
        'group': {
            'to-tcore4-rohan': {
                'xc': {
                    'to-tcore4-rohan': {
                        'state': 'unresolved',
                        'interworking': 'none',
                        'pw': {
                            'neighbor': {
                                '67.70.219.75': {
                                    'id': {
                                        2015030201: {
                                            'state': 'unresolved',
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
            'to-tcore1-mordor': {
                'xc': {
                    'to-tcore1-mordor': {
                        'state': 'down',
                        'interworking': 'none',
                        'ac': {
                            'TenGigE0/4/0/5': {
                                'state': 'up',
                                'type': 'Ethernet',
                                'mtu': 4470,
                                'xc_id': '0x1480001',
                                'interworking': 'none',
                                'statistics': {
                                    'packet_totals': {
                                        'receive': 0,
                                        'send': 0,
                                    },
                                    'byte_totals': {
                                        'receive': 0,
                                        'send': 0,
                                    },
                                },
                            },
                        },
                        'pw': {
                            'neighbor': {
                                '69.158.196.10': {
                                    'id': {
                                        1152: {
                                            'state': 'down ( local ready )',
                                            'pw_class': 'port-based',
                                            'xc_id': '0xfffe0001',
                                            'encapsulation': 'MPLS',
                                            'protocol': 'LDP',
                                            'source_address': '67.70.219.115',
                                            'type': 'Ethernet',
                                            'control_word': 'enabled',
                                            'interworking': 'none',
                                            'backup_disable_delay': 0,
                                            'sequencing': 'not set',
                                            'lsp': 'Up',
                                            'status_tlv': 'not set',
                                            'mpls': {
                                                'label': {
                                                    'local': '100483',
                                                    'remote': 'unknown',
                                                },
                                                'group_id': {
                                                    'local': '0x1480520',
                                                    'remote': 'unknown',
                                                },
                                                'interface': {
                                                    'local': 'TenGigE0/4/0/5',
                                                    'remote': 'unknown',
                                                },
                                                'mtu': {
                                                    'local': '4470',
                                                    'remote': 'unknown',
                                                },
                                                'control_word': {
                                                    'local': 'enabled',
                                                    'remote': 'unknown',
                                                },
                                                'pw_type': {
                                                    'local': 'Ethernet',
                                                    'remote': 'unknown',
                                                },
                                                'vccv_cv_type': {
                                                    'local': '0x2',
                                                    'remote': '0x0',
                                                    'local_type': ['LSP ping verification'],
                                                    'remote_type': ['none'],
                                                },
                                                'vccv_cc_type': {
                                                    'local': '0x7',
                                                    'remote': '0x0',
                                                    'local_type': ['control word', 'router alert label', 'TTL expiry'],
                                                    'remote_type': ['none'],
                                                },
                                            },
                                            'create_time': '11/10/2019 11:09:47 (1w5d ago)',
                                            'last_time_status_changed': '11/10/2019 11:13:16 (1w5d ago)',
                                            'statistics': {
                                                'packet_totals': {
                                                    'receive': 0,
                                                    'send': 0,
                                                },
                                                'byte_totals': {
                                                    'receive': 0,
                                                    'send': 0,
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
            'TO-tcore4gondor-port': {
                'xc': {
                    'T-0-4-0-2': {
                        'state': 'unresolved',
                        'interworking': 'none',
                        'pw': {
                            'neighbor': {
                                '67.70.219.98': {
                                    'id': {
                                        4293089094: {
                                            'state': 'unresolved',
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }

    golden_output6 = {'execute.return_value': '''
        show l2vpn xconnect detail

        Wed Oct 23 13:55:55.601 EDT

        Group vpws, XC vpws, state is unresolved; Interworking none
        Not provisioned reason(s):
            AC I/F not ready

        AC: TenGigE0/1/0/0, state is unresolved
        EVPN: neighbor 0.0.0.0, PW ID: evi 200, ac-id 202, state is down ( idle )
            XC ID 0xa0000003
            Encapsulation MPLS
            Source address 67.70.219.85
            Encap type unknown, control word unknown
            Sequencing not set
            LSP : Up

            PW Status TLV in use
            EVPN         Local                          Remote                        
            ------------ ------------------------------ -----------------------------
            Label        unassigned                     unknown                       
            MTU          unknown                        unknown                       
            Control word unknown                        unknown                       
            AC ID        201                            202                           
            EVPN type    unknown                        unknown                       

            ------------ ------------------------------ -----------------------------
            Create time: 11/07/2019 13:01:41 (14w6d ago)
            No status change since creation

        Group vpws, XC vrp_vpws_tor2_bl2_10294, state is down; Interworking none
        AC: Bundle-Ether2.60, state is up
            Type VLAN; Num Ranges: 1
            Rewrite Tags: []
            VLAN ranges: [60, 60]
            MTU 9198; XC ID 0xc0000002; interworking none
            Statistics:
            packets: received 1809419, sent 0
            bytes: received 174143224, sent 0
            drops: illegal VLAN 0, illegal length 0
        EVPN: neighbor 172.16.2.89, PW ID: evi 10294, ac-id 20294, state is down ( local ready )
            XC ID 0xa0000005
            Encapsulation MPLS
            Source address 67.70.219.85
            Encap type Ethernet, control word enabled
            Sequencing not set
            LSP : Up

            EVPN         Local                          Remote                        
            ------------ ------------------------------ -----------------------------
            Label        100483                         unknown                       
            MTU          9198                           unknown                       
            Control word enabled                        unknown                       
            AC ID        30294                          20294                         
            EVPN type    Ethernet                       unknown                       

            ------------ ------------------------------ -----------------------------
            Create time: 11/07/2019 13:01:41 (14w6d ago)
            Last time status changed: 11/09/2019 08:03:16 (6w0d ago)
            Last time PW went down: 26/08/2019 15:14:22 (8w1d ago)
            Statistics:
            packets: received 0, sent 1809419
            bytes: received 0, sent 174143224
    '''}

    golden_parsed_output6 = {
        'group': {
            'vpws': {
                'xc': {
                    'vpws': {
                        'state': 'unresolved',
                        'interworking': 'none',
                        'ac': {
                            'TenGigE0/1/0/0': {
                                'state': 'unresolved',
                            },
                        },
                        'evpn': {
                            'neighbor': {
                                '0.0.0.0': {
                                    'id': {
                                        'evi 200': {
                                            'state': 'down ( idle )',
                                            'ac_id': 202,
                                            'xc_id': '0xa0000003',
                                            'encapsulation': 'MPLS',
                                            'source_address': '67.70.219.85',
                                            'encap_type': 'unknown',
                                            'control_word': 'unknown',
                                            'sequencing': 'not set',
                                            'lsp': 'Up',
                                            'status_tlv': 'not set',
                                            'evpn': {
                                                'label': {
                                                    'local': 'unassigned',
                                                    'remote': 'unknown',
                                                },
                                                'mtu': {
                                                    'local': 'unknown',
                                                    'remote': 'unknown',
                                                },
                                                'control_word': {
                                                    'local': 'unknown',
                                                    'remote': 'unknown',
                                                },
                                                'ac_id': {
                                                    'local': '201',
                                                    'remote': '202',
                                                },
                                                'evpn_type': {
                                                    'local': 'unknown',
                                                    'remote': 'unknown',
                                                },
                                            },
                                            'create_time': '11/07/2019 13:01:41 (14w6d ago)',
                                        },
                                    },
                                },
                            },
                        },
                    },
                    'vrp_vpws_tor2_bl2_10294': {
                        'state': 'down',
                        'interworking': 'none',
                        'ac': {
                            'Bundle-Ether2.60': {
                                'state': 'up',
                                'type': 'VLAN',
                                'num_ranges': 1,
                                'rewrite_tags': '',
                                'vlan_ranges': ['60', '60'],
                                'mtu': 9198,
                                'xc_id': '0xc0000002',
                                'interworking': 'none',
                                'statistics': {
                                    'packet_totals': {
                                        'receive': 1809419,
                                        'send': 0,
                                    },
                                    'byte_totals': {
                                        'receive': 174143224,
                                        'send': 0,
                                    },
                                    'drops': {
                                        'illegal_vlan': 0,
                                        'illegal_length': 0,
                                    },
                                },
                            },
                        },
                        'evpn': {
                            'neighbor': {
                                '172.16.2.89': {
                                    'id': {
                                        'evi 10294': {
                                            'state': 'down ( local ready )',
                                            'ac_id': 20294,
                                            'xc_id': '0xa0000005',
                                            'encapsulation': 'MPLS',
                                            'source_address': '67.70.219.85',
                                            'encap_type': 'Ethernet',
                                            'control_word': 'enabled',
                                            'sequencing': 'not set',
                                            'lsp': 'Up',
                                            'evpn': {
                                                'label': {
                                                    'local': '100483',
                                                    'remote': 'unknown',
                                                },
                                                'mtu': {
                                                    'local': '9198',
                                                    'remote': 'unknown',
                                                },
                                                'control_word': {
                                                    'local': 'enabled',
                                                    'remote': 'unknown',
                                                },
                                                'ac_id': {
                                                    'local': '30294',
                                                    'remote': '20294',
                                                },
                                                'evpn_type': {
                                                    'local': 'Ethernet',
                                                    'remote': 'unknown',
                                                },
                                            },
                                            'create_time': '11/07/2019 13:01:41 (14w6d ago)',
                                            'last_time_status_changed': '11/09/2019 08:03:16 (6w0d ago)',
                                            'statistics': {
                                                'packet_totals': {
                                                    'receive': 0,
                                                    'send': 1809419,
                                                },
                                                'byte_totals': {
                                                    'receive': 0,
                                                    'send': 174143224,
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }

    golden_output7 = {'execute.return_value': '''
        show l2vpn xconnect detail

        Wed Oct 23 13:54:23.929 EDT

        Group vpws, XC vrp_vpws_tor1_bl1_10293, state is unresolved; Interworking none
        Not provisioned reason(s):
            AC I/F not ready

        AC: Bundle-Ether1.59, state is unresolved
        EVPN: neighbor 0.0.0.0, PW ID: evi 10293, ac-id 20293, state is down ( idle )
            XC ID 0xa0000003
            Encapsulation MPLS
            Source address 67.70.219.84
            Encap type unknown, control word unknown
            Sequencing not set
            LSP : Up

            PW Status TLV in use
            EVPN         Local                          Remote                        
            ------------ ------------------------------ -----------------------------
            Label        unassigned                     unknown                       
            MTU          unknown                        unknown                       
            Control word unknown                        unknown                       
            AC ID        30293                          20293                         
            EVPN type    unknown                        unknown                       

            ------------ ------------------------------ -----------------------------
            Create time: 27/08/2019 09:44:55 (8w1d ago)
            No status change since creation

        Group BL-PE-BG, XC G0-0-0-12-200, state is up; Interworking none
        AC: GigabitEthernet0/0/0/12.200, state is up
            Type VLAN; Num Ranges: 1
            Rewrite Tags: []
            VLAN ranges: [200, 200]
            MTU 4474; XC ID 0x200008; interworking none
            Statistics:
            packets: received 0, sent 0
            bytes: received 0, sent 0
            drops: illegal VLAN 0, illegal length 0
        EVPN: neighbor 67.70.219.82, PW ID: evi 2112, ac-id 3001, state is up ( established )
            XC ID 0xa0000005
            Encapsulation MPLS
            Source address 67.70.219.84
            Encap type Ethernet, control word enabled
            Sequencing not set
            LSP : Up

            EVPN         Local                          Remote                        
            ------------ ------------------------------ -----------------------------
            Label        100562                         100002                        
            MTU          4474                           4474                          
            Control word enabled                        enabled                       
            AC ID        1001                           3001                          
            EVPN type    Ethernet                       Ethernet                      

            ------------ ------------------------------ -----------------------------
            Create time: 27/08/2019 09:44:55 (8w1d ago)
            Last time status changed: 22/10/2019 14:50:08 (23:04:15 ago)
            Last time PW went down: 22/10/2019 14:46:56 (23:07:27 ago)
            Statistics:
            packets: received 0, sent 0
            bytes: received 0, sent 0

        Group BL-2-DCPE, XC G0-0-0-12-100, state is up; Interworking none
        AC: GigabitEthernet0/0/0/12.100, state is up
            Type VLAN; Num Ranges: 1
            Rewrite Tags: []
            VLAN ranges: [100, 100]
            MTU 4470; XC ID 0x200006; interworking none
            Statistics:
            packets: received 0, sent 0
            bytes: received 0, sent 0
            drops: illegal VLAN 0, illegal length 0
        PW: neighbor 67.70.219.82, PW ID 8482100, state is up ( established )
            PW class BL-2-DCPE, XC ID 0xa0000007
            Encapsulation MPLS, protocol LDP
            Source address 67.70.219.84
            PW type Ethernet VLAN, control word disabled, interworking none
            PW backup disable delay 0 sec
            Sequencing not set
            LSP : Up

            PW Status TLV in use
            MPLS         Local                          Remote                        
            ------------ ------------------------------ -----------------------------
            Label        100563                         100008                        
            Group ID     0x5c0                          0x1c8                         
            Interface    GigabitEthernet0/0/0/12.100    TenGigE0/0/0/47.100           
            MTU          4470                           4470                          
            Control word disabled                       disabled                      
            PW type      Ethernet VLAN                  Ethernet VLAN                 
            VCCV CV type 0x2                            0x2                           
                        (LSP ping verification)        (LSP ping verification)       
            VCCV CC type 0x6                            0x6                           
                        (router alert label)           (router alert label)          
                        (TTL expiry)                   (TTL expiry)                  
            ------------ ------------------------------ -----------------------------
            Incoming Status (PW Status TLV):
            Status code: 0x0 (Up) in Notification message
            Outgoing Status (PW Status TLV):
            Status code: 0x0 (Up) in Notification message
            MIB cpwVcIndex: 2684354567
            Create time: 27/08/2019 09:44:55 (8w1d ago)
            Last time status changed: 22/10/2019 14:50:02 (23:04:21 ago)
            Last time PW went down: 22/10/2019 14:46:56 (23:07:27 ago)
            Statistics:
            packets: received 0, sent 0
            bytes: received 0, sent 0
    '''}

    golden_parsed_output7 = {
        'group': {
            'vpws': {
                'xc': {
                    'vrp_vpws_tor1_bl1_10293': {
                        'state': 'unresolved',
                        'interworking': 'none',
                        'ac': {
                            'Bundle-Ether1.59': {
                                'state': 'unresolved',
                            },
                        },
                        'evpn': {
                            'neighbor': {
                                '0.0.0.0': {
                                    'id': {
                                        'evi 10293': {
                                            'state': 'down ( idle )',
                                            'ac_id': 20293,
                                            'xc_id': '0xa0000003',
                                            'encapsulation': 'MPLS',
                                            'source_address': '67.70.219.84',
                                            'encap_type': 'unknown',
                                            'control_word': 'unknown',
                                            'sequencing': 'not set',
                                            'lsp': 'Up',
                                            'status_tlv': 'not set',
                                            'evpn': {
                                                'label': {
                                                    'local': 'unassigned',
                                                    'remote': 'unknown',
                                                },
                                                'mtu': {
                                                    'local': 'unknown',
                                                    'remote': 'unknown',
                                                },
                                                'control_word': {
                                                    'local': 'unknown',
                                                    'remote': 'unknown',
                                                },
                                                'ac_id': {
                                                    'local': '30293',
                                                    'remote': '20293',
                                                },
                                                'evpn_type': {
                                                    'local': 'unknown',
                                                    'remote': 'unknown',
                                                },
                                            },
                                            'create_time': '27/08/2019 09:44:55 (8w1d ago)',
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
            'BL-PE-BG': {
                'xc': {
                    'G0-0-0-12-200': {
                        'state': 'up',
                        'interworking': 'none',
                        'ac': {
                            'GigabitEthernet0/0/0/12.200': {
                                'state': 'up',
                                'type': 'VLAN',
                                'num_ranges': 1,
                                'rewrite_tags': '',
                                'vlan_ranges': ['200', '200'],
                                'mtu': 4474,
                                'xc_id': '0x200008',
                                'interworking': 'none',
                                'statistics': {
                                    'packet_totals': {
                                        'receive': 0,
                                        'send': 0,
                                    },
                                    'byte_totals': {
                                        'receive': 0,
                                        'send': 0,
                                    },
                                    'drops': {
                                        'illegal_vlan': 0,
                                        'illegal_length': 0,
                                    },
                                },
                            },
                        },
                        'evpn': {
                            'neighbor': {
                                '67.70.219.82': {
                                    'id': {
                                        'evi 2112': {
                                            'state': 'up ( established )',
                                            'ac_id': 3001,
                                            'xc_id': '0xa0000005',
                                            'encapsulation': 'MPLS',
                                            'source_address': '67.70.219.84',
                                            'encap_type': 'Ethernet',
                                            'control_word': 'enabled',
                                            'sequencing': 'not set',
                                            'lsp': 'Up',
                                            'evpn': {
                                                'label': {
                                                    'local': '100562',
                                                    'remote': '100002',
                                                },
                                                'mtu': {
                                                    'local': '4474',
                                                    'remote': '4474',
                                                },
                                                'control_word': {
                                                    'local': 'enabled',
                                                    'remote': 'enabled',
                                                },
                                                'ac_id': {
                                                    'local': '1001',
                                                    'remote': '3001',
                                                },
                                                'evpn_type': {
                                                    'local': 'Ethernet',
                                                    'remote': 'Ethernet',
                                                },
                                            },
                                            'create_time': '27/08/2019 09:44:55 (8w1d ago)',
                                            'last_time_status_changed': '22/10/2019 14:50:08 (23:04:15 ago)',
                                            'statistics': {
                                                'packet_totals': {
                                                    'receive': 0,
                                                    'send': 0,
                                                },
                                                'byte_totals': {
                                                    'receive': 0,
                                                    'send': 0,
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
            'BL-2-DCPE': {
                'xc': {
                    'G0-0-0-12-100': {
                        'state': 'up',
                        'interworking': 'none',
                        'ac': {
                            'GigabitEthernet0/0/0/12.100': {
                                'state': 'up',
                                'type': 'VLAN',
                                'num_ranges': 1,
                                'rewrite_tags': '',
                                'vlan_ranges': ['100', '100'],
                                'mtu': 4470,
                                'xc_id': '0x200006',
                                'interworking': 'none',
                                'statistics': {
                                    'packet_totals': {
                                        'receive': 0,
                                        'send': 0,
                                    },
                                    'byte_totals': {
                                        'receive': 0,
                                        'send': 0,
                                    },
                                    'drops': {
                                        'illegal_vlan': 0,
                                        'illegal_length': 0,
                                    },
                                },
                            },
                        },
                        'pw': {
                            'neighbor': {
                                '67.70.219.82': {
                                    'id': {
                                        8482100: {
                                            'state': 'up ( established )',
                                            'pw_class': 'BL-2-DCPE',
                                            'xc_id': '0xa0000007',
                                            'encapsulation': 'MPLS',
                                            'protocol': 'LDP',
                                            'source_address': '67.70.219.84',
                                            'backup_disable_delay': 0,
                                            'sequencing': 'not set',
                                            'lsp': 'Up',
                                            'status_tlv': 'not set',
                                            'mpls': {
                                                'label': {
                                                    'local': '100563',
                                                    'remote': '100008',
                                                },
                                                'group_id': {
                                                    'local': '0x5c0',
                                                    'remote': '0x1c8',
                                                },
                                                'interface': {
                                                    'local': 'GigabitEthernet0/0/0/12.100',
                                                    'remote': 'TenGigE0/0/0/47.100',
                                                },
                                                'mtu': {
                                                    'local': '4470',
                                                    'remote': '4470',
                                                },
                                                'control_word': {
                                                    'local': 'disabled',
                                                    'remote': 'disabled',
                                                },
                                                'pw_type': {
                                                    'local': 'Ethernet VLAN',
                                                    'remote': 'Ethernet VLAN',
                                                },
                                                'vccv_cv_type': {
                                                    'local': '0x2',
                                                    'remote': '0x2',
                                                    'local_type': ['LSP ping verification'],
                                                    'remote_type': ['LSP ping verification'],
                                                },
                                                'vccv_cc_type': {
                                                    'local': '0x6',
                                                    'remote': '0x6',
                                                    'local_type': ['router alert label', 'TTL expiry'],
                                                    'remote_type': ['router alert label', 'TTL expiry'],
                                                },
                                            },
                                            'create_time': '27/08/2019 09:44:55 (8w1d ago)',
                                            'last_time_status_changed': '22/10/2019 14:50:02 (23:04:21 ago)',
                                            'statistics': {
                                                'packet_totals': {
                                                    'receive': 0,
                                                    'send': 0,
                                                },
                                                'byte_totals': {
                                                    'receive': 0,
                                                    'send': 0,
                                                },
                                            },
                                        },
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
        self.device = Mock(**self.empty_output)
        obj = ShowL2vpnXconnectDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowL2vpnXconnectDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)
    
    def test_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowL2vpnXconnectDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)
    
    def test_golden3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        obj = ShowL2vpnXconnectDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output3)
    
    def test_golden4(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output4)
        obj = ShowL2vpnXconnectDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output4)
    
    def test_golden5(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output5)
        obj = ShowL2vpnXconnectDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output5)
    
    def test_golden6(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output6)
        obj = ShowL2vpnXconnectDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output6)
    
    def test_golden7(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output7)
        obj = ShowL2vpnXconnectDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output7)

# ==================================================
#  Unit test for 'show l2vpn xconnect summary'
# ==================================================
class TestShowL2vpnXconnectSummary(unittest.TestCase):
    """Unit test for 'show l2vpn xconnect summary' """

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'number_of_groups': {
            'total': 0,
        },
        'number_of_xconnects': {
            'total': 0,
            'up': 0,
            'down': 0,
            'unresolved': 0,
            'partially_programmed': 0,
            'ac_pw': 0,
            'ac_ac': 0,
            'pw_pw': 0,
            'monitor_session_pw': 0,
        },
        'number_of_admin_down_segments': {
            'total': 0,
        },
        'number_of_mp2mp_xconnects': {
            'total': 0,
            'up': 0,
            'down': 0,
            'advertised': 0,
            'non_advertised': 0,
        },
        'number_of_ce_connections': {
            'total': 0,
            'advertised': 0,
            'non_advertised': 0,
        },
        'backup_pw': {
            'configured': 0,
            'up': 0,
            'down': 0,
            'admin_down': 0,
            'unresolved': 0,
            'standby': 0,
            'standby_ready': 0,
        },
        'backup_interface': {
            'configured': 0,
            'up': 0,
            'down': 0,
            'admin_down': 0,
            'unresolved': 0,
            'standby': 0,
        },
    }

    golden_output = {'execute.return_value': '''
        Device#show l2vpn xconnect summary
        Thu Sep 26 11:00:09.210 EDT
        Number of groups: 0
        Number of xconnects: 0
        Up: 0  Down: 0  Unresolved: 0 Partially-programmed: 0
        AC-PW: 0  AC-AC: 0  PW-PW: 0 Monitor-Session-PW: 0
        Number of Admin Down segments: 0
        Number of MP2MP xconnects: 0
        Up 0 Down 0
        Advertised: 0 Non-Advertised: 0
        Number of CE Connections: 0
        Advertised: 0 Non-Advertised: 0
        Backup PW:
        Configured   : 0
        UP           : 0
        Down         : 0
        Admin Down   : 0
        Unresolved   : 0
        Standby      : 0
        Standby Ready: 0
        Backup Interface:
        Configured   : 0
        UP           : 0
        Down         : 0
        Admin Down   : 0
        Unresolved   : 0
        Standby      : 0
        Device#
        '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowL2vpnXconnectSummary(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowL2vpnXconnectSummary(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


# ==================================================
#  Unit test for 'show l2vpn xconnect mp2mp detail'
# ==================================================
class TestShowL2vpnXconnectMp2mpDetail(unittest.TestCase):
    """Unit test for 'show l2vpn xconnect mp2mp detail' """

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'group': {
            'gr1': {
                'mp2mp': {
                    'mp1': {
                        'state': 'up',
                        'vpn_id': 100,
                        'vpn_mtu': 1500,
                        'l2_encapsulation': 'VLAN',
                        'auto_discovery': {
                            'BGP': {
                                'state': 'Advertised',
                                'event_name': 'Service Connected',
                                'route_distinguisher': '(auto) 10.36.3.3:32770',
                            },
                        },
                        'import_route_targets': ['10.16.2.2:100'],
                        'export_route_targets': ['10.16.2.2:100'],
                        'signaling_protocol': {
                            'BGP': {
                                'ce_range': 10,
                            },
                        },
                    },
                },
                'xc': {
                    'mp1.1:2': {
                        'state': 'up',
                        'interworking': 'none',
                        'local_ce_id': 1,
                        'remote_ce_id': 2,
                        'discovery_state': 'Advertised',
                        'ac': {
                            'GigabitEthernet0/1/0/1.1': {
                                'state': 'up',
                                'type': 'VLAN',
                                'num_ranges': 1,
                                'vlan_ranges': ['1', '1'],
                                'mtu': 1500,
                                'xc_id': '0x2000013',
                                'interworking': 'none',
                            },
                        },
                        'pw': {
                            'neighbor': {
                                '10.4.1.1': {
                                    'id': {
                                        65538: {
                                            'state': 'up ( established )',
                                            'pw_class': 'not set',
                                            'xc_id': '0x2000013',
                                            'encapsulation': 'MPLS',
                                            'protocol': 'BGP',
                                            'mpls': {
                                                'label': {
                                                    'local': '16031',
                                                    'remote': '16045',
                                                },
                                                'mtu': {
                                                    'local': '1500',
                                                    'remote': '1500',
                                                },
                                                'control_word': {
                                                    'local': 'enabled',
                                                    'remote': 'enabled',
                                                },
                                                'pw_type': {
                                                    'local': 'Ethernet VLAN',
                                                    'remote': 'Ethernet VLAN',
                                                },
                                                'ce_id': {
                                                    'local': '1',
                                                    'remote': '2',
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }
    
    golden_output = {'execute.return_value': '''
        show l2vpn xconnect mp2mp detail

        Group gr1, MP2MP mp1, state: up

        VPN ID: 100

        VPN MTU: 1500

        L2 Encapsulation: VLAN

        Auto Discovery: BGP, state is Advertised (Service Connected)

            Route Distinguisher: (auto) 10.36.3.3:32770

        Import Route Targets:

            10.16.2.2:100

        Export Route Targets:

            10.16.2.2:100

        Signaling protocol:BGP

            CE Range:10

        Group gr1, XC mp1.1:2, state is up; Interworking none

        Local CE ID: 1, Remote CE ID: 2, Discovery State: Advertised

        AC: GigabitEthernet0/1/0/1.1, state is up

        Type VLAN; Num Ranges: 1

        VLAN ranges: [1, 1]

        MTU 1500; XC ID 0x2000013; interworking none

        PW: neighbor 10.4.1.1, PW ID 65538, state is up ( established )

        PW class not set, XC ID 0x2000013

        Encapsulation MPLS, Auto-discovered (BGP), protocol BGP

            MPLS         Local                         Remote                       

            ------------ ------------------------------ -----------------------------

            Label        16031                          16045                        

            MTU          1500                           1500                        

        Control word     enabled                        enabled                      

            PW type      Ethernet VLAN                  Ethernet VLAN                

            CE-ID        1                              2                            
    '''}
    
    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowL2vpnXconnectMp2mpDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowL2vpnXconnectMp2mpDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

if __name__ == '__main__':
    unittest.main()