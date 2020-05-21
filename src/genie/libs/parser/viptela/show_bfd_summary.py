from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any
from pprint import pprint
import re


# ===============================================
# Schema for 'show bfd summary'
# ===============================================

class ShowBfdSummarySchema(MetaParser):

    """ Schema for "show bfd summary" command """

    schema = {
        "sessions_total": int,
        "sessions_up": int,
        "sessions_max": int,
        "sessions_flap": int,
        "poll_interval": int,
    }

# ===============================================
# Parser for 'show bfd summary'
# ===============================================

class ShowBfdSummary(ShowBfdSummarySchema):

    """ Parser for "show bfd summary" """
    
    exclude = []
    
    cli_command = "show bfd summary"

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
                parsed_dict['sessions_total'] = int(m.groupdict()['sessions_total'])
                continue

            m = p2.match(line)
            if m:
                parsed_dict['sessions_up'] = int(m.groupdict()['sessions_up'])
                continue

            m = p3.match(line)
            if m:
                parsed_dict['sessions_max'] = int(m.groupdict()['sessions_max'])
                continue

            m = p4.match(line)
            if m:
                parsed_dict['sessions_flap'] = int(m.groupdict()['sessions_flap'])
                continue

            m = p5.match(line)
            if m:
                parsed_dict['poll_interval'] = int(m.groupdict()['poll_interval'])
                continue

        return parsed_dict

