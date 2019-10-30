'''
show_route.py

'''

from genie.libs.parser.iosxe.show_routing import ShowIpRoute as ShowIpRoute_iosxe,\
                                                 ShowIpv6Route as ShowIpv6Route_iosxe,\
                                                 ShowIpv6RouteUpdated as ShowIpv6RouteUpdated_iosxe,\
                                                 ShowIpRouteWord as ShowIpRouteWord_iosxe,\
                                                 ShowIpv6RouteWord as ShowIpv6RouteWord_iosxe,\
                                                 ShowIpRouteSummary as ShowIpRouteSummary_iosxe

class ShowIpRoute(ShowIpRoute_iosxe):
    """Parser for :
       show ip route
       show ip route vrf <vrf>
       """
    pass

class ShowIpv6Route(ShowIpv6Route_iosxe):
    """Parser for :
       show ip route
       show ip route vrf <vrf>
       """
    pass


class ShowIpv6RouteUpdated(ShowIpv6RouteUpdated_iosxe):
    """Parser for :
       show ipv6 route updated
       show ipv6 route vrf <vrf> updated"""
    pass

class ShowIpRouteWord(ShowIpRouteWord_iosxe):
    """Parser for :
       show ip route <Hostname or A.B.C.D>
       show ip route vrf <vrf> <Hostname or A.B.C.D>"""
    pass

class ShowIpv6RouteWord(ShowIpv6RouteWord_iosxe):
    """Parser for :
       show ipv6 route <Hostname or A.B.C.D>
       show ipv6 route vrf <vrf> <Hostname or A.B.C.D>"""
    pass

class ShowIpRouteSummary(ShowIpRouteSummary_iosxe):
    """Parser for :
       show ip route summary
       show ip route vrf <vrf> summary"""
    pass