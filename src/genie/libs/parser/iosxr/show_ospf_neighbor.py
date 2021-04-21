"""
    show_ospf_neighbor.py
    IOSXR parsers for the following show commands:

    * show ospf neighbor
    * show ospf {process_name} neighbor
    * show ospf vrf all-inclusive neighbor
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any


# ======================================================
# schema for:
#   * show ospf neighbor
#   * show ospf {process_name} neighbor
#   * show ospf vrf all-inclusive neighbor
# ======================================================

class ShowOspfNeighborSchema(MetaParser):
    """Schema for show ospf neighbor detail"""
    schema = {
        'processes': {
            Any(): {  # process name
                Any(): {  # neighbor id
                    'id': str,
                    'priority': str,
                    'state': str,
                    'dead_time': str,
                    'address': str,
                    'interface': str,
                    'up_time': str
                },
                'total_neighbor_count': int
            }

        }
    }
# ======================================================
# parser for:
#   * show ospf neighbor
#   * show ospf {process_name} neighbor
#   * show ospf vrf all-inclusive neighbor
# ======================================================


class ShowOspfNeighbor(ShowOspfNeighborSchema):
    """output
    Mon Apr 12 11:10:38.799 JST

    * Indicates MADJ interface
    # Indicates Neighbor awaiting BFD session up

    Neighbors for OSPF mpls1

    Neighbor ID     Pri   State           Dead Time   Address         Interface
    100.100.100.100 1     FULL/  -        00:00:38    100.10.0.2      GigabitEthernet0/0/0/0
        Neighbor is up for 2d18h
    95.95.95.95     1     FULL/  -        00:00:38    100.20.0.2      GigabitEthernet0/0/0/1
        Neighbor is up for 2d18h

    Total neighbor count: 2
    """

    cli_command = ['show ospf neighbor', 'show ospf {process_name} neighbor', 'show ospf vrf all-inclusive neighbor']

    def cli(self, process_name='', output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # Neighbors for OSPF mpls1
        p1 = re.compile(r'Neighbors +for +OSPF +(?P<process_name>\w+$)')

        # Neighbor ID     Pri   State           Dead Time   Address         Interface
        # 100.100.100.100 1     FULL/  -        00:00:38    100.10.0.2      GigabitEthernet0/0/0/0
        # 95.95.95.95     1     FULL/  -        00:00:38    100.20.0.2      GigabitEthernet0/0/0/1
        p2 = re.compile(
            r'(?P<neighbor_id>\S+) +(?P<priority>\d+) +(?P<state>\S+\s*\S+) +(?P<dead_time>(\d+:){2}\d+)'
            r' +(?P<address>(\d+\.){3}\d) +(?P<interface>\S+)')

        # Neighbor is up for 2d18h
        p3 = re.compile(r'Neighbor +is +up +for +(?P<up_time>\S+)')

        # Total neighbor count: 2
        p4 = re.compile(r'Total +neighbor +count: +(?P<total_neighbor_count>\S+)')

        for line in out.splitlines():
            line = line.strip()

            # Neighbors for OSPF mpls1
            m = p1.match(line)
            if m:
                process_name = m.groupdict()['process_name']
                processes_dict = ret_dict.setdefault('processes', {}).setdefault(process_name, {})
                continue

            # Neighbor ID     Pri   State           Dead Time   Address         Interface
            # 100.100.100.100 1     FULL/  -        00:00:38    100.10.0.2      GigabitEthernet0/0/0/0
            # 95.95.95.95     1     FULL/  -        00:00:38    100.20.0.2      GigabitEthernet0/0/0/1
            m = p2.match(line)
            if m:
                neighbor_id = m.groupdict()['neighbor_id']
                priority = m.groupdict()['priority']
                state = m.groupdict()['state']
                dead_time = m.groupdict()['dead_time']
                address = m.groupdict()['address']
                interface = m.groupdict()['interface']

                neighbor_dict = processes_dict.setdefault(neighbor_id, {})

                neighbor_dict['id'] = neighbor_id
                neighbor_dict['priority'] = priority
                neighbor_dict['state'] = state
                neighbor_dict['dead_time'] = dead_time
                neighbor_dict['address'] = address
                neighbor_dict['interface'] = interface

                continue

            # Neighbor is up for 2d18h
            m = p3.match(line)
            if m:
                up_time = m.groupdict()['up_time']
                neighbor_dict['up_time'] = up_time

                continue

            # Total neighbor count: 2
            m = p4.match(line)
            if m:
                total_neighbor_count = m.groupdict()['total_neighbor_count']
                processes_dict['total_neighbor_count'] = int(total_neighbor_count)

        return ret_dict
