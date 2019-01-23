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


class ShowIpArp(ShowArp_iosxe):
    """ Parser for show arp
                  show ip arp <WROD>
                  show ip arp vrf <vrf>
                  show ip arp vrf <vrf> <WROD> """

    cli_command = ['show ip arp','show ip arp vrf {vrf}','show ip arp vrf {vrf} {intf_or_ip}', 'show ip arp {intf_or_ip}']

    def cli(self, vrf='', intf_or_ip='',output=None):
        if vrf and not intf_or_ip :
            cmd = self.cli_command[1].format(vrf=vrf)
        if vrf and intf_or_ip:
            cmd = self.cli_command[2].format(vrf=vrf,intf_or_ip=intf_or_ip)
        if not vrf and intf_or_ip:
            cmd = self.cli_command[3].format(intf_or_ip=intf_or_ip)
        if not vrf and not intf_or_ip:
            cmd = self.cli_command[0]

        ret_dict = super().cli(self, cmd=cmd)

        return ret_dict


class ShowIpArpSummary(ShowIpArpSummary_iosxe):
    """Parser for show ip arp summary"""
    pass


class ShowIpTraffic(ShowIpTraffic_iosxe):
    """Parser for: show ip traffic"""
    pass