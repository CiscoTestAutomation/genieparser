'''show_keychain.py

NXOS parsers for the following show commands:
    * show key chain
    * show key chain detail
    * show key chain mode decrypt
    * show key chain {key} 
    * show key chain {key} detail 
    * show key chain {key} mode decrypt
'''

# python
import re
# metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

# import parser utils
from genie.libs.parser.utils.common import Common   

class ShowKeyChainSchema(MetaParser):
    """Schema for 
        'show key chain', 
        'show key chain detail', 
        'show key chain mode decrypt', 
        'show key chain {key}', 
        'show key chain {key} detail', 
        'show key chain {key} mode decrypt'
    """

    schema = {
        'keychains' : {
            Any(): {
                Optional("key_type"): str,  # Macsec or tunnel-encryption or none
                Optional("active_send_key"): str,
                Any(): {
                    Optional("key_octet_string"): str,
                    Optional("encryption_type"): str,  #No Encryption type plain (0), encryption type Proprietary(7)
                    Optional("crypto_algorithm"): str,
                    Optional("lifetime_state"): str
            }
        }
      }
    }

# =====================================
# Parser for 'show macsec mka summary'
# ======================================

class ShowKeyChain(ShowKeyChainSchema):
    """Parser for
        'show key chain', 
        'show key chain detail', 
        'show key chain mode decrypt', 
        'show key chain {key}', 
        'show key chain {key} detail', 
        'show key chain {key} mode decrypt'
    """
    cli_command = ['show key chain', 
                   'show key chain {detail}', 
                   'show key chain mode {decrypt}', 
                   'show key chain {key}', 
                   'show key chain {key} {detail}', 
                   'show key chain {key} mode {decrypt}'
                ]

    def cli(self,key="", decrypt="", detail="",output=None):
        if output is None:
            if key and detail:
                cmd = self.cli_command[4].format(key=key, detail=detail)
            elif key and decrypt:
                cmd = self.cli_command[5].format(key=key, decrypt=decrypt)
            elif detail:
                cmd = self.cli_command[1].format(detail=detail)
            elif decrypt:
                 cmd = self.cli_command[2].format(decrypt=decrypt)
            elif key:
                cmd = self.cli_command[3].format(key=key)
            else:
                cmd = self.cli_command[0]
            
            output = self.device.execute(cmd)
        

        # Key-Chain 1 Macsec
        p1 = re.compile(r'^Key-Chain\s+(?P<name>\S+)\s?(?P<key_type>.*)')

        # Key 11 -- text 7 "075d731e1c5b4b574540595e567879767a6167704155445153040b0a01065c514a"
        p2 = re.compile(r'^Key\s+(?P<key_id>\S+)\s+'
            r'\S+\s+text\s+(?P<encryption_type>\d+)\s+"(?P<key_octet_string>[0-9a-fA-F*]+)"')

        # cryptographic-algorithm AES_128_CMAC
        p3 = re.compile(r'^cryptographic-algorithm\s+(?P<crypto_algorithm>\S+)')

        # send lifetime (always valid) [active]
        # send lifetime local (06:03:04 Nov 24 2022)-(duration 10)
        p4 = re.compile(r'^send lifetime(?P<lifetime_state>.*)')
        
        # youngest active send key: 12
        p5 = re.compile(r'^youngest active send key:\s+(?P<active_send_key>\S+)')

        result_dict = {}
        
        for line in output.splitlines():
            keyChainDict= result_dict.setdefault('keychains', {})  
            line = line.strip()

            # Key-Chain 1 Macsec
            m = p1.match(line)
            if m:
                group = m.groupdict()
                key_chain = group['name']
                if key_chain not in keyChainDict:
                    key_dict = keyChainDict.setdefault(key_chain, {})
                    key_dict.update({'key_type': group['key_type']})
                continue 
            
            # Key 11 -- text 7 "075d731e1c5b4b574540595e567879767a6167704155445153040b0a01065c514a"
            m = p2.match(line)
            if m: 
                group = m.groupdict()
                key_id = group.pop('key_id')
                key_id_dict =  key_dict.setdefault(key_id, {})
                key_id_dict.update(group)
                continue

            # cryptographic-algorithm AES_128_CMAC
            m = p3.match(line)
            if m:
                #keyChainDict[key_chain][key_id].update(m.groupdict())
                key_id_dict.update(m.groupdict())
                continue
            
            # send lifetime (always valid) [active]
            # send lifetime local (06:03:04 Nov 24 2022)-(duration 10)
            m = p4.match(line)
            if m:
                key_id_dict.update(m.groupdict())
                continue
            
            # youngest active send key: 12
            m = p5.match(line)
            if m:
                key_dict.update(m.groupdict())

        return result_dict
