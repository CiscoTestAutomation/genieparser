import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


class ShowCdpNeighborsSchema(MetaParser):

    schema = {
        'cdp':
            {'device_id':
                {Any():
                    {'local_interface': str,
                     'hold_time': int,
                     Optional('capability'): str,
                     'platform': str,
                     'port_id': str, }, }, },
    }


class ShowCdpNeighbors(ShowCdpNeighborsSchema):

    cli_command = 'show cdp neighbors'

    def cli(self, output=None):

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}

        p1 = re.compile('^(?P<device_id>(\S+)) +'
                        '(?P<local_interface>([a-zA-Z0-9\s]+)) +'
                        '(?P<hold_time>(\d+))'
                        '(?: +(?P<capability>([A-Z\s]+)))? +'
                        '(?P<platform>([A-Z0-9\-]+)) +'
                        '(?P<port_id>([a-zA-Z0-9\/\s]+))$')

        p2 = re.compile('^(?P<device_id>(\S+)) +'
                        '(?P<local_interface>([a-zA-Z0-9\s\/]+)) +'
                        '(?P<hold_time>(\d+))'
                        '(?: +(?P<capability>([A-Z\s]+)))? +'
                        '(?P<platform>([a-zA-Z0-9\-]+)) +'
                        '(?P<port_id>([a-zA-Z0-9\/\s]+))$')

        for line in out.splitlines():
            line = line.strip()

            result = p1.match(line)

            if not result:
                result = p2.match(line)

            if result:

                if not parsed_dict:

                    device_id_dict = parsed_dict.setdefault('cdp', {}).\
                                        setdefault('device_id', {})

                group = result.groupdict()
                device_id = group['device_id'].lower().strip()

                devices_dict = device_id_dict.setdefault(device_id, {})

                devices_dict['local_interface'] = \
                    group['local_interface'].lower().strip()
                devices_dict['hold_time'] = int(group['hold_time'])
                devices_dict['capability'] = \
                    group['capability'].lower().strip()
                devices_dict['platform'] = group['platform'].lower().strip()
                devices_dict['port_id'] = group['port_id'].lower().strip()

        return parsed_dict
