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
        p1 = re.compile(r'^OSPF +database, +Area +(?P<ospf_area>[/d/.]+)$')

        # Router  *111.87.5.252     111.87.5.252     0x80001b9e  1801  0x22 0x1e2  120
        p2 = re.compile(r'^(?P<lsa_type>\S+)( +)(?P<lsa_id>\S+)( +)(?P<advertising_router>\S+)( +)(?P<sequence_number>\S+)( +)(?P<age>\S+)( +)(?P<options>\S+)( +)(?P<checksum>\S+)( +)(?P<lsa_length>\S+)$')

        # bits 0x2, link count 8
        p3 = re.compile(r'^bits +(?P<bits>\S+), +link +count (?P<link_count>\d+)$')

        # id 111.87.5.253, data 111.87.5.93, Type PointToPoint (1)
        p4 = re.compile(r'^id (?P<link_id>[\d\.]+), data (?P<link_data>[\d\.]+), Type (?P<link_type_name>\S+) \((?P<link_type_value>\S+)\)$')

        # Topology count: 0, Default metric: 5
        p5 = re.compile(r'^Topology +count: (?P<ospf_topology_count>\d+), Default metric: (?P<metric>\d+)$')

        # Topology default (ID 0)
        p6 = re.compile(r'^Topology +(?P<ospf_topology_name>\S+) +\(ID +(?P<ospf_topology_id>\S+)\)$')

        ret_dict = {}

        # group = m.groupdict()
        # entry = {}
        # for group_key, group_value in group.items():
        #     entry_key = group_key.replace('_','-')
        #     entry[entry_key] = group_value

        for line in out.splitlines():
            line = line.strip()

            # OSPF database, Area 0.0.0.8
            m = p1.match(line)
            if m:
                ospf_area = ret_dict.setdefault("ospf-database-information", {}).setdefault("ospf-area-header", {}).setdefault("ospf-area", None)
                if ospf_area:
                    raise Exception("ospf-area has already been set.")

                group = m.groupdict()
                ret_dict["ospf-database-information"]["ospf-area-header"]["ospf-area"] = group["ospf_area"]
                continue

            # Router  *111.87.5.252     111.87.5.252     0x80001b9e  1801  0x22 0x1e2  120
            m = p2.match(line)
            if m:
                database_list = ret_dict.setdefault("ospf-database-information", {}).setdefault("ospf-database", [])

                group = m.groupdict()
                entry = {}
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value

                database_list.append(entry)
                continue

            # bits 0x2, link count 8
            m = p3.match(line)
            if m:
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




        return ret_dict
