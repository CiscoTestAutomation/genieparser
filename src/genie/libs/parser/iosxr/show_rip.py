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
                                    'update_interval': str,
                                    'invalid_interval': str,
                                    'holddown_interval': str,
                                    'flush_interval': str
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

    cli_commands = ['show rip', 'show rip vrf {vrf}']

    def cli(self, vrf="", output=None):

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
        # VRF: <name>
        p1 = re.compile(r'^VRF: +(?P<vrf>\w+)$')
        # Active:                    Yes
        # Added to socket:           Yes
        # Out-of-memory state:        Normal
        # Version:                    2.3
        # Default metric:             3
        # Maximum paths:              4
        # Auto summarize:            No
        # Broadcast for V2:          No
        # Packet source validation:  Yes
        # NSF:                        Disabled
        p2 = re.compile(r'^(?P<parameter>[A-Z][\w\- ]*?):\s+(?P<value>[\w.]+)$')
        # Timers: Update:             10 seconds (7 seconds until next update)
        # Invalid:            31 seconds
        # Holddown:           32 seconds
        # Flush:              33 seconds
        p3 = re.compile(r'^(\w+: )?(?P<timer_type>\w+):\s+(?P<interval>\d+ +seconds)([ \w\(\)]+)?$')

        ret_dict = {}

        if out:
            vrf_dict = ret_dict.setdefault('vrf', {})

        for line in out.splitlines():
            line = line.strip()
            m = p1.match(line)
            if m:
                group = m.groupdict()
                vrf = group['vrf']
                continue

            # Initial datastructure setup after vrf type is determined
            if "RIP config:" in line:
                vrf = vrf if vrf else None
                rip_dict = vrf_dict.setdefault(vrf, {}) \
                                    .setdefault('address_family', {}).setdefault(None, {}) \
                                    .setdefault('instance', {}). setdefault('rip', {})
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                parameter = group['parameter']
                parameter = re.sub(r'[ -]', '_', parameter)
                parameter = parameter.lower()
                # parameter = parameter.replace(" ", "_").replace("-", "_")
                value = group['value']

                if parameter in ['version', 'default_metric', 'maximum_paths']:
                    rip_dict.update({parameter: int(value)})
                else:
                    rip_dict.update({parameter: value})
                continue

            m = p3.match(line)
            if m:
                if "Timers:" in line:
                    timer_dict = rip_dict.setdefault('timers', {})

                group = m.groupdict()
                timer_type = group['timer_type']
                timer_type = timer_type.lower()
                interval = group['interval']

                timer_dict.update({'{}_interval'.format(timer_type): interval})

        return ret_dict
