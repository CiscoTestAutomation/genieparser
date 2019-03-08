# Python
import unittest
from unittest.mock import Mock


# ATS
from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
        SchemaMissingKeyError


# Parser
from genie.libs.parser.iosxe.show_config import ShowConfigurationLock


# ======================================================
# Parser fr 'show configuration lock'
#=======================================================


class test_show_configuration_lock(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'owner': {
            'owner_pid': 578,
            'tty_number': 2,
            'tty_username': 'testuser',
            'user_debug_info': 'CLI Session Lock',
            'lock_active_time_in_sec': 17
        }
    }

    golden_output = {'execute.return_value': '''\
            Config Session Lock
            ---------------------
            Owner PID               : 578
            TTY number              : 2
            TTY username            : testuser
            User debug info         : CLI Session Lock
            Lock Active time (in Sec)   : 17
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


if __name__ == '__main__':
    unittest.main()


