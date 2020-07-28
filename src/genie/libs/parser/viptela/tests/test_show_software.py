# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
    SchemaMissingKeyError

# Parser
from genieparser.src.genie.libs.parser.viptela.show_software import ShowSoftware


# ============================================
# Parser for the following commands
#   * 'show bfd connections'
# ============================================
class TestShowSoftware(unittest.TestCase):
    device = Device(name='aDevice')
    maxDiff = None
    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        vEdge# show software | tab
        VERSION         ACTIVE  DEFAULT  PREVIOUS  CONFIRMED  TIMESTAMP
        ---------------------------------------------------------------------------------
        17.2.01.0.12    false   false    true      user       2020-03-30T02:15:00-00:00
        17.2.01.0.32    true    false    false     user       2020-04-11T09:43:37-00:00
        17.2.02.0.1857  false   true     false     auto       2020-03-30T02:13:24-00:00     
    '''}

    golden_parsed_output = {
        '17.2.01.0.12': {'ACTIVE': 'false',
                  'CONFIRMED': 'user',
                  'DEFAULT': 'false',
                  'PREVIOUS': 'true',
                  'TIMESTAMP': '2020-03-30T02:15:00-00:00',
                  'VERSION': '17.2.01.0.12'},
        '17.2.01.0.32': {'ACTIVE': 'true',
                  'CONFIRMED': 'user',
                  'DEFAULT': 'false',
                  'PREVIOUS': 'false',
                  'TIMESTAMP': '2020-04-11T09:43:37-00:00',
                  'VERSION': '17.2.01.0.32'},
        '17.2.02.0.1857': {'ACTIVE': 'false',
                    'CONFIRMED': 'auto',
                    'DEFAULT': 'true',
                    'PREVIOUS': 'false',
                    'TIMESTAMP': '2020-03-30T02:13:24-00:00',
                    'VERSION': '17.2.02.0.1857'}
 }
    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowSoftware(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowSoftware(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == '__main__':
    unittest.main()
