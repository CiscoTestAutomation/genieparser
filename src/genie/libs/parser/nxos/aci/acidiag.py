""" Parsers for 'acidiag' commands """

import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any

class AcidiagFnvreadSchema(MetaParser):
    """ Schema for 'acidiag fnvread' """

    schema = {
        'id': {
            Any(): {
                'pod_id': int,
                'name': str,
                'serial_number': str,
                'ip_address': str,
                'role': str,
                'state': str,
                'last_upd_msg_id': int
            }
        }
    }

class AcidiagFnvread(AcidiagFnvreadSchema):
    """ Parser class for 'acidiag fnvread' """

    cli_command = ['acidiag fnvread']

    def cli(self, output=None):
        if not output:
            output = self.device.execute(self.cli_command[0])

        # 201        1       hw_spine1_II23      FDO221425X6     10.0.152.65/32   spine         active   0
        p1 = re.compile(r'^(?P<id>\d+) +(?P<pod_id>\d+) +(?P<name>\S+) +(?P<serial_number>\S+) +(?P<ip_address>\S+) +(?P<role>\S+) +(?P<state>\S+) +(?P<last_upd_msg_id>\d+)$')

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # 201        1       hw_spine1_II23      FDO221425X6     10.0.152.65/32   spine         active   0
            m = p1.match(line)
            if m:
                groups = m.groupdict()

                id_dict = ret_dict.setdefault('id', {}).setdefault(int(groups['id']), {})
                id_dict.update({'pod_id': int(groups['pod_id'])})
                id_dict.update({'name': groups['name']})
                id_dict.update({'serial_number': groups['serial_number']})
                id_dict.update({'ip_address': groups['ip_address']})
                id_dict.update({'role': groups['role']})
                id_dict.update({'state': groups['state']})
                id_dict.update({'last_upd_msg_id': int(groups['last_upd_msg_id'])})

        return ret_dict


