import re
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Parser
from genie.libs.parser.nxos.show_track import ShowTrack

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# =================================
# Unit test for 'show track'
# =================================
class test_show_track(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        "track": {
           1: {
               "type": "IPv6 Route",
               "instance": "10:1::1:2/32",
               "subtrack": "Reachability",
               "state": "DOWN",
               "change_count": 1,
               "last_change": "1w2d"
            }
        }
    }

    golden_output = {'execute.return_value': '''\
        Track 1
          IPv6 Route 10:1::1:2/32 Reachability
          Reachability is DOWN
          1 changes, last change 1w2d
    '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowTrack(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowTrack(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


if __name__ == '__main__':
    unittest.main()



