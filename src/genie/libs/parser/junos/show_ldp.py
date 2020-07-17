"""show_ldp.py

JUNOS parsers for the following commands:
    * show ldp session
    * show ldp interface {interface}
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

        # 10.34.2.250                        Operational Open          26         DU
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


class ShowLDPInterfaceSchema(MetaParser):
    """ Schema for:
            * show ldp interface {interface}
    """
    schema = {
        Optional("@xmlns:junos"): str,
        "ldp-interface-information": {
            Optional("@xmlns"): str,
            "ldp-interface": {
                "interface-name": str,
                "ldp-interface-local-address": str,
                "ldp-label-space-id": str,
                "ldp-neighbor-count": str,
                "ldp-next-hello": str
            }
        }
    }


class ShowLDPInterface(ShowLDPInterfaceSchema):
    """ Parser for:
            * show ldp interface {interface}
    """
    cli_command = 'show ldp interface {interface}'

    def cli(self, interface, output=None):
        if not output:
            out = self.device.execute(self.cli_command.format(
                interface=interface
            ))
        else:
            out = output
        
        # ge-0/0/0.0         106.187.14.157                   106.187.14.240:0  1      3
        p1 = re.compile(r'^(?P<interface_name>\S+) +(?P<local_address>\S+) +'
            r'(?P<space_id>\S+) +(?P<neighbor_count>\d+) +(?P<next_hello>\d+)$')

        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # ge-0/0/0.0         106.187.14.157                   106.187.14.240:0  1      3
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ldp_interface_info_dict = ret_dict.setdefault('ldp-interface-information', {}). \
                    setdefault('ldp-interface', {})
                ldp_interface_info_dict.update({'interface-name': group['interface_name']})
                ldp_interface_info_dict.update({'ldp-interface-local-address': group['local_address']})
                ldp_interface_info_dict.update({'ldp-label-space-id': group['space_id']})
                ldp_interface_info_dict.update({'ldp-neighbor-count': group['neighbor_count']})
                ldp_interface_info_dict.update({'ldp-next-hello': group['next_hello']})
                continue

        return ret_dict
