# Python
import unittest
from unittest.mock import Mock
from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError

from genie.libs.parser.iosxr.show_xconnect import ShowL2VpnXconnect


# ==================================================
#  Unit test for 'show l2vpn xconnect'
# ==================================================

class test_show_l2vpn_xconnect(unittest.TestCase):
    """Unit test for 'show l2vpn xconnect' """

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {'groups':
            {'Test_XCONN_Group2':
				{'Name':
					{'3000': {'s0': 'UR',
							  'segment_1':
								{'Gi0/0/0/5.3000':
							 		{'s1': 'UR',
							 		 'segment_2':
							 			{'1.1.1.206       3000':
							 				{'s2': 'DN'}
							 			}
							 		}
							 	}
							 }
					}
				},
			'Test_XCONN_Group':
				{'Name':
					{'2000': {'s0': 'DN',
							  'segment_1':
								{'Gi0/0/0/5.2000':
					 				{'s1': 'UP',
					 				 'segment_2':
					 					{'1.1.1.206       2000':
					 						{'s2': 'DN'}
					 					}
					 				}
					 			}
						 	},
				 	 '1000': {'s0': 'DN',
				 	 		  'segment_1':
				 	 		    {'Gi0/0/0/5.1000':
				 		 			{'s1': 'UP',
				 		 			 'segment_2':
				 		 				{'1.1.1.206       1000':
				 		 					{'s2': 'DN'}
				 		 				}
				 		 			}
				 		 		}
				 		 	  }
				 	}
				}
			}
    }

    golden_output = {'execute.return_value': '''
    XRv01_NUC# show l2vpn xconnect
    Legend: ST = State, UP = Up, DN = Down, AD = Admin Down, UR = Unresolved,
            SB = Standby, SR = Standby Ready, (PP) = Partially Programmed
     XConnect                   Segment 1                       Segment 2                
    Group      Name     ST   Description       ST   Description            ST
    ----------------------   --------------------   ---------------------------
    Test_XCONN_Group
               1000     DN   Gi0/0/0/5.1000    UP   1.1.1.206       1000   DN
    ---------------------------------------------------------------------------
    Test_XCONN_Group
               2000     DN   Gi0/0/0/5.2000    UP   1.1.1.206       2000   DN    
    ---------------------------------------------------------------------------
    Test_XCONN_Group2
               3000     UR   Gi0/0/0/5.3000    UR   1.1.1.206       3000   DN
    ---------------------------------------------------------------------------
        '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowL2VpnXconnect(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowL2VpnXconnect(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == '__main__':
    unittest.main()