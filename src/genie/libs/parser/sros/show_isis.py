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
        'instance': {
            Any(): {
                'level': {
                    Any(): {
                        'total_adjacency_count': int,
                        'interfaces': {
                            Any(): {
                                'system_id': {
                                    Any(): {
                                        'hold': int,
                                        'state': str,
                                        'mt_id': int,
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
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

        # Rtr Base ISIS Instance 0 Adjacency
        p0 = re.compile(r'^Rtr Base ISIS Instance (?P<instance>\d+) Adjacency$')

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

            m = p0.match(line)
            if m:
                instance_dict = parsed_dict.setdefault('instance', {})\
                                            .setdefault(m.groupdict()['instance'], {})
                continue

            m = p1.match(line)
            if m:
                group = m.groupdict()
                system_id = group['system_id']
                level = group['usage']
                state = group['state']
                hold = int(group['hold'])
                interface = group['interface']
                mt_id = int(group['mt_id'])

                level_dict = instance_dict.setdefault('level', {}).setdefault(level, {})

                interfaces_dict = level_dict.setdefault('interfaces', {}).setdefault(interface, {})

                system_id_dict = interfaces_dict.setdefault('system_id', {}).setdefault(system_id, {})

                system_id_dict['hold'] = hold
                system_id_dict['state'] = state
                system_id_dict['mt_id'] = mt_id

                continue

            # Adjacencies: 3
            m = p2.match(line)
            if m:
                count = int(m.groupdict()['adjacencies'])
                level_dict['total_adjacency_count'] = count
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

class ShowRouterIsisAdjacencyDetailSchema2(MetaParser):
    """Schema for show router isis adjacency detail"""

    schema = {
        'hostname': {
            Any(): {
                'system_id': str,
                'state': str,
                'snpa': str,
                'interface': str,
                'up_time': str,
                'priority': int,
            }
        }
    }

class ShowRouterIsisAdjacencyDetail(ShowRouterIsisAdjacencyDetailSchema):
    """ Parser for show router isis adjacency detail"""

    cli_command = 'show router isis adjacency detail'

    def cli(self, output=None):
        import time
        start_time = time.time()

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}

        p = re.compile(r'^: +(?P<hostname>\S+)'
                       r' +SystemID +: +(?P<system_id>\S+) +SNPA +: +(?P<snpa>\S+)'
                       r' +Interface +: +(?P<interface>\S+) +Up Time +: +(?P<up_time>[\S]+ [\S]+)'
                       r' +State +: +(?P<state>\S+) +Priority +: +(?P<priority>\d+)'
                       r' +Nbr Sys Typ +: +(?P<nbr_sys_typ>\S+) +L. Circ Typ +: +(?P<l_circ_typ>\S+)'
                       r' +Hold Time +: +(?P<hold_time>\d+) +Max Hold +: +(?P<max_hold>\d+)'
                       r' +Adj Level +: +(?P<adj_level>\S+) +MT Enabled +: +(?P<mt_enabled>\S+)'
                       r' +Topology +: +(?P<topology>\S+)'
                       r' +IPv6 Neighbor +: +(?P<ipv6_neighbor>\S+)'
                       r' +IPv4 Neighbor +: +(?P<ipv4_neighbor>\S+)'
                       r' +IPv4 Adj SID +: +(?P<ipv4_adj_sid>\S+ \d+)'
                       r' +Restart Support +: +(?P<restart_support>\S+)'
                       r' +Restart Status +: +(?P<restart_status>[ \S]+)'
                       r' +Restart Supressed +: +(?P<restart_supressed>\S+)'
                       r' +Number of Restarts: (?P<number_of_restarts>\d+)'
                       r'  +Last Restart at +: +(?P<last_restart_at>\S+)')

        content_str = out.split('===============================================================================')[-1]
        content_list = content_str.strip().split('Hostname')

        for c in content_list:
            c_str = c.replace('\n', '').strip()
            m = p.match(c_str)
            if m:
                group = m.groupdict()
                # ==============
                # next step: grab group['key'] and construct the dictionary
                # ==============
                print('yes')



        print("--- %s seconds ---" % (time.time() - start_time))
        import pdb
        pdb.set_trace()
        return parsed_dict



