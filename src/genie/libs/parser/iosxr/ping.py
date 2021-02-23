"""ping.py

IOSXR parsers for the following show commands:
    * ping {addr} source {source} repeat {count}
"""
# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (Any,
        Optional, Use, SchemaTypeError, Schema)

class PingSchema(MetaParser):
    """ Schema for
            * ping {addr} source {source} repeat {count}
    """

    schema = {
        'ping': {
            'address': str,
            'data_bytes': int,
            Optional('repeat'): int,
            Optional('timeout_secs'): int,
            Optional('source'): str,
            Optional('result_per_line'): list,
            'statistics': {
                'send': int,
                'received': int,
                'success_rate_percent': float,
                Optional('round-trip'): {
                    'min_ms': int,
                    'avg_ms': int,
                    'max_ms': int,
                }
            }
        }
    }

class Ping(PingSchema):

    """ parser for
        * ping {addr} source {source} repeat {count}
    """

    cli_command = [
        'ping {addr} source {source} repeat {count}',
    ]

    def cli(self, addr, count=None, source=None, output=None):

        if not output:
            out = self.device.execute(self.cli_command[0].format(addr=addr, source=source, count=count))
        else:
            out = output

        ret_dict = {}
        result_per_line = []

        # Sending 100, 100-byte ICMP Echos to 31.1.1.1, timeout is 2 seconds:
        p1 = re.compile(r'Sending +(?P<repeat>\d+), +(?P<data_bytes>\d+)-byte'
                        r' +ICMP +Echos +to +(?P<address>[\S\s]+), +timeout'
                        r' +is +(?P<timeout>\d+) +seconds:')

        # !!!!!!!
        p2 = re.compile(r'!+')

        # Success rate is 100 percent (100/100), round-trip min/avg/max = 1/2/14 ms
        p3 = re.compile(r'Success +rate +is +(?P<success_percent>\d+) +percent'
                        r' +\((?P<received>\d+)\/(?P<send>\d+)\),'
                        r' +round-trip +min/avg/max *= *(?P<min>\d+)/(?P<max>\d+)/(?P<avg>\d+) +(?P<unit>\w+)')

        for line in out.splitlines():
            line = line.strip()

            # Sending 100, 100-byte ICMP Echos to 31.1.1.1, timeout is 2 seconds:
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ping_dict = ret_dict.setdefault('ping', {})
                ping_dict.update({'repeat': int(group['repeat']),
                                  'data_bytes':int(group['data_bytes']),
                                  'address': group['address'],
                                  'timeout_secs': int(group['timeout'])})

                continue

            # !!!!!!
            m = p2.match(line)
            if m:
                group = m.groupdict()
                result_per_line.append(line)
                ping_dict.update({'result_per_line': result_per_line})

            # Success rate is 100 percent (100/100), round-trip min/avg/max = 1/2/14 ms
            m = p3.match(line)
            if m:
                group = m.groupdict()
                stat_dict = ping_dict.setdefault('statistics', {})
                stat_dict.update({'success_rate_percent': float(group['success_percent']),
                                  'received':int(group['received']),
                                  'send': int(group['send'])})

                round_dict = stat_dict.setdefault('round-trip', {})

                min_ms = int(group['min'])
                max_ms = int(group['max'])
                avg_ms = int(group['avg'])

                if group['unit'] == "s":
                    min_ms *= 1000
                    max_ms *= 1000
                    avg_ms *= 1000

                round_dict.update({
                        'min_ms': min_ms,
                        'max_ms': max_ms,
                        'avg_ms': avg_ms
                })

                continue

        return ret_dict
