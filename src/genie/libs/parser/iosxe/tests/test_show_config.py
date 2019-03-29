# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
        SchemaMissingKeyError

# Parser
from genie.libs.parser.iosxe.show_config import ShowConfigurationLock

# ======================================================
# Parser for 'show configuration lock'
#=======================================================
class test_show_configuration_lock(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {
        'config_session_lock': {
	    'owner_pid': { 
                578: {
                    'tty_number': 2,
                    'tty_username': 'testuser',
                    'user_debug_info': 'CLI Session Lock',
                    'lock_active_time_in_sec': 17
                },
                5781: {
                    'tty_number': 21,
                    'tty_username': 'testuser1',
                    'user_debug_info': 'CLI Session Lock',
                    'lock_active_time_in_sec': 171
                }
            }
        }
    }

    golden_parsed_output_optional = {
	'config_session_lock': {
	    'owner_pid': {
            	578: {
                    'tty_number': 2,
                    'tty_username': 'testuser',
                    'user_debug_info': 'CLI Session Lock',
                    'lock_active_time_in_sec': 17
                }
            }
        },
        'parser_configure_lock': {
            'owner_pid': {
                10: {
		    'user': 'User1',
		    'tty': 3,
		    'type': 'EXCLUSIVE',
		    'state': 'LOCKED',
		    'class': 'Exposed',
		    'count': 0,
		    'pending_requests': 0,
		    'user_debug_info': '0'
                },
                11 : {
		    'user': 'User11',
		    'tty': 31,
		    'type': 'EXCLUSIVE',
		    'state': 'LOCKED',
		    'class': 'Exposed',
		    'count': 0,
		    'pending_requests': 0,
		    'user_debug_info': '0'
                }
	    }
	}
    } 

    golden_output = {'execute.return_value': '''\
            Config Session Lock
            ---------------------
            Owner PID   : 578
            TTY number  : 2
            TTY username    : testuser
            User debug info : CLI Session Lock
            Lock Active time (in Sec)   : 17
            Owner PID   : 5781
            TTY number  : 21
            TTY username    : testuser1
            User debug info : CLI Session Lock
            Lock Active time (in Sec)   : 171
            '''}
    
    golden_output_optional = {'execute.return_value': '''\
            Config Session Lock
            ---------------------
            Owner PID   : 578
            TTY number  : 2
            TTY username    : testuser
            User debug info : CLI Session Lock
            Lock Active time (in Sec)   : 17
            Parser Configure Lock
            Owner PID           : 10
            User                :   User1
            TTY                 :   3
            Type                :   EXCLUSIVE
            State               :   LOCKED
            Class               :   Exposed
            Count               :   0
            Pending Requests    :   0
            User debug info     :   0
            Owner PID           : 11
            User                : User11
            TTY                 : 31
            Type                : EXCLUSIVE
            State               : LOCKED
            Class               : Exposed
            Count               : 0
            Pending Requests    : 0
            User debug info     : 0
            '''}

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
    
    def test_golden_optional(self):
        self.device = Mock(**self.golden_output_optional)
        obj = ShowConfigurationLock(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_optional)

if __name__ == '__main__':
    unittest.main()


