# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                             SchemaMissingKeyError

# Parser
from genie.libs.parser.viptela.show_bfd_summary import ShowBfdSummary


# ============================================
# Parser for the following commands
#   * 'show bfd summary'
# ============================================
class TestShowBfdSummary(unittest.TestCase):
    device = Device(name='aDevice')
    maxDiff = None 
    empty_output = {'execute.return_value' : ''}

    golden_output = {'execute.return_value': '''
        # show bfd summary
        sessions-total         4
        sessions-up            4
        sessions-max           4
        sessions-flap          4
        poll-interval          600000
    '''}

    golden_parsed_output = {
        'poll_interval': '600000',
        'sessions_flap': '4',
        'sessions_max': '4',
        'sessions_total': '4',
        'sessions_up': '4'
        }


    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowBfdSummary(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()
    
    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowBfdSummary(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


if __name__ == '__main__':
		unittest.main()       