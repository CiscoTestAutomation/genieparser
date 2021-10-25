"""ping.py

AIREOS parsers for the following commands:
    * ping {addr}
    * ping {addr} {interface-name}
    * ping {addr} {repeat count}
    * ping {addr} {repeat count} {packet size}
    * ping {addr} {interface-name} {repeat count} {packet size}
"""
# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (Any,
        Optional, Use, SchemaTypeError, Schema)

class PingSchema(MetaParser):
    """ Schema for
        * ping {addr}
        * ping {addr} {interface-name}
        * ping {addr} {repeat count}
        * ping {addr} {repeat count} {packet size}
        * ping {addr} {interface-name} {repeat count} {packet size}
    """

    schema = {
        'ping': {
            'address': str,
            'repeat': int,
            'statistics': {
                'send': int,
                'received': int,
                Optional('packet_size'): int,
            }
        }
    }


class Ping(PingSchema):
    """ Parser for
        * ping {addr}
        * ping {addr} {interface-name}
        * ping {addr} {repeat count}
        * ping {addr} {repeat count} {packet size}
        * ping {addr} {interface-name} {repeat count} {packet size}
    """

    cli_command = [
        'ping {addr}',
        'ping {addr} {intf_name}',
        'ping {addr} {count}',
        'ping {addr} {count} {size}',
        'ping {addr} {intf_name} {count} {size}'
    ]

    def cli(self,
            addr=None,
            intf_name=None,
            count=None,
            size=None,
            output=None):

        if not output:
            cmd = []
            if addr:
                cmd.append('{addr}'.format(addr=addr))
            if intf_name:
                cmd.append('{intf_name}'.format(intf_name=intf_name))
            if count:
                cmd.append('{count}'.format(count=count))
            if size:
                cmd.append('{size}'.format(size=size))     

            cmd = "ping " + ' '.join(cmd)
            out = self.device.execute(cmd)
        else:
            out = output
        
        ret_dict = {}

        # Send count=10, Receive count=10 from 10.25.10.1, Packet size = 2000
        # Send count=10, Receive count=10 from 10.25.10.1, Packet size = 100
        # Send count=10, Receive count=10 from 10.25.10.1, Packet size = 84
        # Send count=3, Receive count=3 from 10.25.10.1

        p1 = re.compile(r'Send count=+(?P<send_count>\d+), Receive ' \
                        r'count=+(?P<rec_count>\d+) +from ' \
                        r'+(?P<addr>\d+\.\d+\.\d+\.\d+)(, Packet +size = ' \
                        r'+(?P<packet_size>\d+))?')
        
        ping_dict = {}
        stat_dict = {}
        
        for line in out.splitlines():
            line = line.strip()

            # Send count=10, Receive count=10 from 10.25.10.1, Packet size = 2000
            # Send count=10, Receive count=10 from 10.25.10.1, Packet size = 100
            # Send count=10, Receive count=10 from 10.25.10.1, Packet size = 84
            # Send count=3, Receive count=3 from 10.25.10.1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ping_dict = ret_dict.setdefault('ping', {})
                stat_dict = ping_dict.setdefault('statistics', {})
                ping_dict.update({
                    'address': str(group['addr']),
                    'repeat': int(group['send_count'])
                })
                stat_dict.update({
                    'send': int(group['send_count']),
                    'received': int(group['rec_count'])
                })
                if group['packet_size']:
                    stat_dict.update ({'packet_size': int(group['packet_size'])})
                
                continue

        return ret_dict