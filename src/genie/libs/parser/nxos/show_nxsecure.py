"""show_nxsecure.py

NXOS parsers for the following show commands:
    * show nxsecure status
"""

import re

from genie.metaparser import MetaParser


# ====================================================================
# Schema for 'show nxsecure status'
# ====================================================================
class ShowNxsecureStatusSchema(MetaParser):
    """Schema for show nxsecure status"""

    schema = {
        'tetragon_agent_status': str,
    }


# ====================================================================
# Parser for 'show nxsecure status'
# ====================================================================
class ShowNxsecureStatus(ShowNxsecureStatusSchema):
    """Parser for show nxsecure status"""

    cli_command = 'show nxsecure status'

    def cli(self, command='', output=None, **kwargs):
        if output is None:
            output = self.device.execute(command or self.cli_command)

        ret_dict = {}

        # Tetragon Agent Status: Running
        p1 = re.compile(r'^Tetragon +Agent +Status: +(?P<tetragon_agent_status>\S+)$')

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            # Tetragon Agent Status: Running
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                ret_dict.update({
                    'tetragon_agent_status': groups['tetragon_agent_status'],
                })
                continue

        return ret_dict
