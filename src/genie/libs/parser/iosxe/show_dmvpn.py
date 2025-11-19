"""
    * 'show dmvpn'
    * 'show dmvpn interface {interface}'
"""

# Metaparser
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Optional
from genie.libs.parser.utils.common import Common


# ==============================
# Schema for
#   'show dmvpn'
#   'show dmvpn interface {interface}'
# ==============================
class ShowDmvpnSchema(MetaParser):
    """
    Schema for
        * 'show dmvpn'
        * 'show dmvpn interface {interface}'
    """

    # These are the key-value pairs to add to the parsed dictionary
    schema = {
        'interfaces': {
            Any(): {
                'nhrp_peers': int,
                'type': str,
                'ent': {
                    Any(): {
                        'peers': {
                            Any(): {
                                'tunnel_addr': {
                                    Any(): {
                                        'attrb': {
                                            Any(): {
                                                'state': str,
                                                'time': str,
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
            },
        },
    }


# Python (this imports the Python re module for RegEx)
# ==============================
# Parser for
#   'show dmvpn'
#   'show dmvpn interface {interface}'
# ==============================

# The parser class inherits from the schema class

class ShowDmvpn(ShowDmvpnSchema):
    """
    Parser for
        * 'show dmvpn'
        * 'show dmvpn interface {interface}'
    """

    cli_command = ['show dmvpn interface {interface}', 'show dmvpn']

    # Defines a function to run the cli_command
    def cli(self, interface='', output=None):
        if output is None:
            if interface:
                cmd = self.cli_command[0].format(interface=interface)
            else:
                cmd = self.cli_command[1]
            out = self.device.execute(cmd)
        else:
            out = output

        # Initializes the Python dictionary variable
        parsed_dict = {}

        # Interface: Tunnel84, IPv4 NHRP Details
        p1 = re.compile(r'Interface: +(?P<interfaces>\S+),')

        # Type:Spoke, NHRP Peers:1,
        p2 = re.compile(r'Type:(?P<type>\S+),'
                        r' +NHRP Peers:(?P<nhrp_peers>(\d+)),$')

        # # Ent  Peer NBMA Addr Peer Tunnel Add State  UpDn Tm Attrb
        # ----- --------------- --------------- ----- -------- -----
        #     1 172.29.0.1          172.30.90.1   IKE     3w5d     S
        #     1 172.29.0.2          172.30.90.2    UP    6d12h     S
        #                           172.30.90.25   UP    6d12h     S
        #     2 172.29.134.1       172.30.72.72    UP 00:29:40   DT2
        #                          172.30.72.72    UP 00:29:40   DT1
        p3 = re.compile(r'^((?P<ent>(\d+))'
                        r' +(?P<peers>([a-z0-9\.\:]+|UNKNOWN))'
                        r' +)?(?P<tunnel_addr>[a-z0-9\.\:]+)'
                        r' +(?P<state>[a-zA-Z]+)'
                        r' +(?P<time>(\d+\w)+|never|[0-9\:]+)'
                        r' +(?P<attrb>(\w)+)$')
        # 1 2001:DB8:1201::222
        p3a = re.compile(r'^(?P<ent>(\d+)) +(?P<peers>([a-zA-Z0-9\:\.]+))$')

        # Defines the "for" loop, to pattern match each line of output
        v6_v4 = False
        for line in out.splitlines():
            line = line.strip()

            # Processes the matched line | Interface: Tunnel84, IPv4 NHRP Details
            m = p1.match(line)
            if m:
                group = m.groupdict()
                interface = group['interfaces']
                interface_dict = parsed_dict.setdefault('interfaces', {}).\
                                             setdefault(interface, {})
                continue

            # Processes the matched line | Type:Spoke, NHRP Peers:1,
            m = p2.match(line)

            if m:
                group = m.groupdict()
                interface_dict['type'] = group['type']
                interface_dict['nhrp_peers'] = int(group['nhrp_peers'])
                continue
            
            # 1 2001:DB8:1201::222
            m = p3a.match(line)
            if m:
                group = m.groupdict()
                v6_peer= interface_dict.setdefault('ent', {}).setdefault(int(group['ent']), {}).\
                                                                setdefault('peers', {}).\
                                                                setdefault(group['peers'], {})
                v6_v4 = True
                continue


            #   Ent  Peer NBMA Addr Peer Tunnel Add State  UpDn Tm Attrb
            # ----- --------------- --------------- ----- -------- -----
            #     1 172.29.0.1          172.30.90.1   IKE     3w5d     S
            #     1 172.29.0.2          172.30.90.2    UP    6d12h     S
            #                           172.30.90.25   UP    6d12h     S
            #     2 172.29.134.1       172.30.72.72    UP 00:29:40   DT2
            #                          172.30.72.72    UP 00:29:40   DT1
            m = p3.match(line)
            if m:
                group = m.groupdict()
                # 192.2.1.1    UP 17:56:26     D
                if v6_v4:
                    # This is to handle the v6 over v4 case
                    
                    attrb = group['attrb']
                    tunnel_addr_dict = v6_peer.setdefault('tunnel_addr', {}).\
                                                        setdefault(group['tunnel_addr'], {})
                    attrb_dict = tunnel_addr_dict.setdefault('attrb', {}).\
                                                    setdefault(attrb, {})
                    attrb_dict['time'] = group['time']
                    attrb_dict['state'] = group['state']
                    continue

                # 1 172.29.0.1          172.30.90.1   IKE     3w5d     S
                if group['ent'] and group['peers']:

                    ent = int(group['ent'])
                    peers = group['peers']
                    tunnel_addr = group['tunnel_addr']
                    attrb = group['attrb']

                    interface_dict.setdefault('ent', {}).setdefault(ent, {})
                    tunnel_addr_dict = interface_dict['ent'][ent].setdefault('peers', {}).\
                                                                  setdefault(peers, {}).\
                                                                  setdefault('tunnel_addr', {})

                    attrb_dict = tunnel_addr_dict.setdefault(tunnel_addr, {}).\
                                                    setdefault('attrb', {}).\
                                                    setdefault(attrb, {})

                    attrb_dict['time'] = group['time']
                    attrb_dict['state'] = group['state']

                # 172.30.90.25   UP    6d12h     S
                else:
                    if group['attrb'] != attrb:
                        sub_attrb_dict = tunnel_addr_dict[tunnel_addr]['attrb'].\
                                                        setdefault(group['attrb'], {})
                        sub_attrb_dict['time'] = group['time']
                        sub_attrb_dict['state'] = group['state']
                        continue

                    tmp = {}
                    sub_attrb_dict = tmp.setdefault('attrb', {}).\
                                        setdefault(group['attrb'], {})

                    sub_attrb_dict['time'] = group['time']
                    sub_attrb_dict['state'] = group['state']

                    # append to the recent added dictionary
                    tunnel_addr_dict.update({group['tunnel_addr']: tmp})

                continue

        return parsed_dict


# =================================================
# Schema for 'show dmvpn | count Status: {service}'
# =================================================
class ShowDmvpnCountStatusSchema(MetaParser):
    schema = {
        'count': int
    }
    
# ================================================
# Parser for:
# 'show dmvpn | count Status: {service}'
# ================================================
class ShowDmvpnCountStatus(ShowDmvpnCountStatusSchema):
 
    cli_command = ['show dmvpn | count {service}', 'show dmvpn | count Status: {service}']


    def cli(self, ipv6= False, service='', output=None):
        if output is None:
            output = self.device.execute(self.cli_command[int(ipv6)].format(service=service))
        dict_count = {}

        # Number of lines which match regexp = 2648
        p1 = re.compile(r"^Number of lines which match regexp\s*=\s*(?P<count>[\d]+)$")

        for line in output.splitlines():
            line = line.strip()

            # Number of lines which match regexp = 2648
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                count = int(groups['count'])
                dict_count['count'] = count

        return dict_count

# ==============================
# Schema for
#   'show dmvpn ipv6'
#   'show dmvpn ipv6 interface {interface}'
# ==============================
class ShowDmvpnipv6Schema(MetaParser):
    """
    Schema for
        * 'show dmvpn ipv6'
        * 'show dmvpn ipv6 interface {interface}'
    """

    # These are the key-value pairs to add to the parsed dictionary
    schema = {
        'interfaces': {
            str: {  # Interface name, e.g., 'Tunnel1'
                'type': str,
                'nhrp_peers': int,
                'peers': {
                    str: {  # Peer IPv6 address, e.g., '2001:DB8:1202::222'
                        'tunnel_addr': str,
                        'ipv6_target_network': str,
                        'ent': int,
                        'status': str,
                        'updn_time': str,
                        'cache_attrib': str,
                    }
                }
            }
        }
    }

class ShowDmvpnIpv6(ShowDmvpnipv6Schema):
    """ Parser for 
        * 'show dmvpn ipv6'
        * 'show dmvpn ipv6 interface {interface}'
    """
    cli_command = ['show dmvpn ipv6', 'show dmvpn ipv6 interface {interface}']
    def cli(self, interface='', output=None):
        if output is None:
            if interface:
                output = self.device.execute(self.cli_command[1].format(interface=interface))
            else:
                output = self.device.execute(self.cli_command[0])

        # Initializes the Python dictionary variable
        parsed_dict = {}

        # Interface: Tunnel1, IPv6 NHRP Details
        p1 = re.compile(r'Interface: +(?P<interfaces>\S+),')

        # Type:Hub, Total NBMA Peers (v4/v6): 2
        p2 = re.compile(r'Type:(?P<type>\S+),'
                        r' +Total NBMA Peers .*: (?P<nhrp_peers>(\d+))$')

        # 1.Peer NBMA Address: 2001:DB8:1202::222
        p3 = re.compile(r'^(?P<ent>(\d+))\.Peer NBMA Address\: +(?P<peers>([a-zA-Z0-9\:\.]+))$')
        
        # Tunnel IPv6 Address: FD00:192::1102
        p4 = re.compile(r'Tunnel IPv6 Address: +(?P<tunnel_addr>[a-zA-Z0-9\:\.]+)$')
        
        # IPv6 Target Network: FD00:192::1102/128
        # IPv6 Target Network: FD00:192::1201/128 (ivrf)
        p5 = re.compile(r'IPv6 Target Network: +(?P<target_network>[a-zA-Z0-9\:\.]+/\d+)')
        
        # # Ent: 1, Status: UP, UpDn Time: 01:28:21, Cache Attrib: D
        p6 = re.compile(r'# Ent: +(?P<ent>(\d+)), Status: +(?P<status>\S+), UpDn Time: +(?P<updn_time>\S+), Cache Attrib: +(?P<cache_attrib>\S+)$')

        for line in output.splitlines():
            line = line.strip()
            
            # Interface: Tunnel1, IPv6 NHRP Details
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                interface = groups['interfaces']
                interface_dict = parsed_dict.setdefault('interfaces', {}).\
                                             setdefault(interface, {})
                continue
            # Type:Hub, Total NBMA Peers (v4/v6): 2
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                interface_dict['type'] = groups['type']
                interface_dict['nhrp_peers'] = int(groups['nhrp_peers'])
                continue
            # 1.Peer NBMA Address: 2001:DB8:1202::222
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                ent = groups['ent']
                peers = groups['peers']
                peer_addr_dict = interface_dict.setdefault('peers', {}).\
                                                setdefault(peers, {})
                continue
            # Tunnel IPv6 Address: FD00:192::1102
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                peer_addr_dict['tunnel_addr'] = groups['tunnel_addr']
                continue
            # IPv6 Target Network: FD00:192::1102/128
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                peer_addr_dict['ipv6_target_network'] = groups['target_network']
                continue
            # # Ent: 1, Status: UP, UpDn Time: 01:28:21, Cache Attrib: D
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                peer_addr_dict['ent'] = int(groups['ent'])
                peer_addr_dict['status'] = groups['status']
                peer_addr_dict['updn_time'] = groups['updn_time']
                peer_addr_dict['cache_attrib'] = groups['cache_attrib']
                continue
        return parsed_dict