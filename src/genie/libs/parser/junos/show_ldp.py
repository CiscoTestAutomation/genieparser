"""show_ldp.py

JUNOS parsers for the following commands:
    * show ldp session
    * show ldp neighbor
"""

import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional, Use, Schema
from genie.metaparser.util.exceptions import SchemaTypeError


class ShowLDPSessionSchema(MetaParser):
    """ Schema for
        * show ldp session
    """
    def validate_ldp_session(value):
        if not isinstance(value, list):
            raise SchemaTypeError('LDP Session not a list')

        ldp_session = Schema({
            "ldp-neighbor-address": str,
            "ldp-session-state": str,
            "ldp-connection-state": str,
            "ldp-remaining-time": str,
            Optional("ldp-session-adv-mode"): str,
        })

        for item in value:
            ldp_session.validate(item)
        return value

    schema = {
        "ldp-session-information": {
            "ldp-session": Use(validate_ldp_session)
        }
    }


class ShowLDPSession(ShowLDPSessionSchema):
    """ Parser for:
        * show ldp session
    """

    cli_command = 'show ldp session'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # 59.128.2.250                        Operational Open          26         DU
        p1 = re.compile(r'^(?P<ldp_neighbor_address>\S+) +'
                        r'(?P<ldp_session_state>\S+) +'
                        r'(?P<ldp_connection_state>\S+) +'
                        r'(?P<ldp_remaining_time>\d+)( +)?'
                        r'(?P<ldp_session_adv_mode>\S+)?$')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                session_list = ret_dict.setdefault("ldp-session-information",
                                                   {}).setdefault(
                                                       "ldp-session", [])
                session_list.append({
                    k.replace('_', '-'): v
                    for k, v in group.items() if v is not None
                })

        return ret_dict


class ShowLdpNeighborSchema(MetaParser):
    """ Schema for:
            * show ldp neighbor
    """

    schema = {
    Optional("@xmlns:junos"): str,
    "ldp-neighbor-information": {
        Optional("@xmlns"): str,
        "ldp-neighbor": [
                {
            "interface-name": str,
            "ldp-label-space-id": str,
            "ldp-neighbor-address": str,
            "ldp-remaining-time": str
                }
            ]
        }
    }

    def validate_ldp_neighbor(value):
        if not isinstance(value, list):
            raise SchemaTypeError('LDP neighbor is not a list')

        ldp_neighbor = Schema({
            "interface-name": str,
            "ldp-label-space-id": str,
            "ldp-neighbor-address": str,
            "ldp-remaining-time": str
        })

        for item in value:
            ldp_neighbor.validate(item)
        return value

    schema = {
    Optional("@xmlns:junos"): str,
    "ldp-neighbor-information": {
        Optional("@xmlns"): str,
        "ldp-neighbor": Use(validate_ldp_neighbor)
        }
    }

class ShowLdpNeighbor(ShowLdpNeighborSchema):
    """ Parser for:
            * show ldp neighbor
    """

    cli_command = 'show ldp neighbor'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # 106.187.14.158                      ge-0/0/0.0      59.128.2.250:0       14
        p1 = re.compile(
            r'^(?P<ldp_neighbor_address>\S+) '
            r'+(?P<interface_name>\S+) +(?P<ldp_label_space_id>\S+) '
            r'+(?P<ldp_remaining_time>\S+)$'
        )

        for line in out.splitlines():
            line = line.strip()

            # 106.187.14.158                      ge-0/0/0.0      59.128.2.250:0       14
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ldp_neighbor_list = ret_dict.setdefault('ldp-neighbor-information', {}).\
                    setdefault('ldp-neighbor', [])
                ldp_dict = {}
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_', '-')
                    ldp_dict[entry_key] = group_value

                ldp_neighbor_list.append(ldp_dict)
                continue

        return ret_dict