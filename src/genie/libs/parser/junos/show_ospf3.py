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

        # use the pattern r'[0-9]{1,3}(\.[0-9]{1,3}){3}' to pick up on ip addresses
        # in 'area', 'dr_id' and 'bdr_id'

        # ge-0/0/0.0          PtToPt  0.0.0.8         0.0.0.0         0.0.0.0            1
        p1 = re.compile(r'^(?P<interface>\S+) +(?P<state>\S+) +(?P<area>[0-9]{1,3}(\.[0-9]{1,3}){3})'
            r' +(?P<dr_id>[0-9]{1,3}(\.[0-9]{1,3}){3}) +(?P<bdr_id>[0-9]{1,3}(\.[0-9]{1,3}){3}) +(?P<nbrs>\S+)$')

        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # ge-0/0/0.0          PtToPt  0.0.0.8         0.0.0.0         0.0.0.0            1
            m = p1.match(line)
            if m:

                entry_list = ret_dict.setdefault("ospf3-interface-information", {}).setdefault("ospf3-interface", [])

                group = m.groupdict()

                interface_entry = {}
                interface_entry['interface-name'] = group['interface']
                interface_entry['ospf-interface-state'] = group['state']
                interface_entry['ospf-area'] = group['area']
                interface_entry['dr-id'] = group['dr_id']
                interface_entry['bdr-id'] = group['bdr_id']
                interface_entry['neighbor-count'] = group['nbrs']

                entry_list.append(interface_entry)
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