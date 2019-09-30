"""show_l2route.py

show l2route parser class

"""

import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


class ShowL2routeTopologySchema(MetaParser):
    """Schema for:
        * 'show l2route topology'
    """
    schema = {
        Any(): {
            'topo_id': {
                Any(): {
                    'topo_name': {
                        Any(): {
                            Optional('topo_type'): str
                        }
                    }
                }
            }
        }
    }


class ShowL2routeTopology(ShowL2routeTopologySchema):
    """Parser class for show l2route topology """

    cli_command = 'show l2route topology'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Topology ID   Topology Name    Type
        # -----------   -------------    ----
        # 51             bd2              L2VRF
        # 4294967294     GLOBAL           N/A
        # 4294967295     ALL              N/A

        p = re.compile(
            r'^\s*(?P<topo_id>\d+)\s* +'
            r'(?P<topo_name>\S+)\s* +'
            r'(?:N/A|(?P<topo_type>\S+))')

        parsed_dict = {}
        counts = 0

        for line in out.splitlines():
            line = line.rstrip()

            result = p.match(line)

            if result:
                counts += 1
                group_dict = result.groupdict()

                str_topology = 'topology %d' % counts
                str_id = group_dict['topo_id']
                str_name = group_dict['topo_name']
                str_type = group_dict['topo_type']

                if str_type is None:
                    str_type = 'N/A'

                id_dict = {}
                name_dict = {}
                type_dict = {}

                id_dict['topo_id'] = {}
                name_dict['topo_name'] = {}
                type_dict['topo_type'] = {}

                type_dict['topo_type'] = str_type
                name_dict['topo_name'].setdefault(str_name, type_dict)
                id_dict['topo_id'].setdefault(str_id, name_dict)

                parsed_dict.update({str_topology: id_dict})

                continue

        return parsed_dict
