""" show_system_ntp_all.py
    supports commands:
        * show system ntp all
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

# parser utils
from genie.libs.parser.utils.common import Common

# =============================================
# Parser for 'show system ntp all'
# =============================================


class ShowSystemNtpAllSchema(MetaParser):
    """schema for show system ntp all"""

    schema = {
        'clock_state': {
            'system_status': {
                'configured': str,
                'admin_status': str,
                'server_enabled': str,
                'clock_source': str,
                'auth_check': str,
                'current_date_time': str,
                'stratum': int,
                'oper_status': str,
                'server_authenticate': str,
            }
        },
        'peer': {
            Any(): { # == group['remote']
                'local_mode': {
                    Any(): { # == 'client'
                        'state': str,
                        'refid': str,
                        Optional('stratum'): int, # values: '-' and 4
                        'type': str,
                        'poll': int,
                        'reach': str, # TBD
                        'offset': float,
                        'a': str,
                        'router': str,
                        'remote': str,
                    }
                }
            }
        },
    }


class ShowSystemNtpAll(ShowSystemNtpAllSchema):
    """ Parser for show system ntp all"""

    cli_command = 'show system ntp all'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}






