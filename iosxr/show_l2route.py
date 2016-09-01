''' show_l2route.py

show l2route parser class

'''

import re
from netaddr import EUI
from ipaddress import ip_address

from ats import tcl
from ats.tcl import tclobj, tclstr
from metaparser import MetaParser
from metaparser.util.schemaengine import Any


class ShowL2routeEvpnMac(MetaParser):
    '''Parser class for 'show l2route evpn mac all' CLI.'''

    # TODO schema

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def cli(self):
        cmd = 'show l2route evpn mac all'.format()

        out = self.device.execute(cmd)

        result = {
            'entries': []
        }


        for line in out.splitlines():
            line = line.rstrip()

            # Topo ID  Mac Address    Prod   Next Hop(s)                             
            # -------- -------------- ------ ----------------------------------------                          

            # 1        7777.7777.0002 LOCAL  Bundle-Ether1.7      
            m = re.match(r'^(?P<topo_id>\d+)'
                         r' +(<?P<mac>[A-Za-z0-9]+\.[A-Za-z0-9]+\.[A-Za-z0-9]+)'
                         r' +(?P<producer>\S+)'
                         r' +(?:none|(?P<next_hop>\S+))$', line)
            if m:
                entry = {
                    'topo_id': eval(m.group('topo_id')),
                    'mac': EUI(m.group('mac')),
                    'producer': {'LOCAL': 'local'}.get(m.group('producer'), m.group('producer')),
                    'next_hop': m.group('next_hop'),
                }
                result['entries'].append(entry)
                continue

        return result

# vim: ft=python ts=8 sw=4 et
