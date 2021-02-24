'''show_route.py

IOS parsers for the following show commands:
    * show ip route
    * show ip route vrf <vrf>
    * show ipv6 route
    * show ipv6 route vrf <vrf>
    * show ip route <Hostname or A.B.C.D>
    * show ip route vrf <vrf> <Hostname or A.B.C.D>
    * show ipv6 route <Hostname or 2001:DB8:64:79::C:D>
    * show ipv6 route vrf <vrf> <Hostname or 2001:DB8:64:79::C:D>
    * show ipv6 route updated
    * show ipv6 route vrf <vrf> updated
    * show ip route summary
    * show ip route vrf <vrf> summary

'''

from genie.libs.parser.iosxe.show_routing import (
    ShowIpv6RouteUpdated as ShowIpv6RouteUpdated_iosxe, ShowIpRouteSummary as
    ShowIpRouteSummary_iosxe, ShowIpRouteDistributor as
    ShowIpRouteDistributor_iosxe, ShowIpv6RouteDistributor as
    ShowIpv6RouteDistributor_iosxe)


class ShowIpRouteDistributor(ShowIpRouteDistributor_iosxe):
    """distributor class for show ip route"""
    pass


class ShowIpv6RouteDistributor(ShowIpv6RouteDistributor_iosxe):
    """distributor class for show ipv6 route"""
    pass


class ShowIpv6RouteUpdated(ShowIpv6RouteUpdated_iosxe):
    """Parser for :
       show ipv6 route updated
       show ipv6 route vrf <vrf> updated"""
    pass


class ShowIpRouteSummary(ShowIpRouteSummary_iosxe):
    """Parser for :
       show ip route summary
       show ip route vrf <vrf> summary"""
    pass