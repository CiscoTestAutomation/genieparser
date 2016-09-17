''' show_controllers.py

show controllers parser class

'''

import re
from netaddr import EUI

from ats import tcl
from ats.tcl import tclobj, tclstr
from metaparser import MetaParser
from metaparser.util.schemaengine import Any


class ShowControllersFiaDiagshellL2show(MetaParser):
    '''Parser class for 'show controllers fia diagshell 0 "l2 show"' CLI.'''

    # TODO schema

    def __init__(self, diagshell_unit=0, location='all', **kwargs):
        self.diagshell_unit = diagshell_unit
        self.location = location
        super().__init__(**kwargs)

    def cli(self):
        cmd = 'show controllers fia diagshell {diagshell_unit} "l2 show" location {location}'.format(
            diagshell_unit=self.diagshell_unit,
            location=self.location)

        # Fix bug in csccon (1.0.0) where Tcl command is not correctly quoted.
        cmd = cmd.replace('"', r'\"')

        out = self.device.execute(cmd)

        result = {
            'nodes': {}
        }

        node_id = None
        for line in out.splitlines():
            line = line.rstrip()
            # Node ID: 0/0/CPU0
            m = re.match(r'^Node ID: (\S+)$', line)
            if m:
                node_id = m.group(1)
                result['nodes'].setdefault(node_id, {
                    'entries': [],
                })
                continue
            # mac=fc:00:00:01:00:9b vlan=2544 GPORT=0x8000048 encap_id=0x2007
            # mac=fc:00:00:01:00:9b vlan=2544 GPORT=0x8000048 Trunk=0 encap_id=0x2007
            m = re.match(r'^mac=(?P<mac>[A-Fa-f0-9:]+)'
                         r' +vlan=(?P<vlan>\d+)'
                         r' +GPORT=(?P<gport>\d+|0x[[A-Fa-f0-9]+)'
                         r'(?: +Trunk=(?P<trunk>\d+))?'
                         r' +encap_id=(?P<encap_id>\d+|0x[[A-Fa-f0-9]+)$', line)
            if m:
                entry = {
                    'mac': EUI(m.group('mac')),
                    'vlan': int(m.group('vlan')),
                    'gport': eval(m.group('gport')),
                    'trunk': m.group('trunk') and eval(m.group('trunk')),
                    'encap_id': eval(m.group('encap_id')),
                }
                result['nodes'][node_id]['entries'].append(entry)
                continue

        return result

# vim: ft=python ts=8 sw=4 et
