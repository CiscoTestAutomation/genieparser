"""show_mcast.py

IOSXE parsers for the following show commands:

    * show ip mroute
    * show ipv6 mroute
    * show ip mroute vrf <vrf_name>
    * show ipv6 mroute vrf <vrf_name>
    * show ip mroute static
    * show ip mroute vrf <vrf_name> static
    * show ip multicast
    * show ip multicast vrf <vrf_name>

"""

from genie.libs.parser.iosxe.show_mcast import ShowIpMroute as ShowIpMroute_iosxe,\
                                               ShowIpv6Mroute as ShowIpv6Mroute_iosxe,\
                                               ShowIpMulticast as ShowIpMulticast_iosxe,\
                                               ShowIpMrouteStatic as ShowIpMrouteStatic_iosxe


class ShowIpMroute(ShowIpMroute_iosxe):
    """Parser for:
        show ip mroute
        show ip mroute vrf <vrf>"""
    pass

class ShowIpv6Mroute(ShowIpv6Mroute_iosxe):
    """Parser for:
       show ipv6 mroute
       show ipv6 mroute vrf <vrf>"""

    pass

class ShowIpMrouteStatic(ShowIpMrouteStatic_iosxe):
    """Parser for:
            show ip mroute static
            show ip mroute vrf <vrf> static
        """
    pass

class ShowIpMulticast(ShowIpMulticast_iosxe):
    """Parser for:
        show ip multicast
        show ip multicast vrf <vrf>
    """
    pass