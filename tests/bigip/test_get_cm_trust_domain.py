# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_cm_trust_domain
from genie.libs.parser.bigip.get_cm_trust_domain import CmTrustdomain

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/cm/trust-domain'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:cm:trust-domain:trust-domaincollectionstate",
            "selfLink": "https://localhost/mgmt/tm/cm/trust-domain?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:cm:trust-domain:trust-domainstate",
                    "name": "Root",
                    "partition": "Common",
                    "fullPath": "/Common/Root",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/cm/trust-domain/~Common~Root?ver=14.1.2.1",
                    "caCert": "/Common/dtca.crt",
                    "caCertReference": {
                        "link": "https://localhost/mgmt/tm/cm/cert/~Common~dtca.crt?ver=14.1.2.1"
                    },
                    "caCertBundle": "/Common/dtca-bundle.crt",
                    "caCertBundleReference": {
                        "link": "https://localhost/mgmt/tm/cm/cert/~Common~dtca-bundle.crt?ver=14.1.2.1"
                    },
                    "caDevices": ["/Common/bigip01.lab.local"],
                    "caDevicesReference": [
                        {
                            "link": "https://localhost/mgmt/tm/cm/device/~Common~bigip01.lab.local?ver=14.1.2.1"
                        }
                    ],
                    "caKey": "/Common/dtca.key",
                    "caKeyReference": {
                        "link": "https://localhost/mgmt/tm/cm/key/~Common~dtca.key?ver=14.1.2.1"
                    },
                    "status": "standalone",
                    "trustGroup": "/Common/device_trust_group",
                    "trustGroupReference": {
                        "link": "https://localhost/mgmt/tm/cm/device-group/~Common~device_trust_group?ver=14.1.2.1"
                    },
                }
            ],
        }


class test_get_cm_trust_domain(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "caCert": "/Common/dtca.crt",
                "caCertBundle": "/Common/dtca-bundle.crt",
                "caCertBundleReference": {
                    "link": "https://localhost/mgmt/tm/cm/cert/~Common~dtca-bundle.crt?ver=14.1.2.1"
                },
                "caCertReference": {
                    "link": "https://localhost/mgmt/tm/cm/cert/~Common~dtca.crt?ver=14.1.2.1"
                },
                "caDevices": ["/Common/bigip01.lab.local"],
                "caDevicesReference": [
                    {
                        "link": "https://localhost/mgmt/tm/cm/device/~Common~bigip01.lab.local?ver=14.1.2.1"
                    }
                ],
                "caKey": "/Common/dtca.key",
                "caKeyReference": {
                    "link": "https://localhost/mgmt/tm/cm/key/~Common~dtca.key?ver=14.1.2.1"
                },
                "fullPath": "/Common/Root",
                "generation": 1,
                "kind": "tm:cm:trust-domain:trust-domainstate",
                "name": "Root",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/cm/trust-domain/~Common~Root?ver=14.1.2.1",
                "status": "standalone",
                "trustGroup": "/Common/device_trust_group",
                "trustGroupReference": {
                    "link": "https://localhost/mgmt/tm/cm/device-group/~Common~device_trust_group?ver=14.1.2.1"
                },
            }
        ],
        "kind": "tm:cm:trust-domain:trust-domaincollectionstate",
        "selfLink": "https://localhost/mgmt/tm/cm/trust-domain?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = CmTrustdomain(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = CmTrustdomain(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
