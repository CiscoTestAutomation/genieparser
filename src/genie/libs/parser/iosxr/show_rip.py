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
                                                Optional('expire_time'): str,
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

    def cli(self, vrf=None, output=None):
        if output is None:
            if not vrf:
                out = self.device.execute(self.cli_commands[0])
            else:
                out = self.device.execute(self.cli_commands[1].format(vrf=vrf))
        else:
            out = output

        # ==============
        # Compiled Regex
        # ==============
        # 172.16.0.0/16    auto-summary
        # 192.168.1.1/32
        p1 = re.compile(r'^(?P<route>\d+\.\d+\.\d+\.\d+/\d+)(\s+(?P<summary_type>[\w-]+))?')
        # [0]    directly connected, GigabitEthernet0/0/0/1.100
        p2 = re.compile(r'^\[(?P<metric>\d+)\]\s+directly +connected, +(?P<interface>[\w\d/\.]+)$')
        # [3] distance: 1    redistributed
        p3 = re.compile(r'^\[(?P<metric>\d+)\]\s+distance: +\d+\s+redistributed$')
        # [11] via 10.1.2.2, next hop 10.1.2.2, Uptime: 15s, GigabitEthernet0/0/0/0.100
        p4 = re.compile(r'^\[(?P<metric>\d+)\] +via +[\d\.]+, +next +hop +(?P<next_hop>[\d\.]+)'
                        r', +Uptime: +(?P<expire_time>\d+s), +(?P<interface>[\w\d/\.]+)$')

        ret_dict = {}

        if out:
            routes_dict = ret_dict.setdefault('vrf', {}).setdefault(vrf, {}).setdefault('address_family', {}). \
                                setdefault(None, {}).setdefault('instance', {}).setdefault('rip', {}). \
                                setdefault('routes', {})

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                index_counter = 0

                groups = m.groupdict()
                route = groups['route']
                summary_type = groups['summary_type']

                route_dict = routes_dict.setdefault(route, {}).setdefault('index', {})

                if summary_type:
                    index_counter += 1
                    index_dict = route_dict.setdefault(index_counter, {})
                    index_dict.update({'summary_type': summary_type})

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

            m = p3.match(line)
            if m:
                index_counter += 1

                groups = m.groupdict()
                metric = groups['metric']

                index_dict = route_dict.setdefault(index_counter, {})
                index_dict.update({'metric': int(metric)})
                index_dict.update({'redistributed': True})

            m = p4.match(line)
            if m:
                index_counter += 1

                groups = m.groupdict()
                metric = groups['metric']
                next_hop = groups['next_hop']
                expire_time = groups['expire_time']
                interface = groups['interface']

                index_dict = route_dict.setdefault(index_counter, {})
                index_dict.update({'metric': int(metric)})
                index_dict.update({'next_hop': next_hop})
                index_dict.update({'expire_time': expire_time})
                index_dict.update({'interface': interface})

        return ret_dict
