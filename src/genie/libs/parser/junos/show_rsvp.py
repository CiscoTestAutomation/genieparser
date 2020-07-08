'''show_rsvp.py

JUNOS parsers for the following commands:
    * show rsvp neighbor
'''

import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional, Use, Schema
from genie.metaparser.util.exceptions import SchemaTypeError

class ShowRSVPNeighborSchema(MetaParser):
    """ Schema for:
        * show rsvp neighbor
    """

    def validate_neighbor_list(value):
        if not isinstance(value, list):
            raise SchemaTypeError('RSVP Neighbor not a list')

        rsvp_neighbor_list = Schema({
                "rsvp-neighbor-address": str,
                "neighbor-idle": str,
                "neighbor-up-count": str,
                "neighbor-down-count": str,
                "last-changed-time": str,
                "hello-interval": str,
                "hellos-sent": str,
                "hellos-received": str,
                "messages-received": str,
            })

        for item in value:
            rsvp_neighbor_list.validate(item)
        return value

    schema = {
            "rsvp-neighbor-information": {
                "rsvp-neighbor-count": str,
                "rsvp-neighbor": Use(validate_neighbor_list)
            }
        }

class ShowRSVPNeighbor(ShowRSVPNeighborSchema):
    """ Parser for:
        * show rsvp neighbor
    """

    cli_command = 'show rsvp neighbor'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # RSVP neighbor: 4 learned
        p1 = re.compile(r'^RSVP +neighbor: +(?P<rsvp_neighbor_count>\d+) +learned$')

        # 10.34.3.252      15:55  0/0       15:52        9   106/0    0
        # 10.169.14.240    34:15  0/0       34:13        9   229/0    0
        # 10.169.14.157        0  1/0       34:13        9   230/229  333
        # 2001::AF       0  1/0       15:55        9   105/105  197
        p2 = re.compile(r'^(?P<rsvp_neighbor_address>\S+) +'
                        r'(?P<neighbor_idle>\S+) +'
                        r'((?P<neighbor_up_count>\d+)/(?P<neighbor_down_count>\d+)) +'
                        r'(?P<last_changed_time>\S+) +(?P<hello_interval>\d+) +'
                        r'((?P<hellos_sent>\d+)/(?P<hellos_received>\d+)) +'
                        r'(?P<messages_received>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            # RSVP neighbor: 4 learned
            m = p1.match(line)
            if m:
                group = m.groupdict()
                neighbor_information = ret_dict.setdefault('rsvp-neighbor-information', {})
                neighbor_information['rsvp-neighbor-count'] = group['rsvp_neighbor_count']
                continue

            # 10.34.3.252      15:55  0/0       15:52        9   106/0    0
            # 10.169.14.240    34:15  0/0       34:13        9   229/0    0
            # 10.169.14.157        0  1/0       34:13        9   230/229  333
            # 2001::AF       0  1/0       15:55        9   105/105  197
            m = p2.match(line)
            if m:
                group = m.groupdict()
                rsvp_neighbor_list = neighbor_information.setdefault('rsvp-neighbor', [])
                rsvp_neighbor_list.append(
                    {k.replace('_', '-'):v for k, v in group.items() if v is not None}
                )
                continue

        return ret_dict



