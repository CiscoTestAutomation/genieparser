# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (Any,
                                                ListOf,
                                                Optional,
                                                Or)
from genie.libs.parser.utils.common import Common

class ShowLispInstanceIdServiceSchema(MetaParser):

    '''Schema for "show lisp all instance-id <instance_id> <service>" '''

    schema = {
        'lisp_id': {
            int: {
                'instance_id': {
                    int: {
                        'locator_table': str,
                        'eid_table': str,
                        'itr': {
                            'enabled': bool,
                            'proxy_itr_router': bool,
                            Optional('proxy_itr_rloc'): str,
                            Optional('local_rloc_last_resort'): str,
                            Optional('use_proxy_etr_rloc'): list,
                            'solicit_map_request': str,
                            'max_smr_per_map_cache': str,
                            'multiple_smr_supression_time': int
                        },
                        'etr': {
                            'enabled': bool,
                            'proxy_etr_router': bool,
                            'accept_mapping_data': str,
                            'map_cache_ttl': str
                        },
                        Optional('nat_traversal_router'): bool,
                        Optional('mobility_first_hop_router'): str,
                        'map_server': {
                            'enabled': bool
                        },
                        'map_resolver': {
                            'enabled': bool
                        },
                        'delegated_database_tree': str,
                        'mr_use_petr': {
                            'role': str,
                            Optional('locator_set'): str,
                        },
                        'first_packet_petr': {
                            'role': str,
                            Optional('locator_set'): str
                        },
                        Optional('multiple_ip_per_mac'): bool,
                        Optional('mcast_flood_access_tunnel'): bool,
                        Optional('pub_sub_eid'): bool,
                        Optional('pub_sub'): {
                            'role': bool,
                            Optional('publishers'): ListOf(str),
                            Optional('subscribers'): ListOf(str)
                        },
                        Optional('site_registration_limit'): int,
                        Optional('itr_map_resolvers'): {
                            'found': bool,
                            Optional(str): {
                                Optional('prefix_list'): str,
                                'reachable': bool
                            }
                        },
                        Optional('etr_map_servers'): {
                            'found': bool,
                            Optional(str): {
                                Optional('prefix_list'): str,
                                Optional('domain_id'): int,
                                'last_map_register': {
                                    'timestamp': str,
                                    Optional('transport_state'): str
                                }
                            }
                        },
                        Optional('xtr_id'): str,
                        Optional('site_id'): str,
                        'locator_status_algorithms': {
                            'rloc_probe_algorithm': str,
                            'rloc_probe_on_route_change': bool,
                            'rloc_probe_member_change': str,
                            'lsb_reports': str,
                            'ipv4_rloc_min_mask_len': int,
                            'ipv6_rloc_min_mask_len': int
                        },
                        'map_cache': {
                            'static_mappings': int,
                            'size': int,
                            'limit': int,
                            'imported_route': {
                                'count': int,
                                'limit': int
                            },
                            'activity_check_period': int,
                            'signal_supress': bool,
                            'conservative_allocation': bool,
                            Optional('fib_updates'): str,
                            'persistent': str,
                            'activity_tracking': bool
                        },
                        'database': {
                            'total_database_mapping': int,
                            'static_database': {
                                'size': int,
                                'limit': int
                            },
                            'dynamic_database': {
                                'size': int,
                                'limit': int
                            },
                            'route_import': {
                                'size': int,
                                'limit': int
                            },
                            'import_site_reg': {
                                'size': int,
                                'limit': int
                            },
                            'dummy_database': {
                                'size': int,
                                'limit': int
                            },
                            'import_publication': {
                                'size': int,
                                'limit': int
                            },
                            'proxy_database': {
                                'size': int
                            },
                            'inactive': {
                                'size': int
                            }
                        },
                        'publication_entries_exported': {
                            'map_cache': int,
                            'rib': int,
                            'database': int,
                            'prefix_list': int
                        },
                        'site_reg_entries_exported': {
                            'map_cache': int,
                            'rib': int
                        },
                        Optional('source_locator_configuration'): {
                            'vlans': {
                                Any(): {
                                    'address': str,
                                    'interface': str
                                }
                            }
                        },
                        'encapsulation_type': str,
                        Optional('ethernet_fast_detection'): bool
                    }
                }
            }
        }
    }


class ShowLispInstanceIdService(ShowLispInstanceIdServiceSchema):

    '''Parser for "show lisp instance-id {instance_id} {service}"'''

    cli_command = ['show lisp instance-id {instance_id} {service}',
                   'show lisp all instance-id {instance_id} {service}',
                   'show lisp {lisp_id} instance-id {instance_id} {service}',
                   'show lisp locator-table {locator_table} instance-id {instance_id} {service}']

    def cli(self, service, instance_id, lisp_id=None, locator_table=None, output=None):
        if output is None:
            if locator_table and instance_id and service:
                cmd = self.cli_command[3].format(locator_table=locator_table, instance_id=instance_id, service=service)
            elif lisp_id and instance_id and service:
                cmd = self.cli_command[2].format(lisp_id=lisp_id, instance_id=instance_id, service=service)
            elif instance_id and service:
                if "all" in self.cli_command:
                    cmd = self.cli_command[1].format(instance_id=instance_id, service=service)
                else:
                    cmd = self.cli_command[0].format(instance_id=instance_id, service=service)
            out = self.device.execute(cmd)
        else:
            out = output

        ret_dict = {}

        state_dict = {
            'disabled': False,
            'enabled': True}

        # Instance ID:                              4100
        p1 = re.compile(r'Instance ID:\s+(?P<instance_id>\d+)$')

        # Router-lisp ID:                      0
        p2 = re.compile(r'Router-lisp +ID *: +(?P<lisp_id>\d+)$')

        # Locator table:                       default
        p3 = re.compile(r'Locator +table *: +(?P<locator_table>\S+)$')

        # EID table:                                vrf red
        p4 = re.compile(r'EID table:\s+(?P<eid_table>.*)$')

        # Ingress Tunnel Router (ITR):         enabled
        # Egress Tunnel Router (ETR):          enabled
        p5 = re.compile(r'(Ingress|Egress) +Tunnel +Router '
                        r'+\((?P<type>(ITR|ETR))\) *: '
                        r'+(?P<enabled>(enabled|disabled))$')

        # Proxy-ITR Router (PITR):             disabled
        # Proxy-ETR Router (PETR):             disabled
        # Proxy-ETR Router (PETR):             enabled RLOCs: 10.10.10.10
        # Proxy-ITR Router (PITR):             enabled RLOCs: 2001:10:10:10::10
        p6 = re.compile(r'Proxy\-(ITR|ETR) +Router +\((?P<proxy_type>(PITR|PETR))\)'
                        r'*: +(?P<proxy_itr_router>(enabled|disabled))'
                        r'(?: +RLOCs: +(?P<proxy_itr_rloc>'
                        r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|[a-fA-F\d\:]+))?$')

        # ITR local RLOC (last resort):             *** NOT FOUND ***
        p7 = re.compile(r'^ITR +local +RLOC +\(last +resort\):\s+'
                        r'(?P<local_rloc_last_resort>.*)$')

        # ITR use proxy ETR RLOC(Encap IID):        1.1.1.1 (self), 66.66.66.66
        p8 = re.compile(r'^ITR\s+use +proxy +ETR +RLOC\(Encap IID\) *'
                        r': +(?P<use_proxy_etr_rloc_1>[\d.]+ *'
                        r'(\(self\))?),? *(?P<use_proxy_etr_rloc_2>([\d.]+)|([a-fA-F\d\:]+))?$')

        # ITR Solicit Map Request (SMR):       accept and process
        p9 = re.compile(r'^ITR +Solicit +Map +Request +\(SMR\) *:'
                        r'+(?P<solicit_map_request>.*)$')

        # Max SMRs per map-cache entry:      8 more specifics
        p10 = re.compile(r'^Max SMRs per map-cache entry:\s+(?P<max_smr_per_map_cache>.*)$')

        # Multiple SMR suppression time:     20 secs
        p11 = re.compile(r'^Multiple +SMR +suppression +time *: +'
                        r'(?P<multiple_smr_supression_time>\d+) +secs$')

        # ETR accept mapping data:             disabled, verify disabled
        p12 = re.compile(r'^ETR +accept +mapping +data *: +(?P<accept_mapping_data>.*)$')

        # ETR map-cache TTL:                   1d00h
        p13 = re.compile(r'^ETR +map-cache +TTL *: +(?P<map_cache_ttl>\S+)$')

        # NAT-traversal Router (NAT-RTR):      disabled
        p14 = re.compile(r'^NAT-traversal +Router +\(NAT\-RTR\) *: +'
                         r'(?P<nat_traversal_router>(enabled|disabled))$')

        # Mobility First-Hop Router:           disabled
        p15 = re.compile(r'Mobility +First-Hop +Router *:'
                         r' +(?P<mobility_first_hop_router>(enabled|disabled))$')

        # Map Server (MS):                     disabled
        p16 = re.compile(r'Map +Server +\(MS\) *:'
                        r' +(?P<enabled>(enabled|disabled))$')

        # Map Resolver (MR):                   disabled
        p17 = re.compile(r'Map +Resolver +\(MR\) *:'
                         r' +(?P<enabled>enabled|disabled)$')

        # Delegated Database Tree (DDT):       disabled
        p18 = re.compile(r'Delegated +Database +Tree +\(DDT\) *:'
                         r' +(?P<delegated_database_tree>enabled|disabled)$')

        # Mr-use-petr:                              enabled
        p19 = re.compile(r'^Mr-use-petr:\s+(?P<role>enabled|disabled)$')

        # Mr-use-petr locator set name:             RLOC1
        p20 = re.compile(r'^Mr-use-petr locator set name:\s+(?P<locator_set>\S+)$')

        # First-Packet pETR:                        enabled
        p21 = re.compile(r'^First-Packet pETR:\s+(?P<role>enabled|disabled)$')

        # First-Packet pETR locator set name:       RLOC1
        p22 = re.compile(r'^First-Packet pETR locator set name:\s+(?P<locator_set>\S+)$')

        # Multiple IP per MAC support:              disabled
        p23 = re.compile(r'^Multiple IP per MAC support:\s+'
                         r'(?P<multiple_ip_per_mac>disabled|enabled)$')

        # Multicast Flood Access-Tunnel:            disabled
        p24 = re.compile(r'^Multicast Flood Access-Tunnel:\s+'
                         r'(?P<mcast_flood_access_tunnel>disabled|enabled)$')

        # Publication-Subscription-EID:             disabled
        p25_1 = re.compile(r'^Publication-Subscription-EID:\s+'
                         r'(?P<pub_sub_eid>disabled|enabled)$')

        # Publication-Subscription:                 enabled
        p25 = re.compile(r'^Publication-Subscription:\s+(?P<role>enabled|disabled)$')

        # Publisher(s):                           *** NOT FOUND ***
        p26 = re.compile(r'^Publisher\(s\):\s+(?P<publishers>[\d.:]+)(?: +.*)?$')

        # Subscriber(s):                           *** NOT FOUND ***
        p27 = re.compile(r'^Subscriber\(s\):\s+(?P<subscribers>.*)')

        # Site Registration Limit:                  0
        p28 = re.compile(r'Site Registration Limit:\s+(?P<site_registration_limit>\d+)$')

        # ITR Map-Resolver(s):                      *** NOT FOUND ***
        p29_1 = re.compile(r'ITR Map-Resolver\(s\): +(?P<imr_not_found>\*\*\* NOT FOUND \*\*\*)$')

        # ITR Map-Resolver(s):                      3800:3800:3800:3800:3800:3800:3800:3800
        # ITR Map-Resolver(s):                      3120:3120:3120:3120:3120:3120:3120:3120 *** not reachable ***
        # ITR Map-Resolver(s):                      3130:3130:3130:3130:3130:3130:3130:3130 prefix-list site1list
        # ITR Map-Resolver(s):                      3140:3140:3140:3140:3140:3140:3140:3140 prefix-list site1list *** not reachable ***
        #                                           3800:3800:3800:3800:3800:3800:3800:3800
        #                                           3120:3120:3120:3120:3120:3120:3120:3120 *** not reachable ***
        #                                           3130:3130:3130:3130:3130:3130:3130:3130 prefix-list site1list
        #                                           3140:3140:3140:3140:3140:3140:3140:3140 prefix-list site1list *** not reachable ***
        p29_2 = re.compile(r'(ITR Map-Resolver\(s\):)? *(?P<imr_address>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
                           r'|([a-fA-F\d\:]+))( prefix-list (?P<imr_prefix_list>\w+))?'
                           r'( (?P<imr_not_reachable>)\*\*\* not reachable \*\*\*)?$')

        # ETR Map-Server(s) (last map-reg sent):    *** NOT FOUND ***
        p31_1 = re.compile(r'ETR Map-Server\(s\): +(?P<ems_not_found>\*\*\* NOT FOUND \*\*\*)$')

        # ETR Map-Server(s) (last map-reg sent):    3120:3120:3120:3120:3120:3120:3120:3120 (00:01:08, TCP)
        # ETR Map-Server(s) (last map-reg sent):    3130:3130:3130:3130:3130:3130:3130:3130 (00:00:09, UDP)
        # ETR Map-Server(s) (last map-reg sent):    3140:3140:3140:3140:3140:3140:3140:3140 (never)
        # ETR Map-Server(s) (last map-reg sent):    3120:3120:3120:3120:3120:3120:3120:3120 domain-id 1 (00:01:08, TCP)
        # ETR Map-Server(s) (last map-reg sent):    3130:3130:3130:3130:3130:3130:3130:3130 domain-id 1 (00:00:09, UDP)
        # ETR Map-Server(s) (last map-reg sent):    3140:3140:3140:3140:3140:3140:3140:3140 domain-id 1 (never)
        # ETR Map-Server(s) (last map-reg sent):    3120:3120:3120:3120:3120:3120:3120:3120 prefix-list site1list domain-id 1 (00:01:08, TCP)
        # ETR Map-Server(s) (last map-reg sent):    3130:3130:3130:3130:3130:3130:3130:3130 prefix-list site1list domain-id 1 (00:00:09, UDP)
        # ETR Map-Server(s) (last map-reg sent):    3140:3140:3140:3140:3140:3140:3140:3140 prefix-list site1list domain-id 1 (never)
        #                                           3120:3120:3120:3120:3120:3120:3120:3120 (00:01:08, TCP)
        #                                           3130:3130:3130:3130:3130:3130:3130:3130 (00:00:09, UDP)
        #                                           3140:3140:3140:3140:3140:3140:3140:3140 (never)
        #                                           3120:3120:3120:3120:3120:3120:3120:3120 domain-id 1 (00:01:08, TCP)
        #                                           3130:3130:3130:3130:3130:3130:3130:3130 domain-id 1 (00:00:09, UDP)
        #                                           3140:3140:3140:3140:3140:3140:3140:3140 domain-id 1 (never)
        #                                           3120:3120:3120:3120:3120:3120:3120:3120 prefix-list site1list domain-id 1 (00:01:08, TCP)
        #                                           3130:3130:3130:3130:3130:3130:3130:3130 prefix-list site1list domain-id 1 (00:00:09, UDP)
        #                                           3140:3140:3140:3140:3140:3140:3140:3140 prefix-list site1list domain-id 1 (never)
        p31_2 = re.compile(r'(ETR Map-Server\(s\) \(last map-reg sent\):)? *(?P<ems_address>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
                           r'|([a-fA-F\d\:]+))( prefix-list (?P<ems_prefix_list>\w+))?( domain-id (?P<ems_domain_id>\d+))?'
                           r' \((?P<ems_last_map_reg_time>[\w:\d]+)(, (?P<ems_last_transport_state>TCP|UDP))?\)$')

        # xTR-ID:                              0x730E0861-0x12996F6D-0xEFEA2114-0xE1C951F7
        p32 = re.compile(r'^xTR-ID *: +(?P<xtr_id>[a-fA-F0-9x-]+)$')

        # site-ID:                             unspecified
        p33 = re.compile(r'site-ID *: +(?P<site_id>\S+)$')

        # RLOC-probe algorithm:              disabled
        p34 = re.compile(r'RLOC\-probe +algorithm *: '
                         r'+(?P<rloc_probe_algorithm>enabled|disabled)$')

        # RLOC-probe on route change:        N/A (periodic probing disabled)
        p35 = re.compile(r'RLOC\-probe +on +route +change *: +(?P<rloc_probe_on_route_change>.*)$')

        # RLOC-probe on member change:       disabled
        p36 = re.compile(r'RLOC\-probe +on +member +change *:'
                         r' +(?P<rloc_probe_member_change>enabled|disabled)$')

        # LSB reports:                       process
        p37 = re.compile(r'LSB +reports *: +(?P<lsb_reports>\S+)$')

        # IPv4 RLOC minimum mask length:     /0
        p38 = re.compile(r'IPv4 +RLOC +minimum +mask +length *:'
                         r' +\/(?P<ipv4_rloc_min_mask_len>\d+)$')

        # IPv6 RLOC minimum mask length:     /0
        p39 = re.compile(r'IPv6 +RLOC +minimum +mask +length *:'
                         r' +\/(?P<ipv6_rloc_min_mask_len>\d+)$')

        # Static mappings configured:             1
        p40 = re.compile(r'Static mappings configured:\s+(?P<static_mappings>\d+)$')

        # Map-cache size/limit:                   2/4294967295
        p41 = re.compile(r'Map-cache size\/limit:\s+(?P<size>\d+)\/(?P<limit>\d+)$')

        # Imported route count/limit:             0/5000
        p42 = re.compile(r'Imported route count\/limit:\s+(?P<count>\d+)\/(?P<limit>\d+)$')

        # Map-cache activity check period:   60 secs
        p43 = re.compile(r'Map-cache +activity +check +period *:'
                         r' +(?P<activity_check_period>\d+) +secs$')

        # Map-cache signal suppress:              disabled
        p44 = re.compile(r'Map-cache signal suppress:\s+(?P<signal_supress>disabled|enabled)$')

        # Conservative-allocation:                disabled
        p45 = re.compile(r'Conservative-allocation:\s+(?P<conservative_allocation>disabled|enabled)$')

        # Map-cache FIB updates:                  established
        p46 = re.compile(r'Map-cache FIB updates:\s+(?P<fib_updates>\S+)$')

        # Persistent map-cache:              disabled
        p47 = re.compile(r'Persistent +map\-cache *:'
                         r' +(?P<persistent>enabled|disabled)$')

        # Map-cache activity-tracking:            enabled
        p48 = re.compile(r'Map-cache activity-tracking:\s+(?P<activity_tracking>\S+)$')

        # Total database mapping size:            2
        p49 = re.compile(r'Total database mapping size:\s+(?P<total_database_mapping>\d+)')

        # static database size/limit:             0/4294967295
        p50 = re.compile(r'static database size\/limit:\s+(?P<size>\d+)\/(?P<limit>\d+)$')

        # dynamic database size/limit:            2/4294967295
        p51 = re.compile(r'dynamic database size\/limit:\s+(?P<size>\d+)\/(?P<limit>\d+)$')

        # route-import database size/limit:       0/5000
        p52 = re.compile(r'route-import database size\/limit:\s+(?P<size>\d+)\/(?P<limit>\d+)$')

        # import-site-reg database size/limit:    0/4294967295
        p53 = re.compile(r'import-site-reg database size\/limit:\s+(?P<size>\d+)\/(?P<limit>\d+)$')

        # dummy database size/limit:              0/4294967295
        p54 = re.compile(r'dummy database size\/limit:\s+(?P<size>\d+)\/(?P<limit>\d+)$')

        # import-publication database size/limit: 0/4294967295
        p55 = re.compile(r'import-publication database size\/limit:\s+(?P<size>\d+)\/(?P<limit>\d+)$')

        # proxy database size:                    0
        p56 = re.compile(r'proxy database size:\s+(?P<size>\d+)$')

        # Inactive (deconfig/away) size:          0
        p57 = re.compile(r'Inactive \(deconfig\/away\) size:\s+(?P<size>\d+)$')

        # Map-cache:                              0
        p58 = re.compile(r'Map-cache:\s+(?P<map_cache>\d+)')

        # RIB:                                    0
        p59 = re.compile(r'RIB:\s+(?P<rib>\d+)')

        # Database:                               0
        p60 = re.compile(r'Database:\s+(?P<database>\d+)')

        # Prefix-list:                            0
        p61 = re.compile(r'Prefix-list:\s+(?P<prefix_list>\d+)')

        #   Vlan100: 10.229.11.1 (Loopback0)
        p62 = re.compile(r'Vlan(?P<vlans>(\d+))\: +(?P<address>([0-9\.\:]+)) +'
                         r'\((?P<interface>(\S+))\)$')

        # Encapsulation type:                       vxlan
        p63 = re.compile(r'Encapsulation type:\s+(?P<encapsulation_type>\S+)$')

        # Ethernet Fast Detection:                  enabled
        # Ethernet Fast Detection:                  disabled
        p64 = re.compile(r'^Ethernet Fast Detection:\s+(?P<eth_fast_detect>enabled|disabled)$')

        count = 0
        for line in out.splitlines():
            line = line.strip()

            # Instance ID:                              4100
            m = p1.match(line)
            if m:
                group = m.groupdict()
                instance_id = int(group['instance_id'])
                instance_dict = ret_dict.setdefault('lisp_id', {}).\
                                setdefault(None, {}).\
                                setdefault('instance_id',{}).\
                                setdefault(instance_id,{})
                continue

            # Router-lisp ID:                      0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                lisp_id = int(group['lisp_id'])
                ret_dict['lisp_id'][lisp_id] = ret_dict['lisp_id'].pop(None)
                continue

            # Locator table:                       default
            m = p3.match(line)
            if m:
                group = m.groupdict()
                locator_table = group['locator_table']
                instance_dict.update({'locator_table':locator_table})
                continue

            # EID table:                                vrf red
            m = p4.match(line)
            if m:
                group = m.groupdict()
                eid_table = group['eid_table']
                instance_dict.update({'eid_table':eid_table})
                continue

            # Ingress Tunnel Router (ITR):         enabled
            # Egress Tunnel Router (ETR):          enabled
            m = p5.match(line)
            if m:
                group = m.groupdict()
                enabled = state_dict[group['enabled'].lower()]
                tunnel_type = m.groupdict()['type'].lower()
                if tunnel_type == 'itr':
                    itr_dict = instance_dict.setdefault('itr', {})
                    itr_dict.update({'enabled':enabled})
                elif tunnel_type == 'etr':
                    etr_dict = instance_dict.setdefault('etr', {})
                    etr_dict.update({'enabled':enabled})
                continue

            # Proxy-ITR Router (PITR):             disabled
            # Proxy-ETR Router (PETR):             disabled
            m = p6.match(line)
            if m:
                group = m.groupdict()
                proxy_type = group['proxy_type'].lower()
                proxy_itr_rloc = group['proxy_itr_rloc']
                proxy_itr_router = state_dict[group['proxy_itr_router'].lower()]
                if proxy_type == 'pitr':
                    itr_dict.update({'proxy_itr_router':proxy_itr_router})
                elif proxy_type == 'petr':
                    etr_dict.update({'proxy_etr_router':proxy_itr_router})
                if group['proxy_itr_rloc']:
                    itr_dict.update({'proxy_itr_rloc':proxy_itr_rloc})
                continue

            # ITR local RLOC (last resort):             *** NOT FOUND ***
            m = p7.match(line)
            if m:
                group = m.groupdict()
                local_rloc_last_resort = group['local_rloc_last_resort']
                itr_dict.update({'local_rloc_last_resort':local_rloc_last_resort})
                continue

            # ITR use proxy ETR RLOC(Encap IID):        1.1.1.1 (self), 66.66.66.66
            m = p8.match(line)
            if m:
                group = m.groupdict()
                proxy_list = itr_dict.setdefault('use_proxy_etr_rloc',[])
                if group['use_proxy_etr_rloc_1']:
                    use_proxy_etr_rloc_val = group['use_proxy_etr_rloc_1']
                    proxy_list.append(use_proxy_etr_rloc_val)
                if group['use_proxy_etr_rloc_2']:
                    use_proxy_etr_rloc_val = group['use_proxy_etr_rloc_2']
                    proxy_list.append(use_proxy_etr_rloc_val)
                continue

            # ITR Solicit Map Request (SMR):       accept and process
            m = p9.match(line)
            if m:
                group = m.groupdict()
                solicit_map_request = group['solicit_map_request'].strip()
                itr_dict.update({'solicit_map_request':solicit_map_request})
                continue

            # Max SMRs per map-cache entry:      8 more specifics
            m = p10.match(line)
            if m:
                group = m.groupdict()
                max_smr_per_map_cache = group['max_smr_per_map_cache']
                itr_dict.update({'max_smr_per_map_cache':max_smr_per_map_cache})
                continue

            # Multiple SMR suppression time:     20 secs
            m = p11.match(line)
            if m:
                group = m.groupdict()
                multiple_smr_supression_time = int(group['multiple_smr_supression_time'])
                itr_dict.update({'multiple_smr_supression_time':multiple_smr_supression_time})
                continue

            # ETR accept mapping data:             disabled, verify disabled
            m = p12.match(line)
            if m:
                group = m.groupdict()
                accept_mapping_data = group['accept_mapping_data']
                etr_dict.update({'accept_mapping_data':accept_mapping_data})
                continue

            # ETR map-cache TTL:                   1d00h
            m = p13.match(line)
            if m:
                group = m.groupdict()
                map_cache_ttl = group['map_cache_ttl']
                etr_dict.update({'map_cache_ttl':map_cache_ttl})
                continue

            # NAT-traversal Router (NAT-RTR):      disabled
            m = p14.match(line)
            if m:
                group = m.groupdict()
                nat_traversal_router = state_dict[group['nat_traversal_router'].lower()]
                instance_dict.update({'nat_traversal_router':nat_traversal_router})
                continue

            # Mobility First-Hop Router:           disabled
            m = p15.match(line)
            if m:
                group = m.groupdict()
                mobility_first_hop_router = group['mobility_first_hop_router']
                instance_dict.update({'mobility_first_hop_router':mobility_first_hop_router})
                continue

            # Map Server (MS):                     disabled
            m = p16.match(line)
            if m:
                group = m.groupdict()
                enabled = state_dict[group['enabled'].lower()]
                map_server_dict = instance_dict.setdefault('map_server',{})
                map_server_dict.update({'enabled':enabled})
                continue

            # Map Resolver (MR):                   disabled
            m = p17.match(line)
            if m:
                group = m.groupdict()
                enabled = state_dict[group['enabled'].lower()]
                map_resolver_dict = instance_dict.setdefault('map_resolver',{})
                map_resolver_dict.update({'enabled':enabled})
                continue

            # Delegated Database Tree (DDT):       disabled
            m = p18.match(line)
            if m:
                group = m.groupdict()
                delegated_database_tree = group['delegated_database_tree']
                instance_dict.update({'delegated_database_tree':delegated_database_tree})
                continue

            # Mr-use-petr:                              enabled
            m = p19.match(line)
            if m:
                group = m.groupdict()
                role = group['role']
                mr_dict = instance_dict.setdefault('mr_use_petr',{})
                mr_dict.update({'role':role})
                continue

            # Mr-use-petr locator set name:             RLOC1
            m = p20.match(line)
            if m:
                group = m.groupdict()
                locator_set = group['locator_set']
                mr_dict.update({'locator_set':locator_set})
                continue

            # First-Packet pETR:                        enabled
            m = p21.match(line)
            if m:
                group = m.groupdict()
                role = group['role']
                first_dict = instance_dict.setdefault('first_packet_petr',{})
                first_dict.update({'role':role})
                continue

            # First-Packet pETR locator set name:       RLOC1
            m = p22.match(line)
            if m:
                group = m.groupdict()
                locator_set = group['locator_set']
                first_dict.update({'locator_set':locator_set})
                continue

            # Multiple IP per MAC support:              disabled
            m = p23.match(line)
            if m:
                group = m.groupdict()
                multiple_ip_per_mac = state_dict[group['multiple_ip_per_mac'].lower()]
                instance_dict.update({'multiple_ip_per_mac':multiple_ip_per_mac})
                continue

            # Multicast Flood Access-Tunnel:            disabled
            m = p24.match(line)
            if m:
                group = m.groupdict()
                mcast_flood_access_tunnel = state_dict[group['mcast_flood_access_tunnel'].lower()]
                instance_dict.update({'mcast_flood_access_tunnel':mcast_flood_access_tunnel})
                continue

            # Publication-Subscription-EID:             disabled
            m = p25_1.match(line)
            if m:
                group = m.groupdict()
                pub_sub_eid = state_dict[group['pub_sub_eid'].lower()]
                instance_dict.update({'pub_sub_eid':pub_sub_eid})
                continue

            # Publication-Subscription:                 enabled
            m = p25.match(line)
            if m:
                group = m.groupdict()
                role = state_dict[group['role'].lower()]
                pub_sub_dict = instance_dict.setdefault('pub_sub',{})
                pub_sub_dict.update({'role':role})
                continue

            # Publisher(s):                           *** NOT FOUND ***
            m = p26.match(line)
            if m:
                group = m.groupdict()
                publishers = group['publishers'].split(',')
                publishers_list = pub_sub_dict.setdefault('publishers',[])
                for publish in publishers:
                    publishers_list.append(publish)

            # Subscriber(s):                           *** NOT FOUND ***
            m = p27.match(line)
            if m:
                group = m.groupdict()
                subscribers = group['subscribers'].split(',')
                subscribers_list = pub_sub_dict.setdefault('subscribers',[])
                for subscribers in subscribers_list:
                    subscribers.append(subscribers)

            # Site Registration Limit:                  0
            m = p28.match(line)
            if m:
                group = m.groupdict()
                site_registration_limit = int(group['site_registration_limit'])
                instance_dict.update({'site_registration_limit':site_registration_limit})
                continue

            # ITR Map-Resolver(s):                      *** NOT FOUND ***
            m = p29_1.match(line)
            if m:
                group = m.groupdict()
                imr_dict = instance_dict.setdefault('itr_map_resolvers', {})
                imr_dict.update({'found': False})
                continue

            # ITR Map-Resolver(s):                      3800:3800:3800:3800:3800:3800:3800:3800
            # ITR Map-Resolver(s):                      3120:3120:3120:3120:3120:3120:3120:3120 *** not reachable ***
            # ITR Map-Resolver(s):                      3130:3130:3130:3130:3130:3130:3130:3130 prefix-list site1list
            # ITR Map-Resolver(s):                      3140:3140:3140:3140:3140:3140:3140:3140 prefix-list site1list *** not reachable ***
            #                                           3800:3800:3800:3800:3800:3800:3800:3800
            #                                           3120:3120:3120:3120:3120:3120:3120:3120 *** not reachable ***
            #                                           3130:3130:3130:3130:3130:3130:3130:3130 prefix-list site1list
            #                                           3140:3140:3140:3140:3140:3140:3140:3140 prefix-list site1list *** not reachable ***
            m = p29_2.match(line)
            if m:
                group = m.groupdict()
                imr_dict = instance_dict.setdefault('itr_map_resolvers', {})
                imr_dict.update({'found': True})
                imr_address_dict = imr_dict.setdefault(group['imr_address'], {})
                if 'imr_not_reachable' in group and group['imr_not_reachable'] is not None:
                    imr_address_dict.update({'reachable': False})
                else:
                    imr_address_dict.update({'reachable': True})
                if 'imr_prefix_list' in group and group['imr_prefix_list'] is not None:
                    imr_address_dict.update({'prefix_list': group['imr_prefix_list']})
                continue

            # ETR Map-Server(s) (last map-reg sent):    *** NOT FOUND ***
            m = p31_1.match(line)
            if m:
                group = m.groupdict()
                ems_dict = instance_dict.setdefault('etr_map_servers', {})
                ems_dict.update({'found': False})
                continue

            # ETR Map-Server(s) (last map-reg sent):    3120:3120:3120:3120:3120:3120:3120:3120 (00:01:08, TCP)
            # ETR Map-Server(s) (last map-reg sent):    3130:3130:3130:3130:3130:3130:3130:3130 (00:00:09, UDP)
            # ETR Map-Server(s) (last map-reg sent):    3140:3140:3140:3140:3140:3140:3140:3140 (never)
            # ETR Map-Server(s) (last map-reg sent):    3120:3120:3120:3120:3120:3120:3120:3120 domain-id 1 (00:01:08, TCP)
            # ETR Map-Server(s) (last map-reg sent):    3130:3130:3130:3130:3130:3130:3130:3130 domain-id 1 (00:00:09, UDP)
            # ETR Map-Server(s) (last map-reg sent):    3140:3140:3140:3140:3140:3140:3140:3140 domain-id 1 (never)
            # ETR Map-Server(s) (last map-reg sent):    3120:3120:3120:3120:3120:3120:3120:3120 prefix-list site1list domain-id 1 (00:01:08, TCP)
            # ETR Map-Server(s) (last map-reg sent):    3130:3130:3130:3130:3130:3130:3130:3130 prefix-list site1list domain-id 1 (00:00:09, UDP)
            # ETR Map-Server(s) (last map-reg sent):    3140:3140:3140:3140:3140:3140:3140:3140 prefix-list site1list domain-id 1 (never)
            #                                           3120:3120:3120:3120:3120:3120:3120:3120 (00:01:08, TCP)
            #                                           3130:3130:3130:3130:3130:3130:3130:3130 (00:00:09, UDP)
            #                                           3140:3140:3140:3140:3140:3140:3140:3140 (never)
            #                                           3120:3120:3120:3120:3120:3120:3120:3120 domain-id 1 (00:01:08, TCP)
            #                                           3130:3130:3130:3130:3130:3130:3130:3130 domain-id 1 (00:00:09, UDP)
            #                                           3140:3140:3140:3140:3140:3140:3140:3140 domain-id 1 (never)
            #                                           3120:3120:3120:3120:3120:3120:3120:3120 prefix-list site1list domain-id 1 (00:01:08, TCP)
            #                                           3130:3130:3130:3130:3130:3130:3130:3130 prefix-list site1list domain-id 1 (00:00:09, UDP)
            #                                           3140:3140:3140:3140:3140:3140:3140:3140 prefix-list site1list domain-id 1 (never)
            m = p31_2.match(line)
            if m:
                group = m.groupdict()
                ems_dict = instance_dict.setdefault('etr_map_servers', {})
                ems_dict.update({'found': True})
                ems_address_dict = ems_dict.setdefault(group['ems_address'], {})
                if 'ems_prefix_list' in group and group['ems_prefix_list'] is not None:
                    ems_address_dict.update({'prefix_list': group['ems_prefix_list']})
                if 'ems_domain_id' in group and group['ems_domain_id'] is not None:
                    ems_address_dict.update({'domain_id': int(group['ems_domain_id'])})
                ems_address_last_map_reg_dict = ems_address_dict.setdefault('last_map_register', {})
                ems_address_last_map_reg_dict.update({'timestamp': group['ems_last_map_reg_time']})
                if 'ems_last_transport_state' in group and group['ems_last_transport_state'] is not None:
                    ems_address_last_map_reg_dict.update({'transport_state': group['ems_last_transport_state']})
                continue

            # xTR-ID:                              0x730E0861-0x12996F6D-0xEFEA2114-0xE1C951F7
            m = p32.match(line)
            if m:
                group = m.groupdict()
                xtr_id = group['xtr_id']
                instance_dict.update({'xtr_id':xtr_id})
                continue

            # site-ID:                             unspecified
            m = p33.match(line)
            if m:
                group = m.groupdict()
                site_id = group['site_id']
                instance_dict.update({'site_id':site_id})
                continue

            # RLOC-probe algorithm:              disabled
            m = p34.match(line)
            if m:
                group = m.groupdict()
                rloc_probe_algorithm = group['rloc_probe_algorithm']
                locator_dict = instance_dict.setdefault('locator_status_algorithms',{})
                locator_dict.update({'rloc_probe_algorithm':rloc_probe_algorithm})
                continue

            # RLOC-probe on route change:        N/A (periodic probing disabled)
            m = p35.match(line)
            if m:
                group = m.groupdict()
                rloc_probe_on_route_change = group['rloc_probe_on_route_change']
                if rloc_probe_on_route_change == "enabled":
                    locator_dict.update({'rloc_probe_on_route_change':True})
                else:
                    locator_dict.update({'rloc_probe_on_route_change':False})
                continue

            # RLOC-probe on member change:       disabled
            m = p36.match(line)
            if m:
                group = m.groupdict()
                rloc_probe_member_change = group['rloc_probe_member_change']
                locator_dict.update({'rloc_probe_member_change':rloc_probe_member_change})
                continue

            # LSB reports:                       process
            m = p37.match(line)
            if m:
                group = m.groupdict()
                lsb_reports = group['lsb_reports']
                locator_dict.update({'lsb_reports':lsb_reports})
                continue

            # IPv4 RLOC minimum mask length:     /0
            m = p38.match(line)
            if m:
                group = m.groupdict()
                ipv4_rloc_min_mask_len = int(group['ipv4_rloc_min_mask_len'])
                locator_dict.update({'ipv4_rloc_min_mask_len':ipv4_rloc_min_mask_len})
                continue

            # IPv6 RLOC minimum mask length:     /0
            m = p39.match(line)
            if m:
                group = m.groupdict()
                ipv6_rloc_min_mask_len = int(group['ipv6_rloc_min_mask_len'])
                locator_dict.update({'ipv6_rloc_min_mask_len':ipv6_rloc_min_mask_len})
                continue

            # Static mappings configured:             1
            m = p40.match(line)
            if m:
                group = m.groupdict()
                static_mappings = int(group['static_mappings'])
                map_cache_dict = instance_dict.setdefault('map_cache',{})
                map_cache_dict.update({'static_mappings':static_mappings})
                continue

            # Map-cache size/limit:                   2/4294967295
            m = p41.match(line)
            if m:
                group = m.groupdict()
                size = int(group['size'])
                limit = int(group['limit'])
                map_cache_dict.update({'size':size,
                                       'limit':limit})
                continue

            # Imported route count/limit:             0/5000
            m = p42.match(line)
            if m:
                group = m.groupdict()
                count = int(group['count'])
                limit = int(group['limit'])
                imported_dict = map_cache_dict.setdefault('imported_route',{})
                imported_dict.update({'count':count,
                                       'limit':limit})
                continue

            # Map-cache activity check period:   60 secs
            m = p43.match(line)
            if m:
                group = m.groupdict()
                activity_check_period = int(group['activity_check_period'])
                map_cache_dict.update({'activity_check_period':activity_check_period})
                continue

            # Map-cache signal suppress:              disabled
            m = p44.match(line)
            if m:
                group = m.groupdict()
                signal_supress = state_dict[group['signal_supress'].lower()]
                map_cache_dict.update({'signal_supress':signal_supress})
                continue

            # Conservative-allocation:                disabled
            m = p45.match(line)
            if m:
                group = m.groupdict()
                conservative_allocation = state_dict[group['conservative_allocation'].lower()]
                map_cache_dict.update({'conservative_allocation':conservative_allocation})
                continue

            # Map-cache FIB updates:                  established
            m = p46.match(line)
            if m:
                group = m.groupdict()
                fib_updates = group['fib_updates']
                map_cache_dict.update({'fib_updates':fib_updates})
                continue

            # Persistent map-cache:              disabled
            m = p47.match(line)
            if m:
                group = m.groupdict()
                persistent = group['persistent']
                map_cache_dict.update({'persistent':persistent})
                continue

            # Map-cache activity-tracking:            enabled
            m = p48.match(line)
            if m:
                group = m.groupdict()
                activity_tracking = state_dict[group['activity_tracking'].lower()]
                map_cache_dict.update({'activity_tracking':activity_tracking})
                continue

            # Total database mapping size:            2
            m = p49.match(line)
            if m:
                group = m.groupdict()
                total_database_mapping = int(group['total_database_mapping'])
                database_dict = instance_dict.setdefault('database',{})
                database_dict.update({'total_database_mapping':total_database_mapping})
                continue

            # static database size/limit:             0/4294967295
            m = p50.match(line)
            if m:
                group = m.groupdict()
                size = int(group['size'])
                limit = int(group['limit'])
                static_dict = database_dict.setdefault('static_database',{})
                static_dict.update({'size':size,
                                    'limit':limit})
                continue

            # dynamic database size/limit:            2/4294967295
            m = p51.match(line)
            if m:
                group = m.groupdict()
                size = int(group['size'])
                limit = int(group['limit'])
                dynamic_dict = database_dict.setdefault('dynamic_database',{})
                dynamic_dict.update({'size':size,
                                    'limit':limit})
                continue

            # route-import database size/limit:       0/5000
            m = p52.match(line)
            if m:
                group = m.groupdict()
                size = int(group['size'])
                limit = int(group['limit'])
                route_dict = database_dict.setdefault('route_import',{})
                route_dict.update({'size':size,
                                    'limit':limit})
                continue

            # import-site-reg database size/limit:    0/4294967295
            m = p53.match(line)
            if m:
                group = m.groupdict()
                size = int(group['size'])
                limit = int(group['limit'])
                import_dict = database_dict.setdefault('import_site_reg',{})
                import_dict.update({'size':size,
                                    'limit':limit})
                continue

            # dummy database size/limit:              0/4294967295
            m = p54.match(line)
            if m:
                group = m.groupdict()
                size = int(group['size'])
                limit = int(group['limit'])
                dummy_dict = database_dict.setdefault('dummy_database',{})
                dummy_dict.update({'size':size,
                                   'limit':limit})
                continue

            # import-publication database size/limit: 0/4294967295
            m = p55.match(line)
            if m:
                group = m.groupdict()
                size = int(group['size'])
                limit = int(group['limit'])
                import_dict = database_dict.setdefault('import_publication',{})
                import_dict.update({'size':size,
                                    'limit':limit})
                continue

            # proxy database size:                    0
            m = p56.match(line)
            if m:
                group = m.groupdict()
                size = int(group['size'])
                proxy_dict = database_dict.setdefault('proxy_database',{})
                proxy_dict.update({'size':size})
                continue

            # Inactive (deconfig/away) size:          0
            m = p57.match(line)
            if m:
                group = m.groupdict()
                size = int(group['size'])
                inactive_dict = database_dict.setdefault('inactive',{})
                inactive_dict.update({'size':size})
                continue

            # Map-cache:                              0
            m = p58.match(line)
            if m:
                group = m.groupdict()
                map_cache = int(group['map_cache'])
                publication_dict = instance_dict.setdefault('publication_entries_exported',{})
                if 'map_cache' not in publication_dict:
                    publication_dict.update({'map_cache':map_cache})
                else:
                    site_reg_dict = instance_dict.setdefault('site_reg_entries_exported',{})
                    site_reg_dict.update({'map_cache':map_cache})
                continue

            # RIB:                                    0
            m = p59.match(line)
            if m:
                group = m.groupdict()
                rib = int(group['rib'])
                if 'rib' not in publication_dict:
                    publication_dict.update({'rib':rib})
                else:
                    site_reg_dict.update({'rib':rib})
                continue

            # Database:                               0
            m = p60.match(line)
            if m:
                group = m.groupdict()
                database = int(group['database'])
                publication_dict.update({'database':database})
                continue

            # Prefix-list:                            0
            m = p61.match(line)
            if m:
                group = m.groupdict()
                prefix_list = int(group['prefix_list'])
                publication_dict.update({'prefix_list':prefix_list})
                continue

            #    Vlan100: 10.229.11.1 (Loopback0)
            m = p62.match(line)
            if m:
                group = m.groupdict()
                vlans = group['vlans']
                address = group['address']
                interface = group['interface']
                source_dict = instance_dict.setdefault('source_locator_configuration',{}).\
                                setdefault('vlans',{}).\
                                setdefault(vlans,{})
                source_dict.update({'address':address,
                                    'interface':interface})
                continue

            # Encapsulation type:                       vxlan
            m = p63.match(line)
            if m:
                group = m.groupdict()
                encapsulation_type = group['encapsulation_type']
                instance_dict.update({'encapsulation_type':encapsulation_type})
                continue

            # Ethernet Fast Detection:                  enabled
            # Ethernet Fast Detection:                  disabled
            m = p64.match(line)
            if m:
                group = m.groupdict()
                fast_detect = group['eth_fast_detect'] == 'enabled'
                instance_dict.update({'ethernet_fast_detection': fast_detect})
                continue

        return ret_dict
      
      
class ShowLispSubscriberSchema(MetaParser):

    ''' Schema for
        * show lisp {lisp_id} instance-id {instance_id} ipv4 subscriber
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 subscriber
        * show lisp instance-id {instance_id} ipv4 subscriber
        * show lisp eid-table {eid_table} ipv4 subscriber
        * show lisp eid-table vrf {vrf} ipv4 subscriber
        * show lisp {lisp_id} instance-id {instance_id} ipv6 subscriber
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv6 subscriber
        * show lisp instance-id {instance_id} ipv6 subscriber
        * show lisp eid-table {eid_table} ipv6 subscriber
        * show lisp eid-table vrf {vrf} ipv6 subscriber
        * show lisp {lisp_id} instance-id {instance_id} ethernet subscriber
        * show lisp locator-table {locator_table} instance-id {instance_id} ethernet subscriber
        * show lisp instance-id {instance_id} ethernet subscriber
        * show lisp eid-table vlan {vlan} ethernet subscriber
    '''

    schema = {
        'lisp_id': {
            int: {
                'instance_id': {
                    int: {
                        'entries': int,
                        'subscribers': {
                          str:{
                            	Optional('port'): int,
                            	'type': str,
                            	Optional('affinity_id_x'): int,
                            	Optional('affinity_id_y'): int
                            }
                        }
                    }
                }
            }
        }
    }

class ShowLispSubscriberSuperParser(ShowLispSubscriberSchema):
    """ Parser for:
        * show lisp {lisp_id} instance-id {instance_id} ipv4 subscriber
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 subscriber
        * show lisp instance-id {instance_id} ipv4 subscriber
        * show lisp eid-table {eid_table} ipv4 subscriber
        * show lisp eid-table vrf {vrf} ipv4 subscriber
        * show lisp {lisp_id} instance-id {instance_id} ipv6 subscriber
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv6 subscriber
        * show lisp instance-id {instance_id} ipv6 subscriber
        * show lisp eid-table {eid_table} ipv6 subscriber
        * show lisp eid-table vrf {vrf} ipv6 subscriber
        * show lisp {lisp_id} instance-id {instance_id} ethernet subscriber
        * show lisp locator-table {locator_table} instance-id {instance_id} ethernet subscriber
        * show lisp instance-id {instance_id} ethernet subscriber
        * show lisp eid-table vlan {vlan} ethernet subscriber
    """

    def cli(self, output=None, lisp_id=None, instance_id=None):

        ret_dict = {}

        # To handle lisp_id
        if not lisp_id or isinstance(lisp_id, str):
            lisp_id = 0
        elif lisp_id.isdigit():
            lisp_id = int(lisp_id)

        # To get instance_id from device
        if not instance_id:
            self.device.sendline('sh lisp eid-table vrf red ipv4 | i Instance')
            out = self.device.expect(
                [r'Instance ID:\s+\S+'],
                timeout=2).match_output
            p0 = re.compile('^Instance ID:\s+(?P<instance_id>\d+)$')
            group = p0.match(out)
            instance_id = int(group['instance_id'])
        else:
            if instance_id.isdigit():
                instance_id = int(instance_id)


        # Output for router lisp 0
        # Output for router lisp 0 instance-id 193
        # Output for router lisp 2 instance-id 101
        p1 = re.compile(r'^Output\s+for\s+router\s+lisp\s+(?P<lisp_id>(\d+))'
                        r'(?: +instance-id +(?P<instance_id>(\d+)))?$')
        # Entries total 1
        p2 = re.compile(r'^Entries\s+total\s+(?P<entries>\d+)$')

        # 66.66.66.66:54087         IID
        # 77.77.77.77:54123         IID
        # 100.110.110.110:45676     IID        200 , 10
        # 2001:10:10:10::10.49787   IID        -
        p3 = re.compile(r'^(?P<subscriber_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
                        r'|[a-fA-F\d\:]+):?\.?(?P<port>\d+)\s+(?P<type>\S+)'
                        r'(\s+(?P<affinity_id_x>\d+))?(\s+,\s+(?P<affinity_id_y>\d+))?')

        for line in output.splitlines():
            line = line.strip()

            # Output for router lisp 0
            # Output for router lisp 0 instance-id 193
            # Output for router lisp 2 instance-id 101
            m = p1.match(line)
            if m:
                group = m.groupdict()
                lisp_id = int(group['lisp_id'])
                if group['instance_id']:
                    instance_id = int(group['instance_id'])
                continue

            # Entries total 1
            m = p2.match(line)
            if m:
                group = m.groupdict()
                lisp_id_dict = \
                    ret_dict.setdefault('lisp_id', {})\
                        .setdefault(lisp_id, {})\
                        .setdefault('instance_id', {})\
                        .setdefault(instance_id, {})
                lisp_id_dict.update({'entries': int(group['entries'])})
                continue

            # 66.66.66.66:54087         IID
            # 77.77.77.77:54123         IID
            m = p3.match(line)
            if m:
                group = m.groupdict()
                subscribers_dict = lisp_id_dict.setdefault('subscribers', {}).setdefault(group['subscriber_ip'], {})
                if group['affinity_id_y']:
                    subscribers_dict.update({'port': int(group['port']),
                                             'type': group['type'],
                                             'affinity_id_x':int(group['affinity_id_x']),
                                             'affinity_id_y':int(group['affinity_id_y'])})
                elif group['affinity_id_x']:
                    subscribers_dict.update({'port': int(group['port']),
                                             'type': group['type'],
                                             'affinity_id_x':int(group['affinity_id_x'])})
                elif group['port']:
                    subscribers_dict.update({'port': int(group['port']),
                                             'type': group['type']})
                else:
                    subscribers_dict.update({'port': int(group['port']),
                                             'type': group['type']})
                continue
        return ret_dict

class ShowLispIpv4Subscriber(ShowLispSubscriberSuperParser):
    """ Parser for:
        * show lisp {lisp_id} instance-id {instance_id} ipv4 subscriber
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 subscriber
        * show lisp instance-id {instance_id} ipv4 subscriber
        * show lisp eid-table {eid_table} ipv4 subscriber
        * show lisp eid-table vrf {vrf} ipv4 subscriber
    """

    cli_command = [
        'show lisp {lisp_id} instance-id {instance_id} ipv4 subscriber',
        'show lisp locator-table {locator_table} instance-id {instance_id} ipv4 subscriber',
        'show lisp instance-id {instance_id} ipv4 subscriber',
        'show lisp eid-table {eid_table} ipv4 subscriber',
        'show lisp eid-table vrf {vrf} ipv4 subscriber'
    ]

    def cli(self, output=None, lisp_id=None, instance_id=None, locator_table=None, eid_table=None,
            vrf=None):

        if output is None:
            if lisp_id and instance_id:
                output = self.device.execute(self.cli_command[0].\
                                             format(lisp_id=lisp_id, instance_id=instance_id))
            elif locator_table and instance_id:
                output = self.device.execute(self.cli_command[1].\
                                             format(locator_table=locator_table, instance_id=instance_id))
            elif instance_id:
                output = self.device.execute(self.cli_command[2].format(instance_id=instance_id))
            elif eid_table:
                output = self.device.execute(self.cli_command[3].format(eid_table=eid_table))
            else:
                output = self.device.execute(self.cli_command[4].format(vrf=vrf))

        return super().cli(output=output, lisp_id=lisp_id, instance_id=instance_id)


class ShowLispIpv6Subscriber(ShowLispSubscriberSuperParser):
    """ Parser for:
        * show lisp {lisp_id} instance-id {instance_id} ipv6 subscriber
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv6 subscriber
        * show lisp instance-id {instance_id} ipv6 subscriber
        * show lisp eid-table {eid_table} ipv6 subscriber
        * show lisp eid-table vrf {vrf} ipv6 subscriber
    """

    cli_command = [
        'show lisp {lisp_id} instance-id {instance_id} ipv6 subscriber',
        'show lisp locator-table {locator_table} instance-id {instance_id} ipv6 subscriber',
        'show lisp instance-id {instance_id} ipv6 subscriber',
        'show lisp eid-table {eid_table} ipv6 subscriber',
        'show lisp eid-table vrf {vrf} ipv6 subscriber',
    ]

    def cli(self, output=None, lisp_id=None, instance_id=None, locator_table=None, eid_table=None,
            vrf=None):

        if output is None:
            if lisp_id and instance_id:
                output = self.device.execute(self.cli_command[0].\
                                             format(lisp_id=lisp_id, instance_id=instance_id))
            elif locator_table and instance_id:
                output = self.device.execute(self.cli_command[1].\
                                             format(locator_table=locator_table, instance_id=instance_id))
            elif instance_id:
                output = self.device.execute(self.cli_command[2].format(instance_id=instance_id))
            elif eid_table:
                output = self.device.execute(self.cli_command[3].format(eid_table=eid_table))
            else:
                output = self.device.execute(self.cli_command[4].format(vrf=vrf))

        return super().cli(output=output, lisp_id=lisp_id, instance_id=instance_id)


class ShowLispEthernetSubscriber(ShowLispSubscriberSuperParser):
    """ Parser for:
        * show lisp {lisp_id} instance-id {instance_id} ethernet subscriber
        * show lisp locator-table {locator_table} instance-id {instance_id} ethernet subscriber
        * show lisp instance-id {instance_id} ethernet subscriber
        * show lisp eid-table vlan {vlan} ethernet subscriber
    """

    cli_command = [
        'show lisp {lisp_id} instance-id {instance_id} ethernet subscriber',
        'show lisp locator-table {locator_table} instance-id {instance_id} ethernet subscriber',
        'show lisp instance-id {instance_id} ethernet subscriber',
        'show lisp eid-table vlan {vlan} ethernet subscriber',
    ]

    def cli(self, output=None, lisp_id=None, instance_id=None, locator_table=None, vlan=None):

        if output is None:
            if lisp_id and instance_id:
                output = self.device.execute(self.cli_command[0].\
                                             format(lisp_id=lisp_id, instance_id=instance_id))
            elif locator_table and instance_id:
                output = self.device.execute(self.cli_command[1].\
                                             format(locator_table=locator_table, instance_id=instance_id))
            elif instance_id:
                output = self.device.execute(self.cli_command[2].format(instance_id=instance_id))
            else:
                output = self.device.execute(self.cli_command[3].format(vlan=vlan))

        return super().cli(output=output, lisp_id=lisp_id, instance_id=instance_id)
