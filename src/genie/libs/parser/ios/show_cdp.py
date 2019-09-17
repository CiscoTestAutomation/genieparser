''' show_cdp.py
    Supported commands:
        * show cdp neighbors
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

# import iosxs parser
from genie.libs.parser.iosxe.show_cdp import ShowCdpNeighbors as ShowCdpNeighbors_iosxe


class ShowCdpNeighbors(ShowCdpNeighbors_iosxe):
    """Parser for show cdp all neighbors"""

    pass
