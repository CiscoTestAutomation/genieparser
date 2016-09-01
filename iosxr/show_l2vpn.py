''' show_l2vpn.py

show l2vpn parser class

'''

import re
from netaddr import EUI
from ipaddress import ip_address

from ats import tcl
from ats.tcl import tclobj, tclstr
from metaparser import MetaParser
from metaparser.util.schemaengine import Any


class ShowL2vpnMacLearning(MetaParser):
    '''Parser class for 'show l2vpn mac-learning mac|mac-ipv4|mac-ipv6 mac' CLI.'''

    # TODO schema

    def __init__(self, mac_type='mac', location='local', **kwargs):
        self.location = location
        self.mac_type = mac_type
        super().__init__(**kwargs)

    def cli(self):
        cmd = 'show l2vpn mac-learning {mac_type} all location {location}'.format(
            mac_type=self.mac_type,
            location=self.location)

        out = self.device.execute(cmd)

        result = {
            'entries': []
        }


        for line in out.splitlines():
            line = line.rstrip()
            # Topo ID   Producer       Next Hop(s)       Mac Address       IP Address       
            # -------   --------       -----------       --------------    ----------       

            # 1         0/0/CPU0       BE1.7             7777.7777.0002      
            m = re.match(r'^(?P<topo_id>\d+)'
                         r' +(?P<producer>\S+)'
                         r' +(?:none|(?P<next_hop>\S+))'
                         r' +(<?P<mac>[A-Za-z0-9]+\.[A-Za-z0-9]+\.[A-Za-z0-9]+)'
                         r'(?: +(?P<ip_address>\d+\.\d+\.\d+\.\d+|[A-Za-z0-9:]+))?$', line)
            if m:
                entry = {
                    'topo_id': eval(m.group('topo_id')),
                    'producer': m.group('producer'),
                    'next_hop': m.group('next_hop'),
                    'mac': EUI(m.group('mac')),
                    'ip_address': m.group('ip_address') and ip_address(m.group('ip_address')),
                }
                result['entries'].append(entry)
                continue

        return result

# vim: ft=python ts=8 sw=4 et
