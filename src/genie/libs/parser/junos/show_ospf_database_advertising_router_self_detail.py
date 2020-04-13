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

    schema = {
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
        p1 = re.compile(r'^OSPF *database, +Area +(?P<ospf_area>[/d/.]+)$')

        # Router  *111.87.5.252     111.87.5.252     0x80001b9e  1801  0x22 0x1e2  120
        p2 = re.compile(r'^(?P<lsa_type>\S+)( *)(?P<lsa_id>\*?[\d\.]+)( +)(?P<advertising_router>\S+)( +)(?P<sequence_number>\S+)( +)(?P<age>\S+)( +)(?P<options>\S+)( +)(?P<checksum>\S+)( +)(?P<lsa_length>\S+)$')

        # bits 0x2, link count 8
        p3 = re.compile(r'^bits +(?P<bits>\S+), +link +count (?P<link_count>\d+)$')

        # id 111.87.5.253, data 111.87.5.93, Type PointToPoint (1)
        p4 = re.compile(r'^id (?P<link_id>[\d\.]+), data (?P<link_data>[\d\.]+), Type (?P<link_type_name>\S+) \((?P<link_type_value>\S+)\)$')

        # Topology count: 0, Default metric: 5
        p5 = re.compile(r'^Topology +count: (?P<ospf_topology_count>\d+), Default metric: (?P<metric>\d+)$')

        # Topology default (ID 0)
        p6 = re.compile(r'^Topology +(?P<ospf_topology_name>\S+) +\(ID +(?P<ospf_topology_id>\S+)\)$')

        # Type: PointToPoint, Node ID: 27.86.198.239
        p7 = re.compile(r'^Type: +(?P<link_type_name>\S+), +Node +ID: +(?P<ospf_lsa_topology_link_node_id>[\d\.]+)$')

        # Metric: 1000, Bidirectional
        p8 = re.compile(r'^Metric: +(?P<link_type_name>\d+), +(?P<link_type_name>\S+)$')

        # RtrAddr (1), length 4:
        p9 =re.compile(r'^(?P<tlv_type_name>\d+) +\((?P<tlv_type_value>\d+)\), +length (?P<link_type_name>\d+):$')

        # 111.87.5.252, 100, 1000Mbps
        p10 = re.compile(r'^(?P<data>\S+)$')

        # Priority 0, 1000Mbps
        p11 = re.compile(r'^Priority \d+, \S+$')

        # Local 336, Remote 0
        p12 = re.compile(r'^Local +\d+, Remote+\d+$')

        ret_dict = {}

        history = []

        for line in out.splitlines():
            line = line.strip()

            # OSPF database, Area 0.0.0.8
            m = p1.match(line)
            if m:
                history.append("p1")
                ospf_area = ret_dict.setdefault("ospf-database-information", {}).setdefault("ospf-area-header", {}).setdefault("ospf-area", None)
                if ospf_area:
                    raise Exception("ospf-area has already been set.")

                group = m.groupdict()
                ret_dict["ospf-database-information"]["ospf-area-header"]["ospf-area"] = group["ospf_area"]
                continue

            # Router  *111.87.5.252     111.87.5.252     0x80001b9e  1801  0x22 0x1e2  120
            m = p2.match(line)
            if m:
                history.append("p2")
                database_list = ret_dict.setdefault("ospf-database-information", {}).setdefault("ospf-database", [])

                group = m.groupdict()
                entry = {}
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value

                if entry['lsa-id'][0] == "*":
                    entry['lsa-id'] = entry['lsa-id'][1:]
                    entry['our-entry'] = True

                database_list.append(entry)
                continue

            # bits 0x2, link count 8
            m = p3.match(line)
            if m:
                history.append("p3")
                last_database = ret_dict["ospf-database-information"]["ospf-database"][-1]

                group = m.groupdict()
                last_database.setdefault("ospf-router-lsa", {})
                last_database["ospf-router-lsa"]["bits"] = group["bits"]
                last_database["ospf-router-lsa"]["link-count"] = group["link_count"]

                database_list.append(entry)
                continue

            # id 111.87.5.253, data 111.87.5.93, Type PointToPoint (1)
            m = p4.match(line)
            if m:
                history.append("p4")
                last_database = ret_dict["ospf-database-information"]["ospf-database"][-1]

                group = m.groupdict()
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
                history.append("p5")
                last_database = ret_dict["ospf-database-information"]["ospf-database"][-1]

                group = m.groupdict()
                ospf_link_list = last_database.setdefault("ospf-router-lsa", {}).setdefault("ospf-link", [])
                last_ospf_link = ospf_link_list[-1]

                group = m.groupdict()
                entry = last_ospf_link
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value

                ospf_link_list.append(entry)
                continue

            # Topology default (ID 0)
            m = p6.match(line)
            if m:
                history.append("p6")
                last_database = ret_dict["ospf-database-information"]["ospf-database"][-1]

                group = m.groupdict()
                ospf_lsa_topology = last_database.setdefault("ospf-lsa-topology", {})

                group = m.groupdict()
                entry = ospf_lsa_topology
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value

                continue

            # Type: PointToPoint, Node ID: 27.86.198.239
            m = p7.match(line)
            if m:
                history.append("p7")
                last_database = ret_dict["ospf-database-information"]["ospf-database"][-1]

                group = m.groupdict()
                ospf_lsa_topology_list = last_database.setdefault("ospf-lsa-topology", {}).setdefault("ospf-lsa-topology-link", [])
                last_ospf_lsa_topology = ospf_lsa_topology_list[-1]

                group = m.groupdict()
                entry = last_ospf_lsa_topology
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value

                ospf_lsa_topology_list.append(entry)
                continue

            # Metric: 1000, Bidirectional
            m = p8.match(line)
            if m:
                history.append("p8")
                last_database = ret_dict["ospf-database-information"]["ospf-database"][-1]

                group = m.groupdict()
                ospf_lsa_topology_list = last_database.setdefault("ospf-lsa-topology", {}).setdefault("ospf-lsa-topology-link", [])
                last_ospf_lsa_topology = ospf_lsa_topology_list[-1]

                group = m.groupdict()
                entry = last_ospf_lsa_topology
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value

                ospf_lsa_topology_list.append(entry)
                continue

            # RtrAddr (1), length 4:
            m = p9.match(line)
            if m:
                history.append("p9")
                last_tlv = line_index
                last_database = ret_dict["ospf-database-information"]["ospf-database"][-1]

                group = m.groupdict()
                tlv_block = last_database.setdefault("ospf-opaque-area-lsa", {})\
                    .setdefault("tlv-block", {})

                if not tlv_block:
                    entry = tlv_block
                    for group_key, group_value in group.items():
                        entry_key = group_key.replace('_','-')
                        entry[entry_key] = group_value
                    tlv_block.setdefault("formatted-tlv-data", "")

                else:
                    last_database.setdefault("ospf-opaque-area-lsa", {}).setdefault("te-subtlv", {}).setdefault("tlv-type-name", []).append(group["tlv_type_name"])
                    last_database.setdefault("ospf-opaque-area-lsa", {}).setdefault("te-subtlv", {}).setdefault("tlv-type-value", []).append(group["tlv_type_value"])
                    last_database.setdefault("ospf-opaque-area-lsa", {}).setdefault("te-subtlv", {}).setdefault("tlv-length", []).append(group["tlv_length"])

                continue

            # word
            m = p10.match(line)
            if m:
                history.append("p10")
                if last_tlv == line_index - 1:
                    last_database = ret_dict["ospf-database-information"]["ospf-database"][-1]

                    group = m.groupdict()
                    te_subtlv = last_database.setdefault("ospf-opaque-area-lsa", {}).setdefault("te-subtlv", {})

                    if not te_subtlv:
                        last_database["ospf-opaque-area-lsa"]["tlv-block"]["formatted-tlv-data"] = group["data"]

                    else:
                        last_database["ospf-opaque-area-lsa"]["te-subtlv"].setdefault("formatted-tlv-data", []).append(group["data"])

                continue

            # Priority 0, 1000Mbps
            m = p11.match(line)
            if m:
                history.append("p11")
                last_database = ret_dict["ospf-database-information"]["ospf-database"][-1]

                group = m.groupdict()
                te_subtlv = last_database.setdefault("ospf-opaque-area-lsa", {}).setdefault("te-subtlv", {})

                if last_tlv == line_index - 1:
                    te_subtlv.setdefault("formatted-tlv-data", []).append(line+ " \n")

                else:
                    te_subtlv["formatted-tlv-data"][-1] += line+ " \n"

                continue

            # Local 336, Remote 0
            m = p12.match(line)
            if m:
                history.append("p12")
                last_database = ret_dict["ospf-database-information"]["ospf-database"][-1]

                group = m.groupdict()
                te_subtlv = last_database.setdefault("ospf-opaque-area-lsa", {}).setdefault("te-subtlv", {})

                te_subtlv.setdefault("formatted-tlv-data", []).append(line)

                continue


        return ret_dict