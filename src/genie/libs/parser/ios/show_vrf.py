"""show_vrf.py

IOS parsers for the following show commands:
    * 'show vrf detail'
    * 'show vrf
"""

# Python
import re
import xmltodict

# genieparser
from genie.libs.parser.iosxe.show_vrf import ShowVrfDetail as ShowVrfDetail_iosxe
from genie.libs.parser.iosxe.show_vrf import ShowVrf as ShowVrf_iosxe


class ShowVrfDetail(ShowVrfDetail_iosxe):
    """Parser for show vrf detail"""
    exclude = ['vrf']
    pass

class ShowVrf(ShowVrf_iosxe):
    """Parser for show vrf"""
    pass
