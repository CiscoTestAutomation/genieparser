#!/bin/env python
import re

# Genie
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

class ShowSegmentRoutingPrefixSidMapSchema(MetaParser):
    ''' Schema for:
          *  show isis segment-routing prefix-sid-map active-policy
          *  show isis segment-routing prefix-sid-map backup-policy
        '''
    schema = {
        Any() : {
            'name' : str,
            Any() : {
                'status' : bool,
                'entries' : int,
                'algorithm' : {
                    'prefix' : str,
                    'sid_index' : int,
                    'range' : int,
                    Optional('flags'): str,
                },
                Optional('isis_id'): int,
                Optional('process_id') : int,
            },
        }
    }

class ShowSegmentRoutingPrefixSidMap(ShowSegmentRoutingPrefixSidMapSchema):
    ''' Parser for:
          *  show isis segment-routing prefix-sid-map active-policy
          *  show isis segment-routing prefix-sid-map backup-policy
        '''

    cli_command = 'show isis segment-routing prefix-sid-map {status}'

    def cli(self, output= None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        
        ret_dict = {}

        p1 = re.compile(r'RP\/0\/0\/CPU0:router# show '
            '(?P<name>\w+)\s+segment-routing prefix-sid-map '
            '(?P<status>\w+)-policy$')
        
        p2 = re.compile(r'^SRMS \w+ policy for Process ID (?P<process_id>\d+)$')
        
        p3 = re.compile(r'^IS-IS (?P<isis_id>\d+) \w+ policy$')

        p4 = re.compile(r'(?P<prefix>[\w\.\/]+)\s+(?P<sid_index>\d+)'
            '\s+(?P<range>\d+)(\s+(?P<flags>)[\w\s]+$)?')
        
        p5 = re.compile(r'Number of mapping entries:\s+(?P<entries>\d+)')

        for line in out.splitlines():
            line = line.strip()
        
            # RP/0/0/CPU0:router# show isis \
                        # segment-routing prefix-sid-map active-policy
            m = p1.match(line)
            if m:
                status_bool = True if 'active' in \
                        m.groupdict()['status'].lower()\
                    else False
                name = m.groupdict()['name']
                status = m.groupdict()['status']

                router_dict = ret_dict.setdefault(name, {})
                router_dict['name'] = name
                status_dict = router_dict.setdefault(status, {})
                status_dict['status'] = status_bool

            # SRMS active policy for Process ID 1
            m = p2.match(line)
            if m:
                status_dict.setdefault('process_id', \
                    int(m.groupdict()['process_id']))
            
            # IS-IS 1 active policy
            m = p3.match(line)
            if m:
                status_dict.setdefault('isis_id', int(m.groupdict()['isis_id']))


            # Prefix               SID Index    Range        Flags
            # 1.1.1.100/32         100          20          
            # 1.1.1.150/32         150          10          
            m = p4.match(line)
            if m:
                algo_dict = status_dict.setdefault('algorithm', {})
                algo_dict.setdefault('prefix', m.groupdict()['prefix'])
                algo_dict.setdefault('sid_index', \
                                            int(m.groupdict()['sid_index']))
                algo_dict.setdefault('range', int(m.groupdict()['range']))
                if 'flag' in line.lower():
                    algo_dict.setdefault('flags', m.groupdict()['flags'])

            # Number of mapping entries: 2
            m = p5.match(line)
            if m:
                status_dict['entries'] = int(m.groupdict()['entries'])
        
        return ret_dict


class ShowPceIPV4PeerSchema(MetaParser):
    ''' Schema for:
        * show pce ipv4 peer
    '''
    schema = {
        'database' : {
            Any() : {
                'peer_address' : str,
                'state' : bool,
                'capabilities' : {
                    'stateful' : bool,
                    'segment-routing' : bool,
                    'update' : bool
                }
            },
        }
    }

class ShowPceIPV4Peer(ShowPceIPV4PeerSchema):
    ''' Parser for:
        * show pce ipv4 peer
    '''
    cli_command = 'show pce ipv4 peer'

    def cli(self, output = None):
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
                database_dict = ret_dict.setdefault('database', {})
                address_dict = database_dict.setdefault(address, {})
                address_dict['peer_address'] = address

            m = p2.match(line)
            if m:
                state_bool = True if 'up' in \
                    m.groupdict()['state'].lower() else False
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
        'database' : {
            Any() : {
                'peer_address' : str,
                'state' : bool,
                'capabilities' : {
                    'stateful' : bool,
                    'segment-routing' : bool,
                    'update' : bool
                },
                'pcep' : {
                    'pcep_uptime': str,
                    'pcep_local_id': int,
                    'pcep_remote_id': int,              
                },
                'ka' : {
                    'sending_intervals': int,
                    'minimum_acceptable_inteval': int,
                },
                'peer_timeout': int,
                'statistics' : {
                    'rx' : {
                        'keepalive_messages' : int,
                        'request_messages' : int,
                        'reply_messages' : int,
                        'error_messages' : int,
                        'open_messages' : int,
                        'report_messages' : int,
                        'update_messages' : int,
                        'initiate_messages' : int,
                    },
                    'tx' : {
                        'keepalive_messages' : int,
                        'request_messages' : int,
                        'reply_messages' : int,
                        'error_messages' : int,
                        'open_messages' : int,
                        'report_messages' : int,
                        'update_messages' : int,
                        'initiate_messages' : int,
                    },
                }
            }
        }
    }

class ShowPceIPV4PeerDetail(ShowPceIPV4PeerDetailSchema):
    ''' Parser for:
        * show pce ipv4 peer detail
    '''

    cli_command = 'show pce ipv4 peer detail'

    def cli(self,output=None):
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
            
        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                address = m.groupdict()['address']
                database_dict = ret_dict.setdefault('database', {})
                address_dict = database_dict.setdefault(address, {})
                address_dict['peer_address'] = address

            m = p2.match(line)
            if m:
                state_bool = True if 'up' in \
                    m.groupdict()['state'].lower() else False
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
                pcep_dict['pcep_uptime'] = m.groupdict()['pcep_up_time']
            
            m = p5.match(line)
            if m:
                pcep_dict['pcep_local_id'] = int(m.groupdict()['local_id'])
                pcep_dict['pcep_remote_id'] = int(m.groupdict()['remote_id'])

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
        
        return ret_dict


class ShowPceIPV4PeerprefixSchema(MetaParser):
    ''' Schema for:
        * show pce ipv4 prefix
    '''
    schema = {
        'prefix' :{
            Any() : {
                'node' : int,
                'te_router_id': str,
                'host_name': str,
                Any() : {
                    'system_id' : str,
                    'level' : int,
                },
                'advertised_prefixes': str,
            }
        }
    }

class ShowPceIPV4PeerPrefix(ShowPceIPV4PeerprefixSchema):
    ''' Parser for:
        * show pce ipv4 prefix
    '''

    cli_command = 'show pcs ipv4 prefix'
    
    def cli(self, output = None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        p1 = re.compile(r'Node (?P<node_number>\d+)')

        p2 = re.compile(r'^TE router ID: (?P<router_id>[\d\.]+)$')

        p3 = re.compile(r'^Host name: (?P<host_name>\w+)$')

        p4 = re.compile(r'^ISIS system ID: (?P<system_id>[\w\.]+)\s+level-(?P<system_id_level>\d+)$')

        p5 = re.compile(r'^(?P<adv_prefixes>[\w\.]+)$')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                node = int(m.groupdict()['node_number'])
                prefix_dict = ret_dict.setdefault('prefix', {})
                node_dict = prefix_dict.setdefault(node, {})

                node_dict['node'] = node

            m = p2.match(line)
            if m:
                node_dict['te_router_id'] = m.groupdict()['router_id']
            
            m = p3.match(line)
            if m:
                node_dict['host_name'] = m.groupdict()['host_name']
            
            m = p4.match(line)
            if m:
                sys_id = m.groupdict()['system_id']
                sys_dict = node_dict.setdefault(sys_id, {})

                sys_dict['system_id'] = sys_id
                sys_dict['level'] = int(m.groupdict()['system_id_level'])

            m = p5.match(line)
            if m:
                node_dict['advertised_prefixes'] = m.groupdict()['adv_prefixes']

        return ret_dict
