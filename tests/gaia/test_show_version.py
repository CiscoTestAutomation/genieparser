#Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

# Parser
from genie.libs.parser.gaia.show_version import ShowVersion

class test_show_version(unittest.TestCase):
    device = Device(name='gw')
    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''\
    Product version Check Point Gaia R80.40
    OS build 294
    OS kernel version 3.10.0-957.21.3cpx86_64
    OS edition 64-bit
    '''}

    golden_parsed_output = {'version': {'product': 'R80.40',
                                        'os': { 'build':'294',
                                                'kernel': '3.10.0-957.21.3cpx86_64', 
                                                'edition':'64-bit'}}}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = ShowVersion(device=self.device1)
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowVersion(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)