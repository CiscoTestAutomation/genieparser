
# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Genie
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError
from genie.libs.parser.ios.show_issu import ShowIssuStateDetail,\
                                              ShowIssuRollbackTimer


# =======================================
#  Unit test for 'show issu state detail'
# =======================================
class test_show_issu_state_detail(unittest.TestCase):

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    semi_empty_output = {'execute.return_value': '''
        Router# show issu state detail
 
        --- Starting installation state synchronization ---
        Finished installation state synchronization
        No ISSU operation is in progress
    '''}

    golden_output = {'execute.return_value': '''
        R1#show issu state detail
        --- Starting local lock acquisition on switch 1 ---
        Finished local lock acquisition on switch 1

        No ISSU operation is in progress
        '''}

    golden_parsed_output = {
        'slot':
            {'1':
                {'issu_in_progress': False}}}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIssuStateDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_semi_empty(self):
        self.device = Mock(**self.semi_empty_output)
        obj = ShowIssuStateDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowIssuStateDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)
        

if __name__ == '__main__':
    unittest.main()
