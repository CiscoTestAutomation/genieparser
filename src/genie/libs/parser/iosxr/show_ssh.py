
''' show_ssh.py

IOSXR parsers for the following show commands:
    * show ssh session details 
    * show ssh history
'''


# Python
import re

# Metaparser
from genie.metaparser import MetaParser
# parser utils
from genie.libs.parser.utils.common import Common
from genie.metaparser.util.schemaengine import Schema, Any, Optional


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


# =====================================
# Schema for 'show ssh history'
# =====================================
class ShowSshHistorySchema(MetaParser):
    #Schema for show SSH history
    schema = {
        'session':{
            'incoming':{
                Any():
                    {'chan': int,
                     'pty' : str,
                     'location':str,
                     'userid':str,
                     'host':str,
                     'ver':str,
                     'authentication':str,
                     'connection_type':str
                     }
            }
        }
    }      

# =====================================
# Parser for 'show ssh session history'
# =====================================
class ShowSshHistory(ShowSshHistorySchema):
    '''Parser for "show ssh history"'''
    cli_command = 'show ssh history'

     # Defines a function to run the cli_command
    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        
        # Initializes the Python dictionary variable
        parsed_dict = {}
        
        # Defines the regex for the lines of device output, which is
        #Incoming sessions
        p1 = re.compile(r'^(Incoming sessions)')
        
        #1        1    vty0    0/RP0/CPU0      admin     172.16.1.254          v2  key-intr       Command-Line-Interface
        p2 = re.compile(r'(?P<id>\d+) +(?P<chan>\d+) +(?P<pty>\S+) +(?P<location>\S+) +(?P<userid>\S+) +(?P<host>\S+) +(?P<ver>\S+) +(?P<authentication>\S+) +(?P<connection_type>\S+)')

         # Defines the "for" loop, to pattern match each line of output
        for line in out.splitlines():
            line = line.strip()
            #match='Incoming sessions'
            m = p1.match(line)
            if m:
                io_dict = parsed_dict.setdefault('session',{})
                direction_dict = io_dict.setdefault('incoming',{})
            
            #match='1        1    vty0    0/RP0/CPU0      admin     1'
            m = p2.match(line)
            
            # Processes the matched patterns for the lines of output
            if m:
                group = m.groupdict()
                id = int(group['id'])
                group_dict =direction_dict.\
                    setdefault(id,{})
                group_dict['chan'] = int(group['chan'])
                group_dict['pty'] = group['pty']
                group_dict['location'] = group['location']
                group_dict['userid'] = group['userid']
                group_dict['host'] = group['host']
                group_dict['ver'] = group['ver']
                group_dict['authentication'] = group['authentication']
                group_dict['connection_type'] = group['connection_type']
                continue
            
        return parsed_dict
