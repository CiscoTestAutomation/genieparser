"""show_lisp_service.py

"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (Any,
                                                ListOf,
                                                Optional,
                                                Or)
from genie.libs.parser.utils.common import Common

from genie.libs.parser.iosxe.show_lisp_super import *


# ==============================================================
# Schema for 'show lisp all instance-id <instance_id> <service>'
# ==============================================================
class ShowLispServiceSchema(MetaParser):

    '''Schema for "show lisp all instance-id <instance_id> <service>" '''

    schema = {
        'lisp_id': {
            int:{
                'locator_table': str,
                'itr':{
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
                    Optional('locator_set'): str
                    },
                'first_packet_petr': {
                    'role': str,
                    Optional('locator_set'): str
                    },
                Optional('multiple_ip_per_mac'): bool,
                Optional('mcast_flood_access_tunnel'): bool,
                Optional('pub_sub'): {
                    'role': bool,
                    Optional('publishers'): list,
                    Optional('subscribers'): list
                    },
                Optional('mapping_servers'): {
                    Any():
                        {'ms_address': str,
                         Optional('prefix_list'): str,
                         },
                        },
                Optional('map_resolvers'): {
                    Any(): {
                        'mr_address': str,
                        Optional('prefix_list'): str
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
                    'limit': int,
                    'activity_check_period': int,
                    'persistent': str
                    },
                'database': {
                    'dynamic_database_limit': int
                    },
                Optional('source_locator_configuration'):
                    {'vlans':
                        {Any():
                            {'address': str,
                             'interface': str,
                            },
                        },
                    }
                }
            }
        }


# ==============================================================
# Parser for 'show lisp all instance-id <instance_id> <service>'
# ==============================================================
class ShowLispService(ShowLispServiceSchema):

    '''Parser for "show lisp all instance-id <instance_id> <service>"'''

    cli_command = ['show lisp service {service}',
                   'show lisp {lisp_id} service {service}']

    def cli(self, service, lisp_id=None, output=None):

        if output is None:
            if lisp_id and service:
                cmd = self.cli_command[1].format(lisp_id=lisp_id,service=service)
            else:
                cmd = self.cli_command[0].format(service=service)
            out = self.device.execute(cmd)
        else:
            out = output

        ret_dict = {}

        # Router-lisp ID:                      0
        p1 = re.compile(r'Router-lisp +ID *: +(?P<lisp_id>(\d+))$')

        # Locator table:                       default
        p2 = re.compile(r'Locator +table *: +(?P<locator_table>(\S+))$')

        # Ingress Tunnel Router (ITR):         enabled
        # Egress Tunnel Router (ETR):          enabled
        p3 = re.compile(r'(Ingress|Egress) +Tunnel +Router '
                        r'+\((?P<type>(ITR|ETR))\) *: '
                        r'+(?P<enabled>(enabled|disabled))$')

        # Proxy-ITR Router (PITR):             disabled
        # Proxy-ETR Router (PETR):             disabled
        # Proxy-ETR Router (PETR):             enabled RLOCs: 10.10.10.10
        # Proxy-ITR Router (PITR):             enabled RLOCs: 2001:21:21:21::21
        p4 = re.compile(r'Proxy\-(ITR|ETR) +Router +\((?P<proxy_type>(PITR|PETR))\)'
                        r'*: +(?P<proxy_itr_router>(enabled|disabled))'
                        r'(?: +RLOCs: +(?P<proxy_itr_rloc>'
                        r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|[a-fA-F\d\:]+))?$')

        # ITR local RLOC (last resort):             *** NOT FOUND ***
        p5 = re.compile(r'^ITR +local +RLOC +\(last +resort\):\s+'
                        r'(?P<local_rloc_last_resort>.*)$')

        # ITR use proxy ETR RLOC(s):           10.10.10.10
        p6 = re.compile(r'^ITR\s+use +proxy +ETR +RLOC\(Encap IID\) *:'
                        r'+(?P<use_proxy_etr_rloc>.*)$')

        # ITR Solicit Map Request (SMR):       accept and process
        p7 = re.compile(r'^ITR +Solicit +Map +Request +\(SMR\) *:'
                        r'+(?P<solicit_map_request>(.*))$')

        # Max SMRs per map-cache entry:      8 more specifics
        p8 = re.compile(r'^Max SMRs per map-cache entry:\s+(?P<max_smr_per_map_cache>.*)$')

        # Multiple SMR suppression time:     20 secs
        p9 = re.compile(r'^Multiple +SMR +suppression +time *: +'
                        r'(?P<multiple_smr_supression_time>(\d+)) +secs$')

        # ETR accept mapping data:             disabled, verify disabled
        p10 = re.compile(r'^ETR +accept +mapping +data *: +(?P<accept_mapping_data>(.*))$')

        # ETR map-cache TTL:                   1d00h
        p11 = re.compile(r'^ETR +map-cache +TTL *: +(?P<map_cache_ttl>(\S+))$')

        # NAT-traversal Router (NAT-RTR):      disabled
        p12 = re.compile(r'^NAT-traversal +Router +\(NAT\-RTR\) *: +'
                         r'(?P<nat_traversal_router>(enabled|disabled))$')

        # Mobility First-Hop Router:           disabled
        p13 = re.compile(r'Mobility +First-Hop +Router *:'
                         r' +(?P<mobility_first_hop_router>(enabled|disabled))$')

        # Map Server (MS):                     disabled
        p14 = re.compile(r'Map +Server +\(MS\) *:'
                        r' +(?P<enabled>(enabled|disabled))$')

        # Map Resolver (MR):                   disabled
        p15 = re.compile(r'Map +Resolver +\(MR\) *:'
                         r' +(?P<enabled>(enabled|disabled))$')

        # Delegated Database Tree (DDT):       disabled
        p16 = re.compile(r'Delegated +Database +Tree +\(DDT\) *:'
                         r' +(?P<delegated_database_tree>(enabled|disabled))$')

        # Mr-use-petr:                              enabled
        p17 = re.compile(r'^Mr-use-petr:\s+(?P<role>enabled|disabled)$')

        # Mr-use-petr locator set name:             RLOC1
        p18 = re.compile(r'^Mr-use-petr locator set name:\s+(?P<locator_set>\S+)$')

        # First-Packet pETR:                        enabled
        p19 = re.compile(r'^First-Packet pETR:\s+(?P<role>enabled|disabled)$')

        # First-Packet pETR locator set name:       RLOC1
        p20 = re.compile(r'^First-Packet pETR locator set name:\s+(?P<locator_set>\S+)$')

        # Multiple IP per MAC support:              disabled
        p21 = re.compile(r'^Multiple IP per MAC support:\s+'
                         r'(?P<multiple_ip_per_mac>disabled|enabled)$')

        # Multicast Flood Access-Tunnel:            disabled
        p22 = re.compile(r'^Multicast Flood Access-Tunnel:\s+'
                         r'(?P<mcast_flood_access_tunnel>disabled|enabled)$')

        # Publication-Subscription:                 enabled
        p23 = re.compile(r'^Publication-Subscription:\s+(?P<role>enabled|disabled)$')

        # Publisher(s):                           *** NOT FOUND ***
        # Publisher(s):                           2001:4:4:4::4
        p24 = re.compile(r'^Publisher\(s\):\s+(?P<publishers>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|[a-fA-F\d\:]+)')

        # Subscriber(s):                           *** NOT FOUND ***
        # Subscriber(s):                           2001:4:4:4::4
        p25 = re.compile(r'^Subscriber\(s\):\s+(?P<subscribers>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|[a-fA-F\d\:]+)')

        # ITR Map-Resolver(s):                 10.64.4.4, 10.166.13.13
        p26 = re.compile(r'ITR +Map\-Resolver\(s\) *: +(?P<mr_address>(.*))$')

        #                                      10.84.66.66 *** not reachable ***
        p26_1 = re.compile(r'^(?P<prefix_list>([0-9\.\:]+)|([a-fA-F\d\:]+))(?: +\*.*)?$')

        # ETR Map-Server(s):                   10.64.4.4 (17:49:58), 10.166.13.13 (00:00:35)
        p27 = re.compile(r'ETR +Map\-Server\(s\) *: +(?P<ms_address>(.*))$')

        #                                      10.84.66.66 (never)
        p27_1 = re.compile(r'^(?P<prefix_list>([0-9\.\:]+)|([a-fA-F\d\:]+))(?: +\((?P<uptime>(\S+))\))?$')

        # xTR-ID:                              0x730E0861-0x12996F6D-0xEFEA2114-0xE1C951F7
        p28 = re.compile(r'^xTR-ID *: +(?P<xtr_id>(\S+))$')

        # site-ID:                             unspecified
        p29 = re.compile(r'site-ID *: +(?P<site_id>(\S+))$')

        # RLOC-probe algorithm:              disabled
        p30 = re.compile(r'RLOC\-probe +algorithm *: '
                         r'+(?P<rloc_probe_algorithm>(enabled|disabled))$')

        # RLOC-probe on route change:        N/A (periodic probing disabled)
        p31 = re.compile(r'RLOC\-probe +on +route +change *: +(?P<rloc_probe_on_route_change>(.*))$')

        # RLOC-probe on member change:       disabled
        p32 = re.compile(r'RLOC\-probe +on +member +change *:'
                         r' +(?P<rloc_probe_member_change>(enabled|disabled))$')

        # LSB reports:                       process
        p33 = re.compile(r'LSB +reports *: +(?P<lsb_reports>(\S+))$')

        # IPv4 RLOC minimum mask length:     /0
        p34 = re.compile(r'IPv4 +RLOC +minimum +mask +length *:'
                         r' +\/(?P<ipv4_rloc_min_mask_len>(\d+))$')

        # IPv6 RLOC minimum mask length:     /0
        p35 = re.compile(r'IPv6 +RLOC +minimum +mask +length *:'
                         r' +\/(?P<ipv6_rloc_min_mask_len>(\d+))$')

        # Map-cache limit:                   5120
        p36 = re.compile(r'Map\-cache +limit *: +(?P<limit>(\d+))$')

        # Map-cache activity check period:   60 secs
        p37 = re.compile(r'Map-cache +activity +check +period *:'
                         r' +(?P<activity_check_period>(\d+)) +secs$')

        # Persistent map-cache:              disabled
        p38 = re.compile(r'Persistent +map\-cache *:'
                         r' +(?P<persistent>(enabled|disabled))$')

        # Dynamic database mapping limit:    5120
        p39 = re.compile(r'Dynamic +database +mapping +limit *:'
                         r' +(?P<dynamic_database_limit>(\d+))$')

        #   Vlan100: 10.229.11.1 (Loopback0)
        p40 = re.compile(r'Vlan(?P<vlans>(\d+))\: +(?P<address>([0-9\.\:]+)) +'
                         r'\((?P<interface>(\S+))\)$')

        for line in out.splitlines():
            line = line.strip()

            # Router-lisp ID:                      0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                lisp_id = int(group['lisp_id'])
                lisp_dict = ret_dict.setdefault('lisp_id', {}).\
                                setdefault(lisp_id, {})
                continue

            # Locator table:                       default
            m = p2.match(line)
            if m:
                group = m.groupdict()
                locator_table = group['locator_table']
                lisp_dict.update({'locator_table':locator_table})
                continue

            # Ingress Tunnel Router (ITR):         enabled
            # Egress Tunnel Router (ETR):          enabled
            m = p3.match(line)
            if m:
                group = m.groupdict()
                enabled_val = group['enabled']
                enabled = bool(re.search('enable',enabled_val))
                tunnel_type = m.groupdict()['type'].lower()
                if tunnel_type == 'itr':
                    itr_dict = lisp_dict.setdefault('itr', {})
                    itr_dict.update({'enabled':enabled})
                elif tunnel_type == 'etr':
                    etr_dict = lisp_dict.setdefault('etr', {})
                    etr_dict.update({'enabled':enabled})
                continue

            # Proxy-ITR Router (PITR):             disabled
            # Proxy-ETR Router (PETR):             disabled
            m = p4.match(line)
            if m:
                group = m.groupdict()
                proxy_type = group['proxy_type'].lower()
                proxy_itr_rloc = group['proxy_itr_rloc']
                proxy_itr_router_val = group['proxy_itr_router']
                proxy_itr_router = bool(re.search('enabled',proxy_itr_router_val))
                if proxy_type == 'pitr':
                    itr_dict.update({'proxy_itr_router':proxy_itr_router})
                elif proxy_type == 'petr':
                    etr_dict.update({'proxy_etr_router':proxy_itr_router})
                if group['proxy_itr_rloc']:
                    itr_dict.update({'proxy_itr_rloc':proxy_itr_rloc})
                continue

            # ITR local RLOC (last resort):             *** NOT FOUND ***
            m = p5.match(line)
            if m:
                group = m.groupdict()
                local_rloc_last_resort = group['local_rloc_last_resort']
                itr_dict.update({'local_rloc_last_resort':local_rloc_last_resort})
                continue

            # ITR use proxy ETR RLOC(s):           10.10.10.10
            m = p6.match(line)
            if m:
                group = m.groupdict()
                use_proxy_etr_rloc_val = [x.strip() for x in group['use_proxy_etr_rloc'].split(',')]
                proxy_list = itr_dict.setdefault('use_proxy_etr_rloc',[])
                for proxy in use_proxy_etr_rloc_val:
                    proxy_list.append(proxy)
                continue

            # ITR Solicit Map Request (SMR):       accept and process
            m = p7.match(line)
            if m:
                group = m.groupdict()
                solicit_map_request = group['solicit_map_request'].strip()
                itr_dict.update({'solicit_map_request':solicit_map_request})
                continue

            # Max SMRs per map-cache entry:      8 more specifics
            m = p8.match(line)
            if m:
                group = m.groupdict()
                max_smr_per_map_cache = group['max_smr_per_map_cache']
                itr_dict.update({'max_smr_per_map_cache':max_smr_per_map_cache})
                continue

            # Multiple SMR suppression time:     20 secs
            m = p9.match(line)
            if m:
                group = m.groupdict()
                multiple_smr_supression_time = int(group['multiple_smr_supression_time'])
                itr_dict.update({'multiple_smr_supression_time':multiple_smr_supression_time})
                continue

            # ETR accept mapping data:             disabled, verify disabled
            m = p10.match(line)
            if m:
                group = m.groupdict()
                accept_mapping_data = group['accept_mapping_data']
                etr_dict.update({'accept_mapping_data':accept_mapping_data})
                continue

            # ETR map-cache TTL:                   1d00h
            m = p11.match(line)
            if m:
                group = m.groupdict()
                map_cache_ttl = group['map_cache_ttl']
                etr_dict.update({'map_cache_ttl':map_cache_ttl})
                continue

            # NAT-traversal Router (NAT-RTR):      disabled
            m = p12.match(line)
            if m:
                group = m.groupdict()
                nat_traversal_router_val = group['nat_traversal_router']
                nat_traversal_router = bool(re.search('enabled',nat_traversal_router_val))
                lisp_dict.update({'nat_traversal_router':nat_traversal_router})
                continue

            # Mobility First-Hop Router:           disabled
            m = p13.match(line)
            if m:
                group = m.groupdict()
                mobility_first_hop_router = group['mobility_first_hop_router']
                lisp_dict.update({'mobility_first_hop_router':mobility_first_hop_router})
                continue

            # Map Server (MS):                     disabled
            m = p14.match(line)
            if m:
                group = m.groupdict()
                enabled_val = group['enabled']
                enabled = bool(re.search('enabled',enabled_val))
                map_server_dict = lisp_dict.setdefault('map_server',{})
                map_server_dict.update({'enabled':enabled})
                continue

            # Map Resolver (MR):                   disabled
            m = p15.match(line)
            if m:
                group = m.groupdict()
                enabled_val = group['enabled']
                enabled = bool(re.search('enabled',enabled_val))
                map_resolver_dict = lisp_dict.setdefault('map_resolver',{})
                map_resolver_dict.update({'enabled':enabled})
                continue

            # Delegated Database Tree (DDT):       disabled
            m = p16.match(line)
            if m:
                group = m.groupdict()
                delegated_database_tree = group['delegated_database_tree']
                lisp_dict.update({'delegated_database_tree':delegated_database_tree})
                continue

            # Mr-use-petr:                              enabled
            m = p17.match(line)
            if m:
                group = m.groupdict()
                role = group['role']
                mr_dict = lisp_dict.setdefault('mr_use_petr',{})
                mr_dict.update({'role':role})
                continue

            # Mr-use-petr locator set name:             RLOC1
            m = p18.match(line)
            if m:
                group = m.groupdict()
                locator_set = group['locator_set']
                mr_dict.update({'locator_set':locator_set})
                continue

            # First-Packet pETR:                        enabled
            m = p19.match(line)
            if m:
                group = m.groupdict()
                role = group['role']
                first_dict = lisp_dict.setdefault('first_packet_petr',{})
                first_dict.update({'role':role})
                continue

            # First-Packet pETR locator set name:       RLOC1
            m = p20.match(line)
            if m:
                group = m.groupdict()
                locator_set = group['locator_set']
                first_dict.update({'locator_set':locator_set})
                continue

            # Multiple IP per MAC support:              disabled
            m = p21.match(line)
            if m:
                group = m.groupdict()
                multiple_ip_per_mac_val = group['multiple_ip_per_mac']
                multiple_ip_per_mac = bool(re.search('enabled',multiple_ip_per_mac_val))
                lisp_dict.update({'multiple_ip_per_mac':multiple_ip_per_mac})
                continue

            # Multicast Flood Access-Tunnel:            disabled
            m = p22.match(line)
            if m:
                group = m.groupdict()
                mcast_flood_access_tunnel_val = group['mcast_flood_access_tunnel']
                mcast_flood_access_tunnel = bool(re.search('enabled',mcast_flood_access_tunnel_val))
                lisp_dict.update({'mcast_flood_access_tunnel':mcast_flood_access_tunnel})
                continue

            # Publication-Subscription:                 enabled
            m = p23.match(line)
            if m:
                group = m.groupdict()
                role_val = group['role']
                role = bool(re.search('enabled',role_val))
                pub_sub_dict = lisp_dict.setdefault('pub_sub',{})
                pub_sub_dict.update({'role':role})
                continue

            # Publisher(s):                           *** NOT FOUND ***
            m = p24.match(line)
            if m:
                group = m.groupdict()
                publishers = group['publishers'].split(',')
                publishers_list = pub_sub_dict.setdefault('publishers',[])
                for publish in publishers:
                    publishers_list.append(publish)
                    val = "publishers_list"

            # Subscriber(s):                           *** NOT FOUND ***
            m = p25.match(line)
            if m:
                group = m.groupdict()
                subscribers = group['subscribers'].split(',')
                subscribers_list = pub_sub_dict.setdefault('subscribers',[])
                for subscribe in subscribers:
                    subscribers_list.append(subscribe)
                    val = "subscribers_list"

            # ITR Map-Resolver(s):                 10.64.4.4, 10.166.13.13
            m = p26.match(line)
            if m:
                map_resolvers = m.groupdict()['mr_address'].split(',')
                for ms in map_resolvers:
                    try:
                        map_resolver, uptime = ms.split()
                        map_resolver = map_resolver.replace(' ', '')
                    except:
                        map_resolver = ms.replace(' ', '')
                    # Set etr_dict under service
                    etr_mr_dict = lisp_dict.setdefault('map_resolvers', {}).\
                                    setdefault(map_resolver, {})
                    etr_mr_dict.update({'mr_address':map_resolver})
                    val = "etr_mr_dict"
                continue

            #                                  10.84.66.66 (never)
            m = p26_1.match(line)
            if m:
                group = m.groupdict()
                prefix_list = group['prefix_list']
                if val == "publishers_list":
                    publishers_list.append(prefix_list)
                elif val == "subscribers_list":
                    subscribers_list.append(prefix_list)
                elif val == "etr_mr_dict":
                    etr_mr_dict.update({'prefix_list':prefix_list})
                elif val == "etr_ms_dict":
                    etr_ms_dict.update({'prefix_list':prefix_list})
                continue

            # ETR Map-Server(s):                   10.64.4.4 (17:49:58), 10.166.13.13 (00:00:35)
            m = p27.match(line)
            if m:
                map_servers = m.groupdict()['ms_address'].split(',')
                for ms in map_servers:
                    try:
                        map_server, uptime = ms.split()
                        map_server = map_server.replace(' ', '')
                    except:
                        map_server = ms.replace(' ', '')
                    # Set etr_dict under service
                    etr_ms_dict = lisp_dict.setdefault('mapping_servers', {}).\
                                    setdefault(map_server, {})
                    etr_ms_dict.update({'ms_address':map_server})
                    val = "etr_ms_dict"
                continue

            # xTR-ID:                              0x730E0861-0x12996F6D-0xEFEA2114-0xE1C951F7
            m = p28.match(line)
            if m:
                group = m.groupdict()
                xtr_id = group['xtr_id']
                lisp_dict.update({'xtr_id':xtr_id})
                continue

            # site-ID:                             unspecified
            m = p29.match(line)
            if m:
                group = m.groupdict()
                site_id = group['site_id']
                lisp_dict.update({'site_id':site_id})
                continue

            # RLOC-probe algorithm:              disabled
            m = p30.match(line)
            if m:
                group = m.groupdict()
                rloc_probe_algorithm = group['rloc_probe_algorithm']
                locator_dict = lisp_dict.setdefault('locator_status_algorithms',{})
                locator_dict.update({'rloc_probe_algorithm':rloc_probe_algorithm})
                continue

            # RLOC-probe on route change:        N/A (periodic probing disabled)
            m = p31.match(line)
            if m:
                group = m.groupdict()
                rloc_probe_on_route_change_val = group['rloc_probe_on_route_change']
                rloc_probe_on_route_change = bool(re.search('enabled',rloc_probe_on_route_change_val))
                locator_dict.update({'rloc_probe_on_route_change':rloc_probe_on_route_change})
                continue

            # RLOC-probe on member change:       disabled
            m = p32.match(line)
            if m:
                group = m.groupdict()
                rloc_probe_member_change = group['rloc_probe_member_change']
                locator_dict.update({'rloc_probe_member_change':rloc_probe_member_change})
                continue

            # LSB reports:                       process
            m = p33.match(line)
            if m:
                group = m.groupdict()
                lsb_reports = group['lsb_reports']
                locator_dict.update({'lsb_reports':lsb_reports})
                continue

            # IPv4 RLOC minimum mask length:     /0
            m = p34.match(line)
            if m:
                group = m.groupdict()
                ipv4_rloc_min_mask_len = int(group['ipv4_rloc_min_mask_len'])
                locator_dict.update({'ipv4_rloc_min_mask_len':ipv4_rloc_min_mask_len})
                continue

            # IPv6 RLOC minimum mask length:     /0
            m = p35.match(line)
            if m:
                group = m.groupdict()
                ipv6_rloc_min_mask_len = int(group['ipv6_rloc_min_mask_len'])
                locator_dict.update({'ipv6_rloc_min_mask_len':ipv6_rloc_min_mask_len})
                continue

            # Map-cache limit:                   5120
            m = p36.match(line)
            if m:
                group = m.groupdict()
                limit = int(group['limit'])
                map_cache_dict = lisp_dict.setdefault('map_cache',{})
                map_cache_dict.update({'limit':limit})
                continue

            # Map-cache activity check period:   60 secs
            m = p37.match(line)
            if m:
                group = m.groupdict()
                activity_check_period = int(group['activity_check_period'])
                map_cache_dict.update({'activity_check_period':activity_check_period})
                continue

            # Persistent map-cache:              disabled
            m = p38.match(line)
            if m:
                group = m.groupdict()
                persistent = group['persistent']
                map_cache_dict.update({'persistent':persistent})
                continue

            # Dynamic database mapping limit:    5120
            m = p39.match(line)
            if m:
                group = m.groupdict()
                dynamic_database_limit = int(group['dynamic_database_limit'])
                dynamic_dict = lisp_dict.setdefault('database',{})
                dynamic_dict.update({'dynamic_database_limit':dynamic_database_limit})
                continue

            # Vlan100: 10.229.11.1 (Loopback0)
            m = p40.match(line)
            if m:
                group = m.groupdict()
                vlans = group['vlans']
                address = group['address']
                interface = group['interface']
                source_dict = lisp_dict.setdefault('source_locator_configuration',{}).\
                                setdefault('vlans',{}).\
                                setdefault(vlans,{})
                source_dict.update({'address':address,
                                    'interface':interface})
                continue
        return ret_dict


# ========================================================================
# Schema for 'show lisp all instance-id <instance_id> <service> map-cache'
# ========================================================================
class ShowLispServiceMapCacheSchema(MetaParser):

    '''Schema for "show lisp all instance-id <instance_id> <service> map-cache" '''

    schema = {
        'lisp_router_instances':
            {Any():
                {'lisp_router_instance_id': int,
                Optional('service'):
                    {Any():
                        {'service': str,
                        'itr':
                            {'map_cache':
                                {Any():
                                    {'vni': str,
                                    'entries': int,
                                    'mappings':
                                        {Any():
                                            {'id': str,
                                            'creation_time': str,
                                            'time_to_live': str,
                                            'via': str,
                                            'eid':
                                                {'address_type': str,
                                                'vrf': str,
                                                Optional('ipv4'):
                                                    {'ipv4': str,
                                                    },
                                                Optional('ipv4_prefix'):
                                                    {'ipv4_prefix': str,
                                                    },
                                                Optional('ipv6'):
                                                    {'ipv6': str,
                                                    },
                                                Optional('ipv6_prefix'):
                                                    {'ipv6_prefix': str,
                                                    },
                                                },
                                            Optional('negative_mapping'):
                                                {'map_reply_action': str,
                                                },
                                            Optional('sgt'): str,
                                            Optional('encap_to_petr'): bool,
                                            Optional('encap_to_petr_iid'): str,
                                            Optional('positive_mapping'):
                                                {'rlocs':
                                                    {Any():
                                                        {'id': str,
                                                        'uptime': str,
                                                        'state': str,
                                                        'priority': int,
                                                        'weight': int,
                                                        Optional('encap_iid'): str,
                                                        'locator_address':
                                                            {'address_type': str,
                                                            'virtual_network_id': str,
                                                            Optional('ipv4'):
                                                                {'ipv4': str,
                                                                },
                                                            Optional('ipv4_prefix'):
                                                                {'ipv4_prefix': str,
                                                                },
                                                            Optional('ipv6'):
                                                                {'ipv6': str,
                                                                },
                                                            Optional('ipv6_prefix'):
                                                                {'ipv6_prefix': str,
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        }


# ========================================================================
# Parser for 'show lisp all instance-id <instance_id> <service> map-cache'
# ========================================================================
class ShowLispServiceMapCache(ShowLispServiceMapCacheSchema):

    '''Parser for "show lisp all instance-id <instance_id> <service> map-cache"'''

    cli_command = 'show lisp all instance-id {instance_id} {service} map-cache'
    exclude = ['creation_time']

    def cli(self, service, instance_id, output=None):

        if output is None:
            assert service in ['ipv4', 'ipv6', 'ethernet']
            out = self.device.execute(self.cli_command.format(instance_id=instance_id,service=service))
        else:
            out = output

        # Init vars
        parsed_dict = {}

        # State dict
        state_dict = {
            'disabled': False,
            'enabled': True}

        # Output for router lisp 0
        # Output for router lisp 0 instance-id 193
        p1 = re.compile(r'Output +for +router +lisp +(?P<router_id>(\S+))'
                         '(?: +instance-id +(?P<instance_id>(\d+)))?$')

        # LISP IPv4 Mapping Cache for EID-table default (IID 101), 2 entries
        # LISP IPv6 Mapping Cache for EID-table vrf red (IID 101), 2 entries
        # LISP MAC Mapping Cache for EID-table Vlan 101 (IID 1), 4 entries
        # LISP IPv4 Mapping Cache for LISP 0 EID-table default (IID 4097), 2 entries
        p2 = re.compile(r'LISP +(?P<type>(IPv4|IPv6|MAC)) +Mapping +Cache +for'
                         ' ((LISP\s*[\d. ]+)|\s*)+EID\-table +(default|(vrf|Vlan)'
                         ' +(?P<vrf>(\S+))) +\(IID +(?P<iid>(\d+))\), +(?P<entries>(\d+))'
                         ' +entries$')

        # 0.0.0.0/0, uptime: 15:23:50, expires: never, via static-send-map-request
        # ::/0, uptime: 00:11:28, expires: never, via static-send-map-request
        # b827.ebff.4720/48, uptime: 22:49:42, expires: 01:10:17, via WLC Map-Notify, complete
        # 192.168.9.0/24, uptime: 00:04:02, expires: 23:55:57, via map-reply, complete
        p3 = re.compile(r'(?P<map_id>(\S+)), +uptime: +(?P<uptime>(\S+)),'
                         ' +expires: +(?P<expires>(\S+)), +via +(?P<via>(.*))$')

        #   Negative cache entry, action: send-map-request
        p4 = re.compile(r'Negative +cache +entry, +action: +(?P<action>(.*))$')

        #   Locator  Uptime    State      Pri/Wgt     Encap-IID
        #   10.1.8.8 00:04:02  up          50/50        -
        # State can be: 'up', 'down', 'route-rejec', 'up, self' and etc
        p5 = re.compile(r'(?P<locator>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|([a-fA-F\d\:]+)) +(?P<uptime>(\S+))'
                         ' +(?P<state>(\S+|up, self))'
                         ' +(?P<priority>(\d+))\/(?P<weight>(\d+))'
                         '(?: +(?P<encap_iid>(\S+)))?$')

        # Encapsulating to proxy ETR
        # Encapsulating to proxy ETR Encap-IID 3
        p6 = re.compile(r'Encapsulating\s+to\s+proxy\s+ETR(\s+Encap-IID\s+(?P<encap_to_petr_iid>\S+))?$')

        # SGT: 3003, software only
        p7 = re.compile(r'SGT:\s+(?P<sgt>[-\w]+)')

        for line in out.splitlines():
            line = line.strip()

            # Output for router lisp 0
            # Output for router lisp 0 instance-id 193
            m = p1.match(line)
            if m:
                group = m.groupdict()
                lisp_router_id = int(group['router_id'])
                lisp_dict = parsed_dict.setdefault('lisp_router_instances', {}).\
                            setdefault(lisp_router_id, {})
                lisp_dict['lisp_router_instance_id'] = lisp_router_id
                if group['instance_id']:
                    instance_id = group['instance_id']
                continue

            # LISP IPv4 Mapping Cache for EID-table default (IID 101), 2 entries
            # LISP IPv6 Mapping Cache for EID-table vrf red (IID 101), 2 entries
            # LISP MAC Mapping Cache for EID-table Vlan 101 (IID 1), 4 entries
            m = p2.match(line)
            if m:
                group = m.groupdict()
                address_type = group['type']
                vrf_name = group['vrf'] if group['vrf'] else 'default'
                # Create dict
                service_dict = lisp_dict.setdefault('service', {}).\
                                setdefault(service, {})
                service_dict['service'] = service
                itr_dict = service_dict.setdefault('itr', {})
                map_cache_dict = itr_dict.setdefault('map_cache', {}).\
                                    setdefault(instance_id, {})
                map_cache_dict['vni'] = str(instance_id)
                map_cache_dict['entries'] = int(group['entries'])
                continue

            # # 0.0.0.0/0, uptime: 15:23:50, expires: never, via static-send-map-request
            # ::/0, uptime: 00:11:28, expires: never, via static-send-map-request
            # b827.ebff.4720/48, uptime: 22:49:42, expires: 01:10:17, via WLC Map-Notify, complete
            # 192.168.9.0/24, uptime: 00:04:02, expires: 23:55:57, via map-reply, complete
            m = p3.match(line)
            if m:
                # reset rloc counter
                rloc_id = 1
                group = m.groupdict()
                mapping_dict = map_cache_dict.\
                                setdefault('mappings', {}).\
                                setdefault(group['map_id'], {})
                mapping_dict['id'] = group['map_id']
                mapping_dict['creation_time'] = group['uptime']
                mapping_dict['time_to_live'] = group['expires']
                mapping_dict['via'] = group['via']
                eid_dict = mapping_dict.setdefault('eid', {})
                if ':' in group['map_id']:
                    ipv6_dict = eid_dict.setdefault('ipv6', {})
                    ipv6_dict['ipv6'] = group['map_id']
                    eid_dict['address_type'] = 'ipv6-afi'
                else:
                    ipv4_dict = eid_dict.setdefault('ipv4', {})
                    ipv4_dict['ipv4'] = group['map_id']
                    eid_dict['address_type'] = 'ipv4-afi'
                try:
                    eid_dict['vrf'] = vrf_name
                except:
                    pass

            #   Negative cache entry, action: send-map-request
            m = p4.match(line)
            if m:
                neg_dict = mapping_dict.setdefault('negative_mapping', {})
                neg_dict['map_reply_action'] = m.groupdict()['action']
                continue

            #  Locator  Uptime    State      Pri/Wgt     Encap-IID
            #  10.1.8.8 00:04:02  up          50/50        -
            m = p5.match(line)
            if m:
                group = m.groupdict()
                # positive_mapping
                postive_dict = mapping_dict.\
                                setdefault('positive_mapping', {}).\
                                setdefault('rlocs', {}).\
                                setdefault(rloc_id, {})
                postive_dict['id'] = str(rloc_id)
                postive_dict['uptime'] = group['uptime']
                postive_dict['state'] = group['state']
                postive_dict['priority'] = int(group['priority'])
                postive_dict['weight'] = int(group['weight'])
                if group['encap_iid']:
                    postive_dict['encap_iid'] = group['encap_iid']
                # locator_address
                locator_dict = postive_dict.setdefault('locator_address', {})
                locator_dict['virtual_network_id'] = str(instance_id)
                if ':' in group['locator']:
                    ipv6_dict = locator_dict.setdefault('ipv6', {})
                    ipv6_dict['ipv6'] = group['locator']
                    locator_dict['address_type'] = 'ipv6-afi'
                else:
                    ipv4_dict = locator_dict.setdefault('ipv4', {})
                    ipv4_dict['ipv4'] = group['locator']
                    locator_dict['address_type'] = 'ipv4-afi'
                # Increment entry
                rloc_id += 1
                continue

            # Encapsulating to proxy ETR
            # Encapsulating to proxy ETR Encap-IID 3
            m = p6.match(line)
            if m:
                mapping_dict['encap_to_petr'] = True
                encap_to_petr_iid = m.groupdict()['encap_to_petr_iid']
                if encap_to_petr_iid:
                    mapping_dict['encap_to_petr_iid'] = encap_to_petr_iid
                continue
            m= p7.match(line)
            if m:
                sgt = m.groupdict()['sgt']
                if sgt:
                    mapping_dict['sgt'] = sgt
                continue

        return parsed_dict


# ===========================================================================
# Schema for 'show lisp all instance-id <instance_id> <service> rloc members'
# ===========================================================================
class ShowLispServiceRlocMembersSchema(MetaParser):

    '''Schema for "show lisp all instance-id <instance_id> <service> rloc members" '''

    schema = {
        'lisp_router_instances':
            {Any():
                {'lisp_router_instance_id': int,
                Optional('service'):
                    {Optional(Any()):
                        {'instance_id':
                            {Any():
                                {Optional('rloc'):
                                    {'total_entries': int,
                                    'valid_entries': int,
                                    'distribution': bool,
                                    Optional('members'):
                                        {Any():
                                            {
                                                'origin': str,
                                                'valid': str,
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


# ===========================================================================
# Parser for 'show lisp all instance-id <instance_id> <service> rloc members'
# ===========================================================================
class ShowLispServiceRlocMembers(ShowLispServiceRlocMembersSchema):

    '''Parser for "show lisp all instance-id <instance_id> <service> server rloc members"'''

    cli_command = ['show lisp all instance-id {instance_id} service {service} rloc members',
                   'show lisp all instance-id {instance_id} {service} server rloc members']

    def cli(self, service, instance_id, output=None):

        if output is None:
            assert service in ['ipv4', 'ipv6', 'ethernet']
            out = self.device.execute(self.cli_command[1].format(instance_id=instance_id, service=service))
        else:
            out = output

        # Init vars
        parsed_dict = {}

        # State dict
        state_dict = {
            'disabled': False,
            'enabled': True}

        # Output for router lisp 0
        # Output for router lisp 0 instance-id 193
        # Output for router lisp 2 instance-id 101
        p1 = re.compile(r'Output +for +router +lisp +(?P<router_id>(\S+))'
                         '(?: +instance-id +(?P<instance_id>(\d+)))?$')

        # LISP RLOC Membership for router lisp 0 IID 101
        p2 = re.compile(r'LISP +RLOC +Membership +for +router +lisp'
                         ' +(?P<router_id>(\S+)) +IID +(?P<instance_id>(\d+))$')

        # Entries: 2 valid / 2 total, Distribution disabled
        p3 = re.compile(r'Entries: +(?P<valid>(\d+)) +valid +\/'
                         ' +(?P<total>(\d+)) +total, +Distribution'
                         ' +(?P<distribution>(enabled|disabled))$')

        # RLOC                    Origin                       Valid
        # 10.16.2.2               Registration                 Yes
        # 10:16:2:2::             Registration                 Yes
        p4 = re.compile(r'(?P<member>([\d\.]+)|([a-fA-F\d\:]+)) +(?P<origin>(\S+))'
                        r' +(?P<valid>(\S+))$')

        for line in out.splitlines():
            line = line.strip()

            # Output for router lisp 0
            # Output for router lisp 0 instance-id 193
            m = p1.match(line)
            if m:
                group = m.groupdict()
                lisp_router_id = int(group['router_id'])
                if group['instance_id']:
                    instance_id = group['instance_id']
                # Create lisp_dict
                lisp_dict = parsed_dict.setdefault('lisp_router_instances', {}).\
                            setdefault(lisp_router_id, {})
                lisp_dict['lisp_router_instance_id'] = lisp_router_id
                # Create service_dict
                iid_dict = lisp_dict.setdefault('service', {}).\
                            setdefault(service, {}).\
                            setdefault('instance_id', {}).\
                            setdefault(str(instance_id), {})
                continue

            # Entries: 2 valid / 2 total, Distribution disabled
            m = p3.match(line)
            if m:
                group = m.groupdict()
                # Create rloc_dict
                rloc_dict = iid_dict.setdefault('rloc', {})
                rloc_dict['valid_entries'] = int(group['valid'])
                rloc_dict['total_entries'] = int(group['total'])
                rloc_dict['distribution'] = state_dict[group['distribution']]
                continue

            # RLOC                    Origin                       Valid
            # 10.16.2.2               Registration                 Yes
            # 10:16:2:2::             Registration                 Yes
            m = p4.match(line)
            if m:
                group = m.groupdict()
                members_dict = rloc_dict.setdefault('members', {}).\
                                setdefault(group['member'], {})
                members_dict['origin'] = group['origin'].lower()
                members_dict['valid'] = group['valid'].lower()
                continue

        return parsed_dict


# ==================================================================
# Schema for 'show lisp all instance-id <instance_id> <service> smr'
# ==================================================================
class ShowLispServiceSmrSchema(MetaParser):

    '''Schema for "show lisp all instance-id <instance_id> <service> smr" '''

    schema = {
        'lisp_router_instances':
            {Any():
                {'lisp_router_instance_id': int,
                Optional('service'):
                    {Optional(Any()):
                        {'instance_id':
                            {Any():
                                {Optional('smr'):
                                    {'vrf': str,
                                    'entries': int,
                                    Optional('prefixes'):
                                        {Any():
                                            {'producer': str,
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        }


# ==================================================================
# Parser for 'show lisp all instance-id <instance_id> <service> smr'
# ==================================================================
class ShowLispServiceSmr(ShowLispServiceSmrSchema):

    '''Parser for "show lisp all instance-id <instance_id> <service> smr"'''

    cli_command = ['show lisp all instance-id {instance_id} service {service} smr',
                   'show lisp all instance-id {instance_id} {service} smr']

    def cli(self, service, instance_id, output=None):

        if output is None:
            assert service in ['ipv4', 'ipv6', 'ethernet']
            out = self.device.execute(self.cli_command[1].format(instance_id=instance_id, service=service))
        else:
            out = output

        # Init vars
        parsed_dict = {}

        # State dict
        state_dict = {
            'disabled': False,
            'enabled': True}

        # Output for router lisp 0
        # Output for router lisp 0 instance-id 193
        # Output for router lisp 2 instance-id 101
        p1 = re.compile(r'Output +for +router +lisp +(?P<router_id>(\S+))'
                         '(?: +instance-id +(?P<instance_id>(\d+)))?$')

        # LISP SMR Table for router lisp 0 (red) IID 101
        p2 = re.compile(r'LISP +SMR +Table +for +router +lisp +(\d+)'
                         ' +\((?P<vrf>(\S+))\) +IID +(?P<instance_id>(\S+))$')

        # Entries: 1
        p3 = re.compile(r'Entries: +(?P<entries>(\d+))$')

        # Prefix                                  Producer
        # 192.168.0.0/24                          local EID
        # 192:168:0:0::/64                        local EID
        p4 = re.compile(r'(?P<prefix>([\d\.\/]+)|([a-fA-F\d\:]+\/\d{1,3})) +(?P<producer>(.*))$')

        for line in out.splitlines():
            line = line.strip()

            # Output for router lisp 0
            # Output for router lisp 0 instance-id 193
            m = p1.match(line)
            if m:
                group = m.groupdict()
                lisp_router_id = int(group['router_id'])
                if group['instance_id']:
                    instance_id = group['instance_id']
                # Create lisp_dict
                lisp_dict = parsed_dict.setdefault('lisp_router_instances', {}).\
                            setdefault(lisp_router_id, {})
                lisp_dict['lisp_router_instance_id'] = lisp_router_id
                # Create service_dict
                smr_dict = lisp_dict.setdefault('service', {}).\
                            setdefault(service, {}).\
                            setdefault('instance_id', {}).\
                            setdefault(str(instance_id), {}).\
                            setdefault('smr', {})
                continue

            # LISP SMR Table for router lisp 0 (red) IID 101
            m = p2.match(line)
            if m:
                smr_dict['vrf'] = m.groupdict()['vrf']
                continue

            # Entries: 1
            m = p3.match(line)
            if m:
                smr_dict['entries'] = int(m.groupdict()['entries'])
                continue

            # Prefix                                  Producer
            # 192.168.0.0/24                          local EID
            # 192:168:0:0::/64                        local EID
            m = p4.match(line)
            if m:
                prefix_dict = smr_dict.setdefault('prefixes', {}).\
                                        setdefault(m.groupdict()['prefix'], {})
                prefix_dict['producer'] = m.groupdict()['producer']
                continue

        return parsed_dict


# ====================================================
# Schema for 'show lisp all service <service> summary'
# ====================================================
class ShowLispServiceSummarySchema(MetaParser):

    '''Schema for "show lisp all <service> summary" '''

    schema = {
        'lisp_router_instances':
            {Any():
                {'lisp_router_instance_id': int,
                Optional('service'):
                    {Optional(Any()):
                        {Optional('virtual_network_ids'):
                            {Any():
                                {Optional('vrf'): str,
                                'interface': str,
                                'db_size': int,
                                'db_no_route': int,
                                Optional('rloc_status'): str,
                                'cache_size': int,
                                'incomplete': str,
                                'cache_idle': str,
                                'lisp_role':
                                    {Any():
                                        {'lisp_role_type': str,
                                        },
                                    },
                                },
                            },
                        'etr':
                            {'summary':
                                {'instance_count': int,
                                'total_eid_tables': int,
                                'total_db_entries': int,
                                'total_db_entries_inactive': int,
                                Optional('maximum_db_entries'): int,
                                'total_map_cache_entries': int,
                                Optional('maximum_map_cache_entries'): int,
                                'eid_tables_inconsistent_locators': int,
                                'eid_tables_incomplete_map_cache_entries': int,
                                'eid_tables_pending_map_cache_update_to_fib': int,
                                },
                            },
                        },
                    },
                },
            },
        }


# ====================================================
# Parser for 'show lisp all service <service> summary'
# ====================================================
class ShowLispServiceSummary(ShowLispServiceSummarySchema):

    ''' Parser for:
        * show lisp service {service} summary
        * show lisp {lisp_id} service {service} summary
        * show lisp locator-table {locator_table} service {service} summary
        * show lisp locator-table vrf {rloc_vrf} service {service} summary
    '''

    cli_command = ['show lisp service {service} summary',
                   'show lisp {lisp_id} service {service} summary',
                   'show lisp locator-table {locator_table} service {service} summary',
                   'show lisp locator-table vrf {vrf} service {service} summary']

    def cli(self, service, lisp_id=None, locator_table=None, vrf=None, output=None):

        if output is None:
            assert service in ['ipv4', 'ipv6', 'ethernet']
            if lisp_id:
                cmd = self.cli_command[1].format(lisp_id=lisp_id, service=service)
            elif locator_table:
                cmd = self.cli_command[2].format(vrf=vrf, service=service)
            elif vrf:
                cmd = self.cli_command[3].format(locator_table=locator_table, service=service)
            else:
                cmd = self.cli_command[0].format(service=service)
            out = self.device.execute(cmd)
        else:
            out = output

        # Init vars
        parsed_dict = {}

        # Output for router lisp 0
        p1 = re.compile(r'Output +for +router +lisp +(?P<router_id>(\S+))$')

        # Router-lisp ID:   0
        p2 = re.compile(r'Router-lisp +ID: +(?P<router_id>(\S+))$')

        # Instance count:   2
        p3 = re.compile(r'Instance +count: +(?P<val>(\d+))$')

        # Key: DB - Local EID Database entry count (@ - RLOC check pending
        #                                   * - RLOC consistency problem),
        # DB no route - Local EID DB entries with no matching RIB route,
        # Cache - Remote EID mapping cache size, IID - Instance ID,
        # Role - Configured Role

        #                       Interface    DB  DB no  Cache  Incom  Cache
        # EID VRF name             (.IID)  size  route   size  plete  Idle  Role
        # red                   LISP0.101     1      0      2   0.0%  0.0%  ITR-ETR
        # blue                  LISP0.102     1      0      1   0.0%    0%  ITR-ETR
        # blue                  LISP0.102     1@     0      1   0.0%    0%  ITR-ETR
        # blue                  LISP0.102     1*     0      1   0.0%    0%  ITR-ETR
        p4_1 = re.compile(r'(?P<vrf>(\S+)) +(?P<interface>(\S+))\.(?P<iid>(\d+))'
                          r' +(?P<db_size>(\d+))(?P<rloc_status>(\W))? +(?P<db_no_route>(\d+))'
                          r' +(?P<cache_size>(\d+)) +(?P<incomplete>(\S+))'
                          r' +(?P<cache_idle>(\S+)) +(?P<role>(\S+))$')

        p4_2 = re.compile(r'(?P<interface>(\S+))\.(?P<iid>(\d+))'
                          r' +(?P<db_size>(\d+))(?P<rloc_status>(\W))? +(?P<db_no_route>(\d+))'
                          r' +(?P<cache_size>(\d+)) +(?P<incomplete>(\S+))'
                          r' +(?P<cache_idle>(\S+)) +(?P<role>(\S+))$')

        # Number of eid-tables:                                 2
        p5 = re.compile(r'Number +of +eid-tables: +(?P<val>(\d+))$')

        # Total number of database entries:                     2 (inactive 0)
        p6 = re.compile(r'Total +number +of +database +entries:'
                        r' +(?P<val>(\d+))(?: +\(inactive'
                        r' +(?P<inactive>(\d+))\))?$')

        # EID-tables with inconsistent locators:                0
        p7 = re.compile(r'EID-tables +with +inconsistent +locators:'
                        r' +(?P<val>(\d+))$')

        # Total number of map-cache entries:                    3
        p8 = re.compile(r'Total +number +of +map-cache +entries:'
                        r' +(?P<val>(\d+))$')

        # EID-tables with incomplete map-cache entries:         0
        p9 = re.compile(r'EID-tables +with +incomplete +map-cache +entries:'
                        r' +(?P<val>(\d+))$')

        # EID-tables pending map-cache update to FIB:           0
        p10 = re.compile(r'EID-tables +pending +map-cache +update +to +FIB:'
                         r' +(?P<val>(\d+))$')

        # Maximum database entries:                        123456
        p11 = re.compile(r'^Maximum database entries: +(?P<maximum_db_entries>\d+)$')

        # Maximum map-cache entries:                       654321
        p12 = re.compile(r'Maximum map-cache entries: +(?P<maximum_map_cache_entries>\d+)$')

        lisp_router_id = None
        for line in out.splitlines():
            line = line.strip()

            # Output for router lisp 0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                lisp_router_id = int(group['router_id'])
                continue

            # Router-lisp ID:   0
            m = p2.match(line)
            if m:
                if lisp_router_id:
                    if int(m.groupdict()['router_id']) == lisp_router_id:
                        # Create lisp_dict
                        lisp_dict = parsed_dict.\
                                    setdefault('lisp_router_instances', {}).\
                                    setdefault(lisp_router_id, {})
                        lisp_dict['lisp_router_instance_id'] = lisp_router_id
                        # Create summary dict
                        sum_dict = lisp_dict.setdefault('service', {}).\
                                        setdefault(service, {}).\
                                        setdefault('etr', {}).\
                                        setdefault('summary', {})
                else:
                    lisp_router_id = int(m.groupdict()['router_id'])
                    # Create lisp_dict
                    lisp_dict = parsed_dict. \
                        setdefault('lisp_router_instances', {}). \
                        setdefault(lisp_router_id, {})
                    lisp_dict['lisp_router_instance_id'] = lisp_router_id
                    # Create summary dict
                    sum_dict = lisp_dict.setdefault('service', {}). \
                        setdefault(service, {}). \
                        setdefault('etr', {}). \
                        setdefault('summary', {})
                continue

            # Instance count:   2
            m = p3.match(line)
            if m:
                sum_dict['instance_count'] = int(m.groupdict()['val'])
                continue

            # blue              LISP0.102  1      0      1  0.0%    0%  ITR-ETR
            #                   LISP0.2    2      0      0    0%    0%  NONE
            m1 = p4_1.match(line)
            m2 = p4_2.match(line)
            m = m1 if m1 else m2
            if m:
                group = m.groupdict()
                vni_dict = lisp_dict.setdefault('service', {}).\
                            setdefault(service, {}).\
                            setdefault('virtual_network_ids', {}).\
                            setdefault(group['iid'], {})
                vni_dict['interface'] = group['interface'] + '.' + group['iid']
                vni_dict['db_size'] = int(group['db_size'])
                if group['rloc_status']!=' ':
                    vni_dict['rloc_status'] = group['rloc_status']
                vni_dict['db_no_route'] = int(group['db_no_route'])
                vni_dict['cache_size'] = int(group['cache_size'])
                vni_dict['incomplete'] = group['incomplete']
                vni_dict['cache_idle'] = group['cache_idle']
                role_dict = vni_dict.setdefault('lisp_role', {}).\
                                setdefault(group['role'].lower(), {})
                role_dict['lisp_role_type'] = group['role'].lower()
                if 'vrf' in group:
                    vni_dict['vrf'] = group['vrf']
                continue

            # Number of eid-tables:                                 2
            m = p5.match(line)
            if m:
                sum_dict['total_eid_tables'] = int(m.groupdict()['val'])
                continue

            # Total number of database entries:                     2 (inactive 0)
            m = p6.match(line)
            if m:
                sum_dict['total_db_entries'] = int(m.groupdict()['val'])
                if m.groupdict()['inactive']:
                    sum_dict['total_db_entries_inactive'] = \
                        int(m.groupdict()['inactive'])
                continue

            # EID-tables with inconsistent locators:                0
            m = p7.match(line)
            if m:
                sum_dict['eid_tables_inconsistent_locators'] = \
                    int(m.groupdict()['val'])
                continue

            # Total number of map-cache entries:                    3
            m = p8.match(line)
            if m:
                sum_dict['total_map_cache_entries'] = int(m.groupdict()['val'])
                continue

            # EID-tables with incomplete map-cache entries:         0
            m = p9.match(line)
            if m:
                sum_dict['eid_tables_incomplete_map_cache_entries'] = \
                    int(m.groupdict()['val'])
                continue

            # EID-tables pending map-cache update to FIB:           0
            m = p10.match(line)
            if m:
                sum_dict['eid_tables_pending_map_cache_update_to_fib'] = \
                    int(m.groupdict()['val'])
                continue

            # Maximum database entries:                        123456
            m = p11.match(line)
            if m:
                sum_dict['maximum_db_entries'] = int(m.groupdict()['maximum_db_entries'])
                continue

            # Maximum map-cache entries:                       654321
            m = p12.match(line)
            if m:
                sum_dict['maximum_map_cache_entries'] = int(m.groupdict()['maximum_map_cache_entries'])
                continue

        return parsed_dict



# =======================================================================
# Parser for 'show lisp {lisp_id} instance-id <instance_id> <service> dabatase'
# =======================================================================
class ShowLispServiceDatabase(ShowLispDatabaseSuperParser):

    '''Parser for "show lisp {lisp_id} instance-id <instance_id> <service> dabatase"'''

    cli_command = ['show lisp instance-id {instance_id} {service} database',
                   'show lisp {lisp_id} instance-id {instance_id} {service} database',
                   'show lisp locator-table {locator_table} instance-id {instance_id} {service} database']

    def cli(self, service, instance_id, locator_table=None, lisp_id=None, output=None):
        
        if output is None:
            if locator_table and instance_id and service:
                output = self.device.execute(self.cli_command[2].\
                                            format(locator_table = locator_table,
                                                   instance_id=instance_id,
                                                   service=service))
            elif lisp_id and instance_id and service:
                output = self.device.execute(self.cli_command[1].\
                                            format(lisp_id = lisp_id,
                                                   instance_id=instance_id,
                                                   service=service))
            else:
                output = self.device.execute(self.cli_command[0].\
                                            format(instance_id=instance_id,
                                                   service=service),timeout=300)
        return super().cli(output=output)


class ShowLispEidTableServiceDatabase(ShowLispDatabaseSuperParser):

    '''Parser for "show lisp eid-table vrf {vrf} {service} database"'''

    cli_command = ['show lisp eid-table vrf {vrf} {service} database',
                   'show lisp eid-table {eid_table} {service} database']

    def cli(self, service, vrf=None, eid_table=None, output=None):
        if output is None:
            if eid_table and service:
                output = self.device.execute(self.cli_command[1].\
                                            format(eid_table = eid_table,
                                                   service=service),timeout=300)
            else:
                output = self.device.execute(self.cli_command[0].\
                                            format(vrf = vrf,
                                                   service=service),timeout=300)
        return super().cli(output=output)


# =============================================================================
# Schema for 'show lisp all instance-id <instance_id> <service> server summary'
# =============================================================================
class ShowLispServiceServerSummarySchema(MetaParser):

    '''Schema for "show lisp all instance-id <instance_id> <service> server summary" '''

    schema = {
        'lisp_router_instances':
            {Any():
                {'lisp_router_instance_id': int,
                'service':
                    {Any():
                        {'instance_id':
                            {Any():
                                {'map_server':
                                    {Optional('sites'):
                                        {Any():
                                            {'site_id': str,
                                            'configured': int,
                                            'registered': int,
                                            'inconsistent': int,
                                            },
                                        },
                                    'summary':
                                        {'number_configured_sites': int,
                                        'number_registered_sites':int,
                                        Optional('af_datum'):
                                            {Any():
                                                {'address_type': str,
                                                Optional('number_configured_eids'): int,
                                                Optional('number_registered_eids'): int,
                                                },
                                            },
                                        'sites_with_inconsistent_registrations': int,
                                        Optional('site_registration_limit'): int,
                                        Optional('site_registration_count'): int,
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        }


# =============================================================================
# Parser for 'show lisp all instance-id <instance_id> <service> server summary'
# =============================================================================
class ShowLispServiceServerSummary(ShowLispServiceServerSummarySchema):

    '''Parser for "show lisp all instance-id <instance_id> <service> server summary"'''

    cli_command = 'show lisp all instance-id {instance_id} {service} server summary'

    def cli(self, service, instance_id, output=None):
        if output is None:
            assert service in ['ipv4', 'ipv6', 'ethernet']
            out = self.device.execute(self.cli_command.format(instance_id=instance_id, service=service))
        else:
            out = output

        # Init vars
        parsed_dict = {}

        # Output for router lisp 0
        # Output for router lisp 0 instance-id 193
        # Output for router lisp 2 instance-id 101
        p1 = re.compile(r'Output +for +router +lisp +(?P<router_id>(\S+))'
                         '(?: +instance-id +(?P<instance_id>(\d+)))?$')

        #                      -----------  IPv4 -----------
        #  Site name            Configured Registered Incons
        # xtr1_1                        1          1      0
        # xtr2                          1          1      0
        p2 = re.compile(r'(?P<site_name>(\S+)) +(?P<cfgd>(\d+))'
                         ' +(?P<registered>(\d+)) +(?P<incons>(\d+))$')

        # Number of configured sites:                     2
        p3 = re.compile(r'Number +of +configured +sites: +(?P<val>(\d+))$')

        # Number of registered sites:                     2
        p4 = re.compile(r'Number +of +registered +sites: +(?P<val>(\d+))$')

        # Number of configured EID prefixes:            2
        p5 = re.compile(r'Number +of +configured +EID +prefixes:'
                         ' +(?P<val>(\d+))$')

        # Number of registered EID prefixes:            2
        p6 = re.compile(r'Number +of +registered +EID +prefixes:'
                         ' +(?P<val>(\d+))$')

        # Site-registration limit for router lisp 2:            0
        p7 = re.compile(r'Site-registration +limit +for +router +lisp'
                         ' +(?P<router_id>(\d+)): +(?P<val>(\d+))$')

        # Site-registration count for router lisp 2:            0
        p8 = re.compile(r'Site-registration +count +for +router +lisp'
                         ' +(?P<router_id>(\d+)): +(?P<val>(\d+))$')

        # Sites with inconsistent registrations:          0
        p9 = re.compile(r'Sites +with +inconsistent +registrations:'
                         ' +(?P<val>(\d+))$')

        for line in out.splitlines():
            line = line.strip()

            # Output for router lisp 0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                lisp_router_id = int(group['router_id'])
                if group['instance_id']:
                    instance_id = group['instance_id']
                # Create lisp_dict
                lisp_dict = parsed_dict.\
                            setdefault('lisp_router_instances', {}).\
                            setdefault(lisp_router_id, {})
                lisp_dict['lisp_router_instance_id'] = lisp_router_id
                # Create ms dict
                ms_dict = lisp_dict.setdefault('service', {}).\
                                setdefault(service, {}).\
                                setdefault('instance_id', {}).\
                                setdefault(instance_id, {}).\
                                setdefault('map_server', {})
                # Create counters dict
                summary_dict = ms_dict.setdefault('summary', {})
                continue

            #  Site name            Configured Registered Incons
            # xtr2                           1          1      0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                # Create sites dict
                sites_dict = ms_dict.setdefault('sites', {}).\
                                setdefault(group['site_name'], {})
                sites_dict['site_id'] = group['site_name']
                sites_dict['configured'] = int(group['cfgd'])
                sites_dict['registered'] = int(group['registered'])
                sites_dict['inconsistent'] = int(group['incons'])
                continue

            # Number of configured sites:                     2
            m = p3.match(line)
            if m:
                summary_dict['number_configured_sites'] = \
                    int(m.groupdict()['val'])
                continue

            # Number of registered sites:                     2
            m = p4.match(line)
            if m:
                summary_dict['number_registered_sites'] = \
                    int(m.groupdict()['val'])
                continue

            # Number of configured EID prefixes:            2
            m = p5.match(line)
            if m:
                address_type = service + '-afi'
                datum_dict = summary_dict.setdefault('af_datum', {}).\
                                setdefault(address_type, {})
                datum_dict['address_type'] = address_type
                datum_dict['number_configured_eids'] = \
                    int(m.groupdict()['val'])
                continue

            # Number of registered EID prefixes:            2
            m = p6.match(line)
            if m:
                datum_dict['number_registered_eids'] = \
                    int(m.groupdict()['val'])
                continue

            # Site-registration limit for router lisp 2:            0
            m = p7.match(line)
            if m:
                summary_dict['site_registration_limit'] = \
                    int(m.groupdict()['val'])
                continue

            # Site-registration count for router lisp 2:            0
            m = p8.match(line)
            if m:
                summary_dict['site_registration_count'] = \
                    int(m.groupdict()['val'])
                continue

            # Sites with inconsistent registrations:          0
            m = p9.match(line)
            if m:
                summary_dict['sites_with_inconsistent_registrations'] = \
                    int(m.groupdict()['val'])
                continue

        return parsed_dict


# =====================================================================================
# Schema for 'show lisp all instance-id <instance_id> <service> server detail internal'
# =====================================================================================
class ShowLispServiceServerDetailInternalSchema(MetaParser):

    '''Schema for "show lisp all instance-id <instance_id> <service> server detail internal" '''

    schema = {
        'lisp_router_instances':
            {Any():
                {Optional('service'):
                    {Any():
                        {'map_server':
                            {'sites':
                                {Any():
                                    {'site_id': str,
                                    'allowed_configured_locators': str,
                                    },
                                },
                            Optional('virtual_network_ids'):
                                {Any():
                                    {'vni': str,
                                    'mappings':
                                        {Any():
                                            {'eid_id': str,
                                            'eid_address':
                                                {'address_type': str,
                                                'virtual_network_id': str,
                                                Optional('ipv4'):
                                                    {'ipv4': str,
                                                    },
                                                Optional('ipv6'):
                                                    {'ipv6': str,
                                                    },
                                                Optional('ipv4_prefix'):
                                                    {'ipv4_prefix': str,
                                                    },
                                                Optional('ipv6_prefix'):
                                                    {'ipv6_prefix': str,
                                                    },
                                                },
                                            'site_id': str,
                                            'first_registered': str,
                                            'last_registered': str,
                                            'routing_table_tag': int,
                                            'origin': str,
                                            Optional('more_specifics_accepted'): bool,
                                            'merge_active': bool,
                                            'proxy_reply': bool,
                                            'ttl': str,
                                            'state': str,
                                            'registration_errors':
                                                {'authentication_failures': int,
                                                'allowed_locators_mismatch': int,
                                                },
                                            Optional('sgt'): int,
                                            Optional('mapping_records'):
                                                {Any():
                                                    {'xtr_id': str,
                                                    'site_id': str,
                                                    'etr': str,
                                                    'eid':
                                                        {'address_type': str,
                                                        'virtual_network_id': str,
                                                        Optional('ipv4'):
                                                            {'ipv4': str,
                                                            },
                                                        Optional('ipv6'):
                                                            {'ipv6': str,
                                                            },
                                                        Optional('ipv4_prefix'):
                                                            {'ipv4_prefix': str,
                                                            },
                                                        Optional('ipv6_prefix'):
                                                            {'ipv6_prefix': str,
                                                            },
                                                        },
                                                    'ttl': str,
                                                    'time_to_live': int,
                                                    'creation_time': str,
                                                    'merge': bool,
                                                    'proxy_reply': bool,
                                                    'map_notify': bool,
                                                    'hash_function': str,
                                                    'nonce': str,
                                                    'state': str,
                                                    'security_capability': bool,
                                                    'sourced_by': str,
                                                    'locator':
                                                        {Any():
                                                            {'local': bool,
                                                            'state': str,
                                                            'priority': int,
                                                            'weight': int,
                                                            'scope': str,
                                                            },
                                                        },
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        }


# =====================================================================================
# Parser for 'show lisp all instance-id <instance_id> <service> server detail internal'
# =====================================================================================
class ShowLispServiceServerDetailInternal(ShowLispServiceServerDetailInternalSchema):

    '''Parser for "show lisp all instance-id <instance_id> <service> server detail internal"'''

    cli_command = 'show lisp all instance-id {instance_id} {service} server detail internal'

    def cli(self, service, instance_id, output=None):
        if output is None:
            assert service in ['ipv4', 'ipv6', 'ethernet']
            out = self.device.execute(self.cli_command.format(instance_id=instance_id, service=service))
        else:
            out = output

        # Init vars
        parsed_dict = {}

        # state dict
        state_dict = {
            'yes': True,
            'no': False,
            }

        # Output for router lisp 0
        # Output for router lisp 0 instance-id 193
        # Output for router lisp 2 instance-id 101
        p1 = re.compile(r'Output +for +router +lisp +(?P<router_id>(\S+))'
                         '(?: +instance-id +(?P<instance_id>(\d+)))?$')

        # Site name: prov1
        # Site name: provider
        p2 = re.compile(r'Site +name: +(?P<site_name>(\S+))$')

        # Allowed configured locators: any
        p3 = re.compile(r'Allowed +configured +locators: +(?P<val>(\S+))$')

        # EID-prefix: 192.168.0.1/32 instance-id 101
        p4 = re.compile(r'EID-prefix: +(?P<eid>(\S+)) +instance-id'
                         ' +(?P<iid>(\d+))$')

        # First registered:     01:12:41
        p5 = re.compile(r'First +registered: +(?P<first>(\S+))$')

        # Last registered:      01:12:41
        p6 = re.compile(r'Last +registered: +(?P<last>(\S+))$')

        # Routing table tag:    0
        p7 = re.compile(r'Routing +table +tag: +(?P<rtt>(\d+))$')

        # Origin:               Dynamic, more specific of 192.168.0.0/24
        p8_1 = re.compile(r'Origin: +(?P<origin>(\S+))(?:, +more +specific +of'
                         ' +(\S+))?$')

        # Origin:               Configuration, accepting more specifics
        p8_2 = re.compile(r'Origin: +(?P<origin>(\S+))(?:,'
                         ' +(?P<more_specific>(accepting more specifics)))?$')

        # Merge active:         No
        p9 = re.compile(r'Merge +active: +(?P<merge>(Yes|No))$')

        # Proxy reply:          Yes
        p10 = re.compile(r'Proxy +reply: +(?P<proxy>(Yes|No))$')

        # TTL:                  1d00h
        p11 = re.compile(r'TTL: +(?P<ttl>(\S+))$')

        # State:                complete
        p12 = re.compile(r'State: +(?P<state>(\S+))$')

        # Registration errors:
        #  Authentication failures:   0
        p13 = re.compile(r'Authentication +failures: +(?P<auth_failures>(\d+))$')

        # Allowed locators mismatch: 0
        p14 = re.compile(r'Allowed +locators +mismatch: +(?P<mismatch>(\d+))$')

        # ETR 10.16.2.2, last registered 01:12:41, proxy-reply, map-notify
        p15 = re.compile(r'ETR +(?P<etr>(\S+)), +last +registered'
                          ' +(?P<last_registered>(\S+)),'
                          '(?: +(?P<proxy_reply>(proxy-reply)),)?'
                          '(?: +(?P<map_notify>(map-notify)))?$')

        # TTL 1d00h, no merge, hash-function sha1, nonce 0x70D18EF4-0x3A605D67
        p16 = re.compile(r'TTL +(?P<ttl>(\S+)),(?: +(?P<merge>(no merge)),)?'
                          ' +hash-function +(?P<hash>(\S+)) +nonce'
                          ' +(?P<nonce>(\S+))$')

        # state complete, no security-capability
        p17 = re.compile(r'state +(?P<state>(\S+))'
                          '(?:, +(?P<security>(no security-capability)))?$')

        # xTR-ID 0x21EDD25F-0x7598784C-0x769C8E4E-0xC04926EC
        p18 = re.compile(r'xTR-ID +(?P<xtr_id>(.*))$')

        # site-ID unspecified
        p19 = re.compile(r'site-ID +(?P<site_id>(.*))$')

        # sourced by reliable transport
        p20 = re.compile(r'sourced +by +(?P<source>(.*))$')

        # Locator  Local  State      Pri/Wgt  Scope
        # 10.16.2.2 yes    up          50/50   IPv4 none
        p21 = re.compile(r'(?P<locator>(\S+)) +(?P<local>(\S+))'
                          ' +(?P<state>(\S+)) +(?P<priority>(\d+))\/'
                          '(?P<weight>(\d+)) +(?P<scope>(.*))$')

        # ETR 10.16.2.2
        p22 = re.compile(r'ETR +(?P<etr>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})$')

        # ETR 1000:1000:1000:1000:1000::
        p23 = re.compile(r'ETR +(?P<etr>[a-fA-F\d\:]+)$')

        # last registered 01:12:41, proxy-reply, map-notify
        p24 = re.compile(r'last +registered +(?P<last_registered>(\S+)),'
                          '(?: +(?P<proxy_reply>(proxy-reply)),)'
                          '?(?: +(?P<map_notify>(map-notify)))?$')

        # SGT: 10
        p25 = re.compile(r'SGT:\s+(?P<sgt>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            # Output for router lisp 0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                lisp_router_id = int(group['router_id'])
                if group['instance_id']:
                    instance_id = group['instance_id']
                continue

            # Site name: prov1
            m = p2.match(line)
            if m:
                site_id = m.groupdict()['site_name']
                # Create service dict
                ms_dict = parsed_dict.\
                                setdefault('lisp_router_instances', {}).\
                                setdefault(lisp_router_id, {}).\
                                setdefault('service', {}).\
                                setdefault(service, {}).\
                                setdefault('map_server', {})
                # Create sites dict
                sites_dict = ms_dict.setdefault('sites', {}).\
                                setdefault(site_id, {})
                sites_dict['site_id'] = site_id
                continue

            # Allowed configured locators: any
            m = p3.match(line)
            if m:
                sites_dict['allowed_configured_locators'] = m.groupdict()['val']
                continue

            # EID-prefix: 192.168.0.1/32 instance-id 101
            m = p4.match(line)
            if m:
                group = m.groupdict()
                eid = group['eid']
                # Create vni dict
                vni_dict = ms_dict.setdefault('virtual_network_ids', {}).\
                            setdefault(group['iid'], {})
                vni_dict['vni'] = group['iid']
                mappings_dict = vni_dict.setdefault('mappings', {}).\
                                    setdefault(eid, {})
                mappings_dict['eid_id'] = eid
                eid_address_dict = mappings_dict.setdefault('eid_address', {})
                eid_address_dict['virtual_network_id'] = group['iid']
                if ":" not in eid:
                    eid_address_dict['address_type'] = 'ipv4-afi'
                    eid_address_dict.setdefault('ipv4', {})['ipv4'] = eid
                else:
                    eid_address_dict['address_type'] = 'ipv6-afi'
                    eid_address_dict.setdefault('ipv6', {})['ipv6'] = eid
                mappings_dict['site_id'] = site_id
                continue

            # First registered:     01:12:41
            m = p5.match(line)
            if m:
                mappings_dict['first_registered'] = m.groupdict()['first']
                continue

            #     Last registered:      01:12:41
            m = p6.match(line)
            if m:
                mappings_dict['last_registered'] = m.groupdict()['last']
                continue

            # Routing table tag:    0
            m = p7.match(line)
            if m:
                mappings_dict['routing_table_tag'] = int(m.groupdict()['rtt'])
                continue

            # Origin:               Dynamic, more specific of 192.168.0.0/24
            m = p8_1.match(line)
            if m:
                mappings_dict['origin'] = m.groupdict()['origin']
                continue

            # Origin:               Configuration, accepting more specifics
            m = p8_2.match(line)
            if m:
                mappings_dict['origin'] = m.groupdict()['origin']
                if m.groupdict()['more_specific']:
                    mappings_dict['more_specifics_accepted'] = True
                continue

            # Merge active:         No
            m = p9.match(line)
            if m:
                mappings_dict['merge_active'] = \
                    state_dict[m.groupdict()['merge'].lower()]
                continue

            # Proxy reply:          Yes
            m = p10.match(line)
            if m:
                mappings_dict['proxy_reply'] = \
                    state_dict[m.groupdict()['proxy'].lower()]
                continue

            # TTL:                  1d00h
            m = p11.match(line)
            if m:
                mappings_dict['ttl'] = m.groupdict()['ttl']
                continue

            # State:                complete
            m = p12.match(line)
            if m:
                mappings_dict['state'] = m.groupdict()['state']
                continue

            # Registration errors:
            #  Authentication failures:   0
            m = p13.match(line)
            if m:
                reg_errors_dict = mappings_dict.\
                                    setdefault('registration_errors', {})
                reg_errors_dict['authentication_failures'] = \
                    int(m.groupdict()['auth_failures'])
                continue

            # Allowed locators mismatch: 0
            m = p14.match(line)
            if m:
                reg_errors_dict['allowed_locators_mismatch'] = \
                    int(m.groupdict()['mismatch'])
                continue

            # ETR 10.16.2.2, last registered 01:12:41, proxy-reply, map-notify
            m = p15.match(line)
            if m:
                group = m.groupdict()
                etr = group['etr']
                creation_time = group['last_registered']
                if group['proxy_reply']:
                    proxy_reply = True
                if group['map_notify']:
                    map_notify = True
                continue

            #  TTL 1d00h, no merge, hash-function sha1, nonce 0x70D18EF4-0x3A605D67
            m = p16.match(line)
            if m:
                group = m.groupdict()
                ttl = group['ttl']
                n = re.match('(?P<day>(\d+))d(?P<hours>(\d+))h', ttl)
                days = n.groupdict()['day'] ; hours = n.groupdict()['hours']
                time_to_live = (int(days) * 86400) + (int(hours) * 3600)
                if group['merge'] == 'no merge':
                    merge_active = False
                hash_function = group['hash']
                nonce = group['nonce']
                continue

            # state complete, no security-capability
            m = p17.match(line)
            if m:
                group = m.groupdict()
                state = group['state']
                if 'no' in group['security']:
                    security_capability = False
                else:
                    security_capability = True
                continue

            # xTR-ID 0x21EDD25F-0x7598784C-0x769C8E4E-0xC04926EC
            m = p18.match(line)
            if m:
                group = m.groupdict()
                mapping_records_dict = mappings_dict.\
                                        setdefault('mapping_records', {}).\
                                        setdefault(group['xtr_id'], {})
                mapping_records_dict['xtr_id'] = group['xtr_id']
                mapping_records_dict['etr'] = etr
                mr_eid_dict = mapping_records_dict.setdefault('eid', {})
                mr_eid_dict['virtual_network_id'] = instance_id
                if ":" not in eid:
                    mr_eid_dict['address_type'] = 'ipv4-afi'
                    mr_eid_dict.setdefault('ipv4', {})['ipv4'] = eid
                else:
                    mr_eid_dict['address_type'] = 'ipv6-afi'
                    mr_eid_dict.setdefault('ipv6', {})['ipv6'] = eid
                # Set previously parsed values
                mapping_records_dict['security_capability'] = security_capability
                mapping_records_dict['state'] = state
                mapping_records_dict['nonce'] = nonce
                mapping_records_dict['hash_function'] = hash_function
                mapping_records_dict['merge'] = merge_active
                mapping_records_dict['ttl'] = ttl
                mapping_records_dict['time_to_live'] = time_to_live
                mapping_records_dict['map_notify'] = map_notify
                mapping_records_dict['proxy_reply'] = proxy_reply
                mapping_records_dict['map_notify'] = map_notify
                mapping_records_dict['creation_time'] = creation_time
                continue

            # site-ID unspecified
            m = p19.match(line)
            if m:
                mapping_records_dict['site_id'] = m.groupdict()['site_id']
                continue

            # sourced by reliable transport
            m = p20.match(line)
            if m:
                mapping_records_dict['sourced_by'] = m.groupdict()['source']
                continue

            # Locator  Local  State      Pri/Wgt  Scope
            # 10.16.2.2  yes    up          50/50   IPv4 none
            m = p21.match(line)
            if m:
                group = m.groupdict()
                locator_dict = mapping_records_dict.setdefault('locator', {}).\
                                setdefault(group['locator'], {})
                locator_dict['local'] = state_dict[group['local']]
                locator_dict['state'] = group['state']
                locator_dict['priority'] = int(group['priority'])
                locator_dict['weight'] = int(group['weight'])
                locator_dict['scope'] = group['scope']
                continue

            # ETR 10.16.2.2
            m = p22.match(line)
            if m:
                group = m.groupdict()
                etr = group['etr']
                continue

            # ETR 1000:1000:1000:1000:1000::
            m = p23.match(line)
            if m:
                group = m.groupdict()
                etr = group['etr']
                continue

            # last registered 01:12:41, proxy-reply, map-notify
            m = p24.match(line)
            if m:
                group = m.groupdict()
                creation_time = group['last_registered']
                if group['proxy_reply']:
                    proxy_reply = True
                if group['map_notify']:
                    map_notify = True
                continue

            # SGT: 10
            m = p25.match(line)
            if m:
                mappings_dict['sgt'] = int(m.groupdict()['sgt'])
                continue

        return parsed_dict


# =========================================================================
# Schema for 'show lisp all instance-id <instance_id> <service> statistics'
# =========================================================================
class ShowLispServiceStatisticsSchema(MetaParser):

    ''' Schema for
    * show lisp service {service} statistics
    * show lisp {lisp_id} service {service} statistics'''

    schema = {
        'lisp_id': {
            int: {
                'last_cleared': str,
                'control_packets': {
                    'map_requests': {
                        'in': int,
                        'out': int,
                        '5_sec': int,
                        '1_min': int,
                        '5_min': int,
                        'encapsulated': {
                            'in': int,
                            'out': int
                            },
                        'rloc_probe': {
                            'in': int,
                            'out': int
                            },
                        'smr_based': {
                            'in': int,
                            'out': int
                            },
                        'extranet_smr_cross_iid': {
                            'in': int
                            },
                        'expired': {
                            'on_queue': int,
                            'no_reply': int
                            },
                        'map_resolver_forwarded': int,
                        'map_server_forwarded': int
                        },
                    'map_reply': {
                        'in': int,
                        'out': int,
                        'authoritative': {
                            'in': int,
                            'out': int
                            },
                        'non_authoritative': {
                            'in': int,
                            'out': int
                            },
                        'negative': {
                            'in': int,
                            'out': int
                            },
                        'rloc_probe': {
                            'in': int,
                            'out': int
                            },
                        'map_server_proxy_reply': {
                            'out': int
                            }
                        },
                    'wlc_map_subscribe': {
                        'in': int,
                        'out': int,
                        'failures': {
                            'in': int,
                            'out': int
                            }
                        },
                    'wlc_map_unsubscribe': {
                        'in': int,
                        'out': int,
                        'failures': {
                            'in': int,
                            'out': int
                            }
                        },
                    'map_register': {
                        'in': int,
                        'out': int,
                        '5_sec': int,
                        '1_min': int,
                        '5_min': int,
                        'map_server_af_disabled': int,
                        'not_valid_site_eid_prefix': int,
                        'authentication_failures': int,
                        'disallowed_locators': int,
                        'misc': int
                        },
                    'wlc_map_registers': {
                        'in': int,
                        'out': int,
                        'ap': {
                            'in': int,
                            'out': int
                            },
                        'client': {
                            'in': int,
                            'out': int
                            },
                        'failures': {
                            'in': int,
                            'out': int
                            }
                        },
                    'map_notify': {
                        'in': int,
                        'out': int,
                        'authentication_failures': int
                        },
                    'wlc_map_notify': {
                        'in': int,
                        'out': int,
                        'ap': {
                            'in': int,
                            'out': int
                            },
                        'client': {
                            'in': int,
                            'out': int
                            },
                        'failures': {
                            'in': int,
                            'out': int
                            }
                        },
                    'publish_subscribe': {
                        'subscription_request': {
                            'in': int,
                            'out': int,
                            'iid': {
                                'in': int,
                                'out': int
                                },
                            'pub_refresh': {
                                'in': int,
                                'out': int
                                },
                            'policy': {
                                'in': int,
                                'out': int
                                },
                            'failures': {
                                'in': int,
                                'out': int
                                }
                            },
                        'subscription_status': {
                            'in': int,
                            'out': int,
                            'end_of_publication': {
                                'in': int,
                                'out': int
                                },
                            'subscription_rejected': {
                                'in': int,
                                'out': int
                                },
                            'subscription_removed': {
                                'in': int,
                                'out': int
                                },
                            'failures': {
                                'in': int,
                                'out': int
                                }
                            },
                        'solicit_subscription': {
                            'in': int,
                            'out': int,
                            'failures': {
                                'in': int,
                                'out': int
                                }
                            },
                        'publication': {
                        'in': int,
                        'out': int,
                        'failures': {
                            'in': int,
                            'out': int
                            }
                        }
                        }
                    },
                'errors': {
                    'mapping_rec_ttl_alerts': int,
                    'map_request_invalid_source_rloc_drops': int,
                    'map_register_invalid_source_rloc_drops': int,
                    'ddt_requests_failed': int,
                    'ddt_itr_map_requests': {
                        'dropped': int,
                        'nonce_collision': int,
                        'bad_xtr_nonce': int
                        }
                    },
                'cache_related': {
                    'cache_entries': {
                        'created': int,
                        'deleted': int
                        },
                    'nsf_cef_replay_entry_count': int,
                    'rejected_eid_prefix_due_to_limit': int
                    },
                'forwarding': {
                    'data_signals': {
                        'processed': int,
                        'dropped': int
                        },
                    'reachability_reports': {
                        'count': int,
                        'dropped': int
                        },
                    'smr_signals': {
                        'dropped': int
                        }
                    },
                'rloc_statistics': {
                    'last_cleared': str,
                    'control_packets': {
                        'rtr': {
                            'map_requests_forwarded': int,
                            'map_notifies_forwarded': int
                            },
                        'ddt': {
                            'map_requests': {
                                'in': int,
                                'out': int
                                },
                            'map_referrals': {
                                'in': int,
                                'out': int
                                }
                            }
                        },
                    'errors': {
                        'map_request_format': int,
                        'map_reply_format': int,
                        'map_referral': int
                        }
                    },
                'misc_statistics': {
                    'invalid': {
                        'ip_version_drops': int,
                        'ip_header_drops': int,
                        'ip_proto_field_drops': int,
                        'packet_size_drops': int,
                        'lisp_control_port_drops': int,
                        'lisp_checksum_drops': int,
                        },
                    'unsupported_lisp_packet_drops': int,
                    'unknown_packet_drops': int
                    }
                }
            }
        }


class ShowLispServiceStatistics(ShowLispServiceStatisticsSchema):

    ''' Parser for
    * show lisp service {service} statistics
    * show lisp {lisp_id} service {service} statistics'''

    cli_command = ['show lisp service {service} statistics',
                   'show lisp {lisp_id} service {service} statistics']

    def cli(self, service, output=None, lisp_id=None):

        if output is None:
            if lisp_id and service:
                output = self.device.execute(self.cli_command[1].format(lisp_id=lisp_id, service=service))
            elif service:
                output = self.device.execute(self.cli_command[0].format(service=service))
            else:
                raise TypeError("No arguments provided to parser")

        ret_dict = {}

        # Output for router lisp 0
        # Output for router lisp 0 instance-id 101
        p1 = re.compile(r'^Output for router lisp (?P<lisp_id>\d+)(\s+instance-id\s+\d+)?$')

        # LISP EID Statistics for all EID instances - last cleared: never
        p2 = re.compile(r'^LISP EID Statistics for all EID instances - last cleared: (?P<last_cleared>\S+)$')

        # Map-Requests in/out:                              1/24
        p3 = re.compile(r'^Map-Requests in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Map-Requests in (5 sec/1 min/5 min):            0/0/0
        p4 = re.compile(r'^Map-Requests in \(5 sec\/1 min\/5 min\):\s+(?P<sec>\d+)\/(?P<min1>\d+)\/(?P<min5>\d+)$')

        # Encapsulated Map-Requests in/out:               0/23
        p5 = re.compile(r'^Encapsulated Map-Requests in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # RLOC-probe Map-Requests in/out:                 1/1
        p6 = re.compile(r'^RLOC-probe Map-Requests in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)')

        # SMR-based Map-Requests in/out:                  0/0
        p7 = re.compile(r'^SMR-based Map-Requests in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Extranet SMR cross-IID Map-Requests in:         0
        p8 = re.compile(r'^Extranet SMR cross-IID Map-Requests in:\s+(?P<in>\d+)$')

        # Map-Requests expired on-queue/no-reply          0/3
        p9 = re.compile(r'^Map-Requests expired on-queue\/no-reply\s+(?P<on_queue>\d+)\/(?P<no_reply>\d+)$')

        # Map-Resolver Map-Requests forwarded:            0
        p10 = re.compile(r'^Map-Resolver Map-Requests forwarded:\s+(?P<map_resolver_forwarded>\d+)$')

        # Map-Server Map-Requests forwarded:              0
        p11 = re.compile(r'^Map-Server Map-Requests forwarded:\s+(?P<map_server_forwarded>\d+)$')

        # Map-Reply records in/out:                         24/1
        p12 = re.compile(r'^Map-Reply records in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Authoritative records in/out:                   23/1
        p13 = re.compile(r'^Authoritative records in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Non-authoritative records in/out:               1/0
        p14 = re.compile(r'^Non-authoritative records in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Negative records in/out:                        22/0
        p15 = re.compile(r'^Negative records in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # RLOC-probe records in/out:                      1/1
        p16 = re.compile(r'^RLOC-probe records in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Map-Server Proxy-Reply records out:             0
        p17 = re.compile(r'^Map-Server Proxy-Reply records out:\s+(?P<out>\d+)$')

        # WLC Map-Subscribe records in/out:                 0/2
        p18 = re.compile(r'^WLC Map-Subscribe records in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Map-Subscribe failures in/out:                  0/0
        p19 = re.compile(r'^Map-Subscribe failures in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # WLC Map-Unsubscribe records in/out:               0/0
        p20 = re.compile(r'^WLC Map-Unsubscribe records in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Map-Unsubscribe failures in/out:                0/0
        p21 = re.compile(r'^Map-Unsubscribe failures in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Map-Register records in/out:                      0/6
        p22 = re.compile(r'^Map-Register records in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Map-Registers in (5 sec/1 min/5 min):           0/0/0
        p23 = re.compile(r'^Map-Registers in \(5 sec\/1 min\/5 min\):\s+(?P<sec_5>\d+)\/(?P<min_1>\d+)\/(?P<min_5>\d+)$')

        # Map-Server AF disabled:                         0
        p24 = re.compile(r'^Map-Server AF disabled:\s+(?P<map_server_af_disabled>\d+)$')

        # Not valid site eid prefix:                      0
        p25 = re.compile(r'^Not valid site eid prefix:\s+(?P<not_valid_site_eid_prefix>\d+)$')

        # Authentication failures:                        0
        p26 = re.compile(r'^Authentication failures:\s+(?P<authentication_failures>\d+)$')

        # Disallowed locators:                            0
        p27 = re.compile(r'^Disallowed locators:\s+(?P<disallowed_locators>\d+)$')

        # Miscellaneous:                                  0
        p28 = re.compile(r'^Miscellaneous:\s+(?P<misc>\d+)$')

        # WLC Map-Register records in/out:                  0/0
        p29 = re.compile(r'^WLC Map-Register records in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # WLC AP Map-Register in/out:                     0/0
        p30 = re.compile(r'^WLC AP Map-Register in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # WLC Client Map-Register in/out:                 0/0
        p31 = re.compile(r'^WLC Client Map-Register in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # WLC Map-Register failures in/out:               0/0
        p32 = re.compile(r'^WLC Map-Register failures in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Map-Notify records in/out:                        8/0
        p33 = re.compile(r'^Map-Notify records in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Authentication failures:                        0
        p34 = re.compile(r'^Authentication failures:\s+(?P<authentication_failures>\d+)')

        # WLC Map-Notify records in/out:                    0/0
        p35 = re.compile(r'^WLC Map-Notify records in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)')

        # WLC AP Map-Notify in/out:                       0/0
        p36 = re.compile(r'^WLC AP Map-Notify in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)')

        # WLC Client Map-Notify in/out:                   0/0
        p37 = re.compile(r'^WLC Client Map-Notify in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)')

        # WLC Map-Notify failures in/out:                 0/0
        p38 = re.compile(r'^WLC Map-Notify failures in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Subscription Request records in/out:            0/4
        p39 = re.compile(r'^Subscription Request records in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # IID subscription requests in/out:             0/0
        p40 = re.compile(r'^IID subscription requests in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Pub-refresh subscription requests in/out:     0/0
        p41 = re.compile(r'^Pub-refresh subscription requests in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Policy subscription requests in/out:          0/4
        p42 = re.compile(r'^Policy subscription requests in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Subscription Request failures in/out:           0/0
        p43 = re.compile(r'^Subscription Request failures in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Subscription Status records in/out:             2/0
        p44 = re.compile(r'^Subscription Status records in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # End of Publication records in/out:            0/0
        p45 = re.compile(r'^End of Publication records in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Subscription rejected records in/out:         0/0
        p46 = re.compile(r'^Subscription rejected records in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Subscription removed records in/out:          0/0
        p47 = re.compile(r'^Subscription removed records in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Subscription Status failures in/out:            0/0
        p48 = re.compile(r'^Subscription Status failures in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Solicit Subscription records in/out:            2/0
        p49 = re.compile(r'^Solicit Subscription records in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Solicit Subscription failures in/out:           0/0
        p50 = re.compile(r'^Solicit Subscription failures in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Publication records in/out:                     0/0
        p51 = re.compile(r'^Publication records in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Publication failures in/out:                    0/0
        p52 = re.compile(r'^Publication failures in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Mapping record TTL alerts:                        0
        p53 = re.compile(r'^Mapping record TTL alerts:\s+(?P<mapping_rec_ttl_alerts>\d+)$')

        # Map-Request invalid source rloc drops:            0
        p54 = re.compile(r'^Map-Request invalid source rloc drops:\s+(?P<map_request_invalid_source_rloc>\d+)$')

        # Map-Register invalid source rloc drops:           0
        p55 = re.compile(r'^Map-Register invalid source rloc drops:\s+(?P<map_register_invalid_source_rloc>\d+)$')

        # DDT Requests failed:                              0
        p56 = re.compile(r'^DDT Requests failed:\s+(?P<ddt_requests_failed>\d+)$')

        # DDT ITR Map-Requests dropped:                     0 (nonce-collision: 0, bad-xTR-nonce: 0)
        p57 = re.compile(r'^DDT ITR Map-Requests dropped:\s+(?P<dropped>\d+)\s+'
                         r'\(nonce-collision:\s+(?P<nonce_collision>\d+), '
                         r'bad-xTR-nonce:\s+(?P<bad_xtr_nonce>\d+)\)$')

        # Cache entries created/deleted:                    10/8
        p58 = re.compile(r'^Cache entries created\/deleted:\s+(?P<created>\d+)\/(?P<deleted>\d+)$')

        # NSF CEF replay entry count                        0
        p59 = re.compile(r'^NSF CEF replay entry count\s+(?P<nsf_cef_replay_entry_count>\d+)$')

        # Number of rejected EID-prefixes due to limit:     0
        p60 = re.compile(r'^Number of rejected EID-prefixes due to limit:\s+'
                         r'(?P<rejected_eid_prefix_due_to_limit>\d+)$')

        # Number of data signals processed:                 2 (+ dropped 0)
        p61 = re.compile(r'^Number of data signals processed:\s+'
                         r'(?P<processed>\d+)\s+\(\+\s+dropped\s(?P<dropped>\d+)\)$')

        # Number of reachability reports:                   0 (+ dropped 0)
        p62 = re.compile(r'^Number of reachability reports:\s+'
                         r'(?P<count>\d+)\s+\(\+\s+dropped\s(?P<dropped>\d+)\)$')

        # Number of SMR signals dropped:                    0
        p63 = re.compile(r'^Number of SMR signals dropped:\s+(?P<dropped>\d+)$')

        # LISP RLOC Statistics - last cleared: never
        p64 = re.compile(r'^LISP RLOC Statistics - last cleared:\s(?P<last_cleared>\S+)$')

        # RTR Map-Requests forwarded:                       0
        p65 = re.compile(r'^RTR Map-Requests forwarded:\s+(?P<map_requests_forwarded>\d+)$')

        # RTR Map-Notifies forwarded:                       0
        p66 = re.compile(r'^RTR Map-Notifies forwarded:\s+(?P<map_notifies_forwarded>\d+)$')

        # DDT-Map-Requests in/out:                          0/0
        p67 = re.compile(r'^DDT-Map-Requests in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # DDT-Map-Referrals in/out:                         0/0
        p68 = re.compile(r'^DDT-Map-Referrals in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Map-Request format errors:                        0
        p69 = re.compile(r'^Map-Request format errors:\s+(?P<map_request_format>\d+)$')

        # Map-Reply format errors:                          0
        p70 = re.compile(r'^Map-Reply format errors:\s+(?P<map_reply_format>\d+)$')

        # Map-Referral format errors:                       0
        p71 = re.compile(r'^Map-Referral format errors:\s+(?P<map_referral>\d+)$')

        # Invalid IP version drops:                         0
        p72 = re.compile(r'^Invalid IP version drops:\s+(?P<ip_version_drops>\d+)$')

        # Invalid IP header drops:                          0
        p73 = re.compile(r'^Invalid IP header drops:\s+(?P<ip_header_drops>\d+)$')

        # Invalid IP proto field drops:                     0
        p74 = re.compile(r'^Invalid IP proto field drops:\s+(?P<ip_proto_field_drops>\d+)$')

        # Invalid packet size drops:                        0
        p75 = re.compile(r'^Invalid packet size drops:\s+(?P<packet_size_drops>\d+)$')

        # Invalid LISP control port drops:                  0
        p76 = re.compile(r'^Invalid LISP control port drops:\s+(?P<lisp_control_port_drops>\d+)$')

        # Invalid LISP checksum drops:                      0
        p77 = re.compile(r'^Invalid LISP checksum drops:\s+(?P<lisp_checksum_drops>\d+)$')

        # Unsupported LISP packet type drops:               0
        p78 = re.compile(r'^Unsupported LISP packet type drops:\s+(?P<unsupported_lisp_packet_drops>\d+)$')

        # Unknown packet drops:                             0
        p79 = re.compile(r'^Unknown packet drops:\s+(?P<unknown_packet_drops>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            # Output for router lisp 0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                lisp_id = int(group['lisp_id'])
                lisp_dict = ret_dict.setdefault('lisp_id',{}).\
                                     setdefault(lisp_id,{})
                continue

            # LISP EID Statistics for all EID instances - last cleared: never
            m = p2.match(line)
            if m:
                lisp_id = int(lisp_id) if lisp_id else 0
                lisp_dict = ret_dict.setdefault('lisp_id', {}).setdefault(lisp_id, {})
                group = m.groupdict()
                last_cleared = group['last_cleared']
                lisp_dict.update({'last_cleared':last_cleared})
                continue

            # Map-Requests in/out:                              1/24
            m = p3.match(line)
            if m:
                group = m.groupdict()
                map_in = int(group['in'])
                out = int(group['out'])
                control_dict = lisp_dict.setdefault('control_packets',{})
                map_dict = control_dict.setdefault('map_requests',{})
                map_dict.update({'in':map_in,
                                 'out':out})
                continue

            # Map-Requests in (5 sec/1 min/5 min):            0/0/0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                sec = int(group['sec'])
                min5 = int(group['min5'])
                min1 = int(group['min1'])
                map_dict.update({'5_sec':sec,
                                 '1_min':min1,
                                 '5_min':min5})
                continue

            # Encapsulated Map-Requests in/out:               0/23
            m = p5.match(line)
            if m:
                group = m.groupdict()
                encap_in = int(group['in'])
                out = int(group['out'])
                encap_dict = map_dict.setdefault('encapsulated',{})
                encap_dict.update({'in':encap_in,
                                 'out':out})
                continue

            # RLOC-probe Map-Requests in/out:                 1/1
            m = p6.match(line)
            if m:
                group = m.groupdict()
                encap_in = int(group['in'])
                out = int(group['out'])
                rloc_dict = map_dict.setdefault('rloc_probe',{})
                rloc_dict.update({'in':encap_in,
                                 'out':out})
                continue

            # SMR-based Map-Requests in/out:                  0/0
            m = p7.match(line)
            if m:
                group = m.groupdict()
                smr_in = int(group['in'])
                out = int(group['out'])
                smr_dict = map_dict.setdefault('smr_based',{})
                smr_dict.update({'in':smr_in,
                                 'out':out})
                continue

            # Extranet SMR cross-IID Map-Requests in:         0
            m = p8.match(line)
            if m:
                group = m.groupdict()
                smr_in = int(group['in'])
                extranet_smr_dict = map_dict.setdefault('extranet_smr_cross_iid',{})
                extranet_smr_dict.update({'in':smr_in})
                continue

            # Map-Requests expired on-queue/no-reply          0/3
            m = p9.match(line)
            if m:
                group = m.groupdict()
                on_queue = int(group['on_queue'])
                no_reply = int(group['no_reply'])
                expired_dict = map_dict.setdefault('expired',{})
                expired_dict.update({'on_queue':on_queue,
                                     'no_reply':no_reply})
                continue

            # Map-Resolver Map-Requests forwarded:            0
            m = p10.match(line)
            if m:
                group = m.groupdict()
                map_resolver_forwarded = int(group['map_resolver_forwarded'])
                map_dict.update({'map_resolver_forwarded':map_resolver_forwarded})
                continue

            # Map-Server Map-Requests forwarded:              0
            m = p11.match(line)
            if m:
                group = m.groupdict()
                map_server_forwarded = int(group['map_server_forwarded'])
                map_dict.update({'map_server_forwarded':map_server_forwarded})
                continue

            # Map-Reply records in/out:                         24/1
            m = p12.match(line)
            if m:
                group = m.groupdict()
                map_reply_in = int(group['in'])
                out = int(group['out'])
                map_reply_dict = control_dict.setdefault('map_reply',{})
                map_reply_dict.update({'in':map_reply_in,
                                       'out':out})
                continue

            # Authoritative records in/out:                   23/1
            m = p13.match(line)
            if m:
                group = m.groupdict()
                auth_in = int(group['in'])
                out = int(group['out'])
                auth_dict = map_reply_dict.setdefault('authoritative',{})
                auth_dict.update({'in':auth_in,
                                  'out':out})
                continue

            # Non-authoritative records in/out:               1/0
            m = p14.match(line)
            if m:
                group = m.groupdict()
                non_auth_in = int(group['in'])
                out = int(group['out'])
                non_auth_dict = map_reply_dict.setdefault('non_authoritative',{})
                non_auth_dict.update({'in':non_auth_in,
                                      'out':out})
                continue

            # Negative records in/out:                        22/0
            m = p15.match(line)
            if m:
                group = m.groupdict()
                negative_in = int(group['in'])
                out = int(group['out'])
                negative_dict = map_reply_dict.setdefault('negative',{})
                negative_dict.update({'in':negative_in,
                                      'out':out})
                continue

            # RLOC-probe records in/out:                      1/1
            m = p16.match(line)
            if m:
                group = m.groupdict()
                rloc_probe_in = int(group['in'])
                out = int(group['out'])
                rloc_probe_dict = map_reply_dict.setdefault('rloc_probe',{})
                rloc_probe_dict.update({'in':rloc_probe_in,
                                        'out':out})
                continue

            # Map-Server Proxy-Reply records out:             0
            m = p17.match(line)
            if m:
                group = m.groupdict()
                out = int(group['out'])
                map_server_dict = map_reply_dict.setdefault('map_server_proxy_reply',{})
                map_server_dict.update({'out':out})
                continue

            # WLC Map-Subscribe records in/out:                 0/2
            m = p18.match(line)
            if m:
                group = m.groupdict()
                wlc_in = int(group['in'])
                out = int(group['out'])
                wlc_dict = control_dict.setdefault('wlc_map_subscribe',{})
                wlc_dict.update({'in':wlc_in,
                                 'out':out})
                continue

            # Map-Subscribe failures in/out:                  0/0
            m = p19.match(line)
            if m:
                group = m.groupdict()
                sub_in = int(group['in'])
                out = int(group['out'])
                fail_dict = wlc_dict.setdefault('failures',{})
                fail_dict.update({'in':sub_in,
                                  'out':out})
                continue

            # WLC Map-Unsubscribe records in/out:               0/0
            m = p20.match(line)
            if m:
                group = m.groupdict()
                unsub_in = int(group['in'])
                out = int(group['out'])
                wlc_unsub_dict = control_dict.setdefault('wlc_map_unsubscribe',{})
                wlc_unsub_dict.update({'in':unsub_in,
                                       'out':out})
                continue

            # Map-Unsubscribe failures in/out:                0/0
            m = p21.match(line)
            if m:
                group = m.groupdict()
                fail_unsub_in = int(group['in'])
                out = int(group['out'])
                wlc_map_unsub_dict = wlc_unsub_dict.setdefault('failures',{})
                wlc_map_unsub_dict.update({'in':fail_unsub_in,
                                           'out':out})
                continue

            # Map-Register records in/out:                      0/6
            m = p22.match(line)
            if m:
                group = m.groupdict()
                map_record_in = int(group['in'])
                out = int(group['out'])
                map_reg_record_dict = control_dict.setdefault('map_register',{})
                map_reg_record_dict.update({'in':map_record_in,
                                           'out':out})
                continue

            # Map-Registers in (5 sec/1 min/5 min):           0/0/0
            m = p23.match(line)
            if m:
                group = m.groupdict()
                sec_5 = int(group['sec_5'])
                min_1 = int(group['min_1'])
                min_5 = int(group['min_5'])
                map_reg_record_dict.update({'5_sec':sec_5,
                                           '1_min':min_1,
                                           '5_min':min_5})
                continue

            # Map-Server AF disabled:                         0
            m = p24.match(line)
            if m:
                group = m.groupdict()
                map_server_af_disabled = int(group['map_server_af_disabled'])
                map_reg_record_dict.update({'map_server_af_disabled':map_server_af_disabled})
                continue

            # Not valid site eid prefix:                      0
            m = p25.match(line)
            if m:
                group = m.groupdict()
                not_valid_site_eid_prefix = int(group['not_valid_site_eid_prefix'])
                map_reg_record_dict.update({'not_valid_site_eid_prefix':not_valid_site_eid_prefix})
                continue

            # Authentication failures:                        0
            m = p26.match(line)
            if m and "authentication_failures" not in map_reg_record_dict:
                group = m.groupdict()
                authentication_failures = int(group['authentication_failures'])
                map_reg_record_dict.update({'authentication_failures':authentication_failures})
                continue

            # Disallowed locators:                            0
            m = p27.match(line)
            if m:
                group = m.groupdict()
                disallowed_locators = int(group['disallowed_locators'])
                map_reg_record_dict.update({'disallowed_locators':disallowed_locators})
                continue

            # Miscellaneous:                                  0
            m = p28.match(line)
            if m:
                group = m.groupdict()
                misc = int(group['misc'])
                map_reg_record_dict.update({'misc':misc})
                continue

            # WLC Map-Register records in/out:                  0/0
            m = p29.match(line)
            if m:
                group = m.groupdict()
                wlc_map_in = int(group['in'])
                out = int(group['out'])
                wlc_map_registers_dict = control_dict.setdefault('wlc_map_registers',{})
                wlc_map_registers_dict.update({'in':wlc_map_in,
                                               'out':out})
                continue

            # WLC AP Map-Register in/out:                     0/0
            m = p30.match(line)
            if m:
                group = m.groupdict()
                wlc_ap_map_in = int(group['in'])
                out = int(group['out'])
                wlc_ap_dict = wlc_map_registers_dict.setdefault('ap',{})
                wlc_ap_dict.update({'in':wlc_ap_map_in,
                                    'out':out})
                continue

            # WLC Client Map-Register in/out:                 0/0
            m = p31.match(line)
            if m:
                group = m.groupdict()
                wlc_client_map_in = int(group['in'])
                out = int(group['out'])
                wlc_client_dict = wlc_map_registers_dict.setdefault('client',{})
                wlc_client_dict.update({'in':wlc_client_map_in,
                                        'out':out})
                continue

            # WLC Map-Register failures in/out:               0/0
            m = p32.match(line)
            if m:
                group = m.groupdict()
                wlc_fail_map_in = int(group['in'])
                out = int(group['out'])
                wlc_fail_dict = wlc_map_registers_dict.setdefault('failures',{})
                wlc_fail_dict.update({'in':wlc_fail_map_in,
                                      'out':out})
                continue

            # Map-Notify records in/out:                        8/0
            m = p33.match(line)
            if m:
                group = m.groupdict()
                map_notify_in = int(group['in'])
                out = int(group['out'])
                map_notify_dict = control_dict.setdefault('map_notify',{})
                map_notify_dict.update({'in':map_notify_in,
                                        'out':out})
                continue

            # Authentication failures:                        0
            m = p34.match(line)
            if m:
                group = m.groupdict()
                authentication_failures = int(group['authentication_failures'])
                map_notify_dict.update({'authentication_failures':authentication_failures})
                continue

            # WLC Map-Notify records in/out:                    0/0
            m = p35.match(line)
            if m:
                group = m.groupdict()
                wlc_map_notify_in = int(group['in'])
                out = int(group['out'])
                wlc_map_notify_dict = control_dict.setdefault('wlc_map_notify',{})
                wlc_map_notify_dict.update({'in':wlc_map_notify_in,
                                            'out':out})
                continue

            # WLC AP Map-Notify in/out:                       0/0
            m = p36.match(line)
            if m:
                group = m.groupdict()
                wlc_ap_notify_in = int(group['in'])
                out = int(group['out'])
                wlc_ap_notify_dict = wlc_map_notify_dict.setdefault('ap',{})
                wlc_ap_notify_dict.update({'in':wlc_ap_notify_in,
                                           'out':out})
                continue

            # WLC Client Map-Notify in/out:                   0/0
            m = p37.match(line)
            if m:
                group = m.groupdict()
                wlc_client_notify_in = int(group['in'])
                out = int(group['out'])
                wlc_client_notify_dict = wlc_map_notify_dict.setdefault('client',{})
                wlc_client_notify_dict.update({'in':wlc_client_notify_in,
                                               'out':out})
                continue

            # WLC Map-Notify failures in/out:                 0/0
            m = p38.match(line)
            if m:
                group = m.groupdict()
                wlc_failures_notify_in = int(group['in'])
                out = int(group['out'])
                wlc_fail_notify_dict = wlc_map_notify_dict.setdefault('failures',{})
                wlc_fail_notify_dict.update({'in':wlc_failures_notify_in,
                                             'out':out})
                continue

            # Subscription Request records in/out:            0/4
            m = p39.match(line)
            if m:
                group = m.groupdict()
                sub_request_in = int(group['in'])
                out = int(group['out'])
                publish_dict = control_dict.setdefault('publish_subscribe',{})
                subscription_request_dict = publish_dict.setdefault('subscription_request',{})
                subscription_request_dict.update({'in':sub_request_in,
                                                  'out':out})
                continue

            # IID subscription requests in/out:             0/0
            m = p40.match(line)
            if m:
                group = m.groupdict()
                iid_in = int(group['in'])
                out = int(group['out'])
                iid_dict = subscription_request_dict.setdefault('iid',{})
                iid_dict.update({'in':iid_in,
                                 'out':out})
                continue

            # Pub-refresh subscription requests in/out:     0/0
            m = p41.match(line)
            if m:
                group = m.groupdict()
                pub_in = int(group['in'])
                out = int(group['out'])
                pub_refresh_dict = subscription_request_dict.setdefault('pub_refresh',{})
                pub_refresh_dict.update({'in':pub_in,
                                         'out':out})
                continue

            # Policy subscription requests in/out:          0/4
            m = p42.match(line)
            if m:
                group = m.groupdict()
                policy_in = int(group['in'])
                out = int(group['out'])
                policy_dict = subscription_request_dict.setdefault('policy',{})
                policy_dict.update({'in':policy_in,
                                    'out':out})
                continue

            # Subscription Request failures in/out:           0/0
            m = p43.match(line)
            if m:
                group = m.groupdict()
                policy_in = int(group['in'])
                out = int(group['out'])
                failures_dict = subscription_request_dict.setdefault('failures',{})
                failures_dict.update({'in':policy_in,
                                      'out':out})
                continue

            # Subscription Status records in/out:             2/0
            m = p44.match(line)
            if m:
                group = m.groupdict()
                sub_request_in = int(group['in'])
                out = int(group['out'])
                sub_status_dict = publish_dict.setdefault('subscription_status',{})
                sub_status_dict.update({'in':sub_request_in,
                                        'out':out})
                continue

            # End of Publication records in/out:            0/0
            m = p45.match(line)
            if m:
                group = m.groupdict()
                iid_in = int(group['in'])
                out = int(group['out'])
                end_pub_dict = sub_status_dict.setdefault('end_of_publication',{})
                end_pub_dict.update({'in':iid_in,
                                     'out':out})
                continue

            # Subscription rejected records in/out:         0/0
            m = p46.match(line)
            if m:
                group = m.groupdict()
                pub_in = int(group['in'])
                out = int(group['out'])
                sub_reject_dict = sub_status_dict.setdefault('subscription_rejected',{})
                sub_reject_dict.update({'in':pub_in,
                                        'out':out})
                continue

            # Subscription removed records in/out:          0/0
            m = p47.match(line)
            if m:
                group = m.groupdict()
                policy_in = int(group['in'])
                out = int(group['out'])
                sub_removed_dict = sub_status_dict.setdefault('subscription_removed',{})
                sub_removed_dict.update({'in':policy_in,
                                         'out':out})
                continue

            # Subscription Status failures in/out:            0/0
            m = p48.match(line)
            if m:
                group = m.groupdict()
                policy_in = int(group['in'])
                out = int(group['out'])
                sub_failures_dict = sub_status_dict.setdefault('failures',{})
                sub_failures_dict.update({'in':policy_in,
                                          'out':out})
                continue

            # Solicit Subscription records in/out:            2/0
            m = p49.match(line)
            if m:
                group = m.groupdict()
                sub_request_in = int(group['in'])
                out = int(group['out'])
                solicit_subscription_dict = publish_dict.setdefault('solicit_subscription',{})
                solicit_subscription_dict.update({'in':sub_request_in,
                                                  'out':out})
                continue

            # Solicit Subscription failures in/out:           0/0
            m = p50.match(line)
            if m:
                group = m.groupdict()
                iid_in = int(group['in'])
                out = int(group['out'])
                solicit_fail_dict = solicit_subscription_dict.setdefault('failures',{})
                solicit_fail_dict.update({'in':iid_in,
                                          'out':out})
                continue

            # Publication records in/out:                     0/0
            m = p51.match(line)
            if m:
                group = m.groupdict()
                sub_request_in = int(group['in'])
                out = int(group['out'])
                solicit_publication_dict = publish_dict.setdefault('publication',{})
                solicit_publication_dict.update({'in':sub_request_in,
                                                 'out':out})
                continue

            # Publication failures in/out:                    0/0
            m = p52.match(line)
            if m:
                group = m.groupdict()
                iid_in = int(group['in'])
                out = int(group['out'])
                solicit_failure_dict = solicit_publication_dict.setdefault('failures',{})
                solicit_failure_dict.update({'in':iid_in,
                                             'out':out})
                continue

            # Mapping record TTL alerts:                        0
            m = p53.match(line)
            if m:
                group = m.groupdict()
                mapping_rec_ttl_alerts = int(group['mapping_rec_ttl_alerts'])
                error_dict = lisp_dict.setdefault('errors',{})
                error_dict.update({'mapping_rec_ttl_alerts':mapping_rec_ttl_alerts})
                continue

            # Map-Request invalid source rloc drops:            0
            m = p54.match(line)
            if m:
                group = m.groupdict()
                map_request_invalid_source_rloc_drops = int(group['map_request_invalid_source_rloc'])
                error_dict.update({'map_request_invalid_source_rloc_drops':map_request_invalid_source_rloc_drops})
                continue

            # Map-Register invalid source rloc drops:           0
            m = p55.match(line)
            if m:
                group = m.groupdict()
                map_register_invalid_source_rloc_drops = int(group['map_register_invalid_source_rloc'])
                error_dict.update({'map_register_invalid_source_rloc_drops':map_register_invalid_source_rloc_drops})
                continue

            # DDT Requests failed:                              0
            m = p56.match(line)
            if m:
                group = m.groupdict()
                ddt_requests_failed = int(group['ddt_requests_failed'])
                error_dict.update({'ddt_requests_failed':ddt_requests_failed})
                continue

            # DDT ITR Map-Requests dropped:                     0 (nonce-collision: 0, bad-xTR-nonce: 0)
            m = p57.match(line)
            if m:
                group = m.groupdict()
                dropped = int(group['dropped'])
                nonce_collision = int(group['nonce_collision'])
                bad_xtr_nonce = int(group['bad_xtr_nonce'])
                ddt_itr_map = error_dict.setdefault('ddt_itr_map_requests',{})
                ddt_itr_map.update({'dropped':dropped,
                                    'nonce_collision':nonce_collision,
                                    'bad_xtr_nonce':bad_xtr_nonce})
                continue

            # Cache entries created/deleted:                    10/8
            m = p58.match(line)
            if m:
                group = m.groupdict()
                created = int(group['created'])
                deleted = int(group['deleted'])
                cache_dict = lisp_dict.setdefault('cache_related',{})
                cache_entries_dict = cache_dict.setdefault('cache_entries',{})
                cache_entries_dict.update({'created':created,
                                           'deleted':deleted})
                continue

            # NSF CEF replay entry count                        0
            m = p59.match(line)
            if m:
                group = m.groupdict()
                nsf_cef_replay_entry_count = int(group['nsf_cef_replay_entry_count'])
                cache_dict.update({'nsf_cef_replay_entry_count':nsf_cef_replay_entry_count})
                continue

            # Number of rejected EID-prefixes due to limit:     0
            m = p60.match(line)
            if m:
                group = m.groupdict()
                rejected_eid_prefix_due_to_limit = int(group['rejected_eid_prefix_due_to_limit'])
                cache_dict.update({'rejected_eid_prefix_due_to_limit':rejected_eid_prefix_due_to_limit})
                continue


            # Number of data signals processed:                 2 (+ dropped 0)
            m = p61.match(line)
            if m:
                group = m.groupdict()
                processed = int(group['processed'])
                dropped = int(group['dropped'])
                forwarding_dict = lisp_dict.setdefault('forwarding',{})
                data_signal_dict = forwarding_dict.setdefault('data_signals',{})
                data_signal_dict.update({'processed':processed,
                                         'dropped':dropped})
                continue

            # Number of reachability reports:                   0 (+ dropped 0)
            m = p62.match(line)
            if m:
                group = m.groupdict()
                count = int(group['count'])
                dropped = int(group['dropped'])
                reachability_dict = forwarding_dict.setdefault('reachability_reports',{})
                reachability_dict.update({'count':count,
                                         'dropped':dropped})
                continue

            # Number of SMR signals dropped:                    0
            m = p63.match(line)
            if m:
                group = m.groupdict()
                dropped = int(group['dropped'])
                smr_signal_dict = forwarding_dict.setdefault('smr_signals',{})
                smr_signal_dict.update({'dropped':dropped})
                continue

            # LISP RLOC Statistics - last cleared: never
            m = p64.match(line)
            if m:
                group = m.groupdict()
                last_cleared = group['last_cleared']
                rloc_stat_dict = lisp_dict.setdefault('rloc_statistics',{})
                rloc_stat_dict.update({'last_cleared':last_cleared})
                continue

            # RTR Map-Requests forwarded:                       0
            m = p65.match(line)
            if m:
                group = m.groupdict()
                map_requests_forwarded = int(group['map_requests_forwarded'])
                control_packets_dict = rloc_stat_dict.setdefault('control_packets',{})
                rtr_dict = control_packets_dict.setdefault('rtr',{})
                rtr_dict.update({'map_requests_forwarded':map_requests_forwarded})
                continue

            # RTR Map-Notifies forwarded:                       0
            m = p66.match(line)
            if m:
                group = m.groupdict()
                map_notifies_forwarded = int(group['map_notifies_forwarded'])
                rtr_dict.update({'map_notifies_forwarded':map_notifies_forwarded})
                continue

            # DDT-Map-Requests in/out:                          0/0
            m = p67.match(line)
            if m:
                group = m.groupdict()
                map_requests_in = int(group['in'])
                out = int(group['out'])
                ddt_dict = control_packets_dict.setdefault('ddt',{})
                map_requests_request = ddt_dict.setdefault('map_requests',{})
                map_requests_request.update({'in':map_requests_in,
                                             'out':out})
                continue

            # DDT-Map-Referrals in/out:                         0/0
            m = p68.match(line)
            if m:
                group = m.groupdict()
                map_requests_in = int(group['in'])
                out = int(group['out'])
                map_referral_request = ddt_dict.setdefault('map_referrals',{})
                map_referral_request.update({'in':map_requests_in,
                                             'out':out})
                continue

            # Map-Request format errors:                        0
            m = p69.match(line)
            if m:
                group = m.groupdict()
                map_request_format = int(group['map_request_format'])
                map_errors_dict = rloc_stat_dict.setdefault('errors',{})
                map_errors_dict.update({'map_request_format':map_request_format})
                continue

            # Map-Reply format errors:                          0
            m = p70.match(line)
            if m:
                group = m.groupdict()
                map_reply_format = int(group['map_reply_format'])
                map_errors_dict.update({'map_reply_format':map_reply_format})
                continue

            # Map-Referral format errors:                       0
            m = p71.match(line)
            if m:
                group = m.groupdict()
                map_referral = int(group['map_referral'])
                map_errors_dict.update({'map_referral':map_referral})
                continue

            # Invalid IP version drops:                         0
            m = p72.match(line)
            if m:
                group = m.groupdict()
                ip_version_drops = int(group['ip_version_drops'])
                misc_dict = lisp_dict.setdefault('misc_statistics',{})
                invalid_dict = misc_dict.setdefault('invalid',{})
                invalid_dict.update({'ip_version_drops':ip_version_drops})
                continue

            # Invalid IP header drops:                          0
            m = p73.match(line)
            if m:
                group = m.groupdict()
                ip_header_drops = int(group['ip_header_drops'])
                invalid_dict.update({'ip_header_drops':ip_header_drops})
                continue

            # Invalid IP proto field drops:                     0
            m = p74.match(line)
            if m:
                group = m.groupdict()
                ip_proto_field_drops = int(group['ip_proto_field_drops'])
                invalid_dict.update({'ip_proto_field_drops':ip_proto_field_drops})
                continue

            # Invalid packet size drops:                        0
            m = p75.match(line)
            if m:
                group = m.groupdict()
                packet_size_drops = int(group['packet_size_drops'])
                invalid_dict.update({'packet_size_drops':packet_size_drops})
                continue

            # Invalid LISP control port drops:                  0
            m = p76.match(line)
            if m:
                group = m.groupdict()
                lisp_control_port_drops = int(group['lisp_control_port_drops'])
                invalid_dict.update({'lisp_control_port_drops':lisp_control_port_drops})
                continue

            # Invalid LISP checksum drops:                      0
            m = p77.match(line)
            if m:
                group = m.groupdict()
                lisp_checksum_drops = int(group['lisp_checksum_drops'])
                invalid_dict.update({'lisp_checksum_drops':lisp_checksum_drops})
                continue

            # Unsupported LISP packet type drops:               0
            m = p78.match(line)
            if m:
                group = m.groupdict()
                unsupported_lisp_packet_drops = int(group['unsupported_lisp_packet_drops'])
                misc_dict.update({'unsupported_lisp_packet_drops':unsupported_lisp_packet_drops})
                continue

            # Unknown packet drops:                             0
            m = p79.match(line)
            if m:
                group = m.groupdict()
                unknown_packet_drops = int(group['unknown_packet_drops'])
                misc_dict.update({'unknown_packet_drops':unknown_packet_drops})
                continue
        return ret_dict



