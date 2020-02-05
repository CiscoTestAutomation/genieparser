
# Python
import re
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Parser
from genie.libs.parser.nxos.show_checkpoint import ShowCheckpointSummary

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

 
# ========================================
#  Unit test for 'show checkpoint summary'
# ========================================

class test_show_checkpoint_summary(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'checkpoint':
            {'bgp-Wed_May_31_12_56_56_2017':
                {'created_by': 'admin',
                 'created_time': 'Wed, 12:56:56 31 May 2017',
                 'size': 26154,
                 'description': 'None'},
            'system-fm-bfd':
                {'created_by': 'admin',
                 'created_time': 'Mon, 12:41:58 29 May 2017',
                 'size': 26154,
                 'description': 'Created by Feature Manager.'},}}

    golden_output = {'execute.return_value': '''
        1) bgp-Wed_May_31_12_56_56_2017:
        Created by admin
        Created at Wed, 12:56:56 31 May 2017
        Size is 26,154 bytes
        User Checkpoint Summary
        -----------------------------------------------------
        Description: None

        2) system-fm-bfd:
        Created by admin
        Created at Mon, 12:41:58 29 May 2017
        Size is 26,154 bytes
        System Checkpoint Summary
        -----------------------------------------------------
        Description: Created by Feature Manager.

        '''}

    def test_show_checkpoint_summary_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowCheckpointSummary(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_show_checkpoint_summary_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowCheckpointSummary(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

if __name__ == '__main__':
    unittest.main()


# vim: ft=python et sw=4