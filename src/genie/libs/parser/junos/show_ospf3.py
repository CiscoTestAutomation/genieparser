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
            "ospf-router-id": str,
            "ospf-tilfa-overview": {
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

    cli_command = [
        'show ospf3 overview'
    ]

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command[0])
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
        p5 = re.compile(r'^LSA refresh time: +(?P<ospf_lsa_refresh_time>\d+) minutes$')

        #Post Convergence Backup: Disabled
        p6 = re.compile(r'^Post Convergence Backup: +(?P<ospf_tilfa_enabled>\S+)$')

        #Area: 0.0.0.8
        p7 = re.compile(r'^Area: +(?P<ospf_area>[\w\.\:\/]+)$')

        #Stub type: Not Stub
        p8 = re.compile(r'^Stub type: +(?P<ospf_stub_type>\w+ \w+)$')

        #Area border routers: 0, AS boundary routers: 5
        p9 = re.compile(r'^Area border routers: +(?P<ospf_abr_count>\d+), AS boundary routers: +(?P<ospf_asbr_count>\d+)$')

        
        #Up (in full state): 2
        p10 = re.compile(r'^Up \(in full state\): +(?P<ospf_nbr_up_count>\d+)$')

        #Topology: default (ID 0)
        p11 = re.compile(r'^Topology: +(?P<ospf_topology_name>\S+) \(ID +(?P<ospf_topology_id>\d+)\)$')

        #Prefix export count: 1
        p12 = re.compile(r'^Prefix export count: +(?P<ospf_prefix_export_count>\d+)$')

        #Full SPF runs: 1934
        p13 = re.compile(r'^Full SPF runs: +(?P<ospf_full_spf_count>\d+)$')

        #SPF delay: 0.200000 sec, SPF holddown: 2 sec, SPF rapid runs: 3
        p14 = re.compile(r'^SPF delay: +(?P<ospf_spf_delay>[\w\.\:\/]+) sec, SPF holddown: +(?P<ospf_spf_holddown>[\w\.]+) sec, SPF rapid runs: +(?P<ospf_spf_rapid_runs>[\w\.]+)$')

        #Backup SPF: Not Needed
        p15 = re.compile(r'^Backup SPF: +(?P<ospf_backup_spf_status>\w+ \w+)$')


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
            
            #Router ID: 111.87.5.252
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ospf3_entry_list['ospf-router-id'] = group['ospf_router_id']
                continue

            #Route table index: 0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ospf3_entry_list['ospf-route-table-index'] = group['ospf_route_table_index']
                continue

            #LSA refresh time: 50 minute
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ospf3_entry_list['ospf-lsa-refresh-time'] = group['ospf_lsa_refresh_time']
                continue

            #Post Convergence Backup: Disabled
            m = p6.match(line)
            if m:
                group = m.groupdict()
                ospf3_entry_list['ospf-tilfa-overview'] = {'ospf-tilfa-enabled': group['ospf_tilfa_enabled']}
                continue

            #Area: 0.0.0.8
            m = p7.match(line)
            if m:
                group = m.groupdict()
                ospf3_area_entry_dict = ospf3_entry_list.setdefault('ospf-area-overview', {})
                ospf3_area_entry_dict.update({'ospf-area': group['ospf_area']})
                continue

            #Stub type: Not Stub
            m = p8.match(line)
            if m:
                group = m.groupdict()
                ospf3_area_entry_dict.update({'ospf-stub-type': group['ospf_stub_type']})
                continue

            #Area border routers: 0, AS boundary routers: 5
            m = p9.match(line)
            if m:
                group = m.groupdict()
                ospf3_area_entry_dict.update({'ospf-abr-count': group['ospf_abr_count']})
                ospf3_area_entry_dict.update({'ospf-asbr-count': group['ospf_asbr_count']})
                continue

            #Up (in full state): 2
            m = p10.match(line)
            if m:
                group = m.groupdict()
                ospf3_area_entry_dict.setdefault('ospf-nbr-overview', {"ospf-nbr-up-count":group['ospf_nbr_up_count']})
                continue

            #Topology: default (ID 0)
            m = p11.match(line)
            if m:
                group = m.groupdict()
                ospf3_topology_entry_dict = ospf3_entry_list.setdefault('ospf-topology-overview', {})
                ospf3_topology_entry_dict.update({'ospf-topology-name': group['ospf_topology_name']})
                ospf3_topology_entry_dict.update({'ospf-topology-id': group['ospf_topology_id']})
                continue

            #Prefix export count: 1
            m = p12.match(line)
            if m:
                group = m.groupdict()
                ospf3_topology_entry_dict.update({'ospf-prefix-export-count': group['ospf_prefix_export_count']})
                continue

            #Full SPF runs: 1934
            m = p13.match(line)
            if m:
                group = m.groupdict()
                ospf3_topology_entry_dict.update({'ospf-full-spf-count': group['ospf_full_spf_count']})
                continue

            #SPF delay: 0.200000 sec, SPF holddown: 2 sec, SPF rapid runs: 3
            m = p14.match(line)
            if m:
                group = m.groupdict()
                ospf3_topology_entry_dict.update({'ospf-spf-delay': group['ospf_spf_delay']})
                ospf3_topology_entry_dict.update({'ospf-spf-holddown': group['ospf_spf_holddown']})
                ospf3_topology_entry_dict.update({'ospf-spf-rapid-runs': group['ospf_spf_rapid_runs']})
                continue

            #Backup SPF: Not Needed
            m = p15.match(line)
            if m:
                group = m.groupdict()
                ospf3_topology_entry_dict.update({'ospf-backup-spf-status': group['ospf_backup_spf_status']})
                continue
        
        return ret_dict

class ShowOspf3OverviewExtensive(ShowOspf3Overview):
    """ Parser for:
            - show ospf3 overview extensive
    """

    cli_command = [
        'show ospf3 overview extensive'
    ]

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command[0])
        else:
            out = output

        return super().cli(output=out)