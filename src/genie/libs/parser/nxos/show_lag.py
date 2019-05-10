"""show_lag.py
    supported commands:
    * show feature
    * show lacp system-identifier
    * show lacp counters
    * show lacp neighbor
    * show port-channel summary
    * show port-channel database
"""

# Python
import re
import random

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
    Any, \
    Optional, \
    Or, \
    And, \
    Default, \
    Use

# import parser utils
from genie.libs.parser.utils.common import Common


# ============================
# parser for show feature
# ============================
class ShowFeatureSchema(MetaParser):
    """schema for: show feature"""
    schema = {
        'features': {
            Any(): {
                'instances': {
                    Any(): bool
                }
            }
        }
    }


class ShowFeature(ShowFeatureSchema):
    """parser for show feature"""
    cli_command = 'show feature'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # init dictionary
        parsed_dict = {}
        # bash-shell             1          disabled
        p1 = re.compile(
            r'^(?P<feature_name>[\w-]+)\s+(?P<instance>\d+)\s+(?P<state>('
            r'disabled|enabled))$')

        for line in out.splitlines():
            line = line.strip()
            # bash-shell             1          disabled
            m = p1.match(line)
            if m:
                group = m.groupdict()
                state = True if group['state'] == 'enabled' else False
                sub_dict = parsed_dict.setdefault('features', {}).setdefault(
                    group['feature_name'], {}).setdefault('instances', {})
                sub_dict[group['instance']]=state

                continue
        return parsed_dict





