''' show_l2vpn.py

IOS parsers for the following show commands:

    * show l2vpn vfi
    * show l2vpn service all
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
from genie.libs.parser.iosxe.show_l2vpn import ShowL2vpnVfi as ShowL2vpnVfi_iosxe,\
                                               ShowL2vpnServiceAll as ShowL2vpnServiceAll_iosxe, \
                                               ShowEthernetServiceInstanceStats as ShowEthernetServiceInstanceStats_iosxe

# ===========================
# Parser for 'show l2vpn vfi'
# ===========================
class ShowL2vpnVfi(ShowL2vpnVfi_iosxe):
    """Parser for show l2vpn vfi
    """
    pass


# ===================================
# Parser for 'show l2vpn service all'
# ===================================
class ShowL2vpnServiceAll(ShowL2vpnServiceAll_iosxe):
    """Parser for show l2vpn service all
    """
    pass


# =================================================
# Parser for 'show ethernet service instance stats'
# =================================================
class ShowEthernetServiceInstanceStats(ShowEthernetServiceInstanceStats_iosxe):
    """Parser for show ethernet service instance stats
                  show ethernet service instance interface <interface> stats
    """
    pass