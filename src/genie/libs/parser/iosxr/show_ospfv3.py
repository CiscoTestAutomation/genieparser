''' show_ospfv3.py

Parser for the following commands:
    * show ospfv3 neighbor
    * show ospfv3 {process} neighbor
    * show ospfv3 vrf {vrf} neighbor

'''
import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


class ShowOspfv3NeighborSchema(MetaParser):
    """ Schema for:
    * show ospfv3 neighbor
    """
    schema = {
        'process': str,
        'vrfs': {
            Any(): {
                'neighbors': {
                    Any(): {
                        'priority': str,
                        'state': str,
                        'dead_time': str,
                        'address': str,
                        'interface': str,
                        'up_time': str
                    }
                },
                Optional('total_neighbor_count'): int
            }
        }
    }


class ShowOspfv3Neighbor(ShowOspfv3NeighborSchema):
    """ Schema for:
    * show ospfv3 neighbor
    """
    cli_command = [
        'show ospfv3 neighbor',
        'show ospfv3 {process} neighbor',
        'show ospfv3 vrf {vrf} neighbor',
        'show ospfv3 {process} vrf {vrf} neighbor',
    ]

    def cli(self, process="", vrf="", output=None):
        if output is None:
            if process:
                if vrf:
                    out = self.device.execute(
                        self.cli_command[3].format(process=process, vrf=vrf))
                else:
                    out = self.device.execute(
                        self.cli_command[1].format(process=process))
            elif vrf:
                out = self.device.execute(
                    self.cli_command[2].format(vrf=vrf))
            else:
                out = self.device.execute(self.cli_command[0])
        else:
            out = output

        result_dict = {}

        # Neighbors for OSPFv3 1
        # Neighbors for OSPFv3 1, VRF default
        # Neighbors for OSPFv3 1, VRF VRF1
        p1 = re.compile(r'^Neighbors +for +OSPFv3 +(?P<process>\w+)'
                        '(, +VRF (?P<vrf>[\w]+))?$')

        # Neighbor ID     Pri   State           Dead Time   Interface ID    Interface
        # 95.95.95.95     1     FULL/  -        00:00:37    5               GigabitEthernet0/0/0/1
        # 100.100.100.100 1     FULL/  -        00:00:38    6               GigabitEthernet0/0/0/0
        p2 = re.compile(r'^(?P<neighbor_id>\S+) +(?P<priority>\d+)'
                        ' +(?P<state>\S+\s*\S+) +(?P<dead_time>\S+)'
                        ' +(?P<address>\S+) +(?P<interface>\S+)$')

        # Neighbor is up for 2d18h
        # Neighbor is up for 2d19h
        p3 = re.compile(r'^Neighbor +is +up +for +(?P<up_time>\S+)$')

        # Total neighbor count: 2
        p4 = re.compile(r'^Total +neighbor +count:'
                        ' +(?P<total_neighbor_count>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            # Neighbors for OSPF mpls1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                result_dict['process'] = group['process']

                vrfs_dict = result_dict.setdefault('vrfs', {})

                vrf_name = group['vrf'] if group['vrf'] \
                    else 'default'
                vrf_dict = vrfs_dict.setdefault(vrf_name, {})

                neighbors_dict = vrf_dict.setdefault('neighbors', {})
                continue

            # Neighbor ID     Pri   State           Dead Time   Interface ID    Interface
            # 95.95.95.95     1     FULL/  -        00:00:37    5               GigabitEthernet0/0/0/1
            # 100.100.100.100 1     FULL/  -        00:00:38    6               GigabitEthernet0/0/0/0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                neighbor_dict = neighbors_dict.setdefault(
                    group['neighbor_id'], {})

                neighbor_dict.update({
                    'priority': group['priority'],
                    'state': group['state'],
                    'dead_time': group['dead_time'],
                    'address': group['address'],
                    'interface': group['interface']
                })
                continue

            # Neighbor is up for 2d18h
            m = p3.match(line)
            if m:
                group = m.groupdict()
                neighbor_dict['up_time'] = group['up_time']
                continue

            # Total neighbor count: 2
            m = p4.match(line)
            if m:
                group = m.groupdict()
                vrf_dict['total_neighbor_count'] = \
                    int(group['total_neighbor_count'])

        return result_dict
