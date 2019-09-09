""" show_msdp.py
IOS parsers for the following commands
    * 'show ip msdp peer'
    * 'show ip msdp vrf {vrf} peer'
    * 'show ip msdp sa-cache'
    * 'show ip msdp vrf {vrf} sa-cache'
"""

# iosxe show msdp
from genie.libs.parser.iosxe.show_msdp import (
    ShowIpMsdpPeer as ShowIpMsdpPeer_iosxe,
    ShowIpMsdpSaCache as ShowIpMsdpSaCache_iosxe,
)


class ShowIpMsdpPeer(ShowIpMsdpPeer_iosxe):
    """ Parser for:
        * 'show ip msdp peer'
        * 'show ip msdp vrf <vrf> peer'
    """
    pass


class ShowIpMsdpSaCache(ShowIpMsdpSaCache_iosxe):
    """ Parser for:
		* 'show ip msdp vrf {vrf} sa-cache'
        * 'show ip msdp sa-cache'
	"""
    pass
