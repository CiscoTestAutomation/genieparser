
# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Genie
from genie.metaparser.util.exceptions import SchemaEmptyParserError
from genie.libs.parser.ios.show_crypto import ShowCryptoPkiCertificates

from genie.libs.parser.iosxe.tests.test_show_crypto \
    import test_show_crypto_pki_certificate as test_show_crypto_pki_certificate_iosxe

# ====================================================
#  Unit test for 'show crypto pki certificates <WORD>'
# ====================================================
class test_show_crypto_pki_certificate(test_show_crypto_pki_certificate_iosxe):

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowCryptoPkiCertificates(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()    

    def test_c3850(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_c3850)
        obj = ShowCryptoPkiCertificates(device=self.device)
        parsed_output = obj.parse(trustpoint_name='CISCO_IDEVID_SUDI')
        self.assertEqual(parsed_output, self.golden_parsed_output_c3850)

    def test_csr1000(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_csr1000)
        obj = ShowCryptoPkiCertificates(device=self.device)
        parsed_output = obj.parse(trustpoint_name='TP-self-signed-4146203551')
        self.assertEqual(parsed_output, self.golden_parsed_output_csr1000)


if __name__ == '__main__':
    unittest.main()
