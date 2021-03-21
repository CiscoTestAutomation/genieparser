""" show_lacp.py

JunOs parsers for the following show commands:
    * show lacp interfaces {interface}
    * show lacp statistics interfaces {interface}
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from pyats.utils.exceptions import SchemaError
from genie.metaparser.util.schemaengine import (Any,
        Optional, Use, Schema, ListOf)


class ShowLacpInterfacesInterfaceSchema(MetaParser):
    """ Schema for:
            * show lacp interfaces {interface}
    """

    schema = {
        "lacp-interface-information-list": {
            "lacp-interface-information": {
                "lag-lacp-header": {
                    "aggregate-name": str
                },
                "lag-lacp-protocol": ListOf({
                    "lacp-mux-state": str,
                    "lacp-receive-state": str,
                    "lacp-transmit-state": str,
                    "name": str
                }),
                "lag-lacp-state": ListOf({
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
        #     xe-3/0/2                  Defaulted   Fast periodic Collecting distributing
        #     xe-3/0/3                  Port disabled   Fast periodic Collecting distributing
        p3 = re.compile(r'^(?P<name>\S+) +(?P<lacp_receive_state>(Current|Defaulted|Port +disabled)) +'
                        r'(?P<lacp_transmit_state>\S+( +\S+)?) +(?P<lacp_mux_state>\S+( +\S+)?)$')

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
            #     xe-3/0/2                  Defaulted   Fast periodic Collecting distributing
            #     xe-3/0/3                  Port disabled   Fast periodic Collecting distributing
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

class ShowLacpStatisticsInterfacesInterfaceSchema(MetaParser):
    """ Schema for:
            * show lacp statistics interfaces {interface}
    """
    """
    schema = {
        Optional("@xmlns:junos"): str,
        "lacp-interface-statistics-list": {
            Optional("@xmlns"): str,
            "lacp-interface-statistics": {
                Optional("@xmlns"): str,
                "lag-lacp-header": {
                    "aggregate-name": str
                },
                "lag-lacp-statistics": [
                    {
                        "illegal-rx-packets": str,
                        "lacp-rx-packets": str,
                        "lacp-tx-packets": str,
                        "name": str,
                        "unknown-rx-packets": str
                    }
                ]
            }
        }
    }
    """

    schema = {
        "lacp-interface-statistics-list": {
            "lacp-interface-statistics": {
                "lag-lacp-header": {
                    "aggregate-name": str
                },
                "lag-lacp-statistics": ListOf({
                    "illegal-rx-packets": str,
                    "lacp-rx-packets": str,
                    "lacp-tx-packets": str,
                    "name": str,
                    "unknown-rx-packets": str,
                }),
            }
        }
    }


class ShowLacpStatisticsInterfacesInterface(ShowLacpStatisticsInterfacesInterfaceSchema):
    """ Parser for:
            * show lacp statistics interfaces {interface}
    """
    cli_command = ['show lacp statistics interfaces {interface}']

    def cli(self, output=None, interface=None):
        if not output:
            out = self.device.execute(self.cli_command[0].format(interface=interface))
        else:
            out = output

        ret_dict = {}

        # Aggregated interface: ae4
        p1 = re.compile(r'^Aggregated +interface: +(?P<aggregate_name>\S+)$')

        #      ge-0/0/6                 286         291            0            0
        p2 = re.compile(r'(?P<name>\S+)\s+(?P<lacp_rx_packets>\d+)\s+(?P<lacp_tx_packets>\d+)\s+(?P<unknown_rx_packets>\d+)\s+(?P<illegal_rx_packets>\d+)')

        for line in out.splitlines():
            line = line.strip()

            # Aggregated interface: ae4
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault("lacp-interface-statistics-list", {})\
                    .setdefault("lacp-interface-statistics", {})\
                        .setdefault("lag-lacp-header", {})\
                            .setdefault("aggregate-name", group['aggregate_name'])
                continue

            #      ge-0/0/6                 286         291            0            0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                entry_list = ret_dict.setdefault("lacp-interface-statistics-list", {})\
                    .setdefault("lacp-interface-statistics", {})\
                        .setdefault("lag-lacp-statistics", [])
                entry = {}
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value
                entry_list.append(entry)
                continue

        return ret_dict
