"""
show_nameif.py
Parser for the following command:
    * show nameif
"""
import re

from pprint import pprint
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (Schema, Any, Optional)
from genie import parsergen


class ShowNameifSchema(MetaParser):
    """ Schema for
        * show nameif
    """

    schema = {
        Any(): {
            'interface': str,
            'name': str,
            'security_level': int
        }
    }


class ShowNameif(ShowNameifSchema):
    """ Parser for
        * show nameif
    """
    cli_command = 'show nameif'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Interface                Name                     Security
        # GigabitEthernet0/0       outside                    0
        header = ['Interface', 'Name', 'Security']

        result = parsergen.oper_fill_tabular(
            device_output=out,
            device_os='asa',
            header_fields=header,
            index=[0]
        )
        nameif_entries = result.entries

        line_dict = {}

        for k in nameif_entries.keys():
            curr_dict = nameif_entries[k]

            interface_dict = line_dict.setdefault(k, {})
            interface_dict.update({'interface': curr_dict['Interface']})
            interface_dict.update({'name': curr_dict['Name']})
            interface_dict.update({
                'security_level': int(curr_dict['Security'])
            })

        return line_dict
