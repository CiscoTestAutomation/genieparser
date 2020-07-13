"""show_bfd.py

JUNOS parsers for the following commands:
    * show bfd session
"""

import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional, Use, Schema
from genie.metaparser.util.exceptions import SchemaTypeError

class ShowBFDSessionSchema(MetaParser):
    """ Schema for
        * show bfd session
    """

    def validate_bfd_session(value):
        if not isinstance(value, list):
            raise SchemaTypeError('BFD Session not a list')
    
        bfd_session = Schema({
            "session-neighbor": str,
            "session-state": str,
            Optional("session-interface"): str,
            "session-detection-time": str,
            "session-transmission-interval": str,
            "session-adaptive-multiplier": str,
        })
    
        for item in value:
            bfd_session.validate(item)
        return value

    schema = {
        "bfd-session-information": {
            "bfd-session": Use(validate_bfd_session)
        }
    }

class ShowBFDSession(ShowBFDSessionSchema):
    """ Parser for:
        * show bfd session
    """

    cli_command = 'show bfd session'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # 10.0.0.1                        Operational Open          26         DU
        # 10.0.0.2               Up        ge-0/0/0.0     1.500     0.500        3
        p1 = re.compile(r'^(?P<session_neighbor>\S+) +'
                        r'(?P<session_state>\S+)'
                        r'( +(?P<session_interface>\S+))? +'
                        r'(?P<session_detection_time>[\d\.]+) +'
                        r'(?P<session_transmission_interval>[\d\.]+) +'
                        r'(?P<session_adaptive_multiplier>\S+)$')


        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                session_list = ret_dict.setdefault("bfd-session-information", {}).\
                    setdefault("bfd-session", [])
                session_list.append(
                    {k.replace('_', '-'):v for k, v in group.items() if v is not None}
                )

        return ret_dict