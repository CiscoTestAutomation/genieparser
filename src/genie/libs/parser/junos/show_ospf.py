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
        p2 = re.compile(r'^(?P<lsa_type>[a-zA-Z]+)+(\*+|\s+)(?P<lsa_id>[\d\.\*]+)+(\s+)(?P<advertising_router>[\d\.]+)+'
                r'(\s+)(?P<sequence_number>\S+)(\s+)+(?P<age>\d+)(\s+)+(?P<options>\S+)(\s+)+(?P<checksum>\S+)(\s+)+(?P<lsa_length>\d+)$')

        #(?P<lsa_type>[a-zA-Z]+)+(\*+|\s+)(?P<aa>[\d\.\*]+)+(\s+)(?P<a>[\d\.]+)+(\s+)(?P<b>\S+)(\s+)+(?P<c>\d+)(\s+)+(?P<v>\S+)(\s+)+(?P<wewe>\S+)(\s+)+(?P<asdf>\d+)

        #(?P<lsa_type>[a-zA-Z]+)+(\*+|\s+)(?P<aa>[\d\.\*]+)+(\s+)(?P<a>[\d\.]+)+(\s+)(?P<b>\S+)(\s+)+(?P<c>\d+)(\s+)+(?P<v>\S+)(\s+)+(?P<wewe>\S+)(\s+)+(?P<asdf>\d+)
        
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
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ospf_entry_dict = {}
                ospf_entry_dict['lsa-type'] = group['lsa_type']
                if group['lsa_id'][0] == '*':
                    ospf_entry_dict['lsa-id'] = group['lsa_id'][1:]
                    ospf_entry_dict['our-entry'] = True
                else:
                    ospf_entry_dict['lsa-id'] = group['lsa_id']
                #ospf_entry_dict['lsa-id'] = group['lsa_id']
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
        p2 = re.compile(r'^(?P<area_value>\d+) (?P<area_name>\S+) LSAs$')

        #Externals:
        p3 = re.compile(r'^(?P<externals>\S+):$')

        #19 Extern LSAs
        p4 = re.compile(r'^(?P<external_value>\d+) (?P<external_name>\S+) LSAs$')

        #Area 0.0.0.8:
        p5 = re.compile(r'^Area +(?P<ospf_area2>[\w\.\/]+):$')

        #Interface ge-0/0/3.0:
        p6 = re.compile(r'^Interface (?P<interface>\S+):$')



        

        for line in out.splitlines():
            line = line.strip()
            #import pdb; pdb.set_trace()
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

                ospf_database_info_list[0:] = ospf_database_entry_dict1, ospf_database_entry_dict2, ospf_database_entry_dict3
                #ospf_database_info_list.append(ospf_database_entry_dict1)
                #ospf_database_info_list.append(ospf_database_entry_dict2)
                #ospf_database_info_list.append(ospf_database_entry_dict3)
                continue
        
        if ret_dict:
            ospf_database_entry_dict1["ospf-lsa-count"] = ospf_database_entry_value_list
            ospf_database_entry_dict1["ospf-lsa-type"] = ospf_database_entry_name_list
            ospf_database_entry_dict3["ospf-area"] = ospf_database_entry_area_list
            ospf_database_entry_dict3["ospf-intf"] = ospf_database_entry_intf_list

        

        


        return ret_dict

