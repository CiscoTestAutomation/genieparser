# Python
import re
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# Parser
from genie.libs.parser.linux.ps import Ps
 

# ===============
# Unit tests for:
#   'ps -ef'
# ===============
class test_ps(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {
        'ps': {
            '0': {
                'uid': 'root',
                'pid': '1',
                'ppid': '0',
                'c': '0',
                'stime': '2019',
                'tty': '?',
                'time': '00:03:36',
                'cmd': '/sbin/init'
            },
            '1': {
                'uid': 'root',
                'pid': '2',
                'ppid': '0',
                'c': '0',
                'stime': '2019',
                'tty': '?',
                'time': '00:00:07',
                'cmd': '[kthreadd]'
            },
            '2': {
                'uid': 'root',
                'pid': '1774',
                'ppid': '1730',
                'c': '0',
                'stime': '2019',
                'tty': '?',
                'time': '00:00:00',
                'cmd': 'hald-addon-input: Listening on /dev/input/event2 /dev/input/event0'
            },
            '3': {
                'uid': '68',
                'pid': '1781',
                'ppid': '1730',
                'c': '0',
                'stime': '2019',
                'tty': '?',
                'time': '00:00:00',
                'cmd': 'hald-addon-acpi: listening on acpid socket /var/run/acpid.socket'
            }
        }
    }

    golden_output = {'execute.return_value': '''
        UID        PID  PPID  C STIME TTY          TIME CMD       
        root         1     0  0  2019 ?        00:03:36 /sbin/init
        root         2     0  0  2019 ?        00:00:07 [kthreadd]                  
        root      1774  1730  0  2019 ?        00:00:00 hald-addon-input: Listening on /dev/input/event2 /dev/input/event0  
        68        1781  1730  0  2019 ?        00:00:00 hald-addon-acpi: listening on acpid socket /var/run/acpid.socket
    '''}

    def test_ps_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = Ps(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_ps_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = Ps(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

if __name__ == '__main__':
    unittest.main()
