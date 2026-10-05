""" show_candidate.py

NXOS parsers for the following show commands:
    * 'show candidate summary'
    * 'show candidate summary committed'
    * 'show candidate summary pending'
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import ListOf, Optional, Or


# ======================================
# Parser for 'show candidate summary'
# ======================================
class ShowCandidateSummarySchema(MetaParser):
    """Schema for:
        * show candidate summary
        * show candidate summary committed
        * show candidate summary pending
    """

    schema = {
        'candidate_summary': ListOf(Or(
            {
                'session_name': str,
                'created_timestamp': str,
                'created_user': str,
                'current_last_user': str,
                'last_action_timestamp': str,
                'last_action_terminal': str,
                'session_state': str,
                Optional('commit_id'): int,
                Optional('commit_description'): str,
            },
            {
                'commit_id': int,
                'commit_description': str,
                Optional('created_timestamp'): str,
                Optional('session_name'): str,
                Optional('created_user'): str,
                Optional('current_last_user'): str,
                Optional('last_action_timestamp'): str,
                Optional('last_action_terminal'): str,
                Optional('session_state'): str,
            },
        )),
    }


class ShowCandidateSummary(ShowCandidateSummarySchema):
    """Parser for:
        * show candidate summary
        * show candidate summary committed
        * show candidate summary pending
    """

    cli_command = [
        'show candidate summary',
        'show candidate summary committed',
        'show candidate summary pending',
    ]

    def cli(self, command, output=None):
        if output is None:
            output = self.device.execute(command)

        ret_dict = {}
        current_entry = None

        # Created Timestamp            : 04:12:21 31 Aug 2026
        p1 = re.compile(
            r'^Created +Timestamp +: +(?P<created_timestamp>'
            r'\d{2}:\d{2}:\d{2} +\d{1,2} +'
            r'(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) +'
            r'\d{4})$')

        # Session Name                 : force-sessionnqanWT9Y
        p2 = re.compile(r'^Session +Name +: +(?P<session_name>\S+)$')

        # Created User                 : admin
        p3 = re.compile(r'^Created +User +: +(?P<created_user>\S+)$')

        # Current/Last user            : admin
        p4 = re.compile(r'^Current/Last +user +: +(?P<current_last_user>\S+)$')

        # Last Action Timestamp        : 04:12:32 31 Aug 2026
        p5 = re.compile(
            r'^Last +Action +Timestamp +: +(?P<last_action_timestamp>'
            r'\d{2}:\d{2}:\d{2} +\d{1,2} +'
            r'(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) +'
            r'\d{4})$')

        # Last Action Terminal         : /dev/pts/27
        p6 = re.compile(
            r'^Last +Action +Terminal +: +'
            r'(?P<last_action_terminal>\S+)$')

        # Session State                : PENDING
        p7 = re.compile(r'^Session +State +: +(?P<session_state>\S+)$')

        # commit ID                    : 2000001124
        p8 = re.compile(r'^commit +ID +: +(?P<commit_id>\d+)$')

        # commit Description           :
        p9 = re.compile(
            r'^commit +Description +: *'
            r'(?P<commit_description>[^\r\n]*)$')

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            # Created Timestamp            : 04:12:21 31 Aug 2026
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                if (current_entry is None or
                        'created_timestamp' in current_entry or
                        'session_state' in current_entry):
                    current_entry = {}
                    ret_dict.setdefault('candidate_summary', []).append(
                        current_entry)

                current_entry['created_timestamp'] = groups['created_timestamp']
                continue

            # Session Name                 : force-sessionnqanWT9Y
            m = p2.match(line)
            if m and current_entry is not None:
                groups = m.groupdict()
                current_entry['session_name'] = groups['session_name']
                continue

            # Created User                 : admin
            m = p3.match(line)
            if m and current_entry is not None:
                groups = m.groupdict()
                current_entry['created_user'] = groups['created_user']
                continue

            # Current/Last user            : admin
            m = p4.match(line)
            if m and current_entry is not None:
                groups = m.groupdict()
                current_entry['current_last_user'] = groups['current_last_user']
                continue

            # Last Action Timestamp        : 04:12:32 31 Aug 2026
            m = p5.match(line)
            if m and current_entry is not None:
                groups = m.groupdict()
                current_entry['last_action_timestamp'] = \
                    groups['last_action_timestamp']
                continue

            # Last Action Terminal         : /dev/pts/27
            m = p6.match(line)
            if m and current_entry is not None:
                groups = m.groupdict()
                current_entry['last_action_terminal'] = \
                    groups['last_action_terminal']
                continue

            # Session State                : PENDING
            m = p7.match(line)
            if m and current_entry is not None:
                groups = m.groupdict()
                current_entry['session_state'] = groups['session_state']
                continue

            # commit ID                    : 2000001124
            m = p8.match(line)
            if m:
                groups = m.groupdict()
                if current_entry is None or 'commit_id' in current_entry:
                    current_entry = {}
                    ret_dict.setdefault('candidate_summary', []).append(
                        current_entry)

                current_entry['commit_id'] = int(groups['commit_id'])
                continue

            # commit Description           :
            m = p9.match(line)
            if m and current_entry is not None:
                groups = m.groupdict()
                current_entry['commit_description'] = \
                    groups['commit_description']
                continue

        return ret_dict
