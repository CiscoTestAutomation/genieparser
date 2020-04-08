
''' show_ospf3.py

Parser for the following show commands:
    * show ospf3 interface
    * show ospf3 database
'''
import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (Any,
        Optional, Use, SchemaTypeError, Schema)

class ShowOspf3InterfaceSchema(MetaParser):

    '''schema = {
    "ospf3-interface-information": {
        "ospf3-interface": [
            {
                "bdr-id": str,
                "dr-id": str,
                "interface-name": str,
                "neighbor-count": str,
                "ospf-area": str,
                "ospf-interface-state": str
            }
        ]
    }'''

    # Sub Schema
    def validate_ospf3_interface_list(value):
        # Pass ospf3-interface list as value
        if not isinstance(value, list):
            raise SchemaTypeError('ospf-interface is not a list')
        ospf3_interface_schema = Schema({
                "bdr-id": str,
                "dr-id": str,
                "interface-name": str,
                "neighbor-count": str,
                "ospf-area": str,
                "ospf-interface-state": str
            })
        # Validate each dictionary in list
        for item in value:
            ospf3_interface_schema.validate(item)
        return value

    # Main Schema
    schema = {
        "ospf3-interface-information": {
            "ospf3-interface": Use(validate_ospf3_interface_list)
        }
    }

class ShowOspf3Interface(ShowOspf3InterfaceSchema):
    """ Parser for:
    * show ospf3 interface
    """
    cli_command = 'show ospf3 interface'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # ge-0/0/0.0          PtToPt  0.0.0.8         0.0.0.0         0.0.0.0            1
        p1 = re.compile(r'^(?P<interface_name>\S+) +(?P<ospf_interface_state>\S+)'
            r' +(?P<ospf_area>[0-9]{1,3}(\.[0-9]{1,3}){3}) +(?P<dr_id>[0-9]{1,3}'
            r'(\.[0-9]{1,3}){3}) +(?P<bdr_id>[0-9]{1,3}(\.[0-9]{1,3}){3}) +(?P<neighbor_count>\S+)$')

        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # ge-0/0/0.0          PtToPt  0.0.0.8         0.0.0.0         0.0.0.0            1
            m = p1.match(line)
            if m:

                entry_list = ret_dict.setdefault("ospf3-interface-information", {})\
                    .setdefault("ospf3-interface", [])

                group = m.groupdict()
                entry = {}
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value

                entry_list.append(entry)
                continue

        return ret_dict

class ShowOspf3DatabaseSchema(MetaParser):
    '''
    schema = {
        "ospf3-database-information": {
            "ospf3-area-header": {
                "ospf-area": str
            },
            "ospf3-database": [
                {
                    "advertising-router": str,
                    "age": str,
                    "checksum": str,
                    "lsa-id": str,
                    "lsa-length": str,
                    "lsa-type": str,
                    "sequence-number": str,
                    Optional('our-entry'): None
                }
            ],
            "ospf3-intf-header": [
                {
                    "ospf-intf": str
                }
            ]
        }
    }
    '''

    # Sub Schema ospf3-database
    def validate_ospf3_database_list(value):
        # Pass ospf3-database list as value
        if not isinstance(value, list):
            raise SchemaTypeError('ospf3-database is not a list')
        ospf3_database_schema = Schema({
                "advertising-router": str,
                "age": str,
                "checksum": str,
                "lsa-id": str,
                "lsa-length": str,
                "lsa-type": str,
                "sequence-number": str,
                Optional('our-entry'): None
            })
        # Validate each dictionary in list
        for item in value:
            ospf3_database_schema.validate(item)
        return value

    # Sub Schema ospf3-intf-header
    def validate_ospf3_intf_header_list(value):
        # Pass ospf3-intf-header list as value
        if not isinstance(value, list):
            raise SchemaTypeError('ospf3-intf-header is not a list')
        ospf3_intf_header_schema = Schema({
                "ospf-area": str,
                "ospf-intf": str
            })
        # Validate each dictionary in list
        for item in value:
            ospf3_intf_header_schema.validate(item)
        return value

    # Main Schema
    schema = {
        "ospf3-database-information": {
            "ospf3-area-header": {
                "ospf-area": str
            },
            "ospf3-database": Use(validate_ospf3_database_list),
            "ospf3-intf-header": Use(validate_ospf3_intf_header_list),
        }
    }

class ShowOspf3Database(ShowOspf3DatabaseSchema):
    """ Parser for:
    * show ospf3 database
    """
    cli_command = 'show ospf3 database'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        #    OSPF3 database, Area 0.0.0.8
        p1 = re.compile(r'^OSPF3( +)database,( +)Area( +)'
            r'(?P<ospf_area>(\*{0,1})[0-9]{1,3}(\.[0-9]{1,3}){3})$')

        # Type       ID               Adv Rtr           Seq         Age  Cksum  Len
        # Router      0.0.0.0          10.34.2.250     0x800018ed  2407  0xaf2d  56
        p2 = re.compile(r'^(?P<lsa_type>\S+) +(?P<lsa_id>(\*{0,1})[0-9]{1,3}'
            r'(\.[0-9]{1,3}){3}) +(?P<advertising_router>[0-9]{1,3}(\.[0-9]{1,3})'
            r'{3}) +(?P<sequence_number>\S+) +(?P<age>\d+) +(?P<checksum>\S+) +(?P<lsa_length>\d+)$')

        # OSPF3 Link-Local database, interface ge-0/0/0.0 Area 0.0.0.8
        p3 = re.compile(r'^OSPF3( +)Link-Local( +)database,( +)interface( +)'
            r'(?P<ospf_intf>\S+)( +)Area( +)(?P<ospf_area>[0-9]{1,3}(\.[0-9]{1,3}){3})$')

        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # ge-0/0/0.0          PtToPt  0.0.0.8         0.0.0.0         0.0.0.0            1
            m = p1.match(line)
            if m:
                ospf_area = ret_dict.setdefault("ospf3-database-information", {})\
                    .setdefault("ospf3-area-header", {}).setdefault("ospf-area", None)
                if ospf_area:
                    raise Exception("ospf-area already exists"+str(ospf_area))

                group = m.groupdict()

                ret_dict["ospf3-database-information"]["ospf3-area-header"]["ospf-area"]\
                     = group["ospf_area"]
                continue

            # Router      0.0.0.0          10.34.2.250     0x800018ed  2407  0xaf2d  56
            m = p2.match(line)
            if m:
                entry_list = ret_dict.setdefault("ospf3-database-information", {})\
                    .setdefault("ospf3-database", [])

                group = m.groupdict()
                entry = {}
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value

                lsa_id = entry['lsa-id']
                if lsa_id[0] == '*':
                    entry['lsa-id'] = lsa_id[1:]
                    entry['our-entry'] = None

                entry_list.append(entry)
                continue

            # OSPF3 Link-Local database, interface ge-0/0/0.0 Area 0.0.0.8
            m = p3.match(line)
            if m:
                entry_list = ret_dict.setdefault("ospf3-database-information", {})\
                    .setdefault("ospf3-intf-header", [])

                group = m.groupdict()
                entry = {}
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value

                entry_list.append(entry)
                continue

        return ret_dict

class ShowOspf3DatabaseExtensiveSchema(MetaParser):
    '''
    schema = {
        "ospf3-database-information": {
            "ospf3-area-header": {
                "ospf-area": str
            },
            "ospf3-database": [
                {
                    "advertising-router": str,
                    "age": str,
                    "checksum": str,
                    "lsa-id": str,
                    "lsa-length": str,
                    "lsa-type": str,
                    "ospf-database-extensive": {
                        "aging-timer": {
                            "#text": str
                        },
                        "expiration-time": {},
                        "installation-time": {},
                        "lsa-change-count": str,
                        "lsa-changed-time": {},
                        "send-time": {}
                    },
                    "ospf3-intra-area-prefix-lsa" : {
                        "reference-lsa-type": str,
                        "reference-lsa-id": str,
                        "reference-lsa-router-id": str,
                        "prefix-count": str,
                        "ospf3-prefix": [],
                        "ospf3-prefix-options": [],
                        "ospf3-prefix-metric": []
                    },
                    "ospf3-router-lsa": {
                        "bits": str,
                        "ospf3-options": str,
                        "ospf3-link": [
                            {
                                "link-intf-id": str,
                                "link-metric": str,
                                "link-type-name": str,
                                "link-type-value": str,
                                "nbr-intf-id": str,
                                "nbr-rtr-id": str
                            }
                        ],
                        "ospf3-lsa-topology": {
                            "ospf-topology-id": str,
                            "ospf-topology-name": str,
                            "ospf3-lsa-topology-link": [
                                {
                                    "ospf-lsa-topology-link-metric": str,
                                    "ospf-lsa-topology-link-node-id": str,
                                    "ospf-lsa-topology-link-state": str
                                }
                            ]
                        },
                        "ospf3-options": str
                    },
                    "sequence-number": str
                    Optional("ospf3-link-lsa"): {
                        "linklocal-address": str,
                        "ospf3-options": str,
                        Optional("ospf3-prefix"): str,
                        Optional("ospf3-prefix-options"): str,
                        "prefix-count": str,
                        "router-priority": str
                    }
                }
            ],
            "ospf3-intf-header": [
                {
                    "ospf-intf": str
                }
            ]
        }
    }
    '''
    # Sub Schema ospf3-link
    def validate_ospf3_link_list(value):
        if not isinstance(value, list):
            raise SchemaTypeError('ospf3-link is not a list')
        ospf3_link_schema = Schema({
                "link-intf-id": str,
                "link-metric": str,
                "link-type-name": str,
                "link-type-value": str,
                "nbr-intf-id": str,
                "nbr-rtr-id": str
            })
        # Validate each dictionary in list
        for item in value:
            ospf3_link_schema.validate(item)
        return value

    # Sub Schema ospf3-lsa-topology-link
    def validate_ospf3_lsa_topology_link_list(value):
        if not isinstance(value, list):
            raise SchemaTypeError('ospf3-lsa-topology-link is not a list')
        ospf3_lsa_topology_link_schema = Schema({
                "link-type-name": str,
                "ospf-lsa-topology-link-metric": str,
                "ospf-lsa-topology-link-node-id": str,
                "ospf-lsa-topology-link-state": str
            })
        # Validate each dictionary in list
        for item in value:
            ospf3_lsa_topology_link_schema.validate(item)
        return value

    # Sub Schema ospf3-database
    def validate_ospf3_database_list(value):
        if not isinstance(value, list):
            raise SchemaTypeError('ospf3-database is not a list')
        ospf3_database_schema = Schema({
                "advertising-router": str,
                "age": str,
                "checksum": str,
                "lsa-id": str,
                Optional("our-entry"): None,
                "lsa-length": str,
                "lsa-type": str,
                "sequence-number": str,
                Optional("ospf-database-extensive"): {
                    "aging-timer": {
                        "#text": str
                    },
                    "expiration-time": {
                        "#text": str
                    },
                    "installation-time": {
                        "#text": str
                    },
                    Optional("generation-timer"): {
                        "#text": str
                    },
                    "lsa-change-count": str,
                    "lsa-changed-time": {
                        "#text": str
                    },
                    Optional("send-time"): {
                        "#text": str
                    },
                    Optional("database-entry-state"): str
                },
                Optional("ospf3-intra-area-prefix-lsa"): {
                    "prefix-count": str,
                    "reference-lsa-id": str,
                    "reference-lsa-router-id": str,
                    "reference-lsa-type": str,
                    "ospf3-prefix": list,
                    "ospf3-prefix-metric": list,
                    "ospf3-prefix-options": list,
                },
                Optional("ospf3-router-lsa"): {
                    "bits": str,
                    "ospf3-options": str,
                    "ospf3-link": Use(ShowOspf3DatabaseExtensive.validate_ospf3_link_list),
                    "ospf3-lsa-topology": {
                        "ospf-topology-id": str,
                        "ospf-topology-name": str,
                        "ospf3-lsa-topology-link": Use(ShowOspf3DatabaseExtensive.validate_ospf3_lsa_topology_link_list)
                    }
                },
                Optional("ospf3-link-lsa"): {
                    "linklocal-address": str,
                    "ospf3-options": str,
                    Optional("ospf3-prefix"): str,
                    Optional("ospf3-prefix-options"): str,
                    "prefix-count": str,
                    "router-priority": str
                },
                Optional("ospf3-external-lsa"): {
                    Optional("metric"): str,
                    Optional("ospf3-prefix"): str,
                    Optional("ospf3-prefix-options"): str,
                    Optional("type-value"): str
                }
            })
        # Validate each dictionary in list
        for item in value:
            ospf3_database_schema.validate(item)
        return value

    # Sub Schema ospf3-intf-header
    def validate_ospf3_intf_header_list(value):
        if not isinstance(value, list):
            raise SchemaTypeError('ospf3-intf-header is not a list')
        ospf3_link_schema = Schema({
                "ospf-area": str,
                "ospf-intf": str
            })
        # Validate each dictionary in list
        for item in value:
            ospf3_link_schema.validate(item)
        return value

    schema = {
        "ospf3-database-information": {
            "ospf3-area-header": {
                "ospf-area": str
            },
            "ospf3-database": Use(validate_ospf3_database_list),
            "ospf3-intf-header": Use(validate_ospf3_intf_header_list)
        }
    }
class ShowOspf3DatabaseExtensive(ShowOspf3DatabaseExtensiveSchema):
    """ Parser for:
    * show ospf3 database extensive
    """
    cli_command = 'show ospf3 database extensive'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        self.state = None

        #    OSPF3 database, Area 0.0.0.8
        p1 = re.compile(r'^OSPF3( +)database,( +)Area( +)'
                r'(?P<ospf_area>[0-9]{1,3}(\.[0-9]{1,3}){3})$')

        # Type       ID               Adv Rtr           Seq         Age  Cksum  Len
            # Router      0.0.0.0          10.34.2.250     0x800018ed  2407  0xaf2d  56
        p2 = re.compile(r'^(?P<lsa_type>\S+) +(?P<lsa_id>(\*{0,1})[0-9]{1,3}'
            r'(\.[0-9]{1,3}){3}) +(?P<advertising_router>[0-9]{1,3}(\.[0-9]{1,3})'
            r'{3}) +(?P<sequence_number>\S+) +(?P<age>\d+) +(?P<checksum>\S+) +(?P<lsa_length>\d+)$')

        # bits 0x2, Options 0x33
        p3 = re.compile(r'^bits +(?P<bits>\S+), +Options +(?P<ospf3_options>\S+)$')

        #  Type: PointToPoint, Node ID: 106.187.14.240, Metric: 100, Bidirectional
        p4 = re.compile(r'^Type: (?P<link_type_name>\S+), Node ID: (?P<ospf_lsa_topology_link_node_id>[0-9]{1,3}(\.[0-9]{1,3}){3}), Metric: (?P<ospf_lsa_topology_link_metric>\d+), (?P<ospf_lsa_topology_link_state>\S+)$')

        # Aging timer 00:18:16
        p5 = re.compile(r'^Aging timer +(?P<aging_timer>(\S+ ){0,1}\d\d:\d\d:\d\d)$')

        # Installed 00:10:20 ago, expires in 00:49:31, sent 00:10:18 ago
        p6 = re.compile(r'^Installed (?P<installation_time>(\S+ ){0,1}\d\d:\d\d:\d\d) ago, expires in (?P<expiration_time>(\S+ ){0,1}\d\d:\d\d:\d\d), sent (?P<send_time>(\S+ ){0,1}\d\d:\d\d:\d\d) ago$')

        # Last changed 2w6d 04:50:31 ago, Change count: 196
        p7 = re.compile(r'^Last changed (?P<lsa_changed_time>(\S+ ){0,1}\d\d:\d\d:\d\d) ago, Change count: (?P<lsa_change_count>\d+)$')

        # Ref-lsa-type Router, Ref-lsa-id 0.0.0.0, Ref-router-id 59.128.2.250
        p8 = re.compile(r'^Ref-lsa-type (?P<reference_lsa_type>\S+), Ref-lsa-id (?P<reference_lsa_id>[0-9]{1,3}(\.[0-9]{1,3}){3}), Ref-router-id (?P<reference_lsa_router_id>[0-9]{1,3}(\.[0-9]{1,3}){3})$')

        # Prefix-count 3
        p9 = re.compile(r'^Prefix-count (?P<prefix_count>\d+)$')

        # Prefix 2001:268:fb80:3e::/64
        p10 = re.compile(r'^Prefix (?P<ospf3_prefix>\S+)$')

        # Prefix-options 0x0, Metric 5
        p11 = re.compile(r'^Prefix-options (?P<ospf3_prefix_options>\S+), Metric (?P<metric>\d+)$')

        # fe80::250:56ff:fe8d:a96c
        p12 = re.compile(r'^(?P<linklocal_address>\S{4}::\S{3}:\S{4}:\S{4}:\S{4})$')

        # Gen timer 00:49:49
        p13 = re.compile(r'^Gen timer (?P<generation_timer>\S+)$')

        # OSPF3 Link-Local database, interface ge-0/0/0.0 Area 0.0.0.8
        p14 = re.compile(r'^OSPF3 Link-Local database, interface (?P<ospf_intf>\S+) Area (?P<ospf_area>\S+)$')

        # Type PointToPoint (1), Metric 5
        p15 = re.compile(r'^Type (?P<link_type_name>\S+) \((?P<link_type_value>\S+)\), Metric (?P<link_metric>\S+)$')

        # Loc-If-Id 2, Nbr-If-Id 2, Nbr-Rtr-Id 111.87.5.253
        p16 = re.compile(r'^Loc-If-Id (?P<link_intf_id>\S+), Nbr-If-Id (?P<nbr_intf_id>\S+), Nbr-Rtr-Id (?P<nbr_rtr_id>\S+)$')

        # Options 0x33, Priority 128
        p17 = re.compile(r'^Options (?P<ospf3_options>\S+), Priority (?P<router_priority>\S+)$')

        #   Prefix-options 0x0, Metric 50, Type 1,
        p18 = re.compile(r'^Prefix-options (?P<ospf3_prefix_options>\S+), Metric (?P<metric>\S+), Type (?P<type_value>\S+),$')

        # Last changed 29w5d 21:40:56 ago, Change count: 1, Ours
        p19 = re.compile(r'^Last changed (?P<lsa_changed_time>(\S+ ){0,1}\d\d:\d\d:\d\d) ago, Change count: (?P<lsa_change_count>\d+), (?P<database_entry_state>\S+)$')

        # Installed 00:41:50 ago, expires in 00:18:10
        p20 = re.compile(r'^Installed (?P<installation_time>(\S+ ){0,1}\d\d:\d\d:\d\d) ago, expires in (?P<expiration_time>(\S+ ){0,1}\d\d:\d\d:\d\d)$')

        # Prefix 2001:268:fb8f:1f::/64 Prefix-options 0x0
        p21 = re.compile(r'^Prefix (?P<ospf3_prefix>\S+) Prefix-options (?P<ospf3_prefix_options>\S+)$')

        for line in out.splitlines():
            line = line.strip()

            #    OSPF3 database, Area 0.0.0.8
            m = p1.match(line)
            if m:

                ospf_area = ret_dict.setdefault("ospf3-database-information", {})\
                    .setdefault("ospf3-area-header", {}).setdefault("ospf-area", None)
                if ospf_area:
                    raise Exception("ospf-area already exists"+str(ospf_area))

                group = m.groupdict()

                ret_dict["ospf3-database-information"]["ospf3-area-header"]["ospf-area"]\
                     = group["ospf_area"]
                continue

            # Router      0.0.0.0          59.128.2.250     0x800018ed  2504  0xaf2d  56
            m = p2.match(line)
            if m:
                entry_list = ret_dict.setdefault("ospf3-database-information", {})\
                    .setdefault("ospf3-database", [])

                group = m.groupdict()
                entry = {}
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value

                if entry['lsa-id'][0] == "*":
                    entry['lsa-id'] = entry['lsa-id'][1:]
                    entry['our-entry'] = None

                self.state = group['lsa_type']

                entry_list.append(entry)
                continue

            # bits 0x2, Options 0x33
            m = p3.match(line)
            if m:
                last_database = ret_dict["ospf3-database-information"]["ospf3-database"][-1]

                last_database.setdefault("ospf3-router-lsa", {})

                group = m.groupdict()
                entry = {}
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    last_database["ospf3-router-lsa"][entry_key] = group_value

                continue

            #  Type: PointToPoint, Node ID: 106.187.14.240, Metric: 100, Bidirectional
            m = p4.match(line)
            if m:
                last_database = ret_dict["ospf3-database-information"]["ospf3-database"][-1]

                last_database.setdefault("ospf3-router-lsa", {}).setdefault("ospf3-lsa-topology", {}).setdefault("ospf-topology-id", "0")
                last_database.setdefault("ospf3-router-lsa", {}).setdefault("ospf3-lsa-topology", {}).setdefault("ospf-topology-name", "default")

                link_list = last_database.setdefault("ospf3-router-lsa", {}).setdefault("ospf3-lsa-topology", {}).setdefault("ospf3-lsa-topology-link", [])

                group = m.groupdict()
                entry = {}
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value

                link_list.append(entry)
                continue

            # Aging timer 00:18:16
            m = p5.match(line)
            if m:
                last_entry = ret_dict["ospf3-database-information"]["ospf3-database"][-1]
                last_entry.setdefault("ospf-database-extensive", {}).setdefault("aging-timer", {})

                group = m.groupdict()
                last_entry["ospf-database-extensive"]["aging-timer"]["#text"] = group['aging_timer']

                continue

            # Installed 00:10:20 ago, expires in 00:49:31, sent 00:10:18 ago
            m = p6.match(line)
            if m:
                last_entry = ret_dict["ospf3-database-information"]["ospf3-database"][-1]

                last_entry.setdefault("ospf-database-extensive", {}).setdefault("expiration-time", {})
                last_entry.setdefault("ospf-database-extensive", {}).setdefault("installation-time", {})
                last_entry.setdefault("ospf-database-extensive", {}).setdefault("send-time", {})

                group = m.groupdict()
                last_entry["ospf-database-extensive"]["expiration-time"]["#text"] = group['expiration_time']
                last_entry["ospf-database-extensive"]["installation-time"]["#text"] = group['installation_time']
                last_entry["ospf-database-extensive"]["send-time"]["#text"] = group['send_time']

                continue

            # Last changed 2w6d 04:50:31 ago, Change count: 196
            m = p7.match(line) # lsa_changed_time , lsa_changed_count
            if m:
                last_entry = ret_dict["ospf3-database-information"]["ospf3-database"][-1]

                last_entry.setdefault("ospf-database-extensive", {}).setdefault("lsa-changed-time", {})

                group = m.groupdict()
                last_entry["ospf-database-extensive"]["lsa-changed-time"]["#text"] = group['lsa_changed_time']
                last_entry["ospf-database-extensive"]["lsa-change-count"] = group['lsa_change_count']

                continue

            # Ref-lsa-type Router, Ref-lsa-id 0.0.0.0, Ref-router-id 59.128.2.250
            m = p8.match(line)
            if m:
                last_entry = ret_dict["ospf3-database-information"]["ospf3-database"][-1]

                entry = last_entry.setdefault("ospf3-intra-area-prefix-lsa", {})

                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value

                continue

            # Prefix-count 3
            m = p9.match(line)
            if m:
                last_entry = ret_dict["ospf3-database-information"]["ospf3-database"][-1]

                if self.state == 'IntraArPfx':
                    entry = last_entry.setdefault("ospf3-intra-area-prefix-lsa", {})
                elif self.state == 'Link':
                    entry = last_entry.setdefault("ospf3-link-lsa", {})

                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value

                continue

            # Prefix 2001:268:fb80:3e::/64
            m = p10.match(line)
            if m:
                last_database = ret_dict["ospf3-database-information"]["ospf3-database"][-1]

                group = m.groupdict()

                if self.state == 'IntraArPfx':
                    entry_list = last_database.setdefault("ospf3-intra-area-prefix-lsa", {}).setdefault("ospf3-prefix", [])
                    entry_list.append(group['ospf3_prefix'])

                elif self.state == 'Extern':
                    entry = last_database.setdefault("ospf3-external-lsa", {})
                    entry['ospf3-prefix'] = group['ospf3_prefix']
                else:
                    raise "state error"

                continue

            # Prefix-options 0x0, Metric 5
            m = p11.match(line) # p11 = re.compile(r'^Prefix-options (?P<ospf3_prefix_options>\S+), Metric (?P<metric>\d+)$')
            if m:
                last_entry = ret_dict["ospf3-database-information"]["ospf3-database"][-1]

                group = m.groupdict()

                entry = last_entry.setdefault("ospf3-intra-area-prefix-lsa", {})
                entry.setdefault('ospf3-prefix-options', []).append(group['ospf3_prefix_options'])
                entry.setdefault('ospf3-prefix-metric', []).append(group['metric'])

                continue

            # fe80::250:56ff:fe8d:a96c
            m = p12.match(line)
            if m:
                last_entry = ret_dict["ospf3-database-information"]["ospf3-database"][-1]

                entry = last_entry.setdefault("ospf3-link-lsa", {})

                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value

                continue

            # Gen timer 00:49:49
            m = p13.match(line)
            if m:
                last_entry = ret_dict["ospf3-database-information"]["ospf3-database"][-1]

                last_entry.setdefault("ospf-database-extensive", {}).setdefault("generation-timer", {})

                group = m.groupdict()
                last_entry["ospf-database-extensive"]["generation-timer"]["#text"] = group['generation_timer']

                continue

            # OSPF3 Link-Local database, interface ge-0/0/0.0 Area 0.0.0.8
            m = p14.match(line)
            if m:
                entry_list = ret_dict.setdefault("ospf3-database-information", {}).setdefault("ospf3-intf-header", [])

                group = m.groupdict()
                entry = {}
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value

                entry_list.append(entry)

                continue

            # Type PointToPoint (1), Metric 5
            m = p15.match(line)
            if m:
                last_database = ret_dict["ospf3-database-information"]["ospf3-database"][-1]

                ospf3_link_list = last_database.setdefault("ospf3-router-lsa", {}).setdefault("ospf3-link", [])

                group = m.groupdict()
                entry = {}
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value

                ospf3_link_list.append(entry)

                continue

            # Loc-If-Id 2, Nbr-If-Id 2, Nbr-Rtr-Id 111.87.5.253
            m = p16.match(line)
            if m:
                last_database = ret_dict["ospf3-database-information"]["ospf3-database"][-1]

                last_ospf3_link = last_database["ospf3-router-lsa"]["ospf3-link"][-1]

                group = m.groupdict()
                entry = last_ospf3_link
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value

                continue

            # Options 0x33, Priority 128
            m = p17.match(line) # ospf3-options
            if m:
                last_database = ret_dict["ospf3-database-information"]["ospf3-database"][-1]

                group = m.groupdict()
                entry = last_database["ospf3-link-lsa"]
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value

                continue

            #   Prefix-options 0x0, Metric 50, Type 1,
            m = p18.match(line)
            if m:
                last_database = ret_dict["ospf3-database-information"]["ospf3-database"][-1]

                group = m.groupdict()
                entry = last_entry.setdefault("ospf3-external-lsa", {})
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value

                continue

            # Last changed 29w5d 21:40:56 ago, Change count: 1, Ours
            m = p19.match(line) # lsa_changed_time , lsa_changed_count
            if m:
                last_entry = ret_dict["ospf3-database-information"]["ospf3-database"][-1]

                last_entry.setdefault("ospf-database-extensive", {}).setdefault("lsa-changed-time", {})

                group = m.groupdict() # database_entry_state
                last_entry["ospf-database-extensive"]["lsa-changed-time"]["#text"] = group['lsa_changed_time']
                last_entry["ospf-database-extensive"]["lsa-change-count"] = group['lsa_change_count']
                last_entry["ospf-database-extensive"]["database-entry-state"] = group['database_entry_state']

                continue

            # Installed 00:41:50 ago, expires in 00:18:10
            m = p20.match(line)
            if m:
                last_entry = ret_dict["ospf3-database-information"]["ospf3-database"][-1]

                last_entry.setdefault("ospf-database-extensive", {}).setdefault("expiration-time", {})
                last_entry.setdefault("ospf-database-extensive", {}).setdefault("installation-time", {})

                group = m.groupdict()
                last_entry["ospf-database-extensive"]["expiration-time"]["#text"] = group['expiration_time']
                last_entry["ospf-database-extensive"]["installation-time"]["#text"] = group['installation_time']

                continue

            # Prefix 2001:268:fb8f:1f::/64 Prefix-options 0x0
            m = p21.match(line)
            if m:
                last_entry = ret_dict["ospf3-database-information"]["ospf3-database"][-1]

                entry = last_entry.setdefault("ospf3-link-lsa", {})

                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value

                continue

        # print("here")
        # print()
        # print(ret_dict)
        # print()
        return ret_dict