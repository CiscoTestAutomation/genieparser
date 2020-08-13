"""traceroute.py

JunOS parsers for the following command:
    * traceroute {ipaddress} no-resolve
"""
# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (Any,
        Optional, Use, SchemaTypeError, Schema)

class TracerouteNoResolveSchema(MetaParser):
    """ Schema for:
                * traceroute {ipaddress} no-resolve
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

    def validate_hops_list(value):
        # Pass hops list of dict in value
        if not isinstance(value, list):
            raise SchemaTypeError('hops is not a list')
        # Create hop Schema
        hop_schema = Schema({
                       "hop-number": str,
                       Optional("router-name"): str,
                       "address": str,
                       "round-trip-time": str
        })
        # Validate each dictionary in list
        for item in value:
            hop_schema.validate(item)
        return value

    # Main Schema
    schema = {
        "traceroute": {
            "to": {
                "domain": str,
                "address": str
            },
            "max-hops": str,
            "packet-size": str,
            Optional("hops"): Use(validate_hops_list)
        }
    }

class TracerouteNoResolve(TracerouteNoResolveSchema):
    """ Parser for:
            * traceroute {ipaddress} no-resolve
    """
    cli_command = 'traceroute {addr} no-resolve'

    def cli(self, addr, output=None):
        cmd = self.cli_command.format(addr=addr)
        if not output:
            out = self.device.execute(cmd)
        else:
            out = output

        ret_dict = {}

        # traceroute to 10.135.0.2 (10.135.0.2) 30 hops max 52 byte packets
        p1 = re.compile(r'^traceroute +to +(?P<domain>\S+) +\((?P<address>\S+)\), +'
                        r'(?P<max_hops>\S+) +hops +max, +(?P<packet_size>\S+) +byte +packets$')

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
