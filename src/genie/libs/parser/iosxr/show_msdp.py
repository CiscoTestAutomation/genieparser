"""show_msdp.py
IOSXR parsers for the following commands
    * 'show msdp peer'
    * 'show msdp peer {peer}'
    * 'show msdp vrf {vrf} peer'
    * 'show msdp vrf {vrf} peer {peer}'
    * 'show msdp context'
    * 'show msdp vrf {vrf} context'
    * 'show msdp summary'
    * 'show msdp vrf {vrf} summary'
    * 'show msdp sa-cache'
    * 'show msdp sa-cache {group}'
    * 'show msdp vrf {vrf} sa-cache'
    * 'show msdp vrf {vrf} sa-cache {group}'
    * 'show msdp statistics peer'
    * 'show msdp statistics peer {peer}'
    * 'show msdp vrf {vrf} statistics peer'
    * 'show msdp vrf {vrf} statistics peer {peer}'
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
                        'peer_name': str,
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
        * 'show msdp peer <peer>'
        * 'show msdp vrf <vrf> peer'
        * 'show msdp vrf <vrf> peer <peer>'
    """

    cli_command = ['show msdp vrf {vrf} peer',
                   'show msdp peer',
                   'show msdp peer {peer}',
                   'show msdp vrf {vrf} peer {peer}']
    exclude = ['elapsed_time', 'tlv_message', 'sa_message']

    def cli(self, vrf='', peer='', output=None):
        if output is None:
            if vrf and not peer:
                cmd = self.cli_command[0].format(vrf=vrf)
            elif peer and not vrf:
                cmd = self.cli_command[2].format(peer=peer)
            elif peer and vrf:
                cmd = self.cli_command[3].format(vrf=vrf, peer=peer)
            else:
                cmd = self.cli_command[1]
            out = self.device.execute(cmd)

        else:
            out = output

        # MSDP Peer 192.168.229.3 (?), AS 65109
        # MSDP Peer 10.1.1.1 (R1.cisco.com), AS 65109
        r1 = re.compile(r'MSDP +Peer +(?P<peer>\S+) \((?P<peer_name>\S+)\), +'
                        r'AS (?P<peer_as>\d+)')

        # Description: R1
        # Description:
        r2 = re.compile(r'Description:(?: +(?P<description>\S+))?$')

        # State: Inactive, Resets: 999, Connection Source: 192.168.100.1
        r3 = re.compile(r'State: +(?P<session_state>\S+),'
                        r' +Resets: +(?P<reset>\d+),'
                        r' +Connection +Source: +(?P<connect_source_address>\S+)')

        # Uptime(Downtime): 00:00:09, SA messages received: 0
        r4 = re.compile(r'Uptime\(Downtime\): +(?P<elapsed_time>\S+), +'
                        r'SA messages received: +(?P<sa_message_in>\d+)')

        # TLV messages sent/received: 3/0
        r5 = re.compile(r'TLV messages +sent\/received: +'
                        r'(?P<tlv_message_sent>\d+)\/'
                        r'(?P<tlv_message_received>\d+)$')

        # Output messages discarded: 0
        r6 = re.compile(r'Output +messages +discarded: +'
                        r'(?P<output_message_discarded>\d+)')

        # Connection and counters cleared 00:01:25 ago
        r7 = re.compile(r'Connection +and +counters +cleared +'
                        r'(?P<conn_count_cleared>\S+)\s+ago$')

        # Input (S,G) filter: none
        # Input RP filter: none
        r8 = re.compile(r'Input +(?P<filter_in>\S+) +'
                        r'filter: +(?P<filter>\S+)$')

        # Output (S,G) filter: none
        # Output RP filter: none
        r9 = re.compile(r'Output +(?P<filter_out>\S+) +filter:'
                        r' +(?P<filter>\S+)$')

        # Input filter: none
        r10 = re.compile(r'Input +filter: +(?P<input_filter>\S+)')

        # Sending SA-Requests to peer: disabled
        r11 = re.compile(r'Sending +SA-Requests +to +peer:'
                         r' +(?P<sa_request_to_peer>\S+)')

        # Password: None
        r12 = re.compile(r'Password: +'
                         r'(?P<password>\S+)')

        # Peer ttl threshold: 2
        r13 = re.compile(r'^Peer +ttl +threshold:'
                         r' +(?P<ttl_threshold>\d+)')

        # Input queue size: 0, Output queue size: 0
        r14 = re.compile(r'^Input +queue +size: +(?P<size_in>\d+),'
                         r' +Output +queue +size: +(?P<size_out>\d+)$')

        # KeepAlive timer period: 30
        r15 = re.compile(r'^KeepAlive +timer +period:'
                         r' +(?P<keepalive_interval>\d+)')

        # Peer Timeout timer period: 75
        r16 = re.compile(r'^Peer +Timeout +timer +period:'
                         r' +(?P<peer_timeout_interval>\d+)')

        # State: StopRead, Oper-Downs: 0
        r17 = re.compile(r'^State: +(?P<state>\S+)'
                         r', +Oper-Downs:'
                         r' +(?P<oper_downs>\d+)')

        # NSR-Uptime(NSR-Downtime): 1d02h
        r18 = re.compile(r'NSR-Uptime\(NSR-Downtime\):'
                         r' +(?P<up_down_time>\S+)')

        parsed_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # MSDP Peer 192.168.229.3 (?), AS 65109
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
                peer_dict['peer_name'] = group_dict['peer_name']

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


class ShowMsdpContextSchema(MetaParser):
    """Schema for:
    * 'show msdp context'
    """
    schema = {
        'vrf': {
            Any(): {
                'context_info': {
                    'vrf_id': str,
                    'table_id': str,
                    'table_count': {
                        'active': int,
                        'total': int,
                    }
                },
                'inheritable_config': {
                    'ttl': int,
                    'maximum_sa': int,
                    'keepalive_period': int,
                    'peer_timeout_period': int,
                    Optional('connect_source'): str,
                    Optional('sa_filter'): {
                        'in': str,
                        'out': str,
                    },
                    Optional('rp_filter'): {
                        'in': str,
                        'out': str,
                    }
                },
                'config': {
                    'originator_address': str,
                    Optional('originator_interface'): str,
                    'default_peer_address': str,
                    'sa_holdtime': int,
                    'allow_encaps_count': int,
                    'maximum_sa': int,
                },
                'sa_cache': {
                    'groups': {
                        'current': int,
                        'high_water_mark': int,
                    },
                    'sources': {
                        'current': int,
                        'high_water_mark': int,
                    },
                    'rps': {
                        'current': int,
                        'high_water_mark': int,
                    },
                    'external_sas': {
                        'current': int,
                        'high_water_mark': int,
                    }
                },
                'mrib_update_counts': {
                    'total_updates': int,
                    'with_no_changes': int,
                    'g_routes': int,
                    'sg_routes': int,
                },
                'mrib_update_drops': {
                    'invalid_group': int,
                    'invalid_group_length': int,
                    'invalid_source': int,
                    'auto_rp_address': int,
                }
            }
        }
    }


class ShowMsdpContext(ShowMsdpContextSchema):
    """ Parser for:
        * 'show msdp context'
        * 'show msdp vrf <vrf> context'
    """

    cli_command = ['show msdp vrf {vrf} context',
                   'show msdp context']

    def cli(self, vrf='', output=None):
        if output is None:
            if vrf:
                cmd = self.cli_command[0].format(vrf=vrf)
            else:
                cmd = self.cli_command[1]
            out = self.device.execute(cmd)
        else:
            out = output

        # VRF ID                     : 0x60000000
        # Table ID                   : 0xe0000000
        # Table Count (Active/Total) : 2/2
        r1 = re.compile(r'^VRF +ID +: +(?P<vrf_id>\S+)')

        r2 = re.compile(r'Table +ID +: +(?P<table_id>\S+)')

        r3 = re.compile(r'Table +Count +\(Active\/Total\) +: +'
                        r'(?P<table_count_active>\d+)\/'
                        r'(?P<table_count_total>\d+)')

        # TTL                 : 2
        # Maximum SAs         : 0
        # Keepalive Period    : 30
        # Peer Timeout Period : 75
        # Connect Source      :
        # SA Filter In        :
        # SA Filter Out       :
        # RP Filter In        :
        # RP Filter Out       :
        r4 = re.compile(r'TTL +: +(?P<ttl>\d+)')

        r5 = re.compile(r'Maximum +SAs +: +(?P<maximum_sa>\d+)')

        r6 = re.compile(r'Keepalive Period +: +(?P<keepalive_period>\d+)')

        r7 = re.compile(r'Peer +Timeout +Period +: +(?P<peer_timeout_period>\d+)')

        r8 = re.compile(r'Connect Source +: +(?:(?P<connect_source>\S+))?')

        r9 = re.compile(r'SA +Filter +In +: +(?:(?P<sa_filter_in>\S+))?')

        r10 = re.compile(r'SA +Filter +Out +: +(?:(?P<sa_filter_out>\S+))?')

        r11 = re.compile(r'RP +Filter +In +: +(?:(?P<rp_filter_in>\S+))?')

        r12 = re.compile(r'RP +Filter +Out +: +(?:(?P<rp_filter_out>\S+))?')

        # Originator Address         : 172.16.76.1
        # Originator Interface Name  : Loopback150
        # Default Peer Address       : 0.0.0.0
        # SA Holdtime                : 150
        # Allow Encaps Count         : 0
        # Context Maximum SAs        : 20000
        r13 = re.compile(r'Originator +Address +: +(?P<originator_address>\S+)')

        r14 = re.compile(r'Originator +Interface +Name +: +(?P<originator_interface>\S+)')

        r15 = re.compile(r'Default +Peer +Address +: +(?P<default_peer_address>\S+)')

        r16 = re.compile(r'SA +Holdtime +: +(?P<sa_holdtime>\d+)')

        r17 = re.compile(r'Allow +Encaps +Count +: +(?P<allow_encaps_count>\d+)')

        r18 = re.compile(r'Context +Maximum +SAs +: +(?P<config_maximum_sa>\d+)')

        # Groups       :          2/2
        # Sources      :         12/12
        # RPs          :          3/0
        # External SAs :          3/3
        r19 = re.compile(r'Groups +: +(?P<groups_current>\d+)\/(?P<groups_high>\d+)')

        r20 = re.compile(r'Sources +: +(?P<sources_current>\d+)\/(?P<sources_high>\d+)')

        r21 = re.compile(r'RPs +: +(?P<rps_current>\d+)\/(?P<rps_high>\d+)')

        r22 = re.compile(r'External +SAs +: +(?P<sas_current>\d+)\/(?P<sas_high>\d+)')

        # Total updates        : 473
        # With no changes      : 0
        # (*,G) routes         : 26
        # (S,G) routes         : 447
        r23 = re.compile(r'Total +updates +: +(?P<total_updates>\d+)')
        r24 = re.compile(r'With +no +changes +: +(?P<with_no_changes>\d+)')
        r25 = re.compile(r'\(\*,G\) +routes +: +(?P<g_routes>\d+)')
        r26 = re.compile(r'\(S,G\) +routes +: +(?P<sg_routes>\d+)')

        # Invalid group        : 0
        # Invalid group length : 0
        # Invalid source       : 0
        # Auto-RP Address      : 2
        r27 = re.compile(r'Invalid +group +: +(?P<invalid_group>\d+)')
        r28 = re.compile(r'Invalid +group +length +: +(?P<invalid_group_length>\d+)')
        r29 = re.compile(r'Invalid +source +: +(?P<invalid_source>\d+)')
        r30 = re.compile(r'Auto\-RP +Address +: +(?P<auto_rp_address>\d+)')

        parsed_dict = {}
        for line in out.splitlines():
            line = line.strip()

            # MSDP context information for default
            #   VRF ID                     : 0x60000000
            result = r1.match(line)
            if result:
                group_dict = result.groupdict()
                if not vrf:
                    vrf = 'default'
                vrf_dict = parsed_dict.setdefault(
                    'vrf', {}).setdefault(vrf, {})
                context_dict = vrf_dict.setdefault('context_info', {})
                context_dict['vrf_id'] = group_dict['vrf_id']
                continue

            #   Table ID                   : 0xe0000000
            result = r2.match(line)
            if result:
                group_dict = result.groupdict()
                context_dict['table_id'] = group_dict['table_id']
                continue

            #   Table Count (Active/Total) : 2/2
            result = r3.match(line)
            if result:
                group_dict = result.groupdict()
                table_dict = context_dict.setdefault('table_count', {})
                table_dict['active'] = int(group_dict['table_count_active'])
                table_dict['total'] = int(group_dict['table_count_total'])
                continue

            # Inheritable Configuration
            #   TTL                 : 2
            result = r4.match(line)
            if result:
                group_dict = result.groupdict()
                inheritable_dict = vrf_dict.setdefault(
                    'inheritable_config', {})
                inheritable_dict['ttl'] = int(group_dict['ttl'])
                continue

            #   Maximum SAs         : 0
            result = r5.match(line)
            if result:
                group_dict = result.groupdict()
                inheritable_dict['maximum_sa'] = int(group_dict['maximum_sa'])
                continue

            #   Keepalive Period    : 30
            result = r6.match(line)
            if result:
                group_dict = result.groupdict()
                inheritable_dict['keepalive_period'] = int(
                    group_dict['keepalive_period'])
                continue

            #   Peer Timeout Period : 75
            result = r7.match(line)
            if result:
                group_dict = result.groupdict()
                inheritable_dict['peer_timeout_period'] = int(
                    group_dict['peer_timeout_period'])
                continue

            #   Connect Source      :
            result = r8.match(line)
            if result:
                group_dict = result.groupdict()
                inheritable_dict['connect_source'] = group_dict['connect_source']
                continue

            #   SA Filter In        :
            result = r9.match(line)
            if result:
                group_dict = result.groupdict()
                sa_filter_dict = inheritable_dict.setdefault('sa_filter', {})
                sa_filter_dict['in'] = group_dict['sa_filter_in']
                continue

            #   SA Filter Out       :
            result = r10.match(line)
            if result:
                group_dict = result.groupdict()
                sa_filter_dict['out'] = group_dict['sa_filter_out']
                continue

            #   RP Filter In        :
            result = r11.match(line)
            if result:
                group_dict = result.groupdict()
                rp_filter_dict = inheritable_dict.setdefault('rp_filter', {})
                rp_filter_dict['in'] = group_dict['rp_filter_in']
                continue

            #   RP Filter Out       :
            result = r12.match(line)
            if result:
                group_dict = result.groupdict()
                rp_filter_dict['out'] = group_dict['rp_filter_out']
                continue

            # Configuration:
            #   Originator Address         : 172.16.76.1
            result = r13.match(line)
            if result:
                group_dict = result.groupdict()
                config_dict = vrf_dict.setdefault('config', {})
                config_dict['originator_address'] = group_dict['originator_address']
                continue

            #   Originator Interface Name  : Loopback150
            result = r14.match(line)
            if result:
                group_dict = result.groupdict()
                config_dict['originator_interface'] = group_dict['originator_interface']
                continue

            #   Default Peer Address       : 0.0.0.0
            result = r15.match(line)
            if result:
                group_dict = result.groupdict()
                config_dict['default_peer_address'] = group_dict['default_peer_address']
                continue

            #   SA Holdtime                : 150
            result = r16.match(line)
            if result:
                group_dict = result.groupdict()
                config_dict['sa_holdtime'] = int(group_dict['sa_holdtime'])
                continue

            #   Allow Encaps Count         : 0
            result = r17.match(line)
            if result:
                group_dict = result.groupdict()
                config_dict['allow_encaps_count'] = int(
                    group_dict['allow_encaps_count'])
                continue

            #   Context Maximum SAs        : 20000
            result = r18.match(line)
            if result:
                group_dict = result.groupdict()
                config_dict['maximum_sa'] = int(
                    group_dict['config_maximum_sa'])
                continue

            # SA Cache Counts  (Current/High Water Mark)
            #   Groups       :          2/2
            result = r19.match(line)
            if result:
                group_dict = result.groupdict()
                sa_cache = vrf_dict.setdefault('sa_cache', {})
                groups_dict = sa_cache.setdefault('groups', {})
                groups_dict['current'] = int(group_dict['groups_current'])
                groups_dict['high_water_mark'] = int(group_dict['groups_high'])
                continue

            #   Sources      :         12/12
            result = r20.match(line)
            if result:
                group_dict = result.groupdict()
                sources_dict = sa_cache.setdefault('sources', {})
                sources_dict['current'] = int(group_dict['sources_current'])
                sources_dict['high_water_mark'] = int(
                    group_dict['sources_high'])
                continue

            #   RPs          :          3/0
            result = r21.match(line)
            if result:
                group_dict = result.groupdict()
                rps_dict = sa_cache.setdefault('rps', {})
                rps_dict['current'] = int(group_dict['rps_current'])
                rps_dict['high_water_mark'] = int(group_dict['rps_high'])
                continue

            #   External SAs :          3/3
            result = r22.match(line)
            if result:
                group_dict = result.groupdict()
                external_dict = sa_cache.setdefault('external_sas', {})
                external_dict['current'] = int(group_dict['sas_current'])
                external_dict['high_water_mark'] = int(group_dict['sas_high'])
                continue

            # MRIB Update Counts
            #   Total updates        : 473
            result = r23.match(line)
            if result:
                group_dict = result.groupdict()
                mrib_counts_dict = vrf_dict.setdefault(
                    'mrib_update_counts', {})
                mrib_counts_dict['total_updates'] = int(
                    group_dict['total_updates'])
                continue

            #   With no changes      : 0
            result = r24.match(line)
            if result:
                group_dict = result.groupdict()
                mrib_counts_dict['with_no_changes'] = int(
                    group_dict['with_no_changes'])
                continue

            #   (*,G) routes         : 26
            result = r25.match(line)
            if result:
                group_dict = result.groupdict()
                mrib_counts_dict['g_routes'] = int(group_dict['g_routes'])
                continue

            #   (S,G) routes         : 447
            result = r26.match(line)
            if result:
                group_dict = result.groupdict()
                mrib_counts_dict['sg_routes'] = int(group_dict['sg_routes'])
                continue

            # MRIB Update Drops
            #   Invalid group        : 0
            result = r27.match(line)
            if result:
                group_dict = result.groupdict()
                mrib_drops_dict = vrf_dict.setdefault('mrib_update_drops', {})
                mrib_drops_dict['invalid_group'] = int(
                    group_dict['invalid_group'])
                continue

            #   Invalid group length : 0
            result = r28.match(line)
            if result:
                group_dict = result.groupdict()
                mrib_drops_dict['invalid_group_length'] = int(
                    group_dict['invalid_group_length'])
                continue

            #   Invalid source       : 0
            result = r29.match(line)
            if result:
                group_dict = result.groupdict()
                mrib_drops_dict['invalid_source'] = int(
                    group_dict['invalid_source'])
                continue

            #   Auto-RP Address      : 2
            result = r30.match(line)
            if result:
                group_dict = result.groupdict()
                mrib_drops_dict['auto_rp_address'] = int(
                    group_dict['auto_rp_address'])
                continue

        return parsed_dict


class ShowMsdpSummarySchema(MetaParser):
    """Schema for:
        * 'show msdp summary'
    """
    schema = {
        'vrf': {
            Any(): {
                'maximum_external_sa_global': int,
                'current_external_active_sa': int,
                Optional('peer_address'): {
                    Any(): {
                        'as': int,
                        'state': str,
                        'uptime_downtime': str,
                        'reset_count': int,
                        'name': str,
                        'active_sa_cnt': int,
                        'cfg_max_ext_sas': int,
                        'tlv': {
                            'receive': int,
                            'sent': int,
                        }
                    }
                }
            }
        }
    }


class ShowMsdpSummary(ShowMsdpSummarySchema):
    """Parser for:
        * 'show msdp summary'
        * 'show msdp vrf <vrf> summary'
    """

    cli_command = ['show msdp vrf {vrf} summary',
                   'show msdp summary']

    def cli(self, vrf='', output=None):
        if output is None:
            if vrf:
                cmd = self.cli_command[0].format(vrf=vrf)
            else:
                cmd = self.cli_command[1]
            out = self.device.execute(cmd)

        else:
            out = output

        # Maximum External SA's Global : 20000
        r1 = re.compile(r'Maximum +External +SA\'s +Global +:'
                        r' +(?P<maximum_external_sa_global>\d+)')

        # Current External Active SAs : 0
        r2 = re.compile(r'Current +External +Active +SAs'
                        r' +: +(?P<current_external_active_sa>\d+)')

        # Peer Address	  AS		   State    Uptime/    Reset Peer    Active Cfg.Max    TLV
        #             Downtime    Count Name    SA Cnt Ext.SAs recv/sent
        # 10.64.4.4    200    Connect    20:35:48    0    R4    0   444    0/0
        # 10.229.11.11    0    Listen    18:14:53    0    ?    0    0   0/0
        r3 = re.compile(r'(?P<address>\S+) +(?P<as>\d+)'
                        r' +(?P<state>\S+) +(?P<uptime_downtime>\S+)'
                        r' +(?P<reset_count>\d+) +(?P<name>\S+)'
                        r' +(?P<active_sa_cnt>\d+) +(?P<cfg_max_ext_sas>\d+)'
                        r' +(?P<receive>\d+)\/(?P<sent>\d+)')

        parsed_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # Maximum External SA's Global : 20000
            result = r1.match(line)
            if result:
                group_dict = result.groupdict()
                if not vrf:
                    vrf = 'default'
                vrf_dict = parsed_dict.setdefault(
                    'vrf', {}).setdefault(vrf, {})
                vrf_dict['maximum_external_sa_global'] = int(
                    group_dict['maximum_external_sa_global'])
                continue

            # Current External Active SAs : 0
            result = r2.match(line)
            if result:
                group_dict = result.groupdict()
                vrf_dict['current_external_active_sa'] = int(
                    group_dict['current_external_active_sa'])
                continue

            # 10.64.4.4    200    Connect    20:35:48    0    R4   0    444    0/0
            result = r3.match(line)
            if result:
                # import pdb
                # pdb.set_trace()
                group_dict = result.groupdict()
                summary_dict = vrf_dict.setdefault('peer_address', {})
                address_dict = summary_dict.setdefault(group_dict['address'], {})
                str_name_list = ['state', 'uptime_downtime', 'name']
                int_name_list = [
                    'as',
                    'reset_count',
                    'active_sa_cnt',
                    'cfg_max_ext_sas']

                for i in str_name_list:
                    address_dict[i] = group_dict[i]
                for i in int_name_list:
                    address_dict[i] = int(group_dict[i])

                tlv_dict = address_dict.setdefault('tlv', {})
                tlv_dict['receive'] = int(group_dict['receive'])
                tlv_dict['sent'] = int(group_dict['sent'])
                continue

        return parsed_dict

class ShowMsdpSaCacheSchema(MetaParser):

    """ Schema for:
        * 'show msdp sa-cache'
        * 'show msdp vrf {vrf} sa-cache {group}'
    """
    schema = {
        'vrf': {
            Any(): {
                'sa_cache': {
                    Any(): {
                        'group': str,
                        'source_addr': str,
                        Optional('peer_as'): int,
                        Optional('peer_learned_from'): str,
                        Optional('rpf_peer'): str,
                        'origin_rp': {
                            Any(): {
                                'rp_address': str,
                             },
                        },
                        'flags': {
                            'grp': list,
                            'src': list,
                        },
                        Optional('statistics'): {
                            'received': {
                                'sa': int,
                                'encapsulated_data_received': int,
                            },
                        },
                        'up_time': str,
                        'expire': str
                    }
                }
            }
        }
    }

class ShowMsdpSaCache(ShowMsdpSaCacheSchema):

    cli_command = ['show msdp vrf {vrf} sa-cache',
                   'show msdp sa-cache',
                   'show msdp sa-cache {group}',
                   'show msdp vrf {vrf} sa-cache {group}']

    def cli(self, vrf='', group='', output=None):
        if output is None:
            if vrf and not group:
                cmd = self.cli_command[0].format(vrf=vrf)
            elif group and not vrf:
                cmd = self.cli_command[2].format(group=group)
            elif vrf and group:
                cmd = self.cli_command[3].format(vrf=vrf, group=group)
            else:
                cmd = self.cli_command[1]
            out = self.device.execute(cmd)
        else:
            out = output

        # (10.1.1.10, 239.1.1.1), RP 192.168.1.1, MBGP/AS 200, 00:01:02/00:01:32
        r1 = re.compile(r'\((?P<source_addr>\S+), +(?P<group>\S+)\),'
                        r' +RP +(?P<rp_address>\S+), +(?:MBGP\/)?'
                        r'AS +(?P<peer_as>\S+), +(?P<up_time>\S+)\/(?P<expire>\S+)')

        #    Learned from peer 192.168.1.1, RPF peer 192.168.1.1
        r2 = re.compile(r'Learned +from +peer +(?P<peer_learned_from>\S+),'
                        r' +RPF +peer +(?P<rpf_peer>\S+)')

        # SAs recvd 2, Encapsulated data received: 0
        r3 = re.compile(r'SAs +recvd +(?P<sa_received>\d+),'
                        r' +Encapsulated\s+data\s+received:'
                        r' +(?P<encapsulated_data_received>\d+)')

        # grp flags: PI,    src flags: E, EA, PI
        r4 = re.compile(r'grp +flags: +(?P<grp_flag>\S+), +src'
                        r' +flags: +(?P<src_flag>[\S\s]+)')

        parsed_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # (10.1.1.10, 239.1.1.1), RP 192.168.1.1, MBGP/AS 200, 00:01:02/00:01:32
            result = r1.match(line)
            if result:
                group_dict = result.groupdict()

                gp_addr = group_dict['group']
                src_addr = group_dict['source_addr']
                rp_address = group_dict['rp_address']
                peer_as = group_dict['peer_as']
                up_time = group_dict['up_time']
                expire = group_dict['expire']

                if not vrf:
                    vrf = 'default'

                sa_cache = '{} {}'.format(gp_addr, src_addr)

                vrf_dict = parsed_dict.setdefault('vrf', {})\
                    .setdefault(vrf, {})

                sa_cache_dict = vrf_dict.setdefault('sa_cache', {})\
                    .setdefault(sa_cache, {})
                sa_cache_dict['group'] = gp_addr
                sa_cache_dict['source_addr'] = src_addr
                sa_cache_dict['up_time'] = up_time
                sa_cache_dict['expire'] = expire

                if not peer_as or peer_as != '?':
                    sa_cache_dict['peer_as'] = int(peer_as)

                sa_cache_dict.setdefault('origin_rp', {})\
                    .setdefault(rp_address, {})\
                    .setdefault('rp_address', rp_address)

                continue

            #  Learned from peer 192.168.1.1, RPF peer 192.168.1.1
            result = r2.match(line)
            if result:
                group_dict = result.groupdict()
                sa_cache_dict['peer_learned_from'] = group_dict['peer_learned_from']
                sa_cache_dict['rpf_peer'] = group_dict['rpf_peer']

                continue

            # SAs recvd 2, Encapsulated data received: 0
            result = r3.match(line)
            if result:
                group_dict = result.groupdict()
                received_dict = sa_cache_dict.setdefault('statistics', {})\
                    .setdefault('received', {})
                received_dict['sa'] = int(group_dict['sa_received'])
                received_dict['encapsulated_data_received'] = \
                    int(group_dict['encapsulated_data_received'])

                continue

            # grp flags: PI,    src flags: E, EA, PI
            result = r4.match(line)
            if result:
                group_dict = result.groupdict()
                flags_dict = sa_cache_dict.setdefault('flags', {})
                flags_dict['grp'] = group_dict['grp_flag'].split(', ')
                flags_dict['src'] = group_dict['src_flag'].split(', ')
        return parsed_dict

class ShowMsdpStatisticsPeerSchema(MetaParser):
    """ Schema for:
        * 'show msdp statistics peer'
        * 'show msdp vrf <vrf> statistics peer'
    """
    schema = {
        'vrf': {
            Any(): {
                'peer': {
                    Any(): {
                        'as': int,
                        'state': str,
                        'active_sa': int,
                        'tlv_rcvd': {
                            'total': int,
                            'keepalives': int,
                            'notifications': int,
                            'sa': int,
                            'request': int,
                            'sa_response': int,
                            'unknowns': int,
                        },
                        'tlv_sent': {
                            'total': int,
                            'keepalives': int,
                            'notifications': int,
                            'sa': int,
                            'request': int,
                            'sa_response': int,
                        },
                        'sa_msgs': {
                            'received': int,
                            'sent': int,
                        }
                    }
                }
            }
        }
    }

class ShowMsdpStatisticsPeer(ShowMsdpStatisticsPeerSchema):

    cli_command = ['show msdp statistics peer',
                   'show msdp vrf {vrf} statistics peer',
                   'show msdp statistics peer {peer}',
                   'show msdp vrf {vrf} statistics peer {peer}']

    def cli(self, vrf='', peer='', output=None):
        if output is None:
            if vrf and not peer:
                cmd = self.cli_command[1].format(vrf=vrf)
            elif peer and not vrf:
                cmd = self.cli_command[2].format(peer=peer)
            elif vrf and peer:
                cmd = self.cli_command[3].format(vrf=vrf, peer=peer)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        # Peer 10.64.4.4 : AS is 200, State is Connect, 0 active SAs
        r1 = re.compile(r'Peer +(?P<peer_address>\d+.+) : '
                        r'+AS +is +(?P<as>\d+), +State +is +(?P<state>\S+), '
                        r'+(?P<active_sa>\d+) +active SAs$')

        #     TLV Rcvd : 0 total
        r2 = re.compile(r'TLV +Rcvd +: +(?P<total>\d+) +total$')

        # 0 keepalives, 0 notifications
        r3 = re.compile(r'(?P<keepalives>\d+) +keepalives, +(?P<notifications>\d+) +notifications$')

        # 0 SAs, 0 SA Requests
        r4 = re.compile(r'(?P<sa>\d+) +SAs, +(?P<request>\d+) +SA Requests$')

        # 0 SA responses, 0 unknowns
        # 0 SA responses
        r5 = re.compile(r'(?P<sa_response>\d+) +SA responses(?:, +(?P<unknowns>\d+) +unknowns$)?')

        # TLV Sent : 0 total
        r6 = re.compile(r'TLV +Sent +: +(?P<total>\d+) +total')

        # SA msgs  : 0 received, 0 sent
        r7 = re.compile(r'SA +msgs +: +(?P<received>\d+) +received, +(?P<sent>\d+) +sent$')

        parsed_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # Peer 10.64.4.4 : AS is 200, State is Connect, 0 active SAs
            m = r1.match(line)
            if m:
                group = m.groupdict()

                if not vrf:
                    vrf = 'default'

                vrf_dict = parsed_dict.setdefault('vrf', {})\
                    .setdefault(vrf, {})
                peer_dict = vrf_dict.setdefault('peer', {})\
                    .setdefault(group['peer_address'], {})

                peer_dict['as'] = int(group['as'])
                peer_dict['state'] = group['state']
                peer_dict['active_sa'] = int(group['active_sa'])

                continue

            #     TLV Rcvd : 0 total
            m = r2.match(line)
            if m:
                if 'tlv_rcvd' not in peer_dict:
                    tlv_rcvd_dict = peer_dict.setdefault('tlv_rcvd', {})
                tlv_rcvd_dict['total'] = int(m.groupdict()['total'])

                continue

            # TLV Sent : 0 total
            m = r6.match(line)
            if m:
                if 'tlv_sent' not in peer_dict:
                    tlv_sent_dict = peer_dict.setdefault('tlv_sent', {})
                tlv_sent_dict['total'] = int(m.groupdict()['total'])

                continue

            # 0 keepalives, 0 notifications
            m = r3.match(line)
            if m:
                if 'tlv_sent' not in peer_dict:
                    tlv_rcvd_dict['keepalives'] = int(m.groupdict()['keepalives'])
                    tlv_rcvd_dict['notifications'] = int(m.groupdict()['notifications'])
                else:
                    tlv_sent_dict['keepalives'] = int(m.groupdict()['keepalives'])
                    tlv_sent_dict['notifications'] = int(m.groupdict()['notifications'])

                continue

            # 0 SAs, 0 SA Requests
            m = r4.match(line)
            if m:
                if 'tlv_sent' not in peer_dict:
                    tlv_rcvd_dict['sa'] = int(m.groupdict()['sa'])
                    tlv_rcvd_dict['request'] = int(m.groupdict()['request'])
                else:
                    tlv_sent_dict['sa'] = int(m.groupdict()['request'])
                    tlv_sent_dict['request'] = int(m.groupdict()['request'])

                continue

            # 0 SA responses, 0 unknowns
            # 0 SA responses
            m = r5.match(line)
            if m:
                if 'tlv_sent' not in peer_dict:
                    tlv_rcvd_dict['sa_response'] = int(m.groupdict()['sa_response'])
                    tlv_rcvd_dict['unknowns'] = int(m.groupdict()['unknowns'])
                else:
                    tlv_sent_dict['sa_response'] = int(m.groupdict()['sa_response'])

                continue

            # SA msgs  : 0 received, 0 sent
            m = r7.match(line)
            if m:
                if 'sa_msgs' not in peer_dict:
                    sa_msg_dict = peer_dict.setdefault('sa_msgs', {})
                sa_msg_dict['received'] = int(m.groupdict()['received'])
                sa_msg_dict['sent'] = int(m.groupdict()['sent'])

        return parsed_dict

