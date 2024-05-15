'''
show_ip.py

IOSXE parsers for the following show commands:
    * show ip verify source
    * show ip verify source interface {interface_name}
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

# parser utils
from genie.libs.parser.utils.common import Common


class ShowIpVerifySourceSchema(MetaParser):

    """Schema for show ip verify source"""

    schema = {
        'index': {
            Any(): {
                Optional('ip_address'): str,
                'interface_name': str,
                'filter_type': str,
                'filter_mode': str,
                Optional('vlan'):str,
                Optional('mac_address'): str
            },
        },
    }

class ShowIpVerifySource(ShowIpVerifySourceSchema):
    """Parser for show ip verify source"""

    cli_command = ['show ip verify source', 'show ip verify source interface {interface_name}']

    def cli(self, interface_name=None, output=None):
        if output is None:
            if interface_name:
                output = self.device.execute(self.cli_command[1].format(interface_name=interface_name))
            else:
                output = self.device.execute(self.cli_command[0])

        # Gi1/0/3      ip trk       active       40.1.1.24                           10
        # Gi1/0/13   ip-mac       active       10.1.1.101       00:0A:00:0B:00:01  10
        p1 = re.compile(r"^(?P<interface_name>\S+)\s+(?P<filter_type>ip\s?\S+)\s+(?P<filter_mode>\S+)(\s+(?P<ip_address>\S+)\s+(?P<mac_address>\S+)?\s+(?P<vlan>[\d,]*))?$")

        ret_dict = {}
        index = 0
        for line in output.splitlines():
            line = line.strip()
            # Gi1/0/3      ip trk       active       40.1.1.24                           10
            m = p1.match(line)
            if m:
                dict_val = m.groupdict()
                index_dict = ret_dict.setdefault('index', {}).setdefault(index, {})
                if dict_val['ip_address']:
                    index_dict['ip_address'] = dict_val['ip_address']
                index_dict['interface_name'] = Common.convert_intf_name(dict_val['interface_name'])
                index_dict['filter_type'] = dict_val['filter_type']
                index_dict['filter_mode'] = dict_val['filter_mode']
                if dict_val['vlan']:
                    index_dict['vlan'] = dict_val['vlan']
                if dict_val['mac_address']:
                    index_dict['mac_address'] = dict_val['mac_address']
                index += 1
                continue

        return ret_dict
