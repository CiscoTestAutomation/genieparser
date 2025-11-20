''' show_platform.py
IOSXE parsers for the following show commands:

    * 'show switch'
    '''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional, Use, And, ListOf
from genie.libs.parser.utils.common import Common


class ShowSwitchSchema(MetaParser):
    """Schema for show switch"""
    schema = {
        'switch': {
            'mac_address': str,
            Optional('mac_persistency_wait_time'): str,
            Optional('stack'): {
                Any(): {
                    'role': str,
                    'mac_address': str,
                    'priority': str,
                    Optional('hw_ver'): str,
                    'state': str
                }
            }
        }
    }


class ShowSwitch(ShowSwitchSchema):
    """Parser for show switch."""
    cli_command = 'show switch'

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)

        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern

        # Switch/Stack Mac Address : 0057.d2ff.e71b - Local Mac Address
        p1 = re.compile(r'^([Ss]witch)?(Chassis)?\/[Ss]tack +[Mm]ac +[Aa]ddress +\: +'
                        r'(?P<switch_mac_address>[\w\.]+) *(?P<local>[\w\s\-]+)?$')

        # Mac persistency wait time: Indefinite
        p2 = re.compile(r'^[Mm]ac +persistency +wait +time\: +'
                        r'(?P<mac_persistency_wait_time>[\w\.\:]+)$')

        #                                              H/W   Current
        # Switch#   Role    Mac Address     Priority Version  State
        # -----------------------------------------------------------
        # *1       Active   689c.e2ff.b9d9     3      V04     Ready
        #  2       Standby  689c.e2ff.b9d9     14             Ready
        #  3       Member   bbcc.fcff.7b00     15     0       V-Mismatch
        p3 = re.compile(r'^\*?(?P<switch>\d+) +(?P<role>\w+) +'
                           r'(?P<mac_address>[\w\.]+) +'
                           r'(?P<priority>\d+) +'
                           r'(?P<hw_ver>[\w\d]+)? +'
                           r'(?P<state>[\w\s-]+)$')

        for line in output.splitlines():
            line = line.strip()

            # Switch/Stack Mac Address : 0057.d2ff.e71b - Local Mac Address
            m = p1.match(line)
            if m:
                switch_dict = ret_dict.setdefault('switch', {})
                switch_dict['mac_address'] = m.groupdict()['switch_mac_address']
                continue

            # Mac persistency wait time: Indefinite
            m = p2.match(line)
            if m:
                switch_dict['mac_persistency_wait_time'] = m.groupdict()['mac_persistency_wait_time'].lower()
                continue

            #                                              H/W   Current
            # Switch#   Role    Mac Address     Priority Version  State
            # -----------------------------------------------------------
            # *1       Active   689c.e2ff.b9d9     3      V04     Ready
            #  2       Standby  689c.e2ff.b9d9     14             Ready
            m = p3.match(line)
            if m:
                group = m.groupdict()
                stack = group['switch']
                match_dict = {k: v.lower()for k, v in group.items() if k in ['role', 'state']}
                match_dict.update({k: v for k, v in group.items() if k in ['priority', 'mac_address', 'hw_ver'] and v})
                switch_dict.setdefault('stack', {}).setdefault(stack, {}).update(match_dict)
                continue

        return ret_dict
