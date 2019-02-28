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

    golden_parsed_output = {'tty': {'0': {'a': '-',
               'acci': '-',
               'acco': '-',
               'active': False,
               'int': '-',
               'modem': '-',
               'noise': 2,
               'overruns': '0/0',
               'roty': '-',
               'type': 'CTY',
               'uses': 0},
         '1': {'a': '-',
               'acci': '-',
               'acco': '-',
               'active': False,
               'int': '-',
               'modem': '-',
               'noise': 0,
               'overruns': '0/0',
               'roty': '-',
               'type': 'AUX',
               'uses': 0},
         '10': {'a': '-',
                'acci': '-',
                'acco': '-',
                'active': False,
                'int': '-',
                'modem': '-',
                'noise': 0,
                'overruns': '0/0',
                'roty': '-',
                'type': 'VTY',
                'uses': 0},
         '11': {'a': '-',
                'acci': '-',
                'acco': '-',
                'active': False,
                'int': '-',
                'modem': '-',
                'noise': 0,
                'overruns': '0/0',
                'roty': '-',
                'type': 'VTY',
                'uses': 0},
         '12': {'a': '-',
                'acci': '-',
                'acco': '-',
                'active': False,
                'int': '-',
                'modem': '-',
                'noise': 0,
                'overruns': '0/0',
                'roty': '-',
                'type': 'VTY',
                'uses': 0},
         '13': {'a': '-',
                'acci': '-',
                'acco': '-',
                'active': False,
                'int': '-',
                'modem': '-',
                'noise': 0,
                'overruns': '0/0',
                'roty': '-',
                'type': 'VTY',
                'uses': 0},
         '14': {'a': '-',
                'acci': '-',
                'acco': '-',
                'active': False,
                'int': '-',
                'modem': '-',
                'noise': 0,
                'overruns': '0/0',
                'roty': '-',
                'type': 'VTY',
                'uses': 0},
         '15': {'a': '-',
                'acci': '-',
                'acco': '-',
                'active': False,
                'int': '-',
                'modem': '-',
                'noise': 0,
                'overruns': '0/0',
                'roty': '-',
                'type': 'VTY',
                'uses': 0},
         '16': {'a': '-',
                'acci': '-',
                'acco': '-',
                'active': False,
                'int': '-',
                'modem': '-',
                'noise': 0,
                'overruns': '0/0',
                'roty': '-',
                'type': 'VTY',
                'uses': 0},
         '17': {'a': '-',
                'acci': '-',
                'acco': '-',
                'active': False,
                'int': '-',
                'modem': '-',
                'noise': 0,
                'overruns': '0/0',
                'roty': '-',
                'type': 'VTY',
                'uses': 0},
         '18': {'a': '-',
                'acci': '-',
                'acco': '-',
                'active': False,
                'int': '-',
                'modem': '-',
                'noise': 0,
                'overruns': '0/0',
                'roty': '-',
                'type': 'VTY',
                'uses': 0},
         '19': {'a': '-',
                'acci': '-',
                'acco': '-',
                'active': False,
                'int': '-',
                'modem': '-',
                'noise': 0,
                'overruns': '0/0',
                'roty': '-',
                'type': 'VTY',
                'uses': 0},
         '2': {'a': '-',
               'acci': '-',
               'acco': '-',
               'active': True,
               'int': '-',
               'modem': '-',
               'noise': 0,
               'overruns': '0/0',
               'roty': '-',
               'type': 'VTY',
               'uses': 3},
         '20': {'a': '-',
                'acci': '-',
                'acco': '-',
                'active': False,
                'int': '-',
                'modem': '-',
                'noise': 0,
                'overruns': '0/0',
                'roty': '-',
                'type': 'VTY',
                'uses': 0},
         '21': {'a': '-',
                'acci': '-',
                'acco': '-',
                'active': False,
                'int': '-',
                'modem': '-',
                'noise': 0,
                'overruns': '0/0',
                'roty': '-',
                'type': 'VTY',
                'uses': 0},
         '3': {'a': '-',
               'acci': '-',
               'acco': '-',
               'active': True,
               'int': '-',
               'modem': '-',
               'noise': 0,
               'overruns': '0/0',
               'roty': '-',
               'type': 'VTY',
               'uses': 8},
         '4': {'a': '-',
               'acci': '-',
               'acco': '-',
               'active': True,
               'int': '-',
               'modem': '-',
               'noise': 0,
               'overruns': '0/0',
               'roty': '-',
               'type': 'VTY',
               'uses': 18},
         '5': {'a': '-',
               'acci': '-',
               'acco': '-',
               'active': True,
               'int': '-',
               'modem': '-',
               'noise': 0,
               'overruns': '0/0',
               'roty': '-',
               'type': 'VTY',
               'uses': 1},
         '6': {'a': '-',
               'acci': '-',
               'acco': '-',
               'active': True,
               'int': '-',
               'modem': '-',
               'noise': 0,
               'overruns': '0/0',
               'roty': '-',
               'type': 'VTY',
               'uses': 3},
         '7': {'a': '-',
               'acci': '-',
               'acco': '-',
               'active': False,
               'int': '-',
               'modem': '-',
               'noise': 0,
               'overruns': '0/0',
               'roty': '-',
               'type': 'VTY',
               'uses': 10},
         '8': {'a': '-',
               'acci': '-',
               'acco': '-',
               'active': False,
               'int': '-',
               'modem': '-',
               'noise': 0,
               'overruns': '0/0',
               'roty': '-',
               'type': 'VTY',
               'uses': 6},
         '9': {'a': '-',
               'acci': '-',
               'acco': '-',
               'active': True,
               'int': '-',
               'modem': '-',
               'noise': 0,
               'overruns': '0/0',
               'roty': '-',
               'type': 'VTY',
               'uses': 3}}}

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

    golden_parsed_output = {'line': {'2 vty 0': {'active': False,
                      'host': 'idle',
                      'idle': '00:35:32',
                      'location': '10.0.0.1',
                      'user': 'nos'},
          '3 vty 1': {'active': False,
                      'host': 'idle',
                      'idle': '00:41:43',
                      'location': '10.0.0.2',
                      'user': 'testuser'},
          '4 vty 2': {'active': True,
                      'host': 'idle',
                      'idle': '00:00:07',
                      'location': '10.0.0.3',
                      'user': 'testuser'},
          '5 vty 3': {'active': False,
                      'host': 'idle',
                      'idle': '04:20:29',
                      'location': '10.0.0.4',
                      'user': 'testuser'},
          '6 vty 4': {'active': False,
                      'host': 'idle',
                      'idle': '00:00:44',
                      'location': '10.0.0.5',
                      'user': 'user'}}}

    golden_output = {'execute.return_value': '''\
        Router#show users
        Load for five secs: 14%/0%; one minute: 23%; five minutes: 31%
        Time source is NTP, 16:53:22.622 JST Tue Sep 13 2016

            Line       User       Host(s)              Idle       Location
           2 vty 0     nos        idle                 00:35:32 10.0.0.1
           3 vty 1     testuser   idle                 00:41:43 10.0.0.2
        *  4 vty 2     testuser   idle                 00:00:07 10.0.0.3
           5 vty 3     testuser   idle                 04:20:29 10.0.0.4
           6 vty 4     user       idle                 00:00:44 10.0.0.5

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

