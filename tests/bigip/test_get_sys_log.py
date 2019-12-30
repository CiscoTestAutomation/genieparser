# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_log
from genie.libs.parser.bigip.get_sys_log import SysLog

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/log'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:log:logcollectionstats",
            "selfLink": "https://localhost/mgmt/tm/sys/log?ver=14.1.2.1",
            "apiRawValues": {
                "apiAnonymous": "\nSys::Log\n daemon       : Unix Daemon Logs\n gtm          : Global Traffic Manager Logs\n kernel       : Linux Kernel Messages\n ltm          : Local Traffic Manager Logs\n mail         : Mail Daemon Logs\n messages     : Application Messages\n security     : Security Related Messages\n tmm          : Traffic Manager Microkernel Logs\n user         : Various user process logs\n webui        : Logs for the Web User Interface\n audit        : Audits of configuration changes\n"
            },
        }


class test_get_sys_log(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "apiRawValues": {
            "apiAnonymous": "\n"
            "Sys::Log\n"
            " daemon       : Unix Daemon Logs\n"
            " gtm          : Global Traffic Manager "
            "Logs\n"
            " kernel       : Linux Kernel Messages\n"
            " ltm          : Local Traffic Manager Logs\n"
            " mail         : Mail Daemon Logs\n"
            " messages     : Application Messages\n"
            " security     : Security Related Messages\n"
            " tmm          : Traffic Manager Microkernel "
            "Logs\n"
            " user         : Various user process logs\n"
            " webui        : Logs for the Web User "
            "Interface\n"
            " audit        : Audits of configuration "
            "changes\n"
        },
        "kind": "tm:sys:log:logcollectionstats",
        "selfLink": "https://localhost/mgmt/tm/sys/log?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysLog(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysLog(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
