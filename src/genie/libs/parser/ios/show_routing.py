'''
show_route.py

'''

from genie.libs.parser.iosxe.show_routing import ShowIpRoute as ShowIpRoute_iosxe,\
                                                 ShowIpv6RouteUpdated as ShowIpv6RouteUpdated_iosxe,\
                                                 ShowIpv6RouteWord as ShowIpv6RouteWord_iosxe


class ShowIpRoute(ShowIpRoute_iosxe):
    """Parser for :
       show ip route
       show ip route vrf <vrf>
       show ip route <route>
       show ip route vrf <vrf> <route>"""
    pass


class ShowIpv6RouteUpdated(ShowIpv6RouteUpdated_iosxe):
    """Parser for :
       show ipv6 route updated
       show ipv6 route vrf <vrf> updated"""
    pass


class ShowIpv6RouteWord(ShowIpv6RouteWord_iosxe):
    """Parser for :
       show ipv6 route <Hostname or A.B.C.D>
       show ipv6 route vrf <vrf> <Hostname or A.B.C.D>"""
    pass