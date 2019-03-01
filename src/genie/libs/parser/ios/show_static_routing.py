'''
IOS Parsers

'''

from genie.libs.parser.iosxe.show_static_routing import ShowIpStaticRoute as ShowIpStaticRoute_iosxe,\
                                                        ShowIpv6StaticDetail as ShowIpv6StaticDetail_iosxe

class ShowIpStaticRoute(ShowIpStaticRoute_iosxe):
    pass

class ShowIpv6StaticDetail(ShowIpv6StaticDetail_iosxe):
    pass