from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any
from pprint import pprint
import re


# ===============================================
# Schema for 'show sdwan bfd summary'
# ===============================================

class ShowSdwanBfdSummarySchema(MetaParser):

    """ Schema for "show sdwan bfd summary" command """

    schema = {
        "sessions_total": str,
        "sessions_up": str,
        "sessions_max": str,
        "sessions_flap": str,
        "poll_interval": str,
    }

# ===============================================
# Parser for 'show sdwan bfd summary'
# ===============================================

class ShowSdwanBfdSummary(ShowSdwanBfdSummarySchema):

    """ Parser for "show sdwan bfd summary" """

    cli_command = "show sdwan bfd summary"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
    
        parsed_dict = {}

        # sessions-total         8
        p1 = re.compile(
            r"^sessions-total\s+(?P<sessions_total>\S+)"
        )

        # sessions-up            8
        p2 = re.compile(
            r"^sessions-up\s+(?P<sessions_up>\S+)"
        )

        # sessions-max           10
        p3 = re.compile(
            r"^sessions-max\s+(?P<sessions_max>\S+)"
        )

        # sessions-flap          121
        p4 = re.compile(
            r"^sessions-flap\s+(?P<sessions_flap>\S+)"
        )

        # poll-interval          120000
        p5 = re.compile(
            r"^poll-interval\s+(?P<poll_interval>\S+)"
        )

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                parsed_dict['sessions_total'] = m.groupdict()['sessions_total']
                continue

            m = p2.match(line)
            if m:
                parsed_dict['sessions_up'] = m.groupdict()['sessions_up']
                continue

            m = p3.match(line)
            if m:
                parsed_dict['sessions_max'] = m.groupdict()['sessions_max']
                continue

            m = p4.match(line)
            if m:
                parsed_dict['sessions_flap'] = m.groupdict()['sessions_flap']
                continue

            m = p5.match(line)
            if m:
                parsed_dict['poll_interval'] = m.groupdict()['poll_interval']
                continue

        return parsed_dict

