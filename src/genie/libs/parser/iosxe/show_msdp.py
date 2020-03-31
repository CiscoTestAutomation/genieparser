'''show_msdp.py
IOSXE parsers for the following commands

    * 'show ip msdp peer'
    * 'show ip msdp vrf <vrf> peer'
    * 'show ip msdp sa-cache'
    * 'show ip msdp vrf <vrf> sa-cache'
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


class ShowIpMsdpPeerSchema(MetaParser):
    ''' Schema for:
        * 'show ip msdp peer'
        * 'show ip msdp vrf <vrf> peer'
    '''

    schema = {
        'vrf': {
            Any(): {
                'peer': {
                    Any(): {
                        'elapsed_time': str,
                        Optional('peer_as'): int,
                        'connect_source_address': str,
                        'connect_source': str,
                        'session_state': str,
                        'conn_count_cleared': str,
                        'resets': str,
                        'sa_learned_from': int,
                        'sa_filter': {
                            'in': {
                                Any(): {
                                    'filter': str,
                                    'route_map': str}},
                            'out': {
                                Any(): {
                                    'filter': str,
                                    'route_map': str}}
                        },
                        'ttl_threshold': int,
                        'sa_request': {
                            'input_filter': str,
                        },
                        'signature_protection': bool,
                        'statistics': {
                            'established_transitions': int,
                            'output_msg_discarded': int,
                            'queue': {
                                'size_in': int,
                                'size_out': int,
                            },
                            'received': {
                                'sa_message': int,
                                'sa_request': int,
                                'data_packets': int,
                                'data_message': int,
                            },
                            'sent': {
                                'sa_message': int,
                                'sa_response': int,
                                'data_packets': int,
                                'data_message': int,
                            },
                            'error': {
                                'rpf_failure': int
                            }
                        }
                    }
                }
            }
        }
    }


class ShowIpMsdpPeer(ShowIpMsdpPeerSchema):

    ''' Parser for:
        * 'show ip msdp peer'
        * 'show ip msdp vrf <vrf> peer'
    '''

    cli_command = ['show ip msdp vrf {vrf} peer',
                   'show ip msdp peer']
    exclude = ['elapsed_time' , 'data_message', 'sa_message']

    def cli(self, vrf='', output=None):
        if output is None:
            if vrf:
                cmd = self.cli_command[0].format(vrf=vrf)
            else:
                cmd = self.cli_command[1]
            out = self.device.execute(cmd)

        else:
            out = output

        # MSDP Peer 10.1.100.4 (?), AS 1
        # MSDP Peer 10.4.1.2 (?), AS ?
        r1 = re.compile(r'^MSDP\sPeer\s+(?P<peer>\S+)\s*\(\?\)\,\s*'
                        'AS\s*(?P<peer_as>(\d+|\?))')

        # State: Up, Resets: 0, Connection source: Loopback0 (10.1.100.2)
        r2 = re.compile(r'State:\s*(?P<session_state>(Up|Down))\,\s*Resets:'
                        '\s*(?P<resets>\d+)\,\s*Connection\s+source:\s*'
                        '(?P<connect_source>\S+)\s+\('
                        '(?P<connect_source_address>\S+)\)')

        # Uptime(Downtime): 00:41:18, Messages sent/received: 42/50
        r3 = re.compile(r'^Uptime\(Downtime\):\s*(?P<elapsed_time>\S+),'
                        '\s*Messages\s+sent\/received:\s*'
                        '(?P<data_message_sent>\d+)\/'
                        '(?P<data_message_received>\d+)$')

        # Output messages discarded: 0
        r4 = re.compile(r'^Output\s+messages\s+discarded:\s+'
                        '(?P<output_msg_discarded>\d+)$')

        # Connection and counters cleared 00:43:22 ago
        r5 = re.compile(r'^Connection\s+and\s+counters\s+cleared\s+'
                        '(?P<conn_count_cleared>\S+)\s+ago$')

        # Input (S,G) filter: none, route-map: none
        # Input RP filter: none, route-map: none
        r6 = re.compile(r'^Input\s+(?P<filter_in>[a-zA-Z\,\(\)]+)\s+'
                        'filter:\s*(?P<filter>\S+)\,\s+route-map:\s*'
                        '(?P<route_map>\S+)$')

        # Output (S,G) filter: none, route-map: none
        # Output RP filter: none, route-map: none
        r7 = re.compile(r'^Output\s+(?P<filter_out>[a-zA-Z\,\(\)]+)\s+filter:'
                        '\s*(?P<filter>\S+)\,\s+route-map:\s*'
                        '(?P<route_map>\S+)$')

        # Input filter: none
        r8 = re.compile(r'^Input\s+filter:\s*(?P<input_filter>\S+)')

        # Peer ttl threshold: 0
        r9 = re.compile(r'^Peer\s+ttl\s+threshold:\s*(?P<ttl_threshold>\d+)$')

        # SAs learned from this peer: 0
        r10 = re.compile(r'^SAs\s+learned\s+from\s+this\s+peer:'
                         '\s*(?P<sa_learned_from>\d+)')

        # Number of connection transitions to Established state: 1
        r11 = re.compile(r'^Number\s+of\s+connection\s+transitions\s+to'
                         '\s+Established\s+state:\s*'
                         '(?P<established_transitions>\d+)')

        # Input queue size: 0, Output queue size: 0
        r12 = re.compile(r'^Input\s+queue\s+size:\s*(?P<size_in>\d+),'
                         '\s+Output\s+queue\s+size:\s*(?P<size_out>\d+)$')

        # MD5 signature protection on MSDP TCP connection: not enabled
        r13 = re.compile(r'^MD5\s+signature\s+protection\s+on\s+MSDP\s+TCP'
                         '\s+connection:\s*(?P<signature_protection>'
                         '(?: not)?\s*enabled)$')

        # RPF Failure count: 27
        r14 = re.compile(r'^RPF\s+Failure\s+count:\s*(?P<rpf_failure>\d+)')

        # SA Messages in/out: 27/0
        r15 = re.compile(r'^SA\s+Messages\s+in/out:\s*'
                         '(?P<sa_message_in>\d+)\/'
                         '(?P<sa_message_out>\d+)$')

        # SA Requests in: 0
        r16 = re.compile(r'^SA\s+Requests\s+in:\s*(?P<sa_requests_in>\d+)$')

        # SA Responses out: 0
        r17 = re.compile(r'^SA\s+Responses\s+out:\s*(?P<sa_response_out>\d+)$')

        # Data Packets in/out: 6/0
        r18 = re.compile(r'Data\s+Packets\s+in/out:\s*(?P<data_packets_in>\d+)'
                         '\/(?P<data_packets_out>\d+)')

        parsed_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # MSDP Peer 10.1.100.4 (?), AS 1
            # MSDP Peer 10.4.1.2 (?), AS ?
            result = r1.match(line)
            if result:
                group = result.groupdict()
                if not vrf:
                    vrf = 'default'
                peer_dict = parsed_dict.setdefault('vrf', {})\
                    .setdefault(vrf, {}).setdefault('peer', {})\
                    .setdefault(group['peer'], {})
                peer_as_val = group['peer_as']
                if peer_as_val != '?':
                    peer_dict['peer_as'] = int(peer_as_val)

                continue

            # State: Up, Resets: 0, Connection source: Loopback0 (10.1.100.2)
            result = r2.match(line)
            if result:
                group = result.groupdict()
                peer_dict['session_state'] = group['session_state']
                peer_dict['resets'] = group['resets']
                peer_dict['connect_source'] = group['connect_source']
                peer_dict['connect_source_address'] = \
                    group['connect_source_address']

                continue

            # Uptime(Downtime): 00:41:18, Messages sent/received: 42/50
            result = r3.match(line)
            if result:
                group = result.groupdict()

                peer_dict['elapsed_time'] = group['elapsed_time']

                statistics_dict = peer_dict.setdefault('statistics', {})

                sent_dict = statistics_dict.setdefault('sent', {})
                sent_dict['data_message'] = int(group['data_message_sent'])

                received_dict = statistics_dict.setdefault('received', {})
                received_dict['data_message'] = \
                    int(group['data_message_received'])

                continue

            # Output messages discarded: 0
            result = r4.match(line)
            if result:
                group = result.groupdict()
                statistics_dict['output_msg_discarded'] = \
                    int(group['output_msg_discarded'])

                continue

            # Connection and counters cleared 00:43:22 ago
            result = r5.match(line)
            if result:
                group = result.groupdict()
                peer_dict['conn_count_cleared'] = group['conn_count_cleared']

                continue

            # Input (S,G) filter: none, route-map: none
            # Input RP filter: none, route-map: none
            result = r6.match(line)
            if result:
                group = result.groupdict()
                filter_in = group['filter_in']
                filter_ = group['filter']
                route_map_in = group['route_map']

                filter_in_dict = peer_dict.setdefault('sa_filter', {}).\
                    setdefault('in', {}).\
                    setdefault(filter_in, {})
                filter_in_dict['filter'] = filter_
                filter_in_dict['route_map'] = route_map_in

                continue

            # Output (S,G) filter: none, route-map: none
            # Output RP filter: none, route-map: none
            result = r7.match(line)
            if result:
                group = result.groupdict()
                filter_out = group['filter_out']
                filter_ = group['filter']
                route_map_out = group['route_map']

                filter_in_dict = peer_dict.setdefault('sa_filter', {}).\
                    setdefault('out', {}).\
                    setdefault(filter_out, {})

                filter_in_dict['filter'] = filter_
                filter_in_dict['route_map'] = route_map_out

                continue

            # Input filter: none
            result = r8.match(line)
            if result:
                group = result.groupdict()
                sa_request_dict = peer_dict.setdefault('sa_request', {})
                sa_request_dict['input_filter'] = group['input_filter']

                continue

            # Peer ttl threshold: 0
            result = r9.match(line)
            if result:
                group = result.groupdict()
                peer_dict['ttl_threshold'] = int(group['ttl_threshold'])

                continue

            # SAs learned from this peer: 0
            result = r10.match(line)
            if result:
                group = result.groupdict()
                peer_dict['sa_learned_from'] = int(group['sa_learned_from'])
                continue

            # Number of connection transitions to Established state: 1
            result = r11.match(line)
            if result:
                group = result.groupdict()
                statistics_dict['established_transitions'] = \
                    int(group['established_transitions'])
                continue

            # Input queue size: 0, Output queue size: 0
            result = r12.match(line)
            if result:
                group = result.groupdict()
                queue_dict = statistics_dict.setdefault('queue', {})
                queue_dict['size_in'] = int(group['size_in'])
                queue_dict['size_out'] = int(group['size_out'])

                continue

            # MD5 signature protection on MSDP TCP connection: not enabled
            result = r13.match(line)
            if result:
                group = result.groupdict()

                signature_protection = group['signature_protection'].strip()
                if signature_protection == 'enabled':
                    peer_dict['signature_protection'] = True
                elif signature_protection == 'not enabled':
                    peer_dict['signature_protection'] = False

                continue

            # RPF Failure count: 27
            result = r14.match(line)
            if result:
                group = result.groupdict()

                error_dict = statistics_dict.setdefault('error', {})
                error_dict['rpf_failure'] = int(group['rpf_failure'])
                continue

            # SA Messages in/out: 27/0
            result = r15.match(line)
            if result:
                group = result.groupdict()

                received_dict['sa_message'] = int(group['sa_message_in'])
                sent_dict['sa_message'] = int(group['sa_message_out'])
                continue

            # SA Requests in: 0
            result = r16.match(line)
            if result:
                group = result.groupdict()
                received_dict['sa_request'] = int(group['sa_requests_in'])

                continue

            # SA Responses out: 0
            result = r17.match(line)
            if result:
                group = result.groupdict()
                sent_dict['sa_response'] = int(group['sa_response_out'])
                continue

            # Data Packets in/out: 6/0
            result = r18.match(line)
            if result:
                group = result.groupdict()
                received_dict['data_packets'] = int(group['data_packets_in'])
                sent_dict['data_packets'] = int(group['data_packets_out'])

                continue

        return parsed_dict


class ShowIpMsdpSaCacheSchema(MetaParser):

    ''' Schema for:
        * 'show ip msdp sa-cache'
        * 'show ip msdp vrf <vrf> sa-cache'
    '''
    schema = {
        'vrf': {
            Any(): {
                'num_of_sa_cache': int,
                'sa_cache': {
                    Any(): {
                        'group': str,
                        'source_addr': str,
                        Optional('peer_as'): int,
                        Optional('peer_learned_from'): str,
                        Optional('rpf_peer'): str,
                        'peer': str,
                        'origin_rp': {
                            Any(): {
                                'rp_address': str,
                             },
                        },
                        Optional('statistics'): {
                            'received': {
                                'sa': int,
                                'encapsulated_data_received': int,
                            }
                        },
                        'up_time': str,
                        'expire': str
                    }
                }
            }
        }
    }


class ShowIpMsdpSaCache(ShowIpMsdpSaCacheSchema):

    cli_command = ['show ip msdp vrf {vrf} sa-cache',
                   'show ip msdp sa-cache', ]

    def cli(self, vrf='', output=None):
        if output is None:
            if vrf:
                cmd = self.cli_command[0].format(vrf=vrf)
            else:
                cmd = self.cli_command[1]
            out = self.device.execute(cmd)
        else:
            out = output

        # MSDP Source-Active Cache - 1 entries
        r1 = re.compile(r'MSDP\s+Source\-Active\s+Cache\s*\-\s*'
                        '(?P<num_of_sa_cache>\d+)\s+entries')

        # (10.3.3.18, 225.1.1.1), RP 10.3.100.8, BGP/AS 3, 00:00:10/00:05:49, Peer 10.1.100.4
        # (10.1.4.15, 225.1.1.1), RP 10.1.100.1, AS ?,00:19:29/00:05:14, Peer 10.1.100.1
        r2 = re.compile(r'\((?P<source_addr>\S+),\s*(?P<group>\S+)\),\s*RP\s*'
                        '(?P<rp_address>\S+),\s*(?:BGP\/)'
                        '?AS\s*(?P<peer_as>\S+)'
                        ',\s*(?P<up_time>\S+)\/(?P<expire>\S+)\,\s*Peer\s+'
                        '(?P<peer>\S+)')

        # Learned from peer 10.1.100.4, RPF peer 10.1.100.4,
        r3 = re.compile(r'Learned\s+from\s+peer\s(?P<peer_learned_from>\S+),'
                        '\s+RPF\s+peer\s+(?P<rpf_peer>\S+),')

        # SAs received: 1, Encapsulated data received: 1
        r4 = re.compile(r'SAs\s+received:\s+(?P<sa_received>\d+),'
                        '\s+Encapsulated\s+data\s+'
                        'received:\s+(?P<encapsulated_data_received>\d+)')

        parsed_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # MSDP Source-Active Cache - 1 entries
            result = r1.match(line)
            if result:
                group = result.groupdict()
                num_of_sa_cache = int(group['num_of_sa_cache'])

            # (10.3.3.18, 225.1.1.1), RP 10.3.100.8, BGP/AS 3, 00:00:10/00:05:49, Peer 10.1.100.4
            result = r2.match(line)
            if result:
                group = result.groupdict()

                source_addr = group['source_addr']
                addres_group = group['group']
                rp_address = group['rp_address']
                peer_as = group['peer_as']
                peer = group['peer']
                up_time = group['up_time']
                expire = group['expire']

                sa_cache = '{} {}'.format(addres_group, source_addr)
                if not vrf:
                    vrf = 'default'

                vrf_dict = parsed_dict.setdefault('vrf', {})\
                    .setdefault(vrf, {})
                vrf_dict['num_of_sa_cache'] = num_of_sa_cache

                sa_cache_dict = vrf_dict.setdefault('sa_cache', {})\
                    .setdefault(sa_cache, {})
                sa_cache_dict['group'] = addres_group
                sa_cache_dict['source_addr'] = source_addr
                sa_cache_dict['up_time'] = up_time
                sa_cache_dict['expire'] = expire
                sa_cache_dict['peer'] = peer
                if not peer_as or peer_as != '?':
                    sa_cache_dict['peer_as'] = int(peer_as)

                sa_cache_dict.setdefault('origin_rp', {})\
                    .setdefault(rp_address, {})\
                    .setdefault('rp_address', rp_address)

                continue

            # Learned from peer 10.1.100.4, RPF peer 10.1.100.4,
            result = r3.match(line)
            if result:
                group = result.groupdict()
                sa_cache_dict['peer_learned_from'] = group['peer_learned_from']
                sa_cache_dict['rpf_peer'] = group['rpf_peer']

                continue

            # SAs received: 1, Encapsulated data received: 1
            result = r4.match(line)
            if result:
                group = result.groupdict()
                received_dict = sa_cache_dict.setdefault('statistics', {})\
                    .setdefault('received', {})
                received_dict['sa'] = int(group['sa_received'])
                received_dict['encapsulated_data_received'] = \
                    int(group['encapsulated_data_received'])

                continue

        return parsed_dict
