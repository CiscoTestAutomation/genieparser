"""
Dummy parser for test:
    * show inventory
"""
# Python
import re
import logging

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional

class ShowInventorySchema(MetaParser):

    """ Schema for:
        * show inventory
    """
    schema = {
        'index': {
            Any():
                {'name': str,
                 'descr': str,
                 Optional('pid'): str,
                 Optional('vid'): str,
                 Optional('sn'): str,
                }
            }
        }

class ShowInventory(ShowInventorySchema):
    """
    Parser for :
        * show inventory
    """

    cli_command = 'show inventory'

    def cli(self, output=None):
        print("-------------- new c9300 parser -------------------")
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}
        index = 0

        # --------------------------------------------------------------
        # Regex patterns
        # --------------------------------------------------------------
        # NAME: "c93xx Stack", DESCR: "c93xx Stack"
        p1 = re.compile(r'^NAME: +\"(?P<name>[\s\S]+)\",'
                        r' +DESCR: +\"(?P<descr>[\s\S]+)\"$')

        # PID: C9300-48UXM       , VID: V02  , SN: FCW2242G0V3
        # PID: C9300-24T         , VID:      , SN:
        p2 = re.compile(r'^PID: +(?P<pid>\S+) +, +VID:( +(?P<vid>\S+))? +,'
                        r' +SN:( +(?P<sn>\S+))?$')

        # --------------------------------------------------------------
        # Build the parsed output
        # --------------------------------------------------------------
        for line in out.splitlines():
            line = line.strip()

            # NAME: "c93xx Stack", DESCR: "c93xx Stack"
            m = p1.match(line)
            if m:
                index += 1
                group = m.groupdict()
                final_dict = parsed_dict.setdefault('index', {}).setdefault(index, {})
                for key in group.keys():
                    if group[key]:
                        final_dict[key] = group[key]
                continue

            # PID: C9300-48UXM       , VID: V02  , SN: FCW2242G0V3
            m = p2.match(line)
            if m:
                group = m.groupdict()
                for key in group.keys():
                    if group[key]:
                        final_dict[key] = group[key]
                continue

        return parsed_dict


