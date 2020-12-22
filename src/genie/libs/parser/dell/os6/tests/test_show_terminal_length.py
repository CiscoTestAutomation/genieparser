
# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device
from pyats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                             SchemaMissingKeyError

# iosxe show_ospf
from genie.libs.parser.dell.os6.show_terminal_length import ShowTerminalLength


class test_show_terminal_length(unittest.TestCase):
    '''Unit test for "show terminal length" '''

    device = Device(name='aDevice')
    
    empty_output = {'execute.return_value': ''}
    golden_parsed_output_brief = {'length': 24}

    golden_output_brief = {'execute.return_value': '''
    terminal length................................ 24
    '''}

    def test_show_terminal_length(self):
        self.device = Mock(**self.golden_output_brief)
        obj = ShowTerminalLength(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_brief)

if __name__ == '__main__':
    unittest.main()