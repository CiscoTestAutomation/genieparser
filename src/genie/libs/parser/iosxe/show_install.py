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
        'location': {
            Any(): {
                'pkg_state': {
                    Any(): {
                        'type': str,
                        'state': str,
                        'filename_version': str,
                    }
                },
                'auto_abort_timer': str,
                Optional('time_before_rollback'): str,
            },
        },
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
        # [ R0 ] Installed Package(s) Information:
        p1 = re.compile(r'^\[ +(?P<location>[\S ]+)\] +Installed Package'
                        r'\(s\) +Information:$')
        # SMU   U    bootflash:utah.bm.smu.may15.bin
        # IMG   C    10.69.1.0.66982
        p2 = re.compile(r'^(?P<type>\S+) + (?P<state>\w) +(?P<filename_version>\S+)$')
        
        # Auto abort timer: active on install_activate, time before rollback - 01:49:42
        p3 = re.compile(r'^Auto +abort +timer: +(?P<auto_abort_timer>[\S ]+), +'
                        r'time +before +rollback +\- +(?P<time_before_rollback>\S+)$')

        # Auto abort timer: active on install_activate
        p4 = re.compile(r'^Auto +abort +timer: +(?P<auto_abort_timer>[\S ]+)$')

        for line in out.splitlines():
            line = line.strip()
            
            # [ R0 ] Installed Package(s) Information:
            m = p1.match(line)
            if m:
                group = m.groupdict()
                location = group['location'].strip()
                location_dict = ret_dict.setdefault('location', {}). \
                    setdefault(location, {})
                continue

            # SMU   U    bootflash:utah.bm.smu.may15.bin
            # IMG   C    10.69.1.0.66982
            m = p2.match(line)
            if m:
                group = m.groupdict()
                index += 1
                install_dict = location_dict.setdefault('pkg_state', {}). \
                    setdefault(index, {})
                install_dict.update({'type': group['type']})
                install_dict.update({'state': group['state']})
                install_dict.update({'filename_version': group['filename_version']})
                continue
            
            # Auto abort timer: active on install_activate, time before rollback - 01:49:42
            m = p3.match(line)
            if m:
                group = m.groupdict()
                location_dict.update({'auto_abort_timer': group['auto_abort_timer']})
                time_before_rollback = group.get('time_before_rollback', None)
                if time_before_rollback:
                    location_dict.update({'time_before_rollback': time_before_rollback})
                continue
            
            # Auto abort timer: active on install_activate
            m = p4.match(line)
            if m:
                group = m.groupdict()
                location_dict.update({'auto_abort_timer': group['auto_abort_timer']})
                continue

        return ret_dict

            