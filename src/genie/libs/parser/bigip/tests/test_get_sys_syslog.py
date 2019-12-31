# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_syslog
from genie.libs.parser.bigip.get_sys_syslog import SysSyslog

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/syslog'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:syslog:syslogstate",
            "selfLink": "https://localhost/mgmt/tm/sys/syslog?ver=14.1.2.1",
            "authPrivFrom": "notice",
            "authPrivTo": "emerg",
            "clusteredHostSlot": "enabled",
            "clusteredMessageSlot": "disabled",
            "consoleLog": "enabled",
            "cronFrom": "warning",
            "cronTo": "emerg",
            "daemonFrom": "notice",
            "daemonTo": "emerg",
            "isoDate": "disabled",
            "kernFrom": "debug",
            "kernTo": "emerg",
            "local6From": "notice",
            "local6To": "emerg",
            "mailFrom": "notice",
            "mailTo": "emerg",
            "messagesFrom": "notice",
            "messagesTo": "warning",
            "userLogFrom": "notice",
            "userLogTo": "emerg",
        }


class test_get_sys_syslog(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "authPrivFrom": "notice",
        "authPrivTo": "emerg",
        "clusteredHostSlot": "enabled",
        "clusteredMessageSlot": "disabled",
        "consoleLog": "enabled",
        "cronFrom": "warning",
        "cronTo": "emerg",
        "daemonFrom": "notice",
        "daemonTo": "emerg",
        "isoDate": "disabled",
        "kernFrom": "debug",
        "kernTo": "emerg",
        "kind": "tm:sys:syslog:syslogstate",
        "local6From": "notice",
        "local6To": "emerg",
        "mailFrom": "notice",
        "mailTo": "emerg",
        "messagesFrom": "notice",
        "messagesTo": "warning",
        "selfLink": "https://localhost/mgmt/tm/sys/syslog?ver=14.1.2.1",
        "userLogFrom": "notice",
        "userLogTo": "emerg",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysSyslog(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysSyslog(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
