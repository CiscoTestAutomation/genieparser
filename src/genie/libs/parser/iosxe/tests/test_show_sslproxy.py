import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                             SchemaMissingKeyError

# Parser
from genie.libs.parser.iosxe.show_sslproxy import ShowSslproxyStatus


# ============================================
# unittest for 'show sslproxy status'
# ============================================
class TestShowSslproxyStatus(unittest.TestCase):
    device = Device(name='aDevice')
    maxDiff = None
    empty_output = {'execute.return_value' : ''}
    golden_output = {'execute.return_value': '''
        ==========================================================
                       SSL Proxy Status
        ==========================================================

        Configuration
        -------------
        CA Cert Bundle                 : /bootflash/vmanage-admin/apache.pem
        CA TP Label                    : PROXY-SIGNING-CA
        Cert Lifetime                  : 730
        EC Key type                    : P256
        RSA Key Modulus                : 2048
        Cert Revocation                : NONE
        Expired Cert                   : drop
        Untrusted Cert                 : drop
        Unknown Status                 : drop
        Unsupported Protocol Ver       : drop
        Unsupported Cipher Suites      : drop
        Failure Mode Action            : close
        Min TLS Ver                    : TLS Version 1

        Status
        ------
        SSL Proxy Operational State    : RUNNING
        TCP Proxy Operational State    : RUNNING
        Clear Mode                     : TRUE
        '''
        }

    golden_parsed_output = {
        'ca_cert_bundle': '/bootflash/vmanage-admin/apache.pem',
        'ca_tp_label': 'PROXY-SIGNING-CA',
        'cert_lifetime': 730,
        'ec_key_type': 'P256',
        'rsa_key_modulus': 2048,
        'cert_revocation': 'NONE',
        'expired_cert': 'drop',
        'untrusted_cert': 'drop',
        'unknown_status': 'drop',
        'unsupported_protocol_ver': 'drop',
        'unsupported_cipher_suites': 'drop',
        'failure_mode_action': 'close',
        'min_tls_ver': 'TLS Version 1',
        'ssl_proxy_operational_state': 'RUNNING',
        'tcp_proxy_operational_state': 'RUNNING',
        'clear_mode': 'TRUE'
    }


    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowSslproxyStatus(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,{})

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowSslproxyStatus(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)


if __name__ == '__main__':
		unittest.main()
