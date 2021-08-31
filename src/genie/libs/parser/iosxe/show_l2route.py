''' show_l2route.py

IOS parsers for the following show commands:

    * show l2route evpn mac ip detail
    * show l2route evpn mac ip host-ip <ip> detail
    * show l2route evpn mac ip host-ip <ip> esi <esi> detail
    * show l2route evpn mac ip host-ip <ip> mac-address <mac_addr> detail
    * show l2route evpn mac ip host-ip <ip> mac-address <mac_addr> esi <esi> detail
    * show l2route evpn mac ip host-ip <ip> next-hop <next_hop> detail
    * show l2route evpn mac ip host-ip <ip> next-hop <next_hop> esi <esi> detail
    * show l2route evpn mac ip host-ip <ip> next-hop <next_hop> mac-address <mac_addr> detail
    * show l2route evpn mac ip host-ip <ip> next-hop <next_hop> mac-address <mac_addr> esi <esi> detail
    * show l2route evpn mac ip host-ip <ip> producer <producer> mac-address <mac_addr> detail
    * show l2route evpn mac ip host-ip <ip> producer <producer> mac-address <mac_addr> esi <esi> detail
    * show l2route evpn mac ip host-ip <ip> topology <evi> detail
    * show l2route evpn mac ip host-ip <ip> topology <evi> esi <esi> detail
    * show l2route evpn mac ip host-ip <ip> topology <evi> mac-address <mac_addr> detail
    * show l2route evpn mac ip host-ip <ip> topology <evi> mac-address <mac_addr> esi <esi> detail
    * show l2route evpn mac ip host-ip <ip> topology <evi> next-hop <next_hop> detail
    * show l2route evpn mac ip host-ip <ip> topology <evi> next-hop <next_hop> esi <esi> detail
    * show l2route evpn mac ip host-ip <ip> topology <evi> next-hop <next_hop> mac-address <mac_addr> detail
    * show l2route evpn mac ip host-ip <ip> topology <evi> next-hop <next_hop> mac-address <mac_addr> esi <esi> detail
    * show l2route evpn mac ip host-ip <ip> topology <evi> producer <producer> mac-address <mac_addr> detail
    * show l2route evpn mac ip host-ip <ip> topology <evi> producer <producer> mac-address <mac_addr> esi <esi> detail
    * show l2route evpn mac ip host-ip <ip> topology <evi>:<etag> detail
    * show l2route evpn mac ip host-ip <ip> topology <evi>:<etag> esi <esi> detail
    * show l2route evpn mac ip host-ip <ip> topology <evi>:<etag> mac-address <mac_addr> detail
    * show l2route evpn mac ip host-ip <ip> topology <evi>:<etag> mac-address <mac_addr> esi <esi> detail
    * show l2route evpn mac ip host-ip <ip> topology <evi>:<etag> next-hop <next_hop> detail
    * show l2route evpn mac ip host-ip <ip> topology <evi>:<etag> next-hop <next_hop> esi <esi> detail
    * show l2route evpn mac ip host-ip <ip> topology <evi>:<etag> next-hop <next_hop> mac-address <mac_addr> detail
    * show l2route evpn mac ip host-ip <ip> topology <evi>:<etag> next-hop <next_hop> mac-address <mac_addr> esi <esi> detail
    * show l2route evpn mac ip host-ip <ip> topology <evi>:<etag> producer <producer> mac-address <mac_addr> detail
    * show l2route evpn mac ip host-ip <ip> topology <evi>:<etag> producer <producer> mac-address <mac_addr> esi <esi> detail
    * show l2route evpn imet detail
    * show l2route evpn imet origin-rtr <origin-ip> detail
    * show l2route evpn imet producer <prod> detail
    * show l2route evpn imet producer <prod> origin-rtr <origin-ip> detail
    * show l2route evpn imet topology <evi>:<etag> detail
    * show l2route evpn imet topology <evi>:<etag> producer <prod> detail
    * show l2route evpn imet topology <evi>:<etag> origin-rtr <origin-ip> detail
    * show l2route evpn imet topology <evi>:<etag> producer <prod> origin-rtr <origin-ip> detail
    * show l2route evpn imet topology <evi> detail
    * show l2route evpn imet topology <evi> producer <prod> detail
    * show l2route evpn imet topology <evi> origin-rtr <origin-ip> detail
    * show l2route evpn imet topology <evi> producer <prod> origin-rtr <origin-ip> detail
    * show l2route evpn mac ip
    * show l2route evpn mac ip esi <esi>
    * show l2route evpn mac ip mac-address <macaddr>
    * show l2route evpn mac ip mac-address <macaddr> esi <esi>
    * show l2route evpn mac ip next-hop <next-hop>
    * show l2route evpn mac ip next-hop <next-hop> mac-address <macaddr>
    * show l2route evpn mac ip next-hop <next-hop> mac-address <macaddr> esi <esi>
    * show l2route evpn mac ip producer <prod>
    * show l2route evpn mac ip producer <prod> next-hop <next-hop>
    * show l2route evpn mac ip producer <prod> next-hop <next-hop> mac-address <macaddr>
    * show l2route evpn mac ip producer <prod> next-hop <next-hop> mac-address <macaddr> esi <esi>
    * show l2route evpn mac ip topology <evi:etag>
    * show l2route evpn mac ip topology <evi:etag> producer <prod>
    * show l2route evpn mac ip topology <evi:etag> producer <prod> next-hop <next-hop>
    * show l2route evpn mac ip topology <evi:etag> producer <prod> next-hop <next-hop> mac-address <macaddr>
    * show l2route evpn mac ip topology <evi:etag> producer <prod> next-hop <next-hop> mac-address <macaddr> esi <esi>
    * show l2route evpn mac ip topology <evi>
    * show l2route evpn mac ip topology <evi> producer <prod>
    * show l2route evpn mac ip topology <evi> producer <prod> next-hop <next-hop>
    * show l2route evpn mac ip topology <evi> producer <prod> next-hop <next-hop> mac-address <macaddr>
    * show l2route evpn mac ip topology <evi> producer <prod> next-hop <next-hop> mac-address <macaddr> esi <esi>

Copyright (c) 2021 by Cisco Systems, Inc.
All rights reserved.

'''
import re

# genie
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, ListOf


# =============================================
# Schema for 'show l2route evpn mac ip detail'
# =============================================
class ShowL2routeEvpnMacIpDetailSchema(MetaParser):
    """ Schema for show l2route evpn mac ip detail
                   show l2route evpn mac ip host-ip <ip> detail
                   show l2route evpn mac ip host-ip <ip> esi <esi> detail
                   show l2route evpn mac ip host-ip <ip> mac-address <mac_addr> detail
                   show l2route evpn mac ip host-ip <ip> mac-address <mac_addr> esi <esi> detail
                   show l2route evpn mac ip host-ip <ip> next-hop <next_hop> detail
                   show l2route evpn mac ip host-ip <ip> next-hop <next_hop> esi <esi> detail
                   show l2route evpn mac ip host-ip <ip> next-hop <next_hop> mac-address <mac_addr> detail
                   show l2route evpn mac ip host-ip <ip> next-hop <next_hop> mac-address <mac_addr> esi <esi> detail
                   show l2route evpn mac ip host-ip <ip> producer <producer> mac-address <mac_addr> detail
                   show l2route evpn mac ip host-ip <ip> producer <producer> mac-address <mac_addr> esi <esi> detail
                   show l2route evpn mac ip host-ip <ip> topology <evi> detail
                   show l2route evpn mac ip host-ip <ip> topology <evi> esi <esi> detail
                   show l2route evpn mac ip host-ip <ip> topology <evi> mac-address <mac_addr> detail
                   show l2route evpn mac ip host-ip <ip> topology <evi> mac-address <mac_addr> esi <esi> detail
                   show l2route evpn mac ip host-ip <ip> topology <evi> next-hop <next_hop> detail
                   show l2route evpn mac ip host-ip <ip> topology <evi> next-hop <next_hop> esi <esi> detail
                   show l2route evpn mac ip host-ip <ip> topology <evi> next-hop <next_hop> mac-address <mac_addr> detail
                   show l2route evpn mac ip host-ip <ip> topology <evi> next-hop <next_hop> mac-address <mac_addr> esi <esi> detail
                   show l2route evpn mac ip host-ip <ip> topology <evi> producer <producer> mac-address <mac_addr> detail
                   show l2route evpn mac ip host-ip <ip> topology <evi> producer <producer> mac-address <mac_addr> esi <esi> detail
                   show l2route evpn mac ip host-ip <ip> topology <evi>:<etag> detail
                   show l2route evpn mac ip host-ip <ip> topology <evi>:<etag> esi <esi> detail
                   show l2route evpn mac ip host-ip <ip> topology <evi>:<etag> mac-address <mac_addr> detail
                   show l2route evpn mac ip host-ip <ip> topology <evi>:<etag> mac-address <mac_addr> esi <esi> detail
                   show l2route evpn mac ip host-ip <ip> topology <evi>:<etag> next-hop <next_hop> detail
                   show l2route evpn mac ip host-ip <ip> topology <evi>:<etag> next-hop <next_hop> esi <esi> detail
                   show l2route evpn mac ip host-ip <ip> topology <evi>:<etag> next-hop <next_hop> mac-address <mac_addr> detail
                   show l2route evpn mac ip host-ip <ip> topology <evi>:<etag> next-hop <next_hop> mac-address <mac_addr> esi <esi> detail
                   show l2route evpn mac ip host-ip <ip> topology <evi>:<etag> producer <producer> mac-address <mac_addr> detail
                   show l2route evpn mac ip host-ip <ip> topology <evi>:<etag> producer <producer> mac-address <mac_addr> esi <esi> detail
    """

    schema = {
        'evi': {
            Any(): {
                'producer': {
                    Any(): {
                        'host_ips': {
                            Any(): {
                                'eth_tag': int,
                                'mac_addr': str,
                                'seq_number': int,
                                'label_2': int,
                                'esi': str,
                                'mac_rt_flags': str,
                                'next_hops': ListOf(
                                    {
                                      'next_hop': str
                                    }
                                )
                            }
                        }
                    }
                }
            }
        }
    }


# =============================================
# Parser for 'show l2route evpn mac ip detail''
# =============================================
class ShowL2routeEvpnMacIpDetail(ShowL2routeEvpnMacIpDetailSchema):
    """ Parser for show l2route evpn mac ip detail
                   show l2route evpn mac ip host-ip <ip> detail
                   show l2route evpn mac ip host-ip <ip> esi <esi> detail
                   show l2route evpn mac ip host-ip <ip> mac-address <mac_addr> detail
                   show l2route evpn mac ip host-ip <ip> mac-address <mac_addr> esi <esi> detail
                   show l2route evpn mac ip host-ip <ip> next-hop <next_hop> detail
                   show l2route evpn mac ip host-ip <ip> next-hop <next_hop> esi <esi> detail
                   show l2route evpn mac ip host-ip <ip> next-hop <next_hop> mac-address <mac_addr> detail
                   show l2route evpn mac ip host-ip <ip> next-hop <next_hop> mac-address <mac_addr> esi <esi> detail
                   show l2route evpn mac ip host-ip <ip> producer <producer> mac-address <mac_addr> detail
                   show l2route evpn mac ip host-ip <ip> producer <producer> mac-address <mac_addr> esi <esi> detail
                   show l2route evpn mac ip host-ip <ip> topology <evi> detail
                   show l2route evpn mac ip host-ip <ip> topology <evi> esi <esi> detail
                   show l2route evpn mac ip host-ip <ip> topology <evi> mac-address <mac_addr> detail
                   show l2route evpn mac ip host-ip <ip> topology <evi> mac-address <mac_addr> esi <esi> detail
                   show l2route evpn mac ip host-ip <ip> topology <evi> next-hop <next_hop> detail
                   show l2route evpn mac ip host-ip <ip> topology <evi> next-hop <next_hop> esi <esi> detail
                   show l2route evpn mac ip host-ip <ip> topology <evi> next-hop <next_hop> mac-address <mac_addr> detail
                   show l2route evpn mac ip host-ip <ip> topology <evi> next-hop <next_hop> mac-address <mac_addr> esi <esi> detail
                   show l2route evpn mac ip host-ip <ip> topology <evi> producer <producer> mac-address <mac_addr> detail
                   show l2route evpn mac ip host-ip <ip> topology <evi> producer <producer> mac-address <mac_addr> esi <esi> detail
                   show l2route evpn mac ip host-ip <ip> topology <evi>:<etag> detail
                   show l2route evpn mac ip host-ip <ip> topology <evi>:<etag> esi <esi> detail
                   show l2route evpn mac ip host-ip <ip> topology <evi>:<etag> mac-address <mac_addr> detail
                   show l2route evpn mac ip host-ip <ip> topology <evi>:<etag> mac-address <mac_addr> esi <esi> detail
                   show l2route evpn mac ip host-ip <ip> topology <evi>:<etag> next-hop <next_hop> detail
                   show l2route evpn mac ip host-ip <ip> topology <evi>:<etag> next-hop <next_hop> esi <esi> detail
                   show l2route evpn mac ip host-ip <ip> topology <evi>:<etag> next-hop <next_hop> mac-address <mac_addr> detail
                   show l2route evpn mac ip host-ip <ip> topology <evi>:<etag> next-hop <next_hop> mac-address <mac_addr> esi <esi> detail
                   show l2route evpn mac ip host-ip <ip> topology <evi>:<etag> producer <producer> mac-address <mac_addr> detail
                   show l2route evpn mac ip host-ip <ip> topology <evi>:<etag> producer <producer> mac-address <mac_addr> esi <esi> detail
    """

    cli_command = [
                   'show l2route evpn mac ip detail',
                   'show l2route evpn mac ip host-ip {ip} detail',
                   'show l2route evpn mac ip host-ip {ip} esi {esi} detail',
                   'show l2route evpn mac ip host-ip {ip} mac-address {mac_addr} detail',
                   'show l2route evpn mac ip host-ip {ip} mac-address {mac_addr} esi {esi} detail',
                   'show l2route evpn mac ip host-ip {ip} next-hop {next_hop} detail',
                   'show l2route evpn mac ip host-ip {ip} next-hop {next_hop} esi {esi} detail',
                   'show l2route evpn mac ip host-ip {ip} next-hop {next_hop} mac-address {mac_addr} detail',
                   'show l2route evpn mac ip host-ip {ip} next-hop {next_hop} mac-address {mac_addr} esi {esi} detail',
                   'show l2route evpn mac ip host-ip {ip} producer {producer} mac-address {mac_addr} detail',
                   'show l2route evpn mac ip host-ip {ip} producer {producer} mac-address {mac_addr} esi {esi} detail',
                   'show l2route evpn mac ip host-ip {ip} topology {evi} detail',
                   'show l2route evpn mac ip host-ip {ip} topology {evi} esi {esi} detail',
                   'show l2route evpn mac ip host-ip {ip} topology {evi} mac-address {mac_addr} detail',
                   'show l2route evpn mac ip host-ip {ip} topology {evi} mac-address {mac_addr} esi {esi} detail',
                   'show l2route evpn mac ip host-ip {ip} topology {evi} next-hop {next_hop} detail',
                   'show l2route evpn mac ip host-ip {ip} topology {evi} next-hop {next_hop} esi {esi} detail',
                   'show l2route evpn mac ip host-ip {ip} topology {evi} next-hop {next_hop} mac-address {mac_addr} detail',
                   'show l2route evpn mac ip host-ip {ip} topology {evi} next-hop {next_hop} mac-address {mac_addr} esi {esi} detail',
                   'show l2route evpn mac ip host-ip {ip} topology {evi} producer {producer} mac-address {mac_addr} detail',
                   'show l2route evpn mac ip host-ip {ip} topology {evi} producer {producer} mac-address {mac_addr} esi {esi} detail',
                   'show l2route evpn mac ip host-ip {ip} topology {evi_etag} detail',
                   'show l2route evpn mac ip host-ip {ip} topology {evi_etag} esi {esi} detail',
                   'show l2route evpn mac ip host-ip {ip} topology {evi_etag} mac-address {mac_addr} detail',
                   'show l2route evpn mac ip host-ip {ip} topology {evi_etag} mac-address {mac_addr} esi {esi} detail',
                   'show l2route evpn mac ip host-ip {ip} topology {evi_etag} next-hop {next_hop} detail',
                   'show l2route evpn mac ip host-ip {ip} topology {evi_etag} next-hop {next_hop} esi {esi} detail',
                   'show l2route evpn mac ip host-ip {ip} topology {evi_etag} next-hop {next_hop} mac-address {mac_addr} detail',
                   'show l2route evpn mac ip host-ip {ip} topology {evi_etag} next-hop {next_hop} mac-address {mac_addr} esi {esi} detail',
                   'show l2route evpn mac ip host-ip {ip} topology {evi_etag} producer {producer} mac-address {mac_addr} detail',
                   'show l2route evpn mac ip host-ip {ip} topology {evi_etag} producer {producer} mac-address {mac_addr} esi {esi} detail',
    ]

    def cli(self, output=None, ip=None, esi=None, mac_addr=None, next_hop=None, producer=None, evi=None, etag=None):
        if not output:
            cli_cmd = 'show l2route evpn mac ip'
            if ip:
                cli_cmd += ' host-ip {ip}'.format(ip=ip)
            if evi:
                if etag:
                    evi_etag = "{}:{}".format(evi,etag)
                    cli_cmd += ' topology {evi_etag}'.format(evi_etag=evi_etag)
                else:
                    cli_cmd += ' topology {evi}'.format(evi=evi)
            if producer:
                cli_cmd += ' producer {producer}'.format(producer=producer)
            if next_hop:
                cli_cmd += ' next-hop {next_hop}'.format(next_hop=next_hop)
            if mac_addr:
                cli_cmd += ' mac-address {mac_addr}'.format(mac_addr=mac_addr)
            if esi:
                cli_cmd += ' esi {esi}'.format(esi=esi)
            cli_cmd += ' detail'

            cli_output = self.device.execute(cli_cmd)
        else:
            cli_output = output

        # EVPN Instance:            2
        p1 = re.compile(r'^EVPN Instance:\s+(?P<evi>\d+)$')

        # Ethernet Tag:             0
        p2 = re.compile(r'^Ethernet Tag:\s+(?P<eth_tag>\d+)$')

        # Producer Name:            BGP
        p3 = re.compile(r'^Producer Name:\s+(?P<producer>\w+)$')

        # MAC Address:              0012.0012.0012
        p4 = re.compile(r'^MAC Address:\s+(?P<mac_addr>[0-9a-fA-F\.]+)$')

        # Host IP:                  192.168.12.254
        p5 = re.compile(r'^Host IP:\s+(?P<host_ip>[0-9a-fA-F\.:]+)$')

        # Sequence Number:          0
        p6 = re.compile(r'^Sequence Number:\s+(?P<seq_number>\d+)$')

        # Label 2:                  0
        p7 = re.compile(r'^Label 2:\s+(?P<label_2>\d+)$')

        # ESI:                      0000.0000.0000.0000.0000
        p8 = re.compile(r'^ESI:\s+(?P<esi>[0-9a-fA-F\.]+)$')

        # MAC Route Flags:          BInt(Brm)Dgr
        p9 = re.compile(r'^MAC Route Flags:\s+(?P<mac_rt_flags>[\w()]+)$')

        # Next Hop(s):              L:16 2.2.2.1
        p10 = re.compile(r'^[Next Hop\(s\):]*\s*(?P<next_hop>[\w\d\s.:()/]+)$')

        parser_dict = {}

        for line in cli_output.splitlines():
            line = line.strip()
            if not line:
                continue

            # EVPN Instance:            2
            m = p1.match(line)
            if m:
                group = m.groupdict()
                evi = int(group['evi'])
                evi_list = parser_dict.setdefault('evi', {})
                evis = evi_list.setdefault(evi, {})
                continue

            # Ethernet Tag:             0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                eth_tag = int(group['eth_tag'])
                continue

            # Producer Name:            BGP
            m = p3.match(line)
            if m:
                group = m.groupdict()
                producer_list = evis.setdefault('producer', {})
                producers = producer_list.setdefault(group['producer'], {})
                continue

            # MAC Address:              0012.0012.0012
            m = p4.match(line)
            if m:
                group = m.groupdict()
                mac_addr = group['mac_addr']
                continue

            # Host IP:                  192.168.12.254
            m = p5.match(line)
            if m:
                group = m.groupdict()
                host_ips = producers.setdefault('host_ips', {})
                routes = host_ips.setdefault(group['host_ip'], {})
                next_hops = routes.setdefault('next_hops', [])
                routes.update({'eth_tag': eth_tag})
                routes.update({'mac_addr': mac_addr})
                continue

            # Sequence Number:          0
            m = p6.match(line)
            if m:
                group = m.groupdict()
                routes.update({'seq_number': int(group['seq_number'])})
                continue

            # Label 2:                  0
            m = p7.match(line)
            if m:
                group = m.groupdict()
                routes.update({'label_2': int(group['label_2'])})
                continue

            # ESI:                      0000.0000.0000.0000.0000
            m = p8.match(line)
            if m:
                group = m.groupdict()
                routes.update({'esi': group['esi']})
                continue

            # MAC Route Flags:          BInt(Brm)Dgr
            m = p9.match(line)
            if m:
                group = m.groupdict()
                routes.update({'mac_rt_flags': group['mac_rt_flags']})
                continue

            # Next Hop(s):              L:16 2.2.2.1
            m = p10.match(line)
            if m:
                group = m.groupdict()
                next_hops_dict= {}
                next_hops_dict.update({'next_hop': group['next_hop']})
                next_hops.append(next_hops_dict)
                continue

        return parser_dict

# =============================================
# Schema for 'show l2route evpn imet detail'
# =============================================
class ShowL2routeEvpnImetDetailSchema(MetaParser):
    """ Schema for show l2route evpn imet detail
                   show l2route evpn imet origin-rtr <origin-ip> detail
                   show l2route evpn imet producer <prod> detail
                   show l2route evpn imet producer <prod> origin-rtr <origin-ip> detail
                   show l2route evpn imet topology <evi>:<etag> detail
                   show l2route evpn imet topology <evi>:<etag> producer <prod> detail
                   show l2route evpn imet topology <evi>:<etag> origin-rtr <origin-ip> detail
                   show l2route evpn imet topology <evi>:<etag> producer <prod> origin-rtr <origin-ip> detail
                   show l2route evpn imet topology <evi> detail
                   show l2route evpn imet topology <evi> producer <prod> detail
                   show l2route evpn imet topology <evi> origin-rtr <origin-ip> detail
                   show l2route evpn imet topology <evi> producer <prod> origin-rtr <origin-ip> detail

    """

    schema = {
        'evi': {
            Any(): {
                'producer': {
                    Any(): {
                        'origin_router_ip': {
                            Any(): {
                                'eth_tag': int,
                                'router_eth_tag': int,
                                'tunnel_id': {
                                    Any(): {
                                        'tunnel_flags': int,
                                        'tunnel_type': str,
                                        'tunnel_labels': int,
                                    }
                                },
                                'multi_proxy': str,
                                'next_hops':ListOf(
                                    {
                                        'next_hop': str
                                    }
                                )
                            }
                        }
                    }
                }
            }
        }
    }

# =============================================
# Parser for 'show l2route evpn imet detail'
# =============================================
class ShowL2routeEvpnImetDetail(ShowL2routeEvpnImetDetailSchema):
    """ Parser for show l2route evpn imet detail
                   show l2route evpn imet origin-rtr <origin-ip> detail
                   show l2route evpn imet producer <prod> detail
                   show l2route evpn imet producer <prod> origin-rtr <origin-ip> detail
                   show l2route evpn imet topology <evi>:<etag> detail
                   show l2route evpn imet topology <evi>:<etag> producer <prod> detail
                   show l2route evpn imet topology <evi>:<etag> origin-rtr <origin-ip> detail
                   show l2route evpn imet topology <evi>:<etag> producer <prod> origin-rtr <origin-ip> detail
                   show l2route evpn imet topology <evi> detail
                   show l2route evpn imet topology <evi> producer <prod> detail
                   show l2route evpn imet topology <evi> origin-rtr <origin-ip> detail
                   show l2route evpn imet topology <evi> producer <prod> origin-rtr <origin-ip> detail

    """

    cli_command = [
        'show l2route evpn imet detail',
        'show l2route evpn imet origin-rtr {origin_ip} detail',
        'show l2route evpn imet producer {prod} detail',
        'show l2route evpn imet producer {prod} origin-rtr {origin_ip} detail',
        'show l2route evpn imet topology {evi_etag} detail',
        'show l2route evpn imet topology {evi_etag} producer {prod} detail',
        'show l2route evpn imet topology {evi_etag} origin-rtr {origin_ip} detail',
        'show l2route evpn imet topology {evi_etag} producer {prod} origin-rtr {origin_ip} detail',
        'show l2route evpn imet topology {evi} detail',
        'show l2route evpn imet topology {evi} producer {prod} detail',
        'show l2route evpn imet topology {evi} origin-rtr {origin_ip} detail',
        'show l2route evpn imet topology {evi} producer {prod} origin-rtr {origin_ip} detail'
    ]

    def cli(self, output=None, origin_ip=None, prod=None, evi=None, etag=None):
        if not output:
            cli_command = 'show l2route evpn imet'
            if evi:
                if etag:
                    evi_etag = "{}:{}".format(evi,etag)
                    cli_command += ' topology {evi_etag}'.format(evi_etag=evi_etag)
                else:
                    cli_command += ' topology {evi}'.format(evi=evi)
            if prod:
                cli_command += ' producer {prod}'.format(prod=prod)
            if origin_ip:
                cli_command += ' origin-rtr {origin_ip}'.format(origin_ip=origin_ip)
            cli_command += ' detail'

            cli_output = self.device.execute(cli_command)
        else:
            cli_output = output

        # start regex statement complies

        #EVPN Instance:            1
        p1 = re.compile(r'^EVPN Instance:\s+(?P<evi>\d+)$')

        #Ethernet Tag:             0
        p2 = re.compile(r'^Ethernet Tag:\s+(?P<eth_tag>\d+)$')

        #Producer Name:            BGP
        p3 = re.compile(r'^Producer Name:\s+(?P<producer>\w+)$')

        #Router IP Addr:           3.3.3.2
        p4 = re.compile(r'^Router IP Addr:\s+(?P<origin_ip>[0-9a-fA-F\.:]+)$')

        #Route Ethernet Tag:       0
        p5 = re.compile(r'^Route Ethernet Tag:\s+(?P<r_eth_tag>\d+)$')

        #Tunnel Flags:             0
        p6 = re.compile(r'^Tunnel Flags:\s+(?P<tun_flag>\d+)$')

        #Tunnel Type:              Ingress Replication
        p7 = re.compile(r'^Tunnel Type:\s+(?P<tun_type>.*)$')

        #Tunnel Labels:            20011
        p8 = re.compile(r'^Tunnel Labels:\s+(?P<tun_labels>\d+)$')

        #Tunnel ID:                3.3.3.2
        p9 = re.compile(r'^Tunnel ID:\s+(?P<tun_id>[0-9a-fA-F\.:]+)$')

        #Multicast Proxy:          IGMP
        p10 = re.compile(r'^Multicast Proxy:\s+(?P<multi_proxy>\w+)$')

        #Next Hop(s):              V:20011 3.3.3.2
        #Next Hop(s):              N/A
        p11 = re.compile(r'^[Next Hop\(s\):]+\s+(?P<next_hop>[\w\d\s.:()/]+)$')

        parser_dict = {}

        for line in cli_output.splitlines():
            line = line.strip()
            if not line:
                continue

            #EVPN Instance
            m = p1.match(line)
            if m:
                group = m.groupdict()
                evi = int(group['evi'])
                evi_list = parser_dict.setdefault('evi',{})
                evis = evi_list.setdefault(evi,{})
                continue

            #Ethernet Tag
            m = p2.match(line)
            if m:
                group = m.groupdict()
                eth_tag = int(group['eth_tag'])
                continue

            #Producer Name
            m = p3.match(line)
            if m:
                group = m.groupdict()
                producer_list = evis.setdefault('producer', {})
                producers = producer_list.setdefault(group['producer'], {})
                continue

            #Router IP Addr
            m = p4.match(line)
            if m:
                group = m.groupdict()
                router_ips = producers.setdefault('origin_router_ip', {})
                origins_rtr_ip = router_ips.setdefault(group['origin_ip'], {})
                next_hops = origins_rtr_ip.setdefault('next_hops', [])
                origins_rtr_ip.update({'eth_tag': eth_tag})
                continue

            #Route Ethernet Tag:
            m = p5.match(line)
            if m:
                group = m.groupdict()
                origins_rtr_ip.update({'router_eth_tag': int(group['r_eth_tag'] ) } )
                continue

            #Tunnel Flags:
            m = p6.match(line)
            if m:
                group = m.groupdict()
                tun_flag = int(group['tun_flag'])
                continue

            #Tunnel Type:
            m = p7.match(line)
            if m:
                group = m.groupdict()
                tun_type = str(group['tun_type'])
                continue

            #Tunnel Labels:
            m = p8.match(line)
            if m:
                group = m.groupdict()
                tun_labels = int(group['tun_labels'])
                continue

            #Tunnel ID:
            m = p9.match(line)
            if m:
                group = m.groupdict()
                tun_id = group['tun_id']
                tunnel_info = origins_rtr_ip.setdefault('tunnel_id', {})
                tunnel_id = tunnel_info.setdefault(tun_id, {})
                tunnel_id.update({'tunnel_flags': tun_flag})
                tunnel_id.update({'tunnel_type': tun_type})
                tunnel_id.update({'tunnel_labels': tun_labels})
                continue

            #Multicast Proxy:
            m = p10.match(line)
            if m:
                group = m.groupdict()
                origins_rtr_ip.update({'multi_proxy': str(group['multi_proxy'])})
                continue

            #Next Hop(s):
            m = p11.match(line)
            if m:
                group = m.groupdict()
                next_hops_dict = {}
                next_hops_dict.update({'next_hop': group['next_hop']})
                next_hops.append(next_hops_dict)
                continue
        return (parser_dict)

# =============================================
# Schema for 'show l2route evpn mac ip'
# =============================================
class ShowL2routeEvpnMacIpSchema(MetaParser):
    """ Schema for show l2route evpn mac ip
                   show l2route evpn mac ip esi <esi>
                   show l2route evpn mac ip mac-address <macaddr>
                   show l2route evpn mac ip mac-address <macaddr> esi <esi>
                   show l2route evpn mac ip next-hop <next-hop>
                   show l2route evpn mac ip next-hop <next-hop> mac-address <macaddr>
                   show l2route evpn mac ip next-hop <next-hop> mac-address <macaddr> esi <esi>
                   show l2route evpn mac ip producer <prod>
                   show l2route evpn mac ip producer <prod> next-hop <next-hop>
                   show l2route evpn mac ip producer <prod> next-hop <next-hop> mac-address <macaddr>
                   show l2route evpn mac ip producer <prod> next-hop <next-hop> mac-address <macaddr> esi <esi>
                   show l2route evpn mac ip topology <evi:etag>
                   show l2route evpn mac ip topology <evi:etag> producer <prod>
                   show l2route evpn mac ip topology <evi:etag> producer <prod> next-hop <next-hop>
                   show l2route evpn mac ip topology <evi:etag> producer <prod> next-hop <next-hop> mac-address <macaddr>
                   show l2route evpn mac ip topology <evi:etag> producer <prod> next-hop <next-hop> mac-address <macaddr> esi <esi>
                   show l2route evpn mac ip topology <evi>
                   show l2route evpn mac ip topology <evi> producer <prod>
                   show l2route evpn mac ip topology <evi> producer <prod> next-hop <next-hop>
                   show l2route evpn mac ip topology <evi> producer <prod> next-hop <next-hop> mac-address <macaddr>
                   show l2route evpn mac ip topology <evi> producer <prod> next-hop <next-hop> mac-address <macaddr> esi <esi>

    """

    schema = {
        'evi': {
            Any(): {
                'producer': {
                    Any(): {
                        'host_ip': {
                            Any(): {
                                'eth_tag': int,
                                'mac_addr': str,
                                'next_hops': ListOf(
                                    str
                                )
                            }
                        }
                    }
                }
            }
        }
    }

# =============================================
# Parser for 'show l2route evpn mac ip'
# =============================================
class ShowL2routeEvpnMacIp(ShowL2routeEvpnMacIpSchema):
    """ Parser for show l2route evpn mac ip
                   show l2route evpn mac ip esi <esi>
                   show l2route evpn mac ip mac-address <macaddr>
                   show l2route evpn mac ip mac-address <macaddr> esi <esi>
                   show l2route evpn mac ip next-hop <next-hop>
                   show l2route evpn mac ip next-hop <next-hop> mac-address <macaddr>
                   show l2route evpn mac ip next-hop <next-hop> mac-address <macaddr> esi <esi>
                   show l2route evpn mac ip producer <prod>
                   show l2route evpn mac ip producer <prod> next-hop <next-hop>
                   show l2route evpn mac ip producer <prod> next-hop <next-hop> mac-address <macaddr>
                   show l2route evpn mac ip producer <prod> next-hop <next-hop> mac-address <macaddr> esi <esi>
                   show l2route evpn mac ip topology <evi:etag>
                   show l2route evpn mac ip topology <evi:etag> producer <prod>
                   show l2route evpn mac ip topology <evi:etag> producer <prod> next-hop <next-hop>
                   show l2route evpn mac ip topology <evi:etag> producer <prod> next-hop <next-hop> mac-address <macaddr>
                   show l2route evpn mac ip topology <evi:etag> producer <prod> next-hop <next-hop> mac-address <macaddr> esi <esi>
                   show l2route evpn mac ip topology <evi>
                   show l2route evpn mac ip topology <evi> producer <prod>
                   show l2route evpn mac ip topology <evi> producer <prod> next-hop <next-hop>
                   show l2route evpn mac ip topology <evi> producer <prod> next-hop <next-hop> mac-address <macaddr>
                   show l2route evpn mac ip topology <evi> producer <prod> next-hop <next-hop> mac-address <macaddr> esi <esi>

    """

    cli_command = [
        'show l2route evpn mac ip',
        'show l2route evpn mac ip esi {esi}',
        'show l2route evpn mac ip mac-address {macaddr}',
        'show l2route evpn mac ip mac-address {macaddr} esi {esi}',
        'show l2route evpn mac ip next-hop {next_hop}',
        'show l2route evpn mac ip next-hop {next_hop} mac-address {macaddr}',
        'show l2route evpn mac ip next-hop {next_hop} mac-address {macaddr} esi {esi}',
        'show l2route evpn mac ip producer {prod}',
        'show l2route evpn mac ip producer {prod} next-hop {next_hop}',
        'show l2route evpn mac ip producer {prod} next-hop {next_hop} mac-address {macaddr}',
        'show l2route evpn mac ip producer {prod} next-hop {next_hop} mac-address {macaddr} esi {esi}',
        'show l2route evpn mac ip topology {evi_etag}',
        'show l2route evpn mac ip topology {evi_etag} producer {prod}',
        'show l2route evpn mac ip topology {evi_etag} producer {prod} next-hop {next_hop}',
        'show l2route evpn mac ip topology {evi_etag} producer {prod} next-hop {next_hop} mac-address {macaddr}',
        'show l2route evpn mac ip topology {evi_etag} producer {prod} next-hop {next_hop} mac-address {macaddr} esi {esi}',
        'show l2route evpn mac ip topology {evi}',
        'show l2route evpn mac ip topology {evi} producer {prod}',
        'show l2route evpn mac ip topology {evi} producer {prod} next-hop {next_hop}',
        'show l2route evpn mac ip topology {evi} producer {prod} next-hop {next_hop} mac-address {macaddr}',
        'show l2route evpn mac ip topology {evi} producer {prod} next-hop {next_hop} mac-address {macaddr} esi {esi}'
        ]

    def cli (self, output=None, esi=None, macaddr=None, next_hop=None, prod=None, evi=None, etag=None):
        if not output:
            cli_command = 'show l2route evpn mac ip'

            if esi:
                cli_command += ' esi {esi}'.format(esi=esi)
            if macaddr:
                cli_command += ' mac-address {macaddr}'.format(macaddr=macaddr)
            if next_hop:
                cli_command += ' next-hop {next_hop}'.format(next_hop=next_hop)
            if prod:
                cli_command += ' producer {prod}'.format(prod=prod)
            if evi:
                if etag:
                    cli_command += ' topology {evi}:{etag}'.format(evi,etag)
                else:
                    cli_command += ' topology {evi}'.format(evi=evi)

            cli_output = self.device.execute(cli_command)
        else:
            cli_output = output

        #  EVI       ETag  Prod    Mac Address         Host IP                Next Hop(s)
        p1 = re.compile(r'^EVI\s+ETag\s+Prod\s+Mac Address\s+Host IP\s+Next Hop\(s\)$')

        #    1          0   BGP 0011.0011.0011  192.168.11.254            V:20011 3.3.3.2
        #    1          0 L2VPN aabb.0011.0011 FE80::A8BB:FF:FE11:11 \
        p2 = re.compile(r'^(?P<evi>\d+)\s+(?P<eth_tag>\d+)\s+(?P<producer>\w+)\s+(?P<mac_addr>[0-9a-fA-F.]+)'
                        r'\s+(?P<host_ip>[0-9a-fA-F.:]+)\s+(?P<next_hop>.+)$')

        # Et0/1:11
        p3 = re.compile(r'^(?P<next_hop>.+)$')

        parser_dict = {}
        header_found = False
        next_hop_in_newline = False

        for line in cli_output.splitlines():
            line = line.strip()
            if not line:
                continue

            # test for the correct header
            m = p1.match(line)
            if m:
                header_found = True
                continue

            #    1          0   BGP 0011.0011.0011  192.168.11.254            V:20011 3.3.3.2
            #    1          0 L2VPN aabb.0011.0011 FE80::A8BB:FF:FE11:11 \
            m = p2.match(line)
            if m:
                group = m.groupdict()

                evis = parser_dict.setdefault('evi', {})
                evi_list = evis.setdefault(int(group['evi']), {})

                producers = evi_list.setdefault('producer', {})
                producers_list = producers.setdefault( group['producer'], {} )

                host_ip = producers_list.setdefault( 'host_ip' , {} )
                host_ip_list = host_ip.setdefault( group['host_ip'], {} )

                if group['next_hop'] != '\\':
                    host_ip_list.update({
                        'eth_tag': int(group['eth_tag']),
                        'mac_addr': group['mac_addr']
                    })
                    next_hops = host_ip_list.setdefault('next_hops', [])
                    next_hops.append(group['next_hop'])
                else:
                    eth_tag = int(group['eth_tag'])
                    mac_addr = group['mac_addr']
                    next_hop_in_newline = True

                continue

            # Et0/1:11
            m = p3.match(line)
            if m:
                group = m.groupdict()
                if next_hop_in_newline:
                    host_ip_list.update({
                        'eth_tag': eth_tag,
                        'mac_addr': mac_addr
                    })
                    next_hops = host_ip_list.setdefault('next_hops', [])
                    next_hops.append(group['next_hop'])
                next_hop_in_newline = False
                continue

        if not header_found:
            return ({})
        return (parser_dict)
