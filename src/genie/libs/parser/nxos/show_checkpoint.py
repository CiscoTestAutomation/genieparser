""" show_checkpoint.py

NXOS parsers for the following show commands:
    * 'show checkpoint summary'
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Or, And,\
                                         Default, Use


# =====================================
# Parser for 'show checkpoint summary'
# =====================================
class ShowCheckpointSummarySchema(MetaParser):    
    """Schema for show checkpoint summary"""
    schema = {'checkpoint':
                {Any():
                    {'created_by': str,
                     'created_time': str,
                     'size': int,
                     'description': str}
                },
            }

class ShowCheckpointSummary(ShowCheckpointSummarySchema):
    """Parser for show checkpoint summary"""
    cli_command = 'show checkpoint summary'

    def cli(self, output=None):

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        ck_dict = {}

        for line in out.splitlines():
            line = line.strip()
            # 1) checkpoint1:
            p1 = re.compile(r'^\d+\) +(?P<id>[\s\w\.\-]+):$')
            m = p1.match(line)
            if m:
                if 'checkpoint' not in ck_dict:
                    ck_dict['checkpoint'] = {}

                id = m.groupdict()['id']
                if id not in ck_dict['checkpoint']:
                    ck_dict['checkpoint'][id] = {}
                continue

            # Created by admin
            p2 = re.compile(r'^Created +by +(?P<user>[\s\w\.\-\:]+)$')
            m = p2.match(line)
            if m:
                ck_dict['checkpoint'][id]['created_by'] = m.groupdict()['user']
                continue

            # Created at Tue, 22:13:49 20 Nov 2017
            p3 = re.compile(r'^Created +at +(?P<time>[\s\w\.\-\:\,]+)$')
            m = p3.match(line)
            if m:
                ck_dict['checkpoint'][id]['created_time'] = \
                    m.groupdict()['time']
                continue

            # Size is 25,671 bytes
            p4 = re.compile(r'^Size +is +(?P<size>[,\d]+) +bytes$')
            m = p4.match(line)
            if m:
                ck_dict['checkpoint'][id]['size'] = \
                    int(m.groupdict()['size'].replace(',', ''))
                continue

            # Description: Created by Feature Manager.
            p5 = re.compile(r'^Description: +(?P<desc>[\s\w\.\-\:]+)$')
            m = p5.match(line)
            if m:
                ck_dict['checkpoint'][id]['description'] = \
                    m.groupdict()['desc']
                continue
        return ck_dict
