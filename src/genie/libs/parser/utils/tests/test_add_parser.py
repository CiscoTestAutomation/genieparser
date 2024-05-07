import logging
import unittest
import pkg_resources
from unittest.mock import Mock, patch

from genie.libs.parser.utils import common


class TestAddParser(unittest.TestCase):

    def setUp(self):
        common.parser_data = None

    def test_add_parser_command_string(self):
        cli_command = 'show test_add_parser_single_command_string'
        mock_parser = Mock()
        mock_parser.MockParser = Mock(cli_command=cli_command)
        mock_parser.MockParser.__name__ = 'asa.MockParser'
        mock_parser.MockParser.__package__ = 'asa'
        mock_package = Mock()
        mock_package.load().return_value = {'asa': [mock_parser.MockParser]}

        self.assertIsNone(common.parser_data)

        with patch.object(pkg_resources, 'iter_entry_points') as mock_entrypoints:
            mock_entrypoints.return_value = [mock_package]
            common._load_parser_json()

        self.assertIn(cli_command, common.parser_data)

    def test_add_parser_command_iterable(self):
        cli_command = ['show test_add_parser_single_command_iterable1',
                       'show test_add_parser_single_command_iterable2']

        mock_parser = Mock()
        mock_parser.MockParser = Mock(cli_command=cli_command)
        mock_parser.MockParser.__name__ = 'asa.MockParser'
        mock_parser.MockParser.__package__ = 'asa'
        mock_package = Mock()
        mock_package.load().return_value = {'asa': [mock_parser.MockParser]}

        self.assertIsNone(common.parser_data)

        with patch.object(pkg_resources, 'iter_entry_points') as mock_entrypoints:
            mock_entrypoints.return_value = [mock_package]
            common._load_parser_json()

        for cmd in cli_command:
            self.assertIn(cmd, common.parser_data)

if __name__ == '__main__':
    unittest.main()
