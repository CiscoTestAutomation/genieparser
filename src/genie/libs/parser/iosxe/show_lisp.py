''' show_lisp.py

IOSXE parsers for the following show commands:
    * show lisp session
    * show lisp session redundancy
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
    * show lisp {lisp_id} instance-id {instance_id} dynamic-eid summary
    * show lisp locator-table {vrf} instance-id {instance_id} dynamic-eid summary
    * show lisp instance-id {instance_id} dynamic-eid summary
    * show lisp eid-table vrf {vrf} dynamic-eid summary
    * show lisp eid-table vlan {vlan} dynamic-eid summary
    * show lisp eid-table {eid_table} dynamic-eid summary
    * show lisp {lisp_id} instance-id {instance_id} dynamic-eid
    * show lisp locator-table {vrf} instance-id {instance_id} dynamic-eid
    * show lisp instance-id {instance_id} dynamic-eid
    * show lisp eid-table {eid_table} dynamic-eid
    * show lisp eid-table vrf {vrf} dynamic-eid
    * show lisp eid-table vlan {vlan} dynamic-eid
    * show lisp {lisp_id} instance-id {instance_id} dynamic-eid detail
    * show lisp locator-table {vrf} instance-id {instance-id} dynamic-eid detail
    * show lisp instance-id {instance_id} dynamic-eid detail
    * show lisp eid-table {eid-table} dynamic-eid detail
    * show lisp eid-table vrf {vrf} dynamic-eid detail
    * show lisp eid-table vlan {vlan} dynamic-eid detail
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
    * show lisp {lisp_id} instance-id {instance_id} ipv4 publisher
    * show lisp locator-table {vrf} instance-id {instance_id} ipv4 publisher
    * show lisp instance-id {instance_id} ipv4 publisher
    * show lisp eid-table {eid_table} ipv4 publisher
    * show lisp eid-table vrf {vrf} ipv4 publisher
    * show lisp {lisp_id} instance-id {instance_id} ipv6 publisher
    * show lisp locator-table {vrf} instance-id {instance_id} ipv6 publisher
    * show lisp instance-id {instance_id} ipv6 publisher
    * show lisp eid-table {eid_table} ipv6 publisher
    * show lisp eid-table vrf {vrf} ipv6 publisher
    * show lisp {lisp_id} instance-id {instance_id} ethernet publisher
    * show lisp locator-table {vrf} instance-id {instance_id} ethernet publisher
    * show lisp instance-id {instance_id} ethernet publisher
    * show lisp eid-table vlan {vlan} ethernet publisher
    * show lisp instance-id {instance_id} ipv4 away
    * show lisp instance-id {instance_id} ipv4 away {eid}
    * show lisp instance-id {instance_id} ipv4 away {eid_prefix}
    * show lisp {lisp_id} instance-id {instance_id} ipv4 away
    * show lisp {lisp_id} instance-id {instance_id} ipv4 away {eid}
    * show lisp {lisp_id} instance-id {instance_id} ipv4 away {eid_prefix}
    * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 away
    * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 away {eid}
    * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 away {eid_prefix}
    * show lisp eid-table {eid_table} ipv4 away
    * show lisp eid-table {eid_table} ipv4 away {eid}
    * show lisp eid-table {eid_table} ipv4 away {eid_prefix}
    * show lisp eid-table vrf {eid_table} ipv4 away
    * show lisp eid-table vrf {eid_table} ipv4 away {eid}
    * show lisp eid-table vrf {eid_table} ipv4 away {eid_prefix}
    * show lisp {lisp_id} instance-id {instance_id} ipv4 publisher {publisher_id}
    * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 publisher {publisher_id}
    * show lisp instance-id {instance_id} ipv4 publisher {publisher_id}
    * show lisp eid-table {eid_table} ipv4 publisher {publisher_id}
    * show lisp eid-table vrf {vrf} ipv4 publisher {publisher_id}
    * show lisp eid-table vrf ipv4 publisher {publisher_id}
    * show lisp instance-id {instance-id} {address-family} database {prefix}
    * show lisp {lisp_id} instance-id {instance-id} {address-family} database {prefix}
    * show lisp locator-table {vrf} instance-id {instance-id} {address-family} database {prefix}
    * show lisp locator-table vrf {vrf} instance-id {instance-id} {address-family} database {prefix}
    * show lisp eid-table {vrf} {address-family} {prefix}
    * show lisp eid-table vrf {vrf} {address-family} database {prefix}
    * show lisp eid-table vlan {vlan_id} ethernet database {prefix}
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional, ListOf
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

    cli_command = 'show lisp session'
    exclude = ['time']

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Init vars
        parsed_dict = {}

        # Sessions for VRF default, total: 3, established: 3
        p1 = re.compile(r'Sessions +for +VRF +(?P<vrf>\S+),'
                         ' +total: +(?P<total>\d+),'
                         ' +established: +(?P<established>\d+)$')

        # Peer                           State      Up/Down        In/Out    Users
        # 10.16.2.2                      Up         00:51:38        8/13     3
        # 2001:DB8:B:2::2                Init       never           0/0      1
        p2 = re.compile(r'(?P<peer>\S+) +(?P<state>\S+) +(?P<time>\S+)'
                         ' +(?P<in>\d+)\/(?P<out>\d+) +(?P<users>\d+)$')

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

            # 10.1.8.8                       Up         00:52:15        8/13     3
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

    cli_command = 'show lisp platform'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

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
                {Optional('service'):
                    {Any():
                        {Optional('map_server'):
                            {Optional('virtual_network_ids'):
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

    cli_command = 'show lisp all extranet {extranet} instance-id {instance_id}'

    def cli(self, extranet, instance_id, output=None):
        if output is None:
            out = self.device.execute(self.cli_command.format(extranet=extranet,instance_id=instance_id))
        else:
            out = output

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
        # Provider             103        10.121.88.0/24
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
            # Provider             103        10.121.88.0/24
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
                {Optional('service'):
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

    cli_command = 'show lisp all instance-id {instance_id} dynamic-eid detail'

    def cli(self, instance_id, output=None):
        if output is None:
            out = self.device.execute(self.cli_command.format(instance_id=instance_id))
        else:
            out = output

        # Init vars
        parsed_dict = {}

        # Output for router lisp 0
        # Output for router lisp 0 instance-id 101
        p1 = re.compile(r'Output +for +router +lisp +(?P<lisp_router_id>(\S+))'
                         '(?: +instance-id +(?P<instance_id>(\d+)))?$')

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

        # Map-Server(s): 10.64.4.4  (proxy-replying)
        # Map-Server(s): 10.144.6.6
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
            # Output for router lisp 0 instance-id 101
            m = p1.match(line)
            if m:
                group = m.groupdict()
                lisp_router_id = int(group['lisp_router_id'])
                lisp_dict = parsed_dict.setdefault(
                    'lisp_router_instances', {}).setdefault(lisp_router_id, {})
                if group['instance_id']:
                    instance_id = group['instance_id']
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

            # Map-Server(s): 10.64.4.4  (proxy-replying)
            # Map-Server(s): 10.144.6.6
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
                Optional('lisp_router_id'):
                    {'site_id': str,
                    'xtr_id': str,
                    },
                Optional('service'):
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
                                Optional('mapping_servers'):
                                    {Any():
                                        {'ms_address': str,
                                        Optional('uptime'): str,
                                        },
                                    },
                                'itr':
                                    {'local_rloc_last_resort': str,
                                    Optional('use_proxy_etr_rloc'): str,
                                    },
                                Optional('map_cache'):
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
                            Optional('use_petrs'):
                                {Any():
                                    {'use_petr': str,
                                    },
                                },
                            Optional('mapping_servers'):
                                {Any():
                                    {'ms_address': str,
                                    Optional('uptime'): str,
                                    },
                                },
                            },
                        'itr':
                            {'enabled': bool,
                            'proxy_itr_router': bool,
                            Optional('proxy_itrs'):
                                {Any():
                                    {'proxy_etr_address': str,
                                    },
                                },
                            'solicit_map_request': str,
                            'max_smr_per_map_cache_entry': str,
                            'multiple_smr_suppression_time': int,
                            Optional('map_resolvers'):
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

    cli_command = ['show lisp all instance-id {instance_id} {service}','show lisp all service {service}']

    def cli(self, service, instance_id=None, output=None):

        if output is None:
            assert service in ['ipv4', 'ipv6', 'ethernet']
            if instance_id:
                cmd = self.cli_command[0].format(instance_id=instance_id,service=service)
            else:
                cmd = self.cli_command[1].format(service=service)
            out = self.device.execute(cmd)
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
        # Proxy-ETR Router (PETR):             enabled RLOCs: 10.10.10.10
        p7 = re.compile(r'Proxy\-(ITR|ETR) +Router'
                         ' +\((?P<proxy_type>(PITR|PETR))\) *:'
                         ' +(?P<state>(enabled|disabled))'
                         '(?: +RLOCs: +(?P<proxy_itr>(\S+)))?$')

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

        # ITR Map-Resolver(s):                 10.64.4.4, 10.166.13.13
        p15 = re.compile(r'ITR +Map\-Resolver\(s\) *: +(?P<resolvers>(.*))$')

        #                                      10.84.66.66 *** not reachable ***
        p15_1 = re.compile(r'(?P<resolver>([0-9\.\:]+))(?: +\*.*)?$')

        # ETR Map-Server(s):                   10.64.4.4 (17:49:58), 10.166.13.13 (00:00:35)
        p16 = re.compile(r'ETR +Map\-Server\(s\) *: +(?P<servers>(.*))$')

        #                                      10.84.66.66 (never)
        p16_1 = re.compile(r'(?P<server>([0-9\.\:]+))(?: +\((?P<uptime>(\S+))\))?$')

        # xTR-ID:                              0x730E0861-0x12996F6D-0xEFEA2114-0xE1C951F7
        p17 = re.compile(r'xTR-ID *: +(?P<xtr_id>(\S+))$')

        # site-ID:                             unspecified
        p18 = re.compile(r'site-ID *: +(?P<site_id>(\S+))$')

        # ITR local RLOC (last resort):        10.16.2.2
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

        #   Vlan100: 10.229.11.1 (Loopback0)
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
                group = m.groupdict()
                proxy_type = group['proxy_type'].lower()
                if proxy_type == 'pitr':
                    itr_dict['proxy_itr_router'] = \
                        state_dict[group['state']]
                elif proxy_type == 'petr':
                    etr_dict['proxy_etr_router'] = \
                        state_dict[group['state']]
                if group['proxy_itr']:
                    pitr_dict = itr_dict.setdefault('proxy_itrs', {}).\
                                setdefault(group['proxy_itr'], {})
                    pitr_dict['proxy_etr_address'] = group['proxy_itr']
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

            # ITR Map-Resolver(s):                 10.64.4.4, 10.166.13.13
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

            # ETR Map-Server(s):                   10.64.4.4 (17:49:58), 10.166.13.13 (00:00:35)
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

            #                                  10.84.66.66 (never)
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

            # ITR local RLOC (last resort):        10.16.2.2
            m = p19.match(line)
            if m:
                iid_itr_dict = iid_dict.setdefault('itr', {})
                iid_itr_dict['local_rloc_last_resort'] = m.groupdict()['val']
                continue

            # ITR use proxy ETR RLOC(s):           10.10.10.10
            m = p20.match(line)
            if m:
                group = m.groupdict()
                iid_itr_dict['use_proxy_etr_rloc'] = group['val']
                use_petr_dict = etr_dict.\
                                setdefault('use_petrs', {}).\
                                setdefault(group['val'], {})
                use_petr_dict['use_petr'] = group['val']
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

            #   Vlan100: 10.229.11.1 (Loopback0)
            #   Vlan101: 10.229.11.1 (Loopback0)
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
        p2 = re.compile(r'LISP +(?P<type>(IPv4|IPv6|MAC)) +Mapping +Cache +for'
                         ' +EID\-table +(default|(vrf|Vlan) +(?P<vrf>(\S+)))'
                         ' +\(IID +(?P<iid>(\d+))\), +(?P<entries>(\d+))'
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
        p5 = re.compile(r'(?P<locator>(\S+)) +(?P<uptime>(\S+))'
                         ' +(?P<state>(\S+|up, self))'
                         ' +(?P<priority>(\d+))\/(?P<weight>(\d+))'
                         '(?: +(?P<encap_iid>(\S+)))?$')

        # Encapsulating to proxy ETR
        # Encapsulating to proxy ETR Encap-IID 3
        p6 = re.compile(r'Encapsulating\s+to\s+proxy\s+ETR(\s+Encap-IID\s+(?P<encap_to_petr_iid>\S+))?$')

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

    cli_command = 'show lisp all instance-id {instance_id} service {service} rloc members'

    def cli(self, service, instance_id, output=None):

        if output is None:
            assert service in ['ipv4', 'ipv6', 'ethernet']
            out = self.device.execute(self.cli_command.format(instance_id=instance_id, service=service))
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
            # 10.16.2.2               Registration                 Yes
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
                                    'prefixes':
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

    cli_command = 'show lisp all instance-id {instance_id} service {service} smr'

    def cli(self, service, instance_id, output=None):

        if output is None:
            assert service in ['ipv4', 'ipv6', 'ethernet']
            out = self.device.execute(self.cli_command.format(instance_id=instance_id, service=service))
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
        p4 = re.compile(r'(?P<prefix>([0-9\.\/\:]+)) +(?P<producer>(.*))$')

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
                                'total_map_cache_entries': int,
                                'total_db_entries_inactive': int,
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

    '''Parser for "show lisp all service <service> summary"'''

    cli_command = 'show lisp all service {service} summary'

    def cli(self, service, output=None):

        if output is None:
            assert service in ['ipv4', 'ipv6', 'ethernet']
            out = self.device.execute(self.cli_command.format(service=service))
        else:
            out = output

        # Init vars
        parsed_dict = {}

        # State dict
        state_dict = {
            'disabled': False,
            'enabled': True}

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
                         ' +(?P<db_size>(\d+))(?P<rloc_status>(\W))? +(?P<db_no_route>(\d+))'
                         ' +(?P<cache_size>(\d+)) +(?P<incomplete>(\S+))'
                         ' +(?P<cache_idle>(\S+)) +(?P<role>(\S+))$')

        p4_2 = re.compile(r'(?P<interface>(\S+))\.(?P<iid>(\d+))'
                         ' +(?P<db_size>(\d+))(?P<rloc_status>(\W))? +(?P<db_no_route>(\d+))'
                         ' +(?P<cache_size>(\d+)) +(?P<incomplete>(\S+))'
                         ' +(?P<cache_idle>(\S+)) +(?P<role>(\S+))$')

        # Number of eid-tables:                                 2
        p5 = re.compile(r'Number +of +eid-tables: +(?P<val>(\d+))$')

        # Total number of database entries:                     2 (inactive 0)
        p6 = re.compile(r'Total +number +of +database +entries:'
                         ' +(?P<val>(\d+))(?: +\(inactive'
                         ' +(?P<inactive>(\d+))\))?$')

        # EID-tables with inconsistent locators:                0
        p7 = re.compile(r'EID-tables +with +inconsistent +locators:'
                         ' +(?P<val>(\d+))$')

        # Total number of map-cache entries:                    3
        p8 = re.compile(r'Total +number +of +map-cache +entries:'
                         ' +(?P<val>(\d+))$')

        # EID-tables with incomplete map-cache entries:         0
        p9 = re.compile(r'EID-tables +with +incomplete +map-cache +entries:'
                         ' +(?P<val>(\d+))$')

        # EID-tables pending map-cache update to FIB:           0
        p10 = re.compile(r'EID-tables +pending +map-cache +update +to +FIB:'
                          ' +(?P<val>(\d+))$')

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

        return parsed_dict


# =======================================================================
# Schema for 'show lisp all instance-id <instance_id> <service> dabatase'
# =======================================================================
class ShowLispServiceDatabaseSchema(MetaParser):

    '''Schema for "show lisp all instance-id <instance_id> <service> dabatase" '''

    schema = {
        'lisp_router_instances':
            {Any():
                {'lisp_router_instance_id': int,
                'locator_sets':
                    {Any():
                        {'locator_set_name': str,
                        },
                    },
                Optional('service'):
                    {Optional(Any()):
                        {'etr':
                            {'local_eids':
                                {Any():
                                    {'vni': str,
                                    'total_eid_entries': int,
                                    'no_route_eid_entries': int,
                                    'inactive_eid_entries': int,
                                    Optional('dynamic_eids'):
                                        {Any():
                                            {'id': str,
                                            Optional('dynamic_eid'): str,
                                            'eid_address':
                                                {'address_type': str,
                                                'vrf': str,
                                                },
                                            'rlocs': str,
                                            'loopback_address': str,
                                            'priority': int,
                                            'weight': int,
                                            'source': str,
                                            'state': str,
                                            },
                                        },
                                    Optional('eids'):
                                        {Any():
                                            {'id': str,
                                            'eid_address':
                                                {'address_type': str,
                                                'vrf': str,
                                                },
                                            'rlocs': str,
                                            'loopback_address': str,
                                            'priority': int,
                                            'weight': int,
                                            'source': str,
                                            'state': str,
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
# Parser for 'show lisp all instance-id <instance_id> <service> dabatase'
# =======================================================================
class ShowLispServiceDatabase(ShowLispServiceDatabaseSchema):

    '''Parser for "show lisp all instance-id <instance_id> <service> dabatase"'''

    cli_command = 'show lisp all instance-id {instance_id} {service} database'

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

        # LISP ETR IPv4 Mapping Database for EID-table default (IID 101), LSBs: 0x1
        # LISP ETR IPv6 Mapping Database for EID-table vrf red (IID 101), LSBs: 0x1
        # LISP ETR MAC Mapping Database for EID-table Vlan 101 (IID 1), LSBs: 0x1
        p2 = re.compile(r'LISP +ETR +(IPv4|IPv6|MAC) +Mapping +Database +for'
                         ' +EID\-table +(default|(vrf|Vlan) +(?P<vrf>(\S+)))'
                         ' +\(IID +(?P<instance_id>(\d+))\),'
                         ' +LSBs: +(?P<lsb>(\S+))$')

        # Entries total 1, no-route 0, inactive 0
        # Entries total 2, no-route 0, inactive 0
        p3 = re.compile(r'Entries +total +(?P<total>(\d+)), +no-route'
                         ' +(?P<no_route>(\d+)),'
                         ' +inactive +(?P<inactive>(\d+))$')

        # 192.168.0.0/24, locator-set RLOC
        # 2001:192:168::/64, locator-set RLOC
        # 0050.56ff.1bbe/48, dynamic-eid Auto-L2-group-1, inherited from default locator-set RLOC
        # cafe.caff.c9fd/48, dynamic-eid Auto-L2-group-1, inherited from default locator-set RLOC
        p4 = re.compile(r'(?P<etr_eid>(\S+)),'
                         '(?: +dynamic-eid +(?P<dyn_eid>(\S+)),'
                         ' +inherited +from +default)?'
                         ' +locator-set +(?P<locator_set>(\S+))$')

        # Locator       Pri/Wgt  Source     State
        # 10.16.2.2     50/50    cfg-intf   site-self, reachable
        # 10.229.11.1   1/100    cfg-intf   site-self, reachable
        p5 = re.compile(r'(?P<locator>(\S+))'
                         ' +(?P<priority>(\d+))\/(?P<weight>(\d+))'
                         ' +(?P<source>(\S+)) +(?P<state>(.*))$')

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

            # LISP ETR IPv6 Mapping Database for EID-table vrf red (IID 101), LSBs: 0x1
            m = p2.match(line)
            if m:
                group = m.groupdict()
                etr_eid_vrf = group['vrf'] if group['vrf'] else 'default'
                lsb = group['lsb']
                # Create lisp_dict
                lisp_dict = parsed_dict.\
                            setdefault('lisp_router_instances', {}).\
                            setdefault(lisp_router_id, {})
                lisp_dict['lisp_router_instance_id'] = lisp_router_id
                continue

            # Entries total 2, no-route 0, inactive 0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                total_entries = int(group['total'])
                no_route_entries = int(group['no_route'])
                inactive_entries = int(group['inactive'])
                continue

            # 192.168.0.0/24, locator-set RLOC
            # cafe.caff.c9fd/48, dynamic-eid Auto-L2-group-1, inherited from default locator-set RLOC
            m = p4.match(line)
            if m:
                group = m.groupdict()
                # Create locator_set_dict
                ls_dict = lisp_dict.setdefault('locator_sets', {}).\
                            setdefault(group['locator_set'], {})
                ls_dict['locator_set_name'] = group['locator_set']
                etr_dict = lisp_dict.setdefault('service', {}).\
                                setdefault(service, {}).\
                                setdefault('etr', {}).\
                                setdefault('local_eids', {}).\
                                setdefault(instance_id, {})
                etr_dict['vni'] = instance_id
                etr_dict['total_eid_entries'] = total_entries
                etr_dict['no_route_eid_entries'] = no_route_entries
                etr_dict['inactive_eid_entries'] = inactive_entries
                # Create eid dict
                if group['dyn_eid']:
                    eid_dict_name = 'dynamic_eids'
                else:
                    eid_dict_name = 'eids'
                eid_dict = etr_dict.setdefault(eid_dict_name, {}).\
                            setdefault(group['etr_eid'], {})
                eid_dict['id'] = group['etr_eid']
                eid_dict['rlocs'] = group['locator_set']
                if group['dyn_eid']:
                    eid_dict['dynamic_eid'] = group['dyn_eid']
                # Create eid_addr_dict
                eid_addr_dict = eid_dict.setdefault('eid_address', {})
                eid_addr_dict['address_type'] = service
                eid_addr_dict['vrf'] = etr_eid_vrf
                continue

            # Locator       Pri/Wgt  Source     State
            # 10.16.2.2     50/50    cfg-intf   site-self, reachable
            m = p5.match(line)
            if m:
                group = m.groupdict()
                eid_dict['loopback_address'] = group['locator']
                eid_dict['priority'] = int(group['priority'])
                eid_dict['weight'] = int(group['weight'])
                eid_dict['source'] = group['source']
                eid_dict['state'] = group['state']
                continue

        return parsed_dict


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

        return parsed_dict


# =========================================================================
# Schema for 'show lisp all instance-id <instance_id> <service> statistics'
# =========================================================================
class ShowLispServiceStatisticsSchema(MetaParser):

    '''Schema for "show lisp all instance-id <instance_id> <service> statistics" '''

    schema = {
        'lisp_router_instances':
            {Any():
                {'service':
                    {Any():
                        {'statistics':
                            {Any():
                                {'last_cleared': str,
                                Any(): Any(),
                                Optional('map_resolvers'):
                                    {Any():
                                        {'last_reply': str,
                                        'metric': str,
                                        'reqs_sent': int,
                                        'positive': int,
                                        'negative': int,
                                        'no_reply': int,
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        }


# =========================================================================
# Parser for 'show lisp all instance-id <instance_id> <service> statistics'
# =========================================================================
class ShowLispServiceStatistics(ShowLispServiceStatisticsSchema):

    '''Parser for "show lisp all instance-id <instance_id> <service> statistics"'''

    cli_command = 'show lisp all instance-id {instance_id} {service} statistics'
    exclude = ['map_register_records_out']

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
        p1 = re.compile(r'^Output +for +router +lisp +(?P<router_id>(\S+))'
                         '(?: +instance-id +(?P<instance_id>(\d+)))?$')

        # LISP EID Statistics for instance ID 1 - last cleared: never
        # LISP RLOC Statistics - last cleared: never
        # LISP Miscellaneous Statistics - last cleared: never
        p2 = re.compile(r'LISP +(?P<stat_type>(\S+)) +Statistics'
                         '(?: +for +instance +ID +(?P<iid>(\d+)))?'
                         ' +\- +last +cleared: +(?P<last_cleared>(\S+))$')

        # Control Packets:
        p3_1 = re.compile(r'Control Packets:$')

        # Errors:
        p3_2 = re.compile(r'Errors:$')

        # Map-Register records in/out:              0/52
        p4 = re.compile(r'Map-Register +records +in\/out: +(?P<in>(\d+))\/(?P<out>(\d+))$')

        # Map-Notify records in/out:                2/0
        p5 = re.compile(r'Map-Notify +records +in\/out: +(?P<in>(\d+))\/(?P<out>(\d+))$')

        # Authentication failures:                0
        p6 = re.compile(r'Authentication +failures: +(?P<auth_failures>(\d+))$')

        # Map-Requests in/out:                              8/40
        # Encapsulated Map-Requests in/out:               8/36
        # RLOC-probe Map-Requests in/out:                 0/4
        # SMR-based Map-Requests in/out:                  0/4
        # Extranet SMR cross-IID Map-Requests in:         0
        # Map-Requests expired on-queue/no-reply          0/13
        # Map-Resolver Map-Requests forwarded:            0
        # Map-Server Map-Requests forwarded:              0
        p7 = re.compile(r'^(?P<key>([a-zA-Z\-\/\s]+))\: +(?P<value>(.*))$')

        # Map-Resolver    LastReply  Metric ReqsSent Positive Negative No-Reply
        # 10.94.44.44     never           1      306       18        0       66
        # 10.84.66.66     never     Unreach        0        0        0        0
        p8 = re.compile(r'(?P<mr>([a-zA-Z0-9\.\:]+)) +(?P<last_reply>(\S+))'
                         ' +(?P<metric>(\S+)) +(?P<sent>(\d+))'
                         ' +(?P<positive>(\d+)) +(?P<negative>(\d+))'
                         ' +(?P<no_reply>(\d+))$')

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

            # LISP EID Statistics for instance ID 1 - last cleared: never
            m = p2.match(line)
            if m:
                group = m.groupdict()
                # Create stats dict
                stats_dict = parsed_dict.\
                                setdefault('lisp_router_instances', {}).\
                                setdefault(lisp_router_id, {}).\
                                setdefault('service', {}).\
                                setdefault(service, {}).\
                                setdefault('statistics', {}).\
                                setdefault(group['stat_type'], {})
                stats_dict['last_cleared'] = m.groupdict()['last_cleared']
                continue

            # Control Packets:
            m = p3_1.match(line)
            if m:
                last_dict = stats_dict.setdefault('control', {})
                continue

            # Errors:
            m = p3_2.match(line)
            if m:
                last_dict = stats_dict.setdefault('errors', {})
                continue

            # Map-Register records in/out:              0/52
            m = p4.match(line)
            if m:
                group = m.groupdict()
                last_dict['map_register_records_in'] = group['in']
                last_dict['map_register_records_out'] = group['out']
                map_register = True
                continue

            # Map-Notify records in/out:                2/0
            m = p5.match(line)
            if m:
                group = m.groupdict()
                last_dict['map_notify_records_in'] = group['in']
                last_dict['map_notify_records_out'] = group['out']
                map_register = False
                continue

            # Authentication failures:                0
            m = p6.match(line)
            if m:
                failures = m.groupdict()['auth_failures']
                if map_register:
                    last_dict['map_registers_in_auth_failed'] = failures
                else:
                    last_dict['map_notify_auth_failures'] = failures
                continue

            # Map-Requests in/out:                              8/40
            # Encapsulated Map-Requests in/out:               8/36
            # RLOC-probe Map-Requests in/out:                 0/4
            # SMR-based Map-Requests in/out:                  0/4
            # Extranet SMR cross-IID Map-Requests in:         0
            # Map-Requests expired on-queue/no-reply          0/13
            # Map-Resolver Map-Requests forwarded:            0
            # Map-Server Map-Requests forwarded:              0
            m = p7.match(line)
            if m:
                group = m.groupdict()
                if "/" in group['key']:
                    # split the key into 2
                    splitkey = re.search('(?P<splitkey>(\S+\/\S+))', group['key'])\
                                .groupdict()['splitkey']
                    splitkey1, splitkey2 = splitkey.split("/")
                    key = group['key'].replace(splitkey, "").strip().lower().\
                            replace(" ", "_").replace("-", "_")
                    key1 = key + "_" + splitkey1
                    key2 = key + "_" + splitkey2
                    # set values
                    val1, val2 = group['value'].split("/")
                    last_dict[key1] = val1
                    last_dict[key2] = val2
                else:
                    key = group['key'].lower().replace(" ", "_").\
                            replace("-", "_")
                    last_dict[key] = group['value']
                continue

            # Map-Resolver    LastReply  Metric ReqsSent Positive Negative No-Reply
            # 10.94.44.44     never           1      306       18        0       66
            # 10.84.66.66     never     Unreach        0        0        0        0
            m = p8.match(line)
            if m:
                group = m.groupdict()
                mr_dict = last_dict.setdefault('map_rseolvers', {}).\
                            setdefault(group['mr'], {})
                mr_dict['last_reply'] = group['last_reply']
                mr_dict['metric'] = group['metric']
                mr_dict['reqs_sent'] = int(group['sent'])
                mr_dict['positive'] = int(group['positive'])
                mr_dict['negative'] = int(group['negative'])
                mr_dict['no_reply'] = int(group['no_reply'])
                continue

        return parsed_dict


# ===================
# Schema for:
#  * 'show lisp site'
# ===================
class ShowLispSiteSchema(MetaParser):
    """Schema for show lisp site."""

    schema = {
        "site_names": {
            str: {
                int: {
                    "last_register": str,
                    "up": str,
                    "who_last_registered": str,
                    "inst_id": int,
                    "eid_prefix": str
                }
            }
        }
    }


# ===================
# Parser for:
#  * 'show lisp site'
# ===================
class ShowLispSite(ShowLispSiteSchema):
    """Parser for show lisp site"""

    cli_command = 'show lisp site'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        lisp_site_dict = {}

        # LISP Site Registration Information
        # * = Some locators are down or unreachable
        # # = Some registrations are sourced by reliable transport
        #
        # Site Name      Last      Up     Who Last             Inst     EID Prefix
        #                Register         Registered           ID
        # site_uci       never     no     --                   4097     10.10.64.0/27
        #                2w4d      yes#   10.1.64.71:36820  4097     10.10.64.2/32
        #                2w4d      yes#   10.1.64.71:36820  4097     10.10.64.6/32
        #                2w4d      yes#   10.1.64.106:51580 4097     10.10.64.7/32
        #                2w4d      yes#   10.1.64.106:51580 4097     10.10.64.18/32
        #                never     no     --                   4099     10.19.22.0/26
        #                02:05:11  yes#   10.1.64.71:36820  4099     10.19.22.2/32
        #                2d16h     yes#   10.1.64.106:51580 4099     10.19.22.3/32
        #                00:33:39  yes#   10.1.64.71:36820  4099     10.19.22.21/32
        #                never     no     --                   4099     10.19.22.64/27
        #                4w3d      yes#   10.1.64.76:30688  4099     10.19.22.66/32
        #                never     no     --                   4099     10.19.22.96/27
        #                3w5d      yes#   10.1.64.71:36820  4099     10.19.22.112/32
        #                never     no     --                   4099     2001:DB8:211:F5D7::/66
        #                never     no     --                   4099     2001:DB8:211:F5D7:4000::/66
        #                4w3d      yes#   10.1.64.76:30688  4099     2001:DB8:4228:510:502A:1ADA:1ADA:1ADA/128
        #                never     no     --                   4100     10.19.20.0/25
        #                01:05:05  yes#   10.1.64.106:51580 4100     10.19.20.55/32

        # site_uci       never     no     --                   4097     10.10.64.0/27
        lisp_site_capture = re.compile(
            r"^(?P<lisp_site>\S+)\s+(?P<last_register>\S+)\s+(?P<up>\S+)\s+(?P<who_last_registered>\S+)\s+(?P<inst_id>\d+)\s+(?P<eid_prefix>\S+)")
        #                2w4d      yes#   10.1.64.71:36820  4097     10.10.64.2/32
        list_site_info_capture = re.compile(
            r"^(?P<last_register>\S+)\s+(?P<up>\S+)\s+(?P<who_last_registered>\S+)\s+(?P<inst_id>\d+)\s+(?P<eid_prefix>\S+)")

        remove_lines = (
            'LISP Site Registration Information',
            '* = Some locators are down or unreachable',
            '# = Some registrations are sourced by reliable transport',
            'Site Name      Last      Up     Who Last             Inst     EID Prefix',
            'Register         Registered           ID'
        )

        # Remove unwanted lines from raw text
        def filter_lines(raw_output, remove_lines):
            # Remove empty lines
            clean_lines = list(filter(None, raw_output.splitlines()))
            rendered_lines = []
            for clean_line in clean_lines:
                clean_line_strip = clean_line.strip()
                # Remove lines unwanted lines from list of "remove_lines"
                if not clean_line_strip.startswith(remove_lines):
                    rendered_lines.append(clean_line_strip)
            return rendered_lines

        out = filter_lines(raw_output=out, remove_lines=remove_lines)

        lisp_site = {}
        lisp_site_index = 1
        lisp_group_dict = {}

        for line in out:
            # site_uci       never     no     --                   4097     10.10.64.0/27
            if lisp_site_capture.match(line):
                lisp_site_match = lisp_site_capture.match(line)
                groups = lisp_site_match.groupdict()
                lisp_site = groups['lisp_site']
                last_register = groups['last_register']
                up = groups['up']
                who_last_registered = groups['who_last_registered']
                inst_id = groups['inst_id']
                eid_prefix = groups['eid_prefix']
                if not lisp_site_dict.get(lisp_site, {}):
                    lisp_site_dict['site_names'] = {}
                    lisp_site_dict['site_names'][lisp_site] = {}
                    lisp_site_index = 1
                lisp_group_dict['last_register'] = last_register
                lisp_group_dict['up'] = up
                lisp_group_dict['who_last_registered'] = who_last_registered
                lisp_group_dict['inst_id'] = int(inst_id)
                lisp_group_dict['eid_prefix'] = eid_prefix
                if not lisp_site_dict['site_names'][lisp_site].get(lisp_site_index, {}):
                    lisp_site_dict['site_names'][lisp_site][lisp_site_index] = lisp_group_dict
                lisp_site_index = lisp_site_index + 1
                lisp_group_dict = {}
                continue
            #                2w4d      yes#   10.1.64.71:36820  4097     10.10.64.2/32
            elif list_site_info_capture.match(line):
                list_site_info_match = list_site_info_capture.match(line)
                groups = list_site_info_match.groupdict()
                last_register = groups['last_register']
                up = groups['up']
                who_last_registered = groups['who_last_registered']
                inst_id = groups['inst_id']
                eid_prefix = groups['eid_prefix']
                lisp_group_dict['last_register'] = last_register
                lisp_group_dict['up'] = up
                lisp_group_dict['who_last_registered'] = who_last_registered
                lisp_group_dict['inst_id'] = int(inst_id)
                lisp_group_dict['eid_prefix'] = eid_prefix
                lisp_site_dict['site_names'][lisp_site][lisp_site_index] = lisp_group_dict
                lisp_site_index = lisp_site_index + 1
                lisp_group_dict = {}
                continue
        return lisp_site_dict

# ==========================================
# Schema for:
#  * 'show lisp eid-table vrf {vrf} ipv4 database'
# ==========================================
class ShowLispEidTableVrfIpv4DatabaseSchema(MetaParser):
    """Schema for show lisp eid-table vrf {vrf} ipv4 database."""

    schema = {
        "vrf": {
            Any(): {
                "iid": int,
                "lsb": str,
                "total_entries": int,
                "no_route": int,
                "inactive": int,
                "eid" : {
                    str: {
                        "locator_set": list,
                        "rlocs": {
                            str: {
                                "priority": int,
                                "weight": int,
                                "source": str,
                                "state": list
                            }
                        }
                    }
                }
            }
        }
    }


# ==========================================
# Parser for:
#  * 'show lisp eid-table vrf {vrf} ipv4 database'
# ==========================================
class ShowLispEidTableVrfIpv4Database(ShowLispEidTableVrfIpv4DatabaseSchema):
    """Parser for show lisp eid-table vrf {vrf} ipv4 database"""

    cli_command = 'show lisp eid-table vrf {vrf} ipv4 database'

    def cli(self, vrf, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(vrf=vrf))
        else:
            output = output

        # LISP ETR IPv4 Mapping Database for EID-table vrf User (IID 4100), LSBs: 0x3
        # Entries total 3, no-route 0, inactive 0
        #
        # 10.16.0.0/19, locator-set rloc_5823c743-d29b-40d4-a063-8a29881a59b2, auto-discover-rlocs, proxy
        #   Locator      Pri/Wgt  Source     State
        #   10.8.190.11   10/10   cfg-intf   site-self, reachable
        #   10.8.190.17   10/10   auto-disc  site-other, report-reachable
        # 10.16.32.0/20, locator-set rloc_5823c743-d29b-40d4-a063-8a29881a59b2, auto-discover-rlocs, proxy
        #   Locator      Pri/Wgt  Source     State
        #   10.8.190.11   10/10   cfg-intf   site-self, reachable
        #   10.8.190.17   10/10   auto-disc  site-other, report-reachable
        # 10.16.48.0/24, locator-set rloc_5823c743-d29b-40d4-a063-8a29881a59b2, auto-discover-rlocs, proxy
        #   Locator      Pri/Wgt  Source     State
        #   10.8.190.11   10/10   cfg-intf   site-self, reachable
        #   10.8.190.17   10/10   auto-disc  site-other, report-reachable

        # LISP ETR IPv4 Mapping Database for EID-table vrf User (IID 4100), LSBs: 0x3
        p_lisp_header = re.compile(r"^LISP\s+ETR\s+IPv4\s+Mapping\s+Database\s+for\s+EID-table\s+vrf\s+(?P<vrf>\S+)"
                                   r"\s+\(IID\s+(?P<iid>\d+)\),\s+LSBs:\s+(?P<lsb>\S+)$")

        # Entries total 3, no-route 0, inactive 0
        p_lisp_header_2 = re.compile(r"^Entries\s+total\s+(?P<total>\d+),\s+no-route\s+(?P<no_route>\d+),\s+inactive\s+(?P<inactive>\d+)$")

        # 10.16.0.0/19, locator-set rloc_5823c743-d29b-40d4-a063-8a29881a59b2, auto-discover-rlocs, proxy
        p_lisp_entry = re.compile(r"^(?P<ip>\S+\/\d+),\s+locator-set\s+(?P<loc_set>.*)$")

        # 10.160.96.166/32, dynamic-eid Voice-IPV4, inherited from default locator-set rloc_20ffdc5c-fe5f-4f22-88db-733e73d1f216
        p_lisp_entry_2 = re.compile(r"^(?P<ip>\S+\/\d+),\s+dynamic-eid\s+(?P<loc_set>.*)$")

        # 10.8.190.11   10/10   cfg-intf   site-self, reachable
        p_lisp_subentry = re.compile(r"(?P<locator>\S+)\s+(?P<pri>\d+)\/(?P<wgt>\d+)\s+(?P<source>\S+)\s+(?P<state>.*)$")


        lisp_dict = {}
        current_entry = ""
        locator_set_list = []
        state_list = []
        vrf = ""

        for line in output.splitlines():
            line = line.strip()

            # LISP ETR IPv4 Mapping Database for EID-table vrf User (IID 4100), LSBs: 0x3
            m = p_lisp_header.match(line)
            if m:
                vrf = m.group("vrf")
                vrf_dict = lisp_dict.setdefault("vrf", {}).setdefault(vrf, {})
                vrf_dict.update({ "iid": int(m.group("iid")) })
                vrf_dict.update({ "lsb": m.group("lsb") })
                continue

            # Entries total 3, no-route 0, inactive 0
            m = p_lisp_header_2.match(line)
            if m:
                vrf_dict.update({ "total_entries": int(m.group("total")) })
                vrf_dict.update({ "no_route": int(m.group("no_route")) })
                vrf_dict.update({ "inactive": int(m.group("inactive")) })
                continue

            # 10.16.0.0/19, locator-set rloc_5823c743-d29b-40d4-a063-8a29881a59b2, auto-discover-rlocs, proxy
            m = p_lisp_entry.match(line)
            if m:
                locator_set_list = [x.strip() for x in m.group("loc_set").split(',')]
                current_entry = m["ip"]
                entry_dict = vrf_dict.setdefault("eid", {} ).setdefault(current_entry, {})
                entry_dict.update({ "locator_set": locator_set_list} )
                continue

            # 10.160.96.146/32, dynamic-eid Voice-IPV4, inherited from default locator-set rloc_20ffdc5c-fe5f-4f22-88db-733e73d1f216
            m = p_lisp_entry_2.match(line)
            if m:
                locator_set_list = [x.strip() for x in m.group("loc_set").split(',')]
                current_entry = m["ip"]
                entry_dict = vrf_dict.setdefault("eid", {} ).setdefault(current_entry, {})
                entry_dict.update({ "locator_set": locator_set_list} )
                continue

            # 10.8.190.11   10/10   cfg-intf   site-self, reachable
            m = p_lisp_subentry.match(line)
            if m:
                state_list = [x.strip() for x in m.group("state").split(',') ]
                sub_dict = entry_dict.setdefault("rlocs", {}).setdefault(m.group("locator"), {})
                sub_dict.update({ "priority": int(m.group("pri")) })
                sub_dict.update({ "weight": int(m.group("wgt")) })
                sub_dict.update({ "source": m.group("source") })
                sub_dict.update({ "state": state_list })
                continue

        return lisp_dict


# ================================================
# Schema for:
#  * 'show lisp eid-table vrf {vrf} ipv4 map-cache'
# ================================================
class ShowLispEidTableVrfUserIpv4MapCacheSchema(MetaParser):
    """Schema for show lisp eid-table vrf {vrf} ipv4 map-cache."""

    schema = {
        "vrf": {
            str: {
                "iid": int,
                "number_of_entries": int,
                "eid": {
                    str: {
                        "uptime": str,
                        "expire": str,
                        "via": list,
                        "rloc": {
                            Optional("status"): str,
                            Optional("action"): str,
                            Optional("ip"): str,
                            Optional("uptime"): str,
                            Optional("state"): str,
                            Optional("priority"): int,
                            Optional("weight"): int,
                            Optional("encap_iid"): str
                        }
                    }
                }
            }
        }
    }


# ================================================
# Parser for:
#  * 'show lisp eid-table vrf {vrf} ipv4 map-cache'
# ================================================
class ShowLispEidTableVrfUserIpv4MapCache(ShowLispEidTableVrfUserIpv4MapCacheSchema):
    """Parser for show lisp eid-table vrf {vrf} ipv4 map-cache"""

    cli_command = "show lisp eid-table vrf {vrf} ipv4 map-cache"

    def cli(self, vrf, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(vrf=vrf))
        else:
            output = output

        # 0.0.0.0/0, uptime: 1w6d, expires: never, via static-send-map-request
        #   Negative cache entry, action: send-map-request
        # 0.0.0.0/5, uptime: 4w6d, expires: 00:14:38, via map-reply, forward-native
        #   Encapsulating to proxy ETR
        # 10.64.0.0/7, uptime: 07:18:55, expires: 00:07:19, via map-reply, forward-native
        #   Encapsulating to proxy ETR
        # 10.0.0.0/9, uptime: 1w4d, expires: 00:00:13, via map-reply, forward-native
        #   Encapsulating to proxy ETR
        # 10.128.0.0/11, uptime: 4w6d, expires: 00:04:45, via map-reply, forward-native
        #   Encapsulating to proxy ETR
        # 10.16.0.17/32, uptime: 1w6d, expires: 13:36:24, via map-reply, self, complete
        #   Locator      Uptime    State      Pri/Wgt     Encap-IID
        #   10.8.129.94  1w6d      up          10/10        -
        # 10.16.0.18/32, uptime: 1w6d, expires: 13:40:30, via map-reply, self, complete
        #   Locator      Uptime    State      Pri/Wgt     Encap-IID
        #   10.8.129.65  1w6d      up          10/10        -
        # 10.16.0.21/32, uptime: 1w6d, expires: 12:55:06, via map-reply, self, complete
        #   Locator       Uptime    State      Pri/Wgt     Encap-IID
        #   10.8.129.124  1w6d      up          10/10        -
        # 10.16.0.22/32, uptime: 1w6d, expires: 20:44:39, via map-reply, self, complete
        #   Locator      Uptime    State      Pri/Wgt     Encap-IID
        #   10.8.129.94  1w6d      up          10/10        -
        # 10.16.0.24/32, uptime: 1w6d, expires: 20:44:39, via map-reply, self, complete
        #   Locator      Uptime    State      Pri/Wgt     Encap-IID
        #   10.8.129.94  1w6d      up          10/10        -
        # 10.16.0.25/32, uptime: 1w6d, expires: 12:45:50, via map-reply, self, complete
        #   Locator      Uptime    State      Pri/Wgt     Encap-IID
        #   10.8.129.94  1w6d      up          10/10        -
        # 10.16.0.26/32, uptime: 1w6d, expires: 12:52:40, via map-reply, self, complete
        #   Locator       Uptime    State      Pri/Wgt     Encap-IID
        #   10.8.129.124  1w6d      up          10/10        -
        # 10.16.0.27/32, uptime: 00:54:02, expires: 23:06:55, via map-reply, self, complete
        #   Locator      Uptime    State      Pri/Wgt     Encap-IID
        #   10.8.129.65  00:54:02  up          10/10        -
        # 10.16.0.28/32, uptime: 1w6d, expires: 20:44:39, via map-reply, self, complete
        #   Locator       Uptime    State      Pri/Wgt     Encap-IID
        #   10.8.129.112  1w6d      up          10/10        -
        # 10.16.0.29/32, uptime: 1w6d, expires: 20:44:39, via map-reply, self, complete
        #   Locator       Uptime    State      Pri/Wgt     Encap-IID
        #   10.8.129.138  1w6d      up          10/10        -

        # LISP IPv4 Mapping Cache for EID-table vrf User (IID 4100), 2186 entries
        p_lisp_header = re.compile(r"^LISP\s+IPv4\s+Mapping\s+Cache\s+for\s+EID-table\s+vrf\s+(?P<vrf>\S+)\s+"
                                   r"\(IID\s+(?P<iid>\d+)\),\s+(?P<entries>\d+)\s+entries$")

        # 0.0.0.0/0, uptime: 1w6d, expires: never, via static-send-map-request
        p_list_entry_1 = re.compile(r"(?P<ip>\S+),"
                                    r"\s+uptime:\s+(?P<uptime>[^,]+),"
                                    r"\s+expires:\s+(?P<expire>[^,]+),"
                                    r"\s+via\s+(?P<source>.*)")

        # Negative cache entry, action: send-map-request
        p_list_entry_negative = re.compile(r"^Negative\s+cache\s+entry,\s+"
                                           r"action:\s+(?P<action>.*)$")

        # Encapsulating to proxy ETR
        p_list_encapsulating = re.compile(r"^Encapsulating\s+to\s+proxy\s+ETR$")

        # 10.8.129.124  1w6d      up          10/10        -
        p_list_rloc = re.compile(r"(?P<locator>\S+)\s+(?P<uptime>\S+)\s+(?P<state>\S+)\s+(?P<pri>\d+)\/(?P<wgt>\d+)\s+(?P<encap>.*)")

        lisp_dict = {}
        current_entry = ""
        current_vrf = ""
        source_list = []

        for line in output.splitlines():
            line = line.strip()
            if p_lisp_header.match(line):
                # LISP IPv4 Mapping Cache for EID-table vrf User (IID 4100), 2186 entries
                match = p_lisp_header.match(line)
                current_vrf = match.group("vrf")
                lisp_dict.update({ "vrf": { current_vrf: {} }})
                lisp_dict["vrf"][current_vrf].update({ "iid": int(match.group("iid"))})
                lisp_dict["vrf"][current_vrf].update({ "number_of_entries": int(match.group("entries")) })
                continue
            elif p_list_entry_1.match(line):
                # 0.0.0.0/0, uptime: 1w6d, expires: never, via static-send-map-request
                match = p_list_entry_1.match(line)
                group = match.groupdict()
                lisp_dict["vrf"][current_vrf].setdefault("eid", {} )
                current_entry = match.group("ip")
                source_list = [x.strip() for x in group["source"].split(",")]
                lisp_dict["vrf"][current_vrf]["eid"].update({ current_entry: {} })
                lisp_dict["vrf"][current_vrf]["eid"][current_entry].update({ "uptime":  group["uptime"]} )
                lisp_dict["vrf"][current_vrf]["eid"][current_entry].update({ "expire":  group["expire"]} )
                lisp_dict["vrf"][current_vrf]["eid"][current_entry].update({ "via":  source_list} )
                continue
            elif p_list_entry_negative.match(line):
                # Negative cache entry, action: send-map-request
                match = p_list_entry_negative.match(line)
                lisp_dict["vrf"][current_vrf]["eid"][current_entry].update({ "rloc": { "status" : "Negative cache entry"}})
                lisp_dict["vrf"][current_vrf]["eid"][current_entry]['rloc'].update({ "action": match.group("action")})
                continue
            elif p_list_encapsulating.match(line):
                # Encapsulating to proxy ETR
                lisp_dict["vrf"][current_vrf]["eid"][current_entry].update({ "rloc": { "status": "Encapsulating to proxy ETR"}})
                continue
            elif p_list_rloc.match(line):
                # 10.8.129.124  1w6d      up          10/10        -
                match = p_list_rloc.match(line)
                group = match.groupdict()
                lisp_dict["vrf"][current_vrf]["eid"][current_entry].update({ "rloc": {} })
                lisp_dict["vrf"][current_vrf]["eid"][current_entry]["rloc"].update({ "ip": group["locator"] })
                lisp_dict["vrf"][current_vrf]["eid"][current_entry]["rloc"].update({ "uptime": group["uptime"] })
                lisp_dict["vrf"][current_vrf]["eid"][current_entry]["rloc"].update({ "state": group["state"] })
                lisp_dict["vrf"][current_vrf]["eid"][current_entry]["rloc"].update({ "priority": int(group["pri"]) })
                lisp_dict["vrf"][current_vrf]["eid"][current_entry]["rloc"].update({ "weight": int(group["wgt"]) })
                lisp_dict["vrf"][current_vrf]["eid"][current_entry]["rloc"].update({ "encap_iid": group["encap"] })
                continue



        return lisp_dict


# ==========================================
# Schema for:
#  * 'show lisp instance-id {instance_id} ethernet server'
# ==========================================
class ShowLispInstanceIdEthernetServerSchema(MetaParser):
    """Schema for show lisp instance-id {instance_id} ethernet server."""

    schema = {
        "instance_id": {
            int: {
                "lisp": int,
                Optional("site_name"): {
                    str: {
                        str: {
                            "last_register": str,
                            "up": str,
                            "who_last_registered": str,
                            "inst_id": int,
                        }
                    }
                },
            }
        }
    }

    
# ==========================================
# Parser for:
#  * 'show lisp instance-id {instance_id} ethernet server'
# ==========================================
class ShowLispInstanceIdEthernetServer(ShowLispInstanceIdEthernetServerSchema):
    """Parser for show lisp instance-id {instance_id} ethernet server"""

    cli_command = 'show lisp instance-id {instance_id} ethernet server'

    def cli(self, instance_id, output=None):
        if output is None:
            cmd = self.cli_command.format(instance_id=instance_id)
            out = self.device.execute(cmd)

        else:
            out = output

        # =================================================
        # Output for router lisp 0 instance-id 8188
        # =================================================
        # LISP Site Registration Information
        # * = Some locators are down or unreachable
        # # = Some registrations are sourced by reliable transport

        # Site Name      Last      Up     Who Last             Inst     EID Prefix
        #             Register         Registered           ID
        # site_uci       never     no     --                   8188     any-mac
        #             2w1d      yes#   10.8.130.4:61275     8188     1416.9dff.e928/48
        #             2w1d      yes#   10.8.130.4:61275     8188     1416.9dff.eae8/48
        #             2w1d      yes#   10.8.130.4:61275     8188     1416.9dff.eb28/48
        #             2w1d      yes#   10.8.130.4:61275     8188     1416.9dff.ebc8/48
        #             2w1d      yes#   10.8.130.4:61275     8188     1416.9dff.1328/48
        #             2w1d      yes#   10.8.130.4:61275     8188     1416.9dff.13e8/48
        # ...OUTPUT OMITTED...

        # Output for router lisp 0 instance-id 8188
        instant_id_capture = re.compile(
            r"^Output for router lisp (?P<lisp>\d+) instance-id (?P<instance_id>\d+)$"
        )

        # site_uci       never     no     --                   8188     any-mac
        site_name_capture = re.compile(
            r"^(?P<site_name>\S+)\s+(?P<last_register>\S+)\s+(?P<up>\S+)\s+(?P<who_last_registered>\-\-|\d+\.\d+\.\d+\.\d+\:\d+)\s+(?P<inst_id>\d+)\s+(?P<eid_prefix>any\-mac|\S+\.\S+\.\S+\d+)$"
        )

        #             2w1d      yes#   10.8.130.4:61275     8188     1416.9dff.e928/48
        lisp_info_capture = re.compile(
            r"^(?P<last_register>\S+)\s+(?P<up>\S+)\s+(?P<who_last_registered>\d+\.\d+\.\d+\.\d+\:\d+)\s+(?P<inst_id>\d+)\s+(?P<eid_prefix>\S+\.\S+\.\S+\d+)$"
        )

        tele_info_obj = {}

        for line in out.splitlines():
            line = line.strip()

            match = instant_id_capture.match(line)
            if match:
                group = match.groupdict()

                # convert str to int
                covert_list = ["lisp", "instance_id"]
                for item in covert_list:
                    group[item] = int(group[item])

                # pull a key from group to use as new_key
                new_key = "instance_id"
                new_group = {group[new_key]: {}}

                # update and pop new_key
                new_group[group[new_key]].update(group)
                new_group[group[new_key]].pop(new_key)

                if not tele_info_obj.get(new_key):
                    tele_info_obj[new_key] = {}

                tele_info_obj[new_key].update(new_group)

                instance_group = tele_info_obj[new_key][group[new_key]]

                continue

            match = site_name_capture.match(line)
            if match:
                group = match.groupdict()            
                
                # convert str to int
                group["inst_id"] = int(group["inst_id"])

                # pull a key from group to use as new_key
                new_key = "site_name"
                new_group = {group[new_key]: {}}

                temp_site_group = new_group[group[new_key]]

                # update and pop new_key
                temp_site_group.update(group)
                temp_site_group.pop(new_key)

                if not instance_group.get(new_key):
                    instance_group[new_key] = {}

                instance_group[new_key].update({group[new_key]: {}})

                site_group = instance_group[new_key][group[new_key]]

                # pull a key from group to use as new_key
                new_key = "eid_prefix"
                new_group = {temp_site_group[new_key]: {}}

                eid_group = new_group[temp_site_group[new_key]]

                # update and pop new_key
                eid_group.update(temp_site_group)
                eid_group.pop(new_key)

                site_group.update(new_group)

                continue

            match = lisp_info_capture.match(line)
            if match:
                group = match.groupdict()

                # # convert str to int
                group["inst_id"] = int(group["inst_id"])

                # pull a key from group to use as new_key
                new_key = "eid_prefix"
                new_group = {group[new_key]: {}}

                eid_group = new_group[group[new_key]]

                # update and pop new_key
                eid_group.update(group)
                eid_group.pop(new_key)

                site_group.update(new_group)

                continue

        return tele_info_obj


class ShowLispDynamicEidSummarySchema(MetaParser):

    ''' Schema for
            * show lisp {lisp_id} instance-id {instance_id} dynamic-eid summary
            * show lisp locator-table {vrf} instance-id {instance_id} dynamic-eid summary
            * show lisp instance-id {instance_id} dynamic-eid summary
            * show lisp eid-table vrf {vrf} dynamic-eid summary
            * show lisp eid-table vlan {vlan} dynamic-eid summary
            * show lisp eid-table {eid_table} dynamic-eid summary
    '''

    schema = {
        "lisp_id": {
            int: {
                "instance_id": {
                    int: {
                        Optional("eid_table"): str,
                        Optional("dynamic_eids"): {
                            str: {
                                "eids": {
                                    str: {
                                        "interface": str,
                                        "uptime": str,
                                        "last_packet": str,
                                        "pending_ping_count": int,
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

class ShowLispDynamicEidSummary(ShowLispDynamicEidSummarySchema):
    """ Parser for:
        * show lisp {lisp_id} instance-id {instance_id} dynamic-eid summary
        * show lisp locator-table {vrf} instance-id {instance_id} dynamic-eid summary
        * show lisp instance-id {instance_id} dynamic-eid summary
        * show lisp eid-table vrf {vrf} dynamic-eid summary
        * show lisp eid-table vlan {vlan} dynamic-eid summary
        * show lisp eid-table {eid_table} dynamic-eid summary
    """

    cli_command = [
       'show lisp {lisp_id} instance-id {instance_id} dynamic-eid summary',
       'show lisp locator-table {vrf} instance-id {instance_id} dynamic-eid summary',
       'show lisp instance-id {instance_id} dynamic-eid summary',
       'show lisp eid-table vrf {vrf} dynamic-eid summary',
       'show lisp eid-table vlan {vlan} dynamic-eid summary',
       'show lisp eid-table {eid_table} dynamic-eid summary',
       ]

    def cli(self, output=None, lisp_id=None, instance_id=None, vrf=None, vlan=None, eid_table=None):

        # init ret_dict
        ret_dict = {}

        if output is None:
            if lisp_id and instance_id:
                out = self.device.execute(self.cli_command[0].format(lisp_id=lisp_id, instance_id=instance_id))
            elif vrf and instance_id:
                out = self.device.execute(self.cli_command[1].format(vrf=vrf, instance_id=instance_id))
            elif instance_id:
                out = self.device.execute(self.cli_command[2].format(instance_id=instance_id))
            elif vrf:
                out = self.device.execute(self.cli_command[3].format(vrf=vrf))
            elif vlan:
                out = self.device.execute(self.cli_command[4].format(vlan=vlan))
            elif eid_table:
                out = self.device.execute(self.cli_command[5].format(eid_table=eid_table))
            else:
                return ret_dict
        else:
            out = output


        # LISP Dynamic EID Summary for router 0, IID 4100, EID-table VRF "red"
        # LISP Dynamic EID Summary for router 0, IID 101
        p1 = re.compile(r'^LISP +Dynamic +EID +Summary +for +router\s+(?P<lisp_id>\d+),\s+IID\s+'
                        r'(?P<instance_id>\d+)(, EID-table VRF\s+)?(?P<eid_table>.+)?$')

        # 192_168_1_0          192.168.1.1             Vl101         1d22h     never     0
        p2 = re.compile(r'^(?P<dynamic_eid_name>\S+)\s+(?P<eid>\S+)\s+(?P<interface>\S+)'
                        r'\s+(?P<uptime>\S+)\s+(?P<last_packet>\S+)\s+(?P<pending_ping_count>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            # LISP Dynamic EID Summary for router 0, IID 4100, EID-table VRF "red"
            # LISP Dynamic EID Summary for router 0, IID 101
            m = p1.match(line)
            if m:
                group = m.groupdict()
                lisp_id_dict = \
                    ret_dict.setdefault('lisp_id', {}) \
                        .setdefault(int(group['lisp_id']), {}) \
                        .setdefault('instance_id', {}) \
                        .setdefault(int(group['instance_id']), {})
                if group['eid_table']:
                    eid_table = group['eid_table'].replace('"','')
                    lisp_id_dict.update({'eid_table': eid_table})
                continue

            # 192_168_1_0          192.168.1.1             Vl101         1d22h     never     0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                dynamic_eid_dict = \
                    lisp_id_dict.setdefault('dynamic_eids', {})\
                                .setdefault(group['dynamic_eid_name'], {})
                each_eid_dict = \
                    dynamic_eid_dict.setdefault('eids', {})\
                                    .setdefault(group['eid'], {})

                # convert interface to full name
                interface = Common.convert_intf_name(group['interface'])

                each_eid_dict.update({
                    'interface': interface,
                    'uptime': group['uptime'],
                    'last_packet': group['last_packet'],
                    'pending_ping_count': int(group['pending_ping_count'])
                })
                continue

        return ret_dict

class ShowLispDynamicEidSchema(MetaParser):

    ''' Schema for
        * show lisp {lisp_id} instance-id {instance_id} dynamic-eid
        * show lisp locator-table {vrf} instance-id {instance_id} dynamic-eid
        * show lisp instance-id {instance_id} dynamic-eid
        * show lisp eid-table {eid_table} dynamic-eid
        * show lisp eid-table vrf {vrf} dynamic-eid
        * show lisp eid-table vlan {vlan} dynamic-eid
        * show lisp {lisp_id} instance-id {instance_id} dynamic-eid detail
        * show lisp locator-table {vrf} instance-id {instance-id} dynamic-eid detail
        * show lisp instance-id {instance_id} dynamic-eid detail
        * show lisp eid-table {eid-table} dynamic-eid detail
        * show lisp eid-table vrf {vrf} dynamic-eid detail
        * show lisp eid-table vlan {vlan} dynamic-eid detail
    '''

    schema = {
        'lisp_id': {
            int: {
                'instance_id': {
                    int: {
                        Optional('eid_table'): str,
                        Optional('dynamic_eids'): {
                            str: {
                                'database_mapping': {
                                    'eid_prefix': str,
                                    'locator_set': str
                                },
                                'map_servers': ListOf(str),
                                Optional('num_of_dynamic_eid'): int,
                                Optional('last_dyn_eid_discovered'): str,
                                Optional('eid_entries'): {
                                    str: {
                                        'interface': str,
                                        'uptime': str,
                                        'last_activity': str,
                                        'discovered_by': str
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

class ShowLispDynamicEidSuperParser(ShowLispDynamicEidSchema):
    """ Parser for:
        * show lisp {lisp_id} instance-id {instance_id} dynamic-eid
        * show lisp locator-table {vrf} instance-id {instance_id} dynamic-eid
        * show lisp instance-id {instance_id} dynamic-eid
        * show lisp eid-table {eid_table} dynamic-eid
        * show lisp eid-table vrf {vrf} dynamic-eid
        * show lisp eid-table vlan {vlan} dynamic-eid
        * show lisp {lisp_id} instance-id {instance_id} dynamic-eid detail
        * show lisp locator-table {vrf} instance-id {instance-id} dynamic-eid detail
        * show lisp instance-id {instance_id} dynamic-eid detail
        * show lisp eid-table {eid-table} dynamic-eid detail
        * show lisp eid-table vrf {vrf} dynamic-eid detail
        * show lisp eid-table vlan {vlan} dynamic-eid detail
    """

    def cli(self, output=None):

        ret_dict = {}

        # LISP Dynamic EID Information for router 0, IID 4100, EID-table VRF "red"
        # LISP Dynamic EID Information for router 0, IID 4100
        p1 = re.compile(r'^LISP +Dynamic +EID +Information +for +router\s+(?P<lisp_id>\d+),\s+IID\s+'
                        r'(?P<instance_id>\d+)(, EID-table VRF\s+)?(?P<eid_table>.+)?$')

        # Dynamic-EID name: 192_168_1_0
        p2 = re.compile(r'^Dynamic-EID name:\s+(?P<dynamic_eids>.+)$')

        # Database-mapping EID-prefix: 192.168.1.0/24, locator-set RLOC
        p3 = re.compile(r'^Database-mapping +EID-prefix:\s+(?P<eid_prefix>[\d.:\/\w\-]+),'
                        r'\s+locator-set\s+(?P<locator_set>.+)$')

        # Map-Server(s): none configured, use global Map-Server
        p4 = re.compile(r'^Map-Server\(s\):\s+(?P<map_servers>.+),.+$')

        # Map-Server(s): 1.1.1.1
        p4_1 = re.compile(r'^Map-Server\(s\):\s+(?P<map_servers>\d{1,3}\.\d{1,3}'
                          r'\.\d{1,3}\.\d{1,3})$')

        # Number of roaming dynamic-EIDs discovered: 2
        p5 = re.compile(r'^Number +of +roaming +dynamic-EIDs +discovered:'
                        r'\s+(?P<num_of_dynamic_eid>\d+)$')

        # Last dynamic-EID discovered: 192.168.1.1, 1d22h ago
        p6 = re.compile(r'^Last +dynamic-EID +discovered:\s+(?P<last_dyn_eid>[\d.:\/\w\-]+),.+$')

        # 2001:192:168:1::1, Vlan101, uptime: 1d22h
        p7 = re.compile(r'^(?P<eid>[\d.:\/\w\-]+),\s+(?P<interface>.+),\s+uptime:\s+(?P<uptime>.+)$')

        # last activity: never, discovered by: Device-tracking, do not register, no-roam
        p8 = re.compile(r'^last +activity:\s+(?P<last_activity>.+),\s+discovered +by:'
                        r'\s+(?P<discovered_by>([^,]+)).+$')

        for line in output.splitlines():
            line = line.strip()

            # LISP Dynamic EID Information for router 0, IID 4100, EID-table VRF "red"
            # LISP Dynamic EID Information for router 0, IID 4100
            m = p1.match(line)
            if m:
                group = m.groupdict()
                lisp_id_dict = \
                    ret_dict.setdefault('lisp_id', {}) \
                        .setdefault(int(group['lisp_id']), {}) \
                        .setdefault('instance_id', {}) \
                        .setdefault(int(group['instance_id']), {})
                if group['eid_table']:
                    eid_table = group['eid_table'].replace('"','')
                    lisp_id_dict.update({'eid_table': eid_table})
                continue

            # Dynamic-EID name: 192_168_1_0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                dyn_eid_dict = \
                    lisp_id_dict.setdefault('dynamic_eids', {})\
                                .setdefault(group['dynamic_eids'], {})
                continue

            # Database-mapping EID-prefix: 192.168.1.0/24, locator-set RLOC
            m = p3.match(line)
            if m:
                group = m.groupdict()
                database_mapping_dict = dyn_eid_dict.setdefault('database_mapping', {})
                database_mapping_dict.update({
                    'eid_prefix': group['eid_prefix'],
                    'locator_set': group['locator_set']
                })
                continue

            # Map-Server(s): none configured, use global Map-Server
            m = p4.match(line)
            if m:
                group = m.groupdict()
                map_server_list = dyn_eid_dict.setdefault('map_servers', [])
                continue

            # Map-Server(s): 1.1.1.1
            m = p4_1.match(line)
            if m:
                group = m.groupdict()
                map_server = group['map_servers']
                map_server_list = dyn_eid_dict.setdefault('map_servers', [])
                map_server_list.append(map_server)
                continue

            # Number of roaming dynamic-EIDs discovered: 2
            m = p5.match(line)
            if m:
                group = m.groupdict()
                dyn_eid_dict.update({'num_of_dynamic_eid': int(group['num_of_dynamic_eid'])})
                continue

            # Last dynamic-EID discovered: 192.168.1.1, 1d22h ago
            m = p6.match(line)
            if m:
                group = m.groupdict()
                dyn_eid_dict.update({'last_dyn_eid_discovered': group['last_dyn_eid']})
                continue

            # 2001:192:168:1::1, Vlan101, uptime: 1d22h
            m = p7.match(line)
            if m:
                group = m.groupdict()
                entries_dict = \
                    dyn_eid_dict.setdefault('eid_entries', {})\
                                .setdefault(group['eid'], {})

                # convert interface to full name
                interface = Common.convert_intf_name(group['interface'])

                entries_dict.update({
                    'interface': interface,
                    'uptime': group['uptime']
                })
                continue

            # last activity: never, discovered by: Device-tracking, do not register, no-roam
            m = p8.match(line)
            if m:
                group = m.groupdict()
                entries_dict.update({
                    'last_activity': group['last_activity'],
                    'discovered_by': group['discovered_by']
                })

        return ret_dict

class ShowLispDynamicEid(ShowLispDynamicEidSuperParser, ShowLispDynamicEidSchema):
    """ Parser for:
        * show lisp {lisp_id} instance-id {instance_id} dynamic-eid
        * show lisp locator-table {vrf} instance-id {instance_id} dynamic-eid
        * show lisp instance-id {instance_id} dynamic-eid
        * show lisp eid-table {eid_table} dynamic-eid
        * show lisp eid-table vrf {vrf} dynamic-eid
        * show lisp eid-table vlan {vlan} dynamic-eid
    """

    cli_command = [
        'show lisp {lisp_id} instance-id {instance_id} dynamic-eid',
        'show lisp locator-table {vrf} instance-id {instance_id} dynamic-eid',
        'show lisp instance-id {instance_id} dynamic-eid',
        'show lisp eid-table {eid_table} dynamic-eid',
        'show lisp eid-table vrf {vrf} dynamic-eid',
        'show lisp eid-table vlan {vlan} dynamic-eid',
    ]

    def cli(self, output=None, lisp_id=None, instance_id=None, vrf=None, vlan=None,
            eid_table=None):

        #init ret_dict
        ret_dict = {}

        if output is None:
            if lisp_id and instance_id:
                output = self.device.execute(self.cli_command[0].\
                                             format(lisp_id=lisp_id, instance_id=instance_id))
            elif vrf and instance_id:
                output = self.device.execute(self.cli_command[1].\
                                             format(vrf=vrf, instance_id=instance_id))
            elif instance_id:
                output = self.device.execute(self.cli_command[2].format(instance_id=instance_id))
            elif eid_table:
                output = self.device.execute(self.cli_command[3].format(eid_table=eid_table))
            elif vrf:
                output = self.device.execute(self.cli_command[4].format(vrf=vrf))
            elif vlan:
                output = self.device.execute(self.cli_command[5].format(vlan=vlan))
            else:
                return ret_dict
        else:
            output = output

        return super().cli(output=output)


class ShowLispDynamicEidAllDetail(ShowLispDynamicEidSuperParser, ShowLispDynamicEidSchema):
    """ Parser for:
        * show lisp {lisp_id} instance-id {instance_id} dynamic-eid detail
        * show lisp locator-table {vrf} instance-id {instance-id} dynamic-eid detail
        * show lisp instance-id {instance_id} dynamic-eid detail
        * show lisp eid-table {eid-table} dynamic-eid detail
        * show lisp eid-table vrf {vrf} dynamic-eid detail
        * show lisp eid-table vlan {vlan} dynamic-eid detail
    """

    cli_command = [
        'show lisp {lisp_id} instance-id {instance_id} dynamic-eid detail',
        'show lisp locator-table {vrf} instance-id {instance_id} dynamic-eid detail',
        'show lisp instance-id {instance_id} dynamic-eid detail',
        'show lisp eid-table {eid_table} dynamic-eid detail',
        'show lisp eid-table vrf {vrf} dynamic-eid detail',
        'show lisp eid-table vlan {vlan} dynamic-eid detail',
    ]

    def cli(self, output=None, lisp_id=None, instance_id=None, vrf=None, vlan=None,
            eid_table=None):

        # init ret_dict
        ret_dict = {}

        if output is None:
            if lisp_id and instance_id:
                output = self.device.execute(self.cli_command[0].\
                                             format(lisp_id=lisp_id, instance_id=instance_id))
            elif vrf and instance_id:
                output = self.device.execute(self.cli_command[1].\
                                             format(vrf=vrf, instance_id=instance_id))
            elif instance_id:
                output = self.device.execute(self.cli_command[2].format(instance_id=instance_id))
            elif eid_table:
                output = self.device.execute(self.cli_command[3].format(eid_table=eid_table))
            elif vrf:
                output = self.device.execute(self.cli_command[4].format(vrf=vrf))
            elif vlan:
                output = self.device.execute(self.cli_command[5].format(vlan=vlan))
            else:
                return ret_dict
        else:
            output = output

        return super().cli(output=output)

# ==========================================
# Schema for:
#  * 'show lisp instance-id {instance_id} ipv4 publication'
#  * 'show lisp {lisp_id} instance-id {instance_id} ipv4 publication'
#  * 'show lisp eid-table {eid-table} ipv4 publication'
#  * 'show lisp eid-table vrf {vrf} ipv4 publication'
#  * 'show lisp locator-table {vrf} instance-id {instance-id} ipv4 publication'
# ==========================================
class ShowLispIpv4PublicationSchema(MetaParser):
    """Schema for validaing output of ShowLispIpv4Publication"""
    schema = {
        'lisp_id': {
            int: {
                'instance_id': {
                    int: {
                        'total_entries': int,
                        'eid_prefix': {
                            str: { # EID Prefix
                                'publisher_ip': str,
                                'last_published': str,
                                'rloc': str,
                                'encap_iid': str
                            }
                        }
                    }
                }
            }
        }
    }

# ==========================================
# Parser for:
#  * 'show lisp instance-id {instance_id} ipv4 publication'
#  * 'show lisp {lisp_id} instance-id {instance_id} ipv4 publication'
#  * 'show lisp eid-table {eid-table} ipv4 publication'
#  * 'show lisp eid-table vrf {vrf} ipv4 publication'
#  * 'show lisp locator-table {vrf} instance-id {instance-id} ipv4 publication'
# ==========================================
class ShowLispIpv4Publication(ShowLispIpv4PublicationSchema):
    """Parser for show lisp ipv4 publication"""
    cli_command = ['show lisp instance-id {instance_id} ipv4 publication',
                   'show lisp {lisp_id} instance-id {instance_id} ipv4 publication',
                   'show lisp eid-table {eid_table} ipv4 publication',
                   'show lisp eid-table vrf {vrf} ipv4 publication',
                   'show lisp locator-table {vrf} instance-id {instance_id} ipv4 publication']

    def cli(self, lisp_id=None, instance_id=None, vrf=None, eid_table=None, output=None):
        if output is None:
            if lisp_id and instance_id:
                cmd = self.cli_command[1].format(lisp_id=lisp_id, instance_id=instance_id)
            elif vrf and instance_id:
                cmd = self.cli_command[4].format(vrf=vrf, instance_id=instance_id)
            elif instance_id:
                cmd = self.cli_command[0].format(instance_id=instance_id)
            elif eid_table:
                cmd = self.cli_command[2].format(eid_table=eid_table)
            else:
                cmd = self.cli_command[3].format(vrf=vrf)
            output = self.device.execute(cmd)
        lisp_v4_pub_dict = {}
        lisp_id_dict = {}
        instance_id_dict = {}
        publications_dict = {}
        #Output for router lisp 0
        p1 = re.compile(r"^Output\s+for\s+router\s+lisp\s+(?P<lisp_id>\d+)")

        #Output for router lisp 0 instance-id 4100
        p2 = re.compile(r"^Output\s+for\s+router\s+lisp\s+\d+\s+instance-id\s+(?P<instance_id>\d+)$")

        #Entries total 2
        p3 = re.compile(r"^Entries\s+total\s+(?P<total_entries>\d+)")

        #44.44.44.44     1d21h       192.168.1.71/32          11.11.11.11     -
        p4 = re.compile(r"^\S+\s+\S+\s+(?P<eid_prefix>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2}))")

        #44.44.44.44     1d21h       192.168.1.71/32          11.11.11.11     -
        p5 = re.compile(r"^(?P<publisher_ip>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}))\s+")

        #44.44.44.44     1d21h       192.168.1.71/32          11.11.11.11     -
        p6 = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+(?P<last_published>\S+)")

        #44.44.44.44     1d21h       192.168.1.71/32          11.11.11.11     -
        p7 = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+\S+\s+\d{1,3}\."
                        r"\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,3}\s+(?P<rloc>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})")

        #44.44.44.44     1d21h       192.168.1.71/32          11.11.11.11     -
        p8 = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+\S+\s+\S+\s+\S+\s+(?P<encap_iid>\S+)")

        #  Instance ID:                              4100
        p9 = re.compile(r"^\s+Instance\s+ID:\s+(?P<inst_id>\S+)")

        for line in output.splitlines():
            #Output for router lisp 0
            m=p1.match(line)
            if m:
                groups = m.groupdict()
                lisp_id = int(groups['lisp_id'])
                lisp_id_dict.setdefault(lisp_id,{})
                lisp_v4_pub_dict['lisp_id'] = lisp_id_dict
                #Output for router lisp 0 instance-id 4100
                m = p2.match(line)
                if m:
                    groups = m.groupdict()
                    instance_id = int(groups['instance_id'])
                    instance_id_dict.setdefault(instance_id,{})
                    lisp_v4_pub_dict['lisp_id'][lisp_id]['instance_id'] = instance_id_dict
                    continue
            if not m and line=="LISP Publication Information":
                if lisp_id and instance_id:
                    lisp_id = int(lisp_id)
                    lisp_id_dict.setdefault(lisp_id,{})
                    lisp_v4_pub_dict['lisp_id'] = lisp_id_dict
                    instance_id = int(instance_id)
                    instance_id_dict.setdefault(instance_id,{})
                    lisp_v4_pub_dict['lisp_id'][lisp_id]['instance_id'] = instance_id_dict
                    continue
                if not lisp_id and instance_id:
                    lisp_id = 0
                    lisp_id_dict.setdefault(lisp_id,{})
                    lisp_v4_pub_dict['lisp_id'] = lisp_id_dict
                    instance_id = int(instance_id)
                    instance_id_dict.setdefault(instance_id,{})
                    lisp_v4_pub_dict['lisp_id'][lisp_id]['instance_id'] = instance_id_dict
                    continue
                if not instance_id:
                    cmd =  "show lisp eid-table vrf red ipv4 | i Instance"
                    out =  self.device.execute(cmd)
                    for line in out.splitlines():
                        m=p9.match(line)
                        if m:
                            groups = m.groupdict()
                            inst_id = int(groups['inst_id'])
                            lisp_id = 0
                            lisp_id_dict.setdefault(lisp_id,{})
                            lisp_v4_pub_dict['lisp_id'] = lisp_id_dict
                            instance_id = inst_id
                            instance_id_dict.setdefault(instance_id,{})
                            lisp_v4_pub_dict['lisp_id'][lisp_id]['instance_id'] = instance_id_dict
                            continue
            #Entries total 2
            m=p3.match(line)
            if m:
                groups = m.groupdict()
                entries = int(groups['total_entries'])
                lisp_v4_pub_dict['lisp_id'][lisp_id]['instance_id'][instance_id]['total_entries'] = entries
                continue

            #44.44.44.44     1d21h       192.168.1.71/32          11.11.11.11
            m=p4.match(line)
            if m:
                groups = m.groupdict()
                publications = groups['eid_prefix']
                publications_dict.setdefault(publications,{})
                lisp_v4_pub_dict['lisp_id'][lisp_id]['instance_id'][instance_id]['eid_prefix'] = publications_dict
                #44.44.44.44     1d21h       192.168.1.71/32          11.11.11.11     -
                m=p5.match(line)
                if m:
                    groups = m.groupdict()
                    publisher_ip = groups['publisher_ip']
                    lisp_v4_pub_dict['lisp_id'][lisp_id]['instance_id'][instance_id]\
                        ['eid_prefix'][publications]['publisher_ip'] = publisher_ip
                #44.44.44.44     1d21h       192.168.1.71/32          11.11.11.11     -
                m=p6.match(line)
                if m:
                    groups = m.groupdict()
                    last_published = groups['last_published']
                    lisp_v4_pub_dict['lisp_id'][lisp_id]['instance_id'][instance_id]\
                        ['eid_prefix'][publications]['last_published'] = last_published
                #44.44.44.44     1d21h       192.168.1.71/32          11.11.11.11     -
                m=p7.match(line)
                if m:
                    groups = m.groupdict()
                    rloc = groups['rloc']
                    lisp_v4_pub_dict['lisp_id'][lisp_id]['instance_id'][instance_id]\
                        ['eid_prefix'][publications]['rloc'] = rloc
                #44.44.44.44     1d21h       192.168.1.71/32          11.11.11.11     -
                m=p8.match(line)
                if m:
                    groups = m.groupdict()
                    encap_iid = groups['encap_iid']
                    lisp_v4_pub_dict['lisp_id'][lisp_id]['instance_id'][instance_id]\
                        ['eid_prefix'][publications]['encap_iid'] = encap_iid
        return lisp_v4_pub_dict


# ==========================================
# Parser for:
#  * 'show lisp instance-id {instance_id} ipv6 publication'
#  * 'show lisp {lisp_id} instance-id {instance_id} ipv6 publication'
#  * 'show lisp eid-table {eid-table} ipv6 publication'
#  * 'show lisp eid-table vrf {vrf} ipv6 publication'
#  * 'show lisp locator-table {vrf} instance-id {instance-id} ipv6 publication'
# ==========================================
class ShowLispIpv6Publication(ShowLispIpv4PublicationSchema):
    """Parser for show lisp ipv4 publication"""
    cli_command = ['show lisp instance-id {instance_id} ipv6 publication',
                   'show lisp {lisp_id} instance-id {instance_id} ipv6 publication',
                   'show lisp eid-table {eid_table} ipv6 publication',
                   'show lisp eid-table vrf {vrf} ipv6 publication',
                   'show lisp locator-table {vrf} instance-id {instance_id} ipv6 publication']

    def cli(self, lisp_id=None, instance_id=None, vrf=None, eid_table=None, output=None):
        if output is None:
            if lisp_id and instance_id:
                cmd = self.cli_command[1].format(lisp_id=lisp_id, instance_id=instance_id)
            elif vrf and instance_id:
                cmd = self.cli_command[4].format(vrf=vrf, instance_id=instance_id)
            elif instance_id:
                cmd = self.cli_command[0].format(instance_id=instance_id)
            elif eid_table:
                cmd = self.cli_command[2].format(eid_table=eid_table)
            else:
                cmd = self.cli_command[3].format(vrf=vrf)
            output = self.device.execute(cmd)
        lisp_v6_pub_dict = {}
        lisp_id_dict = {}
        instance_id_dict = {}
        publications_dict = {}
        #Output for router lisp 0
        p1 = re.compile(r"^Output\s+for\s+router\s+lisp\s+(?P<lisp_id>\d+)")

        #Output for router lisp 0 instance-id 4100
        p2 = re.compile(r"^Output\s+for\s+router\s+lisp\s+\d+\s+instance-id\s+(?P<instance_id>\d+)$")

        #Entries total 2
        p3 = re.compile(r"^Entries\s+total\s+(?P<total_entries>\d+)")

        #100.14.14.14    01:11:02    2001:192:168:1::2/128    100.11.11.11    -
        p4 = re.compile(r"^\S+\s+\S+\s+(?P<eid_prefix>[a-fA-F\d\:]+\/\d{1,3})")

        #100.14.14.14    01:11:02    2001:192:168:1::2/128    100.11.11.11    -
        p5 = re.compile(r"^(?P<publisher_ip>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}))\s+")

        #100.14.14.14    01:11:02    2001:192:168:1::2/128    100.11.11.11    -
        p6 = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+(?P<last_published>\S+)")

        #100.14.14.14    01:11:02    2001:192:168:1::2/128    100.11.11.11    -
        p7 = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+\S+\s+[a-fA-F\d\:]+"
                        r"\/\d{1,3}\s+(?P<rloc>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})")

        #100.14.14.14    01:11:02    2001:192:168:1::2/128    100.11.11.11    -
        p8 = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+\S+\s+\S+\s+\S+\s+(?P<encap_iid>\S+)")

        #  Instance ID:                              4100
        p9 = re.compile(r"^\s+Instance\s+ID:\s+(?P<inst_id>\S+)")

        for line in output.splitlines():
            #Output for router lisp 0
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                lisp_id = int(groups['lisp_id'])
                lisp_id_dict.setdefault(lisp_id,{})
                lisp_v6_pub_dict['lisp_id'] = lisp_id_dict
                #Output for router lisp 0 instance-id 4100
                m = p2.match(line)
                if m:
                    groups = m.groupdict()
                    instance_id = int(groups['instance_id'])
                    instance_id_dict.setdefault(instance_id,{})
                    lisp_v6_pub_dict['lisp_id'][lisp_id]['instance_id'] = instance_id_dict
                    continue
            if not m and line=="LISP Publication Information":
                if lisp_id and instance_id:
                    lisp_id = int(lisp_id)
                    lisp_id_dict.setdefault(lisp_id,{})
                    lisp_v6_pub_dict['lisp_id'] = lisp_id_dict
                    instance_id = int(instance_id)
                    instance_id_dict.setdefault(instance_id,{})
                    lisp_v6_pub_dict['lisp_id'][lisp_id]['instance_id'] = instance_id_dict
                    continue
                if not lisp_id and instance_id:
                    lisp_id = 0
                    lisp_id_dict.setdefault(lisp_id,{})
                    lisp_v6_pub_dict['lisp_id'] = lisp_id_dict
                    instance_id = int(instance_id)
                    instance_id_dict.setdefault(instance_id,{})
                    lisp_v6_pub_dict['lisp_id'][lisp_id]['instance_id'] = instance_id_dict
                    continue
                if not instance_id:
                    cmd =  "show lisp eid-table vrf red ipv6 | i Instance"
                    out =  self.device.execute(cmd)
                    for line in out.splitlines():
                        m=p9.match(line)
                        if m:
                            groups = m.groupdict()
                            inst_id = int(groups['inst_id'])
                            lisp_id = 0
                            lisp_id_dict.setdefault(lisp_id,{})
                            lisp_v6_pub_dict['lisp_id'] = lisp_id_dict
                            instance_id = inst_id
                            instance_id_dict.setdefault(instance_id,{})
                            lisp_v6_pub_dict['lisp_id'][lisp_id]['instance_id'] = instance_id_dict
                            continue
            #Entries total 2
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                entries = int(groups['total_entries'])
                lisp_v6_pub_dict['lisp_id'][lisp_id]['instance_id'][instance_id]['total_entries'] = entries
                continue

            #100.14.14.14    01:11:02    2001:192:168:1::2/128    100.11.11.11    -
            m=p4.match(line)
            if m:
                groups = m.groupdict()
                publications = groups['eid_prefix']
                publications_dict.setdefault(publications,{})
                lisp_v6_pub_dict['lisp_id'][lisp_id]['instance_id'][instance_id]['eid_prefix'] = publications_dict

                #100.14.14.14    01:11:02    2001:192:168:1::2/128    100.11.11.11    -
                m=p5.match(line)
                if m:
                    groups = m.groupdict()
                    publisher_ip = groups['publisher_ip']
                    lisp_v6_pub_dict['lisp_id'][lisp_id]['instance_id'][instance_id]\
                        ['eid_prefix'][publications]['publisher_ip'] = publisher_ip
                #100.14.14.14    01:11:02    2001:192:168:1::2/128    100.11.11.11    -
                m=p6.match(line)
                if m:
                    groups = m.groupdict()
                    last_published = groups['last_published']
                    lisp_v6_pub_dict['lisp_id'][lisp_id]['instance_id'][instance_id]\
                        ['eid_prefix'][publications]['last_published'] = last_published
                #100.14.14.14    01:11:02    2001:192:168:1::2/128    100.11.11.11    -
                m=p7.match(line)
                if m:
                    groups = m.groupdict()
                    rloc = groups['rloc']
                    lisp_v6_pub_dict['lisp_id'][lisp_id]['instance_id'][instance_id]\
                        ['eid_prefix'][publications]['rloc'] = rloc
                #100.14.14.14    01:11:02    2001:192:168:1::2/128    100.11.11.11    -
                m=p8.match(line)
                if m:
                    groups = m.groupdict()
                    encap_iid = groups['encap_iid']
                    lisp_v6_pub_dict['lisp_id'][lisp_id]['instance_id'][instance_id]\
                        ['eid_prefix'][publications]['encap_iid'] = encap_iid
        return lisp_v6_pub_dict


class ShowLispPrefixListSchema(MetaParser):

    """
    Schema for show lisp prefix-list <name>
    """
    schema = {
        'lisp_id': {
            int: {
                'prefix_list_name': {
                    str:{
                        'number_of_entries': int,
                        Optional('users'):
                            ListOf({
                                Optional(str): str
                                }),
                        'entries':{
                            str:{
                                'sources': str,
                                'first_added': str,
                                'last_verified_by':  str,
                                'last_verified': str
                                }
                            }
                        }
                    }
                }
            }
        }


'''Parser for "show lisp prefix-list"'''
class ShowLispPrefixList(ShowLispPrefixListSchema):

    '''Parser for "show lisp prefix-list"'''
    cli_command = ['show lisp prefix-list',
                   'show lisp prefix-list {prefix_list_name}',
                   'show lisp {lisp_id} prefix-list',
                   'show lisp {lisp_id} prefix-list {prefix_list_name}']

    def cli(self, lisp_id=None, instance_id=None, prefix_list_name=None, output=None):
        if output is None:
            if lisp_id and prefix_list_name:
                cmd = self.cli_command[3].format(lisp_id=lisp_id, prefix_list_name=prefix_list_name)
            elif prefix_list_name:
                cmd = self.cli_command[1].format(prefix_list_name=prefix_list_name)
            elif lisp_id:
                cmd = self.cli_command[2].format(lisp_id=lisp_id)
            else:
                cmd = self.cli_command[0]
            output = self.device.execute(cmd)
        lisp_prefix_dict = {}

        #LISP Prefix List information for router lisp 0
        p1 = re.compile(r"^LISP Prefix List information for router lisp\s+(?P<lisp_prefix_id>\d+)$")

        #Prefix List: site1
        p2 = re.compile(r"^Prefix\s+List:\s+(?P<prefix_list_name>\S+)$")

        #Number of entries: 2
        p3 = re.compile(r"^\s+Number\s+of\s+entries:\s+(?P<no_entries>\d+)")

        #ITR Map Resolver    100.100.100.100|2001:192:168:1::
        p4 = re.compile(r"^\s+ITR\s+Map\s+Resolver\s+(?P<itr_map_resolver_ip>[0-9a-fA-F\d:]+|\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})$")

        #ETR Map Server      44.44.44.44|2001:192:168:1::
        p5 = re.compile(r"^\s+ETR\s+Map\s+Server\s+(?P<etr_map_server_ip>[0-9a-fA-F\d:]+|\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})$")

        #Import Publication
        p6 = re.compile(r"^\s+Import\s+Publication(?P<import_publication>\s)")

        #Import
        p7 = re.compile(r"^\s+Import(?P<import>\s)")

        #Route Import
        p8 = re.compile(r"^\s+Route\s+Import(?P<route_import>\s)")

        #192.168.1.0/24|2001:192:168:1::/64
        p9 = re.compile(r"^\s+(?P<eid_prefix>[0-9a-fA-F\d:]+\/\d+|\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2})$")

        #Sources: static
        p10 = re.compile(r"^\s+Sources:\s+(?P<prefix_source>\S+)$")

        #First added: 00:09:20
        p11 = re.compile(r"^\s+First added:\s+(?P<first_added>\S+),")

        #last verified: by static
        p12 = re.compile(r"^\s+First added:\s+\S+\s+last verified:\s+(?P<last_verified_by>\S+\s+\S+),")

        #00:09:20
        p13 = re.compile(r"^\s+First added:\s+\S+\s+last verified:\s\S+\s+\S+,\s+(?P<last_verified>\S+)")

        for line in output.splitlines():
            #LISP Prefix List information for router lisp 0
            m=p1.match(line)
            if m:
                groups = m.groupdict()
                prefix_id = int(groups['lisp_prefix_id'])
                lisp_id_dict = lisp_prefix_dict.setdefault('lisp_id',{})\
                    .setdefault(prefix_id,{})
                continue

            #Prefix List: site1
            m=p2.match(line)
            if m:
                groups = m.groupdict()
                prefix_list_name = groups['prefix_list_name']
                prefix_dict = lisp_id_dict.setdefault('prefix_list_name',{})\
                    .setdefault(prefix_list_name,{})
                continue

            #Number of entries: 2
            m=p3.match(line)
            if m:
                groups = m.groupdict()
                no_entries = int(groups['no_entries'])
                prefix_dict.update({'number_of_entries':no_entries})
                continue

            #ITR Map Resolver    100.100.100.100|2001:192:168:1::
            m=p4.match(line)
            if m:
                groups = m.groupdict()
                itr_ip = groups['itr_map_resolver_ip']
                itr_list = prefix_dict.setdefault('users',[])
                itr_dict = {}
                itr_dict.update({'itr_map_resolver' : itr_ip})
                itr_list.append(itr_dict)
                itr_dict={}
                prefix_dict.update({'users':itr_list})
                continue

            #ETR Map Server      44.44.44.44|2001:192:168:1::
            m=p5.match(line)
            if m:
                groups = m.groupdict()
                etr_ip = groups['etr_map_server_ip']
                itr_dict.update({'etr_map_server' : etr_ip})
                itr_list.append(itr_dict)
                itr_dict = {}
                prefix_dict.update({'users':itr_list})
                continue

            #Import Publication
            m=p6.match(line)
            if m:
                groups = m.groupdict()
                import_user = groups['import_publication']
                itr_dict.update({'import_publication' : import_user})
                itr_list.append(itr_dict)
                itr_dict = {}
                prefix_dict.update({'users':itr_list})
                continue

            #Import
            m=p7.match(line)
            if m:
                groups = m.groupdict()
                import_publication = groups['import']
                itr_dict.update({'import' : import_publication})
                itr_list.append(itr_dict)
                itr_dict = {}
                prefix_dict.update({'users':itr_list})
                continue

            #Route Import
            m=p8.match(line)
            if m:
                groups = m.groupdict()
                route_import = groups['route_import']
                itr_dict.update({'route_import' : route_import})
                itr_list.append(itr_dict)
                itr_dict = {}
                prefix_dict.update({'users':itr_list})
                continue

            #192.168.1.0/24|2001:192:168:1::/64
            m=p9.match(line)
            if m:
                groups = m.groupdict()
                resolver_ip = groups['eid_prefix']
                dynamic_eid_dict = \
                    prefix_dict.setdefault('entries', {})\
                                    .setdefault(resolver_ip, {})
                continue

            #Sources: static
            m=p10.match(line)
            if m:
                groups = m.groupdict()
                source = groups['prefix_source']
                dynamic_eid_dict.update({'sources' : source})
                continue

            #First added: 00:09:20
            m=p11.match(line)
            if m:
                groups = m.groupdict()
                first_add = groups['first_added']
                dynamic_eid_dict.update({'first_added' : first_add})

                m=p12.match(line)
                if m:
                    groups = m.groupdict()
                    last_verified_by = groups['last_verified_by']
                    dynamic_eid_dict.update({'last_verified_by' : last_verified_by})

                #00:09:20
                m=p13.match(line)
                if m:
                    groups = m.groupdict()
                    last_Verified = groups['last_verified']
                    dynamic_eid_dict.update({'last_verified' : last_Verified})
        return lisp_prefix_dict

class ShowLispRouteImportMapCacheSchema(MetaParser):
    '''
    Schema for Lisp Route Import Map Cache
    'show lisp instance-id {instance_id} ipv4 route-import map-cache',
    'show lisp instance-id {instance_id} ipv4 route-import map-cache {eid}',
    'show lisp instance-id {instance_id} ipv4 route-import map-cache {eid_prefix}',
    'show lisp {lisp_id} instance-id {instance_id} ipv4 route-import map-cache',
    'show lisp {lisp_id} instance-id {instance_id} ipv4 route-import map-cache {eid}',
    'show lisp {lisp_id} instance-id {instance_id} ipv4 route-import map-cache {eid_prefix}',
    'show lisp eid-table vrf {vrf} ipv4 route-import map-cache',
    'show lisp eid-table vrf {vrf} ipv4 route-import map-cache {eid}',
    'show lisp eid-table vrf {vrf} ipv4 route-import map-cache {eid_prefix}',
    'show lisp eid-table {eid_table} ipv4 route-import map-cache',
    'show lisp eid-table {eid_table} ipv4 route-import map-cache {eid}',
    'show lisp eid-table {eid_table} ipv4 route-import map-cache {eid_prefix}'
    'show lisp locator-table {locator_table} instance-id {instance_id} ipv4 route-import map-cache'
    'show lisp locator-table {locator_table} instance-id {instance_id} ipv4 route-import map-cache {eid}'
    'show lisp locator-table {locator_table} instance-id {instance_id} ipv4 route-import map-cache {eid_prefix}'
    '''
    schema = {
    'lisp_id': {
           int :  {
               'instance_id': {
                    int : {
                        'eid_table': str,
                        'config': int,
                        'entries': int,
                        'limit': int,
                        'eids':  {
                            'str':  {
                                'uptime': str,
                                'source': str,
                                Optional('rloc_set'): str,
                                'cache_db' : str,
                                Optional('state'): str
                            }

                        }
                    }
                }
            }
        }
    }



class ShowLispRouteImportMapCacheSuperParser(ShowLispRouteImportMapCacheSchema):
    ''' Super Parser for Route Import Map-Cache
        'show lisp instance-id {instance_id} ipv4 route-import map-cache',
        'show lisp instance-id {instance_id} ipv4 route-import map-cache {eid}',
        'show lisp instance-id {instance_id} ipv4 route-import map-cache {eid_prefix}',
        'show lisp {lisp_id} instance-id {instance_id} ipv4 route-import map-cache',
        'show lisp {lisp_id} instance-id {instance_id} ipv4 route-import map-cache {eid}',
        'show lisp {lisp_id} instance-id {instance_id} ipv4 route-import map-cache {eid_prefix}',
        'show lisp eid-table vrf {vrf} ipv4 route-import map-cache',
        'show lisp eid-table vrf {vrf} ipv4 route-import map-cache {eid}',
        'show lisp eid-table vrf {vrf} ipv4 route-import map-cache {eid_prefix}',
        'show lisp eid-table {eid_table} ipv4 route-import map-cache',
        'show lisp eid-table {eid_table} ipv4 route-import map-cache {eid}',
        'show lisp eid-table {eid_table} ipv4 route-import map-cache {eid_prefix}'
        'show lisp locator-table {locator_table} instance-id {instance_id} ipv4 route-import map-cache'
        'show lisp locator-table {locator_table} instance-id {instance_id} ipv4 route-import map-cache {eid}'
        'show lisp locator-table {locator_table} instance-id {instance_id} ipv4 route-import map-cache {eid_prefix}'
    '''
    def cli(self, output=None):
        parsed_dict = {}

        # LISP IPv4 imported routes for EID-table vrf blue (IID 102)
        # LISP IPv4 imported routes for LISP 1 EID-table vrf red (IID 105)
        p1 = re.compile(r'LISP +IPv(?P<v4_v6>[4-6]) +imported +routes +for(\sLISP\s)?(\s?P<lisp_id>\d)? +EID-table(\svrf)? +(?P<vrf>.+) +\(+IID +(?P<instance_id>\d+)+\)$')

        # Config: 2, Entries: 1 (limit 5000)
        p2 = re.compile(r'Config: +(?P<config>\d+), +Entries: +(?P<entries>\d+) +\(+limit+ (?P<limit>\d+)+\)$')

        # 50.1.1.0/24               00:00:13  static                          installed
        p3 = re.compile(r'(?P<eid>[\da-fA-F.:]+\/\d+\S+) +(?P<uptime>\d{1,2}:\d{2}:\d{2}) +(?P<source>.+\S+) +(?P<rloc>.+\S+)? +(?P<cached>none|installed|replaced|full\S+)+(?P<state>.+)?$')

        for line in output.splitlines():
            line = line.strip()
            # LISP IPv4 imported routes for EID-table vrf blue (IID 102)
            # LISP IPv4 imported routes for LISP 1 EID-table vrf red (IID 105)

            m = p1.match(line)
            if m:
                group = m.groupdict()
                if 'lisp_id' not in group:
                    lisp_id = 0
                instance_id = int(group['instance_id'])
                lisp_id_dict = \
                    parsed_dict.setdefault('lisp_id', {}) \
                               .setdefault(int(group['lisp_id']), {})
                instance_id_dict = \
                    lisp_id_dict.setdefault('instance_id', {})\
                                .setdefault(instance_id, {})

                lisp_id_dict.update({'eid_table': group['eid_table']})
                continue


            # Config: 2, Entries: 1 (limit 5000)
            m = p2.match(line)
            if m:
               group = m.groupdict()
               instance_id_dict.update({'config': group['config']})
               instance_id_dict.update({'entries': group['entries']})
               instance_id_dict.update({'limit': group['limit']})
               continue

            # 50.1.1.0/24               00:00:13  static                          installed
            m = p3.match(line)
            if m:
               group = m.groupdict()
               eid_dict = \
                   instance_id_dict.setdefault('eid',{})\
                                   .setdefault(group['eid'],{})
               eid_dict.update({'uptime': group['uptime']})
               eid_dict.update({'source': group['source']})
               eid_dict.update({'cached': group['cached']})

               if 'rloc' in group:
                   eid_dict.update({'rloc': group['rloc']})

               if 'state' in group:
                   eid_dict.update({'state': group['state']})

        return parsed_dict

class ShowLispIpv4RouteImport(ShowLispRouteImportMapCacheSuperParser,ShowLispRouteImportMapCacheSchema):
      '''route Import map-cache cli variations'''
      cli_command = [
        'show lisp instance-id {instance_id} ipv4 route-import map-cache',
        'show lisp instance-id {instance_id} ipv4 route-import map-cache {eid}',
        'show lisp instance-id {instance_id} ipv4 route-import map-cache {eid_prefix}',
        'show lisp {lisp_id} instance-id {instance_id} ipv4 route-import map-cache',
        'show lisp {lisp_id} instance-id {instance_id} ipv4 route-import map-cache {eid}',
        'show lisp {lisp_id} instance-id {instance_id} ipv4 route-import map-cache {eid_prefix}',
        'show lisp eid-table vrf {vrf} ipv4 route-import map-cache',
        'show lisp eid-table vrf {vrf} ipv4 route-import map-cache {eid}',
        'show lisp eid-table vrf {vrf} ipv4 route-import map-cache {eid_prefix}',
        'show lisp eid-table {eid_table} ipv4 route-import map-cache',
        'show lisp eid-table {eid_table} ipv4 route-import map-cache {eid}',
        'show lisp eid-table {eid_table} ipv4 route-import map-cache {eid_prefix}',
        'show lisp locator-table {locator_table} instance-id {instance_id} ipv4 route-import map-cache',
        'show lisp locator-table {locator_table} instance-id {instance_id} ipv4 route-import map-cache {eid}',
        'show lisp locator-table {locator_table} instance-id {instance_id} ipv4 route-import map-cache {eid_prefix}'
      ]

      def cli(self, output=None, lisp_id=None, instance_id=None, locator_table=None,
            eid_table=None, eid=None, vrf=None, eid_prefix=None):

          if output is None:
             if lisp_id and instance_id and eid:
                 output = self.device.execute(self.cli_command[4].\
                                             format(lisp_id=lisp_id, instance_id=instance_id, eid=eid))
             elif lisp_id and instance_id and eid_prefix :
                 output = self.device.execute(self.cli_command[5].\
                                             format(lisp_id=lisp_id, instance_id=instance_id, eid_prefix=eid_prefix))
             elif lisp_id and instance_id:
                 output = self.device.execute(self.cli_command[3].\
                                             format(lisp_id=lisp_id, instance_id=instance_id))
             elif instance_id and eid:
                 output = self.device.execute(self.cli_command[1].\
                                             format(instance_id=instance_id, eid=eid))
             elif instance_id and eid_prefix:
                 output = self.device.execute(self.cli_command[2].\
                                             format(instance_id=instance_id, eid_prefix=eid_prefix))
             elif instance_id:
                 output = self.device.execute(self.cli_command[0].\
                                             format(instance_id=instance_id))
             elif vrf and eid:
                 output = self.device.execute(self.cli_command[7].\
                                             format(vrf=vrf, eid=eid))
             elif vrf and eid_prefix:
                 output = self.device.execute(self.cli_command[8].\
                                             format(vrf=vrf, eid_prefix=eid_prefix))
             elif vrf:
                 output = self.device.execute(self.cli_command[6].\
                                             format(vrf=vrf))
             elif eid_table and eid:
                 output = self.device.execute(self.cli_command[10].\
                                             format(eid_table=eid_table, eid=eid))
             elif eid_table and eid:
                 output = self.device.execute(self.cli_command[11].\
                                             format(eid_table=eid_table, eid_prefix=eid_prefix))
             elif eid_table:
                 output = self.device.execute(self.cli_command[9].\
                                             format(eid_table=eid_table))
             elif locator_table and instance_id and eid_prefix:
                 output = self.device.execute(self.cli_command[14].\
                                             format(locator_table=locator_table, eid_prefix=eid_prefix))
             elif locator_table and instance_id and eid:
                 output = self.device.execute(self.cli_command[13].\
                                             format(locator_table=locator_table, eid=eid))
             else:
                 output = self.device.execute(self.cli_command[12].\
                                             format(locator_table=locator_table))
          else:
              output = output
          return super().cli(output=output)

class ShowLispEidAwaySchema(MetaParser):
    '''Metaparser for Show Lisp Ipv4 away command'''

    schema = {
        'lisp_id': {
            int :  {
                'instance_id': {
                    int : {
                        'vrf': str,
                        Optional('entries'): int,
                        'eid_prefix': {
                            str: {
                            'producer': str,
                            'created' : str
                            }
                        }
                    }
                }
            }
        }
    }

class ShowLispEidAwaySuperParser(ShowLispEidAwaySchema):
    ''' Super Parser for show lisp away command'''
    '''
        Commands are:
        show lisp instance-id {instance_id} ipv4 away
        show lisp instance-id {instance_id} ipv4 away {eid}
        show lisp instance-id {instance_id} ipv4 away {eid_prefix}
        show lisp {lisp_id} instance-id {instance_id} ipv4 away
        show lisp {lisp_id} instance-id {instance_id} ipv4 away {eid}
        show lisp {lisp_id} instance-id {instance_id} ipv4 away {eid_prefix}
        show lisp locator-table {locator_table} instance-id {instance_id} ipv4 away
        show lisp locator-table {locator_table} instance-id {instance_id} ipv4 away {eid}
        show lisp locator-table {locator_table} instance-id {instance_id} ipv4 away {eid_prefix}
        show lisp eid-table {eid_table} ipv4 away
        show lisp eid-table {eid_table} ipv4 away {eid}
        show lisp eid-table {eid_table} ipv4 away {eid_prefix}
        show lisp eid-table vrf {eid_table} ipv4 away
        show lisp eid-table vrf {eid_table} ipv4 away {eid}
        show lisp eid-table vrf {eid_table} ipv4 away {eid_prefix}
    '''
    def cli(self, output=None):
        parsed_dict = {}
        # LISP Away Table for router lisp 0 (blue) IID 102
        p1 = re.compile(r'^LISP +Away +Table +for +router +lisp (?P<lisp_id>\d+) +\((?P<vrf>.+)\) +IID +(?P<instance_id>\d+)$')
        # Entries: 1
        p2 = re.compile(r'^Entries: +(?P<entries>\d+)$')
        # 10.1.0.0/16                             dyn-eid                        4d20h
        p3 = re.compile(r'^(?P<eid_prefix>[\da-fA-F.:]+\S+) +(?P<producer>\S+) +(?P<created>\S+)$')
        for line in output.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                lisp_id_dict = \
                    parsed_dict.setdefault('lisp_id', {}) \
                        .setdefault(int(group['lisp_id']), {})
                instance_id_dict = \
                    lisp_id_dict.setdefault('instance_id', {}) \
                        .setdefault(int(group['instance_id']), {})
                instance_id_dict.update({'vrf': group['vrf'].strip('(').strip(')')})

                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                instance_id_dict.update({'entries': int(group['entries'])})
                continue

            m = p3.match(line)
            if m:
                group = m.groupdict()
                eid_prefix_dict = instance_id_dict.setdefault('eid_prefix',{})\
                                                    .setdefault(str(group['eid_prefix']), {})
                eid_prefix_dict.update({'producer': group['producer'].strip()})
                eid_prefix_dict.update({'created': group['created'].strip()})
                continue

        return parsed_dict

class ShowLispIpv4Away(ShowLispEidAwaySuperParser, ShowLispEidAwaySchema):
    ''' Show Command Ipv4 Away
        show lisp instance-id {instance_id} ipv4 away
        show lisp instance-id {instance_id} ipv4 away {eid}
        show lisp instance-id {instance_id} ipv4 away {eid_prefix}
        show lisp {lisp_id} instance-id {instance_id} ipv4 away
        show lisp {lisp_id} instance-id {instance_id} ipv4 away {eid}
        show lisp {lisp_id} instance-id {instance_id} ipv4 away {eid_prefix}
        show lisp locator-table {locator_table} instance-id {instance_id} ipv4 away
        show lisp locator-table {locator_table} instance-id {instance_id} ipv4 away {eid}
        show lisp locator-table {locator_table} instance-id {instance_id} ipv4 away {eid_prefix}
        show lisp eid-table {eid_table} ipv4 away
        show lisp eid-table {eid_table} ipv4 away {eid}
        show lisp eid-table {eid_table} ipv4 away {eid_prefix}
        show lisp eid-table vrf {eid_table} ipv4 away
        show lisp eid-table vrf {eid_table} ipv4 away {eid}
        show lisp eid-table vrf {eid_table} ipv4 away {eid_prefix}
    '''

    cli_command = [
        'show lisp instance-id {instance_id} ipv4 away',
        'show lisp instance-id {instance_id} ipv4 away {eid}',
        'show lisp instance-id {instance_id} ipv4 away {eid_prefix}',
        'show lisp {lisp_id} instance-id {instance_id} ipv4 away',
        'show lisp {lisp_id} instance-id {instance_id} ipv4 away {eid}',
        'show lisp {lisp_id} instance-id {instance_id} ipv4 away {eid_prefix}',
        'show lisp locator-table {locator_table} instance-id {instance_id} ipv4 away',
        'show lisp locator-table {locator_table} instance-id {instance_id} ipv4 away {eid}',
        'show lisp locator-table {locator_table} instance-id {instance_id} ipv4 away {eid_prefix}',
        'show lisp eid-table {eid_table} ipv4 away',
        'show lisp eid-table {eid_table} ipv4 away {eid}',
        'show lisp eid-table {eid_table} ipv4 away {eid_prefix}',
        'show lisp eid-table vrf {vrf} ipv4 away',
        'show lisp eid-table vrf {vrf} ipv4 away {eid}',
        'show lisp eid-table vrf {vrf} ipv4 away {eid_prefix}'
    ]

    def cli(self, output=None, lisp_id=None, instance_id=None, vrf=None, locator_table=None,
            eid_table=None, eid=None, eid_prefix=None):
        if output is None:
            if lisp_id and instance_id and eid:
                output = self.device.execute(self.cli_command[4].\
                                                format(lisp_id=lisp_id, instance_id=instance_id, eid=eid))
            elif lisp_id and instance_id and eid_prefix:
                output = self.device.execute(self.cli_command[5].\
                                                format(lisp_id=lisp_id, instance_id=instance_id, eid_prefix=eid_prefix))
            elif lisp_id and instance_id:
                output = self.device.execute(self.cli_command[3].\
                                                format(lisp_id=lisp_id, instance_id=instance_id))
            elif instance_id and eid:
                output = self.device.execute(self.cli_command[1].\
                                                format(instance_id=instance_id, eid= eid))
            elif instance_id and eid_prefix:
                output = self.device.execute(self.cli_command[2].\
                                                format(instance_id=instance_id, eid_prefix=eid_prefix))
            elif instance_id:
                output = self.device.execute(self.cli_command[0].\
                                                format(instance_id=instance_id))
            elif locator_table and instance_id and eid:
                output = self.device.execute(self.cli_command[7].\
                                                format(locator_table=locator_table, instance_id=instance_id, eid=eid))
            elif locator_table and instance_id and eid_prefix:
                output = self.device.execute(self.cli_command[8].\
                                                format(locator_table=locator_table, instance_id=instance_id, eid_prefix=eid_prefix))
            elif locator_table and instance_id:
                output = self.device.execute(self.cli_command[6].\
                                                format(locator_table=locator_table, instance_id=instance_id))
            elif eid_table and eid:
                output = self.device.execute(self.cli_command[10].\
                                                format(eid_table=eid_table, eid=eid))
            elif eid_table and eid_prefix:
                output = self.device.execute(self.cli_command[11].\
                                                format(eid_table=eid_table, eid_prefix=eid_prefix))
            elif eid_table:
                output = self.device.execute(self.cli_command[9].\
                                                format(eid_table=eid_table))
            elif vrf and eid:
                output = self.device.execute(self.cli_command[13].\
                                                format(vrf=vrf, eid=eid))
            elif vrf and eid_prefix:
                output = self.device.execute(self.cli_command[14].\
                                                format(vrf=vrf, eid_prefix=eid_prefix))
            else:
                output = self.device.execute(self.cli_command[12].\
                                                format(vrf=vrf))
        else:
            output = output

        return super().cli(output=output)

# ==========================================
# Parser for: show lisp session redundancy
# ==========================================
class ShowLispSessionRedundancySchema(MetaParser):
    schema = {
        'passive_sessions': {
            'synced': int,
            'pending_tcp_action': int,
            'pending_checkpoints': int
        },
        'listeners': {
            'synced': int,
            'pending_tcp_action': int,
            'pending_checkpoints': int
        }
    }

class ShowLispSessionRedundancy(ShowLispSessionRedundancySchema):
    cli_command = 'show lisp session redundancy'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        lisp_dict = {}

        #  Passive sessions
        p1 = re.compile(r"^Passive sessions$")

        #  Listeners
        p2 = re.compile(r"^Listeners$")

        #    Synced/pending TCP action/pending checkpoint: 7/0/3
        p3 = re.compile(r"^Synced\/pending\sTCP\saction\/pending\scheckpoint:\s(?P<synced>\d+)\/(?P<pending_tcp_action>\d+)\/(?P<pending_checkpoints>\d+)$")

        for line in output.splitlines():
            line = line.strip()

            #  Passive sessions
            m=p1.match(line)
            if m:
                currently_parsing_passive_session = True
                passive_sessions_dict = lisp_dict.setdefault('passive_sessions', {})
                continue

            #  Listeners
            m=p2.match(line)
            if m:
                currently_parsing_passive_session = False
                listeners_dict = lisp_dict.setdefault('listeners', {})
                continue

            #  Synced/pending TCP action/pending checkpoint: 7/0/3
            m=p3.match(line)
            if m:
                group = m.groupdict()
                if currently_parsing_passive_session:
                    passive_sessions_dict['synced'] = int(group['synced'])
                    passive_sessions_dict['pending_tcp_action'] = int(group['pending_tcp_action'])
                    passive_sessions_dict['pending_checkpoints'] = int(group['pending_checkpoints'])
                else:
                    listeners_dict['synced'] = int(group['synced'])
                    listeners_dict['pending_tcp_action'] = int(group['pending_tcp_action'])
                    listeners_dict['pending_checkpoints'] = int(group['pending_checkpoints'])
                continue

        return lisp_dict


class ShowLispARSchema(MetaParser):

    schema = {
        'lisp_id': {
            int: {
                'instance_id': {
                    int: {
                        Optional('entries'): {
                            str: {
                                'mac_address': str,
                                'inst_id': str
                            },
                        }
                    }
                }
            }
        }
    }


# ==========================================
# Parser for:
#   'Parser for show lisp instance-id <id> ethernet server address-resolution'
# ==========================================
class ShowLispAR(ShowLispARSchema):
    cli_command = ["show lisp {lisp_id} instance-id {instance_id} ethernet server address-resolution",
                   "show lisp instance-id {instance_id} ethernet server address-resolution"]

    def cli(self, lisp_id=None, instance_id=None, output=None):

        if not output:
            if lisp_id and instance_id:
                out = self.device.execute(self.cli_command[0].format(lisp_id=lisp_id, instance_id=instance_id))
            else:
                out = self.device.execute(self.cli_command[1].format(instance_id=instance_id))
        else:
            out = output

        lisp_ar_dict = {}

        # Address-resolution data for router lisp 0 instance-id 1
        p1 = re.compile(
            r"^Address-resolution\s+data\s+for\s+router\s+lisp\s+"
            r"(?P<lisp_id>\d+)\s+instance-id\s+(?P<instance_id>\d+)$")

        # 0    192.168.1.1/32       aabb.cc00.ca00
        p2 = re.compile(
            r"^(?P<l2_inst_id>\d+)\s+(?P<eid_address>[0-9.]+\d+\/\d+"
            r"|[0-9a-fA-F.:]+\d+\/\d+)\s+(?P<mac_addr>[0-9a-fA-F.]+)$")

        for line in out.splitlines():
            line = line.strip()
            # Address-resolution data for router lisp 0 instance-id 1
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                lisp_id = int(groups['lisp_id'])
                instance_id = int(groups['instance_id'])
                lisp_id_dict = lisp_ar_dict.setdefault('lisp_id', {}) \
                    .setdefault(lisp_id, {})
                instance_id_dict = lisp_id_dict.setdefault('instance_id', {}) \
                    .setdefault(instance_id, {})
                continue

            # 0    192.168.1.1/32       aabb.cc00.ca00
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                eid_address = groups['eid_address']
                mac_address = groups['mac_addr']
                inst_id = groups['l2_inst_id']
                entries_dict = instance_id_dict.setdefault('entries', {}) \
                    .setdefault(eid_address, {})
                entries_dict.update({'mac_address': mac_address})
                entries_dict.update({'inst_id': inst_id})
        return lisp_ar_dict


class ShowLispPublisherSchema(MetaParser):

    ''' Schema for
        * show lisp {lisp_id} instance-id {instance_id} ipv4 publisher
        * show lisp locator-table {vrf} instance-id {instance_id} ipv4 publisher
        * show lisp instance-id {instance_id} ipv4 publisher
        * show lisp eid-table {eid_table} ipv4 publisher
        * show lisp eid-table vrf {vrf} ipv4 publisher
        * show lisp {lisp_id} instance-id {instance_id} ipv6 publisher
        * show lisp locator-table {vrf} instance-id {instance_id} ipv6 publisher
        * show lisp instance-id {instance_id} ipv6 publisher
        * show lisp eid-table {eid_table} ipv6 publisher
        * show lisp eid-table vrf {vrf} ipv6 publisher
        * show lisp {lisp_id} instance-id {instance_id} ethernet publisher
        * show lisp locator-table {vrf} instance-id {instance_id} ethernet publisher
        * show lisp instance-id {instance_id} ethernet publisher
        * show lisp eid-table vlan {vlan} ethernet publisher
    '''

    schema = {
        'lisp_id': {
            int: {
                'instance_id': {
                    Any(): {
                        'publishers': {
                            str: {
                                'state': str,
                                'session': str,
                                'pubsub_state': str
                            }
                        }
                    }
                }
            }
        }
    }


class ShowLispPublisherSuperParser(ShowLispPublisherSchema):
    """ Parser for:
        * show lisp {lisp_id} instance-id {instance_id} ipv4 publisher
        * show lisp locator-table {vrf} instance-id {instance_id} ipv4 publisher
        * show lisp instance-id {instance_id} ipv4 publisher
        * show lisp eid-table {eid_table} ipv4 publisher
        * show lisp eid-table vrf {vrf} ipv4 publisher
        * show lisp {lisp_id} instance-id {instance_id} ipv6 publisher
        * show lisp locator-table {vrf} instance-id {instance_id} ipv6 publisher
        * show lisp instance-id {instance_id} ipv6 publisher
        * show lisp eid-table {eid_table} ipv6 publisher
        * show lisp eid-table vrf {vrf} ipv6 publisher
        * show lisp {lisp_id} instance-id {instance_id} ethernet publisher
        * show lisp locator-table {vrf} instance-id {instance_id} ethernet publisher
        * show lisp instance-id {instance_id} ethernet publisher
        * show lisp eid-table vlan {vlan} ethernet publisher
    """

    def cli(self, output=None, lisp_id=None, instance_id=None):

        # To handle lisp_id
        if not lisp_id or not lisp_id.isdigit():
            lisp_id = 0
        else:
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

        # Initialize dictionary
        ret_dict = {}

        # Output for router lisp 0
        # Output for router lisp 0 instance-id 193
        # Output for router lisp 2 instance-id 101
        p1 = re.compile(r'^Output +for +router +lisp +(?P<lisp_id>(\S+))'
                        '(?: +instance-id +(?P<instance_id>(\d+)))?$')

        # 23.23.23.23                             ETR Map-Server not found       Down            Off
        # 23.23.23.23                             Unreachable       Down                         Off
        # 23.23.23.23                             Reachable       Down                           Off
        p2 = re.compile(r'^(?P<publisher_ip>[\da-fA-F.:]+)\s+(?P<state>ETR Map-Server '
                        r'not found|Unreachable|Reachable)\s+(?P<session>\w+)\s+(?P<pubsub_state>\w+)$')

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

            # 23.23.23.23                             ETR Map-Server not found       Down            Off
            # 23.23.23.23                             Unreachable       Down                         Off
            # 23.23.23.23                             Reachable       Down                           Off
            m = p2.match(line)
            if m:
                group = m.groupdict()
                publisher_ip = group.pop('publisher_ip')
                publisher_ip_dict = \
                    ret_dict.setdefault('lisp_id', {})\
                        .setdefault(lisp_id, {})\
                        .setdefault('instance_id', {})\
                        .setdefault(instance_id, {})\
                        .setdefault('publishers', {})\
                        .setdefault(publisher_ip, {})

                publisher_ip_dict.update(
                    {k:v for k, v in group.items() if v is not None}
                )
                continue

        return ret_dict


class ShowLispIpv4Publisher(ShowLispPublisherSuperParser, ShowLispPublisherSchema):
    """ Parser for:
        * show lisp {lisp_id} instance-id {instance_id} ipv4 publisher
        * show lisp locator-table {vrf} instance-id {instance_id} ipv4 publisher
        * show lisp instance-id {instance_id} ipv4 publisher
        * show lisp eid-table {eid_table} ipv4 publisher
        * show lisp eid-table vrf {vrf} ipv4 publisher
    """

    cli_command = [
        'show lisp {lisp_id} instance-id {instance_id} ipv4 publisher',
        'show lisp locator-table {vrf} instance-id {instance_id} ipv4 publisher',
        'show lisp instance-id {instance_id} ipv4 publisher',
        'show lisp eid-table {eid_table} ipv4 publisher',
        'show lisp eid-table vrf {vrf} ipv4 publisher',
    ]

    def cli(self, output=None, lisp_id=None, instance_id=None, vrf=None, eid_table=None):

        if output is None:
            if lisp_id and instance_id:
                output = self.device.execute(self.cli_command[0].\
                                             format(lisp_id=lisp_id, instance_id=instance_id))
            elif vrf and instance_id:
                output = self.device.execute(self.cli_command[1].\
                                             format(vrf=vrf, instance_id=instance_id))
            elif instance_id:
                output = self.device.execute(self.cli_command[2].format(instance_id=instance_id))
            elif eid_table:
                output = self.device.execute(self.cli_command[3].format(eid_table=eid_table))
            else:
                output = self.device.execute(self.cli_command[4].format(vrf=vrf))

        return super().cli(output=output, lisp_id=lisp_id, instance_id=instance_id)


class ShowLispIpv6Publisher(ShowLispPublisherSuperParser, ShowLispPublisherSchema):
    """ Parser for:
        * show lisp {lisp_id} instance-id {instance_id} ipv6 publisher
        * show lisp locator-table {vrf} instance-id {instance_id} ipv6 publisher
        * show lisp instance-id {instance_id} ipv6 publisher
        * show lisp eid-table {eid_table} ipv6 publisher
        * show lisp eid-table vrf {vrf} ipv6 publisher
    """

    cli_command = [
        'show lisp {lisp_id} instance-id {instance_id} ipv6 publisher',
        'show lisp locator-table {vrf} instance-id {instance_id} ipv6 publisher',
        'show lisp instance-id {instance_id} ipv6 publisher',
        'show lisp eid-table {eid_table} ipv6 publisher',
        'show lisp eid-table vrf {vrf} ipv6 publisher',
    ]

    def cli(self, output=None, lisp_id=None, instance_id=None, vrf=None, eid_table=None):

        # Initialize dictionary
        ret_dict = {}

        if output is None:
            if lisp_id and instance_id:
                output = self.device.execute(self.cli_command[0].\
                                             format(lisp_id=lisp_id, instance_id=instance_id))
            elif vrf and instance_id:
                output = self.device.execute(self.cli_command[1].\
                                             format(vrf=vrf, instance_id=instance_id))
            elif instance_id:
                output = self.device.execute(self.cli_command[2].format(instance_id=instance_id))
            elif eid_table:
                output = self.device.execute(self.cli_command[3].format(eid_table=eid_table))
            else:
                output = self.device.execute(self.cli_command[4].format(vrf=vrf))

        return super().cli(output=output, lisp_id=lisp_id, instance_id=instance_id)


class ShowLispEthernetPublisher(ShowLispPublisherSuperParser, ShowLispPublisherSchema):
    """ Parser for:
        * show lisp {lisp_id} instance-id {instance_id} ethernet publisher
        * show lisp locator-table {vrf} instance-id {instance_id} ethernet publisher
        * show lisp instance-id {instance_id} ethernet publisher
        * show lisp eid-table vlan {vlan} ethernet publisher
    """

    cli_command = [
        'show lisp {lisp_id} instance-id {instance_id} ethernet publisher',
        'show lisp locator-table {vrf} instance-id {instance_id} ethernet publisher',
        'show lisp instance-id {instance_id} ethernet publisher',
        'show lisp eid-table vlan {vlan} ethernet publisher',
    ]

    def cli(self, output=None, lisp_id=None, instance_id=None, vrf=None, vlan=None):

        # Initialize dictionary
        ret_dict = {}

        if output is None:
            if lisp_id and instance_id:
                output = self.device.execute(self.cli_command[0].\
                                             format(lisp_id=lisp_id, instance_id=instance_id))
            elif vrf and instance_id:
                output = self.device.execute(self.cli_command[1].\
                                             format(vrf=vrf, instance_id=instance_id))
            elif instance_id:
                output = self.device.execute(self.cli_command[2].format(instance_id=instance_id))
            else:
                output = self.device.execute(self.cli_command[3].format(vlan=vlan))

        return super().cli(output=output, lisp_id=lisp_id, instance_id=instance_id)


class ShowLispPublicationPrefixSchema(MetaParser):

    schema = {
        'lisp_id': {
            int: {
                'instance_id': {
                    int: {
                        'eid_prefixes': {
                            str: {
                                'first_published': str,
                                'last_published': str,
                                'state': str,
                                'exported_to': list,
                                'publishers': {
                                    str: {
                                        'port': int,
                                        'last_published': str, # (complete|unknown)
                                        'ttl': str,
                                        'publisher_epoch': int,
                                        'entry_epoch': int,
                                        'entry_state': str,
                                        Optional('routing_tag'): int,
                                        'xtr_id': str,
                                        Optional('site_id'): str,
                                        Optional('domain_id'): str,
                                        Optional('multihoming_id'): str,
                                        Optional('extranet_iid'): int,
                                        'locators': {
                                            str: {
                                                'priority': int,
                                                'weight': int,
                                                'state': str, # (up|down)
                                                'encap_iid': str,
                                                Optional('metric'): int,
                                                Optional('domain_id'): int,
                                                Optional('multihoming_id'): int,
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
        }


'''Parser for "show lisp {lisp_id} instance-id {instance_id} ipv4 publication {eid_prefix | detail}"'''
class ShowLispPublicationPrefixSuperParser(ShowLispPublicationPrefixSchema):

    def cli(self, lisp_id=None, instance_id=None, eid_table=None, eid_prefix=None, vrf=None, output=None):
        lisp_v4_pub_pre = {}
        count = 0

        #Output for router lisp 0 instance-id 4100
        p1 = re.compile(r"^Output\s+for\s+router\s+lisp\s+(?P<lisp_id>\d+)\s+"
                        r"instance-id\s+(?P<instance_id>\d+)$")

        #EID-prefix: 192.168.1.71/32
        p2 = re.compile(r"^EID-prefix:\s+(?P<eid_prefixes>(\d{1,3}\.\d{1,3}\.\d{1,3}"
                        r"\.\d{1,3}\/\d{1,2})|([a-fA-F\d\:]+\/\d{1,3}))$")

        #First published:      03:05:56
        p3 = re.compile(r"^First\s+published:\s+(?P<first_published>\S+)$")

        #Last published:      03:05:56
        p4 = re.compile(r"^Last\s+published:\s+(?P<last_published>\S+)$")

        #State:                complete
        p5 = re.compile(r"^State:\s+(?P<state>\S+)$")

        #Exported to:          map-cache
        p6 = re.compile(r"^Exported\s+to:\s+(?P<exported_to>\S+)$")

        #Publisher 100.100.100.100:4342, last published 16:02:47, TTL never
        p7 = re.compile(r"^Publisher\s+(?P<publishers>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
                        r":(?P<port>\d+),\s+last\s+published\s+"
                        r"(?P<last_published>\S+),\s+TTL\s+(?P<ttl>\S+)")

        #publisher epoch 1, entry epoch 1
        p8 = re.compile(r"^publisher\s+epoch\s+(?P<publisher_epoch>\d+),"
                        r"\s+entry\s+epoch\s+(?P<entry_epoch>\d+)")

        #entry-state complete
        p9 = re.compile(r"^entry-state\s+(?P<entry_state>\S+)")

        #routing table tag 101
        p10 = re.compile(r"^routing\s+table\s+tag\s+(?P<routing_tag>\d+)")

        #xTR-ID 0x790800FF-0x426D6D8E-0xC6C5F60C-0xB4386D22
        p11 = re.compile(r"^xTR-ID\s+(?P<xtr_id>\S+)")

        #site-ID unspecified
        p12 = re.compile(r"^site-ID\s+(?P<site_id>\S+)")

        #Domain-ID unset
        p13 = re.compile(r"^Domain-ID\s+(?P<domain_id>\S+)")

        #Multihoming-ID unspecified
        p14 = re.compile(r"^Multihoming-ID\s+(?P<multihoming_id>\S+)")

        #100.88.88.88  100/50   up        -                   1/1       44
        p15 = re.compile(r"^(?P<locators>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+"
                         r"(?P<priority>\d+)\/(?P<weight>\d+)\s+(?P<state>\S+)\s+(?P<encap_iid>\S+)"
                         r"|\s+(?P<domain_id>\d+)\/(?P<multihoming_id>\d+)\s+(?P<metric>\d+)")

        #  Instance ID:                              4100
        p16 = re.compile(r"^\s+Instance\s+ID:\s+(?P<inst_id>\S+)")

        for line in output.splitlines():
            line = line.strip()
            count += 1
            #Output for router lisp 0 instance-id 4100
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                lisp_id = int(groups['lisp_id'])
                prefix_id = int(groups['instance_id'])
                lisp_id_dict = lisp_v4_pub_pre.setdefault('lisp_id',{})\
                                              .setdefault(lisp_id,{})
                instance_id_dict = lisp_id_dict.setdefault('instance_id',{})\
                                               .setdefault(prefix_id,{})
                continue

            if not m and count < 2 and lisp_id != "all":
                if lisp_id and instance_id:
                    lisp_id = int(lisp_id)
                    lisp_id_dict = lisp_v4_pub_pre.setdefault('lisp_id',{})\
                                                  .setdefault(lisp_id,{})
                    instance_id = int(instance_id)
                    instance_id_dict = lisp_id_dict.setdefault('instance_id',{})\
                                                   .setdefault(instance_id,{})
                    count += 1
                if not lisp_id and instance_id:
                    lisp_id = 0
                    lisp_id_dict = lisp_v4_pub_pre.setdefault('lisp_id',{})\
                                                  .setdefault(lisp_id,{})
                    instance_id = int(instance_id)
                    instance_id_dict = lisp_id_dict.setdefault('instance_id',{})\
                                                   .setdefault(instance_id,{})
                    count += 1
                if not instance_id:
                    cmd =  "show lisp eid-table vrf red ipv4 | i Instance"
                    out =  self.device.execute(cmd) #This is temporary.This execute() will be removed in the future
                    for line in out.splitlines():
                        m = p16.match(line)
                        if m:
                            groups = m.groupdict()
                            inst_id = int(groups['inst_id'])
                            lisp_id = 0
                            lisp_id_dict = lisp_v4_pub_pre.setdefault('lisp_id',{})\
                                                          .setdefault(lisp_id,{})
                            instance_id = inst_id
                            instance_id_dict = lisp_id_dict.setdefault('instance_id',{})\
                                                           .setdefault(instance_id,{})
                            count += 1

            #EID-prefix: 192.168.1.71/3
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                eid_prefixes = groups['eid_prefixes']
                eid_prefix_dict = instance_id_dict.setdefault('eid_prefixes',{})\
                                                  .setdefault(eid_prefixes,{})
                continue

            #First published:      03:05:56
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                first_published = groups['first_published']
                eid_prefix_dict.update({'first_published':first_published})
                continue

            #Last published:      03:05:56
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                last_published = groups['last_published']
                eid_prefix_dict.update({'last_published':last_published})
                continue

            #State:                complete
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                state = groups['state']
                eid_prefix_dict.update({'state':state})
                continue

            #Exported to:          map-cache
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                exported_to = groups['exported_to']
                exported_list = eid_prefix_dict.setdefault('exported_to',[])
                exported_list.append(exported_to)
                eid_prefix_dict.update({'exported_to':exported_list})
                continue

            #Publisher 100.100.100.100:4342, last published 16:02:47, TTL never
            m = p7.match(line)
            if m:
                groups = m.groupdict()
                publishers = groups['publishers']
                port = int(groups['port'])
                last_published = groups['last_published']
                ttl = groups['ttl']
                publishers = "{}:{}".format(publishers,port)
                publish_dict = eid_prefix_dict.setdefault('publishers',{})\
                                              .setdefault(publishers,{})
                publish_dict.update({'port':port})
                publish_dict.update({'last_published':last_published})
                publish_dict.update({'ttl':ttl})
                continue

            #publisher epoch 0,entry epoch 0
            m = p8.match(line)
            if m:
                groups = m.groupdict()
                publisher_epoch = int(groups['publisher_epoch'])
                entry_epoch = int(groups['entry_epoch'])
                publish_dict.update({'publisher_epoch':publisher_epoch})
                publish_dict.update({'entry_epoch':entry_epoch})
                continue

            #entry-state complete
            m = p9.match(line)
            if m:
                groups = m.groupdict()
                entry_state = groups['entry_state']
                publish_dict.update({'entry_state':entry_state})
                continue

            #routing table tag 101
            m = p10.match(line)
            if m:
                groups = m.groupdict()
                routing_tag = int(groups['routing_tag'])
                publish_dict.update({'routing_tag':routing_tag})
                continue

            #xTR-ID 0x790800FF-0x426D6D8E-0xC6C5F60C-0xB4386D22
            m = p11.match(line)
            if m:
                groups = m.groupdict()
                xtr_id = groups['xtr_id']
                publish_dict.update({'xtr_id':xtr_id})
                continue

            #site-ID unspecified
            m = p12.match(line)
            if m:
                groups = m.groupdict()
                site_id = groups['site_id']
                publish_dict.update({'site_id':site_id})
                continue

            #Domain-ID unset
            m = p13.match(line)
            if m:
                groups = m.groupdict()
                domain_id = (groups['domain_id'])
                publish_dict.update({'domain_id':domain_id})
                continue

            #Multihoming-ID unspecified
            m = p14.match(line)
            if m:
                groups = m.groupdict()
                multihoming_id = (groups['multihoming_id'])
                publish_dict.update({'multihoming_id':multihoming_id})
                continue

            #22.22.22.22   10/10   up        -
            m = p15.match(line)
            if m:
                groups = m.groupdict()
                locators = (groups['locators'])
                priority = int(groups['priority'])
                weight = int(groups['weight'])
                state = groups['state']
                encap_iid = groups['encap_iid']
                locator_dict =  publish_dict.setdefault('locators',{})\
                                            .setdefault(locators,{})
                locator_dict.update({'priority':priority})
                locator_dict.update({'weight':weight})
                locator_dict.update({'state':state})
                locator_dict.update({'encap_iid':encap_iid})
                if groups['metric'] != None:
                    metric = int(groups['metric'])
                    locator_dict.update({'metric':metric})
                if groups['domain_id'] != None:
                    domain_id = int(groups['domain_id'])
                    locator_dict.update({'domain_id':domain_id})
                if groups['multihoming_id'] != None:
                    multihoming_id = int(groups['multihoming_id'])
                    locator_dict.update({'multihoming_id':multihoming_id})
                continue
        return lisp_v4_pub_pre


class ShowLispV4PublicationPrefix(ShowLispPublicationPrefixSuperParser):

    """
    Parser for
    *show lisp instance-id {instance_id} ipv4 publication {eid_prefix}
    *show lisp {lisp_id} instance-id {instance_id} ipv4 publication {eid_prefix}
    *show lisp eid-table {eid_table} ipv4 publication {eid_prefix}
    *show lisp {lisp_id} eid-table vrf {vrf} ipv4 publication {eid_prefix}
    *show lisp locator-table {vrf} instance-id {instance_id} ipv4 publication {eid_prefix}
    *show lisp locator-table vrf {vrf} instance-id {instance_id} ipv4 publication {eid_prefix}
    *show lisp instance-id {instance_id} ipv4 publication detail
    *show lisp {lisp_id} instance-id {instance_id} ipv4 publication detail
    *show lisp eid-table {eid_table} ipv4 publication detail
    *show lisp {lisp_id} eid-table vrf {vrf} ipv4 publication detail
    *show lisp locator-table {vrf} instance-id {instance_id} ipv4 publication detail
    *show lisp locator-table vrf {vrf} instance-id {instance_id} ipv4 publication detail
    """
    cli_command = ['show lisp instance-id {instance_id} ipv4 publication {eid_prefix}',
                   'show lisp {lisp_id} instance-id {instance_id} ipv4 publication {eid_prefix}',
                   'show lisp eid-table {eid_table} ipv4 publication {eid_prefix}',
                   'show lisp {lisp_id} eid-table vrf {vrf} ipv4 publication {eid_prefix}',
                   'show lisp locator-table {vrf} instance-id {instance_id} ipv4 publication {eid_prefix}',
                   'show lisp locator-table vrf {vrf} instance-id {instance_id} ipv4 publication {eid_prefix}',
                   'show lisp instance-id {instance_id} ipv4 publication detail',
                   'show lisp {lisp_id} instance-id {instance_id} ipv4 publication detail',
                   'show lisp eid-table {eid_table} ipv4 publication detail',
                   'show lisp {lisp_id} eid-table vrf {vrf} ipv4 publication detail',
                   'show lisp locator-table {vrf} instance-id {instance_id} ipv4 publication detail',
                   'show lisp locator-table vrf {vrf} instance-id {instance_id} ipv4 publication detail']

    def cli(self, lisp_id=None, instance_id=None, eid_table=None, eid_prefix=None, vrf=None, output=None):
        if output is None:
            if lisp_id and instance_id and eid_prefix:
                output = self.device.execute(self.cli_command[1].format(lisp_id=lisp_id, instance_id=instance_id, eid_prefix=eid_prefix))
            elif lisp_id and vrf and eid_prefix:
                output = self.device.execute(self.cli_command[3].format(lisp_id=lisp_id, vrf=vrf, eid_prefix=eid_prefix))
            elif vrf and instance_id and eid_prefix:
                if "vrf" in self.cli_command:
                    output = self.device.execute(self.cli_command[5].format(vrf=vrf, instance_id=instance_id, eid_prefix=eid_prefix))
                else:
                    output = self.device.execute(self.cli_command[4].format(vrf=vrf, instance_id=instance_id, eid_prefix=eid_prefix))
            elif instance_id and eid_prefix:
                output = self.device.execute(self.cli_command[0].format(instance_id=instance_id, eid_prefix=eid_prefix))
            elif eid_table and eid_prefix:
                output = self.device.execute(self.cli_command[2].format(eid_table=eid_table, eid_prefix=eid_prefix))
            elif lisp_id and instance_id:
                output = self.device.execute(self.cli_command[7].format(lisp_id=lisp_id, instance_id=instance_id))
            elif lisp_id and vrf:
                output = self.device.execute(self.cli_command[9].format(lisp_id=lisp_id, vrf=vrf))
            elif vrf and instance_id:
                if vrf == "default":
                    output = self.device.execute(self.cli_command[10].format(vrf=vrf, instance_id=instance_id))
                else:
                    output = self.device.execute(self.cli_command[11].format(vrf=vrf, instance_id=instance_id))
            elif instance_id:
                output = self.device.execute(self.cli_command[6].format(instance_id=instance_id))
            elif eid_table:
                output = self.device.execute(self.cli_command[8].format(eid_table=eid_table))
        return super().cli(lisp_id=lisp_id, instance_id=instance_id, eid_table=eid_table, eid_prefix=eid_prefix, vrf=vrf, output=output)


class ShowLispV6PublicationPrefix(ShowLispPublicationPrefixSuperParser):

    """
    Parser for
    *show lisp instance-id {instance_id} ipv6 publication {eid_prefix}
    *show lisp {lisp_id} instance-id {instance_id} ipv6 publication {eid_prefix}
    *show lisp eid-table {eid_table} ipv6 publication {eid_prefix}
    *show lisp {lisp_id} eid-table vrf {vrf} ipv6 publication {eid_prefix}
    *show lisp locator-table {vrf} instance-id {instance_id} ipv6 publication {eid_prefix}
    *show lisp locator-table vrf {vrf} instance-id {instance_id} ipv6 publication {eid_prefix}
    *show lisp instance-id {instance_id} ipv6 publication detail
    *show lisp {lisp_id} instance-id {instance_id} ipv6 publication detail
    *show lisp eid-table {eid_table} ipv6 publication detail
    *show lisp {lisp_id} eid-table vrf {vrf} ipv6 publication detail
    *show lisp locator-table {vrf} instance-id {instance_id} ipv6 publication detail
    *show lisp locator-table vrf {vrf} instance-id {instance_id} ipv6 publication detail
    """
    cli_command = ['show lisp instance-id {instance_id} ipv6 publication {eid_prefix}',
                   'show lisp {lisp_id} instance-id {instance_id} ipv6 publication {eid_prefix}',
                   'show lis locator-table {vrf} instance-id {instance_id} ipv6 publication {eid_prefix}',
                   'show lispp eid-table {eid_table} ipv6 publication {eid_prefix}',
                   'show lisp {lisp_id} eid-table vrf {vrf} ipv6 publication {eid_prefix}',
                   'show lisp locator-table vrf {vrf} instance-id {instance_id} ipv6 publication {eid_prefix}',
                   'show lisp instance-id {instance_id} ipv6 publication detail',
                   'show lisp {lisp_id} instance-id {instance_id} ipv6 publication detail',
                   'show lisp eid-table {eid_table} ipv6 publication detail',
                   'show lisp {lisp_id} eid-table vrf {vrf} ipv6 publication detail',
                   'show lisp locator-table {vrf} instance-id {instance_id} ipv6 publication detail',
                   'show lisp locator-table vrf {vrf} instance-id {instance_id} ipv6 publication detail']

    def cli(self, lisp_id=None, instance_id=None, eid_table=None, eid_prefix=None, vrf=None, output=None):
        if output is None:
            if lisp_id and instance_id and eid_prefix:
                output = self.device.execute(self.cli_command[1].format(lisp_id=lisp_id, instance_id=instance_id, eid_prefix=eid_prefix))
            elif lisp_id and vrf and eid_prefix:
                output = self.device.execute(self.cli_command[3].format(lisp_id=lisp_id, vrf=vrf, eid_prefix=eid_prefix))
            elif vrf and instance_id and eid_prefix:
                if "vrf" in self.cli_command:
                    output = self.device.execute(self.cli_command[5].format(vrf=vrf, instance_id=instance_id, eid_prefix=eid_prefix))
                else:
                    output = self.device.execute(self.cli_command[4].format(vrf=vrf, instance_id=instance_id, eid_prefix=eid_prefix))
            elif instance_id and eid_prefix:
                output = self.device.execute(self.cli_command[0].format(instance_id=instance_id, eid_prefix=eid_prefix))
            elif eid_table and eid_prefix:
                output = self.device.execute(self.cli_command[2].format(eid_table=eid_table, eid_prefix=eid_prefix))
            elif lisp_id and instance_id:
                output = self.device.execute(self.cli_command[7].format(lisp_id=lisp_id, instance_id=instance_id))
            elif lisp_id and vrf:
                output = self.device.execute(self.cli_command[9].format(lisp_id=lisp_id, vrf=vrf))
            elif vrf and instance_id:
                if vrf == "default":
                    output = self.device.execute(self.cli_command[10].format(vrf=vrf, instance_id=instance_id))
                else:
                    output = self.device.execute(self.cli_command[11].format(vrf=vrf, instance_id=instance_id))
            elif instance_id:
                output = self.device.execute(self.cli_command[6].format(instance_id=instance_id))
            elif eid_table:
                output = self.device.execute(self.cli_command[8].format(eid_table=eid_table))
        return super().cli(lisp_id=lisp_id, instance_id=instance_id, eid_table=eid_table, eid_prefix=eid_prefix, vrf=vrf, output=output)


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
                            str: ListOf(
                                    {
                                    'port': int,
                                    'type': str
                                }
                            )
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
                        '(?: +instance-id +(?P<instance_id>(\d+)))?$')

        # Entries total 1
        p2 = re.compile(r'^Entries\s+total\s+(?P<entries>\d+)$')

        # 66.66.66.66:54087         IID
        # 77.77.77.77:54123         IID
        p3 = re.compile(r'^(?P<subscriber_ip>[\da-fA-F.:]+):(?P<port>\d+)\s+(?P<type>.+)$')


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
                subscribers_dict = lisp_id_dict.setdefault('subscribers', {}).setdefault(group['subscriber_ip'], [])
                subscribers_dict.append({'port': int(group['port']),
                                         'type': group['type']})
                continue
        return ret_dict


class ShowLispIpv4Subscriber(ShowLispSubscriberSuperParser, ShowLispSubscriberSchema):
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
        'show lisp eid-table vrf {vrf} ipv4 subscriber',
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


class ShowLispIpv6Subscriber(ShowLispSubscriberSuperParser, ShowLispSubscriberSchema):
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


class ShowLispEthernetSubscriber(ShowLispSubscriberSuperParser, ShowLispSubscriberSchema):
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


# ==========================================
# Parser for:
#  * 'show lisp instance-id {instance_id} ethernet publication'
#  * 'show lisp {lisp_id} instance-id {instance_id} ethernet publication'
#  * 'show lisp locator-table {vrf} instance-id {instance-id} ethernet publication'
# ==========================================
class ShowLispEthernetPublication(ShowLispIpv4PublicationSchema):
    """Parser for show lisp ethernet publication"""
    cli_command = ['show lisp instance-id {instance_id} ethernet publication',
                   'show lisp {lisp_id} instance-id {instance_id} ethernet publication',
                   'show lisp locator-table {vrf} instance-id {instance_id} ethernet publication']

    def cli(self, lisp_id=None, instance_id=None, vrf=None, output=None):
        if output is None:
            if lisp_id and instance_id:
                cmd = self.cli_command[1].format(lisp_id=lisp_id, instance_id=instance_id)
            elif vrf and instance_id:
                cmd = self.cli_command[2].format(vrf=vrf, instance_id=instance_id)
            else:
                cmd = self.cli_command[0].format(instance_id=instance_id)
            output = self.device.execute(cmd)
        ret_dict = {}
        #Output for router lisp 0 instance-id 101
        p1 = re.compile(r"^Output\s+for\s+router\s+lisp\s+(?P<lisp_id>\d+)\s+"
                        r"instance-id\s+(?P<instance_id>\d+)$")

        #Entries total 2
        p2 = re.compile(r"^Entries\s+total\s+(?P<total_entries>\d+)$")

        #100.100.100.100 15:52:51    aabb.cc00.c901/48        11.11.11.11     -
        p3 = re.compile(r"^(?P<publisher_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+"
                        r"(?P<last_published>\S+)\s+(?P<eid_prefix>([a-fA-F\d]{4}\.){2}"
                        r"[a-fA-F\d]{4}\/\d{1,3})\s+(?P<rloc>\d{1,3}\.\d{1,3}\.\d{1,3}\."
                        r"\d{1,3})\s+(?P<encap_iid>\S+)$")

        #  Instance ID:                              4100
        p4 = re.compile(r"^\s+Instance\s+ID:\s+(?P<inst_id>\d+)")
        count = 0

        for line in output.splitlines():
            line = line.strip()
            count += 1
            #Output for router lisp 0
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                lisp_id = int(groups['lisp_id'])
                instance_id = int(groups['instance_id'])
                lisp_id_dict = ret_dict.setdefault('lisp_id',{})\
                    .setdefault(lisp_id,{})
                instance_id_dict = lisp_id_dict.setdefault('instance_id',{})\
                    .setdefault(instance_id,{})
            if not m and count < 2 and lisp_id != "all":
                if lisp_id and instance_id:
                    lisp_id = int(lisp_id)
                    lisp_id_dict = ret_dict.setdefault('lisp_id',{})\
                        .setdefault(lisp_id,{})
                    instance_id = int(instance_id)
                    instance_id_dict = lisp_id_dict.setdefault('instance_id',{})\
                        .setdefault(instance_id,{})
                    count += 1
                    continue
                if not lisp_id and instance_id:
                    lisp_id = 0
                    lisp_id_dict = ret_dict.setdefault('lisp_id',{})\
                        .setdefault(lisp_id,{})
                    instance_id = int(instance_id)
                    instance_id_dict = lisp_id_dict.setdefault('instance_id',{})\
                        .setdefault(instance_id,{})
                    count += 1
                    continue

            #Entries total 2
            m=p2.match(line)
            if m:
                groups = m.groupdict()
                entries = int(groups['total_entries'])
                instance_id_dict.update({'total_entries':entries})
                continue

            #44.44.44.44     1d21h       192.168.1.71/32          11.11.11.11     -
            m=p3.match(line)
            if m:
                groups = m.groupdict()
                publications = groups['eid_prefix']
                publisher_ip = groups['publisher_ip']
                last_published = groups['last_published']
                rloc = groups['rloc']
                encap_iid = groups['encap_iid']
                eid_prefix = instance_id_dict.setdefault('eid_prefix',{})\
                    .setdefault(publications,{})
                eid_prefix.update({'publisher_ip':publisher_ip})
                eid_prefix.update({'last_published':last_published})
                eid_prefix.update({'rloc':rloc})
                eid_prefix.update({'encap_iid':encap_iid})
        return ret_dict


class ShowLispEthernetPublicationPrefix(ShowLispPublicationPrefixSchema):
    """
    Parser for
    *show lisp instance-id {instance_id} ethernet publication {eid_prefix}
    *show lisp {lisp_id} instance-id {instance_id} ethernet publication {eid_prefix}
    *show lisp eid-table vlan {vlan} ethernet publication {eid_prefix}
    *show lisp locator-table {vrf} instance-id {instance_id} ethernet publication {eid_prefix}
    *show lisp locator-table vrf {vrf} instance-id {instance_id} ethernet publication {eid_prefix}
    """
    cli_command = ['show lisp instance-id {instance_id} ethernet publication {eid_prefix}',
                   'show lisp {lisp_id} instance-id {instance_id} ethernet publication {eid_prefix}',
                   #'show lisp eid-table vlan {vlan} ethernet publication {eid_prefix}',
                   'show lisp locator-table {vrf} instance-id {instance_id} ethernet publication {eid_prefix}',
                   'show lisp locator-table vrf {vrf} instance-id {instance_id} ethernet publication {eid_prefix}']

    def cli(self, lisp_id=None, instance_id=None, eid_table=None, vlan=None, eid_prefix=None, vrf=None, output=None):
        ret_dict = {}
        if output is None:
            if lisp_id and instance_id and eid_prefix:
                output = self.device.execute(self.cli_command[1].format(lisp_id=lisp_id, instance_id=instance_id, eid_prefix=eid_prefix))
            elif vrf and instance_id and eid_prefix:
                if "vrf" in self.cli_command:
                    output = self.device.execute(self.cli_command[4].format(vrf=vrf, instance_id=instance_id, eid_prefix=eid_prefix))
                else:
                    output = self.device.execute(self.cli_command[3].format(vrf=vrf, instance_id=instance_id, eid_prefix=eid_prefix))
            else:
                output = self.device.execute(self.cli_command[0].format(instance_id=instance_id, eid_prefix=eid_prefix))
            #else:
            #    output = self.device.execute(self.cli_command[2].format(vlan=vlan,eid_prefix=eid_prefix))
        else:
            output = output
        #Output for router lisp 0 instance-id 4100
        p1 = re.compile(r"^Output\s+for\s+router\s+lisp\s+(?P<lisp_id>\d+)"
                        r"\s+instance-id\s+(?P<instance_id>\d+)$")

        #EID-prefix: aabb.cc00.c901/48
        p2 = re.compile(r"^EID-prefix:\s+(?P<eid_prefixes>([a-fA-F\d]{4}\.){2}[a-fA-F\d]{4}\/\d{1,3})$")

        #First published:      03:05:56
        p3 = re.compile(r"^First\s+published:\s+(?P<first_published>\S+)$")

        #Last published:      03:05:56
        p4 = re.compile(r"^Last\s+published:\s+(?P<last_published>\S+)$")

        #State:                complete
        p5 = re.compile(r"^State:\s+(?P<state>\S+)$")

        #Exported to:          map-cache
        p6 = re.compile(r"^Exported\s+to:\s+(?P<exported_to>\S+)$")

        #Publisher 100.100.100.100:4342, last published 16:02:47, TTL never
        p7 = re.compile(r"^Publisher\s+(?P<publishers>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):"
                        r"(?P<port>\d+),\s+last\s+published\s+(?P<last_published>\S+),\s+"
                        r"TTL\s+(?P<ttl>\S+)")

        #publisher epoch 1, entry epoch 1
        p8 = re.compile(r"^publisher\s+epoch\s+(?P<publisher_epoch>\d+),"
                        r"\s+entry\s+epoch\s+(?P<entry_epoch>\d+)")

        #entry-state complete
        p9 = re.compile(r"^entry-state\s+(?P<entry_state>\S+)")

        #routing table tag 101
        p10 = re.compile(r"^routing\s+table\s+tag\s+(?P<routing_tag>\d+)")

        #xTR-ID 0x790800FF-0x426D6D8E-0xC6C5F60C-0xB4386D22
        p11 = re.compile(r"^xTR-ID\s+(?P<xtr_id>\S+)")

        #site-ID unspecified
        p12 = re.compile(r"^site-ID\s+(?P<site_id>\S+)")

        #Domain-ID unset
        p13 = re.compile(r"^Domain-ID\s+(?P<domain_id>\S+)")

        #Multihoming-ID unspecified
        p14 = re.compile(r"^Multihoming-ID\s+(?P<multihoming_id>\S+)")

        #11.11.11.11   10/10   up        -                   1/1       44
        p15 = re.compile(r"^(?P<locators>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+"
                         r"(?P<priority>\d+)\/(?P<weight>\d+)\s+(?P<state>\S+)\s+(?P<encap_iid>\S+)"
                         r"|\s+(?P<domain_id>\d+)\/(?P<multihoming_id>\d+)\s+(?P<metric>\d+)")

        #  Instance ID:                              4100
        p16 = re.compile(r"^\s+Instance\s+ID:\s+(?P<inst_id>\d+)")
        count = 0

        for line in output.splitlines():
            line = line.strip()
            count += 1
            #Output for router lisp 0 instance-id 4100
            m=p1.match(line)
            if m:
                groups = m.groupdict()
                lisp_id = int(groups['lisp_id'])
                prefix_id = int(groups['instance_id'])
                lisp_id_dict = ret_dict.setdefault('lisp_id',{})\
                                                 .setdefault(lisp_id,{})
                instance_id_dict = ret_dict.setdefault('instance_id',{})\
                                                     .setdefault(prefix_id,{})
                continue
            if not m and count < 2 and lisp_id != "all":
                if lisp_id and instance_id:
                    lisp_id = int(lisp_id)
                    lisp_id_dict = ret_dict.setdefault('lisp_id',{})\
                        .setdefault(lisp_id,{})
                    instance_id = int(instance_id)
                    instance_id_dict = lisp_id_dict.setdefault('instance_id',{})\
                        .setdefault(instance_id,{})
                    count += 1
                    continue
                if not lisp_id and instance_id:
                    lisp_id = 0
                    lisp_id_dict = ret_dict.setdefault('lisp_id',{})\
                        .setdefault(lisp_id,{})
                    instance_id = int(instance_id)
                    instance_id_dict = lisp_id_dict.setdefault('instance_id',{})\
                        .setdefault(instance_id,{})
                    count += 1
                    continue

            #EID-prefix: 192.168.1.71/3
            m=p2.match(line)
            if m:
                groups = m.groupdict()
                eid_prefixes = groups['eid_prefixes']
                eid_prefix = instance_id_dict.setdefault('eid_prefixes',{})\
                    .setdefault(eid_prefixes,{})
                continue

            #First published:      03:05:56
            m=p3.match(line)
            if m:
                groups = m.groupdict()
                first_published = groups['first_published']
                eid_prefix.update({'first_published':first_published})

            #Last published:      03:05:56
            m=p4.match(line)
            if m:
                groups = m.groupdict()
                last_published = groups['last_published']
                eid_prefix.update({'last_published':last_published})

            #State:                complete
            m=p5.match(line)
            if m:
                groups = m.groupdict()
                state = groups['state']
                eid_prefix.update({'state':state})

            #Exported to:          map-cache
            m=p6.match(line)
            if m:
                groups = m.groupdict()
                exported_to = groups['exported_to']
                exported_list = eid_prefix.setdefault('exported_to',[])
                exported_list.append(exported_to)
                eid_prefix.update({'exported_to':exported_list})

            #Publisher 100.100.100.100:4342, last published 16:02:47, TTL never
            m=p7.match(line)
            if m:
                groups = m.groupdict()
                publishers = groups['publishers']
                port = int(groups['port'])
                last_published = groups['last_published']
                ttl = groups['ttl']
                publishers = "{}:{}".format(publishers,port)
                publish_dict = eid_prefix.setdefault('publishers',{})\
                    .setdefault(publishers,{})
                publish_dict.update({'port':port})
                publish_dict.update({'last_published':last_published})
                publish_dict.update({'ttl':ttl})

            #publisher epoch 0,entry epoch 0
            m=p8.match(line)
            if m:
                groups = m.groupdict()
                publisher_epoch = int(groups['publisher_epoch'])
                entry_epoch = int(groups['entry_epoch'])
                publish_dict.update({'publisher_epoch':publisher_epoch})
                publish_dict.update({'entry_epoch':entry_epoch})

            #entry-state complete
            m=p9.match(line)
            if m:
                groups = m.groupdict()
                entry_state = groups['entry_state']
                publish_dict.update({'entry_state':entry_state})

            #routing table tag 101
            m=p10.match(line)
            if m:
                groups = m.groupdict()
                routing_tag = int(groups['routing_tag'])
                publish_dict.update({'routing_tag':routing_tag})

            #xTR-ID 0x790800FF-0x426D6D8E-0xC6C5F60C-0xB4386D22
            m=p11.match(line)
            if m:
                groups = m.groupdict()
                xtr_id = groups['xtr_id']
                publish_dict.update({'xtr_id':xtr_id})

            #site-ID unspecified
            m=p12.match(line)
            if m:
                groups = m.groupdict()
                site_id = groups['site_id']
                publish_dict.update({'site_id':site_id})

            #Domain-ID unset
            m=p13.match(line)
            if m:
                groups = m.groupdict()
                domain_id = (groups['domain_id'])
                publish_dict.update({'domain_id':domain_id})

            #Multihoming-ID unspecified
            m=p14.match(line)
            if m:
                groups = m.groupdict()
                multihoming_id = (groups['multihoming_id'])
                publish_dict.update({'multihoming_id':multihoming_id})

            #22.22.22.22   10/10   up        -                   1/1       44
            m=p15.match(line)
            if m:
                groups = m.groupdict()
                locators = (groups['locators'])
                priority = int(groups['priority'])
                weight = int(groups['weight'])
                state = groups['state']
                encap_iid = groups['encap_iid']
                locator_dict =  publish_dict.setdefault('locators',{})\
                                            .setdefault(locators,{})
                locator_dict.update({'priority':priority})
                locator_dict.update({'weight':weight})
                locator_dict.update({'state':state})
                locator_dict.update({'encap_iid':encap_iid})
                if groups['metric'] != None:
                    metric = int(groups['metric'])
                    locator_dict.update({'metric':metric})
                if groups['domain_id'] != None:
                    domain_id = int(groups['domain_id'])
                    locator_dict.update({'domain_id':domain_id})
                if groups['multihoming_id'] != None:
                    multihoming_id = int(groups['multihoming_id'])
                    locator_dict.update({'multihoming_id':multihoming_id})
                continue
        return ret_dict


class ShowLispARDetailSchema(MetaParser):

    schema = {
        'lisp_id': {
        int: {
            'instance_id': {
                int: {
                    'site': str,
                    'host_address': {
                        str: { # ipv4 or ipv6
                            'hardware_address': str, # MAC address
                            'first_registered': str,
                            'last_registered': str,
                            'registration_errors': {
                                'authentication_failures': int
                            },
                            'etr': {
                                str: {
                                    'port': int,
                                    'last_registered': str,
                                    'ttl': str,
                                    'xtr_id': str,
                                    'site_id': str,
                                    'registered_addr': str,
                                    'l3_instance_id': int
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}


'''Parser for show lisp {lisp_id} instance-id {instance_id} ethernet server address-resolution {prefix | detail}'''
class ShowLispARDetailParser(ShowLispARDetailSchema):
    """ Parser for:
        * show lisp instance-id {instance_id} ethernet server address-resolution {eid}
        * show lisp {lisp_id} instance-id {instance_id} ethernet server address-resolution {eid}
        * show lisp eid-table vlan {vlan} ethernet server address-resolution {eid}
        * show lisp locator-table {locator_table} instance-id {instance_id} ethernet server address-resolution {eid}
        * show lisp locator-table vrf {vrf} instance-id {instance_id} ethernet server address-resolution {eid}
        * show lisp instance-id {instance_id} ethernet server address-resolution detail
        * show lisp {lisp_id} instance-id {instance_id} ethernet server address-resolution detail
        * show lisp eid-table vlan {vlan} ethernet server address-resolution detail
        * show lisp locator-table {locator_table} instance-id {instance_id} ethernet server address-resolution detail
        * show lisp locator-table vrf {vrf} instance-id {instance_id} ethernet server address-resolution detail"""

    cli_command = ['show lisp instance-id {instance_id} ethernet server address-resolution {eid}',
                   'show lisp {lisp_id} instance-id {instance_id} ethernet server address-resolution {eid}',
                   'show lisp eid-table vlan {vlan} ethernet server address-resolution {eid}',
                   'show lisp locator-table {locator_table} instance-id {instance_id} ethernet server address-resolution {eid}',
                   'show lisp locator-table vrf {vrf} instance-id {instance_id} ethernet server address-resolution {eid}',
                   'show lisp {lisp_id} instance-id {instance_id} ethernet server address-resolution detail',
                   'show lisp eid-table vlan {vlan} ethernet server address-resolution detail',
                   'show lisp locator-table {locator_table} instance-id {instance_id} ethernet server address-resolution detail',
                   'show lisp locator-table vrf {vrf} instance-id {instance_id} ethernet server address-resolution detail']

    def cli(self, lisp_id=None, instance_id=None, vlan=None, vrf=None, eid=None, locator_table=None, output=None):

        ret_dict = {}
        if output is None:
            if locator_table and instance_id and eid:
                cmd = self.cli_command[3].format(locator_table=locator_table, instance_id=instance_id, eid=eid)
            elif vrf and instance_id and eid:
                cmd = self.cli_command[4].format(vrf=vrf, instance_id=instance_id, eid=eid)
            elif lisp_id and instance_id and eid:
                cmd = self.cli_command[1].format(lisp_id=lisp_id, instance_id=instance_id, eid=eid)
            elif instance_id and eid:
                cmd = self.cli_command[0].format(instance_id=instance_id, eid=eid)
            elif vlan and eid:
                cmd = self.cli_command[2].format(vlan=vlan, eid=eid)
            elif lisp_id and instance_id:
                cmd = self.cli_command[5].format(instance_id=instance_id, lisp_id=lisp_id)
            elif locator_table and instance_id:
                cmd = self.cli_command[7].format(instance_id=instance_id, locator_table=locator_table)
            elif vrf and instance_id:
                cmd = self.cli_command[8].format(instance_id=instance_id, vrf=vrf)
            else:
                cmd = self.cli_command[6].format(vlan=vlan)
            output = self.device.execute(cmd)

        #Address-resolution data for router lisp 0 instance-id 101
        p1 = re.compile(r"^Address-resolution\s+data\s+for\s+router\s+"
                        r"lisp\s+(?P<lisp_id>\d+)\s+instance-id\s+(?P<instance_id>\d+)$")

        #Site name: Shire
        p2 = re.compile(r"^Site\s+name:\s+(?P<site>\S+)$")

        #Host Address:         192.168.1.71/32
        p3 = re.compile(r"^Host\s+Address:\s+(?P<host_address>\d{1,3}\."
                        r"\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2}|[a-fA-F\d\:]+\/\d{1,3})$")

        #Hardware Address:     aabb.cc00.c901
        p4 = re.compile(r"^Hardware\s+Address:\s+(?P<hardware_address>"
                        r"([a-fA-F\d]{4}\.){2}[a-fA-F\d]{4})$")

        #First registered:     1w0d
        p5 = re.compile(r"^First\s+registered:\s+(?P<first_registered>\S+)$")

        #Last registered:      1w0d
        p6 = re.compile(r"^Last\s+registered:\s+(?P<last_registered>\S+)$")

        #Authentication failures:   0
        p7 = re.compile(r"^\s+Authentication\s+failures:\s+(?P<authentication_failures>\d+)$")

        #ETR 11.11.11.11:28966
        p8 = re.compile(r"^\s+ETR\s+(?P<etr>\d{1,3}\.\d{1,3}\."
                        r"\d{1,3}\.\d{1,3}:(?P<port>\d+))$")

        #Last registered:      1w0d
        p9 = re.compile(r"^\s+Last\s+registered:\s+(?P<etr_last_registered>\S+)$")

        #TTL:                   1d00h
        p10 = re.compile(r"^\s+TTL:\s+(?P<ttl>\S+)$")

        #xTR-ID:                0xC25C9262-0xC9865A33-0x008E8A37-0x9206AC33
        p11 = re.compile(r"^\s+xTR-ID:\s+(?P<xtr_id>\S+)$")

        #Site-ID:               unspecified
        p12 = re.compile(r"^\s+Site-ID:\s+(?P<site_id>\S+)$")

        #Registered addr:       aabb.cc00.c901
        p13 = re.compile(r"^\s+Registered\s+addr:\s+(?P<registered_addr>"
                         r"([a-fA-F\d]{4}\.){2}[a-fA-F\d]{4})$")

        #L3 Instance ID:        4100
        p14 = re.compile(r"^\s+L3\s+Instance\s+ID:\s+(?P<l3_instance_id>\d+)$")

        for line in output.splitlines():
            #Address-resolution data for router lisp 0 instance-id 101
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                lisp_id = int(groups['lisp_id'])
                prefix_id = int(groups['instance_id'])
                lisp_id_dict = ret_dict.setdefault('lisp_id',{})\
                                       .setdefault(lisp_id,{})
                instance_id_dict = lisp_id_dict.setdefault('instance_id',{})\
                                               .setdefault(prefix_id,{})
                continue

            #Site name: Shire
            m=p2.match(line)
            if m:
                groups = m.groupdict()
                site = groups['site']
                instance_id_dict.update({'site':site})
                continue

            #Site name: Shire
            m=p2.match(line)
            if m:
                groups = m.groupdict()
                site = groups['site']
                instance_id_dict.update({'site':site})
                continue

            #Host Address:         192.168.1.71/32
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                host_address = groups['host_address']
                host_address_dict = instance_id_dict.setdefault('host_address',{})\
                                                    .setdefault(host_address,{})
                continue

            #Hardware Address:     aabb.cc00.c901
            m=p4.match(line)
            if m:
                groups = m.groupdict()
                hardware_address = groups['hardware_address']
                host_address_dict.update({'hardware_address':hardware_address})
                continue

            #First registered:     1w0d
            m=p5.match(line)
            if m:
                groups = m.groupdict()
                first_registered = groups['first_registered']
                host_address_dict.update({'first_registered':first_registered})
                continue

            #Last registered:      1w0d
            m=p6.match(line)
            if m:
                groups = m.groupdict()
                last_registered = groups['last_registered']
                host_address_dict.update({'last_registered':last_registered})
                continue

            #Authentication failures:   0
            m = p7.match(line)
            if m:
                groups = m.groupdict()
                authentication_failures = int(groups['authentication_failures'])
                authentication_dict = host_address_dict.setdefault('registration_errors',{})\
                                                       .setdefault('authentication_failures',authentication_failures)
                continue

            #ETR 11.11.11.11:28966
            m = p8.match(line)
            if m:
                groups = m.groupdict()
                etr = groups['etr']
                port = int(groups['port'])
                etr_dict = host_address_dict.setdefault('etr',{})\
                                            .setdefault(etr,{})
                etr_dict.update({'port':port})
                continue
            #Last registered:      1w0d
            m=p9.match(line)
            if m:
                groups = m.groupdict()
                etr_last_registered = groups['etr_last_registered']
                etr_dict.update({'last_registered':etr_last_registered})
                continue

            #TTL:                   1d00h
            m=p10.match(line)
            if m:
                groups = m.groupdict()
                ttl = groups['ttl']
                etr_dict.update({'ttl':ttl})
                continue

            #xTR-ID:                0xC25C9262-0xC9865A33-0x008E8A37-0x9206AC33
            m=p11.match(line)
            if m:
                groups = m.groupdict()
                xtr_id = groups['xtr_id']
                etr_dict.update({'xtr_id':xtr_id})
                continue

            #Site-ID:               unspecified
            m=p12.match(line)
            if m:
                groups = m.groupdict()
                site_id = groups['site_id']
                etr_dict.update({'site_id':site_id})
                continue

            #Registered addr:       aabb.cc00.c901
            m=p13.match(line)
            if m:
                groups = m.groupdict()
                registered_addr = groups['registered_addr']
                etr_dict.update({'registered_addr':registered_addr})
                continue

            #L3 Instance ID:        4100
            m=p14.match(line)
            if m:
                groups = m.groupdict()
                l3_instance_id = int(groups['l3_instance_id'])
                etr_dict.update({'l3_instance_id':l3_instance_id})
        return ret_dict




# ==========================================
# Parser for: show lisp {lisp_id} instance-id
# {id} {address-family} database {prefix}
# ==========================================
class ShowLispDatabaseEidSchema(MetaParser):
    schema = {
        'lisp_id': {
            int: { # lisp id
                'instance_id': {
                    int: { # instance id
                        'address_family': str,
                        'eid_table': str,
                        'lsb': str,
                        'entries_total': int,
                        'no_route_entries': int,
                        'inactive_entries': int,
                        'do_not_register_entries': int,
                        'all_no_route': bool,
                        'eid_prefix': str,
                        'eid_info': str,
                        Optional('route_map'): str,
                        'domain_id': str,
                        Optional('metric'): str,
                        'srvc_ins_type': str,
                        'srvc_ins_id': int,
                        Optional('extranet_iid'): int,
                        Optional('sgt'): int,
                        'locators': {
                            str: { # locator address
                                Optional('priority'): int,
                                Optional('weight'): int,
                                Optional('source'): str,
                                Optional('state'): str,
                                'config_missing': bool
                            }
                        },
                        'map_servers': {
                            str: { # map-server address
                                'uptime': str,
                                'ack': str,
                                'domain_id': str
                            }
                        }
                    }
                }
            }
        }
    }


class ShowLispDatabaseEid(ShowLispDatabaseEidSchema):
    cli_command = ['show lisp instance-id {instance_id} {address_family} database {prefix}',
                   'show lisp {lisp_id} instance-id {instance_id} {address_family} database {prefix}',
                   'show lisp locator-table {rloc_vrf} instance-id {instance_id} {address_family} database {prefix}',
                   'show lisp locator-table vrf {rloc_vrf} instance-id {instance_id} {address_family} database {prefix}',
                   'show lisp eid-table {eid_vrf} {address_family} database {prefix}',
                   'show lisp eid-table vrf {eid_vrf} {address_family} database {prefix}',
                   'show lisp eid-table vlan {vlan_id} ethernet database {prefix}']

    def cli(self, lisp_id=None, instance_id=None, address_family=None, prefix=None, rloc_vrf=None, eid_vrf=None, vlan_id=None, output=None):
        if output is None:
            if lisp_id and instance_id:
                cmd = self.cli_command[1].format(lisp_id=lisp_id, instance_id=instance_id, address_family=address_family, prefix=prefix)
            elif rloc_vrf and instance_id:
                cmd = self.cli_command[2].format(rloc_vrf=rloc_vrf, instance_id=instance_id, address_family=address_family, prefix=prefix)
            elif eid_vrf:
                cmd = self.cli_command[4].format(eid_vrf=eid_vrf, address_family=address_family, prefix=prefix)
            elif vlan_id:
                cmd = self.cli_command[6].format(vlan_id=vlan_id, prefix=prefix)
            else:
                cmd = self.cli_command[0].format(instance_id=instance_id, address_family=address_family, prefix=prefix)
            output = self.device.execute(cmd)

        lisp_id_dict = {}

        #LISP ETR IPv4 Mapping Database for EID-table vrf red (IID 101), LSBs: 0x0
        #LISP ETR MAC Mapping Database for EID-table Vlan 111 (IID 102), LSBs: 0x1
        #LISP ETR IPv4 Mapping Database for LISP 1 EID-table vrf red (IID 101), LSBs: 0x0
        #LISP ETR MAC Mapping Database for LISP 1 EID-table Vlan 111 (IID 102), LSBs: 0x1
        p1 = re.compile(r"^LISP\sETR\s(?P<address_family>[A-Za-z0-9]+)\sMapping\sDatabase\sfor(\sLISP\s)?(?P<lisp_id>\d)?\sEID-table\s(?P<eid_table>(vrf\s\w+)|(Vlan\s\d+))\s\(IID\s(?P<instance_id>\d+)\),\sLSBs:\s(?P<lsb>0x[a-fA-F\d]+)$")

        #Entries total 2, no-route 2, inactive 0, do-not-register 0
        p2 = re.compile(r"^Entries total\s(?P<entries_total>\d+),\sno-route\s(?P<no_route_entries>\d+),\sinactive\s(?P<inactive_entries>\d+),\sdo-not-register\s(?P<do_not_register_entries>\d+)$")

        #*** ALL ACTIVE LOCAL EID PREFIXES HAVE NO ROUTE ***
        #***    REPORTING LOCAL RLOCS AS UNREACHABLE     ***
        p3 = re.compile(r"^(?P<all_no_route>\*\*\* ALL ACTIVE LOCAL EID PREFIXES HAVE NO ROUTE \*\*\*)")

        #192.168.1.0/24, locator-set RLOC *** NO ROUTE TO EID PREFIX ***
        #00aa.00bb.00cc/48, locator-set RLOC
        p4 = re.compile(r"^(?P<eid_prefix>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2})|([a-fA-F\d\:]+\/\d{1,3})|(([a-fA-F\d]{4}\.){2}[a-fA-F\d]{4}\/\d{1,2})),\s(?P<eid_info>.+)$")

        #  Uptime: 00:00:56, Last-change: 00:00:56
        # Line not parsed, not interesting data for now

        #  Route-map: match-metric
        p5 = re.compile(r"^Route-map:\s(?P<route_map>.+)$")

        #  Domain-ID: unset
        p6 = re.compile(r"^Domain-ID:\s(?P<domain_id>.+)$")

        #  Metric: -
        p7 = re.compile(r"^Metric:\s(?P<metric>.+)$")

        #  Service-Insertion: N/A (0)
        p8 = re.compile(r"^Service-Insertion:\s(?P<srvc_ins_type>[^\s]+)\s\((?P<srvc_ins_id>\d+)\)$")

        #  Extranet-IID: 4100
        p9 = re.compile(r"^Extranet-IID:\s(?P<extranet_iid>\d+)$")

        # SGT: 10
        p10 = re.compile(r"^SGT:\s(?P<sgt>\d+)$")

        #  Locator       Pri/Wgt  Source     State
        #  100.31.31.31    1/1    cfg-addr   site-self, unreachable
        #  100.44.44.44 *** missing in configuration ***
        p11 = re.compile(r"^(?P<locator>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|([a-fA-F\d\:]+))\s+(?P<priority>\d+)\/(?P<weight>\d+)\s+(?P<source>[\w-]+)\s+(?P<state>.+)$")
        p12 = re.compile(r"^(?P<locator>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|([a-fA-F\d\:]+))\s(?P<config_missing>\*\*\* missing in configuration \*\*\*)$")

        #  Map-server       Uptime         ACK  Domain-ID
        #  100.31.31.31     00:00:21       No   0
        #  100.31.31.31     never          No   0
        p13 = re.compile(r"^(?P<map_server>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|([a-fA-F\d\:]+))\s+(?P<uptime>(\d{2}:\d{2}:\d{2})|never)\s+(?P<ack>Yes|No)\s+(?P<domain_id>\w+)")

        for line in output.splitlines():
            line = line.strip()

            #LISP ETR IPv4 Mapping Database for EID-table vrf red (IID 101), LSBs: 0x0
            #LISP ETR MAC Mapping Database for EID-table Vlan 111 (IID 102), LSBs: 0x1
            #LISP ETR IPv4 Mapping Database for LISP 1 EID-table vrf red (IID 101), LSBs: 0x0
            #LISP ETR MAC Mapping Database for LISP 1 EID-table Vlan 111 (IID 102), LSBs: 0x1
            m=p1.match(line)
            if m:
                groups = m.groupdict()
                if 'lisp_id' in groups and groups['lisp_id'] is not None:
                    lisp_id = int(groups['lisp_id'])
                else:
                    lisp_id = 0

                instance_id = int(groups['instance_id'])
                instance_id_dict = lisp_id_dict.setdefault('lisp_id', {}) \
                                                .setdefault(lisp_id, {}) \
                                                .setdefault('instance_id', {}) \
                                                .setdefault(instance_id, {})

                instance_id_dict['address_family'] = groups['address_family']
                instance_id_dict['eid_table'] = groups['eid_table']
                instance_id_dict['lsb'] = groups['lsb']
                instance_id_dict['all_no_route'] = False # default value
                continue

            #Entries total 2, no-route 2, inactive 0, do-not-register 0
            m=p2.match(line)
            if m:
                groups = m.groupdict()
                instance_id_dict['entries_total'] = int(groups['entries_total'])
                instance_id_dict['no_route_entries'] = int(groups['no_route_entries'])
                instance_id_dict['inactive_entries'] = int(groups['inactive_entries'])
                instance_id_dict['do_not_register_entries'] = int(groups['do_not_register_entries'])
                continue

            #*** ALL ACTIVE LOCAL EID PREFIXES HAVE NO ROUTE ***
            #***    REPORTING LOCAL RLOCS AS UNREACHABLE     ***
            m=p3.match(line)
            if m:
                instance_id_dict['all_no_route'] = True
                continue

            #192.168.1.0/24, locator-set RLOC *** NO ROUTE TO EID PREFIX ***
            #00aa.00bb.00cc/48, locator-set RLOC
            m=p4.match(line)
            if m:
                groups = m.groupdict()
                instance_id_dict['eid_prefix'] = groups['eid_prefix']
                instance_id_dict['eid_info'] = groups['eid_info']
                continue

            #  Route-map: match-metric
            m=p5.match(line)
            if m:
                groups = m.groupdict()
                instance_id_dict['route_map'] = groups['route_map']
                continue

            #  Domain-ID: unset
            m=p6.match(line)
            if m:
                groups = m.groupdict()
                instance_id_dict['domain_id'] = groups['domain_id']
                continue

            #  Metric: -
            m=p7.match(line)
            if m:
                groups = m.groupdict()
                instance_id_dict['metric'] = groups['metric']
                continue

            #  Service-Insertion: N/A (0)
            m=p8.match(line)
            if m:
                groups = m.groupdict()
                instance_id_dict['srvc_ins_type'] = groups['srvc_ins_type']
                instance_id_dict['srvc_ins_id'] = int(groups['srvc_ins_id'])
                continue

            #  Extranet-IID: 4100
            m=p9.match(line)
            if m:
                groups = m.groupdict()
                instance_id_dict['extranet_iid'] = int(groups['extranet_iid'])
                continue

            # SGT: 10
            m=p10.match(line)
            if m:
                groups = m.groupdict()
                instance_id_dict['sgt'] = int(groups['sgt'])
                continue

            #  Locator       Pri/Wgt  Source     State
            #  100.31.31.31    1/1    cfg-addr   site-self, unreachable
            m=p11.match(line)
            if m:
                groups = m.groupdict()
                locator = groups['locator']
                locator_dict = instance_id_dict.setdefault('locators', {}) \
                                               .setdefault(locator, {})

                locator_dict['priority'] = int(groups['priority'])
                locator_dict['weight'] = int(groups['weight'])
                locator_dict['source'] = groups['source']
                locator_dict['state'] = groups['state']
                locator_dict['config_missing'] = False
                continue

            #  100.44.44.44 *** missing in configuration ***
            m=p12.match(line)
            if m:
                groups = m.groupdict()
                locator = groups['locator']
                locator_dict = instance_id_dict.setdefault('locators', {}) \
                                               .setdefault(locator, {})
                locator_dict['config_missing'] = True
                continue

            #  Map-server       Uptime         ACK  Domain-ID
            #  100.31.31.31     00:00:21       No   0
            #  100.31.31.31     never          No   0
            m=p13.match(line)
            if m:
                groups = m.groupdict()
                map_server = groups['map_server']
                map_server_dict = instance_id_dict.setdefault('map_servers', {}) \
                                                  .setdefault(map_server, {})

                map_server_dict['uptime'] = groups['uptime']
                map_server_dict['ack'] = groups['ack']
                map_server_dict['domain_id'] = groups['domain_id']
                continue

        return lisp_id_dict


class ShowLispIpv4PublisherRlocSchema(MetaParser):

    ''' Schema for
     * show lisp {lisp_id} instance-id {instance_id} ipv4 publisher {publisher_id}
     * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 publisher {publisher_id}
     * show lisp instance-id {instance_id} ipv4 publisher {publisher_id}
     * show lisp eid-table {eid_table} ipv4 publisher {publisher_id}
     * show lisp eid-table vrf {vrf} ipv4 publisher {publisher_id}
     * show lisp eid-table vrf ipv4 publisher {publisher_id}
    '''

    schema = {
        "lisp_id": {
            int: {
                "instance_id": {
                    int: {
                        "address_family": str,
                        "eid_table": str,
                        "state": str,
                        "epoch": int,
                        "entries": int,
                        "eid_prefix": {
                            str: {
                                "eid_epoch": int,
                                "last_pub_time": str,
                                "ttl": str,
                                "eid_state": str,
                                "rloc_set": {
                                    str: {
                                        "priority": int,
                                        "weight": int,
                                        "rloc_state": str,
                                        "encap_iid": str,
                                    }
                                },
                            }
                        },
                    }
                }
            }
        }
    }



class ShowLispIpv4PublisherRloc(ShowLispIpv4PublisherRlocSchema):
    ''' Schema for
     * show lisp {lisp_id} instance-id {instance_id} ipv4 publisher {publisher_id}
     * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 publisher {publisher_id}
     * show lisp instance-id {instance_id} ipv4 publisher {publisher_id}
     * show lisp eid-table {eid_table} ipv4 publisher {publisher_id}
     * show lisp eid-table vrf {vrf} ipv4 publisher {publisher_id}
     * show lisp eid-table vrf ipv4 publisher {publisher_id}
    '''

    cli_command = [
        'show lisp {lisp_id} instance-id {instance_id} ipv4 publisher {publisher_id}',
        'show lisp locator-table {locator_table} instance-id {instance_id} ipv4 publisher {publisher_id}',
        'show lisp instance-id {instance_id} ipv4 publisher {publisher_id}',
        'show lisp eid-table {eid_table} ipv4 publisher {publisher_id}',
        'show lisp eid-table vrf {vrf} ipv4 publisher {publisher_id}',
        'show lisp eid-table vrf ipv4 publisher {publisher_id}',
    ]

    def cli(self, output=None, lisp_id=None, instance_id=None, publisher_id=None, locator_table=None,
            eid_table=None, vrf=None):

        if output is None:
            if lisp_id and instance_id and publisher_id:
                cmd = self.cli_command[0].format(lisp_id=lisp_id, instance_id=instance_id,\
                                                 publisher_id=publisher_id)

            elif locator_table and instance_id and publisher_id:
                cmd = self.cli_command[1].format(locator_table=locator_table, instance_id=instance_id,\
                                                 publisher_id=publisher_id)
            elif instance_id and publisher_id:
                cmd = self.cli_command[2].format(instance_id=instance_id, publisher_id=publisher_id)

            elif eid_table and publisher_id:
                cmd = self.cli_command[3].format(eid_table=eid_table, publisher_id=publisher_id)

            elif vrf and publisher_id:
                cmd = self.cli_command[4].format(vrf=vrf, publisher_id=publisher_id)

            else:
                cmd = self.cli_command[5].format(publisher_id=publisher_id)

            output = self.device.execute(cmd)

        # Initialize dictionary
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

        # LISP ETR IPv4 Publisher Table for EID-table vrf red (IID 4099)
        p2 = re.compile(r'^LISP\sETR\s(?P<address_family>\S+)\s+Publisher\sTable'\
                        r'\sfor\sEID-table\svrf\s(?P<eid_table>\S+).+$')

        # Publisher state: Established, Publisher epoch 0, Entries total 2
        p3 = re.compile(r'^Publisher\sstate:\s+(?P<state>\S+),\sPublisher\sepoch\s'\
                        r'(?P<epoch>\d+),\sEntries\stotal\s(?P<entries>\d+)$')

        # 0.0.0.0/0, Epoch: 0, Last Published: 5d22h
        p4 = re.compile(r'^(?P<eid_prefix>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2})'\
                        r',\sEpoch:\s(?P<eid_epoch>\d+),\sLast Published:\s+(?P<last_pub_time>.+)$')

        # TTL: never, State unknown-eid-forward
        p5 = re.compile(r'^TTL:\s(?P<ttl>\S+),\sState\s(?P<eid_state>\S+)$')

        # 203.203.203.203  255/10   up        -
        p6 = re.compile(r'^(?P<rloc_set>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(?P<priority>\d+)\/'\
                        r'(?P<weight>\d+)\s+(?P<rloc_state>\S+)\s+(?P<encap_iid>\S+)$')


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

            # LISP ETR IPv4 Publisher Table for EID-table vrf red (IID 4099)
            m = p2.match(line)
            if m:
                group = m.groupdict()
                lisp_id_dict = \
                    ret_dict.setdefault('lisp_id', {})\
                        .setdefault(lisp_id, {})\
                        .setdefault('instance_id', {})\
                        .setdefault(instance_id, {})
                lisp_id_dict.update({
                    'address_family': group['address_family'],
                    'eid_table': group['eid_table']
                })
                continue

            # Publisher state: Established, Publisher epoch 0, Entries total 2
            m = p3.match(line)
            if m:
                group = m.groupdict()
                lisp_id_dict.update({
                    'state': group['state'],
                    'epoch': int(group['epoch']),
                    'entries': int(group['entries'])
                })
                continue

            # 0.0.0.0/0, Epoch: 0, Last Published: 5d22h
            m = p4.match(line)
            if m:
                group = m.groupdict()
                eid_prefix_dict = lisp_id_dict.setdefault('eid_prefix', {})\
                                              .setdefault(group['eid_prefix'], {})
                eid_prefix_dict.update({
                    'eid_epoch': int(group['eid_epoch']),
                    'last_pub_time': group['last_pub_time']
                })
                continue

            # TTL: never, State unknown-eid-forward
            m = p5.match(line)
            if m:
                group = m.groupdict()
                eid_prefix_dict.update({
                    'ttl': group['ttl'],
                    'eid_state': group['eid_state']
                })
                continue

            # 203.203.203.203  255/10   up        -
            m = p6.match(line)
            if m:
                group = m.groupdict()
                rloc_set_dict = eid_prefix_dict.setdefault('rloc_set', {})\
                                               .setdefault(group['rloc_set'], {})
                rloc_set_dict.update({
                    'priority': int(group['priority']),
                    'weight': int(group['weight']),
                    'rloc_state': group['rloc_state'],
                    'encap_iid': group['encap_iid']
                })
                continue

        return ret_dict


class ShowLispSessionCapabilitySchema(MetaParser):

    ''' Schema for
        * show lisp vrf default session capability
        * show lisp vrf * session capability
    '''
    schema = {
        'vrf': {
            str: {
                'peer': {
                    str:
                        ListOf({
                            'port': int,
                            'tx_flags': str,
                            'rx_flags': str,
                            'rx_count': int,
                            'err_count': int
                        })
                    }
                }
            }
        }


class ShowLispSessionCapability(ShowLispSessionCapabilitySchema):
    """Parser for show lisp vrf {vrf} session capability"""
    cli_command = ['show lisp vrf {vrf} session capability']

    def cli(self, vrf=None, output=None):
        if output is None:
            if vrf:
                output = self.device.execute(self.cli_command[0].format(vrf=vrf))
        ret_dict = {}

        #Output for router lisp vrf red
        p1 = re.compile(r"^Output\s+for\s+router\s+lisp\s+vrf\s+(?P<vrf>\S+)$")

        #44.44.44.44:4342               0x1FF      0x1FF      1         0
        p2 = re.compile(r"^(?P<peer>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(?P<port>\d+)"
                        r"\s+(?P<tx_flags>\S+)\s+(?P<rx_flags>\S+)\s+(?P<rx_count>\d+)"
                        r"\s+(?P<err_count>\d+)$")
        for line in output.splitlines():
            line = line.strip()
            #Output for router lisp vrf red
            m=p1.match(line)
            if m:
                groups = m.groupdict()
                vrf = groups['vrf']
                vrf_dict = ret_dict.setdefault('vrf',{})\
                                   .setdefault(vrf,{})
                continue

            #44.44.44.44:4342               0x1FF      0x1FF      1         0
            m=p2.match(line)
            if m:
                if "vrf" not in ret_dict:
                    vrf_dict = ret_dict.setdefault('vrf',{})\
                                       .setdefault(vrf,{})
                groups = m.groupdict()
                peer = groups['peer']
                port = int(groups['port'])
                tx_flags = groups['tx_flags']
                rx_flags = groups['rx_flags']
                rx_count = int(groups['rx_count'])
                err_count = int(groups['err_count'])
                peer_dict = vrf_dict.setdefault('peer',{})
                peer_list = peer_dict.setdefault(peer, [])
                session_dict = {}
                session_dict.update({
                    'port': port,
                    'tx_flags': tx_flags,
                    'rx_flags': rx_flags,
                    'rx_count': rx_count,
                    'err_count': err_count})
                peer_list.append(session_dict)
        return ret_dict


class ShowLispSMRSchema(MetaParser):

    ''' Schema for
        * show lisp instance-id {instance_id} ipv4 smr
        * show lisp {lisp_id} instance-id {instance_id} ipv4 smr
        * show lisp eid-table {eid_table} ipv4 smr
        * show lisp eid-table vrf {vrf} ipv4 smr
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 smr
    '''

    schema = {
        'lisp_id': {
            int: {
                'instance_id': {
                    int: {
                        Optional('eid_table'): str,
                        'entries': int,
                        'prefix': {
                            str: { # EID prefix
                                'producer': list
                                }
                            }
                        }
                    }
                }
            }
        }


class ShowLispV4SMRParser(ShowLispSMRSchema):
    """
    Parser for
    * show lisp instance-id {instance_id} ipv4 smr
    * show lisp {lisp_id} instance-id {instance_id} ipv4 smr
    * show lisp eid-table {eid_table} ipv4 smr
    * show lisp eid-table vrf {vrf} ipv4 smr
    * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 smr
    """
    cli_command = ['show lisp instance-id {instance_id} ipv4 smr',
                   'show lisp {lisp_id} instance-id {instance_id} ipv4 smr',
                   'show lisp locator-table {locator_table} instance-id {instance_id} ipv4 smr'
                   #'show lisp eid-table {eid_table} ipv4 smr',
                   #'show lisp eid-table vrf {vrf} ipv4 smr',
                   ]

    def cli(self, lisp_id=None, instance_id=None, eid_table=None, vrf=None, locator_table=None, output=None):
        if output is None:
            if lisp_id and instance_id:
                output = self.device.execute(self.cli_command[1].format(lisp_id=lisp_id, instance_id=instance_id))
            elif locator_table and instance_id:
                output = self.device.execute(self.cli_command[2].format(locator_table=locator_table, instance_id=instance_id))
            else:
                output = self.device.execute(self.cli_command[0].format(instance_id=instance_id))
            """elif vrf:
                output = self.device.execute(self.cli_command[3].format(vrf=vrf))
            else:
                output = self.device.execute(self.cli_command[2].format(eid_table=eid_table))"""
        lisp_v4_smr = {}
        count = 0

        #Output for router lisp 0 instance-id 4100
        p1 = re.compile(r"^Output\s+for\s+router\s+lisp\s+(?P<lisp_id>\d+)"
                        r"\s+instance-id\s+(?P<instance_id>\d+)$")

        #LISP SMR Table for router lisp 0 (red) IID 4100
        p2 = re.compile(r"^LISP\s+SMR\s+Table\s+for\s+router\s+lisp\s+"
                        r"\d+\s+\((?P<eid_table>\S+)\)\s+IID\s+\d+")

        #Entries: 3
        p3 = re.compile(r"^Entries:\s+(?P<entries>\d+)")

        #192.168.1.0/24                          away table
        p4 = re.compile(r"^(?P<prefix>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
                        r"\/\d{1,2}|[a-fA-F\d\:]+\/\d{1,3})\s+"
                        r"(?P<producer>\w+\s\w+\,\s\w+\s\w+|\w+\s\w+|\w+)")

        #  Instance ID:                              4100
        p5 = re.compile(r"^\s+Instance\s+ID:\s+(?P<inst_id>\S+)")

        for line in output.splitlines():
            line = line.strip()
            count += 1
            #Output for router lisp 0 instance-id 4100
            m=p1.match(line)
            if m:
                groups = m.groupdict()
                lisp_id = int(groups['lisp_id'])
                instance_id = int(groups['instance_id'])
                lisp_id_dict = lisp_v4_smr.setdefault('lisp_id',{})\
                                          .setdefault(lisp_id,{})
                instance_id_dict = lisp_id_dict.setdefault('instance_id',{})\
                                              .setdefault(instance_id,{})
                continue
            if not m and count < 2 and lisp_id != "all" and line != "":
                if lisp_id and instance_id:
                    lisp_id = int(lisp_id)
                    lisp_id_dict = lisp_v4_smr.setdefault('lisp_id',{})\
                                              .setdefault(lisp_id,{})
                    instance_id = int(instance_id)
                    instance_id_dict = lisp_id_dict.setdefault('instance_id',{})\
                                                   .setdefault(instance_id,{})
                    count += 1
                    continue
                if not lisp_id and instance_id:
                    lisp_id = 0
                    lisp_id_dict = lisp_v4_smr.setdefault('lisp_id',{})\
                                              .setdefault(lisp_id,{})
                    if instance_id != "*":
                        instance_id = int(instance_id)
                        instance_id_dict = lisp_id_dict.setdefault('instance_id',{})\
                                                       .setdefault(instance_id,{})
                    count += 1
                    continue

            #LISP SMR Table for router lisp 0 (red) IID 4100
            m=p2.match(line)
            if m:
                groups = m.groupdict()
                eid_table = groups['eid_table']
                instance_id_dict.update({'eid_table':eid_table})
                continue

            #Entries: 3
            m=p3.match(line)
            if m:
                groups = m.groupdict()
                entries = int(groups['entries'])
                instance_id_dict.update({'entries':entries})
                continue

            #192.168.1.0/24                          away table
            m=p4.match(line)
            if m:
                groups = m.groupdict()
                prefix = groups['prefix']
                producer = groups['producer']
                prefix_dict = instance_id_dict.setdefault('prefix',{})\
                                          .setdefault(prefix,{})
                producer_list = prefix_dict.setdefault('producer',[])
                producer_list.append(producer)
                producer_list = producer_list[0].split(',')
                prefix_dict.update({'producer':producer_list})
        return lisp_v4_smr


class ShowLispV6SMRParser(ShowLispV4SMRParser):
    """
    Parser for
    * show lisp instance-id {instance_id} ipv6 smr
    * show lisp {lisp_id} instance-id {instance_id} ipv6 smr
    * show lisp eid-table {eid_table} ipv6 smr
    * show lisp eid-table vrf {vrf} ipv6 smr
    * show lisp locator-table {locator_table} instance-id {instance_id} ipv6 smr
    """
    cli_command = ['show lisp instance-id {instance_id} ipv6 smr',
                   'show lisp {lisp_id} instance-id {instance_id} ipv6 smr',
                   'show lisp locator-table {locator_table} instance-id {instance_id} ipv6 smr'
                   #'show lisp eid-table {eid_table} ipv6 smr',
                   #'show lisp eid-table vrf {vrf} ipv6 smr'
                   ]

    def cli(self, lisp_id=None, instance_id=None, eid_table=None, vrf=None, locator_table=None, output=None):
        if output is None:
            if lisp_id and instance_id:
                output = self.device.execute(self.cli_command[1].format(lisp_id=lisp_id, instance_id=instance_id))
            elif locator_table and instance_id:
                output = self.device.execute(self.cli_command[2].format(locator_table=locator_table, instance_id=instance_id))
            else:
                output = self.device.execute(self.cli_command[0].format(instance_id=instance_id))
            """elif vrf:
                output = self.device.execute(self.cli_command[3].format(vrf=vrf))
            else:
                output = self.device.execute(self.cli_command[2].format(eid_table=eid_table))"""
        return super().cli(lisp_id=lisp_id, instance_id=instance_id, eid_table=eid_table, vrf=vrf, locator_table=locator_table, output=output)
