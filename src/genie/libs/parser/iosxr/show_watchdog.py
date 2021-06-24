"""
show watchdog memory-state
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (Schema, Any, Optional,
                                                Or, And, Default, Use)

# Parser Utils
from genie.libs.parser.utils.common import Common


class ShowWatchdogMemoryStateSchema(MetaParser):
    """
    Schema for show watchdog memory-state
    """

    schema = {
        'node': {
            str: {
                'physical': float,
                'free': float,
                'state': str
            }
        }
    }


class ShowWatchdogMemoryState(ShowWatchdogMemoryStateSchema):
    """
    Parser for show watchdog memory-state
    """
    cli_command = "show watchdog memory-state"

    def cli(self, output=None, location=None):
        if location:
            self.cli_command += f" Location {location}"
            print(location)

        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # print(self.cli_command)

        # match the line identifying the node location
        # ---- node0_RP0_CPU0 ----
        p1 = re.compile(r'^-+\s(?P<location>\S+)\s-+$')

        # match the lines with memory amounts
        #     Physical Memory     : 4608.0   MB
        p2 = re.compile(r'^(\s+)?(?P<type>.+\b)\s+:\s+(?P<amount>\d+(\.\d+)?)\s+(?P<unit>\w+\b)$')

        # match the lines with the current memory state
        #     Memory State        :   Normal
        p3 = re.compile(r'^(\s+)?(Memory State)\s+:\s+(?P<state>.+)$')

        ret_dict = {}
        current_node = ""

        for line in out.splitlines():
            line.strip()

            # match the location line and set the current node we are gathering info from
            # everything after we match this line is a part of this node until we find a new location line
            m = p1.match(line)
            if m:
                current_node = m.groupdict()['location']
                ret_dict.setdefault('node', {}).setdefault(current_node, {})

                continue

            # match the two lines of memory statistics
            m = p2.match(line)
            if m:
                memory_type = m.groupdict()['type'].replace('Memory', '').strip().lower()
                memory_amount = float(m.groupdict()['amount'])
                memory_unit = m.groupdict()['unit']

                # not familiar enough with iosxr to know if it will output amounts in GB if enough memory is used
                # added this just in case, because we are returning a float for memory, not a string with a unit
                if memory_unit == 'GB':
                    memory_amount *= 1000

                ret_dict.get('node').get(current_node).update({memory_type: memory_amount})

                continue

            # match the line with a string describing the state of the memory
            m = p3.match(line)
            if m:
                memory_state = m.groupdict()['state']
                ret_dict.get('node').get(current_node).update({'state': memory_state})

                continue

        print(ret_dict)
        print(location)

        return ret_dict
