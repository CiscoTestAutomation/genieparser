'''
show_key_chain.py
Parser for following commands:
    * show key chain
'''

import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional


class ShowKeyChainSchema(MetaParser):
    '''
    Schema for
        * show key chain
    '''
    schema = {
        'key_chains': {
            Any(): {
                Optional('is_macsec') : bool,
                Optional('keys'): {
                    Any(): {
                        Optional('key_string'): str,
                        Optional('cryptographic_algo'): str,
                        Optional('accept_lifetime'): {
                            Optional('start'): str,
                            Optional('end'): str,
                            Optional('is_valid'): bool
                        },
                        Optional('send_lifetime'): {
                            Optional('start'): str,
                            Optional('end'): str,
                            Optional('is_valid'): bool
                        },
                        Optional('lifetime'): {
                            Optional('start'): str,
                            Optional('end'): str,
                            Optional('is_valid'): bool
                        },
                    },
                },
            },
        },
    }


class ShowKeyChain(ShowKeyChainSchema):

    cli_command = 'show key chain'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Key-chain hello:
        p1 = re.compile(r'\s*^Key\-chain\s+(?P<name>[A-Za-z0-9\-_]+):$')


        #MacSEC key chain
        p2 = re.compile(r'\s*(?P<is_macsec>MacSEC key chain)')

        # key 1 -- text "cisco123"
        p3 = re.compile(
            r'^\s*key\s+(?P<id>[\d\w]+)\s+\-\-\s+text\s+'
            r'\"(?P<key_string>.*)\"$'
        )

        #cryptographic-algorithm: aes-256-cmac
        p4 = re.compile(r'^\s*cryptographic-algorithm\: (?P<cryptographic_algo>.*)')

        # accept lifetime (11:11:11 UTC Mar 1 2001) - (infinite) [valid now]
        # accept lifetime (always valid) - (always valid) [valid now]
        # accept lifetime (10:10:10 UTC Jan 1 2002) - (06:01:00 UTC Jan 1 2010)
        p5 = re.compile(
            r'^\s*accept\s+lifetime\s+\((?P<start>[A-Za-z0-9:\s\+\-_]+)\)\s+\-\s+'
            r'\((?P<end>[A-Za-z0-9:\s\+\-_]+)\)'
            r'(\s+\[(?P<is_valid>[A-Za-z0-9\s\-_]+)\])?$'
        )

        # send lifetime (11:11:11 UTC Mar 1 2001) - (infinite) [valid now]
        # send lifetime (10:10:10 UTC Jan 1 2002) - (06:01:00 UTC Jan 1 2010)
        # send lifetime (always valid) - (always valid) [valid now]
        p6 = re.compile(
            r'^\s*send\s+lifetime\s+\((?P<start>[A-Za-z0-9:\s\+\-_]+)\)\s+\-\s+'
            r'\((?P<end>[A-Za-z0-9:\s\+\-_]+)\)'
            r'(\s+\[(?P<is_valid>[A-Za-z0-9\s\-_]+)\])?$'
        )


        #lifetime (20:20:00 IST Jun 15 2023) - (20:34:00 IST Jun 15 2023)
        #lifetime (always valid) - (always valid) [valid now]
        #lifetime (11:11:11 UTC Mar 1 2001) - (infinite) [valid now]
        p7 = re.compile(r'^\s*lifetime\s+\((?P<start>[A-Za-z0-9:\s\+\-_]+)\)\s+\-\s+'
            r'\((?P<end>[A-Za-z0-9:\s\+\-_]+)\)'
            r'(\s+\[(?P<is_valid>[A-Za-z0-9\s\-_]+)\])?$')

        parsed_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # Key-chain hello:
            m = p1.match(line)
            if m:
                group = m.groupdict()
                key_chain_dict = parsed_dict.setdefault(
                    'key_chains', {}
                ).setdefault(
                    group['name'], {}
                )
                continue
            
            #MacSEC key chain
            m = p2.match(line)
            if m:
                group = m.groupdict()
                key_chain_dict.update({'is_macsec': True if group['is_macsec'] else False})
                continue

            # key 1 -- text "cisco123"
            m = p3.match(line)
            if m:
                group = m.groupdict()
                key_dict = key_dict = key_chain_dict.setdefault('keys', {}).setdefault(group['id'], {})
                key_dict.update({'key_string': group['key_string']})
                continue

            #cryptographic-algorithm: aes-256-cmac
            m = p4.match(line)
            if m:
                group = m.groupdict()
                key_dict.update({'cryptographic_algo': group['cryptographic_algo']})
                continue
            
            # accept lifetime (11:11:11 UTC Mar 1 2001) - (infinite) [valid now]
            # accept lifetime (always valid) - (always valid) [valid now]
            # accept lifetime (10:10:10 UTC Jan 1 2002) - (06:01:00 UTC Jan 1 2010)
            m = p5.match(line)
            if m:
                group = m.groupdict()
                lifetime = {
                    'start': group['start'],
                    'end': group['end'],
                    'is_valid': True if group['is_valid'] else False,
                }
                key_dict.update({'accept_lifetime': lifetime})
                continue

            # send lifetime (11:11:11 UTC Mar 1 2001) - (infinite) [valid now]
            # send lifetime (10:10:10 UTC Jan 1 2002) - (06:01:00 UTC Jan 1 2010)
            # send lifetime (always valid) - (always valid) [valid now]
            m = p6.match(line)
            if m:
                group = m.groupdict()
                lifetime = {
                    'start': group['start'],
                    'end': group['end'],
                    'is_valid': True if group['is_valid'] else False,
                }
                key_dict.update({'send_lifetime': lifetime})
                continue
            
            #lifetime (20:20:00 IST Jun 15 2023) - (20:34:00 IST Jun 15 2023)
            #lifetime (always valid) - (always valid) [valid now]
            #lifetime (11:11:11 UTC Mar 1 2001) - (infinite) [valid now]
            m = p7.match(line)
            if m:
                group = m.groupdict()
                lifetime = {
                    'start': group['start'],
                    'end': group['end'],
                    'is_valid': True if group['is_valid'] else False,
                }
                key_dict.update({'lifetime': lifetime})
                continue

        return parsed_dict
