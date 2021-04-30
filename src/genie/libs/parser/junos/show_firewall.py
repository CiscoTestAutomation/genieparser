""" show_firewall.py

JunOs parsers for the following show commands:
    * show firewall
    * show firewall counter filter v6_local-access-control v6_last_policer
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from pyats.utils.exceptions import SchemaError
from genie.metaparser.util.schemaengine import (Any,
        Optional, Use, Schema, Or, ListOf)

class ShowFirewallSchema(MetaParser):

    """ Schema for:
            * show firewall

    schema = {
        Optional("@xmlns:junos"): str,
        "firewall-information": {
            Optional("@xmlns"): str,
            "filter-information": ListOf({
                Optional("counter"): ListOf({
                    "byte-count": str,
                    "counter-name": str,
                    "packet-count": str
                }),
                "filter-name": str,
                Optional("policer"): {
                    "byte-count": str,
                    "packet-count": str,
                    "policer-name": str
                }
            })
        }
    }
"""

    schema = {
        Optional("@xmlns:junos"): str,
        "firewall-information": {
            Optional("@xmlns"): str,
            "filter-information": ListOf({
                Optional("counter"): ListOf({
                    "byte-count": str,
                    "counter-name": str,
                    "packet-count": str
                }),
                "filter-name": str,
                Optional("policer"): {
                    "byte-count": str,
                    "packet-count": str,
                    "policer-name": str
                }
            })
        }
    }


class ShowFirewall(ShowFirewallSchema):
    """ Parser for:
            * show firewall
    """

    cli_command = 'show firewall'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Filter: catch_all
        p1 = re.compile(r'^Filter: +(?P<filter_name>\S+)$')

        # cflow_counter_v4                              28553344730            151730215
        p2 = re.compile(r'^(?P<counter_name>\S+) +(?P<byte_count>\d+) +(?P<packet_count>\d+)$')

        # Policers:
        p3 = re.compile(r'^Policers:$')

        # Counters:
        p4 = re.compile(r'^Counters:$')
        
        ret_dict = {}
        pol_coun = None

        for line in out.splitlines():
            line = line.strip()

            # Filter: catch_all
            m = p1.match(line)
            if m:
                group = m.groupdict()
                filter_list = ret_dict.setdefault("firewall-information", {}) \
                    .setdefault("filter-information", [])
                filter_dict = {"filter-name": group['filter_name']}
                filter_list.append(filter_dict)

            # cflow_counter_v4                              28553344730            151730215
            m = p2.match(line)
            if m:
                group = m.groupdict()
                if pol_coun == 'counter':
                    counter_list = filter_dict.setdefault('counter', [])
                    counter_dict = {k.replace('_', '-'):v for k, v in group.items() if v is not None}
                    counter_list.append(counter_dict)
                elif pol_coun == 'policer':
                    policer_dict = filter_dict.setdefault('policer', {})
                    policer_dict.update({"policer-name": group.pop("counter_name")})
                    policer_dict.update({k.replace('_', '-'):v for k, v in group.items() if v is not None})

            # Policers:
            m = p3.match(line)
            if m:
                pol_coun = 'policer'

            # Counters:
            m = p4.match(line)
            if m:
                pol_coun = 'counter'

        return ret_dict

class ShowFirewallCounterFilterSchema(MetaParser):

    """ Schema for:
            * show firewall counter filter {filter} {counter-name}
    """

    schema = {
    Optional("@xmlns:junos"): str,
    "firewall-information": {
        Optional("@xmlns"): str,
        "filter-information": {
            "counter": {
                "byte-count": str,
                "counter-name": str,
                "packet-count": str
            },
            "filter-name": str
            }
        }
    }


class ShowFirewallCounterFilter(ShowFirewallCounterFilterSchema):
    """ Parser for:
            * show firewall counter filter {filter} {counter-name}
            * show firewall counter filter {filter} block
    """
    cli_command = [
        'show firewall counter filter {filter} {counter_name}',
        'show firewall counter filter {filter} block'
        ]

    def cli(self, filter=None, counter_name=None, output=None):
        if not output:
            if filter and not counter_name:
                out = self.device.execute(self.cli_command[1].format(
                    filter=filter
                ))
            else:
                out = self.device.execute(self.cli_command[0].format(filter=filter,
                                                                  counter_name=counter_name))
        else:
            out = output

        #Filter: catch_all
        p1 = re.compile(r'^Filter: +(?P<filter_name>\S+)$')

        #cflow_counter_v4                              28553344730            151730215
        p2 = re.compile(r'^(?P<counter_name>\S+) +(?P<byte_count>\d+) +(?P<packet_count>\d+)$')

        #Policers:
        p3 = re.compile(r'^(?P<filter_name>\APolicers:)$')
        
        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            #Filter: catch_all
            m = p1.match(line)
            if m:
                group = m.groupdict()
                filter_information_list = ret_dict.setdefault("firewall-information", {})\
                    .setdefault("filter-information", {})

                filter_information_list["filter-name"] = group["filter_name"]
                continue

            #v6_last_policer                                1061737740              7860915
            m = p2.match(line)
            if m:
                group = m.groupdict()
                inner_filter_dict = {}
                inner_filter_dict["counter-name"] = group["counter_name"]
                inner_filter_dict["byte-count"] = group["byte_count"]
                inner_filter_dict["packet-count"] = group["packet_count"]

                filter_information_list["counter"] = inner_filter_dict
                
                continue

        return ret_dict


class ShowFirewallLogSchema(MetaParser):

    """ Schema for:
            * show firewall log
    """

    """schema = {
    "firewall-log-information": {
        "log-information": [
            {
                "action-name": str,
                "destination-address": str,
                "filter-name": str,
                "interface-name": str,
                "protocol-name": str,
                "source-address": str,
                "time": str
            }
        ]
    }
}"""

    schema = {
    "firewall-log-information": {
        "log-information": ListOf({
                        "action-name": str,
                        "destination-address": str,
                        "filter-name": str,
                        "interface-name": str,
                        "protocol-name": str,
                        "source-address": str,
                        "time": str
                })
            }
        }


class ShowFirewallLog(ShowFirewallLogSchema):
    """ Parser for:
            * show firewall log
    """
    cli_command = 'show firewall log'

    def cli(self, output=None):

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        #10:28:22  pfe       D      ge-0/0/0.0    TCP             10.70.0.2                         10.70.0.1
        p1 = re.compile(r'^(?P<time>[\d\:]+) +(?P<filter_name>\S+) '
                        r'+(?P<action_name>\S+) +(?P<interface_name>\S+) '
                        r'+(?P<protocol_name>\S+) +(?P<source_address>\S+) '
                        r'+(?P<destination_address>\S+)$')

        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            #10:28:22  pfe       D      ge-0/0/0.0    TCP             10.70.0.2                         10.70.0.1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                log_information_list = ret_dict.setdefault("firewall-log-information", {})\
                    .setdefault("log-information", [])

                entry_dict = {}
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_', '-')
                    entry_dict[entry_key] = group_value
                log_information_list.append(entry_dict)
                continue

        return ret_dict