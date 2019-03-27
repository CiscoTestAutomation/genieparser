''' show_l2vpn.py

IOS parsers for the following show commands:

    * show l2vpn vfi
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                         Any, \
                                         Optional, \
                                         Or, \
                                         And, \
                                         Default, \
                                         Use

# import iosxe parser
from genie.libs.parser.iosxe.show_l2vpn import ShowL2vpnVfi as ShowL2vpnVfi_iosxe


# ===========================
# Parser for 'show l2vpn vfi'
# ===========================
class ShowL2vpnVfi(ShowL2vpnVfi_iosxe):
    """Parser for show l2vpn vfi
    """
    pass
