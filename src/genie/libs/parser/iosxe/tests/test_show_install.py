#!/bin/env python
import unittest

from unittest.mock import Mock
from pyats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                       SchemaMissingKeyError
from genie.libs.parser.iosxe.show_install import (ShowInstallSummary)


class TestShowInstallSummary(unittest.TestCase):
    dev = Device(name='dev')
    empty_output = {'execute.return_value': '      '}

    golden_parsed_output = {
        1: {
            'filename_version': 'bootflash:utah.bm.smu.may15.bin',
            'state': 'U',
            'type': 'SMU'},
        2: {
            'filename_version': '17.1.1.0.66982', 
            'state': 'C', 'type': 'IMG'
            },
        'auto_abort_timer': 'active on install_activate',
        'time_before_rollback': '01:49:42'}

    golden_output = {'execute.return_value': '''\
        Router#show install summary
        [ R0 ] Installed Package(s) Information:
        State (St): I - Inactive, U - Activated & Uncommitted,
                    C - Activated & Committed, D - Deactivated & Uncommitted
        --------------------------------------------------------------------------------
        Type  St   Filename/Version
        --------------------------------------------------------------------------------
        SMU   U    bootflash:utah.bm.smu.may15.bin
        IMG   C    17.1.1.0.66982

        --------------------------------------------------------------------------------
        Auto abort timer: active on install_activate, time before rollback - 01:49:42
        --------------------------------------------------------------------------------

        '''}
    
    def test_empty(self):
        self.dev = Mock(**self.empty_output)
        obj = ShowInstallSummary(device=self.dev)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.dev = Mock(**self.golden_output)
        obj = ShowInstallSummary(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

if __name__ == '__main__':
    unittest.main()

