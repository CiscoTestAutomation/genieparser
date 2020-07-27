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

        # to 10.49.194.125;
        p1 = re.compile(r'^to +(?P<to>[\S]+);$')

        # revert-timer 0;
        p2 = re.compile(r'^revert-timer +(?P<revert_timer>[\S]+);$')

        # priority 3 3;
        p3 = re.compile(r'^priority +(?P<setup_priority>[\S]+) +(?P<reservation_priority>[\S]+);$')

        # primary test_path_01;
        p4 = re.compile(r'^primary +(?P<primary>[\S]+);$')

        # no-cspf;
        # record;
        # inter-domain;
        p5 = re.compile(r'^(?P<flag>[^\s;]+);$')

        for line in out.splitlines():
            line = line.strip()

            # to 10.49.194.125;
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

    def validate_path_list_schema(value):
        if not isinstance(value, list):
            raise SchemaTypeError('path list schema is not a list')
    
        path_list_schema = Schema({
            'name': str,
            'type': str,
        })
    
        for item in value:
            path_list_schema.validate(item)
        return value

    schema = {
        "configuration": {
            "protocols": {
                "mpls": {
                    "path": {
                        "path-list": Use(validate_path_list_schema)
                    }
                }
            }
        }
    }

class ShowConfigurationProtocolsMplsPath(ShowConfigurationProtocolsMplsPathSchema):
    """ Parser for:
        * show configuration protocols mpls path {path}
    """

    cli_command = 'show configuration protocols mpls path {path}'

    def cli(self, path, output=None):
        if not output:
            out = self.device.execute(self.cli_command.format(path=path))
        else:
            out = output

        ret_dict = {}

        # 10.0.0.1 strict;
        p1 = re.compile(r'^(?P<name>\S+) +(?P<type>[\S]+);$')

        for line in out.splitlines():
            line = line.strip()

            # 10.0.0.1 strict;
            m = p1.match(line)
            if m:
                group = m.groupdict()
                path_list = ret_dict.setdefault('configuration', {})\
                                    .setdefault('protocols', {})\
                                    .setdefault('mpls', {})\
                                    .setdefault('path', {})\
                                    .setdefault('path-list', [])
                path_dict = {}
                path_dict.update({
                    k.replace('_', '-'): v for k, v in group.items() if v is not None
                })
                path_list.append(path_dict)

        return ret_dict