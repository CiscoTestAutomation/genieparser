"""
Module:
    genie.libs.parser.ironware.show_routing

Author:
    James Di Trapani <james@ditrapani.com.au> - https://github.com/jamesditrapani

Description:
    Routing based parsers for IronWare devices
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
                'gateway': str,
                'cost': str,
                'type': str,
                'uptime': str,
                'vrf': str
            }
        }
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
    Total number of IP routes: 449
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
    """

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        ip_dict = {}

        result_dict = {}

        p0 = re.compile(
            r'((?P<number>^\d+)\s+(?P<network>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\/(?P<cidr>\d{1,2})\s+ '
            r'(?P<gateway>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\s+(?P<port>eth\s\d{1,2}\/\d{1,2})\s+ '
            r'(?P<cost>\w+\/\w+)\s+(?P<type>\w)\s+(?P<uptime>\w+)\s+(?P<vrf>[\w+|-]))')

        for line in out.splitlines():
            line = line.strip()

            m = p0.match(line)
            if m:
                number = m.groupdict()['number']
                network = m.groupdict()['network']
                cidr = m.groupdict()['cidr']
                gateway = m.groupdict()['gateway']
                cost = m.groupdict()['cost']
                route_type = m.groupdict()['type']
                uptime = m.groupdict()['uptime']
                vrf = m.groupdict()['vrf']

                if 'routes' not in ip_dict:
                    result_dict = ip_dict.setdefault('routes', {})

                result_dict[network + '/' + cidr] = {
                  'network': network,
                  'cidr': cidr, 
                  'gateway': gateway,
                  'cost': cost,
                  'type': route_type,
                  'uptime': uptime,
                  'vrf': vrf if vrf != '-' else None
                }
                continue
        return ip_dict