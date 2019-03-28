"""  show_mpls.py
   supported commands:
        *  show mpls l2transport vc detail
"""

import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                               Any, \
                                               Optional

from genie.libs.parser.iosxe.show_mpls import ShowMplsL2TransportDetail as ShowMplsL2TransportDetail_iosxe


# ================================================
#   Show mpls l2transport vc detail
# ================================================
class ShowMplsL2TransportDetail(ShowMplsL2TransportDetail_iosxe):
    """
    Parser for show mpls l2transport vc detail
    """
    pass