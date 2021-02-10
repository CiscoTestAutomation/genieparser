"""ping.py

NXOS parsers for the following show commands:
    * ping {addr}
    * ping {addr} count {count}
    * ping {addr} source {source}
    * ping {addr} packet-size {size}
    * ping {addr} timeout {timeout}
    * ping {addr} source {source} timeout {timeout}
    * ping {addr} timeout {timeout} source {source}
    * ping {addr} packet-size {size} timeout {timeout}
    * ping {addr} timeout {timeout} packet-size {size}
    * ping {addr} count {count} source {source}
    * ping {addr} source {source} count {count}
    * ping {addr} source {source} packet-size {size}
    * ping {addr} packet-size {size} source {source}
    * ping {addr} count {count} timeout {timeout}
    * ping {addr} timeout {timeout} count {count}
    * ping {addr} count {count} packet-size {size}
    * ping {addr} packet-size {size} count {count}
    * ping {addr} count {count} packet-size {size} timeout {timeout}
    * ping {addr} count {count} timeout {timeout} packet-size {size}
    * ping {addr} packet-size {size} count {count} timeout {timeout}
    * ping {addr} packet-size {size} timeout {timeout} count {count}
    * ping {addr} timeout {timeout} count {count} packet-size {size}
    * ping {addr} timeout {timeout} packet-size {size} count {count}
    * ping {addr} count {count} source {source} timeout {timeout}
    * ping {addr} count {count} timeout {timeout} source {source}
    * ping {addr} source {source} count {count} timeout {timeout}
    * ping {addr} source {source} timeout {timeout} count {count}
    * ping {addr} timeout {timeout} count {count} source {source}
    * ping {addr} timeout {timeout} source {source} count {count}
    * ping {addr} count {count} source {source} packet-size {size}
    * ping {addr} count {count} packet-size {size} source {source}
    * ping {addr} source {source} count {count} packet-size {size}
    * ping {addr} source {source} packet-size {size} count {count}
    * ping {addr} packet-size {size} count {count} source {source}
    * ping {addr} packet-size {size} source {source} count {count}
    * ping {addr} source {source} packet-size {size} timeout {timeout}
    * ping {addr} source {source} timeout {timeout} packet-size {size}
    * ping {addr} packet-size {size} source {source} timeout {timeout}
    * ping {addr} packet-size {size} timeout {timeout} source {source}
    * ping {addr} timeout {timeout} source {source} packet-size {size}
    * ping {addr} timeout {timeout} packet-size {size} source {source}
    * ping {addr} source {source} count {count} packet-size {size} timeout {timeout}
    * ping {addr} source {source} count {count} timeout {timeout} packet-size {size}
    * ping {addr} source {source} packet-size {size} count {count} timeout {timeout}
    * ping {addr} source {source} packet-size {size} timeout {timeout} count {count}
    * ping {addr} source {source} timeout {timeout} count {count} packet-size {size}
    * ping {addr} source {source} timeout {timeout} packet-size {size} count {count}
    * ping {addr} packet-size {size} count {count} source {source} timeout {timeout}
    * ping {addr} packet-size {size} count {count} timeout {timeout} source {source}
    * ping {addr} packet-size {size} source {source} count {count} timeout {timeout}
    * ping {addr} packet-size {size} source {source} timeout {timeout} count {count}
    * ping {addr} packet-size {size} timeout {timeout} count {count} source {source}
    * ping {addr} packet-size {size} timeout {timeout} source {source} count {count}
    * ping {addr} timeout {timeout} count {count} source {source} packet-size {size}
    * ping {addr} timeout {timeout} count {count} packet-size {size} source {source}
    * ping {addr} timeout {timeout} source {source} count {count} packet-size {size}
    * ping {addr} timeout {timeout} source {source} packet-size {size} count {count}
    * ping {addr} timeout {timeout} packet-size {size} count {count} source {source}
    * ping {addr} timeout {timeout} packet-size {size} source {source} count {count}
    * ping {addr} count {count} source {source} packet-size {size} timeout {timeout}
    * ping {addr} count {count} source {source} timeout {timeout} packet-size {size}
    * ping {addr} count {count} packet-size {size} source {source} timeout {timeout}
    * ping {addr} count {count} packet-size {size} timeout {timeout} source {source}
    * ping {addr} count {count} timeout {timeout} source {source} packet-size {size}
    * ping {addr} count {count} timeout {timeout} packet-size {size} source {source}
    * ping vrf {vrf} {addr}
    * ping vrf {vrf} {addr} count {count}
    * ping vrf {vrf} {addr} source {source}
    * ping vrf {vrf} {addr} packet-size {size}
    * ping vrf {vrf} {addr} timeout {timeout}
    * ping vrf {vrf} {addr} source {source} timeout {timeout}
    * ping vrf {vrf} {addr} timeout {timeout} source {source}
    * ping vrf {vrf} {addr} packet-size {size} timeout {timeout}
    * ping vrf {vrf} {addr} timeout {timeout} packet-size {size}
    * ping vrf {vrf} {addr} count {count} source {source}
    * ping vrf {vrf} {addr} source {source} count {count}
    * ping vrf {vrf} {addr} source {source} packet-size {size}
    * ping vrf {vrf} {addr} packet-size {size} source {source}
    * ping vrf {vrf} {addr} count {count} timeout {timeout}
    * ping vrf {vrf} {addr} timeout {timeout} count {count}
    * ping vrf {vrf} {addr} count {count} packet-size {size}
    * ping vrf {vrf} {addr} packet-size {size} count {count}
    * ping vrf {vrf} {addr} count {count} packet-size {size} timeout {timeout}
    * ping vrf {vrf} {addr} count {count} timeout {timeout} packet-size {size}
    * ping vrf {vrf} {addr} packet-size {size} count {count} timeout {timeout}
    * ping vrf {vrf} {addr} packet-size {size} timeout {timeout} count {count}
    * ping vrf {vrf} {addr} timeout {timeout} count {count} packet-size {size}
    * ping vrf {vrf} {addr} timeout {timeout} packet-size {size} count {count}
    * ping vrf {vrf} {addr} count {count} source {source} timeout {timeout}
    * ping vrf {vrf} {addr} count {count} timeout {timeout} source {source}
    * ping vrf {vrf} {addr} source {source} count {count} timeout {timeout}
    * ping vrf {vrf} {addr} source {source} timeout {timeout} count {count}
    * ping vrf {vrf} {addr} timeout {timeout} count {count} source {source}
    * ping vrf {vrf} {addr} timeout {timeout} source {source} count {count}
    * ping vrf {vrf} {addr} count {count} source {source} packet-size {size}
    * ping vrf {vrf} {addr} count {count} packet-size {size} source {source}
    * ping vrf {vrf} {addr} source {source} count {count} packet-size {size}
    * ping vrf {vrf} {addr} source {source} packet-size {size} count {count}
    * ping vrf {vrf} {addr} packet-size {size} count {count} source {source}
    * ping vrf {vrf} {addr} packet-size {size} source {source} count {count}
    * ping vrf {vrf} {addr} source {source} packet-size {size} timeout {timeout}
    * ping vrf {vrf} {addr} source {source} timeout {timeout} packet-size {size}
    * ping vrf {vrf} {addr} packet-size {size} source {source} timeout {timeout}
    * ping vrf {vrf} {addr} packet-size {size} timeout {timeout} source {source}
    * ping vrf {vrf} {addr} timeout {timeout} source {source} packet-size {size}
    * ping vrf {vrf} {addr} timeout {timeout} packet-size {size} source {source}
    * ping vrf {vrf} {addr} source {source} count {count} packet-size {size} timeout {timeout}
    * ping vrf {vrf} {addr} source {source} count {count} timeout {timeout} packet-size {size}
    * ping vrf {vrf} {addr} source {source} packet-size {size} count {count} timeout {timeout}
    * ping vrf {vrf} {addr} source {source} packet-size {size} timeout {timeout} count {count}
    * ping vrf {vrf} {addr} source {source} timeout {timeout} count {count} packet-size {size}
    * ping vrf {vrf} {addr} source {source} timeout {timeout} packet-size {size} count {count}
    * ping vrf {vrf} {addr} packet-size {size} count {count} source {source} timeout {timeout}
    * ping vrf {vrf} {addr} packet-size {size} count {count} timeout {timeout} source {source}
    * ping vrf {vrf} {addr} packet-size {size} source {source} count {count} timeout {timeout}
    * ping vrf {vrf} {addr} packet-size {size} source {source} timeout {timeout} count {count}
    * ping vrf {vrf} {addr} packet-size {size} timeout {timeout} count {count} source {source}
    * ping vrf {vrf} {addr} packet-size {size} timeout {timeout} source {source} count {count}
    * ping vrf {vrf} {addr} timeout {timeout} count {count} source {source} packet-size {size}
    * ping vrf {vrf} {addr} timeout {timeout} count {count} packet-size {size} source {source}
    * ping vrf {vrf} {addr} timeout {timeout} source {source} count {count} packet-size {size}
    * ping vrf {vrf} {addr} timeout {timeout} source {source} packet-size {size} count {count}
    * ping vrf {vrf} {addr} timeout {timeout} packet-size {size} count {count} source {source}
    * ping vrf {vrf} {addr} timeout {timeout} packet-size {size} source {source} count {count}
    * ping vrf {vrf} {addr} count {count} source {source} packet-size {size} timeout {timeout}
    * ping vrf {vrf} {addr} count {count} source {source} timeout {timeout} packet-size {size}
    * ping vrf {vrf} {addr} count {count} packet-size {size} source {source} timeout {timeout}
    * ping vrf {vrf} {addr} count {count} packet-size {size} timeout {timeout} source {source}
    * ping vrf {vrf} {addr} count {count} timeout {timeout} source {source} packet-size {size}
    * ping vrf {vrf} {addr} count {count} timeout {timeout} packet-size {size} source {source}
"""
# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (Any, Optional, Use,
                                                SchemaTypeError, Schema)


class PingSchema(MetaParser):
    """ Schema for
            * ping {addr}
            * ping {addr} count {count}
            * ping {addr} source {source}
            * ping {addr} packet-size {size}
            * ping {addr} timeout {timeout}
            * ping {addr} source {source} timeout {timeout}
            * ping {addr} timeout {timeout} source {source}
            * ping {addr} packet-size {size} timeout {timeout}
            * ping {addr} timeout {timeout} packet-size {size}
            * ping {addr} count {count} source {source}
            * ping {addr} source {source} count {count}
            * ping {addr} source {source} packet-size {size}
            * ping {addr} packet-size {size} source {source}
            * ping {addr} count {count} timeout {timeout}
            * ping {addr} timeout {timeout} count {count}
            * ping {addr} count {count} packet-size {size}
            * ping {addr} packet-size {size} count {count}
            * ping {addr} count {count} packet-size {size} timeout {timeout}
            * ping {addr} count {count} timeout {timeout} packet-size {size}
            * ping {addr} packet-size {size} count {count} timeout {timeout}
            * ping {addr} packet-size {size} timeout {timeout} count {count}
            * ping {addr} timeout {timeout} count {count} packet-size {size}
            * ping {addr} timeout {timeout} packet-size {size} count {count}
            * ping {addr} count {count} source {source} timeout {timeout}
            * ping {addr} count {count} timeout {timeout} source {source}
            * ping {addr} source {source} count {count} timeout {timeout}
            * ping {addr} source {source} timeout {timeout} count {count}
            * ping {addr} timeout {timeout} count {count} source {source}
            * ping {addr} timeout {timeout} source {source} count {count}
            * ping {addr} count {count} source {source} packet-size {size}
            * ping {addr} count {count} packet-size {size} source {source}
            * ping {addr} source {source} count {count} packet-size {size}
            * ping {addr} source {source} packet-size {size} count {count}
            * ping {addr} packet-size {size} count {count} source {source}
            * ping {addr} packet-size {size} source {source} count {count}
            * ping {addr} source {source} packet-size {size} timeout {timeout}
            * ping {addr} source {source} timeout {timeout} packet-size {size}
            * ping {addr} packet-size {size} source {source} timeout {timeout}
            * ping {addr} packet-size {size} timeout {timeout} source {source}
            * ping {addr} timeout {timeout} source {source} packet-size {size}
            * ping {addr} timeout {timeout} packet-size {size} source {source}
            * ping {addr} source {source} count {count} packet-size {size} timeout {timeout}
            * ping {addr} source {source} count {count} timeout {timeout} packet-size {size}
            * ping {addr} source {source} packet-size {size} count {count} timeout {timeout}
            * ping {addr} source {source} packet-size {size} timeout {timeout} count {count}
            * ping {addr} source {source} timeout {timeout} count {count} packet-size {size}
            * ping {addr} source {source} timeout {timeout} packet-size {size} count {count}
            * ping {addr} packet-size {size} count {count} source {source} timeout {timeout}
            * ping {addr} packet-size {size} count {count} timeout {timeout} source {source}
            * ping {addr} packet-size {size} source {source} count {count} timeout {timeout}
            * ping {addr} packet-size {size} source {source} timeout {timeout} count {count}
            * ping {addr} packet-size {size} timeout {timeout} count {count} source {source}
            * ping {addr} packet-size {size} timeout {timeout} source {source} count {count}
            * ping {addr} timeout {timeout} count {count} source {source} packet-size {size}
            * ping {addr} timeout {timeout} count {count} packet-size {size} source {source}
            * ping {addr} timeout {timeout} source {source} count {count} packet-size {size}
            * ping {addr} timeout {timeout} source {source} packet-size {size} count {count}
            * ping {addr} timeout {timeout} packet-size {size} count {count} source {source}
            * ping {addr} timeout {timeout} packet-size {size} source {source} count {count}
            * ping {addr} count {count} source {source} packet-size {size} timeout {timeout}
            * ping {addr} count {count} source {source} timeout {timeout} packet-size {size}
            * ping {addr} count {count} packet-size {size} source {source} timeout {timeout}
            * ping {addr} count {count} packet-size {size} timeout {timeout} source {source}
            * ping {addr} count {count} timeout {timeout} source {source} packet-size {size}
            * ping {addr} count {count} timeout {timeout} packet-size {size} source {source}
            * ping vrf {vrf} {addr}
            * ping vrf {vrf} {addr} count {count}
            * ping vrf {vrf} {addr} source {source}
            * ping vrf {vrf} {addr} packet-size {size}
            * ping vrf {vrf} {addr} timeout {timeout}
            * ping vrf {vrf} {addr} source {source} timeout {timeout}
            * ping vrf {vrf} {addr} timeout {timeout} source {source}
            * ping vrf {vrf} {addr} packet-size {size} timeout {timeout}
            * ping vrf {vrf} {addr} timeout {timeout} packet-size {size}
            * ping vrf {vrf} {addr} count {count} source {source}
            * ping vrf {vrf} {addr} source {source} count {count}
            * ping vrf {vrf} {addr} source {source} packet-size {size}
            * ping vrf {vrf} {addr} packet-size {size} source {source}
            * ping vrf {vrf} {addr} count {count} timeout {timeout}
            * ping vrf {vrf} {addr} timeout {timeout} count {count}
            * ping vrf {vrf} {addr} count {count} packet-size {size}
            * ping vrf {vrf} {addr} packet-size {size} count {count}
            * ping vrf {vrf} {addr} count {count} packet-size {size} timeout {timeout}
            * ping vrf {vrf} {addr} count {count} timeout {timeout} packet-size {size}
            * ping vrf {vrf} {addr} packet-size {size} count {count} timeout {timeout}
            * ping vrf {vrf} {addr} packet-size {size} timeout {timeout} count {count}
            * ping vrf {vrf} {addr} timeout {timeout} count {count} packet-size {size}
            * ping vrf {vrf} {addr} timeout {timeout} packet-size {size} count {count}
            * ping vrf {vrf} {addr} count {count} source {source} timeout {timeout}
            * ping vrf {vrf} {addr} count {count} timeout {timeout} source {source}
            * ping vrf {vrf} {addr} source {source} count {count} timeout {timeout}
            * ping vrf {vrf} {addr} source {source} timeout {timeout} count {count}
            * ping vrf {vrf} {addr} timeout {timeout} count {count} source {source}
            * ping vrf {vrf} {addr} timeout {timeout} source {source} count {count}
            * ping vrf {vrf} {addr} count {count} source {source} packet-size {size}
            * ping vrf {vrf} {addr} count {count} packet-size {size} source {source}
            * ping vrf {vrf} {addr} source {source} count {count} packet-size {size}
            * ping vrf {vrf} {addr} source {source} packet-size {size} count {count}
            * ping vrf {vrf} {addr} packet-size {size} count {count} source {source}
            * ping vrf {vrf} {addr} packet-size {size} source {source} count {count}
            * ping vrf {vrf} {addr} source {source} packet-size {size} timeout {timeout}
            * ping vrf {vrf} {addr} source {source} timeout {timeout} packet-size {size}
            * ping vrf {vrf} {addr} packet-size {size} source {source} timeout {timeout}
            * ping vrf {vrf} {addr} packet-size {size} timeout {timeout} source {source}
            * ping vrf {vrf} {addr} timeout {timeout} source {source} packet-size {size}
            * ping vrf {vrf} {addr} timeout {timeout} packet-size {size} source {source}
            * ping vrf {vrf} {addr} source {source} count {count} packet-size {size} timeout {timeout}
            * ping vrf {vrf} {addr} source {source} count {count} timeout {timeout} packet-size {size}
            * ping vrf {vrf} {addr} source {source} packet-size {size} count {count} timeout {timeout}
            * ping vrf {vrf} {addr} source {source} packet-size {size} timeout {timeout} count {count}
            * ping vrf {vrf} {addr} source {source} timeout {timeout} count {count} packet-size {size}
            * ping vrf {vrf} {addr} source {source} timeout {timeout} packet-size {size} count {count}
            * ping vrf {vrf} {addr} packet-size {size} count {count} source {source} timeout {timeout}
            * ping vrf {vrf} {addr} packet-size {size} count {count} timeout {timeout} source {source}
            * ping vrf {vrf} {addr} packet-size {size} source {source} count {count} timeout {timeout}
            * ping vrf {vrf} {addr} packet-size {size} source {source} timeout {timeout} count {count}
            * ping vrf {vrf} {addr} packet-size {size} timeout {timeout} count {count} source {source}
            * ping vrf {vrf} {addr} packet-size {size} timeout {timeout} source {source} count {count}
            * ping vrf {vrf} {addr} timeout {timeout} count {count} source {source} packet-size {size}
            * ping vrf {vrf} {addr} timeout {timeout} count {count} packet-size {size} source {source}
            * ping vrf {vrf} {addr} timeout {timeout} source {source} count {count} packet-size {size}
            * ping vrf {vrf} {addr} timeout {timeout} source {source} packet-size {size} count {count}
            * ping vrf {vrf} {addr} timeout {timeout} packet-size {size} count {count} source {source}
            * ping vrf {vrf} {addr} timeout {timeout} packet-size {size} source {source} count {count}
            * ping vrf {vrf} {addr} count {count} source {source} packet-size {size} timeout {timeout}
            * ping vrf {vrf} {addr} count {count} source {source} timeout {timeout} packet-size {size}
            * ping vrf {vrf} {addr} count {count} packet-size {size} source {source} timeout {timeout}
            * ping vrf {vrf} {addr} count {count} packet-size {size} timeout {timeout} source {source}
            * ping vrf {vrf} {addr} count {count} timeout {timeout} source {source} packet-size {size}
            * ping vrf {vrf} {addr} count {count} timeout {timeout} packet-size {size} source {source}
    """

    schema = {
        'ping': {
            'address': str,
            'ip': str,
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
                    'min_ms': float,
                    'avg_ms': float,
                    'max_ms': float,
                }
            }
        }
    }


class Ping(PingSchema):
    """ parser for
            * ping {addr}
            * ping {addr} count {count}
            * ping {addr} source {source}
            * ping {addr} packet-size {size}
            * ping {addr} timeout {timeout}
            * ping {addr} source {source} timeout {timeout}
            * ping {addr} timeout {timeout} source {source}
            * ping {addr} packet-size {size} timeout {timeout}
            * ping {addr} timeout {timeout} packet-size {size}
            * ping {addr} count {count} source {source}
            * ping {addr} source {source} count {count}
            * ping {addr} source {source} packet-size {size}
            * ping {addr} packet-size {size} source {source}
            * ping {addr} count {count} timeout {timeout}
            * ping {addr} timeout {timeout} count {count}
            * ping {addr} count {count} packet-size {size}
            * ping {addr} packet-size {size} count {count}
            * ping {addr} count {count} packet-size {size} timeout {timeout}
            * ping {addr} count {count} timeout {timeout} packet-size {size}
            * ping {addr} packet-size {size} count {count} timeout {timeout}
            * ping {addr} packet-size {size} timeout {timeout} count {count}
            * ping {addr} timeout {timeout} count {count} packet-size {size}
            * ping {addr} timeout {timeout} packet-size {size} count {count}
            * ping {addr} count {count} source {source} timeout {timeout}
            * ping {addr} count {count} timeout {timeout} source {source}
            * ping {addr} source {source} count {count} timeout {timeout}
            * ping {addr} source {source} timeout {timeout} count {count}
            * ping {addr} timeout {timeout} count {count} source {source}
            * ping {addr} timeout {timeout} source {source} count {count}
            * ping {addr} count {count} source {source} packet-size {size}
            * ping {addr} count {count} packet-size {size} source {source}
            * ping {addr} source {source} count {count} packet-size {size}
            * ping {addr} source {source} packet-size {size} count {count}
            * ping {addr} packet-size {size} count {count} source {source}
            * ping {addr} packet-size {size} source {source} count {count}
            * ping {addr} source {source} packet-size {size} timeout {timeout}
            * ping {addr} source {source} timeout {timeout} packet-size {size}
            * ping {addr} packet-size {size} source {source} timeout {timeout}
            * ping {addr} packet-size {size} timeout {timeout} source {source}
            * ping {addr} timeout {timeout} source {source} packet-size {size}
            * ping {addr} timeout {timeout} packet-size {size} source {source}
            * ping {addr} source {source} count {count} packet-size {size} timeout {timeout}
            * ping {addr} source {source} count {count} timeout {timeout} packet-size {size}
            * ping {addr} source {source} packet-size {size} count {count} timeout {timeout}
            * ping {addr} source {source} packet-size {size} timeout {timeout} count {count}
            * ping {addr} source {source} timeout {timeout} count {count} packet-size {size}
            * ping {addr} source {source} timeout {timeout} packet-size {size} count {count}
            * ping {addr} packet-size {size} count {count} source {source} timeout {timeout}
            * ping {addr} packet-size {size} count {count} timeout {timeout} source {source}
            * ping {addr} packet-size {size} source {source} count {count} timeout {timeout}
            * ping {addr} packet-size {size} source {source} timeout {timeout} count {count}
            * ping {addr} packet-size {size} timeout {timeout} count {count} source {source}
            * ping {addr} packet-size {size} timeout {timeout} source {source} count {count}
            * ping {addr} timeout {timeout} count {count} source {source} packet-size {size}
            * ping {addr} timeout {timeout} count {count} packet-size {size} source {source}
            * ping {addr} timeout {timeout} source {source} count {count} packet-size {size}
            * ping {addr} timeout {timeout} source {source} packet-size {size} count {count}
            * ping {addr} timeout {timeout} packet-size {size} count {count} source {source}
            * ping {addr} timeout {timeout} packet-size {size} source {source} count {count}
            * ping {addr} count {count} source {source} packet-size {size} timeout {timeout}
            * ping {addr} count {count} source {source} timeout {timeout} packet-size {size}
            * ping {addr} count {count} packet-size {size} source {source} timeout {timeout}
            * ping {addr} count {count} packet-size {size} timeout {timeout} source {source}
            * ping {addr} count {count} timeout {timeout} source {source} packet-size {size}
            * ping {addr} count {count} timeout {timeout} packet-size {size} source {source}
            * ping vrf {vrf} {addr}
            * ping vrf {vrf} {addr} count {count}
            * ping vrf {vrf} {addr} source {source}
            * ping vrf {vrf} {addr} packet-size {size}
            * ping vrf {vrf} {addr} timeout {timeout}
            * ping vrf {vrf} {addr} source {source} timeout {timeout}
            * ping vrf {vrf} {addr} timeout {timeout} source {source}
            * ping vrf {vrf} {addr} packet-size {size} timeout {timeout}
            * ping vrf {vrf} {addr} timeout {timeout} packet-size {size}
            * ping vrf {vrf} {addr} count {count} source {source}
            * ping vrf {vrf} {addr} source {source} count {count}
            * ping vrf {vrf} {addr} source {source} packet-size {size}
            * ping vrf {vrf} {addr} packet-size {size} source {source}
            * ping vrf {vrf} {addr} count {count} timeout {timeout}
            * ping vrf {vrf} {addr} timeout {timeout} count {count}
            * ping vrf {vrf} {addr} count {count} packet-size {size}
            * ping vrf {vrf} {addr} packet-size {size} count {count}
            * ping vrf {vrf} {addr} count {count} packet-size {size} timeout {timeout}
            * ping vrf {vrf} {addr} count {count} timeout {timeout} packet-size {size}
            * ping vrf {vrf} {addr} packet-size {size} count {count} timeout {timeout}
            * ping vrf {vrf} {addr} packet-size {size} timeout {timeout} count {count}
            * ping vrf {vrf} {addr} timeout {timeout} count {count} packet-size {size}
            * ping vrf {vrf} {addr} timeout {timeout} packet-size {size} count {count}
            * ping vrf {vrf} {addr} count {count} source {source} timeout {timeout}
            * ping vrf {vrf} {addr} count {count} timeout {timeout} source {source}
            * ping vrf {vrf} {addr} source {source} count {count} timeout {timeout}
            * ping vrf {vrf} {addr} source {source} timeout {timeout} count {count}
            * ping vrf {vrf} {addr} timeout {timeout} count {count} source {source}
            * ping vrf {vrf} {addr} timeout {timeout} source {source} count {count}
            * ping vrf {vrf} {addr} count {count} source {source} packet-size {size}
            * ping vrf {vrf} {addr} count {count} packet-size {size} source {source}
            * ping vrf {vrf} {addr} source {source} count {count} packet-size {size}
            * ping vrf {vrf} {addr} source {source} packet-size {size} count {count}
            * ping vrf {vrf} {addr} packet-size {size} count {count} source {source}
            * ping vrf {vrf} {addr} packet-size {size} source {source} count {count}
            * ping vrf {vrf} {addr} source {source} packet-size {size} timeout {timeout}
            * ping vrf {vrf} {addr} source {source} timeout {timeout} packet-size {size}
            * ping vrf {vrf} {addr} packet-size {size} source {source} timeout {timeout}
            * ping vrf {vrf} {addr} packet-size {size} timeout {timeout} source {source}
            * ping vrf {vrf} {addr} timeout {timeout} source {source} packet-size {size}
            * ping vrf {vrf} {addr} timeout {timeout} packet-size {size} source {source}
            * ping vrf {vrf} {addr} source {source} count {count} packet-size {size} timeout {timeout}
            * ping vrf {vrf} {addr} source {source} count {count} timeout {timeout} packet-size {size}
            * ping vrf {vrf} {addr} source {source} packet-size {size} count {count} timeout {timeout}
            * ping vrf {vrf} {addr} source {source} packet-size {size} timeout {timeout} count {count}
            * ping vrf {vrf} {addr} source {source} timeout {timeout} count {count} packet-size {size}
            * ping vrf {vrf} {addr} source {source} timeout {timeout} packet-size {size} count {count}
            * ping vrf {vrf} {addr} packet-size {size} count {count} source {source} timeout {timeout}
            * ping vrf {vrf} {addr} packet-size {size} count {count} timeout {timeout} source {source}
            * ping vrf {vrf} {addr} packet-size {size} source {source} count {count} timeout {timeout}
            * ping vrf {vrf} {addr} packet-size {size} source {source} timeout {timeout} count {count}
            * ping vrf {vrf} {addr} packet-size {size} timeout {timeout} count {count} source {source}
            * ping vrf {vrf} {addr} packet-size {size} timeout {timeout} source {source} count {count}
            * ping vrf {vrf} {addr} timeout {timeout} count {count} source {source} packet-size {size}
            * ping vrf {vrf} {addr} timeout {timeout} count {count} packet-size {size} source {source}
            * ping vrf {vrf} {addr} timeout {timeout} source {source} count {count} packet-size {size}
            * ping vrf {vrf} {addr} timeout {timeout} source {source} packet-size {size} count {count}
            * ping vrf {vrf} {addr} timeout {timeout} packet-size {size} count {count} source {source}
            * ping vrf {vrf} {addr} timeout {timeout} packet-size {size} source {source} count {count}
            * ping vrf {vrf} {addr} count {count} source {source} packet-size {size} timeout {timeout}
            * ping vrf {vrf} {addr} count {count} source {source} timeout {timeout} packet-size {size}
            * ping vrf {vrf} {addr} count {count} packet-size {size} source {source} timeout {timeout}
            * ping vrf {vrf} {addr} count {count} packet-size {size} timeout {timeout} source {source}
            * ping vrf {vrf} {addr} count {count} timeout {timeout} source {source} packet-size {size}
            * ping vrf {vrf} {addr} count {count} timeout {timeout} packet-size {size} source {source}
    """

    cli_command = [
        'ping {addr}',
        'ping {addr} count {count}',
        'ping {addr} source {source}',
        'ping {addr} packet-size {size}',
        'ping {addr} timeout {timeout}',
        'ping {addr} source {source} timeout {timeout}',
        'ping {addr} timeout {timeout} source {source}',
        'ping {addr} packet-size {size} timeout {timeout}',
        'ping {addr} timeout {timeout} packet-size {size}',
        'ping {addr} count {count} source {source}',
        'ping {addr} source {source} count {count}',
        'ping {addr} source {source} packet-size {size}',
        'ping {addr} packet-size {size} source {source}',
        'ping {addr} count {count} timeout {timeout}',
        'ping {addr} timeout {timeout} count {count}',
        'ping {addr} count {count} packet-size {size}',
        'ping {addr} packet-size {size} count {count}',
        'ping {addr} count {count} packet-size {size} timeout {timeout}',
        'ping {addr} count {count} timeout {timeout} packet-size {size}',
        'ping {addr} packet-size {size} count {count} timeout {timeout}',
        'ping {addr} packet-size {size} timeout {timeout} count {count}',
        'ping {addr} timeout {timeout} count {count} packet-size {size}',
        'ping {addr} timeout {timeout} packet-size {size} count {count}',
        'ping {addr} count {count} source {source} timeout {timeout}',
        'ping {addr} count {count} timeout {timeout} source {source}',
        'ping {addr} source {source} count {count} timeout {timeout}',
        'ping {addr} source {source} timeout {timeout} count {count}',
        'ping {addr} timeout {timeout} count {count} source {source}',
        'ping {addr} timeout {timeout} source {source} count {count}',
        'ping {addr} count {count} source {source} packet-size {size}',
        'ping {addr} count {count} packet-size {size} source {source}',
        'ping {addr} source {source} count {count} packet-size {size}',
        'ping {addr} source {source} packet-size {size} count {count}',
        'ping {addr} packet-size {size} count {count} source {source}',
        'ping {addr} packet-size {size} source {source} count {count}',
        'ping {addr} source {source} packet-size {size} timeout {timeout}',
        'ping {addr} source {source} timeout {timeout} packet-size {size}',
        'ping {addr} packet-size {size} source {source} timeout {timeout}',
        'ping {addr} packet-size {size} timeout {timeout} source {source}',
        'ping {addr} timeout {timeout} source {source} packet-size {size}',
        'ping {addr} timeout {timeout} packet-size {size} source {source}',
        'ping {addr} source {source} count {count} packet-size {size} timeout {timeout}',
        'ping {addr} source {source} count {count} timeout {timeout} packet-size {size}',
        'ping {addr} source {source} packet-size {size} count {count} timeout {timeout}',
        'ping {addr} source {source} packet-size {size} timeout {timeout} count {count}',
        'ping {addr} source {source} timeout {timeout} count {count} packet-size {size}',
        'ping {addr} source {source} timeout {timeout} packet-size {size} count {count}',
        'ping {addr} packet-size {size} count {count} source {source} timeout {timeout}',
        'ping {addr} packet-size {size} count {count} timeout {timeout} source {source}',
        'ping {addr} packet-size {size} source {source} count {count} timeout {timeout}',
        'ping {addr} packet-size {size} source {source} timeout {timeout} count {count}',
        'ping {addr} packet-size {size} timeout {timeout} count {count} source {source}',
        'ping {addr} packet-size {size} timeout {timeout} source {source} count {count}',
        'ping {addr} timeout {timeout} count {count} source {source} packet-size {size}',
        'ping {addr} timeout {timeout} count {count} packet-size {size} source {source}',
        'ping {addr} timeout {timeout} source {source} count {count} packet-size {size}',
        'ping {addr} timeout {timeout} source {source} packet-size {size} count {count}',
        'ping {addr} timeout {timeout} packet-size {size} count {count} source {source}',
        'ping {addr} timeout {timeout} packet-size {size} source {source} count {count}',
        'ping {addr} count {count} source {source} packet-size {size} timeout {timeout}',
        'ping {addr} count {count} source {source} timeout {timeout} packet-size {size}',
        'ping {addr} count {count} packet-size {size} source {source} timeout {timeout}',
        'ping {addr} count {count} packet-size {size} timeout {timeout} source {source}',
        'ping {addr} count {count} timeout {timeout} source {source} packet-size {size}',
        'ping {addr} count {count} timeout {timeout} packet-size {size} source {source}',
        'ping {addr} vrf {vrf}',
        'ping {addr} vrf {vrf} count {count}',
        'ping {addr} vrf {vrf} source {source}',
        'ping {addr} vrf {vrf} packet-size {size}',
        'ping {addr} vrf {vrf} timeout {timeout}',
        'ping {addr} vrf {vrf} source {source} timeout {timeout}',
        'ping {addr} vrf {vrf} timeout {timeout} source {source}',
        'ping {addr} vrf {vrf} packet-size {size} timeout {timeout}',
        'ping {addr} vrf {vrf} timeout {timeout} packet-size {size}',
        'ping {addr} vrf {vrf} count {count} source {source}',
        'ping {addr} vrf {vrf} source {source} count {count}',
        'ping {addr} vrf {vrf} source {source} packet-size {size}',
        'ping {addr} vrf {vrf} packet-size {size} source {source}',
        'ping {addr} vrf {vrf} count {count} timeout {timeout}',
        'ping {addr} vrf {vrf} timeout {timeout} count {count}',
        'ping {addr} vrf {vrf} count {count} packet-size {size}',
        'ping {addr} vrf {vrf} packet-size {size} count {count}',
        'ping {addr} vrf {vrf} count {count} packet-size {size} timeout {timeout}',
        'ping {addr} vrf {vrf} count {count} timeout {timeout} packet-size {size}',
        'ping {addr} vrf {vrf} packet-size {size} count {count} timeout {timeout}',
        'ping {addr} vrf {vrf} packet-size {size} timeout {timeout} count {count}',
        'ping {addr} vrf {vrf} timeout {timeout} count {count} packet-size {size}',
        'ping {addr} vrf {vrf} timeout {timeout} packet-size {size} count {count}',
        'ping {addr} vrf {vrf} count {count} source {source} timeout {timeout}',
        'ping {addr} vrf {vrf} count {count} timeout {timeout} source {source}',
        'ping {addr} vrf {vrf} source {source} count {count} timeout {timeout}',
        'ping {addr} vrf {vrf} source {source} timeout {timeout} count {count}',
        'ping {addr} vrf {vrf} timeout {timeout} count {count} source {source}',
        'ping {addr} vrf {vrf} timeout {timeout} source {source} count {count}',
        'ping {addr} vrf {vrf} count {count} source {source} packet-size {size}',
        'ping {addr} vrf {vrf} count {count} packet-size {size} source {source}',
        'ping {addr} vrf {vrf} source {source} count {count} packet-size {size}',
        'ping {addr} vrf {vrf} source {source} packet-size {size} count {count}',
        'ping {addr} vrf {vrf} packet-size {size} count {count} source {source}',
        'ping {addr} vrf {vrf} packet-size {size} source {source} count {count}',
        'ping {addr} vrf {vrf} source {source} packet-size {size} timeout {timeout}',
        'ping {addr} vrf {vrf} source {source} timeout {timeout} packet-size {size}',
        'ping {addr} vrf {vrf} packet-size {size} source {source} timeout {timeout}',
        'ping {addr} vrf {vrf} packet-size {size} timeout {timeout} source {source}',
        'ping {addr} vrf {vrf} timeout {timeout} source {source} packet-size {size}',
        'ping {addr} vrf {vrf} timeout {timeout} packet-size {size} source {source}',
        'ping {addr} vrf {vrf} source {source} count {count} packet-size {size} timeout {timeout}',
        'ping {addr} vrf {vrf} source {source} count {count} timeout {timeout} packet-size {size}',
        'ping {addr} vrf {vrf} source {source} packet-size {size} count {count} timeout {timeout}',
        'ping {addr} vrf {vrf} source {source} packet-size {size} timeout {timeout} count {count}',
        'ping {addr} vrf {vrf} source {source} timeout {timeout} count {count} packet-size {size}',
        'ping {addr} vrf {vrf} source {source} timeout {timeout} packet-size {size} count {count}',
        'ping {addr} vrf {vrf} packet-size {size} count {count} source {source} timeout {timeout}',
        'ping {addr} vrf {vrf} packet-size {size} count {count} timeout {timeout} source {source}',
        'ping {addr} vrf {vrf} packet-size {size} source {source} count {count} timeout {timeout}',
        'ping {addr} vrf {vrf} packet-size {size} source {source} timeout {timeout} count {count}',
        'ping {addr} vrf {vrf} packet-size {size} timeout {timeout} count {count} source {source}',
        'ping {addr} vrf {vrf} packet-size {size} timeout {timeout} source {source} count {count}',
        'ping {addr} vrf {vrf} timeout {timeout} count {count} source {source} packet-size {size}',
        'ping {addr} vrf {vrf} timeout {timeout} count {count} packet-size {size} source {source}',
        'ping {addr} vrf {vrf} timeout {timeout} source {source} count {count} packet-size {size}',
        'ping {addr} vrf {vrf} timeout {timeout} source {source} packet-size {size} count {count}',
        'ping {addr} vrf {vrf} timeout {timeout} packet-size {size} count {count} source {source}',
        'ping {addr} vrf {vrf} timeout {timeout} packet-size {size} source {source} count {count}',
        'ping {addr} vrf {vrf} count {count} source {source} packet-size {size} timeout {timeout}',
        'ping {addr} vrf {vrf} count {count} source {source} timeout {timeout} packet-size {size}',
        'ping {addr} vrf {vrf} count {count} packet-size {size} source {source} timeout {timeout}',
        'ping {addr} vrf {vrf} count {count} packet-size {size} timeout {timeout} source {source}',
        'ping {addr} vrf {vrf} count {count} timeout {timeout} source {source} packet-size {size}',
        'ping {addr} vrf {vrf} count {count} timeout {timeout} packet-size {size} source {source}',
    ]

    def cli(self,
            addr,
            count=None,
            source=None,
            vrf=None,
            size=None,
            timeout=None,
            output=None):

        if not output:
            cmd = []
            if addr and vrf:
                cmd.append('ping {addr} vrf {vrf}'.format(vrf=vrf, addr=addr))
            elif addr:
                cmd.append('ping {addr}'.format(addr=addr))
            if source:
                cmd.append('source {source}'.format(source=source))
            if count:
                cmd.append('count {count}'.format(count=count))
            if size:
                cmd.append('packet-size {size}'.format(size=size))
            if timeout:
                cmd.append('timeout {timeout}'.format(timeout=timeout))
            cmd = ' '.join(cmd)
            out = self.device.execute(cmd)
        else:
            out = output

        ret_dict = {}
        result_per_line = []

        # PING 10.2.2.2 (10.2.2.2): 56 data bytes
        # PING R2_xr (10.2.2.2) from 10.3.3.3: 56 data bytes
        p1 = re.compile(
            r'^PING\s+(?P<address>[\S]+)\s+\((?P<ip>\S+)\)(\s+from\s+(?P<source>\S+))?:\s+(?P<data_bytes>\d+)\s+data\s+bytes'
        )

        # 64 bytes from 10.2.2.2: icmp_seq=0 ttl=254 time=4.669 ms
        p2 = re.compile(r'^\d+\s+bytes\s+from')

        # Request 0 timed out
        p2_1 = re.compile(r'^Request\s+\d+\s+timed\s+out')

        # ping: sendto 10.1.1.5 64 chars, No route to host
        p2_2 = re.compile(r'^ping:\ssendto\s')

        # 10 packets transmitted, 0 packets received, 100.00% packet loss
        p3 = re.compile(
            r'^(?P<send>\d+)\s+packets\s+transmitted,\s+(?P<received>\d+)\s+packets\s+received,\s+(?P<loss_percent>\S+)%\s+packet\s+loss'
        )

        # round-trip min/avg/max = 2.334/3.74/5.13 ms
        p4 = re.compile(
            r'^round-trip\smin/avg/max\s=\s+(?P<min_ms>\d+\.\d+)/(?P<avg_ms>\d+\.\d+)/(?P<max_ms>\d+\.\d+)\s+ms'
        )

        ping_dict = {}
        for line in out.splitlines():
            line = line.strip()

            # PING 10.2.2.2 (10.2.2.2): 56 data bytes
            # PING R2_xr (10.2.2.2) from 10.3.3.3: 56 data bytes
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ping_dict = ret_dict.setdefault('ping', {})
                ping_dict.update({
                    'data_bytes': int(group['data_bytes']),
                    'address': group['address'],
                    'ip': group['ip'],
                })
                if count:
                    ping_dict.update({'repeat': int(count)})
                else:
                    ping_dict.update({'repeat': 5})
                if timeout:
                    ping_dict.update({'timeout_secs': int(timeout)})
                if group['source']:
                    ping_dict.update({'source': group['source']})
                continue

            # 64 bytes from 10.2.2.2: icmp_seq=0 ttl=254 time=4.669 ms
            m = p2.match(line)
            if m:
                group = m.groupdict()
                result_per_line.append(line)
                ping_dict.update({'result_per_line': result_per_line})
                continue

            # Request 0 timed out
            m = p2_1.match(line)
            if m:
                group = m.groupdict()
                result_per_line.append(line)
                ping_dict.update({'result_per_line': result_per_line})
                continue

            # ping: sendto 10.1.1.5 64 chars, No route to host
            m = p2_2.match(line)
            if m:
                group = m.groupdict()
                result_per_line.append(line)
                ping_dict.update({'result_per_line': result_per_line})
                continue

            # 10 packets transmitted, 0 packets received, 100.00% packet loss
            m = p3.match(line)
            if m:
                group = m.groupdict()
                stat_dict = ping_dict.setdefault('statistics', {})
                stat_dict.update({
                    'success_rate_percent':
                    float(100 - float(group['loss_percent'])),
                    'received':
                    int(group['received']),
                    'send':
                    int(group['send']),
                })
                continue

            # round-trip min/avg/max = 2.334/3.74/5.13 ms
            m = p4.match(line)
            if m:
                group = m.groupdict()
                if 'statistics' in ping_dict:
                    ping_dict['statistics'].setdefault(
                        'round_trip', {}).update({
                            'min_ms':
                            float(group['min_ms']),
                            'avg_ms':
                            float(group['avg_ms']),
                            'max_ms':
                            float(group['max_ms']),
                        })

        return ret_dict
