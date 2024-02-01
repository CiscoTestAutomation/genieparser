''' show_qfp.py
IOSXE parsers for the following show commands:

    * show qfp drops thresholds

'''

# Python
import re
import logging

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional
# genie.parsergen
try:
    import genie.parsergen
except (ImportError, OSError):
    pass


class ShowQfpDropsThresholdsSchema(MetaParser):
    """Schema for show qfp drops thresholds"""

    schema = {
        Optional('thresholds'): {
            Any(): int
        },
    }

class ShowQfpDropsThresholds(ShowQfpDropsThresholdsSchema):
    """
    Parser for
        show qfp drops thresholds
    """

    cli_command = 'show qfp drops thresholds'

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        # total    3
        # 4       40
        p1 = re.compile(r'^(?P<drop_id>total|\d+)\s+(?P<threshold>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            # total    3
            # 4       40
            m = p1.match(line)
            if m:
                group = m.groupdict()
                thresholds_dict = ret_dict.setdefault('thresholds', {})
                thresholds_dict[group['drop_id']] = int(group['threshold'])
                continue

        return ret_dict

