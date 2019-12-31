# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_cryptomaster_key
from genie.libs.parser.bigip.get_sys_cryptomaster_key import SysCryptoMasterkey

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/crypto/master-key'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:crypto:master-key:master-keystats",
            "selfLink": "https://localhost/mgmt/tm/sys/crypto/master-key?ver=14.1.2.1",
            "entries": {
                "https://localhost/mgmt/tm/sys/crypto/master-key/0": {
                    "nestedStats": {
                        "entries": {
                            "masterKeyHash": {
                                "description": "/4zu3nomIzf7NMIkL5War/O9GKfooKuvUKd479obmHKDnLMcbKuKmPAhRkN7jM9Y+AWtb3y1C24yaCk51iXXQA=="
                            }
                        }
                    }
                }
            },
        }


class test_get_sys_cryptomaster_key(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "entries": {
            "https://localhost/mgmt/tm/sys/crypto/master-key/0": {
                "nestedStats": {
                    "entries": {
                        "masterKeyHash": {
                            "description": "/4zu3nomIzf7NMIkL5War/O9GKfooKuvUKd479obmHKDnLMcbKuKmPAhRkN7jM9Y+AWtb3y1C24yaCk51iXXQA=="
                        }
                    }
                }
            }
        },
        "kind": "tm:sys:crypto:master-key:master-keystats",
        "selfLink": "https://localhost/mgmt/tm/sys/crypto/master-key?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysCryptoMasterkey(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysCryptoMasterkey(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
