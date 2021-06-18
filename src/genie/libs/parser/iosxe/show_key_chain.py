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
                'keys': {
                    Any(): {
                        'key_string': str,
                        'accept_lifetime': {
                            'start': str,
                            'end': str,
                            'is_valid': bool
                        },
                        'send_lifetime': {
                            'start': str,
                            'end': str,
                            'is_valid': bool
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
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Key-chain hello:
        p1 = re.compile(r'^Key\-chain\s+(?P<name>[A-Za-z0-9\-_]+):$')

        # key 1 -- text "cisco123"
        p2 = re.compile(
            r'^key\s+(?P<id>\d+)\s+\-\-\s+text\s+'
            r'\"(?P<key_string>\S+)\"$'
        )

        # accept lifetime (11:11:11 UTC Mar 1 2001) - (infinite) [valid now]
        # accept lifetime (always valid) - (always valid) [valid now]
        # accept lifetime (always valid) - (always valid) [valid now]
        # accept lifetime (10:10:10 UTC Jan 1 2002) - (06:01:00 UTC Jan 1 2010)
        p3 = re.compile(
            r'^accept\s+lifetime\s+\((?P<start>[A-Za-z0-9:\s\+\-_]+)\)\s+\-\s+'
            '\((?P<end>[A-Za-z0-9:\s\+\-_]+)\)'
            r'(\s+\[(?P<is_valid>[A-Za-z0-9\s\-_]+)\])?$'
        )

        # send lifetime (11:11:11 UTC Mar 1 2001) - (infinite) [valid now]
        # send lifetime (10:10:10 UTC Jan 1 2002) - (06:01:00 UTC Jan 1 2010)
        # send lifetime (always valid) - (always valid) [valid now]
        p4 = re.compile(
            r'^send\s+lifetime\s+\((?P<start>[A-Za-z0-9:\s\+\-_]+)\)\s+\-\s+'
            '\((?P<end>[A-Za-z0-9:\s\+\-_]+)\)'
            r'(\s+\[(?P<is_valid>[A-Za-z0-9\s\-_]+)\])?$'
        )

        parsed_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # Key-chain hello:
            m = p1.match(line)
            if m:
                group = m.groupdict()
                key_chain_dict = parsed_dict.setdefault(
                    'key_chains', {}
                ).setdefault(
                    group['name'], {}
                ).setdefault(
                    'keys', {}
                )
                continue

            # key 1 -- text "cisco123"
            m = p2.match(line)
            if m:
                group = m.groupdict()
                key_dict = key_chain_dict.setdefault(int(group['id']), {})
                key_dict.update({'key_string': group['key_string']})
                continue

            # accept lifetime (11:11:11 UTC Mar 1 2001) - (infinite) [valid now]
            # accept lifetime (always valid) - (always valid) [valid now]
            # accept lifetime (always valid) - (always valid) [valid now]
            m = p3.match(line)
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
            m = p4.match(line)
            if m:
                group = m.groupdict()
                lifetime = {
                    'start': group['start'],
                    'end': group['end'],
                    'is_valid': True if group['is_valid'] else False,
                }
                key_dict.update({'send_lifetime': lifetime})
                continue

        return parsed_dict
