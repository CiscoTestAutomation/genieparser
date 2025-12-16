"""show_fcs.py
   IOSXE parsers for the following show commands:
     * show fcs-threshold
"""
#python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema,Any,Optional,Or,And,Default,Use

# ==================================================
# Schema for 'show fcs-threshold'
# ==================================================
class ShowFcsThresholdSchema(MetaParser):
    """Schema for show fcs-threshold"""

    schema = {
        'port': {
            Any(): {
                'fcs_threshold': int,
            },
        },
    }

# ==================================================
# Parser for 'show fcs-threshold'
# ==================================================
class ShowFcsThreshold(ShowFcsThresholdSchema):
    """Parser for show fcs-threshold"""

    cli_command = 'show fcs-threshold'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # initial return dictionary
        ret_dict = {}

        # Te1/1           8
        p1 = re.compile(r'^(?P<port>\S+)\s+(?P<fcs_threshold>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            # Te1/1           8
            m = p1.match(line)
            if m:
                group = m.groupdict()
                port = group['port']
                fcs_threshold = int(group['fcs_threshold'])

                port_dict = ret_dict.setdefault('port', {}).setdefault(port, {})
                port_dict['fcs_threshold'] = fcs_threshold
                continue

        return ret_dict