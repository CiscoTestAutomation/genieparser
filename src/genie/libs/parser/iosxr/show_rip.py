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
                                'default_metric': int,
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

        if output is None:
            if not vrf:
                vrf = 'default'
                out = self.device.execute(self.cli_command[0])
            else:
                out = self.device.execute(self.cli_command[1].format(vrf=vrf))
        else:
            out = output

        instance = 'rip'
        ret_dict = {}

        # RIP config:
        p1 = re.compile(r'^RIP +config:$')

        # Active:                    Yes
        p2 = re.compile(r'^Active:\s+(?P<active>\w+)$')

        # Added to socket:           Yes
        p3 = re.compile(r'^Added +to +socket:\s+(?P<added_to_socket>\w+)$')

        # Out-of-memory state:        Normal
        p4 = re.compile(r'^Out-of-memory +state:\s+(?P<memory_state>\w+)$')

        # Version:                    2.3
        p5 = re.compile(r'^Version:\s+(?P<version>[\d.]+)$')

        # Default metric:             3
        p6 = re.compile(r'^Default +metric:\s+(?P<default_metric>\d+)$')

        # Maximum paths:              4
        p7 = re.compile(r'^Maximum +paths:\s+(?P<max_paths>\d+)$')

        # Auto summarize:            No
        p8 = re.compile(r'^Auto +summarize:\s+(?P<auto_summarize>\w+)$')

        # Broadcast for V2:          No
        p9 = re.compile(r'^Broadcast +for +V2:\s+(?P<broadcast>\w+)$')

        # Packet source validation:  Yes
        p10 = re.compile(r'^Packet +source +validation:\s+(?P<packet_validation>\w+)$')

        # NSF:                        Disabled
        p11 = re.compile(r'^NSF:\s+(?P<nsf>\w+)$')

        # Timers: Update:             10 seconds (7 seconds until next update)
        p12 = re.compile(r'^Timers: +Update:\s+(?P<update_timer>\d+) +seconds +\((?P<next_update>\d+)[\s\w]+\)$')

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
                instance_dict = ret_dict.setdefault('vrf', {}).setdefault(vrf, {}).setdefault('address_family', {}). \
                                        setdefault('ipv4', {}).setdefault('instance', {}).setdefault(instance, {})
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
                instance_dict.update({'default_metric': int(groups['default_metric'])})
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
                instance_dict.update({'packet_source_validation': groups['packet_validation']})
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
