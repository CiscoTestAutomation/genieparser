"""
    show_ospf_neighbor.py
    IOSXR parsers for the following show commands:
        * show ospf neighbor
        * show ospf {process_name} neighbor
        * show ospf vrf {vrf} neighbor
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# ======================================================
# schema for:
#   * show ospf neighbor
#   * show ospf {process_name} neighbor
#   * show ospf vrf {vrf} neighbor
# ======================================================
class ShowOspfNeighborSchema(MetaParser):
    """Schema detail for:
          * show ospf neighbor
          * show ospf {process_name} neighbor
          * show ospf vrf {vrf} neighbor
     """
    schema = {
        Optional('process_name'): str,
        'vrfs': {
            Any(): {
                'neighbors': {
                    Optional(Any()): { # neighbor_id
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


# ======================================================
# parser for:
#   * show ospf neighbor
#   * show ospf {process_name} neighbor
#   * show ospf vrf {vrf} neighbor
# ======================================================
class ShowOspfNeighbor(ShowOspfNeighborSchema):
    """parser details for:
        * show ospf neighbor
        * show ospf {process_name} neighbor
        * show ospf vrf all-inclusive neighbor
    """

    cli_command = ['show ospf neighbor', 'show ospf {process_name} neighbor', 'show ospf vrf {vrf} neighbor']

    def cli(self, process_name='', vrf='', output=None):
        if output is None:
            if process_name:
                out = self.device.execute(
                    self.cli_command[1].format(process_name=process_name))
            elif vrf:
                out = self.device.execute(
                    self.cli_command[2].format(vrf=vrf))
            else:
                out = self.device.execute(self.cli_command[0])
        else:
            out = output

        ret_dict = {}

        if out:
            # process_name is passed from cli
            if process_name:
                ret_dict['process_name'] = process_name

        # Neighbors for OSPF
        p1 = re.compile(r'^Neighbors +for +OSPF')
        # Neighbors for OSPFv3 mpls1
        p1_1 = re.compile(r'^Neighbors +for +OSPF\w* +(?P<process_name>\w+)$')
        # Neighbors for OSPFv3 mpls1, VRF 1
        p1_2 = re.compile(r'Neighbors +for +OSPF\w* +(?P<process_name>\w+), VRF +(?P<vrf>\S+)')

        # Neighbor ID     Pri   State           Dead Time   Address         Interface
        # 100.100.100.100 1     FULL/  -        00:00:38    100.10.0.2      GigabitEthernet0/0/0/0
        # 95.95.95.95     1     FULL/  -        00:00:38    100.20.0.2      GigabitEthernet0/0/0/1
        # 192.168.199.137 1    FULL/DR       0:00:31    172.31.80.37      GigabitEthernet 0/3/0/2
        p2 = re.compile(r'^(?P<neighbor_id>\S+)\s+(?P<priority>\d+) +(?P<state>[A-Z]+/\s{0,3}[A-Z-]*)'
                        r' +(?P<dead_time>(\d+:){2}\d+) +(?P<address>(\d+\.){3}\d+) +(?P<interface>\w+\s*\S+)$')

        # Neighbor is up for 2d18h
        p3 = re.compile(r'^Neighbor +is +up +for +(?P<up_time>\S+)$')

        # Total neighbor count: 2
        p4 = re.compile(r'^Total +neighbor +count: +(?P<total_neighbor_count>\S+)$')

        for line in out.splitlines():
            line = line.strip()

            # Neighbors for OSPF
            m = p1.match(line)
            if m:
                # Neighbors for OSPFv3 mpls1
                m = p1_1.match(line)
                if m:
                    process_name = m.groupdict()['process_name']

                    ret_dict['process_name'] = process_name
                    vrfs_dict = ret_dict.setdefault('vrfs', {})

                    vrf_dict = vrfs_dict.setdefault('default', {})
                    neighbors_dict = vrf_dict.setdefault('neighbors', {})
                    continue

                # Neighbors for OSPFv3 mpls1, VRF 1
                m = p1_2.match(line)
                if m:
                    process_name = m.groupdict()['process_name']
                    vrf_name = m.groupdict()['vrf']

                    ret_dict['process_name'] = process_name
                    vrfs_dict = ret_dict.setdefault('vrfs', {})

                    vrf_dict = vrfs_dict.setdefault(vrf_name, {})
                    neighbors_dict = vrf_dict.setdefault('neighbors', {})
                    continue

                # Neighbors for OSPF
                vrfs_dict = ret_dict.setdefault('vrfs', {})
                vrf_dict = vrfs_dict.setdefault('default', {})
                neighbors_dict = vrf_dict.setdefault('neighbors', {})

                continue

            # Neighbor ID     Pri   State           Dead Time   Address         Interface
            # 100.100.100.100 1     FULL/  -        00:00:38    100.10.0.2      GigabitEthernet0/0/0/0
            # 95.95.95.95     1     FULL/  -        00:00:38    100.20.0.2      GigabitEthernet0/0/0/1
            # 192.168.199.137 1    FULL/DR       0:00:31    172.31.80.37      GigabitEthernet 0/3/0/2
            m = p2.match(line)
            if m:
                neighbor_id = m.groupdict()['neighbor_id']
                priority = m.groupdict()['priority']
                state = m.groupdict()['state']
                dead_time = m.groupdict()['dead_time']
                address = m.groupdict()['address']
                interface = m.groupdict()['interface']

                neighbor_dict = neighbors_dict.setdefault(neighbor_id, {})

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
                vrf_dict['total_neighbor_count'] = int(total_neighbor_count)

        return ret_dict
