# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (Any,
        Optional, Use, SchemaTypeError, Schema)

class ShowOspfDatabaseAdvertisingRouterSelfDetailSchema(MetaParser):
    """ Schema for:
            * show ospf database advertising-router self detail
    """

    '''schema = {
        "ospf-database-information": {
            "ospf-area-header": {
                "ospf-area": str
            },
            "ospf-database": [
                {
                    "advertising-router": str,
                    "age": str,
                    "checksum": str,
                    "lsa-id": str,
                    Optional("our-entry"): bool,
                    "lsa-length": str,
                    "lsa-type": str,
                    "options": str,
                    "ospf-router-lsa": {
                        "bits": str,
                        "link-count": str,
                        "ospf-link": [
                            {
                                "link-data": str,
                                "link-id": str,
                                "link-type-name": str,
                                "link-type-value": str,
                                "metric": str,
                                "ospf-topology-count": str
                            }
                        ],
                        "ospf-lsa-topology": {
                            "ospf-lsa-topology-link": [
                                {
                                    "ospf-lsa-topology-link-metric": str,
                                    "ospf-lsa-topology-link-node-id": str,
                                    "ospf-lsa-topology-link-state": str
                                }
                            ],
                            "ospf-topology-id": str,
                            "ospf-topology-name": str
                        }
                    },
                    "sequence-number": str
                }
            ]
        }
    }'''

    def validate_ospf_database(value):
        if not isinstance(value, list):
            raise SchemaTypeError('ospf-database is not a list')

        def validate_ospf_link(value): # not in use
            if not isinstance(value, list):
                raise SchemaTypeError('ospf-link is not a list')
            ospf_link_schema = Schema(
                {
                    "link-data": str,
                    "link-id": str,
                    "link-type-name": str,
                    "link-type-value": str,
                    "metric": str,
                    "ospf-topology-count": str
                })
            for item in value:
                ospf_link_schema.validate(item)
            return value

        def validate_ospf_lsa_topology_link(value):
            if not isinstance(value, list):
                raise SchemaTypeError('ospf-lsa-topology-link is not a list')
            ospf_lsa_topology_ink_schema = Schema(
                {
                    "link-type-name": str,
                    "ospf-lsa-topology-link-metric": str,
                    "ospf-lsa-topology-link-node-id": str,
                    "ospf-lsa-topology-link-state": str
                })
            for item in value:
                ospf_lsa_topology_ink_schema.validate(item)
            return value

        ospf_database_schema = Schema({
                "advertising-router": str,
                "age": str,
                "checksum": str,
                "lsa-id": str,
                Optional("our-entry"): bool,
                "lsa-length": str,
                "lsa-type": str,
                "options": str,
                Optional("ospf-router-lsa"): {
                    "bits": str,
                    "link-count": str,
                    "ospf-link": Use(validate_ospf_link),
                    "ospf-lsa-topology": {
                        "ospf-lsa-topology-link": Use(validate_ospf_lsa_topology_link),
                        "ospf-topology-id": str,
                        "ospf-topology-name": str
                    }
                },
                Optional("ospf-opaque-area-lsa"): {
                    "tlv-block": {
                        "formatted-tlv-data": str,
                        "tlv-length": str,
                        "tlv-type-name": str,
                        "tlv-type-value": str
                    },
                    Optional("te-subtlv"): {
                        "formatted-tlv-data": list,
                        "tlv-length": list,
                        "tlv-type-name": list,
                        "tlv-type-value": list
                    }
                },
                Optional("ospf-external-lsa"): {
                    "address-mask": str,
                    "ospf-external-lsa-topology": {
                        "forward-address": str,
                        "ospf-topology-id": str,
                        "ospf-topology-metric": str,
                        "ospf-topology-name": str,
                        "tag": str,
                        "type-value": str
                    }
                },
                "sequence-number": str
            })
        for item in value:
            ospf_database_schema.validate(item)
        return value

    schema = {
        "ospf-database-information": {
            "ospf-area-header": {
                "ospf-area": str
            },
            "ospf-database": Use(validate_ospf_database)
        }
    }

class ShowOspfDatabaseAdvertisingRouterSelfDetail(ShowOspfDatabaseAdvertisingRouterSelfDetailSchema):
    """ Parser for:
            * show ospf database advertising-router self detail
    """
    cli_command = 'show ospf database advertising-router self detail'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # OSPF database, Area 0.0.0.8
        p1 = re.compile(r'^OSPF +database, +Area +(?P<ospf_area>[\d\.]+)$')

        # Router  *111.87.5.252     111.87.5.252     0x80001b9e  1801  0x22 0x1e2  120
        p2 = re.compile(r'^(?P<lsa_type>[a-zA-Z]+)( *)(?P<lsa_id>\*?\d{1,3}(\.\d{1,3}){3})'
            r'( +)(?P<advertising_router>\S+)( +)(?P<sequence_number>\S+)( +)(?P<age>\S+)'
            r'( +)(?P<options>\S+)( +)(?P<checksum>\S+)( +)(?P<lsa_length>\S+)$')

        # bits 0x2, link count 8
        p3 = re.compile(r'^bits +(?P<bits>\S+), +link +count (?P<link_count>\d+)$')

        # id 111.87.5.253, data 111.87.5.93, Type PointToPoint (1)
        p4 = re.compile(r'^id +(?P<link_id>[\d\.]+), +data +(?P<link_data>[\d\.]+)'
            r', +Type +(?P<link_type_name>\S+) +\((?P<link_type_value>\S+)\)$')

        # Topology count: 0, Default metric: 5
        p5 = re.compile(r'^Topology +count: +(?P<ospf_topology_count>\d+), +Default'
            r' +metric: +(?P<metric>\d+)$')

        # Topology default (ID 0)
        p6 = re.compile(r'^Topology +(?P<ospf_topology_name>\S+) +\(ID +(?P<ospf_topology_id>\S+)\)$')

        # Type: PointToPoint, Node ID: 27.86.198.239
        p7 = re.compile(r'^Type: +(?P<link_type_name>\S+), +Node +ID: +'
            r'(?P<ospf_lsa_topology_link_node_id>[\d\.]+)$')

        # Metric: 1000, Bidirectional
        p8 = re.compile(r'^Metric: +(?P<ospf_lsa_topology_link_metric>\d+), +'
            r'(?P<ospf_lsa_topology_link_state>\S+)$')

        # RtrAddr (1), length 4:
        p9 = re.compile(r'^(?P<tlv_type_name>[\s\S]+) +\((?P<tlv_type_value>\d+)\)'
            r', +length +(?P<tlv_length>\d+):$')

        # 111.87.5.252
        p10 = re.compile(r'^(?P<formatted_tlv_data>\S+)$')

        # Priority 0, 1000Mbps
        p11 = re.compile(r'^Priority (?P<priority_number>\d+), \S+$')

        # Local 336, Remote 0
        p12 = re.compile(r'^(?P<formatted_tlv_data>Local +\d+, +Remote +\d+)$')

        # mask 255.255.255.255
        p13 = re.compile(r'^mask +(?P<address_mask>[\d\.]+)$')

        # Topology default (ID 0)
        p14 = re.compile(r'^Topology +(?P<ospf_topology_name>\S+) +\(ID +(?P<ospf_topology_id>\S+)\)$')

        # Type: 1, Metric: 50, Fwd addr: 0.0.0.0, Tag: 0.0.0.0
        p15 = re.compile(r'^Type: +(?P<type_value>\d+), +Metric: +(?P<ospf_topology_metric>\d+)'
            r', +Fwd +addr: +(?P<forward_address>[\d\.]+), +Tag: +(?P<tag>[\d\.]+)$')


        ret_dict = {}

        self.lsa_type = None

        for line in out.splitlines():
            line = line.strip()

            # # OSPF database, Area 0.0.0.8
            m = p1.match(line)
            if m:
                ospf_area = ret_dict.setdefault("ospf-database-information", {}).setdefault("ospf-area-header", {})

                group = m.groupdict()
                ret_dict["ospf-database-information"]["ospf-area-header"]["ospf-area"] = group["ospf_area"]
                continue

            # # Router  *111.87.5.252     111.87.5.252     0x80001b9e  1801  0x22 0x1e2  120
            m = p2.match(line)
            if m:
                database_list = ret_dict.setdefault("ospf-database-information", {}).setdefault("ospf-database", [])

                group = m.groupdict()
                entry = {}
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value

                if entry['lsa-id'][0] == "*":
                    entry['lsa-id'] = entry['lsa-id'][1:]
                    entry['our-entry'] = True

                self.lsa_type = group['lsa_type']

                database_list.append(entry)
                continue


            if self.lsa_type == "Router":
                 # bits 0x2, link count 8
                m = p3.match(line)
                if m:
                    last_database = ret_dict["ospf-database-information"]["ospf-database"][-1]

                    group = m.groupdict()
                    last_database.setdefault("ospf-router-lsa", {})
                    last_database["ospf-router-lsa"]["bits"] = group["bits"]
                    last_database["ospf-router-lsa"]["link-count"] = group["link_count"]

                    continue

                # id 111.87.5.253, data 111.87.5.93, Type PointToPoint (1)
                m = p4.match(line)
                if m:
                    last_database = ret_dict["ospf-database-information"]["ospf-database"][-1]

                    ospf_link_list = last_database.setdefault("ospf-router-lsa", {}).setdefault("ospf-link", [])

                    group = m.groupdict()
                    entry = {}
                    for group_key, group_value in group.items():
                        entry_key = group_key.replace('_','-')
                        entry[entry_key] = group_value

                    ospf_link_list.append(entry)
                    continue

                # Topology count: 0, Default metric: 5
                m = p5.match(line)
                if m:
                    last_database = ret_dict["ospf-database-information"]["ospf-database"][-1]

                    ospf_link_list = last_database.setdefault("ospf-router-lsa", {}).setdefault("ospf-link", [])
                    last_ospf_link = ospf_link_list[-1]

                    group = m.groupdict()
                    entry = last_ospf_link
                    for group_key, group_value in group.items():
                        entry_key = group_key.replace('_','-')
                        entry[entry_key] = group_value

                    ospf_link_list.append(entry)
                    continue

                # # Topology default (ID 0)
                m = p6.match(line)
                if m:
                    last_database = ret_dict["ospf-database-information"]["ospf-database"][-1]

                    ospf_lsa_topology = last_database.setdefault("ospf-router-lsa", {})\
                        .setdefault("ospf-lsa-topology", {})

                    group = m.groupdict()
                    entry = ospf_lsa_topology
                    for group_key, group_value in group.items():
                        entry_key = group_key.replace('_','-')
                        entry[entry_key] = group_value

                    continue

                # # Type: PointToPoint, Node ID: 27.86.198.239
                m = p7.match(line)
                if m:
                    last_database = ret_dict["ospf-database-information"]["ospf-database"][-1]

                    ospf_lsa_topology_list = last_database.setdefault("ospf-router-lsa", {})\
                        .setdefault("ospf-lsa-topology", {}).setdefault("ospf-lsa-topology-link", [])

                    group = m.groupdict()
                    entry = {}
                    for group_key, group_value in group.items():
                        entry_key = group_key.replace('_','-')
                        entry[entry_key] = group_value

                    ospf_lsa_topology_list.append(entry)
                    continue

                # Metric: 1000, Bidirectional
                m = p8.match(line)
                if m:
                    last_database = ret_dict["ospf-database-information"]["ospf-database"][-1]

                    group = m.groupdict()
                    last_link = last_database["ospf-router-lsa"]["ospf-lsa-topology"]["ospf-lsa-topology-link"][-1]

                    group = m.groupdict()
                    entry = last_link
                    for group_key, group_value in group.items():
                        entry_key = group_key.replace('_','-')
                        entry[entry_key] = group_value

                    continue

            if self.lsa_type == "OpaqArea":
                # RtrAddr (1), length 4:
                m = p9.match(line)
                if m:
                    group = m.groupdict()
                    last_database = ret_dict["ospf-database-information"]["ospf-database"][-1]
                    last_database.setdefault("ospf-opaque-area-lsa", {}).setdefault("tlv-block", {})

                    if "tlv-type-name" not in last_database["ospf-opaque-area-lsa"]["tlv-block"]:
                        entry = last_database["ospf-opaque-area-lsa"]["tlv-block"]
                        for group_key, group_value in group.items():
                            entry_key = group_key.replace('_','-')
                            entry[entry_key] = group_value
                        entry['formatted-tlv-data'] = ""

                    else:
                        last_database.setdefault("ospf-opaque-area-lsa", {})\
                            .setdefault("te-subtlv", {}).setdefault("tlv-type-value",[])\
                                .append(group["tlv_type_value"])

                        last_database.setdefault("ospf-opaque-area-lsa", {})\
                            .setdefault("te-subtlv", {}).setdefault("tlv-type-name",[])\
                                .append(group["tlv_type_name"])

                        last_database.setdefault("ospf-opaque-area-lsa", {})\
                            .setdefault("te-subtlv", {}).setdefault("tlv-length",[])\
                                .append(group["tlv_length"])

                    continue

                # 111.87.5.252
                m = p10.match(line)
                if m:
                    group = m.groupdict()

                    last_database = ret_dict["ospf-database-information"]["ospf-database"][-1]

                    if "te-subtlv" not in last_database["ospf-opaque-area-lsa"]:
                        last_database["ospf-opaque-area-lsa"]["tlv-block"]["formatted-tlv-data"] = group["formatted_tlv_data"]
                    else:
                        last_database.setdefault("ospf-opaque-area-lsa", {})\
                            .setdefault("te-subtlv", {}).setdefault("formatted-tlv-data",[])\
                                .append(group["formatted_tlv_data"])

                # Priority 0, 1000Mbps
                m = p11.match(line)
                if m:
                    group = m.groupdict()

                    line.strip()
                    line += '\n'

                    last_database = ret_dict["ospf-database-information"]["ospf-database"][-1]

                    if group["priority_number"] == "0":

                        last_database.setdefault("ospf-opaque-area-lsa", {})\
                            .setdefault("te-subtlv", {}).setdefault("formatted-tlv-data",[]).append(line)
                    else:

                        last_database["ospf-opaque-area-lsa"]["te-subtlv"]["formatted-tlv-data"][-1] += line

                    continue

                # # Local 336, Remote 0
                m = p12.match(line)
                if m:
                    group = m.groupdict()

                    last_database = ret_dict["ospf-database-information"]["ospf-database"][-1]

                    if "te-subtlv" not in last_database["ospf-opaque-area-lsa"]:
                        last_database["ospf-opaque-area-lsa"]["formatted-tlv-data"] = group["formatted_tlv_data"]
                    else:
                        last_database.setdefault("ospf-opaque-area-lsa", {})\
                            .setdefault("te-subtlv", {}).setdefault("formatted-tlv-data",[])\
                                .append(group["formatted_tlv_data"])

                    continue

            if self.lsa_type == "Extern":

                m = p13.match(line)
                if m:
                    group = m.groupdict()

                    last_database = ret_dict["ospf-database-information"]["ospf-database"][-1]
                    last_database.setdefault("ospf-external-lsa", {})\
                        .setdefault("address-mask", group['address_mask'])
                    continue

                m = p14.match(line)
                if m:
                    group = m.groupdict()

                    last_database = ret_dict["ospf-database-information"]["ospf-database"][-1]

                    last_database.setdefault("ospf-external-lsa", {})\
                        .setdefault("ospf-external-lsa-topology", {})\
                            .setdefault("ospf-topology-name", group["ospf_topology_name"])

                    last_database.setdefault("ospf-external-lsa", {})\
                        .setdefault("ospf-external-lsa-topology", {})\
                            .setdefault("ospf-topology-id", group["ospf_topology_id"])

                    continue

                m = p15.match(line)
                if m:
                    group = m.groupdict()

                    last_database.setdefault("ospf-external-lsa", {})\
                        .setdefault("ospf-external-lsa-topology", {})\
                            .setdefault("type-value", group["type_value"])
                    last_database.setdefault("ospf-external-lsa", {})\
                        .setdefault("ospf-external-lsa-topology", {})\
                            .setdefault("ospf-topology-metric", group["ospf_topology_metric"])

                    last_database.setdefault("ospf-external-lsa", {})\
                        .setdefault("ospf-external-lsa-topology", {})\
                            .setdefault("forward-address", group["forward_address"])

                    last_database.setdefault("ospf-external-lsa", {})\
                        .setdefault("ospf-external-lsa-topology", {})\
                            .setdefault("tag", group["tag"])

                    continue


        return ret_dict