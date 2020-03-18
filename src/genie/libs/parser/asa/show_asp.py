"""
show_asp.py
Parser for the following show command(s):
    * show asp drop
"""

import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                                Any, \
                                                Optional


# =============================================
# Schema for 'show asp drop'
# =============================================
class ShowAspDropSchema(MetaParser):
    """
    Schema for
         * show asp drop
    """
    schema = {
        'frame_drop': {
            Any(): int,
            'last_clearing': str,
        },
        'flow_drop': {
            Any(): int,
            'last_clearing': str,
        }
    }


# =============================================
# Parser for 'show asp drop'
# =============================================
class ShowAspDrop(ShowAspDropSchema):
    """Parser for
        * show asp drop
    """

    cli_command = 'show asp drop'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}

        # -----------------------------------------------
        # Regular expression patterns
        # -----------------------------------------------
        # Frame drop:
        p0 = re.compile(r'^Frame drop:$')

        #   Reverse-path verify failed (rpf-violated)                                   23
        p1 = re.compile(r'^.*\((?P<drop>\S+)\)\s+(?P<counts>\d+)$')

        # Last clearing: 10:43:33 EDT Mar 27 2019 by genie
        p2 = re.compile(r'^Last\s+clearing:\s+(?P<last_clearing>[\s\S]+)$')

        # Flow drop:
        p3 = re.compile(r'^Flow drop:$')

        # -----------------------------------------------
        # Parse the output
        # -----------------------------------------------
        for line in out.splitlines():
            line = line.strip()

            # Frame drop:
            m = p0.match(line)
            if m:
                frame_drop_dict = parsed_dict.setdefault('frame_drop', {})
                continue

            # Flow drop:
            m = p3.match(line)
            if m:
                flow_drop_dict = parsed_dict.setdefault('flow_drop', {})
                continue

            #   Reverse-path verify failed (rpf-violated)                                   23
            m = p1.match(line)
            if m:
                group = m.groupdict()
                if 'flow_drop' in parsed_dict:
                    flow_drop_dict[group['drop']] = int(group['counts'])
                else:
                    frame_drop_dict[group['drop']] = int(group['counts'])
                continue

            #  Last clearing: 10:43:33 EDT Mar 27 2019 by genie
            m = p2.match(line)
            if m:
                val = m.groupdict()['last_clearing']
                if 'flow_drop' in parsed_dict:
                    flow_drop_dict['last_clearing'] = val
                else:
                    frame_drop_dict['last_clearing'] = val
                continue

        return parsed_dict




