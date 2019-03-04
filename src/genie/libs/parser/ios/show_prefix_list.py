"""show_prefix_list.py

IOS parsers for the following show commands:

    * show ip prefix-list detail
    * show ipv6 prefix-list detail
"""

from genie.libs.parser.iosxe.show_prefix_list import ShowIpPrefixListDetail as ShowIpPrefixListDetail_iosxe,\
                                                     ShowIpv6PrefixListDetail as ShowIpv6PrefixListDetail_iosxe

class ShowIpPrefixListDetail(ShowIpPrefixListDetail_iosxe):
    """Parser for:
        show ip prefix-list detail
        show ipv6 prefix-list detail"""
    pass


class ShowIpv6PrefixListDetail(ShowIpv6PrefixListDetail_iosxe):
    """Parser for show ipv6 prefix-list detail"""
    pass

