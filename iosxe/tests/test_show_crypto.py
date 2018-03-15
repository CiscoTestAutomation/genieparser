#!/bin/env python
import unittest
from unittest.mock import Mock
from ats.topology import Device

from metaparser.util.exceptions import SchemaEmptyParserError,\
                                       SchemaMissingKeyError
from parser.iosxe.show_crypto import ShowCryptoPkiCertificates


class test_show_crypto_pki_certificate(unittest.TestCase):
    dev1 = Device(name='empty')
    dev_c3850 = Device(name='c3850')
    empty_output = {'execute.return_value': '      '}

    golden_parsed_output_c3850 = {
        "trustpoints": {
            "CISCO_IDEVID_SUDI": {
               "certificate": {
                    "status": "Available",
                    "serial_number_in_hex": "793B572700000003750B",
                    "subject": {
                         "name": "WS-C3850-24P-0057D21BC800",
                         "pid": "WS-C3850-24P",
                         "cn": "WS-C3850-24P-0057D21BC800",
                         "serial_number": "FCW1947C0GF"
                    },
                    "issuer": {
                         "cn": "Cisco Manufacturing CA SHA2",
                         "o": "Cisco"
                    },
                    "crl_distribution_points": "http://www.cisco.com/security/pki/crl/cmca2.crl",
                    "usage": "General Purpose",
                    "validity_date": {
                         "start_date": "00:34:52 UTC Nov 20 2015",
                         "end_date": "00:44:52 UTC Nov 20 2025"
                    }
               },
               "ca_certificate": {
                    "status": "Available",
                    "serial_number_in_hex": "02",
                    "subject": {
                         "cn": "Cisco Manufacturing CA SHA2",
                         "o": "Cisco"
                    },
                    "issuer": {
                         "cn": "Cisco Root CA M2",
                         "o": "Cisco"
                    },
                    "crl_distribution_points": "http://www.cisco.com/security/pki/crl/crcam2.crl",
                    "usage": "Signature",
                    "validity_date": {
                         "start_date": "13:50:58 UTC Nov 12 2012",
                         "end_date": "13:00:17 UTC Nov 12 2037"
                    }
               }
            }
        }
    }

    golden_output_c3850 = {'execute.return_value': '''\
        Certificate
          Status: Available
          Certificate Serial Number (hex): 793B572700000003750B
          Certificate Usage: General Purpose
          Issuer: 
            cn=Cisco Manufacturing CA SHA2
            o=Cisco
          Subject:
            Name: WS-C3850-24P-0057D21BC800
            Serial Number: PID:WS-C3850-24P SN:FCW1947C0GF
            cn=WS-C3850-24P-0057D21BC800
            serialNumber=PID:WS-C3850-24P SN:FCW1947C0GF
          CRL Distribution Points: 
            http://www.cisco.com/security/pki/crl/cmca2.crl
          Validity Date: 
            start date: 00:34:52 UTC Nov 20 2015
            end   date: 00:44:52 UTC Nov 20 2025
          Associated Trustpoints: CISCO_IDEVID_SUDI 

        CA Certificate
          Status: Available
          Certificate Serial Number (hex): 02
          Certificate Usage: Signature
          Issuer: 
            cn=Cisco Root CA M2
            o=Cisco
          Subject: 
            cn=Cisco Manufacturing CA SHA2
            o=Cisco
          CRL Distribution Points: 
            http://www.cisco.com/security/pki/crl/crcam2.crl
          Validity Date: 
            start date: 13:50:58 UTC Nov 12 2012
            end   date: 13:00:17 UTC Nov 12 2037
          Associated Trustpoints: CISCO_IDEVID_SUDI Trustpool
    '''
    }

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        obj = ShowCryptoPkiCertificates(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()    

    def test_golden(self):
        self.maxDiff = None
        self.dev_c3850 = Mock(**self.golden_output_c3850)
        obj = ShowCryptoPkiCertificates(device=self.dev_c3850)
        parsed_output = obj.parse(trustpoint_name='CISCO_IDEVID_SUDI')
        self.assertEqual(parsed_output,self.golden_parsed_output_c3850)

if __name__ == '__main__':
    unittest.main()

