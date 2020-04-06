"""ping.py

JunOS parsers for the following show commands:
    * ping {addr}
    * ping {addr} count {count} 
"""
# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (Any, 
        Optional, Use, SchemaTypeError, Schema)

class PingSchema(MetaParser):
    # schema = {
    #     'ping': {
    #         'addr': str,
    #         'data-bytes': str,
    #         'result': [
    #             {
    #                 'bytes': str,
    #                 'from': str,
    #                 'icmp-seq': str,
    #                 'ttl': str,
    #                 'time': str,
    #             }
    #         ],
    #         'ping-statistics': {
    #             'packets-transmitted': str,
    #             'packets-received': str,
    #             'packet-loss': str,
    #             'round-trip': {
    #                 'min': str,
    #                 'avg': str,
    #                 'max': str,
    #                 'stddev': str,
    #             }
    #         }
    #     }
    # }
    def validate_ping_result_list(value):
        # Pass ping result list of dict in value
        if not isinstance(value, list):
            raise SchemaTypeError('ping result is not a list')
        # Create Arp Entry Schema
        ping_result_schema = Schema({
                    'bytes': str,
                    'from': str,
                    'icmp-seq': str,
                    'ttl': str,
                    'time': str,
                })
        # Validate each dictionary in list
        for item in value:
            ping_result_schema.validate(item)
        return value
    
    # Main Schema
    schema = {
        'ping': {
            'addr': str,
            'data-bytes': str,
            'result': Use(validate_ping_result_list),
            'ping-statistics': {
                'packets-transmitted': str,
                'packets-received': str,
                'packet-loss': str,
                'round-trip': {
                    'min': str,
                    'avg': str,
                    'max': str,
                    'stddev': str,
                }
            }
        }
    }

class Ping(PingSchema):

    cli_command = ['ping {addr}',
        'ping {addr} count {count}']

    def cli(self, addr, count=None, output=None):
        
        if not output:
            if count:
                cmd = self.cli_command[1].format(addr=addr, count=count)
            else:
                cmd = self.cli_command[0].format(addr=addr)
            out = self.device.execute(cmd)
        else:
            out = output
        
        ret_dict = {}

        # PING 10.189.5.94 (10.189.5.94): 56 data bytes
        p1 = re.compile(r'^PING +(?P<addr>\S+) +\(\S+\): +'
                r'(?P<data_bytes>\d+) +data +bytes$')

        # 64 bytes from 10.189.5.94: icmp_seq=0 ttl=62 time=2.261 ms
        p2 = re.compile(r'^(?P<bytes>\d+) +bytes +from +(?P<from>\S+): +'
                r'icmp_seq=(?P<icmp_seq>\d+) +ttl=(?P<ttl>\d+) +'
                r'time=(?P<time>\S+) +ms$')

        # 5 packets transmitted, 5 packets received, 0% packet loss
        p3 = re.compile(r'^(?P<packets_transmitted>\d+) +packets +transmitted, +'
                r'(?P<packets_received>\d+) packets +received, +'
                r'(?P<packet_loss>\d+)\% +packet +loss$')
        
        # round-trip min/avg/max/stddev = 1.823/2.175/2.399/0.191 ms
        p4 = re.compile(r'^round-trip +min\/avg\/max\/stddev +\= +'
                r'(?P<min>[\d\.]+)\/(?P<avg>[\d\.]+)\/(?P<max>[\d\.]+)\/'
                r'(?P<stddev>[\d\.]+) +ms$')
        
        for line in out.splitlines():
            line = line.strip()

            # PING 10.189.5.94 (10.189.5.94): 56 data bytes
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ping_dict = ret_dict.setdefault('ping', {})
                ping_dict.update({k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue
            
            # 64 bytes from 10.189.5.94: icmp_seq=0 ttl=62 time=2.261 ms
            m = p2.match(line)
            if m:
                group = m.groupdict()
                result_list = ping_dict.setdefault('result', [])
                result_dict = {}
                result_dict.update({k.replace('_', '-'):v for k, v in group.items() if v is not None})
                result_list.append(result_dict)
                continue
            
            # 5 packets transmitted, 5 packets received, 0% packet loss
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ping_statistics_dict = ping_dict.setdefault('ping-statistics', {})
                ping_statistics_dict.update({k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue
            
            # round-trip min/avg/max/stddev = 1.823/2.175/2.399/0.191 ms
            m = p4.match(line)
            if m:
                group = m.groupdict()
                round_trip_dict = ping_statistics_dict.setdefault('round-trip', {})
                round_trip_dict.update({k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue
        return ret_dict