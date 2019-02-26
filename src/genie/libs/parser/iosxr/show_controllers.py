''' show_controllers.py

show controllers parser class

'''

import re
import logging
from netaddr import EUI

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any

from genie.libs.parser.base import *

logger = logging.getLogger(__name__)

class ShowControllersFiaDiagshellL2show(MetaParser):
    """Parser class for show controllers fia diagshell 0 'l2 show' """

    # TODO schema
    cli_command = 'show controllers fia diagshell {diagshell_unit} "l2 show" location {location}'

    def __init__(self, diagshell_unit=0, location='all', **kwargs):
        self.diagshell_unit = diagshell_unit
        self.location = location
        super().__init__(**kwargs)

    def cli(self):
        cmd = self.cli_command.format(
            diagshell_unit=self.diagshell_unit,
            location=self.location)

        # Fix bug in csccon (1.0.0) where Tcl command is not correctly quoted.
        cmd = cmd.replace('"', r'\"')

        out = self.device.execute(cmd)

        result = {
            'nodes': {},
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
            # mac=fc:00:00:01:00:02 vlan=2522 GPORT=0x9800401d Static encap_id=0xffffffff
            # mac=fc:00:00:01:00:9b vlan=2544 GPORT=0x8000048 Trunk=0 encap_id=0x2007
            # mac=fc:00:00:01:00:0b vlan=2524 GPORT=0xc000000 Trunk=0 Static encap_id=0x3001'
            m = re.match(r'^mac=(?P<mac>[A-Fa-f0-9:]+)'
                         r' +vlan=(?P<vlan>\d+)'
                         r' +GPORT=(?P<gport>\d+|0x[[A-Fa-f0-9]+)'
                         r'(?: +Trunk=(?P<trunk>\d+))?'
                         r'(?P<b_static> +Static)?'
                         r' +encap_id=(?P<encap_id>\d+|0x[[A-Fa-f0-9]+)$', line)
            if m:
                entry = {
                    'mac': EUI(m.group('mac')),
                    'vlan': int(m.group('vlan')),
                    'gport': eval(m.group('gport')),
                    'static': bool(m.group('b_static')),
                    'trunk': m.group('trunk') and eval(m.group('trunk')),
                    'encap_id': eval(m.group('encap_id')),
                }
                result['nodes'][node_id]['entries'].append(entry)
                continue

            if line.startswith('mac='):
                logger.warning('Unrecognized MAC line in %r: %r', cmd, line)

        return result

# vim: ft=python ts=8 sw=4 et
