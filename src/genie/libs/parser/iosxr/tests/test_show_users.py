
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
from genie.libs.parser.iosxr.show_session import ShowUsers


# ================
# Unit test for:
#   * 'show users'
# ================
class TestShowUsers(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = ''

    golden_parsed_output = {
    "date":"Thu Jan 28 15:14:53.365 UTC",
    "line":{
        "con0/RP0/CPU0":{
            "active":True,
            "user":"admin",
            "service":"hardware",
            "conns":"0",
            "idle":"00:00:00"
        },
        "con1/RP0/CPU0":{
            "active":False,
            "user":"admin",
            "service":"hardware",
            "conns":"0",
            "idle":"00:00:00"
        },
        "con2/RP0/CPU0":{
            "active":False,
            "user":"admin",
            "service":"hardware",
            "conns":"0",
            "idle":"00:00:00",
            "location":"10.20.11.04"
        }
    }
}

    golden_output = '''\
    Thu Jan 28 15:14:53.365 UTC
    Line            User                 Service  Conns   Idle        Location
    *  con0/RP0/CPU0   admin                hardware     0  00:00:00
    con1/RP0/CPU0   admin                hardware     0  00:00:00
    con2/RP0/CPU0   admin                hardware     0  00:00:00    10.20.11.04
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
