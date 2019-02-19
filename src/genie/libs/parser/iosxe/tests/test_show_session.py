#!/bin/env python
import unittest
from unittest.mock import Mock
from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                             SchemaMissingKeyError
from genie.libs.parser.iosxe.show_session import ShowLine,\
                                                ShowUsers


class test_show_line(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': '      '}

    golden_parsed_output = {
        'a': '-',
        'acci': '-',
        'acco': '-',
        'busy': False,
        'day': '13',
        'int': '-',
        'load': {
            'five_min': '33%',
            'five_secs': '52%/0%',
            'one_min': '37%'},
        'modem': '-',
        'month': 'Sep',
        'noise': 0,
        'overruns': '0/0',
        'roty': '-',
        'source': 'NTP',
        'time': '17:11:11.421',
        'tty': '21',
        'type': 'VTY',
        'uses': 0,
        'week_day': 'Tue',
        'year': '2016',
        'zone': 'JST'}

    golden_output = {'execute.return_value': '''\
        Router#show line
        Load for five secs: 52%/0%; one minute: 37%; five minutes: 33%
        Time source is NTP, 17:11:11.421 JST Tue Sep 13 2016

           Tty Typ     Tx/Rx    A Modem  Roty AccO AccI   Uses   Noise  Overruns   Int
              0 CTY              -    -      -    -    -      0       2     0/0       -
              1 AUX   9600/9600  -    -      -    -    -      0       0     0/0       -
        *     2 VTY              -    -      -    -    -      3       0     0/0       -
        *     3 VTY              -    -      -    -    -      8       0     0/0       -
        *     4 VTY              -    -      -    -    -     18       0     0/0       -
        *     5 VTY              -    -      -    -    -      1       0     0/0       -
        *     6 VTY              -    -      -    -    -      3       0     0/0       -
              7 VTY              -    -      -    -    -     10       0     0/0       -
              8 VTY              -    -      -    -    -      6       0     0/0       -
        *     9 VTY              -    -      -    -    -      3       0     0/0       -
             10 VTY              -    -      -    -    -      0       0     0/0       -
             11 VTY              -    -      -    -    -      0       0     0/0       -
             12 VTY              -    -      -    -    -      0       0     0/0       -
             13 VTY              -    -      -    -    -      0       0     0/0       -
             14 VTY              -    -      -    -    -      0       0     0/0       -
             15 VTY              -    -      -    -    -      0       0     0/0       -
             16 VTY              -    -      -    -    -      0       0     0/0       -
             17 VTY              -    -      -    -    -      0       0     0/0       -
             18 VTY              -    -      -    -    -      0       0     0/0       -
             19 VTY              -    -      -    -    -      0       0     0/0       -
             20 VTY              -    -      -    -    -      0       0     0/0       -
             21 VTY              -    -      -    -    -      0       0     0/0       -
    '''
    }

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        line_obj = ShowLine(device=self.device)
        parsed_output = line_obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        line_obj = ShowLine(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = line_obj.parse()


class test_show_users(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': '      '}

    golden_parsed_output = {
        'busy': False,
        'day': '13',
        'host': 'idle',
        'idle': '00:07:09',
        'line': '9 vty 7    ',
        'load': {
            'five_min': '31%',
            'five_secs': '14%/0%',
            'one_min': '23%'},
        'location': '10.241.137.203',
        'month': 'Sep',
        'source': 'NTP',
        'time': '16:53:22.622',
        'user': 'testuser2',
        'week_day': 'Tue',
        'year': '2016',
        'zone': 'JST'}

    golden_output = {'execute.return_value': '''\
        Router#show users
        Load for five secs: 14%/0%; one minute: 23%; five minutes: 31%
        Time source is NTP, 16:53:22.622 JST Tue Sep 13 2016

            Line       User       Host(s)              Idle       Location
           2 vty 0     nos        idle                 00:35:32 10.241.137.203
           3 vty 1     testuser   idle                 00:41:43 10.241.147.155
        *  4 vty 2     testuser   idle                 00:00:07 10.241.146.52
           5 vty 3     testuser   idle                 04:20:29 10.241.137.111
           6 vty 4     user       idle                 00:00:44 10.241.142.37
           9 vty 7     testuser2  idle                 00:07:09 10.241.137.203

          Interface    User               Mode         Idle     Peer Address
    '''
    }

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        users_obj = ShowUsers(device=self.device)
        parsed_output = users_obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        users_obj = ShowUsers(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = users_obj.parse()


if __name__ == '__main__':
    unittest.main()

