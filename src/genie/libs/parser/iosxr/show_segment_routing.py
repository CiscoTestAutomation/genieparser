''' show_segment_routing.py

Parser for the following show commands:
    * show isis segment-routing prefix-sid-map active-policy
    *  show isis segment-routing prefix-sid-map backup-policy
    *  show isis segment-routing prefix-sid-map active-policy
    *  show isis segment-routing prefix-sid-map backup-policy
    *  show ospf segment-routing prefix-sid-map active-policy
    *  show ospf segment-routing prefix-sid-map backup-policy
    * show segment-routing mapping-server prefix-sid-map ipv4 detail
    * show segment-routing mapping-server prefix-sid-map ipv4
    * show segment-routing local-block inconsistencies
    * show pce lsp detail
    * show pce lsp
    * show pce ipv4 prefix
    * show pce ipv4 peer detail
    * show pce ipv4 peer
    * show segment-routing srv6 locator
    * show segment-routing srv6 locator {locator_name}
'''

# !/bin/env python
import re

# Genie
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional


class ShowIsisSegmentRoutingPrefixSidMapSchema(MetaParser):
    ''' Schema for:
          *  show isis segment-routing prefix-sid-map active-policy
          *  show isis segment-routing prefix-sid-map backup-policy
        '''
    schema = {
        'process_id': {
            Any(): {
                'policy': {
                    Any(): {
                        'sid': {
                            Any(): {
                                'prefix': str,
                                'range': int,
                                Optional('flags'): str,
                            },
                        },
                        'number_of_mapping_entries': int,
                    },
                }
            },
        }
    }


class ShowIsisSegmentRoutingPrefixSidMap(ShowIsisSegmentRoutingPrefixSidMapSchema):
    ''' Parser for:
          *  show isis segment-routing prefix-sid-map active-policy
          *  show isis segment-routing prefix-sid-map backup-policy
        '''

    cli_command = 'show isis segment-routing prefix-sid-map {status}'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}
        # # SRMS active policy for Process ID 1
        # p2 = re.compile(r'^SRMS \w+ policy for Process ID (?P<process_id>\d+)$')

        # IS-IS 1 active policy
        p1 = re.compile(r'^IS-IS (?P<isis_id>\d+) (?P<status>\w+) policy$')

        # Prefix               SID Index    Range        Flags
        # 10.4.1.100/32         100          20          
        # 10.4.1.150/32         150          10          
        p2 = re.compile(r'(?P<prefix>[\w\.\/]+)\s+(?P<sid_index>\d+)'
                        '\s+(?P<range>\d+)(\s+(?P<flags>)[\w\s]+$)?')

        # Number of mapping entries: 2
        p3 = re.compile(r'Number of mapping entries:\s+(?P<entries>\d+)')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                isis_id = int(m.groupdict()['isis_id'])
                status = m.groupdict()['status']

                process_dict = ret_dict.setdefault('process_id', {})
                isis_dict = process_dict.setdefault(isis_id, {})
                policy_dict = isis_dict.setdefault('policy', {})
                status_dict = policy_dict.setdefault(status, {})

            m = p2.match(line)
            if m:
                sid_index = int(m.groupdict()['sid_index'])

                sid_dict = status_dict.setdefault('sid', {})
                index_dict = sid_dict.setdefault(sid_index, {})
                index_dict['prefix'] = m.groupdict()['prefix']
                index_dict['range'] = int(m.groupdict()['range'])
                if 'flag' in line.lower():
                    index_dict['flags'] = m.groupdict()['flags']

            m = p3.match(line)
            if m:
                status_dict['number_of_mapping_entries'] = \
                    int(m.groupdict()['entries'])

        return ret_dict


class ShowOspfSegmentRoutingPrefixSidMapSchema(MetaParser):
    ''' Schema for:
          *  show ospf segment-routing prefix-sid-map active-policy
          *  show ospf segment-routing prefix-sid-map backup-policy
        '''
    schema = {
        'process_id': {
            Any(): {
                'policy': {
                    Any(): {
                        'sid': {
                            Any(): {
                                'prefix': str,
                                'range': int,
                                Optional('flags'): str,
                            },
                        },
                        'number_of_mapping_entries': int,
                    },
                }
            },
        }
    }


class ShowOspfSegmentRoutingPrefixSidMap(ShowOspfSegmentRoutingPrefixSidMapSchema):
    ''' Parser for:
          *  show ospf segment-routing prefix-sid-map active-policy
          *  show ospf segment-routing prefix-sid-map backup-policy
        '''

    cli_command = 'show ospf segment-routing prefix-sid-map {status}'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}
        # SRMS active policy for Process ID 1
        p1 = re.compile(r'^SRMS (?P<status>\w+) policy for Process '
                        'ID (?P<process_id>\d+)$')

        # Prefix               SID Index    Range        Flags
        # 10.4.1.100/32         100          20          
        # 10.4.1.150/32         150          10          
        p2 = re.compile(r'(?P<prefix>[\w\.\/]+)\s+(?P<sid_index>\d+)'
                        '\s+(?P<range>\d+)(\s+(?P<flags>)[\w\s]+$)?')

        # Number of mapping entries: 2
        p3 = re.compile(r'Number of mapping entries:\s+(?P<entries>\d+)')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                process_id = int(m.groupdict()['process_id'])
                status = m.groupdict()['status']

                process_dict = ret_dict.setdefault('process_id', {})
                isis_dict = process_dict.setdefault(process_id, {})
                policy_dict = isis_dict.setdefault('policy', {})
                status_dict = policy_dict.setdefault(status, {})

            m = p2.match(line)
            if m:
                sid_index = int(m.groupdict()['sid_index'])

                sid_dict = status_dict.setdefault('sid', {})
                index_dict = sid_dict.setdefault(sid_index, {})
                index_dict['prefix'] = m.groupdict()['prefix']
                index_dict['range'] = int(m.groupdict()['range'])
                if 'flag' in line.lower():
                    index_dict['flags'] = m.groupdict()['flags']

            m = p3.match(line)
            if m:
                status_dict['number_of_mapping_entries'] = \
                    int(m.groupdict()['entries'])

        return ret_dict


class ShowPceIPV4PeerSchema(MetaParser):
    ''' Schema for:
        * show pce ipv4 peer
    '''
    schema = {
        'pce_peer_database': {
            Any(): {
                'state': str,
                'capabilities': {
                    Optional('stateful'): bool,
                    Optional('segment-routing'): bool,
                    Optional('update'): bool
                }
            },
        }
    }


class ShowPceIPV4Peer(ShowPceIPV4PeerSchema):
    ''' Parser for:
        * show pce ipv4 peer
    '''
    cli_command = 'show pce ipv4 peer'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # Peer address: 192.168.0.1
        p1 = re.compile(r'^Peer address: (?P<address>[\d\.]+)$')

        p2 = re.compile(r'^State: (?P<state>\w+)$')

        p3 = re.compile(r'Capabilities: (?P<stateful>\w+)\,\s+'
                        '(?P<segment_routing>[\w\-]+)\,\s+(?P<update>\w+)$')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                address = m.groupdict()['address']
                database_dict = ret_dict.setdefault('pce_peer_database', {})
                address_dict = database_dict.setdefault(address, {})

            m = p2.match(line)
            if m:
                state_bool = m.groupdict()['state']
                address_dict['state'] = state_bool

            m = p3.match(line)
            if m:
                capabilities_dict = address_dict.setdefault('capabilities', {})

                stateful_bool = True if 'stateful' in \
                                        m.groupdict()['stateful'].lower() else False
                segment_bool = True if 'segment-routing' in \
                                       m.groupdict()['segment_routing'].lower() else False
                update_bool = True if 'update' in \
                                      m.groupdict()['update'].lower() else False

                capabilities_dict['stateful'] = stateful_bool
                capabilities_dict['segment-routing'] = segment_bool
                capabilities_dict['update'] = update_bool
        return ret_dict


class ShowPceIPV4PeerDetailSchema(MetaParser):
    ''' Schema for:
        * show pce ipv4 peer detail
    '''
    schema = {
        'pce_peer_database': {
            Any(): {
                'state': str,
                'capabilities': {
                    'stateful': bool,
                    'segment-routing': bool,
                    'update': bool,
                    Optional('instantiation'): bool
                },
                'pcep': {
                    'uptime': str,
                    'session_id_local': int,
                    'session_id_remote': int,
                },
                Optional('md5'): str,
                'ka': {
                    'sending_intervals': int,
                    'minimum_acceptable_inteval': int,
                },
                'peer_timeout': int,
                Optional('maximum_sid_depth'): int,
                'statistics': {
                    'rx': {
                        'keepalive_messages': int,
                        'request_messages': int,
                        'reply_messages': int,
                        'error_messages': int,
                        'open_messages': int,
                        'report_messages': int,
                        'update_messages': int,
                        'initiate_messages': int,
                    },
                    'tx': {
                        'keepalive_messages': int,
                        'request_messages': int,
                        'reply_messages': int,
                        'error_messages': int,
                        'open_messages': int,
                        'report_messages': int,
                        'update_messages': int,
                        'initiate_messages': int,
                    },
                },
                Optional('last_pcerror'): {
                    'received': str,
                    'sent': str,
                }
            }
        }
    }


class ShowPceIPV4PeerDetail(ShowPceIPV4PeerDetailSchema):
    ''' Parser for:
        * show pce ipv4 peer detail
    '''

    cli_command = 'show pce ipv4 peer detail'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        p1 = re.compile(r'^Peer address: (?P<address>[\d\.]+)$')

        p2 = re.compile(r'^State: (?P<state>\w+)$')

        p3 = re.compile(r'^Capabilities: (?P<stateful>\w+)\,\s+'
                        '(?P<segment_routing>[\w\-]+)\,\s+(?P<update>\w+)$')
            
        p4 = re.compile(r'^PCEP has been up for: (?P<pcep_up_time>[\w+\:]+)$')

        p5 = re.compile(r'^PCEP session ID: local (?P<local_id>\d+)\, remote '
                        '(?P<remote_id>\d+)$')

        p6 = re.compile(r'^Sending KA every (?P<ka_time_intervals>\d+)'
                        '\s+seconds$')

        p7 = re.compile(r'^Minimum acceptable KA interval: '
                        '(?P<minimum_ka_interval>\d+)\s+seconds$')

        p8 = re.compile(r'^Peer timeout after (?P<peer_timeout>\d+)\sseconds$')

        p9 = re.compile(r'^Keepalive messages:\s+rx\s+'
                        '(?P<keepalive_messages_rx>\d+)\s+tx\s+(?P<keepalive_messages_tx>\d+)$')

        p10 = re.compile(r'Request messages:\s+rx\s+(?P<request_messages_rx>'
                         '\d+)\s+tx\s+(?P<request_messages_tx>\d+)$')

        p11 = re.compile(r'^Reply messages:\s+rx\s+(?P<reply_messages_rx>\d+)'
                         '\s+tx\s+(?P<reply_messages_tx>\d+)$')

        p12 = re.compile(r'^Error messages:\s+rx\s+(?P<error_messages_rx>\d+)'
                         '\s+tx\s+(?P<error_messages_tx>\d+)$')

        p13 = re.compile(r'^Open messages:\s+rx\s+(?P<open_messages_rx>\d+)\s+'
                         'tx\s+(?P<open_messages_tx>\d+)$')

        p14 = re.compile(r'^Report messages:\s+rx\s+(?P<report_messages_rx>\d+)'
                         '\s+tx\s+(?P<report_messages_tx>\d+)$')

        p15 = re.compile(r'^Update messages:\s+rx\s+(?P<update_messages_rx>\d+)'
                         '\s+tx\s+(?P<update_messages_tx>\d+)$')

        p16 = re.compile(r'^Initiate messages:\s+rx\s+(?P<initiate_messages_rx>'
                         '\d+)\s+tx\s+(?P<initiate_messages_tx>\d+)$')
        
        # Capabilities: Stateful, Segment-Routing, Update, Instantiation
        p17 = re.compile(r'^Capabilities: (?P<stateful>\w+)\,\s+'
                        '(?P<segment_routing>[\w\-]+)\,\s+(?P<update>\w+)'
                        '\,\s+(?P<instantiation>\w+)')
        
        # MD5: Enabled
        p18 = re.compile(r'^MD5:\s+(?P<md5>\w+)$')

        # Maximum SID Depth: 10
        p19 = re.compile(r'^Maximum SID Depth:\s+(?P<maximum_sid_depth>\d+)$')

        # Last PCError:
        p20 = re.compile(r'^Last\s+PCError:$')

        # Received: None
        p21 = re.compile(r'^Received:\s+(?P<received_pcerror>\w+)$')

        # Sent: None
        p22 = re.compile(r'^Sent:\s+(?P<sent_pcerror>\w+)$')
            
        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                address = m.groupdict()['address']
                database_dict = ret_dict.setdefault('pce_peer_database', {})
                address_dict = database_dict.setdefault(address, {})

            m = p2.match(line)
            if m:
                state_bool = m.groupdict()['state']
                address_dict['state'] = state_bool

            m = p3.match(line)
            if m:
                capabilities_dict = address_dict.setdefault('capabilities', {})

                stateful_bool = True if 'stateful' in \
                                        m.groupdict()['stateful'].lower() else False
                segment_bool = True if 'segment-routing' in \
                                       m.groupdict()['segment_routing'].lower() else False
                update_bool = True if 'update' in \
                                      m.groupdict()['update'].lower() else False

                capabilities_dict['stateful'] = stateful_bool
                capabilities_dict['segment-routing'] = segment_bool
                capabilities_dict['update'] = update_bool

            m = p4.match(line)
            if m:
                pcep_dict = address_dict.setdefault('pcep', {})
                pcep_dict['uptime'] = m.groupdict()['pcep_up_time']

            m = p5.match(line)
            if m:
                pcep_dict['session_id_local'] = int(m.groupdict()['local_id'])
                pcep_dict['session_id_remote'] = int(m.groupdict()['remote_id'])

            m = p6.match(line)
            if m:
                ka_dict = address_dict.setdefault('ka', {})
                ka_dict['sending_intervals'] = \
                    int(m.groupdict()['ka_time_intervals'])

            m = p7.match(line)
            if m:
                ka_dict['minimum_acceptable_inteval'] = \
                    int(m.groupdict()['minimum_ka_interval'])

            m = p8.match(line)
            if m:
                peer_timeout = int(m.groupdict()['peer_timeout'])
                address_dict.setdefault('peer_timeout', peer_timeout)

            m = p9.match(line)
            if m:
                stats_dict = address_dict.setdefault('statistics', {})
                rx_dict = stats_dict.setdefault('rx', {})
                tx_dict = stats_dict.setdefault('tx', {})

                rx_dict['keepalive_messages'] = \
                    int(m.groupdict()['keepalive_messages_rx'])
                tx_dict['keepalive_messages'] = \
                    int(m.groupdict()['keepalive_messages_tx'])

            m = p10.match(line)
            if m:
                rx_dict['request_messages'] = \
                    int(m.groupdict()['request_messages_rx'])
                tx_dict['request_messages'] = \
                    int(m.groupdict()['request_messages_tx'])

            m = p11.match(line)
            if m:
                rx_dict['reply_messages'] = \
                    int(m.groupdict()['reply_messages_rx'])
                tx_dict['reply_messages'] = \
                    int(m.groupdict()['reply_messages_tx'])

            m = p12.match(line)
            if m:
                rx_dict['error_messages'] = \
                    int(m.groupdict()['error_messages_rx'])
                tx_dict['error_messages'] = \
                    int(m.groupdict()['error_messages_tx'])

            m = p13.match(line)
            if m:
                rx_dict['open_messages'] = \
                    int(m.groupdict()['open_messages_rx'])
                tx_dict['open_messages'] = \
                    int(m.groupdict()['open_messages_tx'])

            m = p14.match(line)
            if m:
                rx_dict['report_messages'] = \
                    int(m.groupdict()['report_messages_rx'])
                tx_dict['report_messages'] = \
                    int(m.groupdict()['report_messages_tx'])

            m = p15.match(line)
            if m:
                rx_dict['update_messages'] = \
                    int(m.groupdict()['update_messages_rx'])
                tx_dict['update_messages'] = \
                    int(m.groupdict()['update_messages_tx'])

            m = p16.match(line)
            if m:
                rx_dict['initiate_messages'] = \
                    int(m.groupdict()['initiate_messages_rx'])
                tx_dict['initiate_messages'] = \
                    int(m.groupdict()['initiate_messages_tx'])

            m = p17.match(line)
            if m:
                capabilities_dict = address_dict.setdefault('capabilities', {})
                group = m.groupdict()
                
                capabilities_dict['stateful'] = 'stateful' in group['stateful'].lower()
                capabilities_dict['segment-routing'] = 'segment-routing' in group['segment_routing'].lower()
                capabilities_dict['update'] = 'update' in group['update'].lower()
                capabilities_dict['instantiation'] = 'instantiation' in group['instantiation'].lower()
            
            m = p18.match(line)
            if m:
                md5_status_bool = m.groupdict()['md5']
                address_dict['md5'] = md5_status_bool
            
            m = p19.match(line)
            if m:
                maximum_sid_depth_bool = int(m.groupdict()['maximum_sid_depth'])
                address_dict['maximum_sid_depth'] = maximum_sid_depth_bool

            m = p20.match(line)
            if m:
                last_pcerror_dict = address_dict.setdefault('last_pcerror', {})
                last_pcerror_flag = True
            
            m = p21.match(line)
            if m:
                group = m.groupdict()
                received_pcerror = group['received_pcerror']
                if last_pcerror_flag:
                    last_pcerror_dict['received'] = received_pcerror
            
            m = p22.match(line)
            if m:
                group = m.groupdict()
                sent_pcerror = group['sent_pcerror']
                if last_pcerror_flag:
                    last_pcerror_dict['sent'] = sent_pcerror

        return ret_dict


class ShowPceIPV4PeerprefixSchema(MetaParser):
    ''' Schema for:
        * show pce ipv4 prefix
    '''
    schema = {
        'nodes': {
            Any(): {
                'te_router_id': str,
                'host_name': str,
                'isis_system_id': list,
                Optional('asn'): list,
                Optional('domain_id'): list,
                'advertised_prefixes': list,
            },
        }
    }


class ShowPceIPV4PeerPrefix(ShowPceIPV4PeerprefixSchema):
    ''' Parser for:
        * show pce ipv4 prefix
    '''


    cli_command = 'show pce ipv4 prefix'

    def cli(self, output=None):

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        p1 = re.compile(r'Node (?P<node_number>\d+)')

        p2 = re.compile(r'^TE router ID: (?P<router_id>[\d\.]+)$')

        p3 = re.compile(r'^Host name: (?P<host_name>\w+)$')

        p4 = re.compile(r'^ISIS system ID: (?P<system_id>[\w\.]+\s+level-\d+)'
                        '( ASN: (?P<asn>\w+) domain ID: (?P<domain_id>\d+))*')

        p5 = re.compile(r'^(?P<adv_prefixes>\d+\.\d+\.\d+\.\d+)$')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                node = int(m.groupdict()['node_number'])
                prefix_dict = ret_dict.setdefault('nodes', {})
                node_dict = prefix_dict.setdefault(node, {})

            m = p2.match(line)
            if m:
                node_dict['te_router_id'] = m.groupdict()['router_id']

            m = p3.match(line)
            if m:
                node_dict['host_name'] = m.groupdict()['host_name']

            m = p4.match(line)
            if m:
                sys_id = m.groupdict()['system_id']
                node_dict.setdefault('isis_system_id', []).append(sys_id)

                if 'asn' in line.lower():
                    domain = int(m.groupdict()['domain_id'])
                    node_dict.setdefault('asn', []). \
                        append(int(m.groupdict()['asn']))

                    node_dict.setdefault('domain_id', []). \
                        append(int(m.groupdict()['domain_id']))

            m = p5.match(line)
            if m:
                node_dict.setdefault('advertised_prefixes', [])
                node_dict['advertised_prefixes']. \
                    append(m.groupdict()['adv_prefixes'])

        return ret_dict


class ShowPceIpv4TopologySummarySchema(MetaParser):
    ''' Schema for:
        * show pce ipv4 topology summary
    '''
    schema = {
        'pce_topology_database_summary': {
            'topology_nodes': int,
            'prefixes': int,
            'prefix_sids': {
                'total': int,
                Optional('regular'): int,
                Optional('strict'): int,
            },
            'links': {
                'total': int,
                Optional('epe'): int,
            },
            'adjancency_sids': {
                'total': int,
                Optional('unprotected'): int,
                Optional('protected'): int,
                Optional('epe'): int,
            },
            Optional('private_information'): {
                'lookup_nodes': int,
                'consistent': str,
                'update_stats': {
                    'noded': {
                        'added': int,
                        'deleted': int,
                    },
                    'links': {
                        'added': int,
                        'deleted': int,
                    },
                    'prefix': {
                        'added': int,
                        'deleted': int,
                    },
                }
            }
        }
    }


class ShowPceIpv4TopologySummary(ShowPceIpv4TopologySummarySchema):
    ''' parser for:
        * show pce ipv4 topology summary
    '''

    cli_command = 'show pce ipv4 topology summary'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        p1 = re.compile(r'^Topology nodes:\s+(?P<topology_nodes>\d+)$')

        p2 = re.compile(r'^Prefixes:\s+(?P<prefixes>\d+)$')

        p3 = re.compile(r'^Prefix +SIDs: +(?:(?P<prefix_sids>\d+))?$')

        p4 = re.compile(r'^Links: +(?:(?P<links>\d+))?$')

        p5 = re.compile(r'^Adjacency +SIDs: +(?:(?P<adjacency>\d+))?$')

        p6 = re.compile(r'^Total: +(?P<total>\d+)$')
        p7 = re.compile(r'^Regular: +(?P<regular>\d+)$')
        p8 = re.compile(r'^Strict: +(?P<strict>\d+)$')
        p9 = re.compile(r'^EPE: +(?P<epe>\d+)$')
        p10 = re.compile(r'^Unprotected: +(?P<unprotected>\d+)$')
        p11 = re.compile(r'^Protected: +(?P<protected>\d+)$')
        p12 = re.compile(r'^Lookup +Nodes +(?P<lookup>\d+)$')
        p13 = re.compile(r'^Consistent +(?P<consistent>\S+)$')
        p14 = re.compile(r'^Noded +added: +(?P<added>\d+)$')
        p15 = re.compile(r'^Noded +deleted: +(?P<deleted>\d+)$')

        p16 = re.compile(r'^Links +added: +(?P<added>\d+)$')
        p17 = re.compile(r'^Links +deleted: +(?P<deleted>\d+)$')

        p18 = re.compile(r'^Prefix +added: +(?P<added>\d+)$')
        p19 = re.compile(r'^Prefix +deleted: +(?P<deleted>\d+)$')

        parsed_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # Topology nodes:                0
            m = p1.match(line)
            if m:
                topology_dict = parsed_dict.setdefault \
                    ('pce_topology_database_summary', {})
                topology_dict['topology_nodes'] = \
                    int(m.groupdict()['topology_nodes'])
                continue

            # Prefixes:                      0
            m = p2.match(line)
            if m:
                topology_dict['prefixes'] = \
                    int(m.groupdict()['prefixes'])
                continue

            # Prefix SIDs:                 4
            m = p3.match(line)
            if m:
                if 'prefix_sids' not in topology_dict:
                    prefix_dict = topology_dict.setdefault('prefix_sids', {})
                prefix_dict['total'] = int(m.groupdict()['prefix_sids'])
                continue

            # Links:                 5
            m = p4.match(line)
            if m:
                if 'links' not in topology_dict:
                    link_dict = topology_dict.setdefault('links', {})
                link_dict['total'] = int(m.groupdict()['links'])
                continue

            # Adjacency SIDs:                 6
            m = p5.match(line)
            if m:
                if 'adjancency_sids' not in topology_dict:
                    adj_dict = topology_dict.setdefault('adjancency_sids', {})
                adj_dict['total'] = int(m.groupdict()['adjacency'])
                continue

            # Total:                       0
            m = p6.match(line)
            if m:
                if 'prefix_sids' not in topology_dict:
                    prefix_dict = topology_dict.setdefault('prefix_sids', {})
                    prefix_dict['total'] = int(m.groupdict()['total'])
                elif 'links' not in topology_dict:
                    link_dict = topology_dict.setdefault('links', {})
                    link_dict['total'] = int(m.groupdict()['total'])
                elif 'adjancency_sids' not in topology_dict:
                    adj_dict = topology_dict.setdefault('adjancency_sids', {})
                    adj_dict['total'] = int(m.groupdict()['total'])
                continue

            #  Regular:                     0
            m = p7.match(line)
            if m:
                prefix_dict['regular'] = int(m.groupdict()['regular'])
                continue

            # Strict:                      0
            m = p8.match(line)
            if m:
                prefix_dict['strict'] = int(m.groupdict()['strict'])
                continue

            # EPE:                         0
            m = p9.match(line)
            if m:
                if 'adjancency_sids' not in topology_dict:
                    link_dict['epe'] = int(m.groupdict()['epe'])
                else:
                    adj_dict['epe'] = int(m.groupdict()['epe'])
                continue

            # Unprotected:                 0
            m = p10.match(line)
            if m:
                adj_dict['unprotected'] = int(m.groupdict()['unprotected'])
                continue

            # Protected:                 0
            m = p11.match(line)
            if m:
                adj_dict['protected'] = int(m.groupdict()['protected'])
                continue

            # Lookup Nodes                   0
            m = p12.match(line)
            if m:
                if 'private_information' not in topology_dict:
                    private_dict = topology_dict.setdefault('private_information', {})
                private_dict['lookup_nodes'] = int(m.groupdict()['lookup'])
                continue

            # Consistent                   yes
            m = p13.match(line)
            if m:
                private_dict['consistent'] = str(m.groupdict()['consistent'])
                continue

            #   Noded added:                 0
            m = p14.match(line)
            if m:
                if 'update_stats' not in private_dict:
                    update_dict = private_dict.setdefault('update_stats', {})
                noded_dict = update_dict.setdefault('noded', {})
                noded_dict['added'] = int(m.groupdict()['added'])
                continue

            #   Noded deleted:               0
            m = p15.match(line)
            if m:
                noded_dict['deleted'] = int(m.groupdict()['deleted'])
                continue

            #   Links added:                 0
            m = p16.match(line)
            if m:
                if 'links' not in update_dict:
                    update_links_dict = update_dict.setdefault('links', {})
                update_links_dict['added'] = int(m.groupdict()['added'])
                continue

            #   Links deleted:               0
            m = p17.match(line)
            if m:
                update_links_dict['deleted'] = int(m.groupdict()['deleted'])
                continue

            #   Prefix added:                0
            m = p18.match(line)
            if m:
                if 'prefix' not in update_dict:
                    update_prefix_dict = update_dict.setdefault('prefix', {})
                update_prefix_dict['added'] = int(m.groupdict()['added'])
                continue

            #   Prefix deleted:              0
            m = p19.match(line)
            if m:
                update_prefix_dict['deleted'] = int(m.groupdict()['deleted'])
                continue

        return parsed_dict


class ShowPceLspSchema(MetaParser):
    ''' Schema for:
            show pce lsp
    '''
    schema = {
        'pcc': {
            Any(): {
                'tunnel_name': {
                    Any(): {
                        'lsps': {
                            Any(): {
                                'source': str,
                                'destination': str,
                                'tunnel_id': int,
                                'lsp_id': int,
                                'admin_state': str,
                                'operation_state': str,
                                'setup_type': str,
                                'binding_sid': int
                            },
                        }
                    },
                }
            },
        }

    }


class ShowPceLsp(ShowPceLspSchema):
    ''' Parser for:
            show pce lsp
    '''

    cli_command = 'show pce lsp'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        p1 = re.compile(r'^PCC (?P<pcc_id>[\d\.]+):$')

        p2 = re.compile(r'^Tunnel Name: (?P<tunnel_name>\w+)$')

        p3 = re.compile(r'^LSP\[(?P<lsp_number>\d+)\]:$')

        p4 = re.compile(r'^source (?P<lsp_source>[\d\.]+), destination '
                        '(?P<lsp_destination>[\d\.]+), tunnel ID (?P<tunnel_id>\d+), '
                        'LSP ID (?P<lsp_id>\d+)$')

        p5 = re.compile(r'State: Admin (?P<admin_state>\w+), Operation '
                        '(?P<operation_state>\w+)$')

        p6 = re.compile(r'^Setup type: (?P<setup_type>[\w\s]+)$')

        p7 = re.compile(r'^Binding SID: (?P<binding_sid>\d+)$')

        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                pcc_id = m.groupdict()['pcc_id']
                pccs_dict = ret_dict.setdefault('pcc', {})

                pcc_dict = pccs_dict.setdefault(pcc_id, {})

            m = p2.match(line)
            if m:
                tunnel_name = m.groupdict()['tunnel_name']

                tunnels_dict = pcc_dict.setdefault('tunnel_name', {})
                tunnel_dict = tunnels_dict.setdefault(tunnel_name, {})

            m = p3.match(line)
            if m:
                lsp_numb = int(m.groupdict()['lsp_number'])

                lsps_dict = tunnel_dict.setdefault('lsps', {})
                lsp_dict = lsps_dict.setdefault(lsp_numb, {})

            m = p4.match(line)
            if m:
                lsp_dict['source'] = m.groupdict()['lsp_source']
                lsp_dict['destination'] = m.groupdict()['lsp_destination']
                lsp_dict['tunnel_id'] = int(m.groupdict()['tunnel_id'])
                lsp_dict['lsp_id'] = int(m.groupdict()['lsp_id'])

            m = p5.match(line)
            if m:
                admin_state = m.groupdict()['admin_state'].lower()
                operation_state = m.groupdict()['operation_state'].lower()

                lsp_dict['admin_state'] = admin_state
                lsp_dict['operation_state'] = operation_state

            m = p6.match(line)
            if m:
                lsp_dict['setup_type'] = m.groupdict()['setup_type']

            m = p7.match(line)
            if m:
                lsp_dict['binding_sid'] = int(m.groupdict()['binding_sid'])

        return ret_dict


class ShowPceLspDetailSchema(MetaParser):
    ''' Schema for:
       * show pce lsp detail
    '''
    schema = {
        'pcc': {
            Any(): {
                'tunnel_name': str,
                'lsps': {
                    Any(): {
                        'source': str,
                        'destination': str,
                        'tunnel_id': int,
                        'lsp_id': int,
                        'admin_state': str,
                        'operation_state': str,
                        'setup_type': str,
                        'binding_sid': int,
                        'pcep_information': {
                            'plsp_id': int,
                            'flags': {
                                'd': int,
                                's': int,
                                'r': int,
                                'a': int,
                                'o': int,
                            }
                        },
                        'paths': {
                            Any(): {
                                Optional('metric_type'): str,
                                Optional('accumulated_metric'): int,
                                Optional('none'): str,
                                Optional('sids'): {
                                    Any(): {
                                        'type': str,
                                        'label': int,
                                        'local_address': str,
                                        'remote_address': str,
                                    },
                                },
                            },
                        },
                    },
                    'event_history': {
                        Any(): {
                            Any(): {
                                'symbolic_name': str,
                                Optional('lsp-id'): int,
                                Optional('plsp-id'): int,
                                Optional('source'): str,
                                Optional('destination'): str,
                                Optional('flags'): {
                                    'd': int,
                                    'r': int,
                                    'a': int,
                                    'o': int,
                                    'sig_bw': int,
                                    'act_bw': int,
                                },
                                Optional('peer'): str,
                            },
                        },
                    }
                }
            },
        }
    }


class ShowPceLspDetail(ShowPceLspDetailSchema):
    ''' Parser for:
       * show pce lsp detail
    '''

    cli_command = 'show pce lsp detail'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        p1 = re.compile(r'^PCC (?P<pcc_id>[\d\.]+):$')

        p2 = re.compile(r'^Tunnel Name: (?P<tunnel_name>\w+)$')

        p3 = re.compile(r'^LSP\[(?P<lsp_number>\d+)\]:$')

        p4 = re.compile(r'^source (?P<lsp_source>[\d\.]+), destination '
                        '(?P<lsp_destination>[\d\.]+), tunnel ID '
                        '(?P<tunnel_id>\d+), LSP ID (?P<lsp_id>\d+)$')

        p5 = re.compile(r'State: Admin (?P<admin_state>\w+), Operation '
                        '(?P<operation_state>\w+)$')

        p6 = re.compile(r'^Setup type: (?P<setup_type>[\w\s]+)$')

        p7 = re.compile(r'^Binding SID: (?P<binding_sid>\d+)$')

        p8 = re.compile(r'^plsp-id (?P<plsp_id>\d+), flags: D:(?P<d_flag>\d+) '
                        'S:(?P<s_flag>\d+) R:(?P<r_flag>\d+) A:'
                        '(?P<a_flag>\d+) O:(?P<o_flag>\d+)$')

        #   Reported path: 
        p9 = re.compile(r'^(?P<specified_path>\w+) path:$')

        p10 = re.compile(r'^Metric type: (?P<metric_type>\w+), '
                         'Accumulated Metric (?P<accumulated_metric>\d+)$')

        # SID[0]: Adj, Label 24000, Address: local 10.10.10.1 remote 10.10.10.2
        p11 = re.compile(r'^SID\[(?P<sid_number>\d+)\]: (?P<sid_type>\w+), '
                         'Label (?P<sid_label>\d+), Address: local '
                         '(?P<sid_local_address>[\d\.]+) remote '
                         '(?P<sid_remote_address>[\d\.]+)$')
        # June 13 2016 13:28:29     Report
        p12 = re.compile(r'^(?P<event_time>\w+ \d+ \d+ [\d\:]+)\s+ '
                         '(?P<event_type>\w+)$')
        # Symbolic-name: rtrA_t1, LSP-ID: 2,
        p13 = re.compile(r'^Symbolic-name: (?P<symbolic_name>\w+), '
                         '(?P<id_name>[\w\-]+): (?P<symbolic_id>\d+),$')
        # Source: 192.168.0.1 Destination: 192.168.0.4,
        p14 = re.compile(r'^Source: (?P<event_source>[\d\.]+) Destination: '
                         '(?P<dest_source>[\d\.]+),$')

        # D:1, R:0, A:1 O:1, Sig.BW: 0, Act.BW: 0
        p15 = re.compile(r'^D:(?P<d_event>\d+), R:(?P<r_event>\d+), '
                         'A:(?P<a_event>\d+) O:(?P<o_event>\d+), Sig\.BW: '
                         '(?P<event_sig>\d+), Act.BW: (?P<event_act>\d+)$')

        p16 = re.compile(r'Peer: (?P<event_peer>[\d\.]+)')

        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                pcc_id = m.groupdict()['pcc_id']
                pccs_dict = ret_dict.setdefault('pcc', {})

                pcc_dict = pccs_dict.setdefault(pcc_id, {})

            m = p2.match(line)
            if m:
                pcc_dict['tunnel_name'] = m.groupdict()['tunnel_name']

            m = p3.match(line)
            if m:
                lsp_numb = int(m.groupdict()['lsp_number'])

                lsps_dict = pcc_dict.setdefault('lsps', {})
                lsp_dict = lsps_dict.setdefault(lsp_numb, {})

            m = p4.match(line)
            if m:
                lsp_dict['source'] = m.groupdict()['lsp_source']
                lsp_dict['destination'] = m.groupdict()['lsp_destination']
                lsp_dict['tunnel_id'] = int(m.groupdict()['tunnel_id'])
                lsp_dict['lsp_id'] = int(m.groupdict()['lsp_id'])

            m = p5.match(line)
            if m:
                admin_state = m.groupdict()['admin_state'].lower()
                operation_state = m.groupdict()['operation_state'].lower()
                lsp_dict.setdefault('admin_state', admin_state)
                lsp_dict.setdefault('operation_state', operation_state)

            m = p6.match(line)
            if m:
                lsp_dict['setup_type'] = m.groupdict()['setup_type'].lower()

            m = p7.match(line)
            if m:
                lsp_dict['binding_sid'] = int(m.groupdict()['binding_sid'])

            m = p8.match(line)
            if m:
                pcep_info_dict = lsp_dict.setdefault('pcep_information', {})
                pcep_info_dict['plsp_id'] = int(m.groupdict()['plsp_id'])
                flags_dict = pcep_info_dict.setdefault('flags', {})
                flags_dict['d'] = int(m.groupdict()['d_flag'])
                flags_dict['s'] = int(m.groupdict()['s_flag'])
                flags_dict['r'] = int(m.groupdict()['r_flag'])
                flags_dict['a'] = int(m.groupdict()['a_flag'])
                flags_dict['o'] = int(m.groupdict()['o_flag'])

            m = p9.match(line)
            if m:
                path = m.groupdict()['specified_path'].lower()
                path_dict = lsp_dict.setdefault('paths', {}).setdefault(path, {})

            m = p10.match(line)
            if m:
                path_dict['metric_type'] = m.groupdict()['metric_type']
                path_dict['accumulated_metric'] = \
                    int(m.groupdict()['accumulated_metric'])

            m = p11.match(line)
            if m:
                sid_number = int(m.groupdict()['sid_number'])
                sid_dict = path_dict.setdefault('sids', {}). \
                    setdefault(sid_number, {})

                sid_dict['type'] = m.groupdict()['sid_type']
                sid_dict['label'] = int(m.groupdict()['sid_label'])
                sid_dict['local_address'] = m.groupdict()['sid_local_address']
                sid_dict['remote_address'] = \
                    m.groupdict()['sid_remote_address']

            m = p12.match(line)
            if m:
                event_time = m.groupdict()['event_time']
                event_type = m.groupdict()['event_type'].lower()

                time_dict = lsps_dict.setdefault('event_history', {}). \
                    setdefault(event_time, {})

                event_dict = time_dict.setdefault(event_type, {})

            m = p13.match(line)
            if m:
                id_name = m.groupdict()['id_name'].lower()
                event_dict['symbolic_name'] = m.groupdict()['symbolic_name']
                event_dict[id_name] = int(m.groupdict()['symbolic_id'])

            m = p14.match(line)
            if m:
                event_dict['source'] = m.groupdict()['event_source']
                event_dict['destination'] = m.groupdict()['dest_source']

            m = p15.match(line)
            if m:
                flag_dict = event_dict.setdefault('flags', {})
                flag_dict['d'] = int(m.groupdict()['d_event'])
                flag_dict['r'] = int(m.groupdict()['r_event'])
                flag_dict['a'] = int(m.groupdict()['a_event'])
                flag_dict['o'] = int(m.groupdict()['o_event'])
                flag_dict['sig_bw'] = int(m.groupdict()['event_sig'])
                flag_dict['act_bw'] = int(m.groupdict()['event_act'])

            m = p16.match(line)
            if m:
                if 'peer' in line.lower():
                    event_dict['peer'] = m.groupdict()['event_peer']

        return ret_dict


class ShowSegmentRoutingLocalBlockInconsistenciesSchema(MetaParser):
    ''' Schema for:
        * show segment-routing local-block inconsistencies
    '''

    schema = {
        'srlb_inconsistencies_range': {
            'start': int,
            'end': int,
        }
    }


class ShowSegmentRoutingLocalBlockInconsistencies(ShowSegmentRoutingLocalBlockInconsistenciesSchema):
    ''' Parser for: 
        * show segment-routing local-block inconsistencies
    '''

    cli_command = 'show segment-routing local-block inconsistencies'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        # SRLB inconsistencies range: Start/End: 30000/30009
        p1 = re.compile(r'(?P<inconsistency_type>\w+) inconsistencies range: '
                        'Start\/End: (?P<start>\d+)\/(?P<end>\d+)')

        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                inconsistency_dict = ret_dict. \
                    setdefault('srlb_inconsistencies_range', {})

                inconsistency_dict['start'] = int(m.groupdict()['start'])
                inconsistency_dict['end'] = int(m.groupdict()['end'])

        return ret_dict


class ShowSegmentRoutingMappingServerPrefixSidMapIPV4Schema(MetaParser):
    ''' Schema for:
        * show segment-routing mapping-server prefix-sid-map ipv4
    '''

    schema = {
        'ipv4': {
            'number_of_mapping_entries': int,
            'prefix': {
                Any(): {
                    'sid_index': int,
                    'range': int,
                    Optional('flags'): str,
                },
            }
        }
    }


class ShowSegmentRoutingMappingServerPrefixSidMapIPV4(ShowSegmentRoutingMappingServerPrefixSidMapIPV4Schema):
    ''' Parser for:
        * show segment-routing mapping-server prefix-sid-map ipv4
    '''

    cli_command = 'show segment-routing mapping-server prefix-sid-map ipv4'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # 10.186.1.0/24          400          300          
        p1 = re.compile(r'(?P<prefix>[\w\.\/]+)\s+(?P<sid_index>\d+)'
                        '\s+(?P<range>\d+)(\s+(?P<flags>)[\w\s]+$)?')
        # Number of mapping entries: 2
        p2 = re.compile(r'Number of mapping entries:\s+(?P<entries>\d+)')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                prefix = m.groupdict()['prefix']
                ipv_dict = ret_dict.setdefault('ipv4', {})
                prefixes_dict = ipv_dict.setdefault('prefix', {})

                prefix_dict = prefixes_dict.setdefault(prefix, {})

                prefix_dict['sid_index'] = int(m.groupdict()['sid_index'])
                prefix_dict['range'] = int(m.groupdict()['range'])

                if m.groupdict()['flags']:
                    prefix_dict['flags'] = m.groupdict()['flags']

            m = p2.match(line)
            if m:
                ipv_dict.setdefault('number_of_mapping_entries', \
                                    int(m.groupdict()['entries']))

        return ret_dict


class ShowSegmentRoutingMappingServerPrefixSidMapIPV4DetailSchema(MetaParser):
    ''' Schema for:
        * show segment-routing mapping-server prefix-sid-map ipv4 detail
    '''

    schema = {
        'ipv4': {
            'prefix': {
                Any(): {
                    'sid_index': int,
                    'range': int,
                    Optional('last_prefix'): str,
                    Optional('last_sid_index'): int,
                    Optional('flags'): str,
                },
            }
        }
    }


class ShowSegmentRoutingMappingServerPrefixSidMapIPV4Detail(
    ShowSegmentRoutingMappingServerPrefixSidMapIPV4DetailSchema):
    ''' Parser for:
        * show segment-routing mapping-server prefix-sid-map ipv4 detail
    '''

    cli_command = 'show segment-routing mapping-server prefix-sid-map ipv4 detail'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # 10.186.1.0/24
        p1 = re.compile(r'^(?P<prefix>\d+\.\d+\.\d+\.\d+\/\d+)$')

        # SID Index:      400
        p2 = re.compile(r'^SID Index:\s+(?P<sid_index>\d+)$')

        # Range:          300
        p3 = re.compile(r'^Range:\s+(?P<range>\d+)$')

        # Last Prefix:    10.229.44.0/24
        p4 = re.compile(r'^Last Prefix:\s+(?P<last_prefix>[\d\.\/]+)$')

        # Last SID Index: 699
        p5 = re.compile(r'^Last SID Index: (?P<last_sid_index>\d+)$')

        # Flags
        p6 = re.compile(r'^Flags:\s+(?P<flags>\w+)$')

        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                prefix = m.groupdict()['prefix']

                ipv4_dict = ret_dict.setdefault('ipv4', {})
                prefixes_dict = ipv4_dict.setdefault('prefix', {})
                prefix_dict = prefixes_dict.setdefault(prefix, {})

            m = p2.match(line)
            if m:
                prefix_dict['sid_index'] = int(m.groupdict()['sid_index'])

            m = p3.match(line)
            if m:
                prefix_dict['range'] = int(m.groupdict()['range'])

            m = p4.match(line)
            if m:
                prefix_dict['last_prefix'] = m.groupdict()['last_prefix']

            m = p5.match(line)
            if m:
                prefix_dict['last_sid_index'] = \
                    int(m.groupdict()['last_sid_index'])

            m = p6.match(line)
            if m:
                prefix_dict['flags'] = m.groupdict()['flags']

        return ret_dict


################################################################################

"""Schema for 'show segment-routing srv6 sid'"""
class ShowSegmentRoutingSrv6LocatorSidSchema(MetaParser):
    schema = {
        'locator': {
            Any(): {
                'sid': {
                    Any(): {
                        'behavior': str,
                        'context': str,
                        'owner': str,
                        'state': str,
                        'rw': str
                    }
                }
            }
        }
    }

# ==============================================
# Parser for 'show segment-routing srv6 sid'
# ==============================================

class ShowSegmentRoutingSrv6LocatorSid(ShowSegmentRoutingSrv6LocatorSidSchema):
    """Parser for:
    * show segment-routing srv6 sid
    * show segment-routing srv6 locator {locator} sid"""

    cli_command = ['show segment-routing srv6 sid',
                   'show segment-routing srv6 locator {locator} sid']

    def cli(self, locator=None, output=None):

        if output is None:
            if locator:
                output = self.device.execute(self.cli_command[1].format(locator=locator))
            else:
                output = self.device.execute(self.cli_command[0])

        ret_dict = {}
        locator_dict = ret_dict.setdefault('locator',{})

        # SID    Behavior    Context    Owner    State    RW
        p = re.compile(r'SID\s+Behavior\s+Context\s+Owner\s+State\s+RW')
        
        # *** Locator: 'ALGO_0' ***
        p1 = re.compile(r'^\*+\s+Locator:\s+\'(?P<locator>\S+)\'\s+\*+$')
        
        # cafe:0:200::                uN (PSP/USD)      'default':512                     sidmgr              InUse  Y
        # cafe:0:200:e000::           uDT2U             1:0                               l2vpn_srv6          InUse  Y
        p2 = re.compile(r'^(?P<sid>[\w+:]+)\s+(?P<behavior>\S+\s?\S+) +'
                        r'\s+(?P<context>\S+\s?\S+)\s+(?P<owner>\S+)\s+(?P<state>\S+)\s+(?P<rw>\S+)$')

        for line in output.splitlines():
            line = line.strip()
            # SID    Behavior    Context    Owner    State    RW
            if p.match(line):
                continue
            # *** Locator: 'ALGO_0' ***
            m = p1.match(line)
            if m:
                locator = m.groupdict()['locator']
                continue

            # cafe:0:200::                uN (PSP/USD)      'default':512                     sidmgr              InUse  Y
            # cafe:0:200:e000::           uDT2U             1:0                               l2vpn_srv6          InUse  Y
            m = p2.match(line)
            if m:
                group = m.groupdict()
                sid = group.pop('sid')
                sid_dict = locator_dict.setdefault(locator, {}).setdefault('sid',{}).setdefault(sid,{})
                sid_dict.update(group)
                continue

        return ret_dict

class ShowSegmentRoutingSrv6LocatorSchema(MetaParser):
    ''' Schema for:
        * show segment-routing srv6 locator
        * show segment-routing srv6 locator {locator_name}
    '''
    schema = {
        'locators': {
            Any(): {
                'name': str,
                'id': int,
                'algorithm': int,
                'prefix': str,
                'status': str,
                'flags': str
            }
        }
    }


class ShowSegmentRoutingSrv6Locator(ShowSegmentRoutingSrv6LocatorSchema):
    ''' Parser for:
        * show segment-routing srv6 locator
        * show segment-routing srv6 locator {locator_name}
    '''
    cli_command = ['show segment-routing srv6 locator',
                   'show segment-routing srv6 locator {locator_name}']

    def cli(self, locator_name=None, output=None):
        if output is None:
            if locator_name:
                output = self.device.execute(self.cli_command[1].format(locator_name=locator_name))
            else:
                output = self.device.execute(self.cli_command[0])

        # LL                    1        128   fc00:c001:1001::/48       Up       U
        # MAIN                  2        0     fc00:c000:1001::/48       Up       U
        p1 = re.compile(r'^(?P<name>\w+)\s+(?P<id>\d+)\s+(?P<algorithm>\d+)\s+(?P<prefix>[\w:\/]+)\s+(?P<status>[Up|Dn]+)\s+(?P<flags>[U])$')

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # LL                    1        128   fc00:c001:1001::/48       Up       U
            # MAIN                  2        0     fc00:c000:1001::/48       Up       U
            m = p1.match(line)
            if m:
                group = m.groupdict()
                locator_dict = ret_dict.setdefault('locators', {}). \
                                    setdefault(group['name'], {})
                locator_dict['name'] = group['name']
                locator_dict['id'] = int(group['id'])
                locator_dict['algorithm'] = int(group['algorithm'])
                locator_dict['prefix'] = group['prefix']
                locator_dict['status'] = group['status']
                locator_dict['flags'] = group['flags']
                continue

        return ret_dict

class ShowSegmentRoutingTrafficEnggPccLspSchema(MetaParser):
    ''' Schema for:
        * show segment-routing traffic-eng pcc lsp
    '''
    schema = {
        'pce_sr_policy_database': {
            'symbolic_name': str,
            'lsps': {
                Any(): {
                 'source': str,
                 'destination': str,
                 'tunnel_id': int,
                 'lsp_id': int,
                 'admin_state': str,
                 'operation_state': str,
                 'setup_type': str,
                 'binding_sid': int
                },
            },
        },
    }
    
class ShowSegmentRoutingTrafficEnggPccLsp(
    ShowSegmentRoutingTrafficEnggPccLspSchema):
    ''' Parser for:
        * ShowSegmentRoutingTrafficEnggPccLsp
    '''

    cli_command = 'show segment-routing traffic-eng pcc lsp'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Symbolic Name: cfg_srte_c_30_ep_10.0.0.14_discr_100
        p1 = re.compile(r'^Symbolic Name: (?P<symbolic_name>[A-Za-z0-9_?.?]+)$')
        
        # LSP[0]:
        p2 = re.compile(r'^LSP\[(?P<lsp_number>\d+)\]:$')
 
        # Source 10.0.0.2, Destination 10.0.0.14, Tunnel ID 1, LSP ID 1048
        p3 = re.compile(r'^Source (?P<lsp_source>[\d\.]+), Destination '
                        '(?P<lsp_destination>[\d\.]+), Tunnel ID (?P<tunnel_id>\d+), '
                        'LSP ID (?P<lsp_id>\d+)$')
        
        # State: Admin up, Operation up
        p4 = re.compile(r'State: Admin (?P<admin_state>\w+), Operation '
                          '(?P<operation_state>\w+)$')
        
        # Setup type: SR
        p5 = re.compile(r'^Setup type: (?P<setup_type>[\w\s]+)$')

        # Binding SID: 26276
        p6 = re.compile(r'^Binding SID: (?P<binding_sid>\d+)$')

        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # Symbolic Name: cfg_srte_c_30_ep_10.0.0.14_discr_100 
            m = p1.match(line)
            if m:
                policy_dict = ret_dict.setdefault \
                    ('pce_sr_policy_database', {})
                policy_dict['symbolic_name'] = \
                    str(m.groupdict()['symbolic_name'])
                continue
            
            # LSP[0]:
            m = p2.match(line)
            if m:
                lsp_numb = int(m.groupdict()['lsp_number'])
                lsps_dict = policy_dict.setdefault('lsps', {})
                lsp_dict = lsps_dict.setdefault(lsp_numb, {})
                continue
            
            # Source 10.0.0.2, Destination 10.0.0.14, Tunnel ID 1, LSP ID 1048
            m = p3.match(line)
            if m:
                lsp_dict['source'] = str(m.groupdict()['lsp_source'])
                lsp_dict['destination'] = str(m.groupdict()['lsp_destination'])
                lsp_dict['tunnel_id'] = int(m.groupdict()['tunnel_id'])
                lsp_dict['lsp_id'] = int(m.groupdict()['lsp_id'])
                continue
            
            # State: Admin up, Operation up
            m = p4.match(line)
            if m:
                admin_state = m.groupdict()['admin_state'].lower()
                operation_state = m.groupdict()['operation_state'].lower()
                lsp_dict.setdefault('admin_state', admin_state)
                lsp_dict.setdefault('operation_state', operation_state)
                continue
            
            # Setup type: SR
            m = p5.match(line)
            if m:
                lsp_dict['setup_type'] = m.groupdict()['setup_type'].lower()
                continue
            
            # Binding SID: 26276
            m = p6.match(line)
            if m:
                lsp_dict['binding_sid'] = int(m.groupdict()['binding_sid'])
                continue

        return ret_dict

# ==================================================================
# Parser for:
#    * 'show segment-routing traffic-eng policy color {color_code} endpoint ipv4 {endpoint_ip}'
# ==================================================================
class ShowSegmentRoutingTrafficEngPolicyColorEndpointSchema(MetaParser):
    """Schema for
    'show segment-routing traffic-eng policy color {color_code} endpoint ipv4 {endpoint_ip}'
    """

    schema = {
        "pce_sr_policy_database": {
            "color": int,
            "end_point": str,
            "name": str,
            "status": {
                "admin": str,
                "operational": {
                    "state": str,
                    "time_for_state": str,
                    "since": str,
                },
            },
            Optional("candidate_paths"): {
                "preference": {
                    Any(): {
                        Optional("name"): str,
                        Optional("Requested_bsid"): str,
                        "pcc_info": {
                            "symbolic_name": str,
                            Optional("plsp_id"): int,
                        },
                        "constraints": {
                            "protection_type": str,
                            Optional("maximum_dept"): int,
                        },
                        "path_type": {
                            Optional("dynamic"): {
                                "status": str,
                                Optional("pce"): bool,
                                "metric_type": str,
                                Optional("path_accumulated_metric"): int,
                                Optional("hops"): {
                                    Any(): {
                                        "sid": int,
                                        Optional("sid_type"): str,
                                        Optional("local_address"): str,
                                        Optional("remote_address"): str,
                                    },
                                },
                            },
                        },
                    },
                },
            },
            Optional("attributes"): {
                    Optional("binding_sid"): str,
                    Optional("forward_class"): str,
                    Optional("steering_labeled_services_disabled"): str,
                    Optional("steering_bgp_disabled"): str,
                    Optional("ipv6_caps_enable"): str,
                    Optional("invalidation_drop_enabled"): str,
                    Optional("max_install_standby_candidate_paths"): int,
                },
            },
        }
    
class ShowSegmentRoutingTrafficEngPolicyColorEndpoint(ShowSegmentRoutingTrafficEngPolicyColorEndpointSchema):
    """ Parser for 
        'show segment-routing traffic-eng policy color {color_code} endpoint ipv4 {endpoint_ip}'
    """

    cli_command = 'show segment-routing traffic-eng policy color {color_code} endpoint ipv4 {endpoint_ip}'

    def cli(self, color_code='', endpoint_ip='', output=None):
        if output is None:
            cmd = self.cli_command.format(color_code=color_code, endpoint_ip=endpoint_ip)
                
            output = self.device.execute(cmd)

        # Color: 30, End-point: 10.0.0.14
        p1 = re.compile(r'^Color: +(?P<color>\d+), +End-point: *(?P<end_point>\S+)')
        
        # Name: srte_c_30_ep_10.0.0.14
        p2 = re.compile(r'^Name: +(?P<name>\S+)')
        
        # Admin: up  Operational: up for N/A (since Oct 25 07:51:47.805)
        p3 = re.compile(r'^Admin: (?P<admin>\w+)\s+Operational:\s+(?P<oper>\w+)\s+for\s+(?P<time>\S+) \(since\s(?P<since>\S+\s+\S+\s\S+)')
        
        # Preference: 100 (configuration) (active) (reoptimizing)
        p4 = re.compile(r'^Preference:\s+(?P<preference>\d+)')
        
        # Name: srte_c_30_ep_10.0.0.14    
        p5 = re.compile(r'^Name: +(?P<per_name>\S+)')
        
        #  Requested BSID: dynamic
        p6 = re.compile(r'^Requested\s+BSID:\s+(?P<bsid>\w+)')
       
        # Symbolic name: cfg_srte_c_30_ep_10.0.0.14_discr_100
        p7 = re.compile(r'^Symbolic name: (?P<symbolic_name>[A-Za-z0-9_?.?]+)$')
        
        # PLSP-ID: 1
        p8 = re.compile(r'^PLSP-ID:\s+(?P<plsp_id>\d+)')
        
        # Protection Type: protected-preferred
        p9 = re.compile(r'^Protection\s+Type:\s(?P<protection_type>\S+)')
        
        # Maximum SID Depth: 12
        p10 = re.compile(r'^Maximum\s+SID\s+Depth:\s+(?P<maximum_sid_depth>\d+)')
        
        # Dynamic (pce 10.0.0.11) (valid)
        p11 = re.compile(r'^Dynamic( +(?P<pce>\(pce.*\)))? +\((?P<status>\w+)\)$')

        # Metric Type: IGP, Path Accumulated Metric: 2200
        p12 = re.compile(r'^Metric +Type: +(?P<metric_type>[\S]+)\s+Path\s+Accumulated\s+Metric:\s+(?P<path_accumulated_metric>\d+)')
        
        #         16063 [Prefix-SID, 10.169.196.241]
        #         16072 [Prefix-SID, 10.189.5.253 - 10.189.6.253]
        #         16063
        p13 = re.compile(r'^(?P<sid>[\d]+)(?: +\[(?P<sid_type>[\S]+), +(?P<local_address>[\S]+)'
                         '( +- +(?P<remote_address>[\S]+))?\])?$')
        
        #     Binding SID: 15000
        p14 = re.compile(r'^Binding +SID: +(?P<binding_sid>[\d]+)$')
        
        # Forward Class: Not Configured
        p15 = re.compile(r'^Forward\s+Class:\s+(?P<forward_class>\w+\s?\w+)$')
        
        # Steering labeled-services disabled: no
        p16 = re.compile(r'^Steering\s+labeled.?services\s+disabled:\s+(?P<steering_labled_services_status>\w+)')
        
        #Steering BGP disabled: no
        p17 = re.compile(r'^Steering\s+BGP\s+disabled:\s+(?P<steering_bgp_status>\w+)$')
        
        # IPv6 caps enable: yes
        p18 = re.compile(r'^IPv6\s+caps\s+enable:\s+(?P<ipv6_caps_status>\w+)$')
        
        # Invalidation drop enabled: no
        p19 = re.compile(r'^Invalidation\s+drop\s+enabled:\s+(?P<invalidation_drop_status>\w+)$')
        
        # Max Install Standby Candidate Paths: 0
        p20 = re.compile(r'^Max\s+Install\s+Standby\s+Candidate\s+Paths:\s+(?P<max_install_standby_pats>\d+)$')
        
        # initial variables
        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            # Color: 30, End-point: 10.0.0.14
            m = p1.match(line)
            if m:
                group = m.groupdict()
                color = int(group['color'])
                policy_dict = ret_dict.setdefault \
                    ('pce_sr_policy_database', {})
                policy_dict['color'] = color
                policy_dict['end_point'] = group['end_point']
                continue
            
            # Name: srte_c_30_ep_10.0.0.14
            m = p2.match(line)
            if m:
                group = m.groupdict()
                policy_dict['name'] = group['name']
                continue
            

            # Admin: up, Operational: up for 09:38:18 (since 08-28 20:56:55.275)
            m = p3.match(line)
            if m:
                group = m.groupdict()
                status_dict = policy_dict.setdefault('status', {})
                status_dict['admin'] = group['admin']

                oper_dict = status_dict.setdefault('operational', {})
                oper_dict['state'] = group['oper']
                oper_dict['time_for_state'] = group['time']
                oper_dict['since'] = group['since']
                continue
            
            # Preference: 100 (configuration) (active) (reoptimizing)
            m = p4.match(line)
            if m:
                group = m.groupdict()
                pref = int(group['preference'])
                pref_dict = policy_dict.setdefault("candidate_paths", {}).\
                            setdefault('preference', {}).setdefault(pref, {})
                hop_index = 0
                continue
            
            # Name: srte_c_30_ep_10.0.0.14
            m = p5.match(line)
            if m:
                group = m.groupdict()
                pref_dict['name'] = group['per_name']
                continue

            # Requested BSID: dynamic
            m = p6.match(line)
            if m:
                group = m.groupdict()
                pref_dict['Requested_bsid'] = group['bsid']
                continue  
            
            # Symbolic name: cfg_srte_c_30_ep_10.0.0.14_discr_100
            m = p7.match(line)
            if m:
                group = m.groupdict()
                pcc_dict = pref_dict.setdefault('pcc_info', {})
                pcc_dict['symbolic_name'] = group['symbolic_name']
                continue
            
            # PLSP-ID: 1
            m = p8.match(line)
            if m:
                group = m.groupdict()
                pcc_dict['plsp_id'] = int(group['plsp_id'])
                continue
            
            # Protection Type: protected-preferred
            m = p9.match(line)
            if m:
                group = m.groupdict()
                constraints_dict = pref_dict.setdefault('constraints', {})
                constraints_dict['protection_type'] = group['protection_type']
                continue
            
            # Maximum SID Depth: 12 
            m = p10.match(line)
            if m:
                group = m.groupdict()
                constraints_dict['maximum_dept'] = int(group['maximum_sid_depth'])
                continue
            
            # Dynamic (pce 10.0.0.11) (valid)
            m = p11.match(line)
            if m:
                group = m.groupdict()
                path_dict = pref_dict.setdefault('path_type', {}).setdefault('dynamic', {})
                path_dict['status'] = group['status']
           
            # Metric Type: TE,   Path Accumulated Metric: 260    
            m = p12.match(line)
            if m:
                group = m.groupdict()
                path_dict['metric_type'] = group['metric_type']

                if group.get('path_accumulated_metric'):
                   metric = int(group['path_accumulated_metric'])
                   path_dict['path_accumulated_metric'] = metric
                continue
            
            # 24000 [Adjacency-SID, 10.2.12.1 - 10.2.12.2]
            # 24008 [Adjacency-SID, 10.12.14.1 - 10.12.14.2]     
            m = p13.match(line)
            if m:
                hop_index += 1
                group = m.groupdict()
                hop_dict = path_dict.setdefault('hops', {}).setdefault(hop_index, {})
                
                hop_dict.update({'sid': int(group['sid'])})
                if group.get('sid_type'):
                    hop_dict['sid_type'] = group['sid_type']
                if group.get('local_address'):
                    hop_dict['local_address'] = group['local_address']
                if group.get('remote_address'):
                    hop_dict['remote_address'] = group['remote_address']
                continue
            
            # Attributes:
            #   Binding SID: 15000
            m = p14.match(line)
            if m:
                group = m.groupdict()
                bind_dict = policy_dict.setdefault("attributes", {})
                bind_dict['binding_sid'] = group['binding_sid']
                
            # Forward Class: Not Configured    
            m = p15.match(line)
            if m:
                group = m.groupdict()
                bind_dict['forward_class'] = group['forward_class']
                continue
            
            # Steering labeled-services disabled: no
            m = p16.match(line)
            if m:
                group = m.groupdict()
                bind_dict['steering_labeled_services_disabled'] = group['steering_labled_services_status']
                continue
            
            # Steering BGP disabled: no
            m = p17.match(line)
            if m:
                group = m.groupdict()
                bind_dict['steering_bgp_disabled'] = group['steering_bgp_status']
                continue  
            
            # IPv6 caps enable: yes
            m = p18.match(line)
            if m:
                group = m.groupdict()
                bind_dict['ipv6_caps_enable'] = group['ipv6_caps_status']
                continue
            
            # Invalidation drop enabled: no
            m = p19.match(line)
            if m:
                group = m.groupdict()
                bind_dict['invalidation_drop_enabled'] = group['invalidation_drop_status']
                continue
            
            #  Max Install Standby Candidate Paths: 0
            m = p20.match(line)
            if m:
                group = m.groupdict()
                bind_dict['max_install_standby_candidate_paths'] = int(group['max_install_standby_pats'])
                continue
            
        return ret_dict