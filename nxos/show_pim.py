import re
from metaparser import MetaParser
from metaparser.util.schemaengine import Schema, Any, Optional

# ====================================================
# schema Parser for 'show ip pim interface vrf all'
# ====================================================
class ShowIpPimInterfaceVrfAllSchema(MetaParser):

    '''Schema for show ip pim interface vrf all'''

    schema = {
        'vrf':{
            Any():{
                'interfaces':{
                    Any():{
                        'address_family': {
                            Any(): {
                                Optional('interface_status'): str,
                                Optional('ip_address'): str,
                                Optional('ip_subnet'): str,
                                Optional('dr_address'): str,
                                Optional('dr_priority'): str,
                                Optional('neighbor_count'): str,
                                Optional('hello_interval'): str,
                                Optional('hello_expiration'): str,
                                Optional('neighbor_holdtime'): int,
                                Optional('dr_delay'): int,
                                Optional('border_interface'): bool,
                                Optional('genid'): str,
                                Optional('hello_md5_ah_authentication'): str,
                                Optional('neighbor_policy'): str,
                                Optional('jp_inbound_policy'): str,
                                Optional('jp_outbound_policy'): str,
                                Optional('jp_interval'): int,
                                Optional('jp_next_sending'): int,
                                Optional('bfd'):{
                                    Optional('enable'): bool,
                                    },
                                Optional('passive_interface'): bool,
                                Optional('vpc_svi'): bool,
                                Optional('auto_enabled'): bool,
                                Optional('statistics'):{
                                    Optional('general'):{
                                        Optional('hellos'): str,
                                        Optional('jps'): str,
                                        Optional('grafts'): str,
                                        Optional('grafts_acks'): str,
                                        Optional('df_offers'): str,
                                        Optional('df_winners'): str,
                                        Optional('df_backoffs'): str,
                                        Optional('df_passes'): str,
                                    },
                                    Optional('error'):{
                                        Optional('checksum'): int,
                                        Optional('invalid_packet_types'): int,
                                        Optional('invalid_df_subtypes'): int,
                                        Optional('authentication_failed'): int,
                                        Optional('packet_length'): int,
                                        Optional('bad_version_packets'): int,
                                        Optional('packets_from_self'): int,
                                        Optional('packets_from_non_neighbors'): int,
                                        Optional('packets_ received_on_passiveinterface'): int,
                                        Optional('jpPs_received_on_rpf_interface'): int,
                                        Optional('joins_received_with_no_rp'): int,
                                        Optional('joins_received_with_wrong_rp'): int,
                                        Optional('joins_received_with_ssm_groups'): int,
                                        Optional('joins_received_with_bidir_groups'): int,
                                        Optional('jps_filtered_by_inbound_policy'): int,
                                        Optional('jps_filtered_by_outbound_policy'): int,
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }

# ==========================================================
#  parser for show ip pim interface vrf all
#
# ==========================================================
class ShowIpPimInterfaceVrfAll(ShowIpPimInterfaceVrfAllSchema):
    '''Parser for show ip pim interface vrf all'''

    def cli(self):

        cmd = 'show ip pim interface vrf all'
        out = self.device.execute(cmd)
        af_name = 'ipv4'

        # Init dictionary
        parsed_dict = dict()

        for line in out.splitlines():
            line = line.rstrip()

            #PIM Interface Status for VRF "VRF1"
            p1 = re.compile(r'^\s*PIM +Interface +Status +for +VRF+ \"(?P<vrf>[\w]+)\"$')
            m = p1.match(line)
            if m:
                vrf = m.groupdict()['vrf']

            # Ethernet2/2, Interface status: protocol-up/link-up/admin-up
            p2 = re.compile(r'^\s*(?P<interface_name>[\w\/]+),'
                            ' +Interface +status: +(?P<interface_status>[\w\-\/]+)$')
            m = p2.match(line)
            if m:
                interface_name = m.groupdict()['interface_name']
                interface_status = m.groupdict()['interface_status']

        return parsed_dict
# ================================
# schema Parser for 'show ipv6 pim vrf all detail'
# ================================
class ShowIpv6PimVrfAllDetailSchema(MetaParser):

    '''Schema for show ipv6 pim vrf all detail'''

    schema = {
        'vrf':{
            Any():{
            'address_family':{
                Any():{
                   Optional('vrf_id'): int,
                   Optional('table_id'): str,
                   Optional('interface_count'): int,
                   Optional('bfd'):{
                       Optional('enable'): bool,
                   },
                   Optional('state_limit'): str,
                   Optional('register_rate_limit'): str,
                   Optional('shared_tree_route_map'): str,
                   Optional('shared_tree_route_ranges'): str,
                   Optional('shared_tree_ranges'): str,
                   },
                },
            },
        },
    }

# ==========================================================
#  parser for show ipv6 pim vrf all detail
#
# ==========================================================
class ShowIpv6PimVrfAllDetail(ShowIpv6PimVrfAllDetailSchema):
    '''Parser for show ipv6 pim vrf all detail'''

    def cli(self):

        cmd = 'show ipv6 pim vrf all detail'
        out = self.device.execute(cmd)
        af_name = 'ipv6'
        # Init dictionary
        parsed_dict = dict()

        for line in out.splitlines():
            line = line.rstrip()

            #VRF Name              VRF      Table       Interface  BFD
            #          ID       ID          Count      Enabled
            # default               1        0x80000001  3          no
            p1 = re.compile(r'^\s*(?P<vrf>[\w\d]+) +(?P<vrf_id>\d+)'
                            ' +(?P<table_id>0x[a_f0-9]+) +(?P<interface_count>\d+)'
                            ' +(?P<bfd>\w+)$')
            m = p1.match(line)
            if m:
                vrf_name = m.groupdict()['vrf']
                vrf_id = int(m.groupdict()['vrf_id'])
                table_id = m.groupdict()['table_id']
                interface_count = int(m.groupdict()['interface_count'])
                bfd_enabled = True if m.groupdict()['bfd'].lower() == 'yes' else False

                if 'vrf' not in parsed_dict:
                    parsed_dict['vrf'] = {}
                if vrf_name not in parsed_dict['vrf']:
                    parsed_dict['vrf'][vrf_name] = {}
                if 'address_family' not in parsed_dict['vrf'][vrf_name]:
                    parsed_dict['vrf'][vrf_name]['address_family'] = {}
                if af_name not in parsed_dict['vrf'][vrf_name]['address_family']:
                    parsed_dict['vrf'][vrf_name]['address_family'][af_name] = {}

                parsed_dict['vrf'][vrf_name]['address_family'] \
                    [af_name]['vrf_id'] = vrf_id

                parsed_dict['vrf'][vrf_name]['address_family'] \
                    [af_name]['table_id'] = table_id
                parsed_dict['vrf'][vrf_name]['address_family'] \
                    [af_name]['interface_count'] = interface_count

                parsed_dict['vrf'][vrf_name]['address_family'] \
                    [af_name]['bfd'] = {}
                parsed_dict['vrf'][vrf_name]['address_family'] \
                    [af_name]['bfd']['enable'] = bfd_enabled

                continue

            # State Limit: None
            p2 = re.compile(r'^\s*State +Limit: +(?P<state_limit>\w+)$')
            m = p2.match(line)
            if m:
                state_limit = m.groupdict()['state_limit'].lower()
                parsed_dict['vrf'][vrf_name]['address_family'] \
                [af_name]['state_limit'] = state_limit
                continue


            # Register Rate Limit: none
            p3 = re.compile(r'^\s*Register +Rate +Limit: +(?P<register_rate_limit>\w+)$')
            m = p3.match(line)
            if m:
                register_rate_limit = m.groupdict()['register_rate_limit'].lower()
                parsed_dict['vrf'][vrf_name]['address_family'] \
                    [af_name]['register_rate_limit'] = register_rate_limit
                continue

            # Shared tree route-map: v6spt-threshold-group-list
            p4 = re.compile(r'^\s*Shared +tree +route-map: +(?P<route_map>[\w\d\S]+)$')
            m = p4.match(line)
            if m:
                shared_tree_route_map = m.groupdict()['route_map']
                parsed_dict['vrf'][vrf_name]['address_family'] \
                    [af_name]['shared_tree_route_map'] = shared_tree_route_map
                continue

            # route-ranges: xxxxx
            p4 = re.compile(r'^\s*route-ranges:( +(?P<route_range>[\w\d\S]+))?$')
            m = p4.match(line)
            if m:
                if m.groupdict()['route_range']:
                    shared_tree_route_range = m.groupdict()['route_range']

                    parsed_dict['vrf'][vrf_name]['address_family'] \
                    [af_name]['shared_tree_route_ranges'] = shared_tree_route_range

                continue

            # Shared tree ranges: none
            p6 = re.compile(r'^\s*Shared +tree +ranges: +(?P<shared_tree_ranges>\w+)$')
            m = p6.match(line)
            if m:
                shared_tree_ranges = m.groupdict()['shared_tree_ranges']
                parsed_dict['vrf'][vrf_name]['address_family'] \
                    [af_name]['shared_tree_ranges'] = shared_tree_ranges

                continue

        return parsed_dict