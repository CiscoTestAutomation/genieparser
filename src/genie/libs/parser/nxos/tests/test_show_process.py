
# Python
import re
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Parser
from genie.libs.parser.nxos.show_process import ShowProcesses

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# ====================================================================
# Parser for 'show processes'
# ====================================================================

class test_show_proceese(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        "process": {
              "kworker/0:0": {
                   "pid": {
                        4: {
                             "start_cnt": 1,
                             "pid": 4,
                             "type": "O",
                             "process": "kworker/0:0",
                             "pc": "0",
                             "state": "S"
                        }
                   }
              },
              "dbus-daemon": {
                   "pid": {
                        26675: {
                             "start_cnt": 1,
                             "pid": 26675,
                             "type": "O",
                             "process": "dbus-daemon",
                             "pc": "9c608843",
                             "state": "S"
                        }
                   }
              },
              "ksoftirqd/1": {
                   "pid": {
                        10: {
                             "start_cnt": 1,
                             "pid": 10,
                             "type": "O",
                             "process": "ksoftirqd/1",
                             "pc": "0",
                             "state": "S"
                        }
                   }
              },
              "init": {
                   "pid": {
                        1: {
                             "start_cnt": 1,
                             "pid": 1,
                             "type": "O",
                             "process": "init",
                             "pc": "b8dffed3",
                             "state": "S"
                        }
                   }
              },
              "rsyslogd": {
                   "pid": {
                        26668: {
                             "start_cnt": 1,
                             "pid": 26668,
                             "type": "O",
                             "process": "rsyslogd",
                             "pc": "cbdcd9b3",
                             "state": "S"
                        }
                   }
              },
              "agetty": {
                   "pid": {
                        26687: {
                             "start_cnt": 1,
                             "pid": 26687,
                             "tty": 0,
                             "type": "O",
                             "process": "agetty",
                             "pc": "e4385a40",
                             "state": "S"
                        }
                   }
              },
              "ldap": {
                   "start_cnt": 0,
                   "process": "ldap",
                   "type": "X",
                   "state": "NR"
              }
         }
    }

    golden_output = {'execute.return_value': '''
        N95_1# show processes

        PID    State  PC        Start_cnt    TTY   Type  Process
        -----  -----  --------  -----------  ----  ----  -------------
            1      S  b8dffed3            1     -     O  init
            4      S         0            1     -     O  kworker/0:0
           10      S         0            1     -     O  ksoftirqd/1
        26668      S  cbdcd9b3            1     -     O  rsyslogd
        26675      S  9c608843            1     -     O  dbus-daemon
        26687      S  e4385a40            1     0     O  agetty
            -     NR         -            0     -     X  ldap

        State: R(runnable), S(sleeping), Z(defunct)

        Type:  U(unknown), O(non sysmgr)
               VL(vdc-local), VG(vdc-global), VU(vdc-unaware)
               NR(not running), ER(terminated etc)

        '''}

    def test_show_proceese_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowProcesses(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_show_proceese_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowProcesses(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

if __name__ == '__main__':
    unittest.main()


# vim: ft=python et sw=4