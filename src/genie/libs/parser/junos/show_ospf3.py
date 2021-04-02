''' show_ospf3.py

Parser for the following show commands:
    * show ospf3 interface
    * show ospf3 interface extensive
    * show ospf3 database
    * show ospf3 database extensive
    * show ospf3 database advertising-router {address} extensive
    * show ospf3 database {lsa_type} advertising-router {address} extensive
    * show ospf3 database external extensive
    * show ospf3 overview
    * show ospf3 overview extensive
    * show ospf3 database network detail
    * show ospf3 database link advertising-router {ipaddress} detail
    * show ospf3 neighbor
    * show ospf3 neighbor instance {instance_name}
    * show ospf3 neighbor instance all
'''
import re

from genie.metaparser import MetaParser
from pyats.utils.exceptions import SchemaError
from genie.metaparser.util.schemaengine import (Any, Optional, Use,
                                                Schema, ListOf)


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

    # Main Schema
    schema = {
        "ospf3-interface-information": {
            "ospf3-interface": ListOf({
                "bdr-id": str,
                "dr-id": str,
                "interface-name": str,
                "neighbor-count": str,
                "ospf-area": str,
                "ospf-interface-state": str
            })
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
        p1 = re.compile(
            r'^(?P<interface_name>\S+) +(?P<ospf_interface_state>\S+)'
            r' +(?P<ospf_area>[0-9]{1,3}(\.[0-9]{1,3}){3}) +(?P<dr_id>[0-9]{1,3}'
            r'(\.[0-9]{1,3}){3}) +(?P<bdr_id>[0-9]{1,3}(\.[0-9]{1,3}){3}) +(?P<neighbor_count>\S+)$'
        )

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
                    entry_key = group_key.replace('_', '-')
                    entry[entry_key] = group_value

                entry_list.append(entry)
                continue

        return ret_dict


# ==============================================
#  Schema for show ospf3 neighbor extensive
# ==============================================


class ShowOspf3NeighborExtensiveSchema(MetaParser):
    """schema = {
    "ospf3-neighbor-information": {
        "ospf3-neighbor": [
            {
                "activity-timer": str,
                "bdr-id": str,
                "dr-id": str,
                "interface-name": str,
                "neighbor-address": str,
                "neighbor-adjacency-time": {
                    "#text": str
                },
                "neighbor-id": str,
                "neighbor-priority": str,
                "neighbor-up-time": {},
                "options": str,
                "ospf-area": str,
                "ospf-neighbor-state": str,
                "ospf3-interface-index": str
            }
        ]
    }
}"""

    # Main Schema
    schema = {
        "ospf3-neighbor-information": {
            "ospf3-neighbor": ListOf({
                "activity-timer": str,
                "bdr-id": str,
                "dr-id": str,
                "interface-name": str,
                "neighbor-address": str,
                Optional("neighbor-adjacency-time"): {
                    "#text": str
                },
                "neighbor-id": str,
                "neighbor-priority": str,
                Optional("neighbor-up-time"): {
                    "#text": str
                },
                "options": str,
                "ospf-area": str,
                "ospf-neighbor-state": str,
                "ospf3-interface-index": str
            })
        }
    }


# ==============================================
#  Schema for show ospf3 neighbor extensive
# ==============================================
class ShowOspf3NeighborExtensive(ShowOspf3NeighborExtensiveSchema):
    """ Parser for:
            * show ospf3 neighbor extensive
    """

    cli_command = ['show ospf3 neighbor extensive']

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command[0])
        else:
            out = output

        ret_dict = {}

        #10.189.5.253     ge-0/0/0.0             Full      128     35
        p1 = re.compile(
            r'^(?P<neighborid>[\w\.\:\/]+) +(?P<interfacename>\S+) '
            r'+(?P<ospfneighborstate>\S+) +(?P<pri>\S+) +(?P<dead>\d+)$')

        #Neighbor-address fe80::250:56ff:fe8d:53c0
        p2 = re.compile(r'^Neighbor-address +(?P<neighbor_address>\S+)$')

        #Area 0.0.0.8, opt 0x13, OSPF3-Intf-Index 2
        p3 = re.compile(
            r'^Area +(?P<area>\S+), opt +(?P<opt>\S+), OSPF3-Intf-Index +(?P<ospf3>\d+)$'
        )

        #DR-ID 0.0.0.0, BDR-ID 0.0.0.0
        p4 = re.compile(r'^DR-ID +(?P<drid>\S+), BDR-ID +(?P<bdrid>\S+)$')

        #Up 3w0d 17:07:00, adjacent 3w0d 17:07:00
        #Up 00:00:08
        p5 = re.compile(
            r'^Up +(?P<up>\S+( +[\d\:]+)?)(, +adjacent +(?P<adjacent>\S+ +[\d\:]+))?$'
        )

        for line in out.splitlines():
            line = line.strip()

            #10.189.5.253     ge-0/0/0.0             Full      128     35
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ospf3_entry_list = ret_dict.setdefault('ospf3-neighbor-information', {}).\
                    setdefault('ospf3-neighbor', [])
                ospf3_entry_dict = {}
                ospf3_entry_dict['activity-timer'] = group['dead']
                ospf3_entry_dict['neighbor-id'] = group['neighborid']
                ospf3_entry_dict['interface-name'] = group['interfacename']
                ospf3_entry_dict['ospf-neighbor-state'] = group[
                    'ospfneighborstate']
                ospf3_entry_dict['neighbor-priority'] = group['pri']
                ospf3_entry_list.append(ospf3_entry_dict)
                continue

            #Neighbor-address fe80::250:56ff:fe8d:53c0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ospf3_entry_dict['neighbor-address'] = group[
                    'neighbor_address']
                continue

            #Area 0.0.0.8, opt 0x13, OSPF3-Intf-Index 2
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ospf3_entry_dict['ospf-area'] = group['area']
                ospf3_entry_dict['options'] = group['opt']
                ospf3_entry_dict['ospf3-interface-index'] = group['ospf3']
                continue

            #DR-ID 0.0.0.0, BDR-ID 0.0.0.0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ospf3_entry_dict['dr-id'] = group['drid']
                ospf3_entry_dict['bdr-id'] = group['bdrid']
                continue

            #Up 3w0d 17:07:00, adjacent 3w0d 17:07:00
            m = p5.match(line)
            if m:
                group = m.groupdict()
                if group['adjacent']:
                    ospf3_entry_dict['neighbor-adjacency-time'] = {
                        '#text': group['adjacent']
                    }
                ospf3_entry_dict['neighbor-up-time'] = {'#text': group['up']}
                continue

        return ret_dict


# ==============================================
# Schema for 'show ospf3 neighbor'
# ==============================================


class ShowOspf3NeighborSchema(MetaParser):
    """schema = {
    "ospf3-neighbor-information": {
        "ospf3-neighbor": [
            {
                "activity-timer": str,
                "interface-name": str,
                "neighbor-address": str,
                "neighbor-id": str,
                "neighbor-priority": str,
                "ospf-neighbor-state": str
            }
        ]
   }
}"""

    # Main Schema
    schema = {
        "ospf3-neighbor-information": {
            "ospf3-neighbor": ListOf({
                "activity-timer": str,
                "interface-name": str,
                "neighbor-address": str,
                "neighbor-id": str,
                "neighbor-priority": str,
                "ospf-neighbor-state": str
            })
        }
    }


# ==============================================
# Parser for 'show ospf3 neighbor'
# ==============================================
class ShowOspf3Neighbor(ShowOspf3NeighborSchema):
    """ Parser for:
            * show ospf3 neighbor
    """

    cli_command = ['show ospf3 neighbor', 'show ospf3 neighbor instance {name}']

    def cli(self, name=None, output=None):
        if not output:
            if name:
                out = self.device.execute(self.cli_command[1].format(name=name))
            else:
                out = self.device.execute(self.cli_command[0])
        else:
            out = output

        ret_dict = {}

        #10.189.5.253     ge-0/0/0.0             Full      128     35
        p1 = re.compile(r'^(?P<id>[\d\.]+) +(?P<interface>\S+) '
                        r'+(?P<state>\S+) +(?P<pri>\S+) +(?P<dead>\d+)$')

        #Neighbor-address fe80::250:56ff:fe8d:53c0
        p2 = re.compile(r'^Neighbor-address +(?P<neighbor_address>\S+)$')

        for line in out.splitlines():
            line = line.strip()

            #10.189.5.253     ge-0/0/0.0             Full      128     35
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ospf3_entry_list = ret_dict.setdefault('ospf3-neighbor-information', {}).\
                    setdefault('ospf3-neighbor', [])
                ospf3_entry_dict = {}
                ospf3_entry_dict['activity-timer'] = group['dead']
                ospf3_entry_dict['interface-name'] = group['interface']
                ospf3_entry_dict['neighbor-id'] = group['id']
                ospf3_entry_dict['neighbor-priority'] = group['pri']
                ospf3_entry_dict['ospf-neighbor-state'] = group['state']
                continue

            #Neighbor-address fe80::250:56ff:fe8d:53c0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                neighbor_address = group['neighbor_address']
                ospf3_entry_dict['neighbor-address'] = neighbor_address
                ospf3_entry_list.append(ospf3_entry_dict)
                continue
            
            
        return ret_dict


class ShowOspf3NeighborInstance(ShowOspf3Neighbor):
    """ Parser for:
            * show ospf3 neighbor instance {instance_name}
    """

    cli_command = 'show ospf3 neighbor instance {instance_name}'

    def cli(self, instance_name, output=None):
        if not output:
            out = self.device.execute(self.cli_command.format(
                                        instance_name=instance_name))
        else:
            out = output

        return super().cli(
            output=' ' if not out else out
            )


class ShowOspf3NeighborDetail(ShowOspf3NeighborExtensive):
    """ Parser for:
            - show ospf3 neighbor detail
    """

    cli_command = ['show ospf3 neighbor detail']

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command[0])
        else:
            out = output

        return super().cli(output=out)


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

    # Main Schema
    schema = {
        "ospf3-database-information": ListOf({
            "ospf3-area-header": {
                "ospf-area": str
            },
            "ospf3-database": ListOf({
                "advertising-router": str,
                "age": str,
                "checksum": str,
                "lsa-id": str,
                "lsa-length": str,
                "lsa-type": str,
                "sequence-number": str,
                Optional('our-entry'): bool
            }),
            Optional("ospf3-intf-header"): ListOf({
                "ospf-area": str,
                "ospf-intf": str
            }),
        })
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
        p1 = re.compile(
            r'^OSPF3( +)database,( +)Area( +)'
            r'(?P<ospf_area>(\*{0,1})[0-9]{1,3}(\.[0-9]{1,3}){3})$')

        # Type       ID               Adv Rtr           Seq         Age  Cksum  Len
        # Router      0.0.0.0          10.34.2.250     0x800018ed  2407  0xaf2d  56
        p2 = re.compile(
            r'^(?P<lsa_type>\S+) +(?P<lsa_id>(\*{0,1})[0-9]{1,3}'
            r'(\.[0-9]{1,3}){3}) +(?P<advertising_router>[0-9]{1,3}(\.[0-9]{1,3})'
            r'{3}) +(?P<sequence_number>\S+) +(?P<age>\d+) +(?P<checksum>\S+) +(?P<lsa_length>\d+)$'
        )

        # OSPF3 Link-Local database, interface ge-0/0/0.0 Area 0.0.0.8
        p3 = re.compile(
            r'^OSPF3( +)Link-Local( +)database,( +)interface( +)'
            r'(?P<ospf_intf>\S+)( +)Area( +)(?P<ospf_area>[0-9]{1,3}(\.[0-9]{1,3}){3})$'
        )

        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()
            #    OSPF3 database, Area 0.0.0.8
            m = p1.match(line)
            if m:
                entry_list = ret_dict.setdefault("ospf3-database-information",
                                                 [])

                entry = {}

                group = m.groupdict()

                entry.setdefault("ospf3-area-header",
                                 {}).setdefault("ospf-area",
                                                group["ospf_area"])

                entry_list.append(entry)
                continue

            # Router      0.0.0.0          10.34.2.250     0x800018ed  2407  0xaf2d  56
            m = p2.match(line)
            if m:
                entry_list = ret_dict.setdefault("ospf3-database-information",
                                                 [])[-1].setdefault(
                                                     "ospf3-database", [])

                group = m.groupdict()
                entry = {}
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_', '-')
                    entry[entry_key] = group_value

                lsa_id = entry['lsa-id']
                if lsa_id[0] == '*':
                    entry['lsa-id'] = lsa_id[1:]
                    entry['our-entry'] = True

                entry_list.append(entry)

                continue

            # OSPF3 Link-Local database, interface ge-0/0/0.0 Area 0.0.0.8
            m = p3.match(line)
            if m:
                entry_list = ret_dict.setdefault("ospf3-database-information",
                                                 [])[-1].setdefault(
                                                     "ospf3-intf-header", [])

                group = m.groupdict()
                entry = {}
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_', '-')
                    entry[entry_key] = group_value

                entry_list.append(entry)

                continue

        return ret_dict


class ShowOspf3InterfaceExtensiveSchema(MetaParser):
    """ Schema for:
            * show ospf3 interface extensive
    """

    schema = {
        "ospf3-interface-information": {
            "ospf3-interface": ListOf({
                "adj-count": str,
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
                "ospf-stub-type": str,
                "ospf3-interface-index": str,
                Optional("ospf3-router-lsa-id"): str,
                "prefix-length": str,
                "retransmit-interval": str,
                Optional("router-priority"): str,
                Optional("dr-address"): str,
                Optional("br-address"): str
            })
        }
    }


class ShowOspf3InterfaceExtensive(ShowOspf3InterfaceExtensiveSchema):
    """ Parser for:
    * show ospf3 interface extensive
    """
    cli_command = 'show ospf3 interface extensive'

    def cli(self, output=None):

        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # ge-0/0/0.0          PtToPt  0.0.0.8         0.0.0.0         0.0.0.0            1
        p1 = re.compile(
            r'^(?P<interface_name>\S+)( +)(?P<ospf_interface_state>\S+)'
            r'( +)(?P<ospf_area>[\d\.]+)( +)(?P<dr_id>[\d\.]+)( +)'
            r'(?P<bdr_id>[\d\.]+)( +)(?P<neighbor_count>\d+)$')

        # Address fe80::250:56ff:fe8d:c829, Prefix-length 64
        p2 = re.compile(
            r'Address( +)(?P<interface_address>\S+),( +)Prefix-length'
            r'( +)(?P<prefix_length>\d+)')

        # OSPF3-Intf-index 2, Type P2P, MTU 1500, Cost 5
        p3 = re.compile(
            r'^OSPF3-Intf-index( +)(?P<ospf3_interface_index>\d+),( +)'
            r'Type( +)(?P<interface_type>\S+),( +)MTU( +)(?P<mtu>\d+),( +)Cost( +)'
            r'(?P<interface_cost>\d+)$')

        # Adj count: 1, Router LSA ID: 0
        p4 = re.compile(
            r'^Adj( +)count:( +)(?P<adj_count>\d+),( +)Router( +)LSA'
            r'( +)ID:( +)(?P<ospf3_router_lsa_id>\S+)(, \S+)?$')

        # Hello 10, Dead 40, ReXmit 5, Not Stub
        p5 = re.compile(
            r'^Hello( +)(?P<hello_interval>\d+),( +)Dead( +)'
            r'(?P<dead_interval>\d+),( +)ReXmit( +)(?P<retransmit_interval>\d+),'
            r'( +)(?P<ospf_stub_type>(\S+ ){0,1}\S+)$')

        # Protection type: None
        p6 = re.compile(
            r'^Protection( +)type:( +)(?P<ospf_interface_protection_type>\S+)$'
        )

        #   OSPF3-Intf-index 1, Type LAN, MTU 65535, Cost 0, Priority 128
        p7 = re.compile(
            r'^OSPF3-Intf-index( +)(?P<ospf3_interface_index>\d+),( +)'
            r'Type( +)(?P<interface_type>\S+),( +)MTU( +)(?P<mtu>\d+),( +)Cost( +)'
            r'(?P<interface_cost>\d+),( +)Priority( +)(?P<router_priority>\d+)$'
        )

        # DR addr fe80::250:560f:fc8d:7c08
        p8 = re.compile(r'^DR( +)addr( +)(?P<dr_address>\S+)$')

        # DR addr fe80::250:560f:fc8d:7c08 BDR addr fe80::250:560f:fc8d:7c08
        p9 = re.compile(r'^DR addr +(?P<dr_address>\S+), BDR addr +(?P<br_address>\S+)$')

        # Validate each dictionary in list
        for line in out.splitlines():
            line = line.strip()
            # ge-0/0/0.0          PtToPt  0.0.0.8         0.0.0.0         0.0.0.0            1
            m = p1.match(line)
            if m:
                interface_list = ret_dict.setdefault("ospf3-interface-information", {})\
                    .setdefault("ospf3-interface", [])

                group = m.groupdict()
                entry = {}
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_', '-')
                    entry[entry_key] = group_value

                interface_list.append(entry)
                continue

            # Address fe80::250:56ff:fe8d:c829, Prefix-length 64
            m = p2.match(line)
            if m:
                last_interface = ret_dict["ospf3-interface-information"][
                    "ospf3-interface"][-1]

                group = m.groupdict()
                entry = last_interface
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_', '-')
                    entry[entry_key] = group_value

                continue

            # OSPF3-Intf-index 2, Type P2P, MTU 1500, Cost 5
            m = p3.match(line)
            if m:
                last_interface = ret_dict["ospf3-interface-information"][
                    "ospf3-interface"][-1]

                group = m.groupdict()
                entry = last_interface
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_', '-')
                    entry[entry_key] = group_value

                continue

            # Adj count: 1, Router LSA ID: 0
            m = p4.match(line)
            if m:
                last_interface = ret_dict["ospf3-interface-information"][
                    "ospf3-interface"][-1]

                group = m.groupdict()
                entry = last_interface
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_', '-')
                    entry[entry_key] = group_value

                if entry['ospf3-router-lsa-id'] == '-':
                    del entry['ospf3-router-lsa-id']

                continue

            # Hello 10, Dead 40, ReXmit 5, Not Stub
            m = p5.match(line)
            if m:
                last_interface = ret_dict["ospf3-interface-information"][
                    "ospf3-interface"][-1]

                group = m.groupdict()
                entry = last_interface
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_', '-')
                    entry[entry_key] = group_value

                continue

            # Protection type: None
            m = p6.match(line)
            if m:
                last_interface = ret_dict["ospf3-interface-information"][
                    "ospf3-interface"][-1]

                group = m.groupdict()
                entry = last_interface
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_', '-')
                    entry[entry_key] = group_value

                continue

            #   OSPF3-Intf-index 1, Type LAN, MTU 65535, Cost 0, Priority 128
            m = p7.match(line)
            if m:
                last_interface = ret_dict["ospf3-interface-information"][
                    "ospf3-interface"][-1]

                group = m.groupdict()
                entry = last_interface
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_', '-')
                    entry[entry_key] = group_value

                continue

            # DR addr fe80::250:560f:fc8d:7c08
            m = p8.match(line)
            if m:
                last_interface = ret_dict["ospf3-interface-information"][
                    "ospf3-interface"][-1]

                group = m.groupdict()
                entry = last_interface
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_', '-')
                    entry[entry_key] = group_value

                continue

            # DR addr fe80::250:560f:fc8d:7c08 BR addr fe80::250:560f:fc8d:7c08
            m = p9.match(line)
            if m:
                last_interface = ret_dict["ospf3-interface-information"][
                    "ospf3-interface"][-1]

                group = m.groupdict()
                entry = last_interface
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_', '-')
                    entry[entry_key] = group_value

                continue
            
        return ret_dict


class ShowOspf3DatabaseExternalExtensiveSchema(MetaParser):
    """ Schema for:
            * show ospf3 database external extensive
    """

    schema = {
        "ospf3-database-information": {
            "ospf3-database": ListOf({
                "advertising-router": str,
                "age": str,
                "checksum": str,
                "lsa-id": str,
                "lsa-length": str,
                "lsa-type": str,
                Optional('our-entry'): bool,
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
                    "lsa-change-count": str,
                    "lsa-changed-time": {
                        "#text": str
                    },
                    Optional("send-time"): {
                        "#text": str
                    },
                    Optional("database-entry-state"): str
                },
                "ospf3-external-lsa": {
                    "metric": str,
                    "ospf3-prefix": str,
                    "ospf3-prefix-options": str,
                    "type-value": str
                },
                "sequence-number": str
            })
        }
    }


class ShowOspf3DatabaseExternalExtensive(
        ShowOspf3DatabaseExternalExtensiveSchema):
    """ Parser for:
            * show ospf3 database external extensive
    """
    cli_command = 'show ospf3 database external extensive'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # Extern      0.0.0.1          10.34.2.250     0x8000178e  1412  0x3c81  28
        p1 = re.compile(
            r'^(?P<lsa_type>\S+) +(?P<lsa_id>(\*{0,1})[\d\.]+) +'
            r'(?P<advertising_router>[\d\.]+) +(?P<sequence_number>\S+) +(?P<age>\d+)'
            r' +(?P<checksum>\S+) +(?P<lsa_length>\d+)$')

        # Prefix ::/0
        p2 = re.compile(r'^Prefix +(?P<ospf3_prefix>\S+)$')

        # Prefix-options 0x0, Metric 1, Type 1,
        p3 = re.compile(
            r'^Prefix-options +(?P<ospf3_prefix_options>\S+),'
            r' Metric +(?P<metric>\d+), +Type +(?P<type_value>\d+),$')

        # Aging timer 00:36:27
        p4 = re.compile(r'^Aging +timer +(?P<aging_timer>(\S+ ){0,1}[\d:]+)$')

        # Gen timer 00:49:49
        p5 = re.compile(r'^Gen +timer +(?P<generation_timer>\S+)$')

        # Installed 00:23:26 ago, expires in 00:36:28, sent 00:23:24 ago
        p6 = re.compile(
            r'^Installed +(?P<installation_time>(\S+ ){0,1}[\d:]+)'
            r' ago, +expires +in +(?P<expiration_time>(\S+ ){0,1}[\d:]+),'
            r' sent +(?P<send_time>(\S+ ){0,1}[\d:]+) +ago$')

        # Last changed 29w5d 21:04:29 ago, Change count: 1
        p7 = re.compile(
            r'^Last +changed +(?P<lsa_changed_time>(\S+ ){0,1}[\d:]+)'
            r' ago, +Change +count: +(?P<lsa_change_count>\d+)$')

        # Last changed 3w0d 17:02:47 ago, Change count: 2, Ours
        p8 = re.compile(
            r'^Last +changed +(?P<lsa_changed_time>(\S+ ){0,1}[\d:]+)'
            r' ago, +Change +count: +(?P<lsa_change_count>\d+), +(?P<database_entry_state>\S+)$'
        )

        for line in out.splitlines():
            line = line.strip()

            # Extern      0.0.0.1          10.34.2.250     0x8000178e  1412  0x3c81  28
            m = p1.match(line)
            if m:
                entry_list = ret_dict.setdefault("ospf3-database-information", {})\
                    .setdefault("ospf3-database", [])

                group = m.groupdict()
                entry = {}
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_', '-')
                    entry[entry_key] = group_value

                if entry['lsa-id'][0] == "*":
                    entry['lsa-id'] = entry['lsa-id'][1:]
                    entry['our-entry'] = True

                entry_list.append(entry)
                continue

            # Prefix ::/0
            m = p2.match(line)
            if m:
                last_database = ret_dict["ospf3-database-information"][
                    "ospf3-database"][-1]

                group = m.groupdict()

                entry = last_database.setdefault("ospf3-external-lsa", {})
                entry['ospf3-prefix'] = group['ospf3_prefix']

                continue

            # Prefix-options 0x0, Metric 1, Type 1,
            m = p3.match(line)
            if m:
                last_database = ret_dict["ospf3-database-information"][
                    "ospf3-database"][-1]

                group = m.groupdict()
                entry = last_database.setdefault("ospf3-external-lsa", {})
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_', '-')
                    entry[entry_key] = group_value

                continue

            # Aging timer 00:36:27
            m = p4.match(line)
            if m:
                last_database = ret_dict["ospf3-database-information"][
                    "ospf3-database"][-1]
                last_database.setdefault("ospf-database-extensive",
                                         {}).setdefault("aging-timer", {})

                group = m.groupdict()
                last_database["ospf-database-extensive"]["aging-timer"][
                    "#text"] = group['aging_timer']

                continue

            # Gen timer 00:49:49
            m = p5.match(line)
            if m:
                last_database = ret_dict["ospf3-database-information"][
                    "ospf3-database"][-1]

                last_database.setdefault("ospf-database-extensive", {})\
                    .setdefault("generation-timer", {})

                group = m.groupdict()
                last_database["ospf-database-extensive"]["generation-timer"]["#text"]\
                     = group['generation_timer']

                continue

            # Installed 00:23:26 ago, expires in 00:36:28, sent 00:23:24 ago
            m = p6.match(line)
            if m:
                last_database = ret_dict["ospf3-database-information"][
                    "ospf3-database"][-1]

                last_database.setdefault("ospf-database-extensive", {})\
                    .setdefault("expiration-time", {})
                last_database.setdefault("ospf-database-extensive", {})\
                    .setdefault("installation-time", {})
                last_database.setdefault("ospf-database-extensive", {})\
                    .setdefault("send-time", {})

                group = m.groupdict()
                last_database["ospf-database-extensive"]["expiration-time"]["#text"]\
                     = group['expiration_time']
                last_database["ospf-database-extensive"]["installation-time"]["#text"]\
                     = group['installation_time']
                last_database["ospf-database-extensive"]["send-time"]["#text"]\
                     = group['send_time']

                continue

            # Last changed 29w5d 21:04:29 ago, Change count: 1
            m = p7.match(line)
            if m:
                last_database = ret_dict["ospf3-database-information"][
                    "ospf3-database"][-1]

                last_database.setdefault("ospf-database-extensive",
                                         {}).setdefault(
                                             "lsa-changed-time", {})

                group = m.groupdict()
                last_database["ospf-database-extensive"]["lsa-changed-time"]["#text"]\
                    = group['lsa_changed_time']
                last_database["ospf-database-extensive"]["lsa-change-count"]\
                    = group['lsa_change_count']

                continue

            # Last changed 29w5d 21:40:56 ago, Change count: 1, Ours
            m = p8.match(line)
            if m:
                last_database = ret_dict["ospf3-database-information"][
                    "ospf3-database"][-1]

                last_database.setdefault("ospf-database-extensive", {})\
                    .setdefault("lsa-changed-time", {})

                group = m.groupdict()
                last_database["ospf-database-extensive"]["lsa-changed-time"]["#text"]\
                    = group['lsa_changed_time']
                last_database["ospf-database-extensive"]["lsa-change-count"]\
                    = group['lsa_change_count']
                last_database["ospf-database-extensive"]["database-entry-state"]\
                    = group['database_entry_state']

                continue

        return ret_dict


# ==============================================
#  Schema for show ospf3 overview
# ==============================================


class ShowOspf3OverviewSchema(MetaParser):
    schema = {
        "ospf3-overview-information": {
            "ospf-overview": {
                "instance-name": str,
                "ospf-area-overview": {
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
                Optional("ospf-tilfa-overview"): {
                    "ospf-tilfa-enabled": str
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


# ==============================================
#  Parser for show ospf3 overview
# ==============================================
class ShowOspf3Overview(ShowOspf3OverviewSchema):
    """ Parser for:
            * show ospf3 overview
    """

    cli_command = ['show ospf3 overview']

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command[0])
        else:
            out = output

        ret_dict = {}

        #Instance: master
        p1 = re.compile(r'^Instance: +(?P<instance_name>\S+)$')

        #Router ID: 10.189.5.252
        p2 = re.compile(r'^Router ID: +(?P<ospf_router_id>[\w\.\:\/]+)$')

        #Route table index: 0
        p3 = re.compile(
            r'^Route table index: +(?P<ospf_route_table_index>\d+)$')

        #LSA refresh time: 50 minutes
        p5 = re.compile(
            r'^LSA refresh time: +(?P<ospf_lsa_refresh_time>\d+) minutes$')

        #Post Convergence Backup: Disabled
        p6 = re.compile(
            r'^Post Convergence Backup: +(?P<ospf_tilfa_enabled>\S+)$')

        #Area: 0.0.0.8
        p7 = re.compile(r'^Area: +(?P<ospf_area>[\w\.\:\/]+)$')

        #Stub type: Not Stub
        p8 = re.compile(r'^Stub type: +(?P<ospf_stub_type>[\S\s]+)$')

        #Area border routers: 0, AS boundary routers: 5
        p9 = re.compile(
            r'^Area border routers: +(?P<ospf_abr_count>\d+), AS boundary routers: +(?P<ospf_asbr_count>\d+)$'
        )

        #Up (in full state): 2
        p10 = re.compile(
            r'^Up \(in full state\): +(?P<ospf_nbr_up_count>\d+)$')

        #Topology: default (ID 0)
        p11 = re.compile(
            r'^Topology: +(?P<ospf_topology_name>\S+) \(ID +(?P<ospf_topology_id>\d+)\)$'
        )

        #Prefix export count: 1
        p12 = re.compile(
            r'^Prefix export count: +(?P<ospf_prefix_export_count>\d+)$')

        #Full SPF runs: 1934
        p13 = re.compile(r'^Full SPF runs: +(?P<ospf_full_spf_count>\d+)$')

        #SPF delay: 0.200000 sec, SPF holddown: 2 sec, SPF rapid runs: 3
        p14 = re.compile(
            r'^SPF delay: +(?P<ospf_spf_delay>[\w\.\:\/]+) sec, SPF holddown: +(?P<ospf_spf_holddown>[\w\.]+) sec, SPF rapid runs: +(?P<ospf_spf_rapid_runs>[\w\.]+)$'
        )

        #Backup SPF: Not Needed
        p15 = re.compile(r'^Backup SPF: +(?P<ospf_backup_spf_status>[\S\s]+)$')

        # Configured overload, expires in 14 seconds
        p16 = re.compile(
            r'^Configured +overload, +expires +in +'
            r'(?P<ospf_configured_overload_remaining_time>\d+) +\S+$'
        )

        for line in out.splitlines():
            line = line.strip()

            #Instance: master
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ospf3_entry_list = ret_dict.setdefault('ospf3-overview-information', {}).\
                    setdefault('ospf-overview', {})
                ospf3_entry_list['instance-name'] = group['instance_name']
                continue

            #Router ID: 10.189.5.252
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ospf3_entry_list['ospf-router-id'] = group['ospf_router_id']
                continue

            #Route table index: 0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ospf3_entry_list['ospf-route-table-index'] = group[
                    'ospf_route_table_index']
                continue

            #LSA refresh time: 50 minute
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ospf3_entry_list['ospf-lsa-refresh-time'] = group[
                    'ospf_lsa_refresh_time']
                continue

            #Post Convergence Backup: Disabled
            m = p6.match(line)
            if m:
                group = m.groupdict()
                ospf3_entry_list['ospf-tilfa-overview'] = {
                    'ospf-tilfa-enabled': group['ospf_tilfa_enabled']
                }
                continue

            #Area: 0.0.0.8
            m = p7.match(line)
            if m:
                group = m.groupdict()
                ospf3_area_entry_dict = ospf3_entry_list.setdefault(
                    'ospf-area-overview', {})
                ospf3_area_entry_dict.update({'ospf-area': group['ospf_area']})
                continue

            #Stub type: Not Stub
            m = p8.match(line)
            if m:
                group = m.groupdict()
                ospf3_area_entry_dict.update(
                    {'ospf-stub-type': group['ospf_stub_type']})
                continue

            #Area border routers: 0, AS boundary routers: 5
            m = p9.match(line)
            if m:
                group = m.groupdict()
                ospf3_area_entry_dict.update(
                    {'ospf-abr-count': group['ospf_abr_count']})
                ospf3_area_entry_dict.update(
                    {'ospf-asbr-count': group['ospf_asbr_count']})
                continue

            #Up (in full state): 2
            m = p10.match(line)
            if m:
                group = m.groupdict()
                ospf3_area_entry_dict.setdefault(
                    'ospf-nbr-overview',
                    {"ospf-nbr-up-count": group['ospf_nbr_up_count']})
                continue

            #Topology: default (ID 0)
            m = p11.match(line)
            if m:
                group = m.groupdict()
                ospf3_topology_entry_dict = ospf3_entry_list.setdefault(
                    'ospf-topology-overview', {})
                ospf3_topology_entry_dict.update(
                    {'ospf-topology-name': group['ospf_topology_name']})
                ospf3_topology_entry_dict.update(
                    {'ospf-topology-id': group['ospf_topology_id']})
                continue

            #Prefix export count: 1
            m = p12.match(line)
            if m:
                group = m.groupdict()
                ospf3_topology_entry_dict.update({
                    'ospf-prefix-export-count':
                    group['ospf_prefix_export_count']
                })
                continue

            #Full SPF runs: 1934
            m = p13.match(line)
            if m:
                group = m.groupdict()
                ospf3_topology_entry_dict.update(
                    {'ospf-full-spf-count': group['ospf_full_spf_count']})
                continue

            #SPF delay: 0.200000 sec, SPF holddown: 2 sec, SPF rapid runs: 3
            m = p14.match(line)
            if m:
                group = m.groupdict()
                ospf3_topology_entry_dict.update(
                    {'ospf-spf-delay': group['ospf_spf_delay']})
                ospf3_topology_entry_dict.update(
                    {'ospf-spf-holddown': group['ospf_spf_holddown']})
                ospf3_topology_entry_dict.update(
                    {'ospf-spf-rapid-runs': group['ospf_spf_rapid_runs']})
                continue

            #Backup SPF: Not Needed
            m = p15.match(line)
            if m:
                group = m.groupdict()
                ospf3_topology_entry_dict.update({
                    'ospf-backup-spf-status':
                    group['ospf_backup_spf_status']
                })
                continue

            # Configured overload, expires in 14 seconds
            m = p16.match(line)
            if m:
                group = m.groupdict()
                ospf3_entry_list["ospf-configured-overload-remaining-time"] = \
                    group["ospf_configured_overload_remaining_time"]
                continue

        return ret_dict


class ShowOspf3OverviewExtensive(ShowOspf3Overview):
    """ Parser for:
            - show ospf3 overview extensive
    """

    cli_command = ['show ospf3 overview extensive']

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command[0])
        else:
            out = output

        return super().cli(output=out)


# ==============================================
#  Parser for show ospf3 database extensive
# ==============================================


class ShowOspf3DatabaseExtensiveSchema(MetaParser):
    """
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
                    "ospf3-inter-area-prefix-lsa" : {
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
    """

    schema = {
        "ospf3-database-information": {
            Optional("ospf3-area-header"): {
                "ospf-area": str
            },
            "ospf3-database": ListOf({
                "advertising-router": str,
                "age": str,
                "checksum": str,
                "lsa-id": str,
                Optional("our-entry"): bool,
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
                    Optional("ospf3-intra-area-prefix-lsa"): {
                        Optional("prefix-count"): str,
                        Optional("reference-lsa-id"): str,
                        Optional("reference-lsa-router-id"): str,
                        Optional("reference-lsa-type"): str,
                        "ospf3-prefix": list,
                        "ospf3-prefix-metric": list,
                        "ospf3-prefix-options": list,
                    },
                    Optional("ospf3-inter-area-prefix-lsa"): {
                        Optional("prefix-count"): str,
                        Optional("reference-lsa-id"): str,
                        Optional("reference-lsa-router-id"): str,
                        Optional("reference-lsa-type"): str,
                        "ospf3-prefix": list,
                        "ospf3-prefix-metric": list,
                        "ospf3-prefix-options": list,
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
                    Optional("database-entry-state"): str,
                },
                Optional("ospf3-intra-area-prefix-lsa"): {
                    Optional("prefix-count"): str,
                    Optional("reference-lsa-id"): str,
                    Optional("reference-lsa-router-id"): str,
                    Optional("reference-lsa-type"): str,
                    "ospf3-prefix": list,
                    "ospf3-prefix-metric": list,
                    "ospf3-prefix-options": list,
                },
                Optional("ospf3-inter-area-prefix-lsa"): {
                    Optional("prefix-count"): str,
                    Optional("reference-lsa-id"): str,
                    Optional("reference-lsa-router-id"): str,
                    Optional("reference-lsa-type"): str,
                    "ospf3-prefix": list,
                    "ospf3-prefix-metric": list,
                    "ospf3-prefix-options": list,
                },
                Optional("ospf3-router-lsa"): {
                    Optional("bits"):
                    str,
                    Optional("ospf3-options"):
                    str,
                    Optional("ospf3-link"): ListOf({
                        "link-intf-id": str,
                        "link-metric": str,
                        "link-type-name": str,
                        "link-type-value": str,
                        "nbr-intf-id": str,
                        "nbr-rtr-id": str,
                    }),
                    Optional("ospf3-lsa-topology"): {
                        "ospf-topology-id":
                        str,
                        "ospf-topology-name":
                        str,
                        "ospf3-lsa-topology-link": ListOf({
                            "link-type-name": str,
                            "ospf-lsa-topology-link-metric": str,
                            "ospf-lsa-topology-link-node-id": str,
                            "ospf-lsa-topology-link-state": str,
                        }),
                    },
                },
                Optional("ospf3-link-lsa"): {
                    "linklocal-address": str,
                    "ospf3-options": str,
                    Optional("ospf3-prefix"): str,
                    Optional("ospf3-prefix-options"): str,
                    "prefix-count": str,
                    "router-priority": str,
                },
                Optional("ospf3-external-lsa"): {
                    "metric": str,
                    "ospf3-prefix": str,
                    "ospf3-prefix-options": str,
                    "type-value": str,
                },
            }),
            Optional("ospf3-intf-header"): ListOf({
                "ospf-area": str,
                "ospf-intf": str
            }),
        }
    }


class ShowOspf3DatabaseExtensive(ShowOspf3DatabaseExtensiveSchema):
    """ Parser for:
    * show ospf3 database extensive
    * show ospf3 database advertising-router {address} extensive
    * show ospf3 database {lsa_type} advertising-router {address} extensive
    """

    cli_command = [
        "show ospf3 database extensive",
        "show ospf3 database advertising-router {address} extensive",
        "show ospf3 database {lsa_type} advertising-router {address} extensive"]

    def cli(self, lsa_type=None, address=None, output=None):
        if not output:
            if lsa_type and address:
                out = self.device.execute(self.cli_command[2].format(
                    address=address,
                    lsa_type=lsa_type))
            elif address:
                out = self.device.execute(self.cli_command[1].format(address=address))
            else:
                out = self.device.execute(self.cli_command[0])
        else:
            out = output

        ret_dict = {}

        self.state = None

        #    OSPF3 database, Area 0.0.0.8
        p1 = re.compile(r"^OSPF3( +)database,( +)Area( +)"
                        r"(?P<ospf_area>[\d\.]+)$")

        # Type       ID               Adv Rtr           Seq         Age  Cksum  Len
        # Router      0.0.0.0          10.34.2.250     0x800018ed  2407  0xaf2d  56
        p2 = re.compile(
            r"^(?P<lsa_type>\S+) +(?P<lsa_id>(\*{0,1})[\d\.]+) +(?P<advertising_router>[0-9][\d\.]+)"
            r" +(?P<sequence_number>\S+) +(?P<age>\d+) +(?P<checksum>\S+) +(?P<lsa_length>\d+)$"
        )

        # bits 0x2, Options 0x33
        p3 = re.compile(
            r"^bits +(?P<bits>\S+), +Options +(?P<ospf3_options>\S+)$")

        #  Type: PointToPoint, Node ID: 10.169.14.240, Metric: 100, Bidirectional
        p4 = re.compile(
            r"^Type: +(?P<link_type_name>\S+), +Node +ID: +(?P<ospf_lsa_topology_link_node_id>[\d\.]+)"
            r", +Metric: +(?P<ospf_lsa_topology_link_metric>\d+), +(?P<ospf_lsa_topology_link_state>\S+)$"
        )

        # Aging timer 00:18:16
        p5 = re.compile(r"^Aging timer +(?P<aging_timer>(\S+ ){0,1}[\d\:]+)$")

        # Installed 00:10:20 ago, expires in 00:49:31, sent 00:10:18 ago
        p6 = re.compile(
            r"^Installed +(?P<installation_time>(\S+ ){0,1}[\d\:]+) +ago, +expires +in +"
            r"(?P<expiration_time>(\S+ ){0,1}[\d\:]+), +sent +(?P<send_time>(\S+ ){0,1}[\d\:]+) +ago$"
        )

        # Last changed 2w6d 04:50:31 ago, Change count: 196
        p7 = re.compile(
            r"^Last changed +(?P<lsa_changed_time>(\S+ ){0,1}[\d\:]+) +ago, +Change +"
            r"count: +(?P<lsa_change_count>\d+)$")

        # Ref-lsa-type Router, Ref-lsa-id 0.0.0.0, Ref-router-id 10.34.2.250
        p8 = re.compile(
            r"^Ref-lsa-type +(?P<reference_lsa_type>\S+), +Ref-lsa-id +(?P<reference_lsa_id>[\d\.]+)"
            r", +Ref-router-id +(?P<reference_lsa_router_id>[\d\.]+)$")

        # Prefix-count 3
        p9 = re.compile(r"^Prefix-count +(?P<prefix_count>\d+)$")

        # Prefix 2001:db8:b0f8:3ab::/64
        p10 = re.compile(r"^Prefix +(?P<ospf3_prefix>\S+)$")

        # Prefix-options 0x0, Metric 5
        p11 = re.compile(
            r"^Prefix-options +(?P<ospf3_prefix_options>\S+), +Metric +(?P<metric>\d+)$"
        )

        # fe80::250:56ff:fe8d:a96c
        p12 = re.compile(r"^(?P<linklocal_address>[a-fA-F\d\:]+)$")

        # Gen timer 00:49:49
        p13 = re.compile(r"^Gen +timer +(?P<generation_timer>\S+)$")

        # OSPF3 Link-Local database, interface ge-0/0/0.0 Area 0.0.0.8
        p14 = re.compile(
            r"^OSPF3 +Link-Local +database, +interface +(?P<ospf_intf>\S+) +"
            r"Area +(?P<ospf_area>\S+)$")

        # Type PointToPoint (1), Metric 5
        p15 = re.compile(
            r"^Type +(?P<link_type_name>\S+) +\((?P<link_type_value>\S+)\), +"
            r"Metric +(?P<link_metric>\S+)$")

        # Loc-If-Id 2, Nbr-If-Id 2, Nbr-Rtr-Id 10.189.5.253
        p16 = re.compile(
            r"^Loc-If-Id +(?P<link_intf_id>\S+), +Nbr-If-Id +(?P<nbr_intf_id>\S+)"
            r", +Nbr-Rtr-Id +(?P<nbr_rtr_id>\S+)$")

        # Options 0x33, Priority 128
        p17 = re.compile(
            r"^Options +(?P<ospf3_options>\S+), +Priority +(?P<router_priority>\S+)$"
        )

        #   Prefix-options 0x0, Metric 50, Type 1,
        p18 = re.compile(
            r"^Prefix-options +(?P<ospf3_prefix_options>\S+), +Metric +(?P<metric>\S+)"
            r", +Type +(?P<type_value>\S+),$")

        # Last changed 29w5d 21:40:56 ago, Change count: 1, Ours
        p19 = re.compile(
            r"^Last +changed +(?P<lsa_changed_time>(\S+ ){0,1}[\d\:]+) +ago, +"
            r"Change +count: +(?P<lsa_change_count>\d+), +(?P<database_entry_state>\S+)$"
        )

        # Installed 00:41:50 ago, expires in 00:18:10
        p20 = re.compile(
            r"^Installed +(?P<installation_time>(\S+ ){0,1}[\d\:]+) +ago, +expires +"
            r"in +(?P<expiration_time>(\S+ ){0,1}[\d\:]+)$")

        # Prefix 2001:db8:eb18:6337::/64 Prefix-options 0x0
        p21 = re.compile(
            r"^Prefix +(?P<ospf3_prefix>\S+) +Prefix-options +(?P<ospf3_prefix_options>\S+)$"
        )

        for line in out.splitlines():
            line = line.strip()

            #    OSPF3 database, Area 0.0.0.8
            m = p1.match(line)
            if m:

                ospf_area = (ret_dict.setdefault(
                    "ospf3-database-information",
                    {}).setdefault("ospf3-area-header",
                                   {}).setdefault("ospf-area", None))

                group = m.groupdict()

                ret_dict["ospf3-database-information"]["ospf3-area-header"][
                    "ospf-area"] = group["ospf_area"]
                continue

            # Router      0.0.0.0          10.34.2.250     0x800018ed  2504  0xaf2d  56
            m = p2.match(line)
            if m:
                entry_list = ret_dict.setdefault("ospf3-database-information",
                                                 {}).setdefault(
                                                     "ospf3-database", [])

                group = m.groupdict()
                entry = {}
                for group_key, group_value in group.items():
                    entry_key = group_key.replace("_", "-")
                    entry[entry_key] = group_value

                if entry["lsa-id"][0] == "*":
                    entry["lsa-id"] = entry["lsa-id"][1:]
                    entry["our-entry"] = True

                self.state = group["lsa_type"]

                entry_list.append(entry)
                continue

            # bits 0x2, Options 0x33
            m = p3.match(line)
            if m:
                last_database = ret_dict["ospf3-database-information"][
                    "ospf3-database"][-1]

                entry = last_database.setdefault("ospf3-router-lsa", {})

                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace("_", "-")
                    entry[entry_key] = group_value

                continue

            #  Type: PointToPoint, Node ID: 10.169.14.240, Metric: 100, Bidirectional
            m = p4.match(line)
            if m:
                last_database = ret_dict["ospf3-database-information"][
                    "ospf3-database"][-1]

                topology = last_database.setdefault("ospf3-router-lsa",
                                                    {}).setdefault(
                                                        "ospf3-lsa-topology",
                                                        {})
                topology["ospf-topology-id"] = "0"
                topology["ospf-topology-name"] = "default"

                link_list = topology.setdefault("ospf3-lsa-topology-link", [])

                group = m.groupdict()
                entry = {}
                for group_key, group_value in group.items():
                    entry_key = group_key.replace("_", "-")
                    entry[entry_key] = group_value

                link_list.append(entry)
                continue

            # Aging timer 00:18:16
            m = p5.match(line)
            if m:
                last_database = ret_dict["ospf3-database-information"][
                    "ospf3-database"][-1]
                last_database.setdefault("ospf-database-extensive",
                                         {}).setdefault("aging-timer", {})

                group = m.groupdict()
                last_database["ospf-database-extensive"]["aging-timer"][
                    "#text"] = group["aging_timer"]

                continue

            # Installed 00:10:20 ago, expires in 00:49:31, sent 00:10:18 ago
            m = p6.match(line)
            if m:
                last_entry = ret_dict["ospf3-database-information"][
                    "ospf3-database"][-1]

                last_entry.setdefault("ospf-database-extensive",
                                      {}).setdefault("expiration-time", {})
                last_entry.setdefault("ospf-database-extensive",
                                      {}).setdefault("installation-time", {})
                last_entry.setdefault("ospf-database-extensive",
                                      {}).setdefault("send-time", {})

                group = m.groupdict()
                last_entry["ospf-database-extensive"]["expiration-time"][
                    "#text"] = group["expiration_time"]
                last_entry["ospf-database-extensive"]["installation-time"][
                    "#text"] = group["installation_time"]
                last_entry["ospf-database-extensive"]["send-time"][
                    "#text"] = group["send_time"]

                continue

            # Last changed 2w6d 04:50:31 ago, Change count: 196
            m = p7.match(line)  # lsa_changed_time , lsa_changed_count
            if m:
                last_entry = ret_dict["ospf3-database-information"][
                    "ospf3-database"][-1]

                last_entry.setdefault("ospf-database-extensive",
                                      {}).setdefault("lsa-changed-time", {})

                group = m.groupdict()
                last_entry["ospf-database-extensive"]["lsa-changed-time"]["#text"]\
                     = group["lsa_changed_time"]
                last_entry["ospf-database-extensive"][
                    "lsa-change-count"] = group["lsa_change_count"]

                continue

            # Ref-lsa-type Router, Ref-lsa-id 0.0.0.0, Ref-router-id 10.34.2.250
            m = p8.match(line)
            if m:
                last_entry = ret_dict["ospf3-database-information"][
                    "ospf3-database"][-1]

                if self.state == "IntraArPfx":
                    entry = last_entry.setdefault("ospf3-intra-area-prefix-lsa", {})
                elif self.state == "InterArPfx":
                    entry = last_entry.setdefault("ospf3-inter-area-prefix-lsa", {})

                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace("_", "-")
                    entry[entry_key] = group_value

                continue

            # Prefix-count 3
            m = p9.match(line)
            if m:
                last_entry = ret_dict["ospf3-database-information"][
                    "ospf3-database"][-1]

                if self.state == "IntraArPfx":
                    entry = last_entry.setdefault("ospf3-intra-area-prefix-lsa", {})
                elif self.state == "InterArPfx":
                    entry = last_entry.setdefault("ospf3-inter-area-prefix-lsa", {})
                elif self.state == "Link":
                    entry = last_entry.setdefault("ospf3-link-lsa", {})

                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace("_", "-")
                    entry[entry_key] = group_value

                continue

            # Prefix 2001:db8:b0f8:3ab::/64
            m = p10.match(line)
            if m:
                last_database = ret_dict["ospf3-database-information"][
                    "ospf3-database"][-1]

                group = m.groupdict()

                if self.state == "IntraArPfx":
                    entry_list = last_database.setdefault(
                        "ospf3-intra-area-prefix-lsa",
                        {}).setdefault("ospf3-prefix", [])
                    entry_list.append(group["ospf3_prefix"])
                
                elif self.state == "InterArPfx":
                    entry_list = last_database.setdefault(
                        "ospf3-inter-area-prefix-lsa", {}
                    ).setdefault("ospf3-prefix", [])
                    entry_list.append(group["ospf3_prefix"])

                elif self.state == "Extern":

                    entry = last_database.setdefault("ospf3-external-lsa", {})
                    entry["ospf3-prefix"] = group["ospf3_prefix"]

                else:
                    raise "state error"

                continue

            # Prefix-options 0x0, Metric 5
            m = p11.match(line)
            if m:
                last_database = ret_dict["ospf3-database-information"][
                    "ospf3-database"][-1]

                group = m.groupdict()

                if self.state == "IntraArPfx":
                    entry = last_database.setdefault("ospf3-intra-area-prefix-lsa", {})
                elif self.state == "InterArPfx":
                    entry = last_database.setdefault("ospf3-inter-area-prefix-lsa", {})
                entry.setdefault("ospf3-prefix-options", []).append(
                    group["ospf3_prefix_options"]
                )
                entry.setdefault("ospf3-prefix-metric", []).append(group["metric"])

                continue

            # fe80::250:56ff:fe8d:a96c
            m = p12.match(line)
            if m:
                last_database = ret_dict["ospf3-database-information"][
                    "ospf3-database"][-1]

                entry = last_database.setdefault("ospf3-link-lsa", {})

                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace("_", "-")
                    entry[entry_key] = group_value

                continue

            # Gen timer 00:49:49
            m = p13.match(line)
            if m:
                last_database = ret_dict["ospf3-database-information"][
                    "ospf3-database"][-1]

                last_database.setdefault("ospf-database-extensive", {})\
                    .setdefault("generation-timer", {})

                group = m.groupdict()
                last_database["ospf-database-extensive"]["generation-timer"][
                    "#text"] = group["generation_timer"]

                continue

            # OSPF3 Link-Local database, interface ge-0/0/0.0 Area 0.0.0.8
            m = p14.match(line)
            if m:
                header_list = ret_dict.setdefault("ospf3-database-information",
                                                  {}).setdefault(
                                                      "ospf3-intf-header", [])

                group = m.groupdict()
                entry = {}
                for group_key, group_value in group.items():
                    entry_key = group_key.replace("_", "-")
                    entry[entry_key] = group_value

                header_list.append(entry)

                continue

            # Type PointToPoint (1), Metric 5
            m = p15.match(line)
            if m:
                last_database = ret_dict["ospf3-database-information"][
                    "ospf3-database"][-1]

                ospf3_link_list = last_database.setdefault(
                    "ospf3-router-lsa", {}).setdefault("ospf3-link", [])

                group = m.groupdict()
                entry = {}
                for group_key, group_value in group.items():
                    entry_key = group_key.replace("_", "-")
                    entry[entry_key] = group_value

                ospf3_link_list.append(entry)

                continue

            # Loc-If-Id 2, Nbr-If-Id 2, Nbr-Rtr-Id 10.189.5.253
            m = p16.match(line)
            if m:
                last_database = ret_dict["ospf3-database-information"][
                    "ospf3-database"][-1]

                last_ospf3_link = last_database["ospf3-router-lsa"][
                    "ospf3-link"][-1]

                group = m.groupdict()
                entry = last_ospf3_link
                for group_key, group_value in group.items():
                    entry_key = group_key.replace("_", "-")
                    entry[entry_key] = group_value

                continue

            # Options 0x33, Priority 128
            m = p17.match(line)  # ospf3-options
            if m:
                last_database = ret_dict["ospf3-database-information"][
                    "ospf3-database"][-1]

                group = m.groupdict()
                entry = last_database["ospf3-link-lsa"]
                for group_key, group_value in group.items():
                    entry_key = group_key.replace("_", "-")
                    entry[entry_key] = group_value

                continue

            #   Prefix-options 0x0, Metric 50, Type 1,
            m = p18.match(line)
            if m:
                last_database = ret_dict["ospf3-database-information"][
                    "ospf3-database"][-1]
                group = m.groupdict()
                entry = last_database.setdefault("ospf3-external-lsa", {})
                for group_key, group_value in group.items():
                    entry_key = group_key.replace("_", "-")
                    entry[entry_key] = group_value

                continue

            # Last changed 29w5d 21:40:56 ago, Change count: 1, Ours
            m = p19.match(line)  # lsa_changed_time , lsa_changed_count
            if m:
                last_entry = ret_dict["ospf3-database-information"][
                    "ospf3-database"][-1]

                last_entry.setdefault("ospf-database-extensive",
                                      {}).setdefault("lsa-changed-time", {})

                group = m.groupdict()  # database_entry_state
                last_entry["ospf-database-extensive"]["lsa-changed-time"][
                    "#text"] = group["lsa_changed_time"]
                last_entry["ospf-database-extensive"][
                    "lsa-change-count"] = group["lsa_change_count"]
                last_entry["ospf-database-extensive"][
                    "database-entry-state"] = group["database_entry_state"]

                continue

            # Installed 00:41:50 ago, expires in 00:18:10
            m = p20.match(line)
            if m:
                last_entry = ret_dict["ospf3-database-information"][
                    "ospf3-database"][-1]

                last_entry.setdefault("ospf-database-extensive",
                                      {}).setdefault("expiration-time", {})
                last_entry.setdefault("ospf-database-extensive",
                                      {}).setdefault("installation-time", {})

                group = m.groupdict()
                last_entry["ospf-database-extensive"]["expiration-time"][
                    "#text"] = group["expiration_time"]
                last_entry["ospf-database-extensive"]["installation-time"][
                    "#text"] = group["installation_time"]

                continue

            # Prefix 2001:db8:eb18:6337::/64 Prefix-options 0x0
            m = p21.match(line)
            if m:
                last_entry = ret_dict["ospf3-database-information"][
                    "ospf3-database"][-1]

                entry = last_entry.setdefault("ospf3-link-lsa", {})

                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace("_", "-")
                    entry[entry_key] = group_value
                continue

        return ret_dict


class ShowOspf3DatabaseNetworkDetailSchema(MetaParser):
    """ Schema for:
            * show ospf3 database network detail
    """
    """ schema = {
    Optional("@xmlns:junos"): str,
    "ospf3-database-information": {
        Optional("@xmlns"): str,
        "ospf3-area-header": {
            "ospf-area": str
        },
        "ospf3-database": [
            {
                Optional("@heading"): str,
                "advertising-router": str,
                "age": str,
                "checksum": str,
                "lsa-id": str,
                "lsa-length": str,
                "lsa-type": str,
                "ospf3-network-lsa": {
                    "attached-router": "list",
                    "ospf3-lsa-topology": {
                        "ospf-topology-id": str,
                        "ospf-topology-name": str,
                        "ospf3-lsa-topology-link": [
                            {
                                "link-type-name": str,
                                "ospf-lsa-topology-link-metric": str,
                                "ospf-lsa-topology-link-node-id": str,
                                "ospf-lsa-topology-link-state": str
                            }
                        ]
                    },
                    "ospf3-options": str
                },
                "our-entry": str,
                "sequence-number": str
                }
            ]
        }
    } """

    schema = {
        Optional("@xmlns:junos"): str,
        "ospf3-database-information": {
            Optional("@xmlns"): str,
            "ospf3-area-header": {
                "ospf-area": str
            },
            "ospf3-database": ListOf({
                Optional("@heading"): str,
                "advertising-router": str,
                "age": str,
                "checksum": str,
                "lsa-id": str,
                "lsa-length": str,
                "lsa-type": str,
                "ospf3-network-lsa": {
                    "attached-router": list,
                    "ospf3-lsa-topology": {
                        Optional("ospf-topology-id"):
                        str,
                        Optional("ospf-topology-name"):
                        str,
                        "ospf3-lsa-topology-link": ListOf({
                            "link-type-name": str,
                            "ospf-lsa-topology-link-metric": str,
                            "ospf-lsa-topology-link-node-id": str,
                            "ospf-lsa-topology-link-state": str
                        })
                    },
                    "ospf3-options": str
                },
                Optional("our-entry"): bool,
                "sequence-number": str
            })
        }
    }


class ShowOspf3DatabaseNetworkDetail(ShowOspf3DatabaseNetworkDetailSchema):
    """ Parser for:
            * show ospf3 database network detail
    """
    cli_command = 'show ospf3 database network detail'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # OSPF3 database, Area 0.0.0.0
        p1 = re.compile(r'^OSPF3 +database, +Area +(?P<ospf_area>\S+)$')

        # Network    *0.0.0.9          192.168.219.235   0x8000001d   892  0xf99f  36
        # Network     0.0.0.3          192.168.219.236   0x80000b14  2142  0x1983  36
        p2 = re.compile(r'^(?P<lsa_type>\S+) *(?P<our_entry>\*)?'
                        r'(?P<lsa_id>[\d\.]+) +(?P<advertising_router>\S+) '
                        r'+(?P<sequence_number>\S+) +(?P<age>\S+) '
                        r'+(?P<checksum>\S+) +(?P<lsa_length>\S+)$')

        # Options 0x33
        p3 = re.compile(r'^Options +(?P<ospf3_options>\S+)$')

        # Attached router 192.168.219.235
        p4 = re.compile(r'^Attached router +(?P<attached_router>\S+)$')

        # Type: Transit, Node ID: 192.168.219.236, Metric: 0, Bidirectional
        p6 = re.compile(
            r'^Type: +(?P<link_type_name>\S+)+, '
            r'+Node +ID: +(?P<ospf_lsa_topology_link_node_id>\S+), '
            r'+Metric: +(?P<ospf_lsa_topology_link_metric>\d+), '
            r'+(?P<ospf_lsa_topology_link_state>\S+)$')

        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # OSPF3 database, Area 0.0.0.0
            m = p1.match(line)
            if m:
                ospf_database_information_entry = ret_dict.setdefault(
                    "ospf3-database-information", {})
                ospf3_database_list = ospf_database_information_entry.setdefault(
                    "ospf3-database", [])
                group = m.groupdict()
                entry_dict = {}
                entry_dict["ospf-area"] = group["ospf_area"]
                ospf_database_information_entry[
                    "ospf3-area-header"] = entry_dict
                continue

            # Network *10.69.197.1    192.168.219.235   0x80000026  1730  0x22 0x1b56  36
            # Network     0.0.0.3          192.168.219.236   0x80000b14  2142  0x1983  36
            m = p2.match(line)
            if m:
                ospf3_database_dict = {}
                attached_router_list = []
                ospf3_network_lsa = {}
                ospf3_lsa_topology = {}
                ospf3_lsa_topology_link = []
                ospf3_network_lsa["attached-router"] = attached_router_list
                ospf3_lsa_topology[
                    "ospf3-lsa-topology-link"] = ospf3_lsa_topology_link
                ospf3_network_lsa["ospf3-lsa-topology"] = ospf3_lsa_topology
                ospf3_database_dict["ospf3-network-lsa"] = ospf3_network_lsa
                ospf3_database_list.append(ospf3_database_dict)
                group = m.groupdict()
                for group_key, group_value in group.items():
                    if (group_key == "our_entry"):
                        if (group_value == '*'):
                            ospf3_database_dict['our-entry'] = True
                    else:
                        entry_key = group_key.replace('_', '-')
                        ospf3_database_dict[entry_key] = group_value
                continue

            # Options 0x33
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ospf3_network_lsa["ospf3-options"] = group["ospf3_options"]
                continue

            # attached router 192.168.219.235
            m = p4.match(line)
            if m:
                group = m.groupdict()
                attached_router_list.append(group["attached_router"])
                continue

            # Type: Transit, Node ID: 192.168.219.236, Metric: 0, Bidirectional
            m = p6.match(line)
            if m:
                group = m.groupdict()
                entry_dict = {}
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_', '-')
                    entry_dict[entry_key] = group_value
                ospf3_lsa_topology_link.append(entry_dict)
                continue

        return ret_dict


class ShowOspf3DatabaseLinkAdvertisingRouterSchema(MetaParser):
    """ Schema for:
            * show ospf3 database link advertising-router {ipaddress} detail
    """
    """ schema = {
        Optional("@xmlns:junos"): str,
        "ospf3-database-information": {
            Optional("@xmlns"): str,
            "ospf3-database": [
                {
                    Optional("@heading"): str,
                    "advertising-router": str,
                    "age": str,
                    "checksum": str,
                    "lsa-id": str,
                    "lsa-length": str,
                    "lsa-type": str,
                    "ospf3-link-lsa": {
                        "linklocal-address": str,
                        "ospf3-options": str,
                        "ospf3-prefix": str,
                        "ospf3-prefix-options": str,
                        "prefix-count": str,
                        "router-priority": str
                    },
                    "our-entry": str,
                    "sequence-number": str
                }
            ],
            "ospf3-intf-header": [
                {
                    "ospf-area": str,
                    "ospf-intf": str
                }
            ]
        }
    } """

    schema = {
        Optional("@xmlns:junos"): str,
        "ospf3-database-information": {
            Optional("@xmlns"): str,
            "ospf3-database": ListOf({
                Optional("@heading"): str,
                "advertising-router": str,
                "age": str,
                "checksum": str,
                "lsa-id": str,
                "lsa-length": str,
                "lsa-type": str,
                "ospf3-link-lsa": {
                    "linklocal-address": str,
                    "ospf3-options": str,
                    Optional("ospf3-prefix"): str,
                    Optional("ospf3-prefix-options"): str,
                    "prefix-count": str,
                    "router-priority": str
                },
                Optional("our-entry"): bool,
                "sequence-number": str
            }),
            "ospf3-intf-header": ListOf({
                "ospf-area": str,
                "ospf-intf": str
            })
        }
    }


class ShowOspf3DatabaseLinkAdvertisingRouter(
        ShowOspf3DatabaseLinkAdvertisingRouterSchema):
    """ Parser for:
            * show ospf3 database link advertising-router {ipaddress} detail
    """
    cli_command = 'show ospf3 database link advertising-router {ipaddress} detail'

    def cli(self, ipaddress=None, output=None):
        if not output:
            if ipaddress:
                cmd = self.cli_command.format(ipaddress=ipaddress)
            else:
                cmd = self.cli_command

            out = self.device.execute(cmd)
        else:
            out = output

        # Type       ID               Adv Rtr           Seq      Age  Opt  Cksum  Len
        p0 = re.compile(r'^(?P<heading>Type \s+ID[\s\S]+)$')

        # OSPF3 Link-Local database, interface ge-0/0/2.0 Area 0.0.0.0
        p1 = re.compile(r'^OSPF3 +Link-Local +database, +interface '
                        r'+(?P<ospf_intf>\S+) +Area +(?P<ospf_area>\S+)$')

        # Link       *0.0.0.9          192.168.219.235   0x80000b10  1379  0xd3b0  56
        p2 = re.compile(r'^(?P<lsa_type>\S+) *(?P<our_entry>\*)?'
                        r'(?P<lsa_id>[\d\.]+) +(?P<advertising_router>\S+) '
                        r'+(?P<sequence_number>\S+) +(?P<age>\S+) '
                        r'+(?P<checksum>\S+) +(?P<lsa_length>\S+)$')

        # fe80::20c:2900:3367:243d
        p3 = re.compile(r'^(?P<linklocal_address>fe80+[\s\S]+)$')

        # Options 0x33, Priority 20
        p4 = re.compile(
            r'^Options +(?P<ospf3_options>\S+), Priority +(?P<router_priority>\S+)$'
        )

        # Prefix-count 1
        p5 = re.compile(r'^Prefix-count +(?P<prefix_count>\S+)$')

        # Prefix 2001:db8:dae9:cf16::/64 Prefix-options 0x0
        p6 = re.compile(r'^Prefix +(?P<ospf3_prefix>\S+) '
                        r'+Prefix-options +(?P<ospf3_prefix_options>\S+)$')

        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()
            # Type       ID               Adv Rtr           Seq      Age  Opt  Cksum  Len
            m = p0.match(line)
            if m:
                ospf3_database_dict = {}
                group = m.groupdict()
                ospf3_database_dict["@heading"] = group["heading"]

            # OSPF3 Link-Local database, interface ge-0/0/2.0 Area 0.0.0.0
            m = p1.match(line)
            if m:
                ospf_database_information_entry = ret_dict.setdefault(
                    "ospf3-database-information", {})
                ospf3_database_list = ospf_database_information_entry.setdefault(
                    "ospf3-database", [])
                ospf3_intf_header = ospf_database_information_entry.setdefault(
                    "ospf3-intf-header", [])

                group = m.groupdict()
                entry_dict = {}
                entry_dict["ospf-area"] = group["ospf_area"]
                entry_dict["ospf-intf"] = group["ospf_intf"]
                ospf3_intf_header.append(entry_dict)
                continue

            # Link       *0.0.0.9          192.168.219.235   0x80000b10  1379  0xd3b0  56
            m = p2.match(line)
            if m:

                ospf3_link_lsa = {}
                group = m.groupdict()
                for group_key, group_value in group.items():

                    if (group_key == "our_entry"):
                        if (group_value == '*'):
                            ospf3_database_dict['our-entry'] = True
                    else:
                        entry_key = group_key.replace('_', '-')
                        ospf3_database_dict[entry_key] = group_value
                ospf3_database_list.append(ospf3_database_dict)
                continue

            # fe80::20c:2900:3367:243d
            m = p3.match(line)
            if m:
                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_', '-')
                    ospf3_link_lsa[entry_key] = group_value
                continue

            # Options 0x33, Priority 20
            m = p4.match(line)
            if m:
                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_', '-')
                    ospf3_link_lsa[entry_key] = group_value
                continue

            # Prefix-count 1
            m = p5.match(line)
            if m:
                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_', '-')
                    ospf3_link_lsa[entry_key] = group_value
                ospf3_database_dict["ospf3-link-lsa"] = ospf3_link_lsa
                continue

            # Prefix 2001:db8:dae9:cf16::/64 Prefix-options 0x0
            m = p6.match(line)
            if m:
                group = m.groupdict()
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_', '-')
                    ospf3_link_lsa[entry_key] = group_value
                continue

        return ret_dict


class ShowOspf3RouteNetworkExtensiveSchema(MetaParser):
    '''schema = {
    "ospf3-route-information": {
        "ospf-topology-route-table": {
            "ospf3-route": [
                "ospf3-route-entry": {
                    "address-prefix": str,
                    "interface-cost": str,
                    "next-hop-type": str,
                    "ospf-area": str,
                    "ospf-next-hop": {
                        "next-hop-name": {
                            "interface-name": str
                        }
                    },
                    "route-origin": str,
                    "route-path-type": str,
                    "route-priority": str,
                    "route-type": str
                    }
                ]
            }
        }
    }'''

    schema = {
    "ospf3-route-information": {
        "ospf-topology-route-table": {
            "ospf3-route": ListOf({
                "ospf3-route-entry": {
                    "address-prefix": str,
                    Optional("forward"): str,
                    "interface-cost": str,
                    "next-hop-type": str,
                    "ospf-area": str,
                    Optional("ospf-next-hop"): {
                        Optional("next-hop-address"): {
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
                })
            }
        }
    }

'''
Parser for:
    * show ospf3 route network extensive
'''


class ShowOspf3RouteNetworkExtensive(ShowOspf3RouteNetworkExtensiveSchema):
    cli_command = 'show ospf3 route network extensive'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        #2001::4/128                                  Intra Network    IP   0
        p1 = re.compile(r'^(?P<address_prefix>[\d\:\/]+) '
                        r'+(?P<route_path_type>\S+) +(?P<route_type>\S+) '
                        r'+(?P<next_hop_type>\S+) +(?P<interface_cost>\d+)$')

        #NH-interface lo0.0
        #NH-interface et-0/0/0.0, NH-addr fe80::96f7:adff:fe5a:4840
        p2 = re.compile(r'^NH-interface +(?P<interface_name>[\w\d\-\/\.]+)(, +NH-addr +(?P<interface_address>\S+))?$')

        #Area 0.0.0.0, Origin 10.64.4.4, Priority low
        #Area 0.0.0.0, Origin 10.36.3.3, Fwd NZ, Priority medium
        p3 = re.compile(r'^Area +(?P<ospf_area>\S+),+ Origin +(?P<route_origin>\S+),( +Fwd +(?P<forward>\S+),)? +Priority +(?P<route_priority>\S+)$')


        for line in out.splitlines():
            line = line.strip()

            #2001::4/128                                  Intra Network    IP   0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ospf3_topology_route_table = ret_dict.setdefault(
                    'ospf3-route-information', {}).setdefault('ospf-topology-route-table', {}).\
                    setdefault('ospf3-route', [])

                    
                
                route_entry_dict = {}

                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_', '-')
                    route_entry_dict[entry_key] = group_value

            #NH-interface lo0.0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                next_hop_dict = {'next-hop-name':{'interface-name':group['interface_name']}}
                if group['interface_address']:
                    next_hop_dict['next-hop-address'] = {'interface-address':group['interface_address']} 
                route_entry_dict['ospf-next-hop'] = next_hop_dict                
                continue

            #Area 0.0.0.0, Origin 10.64.4.4, Priority low
            m = p3.match(line)
            if m:
                group = m.groupdict()
                for group_key, group_value in group.items():
                    if group_value != None:
                        entry_key = group_key.replace('_', '-')
                        route_entry_dict[entry_key] = group_value

                ospf3_parent_route_dict = {}
                ospf3_parent_route_dict['ospf3-route-entry'] = route_entry_dict
                ospf3_topology_route_table.append(ospf3_parent_route_dict)
                continue

        return ret_dict

class ShowOspf3NeighborInstanceAllSchema(MetaParser):
    """schema = {
        "ospf3-neighbor-information-all": {
            "ospf3-instance-neighbor": {
                "ospf3-instance-name": str,
                "ospf3-realm-neighbor": {
                    "ospf3-realm-name": str
                    "ospf3-neighbor": [
                        {
                            "activity-timer": str,
                            "interface-name": str,
                            "neighbor-address": str,
                            "neighbor-id": str,
                            "neighbor-priority": str,
                            "ospf-neighbor-state": str
                        }
                    ]
                }
            }
        }
    }"""

    # Main Schema
    schema = {
        "ospf3-neighbor-information-all": {
            "ospf3-instance-neighbor": {
                "ospf3-instance-name": str,
                "ospf3-realm-neighbor": {
                    "ospf3-realm-name": str,
                    Optional("ospf3-neighbor"): ListOf({
                        "activity-timer": str,
                        "interface-name": str,
                        "neighbor-address": str,
                        "neighbor-id": str,
                        "neighbor-priority": str,
                        "ospf-neighbor-state": str
                    })
                }
            }
        }
    }


# ==============================================
# Parser for 'show ospf3 neighbor instance all'
# ==============================================
class ShowOspf3NeighborInstanceAll(ShowOspf3NeighborInstanceAllSchema):
    """ Parser for:
            * show ospf3 neighbor instance all
    """

    cli_command = ['show ospf3 neighbor instance all']

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command[0])
        else:
            out = output

        ret_dict = {}

        # Instance: master
        p0 = re.compile(r'^Instance: +(?P<instance_name>\S+)$')

        # Realm: ipv6-unicast
        p1 = re.compile(r'^Realm: +(?P<realm_name>\S+)$')

        #10.189.5.253     ge-0/0/0.0             Full      128     35
        p2 = re.compile(r'^(?P<id>[\d\.]+) +(?P<interface>\S+) '
                        r'+(?P<state>\S+) +(?P<pri>\S+) +(?P<dead>\d+)$')

        #Neighbor-address fe80::250:56ff:fe8d:53c0
        p3 = re.compile(r'^Neighbor-address +(?P<neighbor_address>\S+)$')

        for line in out.splitlines():
            line = line.strip()

            # Instance: master
            m = p0.match(line)
            if m:
                group = m.groupdict()
                instance = group['instance_name']
                ospf3_instance_neighbor = ret_dict.setdefault('ospf3-neighbor-information-all', {}).setdefault(
                    'ospf3-instance-neighbor', {})
                ospf3_instance_neighbor['ospf3-instance-name'] = instance
                continue
            # Realm: ipv6-unicast
            m = p1.match(line)
            if m:
                group = m.groupdict()
                realm_name = group['realm_name']
                ospf3_realm_neighbor = ospf3_instance_neighbor.setdefault("ospf3-realm-neighbor", {})
                ospf3_realm_neighbor["ospf3-realm-name"] = realm_name
                continue
            #10.189.5.253     ge-0/0/0.0             Full      128     35
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ospf3_entry_list = ospf3_realm_neighbor.setdefault('ospf3-neighbor', [])
                ospf3_entry_dict = {}
                ospf3_entry_dict['activity-timer'] = group['dead']
                ospf3_entry_dict['interface-name'] = group['interface']
                ospf3_entry_dict['neighbor-id'] = group['id']
                ospf3_entry_dict['neighbor-priority'] = group['pri']
                ospf3_entry_dict['ospf-neighbor-state'] = group['state']
                continue

            #Neighbor-address fe80::250:56ff:fe8d:53c0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                neighbor_address = group['neighbor_address']
                ospf3_entry_dict['neighbor-address'] = neighbor_address
                ospf3_entry_list.append(ospf3_entry_dict)
                continue

        return ret_dict

class ShowOspf3RouteRouteSchema(MetaParser):

    # schema = {
    #   "ospf3-route-information": {
    #         "ospf-topology-route-table": {
    #             "ospf3-route": {
    #                 "ospf3-route-entry": {
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
    #                     }
    #                 }
    #             }
    #         }
    #     }

    schema = {
      "ospf3-route-information": {
            "ospf-topology-route-table": {
                "ospf3-route": {
                    "ospf3-route-entry": {
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
                    }
                }
            }
        }

'''
Parser for:
    * show ospf3 route {route}
'''


class ShowOspf3RoutePrefix(ShowOspf3RouteRouteSchema):
    cli_command = 'show ospf3 route {prefix}'

    def cli(self ,prefix, output=None):
        if not output:
            out = self.device.execute(self.cli_command.format(
                prefix=prefix
            ))
        else:
            out = output

        ret_dict = {}

        #2001:30::/64                                 Intra Network    IP   2
        p1 = re.compile(r'^(?P<address_prefix>[\d\:\/]+) '
                        r'+(?P<route_path_type>\S+) +(?P<route_type>\S+) '
                        r'+(?P<next_hop_type>\S+) +(?P<interface_cost>\d+)$')

        #NH-interface ge-0/0/4.0, NH-addr fe80::250:56ff:fe8d:351d
        p2 = re.compile(r'^NH-interface +(?P<interface_name>[\w\d\-\/\.]+)(, +NH-addr +(?P<interface_address>\S+))?$')

        for line in out.splitlines():
            line = line.strip()

            #2001:30::/64                                 Intra Network    IP   2
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ospf3_topology_route_table = ret_dict.setdefault(
                    'ospf3-route-information', {}).setdefault('ospf-topology-route-table', {})

                route_entry_dict = {}

                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_', '-')
                    route_entry_dict[entry_key] = group_value

            #NH-interface ge-0/0/4.0, NH-addr fe80::250:56ff:fe8d:351d
            m = p2.match(line)
            if m:
                group = m.groupdict()
                next_hop_dict = {'next-hop-name':{'interface-name':group['interface_name']}}
                if group['interface_address']:
                    next_hop_dict['next-hop-address'] = {'interface-address':group['interface_address']} 
                route_entry_dict.setdefault('ospf-next-hop', []).append(next_hop_dict)
                ospf3_parent_route_dict = {}
                ospf3_parent_route_dict['ospf3-route-entry'] = route_entry_dict
                ospf3_topology_route_table['ospf3-route'] = ospf3_parent_route_dict   
                continue

        return ret_dict