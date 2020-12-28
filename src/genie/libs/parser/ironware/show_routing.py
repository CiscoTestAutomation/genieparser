"""
Module:
    genie.libs.parser.ironware.show_routing

Author:
    James Di Trapani <james@ditrapani.com.au> - https://github.com/jamesditrapani

Description:
    Routing based parsers for IronWare devices

Parsers:
    * show ip route
"""

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Optional
import re

# ======================================================
# Schema for 'show ip route'
# ======================================================
class ShowIPRouteSchema(MetaParser):
    """Schema for show ip route"""
    schema = {
        'routes': {
            Any(): {
                'network': str,
                'cidr': int,
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
    Type Codes - B:BGP D:Connected I:ISIS O:OSPF R:RIP S:Static; Cost - Dist/Metric
    BGP  Codes - i:iBGP e:eBGP
    ISIS Codes - L1:Level-1 L2:Level-2
    OSPF Codes - i:Inter Area 1:External Type 1 2:External Type 2 s:Sham Link
    STATIC Codes - d:DHCPv6
            Destination        Gateway         Port           Cost          Type Uptime src-vrf
    1       10.200.0.12/30     10.254.248.10   eth 2/2        110/28        O    40d0h  -
    2       10.200.0.16/30     10.254.248.10   eth 2/2        110/194       O    6d12h  -
    3       10.200.0.28/30     10.254.248.10   eth 2/2        110/138       O    40d0h  -
    4       10.200.0.32/30     10.254.248.10   eth 2/2        110/36        O    40d0h  -
    5       10.200.0.56/30     10.254.248.10   eth 2/2        110/36        O    12d4h  -
    6       10.200.0.60/30     10.254.248.10   eth 2/2        110/38        O    40d0h  -
    7       10.200.0.65/32     10.254.248.10   eth 2/2        110/63        O    40d0h  -
    8       10.200.0.73/32     10.254.248.10   eth 2/2        110/73        O    40d0h  -
    9       10.200.0.80/30     10.254.248.10   eth 2/2        110/76        O    1d1h   -
    10      10.200.0.85/32     10.254.248.10   eth 2/2        110/27        O    40d0h  -
    11     200.200.200.200/32   DIRECT          loopback 1     0/0           D    248d   
    -
    12      1.1.1.1/32         10.254.251.2    eth 5/1       110/52        O    15h47m -
            1.1.1.1/32         10.254.251.108  eth 7/1       110/52        O    15h47m -
    13      2.2.2.2/32         10.254.251.2    eth 5/1       110/42        O    15h47m -
            2.2.2.2/32         10.254.251.108  eth 7/1       110/42        O    15h47m -
    """

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        ip_dict = {}

        result_dict = {}

        p0 = re.compile(
            r'(^Total number of IP routes:\s+(?P<total>\d+))'
        )

        p1 = re.compile(
            r'((?P<number>^\d+)\s+ '
            r'(?P<network>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\/(?P<cidr>\d{1,2})\s+ '
            r'(?P<gateway>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}|DIRECT)\s+ '
            r'(?P<port>eth\s\d{1,2}\/\d{1,2}|loopback\s\d{1,3})\s+ '
            r'(?P<cost>\w+\/\w+)\s+(?P<type>\w+)\s+(?P<uptime>\w+)\s+(?P<vrf>[\w+|-]))'
        )

        # Used when src-vrf output wraps to the next line, Brocade has no terminal-width
        p2 = re.compile(
            r'((?P<number>^\d+)\s+ '
            r'(?P<network>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\/(?P<cidr>\d{1,2})\s+ '
            r'(?P<gateway>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}|DIRECT)\s+ '
            r'(?P<port>eth\s\d{1,2}\/\d{1,2}|loopback\s\d{1,3})\s+ '
            r'(?P<cost>\w+\/\w+)\s+(?P<type>\w+)\s+(?P<uptime>\w+)$)'
        )

        # Used when equal cost paths exist
        p3 = re.compile(
            r'(^(?P<network>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\/(?P<cidr>\d{1,2})\s+ '
            r'(?P<gateway>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}|DIRECT)\s+ '
            r'(?P<port>eth\s\d{1,2}\/\d{1,2}|loopback\s\d{1,3})\s+ '
            r'(?P<cost>\w+\/\w+)\s+(?P<type>\w+)\s+(?P<uptime>\w+)\s+(?P<vrf>[\w+|-]))'
        )

        for line in out.splitlines():
            line = line.strip()

            m = p0.match(line)
            if m:
                ip_dict['total_routes'] = int(m.groupdict()['total'])

            # Will only even match on one as EOL provided in P2
            m = p1.match(line)
            n = p2.match(line)
            m = m if m else n

            if m:
                network = m.groupdict()['network']
                cidr = int(m.groupdict()['cidr'])
                srcvrf = m.groupdict().get('vrf')

                if 'routes' not in ip_dict:
                    result_dict = ip_dict.setdefault('routes', {})

                result_dict['{0}/{1}'.format(network, cidr)] = {
                  'network': network,
                  'cidr': cidr,
                  'via': {
                      m.groupdict()['gateway']: {
                          'interface': m.groupdict()['port'],
                          'cost': m.groupdict()['cost'],
                          'type': m.groupdict()['type'],
                          'uptime': m.groupdict()['uptime'],
                          'src-vrf': srcvrf if srcvrf != None else 'Unknown'
                      }
                  }
                }
                continue

            m = p3.match(line)
            if m:
                network = m.groupdict()['network']
                cidr = int(m.groupdict()['cidr'])
                route = '{0}/{1}'.format(network, cidr)

                result_dict[route]['via'][m.groupdict()['gateway']] = {
                    'interface': m.groupdict()['port'],
                    'cost': m.groupdict()['cost'],
                    'type': m.groupdict()['type'],
                    'uptime': m.groupdict()['uptime'],
                    'src-vrf': srcvrf if srcvrf != None else 'Unknown'
                }
                continue
                
        return ip_dict