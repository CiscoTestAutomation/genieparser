''' show_cdp.py
    Supported commands:
        * show cdp neighbors
'''

# import iosxe parser
from genie.libs.parser.iosxe.show_cdp import ShowCdpNeighbors as ShowCdpNeighbors_iosxe, \
    ShowCdpNeighborsDetail as ShowCdpNeighborsDetail_iosxe


class ShowCdpNeighbors(ShowCdpNeighbors_iosxe):
    """Parser for show cdp all neighbors"""

    pass


class ShowCdpNeighborsDetail(ShowCdpNeighborsDetail_iosxe):
    """Parser for show cdp neighbors details"""

    pass
