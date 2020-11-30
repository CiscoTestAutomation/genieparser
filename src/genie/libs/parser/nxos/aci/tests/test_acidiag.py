
import unittest
from unittest.mock import Mock
from pyats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError

from genie.libs.parser.nxos.aci.acidiag import AcidiagFnvread


class TestAcidiagFnvread(unittest.TestCase):
    dev = Device(name='aci')
    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': """\
      ID   Pod ID                 Name    Serial Number         IP Address    Role        State   LastUpdMsgId
--------------------------------------------------------------------------------------------------------------
     101        1        hw_leaf1_II23      FDO20521053     10.0.152.66/32    leaf         active   0
     102        1        hw_leaf2_II23      FDO23151BX4     10.0.152.64/32    leaf         active   0
     201        1       hw_spine1_II23      FDO221425X6     10.0.152.65/32   spine         active   0
    """}

    golden_parsed_output = {
        'id': {
            101: {
                'ip_address': '10.0.152.66/32',
                'last_upd_msg_id': 0,
                'name': 'hw_leaf1_II23',
                'pod_id': 1,
                'role': 'leaf',
                'serial_number': 'FDO20521053',
                'state': 'active'
            },
            102: {
                'ip_address': '10.0.152.64/32',
                'last_upd_msg_id': 0,
                'name': 'hw_leaf2_II23',
                'pod_id': 1,
                'role': 'leaf',
                'serial_number': 'FDO23151BX4',
                'state': 'active'
            },
            201: {
                'ip_address': '10.0.152.65/32',
                'last_upd_msg_id': 0,
                'name': 'hw_spine1_II23',
                'pod_id': 1,
                'role': 'spine',
                'serial_number': 'FDO221425X6',
                'state': 'active'
            }
        }
    }

    def test_empty(self):
        self.dev = Mock(**self.empty_output)
        obj = AcidiagFnvread(device=self.dev)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output)
        obj = AcidiagFnvread(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == '__main__':
    unittest.main()