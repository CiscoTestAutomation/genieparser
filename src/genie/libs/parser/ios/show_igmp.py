"""
show_igmp.py

IOS parsers for the following show commands:

    * show ip igmp interface 
    * show ip igmp vrf <WORD> interface 
    * show ip igmp groups detail
    * show ip igmp vrf <WORD> groups detail
"""

# Python

from genie.libs.parser.iosxe.show_igmp import ShowIpIgmpInterface as ShowIpIgmpInterface_iosxe,\
                                              ShowIpIgmpGroupsDetail as ShowIpIgmpGroupsDetail_iosxe, \
                                              ShowIpIgmpSsmMapping as ShowIpIgmpSsmMapping_iosxe

class ShowIpIgmpInterface(ShowIpIgmpInterface_iosxe):
    """
    Parser for 'show ip igmp interface'
    Parser for 'show ip igmp vrf <WORD> interface'
    """
    pass

class ShowIpIgmpGroupsDetail(ShowIpIgmpGroupsDetail_iosxe):
    """
    Parser for 'show ip igmp groups detail'
    Parser for 'show ip igmp vrf <WORD> groups detail'
    """
    pass

class ShowIpIgmpSsmMapping(ShowIpIgmpSsmMapping_iosxe):
    """
    Parser for 'show ip igmp ssm-mapping <WROD>'
    parser for 'show ip igmp vrf <WORD> ssm-mapping <WORD>'
    """
    pass