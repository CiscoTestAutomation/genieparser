"""show_rip.py

IOSXR parser for the following show commands:
    * show rip
    * show rip vrf {vrf}
    * show rip database
    * show rip vrf {vrf} database
    * show rip interface
    * show rip vrf {vrf} interface
    * show rip statistics
    * show rip vrf {vrf} statistics
"""

# Python
import re

# MetaParser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

# ======================================
# Schema for:
#    show rip database
#    show rip vrf {vrf} database
# ======================================
class ShowRipDatabaseSchema(MetaParser):
    """Schema for:
        show rip database
        show rip vrf {vrf} database"""

    schema = {
        'vrf': {
            Any(): {
                'address_family': {
                    Any(): {
                        'instance': {
                            Any(): {
                                'routes': {
                                    Any(): {
                                        'index': {
                                            Any(): {
                                                Optional('route_type'): str,
                                                Optional('metric'): int,
                                                Optional('interface'): str,
                                                Optional('next_hop'): str,
                                                Optional('redistributed'): bool,
                                                Optional('summary_type'): str,
                                                Optional('up_time'): str,
                                                Optional('distance'): int
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }


# ======================================
# Parser for:
#    show rip database
#    show rip vrf {vrf} database
# ======================================
class ShowRipDatabase(ShowRipDatabaseSchema):
    """Parser for:
        show rip database
        show rip vrf {vrf} database"""

    cli_commands = ['show rip database', 'show rip vrf {vrf} database']

    def cli(self, vrf='', output=None):
        if output is None:
            if not vrf:
                vrf = 'default'
                out = self.device.execute(self.cli_commands[0])
            else:
                out = self.device.execute(self.cli_commands[1].format(vrf=vrf))
        else:
            out = output
        
        ret_dict = {}

        # 172.16.0.0/16    auto-summary
        # 192.168.1.1/32
        # 2001:DB8:2:3::/64
        p1 = re.compile(r'^(?P<route>[\w\.\/:]+)(\s+(?P<summary_type>[\w-]+))?$')

        # [0]    directly connected, GigabitEthernet0/0/0/1.100
        p2 = re.compile(r'^\[(?P<metric>\d+)\]\s+directly +connected, +(?P<interface>[\w\d/\.]+)$')

        # [3] distance: 1    redistributed
        p3 = re.compile(r'^\[(?P<metric>\d+)\]\s+distance: +(?P<distance>\d+)\s+redistributed$')

        # [11] via 10.1.2.2, next hop 10.1.2.2, Uptime: 15s, GigabitEthernet0/0/0/0.100
        p4 = re.compile(r'^\[(?P<metric>\d+)\] +via +[\d\.]+, +next +hop +(?P<next_hop>[\d\.]+)'
                        r', +Uptime: +(?P<up_time>\w+), +(?P<interface>[\w\d/\.]+)$')

        for line in out.splitlines():
            line = line.strip()

            # 172.16.0.0/16    auto-summary
            # 192.168.1.1/32
            # 2001:DB8:2:3::/64
            m = p1.match(line)
            if m:
                index_counter = 0

                groups = m.groupdict()
                route = groups['route']
                summary_type = groups['summary_type']
                address_family = 'ipv6' if ':' in route else 'ipv4'
                
                if not ret_dict:
                    routes_dict = ret_dict.setdefault('vrf', {}).setdefault(vrf, {}).setdefault('address_family', {}). \
                                        setdefault(address_family, {}).setdefault('instance', {}).setdefault('rip', {}). \
                                        setdefault('routes', {})

                route_dict = routes_dict.setdefault(route, {}).setdefault('index', {})

                if summary_type:
                    index_counter += 1
                    index_dict = route_dict.setdefault(index_counter, {})
                    index_dict.update({'summary_type': summary_type})

            # [0]    directly connected, GigabitEthernet0/0/0/1.100
            m = p2.match(line)
            if m:
                index_counter += 1

                groups = m.groupdict()
                metric = groups['metric']
                interface = groups['interface']

                index_dict = route_dict.setdefault(index_counter, {})
                index_dict.update({'metric': int(metric)})
                index_dict.update({'route_type': 'connected'})
                index_dict.update({'interface': interface})

            # [3] distance: 1    redistributed
            m = p3.match(line)
            if m:
                index_counter += 1

                groups = m.groupdict()
                metric = groups['metric']
                distance = groups['distance']

                index_dict = route_dict.setdefault(index_counter, {})
                index_dict.update({'metric': int(metric)})
                index_dict.update({'redistributed': True})
                index_dict.update({'distance': int(distance)})

            # [11] via 10.1.2.2, next hop 10.1.2.2, Uptime: 15s, GigabitEthernet0/0/0/0.100
            m = p4.match(line)
            if m:
                index_counter += 1

                groups = m.groupdict()
                metric = groups['metric']
                next_hop = groups['next_hop']
                up_time = groups['up_time']
                interface = groups['interface']

                index_dict = route_dict.setdefault(index_counter, {})
                index_dict.update({'metric': int(metric)})
                index_dict.update({'next_hop': next_hop})
                index_dict.update({'up_time': up_time})
                index_dict.update({'interface': interface})

        return ret_dict
