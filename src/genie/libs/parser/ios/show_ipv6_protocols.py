''' show_protocols.py

IOS parsers for the following show commands:
    * show ipv6 protocols
'''

from genie.libs.parser.iosxe.show_ipv6_protocols import ShowIpv6Protocols as \
                                                        ShowIpv6Protocols_iosxe


class ShowIpv6Protocols(ShowIpv6Protocols_iosxe):
    ''' Parser for "show ipv6 protocols" '''
    pass
