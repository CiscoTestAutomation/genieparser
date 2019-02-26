""" show_ip_route.py

IOSXE parsers for the following show commands:
    * 'show ip route bgp'
    * 'show ip route vrf <WORD> bgp'
    * 'show ipv6 route bgp'
    * 'show ipv6 route vrf <WORD> bgp'
"""

from genie.libs.parser.iosxe.show_ip_route import ShowIpRoute as ShowIpRoute_iosxe, \
                                                  ShowIpv6Route as ShowIpv6Route_iosxe
class ShowIpRoute(ShowIpRoute_iosxe):
    """Parser for:
        show ip route bgp
        show ip route vrf <vrf> bgp
        show ipv6 route bgp
        show ipv6 route vrf <vrf> bgp"""
    pass

class ShowIpv6Route(ShowIpv6Route_iosxe):
    """Parser for:
        show ipv6 route bgp
        show ipv6 route vrf <vrf> bgp"""

    pass
