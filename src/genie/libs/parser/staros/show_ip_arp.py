
"""starOS implementation of show_ip_arp.py

"""
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Schema

class ShowIpArpSchema(MetaParser):
    """Schema for show ip arp"""

    schema = {
        'ip_arp': {
            Any(): {
                'ipaddr': str,
                'linktype': str,
                'macaddr': str,
                'flag': str,
                'interface': str
            },
        }    
    }


class ShowIpArp(ShowIpArpSchema):
    """Parser for show ip arp"""

    cli_command = 'show ip arp'

    """
Flags codes:
I - Incomplete, R - Reachable, M - Permanent, S - Stale, 
D - Delay,      P - Probe,     F - Failed
# Indicate vpn  and npu audit result is success 
^ Indicate vpn  and npu audit result is failure 

  Address         Link Type Link Address      Flags  Mask            Interface
   172.16.224.34   ether     A0:E0:AF:13:B2:77 R                      5/11-S5S8
   172.16.224.32   ether     A0:E0:AF:14:04:F7 R                      5/10-S5S8
Total number of arps: 2   
    """

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        arp_dict = {}
        
        result_dict = {}

        # initial regexp pattern
        p0 = re.compile(r'((?P<ipaddr>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(?P<linktype>\w\w+)\s+(?P<macaddr>[0-9a-fA-F][0-9a-fA-F]\:[0-9a-fA-F][0-9a-fA-F]\:[0-9a-fA-F][0-9a-fA-F]\:[0-9a-fA-F][0-9a-fA-F]\:[0-9a-fA-F][0-9a-fA-F]\:[0-9a-fA-F][0-9a-fA-F])\s+(?P<flag>[a-zA-Z])\s+(?P<interface>\w\w+))')

        for line in out.splitlines():
            line = line.strip()

            m = p0.match(line)
            if m:
                if 'ip_arp' not in arp_dict:
                    result_dict = arp_dict.setdefault('ip_arp',{})
                arp = m.groupdict()['ipaddr']
                ip_address = m.groupdict()['ipaddr']
                link_type = m.groupdict()['linktype']
                mac_address = m.groupdict()['macaddr']
                flag = m.groupdict()['flag']
                interface = m.groupdict()['interface']
                result_dict[arp] = {}
                result_dict[arp]['ipaddr'] = ip_address
                result_dict[arp]['linktype'] = link_type
                result_dict[arp]['macaddr'] = mac_address
                result_dict[arp]['flag'] = flag
                result_dict[arp]['interface'] = interface             
                continue

        return arp_dict