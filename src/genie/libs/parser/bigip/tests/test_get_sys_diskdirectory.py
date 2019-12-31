# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_diskdirectory
from genie.libs.parser.bigip.get_sys_diskdirectory import SysDiskDirectory

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/disk/directory'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:disk:directory:directorycollectionstats",
            "selfLink": "https://localhost/mgmt/tm/sys/disk/directory?ver=14.1.2.1",
            "apiRawValues": {
                "apiAnonymous": "\nDirectory Name                  Current Size    New Size        \n--------------                  ------------    --------        \n/config                         2273280         -               \n/shared                         15728640        -               \n/var                            3145728         -               \n/var/log                        3072000         -               \n/appdata                        26128384        -               \n\n"
            },
        }


class test_get_sys_diskdirectory(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "apiRawValues": {
            "apiAnonymous": "\n"
            "Directory Name                  Current "
            "Size    New Size        \n"
            "--------------                  "
            "------------    --------        \n"
            "/config                         "
            "2273280         -               \n"
            "/shared                         "
            "15728640        -               \n"
            "/var                            "
            "3145728         -               \n"
            "/var/log                        "
            "3072000         -               \n"
            "/appdata                        "
            "26128384        -               \n"
            "\n"
        },
        "kind": "tm:sys:disk:directory:directorycollectionstats",
        "selfLink": "https://localhost/mgmt/tm/sys/disk/directory?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysDiskDirectory(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysDiskDirectory(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
