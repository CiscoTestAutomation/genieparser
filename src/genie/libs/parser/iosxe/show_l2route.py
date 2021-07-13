''' show_l2route_evpn_mac.py

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
                cli_cmd += ' producer'.format(producer=producer)
            if mac_addr:
                cli_cmd += ' mac-address'.format(mac_addr=mac_addr)
            if esi:
                cli_cmd += ' esi'.format(esi=esi)
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
