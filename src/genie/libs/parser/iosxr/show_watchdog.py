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
            Any(): {
                'physical_memory_mb': float,
                'free_memory_mb': float,
                'state': str
            }
        }
    }


class ShowWatchdogMemoryState(ShowWatchdogMemoryStateSchema):
    """
    Parser for show watchdog memory-state
    """
    cli_command = ["show watchdog memory-state", "show watchdog memory-state Location {location}"]

    def cli(self, output=None, location=None):
        if not output:
            if location:
                cmd = self.cli_command[1].format(location=location)
            else:
                cmd = self.cli_command[0]

            out = self.device.execute(cmd)

        else:
            out = output

        # ---- node0_RP0_CPU0 ----
        p1 = re.compile(r'^-+\s(?P<location>\S+)\s-+$')

        # match the lines with memory amounts
        #     Physical Memory     : 4608.0   MB
        p2 = re.compile(r'^(?P<type>.+\b)\s+:\s+(?P<amount>\d+(\.\d+)?)\s+(?P<unit>\w+\b)$')

        # match the lines with the current memory state
        #     Memory State        :   Normal
        p3 = re.compile(r'^(Memory State)\s+:\s+(?P<state>.+)$')

        ret_dict = {}
        current_node = ""

        for line in out.splitlines():
            line = line.strip()

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
                group = m.groupdict()

                memory_type = group['type'].replace('Memory', '').strip().lower() + '_memory_mb'
                memory_amount = float(group['amount'])
                memory_unit = group['unit']

                if memory_unit == 'GB':
                    memory_amount *= 1000

                ret_dict.get('node').get(current_node).update({memory_type: memory_amount})

                continue

            # match the line with a string describing the state of the memory
            m = p3.match(line)
            if m:
                group = m.groupdict()

                memory_state = group['state']
                ret_dict.get('node').get(current_node).update({'state': memory_state})

                continue

        return ret_dict
