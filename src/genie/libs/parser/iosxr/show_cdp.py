''' show_cdp.py

IOSXR parsers for the following commands:

    * 'show cdp neighbors'
    * 'show cdp neighbors detail'

'''

# Python
import re

# Metaparser
from genie.libs.parser.utils.common import Common
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


class ShowCdpNeighborsSchema(MetaParser):

    '''
        Schema for:
            * 'show cdp neighbors'
    '''

    schema = {
        'cdp':
            {Optional('index'):
             {Any():
              {'device_id': str,
               'local_interface': str,
               'hold_time': int,
               Optional('capability'): str,
               Optional('platform'): str,
               'port_id': str, }, }, },
    }


# ================================
# Parser for 'show cdp neighbors'
# ================================
class ShowCdpNeighbors(ShowCdpNeighborsSchema):

    exclude = ['hold_time']

    cli_command = 'show cdp neighbors'

    def cli(self, output=None):

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
        #                   S - Switch, H - Host, I - IGMP, r - Repeater
        #

        # Specifically for situations when Platform and Port Id are concatenated
        p1 = re.compile(r'^(?P<device_id>\S+) +'
                         '(?P<local_interface>[a-zA-Z]+[\s]*[\d\/\.]+) +'
                         '(?P<hold_time>\d+) +(?P<capability>[RTBSHIrPDCM\s]+) +'
                         '(?P<platform>\S+)'
                         '(?P<port_id>(Fa|Gi|GE).\s*\d*\/*\d*)$')



        # No platform
        p2 = re.compile(r'^(?P<device_id>\S+) +'
                         '(?P<local_interface>[a-zA-Z]+[\s]*[\d\/\.]+) +'
                         '(?P<hold_time>\d+) +(?P<capability>[RTBSHIrPDCM\s]+)'
                         '(?: +(?P<platform>[\w\-]+) )? +'
                         '(?P<port_id>[a-zA-Z0-9\/\s]+)$')


        # device6 Gig 0 157 R S I C887VA-W-W Gi 0
        p3 = re.compile(r'^(?P<device_id>\S+) +'
                         '(?P<local_interface>[a-zA-Z]+[\s]*[\d\/\.]+) +'
                         '(?P<hold_time>\d+) +(?P<capability>[RTBSHIrPDCM\s]+) +'
                         '(?P<platform>\S+) (?P<port_id>[a-zA-Z0-9\/\s]+)$')

        # p4 and p5 for two-line output, where device id is on a separate line
        p4 = re.compile(r'^(?P<device_id>\S+)$')
        p5 = re.compile(r'(?P<local_interface>[a-zA-Z]+[\s]*[\d/.]+) +'
                        r'(?P<hold_time>\d+) +(?P<capability>[RTBSHIrPDCM\s]+) +'
                        r'(?P<platform>\S+) (?P<port_id>[a-zA-Z0-9/\s]+)$')

        device_id_index = 0
        parsed_dict = {}
        devices_dict_info = {}

        for line in out.splitlines():
            line = line.strip()

            result = p1.match(line)

            if not result:
                result = p2.match(line)
                if not result:
                    result = p3.match(line)
            if result:

                device_id_index += 1

                device_dict = devices_dict_info.setdefault(device_id_index, {})

                group = result.groupdict()

                device_dict['device_id'] = group['device_id'].strip()
                device_dict['local_interface'] = Common.convert_intf_name \
                    (intf=group['local_interface'].strip())
                device_dict['hold_time'] = int(group['hold_time'])
                device_dict['capability'] = group['capability'].strip()
                if group['platform']:
                    device_dict['platform'] = group['platform'].strip()
                elif not group['platform']:
                    device_dict['platform'] = ''

                device_dict['port_id'] = Common.convert_intf_name \
                    (intf=group['port_id'].strip())
                continue

            result = p4.match(line)
            if result:
                group = result.groupdict()
                if 'Eth' not in group['device_id']:
                    device_id_index += 1
                    device_dict = parsed_dict.setdefault('cdp', {}) \
                        .setdefault('index', {}).setdefault(device_id_index, {})
                    device_dict['device_id'] = group['device_id'].strip()
                else:
                    device_dict['port_id'] = Common \
                        .convert_intf_name(intf=group['device_id'].strip())
                continue

            result = p5.match(line)
            if result:
                group = result.groupdict()
                device_dict = parsed_dict.setdefault('cdp', {}) \
                    .setdefault('index', {}).setdefault(device_id_index, {})
                device_dict['local_interface'] = Common \
                    .convert_intf_name(intf=group['local_interface'].strip())
                device_dict['hold_time'] = int(group['hold_time'])
                device_dict['capability'] = group['capability'].strip()
                if group['platform']:
                    device_dict['platform'] = group['platform'].strip()
                elif not group['platform']:
                    device_dict['platform'] = ''

                device_dict['port_id'] = Common \
                    .convert_intf_name(intf=group['port_id'].strip())
                continue

        if device_id_index:
            parsed_dict.setdefault('cdp', {}). \
                setdefault('index', devices_dict_info)

        return parsed_dict

















