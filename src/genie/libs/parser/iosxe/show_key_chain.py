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
                Optional('is_tcp') : bool,
                Optional('preferred_mkt_id'): int,
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
                    # --- New TCP AO–specific fields ---
                    Optional('send_id'): int,
                    Optional('recv_id'): int,
                    Optional('include_tcp_options'): bool,
                    Optional('accept_ao_mismatch'): bool,

                    # --- MKT-related fields ---
                    Optional('mkt_ready'): bool,
                    Optional('mkt_preferred'): bool,
                    Optional('mkt_in_use'): bool,
                    Optional('mkt_id'): int,
                    Optional('mkt_send_id'): int,
                    Optional('mkt_recv_id'): int,
                    Optional('mkt_alive_send'): bool,
                    Optional('mkt_alive_recv'): bool,
                    Optional('mkt_include_tcp_options'): bool,
                    Optional('mkt_accept_ao_mismatch'): bool,
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
  
        # TCP key chain
        p8 = re.compile(r'^\s*(?P<is_tcp>TCP key chain)$')

        # Preferred MKT id - 1
        p9 = re.compile(r'^\s*Preferred\s+MKT\s+id\s*-\s*(?P<preferred_mkt_id>\d+)$')

        # send-id - 1
        p10 = re.compile(r'^\s*send-id\s*-\s*(?P<send_id>\d+)$')

        # recv-id - 1
        p11 = re.compile(r'^\s*recv-id\s*-\s*(?P<recv_id>\d+)$')

        # include-tcp-options
        p12 = re.compile(r'^\s*include-tcp-options$')

        # accept-ao-mismatch
        p13 = re.compile(r'^\s*accept-ao-mismatch$')

        # MKT related fields
        # MKT ready - true
        p14 = re.compile(r'^\s*MKT\s+ready\s*-\s*(?P<mkt_ready>\S+)$')

        # MKT preferred - true
        p15 = re.compile(r'^\s*MKT\s+preferred\s*-\s*(?P<mkt_preferred>\S+)$')

        # MKT in-use - false
        p16 = re.compile(r'^\s*MKT\s+in-use\s*-\s*(?P<mkt_in_use>\S+)$')

        # MKT id - 1
        p17 = re.compile(r'^\s*MKT\s+id\s*-\s*(?P<mkt_id>\d+)$')

        # MKT send-id - 1
        p18 = re.compile(r'^\s*MKT\s+send-id\s*-\s*(?P<mkt_send_id>\d+)$')

        # MKT recv-id - 1
        p19 = re.compile(r'^\s*MKT\s+recv-id\s*-\s*(?P<mkt_recv_id>\d+)$')

        # MKT alive (send) - true
        p20 = re.compile(r'^\s*MKT\s+alive\s+\(send\)\s*-\s*(?P<mkt_alive_send>\S+)$')

        # MKT alive (recv) - true
        p21 = re.compile(r'^\s*MKT\s+alive\s+\(recv\)\s*-\s*(?P<mkt_alive_recv>\S+)$')

        # MKT include TCP options - true
        p22 = re.compile(r'^\s*MKT\s+include\s+TCP\s+options\s*-\s*(?P<mkt_include_tcp_options>\S+)$')

        # MKT accept AO mismatch - true
        p23 = re.compile(r'^\s*MKT\s+accept\s+AO\s+mismatch\s*-\s*(?P<mkt_accept_ao_mismatch>\S+)$')


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

            
            # === TCP key chain section ===
            # TCP key chain
            m = p8.match(line)
            if m:
                group = m.groupdict()
                key_chain_dict.update({'is_tcp': True if group['is_tcp'] else False})
                continue

            # Preferred MKT id - 1
            m = p9.match(line)
            if m:
                group = m.groupdict()
                key_chain_dict.update({'preferred_mkt_id': int(group['preferred_mkt_id'])})
                continue

            # send-id - 1
            m = p10.match(line)
            if m:
                group = m.groupdict()
                key_dict.update({'send_id': int(group['send_id'])})
                continue

            # recv-id - 1
            m = p11.match(line)
            if m:
                group = m.groupdict()
                key_dict.update({'recv_id': int(group['recv_id'])})
                continue

            # include-tcp-options
            m = p12.match(line)
            if m:
                key_dict.update({'include_tcp_options': True})
                continue

            # accept-ao-mismatch
            m = p13.match(line)
            if m:
                key_dict.update({'accept_ao_mismatch': True})
                continue

            # --- MKT fields ---
            for ptn in [p14, p15, p16, p17, p18, p19, p20, p21, p22, p23]:
                m = ptn.match(line)
                if m:
                    group = m.groupdict()
                    for key, val in group.items():
                        if val is None:
                            continue
                        if val.lower() in ['true', 'false']:
                            val = True if val.lower() == 'true' else False
                        elif val.isdigit():
                            val = int(val)
                        key_dict.update({key: val})
                    break



        return parsed_dict



