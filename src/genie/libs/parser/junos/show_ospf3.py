
''' show_ospf3.py

Parser for the following show commands:
    * show ospf3 interface
    * show ospf3 database
    * show ospf3 interface extensive
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

    def validate_ospf3_neighbor_extensive_list(value):
            # Pass osp3_neighbor_extensive-entry list of dict in value
        if not isinstance(value, list):
            raise SchemaTypeError('ospf3-table-entry is not a list')
        # Create Arp Entry Schema
        entry_schema = Schema({
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
            "neighbor-up-time": {
                "#text": str
            },
            "options": str,
            "ospf-area": str,
            "ospf-neighbor-state": str,
            "ospf3-interface-index": str
        })
        # Validate each dictionary in list
        for item in value:
            entry_schema.validate(item)
        return value

    # Main Schema
    schema = {
        "ospf3-neighbor-information": {
        "ospf3-neighbor": Use(validate_ospf3_neighbor_extensive_list)
        }
    }

# ==============================================
#  Schema for show ospf3 neighbor extensive
# ==============================================
class ShowOspf3NeighborExtensive(ShowOspf3NeighborExtensiveSchema):
    """ Parser for:
            * show ospf3 neighbor extensive
    """

    cli_command = [
        'show ospf3 neighbor extensive'
    ]

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command[0])
        else:
            out = output

        ret_dict = {}

        #10.189.5.253     ge-0/0/0.0             Full      128     35
        p1 = re.compile(r'^(?P<neighborid>[\w\.\:\/]+) +(?P<interfacename>\S+) '
                r'+(?P<ospfneighborstate>\S+) +(?P<pri>\S+) +(?P<dead>\d+)$')

        #Neighbor-address fe80::250:56ff:fe8d:53c0
        p2 = re.compile(r'^Neighbor-address +(?P<neighbor_address>\S+)$')

        #Area 0.0.0.8, opt 0x13, OSPF3-Intf-Index 2
        p3 = re.compile(r'^Area +(?P<area>\S+), opt +(?P<opt>\S+), OSPF3-Intf-Index +(?P<ospf3>\d+)$')

        #DR-ID 0.0.0.0, BDR-ID 0.0.0.0
        p4 = re.compile(r'^DR-ID +(?P<drid>\S+), BDR-ID +(?P<bdrid>\S+)$')

        #Up 3w0d 17:07:00, adjacent 3w0d 17:07:00
        p5 = re.compile(r'^Up +(?P<up>\S+ +[\d\:]+), adjacent +(?P<adjacent>\S+ +[\d\:]+)$')

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
                ospf3_entry_dict['ospf-neighbor-state'] = group['ospfneighborstate']
                ospf3_entry_dict['neighbor-priority'] = group['pri']

                continue

            #Neighbor-address fe80::250:56ff:fe8d:53c0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ospf3_entry_dict['neighbor-address'] = group['neighbor_address']
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
                ospf3_entry_dict['neighbor-adjacency-time'] = {'#text': group['adjacent']}
                ospf3_entry_dict['neighbor-up-time'] = {'#text': group['up']}
                ospf3_entry_list.append(ospf3_entry_dict)
                continue

        return ret_dict

# ==============================================
# Schema for 'show ospf3 neighbor | no more'
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

    def validate_ospf3_neighbor_list(value):
            # Pass osp3_neighbor_detail-entry list of dict in value
        if not isinstance(value, list):
            raise SchemaTypeError('ospf3-table-entry is not a list')
        # Create Arp Entry Schema
        entry_schema = Schema({
            "activity-timer": str,
            "interface-name": str,
            "neighbor-address": str,
            "neighbor-id": str,
            "neighbor-priority": str,
            "ospf-neighbor-state": str
        })
        # Validate each dictionary in list
        for item in value:
            entry_schema.validate(item)
        return value

    # Main Schema
    schema = {
        "ospf3-neighbor-information": {
        "ospf3-neighbor": Use(validate_ospf3_neighbor_list)
        }
    }

# ==============================================
# Parser for 'show ospf3 neighbor | no more'
# ==============================================
class ShowOspf3Neighbor(ShowOspf3NeighborSchema):
    """ Parser for:
            * show ospf3 neighbor | no more
    """

    cli_command = [
        'show ospf3 neighbor | no more'
    ]

    def cli(self, output=None):
        if not output:
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

class ShowOspf3NeighborDetail(ShowOspf3NeighborExtensive):
    """ Parser for:
            - show ospf3 neighbor detail
    """

    cli_command = [
        'show ospf3 neighbor detail'
    ]

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

    # Sub Schema ospf3-database
    def validate_ospf3_database_list(value):
        # Pass ospf3-database list as value
        if not isinstance(value, list):
            raise SchemaTypeError('ospf-interface is not a list')
        ospf3_database_schema = Schema({
                "advertising-router": str,
                "age": str,
                "checksum": str,
                "lsa-id": str,
                "lsa-length": str,
                "lsa-type": str,
                "sequence-number": str,
                Optional('our-entry'): bool
            })
        # Validate each dictionary in list
        for item in value:
            ospf3_database_schema.validate(item)
        return value

    # Sub Schema ospf3-intf-header
    def validate_ospf3_intf_header_list(value):
        # Pass ospf3-intf-header list as value
        if not isinstance(value, list):
            raise SchemaTypeError('ospf-interface is not a list')
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
                    entry['our-entry'] = True

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

class ShowOspf3InterfaceExtensiveSchema(MetaParser):
    """ Schema for:
            * show ospf3 interface extensive
    """

    # Sub Schema ospf3-interface
    def validate_ospf3_interface_list(value):
        # Pass ospf3-interface list as value
        if not isinstance(value, list):
            raise SchemaTypeError('ospf3-interface is not a list')
        ospf3_interface_schema = Schema({
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
            Optional("dr-address"): str
        })
        # Validate each dictionary in list
        for item in value:
            ospf3_interface_schema.validate(item)
        return value

    schema = {
        "ospf3-interface-information": {
            "ospf3-interface": Use(validate_ospf3_interface_list)
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
        p1 = re.compile(r'^(?P<interface_name>\S+)( +)(?P<ospf_interface_state>\S+)'
            r'( +)(?P<ospf_area>[\d\.]+)( +)(?P<dr_id>[\d\.]+)( +)'
            r'(?P<bdr_id>[\d\.]+)( +)(?P<neighbor_count>\d+)$')

        # Address fe80::250:56ff:fe8d:c829, Prefix-length 64
        p2 = re.compile(r'Address( +)(?P<interface_address>\S+),( +)Prefix-length'
            r'( +)(?P<prefix_length>\d+)')

        # OSPF3-Intf-index 2, Type P2P, MTU 1500, Cost 5
        p3 = re.compile(r'^OSPF3-Intf-index( +)(?P<ospf3_interface_index>\d+),( +)'
            r'Type( +)(?P<interface_type>\S+),( +)MTU( +)(?P<mtu>\d+),( +)Cost( +)'
            r'(?P<interface_cost>\d+)$')

        # Adj count: 1, Router LSA ID: 0
        p4 = re.compile(r'^Adj( +)count:( +)(?P<adj_count>\d+),( +)Router( +)LSA'
            r'( +)ID:( +)(?P<ospf3_router_lsa_id>\S+)$')

        # Hello 10, Dead 40, ReXmit 5, Not Stub
        p5 = re.compile(r'^Hello( +)(?P<hello_interval>\d+),( +)Dead( +)'
            r'(?P<dead_interval>\d+),( +)ReXmit( +)(?P<retransmit_interval>\d+),'
            r'( +)(?P<ospf_stub_type>(\S+ ){0,1}\S+)$')

        # Protection type: None
        p6 = re.compile(r'^Protection( +)type:( +)(?P<ospf_interface_protection_type>\S+)$')

        #   OSPF3-Intf-index 1, Type LAN, MTU 65535, Cost 0, Priority 128
        p7 = re.compile(r'^OSPF3-Intf-index( +)(?P<ospf3_interface_index>\d+),( +)'
            r'Type( +)(?P<interface_type>\S+),( +)MTU( +)(?P<mtu>\d+),( +)Cost( +)'
            r'(?P<interface_cost>\d+),( +)Priority( +)(?P<router_priority>\d+)$')

        # DR addr fe80::250:560f:fc8d:7c08
        p8 = re.compile(r'^DR( +)addr( +)(?P<dr_address>\S+)$')

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
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value

                interface_list.append(entry)
                continue

            # Address fe80::250:56ff:fe8d:c829, Prefix-length 64
            m = p2.match(line)
            if m:
                last_interface = ret_dict["ospf3-interface-information"]["ospf3-interface"][-1]

                group = m.groupdict()
                entry = last_interface
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value

                continue

            # OSPF3-Intf-index 2, Type P2P, MTU 1500, Cost 5
            m = p3.match(line)
            if m:
                last_interface = ret_dict["ospf3-interface-information"]["ospf3-interface"][-1]

                group = m.groupdict()
                entry = last_interface
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value

                continue

            # Adj count: 1, Router LSA ID: 0
            m = p4.match(line)
            if m:
                last_interface = ret_dict["ospf3-interface-information"]["ospf3-interface"][-1]

                group = m.groupdict()
                entry = last_interface
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value

                if entry['ospf3-router-lsa-id'] == '-':
                    del entry['ospf3-router-lsa-id']

                continue

            # Hello 10, Dead 40, ReXmit 5, Not Stub
            m = p5.match(line)
            if m:
                last_interface = ret_dict["ospf3-interface-information"]["ospf3-interface"][-1]

                group = m.groupdict()
                entry = last_interface
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value

                continue

            # Protection type: None
            m = p6.match(line)
            if m:
                last_interface = ret_dict["ospf3-interface-information"]["ospf3-interface"][-1]

                group = m.groupdict()
                entry = last_interface
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value

                continue

            #   OSPF3-Intf-index 1, Type LAN, MTU 65535, Cost 0, Priority 128
            m = p7.match(line)
            if m:
                last_interface = ret_dict["ospf3-interface-information"]["ospf3-interface"][-1]

                group = m.groupdict()
                entry = last_interface
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value

                continue

            # DR addr fe80::250:560f:fc8d:7c08
            m = p8.match(line)
            if m:
                last_interface = ret_dict["ospf3-interface-information"]["ospf3-interface"][-1]

                group = m.groupdict()
                entry = last_interface
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value

                continue

        return ret_dict

class ShowOspf3DatabaseExternalExtensiveSchema(MetaParser):
    """ Schema for:
            * show ospf3 database external extensive
    """

    # Sub Schema
    def validate_ospf3_database_list(value):
        # Pass ospf3-database list as value
        if not isinstance(value, list):
            raise SchemaTypeError('ospf-interface is not a list')
        ospf3_interface_schema = Schema({
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
        # Validate each dictionary in list
        for item in value:
            ospf3_interface_schema.validate(item)
        return value

    schema = {
    "ospf3-database-information": {
        "ospf3-database": Use(validate_ospf3_database_list)
    }
}

class ShowOspf3DatabaseExternalExtensive(ShowOspf3DatabaseExternalExtensiveSchema):
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

        # Extern      0.0.0.1          59.128.2.250     0x8000178e  1412  0x3c81  28
        p1 = re.compile(r'^(?P<lsa_type>\S+) +(?P<lsa_id>(\*{0,1})[\d\.]+) +'
            r'(?P<advertising_router>[\d\.]+) +(?P<sequence_number>\S+) +(?P<age>\d+)'
            r' +(?P<checksum>\S+) +(?P<lsa_length>\d+)$')

        # Prefix ::/0
        p2 = re.compile(r'^Prefix +(?P<ospf3_prefix>\S+)$')

        # Prefix-options 0x0, Metric 1, Type 1,
        p3 = re.compile(r'^Prefix-options +(?P<ospf3_prefix_options>\S+),'
            r' Metric +(?P<metric>\d+), +Type +(?P<type_value>\d+),$')

        # Aging timer 00:36:27
        p4 = re.compile(r'^Aging +timer +(?P<aging_timer>(\S+ ){0,1}[\d:]+)$')

        # Gen timer 00:49:49
        p5 = re.compile(r'^Gen +timer +(?P<generation_timer>\S+)$')

        # Installed 00:23:26 ago, expires in 00:36:28, sent 00:23:24 ago
        p6 = re.compile(r'^Installed +(?P<installation_time>(\S+ ){0,1}[\d:]+)'
            r' ago, +expires +in +(?P<expiration_time>(\S+ ){0,1}[\d:]+),'
            r' sent +(?P<send_time>(\S+ ){0,1}[\d:]+) +ago$')

        # Last changed 29w5d 21:04:29 ago, Change count: 1
        p7 =re.compile(r'^Last +changed +(?P<lsa_changed_time>(\S+ ){0,1}[\d:]+)'
            r' ago, +Change +count: +(?P<lsa_change_count>\d+)$')

        # Last changed 3w0d 17:02:47 ago, Change count: 2, Ours
        p8 = re.compile(r'^Last +changed +(?P<lsa_changed_time>(\S+ ){0,1}[\d:]+)'
            r' ago, +Change +count: +(?P<lsa_change_count>\d+), +(?P<database_entry_state>\S+)$')

        for line in out.splitlines():
            line = line.strip()

            # Extern      0.0.0.1          59.128.2.250     0x8000178e  1412  0x3c81  28
            m = p1.match(line)
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
                    entry['our-entry'] = True

                entry_list.append(entry)
                continue

            # Prefix ::/0
            m = p2.match(line)
            if m:
                last_database = ret_dict["ospf3-database-information"]["ospf3-database"][-1]

                group = m.groupdict()

                entry = last_database.setdefault("ospf3-external-lsa", {})
                entry['ospf3-prefix'] = group['ospf3_prefix']

                continue

            # Prefix-options 0x0, Metric 1, Type 1,
            m = p3.match(line)
            if m:
                last_database = ret_dict["ospf3-database-information"]["ospf3-database"][-1]

                group = m.groupdict()
                entry = last_database.setdefault("ospf3-external-lsa", {})
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value

                continue

            # Aging timer 00:36:27
            m = p4.match(line)
            if m:
                last_database = ret_dict["ospf3-database-information"]["ospf3-database"][-1]
                last_database.setdefault("ospf-database-extensive", {}).setdefault("aging-timer", {})

                group = m.groupdict()
                last_database["ospf-database-extensive"]["aging-timer"]["#text"] = group['aging_timer']

                continue

            # Gen timer 00:49:49
            m = p5.match(line)
            if m:
                last_database = ret_dict["ospf3-database-information"]["ospf3-database"][-1]

                last_database.setdefault("ospf-database-extensive", {})\
                    .setdefault("generation-timer", {})

                group = m.groupdict()
                last_database["ospf-database-extensive"]["generation-timer"]["#text"]\
                     = group['generation_timer']

                continue

            # Installed 00:23:26 ago, expires in 00:36:28, sent 00:23:24 ago
            m = p6.match(line)
            if m:
                last_database = ret_dict["ospf3-database-information"]["ospf3-database"][-1]

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
                last_database = ret_dict["ospf3-database-information"]["ospf3-database"][-1]

                last_database.setdefault("ospf-database-extensive", {}).setdefault("lsa-changed-time", {})

                group = m.groupdict()
                last_database["ospf-database-extensive"]["lsa-changed-time"]["#text"]\
                    = group['lsa_changed_time']
                last_database["ospf-database-extensive"]["lsa-change-count"]\
                    = group['lsa_change_count']

                continue

            # Last changed 29w5d 21:40:56 ago, Change count: 1, Ours
            m = p8.match(line)
            if m:
                last_database = ret_dict["ospf3-database-information"]["ospf3-database"][-1]

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