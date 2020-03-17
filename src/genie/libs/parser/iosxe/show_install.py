"""show_install.py
   supported commands:
     *  show install summary
"""

# Python
import re
import random

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (Schema,
                                                Any,
                                                Optional)

# import parser utils
from genie.libs.parser.utils.common import Common


class ShowInstallSummarySchema(MetaParser):
    """Schema for show install summary"""
    schema = {
        Any(): {
            'type': str,
            'state': str,
            'filename_version': str,
        },
        'auto_abort_timer': str,
        'time_before_rollback': str,
    }

class ShowInstallSummary(ShowInstallSummarySchema):
    """Parser for show install summary"""

    cli_command = 'show install summary'

    def cli(self, output=None):
        if output is None:
            # get output from device
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}
        index = 0
        # initial regexp pattern
        # SMU   U    bootflash:utah.bm.smu.may15.bin
        # IMG   C    17.1.1.0.66982
        p1 = re.compile(r'^(?P<type>\S+) + (?P<state>\w) +(?P<filename_version>\S+)$')
        
        # Auto abort timer: active on install_activate, time before rollback - 01:49:42
        p2 = re.compile(r'^Auto +abort +timer: +(?P<auto_abort_timer>[\S ]+), +'
                        r'time +before +rollback +\- +(?P<time_before_rollback>\S+)$')

        for line in out.splitlines():
            line = line.strip()
            
            # SMU   U    bootflash:utah.bm.smu.may15.bin
            # IMG   C    17.1.1.0.66982
            m = p1.match(line)
            if m:
                group = m.groupdict()
                index += 1
                install_dict = ret_dict.setdefault(index, {})
                install_dict.update({'type': group['type']})
                install_dict.update({'state': group['state']})
                install_dict.update({'filename_version': group['filename_version']})
                continue
            
            # Auto abort timer: active on install_activate, time before rollback - 01:49:42
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({'auto_abort_timer': group['auto_abort_timer']})
                ret_dict.update({'time_before_rollback': group['time_before_rollback']})
                continue

        return ret_dict

            