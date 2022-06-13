"""show_tacacs.py
   IOSXR parsers for the following show commands:
     *  show tacacs
"""
# python

# Metaparser
# python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# ==================================================
# Schema for 'show tacacs'
# ==================================================
class ShowTacacsSchema(MetaParser):
    """Schema for show tacacs"""

    schema = {
        'server': {
            Any(): {
                Optional('vrf'): str,
                Optional('server_type'): str,
                'opens': str,
                'closes': str,
                'aborts': str,
                'errors': str,
                'packets_in': str,
                'packets_out': str,
                'status': str,
                'single_connect': str,
                'family': str,
            },
        },
    }


# ==================================================
# Parser for 'show tacacs'
# ==================================================
class ShowTacacs(ShowTacacsSchema):

    cli_command = ['show tacacs']

    def cli(self, output=None):
        if output is None:
            cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        # initial dictionaries
        server_dict = {}
        ret_dict = {}

        # Server: 127.0.0.1/24 vrf=default [private]
        p1 = re.compile(
            r'^Server:\s(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2})\svrf=(?P<vrf>[A-Za-z0-9]+)\s?\[(?P<server_type>\w+)\]$')

        # Server: opens=123309 closes=123309 aborts=592 errors=0
        p1_1 = re.compile(
            r'^Server:\s(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2})\sopens=(?P<opens>\d+)\scloses=(?P<closes>\d+)\saborts=(?P<aborts>\d+)\serrors=(?P<errors>\d+)$')

        # opens=123309 closes=123309 aborts=592 errors=0
        p2 = re.compile(r'^opens=(?P<opens>\d+)\scloses=(?P<closes>\d+)\saborts=(?P<aborts>\d+)\serrors=(?P<errors>\d+)$')

        #  packets in=134136 packets out=134161
        p3 = re.compile(r'^packets\sin=(?P<packets_in>\d+)\spackets\sout=(?P<packets_out>\d+)$')

        # status=up single-connect=false family=IPv4
        p4 = re.compile(
            r'^status=(?P<status>\w+)\ssingle-connect=(?P<single_connect>\w+)\sfamily=(?P<family>\S+)$')

        # IP which is processed right now, will be used as dictionary index
        current_ip = ''

        for line in out.splitlines():
            line = line.strip()

            res = p1.match(line)
            if res:
                if 'server' not in ret_dict:
                    server_dict = ret_dict.setdefault('server', {})

                group = res.groupdict()
                ip = group['ip']
                vrf = group['vrf']
                server_type = group['server_type']

                current_ip = ip

                server_dict[current_ip] = {}
                server_dict[current_ip]['vrf'] = vrf
                server_dict[current_ip]['server_type'] = server_type
                continue

            res = p1_1.match(line)
            if res:
                if 'server' not in ret_dict:
                    server_dict = ret_dict.setdefault('server', {})

                group = res.groupdict()
                ip = group['ip']
                current_ip = ip

                server_dict[current_ip] = {}
                server_dict[current_ip]['opens'] = group['opens']
                server_dict[current_ip]['closes'] = group['closes']
                server_dict[current_ip]['aborts'] = group['aborts']
                server_dict[current_ip]['errors'] = group['errors']
                continue

            res = p2.match(line)
            if res:
                group = res.groupdict()
                server_dict[current_ip]['opens'] = group['opens']
                server_dict[current_ip]['closes'] = group['closes']
                server_dict[current_ip]['aborts'] = group['aborts']
                server_dict[current_ip]['errors'] = group['errors']
                continue

            res = p3.match(line)
            if res:
                group = res.groupdict()
                server_dict[current_ip]['packets_in'] = group['packets_in']
                server_dict[current_ip]['packets_out'] = group['packets_out']
                continue

            res = p4.match(line)
            if res:
                group = res.groupdict()
                server_dict[current_ip]['status'] = group['status']
                server_dict[current_ip]['single_connect'] = group['single_connect']
                server_dict[current_ip]['family'] = group['family']
                continue

        return ret_dict
