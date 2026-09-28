"""show_idb.py

IOSXE parser for the following show command:
    * show idb
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# ==============================================
#  Schema for show idb
# ==============================================
class ShowIdbSchema(MetaParser):
    """Schema for show idb"""

    schema = {
        Optional('software_idbs'): {
            'maximum': int,
            'in_use': int,
        },
        Optional('micro_software_idbs'): {
            'maximum': int,
            'in_use': int,
        },
        Optional('idb_summary'): {
            Any(): {
                'hwidbs': int,
                'swidbs': int,
                'uhwidbs': int,
                'uswidbs': int,
            },
        },
        Optional('interfaces'): {
            Any(): {
                Optional('H'): {
                    'sidx': int,
                    'idx': int,
                    'state': str,
                    Optional('old_state'): str,
                    Optional('shadow_state'): str,
                    Optional('subblocks'): {
                        Any(): int,
                    },
                },
                Optional('S'): {
                    'sidx': int,
                    'idx': int,
                    'state': str,
                    Optional('old_state'): str,
                    Optional('shadow_state'): str,
                    Optional('subblocks'): {
                        Any(): int,
                    },
                },
            },
        },
    }


# ==============================================
#  Parser for show idb
# ==============================================
class ShowIdb(ShowIdbSchema):
    """Parser for show idb"""

    cli_command = 'show idb'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        # Maximum number of Software IDBs 131072.  In use 280.
        # Maximum number of Micro Software IDBs 49152.  In use 0.
        p1 = re.compile(
            r'^Maximum +number +of +(?P<idb_type>Micro +Software|Software) +'
            r'IDBs +(?P<maximum>\d+)\. +In +use +(?P<in_use>\d+)\.$'
        )

        # Active                    271        271                0          0
        # Size each (bytes)        5000       1976             3904        640
        p2 = re.compile(
            r'^(?P<row>Active|Inactive|Total +IDBs|Size +each +\(bytes\)|'
            r'Total +bytes) +(?P<hwidbs>\d+) +(?P<swidbs>\d+) +'
            r'(?P<uhwidbs>\d+) +(?P<uswidbs>\d+)$'
        )

        # H     1  1298   U,U,R  Vlan1 (PF_IDB(4), Ether(1))
        # S     1  1299   U       Vlan1 (CTS PLATFORM SB(24), KEEPALIVE(1))
        p3 = re.compile(
            r'^(?P<idb_type>[HS]) +(?P<sidx>\d+) +(?P<idx>\d+) +'
            r'(?P<states>[A-Z](?:,[A-Z],[A-Z])?) +(?P<interface>\S+)'
            r'(?: +\((?P<subblocks>.*)\))?$'
        )

        # PF_IDB(4), Ether(1)
        p4 = re.compile(r'^(?P<name>.+)\((?P<id>\d+)\)$')

        for line in output.splitlines():
            line = line.strip()

            if not line:
                continue

            # Maximum number of Software IDBs 131072.  In use 280.
            m = p1.match(line)
            if m:
                group = m.groupdict()
                key = group['idb_type'].lower().replace(' ', '_') + '_idbs'
                ret_dict[key] = {
                    'maximum': int(group['maximum']),
                    'in_use': int(group['in_use']),
                }
                continue

            # Active                    271        271                0          0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                row = re.sub(r' +', ' ', group.pop('row'))
                ret_dict.setdefault('idb_summary', {})[row] = {
                    key: int(value) for key, value in group.items()
                }
                continue

            # H     1  1298   U,U,R  Vlan1 (PF_IDB(4), Ether(1))
            # S     1  1299   U       Vlan1 (CTS PLATFORM SB(24), KEEPALIVE(1))
            m = p3.match(line)
            if m:
                group = m.groupdict()
                interface = group['interface']
                idb_type = group['idb_type']
                states = group['states'].split(',')

                idb_dict = ret_dict.setdefault('interfaces', {}).setdefault(
                    interface, {}).setdefault(idb_type, {})
                idb_dict.update({
                    'sidx': int(group['sidx']),
                    'idx': int(group['idx']),
                    'state': states[0],
                })

                if len(states) == 3:
                    idb_dict['old_state'] = states[1]
                    idb_dict['shadow_state'] = states[2]

                subblocks = {}
                for subblock in (group.get('subblocks') or '').split(','):
                    subblock = subblock.strip()
                    if not subblock:
                        continue

                    m_subblock = p4.match(subblock)
                    if m_subblock:
                        subblock_group = m_subblock.groupdict()
                        subblocks[subblock_group['name'].strip()] = int(
                            subblock_group['id'])

                if subblocks:
                    idb_dict['subblocks'] = subblocks

                continue

        return ret_dict
