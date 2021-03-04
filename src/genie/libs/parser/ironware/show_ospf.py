"""
Module:
    genie.libs.parser.ironware.show_ospf

Author:
    James Di Trapani <james@ditrapani.com.au> - https://github.com/jamesditrapani

Description:
    OSPF parsers for IronWare devices

Parsers:
    * show ip ospf neighbor
    * show ip ospf interface brief
"""

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Optional
import re

__author__ = 'James Di Trapani <james@ditrapani.com.au>'


# ======================================================
# Schema for 'show ip ospf neighbors'
# ======================================================
class ShowIPOSPFNeighborSchema(MetaParser):
    """Schema for show ip ospf neighbor"""
    schema = {
        Optional('total'): int,
        Optional('total_full'): int,
        'vrf': {
            Any(): {
                'neighbors': {
                    Any(): {
                        'interface': str,
                        'local_ip': str,
                        'priority': int,
                        'state': str,
                        'neighbor_rid': str,
                        'state_changes': int,
                        'options': int,
                        'lsa_retransmits': int
                    }
                }
            }
        }
    }


# ====================================================
#  parser for 'show ip ospf neighbor'
# ====================================================
class ShowIPOSPFNeighbor(ShowIPOSPFNeighborSchema):
    """
    Parser for show ip ospf neighbor on Ironware devices
    """
    cli_command = 'show ip ospf neighbor'

    """
Number of Neighbors is 2, in FULL state 2

Port   Address         Pri State      Neigh Address   Neigh ID Ev Opt Cnt
5/1    10.254.251.3    1   FULL/OTHER 10.254.251.2    10.9.3.4  61 82  0
7/1    10.254.251.109  1   FULL/OTHER 10.254.251.108  10.49.2.1  83 82  0
v10    10.1.10.1       1   FULL/DR    10.1.10.2       10.65.12.1 5 2 0
    """

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        result_dict = {}

        # Number of Neighbors is 2, in FULL state 2
        p1 = re.compile(r'(^Number\s+of\s+Neighbors\s+is\s+(?P<num>\d+),\s'
                        r'+in\s+FULL\s+state\s+(?P<full>\d+))')

        # 5/1    10.254.251.3 1 FULL/OTHER 10.254.251.2 10.9.3.4  61 82  0
        p2 = re.compile(r'(^(?P<port>\d+\/\d+|v\d+|tn\d+)\s+'
                        r'(?P<local>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\s+'
                        r'(?P<pri>\d+)\s+(?P<state>\S+)\s+'
                        r'(?P<neighbor>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\s+'
                        r'(?P<neighrid>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\s+'
                        r'(?P<changes>\d+)\s+'
                        r'(?P<opt>\d+)\s+(?P<lsaretrans>\d+)$)')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                result_dict['total'] = int(m.groupdict()['num'])
                result_dict['total_full'] = int(m.groupdict()['full'])
                continue

            m = p2.match(line)
            if m:
                # Set VRF to default given this command is not parsing
                # vrf specific output
                if result_dict.get('vrf') is None:
                    result_dict.update({'vrf': {'default': {}}})

                neighbors = result_dict['vrf']['default'].setdefault(
                                                            'neighbors', {})

                group = m.groupdict()
                neighbor = group['neighbor']
                neigh_dict = neighbors.update({neighbor: {
                    'interface': group['port'],
                    'local_ip': group['local'],
                    'priority': int(group['pri']),
                    'state': group['state'],
                    'neighbor_rid': group['neighrid'],
                    'state_changes': int(group['changes']),
                    'options': int(group['opt']),
                    'lsa_retransmits': int(group['lsaretrans'])
                }})
                continue

        return result_dict


# ======================================================
# Schema for 'show ip ospf interface brief'
# ======================================================
class ShowIPOSPFInterfaceBriefSchema(MetaParser):
    """Schema for show interfaces brief wide"""
    schema = {
        Optional('total'): int,
        'interfaces': {
            Any(): {
                'area': int,
                'network': str,
                'cost': int,
                'state': str,
                'full_neighbors': int,
                'configured_neighbors': int
            }
        }
    }


# ====================================================
#  parser for 'show ip ospf interface brief'
# ====================================================
class ShowIPOSPFInterfaceBrief(ShowIPOSPFInterfaceBriefSchema):
    """
    Parser for show ip ospf interface brief on Ironware devices
    """
    cli_command = 'show ip ospf interface brief'

    """
    Number of Interfaces is 3

    Interface   Area      IP Addr/Mask       Cost  State    Nbrs(F/C)
    eth 5/1     0         10.254.251.21/31   20    ptpt     1/1
    eth 7/1     0         10.254.251.23/31   20    ptpt     1/1
    loopback 1  0         10.69.33.44/32  1     DR       0/0
    """

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        interface_def = {
            'mgmt': 'management',
            'eth': 'ethernet',
            'lb': 'loopback',
            'loopback': 'loopback',
            'tn': 'tunnel',
            'tunnel': 'tunnel',
            've': 've'
        }

        result_dict = {}

        # Number of Interfaces is 3
        p1 = re.compile(r'(^Number\s+of\s+Interfaces\s+is\s+(?P<num>\d+)$)')

        # eth 5/1     0         10.254.251.21/31   20    ptpt     1/1
        p2 = re.compile(r'(^(?P<int_name>eth|mgmt|loopback|ve|tn|tunnel)\s+'
                        r'(?P<int_num>\d+\/\d+|\d+)\s+(?P<area>\d+)\s+'
                        r'(?P<net>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}\/\d{1,2})\s+'
                        r'(?P<cost>\d+)\s+(?P<state>\S+)\s+'
                        r'(?P<fullneigh>\d+)\/(?P<configdneigh>\d+))')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                total = int(m.groupdict()['num'])
                result_dict['total'] = total
                continue

            m = p2.match(line)
            if m:
                interfaces = result_dict.setdefault('interfaces', {})

                group = m.groupdict()
                interface = '{0}{1}'.format(interface_def.get(
                                group['int_name']), group['int_num'])

                interface_dict = interfaces.update({interface: {
                    'area': int(group['area']),
                    'network': group['net'],
                    'cost': int(group['cost']),
                    'state': group['state'],
                    'full_neighbors': int(group['fullneigh']),
                    'configured_neighbors': int(group['configdneigh'])
                }})
                continue

        return result_dict
