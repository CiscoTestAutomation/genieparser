# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_cm_sha1_fingerprint
from genie.libs.parser.bigip.get_cm_sha1_fingerprint import CmSha1fingerprint

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/cm/sha1-fingerprint'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:cm:sha1-fingerprint:sha1-fingerprintstats",
            "selfLink": "https://localhost/mgmt/tm/cm/sha1-fingerprint?ver=14.1.2.1",
            "entries": {
                "https://localhost/mgmt/tm/cm/sha1-fingerprint/0": {
                    "nestedStats": {
                        "entries": {
                            "description": {
                                "description": "(/etc/httpd/conf/ssl.crt/server.crt) = 9938438b2634c4f681b0f168827aec53e3170af2"
                            }
                        }
                    }
                }
            },
        }


class test_get_cm_sha1_fingerprint(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "entries": {
            "https://localhost/mgmt/tm/cm/sha1-fingerprint/0": {
                "nestedStats": {
                    "entries": {
                        "description": {
                            "description": "(/etc/httpd/conf/ssl.crt/server.crt) "
                            "= "
                            "9938438b2634c4f681b0f168827aec53e3170af2"
                        }
                    }
                }
            }
        },
        "kind": "tm:cm:sha1-fingerprint:sha1-fingerprintstats",
        "selfLink": "https://localhost/mgmt/tm/cm/sha1-fingerprint?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = CmSha1fingerprint(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = CmSha1fingerprint(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
