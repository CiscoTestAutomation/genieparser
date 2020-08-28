""" show_lacp.py

JunOs parsers for the following show commands:
    * show lacp interfaces {interface}
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from pyats.utils.exceptions import SchemaError
from genie.metaparser.util.schemaengine import (Any,
        Optional, Use, Schema)


class ShowLacpInterfacesInterfaceSchema(MetaParser):
    """ Schema for:
            * show lacp interfaces {interface}
    """
    def validate_lag_lacp_state_list(value):
        if not isinstance(value, list):
            raise SchemaError('lag-lacp-state is not a list')
        entry_schema = Schema({
            "lacp-activity": str,
            "lacp-aggregation": str,
            "lacp-collecting": str,
            "lacp-defaulted": str,
            "lacp-distributing": str,
            "lacp-expired": str,
            "lacp-role": str,
            "lacp-synchronization": str,
            "lacp-timeout": str,
            "name": str
        })
        # Validate each dictionary in list
        for item in value:
            entry_schema.validate(item)
        return value

    def validate_lag_lacp_protocol_list(value):
        if not isinstance(value, list):
            raise SchemaError('lag-lacp-protocol is not a list')
        entry_schema = Schema({
                "lacp-mux-state": str,
                "lacp-receive-state": str,
                "lacp-transmit-state": str,
                "name": str
            })
        # Validate each dictionary in list
        for item in value:
            entry_schema.validate(item)
        return value

    schema = {
        "lacp-interface-information-list": {
            "lacp-interface-information": {
                "lag-lacp-header": {
                    "aggregate-name": str
                },
                "lag-lacp-protocol": Use(validate_lag_lacp_protocol_list),
                "lag-lacp-state": Use(validate_lag_lacp_state_list)
            }
        }
    }


class ShowLacpInterfacesInterface(ShowLacpInterfacesInterfaceSchema):
    """ Parser for:
            * show lacp interfaces {interface}
    """
    cli_command = ['show lacp interfaces {interface}']

    def cli(self, output=None, interface=None):
        if not output:
            out = self.device.execute(self.cli_command[0].format(interface=interface))
        else:
            out = output

        ret_dict = {}

        # Aggregated interface: ae4
        p1 = re.compile(r'^Aggregated +interface: +(?P<aggregate_name>\S+)$')

        #     xe-3/0/1       Actor    No    No   Yes  Yes  Yes   Yes     Fast    Active
        p2 = re.compile(r'^(?P<name>\S+) +(?P<lacp_role>\S+) +(?P<lacp_expired>\S+)'
            r' +(?P<lacp_defaulted>\S+) +(?P<lacp_distributing>\S+) +(?P<lacp_collecting>\S+)'
            r' +(?P<lacp_synchronization>\S+) +(?P<lacp_aggregation>\S+) +(?P<lacp_timeout>\S+)'
            r' +(?P<lacp_activity>\S+)$')

        #     xe-3/0/1                  Current   Fast periodic Collecting distributing
        p3 = re.compile(r'^(?P<name>\S+) +(?P<lacp_receive_state>\S+) +'
        r'(?P<lacp_transmit_state>\S+ +\S+) +(?P<lacp_mux_state>\S+ +\S+)$')

        for line in out.splitlines():
            line = line.strip()

            # Aggregated interface: ae4
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault("lacp-interface-information-list", {})\
                    .setdefault("lacp-interface-information", {})\
                        .setdefault("lag-lacp-header", {})\
                            .setdefault("aggregate-name", group['aggregate_name'])
                continue

            #     xe-3/0/1       Actor    No    No   Yes  Yes  Yes   Yes     Fast    Active
            m = p2.match(line)
            if m:
                group = m.groupdict()
                entry_list = ret_dict.setdefault("lacp-interface-information-list", {})\
                    .setdefault("lacp-interface-information", {})\
                        .setdefault("lag-lacp-state", [])
                entry = {}
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value
                entry_list.append(entry)
                continue

            #     xe-3/0/1                  Current   Fast periodic Collecting distributing
            m = p3.match(line)
            if m:
                group = m.groupdict()
                entry_list = ret_dict.setdefault("lacp-interface-information-list", {})\
                    .setdefault("lacp-interface-information", {})\
                        .setdefault("lag-lacp-protocol", [])
                entry = {}
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value
                entry_list.append(entry)
                continue

        return ret_dict
