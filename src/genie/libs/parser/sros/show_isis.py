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
                                        'hold_time': int,
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

                system_id_dict['hold_time'] = hold
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
        'instance': {
            Any(): {
                'level': {
                    Any(): {
                        'interfaces': {
                            Any(): {
                                'system_id': {
                                    Any(): {
                                        'hostname': str,
                                        'state': str,
                                        'nbr_sys_typ': str,
                                        'hold_time': int,
                                        'topology': str,
                                        'ipv6_neighbor': str,
                                        'ipv4_neighbor': str,
                                        'ipv4_adj_sid': str,
                                        'restart_support': str,
                                        'restart_supressed': str,
                                        'restart_status': str,
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
                        }
                    }
                }
            }
        }
    }


# =============================================
# Helper Functions for ShowRouterIsisAdjacencyDetail
# =============================================

# Build a child dictionary for the final result
def build_level_dict(s, pattern):
    level_dict = {}
    m = pattern.match(s)
    group = m.groupdict()
    system_id_dict = level_dict.setdefault('level', {}). \
        setdefault(group['adj_level'], {}). \
        setdefault('interfaces', {}). \
        setdefault(group['interface'], {}). \
        setdefault('system_id', {}). \
        setdefault(group['system_id'], {})

    str_keys = ['hostname', 'state', 'nbr_sys_typ', 'topology',
                'ipv6_neighbor', 'ipv4_neighbor', 'ipv4_adj_sid',
                'restart_support', 'restart_supressed', 'restart_status', 'last_restart_at',
                'snpa', 'up_time', 'l_circ_typ', 'mt_enabled']
    int_keys = ['hold_time', 'number_of_restarts', 'priority', 'max_hold']

    for k in str_keys:
        system_id_dict[k] = group[k].strip()

    for k in int_keys:
        system_id_dict[k] = int(group[k])

    return level_dict


# Merge two dictionaries
# reference: https://bit.ly/36y1M1L
def merge_dicts(dict1, dict2):
    for k in set(dict1.keys()).union(dict2.keys()):
        if k in dict1 and k in dict2:
            if isinstance(dict1[k], dict) and isinstance(dict2[k], dict):
                yield (k, dict(merge_dicts(dict1[k], dict2[k])))
            else:
                # If one of the values is not a dict, you can't continue merging it.
                # Value from second dict overrides one in first and we move on.
                yield (k, dict2[k])
                # Alternatively, replace this with exception raiser to alert you of value conflicts
        elif k in dict1:
            yield (k, dict1[k])
        else:
            yield (k, dict2[k])


def prepare_text(t, pattern):
    result = {}

    # Rtr Base ISIS Instance 0 Adjacency (detail)
    p0 = re.compile(r'Rtr Base ISIS Instance (?P<instance>\d+) Adjacency \(detail\)')

    home_block = ''
    home_dicts = {}
    instance_num = None
    for line in t.splitlines():

        if 'Rtr Base ISIS Instance' in line:
            line = line.strip()

        m = p0.match(line)
        if m:
            instance_num = m.groupdict()['instance']
            home_dicts = {}

            continue

        if 'Last Restart at' in line:
            result.setdefault('instance', {})
            # build level dict
            home_block += line
            curr_dict = build_level_dict(home_block.strip(), pattern)
            home_dicts = dict(merge_dicts(curr_dict, home_dicts))
            home_block = ''

            # insert the level dictionaries into the instance dictionary
            result['instance'][instance_num] = home_dicts
            continue

        elif 'Hostname' in line or len(home_block) > 0:
            home_block += line
            continue

    return result


class ShowRouterIsisAdjacencyDetail(ShowRouterIsisAdjacencyDetailSchema):
    """ Parser for show router isis adjacency detail"""

    cli_command = 'show router isis adjacency detail'

    def cli(self, output=None):

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        p = re.compile(r'^Hostname +: +(?P<hostname>\S+)'
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

        result = prepare_text(out, p)

        return result



class ShowRouterIsisAdjacencyDetailOld(ShowRouterIsisAdjacencyDetailSchema):
    """ Parser for show router isis adjacency detail"""

    cli_command = 'show router isis adjacency detail'

    def cli(self, output=None):

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # ============================================
        # regex patterns
        # ============================================
        p0 = re.compile(r'Rtr Base ISIS Instance (?P<instance>\d+) Adjacency \(detail\)')

        # Hostname    : COPQON05R07
        p1 = re.compile(r'^Hostname +: +(?P<hostname>\S+)$')
        # SystemID    : 0691.5819.6089                   SNPA        : 00:23:3e:8f:17:97
        p2 = re.compile(r'^SystemID +: +(?P<system_id>\S+) +SNPA +: +(?P<snpa>\S+)$')
        # Interface   : To-COPQON05R07-LAG-7             Up Time     : 58d 03:24:48
        p3 = re.compile(r'^Interface +: +(?P<interface>\S+) +Up Time +: +(?P<up_time>[\s\S]+)$')
        # State       : Up                               Priority    : 0
        p4 = re.compile(r'^State +: +(?P<state>\S+) +Priority +: +(?P<priority>\d+)$')
        # Nbr Sys Typ : L2                               L. Circ Typ : L2
        p5 = re.compile(r'^Nbr Sys Typ +: +(?P<nbr_sys_typ>\S+) +L. Circ Typ +: +(?P<l_circ_typ>\S+)$')
        # Hold Time   : 22                               Max Hold    : 30
        p6 = re.compile(r'^Hold Time +: +(?P<hold_time>\d+) +Max Hold +: +(?P<max_hold>\d+)$')
        # Adj Level   : L2                               MT Enabled  : No
        p7 = re.compile(r'^Adj Level +: +(?P<adj_level>\S+) +MT Enabled +: +(?P<mt_enabled>\S+)$')
        # Topology    : Unicast
        p8 = re.compile(r'^Topology +: +(?P<topology>\S+)$')
        # IPv6 Neighbor     : ::
        p9 = re.compile(r'^IPv6 Neighbor +: +(?P<ipv6_neighbor>\S+)$')
        # IPv4 Neighbor     : 10.11.97.22
        p10 = re.compile(r'^IPv4 Neighbor +: +(?P<ipv4_neighbor>\S+)$')
        # IPv4 Adj SID      : Label 524213
        p11 = re.compile(r'^IPv4 Adj SID +: +(?P<ipv4_adj_sid>[\S\s]+)$')
        # Restart Support   : Disabled
        p12 = re.compile(r'^Restart Support +: +(?P<restart_support>\S+)$')
        # Restart Status    : Not currently being helped
        p13 = re.compile(r'^Restart Status +: +(?P<restart_status>[\s\S]+)$')
        # Restart Supressed : Disabled
        p14 = re.compile(r'^Restart Supressed +: +(?P<restart_supressed>\S+)$')
        # Number of Restarts: 0
        p15 = re.compile(r'^Number of Restarts: +(?P<number_of_restarts>\d+)$')
        # Last Restart at   : Never
        p16 = re.compile(r'^Last Restart at +: +(?P<last_restart_at>\S+)$')

        parsed_dict = {}
        tmp = {}
        for line in out.splitlines():
            line = line.strip()

            m = p0.match(line)
            if m:
                instance_dict = parsed_dict.setdefault('instance', {}).\
                                            setdefault(m.groupdict()['instance'], {})
                continue

            m = p7.match(line)
            if m:
                group = m.groupdict()
                level_num = group['adj_level']
                mt_enabled = group['mt_enabled']

                system_dict['mt_enabled'] = mt_enabled
                continue

            m = p3.match(line)
            if m:
                group = m.groupdict()
                interface = group['interface']
                up_time = group['up_time']

                system_dict['up_time'] = up_time
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                system_id = group['system_id']
                snpa = group['snpa']


                system_dict = tmp.setdefault('system_id', {}).\
                                             setdefault(system_id, {})
                system_dict['snpa'] = snpa
                system_dict['hostname'] = hostname
                continue

            m = p1.match(line)
            if m:
                hostname = m.groupdict()['hostname']
                continue

            m =p4.match(line)
            if m:
                system_dict['state'] = m.groupdict()['state']
                system_dict['priority'] = int(m.groupdict()['priority'])
                continue

            m = p5.match(line)
            if m:
                system_dict['nbr_sys_typ'] = m.groupdict()['nbr_sys_typ']
                system_dict['l_circ_typ'] = m.groupdict()['l_circ_typ']
                continue

            m = p6.match(line)
            if m:
                system_dict['hold_time'] = int(m.groupdict()['hold_time'])
                system_dict['max_hold'] = int(m.groupdict()['max_hold'])
                continue

            m = p8.match(line)
            if m:
                system_dict['topology'] = m.groupdict()['topology']
                continue

            m = p9.match(line)
            if m:
                system_dict['ipv6_neighbor'] = m.groupdict()['ipv6_neighbor']
                continue

            m = p10.match(line)
            if m:
                system_dict['ipv4_neighbor'] = m.groupdict()['ipv4_neighbor']
                continue

            m = p11.match(line)
            if m:
                system_dict['ipv4_adj_sid'] = m.groupdict()['ipv4_adj_sid']
                continue

            m = p12.match(line)
            if m:
                system_dict['restart_support'] = m.groupdict()['restart_support']
                continue

            m = p13.match(line)
            if m:
                system_dict['restart_status'] = m.groupdict()['restart_status']
                continue

            m = p14.match(line)
            if m:
                system_dict['restart_supressed'] = m.groupdict()['restart_supressed']
                continue

            m = p15.match(line)
            if m:
                system_dict['number_of_restarts'] = int(m.groupdict()['number_of_restarts'])

                continue

            m = p16.match(line)
            if m:
                system_dict['last_restart_at'] = m.groupdict()['last_restart_at']
                instance_dict.setdefault('level', {}).\
                    setdefault(level_num, {}).\
                    setdefault('interfaces', {}).\
                    setdefault(interface, {}).\
                    setdefault('system_id', {}).\
                    setdefault(system_id, system_dict)
                continue

        return parsed_dict

