"""show_vrf.py

IOS parsers for the following show commands:
    * 'show vrf detail'
"""

# Python
import re
import xmltodict

# genieparser
from genie.libs.parser.iosxe.show_vrf import ShowVrfDetail as ShowVrfDetail_iosxe


class ShowVrfDetail(ShowVrfDetail_iosxe):
    """Parser for show vrf detail"""
    pass
