'''
IOSXE parsers for the following show commands: 
show_beacon_all.py
'''
# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any


class ShowBeaconAllSchema(MetaParser):
    """
    Schema for show beacon all
    """
    schema = {
        'switch': {
            Any(): {
                'beacon_status': str
            }
        }
    }		  


class ShowBeaconAll(ShowBeaconAllSchema):
    """ Parser for show hardware led for c9300"""

    cli_command = 'show beacon all'

    def cli(self, output=None): 
        if output is None:
            output = self.device.execute(self.cli_command)
        
        ret_dict = {}

        # Switch#   Beacon Status
        # 1        OFF
        p1 = re.compile(r'^\*?(?P<switch_number>\d+)\s+(?P<beacon_status>\w+)$')

        for line in output.splitlines():
            line = line.strip()

            # Switch#   Beacon Status
            # 1        OFF
            m=p1.match(line)
            if m:
                switch_dict = ret_dict.setdefault('switch', {}).setdefault(m.groupdict()['switch_number'], {})
                switch_dict['beacon_status'] = m.groupdict()['beacon_status']

        return ret_dict        
