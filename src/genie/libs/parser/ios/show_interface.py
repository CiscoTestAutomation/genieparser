"""
    show_interface.py
    IOS parsers for the following show commands:

    * show interfaces
    * show ip interface brief
    * show ip interface brief | include Vlan
    * show ip interface brief | include <WROD>
    * show ip interface
    * show ipv6 interface
    * show interfaces accounting

    # TODO: Need find replacement command for IOSXE 'show interface <intf> counters'
"""

# python
import re

# genie
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                         Any, Optional

# import iosxe parser
from genie.libs.parser.iosxe.show_interface import \
    ShowInterfaces as ShowInterfaces_iosxe, \
    ShowIpInterfaceBrief as ShowIpInterfaceBrief_iosxe, \
    ShowIpInterfaceBriefPipeVlan as ShowIpInterfaceBriefPipeVlan_iosxe, \
    ShowIpInterfaceBriefPipeIp as ShowIpInterfaceBriefPipeIp_iosxe, \
    ShowIpInterface as ShowIpInterface_iosxe, \
    ShowIpv6Interface as ShowIpv6Interface_iosxe, \
    ShowInterfacesAccounting as ShowInterfacesAccounting_iosxe

# import parser utils
from genie.libs.parser.utils.common import Common


class ShowInterfaces(ShowInterfaces_iosxe):
    """parser for show interfaces"""
    pass


class ShowIpInterfaceBrief(ShowIpInterfaceBrief_iosxe):
    """Parser for: show ip interface brief"""
    pass


class ShowIpInterfaceBriefPipeVlan(ShowIpInterfaceBriefPipeVlan_iosxe):
    """Parser for: show ip interface brief | include Vlan"""
    pass


class ShowIpInterfaceBriefPipeIp(ShowIpInterfaceBriefPipeIp_iosxe):
    """Parser for:  show ip interface brief | include <WORD>"""
    pass


class ShowIpInterface(ShowIpInterface_iosxe):
    """Parser for show ip interface"""
    pass


class ShowIpv6Interface(ShowIpv6Interface_iosxe):
    """Parser for show ipv6 interface"""
    pass


class ShowInterfacesAccounting(ShowInterfacesAccounting_iosxe):
    """Parser for:
        show interfaces accounting
        show interfaces <interface> accounting
    """
    pass
