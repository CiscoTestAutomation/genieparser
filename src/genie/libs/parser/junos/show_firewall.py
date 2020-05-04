""" show_firewall.py

JunOs parsers for the following show commands:
    * show firewall
    * show firewall counter filter v6_local-access-control v6_last_policer
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (Any, 
        Optional, Use, SchemaTypeError, Schema, Or)

class ShowFirewallSchema(MetaParser):

    """ Schema for:
            * show firewall
    """

    """schema = {
    Optional("@xmlns:junos"): str,
    "firewall-information": {
        Optional("@xmlns"): str,
        "filter-information": [
            {
                Optional("counter"): {
                    "byte-count": str,
                    "counter-name": str,
                    "packet-count": str
                },
                "filter-name": str,
                Optional("policer"): {
                    "byte-count": str,
                    "packet-count": str,
                    "policer-name": str
                }
            }
        ]
    }
}"""

    def validate_counter_list(value):
        # Pass firmware list as value
        if not isinstance(value, list):
            raise SchemaTypeError('counter is not a list')
        counter_inner_schema = Schema(
                        {
                            "byte-count": str,
                            "counter-name": str,
                            "packet-count": str
                        
                        }
                    
        )
        # Validate each dictionary in list
        for item in value:
            counter_inner_schema.validate(item)
        return value

    
    def validate_filter_information_list(value):
        if not isinstance(value, list):
            raise SchemaTypeError('filter-information is not a list')
        filter_schema = Schema({
                Optional("counter"): Use(ShowFirewall.validate_counter_list),
                "filter-name": str,
                Optional("policer"): {
                    "byte-count": str,
                    "packet-count": str,
                    "policer-name": str
                }
        })
        for item in value:
            filter_schema.validate(item)
        return value
    schema = {
        Optional("@xmlns:junos"): str,
        "firewall-information": {
            Optional("@xmlns"): str,
            "filter-information": Use(validate_filter_information_list)
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
                filter_name = ""
                if(group["filter_name"] == "catch_all"):
                    filter_information_list = ret_dict.setdefault("firewall-information", {})\
                        .setdefault("filter-information", [])

                if(group["filter_name"] == "__default_bpdu_filter__"):
                    outter_dict = {}
                    outter_dict["filter-name"] = group["filter_name"]
                    filter_information_list.append(outter_dict)

                
                inner_filter_list = []
                outter_filter_dict = {}
                outter_filter_dict["filter-name"] = group["filter_name"]
                filter_name = group["filter_name"]

                continue

            #cflow_counter_v4                              28553344730            151730215
            m = p2.match(line)
            if m:
                group = m.groupdict()
                
                if(filter_name == "catch_all"):
                    inner_filter_dict = {}
                    inner_list = []
                    for group_key, group_value in group.items():
                        entry_key = group_key.replace('_','-')
                        inner_filter_dict[entry_key] = group_value
                    inner_list.append(inner_filter_dict)
                    outter_filter_dict["counter"] = inner_list
                    filter_information_list.append(outter_filter_dict)

                elif(filter_name == "local-access-control"):
                    inner_filter_dict = {}
                    for group_key, group_value in group.items():
                        entry_key = group_key.replace('_','-')
                        inner_filter_dict[entry_key] = group_value
                    inner_filter_list.append(inner_filter_dict)
                    if(group["counter_name"] == "traceroute-udp-deny-count"):
                        outter_filter_dict["counter"] = inner_filter_list
                
                elif(filter_name == "MINIMUM-RATE-POLICER"):
                    policer_dict = {}
                    policer_dict["policer-name"] = group["counter_name"]
                    policer_dict["byte-count"] = group["byte_count"]
                    policer_dict["packet-count"] = group["packet_count"]
                    outter_filter_dict["policer"] = policer_dict

                    filter_information_list.append(outter_filter_dict)

                elif(filter_name == "v4_EXT_inbound"):
                    inner_filter_dict = {}
                    for group_key, group_value in group.items():
                        entry_key = group_key.replace('_','-')
                        inner_filter_dict[entry_key] = group_value
                    inner_filter_list.append(inner_filter_dict)
                    if(group["counter_name"] == "deny-src-in"):
                        outter_filter_dict["counter"] = inner_filter_list
                        filter_information_list.append(outter_filter_dict)

                elif(filter_name == "v4_toIPVPN_inbound"):
                    inner_filter_dict = {}
                    for group_key, group_value in group.items():
                        entry_key = group_key.replace('_','-')
                        inner_filter_dict[entry_key] = group_value
                    inner_filter_list.append(inner_filter_dict)
                    if(group["counter_name"] == "deny-rsvp-in"):
                        outter_filter_dict["counter"] = inner_filter_list
                        filter_information_list.append(outter_filter_dict)

                elif(filter_name == "v6_catch_all"):
                    inner_filter_dict = {}
                    for group_key, group_value in group.items():
                        entry_key = group_key.replace('_','-')
                        inner_filter_dict[entry_key] = group_value
                    inner_filter_list.append(inner_filter_dict)

                    outter_filter_dict["counter"] = inner_filter_list
                    filter_information_list.append(outter_filter_dict)
                    
                elif(filter_name == "v6_local-access-control"):
                    inner_filter_dict = {}
                    for group_key, group_value in group.items():
                        entry_key = group_key.replace('_','-')
                        inner_filter_dict[entry_key] = group_value
                    inner_filter_list.append(inner_filter_dict)
                    if(group["counter_name"] == "v6_last_policer"):
                        outter_filter_dict["counter"] = inner_filter_list

                elif(filter_name == "MINIMUM-RATE-POLICER"):
                    
                    if(prev_filter_name == "v6_local-access-control"):
                        policer_dict = {}
                        policer_dict["policer-name"] = group["counter_name"]
                        policer_dict["byte-count"] = group["byte_count"]
                        policer_dict["packet-count"] = group["packet_count"]
                        outter_filter_dict["policer"] = policer_dict

                        filter_information_list.append(outter_filter_dict)
                
                continue

            #Policers:
            m = p3.match(line)
            if m:
                group = m.groupdict()
                prev_filter_name = filter_name
                filter_name = "MINIMUM-RATE-POLICER"

                continue

        return ret_dict

class ShowFirewallCounterFilterSchema(MetaParser):

    """ Schema for:
            * show firewall counter filter v6_local-access-control v6_last_policer
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
            * show firewall counter filter v6_local-access-control v6_last_policer
    """

    cli_command = 'show firewall counter filter v6_local-access-control v6_last_policer'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
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