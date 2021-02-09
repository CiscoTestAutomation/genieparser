
# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device
from pyats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                             SchemaMissingKeyError

# iosxr traceroute
from genie.libs.parser.nxos.show_users import ShowUsers


# ================
# Unit test for:
#   * 'show users'
# ================
class TestShowUsers(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = ''

    golden_parsed_output = {
        "line":{
            "pts/0":{
                "active":False,
                "name":"admin",
                "time":"Jan 28 13:44",
                "idle":".",
                "pid":"8096",
                "comment":"adding some comments"
            },
            "pts/1":{
                "active":False,
                "name":"admin",
                "time":"Jan 28 13:44",
                "idle":".",
                "pid":"8096"
            },
            "pts/2":{
                "active":True,
                "name":"admin",
                "time":"Jan 28 13:44",
                "idle":".",
                "pid":"8096",
                "comment":"adding some comments "
            }
        }
    }

    golden_output = '''\
    NAME     LINE         TIME         IDLE          PID COMMENT
    admin    pts/0        Jan 28 13:44   .          8096 adding some comments 
    admin    pts/1        Jan 28 13:44   .          8096  
    admin    pts/2        Jan 28 13:44   .          8096 adding some comments *
        '''

    def test_show_users_empty(self):
        obj = ShowUsers(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(output=self.empty_output)

    def test_show_users_golden(self):
        self.maxDiff = None
        obj = ShowUsers(device=self.device)
        parsed_output = obj.parse(output=self.golden_output)
        self.assertEqual(parsed_output, self.golden_parsed_output)

if __name__ == '__main__':
    unittest.main()
