"""
Module:
    genie.libs.parser.ironware.show_routing

Author:
    James Di Trapani <james@ditrapani.com.au> - https://github.com/jamesditrapani

Description:
    Routing based parsers for IronWare devices

Parsers:
    * show ip route
    * show ip route summary
"""

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Optional
import re

__author__ = 'James Di Trapani <james@ditrapani.com.au>'


# ======================================================
# Schema for 'show ip route'
# ======================================================
class ShowIPRouteSchema(MetaParser):
    """Schema for show ip route"""
    schema = {
        'vrf': {
            Any(): {
                'routes': {
                    Any(): {
                        'network': str,
                        'netmask': int,
                        'via': {
                            Any(): {
                                'cost': str,
                                'interface': str,
                                'type': str,
                                'uptime': str,
                                'src-vrf': str
                            }
                        }
                    }
                }
            }
        },
        'total_routes': int
    }


# ====================================================
#  parser for 'show ip route'
# ====================================================
class ShowIPRoute(ShowIPRouteSchema):
    """
    Parser for Show IP Route on Devices running IronWare
    """
    cli_command = 'show ip route'

    """
Total number of IP routes: 13
Type Codes - B:BGP D:Connected I:ISIS O:OSPF R:RIP S:Static; Cost -Dist/Metric
BGP  Codes - i:iBGP e:eBGP
ISIS Codes - L1:Level-1 L2:Level-2
OSPF Codes - i:Inter Area 1:External Type 1 2:External Type 2 s:Sham Link
STATIC Codes - d:DHCPv6
    Destination        Gateway         Port      Cost      Type Uptime src-vrf
1   10.200.0.12/30     10.254.248.10   eth 2/2   110/28     O   40d0h  -
2   10.200.0.16/30     10.254.248.10   eth 2/2   110/194    O   6d12h  -
3   10.200.0.28/30     10.254.248.10   eth 2/2   110/138    O   40d0h  -
4   10.200.0.32/30     10.254.248.10   eth 2/2   110/36     O   40d0h  -
5   10.200.0.56/30     10.254.248.10   eth 2/2   110/36     O   12d4h  -
6   10.200.0.60/30     10.254.248.10   eth 2/2   110/38     O   40d0h  -
7   10.200.0.65/32     10.254.248.10   eth 2/2   110/63     O   40d0h  -
8   10.200.0.73/32     10.254.248.10   eth 2/2   110/73     O   40d0h  -
9   10.200.0.80/30     10.254.248.10   eth 2/2   110/76     O   1d1h   -
10  10.200.0.85/32     10.254.248.10   eth 2/2   110/27     O   40d0h  -
11  192.168.195.200/32   DIRECT        loopback 1 0/0       D   248d
-
12  10.4.1.1/32         10.254.251.2    eth 5/1    110/52     O   15h47m -
    10.4.1.1/32         10.254.251.108  eth 7/1    110/52     O   15h47m -
13  10.16.2.2/32         10.254.251.2    eth 5/1    110/42     O   15h47m -
    10.16.2.2/32         10.254.251.108  eth 7/1    110/42     O   15h47m -
    """

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        ip_dict = {}

        result_dict = {}

        # Total number of IP routes: 13
        p1 = re.compile(
            r'(^Total number of IP routes:\s+(?P<total>\d+))'
        )

        # 10  10.200.0.85/32 10.254.248.10 eth 2/2 110/27 O  40d0h  -
        p2 = re.compile(
            r'((?P<number>^\d+)\s+'
            r'(?P<network>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\/'
            r'(?P<netmask>\d{1,2})\s+'
            r'(?P<gateway>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}|DIRECT)\s+'
            r'(?P<port>eth\s\d{1,2}\/\d{1,2}|loopback\s\d{1,3})\s+'
            r'(?P<cost>\w+\/\w+)\s+(?P<type>\w+)\s+(?P<uptime>\w+)\s+'
            r'(?P<vrf>[\w+|-]))'
        )

        # Used when src-vrf output wraps to the next line,
        # Brocade has no terminal-width
        # 11  192.168.195.200/32   DIRECT   loopback 1 0/0   D   248d
        p3 = re.compile(
            r'((?P<number>^\d+)\s+'
            r'(?P<network>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\/'
            r'(?P<netmask>\d{1,2})\s+'
            r'(?P<gateway>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}|DIRECT)\s+'
            r'(?P<port>eth\s\d{1,2}\/\d{1,2}|loopback\s\d{1,3})\s+'
            r'(?P<cost>\w+\/\w+)\s+(?P<type>\w+)\s+(?P<uptime>\w+)$)'
        )

        # Used when equal cost paths exist
        #     10.4.1.1/32   10.254.251.108  eth 7/1  110/52  O  15h47m -
        p4 = re.compile(
            r'(^(?P<network>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\/'
            r'(?P<netmask>\d{1,2})\s+'
            r'(?P<gateway>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}|DIRECT)\s+'
            r'(?P<port>eth\s\d{1,2}\/\d{1,2}|loopback\s\d{1,3})\s+'
            r'(?P<cost>\w+\/\w+)\s+(?P<type>\w+)\s+(?P<uptime>\w+)\s+'
            r'(?P<vrf>[\w+|-]))'
        )

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                ip_dict['total_routes'] = int(m.groupdict()['total'])

            # Will only even match on one as EOL provided in P2
            m = p2.match(line)
            n = p3.match(line)
            m = m if m else n

            if m:
                network = m.groupdict()['network']
                cidr = int(m.groupdict()['netmask'])
                srcvrf = m.groupdict().get('vrf')
                if srcvrf is None:
                    srcvrf = 'Unknown'

                # Set VRF to default given this command is not parsing
                # vrf specific output
                if ip_dict.get('vrf') is None:
                    ip_dict.update({'vrf': {'default': {}}})

                result_dict = ip_dict['vrf']['default'].setdefault(
                                                            'routes', {})

                result_dict['{0}/{1}'.format(network, cidr)] = {
                  'network': network,
                  'netmask': cidr,
                  'via': {
                      m.groupdict()['gateway']: {
                          'interface': m.groupdict()['port'],
                          'cost': m.groupdict()['cost'],
                          'type': m.groupdict()['type'],
                          'uptime': m.groupdict()['uptime'],
                          'src-vrf': 'local' if srcvrf == '-' else srcvrf
                      }
                  }
                }
                continue

            m = p4.match(line)
            if m:
                network = m.groupdict()['network']
                cidr = int(m.groupdict()['netmask'])
                route = '{0}/{1}'.format(network, cidr)

                result_dict[route]['via'][m.groupdict()['gateway']] = {
                    'interface': m.groupdict()['port'],
                    'cost': m.groupdict()['cost'],
                    'type': m.groupdict()['type'],
                    'uptime': m.groupdict()['uptime'],
                    'src-vrf': 'local' if srcvrf == '-' else srcvrf
                }
                continue

        return ip_dict


# ======================================================
# Schema for 'show ip route summary'
# ======================================================
class ShowIPRouteSummarySchema(MetaParser):
    """Schema for show ip route summary"""
    schema = {
        'total': int,
        'protocols': {
            'connected': int,
            'static': int,
            'rip': int,
            'ospf': int,
            'bgp': int,
            'isis': int
        },
        'netmask': {
            Optional(32): int,
            Optional(31): int,
            Optional(30): int,
            Optional(29): int,
            Optional(28): int,
            Optional(27): int,
            Optional(26): int,
            Optional(25): int,
            Optional(24): int,
            Optional(23): int,
            Optional(22): int,
            Optional(21): int,
            Optional(20): int,
            Optional(19): int,
            Optional(18): int,
            Optional(17): int,
            Optional(16): int,
            Optional(15): int,
            Optional(14): int,
            Optional(13): int,
            Optional(12): int,
            Optional(11): int,
            Optional(10): int,
            Optional(9): int,
            Optional(8): int,
            Optional(7): int,
            Optional(6): int,
            Optional(5): int,
            Optional(4): int,
            Optional(3): int,
            Optional(2): int,
            Optional(1): int
        },
        'next_hop_table': int
    }


# ====================================================
#  parser for 'show ip route summary'
# ====================================================
class ShowIPRouteSummary(ShowIPRouteSummarySchema):
    """
    Parser for Show IP Route Summary on Devices running IronWare
    """
    cli_command = 'show ip route summary'

    """
    IP Routing Table - 449 entries
    3 connected, 0 static, 0 RIP, 446 OSPF, 0 BGP, 0 ISIS
    Number of prefixes:
    /24: 1 /26: 2 /27: 3 /28: 5 /29: 1 /30: 34 /31: 242 /32: 161
    Nexthop Table Entry - 5 entries
    """

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        route_dict = {}

        result_dict = {}

        # IP Routing Table - 449 entries
        p1 = re.compile(r'(^IP\s+Routing\s+Table\s+-\s+'
                        r'(?P<entries>\S+)\s+entries)')

        # 3 connected, 0 static, 0 RIP, 446 OSPF, 0 BGP, 0 ISIS
        p2 = re.compile(r'(^(?P<connected>\S+)\s+connected,\s+'
                        r'(?P<static>\S+)\s+static,\s+(?P<rip>\S+)\s+'
                        r'RIP,\s+(?P<ospf>\S+)\s+OSPF,\s+(?P<bgp>\S+)\s+'
                        r'BGP,\s+(?P<isis>\S+)\s+ISIS)')

        # /24: 1 /26: 2 /27: 3 /28: 5 /29: 1 /30: 34 /31: 242 /32: 161
        p3 = re.compile(r'(\/\d{1,2}:\s+\d+)')

        # /27: 3
        p4 = re.compile(r'(^\/(?P<key>\d{1,2}):\s+(?P<num>\d+))')

        # Nexthop Table Entry - 5 entries
        p5 = re.compile(r'(^Nexthop\s+Table\s+Entry\s+\-\s+'
                        r'(?P<entries>\d+)\s+entries$)')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                route_dict['total'] = int(m.groupdict()['entries'])
                continue

            m = p2.match(line)
            if m:
                protocols = route_dict.setdefault('protocols', {})
                protocols['connected'] = int(m.groupdict()['connected'])
                protocols['static'] = int(m.groupdict()['static'])
                protocols['rip'] = int(m.groupdict()['rip'])
                protocols['ospf'] = int(m.groupdict()['ospf'])
                protocols['bgp'] = int(m.groupdict()['bgp'])
                protocols['isis'] = int(m.groupdict()['isis'])
                continue

            m = p3.match(line)
            if m:
                cidrs = route_dict.setdefault('netmask', {})

                # Find all occurrences of a CIDR notation so we
                # don't have to do each key individually
                all_matches = p3.findall(line)

                for match in all_matches:
                    x = p4.match(match)
                    if x:
                        key = int(x.groupdict()['key'])
                        cidrs[key] = int(x.groupdict()['num'])
                continue
            
            m = p5.match(line)
            if m:
                entries = m.groupdict()['entries']
                route_dict['next_hop_table'] = int(entries)
                continue

        return route_dict
