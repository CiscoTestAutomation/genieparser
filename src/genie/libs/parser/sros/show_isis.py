""" show_isis.py
    supports commands:
        * show router isis adjacency
        * show router isis adjacency detail
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

# parser utils
from genie.libs.parser.utils.common import Common

# =============================================
# Parser for 'show router isis adjacency'
# =============================================


class ShowRouterIsisAdjacencySchema(MetaParser):
    """Schema for show router isis adjacency"""
    schema = {
        'system_id': {
            Any(): {
                'usage': str,
                'state': str,
                'hold': int,
                'interface': str,
                'mt_id': int,
            },
        },
        'adjacencies': int,
    }


class ShowRouterIsisAdjacency(ShowRouterIsisAdjacencySchema):
    """ Parser for show router isis adjacency"""

    cli_command = 'show router isis adjacency'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}

        # System ID                Usage State Hold Interface                     MT-ID
        # -------------------------------------------------------------------------------
        # COPQON05R07              L2    Up    24   To-COPQON05R07-LAG-7          0
        # COTKON04XR1              L2    Up    24   To-COTKON04XR1-LAG-4          0
        # COTKPQ03R07              L2    Up    24   To-COTKPQ03R07-LAG-9          0
        # -------------------------------------------------------------------------------
        p1 = re.compile(r'^(?P<system_id>\S+) +(?P<usage>\S+) +(?P<state>\S+) '
                        r'+(?P<hold>\d+) +(?P<interface>\S+) +(?P<mt_id>\d+)$')

        # Adjacencies : 3
        p2 = re.compile(r'^Adjacencies : (?P<adjacencies>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()

                system_id_dict = parsed_dict.setdefault('system_id', {}).\
                                setdefault(group['system_id'], {})
                for k in ['usage', 'state', 'interface']:
                    system_id_dict[k] = group[k]
                for int_k in ['hold', 'mt_id']:
                    system_id_dict[int_k] = int(group[int_k])
                continue

            # Adjacencies: 3
            m = p2.match(line)
            if m:
                parsed_dict['adjacencies'] = int(m.groupdict()['adjacencies'])
                continue

        return parsed_dict


# =============================================
# Parser for 'show router isis adjacency detail'
# =============================================
class ShowRouterIsisAdjacencyDetailSchema(MetaParser):
    """Schema for show router isis adjacency detail"""

    schema = {
        'hostname': {
            Any(): {
                'system_id': str,
                'interface': str,
                'state': str,
                'nbr_sys_typ': str,
                'hold_time': int,
                'adj_level': str,
                'topology': str,
                'ipv6_neighbor': str,
                'ipv4_neighbor': str,
                'ipv4_adj_sid': str,
                'restart_support': str,
                'restart_supressed': str,
                'number_of_restarts': int,
                'last_restart_at': str,
                'snpa': str,
                'up_time': str,
                'priority': int,
                'l_circ_typ': str,
                'max_hold': int,
                'mt_enabled': str,
            }
        }
    }