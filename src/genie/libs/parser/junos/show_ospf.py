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
    * show ospf neighbor
    * show ospf database
    * show ospf database summary
    * show ospf database external extensive
    * show ospf overview
    * show ospf overview extensive
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (Any, 
        Optional, Use, SchemaTypeError, Schema, Or)


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


class ShowOspfDatabaseSchema(MetaParser):
    '''
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
                Optional('our-entry'): bool
                "sequence-number": str
            }
        ]
    }
}
    '''
    def validate_neighbor_database_list(value):
        if not isinstance(value, list):
            raise SchemaTypeError('ospf-neighbor is not a list')
        neighbor_schema = Schema({
            "advertising-router": str,
                "age": str,
                "checksum": str,
                "lsa-id": str,
                "lsa-length": str,
                "lsa-type": str,
                "options": str,
                Optional('our-entry'): bool,
                "sequence-number": str
        })
        for item in value:
            neighbor_schema.validate(item)
        return value
    schema = {
        'ospf-database-information': {
            "ospf-area-header": {
            "ospf-area": str
        },
            'ospf-database': Use(validate_neighbor_database_list)
        }
    }

'''
Parser for:
    * show ospf database
'''
class ShowOspfDatabase(ShowOspfDatabaseSchema):
    cli_command = 'show ospf database'
    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        
        ret_dict = {}

        #OSPF database, Area 0.0.0.8
        p1 = re.compile(r'^OSPF database, Area +(?P<ospf_area>[\w\.\:\/]+)$')

        #Router   3.3.3.3          3.3.3.3          0x80004d2d    61  0x22 0xa127 2496
        #Router  *111.87.5.252     111.87.5.252     0x80001b9e  1608  0x22 0x1e2  120
        p2 = re.compile(r'^(?P<lsa_type>[a-zA-Z]+) *(?P<our_entry>\*)?(?P<lsa_id>[\d\.]+) +(?P<advertising_router>[\d\.]+) +(?P<sequence_number>\S+) +(?P<age>\d+) +(?P<options>\S+) +(?P<checksum>\S+) +(?P<lsa_length>\d+)$')
        
        for line in out.splitlines():
            line = line.strip()

            #OSPF database, Area 0.0.0.8
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ospf_database_info_dict = ret_dict.setdefault('ospf-database-information', {})

                ospf_database_info_list = ospf_database_info_dict.setdefault('ospf-database', [])
                ospf_database_info_dict2 = ospf_database_info_dict.setdefault('ospf-area-header', {})
                ospf_database_info_dict2['ospf-area'] = group['ospf_area']
                continue
            
            #Router   3.3.3.3          3.3.3.3          0x80004d2d    61  0x22 0xa127 2496
            #Router  *111.87.5.252     111.87.5.252     0x80001b9e  1608  0x22 0x1e2  120
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ospf_entry_dict = {}
                ospf_entry_dict['lsa-type'] = group['lsa_type']
                if group['our_entry'] == '*':
                    ospf_entry_dict['lsa-id'] = group['lsa_id'][1:]
                    ospf_entry_dict['our-entry'] = True
                else:
                    ospf_entry_dict['lsa-id'] = group['lsa_id']
                ospf_entry_dict['advertising-router'] = group['advertising_router']
                ospf_entry_dict['sequence-number'] = group['sequence_number']
                ospf_entry_dict['age'] = group['age']
                ospf_entry_dict['options'] = group['options']
                ospf_entry_dict['checksum'] = group['checksum']
                ospf_entry_dict['lsa-length'] = group['lsa_length']
                ospf_database_info_list.append(ospf_entry_dict)
                continue

        return ret_dict


class ShowOspfDatabaseSummarySchema(MetaParser):
    '''
    schema = {
    Optional("@xmlns:junos"): str,
    "ospf-database-information": {
        Optional("@xmlns"): str,
        "ospf-database-summary": [
            {
                Optional("@external-heading"): str,
                Optional("ospf-area"): Or(list, str),
                Optional("ospf-intf"): list,
                Optional("ospf-lsa-count"): Or(list, str),
                Optional("ospf-lsa-type"): Or(list, str)
            }
        ]
    }
    '''
    def validate_neighbor_database_summary_list(value):
        if not isinstance(value, list):
            raise SchemaTypeError('ospf-database-summary is not a list')
        neighbor_schema = Schema({
            Optional("@external-heading"): str,
            Optional("ospf-area"): Or(list, str),
            Optional("ospf-intf"): list,
            Optional("ospf-lsa-count"): Or(list, str),
            Optional("ospf-lsa-type"): Or(list, str)
        })
        for item in value:
            neighbor_schema.validate(item)
        return value
        
    schema = {
        'ospf-database-information': {
            'ospf-database-summary': Use(validate_neighbor_database_summary_list)
        }
    }

'''
Parser for:
    * show ospf database
'''
class ShowOspfDatabaseSummary(ShowOspfDatabaseSummarySchema):
    cli_command = 'show ospf database summary'
    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        
        ret_dict = {}

        #Area 0.0.0.8:
        p1 = re.compile(r'^Area +(?P<ospf_area1>[\w\.\/]+):$')

        #12 Router LSAs
        p2 = re.compile(r'^(?P<area_value>\d+) +(?P<area_name>\S+) LSAs$')

        #Externals:
        p3 = re.compile(r'^(?P<externals>\S+):$')

        #19 Extern LSAs
        p4 = re.compile(r'^(?P<external_value>\d+) +(?P<external_name>\S+) LSAs$')

        #Area 0.0.0.8:
        p5 = re.compile(r'^Area +(?P<ospf_area2>[\w\.\/]+):$')

        #Interface ge-0/0/3.0:
        p6 = re.compile(r'^Interface +(?P<interface>\S+):$')

        for line in out.splitlines():
            line = line.strip()
            #Area 0.0.0.8:
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ospf_database_info_dict = ret_dict.setdefault('ospf-database-information', {})
                ospf_database_info_list = ospf_database_info_dict.setdefault('ospf-database-summary', [None]*3)
                ospf_database_entry_dict1 = {}
                ospf_database_entry_dict2 = {}
                ospf_database_entry_dict3 = {}
                ospf_database_entry_name_list = []
                ospf_database_entry_value_list = []
                ospf_database_entry_area_list = []
                ospf_database_entry_intf_list = []
                
                ospf_database_entry_dict1['ospf-area'] = group['ospf_area1']
                p1 = re.compile(r'^empty$')
                continue
            
            #12 Router LSAs
            m = p2.match(line)
            if m:
                group = m.groupdict()
                
                ospf_database_entry_value_list.append(group['area_value'])
                ospf_database_entry_name_list.append(group['area_name'])
                continue

            #Externals:
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ospf_database_entry_dict2['@external-heading'] = group['externals']
                p1 = re.compile(r'^empty$')
                p2 = re.compile(r'^empty$')
                continue

            #19 Extern LSAs
            m = p4.match(line)
            if m:
                group = m.groupdict()
                
                ospf_database_entry_dict2['ospf-lsa-count'] = group['external_value']
                ospf_database_entry_dict2['ospf-lsa-type'] = group['external_name']
                continue

            #Area 0.0.0.8:
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ospf_database_entry_area_list.append(group['ospf_area2'])
                continue

            #Interface ge-0/0/3.0:
            m = p6.match(line)
            if m:
                group = m.groupdict()
                ospf_database_entry_intf_list.append(group['interface'])

                ospf_database_entry_dict1["ospf-lsa-count"] = ospf_database_entry_value_list
                ospf_database_entry_dict1["ospf-lsa-type"] = ospf_database_entry_name_list
                ospf_database_entry_dict3["ospf-area"] = ospf_database_entry_area_list
                ospf_database_entry_dict3["ospf-intf"] = ospf_database_entry_intf_list

                ospf_database_info_list[0:] = ospf_database_entry_dict1, \
                                            ospf_database_entry_dict2, ospf_database_entry_dict3
                continue

        return ret_dict

class ShowOspfDatabaseExternalExtensiveSchema(MetaParser):
    
    """ schema = {
    Optional("@xmlns:junos"): str,
    "ospf-database-information": {
        Optional("@xmlns"): str,
        "ospf-database": [
            {
                Optional("@external-heading"): str,
                Optional("@heading"): str,
                "advertising-router": str,
                "age": str,
                "checksum": str,
                "lsa-id": str,
                "lsa-length": str,
                "lsa-type": str,
                "options": str,
                "ospf-database-extensive": {
                    "aging-timer": {
                        "#text": str,
                        Optional("@junos:seconds"): str
                    },
                    "expiration-time": {
                        "#text": str,
                        Optional("@junos:seconds"): str
                    },
                    "installation-time": {
                        "#text": str,
                        Optional("@junos:seconds"): str
                    },
                    "lsa-change-count": str,
                    "lsa-changed-time": {
                        "#text": str,
                        Optional("@junos:seconds"): str
                    },
                    "send-time": {
                        "#text": str,
                        Optional("@junos:seconds"): str
                    }
                },
                "ospf-external-lsa": {
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
            }
        ]
    }
} """
    
    def validate_neighbor_database_external_extensive_list(value):
        if not isinstance(value, list):
            raise SchemaTypeError('ospf-database is not a list')
        neighbor_schema = Schema({
            Optional("@external-heading"): str,
                Optional("@heading"): str,
                "advertising-router": str,
                "age": str,
                "checksum": str,
                "lsa-id": str,
                "lsa-length": str,
                "lsa-type": str,
                "options": str,
                "ospf-database-extensive": {
                    "aging-timer": {
                        "#text": str,
                        Optional("@junos:seconds"): str
                    },
                    "expiration-time": {
                        "#text": str,
                        Optional("@junos:seconds"): str
                    },
                    "installation-time": {
                        "#text": str,
                        Optional("@junos:seconds"): str
                    },
                    "lsa-change-count": str,
                    "lsa-changed-time": {
                        "#text": str,
                        Optional("@junos:seconds"): str
                    },
                    "send-time": {
                        "#text": str,
                        Optional("@junos:seconds"): str
                    }
                },
                "ospf-external-lsa": {
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
            neighbor_schema.validate(item)
        return value
        
    schema = {
        Optional("@xmlns:junos"): str,
        'ospf-database-information': {
            Optional("@xmlns"): str,
            'ospf-database': Use(validate_neighbor_database_external_extensive_list)
        }
    }

'''
Parser for:
    * show ospf database external extensive
'''
class ShowOspfDatabaseExternalExtensive(ShowOspfDatabaseExternalExtensiveSchema):
    cli_command = 'show ospf database external extensive'
    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        
        ret_dict = {}

        #OSPF AS SCOPE link state database        
        p1 = re.compile(r'^(?P<external_heading>\AOSPF AS[\S\s]+)$')
        
        #Type       ID               Adv Rtr           Seq      Age  Opt  Cksum  Len
        p2 = re.compile(r'^(?P<heading>\AType +ID[\S\s]+)$')

        #Extern   0.0.0.0          59.128.2.251     0x800019e3  2728  0x22 0x6715  36
        p3 = re.compile(r'^(?P<lsa_type>\S+)\s+(?P<lsa_id>[\d+\.]+)\s+'
                        r'(?P<advertising_router>[\d+\.]+)\s+(?P<sequence_number>\S+)'
                        r'\s+(?P<age>\d+)\s+(?P<options>[\S]+)\s+(?P<checksum>[\S]+)'
                        r'\s+(?P<lsa_length>\d+)$')

        #mask 0.0.0.0
        p4 = re.compile(r'^mask +(?P<address_mask>\S+)$')

        #Topology default (ID 0)
        p5 = re.compile(r'^Topology (?P<ospf_topology_name>\S+) +\(ID +(?P<ospf_topology_id>\d+)\)$')
        
        #Type: 1, Metric: 1, Fwd addr: 0.0.0.0, Tag: 0.0.0.0
        p6 = re.compile(r'^Type: +(?P<type_value>\d+), Metric: +(?P<ospf_topology_metric>\d+), '
                        r'Fwd addr: +(?P<forward_address>[\w\.\/]+), '
                        r'Tag: +(?P<tag>[\w\.\/]+)$')
        
        #Aging timer 00:14:32
        p7 = re.compile(r'^Aging timer +(?P<text>[\w\:]+)$')

        #Installed 00:45:19 ago, expires in 00:14:32, sent 00:45:17 ago
        p8 = re.compile(r'^Installed +(?P<installed_time>[\w\.\/\:]+) ' 
                        r'ago, expires in +(?P<expired_time>[\w\.\/\:]+), '
                        r'sent +(?P<sent_time>[\w\.\/\:]+) ago$')

        #Last changed 30w0d 01:34:30 ago, Change count: 1
        p9 = re.compile(r'Last changed +(?P<installed_time>[\S]+) '
                        r'+(?P<installed_time2>[\S]+) ago, Change count: '
                        r'+(?P<lsa_change_count>[\S]+)$')         


        for line in out.splitlines()[2:]:
            line = line.strip()

            #OSPF AS SCOPE link state database
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ospf_database_info_dict = ret_dict.setdefault('ospf-database-information', {})
                ospf_database_info_list = ospf_database_info_dict.setdefault('ospf-database', [])
                ospf_database_entry_dict = {}
                
                ospf_database_entry_dict['@external-heading'] = group['external_heading']
                #p1 = re.compile(r'^empty$')
                reset = True
                continue
            
            #Type       ID               Adv Rtr           Seq      Age  Opt  Cksum  Len            
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ospf_database_entry_dict['@heading'] = group['heading']
                #p2 = re.compile(r'^empty$')
                continue

            #Extern   0.0.0.0          59.128.2.251     0x800019e3  2728  0x22 0x6715  36
            m = p3.match(line)
            if m:
                if reset:
                    pass
                else:
                    ospf_database_entry_dict = {}

                group = m.groupdict()
                ospf_database_entry_dict['lsa-type'] = group['lsa_type']
                ospf_database_entry_dict['lsa-id'] = group['lsa_id']
                ospf_database_entry_dict['advertising-router'] = group['advertising_router']
                ospf_database_entry_dict['sequence-number'] = group['sequence_number']

                ospf_database_entry_dict['age'] = group['age']
                ospf_database_entry_dict['options'] = group['options']
                ospf_database_entry_dict['checksum'] = group['checksum']
                ospf_database_entry_dict['lsa-length'] = group['lsa_length']
                reset = False
                continue

            #mask 0.0.0.0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ospf_external_dict = {}
                ospf_external_dict["address-mask"] = group['address_mask']
                continue

            #Topology default (ID 0)
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ospf_external_topology_dict = {}
                ospf_external_topology_dict["ospf-topology-id"] = group['ospf_topology_id']
                ospf_external_topology_dict["ospf-topology-name"] = group['ospf_topology_name']
                continue

            #Type: 1, Metric: 1, Fwd addr: 0.0.0.0, Tag: 0.0.0.0
            m = p6.match(line)
            if m:
                group = m.groupdict()
                ospf_external_topology_dict["type-value"] = group['type_value']
                ospf_external_topology_dict["ospf-topology-metric"] = group['ospf_topology_metric']
                ospf_external_topology_dict["forward-address"] = group['forward_address']
                ospf_external_topology_dict["tag"] = group['tag']

                ospf_external_dict["ospf-external-lsa-topology"] = ospf_external_topology_dict

                ospf_database_entry_dict["ospf-external-lsa"] = ospf_external_dict

            #Aging timer 00:14:32
            m = p7.match(line)
            if m:
                group = m.groupdict()
                ospf_database_info_list
                ospf_db_ext_dict = {}

                age_dict = ospf_db_ext_dict.setdefault('aging-timer', {})
                exp_dict = ospf_db_ext_dict.setdefault('expiration-time', {})
                inst_dict = ospf_db_ext_dict.setdefault('installation-time', {})
                lsa_dict = ospf_db_ext_dict.setdefault('lsa-changed-time', {})
                send_time_dict = ospf_db_ext_dict.setdefault('send-time', {})

                age_dict.update({'#text': group['text']})
                continue

            #Installed 00:45:19 ago, expires in 00:14:32, sent 00:45:17 ago
            m = p8.match(line)
            if m:
                group = m.groupdict()

                inst_dict.update({'#text': group['installed_time']})
                exp_dict.update({'#text': group['expired_time']})
                send_time_dict.update({'#text': group['sent_time']})
                continue

            #Last changed 30w0d 01:34:30 ago, Change count: 1
            m = p9.match(line)
            if m:
                group = m.groupdict()

                lsa_dict.update({'#text': group['installed_time'] + ' ' + group['installed_time2']})
                ospf_db_ext_dict["lsa-change-count"] = group['lsa_change_count']

                ospf_database_entry_dict["ospf-database-extensive"] = ospf_db_ext_dict
                ospf_database_info_list.append(ospf_database_entry_dict)
                continue

        return ret_dict


class ShowOspfOverviewSchema(MetaParser):
    
    schema = {
    Optional("@xmlns:junos"): str,
    "ospf-overview-information": {
        Optional("@xmlns"): str,
        "ospf-overview": {
            "instance-name": str,
            "ospf-area-overview": {
                "authentication-type": str,
                "ospf-abr-count": str,
                "ospf-area": str,
                "ospf-asbr-count": str,
                "ospf-nbr-overview": {
                    "ospf-nbr-up-count": str
                },
                "ospf-stub-type": str
            },
            "ospf-lsa-refresh-time": str,
            "ospf-route-table-index": str,
            "ospf-router-id": str,
            "ospf-spring-overview": {
                "ospf-node-segment": {
                    "ospf-node-segment-ipv4-index": str
                },
                "ospf-node-segment-enabled": str,
                "ospf-spring-enabled": str,
                "ospf-srgb-allocation": str,
                "ospf-srgb-block": {
                    "ospf-srgb-first-label": str,
                    "ospf-srgb-last-label": str,
                    "ospf-srgb-size": str,
                    "ospf-srgb-start-index": str
                },
                "ospf-srgb-config": {
                    "ospf-srgb-config-block-header": str,
                    "ospf-srgb-index-range": str,
                    "ospf-srgb-start-label": str
                }
            },
            "ospf-tilfa-overview": {
                "ospf-tilfa-ecmp-backup": str,
                "ospf-tilfa-enabled": str,
                "ospf-tilfa-max-labels": str,
                "ospf-tilfa-max-spf": str
            },
            "ospf-topology-overview": {
                "ospf-backup-spf-status": str,
                "ospf-full-spf-count": str,
                "ospf-prefix-export-count": str,
                "ospf-spf-delay": str,
                "ospf-spf-holddown": str,
                "ospf-spf-rapid-runs": str,
                "ospf-topology-id": str,
                "ospf-topology-name": str
            }
        }
    }
}
    
  

'''
Parser for:
    * show ospf overview
'''
class ShowOspfOverview(ShowOspfOverviewSchema):
    cli_command = 'show ospf overview'
    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        
        ret_dict = {}


        #Instance: master
        p1 = re.compile(r'^Instance: +(?P<instance_name>\S+)$')
        
        #Router ID: 111.87.5.252
        p2 = re.compile(r'^Router ID: +(?P<ospf_router_id>[\w\.\:\/]+)$')

        #Route table index: 0
        p3 = re.compile(r'^Route table index: +(?P<ospf_route_table_index>\d+)$')

        #LSA refresh time: 50 minutes
        p4 = re.compile(r'^LSA refresh time: +(?P<ospf_lsa_refresh_time>\d+) minutes$')

        #SPRING: Enabled
        p5 = re.compile(r'^SPRING: +(?P<ospf_spring_enabled>\S+)$')

        #SRGB Start-Label : 16000, SRGB Index-Range : 8000
        p6 = re.compile(r'^SRGB Start-Label : +(?P<ospf_srgb_start_label>\d+), SRGB Index-Range : '
                        r'+(?P<ospf_srgb_index_range>\d+)$')
        
        #SRGB Block Allocation: Success
        p7 = re.compile(r'^SRGB Block Allocation: +(?P<ospf_srgb_allocation>\S+)$')

        #SRGB Start Index : 16000, SRGB Size : 8000, Label-Range: [ 16000, 23999 ]
        p8 = re.compile(r'^SRGB Start Index : +(?P<ospf_srgb_start_index>\d+), SRGB Size : '
                        r'+(?P<ospf_srgb_size>\d+), Label-Range: \[ +(?P<ospf_srgb_first_label>\d+), '
                        r'+(?P<ospf_srgb_last_label>\d+) \]$')
        
        #Node Segments: Enabled
        p9 = re.compile(r'^Node Segments: +(?P<ospf_node_segment_enabled>\S+)$')

        #Ipv4 Index : 71
        p10 = re.compile(r'^Ipv4 Index : +(?P<ospf_node_segment_ipv4_index>\d+)$')

        #Post Convergence Backup: Enabled
        p11 = re.compile(r'^Post Convergence Backup: +(?P<ospf_tilfa_enabled>\S+)$')

        #Max labels: 3, Max spf: 100, Max Ecmp Backup: 1
        p12 = re.compile(r'^Max labels: +(?P<ospf_tilfa_max_labels>\d+), '
                         r'Max spf: +(?P<ospf_tilfa_max_spf>\d+), Max Ecmp Backup: '
                         r'+(?P<ospf_tilfa_ecmp_backup>\d+)$')

        #Area: 0.0.0.8
        p13 = re.compile(r'^Area: +(?P<ospf_area>[\w\.\:\/]+)$')

        #Stub type: Not Stub
        p14 = re.compile(r'^Stub type: +(?P<ospf_stub_type>[\S+\s]+)$')

        #Authentication Type: None
        p15 = re.compile(r'^Authentication Type: +(?P<authentication_type>\S+)$')

        #Area border routers: 0, AS boundary routers: 7
        p16 = re.compile(r'^Area border routers: +(?P<ospf_abr_count>\d+), '
                         r'AS boundary routers: +(?P<ospf_asbr_count>\d+)$')

        #Up (in full state): 3
        p17 = re.compile(r'^Up \(in full state\): +(?P<ospf_nbr_up_count>\d+)$')

        #Topology: default (ID 0)
        p18 = re.compile(r'^Topology: +(?P<ospf_topology_name>\S+) \(ID +(?P<ospf_topology_id>\d+)\)$')

        #Prefix export count: 1
        p19 = re.compile(r'^Prefix export count: +(?P<ospf_prefix_export_count>\d+)$')

        #Full SPF runs: 173416
        p20 = re.compile(r'^Full SPF runs: +(?P<ospf_full_spf_count>\d+)$')

        #SPF delay: 0.200000 sec, SPF holddown: 2 sec, SPF rapid runs: 3
        p21 = re.compile(r'^SPF delay: +(?P<ospf_spf_delay>[\w\.]+) sec, SPF holddown: '
                         r'+(?P<ospf_spf_holddown>[\w\.]+) sec, SPF rapid runs: +'
                         r'(?P<ospf_spf_rapid_runs>[\w\.]+)$')

        #Backup SPF: Not Needed
        p22 = re.compile(r'^Backup SPF: +(?P<ospf_backup_spf_status>[\S\s]+)$')


        for line in out.splitlines():
            line = line.strip()

            #Instance: master
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ospf_entry_list = ret_dict.setdefault('ospf-overview-information', {}).\
                    setdefault('ospf-overview', {})
                ospf_entry_list['instance-name'] = group['instance_name']
                continue
            
            #Router ID: 111.87.5.252
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ospf_entry_list['ospf-router-id'] = group['ospf_router_id']
                continue

            #Route table index: 0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ospf_entry_list['ospf-route-table-index'] = group['ospf_route_table_index']
                continue

            #LSA refresh time: 50 minute
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ospf_entry_list['ospf-lsa-refresh-time'] = group['ospf_lsa_refresh_time']
                continue

            #SPRING: Enabled
            m = p5.match(line)
            if m:
                group = m.groupdict()
                spring_dict = {}
                spring_dict["ospf-spring-enabled"] = group["ospf_spring_enabled"]
                continue

            #SRGB Start-Label : 16000, SRGB Index-Range : 8000
            m = p6.match(line)
            if m:
                group = m.groupdict()
                spring_config_dict = {}
                spring_config_dict["ospf-srgb-config-block-header"] = "SRGB Config Range"
                spring_config_dict["ospf-srgb-index-range"] = group["ospf_srgb_index_range"]
                spring_config_dict["ospf-srgb-start-label"] = group["ospf_srgb_start_label"]

                spring_dict["ospf-srgb-config"] = spring_config_dict
                continue

            #SRGB Block Allocation: Success
            m = p7.match(line)
            if m:
                group = m.groupdict()
                spring_dict["ospf-srgb-allocation"] = group["ospf_srgb_allocation"]
                continue

            #SRGB Start Index : 16000, SRGB Size : 8000, Label-Range: [ 16000, 23999 ]
            m = p8.match(line)
            if m:
                group = m.groupdict()
                ospf_srgb_block_dict = {}
                ospf_srgb_block_dict["ospf-srgb-start-index"] = group["ospf_srgb_start_index"]
                ospf_srgb_block_dict["ospf-srgb-size"] = group["ospf_srgb_size"]
                ospf_srgb_block_dict["ospf-srgb-first-label"] = group["ospf_srgb_first_label"]
                ospf_srgb_block_dict["ospf-srgb-last-label"] = group["ospf_srgb_last_label"]

                spring_dict["ospf-srgb-block"] = ospf_srgb_block_dict
                continue

            #Node Segments: Enabled
            m = p9.match(line)
            if m:
                group = m.groupdict()
                spring_dict["ospf-node-segment-enabled"] = group["ospf_node_segment_enabled"]
                continue

            #Ipv4 Index : 71
            m = p10.match(line)
            if m:
                group = m.groupdict()
                node_dict = {}
                node_dict["ospf-node-segment-ipv4-index"] = group["ospf_node_segment_ipv4_index"]

                spring_dict["ospf-node-segment"] = node_dict
                continue

            #Post Convergence Backup: Enabled
            m = p11.match(line)
            if m:
                group = m.groupdict()
                tilfa_dict = {}
                tilfa_dict["ospf-tilfa-enabled"] = group["ospf_tilfa_enabled"]
                continue

            #Max labels: 3, Max spf: 100, Max Ecmp Backup: 1
            m = p12.match(line)
            if m:
                group = m.groupdict()
                tilfa_dict["ospf-tilfa-max-labels"] = group["ospf_tilfa_max_labels"]
                tilfa_dict["ospf-tilfa-max-spf"] = group["ospf_tilfa_max_spf"]
                tilfa_dict["ospf-tilfa-ecmp-backup"] = group["ospf_tilfa_ecmp_backup"]

                ospf_entry_list["ospf-tilfa-overview"] = tilfa_dict
                continue

            #Area: 0.0.0.8
            m = p13.match(line)
            if m:
                group = m.groupdict()
                ospf_area_entry_dict = ospf_entry_list.setdefault('ospf-area-overview', {})
                ospf_area_entry_dict.update({'ospf-area': group['ospf_area']})
                continue

            #Stub type: Not Stub
            m = p14.match(line)
            if m:
                group = m.groupdict()
                ospf_area_entry_dict.update({'ospf-stub-type': group['ospf_stub_type']})
                continue

            #Authentication Type: None
            m = p15.match(line)
            if m:
                group = m.groupdict()
                ospf_area_entry_dict.update({'authentication-type': group['authentication_type']})
                continue

             #Area border routers: 0, AS boundary routers: 7
            m = p16.match(line)
            if m:
                group = m.groupdict()
                ospf_area_entry_dict.update({'ospf-abr-count': group['ospf_abr_count']})
                ospf_area_entry_dict.update({'ospf-asbr-count': group['ospf_asbr_count']})
                continue

            #Up (in full state): 2
            m = p17.match(line)
            if m:
                group = m.groupdict()
                ospf_area_entry_dict.setdefault('ospf-nbr-overview', {"ospf-nbr-up-count":group['ospf_nbr_up_count']})
                continue

            #Topology: default (ID 0)
            m = p18.match(line)
            if m:
                group = m.groupdict()
                ospf_topology_entry_dict = ospf_entry_list.setdefault('ospf-topology-overview', {})
                ospf_topology_entry_dict.update({'ospf-topology-name': group['ospf_topology_name']})
                ospf_topology_entry_dict.update({'ospf-topology-id': group['ospf_topology_id']})
                continue

            #Prefix export count: 1
            m = p19.match(line)
            if m:
                group = m.groupdict()
                ospf_topology_entry_dict.update({'ospf-prefix-export-count': group['ospf_prefix_export_count']})
                continue

            #Full SPF runs: 1934
            m = p20.match(line)
            if m:
                group = m.groupdict()
                ospf_topology_entry_dict.update({'ospf-full-spf-count': group['ospf_full_spf_count']})
                continue

            #SPF delay: 0.200000 sec, SPF holddown: 2 sec, SPF rapid runs: 3
            m = p21.match(line)
            if m:
                group = m.groupdict()
                ospf_topology_entry_dict.update({'ospf-spf-delay': group['ospf_spf_delay']})
                ospf_topology_entry_dict.update({'ospf-spf-holddown': group['ospf_spf_holddown']})
                ospf_topology_entry_dict.update({'ospf-spf-rapid-runs': group['ospf_spf_rapid_runs']})
                continue

            #Backup SPF: Not Needed
            m = p22.match(line)
            if m:
                group = m.groupdict()
                ospf_topology_entry_dict.update({'ospf-backup-spf-status': group['ospf_backup_spf_status']})

                ospf_entry_list['ospf-spring-overview'] = spring_dict

                continue
        
        return ret_dict 

class ShowOspfOverviewExtensive(ShowOspfOverview):
    """ Parser for:
            - show ospf overview extensive
    """

    cli_command = [
        'show ospf overview extensive'
    ]

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command[0])
        else:
            out = output

        return super().cli(output=out)