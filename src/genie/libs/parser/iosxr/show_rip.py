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
                                    'packets_received_at_standby': int,
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
        if output is None:
            if not vrf:
                vrf = 'default'
                out = self.device.execute(self.cli_command[0])
            else:
                out = self.device.execute(self.cli_command[1].format(vrf=vrf))
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