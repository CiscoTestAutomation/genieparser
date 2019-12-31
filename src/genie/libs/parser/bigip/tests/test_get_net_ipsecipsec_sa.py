# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_net_ipsecipsec_sa
from genie.libs.parser.bigip.get_net_ipsecipsec_sa import NetIpsecIpsecsa

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/net/ipsec/ipsec-sa'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:net:ipsec:ipsec-sa:ipsec-sastats",
            "selfLink": "https://localhost/mgmt/tm/net/ipsec/ipsec-sa?ver=14.1.2.1",
            "apiRawValues": {
                "apiAnonymous": "IPsec::SecurityAssociations\nTotal records returned: 0\n"
            },
        }


class test_get_net_ipsecipsec_sa(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "apiRawValues": {
            "apiAnonymous": "IPsec::SecurityAssociations\n"
            "Total records returned: 0\n"
        },
        "kind": "tm:net:ipsec:ipsec-sa:ipsec-sastats",
        "selfLink": "https://localhost/mgmt/tm/net/ipsec/ipsec-sa?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = NetIpsecIpsecsa(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = NetIpsecIpsecsa(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
