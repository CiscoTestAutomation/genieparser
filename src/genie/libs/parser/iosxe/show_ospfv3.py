""" ShowOspfv3SummaryPrefix.py

IOSXE parser for the following show command:
    * show ospfv3 summary-prefix
"""

# python
import re

# metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional, Use, Default

# ===============================================
# Schema for 'show ospfv3 summary-prefix'
# Optional: allowing either ipv4 or ipv6 or both
# ===============================================

class ShowOspfv3SummaryPrefixSchema(MetaParser):
    schema = {
        'process_id': {
            Any(): {
                'address_family': str,
                'router_id': str,
                'null_route': {
                    Any(): {
                        'null_metric': str,
                    },
                },
                'summary': {
                    Any(): {
                        'sum_type': str,
                        'sum_tag': int,
                        'sum_metric': int
                    },
                },
            },
        },
    }


# ====================================
# Parser for 'ShowOspfv3SummaryPrefix'
# ====================================

class ShowOspfv3SummaryPrefix(ShowOspfv3SummaryPrefixSchema):
    """
        Router#sh ospfv3 summary-prefix

                OSPFv3 10000 address-family ipv6 (router-id 10.2.2.21)

        10:2::/96           Metric <unreachable>
        10:2:2::/96         Metric 111, External metric type 2, Tag 111
        Router#
    """

    cli_command = 'show ospfv3 summary-prefix'

    def cli(self, output=None):

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # init var
        ret_dict = {}
        ospf_id = ""

        # OSPFv3 10000 address-family ipv6 (router-id 10.2.2.21)
        p1 = re.compile(
            r'^OSPFv3 +(?P<ospf_id>(\d+)) +address-family +(?P<address_family>(\S+)) +\(router-id +(?P<router_id>(\S+))\)')

        # 10:2::/96           Metric <unreachable>
        p2 = re.compile(r'^(?P<null_prefix>(\S+)) +.* Metric\s+(?P<null_metric>(\S+$))')

        # 10:2:2::/96         Metric 111, External metric type 2, Tag 111
        p3 = re.compile(
            r'^(?P<sum_prefix>(\S+)) +.* Metric\s+(?P<sum_metric>(\d+)),.* +type +(?P<sum_type>(\d)),\s+Tag +(?P<sum_tag>(\S+))')

        for line in out.splitlines():
            line = line.strip()
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['process_id'] = {}
                ospf_id = group['ospf_id']
                ret_dict['process_id'][ospf_id] = {}
                ret_dict['process_id'][ospf_id]['null_route'] = {}
                ret_dict['process_id'][ospf_id]['summary'] = {}
                ret_dict['process_id'][ospf_id]['address_family'] = group['address_family']
                ret_dict['process_id'][ospf_id]['router_id'] = group['router_id']
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                if group['null_prefix']:
                    n_prefix = group['null_prefix']
                    ret_dict['process_id'][ospf_id]['null_route'][n_prefix] = {}
                    ret_dict['process_id'][ospf_id]['null_route'][n_prefix]['null_metric'] = group['null_metric']
                    continue

            m = p3.match(line)
            if m:
                group = m.groupdict()
                if group['sum_prefix']:
                    prefix = group['sum_prefix']
                    ret_dict['process_id'][ospf_id]['summary'][prefix] = {}
                    ret_dict['process_id'][ospf_id]['summary'][prefix]['sum_metric'] = int(group['sum_metric'])
                    ret_dict['process_id'][ospf_id]['summary'][prefix]['sum_type'] = group['sum_type']
                    ret_dict['process_id'][ospf_id]['summary'][prefix]['sum_tag'] = int(group['sum_tag'])
                    continue


        return ret_dict

# ===============================================
# schema for:
#   * show ospfv3 vrf {vrf_id} neighbor
# ======================================================
class ShowOspfv3vrfNeighborSchema(MetaParser):
    """Schema detail for:
          * show ospfv3 vrf {vrf_id} neighbor
     """
    schema = {
        'process_id': int,
        'address_family': str,
        'router_id': str,
        'vrfs': {
            int: {
                'neighbor_id': {
                    str: {
                        'priority': int,
                        'state': str,
                        'dead_time': str,
                        'address': int,
                        'interface': str
                        },
                   },
               },
            },
        }

# ======================================================
# parser for:
#   * show ospfv3 vrf {vrf_id} neighbor
# ======================================================
class ShowOspfv3vrfNeighbor(ShowOspfv3vrfNeighborSchema):
    """parser details for:
        * show ospfv3 vrf {vrf_id} neighbor
    """

    cli_command = 'show ospfv3 vrf {vrf_id} neighbor'

    def cli(self, vrf_id='', output=None):
        cmd = self.cli_command.format(vrf_id=vrf_id)

        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        # OSPFv3 2 address-family ipv6 vrf 2 (router-id 173.19.2.2)
        p1 = re.compile(
            r'^OSPFv3\s+(?P<process_id>\d+)+\s+address-family\s(?P<address_family>\w+)\s+vrf\s(?P<vrf_id>\d+)'
            r'\s+\(router-id\s+(?P<router_id>[\d\.\/]+)\)$')

        # Neighbor ID     Pri   State           Dead Time   Address         Interface
        # 100.100.100.100 1     FULL/  -        00:00:38    100.10.0.2      GigabitEthernet0/0/0/0
        # 95.95.95.95     1     FULL/  -        00:00:38    100.20.0.2      GigabitEthernet0/0/0/1
        # 192.168.199.137 1    FULL/DR       0:00:31    172.31.80.37      GigabitEthernet 0/3/0/2
        p2 = re.compile(r'^(?P<neighbor_id>\S+)\s+(?P<priority>\d+) +(?P<state>[A-Z]+/\s*[A-Z-]*)'
                        r' +(?P<dead_time>(\d+:){2}\d+) +(?P<address>[\d\.\/]+) +(?P<interface>\w+\s*\S+)$')

        for line in output.splitlines():
            line = line.strip()

            # OSPFv3 2 address-family ipv6 vrf 2 (router-id 173.19.2.2)
            m = p1.match(line)
            if m:
                group = m.groupdict()
                vrf_id = int(group['vrf_id'])
                ret_dict['process_id'] = int(group['process_id'])
                ret_dict['address_family'] = group['address_family']
                ret_dict['router_id'] = group['router_id']
                vrf_dict = ret_dict.setdefault('vrfs', {}).setdefault(vrf_id, {})

            # Neighbor ID     Pri   State           Dead Time   Address         Interface
            # 100.100.100.100 1     FULL/  -        00:00:38    100.10.0.2      GigabitEthernet0/0/0/0
            # 95.95.95.95     1     FULL/  -        00:00:38    100.20.0.2      GigabitEthernet0/0/0/1
            # 192.168.199.137 1    FULL/DR       0:00:31    172.31.80.37      GigabitEthernet 0/3/0/2
            m = p2.match(line)
            if m:
                group = m.groupdict()
                neighbor_id = group['neighbor_id']
                neighbor_dict = vrf_dict.setdefault('neighbor_id', {}).setdefault(neighbor_id, {})
                neighbor_dict['priority'] = int(group['priority'])
                neighbor_dict['state'] = group['state']
                neighbor_dict['dead_time'] = group['dead_time']
                neighbor_dict['address'] = int(group['address'])
                neighbor_dict['interface'] = group['interface']

                continue

        return ret_dict
