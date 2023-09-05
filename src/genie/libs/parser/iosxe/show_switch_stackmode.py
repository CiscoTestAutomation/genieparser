import re

from genie.libs.parser.utils.common import Common
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (And, Any, Default, Optional,
                                                Or, Schema, Use)

# ======================================================
# Parser for 'show switch stack-mode '
# ======================================================

class ShowSwitchStackModeSchema(MetaParser):
    """Schema for show switch stack-mode"""

    schema = {
        'switch': {
            Any(): {
                'switch_id': int,
                'role': str,
                'mac_address': str,
                'version': str,
                'mode': str,
                'configured': str,
                'state': str,
            },
        },

    }

class ShowSwitchStackMode(ShowSwitchStackModeSchema):
    """Parser for show switch stack-mode"""

    cli_command = 'show switch stack-mode'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # *1      Active   4cbc.4897.ec80    V00     N+1     None       Ready
        # *1      Active   00a5.bf53.d400    V02     N+1'    Active'    Ready               
        p1 = re.compile(r"\s*\**(?P<switch_id>\d+)\s+(?P<role>\w+)\s+(?P<mac_address>\S+)\s+(?P<version>\S+)\s+(?P<mode>\S+)\s+(?P<configured>\w+)\'?\s+(?P<state>\w+)\s+$")

        ret_dict = {}

        for line in output.splitlines():

            # *1      Active   4cbc.4897.ec80    V00     N+1     None       Ready

            m = p1.match(line)
            if m:
                dict_val = m.groupdict()
                switch_id_var = dict_val['switch_id']
                switch = ret_dict.setdefault('switch', {})
                switch_id_dict = ret_dict['switch'].setdefault(switch_id_var, {})
                switch_id_dict['switch_id'] = int(dict_val['switch_id'])
                switch_id_dict['role'] = dict_val['role']
                switch_id_dict['mac_address'] = dict_val['mac_address']
                switch_id_dict['version'] = dict_val['version']
                switch_id_dict['mode'] = dict_val['mode']
                switch_id_dict['configured'] = dict_val['configured']
                switch_id_dict['state'] = dict_val['state']
                continue


        return ret_dict

