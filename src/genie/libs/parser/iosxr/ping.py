"""ping.py

IOSXR parsers for the following show commands:
    * ping {addr}
    * ping {addr} count {count}
    * ping {addr} source {source}
    * ping {addr} size {size}
    * ping {addr} timeout {timeout}
    * ping {addr} source {source} timeout {timeout}
    * ping {addr} timeout {timeout} source {source}
    * ping {addr} size {size} timeout {timeout}
    * ping {addr} timeout {timeout} size {size}
    * ping {addr} count {count} source {source}
    * ping {addr} source {source} count {count}
    * ping {addr} source {source} size {size}
    * ping {addr} size {size} source {source}
    * ping {addr} count {count} timeout {timeout}
    * ping {addr} timeout {timeout} count {count}
    * ping {addr} count {count} size {size}
    * ping {addr} size {size} count {count}
    * ping {addr} count {count} size {size} timeout {timeout}
    * ping {addr} count {count} timeout {timeout} size {size}
    * ping {addr} size {size} count {count} timeout {timeout}
    * ping {addr} size {size} timeout {timeout} count {count}
    * ping {addr} timeout {timeout} count {count} size {size}
    * ping {addr} timeout {timeout} size {size} count {count}
    * ping {addr} count {count} source {source} timeout {timeout}
    * ping {addr} count {count} timeout {timeout} source {source}
    * ping {addr} source {source} count {count} timeout {timeout}
    * ping {addr} source {source} timeout {timeout} count {count}
    * ping {addr} timeout {timeout} count {count} source {source}
    * ping {addr} timeout {timeout} source {source} count {count}
    * ping {addr} count {count} source {source} size {size}
    * ping {addr} count {count} size {size} source {source}
    * ping {addr} source {source} count {count} size {size}
    * ping {addr} source {source} size {size} count {count}
    * ping {addr} size {size} count {count} source {source}
    * ping {addr} size {size} source {source} count {count}
    * ping {addr} source {source} size {size} timeout {timeout}
    * ping {addr} source {source} timeout {timeout} size {size}
    * ping {addr} size {size} source {source} timeout {timeout}
    * ping {addr} size {size} timeout {timeout} source {source}
    * ping {addr} timeout {timeout} source {source} size {size}
    * ping {addr} timeout {timeout} size {size} source {source}
    * ping {addr} source {source} count {count} size {size} timeout {timeout}
    * ping {addr} source {source} count {count} timeout {timeout} size {size}
    * ping {addr} source {source} size {size} count {count} timeout {timeout}
    * ping {addr} source {source} size {size} timeout {timeout} count {count}
    * ping {addr} source {source} timeout {timeout} count {count} size {size}
    * ping {addr} source {source} timeout {timeout} size {size} count {count}
    * ping {addr} size {size} count {count} source {source} timeout {timeout}
    * ping {addr} size {size} count {count} timeout {timeout} source {source}
    * ping {addr} size {size} source {source} count {count} timeout {timeout}
    * ping {addr} size {size} source {source} timeout {timeout} count {count}
    * ping {addr} size {size} timeout {timeout} count {count} source {source}
    * ping {addr} size {size} timeout {timeout} source {source} count {count}
    * ping {addr} timeout {timeout} count {count} source {source} size {size}
    * ping {addr} timeout {timeout} count {count} size {size} source {source}
    * ping {addr} timeout {timeout} source {source} count {count} size {size}
    * ping {addr} timeout {timeout} source {source} size {size} count {count}
    * ping {addr} timeout {timeout} size {size} count {count} source {source}
    * ping {addr} timeout {timeout} size {size} source {source} count {count}
    * ping {addr} count {count} source {source} size {size} timeout {timeout}
    * ping {addr} count {count} source {source} timeout {timeout} size {size}
    * ping {addr} count {count} size {size} source {source} timeout {timeout}
    * ping {addr} count {count} size {size} timeout {timeout} source {source}
    * ping {addr} count {count} timeout {timeout} source {source} size {size}
    * ping {addr} count {count} timeout {timeout} size {size} source {source}
    * ping vrf {vrf} {addr}
    * ping vrf {vrf} {addr} count {count}
    * ping vrf {vrf} {addr} source {source}
    * ping vrf {vrf} {addr} size {size}
    * ping vrf {vrf} {addr} timeout {timeout}
    * ping vrf {vrf} {addr} source {source} timeout {timeout}
    * ping vrf {vrf} {addr} timeout {timeout} source {source}
    * ping vrf {vrf} {addr} size {size} timeout {timeout}
    * ping vrf {vrf} {addr} timeout {timeout} size {size}
    * ping vrf {vrf} {addr} count {count} source {source}
    * ping vrf {vrf} {addr} source {source} count {count}
    * ping vrf {vrf} {addr} source {source} size {size}
    * ping vrf {vrf} {addr} size {size} source {source}
    * ping vrf {vrf} {addr} count {count} timeout {timeout}
    * ping vrf {vrf} {addr} timeout {timeout} count {count}
    * ping vrf {vrf} {addr} count {count} size {size}
    * ping vrf {vrf} {addr} size {size} count {count}
    * ping vrf {vrf} {addr} count {count} size {size} timeout {timeout}
    * ping vrf {vrf} {addr} count {count} timeout {timeout} size {size}
    * ping vrf {vrf} {addr} size {size} count {count} timeout {timeout}
    * ping vrf {vrf} {addr} size {size} timeout {timeout} count {count}
    * ping vrf {vrf} {addr} timeout {timeout} count {count} size {size}
    * ping vrf {vrf} {addr} timeout {timeout} size {size} count {count}
    * ping vrf {vrf} {addr} count {count} source {source} timeout {timeout}
    * ping vrf {vrf} {addr} count {count} timeout {timeout} source {source}
    * ping vrf {vrf} {addr} source {source} count {count} timeout {timeout}
    * ping vrf {vrf} {addr} source {source} timeout {timeout} count {count}
    * ping vrf {vrf} {addr} timeout {timeout} count {count} source {source}
    * ping vrf {vrf} {addr} timeout {timeout} source {source} count {count}
    * ping vrf {vrf} {addr} count {count} source {source} size {size}
    * ping vrf {vrf} {addr} count {count} size {size} source {source}
    * ping vrf {vrf} {addr} source {source} count {count} size {size}
    * ping vrf {vrf} {addr} source {source} size {size} count {count}
    * ping vrf {vrf} {addr} size {size} count {count} source {source}
    * ping vrf {vrf} {addr} size {size} source {source} count {count}
    * ping vrf {vrf} {addr} source {source} size {size} timeout {timeout}
    * ping vrf {vrf} {addr} source {source} timeout {timeout} size {size}
    * ping vrf {vrf} {addr} size {size} source {source} timeout {timeout}
    * ping vrf {vrf} {addr} size {size} timeout {timeout} source {source}
    * ping vrf {vrf} {addr} timeout {timeout} source {source} size {size}
    * ping vrf {vrf} {addr} timeout {timeout} size {size} source {source}
    * ping vrf {vrf} {addr} source {source} count {count} size {size} timeout {timeout}
    * ping vrf {vrf} {addr} source {source} count {count} timeout {timeout} size {size}
    * ping vrf {vrf} {addr} source {source} size {size} count {count} timeout {timeout}
    * ping vrf {vrf} {addr} source {source} size {size} timeout {timeout} count {count}
    * ping vrf {vrf} {addr} source {source} timeout {timeout} count {count} size {size}
    * ping vrf {vrf} {addr} source {source} timeout {timeout} size {size} count {count}
    * ping vrf {vrf} {addr} size {size} count {count} source {source} timeout {timeout}
    * ping vrf {vrf} {addr} size {size} count {count} timeout {timeout} source {source}
    * ping vrf {vrf} {addr} size {size} source {source} count {count} timeout {timeout}
    * ping vrf {vrf} {addr} size {size} source {source} timeout {timeout} count {count}
    * ping vrf {vrf} {addr} size {size} timeout {timeout} count {count} source {source}
    * ping vrf {vrf} {addr} size {size} timeout {timeout} source {source} count {count}
    * ping vrf {vrf} {addr} timeout {timeout} count {count} source {source} size {size}
    * ping vrf {vrf} {addr} timeout {timeout} count {count} size {size} source {source}
    * ping vrf {vrf} {addr} timeout {timeout} source {source} count {count} size {size}
    * ping vrf {vrf} {addr} timeout {timeout} source {source} size {size} count {count}
    * ping vrf {vrf} {addr} timeout {timeout} size {size} count {count} source {source}
    * ping vrf {vrf} {addr} timeout {timeout} size {size} source {source} count {count}
    * ping vrf {vrf} {addr} count {count} source {source} size {size} timeout {timeout}
    * ping vrf {vrf} {addr} count {count} source {source} timeout {timeout} size {size}
    * ping vrf {vrf} {addr} count {count} size {size} source {source} timeout {timeout}
    * ping vrf {vrf} {addr} count {count} size {size} timeout {timeout} source {source}
    * ping vrf {vrf} {addr} count {count} timeout {timeout} source {source} size {size}
    * ping vrf {vrf} {addr} count {count} timeout {timeout} size {size} source {source}
"""
# Python
import re
from typing import Counter, Sized

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (Any,
        Optional, Use, SchemaTypeError, Schema)

class PingSchema(MetaParser):
    """ Schema for
            * ping {addr}
            * ping {addr} count {count}
            * ping {addr} source {source}
            * ping {addr} size {size}
            * ping {addr} timeout {timeout}
            * ping {addr} source {source} timeout {timeout}
            * ping {addr} timeout {timeout} source {source}
            * ping {addr} size {size} timeout {timeout}
            * ping {addr} timeout {timeout} size {size}
            * ping {addr} count {count} source {source}
            * ping {addr} source {source} count {count}
            * ping {addr} source {source} size {size}
            * ping {addr} size {size} source {source}
            * ping {addr} count {count} timeout {timeout}
            * ping {addr} timeout {timeout} count {count}
            * ping {addr} count {count} size {size}
            * ping {addr} size {size} count {count}
            * ping {addr} count {count} size {size} timeout {timeout}
            * ping {addr} count {count} timeout {timeout} size {size}
            * ping {addr} size {size} count {count} timeout {timeout}
            * ping {addr} size {size} timeout {timeout} count {count}
            * ping {addr} timeout {timeout} count {count} size {size}
            * ping {addr} timeout {timeout} size {size} count {count}
            * ping {addr} count {count} source {source} timeout {timeout}
            * ping {addr} count {count} timeout {timeout} source {source}
            * ping {addr} source {source} count {count} timeout {timeout}
            * ping {addr} source {source} timeout {timeout} count {count}
            * ping {addr} timeout {timeout} count {count} source {source}
            * ping {addr} timeout {timeout} source {source} count {count}
            * ping {addr} count {count} source {source} size {size}
            * ping {addr} count {count} size {size} source {source}
            * ping {addr} source {source} count {count} size {size}
            * ping {addr} source {source} size {size} count {count}
            * ping {addr} size {size} count {count} source {source}
            * ping {addr} size {size} source {source} count {count}
            * ping {addr} source {source} size {size} timeout {timeout}
            * ping {addr} source {source} timeout {timeout} size {size}
            * ping {addr} size {size} source {source} timeout {timeout}
            * ping {addr} size {size} timeout {timeout} source {source}
            * ping {addr} timeout {timeout} source {source} size {size}
            * ping {addr} timeout {timeout} size {size} source {source}
            * ping {addr} source {source} count {count} size {size} timeout {timeout}
            * ping {addr} source {source} count {count} timeout {timeout} size {size}
            * ping {addr} source {source} size {size} count {count} timeout {timeout}
            * ping {addr} source {source} size {size} timeout {timeout} count {count}
            * ping {addr} source {source} timeout {timeout} count {count} size {size}
            * ping {addr} source {source} timeout {timeout} size {size} count {count}
            * ping {addr} size {size} count {count} source {source} timeout {timeout}
            * ping {addr} size {size} count {count} timeout {timeout} source {source}
            * ping {addr} size {size} source {source} count {count} timeout {timeout}
            * ping {addr} size {size} source {source} timeout {timeout} count {count}
            * ping {addr} size {size} timeout {timeout} count {count} source {source}
            * ping {addr} size {size} timeout {timeout} source {source} count {count}
            * ping {addr} timeout {timeout} count {count} source {source} size {size}
            * ping {addr} timeout {timeout} count {count} size {size} source {source}
            * ping {addr} timeout {timeout} source {source} count {count} size {size}
            * ping {addr} timeout {timeout} source {source} size {size} count {count}
            * ping {addr} timeout {timeout} size {size} count {count} source {source}
            * ping {addr} timeout {timeout} size {size} source {source} count {count}
            * ping {addr} count {count} source {source} size {size} timeout {timeout}
            * ping {addr} count {count} source {source} timeout {timeout} size {size}
            * ping {addr} count {count} size {size} source {source} timeout {timeout}
            * ping {addr} count {count} size {size} timeout {timeout} source {source}
            * ping {addr} count {count} timeout {timeout} source {source} size {size}
            * ping {addr} count {count} timeout {timeout} size {size} source {source}
            * ping vrf {vrf} {addr}
            * ping vrf {vrf} {addr} count {count}
            * ping vrf {vrf} {addr} source {source}
            * ping vrf {vrf} {addr} size {size}
            * ping vrf {vrf} {addr} timeout {timeout}
            * ping vrf {vrf} {addr} source {source} timeout {timeout}
            * ping vrf {vrf} {addr} timeout {timeout} source {source}
            * ping vrf {vrf} {addr} size {size} timeout {timeout}
            * ping vrf {vrf} {addr} timeout {timeout} size {size}
            * ping vrf {vrf} {addr} count {count} source {source}
            * ping vrf {vrf} {addr} source {source} count {count}
            * ping vrf {vrf} {addr} source {source} size {size}
            * ping vrf {vrf} {addr} size {size} source {source}
            * ping vrf {vrf} {addr} count {count} timeout {timeout}
            * ping vrf {vrf} {addr} timeout {timeout} count {count}
            * ping vrf {vrf} {addr} count {count} size {size}
            * ping vrf {vrf} {addr} size {size} count {count}
            * ping vrf {vrf} {addr} count {count} size {size} timeout {timeout}
            * ping vrf {vrf} {addr} count {count} timeout {timeout} size {size}
            * ping vrf {vrf} {addr} size {size} count {count} timeout {timeout}
            * ping vrf {vrf} {addr} size {size} timeout {timeout} count {count}
            * ping vrf {vrf} {addr} timeout {timeout} count {count} size {size}
            * ping vrf {vrf} {addr} timeout {timeout} size {size} count {count}
            * ping vrf {vrf} {addr} count {count} source {source} timeout {timeout}
            * ping vrf {vrf} {addr} count {count} timeout {timeout} source {source}
            * ping vrf {vrf} {addr} source {source} count {count} timeout {timeout}
            * ping vrf {vrf} {addr} source {source} timeout {timeout} count {count}
            * ping vrf {vrf} {addr} timeout {timeout} count {count} source {source}
            * ping vrf {vrf} {addr} timeout {timeout} source {source} count {count}
            * ping vrf {vrf} {addr} count {count} source {source} size {size}
            * ping vrf {vrf} {addr} count {count} size {size} source {source}
            * ping vrf {vrf} {addr} source {source} count {count} size {size}
            * ping vrf {vrf} {addr} source {source} size {size} count {count}
            * ping vrf {vrf} {addr} size {size} count {count} source {source}
            * ping vrf {vrf} {addr} size {size} source {source} count {count}
            * ping vrf {vrf} {addr} source {source} size {size} timeout {timeout}
            * ping vrf {vrf} {addr} source {source} timeout {timeout} size {size}
            * ping vrf {vrf} {addr} size {size} source {source} timeout {timeout}
            * ping vrf {vrf} {addr} size {size} timeout {timeout} source {source}
            * ping vrf {vrf} {addr} timeout {timeout} source {source} size {size}
            * ping vrf {vrf} {addr} timeout {timeout} size {size} source {source}
            * ping vrf {vrf} {addr} source {source} count {count} size {size} timeout {timeout}
            * ping vrf {vrf} {addr} source {source} count {count} timeout {timeout} size {size}
            * ping vrf {vrf} {addr} source {source} size {size} count {count} timeout {timeout}
            * ping vrf {vrf} {addr} source {source} size {size} timeout {timeout} count {count}
            * ping vrf {vrf} {addr} source {source} timeout {timeout} count {count} size {size}
            * ping vrf {vrf} {addr} source {source} timeout {timeout} size {size} count {count}
            * ping vrf {vrf} {addr} size {size} count {count} source {source} timeout {timeout}
            * ping vrf {vrf} {addr} size {size} count {count} timeout {timeout} source {source}
            * ping vrf {vrf} {addr} size {size} source {source} count {count} timeout {timeout}
            * ping vrf {vrf} {addr} size {size} source {source} timeout {timeout} count {count}
            * ping vrf {vrf} {addr} size {size} timeout {timeout} count {count} source {source}
            * ping vrf {vrf} {addr} size {size} timeout {timeout} source {source} count {count}
            * ping vrf {vrf} {addr} timeout {timeout} count {count} source {source} size {size}
            * ping vrf {vrf} {addr} timeout {timeout} count {count} size {size} source {source}
            * ping vrf {vrf} {addr} timeout {timeout} source {source} count {count} size {size}
            * ping vrf {vrf} {addr} timeout {timeout} source {source} size {size} count {count}
            * ping vrf {vrf} {addr} timeout {timeout} size {size} count {count} source {source}
            * ping vrf {vrf} {addr} timeout {timeout} size {size} source {source} count {count}
            * ping vrf {vrf} {addr} count {count} source {source} size {size} timeout {timeout}
            * ping vrf {vrf} {addr} count {count} source {source} timeout {timeout} size {size}
            * ping vrf {vrf} {addr} count {count} size {size} source {source} timeout {timeout}
            * ping vrf {vrf} {addr} count {count} size {size} timeout {timeout} source {source}
            * ping vrf {vrf} {addr} count {count} timeout {timeout} source {source} size {size}
            * ping vrf {vrf} {addr} count {count} timeout {timeout} size {size} source {source}
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
            * ping {addr} size {size}
            * ping {addr} timeout {timeout}
            * ping {addr} source {source} timeout {timeout}
            * ping {addr} timeout {timeout} source {source}
            * ping {addr} size {size} timeout {timeout}
            * ping {addr} timeout {timeout} size {size}
            * ping {addr} count {count} source {source}
            * ping {addr} source {source} count {count}
            * ping {addr} source {source} size {size}
            * ping {addr} size {size} source {source}
            * ping {addr} count {count} timeout {timeout}
            * ping {addr} timeout {timeout} count {count}
            * ping {addr} count {count} size {size}
            * ping {addr} size {size} count {count}
            * ping {addr} count {count} size {size} timeout {timeout}
            * ping {addr} count {count} timeout {timeout} size {size}
            * ping {addr} size {size} count {count} timeout {timeout}
            * ping {addr} size {size} timeout {timeout} count {count}
            * ping {addr} timeout {timeout} count {count} size {size}
            * ping {addr} timeout {timeout} size {size} count {count}
            * ping {addr} count {count} source {source} timeout {timeout}
            * ping {addr} count {count} timeout {timeout} source {source}
            * ping {addr} source {source} count {count} timeout {timeout}
            * ping {addr} source {source} timeout {timeout} count {count}
            * ping {addr} timeout {timeout} count {count} source {source}
            * ping {addr} timeout {timeout} source {source} count {count}
            * ping {addr} count {count} source {source} size {size}
            * ping {addr} count {count} size {size} source {source}
            * ping {addr} source {source} count {count} size {size}
            * ping {addr} source {source} size {size} count {count}
            * ping {addr} size {size} count {count} source {source}
            * ping {addr} size {size} source {source} count {count}
            * ping {addr} source {source} size {size} timeout {timeout}
            * ping {addr} source {source} timeout {timeout} size {size}
            * ping {addr} size {size} source {source} timeout {timeout}
            * ping {addr} size {size} timeout {timeout} source {source}
            * ping {addr} timeout {timeout} source {source} size {size}
            * ping {addr} timeout {timeout} size {size} source {source}
            * ping {addr} source {source} count {count} size {size} timeout {timeout}
            * ping {addr} source {source} count {count} timeout {timeout} size {size}
            * ping {addr} source {source} size {size} count {count} timeout {timeout}
            * ping {addr} source {source} size {size} timeout {timeout} count {count}
            * ping {addr} source {source} timeout {timeout} count {count} size {size}
            * ping {addr} source {source} timeout {timeout} size {size} count {count}
            * ping {addr} size {size} count {count} source {source} timeout {timeout}
            * ping {addr} size {size} count {count} timeout {timeout} source {source}
            * ping {addr} size {size} source {source} count {count} timeout {timeout}
            * ping {addr} size {size} source {source} timeout {timeout} count {count}
            * ping {addr} size {size} timeout {timeout} count {count} source {source}
            * ping {addr} size {size} timeout {timeout} source {source} count {count}
            * ping {addr} timeout {timeout} count {count} source {source} size {size}
            * ping {addr} timeout {timeout} count {count} size {size} source {source}
            * ping {addr} timeout {timeout} source {source} count {count} size {size}
            * ping {addr} timeout {timeout} source {source} size {size} count {count}
            * ping {addr} timeout {timeout} size {size} count {count} source {source}
            * ping {addr} timeout {timeout} size {size} source {source} count {count}
            * ping {addr} count {count} source {source} size {size} timeout {timeout}
            * ping {addr} count {count} source {source} timeout {timeout} size {size}
            * ping {addr} count {count} size {size} source {source} timeout {timeout}
            * ping {addr} count {count} size {size} timeout {timeout} source {source}
            * ping {addr} count {count} timeout {timeout} source {source} size {size}
            * ping {addr} count {count} timeout {timeout} size {size} source {source}
            * ping vrf {vrf} {addr}
            * ping vrf {vrf} {addr} count {count}
            * ping vrf {vrf} {addr} source {source}
            * ping vrf {vrf} {addr} size {size}
            * ping vrf {vrf} {addr} timeout {timeout}
            * ping vrf {vrf} {addr} source {source} timeout {timeout}
            * ping vrf {vrf} {addr} timeout {timeout} source {source}
            * ping vrf {vrf} {addr} size {size} timeout {timeout}
            * ping vrf {vrf} {addr} timeout {timeout} size {size}
            * ping vrf {vrf} {addr} count {count} source {source}
            * ping vrf {vrf} {addr} source {source} count {count}
            * ping vrf {vrf} {addr} source {source} size {size}
            * ping vrf {vrf} {addr} size {size} source {source}
            * ping vrf {vrf} {addr} count {count} timeout {timeout}
            * ping vrf {vrf} {addr} timeout {timeout} count {count}
            * ping vrf {vrf} {addr} count {count} size {size}
            * ping vrf {vrf} {addr} size {size} count {count}
            * ping vrf {vrf} {addr} count {count} size {size} timeout {timeout}
            * ping vrf {vrf} {addr} count {count} timeout {timeout} size {size}
            * ping vrf {vrf} {addr} size {size} count {count} timeout {timeout}
            * ping vrf {vrf} {addr} size {size} timeout {timeout} count {count}
            * ping vrf {vrf} {addr} timeout {timeout} count {count} size {size}
            * ping vrf {vrf} {addr} timeout {timeout} size {size} count {count}
            * ping vrf {vrf} {addr} count {count} source {source} timeout {timeout}
            * ping vrf {vrf} {addr} count {count} timeout {timeout} source {source}
            * ping vrf {vrf} {addr} source {source} count {count} timeout {timeout}
            * ping vrf {vrf} {addr} source {source} timeout {timeout} count {count}
            * ping vrf {vrf} {addr} timeout {timeout} count {count} source {source}
            * ping vrf {vrf} {addr} timeout {timeout} source {source} count {count}
            * ping vrf {vrf} {addr} count {count} source {source} size {size}
            * ping vrf {vrf} {addr} count {count} size {size} source {source}
            * ping vrf {vrf} {addr} source {source} count {count} size {size}
            * ping vrf {vrf} {addr} source {source} size {size} count {count}
            * ping vrf {vrf} {addr} size {size} count {count} source {source}
            * ping vrf {vrf} {addr} size {size} source {source} count {count}
            * ping vrf {vrf} {addr} source {source} size {size} timeout {timeout}
            * ping vrf {vrf} {addr} source {source} timeout {timeout} size {size}
            * ping vrf {vrf} {addr} size {size} source {source} timeout {timeout}
            * ping vrf {vrf} {addr} size {size} timeout {timeout} source {source}
            * ping vrf {vrf} {addr} timeout {timeout} source {source} size {size}
            * ping vrf {vrf} {addr} timeout {timeout} size {size} source {source}
            * ping vrf {vrf} {addr} source {source} count {count} size {size} timeout {timeout}
            * ping vrf {vrf} {addr} source {source} count {count} timeout {timeout} size {size}
            * ping vrf {vrf} {addr} source {source} size {size} count {count} timeout {timeout}
            * ping vrf {vrf} {addr} source {source} size {size} timeout {timeout} count {count}
            * ping vrf {vrf} {addr} source {source} timeout {timeout} count {count} size {size}
            * ping vrf {vrf} {addr} source {source} timeout {timeout} size {size} count {count}
            * ping vrf {vrf} {addr} size {size} count {count} source {source} timeout {timeout}
            * ping vrf {vrf} {addr} size {size} count {count} timeout {timeout} source {source}
            * ping vrf {vrf} {addr} size {size} source {source} count {count} timeout {timeout}
            * ping vrf {vrf} {addr} size {size} source {source} timeout {timeout} count {count}
            * ping vrf {vrf} {addr} size {size} timeout {timeout} count {count} source {source}
            * ping vrf {vrf} {addr} size {size} timeout {timeout} source {source} count {count}
            * ping vrf {vrf} {addr} timeout {timeout} count {count} source {source} size {size}
            * ping vrf {vrf} {addr} timeout {timeout} count {count} size {size} source {source}
            * ping vrf {vrf} {addr} timeout {timeout} source {source} count {count} size {size}
            * ping vrf {vrf} {addr} timeout {timeout} source {source} size {size} count {count}
            * ping vrf {vrf} {addr} timeout {timeout} size {size} count {count} source {source}
            * ping vrf {vrf} {addr} timeout {timeout} size {size} source {source} count {count}
            * ping vrf {vrf} {addr} count {count} source {source} size {size} timeout {timeout}
            * ping vrf {vrf} {addr} count {count} source {source} timeout {timeout} size {size}
            * ping vrf {vrf} {addr} count {count} size {size} source {source} timeout {timeout}
            * ping vrf {vrf} {addr} count {count} size {size} timeout {timeout} source {source}
            * ping vrf {vrf} {addr} count {count} timeout {timeout} source {source} size {size}
            * ping vrf {vrf} {addr} count {count} timeout {timeout} size {size} source {source}
    """

    cli_command = [
        'ping {addr}',
        'ping {addr} count {count}',
        'ping {addr} source {source}',
        'ping {addr} size {size}',
        'ping {addr} timeout {timeout}',
        'ping {addr} source {source} timeout {timeout}',
        'ping {addr} timeout {timeout} source {source}',
        'ping {addr} size {size} timeout {timeout}',
        'ping {addr} timeout {timeout} size {size}',
        'ping {addr} count {count} source {source}',
        'ping {addr} source {source} count {count}',
        'ping {addr} source {source} size {size}',
        'ping {addr} size {size} source {source}',
        'ping {addr} count {count} timeout {timeout}',
        'ping {addr} timeout {timeout} count {count}',
        'ping {addr} count {count} size {size}',
        'ping {addr} size {size} count {count}',
        'ping {addr} count {count} size {size} timeout {timeout}',
        'ping {addr} count {count} timeout {timeout} size {size}',
        'ping {addr} size {size} count {count} timeout {timeout}',
        'ping {addr} size {size} timeout {timeout} count {count}',
        'ping {addr} timeout {timeout} count {count} size {size}',
        'ping {addr} timeout {timeout} size {size} count {count}',
        'ping {addr} count {count} source {source} timeout {timeout}',
        'ping {addr} count {count} timeout {timeout} source {source}',
        'ping {addr} source {source} count {count} timeout {timeout}',
        'ping {addr} source {source} timeout {timeout} count {count}',
        'ping {addr} timeout {timeout} count {count} source {source}',
        'ping {addr} timeout {timeout} source {source} count {count}',
        'ping {addr} count {count} source {source} size {size}',
        'ping {addr} count {count} size {size} source {source}',
        'ping {addr} source {source} count {count} size {size}',
        'ping {addr} source {source} size {size} count {count}',
        'ping {addr} size {size} count {count} source {source}',
        'ping {addr} size {size} source {source} count {count}',
        'ping {addr} source {source} size {size} timeout {timeout}',
        'ping {addr} source {source} timeout {timeout} size {size}',
        'ping {addr} size {size} source {source} timeout {timeout}',
        'ping {addr} size {size} timeout {timeout} source {source}',
        'ping {addr} timeout {timeout} source {source} size {size}',
        'ping {addr} timeout {timeout} size {size} source {source}',
        'ping {addr} source {source} count {count} size {size} timeout {timeout}',
        'ping {addr} source {source} count {count} timeout {timeout} size {size}',
        'ping {addr} source {source} size {size} count {count} timeout {timeout}',
        'ping {addr} source {source} size {size} timeout {timeout} count {count}',
        'ping {addr} source {source} timeout {timeout} count {count} size {size}',
        'ping {addr} source {source} timeout {timeout} size {size} count {count}',
        'ping {addr} size {size} count {count} source {source} timeout {timeout}',
        'ping {addr} size {size} count {count} timeout {timeout} source {source}',
        'ping {addr} size {size} source {source} count {count} timeout {timeout}',
        'ping {addr} size {size} source {source} timeout {timeout} count {count}',
        'ping {addr} size {size} timeout {timeout} count {count} source {source}',
        'ping {addr} size {size} timeout {timeout} source {source} count {count}',
        'ping {addr} timeout {timeout} count {count} source {source} size {size}',
        'ping {addr} timeout {timeout} count {count} size {size} source {source}',
        'ping {addr} timeout {timeout} source {source} count {count} size {size}',
        'ping {addr} timeout {timeout} source {source} size {size} count {count}',
        'ping {addr} timeout {timeout} size {size} count {count} source {source}',
        'ping {addr} timeout {timeout} size {size} source {source} count {count}',
        'ping {addr} count {count} source {source} size {size} timeout {timeout}',
        'ping {addr} count {count} source {source} timeout {timeout} size {size}',
        'ping {addr} count {count} size {size} source {source} timeout {timeout}',
        'ping {addr} count {count} size {size} timeout {timeout} source {source}',
        'ping {addr} count {count} timeout {timeout} source {source} size {size}',
        'ping {addr} count {count} timeout {timeout} size {size} source {source}',
        'ping vrf {vrf} {addr}',
        'ping vrf {vrf} {addr} count {count}',
        'ping vrf {vrf} {addr} source {source}',
        'ping vrf {vrf} {addr} size {size}',
        'ping vrf {vrf} {addr} timeout {timeout}',
        'ping vrf {vrf} {addr} source {source} timeout {timeout}',
        'ping vrf {vrf} {addr} timeout {timeout} source {source}',
        'ping vrf {vrf} {addr} size {size} timeout {timeout}',
        'ping vrf {vrf} {addr} timeout {timeout} size {size}',
        'ping vrf {vrf} {addr} count {count} source {source}',
        'ping vrf {vrf} {addr} source {source} count {count}',
        'ping vrf {vrf} {addr} source {source} size {size}',
        'ping vrf {vrf} {addr} size {size} source {source}',
        'ping vrf {vrf} {addr} count {count} timeout {timeout}',
        'ping vrf {vrf} {addr} timeout {timeout} count {count}',
        'ping vrf {vrf} {addr} count {count} size {size}',
        'ping vrf {vrf} {addr} size {size} count {count}',
        'ping vrf {vrf} {addr} count {count} size {size} timeout {timeout}',
        'ping vrf {vrf} {addr} count {count} timeout {timeout} size {size}',
        'ping vrf {vrf} {addr} size {size} count {count} timeout {timeout}',
        'ping vrf {vrf} {addr} size {size} timeout {timeout} count {count}',
        'ping vrf {vrf} {addr} timeout {timeout} count {count} size {size}',
        'ping vrf {vrf} {addr} timeout {timeout} size {size} count {count}',
        'ping vrf {vrf} {addr} count {count} source {source} timeout {timeout}',
        'ping vrf {vrf} {addr} count {count} timeout {timeout} source {source}',
        'ping vrf {vrf} {addr} source {source} count {count} timeout {timeout}',
        'ping vrf {vrf} {addr} source {source} timeout {timeout} count {count}',
        'ping vrf {vrf} {addr} timeout {timeout} count {count} source {source}',
        'ping vrf {vrf} {addr} timeout {timeout} source {source} count {count}',
        'ping vrf {vrf} {addr} count {count} source {source} size {size}',
        'ping vrf {vrf} {addr} count {count} size {size} source {source}',
        'ping vrf {vrf} {addr} source {source} count {count} size {size}',
        'ping vrf {vrf} {addr} source {source} size {size} count {count}',
        'ping vrf {vrf} {addr} size {size} count {count} source {source}',
        'ping vrf {vrf} {addr} size {size} source {source} count {count}',
        'ping vrf {vrf} {addr} source {source} size {size} timeout {timeout}',
        'ping vrf {vrf} {addr} source {source} timeout {timeout} size {size}',
        'ping vrf {vrf} {addr} size {size} source {source} timeout {timeout}',
        'ping vrf {vrf} {addr} size {size} timeout {timeout} source {source}',
        'ping vrf {vrf} {addr} timeout {timeout} source {source} size {size}',
        'ping vrf {vrf} {addr} timeout {timeout} size {size} source {source}',
        'ping vrf {vrf} {addr} source {source} count {count} size {size} timeout {timeout}',
        'ping vrf {vrf} {addr} source {source} count {count} timeout {timeout} size {size}',
        'ping vrf {vrf} {addr} source {source} size {size} count {count} timeout {timeout}',
        'ping vrf {vrf} {addr} source {source} size {size} timeout {timeout} count {count}',
        'ping vrf {vrf} {addr} source {source} timeout {timeout} count {count} size {size}',
        'ping vrf {vrf} {addr} source {source} timeout {timeout} size {size} count {count}',
        'ping vrf {vrf} {addr} size {size} count {count} source {source} timeout {timeout}',
        'ping vrf {vrf} {addr} size {size} count {count} timeout {timeout} source {source}',
        'ping vrf {vrf} {addr} size {size} source {source} count {count} timeout {timeout}',
        'ping vrf {vrf} {addr} size {size} source {source} timeout {timeout} count {count}',
        'ping vrf {vrf} {addr} size {size} timeout {timeout} count {count} source {source}',
        'ping vrf {vrf} {addr} size {size} timeout {timeout} source {source} count {count}',
        'ping vrf {vrf} {addr} timeout {timeout} count {count} source {source} size {size}',
        'ping vrf {vrf} {addr} timeout {timeout} count {count} size {size} source {source}',
        'ping vrf {vrf} {addr} timeout {timeout} source {source} count {count} size {size}',
        'ping vrf {vrf} {addr} timeout {timeout} source {source} size {size} count {count}',
        'ping vrf {vrf} {addr} timeout {timeout} size {size} count {count} source {source}',
        'ping vrf {vrf} {addr} timeout {timeout} size {size} source {source} count {count}',
        'ping vrf {vrf} {addr} count {count} source {source} size {size} timeout {timeout}',
        'ping vrf {vrf} {addr} count {count} source {source} timeout {timeout} size {size}',
        'ping vrf {vrf} {addr} count {count} size {size} source {source} timeout {timeout}',
        'ping vrf {vrf} {addr} count {count} size {size} timeout {timeout} source {source}',
        'ping vrf {vrf} {addr} count {count} timeout {timeout} source {source} size {size}',
        'ping vrf {vrf} {addr} count {count} timeout {timeout} size {size} source {source}',
    ]

    def cli(self, addr, vrf=None, count=None, source=None, size=None, timeout=None, output=None):

        if not output:
            cmd = []
            if addr and vrf:
                cmd.append('ping vrf {vrf} {addr}'.format(vrf=vrf, addr=addr))
            elif addr:
                cmd.append('ping {addr}'.format(addr=addr))
            if source:
                cmd.append('source {source}'.format(source=source))
            if count:
                cmd.append('count {count}'.format(count=count))
            if size:
                cmd.append('size {size}'.format(size=size))
            if timeout:
                cmd.append('timeout {timeout}'.format(timeout=timeout))
            cmd = ' '.join(cmd)
            out = self.device.execute(cmd)
        else:
            out = output


        ret_dict = {}
        result_per_line = []
        # Sending 10, 100-byte ICMP Echos to 21.1.1.1, timeout is 2 seconds:
        p1 = re.compile(r'Sending +(?P<repeat>\d+), +(?P<data_bytes>\d+)-byte +ICMP +Echos +to +(?P<address>[\S\s]+), +timeout +is +(?P<timeout>\d+) +seconds:')

        #Packet sent with a source address of 21.1.1.2
        p2 = re.compile(r'Packet +sent +with +a +source +address +of +(?P<source>[\S\s]+)')

        # !!!!!!!
        # !.UQM?&
        p3 = re.compile(r'[!\.UQM\?&]+')

        # Success rate is 100 percent (100/100), round-trip min/avg/max = 1/2/14 ms
        p4 = re.compile(r'Success +rate +is +(?P<success_percent>\d+) +percent +\((?P<received>\d+)\/(?P<send>\d+)\), +round-trip +min/avg/max *= *(?P<min>\d+)/(?P<max>\d+)/(?P<avg>\d+) +(?P<unit>\w+)')

        ping_dict = {}
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
            # Packet sent with a source address of 21.1.1.2
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


            # Sending 10, 100-byte ICMP Echos to 21.1.1.1, timeout is 2 seconds:
            m = p4.match(line)
            if m:
                group = m.groupdict()
                stat_dict = ping_dict.setdefault('statistics', {})
                stat_dict.update({'success_rate_percent': float(group['success_percent']),
                                  'received':int(group['received']),
                                  'send': int(group['send'])})

                round_dict = stat_dict.setdefault('round_trip', {})

                min_ms = float(group['min'])
                max_ms = float(group['max'])
                avg_ms = float(group['avg'])

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
