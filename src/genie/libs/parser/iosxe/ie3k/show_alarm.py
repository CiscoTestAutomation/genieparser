''' show_alarm.py
IOSXE parsers for the following show commands for IE3K:
    * show facility-alarm status
'''

import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

# =============================================
# Schema for 'show facility-alarm status'
# =============================================

class ShowFacilityAlarmStatusSchema(MetaParser):
    '''Schema for show facility-alarm status'''
    schema = {
        'alarms': {
            Any(): {
                int: {
                   Optional('severity'): str,
                   Optional('description'): str,
                   Optional('relay'): str,
                   Optional('time'): str,
            },
        },
    },
}


# =============================================
# Parser for 'show facility-alarm status'
# =============================================

class ShowFacilityAlarmStatus(ShowFacilityAlarmStatusSchema):
    '''Parser for show facility-alarm status'''
    cli_command = 'show facility-alarm status'

    def cli(self, output=None):
        if output is None:           
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}
        alarms = ret_dict.setdefault('alarms', {})

        # Source                 Severity Description                         Relay    Time
        p1 = re.compile(r'^\s*Source\s+Severity\s+Description\s+Relay\s+Time$')

        # RIO6                     MAJOR    1 Temp above max primary thresh     MAJ      Feb 08 1970 02:20:21
        # stack-of-3 1             MAJOR    1 Temp above max primary thresh     MAJ      Jun 27 2025 16:14:39
        p2 = re.compile(
            r'^(?P<source>.+?)\s{2,}'           # Source (non-greedy) until 2+ blanks
            r'(?P<severity>\S+)\s{2,}'          # Severity
            r'(?P<description>.+?)\s{2,}'       # Description (non-greedy) until 2+ blanks
            r'(?P<relay>\S+)\s+'                # Relay
            r'(?P<time>.+)$'                    # Time
        )

        for line in out.splitlines():
            line = line.strip()
            if not line or p1.match(line):
                continue

            m = p2.match(line)
            if not m:
                continue

            g = m.groupdict()

            # Ensure a bucket exists for this source
            src_key = g['source']
            src_bucket = alarms.setdefault(src_key, {})

            # Next ordinal index inside the bucket
            next_idx = len(src_bucket) + 1

            src_bucket[next_idx] = {
                'severity':    g['severity'],
                'description': g['description'].strip(),
                'relay':       g['relay'],
                'time':        g['time'],
            }

        return ret_dict       
