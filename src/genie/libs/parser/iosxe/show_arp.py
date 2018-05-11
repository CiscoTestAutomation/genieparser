''' show_archive.py

IOSXE parsers for the following show commands:
    * show archive
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

# parser utils
from genie.libs.parser.utils.common import Common


# =============================================
# Parser for 'show arp [vrf <WORD>] <WROD>'
# =============================================

class ShowArpSchema(MetaParser):
    """Schema for show arp
                  show arp <WROD>
                  show arp vrf <vrf>
                  show arp vrf <vrf> <WROD>
    """

    schema = {
        'address': {        
            Any(): {
                'address': str,
                'protocol': str,
                Optional('age'): str,
                'mac': str,
                'type': str,
                'interface': str
            },
        }
    }

class ShowArp(ShowArpSchema):
    """ Parser for show arp
                  show arp <WROD>
                  show arp vrf <vrf>
                  show arp vrf <vrf> <WROD> """

    def cli(self, vrf='', intf_or_ip=''):

        # excute command to get output
        cmd = 'show arp'
        if vrf:
            cmd += 'vrf ' + vrf
        if intf_or_ip:
            cmd += ' ' + intf_or_ip
        out = self.device.execute(cmd)

        # initial regexp pattern
        p1 = re.compile(r'^(?P<protocol>\w+) +(?P<address>[\d\.\:]+) +(?P<age>[\d\-]+) +'
                         '(?P<mac>[\w\.]+) +(?P<type>\w+) +(?P<interface>[\w\.\/\-]+)$')
        # initial variables
        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # Internet  201.0.12.1              -   58bf.eab6.2f51  ARPA   Vlan100
            m = p1.match(line)
            if m:
                group = m.groupdict()
                address = group['address']
                addr_dict = ret_dict.setdefault('address', {}).setdefault(address, {})
                addr_dict['interface'] = Common.convert_intf_name(group.pop('interface'))
                addr_dict.update({k:v for k,v in group.items() if v != '-'})
                continue

        return ret_dict
