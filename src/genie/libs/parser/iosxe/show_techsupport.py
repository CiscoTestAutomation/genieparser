"""show_techsupport.py
   IOSXE parsers for the following show commands:
     *  show tech-support | i show
"""
# python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie import parsergen
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional, Use, Default

# pyATS
# import parser utils
from genie.libs.parser.utils.common import Common

class ShowTechSupportIncludeShowSchema(MetaParser):
    """Schema for show tech-support | include show"""

    schema = {
        'cli': {
            Any(): {
                'command': str,
            },
        },
    }

class ShowTechSupportIncludeShow(ShowTechSupportIncludeShowSchema):
    """Parser for show tech-support | include show"""

    cli_command = 'show tech-support | include {show_option}'

    def cli(self, show_option="",output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(show_option=show_option),timeout=200)

        # ------------------ show vlan virtual-port -------------------
        # ------------------ show interfaces history ------------------
        p1 = re.compile(r"^-+\s(?P<command>[\w\.\:\-\s]+)\s-+$")

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # ------------------ show vlan virtual-port -------------------
            # ------------------ show interfaces history ------------------
            m = p1.match(line)
            if m:
                group = m.groupdict()
                cli_dict = ret_dict.setdefault('cli', {})
                cmd_dict = cli_dict.setdefault((group['command'].strip()).replace(' ', '_').replace('-', '_'), {})
                cmd_dict['command'] = group['command']
               
        return ret_dict            