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
    * show ospf database opaque-area
    * show ospf overview
    * show ospf overview extensive
    * show ospf database advertising-router self detail
    * show ospf neighbor extensive
    * show ospf neighbor detail
    * show ospf neighbor {neighbor} detail
    * show ospf neighbor instance {instance_name}
    * show ospf interface extensive
    * show ospf database network lsa-id {ipaddress} detail
    * show ospf database lsa-id {ipaddress} detail
    * show ospf route brief
    * show ospf route network extensive
    * show ospf database advertising-router {ipaddress} extensive
    * show ospf neighbor instance all
    * show ospf statistics
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from pyats.utils.exceptions import SchemaError
from genie.metaparser.util.schemaengine import (Any, Optional, Use,
                                                Schema, Or, ListOf)


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
        'show ospf interface {interface} brief', 'show ospf interface brief',
        'show ospf interface brief instance {instance}'
    ]

    def cli(self, interface=None, instance=None, output=None):
        if output is None:
            if instance:
                out = self.device.execute(
                    self.cli_command[2].format(instance=instance))
            elif interface:
                out = self.device.execute(
                    self.cli_command[0].format(interface=interface))
            else:
                out = self.device.execute(self.cli_command[1])
        else:
            out = output

        # Init vars
        ret_dict = {}
        instance = instance if instance else 'master'

        # ge-0/0/2.0    BDR    0.0.0.1    10.16.2.2    10.64.4.4     5
        p1 = re.compile(
            r'^(?P<interface>\S+) +(?P<state>\S+) '
            '+(?P<area>\S+) +(?P<dr_id>\S+) +(?P<bdr_id>\S+) +(?P<nbrs_count>\d+)$'
        )

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

                intf_dict.update({'state': group['state']})
                intf_dict.update({'dr_id': group['dr_id']})
                intf_dict.update({'bdr_id': group['bdr_id']})
                intf_dict.update({'nbrs_count': int(group['nbrs_count'])})
                continue

        return ret_dict


class ShowOspfInterface(ShowOspfInterfaceBrief):
    """ Parser for:
            * show ospf interface
            * show ospf interface {interface}
            * show ospf interface instance {instance}
    """

    cli_command = [
        'show ospf interface', 'show ospf interface {interface}',
        'show ospf interface instance {instance}'
    ]

    def cli(self, interface=None, instance=None, output=None):
        if output is None:
            if interface:
                out = self.device.execute(
                    self.cli_command[1].format(interface=interface))
            elif instance:
                out = self.device.execute(
                    self.cli_command[2].format(instance=instance))
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
        'show ospf interface detail', 'show ospf interface {interface} detail',
        'show ospf interface detail instance {instance}',
        'show ospf interface {interface} detail instance {instance}'
    ]

    def cli(self, interface=None, instance=None, output=None):
        if output is None:
            if interface and instance:
                out = self.device.execute(self.cli_command[3].format(
                    interface=interface, instance=instance))
            elif interface:
                out = self.device.execute(
                    self.cli_command[1].format(interface=interface))
            elif instance:
                out = self.device.execute(
                    self.cli_command[2].format(instance=instance))
            else:
                out = self.device.execute(self.cli_command[0])
        else:
            out = output

        # Init vars
        ret_dict = {}
        instance = 'master'

        # ge-0/0/2.0    BDR    0.0.0.1        10.64.4.4     5
        p1 = re.compile(
            r'^(?P<interface>\S+) +(?P<state>\S+) '
            r'+(?P<area>\S+) +(?P<dr_id>\S+) +(?P<bdr_id>\S+) +(?P<nbrs_count>\d+)$'
        )

        # Type: P2P, Address: 172.16.76.25, Mask: 255.255.255.0, MTU: 1200, Cost: 100
        p2 = re.compile(
            r'^Type: +(?P<interface_type>\w+), +Address: +(?P<interface_address>[\d.]+)'
            r', +Mask: +(?P<address_mask>[\d.]+), +MTU: +(?P<mtu>\d+), +Cost: +(?P<interface_cost>\d+)$'
        )

        # Adj count: 4
        p3 = re.compile(r'^Adj +count: +(?P<adj_count>\d+)$')

        # Hello: 10, Dead: 40, ReXmit: 5, Not Stub
        p4 = re.compile(
            r'^Hello: +(?P<hello_interval>\d+), +Dead: +(?P<dead_interval>\d+), +'
            r'ReXmit: +(?P<retransmit_interval>\d+), +(?P<ospf_stub_type>[\w ]+)$'
        )

        # Auth type: None
        p5 = re.compile(r'^Auth +type: +(?P<authentication_type>[\w ]+)$')

        # Protection type: Post Convergence
        p6 = re.compile(r'^Protection +type: +(?P<protection_type>[\w ]+)$')

        # Post convergence protection: Enabled, Fate sharing: No, SRLG: No, Node cost: 150
        p7 = re.compile(
            r'^Post +convergence +protection: +(?P<prot_link>\w+), +Fate +sharing: +'
            r'(?P<prot_fate>\w+), +SRLG: +(?P<prot_srlg>\w+), +Node +cost: +(?P<prot_node>\d+)$'
        )

        # Topology default (ID 0) -> Cost: 1000
        p8 = re.compile(
            r'^Topology +(?P<name>\w+) +\(ID +(?P<id>\d+)\) +-> +Cost: +(?P<metric>\d+)$'
        )

        # DR addr: 10.16.2.2, Priority: 128
        p9 = re.compile(
            r'^DR +addr: +(?P<dr_address>[\d.]+), +Priority: +(?P<router_priority>\d+)$'
        )

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

                intf_dict.update({'state': group['state']})
                intf_dict.update({'dr_id': group['dr_id']})
                intf_dict.update({'bdr_id': group['bdr_id']})
                intf_dict.update({'nbrs_count': int(group['nbrs_count'])})
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
                intf_dict.update(
                    {'authentication_type': group['authentication_type']})
                continue

            # Protection type: Post Convergence
            m = p6.match(line)
            if m:
                group = m.groupdict()
                ospf_intf_dict = intf_dict.setdefault('ospf_interface', {})
                ospf_intf_dict.update(
                    {'protection_type': group['protection_type']})
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
                topology_dict = ospf_intf_dict.setdefault(
                    'topology', {}).setdefault(group['name'], {})
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

    schema = {
        'ospf-neighbor-information': {
            'ospf-neighbor': ListOf({
                'neighbor-address': str,
                'interface-name': str,
                'ospf-neighbor-state': str,
                'neighbor-id': str,
                'neighbor-priority': str,
                'activity-timer': str
            })
        }
    }


'''
Parser for:
    * show ospf neighbor
'''


class ShowOspfNeighbor(ShowOspfNeighborSchema):
    cli_command = ['show ospf neighbor', 'show ospf neighbor instance {name}']

    def cli(self, name=None, output=None):
        if not output:
            if name:
                out = self.device.execute(self.cli_command[1].format(name=name))
            else:
                out = self.device.execute(self.cli_command[0])
        else:
            out = output

        ret_dict = {}

        # 10.189.5.94      ge-0/0/0.0             Full      10.189.5.253     128    32
        p1 = re.compile(
            r'^(?P<neighbor>\S+) +(?P<interface>\S+) +'
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

class ShowOspfNeighborInstance(ShowOspfNeighbor):
    """ Parser for:
            * show ospf neighbor instance {instance_name}
    """

    cli_command = 'show ospf neighbor instance {instance_name}'

    def cli(self, instance_name, output=None):
        if not output:
            out = self.device.execute(self.cli_command.format(
                                        instance_name=instance_name))
        else:
            out = output

        return super().cli(
            output=' ' if not out else out
            )


'''
Schema for:
    * show ospf neighbor instance all
'''


class ShowOspfNeighborInstanceAllSchema(MetaParser):
    '''
    schema = {
        'ospf-neighbor-information-all': {
        	'ospf-instance-neighbor': {
        		'ospf-instance-name': str,
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
    }
    '''

    schema = {
        'ospf-neighbor-information-all': {
            'ospf-instance-neighbor': {
                'ospf-instance-name': str,
                Optional('ospf-neighbor'): ListOf({
                    'neighbor-address': str,
                    'interface-name': str,
                    'ospf-neighbor-state': str,
                    'neighbor-id': str,
                    'neighbor-priority': str,
                    'activity-timer': str
                })
            }
        }
    }


'''
Parser for:
    * show ospf neighbor instance all
'''


class ShowOspfNeighborInstanceAll(ShowOspfNeighborInstanceAllSchema):
    cli_command = 'show ospf neighbor instance all'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # Instance: master
        p0 = re.compile(r'^Instance: +(?P<instance_name>\S+)$')

        # 10.189.5.94      ge-0/0/0.0             Full      10.189.5.253     128    32
        p1 = re.compile(
            r'^(?P<neighbor>\S+) +(?P<interface>\S+) +'
            r'(?P<state>\S+) +(?P<id>\S+) +(?P<pri>\d+) +(?P<dead>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            # Instance: master
            m = p0.match(line)
            if m:
                group = m.groupdict()
                instance = group['instance_name']
                ospf_instance_neighbor = ret_dict.setdefault('ospf-neighbor-information-all', {}).setdefault(
                    'ospf-instance-neighbor', {})
                ospf_instance_neighbor['ospf-instance-name'] = instance
                continue
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
                neighbor_list = ospf_instance_neighbor.setdefault('ospf-neighbor', [])
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

    schema = {
        'ospf-database-information': {
            "ospf-area-header": {
                "ospf-area": str
            },
            'ospf-database': ListOf({
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

        #Router   10.36.3.3          10.36.3.3          0x80004d2d    61  0x22 0xa127 2496
        #Router  *10.189.5.252     10.189.5.252     0x80001b9e  1608  0x22 0x1e2  120
        p2 = re.compile(
            r'^(?P<lsa_type>[a-zA-Z]+) *(?P<our_entry>\*)'
            r'?(?P<lsa_id>[\d\.]+) +(?P<advertising_router>'
            r'[\d\.]+) +(?P<sequence_number>\S+) +(?P<age>\d+) '
            r'+(?P<options>\S+) +(?P<checksum>\S+) +(?P<lsa_length>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            #OSPF database, Area 0.0.0.8
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ospf_database_info_dict = ret_dict.setdefault(
                    'ospf-database-information', {})

                ospf_database_info_list = ospf_database_info_dict.setdefault(
                    'ospf-database', [])
                ospf_database_info_dict2 = ospf_database_info_dict.setdefault(
                    'ospf-area-header', {})
                ospf_database_info_dict2['ospf-area'] = group['ospf_area']
                continue

            #Router   10.36.3.3          10.36.3.3          0x80004d2d    61  0x22 0xa127 2496
            #Router  *10.189.5.252     10.189.5.252     0x80001b9e  1608  0x22 0x1e2  120
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ospf_entry_dict = {}
                ospf_entry_dict['lsa-type'] = group['lsa_type']
                if group['our_entry'] == '*':
                    ospf_entry_dict['our-entry'] = True
                ospf_entry_dict['lsa-id'] = group['lsa_id']
                ospf_entry_dict['advertising-router'] = group[
                    'advertising_router']
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

    schema = {
        'ospf-database-information': {
            'ospf-database-summary': ListOf({
                Optional("@external-heading"): str,
                Optional("ospf-area"): Or(list, str),
                Optional("ospf-intf"): list,
                Optional("ospf-lsa-count"): Or(list, str),
                Optional("ospf-lsa-type"): Or(list, str)
            })
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
        p2 = re.compile(r'^(?P<area_value>\d+) +(?P<area_name>\S+) +LSAs$')

        #Externals:
        p3 = re.compile(r'^(?P<externals>\S+):$')

        #19 Extern LSAs
        p4 = re.compile(
            r'^(?P<external_value>\d+) +(?P<external_name>\S+) +LSAs$')

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
                ospf_database_info_dict = ret_dict.setdefault(
                    'ospf-database-information', {})
                ospf_database_info_list = ospf_database_info_dict.setdefault(
                    'ospf-database-summary', [None] * 3)
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
                ospf_database_entry_dict2['@external-heading'] = group[
                    'externals']
                p1 = re.compile(r'^empty$')
                p2 = re.compile(r'^empty$')
                continue

            #19 Extern LSAs
            m = p4.match(line)
            if m:
                group = m.groupdict()

                ospf_database_entry_dict2['ospf-lsa-count'] = group[
                    'external_value']
                ospf_database_entry_dict2['ospf-lsa-type'] = group[
                    'external_name']
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

                ospf_database_entry_dict1[
                    "ospf-lsa-count"] = ospf_database_entry_value_list
                ospf_database_entry_dict1[
                    "ospf-lsa-type"] = ospf_database_entry_name_list
                ospf_database_entry_dict3[
                    "ospf-area"] = ospf_database_entry_area_list
                ospf_database_entry_dict3[
                    "ospf-intf"] = ospf_database_entry_intf_list

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

    schema = {
        Optional("@xmlns:junos"): str,
        'ospf-database-information': {
            Optional("@xmlns"):
            str,
            'ospf-database': ListOf({
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
        }
    }


'''
Parser for:
    * show ospf database external extensive
'''


class ShowOspfDatabaseExternalExtensive(ShowOspfDatabaseExternalExtensiveSchema
                                        ):
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

        #Extern   0.0.0.0          10.34.2.251     0x800019e3  2728  0x22 0x6715  36
        p3 = re.compile(
            r'^(?P<lsa_type>\S+)\s+(?P<lsa_id>[\d+\.]+)\s+'
            r'(?P<advertising_router>[\d+\.]+)\s+(?P<sequence_number>\S+)'
            r'\s+(?P<age>\d+)\s+(?P<options>[\S]+)\s+(?P<checksum>[\S]+)'
            r'\s+(?P<lsa_length>\d+)$')

        #mask 0.0.0.0
        p4 = re.compile(r'^mask +(?P<address_mask>\S+)$')

        #Topology default (ID 0)
        p5 = re.compile(
            r'^Topology (?P<ospf_topology_name>\S+) +\(ID +(?P<ospf_topology_id>\d+)\)$'
        )

        #Type: 1, Metric: 1, Fwd addr: 0.0.0.0, Tag: 0.0.0.0
        p6 = re.compile(
            r'^Type: +(?P<type_value>\d+), Metric: +(?P<ospf_topology_metric>\d+), '
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
                ospf_database_info_dict = ret_dict.setdefault(
                    'ospf-database-information', {})
                ospf_database_info_list = ospf_database_info_dict.setdefault(
                    'ospf-database', [])
                ospf_database_entry_dict = {}

                ospf_database_entry_dict['@external-heading'] = group[
                    'external_heading']
                reset = True
                continue

            #Type       ID               Adv Rtr           Seq      Age  Opt  Cksum  Len
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ospf_database_entry_dict['@heading'] = group['heading']
                continue

            #Extern   0.0.0.0          10.34.2.251     0x800019e3  2728  0x22 0x6715  36
            m = p3.match(line)
            if m:
                if reset:
                    pass
                else:
                    ospf_database_entry_dict = {}

                group = m.groupdict()
                ospf_database_entry_dict['lsa-type'] = group['lsa_type']
                ospf_database_entry_dict['lsa-id'] = group['lsa_id']
                ospf_database_entry_dict['advertising-router'] = group[
                    'advertising_router']
                ospf_database_entry_dict['sequence-number'] = group[
                    'sequence_number']

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
                ospf_external_topology_dict["ospf-topology-id"] = group[
                    'ospf_topology_id']
                ospf_external_topology_dict["ospf-topology-name"] = group[
                    'ospf_topology_name']
                continue

            #Type: 1, Metric: 1, Fwd addr: 0.0.0.0, Tag: 0.0.0.0
            m = p6.match(line)
            if m:
                group = m.groupdict()
                ospf_external_topology_dict["type-value"] = group['type_value']
                ospf_external_topology_dict["ospf-topology-metric"] = group[
                    'ospf_topology_metric']
                ospf_external_topology_dict["forward-address"] = group[
                    'forward_address']
                ospf_external_topology_dict["tag"] = group['tag']

                ospf_external_dict[
                    "ospf-external-lsa-topology"] = ospf_external_topology_dict

                ospf_database_entry_dict[
                    "ospf-external-lsa"] = ospf_external_dict

            #Aging timer 00:14:32
            m = p7.match(line)
            if m:
                group = m.groupdict()
                ospf_database_info_list
                ospf_db_ext_dict = {}

                age_dict = ospf_db_ext_dict.setdefault('aging-timer', {})
                exp_dict = ospf_db_ext_dict.setdefault('expiration-time', {})
                inst_dict = ospf_db_ext_dict.setdefault(
                    'installation-time', {})
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

                lsa_dict.update({
                    '#text':
                    group['installed_time'] + ' ' + group['installed_time2']
                })
                ospf_db_ext_dict["lsa-change-count"] = group[
                    'lsa_change_count']

                ospf_database_entry_dict[
                    "ospf-database-extensive"] = ospf_db_ext_dict
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
                Optional("ospf-configured-overload-remaining-time"): str,
                "ospf-router-id": str,
                Optional("ospf-spring-overview"): {
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
                Optional("ospf-tilfa-overview"): {
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
        spring_dict = {}

        #Instance: master
        p1 = re.compile(r'^Instance: +(?P<instance_name>\S+)$')

        #Router ID: 10.189.5.252
        p2 = re.compile(r'^Router ID: +(?P<ospf_router_id>[\w\.\:\/]+)$')

        #Route table index: 0
        p3 = re.compile(
            r'^Route table index: +(?P<ospf_route_table_index>\d+)$')

        #LSA refresh time: 50 minutes
        p4 = re.compile(
            r'^LSA refresh time: +(?P<ospf_lsa_refresh_time>\d+) minutes$')

        #SPRING: Enabled
        p5 = re.compile(r'^SPRING: +(?P<ospf_spring_enabled>\S+)$')

        #SRGB Start-Label : 16000, SRGB Index-Range : 8000
        p6 = re.compile(
            r'^SRGB +Start-Label : +(?P<ospf_srgb_start_label>\d+), SRGB +Index-Range : '
            r'+(?P<ospf_srgb_index_range>\d+)$')

        #SRGB Block Allocation: Success
        p7 = re.compile(
            r'^SRGB Block Allocation: +(?P<ospf_srgb_allocation>\S+)$')

        #SRGB Start Index : 16000, SRGB Size : 8000, Label-Range: [ 16000, 23999 ]
        p8 = re.compile(
            r'^SRGB +Start +Index : +(?P<ospf_srgb_start_index>\d+), +SRGB Size : '
            r'+(?P<ospf_srgb_size>\d+), +Label-Range: \[ +(?P<ospf_srgb_first_label>\d+), '
            r'+(?P<ospf_srgb_last_label>\d+) \]$')

        #Node Segments: Enabled
        p9 = re.compile(
            r'^Node +Segments: +(?P<ospf_node_segment_enabled>\S+)$')

        #Ipv4 Index : 71
        p10 = re.compile(
            r'^Ipv4 +Index : +(?P<ospf_node_segment_ipv4_index>\d+)$')

        #Post Convergence Backup: Enabled
        p11 = re.compile(
            r'^Post +Convergence +Backup: +(?P<ospf_tilfa_enabled>\S+)$')

        #Max labels: 3, Max spf: 100, Max Ecmp Backup: 1
        p12 = re.compile(
            r'^Max +labels: +(?P<ospf_tilfa_max_labels>\d+), '
            r'Max +spf: +(?P<ospf_tilfa_max_spf>\d+), +Max +Ecmp +Backup: '
            r'+(?P<ospf_tilfa_ecmp_backup>\d+)$')

        #Area: 0.0.0.8
        p13 = re.compile(r'^Area: +(?P<ospf_area>[\w\.\:\/]+)$')

        #Stub type: Not Stub
        p14 = re.compile(r'^Stub +type: +(?P<ospf_stub_type>[\S+\s]+)$')

        #Authentication Type: None
        p15 = re.compile(
            r'^Authentication +Type: +(?P<authentication_type>\S+)$')

        #Area border routers: 0, AS boundary routers: 7
        p16 = re.compile(r'^Area +border +routers: +(?P<ospf_abr_count>\d+), +'
                         r'AS +boundary +routers: +(?P<ospf_asbr_count>\d+)$')

        #Up (in full state): 3
        p17 = re.compile(
            r'^Up +\(in full state\): +(?P<ospf_nbr_up_count>\d+)$')

        #Topology: default (ID 0)
        p18 = re.compile(
            r'^Topology: +(?P<ospf_topology_name>\S+) \(ID +(?P<ospf_topology_id>\d+)\)$'
        )

        #Prefix export count: 1
        p19 = re.compile(
            r'^Prefix +export +count: +(?P<ospf_prefix_export_count>\d+)$')

        #Full SPF runs: 173416
        p20 = re.compile(r'^Full +SPF +runs: +(?P<ospf_full_spf_count>\d+)$')

        #SPF delay: 0.200000 sec, SPF holddown: 2 sec, SPF rapid runs: 3
        p21 = re.compile(
            r'^SPF +delay: +(?P<ospf_spf_delay>[\w\.]+) +sec, +SPF +holddown: '
            r'+(?P<ospf_spf_holddown>[\w\.]+) +sec, +SPF +rapid +runs: +'
            r'(?P<ospf_spf_rapid_runs>[\w\.]+)$')

        #Backup SPF: Not Needed
        p22 = re.compile(
            r'^Backup +SPF: +(?P<ospf_backup_spf_status>[\S\s]+)$')

        # Configured overload, expires in 14 seconds
        p23 = re.compile(
            r'^Configured +overload, +expires +in +'
            r'(?P<ospf_configured_overload_remaining_time>\d+) +\S+$'
        )

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

            #Router ID: 10.189.5.252
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ospf_entry_list['ospf-router-id'] = group['ospf_router_id']
                continue

            #Route table index: 0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ospf_entry_list['ospf-route-table-index'] = group[
                    'ospf_route_table_index']
                continue

            #LSA refresh time: 50 minute
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ospf_entry_list['ospf-lsa-refresh-time'] = group[
                    'ospf_lsa_refresh_time']
                continue

            #SPRING: Enabled
            m = p5.match(line)
            if m:
                group = m.groupdict()
                spring_dict = {}
                spring_dict["ospf-spring-enabled"] = group[
                    "ospf_spring_enabled"]
                continue

            #SRGB Start-Label : 16000, SRGB Index-Range : 8000
            m = p6.match(line)
            if m:
                group = m.groupdict()
                spring_config_dict = {}
                spring_config_dict[
                    "ospf-srgb-config-block-header"] = "SRGB Config Range"
                spring_config_dict["ospf-srgb-index-range"] = group[
                    "ospf_srgb_index_range"]
                spring_config_dict["ospf-srgb-start-label"] = group[
                    "ospf_srgb_start_label"]

                spring_dict["ospf-srgb-config"] = spring_config_dict
                continue

            #SRGB Block Allocation: Success
            m = p7.match(line)
            if m:
                group = m.groupdict()
                spring_dict["ospf-srgb-allocation"] = group[
                    "ospf_srgb_allocation"]
                continue

            #SRGB Start Index : 16000, SRGB Size : 8000, Label-Range: [ 16000, 23999 ]
            m = p8.match(line)
            if m:
                group = m.groupdict()
                ospf_srgb_block_dict = {}
                ospf_srgb_block_dict["ospf-srgb-start-index"] = group[
                    "ospf_srgb_start_index"]
                ospf_srgb_block_dict["ospf-srgb-size"] = group[
                    "ospf_srgb_size"]
                ospf_srgb_block_dict["ospf-srgb-first-label"] = group[
                    "ospf_srgb_first_label"]
                ospf_srgb_block_dict["ospf-srgb-last-label"] = group[
                    "ospf_srgb_last_label"]

                spring_dict["ospf-srgb-block"] = ospf_srgb_block_dict
                continue

            #Node Segments: Enabled
            m = p9.match(line)
            if m:
                group = m.groupdict()
                spring_dict["ospf-node-segment-enabled"] = group[
                    "ospf_node_segment_enabled"]
                continue

            #Ipv4 Index : 71
            m = p10.match(line)
            if m:
                group = m.groupdict()
                node_dict = {}
                node_dict["ospf-node-segment-ipv4-index"] = group[
                    "ospf_node_segment_ipv4_index"]

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
                tilfa_dict["ospf-tilfa-max-labels"] = group[
                    "ospf_tilfa_max_labels"]
                tilfa_dict["ospf-tilfa-max-spf"] = group["ospf_tilfa_max_spf"]
                tilfa_dict["ospf-tilfa-ecmp-backup"] = group[
                    "ospf_tilfa_ecmp_backup"]

                ospf_entry_list["ospf-tilfa-overview"] = tilfa_dict
                continue

            #Area: 0.0.0.8
            m = p13.match(line)
            if m:
                group = m.groupdict()
                ospf_area_entry_dict = ospf_entry_list.setdefault(
                    'ospf-area-overview', {})
                ospf_area_entry_dict.update({'ospf-area': group['ospf_area']})
                continue

            #Stub type: Not Stub
            m = p14.match(line)
            if m:
                group = m.groupdict()
                ospf_area_entry_dict.update(
                    {'ospf-stub-type': group['ospf_stub_type']})
                continue

            #Authentication Type: None
            m = p15.match(line)
            if m:
                group = m.groupdict()
                ospf_area_entry_dict.update(
                    {'authentication-type': group['authentication_type']})
                continue

            #Area border routers: 0, AS boundary routers: 7
            m = p16.match(line)
            if m:
                group = m.groupdict()
                ospf_area_entry_dict.update(
                    {'ospf-abr-count': group['ospf_abr_count']})
                ospf_area_entry_dict.update(
                    {'ospf-asbr-count': group['ospf_asbr_count']})
                continue

            #Up (in full state): 2
            m = p17.match(line)
            if m:
                group = m.groupdict()
                ospf_area_entry_dict.setdefault('ospf-nbr-overview',\
                     {"ospf-nbr-up-count":group['ospf_nbr_up_count']})
                continue

            #Topology: default (ID 0)
            m = p18.match(line)
            if m:
                group = m.groupdict()
                ospf_topology_entry_dict = ospf_entry_list.setdefault(
                    'ospf-topology-overview', {})
                ospf_topology_entry_dict.update(
                    {'ospf-topology-name': group['ospf_topology_name']})
                ospf_topology_entry_dict.update(
                    {'ospf-topology-id': group['ospf_topology_id']})
                continue

            #Prefix export count: 1
            m = p19.match(line)
            if m:
                group = m.groupdict()
                ospf_topology_entry_dict\
                    .update({'ospf-prefix-export-count': group['ospf_prefix_export_count']})
                continue

            #Full SPF runs: 1934
            m = p20.match(line)
            if m:
                group = m.groupdict()
                ospf_topology_entry_dict.update(
                    {'ospf-full-spf-count': group['ospf_full_spf_count']})
                continue

            #SPF delay: 0.200000 sec, SPF holddown: 2 sec, SPF rapid runs: 3
            m = p21.match(line)
            if m:
                group = m.groupdict()
                ospf_topology_entry_dict.update(
                    {'ospf-spf-delay': group['ospf_spf_delay']})
                ospf_topology_entry_dict.update(
                    {'ospf-spf-holddown': group['ospf_spf_holddown']})
                ospf_topology_entry_dict.update(
                    {'ospf-spf-rapid-runs': group['ospf_spf_rapid_runs']})
                continue

            #Backup SPF: Not Needed
            m = p22.match(line)
            if m:
                group = m.groupdict()
                ospf_topology_entry_dict.update({
                    'ospf-backup-spf-status':
                    group['ospf_backup_spf_status']
                })
                if spring_dict:
                    ospf_entry_list['ospf-spring-overview'] = spring_dict
                continue

            # Configured overload, expires in 14 seconds
            m = p23.match(line)
            if m:
                group = m.groupdict()
                ospf_entry_list["ospf-configured-overload-remaining-time"] = \
                    group["ospf_configured_overload_remaining_time"]
                continue

        return ret_dict


class ShowOspfOverviewExtensive(ShowOspfOverview):
    """ Parser for:
            - show ospf overview extensive
    """

    cli_command = 'show ospf overview extensive'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command[0])
        else:
            out = output

        return super().cli(output=out)


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
                        "ospf-network-lsa": {
                            "address-mask": str,
                            "attached-router": "list",
                            "ospf-lsa-topology": {
                                "ospf-lsa-topology-link": [
                                    {
                                        "link-type-name": str,
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

    schema = {
        "ospf-database-information": {
            Optional("ospf-area-header"): {
                "ospf-area": str
            },
            "ospf-database": ListOf({
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
                    "ospf-link": ListOf({
                        "link-data": str,
                        "link-id": str,
                        "link-type-name": str,
                        "link-type-value": str,
                        "metric": str,
                        "ospf-topology-count": str
                    }),
                    Optional("ospf-lsa-topology"): {
                        "ospf-lsa-topology-link": ListOf({
                            "link-type-name": str,
                            "ospf-lsa-topology-link-metric": str,
                            "ospf-lsa-topology-link-node-id": str,
                            "ospf-lsa-topology-link-state": str
                        }),
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
                Optional("ospf-network-lsa"): {
                    "address-mask": str,
                    "attached-router": list,
                    "ospf-lsa-topology": {
                        "ospf-lsa-topology-link": ListOf({
                            "link-type-name": str,
                            "ospf-lsa-topology-link-metric": str,
                            "ospf-lsa-topology-link-node-id": str,
                            "ospf-lsa-topology-link-state": str
                        }),
                        "ospf-topology-id": str,
                        "ospf-topology-name": str
                    }
                },
                "sequence-number": str
            })
        }
    }


class ShowOspfDatabaseAdvertisingRouterSelfDetail(
        ShowOspfDatabaseAdvertisingRouterSelfDetailSchema):
    """ Parser for:
            * show ospf database advertising-router self detail
    """
    cli_command = [
        'show ospf database advertising-router self detail',
    ]

    def cli(self, output=None, ipaddress=None):
        if not output:
            out = self.device.execute(self.cli_command[0])
        else:
            out = output

        # OSPF database, Area 0.0.0.8
        p1 = re.compile(r'^OSPF +database, +Area +(?P<ospf_area>[\d\.]+)$')

        # Router  *10.189.5.252     10.189.5.252     0x80001b9e  1801  0x22 0x1e2  120
        # Network *10.145.0.3         10.36.3.3          0x80000002    65  0x22 0x9958  36
        p2 = re.compile(
            r'^(?P<lsa_type>[a-zA-Z]+)( *)(?P<lsa_id>\*?[\d\.]+)'
            r'( +)(?P<advertising_router>\S+)( +)(?P<sequence_number>\S+)( +)(?P<age>\S+)'
            r'( +)(?P<options>\S+)( +)(?P<checksum>\S+)( +)(?P<lsa_length>\S+)$'
        )

        # bits 0x2, link count 8
        p3 = re.compile(
            r'^bits +(?P<bits>\S+), +link +count +(?P<link_count>\d+)$')

        # id 10.189.5.253, data 10.189.5.93, Type PointToPoint (1)
        p4 = re.compile(
            r'^id +(?P<link_id>[\d\.]+), +data +(?P<link_data>[\d\.]+)'
            r', +Type +(?P<link_type_name>\S+) +\((?P<link_type_value>\S+)\)$')

        # Topology count: 0, Default metric: 5
        p5 = re.compile(
            r'^Topology +count: +(?P<ospf_topology_count>\d+), +Default'
            r' +metric: +(?P<metric>\d+)$')

        # Topology default (ID 0)
        p6 = re.compile(
            r'^Topology +(?P<ospf_topology_name>\S+) +\(ID +(?P<ospf_topology_id>\S+)\)$'
        )

        # Type: PointToPoint, Node ID: 10.19.198.239
        p7 = re.compile(r'^Type: +(?P<link_type_name>\S+), +Node +ID: +'
                        r'(?P<ospf_lsa_topology_link_node_id>[\d\.]+)$')

        # Metric: 1000, Bidirectional
        p8 = re.compile(r'^Metric: +(?P<ospf_lsa_topology_link_metric>\d+), +'
                        r'(?P<ospf_lsa_topology_link_state>\S+)$')

        # RtrAddr (1), length 4:
        p9 = re.compile(
            r'^(?P<tlv_type_name>[\s\S]+) +\((?P<tlv_type_value>\d+)\)'
            r', +length +(?P<tlv_length>\d+):$')

        # 10.189.5.252
        p10 = re.compile(r'^(?P<formatted_tlv_data>\S+)$')

        # Priority 0, 1000Mbps
        p11 = re.compile(r'^Priority (?P<priority_number>\d+), \S+$')

        # Local 336, Remote 0
        p12 = re.compile(r'^(?P<formatted_tlv_data>Local +\d+, +Remote +\d+)$')

        # mask 255.255.255.255
        p13 = re.compile(r'^mask +(?P<address_mask>[\d\.]+)$')

        # Topology default (ID 0)
        p14 = re.compile(r'^Topology +(?P<ospf_topology_name>\S+) +'
                         r'\(ID +(?P<ospf_topology_id>\S+)\)$')

        # Type: 1, Metric: 50, Fwd addr: 0.0.0.0, Tag: 0.0.0.0
        p15 = re.compile(
            r'^Type: +(?P<type_value>\d+), +Metric: +(?P<ospf_topology_metric>\d+)'
            r', +Fwd +addr: +(?P<forward_address>[\d\.]+), +Tag: +(?P<tag>[\d\.]+)$'
        )

        # attached router 192.168.219.235
        p16 = re.compile(r'^attached router +(?P<attached_router>\S+)$')

        ret_dict = {}

        self.lsa_type = None

        for line in out.splitlines():
            line = line.strip()

            # OSPF database, Area 0.0.0.8
            m = p1.match(line)
            if m:
                ospf_area = ret_dict.setdefault("ospf-database-information", {})\
                    .setdefault("ospf-area-header", {})

                group = m.groupdict()
                ospf_area["ospf-area"] = group["ospf_area"]
                continue

            # Router  *10.189.5.252     10.189.5.252     0x80001b9e  1801  0x22 0x1e2  120
            m = p2.match(line)
            if m:
                database_list = ret_dict.setdefault("ospf-database-information", {})\
                    .setdefault("ospf-database", [])

                group = m.groupdict()
                entry = {}
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_', '-')
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
                    last_database = ret_dict["ospf-database-information"][
                        "ospf-database"][-1]

                    group = m.groupdict()
                    last_database.setdefault("ospf-router-lsa", {})
                    last_database["ospf-router-lsa"]["bits"] = group["bits"]
                    last_database["ospf-router-lsa"]["link-count"] = group[
                        "link_count"]

                    continue

                # id 10.189.5.253, data 10.189.5.93, Type PointToPoint (1)
                m = p4.match(line)
                if m:
                    last_database = ret_dict["ospf-database-information"][
                        "ospf-database"][-1]

                    ospf_link_list = last_database.setdefault("ospf-router-lsa", {})\
                        .setdefault("ospf-link", [])

                    group = m.groupdict()
                    entry = {}
                    for group_key, group_value in group.items():
                        entry_key = group_key.replace('_', '-')
                        entry[entry_key] = group_value

                    ospf_link_list.append(entry)
                    continue

                # Topology count: 0, Default metric: 5
                m = p5.match(line)
                if m:
                    last_database = ret_dict["ospf-database-information"][
                        "ospf-database"][-1]

                    ospf_link_list = last_database.setdefault("ospf-router-lsa", {})\
                        .setdefault("ospf-link", [])
                    last_ospf_link = ospf_link_list[-1]

                    group = m.groupdict()
                    entry = last_ospf_link
                    for group_key, group_value in group.items():
                        entry_key = group_key.replace('_', '-')
                        entry[entry_key] = group_value

                    ospf_link_list.append(entry)
                    continue

                # Topology default (ID 0)
                m = p6.match(line)
                if m:
                    last_database = ret_dict["ospf-database-information"][
                        "ospf-database"][-1]

                    ospf_lsa_topology = last_database.setdefault("ospf-router-lsa", {})\
                        .setdefault("ospf-lsa-topology", {})

                    group = m.groupdict()
                    entry = ospf_lsa_topology
                    for group_key, group_value in group.items():
                        entry_key = group_key.replace('_', '-')
                        entry[entry_key] = group_value

                    continue

                # Type: PointToPoint, Node ID: 10.19.198.239
                m = p7.match(line)
                if m:
                    last_database = ret_dict["ospf-database-information"][
                        "ospf-database"][-1]

                    ospf_lsa_topology_list = last_database.setdefault("ospf-router-lsa", {})\
                        .setdefault("ospf-lsa-topology", {}).setdefault("ospf-lsa-topology-link", [])

                    group = m.groupdict()
                    entry = {}
                    for group_key, group_value in group.items():
                        entry_key = group_key.replace('_', '-')
                        entry[entry_key] = group_value

                    ospf_lsa_topology_list.append(entry)
                    continue

                # Metric: 1000, Bidirectional
                m = p8.match(line)
                if m:
                    last_database = ret_dict["ospf-database-information"][
                        "ospf-database"][-1]

                    group = m.groupdict()
                    last_link = last_database["ospf-router-lsa"][
                        "ospf-lsa-topology"]["ospf-lsa-topology-link"][-1]

                    group = m.groupdict()
                    entry = last_link
                    for group_key, group_value in group.items():
                        entry_key = group_key.replace('_', '-')
                        entry[entry_key] = group_value

                    continue

            if self.lsa_type == "OpaqArea":
                # RtrAddr (1), length 4:
                m = p9.match(line)
                if m:
                    group = m.groupdict()
                    last_database = ret_dict["ospf-database-information"][
                        "ospf-database"][-1]
                    last_database.setdefault("ospf-opaque-area-lsa",
                                             {}).setdefault("tlv-block", {})

                    if "tlv-type-name" not in last_database[
                            "ospf-opaque-area-lsa"]["tlv-block"]:
                        entry = last_database["ospf-opaque-area-lsa"][
                            "tlv-block"]
                        for group_key, group_value in group.items():
                            entry_key = group_key.replace('_', '-')
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

                # 10.189.5.252
                m = p10.match(line)
                if m:
                    group = m.groupdict()

                    last_database = ret_dict["ospf-database-information"][
                        "ospf-database"][-1]

                    if "te-subtlv" not in last_database[
                            "ospf-opaque-area-lsa"]:
                        last_database["ospf-opaque-area-lsa"]["tlv-block"][
                            "formatted-tlv-data"] = group["formatted_tlv_data"]
                    else:
                        last_database.setdefault("ospf-opaque-area-lsa", {})\
                            .setdefault("te-subtlv", {}).setdefault("formatted-tlv-data",[])\
                                .append(group["formatted_tlv_data"])

                # Priority 0, 1000Mbps
                m = p11.match(line)
                if m:
                    group = m.groupdict()

                    line += '\n'

                    last_database = ret_dict["ospf-database-information"][
                        "ospf-database"][-1]

                    if group["priority_number"] == "0":

                        last_database.setdefault("ospf-opaque-area-lsa", {})\
                            .setdefault("te-subtlv", {}).setdefault("formatted-tlv-data",[]).append(line)
                    else:

                        last_database["ospf-opaque-area-lsa"]["te-subtlv"][
                            "formatted-tlv-data"][-1] += line

                    continue

                # Local 336, Remote 0
                m = p12.match(line)
                if m:
                    group = m.groupdict()

                    last_database = ret_dict["ospf-database-information"][
                        "ospf-database"][-1]

                    if "te-subtlv" not in last_database[
                            "ospf-opaque-area-lsa"]:
                        last_database["ospf-opaque-area-lsa"][
                            "formatted-tlv-data"] = group["formatted_tlv_data"]
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

                    last_database = ret_dict["ospf-database-information"][
                        "ospf-database"][-1]
                    last_database.setdefault("ospf-external-lsa", {})\
                        .setdefault("address-mask", group['address_mask'])
                    continue

                # Topology default (ID 0)
                m = p14.match(line)
                if m:
                    group = m.groupdict()

                    last_database = ret_dict["ospf-database-information"][
                        "ospf-database"][-1]

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

            if self.lsa_type == "Network":
                # mask 255.255.255.255
                m = p13.match(line)
                if m:
                    group = m.groupdict()

                    last_database = ret_dict["ospf-database-information"][
                        "ospf-database"][-1]
                    last_database.setdefault("ospf-network-lsa", {})\
                        .setdefault("address-mask", group['address_mask'])
                    continue

                # attached router 192.168.219.235
                m = p16.match(line)
                if m:
                    group = m.groupdict()
                    last_database = ret_dict["ospf-database-information"][
                        "ospf-database"][-1]

                    last_database.setdefault("ospf-network-lsa", {})\
                        .setdefault("attached-router", []).append(group['attached_router'])
                    continue

                # Topology default (ID 0)
                m = p6.match(line)
                if m:
                    last_database = ret_dict["ospf-database-information"][
                        "ospf-database"][-1]

                    ospf_lsa_topology = last_database.setdefault("ospf-network-lsa", {})\
                        .setdefault("ospf-lsa-topology", {})

                    group = m.groupdict()
                    entry = ospf_lsa_topology
                    for group_key, group_value in group.items():
                        entry_key = group_key.replace('_', '-')
                        entry[entry_key] = group_value

                    continue

                # Type: PointToPoint, Node ID: 10.19.198.239
                m = p7.match(line)
                if m:
                    last_database = ret_dict["ospf-database-information"][
                        "ospf-database"][-1]

                    ospf_lsa_topology_list = last_database.setdefault("ospf-network-lsa", {})\
                        .setdefault("ospf-lsa-topology", {}).setdefault("ospf-lsa-topology-link", [])

                    group = m.groupdict()
                    entry = {}
                    for group_key, group_value in group.items():
                        entry_key = group_key.replace('_', '-')
                        entry[entry_key] = group_value

                    ospf_lsa_topology_list.append(entry)
                    continue

                # Metric: 1000, Bidirectional
                m = p8.match(line)
                if m:
                    last_database = ret_dict["ospf-database-information"][
                        "ospf-database"][-1]

                    group = m.groupdict()
                    last_link = last_database["ospf-network-lsa"][
                        "ospf-lsa-topology"]["ospf-lsa-topology-link"][-1]

                    group = m.groupdict()
                    entry = last_link
                    for group_key, group_value in group.items():
                        entry_key = group_key.replace('_', '-')
                        entry[entry_key] = group_value

                    continue
        return ret_dict


class ShowOspfDatabaseExtensiveSchema(MetaParser):
    """ Schema for:
            * show ospf database extensive
            * show ospf database advertising-router {ipaddress} extensive
            * show ospf database {data_type} extensive
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
                    Optional("ospf-network-lsa"): {
                        "address-mask": str,
                        "attached-router": list,
                        "ospf-lsa-topology": {
                            "ospf-lsa-topology-link": {
                                "link-type-name": str,
                                "ospf-lsa-topology-link-metric": str,
                                "ospf-lsa-topology-link-node-id": str,
                                "ospf-lsa-topology-link-state": str
                            },
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
                        "ospf-link": {
                            "link-data": str,
                            "link-id": str,
                            "link-type-name": str,
                            "link-type-value": str,
                            "metric": str,
                            "ospf-topology-count": str
                        },
                        "ospf-lsa-topology": {
                            "ospf-lsa-topology-link": {
                                "link-type-name": str,
                                "ospf-lsa-topology-link-metric": str,
                                "ospf-lsa-topology-link-node-id": str,
                                "ospf-lsa-topology-link-state": str
                            },
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
                }
            ]
        }
    }'''

    schema = {
        "ospf-database-information": {
            "ospf-area-header": {
                "ospf-area": str
            },
            "ospf-database": ListOf({
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
                        "ospf-lsa-topology-link": ListOf({
                            "link-type-name": str,
                            "ospf-lsa-topology-link-metric": str,
                            "ospf-lsa-topology-link-node-id": str,
                            "ospf-lsa-topology-link-state": str
                        }),
                        "ospf-topology-id": str,
                        "ospf-topology-name": str
                    }
                },
                "ospf-database-extensive": {
                    "aging-timer": {
                        "#text": str
                    },
                    Optional("expiration-time"): {
                        "#text": str
                    },
                    Optional("installation-time"): {
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
                        Optional("#text"): str
                    },
                    Optional("database-entry-state"): str
                },
                Optional("ospf-router-lsa"): {
                    "bits": str,
                    "link-count": str,
                    "ospf-link": ListOf({
                        "link-data": str,
                        "link-id": str,
                        "link-type-name": str,
                        "link-type-value": str,
                        "metric": str,
                        "ospf-topology-count": str
                    }),
                    Optional("ospf-lsa-topology"): {
                        "ospf-lsa-topology-link": ListOf({
                            "link-type-name": str,
                            "ospf-lsa-topology-link-metric": str,
                            "ospf-lsa-topology-link-node-id": str,
                            "ospf-lsa-topology-link-state": str
                        }),
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
                Optional("ospf-summary-lsa"): {
                    "address-mask": str,
                    "ospf-summary-lsa-topology": {
                        "ospf-topology-name": str,
                        "ospf-topology-id": str,
                        "ospf-topology-metric": str,
                    }
                },
                "sequence-number": str
            })
        }
    }


class ShowOspfDatabaseExtensive(ShowOspfDatabaseExtensiveSchema):
    """ Parser for:
            * show ospf database extensive
            * show ospf database {data_type} extensive
    """
    cli_command = [
        'show ospf database extensive',
        'show ospf database {data_type} extensive'
        ]

    def cli(self, data_type=None, output=None):
        if not output:
            if data_type:
                out = self.device.execute(self.cli_command[1].format(
                    data_type=data_type
                ))
            else:
                out = self.device.execute(self.cli_command[0])
        else:
            out = output

        # OSPF database, Area 0.0.0.8
        p1 = re.compile(r'^OSPF +database, +Area +(?P<ospf_area>[\d\.]+)$')

        # Router  *10.189.5.252     10.189.5.252     0x80001b9e  1801  0x22 0x1e2  120
        p2 = re.compile(
            r'^(?P<lsa_type>[a-zA-Z]+)( *)(?P<lsa_id>\*?[\d\.]+)'
            r'( +)(?P<advertising_router>\S+)( +)(?P<sequence_number>\S+)( +)(?P<age>\S+)'
            r'( +)(?P<options>\S+)( +)(?P<checksum>\S+)( +)(?P<lsa_length>\S+)$'
        )

        # bits 0x2, link count 8
        p3 = re.compile(
            r'^bits +(?P<bits>\S+), +link +count +(?P<link_count>\d+)$')

        # id 10.189.5.253, data 10.189.5.93, Type PointToPoint (1)
        p4 = re.compile(
            r'^id +(?P<link_id>[\d\.]+), +data +(?P<link_data>[\d\.]+)'
            r', +Type +(?P<link_type_name>\S+) +\((?P<link_type_value>\S+)\)$')

        # Topology count: 0, Default metric: 5
        p5 = re.compile(
            r'^Topology +count: +(?P<ospf_topology_count>\d+), +Default'
            r' +metric: +(?P<metric>\d+)$')

        # Topology default (ID 0)
        p6 = re.compile(
            r'^Topology +(?P<ospf_topology_name>\S+) +\(ID +(?P<ospf_topology_id>\S+)\)$'
        )

        # Type: PointToPoint, Node ID: 10.19.198.239
        p7 = re.compile(r'^Type: +(?P<link_type_name>\S+), +Node +ID: +'
                        r'(?P<ospf_lsa_topology_link_node_id>[\d\.]+)$')

        # Metric: 1000, Bidirectional
        p8 = re.compile(r'^Metric: +(?P<ospf_lsa_topology_link_metric>\d+), +'
                        r'(?P<ospf_lsa_topology_link_state>\S+)$')

        # RtrAddr (1), length 4:
        p9 = re.compile(
            r'^(?P<tlv_type_name>[\s\S]+) +\((?P<tlv_type_value>\d+)\)'
            r', +length +(?P<tlv_length>\d+):$')

        # 10.189.5.252
        p10 = re.compile(r'^(?P<formatted_tlv_data>\S+)$')

        # Priority 0, 1000Mbps
        p11 = re.compile(r'^Priority (?P<priority_number>\d+), \S+$')

        # Local 336, Remote 0
        p12 = re.compile(r'^(?P<formatted_tlv_data>Local +\d+, +Remote +\d+)$')

        # mask 255.255.255.255
        p13 = re.compile(r'^mask +(?P<address_mask>[\d\.]+)$')

        # Topology default (ID 0)
        p14 = re.compile(
            r'^Topology +(?P<ospf_topology_name>\S+) +\(ID +(?P<ospf_topology_id>\S+)\)$'
        )

        # Topology default (ID 0) -> Metric: 0
        p14_1 = re.compile(
            r'^Topology +(?P<ospf_topology_name>\S+) +\(ID +(?P<ospf_topology_id>\S+)\) +'
            r'-> +Metric: +(?P<ospf_topology_metric>\d+)$'
        )

        # Type: 1, Metric: 50, Fwd addr: 0.0.0.0, Tag: 0.0.0.0
        p15 = re.compile(
            r'^Type: +(?P<type_value>\d+), +Metric: +(?P<ospf_topology_metric>\d+)'
            r', +Fwd +addr: +(?P<forward_address>[\d\.]+), +Tag: +(?P<tag>[\d\.]+)$'
        )

        # Aging timer 00:18:16
        p16 = re.compile(r"^Aging timer +(?P<aging_timer>(\S+ ){0,1}[\d\:]+)$")

        # Installed 00:10:20 ago, expires in 00:49:31, sent 00:10:18 ago
        # Installed 00:10:20 ago, expires in 00:49:31
        p17 = re.compile(
            r"^Installed +(?P<installation_time>(\S+ ){0,1}[\d\:]+) +ago, +expires +in +"
            r"(?P<expiration_time>(\S+ ){0,1}[\d\:]+)(, +sent +(?P<send_time>(\S+ ){0,1}[\d\:]+) +ago)?$"
        )

        # Last changed 2w6d 04:50:31 ago, Change count: 196
        p18 = re.compile(
            r"^Last +changed +(?P<lsa_changed_time>(\S+ +){0,1}[\d\:]+) +ago, +Change +"
            r"count: +(?P<lsa_change_count>\d+)(, +(?P<database_entry_state>\S+)"
            r"(, +TE +Link +ID: +(?P<database_telink_id>\S+)))?$")

        # Gen timer 00:49:49
        p19 = re.compile(r"^Gen +timer +(?P<generation_timer>\S+)$")

        # attached router 10.169.14.240
        p20 = re.compile(r'^attached +router +(?P<attached_router>[\d\.]+)$')

        ret_dict = {}

        self.lsa_type = None

        for line in out.splitlines():
            line = line.strip()

            # OSPF database, Area 0.0.0.8
            m = p1.match(line)
            if m:
                ospf_area = ret_dict.setdefault("ospf-database-information", {})\
                    .setdefault("ospf-area-header", {})

                group = m.groupdict()
                ret_dict["ospf-database-information"]["ospf-area-header"]["ospf-area"]\
                     = group["ospf_area"]
                continue

            # Router  *10.189.5.252     10.189.5.252     0x80001b9e  1801  0x22 0x1e2  120
            m = p2.match(line)
            if m:
                database_list = ret_dict.setdefault("ospf-database-information", {})\
                    .setdefault("ospf-database", [])

                group = m.groupdict()
                entry = {}
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_', '-')
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
                    last_database = ret_dict["ospf-database-information"][
                        "ospf-database"][-1]

                    group = m.groupdict()
                    last_database.setdefault("ospf-router-lsa", {})
                    last_database["ospf-router-lsa"]["bits"] = group["bits"]
                    last_database["ospf-router-lsa"]["link-count"] = group[
                        "link_count"]

                    continue

                # id 10.189.5.253, data 10.189.5.93, Type PointToPoint (1)
                m = p4.match(line)
                if m:
                    last_database = ret_dict["ospf-database-information"][
                        "ospf-database"][-1]

                    ospf_link_list = last_database.setdefault("ospf-router-lsa", {})\
                        .setdefault("ospf-link", [])

                    group = m.groupdict()
                    entry = {}
                    for group_key, group_value in group.items():
                        entry_key = group_key.replace('_', '-')
                        entry[entry_key] = group_value

                    ospf_link_list.append(entry)
                    continue

                # Topology count: 0, Default metric: 5
                m = p5.match(line)
                if m:
                    last_database = ret_dict["ospf-database-information"][
                        "ospf-database"][-1]

                    ospf_link_list = last_database.setdefault("ospf-router-lsa", {})\
                        .setdefault("ospf-link", [])
                    last_ospf_link = ospf_link_list[-1]

                    group = m.groupdict()
                    entry = last_ospf_link
                    for group_key, group_value in group.items():
                        entry_key = group_key.replace('_', '-')
                        entry[entry_key] = group_value

                    ospf_link_list.append(entry)
                    continue

                # Topology default (ID 0)
                m = p6.match(line)
                if m:
                    last_database = ret_dict["ospf-database-information"][
                        "ospf-database"][-1]

                    ospf_lsa_topology = last_database.setdefault("ospf-router-lsa", {})\
                        .setdefault("ospf-lsa-topology", {})

                    group = m.groupdict()
                    entry = ospf_lsa_topology
                    for group_key, group_value in group.items():
                        entry_key = group_key.replace('_', '-')
                        entry[entry_key] = group_value

                    continue

                # Type: PointToPoint, Node ID: 10.19.198.239
                m = p7.match(line)
                if m:
                    last_database = ret_dict["ospf-database-information"][
                        "ospf-database"][-1]

                    ospf_lsa_topology_list = last_database.setdefault("ospf-router-lsa", {})\
                        .setdefault("ospf-lsa-topology", {}).setdefault("ospf-lsa-topology-link", [])

                    group = m.groupdict()
                    entry = {}
                    for group_key, group_value in group.items():
                        entry_key = group_key.replace('_', '-')
                        entry[entry_key] = group_value

                    ospf_lsa_topology_list.append(entry)
                    continue

                # Metric: 1000, Bidirectional
                m = p8.match(line)
                if m:
                    last_database = ret_dict["ospf-database-information"][
                        "ospf-database"][-1]

                    group = m.groupdict()
                    last_link = last_database["ospf-router-lsa"]["ospf-lsa-topology"]\
                        ["ospf-lsa-topology-link"][-1]

                    group = m.groupdict()
                    entry = last_link
                    for group_key, group_value in group.items():
                        entry_key = group_key.replace('_', '-')
                        entry[entry_key] = group_value

                    continue

                # Aging timer 00:18:16
                m = p16.match(line)
                if m:
                    last_database = ret_dict["ospf-database-information"][
                        "ospf-database"][-1]
                    last_database.setdefault("ospf-database-extensive",
                                             {}).setdefault("aging-timer", {})

                    group = m.groupdict()
                    last_database["ospf-database-extensive"]["aging-timer"][
                        "#text"] = group["aging_timer"]

                    continue

                # Installed 00:10:20 ago, expires in 00:49:31, sent 00:10:18 ago
                m = p17.match(line)
                if m:
                    last_entry = ret_dict["ospf-database-information"][
                        "ospf-database"][-1]

                    last_entry.setdefault("ospf-database-extensive", {})\
                        .setdefault("expiration-time", {})
                    last_entry.setdefault("ospf-database-extensive", {})\
                        .setdefault("installation-time", {})


                    group = m.groupdict()
                    last_entry["ospf-database-extensive"]["expiration-time"]["#text"]\
                     = group["expiration_time"]
                    last_entry["ospf-database-extensive"]["installation-time"]["#text"]\
                     = group["installation_time"]
                    if group.get('send_time'):
                        last_entry.setdefault("ospf-database-extensive", {}) \
                            .setdefault("send-time", {})
                        last_entry["ospf-database-extensive"]["send-time"]["#text"]\
                         = group["send_time"]

                    continue

                # Last changed 2w6d 04:50:31 ago, Change count: 196
                m = p18.match(line)  # lsa_changed_time , lsa_changed_count
                if m:
                    last_entry = ret_dict["ospf-database-information"][
                        "ospf-database"][-1]

                    last_entry.setdefault("ospf-database-extensive",
                                          {}).setdefault(
                                              "lsa-changed-time", {})

                    group = m.groupdict()
                    last_entry["ospf-database-extensive"]["lsa-changed-time"]["#text"]\
                        = group["lsa_changed_time"]
                    last_entry["ospf-database-extensive"][
                        "lsa-change-count"] = group["lsa_change_count"]

                    continue

                # Gen timer 00:49:49
                m = p19.match(line)
                if m:
                    last_database = ret_dict["ospf-database-information"][
                        "ospf-database"][-1]

                    last_database.setdefault("ospf-database-extensive", {})\
                        .setdefault("generation-timer", {})

                    group = m.groupdict()
                    last_database["ospf-database-extensive"][
                        "generation-timer"]["#text"] = group[
                            "generation_timer"]

                    continue

            if self.lsa_type == "Network":
                # mask 255.255.255.255
                m = p13.match(line)
                if m:
                    group = m.groupdict()

                    last_database = ret_dict["ospf-database-information"][
                        "ospf-database"][-1]
                    last_database.setdefault("ospf-network-lsa", {})\
                        .setdefault("address-mask", group['address_mask'])
                    continue

                # attached router 10.169.14.240
                m = p20.match(line)
                if m:
                    group = m.groupdict()

                    last_database = ret_dict["ospf-database-information"][
                        "ospf-database"][-1]

                    last_database.setdefault("ospf-network-lsa", {})\
                        .setdefault("attached-router", []).append(group['attached_router'])

                    continue

                # Topology default (ID 0)
                m = p6.match(line)
                if m:
                    last_database = ret_dict["ospf-database-information"][
                        "ospf-database"][-1]

                    ospf_lsa_topology = last_database.setdefault("ospf-network-lsa", {})\
                        .setdefault("ospf-lsa-topology", {})

                    group = m.groupdict()
                    entry = ospf_lsa_topology
                    for group_key, group_value in group.items():
                        entry_key = group_key.replace('_', '-')
                        entry[entry_key] = group_value

                    continue

                # Type: PointToPoint, Node ID: 10.19.198.239
                m = p7.match(line)
                if m:
                    last_database = ret_dict["ospf-database-information"][
                        "ospf-database"][-1]

                    ospf_lsa_topology_list = last_database.setdefault("ospf-network-lsa", {})\
                        .setdefault("ospf-lsa-topology", {}).setdefault("ospf-lsa-topology-link", [])

                    group = m.groupdict()
                    entry = {}
                    for group_key, group_value in group.items():
                        entry_key = group_key.replace('_', '-')
                        entry[entry_key] = group_value

                    ospf_lsa_topology_list.append(entry)
                    continue

                # Metric: 1000, Bidirectional
                m = p8.match(line)
                if m:
                    last_database = ret_dict["ospf-database-information"][
                        "ospf-database"][-1]

                    group = m.groupdict()
                    last_link = last_database["ospf-network-lsa"]["ospf-lsa-topology"]\
                        ["ospf-lsa-topology-link"][-1]

                    group = m.groupdict()
                    entry = last_link
                    for group_key, group_value in group.items():
                        entry_key = group_key.replace('_', '-')
                        entry[entry_key] = group_value

                    continue

                # Aging timer 00:18:16
                m = p16.match(line)
                if m:
                    last_database = ret_dict["ospf-database-information"][
                        "ospf-database"][-1]
                    last_database.setdefault("ospf-database-extensive",
                                             {}).setdefault("aging-timer", {})

                    group = m.groupdict()
                    last_database["ospf-database-extensive"]["aging-timer"][
                        "#text"] = group["aging_timer"]

                    continue

                # Installed 00:10:20 ago, expires in 00:49:31, sent 00:10:18 ago
                m = p17.match(line)
                if m:
                    last_entry = ret_dict["ospf-database-information"][
                        "ospf-database"][-1]

                    last_entry.setdefault("ospf-database-extensive", {})\
                        .setdefault("expiration-time", {})
                    last_entry.setdefault("ospf-database-extensive", {})\
                        .setdefault("installation-time", {})
                    # last_entry.setdefault("ospf-database-extensive", {})\
                    #     .setdefault("send-time", {})

                    group = m.groupdict()
                    last_entry["ospf-database-extensive"]["expiration-time"]\
                        ["#text"] = group["expiration_time"]
                    last_entry["ospf-database-extensive"]["installation-time"]\
                        ["#text"] = group["installation_time"]
                    # last_entry["ospf-database-extensive"]["send-time"]\
                    #     ["#text"] = group["send_time"]
                    
                    if group.get('send_time'):
                        last_entry.setdefault("ospf-database-extensive", {}) \
                            .setdefault("send-time", {})
                        last_entry["ospf-database-extensive"]["send-time"]["#text"]\
                         = group["send_time"]

                    continue

                # Last changed 2w6d 04:50:31 ago, Change count: 196
                m = p18.match(line)  # lsa_changed_time , lsa_changed_count
                if m:
                    last_entry = ret_dict["ospf-database-information"][
                        "ospf-database"][-1]

                    last_entry.setdefault("ospf-database-extensive", {})\
                        .setdefault("lsa-changed-time", {})

                    group = m.groupdict()
                    last_entry["ospf-database-extensive"]["lsa-changed-time"]["#text"]\
                        = group["lsa_changed_time"]
                    last_entry["ospf-database-extensive"]["lsa-change-count"]\
                         = group["lsa_change_count"]

                    continue

                # Gen timer 00:49:49
                m = p19.match(line)
                if m:
                    last_database = ret_dict["ospf-database-information"][
                        "ospf-database"][-1]

                    last_database.setdefault("ospf-database-extensive", {})\
                        .setdefault("generation-timer", {})

                    group = m.groupdict()
                    last_database["ospf-database-extensive"]["generation-timer"]\
                        ["#text"] = group["generation_timer"]

                    continue

            if self.lsa_type == "OpaqArea":
                # RtrAddr (1), length 4:
                m = p9.match(line)
                if m:
                    group = m.groupdict()
                    last_database = ret_dict["ospf-database-information"][
                        "ospf-database"][-1]
                    last_database.setdefault("ospf-opaque-area-lsa",
                                             {}).setdefault("tlv-block", {})

                    if "tlv-type-name" not in last_database[
                            "ospf-opaque-area-lsa"]["tlv-block"]:
                        entry = last_database["ospf-opaque-area-lsa"][
                            "tlv-block"]
                        for group_key, group_value in group.items():
                            entry_key = group_key.replace('_', '-')
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

                # 10.189.5.252
                m = p10.match(line)
                if m:
                    group = m.groupdict()

                    last_database = ret_dict["ospf-database-information"][
                        "ospf-database"][-1]

                    if "te-subtlv" not in last_database[
                            "ospf-opaque-area-lsa"]:
                        last_database["ospf-opaque-area-lsa"]["tlv-block"]\
                            ["formatted-tlv-data"] = group["formatted_tlv_data"]
                    else:
                        last_database.setdefault("ospf-opaque-area-lsa", {})\
                            .setdefault("te-subtlv", {}).setdefault("formatted-tlv-data",[])\
                                .append(group["formatted_tlv_data"])

                    continue

                # Priority 0, 1000Mbps
                m = p11.match(line)
                if m:
                    group = m.groupdict()

                    line += '\n'

                    last_database = ret_dict["ospf-database-information"][
                        "ospf-database"][-1]

                    if group["priority_number"] == "0":

                        last_database.setdefault("ospf-opaque-area-lsa", {})\
                            .setdefault("te-subtlv", {}).setdefault("formatted-tlv-data",[])\
                                .append(line)
                    else:

                        last_database["ospf-opaque-area-lsa"]["te-subtlv"]\
                            ["formatted-tlv-data"][-1] += line

                    continue

                # Local 336, Remote 0
                m = p12.match(line)
                if m:
                    group = m.groupdict()

                    last_database = ret_dict["ospf-database-information"][
                        "ospf-database"][-1]

                    if "te-subtlv" not in last_database[
                            "ospf-opaque-area-lsa"]:
                        last_database["ospf-opaque-area-lsa"]["formatted-tlv-data"]\
                             = group["formatted_tlv_data"]
                    else:
                        last_database.setdefault("ospf-opaque-area-lsa", {})\
                            .setdefault("te-subtlv", {}).setdefault("formatted-tlv-data",[])\
                                .append(group["formatted_tlv_data"])

                    continue

                # Aging timer 00:18:16
                m = p16.match(line)
                if m:
                    last_database = ret_dict["ospf-database-information"][
                        "ospf-database"][-1]
                    last_database.setdefault("ospf-database-extensive",
                                             {}).setdefault("aging-timer", {})

                    group = m.groupdict()
                    last_database["ospf-database-extensive"]["aging-timer"][
                        "#text"] = group["aging_timer"]

                    continue

                # Installed 00:10:20 ago, expires in 00:49:31, sent 00:10:18 ago
                m = p17.match(line)
                if m:
                    last_entry = ret_dict["ospf-database-information"][
                        "ospf-database"][-1]

                    last_entry.setdefault("ospf-database-extensive", {})\
                        .setdefault("expiration-time", {})
                    last_entry.setdefault("ospf-database-extensive", {})\
                        .setdefault("installation-time", {})
                    # last_entry.setdefault("ospf-database-extensive", {})\
                    #     .setdefault("send-time", {})

                    group = m.groupdict()
                    last_entry["ospf-database-extensive"]["expiration-time"]\
                        ["#text"] = group["expiration_time"]
                    last_entry["ospf-database-extensive"]["installation-time"]\
                        ["#text"] = group["installation_time"]
                    # last_entry["ospf-database-extensive"]["send-time"]["#text"]\
                    #  = group["send_time"]
                    
                    if group.get('send_time'):
                        last_entry.setdefault("ospf-database-extensive", {}) \
                            .setdefault("send-time", {})
                        last_entry["ospf-database-extensive"]["send-time"]["#text"]\
                         = group["send_time"]

                    continue

                # Last changed 3w1d 21:01:25 ago, Change count: 4, Ours, TE Link ID: 2147483651
                m = p18.match(line)  # lsa_changed_time , lsa_changed_count
                if m:
                    last_entry = ret_dict["ospf-database-information"][
                        "ospf-database"][-1]

                    last_entry.setdefault("ospf-database-extensive",
                                          {}).setdefault(
                                              "lsa-changed-time", {})

                    group = m.groupdict()
                    last_entry["ospf-database-extensive"]["lsa-changed-time"]["#text"]\
                        = group["lsa_changed_time"]
                    last_entry["ospf-database-extensive"][
                        "lsa-change-count"] = group["lsa_change_count"]

                    continue

                # Gen timer 00:49:49
                m = p19.match(line)
                if m:
                    last_database = ret_dict["ospf-database-information"][
                        "ospf-database"][-1]

                    last_database.setdefault("ospf-database-extensive", {})\
                        .setdefault("generation-timer", {})

                    group = m.groupdict()
                    last_database["ospf-database-extensive"][
                        "generation-timer"]["#text"] = group[
                            "generation_timer"]

                    continue

            if self.lsa_type == "Extern":

                # mask 255.255.255.255
                m = p13.match(line)
                if m:
                    group = m.groupdict()

                    last_database = ret_dict["ospf-database-information"][
                        "ospf-database"][-1]
                    last_database.setdefault("ospf-external-lsa", {})\
                        .setdefault("address-mask", group['address_mask'])
                    continue

                # Topology default (ID 0)
                m = p14.match(line)
                if m:
                    group = m.groupdict()

                    last_database = ret_dict["ospf-database-information"][
                        "ospf-database"][-1]

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
                    last_database = ret_dict["ospf-database-information"][
                        "ospf-database"][-1]
                    last_database.setdefault("ospf-database-extensive",
                                             {}).setdefault("aging-timer", {})

                    group = m.groupdict()
                    last_database["ospf-database-extensive"]["aging-timer"][
                        "#text"] = group["aging_timer"]

                    continue

                # Installed 00:10:20 ago, expires in 00:49:31, sent 00:10:18 ago
                m = p17.match(line)
                if m:
                    last_entry = ret_dict["ospf-database-information"][
                        "ospf-database"][-1]

                    last_entry.setdefault("ospf-database-extensive", {})\
                        .setdefault("expiration-time", {})
                    last_entry.setdefault("ospf-database-extensive", {})\
                        .setdefault("installation-time", {})
                    # last_entry.setdefault("ospf-database-extensive", {})\
                    #     .setdefault("send-time", {})

                    group = m.groupdict()
                    last_entry["ospf-database-extensive"]["expiration-time"]\
                        ["#text"] = group["expiration_time"]
                    last_entry["ospf-database-extensive"]["installation-time"]\
                        ["#text"] = group["installation_time"]
                    # if group["send_time"]:
                    #     last_entry["ospf-database-extensive"]["send-time"]["#text"]\
                    #     = group["send_time"]
                    
                    if group.get('send_time'):
                        last_entry.setdefault("ospf-database-extensive", {}) \
                            .setdefault("send-time", {})
                        last_entry["ospf-database-extensive"]["send-time"]["#text"]\
                         = group["send_time"]


                    continue

                # Last changed 2w6d 04:50:31 ago, Change count: 196
                m = p18.match(line)  # lsa_changed_time , lsa_changed_count
                if m:
                    last_entry = ret_dict["ospf-database-information"][
                        "ospf-database"][-1]

                    last_entry.setdefault("ospf-database-extensive", {})\
                        .setdefault("lsa-changed-time", {})

                    group = m.groupdict()
                    last_entry["ospf-database-extensive"]["lsa-changed-time"]["#text"]\
                        = group["lsa_changed_time"]
                    last_entry["ospf-database-extensive"]["lsa-change-count"] = \
                        group["lsa_change_count"]

                    continue

                # Gen timer 00:49:49
                m = p19.match(line)
                if m:
                    last_database = ret_dict["ospf-database-information"][
                        "ospf-database"][-1]

                    last_database.setdefault("ospf-database-extensive", {})\
                        .setdefault("generation-timer", {})

                    group = m.groupdict()
                    last_database["ospf-database-extensive"]["generation-timer"]\
                        ["#text"] = group["generation_timer"]

                    continue

            if self.lsa_type == "Summary":
                
                # mask 255.255.255.255
                m = p13.match(line)
                if m:
                    group = m.groupdict()

                    last_database = ret_dict["ospf-database-information"][
                        "ospf-database"][-1]
                    last_database.setdefault("ospf-summary-lsa", {})\
                        .setdefault("address-mask", group['address_mask'])
                    continue

                # Topology default (ID 0) -> Metric: 0
                m = p14_1.match(line)
                if m:
                    group = m.groupdict()
                    last_database = ret_dict["ospf-database-information"][
                            "ospf-database"][-1]

                    last_database.setdefault("ospf-summary-lsa", {})\
                            .setdefault("ospf-summary-lsa-topology", {})\
                                .setdefault("ospf-topology-name", group["ospf_topology_name"])

                    last_database.setdefault("ospf-summary-lsa", {})\
                        .setdefault("ospf-summary-lsa-topology", {})\
                            .setdefault("ospf-topology-id", group["ospf_topology_id"])

                    last_database.setdefault("ospf-summary-lsa", {})\
                        .setdefault("ospf-summary-lsa-topology", {})\
                            .setdefault("ospf-topology-metric", group["ospf_topology_metric"])
                    
                    continue

                # Aging timer 00:18:16
                m = p16.match(line)
                if m:
                    last_database = ret_dict["ospf-database-information"][
                        "ospf-database"][-1]
                    last_database.setdefault("ospf-database-extensive",
                                             {}).setdefault("aging-timer", {})

                    group = m.groupdict()
                    last_database["ospf-database-extensive"]["aging-timer"][
                        "#text"] = group["aging_timer"]

                    continue

                # Installed 00:10:20 ago, expires in 00:49:31, sent 00:10:18 ago
                m = p17.match(line)
                if m:
                    last_entry = ret_dict["ospf-database-information"][
                        "ospf-database"][-1]

                    last_entry.setdefault("ospf-database-extensive", {})\
                        .setdefault("expiration-time", {})
                    last_entry.setdefault("ospf-database-extensive", {})\
                        .setdefault("installation-time", {})
                    # last_entry.setdefault("ospf-database-extensive", {})\
                    #     .setdefault("send-time", {})

                    group = m.groupdict()
                    last_entry["ospf-database-extensive"]["expiration-time"]\
                        ["#text"] = group["expiration_time"]
                    last_entry["ospf-database-extensive"]["installation-time"]\
                        ["#text"] = group["installation_time"]
                    # last_entry["ospf-database-extensive"]["send-time"]["#text"]\
                    #  = group["send_time"]
                    
                    if group.get('send_time'):
                        last_entry.setdefault("ospf-database-extensive", {}) \
                            .setdefault("send-time", {})
                        last_entry["ospf-database-extensive"]["send-time"]["#text"]\
                         = group["send_time"]

                    continue

                # Last changed 2w6d 04:50:31 ago, Change count: 196
                m = p18.match(line)  # lsa_changed_time , lsa_changed_count
                if m:
                    last_entry = ret_dict["ospf-database-information"][
                        "ospf-database"][-1]

                    last_entry.setdefault("ospf-database-extensive", {})\
                        .setdefault("lsa-changed-time", {})

                    group = m.groupdict()
                    last_entry["ospf-database-extensive"]["lsa-changed-time"]["#text"]\
                        = group["lsa_changed_time"]
                    last_entry["ospf-database-extensive"]["lsa-change-count"] = \
                        group["lsa_change_count"]

                    continue

                # Gen timer 00:49:49
                m = p19.match(line)
                if m:
                    last_database = ret_dict["ospf-database-information"][
                        "ospf-database"][-1]

                    last_database.setdefault("ospf-database-extensive", {})\
                        .setdefault("generation-timer", {})

                    group = m.groupdict()
                    last_database["ospf-database-extensive"]["generation-timer"]\
                        ["#text"] = group["generation_timer"]

                    continue

        return ret_dict

class ShowOspfDatabaseAdvertisingRouterExtensive(ShowOspfDatabaseExtensive):
    """ Parser for:
            * show ospf database advertising-router {ipaddress} extensive
    """

    cli_command = 'show ospf database advertising-router {ipaddress} extensive'

    def cli(self, ipaddress, output=None):
        if not output:
            out = self.device.execute(self.cli_command.format(ipaddress=ipaddress))
        else:
            out = output
        return super().cli(output=out)

class ShowOspfNeighborExtensiveSchema(MetaParser):
    """ Schema for:
            * show ospf neighbor extensive
    """

    schema = {
        "ospf-neighbor-information": {
            "ospf-neighbor": ListOf({
                "activity-timer": str,
                Optional("adj-sid-list"): {
                    'spring-adjacency-labels': ListOf({
                        'label': str,
                        'flags': str,
                        'adj-sid-type': str
                    })
                },
                "bdr-address": str,
                "dr-address": str,
                "interface-name": str,
                "neighbor-address": str,
                Optional("neighbor-adjacency-time"): {
                    "#text": str
                },
                "neighbor-id": str,
                "neighbor-priority": str,
                Optional("neighbor-up-time"): {
                    "#text": str,
                    Optional("junos:seconds"): str,
                },
                "options": str,
                "ospf-area": str,
                "ospf-neighbor-state": str,
                Optional("ospf-neighbor-topology"): {
                    "ospf-neighbor-topology-state": str,
                    "ospf-topology-id": str,
                    "ospf-topology-name": str
                }
            })
        }
    }


class ShowOspfNeighborExtensive(ShowOspfNeighborExtensiveSchema):
    """ Parser for:
            * show ospf neighbor extensive
    """
    cli_command = 'show ospf neighbor extensive'

    def cli(self, output=None, neighbor=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # 10.189.5.94      ge-0/0/0.0             Full      10.189.5.253     128    39
        p1 = re.compile(
            r'^(?P<neighbor_address>[\d\.]+) +(?P<interface_name>\S+)'
            r' +(?P<ospf_neighbor_state>\S+) +(?P<neighbor_id>[\d\.]+) +'
            r'(?P<neighbor_priority>\d+) +(?P<activity_timer>\d+)$')

        # Area 0.0.0.8, opt 0x52, DR 0.0.0.0, BDR 0.0.0.0
        p2 = re.compile(
            r'^Area +(?P<ospf_area>[\d\.]+), +opt +(?P<options>\S+),'
            r' +DR +(?P<dr_address>[\.\d]+), +BDR +(?P<bdr_address>[\.\d]+)$')

        # Up 3w0d 16:50:35, adjacent 3w0d 16:50:35
        p3 = re.compile(r'^Up +(?P<neighbor_up_time>\S+ +[\d:]+), +adjacent +'
                        r'(?P<neighbor_adjacency_time>\S+ +[\d:]+)$')

        #     28985       BVL         Protected
        p4 = re.compile(
            r'^(?P<label>\d+) +(?P<flags>\S+) + (?P<adj_sid_type>\S+)$')

        # Topology default (ID 0) -> Bidirectional
        p5 = re.compile(
            r'^Topology +(?P<ospf_topology_name>\S+) +\(ID +(?P<ospf_topology_id>\d+)\)'
            r' +-> +(?P<ospf_neighbor_topology_state>\S+)$')

        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # 10.189.5.94      ge-0/0/0.0             Full      10.189.5.253     128    39
            m = p1.match(line)
            if m:
                neighbor_list = ret_dict.setdefault("ospf-neighbor-information", {})\
                    .setdefault("ospf-neighbor", [])
                group = m.groupdict()
                entry = {}

                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_', '-')
                    entry[entry_key] = group_value

                neighbor_list.append(entry)
                continue

            # Area 0.0.0.8, opt 0x52, DR 0.0.0.0, BDR 0.0.0.0
            m = p2.match(line)
            if m:
                last_neighbor = ret_dict["ospf-neighbor-information"][
                    "ospf-neighbor"][-1]

                entry = last_neighbor
                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_', '-')
                    entry[entry_key] = group_value

                continue

            # Up 3w0d 16:50:35, adjacent 3w0d 16:50:35
            m = p3.match(line)
            if m:
                last_neighbor = ret_dict["ospf-neighbor-information"][
                    "ospf-neighbor"][-1]

                entry = last_neighbor
                group = m.groupdict()

                entry.setdefault("neighbor-up-time",
                                 {}).setdefault("#text",
                                                group["neighbor_up_time"])
                entry.setdefault("neighbor-adjacency-time", {})\
                    .setdefault("#text", group["neighbor_adjacency_time"])

                continue

            #     28985       BVL         Protected
            m = p4.match(line)
            if m:
                last_neighbor = ret_dict["ospf-neighbor-information"][
                    "ospf-neighbor"][-1]

                entry = {}
                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_', '-')
                    entry[entry_key] = group_value

                last_neighbor.setdefault("adj-sid-list", {})\
                    .setdefault("spring-adjacency-labels", []).append(entry)
                continue

            # Topology default (ID 0) -> Bidirectional
            m = p5.match(line)
            if m:
                last_neighbor = ret_dict["ospf-neighbor-information"][
                    "ospf-neighbor"][-1]

                entry = last_neighbor.setdefault("ospf-neighbor-topology", {})
                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_', '-')
                    entry[entry_key] = group_value

                continue

        return ret_dict


class ShowOspfInterfaceExtensiveSchema(MetaParser):
    """ Schema for:
            * show ospf interface extensive
    """

    schema = {
        "ospf-interface-information": {
            "ospf-interface": ListOf({
                "address-mask": str,
                "adj-count": str,
                "authentication-type": str,
                "bdr-id": str,
                "dead-interval": str,
                "dr-id": str,
                "hello-interval": str,
                "interface-address": str,
                "interface-cost": str,
                "interface-name": str,
                "interface-type": str,
                "mtu": str,
                "neighbor-count": str,
                "ospf-area": str,
                "ospf-interface-protection-type": str,
                "ospf-interface-state": str,
                Optional("ospf-interface-tilfa-prot-fate"): str,
                Optional("ospf-interface-tilfa-prot-link"): str,
                Optional("ospf-interface-tilfa-prot-node"): str,
                Optional("ospf-interface-tilfa-prot-srlg"): str,
                Optional("passive"): str,
                Optional("dr-address"): str,
                Optional("router-priority"): str,
                "ospf-interface-topology": {
                    "ospf-topology-id": str,
                    "ospf-topology-metric": str,
                    "ospf-topology-name": str,
                    Optional("ospf-topology-passive"): bool,
                },
                "ospf-stub-type": str,
                "retransmit-interval": str
            }),
        }
    }


class ShowOspfInterfaceExtensive(ShowOspfInterfaceExtensiveSchema):
    """ Parser for:
            * show ospf interface extensive
    """
    cli_command = 'show ospf interface extensive'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # ge-0/0/0.0          PtToPt  0.0.0.8         0.0.0.0         0.0.0.0            1
        p1 = re.compile(
            r'^(?P<interface_name>\S+) +(?P<ospf_interface_state>\S+)'
            r' +(?P<ospf_area>[\d\.]+) +(?P<dr_id>[\d\.]+) +(?P<bdr_id>[\d\.]+) +'
            r'(?P<neighbor_count>\d+)$')

        # Type: P2P, Address: 10.189.5.93, Mask: 255.255.255.252, MTU: 1500, Cost: 5
        p2 = re.compile(
            r'^Type: +(?P<interface_type>\S+), +Address: +(?P<interface_address>[\w\.\:]+)'
            r', +Mask: +(?P<address_mask>[\d\.]+), +MTU: +(?P<mtu>\d+), +Cost: +(?P<interface_cost>\d+)$'
        )

        # Adj count: 1
        # Adj count: 0, Passive
        p3 = re.compile(
            r'^Adj +count: +(?P<adj_count>\d+)(, +(?P<passive>\S+))?$')

        # Hello: 10, Dead: 40, ReXmit: 5, Not Stub
        p4 = re.compile(
            r'^Hello: +(?P<hello_interval>\d+), +Dead: +(?P<dead_interval>\d+)'
            r', +ReXmit: +(?P<retransmit_interval>\d+), +(?P<ospf_stub_type>.+)$'
        )

        # Auth type: None
        p5 = re.compile(r'^Auth +type: +(?P<authentication_type>\S+)$')

        # Protection type: Post Convergence
        p6 = re.compile(
            r'^Protection +type: +(?P<ospf_interface_protection_type>.+)$')

        # Post convergence protection: Enabled, Fate sharing: No, SRLG: No, Node cost: 100
        p7 = re.compile(
            r'^Post +convergence +protection: +(?P<ospf_interface_tilfa_prot_link>\S+)'
            r', +Fate +sharing: +(?P<ospf_interface_tilfa_prot_srlg>\S+), +SRLG: +'
            r'(?P<ospf_interface_tilfa_prot_fate>\S+), +Node +cost: +'
            r'(?P<ospf_interface_tilfa_prot_node>\S+)$')

        # Topology default (ID 0) -> Cost: 5
        # Topology default (ID 0) -> Passive, Cost: 100
        p8 = re.compile(
            r'^Topology +(?P<ospf_topology_name>\S+) +\(ID +(?P<ospf_topology_id>\d+)\)'
            r' +->(?P<ospf_topology_passive> +Passive,)? +Cost: +(?P<ospf_topology_metric>\d+)$'
        )

        # DR addr: 10.189.5.252, Priority: 128
        p9 = re.compile(r'^DR +addr: +(?P<dr_address>[\d\.]+), +Priority: +'
                        r'(?P<router_priority>\d+)$')

        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # ge-0/0/0.0          PtToPt  0.0.0.8         0.0.0.0         0.0.0.0            1
            m = p1.match(line)
            if m:
                interface_list = ret_dict.setdefault("ospf-interface-information", {})\
                    .setdefault("ospf-interface", [])
                group = m.groupdict()
                entry = {}
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_', '-')
                    entry[entry_key] = group_value

                interface_list.append(entry)
                continue

            # Type: P2P, Address: 10.189.5.93, Mask: 255.255.255.252, MTU: 1500, Cost: 5
            m = p2.match(line)
            if m:
                last_interface = ret_dict["ospf-interface-information"]\
                    ["ospf-interface"][-1]
                group = m.groupdict()
                entry = last_interface
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_', '-')
                    entry[entry_key] = group_value
                continue

            # Adj count: 1
            m = p3.match(line)
            if m:
                last_interface = ret_dict["ospf-interface-information"]\
                    ["ospf-interface"][-1]
                group = m.groupdict()
                entry = last_interface
                entry['adj-count'] = group['adj_count']

                if group['passive']:
                    entry['passive'] = group['passive']

                continue

            # Hello: 10, Dead: 40, ReXmit: 5, Not Stub
            m = p4.match(line)
            if m:
                last_interface = ret_dict["ospf-interface-information"]\
                    ["ospf-interface"][-1]
                group = m.groupdict()
                entry = last_interface
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_', '-')
                    entry[entry_key] = group_value
                continue

            # Auth type: None
            m = p5.match(line)
            if m:
                last_interface = ret_dict["ospf-interface-information"]\
                    ["ospf-interface"][-1]
                group = m.groupdict()
                entry = last_interface
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_', '-')
                    entry[entry_key] = group_value
                continue

            # Protection type: Post Convergence
            m = p6.match(line)
            if m:
                last_interface = ret_dict["ospf-interface-information"]\
                    ["ospf-interface"][-1]
                group = m.groupdict()
                entry = last_interface
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_', '-')
                    entry[entry_key] = group_value
                continue

            # Post convergence protection: Enabled, Fate sharing: No, SRLG: No, Node cost: 100
            m = p7.match(line)
            if m:
                last_interface = ret_dict["ospf-interface-information"]\
                    ["ospf-interface"][-1]
                group = m.groupdict()
                entry = last_interface
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_', '-')
                    entry[entry_key] = group_value
                continue

            # Topology default (ID 0) -> Cost: 5
            m = p8.match(line)
            if m:
                last_interface = ret_dict["ospf-interface-information"]\
                    ["ospf-interface"][-1]
                group = m.groupdict()
                entry = last_interface
                entry = entry.setdefault('ospf-interface-topology', {})

                entry['ospf-topology-name'] = group['ospf_topology_name']
                entry['ospf-topology-id'] = group['ospf_topology_id']
                entry['ospf-topology-metric'] = group['ospf_topology_metric']

                if group['ospf_topology_passive']:
                    entry['ospf-topology-passive'] = True

                continue

            # DR addr: 10.189.5.252, Priority: 128
            m = p9.match(line)
            if m:
                last_interface = ret_dict["ospf-interface-information"]\
                    ["ospf-interface"][-1]
                group = m.groupdict()
                entry = last_interface
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_', '-')
                    entry[entry_key] = group_value

                continue

        return ret_dict


class ShowOspfNeighborDetail(ShowOspfNeighborExtensive):
    """ Parser for:
            * show ospf neighbor detail
            * show ospf neighbor {neighbor} detail
    """
    cli_command = [
        'show ospf neighbor detail', 'show ospf neighbor {neighbor} detail'
    ]

    def cli(self, neighbor=None, output=None):
        if output is None:
            if neighbor:
                out = self.device.execute(
                    self.cli_command[1].format(neighbor=neighbor))
            else:
                out = self.device.execute(self.cli_command[0])
        else:
            out = output

        return super().cli(output=out, neighbor=neighbor)


class ShowOspfRouteBriefSchema(MetaParser):
    """ Schema for:
            * show ospf route brief
    """
    """
    schema = {
        "ospf-route-information": {
            "ospf-topology-route-table": {
                "ospf-route": [{
                "ospf-route-entry": [{
                    "address-prefix": str,
                    "interface-cost": str,
                    "next-hop-type": str,
                    "ospf-next-hop": {
                        Optional("next-hop-address"): {
                            "interface-address": str
                        },
                        "next-hop-name": {
                            "interface-name": str
                        }
                    },
                    "route-path-type": str,
                    "route-type": str,
                    Optional("ospf-backup-next-hop"): {
                        "ospf-backup-next-hop-type": str,
                        "ospf-backup-next-hop-address": str,
                        "ospf-backup-next-hop-interface": str
                    }
                }]
            }],
                Optional("ospf-topology-name"): str
            }
        }
    }
    """

    schema = {
        "ospf-route-information": {
            "ospf-topology-route-table": {
                "ospf-route": ListOf({
                    "ospf-route-entry": ListOf({
                        "address-prefix": str,
                        "interface-cost": str,
                        "next-hop-type": str,
                        "ospf-next-hop": {
                            Optional("next-hop-address"): {
                                "interface-address": str
                            },
                            "next-hop-name": {
                                "interface-name": str
                            }
                        },
                        "route-path-type": str,
                        "route-type": str,
                        Optional("ospf-backup-next-hop"): {
                            "ospf-backup-next-hop-type": str,
                            "ospf-backup-next-hop-address": str,
                            "ospf-backup-next-hop-interface": str
                        }
                    })
                }),
                Optional("ospf-topology-name"): str
            }
        }
    }


class ShowOspfRouteBrief(ShowOspfRouteBriefSchema):
    """ Parser for:
            * show ospf route brief
    """
    cli_command = 'show ospf route brief'

    address_prefix = None

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # 10.36.3.3            Intra Router     IP         1201 ge-0/0/1.0    10.169.14.121
        # 10.19.198.28/30    Intra Network    IP         1005 ge-0/0/0.0    10.189.5.94
        # 2568 (S=0)         Intra Network    Mpls          0 ge-0/0/1.0    10.169.14.121
        # 10.169.14.120/30  Intra Network    IP          100 ge-0/0/1.0
        p1 = re.compile(
            r'^(?P<address_prefix>[\d\.\/]+( \(S=\d+\))?) +(?P<route_path_type>\S+)'
            r' +(?P<route_type>\S+|(AS BR)) +(?P<next_hop_type>\S+) +(?P<interface_cost>\S+)'
            r' +(?P<interface_name>\S+)( +(?P<interface_address>[\d\.]+))?$')

        # Bkup SPRING     ge-0/0/0.0    10.189.5.94
        p2 = re.compile(
            r'^(?P<ospf_backup_next_hop_type>Bkup +\S+) +'
            r'(?P<ospf_backup_next_hop_interface>\S+) +(?P<ospf_backup_next_hop_address>[\d\.]+)$'
        )

        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # 10.36.3.3            Intra Router     IP         1201 ge-0/0/1.0    10.169.14.121
            # 10.19.198.28/30    Intra Network    IP         1005 ge-0/0/0.0    10.189.5.94
            # 2568 (S=0)         Intra Network    Mpls          0 ge-0/0/1.0    10.169.14.121
            # 10.169.14.120/30  Intra Network    IP          100 ge-0/0/1.0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault("ospf-route-information", {})\
                    .setdefault("ospf-topology-route-table", {})\
                        .setdefault("ospf-route", [])

                entry = {}
                entry.setdefault("address-prefix", group['address_prefix'])
                entry.setdefault("route-path-type", group['route_path_type'])
                entry.setdefault("route-type", group['route_type'])
                entry.setdefault("next-hop-type", group['next_hop_type'])
                entry.setdefault("interface-cost", group['interface_cost'])
                entry.setdefault("ospf-next-hop", {}).setdefault("next-hop-name", {})\
                        .setdefault("interface-name", group['interface_name'])

                if "interface_address" in group and group['interface_address']:
                    entry.setdefault("ospf-next-hop", {}).setdefault("next-hop-address", {})\
                            .setdefault("interface-address", group['interface_address'])

                if self.address_prefix == group['address_prefix']:
                    ret_dict["ospf-route-information"]["ospf-topology-route-table"]\
                        ["ospf-route"][-1]["ospf-route-entry"].append(entry)
                else:
                    ret_dict["ospf-route-information"]["ospf-topology-route-table"]\
                        ["ospf-route"].append({"ospf-route-entry":[entry]})

                self.address_prefix = group['address_prefix']
                continue

            # Bkup SPRING     ge-0/0/0.0    10.189.5.94
            m = p2.match(line)
            if m:
                group = m.groupdict()

                last_route = ret_dict["ospf-route-information"]["ospf-topology-route-table"]\
                    ["ospf-route"][-1]

                last_route["ospf-route-entry"][-1]["ospf-backup-next-hop"] = {}

                entry = last_route["ospf-route-entry"][-1][
                    "ospf-backup-next-hop"]
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_', '-')
                    entry[entry_key] = group_value
                continue

        return ret_dict


class ShowOspfRouteDetail(ShowOspfRouteBrief):
    """ Parser for:
            * show ospf route detail
    """

    cli_command = 'show ospf route detail'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        return super().cli(output=out)


class ShowOspfDatabaseNetworkLsaidDetailSchema(MetaParser):
    """ Schema for:
            * show ospf database network lsa-id {ipaddress} detail
    """
    """ schema = {
    Optional("@xmlns:junos"): str,
    "ospf-database-information": {
        Optional("@xmlns"): str,
        "ospf-area-header": {
            "ospf-area": str
        },
        "ospf-database": {
            Optional("@heading"): str,
            "advertising-router": str,
            "age": str,
            "checksum": str,
            "lsa-id": str,
            "lsa-length": str,
            "lsa-type": str,
            "options": str,
            "ospf-network-lsa": {
                "address-mask": str,
                "attached-router": "list",
                "ospf-lsa-topology": {
                    "ospf-lsa-topology-link": [
                        {
                            "link-type-name": str,
                            "ospf-lsa-topology-link-metric": str,
                            "ospf-lsa-topology-link-node-id": str,
                            "ospf-lsa-topology-link-state": str
                        }
                    ],
                    "ospf-topology-id": str,
                    "ospf-topology-name": str
                }
            },
            "our-entry": str,
            "sequence-number": str
            }
        }
    } """

    schema = {
        Optional("@xmlns:junos"): str,
        "ospf-database-information": {
            Optional("@xmlns"): str,
            "ospf-area-header": {
                "ospf-area": str
            },
            "ospf-database": {
                Optional("@heading"): str,
                "advertising-router": str,
                "age": str,
                "checksum": str,
                "lsa-id": str,
                "lsa-length": str,
                "lsa-type": str,
                "options": str,
                "ospf-network-lsa": {
                    "address-mask": str,
                    "attached-router": list,
                    "ospf-lsa-topology": {
                        "ospf-lsa-topology-link": ListOf({
                            "link-type-name": str,
                            "ospf-lsa-topology-link-metric": str,
                            "ospf-lsa-topology-link-node-id": str,
                            "ospf-lsa-topology-link-state": str
                        }),
                        "ospf-topology-id":
                        str,
                        "ospf-topology-name":
                        str
                    }
                },
                Optional("our-entry"): bool,
                "sequence-number": str
            }
        }
    }


class ShowOspfDatabaseNetworkLsaidDetail(
        ShowOspfDatabaseNetworkLsaidDetailSchema):
    """ Parser for:
            * show ospf database network lsa-id {ipaddress} detail
    """
    cli_command = 'show ospf database network lsa-id {ipaddress} detail'

    def cli(self, ipaddress=None, output=None):
        if not output:
            cmd = self.cli_command.format(ipaddress=ipaddress)
            out = self.device.execute(cmd)
        else:
            out = output

        # Type       ID               Adv Rtr           Seq      Age  Opt  Cksum  Len
        p0 = re.compile(r'^(?P<heading>Type \s+ID[\s\S]+)$')

        # OSPF database, Area 192.168.76.0
        p1 = re.compile(r'^OSPF +database, +Area +(?P<ospf_area>\S+)$')

        # Network *10.69.197.1    192.168.219.235   0x80000026  1730  0x22 0x1b56  36
        p2 = re.compile(
            r'^(?P<lsa_type>\S+) *(?P<our_entry>\*)?(?P<lsa_id>[\d\.]+) '
            r'+(?P<advertising_router>\S+) +(?P<sequence_number>\S+) +'
            r'(?P<age>\S+) +(?P<options>\S+) +(?P<checksum>\S+) +'
            r'(?P<lsa_length>\S+)$')

        # mask 255.255.255.128
        p3 = re.compile(r'^mask +(?P<address_mask>\S+)$')

        # attached router 192.168.219.235
        p4 = re.compile(r'^attached router +(?P<attached_router>\S+)$')

        # Topology default (ID 0)
        p5 = re.compile(
            r'^Topology +(?P<ospf_topology_name>\S+) +\(ID +(?P<ospf_topology_id>\S+)+\)$'
        )

        # Type: Transit, Node ID: 192.168.219.236
        p6 = re.compile(
            r'^Type: +(?P<link_type_name>\S+)+, '
            r'+Node +ID: +(?P<ospf_lsa_topology_link_node_id>\S+)$')

        # Metric: 0, Bidirectional
        p7 = re.compile(r'^Metric: +(?P<ospf_lsa_topology_link_metric>\S+)+, '
                        r'+(?P<ospf_lsa_topology_link_state>\S+)$')

        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # Type       ID               Adv Rtr           Seq      Age  Opt  Cksum  Len
            m = p0.match(line)
            if m:
                group = m.groupdict()
                ospf_database_dict["@heading"] = group["heading"]

            # OSPF database, Area 192.168.76.0
            m = p1.match(line)
            if m:
                ospf_database_information_entry = ret_dict.setdefault(
                    "ospf-database-information", {})
                ospf_database_dict = ospf_database_information_entry.setdefault(
                    "ospf-database", {})
                ospf_network_lsa = ospf_database_dict.setdefault(
                    "ospf-network-lsa", {})
                attached_router = ospf_network_lsa.setdefault(
                    "attached-router", [])
                ospf_lsa_topology = ospf_network_lsa.setdefault(
                    "ospf-lsa-topology", {})
                ospf_lsa_topology_link = ospf_lsa_topology.setdefault(
                    "ospf-lsa-topology-link", [])
                group = m.groupdict()
                entry_dict = {}
                entry_dict["ospf-area"] = group["ospf_area"]
                ospf_database_information_entry[
                    "ospf-area-header"] = entry_dict
                continue

            # Network *10.69.197.1    192.168.219.235   0x80000026  1730  0x22 0x1b56  36
            m = p2.match(line)
            if m:
                group = m.groupdict()
                for group_key, group_value in group.items():
                    if (group_key == "our_entry"):
                        if (group_value == '*'):
                            ospf_database_dict['our-entry'] = True
                    else:
                        entry_key = group_key.replace('_', '-')
                        ospf_database_dict[entry_key] = group_value
                continue

            # mask 255.255.255.128
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ospf_network_lsa["address-mask"] = group["address_mask"]
                continue

            # attached router 192.168.219.235
            m = p4.match(line)
            if m:
                group = m.groupdict()
                attached_router.append(group["attached_router"])
                continue

            # Topology default (ID 0)
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ospf_lsa_topology["ospf-topology-id"] = group[
                    "ospf_topology_name"]
                ospf_lsa_topology["ospf-topology-name"] = group[
                    "ospf_topology_name"]
                continue

            # Type: Transit, Node ID: 192.168.219.236
            m = p6.match(line)
            if m:
                group = m.groupdict()
                entry_dict = {}
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_', '-')
                    entry_dict[entry_key] = group_value
                continue

            # Metric: 0, Bidirectional
            m = p7.match(line)
            if m:
                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_', '-')
                    entry_dict[entry_key] = group_value
                ospf_lsa_topology_link.append(entry_dict)
                continue

        return ret_dict


class ShowOspfDatabaseLsaidDetail(ShowOspfDatabaseAdvertisingRouterSelfDetail):
    """ Parser for:
            - show ospf database lsa-id {ipaddress} detail
    """

    cli_command = 'show ospf database lsa-id {ipaddress} detail'

    def cli(self, output=None, ipaddress=None):
        if not output:
            out = self.device.execute(
                self.cli_command.format(ipaddress=ipaddress))
        else:
            out = output

        return super().cli(output = ' ' if not out else out)


class ShowOspfRouteNetworkExtensiveSchema(MetaParser):
    '''
    schema = {
    Optional("@xmlns:junos"): str,
    "ospf-route-information": {
        Optional("@xmlns"): str,
        "ospf-topology-route-table": {
            "ospf-route": [
                {
                    "ospf-route-entry": {
                        "address-prefix": str,
                        "interface-cost": str,
                        "next-hop-type": str,
                        "ospf-area": str,
                        "ospf-next-hop": {
                            "next-hop-address": {
                                "interface-address": str
                            },
                            "next-hop-name": {
                                "interface-name": str
                            }
                        },
                        "route-origin": str,
                        "route-path-type": str,
                        "route-priority": str,
                        "route-type": str
                    }
                }
            ],
            "ospf-topology-name": str
        }
    }
}
    '''

    schema = {
        "ospf-route-information": {
            Optional("@xmlns"): str,
            "ospf-topology-route-table": {
                "ospf-route": ListOf({
                    "ospf-route-entry": {
                        "address-prefix": str,
                        "interface-cost": str,
                        "next-hop-type": str,
                        "ospf-area": str,
                        "ospf-next-hop": {
                            Optional("next-hop-address"): {
                                Optional("interface-address"): str
                            },
                            "next-hop-name": {
                                "interface-name": str
                            }
                        },
                        "route-origin": str,
                        "route-path-type": str,
                        "route-priority": str,
                        "route-type": str
                    }
                }),
                "ospf-topology-name": str
            }
        }
    }


'''
Parser for:
    * show ospf route network extensive
'''


class ShowOspfRouteNetworkExtensive(ShowOspfRouteNetworkExtensiveSchema):
    cli_command = 'show ospf route network extensive'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # Topology default Route Table:
        p1 = re.compile(r'^Topology +(?P<ospf_topology_name>\S+) +Route +Table:$')

        #10.1.0.0/24         Ext2  Network    IP            0 ge-0/0/0.0    10.70.0.4
        p2 = re.compile(r'^(?P<address_prefix>\S+) +(?P<route_path_type>\S+) '
                        r'+(?P<route_type>\S+) +(?P<next_hop_type>\S+) +'
                        r'(?P<interface_cost>\d+) +(?P<interface_name>\S+)'
                        r'( +(?P<interface_address>\S+))?$')

        #area 0.0.0.0, origin 10.64.4.4, priority medium
        p3 = re.compile(r'^area +(?P<ospf_area>[\d\.]+)+, +origin '
                        r'+(?P<route_origin>[\d\.]+), +priority +'
                        r'(?P<route_priority>\w+)$')

        for line in out.splitlines():
            line = line.strip()

            # Topology default Route Table:
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ospf_topology_route_table = ret_dict.setdefault(
                    'ospf-route-information', {}).setdefault('ospf-topology-route-table', {})
                ospf_route = ospf_topology_route_table.setdefault('ospf-route', [])

                ospf_topology_route_table['ospf-topology-name'] = group['ospf_topology_name']

            #10.1.0.0/24         Ext2  Network    IP            0 ge-0/0/0.0    10.70.0.4
            m = p2.match(line)
            if m:
                group = m.groupdict()

                ospf_route_entry_dict = {}
                ospf_next_hop_dict = {}

                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_', '-')

                    if (entry_key == 'interface-address' and group_value != None):
                        next_hop_add = {}
                        next_hop_add['interface-address'] = group_value
                        ospf_next_hop_dict.update({'next-hop-address': next_hop_add})
                    elif (entry_key == 'interface-name'):
                        next_hop_name = {}
                        next_hop_name['interface-name'] = group_value
                        ospf_next_hop_dict.update({'next-hop-name': next_hop_name})
                    else:
                        if group_value != None:
                            entry_key = group_key.replace('_', '-')
                            ospf_route_entry_dict[entry_key] = group_value

                ospf_route_entry_dict.update({'ospf-next-hop': ospf_next_hop_dict})
                continue

            #area 0.0.0.0, origin 10.64.4.4, priority medium
            m = p3.match(line)
            if m:
                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_', '-')
                    ospf_route_entry_dict[entry_key] = group_value

                ospf_parent_route_dict = {}
                ospf_parent_route_dict['ospf-route-entry'] = ospf_route_entry_dict

                ospf_route.append(ospf_parent_route_dict)
                continue

        return ret_dict

class ShowOspfDatabaseOpaqueAreaSchema(MetaParser):
    """ Schema for:
            * show ospf database opaque-area 

	schema = {
        "ospf-database-information": {
            "ospf-area-header": {
                "ospf-area": str
            },
            "ospf-database": [
                {
                    Optional("@heading"): str,
                    "advertising-router": str,
                    "age": str,
                    "checksum": str,
                    "lsa-id": str,
                    "lsa-length": str,
                    "lsa-type": str,
                    "options": str,
                    Optional("our-entry"): bool,
                    "sequence-number": str
                }
            ]
        }
    }
    """

    schema = {
        "ospf-database-information": {
            "ospf-area-header": {
                "ospf-area": str
            },
            "ospf-database": ListOf({
                Optional("@heading"): str,
                    "advertising-router": str,
                    "age": str,
                    "checksum": str,
                    "lsa-id": str,
                    "lsa-length": str,
                    "lsa-type": str,
                    "options": str,
                    Optional("our-entry"): bool,
                    "sequence-number": str
            })
        }
    }

class ShowOspfDatabaseOpaqueArea(ShowOspfDatabaseOpaqueAreaSchema):
    """ Parser for:
            * show ospf database opaque-area
    """
    cli_command = 'show ospf database opaque-area'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}   
  
        # OSPF database, Area 0.0.0.8
        p1 = re.compile(r'^OSPF database, Area +(?P<ospf_area>\S+)$')
      
        # OpaqArea 10.1.0.1          10.49.194.125    0x80000002   359  0x22 0x6f5d  28
        # OpaqArea*10.1.0.1          10.34.2.250     0x80000003   227  0x22 0xa11a  28
        p2 = re.compile(r'^(?P<lsa_type>[a-zA-Z]+) *(?P<lsa_id>\*?[\d\.]+) +' 
                        r'(?P<advertising_router>\S+) +(?P<sequence_number>\S+) +' 
                        r'(?P<age>\S+) +(?P<options>\S+) +(?P<checksum>\S+) +' 
                        r'(?P<lsa_length>\S+)$')

        for line in out.splitlines():
            line = line.strip()

            # OSPF database, Area 0.0.0.8
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ospf_db_info = ret_dict.setdefault('ospf-database-information', 
                                                    {})
                ospf_area_header = ospf_db_info.setdefault('ospf-area-header', 
                                                    {})
                ospf_area_header.setdefault('ospf-area', group['ospf_area'])
		        
                # OSPF DB Entry List
                ospf_db_entry_list = []
                ospf_db_info['ospf-database'] = ospf_db_entry_list
                continue
            
            # OpaqArea 10.1.0.1          10.49.194.125    0x80000002   359  0x22 0x6f5d  28
            # OpaqArea*10.1.0.1          10.34.2.250     0x80000003   227  0x22 0xa11a  28
            m = p2.match(line)
            if m:
                group = m.groupdict()
		        
                # OSPF DB Entry dict
                ospf_db_entry_dict = {}
          
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_', '-')
                    ospf_db_entry_dict[entry_key] = group_value
    
                if ospf_db_entry_dict['lsa-id'][0] == "*":
                    ospf_db_entry_dict['lsa-id'] = group['lsa_id'][1:]
                    ospf_db_entry_dict['our-entry'] = True
                    
                ospf_db_entry_list.append(ospf_db_entry_dict)
                continue
                                           
        return ret_dict


class ShowOspfRoutePrefixSchema(MetaParser):

    # schema = {
    #     "ospf-route-information": {
    #         "ospf-topology-route-table": {
    #             "ospf-route": {
    #                 "ospf-route-entry": {
    #                     "address-prefix": str,
    #                     "interface-cost": str,
    #                     "next-hop-type": str,
    #                     "ospf-next-hop": [
    #                         {
    #                             "next-hop-address": {
    #                                 "interface-address": str
    #                             },
    #                             "next-hop-name": {
    #                                 "interface-name": str
    #                             }
    #                         }
    #                     ],
    #                     "route-path-type": str,
    #                     "route-type": str
    #                 }
    #             },
    #             "ospf-topology-name": str
    #         }
    #     }
    # }

    schema = {
        "ospf-route-information": {
            "ospf-topology-route-table": {
                "ospf-route": {
                    "ospf-route-entry": {
                        "address-prefix": str,
                        "interface-cost": str,
                        "next-hop-type": str,
                        "ospf-next-hop": ListOf({
                            "next-hop-address": {
                                "interface-address": str,
                            },
                            "next-hop-name": {
                                "interface-name": str,
                            }
                        }),
                        "route-path-type": str,
                        "route-type": str
                    }
                },
                "ospf-topology-name": str
            }
        }
    }


'''
Parser for:
    * show ospf route prefix
'''


class ShowOspfRoutePrefix(ShowOspfRoutePrefixSchema):
    cli_command = 'show ospf route {prefix}'

    def cli(self,prefix, output=None):
        if not output:
            out = self.device.execute(self.cli_command.format(
                prefix=prefix
            ))
        else:
            out = output

        ret_dict = {}

        # Topology default Route Table:
        p1 = re.compile(r'^Topology +(?P<ospf_topology_name>\S+) +Route +Table:$')

        #10.1.0.0/24         Ext2  Network    IP            0 ge-0/0/0.0    10.70.0.4
        p2 = re.compile(r'^(?P<address_prefix>\S+) +(?P<route_path_type>\S+) '
                        r'+(?P<route_type>\S+) +(?P<next_hop_type>\S+) +'
                        r'(?P<interface_cost>\d+) +(?P<interface_name>\S+)'
                        r'( +(?P<interface_address>\S+))?$')

        #                                                    ge-0/0/4.0    10.0.0.2
        p2_1 = re.compile(r'^(?P<interface_name>[a-z]{2}-\d+/\d+/\d+(\.\d+))?\s+(?P<interface_address>\d+.\d+\.\d+\.\d+)$')

        #area 0.0.0.0, origin 10.64.4.4, priority medium
        p3 = re.compile(r'^area +(?P<ospf_area>[\d\.]+)+, +origin '
                        r'+(?P<route_origin>[\d\.]+), +priority +'
                        r'(?P<route_priority>\w+)$')

        ospf_topology_name = ''

        for line in out.splitlines():
            line = line.strip()

            # Topology default Route Table:
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ospf_topology_name = group['ospf_topology_name']

            #10.1.0.0/24         Ext2  Network    IP            0 ge-0/0/0.0    10.70.0.4
            m = p2.match(line)
            if m:
                if ospf_topology_name:

                    ospf_topology_route_table = ret_dict.setdefault(
                        'ospf-route-information', {}).setdefault('ospf-topology-route-table', {})
                    ospf_topology_route_table['ospf-topology-name'] = ospf_topology_name
                    ospf_topology_name = ''

                group = m.groupdict()

                ospf_route_entry_dict = {}
                ospf_next_hop_dict = {}

                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_', '-')

                    if (entry_key == 'interface-address' and group_value != None):
                        next_hop_add = {}
                        next_hop_add['interface-address'] = group_value
                        ospf_next_hop_dict.update({'next-hop-address': next_hop_add})
                    elif (entry_key == 'interface-name'):
                        next_hop_name = {}
                        next_hop_name['interface-name'] = group_value
                        ospf_next_hop_dict.update({'next-hop-name': next_hop_name})
                    else:
                        if group_value != None:
                            entry_key = group_key.replace('_', '-')
                            ospf_route_entry_dict[entry_key] = group_value

                ospf_route_entry_dict.update({'ospf-next-hop': [ospf_next_hop_dict]})
                ospf_parent_route_dict = {}
                ospf_parent_route_dict['ospf-route-entry'] = ospf_route_entry_dict
                ospf_topology_route_table['ospf-route'] = ospf_parent_route_dict
                continue

            #                                                    ge-0/0/4.0    10.0.0.2
            m = p2_1.match(line)
            if m:
                group = m.groupdict()
                ospf_next_hop_dict = {}
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_', '-')
                    if entry_key == 'interface-address':
                        ospf_next_hop_dict.setdefault('next-hop-address', {}).setdefault(entry_key, group_value)
                    if entry_key == 'interface-name':
                        ospf_next_hop_dict.setdefault('next-hop-name', {}).setdefault(entry_key, group_value)
                ospf_route_entry_dict['ospf-next-hop'].append(ospf_next_hop_dict)
                continue

        return ret_dict


class ShowOspfStatisticsSchema(MetaParser):
    """ Schema for:
            * show ospf statistics
    """

    '''schema = {
    Optional("@xmlns:junos"): str,
    "ospf-statistics-information": {
        Optional("@xmlns"): str,
        "ospf-statistics": {
            "dbds-retransmit": str,
            "dbds-retransmit-5seconds": str,
            "flood-queue-depth": str,
            "lsas-acknowledged": str,
            "lsas-acknowledged-5seconds": str,
            "lsas-flooded": str,
            "lsas-flooded-5seconds": str,
            "lsas-high-prio-flooded": str,
            "lsas-high-prio-flooded-5seconds": str,
            "lsas-nbr-transmit": str,
            "lsas-nbr-transmit-5seconds": str,
            "lsas-requested": str,
            "lsas-requested-5seconds": str,
            "lsas-retransmit": str,
            "lsas-retransmit-5seconds": str,
            "ospf-errors": {
                "subnet-mismatch-error": str
            },
            "packet-statistics": [
                {
                    "ospf-packet-type": str,
                    "packets-received": str,
                    "packets-received-5seconds": str,
                    "packets-sent": str,
                    "packets-sent-5seconds": str
                }
            ],
            "total-database-summaries": str,
            "total-linkstate-request": str,
            "total-retransmits": str
        }
    }
}'''

    schema = {
        Optional("@xmlns:junos"): str,
        "ospf-statistics-information": {
            Optional("@xmlns"): str,
            "ospf-statistics": {
                "dbds-retransmit": str,
                "dbds-retransmit-5seconds": str,
                "flood-queue-depth": str,
                "lsas-acknowledged": str,
                "lsas-acknowledged-5seconds": str,
                "lsas-flooded": str,
                "lsas-flooded-5seconds": str,
                "lsas-high-prio-flooded": str,
                "lsas-high-prio-flooded-5seconds": str,
                "lsas-nbr-transmit": str,
                "lsas-nbr-transmit-5seconds": str,
                "lsas-requested": str,
                "lsas-requested-5seconds": str,
                "lsas-retransmit": str,
                "lsas-retransmit-5seconds": str,
                "ospf-errors": {
                    "subnet-mismatch-error": str
                },
                "packet-statistics": ListOf({
                    "ospf-packet-type": str,
                    "packets-received": str,
                    "packets-received-5seconds": str,
                    "packets-sent": str,
                    "packets-sent-5seconds": str
                }),
                "total-database-summaries": str,
                "total-linkstate-request": str,
                "total-retransmits": str
                }
        }
    }


class ShowOspfStatistics(ShowOspfStatisticsSchema):
    """ Parser for:
            * show ospf statistics
    """
    cli_command = 'show ospf statistics'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        #Packet type             Total                  Last 5 seconds
        p0 = re.compile(r'^(?P<heading>\APacket +type[\S\s]+)$')

        #Hello        6202169       5703920           0             3
        p1 = re.compile(r'^(?P<ospf_packet_type>\S+) +(?P<packets_sent>\d+) '
                        r'+(?P<packets_received>\d+) +'
                        r'(?P<packets_sent_5seconds>\d+) '
                        r'+(?P<packets_received_5seconds>\d+)$')

        #DBDs retransmitted     :               203656, last 5 seconds :          0
        p2 = re.compile(r'^DBDs retransmitted +: +(?P<dbds_retransmit>\d+), '
                        r'+last +5 +seconds +: +(?P<dbds_retransmit_5seconds>\d+)$')
  
        #LSAs flooded           :             66582263, last 5 seconds :          0
        p3 = re.compile(r'^LSAs flooded +: +(?P<lsas_flooded>\d+), '
                        r'+last +5 +seconds +: +(?P<lsas_flooded_5seconds>\d+)$')

        #LSAs flooded high-prio :            375568998, last 5 seconds :          0
        p4 = re.compile(r'^LSAs flooded high-prio +: +(?P<lsas_high_prio_flooded>\d+), '
                        r'+last +5 +seconds +: +(?P<lsas_high_prio_flooded_5seconds>\d+)$')

        #LSAs retransmitted     :              8064643, last 5 seconds :          0
        p5 = re.compile(r'^LSAs retransmitted +: +(?P<lsas_retransmit>\d+), '
                        r'+last +5 +seconds +: +(?P<lsas_retransmit_5seconds>\d+)$')

        #LSAs transmitted to nbr:              3423982, last 5 seconds :          0
        p6 = re.compile(r'^LSAs transmitted to nbr+: +(?P<lsas_nbr_transmit>\d+), '
                        r'+last +5 +seconds +: +(?P<lsas_nbr_transmit_5seconds>\d+)$')

        #LSAs requested         :                 3517, last 5 seconds :          0
        p7 = re.compile(r'^LSAs requested +: +(?P<lsas_requested>\d+), '
                        r'+last +5 +seconds +: +(?P<lsas_requested_5seconds>\d+)$')

        #LSAs acknowledged      :            225554974, last 5 seconds :          0
        p8 = re.compile(r'^LSAs acknowledged +: +(?P<lsas_acknowledged>\d+), +last '
                        r'+5 +seconds +: +(?P<lsas_acknowledged_5seconds>\d+)$')

        #Flood queue depth      :               0
        #Total rexmit entries   :               0
        #db summaries           :               0
        #lsreq entries          :               0
        p9 = re.compile(r'^(?P<pattern>[\w\s]+): +(?P<value>\d+)$')
        
        #12 subnet mismatches
        p10 = re.compile(r'^(?P<subnet_mismatch_error>\d+) +subnet +mismatches$')

        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            #Packet type             Total                  Last 5 seconds
            m = p0.match(line)
            if m:
                ospf_area = ret_dict.setdefault("ospf-statistics-information", \
                                                {}).setdefault("ospf-statistics", {})
                group = m.groupdict()
                packet_list = []
                continue

            #Hello        6202169       5703920           0             3
            m = p1.match(line)
            if m:
                group = m.groupdict()
                inner_packet_dict = {}
                inner_packet_dict["ospf-packet-type"] = group["ospf_packet_type"]
                inner_packet_dict["packets-sent"] = group["packets_sent"]
                inner_packet_dict["packets-received"] = group["packets_received"]
                inner_packet_dict["packets-sent-5seconds"] = group["packets_sent_5seconds"]
                inner_packet_dict["packets-received-5seconds"] = group["packets_received_5seconds"]

                packet_list.append(inner_packet_dict)
                ospf_area["packet-statistics"] = packet_list
                continue

            #DBDs retransmitted     :               203656, last 5 seconds :          0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ospf_area["dbds-retransmit"] = group["dbds_retransmit"]
                ospf_area["dbds-retransmit-5seconds"] = group["dbds_retransmit_5seconds"]
                continue

            #LSAs flooded           :             66582263, last 5 seconds :          0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ospf_area["lsas-flooded"] = group["lsas_flooded"]
                ospf_area["lsas-flooded-5seconds"] = group["lsas_flooded_5seconds"]
                continue

            #LSAs flooded high-prio :            375568998, last 5 seconds :          0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ospf_area["lsas-high-prio-flooded"] = group["lsas_high_prio_flooded"]
                ospf_area["lsas-high-prio-flooded-5seconds"] = group["lsas_high_prio_flooded_5seconds"]
                continue

            #LSAs retransmitted     :              8064643, last 5 seconds :          0
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ospf_area["lsas-retransmit"] = group["lsas_retransmit"]
                ospf_area["lsas-retransmit-5seconds"] = group["lsas_retransmit_5seconds"]
                continue

            #LSAs transmitted to nbr:              3423982, last 5 seconds :          0
            m = p6.match(line)
            if m:
                group = m.groupdict()
                ospf_area["lsas-nbr-transmit"] = group["lsas_nbr_transmit"]
                ospf_area["lsas-nbr-transmit-5seconds"] = group["lsas_nbr_transmit_5seconds"]
                continue

            #LSAs requested         :                 3517, last 5 seconds :          0
            m = p7.match(line)
            if m:
                group = m.groupdict()
                ospf_area["lsas-requested"] = group["lsas_requested"]
                ospf_area["lsas-requested-5seconds"] = group["lsas_requested_5seconds"]
                continue

            #LSAs acknowledged      :            225554974, last 5 seconds :          0
            m = p8.match(line)
            if m:
                group = m.groupdict()
                ospf_area["lsas-acknowledged"] = group["lsas_acknowledged"]
                ospf_area["lsas-acknowledged-5seconds"] = group["lsas_acknowledged_5seconds"]
                continue

            #Flood queue depth      :               0
            #Total rexmit entries   :               0
            #db summaries           :               0
            #lsreq entries          :               0
            m = p9.match(line)
            if m:
                group = m.groupdict()
                if re.search('(Flood +queue +depth)', group['pattern'].strip()):
                    key = 'flood-queue-depth'
                elif re.search('(Total +rexmit +entries)', group['pattern'].strip()):
                    key = 'total-retransmits'
                elif re.search('(db +summaries)', group['pattern'].strip()):
                    key = 'total-database-summaries'
                elif re.search('(lsreq +entries)', group['pattern'].strip()):
                    key = 'total-linkstate-request'
                else:
                    continue
                ospf_area[key] = group["value"]
                continue

            #12 subnet mismatches
            m = p10.match(line)
            if m:
                group = m.groupdict()
                inner_dict = {}
                inner_dict["subnet-mismatch-error"] = group["subnet_mismatch_error"]
                ospf_area["ospf-errors"] = inner_dict
                continue

        return ret_dict
