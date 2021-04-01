"""traceroute.py

JunOS parsers for the following command:
    * traceroute {ipaddress} no-resolve
    * traceroute {ipaddress} source {ipaddress2} no-resolve
"""
# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from pyats.utils.exceptions import SchemaError
from genie.metaparser.util.schemaengine import (Any,
        Optional, Use, Schema, ListOf)


class TracerouteNoResolveSchema(MetaParser):
    """ Schema for:
                * traceroute {ipaddress} no-resolve
                * traceroute {ipaddress} source {ipaddress2} no-resolve
    """
    """schema = {
        "traceroute": {
            "to": {
                "domain": str,
                "address": str
            },
            "max-hops": str,
            "packet-size": str,
            "hops": [
                        {
                            "hop-number": str,
                            Optional("router-name"): str,
                            "address": str,
                            "round-trip-time": str
                        }
            ]
        }
    }
    """

    # Main Schema
    schema = {
        "traceroute": {
            "to": {
                "domain": str,
                "address": str
            },
            "max-hops": str,
            "packet-size": str,
            Optional("hops"): ListOf({
                "hop-number": str,
                Optional("router-name"): str,
                "address": str,
                "round-trip-time": str
            })
        }
    }

class TracerouteNoResolve(TracerouteNoResolveSchema):
    """ Parser for:
            * traceroute {ipaddress} no-resolve
            * traceroute {ipaddress} source {ipaddress2} no-resolve
    """
    cli_command = ['traceroute {addr} no-resolve',
                    'traceroute {addr} source {addr2} no-resolve']

    def cli(self, addr, addr2=None, output=None):
        if addr2:
            cmd = self.cli_command[1].format(addr=addr, addr2=addr2)
        else:
            cmd = self.cli_command[0].format(addr=addr)

        if not output:
            out = self.device.execute(cmd)
        else:
            out = output

        ret_dict = {}

        # traceroute to 10.135.0.2 (10.135.0.2) 30 hops max 52 byte packets
        # traceroute6 to 2001::2 (2001::2) from 2001::1, 64 hops max, 12 byte packets
        p1 = re.compile(r'^traceroute(6)? +to +(?P<domain>\S+) +\((?P<address>\S+)\)'
                        r'( +from +(?P<source>\S+))?, +(?P<max_hops>\S+) +hops +max, '
                        r'+(?P<packet_size>\S+) +byte +packets$')

        #  1  10.135.0.2  1.792 ms  1.142 ms  0.831 ms
        p2 = re.compile(r'^(?P<hop_number>\S+) +( +(?P<router_name>\S+))? +'
                        r'(?P<address>\S+) +(?P<round_trip_time>\S+ +ms +\S+ +ms +\S+ +ms)$')

        for line in out.splitlines():
            line = line.strip()

            # traceroute to 10.135.0.2 (10.135.0.2) 30 hops max 52 byte packets
            m = p1.match(line)

            if m:
                group = m.groupdict()
                traceroute_dict = ret_dict.setdefault('traceroute', {})
                to_dict = traceroute_dict.setdefault('to', {})
                to_dict['domain'] = group['domain']
                to_dict['address'] = group['address']
                traceroute_dict['max-hops'] = group['max_hops']
                traceroute_dict['packet-size'] = group['packet_size']
                continue

            #  1  10.135.0.2  1.792 ms  1.142 ms  0.831 ms
            m = p2.match(line)
            if m:
                group = m.groupdict()
                hops_list = traceroute_dict.setdefault('hops', [])
                hop_dict = {}
                hop_dict.update({k.replace('_', '-'):
                                                 v for k, v in group.items() if v is not None})
                hops_list.append(hop_dict)
                continue

        return ret_dict
