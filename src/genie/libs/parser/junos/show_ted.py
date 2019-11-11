"""show_ted.py

JunOS parsers for the following show commands:
    - 'show ted database extensive'
    - 'show ted database extensive {node_id}'
"""

# python
import re

# metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional


class ShowTedDatabaseExtensiveSchema(MetaParser):
    """ Schema for:
            - 'show ted database extensive'
            - 'show ted database extensive {node_id}'
    """

    schema = {
        'isis_nodes': int,
        'inet_nodes': int,
        'node': {
            Any(): {  # '172.16.1.1'
                'type': str,
                'age': int,
                'link_in': int,
                'link_out': int,
                Optional('protocol'): {
                    Any(): {  # 'ospf(0.0.0.1)'
                        'to': {
                            Any(): {  # '172.16.1.1'
                                'local': {
                                    Any(): {  # '172.16.1.1'
                                        'remote': {
                                            Any(): {  # '172.16.1.1'
                                                'local_interface_index': int,
                                                'remote_interface_index': int,
                                                Optional('color'): str,
                                                'metric': int,
                                                Optional('static_bw'): str,
                                                Optional('reservable_bw'): str,
                                                Optional('available_bw'): {
                                                    Any(): {  # priority
                                                        'bw': str
                                                    }
                                                },
                                                'interface_switching_capability_descriptor': {
                                                    Any(): {  # from Interface Switching Capability Descriptor(1):
                                                        'switching_type': str,
                                                        'encoding_type': str,
                                                        'maximum_lsp_bw': {
                                                            Any(): {  # 1, 2, 3, ...
                                                                'bw': str
                                                            }
                                                        }
                                                    }
                                                },
                                                Optional('p2p_adj_sid'): {
                                                    'sid': {
                                                        Any(): {
                                                            'address_family': str,
                                                            'flags': str,
                                                            'weight': int
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        Optional('prefixes'): {
                            Any(): {  # prefix
                                'flags': str,
                                'prefix_sid': {
                                    Any(): {  # sid
                                        'flags': str,
                                        'algo': int
                                    }
                                }
                            }
                        },
                        Optional('spring_capabilities'): {
                            'srgb_block': {
                                'start': int,
                                'range': int,
                                'flags': str
                            }
                        },
                        Optional('spring_algorithms'): list
                    }
                }
            }
        }
    }


class ShowTedDatabaseExtensive(ShowTedDatabaseExtensiveSchema):
    """ Parser for:
            - 'show ted database extensive'
            - 'show ted database extensive {node_id}'
    """

    cli_command = [
        'show ted database extensive',
        'show ted database extensive {node_id}'
    ]

    def cli(self, node_id=None, output=None):
        if output is None:
            if node_id:
                cmd = self.cli_command[1].format(node_id=node_id)
            else:
                cmd = self.cli_command[0]

            out = self.device.execute(cmd)
        else:
            out = output

        # init vars
        ret_dict = {}

        # TED database: 0 ISIS nodes 0 INET nodes
        p1 = re.compile(r'^TED +database: +(?P<isis_nodes>\d+) +ISIS +nodes +(?P<inet_nodes>\d+) +INET +nodes$')

        # NodeID: 172.16.1.1
        p2 = re.compile(r'^NodeID: +(?P<node_id>\S+)$')

        # Type: Rtr, Age: 1000 secs, LinkIn: 0, LinkOut: 0
        p3 = re.compile(r'^Type: +(?P<type>[\w-]+), +Age: +(?P<age>\d+) +secs, +LinkIn: '
                        r'+(?P<link_in>\d+), +LinkOut: +(?P<link_out>\d+)$')

        # Protocol: OSPF(0.0.0.1)
        p4 = re.compile(r'^Protocol: +(?P<protocol>[\w().]+)$')

        # To: 172.16.1.1, Local: 10.16.0.1, Remote: 10.16.0.2
        p5 = re.compile(r'^To: +(?P<to>\S+), +Local: +(?P<local>\S+), +Remote: +(?P<remote>\S+)$')

        # Local interface index: 0, Remote interface index: 0
        p6 = re.compile(r'^Local +interface +index: +(?P<local_interface_index>\d+), +'
                        r'Remote +interface +index: +(?P<remote_interface_index>\d+)$')

        # Color: 0 blue
        p7 = re.compile(r'^Color: +(?P<color>[\w<> ]+)$')

        # Metric: 0
        p8 = re.compile(r'^Metric: +(?P<metric>\d+)$')

        # Static BW: 100Mbps
        p9 = re.compile(r'^Static +BW: +(?P<static_bw>\w+)$')

        # Reservable BW: 100bps
        p10 = re.compile(r'^Reservable +BW: +(?P<reservable_bw>\w+)$')

        # [0] 0bps
        # [0] 0bps         [1] 0bps
        # [0] 0bps         [1] 0bps        [2] 0bps
        # [0] 0bps         [1] 0bps        [2] 0bps        [3] 0bps
        p11 = re.compile(r'\[(?P<priority>\d+)\] +(?P<bw>\w+)')

        # Interface Switching Capability Descriptor(1):
        p12 = re.compile(r'^Interface +Switching +Capability +Descriptor\((?P<descriptor>[\w ]+)\):$')

        # Switching type: Packet
        p13 = re.compile(r'^Switching +type: +(?P<switching_type>\w+)$')

        # Encoding type: Packet
        p14 = re.compile(r'^Encoding +type: +(?P<encoding_type>\w+)$')

        # IPV4, SID: 12345, Flags: 0x00, Weight: 0
        p15 = re.compile(r'^(?P<address_family>\w+), +SID: +(?P<sid>\d+), +Flags: +'
                         r'(?P<flags>\w+), +Weight: +(?P<weight>\d+)$')

        # 172.16.1.1/32
        p16 = re.compile(r'^(?P<prefix>\S+/\d+)$')

        # Flags: 0x60
        p17 = re.compile(r'^Flags: +(?P<flags>\w+)$')

        # SID: 1234, Flags: 0x00, Algo: 0
        p18 = re.compile(r'^SID: +(?P<sid>\d+), +Flags: +(?P<flags>\w+), +Algo: +(?P<algo>\d+)$')

        # SRGB block [Start: 12345, Range: 1234, Flags: 0x00]
        p19 = re.compile(r'^SRGB +block +\[Start: +(?P<start>\d+), +Range: +'
                         r'(?P<range>\d+), +Flags: +(?P<flags>\w+)\]$')

        # Algo: 0
        p20 = re.compile(r'^Algo: +(?P<algo>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({k: int(v) for k, v in group.items()})
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                node_dict = ret_dict.setdefault('node', {}).setdefault(group['node_id'], {})
                continue

            m = p3.match(line)
            if m:
                group = m.groupdict()
                node_dict.update({'type': group['type']})
                node_dict.update({'age': int(group['age'])})
                node_dict.update({'link_in': int(group['link_in'])})
                node_dict.update({'link_out': int(group['link_out'])})
                continue

            m = p4.match(line)
            if m:
                group = m.groupdict()
                protocol_dict = node_dict.setdefault('protocol', {}).setdefault(group['protocol'], {})
                continue

            m = p5.match(line)
            if m:
                group = m.groupdict()
                remote_dict = (protocol_dict.setdefault('to', {}).setdefault(group['to'], {})
                               .setdefault('local', {}).setdefault(group['local'], {})
                               .setdefault('remote', {}).setdefault(group['remote'], {}))
                continue

            m = p6.match(line)
            if m:
                group = m.groupdict()
                remote_dict.update({k: int(v) for k, v in group.items()})
                continue

            m = p7.match(line)
            if m:
                group = m.groupdict()
                remote_dict.update({'color': group['color']})
                continue

            m = p8.match(line)
            if m:
                group = m.groupdict()
                remote_dict.update({'metric': int(group['metric'])})
                continue

            m = p9.match(line)
            if m:
                group = m.groupdict()
                remote_dict.update({'static_bw': group['static_bw']})
                continue

            m = p10.match(line)
            if m:
                group = m.groupdict()
                remote_dict.update({'reservable_bw': group['reservable_bw']})
                continue

            m = p11.findall(line)
            if m:
                if 'interface_switching_capability_descriptor' in remote_dict:
                    for k, v in m:
                        (descriptor_dict.setdefault('maximum_lsp_bw', {})
                         .setdefault(int(k), {})
                         .update({'bw': v}))
                else:
                    for k, v in m:
                        (remote_dict.setdefault('available_bw', {})
                         .setdefault(int(k), {})
                         .update({'bw': v}))
                continue

            m = p12.match(line)
            if m:
                group = m.groupdict()
                descriptor_dict = (remote_dict.setdefault('interface_switching_capability_descriptor', {})
                                   .setdefault(group['descriptor'], {}))
                continue

            m = p13.match(line)
            if m:
                group = m.groupdict()
                descriptor_dict.update({'switching_type': group['switching_type']})
                continue

            m = p14.match(line)
            if m:
                group = m.groupdict()
                descriptor_dict.update({'encoding_type': group['encoding_type']})
                continue

            m = p15.match(line)
            if m:
                group = m.groupdict()
                p2p_adj_sid_dict = (remote_dict.setdefault('p2p_adj_sid', {})
                                    .setdefault('sid', {})
                                    .setdefault(group['sid'], {}))
                p2p_adj_sid_dict.update({'address_family': group['address_family']})
                p2p_adj_sid_dict.update({'flags': group['flags']})
                p2p_adj_sid_dict.update({'weight': int(group['weight'])})
                continue

            m = p16.match(line)
            if m:
                group = m.groupdict()
                prefix_dict = (protocol_dict.setdefault('prefixes', {})
                               .setdefault(group['prefix'], {}))
                continue

            m = p17.match(line)
            if m:
                group = m.groupdict()
                prefix_dict.update({'flags': group['flags']})
                continue

            m = p18.match(line)
            if m:
                group = m.groupdict()
                prefix_sid_dict = (prefix_dict.setdefault('prefix_sid', {})
                                   .setdefault(int(group['sid']), {}))
                prefix_sid_dict.update({'flags': group['flags']})
                prefix_sid_dict.update({'algo': int(group['algo'])})
                continue

            m = p19.match(line)
            if m:
                group = m.groupdict()
                srgb_block_dict = (protocol_dict.setdefault('spring_capabilities', {})
                                   .setdefault('srgb_block', {}))
                srgb_block_dict.update({'start': int(group['start'])})
                srgb_block_dict.update({'range': int(group['range'])})
                srgb_block_dict.update({'flags': group['flags']})
                continue

            m = p20.match(line)
            if m:
                group = m.groupdict()
                current_algorithms = protocol_dict.get('spring_algorithms', [])
                current_algorithms.append(group['algo'])
                protocol_dict.update({'spring_algorithms': current_algorithms})

        return ret_dict

