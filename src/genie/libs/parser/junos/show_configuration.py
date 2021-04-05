"""show_configuration.py

JUNOS parsers for the following commands:
    * show configuration protocols mpls label-switched-path {path}
    * show configuration protocols mpls path {path}
    * show configuration interfaces {interface} unit {unit} family bridge vlan-id
"""

import re

# Metaparser
from genie.metaparser import MetaParser
from pyats.utils.exceptions import SchemaError
from genie.metaparser.util.schemaengine import Any, Optional, Use, Schema, ListOf


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

    schema = {
        "configuration": {
            "protocols": {
                "mpls": {
                    "path": {
                        "path-list": ListOf({
                        'name': str,
                        'type': str,
                    })
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

class ShowConfigurationFamilyBridgeVlanIdSchema(MetaParser):
    """ Schema for:
        show configuration interfaces {interface} unit {unit} family bridge vlan-id
    """

    schema = {
        Optional("@xmlns:junos"): str,
        "configuration": {
            Optional("@junos:commit-localtime"): str,
            Optional("@junos:commit-seconds"): str,
            Optional("@junos:commit-user"): str,
            "interfaces": {
                "interface": {
                    "name": str,
                    "unit": {
                        "family": {
                            "bridge": {
                                "vlan-id": str
                            }
                        },
                        "name": str
                    }
                }
            }
        }
    }

class ShowConfigurationFamilyBridgeVlanId(ShowConfigurationFamilyBridgeVlanIdSchema):
    cli_command = ['show configuration interfaces {interface} unit {unit} family bridge vlan-id']

    def cli(self, interface, unit, output=None):
        if not output:
            out = self.device.execute(self.cli_command[0].format(
                interface=interface,
                unit=unit
            ))
        else:
            out = output
        ret_dict = {}
        
        # vlan-id 10;
        p1 = re.compile(r'^vlan-id +(?P<vlan_id>\S+);$')
        
        for line in out.splitlines():
            line = line.strip()

            #  vlan-id 10;
            m = p1.match(line)
            if m:
                group = m.groupdict()
                vlan_id = group['vlan_id']
                configuration_dict = ret_dict.setdefault('configuration', {})
                interface_dict = configuration_dict.setdefault('interfaces', {}). \
                    setdefault('interface', {})
                interface_dict.update({'name': interface})
                unit_dict = interface_dict.setdefault('unit', {})
                unit_dict.update({'name': unit})
                vlan_dict = unit_dict.setdefault('family', {}).setdefault('bridge', {})
                vlan_dict.update({'vlan-id': vlan_id})
                continue

        return ret_dict