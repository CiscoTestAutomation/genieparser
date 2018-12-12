''' show_arp.py

IOS parsers for the following show commands:
    * show arp
    * show arp <WORD>
    * show arp vrf <vrf>
    * show arp vrf <vrf> <WORD>
    * show ip arp
    * show ip arp summary
    * show ip traffic
'''

# python
import re

# genie
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

# import iosxe parser
from genie.libs.parser.iosxe.show_arp import \
    ShowArp as ShowArp_iosxe, \
    ShowIpArpSummary as ShowIpArpSummary_iosxe, \
    ShowIpTraffic as ShowIpTraffic_iosxe


class ShowArp(ShowArp_iosxe):
    """ Parser for show arp
                  show ip arp <WROD>
                  show ip arp vrf <vrf>
                  show ip arp vrf <vrf> <WROD> """

    def cli(self, vrf='', intf_or_ip=''):
        cmd = 'show ip arp'
        if vrf:
            cmd += 'vrf ' + vrf
        if intf_or_ip:
            cmd += ' ' + intf_or_ip
        ret_dict = super().cli(self, cmd=cmd)

        return ret_dict


class ShowIpArpSummary(ShowIpArpSummary_iosxe):
    """Parser for show ip arp summary"""
    pass


class ShowIpTraffic(ShowIpTraffic_iosxe):
    """Parser for: show ip traffic"""
    pass