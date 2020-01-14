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
class ShowSSHSchema(MetaParser):
    ''' Schema for "show ssh session details" '''

    schema = {
        'session': {
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
class ShowSSH(ShowSSHSchema):
 
    ''' Parser for "show ssh session details"'''
 
    cli_command = 'show ssh session details'
 
    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
 
        # Init vars
        parsed_dict = {}

        p1 = re.compile(r'^(?P<id>(\d+))\s+(?P<key_exchange>([\w+|-]+))'
                         '\s+(?P<pubkey>([\w+|-]+))\s+(?P<incipher>([\w+|-]+))'
                         '\s+(?P<outcipher>([\w+|-]+))\s+(?P<inmac>([\w+|-]+))'
                         '\s+(?P<outmac>([\w+|-]+))$')

        p2 = re.compile('^Incoming Session')

        p3 = re.compile('^Outgoing connection')
    
        isIncoming = None
 
        for line in out.splitlines():
            line = line.strip()
 
            m = p1.match(line)
            if m:
                group = m.groupdict()
                group_id = group['id']
                group['id'] = int(group_id)
                
                ret_dict = parsed_dict.setdefault('session', {})\
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
 
        return parsed_dict