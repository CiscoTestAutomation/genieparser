# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                             SchemaMissingKeyError

# Parser
from genie.libs.parser.iosxe.show_sdwan_software import ShowSdwanSoftware


# ============================================
# Parser for the following commands
#   * 'show sdwan software'
# ============================================
class TestShowSdwanSoftware(unittest.TestCase):
    device = Device(name='aDevice')
    maxDiff = None 
    empty_output = {'execute.return_value' : ''}
    golden_output = {'execute.return_value': '''
        vEdge# show sdwan software
        VERSION         ACTIVE  DEFAULT  PREVIOUS  CONFIRMED  TIMESTAMP
        ---------------------------------------------------------------------------------
        17.2.01.0.12    false   false    true      user       2020-03-30T02:15:00-00:00
        17.2.01.0.32    true    false    false     user       2020-04-11T09:43:37-00:00
        17.2.02.0.1857  false   true     false     auto       2020-03-30T02:13:24-00:00

        Total Space:387M Used Space:141M Available Space:241M     
    '''}

    golden_parsed_output = {'version': {
                '17.2.01.0.12': {'active': 'false',
                            'confirmed': 'user',
                            'default': 'false',
                            'previous': 'true',
                            'timestamp': '2020-03-30T02:15:00-00:00'},
                '17.2.01.0.32': {'active': 'true',
                            'confirmed': 'user',
                            'default': 'false',
                            'previous': 'false',
                            'timestamp': '2020-04-11T09:43:37-00:00'},
                '17.2.02.0.1857': {'active': 'false',
                            'confirmed': 'auto',
                            'default': 'true',
                            'previous': 'false',
                            'timestamp': '2020-03-30T02:13:24-00:00'}
                        }
                    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowSdwanSoftware(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()
    
    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowSdwanSoftware(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

if __name__ == '__main__':
		unittest.main()        