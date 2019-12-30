# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_sys_cryptoencrypted_attributes
from genie.libs.parser.bigip.get_sys_cryptoencrypted_attributes import (
    SysCryptoEncryptedattributes,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/sys/crypto/encrypted-attributes'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:sys:crypto:encrypted-attributes:encrypted-attributesstats",
            "selfLink": "https://localhost/mgmt/tm/sys/crypto/encrypted-attributes?ver=14.1.2.1",
            "entries": {
                "https://localhost/mgmt/tm/sys/crypto/encrypted-attributes/0": {
                    "nestedStats": {
                        "entries": {
                            "attributeName": {"description": "passphrase"},
                            "className": {
                                "description": "certificate_key_file_object"
                            },
                            "objectName": {
                                "description": "/Common/f5_api_com.key"
                            },
                            "validEncryption": {"description": "1"},
                        }
                    }
                },
                "https://localhost/mgmt/tm/sys/crypto/encrypted-attributes/1": {
                    "nestedStats": {
                        "entries": {
                            "attributeName": {"description": "secret"},
                            "className": {"description": "profile_sctp"},
                            "objectName": {"description": "/Common/sctp"},
                            "validEncryption": {"description": "1"},
                        }
                    }
                },
            },
        }


class test_get_sys_cryptoencrypted_attributes(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "entries": {
            "https://localhost/mgmt/tm/sys/crypto/encrypted-attributes/0": {
                "nestedStats": {
                    "entries": {
                        "attributeName": {"description": "passphrase"},
                        "className": {
                            "description": "certificate_key_file_object"
                        },
                        "objectName": {
                            "description": "/Common/f5_api_com.key"
                        },
                        "validEncryption": {"description": "1"},
                    }
                }
            },
            "https://localhost/mgmt/tm/sys/crypto/encrypted-attributes/1": {
                "nestedStats": {
                    "entries": {
                        "attributeName": {"description": "secret"},
                        "className": {"description": "profile_sctp"},
                        "objectName": {"description": "/Common/sctp"},
                        "validEncryption": {"description": "1"},
                    }
                }
            },
        },
        "kind": "tm:sys:crypto:encrypted-attributes:encrypted-attributesstats",
        "selfLink": "https://localhost/mgmt/tm/sys/crypto/encrypted-attributes?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = SysCryptoEncryptedattributes(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = SysCryptoEncryptedattributes(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
