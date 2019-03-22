# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

# Parser
from genie.libs.parser.iosxe.show_service_lunzhi import ShowServiceGroupTrafficStats


###################################################
# unit test for show interface stats
####################################################
class test_show_interface_stats(unittest.TestCase):
    """unit test for show interface stats """

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        Router# show service-group traffic-stats 
        Traffic Statistics of service groups:
          Group     Pks In   Bytes In   Pkts Out  Bytes Out
              1          1         22          3         62
              2          0          0          0          0
              3          0          0          0          0
             10          0          0          0          0
             20          0          0          0          0
    '''}

    golden_parsed_output = {
        "group": {
            1: {
                "pkts_in": 1,
                "bytes_in": 22,
                "pkts_out": 3,
                "bytes_out": 62
            },
            2: {
                "pkts_in": 0,
                "bytes_in": 0,
                "pkts_out": 0,
                "bytes_out": 0
            },
            3: {
                "pkts_in": 0,
                "bytes_in": 0,
                "pkts_out": 0,
                "bytes_out": 0
            },
            10: {
                "pkts_in": 0,
                "bytes_in": 0,
                "pkts_out": 0,
                "bytes_out": 0
            },
            20: {
                "pkts_in": 0,
                "bytes_in": 0,
                "pkts_out": 0,
                "bytes_out": 0
            }
        }
    }

    golden_output_group = {'execute.return_value': '''
        Router# show service-group traffic-stats group 1 
        Traffic Statistics of service groups:
          Group    Pkts In   Bytes In   Pkts Out  Bytes Out
              1         78      10548        172      18606
    '''}

    golden_parsed_output_group = {
        "group": {
            1: {
                "pkts_in": 78,
                "bytes_in": 10548,
                "pkts_out": 172,
                "bytes_out": 18606
            }
        }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowServiceGroupTrafficStats(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowServiceGroupTrafficStats(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_show_interfaces(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_group)
        obj = ShowServiceGroupTrafficStats(device=self.device)
        parsed_output = obj.parse(group="group 1")
        self.assertEqual(parsed_output,self.golden_parsed_output_group)


if __name__ == '__main__':
    unittest.main()