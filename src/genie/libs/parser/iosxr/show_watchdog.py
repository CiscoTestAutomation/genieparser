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
from genie.libs.sdk.apis.utils import unit_convert


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

    def cli(self, location=None, output=None):
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

        #     Physical Memory     : 4608.0   MB
        p2 = re.compile(r'^(?P<type>.+\b)\s+:\s+(?P<amount>\d+(\.\d+)?)\s+(?P<unit>\w+\b)$')

        #     Memory State        :   Normal
        p3 = re.compile(r'^(Memory\s+State)\s+:\s+(?P<state>.+)$')

        ret_dict = {}
        current_node_dict = {}
        current_node = ""

        for line in out.splitlines():
            line = line.strip()

            # ---- node0_RP0_CPU0 ----
            m = p1.match(line)
            if m:
                group = m.groupdict()
                current_node = group['location']
                current_node_dict = ret_dict.setdefault('node', {}).setdefault(current_node, {})
                continue

            #     Physical Memory     : 4608.0   MB
            m = p2.match(line)
            if m:
                group = m.groupdict()
                memory_type = group['type'].replace('Memory', '').strip().lower() + '_memory_mb'
                memory_amount = float(group['amount'])
                memory_unit = group['unit']

                if memory_unit == 'GB':
                    memory_amount = unit_convert((str(memory_amount)+'G'), 'M')

                current_node_dict.update({memory_type: memory_amount})
                continue

            #     Memory State        :   Normal
            m = p3.match(line)
            if m:
                group = m.groupdict()
                memory_state = group['state']
                current_node_dict.update({'state': memory_state})
                continue

        return ret_dict
