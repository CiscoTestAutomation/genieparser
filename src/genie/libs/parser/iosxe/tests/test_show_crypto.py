
# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Genie
from genie.metaparser.util.exceptions import SchemaEmptyParserError
from genie.libs.parser.iosxe.show_crypto import ShowCryptoPkiCertificates


# ====================================================
#  Unit test for 'show crypto pki certificates <WORD>'
# ====================================================
class test_show_crypto_pki_certificate(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output_c3850 = {
        "trustpoints": {
            "CISCO_IDEVID_SUDI": {
               "associated_trustpoints":{
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
    }

    golden_output_c3850 = {'execute.return_value': '''
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
        '''}

    golden_parsed_output_csr1000 = {
        'trustpoints': 
            {'TP-self-signed-4146203551': 
                {'associated_trustpoints': 
                    {'router_self_signed_certificate': 
                        {'issuer': 
                            {'cn': 'IOS-Self-Signed-Certificate-4146203551'},
                        'serial_number_in_hex': '01',
                        'status': 'Available',
                        'storage': 'nvram:IOS-Self-Sig#1.cer',
                        'subject': 
                            {'cn': 'IOS-Self-Signed-Certificate-4146203551',
                            'name': 'IOS-Self-Signed-Certificate-4146203551'},
                        'usage': 'General Purpose',
                        'validity_date': 
                            {'end_date': '00:00:00 UTC Jan 1 2020',
                            'start_date': '21:37:27 UTC Apr 23 2018'}}}}}}

    golden_output_csr1000 = {'execute.return_value': '''
        Router Self-Signed Certificate
          Status: Available
          Certificate Serial Number (hex): 01
          Certificate Usage: General Purpose
          Issuer:
            cn=IOS-Self-Signed-Certificate-4146203551
          Subject:
            Name: IOS-Self-Signed-Certificate-4146203551
            cn=IOS-Self-Signed-Certificate-4146203551
          Validity Date:
            start date: 21:37:27 UTC Apr 23 2018
            end   date: 00:00:00 UTC Jan 1 2020
          Associated Trustpoints: TP-self-signed-4146203551
          Storage: nvram:IOS-Self-Sig#1.cer
        '''}

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
