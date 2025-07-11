'''show_logging.py

IOSXE parsers for the following show commands:

    * show logging onboard slot {slot} status
'''

import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional, Or


class ShowLoggingOnboardSlotStatusSchema(MetaParser):
    """Schema for show logging onboard slot <slot> status"""

    schema = {
        Any(): {
            'path': str,
            'cli_enable_status': str,
        },
    }

class ShowLoggingOnboardSlotStatus(ShowLoggingOnboardSlotStatusSchema):
    """Parser for show logging onboard slot <slot> status"""

    cli_command = 'show logging onboard slot {slot} status'

    def cli(self, slot = "", output=None):
        if output is None:
            #Build the command
            cmd = self.cli_command.format(slot = slot)
            output = self.device.execute(cmd)

        ret_dict = {}
        current_app = None

        # Application Uptime:
        p1 = re.compile(r'^(?P<application>(Application.*?):)$')

        # Path: /obfl_cc/1/
        p2 = re.compile(r'^\s*Path:?\s?(?P<path>.*)$')

        # Cli enable status: enabled
        p3 = re.compile(r'^\s*Cli enable status:?\s?(?P<cli_enable_status>.*)$')

        for line in output.splitlines():
            # remove any trailing or leading spaces
            line = line.strip()

            # Application Uptime:
            m = p1.match(line)
            if m:
                group = m.groupdict()
                current_app = group['application']
                ret_dict.setdefault(current_app, {})
                continue

            # Path: /obfl_cc/1/
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict[current_app]['path'] = group['path']
                continue

            # Cli enable status: enabled
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict[current_app]['cli_enable_status'] = group['cli_enable_status']
                continue

        return ret_dict
