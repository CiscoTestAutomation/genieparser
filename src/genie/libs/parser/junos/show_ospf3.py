
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
        p1 = re.compile(r'^(?P<interface_name>\S+) +(?P<ospf_interface_state>\S+) +(?P<ospf_area>[0-9]{1,3}(\.[0-9]{1,3}){3})'
            r' +(?P<dr_id>[0-9]{1,3}(\.[0-9]{1,3}){3}) +(?P<bdr_id>[0-9]{1,3}(\.[0-9]{1,3}){3}) +(?P<neighbor_count>\S+)$')

        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # ge-0/0/0.0          PtToPt  0.0.0.8         0.0.0.0         0.0.0.0            1
            m = p1.match(line)
            if m:

                entry_list = ret_dict.setdefault("ospf3-interface-information", {}).setdefault("ospf3-interface", [])

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
                    "sequence-number": str
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
                "sequence-number": str
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
        p1 = re.compile(r'^( *)OSPF3( +)database,( +)Area( +)(?P<ospf_area>(\*{0,1})[0-9]{1,3}(\.[0-9]{1,3}){3})$')

        # Type       ID               Adv Rtr           Seq         Age  Cksum  Len
        # Router      0.0.0.0          10.34.2.250     0x800018ed  2407  0xaf2d  56
        p2 = re.compile(r'^( *)(?P<lsa_type>\S+) +(\*{0,1})(?P<lsa_id>[0-9]{1,3}(\.[0-9]{1,3}){3}) +(?P<advertising_router>[0-9]{1,3}(\.[0-9]{1,3}){3}) +(?P<sequence_number>\S+) +(?P<age>\d+) +(?P<checksum>\S+) +(?P<lsa_length>\d+)$')

        # OSPF3 Link-Local database, interface ge-0/0/0.0 Area 0.0.0.8
        p3 = re.compile(r'^( *)OSPF3( +)Link-Local( +)database,( +)interface( +)(?P<ospf_intf>\S+)( +)Area( +)(?P<ospf_area>[0-9]{1,3}(\.[0-9]{1,3}){3})$')

        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # ge-0/0/0.0          PtToPt  0.0.0.8         0.0.0.0         0.0.0.0            1
            m = p1.match(line)
            if m:
                ospf_area = ret_dict.setdefault("ospf3-database-information", {}).setdefault("ospf3-area-header", {}).setdefault("ospf-area", None)
                if ospf_area:
                    raise Exception("ospf-area already exists"+str(ospf_area))

                group = m.groupdict()

                ret_dict["ospf3-database-information"]["ospf3-area-header"]["ospf-area"] = group["ospf_area"]
                continue

            # Router      0.0.0.0          10.34.2.250     0x800018ed  2407  0xaf2d  56
            m = p2.match(line)
            if m:
                entry_list = ret_dict.setdefault("ospf3-database-information", {}).setdefault("ospf3-database", [])

                group = m.groupdict()
                entry = {}
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value

                entry_list.append(entry)
                continue

            # OSPF3 Link-Local database, interface ge-0/0/0.0 Area 0.0.0.8
            m = p3.match(line)
            if m:
                entry_list = ret_dict.setdefault("ospf3-database-information", {}).setdefault("ospf3-intf-header", [])

                group = m.groupdict()
                entry = {}
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value

                entry_list.append(entry)
                continue

        return ret_dict