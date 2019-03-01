"""show_mld.py

IOS parsers for the following show commands:

    * show ipv6 mld interface 
    * show ipv6 mld vrf <WORD> interface 
    * show ipv6 mld groups detail
    * show ipv6 mld vrf <WORD> groups detail
    * show ipv6 mld ssm-map <WORD>
    * show ipv6 mld vrf <WORD> ssm-map <WORD>
"""

from genie.libs.parser.iosxe.show_mld import ShowIpv6MldGroupsDetail as ShowIpv6MldGroupsDetail_iosxe,\
                                             ShowIpv6MldInterface as ShowIpv6MldInterface_iosxe,\
                                             ShowIpv6MldSsmMap as ShowIpv6MldSsmMap_iosxe


class ShowIpv6MldInterface(ShowIpv6MldInterface_iosxe):
    """Parser for:
        show ipv6 mld interface
        show ipv6 mld vrf <vrf> interface"""
    pass

class ShowIpv6MldGroupsDetail(ShowIpv6MldGroupsDetail_iosxe):
    """Parser for:
        show ipv6 mld groups detail
        show ipv6 mld vrf <vrf> groups detail"""
    pass

class ShowIpv6MldSsmMap(ShowIpv6MldSsmMap_iosxe):
    """Parser for:
        show ipv6 mld ssm-map <group_address>
        show ipv6 mld vrf <vrf> ssm-map <group_address>"""

    pass