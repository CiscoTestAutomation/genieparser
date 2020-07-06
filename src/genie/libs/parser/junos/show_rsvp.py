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
                "neighbor-idle": {
                    "@junos:seconds": str,
                    "#text": str,
                },
                "neighbor-up-count": str,
                "neighbor-down-count": str,
                "last-changed-time": {
                    "@junos:seconds": str,
                    "#text": str,
                },
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

    # 59.128.3.252      15:55  0/0       15:52        9   106/0    0
    # 106.187.14.240    34:15  0/0       34:13        9   229/0    0
    # 106.187.14.157        0  1/0       34:13        9   230/229  333
    # 2001::AF       0  1/0       15:55        9   105/105  197
    p2 = re.compile(r'')

    for line in out.splitlines():
        line = line.strip()


