'''show_rsvp.py

JUNOS parsers for the following commands:
    * show rsvp neighbor
    * show rsvp session
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


class ShowRSVPSessionSchema(MetaParser):
    """ Schema for:
        * show rsvp session
    """

    def validate_session_data_list(value):
        if not isinstance(value, list):
            raise SchemaTypeError('RSVP session data not a list')

        def validate_session_list(value):
            if not isinstance(value, list):
                raise SchemaTypeError('RSVP session not a list')

            rsvp_session_list = Schema({
                    "destination-address": str,
                    "source-address": str,
                    "lsp-state": str,
                    "route-count": str,
                    "rsb-count": str,
                    "resv-style": str,
                    "label-in": str,
                    "label-out": str,
                    "name": str,
                })

            for item in value:
                rsvp_session_list.validate(item)
            return value

        rsvp_session_data_list = Schema({
                "session-type": str,
                "count": str,
                Optional("rsvp-session"): Use(validate_session_list),
                "display-count": str,
                "up-count": str,
                "down-count": str,
            })

        for item in value:
            rsvp_session_data_list.validate(item)
        return value

    schema = {
            "rsvp-session-information": {
                "rsvp-session-data": Use(validate_session_data_list)
            }
        }

class ShowRSVPSession(ShowRSVPSessionSchema):
    """ Parser for:
        * show rsvp session
    """

    cli_command = 'show rsvp session'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # Ingress RSVP: 0 sessions
        # Egress RSVP: 0 sessions
        # Transit RSVP: 30 sessions
        p1 = re.compile(r'^(?P<session_type>\S+) RSVP: +(?P<count>\d+) +sessions$')

        # Total 30 displayed, Up 30, Down 0
        p2 = re.compile(r'^Total +(?P<display_count>\d+) +displayed, +'
                        r'Up +(?P<up_count>\d+), +Down +(?P<down_count>\d+)$')

        # 10.49.194.125 10.49.194.127 Up 0 1 FF 46 44 test_lsp_01
        p3 = re.compile(r'^(?P<destination_address>[\d\.]+) +'
                        r'(?P<source_address>[\d\.]+) +(?P<lsp_state>\S+) +'
                        r'(?P<route_count>\d+) +(?P<rsb_count>\d+) +'
                        r'(?P<resv_style>\S+) +(?P<label_in>\S+) +'
                        r'(?P<label_out>\S+) +(?P<name>\S+)$')
        

        for line in out.splitlines():
            line = line.strip()

            # Ingress RSVP: 0 sessions
            # Egress RSVP: 0 sessions
            # Transit RSVP: 30 sessions
            m = p1.match(line)
            if m:
                group = m.groupdict()
                session_data_list = ret_dict.setdefault('rsvp-session-information', {}) \
                                        .setdefault('rsvp-session-data', [])
                session_data_dict = {}
                session_data_dict.update(
                    {k.replace('_', '-'):v for k, v in group.items() if v is not None}
                )
                session_data_list.append(session_data_dict)
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                session_data_dict.update(
                    {k.replace('_', '-'):v for k, v in group.items() if v is not None}
                )
                continue

            m = p3.match(line)
            if m:
                group = m.groupdict()
                rsvp_session_list = session_data_dict.setdefault('rsvp-session', [])
                rsvp_session_dict = {}
                rsvp_session_dict.update(
                    {k.replace('_', '-'):v for k, v in group.items() if v is not None}
                )
                rsvp_session_list.append(rsvp_session_dict)
                continue

        return ret_dict



