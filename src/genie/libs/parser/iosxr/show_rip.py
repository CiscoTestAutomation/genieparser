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


# ==============================
# Schema for:
#   show rip
#   show rip vrf {vrf}
# ==============================
class ShowRipSchema(MetaParser):
    """Schema for:
        * show rip
        * show rip vrf {vrf}"""

    schema = {
        'vrf': {
            Any(): {
                'address_family': {
                    Any(): {
                        'instance': {
                            Any(): {
                                'active': str,
                                'added_to_socket': str,
                                'out_of_memory_state': str,
                                'version': int,
                                'default_metric': str,
                                'maximum_paths': int,
                                'auto_summarize': str,
                                'broadcast_for_v2': str,
                                'packet_source_validation': str,
                                'nsf': str,
                                'timers': {
                                    'until_next_update': int,
                                    'update_interval': int,
                                    'invalid_interval': int,
                                    'holddown_interval': int,
                                    'flush_interval': int
                                }
                            }
                        }
                    }
                }
            }
        }
    }


# ===========================
# Parser for:
#    show rip
#    show rip vrf {vrf}
# ===========================
class ShowRip(ShowRipSchema):
    """Parser for:
        show rip
        show rip vrf {vrf}"""

    cli_command = ['show rip', 'show rip vrf {vrf}']

    def cli(self, vrf="", output=None):
        if vrf:
            cmd = self.cli_command[1].format(vrf=vrf)
        else:
            cmd = self.cli_command[0]
            vrf = 'default'

        if output is None:
            out = self.device.execute(cmd)
        else:
            out = output

        instance = 'rip'
        ret_dict = {}

        # RIP config:
        p1 = re.compile(r'^RIP +config:$')

        # Active:                    Yes
        p2 = re.compile(r'^Active\??:\s+(?P<active>\w+)$')

        # Added to socket:           Yes
        p3 = re.compile(r'^Added +to +socket\??:\s+(?P<added_to_socket>\w+)$')

        # Out-of-memory state:        Normal
        p4 = re.compile(r'^Out-of-memory +state:\s+(?P<memory_state>\w+)$')

        # Version:                    2.3
        p5 = re.compile(r'^Version:\s+(?P<version>[\d.]+)$')

        # Default metric:             3
        p6 = re.compile(r'^Default +metric:\s+(?P<default_metric>[\w\s]+)$')

        # Maximum paths:              4
        p7 = re.compile(r'^Maximum +paths:\s+(?P<max_paths>\d+)$')

        # Auto summarize:            No
        p8 = re.compile(r'^Auto +summarize\??:\s+(?P<auto_summarize>\w+)$')

        # Broadcast for V2:          No
        p9 = re.compile(r'^Broadcast +for +V2\??:\s+(?P<broadcast>\w+)$')

        # Packet source validation:  Yes
        p10 = re.compile(r'^Packet +source +validation\??:\s+(?P<'
                         r'packet_validation>\w+)$')

        # NSF:                        Disabled
        p11 = re.compile(r'^NSF:\s+(?P<nsf>\w+)$')

        # Timers: Update:             10 seconds (7 seconds until next update)
        p12 = re.compile(r'^Timers: +Update:\s+(?P<update_timer>\d+) +seconds'
                         r' +\((?P<next_update>\d+)[\s\w]+\)$')

        # Invalid:            31 seconds
        p13 = re.compile(r'^Invalid:\s+(?P<invalid_timer>\d+)[\s\w]+$')

        # Holddown:           32 seconds
        p14 = re.compile(r'^Holddown:\s+(?P<holddown_timer>\d+)[\s\w]+$')

        # Flush:              33 seconds
        p15 = re.compile(r'^Flush:\s+(?P<flush_timer>\d+)[\s\w]+$')

        for line in out.splitlines():
            line = line.strip()

            # RIP config:
            m = p1.match(line)
            if m:
                instance_dict = ret_dict.setdefault('vrf', {}). \
                    setdefault(vrf, {}).setdefault('address_family', {}). \
                    setdefault('ipv4', {}).setdefault('instance', {}). \
                    setdefault(instance, {})
                continue

            # Active:                    Yes
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                instance_dict.update({'active': groups['active']})
                continue

            # Added to socket:           Yes
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                instance_dict.update({'added_to_socket': groups['added_to_socket']})
                continue

            # Out-of-memory state:        Normal
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                instance_dict.update({'out_of_memory_state': groups['memory_state']})
                continue

            # Version:                    2.3
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                instance_dict.update({'version': int(groups['version'])})
                continue

            # Default metric:             3
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                instance_dict.update({'default_metric': groups['default_metric']})
                continue

            # Maximum paths:              4
            m = p7.match(line)
            if m:
                groups = m.groupdict()
                instance_dict.update({'maximum_paths': int(groups['max_paths'])})
                continue

            # Auto summarize:            No
            m = p8.match(line)
            if m:
                groups = m.groupdict()
                instance_dict.update({'auto_summarize': groups['auto_summarize']})
                continue

            # Broadcast for V2:          No
            m = p9.match(line)
            if m:
                groups = m.groupdict()
                instance_dict.update({'broadcast_for_v2': groups['broadcast']})
                continue

            # Packet source validation:  Yes
            m = p10.match(line)
            if m:
                groups = m.groupdict()
                instance_dict.update({'packet_source_validation': groups[
                    'packet_validation']})
                continue

            # NSF:                        Disabled
            m = p11.match(line)
            if m:
                groups = m.groupdict()
                instance_dict.update({'nsf': groups['nsf']})
                continue

            # Timers: Update:             10 seconds (7 seconds until next update)
            m = p12.match(line)
            if m:
                groups = m.groupdict()

                timer_dict = instance_dict.setdefault('timers', {})
                timer_dict.update({'until_next_update': int(groups['next_update'])})
                timer_dict.update({'update_interval': int(groups['update_timer'])})
                continue

            # Invalid:            31 seconds
            m = p13.match(line)
            if m:
                groups = m.groupdict()
                timer_dict.update({'invalid_interval': int(groups['invalid_timer'])})
                continue

            # Holddown:           32 seconds
            m = p14.match(line)
            if m:
                groups = m.groupdict()
                timer_dict.update({'holddown_interval': int(groups['holddown_timer'])})
                continue

            # Flush:              33 seconds
            m = p15.match(line)
            if m:
                groups = m.groupdict()
                timer_dict.update({'flush_interval': int(groups['flush_timer'])})

        return ret_dict


# ======================================
# Schema for:
#    show rip statistics
#    show rip vrf {vrf} statistics
# ======================================
class ShowRipStatisticsSchema(MetaParser):
    """Schema for:
        show rip statistics
        show rip vrf {vrf} statistics"""

    schema = {
        'vrf': {
            Any(): {
                'address_family': {
                    Any(): {
                        'instance': {
                            Any(): {
                                'statistics': {
                                    'total_messages_sent': int,
                                    'message_send_failures': int,
                                    'regular_updates_sent': int,
                                    'queries_responsed_to': int,
                                    'rib_updates': int,
                                    'total_packets_received': int,
                                    'packets_discarded': int,
                                    'routes_discarded': int,
                                    Optional('packets_received_at_standby'): int,
                                    'routes_allocated': int,
                                    'paths_allocated': int,
                                    'route_malloc_failures': int,
                                    'path_malloc_failures': int
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
#    show rip statistics
#    show rip vrf {vrf} statistics
# ======================================
class ShowRipStatistics(ShowRipStatisticsSchema):
    """Parser for:
        show rip statistics
        show rip vrf {vrf} statistics"""

    cli_command = ['show rip statistics', 'show rip vrf {vrf} statistics']

    def cli(self, vrf='', output=None):
        if vrf:
            cmd = self.cli_command[1].format(vrf=vrf)
        else:
            cmd = self.cli_command[0]
            vrf = 'default'

        if output is None:
            out = self.device.execute(cmd)
        else:
            out = output

        ret_dict = {}

        # RIP statistics:
        p1 = re.compile(r'^RIP +statistics:$')

        # Total messages sent:        5294
        p2 = re.compile(r'^Total +messages +sent:\s+(?P<number_of_messages>\d+)$')

        # Message send failures:      0
        p3 = re.compile(r'^Message +send +failures:\s+(?P<number_of_failures>\d+)$')

        # Regular updates sent:       2944
        p4 = re.compile(r'^Regular +updates +sent:\s+(?P<number_of_updates>\d+)$')

        # Queries responsed to:       0
        p5 = re.compile(r'^Queries +responsed +to:\s+(?P<number_of_queries>\d+)$')

        # RIB updates:                4365
        p6 = re.compile(r'^RIB +updates:\s+(?P<number_of_rib_updates>\d+)$')

        # Total packets received:     4896
        p7 = re.compile(r'^Total +packets +received:\s+(?P<packets_received>\d+)$')

        # Discarded packets:          0
        p8 = re.compile(r'^Discarded +packets:\s+(?P<discarded_packets>\d+)$')

        # Discarded routes:           4760
        p9 = re.compile(r'^Discarded +routes:\s+(?P<discarded_routes>\d+)$')

        # Packet received at standby: 0
        p10 = re.compile(r'^Packet +received +at +standby:\s+(?P<packets_received>\d+)$')

        # Number of routes allocated: 9
        p11 = re.compile(r'^Number +of +routes +allocated:\s+(?P<number_of_routes>\d+)$')

        # Number of paths allocated:  6
        p12 = re.compile(r'^Number +of +paths +allocated:\s+(?P<number_of_paths>\d+)$')

        # Route malloc failures:      0
        p13 = re.compile(r'^Route +malloc +failures:\s+(?P<route_malloc_failures>\d+)$')

        # Path malloc failures:       0
        p14 = re.compile(r'^Path +malloc +failures:\s+(?P<path_malloc_failures>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            # RIP statistics:
            m = p1.match(line)
            if m:
                statistics_dict = ret_dict.setdefault('vrf', {}).setdefault(vrf, {}). \
                            setdefault('address_family', {}).setdefault('ipv4', {}). \
                            setdefault('instance', {}).setdefault('rip', {}). \
                            setdefault('statistics', {})
                continue

            # Total messages sent:        5294
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                statistics_dict.update({'total_messages_sent': int(groups['number_of_messages'])})
                continue

            # Message send failures:      0
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                statistics_dict.update({'message_send_failures': int(groups['number_of_failures'])})
                continue

            # Regular updates sent:       2944
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                statistics_dict.update({'regular_updates_sent': int(groups['number_of_updates'])})
                continue

            # Queries responsed to:       0
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                statistics_dict.update({'queries_responsed_to': int(groups['number_of_queries'])})
                continue

            # RIB updates:                4365
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                statistics_dict.update({'rib_updates': int(groups['number_of_rib_updates'])})
                continue

            # Total packets received:     4896
            m = p7.match(line)
            if m:
                groups = m.groupdict()
                statistics_dict.update({'total_packets_received': int(groups['packets_received'])})
                continue

            # Discarded packets:          0
            m = p8.match(line)
            if m:
                groups = m.groupdict()
                statistics_dict.update({'packets_discarded': int(groups['discarded_packets'])})
                continue

            # Discarded routes:           4760
            m = p9.match(line)
            if m:
                groups = m.groupdict()
                statistics_dict.update({'routes_discarded': int(groups['discarded_routes'])})
                continue

            # Packet received at standby: 0
            m = p10.match(line)
            if m:
                groups = m.groupdict()
                statistics_dict.update({'packets_received_at_standby': int(groups['packets_received'])})
                continue

            # Number of routes allocated: 9
            m = p11.match(line)
            if m:
                groups = m.groupdict()
                statistics_dict.update({'routes_allocated': int(groups['number_of_routes'])})
                continue

            # Number of paths allocated:  6
            m = p12.match(line)
            if m:
                groups = m.groupdict()
                statistics_dict.update({'paths_allocated': int(groups['number_of_paths'])})
                continue

            # Route malloc failures:      0
            m = p13.match(line)
            if m:
                groups = m.groupdict()
                statistics_dict.update({'route_malloc_failures': int(groups['route_malloc_failures'])})
                continue

            # Path malloc failures:       0
            m = p14.match(line)
            if m:
                groups = m.groupdict()
                statistics_dict.update({'path_malloc_failures': int(groups['path_malloc_failures'])})

        return ret_dict


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
                                                Optional('inactive'): bool,
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

    cli_command = ['show rip database', 'show rip vrf {vrf} database']

    def cli(self, vrf='', output=None):
        if vrf:
            cmd = self.cli_command[1].format(vrf=vrf)
        else:
            cmd = self.cli_command[0]
            vrf = 'default'

        if output is None:
            out = self.device.execute(cmd)
        else:
            out = output
        
        ret_dict = {}

        # 172.16.0.0/16    auto-summary
        # 192.168.1.1/32
        # 2001:DB8:2:3::/64
        p1 = re.compile(r'^(?P<route>[\w\.\/:]+)(\s+(?P<summary_type>[\(\)\w-]+))?$')

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
                    routes_dict = ret_dict.setdefault('vrf', {}).setdefault(vrf, {}). \
                        setdefault('address_family', {}).setdefault(address_family, {}). \
                        setdefault('instance', {}).setdefault('rip', {}). \
                        setdefault('routes', {})

                route_dict = routes_dict.setdefault(route, {}).setdefault('index', {})

                if summary_type:
                    index_counter += 1
                    index_dict = route_dict.setdefault(index_counter, {})
                    if 'inactive' in summary_type:
                        index_dict.update({'inactive': True})
                    else:
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
