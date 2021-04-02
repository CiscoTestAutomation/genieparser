"""ping.py

JunOS parsers for the following show commands:
    * ping {addr}
    * ping {addr} count {count}
    * ping mpls rsvp {rsvp}
    * ping {addr} ttl {ttl} count {count} wait {wait}
    * ping {addr} source {source} count {count}
    * ping {addr} source {source} size {size} do-not-fragment count {count}
    * ping {addr} size {size} count {count} do-not-fragment
"""
# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (Any,
        Optional, Use, SchemaTypeError, Schema, ListOf)


class PingSchema(MetaParser):
    """
        schema = {
            'ping': {
                'addrress': str,
                'source': str,
                'data-bytes': int,
                'result': [
                    {
                        'bytes': int,
                        'from': str,
                        'icmp-seq': int,
                        'ttl': int,
                        'hlim': int,
                        'time': str,
                    }
                ],
                'ping-statistics': {
                    'send': str,
                    'received': str,
                    'loss-rate': str,
                    'round-trip': {
                        'min': str,
                        'avg': str,
                        'max': str,
                        'stddev': str,
                    }
                }
            }
        }
    """

    # Main Schema
    schema = {
        'ping': {
            Optional('address'): str,
            Optional('source'): str,
            Optional('data-bytes'): int,
            Optional('result'): ListOf({
                    'bytes': int,
                    'from': str,
                    Optional('icmp-seq'): int,
                    Optional('hlim'): int,
                    Optional('ttl'): int,
                    Optional('time'): str,
                    Optional('message'): str,
                    Optional('mtu'): int,
                }),
            'statistics': {
                'send': int,
                'received': int,
                'loss-rate': int,
                Optional('round-trip'): {
                    'min': str,
                    'avg': str,
                    'max': str,
                    'stddev': str,
                }
            }
        }
    }

class Ping(PingSchema):

    cli_command = [
        'ping {addr}',
        'ping {addr} count {count}',
        'ping {addr} ttl {ttl} count {count} wait {wait}',
        'ping {addr} source {source} count {count}',
        'ping {addr} source {source} size {size} do-not-fragment count {count}',
        'ping {addr} source {source} size {size} count {count} tos {tos} rapid',
        'ping {addr} size {size} count {count} do-not-fragment'
    ]

    def cli(self, addr, count=None, ttl=None,
            wait=None, source=None, size=None,
            tos=None, output=None):

        if not output:
            if addr and count:
                if ttl and wait:
                    cmd = self.cli_command[2].format(
                        addr=addr,
                        count=count,
                        ttl=ttl,
                        wait=wait)
                elif source and size and tos:
                    cmd = self.cli_command[5].format(
                        addr=addr,
                        source=source,
                        size=size,
                        count=count,
                        tos=tos)
                elif source and size:
                    cmd = self.cli_command[4].format(
                        addr=addr,
                        source=source,
                        size=size,
                        count=count,
                    )
                elif source:
                    cmd = self.cli_command[3].format(
                        addr=addr,
                        source=source,
                        count=count)
                elif size:
                    cmd = self.cli_command[6].format(
                        addr=addr,
                        size=size,
                        count=count)
                else:
                    cmd = self.cli_command[1].format(
                        addr=addr,
                        count=count)
            else:
                cmd = self.cli_command[0].format(addr=addr)
            out = self.device.execute(cmd)
        else:
            out = output

        ret_dict = {}

        # PING 10.189.5.94 (10.189.5.94): 56 data bytes
        p1 = re.compile(r'^PING +(?P<address>\S+) +\((?P<source>\S+)\): +'
                r'(?P<data_bytes>\d+) +data +bytes$')

        # PING6(56=40+8+8 bytes) 2001:db8:223c:2c16::1 --> 2001:db8:223c:2c16::2
        p1_1 = re.compile(r'^PING6\((?P<data_bytes>\d+)=\S+ +bytes\) +'
                r'(?P<source>\S+) --> +(?P<address>\S+)$')

        # 64 bytes from 10.189.5.94: icmp_seq=0 ttl=62 time=2.261 ms
        p2 = re.compile(r'^(?P<bytes>\d+)\s+bytes\s+from\s+(?P<from>\S+)'
                r'(:|,)\s+icmp_seq=(?P<icmp_seq>\d+)\s+'
                r'(ttl=(?P<ttl>\d+)|hlim=(?P<hlim>\d+)) +'
                r'time=(?P<time>\S+) +ms$')

        # 36 bytes from 10.136.0.1: frag needed and DF set (MTU 1186)
        # 1240 bytes from 2001:34::1: Packet too big mtu = 1386
        p2_2 = re.compile(r'^(?P<bytes>\d+)\s+bytes\s+from\s+(?P<from>\S+)'
                          r':\s+(?P<message>[\s\w]+)(\(MTU\s|mtu\s=\s)(?P<mtu>\d+)(\))?$')

        # 5 packets transmitted, 5 packets received, 0% packet loss
        # 5 packets transmitted, 0 packets received, 100% packet loss
        p3 = re.compile(r'^(?P<send>\d+) +packets +transmitted, +'
                r'(?P<received>\d+) +packets +received, +'
                r'(?P<loss_rate>\d+)\% +packet +loss$')

        # round-trip min/avg/max/stddev = 1.823/2.175/2.399/0.191 ms
        # round-trip min/avg/max/std-dev = 0.677/98.186/973.514/291.776 ms
        p4 = re.compile(r'^round-trip +min\/avg\/max\/std(\-)?'
                r'dev +\= +(?P<min>[\d\.]+)\/(?P<avg>[\d\.]+)\/'
                r'(?P<max>[\d\.]+)\/(?P<stddev>[\d\.]+) +ms$')

        for line in out.splitlines():
            line = line.strip()

            # PING 10.189.5.94 (10.189.5.94): 56 data bytes
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ping_dict = ret_dict.setdefault('ping', {})
                ping_dict.update({k.replace('_', '-'): (int(v)
                    if v.isdigit() else v) for k, v in group.items() if v is not None})
                continue

            m = p1_1.match(line)
            if m:
                group = m.groupdict()
                ping_dict = ret_dict.setdefault('ping', {})
                ping_dict.update({k.replace('_', '-'): (int(v)
                    if v.isdigit() else v) for k, v in group.items() if v is not None})
                continue

            # 64 bytes from 10.189.5.94: icmp_seq=0 ttl=62 time=2.261 ms

            # 36 bytes from 10.136.0.1: frag needed and DF set (MTU 1186)
            # 1240 bytes from 2001:34::1: Packet too big mtu = 1386
            m = p2.match(line) or p2_2.match(line)
            if m:
                group = m.groupdict()
                result_list = ping_dict.setdefault('result', [])
                result_dict = {}
                result_dict.update({k.replace('_', '-'): (int(v)
                    if v.isdigit() else v) for k, v in group.items() if v is not None})
                result_list.append(result_dict)
                continue

            # 5 packets transmitted, 5 packets received, 0% packet loss
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ping_dict = ret_dict.setdefault('ping', {})
                ping_statistics_dict = ping_dict.setdefault('statistics', {})
                ping_statistics_dict.update({k.replace('_', '-'): (
                    int(v) if v.isdigit() else v) for k, v in group.items() if v is not None})
                continue

            # round-trip min/avg/max/stddev = 1.823/2.175/2.399/0.191 ms
            m = p4.match(line)
            if m:
                group = m.groupdict()
                round_trip_dict = ping_statistics_dict.setdefault('round-trip', {})
                round_trip_dict.update({k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue

        return ret_dict

class PingMplsRsvpSchema(MetaParser):
    schema = {
        'lsping-statistics': {
            'send': int,
            'received': int,
            'loss-rate': int,
        }
    }

class PingMplsRsvp(PingMplsRsvpSchema):

    cli_command = 'ping mpls rsvp {rsvp}'

    def cli(self, rsvp, output=None):

        if not output:
            cmd = self.cli_command.format(rsvp=rsvp)
            out = self.device.execute(cmd)
        else:
            out = output

        ret_dict = {}

        # 5 packets transmitted, 5 packets received, 0% packet loss
        p1 = re.compile(r'^(?P<send>\d+) +packets +transmitted, +'
                r'(?P<received>\d+) packets +received, +'
                r'(?P<loss_rate>\d+)\% +packet +loss$')

        for line in out.splitlines():
            line = line.strip()

            # 5 packets transmitted, 5 packets received, 0% packet loss
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ping_statistics_dict = ret_dict.setdefault('lsping-statistics', {})
                ping_statistics_dict.update({k.replace('_', '-'): (
                    int(v) if v.isdigit() else v) for k, v in group.items() if v is not None})
                continue

        return ret_dict