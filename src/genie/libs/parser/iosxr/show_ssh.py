''' show_ssh.py

IOSXR parsers for the following show commands:
    * show ssh session details 
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

# parser utils
from genie.libs.parser.utils.common import Common

# =====================================
# Schema for 'show ssh session details'
# =====================================
class ShowSshSchema(MetaParser):
    ''' Schema for "show ssh session details" '''

    schema = {
        'session': {
            'version': str,
            Optional('incoming'): {
                Any(): {
                    'id': int,
                    'key_exchange': str,
                    'pubkey': str,
                    'incipher': str,
                    'outcipher': str,
                    'inmac': str,
                    'outmac': str
                }
            },
            Optional('outgoing'): {
                Any(): {
                    'id': int,
                    'key_exchange': str,
                    'pubkey': str,
                    'incipher': str,
                    'outcipher': str,
                    'inmac': str,
                    'outmac': str
                }
            }
        }
    }
 
# =====================================
# Parser for 'show ssh session details'
# =====================================
class ShowSsh(ShowSshSchema):
 
    ''' Parser for "show ssh session details"'''
 
    cli_command = 'show ssh session details'
 
    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
 
        # Init vars
        parsed_dict = {}

        # 1       ecdh-sha2-nistp256     ssh-rsa              aes128-ctr  aes128-ctr  hmac-sha2-256 hmac-sha2-256
        # 1       ecdh-sha2-nistp521     ecdsa-sha2-nistp256  aes128-ctr  aes128-ctr  hmac-sha2-512 hmac-sha2-512
        p1 = re.compile(r'^(?P<id>(\d+))\s+(?P<key_exchange>(\S+))'
                         '\s+(?P<pubkey>(\S+))\s+(?P<incipher>(\S+))'
                         '\s+(?P<outcipher>(\S+))\s+(?P<inmac>(\S+))'
                         '\s+(?P<outmac>(\S+))$')

        # Incoming Session
        p2 = re.compile(r'^Incoming Session')

        # Outgoing connection
        p3 = re.compile(r'^Outgoing connection')

        # SSH version : Cisco-2.0
        p4 = re.compile(r'^SSH version : (?P<version>(\S+))')
    
        isIncoming = None
 
        for line in out.splitlines():
            line = line.strip()
 
            m = p1.match(line)
            if m:
                group = m.groupdict()
                group_id = group['id']
                group['id'] = int(group_id)
                
                parsed_dict.setdefault('session', {})\
                    .setdefault('incoming' if isIncoming else 'outgoing', {})\
                    .setdefault(group_id, group)
                continue

            m = p2.match(line)
            if m:
                isIncoming = True
                continue
            
            m = p3.match(line)
            if m:
                isIncoming = False
                continue

            m = p4.match(line)
            if m:
                group = m.groupdict()
                parsed_dict.setdefault('session', {})\
                    .setdefault('version', group['version'])
                continue
 
        return parsed_dict