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
from genie.libs.parser.iosxe.show_interface import *

# import parser utils
from genie.libs.parser.utils.common import Common


class ShowInterfaces(ShowInterfaces):
    """parser for show interfaces"""

    pass


class ShowIpInterfaceBrief(ShowIpInterfaceBrief):
    """Parser for: show ip interface brief"""
    pass


class ShowIpInterfaceBriefPipeVlan(ShowIpInterfaceBriefPipeVlan):
    """Parser for: show ip interface brief | include Vlan"""
    pass


class ShowIpInterfaceBriefPipeIp(ShowIpInterfaceBriefPipeIp):
    """Parser for:  show ip interface brief | include <WORD>"""
    pass


class ShowIpInterface(ShowIpInterface):
    """Parser for show ip interface"""
    pass


class ShowIpv6Interface(ShowIpv6Interface):
    """Parser for show ipv6 interface"""
    pass


class ShowInterfacesAccounting(ShowInterfacesAccounting):
    """Parser for:
        show interfaces accounting
        show interfaces <interface> accounting
    """
    pass
