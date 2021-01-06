"""
IOSXE C9200 parsers for the following show commands:
    * show environment all
"""
# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional

# import iosxe c9300 parser
from genie.libs.parser.iosxe.c9300.show_platform import ShowEnvironmentAll as ShowEnvironmentAll_C9300

class ShowEnvironmentAllSchema(ShowEnvironmentAll_C9300):
    """Schema for show environment all"""
    schema = {
        'switch': {
            Any(): {
                'fan': {
                    Any(): {
                        'state': str,
                        Optional('direction'): str,
                        Optional('speed'): int,
                    },
                },
                'power_supply': {
                    Any(): {
                        Optional('state'): str,
                        Optional('pid'): str,
                        Optional('serial_number'): str,
                        'status': str,
                        Optional('system_power'): str,
                        Optional('poe_power'): str,
                        Optional('watts'): str
                    }
                },
                'system_temperature_state': str,
                Optional('inlet_temperature'): {
                    'value': str,
                    'state': str,
                    'yellow_threshold': str,
                    'red_threshold': str
                },
                Optional('outlet_temperature'): {
                    'value': str,
                    'state': str,
                    'yellow_threshold': str,
                    'red_threshold': str
                },
                Optional('hotspot_temperature'): {
                    'value': str,
                    'state': str,
                    'yellow_threshold': str,
                    'red_threshold': str
                },
                Optional('asic_temperature'): {
                    'value': str,
                    'state': str,
                    'yellow_threshold': str,
                    'red_threshold': str
                },
            },
        },
    }


class ShowEnvironmentAll(ShowEnvironmentAllSchema):
    """Parser for show environment all"""
    pass