import re

from genie.libs.parser.utils.common import Common
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (And, Any, Default, Optional,
                                                Or, Schema, Use)

# ======================================================
# Parser for 'show port-security interface address vlan '
# ======================================================

class ShowPortSecurityInterfaceAddressVlanSchema(MetaParser):
    """Schema for show port-security interface {interface} address vlan"""

    schema = {
        'vlan': int,
        'max': str,
        'current': int,
    }

class ShowPortSecurityInterfaceAddressVlan(ShowPortSecurityInterfaceAddressVlanSchema):
    """Parser for show port-security interface {interface} address vlan"""

    cli_command = 'show port-security interface {interface} address vlan'

    def cli(self, interface='', output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(interface=interface))

        # 2     default    3
        p1 = re.compile(r"^(?P<vlan>\d+)\s+(?P<max>\w+)\s+(?P<current>\d+)$")

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()
            # 2     default    3
            m = p1.match(line)
            if m:
                dict_val = m.groupdict()
                ret_dict['vlan'] = int(dict_val['vlan'])
                ret_dict['max'] = dict_val['max']
                ret_dict['current'] = int(dict_val['current'])
                continue


        return ret_dict

