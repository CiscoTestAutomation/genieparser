import unittest
from unittest.mock import Mock

from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError

from genie.libs.parser.iosxe.show_eigrp import ShowEigrpNeighbors

class test_show_eigrp_neighbors(unittest.TestCase):

    device = Device(name='aDevice')

    expected_parsed_output_1 = {}
    expected_parsed_output_2 = {}
    expected_parsed_output_3 = {}

    device_output_1 = {'execute.return_value': '''

        H   Address      Interface  Hold  Uptime    SRTT   RTO    Q   Seq
                                    (sec)           (ms)          Cnt Num
        0   10.1.1.2     Gi0/0      13    00:00:03  1996   5000   0   5
    '''}

    device_output_2 = {'execute.return_value': '''
        H   Address      Interface  Hold  Uptime    SRTT   RTO    Q   Seq
                                    (sec)           (ms)          Cnt Num        
        2   10.1.1.9     Gi0/0      14    00:02:24  206    5000   0   5        
    '''}

    device_output_3 = {'execute.return_value': '''
        H   Address      Interface  Hold  Uptime    SRTT   RTO    Q   Seq
                                    (sec)           (ms)          Cnt Num
        1   10.1.2.3     Gi0/1      11    00:20:39  2202   5000   0   5
    '''}


    def test_show_eigrp_neighbors_1(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output_1)
        obj = ShowCdpNeighbors(device=self.device)        
        parsed_output = obj.parse()        
        self.assertEqual(parsed_output, self.expected_parsed_output_1)
    