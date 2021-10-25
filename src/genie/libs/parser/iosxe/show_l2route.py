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
    * show l2route evpn mac ip host-ip <ip> topology <evi_etag> detail
    * show l2route evpn mac ip host-ip <ip> topology <evi_etag> esi <esi> detail
    * show l2route evpn mac ip host-ip <ip> topology <evi_etag> mac-address <mac_addr> detail
    * show l2route evpn mac ip host-ip <ip> topology <evi_etag> mac-address <mac_addr> esi <esi> detail
    * show l2route evpn mac ip host-ip <ip> topology <evi_etag> next-hop <next_hop> detail
    * show l2route evpn mac ip host-ip <ip> topology <evi_etag> next-hop <next_hop> esi <esi> detail
    * show l2route evpn mac ip host-ip <ip> topology <evi_etag> next-hop <next_hop> mac-address <mac_addr> detail
    * show l2route evpn mac ip host-ip <ip> topology <evi_etag> next-hop <next_hop> mac-address <mac_addr> esi <esi> detail
    * show l2route evpn mac ip host-ip <ip> topology <evi_etag> producer <producer> mac-address <mac_addr> detail
    * show l2route evpn mac ip host-ip <ip> topology <evi_etag> producer <producer> mac-address <mac_addr> esi <esi> detail
    * show l2route evpn imet detail
    * show l2route evpn imet origin-rtr <origin-ip> detail
    * show l2route evpn imet producer <prod> detail
    * show l2route evpn imet producer <prod> origin-rtr <origin-ip> detail
    * show l2route evpn imet topology <evi_etag> detail
    * show l2route evpn imet topology <evi_etag> producer <prod> detail
    * show l2route evpn imet topology <evi_etag> origin-rtr <origin-ip> detail
    * show l2route evpn imet topology <evi_etag> producer <prod> origin-rtr <origin-ip> detail
    * show l2route evpn mac ip
    * show l2route evpn mac ip host-ip <ip>
    * show l2route evpn mac ip esi <esi>
    * show l2route evpn mac ip host-ip <ip> esi <esi>
    * show l2route evpn mac ip mac-address <macaddr>
    * show l2route evpn mac ip mac-address <macaddr> esi <esi>
    * show l2route evpn mac ip host-ip <ip> mac-address <macaddr> esi <esi>
    * show l2route evpn mac ip next-hop <next-hop>
    * show l2route evpn mac ip next-hop <next-hop> mac-address <macaddr>
    * show l2route evpn mac ip next-hop <next-hop> mac-address <macaddr> esi <esi>
    * show l2route evpn mac ip host-ip <ip> next-hop <next-hop> mac-address <macaddr> esi <esi>
    * show l2route evpn mac ip producer <prod>
    * show l2route evpn mac ip producer <prod> next-hop <next-hop>
    * show l2route evpn mac ip producer <prod> next-hop <next-hop> mac-address <macaddr>
    * show l2route evpn mac ip producer <prod> next-hop <next-hop> mac-address <macaddr> esi <esi>
    * show l2route evpn mac ip host-ip <ip> producer <prod> next-hop <next-hop> mac-address <macaddr> esi <esi>
    * show l2route evpn mac ip topology <evi_etag>
    * show l2route evpn mac ip topology <evi_etag> producer <prod>
    * show l2route evpn mac ip topology <evi_etag> producer <prod> next-hop <next-hop>
    * show l2route evpn mac ip topology <evi_etag> producer <prod> next-hop <next-hop> mac-address <macaddr>
    * show l2route evpn mac ip topology <evi_etag> producer <prod> next-hop <next-hop> mac-address <macaddr> esi <esi>
    * show l2route evpn mac ip host-ip <ip> topology <evi_etag> producer <prod> next-hop <next-hop> mac-address <macaddr> esi <esi>
    * show l2route evpn default-gateway [host-ip <ip>] [topology <evi>[:<etag>]] [producer <producer>] [next-hop <nexthop>] [mac-address <mac>] [esi <esi-value>]
    * show l2route evpn default-gateway [host-ip <ip>] [topology <evi>[:<etag>]] [producer <producer>] [next-hop <nexthop>] [mac-address <mac>] [esi <esi-value>] detail
    * show l2route evpn peers [topology <evi>[:<etag>]] [peer-ip <peer_id>]
    * show l2route evpn peers [topology <evi>[:<etag>]] [peer-ip <peer_id>] detail
    * show l2route evpn mac detail
    * show l2route evpn mac esi <esi> detail
    * show l2route evpn mac mac-address <mac_addr> detail
    * show l2route evpn mac mac-address <mac_addr> esi <esi> detail
    * show l2route evpn mac next-hop <next_hop> detail
    * show l2route evpn mac next-hop <next_hop> esi <esi> detail
    * show l2route evpn mac next-hop <next_hop> mac-address <mac_addr> detail
    * show l2route evpn mac next-hop <next_hop> mac-address <mac_addr> esi <esi> detail
    * show l2route evpn mac producer <producer> detail
    * show l2route evpn mac producer <producer> esi <esi> detail
    * show l2route evpn mac producer <producer> mac-address <mac_addr> detail
    * show l2route evpn mac producer <producer> mac-address <mac_addr> esi <esi> detail
    * show l2route evpn mac producer <producer> next-hop <next_hop> detail
    * show l2route evpn mac producer <producer> next-hop <next_hop> esi <esi> detail
    * show l2route evpn mac producer <producer> next-hop <next_hop> mac-address <mac_addr> detail
    * show l2route evpn mac producer <producer> next-hop <next_hop> mac-address <mac_addr> esi <esi> detail
    * show l2route evpn mac topology <evi_etag> detail
    * show l2route evpn mac topology <evi_etag> esi <esi> detail
    * show l2route evpn mac topology <evi_etag> mac-address <mac_addr> detail
    * show l2route evpn mac topology <evi_etag> mac-address <mac_addr> esi <esi> detail
    * show l2route evpn mac topology <evi_etag> next-hop <next_hop> detail
    * show l2route evpn mac topology <evi_etag> next-hop <next_hop> esi <esi> detail
    * show l2route evpn mac topology <evi_etag> next-hop <next_hop> mac-address <mac_addr> detail
    * show l2route evpn mac topology <evi_etag> next-hop <next_hop> mac-address <mac_addr> esi <esi> detail
    * show l2route evpn mac topology <evi_etag> producer <producer> mac-address <mac_addr> detail
    * show l2route evpn mac topology <evi_etag> producer <producer> mac-address <mac_addr> esi <esi> detail
    * show l2route evpn mac topology <evi_etag> producer <producer> next-hop <next_hop> mac-address <mac_addr> esi <esi> detail
    * show l2route evpn mac
    * show l2route evpn mac esi <esi>
    * show l2route evpn mac mac-address <mac_addr>
    * show l2route evpn mac mac-address <mac_addr> esi <esi>
    * show l2route evpn mac next-hop <next_hop>
    * show l2route evpn mac next-hop <next_hop> esi <esi>
    * show l2route evpn mac next-hop <next_hop> mac-address <mac_addr>
    * show l2route evpn mac next-hop <next_hop> mac-address <mac_addr> esi <esi>
    * show l2route evpn mac producer <producer>
    * show l2route evpn mac producer <producer> esi <esi>
    * show l2route evpn mac producer <producer> mac-address <mac_addr>
    * show l2route evpn mac producer <producer> mac-address <mac_addr> esi <esi>
    * show l2route evpn mac producer <producer> next-hop <next_hop>
    * show l2route evpn mac producer <producer> next-hop <next_hop> esi <esi>
    * show l2route evpn mac producer <producer> next-hop <next_hop> mac-address <mac_addr>
    * show l2route evpn mac producer <producer> next-hop <next_hop> mac-address <mac_addr> esi <esi>
    * show l2route evpn mac topology <evi_etag>
    * show l2route evpn mac topology <evi_etag> esi <esi>
    * show l2route evpn mac topology <evi_etag> mac-address <mac_addr>
    * show l2route evpn mac topology <evi_etag> mac-address <mac_addr> esi <esi>
    * show l2route evpn mac topology <evi_etag> next-hop <next_hop>
    * show l2route evpn mac topology <evi_etag> next-hop <next_hop> esi <esi>
    * show l2route evpn mac topology <evi_etag> next-hop <next_hop> mac-address <mac_addr>
    * show l2route evpn mac topology <evi_etag> next-hop <next_hop> mac-address <mac_addr> esi <esi>
    * show l2route evpn mac topology <evi_etag> producer <producer> mac-address <mac_addr>
    * show l2route evpn mac topology <evi_etag> producer <producer> mac-address <mac_addr> esi <esi>
    * show l2route evpn mac topology <evi_etag> producer <producer> next-hop <next_hop> mac-address <mac_addr> esi <esi>

Copyright (c) 2021 by Cisco Systems, Inc.
All rights reserved.

'''
import re

# genie
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, ListOf, Optional


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
                   show l2route evpn mac ip host-ip <ip> topology <evi_etag> detail
                   show l2route evpn mac ip host-ip <ip> topology <evi_etag> esi <esi> detail
                   show l2route evpn mac ip host-ip <ip> topology <evi_etag> mac-address <mac_addr> detail
                   show l2route evpn mac ip host-ip <ip> topology <evi_etag> mac-address <mac_addr> esi <esi> detail
                   show l2route evpn mac ip host-ip <ip> topology <evi_etag> next-hop <next_hop> detail
                   show l2route evpn mac ip host-ip <ip> topology <evi_etag> next-hop <next_hop> esi <esi> detail
                   show l2route evpn mac ip host-ip <ip> topology <evi_etag> next-hop <next_hop> mac-address <mac_addr> detail
                   show l2route evpn mac ip host-ip <ip> topology <evi_etag> next-hop <next_hop> mac-address <mac_addr> esi <esi> detail
                   show l2route evpn mac ip host-ip <ip> topology <evi_etag> producer <producer> mac-address <mac_addr> detail
                   show l2route evpn mac ip host-ip <ip> topology <evi_etag> producer <producer> mac-address <mac_addr> esi <esi> detail
    """

    schema = {
        'evi': {
            Any(): {
                'producer': {
                    Any(): {
                        'host_ips': {
                            Any(): {
                                'eth_tag': {
                                    Any(): {
                                        'mac_addr': {
                                            Any() : {
                                                'seq_number': int,
                                                'label_2': int,
                                                'esi': str,
                                                'mac_rt_flags': str,
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
                   show l2route evpn mac ip host-ip <ip> topology <evi_etag> detail
                   show l2route evpn mac ip host-ip <ip> topology <evi_etag> esi <esi> detail
                   show l2route evpn mac ip host-ip <ip> topology <evi_etag> mac-address <mac_addr> detail
                   show l2route evpn mac ip host-ip <ip> topology <evi_etag> mac-address <mac_addr> esi <esi> detail
                   show l2route evpn mac ip host-ip <ip> topology <evi_etag> next-hop <next_hop> detail
                   show l2route evpn mac ip host-ip <ip> topology <evi_etag> next-hop <next_hop> esi <esi> detail
                   show l2route evpn mac ip host-ip <ip> topology <evi_etag> next-hop <next_hop> mac-address <mac_addr> detail
                   show l2route evpn mac ip host-ip <ip> topology <evi_etag> next-hop <next_hop> mac-address <mac_addr> esi <esi> detail
                   show l2route evpn mac ip host-ip <ip> topology <evi_etag> producer <producer> mac-address <mac_addr> detail
                   show l2route evpn mac ip host-ip <ip> topology <evi_etag> producer <producer> mac-address <mac_addr> esi <esi> detail
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
                   'show l2route evpn mac ip host-ip {ip} topology {evi_etag} detail',
                   'show l2route evpn mac ip host-ip {ip} topology {evi_etag} esi {esi} detail',
                   'show l2route evpn mac ip host-ip {ip} topology {evi_etag} mac-address {mac_addr} detail',
                   'show l2route evpn mac ip host-ip {ip} topology {evi_etag} mac-address {mac_addr} esi {esi} detail',
                   'show l2route evpn mac ip host-ip {ip} topology {evi_etag} next-hop {next_hop} detail',
                   'show l2route evpn mac ip host-ip {ip} topology {evi_etag} next-hop {next_hop} esi {esi} detail',
                   'show l2route evpn mac ip host-ip {ip} topology {evi_etag} next-hop {next_hop} mac-address {mac_addr} detail',
                   'show l2route evpn mac ip host-ip {ip} topology {evi_etag} next-hop {next_hop} mac-address {mac_addr} esi {esi} detail',
                   'show l2route evpn mac ip host-ip {ip} topology {evi_etag} producer {producer} mac-address {mac_addr} detail',
                   'show l2route evpn mac ip host-ip {ip} topology {evi_etag} producer {producer} mac-address {mac_addr} esi {esi} detail'
    ]

    def cli(self, output=None, ip=None, esi=None, mac_addr=None, next_hop=None, producer=None, evi_etag=None):
        if not output:
            cli_cmd = 'show l2route evpn mac ip'
            if ip:
                cli_cmd += ' host-ip {ip}'.format(ip=ip)
            if evi_etag:
                cli_cmd += ' topology {evi_etag}'.format(evi_etag=evi_etag)
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
        p10 = re.compile(r'^[Next Hop\(s\):]*\s*(?P<next_hop>.+)$')

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
                mac_address = group['mac_addr']
                continue

            # Host IP:                  192.168.12.254
            m = p5.match(line)
            if m:
                group = m.groupdict()
                host_ips = producers.setdefault('host_ips', {})
                routes = host_ips.setdefault(group['host_ip'], {})

                etag_list = routes.setdefault('eth_tag', {})
                etags = etag_list.setdefault(eth_tag, {})

                mac_addr_list = etags.setdefault('mac_addr', {})
                mac_addrs = mac_addr_list.setdefault(mac_address, {})

                continue

            # Sequence Number:          0
            m = p6.match(line)
            if m:
                group = m.groupdict()
                mac_addrs.update({'seq_number': int(group['seq_number'])})
                continue

            # Label 2:                  0
            m = p7.match(line)
            if m:
                group = m.groupdict()
                mac_addrs.update({'label_2': int(group['label_2'])})
                continue

            # ESI:                      0000.0000.0000.0000.0000
            m = p8.match(line)
            if m:
                group = m.groupdict()
                mac_addrs.update({'esi': group['esi']})
                continue

            # MAC Route Flags:          BInt(Brm)Dgr
            m = p9.match(line)
            if m:
                group = m.groupdict()
                mac_addrs.update({'mac_rt_flags': group['mac_rt_flags']})
                continue

            # Next Hop(s):              L:16 2.2.2.1
            m = p10.match(line)
            if m:
                group = m.groupdict()
                next_hops = group['next_hop'].split(", ")
                mac_addrs.update({'next_hops': next_hops })
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
                   show l2route evpn imet topology <evi_etag> detail
                   show l2route evpn imet topology <evi_etag> producer <prod> detail
                   show l2route evpn imet topology <evi_etag> origin-rtr <origin-ip> detail
                   show l2route evpn imet topology <evi_etag> producer <prod> origin-rtr <origin-ip> detail

    """

    schema = {
        'evi': {
            Any(): {
                'producer': {
                    Any(): {
                        'origin_router_ip': {
                            Any(): {
                                'eth_tag': {
                                    Any() : {
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
                                            str
                                        )
                                    }
                                }
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
                   show l2route evpn imet topology <evi_etag> detail
                   show l2route evpn imet topology <evi_etag> producer <prod> detail
                   show l2route evpn imet topology <evi_etag> origin-rtr <origin-ip> detail
                   show l2route evpn imet topology <evi_etag> producer <prod> origin-rtr <origin-ip> detail

    """

    cli_command = [
        'show l2route evpn imet detail',
        'show l2route evpn imet origin-rtr {origin_ip} detail',
        'show l2route evpn imet producer {prod} detail',
        'show l2route evpn imet producer {prod} origin-rtr {origin_ip} detail',
        'show l2route evpn imet topology {evi_etag} detail',
        'show l2route evpn imet topology {evi_etag} producer {prod} detail',
        'show l2route evpn imet topology {evi_etag} origin-rtr {origin_ip} detail',
        'show l2route evpn imet topology {evi_etag} producer {prod} origin-rtr {origin_ip} detail'
    ]

    def cli(self, output=None, origin_ip=None, prod=None, evi_etag=None):
        if not output:
            cli_command = 'show l2route evpn imet'
            if evi_etag:
                cli_command += ' topology {evi_etag}'.format(evi_etag=evi_etag)
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

        #Multicast Proxy:          IGMP, MLD
        p10 = re.compile(r'^Multicast Proxy:\s+(?P<multi_proxy>.+)$')

        #Next Hop(s):              V:20011 3.3.3.2
        #Next Hop(s):              N/A
        p11 = re.compile(r'^[Next Hop\(s\):]+\s+(?P<next_hop>[\w\s.:()/]+)$')

        parser_dict = {}

        for line in cli_output.splitlines():
            line = line.strip()
            if not line:
                continue

            #EVPN Instance
            m = p1.match(line)
            if m:
                group = m.groupdict()
                eviNum = int(group['evi'])
                evi_list = parser_dict.setdefault('evi',{})
                evis = evi_list.setdefault(eviNum,{})
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
                eth_tag_list = origins_rtr_ip.setdefault('eth_tag', {})
                eth_tags = eth_tag_list.setdefault(eth_tag, {})
                next_hops = eth_tags.setdefault('next_hops', [])
                continue

            #Route Ethernet Tag:
            m = p5.match(line)
            if m:
                group = m.groupdict()
                eth_tags.update({'router_eth_tag': int(group['r_eth_tag'] ) } )
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
                tunnel_info = eth_tags.setdefault('tunnel_id', {})
                tunnel_id = tunnel_info.setdefault(tun_id, {})
                tunnel_id.update({'tunnel_flags': tun_flag,
                                  'tunnel_type': tun_type,
                                  'tunnel_labels': tun_labels
                                  })
                continue

            #Multicast Proxy:
            m = p10.match(line)
            if m:
                group = m.groupdict()
                eth_tags.update({'multi_proxy': str(group['multi_proxy'])})
                continue

            #Next Hop(s):
            m = p11.match(line)
            if m:
                group = m.groupdict()
                next_hops.append(group['next_hop'])
                continue
        return (parser_dict)

# =============================================
# Schema for 'show l2route evpn mac ip'
# =============================================
class ShowL2routeEvpnMacIpSchema(MetaParser):
    """ Schema for show l2route evpn mac ip
                   show l2route evpn mac ip host-ip <ip>
                   show l2route evpn mac ip esi <esi>
                   show l2route evpn mac ip host-ip <ip> esi <esi>
                   show l2route evpn mac ip mac-address <macaddr>
                   show l2route evpn mac ip mac-address <macaddr> esi <esi>
                   show l2route evpn mac ip host-ip <ip> mac-address <macaddr> esi <esi>
                   show l2route evpn mac ip next-hop <next-hop>
                   show l2route evpn mac ip next-hop <next-hop> mac-address <macaddr>
                   show l2route evpn mac ip next-hop <next-hop> mac-address <macaddr> esi <esi>
                   show l2route evpn mac ip host-ip <ip> next-hop <next-hop> mac-address <macaddr> esi <esi>
                   show l2route evpn mac ip producer <prod>
                   show l2route evpn mac ip producer <prod> next-hop <next-hop>
                   show l2route evpn mac ip producer <prod> next-hop <next-hop> mac-address <macaddr>
                   show l2route evpn mac ip producer <prod> next-hop <next-hop> mac-address <macaddr> esi <esi>
                   show l2route evpn mac ip host-ip <ip> producer <prod> next-hop <next-hop> mac-address <macaddr> esi <esi>
                   show l2route evpn mac ip topology <evi_etag>
                   show l2route evpn mac ip topology <evi_etag> producer <prod>
                   show l2route evpn mac ip topology <evi_etag> producer <prod> next-hop <next-hop>
                   show l2route evpn mac ip topology <evi_etag> producer <prod> next-hop <next-hop> mac-address <macaddr>
                   show l2route evpn mac ip topology <evi_etag> producer <prod> next-hop <next-hop> mac-address <macaddr> esi <esi>
                   show l2route evpn mac ip host-ip <ip> topology <evi_etag> producer <prod> next-hop <next-hop> mac-address <macaddr> esi <esi>

    """

    schema = {
        'evi': {
            Any(): {
                'producer': {
                    Any(): {
                        'host_ip': {
                            Any(): {
                                'eth_tag': {
                                    Any() : {
                                        'mac_addr': {
                                            Any() : {
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
                }
            }
        }
    }

# =============================================
# Parser for 'show l2route evpn mac ip'
# =============================================
class ShowL2routeEvpnMacIp(ShowL2routeEvpnMacIpSchema):
    """ Parser for show l2route evpn mac ip
                   show l2route evpn mac ip host-ip <ip>
                   show l2route evpn mac ip esi <esi>
                   show l2route evpn mac ip host-ip <ip> esi <esi>
                   show l2route evpn mac ip mac-address <macaddr>
                   show l2route evpn mac ip mac-address <macaddr> esi <esi>
                   show l2route evpn mac ip host-ip <ip> mac-address <macaddr> esi <esi>
                   show l2route evpn mac ip next-hop <next-hop>
                   show l2route evpn mac ip next-hop <next-hop> mac-address <macaddr>
                   show l2route evpn mac ip next-hop <next-hop> mac-address <macaddr> esi <esi>
                   show l2route evpn mac ip host-ip <ip> next-hop <next-hop> mac-address <macaddr> esi <esi>
                   show l2route evpn mac ip producer <prod>
                   show l2route evpn mac ip producer <prod> next-hop <next-hop>
                   show l2route evpn mac ip producer <prod> next-hop <next-hop> mac-address <macaddr>
                   show l2route evpn mac ip producer <prod> next-hop <next-hop> mac-address <macaddr> esi <esi>
                   show l2route evpn mac ip host-ip <ip> producer <prod> next-hop <next-hop> mac-address <macaddr> esi <esi>
                   show l2route evpn mac ip topology <evi_etag>
                   show l2route evpn mac ip topology <evi_etag> producer <prod>
                   show l2route evpn mac ip topology <evi_etag> producer <prod> next-hop <next-hop>
                   show l2route evpn mac ip topology <evi_etag> producer <prod> next-hop <next-hop> mac-address <macaddr>
                   show l2route evpn mac ip topology <evi_etag> producer <prod> next-hop <next-hop> mac-address <macaddr> esi <esi>
                   show l2route evpn mac ip host-ip <ip> topology <evi_etag> producer <prod> next-hop <next-hop> mac-address <macaddr> esi <esi>

    """

    cli_command = [
        'show l2route evpn mac ip',
        'show l2route evpn mac ip host-ip {ip}',
        'show l2route evpn mac ip esi {esi}',
        'show l2route evpn mac ip host-ip {ip} esi {esi}',
        'show l2route evpn mac ip mac-address {macaddr}',
        'show l2route evpn mac ip mac-address {macaddr} esi {esi}',
        'show l2route evpn mac ip host-ip {ip} mac-address {macaddr} esi {esi}',
        'show l2route evpn mac ip next-hop {next_hop}',
        'show l2route evpn mac ip next-hop {next_hop} mac-address {macaddr}',
        'show l2route evpn mac ip next-hop {next_hop} mac-address {macaddr} esi {esi}',
        'show l2route evpn mac ip host-ip {ip} next-hop {next_hop} mac-address {macaddr} esi {esi}',
        'show l2route evpn mac ip producer {prod}',
        'show l2route evpn mac ip producer {prod} next-hop {next_hop}',
        'show l2route evpn mac ip producer {prod} next-hop {next_hop} mac-address {macaddr}',
        'show l2route evpn mac ip producer {prod} next-hop {next_hop} mac-address {macaddr} esi {esi}',
        'show l2route evpn mac ip host-ip {ip} producer {prod} next-hop {next_hop} mac-address {macaddr} esi {esi}',
        'show l2route evpn mac ip topology {evi_etag}',
        'show l2route evpn mac ip topology {evi_etag} producer {prod}',
        'show l2route evpn mac ip topology {evi_etag} producer {prod} next-hop {next_hop}',
        'show l2route evpn mac ip topology {evi_etag} producer {prod} next-hop {next_hop} mac-address {macaddr}',
        'show l2route evpn mac ip topology {evi_etag} producer {prod} next-hop {next_hop} mac-address {macaddr} esi {esi}',
        'show l2route evpn mac ip host-ip {ip} topology {evi_etag} producer {prod} next-hop {next_hop} mac-address {macaddr} esi {esi}'
        ]

    def cli (self, output=None, esi=None, macaddr=None, next_hop=None, prod=None, evi_etag=None, ip=None):
        if not output:
            cli_command = 'show l2route evpn mac ip'

            if ip:
                cli_command += ' host-ip {ip}'.format(ip=ip)
            if evi_etag:
                cli_command += ' topology {evi_etag}'.format(evi_etag=evi_etag)
            if prod:
                cli_command += ' producer {prod}'.format(prod=prod)
            if next_hop:
                cli_command += ' next-hop {next_hop}'.format(next_hop=next_hop)
            if macaddr:
                cli_command += ' mac-address {macaddr}'.format(macaddr=macaddr)
            if esi:
                cli_command += ' esi {esi}'.format(esi=esi)

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
        p3 = re.compile(r'^(?!-)(?P<next_hop>.+)$')

        parser_dict = {}
        header_found = False

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
            #    1          0 L2VPN aabb.0011.0011 FE80::A8BB:FF:FE11:11    \
            m = p2.match(line)
            if m:
                group = m.groupdict()

                evis = parser_dict.setdefault('evi', {})
                evi_list = evis.setdefault(int(group['evi']), {})

                producers = evi_list.setdefault('producer', {})
                producers_list = producers.setdefault( group['producer'], {} )

                host_ip = producers_list.setdefault( 'host_ip' , {} )
                host_ip_list = host_ip.setdefault( group['host_ip'], {} )

                eth_tags = host_ip_list.setdefault('eth_tag', {})
                eth_tags_list = eth_tags.setdefault(int(group['eth_tag']) ,{})

                mac_addrs = eth_tags_list.setdefault('mac_addr', {})
                mac_addr_list = mac_addrs.setdefault(group['mac_addr'], {})

                next_hops = mac_addr_list.setdefault('next_hops', [])

                if group['next_hop'] != '\\':
                    next_hops.append(group['next_hop'])

                continue

            # Et0/1:11
            m = p3.match(line)
            if m:
                group = m.groupdict()
                if next_hops:
                    next_hops.append(group['next_hop'])
                continue

        if not header_found:
            return ({})
        return (parser_dict)

# ==============================================
# Schema for 'show l2route evpn default-gateway'
# ==============================================
class ShowL2routeEvpnDGWSchema(MetaParser):
    """ Schema for show l2route evpn default-gateway
                   show l2route evpn default-gateway host-ip <ip>
                   show l2route evpn default-gateway host-ip <ip> topology <evi-etag>
                   show l2route evpn default-gateway host-ip <ip> topology <evi-etag> producer <prod>
                   show l2route evpn default-gateway host-ip <ip> topology <evi-etag> producer <prod> next-hop <next_hop>
                   show l2route evpn default-gateway host-ip <ip> topology <evi-etag> producer <prod> next-hop <next_hop> mac-address <macaddr>
                   show l2route evpn default-gateway host-ip <ip> topology <evi-etag> producer <prod> next-hop <next_hop> mac-address <macaddr> esi <esi>
                   show l2route evpn default-gateway host-ip <ip> topology <evi-etag> producer <prod> next-hop <next_hop> esi <esi>
                   show l2route evpn default-gateway host-ip <ip> topology <evi-etag> producer <prod> mac-address <macaddr>
                   show l2route evpn default-gateway host-ip <ip> topology <evi-etag> producer <prod> mac-address <macaddr> esi <esi>
                   show l2route evpn default-gateway host-ip <ip> topology <evi-etag> producer <prod> esi <esi>
                   show l2route evpn default-gateway host-ip <ip> topology <evi-etag> next-hop <next_hop>
                   show l2route evpn default-gateway host-ip <ip> topology <evi-etag> next-hop <next_hop> mac-address <macaddr>
                   show l2route evpn default-gateway host-ip <ip> topology <evi-etag> next-hop <next_hop> mac-address <macaddr> esi <esi>
                   show l2route evpn default-gateway host-ip <ip> topology <evi-etag> next-hop <next_hop> esi <esi>
                   show l2route evpn default-gateway host-ip <ip> topology <evi-etag> mac-address <macaddr>
                   show l2route evpn default-gateway host-ip <ip> topology <evi-etag> <macaddr> esi <esi>
                   show l2route evpn default-gateway host-ip <ip> topology <evi-etag> esi <esi>
                   show l2route evpn default-gateway host-ip <ip> producer <prod>
                   show l2route evpn default-gateway host-ip <ip> producer <prod> next-hop <next_hop>
                   show l2route evpn default-gateway host-ip <ip> producer <prod> next-hop <next_hop> mac-address <macaddr>
                   show l2route evpn default-gateway host-ip <ip> producer <prod> next-hop <next_hop> mac-address <macaddr> esi <esi>
                   show l2route evpn default-gateway host-ip <ip> producer <prod> next-hop <next_hop> esi <esi>
                   show l2route evpn default-gateway host-ip <ip> producer <prod> mac-address <macaddr>
                   show l2route evpn default-gateway host-ip <ip> producer <prod> mac-address <macaddr> esi <esi>
                   show l2route evpn default-gateway host-ip <ip> producer <prod> esi <esi>
                   show l2route evpn default-gateway host-ip <ip> next-hop <next_hop>
                   show l2route evpn default-gateway host-ip <ip> next-hop <next_hop> mac-address <macaddr>
                   show l2route evpn default-gateway host-ip <ip> next-hop <next_hop> mac-address <macaddr> esi <esi>
                   show l2route evpn default-gateway host-ip <ip> next-hop <next_hop> esi <esi>
                   show l2route evpn default-gateway host-ip <ip> mac-address <macaddr>
                   show l2route evpn default-gateway host-ip <ip> mac-address <macaddr> esi <esi>
                   show l2route evpn default-gateway host-ip <ip> esi <esi>
                   show l2route evpn default-gateway topology <evi-etag>
                   show l2route evpn default-gateway topology <evi-etag> producer <prod>
                   show l2route evpn default-gateway topology <evi-etag> producer <prod> next-hop <next_hop>
                   show l2route evpn default-gateway topology <evi-etag> producer <prod> next-hop <next_hop> mac-address <macaddr>
                   show l2route evpn default-gateway topology <evi-etag> producer <prod> next-hop <next_hop> mac-address <macaddr> esi <esi>
                   show l2route evpn default-gateway topology <evi-etag> producer <prod> next-hop <next_hop> esi <esi>
                   show l2route evpn default-gateway topology <evi-etag> producer <prod> mac-address <macaddr>
                   show l2route evpn default-gateway topology <evi-etag> producer <prod> mac-address <macaddr> esi <esi>
                   show l2route evpn default-gateway topology <evi-etag> producer <prod> esi <esi>
                   show l2route evpn default-gateway topology <evi-etag> next-hop <next_hop>
                   show l2route evpn default-gateway topology <evi-etag> next-hop <next_hop> mac-address <macaddr>
                   show l2route evpn default-gateway topology <evi-etag> next-hop <next_hop> mac-address <macaddr> esi <esi>
                   show l2route evpn default-gateway topology <evi-etag> next-hop <next_hop> esi <esi>
                   show l2route evpn default-gateway topology <evi-etag> mac-address <macaddr>
                   show l2route evpn default-gateway topology <evi-etag> mac-address <macaddr> esi <esi>
                   show l2route evpn default-gateway topology <evi-etag> esi <esi>
                   show l2route evpn default-gateway producer <prod>
                   show l2route evpn default-gateway producer <prod> next-hop <next_hop>
                   show l2route evpn default-gateway producer <prod> next-hop <next_hop> mac-address <macaddr>
                   show l2route evpn default-gateway producer <prod> next-hop <next_hop> mac-address <macaddr> esi <esi>
                   show l2route evpn default-gateway producer <prod> next-hop <next_hop> esi <esi>
                   show l2route evpn default-gateway producer <prod> mac-address <macaddr>
                   show l2route evpn default-gateway producer <prod> mac-address <macaddr> esi <esi>
                   show l2route evpn default-gateway producer <prod> esi <esi>
                   show l2route evpn default-gateway next-hop <next_hop>
                   show l2route evpn default-gateway next-hop <next_hop> mac-address <macaddr>
                   show l2route evpn default-gateway next-hop <next_hop> mac-address <macaddr> esi <esi>
                   show l2route evpn default-gateway next-hop <next_hop> esi <esi>
                   show l2route evpn default-gateway mac-address <macaddr>
                   show l2route evpn default-gateway mac-address <macaddr> esi <esi>
                   show l2route evpn default-gateway esi <esi>
    """

    schema = {
        'evi': {
            Any(): {
                'eth_tag': {
                    Any(): {
                        'producer': {
                            Any(): {
                                'mac_addr': {
                                    Any(): {
                                        'host_ip': {
                                            Any(): {
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
                }
            }
        }
    }

# ==============================================
# Parser for 'show l2route evpn default-gateway'
# ==============================================
class ShowL2routeEvpnDGW(ShowL2routeEvpnDGWSchema):
    """ Parser for show l2route evpn default-gateway
                   show l2route evpn default-gateway host-ip <ip>
                   show l2route evpn default-gateway host-ip <ip> topology <evi-etag>
                   show l2route evpn default-gateway host-ip <ip> topology <evi-etag> producer <prod>
                   show l2route evpn default-gateway host-ip <ip> topology <evi-etag> producer <prod> next-hop <next_hop>
                   show l2route evpn default-gateway host-ip <ip> topology <evi-etag> producer <prod> next-hop <next_hop> mac-address <macaddr>
                   show l2route evpn default-gateway host-ip <ip> topology <evi-etag> producer <prod> next-hop <next_hop> mac-address <macaddr> esi <esi>
                   show l2route evpn default-gateway host-ip <ip> topology <evi-etag> producer <prod> next-hop <next_hop> esi <esi>
                   show l2route evpn default-gateway host-ip <ip> topology <evi-etag> producer <prod> mac-address <macaddr>
                   show l2route evpn default-gateway host-ip <ip> topology <evi-etag> producer <prod> mac-address <macaddr> esi <esi>
                   show l2route evpn default-gateway host-ip <ip> topology <evi-etag> producer <prod> esi <esi>
                   show l2route evpn default-gateway host-ip <ip> topology <evi-etag> next-hop <next_hop>
                   show l2route evpn default-gateway host-ip <ip> topology <evi-etag> next-hop <next_hop> mac-address <macaddr>
                   show l2route evpn default-gateway host-ip <ip> topology <evi-etag> next-hop <next_hop> mac-address <macaddr> esi <esi>
                   show l2route evpn default-gateway host-ip <ip> topology <evi-etag> next-hop <next_hop> esi <esi>
                   show l2route evpn default-gateway host-ip <ip> topology <evi-etag> mac-address <macaddr>
                   show l2route evpn default-gateway host-ip <ip> topology <evi-etag> <macaddr> esi <esi>
                   show l2route evpn default-gateway host-ip <ip> topology <evi-etag> esi <esi>
                   show l2route evpn default-gateway host-ip <ip> producer <prod>
                   show l2route evpn default-gateway host-ip <ip> producer <prod> next-hop <next_hop>
                   show l2route evpn default-gateway host-ip <ip> producer <prod> next-hop <next_hop> mac-address <macaddr>
                   show l2route evpn default-gateway host-ip <ip> producer <prod> next-hop <next_hop> mac-address <macaddr> esi <esi>
                   show l2route evpn default-gateway host-ip <ip> producer <prod> next-hop <next_hop> esi <esi>
                   show l2route evpn default-gateway host-ip <ip> producer <prod> mac-address <macaddr>
                   show l2route evpn default-gateway host-ip <ip> producer <prod> mac-address <macaddr> esi <esi>
                   show l2route evpn default-gateway host-ip <ip> producer <prod> esi <esi>
                   show l2route evpn default-gateway host-ip <ip> next-hop <next_hop>
                   show l2route evpn default-gateway host-ip <ip> next-hop <next_hop> mac-address <macaddr>
                   show l2route evpn default-gateway host-ip <ip> next-hop <next_hop> mac-address <macaddr> esi <esi>
                   show l2route evpn default-gateway host-ip <ip> next-hop <next_hop> esi <esi>
                   show l2route evpn default-gateway host-ip <ip> mac-address <macaddr>
                   show l2route evpn default-gateway host-ip <ip> mac-address <macaddr> esi <esi>
                   show l2route evpn default-gateway host-ip <ip> esi <esi>
                   show l2route evpn default-gateway topology <evi>
                   show l2route evpn default-gateway topology <evi-etag> producer <prod>
                   show l2route evpn default-gateway topology <evi-etag> producer <prod> next-hop <next_hop>
                   show l2route evpn default-gateway topology <evi-etag> producer <prod> next-hop <next_hop> mac-address <macaddr>
                   show l2route evpn default-gateway topology <evi-etag> producer <prod> next-hop <next_hop> mac-address <macaddr> esi <esi>
                   show l2route evpn default-gateway topology <evi-etag> producer <prod> next-hop <next_hop> esi <esi>
                   show l2route evpn default-gateway topology <evi-etag> producer <prod> mac-address <macaddr>
                   show l2route evpn default-gateway topology <evi-etag> producer <prod> mac-address <macaddr> esi <esi>
                   show l2route evpn default-gateway topology <evi-etag> producer <prod> esi <esi>
                   show l2route evpn default-gateway topology <evi-etag> next-hop <next_hop>
                   show l2route evpn default-gateway topology <evi-etag> next-hop <next_hop> mac-address <macaddr>
                   show l2route evpn default-gateway topology <evi-etag> next-hop <next_hop> mac-address <macaddr> esi <esi>
                   show l2route evpn default-gateway topology <evi-etag> next-hop <next_hop> esi <esi>
                   show l2route evpn default-gateway topology <evi-etag> mac-address <macaddr>
                   show l2route evpn default-gateway topology <evi-etag> mac-address <macaddr> esi <esi>
                   show l2route evpn default-gateway topology <evi-etag> esi <esi>
                   show l2route evpn default-gateway producer <prod>
                   show l2route evpn default-gateway producer <prod> next-hop <next_hop>
                   show l2route evpn default-gateway producer <prod> next-hop <next_hop> mac-address <macaddr>
                   show l2route evpn default-gateway producer <prod> next-hop <next_hop> mac-address <macaddr> esi <esi>
                   show l2route evpn default-gateway producer <prod> next-hop <next_hop> esi <esi>
                   show l2route evpn default-gateway producer <prod> mac-address <macaddr>
                   show l2route evpn default-gateway producer <prod> mac-address <macaddr> esi <esi>
                   show l2route evpn default-gateway producer <prod> esi <esi>
                   show l2route evpn default-gateway next-hop <next_hop>
                   show l2route evpn default-gateway next-hop <next_hop> mac-address <macaddr>
                   show l2route evpn default-gateway next-hop <next_hop> mac-address <macaddr> esi <esi>
                   show l2route evpn default-gateway next-hop <next_hop> esi <esi>
                   show l2route evpn default-gateway mac-address <macaddr>
                   show l2route evpn default-gateway mac-address <macaddr> esi <esi>
                   show l2route evpn default-gateway esi <esi>
    """

    cli_command = [
                   'show l2route evpn default-gateway',
                   'show l2route evpn default-gateway host-ip {ip}',
                   'show l2route evpn default-gateway host-ip {ip} topology {evi_etag}',
                   'show l2route evpn default-gateway host-ip {ip} topology {evi_etag} producer {prod}',
                   'show l2route evpn default-gateway host-ip {ip} topology {evi_etag} producer {prod} next-hop {next_hop}',
                   'show l2route evpn default-gateway host-ip {ip} topology {evi_etag} producer {prod} next-hop {next_hop} mac-address {macaddr}',
                   'show l2route evpn default-gateway host-ip {ip} topology {evi_etag} producer {prod} next-hop {next_hop} mac-address {macaddr} esi {esi}',
                   'show l2route evpn default-gateway host-ip {ip} topology {evi_etag} producer {prod} next-hop {next_hop} esi {esi}',
                   'show l2route evpn default-gateway host-ip {ip} topology {evi_etag} producer {prod} mac-address {macaddr}',
                   'show l2route evpn default-gateway host-ip {ip} topology {evi_etag} producer {prod} mac-address {macaddr} esi {esi}',
                   'show l2route evpn default-gateway host-ip {ip} topology {evi_etag} producer {prod} esi {esi}',
                   'show l2route evpn default-gateway host-ip {ip} topology {evi_etag} next-hop {next_hop}',
                   'show l2route evpn default-gateway host-ip {ip} topology {evi_etag} next-hop {next_hop} mac-address {macaddr}',
                   'show l2route evpn default-gateway host-ip {ip} topology {evi_etag} next-hop {next_hop} mac-address {macaddr} esi {esi}',
                   'show l2route evpn default-gateway host-ip {ip} topology {evi_etag} next-hop {next_hop} esi {esi}',
                   'show l2route evpn default-gateway host-ip {ip} topology {evi_etag} mac-address {macaddr}',
                   'show l2route evpn default-gateway host-ip {ip} topology {evi_etag} {macaddr} esi {esi}',
                   'show l2route evpn default-gateway host-ip {ip} topology {evi_etag} esi {esi}',
                   'show l2route evpn default-gateway host-ip {ip} producer {prod}',
                   'show l2route evpn default-gateway host-ip {ip} producer {prod} next-hop {next_hop}',
                   'show l2route evpn default-gateway host-ip {ip} producer {prod} next-hop {next_hop} mac-address {macaddr}',
                   'show l2route evpn default-gateway host-ip {ip} producer {prod} next-hop {next_hop} mac-address {macaddr} esi {esi}',
                   'show l2route evpn default-gateway host-ip {ip} producer {prod} next-hop {next_hop} esi {esi}',
                   'show l2route evpn default-gateway host-ip {ip} producer {prod} mac-address {macaddr}',
                   'show l2route evpn default-gateway host-ip {ip} producer {prod} mac-address {macaddr} esi {esi}',
                   'show l2route evpn default-gateway host-ip {ip} producer {prod} esi {esi}',
                   'show l2route evpn default-gateway host-ip {ip} next-hop {next_hop}',
                   'show l2route evpn default-gateway host-ip {ip} next-hop {next_hop} mac-address {macaddr}',
                   'show l2route evpn default-gateway host-ip {ip} next-hop {next_hop} mac-address {macaddr} esi {esi}',
                   'show l2route evpn default-gateway host-ip {ip} next-hop {next_hop} esi {esi}',
                   'show l2route evpn default-gateway host-ip {ip} mac-address {macaddr}',
                   'show l2route evpn default-gateway host-ip {ip} mac-address {macaddr} esi {esi}',
                   'show l2route evpn default-gateway host-ip {ip} esi {esi}',
                   'show l2route evpn default-gateway topology {evi_etag}',
                   'show l2route evpn default-gateway topology {evi_etag} producer {prod}',
                   'show l2route evpn default-gateway topology {evi_etag} producer {prod} next-hop {next_hop}',
                   'show l2route evpn default-gateway topology {evi_etag} producer {prod} next-hop {next_hop} mac-address {macaddr}',
                   'show l2route evpn default-gateway topology {evi_etag} producer {prod} next-hop {next_hop} mac-address {macaddr} esi {esi}',
                   'show l2route evpn default-gateway topology {evi_etag} producer {prod} next-hop {next_hop} esi {esi}',
                   'show l2route evpn default-gateway topology {evi_etag} producer {prod} mac-address {macaddr}',
                   'show l2route evpn default-gateway topology {evi_etag} producer {prod} mac-address {macaddr} esi {esi}',
                   'show l2route evpn default-gateway topology {evi_etag} producer {prod} esi {esi}',
                   'show l2route evpn default-gateway topology {evi_etag} next-hop {next_hop}',
                   'show l2route evpn default-gateway topology {evi_etag} next-hop {next_hop} mac-address {macaddr}',
                   'show l2route evpn default-gateway topology {evi_etag} next-hop {next_hop} mac-address {macaddr} esi {esi}',
                   'show l2route evpn default-gateway topology {evi_etag} next-hop {next_hop} esi {esi}',
                   'show l2route evpn default-gateway topology {evi_etag} mac-address {macaddr}',
                   'show l2route evpn default-gateway topology {evi_etag} mac-address {macaddr} esi {esi}',
                   'show l2route evpn default-gateway topology {evi_etag} esi {esi}',
                   'show l2route evpn default-gateway producer {prod}',
                   'show l2route evpn default-gateway producer {prod} next-hop {next_hop}',
                   'show l2route evpn default-gateway producer {prod} next-hop {next_hop} mac-address {macaddr}',
                   'show l2route evpn default-gateway producer {prod} next-hop {next_hop} mac-address {macaddr} esi {esi}',
                   'show l2route evpn default-gateway producer {prod} next-hop {next_hop} esi {esi}',
                   'show l2route evpn default-gateway producer {prod} mac-address {macaddr}',
                   'show l2route evpn default-gateway producer {prod} mac-address {macaddr} esi {esi}',
                   'show l2route evpn default-gateway producer {prod} esi {esi}',
                   'show l2route evpn default-gateway next-hop {next_hop}',
                   'show l2route evpn default-gateway next-hop {next_hop} mac-address {macaddr}',
                   'show l2route evpn default-gateway next-hop {next_hop} mac-address {macaddr} esi {esi}',
                   'show l2route evpn default-gateway next-hop {next_hop} esi {esi}',
                   'show l2route evpn default-gateway mac-address {macaddr}',
                   'show l2route evpn default-gateway mac-address {macaddr} esi {esi}',
                   'show l2route evpn default-gateway esi {esi}'
        ]

    def cli (self, output=None, host_ip=None, evi_etag=None, prod=None, next_hop=None, macaddr=None, esi=None):
        if not output:
            cli_command = 'show l2route evpn default-gateway'

            if host_ip:
                cli_command += ' host-ip {ip}'.format(ip=host_ip)
            if evi_etag:
                cli_command += ' topology {evi_etag}'.format(evi_etag=evi_etag)
            if prod:
                cli_command += ' producer {prod}'.format(prod=prod)
            if next_hop:
                cli_command += ' next-hop {next_hop}'.format(next_hop=next_hop)
            if macaddr:
                cli_command += ' mac-address {macaddr}'.format(macaddr=macaddr)
            if esi:
                cli_command += ' esi {esi}'.format(esi=esi)

            out = self.device.execute(cli_command)
        else:
            out = output

        #  EVI       ETag  Prod    Mac Address         Host IP                Next Hop(s)
        #    1          0   BGP 0011.0011.0011  192.168.11.254            V:20011 3.3.3.2
        #    1          0 L2VPN aabb.0011.0011 FE80::A8BB:FF:FE11:11 \
        p1 = re.compile(r'^(?P<evi>\d+)\s+(?P<eth_tag>\d+)\s+(?P<producer>\w+)\s+(?P<mac_addr>[0-9a-fA-F.]+)'
                        r'\s+(?P<host_ip>[0-9a-fA-F.:]+)\s+(?P<next_hop>.+)$')

        # Et0/1:11
        p2 = re.compile(r'^(?P<next_hop>.+)$')

        ret_dict = {}
        next_hop_list = []

        for line in out.splitlines():
            line = line.strip()
            if not line:
                continue

            #    1          0   BGP 0011.0011.0011  192.168.11.254            V:20011 3.3.3.2
            #    1          0 L2VPN aabb.0011.0011 FE80::A8BB:FF:FE11:11 \
            m = p1.match(line)
            if m:
                group = m.groupdict()

                evi_list = ret_dict.setdefault('evi', {}).setdefault(int(group['evi']), {})

                etag_list = evi_list.setdefault('eth_tag', {}).setdefault(int(group['eth_tag']), {})

                producers_list = etag_list.setdefault('producer', {}).setdefault( group['producer'], {})

                mac_list = producers_list.setdefault('mac_addr', {}).setdefault( group['mac_addr'], {})

                host_ip_list = mac_list.setdefault('host_ip' , {}).setdefault(group['host_ip'], {})

                next_hop_list = host_ip_list.setdefault('next_hops', [])
                if group['next_hop'] != '\\':
                    next_hop_list.append(group['next_hop'])

                continue

            # Et0/1:11
            m = p2.match(line)
            if m:
                group = m.groupdict()
                next_hop_list.append(group['next_hop'])
                continue

        return ret_dict

# =====================================================
# Schema for 'show l2route evpn default-gateway detail'
# =====================================================
class ShowL2routeEvpnDGWDetailSchema(MetaParser):
    """ Schema for show l2route evpn default-gateway detail
                   show l2route evpn default-gateway host-ip <ip> detail
                   show l2route evpn default-gateway host-ip <ip> topology <evi-etag> detail
                   show l2route evpn default-gateway host-ip <ip> topology <evi-etag> producer <prod> detail
                   show l2route evpn default-gateway host-ip <ip> topology <evi-etag> producer <prod> next-hop <next_hop> detail
                   show l2route evpn default-gateway host-ip <ip> topology <evi-etag> producer <prod> next-hop <next_hop> mac-address <macaddr> detail
                   show l2route evpn default-gateway host-ip <ip> topology <evi-etag> producer <prod> next-hop <next_hop> mac-address <macaddr> esi <esi> detail
                   show l2route evpn default-gateway host-ip <ip> topology <evi-etag> producer <prod> next-hop <next_hop> esi <esi> detail
                   show l2route evpn default-gateway host-ip <ip> topology <evi-etag> producer <prod> mac-address <macaddr> detail
                   show l2route evpn default-gateway host-ip <ip> topology <evi-etag> producer <prod> mac-address <macaddr> esi <esi> detail
                   show l2route evpn default-gateway host-ip <ip> topology <evi-etag> producer <prod> esi <esi> detail
                   show l2route evpn default-gateway host-ip <ip> topology <evi-etag> next-hop <next_hop> detail
                   show l2route evpn default-gateway host-ip <ip> topology <evi-etag> next-hop <next_hop> mac-address <macaddr> detail
                   show l2route evpn default-gateway host-ip <ip> topology <evi-etag> next-hop <next_hop> mac-address <macaddr> esi <esi> detail
                   show l2route evpn default-gateway host-ip <ip> topology <evi-etag> next-hop <next_hop> esi <esi> detail
                   show l2route evpn default-gateway host-ip <ip> topology <evi-etag> mac-address <macaddr> detail
                   show l2route evpn default-gateway host-ip <ip> topology <evi-etag> <macaddr> esi <esi> detail
                   show l2route evpn default-gateway host-ip <ip> topology <evi-etag> esi <esi> detail
                   show l2route evpn default-gateway host-ip <ip> producer <prod> detail
                   show l2route evpn default-gateway host-ip <ip> producer <prod> next-hop <next_hop> detail
                   show l2route evpn default-gateway host-ip <ip> producer <prod> next-hop <next_hop> mac-address <macaddr> detail
                   show l2route evpn default-gateway host-ip <ip> producer <prod> next-hop <next_hop> mac-address <macaddr> esi <esi> detail
                   show l2route evpn default-gateway host-ip <ip> producer <prod> next-hop <next_hop> esi <esi> detail
                   show l2route evpn default-gateway host-ip <ip> producer <prod> mac-address <macaddr> detail
                   show l2route evpn default-gateway host-ip <ip> producer <prod> mac-address <macaddr> esi <esi> detail
                   show l2route evpn default-gateway host-ip <ip> producer <prod> esi <esi> detail
                   show l2route evpn default-gateway host-ip <ip> next-hop <next_hop> detail
                   show l2route evpn default-gateway host-ip <ip> next-hop <next_hop> mac-address <macaddr> detail
                   show l2route evpn default-gateway host-ip <ip> next-hop <next_hop> mac-address <macaddr> esi <esi> detail
                   show l2route evpn default-gateway host-ip <ip> next-hop <next_hop> esi <esi> detail
                   show l2route evpn default-gateway host-ip <ip> mac-address <macaddr> detail
                   show l2route evpn default-gateway host-ip <ip> mac-address <macaddr> esi <esi> detail
                   show l2route evpn default-gateway host-ip <ip> esi <esi> detail
                   show l2route evpn default-gateway topology <evi-etag> detail
                   show l2route evpn default-gateway topology <evi-etag> producer <prod> detail
                   show l2route evpn default-gateway topology <evi-etag> producer <prod> next-hop <next_hop> detail
                   show l2route evpn default-gateway topology <evi-etag> producer <prod> next-hop <next_hop> mac-address <macaddr> detail
                   show l2route evpn default-gateway topology <evi-etag> producer <prod> next-hop <next_hop> mac-address <macaddr> esi <esi> detail
                   show l2route evpn default-gateway topology <evi-etag> producer <prod> next-hop <next_hop> esi <esi> detail
                   show l2route evpn default-gateway topology <evi-etag> producer <prod> mac-address <macaddr> detail
                   show l2route evpn default-gateway topology <evi-etag> producer <prod> mac-address <macaddr> esi <esi> detail
                   show l2route evpn default-gateway topology <evi-etag> producer <prod> esi <esi> detail
                   show l2route evpn default-gateway topology <evi-etag> next-hop <next_hop> detail
                   show l2route evpn default-gateway topology <evi-etag> next-hop <next_hop> mac-address <macaddr> detail
                   show l2route evpn default-gateway topology <evi-etag> next-hop <next_hop> mac-address <macaddr> esi <esi> detail
                   show l2route evpn default-gateway topology <evi-etag> next-hop <next_hop> esi <esi> detail
                   show l2route evpn default-gateway topology <evi-etag> mac-address <macaddr> detail
                   show l2route evpn default-gateway topology <evi-etag> mac-address <macaddr> esi <esi> detail
                   show l2route evpn default-gateway topology <evi-etag> esi <esi> detail
                   show l2route evpn default-gateway producer <prod> detail
                   show l2route evpn default-gateway producer <prod> next-hop <next_hop> detail
                   show l2route evpn default-gateway producer <prod> next-hop <next_hop> mac-address <macaddr> detail
                   show l2route evpn default-gateway producer <prod> next-hop <next_hop> mac-address <macaddr> esi <esi> detail
                   show l2route evpn default-gateway producer <prod> next-hop <next_hop> esi <esi> detail
                   show l2route evpn default-gateway producer <prod> mac-address <macaddr> detail
                   show l2route evpn default-gateway producer <prod> mac-address <macaddr> esi <esi> detail
                   show l2route evpn default-gateway producer <prod> esi <esi> detail
                   show l2route evpn default-gateway next-hop <next_hop> detail
                   show l2route evpn default-gateway next-hop <next_hop> mac-address <macaddr> detail
                   show l2route evpn default-gateway next-hop <next_hop> mac-address <macaddr> esi <esi> detail
                   show l2route evpn default-gateway next-hop <next_hop> esi <esi> detail
                   show l2route evpn default-gateway mac-address <macaddr> detail
                   show l2route evpn default-gateway mac-address <macaddr> esi <esi> detail
                   show l2route evpn default-gateway esi <esi> detail
    """

    schema = {
        'evi': {
            Any(): {
                'eth_tag': {
                    Any(): {
                        'producer': {
                            Any(): {
                                'mac_addr': {
                                    Any(): {
                                        'host_ip': {
                                            Any(): {
                                                'seq_number': int,
                                                'label_2': int,
                                                'esi': str,
                                                'mac_rt_flags': str,
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
                }
            }
        }
    }

# ==============================================
# Parser for 'show l2route evpn default-gateway'
# ==============================================
class ShowL2routeEvpnDGWDetail(ShowL2routeEvpnDGWDetailSchema):
    """ Parser for show l2route evpn default-gateway detail
                   show l2route evpn default-gateway host-ip <ip> detail
                   show l2route evpn default-gateway host-ip <ip> topology <evi-etag> detail
                   show l2route evpn default-gateway host-ip <ip> topology <evi-etag> producer <prod> detail
                   show l2route evpn default-gateway host-ip <ip> topology <evi-etag> producer <prod> next-hop <next_hop> detail
                   show l2route evpn default-gateway host-ip <ip> topology <evi-etag> producer <prod> next-hop <next_hop> mac-address <macaddr> detail
                   show l2route evpn default-gateway host-ip <ip> topology <evi-etag> producer <prod> next-hop <next_hop> mac-address <macaddr> esi <esi> detail
                   show l2route evpn default-gateway host-ip <ip> topology <evi-etag> producer <prod> next-hop <next_hop> esi <esi> detail
                   show l2route evpn default-gateway host-ip <ip> topology <evi-etag> producer <prod> mac-address <macaddr> detail
                   show l2route evpn default-gateway host-ip <ip> topology <evi-etag> producer <prod> mac-address <macaddr> esi <esi> detail
                   show l2route evpn default-gateway host-ip <ip> topology <evi-etag> producer <prod> esi <esi> detail
                   show l2route evpn default-gateway host-ip <ip> topology <evi-etag> next-hop <next_hop> detail
                   show l2route evpn default-gateway host-ip <ip> topology <evi-etag> next-hop <next_hop> mac-address <macaddr> detail
                   show l2route evpn default-gateway host-ip <ip> topology <evi-etag> next-hop <next_hop> mac-address <macaddr> esi <esi> detail
                   show l2route evpn default-gateway host-ip <ip> topology <evi-etag> next-hop <next_hop> esi <esi> detail
                   show l2route evpn default-gateway host-ip <ip> topology <evi-etag> mac-address <macaddr> detail
                   show l2route evpn default-gateway host-ip <ip> topology <evi-etag> <macaddr> esi <esi> detail
                   show l2route evpn default-gateway host-ip <ip> topology <evi-etag> esi <esi> detail
                   show l2route evpn default-gateway host-ip <ip> producer <prod> detail
                   show l2route evpn default-gateway host-ip <ip> producer <prod> next-hop <next_hop> detail
                   show l2route evpn default-gateway host-ip <ip> producer <prod> next-hop <next_hop> mac-address <macaddr> detail
                   show l2route evpn default-gateway host-ip <ip> producer <prod> next-hop <next_hop> mac-address <macaddr> esi <esi> detail
                   show l2route evpn default-gateway host-ip <ip> producer <prod> next-hop <next_hop> esi <esi> detail
                   show l2route evpn default-gateway host-ip <ip> producer <prod> mac-address <macaddr> detail
                   show l2route evpn default-gateway host-ip <ip> producer <prod> mac-address <macaddr> esi <esi> detail
                   show l2route evpn default-gateway host-ip <ip> producer <prod> esi <esi> detail
                   show l2route evpn default-gateway host-ip <ip> next-hop <next_hop> detail
                   show l2route evpn default-gateway host-ip <ip> next-hop <next_hop> mac-address <macaddr> detail
                   show l2route evpn default-gateway host-ip <ip> next-hop <next_hop> mac-address <macaddr> esi <esi> detail
                   show l2route evpn default-gateway host-ip <ip> next-hop <next_hop> esi <esi> detail
                   show l2route evpn default-gateway host-ip <ip> mac-address <macaddr> detail
                   show l2route evpn default-gateway host-ip <ip> mac-address <macaddr> esi <esi> detail
                   show l2route evpn default-gateway host-ip <ip> esi <esi> detail
                   show l2route evpn default-gateway topology <evi> detail
                   show l2route evpn default-gateway topology <evi-etag> producer <prod> detail
                   show l2route evpn default-gateway topology <evi-etag> producer <prod> next-hop <next_hop> detail
                   show l2route evpn default-gateway topology <evi-etag> producer <prod> next-hop <next_hop> mac-address <macaddr> detail
                   show l2route evpn default-gateway topology <evi-etag> producer <prod> next-hop <next_hop> mac-address <macaddr> esi <esi> detail
                   show l2route evpn default-gateway topology <evi-etag> producer <prod> next-hop <next_hop> esi <esi> detail
                   show l2route evpn default-gateway topology <evi-etag> producer <prod> mac-address <macaddr> detail
                   show l2route evpn default-gateway topology <evi-etag> producer <prod> mac-address <macaddr> esi <esi> detail
                   show l2route evpn default-gateway topology <evi-etag> producer <prod> esi <esi> detail
                   show l2route evpn default-gateway topology <evi-etag> next-hop <next_hop> detail
                   show l2route evpn default-gateway topology <evi-etag> next-hop <next_hop> mac-address <macaddr> detail
                   show l2route evpn default-gateway topology <evi-etag> next-hop <next_hop> mac-address <macaddr> esi <esi> detail
                   show l2route evpn default-gateway topology <evi-etag> next-hop <next_hop> esi <esi> detail
                   show l2route evpn default-gateway topology <evi-etag> mac-address <macaddr> detail
                   show l2route evpn default-gateway topology <evi-etag> mac-address <macaddr> esi <esi> detail
                   show l2route evpn default-gateway topology <evi-etag> esi <esi> detail
                   show l2route evpn default-gateway producer <prod> detail
                   show l2route evpn default-gateway producer <prod> next-hop <next_hop> detail
                   show l2route evpn default-gateway producer <prod> next-hop <next_hop> mac-address <macaddr> detail
                   show l2route evpn default-gateway producer <prod> next-hop <next_hop> mac-address <macaddr> esi <esi> detail
                   show l2route evpn default-gateway producer <prod> next-hop <next_hop> esi <esi> detail
                   show l2route evpn default-gateway producer <prod> mac-address <macaddr> detail
                   show l2route evpn default-gateway producer <prod> mac-address <macaddr> esi <esi> detail
                   show l2route evpn default-gateway producer <prod> esi <esi> detail
                   show l2route evpn default-gateway next-hop <next_hop> detail
                   show l2route evpn default-gateway next-hop <next_hop> mac-address <macaddr> detail
                   show l2route evpn default-gateway next-hop <next_hop> mac-address <macaddr> esi <esi> detail
                   show l2route evpn default-gateway next-hop <next_hop> esi <esi> detail
                   show l2route evpn default-gateway mac-address <macaddr> detail
                   show l2route evpn default-gateway mac-address <macaddr> esi <esi> detail
                   show l2route evpn default-gateway esi <esi> detail
    """

    cli_command = [
                   'show l2route evpn default-gateway detail',
                   'show l2route evpn default-gateway host-ip {ip} detail',
                   'show l2route evpn default-gateway host-ip {ip} topology {evi_etag} detail',
                   'show l2route evpn default-gateway host-ip {ip} topology {evi_etag} producer {prod} detail',
                   'show l2route evpn default-gateway host-ip {ip} topology {evi_etag} producer {prod} next-hop {next_hop} detail',
                   'show l2route evpn default-gateway host-ip {ip} topology {evi_etag} producer {prod} next-hop {next_hop} mac-address {macaddr} detail',
                   'show l2route evpn default-gateway host-ip {ip} topology {evi_etag} producer {prod} next-hop {next_hop} mac-address {macaddr} esi {esi} detail',
                   'show l2route evpn default-gateway host-ip {ip} topology {evi_etag} producer {prod} next-hop {next_hop} esi {esi} detail',
                   'show l2route evpn default-gateway host-ip {ip} topology {evi_etag} producer {prod} mac-address {macaddr} detail',
                   'show l2route evpn default-gateway host-ip {ip} topology {evi_etag} producer {prod} mac-address {macaddr} esi {esi} detail',
                   'show l2route evpn default-gateway host-ip {ip} topology {evi_etag} producer {prod} esi {esi} detail',
                   'show l2route evpn default-gateway host-ip {ip} topology {evi_etag} next-hop {next_hop} detail',
                   'show l2route evpn default-gateway host-ip {ip} topology {evi_etag} next-hop {next_hop} mac-address {macaddr} detail',
                   'show l2route evpn default-gateway host-ip {ip} topology {evi_etag} next-hop {next_hop} mac-address {macaddr} esi {esi} detail',
                   'show l2route evpn default-gateway host-ip {ip} topology {evi_etag} next-hop {next_hop} esi {esi} detail',
                   'show l2route evpn default-gateway host-ip {ip} topology {evi_etag} mac-address {macaddr} detail',
                   'show l2route evpn default-gateway host-ip {ip} topology {evi_etag} {macaddr} esi {esi} detail',
                   'show l2route evpn default-gateway host-ip {ip} topology {evi_etag} esi {esi} detail',
                   'show l2route evpn default-gateway host-ip {ip} producer {prod} detail',
                   'show l2route evpn default-gateway host-ip {ip} producer {prod} next-hop {next_hop} detail',
                   'show l2route evpn default-gateway host-ip {ip} producer {prod} next-hop {next_hop} mac-address {macaddr} detail',
                   'show l2route evpn default-gateway host-ip {ip} producer {prod} next-hop {next_hop} mac-address {macaddr} esi {esi} detail',
                   'show l2route evpn default-gateway host-ip {ip} producer {prod} next-hop {next_hop} esi {esi} detail',
                   'show l2route evpn default-gateway host-ip {ip} producer {prod} mac-address {macaddr} detail',
                   'show l2route evpn default-gateway host-ip {ip} producer {prod} mac-address {macaddr} esi {esi} detail',
                   'show l2route evpn default-gateway host-ip {ip} producer {prod} esi {esi} detail',
                   'show l2route evpn default-gateway host-ip {ip} next-hop {next_hop} detail',
                   'show l2route evpn default-gateway host-ip {ip} next-hop {next_hop} mac-address {macaddr} detail',
                   'show l2route evpn default-gateway host-ip {ip} next-hop {next_hop} mac-address {macaddr} esi {esi} detail',
                   'show l2route evpn default-gateway host-ip {ip} next-hop {next_hop} esi {esi} detail',
                   'show l2route evpn default-gateway host-ip {ip} mac-address {macaddr} detail',
                   'show l2route evpn default-gateway host-ip {ip} mac-address {macaddr} esi {esi} detail',
                   'show l2route evpn default-gateway host-ip {ip} esi {esi} detail',
                   'show l2route evpn default-gateway topology {evi_etag} detail',
                   'show l2route evpn default-gateway topology {evi_etag} producer {prod} detail',
                   'show l2route evpn default-gateway topology {evi_etag} producer {prod} next-hop {next_hop} detail',
                   'show l2route evpn default-gateway topology {evi_etag} producer {prod} next-hop {next_hop} mac-address {macaddr} detail',
                   'show l2route evpn default-gateway topology {evi_etag} producer {prod} next-hop {next_hop} mac-address {macaddr} esi {esi} detail',
                   'show l2route evpn default-gateway topology {evi_etag} producer {prod} next-hop {next_hop} esi {esi} detail',
                   'show l2route evpn default-gateway topology {evi_etag} producer {prod} mac-address {macaddr} detail',
                   'show l2route evpn default-gateway topology {evi_etag} producer {prod} mac-address {macaddr} esi {esi} detail',
                   'show l2route evpn default-gateway topology {evi_etag} producer {prod} esi {esi} detail',
                   'show l2route evpn default-gateway topology {evi_etag} next-hop {next_hop} detail',
                   'show l2route evpn default-gateway topology {evi_etag} next-hop {next_hop} mac-address {macaddr} detail',
                   'show l2route evpn default-gateway topology {evi_etag} next-hop {next_hop} mac-address {macaddr} esi {esi} detail',
                   'show l2route evpn default-gateway topology {evi_etag} next-hop {next_hop} esi {esi} detail',
                   'show l2route evpn default-gateway topology {evi_etag} mac-address {macaddr} detail',
                   'show l2route evpn default-gateway topology {evi_etag} mac-address {macaddr} esi {esi} detail',
                   'show l2route evpn default-gateway topology {evi_etag} esi {esi} detail',
                   'show l2route evpn default-gateway producer {prod} detail',
                   'show l2route evpn default-gateway producer {prod} next-hop {next_hop} detail',
                   'show l2route evpn default-gateway producer {prod} next-hop {next_hop} mac-address {macaddr} detail',
                   'show l2route evpn default-gateway producer {prod} next-hop {next_hop} mac-address {macaddr} esi {esi} detail',
                   'show l2route evpn default-gateway producer {prod} next-hop {next_hop} esi {esi} detail',
                   'show l2route evpn default-gateway producer {prod} mac-address {macaddr} detail',
                   'show l2route evpn default-gateway producer {prod} mac-address {macaddr} esi {esi} detail',
                   'show l2route evpn default-gateway producer {prod} esi {esi} detail',
                   'show l2route evpn default-gateway next-hop {next_hop} detail',
                   'show l2route evpn default-gateway next-hop {next_hop} mac-address {macaddr} detail',
                   'show l2route evpn default-gateway next-hop {next_hop} mac-address {macaddr} esi {esi} detail',
                   'show l2route evpn default-gateway next-hop {next_hop} esi {esi} detail',
                   'show l2route evpn default-gateway mac-address {macaddr} detail',
                   'show l2route evpn default-gateway mac-address {macaddr} esi {esi} detail',
                   'show l2route evpn default-gateway esi {esi} detail'
        ]

    def cli (self, output=None, host_ip=None, evi_etag=None, prod=None, next_hop=None, macaddr=None, esi=None):
        if not output:
            cli_command = 'show l2route evpn default-gateway'

            if host_ip:
                cli_command += ' host-ip {ip}'.format(ip=host_ip)
            if evi_etag:
                cli_command += ' topology {evi_etag}'.format(evi_etag=evi_etag)
            if prod:
                cli_command += ' producer {prod}'.format(prod=prod)
            if next_hop:
                cli_command += ' next-hop {next_hop}'.format(next_hop=next_hop)
            if macaddr:
                cli_command += ' mac-address {macaddr}'.format(macaddr=macaddr)
            if esi:
                cli_command += ' esi {esi}'.format(esi=esi)

            cli_command += ' detail'
            out = self.device.execute(cli_command)
        else:
            out = output

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
        p10 = re.compile(r'^[Next Hop\(s\):]*\s*(?P<next_hops>[\w\s.:(),/]+)$')

        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()
            if not line:
                continue

            # EVPN Instance:            2
            m = p1.match(line)
            if m:
                group = m.groupdict()
                evi_list = ret_dict.setdefault('evi', {})
                evi = evi_list.setdefault(int(group['evi']), {})
                continue

            # Ethernet Tag:             0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                etag_list = evi.setdefault('eth_tag', {})
                etag = etag_list.setdefault(int(group['eth_tag']), {})
                continue

            # Producer Name:            BGP
            m = p3.match(line)
            if m:
                group = m.groupdict()
                producer_list = etag.setdefault('producer', {})
                producer = producer_list.setdefault(group['producer'], {})
                continue

            # MAC Address:              0012.0012.0012
            m = p4.match(line)
            if m:
                group = m.groupdict()
                mac_list = producer.setdefault('mac_addr', {})
                mac = mac_list.setdefault( group['mac_addr'], {})
                continue

            # Host IP:                  192.168.12.254
            m = p5.match(line)
            if m:
                group = m.groupdict()
                host_ip_list = mac.setdefault('host_ip' , {})
                route = host_ip_list.setdefault(group['host_ip'], {})
                continue

            # Sequence Number:          0
            m = p6.match(line)
            if m:
                group = m.groupdict()
                route.update({'seq_number': int(group['seq_number'])})
                continue

            # Label 2:                  0
            m = p7.match(line)
            if m:
                group = m.groupdict()
                route.update({'label_2': int(group['label_2'])})
                continue

            # ESI:                      0000.0000.0000.0000.0000
            m = p8.match(line)
            if m:
                group = m.groupdict()
                route.update({'esi': group['esi']})
                continue

            # MAC Route Flags:          BInt(Brm)Dgr
            m = p9.match(line)
            if m:
                group = m.groupdict()
                route.update({'mac_rt_flags': group['mac_rt_flags']})
                continue

            # Next Hop(s):              L:16 2.2.2.1
            m = p10.match(line)
            if m:
                group = m.groupdict()
                route.update({'next_hops': group['next_hops'].split(", ")})
                continue

        return ret_dict

# ====================================
# Schema for 'show l2route evpn peers'
# ====================================
class ShowL2routeEvpnPeersSchema(MetaParser):
    """ Schema for show l2route evpn peers
                   show l2route evpn peers topology <evi-etag>
                   show l2route evpn peers topology <evi-etag> peer-ip <peer_ip>
                   show l2route evpn peers peer-ip <peer_ip>
    """

    schema = {
        'evi': {
            Any(): {
                'eth_tag': {
                    Any(): {
                        'peer_ip': {
                            Any(): {
                                'top_name': str,
                                'num_rtes': int,
                                'up_time': str,
                                'encap': str
                                }
                            }
                        }
                    }
                }
            }
        }

# ====================================
# Parser for 'show l2route evpn peers'
# ====================================
class ShowL2routeEvpnPeers(ShowL2routeEvpnPeersSchema):
    """ Parser for show l2route evpn peers
                   show l2route evpn peers topology <evi-etag>
                   show l2route evpn peers topology <evi-etag> peer-ip <peer_ip>
                   show l2route evpn peers peer-ip <peer_ip>
    """

    cli_command = [
        'show l2route evpn peers',
        'show l2route evpn peers topology {evi_etag}',
        'show l2route evpn peers topology {evi_etag} peer-ip {peer_ip}',
        'show l2route evpn peers peer-ip {peer_ip}'
        ]

    def cli (self, output=None, evi_etag=None, peer_ip= None):
        if not output:
            cli_command = 'show l2route evpn peers'

            if evi_etag:
                cli_command += ' topology {evi_etag}'.format(evi_etag=evi_etag)
            if peer_ip:
                cli_command += ' peer-ip {peer_ip}'.format(peer_ip=peer_ip)

            out = self.device.execute(cli_command)
        else:
            out = output

        # Topo Name   EVI       ETAG         Peer-IP Encap Num Routes    Up Time
        #     BD-12     2          0         3.3.3.1  MPLS          4      2d22h
        #    BD-101     2          0         2.2.2.3 VxLAN          1   00:02:07
        p = re.compile(r'^(?P<top_name>[^\s]+)\s+(?P<evi>\d+)\s+(?P<eth_tag>\d+)\s+'
                        r'(?P<peer_ip>[0-9a-fA-F.:]+)\s+(?P<encap>\w+)\s+(?P<num_rtes>\d+)\s+(?P<up_time>[\w:]+)$')

        ret_dict = {}
        header_found = False

        for line in out.splitlines():
            line = line.strip()
            if not line:
                continue

            m = p.match(line)
            if m:
                group = m.groupdict()

                evi = ret_dict.setdefault('evi', {}).setdefault(int(group['evi']), {})

                etag = evi.setdefault('eth_tag', {}).setdefault(int(group['eth_tag']), {})

                peer_ip = etag.setdefault('peer_ip', {}).setdefault(group['peer_ip'], {})

                peer_ip.update({'top_name': group['top_name'],
                                'num_rtes': int(group['num_rtes']),
                                'up_time': group['up_time'],
                                'encap': group['encap']})

                continue

        return ret_dict


# ====================================
# Schema for 'show l2route evpn peers'
# ====================================
class ShowL2routeEvpnPeersDetailSchema(MetaParser):
    """ Schema for show l2route evpn peers detail
                   show l2route evpn peers topology <evi-etag> detail
                   show l2route evpn peers topology <evi-etag> peer-ip <peer_ip> detail
                   show l2route evpn peers peer-ip <peer_ip> detail
    """

    schema = {
        'evi': {
            Any(): {
                'eth_tag': {
                    Any(): {
                        'peer_ip': {
                            Any(): {
                                'top_name': str,
                                'top_id': str,
                                'up_time': str,
                                'encap': str,
                                'number_of_routes': {
                                    Optional('mac'): int,
                                    Optional('mac_ip'): int,
                                    Optional('imet'): int,
                                    Optional('ead_evi'): int,
                                    Optional('ead_es'): int,
                                    Optional('es'): int
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }

# ====================================
# Parser for 'show l2route evpn peers'
# ====================================
class ShowL2routeEvpnPeersDetail(ShowL2routeEvpnPeersDetailSchema):
    """ Parser for show l2route evpn peers detail
                   show l2route evpn peers topology <evi-etag> detail
                   show l2route evpn peers topology <evi-etag> peer-ip <peer_ip> detail
                   show l2route evpn peers peer-ip <peer_ip> detail
    """

    cli_command = [
        'show l2route evpn peers detail',
        'show l2route evpn peers topology {evi_etag} detail',
        'show l2route evpn peers topology {evi_etag} peer-ip {peer_ip} detail',
        'show l2route evpn peers peer-ip {peer_ip} detail'
        ]

    def cli (self, output=None, evi_etag=None, peer_ip= None):
        if not output:
            cli_command = 'show l2route evpn peers'

            if evi_etag:
                cli_command += ' topology {evi_etag}'.format(evi_etag=evi_etag)
            if peer_ip:
                cli_command += ' peer-ip {peer_ip}'.format(peer_ip=peer_ip)

            cli_command += ' detail'
            out = self.device.execute(cli_command)
        else:
            out = output

        # EVPN Instance:            2
        p1 = re.compile(r'^EVPN Instance:\s+(?P<evi>\d+)$')

        # Ethernet Tag:             0
        p2 = re.compile(r'^Ethernet Tag:\s+(?P<eth_tag>\d+)$')

        # Topology                 BD-12
        p3 = re.compile(r'^Topology:\s+(?P<top_name>[^\s]+)$')

        # Topology ID:              FFFFFFFE00000000
        p4 = re.compile(r'^Topology ID:\s+(?P<top_id>[a-fA-f\d]+)$')

        # Peer IP:                  3.3.3.1
        p5 = re.compile(r'^Peer IP:\s+(?P<peer_ip>[0-9a-fA-F.:]+)$')

        # Encapsulation:            MPLS
        p6 = re.compile(r'^Encapsulation:\s+(?P<encap>\w+)$')

        # Up Time:                  3d02h
        p7 = re.compile(r'^Up Time:\s+(?P<up_time>[\w]+)$')

        # MAC:                    1
        p8 = re.compile(r'^MAC:\s+(?P<mac>\d+)$')

        # MAC-IP:                 1
        p9 = re.compile(r'^MAC-IP:\s+(?P<mac_ip>\d+)$')

        # IMET:                   1
        p10 = re.compile(r'^IMET:\s+(?P<imet>\d+)$')

        # EAD-EVI:                1
        p11 = re.compile(r'^EAD-EVI:\s+(?P<ead_evi>\d+)$')

        # EAD-ES:                 1
        p12 = re.compile(r'^EAD-ES:\s+(?P<ead_es>\d+)$')

        # ES:                     1
        p13 = re.compile(r'^ES:\s+(?P<es>\d+)$')

        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()
            if not line:
                continue

            # EVPN Instance:            2
            m = p1.match(line)
            if m:
                group = m.groupdict()
                evi_list = ret_dict.setdefault('evi', {})
                evi = evi_list.setdefault(int(group['evi']), {})
                continue

            # Ethernet Tag:             0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                etag_list = evi.setdefault('eth_tag', {})
                etag = etag_list.setdefault(int(group['eth_tag']), {})
                continue

            # Topology:                 BD-12
            m = p3.match(line)
            if m:
                group = m.groupdict()
                top_name = group['top_name']
                continue

            # Topology ID:              FFFFFFFE00000000
            m = p4.match(line)
            if m:
                group = m.groupdict()
                top_id = group['top_id']
                continue

            # Peer IP:                  3.3.3.1
            m = p5.match(line)
            if m:
                group = m.groupdict()
                peer_ip_list = etag.setdefault('peer_ip', {})
                peer_ip = peer_ip_list.setdefault(group['peer_ip'], {})
                peer_ip.update({'top_name': top_name,
                                'top_id': top_id})
                continue

            # Encapsulation:            MPLS
            m = p6.match(line)
            if m:
                group = m.groupdict()
                peer_ip.update({'encap': group['encap']})
                continue

            # Up Time:                  3d02h
            m = p7.match(line)
            if m:
                group = m.groupdict()
                peer_ip.update({'up_time': group['up_time']})
                continue

            number_of_routes = peer_ip.setdefault('number_of_routes', {})
            # MAC:                    1
            m = p8.match(line)
            if m:
                group = m.groupdict()
                number_of_routes.update({'mac': int(group['mac'])})
                continue

            # MAC-IP:                 1
            m = p9.match(line)
            if m:
                group = m.groupdict()
                number_of_routes.update({'mac_ip': int(group['mac_ip'])})
                continue

            # IMET:                   1
            m = p10.match(line)
            if m:
                group = m.groupdict()
                number_of_routes.update({'imet': int(group['imet'])})
                continue

            # EAD-EVI:                1
            m = p11.match(line)
            if m:
                group = m.groupdict()
                number_of_routes.update({'ead_evi': int(group['ead_evi'])})
                continue

            # EAD-ES:                 1
            m = p12.match(line)
            if m:
                group = m.groupdict()
                number_of_routes.update({'ead_es': int(group['ead_es'])})
                continue

            # ES:                     1
            m = p13.match(line)
            if m:
                group = m.groupdict()
                number_of_routes.update({'es': int(group['es'])})
                continue

        return ret_dict

# =============================================
# Schema for 'show l2route evpn mac detail'
# =============================================
class ShowL2routeEvpnMacDetailSchema(MetaParser):
    """ Schema for show l2route evpn mac detail
                   show l2route evpn mac esi <esi> detail
                   show l2route evpn mac mac-address <mac_addr> detail
                   show l2route evpn mac mac-address <mac_addr> esi <esi> detail
                   show l2route evpn mac next-hop <next_hop> detail
                   show l2route evpn mac next-hop <next_hop> esi <esi> detail
                   show l2route evpn mac next-hop <next_hop> mac-address <mac_addr> detail
                   show l2route evpn mac next-hop <next_hop> mac-address <mac_addr> esi <esi> detail
                   show l2route evpn mac producer <producer> detail
                   show l2route evpn mac producer <producer> esi <esi> detail
                   show l2route evpn mac producer <producer> mac-address <mac_addr> detail
                   show l2route evpn mac producer <producer> mac-address <mac_addr> esi <esi> detail
                   show l2route evpn mac producer <producer> next-hop <next_hop> detail
                   show l2route evpn mac producer <producer> next-hop <next_hop> esi <esi> detail
                   show l2route evpn mac producer <producer> next-hop <next_hop> mac-address <mac_addr> detail
                   show l2route evpn mac producer <producer> next-hop <next_hop> mac-address <mac_addr> esi <esi> detail
                   show l2route evpn mac topology <evi_etag> detail
                   show l2route evpn mac topology <evi_etag> esi <esi> detail
                   show l2route evpn mac topology <evi_etag> mac-address <mac_addr> detail
                   show l2route evpn mac topology <evi_etag> mac-address <mac_addr> esi <esi> detail
                   show l2route evpn mac topology <evi_etag> next-hop <next_hop> detail
                   show l2route evpn mac topology <evi_etag> next-hop <next_hop> esi <esi> detail
                   show l2route evpn mac topology <evi_etag> next-hop <next_hop> mac-address <mac_addr> detail
                   show l2route evpn mac topology <evi_etag> next-hop <next_hop> mac-address <mac_addr> esi <esi> detail
                   show l2route evpn mac topology <evi_etag> producer <producer> mac-address <mac_addr> detail
                   show l2route evpn mac topology <evi_etag> producer <producer> mac-address <mac_addr> esi <esi> detail
                   show l2route evpn mac topology <evi_etag> producer <producer> next-hop <next_hop> mac-address <mac_addr> esi <esi> detail
    """

    schema = {
        'evi': {
            Any(): {
                'eth_tag': {
                    Any(): {
                        'producer': {
                            Any(): {
                                'mac_addr': {
                                    Any(): {
                                        'no_of_macip_rts': int,
                                        'seq_number': int,
                                        'esi': str,
                                        'flags': str,
                                        Optional('no_of_default_gws'): int,
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
        }
    }

# =============================================
# Parser for 'show l2route evpn mac detail'
# =============================================
class ShowL2routeEvpnMacDetail(ShowL2routeEvpnMacDetailSchema):
    """ Parser for show l2route evpn mac detail
                   show l2route evpn mac esi <esi> detail
                   show l2route evpn mac mac-address <mac_addr> detail
                   show l2route evpn mac mac-address <mac_addr> esi <esi> detail
                   show l2route evpn mac next-hop <next_hop> detail
                   show l2route evpn mac next-hop <next_hop> esi <esi> detail
                   show l2route evpn mac next-hop <next_hop> mac-address <mac_addr> detail
                   show l2route evpn mac next-hop <next_hop> mac-address <mac_addr> esi <esi> detail
                   show l2route evpn mac producer <producer> detail
                   show l2route evpn mac producer <producer> esi <esi> detail
                   show l2route evpn mac producer <producer> mac-address <mac_addr> detail
                   show l2route evpn mac producer <producer> mac-address <mac_addr> esi <esi> detail
                   show l2route evpn mac producer <producer> next-hop <next_hop> detail
                   show l2route evpn mac producer <producer> next-hop <next_hop> esi <esi> detail
                   show l2route evpn mac producer <producer> next-hop <next_hop> mac-address <mac_addr> detail
                   show l2route evpn mac producer <producer> next-hop <next_hop> mac-address <mac_addr> esi <esi> detail
                   show l2route evpn mac topology <evi_etag> detail
                   show l2route evpn mac topology <evi_etag> esi <esi> detail
                   show l2route evpn mac topology <evi_etag> mac-address <mac_addr> detail
                   show l2route evpn mac topology <evi_etag> mac-address <mac_addr> esi <esi> detail
                   show l2route evpn mac topology <evi_etag> next-hop <next_hop> detail
                   show l2route evpn mac topology <evi_etag> next-hop <next_hop> esi <esi> detail
                   show l2route evpn mac topology <evi_etag> next-hop <next_hop> mac-address <mac_addr> detail
                   show l2route evpn mac topology <evi_etag> next-hop <next_hop> mac-address <mac_addr> esi <esi> detail
                   show l2route evpn mac topology <evi_etag> producer <producer> mac-address <mac_addr> detail
                   show l2route evpn mac topology <evi_etag> producer <producer> mac-address <mac_addr> esi <esi> detail
                   show l2route evpn mac topology <evi_etag> producer <producer> next-hop <next_hop> mac-address <mac_addr> esi <esi> detail
    """

    cli_command = [
                   'show l2route evpn mac detail',
                   'show l2route evpn mac esi {esi} detail',
                   'show l2route evpn mac mac-address {mac_addr} detail',
                   'show l2route evpn mac mac-address {mac_addr} esi {esi} detail',
                   'show l2route evpn mac next-hop {next_hop} detail',
                   'show l2route evpn mac next-hop {next_hop} esi {esi} detail',
                   'show l2route evpn mac next-hop {next_hop} mac-address {mac_addr} detail',
                   'show l2route evpn mac next-hop {next_hop} mac-address {mac_addr} esi {esi} detail',
                   'show l2route evpn mac producer {producer} detail',
                   'show l2route evpn mac producer {producer} esi {esi} detail',
                   'show l2route evpn mac producer {producer} mac-address {mac_addr} detail',
                   'show l2route evpn mac producer {producer} mac-address {mac_addr} esi {esi} detail',
                   'show l2route evpn mac producer {producer} next-hop {next_hop} detail',
                   'show l2route evpn mac producer {producer} next-hop {next_hop} esi {esi} detail',
                   'show l2route evpn mac producer {producer} next-hop {next_hop} mac-address {mac_addr} detail',
                   'show l2route evpn mac producer {producer} next-hop {next_hop} mac-address {mac_addr} esi {esi} detail',
                   'show l2route evpn mac topology {evi_etag} detail',
                   'show l2route evpn mac topology {evi_etag} esi {esi} detail',
                   'show l2route evpn mac topology {evi_etag} mac-address {mac_addr} detail',
                   'show l2route evpn mac topology {evi_etag} mac-address {mac_addr} esi {esi} detail',
                   'show l2route evpn mac topology {evi_etag} next-hop {next_hop} detail',
                   'show l2route evpn mac topology {evi_etag} next-hop {next_hop} esi {esi} detail',
                   'show l2route evpn mac topology {evi_etag} next-hop {next_hop} mac-address {mac_addr} detail',
                   'show l2route evpn mac topology {evi_etag} next-hop {next_hop} mac-address {mac_addr} esi {esi} detail',
                   'show l2route evpn mac topology {evi_etag} producer {producer} mac-address {mac_addr} detail',
                   'show l2route evpn mac topology {evi_etag} producer {producer} mac-address {mac_addr} esi {esi} detail',
                   'show l2route evpn mac topology {evi_etag} producer {producer} next-hop {next_hop} mac-address {mac_addr} esi {esi} detail'
    ]

    def cli(self, output=None, esi=None, mac_addr=None, next_hop=None, producer=None, evi_etag=None):
        if not output:
            cli_cmd = 'show l2route evpn mac'
            if evi_etag:
                cli_cmd += ' topology {evi_etag}'.format(evi_etag=evi_etag)
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
        p1 = re.compile(r'^EVPN\s+Instance:\s+(?P<evi>\d+)$')

        # Ethernet Tag:             0
        p2 = re.compile(r'^Ethernet\s+Tag:\s+(?P<eth_tag>\d+)$')

        # Producer Name:            BGP
        p3 = re.compile(r'^Producer\s+Name:\s+(?P<producer>[\w\d]+)$')

        # MAC Address:              0012.0012.0012
        p4 = re.compile(r'^MAC\s+Address:\s+(?P<mac_addr>[0-9a-fA-F\.]+)$')

        # Num of MAC IP Route(s):   2
        p5 = re.compile(r'^[Num of MAC IP Route\(s\):]*\s*(?P<no_of_macip_rts>\d+)$')

        # Sequence Number:          0
        p6 = re.compile(r'^Sequence\s+Number:\s+(?P<seq_number>\d+)$')

        # ESI:                      0000.0000.0000.0000.0000
        p7 = re.compile(r'^ESI:\s+(?P<esi>[0-9a-fA-F\.]+)$')

        # Flags:                    BInt(Brm)Dgr
        p8 = re.compile(r'^Flags:\s+(?P<flags>[\w()]+)$')

        # Num of Default Gateways:  2
        p9 = re.compile(r'^Num\s+of\s+Default\s+Gateways:\s+(?P<no_of_default_gws>\d+)$')

        # Next Hop(s):              L:16 2.2.2.1, L:17 5.5.5.1
        p10 = re.compile(r'^Next\s+Hop\(s\):\s*(?P<next_hop>[\w\d\s.,:()/]+)$')

        parser_dict = {}

        for line in cli_output.splitlines():
            line = line.strip()
            if not line:
                continue

            # EVPN Instance:            2
            m = p1.match(line)
            if m:
                group = m.groupdict()
                evi_dict = parser_dict.setdefault( 'evi', {})
                evis = evi_dict.setdefault( int(group['evi']), {})
                continue

            # Ethernet Tag:             0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                eth_tag_dict = evis.setdefault( 'eth_tag', {})
                eth_tags = eth_tag_dict.setdefault( int(group['eth_tag']), {})
                continue

            # Producer Name:            BGP
            m = p3.match(line)
            if m:
                group = m.groupdict()
                producers_dict = eth_tags.setdefault('producer', {} )
                producers = producers_dict.setdefault( group['producer'], {})
                continue

            # MAC Address:              0012.0012.0012
            m = p4.match(line)
            if m:
                group = m.groupdict()
                mac_addr_dict = producers.setdefault('mac_addr', {})
                mac_addrs = mac_addr_dict.setdefault( group['mac_addr'], {})
                continue

            # Num of MAC IP Route(s):   2
            m = p5.match(line)
            if m:
                group = m.groupdict()
                mac_addrs.update({'no_of_macip_rts': int(group['no_of_macip_rts'])})
                continue

            # Sequence Number:          0
            m = p6.match(line)
            if m:
                group = m.groupdict()
                mac_addrs.update({'seq_number': int(group['seq_number'])})
                continue

            # ESI:                      0000.0000.0000.0000.0000
            m = p7.match(line)
            if m:
                group = m.groupdict()
                mac_addrs.update({'esi': group['esi']})
                continue

            # Flags:                    BInt(Brm)Dgr
            m = p8.match(line)
            if m:
                group = m.groupdict()
                mac_addrs.update({'flags': group['flags']})
                continue

            # Num of Default Gateways:  2
            m = p9.match(line)
            if m:
                group = m.groupdict()
                mac_addrs.update({'no_of_default_gws': int(group['no_of_default_gws'])})
                continue

            # Next Hop(s):              L:16 2.2.2.1
            m = p10.match(line)
            if m:
                group = m.groupdict()
                mac_addrs.update({'next_hops': group['next_hop'].split(", ")})
                continue

        return parser_dict

# =============================================
# Schema for 'show l2route evpn mac'
# =============================================
class ShowL2routeEvpnMacSchema(MetaParser):
    """ Schema for show l2route evpn mac
                   show l2route evpn mac esi <esi>
                   show l2route evpn mac mac-address <mac_addr>
                   show l2route evpn mac mac-address <mac_addr> esi <esi>
                   show l2route evpn mac next-hop <next_hop>
                   show l2route evpn mac next-hop <next_hop> esi <esi>
                   show l2route evpn mac next-hop <next_hop> mac-address <mac_addr>
                   show l2route evpn mac next-hop <next_hop> mac-address <mac_addr> esi <esi>
                   show l2route evpn mac producer <producer>
                   show l2route evpn mac producer <producer> esi <esi>
                   show l2route evpn mac producer <producer> mac-address <mac_addr>
                   show l2route evpn mac producer <producer> mac-address <mac_addr> esi <esi>
                   show l2route evpn mac producer <producer> next-hop <next_hop>
                   show l2route evpn mac producer <producer> next-hop <next_hop> esi <esi>
                   show l2route evpn mac producer <producer> next-hop <next_hop> mac-address <mac_addr>
                   show l2route evpn mac producer <producer> next-hop <next_hop> mac-address <mac_addr> esi <esi>
                   show l2route evpn mac topology <evi_etag>
                   show l2route evpn mac topology <evi_etag> esi <esi>
                   show l2route evpn mac topology <evi_etag> mac-address <mac_addr>
                   show l2route evpn mac topology <evi_etag> mac-address <mac_addr> esi <esi>
                   show l2route evpn mac topology <evi_etag> next-hop <next_hop>
                   show l2route evpn mac topology <evi_etag> next-hop <next_hop> esi <esi>
                   show l2route evpn mac topology <evi_etag> next-hop <next_hop> mac-address <mac_addr>
                   show l2route evpn mac topology <evi_etag> next-hop <next_hop> mac-address <mac_addr> esi <esi>
                   show l2route evpn mac topology <evi_etag> producer <producer> mac-address <mac_addr>
                   show l2route evpn mac topology <evi_etag> producer <producer> mac-address <mac_addr> esi <esi>
                   show l2route evpn mac topology <evi_etag> producer <producer> next-hop <next_hop> mac-address <mac_addr> esi <esi>
    """

    schema = {
        'evi': {
            Any(): {
                'eth_tag': {
                    Any(): {
                        'producer': {
                            Any(): {
                                'mac_addr': {
                                    Any(): {
                                        'seq_number': int,
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
        }
    }

# =============================================
# Parser for 'show l2route evpn mac'
# =============================================
class ShowL2routeEvpnMac(ShowL2routeEvpnMacSchema):
    """ Parser for show l2route evpn mac
                   show l2route evpn mac esi <esi>
                   show l2route evpn mac mac-address <mac_addr>
                   show l2route evpn mac mac-address <mac_addr> esi <esi>
                   show l2route evpn mac next-hop <next_hop>
                   show l2route evpn mac next-hop <next_hop> esi <esi>
                   show l2route evpn mac next-hop <next_hop> mac-address <mac_addr>
                   show l2route evpn mac next-hop <next_hop> mac-address <mac_addr> esi <esi>
                   show l2route evpn mac producer <producer>
                   show l2route evpn mac producer <producer> esi <esi>
                   show l2route evpn mac producer <producer> mac-address <mac_addr>
                   show l2route evpn mac producer <producer> mac-address <mac_addr> esi <esi>
                   show l2route evpn mac producer <producer> next-hop <next_hop>
                   show l2route evpn mac producer <producer> next-hop <next_hop> esi <esi>
                   show l2route evpn mac producer <producer> next-hop <next_hop> mac-address <mac_addr>
                   show l2route evpn mac producer <producer> next-hop <next_hop> mac-address <mac_addr> esi <esi>
                   show l2route evpn mac topology <evi_etag>
                   show l2route evpn mac topology <evi_etag> esi <esi>
                   show l2route evpn mac topology <evi_etag> mac-address <mac_addr>
                   show l2route evpn mac topology <evi_etag> mac-address <mac_addr> esi <esi>
                   show l2route evpn mac topology <evi_etag> next-hop <next_hop>
                   show l2route evpn mac topology <evi_etag> next-hop <next_hop> esi <esi>
                   show l2route evpn mac topology <evi_etag> next-hop <next_hop> mac-address <mac_addr>
                   show l2route evpn mac topology <evi_etag> next-hop <next_hop> mac-address <mac_addr> esi <esi>
                   show l2route evpn mac topology <evi_etag> producer <producer> mac-address <mac_addr>
                   show l2route evpn mac topology <evi_etag> producer <producer> mac-address <mac_addr> esi <esi>
                   show l2route evpn mac topology <evi_etag> producer <producer> next-hop <next_hop> mac-address <mac_addr> esi <esi>
    """

    cli_command = [
                   'show l2route evpn mac',
                   'show l2route evpn mac esi {esi}',
                   'show l2route evpn mac mac-address {mac_addr}',
                   'show l2route evpn mac mac-address {mac_addr} esi {esi}',
                   'show l2route evpn mac next-hop {next_hop}',
                   'show l2route evpn mac next-hop {next_hop} esi {esi}',
                   'show l2route evpn mac next-hop {next_hop} mac-address {mac_addr}',
                   'show l2route evpn mac next-hop {next_hop} mac-address {mac_addr} esi {esi}',
                   'show l2route evpn mac producer {producer}',
                   'show l2route evpn mac producer {producer} esi {esi}',
                   'show l2route evpn mac producer {producer} mac-address {mac_addr}',
                   'show l2route evpn mac producer {producer} mac-address {mac_addr} esi {esi}',
                   'show l2route evpn mac producer {producer} next-hop {next_hop}',
                   'show l2route evpn mac producer {producer} next-hop {next_hop} esi {esi}',
                   'show l2route evpn mac producer {producer} next-hop {next_hop} mac-address {mac_addr}',
                   'show l2route evpn mac producer {producer} next-hop {next_hop} mac-address {mac_addr} esi {esi}',
                   'show l2route evpn mac topology {evi_etag}',
                   'show l2route evpn mac topology {evi_etag} esi {esi}',
                   'show l2route evpn mac topology {evi_etag} mac-address {mac_addr}',
                   'show l2route evpn mac topology {evi_etag} mac-address {mac_addr} esi {esi}',
                   'show l2route evpn mac topology {evi_etag} next-hop {next_hop}',
                   'show l2route evpn mac topology {evi_etag} next-hop {next_hop} esi {esi}',
                   'show l2route evpn mac topology {evi_etag} next-hop {next_hop} mac-address {mac_addr}',
                   'show l2route evpn mac topology {evi_etag} next-hop {next_hop} mac-address {mac_addr} esi {esi}',
                   'show l2route evpn mac topology {evi_etag} producer {producer} mac-address {mac_addr}',
                   'show l2route evpn mac topology {evi_etag} producer {producer} mac-address {mac_addr} esi {esi}',
                   'show l2route evpn mac topology {evi_etag} producer {producer} next-hop {next_hop} mac-address {mac_addr} esi {esi}'
    ]

    def cli(self, output=None, evi_etag=None, producer=None, mac_addr=None, next_hop=None, esi=None):
        if not output:
            cli_cmd = 'show l2route evpn mac'
            if evi_etag:
                cli_cmd += ' topology {evi_etag}'.format(evi_etag=evi_etag)
            if producer:
                cli_cmd += ' producer {producer}'.format(producer=producer)
            if next_hop:
                cli_cmd += ' next-hop {next_hop}'.format(next_hop=next_hop)
            if mac_addr:
                cli_cmd += ' mac-address {mac_addr}'.format(mac_addr=mac_addr)
            if esi:
                cli_cmd += ' esi {esi}'.format(esi=esi)
            cli_output = self.device.execute(cli_cmd)
        else:
            cli_output = output

        # EVI       ETag  Prod    Mac Address                  Next Hop(s) Seq Number
        p1 = re.compile(r'^EVI\s+ETag\s+Prod\s+Mac\s+Address\s+Next\s+Hop\(s\)\s+Seq\s+Number$')

        #1          0 L2VPN 0011.0011.0011                       BD11:0          0
        #1          0 L2VPN aabb.0012.0002                       Gi4:11          0
        #10          0   BGP 000C.000C.000C            V:2002 IP:2.2.2.2          0
        #10          0   BGP 000B.000B.000B             L:101 IP:1.1.1.1          0
        p2 = re.compile(r'^(?P<evi>\d+)\s+(?P<eth_tag>\d+)\s+(?P<producer>[\w\d]+)\s+'
                        r'(?P<mac_addr>[0-9a-fA-F.:]+)\s+(?P<next_hop>[\/\.:\w\d]+\s*[\/\.:\w\d]+)\s+(?P<seq_no>\d+)$')

        #           L:101 IP:1.1.1.1
        p3 = re.compile(r'^(?P<next_hop>[\/\.:\w\d]+\s*[\/\.:\w\d]+)$')

        parser_dict = {}
        header_found = False

        for line in cli_output.splitlines():
            line = line.strip()
            if not line:
                continue

            m = p1.match(line)
            if m:
                header_found = True
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                evi_dict = parser_dict.setdefault('evi', {})
                evis = evi_dict.setdefault(int(group['evi']), {})

                eth_tag_dict = evis.setdefault('eth_tag', {})
                eth_tags = eth_tag_dict.setdefault(int(group['eth_tag']), {})

                producer_dict = eth_tags.setdefault('producer', {})
                producers = producer_dict.setdefault(group['producer'], {})

                mac_addr_dict = producers.setdefault('mac_addr', {})
                mac_addrs = mac_addr_dict.setdefault(group['mac_addr'], {})

                mac_addrs.update({'seq_number': int(group['seq_no'])})
                next_hops = mac_addrs.setdefault('next_hops', [])
                next_hops.append(group['next_hop'])
                continue

            m = p3.match(line)
            if m:
                if next_hops:
                    group = m.groupdict()
                    next_hops.append(group['next_hop'])
                    continue

        if not header_found:
            return({})
        return(parser_dict)