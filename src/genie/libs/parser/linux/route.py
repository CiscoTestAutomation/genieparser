"""route.py

Linux parsers for the following commands:
    * route
"""

# python
import re

# metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

# =======================================================
# Schema for 'route'
# =======================================================
class RouteSchema(MetaParser):
    """Schema for route"""

    # Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
    # 0.0.0.0         192.168.1.1     0.0.0.0         UG        0 0          0 wlo1

    schema = {
        Any(): {
            'destination': str,
            'gateway': str,
            'mask': str,
            'flags': str,
            Optional('metric'): int,
            Optional('ref'): int,
            Optional('use'): int,
            Optional('mss'): int,
            Optional('window'): int,
            Optional('irtt'): int,
            'interface': str
        }
    }

    schema = {
        'routes': {
            Any(): { # 'destination'
                'mask': {
                    Any(): {
                        'nexthop': {
                            Any(): { # index: 1, 2, 3, etc
                                'interface': str,
                                'flags': str,
                                'gateway': str,
                                'metric': int,
                                'ref': int,
                                'use': int
                            }
                        }
                    }
                }
            }
        }
    }

# =======================================================
# Parser for 'route'
# =======================================================
class Route(RouteSchema):
    """Parser for 
        * route
        * route -4 -n 
        * route -4n
        * route -n4
        * route -n -4
        """

    cli_command = ['route', 'route {flag}']

    def cli(self, flag=None, output=None):
        if output is None:    
            cmd = self.cli_command[0]
            if flag in ['-4 -n', '-4n', '-n4']:
                command = self.cli_command[1].replace('{flag}', flag)
            out = self.device.execute(cmd)
        else:
            out = output

        # Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
        # 192.168.1.0     0.0.0.0         255.255.255.0   U     600    0        0 wlo1

        p1 = re.compile(r'(?P<destination>[a-z0-9\.\:]+)'
                        ' +(?P<gateway>[a-z0-9\.\:_]+)'
                        ' +(?P<mask>[a-z0-9\.\:]+)'
                        ' +(?P<flags>[a-zA-Z]+)'
                        ' +(?P<metric>(\d+))'
                        ' +(?P<ref>(\d+))'
                        ' +(?P<use>(\d+))'
                        ' +(?P<interface>\S+)'
                        )
        
        # Initializes the Python dictionary variable
        parsed_dict = {}


        # Defines the "for" loop, to pattern match each line of output

        for line in out.splitlines():
            line = line.strip()


            # 192.168.1.0     0.0.0.0         255.255.255.0   U     600    0        0 wlo1
            m = p1.match(line)
            if m:
                if 'routes' not in parsed_dict:
                    parsed_dict.setdefault('routes', {})
       
                group = m.groupdict()
                destination = group['destination']
                mask = group['mask']

                index_dict = {}
                for str_k in ['interface', 'flags', 'gateway']:
                    index_dict[str_k] = group[str_k]
                
                for int_k in ['metric', 'ref', 'use']:
                    index_dict[int_k] = int(group[int_k])

                if destination in parsed_dict['routes']:
                    if mask in parsed_dict['routes'][destination]['mask']:
                        parsed_dict['routes'][destination]['mask'][mask].\
                                setdefault('nexthop', {index+1: index_dict})
                    else:
                        index = 1
                        parsed_dict['routes'][destination]['mask'].\
                            setdefault(mask, {}).\
                                setdefault('nexthop', {index: index_dict})
                else:
                    index = 1
                    parsed_dict['routes'].setdefault(destination, {}).\
                        setdefault('mask', {}).\
                            setdefault(mask, {}).\
                                setdefault('nexthop', {index: index_dict})

                continue

        return parsed_dict


# =======================================================
# Parser for 'netstat -rn'
# =======================================================
class ShowNetworkStatusRoute(Route, RouteSchema):
    """Parser for 
        * netstat -rn 
        """

    cli_command = ['netstat -rn']

    def cli(self, output=None):
        if output is None:    
            cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        return super().cli(output=out)

