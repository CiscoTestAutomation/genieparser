"""
show_asp_drop.py
Parser for the following show command(s):
    * show asp drop
"""

import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                                Any, \
                                                Optional


# =============================================
# Schema for 'show asp drop'
# =============================================
class ShowAspDropSchema(MetaParser):
    """
    Schema for
         * show asp drop
    """
    schema = {
        'frame_drop': {
            Any(): {
              'counts': int,
            },
            'last_clearing': str,
        },
        'flow_drop': {
            'last_clearing': str,
        }
    }


# =============================================
# Parser for 'show asp drop'
# =============================================
class ShowAspDrop(ShowAspDropSchema):
    """Parser for
        * show asp drop
    """

    cli_command = 'show asp drop'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}

        # -----------------------------------------------
        # Regular expression patterns
        # -----------------------------------------------
        # Frame drop:
        #   Reverse-path verify failed (rpf-violated)                                   23
        #   Flow is denied by configured rule (acl-drop)                                29
        #   Slowpath security checks failed (sp-security-failed)                        11
        #   FP L2 rule drop (l2_acl)                                                    35
        #   FP no mcast output intrf (no-mcast-intrf)                                   31
        #
        # Last clearing: 10:43:33 EDT Mar 27 2019 by genie
        #
        # Flow drop:
        #
        # Last clearing: 10:43:33 EDT Mar 27 2019 by genie

        # -----------------------------------------------
        # Parse the output
        # -----------------------------------------------
