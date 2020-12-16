from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Optional
import re

# ======================================================
# Schema for 'show ip brief'
# ======================================================


class ShowIPBrSchema(MetaParser):
    schema = {
        'ints': {
            'gateway': str,
            'L3_MAC': str,
            Any(): {
                'state': str,
                'ip_address': str,
                'mask': str,
                'method': str
            }
        }
    }


class ShowIPBr(ShowIPBrSchema):
    """Parser for show ip brief on Dell PowerSwitch OS6 devices
    parser class - implements detail parsing mechanisms for cli output.
    """
    cli_command = 'show ip brief'

    """
    Default Gateway................................ 192.168.1.100
    L3 MAC Address................................. F8B1.5683.8734

    Routing Interfaces:

    Interface    State   IP Address      IP Mask         Method
    ----------   -----   --------------- --------------- -------
    Vl1          Down    10.10.10.216    255.255.255.0   DHCP
    Vl20         Up      10.10.21.70     255.255.255.0   DHCP
    """

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        ip_dict = {}

        result_dict = {}

        p0 = re.compile(
            r'^Default+ Gateway+\.+ +(?P<gateway>\d+\.\d+\.\d+\.\d+)')

        p1 = re.compile(r'^L3+ MAC+ Address+\.+ +(?P<l3_mac>....\.....\.....)')

        p2 = re.compile(
            r'^(?P<int_name>[\w]+)+\s+(?P<state>\w+)+\s+(?P<ip_add>[\d+\.]+)+\s+(?P<mask>[\d+\.]+)+\s+(?P<method>\w+)')

        for line in out.splitlines():
            line = line.strip()

            m = p0.match(line)
            if m:
                def_gw = m.groupdict()['gateway']
                if 'ints' not in ip_dict:
                    result_dict = ip_dict.setdefault('ints', {})
                result_dict['gateway'] = def_gw
                continue

            m = p1.match(line)
            if m:
                l3_mac = m.groupdict()['l3_mac']
                result_dict['L3_MAC'] = l3_mac
                continue

            m = p2.match(line)
            if m:
                interface = m.groupdict()['int_name']
                state = m.groupdict()['state']
                ip_address = m.groupdict()['ip_add']
                mask = m.groupdict()['mask']
                method = m.groupdict()['method']
                if interface not in result_dict:
                    result_dict[interface] = {}
                    result_dict[interface]['state'] = state
                    result_dict[interface]['ip_address'] = ip_address
                    result_dict[interface]['mask'] = mask
                    result_dict[interface]['method'] = method
                continue
        return ip_dict
