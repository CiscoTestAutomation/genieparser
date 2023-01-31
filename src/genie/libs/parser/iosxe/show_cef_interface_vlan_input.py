import re

from genie.libs.parser.utils.common import Common
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (And, Any, Default, Optional,
                                                Or, Schema, Use)

# ===============================================================
# Parser for 'show cef interface vlan 1 policy-statistics input'
# ===============================================================


class ShowCefInterfaceVlanInputSchema(MetaParser):
    """Schema for show cef interface vlan"""

    schema = {
        'state': str,
        'if_num': int,
        'vlan_name': str,
        'if_num_fast': int,
        'if_num_first': int,
    }


class ShowCefInterfaceVlanInput(ShowCefInterfaceVlanInputSchema):
    """Parser for show cef interface vlan 1 policy-statistics input"""

    cli_command = 'show cef interface vlan 1 policy-statistics input'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Vlan18 is down (if_number  207)
        p1 = re.compile(
            r"^(?P<vlan_name>\S+)\s+is\s+(?P<state>\w+)\s+\(if_number\s+(?P<if_num>\d+)\)$")
        # Corresponding hwidb if_num_fastber  207
        p2 = re.compile(
            r"^\s+Corresponding\s+hwidb\s+fast_if_number\s+(?P<if_num_fast>\d+)$")
        # Corresponding hwidb firstsw->if_number  207
        p3 = re.compile(
            r"^\s+Corresponding\s+hwidb\s+firstsw->if_number\s+(?P<if_num_first>\d+)$")

        ret_dict = {}

        for line in output.splitlines():

            # Vlan18 is down (if_number  207)
            m = p1.match(line)
            if m:
                dict_val = m.groupdict()
                ret_dict['state'] = dict_val['state']
                ret_dict['if_num'] = int(dict_val['if_num'])
                ret_dict['vlan_name'] = dict_val['vlan_name']
                continue

            #   Corresponding hwidb fast_if_number  207
            m = p2.match(line)
            if m:
                dict_val = m.groupdict()
                ret_dict['if_num_fast'] = int(dict_val['if_num_fast'])
                continue

            #   Corresponding hwidb firstsw->if_number  207
            m = p3.match(line)
            if m:
                dict_val = m.groupdict()
                ret_dict['if_num_first'] = int(dict_val['if_num_first'])
                continue

        return ret_dict
