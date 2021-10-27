"""ping.py

IOSXE parsers for the following show commands:
    * ping {addr}
    * ping {addr} source {source} repeat {count}
    * ping vrf {vrf} {addr}
    * ping mpls ip {addr} {mask} repeat {count} timeout {timeout}
    * ping mpls traffic-eng tunnel {tunnel_id}
    * ping mpls pseudowire <ip> <vc_id>
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
            * ping {addr} source {source} repeat {count}
            * ping vrf {vrf} {addr}
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
                Optional('round_trip'): {
                    'min_ms': int,
                    'avg_ms': int,
                    'max_ms': int,
                }
            }
        }
    }


class Ping(PingSchema):
    """ parser for
        * ping {addr}
        * ping {addr} source {source} repeat {count}
        * ping vrf {vrf} {addr}
    """

    cli_command = [
        'ping {addr}',
        'ping {addr} source {source} repeat {count}',
        'ping vrf {vrf} {addr}'
    ]

    def cli(self,
            addr=None,
            vrf=None,
            count=None,
            source=None,
            size=None,
            ttl=None,
            timeout=None,
            tos=None,
            dscp=None,
            command=None,
            rapid=None,
            do_not_fragment=None,
            validate=None,
            output=None):

        if not output:
            cmd = []
            if addr and vrf:
                cmd.append('ping vrf {vrf} {addr}'.format(vrf=vrf, addr=addr))
            elif addr:
                cmd.append('ping {addr}'.format(addr=addr))
            if source:
                cmd.append('source {source}'.format(source=source))
            if count:
                cmd.append('repeat {count}'.format(count=count))
            if size:
                cmd.append('size {size}'.format(size=size))
            if timeout or timeout==0:
                cmd.append('timeout {timeout}'.format(timeout=timeout))
            if tos:
                cmd.append('tos {tos}'.format(tos=tos))
            if dscp:
                cmd.append('dscp {dscp}'.format(dscp=dscp))
            if do_not_fragment:
                cmd.append('df-bit')
            if validate:
                cmd.append('validate')
            cmd = ' '.join(cmd)
            if command:
                cmd = command
            out = self.device.execute(cmd)
        else:
            out = output

        ret_dict = {}
        result_per_line = []
        # Sending 10, 100-byte ICMP Echos to 10.229.1.1, timeout is 2 seconds:
        p1 = re.compile(r'Sending +(?P<repeat>\d+), +(?P<data_bytes>\d+)-byte +ICMP +Echos +to +(?P<address>[\S\s]+), +timeout +is +(?P<timeout>\d+) +seconds:')

        #Packet sent with a source address of 10.229.1.2
        p2 = re.compile(
            r'Packet +sent +with +a +source +address +of +(?P<source>[\S\s]+)')

        # !!!!!!!
        # !.UQM?&
        p3 = re.compile(r'[!\.UQM\?&]+')

        # Success rate is 100 percent (100/100), round-trip min/avg/max = 1/2/14 ms
        # Success rate is 0 percent (0/10)
        p4 = re.compile(
            r'Success +rate +is +(?P<success_percent>\d+) +percent +\((?P<received>\d+)\/(?P<send>\d+)\)(, +round-trip +min/avg/max *= *(?P<min>\d+)/(?P<max>\d+)/(?P<avg>\d+) +(?P<unit>\w+))?'
        )

        ping_dict = {}
        for line in out.splitlines():
            line = line.strip()

            # Sending 100, 100-byte ICMP Echos to 10.4.1.1, timeout is 2 seconds:
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ping_dict = ret_dict.setdefault('ping', {})
                ping_dict.update({
                    'repeat': int(group['repeat']),
                    'data_bytes': int(group['data_bytes']),
                    'address': group['address'],
                    'timeout_secs': int(group['timeout'])
                })
                continue
            # Packet sent with a source address of 10.229.1.2
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ping_dict.update({'source': group['source']})
                continue

            # !!!!!!
            m = p3.match(line)
            if m:
                group = m.groupdict()
                result_per_line.append(line)
                ping_dict.update({'result_per_line': result_per_line})


            # Sending 10, 100-byte ICMP Echos to 10.229.1.1, timeout is 2 seconds:
            m = p4.match(line)
            if m:
                group = m.groupdict()
                stat_dict = ping_dict.setdefault('statistics', {})
                stat_dict.update({
                    'success_rate_percent':
                    float(group['success_percent']),
                    'received':
                    int(group['received']),
                    'send':
                    int(group['send'])
                })

                if 'min' in group and group['min'] != None:
                    round_dict = stat_dict.setdefault('round_trip', {})

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


class PingMplsSchema(MetaParser):
    """ Schema for
            * ping mpls ip {addr} {mask} repeat {count} timeout {timeout}
            * ping mpls traffic-eng tunnel {tunnel_id}
    """

    schema = {
        'ping': {
            'address': str,
            'data-bytes': int,
            'interval': int,
            Optional('repeat'): int,
            Optional('timeout-secs'): int,
            'statistics': {
                'sent': int,
                'received': int,
                'success-rate-percent': float,
                'elapsed-time': float,
                Optional('round-trip'): {
                    'min-ms': int,
                    'avg-ms': int,
                    'max-ms': int,
                }
            }
        }
    }


class PingMpls(PingMplsSchema):
    """ parser for
        * ping mpls ip {addr} {mask} repeat {count} timeout {timeout}
    """

    cli_command = [
        'ping mpls ip {addr} {mask} repeat {count}',
        'ping mpls traffic-eng tunnel {tunnel_id}',
        'ping mpls pseudowire {addr} {vc_id}'
        
    ]

    def cli(self,
            addr=None,
            count=None,
            mask=None,
            timeout=None,
            command=None,
            tunnel_id=None,
            vc_id=None,
            output=None):

        if not output:
            if not tunnel_id and not vc_id:
                cmd = []
                if mask:
                    cmd.append('ping mpls ip {addr} {mask}'.format(addr=addr,mask=mask))
                if count:
                    cmd.append('repeat {count}'.format(count=count))
                if timeout:
                    cmd.append('timeout {timeout}'.format(timeout=timeout))
                cmd = ' '.join(cmd)
                if command:
                    cmd = command
            elif vc_id and addr:
                cmd = "ping mpls pseudowire {addr} {vc_id}".format(addr=addr, vc_id=vc_id)          
            else:
                cmd = "ping mpls traffic-eng tunnel {tunnel_id}".format(tunnel_id=tunnel_id)
            out = self.device.execute(cmd)
        else:
            out = output
        ret_dict = {}
        #Sending 5, 72-byte MPLS Echos to 4.4.4.4/32,
        p1 = re.compile(r'Sending +(?P<repeat>\d+), +(?P<data_bytes>\d+)-byte +MPLS +Echos +to +(?P<address>[\S\s]+),')

        #timeout is 2 seconds, send interval is 0 msec:
        p2 = re.compile(r'timeout +is +(?P<timeout>\d+) +seconds\, +send +interval +is +(?P<interval>\d+) msec\:')

        #Success rate is 100 percent (5/5), round-trip min/avg/max = 1/173/656 ms
        p3 = re.compile(
            r'Success +rate +is +(?P<success_percent>\d+) +percent +\((?P<received>\d+)\/(?P<sent>\d+)\)(, +round-trip +min/avg/max *= *(?P<min>\d+)/(?P<max>\d+)/(?P<avg>\d+) +(?P<unit>\w+))?'
        )

        #Total Time Elapsed 869 ms
        p4 = re.compile(r'Total +Time +Elapsed +(?P<elapsed_time>\d+) ms')
        for line in out.splitlines():
            line = line.strip()
            m1 = p1.match(line)
            if m1:
                group = m1.groupdict()
                ping_dict = ret_dict.setdefault('ping', {})
                ping_dict.update({
                    'repeat': int(group['repeat']),
                    'data-bytes': int(group['data_bytes']),
                    'address': group['address']
                })
            m2 = p2.match(line)
            if m2:
                group = m2.groupdict()
                ping_dict.update({'timeout-secs': int(group['timeout']), 'interval': int(group['interval'])})
            m3 = p3.match(line)
            if m3:
                group = m3.groupdict()
                stat_dict = ping_dict.setdefault('statistics', {})
                stat_dict.update({
                    'success-rate-percent':
                        float(group['success_percent']),
                    'received':
                        int(group['received']),
                    'sent':
                        int(group['sent'])
                })

                if 'min' in group and group['min'] != None:
                    round_dict = stat_dict.setdefault('round-trip', {})

                    min_ms = int(group['min'])
                    max_ms = int(group['max'])
                    avg_ms = int(group['avg'])

                    if group['unit'] == "s":
                        min_ms *= 1000
                        max_ms *= 1000
                        avg_ms *= 1000

                    round_dict.update({
                        'min-ms': min_ms,
                        'max-ms': max_ms,
                        'avg-ms': avg_ms
                    })
            m4 = p4.match(line)
            if m4:
                group = m4.groupdict()
                stat_dict.update({'elapsed-time':  (float(group['elapsed_time']))})
        return ret_dict
