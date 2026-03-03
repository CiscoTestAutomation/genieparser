"""show_cef.py

IOSXE parsers for the following show commands:

    * show adjacency interface detail 
    * show adjacency interface <interface> id <id> detail
    * show adjacency interface <interface> id <id> prefix <prefix> detail
    * show adjacency vlan <id> detail
    * show adjacency vlan <id> prefix <prefix> detail'
    * show adjacency vlan <id> prefix <prefix> link protocol <protocol> detail
    * show adjacency tunnel {tunnel} internal
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional, ListOf

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


class ShowAdjacencyTunnelTunnelInternalSchema(MetaParser):
    """Schema for:
        show adjacency tunnel {tunnel} internal
    """
    schema = {
        "interface": {
            Any(): {
                "protocol": str,
                "interface": str,
                "address": str,
                "adjacency_id": int,
                "packets": int,
                "bytes": int,
                "epoch": int,
                "sourced_in_sev_epoch": int,
                "encap_length": int,
                "encap": ListOf(str),
                "adjacency_type": str,
                "next_chain_element": {
                    "protocol": str,
                    "out_interface": str,
                    "addr": str,
                    "pointer": str,
                    "parent_oce": str,
                    "frame_origin": str
                },
                "l3_mtu": int,
                "mtu_update_suppressed": bool,
                "flags": str,
                "fixup": {
                    "enabled": bool,
                    "value": str,
                    "note": str
                },
                "hwidb_pointer": str,
                "idb_pointer": str,
                "ip_redirect_disabled": bool,
                "switching_vector": str,
                "next_hop_inferred": bool,
                "ip_tunnel_stack": {
                    "to": str,
                    "vrf": str,
                    "vrf_id": str
                },
                "nh_tracking": {
                    "enabled": bool,
                    "prefix": str,
                    "adjacency": {
                        "protocol": str,
                        "out_interface": str,
                        "addr": str
                    }
                },
                "platform": {
                    "adj_id": str,
                    "adj_id2": str,
                    "tun_qos_dpidx": int
                },
                "adjacency_pointer": str,
                "next_hop": str
            }
        }
    }

class ShowAdjacencyTunnelTunnelInternal(ShowAdjacencyTunnelTunnelInternalSchema):
    """Parser for:
        show adjacency tunnel {tunnel} internal
    """
    cli_command = "show adjacency tunnel {tunnel} internal"

    def cli(self, tunnel=None, output=None):
        if output is None:
            cmd = self.cli_command.format(tunnel=tunnel)
            out = self.device.execute(cmd)
        else:
            out = output

        ret_dict = {}
        

        tunnel_key = "{tunnel}" if tunnel is None else tunnel
        intf_dict = ret_dict.setdefault("interface", {}).setdefault(f"Tunnel{tunnel_key}", {})

        # IP       Tunnel1                   point2point(19)
        p1 = re.compile(r'^(?P<protocol>IP(V6)?)\s+(?P<interface>\S+)\s+(?P<address>[^()]+)\((?P<adjacency_id>\d+)\)$')

        #  1998 packets, 1581880 bytes
        p2 = re.compile(r'^\s*(?P<packets>\d+)\s+packets,\s+(?P<bytes>\d+)\s+bytes$')

        #  epoch 0
        p3 = re.compile(r'^\s*epoch\s+(?P<epoch>\d+)$')

        # sourced in sev-epoch 1110
        p4 = re.compile(r'^\s*sourced\s+in\s+sev-epoch\s+(?P<sourced_in_sev_epoch>\d+)$')

        # Encap length 40
        p5 = re.compile(r'^\s*Encap\s+length\s+(?P<encap_length>\d+)$')

        # 60000000000004FF0100010000010000
        p6 = re.compile(r'^\s*(?P<hex>[0-9A-F]+)\s*$')

        # P2P-ADJ
        p7 = re.compile(r'^\s*P2P-ADJ$')

        # Next chain element:
        p8 = re.compile(r'^\s*Next\s+chain\s+element:$')

        # IPV6 adj out of GigabitEthernet0/0/1, addr FE80::C6B2:39FF:FEFB:DC41 78EE054686C8
        p9 = re.compile(r'^\s*(?P<protocol>IP(V6)?)\s+adj\s+out\s+of\s+(?P<out_interface>\S+),\s+addr\s+(?P<addr>\S+)\s+(?P<pointer>[0-9A-F]+)$')

        # parent oce 0x78EE05468788
        p10 = re.compile(r'^\s*parent\s+oce\s+(?P<parent_oce>\S+)$')

        # frame originated locally (Null0)
        p11 = re.compile(r'^\s*(?P<frame_origin>frame\s+originated\s+locally\s+\(\S+\))$')

        # L3 mtu 1460
        p12 = re.compile(r'^\s*L3\s+mtu\s+(?P<l3_mtu>\d+)$')

        # mtu update from interface suppressed
        p13 = re.compile(r'^\s*mtu\s+update\s+from\s+interface\s+suppressed$')

        # Flags (0x4928E4)
        p14 = re.compile(r'^\s*Flags\s*\(\s*(?P<flags>0x[0-9A-Fa-f]+)\s*\)$')

        # Fixup enabled (0x80000)
        p15 = re.compile(r'^\s*Fixup\s+enabled\s*\(\s*(?P<val>0x[0-9A-Fa-f]+)\s*\)$')

        # IPv6 in IPv6 tunnel
        p16 = re.compile(r'^\s*(?P<note>IPv6\s+in\s+IPv6\s+tunnel)$')

        # HWIDB/IDB pointers 0x78EDFF532770/0x78EE0541C910
        p17 = re.compile(r'^\s*HWIDB/IDB\s+pointers\s+(?P<hwidb>0x[0-9A-Fa-f]+)\s*/\s*(?P<idb>0x[0-9A-Fa-f]+)$')

        # IP redirect disabled
        p18 = re.compile(r'^\s*IP\s+redirect\s+disabled$')

        # Switching vector: IPv4 midchain adj oce
        p19 = re.compile(r'^\s*Switching\s+vector\s*:\s*(?P<sv>.*)$')

        # Next-hop cannot be inferred
        p20 = re.compile(r'^\s*Next-hop\s+cannot\s+be\s+inferred$')

        # IP Tunnel stack to 300:300:1::1 in Default (0x0)
        p21 = re.compile(r'^\s*IP\s+Tunnel\s+stack\s+to\s+(?P<to>\S+)\s+in\s+(?P<vrf>\S+)\s*\(\s*(?P<vrf_id>0x[0-9A-Fa-f]+)\s*\)$')

        # nh tracking enabled: 300:300:1::1/128
        p22 = re.compile(r'^\s*nh\s+tracking\s+enabled\s*:\s*(?P<prefix>\S+)$')

        # IPV6 adj out of GigabitEthernet0/0/1, addr FE80::C6B2:39FF:FEFB:DC41
        p23 = re.compile(r'^\s*(?P<protocol>IP(V6)?)\s+adj\s+out\s+of\s+(?P<out_interface>\S+),\s+addr\s+(?P<addr>\S+)$')

        # Platform adj-id: 0xF8000216, 0x0, tun_qos_dpidx:0
        p24 = re.compile(r'^\s*Platform\s+adj-id\s*:\s*(?P<adj_id>0x[0-9A-Fa-f]+)\s*,\s*(?P<adj_id2>0x[0-9A-Fa-f]+)\s*,\s*tun_qos_dpidx\s*:\s*(?P<dpidx>\d+)$')

        # Adjacency pointer 0x78EE05468F88
        p25 = re.compile(r'^\s*Adjacency\s+pointer\s+(?P<adj_ptr>0x[0-9A-Fa-f]+)$')

        # Next-hop unknown
        p26 = re.compile(r'^\s*Next-hop\s+(?P<nh>unknown)$')

        encap_remaining = 0

        for line in out.splitlines():
            if not line:
                continue
            line = line.strip()

            # IP       Tunnel1                   point2point(19)
            m = p1.match(line)
            if m:
                gd = m.groupdict()
                intf_dict.setdefault("protocol", gd["protocol"])
                intf_dict.setdefault("interface", gd["interface"])
                intf_dict.setdefault("address", gd["address"].strip())
                intf_dict.setdefault("adjacency_id", int(gd["adjacency_id"]))
                continue

            # 1998 packets, 1581880 bytes
            m = p2.match(line)
            if m:
                gd = m.groupdict()
                intf_dict.setdefault("packets", int(gd["packets"]))
                intf_dict.setdefault("bytes", int(gd["bytes"]))
                continue

            # epoch 0
            m = p3.match(line)
            if m:
                intf_dict.setdefault("epoch", int(m.group("epoch")))
                continue

            # sourced in sev-epoch 1110
            m = p4.match(line)
            if m:
                intf_dict.setdefault("sourced_in_sev_epoch", int(m.group("sourced_in_sev_epoch")))
                continue

            # Encap length 40
            m = p5.match(line)
            if m:
                enc_len = int(m.group("encap_length"))
                intf_dict.setdefault("encap_length", enc_len)
                encap_remaining = 2 * enc_len
                intf_dict.setdefault("encap", [])
                continue

            # 60000000000004FF0100010000010000
            m = p6.match(line)
            if m and encap_remaining > 0:
                hexstr = m.group("hex")
                intf_dict["encap"].append(hexstr)
                encap_remaining -= len(hexstr)
                continue

            # P2P-ADJ
            m = p7.match(line)
            if m:
                intf_dict.setdefault("adjacency_type", "P2P-ADJ")
                continue

            # Next chain element:
            m = p8.match(line)
            if m:
                # header seen; actual data parsed by following lines
                continue

            # IPV6 adj out of GigabitEthernet0/0/1, addr FE80::C6B2:39FF:FEFB:DC41 78EE054686C8
            m = p9.match(line)
            if m:
                gd = m.groupdict()
                nce = intf_dict.setdefault("next_chain_element", {})
                nce.setdefault("protocol", gd["protocol"])
                nce.setdefault("out_interface", gd["out_interface"])
                nce.setdefault("addr", gd["addr"])
                nce.setdefault("pointer", gd["pointer"])
                continue

            # parent oce 0x78EE05468788
            m = p10.match(line)
            if m:
                nce = intf_dict.setdefault("next_chain_element", {})
                nce.setdefault("parent_oce", m.group("parent_oce"))
                continue

            # frame originated locally (Null0)
            m = p11.match(line)
            if m:
                nce = intf_dict.setdefault("next_chain_element", {})
                nce.setdefault("frame_origin", m.group("frame_origin"))
                continue

            # L3 mtu 1460
            m = p12.match(line)
            if m:
                intf_dict.setdefault("l3_mtu", int(m.group("l3_mtu")))
                continue

            # mtu update from interface suppressed
            m = p13.match(line)
            if m:
                intf_dict.setdefault("mtu_update_suppressed", True)
                continue

            # Flags (0x4928E4)
            m = p14.match(line)
            if m:
                intf_dict.setdefault("flags", m.group("flags"))
                continue

            # Fixup enabled (0x80000)
            m = p15.match(line)
            if m:
                fix = intf_dict.setdefault("fixup", {})
                fix.setdefault("enabled", True)
                fix.setdefault("value", m.group("val"))
                continue

            # IPv6 in IPv6 tunnel
            m = p16.match(line)
            if m:
                fix = intf_dict.setdefault("fixup", {})
                fix.setdefault("note", m.group("note"))
                continue

            # HWIDB/IDB pointers 0x78EDFF532770/0x78EE0541C910
            m = p17.match(line)
            if m:
                gd = m.groupdict()
                intf_dict.setdefault("hwidb_pointer", gd["hwidb"])
                intf_dict.setdefault("idb_pointer", gd["idb"])
                continue

            # IP redirect disabled
            m = p18.match(line)
            if m:
                intf_dict.setdefault("ip_redirect_disabled", True)
                continue

            # Switching vector: IPv4 midchain adj oce
            m = p19.match(line)
            if m:
                intf_dict.setdefault("switching_vector", m.group("sv"))
                continue

            # Next-hop cannot be inferred
            m = p20.match(line)
            if m:
                intf_dict.setdefault("next_hop_inferred", False)
                continue

            # IP Tunnel stack to 300:300:1::1 in Default (0x0)
            m = p21.match(line)
            if m:
                gd = m.groupdict()
                its = intf_dict.setdefault("ip_tunnel_stack", {})
                its.setdefault("to", gd["to"])
                its.setdefault("vrf", gd["vrf"])
                its.setdefault("vrf_id", gd["vrf_id"])
                continue

            # nh tracking enabled: 300:300:1::1/128
            m = p22.match(line)
            if m:
                nht = intf_dict.setdefault("nh_tracking", {})
                nht.setdefault("enabled", True)
                nht.setdefault("prefix", m.group("prefix"))
                continue

            # IPV6 adj out of GigabitEthernet0/0/1, addr FE80::C6B2:39FF:FEFB:DC41
            m = p23.match(line)
            if m:
                gd = m.groupdict()
                nht = intf_dict.setdefault("nh_tracking", {})
                adj = nht.setdefault("adjacency", {})
                adj.setdefault("protocol", gd["protocol"])
                adj.setdefault("out_interface", gd["out_interface"])
                adj.setdefault("addr", gd["addr"])
                continue

            # Platform adj-id: 0xF8000216, 0x0, tun_qos_dpidx:0
            m = p24.match(line)
            if m:
                gd = m.groupdict()
                plat = intf_dict.setdefault("platform", {})
                plat.setdefault("adj_id", gd["adj_id"])
                plat.setdefault("adj_id2", gd["adj_id2"])
                plat.setdefault("tun_qos_dpidx", int(gd["dpidx"]))
                continue

            # Adjacency pointer 0x78EE05468F88
            m = p25.match(line)
            if m:
                intf_dict.setdefault("adjacency_pointer", m.group("adj_ptr"))
                continue

            # Next-hop unknown
            m = p26.match(line)
            if m:
                intf_dict.setdefault("next_hop", m.group("nh"))
                continue

        return ret_dict
