# Python
import re
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# Parser
from genie.libs.parser.iosxr.show_ssh import ShowSsh
 

# ===============================
# Unit tests for:
#   'show ssh session details'
# ===============================
class test_show_ssh(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {
        'session': {
            'version': 'Cisco-2.0',
            'incoming': {
                '1': {
                    'id': 1,
                    'key_exchange': 'ecdh-sha2-nistp256', 
                    'pubkey': 'ssh-rsa', 
                    'incipher': 'aes128-ctr', 
                    'outcipher': 'aes128-ctr', 
                    'inmac': 'hmac-sha2-256', 
                    'outmac': 'hmac-sha2-256'
                }
            },
            'outgoing': {
                '1': {
                    'id': 1, 
                    'key_exchange': 'ecdh-sha2-nistp521', 
                    'pubkey': 'ecdsa-sha2-nistp256', 
                    'incipher': 'aes128-ctr', 
                    'outcipher': 'aes128-ctr', 
                    'inmac': 'hmac-sha2-512', 
                    'outmac': 'hmac-sha2-512'
                }
            }
        }
    }

    golden_output = {'execute.return_value': '''
        Tue Jan 14 17:58:50.079 UTC
        SSH version : Cisco-2.0
 
        id      key-exchange           pubkey               incipher    outcipher   inmac         outmac  
        ----------------------------------------------------------------------------------------------------
        Incoming Session
        1       ecdh-sha2-nistp256     ssh-rsa              aes128-ctr  aes128-ctr  hmac-sha2-256 hmac-sha2-256
 
        Outgoing connection
        1       ecdh-sha2-nistp521     ecdsa-sha2-nistp256  aes128-ctr  aes128-ctr  hmac-sha2-512 hmac-sha2-512
    '''}

    def test_show_ssh_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowSsh(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_show_ssh_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowSsh(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

if __name__ == '__main__':
    unittest.main()
