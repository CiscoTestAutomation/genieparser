"""show_cef.py

IOSXE parsers for the following show commands:

    * show adjacency interface detail 
    * show adjacency interface <interface> id <id> detail
    * show adjacency interface <interface> id <id> prefix <prefix> detail
    * show adjacency vlan <id> detail
    * show adjacency vlan <id> prefix <prefix> detail'
    * show adjacency vlan <id> prefix <prefix> link protocol <protocol> detail
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional

# Adjacency_source_dict
adjacency_source_dict = {'AToM', 'link raw adjacency', 'ARP', 'P2P-ADJ', 'FR-MAP'
                         'ATM-PVC', 'ATM-SVC', 'ATM-TVC', 'NBMA', 'MPOA', 'ATM-BUNDLE'
                         'LEC', 'NHRP', 'IPv6 isatap tunnel', 'IPv6 auto tunnel',
                         'ADJSRC_FIBLC', 'Virtual', 'Test', 'Multicast', 'Dialer',
                         'Nailed pending SSO flush', 'IP Session', 'Tun endpt',
                         'Inject p2mp Multicast', 'Inject gre non-ip',
                         'Channel interface processor', 'VMI', 'Casa', 'WANOPT',
                         'general mpls interface', 'GPRS', 'LISP', 'IPv6 6RD tunnel',
                         'NAT64 Translation', 'MPLS Transport Profile tunnel',
                         'VXLAN Transport tunnel', 'IPv6 ND'}

class ShowAdjacencyInterfaceDetailSchema(MetaParser):
    """Schema for:
        show adjacency interface detail 
        show adjacency interface <interface> id <id> detail
        show adjacency interface <interface> id <id> prefix <prefix> detail
    """
    schema = {
        'protocol': str,
        'interface': str,
        'address': str,
        Optional('connectionid'): int,
        'traffic_data': {
            'packets': int,
            'bytes': int,
        },
        'epoch': int,
        'sourced_in_sev_epoch': int,
        'encap_length': int,
        'encap_str': str,
        Optional('L2_destination_address'):{
            'byte_offset': int,
            'byte_length': int
        },
        Optional('adjacency_source'): str,
        Optional('link_type_after_encap'): str,
        Optional('next_chain_elem'): {
            Optional('protocol'): str,
            Optional('outgoing_interface'): str,
            Optional('outgoing_address'): str
        }
    }

class ShowAdjacencyInterfaceDetail(ShowAdjacencyInterfaceDetailSchema):
    """Parser for:
        show adjacency interface detail 
        show adjacency interface <interface> id <id> detail
        show adjacency interface <interface> id <id> prefix <prefix> detail
    """
    cli_command = ['show adjacency detail',
                   'show adjacency {interface} {id} detail',
                   'show adjacency {interface} {id} {prefix} detail']

    def cli(self, id=None, interface=None, prefix=None, output=None):
        if output is None:
            if interface and id and prefix: 
                cmd = self.cli_command[2].format(id=id, interface=interface, prefix=prefix)
            elif interface and id:
                cmd = self.cli_command[1].format(id=id, interface=interface)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        # Protocol Interface Address
        # IPV6 Tunnel0 ABCD:2::2(4)
        p1 = re.compile(r'^(?P<protocol>IP(V6)?)\s+(?P<interface>[\w\/\.\-\:]+?)\s+(?P<address>[\da-fA-F:.()/]+)$')

        # connectionid 1
        p2 = re.compile(r'^connectionid (?P<connectionid>\d+)$')

        # 56 packets, 7494 bytes
        p3 = re.compile(r'^(?P<packets>\d+) packets, (?P<bytes>\d+) bytes$')

        # epoch 0
        p4 = re.compile(r'^epoch (?P<epoch>\d+)$')

        # sourced in sev-epoch 1
        p5 = re.compile(r'^sourced in sev-epoch (?P<sourced_in_sev_epoch>\d+)$')

        # Encap length 48
        p6 = re.compile(r'^Encap length (?P<encap_length>\d+)$')

        # L2 destination address byte offset 0
        p7 = re.compile(r'L2 destination address byte offset (?P<byte_offset>\d+)$')

        # L2 destination address byte length 6
        p8 = re.compile(r'L2 destination address byte length (?P<byte_length>\d+)$')

        # Link-type after encap: ipv6
        p9 = re.compile(r'Link-type after encap: (?P<link_type_after_encap>ip(v6)?)$')

        # Entire encap str is 3 lines, next 3 represent that
        # 60000000000011FFABCD000100000000
        # 0000000000000002ABCD000200000000
        # 000000000000000212B512B500000000
        p10 = re.compile(r'^(?P<encap_str>[\dA-F]+)$')

        # Tun endpt
        p11 = re.compile(r'^.+$')

        # Next chain element:
        # IPV6 adj out of Ethernet1/0, addr FE80::A8BB:CCFF:FE02:5710
        p12 = re.compile(r'^(?P<protocol>IP(V6)?)'
                        r' +adj out of (?P<outgoing_interface>[\w\/\.\-\:]+),'
                        r' +addr (?P<outgoing_address>[\da-fA-F:.()/]+)$')

        ret_dict = {}
        encapstr_len = 0

        for line in out.splitlines():
            if not line:
                continue
            line = line.strip()

            # Protocol Interface Address
            # IPV6 Tunnel 0 ABCD:2::2(4)
            m = p1.match(line)
            if m:
                group = m.groupdict()
                for key, value in group.items():
                    ret_dict.setdefault(key, value)
                continue

            # connectionid 1
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('connectionid', int(group['connectionid']))
                continue

            # 56 packets, 7494 bytes
            m = p3.match(line)
            if m:
                group = m.groupdict()
                pak, num_bytes = group['packets'], group['bytes']
                ret_dict.setdefault('traffic_data', {'packets':int(pak), 'bytes':int(num_bytes)})
                continue

            # epoch 0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('epoch', int(group['epoch']))
                continue

            # sourced in sev-epoch 1
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('sourced_in_sev_epoch', int(group['sourced_in_sev_epoch']))
                continue

            # Encap length 48
            m = p6.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('encap_length', int(group['encap_length']))
                encapstr_len = 2*int(group['encap_length'])
                continue

            # L2 destination address byte offset 0
            m = p7.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('L2_destination_address', {'byte_offset':int(group['byte_offset'])})
                continue

            # L2 destination address byte length 6
            m = p8.match(line)
            if m:
                group = m.groupdict()
                ret_dict['L2_destination_address'].setdefault('byte_length', int(group['byte_length']))
                continue

            # Link-type after encap: ipv6
            m = p9.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('link_type_after_encap', group['link_type_after_encap'])
                continue

            # 60000000000011FFABCD000100000000
            # 0000000000000002ABCD000200000000
            # 000000000000000212B512B500000000
            m = p10.match(line)
            if m and encapstr_len > 0:
                group = m.groupdict()
                if 'encap_str' not in ret_dict:
                    ret_dict.setdefault('encap_str', group['encap_str'])
                else: 
                    ret_dict['encap_str'] += group['encap_str']
                encapstr_len -= len(group['encap_str'])
                continue

            # Next chain element:
            # IPV6 adj out of Ethernet1/0, addr FE80::A8BB:CCFF:FE02:5710
            m = p12.match(line)
            if m:
                group = m.groupdict()
                chain_elem_dict = ret_dict.setdefault('next_chain_elem', {})
                for key, value in group.items():
                    chain_elem_dict.setdefault(key, value)
                continue

            #Tun endpt
            m = p11.match(line)
            if m:
                if m.string in adjacency_source_dict:
                    ret_dict.setdefault('adjacency_source', m.string)
                continue

        return ret_dict

class ShowAdjacencyVlanLinkDetailSchema(MetaParser):
    """Schema for:
        show adjacency vlan <id> detail
        show adjacency vlan <id> prefix <prefix> detail'
        show adjacency vlan <id> prefix <prefix> link protocol <protocol> detail
    """
    schema = {
        'protocol': str,
        'interface': str,
        'address': str,
        'traffic_data': {
            'packets': int,
            'bytes': int
        },
        'epoch': int,
        'sourced_in_sev_epoch': int,
        'encap_length': int,
        'encap_str': str,
        'adjacency_source': str
    }

class ShowAdjacencyVlanLinkDetail(ShowAdjacencyVlanLinkDetailSchema):
    """Parser for:
        show adjacency vlan <id> detail
        show adjacency vlan <id> prefix <prefix> detail'
        show adjacency vlan <id> prefix <prefix> link protocol <protocol> detail
    """
    cli_command = ['show adjacency vlan {id} detail',
                   'show adjacency vlan {id} {prefix} detail',
                   'show adjacency vlan {id} {prefix} link {protocol} detail']

    def cli(self, id=None, prefix=None, protocol=None, output=None):
        if output is None:
            if prefix and protocol:
                cmd = self.cli_command[2].format(id=id, prefix=prefix, protocol=protocol)
            elif prefix:
                cmd = self.cli_command[1].format(id=id, prefix=prefix)
            else:
                cmd = self.cli_command[0].format(id=id)
            out = self.device.execute(cmd)
        else:
            out = output

        # Protocol Interface Address
        # IPV6 Vlan3 ABCD:2::2(7)
        p1 = re.compile(r'^(?P<protocol>IP(V6)?)\s+(?P<interface>.+?)\s+(?P<address>[\da-fA-F:.()/]+)$')

        # 0 packets, 0 bytes
        p2 = re.compile(r'^(?P<packets>\d+) packets, (?P<bytes>\d+) bytes$')

        # epoch 0
        p3 = re.compile(r'^epoch (?P<epoch>\d+)$')

        # sourced in sev-epoch 4
        p4 = re.compile(r'^sourced in sev-epoch (?P<sourced_in_sev_epoch>\d+)$')

        # Encap length 14
        p5 = re.compile(r'^Encap length (?P<encap_length>\d+)$')

        # AABBCC81F600AABBCC81F50086DD
        p6 = re.compile(r'^(?P<encap_str>[\dA-F]+)$')

        # VXLAN Transport Tunnel
        p7 = re.compile(r'^.+$')

        ret_dict = {}
        encapstr_len = 0

        for line in out.splitlines():
            if not line: continue
            line = line.strip()

            # Protocol Interface Address
            # IPV6 Vlan3 ABCD:2::2(7)
            m = p1.match(line)
            if m:
                group = m.groupdict()
                for key, value in group.items():
                    ret_dict.setdefault(key, value)
                continue

            # 56 packets, 7494 bytes
            m = p2.match(line)
            if m:
                group = m.groupdict()
                pak, num_bytes = group['packets'], group['bytes']
                ret_dict.setdefault('traffic_data', {'packets':int(pak), 'bytes':int(num_bytes)})
                continue

            # epoch 0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('epoch', int(group['epoch']))
                continue

            # sourced in sev-epoch 4
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('sourced_in_sev_epoch', int(group['sourced_in_sev_epoch']))
                continue

            #Encap length 14
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('encap_length', int(group['encap_length']))
                encapstr_len = 2*int(group['encap_length'])
                continue

            # AABBCC81F600AABBCC81F50086DD
            m = p6.match(line)
            if m and encapstr_len > 0:
                group = m.groupdict()
                if 'encap_str' not in ret_dict:
                    ret_dict.setdefault('encap_str', group['encap_str'])
                else: 
                    ret_dict['encap_str'] += group['encap_str']
                encapstr_len -= len(group['encap_str'])
                continue

            # VXLAN Transport Tunnel
            m = p7.match(line)
            if m:
                if m.string in adjacency_source_dict:
                    ret_dict.setdefault('adjacency_source', m.string)
                continue

        return ret_dict
