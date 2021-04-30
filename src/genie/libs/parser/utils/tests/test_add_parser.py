import logging
import unittest
from unittest.mock import Mock

from genie.libs.parser.utils import common 
from genie.libs.parser.utils.entry_points import add_parser


class TestAddParser(unittest.TestCase):
    
    def setUp(self):
        try:
            del common.parser_data
        except AttributeError as err:
            logging.warning(err)

    def test_add_parser_command_string(self):
        cli_command = 'show test_add_parser_single_command_string'
        mock_parser = Mock()
        mock_parser.MockParser = Mock(cli_command=cli_command)
        mock_parser.MockParser.__name__ = 'asa.MockParser'
        mock_parser.MockParser.__package__ = 'asa'

        with self.assertRaises(AttributeError):
            getattr(common.parser_data)

        add_parser(parser=mock_parser.MockParser, os_name='asa')

        self.assertIn(cli_command, common.parser_data)

    def test_add_parser_command_iterable(self):
        cli_command = ['show test_add_parser_single_command_iterable1',
                       'show test_add_parser_single_command_iterable2']

        mock_parser = Mock()
        mock_parser.MockParser = Mock(cli_command=cli_command)
        mock_parser.MockParser.__name__ = 'asa.MockParser'
        mock_parser.MockParser.__package__ = 'asa'

        with self.assertRaises(AttributeError):
            getattr(common.parser_data)

        add_parser(parser=mock_parser.MockParser, os_name='asa')

        for cmd in cli_command:
            self.assertIn(cmd, common.parser_data)

if __name__ == '__main__':
    unittest.main()
