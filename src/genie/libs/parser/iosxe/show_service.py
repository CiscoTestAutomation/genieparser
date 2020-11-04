'''show_service.py
IOSXE parser for the following show command
	* show service-group state
	* show service-group stats
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
            Any, Optional

# import parser utils
from genie.libs.parser.utils.common import Common


# ==============================================================
# Parser for 'show service-group state'
# ==============================================================
class ShowServiceGroupStateSchema(MetaParser):
    """
	Schema for show service-group state
	"""

    schema = {'group': {Any(): {'state': str}}}


class ShowServiceGroupState(ShowServiceGroupStateSchema):
    """
	Parser for 'show service-group state'
	"""

    cli_command = 'show service-group state'

    def cli(self, output=None):
        if output is None:
            #execute command to get output
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial variables
        ret_dict = {}

        #     1            Up
        p1 = re.compile(r'^\s*(?P<group_number>\d+) +(?P<state>\S+)$')

        for line in out.splitlines():
            line = line.strip()
            #     1            Up
            m = p1.match(line)
            if m:
                group = m.groupdict()
                service_group_state = ret_dict.setdefault(
                    'group', {}).setdefault(group['group_number'], {})
                service_group_state.update({'state': group['state']})
                continue
        return ret_dict


# ==============================================================
# Parser for 'show service-group stats'
# ==============================================================
class ShowServiceGroupStatsSchema(MetaParser):
    """
	Schema for show service-group stats
	"""

    schema = {
        'service_group_statistics': {
            'global': {
                'num_of_groups': int,
                'num_of_members': int
            },
            Any(): {
                'num_of_interfaces': int,
                'num_of_members': {
                    int: {
                        Any(): int
                    }
                },
                'members_joined': int,
                'members_left': int
            }
        }
    }


class ShowServiceGroupStats(ShowServiceGroupStatsSchema):
    """ Parser for 'show service-group stats"""

    cli_command = 'show service-group stats'

    def cli(self, output=None):
        if output is None:
            #execute command to get output
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial variables
        ret_dict = {}
        global_statistics_found = False
        group_statistics_found = False

        # Service Group global statistics:
        p1 = re.compile(r'^\s*Service +Group +global +statistics:$')

        # Number of groups:          1
        p2 = re.compile(r'^\s*Number +of +groups: +(?P<num_of_groups>\d+)$')

        # Number of members:
        p3 = re.compile(r'^\s*Number +of +members: +(?P<num_of_members>\d+)$')

        # Service Group 1 statistics:
        p4 = re.compile(
            r'^\s*Service +Group +(?P<group_statistics>\d+) +statistics:$')

        # Number of Interfaces:      1
        p5 = re.compile(
            r'^\s*Number +of +Interfaces: +(?P<num_of_interfaces>\d+)$')

        #  Number of members:         2
        p6 = re.compile(r'^\s*Number +of +members: +(?P<num_of_members>\d+)$')

        #    Sub-interface:           2
        p7 = re.compile(
            r'^\s*(?P<interface_name>[\w\W]+):? +(?P<sub_interface>\d+)$')

        # Members joined:            103
        p8 = re.compile(r'^\s*Members +joined: +(?P<members_joined>\d+)$')

        # Members left:              101
        p9 = re.compile(r'^\s*Members +left: +(?P<members_left>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            if not global_statistics_found:
                # Service Group global statistics:
                m = p1.match(line)
                if m:
                    service_group_statistics = ret_dict.setdefault( \
                     'service_group_statistics', {})
                    global_statistics = service_group_statistics.setdefault( \
                     'global', {})
                    global_statistics_found = True
                    group_statistics_found = False
                    continue
            else:
                # Number of groups:          1
                m = p2.match(line)
                if m:
                    group = m.groupdict()
                    global_statistics.update(
                        {k: int(v)
                         for k, v in group.items()})
                    continue

# Number of members:         2
                m = p3.match(line)
                if m:
                    group = m.groupdict()
                    global_statistics.update(
                        {k: int(v)
                         for k, v in group.items()})
                    continue

            if not group_statistics_found:
                # Service Group 1 statistics:
                m = p4.match(line)
                if m:
                    group = m.groupdict()
                    group_statistics = service_group_statistics.setdefault( \
                     group['group_statistics'], {})
                    group_statistics_found = True
                    global_statistics_found = False
                    continue

            else:
                # Number of Interfaces:          1
                m = p5.match(line)
                if m:
                    group = m.groupdict()
                    group_statistics.update(
                        {k: int(v)
                         for k, v in group.items()})
                    continue

# Number of members:         2
                m = p6.match(line)
                if m:
                    group = m.groupdict()
                    num_of_members = group_statistics. \
                     setdefault('num_of_members', {}). \
                     setdefault(int(group['num_of_members']), {})
                    continue

# Members joined:         103
                m = p8.match(line)
                if m:
                    group = m.groupdict()
                    group_statistics.update(
                        {k: int(v)
                         for k, v in group.items()})
                    continue

# Members left:         101
                m = p9.match(line)
                if m:
                    group = m.groupdict()
                    group_statistics.update(
                        {k: int(v)
                         for k, v in group.items()})
                    group_statistics_found = False
                    continue

                # Sub-Interface:         2
                m = p7.match(line)
                if m:
                    group = m.groupdict()
                    key = group['interface_name'].rstrip() \
                    .replace('-','_').replace(' ','_').lower()
                    num_of_members.update({key: int(group['sub_interface'])})
                    continue

        return ret_dict


# ====================================================
#  parser for show service-group traffic-stats
# ====================================================
class ShowServiceGroupTrafficStatsSchema(MetaParser):
    """Schema for:
		show service-group traffic-stats
		show service-group traffic-stats <group> """

    schema = {
        'group': {
            Any(): {
                'pkts_in': int,
                'pkts_out': int,
                'bytes_in': int,
                'bytes_out': int,
            },
        }
    }


class ShowServiceGroupTrafficStats(ShowServiceGroupTrafficStatsSchema):
    """Parser for :
		show service-group traffic-stats
		show service-group traffic-stats <group> """

    cli_command = [
        'show service-group traffic-stats',
        'show service-group traffic-stats {group}'
    ]

    def cli(self, group="", output=None):
        if output is None:
            if group:
                cmd = self.cli_command[1].format(group=group)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        # initialize result dict
        result_dict = {}

        # Group    Pkts In   Bytes In   Pkts Out  Bytes Out
        #     1         78      10548        172      18606
        p1 = re.compile(
            r'^\s*(?P<num>[\d]+) +(?P<pkts_in>[\d]+) +(?P<bytes_in>[\d]+)'
            ' +(?P<pkts_out>[\d]+) +(?P<bytes_out>[\d]+)$')

        for line in out.splitlines():
            line = line.rstrip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                num = int(group.pop('num'))
                g_dict = result_dict.setdefault('group',
                                                {}).setdefault(num, {})
                g_dict.update({k: int(v) for k, v in group.items()})
                continue

        return result_dict


# ========================================================================
# Schema for 'show service-insertion type appqoe service-node-group'
# ========================================================================
class ShowServiceInsertionTypeAppqoeServiceNodeGroupSchema(MetaParser):
    """ Schema for show service-insertion type appqoe service-node-group """
    schema = {
        'service_node_group_name': {
            str: {
                'service_context': str,
                'member_service_node_count': int,
            }
        },
        'service_node_sn': str,
        'auto_discovered': str,
        'sn_belongs_to_sng': str,
        'current_status_of_sn': str,
        Optional('system_ip'): str,
        Optional('site_id'): int,
        'time_current_status_was_reached': str,
        Optional('cluster_protocol_vpath_version'): str,
        Optional('cluster_protocol_incarnation_number'): int,
        'cluster_protocol_last_sent_sequence_number': int,
        'cluster_protocol_last_received_sequence_number': int,
        'cluster_protocol_last_received_ack_number': int
    }


# ========================================================================
# Parser for 'show service-insertion type appqoe service-node-group'
# ========================================================================
class ShowServiceInsertionTypeAppqoeServiceNodeGroup(
        ShowServiceInsertionTypeAppqoeServiceNodeGroupSchema):
    """ Parser for "show service-insertion type appqoe service-node-group" """

    cli_command = "show service-insertion type appqoe service-node-group"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Service Node Group name         : SNG-APPQOE
        p0 = re.compile(r'^Service +Node +Group +name *: +(?P<name>\S+)$')
        #     Service Context             : appqoe/1
        p0_1 = re.compile(r'^Service +Context *: +(?P<context>\S+)$')
        #     Member Service Node count   : 1
        p0_2 = re.compile(r'^Member +Service +Node +count *: +(?P<count>\d+)$')

        # Service Node (SN)                   : 192.168.2.2
        # Auto discovered                     : No
        # SN belongs to SNG                   : SNG-APPQOE
        # Current status of SN                : Alive
        # System IP                           : 10.220.100.6
        # Site ID                             : 30
        # Time current status was reached               : Tue Sep 15 18:22:11 2020
        # Cluster protocol VPATH version                : 1 (Bitmap recvd: 1)
        # Cluster protocol incarnation number           : 5
        # Cluster protocol last sent sequence number    : 1600512340
        # Cluster protocol last received ack number     : 1600512339
        p1 = re.compile(r'^(?P<key>[\s\S]+\S) +: +(?P<value>[\s\S]+)$')

        # Cluster protocol last received sequence number: 311442
        p2 = re.compile(r'^(?P<key>[\s\S]+\w)+: +(?P<value>[\s\S]+)$')

        parsed_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # Service Node Group name         : SNG-APPQOE
            m = p0.match(line)
            if m:
                group = m.groupdict()
                service_nodes = parsed_dict.setdefault(
                    'service_node_group_name', {})
                service_node = service_nodes.setdefault(group['name'], {})
                continue

            #   Service Context             : appqoe/1
            m = p0_1.match(line)
            if m:
                group = m.groupdict()
                service_node['service_context'] = group['context']
                continue

            #   Member Service Node count   : 1
            m = p0_2.match(line)
            if m:
                group = m.groupdict()
                service_node['member_service_node_count'] = int(group['count'])
                continue

            # Service Node (SN)                   : 192.168.2.2
            # Auto discovered                     : No
            # SN belongs to SNG                   : SNG-APPQOE
            # Current status of SN                : Alive
            # System IP                           : 10.220.100.6
            # Site ID                             : 30
            # Time current status was reached               : Tue Sep 15 18:22:11 2020
            # Cluster protocol VPATH version                : 1 (Bitmap recvd: 1)
            # Cluster protocol incarnation number           : 5
            # Cluster protocol last sent sequence number    : 1600512340
            # Cluster protocol last received ack number     : 1600512339
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                key = groups['key'].strip(')').replace('(', '_').replace(
                    ' ', '_').replace('__', '_').lower()
                try:
                    value = int(groups['value'])
                except ValueError:
                    value = groups['value']
                parsed_dict.update({key: value})
                continue

            # Cluster protocol last received sequence number: 311442
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                key = groups['key'].replace(' ', '_').lower()
                parsed_dict.update({key: int(groups['value'])})

        return parsed_dict
