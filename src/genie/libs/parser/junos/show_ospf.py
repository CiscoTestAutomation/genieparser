""" show_ospf.py

JunOs parsers for the following show commands:
    * show ospf interface brief
    * show ospf interface {interface} brief
    * show ospf interface brief instance {instance}
    * show ospf interface
    * show ospf interface {interface}
    * show ospf interface detail
    * show ospf interface {interface} detail
    * show ospf interface instance {instance}
    * show ospf interface detail instance {instance}
    * show ospf interface {interface} detail instance {instance}
    * show ospf database advertising-router self detail
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (Any,
        Optional, Use, SchemaTypeError, Schema)

class ShowOspfInterfaceBriefSchema(MetaParser):
    """ Schema for:
            * show ospf interface brief
            * show ospf interface brief instance {instance}
            * show ospf interface {interface} brief
            * show ospf interface
            * show ospf interface instance {instance}
            * show ospf interface {interface}
    """

    schema = {
        'instance': {
            Any(): {
                'areas': {
                    Any(): {
                        'interfaces': {
                            Any(): {
                                'state': str,
                                'dr_id': str,
                                'bdr_id': str,
                                'nbrs_count': int,
                            }
                        }
                    }
                }
            }
        }
    }


class ShowOspfInterfaceBrief(ShowOspfInterfaceBriefSchema):
    """ Parser for:
            * show ospf interface brief
            * show ospf interface brief instance {instance}
            * show ospf interface {interface} brief
    """

    cli_command = [
        'show ospf interface {interface} brief',
        'show ospf interface brief',
        'show ospf interface brief instance {instance}'
    ]

    def cli(self, interface=None, instance=None, output=None):
        if output is None:
            if instance:
                out = self.device.execute(self.cli_command[2].format(instance=instance))
            elif interface:
                out = self.device.execute(self.cli_command[0].format(interface=interface))
            else:
                out = self.device.execute(self.cli_command[1])
        else:
            out = output

        # Init vars
        ret_dict = {}
        instance = instance if instance else 'master'

        # ge-0/0/2.0    BDR    0.0.0.1    10.16.2.2    10.64.4.4     5
        p1 = re.compile(r'^(?P<interface>\S+) +(?P<state>\S+) '
            '+(?P<area>\S+) +(?P<dr_id>\S+) +(?P<bdr_id>\S+) +(?P<nbrs_count>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            # ge-0/0/2.0    BDR    0.0.0.1    10.16.2.2    10.64.4.4     5
            m = p1.match(line)
            if m:
                group = m.groupdict()
                area = group['area']
                intf_dict = ret_dict.setdefault('instance', {}).\
                    setdefault(instance, {}).\
                    setdefault('areas', {}).\
                    setdefault(area, {}).\
                    setdefault('interfaces', {}).\
                    setdefault(group['interface'], {})

                intf_dict.update({'state' : group['state']})
                intf_dict.update({'dr_id' : group['dr_id']})
                intf_dict.update({'bdr_id' : group['bdr_id']})
                intf_dict.update({'nbrs_count' : int(group['nbrs_count'])})
                continue

        return ret_dict


class ShowOspfInterface(ShowOspfInterfaceBrief):
    """ Parser for:
            * show ospf interface
            * show ospf interface {interface}
            * show ospf interface instance {instance}
    """

    cli_command = [
        'show ospf interface',
        'show ospf interface {interface}',
        'show ospf interface instance {instance}'
    ]

    def cli(self, interface=None, instance=None, output=None):
        if output is None:
            if interface:
                out = self.device.execute(self.cli_command[1].format(interface=interface))
            elif instance:
                out = self.device.execute(self.cli_command[2].format(instance=instance))
            else:
                out = self.device.execute(self.cli_command[0])
        else:
            out = output

        return super().cli(output=out)


class ShowOspfInterfaceDetailSchema(MetaParser):
    """ Schema for:
           * show ospf interface detail
           * show ospf interface {interface} detail
           * show ospf interface detail instance {instance}
           * show ospf interface {interface} detail instance {instance}
    """

    schema = {
        'instance': {
            Any(): {
                'areas': {
                    Any(): {
                        'interfaces': {
                            Any(): {
                                'state': str,
                                'dr_id': str,
                                'bdr_id': str,
                                'nbrs_count': int,
                                'type': str,
                                'address': str,
                                'mask': str,
                                'mtu': int,
                                Optional('dr_ip_addr'): str,
                                Optional('priority'): int,
                                'cost': int,
                                'adj_count': int,
                                'hello': int,
                                'dead': int,
                                'rexmit': int,
                                'ospf_stub_type': str,
                                'authentication_type': str,
                                'ospf_interface': {
                                    'protection_type': str,
                                    Optional('tilfa'): {
                                        'prot_link': str,
                                        'prot_srlg': str,
                                        'prot_fate': str,
                                        'prot_node': int
                                    },
                                    'topology': {
                                        Any(): {
                                            'id': int,
                                            'metric': int
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }


class ShowOspfInterfaceDetail(ShowOspfInterfaceDetailSchema):
    """ Parser for:
           * show ospf interface detail
           * show ospf interface {interface} detail
           * show ospf interface detail instance {instance}
           * show ospf interface {interface} detail instance {instance}
    """

    cli_command = [
        'show ospf interface detail',
        'show ospf interface {interface} detail',
        'show ospf interface detail instance {instance}',
        'show ospf interface {interface} detail instance {instance}'
    ]

    def cli(self, interface=None, instance=None, output=None):
        if output is None:
            if interface and instance:
                out = self.device.execute(self.cli_command[3].format(interface=interface, instance=instance))
            elif interface:
                out = self.device.execute(self.cli_command[1].format(interface=interface))
            elif instance:
                out = self.device.execute(self.cli_command[2].format(instance=instance))
            else:
                out = self.device.execute(self.cli_command[0])
        else:
            out = output

        # Init vars
        ret_dict = {}
        instance = 'master'

        # ge-0/0/2.0    BDR    0.0.0.1        10.64.4.4     5
        p1 = re.compile(r'^(?P<interface>\S+) +(?P<state>\S+) '
                        r'+(?P<area>\S+) +(?P<dr_id>\S+) +(?P<bdr_id>\S+) +(?P<nbrs_count>\d+)$')

        # Type: P2P, Address: 172.16.76.25, Mask: 255.255.255.0, MTU: 1200, Cost: 100
        p2 = re.compile(r'^Type: +(?P<interface_type>\w+), +Address: +(?P<interface_address>[\d.]+)'
                        r', +Mask: +(?P<address_mask>[\d.]+), +MTU: +(?P<mtu>\d+), +Cost: +(?P<interface_cost>\d+)$')

        # Adj count: 4
        p3 = re.compile(r'^Adj +count: +(?P<adj_count>\d+)$')

        # Hello: 10, Dead: 40, ReXmit: 5, Not Stub
        p4 = re.compile(r'^Hello: +(?P<hello_interval>\d+), +Dead: +(?P<dead_interval>\d+), +'
                        r'ReXmit: +(?P<retransmit_interval>\d+), +(?P<ospf_stub_type>[\w ]+)$')

        # Auth type: None
        p5 = re.compile(r'^Auth +type: +(?P<authentication_type>[\w ]+)$')

        # Protection type: Post Convergence
        p6 = re.compile(r'^Protection +type: +(?P<protection_type>[\w ]+)$')

        # Post convergence protection: Enabled, Fate sharing: No, SRLG: No, Node cost: 150
        p7 = re.compile(r'^Post +convergence +protection: +(?P<prot_link>\w+), +Fate +sharing: +'
                        r'(?P<prot_fate>\w+), +SRLG: +(?P<prot_srlg>\w+), +Node +cost: +(?P<prot_node>\d+)$')

        # Topology default (ID 0) -> Cost: 1000
        p8 = re.compile(r'^Topology +(?P<name>\w+) +\(ID +(?P<id>\d+)\) +-> +Cost: +(?P<metric>\d+)$')

        # DR addr: 10.16.2.2, Priority: 128
        p9 = re.compile(r'^DR +addr: +(?P<dr_address>[\d.]+), +Priority: +(?P<router_priority>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            # ge-0/0/2.0    BDR    0.0.0.1    10.16.2.2    10.64.4.4     5
            m = p1.match(line)
            if m:
                group = m.groupdict()
                area = group['area']
                intf_dict = ret_dict.setdefault('instance', {}).\
                    setdefault(instance, {}).\
                    setdefault('areas', {}).\
                    setdefault(area, {}).\
                    setdefault('interfaces', {}).\
                    setdefault(group['interface'], {})

                intf_dict.update({'state' : group['state']})
                intf_dict.update({'dr_id' : group['dr_id']})
                intf_dict.update({'bdr_id' : group['bdr_id']})
                intf_dict.update({'nbrs_count' : int(group['nbrs_count'])})
                continue

            # Type: P2P, Address: 172.16.76.25, Mask: 255.255.255.0, MTU: 1200, Cost: 100
            m = p2.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'type': group['interface_type']})
                intf_dict.update({'address': group['interface_address']})
                intf_dict.update({'mask': group['address_mask']})
                intf_dict.update({'mtu': int(group['mtu'])})
                intf_dict.update({'cost': int(group['interface_cost'])})
                continue

            # Adj count: 4
            m = p3.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'adj_count': int(group['adj_count'])})
                continue

            # Hello: 10, Dead: 40, ReXmit: 5, Not Stub
            m = p4.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'hello': int(group['hello_interval'])})
                intf_dict.update({'dead': int(group['dead_interval'])})
                intf_dict.update({'rexmit': int(group['retransmit_interval'])})
                intf_dict.update({'ospf_stub_type': group['ospf_stub_type']})
                continue

            # Auth type: None
            m = p5.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'authentication_type': group['authentication_type']})
                continue

            # Protection type: Post Convergence
            m = p6.match(line)
            if m:
                group = m.groupdict()
                ospf_intf_dict = intf_dict.setdefault('ospf_interface', {})
                ospf_intf_dict.update({'protection_type': group['protection_type']})
                continue

            # Post convergence protection: Enabled, Fate sharing: No, SRLG: No, Node cost: 150
            m = p7.match(line)
            if m:
                group = m.groupdict()
                tilfa_dict = ospf_intf_dict.setdefault('tilfa', {})
                tilfa_dict.update({'prot_link': group['prot_link']})
                tilfa_dict.update({'prot_fate': group['prot_fate']})
                tilfa_dict.update({'prot_srlg': group['prot_srlg']})
                tilfa_dict.update({'prot_node': int(group['prot_node'])})
                continue

            # Topology default (ID 0) -> Cost: 1000
            m = p8.match(line)
            if m:
                group = m.groupdict()
                topology_dict = ospf_intf_dict.setdefault('topology', {}).setdefault(group['name'], {})
                topology_dict.update({'id': int(group['id'])})
                topology_dict.update({'metric': int(group['metric'])})
                continue

            # DR addr: 10.16.2.2, Priority: 128
            m = p9.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'dr_ip_addr': group['dr_address']})
                intf_dict.update({'priority': int(group['router_priority'])})
                continue

        return ret_dict

'''
Schema for:
    * show ospf neighbor
'''
class ShowOspfNeighborSchema(MetaParser):
    '''
    schema = {
        'ospf-neighbor-information': {
            'ospf-neighbor': [{
                'neighbor-address': str,
                'interface-name': str,
                'ospf-neighbor-state': str,
                'neighbor-id': str,
                'neighbor-priority': str,
                'activity-timer': str
            }]
        }
    }
    '''
    def validate_neighbor_list(value):
        if not isinstance(value, list):
            raise SchemaTypeError('ospf-neighbor is not a list')
        neighbor_schema = Schema({
            'neighbor-address': str,
            'interface-name': str,
            'ospf-neighbor-state': str,
            'neighbor-id': str,
            'neighbor-priority': str,
            'activity-timer': str
        })
        for item in value:
            neighbor_schema.validate(item)
        return value
    schema = {
        'ospf-neighbor-information': {
            'ospf-neighbor': Use(validate_neighbor_list)
        }
    }

'''
Parser for:
    * show ospf neighbor
'''
class ShowOspfNeighbor(ShowOspfNeighborSchema):
    cli_command = 'show ospf neighbor'
    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # 10.189.5.94      ge-0/0/0.0             Full      10.189.5.253     128    32
        p1 = re.compile(r'^(?P<neighbor>\S+) +(?P<interface>\S+) +'
                r'(?P<state>\S+) +(?P<id>\S+) +(?P<pri>\d+) +(?P<dead>\d+)$')


        for line in out.splitlines():
            line = line.strip()

            # 10.189.5.94      ge-0/0/0.0             Full      10.189.5.253     128    32
            m = p1.match(line)
            if m:
                group = m.groupdict()
                neighbor = group['neighbor']
                interface = group['interface']
                state = group['state']
                _id = group['id']
                pri = group['pri']
                dead = group['dead']
                neighbor_list = ret_dict.setdefault('ospf-neighbor-information', {}). \
                                setdefault('ospf-neighbor', [])
                new_neighbor = {
                    'neighbor-address': neighbor,
                    'interface-name': interface,
                    'ospf-neighbor-state': state,
                    'neighbor-id': _id,
                    'neighbor-priority': pri,
                    'activity-timer': dead
                }
                neighbor_list.append(new_neighbor)
                continue
        return ret_dict

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

        def validate_ospf_link(value):
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
        p3 = re.compile(r'^bits +(?P<bits>\S+), +link +count +(?P<link_count>\d+)$')

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

                # mask 255.255.255.255
                m = p13.match(line)
                if m:
                    group = m.groupdict()

                    last_database = ret_dict["ospf-database-information"]["ospf-database"][-1]
                    last_database.setdefault("ospf-external-lsa", {})\
                        .setdefault("address-mask", group['address_mask'])
                    continue

                # Topology default (ID 0)
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

                # Type: 1, Metric: 50, Fwd addr: 0.0.0.0, Tag: 0.0.0.0
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

class ShowOspfDatabaseExtensiveSchema(MetaParser):
    """ Schema for:
            * show ospf database extensive
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

        def validate_ospf_link(value):
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
                Optional("ospf-network-lsa"): {
                    "address-mask": str,
                    "attached-router": list,
                    "ospf-lsa-topology": {
                        "ospf-lsa-topology-link": Use(validate_ospf_lsa_topology_link),
                        "ospf-topology-id": str,
                        "ospf-topology-name": str
                    }
                },
                "ospf-database-extensive": {
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
                    Optional("lsa-change-count"): str,
                    Optional("lsa-changed-time"): {
                        "#text": str
                    },
                    Optional("send-time"): {
                        "#text": str
                    },
                    Optional("database-entry-state"): str
                },
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

class ShowOspfDatabaseExtensive(ShowOspfDatabaseExtensiveSchema):
    """ Parser for:
            * show ospf database extensive
    """
    cli_command = 'show ospf database extensive'

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
        p3 = re.compile(r'^bits +(?P<bits>\S+), +link +count +(?P<link_count>\d+)$')

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

        # Aging timer 00:18:16
        p16 = re.compile(r"^Aging timer +(?P<aging_timer>(\S+ ){0,1}[\d\:]+)$")

        # Installed 00:10:20 ago, expires in 00:49:31, sent 00:10:18 ago
        p17 = re.compile(
            r"^Installed +(?P<installation_time>(\S+ ){0,1}[\d\:]+) +ago, +expires +in +"
            r"(?P<expiration_time>(\S+ ){0,1}[\d\:]+), +sent +(?P<send_time>(\S+ ){0,1}[\d\:]+) +ago$"
        )

        # Last changed 2w6d 04:50:31 ago, Change count: 196
        p18 = re.compile(
            r"^Last +changed +(?P<lsa_changed_time>(\S+ +){0,1}[\d\:]+) +ago, +Change +"
            r"count: +(?P<lsa_change_count>\d+)(, +(?P<database_entry_state>\S+)"
            r"(, +TE +Link +ID: +(?P<database_telink_id>\S+)))?$"
        )

        # Gen timer 00:49:49
        p19 = re.compile(r"^Gen +timer +(?P<generation_timer>\S+)$")

        # attached router 106.187.14.240
        p20 = re.compile(r'^attached +router +(?P<attached_router>[\d\.]+)$')

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

                # Aging timer 00:18:16
                m = p16.match(line)
                if m:
                    last_database = ret_dict["ospf-database-information"]["ospf-database"][-1]
                    last_database.setdefault("ospf-database-extensive", {}).setdefault(
                        "aging-timer", {}
                    )

                    group = m.groupdict()
                    last_database["ospf-database-extensive"]["aging-timer"][
                        "#text"
                    ] = group["aging_timer"]

                    continue

                # Installed 00:10:20 ago, expires in 00:49:31, sent 00:10:18 ago
                m = p17.match(line)
                if m:
                    last_entry = ret_dict["ospf-database-information"]["ospf-database"][-1]

                    last_entry.setdefault("ospf-database-extensive", {}).setdefault("expiration-time", {})
                    last_entry.setdefault("ospf-database-extensive", {}).setdefault("installation-time", {})
                    last_entry.setdefault("ospf-database-extensive", {}).setdefault("send-time", {})

                    group = m.groupdict()
                    last_entry["ospf-database-extensive"]["expiration-time"]["#text"] = group["expiration_time"]
                    last_entry["ospf-database-extensive"]["installation-time"]["#text"] = group["installation_time"]
                    last_entry["ospf-database-extensive"]["send-time"]["#text"] = group["send_time"]

                    continue

                # Last changed 2w6d 04:50:31 ago, Change count: 196
                m = p18.match(line)  # lsa_changed_time , lsa_changed_count
                if m:
                    last_entry = ret_dict["ospf-database-information"]["ospf-database"][-1]

                    last_entry.setdefault("ospf-database-extensive", {}).setdefault("lsa-changed-time", {})

                    group = m.groupdict()
                    last_entry["ospf-database-extensive"]["lsa-changed-time"]["#text"]\
                        = group["lsa_changed_time"]
                    last_entry["ospf-database-extensive"]["lsa-change-count"] = group["lsa_change_count"]

                    continue

                # Gen timer 00:49:49
                m = p19.match(line)
                if m:
                    last_database = ret_dict["ospf-database-information"]["ospf-database"][-1]

                    last_database.setdefault("ospf-database-extensive", {})\
                        .setdefault("generation-timer", {})

                    group = m.groupdict()
                    last_database["ospf-database-extensive"]["generation-timer"][
                        "#text"
                    ] = group["generation_timer"]

                    continue

            if self.lsa_type == "Network":
                # mask 255.255.255.255
                m = p13.match(line)
                if m:
                    group = m.groupdict()

                    last_database = ret_dict["ospf-database-information"]["ospf-database"][-1]
                    last_database.setdefault("ospf-network-lsa", {})\
                        .setdefault("address-mask", group['address_mask'])
                    continue

                # attached router 106.187.14.240
                m = p20.match(line)
                if m:
                    group = m.groupdict()

                    last_database = ret_dict["ospf-database-information"]["ospf-database"][-1]

                    last_database.setdefault("ospf-network-lsa", {}).setdefault("attached-router", []).append(group['attached_router'])

                    continue

                # # Topology default (ID 0)
                m = p6.match(line)
                if m:
                    last_database = ret_dict["ospf-database-information"]["ospf-database"][-1]

                    ospf_lsa_topology = last_database.setdefault("ospf-network-lsa", {})\
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

                    ospf_lsa_topology_list = last_database.setdefault("ospf-network-lsa", {})\
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
                    last_link = last_database["ospf-network-lsa"]["ospf-lsa-topology"]["ospf-lsa-topology-link"][-1]

                    group = m.groupdict()
                    entry = last_link
                    for group_key, group_value in group.items():
                        entry_key = group_key.replace('_','-')
                        entry[entry_key] = group_value

                    continue

                # Aging timer 00:18:16
                m = p16.match(line)
                if m:
                    last_database = ret_dict["ospf-database-information"]["ospf-database"][-1]
                    last_database.setdefault("ospf-database-extensive", {}).setdefault(
                        "aging-timer", {}
                    )

                    group = m.groupdict()
                    last_database["ospf-database-extensive"]["aging-timer"][
                        "#text"
                    ] = group["aging_timer"]

                    continue

                # Installed 00:10:20 ago, expires in 00:49:31, sent 00:10:18 ago
                m = p17.match(line)
                if m:
                    last_entry = ret_dict["ospf-database-information"]["ospf-database"][-1]

                    last_entry.setdefault("ospf-database-extensive", {}).setdefault("expiration-time", {})
                    last_entry.setdefault("ospf-database-extensive", {}).setdefault("installation-time", {})
                    last_entry.setdefault("ospf-database-extensive", {}).setdefault("send-time", {})

                    group = m.groupdict()
                    last_entry["ospf-database-extensive"]["expiration-time"]["#text"] = group["expiration_time"]
                    last_entry["ospf-database-extensive"]["installation-time"]["#text"] = group["installation_time"]
                    last_entry["ospf-database-extensive"]["send-time"]["#text"] = group["send_time"]

                    continue

                # Last changed 2w6d 04:50:31 ago, Change count: 196
                m = p18.match(line)  # lsa_changed_time , lsa_changed_count
                if m:
                    last_entry = ret_dict["ospf-database-information"]["ospf-database"][-1]

                    last_entry.setdefault("ospf-database-extensive", {}).setdefault("lsa-changed-time", {})

                    group = m.groupdict()
                    last_entry["ospf-database-extensive"]["lsa-changed-time"]["#text"]\
                        = group["lsa_changed_time"]
                    last_entry["ospf-database-extensive"]["lsa-change-count"] = group["lsa_change_count"]

                    continue

                # Gen timer 00:49:49
                m = p19.match(line)
                if m:
                    last_database = ret_dict["ospf-database-information"]["ospf-database"][-1]

                    last_database.setdefault("ospf-database-extensive", {})\
                        .setdefault("generation-timer", {})

                    group = m.groupdict()
                    last_database["ospf-database-extensive"]["generation-timer"][
                        "#text"
                    ] = group["generation_timer"]

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

                # Aging timer 00:18:16
                m = p16.match(line)
                if m:
                    last_database = ret_dict["ospf-database-information"]["ospf-database"][-1]
                    last_database.setdefault("ospf-database-extensive", {}).setdefault(
                        "aging-timer", {}
                    )

                    group = m.groupdict()
                    last_database["ospf-database-extensive"]["aging-timer"][
                        "#text"
                    ] = group["aging_timer"]

                    continue

                # Installed 00:10:20 ago, expires in 00:49:31, sent 00:10:18 ago
                m = p17.match(line)
                if m:
                    last_entry = ret_dict["ospf-database-information"]["ospf-database"][-1]

                    last_entry.setdefault("ospf-database-extensive", {}).setdefault("expiration-time", {})
                    last_entry.setdefault("ospf-database-extensive", {}).setdefault("installation-time", {})
                    last_entry.setdefault("ospf-database-extensive", {}).setdefault("send-time", {})

                    group = m.groupdict()
                    last_entry["ospf-database-extensive"]["expiration-time"]["#text"] = group["expiration_time"]
                    last_entry["ospf-database-extensive"]["installation-time"]["#text"] = group["installation_time"]
                    last_entry["ospf-database-extensive"]["send-time"]["#text"] = group["send_time"]

                    continue

                # Last changed 3w1d 21:01:25 ago, Change count: 4, Ours, TE Link ID: 2147483651
                m = p18.match(line)  # lsa_changed_time , lsa_changed_count
                if m:
                    last_entry = ret_dict["ospf-database-information"]["ospf-database"][-1]

                    last_entry.setdefault("ospf-database-extensive", {}).setdefault("lsa-changed-time", {})

                    group = m.groupdict()
                    last_entry["ospf-database-extensive"]["lsa-changed-time"]["#text"]\
                        = group["lsa_changed_time"]
                    last_entry["ospf-database-extensive"]["lsa-change-count"] = group["lsa_change_count"]

                    continue

                # Gen timer 00:49:49
                m = p19.match(line)
                if m:
                    last_database = ret_dict["ospf-database-information"]["ospf-database"][-1]

                    last_database.setdefault("ospf-database-extensive", {})\
                        .setdefault("generation-timer", {})

                    group = m.groupdict()
                    last_database["ospf-database-extensive"]["generation-timer"][
                        "#text"
                    ] = group["generation_timer"]

                    continue

            if self.lsa_type == "Extern":

                # mask 255.255.255.255
                m = p13.match(line)
                if m:
                    group = m.groupdict()

                    last_database = ret_dict["ospf-database-information"]["ospf-database"][-1]
                    last_database.setdefault("ospf-external-lsa", {})\
                        .setdefault("address-mask", group['address_mask'])
                    continue

                # Topology default (ID 0)
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

                # Type: 1, Metric: 50, Fwd addr: 0.0.0.0, Tag: 0.0.0.0
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

                # Aging timer 00:18:16
                m = p16.match(line)
                if m:
                    last_database = ret_dict["ospf-database-information"]["ospf-database"][-1]
                    last_database.setdefault("ospf-database-extensive", {}).setdefault(
                        "aging-timer", {}
                    )

                    group = m.groupdict()
                    last_database["ospf-database-extensive"]["aging-timer"][
                        "#text"
                    ] = group["aging_timer"]

                    continue

                # Installed 00:10:20 ago, expires in 00:49:31, sent 00:10:18 ago
                m = p17.match(line)
                if m:
                    last_entry = ret_dict["ospf-database-information"]["ospf-database"][-1]

                    last_entry.setdefault("ospf-database-extensive", {}).setdefault("expiration-time", {})
                    last_entry.setdefault("ospf-database-extensive", {}).setdefault("installation-time", {})
                    last_entry.setdefault("ospf-database-extensive", {}).setdefault("send-time", {})

                    group = m.groupdict()
                    last_entry["ospf-database-extensive"]["expiration-time"]["#text"] = group["expiration_time"]
                    last_entry["ospf-database-extensive"]["installation-time"]["#text"] = group["installation_time"]
                    last_entry["ospf-database-extensive"]["send-time"]["#text"] = group["send_time"]

                    continue

                # Last changed 2w6d 04:50:31 ago, Change count: 196
                m = p18.match(line)  # lsa_changed_time , lsa_changed_count
                if m:
                    last_entry = ret_dict["ospf-database-information"]["ospf-database"][-1]

                    last_entry.setdefault("ospf-database-extensive", {}).setdefault("lsa-changed-time", {})

                    group = m.groupdict()
                    last_entry["ospf-database-extensive"]["lsa-changed-time"]["#text"]\
                        = group["lsa_changed_time"]
                    last_entry["ospf-database-extensive"]["lsa-change-count"] = group["lsa_change_count"]

                    continue

                # Gen timer 00:49:49
                m = p19.match(line)
                if m:
                    last_database = ret_dict["ospf-database-information"]["ospf-database"][-1]

                    last_database.setdefault("ospf-database-extensive", {})\
                        .setdefault("generation-timer", {})

                    group = m.groupdict()
                    last_database["ospf-database-extensive"]["generation-timer"][
                        "#text"
                    ] = group["generation_timer"]

                    continue

        return ret_dict