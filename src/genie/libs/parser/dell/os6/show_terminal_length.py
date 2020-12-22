'''
Author: Knox Hutchinson
Contact: https://dataknox.dev
https://twitter.com/data_knox
https://youtube.com/c/dataknox
'''
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Optional
import re

# ======================================================
# Schema for 'show terminal length'
# ======================================================


class ShowTerminalLengthSchema(MetaParser):
    schema = {
        'length': int
    }


class ShowTerminalLength(ShowTerminalLengthSchema):
    """Parser for show terminal length on Dell PowerSwitch OS6 devices
    parser class - implements detail parsing mechanisms for cli output.
    """
    cli_command = 'show terminal length'

    """
    terminal length................................ 24
    """

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
       
        result_dict = {}

        p0 = re.compile(r'^terminal\slength\.+\s(?P<length>\d+)')

        for line in out.splitlines():
            line = line.strip()

            m = p0.match(line)
            if m:
                length = m.groupdict()['length']
                result_dict['length'] = int(length)
                continue
        return result_dict