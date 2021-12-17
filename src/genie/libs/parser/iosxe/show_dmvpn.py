"""
    * 'show dmvpn'
    * 'show dmvpn interface {interface}'
"""

# Metaparser
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Optional


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

        # Defines the "for" loop, to pattern match each line of output

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

