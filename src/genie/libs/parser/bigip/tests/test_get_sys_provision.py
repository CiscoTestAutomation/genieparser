# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_provision
from genie.libs.parser.bigip.get_sys_provision import SysProvision

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/provision'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:provision:provisioncollectionstate",
            "selfLink": "https://localhost/mgmt/tm/sys/provision?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:sys:provision:provisionstate",
                    "name": "afm",
                    "fullPath": "afm",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/provision/afm?ver=14.1.2.1",
                    "cpuRatio": 0,
                    "diskRatio": 0,
                    "level": "none",
                    "memoryRatio": 0,
                },
                {
                    "kind": "tm:sys:provision:provisionstate",
                    "name": "am",
                    "fullPath": "am",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/provision/am?ver=14.1.2.1",
                    "cpuRatio": 0,
                    "diskRatio": 0,
                    "level": "none",
                    "memoryRatio": 0,
                },
                {
                    "kind": "tm:sys:provision:provisionstate",
                    "name": "apm",
                    "fullPath": "apm",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/provision/apm?ver=14.1.2.1",
                    "cpuRatio": 0,
                    "diskRatio": 0,
                    "level": "none",
                    "memoryRatio": 0,
                },
                {
                    "kind": "tm:sys:provision:provisionstate",
                    "name": "asm",
                    "fullPath": "asm",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/provision/asm?ver=14.1.2.1",
                    "cpuRatio": 0,
                    "diskRatio": 0,
                    "level": "none",
                    "memoryRatio": 0,
                },
                {
                    "kind": "tm:sys:provision:provisionstate",
                    "name": "avr",
                    "fullPath": "avr",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/provision/avr?ver=14.1.2.1",
                    "cpuRatio": 0,
                    "diskRatio": 0,
                    "level": "none",
                    "memoryRatio": 0,
                },
                {
                    "kind": "tm:sys:provision:provisionstate",
                    "name": "dos",
                    "fullPath": "dos",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/provision/dos?ver=14.1.2.1",
                    "cpuRatio": 0,
                    "diskRatio": 0,
                    "level": "none",
                    "memoryRatio": 0,
                },
                {
                    "kind": "tm:sys:provision:provisionstate",
                    "name": "fps",
                    "fullPath": "fps",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/provision/fps?ver=14.1.2.1",
                    "cpuRatio": 0,
                    "diskRatio": 0,
                    "level": "none",
                    "memoryRatio": 0,
                },
                {
                    "kind": "tm:sys:provision:provisionstate",
                    "name": "gtm",
                    "fullPath": "gtm",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/provision/gtm?ver=14.1.2.1",
                    "cpuRatio": 0,
                    "diskRatio": 0,
                    "level": "nominal",
                    "memoryRatio": 0,
                },
                {
                    "kind": "tm:sys:provision:provisionstate",
                    "name": "ilx",
                    "fullPath": "ilx",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/provision/ilx?ver=14.1.2.1",
                    "cpuRatio": 0,
                    "diskRatio": 0,
                    "level": "none",
                    "memoryRatio": 0,
                },
                {
                    "kind": "tm:sys:provision:provisionstate",
                    "name": "lc",
                    "fullPath": "lc",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/provision/lc?ver=14.1.2.1",
                    "cpuRatio": 0,
                    "diskRatio": 0,
                    "level": "none",
                    "memoryRatio": 0,
                },
                {
                    "kind": "tm:sys:provision:provisionstate",
                    "name": "ltm",
                    "fullPath": "ltm",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/provision/ltm?ver=14.1.2.1",
                    "cpuRatio": 0,
                    "diskRatio": 0,
                    "level": "nominal",
                    "memoryRatio": 0,
                },
                {
                    "kind": "tm:sys:provision:provisionstate",
                    "name": "pem",
                    "fullPath": "pem",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/provision/pem?ver=14.1.2.1",
                    "cpuRatio": 0,
                    "diskRatio": 0,
                    "level": "none",
                    "memoryRatio": 0,
                },
                {
                    "kind": "tm:sys:provision:provisionstate",
                    "name": "sslo",
                    "fullPath": "sslo",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/provision/sslo?ver=14.1.2.1",
                    "cpuRatio": 0,
                    "diskRatio": 0,
                    "level": "none",
                    "memoryRatio": 0,
                },
                {
                    "kind": "tm:sys:provision:provisionstate",
                    "name": "swg",
                    "fullPath": "swg",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/provision/swg?ver=14.1.2.1",
                    "cpuRatio": 0,
                    "diskRatio": 0,
                    "level": "none",
                    "memoryRatio": 0,
                },
                {
                    "kind": "tm:sys:provision:provisionstate",
                    "name": "urldb",
                    "fullPath": "urldb",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/sys/provision/urldb?ver=14.1.2.1",
                    "cpuRatio": 0,
                    "diskRatio": 0,
                    "level": "none",
                    "memoryRatio": 0,
                },
            ],
        }


class test_get_sys_provision(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "cpuRatio": 0,
                "diskRatio": 0,
                "fullPath": "afm",
                "generation": 1,
                "kind": "tm:sys:provision:provisionstate",
                "level": "none",
                "memoryRatio": 0,
                "name": "afm",
                "selfLink": "https://localhost/mgmt/tm/sys/provision/afm?ver=14.1.2.1",
            },
            {
                "cpuRatio": 0,
                "diskRatio": 0,
                "fullPath": "am",
                "generation": 1,
                "kind": "tm:sys:provision:provisionstate",
                "level": "none",
                "memoryRatio": 0,
                "name": "am",
                "selfLink": "https://localhost/mgmt/tm/sys/provision/am?ver=14.1.2.1",
            },
            {
                "cpuRatio": 0,
                "diskRatio": 0,
                "fullPath": "apm",
                "generation": 1,
                "kind": "tm:sys:provision:provisionstate",
                "level": "none",
                "memoryRatio": 0,
                "name": "apm",
                "selfLink": "https://localhost/mgmt/tm/sys/provision/apm?ver=14.1.2.1",
            },
            {
                "cpuRatio": 0,
                "diskRatio": 0,
                "fullPath": "asm",
                "generation": 1,
                "kind": "tm:sys:provision:provisionstate",
                "level": "none",
                "memoryRatio": 0,
                "name": "asm",
                "selfLink": "https://localhost/mgmt/tm/sys/provision/asm?ver=14.1.2.1",
            },
            {
                "cpuRatio": 0,
                "diskRatio": 0,
                "fullPath": "avr",
                "generation": 1,
                "kind": "tm:sys:provision:provisionstate",
                "level": "none",
                "memoryRatio": 0,
                "name": "avr",
                "selfLink": "https://localhost/mgmt/tm/sys/provision/avr?ver=14.1.2.1",
            },
            {
                "cpuRatio": 0,
                "diskRatio": 0,
                "fullPath": "dos",
                "generation": 1,
                "kind": "tm:sys:provision:provisionstate",
                "level": "none",
                "memoryRatio": 0,
                "name": "dos",
                "selfLink": "https://localhost/mgmt/tm/sys/provision/dos?ver=14.1.2.1",
            },
            {
                "cpuRatio": 0,
                "diskRatio": 0,
                "fullPath": "fps",
                "generation": 1,
                "kind": "tm:sys:provision:provisionstate",
                "level": "none",
                "memoryRatio": 0,
                "name": "fps",
                "selfLink": "https://localhost/mgmt/tm/sys/provision/fps?ver=14.1.2.1",
            },
            {
                "cpuRatio": 0,
                "diskRatio": 0,
                "fullPath": "gtm",
                "generation": 1,
                "kind": "tm:sys:provision:provisionstate",
                "level": "nominal",
                "memoryRatio": 0,
                "name": "gtm",
                "selfLink": "https://localhost/mgmt/tm/sys/provision/gtm?ver=14.1.2.1",
            },
            {
                "cpuRatio": 0,
                "diskRatio": 0,
                "fullPath": "ilx",
                "generation": 1,
                "kind": "tm:sys:provision:provisionstate",
                "level": "none",
                "memoryRatio": 0,
                "name": "ilx",
                "selfLink": "https://localhost/mgmt/tm/sys/provision/ilx?ver=14.1.2.1",
            },
            {
                "cpuRatio": 0,
                "diskRatio": 0,
                "fullPath": "lc",
                "generation": 1,
                "kind": "tm:sys:provision:provisionstate",
                "level": "none",
                "memoryRatio": 0,
                "name": "lc",
                "selfLink": "https://localhost/mgmt/tm/sys/provision/lc?ver=14.1.2.1",
            },
            {
                "cpuRatio": 0,
                "diskRatio": 0,
                "fullPath": "ltm",
                "generation": 1,
                "kind": "tm:sys:provision:provisionstate",
                "level": "nominal",
                "memoryRatio": 0,
                "name": "ltm",
                "selfLink": "https://localhost/mgmt/tm/sys/provision/ltm?ver=14.1.2.1",
            },
            {
                "cpuRatio": 0,
                "diskRatio": 0,
                "fullPath": "pem",
                "generation": 1,
                "kind": "tm:sys:provision:provisionstate",
                "level": "none",
                "memoryRatio": 0,
                "name": "pem",
                "selfLink": "https://localhost/mgmt/tm/sys/provision/pem?ver=14.1.2.1",
            },
            {
                "cpuRatio": 0,
                "diskRatio": 0,
                "fullPath": "sslo",
                "generation": 1,
                "kind": "tm:sys:provision:provisionstate",
                "level": "none",
                "memoryRatio": 0,
                "name": "sslo",
                "selfLink": "https://localhost/mgmt/tm/sys/provision/sslo?ver=14.1.2.1",
            },
            {
                "cpuRatio": 0,
                "diskRatio": 0,
                "fullPath": "swg",
                "generation": 1,
                "kind": "tm:sys:provision:provisionstate",
                "level": "none",
                "memoryRatio": 0,
                "name": "swg",
                "selfLink": "https://localhost/mgmt/tm/sys/provision/swg?ver=14.1.2.1",
            },
            {
                "cpuRatio": 0,
                "diskRatio": 0,
                "fullPath": "urldb",
                "generation": 1,
                "kind": "tm:sys:provision:provisionstate",
                "level": "none",
                "memoryRatio": 0,
                "name": "urldb",
                "selfLink": "https://localhost/mgmt/tm/sys/provision/urldb?ver=14.1.2.1",
            },
        ],
        "kind": "tm:sys:provision:provisioncollectionstate",
        "selfLink": "https://localhost/mgmt/tm/sys/provision?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysProvision(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysProvision(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
