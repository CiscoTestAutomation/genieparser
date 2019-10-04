"""show_msdp.py
IOSXR parsers for the following commands

    * 'show msdp peer'
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


class ShowMsdpPeerSchema(MetaParser):
    """Schema for:
        * 'show msdp peer'
    """
    schema = {
        'vrf': {
            Any(): {
                'peer': {
                    Any(): {
                        'peer_as': int,
                        Optional('description'): str,
                        'session_state': str,
                        'reset': str,
                        'connect_source_address': str,
                        'elapsed_time': str,
                        'statistics': {
                            'received': {
                                'sa_message': int,
                                'tlv_message': int,
                            },
                            'sent': {
                                'tlv_message': int,
                            },
                            'output_message_discarded': int,
                            'queue': {
                                'size_input': int,
                                'size_output': int,
                            },
                            'conn_count_cleared': str,
                        },
                        'sa_filter': {
                            'in': {
                                Any(): {
                                    'filter': str,
                                }
                            },
                            'out': {
                                Any(): {
                                    'filter': str,
                                }
                            }
                        },
                        'sa_request': {
                            'input_filter': str,
                            'sa_request_to_peer': str,
                        },
                        'password': str,
                        'ttl_threshold': int,
                        'timer': {
                            'keepalive_interval': int,
                            'peer_timeout_interval': int,
                        },
                        'nsr': {
                            'state': str,
                            'oper_downs': int,
                            'up_down_time': str
                        }
                    }
                }
            }
        }
    }


class ShowMsdpPeer(ShowMsdpPeerSchema):
    """ Parser for:
        * 'show msdp peer'
        * 'show msdp vrf <vrf> peer'
    """

    cli_command = ['show msdp vrf {vrf} peer',
                   'show msdp peer']
    exclude = ['elapsed_time', 'tlv_message', 'sa_message']

    def cli(self, vrf='', output=None):
        if output is None:
            if vrf:
                cmd = self.cli_command[0].format(vrf=vrf)
            else:
                cmd = self.cli_command[1]
            out = self.device.execute(cmd)

        else:
            out = output

        # MSDP Peer 202.202.33.3 (?), AS 4134
        r1 = re.compile(r'\s*MSDP\sPeer\s*(?P<peer>\S+)\s*\(\?\)\,\s*'
                        r'AS\s*(?P<peer_as>\d+)')

        # Description: R1
        # Description:
        r2 = re.compile(r'\s*Description\s*:\s*(?:(?P<description>\S+))?$')

        # State: Inactive, Resets: 999, Connection Source: 202.202.11.1
        r3 = re.compile(
            r'\s*State:\s*(?P<session_state>\S+)\,'
            r'\s*Resets:\s*(?P<reset>\d+)\,'
            r'\s*Connection\s*Source:\s*(?P<connect_source_address>\S+)')

        # Uptime(Downtime): 00:00:09, SA messages received: 0
        r4 = re.compile(r'\s*Uptime\(Downtime\):\s*(?P<elapsed_time>\S+)\,\s*'
                        r'SA messages received:\s*(?P<sa_message_in>\d+)')

        # TLV messages sent/received: 3/0
        r5 = re.compile(r'\s*TLV messages\ssent\/received:\s*'
                        r'(?P<tlv_message_sent>\d+)\/'
                        r'(?P<tlv_message_received>\d+)$')

        # Output messages discarded: 0
        r6 = re.compile(r'\s*Output\smessages\sdiscarded:\s*'
                        r'(?P<output_message_discarded>\d+)')

        # Connection and counters cleared 00:01:25 ago
        r7 = re.compile(r'\s*Connection\s*and\s*counters\s*cleared\s*'
                        r'(?P<conn_count_cleared>\S+)\s+ago$')

        # Input (S,G) filter: none
        # Input RP filter: none
        r8 = re.compile(r'\s*Input\s*(?P<filter_in>\S+)\s*'
                        r'filter:\s*(?P<filter>\S+)$')

        # Output (S,G) filter: none
        # Output RP filter: none
        r9 = re.compile(r'\s*Output\s*(?P<filter_out>\S+)\s*filter:'
                        r'\s*(?P<filter>\S+)$')

        # Input filter: none
        r10 = re.compile(r'\s*Input\s*filter:\s*(?P<input_filter>\S+)')

        # Sending SA-Requests to peer: disabled
        r11 = re.compile(r'\s*Sending\s*SA-Requests\s*to\s*peer:'
                         r' +(?P<sa_request_to_peer>\S+)')

        # Password: None
        r12 = re.compile(r'\s*Password:\s*'
                         r'(?P<password>\S+)')

        # Peer ttl threshold: 2
        r13 = re.compile(r'^Peer\s*ttl\s*threshold:'
                         r' +(?P<ttl_threshold>\d+)')

        # Input queue size: 0, Output queue size: 0
        r14 = re.compile(r'^Input\s*queue\s*size:\s*(?P<size_in>\d+),'
                         r'\s*Output\s*queue\s*size:\s*(?P<size_out>\d+)$')

        # KeepAlive timer period: 30
        r15 = re.compile(r'^KeepAlive\s*timer\speriod:'
                         r' +(?P<keepalive_interval>\d+)')

        # Peer Timeout timer period: 75
        r16 = re.compile(r'^Peer\s*Timeout\s*timer\s*period:'
                         r' +(?P<peer_timeout_interval>\d+)')

        # State: StopRead, Oper-Downs: 0
        r17 = re.compile(r'^State:\s*(?P<state>\S+)'
                         r'\,\s*Oper-Downs:'
                         r' +(?P<oper_downs>\d+)')

        # NSR-Uptime(NSR-Downtime): 1d02h
        r18 = re.compile(r'\s*NSR-Uptime\(NSR-Downtime\):'
                         r' +(?P<up_down_time>\S+)')

        parsed_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # MSDP Peer 202.202.33.3 (?), AS 4134
            result = r1.match(line)

            if result:

                group_dict = result.groupdict()

                if not vrf:
                    vrf = 'default'

                peer_dict = parsed_dict.setdefault(
                    'vrf', {}).setdefault(
                    vrf, {}).setdefault(
                    'peer', {}).setdefault(
                    group_dict['peer'], {})

                peer_dict['peer_as'] = int(group_dict['peer_as'])

                continue

            # Description
            result = r2.match(line)
            if result:
                group_dict = result.groupdict()
                des = group_dict['description']
                if des is not None:
                    peer_dict['description'] = des
                else:
                    pass

                continue

            # State: Up, Resets: 0, Connection source: 10.1.100.2
            result = r3.match(line)
            if result:
                group_dict = result.groupdict()
                peer_dict['session_state'] = group_dict['session_state']
                peer_dict['reset'] = group_dict['reset']
                peer_dict['connect_source_address'] = \
                    group_dict['connect_source_address']

                continue

            # Uptime(Downtime): 00:00:09, SA messages received: 0
            result = r4.match(line)
            if result:
                group_dict = result.groupdict()
                peer_dict['elapsed_time'] = group_dict['elapsed_time']

                statistics_dict = peer_dict.setdefault('statistics', {})

                received_dict = statistics_dict.setdefault('received', {})
                received_dict['sa_message'] = int(
                    group_dict['sa_message_in'])

                continue

            # TLV messages sent/received: 3/0
            result = r5.match(line)
            if result:
                group_dict = result.groupdict()

                sent_dict = statistics_dict.setdefault('sent', {})
                sent_dict['tlv_message'] = int(
                    group_dict['tlv_message_sent'])

                received_dict['tlv_message'] = int(
                    group_dict['tlv_message_received'])

                continue

            # Output messages discarded: 0
            result = r6.match(line)
            if result:
                group_dict = result.groupdict()
                statistics_dict['output_message_discarded'] = \
                    int(group_dict['output_message_discarded'])

                continue

            # Connection and counters cleared 00:01:25 ago
            result = r7.match(line)
            if result:
                group_dict = result.groupdict()
                statistics_dict['conn_count_cleared'] = group_dict['conn_count_cleared']

                continue

            # Input (S,G) filter: none
            # Input RP filter: none
            result = r8.match(line)
            if result:
                group_dict = result.groupdict()
                filter_in = group_dict['filter_in']
                filter_ = group_dict['filter']

                filter_in_dict = peer_dict.setdefault('sa_filter', {}). \
                    setdefault('in', {}). \
                    setdefault(filter_in, {})
                filter_in_dict['filter'] = filter_

                continue

            # Output (S,G) filter: none
            # Output RP filter: none
            result = r9.match(line)
            if result:
                group_dict = result.groupdict()
                filter_out = group_dict['filter_out']
                filter_ = group_dict['filter']

                filter_in_dict = peer_dict.setdefault('sa_filter', {}). \
                    setdefault('out', {}). \
                    setdefault(filter_out, {})

                filter_in_dict['filter'] = filter_

                continue

            # Input filter: none
            result = r10.match(line)
            if result:
                group_dict = result.groupdict()
                sa_request_dict = peer_dict.setdefault('sa_request', {})
                sa_request_dict['input_filter'] = group_dict['input_filter']

                continue

            # Sending SA-Requests to peer: disabled
            result = r11.match(line)
            if result:
                group_dict = result.groupdict()
                sa_request_dict['sa_request_to_peer'] = group_dict['sa_request_to_peer']

                continue

            # Password: None
            result = r12.match(line)
            if result:
                group_dict = result.groupdict()
                peer_dict['password'] = group_dict['password']

                continue

            # Peer ttl threshold: 2
            result = r13.match(line)
            if result:
                group_dict = result.groupdict()
                peer_dict['ttl_threshold'] = int(
                    group_dict['ttl_threshold'])

                continue

            # Input queue size: 0, Output queue size: 0
            result = r14.match(line)
            if result:
                group_dict = result.groupdict()
                queue_dict = statistics_dict.setdefault('queue', {})
                queue_dict['size_input'] = int(group_dict['size_in'])
                queue_dict['size_output'] = int(group_dict['size_out'])

                continue

            # KeepAlive timer period: 30
            result = r15.match(line)
            if result:
                group_dict = result.groupdict()
                timer_dict = peer_dict.setdefault('timer', {})
                timer_dict['keepalive_interval'] = int(
                    group_dict['keepalive_interval'])

                continue

            # Peer Timeout timer period: 75
            result = r16.match(line)
            if result:
                group_dict = result.groupdict()
                timer_dict['peer_timeout_interval'] = int(
                    group_dict['peer_timeout_interval'])

                continue

            # State: StopRead, Oper-Downs: 0
            result = r17.match(line)
            if result:
                group_dict = result.groupdict()
                nsr_dict = peer_dict.setdefault('nsr', {})
                nsr_dict['state'] = group_dict['state']
                nsr_dict['oper_downs'] = int(group_dict['oper_downs'])

                continue

            # NSR-Uptime(NSR-Downtime): 1d02h
            result = r18.match(line)
            if result:
                group_dict = result.groupdict()
                nsr_dict['up_down_time'] = group_dict['up_down_time']

                continue

        return parsed_dict
