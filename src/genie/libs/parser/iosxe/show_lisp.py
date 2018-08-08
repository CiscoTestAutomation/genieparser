''' show_lisp.py

IOSXE parsers for the following show commands:
    * show lisp session
    * show lisp platform
    * show lisp all extranet <extranet> instance-id <instance_id>
    * show lisp all instance-id <instance_id> dynamic-eid detail
    * show lisp all service ipv4
    * show lisp all service ipv6
    * show lisp all service ethernet
    * show lisp all instance-id <instance_id> ipv4
    * show lisp all instance-id <instance_id> ipv6
    * show lisp all instance-id <instance_id> ethernet
    * show lisp all instance-id <instance_id> ipv4 map-cache
    * show lisp all instance-id <instance_id> ipv6 map-cache
    * show lisp all instance-id <instance_id> ethernet map-cache
    * show lisp all instance-id <instance_id> ipv4 server rloc members
    * show lisp all instance-id <instance_id> ipv6 server rloc members
    * show lisp all instance-id <instance_id> ethernet server rloc members

    * show lisp all instance-id <instance_id> ipv4 smr
    * show lisp all instance-id <instance_id> ipv6 smr
    * show lisp all instance-id <instance_id> ethernet smr

    * show lisp all service ipv4 summary
    * show lisp all service ipv6 summary
    * show lisp all service ethernet summary

    * show lisp all instance-id <instance_id> ipv4 database
    * show lisp all instance-id <instance_id> ipv6 database
    * show lisp all instance-id <instance_id> ethernet database

    * show lisp all instance-id <instance_id> ipv4 server summary
    * show lisp all instance-id <instance_id> ipv6 server summary
    * show lisp all instance-id <instance_id> ethernet server summary

    * show lisp all instance-id <instance_id> ipv4 server detail internal
    * show lisp all instance-id <instance_id> ipv6 server detail internal
    * show lisp all instance-id <instance_id> ethernet server detail internal

    * show lisp all instance-id <instance_id> ipv4 statistics
    * show lisp all instance-id <instance_id> ipv6 statistics
    * show lisp all instance-id <instance_id> ethernet statistics
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional
from genie.libs.parser.utils.common import Common


# ==============================
# Schema for 'show lisp session'
# ==============================
class ShowLispSessionSchema(MetaParser):

    ''' Schema for "show lisp session" '''

    schema = {
        'vrf':
            {Any():
                {'sessions':
                    {'total': int,
                    'established': int,
                    'peers': 
                        {Any():
                            {'state': str,
                            'time': str,
                            'total_in': int,
                            'total_out': int,
                            'users': int,
                            },
                        },
                    },
                },
            },
        }


# ==============================
# Parser for 'show lisp session'
# ==============================
class ShowLispSession(ShowLispSessionSchema):

    ''' Parser for "show lisp session"'''

    def cli(self):

        # Execute command on device
        out = self.device.execute('show lisp session')

        # Init vars
        parsed_dict = {}

        # Sessions for VRF default, total: 3, established: 3
        p1 = re.compile(r'Sessions +for +VRF +(?P<vrf>(\S+)),'
                         ' +total: +(?P<total>(\d+)),'
                         ' +established: +(?P<established>(\d+))$')

        # Peer                           State      Up/Down        In/Out    Users
        # 2.2.2.2                        Up         00:51:38        8/13     3
        p2 = re.compile(r'(?P<peer>(\S+)) +(?P<state>(Up|Down)) +(?P<time>(\S+))'
                         ' +(?P<in>(\d+))\/(?P<out>(\d+)) +(?P<users>(\d+))$')

        for line in out.splitlines():
            line = line.strip()

            # Sessions for VRF default, total: 3, established: 3
            m = p1.match(line)
            if m:
                group = m.groupdict()
                vrf = group['vrf']
                vrf_dict = parsed_dict.setdefault('vrf', {}).\
                            setdefault(vrf, {}).setdefault('sessions', {})
                vrf_dict['total'] = int(group['total'])
                vrf_dict['established'] = int(group['established'])
                continue

            # 8.8.8.8                        Up         00:52:15        8/13     3
            m = p2.match(line)
            if m:
                group = m.groupdict()
                peer = group['peer']
                peer_dict = vrf_dict.setdefault('peers', {}).setdefault(peer, {})
                peer_dict['state'] = group['state'].lower()
                peer_dict['time'] = group['time']
                peer_dict['total_in'] = int(group['in'])
                peer_dict['total_out'] = int(group['out'])
                peer_dict['users'] = int(group['users'])
                continue

        return parsed_dict


# ===============================
# Schema for 'show lisp platform'
# ===============================
class ShowLispPlatformSchema(MetaParser):

    ''' Schema for "show lisp platform" '''

    schema = {
        'parallel_lisp_instance_limit': int,
        'rloc_forwarding_support':
            {'local':
                {'ipv4': str,
                'ipv6': str,
                'mac': str,
                },
            'remote':
                {'ipv4': str,
                'ipv6': str,
                'mac': str,
                },
            },
        'latest_supported_config_style': str,
        'current_config_style': str,
        }


# ==============================
# Parser for 'show lisp platform'
# ==============================
class ShowLispPlatform(ShowLispPlatformSchema):

    ''' Parser for "show lisp platform" '''

    def cli(self):

        # Execute command on device
        out = self.device.execute('show lisp platform')

        # Init vars
        parsed_dict = {}

        # Parallel LISP instance limit:      2000
        p1 = re.compile(r'Parallel +LISP +instance +limit: +(?P<limit>(\d+))$')

        # IPv4 RLOC, local:                 OK
        # IPv6 RLOC, local:                 OK
        # MAC RLOC, local:                  Unsupported
        p2 = re.compile(r'(?P<type>(IPv4|IPv6|MAC)) RLOC,'
                         ' +local: +(?P<local>(\S+))$')

        # IPv4 RLOC, remote:                OK
        # IPv6 RLOC, remote:                OK
        # MAC RLOC, remote:                 Unsupported
        p3 = re.compile(r'(?P<type>(IPv4|IPv6|MAC)) RLOC,'
                         ' +remote: +(?P<remote>(\S+))$')

        # Latest supported config style:     Service and instance
        p4 = re.compile(r'Latest +supported +config +style:'
                         ' +(?P<supported>([a-zA-Z\s]+))$')

        # Current config style:              Service and instance
        p5 = re.compile(r'Current +config +style:'
                         ' +(?P<current>([a-zA-Z\s]+))$')

        for line in out.splitlines():
            line = line.strip()

            # Parallel LISP instance limit:      2000
            m = p1.match(line)
            if m:
                parsed_dict['parallel_lisp_instance_limit'] = \
                    int(m.groupdict()['limit'])
                continue

            # IPv4 RLOC, local:                 OK
            # IPv6 RLOC, local:                 OK
            # MAC RLOC, local:                  Unsupported
            m = p2.match(line)
            if m:
                local_type = m.groupdict()['type'].lower()
                rloc_dict = parsed_dict.\
                            setdefault('rloc_forwarding_support', {}).\
                            setdefault('local', {})
                rloc_dict[local_type] = m.groupdict()['local'].lower()
                continue

            # IPv4 RLOC, remote:                 OK
            # IPv6 RLOC, remote:                 OK
            # MAC RLOC, remote:                  Unsupported
            m = p3.match(line)
            if m:
                remote_type = m.groupdict()['type'].lower()
                rloc_dict = parsed_dict.\
                            setdefault('rloc_forwarding_support', {}).\
                            setdefault('remote', {})
                rloc_dict[remote_type] = m.groupdict()['remote'].lower()
                continue

            # Latest supported config style:     Service and instance
            m = p4.match(line)
            if m:
                parsed_dict['latest_supported_config_style'] = \
                    m.groupdict()['supported'].lower()
                continue

            # Current config style:              Service and instance
            m = p5.match(line)
            if m:
                parsed_dict['current_config_style'] = \
                    m.groupdict()['current'].lower()
                continue

        return parsed_dict


# ========================================================================
# Schema for 'show lisp all extranet <extranet> instance-id <instance_id>'
# ========================================================================
class ShowLispExtranetSchema(MetaParser):

    ''' Schema for "show lisp all extranet <extranet> instance-id <instance_id>"'''

    schema = {
        'lisp_router_instances':
            {Any():
                {'service':
                    {Any():
                        {'map_server':
                            {'virtual_network_ids': 
                                {'total_extranet_entries': int,
                                Any():
                                    {'vni': str,
                                    'extranets':
                                        {Any():
                                            {'extranet': str,
                                            'home_instance_id': int,
                                            Optional('provider'):
                                                {Any():
                                                    {'eid_record': str,
                                                    'bidirectional': bool,
                                                    },
                                                },
                                            Optional('subscriber'):
                                                {Any():
                                                    {'eid_record': str,
                                                    'bidirectional': bool,
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
# Parser for 'show lisp all extranet <extranet> instance-id <instance_id>'
# ========================================================================
class ShowLispExtranet(ShowLispExtranetSchema):

    ''' Parser for "show lisp all extranet <extranet> instance-id <instance_id>"'''

    def cli(self, extranet, instance_id):

        # Execute command on device
        out = self.device.execute('show lisp all extranet {ext} instance-id {id}'.\
                                    format(ext=extranet,id=instance_id))

        # Init vars
        parsed_dict = {}

        # Output for router lisp 0
        p1 = re.compile(r'Output +for +router +lisp'
                         ' +(?P<lisp_router_id>(\S+))$')

        # Home Instance ID: 103
        p2 = re.compile(r'Home +Instance +ID *: +(?P<home_inst_id>(\d+))$')

        # Total entries: 6
        p3 = re.compile(r'Total +entries *: +(?P<total_entries>(\d+))$')

        # Provider/Subscriber  Inst ID    EID prefix
        # Provider             103        88.88.88.0/24
        # Subscriber           101        192.168.9.0/24
        p4 = re.compile(r'(?P<ext_type>(Provider|Subscriber)) +(?P<inst>(\d+))'
                         ' +(?P<eid>(\S+))$')

        for line in out.splitlines():
            line = line.strip()

            # Output for router lisp 0
            m = p1.match(line)
            if m:
                lisp_router_id = int(m.groupdict()['lisp_router_id'])
                lisp_dict = parsed_dict.setdefault('lisp_router_instances', {}).\
                            setdefault(lisp_router_id, {}).\
                            setdefault('service', {}).\
                            setdefault('ipv4', {}).setdefault('map_server', {})
                continue

            # Home Instance ID: 103
            m = p2.match(line)
            if m:
                home_instance_id = int(m.groupdict()['home_inst_id'])
                continue

            # Total entries: 6
            m = p3.match(line)
            if m:
                total_entries = int(m.groupdict()['total_entries'])
                continue

            # Provider/Subscriber  Inst ID    EID prefix
            # Provider             103        88.88.88.0/24
            # Subscriber           101        192.168.9.0/24
            m = p4.match(line)
            if m:
                group = m.groupdict()
                extranet_type = group['ext_type'].lower()
                type_eid = group['eid']
                inst = group['inst']
                # Create dict
                vni_dict = lisp_dict.setdefault('virtual_network_ids', {})
                # Set total count
                try:
                    vni_dict['total_extranet_entries'] = total_entries
                except:
                    pass
                # Instance
                vni_val_dict = vni_dict.setdefault(inst, {})
                vni_val_dict['vni'] = inst

                # Extranet dict
                ext_dict = vni_val_dict.setdefault('extranets', {}).\
                                setdefault(extranet, {})
                ext_dict['extranet'] = extranet
                try:
                    ext_dict['home_instance_id'] = home_instance_id
                except:
                    pass
                # Set extranet types
                if extranet_type not in ext_dict:
                    ext_dict[extranet_type] = {}
                if type_eid not in ext_dict[extranet_type]:
                    ext_dict[extranet_type][type_eid] = {}
                ext_dict[extranet_type][type_eid]['eid_record'] = \
                    m.groupdict()['eid']
                ext_dict[extranet_type][type_eid]['bidirectional'] = True
                continue

        return parsed_dict


# =======================================================================
# Schema for 'show lisp all instance-id <instance_id> dynamic-eid detail'
# =======================================================================
class ShowLispDynamicEidDetailSchema(MetaParser):

    ''' Schema for "show lisp all instance-id <instance_id> dynamic-eid detail" '''

    schema = {
        'lisp_router_instances':
            {Any():
                {'service':
                    {Any():
                        {'etr':
                            {'local_eids':
                                {Any():
                                    {'dynamic_eids':
                                        {Any():
                                            {'dynamic_eid_name': str,
                                            'id': str,
                                            'rlocs': str,
                                            Optional('registering_more_specific'): bool,
                                            Optional('loopback_address'): str,
                                            Optional('priority'): int,
                                            Optional('weight'): int,
                                            Optional('record_ttl'): int,
                                            Optional('site_based_multicast_map_notify_group'): str,
                                            Optional('proxy_reply'): bool,
                                            Optional('registration_interval'): int,
                                            Optional('global_map_server'): bool,
                                            Optional('num_of_roaming_dynamic_eid'): int,
                                            Optional('mapping_servers'):
                                                {Any():
                                                    {Optional('proxy_reply'): bool,
                                                    },
                                                },
                                            Optional('last_dynamic_eid'):
                                                {Any():
                                                    {'last_dynamic_eid_discovery_elaps_time': str,
                                                    'eids':
                                                        {Any():
                                                            {'interface': str,
                                                            'uptime': str,
                                                            'last_activity': str,
                                                            'discovered_by': str,
                                                            },
                                                        },
                                                    },
                                                },
                                            Optional('eid_address'):
                                                {Optional('address_type'): str,
                                                Optional('virtual_network_id'): str,
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


# =======================================================================
# Parser for 'show lisp all instance-id <instance_id> dynamic-eid detail'
# =======================================================================
class ShowLispDynamicEidDetail(ShowLispDynamicEidDetailSchema):

    ''' Parser for "show lisp all instance-id <instance_id> dynamic-eid detail"'''

    def cli(self, instance_id):

        # Execute command on device
        out = self.device.execute('show lisp all instance-id {} dynamic-eid '
                                  'detail'.format(instance_id))

        # Init vars
        parsed_dict = {}

        # Output for router lisp 0
        p1 = re.compile(r'Output +for +router +lisp'
                         ' +(?P<lisp_router_id>(\S+))$')

        # LISP Dynamic EID Information for VRF "red"
        p2 = re.compile(r'LISP +Dynamic +EID +Information +for +VRF'
                         ' +"(?P<vrf>(\S+))"$')

        # Dynamic-EID name: 192
        p3 = re.compile(r'Dynamic-EID +name: +(?P<eid_id>(\S+))$')

        # Database-mapping EID-prefix: 192.168.0.0/24, locator-set RLOC
        p4 = re.compile(r'Database-mapping +EID-prefix: +(?P<dyn_eid>(\S+)),'
                         ' +locator-set +(?P<locator_set_name>(\S+))$')

        # Registering more-specific dynamic-EIDs
        p5 = re.compile(r'Registering +more-specific +dynamic-EIDs$')

        # Map-Server(s): none configured, use global Map-Server
        p6 = re.compile(r'Map-Server\(s\)\: none configured, use global Map-Server$')

        # Map-Server(s): 4.4.4.4  (proxy-replying)
        # Map-Server(s): 6.6.6.6
        p6_1 = re.compile(r'Map-Server\(s\)\: +(?P<ms>([0-9\.\:]+))'
                           '(?: +\((?P<pr>(proxy-replying))\))?$')

        # Site-based multicast Map-Notify group: none configured
        # Site-based multicast Map-Notify group: 225.1.1.2
        p7 = re.compile(r'Site-based +multicast +Map-Notify +group\:'
                         ' +(?P<map_notify>([a-zA-Z0-9\s]+))$')

        # Number of roaming dynamic-EIDs discovered: 1
        p8 = re.compile(r'Number +of +roaming +dynamic-EIDs +discovered:'
                         ' +(?P<roam>(\d+))$')

        # Last dynamic-EID discovered: 192.168.0.1, 01:17:25 ago
        p9 = re.compile(r'Last +dynamic-EID +discovered: +(?P<last>(\S+)),'
                         ' +(?P<time>(\S+)) +ago$')

        # 192.168.0.1, GigabitEthernet5, uptime: 01:17:25
        p10 = re.compile(r'(?P<eid>([0-9\.\:]+)), +(?P<interface>(\S+)),'
                          ' +uptime: +(?P<uptime>(\S+))$')

        #   last activity: 00:00:23, discovered by: Packet Reception
        p11 = re.compile(r'last +activity: +(?P<last>(\S+)), +discovered +by:'
                          ' +(?P<discovered_by>([a-zA-Z\s]+))$')

        for line in out.splitlines():
            line = line.strip()

            # Output for router lisp 0
            m = p1.match(line)
            if m:
                lisp_router_id = int(m.groupdict()['lisp_router_id'])
                lisp_dict = parsed_dict.setdefault(
                    'lisp_router_instances', {}).setdefault(lisp_router_id, {})
                continue

            # LISP Dynamic EID Information for VRF "red"
            m = p2.match(line)
            if m:
                eid_vrf = m.groupdict()['vrf']
                continue

            # Dynamic-EID name: 192
            m = p3.match(line)
            if m:
                dynamic_eid_name = m.groupdict()['eid_id']
                continue

            # Database-mapping EID-prefix: 192.168.0.0/24, locator-set RLOC
            m = p4.match(line)
            if m:
                group = m.groupdict()
                dyn_eid = group['dyn_eid']
                dynamic_eids_dict = lisp_dict.setdefault('service', {}).\
                                    setdefault('ipv4', {}).\
                                    setdefault('etr', {}).\
                                    setdefault('local_eids', {}).\
                                    setdefault(instance_id, {}).\
                                    setdefault('dynamic_eids', {}).\
                                    setdefault(dyn_eid, {})
                
                # Set values
                dynamic_eids_dict['dynamic_eid_name'] =  dynamic_eid_name
                dynamic_eids_dict['id'] =  dyn_eid
                dynamic_eids_dict['rlocs'] = group['locator_set_name']
                if 'eid_address' not in dynamic_eids_dict:
                    dynamic_eids_dict['eid_address'] = {}
                try:
                    dynamic_eids_dict['eid_address']['virtual_network_id'] = eid_vrf
                except:
                    pass
                continue

            # Registering more-specific dynamic-EIDs
            m = p5.match(line)
            if m:
                dynamic_eids_dict['registering_more_specific'] = True
                continue

            # Map-Server(s): none configured, use global Map-Server
            m = p6.match(line)
            if m:
                dynamic_eids_dict['global_map_server'] = True
                continue

            # Map-Server(s): 4.4.4.4  (proxy-replying)
            # Map-Server(s): 6.6.6.6
            m = p6_1.match(line)
            if m:
                group = m.groupdict()
                mapserver = group['ms']
                ms_dict = dynamic_eids_dict.setdefault('mapping_servers', {}).\
                          setdefault(mapserver, {})
                if group['pr']:
                    ms_dict['proxy_reply'] = True
                continue

            # Site-based multicast Map-Notify group: none configured
            # Site-based multicast Map-Notify group: 225.1.1.2
            m = p7.match(line)
            if m:
                dynamic_eids_dict['site_based_multicast_map_notify_group'] = \
                    m.groupdict()['map_notify']
                continue

            # Number of roaming dynamic-EIDs discovered: 1
            m = p8.match(line)
            if m:
                dynamic_eids_dict['num_of_roaming_dynamic_eid'] = int(m.groupdict()['roam'])

            # Last dynamic-EID discovered: 192.168.0.1, 01:17:25 ago
            m = p9.match(line)
            if m:
                group = m.groupdict()
                last_eid = group['last']
                time = group['time']
                # Create dict
                last_dyn_dict = dynamic_eids_dict.\
                                    setdefault('last_dynamic_eid', {}).\
                                    setdefault(last_eid, {})
                last_dyn_dict['last_dynamic_eid_discovery_elaps_time'] = time
                continue

            # 192.168.0.1, GigabitEthernet5, uptime: 01:17:25
            m = p10.match(line)
            if m:
                group = m.groupdict()
                eid = group['eid']
                interface = group['interface']
                uptime = group['uptime']
                last_eids_dict = last_dyn_dict.setdefault('eids', {}).\
                                    setdefault(eid, {})
                last_eids_dict['interface'] = interface
                last_eids_dict['uptime'] = uptime
                continue

            # last activity: 00:00:23, discovered by: Packet Reception
            m = p11.match(line)
            if m:
                group = m.groupdict()
                last_activity = group['last']
                discovered_by = group['discovered_by'].lower()
                last_eids_dict['last_activity'] = last_activity
                last_eids_dict['discovered_by'] = discovered_by
                continue

        return parsed_dict


# ==============================================================
# Schema for 'show lisp all instance-id <instance_id> <service>'
# ==============================================================
class ShowLispServiceSchema(MetaParser):

    '''Schema for "show lisp all instance-id <instance_id> <service>" '''

    schema = {
        'lisp_router_instances':
            {Any():
                {'lisp_router_instance_id': int,
                'lisp_router_id':
                    {'site_id': str,
                    'xtr_id': str,
                    },
                'service':
                    {Any():
                        {'service': str,
                        'delegated_database_tree': bool,
                        'locator_table': str,
                        'mobility_first_hop_router': bool,
                        'nat_traversal_router': bool,
                        'instance_id':
                            {Any():
                                {Optional('eid_table'): str,
                                Optional('site_registration_limit'): int,
                                Optional('map_request_source'): str,
                                'database':
                                    {Optional('dynamic_database_limit'): int,
                                    Optional('dynamic_database_size'): int,
                                    Optional('inactive_deconfig_away_size'): int,
                                    Optional('route_import_database_limit'): int,
                                    Optional('route_import_database_size'): int,
                                    Optional('static_database_size'): int,
                                    Optional('static_database_limit'): int,
                                    Optional('total_database_mapping_size'): int,
                                    Optional('dynamic_database_mapping_limit'): int,
                                    Optional('import_site_db_size'): int,
                                    Optional('import_site_db_limit'): int,
                                    Optional('proxy_db_size'): int,
                                    },
                                'mapping_servers':
                                    {Any():
                                        {'ms_address': str,
                                        Optional('uptime'): str,
                                        },
                                    },
                                'itr':
                                    {'local_rloc_last_resort': str,
                                    Optional('use_proxy_etr_rloc'): str,
                                    },
                                'map_cache':
                                    {Optional('imported_route_count'): int,
                                    Optional('imported_route_limit'): int,
                                    Optional('map_cache_size'): int,
                                    Optional('persistent_map_cache'): bool,
                                    Optional('static_mappings_configured'): int,
                                    },
                                },
                            },
                        'etr':
                            {'enabled': bool,
                            Optional('encapsulation'): str,
                            'proxy_etr_router': bool,
                            'accept_mapping_data': str,
                            'map_cache_ttl': str,
                            'mapping_servers':
                                {Any():
                                    {'ms_address': str,
                                    Optional('uptime'): str,
                                    },
                                },
                            },
                        'itr':
                            {'enabled': bool,
                            'proxy_itr_router': bool,
                            'solicit_map_request': str,
                            'max_smr_per_map_cache_entry': str,
                            'multiple_smr_suppression_time': int,
                            'map_resolvers':
                                {Any():
                                    {'map_resolver': str,
                                    },
                                },
                            },
                        'locator_status_algorithms':
                            {'rloc_probe_algorithm': bool,
                            'rloc_probe_on_route_change': str,
                            'rloc_probe_on_member_change': bool,
                            'lsb_reports': str,
                            'ipv4_rloc_min_mask_len': int,
                            'ipv6_rloc_min_mask_len': int,
                            },
                        'map_cache':
                            {'map_cache_activity_check_period': int,
                            Optional('map_cache_fib_updates'): str,
                            'map_cache_limit': int,
                            },
                        'map_server':
                            {'enabled': bool,
                            },
                        'map_resolver':
                            {'enabled': bool,
                            },
                        Optional('source_locator_configuration'):
                            {'vlans':
                                {Any():
                                    {'address': str,
                                    'interface': str,
                                    },
                                },
                            },
                        },
                    },
                },
            },
        }


# ==============================================================
# Parser for 'show lisp all instance-id <instance_id> <service>'
# ==============================================================
class ShowLispService(ShowLispServiceSchema):

    '''Parser for "show lisp all instance-id <instance_id> <service>"'''

    def cli(self, service, instance_id=None):

        assert service in ['ipv4', 'ipv6', 'ethernet']

        # Build the command
        cmd = 'show lisp all'
        if instance_id:
            cmd += ' instance-id {}'.format(instance_id)
        cmd += ' service {}'.format(service)
        
        # Execute command on device
        out = self.device.execute(cmd)

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

        # Instance ID: 101
        p2 = re.compile(r'Instance +ID *: +(?P<instance_id>(\d+))$')

        # Router-lisp ID:                      0
        p3 = re.compile(r'Router-lisp +ID *: +(?P<router_id>(\d+))$')

        # Locator table:                       default
        p4 = re.compile(r'Locator +table *: +(?P<locator_table>(\S+))$')

        # EID table:                           vrf red
        p5 = re.compile(r'EID +table *: +(?P<eid_table>[a-zA-Z0-9\s]+)$')

        # Ingress Tunnel Router (ITR):         enabled
        # Egress Tunnel Router (ETR):          enabled
        p6 = re.compile(r'(Ingress|Egress) +Tunnel +Router '
                         '+\((?P<type>(ITR|ETR))\) *: '
                         '+(?P<state>(enabled|disabled))$')

        # Proxy-ITR Router (PITR):             disabled
        # Proxy-ETR Router (PETR):             disabled
        p7 = re.compile(r'Proxy\-(ITR|ETR) +Router'
                         ' +\((?P<proxy_type>(PITR|PETR))\) *:'
                         ' +(?P<state>(enabled|disabled))$')

        # NAT-traversal Router (NAT-RTR):      disabled
        p8 = re.compile(r'NAT-traversal +Router +\(NAT\-RTR\) *:'
                         ' +(?P<state>(enabled|disabled))$')
        
        # Mobility First-Hop Router:           disabled
        p9 = re.compile(r'Mobility +First-Hop +Router *:'
                          ' +(?P<state>(enabled|disabled))$')

        # Map Server (MS):                     disabled
        p10 = re.compile(r'Map +Server +\(MS\) *:'
                          ' +(?P<state>(enabled|disabled))$')

        # Map Resolver (MR):                   disabled
        p11 = re.compile(r'Map +Resolver +\(MR\) *:'
                          ' +(?P<state>(enabled|disabled))$')

        # Delegated Database Tree (DDT):       disabled
        p12 = re.compile(r'Delegated +Database +Tree +\(DDT\) *:'
                          ' +(?P<state>(enabled|disabled))$')

        # Site Registration Limit:             0
        p13 = re.compile(r'Site +Registration +Limit *: +(?P<limit>(\d+))$')

        # Map-Request source:                  derived from EID destination
        p14 = re.compile(r'Map-Request +source *: +(?P<source>(.*))$')

        # ITR Map-Resolver(s):                 4.4.4.4, 13.13.13.13
        p15 = re.compile(r'ITR +Map\-Resolver\(s\) *: +(?P<resolvers>(.*))$')

        #                                      66.66.66.66 *** not reachable ***
        p15_1 = re.compile(r'(?P<resolver>([0-9\.\:]+))(?: +\*.*)?$')

        # ETR Map-Server(s):                   4.4.4.4 (17:49:58), 13.13.13.13 (00:00:35)
        p16 = re.compile(r'ETR +Map\-Server\(s\) *: +(?P<servers>(.*))$')
 
        #                                      66.66.66.66 (never)
        p16_1 = re.compile(r'(?P<server>([0-9\.\:]+))(?: +\((?P<uptime>(\S+))\))?$')

        # xTR-ID:                              0x730E0861-0x12996F6D-0xEFEA2114-0xE1C951F7
        p17 = re.compile(r'xTR-ID *: +(?P<xtr_id>(\S+))$')

        # site-ID:                             unspecified
        p18 = re.compile(r'site-ID *: +(?P<site_id>(\S+))$')

        # ITR local RLOC (last resort):        2.2.2.2
        # ITR local RLOC (last resort):        *** NOT FOUND ***
        p19 = re.compile(r'ITR +local +RLOC +\(last +resort\) *: +(?P<val>(.*))$')

        # ITR use proxy ETR RLOC(s):           10.10.10.10
        p20 = re.compile(r'ITR +use +proxy +ETR +RLOC\(s\) *: +(?P<val>(\S+))$')

        # ITR Solicit Map Request (SMR):       accept and process
        p21 = re.compile(r'ITR +Solicit +Map +Request +\(SMR\) *: +(?P<val>(.*))$')

        # Max SMRs per map-cache entry:      8 more specifics
        p22 = re.compile(r'Max +SMRs +per +map-cache +entry *: +(?P<val>(.*))$')

        # Multiple SMR suppression time:     20 secs
        p23 = re.compile(r'Multiple +SMR +suppression +time *: +(?P<time>(\d+))'
                          ' +secs$')

        # ETR accept mapping data:             disabled, verify disabled
        p24 = re.compile(r'ETR +accept +mapping +data *: +(?P<val>(.*))$')

        # ETR map-cache TTL:                   1d00h
        p25 = re.compile(r'ETR +map-cache +TTL *: +(?P<val>(\S+))$')

        # Locator Status Algorithms:
        p26 = re.compile(r'Locator +Status +Algorithms *:$')

        # RLOC-probe algorithm:              disabled
        p27 = re.compile(r'RLOC\-probe +algorithm *:'
                          ' +(?P<state>(enabled|disabled))$')

        # RLOC-probe on route change:        N/A (periodic probing disabled)
        p28 = re.compile(r'RLOC\-probe +on +route +change *: +(?P<state>(.*))$')

        # RLOC-probe on member change:       disabled
        p29 = re.compile(r'RLOC\-probe +on +member +change *:'
                          ' +(?P<state>(enabled|disabled))$')

        # LSB reports:                       process
        p30 = re.compile(r'LSB +reports *: +(?P<lsb_report>(\S+))$')

        # IPv4 RLOC minimum mask length:     /0
        p31 = re.compile(r'IPv4 +RLOC +minimum +mask +length *:'
                          ' +\/(?P<ipv4_mask_len>(\d+))$')

        # IPv6 RLOC minimum mask length:     /0
        p32 = re.compile(r'IPv6 +RLOC +minimum +mask +length *:'
                          ' +\/(?P<ipv6_mask_len>(\d+))$')

        # Map-cache:
        p33 = re.compile(r'Map\-cache:$')

        # Static mappings configured:        0
        p34 = re.compile(r'Static +mappings +configured *: +(?P<static>(\d+))$')

        # Map-cache size/limit:              2/1000
        p35 = re.compile(r'Map\-cache +size\/+limit *:'
                          ' +(?P<size>(\d+))\/(?P<limit>(\d+))$')

        # Map-cache limit:                   5120
        p35_1 = re.compile(r'Map\-cache +limit *: +(?P<limit>(\d+))$')

        # Imported route count/limit:        0/1000
        p36 = re.compile(r'Imported +route +count\/limit *:'
                          ' +(?P<count>(\d+))\/(?P<limit>(\d+))$')

        # Map-cache activity check period:   60 secs
        p37 = re.compile(r'Map-cache +activity +check +period *:'
                          ' +(?P<period>(\d+)) +secs$')

        # Map-cache FIB updates:             established
        p38 = re.compile(r'Map\-cache +FIB +updates *: +(?P<fib_updates>(.*))$')

        # Persistent map-cache:              disabled
        p39 = re.compile(r'Persistent +map\-cache *:'
                          ' +(?P<state>(enabled|disabled))$')

        # Source locator configuration:
        p40 = re.compile(r'Source +locator +configuration:$')

        #   Vlan100: 11.11.11.1 (Loopback0)
        p41 = re.compile(r'Vlan(?P<vlan>(\d+))\: +(?P<address>([0-9\.\:]+))'
                          ' +\((?P<intf>(\S+))\)$')

        # Database:
        p42 = re.compile(r'Database *:$')

        # Total database mapping size:       1
        p43 = re.compile(r'Total +database +mapping +size *:'
                          ' +(?P<map_size>(\d+))$')

        # Dynamic database mapping limit:    5120
        p44 = re.compile(r'Dynamic +database +mapping +limit *:'
                          ' +(?P<map_limit>(\d+))$')

        # static database size/limit:        1/65535
        p45 = re.compile(r'static +database +size\/+limit *:'
                          ' +(?P<size>(\d+))\/(?P<limit>(\d+))$')

        # dynamic database size/limit:       0/65535
        p46 = re.compile(r'dynamic +database +size\/+limit *:'
                          ' +(?P<size>(\d+))\/(?P<limit>(\d+))$')

        # route-import database size/limit:  0/1000
        p47 = re.compile(r'route\-import +database +size\/+limit *:'
                          ' +(?P<size>(\d+))\/(?P<limit>(\d+))$')

        # Inactive (deconfig/away) size:     0
        p48 = re.compile(r'Inactive +\(deconfig\/away\) +size *:'
                          ' +(?P<inactive>(\d+))$')

        # import-site-reg database size/limit0/65535
        p49 = re.compile(r'import\-site\-reg +database +size\/limit *:?'
                          ' *(?P<size>(\d+))\/(?P<limit>(\d+))$')
        
        # proxy database size:               0
        p50 = re.compile(r'proxy +database +size *: +(?P<size>(\d+))$')

        # Encapsulation type:                  lisp
        p51 = re.compile(r'Encapsulation +type *:'
                          ' +(?P<encap_type>(lisp|vxlan))$')

        for line in out.splitlines():
            line = line.strip()

            # Output for router lisp 0
            # Output for router lisp 0 instance-id 193
            m = p1.match(line)
            if m:
                lisp_router_id = int(m.groupdict()['router_id'])
                # Set value of instance_id if parsed, else take user input
                if m.groupdict()['instance_id']:
                    instance_id = m.groupdict()['instance_id']
                continue

            # Instance ID: 101
            m = p2.match(line)
            if m:
                instance_id = m.groupdict()['instance_id']
                continue

            # Router-lisp ID:                      0
            m = p3.match(line)
            if m:
                lisp_dict = parsed_dict.setdefault('lisp_router_instances', {}).\
                            setdefault(lisp_router_id, {})
                lisp_dict['lisp_router_instance_id'] = lisp_router_id
                # Create service dict
                service_dict = lisp_dict.setdefault('service', {}).\
                                   setdefault(service, {})
                service_dict['service'] = service
                # Create instance_id dict
                iid_dict = service_dict.setdefault('instance_id', {}).\
                            setdefault(instance_id, {})
                continue

            # Locator table:                       default
            m = p4.match(line)
            if m:
                service_dict['locator_table'] = m.groupdict()['locator_table']
                continue

            # EID table:                           vrf red
            m = p5.match(line)
            if m:
                iid_dict['eid_table'] = m.groupdict()['eid_table']
                continue

            # Ingress Tunnel Router (ITR):         enabled
            # Egress Tunnel Router (ETR):          enabled
            m = p6.match(line)
            if m:
                tunnel_type = m.groupdict()['type'].lower()
                if tunnel_type == 'itr':
                    itr_dict = service_dict.setdefault('itr', {})
                    itr_dict['enabled'] = state_dict[m.groupdict()['state']]
                elif tunnel_type == 'etr':
                    etr_dict = service_dict.setdefault('etr', {})
                    etr_dict['enabled'] = state_dict[m.groupdict()['state']]
                continue

            # Proxy-ITR Router (PITR):             disabled
            # Proxy-ETR Router (PETR):             disabled
            m = p7.match(line)
            if m:
                proxy_type = m.groupdict()['proxy_type'].lower()
                if proxy_type == 'pitr':
                    itr_dict['proxy_itr_router'] = \
                        state_dict[m.groupdict()['state']]
                elif proxy_type == 'petr':
                    etr_dict['proxy_etr_router'] = \
                        state_dict[m.groupdict()['state']]
                continue

            # NAT-traversal Router (NAT-RTR):      disabled
            m = p8.match(line)
            if m:
                service_dict['nat_traversal_router'] = \
                    state_dict[m.groupdict()['state']]
                continue

            # Mobility First-Hop Router:           disabled
            m = p9.match(line)
            if m:
                service_dict['mobility_first_hop_router'] = \
                    state_dict[m.groupdict()['state']]
                continue

            # Map Server (MS):                     disabled
            m = p10.match(line)
            if m:
                map_server_dict = service_dict.setdefault('map_server', {})
                map_server_dict['enabled'] = state_dict[m.groupdict()['state']]
                continue

            # Map Resolver (MR):                   disabled
            m = p11.match(line)
            if m:
                map_resolver_dict = service_dict.setdefault('map_resolver', {})
                map_resolver_dict['enabled'] = state_dict[m.groupdict()['state']]
                continue

            # Delegated Database Tree (DDT):       disabled
            m = p12.match(line)
            if m:
                service_dict['delegated_database_tree'] = \
                    state_dict[m.groupdict()['state']]
                continue

            # Site Registration Limit:             0
            m = p13.match(line)
            if m:
                iid_dict['site_registration_limit'] = int(m.groupdict()['limit'])
                continue

            # Map-Request source:                  derived from EID destination
            m = p14.match(line)
            if m:
                iid_dict['map_request_source'] = m.groupdict()['source']
                continue

            # ITR Map-Resolver(s):                 4.4.4.4, 13.13.13.13
            m = p15.match(line)
            if m:
                map_resolvers = m.groupdict()['resolvers'].split(',')
                for mr in map_resolvers:
                    itr_mr_dict = itr_dict.setdefault('map_resolvers', {}).\
                                    setdefault(mr.strip(), {})
                    itr_mr_dict['map_resolver'] = mr.strip()
                continue

            m = p15_1.match(line)
            if m:
                itr_dict['map_resolvers'].setdefault(
                    m.groupdict()['resolver'], {})['map_resolver'] = \
                    m.groupdict()['resolver']
                continue

            # ETR Map-Server(s):                   4.4.4.4 (17:49:58), 13.13.13.13 (00:00:35)
            m = p16.match(line)
            if m:
                map_servers = m.groupdict()['servers'].split(',')
                for ms in map_servers:
                    try:
                        map_server, uptime = ms.split()
                        map_server = map_server.replace(' ', '')
                        uptime = uptime.replace('(', '').replace(')', '')
                    except:
                        map_server = ms.replace(' ', '')
                        uptime = None
                    # Set etr_dict under service
                    etr_ms_dict = etr_dict.setdefault('mapping_servers', {}).\
                                    setdefault(map_server, {})
                    etr_ms_dict['ms_address'] = map_server
                    if uptime:
                        etr_ms_dict['uptime'] = uptime
                    # Set etr_dict under instance_id
                    iid_ms_dict = iid_dict.setdefault('mapping_servers', {}).\
                                        setdefault(map_server, {})
                    iid_ms_dict['ms_address'] = map_server
                    if uptime:
                        iid_ms_dict['uptime'] = uptime
                continue

            #                                  66.66.66.66 (never)
            m = p16_1.match(line)
            if m:
                temp1 = etr_dict['mapping_servers'].setdefault(
                            m.groupdict()['server'], {})
                temp2 = iid_dict['mapping_servers'].setdefault(
                            m.groupdict()['server'], {})
                temp1['ms_address'] =  m.groupdict()['server']
                temp2['ms_address'] =  m.groupdict()['server']
                if m.groupdict()['uptime']:
                    temp1['uptime'] = m.groupdict()['uptime']
                    temp2['uptime'] = m.groupdict()['uptime']
                continue

            # xTR-ID:                              0x730E0861-0x12996F6D-0xEFEA2114-0xE1C951F7
            m = p17.match(line)
            if m:
                lrouterid_dict = lisp_dict.setdefault('lisp_router_id', {})
                lrouterid_dict['xtr_id'] = m.groupdict()['xtr_id']
                continue

            # site-ID:                             unspecified
            m = p18.match(line)
            if m:
                lrouterid_dict['site_id'] = m.groupdict()['site_id']
                continue

            # ITR local RLOC (last resort):        2.2.2.2
            m = p19.match(line)
            if m:
                iid_itr_dict = iid_dict.setdefault('itr', {})
                iid_itr_dict['local_rloc_last_resort'] = m.groupdict()['val']
                continue

            # ITR use proxy ETR RLOC(s):           10.10.10.10
            m = p20.match(line)
            if m:
                iid_itr_dict['use_proxy_etr_rloc'] = m.groupdict()['val']
                continue

            # ITR Solicit Map Request (SMR):       accept and process
            m = p21.match(line)
            if m:
                itr_dict['solicit_map_request'] = m.groupdict()['val']
                continue

            #   Max SMRs per map-cache entry:      8 more specifics
            m = p22.match(line)
            if m:
                itr_dict['max_smr_per_map_cache_entry'] = m.groupdict()['val']
                continue

            #   Multiple SMR suppression time:     20 secs
            m = p23.match(line)
            if m:
                itr_dict['multiple_smr_suppression_time'] = \
                    int(m.groupdict()['time'])
                continue

            # ETR accept mapping data:             disabled, verify disabled
            m = p24.match(line)
            if m:
                etr_dict['accept_mapping_data'] = m.groupdict()['val']
                continue

            # ETR map-cache TTL:                   1d00h
            m = p25.match(line)
            if m:
                etr_dict['map_cache_ttl'] = m.groupdict()['val']
                continue

            # Locator Status Algorithms:
            m = p26.match(line)
            if m:
                locator_dict = service_dict.\
                                setdefault('locator_status_algorithms', {})
                continue

            #   RLOC-probe algorithm:              disabled
            m = p27.match(line)
            if m:
                locator_dict['rloc_probe_algorithm'] = \
                    state_dict[m.groupdict()['state']]
                continue

            #   RLOC-probe on route change:        N/A (periodic probing disabled)
            m = p28.match(line)
            if m:
                locator_dict['rloc_probe_on_route_change'] = \
                    m.groupdict()['state']
                continue

            #   RLOC-probe on member change:       disabled
            m = p29.match(line)
            if m:
                locator_dict['rloc_probe_on_member_change'] = \
                    state_dict[m.groupdict()['state']]
                continue

            #   LSB reports:                       process
            m = p30.match(line)
            if m:
                locator_dict['lsb_reports'] = m.groupdict()['lsb_report']
                continue

            #   IPv4 RLOC minimum mask length:     /0
            m = p31.match(line)
            if m:
                locator_dict['ipv4_rloc_min_mask_len'] = \
                    int(m.groupdict()['ipv4_mask_len'])
                continue

            #   IPv6 RLOC minimum mask length:     /0
            m = p32.match(line)
            if m:
                locator_dict['ipv6_rloc_min_mask_len'] = \
                    int(m.groupdict()['ipv6_mask_len'])
                continue

            # Map-cache:
            m = p33.match(line)
            if m:
                map_cache_dict = service_dict.setdefault('map_cache', {})
                iid_map_cache_dict = iid_dict.setdefault('map_cache', {})
                continue

            #   Static mappings configured:        0
            m = p34.match(line)
            if m:
                iid_map_cache_dict['static_mappings_configured'] = \
                    int(m.groupdict()['static'])
                continue

            #   Map-cache size/limit:              2/1000
            m = p35.match(line)
            if m:
                iid_map_cache_dict['map_cache_size'] = int(m.groupdict()['size'])
                map_cache_dict['map_cache_limit'] = int(m.groupdict()['limit'])
                continue

            #   Map-cache limit:              5120
            m = p35_1.match(line)
            if m:
                map_cache_dict['map_cache_limit'] = int(m.groupdict()['limit'])
                continue

            #   Imported route count/limit:        0/1000
            m = p36.match(line)
            if m:
                iid_map_cache_dict['imported_route_count'] = \
                    int(m.groupdict()['count'])
                iid_map_cache_dict['imported_route_limit'] = \
                    int(m.groupdict()['limit'])
                continue

            #   Map-cache activity check period:   60 secs
            m = p37.match(line)
            if m:
                map_cache_dict['map_cache_activity_check_period'] = \
                    int(m.groupdict()['period'])
                continue

            #   Map-cache FIB updates:             established
            m = p38.match(line)
            if m:
                map_cache_dict['map_cache_fib_updates'] = \
                    m.groupdict()['fib_updates']
                continue

            #   Persistent map-cache:              disabled
            m = p39.match(line)
            if m:
                iid_map_cache_dict['persistent_map_cache'] = \
                    state_dict[m.groupdict()['state']]
                continue

            # Source locator configuration:
            m = p40.match(line)
            if m:
                src_locator_dict = service_dict.setdefault(
                                    'source_locator_configuration', {})
                continue

            #   Vlan100: 11.11.11.1 (Loopback0)
            #   Vlan101: 11.11.11.1 (Loopback0)
            m = p41.match(line)
            if m:
                vlan = 'vlan' + m.groupdict()['vlan']
                src_locator_vlan_dict = src_locator_dict.setdefault(
                    'vlans', {}).setdefault(vlan, {})
                src_locator_vlan_dict['address'] = m.groupdict()['address']
                src_locator_vlan_dict['interface'] = m.groupdict()['intf']
                continue

            # Database:   
            m = p42.match(line)
            if m:
                db_dict = iid_dict.setdefault('database', {})
                continue

            #   Total database mapping size:       1
            m = p43.match(line)
            if m:
                db_dict['total_database_mapping_size'] = \
                    int(m.groupdict()['map_size'])
                continue

            # Dynamic database mapping limit:    5120
            m = p44.match(line)
            if m:
                db_dict['dynamic_database_mapping_limit'] = \
                    int(m.groupdict()['map_limit'])
                continue

            #   static database size/limit:        1/65535
            m = p45.match(line)
            if m:
                db_dict['static_database_size'] = int(m.groupdict()['size'])
                db_dict['static_database_limit'] = int(m.groupdict()['limit'])
                continue

            #   dynamic database size/limit:       0/65535
            m = p46.match(line)
            if m:
                db_dict['dynamic_database_size'] = int(m.groupdict()['size'])
                db_dict['dynamic_database_limit'] = int(m.groupdict()['limit'])
                continue

            #   route-import database size/limit:  0/1000
            m = p47.match(line)
            if m:
                db_dict['route_import_database_size'] = \
                    int(m.groupdict()['size'])
                db_dict['route_import_database_limit'] = \
                    int(m.groupdict()['limit'])
                continue

            #   Inactive (deconfig/away) size:     0
            m = p48.match(line)
            if m:
                db_dict['inactive_deconfig_away_size'] = \
                    int(m.groupdict()['inactive'])
                continue

            # import-site-reg database size/limit0/65535
            m = p49.match(line)
            if m:
                db_dict['import_site_db_size'] = int(m.groupdict()['size'])
                db_dict['import_site_db_limit'] = int(m.groupdict()['limit'])
                continue
        
            # proxy database size:               0
            m = p50.match(line)
            if m:
                db_dict['proxy_db_size'] = int(m.groupdict()['size'])
                continue

            # Encapsulation type:                  lisp
            m = p51.match(line)
            if m:
                etr_dict['encapsulation'] = m.groupdict()['encap_type']
                continue

        return parsed_dict


# ========================================================================
# Schema for 'show lisp all instance-id <instance_id> <service> map-cache'
# ========================================================================
class ShowLispServiceMapCacheSchema(MetaParser):

    '''Schema for "show lisp all instance-id <instance_id> <service> map-cache" '''

    schema = {
        'lisp_router_instances':
            {Any():
                {'lisp_router_instance_id': int,
                'service':
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
                                            'uptime': str,
                                            'expires': str,
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
                                            Optional('positive_mapping'):
                                                {'rlocs':
                                                    {Any():
                                                        {'id': str,
                                                        'locator_address':
                                                            {'address_type': str,
                                                            'virtual_network_id': str,
                                                            'uptime': str,
                                                            'state': str,
                                                            'priority': int,
                                                            'weight': int,
                                                            Optional('encap_iid'): str,
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

    def cli(self, service, instance_id):

        assert service in ['ipv4', 'ipv6', 'ethernet']

        # Execute command on device
        out = self.device.execute('show lisp all instance-id {instance_id}'
                                    ' service {service} map-cache'.\
                            format(instance_id=instance_id, service=service))

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

        # LISP IPv4 Mapping Cache for EID-table vrf red (IID 101), 2 entries
        # LISP IPv6 Mapping Cache for EID-table vrf red (IID 101), 2 entries
        # LISP MAC Mapping Cache for EID-table Vlan 101 (IID 1), 4 entries
        p2 = re.compile(r'LISP +(?P<type>(IPv4|IPv6|MAC)) +Mapping +Cache +for'
                         ' +EID\-table +(vrf|Vlan) +(?P<vrf>([a-zA-Z0-9\s]+))'
                         ' +\(IID +(?P<iid>(\d+))\), +(?P<entries>(\d+))'
                         ' +entries$')

        # 0.0.0.0/0, uptime: 15:23:50, expires: never, via static-send-map-request
        # ::/0, uptime: 00:11:28, expires: never, via static-send-map-request
        # b827.eb51.f5ce/48, uptime: 22:49:42, expires: 01:10:17, via WLC Map-Notify, complete
        # 192.168.9.0/24, uptime: 00:04:02, expires: 23:55:57, via map-reply, complete
        p3 = re.compile(r'(?P<map_id>(\S+)), +uptime: +(?P<uptime>(\S+)),'
                         ' +expires: +(?P<expires>(\S+)), +via +(?P<via>(.*))$')

        #   Negative cache entry, action: send-map-request
        p4 = re.compile(r'Negative +cache +entry, +action: +(?P<action>(.*))$')

        #   Locator  Uptime    State      Pri/Wgt     Encap-IID
        #   8.8.8.8  00:04:02  up          50/50        -
        p5 = re.compile(r'(?P<locator>(\S+)) +(?P<uptime>(\S+))'
                         ' +(?P<state>(up|down))'
                         ' +(?P<priority>(\d+))\/(?P<weight>(\d+))'
                         '(?: +(?P<encap_iid>(\S+)))?$')

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

            # LISP IPv4 Mapping Cache for EID-table vrf red (IID 101), 2 entries
            # LISP IPv6 Mapping Cache for EID-table vrf red (IID 101), 2 entries
            # LISP MAC Mapping Cache for EID-table Vlan 101 (IID 1), 4 entries
            m = p2.match(line)
            if m:
                group = m.groupdict()
                address_type = group['type']
                vrf_name = group['vrf']
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
            # b827.eb51.f5ce/48, uptime: 22:49:42, expires: 01:10:17, via WLC Map-Notify, complete
            # 192.168.9.0/24, uptime: 00:04:02, expires: 23:55:57, via map-reply, complete
            m = p3.match(line)
            if m:
                # reset rloc counter
                rloc_id = 1
                group = m.groupdict()
                mapping_dict = map_cache_dict.setdefault('mappings', {}).\
                                setdefault(group['map_id'], {})
                mapping_dict['id'] = group['map_id']
                mapping_dict['uptime'] = group['uptime']
                mapping_dict['expires'] = group['expires']
                mapping_dict['via'] = group['via']
                eid_dict = mapping_dict.setdefault('eid', {})
                if ':' in group['map_id']:
                    ipv6_dict = eid_dict.setdefault('ipv6', {})
                    ipv6_dict['ipv6'] = group['map_id']
                else:
                    ipv4_dict = eid_dict.setdefault('ipv4', {})
                    ipv4_dict['ipv4'] = group['map_id']
                try:
                    eid_dict['address_type'] = address_type.lower() + '-afi'
                except:
                    pass
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
            #  8.8.8.8  00:04:02  up          50/50        -
            m = p5.match(line)
            if m:
                group = m.groupdict()
                postive_dict = mapping_dict.setdefault('positive_mapping', {}).\
                                setdefault('rlocs', {})
                rloc_dict = postive_dict.setdefault(rloc_id, {})
                rloc_dict['id'] = str(rloc_id)
                locator_dict = rloc_dict.setdefault('locator_address', {})
                locator_dict['address_type'] = address_type.lower() + '-afi'
                locator_dict['virtual_network_id'] = str(instance_id)
                locator_dict['uptime'] = group['uptime']
                locator_dict['state'] = group['state']
                locator_dict['priority'] = int(group['priority'])
                locator_dict['weight'] = int(group['weight'])
                if group['encap_iid']:
                    locator_dict['encap_iid'] = group['encap_iid']
                if ':' in group['locator']:
                    ipv6_dict = locator_dict.setdefault('ipv6', {})
                    ipv6_dict['ipv6'] = group['locator']
                else:
                    ipv4_dict = locator_dict.setdefault('ipv4', {})
                    ipv4_dict['ipv4'] = group['locator']
                # Increment entry
                rloc_id += 1
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
                                    'members':
                                        {Any():
                                            {'origin': str,
                                            'valid': str,
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


# ===========================================================================
# Parser for 'show lisp all instance-id <instance_id> <service> rloc members'
# ===========================================================================
class ShowLispServiceRlocMembers(ShowLispServiceRlocMembersSchema):

    '''Parser for "show lisp all instance-id <instance_id> <service> rloc members"'''

    def cli(self, service, instance_id):

        assert service in ['ipv4', 'ipv6', 'ethernet']
        
        # Execute command on device
        out = self.device.execute('show lisp all instance-id {instance_id}'
                                  ' service {service} rloc members'.\
                            format(instance_id=instance_id, service=service))

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
        # 2.2.2.2                 Registration                 Yes
        p4 = re.compile(r'(?P<member>([0-9\.\:]+)) +(?P<origin>(\S+))'
                         ' +(?P<valid>(\S+))$')

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
            # 2.2.2.2                 Registration                 Yes
            m = p4.match(line)
            if m:
                group = m.groupdict()
                members_dict = rloc_dict.setdefault('members', {}).\
                                setdefault(group['member'], {})
                members_dict['origin'] = group['origin'].lower()
                members_dict['valid'] = group['valid'].lower()
                continue

        return parsed_dict
