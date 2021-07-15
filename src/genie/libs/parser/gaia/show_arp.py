""" show_arp.py

Check Point Gaia parsers for the following show commands:
    * show arp dynamic all
    * show arp static all

"""

import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any


class ShowArpSchema(MetaParser):
    schema = {
        'ip_address': {
            Any(): {
                'mac_address': str
                }
            }
        }

class ShowArpDynamic(ShowArpSchema):
    """ Parser for  show arp dynamic all
                    show arp static all """

    cli_command = ['show arp dynamic all', 'show arp static all']

    def cli(self, cmd=None, output=None):
        if output is None:
            if not cmd:
                cmd = self.cli_command[0]

            out = self.device.execute(cmd)
        else:
            out = output

        ''' Sample Output
        gw-a> show arp dynamic all
        Dynamic Arp Parameters

        IP Address                 Mac Address
        10.1.1.2                50:00:00:ff:82:0c
        10.1.1.1                50:00:00:ff:06:07
        '''

        p1 = re.compile(r'^^(?P<ip_address>[\d+\.*]+)\s+(?P<mac_address>[\w\w\:]+)$')

        # intial variables
        ret_dict = {}

        for line in out.splitlines():
            if 'ip_address' not in ret_dict:
                ret_dict['ip_address'] = {}

            line = line.strip()

            # 10.1.1.2                50:00:00:ff:82:0c
            m = p1.match(line)
            if m:
                ip_address = m.groupdict()['ip_address']
                mac_address = m.groupdict()['mac_address']

                ret_dict['ip_address'].update({
                    ip_address: {'mac_address': mac_address}
                    })

        return ret_dict
