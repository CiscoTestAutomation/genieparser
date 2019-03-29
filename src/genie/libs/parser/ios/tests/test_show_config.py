# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

from genie.libs.parser.iosxe.tests.test_show_config \
                                      import test_show_configuration_lock as \
                                             test_show_configuration_lock_iosxe

# Parser
from genie.libs.parser.ios.show_config import ShowConfigurationLock


# ======================================================
# Parser for 'show configuration lock'
#=======================================================
class test_show_configuration_lock(test_show_configuration_lock_iosxe):

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowConfigurationLock(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowConfigurationLock(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

class test_show_configuration_lock_ios(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''\
        Parser Configure Lock
        ---------------------
        Owner PID : 3
        User : unknown
        TTY : 0
        Type : EXCLUSIVE
        State : LOCKED
        Class : EXPOSED
        Count : 1
        Pending Requests : 0
        User debug info : configure terminal

        Parser Configure Lock
        ---------------------
        Owner PID : -1
        User : unknown
        TTY : -1
        Type : NO LOCK
        State : FREE
        Class : unknown
        Count : 0
        Pending Requests : 0
        User debug info :

        Parser Configure Lock
        ------------------------------------------------------
        Owner PID                         : 3
        User                              : unknown
        TTY                               : 0
        Type                              : EXCLUSIVE
        State                             : LOCKED
        Class                             : EXPOSED
        Count                             : 1
        Pending Requests                  : 0
        User debug info                   : configure terminal
        Session idle state                : TRUE
        No of exec cmds getting executed  : 0
        No of exec cmds blocked           : 0
        Config wait for show completion   : FALSE
        Remote ip address                 : Unknown
        Lock active time (in Sec)         : 6
        Lock Expiration timer (in Sec)    : 593

        Parser Configure Lock
        Owner PID        :  10
        User             :  User1
        TTY              :  3
        Type             :  EXCLUSIVE
        State            :  LOCKED
        Class            :  Exposed
        Count            :  0
        Pending Requests :  0
        User debug info  :  0
            '''}

    golden_parsed_output = {
        'parser_configure_lock': {
            'owner_pid': {
                3: {
                    'user': 'unknown',
                    'tty': 0,
                    'type': 'EXCLUSIVE',
                    'state': 'LOCKED',
                    'class': 'EXPOSED',
                    'count': 1,
                    'pending_requests': 0,
                    'user_debug_info': 'configure terminal',
                    'session_idle_state': 'TRUE',
                    'num_of_exec_cmds_executed': 0,
                    'num_of_exec_cmds_blocked': 0,
                    'config_wait_for_show_completion': 'FALSE',
                    'remote_ip_address': 'Unknown',
                    'lock_active_time_in_sec': 6,
                    'lock_expiration_timer_in_sec': 593,
                    },
                -1: {
                    'user': 'unknown',
                    'tty': -1,
                    'type': 'NO LOCK',
                    'state': 'FREE',
                    'class': 'unknown',
                    'count': 0,
                    'pending_requests': 0,
                    },
                10: {
                    'user': 'User1',
                    'tty': 3,
                    'type': 'EXCLUSIVE',
                    'state': 'LOCKED',
                    'class': 'Exposed',
                    'count': 0,
                    'pending_requests': 0,
                    'user_debug_info': '0',
                    },
                },
            },
        }
    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowConfigurationLock(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowConfigurationLock(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)
if __name__ == '__main__':
    unittest.main()
