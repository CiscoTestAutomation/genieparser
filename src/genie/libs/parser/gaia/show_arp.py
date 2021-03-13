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
        Any(): {'mac_address': str}
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

        p1 = re.compile(r'^^(?P<ip_address>[\d+\.*]+)\s+(?P<mac_address>[\w\w\:]+)$')

        # intial variables
        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                ip_address = m.groupdict()['ip_address']
                mac_address = m.groupdict()['mac_address']

                ret_dict.update({
                    ip_address: {'mac_address': mac_address}
                    })

        return ret_dict
