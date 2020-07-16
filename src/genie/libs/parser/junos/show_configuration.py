"""show_configuration.py

JUNOS parsers for the following commands:
    * show configuration protocols mpls label-switched-path {path}
    * show configuration protocols mpls path {path}
"""

import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional, Use, Schema
from genie.metaparser.util.exceptions import SchemaTypeError

class ShowConfigurationProtocolsMplsLabelSwitchedPathSchema(MetaParser):
    """ Schema for:
        * show configuration protocols mpls label-switched-path {path}
    """

    schema = {
            "configuration": {
                "protocols": {
                    "mpls": {
                        "label-switched-path": {
                            Optional("name"): str,
                            "to": str,
                            "revert-timer": str,
                            Optional("no-cspf"): bool,
                            "setup-priority": str,
                            "reservation-priority": str,
                            Optional("record"): bool,
                            Optional("inter-domain"): bool,
                            "primary": {
                                "name": str,
                            }
                        }
                    }
                }
            }
        }

class ShowConfigurationProtocolsMplsLabelSwitchedPath(ShowConfigurationProtocolsMplsLabelSwitchedPathSchema):
    """ Parser for:
        * show configuration protocols mpls label-switched-path {path}
    """

    cli_command = 'show configuration protocols mpls label-switched-path {path}'

    def cli(self, path, output=None):
        if not output:
            out = self.device.execute(self.cli_command.format(path=path))
        else:
            out = output

        ret_dict = {}

        # to 27.85.194.125;
        p1 = re.compile(r'^to +(?P<to>[^\s;]+);$')

        # revert-timer 0;
        p2 = re.compile(r'^revert-timer +(?P<revert_timer>[^\s;]+);$')

        # priority 3 3;
        p3 = re.compile(r'^priority +(?P<setup_priority>[^\s;]+) +(?P<reservation_priority>[^\s;]+);$')

        # primary test_path_01;
        p4 = re.compile(r'^primary +(?P<primary>[^\s;]+);$')

        # no-cspf;
        # record;
        # inter-domain;
        p5 = re.compile(r'^(?P<flag>[^\s;]+);$')

        for line in out.splitlines():
            line = line.strip()

            # to 27.85.194.125;
            m = p1.match(line)
            if m:
                group = m.groupdict()
                path_dict = ret_dict.setdefault('configuration', {})\
                                    .setdefault('protocols', {})\
                                    .setdefault('mpls', {})\
                                    .setdefault('label-switched-path', {})
                path_dict['to'] = group.get('to')

            # revert-timer 0;
            m = p2.match(line)
            if m:
                group = m.groupdict()
                path_dict['revert-timer'] = group.get('revert_timer')

            # priority 3 3;
            m = p3.match(line)
            if m:
                group = m.groupdict()
                path_dict['setup-priority'] = group.get('setup_priority')
                path_dict['reservation-priority'] = group.get('reservation_priority')

            # primary test_path_01;
            m = p4.match(line)
            if m:
                group = m.groupdict()
                path_dict['primary'] = {
                    "name": group.get('primary')
                }

            # no-cspf;
            # record;
            # inter-domain;
            m = p5.match(line)
            if m:
                group = m.groupdict()
                path_dict.update({
                    v: True for v in group.values()
                })

        return ret_dict



class ShowConfigurationProtocolsMplsPathSchema(MetaParser):
    """ Schema for:
        show configuration protocols mpls path {path}
    """

class ShowConfigurationProtocolsMplsPath(ShowConfigurationProtocolsMplsPathSchema):
    pass