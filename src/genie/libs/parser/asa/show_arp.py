''' show_arp.py

ASA parserr for the following show commands:
    * show arp
'''


# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional


# Schema for 'show arp'
# =============================================
class ShowArpSchema(MetaParser):
    """Schema for
        * show arp
    """

    schema = {
        'arp': {
        	Any(): {
                'name': str,
            	'mac_address': str,
            	'entry': str,
                'ipv4': {
                    Any(): { 
                        Optional('ip'): str,
                        Optional('prefix_length'): str
                    }
                }
            },
        }
    }

# =============================================
# Parser for 'show arp'
# =============================================
class ShowArp(ShowArpSchema):
    """Parser for
        * show arp
    """

    cli_command = 'show arp'

    def cli(self, output=None):
        if output is None:
            # excute command to get output
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}
        arp_id = 1

        # pod100 172.16.100.254 0000.0c9f.f00b 318
        p1 = re.compile(r'^(?P<name>[\w\S\.\-\(\)]+) +(?P<ip>[a-z0-9\.\w]+)'
            '(\/(?P<prefix_length>[0-9]+))? +(?P<mac_address>[\w\.]+) +(?P<entry>[\-\w]+)$')

        for line in out.splitlines():
            line = line.strip()

             # pod100 172.16.100.254 0000.0c9f.f00b 318
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                dict_arp = ret_dict.setdefault('arp', {}).setdefault(arp_id, {})
                dict_arp.update({'name': groups['name']})
                dict_arp.update({'mac_address': groups['mac_address']})
                dict_arp.update({'entry': groups['entry']})
                ipv4 = groups['ip']
                if groups['prefix_length']:
                    address = groups['ip'] + '/' + groups['prefix_length']
                dict_ipv4 = dict_arp.setdefault('ipv4', {}).setdefault(ipv4, {})
                dict_ipv4.update({'ip': groups['ip']})
                if groups['prefix_length']:
                    dict_ipv4.update({'prefix_length': groups['prefix_length']})
                arp_id += 1   
                continue

        return ret_dict