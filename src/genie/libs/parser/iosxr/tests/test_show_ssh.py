
# Import the Python mock functionality
import re
import unittest
from unittest.mock import Mock

  
# pyATS
from pyats.topology import Device
from pyats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

# iosxr show_ssh
from genie.libs.parser.iosxr.show_ssh import ShowSsh, ShowSshHistory

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

# ===============================
# Unit tests for:
#   'show ssh history'
# ===============================
class test_show_ssh_history(unittest.TestCase):

    empty_output = {'execute.return_value': ''}
    golden_parsed_output1 ={
        'session':{
            'incoming': 
                 {1:
                  {'chan': 1,
                   'pty' : 'vty0',
                   'location':'0/RP0/CPU0',
                   'userid':'admin',
                   'host':'172.16.1.254',
                   'ver': 'v2',
                   'authentication':'key-intr',
                   'connection_type':'Command-Line-Interface'
                   },
                  2:
                   {'chan': 1,
                    'pty' : 'vty0',
                    'location':'0/RP0/CPU0',
                    'userid':'admin',
                    'host':'172.16.1.254',
                    'ver': 'v2',
                    'authentication':'key-intr',
                    'connection_type':'Command-Line-Interface'
                    }
                }
        } 
    }
    # Specify the expected unparsed output
    golden_output1 = {'execute.return_value': '''
    id       chan pty     location        userid    host                  ver authentication connection type
    ---------------------------------------------------------------------------------------------------------------
    Incoming sessions
    1        1    vty0    0/RP0/CPU0      admin     172.16.1.254          v2  key-intr       Command-Line-Interface
    2        1    vty0    0/RP0/CPU0      admin     172.16.1.254          v2  key-intr       Command-Line-Interface
    '''}
    
    def test_show_ssh_history_full(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowSshHistory(device=self.device)
        parsed_output = obj.parse()  
        self.assertEqual(parsed_output, self.golden_parsed_output1)
    
    def test_show_ssh_history_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowSshHistory(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()
        
if __name__ == '__main__':
    unittest.main()
